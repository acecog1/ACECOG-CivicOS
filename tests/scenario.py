"""Contract scenario: drive the engine over HTTP through the Riverbend Commons scenario (26.1)
and check the Phase 1 acceptance tests from outside, as an independent reviewer would.

Used by tests/test_contract.py. Run directly to refresh docs/api/contract-test-results.md
and docs/api/examples.json:

    python tests/scenario.py
"""
import json, os, sys, threading, urllib.request, urllib.error
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))
from acecog import server
from acecog.engine import Engine, sha, verify_chain, rehydrate

API_DOCS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs", "api")
PORT = 8799
BASE = f"http://127.0.0.1:{PORT}"
RESULTS, EXAMPLES = [], {}
_n = [0]


def http(method, path, body=None):
    req = urllib.request.Request(BASE + path, method=method, data=None if body is None else json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req) as r:
            return r.status, json.loads(r.read())
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read())


def cmd(name, actor, payload, client="desktop", confirm=None, command_id=None, example=None):
    _n[0] += 1
    env = {"command_id": command_id or f"c-{_n[0]:04d}", "actor_id": actor, "client": client, "payload": payload}
    if confirm:
        env["human_confirmation"] = {"confirmed_by": confirm, "reviewed_payload_hash": sha(payload)}
    code, res = http("POST", f"/v0/commands/{name}", env)
    if example:
        EXAMPLES.setdefault(name, {}).setdefault(example.replace(" ", "_").lower()[:40], {"summary": example, "envelope": env})
    res["_http"], res["_command_id"] = code, env["command_id"]
    return res


def q(path):
    return http("GET", path)[1]


def check(test_id, title, cond, detail=""):
    RESULTS.append((test_id, title, bool(cond), detail))


# ------------------------------------------------------------------ fixture
NODES = [  # id, name, cost, value, water (ML/yr), crew-weeks, grant-eligible
    ("i01", "Riverside trail repair", 120000, 70, 0, 6, False),
    ("i02", "Storm drain upgrade", 220000, 150, 0, 10, True),
    ("i03", "Community garden expansion", 60000, 40, 8, 0, False),
    ("i04", "Library HVAC replacement", 180000, 90, 0, 4, False),
    ("i05", "Main Street bike lanes", 150000, 95, 0, 8, False),
    ("i06", "Tree canopy planting", 80000, 65, 12, 4, True),
    ("i07", "Senior center roof", 140000, 100, 0, 6, False),
    ("i08", "Town hall solar array", 200000, 110, 0, 0, False),
    ("i09", "Playground resurfacing", 70000, 45, 2, 3, False),
    ("i10", "Wetland restoration", 110000, 85, 5, 5, True),
]


def model(budget=900000, water=20):
    nodes = [{"id": i, "name": n, "cost": c, "value": v} | ({"depends_on": ["i02"]} if i == "i05" else {}) for i, n, c, v, *_ in NODES]
    return {"budget": budget, "nodes": nodes, "objectives": [{"id": "obj-public-value", "name": "Total public value score"}],
            "constraints": [
                {"id": "eco-water-ceiling", "name": "Watershed draw ceiling (ML/yr)", "kind": "hard",
                 "coefficients": {i: w for i, _, _, _, w, _, _ in NODES if w}, "limit": water},
                {"id": "crew-capacity", "name": "Public works crew-weeks", "kind": "hard",
                 "coefficients": {i: k for i, _, _, _, _, k, _ in NODES if k}, "limit": 30},
                {"id": "appropriation-limit", "name": "Non-grant spending limited to the appropriation", "kind": "hard",
                 "coefficients": {i: c for i, _, c, _, _, _, g in NODES if not g}, "limit": 650000}]}


def run_all(engine=None):
    RESULTS.clear(); EXAMPLES.clear(); _n[0] = 0
    srv = server.serve(engine or Engine(), PORT)
    t = threading.Thread(target=srv.serve_forever, daemon=True)
    t.start()
    try:
        scenario()
    finally:
        srv.shutdown()
    return RESULTS


def vote_all(pid, choices):
    for a, c in choices.items():
        r = cmd("votes.cast", a, {"proposition_id": pid, "choice": c}, example="Cast a vote")
        assert r["outcome"] == "accepted", r


