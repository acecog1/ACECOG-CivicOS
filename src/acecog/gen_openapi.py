"""Generate docs/api/openapi.yaml from contract.py and the examples recorded by tests/scenario.py.

    python scripts/gen_openapi.py
"""
import json, os, re, sys
import yaml
from . import contract, schemas

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "..", "docs", "api")

GROUPS = {
    "Civic body and rules": ["civic-bodies.create", "governance-processes.adopt", "authorities.grant", "delegation-envelopes.adopt",
                             "legal-effect-declarations.adopt", "compliance-packs.adopt", "change-requests.put-in-force"],
    "Membership and participation": ["credentials.issue", "interest-declarations.record", "delegations.assign", "delegations.revoke",
                                     "propositions.submit", "propositions.amend", "deliberation.post", "votes.cast", "decisions.close"],
    "Evidence and optimization": ["evidence.record", "constraints.attach-evidence", "optimization-runs.request"],
    "Baseline, commitment, execution": ["baselines.create", "commitments.reserve", "actuals.post", "rebalances.propose", "exceptions.resolve"],
    "Records, exit, configuration": ["exports.create", "retention-schedules.adopt", "records.delete", "configuration.set"],
}

DESCRIPTION = """\
**What this is.** The front counter of the ACECOG Civic OS: every request any client (desktop, conversational assistant, mobile)
can make, and exactly what comes back, including refusals and escalations. Derived from the ACECOG specification (v0.24),
Sections 7 (objects), 8 (state machines), 9 (provenance), 11.6 (one API, three clients), 14 (invariants), and 43.2 (Assurance Controls).

**Two halves (11.6.2).** *Commands* change state and are all `POST /v0/commands/<name>`. *Queries* only read and are all `GET /v0/queries/...`.

**Every command is a governed transaction (8.1).** It arrives in a `CommandEnvelope`, independently re-checks authority,
binds to the rule versions in force when it starts (8.9), and returns a `CommandResult` whose `outcome` is one of:

* `accepted` (HTTP 200): the change happened; `result` holds the new object versions.
* `escalated` (HTTP 202): the action was routed to human authority as an Exception Proposition; nothing was decided automatically.
* `refused` (HTTP 422): nothing changed; `refusal` names the rule, usually by invariant ID, so the reason can be traced to the spec.

Refused and escalated commands are still recorded in the hash-chained event log.

**Status (8.0).** Decisions, commitments and published results carry four separate status axes. Nothing is labeled binding
without a Legal Effect Declaration (invariant 26 ASR-STATUS-001).

**Assistant-drafted commands** must carry `human_confirmation` naming the person who reviewed the exact payload (24.3).

**MVP status.** The reference implementation stores everything in one local SQLite file (spec 11.5) and solves with a
small deterministic LP/QP solver (Phase 1 profile, 13.1). Caller authentication (WBS 1.3.2) is not yet in place: the
actor_id in each command is trusted. Do not use for real decisions until it is.
"""


def build():
    ex_path = os.path.join(ROOT, "examples.json")
    examples = json.load(open(ex_path)) if os.path.exists(ex_path) else {}
    doc = {"openapi": "3.1.0",
           "info": {"title": "ACECOG Civic OS API", "version": contract.API_VERSION,
                    "summary": f"Command and query contract derived from {contract.SPEC_VERSION} (change log CL-041).",
                    "description": DESCRIPTION, "license": {"name": "Draft for review"}},
           "servers": [{"url": "http://127.0.0.1:8765", "description": "Local installation"}],
           "tags": [{"name": g} for g in GROUPS] + [{"name": "Queries"}],
           "paths": {}, "components": {"schemas": dict(contract.SCHEMAS)}}
    for group, names in GROUPS.items():
        for name in names:
            summary, refs, enforces = contract.COMMANDS[name]
            pname = "Payload_" + re.sub(r"[^A-Za-z0-9]", "_", name)
            doc["components"]["schemas"][pname] = contract.P[name]
            body = {"allOf": [{"$ref": "#/components/schemas/CommandEnvelope"},
                              {"type": "object", "properties": {"payload": {"$ref": f"#/components/schemas/{pname}"}}}]}
            op = {"tags": [group], "operationId": name.replace(".", "_").replace("-", "_"), "summary": summary,
                  "description": f"Specification: {refs}." + (f" Enforces: {', '.join(enforces)}." if enforces else ""),
                  "x-spec-refs": refs, "x-enforces": enforces,
                  "requestBody": {"required": True, "content": {"application/json": {"schema": body}}},
                  "responses": {code: {"description": d, "content": {"application/json": {"schema": {"$ref": "#/components/schemas/CommandResult"}}}}
                                for code, d in (("200", "Accepted"), ("202", "Escalated to human authority"),
                                                ("422", "Refused by a governance rule"), ("400", "Malformed request"))}}
            if name in examples:
                op["requestBody"]["content"]["application/json"]["examples"] = {
                    k: {"summary": v["summary"], "value": v["envelope"]} for k, v in examples[name].items()}
            doc["paths"][f"/v0/commands/{name}"] = {"post": op}
    for path, (summary, refs) in contract.QUERIES.items():
        params = [{"name": p, "in": "path", "required": True, "schema": {"type": "string"}} for p in re.findall(r"{([^}]+)}", path)]
        if path.endswith("/events"):
            params.append({"name": "after", "in": "query", "schema": {"type": "integer"}, "description": "Return events after this sequence number."})
        schema = {"$ref": "#/components/schemas/DecisionProvenancePacket"} if path.endswith("/provenance") else {"type": "object"}
        doc["paths"][path] = {"get": {"tags": ["Queries"], "operationId": "q_" + re.sub(r"[^a-z0-9]+", "_", path.split("queries/")[1]).strip("_"),
                                      "summary": summary, "description": f"Specification: {refs}.", "x-spec-refs": refs,
                                      "parameters": params,
                                      "responses": {"200": {"description": "OK", "content": {"application/json": {"schema": schema}}},
                                                    "404": {"description": "Not found"}}}}
    # Section 7 domain objects and Section 8 process records live as standalone JSON Schema files.
    for name, sch in schemas.all_schemas().items():
        doc["components"]["schemas"][f"domain.{name}"] = {
            "$ref": f"schemas/{name}.schema.json",
            "description": f"{sch.get('x-acecog-object', name)} (Section {sch.get('x-acecog-section', '7')}; "
                           f"Phase 1: {sch.get('x-acecog-phase1', 'build')})."}
    return doc


def write_schemas():
    d = os.path.join(ROOT, "schemas")
    os.makedirs(d, exist_ok=True)
    keep = set()
    for name, sch in schemas.all_schemas().items():
        f = f"{name}.schema.json"
        keep.add(f)
        with open(os.path.join(d, f), "w") as fh:
            json.dump(sch, fh, indent=2, ensure_ascii=False)
            fh.write("\n")
    for f in os.listdir(d):
        if f.endswith(".schema.json") and f not in keep:
            os.remove(os.path.join(d, f))
    return len(keep)


if __name__ == "__main__":
    out = os.path.join(ROOT, "openapi.yaml")
    yaml.safe_dump(build(), open(out, "w"), sort_keys=False, allow_unicode=True, width=120)
    print("wrote", out)
    print("wrote", write_schemas(), "schema files to", os.path.join(ROOT, "schemas"))
