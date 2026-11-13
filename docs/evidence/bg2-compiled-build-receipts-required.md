# BG2 actual build receipts still required

This is a review request specification, not an upstream message, legal approval,
or authority to spend, build a substitute runtime, merge or publish.

Baseline technical handback: Security/Licensing PR #13 comment 6844718499,
reviewed runtime candidate 09aa4a3ff61f642a5a671dcdc128690c8218a48c.
The collected original texts and component matrix are now versioned under
`docs/evidence/bg2-compiled-notices/`. They include review-only/excluded/host-tool
context and do not constitute a determination that every component is shipped.
The macOS installer screenshot was excluded from the notice-text collection.
No original text has been rewritten or replaced with an SPDX summary.

## Evidence custodians and specific requests

PMO/Security coordinate a named custodian for actual upstream release receipts.
Any external contact or paid review requires its applicable authorization.

| Delivered component | Actual build evidence needed | Why it remains blocking |
|---|---|---|
| SciPy 1.18.0 WASM wheel | Release build URL/job, source/recipe commits and patches; compile_commands.json or equivalent include order; installed pybind11 version/license; link map/archive member list | Resolve vendored Boost.Math 1.91.0 versus recipe Boost 1.84.0, selected headers/numerical routines and excluded SuperLU source; minimum requirements do not identify actual installed build inputs |
| OpenBLAS 0.3.31 / LAPACK 3.12.0 / libf2c from CLAPACK 3.2.1 | Exact source archives and seven libf2c patches/extras; RISCV64_GENERIC selected kernels, object/link inputs, NO_LAPACKE setting | Full libf2c AT&T/Lucent/Bellcore Notice must be preserved; do not treat all CLAPACK numerical sources or excluded LAPACKE/tests as shipped |
| Pyodide 314.0.7 core / hiwire | Actual core/Emscripten 5.0.3 build receipt, source archives/commits/patches and selected SDK/system library inputs | Corresponding source and modifications for both MPL-covered projects; core third parties have their own terms |
| rpds-py 0.30.0 wheel | Actual rustc -Vv, target/features/Cargo dependency tree and linker inputs; Rust commit 8bab26f4f68e0e26f0bb7960be334d5b520ea452 release COPYRIGHT-library.html | Binary std marker is Rust 1.97.1, unlike global recipe 1.93.0; application Cargo.lock alone does not close standard-library or host/generated-output attribution |
| NumPy 2.4.6 wheel | Source/build receipt and archive member selection for libnpymath/libnpyrandom and portable/header contributions | Complete original wheel notice tree retained; architecture-specific source presence alone does not establish WASM inclusion |

Do not rerun closed root/wheel/old-ZIP hash work. A different local rebuild is
not proof of the shipped upstream binary. Missing receipts remain explicit in
the manifest and every native-member record remains UNKNOWN_BLOCKING.

## Qualified human review decisions

PMO must identify the human reviewer and exact scope. Request written decisions
on actual component applicability, corresponding-source sufficiency and patches,
MPL/AGPL combined distribution, Qhull modification/original-source notices,
public-domain treatment, dual-license elections and LLVM/Boost exceptions.
Both alternatives are retained as original texts where collected; Builder has
not silently selected a license option. Commercial rights remain separately HOLD.

After notice applicability and the remaining source/build evidence are resolved,
Builder incorporates the disposition into a new review candidate; Working QA
rechecks its exact source/ZIP/SBOM/notices. Current publication refusal stays in
place. Staging, protected reviews, actual accessibility/host/rollback and separate
Owner acceptance/publication decisions remain later requirements.
