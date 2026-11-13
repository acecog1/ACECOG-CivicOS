# Riverbend counterfactual lab — local proof of concept

**Not deployed. Not a public API. Not part of the existing BG-1 release.**

This research prototype executes the **actual CivicOS Engine**, creates separate in-memory, synthetic governance histories, and compares a reference against modified input assumptions. It reuses the ten-initiative Riverbend portfolio fixture (tests/scenario.py) but creates a **new, shorter** governed transaction history; it does NOT fork the exact canonical 279-event reference chain.

## Try locally

Requires installed pinned Python CI dependencies (including NumPy, SciPy and JSON Schema).

    python scripts/experiment_riverbend.py --flip cara --flip dev
    python scripts/experiment_riverbend.py --budget 600000 --water 12 --crew 20
    python scripts/experiment_riverbend.py --surprise --seed 42
    python -m pytest -q tests/test_riverbend_counterfactual.py

The JSON output includes reference and alternative inputs, source-bound vote tallies, actual decision status, optional real optimization result and its hash, replay status, event count and hash-chain head, plus structured impact narrative statements.

## What changes causally

- **Reference:** Ana, Ben, Cara and Dev vote yes; Fay votes no; Eli is recused and the actual CivicOS vote command refuses the attempted vote. A governed decision approves Plan A, adopts its model, runs a strict-lane optimization, creates a synthetic baseline and reserves its synthetic allocation. Replay re-solves against the bound model.
- **Two flips:** Cara and Dev change to no on a separate branch. The real decision now rejects Plan A; there is no adopted model, no optimization result, no baseline and no funding commitment. The original branch is untouched.
- **Lower resources:** Keep the reference votes but alter budget, water and crew limits. The approved model goes through the actual solver, with a new allocation and result hash; replay must agree with the original alternative-run calculation.
- **Surprise mode:** A seed reproducibly samples actual model inputs and fictional votes, NOT hidden randomness inside the deterministic SciPy LP/QP solver. No randomization on web refresh is implemented.
- **Impact narrative:** No language-model-generated claims; each statement uses actual decision/solver receipts and differences in input variables. Unknown real ecological, economic, resident, legal and municipal effects are explicitly withheld.

## Acceptance and non-authorizations

This candidate is **not** a running public web sandbox. The legacy single global-engine local HTTP server is not suitable as a public multi-tenant environment. We are not importing real municipal records, changing the GoDaddy W+M Beta page, adding write endpoints, changing GitHub Pages workflows, or changing the issued WBS8 budget. All hypothetical funding reservations remain internal to each in-memory branch.

The actual subsequent live release requires a separately reviewed secure session API with per-user isolation, quotas, abuse controls, expiry and private-by-default records. True canonical Riverbend snapshot branch/fork with a versioned pre-decision checkpoint is additional work. A visitor UI must display role/recusal eligibility, allow opt-in randomization, explain measured effects and show a side-by-side comparison and replay evidence. Optional AI narration must ground itself in the validated engine receipt and must not modify engine state, assert missing effects, or impersonate a civic official.

**Builder:** reproduce CLI and tests, repair defects, propose exact snapshot-fork design and cost the incremental UI/backend/AI work.

**Independent QA:** verify real vote refusal and delegated eligibility, no ghost funding on rejected branch, input bounds, hash determinism, replay, no source-only narrative inventions, and no public API exposure. Evaluate concurrency/security and real-identity issues separately for the future live feature.

**Plan steward:** reconcile this future increment with the approved WBS8 P-2/Q-25 backlog before proposing a baseline change. The original 279-event static BG-1 site remains unchanged.

The feature is a local evidence-based feasibility demonstration, not an authorization to publish or a claim of full civic governance readiness.
