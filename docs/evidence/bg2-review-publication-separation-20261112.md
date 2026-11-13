# R3 review integrity and publication separation

Builder correction; not independent QA or release approval. PUBLICATION HOLD.

The integrity-only `bg2-review-integrity.yml` workflow accepts observed review
ZIP/SBOM hashes, validates the source/run and provisional evidence, and issues
only a review-integrity receipt. It never reads release GO variables, uses the
publication environment or deploys. Its default-branch dispatch guard remains;
placement/activation on main has not been approved or performed.

The existing protected publication workflow retains all external exact-source
attestation checks and now invokes `scripts.bg2_publication_gate` before any
positive eligibility receipt. Current `releasable:false` / license HOLD packets
are refused even if all external GO strings match. Flipping embedded flags is
also refused. There is deliberately **no positive publication path yet**:
an approved artifact format and complete accepted redistribution packet have
not been implemented/independently reviewed. This must remain a release blocker,
not be hidden behind a successful review-only run. The new tests cover this
refusal and absence of release-variable reads from review workflow.

CodeQL discrepancy diagnosed against integration source f3f391ba29c09ef1e34d57f5f0f34305058e3d00:
check 131424105092 is a separate GitHub Advanced Security check, failure,
`9 new alerts including 1 error`; the analysis Actions job succeeded. Its error
annotation is vendor_browser_pyodide.py:81, potentially uninitialized `data`.
Builder explicitly initializes and guards the download result and adds a
three-transport-failures/no-partial-write regression. Eight advisory notes remain
for separate triage; no dismissal or suppression, and no claim CodeQL is clear
until the new source receives a successful detailed check.

The new R1 lock/native evidence is integrated into this feature candidate for
review only. Source PR #10 and public main are untouched. Independent licensing,
root rehash, final artifact QA, protected default-branch/reviewer evidence,
native accessibility and actual host/rollback are still required. Owner final
independent acceptance and separate publication authorization are preserved.
