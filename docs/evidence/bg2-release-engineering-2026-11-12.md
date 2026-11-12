# BG-2 release engineering handback — 2026-11-12

**Disposition: PUBLICATION HOLD.** This is release-control evidence and a gated execution plan, not a publication approval, live host test, or independent QA finding. Does not change BG-1 public content or its first-publication workflow.

## Exact observation and scope

- Public CivicOS default branch `main` at `4a28737b515bd6d652a05a971822c92aa0ec2057` contains BG-1's manual-only Pages workflow; the BG-2 preflight is **not** present there.
- BG-2 source reviewed for this handback: development PR #10 head `12c9b7121ede736e0c7e5584ff231e3ac5886fc6`; draft PR, stacked branch, not merged or published.
- The development-branch `.github/workflows/bg2-release-gated.yml` is nonpublishing, manual dispatch only, with source/run/artifact/SBOM attestation checks and an environment named `bg2-publication`. It cannot be considered functional on default until an approved main-branch placement and a real protected-environment dispatch prove it.
- Public API branch metadata shows `protected: true`, with required status-check enforcement `off` and no check contexts. The visible repository ruleset listing is empty. Detailed branch-protection inspection returned HTTP 403 (integration lacks permission); therefore reviewer enforcement, required reviews, and environment protection **are not independently proven**.
- Offline `scripts/bg2_stage.py` performs versioned local staging/selection/rollback rehearsal. It explicitly does **not** validate any actual static host, DNS, CDN/cache behavior, GoDaddy wrapper, or live rollback.
- Current CI / Site build / CodeQL / browser feasibility at development exact SHA were successful, but do not constitute public-host, reviewer-enforcement, license, accessibility or release GO.
- This release-engineering delta adds fail-closed explicit `workflow_dispatch` + protected `main` + expected-repository guards and negative-context unit tests. A skipped job would not have been sufficient evidence of rejection.

## Required evidence before claiming R3 preflight PASS

1. **Authoritative host and reviewers:** Owner names the eligible repository and approves **nonpublishing** placement of the reviewed workflow on its protected default branch. A GitHub administrator separately proves `bg2-publication` independent required reviewers and prevention of self-approval (where supported), applicable branch rules, and enforcement. Attach admin-side rule settings and a human reviewer identity distinct from submitter. Do not infer them from green checks or variables.
2. **Run the *real* nonpublishing workflow:** From the eligible default branch, attempt one nonapproved/mismatched-SHA dispatch and record **failure**; then, only if all independent signatures/artifact conditions legitimately exist, run a positive source-specific preflight with reviewer approval and retain run ID, requested SHA, reviewed ZIP SHA-256 and receipt. All source/artifact/SBOM/QA attestation variables are per *exact* SHA; never populate placeholders to manufacture a green run. If legitimate release attestations do not yet exist, positive dispatch is BLOCKED, not a failed project task.
3. **Isolate the actual BG-2 static host:** Owner selects an independent staging/publishing host. Keep BG-1's root and 279-event evidence untouched. Publish only after separate Owner GO. Stage immutable `/versions/bg2-vX.Y/` under an approved, isolated origin/path; independently verify served JS/HTML/WASM ZIP content against reviewed SHA-256 manifest and content/Cache-Control/CSP headers. Measure browser network requests for any third-party traffic or uploaded scenario data and review applicable ordinary HTTP request logs.
4. **Real rollback drill:** On approved isolated host, prove a previous independently verified version exists; record before/after `current` selector, live URL, version identity, HTTP status, hashes and cache behavior; rollback through an approved change; confirm old version is served at the public URL and BG-1 remains byte-identical. The local `bg2_stage.py` rehearsal cannot substitute for this live drill.
5. **Independent exact-candidate review:** Qualified Security/Licensing, native-device Accessibility QA, Independent QA, PMO WBS8 reconciliation, and final Owner source+artifact publication authorization remain distinct. No automatic green check promotes itself to GO.

## Execution boundary

The release-engineering branch/PR is a **draft against the BG-2 development branch only**, not `main`. No workflow is activated on default, no `bg2-publication` reviewer settings are changed, no environment is authorized, and no Pages, GoDaddy, Render, DNS or production assets are changed. A host-admin/readable release credential and an Owner choice of isolated hosting are material dependencies for the real R3/R4 tests.

Links: [BG-2 candidate PR #10](https://github.com/acecog1/ACECOG-CivicOS/pull/10); [CivicOS BG-2 gate issue #9](https://github.com/acecog1/ACECOG-CivicOS/issues/9); internal Mission Control issue #27 (private).
