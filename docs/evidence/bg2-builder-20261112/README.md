# BG-2 Builder evidence — 12 November 2026

Builder implementation evidence only. **PUBLICATION HOLD.** No independent
root certification, qualified license approval, final Owner acceptance or
publication authorization is asserted by these files.

## Executed observations

`publisher-root-verification.json` records a new official GitHub Release API
lookup and archive download on 2026-11-13 02:44 UTC (12 November in Denver).
The archive SHA-256 and all four extracted roots matched the fixed candidate
pinset. Windows certificate trust was loaded using pip's vendored `truststore`;
TLS validation was retained. This was executed by Builder, not a second reviewer.

`locked-native-inventory.json` records the actual ten-wheel closure selected
from the SHA-256-pinned Pyodide lock. NumPy has 15 native members, rpds-py has
one, and SciPy 1.18.0 has 107, including `scipy.libs/libopenblas.so`.
Each member has a wheel digest, byte length and SHA-256. File presence does not
prove complete static linkage, exact OpenBLAS/Boost version or notice applicability.
Those fields deliberately remain `UNVERIFIED` / `UNKNOWN_BLOCKING`.

## Corrections

- Wheel digests and dependency closure now come from the fixed root lock,
  rather than caller-provided expected hashes. Missing/extra/tampered wheels fail.
- Packager includes this inventory in the review ZIP, binds its digest in the
  release manifest and SBOM, and reconstructs it from inner ZIP bytes on verify.
  A forged inventory with an updated envelope hash still fails.
- CPython license provenance now cites v3.14.2 commit
  `df793163d5821791d4e7caf88885a2c11a107986`; the license blob is unchanged.
  Runtime micro-version and embedded third-party applicability need independent review.
- Browser output exposes a Licenses & source code link, exact ACECOG source
  commit, packaged AGPL license, and pinned MPL-covered Pyodide source. The
  third-party packet remains visibly incomplete and unapproved.
- Native inventory tests are included in the WASM workflow test command.
- Browser source-manifest paths use portable forward slashes on Windows.

## Reproduce

```
python -m scripts.verify_bg2_upstream --pinset docs/evidence/bg2-pyodide-core-candidate-pins-v1.json --output build/bg2-evidence/publisher-root-verification.json
python scripts/vendor_browser_pyodide.py --approved-root-pinset docs/evidence/bg2-pyodide-core-candidate-pins-v1.json
python -m scripts.bg2_native_inventory --vendor build/browser-lab/vendor/pyodide --output build/bg2-evidence/locked-native-inventory.json
python -m pytest -q
python scripts/package_bg2_candidate.py build --source-sha EXACT_CHECKOUT_SHA --vendor-source build/browser-lab/vendor/pyodide --output build/bg2-artifacts/review.zip
python scripts/package_bg2_candidate.py verify --source-sha EXACT_CHECKOUT_SHA --output build/bg2-artifacts/review.zip
```

Commit the source inputs before packaging; a dirty source input must fail.
The final handback comment supplies exact executed source and ZIP/SBOM hashes.
Local Windows suite initially produced 81 PASS and one environment failure
because Bash is unavailable (`test_bg1_release_policy`). No all-suite PASS is
claimed. Linux exact-head CI remains necessary; local tests are Builder checks.

## Remaining acceptance and accountable handoff

Security/Licensing must independently download/hash the official archive and
four roots; determine the actual CPython/Pyodide/SciPy/OpenBLAS/Boost and other
compiled components and exact-version full notices/source obligations; review
user delivery and sign the corrected exact packet. The SciPy source bundled
notice index is not itself all required license texts. Builder must incorporate
that component-specific determination before an approved redistribution packet
can exist. Human qualified legal review retains unresolved interpretations,
including AGPL/proprietary Commercial combination; no executable Commercial pin.

Working QA must independently rehash final ZIP/SBOM and rerun negatives.
Release Engineering/Builder must correct R3 review/publication semantics and
investigate check-level CodeQL (workflow success does not clear its failed check).
Accessibility/Release Engineering still owe physical AT/device/zoom/low-memory,
GoDaddy host/CSP/privacy/cache and real rollback evidence. Owner final independent
beta acceptance and separate publication GO remain later gates. PMO records
residuals without changing issued WBS8/FS v0.24 or proposed CL-084 status.
