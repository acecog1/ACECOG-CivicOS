# Contributing

ACECOG source is licensed under AGPL-3.0; see LICENSE. Outside contributions are not accepted for merge until the required contributor agreement has been reviewed and adopted. Do not submit private civic records, credentials, customer data or proprietary edition material.

For technical changes, preserve the specification's authority, provenance, privacy and invariant boundaries. Add meaningful tests for changed behavior; run `python -m pytest`, regenerate API/schema and capability evidence when affected, and include reproducible results. Proposed changes require human review; a passing test or an AI recommendation is not release approval.

Report vulnerabilities privately using SECURITY.md. Public issues must contain only public-safe, synthetic examples.

## Shared ACECOG delivery team, separate product boundaries

The ACECOG Owner and shared engineering, PMO, quality, security/licensing, accessibility and release roles work on both **public ACECOG-CivicOS** and the separate **private ACECOG-Commercial** edition. A common role roster does **not** make private commercial material, customer information, internal planning, strategy or source available for public issues or pull requests, and it does not grant contributors or agents access to the private repository.

Public CivicOS is the upstream open core. Commercial integration is by a separately reviewed and version-pinned dependency or compatible package, with contract, invariant, license and security tests; **never automatically mirror a public branch, disclose private code, or replace the public core with a commercial fork**. Each repository maintains independent change review, legal/security, deployment and publication approval. The private PMO handles cross-track task routing and evidence; routine review does not confer a release Go. The Owner retains material policy, funding and final beta/release gates. No new contributor agreement, public commercial access, commercial license or product availability is granted by this staffing clarification.
