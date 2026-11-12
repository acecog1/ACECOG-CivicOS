# BG-2 transactional WASM review artifact — reproducibility and handoff

**Status:** Engineering candidate only. **NO Pages/GoDaddy deployment, no BG-2 owner exact-SHA release Go, no independent runtime license/security/QA approval.** This process creates an inspectable *ZIP*, never replaces or edits the BG-1 static site. GitHub Actions `BG-2 sovereign browser feasibility` is the current nondeploying production-*packaging proof*, not a production publishing workflow.

## Artifact contract and how it is assembled

Source checkout must be the **actual PR HEAD or separately approved exact 40-character commit**, never a generated GitHub `pull_request` merge ref represented as if it were the branch's source commit. The workflow checks out `github.event.pull_request.head.sha`, confirms it equals `git rev-parse HEAD` and passes this unchanged value to the packer.

```bash
# From a clean checkout of the intended source commit (not an automatic PR merge):
SOURCE_SHA="$(git rev-parse HEAD)"
python scripts/build_browser_lab.py                       # independent source-extraction checks
python scripts/vendor_browser_pyodide.py                 # feasibility-only: NO approved core root pinset
python scripts/package_bg2_candidate.py build \
  --source-sha "$SOURCE_SHA" \
  --vendor-source build/browser-lab/vendor/pyodide \
  --output "build/bg2-artifacts/bg2-review-$SOURCE_SHA.zip"
python scripts/package_bg2_candidate.py verify \
  --source-sha "$SOURCE_SHA" \
  --output "build/bg2-artifacts/bg2-review-$SOURCE_SHA.zip"
sha256sum "build/bg2-artifacts/bg2-review-$SOURCE_SHA.zip"
```

The static HTML/JS and original CivicOS Python engine/scenario are extracted into **fresh, isolated staging**. WASM vendor inputs must already pass `verify_vendor_directory()`, which rejects missing, extra, symlinked or mutated files and checks the immutable Pyodide lock SHA. Vendor downloading itself also uses a clean sibling staging directory with a backup/restore path on failed replacement. Asset digests are verified *before* writing them to staging; unapproved roots are explicitly flagged `UNPINNED_OBSERVED_ONLY_BLOCK_RELEASE`.

Within the clean package directory, the packer verifies `source-manifest.json` source SHA = checked-out Git HEAD; source asset SHA256 entries = the actual extracted bytes; the Pyodide runtime manifest SHA256 entries = all actually vendored JS/WASM/stdlib/wheel bytes. It builds `release-manifest.json` recording **Git source commit SHA**, **Git source tree SHA**, **source manifest SHA256**, **runtime manifest SHA256**, **every packaged asset SHA256**, and SHA256 of a canonical JSON mapping of all packaged file paths/hashes. A second independent byte-level verifier opens the created ZIP, checks all members and both inner inventory manifests, and confirms its source SHA; any missing/extra/path-escaping/broken asset fails.

The final ZIP uses sorted entries, fixed member timestamps/modes and deterministic compression options. The packer writes it to temporary staging, fully verifies it, and **atomically replaces** only the output ZIP on success. An error in download, file verification, source identity, ZIP creation or post-build verification leaves the previous complete ZIP unmodified. No partial build can be mistaken for the output. These properties are checked by offline tests for build interruption, failed promotion, source mismatch, altered archive bytes, contaminated runtime and repeated byte-identical builds.

**Evidence of reproducibility and independent trust are separate:** Self-consistent hashes alone are **not** a signature or proof of authenticity. QA must obtain the expected source SHA and the final ZIP's SHA256 through an independently trusted review/release record and reproduce the archive before accepting it. Visitor-generated events remain editable synthetic data, with no raw chain replay included in the opt-in export and no authenticated municipal decision implied.

## Nondeployment workflow and future release

- `.github/workflows/bg2-browser-feasibility.yml` checks out exact PR HEAD, runs source and negative integrity tests, fetches vendor dependencies at *build time only*, constructs the review ZIP, verifies source-to-artifact hashes, uploads the ZIP as a **private GitHub Actions review artifact**, then runs actual browser/solver tests. Its explicit `NO Pages deployment` step remains. The existing BG-1 `Site build` workflow and Pages output are **unchanged**.
- The current default vendor build has **no independently approved core JS/WASM/stdlib pinset** and intentionally cannot claim release readiness. QA must compare four pinned core hashes against independent upstream release provenance, assess full package license/SBOM notices and separately certify the result. `--approved-root-pinset` is *only a technical verification input*, not a bypass of independent review.
- A future **new, separately gated BG-2 first-publication workflow** must tie an **approved exact source SHA and source tree** to a reviewed matching ZIP SHA, confirm the full runtime pinset and license/SBOM and independent BG-2 security/a11y/host QA, and receive owner BG-2 final source-identity Go. It must stage a versioned, rollback-ready BG-2 path without replacing the 279-record BG-1 site. That controlled publishing workflow **does not yet exist**.
- Longer-term QA remains: Firefox/Safari, slow/low-memory cold start/bandwidth, true 200% zoom and native assistive technology, GoDaddy nested-frame/full-page fallback and actual privacy/cookie/network/host evidence, Q-39 net WBS8 approval and exact source-specific BG-2 release decision.

**Current synthetic-lineage limitation:** The browser model is an abbreviated independently constructed fictional fixture, **not** the authoritative 279-event reference branch snapshot. No central compute API, visitor submission storage, user credentials, Render deployment or real civic write authority is involved.
