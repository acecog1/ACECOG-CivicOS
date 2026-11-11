"""Governed engine for the ACECOG MVP.

Started as the behavioral mock behind the CL-041 contract and grown into the MVP core.
It keeps real state, enforces the rules the Phase 1 acceptance suite tests (MVP-100..111,
selected INV-AT, CMP, and UIX-NEUTRAL tests), and persists every governed transaction
atomically to a local SQLite store (store.py, spec 11.5). The clock is logical, so hashes
are reproducible; the solver is a small deterministic LP/QP behind the interface the
production solver will use (13.1).
"""
import copy, hashlib, json
import numpy as np
from scipy.optimize import linprog, minimize
import scipy
import jsonschema

from . import contract

UNCERTAIN = {"Estimated", "Assumed", "Scenario output", "Hypothesis"}
TIER_RANK = {"self_attested": 0, "verified": 1}
SOLVER_ID = f"scipy-{scipy.__version__}-highs"
PROTECTED_SETTINGS = {  # Assurance Controls (43.2) that no setting may disable
    "asr.identity_mfa": "ASR-01", "asr.operator_access_log": "ASR-02", "asr.encryption": "ASR-03",
    "asr.audit_log": "ASR-04", "asr.retention": "ASR-05", "asr.accessibility": "ASR-06",
    "asr.privacy": "ASR-07", "asr.legal_status_labels": "ASR-08", "asr.incident_response": "ASR-09",
    "asr.sbom": "ASR-10", "asr.export": "ASR-11",
}
ENGAGEMENT_SETTINGS = {"feed.ranking", "feed.delay", "feed.hide", "notifications.timing"}


def canon(o):
    return json.dumps(o, sort_keys=True, separators=(",", ":"), default=str)


def sha(o):
    return hashlib.sha256(canon(o).encode()).hexdigest()


class Refuse(Exception):
    def __init__(self, code, reason, invariant_id=None, control_id=None, conflicting_layer=None):
        super().__init__(reason)
        self.refusal = {"code": code, "reason": reason, "invariant_id": invariant_id,
                        "control_id": control_id, "conflicting_layer": conflicting_layer}


class Escalate(Exception):
    def __init__(self, escalation, result=None):
        super().__init__(escalation["governing_conflict"])
        self.escalation, self.result = escalation, result


