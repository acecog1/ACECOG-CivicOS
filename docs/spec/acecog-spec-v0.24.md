Integrated Basis of Design & Functional Specification

*Version 0.24 — Civic Design / Build / Operate Architecture (Post-Gate 2 update, 10 November 2026: approvals bind their subject and no actor grants itself authority, CL-079; exception resolutions re-checked and relaxations recorded, CL-080; public demonstration deployment, CL-081; editions and deployments, new 43.6.1, CL-082)*

*Version 0.23 — Civic Design / Build / Operate Architecture (Gate 1 requirements baseline, 10 November 2026: applies the Gate 1 dispositions of the v0.22 review, CL-055 to CL-076; the Markdown in the project repository is now the master, and Word or PDF copies are generated from it (decisions 0006 and 0007); CL-078)*

*Version 0.22 — Civic Design / Build / Operate Architecture (Developer contract v0.1 and mock API, Appendix M; Pilot Program Plan, 13.7, with the pilot WBS crosswalk, Appendix N; delegation concentration disclosure and reconfirmation; Civic Body capitalized as an object name; revised 9 November 2026: identity onboarding and uniqueness assurance, modular Compliance Packs with a Colorado module, civic authority continuity, and owner decisions CL-045, CL-046, CL-049, CL-030, CL-051 to CL-054; Gate 1 baseline, 9 November 2026: review dispositions CL-055 to CL-077)*

*Version 0.21 — Civic Design / Build / Operate Architecture (Build-readiness patch: Phase 1 execution filter, Phase 1 solver profile, local-first definition reconciled with shared hosting and mobile clients, version-binding rule, Delegation Envelope parameters, and Part III marked catalog reserve with no build phase; Appendix L)*

*Version 0.20 — Civic Design / Build / Operate Architecture (Architecture freeze candidate: Invariant Floor normalized to 26 invariants with IDs, seven protection layers and module floors, four-axis decision status model, conditional model language, an acceptance test for every invariant, red-team corrections including Guardian Council accountability, source-checked figures, and Appendix K with the invariant concordance and freeze summary)*

*Version 0.19 — Civic Design / Build / Operate Architecture (Adds Part VI — Compliance & Assurance (Section 43) as the umbrella compliance module: mandatory Assurance Controls, an operator certification roadmap and shared-responsibility matrix, Jurisdiction Compliance Packs with a California reference pack, AI governance alignment, and operator-conduct rules; adds invariants 66–70 and strengthens invariant 38; raises the accessibility floor to WCAG 2.2 AA; adds Appendix I (compliance evidence: ISO crosswalk and proposed standard group) and Appendix J; confirms Part V open decisions on residency, draw band, and guardian veto scope; corrects v0.18 cross-references)*

*Version 0.18 — Civic Design / Build / Operate Architecture (Adds Part V — Prosperity, Commons & Guardian Modules (Sections 31–42): Prosperity Transition, Shared Risk and Benefit Governance, Civic Assurance and Buffering, the Prosperity Floor, the Commons Endowment (sovereign fund), Guardian ("Lorax") Jurisdictions with their own governance floor, Indigenous Alignment, collective funding rules, Funding Instrument extensions, Lifecycle Management, and an Ecosystem Endowment stochastic simulator; adds invariants 52–65 and Appendix H)*

*Version 0.17 — Civic Design / Build / Operate Architecture (Specifies the five remaining Journey Catalog entries — Facilitator/Clerk (30.9), Auditor (30.10), Federation Partner (30.11), Fund Manager (30.12), Program Manager (30.13) — closing the Deferred Journeys reserve; adds Appendix G, a structural-register note on the project’s philosophical lineage that treats its early catastrophist material as genesis context rather than an operating premise)*

*Version 0.16 — Civic Design / Build / Operate Architecture (Adds Section 22.5 Multi-Tenant Hosting and Trust Tiers: shared multi-tenant vs. self-hosted sovereign hosting models, three federation trust tiers for partners who cannot be live API peers — including defense/national-security installations — and a new invariant scoping a shared-hosting platform operator’s authority (TRU-TENANT-001); adds Section 28.1 Domain Portability, stating precisely what makes the core architecture domain-agnostic and where that claim currently runs out)*

*Version 0.15 — Civic Design / Build / Operate Architecture (Adds two Journey Catalog entries: The Concerned Citizen / Voter (30.7), the mass-participation reference case for the Section 11.6.5 mobile tier and feed-neutrality requirement, and The City Manager (30.8), a delegated jurisdiction executive exercising exception handling, escalation, and accountability to the elected Governance Process)*

*Version 0.14 — Civic Design / Build / Operate Architecture (Adds Section 11.6 Interaction Architecture: desktop, conversational, and mobile as three clients of one authority-gated API, command/query separation, a two-tier mobile surface for mass uptake and active roles, and a feed/notification-neutrality requirement)*

*Version 0.13 — Civic Design / Build / Operate Architecture (Adds The Agency Planning Manager journey (30.6): regional, read-only portfolio roll-up, objective-contribution and marginal analysis, and coordination-by-proposition across federated jurisdictions, tracing directly to the project’s original 2019 discovery-phase persona)*

*Version 0.12 — Civic Design / Build / Operate Architecture (Adds Part IV: Roles & User Journeys, beginning with The Aspiring Grad Student individual-proposer journey, and traceability prefix JNY)*

*Version 0.11 — Civic Design / Build / Operate Architecture (Adds the ACECOG Standards Process for amending the invariant floor itself, modeled on civil-engineering design-code precedent, plus the civic-body-level amendment ratchet)*

*Version 0.10 — Civic Design / Build / Operate Architecture (Adds Ashby’s Law variety-amplification and principal-agent track-record invariants)*

*Version 0.9 — Civic Design / Build / Operate Architecture (Adds self-defined Maturity Frameworks alongside the ACECOG Reference Framework, resolving Ostrom’s self-organization principle at GML-1)*

*Version 0.8 — Civic Design / Build / Operate Architecture (Adds accountable-monitoring and graduated-sanction invariants from an Ostrom commons-governance benchmark at GML-1, plus prior stress-test invariants)*

*Version 0.7 — Civic Design / Build / Operate Architecture (Adds four stress-tested invariants for eligibility, cross-jurisdiction rights, AI drafting neutrality, and cumulative distributional effect; integrates the Civilizational Maturity & Type-I Transition module as Part III)*

A public/civic operating platform for scalable direct democracy, quantitative interoperability, portfolio optimization, execution management, provenance, and adaptive self-governance.

> Markdown conversion of `ACECOG_v0.22.docx` (revised 9 November 2026) for line-by-line review. The Word file is the circulated version; the table of contents is omitted here (use your viewer's outline).

# 0. Executive Design Intent

ACECOG is a public/civic design-build-operate platform for scalable direct democracy. It is conceived as a system of systems through which a population can express collective will, translate that will into objectives and constraints, allocate resources, coordinate execution, observe outcomes, and continuously govern the resulting system.

ACECOG is built from the ground up as civic infrastructure. Mature ERP, EPM, PPM, project-controls, financial-management, asset-management, workflow, and public-sector systems are treated as design precedent and interoperability targets—not as the architectural center of ACECOG.

*People → Will → Objectives → Portfolio → Resources → Execution → Actuals → Learning → People*

The democratic process governs values, boundaries, priorities, authority, and exceptions. Quantitative engines govern bounded allocation, scheduling, risk, and routine coordination within those democratically authorized limits. The result is intended to make direct democracy scalable: governance concentrates on consequential value choices while computation handles rote coordination that has already been authorized.

- Public/civic by design: inspectable, portable, forkable, auditable, and independently operable.

- Local sovereignty with federated interoperability: jurisdictions retain authority while sharing quantitative interfaces where they choose.

- Human accountability: automation delegates execution, not responsibility.

- Explainability and replay: every material decision can be reconstructed from the state, rules, evidence, model, authority, and approvals in force at the time.

- Ecological and intergenerational considerations are first-class portfolio variables and constraints rather than externalities.

- Exit is a governance right: a Civic Body must be able to export its governing state, records, models, and operational data in durable open forms.

# 1. Basis of Design

## 1.1 System Purpose

ACECOG shall serve self-governance objectives and processes through integrable technologies, datasets, decision methods, and operating workflows inherent to myriad jurisdictions. It shall provide a common civic operating architecture without requiring uniform political institutions, legal systems, cultures, or technology stacks.

Primary touchpoints include:

- collaborative opportunities among otherwise independent jurisdictions or Civic Bodies;

- common or overlapping objectives;

- similar ecological, geographic, economic, or socio-technical systems;

- shared resources and externalities;

- treaties, compacts, agreements, and other explicit authority interfaces;

- major social maturation events, crises, institutional transitions, and technological discontinuities.

## 1.2 Design / Build / Operate / Learn

| Domain         | Civic question                                       | Core functions                                                                                                                                                             |
|----------------|------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DESIGN         | How shall we govern ourselves, and what do we value? | Civic identity; values; rights; objectives; rules; institutions; jurisdictions; treaties; decision processes; authority; delegation; optimization criteria; risk appetite. |
| BUILD          | How do we turn public will into capability?          | Portfolios; programs; projects; funding; procurement; workforce; infrastructure; schedules; contracts; capital delivery; interjurisdictional collaboration.                |
| OPERATE        | How do we run the civic system?                      | Services; transactions; assets; operations; maintenance; staffing; resource flows; incidents; financial actuals; operational performance.                                  |
| LEARN / GOVERN | What happened, why, and what should change?          | Actuals; outcomes; variance; causal analysis; model calibration; institutional learning; proposed governance change; democratic reconsideration.                           |

These domains form a continuous control loop rather than a linear lifecycle.

## 1.3 Non-Negotiable Design Principles

1.  Human stakeholders remain authoritative over values, rights, public objectives, non-delegable powers, and material unresolved value conflicts.

2.  No state-changing action occurs without an explicit authority path.

3.  Explainability and provenance take precedence over opaque optimization.

4.  Local-first and jurisdiction-aware operation is the default; federation is opt-in and bounded by explicit agreements.

5.  No hard legal, treaty, rights-based, ecological, safety, or other non-compensable constraint may be silently traded away.

6.  Baselines, forecasts, actuals, evidence, and historical decisions remain separately reconstructible.

7.  AI is an interpretive, analytical, process-management, and documentation layer; capability does not create authority.

8.  The platform shall prefer open standards and public inspectability over vendor lock-in.

9.  A jurisdiction or Civic Body shall be able to exit, fork, migrate, or independently operate its civic state.

10. Governance itself may improve through observed outcomes, but changes to governance are proposed and authorized rather than silently learned into force.

## 1.4 System-of-Systems Posture

ACECOG exists between and within self-governing systems, not above them. Independent systems may remain sovereign while sharing compatible descriptions of objectives, constraints, resources, relationships, evidence, and decisions. Interoperability therefore occurs at semantic, quantitative, procedural, and technical layers.

# 2. ACECOG Civic Operating System

| Plane                         | Purpose                                                                 | Representative capabilities                                                                                                                                |
|-------------------------------|-------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Governance Plane              | Translate people and Civic Bodies into legitimate collective direction. | Civic identity; participation; expression; deliberation; collective will; rights; authority; decisions; delegation; minority positions.                    |
| Planning & Optimization Plane | Translate approved direction into feasible portfolios and allocations.  | Objectives; constraints; scenarios; portfolios; resources; PPM; LP/QP/MILP; risk; sensitivity; marginal allocation.                                        |
| Execution Plane               | Turn approved portfolios into coordinated work and services.            | Programs; projects; work packages; CPM; resource leveling; funding; procurement; assets; operations; commitments.                                          |
| Evidence Plane                | Maintain a trustworthy model of what is happening.                      | Financial actuals; operational actuals; sensors; ecological/social indicators; observations; provenance; confidence.                                       |
| Learning Plane                | Compare intent with outcomes and improve decisions and models.          | Variance; benefits realization; causal analysis; risk updates; model calibration; proposed rule/criteria changes.                                          |
| Federation Plane              | Coordinate independent jurisdictions without centralizing sovereignty.  | Treaties; shared portfolios; shared resources; cross-PPM coupling; consented synchronization; dispute/escalation.                                          |
| Civic Trust Plane             | Protect legitimacy across every plane.                                  | Identity; authority; privacy; security; provenance; audit; versioning; replay; portability; signing; open formats; compliance and assurance controls (43). |

## 2.1 Scalable Direct Democracy

ACECOG shall not equate direct democracy with universal manual voting on every operational transaction. Participation shall be capable of moving along a governed spectrum from direct participation, to domain-specific delegation, to bounded automated execution.

*Direct Participation ↔ Delegated Participation ↔ Automated Execution*

Citizens and Civic Bodies should spend governance attention on values, objectives, rights, boundaries, material tradeoffs, and exceptions. Routine allocation and coordination decisions may be executed computationally where the governing body has already authorized the objective function, constraints, tolerances, risk limits, and delegation scope.

## 2.2 Civic Body and Collective Will

The full ACECOG domain begins above the optimization engine. A Civic Body represents a self-identifying body of people capable of self-governance. Through a Governance Process, individual and group Expressions become deliberated propositions and, when legitimately adopted, Collective Will.

*Civic Body → Expression → Deliberation → Collective Will → Objective / Constraint / Authority*

The detailed democratic aggregation mechanisms—voting, consent, sortition, liquid delegation, participatory budgeting, constitutional amendment, or other methods—remain configurable by jurisdiction and are a future specification domain. The optimization engine consumes the resulting approved parameters; it does not invent them.

# 3. Enterprise and Public-Sector Design Precedent

ACECOG shall reuse the conceptual maturity of best-in-class enterprise and public-sector systems while remaining an independent civic platform. Familiar administrative terms should be used where they accurately describe the civic object; ACECOG-specific terms should be introduced only where conventional systems do not adequately represent democratic legitimacy, cross-jurisdiction authority, quantitative coupling, delegation, or decision provenance.

| Established concept                                     | ACECOG treatment                        | ACECOG extension                                                                            |
|---------------------------------------------------------|-----------------------------------------|---------------------------------------------------------------------------------------------|
| Fund / appropriation / grant                            | Retain familiar financial semantics.    | Bind restrictions and provenance through portfolio and jurisdictional optimization.         |
| Portfolio / program / project / work package / activity | Retain familiar PPM hierarchy.          | Couple nodes across trees and jurisdictions through quantitative relationships.             |
| Budget / forecast / actual                              | Retain separate states.                 | Tie every change to governance authority and replayable decision context.                   |
| Resource / capacity / asset / labor pool                | Retain operational semantics.           | Optimize across public objectives, ecological limits, and shared jurisdictions.             |
| KPI / strategic objective                               | Retain performance semantics.           | Derive from democratically approved values and public-will processes.                       |
| Approval workflow                                       | Retain role/gate concepts.              | Add explicit authority provenance and delegation envelopes.                                 |
| Audit trail                                             | Retain event-history concept.           | Expand into Decision Provenance Packets with model and solver replay.                       |
| Exception / escalation                                  | Retain operational concept.             | Generate structured Exception Propositions that identify the governing conflict.            |
| Business rule                                           | Retain machine-executable rule concept. | Distinguish empirical, policy, legal, treaty, rights, ecological, and preference authority. |

# 4. Value-Codified Governance and Adaptive Decision Support

*Values → Objectives → Optimization Criteria → Decision Principles → Governance Rules → Portfolio Decisions → Outcomes → Feedback*

Human stakeholders define what the Civic Body values, how competing objectives should be balanced, which decisions may be delegated, and where human judgment must remain authoritative. ACECOG applies those principles consistently across planning, funding, execution, monitoring, and benefits realization.

- Representative values may include public benefit, ecological resilience, affordability, equity, safety, regulatory compliance, carbon reduction, economic development, schedule urgency, financial sustainability, workforce impact, technical feasibility, reversibility, and intergenerational value.

- Criteria may be objectives to maximize/minimize, hard or soft constraints, thresholds, modifiers, eligibility rules, or escalation conditions.

- Material value conflicts shall be exposed rather than hidden in an aggregate score.

- Machine learning may improve routine support only after sufficient data quality, consistency, provenance, and governance maturity exist; it shall not independently redefine public values or approved decision principles.

## 4.1 Decision Delegation Continuum

| Level                            | Meaning                                                                                                         |
|----------------------------------|-----------------------------------------------------------------------------------------------------------------|
| 0 — Informational                | Assemble and present data without recommending action.                                                          |
| 1 — Analytical Support           | Identify patterns, conflicts, risks, tradeoffs, or comparable cases.                                            |
| 2 — Recommendation               | Evaluate alternatives and recommend one or more actions.                                                        |
| 3 — Conditional Delegation       | Execute a routine decision when predefined criteria, confidence thresholds, and delegation rules are satisfied. |
| 4 — Automated Routine Governance | Execute bounded, reversible, low-risk workflows with complete traceability and exception monitoring.            |

Unresolved value conflicts, material strategic consequences, significant uncertainty, legal or ethical implications, or conditions beyond delegated authority remain subject to human governance.

## 4.2 Governance Maturity Levels (GML)

The Decision Delegation Continuum (4.1) governs how much a given *decision* may be automated. Governance Maturity Level governs a separate question: how much institutional process and compliance rigor a given *Civic Body* is required to carry around every decision, regardless of delegation class. Compliance rigor should scale with demonstrated institutional discipline rather than being imposed uniformly on a three-member pilot council and a statutory public authority alike. Foundational invariants (Section 14) apply at every GML level without exception; GML only modulates the process wrapped around them. The Assurance Controls of Section 43.2 likewise apply at every level; GML scales the review and evidence wrapped around them, never whether they apply.

| Level                      | Environment                                                                        | Controls Added                                                                                                                                                |
|----------------------------|------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GML-0 Exploratory          | Pilot Civic Bodies, sandboxes; validating workflow clarity.                        | Single-approval commit; AI advisory only; baseline RBAC.                                                                                                      |
| GML-1 Structured           | After several clean baseline/rebaseline cycles; formal adoption by the Civic Body. | Dual approval; strict determinism required to commit; data classification; retention schedule formally adopted; novelty-based variety amplification (17.5.1). |
| GML-2 Civic Accountability | Public-facing, defensible governance; audit rehearsal completed.                   | Escalation chain with materiality thresholds; independent accessibility audit; audit-export bundle; legal hold support.                                       |
| GML-3 Institutional        | Statutory-grade public entity deployment.                                          | Multi-signature commit; independent schema- governance review; signed releases; supply- chain verification.                                                   |

A downgrade in GML requires a two-thirds supermajority of votes cast through the Governance Process, a logged justification, and stakeholder notification. An upgrade is decided through the Governance Process by ordinary majority once the entry criteria are met; for GML-1, at least two clean baseline-and-rebaseline cycles with no open audit finding. The level is a governed setting that no actor sets alone (CL-059). Records created under a higher GML level keep the controls that applied when they were created, even after a downgrade.

The levels above constitute the **ACECOG Reference Maturity Framework** — available to any Civic Body without further design work, and the default assumed elsewhere in this document wherever “GML” is referenced by name. It is one framework, not the only one; see 4.3.

**Reference defaults (CL-059).** The Reference Maturity Framework's default values, collected in one place. A Civic Body may tighten any of them through its Governance Process; loosening one is a weakening amendment under invariant 21 (GOV-RATCHET-001). Counsel confirms the voting defaults against applicable law (WBS 3.2.1).

| Setting | Reference default | Where used |
| --- | --- | --- |
| Quorum | 50% of eligible members | 17.5 |
| Approval, majority method | More than 50% of votes cast | 17.5 |
| Abstentions | Count toward quorum, not toward the tally | 17.5 |
| Tie | Fails; the status quo stands | 17.5 |
| Consent method | Passes unless a member lodges a reasoned objection within the window | 17.5 |
| Supermajority, where required | Two-thirds of votes cast | 4.2, 17.5 |
| Minimum notice before voting opens | 7 days | 17.5 |
| Voting window | 7 days | 17.5 |
| Who may close a vote | The clerk, and only after the window ends | 17.2, 17.5 |
| Materiality | 5% of the affected budget or any hard-limit breach, over a rolling 12 months | 5.11 |
| Envelope confidence threshold | 0.90 | 5.9 |
| Envelope minimum reversibility | 2 | 5.9 |
| Envelope aggregate tolerance | Three times the per-action tolerance in any rolling 30 days | 5.9 |
| Delegation concentration flag | Above the larger of 5% of eligible members or 2 members | 17.5 |
| Delegation reconfirmation | 12 months after the last reconfirmation, with a reminder 30 days before | 17.5 |
| Replay tolerance | Objective within one part in a million (relative); every allocation within 0.01 currency units | 9.1 |
| Identity, vouching, and verification window | As set in 23.1.1 | 23.1.1 |
| Continuity sunsets, triggers, and petition threshold | As set in 17.9 | 17.9 |

## 4.3 Self-Defined Maturity Frameworks

A system-imposed maturity ladder as the *only* option available to a Civic Body is in tension with the right of a community to devise its own institutions without an external authority overriding that right. ACECOG therefore treats **Maturity Framework** as a canonical, civic-body-authored object (7) in its own right, with the Reference Framework (4.2) as the default instance rather than a hardcoded requirement.

A Civic Body may adopt the Reference Framework unchanged, adopt it with local amendments, or author a fully custom Maturity Framework — any of which becomes binding only through the Civic Body’s own Governance Process (17.5), the same collective-choice mechanism that authorizes any other governance change. A Maturity Framework, once adopted, is amendable through that same process: maturity-level design is therefore tunable over time, not a one-time, one-way ratchet.

Two constraints bound this freedom, and neither is negotiable:

- No self-defined Maturity Framework may waive, relax, or omit a foundational invariant (Section 14) at any level it defines. Framework design authority extends to how much process wraps around a decision, never to whether the invariants apply.

- Every Maturity Framework — reference or self-defined — shall publish an interoperability declaration mapping its own levels to a common set of control categories: eligibility assurance (invariant 13), cross-jurisdiction rights protection (invariant 14), AI-drafting neutrality (invariant 15), cumulative-effect review (invariant 16), accountable monitoring (invariant 17), and graduated sanctions (invariant 18). This does not require identical mechanisms — only that a federation partner (22) can determine, from the declaration, whether a given level provides comparable coverage of each category, without adopting the same framework itself.

This preserves self-organization at the civic-body level while preserving Section 22’s need for a common trust vocabulary at the federation level: frameworks may differ; what they must cover cannot.

# 5. Optimization & Coordination Engine

## 5.1 Functional Purpose

The Optimization & Coordination Engine provides the common quantitative framework through which independently self-governing jurisdictions may describe, evaluate, coordinate, allocate, and execute portfolios of public interest.

Canonical proposition:

*Governance establishes the permissible solution space; optimization continuously operates within it.*

## 5.2 Hierarchical Portfolio Model

*Jurisdiction → Portfolio → Program → Project → Work Package → Task*

*Nᵢ = {Oᵢ, Cᵢ, Rᵢ, Kᵢ, Dᵢ, Aᵢ, Jᵢ, Tᵢ}*

- Oᵢ objectives; Cᵢ constraints; Rᵢ resources; Kᵢ performance criteria;

- Dᵢ dependencies/interactions; Aᵢ authority/delegation; Jᵢ jurisdiction; Tᵢ temporal characteristics.

## 5.3 Portfolio Polynomial Matrix (PPM)

The portfolio shall be representable as a connected mathematical system in which controllable variables describe allocations or operating levels and polynomial terms describe direct and interacting effects.

*x = \[x₁, x₂, …, xₙ\]ᵀ*

*F(x) = cᵀx − ½xᵀQx*

The Q matrix is the default pairwise interrelationship object. Terms may represent synergy, competition, dependency, substitution, conflict, shared-resource coupling, ecological coupling, financial coupling, temporal coupling, or cross-jurisdiction externality.

**Sign convention (CL-055).** F is maximized, and Q is symmetric. A positive diagonal term means diminishing returns; a positive off-diagonal term means two initiatives compete or substitute for each other. In Phase 1, Q must be positive semidefinite, so the problem is a convex quadratic program. Complementarity (two initiatives worth more together) cannot be expressed through Q in Phase 1: it is modelled as a linear bonus on a bundle node that represents doing both, and full synergy terms enter with MILP or non-convex methods in Phase 1.5 or later.

*F(x) = cᵀx − ½xᵀQx + Σ aᵢⱼₖ xᵢxⱼxₖ + …*

Higher-order terms are permitted where justified, but shall remain sparse, explicit, evidence-linked, versioned, and explainable. They are disabled in Phase 1 (13.1).

## 5.4 Constraint Architecture

*ℱ = {x : gᵢ(x) ≤ 0, hⱼ(x) = 0}*

- Every constraint preserves mathematical expression, authority, provenance, scope, precedence, lifecycle status, and relaxation policy.

- Constraint classes include rights/constitutional, statutory/regulatory, treaty/compact, ecological/physical, financial, resource/capacity, contractual, policy/procedural, risk, and preference.

- A lower authority may not silently relax a hard inherited constraint.

- Soft constraints must state their authorized penalty or tradeoff behavior.

## 5.5 Hierarchical and Cross-Tree Propagation

*K_parent = Φ(K₁, K₂, …, Kₙ)*

- Downward: parent limits or targets may govern descendants or allocate subordinate envelopes.

- Upward: child effects aggregate through declared functions such as sum, weighted mean, maximum, minimum, percentile, or worst-case.

- Cross-tree: nodes in different branches may be directly coupled through shared resources, dependencies, outcomes, or externalities.

## 5.6 Multi-Jurisdiction Composition

*x = \[xᴶ¹; xᴶ²; …; xᴶᵐ\]*

*Q = \[\[Q₁, Q₁₂\], \[Q₂₁, Q₂\]\]*

Local blocks retain jurisdictional ownership; cross-block terms represent shared interests, resources, obligations, or externalities. The jurisdictions need not share a political structure—only compatible representations of the relationships that cross their boundaries.

## 5.7 Objective Hierarchy

*O = {O_mandatory, O_threshold, O_priority, O_efficiency}*

1.  Preserve mandatory boundaries and non-compensable rights.

2.  Satisfy threshold objectives.

3.  Optimize democratically established priorities.

4.  Optimize efficiency among otherwise acceptable solutions.

## 5.8 Public Will as Model Configuration

*Governance → Parameters → Feasible Space → Optimization → Execution*

Governance establishes objectives, weights, priority ordering, thresholds, unacceptable outcomes, acceptable risk, delegation authority, and time horizon. These become version-controlled model parameters.

## 5.9 Delegated Decision Envelope

*E_d = {C, O, T, R, A}*

- C applicable constraints; O approved objectives; T tolerances; R risk limits; A authority.

- **T (tolerances):** an absolute amount, a percentage of the affected budget, or both, set per action and per period (rolling 30 days by default). The per-period aggregate counts every action resolved under the envelope; once it is reached, further actions escalate (CL-060).

- **R (risk limits):** the limits the action may not breach after resolution: hard constraints (5.2), protected floors (invariant 9 (OPT-NONCOMP-001)), and any envelope-specific caps, such as the largest share that may move out of one node.

- **Applicability:** every envelope whose scope covers any node or resource the action affects applies to it, whoever proposes the action.

- **Separation of duties:** the actor who proposes an action may not be the actor who resolves it under the envelope. Confidence and reversibility are derived from the evidence and model records the action depends on, never supplied by the proposer.

- A candidate action is eligible for autonomous resolution only when it remains inside the active envelope and satisfies confidence, reversibility, auditability, and separation-of-duties requirements.

<!-- -->

- **Confidence threshold:** a number from 0 to 1, set per decision class, giving the minimum calibrated confidence of the evidence or model output the action depends on (for example, forecast-interval coverage or solver feasibility margin). The default is 0.90. An action whose inputs carry no calibrated confidence fails closed and escalates.

- **Reversibility index:** an ordinal from 0 to 3. 0 is irreversible; 1 is reversible only at high cost; 2 is reversible within the next cycle at bounded cost; 3 is fully reversible without cost. Each envelope declares the minimum index for autonomous resolution; the default is 2.

- **Validation:** envelope parameters are typed and range-checked when the envelope is adopted. If a parameter is missing or out of range, autonomous resolution is disabled for that envelope and every candidate action escalates. Defaults are Reference Maturity Framework values (4.2); a Civic Body may tighten them through its Governance Process.

<!-- -->

- The most restrictive applicable envelope controls unless explicit precedence states otherwise.

## 5.10 Marginal Allocation and Context

*∇F(x) = c − Qx*

The value of another unit of money, capacity, schedule, or other resource may depend on the current portfolio state. ACECOG therefore evaluates marginal contribution in context rather than relying on static project rankings.

## 5.11 Exception Proposition

When the feasible space, risk envelope, authority, confidence, or approved values cannot support a delegated resolution, the engine shall generate an Exception Proposition rather than merely returning 'no solution'.

- violated or conflicting constraint/objective and originating authority;

- magnitude/materiality and affected jurisdictions/nodes/resources;

- feasible alternatives and tradeoffs;

- sensitivity and possible relaxation paths;

- authority and decision forum required to resolve the exception.

- Cumulative variant: the same structure shall also be generated when no single decision crosses the materiality threshold but a rolling window of decisions produces an equivalent cumulative effect on the same constituency (invariant 16 (GOV-CUMULATIVE-001)), drawing on the cumulative_impact_ledger referenced by affected Collective Will objects (17.4).

**Materiality.** A decision, or a rolling window of decisions, is material when it moves 5% or more of the affected budget (the budget of the Portfolio or Funding Instrument it draws on) or breaches any hard limit. The rolling window is the preceding 12 months. These are Reference Maturity Framework defaults; a Civic Body may set lower thresholds through its Governance Process, never higher ones (invariant 21 (GOV-RATCHET-001)). (CL-051) A constituency is a tag the Governance Process declares (for example a neighborhood, a program's beneficiaries, or a demographic group) and attaches to Portfolio Nodes and Propositions. The system tracks cumulative effect per declared tag; untagged effects are not tracked, so declaring constituencies is part of configuring a Civic Body (CL-058).

**Resolution is re-checked.** A decision that resolves an Exception Proposition is checked again before it changes the baseline: the reallocation must exist in its source, and the result must satisfy every hard limit and the budget (8.7). A decision that intends to relax a constraint must name the constraint and its new limit. The relaxation is recorded as a new version of the constraint, carrying the previous limit and the deciding decision (invariant 3). A resolution that would breach an unnamed limit is refused, and a closed exception can't be resolved again (CL-080).

### 5.11.1 Graduated Response Ladder

An Exception Proposition is the correct response to a materiality-level conflict; it is disproportionate as the *only* response to a first or minor rule deviation. A four-tier ladder applies below Exception Proposition, each tier cheaper than the next:

This ladder is the Reference Maturity Framework’s default practice (4.2). The Invariant Floor fixes only that responses affect governance privileges and never participation access or a module-floor entitlement (invariant 18, GOV-GRADUATED-001).

| Tier                            | Response                                                                   | Trigger                                                                                             |
|---------------------------------|----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| 0 — Notice                      | Informal, logged to the actor and their accountability_path (12.0.1) only. | First/minor deviation; no materiality threshold crossed (5.11).                                     |
| 1 — Warning                     | Logged and visible to the Civic Body; remediation requested.               | Repeat of a Tier-0 issue, or a somewhat larger deviation.                                           |
| 2 — Exception Proposition       | The existing mechanism above, routed to proper authority.                  | Materiality threshold crossed — single- decision or cumulative (invariant 16 (GOV-CUMULATIVE-001)). |
| 3 — GML downgrade consideration | The existing mechanism (4.2).                                              | Pattern of unresolved Tier-2 exceptions for the same actor/rule.                                    |

A breach whose materiality independently crosses the single-decision or cumulative threshold enters directly at Tier 2 — the ladder governs proportionate response to small first-instance deviations; it does not delay or soften the response to a genuine rights or cumulative-harm violation (invariants 9 (OPT-NONCOMP-001), 14 (FED-RIGHTS-001) and 16 (GOV-CUMULATIVE-001)). (GOV-GRADUATED-001)

## 5.12 Closed-Loop Control

*Will → Plan → Allocate → Execute → Measure → Compare → Correct*

*F(x) → F(x, t, s)*

Time t and observed system state s allow ACECOG to evolve from portfolio selection into dynamic civic portfolio control. Two correction loops operate at this layer: a plan-versus-actual loop (did the plan perform as intended) and, at every GML level (CL-070), a periodic cumulative-distribution review (who has borne the cumulative cost or benefit across the rolling window) feeding the Cumulative Exception Proposition above.

## 5.13 Funding Instruments and Capital Constraints

The Funding Instrument object (Section 7) is bound into the PPM as a governed capital resource with its own rules, cost, timing, and risk, rather than a single budget number. Three instrument types are defined; Phase 1 builds only the Appropriation, with its amount, fiscal year, source, and restrictions, and the other two are interface only until Phase 1.5 (CL-057): Appropriation (fixed amount, fiscal-year limited), Fixed-Rate Debt (principal, rate, amortization, covenant thresholds), and Restricted Grant (milestone-released, eligible-use tags, clawback flag). Equity/revenue-share instruments, variable-rate debt, blended capital stacks, and derivative-style structures are explicitly deferred past MVP.

Each instrument adds constraint terms to ℱ (5.4):

- Capital availability: *Capital_required(x, t) ≤ Funding_available(t)*

- Restricted use: allocation variables outside a grant’s eligible set are forced to zero

- Debt service: *Projected_cashflow(t) ≥ Debt_service(t) × DSCR_min*, else infeasible

Financing cost enters the objective as a modifier rather than a hidden side effect: *F’(x) = F(x) + Σ(allocated_capital_i × cost_of_capital_i)*. A funding-instrument milestone or tranche release may also appear as a dependency edge in the execution graph (Section 6), gating task start.

Governance coupling: only an authorized role may create or modify a funding instrument; a covenant breach automatically raises the required approval class; grant non-compliance blocks commitment outright rather than merely generating a warning.

Part V (Section 40) extends Funding Instrument with three further subtypes — Endowment (including the Ecosystem Endowment), Collective Enterprise and Public Finance Institution — each carrying its own governing rules (GOV-COMMONS-001 and ECO-COLLATERAL-001 for endowments). The three MVP types above are unchanged.

# 6. Execution, Scheduling, Capacity, and Risk

## 6.1 Dependency Graph and Scheduling

- Tasks form directed dependency graphs with explicit hard/soft dependency semantics.

- The execution engine supports Critical Path Method, slack/float, topological sorting, and dynamic path recomputation.

- Baseline, forecast, and actual schedule states remain distinct.

## 6.2 Resource and Capacity

- Capacity-constrained scheduling and resource leveling shall detect bottlenecks and infeasibility.

- Resources may be stocks, flows, capacities, entitlements, labor, assets, funds, or other governed quantities.

- Resource balances shall reconcile across reservations, commitments, consumption, production, transfer, and replenishment.

## 6.3 Stochastic Scenario and Risk Management

- Parametric uncertainty may use explicit distributions for cost, duration, availability, yield, demand, and other variables.

- Scenario, Monte Carlo, sensitivity, robust optimization, and tail-risk methods may be introduced according to phase and governance need.

- Stochastic runs shall preserve seeds, distributions, scenario sets, configuration, and environment metadata sufficient for replay.

- Risk limits may constrain Delegation Envelopes and trigger escalation.

## 6.4 Adaptive Rebalancing

1.  Freeze the prior committed state.

2.  Ingest delta conditions or observed variance.

3.  Re-run allocation/optimization under updated constraints.

4.  Re-run scheduling and capacity checks.

5.  Compare divergence from baseline/forecast.

6.  Generate a change-impact and governance-consequence report.

7.  Execute only within authorized rebalance tolerances; otherwise escalate.

# 7. Canonical Civic Domain Objects

Every first-class object shall carry stable identity, immutable version identity, lifecycle status, owner/steward, scope, effective window, provenance, authority basis, confidence where applicable, classifications, and supersession lineage.

| Object                             | Functional meaning                                                                                                                                                                                                              | Key relationships                                                                                                                                                                                              |
|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Civic Body                         | Self-identifying body of people capable of self-governance.                                                                                                                                                                     | Creates governance processes, expressions, collective will, jurisdictions, and authorities.                                                                                                                    |
| Governance Process                 | Authorized procedure for transforming propositions and participation into legitimate decisions.                                                                                                                                 | Consumes expressions; produces decisions, objectives, constraints, authorities.                                                                                                                                |
| Jurisdiction                       | Self-governing authority boundary.                                                                                                                                                                                              | Contains portfolios, rules, resources, authorities; participates in agreements.                                                                                                                                |
| Portfolio Node                     | Nested governed work/investment/service unit.                                                                                                                                                                                   | Parent-child hierarchy plus cross-tree relationships.                                                                                                                                                          |
| Objective                          | Approved outcome/value/optimization criterion.                                                                                                                                                                                  | Receives contributions; may conflict or reinforce other objectives.                                                                                                                                            |
| Constraint                         | Boundary on feasible action/state with authority and provenance.                                                                                                                                                                | Applies to nodes/resources/objectives/decisions; propagates or couples.                                                                                                                                        |
| Resource                           | Scarce or governed quantity.                                                                                                                                                                                                    | Allocated, reserved, consumed, produced, transferred, replenished.                                                                                                                                             |
| Relationship                       | Typed connection among objects.                                                                                                                                                                                                 | Populates dependencies, PPM coefficients, externalities, substitutions, synergies.                                                                                                                             |
| Authority                          | Lawful/organizational capacity to approve, prohibit, delegate, waive, commit, execute.                                                                                                                                          | Authorizes decisions and envelopes; may originate constraints.                                                                                                                                                 |
| Delegation Envelope                | Bounded decision space for a role or computational agent.                                                                                                                                                                       | Tests routine decisions; triggers escalation when exceeded.                                                                                                                                                    |
| Decision                           | Proposed or completed choice among alternatives.                                                                                                                                                                                | Consumes evidence/model/authority; may create commitments or changes.                                                                                                                                          |
| Treaty / Compact / Agreement       | Explicit interface among independent jurisdictions.                                                                                                                                                                             | Creates shared constraints, resources, authorities, and coupling terms.                                                                                                                                        |
| Evidence / Observation             | Information about state, performance, effects, or conditions.                                                                                                                                                                   | Supports constraints, relationships, risk, actuals, decisions.                                                                                                                                                 |
| Funding Instrument                 | Governed financial source and restrictions. MVP types (5.13): Appropriation, Fixed-Rate Debt, Restricted Grant; Part V subtypes (40): Endowment (incl. Ecosystem Endowment), Collective Enterprise, Public Finance Institution. | Funds nodes; creates financial resources and constraints.                                                                                                                                                      |
| Schedule / Milestone               | Temporal commitment/dependency/window.                                                                                                                                                                                          | Constrains nodes/resources and gates funding/authority.                                                                                                                                                        |
| Risk                               | Uncertainty about future condition or consequence.                                                                                                                                                                              | Constrains delegation and feeds simulation/sensitivity.                                                                                                                                                        |
| Exception Proposition              | Structured governance question generated by unresolved conflict or infeasibility.                                                                                                                                               | Routes a quantitative/governance conflict to the proper authority.                                                                                                                                             |
| Actor / Role / Agent               | Identity or function capable of acting in the system.                                                                                                                                                                           | Authority is separately granted and checked; authentication is not authority. Carries accountability_path (12.0.1) and approval_track_record (12.0.1) when exercising approval/monitoring authority at GML-1+. |
| Membership Credential              | Governed attestation that an Actor is a unique, eligible member of a Civic Body.                                                                                                                                                | Bounds participating population for Governance Process (17.5); revocable; carries attestation_confidence.                                                                                                      |
| Maturity Framework                 | Civic-body-authored or ACECOG reference (4.2) definition of graduated institutional rigor.                                                                                                                                      | Defines levels and their controls; adopted/amended via Governance Process (4.3); referenced by Federation Contract’s maturity framework mapping (22.2).                                                        |
| Floor Revision Proposal (FRP)      | Proposed change to the system-level invariant floor (Section 14).                                                                                                                                                               | Classified strengthening/weakening (14.1); weakening proposals require independent verification before ratification into a published edition.                                                                  |
| Ecosystem Entity                   | Rights-holding ecosystem (forest, watershed, basin) represented as a legal person (37).                                                                                                                                         | Governed by exactly one Guardian Jurisdiction per layer; nests by subsidiarity; holds a Natural Capital Account.                                                                                               |
| Guardian Jurisdiction              | Jurisdiction whose defining scope is fiduciary stewardship of an Ecosystem Entity (37).                                                                                                                                         | Has Guardian Council, Science and Monitoring Commission and Member Assembly; trustee of the Commons Endowment; adopts a Statement of Relationship.                                                             |
| Natural Capital Account            | Ledger of an ecosystem's stocks and flows, including non-market value (36.2).                                                                                                                                                   | Certified by the Science and Monitoring Commission; feeds capitalized-yield valuation; never spent directly.                                                                                                   |
| Statement of Relationship          | Guardian Council's statement of its spiritual and cultural relationship to the land (38).                                                                                                                                       | Authored with peoples holding ancestral ties; reviewed on the Lifecycle Management cycle.                                                                                                                      |
| Resource Commitment Registry Entry | Single registration of a committed resource (funds, crews, stocks, capacity) (41.2).                                                                                                                                            | Referenced by every module; prevents double-booking (RES-REGISTRY-001).                                                                                                                                        |
| Compliance Pack                    | Versioned bundle of jurisdiction-specific rule constraints, retention templates, disclosure hooks, and evidence templates (43.4).                                                                                               | Adopted by a Civic Body through its Governance Process; may only add constraints (invariant 19 (GOV-FRAMEWORK-001)).                                                                                           |
| Retention Schedule                 | Record-class retention periods and destruction authority for a Civic Body (43.2, ASR-05).                                                                                                                                       | Governs every deletion; a deletion outside it is refused and itself recorded.                                                                                                                                  |
| Legal Effect Declaration           | Statement of the legal status of a decision class and the authority that confers it (43.2, ASR-08).                                                                                                                             | Required before any result displays as binding (invariant 26 (ASR-STATUS-001)).                                                                                                                                |
| ACECOG Identity                    | One real person within a civic scope, with an assurance tier built from assurance anchors (23.1.1).                                                                                                                             | Issued same day at no cost; at most one per person in scope (invariants 13, 24).                                                                                                                               |
| Assurance Anchor                   | One piece of uniqueness evidence attached to an identity (23.1.1).                                                                                                                                                              | Stored only as a keyed hash; a matching hash opens a Reconciliation Case.                                                                                                                                      |
| Reconciliation Case                | A suspected duplicate identity under review (23.1.1).                                                                                                                                                                           | On merge, affected decisions are recounted; participation never suspended.                                                                                                                                     |
| Continuity Office                  | A Justice of the Peace, Elders Council, or External Convener configured by a Civic Body (17.9).                                                                                                                                 | Process powers only; never reconstitutes itself (invariant 17 (TRU-MONITOR-001)).                                                                                                                              |
| Continuity Case                    | A founding or restoration of an office, from detection to restoration (17.9).                                                                                                                                                   | Carries its warrant, authority basis, verifications, and sunset; replayable.                                                                                                                                   |
| Compliance Module                  | One versioned layer of a Compliance Pack composition (43.4).                                                                                                                                                                    | Only adds constraints; stricter rule wins; conflicts go to counsel (invariant 19).                                                                                                                             |
| Control Mapping                    | Link from an ASR or AI control to an external framework control and its evidence template (43.2, 43.5).                                                                                                                         | Supports operator certification (43.3) and the crosswalk in Appendix I.                                                                                                                                        |
| Engagement Record                  | Scope, fee basis, and staff of an operator, implementer, or auditor engagement with a Civic Body (43.6).                                                                                                                        | Visible in the body’s provenance; outcome-linked fees refused (OPS-NEUTRAL-001).                                                                                                                               |
| Interest Declaration               | A person’s declared interest in propositions before a Civic Body (43.4).                                                                                                                                                        | Blocks deliberation and voting on affected propositions; recusal recorded in provenance.                                                                                                                       |

## 7.1 Canonical Relationship Semantics

| Relationship                    | Meaning                                                 | Quantitative / governance effect             |
|---------------------------------|---------------------------------------------------------|----------------------------------------------|
| contains                        | Structural nesting.                                     | Defines roll-up and inherited scope.         |
| contributes_to                  | Outcome contribution.                                   | Populates value terms.                       |
| constrains                      | Limits feasible behavior.                               | Adds feasible-space condition.               |
| consumes / produces             | Resource demand/supply.                                 | Adds balance and capacity requirements.      |
| depends_on                      | Precondition or sequencing.                             | Adds logical/temporal coupling.              |
| synergizes_with / competes_with | Combined value interaction.                             | Positive/negative PPM interaction.           |
| substitutes_for                 | Alternative means.                                      | Permits governed substitution.               |
| externalizes_to                 | Cross-boundary consequence.                             | Adds cross-jurisdiction coupling.            |
| authorizes / delegates_to       | Permission and bounded transfer of execution authority. | Gates decision and execution.                |
| funds                           | Provides eligible financial capacity.                   | Adds restricted resource.                    |
| measures                        | Observed state/performance.                             | Updates actual/current state.                |
| supersedes                      | Prospective replacement.                                | Preserves historical reconstruction.         |
| conflicts_with                  | Cannot jointly satisfy under current state.             | May trigger exception.                       |
| governs_shared_interface        | Agreement creates interjurisdictional authority.        | Permits shared constraints and transactions. |

# 8. State Machines and Transaction Semantics

## 8.0 Decision Status Model

Every decision, commitment, and published result carries four status attributes, each on its own axis. No value on one axis implies a value on another; invariant 26 (ASR-STATUS-001) makes the separation binding.

**Legal status is fixed when a decision closes.** A Legal Effect Declaration applies only to decisions that close after its effective date; adopting one never changes the legal status of an earlier decision. (CL-045)

| Axis               | Values                                                                                                                        | Defined in                              | Question it answers                                   |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|-------------------------------------------------------|
| Lifecycle state    | Draft, Proposed, Validated, Deliberated, Approved, Baselined, Optimized, Resolved, Committed, Executing, Measured, Reconciled | 8.2–8.10                                | Where is this in the governance-to-execution process? |
| Legal status       | Advisory, Consultative, Binding (with effective date)                                                                         | 43.2 (ASR-08); Legal Effect Declaration | Does it have legal effect, and on what authority?     |
| Delivery readiness | Proposed, Funded but incomplete, Operationally verified, Breached                                                             | 34.2                                    | Can it actually be delivered?                         |
| Epistemic class    | Observed, Reported, Estimated, Assumed, Scenario output, Hypothesis                                                           | 20.1                                    | How certain is the information it rests on?           |

- **Approved** means a Governance Process decision (8.4). **Authorized** means an action cleared by the envelope test (8.7). Neither confers legal status.

- **Committed** means resources are reserved (19.5). It does not mean operationally verified (34) or legally binding.

- **Effective** is reserved for legal status. The terminal state of change control (8.9) is In Force.

- Every view that shows one attribute shows the others where they apply, so no screen implies a status a decision does not have.

## 8.1 Transaction Model

*Transaction = Intent + Prior State + Inputs + Rules + Authority + Result + Provenance*

- Every material state change is an explicit governed transaction.

- Transactions are logically atomic, version-aware, and auditable.

- Validation and authorization precede commitment.

- Recommendation, approval, commitment, execution, and actual outcome are distinct states.

- Rejected, failed, or materially attempted transactions remain auditable.

- Idempotent replay shall not create duplicate commitments, payments, allocations, approvals, or execution events.

## 8.2 Master Governance-to-Execution Lifecycle

*Draft → Proposed → Validated → Deliberated → Approved → Baselined → Optimized → Resolved → Committed → Executing → Measured → Reconciled*

At appropriate points the flow may branch to Rejected, Remanded, Deferred, Suspended, Superseded, Canceled, or Exception.

## 8.3 Proposal and Validation

1.  Draft working content.

2.  Submit a frozen candidate version with requested action.

3.  Screen identity, jurisdiction, completeness, duplication, evidence, and obvious authority defects.

4.  Validate schema, semantics, provenance, jurisdiction, authority, constraints, mathematics, feasibility, and workflow. A proposition that fails validation is set to Returned for correction by the clerk, with reasons, and may be resubmitted as a new version (CL-063).

5.  Route accepted propositions to the correct deliberative body or delegated workflow.

## 8.4 Deliberation and Approval

- The record preserves the exact proposition version considered.

- Material amendments create new versions and may trigger revalidation.

- Evidence, objections, minority positions, recusals, and conflicts remain attached.

- Approval identifies exact scope, conditions, the date it takes effect, and authority.

- Conditional approval creates machine-readable preconditions.

## 8.5 Baseline

- A baseline is an immutable approved reference state.

- Only an approved or validly delegated decision may create/revise a baseline.

- Revisions create new baseline versions; prior versions remain intact.

- The baseline references the objective, constraint, resource, schedule, funding, model, and authority versions in force when approved.

## 8.6 Optimization Run

*Requested → Snapshot Locked → Model Built → Feasibility Checked → Solved → Verified → Published*

Optimization results are evidence for decisions; they are not themselves approvals unless an active Delegation Envelope explicitly authorizes the decision class.

## 8.7 Delegated Resolution and Commitment

*Candidate Action → Envelope Test → Authorized Resolution \| Escalation*

*Resolved → Commitment Pending → Reserved/Committed → Released \| Fulfilled*

- Authority, feasibility, tolerances, risk, confidence, and permitted decision class are checked.

- Immediately before commitment, resource balances, funding eligibility, constraints, and authority are rechecked.

- Commitment changes governed availability and therefore remains distinct from recommendation and approval.

- Cancellation/decommitment creates an explicit compensating transaction.

## 8.8 Execution, Actuals, Variance, and Rebalance

*Committed → Issued → Acknowledged → In Progress → Completed \| Failed \| Canceled*

*Observed → Ingested → Validated → Posted as Actual → Reconciled*

*Actuals → Variance Detection → Classification → Within Tolerance \| Rebalance \| Exception*

- Observation time and ingestion time remain separate.

- Late or corrected actuals supersede without deleting history.

- Within-tolerance rebalances may execute under delegation.

- Constraint-threatening, constraint-violating, model-invalidating, or materially novel variance escalates.

## 8.9 Exception and Change Control

*Detected → Classified → Contained → Routed → Deliberated → Resolved → Closed*

*Change Request → Impact Analysis → Authority Classification → Approval/Delegation → New Version → In Force*

**Version binding.** Every transaction binds, when it starts, to the versions in force of the Governance Process, Maturity Framework, Delegation Envelope, objectives, constraints, and models it uses. A change that reaches In Force applies only to transactions that start after the recorded point at which it takes effect, never to one already in progress. Replay (Section 9) uses the bound versions.

**One approval, one change.** A change decision names the object it changes and a hash of the exact change. Putting a change in force is refused if the target or content differs from what was approved, or if the decision has already put its change in force. A change request passes every check that adopting the same object would. (CL-046)

Empirical recalibration and normative governance change are distinct change classes. Historical decisions remain reproducible under the versions that governed them at the time.

## 8.10 Cross-Jurisdiction Transactions

- Each participant contributes immutable local state and applicable shared-interface objects.

- The shared model is composed from local models plus agreement-authorized coupling terms.

- Local approval requirements remain local; shared approval requirements derive from the governing agreement.

- No federation transaction silently overwrites a jurisdiction's local object.

- Where atomic multi-party commitment is impossible, explicit pending and compensating semantics are required.

# 9. Decision Provenance, Memory, and Replay

ACECOG shall maintain an immutable, append-oriented memory sufficient to reconstruct why a decision occurred, what was known, what authority existed, what model ran, what alternatives were considered, what was approved, and what subsequently happened.

| Decision Provenance Packet element | Minimum content                                                                          |
|------------------------------------|------------------------------------------------------------------------------------------|
| Inputs                             | Evidence, data versions, timestamps, confidence, scenario state.                         |
| Governance                         | Values/objectives, weights, thresholds, constraints, authority, delegation.              |
| Model                              | Schema/model version, objective function, Q/relationship versions, solver configuration. |
| Run                                | Input hash, worker/solver version, seed where stochastic, result hash, warnings.         |
| Analysis                           | Feasibility, binding constraints, marginal effects, sensitivity, alternatives, risk.     |
| Deliberation                       | Participants, positions, minority views, recusals, amendments.                           |
| Disposition                        | Recommendation, approval/rejection, delegated resolution, commitment, execution.         |
| Outcome                            | Actuals, variance, corrective actions, benefits/outcome measures.                        |
| Lineage                            | Supersession, rebaseline, exception, change-control, and replay references.              |

## 9.1 Replay Modes

- Strict / Commit Lane: same immutable inputs, versions, configuration, and seed must reproduce the result within defined numerical tolerances: the objective value within one part in a million (relative) and every allocation within 0.01 currency units. Exact reproduction remains the target when solver versions are pinned (CL-061).

- Best-Effort / Exploration Lane: sufficient metadata is retained to understand and approximate a result, but it is not commit-eligible unless explicitly overridden by authorized governance.

- Historical replay loads historical model, rule, data, authority, and environment references rather than current ones.

# 10. Artificial Intelligence Strategy

AI exists to reduce cognitive friction, translate natural language into structured system inputs, explain model outputs, guide users through governance workflows, surface risks and tradeoffs, manage process, and maintain documentation. AI is not a source of civic authority.

## 10.1 Architectural Boundary

*User ↔ AI Interface ↔ Orchestrator / Governance Control Plane ↔ Core Engines ↔ Ledger / Storage*

- AI shall not write directly to committed storage or bypass the governed commit path.

- Natural-language transformations shall produce structured, reviewable payloads and diffs.

- AI may assemble provenance, draft records, summarize deliberation, map source text to candidate constraints, prepare solver inputs, explain outputs, and monitor workflow.

- AI may execute routine decisions only where an explicit active Delegation Envelope authorizes the class and all deterministic gates pass.

- AI may not create public values, invent legal authority, expand its own authority, silently relax hard constraints, conceal dissent, or retroactively alter records.

- Core governance operation shall not depend on a single proprietary AI model; AI providers/models should be replaceable components.

# 11. Functional System Architecture

## 11.1 Topology

*User Interfaces → Application / Orchestrator → Civic Engines → Solver & Simulation Workers → Persistence & Provenance*

No compute worker may directly mutate committed civic state. Workers are calculators; the governed application/orchestrator controls state transitions.

## 11.2 Core Engines

| Engine                    | Purpose                                                                                               |
|---------------------------|-------------------------------------------------------------------------------------------------------|
| Governance & Deliberation | Civic processes, propositions, participation, deliberation, approvals, authority, delegation.         |
| Sense / Evidence          | Normalize observations, indicators, external data, confidence, provenance, and time series.           |
| Portfolio / Model         | Maintain hierarchy, objectives, constraints, resources, relationships, PPM, and scenarios.            |
| Optimization              | LP/QP/MILP and later robust/stochastic methods; feasibility, sensitivity, marginal allocation.        |
| Execution & Resilience    | Dependencies, CPM, capacity, leveling, risk, shocks, adaptive rebalance.                              |
| Decision & Delegation     | Decision lifecycle, envelope testing, approval gates, commitments, exception routing.                 |
| Memory & Provenance       | Append-only event history, snapshots, Decision Provenance Packets, replay.                            |
| Federation                | Opt-in synchronization, cross-jurisdiction composition, treaty/compact interfaces, conflict handling. |
| AI Process Manager        | Natural-language interface, workflow guidance, explanation, documentation, bounded agent actions.     |

| Notification / Subscription | Watches and subscriptions; neutrally generated alerts across feed, push, and desktop (11.6.6, 11.6.7). |

## 11.3 Storage Model

- Append-only event log for meaningful state changes.

- Snapshot store for efficient current-state reconstruction.

- Artifact store for solver results, schedules, simulations, reports, and signed packets.

- Model/version registry for schemas, rules, solvers, AI models, and policy configurations.

- Local-first storage by default, with explicit federation adapters.

## 11.4 Job Contracts

Compute jobs shall use immutable request/response contracts with payload hashes, model/version references, determinism mode, seed where needed, result hashes, runtime metrics, warnings, environment fingerprints, and failure maps.

| Job                  | Purpose                                                                          |
|----------------------|----------------------------------------------------------------------------------|
| solve_ppm            | Optimize portfolio allocations under approved objectives and constraints.        |
| build_schedule       | Create CPM/capacity-aware execution schedule.                                    |
| validate_feasibility | Fast check of candidate plan executability.                                      |
| run_monte_carlo      | Quantify uncertainty and risk envelopes.                                         |
| inject_shock         | Apply event-driven disruption to a frozen state.                                 |
| rebalance_plan       | Recompute allocation/schedule under changed conditions while preserving lineage. |

## 11.5 Deployment and Packaging Strategy

Local-first sovereignty (1.3, 12) is a deployment constraint, not only a data-residency preference. A Civic Body’s authoritative record lives on an installation that the Civic Body controls, and that installation operates without an internet connection. This rules out silent auto-update, and any arrangement in which a third party’s server is authoritative without the Civic Body’s consent and a guaranteed exit. The reference packaging shape is a single installable bundle containing the UI layer, Orchestrator, storage (event log, snapshot store, artifact store), and worker processes. Desktop and mobile clients reach that installation over a local network or the internet; no peer-to-peer synchronization is required. Hosting on an operator’s shared platform (22.5.1) is an alternative that a Civic Body may choose, protected by invariants 12 (TRU-EXIT-001) and 23 (TRU-TENANT-001).

**Dedicated cloud tenancy (CL-074).** A cloud tenancy dedicated to one Civic Body counts as local-first when the Civic Body holds the encryption keys, controls administrative access, and has passed the exit drill: export, rehydrate, and replay with identical outcomes (invariant 12 (TRU-EXIT-001)).

Two worker-packaging strategies apply across phases:

- Bundled (MVP) — workers ship inside the application bundle; simplest to install and guaranteed version-compatible, at the cost of harder independent scaling of heavy compute.

- Sidecar (Phase 1.5+) — workers run as independently versioned local services (e.g. containerized), each carrying its own worker_build_id; enables per-worker rollback and clearer environment fingerprinting at the cost of more complex installation.

Every job result’s environment fingerprint (11.4) should include worker_build_id and solver-library version at minimum, so replay (Section 9) can distinguish a genuine input change from environment drift. Updates remain user-initiated and logged as governance events with a version delta and determinism-impact note (14) attached before the Civic Body approves the upgrade. Multi-user deployment may extend from a shared workstation to a LAN-hosted node to federated nodes (Phase 2) without changing this packaging model. Backup and portability use signed export/import bundles with integrity verification on import.

## 11.6 Interaction Architecture

Sections 11.1-11.5 specify engines, storage, and deployment. This subsection specifies how humans actually reach them: multiple client surfaces sharing one authority-gated API, so that a conversational interface, a mobile app, and a desktop dashboard are three ways of presenting the same governed actions rather than three different trust models.

### 11.6.1 One API, Three Clients

Every client — desktop web, conversational assistant, mobile — calls the same command/query API and is subject to the same checks (Section 14 invariants 2 (GOV-AUTHPATH-001), 6 (FED-AUTH-001) and 7 (GOV-ENVELOPE-001)). No client has a shortcut to committed state. This is the AI-to-Commit boundary already specified in Section 24.3 (AI-COMMIT-001), generalized: it is not a property of the AI Process Manager specifically, but of every non-human-form interaction path into ACECOG.

### 11.6.2 Command/Query Separation

The API is split along the same line as the underlying event-sourced storage model (Section 9, Section 11.3): a query/projection surface for everything read-heavy (portfolio dashboards, regional roll-ups, decision provenance lookups), and a small set of explicit, typed commands for everything that changes state (propose, deliberate, vote, run an optimization fit-check, commit, rebalance). Every command independently re-checks authority and Delegation Envelope regardless of which client issued it (Section 8.7).

### 11.6.3 Desktop Structured Surface

The primary surface for consequential action: dashboards, forms, and tables rather than a continuous chat scroll, so that binding constraints, vote tallies, and dependency graphs remain visible rather than paraphrased (non-negotiable principle 3: explainability and provenance take precedence over opaque optimization). Voting, approval, and commitment are always explicit UI actions here — a button, not a sentence — regardless of which surface a proposition originated from.

### 11.6.4 Conversational Assistant Surface

The AI Process Manager (Section 24) presented as a persistent assistant panel alongside the structured surface, not a full-screen replacement for it. Used for drafting, explanation, and natural-language query (e.g., 'why did this initiative's marginal value change this cycle'), answered from the same live data a dashboard would show. Any action the assistant helps prepare (a proposition, a rebalance) is surfaced as an explicit, reviewable form before submission — the assistant drafts; it does not submit on the user's behalf without that confirmation step (Section 24.3).

### 11.6.5 Mobile Surface

Mobile is specified as two distinct tiers rather than a single scaled-down app, because the two populations it serves have opposite needs.

- Resident tier (mass uptake): a jurisdiction-scoped feed or map of open propositions and votes, push notifications for relevant deadlines, and one-tap expression (consent, objection, delegate assignment/revocation per 17.3). Onboarding issues an ACECOG Identity at the Provisional tier (23.1.1); a higher tier is required only where the decision class itself requires it (invariant 13 (TRU-ELIG-001)). Decision Provenance (Section 9) is browsable read-only without any account, consistent with Section 0's principle that ACECOG is public and civic by design, and inspectable.

- Active-Role tier (agency staff, delegates, facilitators in the field): a bounded inbox of in-envelope decisions — a delegated rebalance awaiting sign-off, a routine approval within a Delegation Envelope (Section 7) — approved or escalated with a single action. Deliberative or multi-step review (regional roll-up, sensitivity analysis per Section 30.6) remains a desktop task; mobile is deliberately scoped to decisions that are quick, single-shot, and already bounded by an existing envelope.

The mobile surface is specified as a Progressive Web App rather than a native application: one codebase across platforms, and no app-store approval gate sitting between a Civic Body and its own governance tool, consistent with non-negotiable principle 8 (prefer open standards and public inspectability over vendor lock-in). A native shell may be added later only where a specific platform capability (e.g., robust offline sync) genuinely requires it.

### 11.6.6 Notification and Feed Neutrality

Mass-uptake mobile is where engagement-optimized design does the most damage to civic legitimacy, so it is specified against, not left to product judgment later. Generalizing the existing AI-drafting-neutrality invariant (AI-NEUTRAL-001, Section 14) and the participation-versus-outcome distinction of Section 17.3: any feed, ranking, or notification a citizen or active-role user receives shall be generated deterministically from governed proposition, deliberation, and delegation-envelope state — never ranked, timed, or suppressed to optimize engagement or attention — and the reason an item was surfaced (e.g., 'open for comment in your jurisdiction, closes in 3 days') shall always be visible alongside it.

### 11.6.7 New or Clarified Requirements

- A Notification/Subscription Service is added to the Section 11.2 core engines: tracks which Civic Bodies, jurisdictions, and decision classes each Actor watches, and delivers neutrally-generated alerts across mobile push, feed, and desktop surfaces from one shared subscription model.

- The command/query split (11.6.2) is added as an explicit architectural constraint on the Section 15 developer-ready handoff boundary: API and event contracts should be specified as typed commands plus a separate query/projection surface, not a single undifferentiated CRUD API.

<!-- -->

- Connectivity is part of the Prosperity Floor wherever participation depends on it (PF-07, 35.2); municipal broadband is named as the physical delivery path behind no-cost participation (invariant 24 (TRU-ACCESS-001)).

### 11.6.8 Acceptance Criteria (UIX-NEUTRAL-001..004)

- UIX-NEUTRAL-001. Submit the same proposition through the desktop form, the conversational assistant, and a mobile one-tap action, and confirm all three produce an identical governed Proposition object and pass through the identical authority/eligibility checks.

- UIX-NEUTRAL-002. Confirm the conversational assistant cannot submit, vote, or commit without an explicit human confirmation step, mirroring MVP acceptance test 111 and requirement AI-COMMIT-001 (24.3).

- UIX-NEUTRAL-003. Confirm a citizen's feed item and its accompanying push notification both display the reason it was surfaced, and that reordering, delaying, or hiding items for engagement cannot be configured through any exposed setting.

- UIX-NEUTRAL-004. Confirm an active-role mobile approval outside its Delegation Envelope is refused identically to the same action attempted on desktop (invariant 7 (GOV-ENVELOPE-001)), and is routed to escalation rather than silently retried.

# 12. Civic Trust, Security, Privacy, and Sovereignty

- Identity and role are distinct from authority; authentication proves identity, authorization proves permission, and neither alone establishes governance legitimacy.

- Approvals and high-consequence transactions should support cryptographic signing and tamper-evident integrity.

- Privacy shall be purpose-limited and jurisdiction-aware; public transparency shall not imply universal disclosure of personal data.

- Federation and data sharing require explicit consent, authority, and auditability.

- Open formats and exportability shall permit independent audit, migration, fork, and continuity of civic operation.

- No vendor, host, AI provider, or infrastructure operator acquires governance authority by controlling technical access.

- Security controls shall preserve separation of duties, least privilege, immutable history, and recovery from compromise.

Section 43 (Compliance & Assurance) turns these principles into mandatory Assurance Controls (43.2), an operator certification roadmap (43.3), Jurisdiction Compliance Packs (43.4), AI governance alignment (43.5), and operator-conduct rules (43.6).

## 12.0.1 Accountable Monitoring

Dual approval and similar monitoring controls (4.2 GML-1) govern decisions; they do not by themselves govern the monitors. A role exercising approval or monitoring authority requires its own accountability path back to the Civic Body, not only to the decision it reviews.

- Any Actor/Role/Agent (7) exercising approval or monitoring authority at GML-1 and above carries an `accountability_path`: who selected or ratified the role-holder, and the mechanism by which they can be rotated or recalled.

- Selection or ratification of such roles runs through the Civic Body’s own Governance Process (17.5); a role shall not be self-appointed, nor appointed solely by the role it monitors.

- No Actor may grant authority to itself, for any action. Authority is granted as named actions; an open-ended grant of every action exists only in the founding charter and is never grantable afterwards (CL-079).

- An approval authorizes only the subject it names. A decision used to appoint a role, adopt evidence as the basis of a constraint, create a baseline, resolve an exception or put a change in force must name that exact subject in its requested action (the person and the actions; the evidence and the constraint; the model version; the exception; the target and a hash of the change, CL-046), and is used for it once. A mismatched or reused approval is refused (CL-079).

- Selection addresses adverse selection — who is chosen and how they can be removed — but not moral hazard: an agent’s conduct *between* selection and recall. Any such Actor/Role/Agent therefore also carries an `approval_track_record`, automatically populated from Exception Propositions and Tier-2/3 outcomes (5.11.1, invariant 18 (GOV-GRADUATED-001)) linked to their approvals. The record is surfaced whenever rotation or recall is considered; it does not itself trigger recall — recall remains a civic-body decision through the Governance Process, never an automated consequence of the record alone (TRU-MONITOR-002, a requirement since v0.20).

## 12.1 Regulatory and Standards Alignment

Civic software carries compliance obligations beyond sound architecture. What a GML-0/GML-1 MVP should account for now is narrower than what a GML-2/GML-3 statutory deployment eventually requires (4.2); this subsection separates the two rather than front-loading a full federal compliance program onto a pilot council.

Needed from MVP onward, and now enforced at every GML level as the Assurance Controls (43.2): secure-development hygiene aligned with the NIST Secure Software Development Framework (SP 800-218); privacy hygiene consistent with applicable state and regional privacy law; WCAG 2.2 AA (ISO/IEC 40500:2025) accessibility for every interface; an explicit records-retention schedule for the event log and artifact store (11.3); AI transparency and human-oversight documentation consistent with Section 10; and a Software Bill of Materials generated at build time.

Scheduled by hosting model and GML level (43.3): SOC 2 and GovRAMP from the first production tenant on any shared multi-tenant platform (22.5); ISO/IEC 27001 and FedRAMP only where buyers or federal tenants require them; and, for statutory GML-2/GML-3 deployments, full Risk Management Framework authorization (SP 800-37) on the complete SP 800-53 control catalog, GASB and 2 CFR Part 200 alignment for federal-grant funding instruments (5.13), Single Audit Act-sufficient audit trails, and multi-signature release governance.

A standing disclaimer applies regardless of GML level: ACECOG produces advisory planning and coordination outputs. It does not execute financial instruments, replace an accounting system, or constitute legal or financial advice.

ASR-08 carries this disclaimer to every screen by labeling each result’s legal status (43.2). Section 43 is the governing module for everything in this subsection, including jurisdiction-specific obligations (43.4), AI governance alignment (43.5), and operator conduct (43.6).

# 13. Development Phasing

Duration estimates below assume a small, senior team working sequentially (one senior full-stack engineer, one optimization/solver engineer, a part-time UX designer, and the domain/governance owner) and each phase’s gate criteria being met before the next begins. They are planning assumptions, not commitments, and should be revisited once Section 15’s developer-ready contracts exist.

## 13.1 Phase 1 — Civic Governance Workbench / MVP (est. 5–7 months)

The MVP should prove the full governance-to-execution discipline on a deliberately small real or sandbox civic case rather than attempt universal scale.

- One Civic Body / jurisdiction with 3–12 active participants casting binding votes. Residents take part through the Resident tier (comment, expression, and advisory signal), sized for 2,000 registered residents with 200 active at once (CL-065; figure confirmed by the owner at Gate 1).

- Civic propositions, objectives, constraints, authority, delegation, portfolio hierarchy, resources, relationships, decisions, evidence/actuals, and exceptions.

- Portfolio → Program → Project hierarchy with cross-tree relationship edges.

- Phase 1 solver profile: deterministic LP and convex QP only, behind the solver abstraction that later carries MILP, robust, and stochastic methods. Higher-order (cubic and above) PPM terms are disabled. The canonical objective is to maximize cᵀx − ½xᵀQx with Q positive semidefinite (5.3). A Q matrix that is not positive semidefinite is rejected before solving, and the rejection and its reason are recorded in the Decision Provenance Packet.

- Proposal, validation, deliberation/approval, baseline, optimization, delegated resolution, commitment, actuals, variance, and exception state machines.

- Deterministic CPM and basic resource leveling.

- Decision Provenance Packets, immutable version references, replay, and structured minority-position capture.

- One demonstrated rote delegated rebalance and one forced governance escalation.

- A second-jurisdiction coupling scenario retained as a test fixture even if live federation is deferred.

<!-- -->

- Assurance Controls ASR-01 to ASR-11 (43.2), and the open-meeting guard of whichever Jurisdiction Compliance Pack applies to the pilot (43.4).

- If the pilot runs on shared hosting (22.5.1): SOC 2 Type I and GovRAMP Core before the first production tenant (43.3).

### MVP Success Measures

- time to structured decision compared with ordinary process;

- constraint conflicts caught before commitment;

- unauthorized commitment attempts blocked;

- decision replay success rate;

- quality and completeness of provenance;

- user comprehension and trust in outputs;

- ability to rebaseline without losing historical state.

## 13.2 Phase 1.5 — Execution and Risk Maturity (est. +2–3 months)

- expanded CPM/resource leveling and execution adapters;

- triangular or similarly simple Monte Carlo risk analysis;

- rebalance planning and divergence reports;

- stronger signing, separation of duties, and operational security;

- external data ingestion with provenance and quality controls.

v0.18 pulls two Part V items into Phase 1.5: the Funding Instrument extensions (40), which make JNY-FUND-006 testable, and version 0.2 of the Ecosystem Endowment Simulator (42); version 0.1 is a standalone Phase 1 demonstration (13.6, CL-072).

## 13.3 Phase 2 — Federated Intelligence (est. +4–6 months)

- local-first federation protocol and synchronization;

- opt-in data sharing and privacy controls;

- cross-jurisdiction portfolio composition and constraint stacking;

- comparative scenario libraries and pattern detection;

- treaty/compact authority interfaces and shared transaction semantics;

- federation conflict reconciliation and audit trails.

## 13.4 Phase 3 — Large-Scale / Bioregional Coordination (not yet scoped)

- multi-jurisdiction and bioregional portfolio optimization;

- cross-PPM stitching at larger scale;

- long-horizon ecological and infrastructure scenarios;

- civilization-scale coordination sandboxes while preserving jurisdictional sovereignty and explainability.

Unlike Phases 1–2, Phase 3 is deliberately left without a duration estimate. The principle of assuming that sophisticated actors will attack the seams between planes applies most directly here: rushing bioregional or civilization-scale coordination ahead of a proven, GML-2/3-capable Phase 2 is the single largest identified risk to this roadmap, larger than any individual technical risk in Section 6 or 18.

Part V's modules (Sections 31–41) enter the catalog here, as Phase 3 / Catalog Reserve, because they span municipal economic development, public finance and emergency management.

End-to-end, Phases 1 through 2 total roughly 11–16 months from architecture freeze to a working federated-intelligence capability, assuming each phase’s gate criteria (13.1–13.3, 14) are met before the next begins.

## 13.5 Phase 1 Month-by-Month Build Plan

The MVP reference scenario (26.1) — a Civic Body allocating a constrained budget across 8–20 candidate initiatives — anchors this schedule. Each month’s gate must pass before the next begins.

| Month      | Focus and Gate                                                                                                                                                                                                                                      |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1          | Architecture freeze: canonical object schemas (Section 7), job contracts (11.4), state- machine definitions (Section 8), GML-1 governance policy, including a second approver on commitments (CL-052). Gate: no unresolved architectural questions. |
| 2          | Core infrastructure: event log, snapshot store, artifact store, Orchestrator skeleton, role/authority model. Gate: event replay works.                                                                                                              |
| 3          | Governance Plane: Civic Body, Governance Process, propositions, deliberation record, approval rule (17). Gate: two competing propositions preserved with exact versions (MVP test 101).                                                             |
| 4          | Optimization integration: solve_ppm, strict-mode determinism, feasibility and sensitivity output (5, 18). Gate: replay verified across restarts.                                                                                                    |
| 5          | Execution layer: dependency graph, CPM, capacity check, commitment semantics (6, 19, 8.7). Gate: no worker can mutate committed state.                                                                                                              |
| 6          | Evidence and rebalance: actuals ingestion, variance detection, delegated rebalance, Exception Proposition generation (8.8, 5.11, 20). Gate: within-envelope rebalance and forced escalation both demonstrated.                                      |
| 7 (buffer) | Hardening: MVP acceptance tests 100–114 (26.2) run end to end; UX simplification; second-jurisdiction test fixture (13.1) wired but not live-federated.                                                                                             |

## 13.6 Phase 1 Execution Filter

This filter tells a Phase 1 development team what to build. **Build** means implement and test in Phase 1. **Interface only** means define the schema and extension points, but implement no behavior. **Out of scope** means do not build it in Phase 1. When this table and another section differ on Phase 1 scope, this table governs.

| Sections                                                                  | Phase 1 status                                                                                                                                       | Notes                                                                                                                       |
|---------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| 0–6 Purpose, planes, governance model, portfolio mathematics              | Build                                                                                                                                                | Solver limited to the Phase 1 profile (13.1). Funding Instrument: Appropriation type only (5.13). GML-0 and GML-1 controls Build; GML-2 and GML-3 controls interface only (4.2)                                                                                |
| 7 Canonical object model                                                  | Build                                                                                                                                                | Part V objects interface only. Part VI: Retention Schedule, Legal Effect Declaration, Interest Declaration, Compliance Pack, and Compliance Module are Build; Control Mapping and Engagement Record interface only. ACECOG Identity, Assurance Anchor, Reconciliation Case, Continuity Office, and Continuity Case are Build                                                                               |
| 8 State machines and decision status model                                | Build                                                                                                                                                | Including the version-binding rule (8.9). Proposition states (8.2–8.3) and commitment states (8.7) Build; execution states Issued and Acknowledged (8.8) interface only, at the external-system boundary (19.6)                                                                                    |
| 9 Decision Provenance and replay                                          | Build                                                                                                                                                |                                                                                                                             |
| 10 AI authority boundary                                                  | Build                                                                                                                                                |                                                                                                                             |
| 11.1–11.5 Architecture, storage, packaging                                | Build                                                                                                                                                | Bundled workers; local-first as defined in 11.5                                                                             |
| 11.6 Interaction architecture                                             | Build: desktop structured surface, conversational panel, and the Resident tier of the mobile PWA (11.6.5). Out of scope: the Active-Role mobile tier | Resident tier brought into the pilot (CL-049); Active-Role tier at Phase 1.5                                                |
| 12 and 23 Civic Trust Plane                                               | Build                                                                                                                                                |                                                                                                                             |
| 14 Invariant Floor                                                        | Build: invariants 1–19, 21, 23, 24, 26. Interface only: 20, 22, and 25                                                                                         | Invariant 20 needs standards tooling (from 1.0); invariant 22 needs live federation (Phase 2); invariant 25 needs a compulsory obligation (Section 39, Part V)                               |
| 14.2 Module floors                                                        | Out of scope                                                                                                                                         | Enter with their modules                                                                                                    |
| 15 Developer-ready handoff                                                | Build first                                                                                                                                          | Schemas and API contracts precede application code                                                                          |
| 16–21 Governance, optimization, scheduling, execution, evidence, learning | Build                                                                                                                                                | MILP, robust, and stochastic methods are interface only. Delegation: single-level, revocable, per decision class is Build; transitive (liquid) chains are deferred (17.5)                                                                     |
| 22 Federation                                                             | Interface only                                                                                                                                       | The second-jurisdiction coupling scenario stays as a test fixture (13.1). Shared hosting (22.5) only if the pilot is hosted |
| 24 AI Process Manager                                                     | Build                                                                                                                                                | Draft-only; every commit passes the authority gate                                                                          |
| 26–27 Acceptance tests and traceability                                   | Build                                                                                                                                                | MVP-100 to MVP-114 and the INV-AT tests are the Phase 1 acceptance suite                                                    |
| 28 Domain portability                                                     | Reference only                                                                                                                                       |                                                                                                                             |
| 29 Part III, Civilizational Maturity and Type-I Transition                | Out of scope: no build phase                                                                                                                         | See the status note at the start of Section 29                                                                              |
| 30 Journeys                                                               | Build: 30.5 Grad Student, 30.7 Resident/Voter, 30.8 City Manager, 30.9 Facilitator/Clerk. Out of scope: the rest                                     | 30.5 drives the demonstration                                                                                               |
| 31–41 Part V modules                                                      | Out of scope (Phase 3 / catalog reserve)                                                                                                             |                                                                                                                             |
| 42 Ecosystem Endowment Simulator                                          | Build as a standalone demonstration                                                                                                                  | Feeds the Development Environment / Simulator Alpha                                                                         |
| 43 Compliance and Assurance                                               | Build: ASR-01 to ASR-11, pack composition (43.4), and the Colorado module's rules (43.4.2). Out of scope: certifications unless the pilot is hosted  |                                                                                                                             |

## 13.7 Pilot Program Plan

Sections 13.1 to 13.6 say what Phase 1 must build. The pilot program is the plan for putting that build in front of one real jurisdiction. Its stages are called Pilot Stages 1 to 7, to keep them distinct from development Phases 1, 1.5, 2, and 3 (CL-073). Its authoritative form is the ACECOG Pilot WBS workbook (rev 4), which holds durations, costs, logic, risks, milestones, and roles. This subsection records the plan's shape and the rules from this specification that it must respect. Appendix N maps every work package to the sections it delivers or depends on.

| Phase                                    | Purpose                                                                                                                                     | Exit gate                                                  |
|------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| Stage 1 (WBS 1.0): foundation, contracts, and hardening | Publish the developer contracts (Appendix M), close the gap between the prototype and the 13.6 execution filter, harden security, and audit | Phase 1 acceptance suite passing; independent audit closed |
| Stage 2 (WBS 2.0): jurisdiction selection               | Find one consenting jurisdiction with a named sponsor                                                                                       | Sponsor confirmed in writing                               |
| Stage 3 (WBS 3.0): legal validation                     | Answer the 43.8 questions for the pilot state, map authority and envelopes to the charter, and author the pilot-state Compliance Pack       | Legal opinion; pack confirmed by counsel                   |
| Stage 4 (WBS 4.0): program design and agreement         | Select the program, configure the Governance Process, and sign the MOU                                                                      | MOU signed with a Legal Effect Declaration                 |
| Stage 5 (WBS 5.0): configuration                        | Install on hardware the jurisdiction controls (11.5), configure, load data, build the front end, and prove backup, restore, and exit        | Instance ready for shadow operation                        |
| Stage 6 (WBS 6.0): staged validation                    | Shadow run (Advisory), independent review, then one binding cycle and a strict replay                                                       | First binding cycle audited and reproducible               |
| Stage 7 (WBS 7.0): launch and evaluation                | Public launch, stabilization, evaluation, and a joint go/no-go                                                                              | Written go/no-go decision                                  |

**Critical path.** With finish-to-start logic and no calendar, the workbook schedules about 55 working weeks. The critical path runs through jurisdiction selection, legal review, and the pilot-state Compliance Pack, then configuration, the front end, accessibility conformance, the shadow run, the first binding cycle, launch, and evaluation. The Phase 1 conformance work runs in parallel and carries float. Calendar time will be longer once holidays, counsel availability, and legal contingency are added.

**Rules the pilot inherits from this specification.**

- No cycle is presented as binding without a Legal Effect Declaration (invariant 26 (ASR-STATUS-001), ASR-08). The shadow run is labeled Advisory. If no declaration is obtainable, the pilot runs as a consultative or advisory cycle.

- The first binding cycle waits for the independent audit to close, the backup, restore, and exit drill to pass (invariant 12 (TRU-EXIT-001)), and the incident-response plan (ASR-09).

- The pilot runs on an installation the jurisdiction controls (11.5) and under the Assurance Controls (43.2) at every GML level. The pilot body operates at GML-1 before its first binding cycle (CL-052).

- The pilot state is Colorado (CL-048). Its pack is composed from federal, Colorado state, local, and Civic Body modules (43.4); the Colorado module (43.4.2) needs counsel confirmation (WBS 3.3).

- Phase 1 scope follows 13.6: the desktop structured surface, the conversational panel, the Facilitator/Clerk journey, and the Resident tier of the mobile PWA, so residents can take part from a phone (CL-049). The Active-Role mobile tier enters at Phase 1.5. Decision Provenance needs no account.

- Funding uses an MVP Funding Instrument type (5.13). In Colorado that means an existing appropriation, because TABOR requires voter approval for new taxes (39).

**Decided.** The Resident mobile tier is in the pilot (CL-049); WBS 5.3.1 grows to include it.

**Pilot electorate (CL-065).** Binding votes stay with the defined body, within the Phase 1 design size; this is a stated limit of the first test, not a design choice. Residents' first cycle is a mock (advisory) cycle. Their next cycle is binding, or comes with an assurance of recognition: the body commits in advance to adopt the result or to respond to it formally.

**Steering committee (CL-071).** A joint steering committee, if formed (WBS 4.2.2), is advisory to the Governance Process. Operator or steering-committee configuration takes effect only on the body's recorded adoption (43.6).

# 14. System-Level Functional Invariants and Acceptance Criteria

The Invariant Floor is the set of 26 rules that bind every Civic Body on every deployment. Each passes the admission test in 14.1: permitting a Civic Body to violate it would undermine the integrity of self-governance itself. Each has a stable ID, which is the primary reference throughout this specification; the numbers are list positions only. v0.20 renumbered the register from 27–70 to 1–26 and moved module-specific, operational, and commercial rules to the layers below; Appendix K holds the concordance.

## 14.0 Protection Layers

Protections apply in seven layers, highest first. Under invariant 19 (GOV-FRAMEWORK-001), no lower layer may waive or relax a requirement of a higher one.

1.  **Invariant Floor** (Section 14): binds every Civic Body.

2.  **Module floors** (14.2): bind every Civic Body that adopts the module, and only those.

3.  **Assurance Controls** (43.2): bind every deployment.

4.  **Deployment and operator controls** (22.5, 43.3, 43.6).

5.  **Jurisdiction Compliance Packs** (43.4).

6.  **Maturity framework** (4.2, 4.3).

7.  **Local governance configuration** (17.5).

The word "floor" has six meanings in this specification:

| Term                       | Meaning                                                                                                              | Where                  |
|----------------------------|----------------------------------------------------------------------------------------------------------------------|------------------------|
| Invariant Floor            | The 26 invariants of this section                                                                                    | 14                     |
| Module floor               | Rules that bind every Civic Body adopting a module                                                                   | 14.2, 35.4, 36.6, 37.5 |
| Guardian module floor      | The module floor of Guardian Jurisdictions                                                                           | 37.5                   |
| Prosperity Floor           | A Civic Body's ratified substantive entitlement for members with standing; its access conditions form a module floor | 35                     |
| Protected floor            | Any minimum the system protects from trade-offs, such as a Prosperity Floor level or a certified ecological limit    | Invariant 9            |
| Minimum requirements floor | The proposed ISO standard's term for the Invariant Floor                                                             | Appendix I             |

Assurance Controls (43.2) and Civic Assurance and Buffering (34) are different things: the first are compliance controls, the second is the delivery-readiness module.

**The invariants.**

1.  No destructive overwrite of prior approved states, decisions, evidence, baselines, model versions, settlements, or accrued entitlements; later rules never alter a past settlement, an accrued entitlement, or the recorded reasons for an earlier decision. (DPP-IMMUTABLE-001)

2.  No execution without a valid authority path. (GOV-AUTHPATH-001)

3.  No silent relaxation of a hard constraint. (OPT-CNST-001)

4.  No silent conversion of uncertain evidence into normative authority. (EVD-NORM-001)

5.  No baseline overwrite by forecast or actual data. (EXE-BASELINE-001)

6.  No cross-jurisdiction binding effect without explicit authority or agreement. (FED-AUTH-001)

7.  No automated decision outside the active Delegation Envelope. (GOV-ENVELOPE-001)

8.  No commit-eligible solver result without reproducible model, version, and configuration identifiers. (OPT-REPRO-001)

9.  No optimization criterion may compensate for a non-compensable mandatory objective or a protected floor; any shortfall below a protected floor is recorded as a breach. (OPT-NONCOMP-001)

10. Every material exception identifies the governing conflict and the authority required to resolve it. (GOV-EXCEPT-001)

11. Every material decision can be reconstructed from immutable state and provenance. (DPP-REPLAY-001)

12. Every Civic Body can export the information required to continue its governance independently, in documented open formats, without requiring the operator's discretion or cooperation beyond running the export. (TRU-EXIT-001)

13. No participating-population count may exceed the count of currently valid, unique Membership Credentials for the applicable civic scope. A result whose margin or quorum could be reversed by participants below the decision class's full-confidence tier, or by open Reconciliation Cases, is labeled assurance-sensitive and shall not drive a GML-2+ commitment until resolved (23.1.1). (TRU-ELIG-001)

14. No cross-block coupling coefficient (5.6) may take a value, in any proposed joint federated solution, that would violate a non-compensable mandatory objective of any participating jurisdiction, even where that jurisdiction's own local constraints remain nominally unchanged. (FED-RIGHTS-001)

15. AI-drafted proposition text, evidence summaries, and comparative analyses presented for material decisions shall preserve the substantive content and relative framing supplied by their human authors; AI-introduced language, emphasis, or ordering beyond direct transcription shall be flagged as AI-modified and available for side-by-side comparison against the original input. (AI-NEUTRAL-001)

16. A Civic Body's Governance Process shall track cumulative distributional effect on any identifiable constituency across a rolling decision window; when cumulative effect crosses the same materiality threshold that would trigger a single-decision Exception Proposition (5.11), the system shall generate a Cumulative Exception Proposition routed to the same authority, even where no individual decision in the window crossed the threshold alone. (GOV-CUMULATIVE-001)

17. At GML-1 and above, roles exercising approval or monitoring authority shall be selected or ratified through the Civic Body's own Governance Process, subject to defined rotation and recall, and shall not be self-appointed or appointed solely by the role they monitor. (TRU-MONITOR-001)

18. Responses to a breach of a Governance Process rule or Delegation Envelope threshold apply to governance privileges only; no response may suspend or reduce a person's participation access (invariant 24) or any module-floor entitlement (14.2). The graduated ladder that starts with a notice or warning is the Reference Maturity Framework's default practice (5.11.1). (GOV-GRADUATED-001)

19. Protections apply in the layers of 14.0: the Invariant Floor, module floors where a module is adopted, Assurance Controls, deployment and operator controls, Jurisdiction Compliance Packs, maturity frameworks, and local governance configuration. No lower layer may waive or relax a requirement of a higher one. Every Civic Body publishes an interoperability declaration mapping its maturity framework to the common control categories (eligibility, cross-jurisdiction rights, AI neutrality, cumulative effect, accountable monitoring, graduated sanctions) for federation comparability. (GOV-FRAMEWORK-001)

20. Every Floor Revision Proposal (14.1) shall be classified as strengthening or weakening protection under the prime directive (14.1); a proposal that weakens, removes, or narrows any invariant or module-floor rule, including the Floor Revision Process itself, shall not be ratified without independent verification by a reviewer distinct from both the proposer and the Editorial Panel. This classification is self-applying and admits no special case for amending the amendment process. (GOV-FLOOR-001)

21. A Civic Body's amendment to its own Governance Process (17.5) that weakens an existing protection, including amendment of its own amendment rule to ease future weakening, requires the same harder-path threshold that would govern the change it enables; amendments that strengthen an existing protection may proceed through ordinary process. (GOV-RATCHET-001)

22. A Civic Body's ratified floor edition, and any lag behind the current published edition, shall be visible in its federation interoperability declaration (4.3, invariant 19) and Maturity Framework mapping (22.2); a federation partner shall never be left unaware which floor edition another party is operating under. (FED-EDITION-001)

23. A shared-hosting platform operator holds no standing Authority (Section 7) into any tenant Civic Body's Governance Process; every authority and Delegation Envelope check that applies to a self-hosted Civic Body applies identically to one hosted on a shared platform, and no operational or infrastructure role may substitute for, or bypass, that check. (TRU-TENANT-001)

24. No person may be charged a fee, premium, deposit, deductible or contribution-history requirement to take part in any Civic Body's governance process: viewing, proposing, deliberating, voting or consenting, delegating, appealing, or verifying Decision Provenance. The only permitted precondition is positive unique-identity assurance at the tier the action requires (invariant 13); that assurance shall be obtainable at no cost and issued ad hoc to anyone who lacks an identity document, with uniqueness protected afterward by a reconciliation process that merges duplicates without cutting off access, not by barriers at entry. (TRU-ACCESS-001)

25. Anyone subject to a compulsory collective funding obligation has standing in the governance process that sets, amends or renews it. Default for non-resident payers: standing on the obligations they pay only. (GOV-VOICE-001)

26. Every decision and published result carries its lifecycle state and its legal status as separate, separately displayed attributes (8.0). No lifecycle state implies legal effect: a decision is presented as binding only where a Legal Effect Declaration covering its decision class exists, and is otherwise labeled advisory or consultative. (ASR-STATUS-001)

**Acceptance tests.** Every invariant has at least one acceptance test.

| Invariant             | Acceptance tests                      |
|-----------------------|---------------------------------------|
| 1 DPP-IMMUTABLE-001   | MVP-101, MVP-108, INV-AT-01           |
| 2 GOV-AUTHPATH-001    | MVP-111, UIX-NEUTRAL-002, JNY-FAC-006 |
| 3 OPT-CNST-001        | MVP-107                               |
| 4 EVD-NORM-001        | INV-AT-04                             |
| 5 EXE-BASELINE-001    | MVP-105                               |
| 6 FED-AUTH-001        | INV-AT-06, JNY-FED-001..007           |
| 7 GOV-ENVELOPE-001    | MVP-106, MVP-107, UIX-NEUTRAL-004     |
| 8 OPT-REPRO-001       | MVP-103, MVP-109, INV-AT-08           |
| 9 OPT-NONCOMP-001     | MVP-107, PF-AT-01..04, INV-AT-09      |
| 10 GOV-EXCEPT-001     | MVP-107                               |
| 11 DPP-REPLAY-001     | MVP-109, JNY-GRAD-010                 |
| 12 TRU-EXIT-001       | MVP-110, FED-HOST-003, CMP-007        |
| 13 TRU-ELIG-001       | INV-AT-13                             |
| 14 FED-RIGHTS-001     | INV-AT-14, JNY-FED-001..007           |
| 15 AI-NEUTRAL-001     | INV-AT-15, MVP-114                    |
| 16 GOV-CUMULATIVE-001 | INV-AT-16                             |
| 17 TRU-MONITOR-001    | INV-AT-17                             |
| 18 GOV-GRADUATED-001  | INV-AT-18                             |
| 19 GOV-FRAMEWORK-001  | CMP-001, CMP-002, INV-AT-19           |
| 20 GOV-FLOOR-001      | INV-AT-20                             |
| 21 GOV-RATCHET-001    | INV-AT-21                             |
| 22 FED-EDITION-001    | INV-AT-22                             |
| 23 TRU-TENANT-001     | INV-AT-23, FED-HOST-001..005          |
| 24 TRU-ACCESS-001     | INV-AT-24, CAB-AT-01, PF-AT-01..04    |
| 25 GOV-VOICE-001      | INV-AT-25                             |
| 26 ASR-STATUS-001     | CMP-006, INV-AT-26                    |

The INV-AT tests:

- **INV-AT-01:** After a rule change, a prior settlement, accrued entitlement, and recorded reasons replay unchanged.

- **INV-AT-04:** Evidence whose epistemic class is Estimated, Assumed, Scenario output, or Hypothesis cannot be attached as a binding constraint until a decision adopts it; the attempt is refused with its reason.

- **INV-AT-08:** An optimization result missing its model, version, configuration, or seed identifiers is refused at commit.

- **INV-AT-09:** A solution that raises the aggregate score by pushing a protected floor below its minimum is rejected; an unavoidable shortfall is recorded as a breach.

- **INV-AT-13:** A tally whose participant count exceeds valid unique credentials is refused. With a margin of 3 and 4 Provisional participants, the result is assurance-sensitive and blocked from GML-2 commitment; with a margin of 5, it proceeds. A duplicate found after close triggers a recount; an outcome-changing recount is flagged and routed, and the merged person keeps participating. A new anchor whose hash matches an existing identity opens a Reconciliation Case and is not added.

- **INV-AT-16:** Ten individually immaterial decisions that together cross the materiality threshold for one constituency within the window raise a Cumulative Exception Proposition.

- **INV-AT-17:** An approval or monitoring role appointed by the role it monitors is refused; every such role records its rotation and recall terms.

- **INV-AT-18:** A sanction that would reduce a person's participation access or a module-floor entitlement is refused.

- **INV-AT-19:** A Maturity Framework, Compliance Pack, operator default, or local configuration that would relax a higher-layer requirement is refused at adoption, naming the layer it conflicts with.

- **INV-AT-20:** A Floor Revision Proposal classified as weakening cannot reach Ratified without a recorded independent verification. Applies from 1.0; built with the standards tooling.

- **INV-AT-21:** An amendment that lowers the threshold of the amendment rule itself requires the higher threshold it would remove.

- **INV-AT-22:** A federation partner's view shows each other party's floor edition and any lag behind the current edition.

- **INV-AT-25:** A person subject to a new compulsory obligation can propose, deliberate, and vote in the process that sets it; a non-resident payer's standing is limited to that obligation.

- **INV-AT-26:** A Committed decision without a Legal Effect Declaration displays lifecycle state Committed and legal status Advisory; no view labels it binding.

Added at Gate 1 so that every Phase 1 Build invariant has a test that exercises it (CL-056):

- **INV-AT-06:** Against the second-jurisdiction fixture (13.1), an action of one Civic Body that would bind the other without authority under a Federation Contract is refused; with that authority it succeeds and records both bodies' authority basis.

- **INV-AT-14:** Against the same fixture, a coupled decision that would violate the other party's non-compensable objective is blocked before it is finalized, naming the objective.

- **INV-AT-15:** For a material proposition drafted or summarized by the assistant, every AI-introduced change is flagged, and the author and every reviewer can open a side-by-side view of the human and AI versions; an unflagged AI change fails the test.

- **INV-AT-23:** In single-tenant form, an infrastructure or administrator role attempting a governance action (adopting a process, resolving within an envelope, or issuing a credential outside a registrar's direction) is refused like any actor without authority.

- **INV-AT-24:** Every governance function (viewing, proposing, deliberating, voting or consenting, delegating, and verifying provenance) is reachable with no fee, payment step, or contribution-history check, and identity issuance at the Provisional tier costs nothing.

## 14.1 Invariant Floor Amendment (ACECOG Standards Process)

Sections 0–28 and Part III describe how a Civic Body governs itself. This subsection describes how the invariant floor those Civic Bodies operate under is itself governed — the constituent question every durable rule-system eventually has to answer, and one this specification left implicit through v0.10.

The model is civil engineering’s bridge-code tradition rather than software’s: a design code (AASHTO LRFD, ASCE 7) is maintained by a standing technical body distinct from any engineer using it, revised on a fixed cycle, and never waivable by a client’s preference. Software never built the equivalent licensure culture (the PE Software Engineering exam was retired in 2019 for lack of adoption); ACECOG adopts the discipline anyway, deliberately, rather than assuming a professional structure that does not exist for this field.

**Prime directive.** ACECOG’s invariant floor exists to hold paramount the self-governance capacity, rights, and safety of the Civic Bodies and individuals it serves. This duty is not waivable by any Civic Body’s majority, Maturity Framework, or federation agreement — including by the Standards Process’s own amendment power, except through the harder path below. Every Floor Revision Proposal is classified against this directive, not against convenience, efficiency, or any single Civic Body’s preference.

**Stage 1 — Draft.** Any person may submit a Floor Revision Proposal (FRP). Authorship is open, IETF-style: deliberation proceeds by rough consensus, meaning objections are answered on the record rather than outvoted. A small, rotating Editorial Panel manages the process and calls when rough consensus is reached. Panel seats are Actor/Role/Agent instances (7) and therefore already carry `accountability_path` and `approval_track_record` (12.0.1, invariant 17 (TRU-MONITOR-001) and TRU-MONITOR-002) — the one concentration of power in this process is the part already built to be accountable and recallable.

**Stage 2 — Classify.** Every FRP is tested against the prime directive and sorted as strengthening (adds or tightens a protection) or weakening (removes, narrows, or waives one). Strengthening proposals proceed directly to Stage 3b. Weakening proposals — including any FRP that would weaken the Floor Revision Process itself, such as shortening the comment period or removing the verification requirement — are routed to Stage 3a first. This is the same self-applying ratchet invariant 21 (GOV-RATCHET-001) applies at the civic-body level; there is no separate, easier path for amending the amendment rules.

**Stage 3a — Verify (weakening proposals only).** Independent review by a reviewer distinct from both the proposer and the Editorial Panel — the Independent Engineering Verification analog for a major structure. No weakening proposal reaches ratification without this gate (invariant 20 (GOV-FLOOR-001)).

**Stage 3b — Ratify.** A verified or directly-qualifying-strengthening FRP publishes as a new edition with an effective date, on a fixed review cycle with a narrower emergency/errata track for urgent fixes — generalizing the sunset/review pattern already used by 17.5’s emergency authority and 22.2’s Federation Contract exit and amendment terms. Individual Civic Bodies ratify an edition into their own Maturity Framework the same way they ratify the Reference Framework (4.3). A body that does not ratify is never compelled — it continues under its prior edition, grandfathered the same way Sections 9 and 21.3 preserve the versions that governed a historical decision — but its edition is never invisible: invariant 22 (FED-EDITION-001) requires it to appear in that body’s federation interoperability declaration and Maturity Framework mapping, so a prospective federation partner always knows which floor edition they would be trusting.

**Admission test.** Every Floor Revision Proposal that would add an invariant or a module-floor rule states in writing, at Stage 2, why permitting a Civic Body to violate it would undermine the integrity of self-governance itself, and declares its scope: the Invariant Floor or a named module floor. A rule that fails the test belongs in a lower layer (14.0).

**Floor review.** Each major edition includes a review of the whole floor, which may propose demotions; those follow the weakening path through Stage 3a.

**When this process applies.** The Floor Revision Process governs the Invariant Floor and module floors from the first published edition (1.0). Editions numbered 0.x are working drafts managed under the project change log.

## 14.2 Module Floors

A module floor binds every Civic Body that adopts the module, and only those. Module floors are amended like the Invariant Floor (14.1), so their rules keep the same ratchet protection for every adopter. v0.20 moved eight former invariants here (Appendix K).

| Module                     | Module floor | Rules                                                                                                                                                                                                                                     |
|----------------------------|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Prosperity Floor (35)      | 35.4         | GOV-PROSPERITY-001 (unconditioned floor access); PF-F2 (standing changes apply prospectively only)                                                                                                                                        |
| Commons Endowment (36)     | 36.6         | GOV-COMMONS-001 (depletion rents to principal); GOV-COMMONS-002 (collective conditions only); ECO-COLLATERAL-001 (no pledging of ecosystem assets); CE-F4 (certified revenue classification); CE-F5 (standing changes prospective)        |
| Guardian Jurisdiction (37) | 37.5         | The ten Alaska-derived floor items; ECO-GUARD-001 to 003; FED-SYMBIOSIS-001; GJ-F1 (council selection and accountability); GJ-F2 (Commission independence and expiring limits); GJ-F3 (appeal of a binding veto on certification grounds) |

# 15. Developer-Ready Handoff Boundary

This integrated specification defines the civic ethos, functional planes, governance chain, quantitative model, canonical objects, state machines, transaction semantics, AI boundaries, provenance requirements, and phased scope. The next layer should translate these stable semantics into machine contracts without changing their meaning.

- canonical JSON/schema definitions and validation rules;

- API and event contracts;

- authorization and Delegation Envelope policy expressions;

- solver interfaces and numerical tolerances;

- state-machine transition tables and permission tests;

- reference database/event-store representation;

- reference MVP deployment architecture;

- security threat model and recovery semantics;

- end-to-end acceptance-test fixtures for one jurisdiction and one coupled-jurisdiction scenario.

Appendix M records the first of these contracts: the API contract v0.1 for the command/query split, with a mock implementation and contract tests that check the Phase 1 acceptance tests from outside (CL-041).

# Part II - Layered Functional Analysis

This part restores the analytical depth of the original functional specification beneath the v0.3 civic architecture. The Design-Build-Operate-Learn lifecycle describes the civic operating cycle; Sense-Model-Deliberate-Decide-Remember describes the information-processing cycle that recurs within it. Each functional plane below is analyzed in terms of purpose, actors, inputs, transformations, outputs, controls, exceptions, feedback, and dependencies.

*Design / Build / Operate / Learn contains Sense -\> Model -\> Deliberate -\> Decide -\> Remember*

# 16. Recursive Civic Decision Cycle

## 16.1 Sense

Sense converts observations of civic, financial, operational, ecological, and social conditions into governed evidence. It is the boundary between the external world and ACECOG's internal model of that world.

- Inputs: human reports, financial transactions, project actuals, asset/operations data, surveys, public expressions, sensors, GIS, regulatory feeds, external datasets, and jurisdiction-to-jurisdiction exchanges.

- Transformations: authentication, timestamping, normalization, unit conversion, classification, quality scoring, confidence assignment, deduplication, lineage capture, and privacy/access labeling.

- Outputs: immutable Evidence/Observation objects, derived indicators, alerts, candidate model updates, and provenance links.

- Controls: source authority, data quality thresholds, privacy policy, retention, validation, anomaly detection, and separation of raw observations from derived inference.

- Exception behavior: contested, low-confidence, contradictory, or stale evidence is preserved as such and cannot silently become a hard normative constraint.

## 16.2 Model

Model constructs the explicit civic state used for deliberation, planning, optimization, execution, and learning. The model is not presumed to be reality; it is a versioned, evidence-linked representation of the conditions and relationships relevant to a decision.

- Inputs: evidence, approved objectives, constraints, resources, portfolio structure, schedules, relationships, authority, risk assumptions, and jurisdictional agreements.

- Transformations: hierarchy construction, graph linking, PPM coefficient assignment, constraint compilation, state estimation, scenario construction, forecast generation, and solver-ready translation.

- Outputs: current-state snapshots, baseline/forecast states, feasible-space definitions, scenarios, uncertainty descriptions, and model diffs.

- Controls: schema validation, unit compatibility, authority provenance for normative terms, calibration provenance for empirical terms, model versioning, and reproducibility metadata.

- Exception behavior: unresolved semantic conflicts, infeasible models, unsupported coefficients, or missing authority paths are surfaced before commit-eligible analysis.

## 16.3 Deliberate

Deliberate is the human and civic reasoning layer. It combines propositions, evidence, modeled consequences, public expression, alternatives, dissent, and institutional procedure without forcing every issue into a single numerical score.

- Inputs: propositions, evidence, scenarios, alternatives, objective impacts, constraint status, risk, public expressions, expert input, and prior precedent.

- Transformations: structured comparison, amendment, argument mapping, clarification, minority-position capture, conflict-of-interest handling, and generation of decision-ready alternatives.

- Outputs: amended propositions, deliberation records, decision options, unresolved conflicts, conditions of approval, or remand requests.

- Controls: jurisdiction-defined process, notice, participation rights, quorum/threshold rules, recusal, transparency/privacy boundaries, and version locking of the proposition considered.

- Exception behavior: material amendments trigger revalidation; unresolved conflicts may be explicitly preserved and routed rather than concealed.

## 16.4 Decide

Decide converts legitimate authority plus an evaluated proposition into an approved, rejected, delegated, prohibited, or escalated civic action.

- Inputs: deliberation record, approved criteria, authority, delegation envelope, optimization results, alternatives, risk, and constraint status.

- Transformations: authority check, threshold/quorum test, envelope test, feasibility check, conditions check, and disposition recording.

- Outputs: Decision object, baseline authorization, delegated resolution, commitment authorization, rejection, remand, or Exception Proposition.

- Controls: explicit authority path, separation of duties, non-delegable powers, materiality/risk thresholds, hard-constraint enforcement, and deterministic commit gates.

- Exception behavior: no actor or AI may expand its own authority to resolve a conflict.

## 16.5 Remember

Remember makes civic action cumulative rather than episodic. It preserves what was known, what was decided, why, under which rules, and with what result.

- Inputs: evidence snapshots, model versions, deliberation, decision, approvals, solver runs, commitments, execution events, actuals, and variance.

- Transformations: event append, packet assembly, hashing/signing where applicable, indexing, supersession linking, and historical snapshot creation.

- Outputs: Decision Provenance Packets, replayable history, precedents, audit trails, learning datasets, and public records.

- Controls: append orientation, immutability of approved history, retention policy, privacy classification, integrity verification, and exportability.

- Exception behavior: corrections supersede prior records; they do not erase the historical record that informed earlier decisions.

# 17. Governance Plane - Democratic Engine

## 17.1 Functional Purpose

The Governance Plane converts participation by members of a Civic Body into legitimate, versioned public direction. It is responsible for the legitimacy of objectives, constraints, authority, delegation, and changes to the governing process itself. The optimization engine begins only after these elements have a valid authority path.

## 17.2 Functional Actors

| Actor                     | Functional role                                                                                                                        |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Member / citizen          | Express preferences, propose issues, deliberate, vote/consent where authorized, delegate participation, inspect records.               |
| Proposer                  | Creates a formal proposition or amendment and supplies required rationale/evidence.                                                    |
| Facilitator / clerk       | Administers process without acquiring substantive decision authority.                                                                  |
| Representative / delegate | Exercises explicitly delegated participation or decision authority within scope.                                                       |
| Expert / advisor          | Contributes evidence or analysis; expertise alone does not create governance authority.                                                |
| Decision body             | Exercises a jurisdiction-defined collective authority.                                                                                 |
| AI process manager        | Structures submissions, summarizes, detects missing information, explains consequences, and manages workflow within bounded authority. |
| Auditor / observer        | Inspects process, provenance, authority, and outcomes according to access rights.                                                      |

## 17.3 Participation and Expression

ACECOG shall distinguish expression from decision. A preference, comment, petition, ranking, objection, proposal, or delegated instruction becomes governance only through a defined Governance Process.

- Expression objects preserve author/constituency, subject, scope, time, confidence where applicable, privacy choice, and relationship to a proposition.

- The system may support direct vote, ranked choice, consent, objection, liquid/domain delegation, participatory budgeting, juries/sortition, representative decisions, or hybrid procedures as configurable process types.

- No aggregation method is assumed universal. Each Civic Body defines which method applies to which decision class.

- Delegation shall be revocable according to the governing process and shall preserve the chain from principal to delegate to decision.

- Participation metrics may inform legitimacy checks but shall not be conflated with substantive outcome value.

## 17.4 Collective Will Object

Collective Will is a governed output, not an inferred sentiment score. It records the result of an authorized democratic process and becomes a source for Objectives, Constraints, Authorities, Delegation Envelopes, budgets, policies, or constitutional rules.

| Field group                 | Required semantics                                                                                                                                                             |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Question / proposition      | Exact version decided.                                                                                                                                                         |
| Civic scope                 | Who and what the result governs.                                                                                                                                               |
| Process                     | Decision method, eligibility, thresholds, quorum, notice, timing.                                                                                                              |
| Participation               | Eligible population, participating population, delegations, abstentions where relevant.                                                                                        |
| Result                      | Outcome plus minority/dissent positions where process requires.                                                                                                                |
| Authority                   | Constitution/charter/law/process rule authorizing the result.                                                                                                                  |
| In-force state              | Date it takes effect, duration, review/expiry conditions.                                                                                                                            |
| Downstream mapping          | Objectives, constraints, authority, funding, portfolio or rule changes created by the result.                                                                                  |
| Cumulative impact reference | Optional cumulative_impact_ledger_id (per invariant 16 (GOV-CUMULATIVE-001)) recording this result’s contribution to rolling distributional effect on affected constituencies. |

## 17.5 Governance Process as Configurable Civic Logic

Governance Process objects shall define decision classes and their legitimate procedures. This allows ACECOG to scale across jurisdictions without embedding one political theory into code.

- Eligibility: who may initiate, participate, amend, deliberate, decide, observe, or appeal.

- Thresholds: quorum, approval percentage, consent standard, objection threshold, supermajority, or other jurisdiction-defined rule.

- Temporal rules: notice, deliberation windows, cooling-off periods, emergency procedures, expiration and review.

- Delegation rules: permitted domains, depth, revocability, conflict handling, and disclosure. Phase 1 supports single-level, revocable delegation per decision class; transitive chains are deferred. Concentration is disclosed: a delegate holding delegations from more than the larger of 5% of the members eligible for the decision class or 2 members is identified as such on every decision where those delegations count, with eligibility counted at the class's minimum identity tier. A per-class hard cap is available and off by default. A delegation lapses 12 months after its last reconfirmation, with a reminder to the principal 30 days before; a lapsed delegation returns participation to the principal and is recorded. A delegation that lapses during a vote still counts for that vote, which is bound to the rules in force when it opened (8.9). A recused member's delegation does not count on the matter they are recused from (CMP-004). These are Reference Maturity Framework defaults (4.2); a Civic Body may tighten them, and loosening either is a weakening amendment under invariant 21 (GOV-RATCHET-001). (CL-029, CL-064)

- Ballot secrecy: a per-decision-class secret_ballot setting keeps tallies while hiding which member chose what. Reference default: off for official votes of a public body, which the Colorado Open Meetings Law generally requires to be public; available for resident advisory polls (ASR-07; counsel confirms, WBS 3.1.1). (CL-069)

- Amendment rules: what changes force revalidation or restart of deliberation. An amendment that weakens an existing protection — including amendment of this amendment rule itself — requires the harder-path threshold that would govern the change it enables (invariant 21 (GOV-RATCHET-001)); an amendment that strengthens a protection may use the ordinary process.

- Appeal/reconsideration: standing, grounds, authority, timing, and effect on execution.

- Emergency authority: pre-defined scope, duration, reporting, ratification, and automatic sunset.

- Eligibility assurance: the minimum identity assurance tier, and the full-confidence tier for the assurance-sensitive test, for this decision class (23.1.1), per invariant 13 (TRU-ELIG-001). A jurisdiction may permit Provisional identities for low-stakes process types while requiring Documented or Verified identities for binding commitments.

### 17.5.1 Novelty and Variety-Amplification

A fixed approval process (e.g. GML-1’s dual approval) applies equal process weight to a routine, well-precedented decision and a genuinely novel one. By Ashby’s Law of Requisite Variety, a regulator whose variety does not scale with the variety of situations it faces will eventually fail on the cases it wasn’t built to handle — and a uniform approval process is a regulator of fixed variety. Materiality thresholds (5.11, invariant 16 (GOV-CUMULATIVE-001)) escalate on *magnitude*; nothing escalates on *novelty* alone, even though an unprecedented decision of modest magnitude can be exactly the case a fixed process is least equipped to catch.

- A candidate decision’s precedent similarity is assessed against prior committed Decision Provenance Packets (9). A Civic Body configures its own novelty threshold as part of its Governance Process (17.5) or Maturity Framework (4.3).

- A decision falling below that threshold triggers a variety-amplification step before approval can proceed: mandatory Expert/advisor (17.2) consultation, an extended deliberation window, or both — growing the regulator’s effective variety for this decision rather than merely narrowing what is allowed through (attenuation, GML-1’s existing approach).

- This applies regardless of whether the decision’s materiality independently crosses an Exception Proposition threshold; novelty and magnitude are independent triggers and either alone is sufficient.

<!-- -->

- This is a Reference Maturity Framework control at GML-1 and above (GOV-VARIETY-001, an Invariant Floor entry through v0.19). A self-defined framework (4.3) may replace it with another variety-amplification mechanism, stated in its interoperability declaration.

## 17.6 Governance-to-Optimization Contract

*Collective Will -\> {Objectives, Constraints, Authority, Delegation, Risk Appetite, Time Horizon}*

The Governance Plane shall emit machine-readable, versioned parameters rather than informal instructions. Where a civic decision cannot be translated unambiguously into executable parameters, it remains pending clarification or is represented as a qualitative condition requiring human review.

## 17.7 Democratic Engine Exceptions

- Insufficient participation or quorum.

- Conflicting authorities or overlapping jurisdictions.

- Material amendment after notice.

- Unresolvable ambiguity in proposition wording.

- Conflict between a new proposition and a non-amendable/higher-precedence constraint.

- Delegation loop, expired delegation, or delegate conflict.

- Evidence integrity or identity challenge.

- Emergency action exceeding its sunset or ratification window.

## 17.8 Governance Acceptance Criteria

1.  The exact proposition decided can always be reconstructed.

2.  Eligibility, process, authority, and thresholds are machine-checkable.

3.  Expressions and deliberation remain distinguishable from binding decisions.

4.  Delegation chains are visible, bounded, and revocable according to process.

5.  Delegation concentration above the disclosure threshold is shown on every decision it affects, and delegations not reconfirmed in time lapse back to their principals.

6.  Minority/dissent records can be preserved without changing the formal result.

7.  Every binding governance result maps to explicit downstream objects or remains explicitly non-executable.

8.  A governance-process change is itself governed by the authority required to change that process.

9.  Every founding or restoration of an office traces to a Continuity Case with a recorded authority basis, an independent verification, and a sunset (17.9).

## 17.9 Civic Authority Continuity

Any continuity office may start the legitimate reconstitution of another, but none may take its place, and every step ends on a fixed date. This section resolves CL-044: it supplies the authority for founding a Civic Body before any Governance Process exists, and for restoring self-governance when an office is absent, vacant, incapacitated, or compromised. It replaces any standing founding or administrative power over governance (22.5.3).

**Principles.**

1.  Reciprocal procedural recovery, never reciprocal sovereign authority.

2.  Authority derives from constituent consent, recognized custom, an adopted charter, or applicable law, and each step records which.

3.  No self-appointment, self-certification, unilateral succession, or permanent emergency authority.

4.  Independent verification, transparent participation, bounded mandates, automatic sunsets, and immutable provenance.

5.  Institutional forms are configurable. No hierarchy or culturally specific office is mandatory.

6.  If every authority path fails, the system helps people reconstitute; it never invents authority.

### 17.9.1 The Continuity Offices

| Office               | What it is                                       | Where its authority comes from                                  | Typical selection                                                                                                             |
|----------------------|--------------------------------------------------|-----------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Justice of the Peace | One civic officer for process; no judicial power | The charter, or a constituent election                          | Elected or chosen by lot, fixed term, recallable                                                                              |
| Elders Council       | A body recognized for standing and memory        | Recognized custom or the charter                                | As custom or charter defines; acts by quorum                                                                                  |
| External Convener    | A neutral outside party with no stake            | Law, a court order, a Federation Contract, or a member petition | Designated case by case: a neighboring Civic Body's Justice of the Peace, a court-appointed official, or a registered neutral |

A Civic Body configures which offices it has, under any local names; "Justice of the Peace" is the reference name only. At GML-0 the External Convener path alone is enough; from GML-1, at least two independent paths are configured. The External Convener path is always available through law or member petition, so no Civic Body is ever without a path.

**Powers: process only.** A continuity office acting on a Continuity Case may issue a warrant convening a founding assembly, a selection, or an election; open and publish the eligibility roll from the identity register (23.1.1); adopt interim procedural rules needed only to run that process; and request independent verification of the result. It may not adopt substantive policy, spend beyond a capped continuity reserve, amend the substance of a Governance Process, act under a Delegation Envelope, certify its own result, or appoint itself or another continuity office.

### 17.9.2 Authority Graph and Triggers

| Initiator                   | Justice of the Peace | Elders Council | Governance Process and its offices | Founding assembly |
|-----------------------------|----------------------|----------------|------------------------------------|-------------------|
| Justice of the Peace        | Never                | Yes            | Yes                                | Yes               |
| Elders Council              | Yes                  | Never          | Yes                                | Yes               |
| External Convener           | Yes                  | Yes            | Yes                                | Yes               |
| Member petition             | Yes                  | Yes            | Yes                                | Yes               |
| The system (detection only) | Opens a case         | Opens a case   | Opens a case                       | Never             |

No office may start its own reconstitution. The External Convener is designated from outside, case by case, and is never reconstituted by the offices it may convene.

A Continuity Case opens on one of four conditions, each with evidence: **Absent** (never constituted; founding is this case), **Vacant** (term expired, resignation, or death), **Incapacitated** (quorum failed at 3 consecutive scheduled sessions, or no decision possible for 90 days), or **Compromised** (an independent verifier finds capture, fraud, or a disqualifying conflict, or a court so orders). The system may detect the first three and open a case automatically, but never declares one. A case is raised by a continuity office, a member petition (5% of eligible members or 25 members, whichever is fewer), or a court order.

### 17.9.3 Continuity Case States

Main path: Detected → Raised → Verified → Convened → Rolled → Selected → Certified → Restored.

| State     | What happens                                                                            | Next                                           |
|-----------|-----------------------------------------------------------------------------------------|------------------------------------------------|
| Detected  | The system notices a trigger condition and notifies members and the configured offices  | Raised, or closes after 30 days with no action |
| Raised    | An eligible initiator raises the case, with evidence                                    | Verified or Rejected                           |
| Verified  | An independent verifier (not the initiator or a candidate) confirms the trigger         | Convened                                       |
| Convened  | The initiator issues the warrant: what is reconstituted, how, when, and the sunset date | Rolled                                         |
| Rolled    | The eligibility roll is published and open to challenge                                 | Selected                                       |
| Selected  | The assembly, selection, or election is held                                            | Certified or Contested                         |
| Contested | An appeal is heard by a body other than the initiator                                   | Selected (rerun) or Certified                  |
| Certified | A verifier distinct from the initiator certifies the result                             | Restored                                       |
| Restored  | The new office takes effect; the continuity mandate ends                                | Closed                                         |
| Lapsed    | The sunset date passes without restoration                                              | The next authority path takes over             |
| Stalled   | Every configured path has lapsed or is compromised                                      | Facilitated reconstitution                     |
| Rejected  | The trigger is not verified                                                             | Closed, with reasons recorded                  |

### 17.9.4 Safeguards

1.  No self-dealing: the initiator may not be a candidate in its own case, and no office certifies its own result.

2.  Bounded mandates: each case has a sunset date, by default 90 days, extendable once by member petition.

3.  No mutual reseating: an office reconstituted on another's initiative may not start that office's reconstitution for 12 months, unless an independent verifier finds compromise.

4.  Transparency: every step is public, carries its authority basis, and is recorded in provenance.

5.  AI boundary: the assistant may draft notices and summaries, but never raises, verifies, decides, or certifies (invariant 15 (AI-NEUTRAL-001)).

6.  No fees: petitioning, challenging the roll, and taking part cost nothing (invariant 24 (TRU-ACCESS-001)).

7.  Facilitated reconstitution: when every path has failed, the system publishes the case's status and enables a petition-driven founding assembly with external observers. Its result is labeled "reconstituted, recognition pending" until a law, court, charter, or federation partner recognizes it, and it cannot drive a commitment until then. The system never confers recognition itself.

### 17.9.5 Traceability and Acceptance Tests

| Requirement                                                              | Invariant                                  |
|--------------------------------------------------------------------------|--------------------------------------------|
| Every step records its authority basis: consent, custom, charter, or law | 2 (GOV-AUTHPATH-001)                       |
| No self-appointment; terms, rotation, and recall                         | 17 (TRU-MONITOR-001)                       |
| The roll counts each person once and labels assurance-sensitive results  | 13 (TRU-ELIG-001)                          |
| Case history is append-only and replayable                               | 1 (DPP-IMMUTABLE-001), 11 (DPP-REPLAY-001) |
| No fee to petition, challenge, or take part                              | 24 (TRU-ACCESS-001)                        |
| The AI never decides or certifies                                        | 15 (AI-NEUTRAL-001)                        |
| Compliance Packs may add legal conditions but never remove a safeguard   | 19 (GOV-FRAMEWORK-001)                     |

- **CONT-AT-01** A founding (Absent) case convened by an External Convener produces a Governance Process, and the convener holds no authority after Restored.

- **CONT-AT-02** An office attempting to start its own reconstitution, or to certify its own result, is refused.

- **CONT-AT-03** The system detects 3 consecutive quorum failures and opens a case in Detected, but cannot move it to Raised.

- **CONT-AT-04** A case past its sunset date moves to Lapsed, and every act under its warrant is refused afterward.

- **CONT-AT-05** A mutual-reseating attempt within 12 months, without a compromise finding, is refused.

- **CONT-AT-06** A warrant that tries to adopt substantive policy or spend beyond the continuity reserve is refused.

- **CONT-AT-07** An assistant-originated attempt to raise, verify, or certify a case is refused.

- **CONT-AT-08** With every path lapsed, the facilitated assembly's result carries "reconstituted, recognition pending" and cannot drive a commitment.

- **CONT-AT-09** The full case replays from provenance with an identical outcome.

**Open legal questions (to add to 43.8).** Whether the title "Justice of the Peace" misleads where the judicial office no longer exists (Colorado replaced its justice-of-the-peace courts with county courts in the 1960s; to confirm); who may lawfully call a public body's meeting; legal recognition of an Elders Council outside tribal nations (for a tribal nation, ACECOG defers entirely to its own law and custom); whether a continuity election for a public office falls under election law; open-meetings coverage of the continuity assembly; liability of conveners and verifiers; key escrow when a compromised party controls the installation (invariant 12 (TRU-EXIT-001)); the appeal venue for a Contested case; and funding of the continuity reserve.

# 18. Planning & Optimization Plane - Detailed Functional Analysis

## 18.1 Portfolio Construction

The Planning & Optimization Plane translates public direction into a structured portfolio of outcomes, programs, projects, services, resources, and relationships. The hierarchy is a management view; the relationship graph is the systems view.

- A Portfolio Node has one structural parent but may have many cross-tree relationships.

- Objectives may be satisfied by multiple nodes; nodes may contribute to multiple objectives.

- Resources may be shared, substituted, reserved, transferred, replenished, or geographically/time constrained.

- Every normative coefficient or constraint must have an authority path; every empirical coefficient must have evidence/calibration provenance.

## 18.2 Optimization Problem Assembly

1.  Select decision scope and immutable input snapshot.

2.  Resolve applicable jurisdictional and treaty scopes.

3.  Compile mandatory and threshold objectives.

4.  Compile hard/soft constraints with precedence and relaxation policy.

5.  Map resources, balances, eligibility, time windows, and capacities.

6.  Compile portfolio relationships into linear, quadratic, logical, temporal, or scenario terms.

7.  Select approved objective hierarchy and optimization method.

8.  Run feasibility pre-check.

9.  Solve and verify numerical/constraint integrity.

10. Publish recommended state, alternatives, marginal values, sensitivity, risks, and governance consequence.

## 18.3 Solver Family Selection

Phase 1 uses LP and the convex QP form of 5.3 (maximize cᵀx − ½xᵀQx, Q positive semidefinite). The families below beyond that profile are interface only until Phase 1.5 (13.6).

| Problem characteristic                               | Preferred method                                        | Governance implication                                                                           |
|------------------------------------------------------|---------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| Linear continuous allocation                         | LP / simplex or interior-point                          | Highly explainable shadow prices and binding constraints.                                        |
| Pairwise nonlinear interactions                      | QP where convex/appropriate                             | PPM Q terms express synergy/competition; convexity and local/global properties must be reported. |
| Discrete project choices / logical gates             | MILP                                                    | Binary choices and minimum/maximum commitments become explicit.                                  |
| Multiple non-compensable priorities                  | Lexicographic / epsilon-constraint / hierarchical solve | Preserves objective precedence rather than hiding tradeoffs in one weight.                       |
| Uncertain inputs                                     | Scenario / stochastic / robust optimization             | Risk assumptions and distributions become governed model inputs.                                 |
| Strategic interaction among autonomous jurisdictions | Game-theoretic or negotiated equilibrium analysis       | Used as analysis; does not override each jurisdiction's authority.                               |
| Sequential uncertain choices                         | Decision analysis / decision trees / dynamic methods    | Clarifies option value, information value, and staged commitments.                               |

## 18.4 Objective Functions and Public Value

ACECOG shall support weighted utility where appropriate, but shall not require all public value to be collapsed into a single score. The preferred structure is hierarchical: mandatory boundaries, threshold sufficiency, priority optimization, then efficiency.

- Weights and utility curves are versioned governance parameters.

- Non-compensable objectives are never traded for gains elsewhere.

- Threshold objectives may cease adding priority after sufficiency is achieved.

- Diminishing returns may be represented explicitly.

- Distributional outcomes may be modeled separately from aggregate outcomes.

- Intergenerational and ecological effects may use long horizons and explicit discounting policy rather than hidden defaults.

## 18.5 Constraint Propagation Algorithm

1.  Identify originating constraint and scope.

2.  Apply precedence and inheritance mode.

3.  Propagate downward to affected descendants or allocate sub-envelopes.

4.  Aggregate child effects upward using the declared aggregation function.

5.  Apply cross-tree and cross-jurisdiction coupling.

6.  Detect contradictory or infeasible combinations.

7.  Return binding constraints and source authority in every material result.

## 18.6 Sensitivity and Marginal Analysis

- Report marginal objective change for scarce resources where mathematically valid.

- Report shadow prices/dual values for binding linear constraints where meaningful.

- Test sensitivity to weights, thresholds, coefficients, resource availability, and uncertain assumptions.

- Identify decision-stable regions where recommendations do not change under plausible parameter variation.

- Flag fragile recommendations whose ranking changes under small plausible changes.

- Sensitivity outputs are explanatory evidence, not permission to change governed parameters.

## 18.7 Game and Decision Theory

Game theory is used where multiple autonomous actors have strategic choices; decision theory is used where a decision maker faces uncertainty, staged information, or asymmetric consequences. Both are analytical methods subordinate to governance.

- Model actors, strategies, payoffs/objectives, information assumptions, and enforceable commitments explicitly.

- Use cooperative analysis for shared-resource or treaty opportunities; use non-cooperative analysis to expose incentives and instability.

- Where no stable cooperative solution exists, generate governance options such as side payments, shared funding, changed constraints, or revised agreement terms.

- Decision analysis may calculate expected utility, regret, value of information, and option value when authorized criteria exist.

- The system shall expose assumptions rather than present equilibrium or expected value as destiny.

## 18.8 Optimization Outputs

| Output                  | Required content                                                                    |
|-------------------------|-------------------------------------------------------------------------------------|
| Recommended State       | x\*, allocations, activated choices, schedule/resource implications.                |
| Feasibility Statement   | Satisfied, binding, violated, uncertain constraints and authority source.           |
| Marginal Allocation Map | Where additional scarce resource produces highest authorized marginal value.        |
| Interaction Map         | Material synergies, conflicts, dependencies, substitutions, externalities.          |
| Alternative Set         | Near-optimal or materially distinct feasible alternatives.                          |
| Sensitivity Report      | Parameters that materially change result and stability ranges.                      |
| Governance Consequence  | Executable, delegated, reviewable, escalated, prohibited.                           |
| Provenance              | Snapshot, model, solver, version, configuration, authority and evidence references. |

# 19. Execution Plane - Detailed Functional Analysis

## 19.1 Purpose

The Execution Plane converts approved portfolio states into coordinated commitments, schedules, work, services, asset operations, and resource flows while preserving the distinction between planned, committed, executed, and actual states.

## 19.2 Work Breakdown and Dependency Semantics

- Portfolio -\> Program -\> Project -\> Work Package -\> Activity/Task is the default execution hierarchy.

- Dependencies include finish-start, start-start, finish-finish, start-finish, logical gates, external approvals, resource gates, and jurisdictional/treaty gates.

- Dependencies may be hard, soft/preferred, conditional, or evidence-triggered.

- Every dependency has source, owner, status, and effect if violated.

## 19.3 CPM and Schedule Control

- Compute earliest/latest dates, total/free float, critical and near-critical paths.

- Support calendars, windows, milestone constraints, and external dates.

- Recompute path effects after approved changes or observed variance.

- Baseline schedule is immutable; forecast and actual dates are separate.

- Schedule compression or acceleration is treated as an explicit scenario with cost/resource/risk consequences.

## 19.4 Resource Leveling and Capacity

- Resources have availability profiles, calendars, skills/types, location, cost, substitution rules, and ownership.

- The scheduler detects overload, underutilization, bottlenecks, and infeasible commitments.

- Leveling objectives may minimize lateness, peak demand, cost, disruption, or other approved criteria.

- A schedule may not assume a resource transfer across jurisdictional or funding boundaries without an authorized relationship.

## 19.5 Commitment Semantics

Commitment is the civic equivalent of encumbrance/reservation: it changes what remains available to other decisions. Recommendations do not reserve resources; approved commitments do.

- Commitments may be financial, capacity, labor, asset, entitlement, schedule, land, water, energy, or other governed resources.

- Conditional commitments identify release conditions and expiry.

- Compensating transactions release or reverse commitments without erasing the original record.

- Commit-time checks use current balances and authority, not merely the state that existed at recommendation time.

<!-- -->

- Every resource commitment (funds, crews, stocks, capacity) is registered once and referenced by all modules; the same resource cannot be promised twice (RES-REGISTRY-001, an Invariant Floor entry through v0.19).

## 19.6 External Execution Boundary

ACECOG may execute directly or through adapters to operational systems. External systems remain systems of record for facts they authoritatively produce unless governance explicitly designates ACECOG otherwise.

- Issued is distinct from acknowledged.

- Acknowledged is distinct from completed.

- Completion requires class-appropriate evidence.

- Execution failure triggers disposition of the commitment and may trigger risk/variance/exception workflows.

- Adapters must be idempotent and reconcile acknowledgements to transaction IDs.

# 20. Evidence Plane - Detailed Functional Analysis

## 20.1 Evidence Classes

| Class                | Examples                                                   | Primary concern                                        |
|----------------------|------------------------------------------------------------|--------------------------------------------------------|
| Transactional        | Payments, commitments, work orders, permits                | Integrity and reconciliation.                          |
| Operational          | Service levels, asset status, throughput                   | Timeliness and system-of-record authority.             |
| Ecological           | Water, air, habitat, climate, land condition               | Calibration, spatial/temporal scale, uncertainty.      |
| Social / civic       | Surveys, participation, demographic aggregates, complaints | Privacy, representativeness, interpretation.           |
| Expert / documentary | Studies, regulations, engineering reports                  | Authority, date, scope, methodology.                   |
| Model-derived        | Forecasts, estimates, inferred indicators                  | Separation from raw evidence and explicit assumptions. |

Evidence also carries an epistemic class (8.0): Observed, Reported, Estimated, Assumed, Scenario output, or Hypothesis. Source class (above) and epistemic class are independent. Models do not establish what will happen; they establish what follows from stated assumptions, evidence, rules, and uncertainty models. Every model output is labeled Scenario output and cites its scenario, model version, and seed.

## 20.2 Provenance Chain

*Source -\> Raw Observation -\> Transformation -\> Derived Measure -\> Model Input -\> Decision Use*

- Each link is separately identifiable and versioned.

- Transformations record code/rule/model version and units.

- Corrections supersede rather than delete.

- Evidence confidence may be multi-dimensional: source reliability, measurement uncertainty, freshness, completeness, representativeness.

- Privacy classification and public transparency classification are separate attributes.

## 20.3 Data Quality Gates

- Validity: value conforms to expected domain/unit.

- Completeness: required fields and coverage exist.

- Timeliness: data is sufficiently current for the decision class.

- Consistency: no unexplained contradiction with authoritative sources.

- Lineage: origin and transformations are traceable.

- Fitness for use: quality threshold is decision-specific rather than universal.

# 21. Learning Plane - Detailed Functional Analysis

## 21.1 Purpose

Learning closes the civic control loop by comparing intended outcomes with observed outcomes and proposing changes to forecasts, empirical models, execution plans, or governance. It shall distinguish learning about the world from changing public values.

## 21.2 Variance Taxonomy

| Variance type       | Question                                                                  | Typical response                                             |
|---------------------|---------------------------------------------------------------------------|--------------------------------------------------------------|
| Execution variance  | Did work occur as planned?                                                | Forecast/rebalance/corrective action.                        |
| Resource variance   | Did cost/capacity/use differ?                                             | Reallocate or revise resource assumptions.                   |
| Outcome variance    | Did the intended public outcome occur?                                    | Benefits analysis; causal review.                            |
| Model variance      | Were predicted relationships wrong?                                       | Recalibrate empirical coefficients.                          |
| Governance variance | Do outcomes reveal that approved priorities/rules should be reconsidered? | Generate proposition for human governance.                   |
| External shock      | Did conditions change outside the model?                                  | Shock scenario, risk update, rebalance or emergency process. |

## 21.3 Model Calibration

- Empirical coefficients may be recalibrated only under an approved calibration policy.

- Training/calibration datasets preserve lineage and exclusions.

- Backtesting compares predictions with actuals and reports error by context.

- A model update is versioned and cannot alter the model that governed a historical decision.

- Normative weights, rights, priorities, and authorities are never automatically learned from outcomes.

## 21.4 Continuous Improvement

*Observe -\> Compare -\> Explain -\> Propose -\> Authorize -\> Update -\> Observe*

This cycle intentionally aligns with quality-management continuous improvement while preserving civic authority over changes that are normative rather than empirical.

# 22. Federation Plane - Detailed Functional Analysis

## 22.1 Federation Principle

Federation permits independent Civic Bodies to coordinate without requiring a central sovereign database or uniform internal governance. A federation interface exposes only the objects, commitments, constraints, evidence, and authorities that participants have agreed to share.

## 22.2 Federation Contract

| Contract element                    | Function                                                                                                                                                                                 |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Participants                        | Identifies sovereign parties.                                                                                                                                                            |
| Shared scope                        | Defines subject/geography/time covered.                                                                                                                                                  |
| Object mappings                     | Maps local semantics to shared canonical semantics.                                                                                                                                      |
| Authority                           | Defines what may bind whom and through which approval path.                                                                                                                              |
| Data policy                         | Defines shared fields, privacy, retention, update frequency.                                                                                                                             |
| Coupling model                      | Defines shared resources, externalities, constraints, and PPM terms.                                                                                                                     |
| Transaction protocol                | Defines proposal, approval, pending, commit, compensation, dispute.                                                                                                                      |
| Exit / amendment                    | Defines withdrawal, version change, sunset, and continuity behavior.                                                                                                                     |
| Externality-exposed objectives      | Declares which O_mandatory (5.7) objectives, per participating jurisdiction, are exposed through this coupling’s cross-block terms; scopes the check in 22.3.                            |
| Maturity framework mapping          | Declares each participating jurisdiction’s Maturity Framework (4.3) and the interoperability- declaration comparison used to establish trust for this specific coupling.                 |
| Documented interdependence basis    | Declares the certified, measured flows (water, sediment, air, fire risk, species, energy, food, visitors) that ground any obligation between Guardian Jurisdictions (FED-SYMBIOSIS-001). |
| Proportional terms and review cycle | Sets transfers and duties in proportion to those flows and the Lifecycle Management cycle on which they are re-certified (41.1).                                                         |

## 22.3 Cross-PPM Stitching

- Local models remain locally owned and versioned.

- Shared models reference exported interface objects rather than silently copying internal authority.

- Cross-block coefficients must state evidence and agreement basis.

- Shared optimization may recommend joint solutions; each jurisdiction retains the approval rights defined by the agreement.

- If one participant changes a binding local constraint, the shared feasible set is revalidated before further commitment.

- Before a joint solution is offered for approval, the coupling engine shall evaluate the externality each cross-block coefficient imposes on every declared externality-exposed O_mandatory objective (22.2) of every participating jurisdiction, and treat a breach identically to a binding local constraint change above: trigger revalidation rather than pass it through as an ordinary efficiency tradeoff (invariant 14 (FED-RIGHTS-001)).

## 22.4 Conflict and Dispute

- Technical merge conflict, semantic disagreement, authority conflict, and substantive policy dispute are distinct classes.

- Technical conflicts may be automatically reconciled only by agreed deterministic rules.

- Semantic conflicts require mapping/clarification.

- Authority conflicts and substantive disputes route to the agreement-defined governance process.

- Federation shall fail closed for binding commitments when required authority cannot be established.

## 22.5 Multi-Tenant Hosting and Trust Tiers

Federation (22.1-22.4) specifies how independent Civic Bodies agree to interoperate. It does not specify where each Civic Body's own instance runs, or how interoperability degrades gracefully when a federation partner cannot be a normal API peer at all. Both become load-bearing questions the moment ACECOG is asked to span a real region rather than a handful of cooperating bodies — e.g., the 9 counties and roughly 100 cities of the San Francisco Bay Area, plus several hundred special districts, state agencies, and federal installations (a reference region; the count is to be refined), all producing their own climate and resilience plans, competing for the same funding, and participating in shared ecosystem-scale efforts. This subsection specifies the hosting and trust-tier model that makes that scale tractable without weakening local sovereignty (non-negotiable principle 4) or the authority boundary (invariant 2 (GOV-AUTHPATH-001)).

### 22.5.1 Two Hosting Models

- Shared multi-tenant regional platform: a regional body (e.g., a metropolitan planning organization or a purpose-formed joint-powers authority) operates one deployment; each participating Civic Body is an isolated tenant (a separate schema or database per tenant, not row-level filtering alone, so a tenant-isolation defect cannot leak one jurisdiction's deliberations into another's). This is the only practical on-ramp for the majority of small jurisdictions — special districts, small cities, joint-powers authorities — that have no capacity to operate their own server. A shared platform carries operator certification obligations from its first production tenant (43.3) and the operator-conduct rules of 43.6.

- Self-hosted sovereign instance: a Civic Body runs its own deployment inside its own network boundary, on its own cloud tenancy or physical hardware. This is the only viable model for defense and national-security installations, which will not place planning data — however unclassified — on a third party's infrastructure, and is frequently the preferred model for larger, better-resourced bodies (counties, state agencies) for the same local-sovereignty reasons already codified in non-negotiable principle 4.

- Public demonstration deployment (CL-081): an operator-hosted instance that lets the public see and try ACECOG on synthetic Civic Bodies. It holds no real jurisdiction's records and no real identities; every decision is labelled Advisory and Legal Effect Declarations are disabled; visitors act only through demonstration role grants issued by the demonstration body's own Governance Process, in isolated sandboxes; the AI boundary (24.3) applies unchanged. It is not a production tenancy, so the certification prerequisites for the first production tenant (13.1, 43.3) don't apply to it, and no authority, credential or record moves from it to a civic deployment. Its published capability manifest states, for every capability, whether it is built, tested and exposed.

The civic-state export package (Section 15, invariant 12 (TRU-EXIT-001), MVP acceptance test 110) is what keeps the choice between these two models non-binding: any tenant on the shared platform can export its full civic state and stand up a self-hosted instance later without any code change, and vice versa. Hosting location is a deployment decision; it is never a governance one.

### 22.5.2 Three Federation Trust Tiers

Cross-PPM Stitching (22.3) assumes two federation partners that mutually trust each other and can reach each other's live API. That assumption holds for most jurisdictions but not all of them, so federation is specified as three trust tiers rather than one mechanism applied uniformly.

- Tier A — Live API federation: the existing Cross-PPM Stitch, read-only observation mode (30.6) or joint-solve mode, between Civic Bodies with mutual trust and reachable networks. This is the default tier and covers most municipal, county, and special-district partners.

- Tier B — Scheduled batch exchange: periodic exchange of civic-state export bundles (Section 15) rather than a live API connection, for partners behind stricter network boundaries or on an infrequent synchronization cadence (e.g., some state agencies).

- Tier C — One-way sanitized push: a federation partner that will not accept any inbound connection and will not participate as a normal federation peer (defense and national-security installations are the paradigm case) may still periodically publish a declassified, sanitized subset of its own planning posture downstream as an ordinary Evidence feed (Section 20). A Tier C partner never receives a Proposition back through this channel and is never counted toward another Civic Body's eligible or participating population; the channel is one-directional by construction, not by unenforced convention.

A Federation Contract (22.2) shall declare which trust tier governs each direction of a given relationship; a Tier B or Tier C designation is not a degraded Tier A relationship but a distinct, explicitly bounded one.

### 22.5.3 Local Administrator Scope

Every Civic Body, regardless of which hosting model it uses, has a local administrator: an Actor holding technical administration authority scoped strictly to that Civic Body's own object_id. The local administrator installs and maintains the installation, runs backups and exports, and manages accounts and credentials as the Governance Process and registrars direct. It holds no power over the Governance Process, Delegation Envelopes, or Federation Contracts; those change only through the Governance Process (17.5, invariant 21 (GOV-RATCHET-001)), and founding or restoring governance belongs to the continuity offices (17.9). Technical administrator privilege never implies civic decision authority (23.1). (CL-053)

On a shared multi-tenant platform, this creates a second axis that invariant 6 (FED-AUTH-001) (no cross-jurisdiction binding effect without explicit authority) does not by itself cover: the relationship between a tenant and the platform operator, rather than between two federated Civic Bodies. A platform operator can provision and de-provision tenants and operate the underlying infrastructure, but that operational role is not itself a governance Authority, and confers none. This is made explicit as invariant 23 (TRU-TENANT-001):

A shared-hosting platform operator holds no standing Authority (Section 7) into any tenant Civic Body's Governance Process; every authority and Delegation Envelope check that applies to a self-hosted Civic Body applies identically to one hosted on a shared platform, and no operational or infrastructure role may substitute for, or bypass, that check. (TRU-TENANT-001)

### 22.5.4 New or Clarified Requirements

- Tenant isolation is a deployment-level requirement on the shared multi-tenant hosting model (22.5.1): per-tenant schema or database separation, not row-level access control alone, is the minimum bar for a conforming shared deployment.

- Each Civic Body has its own hash chain (ASR-04); an export carries only that body's chain and verifies without any other tenant's records (CL-068).

- Federation Contract (22.2) gains a trust_tier field per direction of the relationship (Tier A, B, or C, per 22.5.2), so a Tier C partner's one-directional, non-authoritative status is explicit in the contract itself rather than inferred from its absence of API access.

- A Civic Body's federation interoperability declaration (invariants 19 (GOV-FRAMEWORK-001) and 22 (FED-EDITION-001)) shall additionally state its own hosting model (shared-tenant or self-hosted) and, if shared, the operating platform — the same visibility principle already required for floor edition and Maturity Framework mapping, extended to hosting.

### 22.5.5 Acceptance Criteria (FED-HOST-001..005)

- FED-HOST-001. Provision two tenant Civic Bodies on a shared multi-tenant platform and confirm each tenant's objects, Actors, and Governance Process are stored in isolated schemas/databases inaccessible to the other tenant's queries.

- FED-HOST-002. Confirm a platform-operator-level credential, absent any Authority object scoped to a specific tenant Civic Body, is refused by require_authority/check_delegation_envelope identically to any other unauthorized caller (TRU-TENANT-001).

- FED-HOST-003. Export a shared-platform tenant's full civic state and reconstruct it as a self-hosted instance from the export bundle alone, with no code change (mirrors MVP acceptance test 110).

- FED-HOST-004. Establish a Tier C federation relationship, confirm the receiving Civic Body can ingest the partner's published Evidence feed, and confirm the Tier C partner is excluded from that Civic Body's eligible/participating population counts and cannot receive a routed Proposition.

- FED-HOST-005. Confirm a Civic Body's federation interoperability declaration displays its hosting model and, for a shared-tenant Civic Body, its operating platform.

# 23. Civic Trust Plane - Detailed Functional Analysis

## 23.1 Identity, Role, and Authority

*Authentication != Authorization != Governance Legitimacy*

- Identity answers who/what is acting.

- Role answers in what organizational function.

- Authority answers what the actor may legitimately do.

- Delegation answers which subset may be exercised by another actor/agent and under what conditions.

- Technical administrator privilege shall not imply civic decision authority.

### 23.1.1 Identity Onboarding and Uniqueness Assurance

ACECOG separates **uniqueness** (this identity belongs to one real person, who holds no other identity in scope) from **standing** (this person may take part in this Civic Body under its charter). The **ACECOG Identity** answers the first. The **Membership Credential** (Section 7) answers the second, and is issued only to an identity. This subsection refines invariant 24 (TRU-ACCESS-001) without weakening it (CL-047, CL-028).

**Principles.**

1.  Anyone can start. An ACECOG Identity is issued the same day, at no cost, with or without documents (invariant 24).

2.  Evidence accumulates; it does not gate. Each identity carries whatever uniqueness evidence exists for that person (assurance anchors), and its assurance tier rises as anchors are added.

3.  Uniqueness is proven against the register, not the person. An anchor counts only after it has been checked against every other identity in scope and found unused.

4.  Duplicates are merged, not punished. Reconciliation counts a person once and never suspends their participation.

5.  The system keeps proofs, not documents. Documents are checked and then discarded unless law requires retention.

**Assurance anchors and tiers.**

| Anchor                                                                                                              | What it proves                                             | How it is checked                                             | Tier it supports |
|---------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|---------------------------------------------------------------|------------------|
| Self-assertion (name, contact, residence claim)                                                                     | Nothing about uniqueness                                   | Recorded as given                                             | Provisional      |
| Device passkey                                                                                                      | The same holder is returning, not uniqueness               | Cryptographic sign-in                                         | None on its own  |
| In-person vouching by two members at Documented or above                                                            | A real local person known to them                          | Vouching limits and ring check                                | Vouched          |
| Document check: government, tribal, or consular ID; voter registration; lease or utility record for residence       | Uniqueness through the document's own identifier           | Keyed-hash match against the register                         | Documented       |
| In-person verification by an authorized registrar with document inspection, or a match to an authoritative register | Uniqueness with a named official accountable for the check | Registrar attestation, recorded with the registrar's identity | Verified         |

Tiers rise in order: Provisional, Vouched, Documented, Verified. Vouched is reachable with no document at all, so no tier above Provisional requires a government ID. Each decision class sets its minimum tier and its full-confidence tier as Governance Process configuration (17.5). Reference Maturity Framework defaults: comment and advisory polls, Provisional; propositions and ordinary votes, Vouched; binding allocations, monitoring-role selection, and Governance Process amendments, Documented; registrars and monitoring-role holders, Verified. The default full-confidence tier is Documented.

**The uniqueness check.** Each anchor is reduced to a normalized identifier (for example, document type, issuer, and number) and stored only as a keyed hash; the Civic Body holds the key (ASR-03, ASR-07). A new anchor is matched against every anchor hash in scope, and a match opens a Reconciliation Case instead of adding the anchor. Raw document images and numbers are discarded after the check unless the adopted Compliance Pack requires retention. Matching across Civic Bodies happens only under a Federation Contract (22.2).

**Vouching limits.** A member may vouch for at most 5 identities in any 12 months, and only in person. Identities vouched for only by each other (a closed ring) stay at Provisional. If an identity a member vouched for is later merged as a duplicate, that member's vouching pauses pending review under the graduated ladder (5.11.1); their own participation is never affected.

**Reconciliation.** When two identities prove to be one person:

1.  They merge into the earlier identity, which takes the higher of the two tiers.

2.  Every decision in which both identities took part is recounted with one vote: the earlier one cast.

3.  If a recount changes an outcome, the change is an outcome-changing reconciliation. It is recorded in the Decision Provenance Packet and routed as an Exception Proposition to the authority that closed the decision.

4.  The person keeps participating throughout. Deliberate duplication is handled under graduated sanctions (invariant 18 (GOV-GRADUATED-001)), never by exclusion.

**Assurance-sensitive results.** When a decision closes, the system compares the margin (votes separating the result from the next outcome, and the surplus above quorum) with the at-risk count: counted participants below the decision class's full-confidence tier, plus any in an open Reconciliation Case. If the at-risk count is at least the margin, or removing it would drop participation below quorum, the result is labeled assurance-sensitive, on the result and in provenance. At GML-2 and above, an assurance-sensitive result cannot drive a commitment until enough at-risk participants upgrade or reconcile that the margin is safe, or the closing authority confirms it after a 14-day verification window. For example, a vote passing 9 to 6 (margin 3) with 4 Provisional participants is assurance-sensitive; if 2 of the 4 upgrade to Documented, it clears.

## 23.2 Transparency and Privacy

ACECOG shall maximize inspectability of public reasoning while minimizing unnecessary exposure of personal data. Transparency applies most strongly to rules, public objectives, model logic, authority, public expenditures, aggregate outcomes, and material decision provenance; privacy applies to personal identity/data according to purpose and law. Compliance-specific privacy and records controls (ASR-05, ASR-07) and jurisdiction records obligations (43.4) are specified in Section 43.

## 23.3 Sovereignty and Exit

- Civic state shall use durable, documented export formats.

- Export includes governance rules, objectives, constraints, authorities, delegations, portfolio/model state, decisions, provenance, and operational records needed for continuity.

- Cryptographic or platform-specific integrity mechanisms shall have documented verification/export paths.

- A hosting or software provider cannot block lawful civic exit by withholding proprietary state semantics.

- Forking preserves lineage so a successor system can show where governance histories diverged.

## 23.4 Security Model

- Least privilege and separation of duties.

- Tamper-evident event history and signed high-consequence actions where appropriate.

- Key/credential rotation and revocation.

- Recovery from compromised actors, hosts, or adapters without rewriting history.

- Threat modeling for insider misuse, identity compromise, model manipulation, data poisoning, replay, double commitment, federation spoofing, and AI prompt/instruction attacks.

- Public audit interfaces shall not expose secrets required for system security or personal privacy.

<!-- -->

- The mandatory Assurance Controls (43.2) and the operator certification roadmap and shared-responsibility matrix (43.3) implement this model for compliance and audit.

# 24. AI Process Manager - Detailed Functional Analysis

## 24.1 Functional Role

The AI process manager is a conversational and analytical interface over governed civic state. It may help participants understand, structure, compare, navigate, and document civic processes, but all state-changing capability is mediated by explicit tools, permissions, validation, and transaction semantics.

## 24.2 AI Task Classes

| Class      | Examples                                                                                 | Default authority                               |
|------------|------------------------------------------------------------------------------------------|-------------------------------------------------|
| Explain    | Explain a rule, model output, constraint, budget, decision history.                      | Read only.                                      |
| Structure  | Convert natural language into draft objectives, constraints, proposals, work breakdowns. | Draft only.                                     |
| Analyze    | Compare alternatives, summarize evidence, identify conflicts, run approved models.       | Analytical; no commitment.                      |
| Coordinate | Route tasks, request missing information, monitor deadlines, assemble packets.           | Workflow actions within role.                   |
| Recommend  | Generate decision or rebalance recommendations.                                          | Recommendation only.                            |
| Execute    | Perform a bounded rote action.                                                           | Only under explicit active Delegation Envelope. |

Explain-class tasks that describe model or simulator outputs count as influencing tasks under invariant 15 (AI-NEUTRAL-001): they carry the output’s epistemic class (8.0) and never present a conditional model output as a prediction.

Structure and Analyze outputs feeding a material Governance Process shall apply the same structural template and comparable word-budget across competing propositions in the same decision; any AI-introduced language, emphasis, or ordering beyond direct transcription is flagged as an AI transformation and held available for side-by-side comparison against the original human input (invariant 15 (AI-NEUTRAL-001)).

## 24.3 AI-to-Commit Boundary

1.  User/agent intent is converted into a structured candidate transaction.

2.  The candidate is shown or otherwise made reviewable according to decision class.

3.  Deterministic validation resolves schema, authority, constraints, balances, and envelope.

4.  If human approval is required, AI cannot substitute its own approval.

5.  The orchestrator commits the authorized transaction; the AI never writes around the commit path.

6.  The resulting transaction and AI transformation metadata enter provenance.

**AI-edit flag (CL-056).** Any change the assistant introduces into human-authored text is marked as AI-introduced, and a side-by-side view of the human and AI versions is available to the author and every reviewer before a material decision (invariant 15 (AI-NEUTRAL-001), INV-AT-15).

## 24.4 Model Independence

- Core civic state and rules are stored outside the language model.

- Prompts are not governance records unless explicitly captured as evidence or transaction context.

- AI provider/model may be replaced without changing civic authority semantics.

- High-consequence structured transformations should be testable against deterministic validators.

- AI uncertainty shall not be hidden behind fluent language.

- Prompts and drafting sessions for any Structure or Analyze task feeding a decision at or above the Civic Body’s GML-defined materiality threshold are mandatory evidence records, not optional captures — closing the gap where AI-shaped framing of a material decision would otherwise leave no reconstructable trace.

# 25. Cross-Plane Functional Traces

## 25.1 Participatory Capital Allocation

1.  Members submit and refine proposals in the Governance Plane.

2.  Evidence Plane validates cost, need, location, asset, ecological, and community data.

3.  Governance adopts objectives, eligibility constraints, budget envelope, and decision method.

4.  Planning Plane maps candidate projects to objectives/resources and solves feasible portfolio alternatives.

5.  Deliberation reviews alternatives, tradeoffs, distributional effects, and dissent.

6.  Decision establishes the baseline portfolio and delegation tolerances.

7.  Execution commits funding/capacity and schedules approved work.

8.  Evidence posts actual cost, schedule, and outcome observations.

9.  Learning compares expected and realized benefits and proposes empirical or governance changes.

10. Remember preserves the complete provenance and supports replay.

## 25.2 Routine Resource Rebalance

1.  Actuals show one program under-consuming a fungible resource while another faces a forecast shortage.

2.  The model recalculates marginal value and feasibility.

3.  A candidate transfer remains within funding eligibility, hard constraints, risk, and delegated tolerance.

4.  The Delegation Envelope test passes.

5.  ACECOG records a Delegated Resolution and commitment adjustment.

6.  Affected parties are notified according to policy; no new public vote is required.

7.  The rebalance and subsequent outcome remain fully traceable.

## 25.3 Forced Governance Escalation

1.  A drought observation reduces the available water resource below the existing portfolio requirement.

2.  The updated model becomes infeasible under current service thresholds and ecological constraints.

3.  The optimizer identifies the binding constraints and feasible relaxation alternatives.

4.  Because the required tradeoff exceeds delegated authority, an Exception Proposition is generated.

5.  The Governance Plane deliberates among service reduction, new supply, emergency funding, changed timing, or other lawful alternatives.

6.  The authorized decision creates a new versioned constraint/objective/baseline state.

7.  Execution and monitoring continue under the new state without rewriting the prior decision history.

## 25.4 Multi-Jurisdiction Shared Resource

1.  Two or more jurisdictions publish agreement-authorized interface models for a shared watershed, corridor, grid, or other resource.

2.  The Federation Plane composes local constraints and shared coupling terms.

3.  The optimizer identifies joint feasible alternatives and distributional effects.

4.  Each jurisdiction applies its own required approval process plus any shared agreement process.

5.  Commitment occurs only after all binding authority conditions are satisfied.

6.  Actual use and outcomes reconcile to the shared resource model and local systems.

7.  Disputes route according to the agreement rather than to a presumed central ACECOG sovereign.

# 26. Detailed MVP Functional Slice

The MVP should implement a thin vertical slice through every essential plane rather than a deep implementation of only optimization. The objective is to prove legitimacy, traceability, bounded automation, and closed-loop control on a small civic problem.

| Plane                 | MVP capability                                                                                                                         | Deferred depth                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| Governance            | Civic Body, member roles, proposal, deliberation record, approval rule, simple direct vote/consent configuration, delegation envelope. | Transitive (liquid) delegation chains, sortition, complex constitutional procedures.  |
| Planning/Optimization | Portfolio hierarchy, objectives, hard/soft constraints, resources, relationships, LP/QP solve, sensitivity basics.                     | MILP library, robust/stochastic optimization, game-theoretic negotiation. |
| Execution             | Milestones, dependencies, CPM, simple capacity, commitments, external action acknowledgement.                                          | Full ERP/procurement/EAM/service operations.                              |
| Evidence              | Manual/API evidence ingestion, provenance, confidence, actuals.                                                                        | Large sensor networks and broad data marketplace.                         |
| Learning              | Variance, simple benefits comparison, model-change proposal.                                                                           | Automated calibration/ML loops.                                           |
| Federation            | Second-jurisdiction simulated interface and shared constraint test.                                                                    | Live distributed federation.                                              |
| Trust                 | Identity/role/authority, immutable versions, audit/export, basic signing hooks.                                                        | Full production PKI/zero-trust/hardware-rooted identity.                  |
| AI                    | Conversational drafting/explanation, structured proposal/model assistance, tool-gated actions.                                         | Broad autonomous operations.                                              |

## 26.1 MVP Reference Scenario

A suitable reference scenario is a small Civic Body allocating a constrained annual improvement budget across 8-20 candidate initiatives with multiple objectives, one ecological/resource ceiling, one capacity constraint, one funding restriction, project dependencies, and a small number of delegated rebalance rules. The scenario should deliberately introduce one shock that can be resolved within delegation and one that requires governance escalation.

## 26.2 MVP End-to-End Acceptance Tests

Each test carries the ID MVP- plus its number, from MVP-100 to MVP-114 (MVP-112 to MVP-114 added at Gate 1, CL-062).

100. Create a Civic Body, Governance Process, members/roles, authority, and a portfolio.

101. Submit two competing proposals and preserve their exact versions.

102. Approve objectives, constraints, budget/resource envelope, and decision method.

103. Build and solve a feasible portfolio; show binding constraints and at least one near-optimal alternative.

104. Commit the approved portfolio without double-allocating resources.

105. Post actuals without altering the baseline.

106. Trigger a within-envelope variance and execute a delegated rebalance.

107. Trigger a hard-constraint or materiality breach and produce an Exception Proposition.

108. Approve a changed state and preserve the prior baseline and decision lineage.

109. Replay the original decision from its historical snapshot.

110. Export the civic state in a documented machine-readable package sufficient for independent reconstruction.

111. Demonstrate that the AI interface cannot bypass a failed authority or constraint check.

112. Compute the critical path, early and late dates, and float for a hand-computed dependency network, and level it against one capacity constraint.

113. Classify variances as Within Tolerance, Delegated Rebalance, or Exception, matching 8.8.

114. Draft a proposition through the conversational panel; the draft matches the desktop form field for field, flags every AI-introduced change, and commits only after human confirmation.

## 26.3 Collapse and Restoration Scenario

A simulator scenario for 17.9, run on Riverbend Commons after the 26.1 reference scenario. It demonstrates recovery without centralized or AI sovereignty.

1.  Collapse: the council misses quorum at 3 consecutive sessions, and the Justice of the Peace's term expires with no successor.

2.  Detection: the system opens a Continuity Case in Detected and notifies members, the Elders Council, and the federation partner. It declares nothing.

3.  Raising: the Elders Council raises an Incapacitated case, and a verifier from a federation partner confirms it.

4.  Convening: the Elders Council issues a warrant for a Justice of the Peace election with a 60-day sunset.

5.  Roll and election: the roll is drawn from the identity register (23.1.1). The result passes 41 to 30 with 6 Provisional voters, so it is not assurance-sensitive. An external verifier certifies it.

6.  Restoration: the new Justice of the Peace convenes a council election under the existing Governance Process, and both continuity mandates end.

7.  Variant, compromise: the Elders Council is found captured, and an External Convener (a neighboring Civic Body's Justice of the Peace, under the Federation Contract) runs the same process.

8.  Variant, total failure: all paths lapse, and members petition for a facilitated founding assembly with observers; its result stays "reconstituted, recognition pending."

Assertions: no actor holds authority after its sunset; the assistant never raises, verifies, or certifies; every step names its authority basis; and the case replays identically (CONT-AT-01 to CONT-AT-09).

# 27. Requirements Traceability Framework

Beginning with v0.4, detailed requirements should receive stable identifiers so future schemas, code, tests, and governance decisions can trace back to the functional intent. The following identifier families are proposed.

| Prefix | Domain                                      | Example                                                                                        |
|--------|---------------------------------------------|------------------------------------------------------------------------------------------------|
| BOD    | Basis of Design                             | BOD-EXIT-001 civic-state portability.                                                          |
| GOV    | Governance Plane                            | GOV-PROC-001 proposition version locking.                                                      |
| OPT    | Planning/Optimization                       | OPT-CNST-001 hard-constraint enforcement.                                                      |
| EXE    | Execution                                   | EXE-COM-001 commit-time balance recheck.                                                       |
| EVD    | Evidence                                    | EVD-PROV-001 raw-to-derived lineage.                                                           |
| LRN    | Learning                                    | LRN-CAL-001 empirical-only automated calibration.                                              |
| FED    | Federation                                  | FED-AUTH-001 explicit multi-party authority.                                                   |
| TRU    | Civic Trust                                 | TRU-EXIT-001 independent export.                                                               |
| AI     | AI Process Manager                          | AI-COMMIT-001 no direct committed-state write.                                                 |
| DPP    | Decision Provenance                         | DPP-REPLAY-001 historical replay.                                                              |
| MVP    | MVP acceptance                              | MVP-E2E-001 vertical-slice scenario.                                                           |
| CMT    | Civilizational Maturity & Type-I Transition | CMT-GATE-001 Type-I Readiness Gate: no single dimension mathematically compensated by another. |
| JNY    | Roles & User Journeys                       | JNY-GRAD-001 Guest Proposer excluded from eligible population.                                 |
| UIX    | Interaction Architecture                    | UIX-NEUTRAL-001 feed/notification neutrality.                                                  |
| PT     | Prosperity Transition                       | PT-06 portfolio formation with explicit complements and substitutes.                           |
| SRBG   | Shared Risk and Benefit Governance          | SRBG-03 floor never scaled by contribution.                                                    |
| CAB    | Civic Assurance and Buffering               | CAB-04 cash without deliverable capacity fails readiness.                                      |
| PF     | Prosperity Floor                            | PF-03 in-kind provisioning first.                                                              |
| CE     | Commons Endowment                           | CE-02 rule-based percent-of-market-value draw.                                                 |
| GJ     | Guardian Jurisdiction                       | GJ-AT binding veto on ecological-limit breach.                                                 |
| IA     | Indigenous Alignment                        | IA-02 free, prior and informed consent for sacred sites.                                       |
| LM     | Lifecycle Management                        | LM-01 per-module cycle registry.                                                               |
| ECO    | Ecological module floor                     | ECO-GUARD-001 guardian fiduciary duty and funding independence.                                |
| ASR    | Assurance Controls                          | ASR-06 accessibility conformance (WCAG 2.2 AA).                                                |
| CMP    | Compliance acceptance                       | CMP-003 open-meeting guard blocks private member-to-member deliberation.                       |
| OPS    | Operator certification                      | OPS-NEUTRAL-001 process-only operator and implementer roles.                                   |
| RES    | Resource registry                           | RES-REGISTRY-001 single registration of every resource commitment.                             |
| INV    | Invariant acceptance tests                  | INV-AT-04 uncertain evidence cannot become a binding constraint.                               |

Two ID schemes are in use. Invariants and cross-cutting requirements use PREFIX-TOPIC-NNN (GOV-FLOOR-001). Module requirement tables and acceptance tests use PREFIX-NN or PREFIX-AT-NN (CE-02, ASR-06, PF-AT-01). MVP acceptance tests keep their Section 26.2 numbers as MVP-100 to MVP-111. IDs are never reused.

The developer-ready revision should convert normative shall-statements throughout the document into an indexed requirements catalog with verification method: inspection, analysis, demonstration, or test.

# 28. Remaining Functional Specification Domains

v0.4 substantially restores the layered analysis beneath the civic architecture, but several domains should be developed before freezing implementation contracts:

- Democratic aggregation methods and constitutional/process templates in greater mathematical and procedural depth.

- Identity, eligibility, residency/membership, delegation, and anti-capture/Sybil-resistance design.

- Rights, privacy, public-record, and due-process semantics across heterogeneous jurisdictions (partly addressed by Jurisdiction Compliance Packs, 43.4).

- Benefits-realization and causal-inference methods for public outcomes.

- Detailed financial accounting, procurement, grants, asset, and service-management scope: native ACECOG capability versus modular civic subsystems.

- Ontology and unit system for ecological, infrastructure, social, and fiscal variables.

- Formal multi-jurisdiction negotiation and treaty lifecycle.

- Production security/threat model and disaster/recovery/continuity architecture.

- Developer contracts: schemas, APIs, events, state transition matrices, policy expressions, solver adapters, and test fixtures.

## 28.1 Domain Portability: Reach and Current Limits

Section 1.1 states the design intent that ACECOG provide 'a common civic operating architecture without requiring uniform political institutions, legal systems, cultures, or technology stacks.' This subsection makes that claim precise rather than aspirational: what in the current specification actually carries it, what has been exercised in the Phase 1 MVP build, and where the claim currently runs out.

### 28.1.1 What Makes the Core Portable

- The canonical object model (Section 7) carries no domain semantics: an Objective is a named weighted vector, a Constraint is a named coefficient row with a sense and right-hand side, a Resource is a named capacity. Nothing in the Governance, Planning/Optimization, Execution, or Evidence Planes reads or depends on what any of these are named. The Phase 1 MVP reference scenario (26.1) and its acceptance suite (26.2, MVP tests 100-111) exercise this pipeline end to end on an ordinary civic budget-allocation problem with no domain-specific content required or assumed anywhere in the engine code.

- A Governance Process's decision rule (eligibility, quorum fraction, approval threshold, novelty threshold, minimum attestation confidence — Section 7) is civic-body configuration, not engine code; different institutional traditions map to different configured instances of the same object, not to different software.

- The invariant floor (Section 14) governs process integrity — no destructive overwrite, no execution without authority, no silent constraint relaxation, full replayability — and deliberately never encodes substantive policy or values. Section 4.3's Self-Defined Maturity Frameworks make this pluralism explicit: a Civic Body need not adopt ACECOG's own reference notion of maturity, only the floor beneath it. Part V (v0.18) adds one deliberate exception, stated openly: ACECOG fixes one access condition — participation and Prosperity Floor access are never priced (invariant 24 (TRU-ACCESS-001) and GOV-PROSPERITY-001) — plus a small set of commons and guardian rules (module floors 36.6 and 37.5) that bind only Civic Bodies adopting the Commons Endowment or Guardian Jurisdiction modules. It still sets no substantive level of benefit.

### 28.1.2 Where Portability Currently Runs Out

- The Optimization Engine (Section 18) is built around allocation-shaped decisions — portfolios, budgets, capacity plans — where a continuous LP relaxation is a natural fit. Adjudicative or purely qualitative decisions (a zoning variance, a policy ruling) are not allocation problems; they are fully served by the Governance Plane's proposition/deliberation/authority spine alone, without invoking Section 18 at all, but that distinction is left implicit rather than named as a first-class usage mode.

- Deliberation method is currently limited to threshold voting by individual eligible members (Section 17). Sortition, consensus-based decision-making, and transitive (liquid) delegation chains are explicitly deferred (single-level delegation is built in Phase 1, 17.5) (Section 26 'deferred depth' column) rather than built; a governance tradition whose legitimate process is not vote-counting cannot yet be represented as itself, only approximated by a voting configuration that isn't how that tradition actually decides.

- Institutional, rather than individual, actors are only partially exercised: the Agency Planning Manager (30.6) and City Manager (30.8) journeys both assume an Actor can carry an institution's standing, but no journey yet specifies an institution — a tribal nation, a special district — as a first-class Federation Contract participant negotiating its own sovereignty claims, as opposed to a role inside an existing Civic Body.

- Legal and regulatory recognition of an exported civic state or a Decision Provenance Packet (Section 9) as compliant evidence under a given jurisdiction's open-meetings, public-records, or due-process law is external integration work, not a technical guarantee this specification provides. This is the same gap Section 28's original list already names ('rights, privacy, public-record, and due-process semantics across heterogeneous jurisdictions'); it is restated here specifically as a portability limit rather than a general open item. Section 43 narrows it: Jurisdiction Compliance Packs (43.4) enforce open-meeting, public-records, and retention rules in product behavior, and Legal Effect Declarations (ASR-08) label every result’s legal status, but recognition itself remains with each jurisdiction.

# Part III — Civilizational Maturity & Type-I Transition Module

# 29. Civilizational Maturity & Type-I Transition (CMT) Module

**Build status (v0.21).** Part III is catalog reserve with no build phase. No Phase 1, 2, or 3 deliverable implements it. Its concepts reach the build only through requirements stated elsewhere, chiefly the Maturity Framework (4.2, 4.3) and Part V.

*Document Status: Concept Functional Specification. System: Accelerated Ecological & Civic Governance (ACECOG). Module: Civilizational Maturity & Type-I Transition (CMT). Purpose: assessment, governance, planning, simulation, and continuous improvement of civilizational maturity across nested social systems.*

## 29.1 Purpose

The Civilizational Maturity & Type-I Transition module provides ACECOG with a structured method for evaluating and improving the maturity of human systems.

The module begins from a fundamental distinction:

**Civilizational power, civilizational maturity, and civilizational reach are related but independent dimensions.**

Traditional measures of development frequently emphasize economic output, technological capability, energy consumption, or institutional form. Such measures can obscure dangerous imbalances. A society may possess extraordinary technological capability while lacking the institutional, ethical, ecological, informational, or coordination capacity necessary to govern that capability safely.

The CMT module therefore represents civilization as a multidimensional system and provides mechanisms to:

- observe its current condition;

- evaluate maturity across multiple dimensions;

- identify developmental bottlenecks;

- detect dangerous maturity gaps;

- model alternative developmental pathways;

- translate values into measurable objectives;

- prioritize interventions;

- monitor outcomes;

- learn from those outcomes; and

- continuously revise the governance response.

The objective is not to define a utopian end state.

The objective is to create a **self-observing, self-governing and continuously improving civilization**.

## 29.2 Intellectual Genesis

The CMT framework synthesizes several existing approaches to civilizational development.

These include:

- **Kardashev / Sagan:** energy utilization and physical capability;

- **Fukuyama:** institutional capacity, rule of law and accountability;

- **Graves / Spiral Dynamics:** development and integration of cultural value systems;

- **Kohlberg / Habermas:** moral reasoning, legitimacy and deliberation;

- **Bostrom and existential-risk theory:** civilization-scale coordination and catastrophic-risk management;

- **Georgist economics:** land, economic rent and community-created value;

- **ecological economics:** regenerative capacity, resource stocks, flows and externalities;

- **cybernetics and complex adaptive systems:** feedback, adaptation and resilience;

- **information and systems theory:** observability, provenance and decision traceability; and

- **space governance and cosmic citizenship:** expansion of civilization beyond planetary boundaries.

ACECOG does not treat these as competing maturity scales.

Instead, their principal insights are represented as **orthogonal dimensions of a common civilizational state model**.

## 29.3 Core Conceptual Model

ACECOG shall represent civilizational maturity as a state vector:

*C = ⟨E, I, V, M, Co, Ec, En, Info, T, R, X, N⟩ — a twelve-dimension state vector, one term per row of the table below.*

where:

| **Code** | **Dimension**                      | **Core Question**                                                                                         |
|----------|------------------------------------|-----------------------------------------------------------------------------------------------------------|
| **E**    | Energy                             | Can the system obtain and employ sufficient energy sustainably?                                           |
| **I**    | Institutions                       | Can power reliably govern itself?                                                                         |
| **V**    | Values                             | Can multiple value systems coexist and integrate constructively?                                          |
| **M**    | Moral Development                  | How broadly does ethical consideration extend?                                                            |
| **Co**   | Coordination                       | Can autonomous actors solve problems at the scale of their consequences?                                  |
| **Ec**   | Ecology                            | Does the system maintain or regenerate the ecological systems supporting it?                              |
| **En**   | Economy                            | Does the economy predominantly reward productive value creation rather than extraction?                   |
| **Info** | Information                        | Can the system reliably perceive and understand its own condition?                                        |
| **T**    | Technology                         | Can increasingly powerful technologies remain governed by explicit social values?                         |
| **R**    | Resilience                         | Can the system absorb disruption while maintaining essential functions and principles?                    |
| **X**    | Cosmic Integration                 | Can civilization responsibly extend civic, ethical and institutional participation beyond its home world? |
| **N**    | Human & Civilizational Flourishing | Does civilization preserve and expand humanity’s capacity to create, discover, flourish, evolve, express? |

These dimensions SHALL NOT ordinarily be reduced to a simple arithmetic average.

ACECOG shall preserve the complete maturity vector so that dangerous asymmetries remain visible.

## 29.4 Type-I Definition

The CMT module distinguishes **Kardashev Type I** from **ACECOG Type I**.

**Kardashev Type I**

Planetary-scale command or utilization of energy.

**ACECOG Type I**

Planetary-scale capability for conscious, adaptive and responsible self-governance.

A Type-I civilization demonstrates sufficient maturity across all critical dimensions to manage the consequences of its own technological and economic capabilities.

ACECOG therefore treats Type-I status as a **minimum viable maturity envelope**, not a single numerical threshold.

A civilization may possess Type-I energy capabilities without qualifying as an ACECOG Type-I civilization.

## 29.5 System Objectives

The CMT module SHALL support five primary functions:

### 29.5.1 Observe

Continuously characterize the condition of the governed system using quantitative and qualitative information.

### 29.5.2 Understand

Transform observations into indicators, trends, relationships, risks and competing interpretations.

### 29.5.3 Deliberate

Allow participants to evaluate conditions and proposed actions against explicit values, objectives and constraints.

### 29.5.4 Act

Translate decisions into portfolios, programs, projects, policies and operating actions.

### 29.5.5 Learn

Compare intended and actual outcomes and incorporate the resulting knowledge into subsequent decisions.

The fundamental control loop shall therefore be:

**Values → Objectives → Observation → Analysis → Deliberation → Decision → Execution → Measurement → Learning → Adaptation**

This loop SHALL be recursive and continuous.

## 29.6 Functional Requirements

### FR-1 — Maturity Assessment Engine

ACECOG SHALL maintain a maturity assessment for each applicable governance entity.

Supported entities may include:

- organizations;

- communities;

- municipalities;

- watersheds;

- bioregions;

- states or provinces;

- nations;

- planetary institutions; and

- future off-world settlements.

Each entity shall maintain an independent 11-dimensional maturity vector.

### FR-2 — Nested Governance Model

Governance entities SHALL be capable of hierarchical nesting.

Example:

**Individual → Community → Municipality → Bioregion → Nation → Planet → Multiworld System**

Higher levels SHALL NOT automatically supersede lower levels.

Authority shall be assigned according to **subsidiarity**:

Decisions should occur at the lowest organizational level possessing sufficient capability, information and jurisdiction to manage their consequences.

ACECOG shall allow issues to escalate when their consequences exceed the competent scope of the originating entity.

### FR-3 — Indicator Registry

Each maturity dimension SHALL contain a configurable set of indicators.

Indicators may be:

- quantitative;

- qualitative;

- observational;

- modeled;

- expert-assessed;

- citizen-reported; or

- machine-derived.

Every indicator SHALL include:

- definition;

- unit;

- source;

- provenance;

- collection date;

- confidence level;

- geographic scope;

- applicable governance level;

- responsible steward;

- update frequency; and

- known limitations.

### FR-4 — Evidence and Provenance

No maturity score SHALL exist without traceable supporting evidence.

Users must be able to traverse:

**Score → Indicator → Observation → Source → Methodology**

ACECOG shall distinguish among:

- observed fact;

- reported information;

- model output;

- inference;

- expert judgment;

- community sentiment;

- scenario assumption; and

- speculative hypothesis.

This distinction shall remain visible throughout downstream decision processes.

## 29.7 Maturity Gap Analysis

ACECOG SHALL identify mismatches between civilizational capability and the capacity required to govern that capability.

A conceptual maturity-gap function may be expressed as:

$$G = P - M_{r}$$

where:

- $P$= potentially transformative or destructive capability;

- $M_{r}$= maturity required to manage that capability responsibly.

A high positive maturity gap SHALL generate a system-level risk signal.

Examples include:

- advanced AI without adequate governance;

- biotechnology without adequate biosecurity;

- nuclear capability without conflict-management capacity;

- geoengineering without planetary coordination;

- resource extraction exceeding ecological governance;

- information technology exceeding epistemic resilience.

The system SHALL prioritize dangerous **imbalances**, not merely low absolute scores.

## 29.8 Bottleneck Analysis

ACECOG SHALL identify dimensions constraining overall system development.

For example:

**Energy: 7 Technology: 8 Information capability: 7 Institutions: 4 Coordination: 3 Ecology: 3**

The system SHALL NOT report this as an average maturity of 5.3.

Instead it should identify:

**Coordination and ecological governance constitute critical developmental bottlenecks while technological capability materially exceeds governance capacity.**

Bottleneck analysis SHALL feed portfolio prioritization.

## 29.9 Values Integration

Each governance entity SHALL maintain an explicit values framework.

Values may include principles such as:

- human dignity;

- individual sovereignty;

- ecological stewardship;

- transparency;

- subsidiarity;

- pluralism;

- non-aggression;

- intergenerational responsibility;

- resilience;

- equity;

- knowledge integrity; and

- protection of sentient life.

Values SHALL be linked to:

**Value → Principle → Objective → Metric → Decision Criterion**

This provides traceability between stated values and actual resource allocation.

The system SHALL flag decisions materially inconsistent with declared values.

## 29.10 Portfolio Optimization

Maturity assessments SHALL feed ACECOG portfolio management.

Candidate policies, programs and projects may be evaluated according to their expected effects on the maturity vector.

Example:

**Land Value Tax Pilot**

Primary dimensions:

- Economy;

- Institutions;

- Ecology;

- Resilience.

**Distributed Renewable Microgrid**

Primary dimensions:

- Energy;

- Ecology;

- Resilience;

- Economy.

**Open Governance Ledger**

Primary dimensions:

- Information;

- Institutions;

- Coordination.

**AI Decision-Support System**

Primary dimensions:

- Technology;

- Information;

- Institutions;

- Coordination;

- Moral Development.

ACECOG SHALL permit portfolio optimization against multiple maturity objectives simultaneously.

## 29.11 Trade-Off Analysis

The system SHALL identify circumstances in which improvement in one dimension degrades another.

Examples:

- energy expansion damaging ecology;

- security measures degrading institutional accountability;

- rapid automation damaging economic resilience;

- centralized coordination degrading local sovereignty;

- ecological restrictions producing disproportionate social hardship.

ACECOG shall present these as explicit trade-offs rather than concealing them within aggregate scores.

## 29.12 Scenario Engine

Users SHALL be able to construct alternative future scenarios.

Scenarios may include:

- baseline continuation;

- technological acceleration;

- economic contraction;

- climate disruption;

- infrastructure failure;

- institutional fragmentation;

- major natural disaster;

- rapid migration;

- energy abundance;

- AI transformation;

- off-world settlement; and

- hypothetical confirmed contact with nonhuman intelligence.

Speculative scenarios SHALL be explicitly labeled as such and separated from empirical baseline assumptions.

For each scenario ACECOG shall estimate:

- maturity-vector effects;

- resource requirements;

- institutional stresses;

- dependencies;

- failure modes;

- opportunities; and

- recovery pathways.

## 29.13 Resilience and Discontinuity Mode

ACECOG SHALL support governance analysis under severe disruption.

The objective is not simply continuity of institutions.

The objective is **continuity of essential values and functions**.

The system shall identify:

- essential services;

- minimum viable governance;

- critical resource stocks;

- infrastructure dependencies;

- knowledge preservation requirements;

- succession mechanisms;

- decentralized fallback capabilities; and

- restoration priorities.

A resilient Type-I architecture should degrade gracefully rather than catastrophically.

## 29.14 Economic Architecture Interface

The CMT module SHALL interface with a broader economic model.

The economic architecture may evaluate:

- land value taxation;

- resource rents;

- commons management;

- productive taxation;

- ecological externalities;

- circular material flows;

- distributed ownership;

- public infrastructure investment;

- markets;

- cooperative enterprise;

- complementary exchange systems; and

- universal access to defined foundational commons.

Each SHALL be treated as one potential economic mechanism rather than the complete economic system.

Economic mechanisms SHALL be evaluated according to their effects across the maturity vector.

## 29.15 Ecological Accounting

ACECOG SHALL represent natural systems as governed assets and dependencies rather than unpriced externalities.

Tracked systems may include:

- watersheds;

- aquifers;

- soils;

- forests;

- biodiversity;

- atmosphere;

- mineral resources;

- energy resources;

- agricultural productivity; and

- waste assimilation capacity.

Ecological indicators SHALL be connected to economic and infrastructure decisions.

The system should distinguish:

**resource stock → sustainable yield → actual extraction → regeneration rate**

## 29.16 Cosmic Integration and Citizenship

ACECOG SHALL include a Cosmic Integration dimension independent of technological maturity.

An illustrative maturity progression is:

- **X0 — Planet-bound:** civilization principally observes the cosmos.
- **X1 — Space-accessing:** routine human or robotic operations beyond the home planet.
- **X2 — Spacefaring:** persistent habitation beyond the home planet.
- **X3 — Multiworld:** autonomous settlements operate across multiple celestial bodies.
- **X4 — Cosmic Citizenship:** civic identity, law and ethical responsibility extend beyond planetary nationality.
- **X5 — Intercivilizational:** if independent technological civilizations are encountered, durable peaceful relations can be maintained.
- **X6 — Galactic Participation:** if a wider interstellar civil order exists, civilization can participate without abandoning legitimate local autonomy.

ACECOG SHALL NOT treat the existence of extraterrestrial civilizations as an empirical assumption.

Instead, potential contact shall constitute a **high-consequence governance scenario** useful for testing institutional readiness.

## 29.17 First-Contact Stress Test

The system SHOULD support a hypothetical First-Contact Readiness assessment.

Questions include:

- Who possesses authority to communicate?

- Who legitimately represents humanity?

- What information may be withheld, and by whom?

- What legal status applies to nonhuman intelligence?

- How are technological transfers governed?

- Can any nation or corporation monopolize received knowledge?

- What constitutes informed planetary consent?

- What rights apply to nonhuman sentient beings?

- How are conflicting religious, cultural and scientific interpretations accommodated?

- How is local sovereignty preserved within a planetary response?

The purpose of this test is broader than extraterrestrial contact.

It evaluates whether institutions can respond coherently to a **novel event whose consequences exceed existing jurisdictional boundaries**.

## 29.18 Continuous Improvement Engine

Every implemented intervention SHALL support a closed feedback cycle:

$$Plan \rightarrow Execute \rightarrow Measure \rightarrow Compare \rightarrow Learn \rightarrow Adapt$$

For each intervention ACECOG should preserve:

- expected outcome;

- actual outcome;

- assumptions;

- variance;

- causal assessment;

- unintended consequences;

- lessons learned; and

- recommended adaptation.

Institutional learning therefore becomes persistent rather than dependent upon individual memory.

## 29.19 Human–AI Relationship

AI SHALL function principally as:

- observer;

- analyst;

- simulator;

- pattern detector;

- optimization engine;

- institutional-memory interface; and

- decision-support system.

AI SHALL NOT automatically acquire governance legitimacy merely through superior computational capability.

The system shall maintain a distinction between:

**analysis → recommendation → authorization → execution**

Authorization requirements shall depend upon the nature, consequence and reversibility of the decision.

## 29.20 User Interface

The primary CMT interface SHOULD provide a **Civilizational Maturity Dashboard** containing:

**Maturity Vector**

Current condition across all eleven dimensions.

**Trend**

Direction and velocity of change.

**Bottlenecks**

Dimensions currently constraining development.

**Maturity Gaps**

Capabilities exceeding governance capacity.

**Risks**

High-consequence vulnerabilities.

**Portfolio**

Active interventions intended to change maturity conditions.

**Scenarios**

Projected state vectors under alternative futures.

**Values Traceability**

Connection between community values, decisions, spending and outcomes.

**Evidence**

Ability to drill from every assessment to underlying data and assumptions.

## 29.21 Regional Prototype

Initial prototypes SHALL be modeled around established fertile bioregional corridors, with functional subregions based upon:

- watersheds;

- settlement patterns;

- transportation;

- agriculture;

- energy;

- ecology;

- culture;

- economic relationships; and

- governance jurisdiction.

CMT Regional Prototypes are not intended initially to constitute a new political jurisdiction.

They function as a **digital governance model and civilizational laboratory**.

## 29.22 Prototype Test Question

The principal prototype question shall be:

**Can a geographically bounded collection of autonomous communities use transparent information, explicit values, ecological accounting and adaptive portfolio governance to behave like a small-scale prototype of a mature planetary civilization?**

Success does not require ideological agreement.

Success requires the ability to:

- recognize disagreement;

- establish shared facts where possible;

- represent uncertainty where facts remain incomplete;

- make legitimate decisions;

- measure consequences;

- preserve local autonomy;

- coordinate shared problems; and

- alter course when evidence demonstrates that a decision is failing.

## 29.23 Type-I Readiness Gate

ACECOG SHALL eventually support a Type-I Readiness Gate.

A system qualifies only when all designated critical dimensions exceed minimum thresholds and no unacceptable maturity gap remains.

Conceptually:

$$TypeI = \left\lbrack \min\left( C_{i} \right) \geq T_{i} \right\rbrack \land \left\lbrack G_{critical} \leq G_{\max} \right\rbrack$$

This prevents exceptional performance in energy, technology or wealth from compensating mathematically for catastrophic weakness in governance, ecology, coordination or resilience.

## 29.24 Design Principles

The CMT module SHALL adhere to the following principles:

**Transparent** — assessments and decisions are traceable.

**Pluralistic** — disagreement is represented rather than suppressed.

**Evidence-based** — facts, inference and speculation remain distinguishable.

**Value-conscious** — optimization cannot occur without explicit objectives.

**Subsidiary** — authority remains as local as practicable.

**Adaptive** — decisions remain subject to evidence and revision.

**Ecologically bounded** — physical limits cannot be optimized away.

**Resilient** — critical functions survive component failure.

**Human-governed** — computational intelligence informs legitimacy rather than replacing it.

**Scalable** — architecture operates from community through planetary and potentially multiworld scales.

**Evolutionary** — the system optimizes the capacity to learn rather than prescribing a permanent social order.

## 29.25 Governing Proposition

The Civilizational Maturity & Type-I Transition module rests upon the following proposition:

**A mature civilization is not one that has solved every problem. It is one capable of accurately perceiving its condition, reconciling action with its values, coordinating at the scale of its consequences, governing its own power, learning from outcomes, and continuously correcting its trajectory.**

ACECOG exists to provide the information, decision architecture, institutional memory and feedback mechanisms through which that capability can emerge.

The Type-I prototype therefore does not attempt to design the final civilization.

It attempts to build the **operating system through which civilization becomes capable of consciously designing, observing and improving itself.**

**  
**

# Part IV — Roles & User Journeys

# 30. Roles & User Journeys

## 30.1 Purpose

Sections 0-29 specify ACECOG plane by plane and, in Section 25, trace a handful of system-level scenarios across planes (Cross-Plane Functional Traces). Those traces are written from the system's point of view: which objects, states, and invariants fire, in what order. This Part complements them with the human point of view: a named persona, their motivation, and the screens and decisions they actually experience end to end. Journeys are how ACECOG's abstractions get checked against a lived, single-user story before any UI is designed or filmed — and they are the intended basis for future reference demonstrations of the platform.

Like the rest of this specification, the Journey Catalog is cumulative: it grows by version, and 30.3 is the template for authoring new entries. It is not a UI specification and does not prescribe visual design; it prescribes which real object states and authority checks a screen must be truthfully backed by.

## 30.2 Relationship to Cross-Plane Functional Traces

A Journey is a Cross-Plane Functional Trace (Section 25) narrated from one participant's seat, extended with the human-facing detail a system trace deliberately omits: what the persona sees, what they're asked to decide, and where the system must surface an explanation rather than a raw object. Every step in a Journey should cite the plane section, object, and state-machine transition it corresponds to, so the Journey stays provably faithful to the canonical model rather than becoming an independent, driftable narrative.

## 30.3 Journey Template

Every catalog entry from 30.5 onward shall use this template:

| Field                      | Content                                                                                                                                                                                                                 |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Persona                    | Who they are, their starting relationship to the Civic Body (member, non-member, staff, auditor, partner jurisdiction), and their motivation.                                                                           |
| Entry point                | How they arrive (Section 23.1 identity/role); whether Membership Credential is required or self-attestation suffices for the decision class involved (Section 17.5 eligibility assurance, invariant 13 (TRU-ELIG-001)). |
| Preconditions              | Civic Body / Governance Process / Portfolio state that must already exist for the journey to begin.                                                                                                                     |
| Step sequence              | Numbered steps, each citing the plane section and object/state-machine transition it exercises (Sections 7, 8, 17-24).                                                                                                  |
| Authority checkpoints      | Every point at which an authority path or Delegation Envelope is required or tested (Section 14 invariants 2 (GOV-AUTHPATH-001), 6 (FED-AUTH-001) and 7 (GOV-ENVELOPE-001)).                                            |
| Surfaces required          | What must be shown to the persona at each step for the journey to be honest rather than cosmetic (e.g., the actual optimization fit-check, not a canned result).                                                        |
| New/clarified requirements | Any gap this journey exposes in Sections 0-29 that should be folded back into the core specification.                                                                                                                   |
| Acceptance criteria        | End-to-end tests in the style of Section 26.2, under this Part's own traceability prefix (Section 27, prefix JNY).                                                                                                      |
| Deferred depth             | What a first build of this journey may simplify, matching the Section 26 pattern.                                                                                                                                       |

## 30.4 Journey Catalog Status

As with the phase-pull model applied to the rest of the specification, journeys are authored into this catalog over time and pulled into a build phase individually rather than being built all at once.

| Journey                            | Primary persona                                 | Status                                                        | Traceability prefix |
|------------------------------------|-------------------------------------------------|---------------------------------------------------------------|---------------------|
| The Aspiring Grad Student (30.5)   | Individual, non-member proposer                 | Specified (v0.12)                                             | JNY-GRAD-\*         |
| The Agency Planning Manager (30.6) | Regional planning-agency observer               | Specified (v0.13)                                             | JNY-AGCY-\*         |
| The Resident / Voter (30.7)        | Mass-participation resident                     | Specified (v0.15)                                             | JNY-CIT-\*          |
| The City Manager (30.8)            | Delegated jurisdiction executive                | Specified (v0.15)                                             | JNY-MGR-\*          |
| The Facilitator/Clerk (30.9)       | Civic-body process administrator                | Specified (v0.17)                                             | JNY-FAC-\*          |
| The Auditor (30.10)                | External observer/auditor                       | Specified (v0.17)                                             | JNY-AUD-\*          |
| The Federation Partner (30.11)     | Delegate of a second jurisdiction               | Specified (v0.17)                                             | JNY-FED-\*          |
| The Fund Manager (30.12)           | External co-investing fund manager (non-member) | Specified (v0.17), pending the full Funding Instrument object | JNY-FUND-\*         |
| The Program Manager (30.13)        | Manager of one multi-node program               | Specified (v0.17)                                             | JNY-PROG-\*         |

## 30.5 Journey: The Aspiring Grad Student

Individual Proposer to Funded, Executing Project. This is the first entry in the Journey Catalog and the reference journey named in the project's own demonstration goals: a single continuous story from an individual originating a proposal through a jurisdiction funding and executing it, provable against live ACECOG state rather than staged screens.

### 30.5.1 Persona & Motivation

A graduate student, not yet a member of the Civic Body whose portfolio she wants to draw on, with a small, well-scoped community project (e.g., a riverside restoration micro-grant in the same domain as the Section 26.1 MVP reference scenario). She wants to propose it, understand honestly whether it can be funded given everything else already committed, and watch it move — or not move — through a real decision, not a submission form that disappears into a queue.

### 30.5.2 Preconditions and Open Design Questions

This journey depends on a jurisdiction (Civic Body + Governance Process + an existing, live Portfolio with real committed and remaining budget — Sections 7, 17, 18) that already exists before she arrives. It surfaces two questions Sections 0-29 do not yet resolve and that should be settled before this journey is built:

- Non-member proposer eligibility: Section 17.5's eligibility assurance already permits a jurisdiction to allow self-attestation for low-stakes process types (invariant 13 (TRU-ELIG-001)). This journey requires that a Governance Process may define a 'proposal submission' decision class as open to self-attested non-members, while the 'approval'/'commit' decision classes for the same proposition remain gated to full Membership Credentials or delegated civic authority — i.e., anyone may propose, only the Civic Body may decide.

- Guest Proposer identity: a lightweight Actor record (Section 7) with no Membership Credential, sufficient for authorship attribution and provenance (Section 9), but explicitly excluded from the eligible population used by quorum and vote-tally calculations (Section 17.4; 17.8 criterion 2).

### 30.5.3 Step Sequence

- Step 1: Entry & identity (Section 23.1): the student authenticates as a Guest Proposer Actor. No Membership Credential is issued or required at this step (invariant 13 (TRU-ELIG-001) is untouched: she is not counted in anyone's eligible population).

- Step 2: Guided proposal drafting (Section 8.3 Draft state; Section 17.2 'Proposer' role): a simple wizard collects title, description, requested budget, resource needs, and any dependency on existing initiatives, and assembles it into a Proposition object (Draft).

- Step 3: Submission & validation (Section 8.3 steps 1–4): Draft -\> Proposed -\> Validated. The same structural and jurisdiction checks any proposition receives apply here unchanged.

- Step 4: Live optimization fit-check (Section 18, 'Optimization Run' Section 8.6): before deliberation, the student is shown a real, live-solved preview of how her proposal interacts with the jurisdiction's current committed portfolio and remaining budget/capacity/ecological headroom — binding constraints and a near-optimal alternative included (Section 18.8; the same OptimizationEngine.solve_ppm output a civic-body member would see, not a separate, simplified calculation).

- Step 5: Routed to deliberation (Section 8.3 step 5; Section 17.3-17.4): the Validated proposition enters the jurisdiction's configured Governance Process. The student can observe deliberation and the live vote tally (Collective Will object, Section 17.4) but cannot vote — she is outside the eligible population (invariant 13 (TRU-ELIG-001)).

- Step 6: Decision (Section 8.4, 17.8): quorum and approval-threshold rules are applied exactly as in Section 17.8's governance acceptance criteria; the exact proposition version considered is preserved (17.8 criterion 1; Decision Provenance, Section 9).

- Step 7: Optimization re-run & baseline (Section 8.5-8.6): on approval, the portfolio is re-solved with her initiative included, producing a new Baseline that supersedes the prior one without destroying it (invariants 1 (DPP-IMMUTABLE-001) and 5 (EXE-BASELINE-001)).

- Step 8: Commitment (Section 8.7, invariants 2 (GOV-AUTHPATH-001) and 7 (GOV-ENVELOPE-001)): the jurisdiction's authorized role commits the new baseline through the same authority path and resource-balance recheck every commitment requires — the student cannot commit her own proposal; only a valid Authority can.

- Step 9: Execution visibility (Section 19, Section 8.8): the student can see her initiative's milestones, schedule position, and (once evidence is posted) actual progress, exactly as Section 20/9 already define, without gaining any write access to committed state.

- Step 10: Full provenance available on request (Section 9): the entire chain — her original proposition version, the deliberation record, the optimization run that qualified it, the approval, and the commitment — is retrievable as one Decision Provenance Packet, replayable per Section 9's Replay Modes.

### 30.5.4 New or Clarified Requirements Surfaced by This Journey

- Guest Proposer as a named, lightweight Actor subtype (Section 7) — an Actor with no Membership Credential, explicitly non-eligible for any vote/quorum calculation, but fully provenanced as an author (Section 9).

- A Governance Process decision class ('proposal_submission') distinct from its approval decision class, so eligibility (17.5) can be opened for submission while remaining restricted for approval/commit — the same object, two different eligibility gates by decision class.

- A non-authoritative, read-only optimization fit-check surface: the same OptimizationRun machinery (Section 8.6) exposed for preview before Deliberation, clearly distinguished from the authoritative run that produces the eventual Baseline, so a proposer sees the truth without that preview itself becoming an approval (Section 8.6: 'results are evidence for decisions; they are not themselves approvals').

### 30.5.5 Acceptance Criteria (JNY-GRAD-001..010)

- JNY-GRAD-001. Create a Guest Proposer Actor with no Membership Credential and confirm she is absent from the Civic Body's eligible population.

- JNY-GRAD-002. Submit a proposition as a Guest Proposer and confirm it reaches Validated through the same checks as a member-submitted proposition.

- JNY-GRAD-003. Run a live optimization fit-check against the jurisdiction's current committed portfolio and confirm it returns real binding constraints and a near-optimal alternative, not a canned response.

- JNY-GRAD-004. Confirm the Guest Proposer cannot cast a vote and that her attempted vote is rejected by the same eligibility check a human clerk would apply.

- JNY-GRAD-005. Deliberate and approve the proposition through the jurisdiction's Governance Process and confirm the Collective Will records the exact proposition version decided.

- JNY-GRAD-006. Re-solve the portfolio with the approved initiative included and confirm the prior baseline is superseded, not destroyed (invariant 1 (DPP-IMMUTABLE-001)).

- JNY-GRAD-007. Attempt to commit the new baseline as the Guest Proposer and confirm AuthorityError is raised identically to any other unauthorized actor (invariant 2 (GOV-AUTHPATH-001)).

- JNY-GRAD-008. Commit the new baseline as the jurisdiction's authorized role and confirm no double-allocation against already-committed initiatives (Section 19.5).

- JNY-GRAD-009. Post actuals against the new initiative's milestones and confirm the Guest Proposer can view execution status without write access.

- JNY-GRAD-010. Assemble and replay the full Decision Provenance Packet for this journey end to end and confirm every referenced object hash matches its historical snapshot (Section 9; mirrors MVP acceptance test 109).

## 30.6 Journey: The Agency Planning Manager

Regional Portfolio Visibility and Coordinated Push. This journey traces directly to the project's own 2019 discovery-phase pitch (prepared for a Marin County Board of Supervisors discovery project): one of five original "ACECOG Stories" was an Agency Planning Manager asking to see "everything related to climate resilience and environmental decarbonization that spans my and my neighbors' jurisdictions... how well those initiatives are resourced, their likelihood of success, and their contribution to regional goals... where I need to push, and how hard." This entry specifies that story against the current canonical model. The Fund Manager, Program Manager, and Resident stories from the same 2019 deck have since been specified (30.12, 30.13, and 30.7).

### 30.6.1 Persona & Motivation

A planning manager at a regional agency (e.g., a bioregional resilience authority) with no commit authority inside any single Civic Body's portfolio, but a standing, federation-scoped Authority (Section 7) to observe every participating jurisdiction's committed portfolio and propose regional coordination. She runs a recurring portfolio-review cycle — the same 'Portfolio Objectives / Portfolio Governance / Portfolio Management' cadence sketched in the project's own original Portfolio Process Matrix — and wants a truthful, live regional roll-up rather than a quarterly PDF assembled by hand.

### 30.6.2 Preconditions

Multiple Civic Bodies (Section 7), each running its own Governance Process and Portfolio, have each opted into a Federation Contract (Section 22.2) sharing read visibility of committed-portfolio state with the regional agency's Authority — local sovereignty is unaffected (non-negotiable principle 4). One of those jurisdictions is Riverbend Commons, whose portfolio now includes the Aspiring Grad Student's approved, executing initiative from 30.5.

### 30.6.3 Step Sequence

- Step 1: Cycle open (Section 21.4 continuous improvement cadence): the agency's recurring portfolio-review cycle opens. Rather than a static export, it pulls a live Cross-PPM Stitch (Section 22.3) across every federated jurisdiction's current committed Portfolio.

- Step 2: Regional roll-up, read-only (Section 22.3, Section 5.6 Multi-Jurisdiction Composition): the manager sees each jurisdiction's committed initiatives, remaining budget/capacity/ecological headroom, and binding constraints, composited against shared regional objectives — a non-authoritative observation view, distinct from a joint-solve federation (invariant 6 (FED-AUTH-001): no cross-jurisdiction binding effect without explicit authority/agreement).

- Step 3: The initiative catches her eye (Section 9 Decision Provenance): the roll-up flags Riverbend Commons' newly committed initiative — the grad student's proposal — as changed since the last cycle. She opens its full Decision Provenance Packet (the same packet assembled at the end of 30.5) and can verify its legitimacy end to end without re-litigating Riverbend Commons' own decision.

- Step 4: Contribution-to-regional-goals check (Section 5.7 Objective Hierarchy, Section 18.4 Objective Functions and Public Value): she runs a regional objective-contribution analysis and sees the initiative's real, live contribution to shared regional objectives (e.g., a bioregion-wide ecological ceiling) alongside every other jurisdiction's committed portfolio.

- Step 5: Marginal analysis - 'where do I need to push, and how hard' (Section 18.6 Sensitivity and Marginal Analysis): she runs marginal/sensitivity analysis across the regional composite, surfacing which jurisdiction's binding constraint, if relaxed (e.g., additional regional co-funding), would most increase aggregate regional value — the same dual-value output the Optimization Engine already produces per jurisdiction, aggregated for regional comparison.

- Step 6: Coordination by proposition, not command (non-negotiable principle 4; Section 22.2): rather than directing any jurisdiction, she drafts her own Proposition — e.g., a regional co-funding offer — and routes it into the relevant jurisdiction(s)' own Governance Process(es). She has no unilateral authority to alter another jurisdiction's committed baseline; her proposal must be independently deliberated and approved locally.

- Step 7: Regional benefits-realization review (Section 21, Learning Plane): she reviews aggregated variance and benefits-realization across every federated jurisdiction for the cycle, including how the grad student's small initiative performed against its committed baseline.

- Step 8: Cycle close (Section 21.4): findings (e.g., 'small, community-originated initiatives are punching above their resource weight on regional ecological objectives') are captured as calibration input for the next cycle's regional objective weighting, proposed back through each jurisdiction's own governance rather than silently applied (non-negotiable principle 10).

### 30.6.4 New or Clarified Requirements Surfaced by This Journey

- Regional Observer role: a named Actor/Role (Section 7, alongside the existing Auditor/observer of 17.2) holding federation-scoped read authority across multiple Civic Bodies but zero commit authority in any one of them — broad visibility paired with narrow authority, by construction rather than by convention.

- Read-only Cross-PPM Stitch mode (Section 22.3): the existing stitching mechanism, explicitly usable in a non-authoritative 'observe and report' mode distinct from a joint-solve federation, so regional roll-up does not itself require or imply a shared optimization run.

- Cross-jurisdiction delta flagging (Section 21.2 Variance Taxonomy): the Learning Plane's variance taxonomy extended so a federation-scoped observer can be shown 'what changed since my last cycle' across every jurisdiction it watches, not only within one Civic Body.

### 30.6.5 Acceptance Criteria (JNY-AGCY-001..008)

- JNY-AGCY-001. Federate two Civic Bodies' read-only portfolio visibility to a regional Authority via a Federation Contract and confirm no commit authority is implied in either direction.

- JNY-AGCY-002. Produce a live regional roll-up (Cross-PPM Stitch, read-only mode) spanning both jurisdictions' current committed portfolios.

- JNY-AGCY-003. Confirm the roll-up flags the Riverbend Commons grad-student initiative as newly committed since the prior cycle snapshot.

- JNY-AGCY-004. Open that initiative's Decision Provenance Packet from the regional view and confirm every referenced object hash matches its historical snapshot (mirrors JNY-GRAD-010/MVP test 109).

- JNY-AGCY-005. Run a regional objective-contribution analysis and confirm the initiative's contribution is computed from live data, not a cached or manually entered figure.

- JNY-AGCY-006. Run regional marginal/sensitivity analysis and confirm it surfaces which jurisdiction's binding constraint most affects aggregate regional value.

- JNY-AGCY-007. Submit a regional co-funding Proposition into a jurisdiction's own Governance Process and confirm the regional Authority cannot commit it directly (invariants 2 (GOV-AUTHPATH-001) and 6 (FED-AUTH-001)).

- JNY-AGCY-008. Close a review cycle and confirm the resulting calibration note is routed back to each jurisdiction's own governance as a proposal, not applied silently (non-negotiable principle 10).

## 30.7 Journey: The Resident / Voter

Mass-Participation Awareness and Voice. This journey traces directly to the second of the project's five original 2019 "ACECOG Stories": a resident asking "What are my city/county/watershed planners working on? Show me what worries them, how it affects my community, and how I can help." It is also the journey that gives the Section 11.6.5 Resident mobile tier, and the Section 11.6.6 feed/notification-neutrality requirement, an end-to-end reference case, and it is where the Aspiring Grad Student's initiative (30.5) and the Agency Planning Manager's regional roll-up (30.6) become visible to the public they ultimately serve.

### 30.7.1 Persona & Motivation

A resident of Riverbend Commons with no governance role, no portfolio training, and no expectation of reading a Portfolio dashboard. She follows local civic matters the way most people do: casually, on a phone, between other things. She is not looking for authority over anything; she wants to know what is being decided that touches her neighborhood, whether it is trustworthy, and whether there is something small and concrete she can do about it.

### 30.7.2 Preconditions

Riverbend Commons is a participating Civic Body with an open Governance Process (Section 7). The resident has completed onboarding at the Provisional tier (23.1.1, invariant 13 (TRU-ELIG-001)) rather than a Documented or Verified identity, which is required only where a specific decision class demands it. The mobile Resident tier (Section 11.6.5) is her only surface; she never touches the desktop structured UI.

### 30.7.3 Step Sequence

- Step 1: Discovery via a neutral feed (Section 11.6.6): her mobile app surfaces open Propositions and votes scoped to her jurisdiction and geography, each carrying the visible reason it was shown (e.g., 'open for comment in your watershed, closes in 3 days') rather than an engagement-optimized ranking.

- Step 2: Plain-language framing (Section 24, AI Process Manager as a client per Section 11.6.4): she opens an item and reads an AI-drafted, plain-language summary of the Proposition, generated read-only from the same governed object a planner would see on desktop, not a separate or simplified copy of it.

- Step 3: Relevance to her community: the summary states, in concrete terms, what the proposition changes and where — e.g., that it affects the same regional ecological ceiling the Agency Planning Manager's roll-up (30.6) tracks, or that it is the small, community-originated initiative that the grad student proposed (30.5), now executing and reporting real variance (Section 21).

- Step 4: Expressing a voice (Section 17.3): with one tap, she registers consent, objection, or comment on the Proposition within her jurisdiction's participation rules — an act of participation, not a binding vote unless the Governance Process defines citizen input as such for that decision class (invariant 13 (TRU-ELIG-001) governs which decision classes require what standing).

- Step 5: Delegating for decisions she does not have time to track herself (Section 7, Delegation Envelope): she assigns a trusted delegate (e.g., a neighborhood association) for a defined decision class, and can revoke that assignment at any time from the same screen — the same revocable delegation model used for staff-level Delegation Envelopes, applied to a citizen's own standing rather than an agency's.

- Step 6: 'How can I help' (a concrete ask, not a slogan): where a Proposition has an attached, concrete need — a public-comment deadline, a volunteer role, a co-funding ask like the one the Agency Planning Manager proposed into Riverbend Commons' governance in 30.6 — the feed item surfaces it as a specific, boundable action, not a generic call to 'get involved.'

- Step 7: Verifying legitimacy without an account (non-negotiable principle 1): before or after acting, she can open the Decision Provenance Packet for any decision that affected her — the same packet the grad student's initiative produced in 30.5 — fully read-only and without registering, confirming the process was followed rather than taking it on faith.

- Step 8: Closing the loop: once a decision is committed and later measured (Section 21), she receives a neutrally-generated notification of the real-world outcome, tying her original one-tap expression of support back to a concrete, traceable result.

### 30.7.4 New or Clarified Requirements Surfaced by This Journey

- Plain-language Proposition summarization is added as a specified AI Process Manager output (Section 24.2), read-only and generated from the live governed object, not a hand-maintained separate description — and subject to the same AI-drafting-neutrality invariant (AI-NEUTRAL-001) already governing proposition drafting.

- Geographic/community relevance tagging is added to Portfolio Node and Proposition metadata (Section 5) so that 'what does this mean for my neighborhood' can be answered structurally rather than left to prose.

- Citizen-scoped Delegation Envelopes (Section 7) are confirmed to use the same revocable delegation model already specified for staff and agency roles, extended down to an individual resident's own decision-class standing, with the same visibility and audit trail (invariant 1 (DPP-IMMUTABLE-001)).

- A bounded 'concrete ask' attachment on a Proposition (a comment deadline, a volunteer role, a co-funding invitation) is added as a lightweight, optional structured field, so mobile feed items can surface a specific action rather than open-ended engagement language.

<!-- -->

- Onboarding never presents a cost or document barrier: a resident without an identity document is issued one ad hoc at no cost (invariant 24 (TRU-ACCESS-001)), and connectivity counts toward the Prosperity Floor where participation depends on it (PF-07).

### 30.7.5 Acceptance Criteria (JNY-CIT-001..007)

- JNY-CIT-001. Confirm a citizen's mobile feed item and its plain-language summary are generated from the same live governed Proposition a desktop user would see, with no separate or divergent copy.

- JNY-CIT-002. Confirm every feed item and push notification displays the reason it was surfaced, and that no exposed setting can reorder, delay, or hide items for engagement (mirrors UIX-NEUTRAL-003).

- JNY-CIT-003. Register a citizen consent/objection on a Proposition via one-tap mobile action and confirm it is recorded against the correct decision class and participation rule for that jurisdiction.

- JNY-CIT-004. Assign a citizen-scoped Delegation Envelope to a delegate, confirm the delegate's action is correctly attributed and bounded, then revoke it and confirm the delegate is immediately unable to act on the citizen's behalf.

- JNY-CIT-005. Attach a concrete ask (e.g., a comment deadline) to a Proposition and confirm it renders as a specific, boundable action in the citizen's feed rather than generic text.

- JNY-CIT-006. Open a Decision Provenance Packet from the citizen mobile surface without any account and confirm every referenced object hash matches its historical snapshot (mirrors JNY-GRAD-010).

- JNY-CIT-007. Commit and later measure a Proposition the citizen expressed support for, and confirm she receives a neutrally-generated outcome notification tracing back to her original expression.

## 30.8 Journey: The City Manager

Delegated Execution, Exception Handling, and Accountability to the Elected Body. Where the Agency Planning Manager (30.6) observes across jurisdictions with no commit authority, the City Manager sits inside one jurisdiction with real, delegated commit authority — the day-to-day executive who runs the committed Portfolio between the elected Governance Process's own deliberative cycles, and who is accountable back to it. This journey is where the system's core authority-gating invariants (Section 14; invariants 2 (GOV-AUTHPATH-001), 6 (FED-AUTH-001) and 7 (GOV-ENVELOPE-001)) are exercised continuously by a human executive, not only by automated checks.

### 30.8.1 Persona & Motivation

The chief appointed executive of Riverbend Commons, holding a broad but explicitly bounded Delegation Envelope (Section 7) granted by the elected Governance Process (the Council). She is not a planner and not a citizen; she is accountable for the jurisdiction's whole committed Portfolio day to day, and for knowing precisely which decisions are hers to make and which must go back to the Council. She wants one command view across every department and program, an exception queue she can trust, and a clean, defensible record to bring to the Council.

### 30.8.2 Preconditions

Riverbend Commons' Governance Process has granted the City Manager a standing Delegation Envelope (Section 7) bounding which decision classes and variance thresholds she may resolve unilaterally versus escalate. The jurisdiction's committed Portfolio already includes the grad student's executing initiative (30.5) and any regional co-funding proposition arising from the Agency Planning Manager's cycle (30.6); both are ordinary line items in her portfolio view, not special cases.

### 30.8.3 Step Sequence

- Step 1: Single command view (Section 11.6.3 desktop structured surface): she opens a consolidated portfolio dashboard spanning every department and program under Riverbend Commons' Governance Process — the same underlying committed Portfolio Nodes the grad student's and other initiatives all belong to, not a separate departmental export.

- Step 2: Exception queue triage (Section 5.11 Exception Proposition, Evidence Engine classify_variance): she reviews a queue of raised exceptions, each already classified as within-tolerance, delegated-rebalance-eligible, or hard-constraint-breaching by the same evidence/variance logic used everywhere else in the system.

- Step 3: In-envelope resolution (Section 7, invariant 7 (GOV-ENVELOPE-001), check_delegation_envelope): for a variance her Delegation Envelope covers, she approves a delegated rebalance directly — the same execute_delegated_rebalance path already specified, exercised here by a human executive rather than an automated policy.

- Step 4: Escalation, not override (invariant 2 (GOV-AUTHPATH-001), invariant 6 (FED-AUTH-001)): for a variance that breaches a hard constraint or exceeds her envelope, she cannot resolve it unilaterally. The system routes it as a new Proposition into the Governance Process for the Council's own deliberation — mirroring the Agency Planning Manager's coordination-by-proposition pattern (30.6), applied to her own escalation path rather than to a peer jurisdiction.

- Step 5: Reviewing citizen engagement on a live initiative (30.7): before deciding how to handle a variance on the grad student's initiative, she can see the same neutrally-generated citizen feed activity and Decision Provenance a resident would see — one shared record of the initiative's history, not a separate management-only narrative.

- Step 6: Preparing the Council report (Section 21.4 continuous improvement cadence; non-negotiable principle 10): she assembles the jurisdiction's cycle-close report — committed portfolio status, resolved and escalated exceptions, benefits realized — directly from live Decision Provenance and Evidence records rather than a hand-built summary.

- Step 7: Accountability to the elected body: she presents the report to the Council, including every escalation she routed rather than resolved, closing the loop between delegated day-to-day execution and the deliberative authority that granted her envelope in the first place.

### 30.8.4 New or Clarified Requirements Surfaced by This Journey

- A cross-department/program Exception Queue view is added to the desktop structured surface (Section 11.6.3): one triage list of raised Exception Propositions across every Portfolio Node under a Civic Body's Governance Process, each pre-classified by the existing Evidence Engine variance taxonomy (Section 21.2).

- An explicit 'escalate' action is added alongside the existing 'resolve within envelope' action on any exception: escalation creates an Exception Proposition (5.11) routed into the Governance Process rather than silently blocking or retrying, giving invariant 2 (GOV-AUTHPATH-001)'s authority boundary a first-class UI affordance rather than only a backend refusal.

- A cycle-close accountability report is specified as a generated, not hand-authored, artifact: assembled from Decision Provenance and Evidence records for a defined Governance Process and period, so what a delegated executive reports to an elected body is provably the same record a citizen or auditor could independently reconstruct (Section 9).

### 30.8.5 Acceptance Criteria (JNY-MGR-001..007)

- JNY-MGR-001. Open a consolidated portfolio dashboard spanning multiple Portfolio Nodes under one Governance Process and confirm it reflects the same live committed state as each node's own view.

- JNY-MGR-002. Raise a variance that is delegated-rebalance-eligible and confirm the City Manager can resolve it directly via execute_delegated_rebalance, correctly checked against her Delegation Envelope (invariant 7 (GOV-ENVELOPE-001)).

- JNY-MGR-003. Raise a variance that breaches a hard constraint and confirm the system refuses unilateral resolution and instead creates an escalation Proposition into the Governance Process (invariant 2 (GOV-AUTHPATH-001)).

- JNY-MGR-004. Confirm an escalated Proposition is deliberated and resolved through the ordinary Governance Process path (Section 8), with no separate executive fast-path to committed state.

- JNY-MGR-005. Confirm the City Manager's view of a citizen-facing initiative's engagement and Decision Provenance is identical to what the Resident (30.7) sees for the same initiative.

- JNY-MGR-006. Generate a cycle-close accountability report from live Decision Provenance and Evidence records and confirm every figure in it traces to a specific, hash-verifiable object.

- JNY-MGR-007. Confirm every action available to the City Manager, however she reaches it, passes through the same require_authority/check_delegation_envelope checks as any other client (Section 11.6.1).

## 30.9 Journey: The Facilitator/Clerk

Process Administration Without Substantive Decision Authority. This entry resolves the first of the three personas the catalog previously carried as deferred (30.14 as of this version), specifying Section 17.2's process-administration role against the current object model. Its central point is architectural rather than narrative: a scribe role, human or artificial, never confers decision authority — the same boundary already enforced for the AI Process Manager (AI-COMMIT-001, Section 24.3) is enforced identically here for a human administrative role, by Authority scoping rather than job description.

### 30.9.1 Persona & Motivation

A process administrator (clerk) for Riverbend Commons' Governance Process: intakes submissions, schedules deliberation windows, tracks quorum feasibility, and ensures the record is published — all without ever casting a vote, approving a proposition, or committing a portfolio. She wants the process to run smoothly and be provably clean of her own influence over outcomes.

### 30.9.2 Preconditions

The clerk holds an Authority (Section 7) whose permitted_actions is limited to a distinct process-administration action set — validate_proposition, schedule_deliberation, publish_provenance — and explicitly excludes deliberate_and_approve, commit_portfolio, and execute_delegated_rebalance. This is the same require_authority chokepoint every other role uses, granted a narrower permitted_actions list rather than a different mechanism.

### 30.9.3 Step Sequence

- Step 1: Intake and structural validation: the clerk calls validate_proposition on new submissions — the existing structural check (non-empty body, known Civic Body, Section 8.3) — without judging their substance.

- Step 2: Scheduling and quorum tracking: the clerk monitors the eligible population (Membership Credentials, Section 7) against pending propositions and schedules deliberation windows so quorum is achievable, surfaced as a dashboard element on the desktop structured surface (11.6.3).

- Step 3: Record publication: the clerk ensures each cycle's CollectiveWill and Decision Provenance Packet are published and reachable per Section 23.2's transparency principle — a publication duty, not an authorship one; she never edits their content.

- Step 4: Authority-boundary test: the clerk attempts deliberate_and_approve directly and is refused by require_authority, identically to any other caller lacking that permitted action — demonstrating 17.2's 'without substantive decision authority' is enforced, not merely stated.

- Step 5: Anomaly escalation: on a structural anomaly outside her judgment (a submission from a revoked Membership Credential, a duplicate filing), the clerk raises it to the Governance Process rather than resolving it herself.

### 30.9.4 New or Clarified Requirements

- Authority.permitted_actions is confirmed to support a process-administration action set distinct from decision-class actions, so a clerk role can be granted the former without the latter as a first-class configuration, not an ad hoc restriction.

- A scheduling/quorum-feasibility dashboard element is added to the desktop structured surface (11.6.3) for the Facilitator/Clerk role.

### 30.9.5 Acceptance Criteria (JNY-FAC-001..006)

- JNY-FAC-001. Grant a clerk Authority scoped to validate_proposition, schedule_deliberation, and publish_provenance only, and confirm deliberate_and_approve and commit_portfolio both raise AuthorityError for that same Actor.

- JNY-FAC-002. Confirm the clerk can validate a structurally incomplete proposition to Remanded state without any vote having occurred.

- JNY-FAC-003. Confirm a scheduling view correctly reflects live eligible-population and quorum-fraction data rather than a cached count.

- JNY-FAC-004. Confirm every CollectiveWill and Decision Provenance Packet the clerk 'published' in a cycle is reachable read-only without her having authored any of its content.

- JNY-FAC-005. Confirm a clerk-raised anomaly is routed to the Governance Process rather than silently resolved by the clerk.

- JNY-FAC-006. Confirm the clerk's authority refusal (test 1) is identical in form to the refusal a human caller receives elsewhere in the system (mirrors MVP acceptance test 111's AI/human parity, applied to two human roles instead).

## 30.10 Journey: The Auditor

Independent Inspection Without Any Write Path. This resolves the second deferred persona, specifying Sections 12 and 23.2's inspection rights as an Authority configuration with zero write-capable permitted actions — a stronger and simpler case than the Facilitator/Clerk's partial administrative grant, since an Auditor is granted nothing beyond read access at all.

### 30.10.1 Persona & Motivation

An independent inspector — internal to no Civic Body's staff, and party to no Governance Process — conducting a periodic or triggered review of a Civic Body's decision integrity: did committed decisions actually follow the rules in force at the time, and does the event log show any sign of tampering or silent invariant violation.

### 30.10.2 Preconditions

The Auditor holds an Authority with an empty or read-only permitted_actions list — by construction, not merely by unused capability, she has no path to any store.put-triggering engine method. Riverbend Commons' full event log and object history are readable to her per Section 23.2's transparency-over-privacy default for public reasoning and material decision provenance.

### 30.10.3 Step Sequence

- Step 1: Scope definition: the Auditor selects a Civic Body, a decision, or a time window to inspect.

- Step 2: Integrity verification: she calls EventStore.verify_integrity() directly, confirming every stored object's hash matches its logged event (invariant 1 (DPP-IMMUTABLE-001)) across the selected scope.

- Step 3: Independent replay: she calls ProvenanceEngine.replay() on a sample of committed decisions — the same mechanism MVP acceptance test 109 exercises, performed here by a non-participant rather than the deciding body itself.

- Step 4: Authority-boundary confirmation: she attempts a write action (e.g., resolve_exception) and is refused identically to any unauthorized caller, confirming inspection rights never imply a write path.

- Step 5: Findings record: her findings (decisions sampled, integrity problems found if any, replay results) are themselves published as a lightweight structured record rather than an informal, untraceable read session — an audit that leaves its own trace.

### 30.10.4 New or Clarified Requirements

- A distinct Auditor Authority shape (empty or read-only permitted_actions) formalizes 12/23.2's 'inspection rights without any write path' as an enforced configuration rather than a policy statement civic-body operators must remember to honor.

- An audit-findings record (scope, decisions sampled, integrity result, replay result) is added as a lightweight structured output, distinct from a Decision Provenance Packet, so an independent review leaves a citable trace of its own.

### 30.10.5 Acceptance Criteria (JNY-AUD-001..006)

- JNY-AUD-001. Grant an Auditor an Authority with empty permitted_actions and confirm every commit-class engine method raises AuthorityError for that Actor.

- JNY-AUD-002. Run verify_integrity() over a Civic Body with no tampering and confirm zero problems are reported.

- JNY-AUD-003. Deliberately corrupt one stored object's recorded hash outside normal write paths and confirm verify_integrity() detects and reports it.

- JNY-AUD-004. Independently replay three committed decisions and confirm all three reproduce their original hashes without the Auditor's involvement in the original decisions.

- JNY-AUD-005. Confirm an Auditor's attempted resolve_exception call is refused identically to any other unauthorized caller.

- JNY-AUD-006. Confirm an audit-findings record is generated and independently readable, citing the specific decisions and results it covers.

## 30.11 Journey: The Federation Partner

A Second Jurisdiction's Own Delegate, Not a Regional Observer. This resolves the third deferred persona and is the direct counterpart to the Agency Planning Manager (30.6): where that role observes across many jurisdictions with no commit authority anywhere, a Federation Partner is a peer Civic Body's own representative, holding full commit authority inside their own jurisdiction, who engages Riverbend Commons only through a treaty-scoped Federation Contract (Section 22).

### 30.11.1 Persona & Motivation

A delegate of a second Civic Body — Willow Creek — with the same standing inside her own jurisdiction that a City Manager or Governance Process holds in Riverbend Commons. She wants her jurisdiction to coordinate with a neighbor on shared regional concerns without either jurisdiction surrendering any authority to the other.

### 30.11.2 Preconditions

Willow Creek and Riverbend Commons have each, through their own Governance Process, approved a Federation Contract (22.2) declaring a Tier A live-API relationship (22.5.2), the scope of shared visibility (22.3), and each jurisdiction's Maturity Framework mapping.

### 30.11.3 Step Sequence

- Step 1: Contract negotiation: entering the Federation Contract is itself an ordinary Proposition deliberated and approved through Willow Creek's own Governance Process — not a special federation-only procedure.

- Step 2: Shared visibility established: Cross-PPM Stitch, read-only mode (22.3), gives each party visibility into the other's committed portfolio to the extent the contract shares it.

- Step 3: Cross-jurisdiction proposition: the Federation Partner drafts a joint initiative (e.g., a shared regional resource) and routes it, independently, into both jurisdictions' own Governance Processes — coordination by proposition, not command (the same pattern as 30.6).

- Step 4: Conflict handling: a semantic or rights conflict surfaces (e.g., a joint coupling coefficient that would violate a mandatory objective in one jurisdiction, invariant 14 (FED-RIGHTS-001)) and is routed per 22.4's conflict taxonomy rather than resolved unilaterally by either party.

- Step 5: Independent ratification: each jurisdiction approves or rejects the joint proposal through its own governance; invariant 6 (FED-AUTH-001) guarantees neither party's approval binds the other.

- Step 6: Contract review and exit: Willow Creek can revoke the Federation Contract unilaterally at any time through its own Governance Process (17.5) — the exit right applies to federation membership itself, not only to data export.

### 30.11.4 New or Clarified Requirements

- A Federation Partner's Authority is confirmed scoped strictly to their own civic_body_id, never granting any Authority inside the partner jurisdiction — the cross-jurisdiction analog of invariant 23 (TRU-TENANT-001)'s platform-operator scoping (22.5.3): together the two cover both axes of 'who may hold authority into my governance.'

- Federation Contract revocation is confirmed as a unilateral action of the revoking Civic Body's Governance Process, requiring no counterparty consent, consistent with non-negotiable principle 4.

### 30.11.5 Acceptance Criteria (JNY-FED-001..007)

- JNY-FED-001. Establish a Tier A Federation Contract between two Civic Bodies and confirm each party's approval was reached through its own independent Governance Process.

- JNY-FED-002. Confirm the resulting Cross-PPM Stitch read-only view reflects both parties' live committed portfolios without granting either party write access to the other.

- JNY-FED-003. Submit a joint Proposition into both jurisdictions' Governance Processes and confirm approval in one jurisdiction has no binding effect in the other prior to that jurisdiction's own approval (invariant 6 (FED-AUTH-001)).

- JNY-FED-004. Construct a joint proposal that would violate a mandatory objective in one jurisdiction and confirm it is blocked per FED-RIGHTS-001 regardless of the other jurisdiction's preference.

- JNY-FED-005. Confirm a Federation Partner's Authority object is scoped to their own civic_body_id and grants no permitted_actions against the partner jurisdiction's civic_body_id.

- JNY-FED-006. Revoke the Federation Contract unilaterally through one party's Governance Process and confirm shared visibility ceases without requiring the counterparty's agreement.

- JNY-FED-007. Confirm a conflict deliberately introduced between the two parties' Maturity Framework mappings is routed per 22.4 rather than silently ignored.

## 30.12 Journey: The Fund Manager

Fiduciary Visibility Into Co-Invested Capital. This journey traces to the 2019 deck's third 'ACECOG Story': 'the smart civic-scale investments and the local ideas that deserve attention ... show me a high-performing portfolio that advances my investors' interests ... show me where I need to intervene.' It is specified honestly against the current object model, which means naming where it currently runs ahead of what is built: full fiduciary fund-tracking properly belongs to the Funding Instrument object (Section 7), whose Appropriation type is built in Phase 1 and whose other types are deferred to Phase 1.5+ (Section 26 'deferred depth'). The MVP's restricted-fund Constraint (26.1) is today's stand-in, and this journey is written against that stand-in rather than against capability that does not yet exist.

### 30.12.1 Persona & Motivation

The manager of an external or quasi-public capital vehicle (e.g., a green-bond or impact-investment fund) co-financing a subset of Riverbend Commons' initiatives. She is not a Civic Body member and holds no Authority inside its Governance Process; her standing is as a resource contributor with a fiduciary interest in how her fund's committed capital performs.

### 30.12.2 Preconditions

A subset of PortfolioNodes are tagged restricted-fund-eligible against the RESTRICTED_FUND_CAP constraint (26.1), standing in for her fund's actual contribution until the Funding Instrument object (7, extended in Section 40) is implemented in the MVP object model. She holds a read-only Authority scoped to that tagged node set.

### 30.12.3 Step Sequence

- Step 1: Fund-scoped visibility: she views only the PortfolioNodes her fund's capital touches (the restricted-fund-eligible set), not the Civic Body's full portfolio.

- Step 2: Performance tracking: she reviews actual-versus-committed Evidence (Section 20) for her tagged initiatives as they execute.

- Step 3: Early-warning threshold: a variance beyond a fund-specific materiality threshold generates a notification through the Notification/Subscription Service (11.6.7) scoped to her fund's node set.

- Step 4: Intervention by proposition, not command: she cannot pull remaining committed capital unilaterally — her fund's contribution is a Resource, not an Authority. She drafts a Proposition (e.g., 'suspend the remaining tranche pending remediation') routed into Riverbend Commons' own Governance Process.

- Step 5: Outcome review: she reviews the resulting decision's Decision Provenance Packet for her own fiduciary reporting.

### 30.12.4 New or Clarified Requirements

- Funding Instrument (Section 7; extended in v0.18 with Endowment, Collective Enterprise and Public Finance Institution subtypes, Section 40) is the long-term object for fund-scoped resource tracking, cost basis and disbursement tranches. It is specified but not yet implemented in the MVP object model, so the restricted-fund Constraint remains the interim, narrower stand-in rather than a permanent design choice.

- Fund-scoped notification thresholds are added as a Notification/Subscription Service configuration (11.6.7), keyed to a node set rather than a civic-body-wide subscription.

### 30.12.5 Acceptance Criteria (JNY-FUND-001..006)

- JNY-FUND-001. Grant a Fund Manager a read-only Authority scoped to the restricted-fund-eligible node set and confirm she cannot query or act on nodes outside that set.

- JNY-FUND-002. Ingest an actual for a fund-tagged node and confirm it is visible to the Fund Manager without exposing evidence for non-tagged nodes.

- JNY-FUND-003. Trigger a fund-specific materiality breach and confirm a notification is generated scoped to her subscription.

- JNY-FUND-004. Submit a Fund-Manager-drafted intervention Proposition and confirm it is deliberated through the ordinary Governance Process, with no direct path for the Fund Manager to alter a Commitment.

- JNY-FUND-005. Confirm the Fund Manager can open the Decision Provenance Packet for a decision affecting her fund's nodes.

- JNY-FUND-006. (Pending Funding Instrument implementation, Section 40) Confirm a fund's own disbursement tranches and cost basis are tracked as first-class fields rather than approximated via the restricted-fund Constraint; testable once Funding Instrument is implemented in the MVP object model (Phase 1.5, 13.2).

## 30.13 Journey: The Program Manager

Managing One Multi-Node Program, Honestly Scoped. This journey traces to the 2019 deck's fifth 'ACECOG Story': 'a mechanism to manage this effort across all key stakeholders ... show me the likelihood of success, given known uncertainties, risk events ... show me where this project ranks with my stakeholders.' It is scoped narrower than the City Manager (30.8, whole-jurisdiction exception authority) and deeper than the Aspiring Grad Student (30.5, a single simple initiative): one program with real sub-project structure, using PortfolioNode.parent_id (Section 7), a field the model already carries but no prior journey has exercised.

### 30.13.1 Persona & Motivation

The manager of a single large, multi-stakeholder program within Riverbend Commons — several sub-projects under one parent initiative, such as a phased flood-plain buyout with distinct acquisition, relocation, and restoration sub-projects. She needs a rolled-up view of her whole program, not just its individual line items, and an honest picture of where it is exposed to schedule or resource risk.

### 30.13.2 Preconditions

The program is modeled as a parent PortfolioNode with several child nodes referencing it via parent_id; each child carries its own cost, resource_demand, and duration_days like any other node. The Program Manager holds an Authority scoped to this node family.

### 30.13.3 Step Sequence

- Step 1: Program roll-up: she views an aggregated dashboard summing cost, resource demand, and schedule across the program's child nodes — a new 11.6.3 surface element built directly on PortfolioNode.parent_id.

- Step 2: Schedule and critical path: she runs run_cpm() across the program's sub-nodes exactly as already specified (Section 19.3), with no new engine required.

- Step 3: Risk and uncertainty, honestly framed: 'likelihood of success' is presented as which constraints are binding and how much slack remains (Section 18.6 marginal/sensitivity analysis) — not a stochastic risk simulation, which 13.2 and Section 26 defer.

- Step 4: Stakeholder ranking: she views her program's marginal contribution to the Civic Body's declared Objectives, the same mechanism the Agency Planning Manager uses for regional objective-contribution (30.6), applied here to one program within one jurisdiction.

- Step 5: Escalation on internal conflict: a sub-node slips its schedule or two sub-nodes compete for the same constrained resource; this is routed as an Exception Proposition (Section 8.9), the same pattern the City Manager's exception queue uses (30.8), scoped here to the program's own sub-nodes.

### 30.13.4 New or Clarified Requirements

- A program roll-up dashboard (aggregate cost/resource/schedule across a PortfolioNode's children) is added to the desktop structured surface (11.6.3), the first journey to exercise PortfolioNode.parent_id.

- 'Likelihood of success' is explicitly named as bounded to the MVP's deterministic tools (binding constraints, slack, marginal sensitivity) rather than stochastic risk simulation, which remains Section 18's deferred scope — an honest-framing clarification, not a new capability.

### 30.13.5 Acceptance Criteria (JNY-PROG-001..006)

- JNY-PROG-001. Construct a parent PortfolioNode with three child nodes and confirm the program roll-up correctly aggregates their cost, resource demand, and schedule.

- JNY-PROG-002. Run run_cpm() across the program's child nodes and confirm the critical path and slack values match a hand-computed forward/backward pass.

- JNY-PROG-003. Confirm the Program Manager's marginal-contribution view matches the Optimization Engine's own marginals_for() output for the same run, with no separately computed figure.

- JNY-PROG-004. Trigger a resource conflict between two sibling sub-nodes and confirm it is raised as an Exception Proposition scoped to the program rather than escalated civic-body-wide.

- JNY-PROG-005. Confirm the Program Manager cannot resolve a hard-constraint-breaching exception unilaterally, mirroring the City Manager's escalation boundary (JNY-MGR-003) at the program's scale.

- JNY-PROG-006. Confirm no 'likelihood of success' figure in the dashboard implies a probability the current engine does not actually compute (a documentation/labeling check, not a state-changing test).

## 30.14 Deferred Journeys (Catalog Reserve)

As of v0.17, all three personas previously carried here (Facilitator/Clerk, Auditor, Federation Partner) and both remaining personas from the 2019 deck's original five ACECOG Stories (Fund Manager, Program Manager) have been specified (30.9-30.13). This reserve is now empty of named entries; it remains open for future personas surfaced by continued use, authored against the Section 30.3 template before being pulled into a build phase, per the same phase-pull discipline used for the core specification (Section 13.5).

# Part V — Prosperity, Commons & Guardian Modules

# 31. Part V Integration

## 31.1 Purpose and Discipline

Part V specifies how a Civic Body develops shared prosperity, governs the commons it lives within, and secures a Prosperity Floor for every member. It realizes, at community and ecosystem scale, the economic and ecological interfaces that Part III already requires (29.14 Economic Architecture Interface, 29.15 Ecological Accounting) and the nested governance model of CMT FR-2.

Part V keeps the source modules' discipline unchanged: advisory-only authority, human approval before any commitment, provenance on every figure, hard gates before ranking, and no single opaque score. Its modules are expressed in ACECOG's canonical vocabulary so that there is one object model. Source input: *ACECOG Prosperity Transition Functional Specification* (concept draft v0.2), as amended in the 25 September 2026 design session (Appendix H).

## 31.2 Terms Introduced in Part V

| Term                               | Definition                                                                                                                                                                                                                                                       |
|------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Invariant floor                    | Existing term. The numbered invariants of Section 14, governing process integrity, amended only through the ACECOG Standards Process (14.1).                                                                                                                     |
| Prosperity Floor                   | A Civic Body's ratified substantive entitlement: the basic needs and services every member with standing receives. Access conditions are fixed by GOV-PROSPERITY-001; content and level are set by the Civic Body. Replaces the source document's "civic floor." |
| Guardian Jurisdiction              | A Jurisdiction whose defining scope is the stewardship of an ecosystem entity, with a fiduciary duty to that ecosystem. Informally, a "Lorax" jurisdiction. The guardian is the jurisdiction (or a critical part of its scope), not a committee inside one.        |
| Guardian module floor              | The minimum rules every Guardian Jurisdiction must adopt (Section 37.5). Everything above it is self-defined.                                                                                                                                                    |
| Ecosystem entity                   | The rights-holding ecosystem (forest, watershed, basin), represented as a legal person in the object model. Boundaries are layered and nested.                                                                                                                   |
| Commons Endowment (Sovereign Fund) | A Guardian Jurisdiction's perpetual fund, built from captured commons value and governed by the Guardian module floor. "Sovereign fund" is an accepted alias.                                                                                                    |
| Natural Capital Account            | The measured value of an ecosystem's stocks and flows, including value that has no market, kept on a separate ledger from the liquid fund.                                                                                                                       |
| Capitalized sustainable yield      | The portion of natural capital that counts toward the fund's market value: the sustainable annual yield of renewable and amenity flows, capitalized. "Spend the land's interest, never the land."                                                                |
| Ecosystem Share                    | The allocation to the ecosystem itself (instream flows, habitat, corridors, fallow), made before any human distribution.                                                                                                                                         |
| Statement of Relationship          | A Guardian Council's statement of its spiritual and cultural relationship to the land, authored with the peoples who hold ancestral ties to it.                                                                                                                  |
| Documented interdependence         | Certified, measured flows between ecosystems. The only basis for obligations between Guardian Jurisdictions (FED-SYMBIOSIS-001).                                                                                                                                 |

## 31.3 Term Mapping to the Canonical Model

| Source-module term                                  | Canonical ACECOG object                                                                         |
|-----------------------------------------------------|-------------------------------------------------------------------------------------------------|
| Authorized Civic Body / constituted human authority | Civic Body acting through its Governance Process                                                |
| Network agreement / intercommunity agreement        | Federation Contract (22.2) / Treaty, Compact, Agreement (7)                                     |
| Standing mandate / delegated authority              | Delegation Envelope                                                                             |
| Independent reviewer                                | Auditor role (30.10) and independent verification (14.1)                                        |
| Audit record / decision log                         | Decision Provenance Packet (9)                                                                  |
| Proposed policy change / revision proposal          | Proposition, or Exception Proposition where it departs from a rule (5.11)                       |
| Civic floor                                         | Prosperity Floor                                                                                |
| Protected minima / hard gates                       | Invariant-floor checks plus civic-body-ratified mandatory objectives and constraints (5.4, 5.7) |
| Service steward / project steward                   | Program Manager (30.13) or a steward role within a Delegation Envelope                          |

## 31.4 Relationship to CMT (Part III)

The Prosperity state vector (32.2) is the community-scale, economic resolution of the relevant CMT dimensions — principally Economy (En), Ecology (Ec), Resilience (R), Institutions (I) and Energy (E) — not a separate maturity ladder. Its 0–4 levels are specific to each dimension and reversible, matching CMT's rule that no dimension compensates for another (29.23). Where a Civic Body uses a self-defined Maturity Framework (4.3), prosperity levels map into it through the framework's interoperability declaration.

The Commons Endowment (36) implements 29.15's required distinction — resource stock → sustainable yield → actual extraction → regeneration rate — as accounting rules, and draws on 29.14's listed mechanisms (land value taxation, resource rents, commons management, cooperative enterprise, universal access to defined foundational commons). Guardian Jurisdictions (37) are an instance of CMT FR-2 nesting: higher layers never automatically supersede lower ones.

## 31.5 Traceability Prefixes

Part V adds the prefixes PT, SRBG, CAB, PF, CE, GJ, IA, LM and ECO to the Section 27 framework. They replace the source document's generic FR/SR/CA identifiers.

## 31.6 Module Interfaces

| Module                     | Owns                                                                                                                      | Provides to others                                          |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| Guardian Jurisdiction (37) | Layered boundaries, Guardian module floor, Council, consent and veto rights                                               | Ecological limits, condition certifications, ratified rules |
| Commons Endowment (36)     | Natural Capital Account, liquid fund, valuation, draw rule, Hartwick routing                                              | Dependable draw and yield, fund value                       |
| Indigenous Alignment (38)  | Statements of Relationship, consent processes, treaty-style participation, sacred sites, traditional ecological knowledge | Consent conditions and constraints, knowledge as evidence   |
| Prosperity Floor (35)      | The entitlement: content, access, mix of in-kind and cash                                                                 | Service requirements and costs                              |
| CAB (34)                   | Delivery, buffers, readiness, response, recovery                                                                          | Readiness status, gaps, replenishment needs                 |
| SRBG (33)                  | Contribution, exposure, benefit and settlement rules                                                                      | Ratified entitlements, funding duties, allocation rules     |
| Prosperity Transition (32) | Economic diagnosis, development portfolios                                                                                | Feasible portfolios, revenue ranges, distributional effects |
| Lifecycle Management (41)  | Cycle registry, review triggers, change control                                                                           | Scheduled reviews, drift signals                            |

## 31.7 Phasing

All Part V modules enter the catalog as Catalog Reserve / Phase 3 (13.4). They cover municipal economic development, public finance and emergency management — heavily institutional, regulated domains. Two items are pulled forward to Phase 1.5 (13.2): the Funding Instrument extensions (40), which unblock JNY-FUND-006 (30.12), and version 0.2 of the Ecosystem Endowment Simulator (42; version 0.1 is a standalone Phase 1 demonstration).

## 31.8 Open Decisions

Settled in the v0.18 design session: unconditioned floor access with ad hoc identity issuance; standing based on identity plus charter; no-cost participation; the guardian is the jurisdiction; binding veto within the guardian's own ecosystem and suspensive veto across boundaries; watershed as the default boundary unit, with layers; Hartwick routing; the land is never pledged; obligations between ecosystems only on documented interdependence, with no guarantee across ecosystems; four distinct modules (Guardian Jurisdiction, Commons Endowment, Indigenous Alignment, Prosperity Floor). Confirmed on 6 November 2026 (Appendix J), together with: the binding veto limited to certified ecological-limit breaches (37.4); the non-resident payer default (invariant 25 (GOV-VOICE-001)); a residency period for commons benefits set by each charter and capped at 12 months (CE-10); and a ratified draw band of 4–5% (CE-02).

Still open:

- Set the minimum momentum-reinvestment share.

- Define the certification method for documented interdependence (FED-SYMBIOSIS-001).

- Choose a legal-realization path per pilot state: easement trust, special district, compact or co-stewardship agreement.

- Carried from the source modules: consent model across different constitutional forms; floors and ecological boundaries; causal evidence standard for "ignition" and multiplier claims; whether fiscal and monetary instruments get their own module; smallest pilot geography and first data partners.

- Simulator v0.2 scope (42.5) and calibration data sources.

# 32. Prosperity Transition (PT)

## 32.1 Purpose and Boundaries

PT diagnoses a community's economic constraints, generates feasible development portfolios, stress-tests them, and presents tradeoffs to authorized decision makers. It has no autonomous policy authority: it never selects values, sets tax rates, commits funds, issues credit or overrides member sovereignty. A network-level recommendation that is unacceptable to a member under its own minimum conditions must be revised or rejected.

## 32.2 State Representation

Ten dimensions: essential provisioning, productive capacity, human capability, opportunity and distribution, capital and fiscal capacity, enterprise and institutions, land and ecology, trade and circulation, resilience and sovereignty, adaptation and innovation. Each carries a condition estimate, trend, uncertainty interval, evidence quality and affected population or place.

Levels run 0 Survival → 1 Dependency → 2 Ignition → 3 Autonomy → 4 Regeneration, per dimension and reversible; thresholds are locally calibrated. There is no overall score. "Ignition" is a diagnostic hypothesis about self-reinforcing activity, not a phase transition proven by a threshold.

## 32.3 Functional Requirements

| ID    | Requirement                                                                                                                                                                                                                                                                  |
|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PT-01 | Provenance: source lineage retained; missing or contradictory evidence shown; never infers precise conditions from absent data; assumptions and estimates visibly distinguished from observations                                                                            |
| PT-02 | Configurability: objectives, weights, non-negotiable thresholds, discounting, risk tolerance, horizon, acceptable network delegation; each change creates a new scenario version                                                                                             |
| PT-03 | Diagnose binding constraints from utilization, queues, prices, failure frequency and counterfactual sensitivity; report competing diagnoses when evidence cannot distinguish them                                                                                            |
| PT-04 | Dependency graph of essential inputs (supplier concentration, substitutes, reserve duration, lead time, shock propagation); flag critical services whose disruption breaches a protected minimum                                                                             |
| PT-05 | Pathway library with prerequisites, authority level, lead time, recurring cost, ecological load, beneficiaries, exit or renewal conditions                                                                                                                                   |
| PT-06 | Portfolio formation under budget, capacity, sequencing, legal, ecological, equity and sovereignty constraints, with complements and substitutes modeled explicitly — native to the PPM (5.3); requires multi-objective optimization beyond the MVP's linear program (28.1.2) |
| PT-07 | Stress tests across locally chosen adverse scenarios (resource shock, recession, migration, climate impact, credit interruption, network exit), with worst acceptable performance and failure modes                                                                          |
| PT-08 | Governance-scale recommendation; any upward delegation specifies scope, duration, oversight, dispute process and withdrawal terms                                                                                                                                            |
| PT-09 | Explain and authorize: Pareto short list, affected groups, reasons for inclusion or exclusion; Decision Provenance Packet on approval                                                                                                                                        |
| PT-10 | Monitor and learn: compare outcomes with forecasts and propose revise, continue, pause or retire; feeds Lifecycle Management (41)                                                                                                                                            |

## 32.4 Decision Rules and Acceptance

Hard gates apply before ranking: lawful and consented authority, protected essential services, ecological limits, fiscal solvency, privacy and explicit member conditions. Feasible portfolios are compared on the full outcome vector, and the recommended set keeps non-dominated options whenever value conflicts remain. The "public propulsion dependence" ratio is reported with a method note and never used as the sole trigger for withdrawing support.

Acceptance tests: PT-AT-01 housing bottleneck — a business subsidy alone cannot outrank a feasible housing-plus-labor package through assumed firm growth; PT-AT-02 critical import shock — a single fragile supplier reveals service breach and recovery time; PT-AT-03 network project — member costs, consent, exit and spillovers visible before approval; PT-AT-04 missing evidence — competing diagnoses plus an information-gathering action; PT-AT-05 policy reversal — an adverse outcome produces a documented review and revised proposal, preserving earlier decisions. Acceptance also requires reproducible rankings from the same data and settings.

# 33. Shared Risk and Benefit Governance (SRBG)

## 33.1 Purpose and Scope

SRBG sets and evaluates the terms under which people, enterprises and Civic Bodies contribute resources, bear exposure, share gains and exercise decision rights. It proposes arrangements and records authorized rules. It never infers consent from participation, equates wealth with authority, or turns a ranking into a binding agreement, and it identifies affected non-participants and cross-border harms as well as members.

## 33.2 Ledgers and Allocation Components

Separate ledgers for contributions, capacity to contribute, exposure borne, risk created, benefits received, decision rights and participation stability. Nonmonetary quantities stay distinct; converting them to money requires a stated method with sensitivity analysis. Missing records are evidence gaps, never proof of no contribution.

Three allocation components are recorded separately and never merged into one score:

- **Common entitlement:** the Prosperity Floor and the Ecosystem Dividend, per member.

- **Contribution-linked return:** including stewardship labor and host-community burdens.

- **Need-based support.**

## 33.3 Functional Requirements

| ID      | Requirement                                                                                                                                              |
|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| SRBG-01 | Register arrangements (versioned), marking benefits as guaranteed entitlements, contingent returns or discretionary distributions                        |
| SRBG-02 | Map contributions and burdens, with no double counting of a contribution as both upfront cost and continuing claim                                       |
| SRBG-03 | Configure allocation rules; the floor is never multiplied by a contribution score or reduced by a deductible (GOV-PROSPERITY-001)                        |
| SRBG-04 | Compare mutual, cooperative, public, private, commons and mixed arrangements; no ownership form is automatically preferred                               |
| SRBG-05 | Model incidence and incentives, including pass-through to prices, wages and rents, withdrawal of high-capacity contributors and strategic underreporting |
| SRBG-06 | Evaluate distribution by group, place and time; aggregate growth may not conceal a material uncompensated loss                                           |
| SRBG-07 | Ratify and publish a plain-language agreement, distribution statement and dissent record; restrict personal financial and vulnerability records          |
| SRBG-08 | Settle and reconcile; separate distributable surplus from revenue needed for commitments; the prototype issues instructions only                         |
| SRBG-09 | Resolve disputes with essential protection preserved throughout; flag and reassign conflicted reviewers                                                  |
| SRBG-10 | Adapt and exit; simulate exit before changing terms; past settlements are never rewritten (invariant 1 (DPP-IMMUTABLE-001))                              |

## 33.4 Safeguards and Acceptance

Creating preventable harm never earns a reward; a participant bearing exposure on behalf of others may be compensated. Funding schedules are tested for effective marginal burden: a small improvement in circumstances may never cost more than it gains.

Acceptance tests: SRBG-AT-01 zero contribution retains the floor; SRBG-AT-02 host-community exposure visible separately from its cash contribution; SRBG-AT-03 avoidable risk creation does not raise returns; SRBG-AT-04 a dividend violating reserve rules is blocked; SRBG-AT-05 a contribution appeal does not suspend protection; SRBG-AT-06 obligations remain visible after a member exits. No single fairness index substitutes for these views.

# 34. Civic Assurance and Buffering (CAB)

## 34.1 Purpose and Authority

CAB is the delivery and buffering engine beneath the Prosperity Floor. It turns the ratified floor into funded services and maintained response capacity, reports what can actually be delivered, and never quietly lowers an entitlement to balance a budget. ACECOG has no inherent emergency powers; CAB interoperates with NIMS/ICS incident-management roles rather than inventing parallel ones.

## 34.2 Buffers and Readiness

Buffers are financial, physical, human, ecological and network, each with its own observations. Cash and stocks are complementary, never interchangeable. Stale inventory is flagged, never assumed available. Readiness states: proposed → funded but incomplete → operationally verified → breached (requiring recovery).

## 34.3 Functional Requirements

| ID     | Requirement                                                                                                                                                                                                                                  |
|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CAB-01 | Specify the floor as measurable service requirements; no premium, contribution or deductible field in access logic                                                                                                                           |
| CAB-02 | Forecast routine and disrupted demand; separate the need for liquidity from the need for sustained physical provisioning                                                                                                                     |
| CAB-03 | Size buffers for chosen scenarios, accounting for spoilage, maintenance, mobilization delay and correlated failure; no universal reserve percentage is assumed                                                                               |
| CAB-04 | Verify readiness: cash without deliverable capacity fails; partners hit by the same shock are not counted at full nominal assistance                                                                                                         |
| CAB-05 | Funding plan from authorized sources (Section 39); insurance and contingent borrowing only as supplements, never as household premiums                                                                                                       |
| CAB-06 | Compare protection portfolios; transfers between civic accounts are not new resources                                                                                                                                                        |
| CAB-07 | Activate a response through ratified criteria; routine actions within a standing Delegation Envelope need no new vote; the prototype simulates orders only                                                                                   |
| CAB-08 | Deliver and appeal through digital and offline routes; provisional assistance when documentation is missing                                                                                                                                  |
| CAB-09 | Recover and replenish, with a dated, costed restoration plan returned to PT and SRBG                                                                                                                                                         |
| CAB-10 | Audit and adapt; record breaches rather than redefining the floor after an event                                                                                                                                                             |
| CAB-11 | Report a commitment as operationally verified only after its resources, providers, dependencies and activation arrangements pass readiness checks; otherwise return an explicit gap (CAB-HONEST-001, an Invariant Floor entry through v0.19) |

## 34.4 Budget Order, Scarcity and Acceptance

Budget order (per Section 36): Ecosystem Share → Prosperity Floor → stewardship → buffer replenishment → dividend → momentum reinvestment. Any departure requires a recorded governance decision stating the interim exposure and replenishment obligation. The charter predefines triage for extreme events; contribution levels or ownership never set emergency priority, and anyone receiving less than the floor is recorded with a restoration plan.

Acceptance tests: CAB-AT-01 premium-free access; CAB-AT-02 cash without capacity produces a readiness failure; CAB-AT-03 correlated shock discounts partner assistance; CAB-AT-04 contribution dispute does not block delivery; CAB-AT-05 insufficient capacity reports a breach and applies authorized priorities; CAB-AT-06 drawdown creates a dated replenishment requirement; CAB-AT-07 missing documentation follows provisional-assistance rules. Simulated success does not certify real operational readiness.

# 35. Prosperity Floor (PF)

## 35.1 Purpose

The Prosperity Floor is the entitlement itself: what every member with standing receives, unconditionally. CAB delivers it, SRBG sets its funding duties, and the Commons Endowment is one of its funding sources, never the only one. The floor's existence never depends on the endowment's performance.

## 35.2 Functional Requirements

| ID    | Requirement                                                                                                                                                                                                                          |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PF-01 | Each Civic Body ratifies the floor's content and level: services (water, food, energy, shelter, care, connectivity, livelihood continuity) and any cash component                                                                    |
| PF-02 | Access conditions are fixed by GOV-PROSPERITY-001: unique identity plus charter-defined standing, with ad hoc identity issuance (via Membership Credential, 7) and provisional access                                                |
| PF-03 | In-kind first: the floor states what the land and collective infrastructure provide directly (community energy, water governed like an acequia, housing on community-held land, local food); only the remainder becomes a money need |
| PF-04 | Funding is drawn from multiple sources: lawful general revenue, the Commons Endowment draw, collective-enterprise returns and agreed transfers                                                                                       |
| PF-05 | Sanctions, disputes and contribution enforcement never suspend floor access (invariant 18 (GOV-GRADUATED-001); GOV-PROSPERITY-001)                                                                                                   |
| PF-06 | Shortfalls are recorded as breaches with a restoration plan (invariant 9 (OPT-NONCOMP-001)); the floor is never quietly redefined                                                                                                    |
| PF-07 | Connectivity is part of the floor wherever participation (invariant 24 (TRU-ACCESS-001)) depends on it; municipal broadband is a named delivery path (11.6.7)                                                                        |
| PF-08 | Standing is portable between Civic Bodies only through Federation Contract terms                                                                                                                                                     |

## 35.3 Design Intent and Acceptance

The floor and the land's bounty secure basic needs; people's work, freed from fear, produces comforts and momentum; stewardship labor is recognized through SRBG contribution-linked returns.

Acceptance tests:

- PF-AT-01 A member with no payment history receives the full floor.

- PF-AT-02 A member under sanction retains the floor.

- PF-AT-03 A person without documents is issued an ad hoc identity and receives provisional access the same day.

- PF-AT-04 A means-tested co-pay fallback is rejected as an GOV-PROSPERITY-001 violation (modeled on New Mexico's universal child care funding bill, SB 241, which as passed by the state Senate on 12 February 2026 requires co-pays for families above 600% of the federal poverty level when economic triggers such as falling oil prices signal decline; final enactment to be confirmed).

## 35.4 Prosperity Module Floor

These rules bind every Civic Body that adopts a Prosperity Floor (14.2).

- **GOV-PROSPERITY-001.** Access to a Civic Body's ratified Prosperity Floor depends only on unique-identity assurance and charter-defined standing; it is never conditioned on premiums, deductibles, contribution history, project ownership, sanctions or pending disputes. Standing may rest on residence, affiliation or membership, never on payment. The Civic Body sets the floor's content and level; ACECOG fixes only the access conditions. Where identity is not yet established, provisional access applies rather than refusal; identifiers are pseudonymous and specific to each Civic Body. (Numbered 53 on the Invariant Floor through v0.19.)

- **PF-F2.** Changes to charter standing apply prospectively only. They never remove an existing member's standing; standing ends only individually, through due process.

# 36. Commons Endowment — Sovereign Fund (CE)

## 36.1 Purpose and Premise

The Commons Endowment turns what the land provides — energy, minerals, renewables, beauty — into a perpetual fund belonging to the ecosystem and all its members, present and future. Its founding premise, carried as the system's starting assumption and measured honestly in each place, is that the land is bountiful and provides for all who walk, crawl, swim, fly or slither across it.

## 36.2 Two Ledgers

- **Natural Capital Account:** all stocks and flows, including non-market value, maintained on the UN SEEA Ecosystem Accounting standard (2021). It guides stewardship and signals whether the land is thriving. It is never spent directly.

- **Fund market value:** liquid principal plus the capitalized sustainable yield of renewable and amenity flows. As ecological condition improves, certified yield rises and the draw can rise with it.

## 36.3 Three Kinds of Abundance

| Class           | Examples                                   | Treatment                                                                   |
|-----------------|--------------------------------------------|-----------------------------------------------------------------------------|
| Flows           | Sun, wind, water cycle, ecosystem services | Perpetual; distributable yield                                              |
| Stocks          | Hydrocarbons, hardrock minerals            | Finite; 100% of captured rent to principal (GOV-COMMONS-001)                |
| Non-rival gifts | Beauty, knowledge                          | Grow when shared; degrade with overuse or fire; yield scales with condition |

## 36.4 Functional Requirements

| ID    | Requirement                                                                                                                                                                                                                                          |
|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CE-01 | Capture commons value only through lawful mechanisms: severance and royalty shares, trust-land revenue, land value capture, resource rents, renewable leases or community ownership shares, visitor and access fees, payments for ecosystem services |
| CE-02 | Rule-based percent-of-market-value draw on a trailing average (default 5% over 5 years, within a ratified band of 4–5%); changes only through a ratified process                                                                                     |
| CE-03 | Valuation certified conservatively by the independent Science and Monitoring Commission (37.3); valuation changes flow through the trailing average                                                                                                  |
| CE-04 | Budget order: Ecosystem Share → Prosperity Floor → guardian stewardship → buffer → dividend → minimum momentum reinvestment                                                                                                                          |
| CE-05 | Equal per-member Ecosystem Dividend; collective conditions (certified ecological condition) scale its size only (GOV-COMMONS-002)                                                                                                                    |
| CE-06 | Every diversion of the draw from the budget order is recorded as a visible breach (the Alaska lesson, 40.3)                                                                                                                                          |
| CE-07 | Skipped inflation-proofing is recorded as an obligation owed to principal                                                                                                                                                                            |
| CE-08 | No pledging or securitizing of ecosystem assets (ECO-COLLATERAL-001)                                                                                                                                                                                 |
| CE-09 | Audited, public accounts every cycle                                                                                                                                                                                                                 |
| CE-10 | Residency period for standing in commons benefits is set by each charter and never exceeds 12 months; standing otherwise follows GOV-PROSPERITY-001                                                                                                  |
| CE-11 | Ratified investment policy statement for the endowment, reviewed on the Lifecycle Management cycle                                                                                                                                                   |
| CE-12 | Related-party transactions prohibited unless ratified with full disclosure                                                                                                                                                                           |
| CE-13 | Every fee paid by the endowment disclosed in the audited public accounts (CE-09); fund managers are covered by the Fund Manager journey (30.12)                                                                                                      |

## 36.5 Scale Note

At \$20,000 per year and a 5% draw, funding basic needs entirely in cash would require about \$400,000 of principal per person; Alaska's fund is about \$125,000 per resident. The vision becomes reachable through PF-03: in-kind provisioning shrinks the money need, and the fund covers only what the land cannot provide directly.

## 36.6 Commons Module Floor

These rules bind every Civic Body that adopts the Commons Endowment (14.2).

- **GOV-COMMONS-001.** Rents from nonrenewable depletion go to protected principal; only the rule-based draw and sustainable renewable or amenity yield may be distributed, and no distribution may depend on exceeding ecological limits. (Numbered 55 on the Invariant Floor through v0.19.)

- **GOV-COMMONS-002.** Conditions on commons benefits are collective and set through the Governance Process; they may change the size of a dividend and never an individual's access to anything. (Numbered 56 on the Invariant Floor through v0.19.)

- **ECO-COLLATERAL-001.** No ecosystem asset, and no claim on its in-place value, may be pledged as collateral or securitized. (Numbered 60 on the Invariant Floor through v0.19.)

- **CE-F4.** The Science and Monitoring Commission (37.3) certifies how each revenue stream is classified (stock, flow, or non-rival gift; 36.3) alongside its valuation. Reclassification is a recorded decision at the harder threshold of invariant 21 (GOV-RATCHET-001).

- **CE-F5.** Changes to charter standing apply prospectively only, as in PF-F2 (35.4).

- **CE-F6.** The endowment belongs to the ecosystem it stewards. A member jurisdiction that leaves a Guardian Jurisdiction takes no share of principal. Its obligations continue through a handoff period of one full funding cycle, during which it transfers records and stewardship duties. Money already committed keeps its status; only the delivery agent changes if needed. If the Guardian Jurisdiction dissolves, its assets pass to a successor steward for the same ecosystem, never to members. (CL-030)

# 37. Guardian Jurisdiction (GJ) and the Guardian Module Floor

## 37.1 Principle

The forests are sovereign. Each ecosystem entity is governed by a Guardian Jurisdiction: the jurisdiction itself, or a critical part of its scope, holding a fiduciary duty to the ecosystem and to future generations. Guardian Jurisdictions have their own module floor (37.5); their guidance and criteria above that floor are self-defined.

## 37.2 Layered Boundaries

Jurisdictions nest by subsidiarity (CMT FR-2), from forest stand or acequia scale, through watershed, to basin and bioregion. The default unit is the watershed; a charter may choose an ecoregion instead. A higher layer sets conditions only for effects that cross boundaries.

## 37.3 Organs of the Jurisdiction

A hybrid of the Mar Menor three-part structure and fiduciary trust practice:

- **Guardian Council:** governs, with a fiduciary duty to the ecosystem. Tribal nations with ancestral ties hold seats by treaty-style acceptance, never by appointment. Dividend recipients never hold a majority (ECO-GUARD-002).

- **Science and Monitoring Commission:** independent; certifies ecological condition and endowment valuation (ties to invariant 17 (TRU-MONITOR-001)).

- **Member Assembly:** the human constituency. It has a voice, receives the dividend and carries out stewardship.

## 37.4 Powers

- Binding veto over any action that would breach a certified ecological limit within its own ecosystem. The binding veto does not extend to objections resting on anything other than a certified limit; those follow the ordinary Governance Process.

- Suspensive veto over effects that cross boundaries, forcing escalation to the next layer and a public decision record. The veto lapses once the next layer decides or a fixed period set in the charter passes; repeated suspensive vetoes on the same matter count toward cumulative-exception review (invariant 16, GOV-CUMULATIVE-001).

- Standing to object to any proposition affecting it, through the Federation Contract's externality-exposed objectives field (22.2).

- Trusteeship of the Commons Endowment (36).

## 37.5 Guardian Module Floor

Derived from the Alaska Permanent Fund, drawing on both its successes and its failures (40.3):

1.  **Common ownership:** the endowment belongs to the ecosystem and all members, present and future (after Alaska Constitution Article VIII).

2.  **Protected principal:** 100% of nonrenewable rent to principal (GOV-COMMONS-001); Alaska protects 25%.

3.  **Rule-based draw,** changeable only through ratification.

4.  **Floor first, and no silent overrides:** every diversion is recorded as a breach.

5.  **Intergenerational equity:** real value is preserved; skipped inflation-proofing is recorded as owed.

6.  **Ecological hard gate and funding independence** (ECO-GUARD-001); extraction pauses below the condition threshold.

7.  **Relationship to the land:** a Statement of Relationship, authored with the peoples who hold ancestral and spiritual ties (38).

8.  **Independent science and audited public accounts.**

9.  **Equal per-member dividend,** changed in size only by collective conditions.

10. **Minimum momentum reinvestment** of every surplus.

These rules are also part of the Guardian module floor (14.2):

- **ECO-GUARD-001.** Every ecosystem entity is governed by a Guardian Jurisdiction whose fiduciary duty runs to the ecosystem and to future generations; the jurisdiction's stewardship functions are never funded from current extraction rents in that ecosystem. (Numbered 57 on the Invariant Floor through v0.19.)

- **ECO-GUARD-002.** Dividend recipients may never hold a majority of a Guardian Council. (Numbered 58 on the Invariant Floor through v0.19.)

- **ECO-GUARD-003.** A Guardian Jurisdiction's standing may be reduced or revoked only through a ratified process, and any revocation remains visible in the federation record. (Numbered 59 on the Invariant Floor through v0.19.)

- **FED-SYMBIOSIS-001.** Obligations between Guardian Jurisdictions arise only from documented, certified interdependence (flows of water, sediment, air, fire risk, species, energy, food or visitors); transfers are exchanges proportional to those flows, never unconditional guarantees. Voluntary solidarity remains permitted. (Numbered 61 on the Invariant Floor through v0.19.)

- **GJ-F1 Council selection and accountability.** Guardian Council seats are filled under a charter process the Member Assembly ratifies, with tribal seats taken up by acceptance (IA-04). Councillors serve fixed terms and may be recalled for breach of fiduciary duty through independent review. The Council publishes an auditable annual fiduciary report.

- **GJ-F2 Commission independence.** Members of the Science and Monitoring Commission are not appointed by the Guardian Council, and each files an Interest Declaration in every jurisdiction. Each certified limit records its method, uncertainty, and a review date, and lapses unless re-certified.

- **GJ-F3 Appeal of a binding veto.** A binding veto may be appealed on certification grounds (method or data) to an independent technical review, never on the merits.

Above the floor, self-defined: draw rate within the ratified 4–5% band (CE-02), dividend versus service mix, stewardship priorities, ceremony and practice, council procedure.

## 37.6 Obligations Between Ecosystems

Treaties rest on documented interdependence — the real reasons people settle downstream (precedent: the Delaware River Basin Commission). Terms are proportional to measured flows: downstream pays upstream for services received, and upstream takes on duties in proportion to the harm it could cause (FED-SYMBIOSIS-001). There is no guarantee across ecosystems; differences in endowment show up in the dividend, never in floor access.

## 37.7 Legal Realization and Acceptance

US law does not generally recognize ecosystem personhood (the Toledo Lake Erie Bill of Rights was struck down in 2020). Inside ACECOG, personhood operates as a governance construct among adopting Civic Bodies; legal force comes from existing tools — conservation easements held by a guardian trust, the public trust doctrine, interstate compacts, tribal co-stewardship agreements, special districts and water funds. This is the same external-integration boundary named in 28.1.2.

Acceptance tests:

- GJ-AT-01 An extraction proposal that would breach limits is blocked by binding veto.

- GJ-AT-02 An upstream proposal affecting a downstream jurisdiction triggers a suspensive veto and escalation.

- GJ-AT-03 A Council composition with a beneficiary majority is rejected.

- GJ-AT-04 A revocation of standing appears in the federation record.

# 38. Indigenous Alignment (IA)

## 38.1 Principle

Every Guardian Council must consider and honor the spiritual relationship with the ecosystems and geology of the land it stewards. ACECOG requires that the relationship be honored; the peoples who hold it define its content, so that no single cosmology is imposed on all. The module also honors governance traditions in which women held real authority, such as Haudenosaunee clan mothers and the matrilineal systems of the Hopi, Zuni, Keres Pueblos and Diné.

## 38.2 Functional Requirements

| ID    | Requirement                                                                                                                                                                                                                                                          |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IA-01 | Statement of Relationship: each Guardian Council adopts one, authored with the peoples who hold ancestral and spiritual ties to the land, and reviews it on the Lifecycle Management cycle                                                                           |
| IA-02 | Free, prior and informed consent of the peoples concerned for any action affecting sacred sites or culturally significant places                                                                                                                                     |
| IA-03 | Tribal sovereignty: a tribal nation's resource estate is never enclosed by drawing a boundary around it; it participates only by treaty-style Federation Contract                                                                                                    |
| IA-04 | Guaranteed Council seats for nations with ancestral ties, taken up by acceptance, never by appointment                                                                                                                                                               |
| IA-05 | Traditional ecological knowledge is an evidence class (20.1), governed by the CARE principles for Indigenous data governance: it counts as evidence, and the people who hold it control its use                                                                      |
| IA-06 | Durability: co-management arrangements rest on the most durable legal basis available (statute, compact, treaty), never on executive discretion alone                                                                                                                |
| IA-07 | Consent is recorded only as an act of the nation’s own governing body, with that body’s record reference; silence or non-response never counts as consent; consent is revocable on the nation’s terms; no AI summary may characterize a nation’s position as consent |

Evidence for IA-06: the Bears Ears Commission (2016) gave the Hopi, Navajo, Ute, Ute Mountain Ute and Zuni nations management authority. A presidential proclamation on July 13, 2026 (Proclamation 11043, 91 FR 45169) cut the monument from about 1.36 million acres to about 121,096, a reduction of about 91%, and disbanded the Commission, without the promised consultation (checked at Gate 1, 9 November 2026).

# 39. Collective Funding Rules

ACECOG never holds the power to compel payment. Only a body with lawful taxing authority can compel. ACECOG models the funding plan, hosts the deliberation, records the obligation and traces it to that authority; it never levies and never enforces.

- **Voluntary networks cannot compel.** They fund themselves through voluntary contributions, asset returns, grants and transfers; under invariant 24 (TRU-ACCESS-001) they may not charge dues as a condition of participation.

- **Federation obligations work like treaties.** They bind a member only after that member ratifies them, and withdrawal terms stay intact.

- **Separation:** collection and enforcement never touch floor access or participation; enforcement uses the jurisdiction's ordinary legal tools outside ACECOG.

- **Authority provenance:** every obligation traces to a legal authority and a ratification event; an untraceable obligation does not exist in the ledger.

- **Capacity-based schedules with no cliffs:** SRBG's marginal-burden test (33.4) is an acceptance criterion.

- **Incidence transparency:** each proposal shows who ultimately pays after pass-through to rents, prices and wages.

- **Floor funding first,** per the budget order in Section 36.

- **Voice,** per invariant 25 (GOV-VOICE-001): non-resident payers have standing on the obligations they pay.

Pilot constraint: Colorado's TABOR amendment requires voter approval for new taxes or tax increases and caps revenue growth. A Colorado pilot therefore allocates existing appropriations, or prepares a ballot measure, and never creates a levy through ACECOG. New Mexico and Arizona have their own constraints.

# 40. Funding Instrument Extensions and Regional Precedents

## 40.1 Three Part V Subtypes

Funding Instrument already exists as a canonical object (7) with three MVP types (5.13: Appropriation, Fixed-Rate Debt, Restricted Grant). Part V adds three subtypes alongside them:

| Subtype                               | What it does                                                   | Governing rules                                                                                       | Closest precedent                                                                                       |
|---------------------------------------|----------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| Endowment (incl. Ecosystem Endowment) | Protected principal, rule-based draw                           | GOV-COMMONS-001 and ECO-COLLATERAL-001; CE-02 to CE-07                                                | Alaska Permanent Fund; New Mexico Land Grant Permanent Fund and Early Childhood Education and Care Fund |
| Collective Enterprise                 | Services delivered in kind plus modest returns                 | SRBG-04; returns enter the income pool                                                                | Colorado Springs Utilities; Longmont NextLight fiber                                                    |
| Public Finance Institution            | Lending that lowers cost of capital and continues in downturns | Lending decisions through Delegation Envelopes with Decision Provenance and independent credit review | Bank of North Dakota                                                                                    |

## 40.2 Ecosystem Endowment Fields

Boundary definition (nested watershed or ecoregion); asset register (mineral, water, land, ecological services); capture mechanisms and the legal authority for each; draw rule; ecological condition gate; distribution rule; Ecosystem Share.

## 40.3 Evidence From Regional and National Precedents

- **Alaska Permanent Fund:** \$91.9B at June 30, 2026; 12.42% return; \$3.8B draw in FY26 (APFC, 2 September 2026); inflation-proofing skipped (an estimated \$1.5B). The 2026 dividend was \$1,000 plus a \$200 energy relief payment (paid from 1 October 2026), against a statutory formula amount of about \$3,800. The endowment worked; the floor did not hold, because it shares an appropriation pot with the rest of the budget.

- **New Mexico:** the Early Childhood Education and Care Fund (~\$11B, fed by surplus oil and gas tax revenue) pays at least \$500M a year and, with Land Grant Permanent Fund distributions, funds universal child care — the Alaska mechanism paid out as services. In October 2026 a legislative economist urged slowing withdrawals to protect the fund.

- **Arizona:** the Permanent Land Endowment paid \$641.9M to schools in FY2026 (not re-verified at Gate 1).

- **Colorado:** the State Land Board manages about 2.85M surface acres and earned \$316M for beneficiaries in FY2024–25, but the Public School Permanent Fund held only \$1.8B.

- **Collective infrastructure:** Longmont's NextLight network (about \$45M in bonds authorized, launched 2014, with a take rate of about 51% of the households it passes); Colorado repealed its municipal-broadband restriction (SB 152) in 2023; Boulder spent about \$29M on electric municipalization and settled with Xcel in 2020. Lesson: building new works; acquiring an incumbent is costly and slow.

- **Public banks:** the Bank of North Dakota earned \$231.8M on \$10.7B in assets in 2025, rated A+, partnering with community banks. San Francisco's Proposition B (November 3, 2026) would authorize a city nonprofit lender that could later seek bank status; it provides no startup capital, and the city controller estimates \$310–460M over eight years. Early returns showed it trailing; as of 8 November 2026 the certified result was pending; New Mexico's state bank bills stalled. Barriers: deposit-insurance limits, Federal Reserve access, capitalization, political insulation — the last of which ACECOG's provenance and authority limits directly answer.

# 41. Lifecycle Management and Shared Planning

## 41.1 Lifecycle Management

Lifecycle Management is specified as a generalization of mechanisms ACECOG already has, not a new function. Only LM-01 is genuinely new.

| ID    | Requirement                                                                                                                                                                                                   | Existing mechanism it generalizes                                                                                        |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| LM-01 | Cycle registry: each module declares its natural cycles (daily operations, seasonal, annual budget, multi-year renewal, generational, ecological recovery); cadence is a domain parameter, not a global timer | New                                                                                                                      |
| LM-02 | Review triggers at cycle boundaries and on events (breaches, new evidence, forecast error, consent change, shocks)                                                                                            | Invariant 17 (TRU-MONITOR-001) and TRU-MONITOR-002; cumulative Exception review loop (invariant 16 (GOV-CUMULATIVE-001)) |
| LM-03 | Version and change control; a model update never alters the record of why an earlier decision was made                                                                                                        | Decision Provenance and replay (9); invariant 1 (DPP-IMMUTABLE-001)                                                      |
| LM-04 | Learning guardrails; binding objectives, protected minima and delegated powers change only with human authorization                                                                                           | Invariant floor; Standards Process (14.1); Learning Plane (21)                                                           |
| LM-05 | Retirement with preserved evidence and migrated consumers                                                                                                                                                     | Phase-pull catalog retirement                                                                                            |

## 41.2 Shared Planning and Risk Analysis

All Part V modules use consistent scenario, population, asset, time and agreement identifiers. A shared risk-analysis capability maintains exposure, correlation and dependency assumptions; it remains a common service, not a standalone module. The planning loop runs: proposed commitment → capacity and funding assessment → development and allocation alternatives → human authorization → execution under standing Delegation Envelopes.

Resource commitments are registered once (RES-REGISTRY-001). When no portfolio meets every commitment, the system names the conflicting constraints and offers staged implementation, more resources or a formal Proposition; it never quietly trades the floor away (invariant 9 (OPT-NONCOMP-001)).

# 42. Ecosystem Endowment Simulator (MVP Module v0.1)

## 42.1 Purpose and Packaging

Under the assumptions in 42.2, the v0.1 reference scenario turns a \$250M seed fund into a median terminal value of about \$1.5B (today's dollars) after 50 years, with a median first dividend in year 15 and a median \$587 per member in year 50. These are scenario outputs, not forecasts (8.0, 20.1). It is delivered as a self-contained numpy module (acecog_endowment_sim) for the Optimization/Evidence planes of the Phase 1 backend, with each run logged as a Decision Provenance input (dataset version, scenario, seed).

## 42.2 Dataset and Model

Dataset: labeled synthetic. A fictional 60,000-member watershed ("Upper Rio Verde"), calibrated to the right order of magnitude for Southern Rockies conditions: hydrocarbons, hardrock minerals, 500 MW solar, 300 MW wind, 2.5M visitor-days a year and \$3M a year in downstream ecosystem-service payments.

Model: mean-reverting commodity prices; renewable resource and price variability; visitor numbers that scale with ecological condition, with wildfire shocks; fat-tailed endowment returns; stochastic inflation; a 5% draw on the 5-year average; 100% Hartwick routing of depletion rent; the CAB budget order; an ecological gate at condition 0.50; dividend multiplier 0.75–1.25 by condition. 5,000 paths × 50 years per scenario in the full design; the results in 42.3 come from a 1,000-path run.

## 42.3 Results

Model outputs of the v0.1 reference scenario (1,000 paths, recorded seed). They are conditional on the assumptions in 42.2 and are not forecasts.

| Scenario                                              | First median dividend | Dividend per member, yr 50 (median, p5–p95) | Floor shortfall risk |
|-------------------------------------------------------|-----------------------|---------------------------------------------|----------------------|
| Baseline                                              | yr 15                 | \$587 (\$205–\$1,634)                       | 3%                   |
| Commodity boom-bust                                   | yr 15                 | \$598                                       | 3%                   |
| No Hartwick (depletion rents spent)                   | yr 2                  | \$416                                       | \<1%                 |
| Alaska-style override (draw diverted in 40% of years) | yr 19                 | \$431                                       | 47%                  |
| Climate stress                                        | yr 26                 | \$105                                       | 23%                  |

- **Momentum:** in the baseline scenario, the median draw exceeds depletion income from year 8; from then on the modeled fund, not extraction, carries the economy.

- **Patience versus spending:** in the model, spending depletion rents pays the first dividend 13 years sooner but leaves about 30% less per member through year 50.

- **The Alaska lesson, modeled:** diverting the draw in 40% of years raises modeled floor-shortfall risk from 3% to 47%.

- **The land sets the pace:** under the reference assumptions and these extraction levels, modeled condition reaches the gate within about 10 years, and the gate then acts as a governor. Under climate stress, extraction is paused about 31 of 50 years and 61% of paths end below the gate.

## 42.4 Invariant Tests

All passing: depletion rents never distributed (GOV-COMMONS-001); floor funded before dividend; guardian never funded from extraction (ECO-GUARD-001); gate halts extraction; overrides visible; runs reproducible.

## 42.5 Next Iteration (v0.2)

- Natural Capital Account alongside the fund, with capitalized-yield valuation.

- Ecosystem Share at the top of the budget order.

- An in-kind provisioning channel that lowers each member's money need.

- Interdependence treaty flows between two linked watersheds.

- Calibration against real data: New Mexico severance tax, Colorado State Land Board revenue, federal energy statistics.

# Part VI — Compliance & Assurance

# 43. Compliance and Assurance

## 43.0 Purpose, Scope, and Relationship to 12.1

Section 43 makes compliance and assurance a first-class module of ACECOG, with a mandatory core in the assurance layer, directly below the Invariant Floor and module floors (14.0), and optional, configurable packs above it. It covers three things 12.1 does not: operator certification for shared hosting, public-sector legal obligations that shape deliberation itself, and the conduct of any organization that operates or advises on ACECOG.

**Umbrella role.** Section 43 is the governing compliance module for the whole specification. Sections 4.2 (GML), 12 and 12.1 (civic trust and regulatory alignment), 13.1 (MVP scope), 22.5 (hosting), 23 (Civic Trust Plane), and 28 and 28.1 (open domains and portability limits) keep their own content and point here for compliance obligations, certification, and evidence. The supporting standards crosswalk and the proposed ISO standard group are in Appendix I; merge notes are in Appendix J.

**Why 12.1 was not sufficient.** Through v0.18, 12.1 deferred SOC 2 and FedRAMP as "relevant only if ACECOG is ever hosted as SaaS." Section 22.5 (v0.16) introduced a shared multi-tenant regional platform for small and under-resourced jurisdictions. That is SaaS. The deferral did not hold for any deployment using the shared-hosting model.

**What 12.1 keeps.** 12.1 remains the short statement of MVP-era hygiene: SSDF (SP 800-218), privacy hygiene, WCAG 2.2 AA (ISO/IEC 40500:2025), records retention (11.3), AI transparency per Section 10, and a build-time SBOM. Its standing advisory-output disclaimer is unchanged and is restated as a floor requirement in 43.2. Its former deferred list is now scheduled by hosting model and GML level in 43.3.

**Scope boundaries.** Section 43 specifies what the software must do and what evidence it must produce. It does not constitute legal advice, and no pack is a substitute for a jurisdiction's own counsel. Items where the specification depends on a legal interpretation not yet obtained are listed in 43.8.

**Structure.**

- 43.1 Three compliance layers

- 43.2 Assurance Controls (mandatory core)

- 43.3 Operator certification roadmap and shared responsibility

- 43.4 Jurisdiction Compliance Packs (California reference pack)

- 43.5 AI and ethics governance alignment

- 43.6 Operator neutrality and commercial conduct

- 43.7 Canonical objects, invariants, acceptance tests

- 43.8 Open items requiring legal review

- Appendix I Compliance evidence: ISO crosswalk and proposed standard group

## 43.1 Three Compliance Layers

Compliance obligations fall into three layers with different owners, different evidence, and different places in the spec. Keeping them separate prevents a common failure: treating an operator's SOC 2 report as if it answered a council's open-meeting or ethics obligations.

| Layer                               | What it governs                                                                                            | Who carries it                                                              | Where ACECOG addresses it                               |
|-------------------------------------|------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|---------------------------------------------------------|
| 1\. Operator certification          | Security and availability of the organization and infrastructure hosting ACECOG                            | Platform operator (shared tier) or the jurisdiction itself (sovereign tier) | 43.3 roadmap; 43.2 evidence generation                  |
| 2\. Public-sector legal obligations | Open meetings, public records, retention, accessibility, privacy, ethics disclosure, legal status of votes | Each Civic Body, per its jurisdiction's law                                 | 43.2 floor controls; 43.4 Jurisdiction Compliance Packs |
| 3\. AI and ethics governance        | AI Process Manager boundary, neutrality of feeds and drafting, operator and consultant conduct             | Operator, implementers, and Civic Bodies jointly                            | 43.5 AI alignment; 43.6 commercial conduct              |

Layer 1 is certified about an organization. Layers 2 and 3 are enforced in the product's behavior. ACECOG's contribution to Layer 1 is evidence: the Evidence plane, event log, and Decision Provenance should make audits cheaper than for conventional govtech, not merely possible.

## 43.2 Assurance Controls (Mandatory Core)

The Assurance Controls are eleven controls that every ACECOG deployment enforces at every GML level, on every hosting model. No Civic Body, federation contract, or Compliance Pack can disable them: they form the assurance layer (14.0), and the layer rule (invariant 19, GOV-FRAMEWORK-001) bars every lower layer from relaxing them. They change only through change management, and from version 1.0 through the Floor Revision Process (14.1).

The Assurance Controls are the mandatory control set of the Civic Trust Plane (2, 12, 23). They add no new plane and no decision authority; they constrain how every plane stores, exposes, and proves what it does. They are distinct from Civic Assurance and Buffering (34), which concerns whether service commitments can actually be delivered.

| ID     | Control                       | Minimum requirement                                                                                                                                                                                                                                                                                                                                                                                      |
|--------|-------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ASR-01 | Identity and access           | Role-based access aligned to authority envelopes; multi-factor authentication for every authority-bearing role; least privilege by default                                                                                                                                                                                                                                                               |
| ASR-02 | Operator access transparency  | Any operator-staff access to tenant data is time-boxed, justified, logged as an event, and visible to the tenant (extends TRU-TENANT-001)                                                                                                                                                                                                                                                                |
| ASR-03 | Encryption                    | Encryption in transit and at rest; key custody declared per hosting tier (43.3)                                                                                                                                                                                                                                                                                                                          |
| ASR-04 | Tamper-evident audit log      | Hash-chained event log, one chain per Civic Body so each body's records can be exported and verified on their own (CL-068); security events (sign-ins, privilege changes, exports, deletions) recorded in the same log as governance events                                                                                                                                                                                                                                                                  |
| ASR-05 | Records and retention         | Each Civic Body holds a Retention Schedule, configurable per record class; the default for every class is permanent retention. Deletion occurs only by schedule or recorded legal order: the content is destroyed and a sealed placeholder (record, schedule or order, authorizing actor, date) stays in the hash-chained log, so the history still verifies (CL-054); records-request search and export |
| ASR-06 | Accessibility                 | WCAG 2.2 AA (ISO/IEC 40500:2025) across all three clients, including the mobile PWA tiers (11.6); an accessibility conformance report per release                                                                                                                                                                                                                                                        |
| ASR-07 | Privacy and data minimization | Eligibility credentials stored apart from participation records; ballot secrecy honored where a Governance Process requires it; no sale or secondary commercial use of civic data; data-residency declaration per tenant                                                                                                                                                                                 |
| ASR-08 | Legal-status labeling         | Every vote, approval, and published result displays its legal status (advisory, consultative, or binding); "binding" requires a Legal Effect Declaration (43.7), adopted only by a recorded Governance Process decision, citing the enabling authority and a counsel opinion, and applying from its effective date (CL-067)                                                                                                                                                                                                                                          |
| ASR-09 | Incident response             | Documented incident process; security incidents recorded as events; tenant notification within the period its pack or contract specifies                                                                                                                                                                                                                                                                 |
| ASR-10 | Supply chain                  | Build-time SBOM (carried from 12.1), dependency vulnerability scanning, signed releases                                                                                                                                                                                                                                                                                                                  |
| ASR-11 | Portability and exit          | Complete tenant export (event log, artifacts, provenance) in documented open formats; exit never requires operator cooperation beyond running the export (implements invariant 12, TRU-EXIT-001)                                                                                                                                                                                                         |

**Standing disclaimer.** 12.1's advisory-output disclaimer is carried here unchanged as a floor statement: ACECOG produces advisory planning and coordination outputs. It does not execute financial instruments, replace an accounting system, or constitute legal or financial advice. ASR-08 is how that disclaimer reaches every screen rather than living only in documentation.

**Evidence by design.** For each control, the system generates exportable evidence (configuration snapshots, log extracts, access reviews) mapped to external frameworks through Control Mappings (43.7). An auditor should be able to test ASR-01 through ASR-11 from exports alone, without operator narration.

## 43.3 Operator Certification Roadmap and Shared Responsibility

Certifications are sequenced by hosting model first and GML level second, because the obligation follows who holds the data, not how mature the Civic Body's governance is. A pilot council self-hosting at GML-1 needs none of them; a shared regional platform serving three small cities at GML-0 needs SOC 2 and a GovRAMP status from launch.

**GovRAMP as the primary state/local target.** GovRAMP (formerly StateRAMP, rebranded February 2025) authorizes cloud products once against a NIST SP 800-53 Rev 5 baseline, and participating state, local, tribal, and education governments reuse that authorization (StateTech). Its status levels form a ladder: Snapshot (40 controls), Core (60, no third-party assessor), Ready (80, with assessor), and Authorized or Provisional (300+, assessor plus government sponsorship) (Compyl guide). GovRAMP accepts a provider's FedRAMP documentation package, but not the reverse, and FedRAMP does not formally recognize GovRAMP as an alternative framework (GovTech, March 2025; checked at Gate 1). The control counts above come from a vendor guide and are to be confirmed against GovRAMP's own documents. Several states now make GovRAMP a buying requirement; California's position should be confirmed before relying on it (43.8).

| Stage                                 | Trigger                                                       | Operator certification target                                                                                                | Notes                                                                    |
|---------------------------------------|---------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| Pilot                                 | Single Civic Body, GML-0/1, self-hosted, including a dedicated cloud tenancy (11.5) | None required; GovRAMP Snapshot as a voluntary readiness gauge. A pilot on a shared platform needs SOC 2 Type I and GovRAMP Core (13.1)                                                         | ASR-01..11 and 12.1 hygiene still apply                                  |
| Shared platform launch                | First production tenant on the 22.5 shared multi-tenant tier  | SOC 2 Type I at launch, Type II after first observation period; GovRAMP Core                                                 | Replaces 12.1's former SaaS deferral                                     |
| Regional scale                        | Regional aggregator license, or procurements that require it  | GovRAMP Ready, then Authorized with a sponsoring agency                                                                      | Sponsorship is a natural role for the anchor regional body               |
| International or ISO-requiring buyers | Buyer requirement                                             | ISO/IEC 27001                                                                                                                | Largely reuses SOC 2 control work                                        |
| Federal tenants                       | A federal agency becomes a tenant on the operator platform    | FedRAMP                                                                                                                      | Avoided when federal partners use the 22.5 one-way sanitized push tier   |
| Statutory deployment                  | GML-2/3, or funding instruments carrying federal money (5.13) | Jurisdiction's own RMF authorization (SP 800-37) on the full SP 800-53 catalog; 2 CFR 200 and Single Audit-sufficient trails | Carried from 12.1's deferred list; applies mainly to sovereign instances |

**Shared-responsibility matrix.** Every tenant contract includes this matrix so that no control falls between operator and jurisdiction. "Operator" means the organization running the shared or dedicated platform; "Tenant" means the Civic Body or its IT authority.

| Control area                                           | Shared tier                                                                 | Dedicated tenant                                 | Sovereign (self-hosted)                            |
|--------------------------------------------------------|-----------------------------------------------------------------------------|--------------------------------------------------|----------------------------------------------------|
| Infrastructure, patching, encryption keys              | Operator                                                                    | Operator (tenant may hold keys)                  | Tenant                                             |
| Application security, releases, SBOM (ASR-10)          | Operator                                                                    | Operator                                         | Operator ships; tenant deploys                     |
| User identity, role assignment (ASR-01)                | Tenant assigns; operator enforces                                           | Tenant, optionally via its own identity provider | Tenant                                             |
| Governance configuration, retention schedules (ASR-05) | Tenant                                                                      | Tenant                                           | Tenant                                             |
| Pack selection and legal interpretation (43.4)         | Tenant                                                                      | Tenant                                           | Tenant                                             |
| Incident response (ASR-09)                             | Operator leads, notifies tenant                                             | Operator leads, notifies tenant                  | Tenant leads; operator supports on product defects |
| Evidence export for audits                             | Operator provides platform evidence; tenant provides configuration evidence | Same                                             | Tenant; product generates evidence                 |

Legal interpretation always stays with the tenant. The operator supplies tools that enforce a pack's rules; it never decides what a jurisdiction's law requires (see 43.6).

## 43.4 Jurisdiction Compliance Packs

A Jurisdiction Compliance Pack is a versioned, optional bundle of constraints a Civic Body adopts to enforce the law that applies to it. Packs follow the same one-way ratchet as the rest of the floor: under the layer rule (invariant 19, GOV-FRAMEWORK-001), a pack can add constraints or evidence requirements, but it can never relax an Assurance Control, a module floor, or an invariant.

**Pack model.**

- A Civic Body declares which packs apply through its Governance Process; adoption, upgrade, and removal are recorded events.

- Each pack contains rule constraints on Governance Process configuration, UI behavior and labels, Retention Schedule templates, disclosure hooks, and evidence templates.

- Packs are authored and maintained with legal review. The operator distributes and enforces them; the adopting body's counsel confirms applicability (43.3 matrix).

- Packs version like floor editions (14.1): a newer pack edition is visible to a body running an older one, and adoption is never silent.

- Packs compose. A special district might adopt the California pack plus a federal-grant pack for a funding instrument.

- **Participation-restricting constraints.** Any pack constraint that restricts participation (a higher identity tier, limits on public comment, narrower notice) cites the specific legal requirement that compels it, is shown to the Civic Body before adoption, and is flagged for cumulative-impact review (invariant 16, GOV-CUMULATIVE-001).

**Composition (CL-050).** A Civic Body's pack is a composition of versioned modules, each maintained and tested on its own.

| Layer                         | Example content                                                                            | Maintained by                                    |
|-------------------------------|--------------------------------------------------------------------------------------------|--------------------------------------------------|
| Federal                       | ADA Title II web accessibility; Section 508                                                | Pack maintainer                                  |
| State                         | Open meetings, public records, retention schedules, fiscal limits, state accessibility law | Pack maintainer, with counsel sign-off per state |
| County or regional (optional) | Special-district or regional-authority rules                                               | Pack maintainer or adopting body                 |
| Local                         | Home-rule charter, municipal code                                                          | Adopting jurisdiction                            |
| Civic Body                    | Its own adopted rules beyond the law                                                       | The Civic Body, through its Governance Process   |

Each module carries an ID, its layer and jurisdiction, an edition and effective dates, its rules with a legal basis for each, its own CMP test fixtures, its maintainer, and the date of counsel review. Rule types are guard (blocks an action), record (keep or publish for a period), notice (advance notice), label (status or disclosure on a result), accommodation (accessibility or language access), and participation restriction (valid only with a cited law that compels it).

Composition rules:

1.  Only adds: no module may waive or relax a higher protection layer (invariant 19 (GOV-FRAMEWORK-001)).

2.  Stricter wins where two modules regulate the same thing. Each rule type defines stricter: longer retention, earlier notice, broader publication, narrower private communication, fuller accommodation.

3.  Conflicting duties go to counsel. Where two rules cannot both be met (disclose versus withhold, retain versus destroy), the composition flags the conflict to counsel and never resolves it automatically. Until counsel decides, the reversible option applies: retain rather than destroy, withhold rather than publish.

4.  Preemption is declared, never inferred: where a higher law preempts a lower one, the module records it with a citation.

5.  Every decision records its composition: the composition manifest (module IDs and editions) has a hash, carried in each transaction's bound versions (8.9) and in the Decision Provenance Packet.

A module edition never changes once published; updates are new editions. Corrections that only add protection may be adopted through ordinary process. A change in law sets a transition date by which the Civic Body adopts the new edition through its Governance Process; transactions already in progress keep their bound edition (8.9). State modules are maintained by a named pack maintainer with counsel sign-off per state.

### 43.4.1 California Reference Pack

California was the first reference pack, written for a Bay Area market; it is restated as a state module under the composition rules above. Every rule below is pending counsel confirmation (43.8); the pack is written so a jurisdiction's attorney can check each rule against its stated basis.

| Rule                         | Legal basis (to confirm)                                                                                                                                           | ACECOG behavior                                                                                                                                                                                                                                                                                                                                                                                                            |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Open-meeting guard           | Ralph M. Brown Act (Gov. Code 54950 et seq.), including the serial-meeting prohibition and its rules on members' internet posts; Bagley-Keene Act for state bodies | For a body declared subject to the Act: no private member-to-member channels on items within its jurisdiction; member deliberation happens only in public, noticed contexts; members cannot reply to one another's posts on such items outside a meeting; staff briefings cannot relay one member's position to others; the body's formal action remains in its noticed meeting, which ACECOG records rather than replaces |
| Public records               | California Public Records Act (Gov. Code 7920.000 et seq.)                                                                                                         | Records-request intake, full-text search across propositions, comments, votes, and artifacts; redaction workflow with reasons recorded; statutory response clocks tracked per request                                                                                                                                                                                                                                      |
| Retention and destruction    | Local-agency records statutes (e.g., Gov. Code 34090 for cities) and the body's adopted schedule                                                                   | Retention Schedule templates; deletion requires a recorded authorizing action; nothing deleted before its schedule allows                                                                                                                                                                                                                                                                                                  |
| Conflict-of-interest recusal | Political Reform Act (Gov. Code 81000 et seq.) and FPPC regulations                                                                                                | Members and designated consultants declare interests; a declared conflict blocks deliberation and voting on that item; recusals are recorded and published with the decision's provenance                                                                                                                                                                                                                                  |
| Language access              | Dymally-Alatorre Bilingual Services Act, where applicable                                                                                                          | Plain-language summaries and core interface available in languages the body designates; translations flagged as AI-assisted where they are (11.6, Section 10)                                                                                                                                                                                                                                                              |
| Legal status of votes        | State and local election law; the body's own enabling authority                                                                                                    | Default label "advisory"; "binding" only with a Legal Effect Declaration citing the authority that gives it effect (ASR-08)                                                                                                                                                                                                                                                                                                |

**Other packs (catalog reserve).** A Texas pack (TX-RAMP is statutorily required for Texas state agencies and higher education, per the Compyl guide); a federal-grant pack (2 CFR 200 and Single Audit evidence, activated by a funding instrument per 5.13); and a pack template so jurisdictions outside these can author their own, subject to the same ratchet.

### 43.4.2 Colorado State Module (Pilot)

Colorado is the pilot state (CL-048). Every rule below is pending counsel confirmation (WBS 3.3).

| Area                  | Rule                                                                                                                                                                                                                             | Legal basis (to confirm)                                             |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| Open meetings         | A gathering of three or more members, or a quorum if fewer, to discuss public business is a meeting. Member-to-member electronic messages on the merits or substance of public business count; scheduling and forwarding do not. | Colorado Open Meetings Law, C.R.S. 24-6-402, as amended by HB21-1025 |
| Notice                | Full and timely notice of meetings; posting period and place to confirm                                                                                                                                                          | C.R.S. 24-6-402                                                      |
| Public records        | Platform records about public business are public records unless an exemption applies                                                                                                                                            | Colorado Open Records Act, C.R.S. 24-72-201 et seq.                  |
| Retention             | Record classes map to the Colorado State Archives schedules                                                                                                                                                                      | State Archives municipal and county schedules                        |
| Fiscal limits         | No new tax or tax-rate increase without voter approval; pilot funds use existing appropriations or restricted grants (5.13)                                                                                                      | Colorado Constitution, Art. X, Sec. 20 (TABOR)                       |
| Accessibility         | State law requires accessible government digital services; the WCAG 2.2 AA floor (ASR-06) already exceeds the WCAG 2.1 standard the state cites                                                                                  | HB21-1110                                                            |
| Conflicts of interest | Disclosure and abstention rules for local officials, implemented as Interest Declarations (43.7)                                                                                                                                 | Statute to confirm                                                   |

## 43.5 AI and Ethics Governance Alignment

ACECOG's existing AI boundary already does most of what recognized AI-governance frameworks ask for; this subsection maps it so buyers with AI procurement policies can verify that, and adds four requirements the mapping exposed as missing.

**Mapping to the NIST AI Risk Management Framework.** The RMF organizes AI risk work into four functions. ACECOG's coverage:

| RMF function | ACECOG mechanism                                                                                                                                                 |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Govern       | AI Process Manager authority boundary (Section 10): AI drafts and forwards, never holds authority; invariant 15 (AI-NEUTRAL-001); feed and notification neutrality (11.6) |
| Map          | AI task-class registry and neutrality classification (24.2)                                                                                                      |
| Measure      | Mandatory evidence capture of AI inputs and outputs (24.4); UIX-NEUTRAL-001..004 acceptance tests                                                                |
| Manage       | Human approval gates on every consequential command; AI-related incidents handled under ASR-09                                                                   |

**ISO/IEC 42001.** 42001 certifies an organization's AI management system, so it is a Layer 1 operator target, not a product feature. It is optional and buyer-driven, sequenced after SOC 2 in the 43.3 roadmap.

**New requirements.**

- **AI-PROV-001 Model provenance.** Every AI-assisted artifact records the model identity and version, the task class, and the prompt template version that produced it.

- **AI-CHANGE-001 Model change visibility.** A change of model or prompt template for any task class is a recorded event, announced to tenants before it takes effect in their instance.

- **AI-TRAIN-001 No training on civic data by default.** Tenant civic data is not used to train or fine-tune models unless the Civic Body records consent through its Governance Process; consent is scoped and revocable.

- **AI-LABEL-001 Disclosure to participants.** Any AI-generated or AI-translated text shown to a participant is labeled as such, including plain-language summaries in the Resident tier (30.7).

## 43.6 Operator Neutrality and Commercial Conduct

An organization that operates ACECOG, advises Civic Bodies on what to fund, and runs the AI that drafts propositions would recreate at the business level the capture risk the spec prevents in code. This subsection binds operators and implementers to process-only roles, and makes the binding checkable.

**Roles.**

- **Operator:** runs a shared or dedicated ACECOG platform (22.5).

- **Certified Implementer:** an organization, which may or may not be the operator, that configures, trains, and supports Civic Bodies.

- **Independent Auditor:** performs audits under the Auditor journey (30.10).

**Conduct rules.**

1.  **Process, not substance.** Operators and implementers may configure Governance Processes, author maturity frameworks with a body (4.3), draft federation contract mechanics, migrate data, and train staff. They may not advise a Civic Body on which propositions to fund, rank, or approve, and may not author propositions on a body's behalf.

2.  **No outcome-linked compensation.** No fee may depend on funds allocated, grants won, propositions approved, or participation volume. Pricing is fixed or banded by jurisdiction size or budget.

3.  **Citizens are never billed or monetized.** Participation is never priced (invariant 24, TRU-ACCESS-001). In addition, Resident participation (30.7) carries no advertising and generates no data for sale (ASR-07).

4.  **Audit independence.** An Independent Auditor may not be the operator, a Certified Implementer serving the audited body, or an affiliate of either, within a cooling-off period set by the certification requirements.

5.  **Disclosure.** Every engagement between an operator or implementer and a Civic Body is recorded as an Engagement Record visible in that body's provenance: scope, fees basis, and staff involved.

6.  **Public-official status.** Where an implementer's role would make its staff public officials under the jurisdiction's ethics law (for example, consultants under California's Political Reform Act), the pack's disclosure hooks apply to them (43.4).

7.  **Defaults take effect only on adoption.** Every operator-supplied default (feed ordering, thresholds, templates, pack editions, AI models) is versioned, and a change takes effect for a tenant only after that Civic Body records its adoption. This generalizes AI-CHANGE-001 to every default.

Rules 1–3 and 5–7 form certification requirement OPS-NEUTRAL-001, and rule 4 forms OPS-AUDIT-001. Conformance is a condition of operator certification (43.3) and binds any organization that uses the ACECOG name or certification mark for hosting or implementation. Both were Invariant Floor entries in v0.19; v0.20 moved them here because they govern commercial conduct rather than the integrity of self-governance (Appendix K).

### 43.6.1 Editions and Deployments

The specification is implemented by one open core. An edition (for example a commercial edition with proprietary configuration packs, adapters or hosting) and every deployment (a public demonstration, a Civic Body's installation or tenant) are built from the core and share nothing else with each other: no credentials, keys, records, identities or authority. The core never depends on an edition. An edition serving a Civic Body may add constraints but may not remove or weaken an invariant, an Assurance Control, exit (invariant 12) or the conduct rules of 43.6, and its configuration is inspectable by that body. Use of an edition outside civic governance (for example corporate governance) is a separate domain decision under 28.1 (CL-082).

## 43.7 Canonical Objects, Invariants, and Acceptance Tests

Section 43 adds eight canonical objects, three rules carried in the Section 14 Invariant Floor, two operator certification requirements, and sixteen acceptance tests under the traceability prefix CMP.

### 43.7.1 New Canonical Objects

These objects are also listed in Section 7.

| Object                   | Key fields                                                                                                                                    | Defined in    |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| Compliance Pack          | pack_id, jurisdiction, edition, rule constraints, retention templates, disclosure hooks, evidence templates, legal-basis citations            | 43.4          |
| Retention Schedule       | civic_body_id, record class, retention period, destruction authority, legal basis                                                             | 43.2 (ASR-05) |
| Legal Effect Declaration | civic_body_id, decision class, legal status, enabling authority citation, adopting action reference                                           | 43.2 (ASR-08) |
| Control Mapping          | control_id (ASR or AI), external framework, external control reference, evidence template                                                     | 43.2, 43.5    |
| Engagement Record        | organization, role (operator, implementer, auditor), civic_body_id, scope, fee basis, staff, dates                                            | 43.6          |
| Interest Declaration     | person_id, civic_body_id, interest description, affected propositions, recusal status                                                         | 43.4          |
| Compliance Module        | module_id, layer, jurisdiction, edition, effective dates, rules with rule type and legal basis, CMP fixtures, maintainer, counsel review date | 43.4          |
| Pack Composition         | civic_body_id, module IDs and editions, composition hash, flagged conflicts and their interim rule                                            | 43.4          |

### 43.7.2 Floor Rules and Certification Requirements

As normalized in v0.20 (Appendix K):

| Rule                | Where it lives                                    | Statement                                                                                                                                                                                                |
|---------------------|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Layer rule          | Invariant 19 (GOV-FRAMEWORK-001), Section 14      | No lower layer (module floor, Assurance Controls, operator controls, Compliance Pack, maturity framework, or local configuration) may relax a higher one. Absorbs v0.19's ASR-FLOOR-001 and CMP-PACK-001 |
| Legal status        | Invariant 26 (ASR-STATUS-001), Section 14         | Lifecycle state and legal status are separate, separately displayed attributes; nothing is presented as binding without a Legal Effect Declaration (8.0)                                                 |
| Exit                | Invariant 12 (TRU-EXIT-001), Section 14           | Complete export in documented open formats, without operator discretion; ASR-11 and CMP-007 trace to it                                                                                                  |
| Operator neutrality | OPS-NEUTRAL-001, certification requirement (43.6) | Conduct rules 1–3 and 5–7                                                                                                                                                                                |
| Audit independence  | OPS-AUDIT-001, certification requirement (43.6)   | Conduct rule 4                                                                                                                                                                                           |

### 43.7.3 Acceptance Tests

- **CMP-001** A configuration change that disables any ASR control is rejected, citing the layer rule (invariant 19).

- **CMP-002** Adopting a pack whose constraints would lower any floor threshold is rejected at adoption, citing the layer rule (invariant 19).

- **CMP-003** Under the California pack's open-meeting guard, a member cannot open a private thread with another member on an in-jurisdiction item, cannot reply to another member's post on it, and can still read and submit public comment.

- **CMP-004** A member with a recorded Interest Declaration on a proposition cannot deliberate or vote on it; the recusal appears in the decision's provenance.

- **CMP-005** Deletion of a record before its Retention Schedule allows is refused; an authorized deletion succeeds, is recorded as an event, and leaves a sealed placeholder that keeps the log verifiable.

- **CMP-006** A result with no Legal Effect Declaration displays "advisory"; with one, it displays "binding" and the cited authority.

- **CMP-007** A full tenant export rehydrates into a fresh instance, and Decision Provenance replay yields identical outcomes.

- **CMP-008** Operator-staff access to tenant data appears in the tenant's audit view with justification and time window.

- **CMP-009** A model or prompt-template change for a task class is announced to tenants before taking effect; subsequent AI-assisted artifacts carry the new model version.

- **CMP-010** An Engagement Record with an outcome-linked fee basis is rejected, citing OPS-NEUTRAL-001.

- **CMP-011** Assigning an auditor affiliated with the body's implementer within the cooling-off period is rejected, citing OPS-AUDIT-001.

- **CMP-012** An exported ASR-04 evidence package lets a third party verify the event log's hash chain without operator tools.

- **CMP-013** Two modules set retention periods of 3 and 7 years for the same record class; the composition applies 7.

- **CMP-014** One module requires publishing a record class and another forbids it; adoption flags the conflict to counsel, and the record is withheld until resolved.

- **CMP-015** Every decision's provenance carries the composition hash, and replay uses the bound module editions.

- **CMP-016** A new module edition adopted mid-cycle does not apply to a transaction already in progress.

**Traceability (Section 27).** New prefixes, added to Section 27: ASR (Assurance Controls), CMP (compliance acceptance tests), and OPS (operator certification requirements). The 43.5 requirements use the existing AI prefix as AI-PROV-001, AI-CHANGE-001, AI-TRAIN-001, and AI-LABEL-001.

## 43.8 Open Items Requiring Legal Review

Eight questions need a qualified attorney's answer before the California pack or the conduct rules ship; each is written so the answer can be recorded directly against the rule it affects.

- **Brown Act scope of ACECOG deliberation.** Does asynchronous public commenting by members on an ACECOG proposition count as participation in a meeting, a serial meeting, or neither? Can any part of the body's formal action occur on the platform, or must it always happen in a noticed meeting? (43.4 open-meeting guard, CMP-003)

- **Public records status.** Which ACECOG records are public records, including drafts, AI-generated summaries, and Resident comments, and which exemptions apply to eligibility credentials? (ASR-05, ASR-07)

- **Retention classes.** How ACECOG record types map onto city, county, and special-district retention schedules. (Retention Schedule templates)

- **Consultant public-official status.** When Certified Implementer staff become designated filers under the Political Reform Act. (43.6 rule 6)

- **Ballot secrecy.** Whether any advisory vote configuration triggers secrecy or election-law requirements, and when a Legal Effect Declaration can lawfully make results binding. (ASR-08)

- **Privacy law applicable to the operator.** Which state privacy statutes apply to an operator processing data on behalf of local agencies, and what the processor contract must include. (ASR-07)

- **GovRAMP in California.** Whether California state or local procurement requires or credits GovRAMP status, and the effect of TX-RAMP-style mandates elsewhere on the 43.3 roadmap.

- **ADA Title II web rule timing.** Current compliance dates and any enforcement changes for the rule's WCAG 2.1 AA requirement, by jurisdiction population size. ASR-06 already exceeds it at 2.2 AA; the question is only which date applies to each tenant. (ASR-06)

# Appendix A — Consolidation Notes

Version 0.3 restructures the original ACECOG functional-specification material around a public/civic Design–Build–Operate–Learn ethos and integrates the Optimization & Coordination Engine object model and state-machine/transaction semantics developed in companion versions 0.1 and 0.2. Earlier enterprise-system analogies are retained as design precedent, but ACECOG is framed as a ground-up civic operating platform rather than an ERP overlay.

The original specification's Sense → Model → Deliberate → Decide → Remember concept remains present as functional behavior distributed across the Governance, Evidence, Planning/Optimization, Decision, and Memory/Provenance engines. The original local-first, human-in-the-loop, ecological, deterministic-replay, federation, and adaptive-governance principles are retained and elevated into system-level invariants.

# Appendix B — v0.5 Reconciliation Notes

Version 0.5 merges the civic-architecture rigor developed in v0.3/v0.4 (governance-to-optimization contract, canonical object model, state machines, MVP acceptance tests, requirements traceability) with operational detail carried in a parallel Basis of Design reorganization of the original v0 functional specification. Five additions were inserted at the sections where v0.4 already named the concept but had not yet detailed it: Governance Maturity Levels (4.2), Funding Instruments and Capital Constraints (5.13), Deployment and Packaging Strategy (11.5), Regulatory and Standards Alignment (12.1), and a resourced Phase 1–2 timeline with a month-by-month MVP build plan (13.1–13.5). No existing v0.4 content was removed; Section 28’s list of remaining domains stands as originally written, minus the phasing-detail item this reconciliation addresses.

# Appendix C — v0.6 Stress-Test Integration Notes

Four adversarial stress tests were run against v0.5’s civic-legitimacy claims, each checked against the invariant list in Section 14. All four identified a real gap and were integrated directly into the sections below, rather than left as a standalone finding, consistent with this document’s own provenance ethos.

| Test                                        | Gap found                                                                                                                                             | Integrated at                                                                                                                               |
|---------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Sybil / capture resistance                  | No mechanism verified participant uniqueness; quorum/threshold math operated on an unguarded input.                                                   | Invariant 39; new Membership Credential object (7); eligibility assurance field (17.5).                                                     |
| Cross-jurisdiction rights conflict          | Federation coupling could produce a rights breach through externalities without touching any local constraint.                                        | Invariant 40; Federation Contract externality-exposed field (22.2); pre-solve check (22.3).                                                 |
| AI Process Manager framing capture          | “Draft only” authority governed what AI could touch, not how neutrally it framed competing proposals; drafting sessions were not captured by default. | Invariant 41; AI task class neutrality requirement and mandatory evidence capture (24.2, 24.4).                                             |
| Escalation fatigue / majority-tyranny drift | Exception Proposition (5.11) was scoped to a single decision; no mechanism aggregated small effects on the same constituency across many decisions.   | Invariant 42; cumulative variant of Exception Proposition (5.11); cumulative review loop (5.12); cumulative_impact_ledger reference (17.4). |

None of the four fixes required abandoning an existing design principle — each extends an existing mechanism (Membership, Federation coupling, AI task classes, Exception Proposition) to cover a case its current scope didn’t reach.

# Appendix D — v0.7 CMT Integration Notes

The Civilizational Maturity & Type-I Transition (CMT) module (Part III, Section 29) was developed independently and integrated at the user’s direction as a full top-level module, cosmic/multiworld sections included. Two points of connection to the rest of this specification are worth stating explicitly, since CMT was authored separately from Sections 0–28:

- **Relationship to GML (4.2).** Governance Maturity Levels gate how much institutional process a Civic Body must carry; CMT’s Type-I Readiness Gate (29.23) gates whether a civilizational system as a whole qualifies as adequately self-governing. Both share the same design move — a hard floor on the weakest dimension rather than an average — and a future revision should decide whether GML is a civic-body-scale instance of the same underlying gate pattern CMT defines at civilizational scale, or a genuinely separate mechanism. This document does not yet resolve that question.

- **Scope relative to Sections 0–28.** Sections 0–28 describe a buildable civic governance and portfolio-optimization system, with a resourced Phase 1–2 roadmap (13.1–13.5). CMT (29.1–29.25) describes an assessment and planning framework operating at a much larger scope, up to and including multiworld and intercivilizational governance (29.16–29.17). CMT currently has no phase-by-phase build plan of its own; before implementation work begins on it, it should receive the same treatment Section 13 gave the core system — an explicit MVP slice, a resourced timeline, and acceptance tests in the style of Section 26.

Integrating CMT here does not imply its cosmic-scale sections (X4–X6, 29.16–29.17) are near-term implementation targets. They are retained because the module’s own logic (29.7 Maturity Gap Analysis) depends on the full dimensional range to detect dangerous asymmetries early, not because Phase 1–3 of Sections 0–28 requires them.

# Appendix E — v0.8 Governance-Theory Benchmark Notes

Section 14’s invariant list is checked not only against adversarial stress tests (Appendix C) but against established governance scholarship, one benchmark at a time. The first pass checked GML-1 (4.2) against Ostrom’s eight design principles for durable commons governance. Six of eight were already well-served by the existing design (clearly defined boundaries via Membership Credential and invariant 39; congruence between rules and local conditions via 17.5’s process pluralism; low-cost conflict resolution via 17.5’s appeal/reconsideration rules; nested enterprises via GML’s own 0-3 ladder and Section 5.2’s jurisdiction hierarchy). Two were not:

- **Accountable monitoring** — GML-1’s dual-approval control governed decisions but not the approvers. Closed by invariant 43 (TRU-MONITOR-001) and the accountability_path field (7, 12.0.1).

- **Graduated sanctions** — the system had only two states, nothing or a full Exception Proposition, with no proportionate response to a first or minor deviation. Closed by invariant 44 (GOV-GRADUATED-001) and the four-tier response ladder (5.11.1).

Two principles were named as deliberate deviations rather than gaps: GML’s ladder is system-defined rather than community-authored (Ostrom’s “minimal recognition of rights to organize” would let each Civic Body design its own maturity ladder; ACECOG needs a common scaffold for federation to function at all), and collective-choice arrangements currently govern rule *adoption* more than ongoing rule *tuning* once a GML level is reached — flagged for a future pass rather than resolved here.

Further benchmark passes append entries to this appendix rather than open new ones, to keep the provenance of each invariant in one place. Ashby’s Law of Requisite Variety, principal-agent/delegation theory, and constitutional amendment design are complete (addenda below); legitimacy-versus-efficiency is the one pass still outstanding.

**Addendum (v0.9):** the Ostrom pass above named two principles as deliberate deviations rather than resolved gaps: a system-defined rather than community-authored maturity ladder (principle 7, minimal recognition of rights to organize), and collective choice governing rule *adoption* more than ongoing rule *tuning* (principle 3). Both are now addressed by Section 4.3’s Self-Defined Maturity Frameworks: a Civic Body may author its own framework through its own Governance Process, and amend it the same way, subject only to the invariant floor and an interoperability declaration (invariant 45) that keeps federation comparability intact without requiring framework identity.

**Addendum (v0.10) — Ashby’s Law of Requisite Variety.** GML-1’s dual-approval control is fixed-variety: identical process weight regardless of whether a decision is routine or unprecedented. Materiality thresholds (5.11, 42) escalate on magnitude; nothing escalated on novelty. Closed by invariant 46 (GOV-VARIETY-001) and Section 17.5.1: a precedent-similarity check against Decision Provenance triggers Expert/advisor consultation or extended deliberation for novel decisions, independent of materiality. This is an amplification response (growing the regulator’s variety) rather than GML’s existing attenuation pattern (narrowing what is allowed through) — Ashby’s law offers both as valid strategies, and GML-1 had only used one of them.

**Addendum (v0.10) — principal-agent / delegation theory.** The collective-principal structure (17.4’s Collective Will aggregating many members into one authorized voice before any agent acts) was already well-aligned with this tradition, and is noted as a strength rather than a gap. Two classic agency problems remained open after v0.8’s accountable-monitoring fix (invariant 43): adverse selection was addressed (who is chosen, how removed) but moral hazard was not (no signal on conduct between selection and recall), and there was no bonding/skin-in-the-game analog tying an individual approver’s history to their own future eligibility. Closed by invariant 47 (TRU-MONITOR-002) and the approval_track_record field (7, 12.0.1): automatically populated from Exception Proposition and Tier-2/3 outcomes tied to a role-holder’s approvals, surfaced at rotation/recall consideration without itself triggering recall.

**Addendum (v0.11) — constitutional amendment design.** This pass found three gaps: no distinction between amending an ordinary rule and amending the amendment rule itself (self-coup vulnerability, at the civic-body level); no process at all for amending the system-level invariant floor (Section 14) — the deepest gap, a genuine constituent- power question this specification had left implicit; and no general sunset/review default for governance-process amendments beyond the two places it already existed (17.5 emergency authority, 22.2 Federation Contract exit and amendment terms). Resolved using civil engineering’s design-code tradition as precedent (AASHTO/ASCE: a standing technical body, distinct from any engineer using the code, revising on a fixed cycle, never waivable by client preference) rather than software’s, which never built an equivalent licensure culture. Closed by Section 14.1’s Standards Process — open drafting (IETF-style rough consensus), self-applying strengthen/weaken classification, independent verification gated specifically on weakening proposals (the IEV analog), and local ratification into each Civic Body’s Maturity Framework with edition-lag visibility rather than compulsion — plus invariants 48–50 and the Floor Revision Proposal object (7). The same ratchet principle was folded into 17.5 at the civic-body level (invariant 49), closing the self-coup gap at both altitudes with one rule rather than two.

Addendum (v0.18) — institutional precedents as design evidence. Part V's invariants (52–65) were checked against working institutions rather than a single theory: the Alaska Permanent Fund (endowment durability versus dividend erosion through appropriation), New Mexico's early-childhood and land-grant funds (commons rents paid out as services), the Delaware River Basin Commission (obligations grounded in shared water), rights-of-nature cases (Whanganui, Te Urewera, Taranaki, Mar Menor, and Toledo's struck-down Lake Erie Bill of Rights), and the 2026 dissolution of the Bears Ears Commission (fragility of executive-created co-management). Each finding is traced in Sections 36–40 and Appendix H. The legitimacy-versus-efficiency benchmark pass remains outstanding.

# Appendix F — Version History

Reconstructed to the best available record. Entries for v0.1–v0.4 predate this reconciliation thread and are recalled from Appendix A’s own account and the v0.4 document as uploaded; they are not independently verified beyond that and should be corrected if this account is wrong.

| Version                       | Principal changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| v0 (original functional spec) | Initial ACECOG functional specification; Sense → Model → Deliberate → Decide → Remember decision lifecycle; separately reorganized into a 22-section Basis of Design with a phase roadmap through Phase 3 federation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| v0.1 – v0.2                   | Companion versions developing the Optimization & Coordination Engine object model and state-machine/transaction semantics later folded into v0.3 (per Appendix A).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| v0.3                          | Restructures the original specification around a public/civic Design–Build–Operate–Learn ethos; integrates v0.1/v0.2’s optimization and state-machine work; elevates the original local-first, human-in-the-loop, ecological, deterministic-replay, federation, and adaptive-governance principles into system-level invariants.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| v0.4                          | Full civic-body/direct-democracy framing; canonical object model; state machines (Section 8); MVP acceptance tests; the requirements traceability framework (Section 27); 28 sections total.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| v0.5                          | Reconciles v0.4 with a parallel Basis of Design reorganization of the original v0 spec: adds Governance Maturity Levels (4.2), Funding Instruments and Capital Constraints (5.13), Deployment and Packaging Strategy (11.5), Regulatory and Standards Alignment (12.1), and a resourced Phase 1–2 timeline with a month-by-month MVP build plan (13.1–13.5).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| v0.6                          | Integrates four adversarial stress-test findings (Sybil/capture resistance, cross-jurisdiction rights conflict, AI framing capture, escalation-fatigue/majority-tyranny drift) as invariants 39–42, with supporting mechanisms in Sections 7, 17.4–17.5, 22.2–22.3, 24.2, 24.4, 5.11–5.12.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| v0.7                          | Integrates the Civilizational Maturity & Type-I Transition (CMT) module as Part III / Section 29 (25 subsections, cosmic sections included); Appendix D documents CMT’s relationship to GML and its lack of a resourced build plan.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| v0.8                          | First governance-theory benchmark pass (Ostrom’s commons-governance design principles) against GML-1; adds accountable-monitoring invariant 43 and graduated-sanctions invariant 44 (12.0.1, 5.11.1); opens Appendix E to track future benchmark passes in one place.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| v0.9                          | Resolves the two Ostrom deviations flagged in v0.8: adds Section 4.3 Self-Defined Maturity Frameworks, the Maturity Framework canonical object (7), a Federation Contract mapping field (22.2), and invariant 45. Adds this version history (Appendix F).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| v0.10                         | Second and third governance-theory benchmark passes (Ashby’s Law of Requisite Variety; principal-agent/delegation theory) against GML-1. Adds novelty-based variety-amplification (17.5.1, invariant 46) alongside GML’s existing attenuation pattern, and an approval_track_record closing the moral-hazard half of the accountable-monitoring fix from v0.8 (12.0.1, invariant 47).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| v0.11                         | Fourth governance-theory benchmark pass (constitutional amendment design), resolved using civil-engineering design-code precedent (AASHTO/ASCE) rather than software licensure, which never matured. Adds Section 14.1 — the ACECOG Standards Process for amending the invariant floor itself: open drafting, self-applying strengthen/weaken classification, independent verification for weakening proposals, and local ratification with edition-lag visibility. Adds the civic-body-level amendment ratchet (17.5, invariant 49) closing the same self-coup vulnerability at that altitude. Adds invariants 48–50 and the Floor Revision Proposal object (7).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| v0.12                         | Adds Part IV — Roles & User Journeys (Section 30): a reusable journey template (30.3), a journey catalog status table (30.4), and the first fully specified entry, The Aspiring Grad Student — an individual, non-member proposer carried from proposition through live optimization fit-check, deliberation, approval, commitment, and execution visibility. Clarifies Guest Proposer eligibility semantics (30.5.2, 30.5.4) and adds traceability prefix JNY (Section 27).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| v0.13                         | Adds the second Journey Catalog entry, The Agency Planning Manager (30.6) — a regional planning-agency observer running a live, read-only cross-jurisdiction portfolio roll-up, objective-contribution and marginal analysis, and coordination-by-proposition rather than command, tracing directly to the project’s 2019 discovery-phase pitch for the Marin County Board of Supervisors. Renumbers Deferred Journeys to 30.7 and adds JNY-AGCY-001..008.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| v0.14                         | Adds Section 11.6 Interaction Architecture: desktop structured UI, conversational assistant (AI Process Manager as a client, not a new trust path), and a two-tier mobile surface (Concerned Citizen mass-uptake feed/push with self-attestation onboarding; Active-Role bounded in-envelope approval inbox), built as a Progressive Web App. Adds command/query separation as an explicit architectural constraint, a Notification/Subscription Service, a feed/notification-neutrality requirement generalizing AI-NEUTRAL-001, traceability prefix UIX, and acceptance tests UIX-NEUTRAL-001..004.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| v0.15                         | Adds the third and fourth Journey Catalog entries: The Concerned Citizen / Voter (30.7) — a mass-participation resident discovering, understanding in plain language, and expressing consent, objection, or delegation on propositions from the mobile Concerned Citizen tier, tracing to the second of the project’s 2019 “ACECOG Stories” — and The City Manager (30.8) — a delegated jurisdiction executive running exception triage, in-envelope resolution, escalation, and cycle-close accountability to the elected Governance Process. Renumbers Deferred Journeys to 30.9 and adds traceability prefixes JNY-CIT and JNY-MGR with acceptance tests JNY-CIT-001..007 and JNY-MGR-001..007.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| v0.16                         | Adds Section 22.5 Multi-Tenant Hosting and Trust Tiers — shared multi-tenant regional platform vs. self-hosted sovereign instance as the two hosting models, three federation trust tiers (live API, scheduled batch exchange, one-way sanitized push for partners such as defense/national-security installations that cannot be normal federation peers), a Federation Contract trust_tier field, and invariant 51 (TRU-TENANT-001) scoping a shared-hosting platform operator’s authority to nothing beyond its own operational role. Adds Section 28.1 Domain Portability: Reach and Current Limits, making precise what in the current specification makes the core architecture portable across governance domains (domain-agnostic object model, civic-body-configured Governance Process, a process-integrity-only invariant floor) and naming four current limits (allocation-shaped optimization bias, threshold-voting-only deliberation, lightly-exercised institutional actors, and out-of-scope legal/regulatory recognition).                                                                                                                                                                                                                                        |
| v0.17                         | Specifies the five remaining Journey Catalog entries: Facilitator/Clerk (30.9, process administration without substantive decision authority), Auditor (30.10, inspection with zero write-capable Authority), Federation Partner (30.11, a peer jurisdiction’s own delegate under a Tier A Federation Contract), Fund Manager (30.12, fiduciary visibility into co-invested capital, honestly scoped against the still-deferred Funding Instrument object), and Program Manager (30.13, a multi-node program using PortfolioNode.parent_id for the first time). Adds JNY-FAC, JNY-AUD, JNY-FED, JNY-FUND, and JNY-PROG acceptance tests; the Deferred Journeys reserve (renumbered 30.14) is now empty of named entries. Adds Appendix G — Project Genesis and Philosophical Lineage, tracing the architecture’s structural principles (autonomy-within-wholes, coupled-system modeling, resilience under discontinuity, values preceding optimization) back to the project’s earliest writing while explicitly treating that writing’s catastrophist content as historical genesis, not an operating premise of the specification.                                                                                                                                                 |
| v0.18                         | Adds Part V — Prosperity, Commons & Guardian Modules (Sections 31–42): Prosperity Transition (32), Shared Risk and Benefit Governance (33), Civic Assurance and Buffering (34), the Prosperity Floor (35), the Commons Endowment / sovereign fund (36), Guardian ("Lorax") Jurisdictions and the guardian governance floor (37), Indigenous Alignment (38), collective funding rules (39), Funding Instrument extensions (40), Lifecycle Management and shared planning (41), and the Ecosystem Endowment Simulator v0.1 (42). Adds invariants 52–65 (no-cost participation, unconditioned Prosperity Floor access, no obligation without voice, Hartwick depletion rule, collective-only conditions, guardian integrity, no collateralized land, interdependence-based obligations, no double-booking, no silent floor trade, no false guarantee, no retroactive rewrite) and clarifies invariant 44. Extends the Section 7 object table, the Federation Contract (22.2) and Section 27 prefixes; amends 13.2, 13.4, 11.6.7, 28.1, 30.7.4 and 30.12. Adds Appendix H.                                                                                                                                                                                                              |
| v0.19                         | Adds Part VI — Compliance & Assurance (Section 43) as the umbrella compliance module: Assurance Controls ASR-01..11 within the Civic Trust Plane, an operator certification roadmap (SOC 2, GovRAMP, ISO/IEC 27001, FedRAMP by hosting model) and shared-responsibility matrix, Jurisdiction Compliance Packs with a California reference pack, AI governance alignment (NIST AI RMF, ISO/IEC 42001; AI-PROV/CHANGE/TRAIN/LABEL-001), operator neutrality and commercial-conduct rules, six canonical objects, invariants 66–70 and a strengthening amendment to invariant 38 (register 27–70), and acceptance tests CMP-001..012. Raises the accessibility floor to WCAG 2.2 AA (ISO/IEC 40500:2025). Adds Appendix I (compliance evidence: ISO crosswalk, proposed standard group for civic self-governance systems, working drafts of Standard Parts 1 and 2) and Appendix J. Confirms the Part V decisions recorded as settled in 31.8, sets the commons-benefit residency cap (CE-10) and the 4–5% draw band (CE-02), and limits the guardian binding veto to certified ecological-limit breaches (37.4). Points 4.2, 7, 12, 12.1, 13.1, 14, 22.5.1, 23, 27, 28 and 28.1.2 to Section 43, and corrects cross-references in invariant 50, 14.1, Appendix E and the title block. |
| v0.20                         | Architecture freeze candidate; no new conceptual module. Normalizes the Invariant Floor from 44 invariants (27–70) to 26 (1–26) with IDs as primary references; adds protection layers and module floors (14.0, 14.2, 35.4, 36.6, 37.5) and the layer rule (invariant 19); adds the four-axis decision status model (8.0) and epistemic classes (20.1); states model outputs as conditional (36.5, 42); adds an acceptance test for every invariant (INV-AT); applies the red-team corrections (Guardian Council selection and accountability, Commission independence, veto lapse and appeal, revenue classification, endowment investment rules, prospective standing, consent, operator defaults, pack constraints, invariant admission test); corrects the journey catalog, test and requirement IDs, and Section 40 figures; adds Appendix K. Prepared under the change log CL-007 to CL-034.                                                                                                                                                                                                                                                                                                                                                                                  |
| v0.21                         | Build-readiness patch in response to an external review of v0.20; no new conceptual module. Adds the Phase 1 execution filter (13.6) and the Phase 1 solver profile (5.3, 13.1); defines local-first as a civic-body-controlled authoritative installation reached by desktop and mobile clients, reconciled with shared hosting (11.5); adds the version-binding rule (8.9) and Delegation Envelope parameters with fail-closed defaults (5.9); marks Part III catalog reserve with no build phase (29); adds Appendix L. Change log CL-035 to CL-040.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| v0.22                         | Developer contract and pilot plan; no new conceptual module. Adds Appendix M, the API contract v0.1 with a mock implementation whose contract tests pass the Phase 1 acceptance checks they cover, and the questions it raised (CL-044 to CL-047); adds 13.7, the Pilot Program Plan, and Appendix N, crosswalking the rebuilt pilot WBS to this specification; adds delegation concentration disclosure and reconfirmation (17.5, 17.8); capitalizes Civic Body throughout. Change log CL-029, CL-041 to CL-043. Revised 9 November 2026: adds identity onboarding and uniqueness assurance (23.1.1, invariant 13), civic authority continuity (17.9, 26.3), modular Compliance Packs and the Colorado module (43.4, 43.4.2), the materiality default (5.11), legal status fixed at close (8.0), one approval per change (8.9), the endowment withdrawal rule (CE-F6), retention defaulting to permanent with sealed placeholders (ASR-05), the local administrator scope (22.5.3), and the GML-1 Phase 1 target (13.5); renames the mass-participation role Resident and brings its mobile tier into the pilot. Change log CL-030, CL-044 to CL-054. Gate 1 baseline (9 November 2026): dispositions of the 59 independent-review findings applied as CL-055 to CL-077, including the canonical QP form, five new invariant tests, MVP-112 to MVP-114, Reference defaults in 4.2, envelope aggregate tolerances, per-Civic-Body hash chains, and checked facts.                                                                                                                              |
| v0.23                         | Gate 1 requirements baseline; no new conceptual module. Applies the owner's dispositions of the independent v0.22 review (CL-055 to CL-076): canonical QP form, five new invariant tests, Phase 1 scope fixes, Reference defaults, envelope aggregate tolerances, delegation rules, per-Civic-Body hash chains, editorial fixes and checked facts. Makes the repository Markdown the master (CL-078).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

# Appendix G — Project Genesis and Philosophical Lineage

This appendix records, in the same structural register as the rest of this specification, how ACECOG's architecture traces back to the project's earliest writing. It is a lineage note, not a premise: the specific circumstances that originally prompted this thinking are not, and are not intended to be, an operating assumption of the system itself. Section 29's Civilizational Maturity module already draws the same distinction at the level of scenario planning (29.12-29.13): a system capable of reasoning about many possible futures, including discontinuity, does not need to adjudicate which future is coming in order to be useful.

The earliest writing that became ACECOG was concerned with a single question: how do autonomous people organize themselves through a period of significant instability and produce something better on the other side, without surrendering their own sovereignty to do it. That question already contained a structural insight, stated first in the language of biology and later re-stated in the language of systems engineering: a part can be fully autonomous and fully embedded in a larger whole at the same time, at every scale from an individual to a federation of communities, and stability comes from that relationship being self-organizing rather than imposed from above.

That is, in substance, non-negotiable principle 4 (local sovereignty with federated interoperability) and the whole of Section 22's Federation model: independent Civic Bodies retain full authority over themselves while choosing to interoperate through explicit, bounded contracts. The specification did not invent this principle; it gave an existing intuition a precise, implementable, and testable form.

The same pattern holds for three further threads that ran through the early material. An instinct to map a coupled system of interdependent variables, rather than analyze isolated events one at a time, became the portfolio and federation architecture of Sections 18 and 22 — the discipline of modeling dependencies, constraints, and cross-jurisdictional coupling explicitly rather than informally. A concern with what survives a serious discontinuity — essential services, critical stocks, decentralized fallback capability, the possibility of reorganizing afterward — generalized into Section 29.13's Resilience and Discontinuity Mode, which is deliberately agnostic about which discontinuity, if any, actually occurs. And a language of sovereignty, collective awareness, and values preceding action found its operational form in subsidiarity and Delegation Envelopes (Section 7), participatory collective intelligence (the Governance Plane, Section 17), and values-before-optimization (Objectives set through deliberation, Section 18, rather than assumed).

None of this required, and none of it now depends on, agreement about any specific predicted event. Section 29.5's design objective — 'not to define a utopian end state' but 'to create a self-observing, self-governing, and continuously improving civilization' — is the same commitment the earliest writing made in less precise terms, with the empirical content removed and the epistemological discipline of Section 20 (Score, Indicator, Observation, Source, Methodology; observed fact distinguished from inference, scenario assumption, and speculative hypothesis) put in its place. That discipline is what lets this specification carry forward the structural insight the project began with, without asking anyone — including its own author — to accept any particular account of why it matters.

# Appendix H — v0.18 Prosperity, Commons & Guardian Integration Notes

v0.18 integrates a three-module concept draft (*ACECOG Prosperity Transition Functional Specification*, header v0.2) and the design decisions, research and simulator build of the 25 September 2026 session, drafted first as a standalone addendum and merged here.

Reconciliations made at merge:

- **Invariant numbering verified.** v0.17's register ended at 51 (TRU-TENANT-001); the addendum's 52–65 stand as drafted, and all fourteen are strengthening proposals under 14.1 (open drafting and local ratification, no independent-verification gate).

- **Funding Instrument was not new.** The addendum treated it as a deferred object; v0.17 already defined it (7, 5.13) with three MVP types. v0.18 therefore extends it with three Part V subtypes (40.1) rather than introducing it. It remains unimplemented in the MVP object model, so JNY-FUND-006 stays pending implementation.

- **No glossary section existed.** Part V terms are defined at 31.2 instead of in a document-wide glossary.

- **Clarification to invariant 44** (graduated sanctions never reach Prosperity Floor access) is recorded as a strengthening Floor Revision Proposal alongside 52–65.

- **Pilot WBS amendment** (a Pilot Stage 2 jurisdiction-selection criterion for existing collectively owned infrastructure, plus an FRP task for 52–65) belongs to the separate pilot workbook, not this specification, and is still to be applied there.

Sources consulted in the 25 September 2026 session: APFC FY26 audited financials; Alaska Story (2026 PFD); Pew Charitable Trusts (state trust funds and child care, 2026); Arizona Daily Independent (Arizona land revenue, 2026); Colorado Legislative Council (Permanent Fund and State Land Board); Colorado Sun (SB 152 repeal); CPR (Boulder municipalization); Bank of North Dakota 2025 Annual Report; Mission Local (San Francisco public bank measure); Next City (public bank barriers); High Country News (Bears Ears Commission); Government Executive (Forest Service reorganization, 2026); National Agricultural Law Center (Colorado River final EIS); DU Water Law Review (post-2026 negotiations); The Spinoff (Taranaki personhood); Heinrich Böll Stiftung (Mar Menor). Other cases cited — Whanganui, Te Urewera, Ecuador and Los Cedros, Toledo, the Delaware River Basin Commission, Valles Caldera Trust, Denver Water Forests to Faucets, the Rio Grande Water Fund, Colorado's instream-flow program, UN SEEA Ecosystem Accounting and the CARE principles — are from general knowledge and should be source-checked before external use. Sources added in the 6 November 2026 source check: APFC Board press release (September 2026); Alaska’s News Source (May 18, 2026); Pew Charitable Trusts (April 28, 2026); The 74 (October 2026); CNHI News (Arizona land endowment, FY2026); Colorado State Land Board FY2025 Annual Report; Longmont Leader (NextLight take rate); Boulder Beat (November 4, 2020); North Dakota Industrial Commission (June 2026); Fortune (November 3, 2026); Bay Area Reporter (November 2026); National Trust for Historic Preservation (July 17, 2026); High Country News (July 2026).

# Appendix I — Compliance Evidence: ISO Crosswalk and Proposed Standard Group

This appendix supports Section 43. It records how Section 43 maps onto existing ISO and ISO/IEC standards, and the proposal to develop the governance-integrity core of ACECOG into an ISO standard group. It is supporting evidence, not normative content of this specification; Section 43 governs wherever the two differ.

## I.1 ISO Standards Crosswalk

Roughly three-quarters of Section 43 maps onto published ISO and ISO/IEC standards; the unmapped remainder is the governance-integrity core that no existing standard addresses. That remainder is the justification for a new standard group (I.2).

The mapping follows a reuse rule: a future ACECOG standard should normatively reference an existing standard wherever one fits, and write new requirements only where none does.

| Section 43 element                                                                                                  | Existing ISO / ISO-IEC standards                                                                                                                                                                      | Fit                                   | What no standard covers                                                                  |
|---------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|------------------------------------------------------------------------------------------|
| Module as a whole                                                                                                   | ISO 37301 (compliance management systems, requirements); ISO 37000 (governance of organizations); ISO Harmonized Structure for management system standards                                            | Strong for the operating organization | Requirements on the integrity of a polity's own decision process                         |
| Community context                                                                                                   | ISO 37101 (sustainable development in communities, management system); ISO 37120 / 37122 / 37123 (city indicators); ISO 18091 (ISO 9001 in local government); ISO 37106 (smart city operating models) | Partial                               | Indicators and service quality, not participatory decision mechanics                     |
| ASR-01 Identity and access                                                                                          | ISO/IEC 27001 / 27002; ISO/IEC 24760 (identity management); ISO/IEC 29115 (authentication assurance)                                                                                                  | Strong                                | Membership and eligibility assurance for civic participation (TRU-ELIG-001)              |
| ASR-02 Operator access transparency                                                                                 | ISO/IEC 27017 (cloud controls); ISO/IEC 27018 (PII in public cloud)                                                                                                                                   | Partial                               | Tenant-visible, time-boxed operator access as a requirement                              |
| ASR-03 Encryption                                                                                                   | ISO/IEC 27002 cryptography controls                                                                                                                                                                   | Strong                                | None                                                                                     |
| ASR-04 Tamper-evident audit log                                                                                     | ISO/IEC 27002 logging controls; ISO 15489-1 (records management)                                                                                                                                      | Partial                               | Hash-chained governance event log with replayable Decision Provenance                    |
| ASR-05 Records and retention                                                                                        | ISO 15489-1; ISO 30301 (management systems for records); ISO 16175 (records in software)                                                                                                              | Strong                                | None beyond jurisdiction schedules                                                       |
| ASR-06 Accessibility                                                                                                | ISO/IEC 40500:2025, which is WCAG 2.2; ISO 9241-171 (software accessibility)                                                                                                                          | Strong                                | None. ASR-06 adopts 40500:2025, so the floor is WCAG 2.2 AA                              |
| ASR-07 Privacy                                                                                                      | ISO/IEC 27701 (privacy information management); ISO/IEC 29100 (privacy framework)                                                                                                                     | Strong                                | Ballot secrecy and separation of eligibility credentials from participation records      |
| ASR-08 Legal-status labeling                                                                                        | None                                                                                                                                                                                                  | None                                  | Entire control                                                                           |
| ASR-09 Incident response                                                                                            | ISO/IEC 27035 (incident management); ISO 22301 (business continuity)                                                                                                                                  | Strong                                | None                                                                                     |
| ASR-10 Supply chain                                                                                                 | ISO/IEC 27036 (supplier relationships); ISO/IEC 5962 (SPDX, for the SBOM)                                                                                                                             | Strong                                | None                                                                                     |
| ASR-11 Portability and exit                                                                                         | ISO/IEC 19941 (cloud interoperability and portability)                                                                                                                                                | Strong                                | Exit without operator discretion as a hard requirement                                   |
| 43.3 Operator certification                                                                                         | ISO/IEC 27001; ISO/IEC 27006 and ISO/IEC 17021-1 (bodies certifying management systems); ISO/IEC 17065 (bodies certifying products and services)                                                      | Strong                                | None. 17065 is the natural basis for an ACECOG conformance mark                          |
| 43.4 Jurisdiction Compliance Packs                                                                                  | ISO 37301's compliance-obligations clauses                                                                                                                                                            | Partial                               | Machine-enforced jurisdiction profiles with a one-way ratchet (CMP-PACK-001)             |
| 43.5 AI governance                                                                                                  | ISO/IEC 42001 (AI management system); ISO/IEC 23894 (AI risk management); ISO/IEC 42005 (AI system impact assessment); ISO/IEC 22989 (AI concepts)                                                    | Strong for the organization           | AI neutrality in civic agenda-setting, drafting, and feeds (AI-NEUTRAL-001, UIX-NEUTRAL) |
| 43.6 Operator neutrality                                                                                            | ISO 37009:2025 (conflict of interest in organizations, guidance); ISO 37001 (anti-bribery); ISO 37002 (whistleblowing); ISO 19011 (auditing, including auditor independence)                          | Partial                               | Outcome-neutral compensation and process-only roles for civic platform providers         |
| Outside Section 43: invariant floor, deliberation and authority model, federation-as-treaty, Floor Revision Process | None                                                                                                                                                                                                  | None                                  | The core of ACECOG                                                                       |

**Reading the table.** The "Strong" rows are supporting infrastructure that a new standard references, not rewrites. ISO 37009 is guidance only, published in September 2025 by ISO/TC 309 (ISO); it supports 43.6 but does not make its rules certifiable. The last column, read top to bottom, is the scope of the proposed standard.

## I.2 Proposed Standard Group: Civic Self-Governance Systems

The proposal is a multi-part ISO standard group whose normative core is the I.1 gap column: governance-integrity requirements for civic decision systems, with existing ISO standards referenced for everything else. ACECOG becomes the reference implementation, not the standard itself.

**Framing for a consensus body.** The working title should be neutral and testable: "Civic self-governance systems." Decided: the Type-I and civilizational-maturity framing (Part III) stays out of the title, scope, and normative clauses; it may appear only as motivation in the Introduction. ISO scopes must be measurable, and a Kardashev reference in a title or scope clause would likely draw objections that slow approval without changing any requirement.

**Three conformance subjects.** The standard certifies three different things, and each part says which one it applies to:

- **System:** the software or platform (conformance against the invariant floor and assurance controls, certified under ISO/IEC 17065).

- **Operator:** the organization hosting or implementing it (management-system certification under ISO/IEC 17021-1).

- **Adopting civic body:** a jurisdiction or council using a conforming system (self-declaration or third-party attestation).

### I.2.1 Proposed Parts

| Part          | Title                                                              | Type                               | Draws on ACECOG                                                                                                                                                                                                | Builds on                                           |
|---------------|--------------------------------------------------------------------|------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| 1             | Vocabulary and principles                                          | Guidance                           | Canonical object model (7); principles of subsidiarity, authority envelopes, provenance                                                                                                                        | ISO 37000; ISO/IEC 22989                            |
| 2             | Governance integrity requirements for civic decision systems       | Requirements (system)              | Section 14 invariants 1–26 and execution requirements RES-REGISTRY-001 and CAB-HONEST-001; deliberation, authority, and approval state machines; Decision Provenance and replay; Floor Revision Process (14.1) | None; this is the new core                          |
| 3             | Assurance controls                                                 | Requirements (system and operator) | Assurance Controls ASR-01..11 (43.2)                                                                                                                                                                           | ISO/IEC 27001 / 27002, 27701, 15489-1, 40500, 19941 |
| 4             | Jurisdiction profiles                                              | Guidance, with a profile template  | Compliance Packs and the one-way ratchet (43.4)                                                                                                                                                                | ISO 37301 compliance obligations                    |
| 5             | AI in civic decision processes                                     | Requirements                       | AI authority boundary (10, 24), AI-NEUTRAL-001, AI-PROV-001, AI-CHANGE-001, AI-TRAIN-001, AI-LABEL-001, feed neutrality (11.6)                                                                                 | ISO/IEC 42001, 23894, 42005                         |
| 6             | Federation and interoperability                                    | Requirements                       | Federation Contract, trust tiers, provenance exchange format (22)                                                                                                                                              | ISO/IEC 19941                                       |
| 7             | Requirements for operators, implementers, and certification bodies | Requirements (operator)            | Operator neutrality and audit independence (43.6, OPS-NEUTRAL-001 and OPS-AUDIT-001)                                                                                                                           | ISO/IEC 17021-1, 17065, 27006; ISO 37009; ISO 19011 |
| 8 (candidate) | Commons, prosperity floor, and guardian jurisdiction profiles      | Requirements (optional profile)    | Part V module floors (14.2)                                                                                                                                                                                    | ISO 37101; ISO 14001                                |

Parts 1 and 2 carry most of the novelty and should be proposed first. Parts 3 and 7 are largely assembly of existing standards and can follow quickly. Part 8 is a candidate: its rules bind only civic bodies that adopt the Part V modules, so it is an optional profile rather than part of the core.

### I.2.2 Route Through ISO

There are two routes; the recommended sequence uses both.

**1. International Workshop Agreement (first).** An IWA is produced through a workshop rather than the full technical-committee process. ISO describes it as a fast route to a recognized ISO document, with format and process largely set by the proposer (JSA summary of the ISO IWA process). A proposal may come from any source; a proposer that is not an ISO member body or liaison organization must notify its national member body, which is ANSI in the US (IWA proposal form). The proposal goes to the Technical Management Board; once approved, ISO circulates the workshop invitation with 90 days' notice. An IWA is reviewed three years after publication and can become a Publicly Available Specification, Technical Specification, or International Standard; it lasts at most six years. If an existing committee's scope covers the topic, ISO allocates the IWA to it for maintenance (ISO deliverables).

**2. Committee work item (second).** Conversion to a full multi-part standard runs through a technical committee. The two likely homes are ISO/TC 309, Governance of organizations (which owns ISO 37000, 37001, 37002, 37009, and 37301), and ISO/TC 268, Sustainable cities and communities (ISO 37101, 37120, 37106). Parts 3 and 5 need liaison with ISO/IEC JTC 1/SC 27 (security and privacy) and SC 42 (AI).

**Recommended sequence.** Propose an IWA covering Parts 1 and 2 through ANSI, naming TC 309 and TC 268 as candidate maintenance committees. Use the three-year review to convert it into the multi-part standard, adding Parts 3 to 7.

### I.2.3 Prerequisites Before Submitting

- **Vendor-neutral text.** Rewrite Parts 1 and 2 so no requirement depends on ACECOG's name, code, or architecture choices; ISO will not standardize one product.

- **ISO drafting form.** Convert invariants into "shall" requirements, guidance into "should," and follow the ISO/IEC Directives Part 2 structure.

- **Stakeholder coalition.** Line up pilot jurisdictions, a regional body, civic-technology organizations, and academic governance researchers as named interested parties; an IWA proposal lists them.

- **Evidence of need.** Pilot results against the Section 26 and CMP acceptance tests, plus the I.1 gap analysis.

- **IP position.** ISO takes copyright in published text, and participants declare relevant patents. An open-core reference implementation is compatible with this; decide it before submission.

- **Informal approach.** Contact ANSI's ISO team for an informal discussion of scope and committee fit before drafting the formal proposal.

## I.3 Working Draft: Standard Part 1, Vocabulary and Principles

This is a first vendor-neutral draft for the IWA proposal. Product names, object names, and section numbers from the ACECOG specification are deliberately absent.

**1 Scope.** This document defines terms and principles for civic self-governance systems: information systems through which a civic body forms, deliberates, decides, records, and federates collective decisions. It applies to such systems regardless of jurisdiction, scale, hosting model, or policy domain. It does not specify the substance of any decision.

**2 Normative references.** None for Part 1.

**3 Terms and definitions.**

| No.  | Term                       | Definition                                                                                                                                 |
|------|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| 3.1  | civic body                 | Group of persons that makes collective decisions under a governance process it has adopted or that has been conferred on it                |
| 3.2  | member                     | Person entitled to participate in a civic body's decisions, as established by an eligibility credential                                    |
| 3.3  | eligibility credential     | Record establishing a person's entitlement to participate in a civic body, with a stated level of assurance                                |
| 3.4  | governance process         | Set of rules a civic body has adopted for forming, deliberating, and deciding propositions, including thresholds, roles, and authority     |
| 3.5  | proposition                | Proposal submitted for a civic body's decision                                                                                             |
| 3.6  | deliberation               | Structured consideration of a proposition by members before decision                                                                       |
| 3.7  | decision                   | Outcome of a proposition under a governance process                                                                                        |
| 3.8  | authority envelope         | Bounded scope within which a role or delegate may act without further decision by the civic body (the specification's Delegation Envelope) |
| 3.9  | delegation                 | Revocable transfer of a member's or body's decision right to another party within a stated scope                                           |
| 3.10 | escalation                 | Referral of a matter outside an authority envelope to the party or process holding the required authority                                  |
| 3.11 | exception                  | Decision permitting a departure from an adopted rule for a stated case                                                                     |
| 3.12 | minimum requirements floor | Set of requirements that no governance process, agreement, or configuration may relax                                                      |
| 3.13 | floor edition              | Versioned release of the minimum requirements floor                                                                                        |
| 3.14 | decision record            | Tamper-evident record of a decision, its inputs, its process steps, and the parties and assistants involved                                |
| 3.15 | replay                     | Re-execution of a recorded decision process from its decision record to verify its outcome                                                 |
| 3.16 | federation agreement       | Agreement between civic bodies defining shared decisions, exchanged data, and the rights each retains                                      |
| 3.17 | externality                | Effect of one civic body's decision on persons or interests outside that body                                                              |
| 3.18 | AI assistant               | Automated system that drafts, summarizes, translates, or analyzes content within a civic self-governance system                            |
| 3.19 | operator                   | Organization hosting or administering a civic self-governance system for one or more civic bodies                                          |
| 3.20 | legal effect declaration   | Record stating the legal status of a class of decisions and the authority that confers it                                                  |
| 3.21 | standing                   | Entitlement to take part in a governance process, resting on identity assurance and the civic body's charter, never on payment             |
| 3.22 | resource commitment        | Recorded promise of funds, personnel, stocks, or capacity to a decided action                                                              |
| 3.23 | non-compensable objective  | Mandatory objective, right, or protected floor that no gain on another criterion may offset                                                |

**4 Principles.** A civic self-governance system should embody the following principles. Part 2 makes them testable.

1.  **Legitimacy through verifiable process.** A decision's legitimacy rests on a process any member can verify, not on trust in the system's provider.

2.  **Bounded authority.** Every role, delegate, operator, and AI assistant acts only within an explicit, inspectable scope.

3.  **Subsidiarity.** Decisions are made by the smallest civic body able to make them; larger bodies coordinate by proposition and agreement, not command.

4.  **Floor, not ceiling.** Minimum requirements protect process integrity; civic bodies may add to them but never relax them.

5.  **Neutrality.** The system, its operator, and its AI assistants do not favor any proposition, participant, or outcome.

6.  **Accountability.** Monitoring, sanctions, and audits are themselves monitored, graduated, and independent.

7.  **Portability.** A civic body can leave any provider with its complete records and decision history intact.

## I.4 Working Draft: Standard Part 2, Governance Integrity Requirements for Civic Decision Systems

Part 2 states 50 system requirements in clauses 4 to 16, two requirements on adopting civic bodies in clause 17, and conformance rules in clause 18. Together they trace every v0.20 Section 14 invariant (1–26), plus two execution requirements that left the floor in v0.20; Part V module-floor rules (14.2) go to candidate Part 8. The "Derived from" column is informative only, for the drafting team; it would not appear in the published standard. Invariant numbers below are v0.20 numbers; Appendix K maps them to earlier editions.

**1 Scope.** This document specifies requirements for civic self-governance systems that protect the integrity of a civic body's decision process. It applies to the system (as product or service). Requirements on operators are limited to those that bound the operator's authority within the system; other operator requirements are in Part 7.

**2 Normative references.** Part 1 (vocabulary). Requirements referencing security, privacy, and records controls are in Part 3.

**3 Terms and definitions.** As in Part 1.

| Clause                                  | ID    | Requirement                                                                                                                                                                                                                                                                                                             | Derived from (informative)                        |
|-----------------------------------------|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| 4 Membership, eligibility, and access   | R4.1  | The system shall record each member's eligibility credential with its level of assurance.                                                                                                                                                                                                                               | 13 TRU-ELIG-001                                   |
|                                         | R4.2  | The system shall enforce, for each decision class, the minimum level of assurance the governance process sets.                                                                                                                                                                                                          | 13                                                |
|                                         | R4.3  | The system shall not report a participating population larger than the number of valid, unrevoked eligibility credentials in the applicable scope.                                                                                                                                                                      | 13                                                |
|                                         | R4.4  | The system shall store eligibility credentials separately from records of how a member participated.                                                                                                                                                                                                                    | ASR-07                                            |
|                                         | R4.5  | The system shall provide no mechanism to condition any governance function (viewing, proposing, deliberating, voting, delegating, appealing, or verifying a decision record) on a fee, deposit, or contribution history; the only precondition it shall support is identity assurance at the level the action requires. | 24 TRU-ACCESS-001                                 |
|                                         | R4.6  | Identity assurance shall be obtainable at no cost, including by persons without an identity document; duplicate identities shall be reconciled without suspending participation.                                                                                                                                        | 24                                                |
| 5 Governance process                    | R5.1  | Governance process rules shall be configuration adopted by the civic body through a recorded decision, not fixed in the system.                                                                                                                                                                                         | Domain portability (28.1)                         |
|                                         | R5.2  | The system shall permit a civic body to define its own maturity framework, provided the framework waives no requirement of this document and declares its comparability to federation partners.                                                                                                                         | 19 GOV-FRAMEWORK-001                              |
|                                         | R5.3  | A person subject to a compulsory collective funding obligation set through the system shall have standing in the process that sets, amends, or renews it.                                                                                                                                                               | 25 GOV-VOICE-001                                  |
| 6 Propositions and deliberation         | R6.1  | The system shall permit any eligible member, and non-members where the governance process allows, to submit a proposition.                                                                                                                                                                                              | Guest Proposer journey (30.5)                     |
|                                         | R6.2  | The system shall not order, rank, or notify participants of propositions using engagement optimization; ordering rules shall be published and applied equally, and the reason an item is shown shall be visible.                                                                                                        | Feed neutrality (11.6.6)                          |
|                                         | R6.3  | The system shall identify propositions whose similarity to recorded precedent falls below the governance process's novelty threshold and shall require the additional review that process specifies before approval.                                                                                                    | GOV-VARIETY-001 (framework control, 17.5.1)       |
| 7 Authority, delegation, and escalation | R7.1  | The system shall check every state-changing action against a valid authority path and shall refuse or escalate any action without one.                                                                                                                                                                                  | 2                                                 |
|                                         | R7.2  | No automated action shall take effect outside the delegation scope active when it is taken.                                                                                                                                                                                                                             | 7                                                 |
|                                         | R7.3  | Delegations shall be scoped, recorded, and revocable by the delegator at any time.                                                                                                                                                                                                                                      | Citizen delegation (30.7)                         |
|                                         | R7.4  | A decision of one civic body shall bind another only with explicit authority or agreement; otherwise one body may affect another only by submitting a proposition to it.                                                                                                                                                | 6; coordination by proposition (30.6)             |
| 8 Evidence and decision support         | R8.1  | The system shall distinguish observed evidence from inference, scenario assumption, and hypothesis, and shall not treat uncertain evidence as establishing a normative requirement unless a decision adopts it.                                                                                                         | 4; evidence classes (20.1)                        |
|                                         | R8.2  | No hard constraint shall be relaxed except by a recorded decision of the party holding authority over it.                                                                                                                                                                                                               | 3                                                 |
|                                         | R8.3  | No optimization or scoring criterion shall offset a non-compensable objective; any shortfall below a protected floor shall be recorded as a breach.                                                                                                                                                                     | 9 OPT-NONCOMP-001                                 |
|                                         | R8.4  | A decision-support result shall be eligible to inform a commitment only if it records the model, version, and configuration identifiers needed to reproduce it.                                                                                                                                                         | 8                                                 |
| 9 Decision records                      | R9.1  | The system shall create a decision record for every decision.                                                                                                                                                                                                                                                           | Decision Provenance (9)                           |
|                                         | R9.2  | No approved state, decision, evidence, baseline, or model version shall be destructively overwritten, and forecasts and actuals shall be stored separately from the baselines they are compared against.                                                                                                                | 1, 5                                              |
|                                         | R9.3  | Decision records shall be tamper-evident, and their integrity shall be verifiable without the operator's tools.                                                                                                                                                                                                         | ASR-04, CMP-012                                   |
|                                         | R9.4  | Replay of a decision record shall reproduce the recorded outcome.                                                                                                                                                                                                                                                       | 11                                                |
|                                         | R9.5  | Any member, and the public where the governance process or law provides, shall be able to verify a decision record without holding an account.                                                                                                                                                                          | Citizen verification (30.7)                       |
|                                         | R9.6  | The system shall display each decision's legal status and shall not present it as binding without a legal effect declaration.                                                                                                                                                                                           | 26 ASR-STATUS-001                                 |
|                                         | R9.7  | A later rule change shall not alter past settlements, accrued entitlements, or the recorded reasons for an earlier decision.                                                                                                                                                                                            | 1 DPP-IMMUTABLE-001                               |
| 10 Commitments                          | R10.1 | Each resource commitment shall be registered once, and the system shall refuse a commitment that would promise the same resource twice.                                                                                                                                                                                 | RES-REGISTRY-001 (requirement, 19.5)              |
|                                         | R10.2 | A commitment shall be reported as assured only after its resources, providers, dependencies, and activation arrangements pass readiness checks; otherwise the system shall report the gap.                                                                                                                              | CAB-HONEST-001 (requirement, 34.3)                |
| 11 Monitoring and sanctions             | R11.1 | The system shall grant approval or monitoring authority only through a recorded selection or ratification by the governance process, shall refuse any appointment made by the appointee or by a role the appointee monitors, and shall record each role's rotation and recall terms.                                    | 17 TRU-MONITOR-001                                |
|                                         | R11.2 | The system shall maintain each approver's approval track record and surface it when rotation or recall is considered, without itself triggering recall.                                                                                                                                                                 | TRU-MONITOR-002 (requirement, 12.0.1)             |
|                                         | R11.3 | The system shall issue a notice or warning for a first or minor breach before initiating escalation, unless the breach is independently material, and shall apply sanctions only to governance privileges.                                                                                                              | 18 GOV-GRADUATED-001                              |
| 12 Exceptions                           | R12.1 | Every material exception shall identify the conflicting rule or objective and the authority required to resolve it.                                                                                                                                                                                                     | 10                                                |
|                                         | R12.2 | The system shall track cumulative effect on each identifiable constituency across a rolling window and shall raise a cumulative exception when that effect crosses the single-decision materiality threshold.                                                                                                           | 16 GOV-CUMULATIVE-001                             |
| 13 AI assistance                        | R13.1 | AI assistants shall hold no decision authority; their outputs shall take effect only through a human action subject to R7.1.                                                                                                                                                                                            | 2; AI-COMMIT-001                                  |
|                                         | R13.2 | AI-drafted or AI-summarized content presented for a material decision shall preserve the substance and relative framing supplied by its human authors, and any AI-introduced change shall be flagged and comparable side by side with the original.                                                                     | 15 AI-NEUTRAL-001                                 |
|                                         | R13.3 | The system shall classify AI tasks by their potential to influence outcomes and shall capture the inputs and outputs of influencing tasks as evidence linked to the affected decision records.                                                                                                                          | AI task classes and evidence capture (24.2, 24.4) |
|                                         | R13.4 | Every AI-assisted item shall record the model and version that produced it, and AI-generated or AI-translated text shall be labeled to participants.                                                                                                                                                                    | AI-PROV-001, AI-LABEL-001                         |
| 14 Federation                           | R14.1 | A federation agreement shall declare the externalities it exposes and the rights each party retains.                                                                                                                                                                                                                    | Federation Contract (22.2)                        |
|                                         | R14.2 | Before a federated decision is finalized, the system shall check it against every party's non-compensable objectives and shall block decisions that would violate them.                                                                                                                                                 | 14 FED-RIGHTS-001                                 |
|                                         | R14.3 | Each party to a federation shall be able to see which floor edition, maturity framework, and hosting model every other party operates under.                                                                                                                                                                            | 22 FED-EDITION-001; 22.5.4                        |
| 15 Operator boundaries                  | R15.1 | The operator shall hold no standing authority in any civic body's governance process, and no operational role shall bypass an authority check.                                                                                                                                                                          | 23 TRU-TENANT-001                                 |
|                                         | R15.2 | Operator access to a civic body's data shall be time-limited, justified, recorded, and visible to that civic body.                                                                                                                                                                                                      | ASR-02                                            |
|                                         | R15.3 | A civic body shall be able to export everything needed to continue its governance independently, in documented open formats, without operator discretion.                                                                                                                                                               | 12 TRU-EXIT-001                                   |
| 16 Minimum requirements floor           | R16.1 | No governance process, federation agreement, profile, or configuration shall relax a requirement of this document.                                                                                                                                                                                                      | 19 GOV-FRAMEWORK-001 (layer rule)                 |
|                                         | R16.2 | Every proposed floor change shall be classified as strengthening or weakening by a published rule that also applies to changes to itself.                                                                                                                                                                               | 20 GOV-FLOOR-001                                  |
|                                         | R16.3 | A weakening proposal shall require independent verification, by a reviewer distinct from the proposer and the editors, before adoption.                                                                                                                                                                                 | 20                                                |
|                                         | R16.4 | Each civic body shall adopt new floor editions through its own governance process; adoption shall never be compelled, and the edition in use shall be visible to members and federation partners.                                                                                                                       | 14.1 Stage 3b; 22                                 |
|                                         | R16.5 | The floor revision process shall be open to public drafting and comment.                                                                                                                                                                                                                                                | 14.1 Stage 1                                      |
|                                         | R16.6 | An amendment to a civic body's own governance process that weakens a protection, including an amendment to its amendment rule, shall require the threshold that would govern the change it enables.                                                                                                                     | 21 GOV-RATCHET-001                                |

**17 Requirements on adopting civic bodies.** A civic body that claims to govern through a conforming system:

- **C17.1** shall apply the rotation and recall terms recorded for each approval or monitoring role, and shall consider the role-holder's approval track record whenever it decides on rotation or recall (supports R11.1–R11.2; derived from 17 and TRU-MONITOR-002);

- **C17.2** shall define graduated responses to breaches in its governance process and apply them as defined (supports R11.3; derived from 18).

**18 Conformance.** A system conforms to this document only if it meets every requirement in clauses 4 to 16. A civic body conforms only if it governs through a conforming system and meets clause 17, by self-declaration or third-party attestation. Claims of partial conformance are not permitted.

**Drafting notes.**

- **Resolved: invariant trace.** Done against the v0.20 register (1–26). Part V module-floor rules (14.2) are held for candidate Part 8.

- **Resolved: invariant IDs.** Every v0.20 invariant has an ID, and IDs are the primary reference (Section 14).

- **Resolved: monitoring scope.** Split by conformance subject. R11.1–R11.3 bind the system (enforce ratification, refuse self-appointment, record terms and track records, apply graduated responses); clause 17 binds the adopting civic body to actually rotate, recall, and sanction as its process defines.

- **Resolved: no-cost access.** Kept mandatory in the core and phrased as a product property (R4.5): the system provides no mechanism to charge for participation. That is testable, and it does not regulate what a jurisdiction charges for other services. The "open participation" conformance option is no longer needed.

**Sources.** StateTech on the GovRAMP rebrand · Compyl GovRAMP and TX-RAMP guide. ISO references in I.1 and I.2 cite ISO and W3C pages where linked; others are from general knowledge and should be confirmed against the ISO catalogue before submission. Statutory citations in 43.4 are from general knowledge and are listed for counsel verification in 43.8.

# Appendix J — v0.19 Compliance & Assurance Integration Notes

v0.19 integrates the Compliance & Assurance addendum drafted between 26 September and 6 November 2026 as a standalone working document and merged here. Section 43 is the umbrella compliance module for the whole specification. Its standards crosswalk and ISO standard-group proposal are supporting evidence in Appendix I.

Reconciliations made at merge:

- **Renumbered.** The addendum was drafted as Part V, Section 31, with invariants 52–57. v0.18 had already assigned Part V, Sections 31–42, and invariants 52–65 to the Prosperity, Commons & Guardian modules, so the addendum is now Part VI, Section 43, with invariants 66–70.

- **Exit invariant folded into invariant 38.** A drafted exit invariant duplicated invariant 38. Its stronger wording (documented open formats, no operator discretion) is applied to invariant 38 instead. With 66–70, the register runs from 27 to 70, which is 44 invariants.

- **All six changes are strengthening Floor Revision Proposals.** Invariants 66–70 and the invariant 38 amendment each add or tighten a protection under 14.1 (open drafting and local ratification, no independent-verification gate).

- **"Assurance Plane" renamed Assurance Controls.** Section 2 already defines a Civic Trust Plane covering identity, privacy, security, audit, and portability, so the controls sit inside it rather than forming a sixth plane. They are distinct from Civic Assurance and Buffering (34).

- **AI requirement IDs aligned with the existing AI prefix.** The drafted AI-01 to AI-04 are now AI-PROV-001, AI-CHANGE-001, AI-TRAIN-001, and AI-LABEL-001.

- **Accessibility floor raised.** WCAG 2.1 AA becomes WCAG 2.2 AA (ISO/IEC 40500:2025) in 12.1 and ASR-06.

- **Compliance evidence moved to an appendix.** The ISO crosswalk, the proposed standard group, and the working drafts of Standard Parts 1 and 2 (drafted as 31.9 and 31.10) are Appendix I.

Existing text updated to point to Section 43:

- **Section 2 (planes table):** the Civic Trust Plane row lists compliance and assurance controls (43).

- **4.2 (GML):** the Assurance Controls apply at every level. GML-1's "defined retention period" now reads as formal adoption of a retention schedule, and GML-2's "accessibility compliance mandatory" now reads as an independent accessibility audit, because ASR-05 and ASR-06 already apply at every level.

- **Section 7:** six canonical objects added (43.7.1).

- **Section 12:** closing pointer to Section 43.

- **12.1:** rewritten as a pointer to Section 43, keeping the MVP hygiene list and the standing disclaimer.

- **13.1:** Phase 1 includes the Assurance Controls, the applicable pack's open-meeting guard, and certification if the pilot uses shared hosting.

- **Section 14:** numbering note, invariant 38 strengthened, invariants 66–70 appended.

- **22.5.1:** shared-tier certification and operator-conduct pointer.

- **23.2 and 23.4:** pointers to ASR-05, ASR-07, 43.2, and 43.3.

- **Section 27:** ASR, CMP, and OPS prefixes added.

- **28 and 28.1.2:** legal-recognition limits now note what Jurisdiction Compliance Packs and Legal Effect Declarations cover.

Reference corrections to v0.18 text:

- **Invariant 50** cited "(40)" for the federation interoperability declaration; it now cites 4.3 and invariant 45.

- **14.1 Stage 3b** cited "22.10's federation design principles" and "Section 9/12.2"; neither section exists. They now cite 22.2's Federation Contract exit and amendment terms, and Sections 9 and 21.3.

- **Appendix E** carried the same 22.10 reference, now 22.2. Its v0.8 paragraph no longer describes three completed benchmark passes as anticipated.

- **The title block** lines for v0.8 to v0.11 were cut off; they are completed.

Decisions confirmed at merge (6 November 2026):

- **31.8 settled items confirmed.** Watershed is the default boundary unit, with ecoregion as a charter option. A guardian holds a binding veto inside its own ecosystem only over a certified ecological-limit breach (37.4), and a suspensive veto over effects that cross boundaries. Standing rests on identity plus charter, never payment (invariant 53).

- **Non-resident payers.** The default in invariant 54 is confirmed: standing on the obligations they pay only.

- **Residency period for commons benefits.** Each charter sets the period, capped at 12 months (CE-10). The cap follows the Alaska Permanent Fund Dividend's full-calendar-year residency rule.

- **Draw band.** The rule-based draw stays at a default of 5% of trailing five-year average market value, within a ratified band of 4–5% (CE-02, 37.5). The minimum momentum-reinvestment share remains open.

- **Standard Part 2 monitoring scope.** Split by conformance subject: R11.1–R11.3 bind the system, and clause 17 binds the adopting Civic Body (I.4).

- **Standard Part 2 no-cost access.** Kept mandatory in the core, phrased as a product property (R4.5).

Still open:

- **30.4 Journey Catalog Status** still shows Facilitator/Clerk, Auditor, and Federation Partner as deferred and omits Fund Manager and Program Manager. Scheduled for a separate session.

- **IDs for invariants 27–38,** so traces in Appendix I can use stable IDs throughout.

- **The legal review items in 43.8.**

- **The pilot workbook amendment noted in Appendix H.**

- **Remaining 31.8 items:** the minimum momentum-reinvestment share, and the certification method for documented interdependence (invariant 61).

- **Other numbered lists also use the document-wide count.** For example, 8.3's steps run 22–26 and 24.3's run 63–68. Journeys cite them by those numbers (30.5 cites 8.3 step 26), so they are left unchanged.

# Appendix K — v0.20 Architecture Normalization and Freeze Summary

v0.20 is the architecture freeze candidate. It adds no new conceptual module. It normalizes the architecture that v0.19 already contained and closes the blocker the red-team found. Every change traces to an entry in the ACECOG Change Management Protocol and Log (CL-007 to CL-034), which holds the full analysis.

## K.1 Changes Applied in v0.20

| Log entry        | Change                                                                                                                      | Where                        |
|------------------|-----------------------------------------------------------------------------------------------------------------------------|------------------------------|
| CL-007           | Invariant triage: floor reduced from 44 invariants to 26                                                                    | 14, K.2                      |
| CL-008           | Seven protection layers, module floors, and the layer rule                                                                  | 14.0, 14.2, invariant 19     |
| CL-009, CL-011   | IDs for every invariant, IDs as primary references, register renumbered 1–26, procedural lists restarted at 1               | 14, throughout               |
| CL-010           | 0.x drafts outside change management; 14.1 applies from 1.0                                                                 | 14.1                         |
| CL-012           | Four-axis decision status model                                                                                             | 8.0, 8.9, 34.3               |
| CL-013           | Model outputs stated as conditional                                                                                         | 20.1, 36.5, 42               |
| CL-014           | Six meanings of "floor" defined; Guardian module floor renamed; Delegation Envelope mapped to the Standard's term           | 14.0, 37, I.3                |
| CL-015           | Two ID schemes stated; RES and INV prefixes; MVP, PT-AT, SRBG-AT, CAB-AT, PF-AT, and GJ-AT test IDs                         | 26.2, 27, Part V             |
| CL-016           | Journey Catalog Status table corrected                                                                                      | 30.4                         |
| CL-017, CL-032   | Bears Ears date and Section 40 figures corrected and sourced                                                                | 38.2, 40.3, 35.3, Appendix H |
| CL-018 to CL-020 | Guardian Council selection and accountability, Commission independence, expiring limits, veto appeal, suspensive-veto lapse | 37.4, 37.5                   |
| CL-021 to CL-023 | Certified revenue classification, endowment investment and fee rules, prospective standing changes                          | 35.4, 36.4, 36.6             |
| CL-024           | Model-output explanations treated as influencing AI tasks                                                                   | 24.2                         |
| CL-025, CL-026   | Operator defaults take effect only on adoption; participation-restricting pack constraints must cite law                    | 43.4, 43.6                   |
| CL-027           | Consent recorded only as the nation's own act; admission test and floor review for invariants                               | 38.2, 14.1                   |
| CL-031, CL-034   | Traceability verified; an acceptance test for every invariant                                                               | 14                           |

## K.2 Invariant Concordance

| v0.19 | v0.20 | ID                 | Disposition                                                             |
|-------|-------|--------------------|-------------------------------------------------------------------------|
| 27    | 1     | DPP-IMMUTABLE-001  | Kept; absorbs 65                                                        |
| 28    | 2     | GOV-AUTHPATH-001   | Kept                                                                    |
| 29    | 3     | OPT-CNST-001       | Kept                                                                    |
| 30    | 4     | EVD-NORM-001       | Kept                                                                    |
| 31    | 5     | EXE-BASELINE-001   | Kept                                                                    |
| 32    | 6     | FED-AUTH-001       | Kept                                                                    |
| 33    | 7     | GOV-ENVELOPE-001   | Kept                                                                    |
| 34    | 8     | OPT-REPRO-001      | Kept                                                                    |
| 35    | 9     | OPT-NONCOMP-001    | Kept; absorbs 63                                                        |
| 36    | 10    | GOV-EXCEPT-001     | Kept                                                                    |
| 37    | 11    | DPP-REPLAY-001     | Kept                                                                    |
| 38    | 12    | TRU-EXIT-001       | Kept                                                                    |
| 39    | 13    | TRU-ELIG-001       | Kept                                                                    |
| 40    | 14    | FED-RIGHTS-001     | Kept                                                                    |
| 41    | 15    | AI-NEUTRAL-001     | Kept                                                                    |
| 42    | 16    | GOV-CUMULATIVE-001 | Kept                                                                    |
| 43    | 17    | TRU-MONITOR-001    | Kept                                                                    |
| 44    | 18    | GOV-GRADUATED-001  | Narrowed; the notice-first ladder moves to 5.11.1 as reference practice |
| 45    | 19    | GOV-FRAMEWORK-001  | Generalized into the layer rule; absorbs 66 and 67                      |
| 46    | —     | GOV-VARIETY-001    | Moved to a Reference Maturity Framework control (17.5.1)                |
| 47    | —     | TRU-MONITOR-002    | Moved to a requirement (12.0.1)                                         |
| 48    | 20    | GOV-FLOOR-001      | Kept; now also covers module floors                                     |
| 49    | 21    | GOV-RATCHET-001    | Kept                                                                    |
| 50    | 22    | FED-EDITION-001    | Kept                                                                    |
| 51    | 23    | TRU-TENANT-001     | Kept                                                                    |
| 52    | 24    | TRU-ACCESS-001     | Kept                                                                    |
| 53    | —     | GOV-PROSPERITY-001 | Moved to the Prosperity module floor (35.4)                             |
| 54    | 25    | GOV-VOICE-001      | Kept                                                                    |
| 55    | —     | GOV-COMMONS-001    | Moved to the Commons module floor (36.6)                                |
| 56    | —     | GOV-COMMONS-002    | Moved to the Commons module floor (36.6)                                |
| 57    | —     | ECO-GUARD-001      | Moved to the Guardian module floor (37.5)                               |
| 58    | —     | ECO-GUARD-002      | Moved to the Guardian module floor (37.5)                               |
| 59    | —     | ECO-GUARD-003      | Moved to the Guardian module floor (37.5)                               |
| 60    | —     | ECO-COLLATERAL-001 | Moved to the Commons module floor (36.6)                                |
| 61    | —     | FED-SYMBIOSIS-001  | Moved to the Guardian module floor (37.5)                               |
| 62    | —     | RES-REGISTRY-001   | Moved to an execution requirement (19.5)                                |
| 63    | 9     | GOV-FLOOR-002      | Merged into OPT-NONCOMP-001                                             |
| 64    | —     | CAB-HONEST-001     | Moved to a CAB requirement (34.3), worded "operationally verified"      |
| 65    | 1     | SRBG-SETTLE-001    | Merged into DPP-IMMUTABLE-001                                           |
| 66    | 19    | ASR-FLOOR-001      | Merged into the layer rule                                              |
| 67    | 19    | CMP-PACK-001       | Merged into the layer rule                                              |
| 68    | 26    | ASR-STATUS-001     | Broadened to the lifecycle and legal-status axes (8.0)                  |
| 69    | —     | OPS-NEUTRAL-001    | Moved to an operator certification requirement (43.6)                   |
| 70    | —     | OPS-AUDIT-001      | Moved to an operator certification requirement (43.6)                   |

Moved rules keep their IDs, so existing traces still resolve. Retired invariant numbers are not reused. Historical appendices (C to J) keep the numbers that were current when they were written.

Under 14.1, fifteen of these changes would be weakening (44, 46, 47, 53, 55–62, 64, 69, 70). Because v0.20 is a 0.x draft, they were made directly; colleague circulation of the draft serves as review.

## K.3 Architecture Freeze Summary

**Blockers.** None remain. The one blocker the red-team found, the Guardian Council's undefined selection and accountability (CL-018), is closed by GJ-F1 in 37.5.

**Recommended corrections.** All applied (K.1).

**Non-blocking improvements, held on the backlog:**

- All four v0.20 backlog items were applied in v0.22: identity tiers and outcome-changing reconciliation (CL-028, 23.1.1), delegation concentration and reconfirmation (CL-029, 17.5), the endowment withdrawal rule (CL-030, CE-F6), and the Civic Body capitalization pass (CL-014; compound adjectives such as "civic-body-controlled" stay lowercase).

**Deferred features:**

- Sortition, consensus, and transitive (liquid) delegation chains (28.1.2); single-level delegation is Phase 1 (17.5).

- Institutional actors as first-class federation parties (28.1.2).

- Funding Instrument types other than Appropriation, and the Part V subtypes (5.13, 40).

- Endowment simulator v0.2 (42.5).

- Standards-process tooling for Floor Revision Proposals (INV-AT-20).

- The cosmic-scale sections of Part III, kept as catalog reserve.

**Assumptions requiring validation:**

- A continuous LP relaxation is adequate for the allocation decisions in early pilots (18).

- Replay is deterministic where solvers and seeds are pinned, and best-effort otherwise (9).

- No-cost, ad hoc identity issuance with later reconciliation resists duplicate identities in practice (invariant 24).

- Jurisdictions will recognize Legal Effect Declarations for at least some decision classes (8.0, 43.2).

- The endowment simulator, once calibrated with real data, supports the module-floor rules (42.5).

- Existing legal tools (easements, compacts, special districts) can carry Guardian Jurisdictions (37.7).

- A GovRAMP path is available to a shared platform in Colorado, if the pilot is hosted (43.3); Colorado's position is to be confirmed.

- A shared platform can serve a region of several hundred jurisdictions (22.5).

- Feed and AI neutrality are measurable with the UIX-NEUTRAL tests (11.6.8).

- The open legal items in 43.8.

- The certified result of San Francisco's Proposition B (40.3).

**Proposed frozen baseline.** These parts of the architecture are frozen as of v0.20:

- The Invariant Floor (1–26), the seven protection layers, and the module floors (Section 14).

- The canonical object model (Section 7).

- The state machines and the four-axis decision status model (Section 8).

- Decision Provenance and replay (Section 9).

- The AI authority boundary (Sections 10 and 24).

- The planes and interaction architecture (Sections 2, 11, and 11.6).

- Federation, hosting, and trust tiers (Section 22).

- The Part V modules as optional modules behind their module floors.

- Compliance and Assurance (Section 43).

After the freeze, every change still enters through the change log. From version 1.0, Invariant Floor and module-floor changes also follow 14.1.

**Next milestone.** The next milestone is the ACECOG Civic OS Development Environment / Simulator Alpha, not another specification release. It derives the developer specification (schemas, APIs, state machines, authority gates, provenance structures, test fixtures, and UI behavior) from this baseline. It uses the Ecosystem Endowment Simulator and the Riverbend Commons portfolio scenario (26.1) as its first executable demonstrations.

# Appendix L — v0.21 Build-Readiness Patch

v0.21 applies six entries from the change log (CL-035 to CL-040) in response to an external build-readiness review of v0.20. Like v0.20, it adds no conceptual module.

| Log entry | Change                                                                                                                                        | Where     |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| CL-035    | Phase 1 execution filter for every section                                                                                                    | 13.6      |
| CL-036    | Phase 1 solver profile: LP and convex QP only; higher-order terms off; non-convex QP rejected with a reason                                   | 5.3, 13.1 |
| CL-037    | Local-first defined as a civic-body-controlled authoritative installation; reconciled with shared hosting and with desktop and mobile clients | 11.5      |
| CL-038    | Version-binding rule: transactions bind to the versions in force when they start                                                              | 8.9       |
| CL-039    | Delegation Envelope parameters defined, with validation and fail-closed defaults                                                              | 5.9       |
| CL-040    | Part III marked catalog reserve with no build phase                                                                                           | 29        |

The review's main finding, that developer contracts do not yet exist, is the next milestone rather than a specification change. CL-041 tracks it: a schema for the Section 7 objects and a mock OpenAPI for the command/query split, derived from this specification (Appendix M), because no prototype code was available.

# Appendix M — Developer Contract v0.1 (CL-041)

Section 15 calls for machine contracts that translate this specification's semantics without changing their meaning. This appendix records the first: an API contract for the command/query split (11.6.2), with a working mock behind it. It was derived from this specification, not from the prototype's code; WBS 1.1.1 and 1.1.2 (13.7) reconcile it with the prototype and turn the differences into the Phase 1 completion backlog.

## M.1 What the Package Contains

| Part           | What it is                                                                                                                             |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------|
| openapi.yaml   | The contract in OpenAPI 3.1: every command and query, its request and response shapes, and worked examples                             |
| Mock server    | A reference implementation with in-memory state, real rule checks, and a deterministic LP and convex QP solver (Phase 1 profile, 13.1) |
| Contract tests | The Riverbend Commons scenario (26.1) driven over HTTP, checking the Phase 1 acceptance tests from outside                             |

One source file defines the contract. The server validates requests against it and the OpenAPI file is generated from it, so documentation and behavior cannot drift apart.

## M.2 Conventions

- **Commands and queries.** Commands change state and are all POST /v0/commands/\<name\>. Queries only read and are all GET /v0/queries/....

- **One envelope for every client.** Desktop, assistant, and mobile send the same command envelope and pass the same checks (11.6.1). An assistant-drafted command must name the person who confirmed the exact payload (24.3).

- **Three outcomes.** Accepted (the change happened), escalated (an Exception Proposition was raised and nothing was decided automatically), or refused (nothing changed; the refusal names the rule, usually by invariant ID). Refused and escalated commands are still recorded (8.1).

- **Status.** Results carry the four status axes of 8.0. Legal status is fixed when a decision closes.

- **Version binding.** Each command reports the rule versions it was bound to when it started (8.9).

- **Idempotency.** Resending a command with the same command ID returns the original result and changes nothing (8.1).

- **Evidence.** The event log is hash-chained (ASR-04). An export can be verified and rehydrated, and replay matches, without operator tools (CMP-007, CMP-012).

## M.3 Commands

| Command                         | What it does                                                                                     | Specification                    | Enforces                                     |
|---------------------------------|--------------------------------------------------------------------------------------------------|----------------------------------|----------------------------------------------|
| civic-bodies.create             | Create a Civic Body with its founding members.                                                   | 7, 17.2, MVP-100                 | —                                            |
| governance-processes.adopt      | Adopt the rules for how each kind of decision is made: method, threshold, and who may take part. | 17.5, 4.2                        | TRU-ACCESS-001, GOV-AUTHPATH-001             |
| authorities.grant               | Give a person or role the authority to do specific things.                                       | 7, 12.0.1, 23.1                  | GOV-AUTHPATH-001, TRU-MONITOR-001            |
| delegation-envelopes.adopt      | Set the bounded space inside which routine decisions may be made automatically.                  | 5.9, 8.7                         | GOV-ENVELOPE-001                             |
| legal-effect-declarations.adopt | Record which law or charter gives a class of decisions legal effect.                             | 43.2 ASR-08, 8.0                 | ASR-STATUS-001                               |
| compliance-packs.adopt          | Adopt a jurisdiction's legal rule bundle. Packs may only add constraints.                        | 43.4                             | GOV-FRAMEWORK-001                            |
| change-requests.put-in-force    | Put an approved change in force. Applies only to transactions that start afterward.              | 8.9                              | DPP-IMMUTABLE-001                            |
| credentials.issue               | Record that a member is a unique, eligible member at an identity tier.                           | 7, 17.5                          | TRU-ELIG-001, TRU-ACCESS-001                 |
| interest-declarations.record    | Declare a personal interest in a proposition; this blocks deliberating and voting on it.         | 43.4, 43.7                       | CMP-004                                      |
| delegations.assign              | Delegate your participation in a decision class to another member.                               | 17.3; CL-029                     | —                                            |
| delegations.revoke              | Withdraw a delegation.                                                                           | 17.3                             | —                                            |
| propositions.submit             | Submit a frozen proposition version for a decision.                                              | 8.3, MVP-101                     | DPP-IMMUTABLE-001, TRU-ELIG-001              |
| propositions.amend              | Amend a proposition. Creates a new version; the old version stays.                               | 8.4                              | DPP-IMMUTABLE-001                            |
| deliberation.post               | Post to the deliberation record on a proposition.                                                | 8.4, 43.4.1                      | CMP-003, CMP-004                             |
| votes.cast                      | Vote or consent on a proposition.                                                                | 17.3, 17.5                       | TRU-ELIG-001, CMP-004                        |
| decisions.close                 | Close a decision, tally it, and record the Collective Will.                                      | 17.4, 8.4, MVP-102               | TRU-ELIG-001, ASR-STATUS-001                 |
| evidence.record                 | Record evidence with its epistemic class.                                                        | 20.1                             | —                                            |
| constraints.attach-evidence     | Use evidence as the basis of a constraint. Uncertain evidence needs a decision first.            | 20.1                             | EVD-NORM-001                                 |
| optimization-runs.request       | Ask the solver for an allocation under the approved model.                                       | 8.6, 13.1, MVP-103               | OPT-CNST-001, OPT-REPRO-001, OPT-NONCOMP-001 |
| baselines.create                | Freeze an approved, commit-eligible result as the baseline.                                      | 8.5                              | OPT-REPRO-001, GOV-AUTHPATH-001              |
| commitments.reserve             | Reserve resources for the baseline, without double-allocating.                                   | 8.7, 19.5, MVP-104               | GOV-AUTHPATH-001                             |
| actuals.post                    | Post what actually happened. Never alters the baseline.                                          | 8.8, MVP-105                     | EXE-BASELINE-001                             |
| rebalances.propose              | Propose a routine reallocation. Inside the envelope it is resolved; otherwise it escalates.      | 5.9, 8.7, 5.11, MVP-106, MVP-107 | GOV-ENVELOPE-001, GOV-EXCEPT-001             |
| exceptions.resolve              | Resolve an Exception Proposition by the authority it names.                                      | 5.11, 8.9, MVP-108               | GOV-EXCEPT-001, DPP-IMMUTABLE-001            |
| exports.create                  | Export everything needed to continue governance elsewhere.                                       | 23.3, ASR-11, MVP-110            | TRU-EXIT-001                                 |
| retention-schedules.adopt       | Adopt a records retention period for a record class.                                             | 43.2 ASR-05                      | —                                            |
| records.delete                  | Delete a record. Allowed only by schedule or legal order, and recorded.                          | 43.2 ASR-05, CMP-005             | —                                            |
| configuration.set               | Change a deployment setting. Settings cannot disable Assurance Controls.                         | 43.2, 14.0                       | GOV-FRAMEWORK-001                            |

**Commands to add for Phase 1 (CL-066).** Revoke a credential; revoke or recall an authority; amend a Governance Process under the ratchet (invariant 21); the clerk's validate, return-for-correction, schedule-deliberation, and publish-provenance actions; Guest Proposer submission with a read-only fit-check preview (30.5); escalate (30.8); the Continuity Case commands (17.9); and the identity commands (23.1.1). Appeal and reconsideration are deferred to Phase 1.5.

## M.4 Queries

| Query                       | Returns                                                                        | Specification           |
|-----------------------------|--------------------------------------------------------------------------------|-------------------------|
| civic-bodies/{id}           | Civic Body, its members, decision classes, and adopted packs.                  | 7                       |
| propositions/{id}           | Every version of a proposition, deliberation record, and votes.                | 8.3, 8.4, MVP-101       |
| decisions/{id}              | A decision with its four status axes.                                          | 8.0                     |
| decisions/{id}/provenance   | Decision Provenance Packet.                                                    | 9                       |
| decisions/{id}/replay       | Replay the decision's optimization from its bound versions and compare hashes. | 9.1, MVP-109            |
| baselines/{id}              | A baseline version and its lineage.                                            | 8.5                     |
| portfolio/{civic_body_id}   | Portfolio nodes, budgets, commitments, actuals, and variance.                  | 5.2, 8.8                |
| exceptions/{id}             | An Exception Proposition: the conflict and the authority required.             | 5.11                    |
| delegations/{civic_body_id} | Delegation chains with concentration disclosure.                               | 17.3; CL-029            |
| feed/{actor_id}             | A member's feed. Every item states why it is shown; order is deterministic.    | 11.6.6, UIX-NEUTRAL-003 |
| events                      | The hash-chained event log (supports ?after=seq).                              | 11.3, ASR-04            |
| exports/{id}                | A completed export package.                                                    | ASR-11                  |

## M.5 Acceptance Coverage

The contract tests ran 48 checks against the mock on the Riverbend Commons scenario; all 48 passed. They cover MVP-100 to MVP-111; INV-AT-04, 08, 13, 17, and 26; the fee rule of invariant 24; CMP-001 to CMP-007 and CMP-012; UIX-NEUTRAL-001 to 004; the envelope parameters (5.9); version binding (8.9); the Phase 1 solver profile (13.1); and delegation disclosure (17.5). Tests that need features outside Phase 1 (federation, standards tooling, operator certification) are not in this set. Phase 1 tests not yet covered, and scheduled in WBS 1.2.4 (CL-066): INV-AT-01, 06, 09, 14, 15, 16, 18, 19, 21, 23, and 24; delegation lapse; the CMP-003 reply rule; CMP-013 to CMP-016; CONT-AT-01 to CONT-AT-09; and MVP-112 to MVP-114.

## M.6 Questions the Contract Raised

Building the mock forced decisions the specification did not yet make. All four were decided on 9 November 2026: CL-044 by the continuity offices (17.9), CL-045 in 8.0, CL-046 in 8.9, and CL-047 by the assurance-sensitive test (23.1.1).

| Log entry | Question                                                                                                                    | What the mock does                                                                                                                    |
|-----------|-----------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| CL-044    | Where does the authority to adopt a Civic Body's first Governance Process come from?                                        | Grants founding members a fixed set of authorities by founding charter                                                                |
| CL-045    | Does a Legal Effect Declaration adopted later make an earlier decision binding?                                             | No: legal status is fixed when a decision closes; declarations apply prospectively                                                    |
| CL-046    | Does one approved change decision authorize more than one change, and must a change request pass the checks adoption would? | Allows reuse (to be closed: bind each approval to the exact change); re-runs adoption checks, so a fee cannot enter by change request |
| CL-047    | What is the default minimum attestation confidence per decision class (invariant 13)?                                       | A decision-class field, default 0.75                                                                                                  |

**Known gap (CL-066).** The v0.1 mock does not authenticate callers: actor, client, and human confirmation are taken from the request. Caller authentication (ASR-01, WBS 1.3.2) will supply them.

# Appendix N — Pilot WBS Crosswalk

Every work package in the ACECOG Pilot WBS (rev 2) mapped to the sections it delivers or depends on. The workbook is authoritative for durations, costs, logic, and owners (13.7). Critical marks the work packages on the critical path in the workbook's calendar-free schedule.

| WBS     | Work package                                                | Specification                 | Critical |
|---------|-------------------------------------------------------------|-------------------------------|----------|
| **1.0** | **Program Foundation, Developer Contracts & Hardening**     | 13.6, 15, 43.2                |          |
| 1.1.1   | API contract and schemas                                    | 15, 11.6.2, 7, 8              |          |
| 1.1.2   | Spec-conformance gap assessment                             | 13.6                          |          |
| 1.2.1   | Status model, version binding, envelope parameters          | 8.0, 8.9, 5.9, 13.1           |          |
| 1.2.2   | Assurance Controls ASR-02 to ASR-11                         | 43.2                          |          |
| 1.2.3   | Compliance objects and Facilitator/Clerk journey            | 43.7.1, 30.9, 17.2            |          |
| 1.2.4   | Phase 1 acceptance suite in CI                              | 26.2, 14, 43.7.3, 11.6.8      |          |
| 1.3.1   | Threat model (API + data layers)                            | 23.4, 15                      |          |
| 1.3.2   | Caller authentication and authorization (ASR-01)            | 23.1, 43.2 ASR-01             |          |
| 1.3.3   | Adversarial / boundary-condition test suite                 | 26.2, 23.4                    |          |
| 1.4.1   | Formal tracked risk register                                | —                             |          |
| 1.4.2   | Change control for spec and code                            | Change log; 14.1 from 1.0     |          |
| 1.5.1   | Contract independent security/gov-tech audit                | 43.6, 43.3                    |          |
| 1.5.2   | Remediate audit findings                                    | 43.6                          |          |
| **2.0** | **Pilot Region Definition & Jurisdiction Selection**        | 13.1, 26.1, 43.4              |          |
| 2.1.1   | Candidate jurisdiction long-list & screening criteria       | 26.1, 43.4, 39                | Yes      |
| 2.1.2   | Exploratory stakeholder outreach                            | —                             | Yes      |
| 2.2.1   | Down-select primary + backup candidate                      | —                             | Yes      |
| 2.2.2   | Identify named executive sponsor                            | —                             | Yes      |
| **3.0** | **Legal, Regulatory & Governance Validation**               | 43.4, 43.8                    |          |
| 3.1.1   | Open-meetings / public-records law review                   | 43.4, 43.8                    | Yes      |
| 3.1.2   | Election-law adjacency and legal status                     | 43.8, 43.2 ASR-08             |          |
| 3.1.3   | Data privacy & accessibility review                         | 43.8, 43.2 ASR-06/07          |          |
| 3.1.4   | Records retention mapping                                   | 43.2 ASR-05, 43.8             | Yes      |
| 3.2.1   | Map Authority, envelope, and process to the charter         | 5.9, 7, 17.5, 8.0             |          |
| 3.2.2   | Liability & informed-consent framework                      | 12.1, 43.2 ASR-08             |          |
| 3.3.1   | Draft pilot-state Compliance Pack                           | 43.4, 43.4.1                  | Yes      |
| 3.3.2   | Encode and confirm pack rules                               | 43.4, 43.7.3                  | Yes      |
| **4.0** | **Pilot Program Design & Governance Agreement**             | 17.5, 43.2, 43.6              |          |
| 4.1.1   | Select discretionary fund / grant program for pilot         | 26.1, 5.13, 39                |          |
| 4.1.2   | Define success criteria & evaluation metrics                | 13.1                          |          |
| 4.1.3   | Configure Governance Process and decision classes           | 17.5, 4.2, 5.9                |          |
| 4.2.1   | Draft and execute MOU                                       | 43.2 ASR-08, 43.6, 23.3       |          |
| 4.2.2   | Establish joint steering committee / RACI                   | —                             |          |
| **5.0** | **Technical Configuration & Integration**                   | 11.5, 13.6, 26.1              |          |
| 5.1.1   | Provision civic-body-controlled installation                | 11.5, 43.2 ASR-03/10          |          |
| 5.1.2   | Configure Civic Body, process, authorities, envelopes, pack | 7, 17.5, 43.4                 | Yes      |
| 5.1.3   | Load pilot portfolio data                                   | 26.1, 5.2, 5.13, 13.1         |          |
| 5.2.1   | Resident onboarding and Membership Credentials              | 17.5, 7, invariants 13 and 24 |          |
| 5.2.2   | Financial system integration (if disbursing funds)          | 12.1, 19.6                    |          |
| 5.3.1   | Minimum viable front end                                    | 11.6.3, 11.6.4, 13.6, 30.9    | Yes      |
| 5.3.2   | Accessibility conformance (WCAG 2.2 AA)                     | 43.2 ASR-06                   | Yes      |
| 5.4.1   | Backup, restore, and exit drill                             | 11.5, 23.3, CMP-007           |          |
| 5.4.2   | Support & incident-response plan                            | 43.2 ASR-09                   |          |
| **6.0** | **Verification & Validation (Staged)**                      | 8.0, 9, 14                    |          |
| 6.1.1   | Run pilot decision in parallel (shadow, non-binding)        | 8.0, 26.1                     | Yes      |
| 6.1.2   | Independent review of shadow-run provenance                 | 9, 14, 12.0.1                 | Yes      |
| 6.2.1   | Execute first real, binding decision cycle                  | 8.0, 43.2 ASR-08              | Yes      |
| 6.2.2   | Post-cycle audit & strict replay check                      | 9.1                           | Yes      |
| **7.0** | **Pilot Launch, Stabilization & Go/No-Go for Scale**        | 13.1, 11.6.6                  |          |
| 7.1.1   | Community outreach & onboarding campaign                    | 11.6.5, 17.5                  | Yes      |
| 7.1.2   | Verify feed/notification neutrality in production           | 11.6.6, UIX-NEUTRAL-003       |          |
| 7.2.1   | Post-launch stabilization                                   | 21.4                          | Yes      |
| 7.3.1   | Evaluation report against success criteria                  | 13.1                          | Yes      |
| 7.3.2   | Joint go/no-go decision & lessons-learned                   | —                             | Yes      |