def scenario():
    founders = [("ana", "Ana (Facilitator/Clerk)", ["facilitator"]), ("ben", "Ben (City Manager)", ["city_manager"]),
                ("cara", "Cara", ["member"]), ("dev", "Dev", ["member"]), ("eli", "Eli", ["member"]), ("fay", "Fay", ["member"])]
    r = cmd("civic-bodies.create", "ana", {"name": "Riverbend Commons", "jurisdiction": "Riverbend (reference scenario 26.1)", "gml_level": 1,
            "founding_members": [{"actor_id": a, "display_name": d, "roles": ro} for a, d, ro in founders]}, example="Create Riverbend Commons")
    cb = r["result"]["civic_body"]["id"]

    classes = [
        {"name": "annual_budget", "method": "direct_vote", "approval_threshold": 0.5, "quorum": 0.5, "min_attestation": "verified"},
        {"name": "routine_rebalance", "method": "consent", "approval_threshold": 1.0, "quorum": 0.5, "min_attestation": "verified"},
        {"name": "minor_rebalance", "method": "consent", "approval_threshold": 1.0, "quorum": 0.5, "min_attestation": "verified"},
        {"name": "change_control", "method": "direct_vote", "approval_threshold": 0.6, "quorum": 0.5, "min_attestation": "verified"},
        {"name": "advisory_poll", "method": "direct_vote", "approval_threshold": 0.5, "quorum": 0.1, "min_attestation": "self_attested"},
    ]
    bad = cmd("governance-processes.adopt", "ana", {"civic_body_id": cb, "decision_classes": [dict(classes[0], participation_fee=5)]})
    check("INV-AT (24)", "A Governance Process that charges a fee to take part is refused (TRU-ACCESS-001)",
          bad["outcome"] == "refused" and bad["refusal"]["invariant_id"] == "TRU-ACCESS-001")
    r = cmd("governance-processes.adopt", "ana", {"civic_body_id": cb, "decision_classes": classes}, example="Adopt decision classes")
    proc_v1 = r["result"]["governance_process"]["version_id"]

    for a, acts in (("ben", ["create_baseline", "commit", "post_actuals", "records_officer"]),):
        cmd("authorities.grant", "ana", {"civic_body_id": cb, "grantee_actor_id": a, "actions": acts}, example="Grant execution authority")
    self_appt = cmd("authorities.grant", "ana", {"civic_body_id": cb, "grantee_actor_id": "ana", "actions": ["approve_disbursement"], "monitoring_role": True})
    check("INV-AT-17", "An approval or monitoring role appointed by itself is refused", self_appt["outcome"] == "refused" and self_appt["refusal"]["invariant_id"] == "TRU-MONITOR-001")
    no_sel = cmd("authorities.grant", "ana", {"civic_body_id": cb, "grantee_actor_id": "cara", "actions": ["approve_disbursement"], "monitoring_role": True})
    check("INV-AT-17", "At GML-1 a monitoring role must be selected through the Governance Process", no_sel["outcome"] == "refused")
    self_g = cmd("authorities.grant", "ana", {"civic_body_id": cb, "grantee_actor_id": "ana", "actions": ["post_actuals"]})
    star = cmd("authorities.grant", "ana", {"civic_body_id": cb, "grantee_actor_id": "cara", "actions": ["*"]})
    check("G-055", "An actor cannot grant authority to themselves, and '*' is not grantable after founding",
          self_g["outcome"] == "refused" and self_g["refusal"]["code"] == "SELF_GRANT"
          and star["outcome"] == "refused" and star["refusal"]["code"] == "WILDCARD_GRANT")

    r = cmd("delegation-envelopes.adopt", "ana", {"civic_body_id": cb, "decision_class": "routine_rebalance", "tolerance": 25000, "authorized_resolver": "ben"},
            example="Adopt envelope with default thresholds")
    env1 = r["result"]["delegation_envelope"]
    check("5.9", "Envelope defaults applied: confidence 0.90, reversibility 2", env1["confidence_threshold"] == 0.9 and env1["min_reversibility"] == 2)
    r = cmd("delegation-envelopes.adopt", "ana", {"civic_body_id": cb, "decision_class": "minor_rebalance", "tolerance": 5000, "confidence_threshold": 1.5})
    check("5.9", "Out-of-range envelope parameter disables autonomous resolution", r["result"]["autonomous_resolution"] == "disabled")

    check("MVP-100", "Create a Civic Body, Governance Process, members/roles, authority, and a portfolio",
          q(f"/v0/queries/civic-bodies/{cb}")["governance_process"] is not None and len(q(f"/v0/queries/civic-bodies/{cb}")["members"]) == 6)

    # ---- MVP-101 competing proposals, amendment preserves versions
    pa = cmd("propositions.submit", "cara", {"civic_body_id": cb, "decision_class": "annual_budget", "title": "FY27 improvement portfolio (Plan A)",
             "body": "Adopt the FY27 portfolio model with a $900k budget and a 20 ML/yr watershed ceiling.",
             "requested_action": {"type": "adopt_portfolio_model", "model": model(water=22)}}, example="Submit a portfolio proposition")
    pid_a = pa["result"]["proposition"]["id"]
    pb = cmd("propositions.submit", "dev", {"civic_body_id": cb, "decision_class": "annual_budget", "title": "FY27 portfolio (Plan B, lower budget)",
             "body": "Adopt the portfolio model at $800k.", "requested_action": {"type": "adopt_portfolio_model", "model": model(budget=800000)},
             "competes_with": pid_a})
    pid_b = pb["result"]["proposition"]["id"]
    am = cmd("propositions.amend", "cara", {"proposition_id": pid_a, "body": "Amended: watershed ceiling tightened to 20 ML/yr.",
             "requested_action": {"type": "adopt_portfolio_model", "model": model()}}, example="Amend a proposition")
    vers = q(f"/v0/queries/propositions/{pid_a}")["versions"]
    check("MVP-101", "Two competing proposals preserved with exact versions; amendment adds a version",
          len(vers) == 2 and vers[0]["body"] != vers[1]["body"] and pb["result"]["proposition"]["competes_with"] == pid_a)

    # ---- CMP-003 open-meeting guard via a pack; CMP-002 relaxing pack refused
    relax = cmd("compliance-packs.adopt", "ana", {"civic_body_id": cb, "pack_id": "pilot-state", "edition": "0.1",
                "rules": [{"rule": "allow_private_quorum_threads", "effect": "relax", "target": "open meetings"}]})
    check("CMP-002", "A pack whose rule would relax a higher layer is refused at adoption", relax["outcome"] == "refused" and relax["refusal"]["code"] == "LAYER_RULE")
    cmd("compliance-packs.adopt", "ana", {"civic_body_id": cb, "pack_id": "pilot-state", "edition": "0.1",
        "rules": [{"rule": "open_meeting_guard", "effect": "add_constraint", "legal_basis": "State open meetings law (to confirm, 43.8)"}]},
        example="Adopt the pilot-state pack")
    priv = cmd("deliberation.post", "dev", {"proposition_id": pid_a, "text": "Can we line up votes before the meeting?", "visibility": "private", "to_actor_id": "eli"})
    pub = cmd("deliberation.post", "dev", {"proposition_id": pid_a, "text": "I support Plan A; the drain upgrade is overdue.", "visibility": "public", "position": "support"},
              example="Post to the public record")
    check("CMP-003", "Under the open-meeting guard, a private member-to-member thread is refused; public posting works",
          priv["outcome"] == "refused" and priv["refusal"]["code"] == "OPEN_MEETING_GUARD" and pub["outcome"] == "accepted")
    cmd("deliberation.post", "fay", {"proposition_id": pid_a, "text": "Minority report: the library HVAC should come first.", "visibility": "public", "position": "minority_report"})

    # ---- CMP-004 recusal
    cmd("interest-declarations.record", "eli", {"civic_body_id": cb, "proposition_id": pid_a, "description": "Owns property adjoining the trail project"},
        example="Declare an interest")
    rv = cmd("votes.cast", "eli", {"proposition_id": pid_a, "choice": "yes"})
    check("CMP-004", "A member with a recorded Interest Declaration cannot vote on the proposition", rv["outcome"] == "refused" and rv["refusal"]["code"] == "RECUSED")

    # ---- CL-029 delegation and concentration disclosure
    dl = cmd("delegations.assign", "fay", {"civic_body_id": cb, "decision_class": "change_control", "delegate_actor_id": "dev"}, example="Delegate a decision class")
    loop = cmd("delegations.assign", "dev", {"civic_body_id": cb, "decision_class": "change_control", "delegate_actor_id": "fay"})
    conc = q(f"/v0/queries/delegations/{cb}")["delegations"]
    cmd("delegations.assign", "cara", {"civic_body_id": cb, "decision_class": "advisory_poll", "delegate_actor_id": "dev"})
    rvk = cmd("delegations.revoke", "cara", {"civic_body_id": cb, "decision_class": "advisory_poll"}, example="Revoke a delegation")
    check("17.3", "A delegation can be revoked", rvk["outcome"] == "accepted" and rvk["result"]["delegation"]["active"] is False)
    check("CL-029", "Delegation concentration above the disclosure threshold is disclosed; delegation loops are refused",
          dl["outcome"] == "accepted" and loop["outcome"] == "refused" and conc and conc[0]["disclosed_concentration"])

    # ---- MVP-102 approve the model
    vote_all(pid_a, {"ana": "yes", "ben": "yes", "cara": "yes", "dev": "yes", "fay": "no"})
    vote_all(pid_b, {"ana": "no", "ben": "no", "cara": "no", "dev": "yes", "fay": "no"})
    d_a = cmd("decisions.close", "ana", {"proposition_id": pid_a}, example="Close a decision")
    d_b = cmd("decisions.close", "ana", {"proposition_id": pid_b})
    dec_a = d_a["result"]["decision"]
    mv = d_a["result"]["portfolio_model"]
    check("MVP-102", "Approve objectives, constraints, budget envelope, and decision method; minority position preserved",
          dec_a["result"] == "approved" and d_b["result"]["decision"]["result"] == "rejected" and len(dec_a["minority_positions"]) >= 2)
    check("INV-AT-26", "An approved decision with no Legal Effect Declaration is labeled Advisory",
          d_a["status"]["legal_status"]["value"] == "Advisory" and d_a["status"]["lifecycle_state"] == "Approved")

    def approve(title, action):
        p = cmd("propositions.submit", "ana", {"civic_body_id": cb, "decision_class": "change_control", "title": title, "body": title,
                "requested_action": action})
        vote_all(p["result"]["proposition"]["id"], {"ana": "yes", "ben": "yes", "cara": "yes", "dev": "yes"})
        return cmd("decisions.close", "ana", {"proposition_id": p["result"]["proposition"]["id"]})["result"]["decision"]

    # ---- G-054 an approval authorizes only its own subject, once
    monitor = {"civic_body_id": cb, "grantee_actor_id": "cara", "actions": ["approve_disbursement"], "monitoring_role": True,
               "rotation_terms": "12-month term; recall by change_control vote"}
    wrong = cmd("authorities.grant", "ana", dict(monitor, selected_by_decision_id=dec_a["id"]))
    dec_appt = approve("Appoint Cara as disbursement monitor", {"type": "appoint", "grantee_actor_id": "cara", "actions": ["approve_disbursement"]})
    other_person = cmd("authorities.grant", "ana", dict(monitor, grantee_actor_id="dev", selected_by_decision_id=dec_appt["id"]))
    appt = cmd("authorities.grant", "ana", dict(monitor, selected_by_decision_id=dec_appt["id"]), example="Appoint a monitoring role selected by decision")
    again = cmd("authorities.grant", "ana", dict(monitor, selected_by_decision_id=dec_appt["id"]))
    check("G-054", "A monitoring appointment needs the decision that approved that person for those actions, and uses it once",
          wrong["refusal"]["code"] == "APPROVAL_MISMATCH" and other_person["refusal"]["code"] == "APPROVAL_MISMATCH"
          and appt["outcome"] == "accepted" and again["refusal"]["code"] == "APPROVAL_ALREADY_USED")
    prov = q(f"/v0/queries/decisions/{dec_a['id']}/provenance")
    check("CMP-004", "The recusal appears in the decision's provenance", any(x["person_id"] == "eli" for x in prov["deliberation"]["recusals"]))

    # ---- MVP-103 solve
    nonpsd = cmd("optimization-runs.request", "cara", {"civic_body_id": cb, "model_version_id": mv["version_id"], "q_matrix": [[0] * 10 for _ in range(9)] + [[0] * 9 + [-1]]})
    check("13.1", "A Q matrix that is not positive semidefinite is rejected before solving", nonpsd["outcome"] == "refused" and nonpsd["refusal"]["code"] == "NOT_PSD")
    qp = cmd("optimization-runs.request", "cara", {"civic_body_id": cb, "model_version_id": mv["version_id"], "lane": "best_effort",
             "q_matrix": [[(5 if i == j else 0) for j in range(10)] for i in range(10)]})
    check("13.1", "A convex QP run is accepted on the exploration lane", qp["outcome"] == "accepted" and qp["result"]["run"]["config"]["profile"] == "QP")
    run = cmd("optimization-runs.request", "cara", {"civic_body_id": cb, "model_version_id": mv["version_id"], "lane": "strict", "seed": 0},
              example="Request a strict-lane run")
    sol = run["result"]["run"]["solution"]
    check("MVP-103", "Feasible portfolio solved; binding constraints shown; a near-optimal alternative reported",
          sol["feasible"] and sol["binding_constraints"] and run["result"]["run"]["alternative"] is not None,
          f"objective {sol['objective']}; binding: {', '.join(sol['binding_constraints'])}")
    check("8.0", "A run result is labeled Scenario output and Advisory", run["status"]["epistemic_class"] == "Scenario output")

    # ---- INV-AT-08 exploration lane not commit-eligible
    nb = cmd("baselines.create", "ben", {"decision_id": dec_a["id"], "run_id": qp["result"]["run"]["id"]})
    check("INV-AT-08", "A result that is not commit-eligible (exploration lane) is refused at baseline", nb["outcome"] == "refused" and nb["refusal"]["invariant_id"] == "OPT-REPRO-001")
    na = cmd("baselines.create", "cara", {"decision_id": dec_a["id"], "run_id": run["result"]["run"]["id"]})
    check("GOV-AUTHPATH-001", "A member without baseline authority cannot create a baseline", na["outcome"] == "refused" and na["refusal"]["code"] == "AUTHORITY_MISSING")
    bl = cmd("baselines.create", "ben", {"decision_id": dec_a["id"], "run_id": run["result"]["run"]["id"]}, example="Create the baseline")
    base = bl["result"]["baseline"]
    bl_wrong = cmd("baselines.create", "ben", {"decision_id": dec_appt["id"], "run_id": run["result"]["run"]["id"]})
    bl_again = cmd("baselines.create", "ben", {"decision_id": dec_a["id"], "run_id": run["result"]["run"]["id"]})
    check("G-054", "A baseline needs the decision that approved the run's model, and a decision baselines once",
          bl_wrong["refusal"]["code"] == "APPROVAL_MISMATCH" and bl_again["refusal"]["code"] == "APPROVAL_ALREADY_USED")

    # ---- MVP-104 commit without double allocation
    c1 = cmd("commitments.reserve", "ben", {"baseline_id": base["id"]}, example="Reserve the commitment")
    c2 = cmd("commitments.reserve", "ben", {"baseline_id": base["id"]})
    check("MVP-104", "Commit the approved portfolio without double-allocating resources",
          c1["outcome"] == "accepted" and c2["outcome"] == "refused" and c2["refusal"]["code"] == "DOUBLE_ALLOCATION")
    check("8.0", "A commitment shows Committed, Funded but incomplete, and Advisory as separate axes",
          c1["status"]["lifecycle_state"] == "Committed" and c1["status"]["delivery_readiness"] == "Funded but incomplete" and c1["status"]["legal_status"]["value"] == "Advisory")
    again = cmd("commitments.reserve", "ben", {"baseline_id": base["id"]}, command_id=c1["_command_id"])
    check("8.1", "Resending a command with the same command_id returns the original result and creates nothing",
          again["transaction_id"] == c1["transaction_id"] and again["outcome"] == "accepted")

    # ---- MVP-105 actuals do not alter baseline
    funded = {k: v for k, v in base["allocations"].items() if v > 0}
    node = sorted(funded)[0]
    a1 = cmd("actuals.post", "ben", {"civic_body_id": cb, "node_id": node, "actual_cost": funded[node] + 4000, "observed_at": "2027-03-31"}, example="Post an actual")
    a2 = cmd("actuals.post", "ben", {"civic_body_id": cb, "node_id": node, "actual_cost": 1, "observed_at": "2027-04-01", "attempt_baseline_update": True})
    after = q(f"/v0/queries/baselines/{base['id']}")["versions"]
    check("MVP-105", "Post actuals without altering the baseline",
          a1["outcome"] == "accepted" and a2["refusal"]["invariant_id"] == "EXE-BASELINE-001" and len(after) == 1 and after[0]["allocations"] == base["allocations"])

    # ---- MVP-106 within-envelope rebalance
    m = mv
    cost = {n["id"]: n["cost"] for n in m["nodes"]}
    lvl = sol["levels"]
    water = m["constraints"][0]["coefficients"]
    crew = m["constraints"][1]["coefficients"]
    grant = {i for i, *_, g in NODES if g}
    def fits(f, t, amt):  # independent check that a move keeps every hard constraint
        nl = dict(lvl); nl[f] -= amt / cost[f]; nl[t] += amt / cost[t]
        if nl[t] > 1 or nl[f] < 0:
            return False
        return all(sum(v * nl[k] for k, v in c["coefficients"].items()) <= c["limit"] + 1e-6 for c in m["constraints"])
    from_n, to_n = next((f, t) for f in sorted(cost) for t in sorted(cost)
                        if f != t and f not in grant and t not in grant and base["allocations"][f] >= 10000 and fits(f, t, 10000))
    rb = cmd("rebalances.propose", "ben", {"civic_body_id": cb, "decision_class": "routine_rebalance", "from_node_id": from_n, "to_node_id": to_n,
             "amount": 10000, "confidence": 0.95, "reversibility": 3}, example="Propose a routine rebalance")
    check("MVP-106", "A within-envelope variance is resolved by delegated rebalance", rb["outcome"] == "accepted" and rb["status"]["lifecycle_state"] == "Resolved",
          f"moved $10,000 {from_n} -> {to_n}")
    noconf = cmd("rebalances.propose", "ben", {"civic_body_id": cb, "decision_class": "routine_rebalance", "from_node_id": from_n, "to_node_id": to_n, "amount": 1000, "reversibility": 3})
    check("5.9", "A rebalance whose inputs carry no calibrated confidence fails closed and escalates",
          noconf["outcome"] == "escalated" and any("no calibrated confidence" in f for f in noconf["escalation"]["failed_tests"]))
    dis = cmd("rebalances.propose", "ben", {"civic_body_id": cb, "decision_class": "minor_rebalance", "from_node_id": from_n, "to_node_id": to_n, "amount": 100, "confidence": 0.99, "reversibility": 3})
    check("5.9", "An envelope with invalid parameters escalates every candidate action", dis["outcome"] == "escalated")

    # ---- UIX-NEUTRAL-004 same refusal on mobile and desktop
    big = {"civic_body_id": cb, "decision_class": "routine_rebalance", "from_node_id": from_n, "to_node_id": to_n, "amount": 60000, "confidence": 0.95, "reversibility": 3}
    dk = cmd("rebalances.propose", "ben", big)
    mb = cmd("rebalances.propose", "ben", big, client="mobile")
    check("UIX-NEUTRAL-004", "An out-of-envelope approval is escalated identically on mobile and desktop",
          dk["outcome"] == mb["outcome"] == "escalated" and dk["escalation"]["failed_tests"] == mb["escalation"]["failed_tests"])

    # ---- MVP-107 hard-constraint breach -> Exception Proposition
    wnode = max(water, key=water.get)
    br = cmd("rebalances.propose", "ben", {"civic_body_id": cb, "decision_class": "routine_rebalance", "from_node_id": from_n, "to_node_id": wnode,
             "amount": 20000, "confidence": 0.95, "reversibility": 3})
    exc = br.get("escalation") or {}
    check("MVP-107", "A hard-constraint breach produces an Exception Proposition naming the conflict and the authority required",
          br["outcome"] == "escalated" and "hard constraint" in exc.get("governing_conflict", "") and exc.get("authority_required"),
          exc.get("governing_conflict", ""))

    # ---- MVP-108 approve changed state; prior baseline preserved
    def decide_exception(e_id, title, apply, relax=None):
        ra = {"type": "resolve_exception", "exception_id": e_id, "apply": apply}
        if relax:
            ra["relax"] = relax
        p = cmd("propositions.submit", "ana", {"civic_body_id": cb, "decision_class": "annual_budget", "title": title, "body": title, "requested_action": ra})
        vote_all(p["result"]["proposition"]["id"], {"ana": "yes", "ben": "yes", "cara": "yes", "dev": "no"})
        return cmd("decisions.close", "ana", {"proposition_id": p["result"]["proposition"]["id"]})["result"]["decision"]

    water_move = {"from_node_id": from_n, "to_node_id": wnode, "amount": 20000}
    bad_d = decide_exception(exc["exception_proposition_id"], "Approve the water-intensive move as proposed", water_move)
    infeasible = cmd("exceptions.resolve", "ben", {"exception_proposition_id": exc["exception_proposition_id"], "resolution": "Approved as proposed",
                     "decision_id": bad_d["id"]})
    check("G-059", "An exception resolution that would breach a hard constraint is refused, even with an approved decision",
          infeasible["outcome"] == "refused" and infeasible["refusal"]["code"] == "HARD_CONSTRAINT")
    rp = cmd("propositions.submit", "ana", {"civic_body_id": cb, "decision_class": "annual_budget", "title": f"Resolve {exc['exception_proposition_id']}",
             "body": "Decline the water-intensive move; shift $5,000 instead.",
             "requested_action": {"type": "resolve_exception", "exception_id": exc["exception_proposition_id"],
                                  "apply": {"from_node_id": from_n, "to_node_id": to_n, "amount": 5000}}})
    vote_all(rp["result"]["proposition"]["id"], {"ana": "yes", "ben": "yes", "cara": "yes", "dev": "no"})
    rd = cmd("decisions.close", "ana", {"proposition_id": rp["result"]["proposition"]["id"]})["result"]["decision"]
    rs = cmd("exceptions.resolve", "ben", {"exception_proposition_id": exc["exception_proposition_id"], "resolution": "Declined; alternative shift approved",
             "decision_id": rd["id"]}, example="Resolve an exception by decision")
    hist = q(f"/v0/queries/baselines/{base['id']}")["versions"]
    check("MVP-108", "Approve a changed state; the prior baseline and decision lineage are preserved",
          rs["outcome"] == "accepted" and len(hist) == 3 and hist[0]["allocations"] == base["allocations"] and hist[2]["supersedes"] == hist[1]["version_id"])
    again = cmd("exceptions.resolve", "ben", {"exception_proposition_id": exc["exception_proposition_id"], "resolution": "again", "decision_id": rd["id"]})
    br2 = cmd("rebalances.propose", "ben", {"civic_body_id": cb, "decision_class": "routine_rebalance", "amount": 20000, "confidence": 0.95, "reversibility": 3,
              "from_node_id": from_n, "to_node_id": wnode})
    exc2 = br2["escalation"]["exception_proposition_id"]
    relax_d = decide_exception(exc2, "Approve the move and raise the watershed ceiling to 40 ML/yr", water_move,
                               [{"constraint_id": "eco-water-ceiling", "limit": 40}])
    relaxed = cmd("exceptions.resolve", "ben", {"exception_proposition_id": exc2, "resolution": "Approved with a recorded relaxation",
                  "decision_id": relax_d["id"]}, example="Resolve an exception with a recorded constraint relaxation")
    pm = relaxed.get("result", {}).get("portfolio_model", {})
    wc = next((c for c in pm.get("constraints", []) if c["id"] == "eco-water-ceiling"), {})
    check("G-059", "A closed exception cannot be resolved again; a relaxation the decision names is recorded as a new constraint version",
          again["refusal"]["code"] == "STATE" and relaxed["outcome"] == "accepted" and wc.get("limit") == 40 and wc.get("previous_limit") == 20
          and wc.get("relaxed_by_decision_id") == relax_d["id"] and relaxed["result"]["baseline"]["model_version_id"] == pm["version_id"],
          f"{pm.get('version_id')}: limit 20 -> 40")

    # ---- MVP-109 replay
    rep = q(f"/v0/queries/decisions/{dec_a['id']}/replay")
    check("MVP-109", "Replay the original decision from its historical snapshot", rep["reproduced"], rep["replayed_result_hash"][:16])

    # ---- INV-AT-04 uncertain evidence
    ev = cmd("evidence.record", "cara", {"civic_body_id": cb, "subject": "Projected 2030 watershed yield", "value": 18,
             "epistemic_class": "Estimated", "confidence": 0.7, "source": "County hydrology model"}, example="Record estimated evidence")
    at = cmd("constraints.attach-evidence", "cara", {"constraint_id": "eco-water-ceiling", "evidence_id": ev["result"]["evidence"]["id"]})
    evid = ev["result"]["evidence"]["id"]
    at_wrong = cmd("constraints.attach-evidence", "cara", {"constraint_id": "eco-water-ceiling", "evidence_id": evid, "adopted_by_decision_id": dec_a["id"]})
    dec_ev = approve("Adopt the 2030 watershed yield estimate", {"type": "adopt_evidence", "evidence_id": evid, "constraint_id": "eco-water-ceiling"})
    at_other = cmd("constraints.attach-evidence", "cara", {"constraint_id": "crew-capacity", "evidence_id": evid, "adopted_by_decision_id": dec_ev["id"]})
    at2 = cmd("constraints.attach-evidence", "cara", {"constraint_id": "eco-water-ceiling", "evidence_id": evid, "adopted_by_decision_id": dec_ev["id"]},
              example="Attach evidence adopted by a decision")
    at3 = cmd("constraints.attach-evidence", "cara", {"constraint_id": "eco-water-ceiling", "evidence_id": evid, "adopted_by_decision_id": dec_ev["id"]})
    check("G-054", "Evidence adoption needs the decision that adopted that evidence for that constraint, and uses it once",
          at_wrong["refusal"]["code"] == "APPROVAL_MISMATCH" and at_other["refusal"]["code"] == "APPROVAL_MISMATCH"
          and at3["refusal"]["code"] == "APPROVAL_ALREADY_USED")
    check("INV-AT-04", "Estimated evidence cannot become a binding constraint until a decision adopts it",
          at["outcome"] == "refused" and at["refusal"]["invariant_id"] == "EVD-NORM-001" and at2["outcome"] == "accepted")

    # ---- INV-AT-13 eligibility tiers (CL-028 configuration)
    cmd("credentials.issue", "ana", {"civic_body_id": cb, "member_actor_id": "gil", "tier": "self_attested", "attestation_confidence": 0.6}, example="Issue a self-attested credential")
    pp = cmd("propositions.submit", "cara", {"civic_body_id": cb, "decision_class": "advisory_poll", "title": "Name the new trail", "body": "Advisory naming poll.",
             "requested_action": {"type": "advisory"}})
    ppid = pp["result"]["proposition"]["id"]
    g1 = cmd("votes.cast", "gil", {"proposition_id": ppid, "choice": "yes"})
    g2 = cmd("propositions.submit", "gil", {"civic_body_id": cb, "decision_class": "annual_budget", "title": "x", "body": "x", "requested_action": {"type": "advisory"}})
    vote_all(ppid, {"cara": "yes"})
    pd = cmd("decisions.close", "ana", {"proposition_id": ppid})["result"]["decision"]
    check("INV-AT-13", "A self-attested member takes part where the decision class allows it and is refused where it requires verification; low-confidence result flagged",
          g1["outcome"] == "accepted" and g2["refusal"]["code"] == "ATTESTATION_TIER" and pd["low_confidence"])

    # ---- 8.9 version binding
    open_p = cmd("propositions.submit", "cara", {"civic_body_id": cb, "decision_class": "annual_budget", "title": "Add a bus shelter study",
                 "body": "Advisory study.", "requested_action": {"type": "advisory"}})
    opid = open_p["result"]["proposition"]["id"]
    proc_id = q(f"/v0/queries/civic-bodies/{cb}")["governance_process"]["id"]
    newc = q(f"/v0/queries/civic-bodies/{cb}")["governance_process"]["decision_classes"]
    newc = [dict(c) for c in newc]; newc[0]["approval_threshold"] = 0.9

    def approve_change(title, changes):
        p = cmd("propositions.submit", "ana", {"civic_body_id": cb, "decision_class": "change_control", "title": title, "body": title,
                "requested_action": {"type": "approve_change", "target_id": proc_id, "change_hash": sha(changes)}})
        vote_all(p["result"]["proposition"]["id"], {"ana": "yes", "ben": "yes", "cara": "yes", "dev": "yes"})
        return cmd("decisions.close", "ana", {"proposition_id": p["result"]["proposition"]["id"]})["result"]["decision"]

    cd = approve_change("Raise annual_budget threshold to 90%", {"decision_classes": newc})
    other = [dict(c) for c in newc]; other[0]["approval_threshold"] = 0.95
    mism = cmd("change-requests.put-in-force", "ana", {"civic_body_id": cb, "target_type": "governance_process", "target_id": proc_id,
               "changes": {"decision_classes": other}, "decision_id": cd["id"]})
    pf = cmd("change-requests.put-in-force", "ana", {"civic_body_id": cb, "target_type": "governance_process",
             "target_id": proc_id, "changes": {"decision_classes": newc}, "decision_id": cd["id"]},
             example="Put an approved change in force")
    reuse = cmd("change-requests.put-in-force", "ana", {"civic_body_id": cb, "target_type": "governance_process", "target_id": proc_id,
                "changes": {"decision_classes": newc}, "decision_id": cd["id"]})
    check("CL-046", "A change that differs from the approved one is refused, and an approval puts its change in force only once",
          mism["outcome"] == "refused" and mism["refusal"]["code"] == "CHANGE_MISMATCH" and pf["outcome"] == "accepted"
          and reuse["outcome"] == "refused" and reuse["refusal"]["code"] == "CHANGE_ALREADY_APPLIED")
    sneak = [dict(c) for c in newc]; sneak[4]["participation_fee"] = 2
    cd2 = approve_change("Charge a fee for polls", {"decision_classes": sneak})
    fee = cmd("change-requests.put-in-force", "ana", {"civic_body_id": cb, "target_type": "governance_process",
              "target_id": proc_id, "changes": {"decision_classes": sneak}, "decision_id": cd2["id"]})
    check("INV-AT (24)", "Even an approved change cannot introduce a participation fee that adoption would refuse",
          fee["outcome"] == "refused" and fee["refusal"]["invariant_id"] == "TRU-ACCESS-001")
    vote_all(opid, {"ana": "yes", "ben": "yes", "cara": "yes", "dev": "no", "fay": "no"})
    od = cmd("decisions.close", "ana", {"proposition_id": opid})["result"]["decision"]
    check("8.9", "A change in force does not apply to a transaction already in progress (bound process version used)",
          pf["outcome"] == "accepted" and od["process_version_id"] == proc_v1 and od["result"] == "approved", "3 of 5 = 60% passed under the bound 50% rule")

    # ---- INV-AT-26 / CMP-006 Legal Effect Declaration
    cmd("legal-effect-declarations.adopt", "ana", {"civic_body_id": cb, "decision_class": "advisory_poll", "legal_status": "Consultative",
        "enabling_authority": "Riverbend Charter s. 4.2 (fixture)", "effective_date": "2027-01-01"}, example="Adopt a Legal Effect Declaration")
    pp2 = cmd("propositions.submit", "cara", {"civic_body_id": cb, "decision_class": "advisory_poll", "title": "Second poll", "body": "x", "requested_action": {"type": "advisory"}})
    vote_all(pp2["result"]["proposition"]["id"], {"cara": "yes", "ana": "yes"})
    d2 = cmd("decisions.close", "ana", {"proposition_id": pp2["result"]["proposition"]["id"]})
    old = q(f"/v0/queries/decisions/{pd['id']}")
    check("CMP-006", "With a Legal Effect Declaration the label shows its status and cited authority; earlier decisions keep theirs",
          d2["status"]["legal_status"]["value"] == "Consultative" and d2["status"]["legal_status"]["enabling_authority"] and old["status"]["legal_status"]["value"] == "Advisory")

    # ---- MVP-111 / UIX-NEUTRAL-001/002 assistant boundary
    same = {"civic_body_id": cb, "decision_class": "advisory_poll", "title": "Library hours poll", "body": "Should Saturday hours extend to 6pm?", "requested_action": {"type": "advisory"}}
    s_desk = cmd("propositions.submit", "cara", same)
    s_ai0 = cmd("propositions.submit", "cara", same, client="assistant")
    s_ai = cmd("propositions.submit", "cara", same, client="assistant", confirm="cara", example="Assistant-drafted proposition with human confirmation")
    s_mob = cmd("propositions.submit", "cara", same, client="mobile")
    strip = lambda r: {k: v for k, v in r["result"]["proposition"].items() if k not in ("id", "version_id", "created_in_transaction", "client", "supersedes")}
    check("UIX-NEUTRAL-002", "The assistant cannot submit without an explicit human confirmation of the exact payload",
          s_ai0["outcome"] == "refused" and s_ai0["refusal"]["code"] == "AI_CONFIRMATION_REQUIRED")
    check("UIX-NEUTRAL-001", "Desktop, assistant, and mobile submissions produce identical governed propositions",
          strip(s_desk) == strip(s_ai) == strip(s_mob))
    ai_bypass = cmd("commitments.reserve", "cara", {"baseline_id": base["id"]}, client="assistant", confirm="cara")
    check("MVP-111", "The AI interface cannot bypass a failed authority check, even with confirmation",
          ai_bypass["outcome"] == "refused" and ai_bypass["refusal"]["code"] == "AUTHORITY_MISSING")

    # ---- UIX-NEUTRAL-003 feed
    feed = q("/v0/queries/feed/gil")
    eng = cmd("configuration.set", "ana", {"civic_body_id": cb, "setting": "feed.ranking", "value": "engagement"})
    check("UIX-NEUTRAL-003", "Every feed item states why it is shown; ranking for engagement is not configurable",
          feed["items"] and all(i["reason_shown"] for i in feed["items"]) and eng["outcome"] == "refused")

    # ---- CMP-001 Assurance Controls cannot be disabled
    off = cmd("configuration.set", "ana", {"civic_body_id": cb, "setting": "asr.audit_log", "value": False},
              example="Attempt to disable an Assurance Control (refused)")
    check("CMP-001", "A configuration change that disables an Assurance Control is refused, citing the layer rule",
          off["outcome"] == "refused" and off["refusal"]["invariant_id"] == "GOV-FRAMEWORK-001" and off["refusal"]["control_id"] == "ASR-04")

    # ---- CMP-005 retention
    cmd("retention-schedules.adopt", "ana", {"civic_body_id": cb, "record_class": "deliberation_post", "retain_days": 730,
        "destruction_authority": "records_officer", "legal_basis": "Pilot-state records schedule (to confirm)"}, example="Adopt a retention schedule")
    post_id = pub["result"]["post"]["id"]
    early = cmd("records.delete", "ben", {"record_id": post_id, "record_class": "deliberation_post", "created_days_ago": 30})
    ok = cmd("records.delete", "ben", {"record_id": post_id, "record_class": "deliberation_post", "created_days_ago": 800},
             example="Delete a record after its retention period")
    evs = q("/v0/queries/events")["events"]
    check("CMP-005", "Deletion before the schedule allows is refused; an authorized deletion succeeds and is recorded",
          early["outcome"] == "refused" and ok["outcome"] == "accepted" and any(e["type"] == "record.deleted" for e in evs))

    # ---- MVP-110 / CMP-007 / CMP-012 export and exit
    ex = cmd("exports.create", "ana", {"civic_body_id": cb}, example="Export the civic body")
    pkg = q(f"/v0/queries/exports/{ex['result']['export']['id']}")
    chain_ok, n = verify_chain(pkg["events"])
    fresh = rehydrate(pkg)
    rep2 = fresh.q_replay(dec_a["id"])
    check("MVP-110", "Export the civic state in a documented machine-readable package sufficient for independent reconstruction",
          pkg["format"] == "acecog-export/0.1" and len(pkg["versions"]) > 20)
    check("CMP-012", "A third party verifies the event log's hash chain from the export alone", chain_ok, f"{n} events verified")
    check("CMP-007", "The export rehydrates into a fresh instance and replay yields identical outcomes",
          rep2["replayed_result_hash"] == rep["original_result_hash"])
    tampered = json.loads(json.dumps(pkg))
    tampered["events"][5]["data"]["tampered"] = True
    check("ASR-04", "A tampered export is detected", not verify_chain(tampered["events"])[0])
    check("8.1", "Refused and escalated commands are recorded in the event log",
          any(e["type"] == "command.refused" for e in evs) and any(e["type"] == "command.escalated" for e in evs))


def write_reports():
    passed = sum(1 for r in RESULTS if r[2])
    lines = ["# ACECOG API: contract test results", "",
             f"Scenario: Riverbend Commons (26.1). {passed} of {len(RESULTS)} checks passed.", "",
             "| Test | Check | Result | Detail |", "| --- | --- | --- | --- |"]
    lines += [f"| {t} | {d} | {'pass' if ok else 'FAIL'} | {x} |" for t, d, ok, x in RESULTS]
    open(os.path.join(API_DOCS, "contract-test-results.md"), "w").write("\n".join(lines) + "\n")
    json.dump(EXAMPLES, open(os.path.join(API_DOCS, "examples.json"), "w"), indent=1)
    return passed


if __name__ == "__main__":
    run_all()
    p = write_reports()
    for t, d, ok, x in RESULTS:
        print(f"{'PASS' if ok else 'FAIL'}  {t:16} {d}" + (f"  [{x}]" if x else ""))
    print(f"\n{p}/{len(RESULTS)} passed")
    sys.exit(0 if p == len(RESULTS) else 1)
