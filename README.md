# ACECOG CivicOS

ACECOG (Accelerated Ecological Governance) is civic software for making, planning, carrying out and auditing community decisions under rules adopted by people. This repository contains the shared prototype engine, API/schema contracts, tests and an engine-generated synthetic walkthrough.

**Pre-release:** caller authentication and parts of Phase 1 are incomplete. Run the development API locally only; do not expose it to the internet or use it for real civic records, binding decisions or financial execution. The reference community and scenario data are synthetic. Source availability does not authorize a website or civic deployment.

## Run and verify

Python 3.11 or newer:

```
python -m venv .venv
. .venv/bin/activate
pip install -r requirements-ci.txt
python -m pytest -q
python scripts/gen_openapi.py
python scripts/build_capability_matrix.py
python scripts/build_site.py
python scripts/run_server.py
```

The server binds to loopback by default. `build/site/` is a static, read-only walkthrough built by running the real engine; publishing it requires separate review. There is no deployment job in this source candidate.

The tests cover governance approvals/refusals, resource constraints, replay/export, durable storage, schemas, capability freshness and the static reference. They do not demonstrate completion of every specified feature or journey. The technical status snapshot records 27 of 88 Phase 1 acceptance criteria covered; passing the repository suite does not change that denominator.

## Technical references

- [API and schemas](docs/api/README.md)
- [Capability evidence and current limits](docs/capabilities/capability-matrix.md)
- [Functional specification v0.24](docs/spec/acecog-spec-v0.24.md): §13.6 controls Phase 1 scope; specified features are not all implemented
- [Security reporting](SECURITY.md) and [contribution policy](CONTRIBUTING.md)

The canonical technical specification is retained verbatim. Its historical pilot-planning references are design context, not a current public project schedule, budget or promise. Internal work plans, market-rate budgets, PMO records, proprietary edition content and development-history archives are not part of this source export.

## License and contributions

The source carries [AGPL-3.0](LICENSE). Third-party dependencies retain their own licenses. Outside contributions remain paused until the required contributor agreement and review process are in place. No commercial license, IP-ownership certification, legal authority or audit certification is asserted by this source candidate.