class Engine:
    def __init__(self, store=None):
        self.events, self.seen, self.counters = [], {}, {}
        self.obj = {}        # id -> current version (dict)
        self.versions = {}   # id -> [versions]
        self.actors = {}     # actor_id -> {civic_body_id, display_name, roles}
        self._exports = {}
        self._txn = None
        self._validators = {}
        self.store = store
        if store is not None:
            self._load(store.load())

    @classmethod
    def open(cls, path):
        """Open (or create) a durable installation backed by one SQLite file (11.5)."""
        from .store import Store
        return cls(Store(path))

    def _load(self, st):
        ok, at = verify_chain(st["events"])
        if not ok:
            raise RuntimeError(f"event log hash chain broken at event {at}; refusing to start (ASR-04)")
        self.events, self.versions, self.seen = st["events"], st["versions"], st["commands"]
        self.obj = {k: v[-1] for k, v in self.versions.items()}
        self.actors, self.counters, self._exports = st["actors"], st["counters"], st["exports"]

    # ------------------------------------------------------------ plumbing
    def new_id(self, prefix):
        n = self.counters.get(prefix, 0) + 1
        self.counters[prefix] = n
        return f"{prefix}-{n:04d}"

    def emit(self, etype, data):
        prev = self.events[-1]["hash"] if self.events else "0" * 64
        ev = {"seq": len(self.events) + 1, "event_id": self.new_id("evt"), "type": etype,
              "transaction_id": self._txn["id"] if self._txn else None,
              "at": f"T+{len(self.events) + 1}", "data": copy.deepcopy(data), "prev_hash": prev}
        ev["hash"] = hashlib.sha256((prev + canon({k: v for k, v in ev.items() if k != "hash"})).encode()).hexdigest()
        self.events.append(ev)
        if self._txn:
            self._txn["events"].append(ev["event_id"])
        return ev

    def put(self, obj_type, data, civic_body_id, oid=None, authority_basis=None, supersedes=None):
        """Store a new immutable version. Prior versions are never altered (DPP-IMMUTABLE-001)."""
        oid = oid or self.new_id(obj_type)
        n = len(self.versions.get(oid, [])) + 1
        v = {"id": oid, "version_id": f"{oid}@v{n}", "object_type": obj_type, "civic_body_id": civic_body_id,
             "authority_basis": authority_basis, "supersedes": supersedes or (self.obj[oid]["version_id"] if oid in self.obj else None),
             "created_in_transaction": self._txn["id"] if self._txn else None, **copy.deepcopy(data)}
        self.versions.setdefault(oid, []).append(v)
        self.obj[oid] = v
        if self._txn:
            self._txn["versions"].append(v)
        self.emit(f"{obj_type}.versioned", {"id": oid, "version_id": v["version_id"]})
        return v

    def get(self, oid, kind=None):
        o = self.obj.get(oid)
        if o is None or (kind and o["object_type"] != kind):
            raise Refuse("NOT_FOUND", f"{kind or 'object'} {oid} not found")
        return o

    def of_type(self, kind, civic_body_id=None):
        return [o for o in self.obj.values() if o["object_type"] == kind and
                (civic_body_id is None or o["civic_body_id"] == civic_body_id)]

    # ---------------------------------------------------------- authority
    def actor(self, actor_id):
        a = self.actors.get(actor_id)
        if not a:
            raise Refuse("AUTHORITY_MISSING", f"unknown actor {actor_id}", "GOV-AUTHPATH-001")
        return a

    def require(self, actor_id, cb, action):
        """Every command independently re-checks authority (11.6.2, 23.1)."""
        self.actor(actor_id)
        for g in self.of_type("authority", cb):
            if g["grantee_actor_id"] == actor_id and not g.get("revoked") and (action in g["actions"] or "*" in g["actions"]):
                return g
        raise Refuse("AUTHORITY_MISSING", f"{actor_id} holds no authority for '{action}' in {cb}", "GOV-AUTHPATH-001")

    def credential(self, cb, actor_id):
        for c in self.of_type("membership_credential", cb):
            if c["member_actor_id"] == actor_id and not c.get("revoked"):
                return c
        return None

    def process(self, cb, version_id=None):
        procs = self.of_type("governance_process", cb)
        if not procs:
            raise Refuse("STATE", f"{cb} has no Governance Process", "GOV-AUTHPATH-001")
        if version_id:
            for v in self.versions[procs[0]["id"]]:
                if v["version_id"] == version_id:
                    return v
        return procs[0]

    def decision_class(self, cb, name, version_id=None):
        for dc in self.process(cb, version_id)["decision_classes"]:
            if dc["name"] == name:
                return dc
        raise Refuse("NOT_FOUND", f"decision class {name} not defined in the Governance Process")

    def legal_status(self, cb, decision_class):
        for d in self.of_type("legal_effect_declaration", cb):
            if d["decision_class"] == decision_class:
                return {"value": d["legal_status"], "legal_effect_declaration_id": d["id"],
                        "enabling_authority": d["enabling_authority"], "effective_date": d.get("effective_date")}
        return {"value": "Advisory", "legal_effect_declaration_id": None, "enabling_authority": None, "effective_date": None}

    def status(self, cb, decision_class, lifecycle, readiness="Not applicable", epistemic="Not applicable", legal=None):
        """Legal status is fixed when a decision closes; later declarations apply prospectively (8.9)."""
        return {"lifecycle_state": lifecycle, "legal_status": legal or self.legal_status(cb, decision_class),
                "delivery_readiness": readiness, "epistemic_class": epistemic}

    def pack_rule(self, cb, rule):
        return any(r["rule"] == rule for p in self.of_type("compliance_pack", cb) for r in p["rules"])

    def envelope(self, cb, decision_class):
        for e in self.of_type("delegation_envelope", cb):
            if e["decision_class"] == decision_class:
                return e
        return None

    def bind_versions(self, cb):
        if not cb:
            return {}
        b = {}
        for kind in ("governance_process", "delegation_envelope", "compliance_pack", "portfolio_model"):
            for o in self.of_type(kind, cb):
                b[o["id"]] = o["version_id"]
        return b

    # ------------------------------------------------------------ execute
    def validator(self, name):
        if name not in self._validators:
            self._validators[name] = jsonschema.Draft202012Validator(contract.P[name])
        return self._validators[name]

    def execute(self, name, envelope):
        """Run one command as a governed transaction (8.1)."""
        try:
            jsonschema.validate(envelope, contract.SCHEMAS["CommandEnvelope"])
            errs = sorted(self.validator(name).iter_errors(envelope["payload"]), key=str)
            if errs:
                raise jsonschema.ValidationError(errs[0].message)
        except (jsonschema.ValidationError, KeyError) as e:
            return {"transaction_id": None, "outcome": "refused", "event_ids": [], "result": None, "escalation": None,
                    "bound_versions": {}, "status": None,
                    "refusal": {"code": "SCHEMA", "reason": str(e).split("\n")[0], "invariant_id": None,
                                "control_id": None, "conflicting_layer": None}}
        key = envelope["command_id"]
        if key in self.seen:                       # idempotent replay creates nothing (8.1)
            return self.seen[key]
        pl = envelope["payload"]
        cb = pl.get("civic_body_id") or self._infer_cb(pl)
        self._txn = {"id": self.new_id("txn"), "events": [], "versions": [], "keep_on_refuse": False}
        ev_start, actors_before, exports_before = len(self.events), copy.deepcopy(self.actors), set(self._exports)
        bound = self.bind_versions(cb)
        res = {"transaction_id": self._txn["id"], "outcome": "accepted", "event_ids": [], "result": None,
               "refusal": None, "escalation": None, "bound_versions": bound, "status": None}
        try:
            if envelope["client"] == "assistant":
                hc = envelope.get("human_confirmation") or {}
                who = hc.get("confirmed_by")
                if not who or who not in self.actors or hc.get("reviewed_payload_hash") != sha(pl):
                    raise Refuse("AI_CONFIRMATION_REQUIRED",
                                 "a command drafted by the assistant needs a human's confirmation of the exact payload",
                                 "GOV-AUTHPATH-001", "AI-COMMIT-001")
            handler = getattr(self, "c_" + name.replace(".", "_").replace("-", "_"))
            out = handler(envelope["actor_id"], pl, bound, envelope)
            res["result"], res["status"] = out if isinstance(out, tuple) else (out, None)
            self.emit("command.accepted", {"command": name, "actor_id": envelope["actor_id"], "client": envelope["client"]})
        except Refuse as r:
            res["outcome"], res["refusal"] = "refused", r.refusal
            if not self._txn["keep_on_refuse"]:      # a refused command changes nothing but the record of its refusal (8.1)
                self._rollback(ev_start, actors_before)
            self.emit("command.refused", {"command": name, "actor_id": envelope["actor_id"], "refusal": r.refusal})
        except Escalate as e:
            res["outcome"], res["escalation"], res["result"] = "escalated", e.escalation, e.result
            self.emit("command.escalated", {"command": name, "actor_id": envelope["actor_id"], "escalation": e.escalation})
        res["event_ids"] = list(self._txn["events"])
        txn, self._txn = self._txn, None
        self.seen[key] = res
        if self.store is not None:
            try:
                self.store.commit(self.events[ev_start:], txn["versions"], key, res, self.actors, self.counters,
                                  {k: v for k, v in self._exports.items() if k not in exports_before})
            except Exception:
                self._load(self.store.load())        # memory never runs ahead of the durable record
                raise
        return res

    def _rollback(self, ev_start, actors_before):
        for v in reversed(self._txn["versions"]):
            lst = self.versions[v["id"]]
            lst.pop()
            if lst:
                self.obj[v["id"]] = lst[-1]
            else:
                del self.versions[v["id"]], self.obj[v["id"]]
        drop = {e["event_id"] for e in self.events[ev_start:]}
        del self.events[ev_start:]
        self._txn["versions"], self._txn["events"] = [], [e for e in self._txn["events"] if e not in drop]
        self.actors = actors_before

    def _infer_cb(self, pl):
        for k in ("proposition_id", "decision_id", "baseline_id", "exception_proposition_id", "constraint_id", "record_id"):
            if k in pl and pl[k] in self.obj:
                return self.obj[pl[k]]["civic_body_id"]
        return None

    # ------------------------------------------------------- governance
    def c_civic_bodies_create(self, actor_id, pl, bound, env):
        cbid = self.new_id("cb")
        cb = self.put("civic_body", {"name": pl["name"], "jurisdiction": pl.get("jurisdiction"),
                                     "gml_level": pl.get("gml_level", 0)}, cbid, oid=cbid)
        founding = ["adopt_process", "grant_authority", "adopt_envelope", "adopt_led", "adopt_pack",
                    "issue_credential", "close_decision", "adopt_retention", "configure", "export"]
        for m in pl["founding_members"]:
            self.actors[m["actor_id"]] = {"civic_body_id": cbid, "display_name": m["display_name"], "roles": m.get("roles", ["member"])}
            self.put("membership_credential", {"member_actor_id": m["actor_id"], "tier": "verified",
                                               "attestation_confidence": 1.0}, cbid, authority_basis="founding charter")
        if actor_id not in self.actors:
            raise Refuse("AUTHORITY_MISSING", "the creating actor must be a founding member", "GOV-AUTHPATH-001")
        self.put("authority", {"grantee_actor_id": actor_id, "actions": founding, "monitoring_role": False},
                 cbid, authority_basis="founding charter")
        return {"civic_body": cb}

    def c_governance_processes_adopt(self, actor_id, pl, bound, env):
        cb = pl["civic_body_id"]
        self.require(actor_id, cb, "adopt_process")
        self._check_classes(pl["decision_classes"])
        existing = self.of_type("governance_process", cb)
        return {"governance_process": self.put("governance_process", {"decision_classes": pl["decision_classes"]}, cb,
                                               oid=existing[0]["id"] if existing else None, authority_basis=actor_id)}

    @staticmethod
    def _check_classes(classes):
        """Validation shared by adoption and by change control, so a change cannot bypass it."""
        for dc in classes:
            if dc.get("participation_fee", 0) > 0:
                raise Refuse("PARTICIPATION_FEE", f"decision class {dc['name']} charges a fee to take part",
                             "TRU-ACCESS-001", conflicting_layer="Invariant Floor")
            dc.setdefault("quorum", 0.5)
            dc.setdefault("min_attestation_confidence", 0.75)
            dc.setdefault("delegation_disclosure_threshold", 0.05)
            dc.setdefault("delegation_reconfirm_days", 365)

    def _approval(self, decision_id, rtype, subject, used, what):
        """G-054: an approval authorizes only the subject it approved, once (the CL-046 pattern).
        `subject` holds the requested_action fields that must match; `used` says whether it was already spent."""
        d = self.obj.get(decision_id or "")
        if not d or d["object_type"] != "decision" or d["result"] != "approved":
            return None
        ra = d.get("requested_action") or {}
        if ra.get("type") != rtype or any(ra.get(k) != v for k, v in subject.items()):
            raise Refuse("APPROVAL_MISMATCH", f"decision {d['id']} did not approve this {what} (it approved '{ra.get('type')}')",
                         "GOV-AUTHPATH-001")
        if used(d["id"]):
            raise Refuse("APPROVAL_ALREADY_USED", f"decision {d['id']} has already been used for its {what}", "GOV-AUTHPATH-001")
        return d

    def c_authorities_grant(self, actor_id, pl, bound, env):
        cb = pl["civic_body_id"]
        self.require(actor_id, cb, "grant_authority")
        if pl["grantee_actor_id"] not in self.actors:
            raise Refuse("NOT_FOUND", f"unknown grantee {pl['grantee_actor_id']}")
        if pl.get("monitoring_role"):
            if pl["grantee_actor_id"] == actor_id:
                raise Refuse("SELF_APPOINTMENT", "an approval or monitoring role cannot be self-appointed", "TRU-MONITOR-001")
            if self.get(cb)["gml_level"] >= 1:
                d = self._approval(pl.get("selected_by_decision_id"), "appoint",
                                   {"grantee_actor_id": pl["grantee_actor_id"], "actions": pl["actions"]},
                                   lambda did: any(g.get("selected_by_decision_id") == did for g in self.of_type("authority", cb)),
                                   "appointment")
                if not d:
                    raise Refuse("SELF_APPOINTMENT", "at GML-1+ a monitoring role is selected through the Governance Process", "TRU-MONITOR-001")
                if not pl.get("rotation_terms"):
                    raise Refuse("SELF_APPOINTMENT", "a monitoring role must record rotation and recall terms", "TRU-MONITOR-001")
        # G-055: authority comes from someone else, and never as an open-ended "*" after founding
        if pl["grantee_actor_id"] == actor_id:
            raise Refuse("SELF_GRANT", "an actor cannot grant authority to themselves", "GOV-AUTHPATH-001")
        if "*" in pl["actions"]:
            raise Refuse("WILDCARD_GRANT", "authority is granted as named actions; '*' is not grantable after founding", "GOV-AUTHPATH-001")
        return {"authority": self.put("authority", {k: pl.get(k) for k in ("grantee_actor_id", "actions", "monitoring_role", "selected_by_decision_id", "rotation_terms")},
                                      cb, authority_basis=actor_id)}

    def c_delegation_envelopes_adopt(self, actor_id, pl, bound, env):
        cb = pl["civic_body_id"]
        self.require(actor_id, cb, "adopt_envelope")
        self.decision_class(cb, pl["decision_class"])
        data = {"decision_class": pl["decision_class"], "tolerance": pl["tolerance"],
                "confidence_threshold": pl.get("confidence_threshold", 0.90),
                "min_reversibility": pl.get("min_reversibility", 2),
                "authorized_resolver": pl.get("authorized_resolver")}
        data["valid"], data["validation_errors"] = self._validate_envelope(data)
        ex = self.envelope(cb, pl["decision_class"])
        e = self.put("delegation_envelope", data, cb, oid=ex["id"] if ex else None, authority_basis=actor_id)
        return {"delegation_envelope": e, "autonomous_resolution": "enabled" if e["valid"] else "disabled"}

    @staticmethod
    def _validate_envelope(e):
        errs = []
        ct, mr = e.get("confidence_threshold"), e.get("min_reversibility")
        if not isinstance(ct, (int, float)) or isinstance(ct, bool) or not 0 <= ct <= 1:
            errs.append("confidence_threshold must be a number from 0 to 1")
        if not isinstance(mr, int) or isinstance(mr, bool) or not 0 <= mr <= 3:
            errs.append("min_reversibility must be an integer from 0 to 3")
        if not isinstance(e.get("tolerance"), (int, float)) or e["tolerance"] < 0:
            errs.append("tolerance must be a non-negative number")
        return (not errs), errs

    def c_legal_effect_declarations_adopt(self, actor_id, pl, bound, env):
        cb = pl["civic_body_id"]
        self.require(actor_id, cb, "adopt_led")
        self.decision_class(cb, pl["decision_class"])
        return {"legal_effect_declaration": self.put("legal_effect_declaration", {k: pl.get(k) for k in
                ("decision_class", "legal_status", "enabling_authority", "effective_date")}, cb, authority_basis=actor_id)}

    def c_compliance_packs_adopt(self, actor_id, pl, bound, env):
        cb = pl["civic_body_id"]
        self.require(actor_id, cb, "adopt_pack")
        for r in pl["rules"]:
            if r["effect"] == "relax":
                raise Refuse("LAYER_RULE", f"pack rule '{r['rule']}' would relax a higher-layer requirement",
                             "GOV-FRAMEWORK-001", conflicting_layer=r.get("target") or "Assurance Controls")
            if r.get("target") == "participation" and not r.get("legal_basis"):
                raise Refuse("LAYER_RULE", f"participation-restricting rule '{r['rule']}' must cite the law that compels it (43.4)",
                             "GOV-FRAMEWORK-001", conflicting_layer="Invariant Floor")
        return {"compliance_pack": self.put("compliance_pack", {k: pl[k] for k in ("pack_id", "edition", "rules")}, cb, authority_basis=actor_id)}

    def c_credentials_issue(self, actor_id, pl, bound, env):
        cb = pl["civic_body_id"]
        self.require(actor_id, cb, "issue_credential")
        mid = pl["member_actor_id"]
        self.actors.setdefault(mid, {"civic_body_id": cb, "display_name": mid, "roles": ["member"]})
        old = self.credential(cb, mid)
        return {"membership_credential": self.put("membership_credential", {"member_actor_id": mid, "tier": pl["tier"],
                "attestation_confidence": pl.get("attestation_confidence", 1.0 if pl["tier"] == "verified" else 0.6)},
                cb, oid=old["id"] if old else None, authority_basis=actor_id)}

    def c_interest_declarations_record(self, actor_id, pl, bound, env):
        cb = pl["civic_body_id"]
        self.actor(actor_id)
        self.get(pl["proposition_id"], "proposition")
        return {"interest_declaration": self.put("interest_declaration", {"person_id": actor_id, "proposition_id": pl["proposition_id"],
                "description": pl["description"], "recusal_status": "recused"}, cb, authority_basis=actor_id)}

    def recused(self, cb, actor_id, pid):
        return any(d["person_id"] == actor_id and d["proposition_id"] == pid for d in self.of_type("interest_declaration", cb))

    def c_delegations_assign(self, actor_id, pl, bound, env):
        cb = pl["civic_body_id"]
        if not self.credential(cb, actor_id):
            raise Refuse("ELIGIBILITY", "only members may delegate", "TRU-ELIG-001")
        dc = self.decision_class(cb, pl["decision_class"])
        tgt = pl["delegate_actor_id"]
        if tgt == actor_id or not self.credential(cb, tgt):
            raise Refuse("STATE", "delegate must be another member")
        if self._delegate_of(cb, tgt, pl["decision_class"]) == actor_id:
            raise Refuse("STATE", "delegation loop (17.7)")
        seq = len(self.events)
        return {"delegation": self.put("delegation", {"principal": actor_id, "delegate": tgt, "decision_class": pl["decision_class"],
                "assigned_at_seq": seq, "reconfirm_by_day": dc["delegation_reconfirm_days"], "active": True}, cb,
                oid=self._delegation_id(cb, actor_id, pl["decision_class"]), authority_basis=actor_id)}

    def c_delegations_revoke(self, actor_id, pl, bound, env):
        cb = pl["civic_body_id"]
        did = self._delegation_id(cb, actor_id, pl["decision_class"])
        if not did:
            raise Refuse("NOT_FOUND", "no delegation to revoke")
        d = self.obj[did]
        return {"delegation": self.put("delegation", {**{k: d[k] for k in ("principal", "delegate", "decision_class", "assigned_at_seq", "reconfirm_by_day")},
                "active": False}, cb, oid=did, authority_basis=actor_id)}

    def _delegation_id(self, cb, principal, dclass):
        for d in self.of_type("delegation", cb):
            if d["principal"] == principal and d["decision_class"] == dclass:
                return d["id"]
        return None

    def _delegate_of(self, cb, principal, dclass):
        for d in self.of_type("delegation", cb):
            if d["principal"] == principal and d["decision_class"] == dclass and d["active"]:
                return d["delegate"]
        return None

    # ---------------------------------------------------- propositions
    def _eligible(self, cb, actor_id, dc):
        c = self.credential(cb, actor_id)
        if not c:
            raise Refuse("ELIGIBILITY", f"{actor_id} holds no valid Membership Credential", "TRU-ELIG-001")
        if TIER_RANK[c["tier"]] < TIER_RANK[dc["min_attestation"]]:
            raise Refuse("ATTESTATION_TIER", f"decision class {dc['name']} requires tier '{dc['min_attestation']}'; {actor_id} holds '{c['tier']}'",
                         "TRU-ELIG-001", "17.5")
        return c

    def c_propositions_submit(self, actor_id, pl, bound, env):
        cb = pl["civic_body_id"]
        dc = self.decision_class(cb, pl["decision_class"])
        self._eligible(cb, actor_id, dc)
        proc = self.process(cb)
        p = self.put("proposition", {"decision_class": pl["decision_class"], "title": pl["title"], "body": pl["body"],
                     "requested_action": pl["requested_action"], "competes_with": pl.get("competes_with"),
                     "proposer": actor_id, "client": env["client"], "bound_process_version": proc["version_id"],
                     "state": "Proposed"}, cb, authority_basis=f"{proc['version_id']}:{dc['name']}")
        return {"proposition": p}, self.status(cb, pl["decision_class"], "Proposed")

    def c_propositions_amend(self, actor_id, pl, bound, env):
        p = self.get(pl["proposition_id"], "proposition")
        if p["state"] != "Proposed":
            raise Refuse("STATE", "only an open proposition can be amended")
        if p["proposer"] != actor_id:
            raise Refuse("AUTHORITY_MISSING", "only the proposer can amend", "GOV-AUTHPATH-001")
        data = {k: v for k, v in p.items() if k not in ("id", "version_id", "object_type", "civic_body_id", "authority_basis", "supersedes", "created_in_transaction")}
        data["body"] = pl["body"]
        if "requested_action" in pl:
            data["requested_action"] = pl["requested_action"]
        return {"proposition": self.put("proposition", data, p["civic_body_id"], oid=p["id"], authority_basis=actor_id),
                "note": "material amendment: votes on the earlier version no longer count (8.4)"}

    def c_deliberation_post(self, actor_id, pl, bound, env):
        p = self.get(pl["proposition_id"], "proposition")
        cb = p["civic_body_id"]
        if not self.credential(cb, actor_id):
            raise Refuse("ELIGIBILITY", "only members post to the deliberation record", "TRU-ELIG-001")
        if self.recused(cb, actor_id, p["id"]):
            raise Refuse("RECUSED", f"{actor_id} declared an interest in {p['id']}", None, "CMP-004")
        if pl["visibility"] == "private" and self.pack_rule(cb, "open_meeting_guard"):
            raise Refuse("OPEN_MEETING_GUARD", "member-to-member private deliberation on an in-jurisdiction item is not allowed under the adopted pack",
                         None, "CMP-003")
        return {"post": self.put("deliberation_post", {"proposition_id": p["id"], "proposition_version_id": p["version_id"],
                "author": actor_id, "text": pl["text"], "visibility": pl["visibility"], "to_actor_id": pl.get("to_actor_id"),
                "position": pl.get("position", "comment")}, cb, authority_basis=actor_id)}

    def c_votes_cast(self, actor_id, pl, bound, env):
        p = self.get(pl["proposition_id"], "proposition")
        cb = p["civic_body_id"]
        if p["state"] != "Proposed":
            raise Refuse("STATE", "voting is closed")
        dc = self.decision_class(cb, p["decision_class"], p["bound_process_version"])
        self._eligible(cb, actor_id, dc)
        if self.recused(cb, actor_id, p["id"]):
            raise Refuse("RECUSED", f"{actor_id} declared an interest in {p['id']}", None, "CMP-004")
        vid = self._vote_id(cb, actor_id, p["id"])
        return {"vote": self.put("vote", {"proposition_id": p["id"], "proposition_version_id": p["version_id"], "voter": actor_id,
                "choice": pl["choice"]}, cb, oid=vid, authority_basis=p["bound_process_version"])}

    def _vote_id(self, cb, voter, pid):
        for v in self.of_type("vote", cb):
            if v["voter"] == voter and v["proposition_id"] == pid:
                return v["id"]
        return None

    def c_decisions_close(self, actor_id, pl, bound, env):
        p = self.get(pl["proposition_id"], "proposition")
        cb = p["civic_body_id"]
        self.require(actor_id, cb, "close_decision")
        if p["state"] != "Proposed":
            raise Refuse("STATE", "decision already closed")
        dc = self.decision_class(cb, p["decision_class"], p["bound_process_version"])   # version binding (8.9)
        eligible = [c["member_actor_id"] for c in self.of_type("membership_credential", cb)
                    if not c.get("revoked") and TIER_RANK[c["tier"]] >= TIER_RANK[dc["min_attestation"]]]
        votes = {v["voter"]: v for v in self.of_type("vote", cb)
                 if v["proposition_id"] == p["id"] and v["proposition_version_id"] == p["version_id"] and v["voter"] in eligible}
        counted = {}
        for m in eligible:
            if m in votes:
                counted[m] = (votes[m]["choice"], "direct")
            else:
                d = self._delegate_of(cb, m, p["decision_class"])
                if d in votes:
                    counted[m] = (votes[d]["choice"], f"delegated to {d}")
        if len(counted) > len(eligible):
            raise Refuse("ELIGIBILITY", "participating count exceeds valid credentials", "TRU-ELIG-001")
        choices = [c for c, _ in counted.values()]
        participation = len(counted) / max(len(eligible), 1)
        if dc["method"] == "consent":
            approved = "object" not in choices and participation >= dc["quorum"]
        else:
            yes, no = choices.count("yes"), choices.count("no")
            approved = participation >= dc["quorum"] and (yes + no) > 0 and yes / (yes + no) >= dc["approval_threshold"]
        low_conf = any(self.credential(cb, m)["attestation_confidence"] < dc["min_attestation_confidence"] for m in counted)
        minority = [{"voter": m, "choice": c} for m, (c, _) in counted.items() if c in ("no", "object")]
        minority += [{"author": x["author"], "text": x["text"]} for x in self.of_type("deliberation_post", cb)
                     if x["proposition_id"] == p["id"] and x["position"] in ("object", "minority_report")]
        decision = self.put("decision", {
            "proposition_id": p["id"], "proposition_version_id": p["version_id"], "decision_class": p["decision_class"],
            "result": "approved" if approved else "rejected",
            "tally": {"eligible": len(eligible), "participating": len(counted), "quorum_met": participation >= dc["quorum"],
                      "choices": {c: choices.count(c) for c in sorted(set(choices))},
                      "basis": {m: how for m, (_, how) in sorted(counted.items())}},
            "minority_positions": minority, "low_confidence": low_conf,
            "process_version_id": p["bound_process_version"], "requested_action": p["requested_action"],
            "lifecycle_state": "Approved" if approved else "Rejected",
            "legal_status": self.legal_status(cb, p["decision_class"])}, cb, authority_basis=p["bound_process_version"])
        pdata = {k: v for k, v in p.items() if k not in ("id", "version_id", "object_type", "civic_body_id", "authority_basis", "supersedes", "created_in_transaction")}
        pdata["state"] = "Decided"
        self.put("proposition", pdata, cb, oid=p["id"], authority_basis=decision["id"])
        out = {"decision": decision}
        if approved and p["requested_action"].get("type") == "adopt_portfolio_model":
            out["portfolio_model"] = self._adopt_model(cb, p["requested_action"]["model"], decision["id"])
        return out, self.status(cb, p["decision_class"], decision["lifecycle_state"], legal=decision["legal_status"])

    # ---------------------------------------------------------- model
    def _adopt_model(self, cb, model, decision_id):
        for c in model.get("constraints", []):
            c.setdefault("kind", "hard")
        ex = self.of_type("portfolio_model", cb)
        return self.put("portfolio_model", model, cb, oid=ex[0]["id"] if ex else None, authority_basis=decision_id)

    def c_evidence_record(self, actor_id, pl, bound, env):
        cb = pl["civic_body_id"]
        if not self.credential(cb, actor_id):
            raise Refuse("ELIGIBILITY", "only members record evidence")
        return {"evidence": self.put("evidence", {k: pl.get(k) for k in ("subject", "value", "epistemic_class", "confidence", "source")},
                                     cb, authority_basis=actor_id)}

    def c_constraints_attach_evidence(self, actor_id, pl, bound, env):
        ev = self.get(pl["evidence_id"], "evidence")
        cb = ev["civic_body_id"]
        if ev["epistemic_class"] in UNCERTAIN:
            d = self._approval(pl.get("adopted_by_decision_id"), "adopt_evidence",
                               {"evidence_id": ev["id"], "constraint_id": pl["constraint_id"]},
                               lambda did: any(x.get("adopted_by_decision_id") == did for x in self.of_type("constraint_basis", cb)),
                               "evidence adoption")
            if not d:
                raise Refuse("EVIDENCE_NOT_ADOPTED", f"evidence classed '{ev['epistemic_class']}' cannot become a binding constraint until a decision adopts it",
                             "EVD-NORM-001")
        return {"constraint_basis": self.put("constraint_basis", {"constraint_id": pl["constraint_id"], "evidence_id": ev["id"],
                "adopted_by_decision_id": pl.get("adopted_by_decision_id")}, cb, authority_basis=pl.get("adopted_by_decision_id") or actor_id)}

    def solve(self, model, q=None, exclude=None):
        """Phase 1 solver profile: deterministic LP, or convex QP when Q is supplied (13.1)."""
        nodes = model["nodes"]
        n = len(nodes)
        idx = {nd["id"]: i for i, nd in enumerate(nodes)}
        value = np.array([nd["value"] for nd in nodes], float)
        cost = np.array([nd["cost"] for nd in nodes], float)
        A, b, names = [cost], [model["budget"]], ["budget"]
        for c in model.get("constraints", []):
            row = np.zeros(n)
            for k, v in c["coefficients"].items():
                row[idx[k]] = v
            A.append(row); b.append(c["limit"]); names.append(c["id"])
        for nd in nodes:
            for dep in nd.get("depends_on", []):
                row = np.zeros(n); row[idx[nd["id"]]] = 1; row[idx[dep]] = -1
                A.append(row); b.append(0.0); names.append(f"dep:{nd['id']}->{dep}")
        bounds = [(nd.get("min_level", 0.0), 0.0 if nd["id"] == exclude else 1.0) for nd in nodes]
        if exclude and nodes[idx[exclude]].get("min_level", 0) > 0:
            return None
        A, b = np.array(A), np.array(b)
        if q is None:
            r = linprog(-value, A_ub=A, b_ub=b, bounds=bounds, method="highs")
            if r.status != 0:
                return {"feasible": False, "message": r.message}
            x, duals = r.x, -r.ineqlin.marginals
        else:
            from scipy.optimize import LinearConstraint, Bounds
            Q = np.array(q, float)
            sc = np.maximum(np.abs(b), 1.0)              # scale rows so the solver is well conditioned
            k = max(float(np.abs(value).max()), 1.0)
            obj = lambda x: (-(value @ x) + 0.5 * x @ Q @ x) / k
            r = minimize(obj, np.array([lo for lo, _ in bounds], float), jac=lambda x: (-value + Q @ x) / k,
                         hess=lambda x: Q / k, method="trust-constr",
                         constraints=[LinearConstraint(A / sc[:, None], -np.inf, b / sc)],
                         bounds=Bounds([lo for lo, _ in bounds], [hi for _, hi in bounds]),
                         options={"gtol": 1e-10, "xtol": 1e-12, "maxiter": 5000})
            if r.status not in (1, 2) or (b - A @ r.x).min() < -1e-6 * max(1.0, float(np.abs(b).max())):
                return {"feasible": False, "message": r.message}
            x, duals = r.x, np.zeros(len(b))
        slack = b - A @ x
        x = np.round(np.clip(x, 0, 1), 6)
        return {"feasible": True, "levels": {nd["id"]: float(x[i]) for i, nd in enumerate(nodes)},
                "allocations": {nd["id"]: round(float(x[i] * cost[i]), 2) for i, nd in enumerate(nodes)},
                "objective": round(float(value @ x - (0.5 * x @ np.array(q) @ x if q is not None else 0)), 6),
                "binding_constraints": [names[i] for i in range(len(b)) if abs(slack[i]) <= 1e-7 * max(1.0, abs(b[i]))],
                "shadow_prices": {names[i]: round(float(duals[i]), 6) for i in range(len(b)) if abs(duals[i]) > 1e-9}}

    def c_optimization_runs_request(self, actor_id, pl, bound, env):
        cb = pl["civic_body_id"]
        if not self.credential(cb, actor_id):
            raise Refuse("ELIGIBILITY", "only members request runs")
        mv = None
        for o in self.of_type("portfolio_model", cb):
            for v in self.versions[o["id"]]:
                if v["version_id"] == pl["model_version_id"]:
                    mv = v
        if mv is None:
            raise Refuse("NOT_FOUND", f"model version {pl['model_version_id']} not found")
        q = pl.get("q_matrix")
        config = {"solver": SOLVER_ID, "profile": "QP" if q else "LP", "lane": pl.get("lane", "strict"), "seed": pl.get("seed", 0)}
        if q is not None:
            Q = np.array(q, float)
            if Q.shape != (len(mv["nodes"]),) * 2 or not np.allclose(Q, Q.T) or np.linalg.eigvalsh(Q).min() < -1e-9:
                run = self.put("optimization_run", {"model_version_id": mv["version_id"], "config": config, "state": "Rejected",
                               "rejection": "Q matrix is not symmetric positive semidefinite; Phase 1 solves convex QP only (13.1)"}, cb, authority_basis=actor_id)
                self._txn["keep_on_refuse"] = True     # the rejection and its reason are recorded (13.1)
                raise Refuse("NOT_PSD", f"run {run['id']} rejected before solving: Q is not positive semidefinite", "OPT-REPRO-001", "13.1")
        inputs = {"model": {k: mv[k] for k in ("nodes", "budget", "constraints")}, "q": q, "config": config}
        sol = self.solve(mv, q)
        state = "Published" if sol["feasible"] else "Infeasible"
        run = {"model_version_id": mv["version_id"], "config": config, "q": q, "input_hash": sha(inputs), "state": state,
               "solution": sol, "result_hash": sha(sol), "worker_build_id": "acecog-mvp-0.1", "commit_eligible": config["lane"] == "strict" and sol["feasible"]}
        if sol["feasible"]:
            top = max(sol["levels"], key=lambda k: sol["allocations"][k])
            alt = self.solve(mv, q, exclude=top)
            run["alternative"] = None if not alt or not alt["feasible"] else {"excluded": top, "objective": alt["objective"],
                                                                               "gap": round(sol["objective"] - alt["objective"], 6)}
        r = self.put("optimization_run", run, cb, authority_basis=actor_id)
        if not sol["feasible"]:
            exc = self._exception(cb, "Approved constraints cannot all be satisfied: the model is infeasible", "decision body (Governance Process)",
                                  ["feasibility"], {"run_id": r["id"]})
            raise Escalate(exc, {"run": r})
        return {"run": r}, {"lifecycle_state": "Optimized", "legal_status": {"value": "Advisory", "legal_effect_declaration_id": None,
                            "enabling_authority": None, "effective_date": None}, "delivery_readiness": "Not applicable", "epistemic_class": "Scenario output"}

    def _exception(self, cb, conflict, authority, failed, context):
        e = self.put("exception_proposition", {"governing_conflict": conflict, "authority_required": authority,
                     "failed_tests": failed, "context": context, "state": "Routed"}, cb)
        return {"exception_proposition_id": e["id"], "authority_required": authority, "governing_conflict": conflict, "failed_tests": failed}

    # ---------------------------------------------- baseline & commitment
    def c_baselines_create(self, actor_id, pl, bound, env):
        d = self.get(pl["decision_id"], "decision")
        cb = d["civic_body_id"]
        self.require(actor_id, cb, "create_baseline")
        if d["result"] != "approved":
            raise Refuse("AUTHORITY_MISSING", "only an approved decision may create a baseline", "GOV-AUTHPATH-001")
        run = self.get(pl["run_id"], "optimization_run")
        if not run.get("commit_eligible"):
            raise Refuse("NOT_COMMIT_ELIGIBLE", "run is exploration-lane or infeasible and is not commit-eligible (9.1)", "OPT-REPRO-001")
        for k in ("input_hash", "result_hash", "model_version_id"):
            if not run.get(k):
                raise Refuse("NOT_COMMIT_ELIGIBLE", f"run lacks {k}", "OPT-REPRO-001")
        # G-054: the baseline must carry out the model this decision approved, and only once
        if self._model_version(run["model_version_id"]).get("authority_basis") != d["id"]:
            raise Refuse("APPROVAL_MISMATCH", f"run {run['id']} uses a model version that decision {d['id']} did not approve", "GOV-AUTHPATH-001")
        if any(x["decision_id"] == d["id"] for x in self.of_type("baseline", cb)):
            raise Refuse("APPROVAL_ALREADY_USED", f"decision {d['id']} already has a baseline; changes go through rebalancing", "GOV-AUTHPATH-001")
        b = self.put("baseline", {"decision_id": d["id"], "run_id": run["id"], "model_version_id": run["model_version_id"],
                     "allocations": run["solution"]["allocations"], "bound_versions": bound, "reason": "initial approval"},
                     cb, authority_basis=d["id"])
        return {"baseline": b}, self.status(cb, d["decision_class"], "Baselined", legal=d["legal_status"])

    def c_commitments_reserve(self, actor_id, pl, bound, env):
        b = self.get(pl["baseline_id"], "baseline")
        cb = b["civic_body_id"]
        d = self.get(b["decision_id"], "decision")
        self.require(actor_id, cb, "commit")          # rechecked immediately before commitment (8.7)
        model = self._model_version(b["model_version_id"])
        reserved = sum(c["amount"] for c in self.of_type("commitment", cb) if c["state"] == "Committed")
        if any(c["baseline_id"] == b["id"] and c["state"] == "Committed" for c in self.of_type("commitment", cb)):
            raise Refuse("DOUBLE_ALLOCATION", f"baseline {b['id']} is already committed", None, "MVP-104")
        amount = round(sum(b["allocations"].values()), 2)
        if reserved + amount > model["budget"] + 1e-6:
            raise Refuse("DOUBLE_ALLOCATION", "reservation exceeds the available budget resource", None, "MVP-104")
        c = self.put("commitment", {"baseline_id": b["id"], "baseline_version_id": b["version_id"], "amount": amount,
                     "lines": b["allocations"], "state": "Committed"}, cb, authority_basis=d["id"])
        return {"commitment": c}, self.status(cb, d["decision_class"], "Committed", "Funded but incomplete", legal=d["legal_status"])

    def _model_version(self, vid):
        oid = vid.split("@")[0]
        return next(v for v in self.versions[oid] if v["version_id"] == vid)

    def current_baseline(self, cb):
        bs = self.of_type("baseline", cb)
        return bs[0] if bs else None

    def c_actuals_post(self, actor_id, pl, bound, env):
        cb = pl["civic_body_id"]
        self.require(actor_id, cb, "post_actuals")
        if pl.get("attempt_baseline_update"):
            raise Refuse("BASELINE_IMMUTABLE", "actuals are recorded beside the baseline and never overwrite it", "EXE-BASELINE-001")
        b = self.current_baseline(cb)
        if not b:
            raise Refuse("STATE", "no baseline to measure against")
        a = self.put("actual", {"node_id": pl["node_id"], "actual_cost": pl["actual_cost"], "observed_at": pl["observed_at"],
                     "ingested_at": f"T+{len(self.events) + 1}", "baseline_version_id": b["version_id"],
                     "variance": round(pl["actual_cost"] - b["allocations"].get(pl["node_id"], 0), 2)}, cb, authority_basis=actor_id)
        return {"actual": a}, {"lifecycle_state": "Measured", "legal_status": self.legal_status(cb, "-"),
                               "delivery_readiness": "Funded but incomplete", "epistemic_class": "Observed"}

    # ------------------------------------------------ rebalance & exceptions
    def c_rebalances_propose(self, actor_id, pl, bound, env):
        cb = pl["civic_body_id"]
        self.actor(actor_id)
        b = self.current_baseline(cb)
        if not b:
            raise Refuse("STATE", "no baseline to rebalance")
        env_ = self.envelope(cb, pl["decision_class"])
        failed = []
        if env_ is None:
            failed.append("no Delegation Envelope for this decision class")
        else:
            env_ = next(v for v in self.versions[env_["id"]] if v["version_id"] == bound.get(env_["id"], env_["version_id"]))
            if not env_["valid"]:
                failed.append("envelope parameters invalid: autonomous resolution disabled")
            else:
                if env_.get("authorized_resolver") not in (None, actor_id):
                    failed.append(f"{actor_id} is not the envelope's authorized resolver")
                if pl["amount"] > env_["tolerance"]:
                    failed.append(f"amount {pl['amount']} exceeds tolerance {env_['tolerance']}")
                conf = pl.get("confidence")
                if conf is None:
                    failed.append("inputs carry no calibrated confidence (fails closed)")
                elif conf < env_["confidence_threshold"]:
                    failed.append(f"confidence {conf} below threshold {env_['confidence_threshold']}")
                rev = pl.get("reversibility")
                if rev is None or rev < env_["min_reversibility"]:
                    failed.append(f"reversibility {rev} below minimum {env_['min_reversibility']}")
        new_alloc = dict(b["allocations"])
        if new_alloc.get(pl["from_node_id"], 0) < pl["amount"]:
            failed.append("source node lacks the amount")
        new_alloc[pl["from_node_id"]] = round(new_alloc.get(pl["from_node_id"], 0) - pl["amount"], 2)
        new_alloc[pl["to_node_id"]] = round(new_alloc.get(pl["to_node_id"], 0) + pl["amount"], 2)
        hard = self._hard_violations(cb, b, new_alloc)
        if hard:
            ex = self._exception(cb, f"rebalance would breach hard constraint(s) {', '.join(hard)}", "decision body (Governance Process)",
                                 failed + [f"hard constraint {h}" for h in hard], {"proposal": pl})
            raise Escalate(ex)
        if failed:
            ex = self._exception(cb, "rebalance falls outside the active Delegation Envelope", "decision body (Governance Process)", failed, {"proposal": pl})
            raise Escalate(ex)
        nb = self.put("baseline", {**{k: b[k] for k in ("decision_id", "run_id", "model_version_id", "bound_versions")},
                      "allocations": new_alloc, "reason": f"delegated rebalance under {env_['version_id']}"},
                      cb, oid=b["id"], authority_basis=env_["version_id"])
        return {"baseline": nb, "envelope_version_id": env_["version_id"]}, self.status(cb, pl["decision_class"], "Resolved", "Funded but incomplete")

    def _hard_violations(self, cb, b, alloc, m=None):
        m = m or self._model_version(b["model_version_id"])
        cost = {n["id"]: n["cost"] for n in m["nodes"]}
        lv = {k: (alloc.get(k, 0) / cost[k] if cost[k] else 0) for k in cost}
        out = [c["id"] for c in m.get("constraints", []) if c["kind"] == "hard" and
               sum(v * lv[k] for k, v in c["coefficients"].items()) > c["limit"] + 1e-6]
        out += [n["id"] + " level>1" for n in m["nodes"] if lv[n["id"]] > 1 + 1e-6]
        return out

    def c_exceptions_resolve(self, actor_id, pl, bound, env):
        e = self.get(pl["exception_proposition_id"], "exception_proposition")
        cb = e["civic_body_id"]
        d = self.get(pl["decision_id"], "decision")
        if d["result"] != "approved" or d["requested_action"].get("exception_id") != e["id"]:
            raise Refuse("AUTHORITY_MISSING", "an exception is resolved only by an approved decision addressing it", "GOV-EXCEPT-001")
        if e.get("state") == "Closed":
            raise Refuse("STATE", f"exception {e['id']} is already closed", "GOV-EXCEPT-001")
        out = {}
        act = d["requested_action"].get("apply")
        if act:
            # G-059 (8.7, invariant 3): the decided change is re-checked before it touches the baseline
            b = self.current_baseline(cb)
            model = self._model_version(b["model_version_id"])
            node_ids = {n["id"] for n in model["nodes"]}
            amt = act.get("amount", 0)
            if act["from_node_id"] not in node_ids or act["to_node_id"] not in node_ids or not amt > 0:
                raise Refuse("STATE", "the reallocation must move a positive amount between nodes of the model", "GOV-EXCEPT-001")
            alloc = dict(b["allocations"])
            if alloc.get(act["from_node_id"], 0) < amt - 1e-6:
                raise Refuse("HARD_CONSTRAINT", f"{act['from_node_id']} holds {alloc.get(act['from_node_id'], 0)}, less than {amt}", "GOV-EXCEPT-001")
            alloc[act["from_node_id"]] = round(alloc[act["from_node_id"]] - amt, 2)
            alloc[act["to_node_id"]] = round(alloc.get(act["to_node_id"], 0) + amt, 2)
            relax = d["requested_action"].get("relax") or []
            if relax:
                # a relaxation is never silent: the decision names it and it becomes a new constraint version
                limits = {r["constraint_id"]: r["limit"] for r in relax}
                cons = {c["id"] for c in model.get("constraints", [])}
                if not set(limits) <= cons:
                    raise Refuse("NOT_FOUND", f"unknown constraint(s) {', '.join(sorted(set(limits) - cons))}", "GOV-EXCEPT-001")
                mdata = {k: v for k, v in model.items() if k not in ("id", "version_id", "object_type", "civic_body_id", "authority_basis", "supersedes", "created_in_transaction")}
                mdata["constraints"] = [dict(c, limit=limits.get(c["id"], c["limit"]),
                                             **({"relaxed_by_decision_id": d["id"], "previous_limit": c["limit"]} if c["id"] in limits else {}))
                                        for c in model["constraints"]]
            else:
                mdata = model
            hard = self._hard_violations(cb, None, alloc, mdata)
            if hard:
                raise Refuse("HARD_CONSTRAINT", f"the decided reallocation would breach {', '.join(hard)}; a decision may relax a constraint only by naming it",
                             "GOV-EXCEPT-001")
            if sum(alloc.values()) > model["budget"] + 1e-6:
                raise Refuse("HARD_CONSTRAINT", "the decided reallocation exceeds the budget", "GOV-EXCEPT-001")
            if relax:
                model = out["portfolio_model"] = self.put("portfolio_model", mdata, cb, oid=model["id"], authority_basis=d["id"])
            out["baseline"] = self.put("baseline", {**{k: b[k] for k in ("run_id", "bound_versions")}, "model_version_id": model["version_id"],
                                       "decision_id": d["id"], "allocations": alloc, "reason": f"exception {e['id']} resolved"},
                                       cb, oid=b["id"], authority_basis=d["id"])
        ed = {k: v for k, v in e.items() if k not in ("id", "version_id", "object_type", "civic_body_id", "authority_basis", "supersedes", "created_in_transaction")}
        ed.update(state="Closed", resolution=pl["resolution"], resolved_by=d["id"])
        out["exception_proposition"] = self.put("exception_proposition", ed, cb, oid=e["id"], authority_basis=d["id"])
        return out, self.status(cb, d["decision_class"], "Resolved", legal=d["legal_status"])

    def c_change_requests_put_in_force(self, actor_id, pl, bound, env):
        cb = pl["civic_body_id"]
        d = self.get(pl["decision_id"], "decision")
        ra = d["requested_action"]
        if d["result"] != "approved" or ra.get("type") != "approve_change":
            raise Refuse("AUTHORITY_MISSING", "a change goes in force only through an approved change decision", "GOV-AUTHPATH-001")
        # CL-046: an approval authorizes exactly the change it approved, once
        if any(v["authority_basis"] == d["id"] and "in_force_from_seq" in v for vs in self.versions.values() for v in vs):
            raise Refuse("CHANGE_ALREADY_APPLIED", f"decision {d['id']} has already put its change in force", "GOV-AUTHPATH-001", "CL-046")
        if ra.get("target_id") != pl["target_id"] or ra.get("change_hash") != sha(pl["changes"]):
            raise Refuse("CHANGE_MISMATCH", "the change differs from the one the decision approved (target or content hash)", "GOV-AUTHPATH-001", "CL-046")
        t = self.get(pl["target_id"])
        data = {k: v for k, v in t.items() if k not in ("id", "version_id", "object_type", "civic_body_id", "authority_basis", "supersedes", "created_in_transaction")}
        data.update(pl["changes"])
        if t["object_type"] == "delegation_envelope":
            data["valid"], data["validation_errors"] = self._validate_envelope(data)
        if t["object_type"] == "governance_process":
            self._check_classes(data["decision_classes"])
        data["in_force_from_seq"] = len(self.events) + 1
        return {"in_force": self.put(t["object_type"], data, cb, oid=t["id"], authority_basis=d["id"]),
                "note": "applies only to transactions that start after this point (8.9)"}

    # -------------------------------------------- export, records, config
    def export_package(self, cb):
        ids = [i for i, o in self.obj.items() if o["civic_body_id"] == cb]
        return {"format": "acecog-export/0.1", "spec": contract.SPEC_VERSION, "civic_body_id": cb,
                "versions": {i: self.versions[i] for i in ids}, "actors": {k: v for k, v in self.actors.items() if v["civic_body_id"] == cb},
                "events": copy.deepcopy(self.events), "counters": dict(self.counters),
                "hash_chain_head": self.events[-1]["hash"] if self.events else None,
                "verification": "recompute sha256(prev_hash + canonical_json(event without 'hash')) for each event in order"}

    def c_exports_create(self, actor_id, pl, bound, env):
        cb = pl["civic_body_id"]
        self.require(actor_id, cb, "export")
        pkg = self.export_package(cb)
        x = self.put("export", {"package_sha256": sha(pkg), "event_count": len(pkg["events"])}, cb, authority_basis=actor_id)
        self.emit("security.export", {"export_id": x["id"], "actor_id": actor_id})
        self._exports[x["id"]] = pkg
        return {"export": x}

    def c_retention_schedules_adopt(self, actor_id, pl, bound, env):
        cb = pl["civic_body_id"]
        self.require(actor_id, cb, "adopt_retention")
        return {"retention_schedule": self.put("retention_schedule", {k: pl.get(k) for k in ("record_class", "retain_days", "destruction_authority", "legal_basis")},
                                               cb, authority_basis=actor_id)}

    def c_records_delete(self, actor_id, pl, bound, env):
        rec = self.get(pl["record_id"])
        cb = rec["civic_body_id"]
        sched = next((s for s in self.of_type("retention_schedule", cb) if s["record_class"] == pl["record_class"]), None)
        if sched is None:
            raise Refuse("RETENTION", f"no Retention Schedule covers record class {pl['record_class']}", None, "ASR-05")
        if pl["created_days_ago"] < sched["retain_days"] and not pl.get("legal_order"):
            raise Refuse("RETENTION", f"record must be kept {sched['retain_days']} days; it is {pl['created_days_ago']} days old", None, "ASR-05")
        self.require(actor_id, cb, sched["destruction_authority"])
        self.emit("record.deleted", {"record_id": rec["id"], "schedule": sched["version_id"], "legal_order": pl.get("legal_order")})
        return {"deleted": rec["id"]}

    def c_configuration_set(self, actor_id, pl, bound, env):
        cb = pl["civic_body_id"]
        self.require(actor_id, cb, "configure")
        s = pl["setting"]
        if s in PROTECTED_SETTINGS and pl["value"] in (False, "off", "disabled", 0):
            raise Refuse("LAYER_RULE", f"{PROTECTED_SETTINGS[s]} is an Assurance Control and cannot be disabled",
                         "GOV-FRAMEWORK-001", PROTECTED_SETTINGS[s], "Assurance Controls")
        if s in ENGAGEMENT_SETTINGS:
            raise Refuse("LAYER_RULE", "feeds and notifications are generated deterministically from governed state; ranking, delay, or hiding for engagement is not configurable",
                         "AI-NEUTRAL-001", "UIX-NEUTRAL-003", "Invariant Floor")
        return {"setting": self.put("setting", {"setting": s, "value": pl["value"]}, cb, authority_basis=actor_id)}

    # --------------------------------------------------------- queries
    def q_decision(self, did):
        d = self.get(did, "decision")
        return {"decision": d, "status": self.status(d["civic_body_id"], d["decision_class"], d["lifecycle_state"], legal=d["legal_status"])}

    def q_provenance(self, did):
        d = self.get(did, "decision")
        cb = d["civic_body_id"]
        p = self.versions[d["proposition_id"]]
        baselines = [v for o in self.of_type("baseline", cb) for v in self.versions[o["id"]] if v["decision_id"] == did]
        run = self.obj.get(baselines[0]["run_id"]) if baselines else None
        return {"decision_id": did, "status": self.q_decision(did)["status"],
                "inputs": {"proposition_versions": [x["version_id"] for x in p],
                           "decided_version": d["proposition_version_id"],
                           "evidence": [e["id"] for e in self.of_type("evidence", cb)]},
                "governance": {"process_version_id": d["process_version_id"], "decision_class": d["decision_class"],
                               "legal_status_at_decision": d["legal_status"]},
                "model": {"model_version_id": run["model_version_id"] if run else None},
                "run": {k: run[k] for k in ("id", "config", "input_hash", "result_hash", "worker_build_id")} if run else {},
                "analysis": {k: run["solution"][k] for k in ("binding_constraints", "shadow_prices")} | {"alternative": run.get("alternative")} if run else {},
                "deliberation": {"posts": [x for x in self.of_type("deliberation_post", cb) if x["proposition_id"] == d["proposition_id"]],
                                 "minority_positions": d["minority_positions"],
                                 "recusals": [x for x in self.of_type("interest_declaration", cb) if x["proposition_id"] == d["proposition_id"]]},
                "disposition": {"result": d["result"], "tally": d["tally"], "low_confidence": d["low_confidence"],
                                "commitments": [c["id"] for c in self.of_type("commitment", cb)]},
                "outcome": {"actuals": [a for a in self.of_type("actual", cb)]},
                "lineage": {"baseline_versions": [v["version_id"] + ": " + v["reason"] for o in self.of_type("baseline", cb) for v in self.versions[o["id"]]],
                            "exceptions": [e["id"] for e in self.of_type("exception_proposition", cb)]}}

    def q_replay(self, did):
        """Strict replay: re-solve from the bound model version and compare hashes (9.1)."""
        d = self.get(did, "decision")
        b = next((v for o in self.of_type("baseline", d["civic_body_id"]) for v in self.versions[o["id"]] if v["decision_id"] == did), None)
        if not b:
            raise Refuse("NOT_FOUND", "decision has no baseline run to replay")
        run = self.versions[b["run_id"]][0]
        mv = self._model_version(run["model_version_id"])
        sol = self.solve(mv, run.get("q"))
        return {"run_id": run["id"], "original_result_hash": run["result_hash"], "replayed_result_hash": sha(sol),
                "reproduced": sha(sol) == run["result_hash"], "model_version_id": mv["version_id"], "solver": run["config"]["solver"]}

    def q_delegations(self, cb):
        out, eligible = [], len([c for c in self.of_type("membership_credential", cb) if not c.get("revoked")])
        classes = {dc["name"]: dc for dc in self.process(cb)["decision_classes"]}
        for name, dc in classes.items():
            counts = {}
            for d in self.of_type("delegation", cb):
                if d["decision_class"] == name and d["active"]:
                    counts.setdefault(d["delegate"], []).append(d["principal"])
            for dlg, ps in sorted(counts.items()):
                share = len(ps) / max(eligible, 1)
                out.append({"decision_class": name, "delegate": dlg, "principals": sorted(ps), "share_of_eligible": round(share, 4),
                            "disclosed_concentration": share > dc["delegation_disclosure_threshold"],
                            "reconfirm_every_days": dc["delegation_reconfirm_days"]})
        return {"civic_body_id": cb, "delegations": out}

    def q_feed(self, actor_id):
        a = self.actor(actor_id)
        cb = a["civic_body_id"]
        items = []
        for p in sorted(self.of_type("proposition", cb), key=lambda p: p["id"]):
            if p["state"] == "Proposed":
                items.append({"proposition_id": p["id"], "title": p["title"],
                              "reason_shown": f"Open for a decision in your civic body (decision class: {p['decision_class']})",
                              "legal_status": self.legal_status(cb, p["decision_class"])["value"]})
        return {"actor_id": actor_id, "ordering": "deterministic: proposition order of submission", "items": items}

    def q_events(self, after=0):
        return {"events": [e for e in self.events if e["seq"] > after], "head": self.events[-1]["hash"] if self.events else None}


def verify_chain(events):
    prev = "0" * 64
    for ev in events:
        body = {k: v for k, v in ev.items() if k != "hash"}
        if ev["prev_hash"] != prev or hashlib.sha256((prev + canon(body)).encode()).hexdigest() != ev["hash"]:
            return False, ev["seq"]
        prev = ev["hash"]
    return True, len(events)


def rehydrate(pkg):
    """Load an export into a fresh engine (CMP-007). Refuses a package whose hash chain fails."""
    ok, at = verify_chain(pkg["events"])
    if not ok:
        raise ValueError(f"hash chain broken at event {at}")
    e = Engine()
    e.events = copy.deepcopy(pkg["events"])
    e.versions = copy.deepcopy(pkg["versions"])
    e.obj = {k: v[-1] for k, v in e.versions.items()}
    e.actors = copy.deepcopy(pkg["actors"])
    e.counters = dict(pkg["counters"])
    return e
