# BG-2 Pages delivery implementation

This is a proposal requiring independent review. No publication, mandatory
licensing closure, legal approval or completed live rollback is asserted.

## Artifacts and source

The browser/WASM workflow also assembles and retains the full-site candidate
after its qualification checks, allowing independent review before merging the
new delivery workflows. The separate candidate workflow runs manually at the exact candidate Git revision, consumes
its successful browser/WASM runtime ZIP and calls the existing exact-Git verifier.
It downloads retained BG-1 evidence from successful deployment run 42997122922,
source `4a28737b515bd6d652a05a971822c92aa0ec2057`, then captures each anonymously
served BG-1 asset only when its SHA-256 matches that deployment's inventory.
Any drift stops assembly. This is a capture of deployed bytes, not a rebuild.

The `bg2-pages-candidate` artifact retains `site.zip`, `previous-site.zip`, their
SHA-256 values and an assembly receipt. BG-1 files stay at the same paths, with
identical bytes. BG-2 is added under `beta/`. Its only application transformation
appends a visible release notice/source link; the original runtime review receipt
is retained as evidence of the original runtime, not relabeled as approval of the
transformation. The final full-site manifest hashes every delivered file.

Original notice supplement and recovery ZIPs remain unchanged. They are expanded
under `beta/legal/original/` and `beta/legal/recovered/`, respectively, including
Rust 1.97.1 COPYRIGHT-library.html, CPython/SDK originals, pinned source archive
references and recovered recipe patches. The new index and finite claims file
keep unresolved sufficiency/applicability marked PENDING/U. These are actual
release blockers until Security/Licensing returns a finite evidenced disposition.
The independently curated replacement documents belong in the committed
`docs/evidence/bg2-recipient-packet/` directory. Assembly verifies every such file
against its exact Git blob and overlays the recipient documents, preserving the
unchanged original and recovered evidence trees. Final notices and claims require
actual evidence-based editing and independent review, not flipping approval flags.

## Independent decision and publication

Independent QA and Security/Licensing review the exact full-site archive, notice
texts, claim disposition, source/modification delivery and browser behavior.
They supply an attributable decision document using schema
`ACECOG-BG2-INDEPENDENT-DECISION-v1`, with exact `source_sha`, `archive_sha256`,
`manifest_sha256`, `claims_sha256`, `mandatory_groups`, `independent_qa` and
`security_licensing` records. Every mandatory group must be CLOSED. Reviewer
records require ACCEPT, reviewer identity and an HTTPS evidence URL. Claim items
must individually be M/SATISFIED, R/ACCEPTED_RESIDUAL or C/CONTEXT with packaged
evidence paths; U and PENDING are rejected. A schema is not reviewer authentication:
the decision's hash must be independently entered in protected configuration.
The Builder must not populate real ACCEPT records on reviewers' behalf.

Use the retention-only `bg2-retain-independent-decision.yml` workflow to retain
the exact reviewer-furnished JSON as `decision.json` in the Actions artifact
`bg2-independent-decision`. Record its run ID and digest. Upload alone confers no
approval; the protected digest and independent environment review remain required.
Protected release configuration
must contain BG2_SOURCE_SHA, BG2_CANDIDATE_RUN_ID, BG2_CANDIDATE_SHA256,
BG2_DECISION_RUN_ID, BG2_DECISION_SHA256 and BG2_PREVIOUS_SITE_SHA256. Reviewer
appointment, document retention and actual environment-protection access must be
verified operationally; this implementation does not claim those settings exist.

After independent human code review and merge, dispatch the delivery workflow
from main, choosing publish. Environment `bg2-publication` must have independent
required reviewers and prevent self-review. The workflow attempts to read and
enforce these settings; unavailable permission fails closed. It downloads exact
retained artifacts, verifies bytes and decisions, compares the entire BG-1 baseline,
uploads the verified Pages tree and invokes deploy-pages. It then hashes every
anonymously served file and retains a delivery receipt. A deployment can succeed
while the served-byte check fails: report the actual deployment and failed check,
and use the retained restore operation; do not label that run an accepted release.

## URL and GoDaddy entry

Expected application URL, **not yet verified published**:
`https://acecog1.github.io/ACECOG-CivicOS/beta/`.

Once that URL passes mandatory prepublication review and actual publication
verification, add a direct link on the existing GoDaddy `https://acecog.org/beta`
entry, retaining its original content before editing. Suggested link text:
“Open the browser-only CivicOS laboratory”. No iframe, paid service or AI widget
is required. Verify the public link and preserve the before/after entry text.
The application discloses ordinary static-host request processing; test actual
CSP, network requests and caching rather than assuming GoDaddy controls the app.

## Restore and acceptance

Dispatch the same protected delivery workflow from main with operation restore.
It verifies and republishes the retained prior-site bytes; it never rebuilds the
previous version. Confirm served hashes against the retained inventory, then
restore the GoDaddy entry's saved original text/link. Actual restore practice
follows initial publication. To return to the candidate after the drill, dispatch
publish with the unchanged reviewed pins. Preserve each actual run/deployment URL.

Use the ten-step script in `bg2-beta-publication-acceptance-sequence-20261116.md`
on the actual published URL. Physical device/AT, hands-on acceptance, live rollback,
schedule reconciliation and formal qualified legal review are final-QA work.
No PASS is inferred for an unexecuted activity.

## Verification recorded so far

Local positive/negative verifier contract tests use clearly synthetic review
records. They do not approve a real candidate. Linux shell gate tests and full
exact-head CI/browser/security results must be recorded against the final PR head.
The initial runtime source PR #21 had all four workflows successful at inspection;
those results do not automatically qualify this changed branch.
