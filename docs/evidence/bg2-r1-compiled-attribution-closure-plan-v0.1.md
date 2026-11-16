# BG-2 R1 compiled-binary attribution and notice closure (Builder proposal)

Status: **OPEN / REVIEW ONLY / NOT A LICENSE APPROVAL**. Source baseline: CivicOS PR #10 `fbea5e8d639dad3e187138dd22f86d8a3bf4b7e6`. Derived from Security/Licensing review on 2026-11-12. No publication authorization.

## Provenance correction (do not rewrite verified source pins)

Pyodide **314.0.7** identifies embedded CPython **3.14.2**, while `docs/evidence/bg2-license-sources/` currently pins the independently matched **CPython v3.14.0** LICENSE source text. The reviewer found the compared license bytes identical. Preserve the v3.14.0 source-file identity as historical provenance until the replacement v3.14.2 tag/blob is independently fetched and verified; record embedded runtime version **3.14.2** separately. Do not mislabel v3.14.0 evidence as v3.14.2 evidence.

## Required exact-artifact inventory (not yet executed)

1. From the pinned Pyodide 314.0.7 lock and the *exact* packaged ZIP, record each Python wheel and native `.so` / `.wasm` / vendored shared library with path, size, SHA-256, package version, wheel RECORD or lock entry, upstream source and applicable license. Enumerate SciPy 1.18.0's actual linked libraries; its Pyodide build recipe declares `vendor-sharedlib: true` and compile dependencies on OpenBLAS and Boost, but those declarations alone do **not** prove inclusion of a particular component in the shipped artifact.
2. Reconcile every compiled component against source license text, binary redistribution requirements, copyright notices, source-offer/source-availability requirements and the actual package contents. Mark unresolved entries **UNKNOWN/BLOCKING**, not absent or cleared. The SciPy `LICENSES_bundled.txt` index is not itself a compiled-component bill of materials.
3. Add the complete applicable notice text and a visible, accessible source/licenses entry point to the browser lab; include actual target paths and test the link against the packaged static artifact. Keep `releasable:false` and independent signoff pending.
4. Regenerate ZIP and SBOM together from the exact source head; publish SHA-256 for outer ZIP, inner artifacts and SBOM, plus repeatable generation command and CI run URLs. Security/Licensing must independently verify exact hashes and applicability; working QA must independently inspect ZIP/SBOM consistency.

## R3 release semantics (separate release-engineering change)

A provisional review packet containing `releasable:false`, `independent_QA_signoff:REQUIRED` and `NOT AN APPROVED NOTICE SET` must **never** pass a publication-eligible positive gate. Either label the current preflight explicitly *review-only*, or introduce a distinct digest-bound, independently approved artifact manifest and fail-closed negative tests. No synthetic signatures, no weakening of approval checks, no deploy step.

## Change control and owners

Builder: implement inventory/notice/source-link and exact-artifact tests on isolated branch; Release Engineer: R3 gate semantics and negative cases; Security/Licensing: independent binary/notice applicability; working QA: exact candidate ZIP/SBOM and CodeQL check-level discrepancy; Accessibility QA: real-device evidence; PMO: log Q-39 residual and proposed FS/CL impacts. **WBS8 and FS v0.24 unchanged; CL-084 remains proposed.** Owner final beta acceptance and publication GO remain separate.
