# ACECOG API

The API is the system's front counter: the full list of requests any app can make ("submit a proposition", "show me this
decision's record", "propose a rebalance") and exactly what comes back, including refusals and escalations.

| File | What it is |
| --- | --- |
| `openapi.yaml` | The contract in OpenAPI 3.1. Paste it into any OpenAPI viewer (for example editor.swagger.io) for a clickable reference. Generated from `src/acecog/contract.py`; do not edit by hand. |
| `schemas/` | JSON Schema for every Section 7 object (38) and every Section 8 process record the engine stores (12), each extending `ObjectHeader`. Each file says whether Phase 1 builds the object or defines only its interface (13.6). Generated from `src/acecog/schemas.py`. |
| `examples.json` | Worked request examples recorded by the contract scenario. |
| `contract-test-results.md` | The latest run of the contract scenario (Riverbend Commons, spec 26.1). |

## How it is organized

* **Commands** change state: `POST /v0/commands/<name>`. **Queries** only read: `GET /v0/queries/...` (spec 11.6.2).
* Every command arrives in the same envelope from every client (desktop, assistant, mobile) and returns one of three outcomes:
  `accepted` (200), `escalated` (202, an Exception Proposition was raised), or `refused` (422, naming the rule that refused it,
  usually an invariant ID from spec Section 14). A refused command changes nothing except the record of its refusal.
* Every result carries the four status axes of spec 8.0. Nothing is labeled binding without a Legal Effect Declaration.
* An assistant-drafted command needs `human_confirmation`: the person who reviewed it and the hash of the exact payload (24.3).
* Every transaction binds to the rule versions in force when it starts (8.9) and reports them in `bound_versions`.
* An approved change goes in force once, exactly as approved (CL-046; decision record 0002).
* The event log is hash-chained (ASR-04). An export can be verified and rehydrated without operator tools (CMP-007, CMP-012).

## Questions the contract raised for the specification

All four (CL-044 to CL-047) were decided on 9 November 2026 and are now in the spec (Appendix M.6). CL-046 is built.
Current implementation limitations are listed in `docs/capabilities/capability-matrix.md`.

## Keeping it current

`python scripts/gen_openapi.py` regenerates `openapi.yaml` and `schemas/`. CI fails if either is out of date with the code.
