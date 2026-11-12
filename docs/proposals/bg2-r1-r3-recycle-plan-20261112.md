# BG-2 R1/R3 recycle — source-only change-control proposal (2026-11-12)

Status: PROPOSED, not implemented, tested, approved or releasable. Base integrated candidate: `f3f391ba29c09ef1e34d57f5f0f34305058e3d00` (CivicOS draft #13); source #10 `fbea5e8d639dad3e187138dd22f86d8a3bf4b7e6`. No main merge or publication.

## R1: actual redistribution inventory

1. Correct CPython runtime provenance from the v3.14.0 reference to the actual Pyodide 314.0.7 CPython 3.14.2 release; obtain exact upstream tag/commit/blob and assert the pinned LICENSE bytes before renaming or rewriting any manifest. Security found the two license texts byte-identical; do not infer a different runtime from license identity.
2. For each of ten vendored wheels and Pyodide core, record immutable archive filename/SHA-256, package/version, internal native .so/.wasm inventory, `dist-info` license declarations, detected linked/vendored libraries, exact tagged source/license URL, applicable license texts, delivery path, and reviewer disposition. Distinguish *observed binary evidence* from *upstream build-recipe dependencies*. For SciPy, examine `vendor-sharedlib: true`, libopenblas and libboost without presuming either license obligation until actual included binary contents are established.
3. Fail closed on unknown native attribution and the SciPy SBOM UNDETERMINED expression; retain the unapproved notice banner until Security/Licensing approves a complete packet. Add visible accessible “Licenses & source code” entry in browser lab, pointing to bundled full texts, source provenance and exact CivicOS AGPL source identity. Validate all links offline in the packaged ZIP.
4. Regenerate artifact, manifest, inventory and SBOM from exact source; independently hash downloaded inner ZIP and compare all files. Request Security/Licensing disposition and independent QA on *new exact SHA and digest*, never inherit old signoff.

## R3: separate review from release eligibility

- **Review receipt**: explicitly nonpublishing and nonreleasable; may validate a provisional artifact with `releasable:false`, `independent_QA_signoff:REQUIRED` and provisional notices. Must not require or claim release GO signatures.
- **Approved candidate receipt**: distinct fail-closed positive path, only after independently signed R1/R2/R3/R4 evidence and Owner final beta acceptance + separate publication authorization; exact immutable artifact and SBOM SHA-256, approved notices and reviewer identities bound together. Require `releasable:true`, complete approved notices, no PENDING/REQUIRED reviewer status, no provisional markers, approved source SHA and protected environment controls. Do not set GO variables as a substitute for evidence.
- Negative cases: reject unsigned/expired/mismatched SHA; review-only artifact presented as release; approved flag with provisional notices; missing wheel attribution; wrong host URL; changed ZIP/SBOM digest; wrong repository/ref; missing protected reviewer; unexpected publish step. Positive fixture must be synthetic, not a fabricated actual approval.

## Verification and gates

Source-only unit tests and existing four CI workflows must be rerun at a new exact integrated head. Release Engineer independently verifies protected manual workflow semantics, actual host asset origin and rollback. Working QA reconciles failed CodeQL check versus successful analyze job, then rehashes artifact. Security/Licensing independently qualifies compiled notices. Accessibility QA verifies native hardware/AT and GoDaddy wrapper. Owner alone performs final beta acceptance and separate publication GO. WBS8 and FS v0.24 remain unchanged; CL-084 remains proposed. Commercial workstream and private strategy material excluded.

References: [Security R1 review](https://github.com/acecog1/ACECOG-CivicOS/pull/10#issuecomment-6835062449); [working QA R3 defect](https://github.com/acecog1/ACECOG-CivicOS/pull/13#issuecomment-6835694385); [Mission Control](https://github.com/acecog1/ACECOG-Internal/issues/27).
