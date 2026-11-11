# ACECOG API: contract test results

Scenario: Riverbend Commons (26.1). 55 of 55 checks passed.

| Test | Check | Result | Detail |
| --- | --- | --- | --- |
| INV-AT (24) | A Governance Process that charges a fee to take part is refused (TRU-ACCESS-001) | pass |  |
| INV-AT-17 | An approval or monitoring role appointed by itself is refused | pass |  |
| INV-AT-17 | At GML-1 a monitoring role must be selected through the Governance Process | pass |  |
| G-055 | An actor cannot grant authority to themselves, and '*' is not grantable after founding | pass |  |
| 5.9 | Envelope defaults applied: confidence 0.90, reversibility 2 | pass |  |
| 5.9 | Out-of-range envelope parameter disables autonomous resolution | pass |  |
| MVP-100 | Create a Civic Body, Governance Process, members/roles, authority, and a portfolio | pass |  |
| MVP-101 | Two competing proposals preserved with exact versions; amendment adds a version | pass |  |
| CMP-002 | A pack whose rule would relax a higher layer is refused at adoption | pass |  |
| CMP-003 | Under the open-meeting guard, a private member-to-member thread is refused; public posting works | pass |  |
| CMP-004 | A member with a recorded Interest Declaration cannot vote on the proposition | pass |  |
| 17.3 | A delegation can be revoked | pass |  |
| CL-029 | Delegation concentration above the disclosure threshold is disclosed; delegation loops are refused | pass |  |
| MVP-102 | Approve objectives, constraints, budget envelope, and decision method; minority position preserved | pass |  |
| INV-AT-26 | An approved decision with no Legal Effect Declaration is labeled Advisory | pass |  |
| G-054 | A monitoring appointment needs the decision that approved that person for those actions, and uses it once | pass |  |
| CMP-004 | The recusal appears in the decision's provenance | pass |  |
| 13.1 | A Q matrix that is not positive semidefinite is rejected before solving | pass |  |
| 13.1 | A convex QP run is accepted on the exploration lane | pass |  |
| MVP-103 | Feasible portfolio solved; binding constraints shown; a near-optimal alternative reported | pass | objective 601.249945; binding: budget, eco-water-ceiling, crew-capacity |
| 8.0 | A run result is labeled Scenario output and Advisory | pass |  |
| INV-AT-08 | A result that is not commit-eligible (exploration lane) is refused at baseline | pass |  |
| GOV-AUTHPATH-001 | A member without baseline authority cannot create a baseline | pass |  |
| G-054 | A baseline needs the decision that approved the run's model, and a decision baselines once | pass |  |
| MVP-104 | Commit the approved portfolio without double-allocating resources | pass |  |
| 8.0 | A commitment shows Committed, Funded but incomplete, and Advisory as separate axes | pass |  |
| 8.1 | Resending a command with the same command_id returns the original result and creates nothing | pass |  |
| MVP-105 | Post actuals without altering the baseline | pass |  |
| MVP-106 | A within-envelope variance is resolved by delegated rebalance | pass | moved $10,000 i05 -> i01 |
| 5.9 | A rebalance whose inputs carry no calibrated confidence fails closed and escalates | pass |  |
| 5.9 | An envelope with invalid parameters escalates every candidate action | pass |  |
| UIX-NEUTRAL-004 | An out-of-envelope approval is escalated identically on mobile and desktop | pass |  |
| MVP-107 | A hard-constraint breach produces an Exception Proposition naming the conflict and the authority required | pass | rebalance would breach hard constraint(s) eco-water-ceiling |
| G-059 | An exception resolution that would breach a hard constraint is refused, even with an approved decision | pass |  |
| MVP-108 | Approve a changed state; the prior baseline and decision lineage are preserved | pass |  |
| G-059 | A closed exception cannot be resolved again; a relaxation the decision names is recorded as a new constraint version | pass | portfolio_model-0001@v2: limit 20 -> 40 |
| MVP-109 | Replay the original decision from its historical snapshot | pass | 08a83dc01dca8a38 |
| G-054 | Evidence adoption needs the decision that adopted that evidence for that constraint, and uses it once | pass |  |
| INV-AT-04 | Estimated evidence cannot become a binding constraint until a decision adopts it | pass |  |
| INV-AT-13 | A self-attested member takes part where the decision class allows it and is refused where it requires verification; low-confidence result flagged | pass |  |
| CL-046 | A change that differs from the approved one is refused, and an approval puts its change in force only once | pass |  |
| INV-AT (24) | Even an approved change cannot introduce a participation fee that adoption would refuse | pass |  |
| 8.9 | A change in force does not apply to a transaction already in progress (bound process version used) | pass | 3 of 5 = 60% passed under the bound 50% rule |
| CMP-006 | With a Legal Effect Declaration the label shows its status and cited authority; earlier decisions keep theirs | pass |  |
| UIX-NEUTRAL-002 | The assistant cannot submit without an explicit human confirmation of the exact payload | pass |  |
| UIX-NEUTRAL-001 | Desktop, assistant, and mobile submissions produce identical governed propositions | pass |  |
| MVP-111 | The AI interface cannot bypass a failed authority check, even with confirmation | pass |  |
| UIX-NEUTRAL-003 | Every feed item states why it is shown; ranking for engagement is not configurable | pass |  |
| CMP-001 | A configuration change that disables an Assurance Control is refused, citing the layer rule | pass |  |
| CMP-005 | Deletion before the schedule allows is refused; an authorized deletion succeeds and is recorded | pass |  |
| MVP-110 | Export the civic state in a documented machine-readable package sufficient for independent reconstruction | pass |  |
| CMP-012 | A third party verifies the event log's hash chain from the export alone | pass | 276 events verified |
| CMP-007 | The export rehydrates into a fresh instance and replay yields identical outcomes | pass |  |
| ASR-04 | A tampered export is detected | pass |  |
| 8.1 | Refused and escalated commands are recorded in the event log | pass |  |
