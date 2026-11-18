# BG-2 Owner-operated Pages publication — review handoff (2026-11-18)

**Status:** Proposed on a review branch. No independent approval, configuration change, publication, or rollback execution is claimed here.

## Owner directive and scope
Allow the repository Owner GitHub account `acecog1` to manually publish or restore the limited browser-only beta without a second GitHub environment reviewer. Keep both independent technical **QA** and **Security/Licensing** acceptance **as data and SHA-pinned evidence**, never as a synthetic approval or a new environment reviewer requirement.

## Exact code changes
- `.github/workflows/bg2-pages-delivery.yml`: replace the GitHub environment protection-rules assertion (`required_reviewers` + `prevent_self_review`) with an Owner-only manual default-branch dispatch and preserved immutable plan check. Environment `bg2-publication` remains the scoped variable/deployment environment, but no longer needs a second human reviewer **in workflow code**.
- `scripts/bg2_owner_publication_record.py`: verify both initiator and rerun initiator are `acecog1`; reject other repository/event/ref/operation or malformed source/ZIP/decision/rollback pins and run IDs. Write Owner, exact run/attempt, operation, candidate/decision/rollback digests to `owner-publication-record.json` before downloading the retained bytes. After actual served-byte verification, add exact served URL, receipt digest and served file count; retain record via Actions artifacts even when downstream deployment fails. This is an operational audit, not a legal opinion or an independently fabricated decision.
- `tests/test_bg2_owner_publication_record.py`: positive publish/restore, negative user/rerun/ref/event/pin paths, verified-receipt binding, and structural fail-closed workflow assertions.

## Unchanged mandatory controls
1. `BG2_SOURCE_SHA`, `BG2_CANDIDATE_RUN_ID`, `BG2_CANDIDATE_SHA256`, `BG2_DECISION_RUN_ID`, `BG2_DECISION_SHA256`, `BG2_PREVIOUS_SITE_SHA256` must be correctly populated from actual retained independent evidence; empty/mismatched values still fail closed.
2. The candidate Actions run must be from `main`, successful, match the pinned candidate SHA, and belong to `acecog1/ACECOG-CivicOS`.
3. Exact retained candidate `site.zip`, independent `decision.json`, and prior BG-1 `previous-site.zip` bytes must each hash to the independently protected pins.
4. `scripts.bg2_publication_gate` continues to require the source/archive/manifest/claims-bound decision, four CLOSED mandatory groups, **attributable independent QA and Security/Licensing ACCEPT**, resolved M/R/C claim dispositions, full manifest, and BG-1 preservation.
5. `restore` republishes the retained original BG-1 archive, not a reconstructed version. Served Pages bytes are independently checked and recorded. Existing GitHub Pages and reversible GoDaddy direct-link procedure remain unchanged.

## Release Engineering — after PR review/merge
1. Independently inspect workflow/test diff and verify branch CI. Do **not** repeat unchanged 637/637 package-content QA or upstream license audits.
2. In **ACECOG-CivicOS → Settings → Environments → `bg2-publication`**, remove required deployment reviewers and disable *Prevent self-review*. This GitHub administrative configuration is distinct from the workflow code change; leaving GitHub environment reviewer rules enabled still blocks solo Owner deployment. Retain the named environment, configured variables and ordinary access/branch restrictions. If unavailable, record the actual GitHub permission/settings obstacle.
3. Confirm all six existing variable values are visible in the correct repository/environment scope and match the prior verified current candidate/independent decision. Do not manufacture approvals or silently repin hashes. Existing exact-main candidate `c0152c0ada8a49f8f82c4d357227ff6f2bfd0012`, site.zip `44bf317c78bd45f720be9f646493241db9456b42405064cca78c573b91fd926b`, independent retained decision SHA256 `f86ad872ae172de6c2d14a067ab64c02e30795a0f8adb108992ed8da21ae1bab`, previous BG-1 archive SHA256 `eccbf4df5d83d1a9baf8c96b5c22725635a6e11f273dfed0ca27b3bada14279c` are the latest verified pins in Mission Control #27. Confirm actual run IDs there before dispatch.
4. Owner account `acecog1` selects Actions → **BG-2 Pages publish or restore** → `publish` on `main`. A newly merged workflow commit is expected while the approved candidate source SHA remains the original pinned exact-main candidate. Record actual run, Owner identity, artifact, decision and served URL from the uploaded `bg2-delivery-receipt-<run_id>-attempt-<run_attempt>`.
5. Confirm actual `https://acecog1.github.io/ACECOG-CivicOS/beta/` HTTP behavior, legal/source/patch links and reversible `https://acecog.org/beta` GoDaddy entry; **do not claim live** before verified. If issues occur, Owner selects `restore` with the same evidence pins; confirm actual restored BG-1 served hashes and restore GoDaddy prior entry. Record the rollback run as its own audit event.
6. Report results to [Mission Control #27](https://github.com/acecog1/ACECOG-Internal/issues/27). Hands-on/native-device acceptance, actual live rollback drill, schedule reconciliation and formal qualified legal review retain their separately established sequence.

**Safety boundary:** This removes only the requirement for a *second GitHub environment reviewer*. It does not remove prior independent QA/Security decisions, the exact decision/ZIP hashes, gate logic or the Owner's auditable responsibility.
