# Technical capability evidence

API 0.1.0; ACECOG v0.24. Scenario: 55/55 checks. Exercised API capabilities: 38/40.

These are bounded scenario checks, not full Phase 1 acceptance. Source inclusion does not enable a public service or civic authority. Exposure modes remain proposed; mutable operations require their authentication, isolation, abuse and release gates.

| Capability | Summary | Spec | Status | Scenario proof | Proposed mode | Release blockers |
|---|---|---|---|---|---|---|
| `civic-bodies.create` | Create a civic body with its founding members. | 7, 17.2, MVP-100 | Tested | INV-AT (24) | P-3 | G-041 auth; B-1 tenancy; B-2 quotas; G-042 threat model; G-023 |
| `governance-processes.adopt` | Adopt the rules for how each kind of decision is made: method, threshold, and w… | 17.5, 4.2 | Tested | INV-AT (24), INV-AT-17 | P-2 | G-041 auth; B-1 tenancy; B-2 quotas; G-042 threat model |
| `authorities.grant` | Give a person or role the authority to do specific things. | 7, 12.0.1, 23.1 | Tested | G-054, G-055, INV-AT-17 | P-2 | G-041 auth; B-1 tenancy; B-2 quotas; G-042 threat model |
| `delegation-envelopes.adopt` | Set the bounded space inside which routine decisions may be made automatically. | 5.9, 8.7 | Tested | 5.9 | P-2 | G-041 auth; B-1 tenancy; B-2 quotas; G-042 threat model |
| `legal-effect-declarations.adopt` | Record which law or charter gives a class of decisions legal effect. | 43.2 ASR-08, 8.0 | Tested | CMP-006 | Off | none claimed |
| `compliance-packs.adopt` | Adopt a jurisdiction's legal rule bundle. Packs may only add constraints. | 43.4 | Tested | CMP-002, CMP-003 | Eval | G-041 auth; B-1 tenancy; B-2 quotas; G-042 threat model |
| `credentials.issue` | Record that a member is a unique, eligible member at an identity tier. | 7, 17.5 | Tested | INV-AT-13 | P-2 | G-041 auth; B-1 tenancy; B-2 quotas; G-042 threat model |
| `interest-declarations.record` | Declare a personal interest in a proposition; this blocks deliberating and voti… | 43.4, 43.7 | Tested | CMP-004 | P-2 | G-041 auth; B-1 tenancy; B-2 quotas; G-042 threat model |
| `delegations.assign` | Delegate your participation in a decision class to another member. | 17.3; CL-029 | Tested | 17.3 | P-2 | G-041 auth; B-1 tenancy; B-2 quotas; G-042 threat model |
| `delegations.revoke` | Withdraw a delegation. | 17.3 | Tested | 17.3 | P-2 | G-041 auth; B-1 tenancy; B-2 quotas; G-042 threat model |
| `propositions.submit` | Submit a frozen proposition version for a decision. | 8.3, MVP-101 | Tested | CL-046, CMP-006, G-054, G-059, INV-AT (24), INV-AT-13, MVP-101, MVP-108, UIX-NEUTRAL-002 | P-2 | G-041 auth; B-1 tenancy; B-2 quotas; G-042 threat model |
| `propositions.amend` | Amend a proposition. Creates a new version; the old version stays. | 8.4 | Tested | MVP-101 | P-2 | G-041 auth; B-1 tenancy; B-2 quotas; G-042 threat model |
| `deliberation.post` | Post to the deliberation record on a proposition. | 8.4, 43.4.1 | Tested | CMP-003, CMP-004 | P-2 | G-041 auth; B-1 tenancy; B-2 quotas; G-042 threat model |
| `votes.cast` | Vote or consent on a proposition. | 17.3, 17.5 | Tested | 8.9, CL-046, CMP-004, CMP-006, G-054, G-059, INV-AT (24), INV-AT-13, MVP-102, MVP-108 | P-2 | G-041 auth; B-1 tenancy; B-2 quotas; G-042 threat model |
| `decisions.close` | Close a decision, tally it, and record the Collective Will. | 17.4, 8.4, MVP-102 | Tested | 8.9, CL-046, CMP-006, G-054, G-059, INV-AT (24), INV-AT-13, MVP-102, MVP-108 | P-2 | G-041 auth; B-1 tenancy; B-2 quotas; G-042 threat model |
| `evidence.record` | Record evidence with its epistemic class. | 20.1 | Tested | G-054 | P-2 | G-041 auth; B-1 tenancy; B-2 quotas; G-042 threat model |
| `constraints.attach-evidence` | Use evidence as the basis of a constraint. Uncertain evidence needs a decision… | 20.1 | Tested | G-054 | P-2 | G-041 auth; B-1 tenancy; B-2 quotas; G-042 threat model |
| `optimization-runs.request` | Ask the solver for an allocation under the approved model. | 8.6, 13.1, MVP-103 | Tested | 13.1, MVP-103 | P-2 | G-041 auth; B-1 tenancy; B-2 quotas; G-042 threat model |
| `baselines.create` | Freeze an approved, commit-eligible result as the baseline. | 8.5 | Tested | G-054, GOV-AUTHPATH-001, INV-AT-08 | P-2 | G-041 auth; B-1 tenancy; B-2 quotas; G-042 threat model |
| `commitments.reserve` | Reserve resources for the baseline, without double-allocating. | 8.7, 19.5, MVP-104 | Tested | 8.1, MVP-104, MVP-111 | P-2 | G-041 auth; B-1 tenancy; B-2 quotas; G-042 threat model |
| `actuals.post` | Post what actually happened. Never alters the baseline. | 8.8, MVP-105 | Tested | MVP-105 | P-2 | G-041 auth; B-1 tenancy; B-2 quotas; G-042 threat model |
| `rebalances.propose` | Propose a routine reallocation. Inside the envelope it is resolved; otherwise i… | 5.9, 8.7, 5.11, MVP-106, MVP-107 | Tested | 5.9, G-059, MVP-106, MVP-107, UIX-NEUTRAL-004 | P-2 | G-041 auth; B-1 tenancy; B-2 quotas; G-042 threat model |
| `exceptions.resolve` | Resolve an Exception Proposition by the authority it names. | 5.11, 8.9, MVP-108 | Tested | G-059, MVP-108 | P-2 | G-041 auth; B-1 tenancy; B-2 quotas; G-042 threat model |
| `change-requests.put-in-force` | Put an approved change in force, once, exactly as approved (the decision names… | 8.9; CL-046 | Tested | CL-046, INV-AT (24) | P-2 | G-041 auth; B-1 tenancy; B-2 quotas; G-042 threat model |
| `exports.create` | Export everything needed to continue governance elsewhere. | 23.3, ASR-11, MVP-110 | Tested | MVP-110 | P-2 | G-041 auth; B-1 tenancy; B-2 quotas; G-042 threat model |
| `retention-schedules.adopt` | Adopt a records retention period for a record class. | 43.2 ASR-05 | Tested | CMP-005 | Eval | G-041 auth; B-1 tenancy; B-2 quotas; G-042 threat model |
| `records.delete` | Delete a record. Allowed only by schedule or legal order, and recorded. | 43.2 ASR-05, CMP-005 | Tested | CMP-005 | Eval | G-041 auth; B-1 tenancy; B-2 quotas; G-042 threat model |
| `configuration.set` | Change a deployment setting. Settings cannot disable Assurance Controls. | 43.2, 14.0 | Tested | CMP-001, UIX-NEUTRAL-003 | Off | none claimed |
| `GET /v0/queries/civic-bodies/{id}` | Civic body, its members, decision classes, and adopted packs. | 7 | Tested | CL-046, MVP-100 | P-1 | Public read-only deployment (B-5) |
| `GET /v0/queries/propositions/{id}` | Every version of a proposition, deliberation record, and votes. | 8.3, 8.4, MVP-101 | Tested | MVP-101 | P-1 | Public read-only deployment (B-5) |
| `GET /v0/queries/decisions/{id}` | A decision with its four status axes. | 8.0 | Tested | CMP-006 | P-1 | Public read-only deployment (B-5) |
| `GET /v0/queries/decisions/{id}/provenance` | Decision Provenance Packet. | 9 | Tested | CMP-004 | P-1 | Public read-only deployment (B-5) |
| `GET /v0/queries/decisions/{id}/replay` | Replay the decision's optimization from its bound versions and compare hashes. | 9.1, MVP-109 | Tested | MVP-109 | P-1 | Public read-only deployment (B-5) |
| `GET /v0/queries/baselines/{id}` | A baseline version and its lineage. | 8.5 | Tested | MVP-105, MVP-108 | P-1 | Public read-only deployment (B-5) |
| `GET /v0/queries/portfolio/{civic_body_id}` | Portfolio nodes, budgets, commitments, actuals, and variance. | 5.2, 8.8 | Implemented | not exercised | P-1 | Public read-only deployment (B-5) |
| `GET /v0/queries/exceptions/{id}` | An Exception Proposition: the conflict and the authority required. | 5.11 | Implemented | not exercised | P-1 | Public read-only deployment (B-5) |
| `GET /v0/queries/delegations/{civic_body_id}` | Delegation chains with concentration disclosure. | 17.3; CL-029 | Tested | 17.3 | P-1 | Public read-only deployment (B-5) |
| `GET /v0/queries/feed/{actor_id}` | A member's feed. Every item states why it is shown; order is deterministic. | 11.6.6, UIX-NEUTRAL-003 | Tested | UIX-NEUTRAL-003 | P-2 | G-041 auth; B-1 tenancy; B-2 quotas; G-042 threat model |
| `GET /v0/queries/events` | The hash-chained event log (supports ?after=seq). | 11.3, ASR-04 | Tested | CMP-005 | P-1 | Public read-only deployment (B-5) |
| `GET /v0/queries/exports/{id}` | A completed export package. | ASR-11 | Tested | MVP-110 | P-1 | Public read-only deployment (B-5) |

## Acceptance coverage

Dated technical coverage snapshot; not a claim that every requirement has been implemented.

| Family | In scope | Covered |
|---|---:|---:|
| MVP-100..114 | 15 | 11 |
| INV-AT (Build invariants) | 16 | 4 (04, 08, 17, 26) |
| CMP-001..009, 012..016 | 14 | 8 (001–007, 012) |
| CONT-AT-01..09 | 9 | 0 |
| UIX-NEUTRAL-001..004 | 4 | 4 |
| JNY-GRAD, CIT, MGR, FAC (30.5, 30.7–30.9) | 30 | 0 |
| Total | 88 | 27 |

## Remaining implementation limits

| Gap | Technical requirement | State |
|---|---|---|
| G-001 | Jurisdiction, Portfolio Node, Objective, Constraint, Resource and Relationship are first-class objects, each with its own identity, versions and lineage (7, 7.1) | Partial |
| G-002 | Funding Instrument, Appropriation type only in Phase 1 (5.13) | Missing |
| G-003 | Schedule/Milestone (18) and Risk (21) objects | Missing |
| G-004 | Actor/Role/Agent is a versioned object carrying `accountability_path` and `approval_track_record` at GML-1+ (12.0.1) | Partial |
| G-005 | Maturity Framework: reference GML-0 and GML-1 controls and the transition rules (4.2, CL-059) | Partial |
| G-006 | Treaty, Floor Revision Proposal, the Part V objects, Control Mapping and Engagement Record are interface only (13.6) | Interface only |
| G-007 | Proposition states per 8.3, including the clerk's validate, *Returned for correction* (CL-063), schedule-deliberation and publish-provenance actions | Partial |
| G-008 | Execution states Issued and Acknowledged, interface only at the external-system boundary (8.8, 19.6) | Interface only |
| G-009 | Assurance-sensitive results: margin compared with the at-risk count (23.1.1; replaces the CL-047 confidence minimum) | Partial |
| G-010 | One hash chain per Civic Body (CL-068, ASR-04) | Partial |
| G-011 | Version binding includes the Compliance Pack composition hash (CMP-015, CMP-016) | Partial |
| G-012 | Delegation rules (CL-064): concentration flag at max(5%, 2 members); lapse with reminder; mid-vote change rule; recusal passes through | Partial |
| G-013 | `secret_ballot` per decision class (CL-069, ASR-07) | Missing |
| G-014 | Constituency tags (CL-058), materiality threshold (CL-051), cumulative Exception Proposition reviewed at every GML level (CL-070) | Missing |
| G-015 | Amend a Governance Process under the ratchet (invariant 21) | Missing |
| G-016 | Revoke a credential; revoke or recall an authority; monitoring roles record rotation *and* recall terms (CL-066) | Partial |
| G-017 | Envelope per-period tolerance (default 3 × T in any rolling 30 days), risk limit, separation of duties (CL-059, CL-060) | Partial |
| G-018 | GML-1 second approver (CL-052); local administrator scope (CL-053) | Missing |
| G-019 | No sanction may reduce participation access (invariant 18) | Missing |
| G-020 | Pilot electorate (CL-065): residents' first cycle advisory, second binding or with an assurance of recognition; capacity for 2,000 registered / 200 active residents | Missing |
| G-021 | ACECOG Identity, Assurance Anchors as keyed hashes (key held by the body), four tiers, vouching limits (5 per 12 months, ring check), Reconciliation with merge and recount, identity commands; credentials link to an identity | Missing |
| G-023 | Continuity Offices and Cases: state machine, authority graph, warrant, sunset, safeguards. Founding goes through an External Convener case, replacing the fixed founding-charter authorities (CL-044) | Missing |
| G-024 | Pack composition from versioned modules by layer; stricter rule wins; conflicts flagged to counsel; composition hash; a mid-cycle edition does not apply to a transaction in progress (43.4) | Partial |
| G-025 | Colorado module rules encoded and confirmed (43.4.2) | Missing |
| G-026 | Retention default is permanent; destruction leaves a sealed placeholder (CL-054) | Partial |
| G-027 | A Legal Effect Declaration is adopted only by a recorded decision, with a counsel opinion reference and an effective date (CL-067) | Partial |
| G-028 | ASR-02 operator access logged and visible to the tenant (CMP-008); ASR-09 incidents recorded as events | Missing |
| G-029 | ASR-03 encryption at rest with key custody declared; ASR-07 credentials stored apart from participation records | Missing |
| G-030 | ASR-10 supply chain: SBOM, dependency scanning, signed releases | Partial |
| G-031 | ASR-06 accessibility, WCAG 2.2 AA, across all three clients | Missing |
| G-033 | Replay tolerance: objective within 1e-6 relative, allocations within $0.01 (CL-061) | Partial |
| G-034 | A solution may not raise the score by pushing a protected floor below its minimum; an unavoidable shortfall is recorded as a breach (invariant 9) | Missing |
| G-035 | Critical path, early and late dates, float, and leveling against one capacity constraint (18) | Missing |
| G-036 | Variance classified as Within Tolerance, Delegated Rebalance or Exception (8.8) | Partial |
| G-037 | Ecosystem Endowment Simulator v0.1, standalone (42, CL-072) | Missing |
| G-038 | Second-jurisdiction test fixture for the federation invariants (13.1; federation itself is interface only) | Missing |
| G-039 | Conversational drafting: the draft matches the desktop form field for field, every AI-introduced change is flagged, and a side-by-side view is available (CL-056) | Missing |
| G-040 | AI-generated or translated text is labeled (AI-LABEL-001) | Missing |
| G-041 | Caller authentication and authorization; MFA for authority holders; passkeys (ASR-01) | Missing |
| G-042 | Threat model, API and data layers | Missing |
| G-044 | Desktop structured surface; Facilitator/Clerk (30.9) and City Manager (30.8) journeys | Missing |
| G-045 | Resident tier of the mobile PWA (11.6.5, CL-049) | Missing |
| G-046 | Guest Proposer submission with a read-only fit-check preview (30.5) | Missing |
| G-047 | Escalate command (30.8) | Missing |
| G-048 | Notification engine, push for relevant deadlines (11.2, CL-059) | Partial |
| G-049 | Every stored object version conforms to its schema (15) | Partial |
| G-052 | Local-first packaging: installer, backup, restore, exit drill (11.5) | Missing |
| G-053 | The 61 Phase 1 acceptance tests not yet fully automated (section 3, including the two R-45 checks in G-062) run in CI (the capacity test and federation fixture are sized separately in G-020 and G-038) | Missing |
| G-056 | A recused member's vote doesn't count through a delegate (R-35) | Missing |
| G-057 | Envelope tests use confidence and reversibility from evidence and model records, require authority to propose, and select envelopes by affected scope (R-36) | Partial |
| G-058 | Commitment state machine per 8.7: Pending, Reserved/Committed, Released, Fulfilled, with compensating transactions (R-41) | Partial |
| G-060 | A record's age and class for deletion come from the record, not the caller (R-44) | Partial |
| G-061 | Refusals cite the right rule ID; QP runs report shadow prices as "not computed" rather than zero (R-46) | Partial |
| G-062 | MVP-105 and INV-AT-13 exercise the real code path, so each check can fail (R-45) | Partial |
