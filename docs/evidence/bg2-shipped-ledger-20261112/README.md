# BG2 shipped-components review ledger

**Builder proposal; licensing HOLD; all 123 native members remain UNKNOWN_BLOCKING.** No legal self-certification, release eligibility, merge or publication authority.

This ledger describes the exact existing [PR #16 review artifact](https://github.com/acecog1/ACECOG-CivicOS/actions/runs/43371657753/artifacts/14011669639), not a rebuilt or newly approved runtime. Source: `8cd6031bd1dd7aff9e266c0abeb729d9d015bc59`; tree: `96dca9c35b0484743d6db6a6eadd79a0eed00194`. Inner ZIP: 24,004,439 bytes; SHA-256 `c8fa9aa4bf97ec977966167dde2eb02db3681f96b2486df614f2e74f64c85a52`.

## Review files

- [ledger.json](ledger.json): exact wheel/member hashes and lengths, package owners, component association grades, original notice IDs, source URLs/paths/digests and reverse component links; explicit unresolved decisions.
- [members.csv](members.csv): one row per exact native member, with component IDs and notice paths for convenient review.
- [component-rules.json](component-rules.json): 46 review component/group records and their explicit gaps. Nested source constituents are grouped where the preserved notice is shared; these are not 46 proven linked runtime libraries.
- [verification.json](verification.json): exact artifact identity and executed coverage results.
- [derive.mjs](derive.mjs): deterministic offline derivation from the unchanged inner ZIP and component rules. Run with Node: `node docs/evidence/bg2-shipped-ledger-20261112/derive.mjs /path/to/exact-review.zip`. It refuses other ZIP hashes, checks source/gates, all 207 payload hashes, all embedded native bytes and complete member sets, inherited map bindings and every notice record.

## Evidence and limits

Executed locally against the downloaded GitHub artifact: **207 payload digests, 123/123 native member bindings, 166/166 preserved evidence-record digests**; no extra/missing native entries. Repeated generation is byte-identical; one-byte corrupted ZIP is rejected. There are **208 ZIP entries: 207 payload files plus release-manifest.json**, correcting ambiguous earlier shorthand. The 166 evidence records comprise **164 original files and two review documents**. The CSV contains 15 NumPy, 1 rpds and 107 SciPy native rows, including test extensions actually present and both NumPy static archives. Test filenames do not exclude shipped bytes.

Package ownership/presence is direct archive evidence. Nested component edges are conservative source-graph/module associations from the preserved COMPONENT_REVIEW.md, which reviewed prior source 09aa4a3f; this ledger independently binds its preserved bytes to #16. Such edges are neither selected-object proof nor notice applicability acceptance. All SciPy modules receive the SciPy source owner and scoped numerical source directory; unresolved translated/first-party/header contributions remain open instead of disappearing as an unowned remainder. Broad xsf/Boost and pybind11 associations are candidate review pools, not proof of those headers in every associated extension. Cargo context similarly does not turn host/proc-macro/Windows dependencies into shipped runtime claims.

All ten wheels include a list of their actual embedded license/notice-text paths and digests, including the seven with no native members. Four core/JS/stdlib files are separately bound by hash and associated with a clearly labeled core candidate pool. The 123-member inventory covers wheel native members only; Python subcomponents, generated JS, CPython embedded headers and selected SDK inputs still require complete attribution. The JSON reverse notice index labels unassigned source/build/Python/architecture/excluded context explicitly. A preserved license text proves its presence, not that its source code was compiled. Both license alternatives remain preserved; no license option is elected.

SBOM SHA-256: `ebe4f0ef7af96d8c34f561c9a41ec2d444b720f71b08216df5dd39ff90caf39f`; native inventory: `981bd16b5187e603177126146ee6f649eaf23b968419d903bb67513322686856`; compiled evidence manifest: `4df0a02c11680269ceb46a84d21ad4407c59ee73d5dde001f346102615837753`. Hash checks here are Builder derivation inputs, not independent QA acceptance or repeated upstream root/wheel verification.

## Blocking handoff

| Owner | Evidence or decision still required |
|---|---|
| Builder + Security/Licensing / actual upstream receipt custodians | SciPy actual compile/include/link inputs (Boost.Math 1.91 vs external 1.84, actual pybind11 version, selected numerical and header attribution); SuperLU excluded source confirmation; full Qhull original-source/modification treatment. |
| Same | OpenBLAS/LAPACK/libf2c selected kernels/objects, seven libf2c patches/extras; NumPy selected static/archive and portable/header contributions. Do not infer external SciPy BLAS for NumPy. |
| Same | Actual Pyodide/Emscripten source/patch/SDK selection; hiwire MPL source separately; CPython HACL/libmpdec and embedded mini-lz4 notices. SQLite tea/license.terms is extension context, not the missing actual sqlite3.c public-domain header. |
| Same | rpds actual rustc -Vv, target/features/dependency/link tree and Rust 1.97.1 release COPYRIGHT-library.html. Collected top-level COPYRIGHT/MIT/Apache texts and all Cargo lock texts do not close stdlib attribution. |
| PMO + qualified human reviewer | Named reviewer/capacity and written acceptance of exact applicability/source sufficiency, MPL/AGPL scope, alternatives, public-domain, Qhull notices and exceptions. No reviewer appointment, spend or external upstream contact performed by this task. |
| Independent Working QA | Recheck this ledger derivation and exact #16 artifact, inventory, SBOM and original notices; prior source/CI PASS is not final artifact/legal approval. |
| Release / Accessibility / Owner | Protected independent review/default-branch controls, native device/AT/zoom/low-memory, real host/privacy/cache/rollback evidence, final hands-on beta acceptance and separate publication authorization. |

This is an additive documentation/evidence proposal based on #16, for a focused stacked review. It changes no runtime, original notice bytes, SBOM, packaging input list, flags, workflow, release gate, GO variable, baseline or deployed host. The old review packet remains immutable. Any future accepted determination needs a new separately digest-bound candidate and independent review; no provisional flags are flipped.

## Component/group index

| ID | Component or review pool | Remaining question |
|---|---|---|
| numpy | NumPy 2.4.6 | Actual selected source/header/object receipt and qualified applicability decision pending |
| scipy | SciPy 1.18.0 | Complete numerical/header attribution, actual pybind11 and include/link receipts pending |
| rpds | rpds-py 0.30.0 | Actual selected source/header/object receipt and qualified applicability decision pending |
| openblas | OpenBLAS 0.3.31 / GotoBLAS | Actual selected source/header/object receipt and qualified applicability decision pending |
| lapack | LAPACK 3.12.0 | Actual selected source/header/object receipt and qualified applicability decision pending |
| libf2c | libf2c from CLAPACK 3.2.1 | Seven recipe patches/extras and selected object notices pending; CLAPACK numerical sources not inferred shipped |
| uarray | uarray (SciPy snapshot) | Actual selected source/header/object receipt and qualified applicability decision pending |
| duccfft | duccfft 0.40.0 / pyduccfft | Actual selected source/header/object receipt and qualified applicability decision pending |
| dop | DOP (SciPy snapshot) | Actual selected source/header/object receipt and qualified applicability decision pending |
| fmm | fast_matrix_market (SciPy snapshot) | Actual selected source/header/object receipt and qualified applicability decision pending |
| direct | DIRECT (2.0.4 ancestry) | Actual selected source/header/object receipt and qualified applicability decision pending |
| highs | HiGHS 1.12.0 / filereaderlp / pdqsort | Actual selected source/header/object receipt and qualified applicability decision pending |
| tnc | TNC (SciPy snapshot) | Actual selected source/header/object receipt and qualified applicability decision pending |
| trlib | trlib (SciPy snapshot) | Actual selected source/header/object receipt and qualified applicability decision pending |
| superlu | SuperLU 7.0.1 / COLAMD | Actual selected source/header/object receipt and qualified applicability decision pending |
| arpack | ARPACK / arnaud translation | Actual selected source/header/object receipt and qualified applicability decision pending |
| propack | PROPACK translation | Actual selected source/header/object receipt and qualified applicability decision pending |
| qhull | Qhull 8.0.2 | Human must accept original-source availability and applicable modification notices; selected source patches not established. |
| xsf | xsf 0.2.2 / Cephes / Faddeeva / qd / mdspan | Actual selected source/header/object receipt and qualified applicability decision pending |
| boost | Boost.Math 1.91.0 vs external Boost 1.84.0 | Actual selected source/header/object receipt and qualified applicability decision pending |
| pybind11 | pybind11 (actual installed version UNKNOWN) | Actual selected source/header/object receipt and qualified applicability decision pending |
| unuran | UNU.RAN 1.9.0 | Actual selected source/header/object receipt and qualified applicability decision pending |
| biasedurn | Biasedurn / copied NumPy random code | Actual selected source/header/object receipt and qualified applicability decision pending |
| ndimage | ndimage (SciPy snapshot) | Actual selected source/header/object receipt and qualified applicability decision pending |
| numpy-pocketfft | NumPy pocketfft | Actual selected source/header/object receipt and qualified applicability decision pending |
| numpy-lapack | NumPy lapack_lite | Actual selected source/header/object receipt and qualified applicability decision pending |
| numpy-core | NumPy core portable/header contribution candidates | Actual selected source/header/object receipt and qualified applicability decision pending |
| numpy-random | NumPy random generators/distributions | Actual selected source/header/object receipt and qualified applicability decision pending |
| rust | Rust 1.97.1 binary std marker | Actual rustc -Vv, target/features and COPYRIGHT-library.html absent; Rust 1.93 global recipe is not this wheel identity |
| crate-rpds-1.2.0 | rpds-1.2.0 | Actual selected source/header/object receipt and qualified applicability decision pending |
| crate-pyo3-0.27.2 | pyo3-0.27.2 | Actual selected source/header/object receipt and qualified applicability decision pending |
| crate-pyo3-ffi-0.27.2 | pyo3-ffi-0.27.2 | Actual selected source/header/object receipt and qualified applicability decision pending |
| crate-triomphe-0.1.15 | triomphe-0.1.15 | Actual selected source/header/object receipt and qualified applicability decision pending |
| cargo-context | Other Cargo.lock crates: target/host applicability unresolved | 26 lock entries are not 26 proven runtime components; proc macros/build helpers/Windows branches must remain context pending actual target/features tree |
| pyodide | Pyodide 314.0.7 | Actual selected source/header/object receipt and qualified applicability decision pending |
| cpython | CPython 3.14.2 | CPython LICENSE/Doc/license.rst/Expat text preserved; HACL, libmpdec and other selected embedded header notices/source mapping incomplete. |
| hiwire | hiwire 6a1e67280a15d929ebeceee54a6358c9c8d5f697 | Actual selected source/header/object receipt and qualified applicability decision pending |
| libffi | libffi 3.4.4 + f08493d249d2067c8b3207ba46693dd858f95db3 | Actual selected source/header/object receipt and qualified applicability decision pending |
| liblzma | liblzma 5.2.2 | Actual selected source/header/object receipt and qualified applicability decision pending |
| sqlite | SQLite 3.39.0 | Collected tea/license.terms is Tcl extension context, NOT the sqlite3.c public-domain header. Actual selected sqlite3.c notice/source receipt is missing. |
| zstd | zstd 1.5.7 | Actual selected source/header/object receipt and qualified applicability decision pending |
| zlib | zlib 1.3.1 | Actual selected source/header/object receipt and qualified applicability decision pending |
| bzip2 | bzip2 1.0.6 | Actual selected source/header/object receipt and qualified applicability decision pending |
| emscripten | Emscripten 5.0.3 selected JS/system runtime | Actual selected SDK/system objects and embedded mini-lz4/liblz4.js notices incomplete; source-only mimalloc/libunwind/LLVM files are not proven selected. |
| lbfgsb | L-BFGS-B C translation (SciPy snapshot) | Actual optimize/__lbfgsb.c inherited header notice not separately preserved; source/header mapping pending |
| lapjvsp | LAPJVsp (SciPy snapshot) | Actual sparse/csgraph/_matching.pyx and selected header notice mapping pending |
