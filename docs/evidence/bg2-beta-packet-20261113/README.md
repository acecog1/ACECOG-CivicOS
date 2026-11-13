# BG2 public-beta licensing/source review supplement

**DRAFT / PUBLICATION HOLD.** This is a review packet, not an approved or deployed beta. Qualified human legal sufficiency and residual accept/reject decisions remain pending. No publication flags are changed.

Download [licensing-source-review.zip](licensing-source-review.zip) and [SHA256SUMS](SHA256SUMS). Extract the ZIP and open `index.html`: it is a static, script-free licenses/source entry point, with full candidate notice texts, source instructions, local links, member mappings and human decision/QA requests. Research-only originals remain separate from component-associated candidate notices; neither category constitutes accepted applicability.

## Exact baselines

- Runtime: PR #16 source `8cd6031bd1dd7aff9e266c0abeb729d9d015bc59`, run `43371657753`, artifact `14011669639`, inner ZIP SHA-256 `c8fa9aa4bf97ec977966167dde2eb02db3681f96b2486df614f2e74f64c85a52` (24,004,439 bytes).
- Ledger/addendum: PR #17 exact `59d6073c68226170c2d63674626f6b3e369da9cf`. No newer runtime artifact is claimed by #17. Its 123-member ledger, all 166 original/evidence records, ten wheel notice sets and four core hashes remain bound to #16. Prior independent unchanged-byte QA is retained.
- Supplement: separate deterministic archive; its SHA256SUMS binds every byte, including `integrity.json`. This does **not** replace or change the old runtime archive. Before/after runtime digest is identical. Any eventual integration into the served runtime requires a new exact candidate and independent QA.

The packet contains full original component-associated notice texts (including libf2c), full embedded notices from all ten shipped wheels, upstream license texts and ACECOG AGPL. It preserves all original research texts and source locations with digests. Missing or unresolved material is recorded rather than represented as complete: Rust 1.97.1 COPYRIGHT-library.html, selected embedded/core headers, effective Boost/pybind11 attribution, and covered-source/patch correspondence. The source page provides full commit pins for ACECOG, Pyodide and hiwire; preserved component source records may use release URLs rather than immutable commits. Notice SHA-256 pins authenticate notice bytes, not entire source archives. Source-tree availability alone does not close source sufficiency.

## Reproduce and verify actual bytes

From the repository root with Node 24:

```
node scripts/build_bg2_beta_packet.mjs /absolute/path/to/exact-review.zip
node scripts/verify_bg2_beta_packet.mjs docs/evidence/bg2-beta-packet-20261113/licensing-source-review.zip SHA256_FROM_SHA256SUMS
```

The builder refuses any other baseline ZIP, checks its release HOLD flags and payload digests, verifies original notices/wheel notice bytes, and emits a deterministic stored ZIP with fixed metadata. The independent verifier checks the archive digest, exact file set, every payload length/digest, and HOLD flags. `integrity.json` excludes itself to avoid a circular digest; the archive sidecar covers it. Rebuilding twice must give identical bytes.

## Remaining decisions and access limitations

`dispositions.json` supplies per-claim M/U, conditional R and C/U classifications, affected member digests, notice references, remediation, owner, revisit trigger and explicit pending accept/reject fields. Historical logs become residual only after mandatory compliance is demonstrated and a qualified human determines them nonessential. No blanket package-level risk acceptance is inferred.

PMO must secure a named qualified reviewer. That person must explicitly ACCEPT or REJECT each residual and decide whole-packet legal sufficiency against exact digests, with rationale and conditions. Builder and automated QA cannot make those decisions. Owner final independent beta acceptance and distinct publication authorization remain separate.

Independent QA is requested to inspect **the committed ZIP bytes**, not merely this README: notices, links, exact member mapping, source/patch sufficiency evidence, checksums, corruption/deletion/addition negatives, keyboard and screen-reader access. See embedded `QA-REQUEST.md`. Local link existence is checked automatically; external HTTP reachability, hosted BG2 source offer, native keyboard/AT/device/zoom/low-memory and real host protections remain **UNTESTED**. Wide CSV/JSON and long original source texts may pose AT/navigation limitations. This supplement does not prove actual hosted accessibility or corresponding-source legal sufficiency.

No merge, deployment, protected variable edit, release-hold closure, legal election, spend or FS/WBS baseline change is authorized or performed.

## Builder recycle correction — 2026-11-13

Replaces the prior supplement digest with SHA-256 `a1192e12a77139a14134fab7323737cd4cee08768b433da884423714295e808d`, 3,806,018 bytes, 217 entries / 216 integrity payloads. Runtime SHA remains `c8fa9aa4bf97ec977966167dde2eb02db3681f96b2486df614f2e74f64c85a52`.

Decision rows now carry explicit multi-component candidate scopes, preserved-original notice IDs, notice/source evidence references and hashes, separate affected core asset hashes, whole-wheel scope including Python sources, unresolved applicability and pending human decisions. B-U2 includes LAPACK/libf2c; B-U4 includes hiwire/CPython/ACECOG and all four core assets; B-U5 includes Rust and tracked runtime crate candidates. Broader candidate pools are review scopes, not findings that every component occurs in every asset. Missing selected headers/mini-lz4, Rust version-specific std notices, effective numerical terms and final correspondence remain unresolved. `required_original_notice_ids` identifies preserved candidate evidence required for this review, not a legally approved exhaustive notice set.

`source-patch-checklist.json` records ACECOG/Pyodide/hiwire candidate source pins with explicit null modification/no-modification evidence, patch hashes, final recipient URL and test time. Missing evidence remains blocking. No repository snapshot is certified as sufficient corresponding source.

Verifier now reconciles central directory, local headers, offsets/counts, exact boundaries, names, CRCs, manifest file set, decision references and HOLD state. It intentionally supports only this generator's stored ZIP format. Run `node scripts/test_bg2_beta_packet.mjs` for eight negative cases using recomputed archive digests: altered central offset/CRC/name, duplicate name, trailing entry, count mismatch, payload corruption and truncation. Builder observed all eight rejected; deterministic repeat build matched; independent .NET ZIP reader enumerated all 217 entries and rehashed all 216 payloads. These are Builder checks, not independent QA acceptance. Missing/extra manifest semantics and broader malformed-format tests remain for independent QA.

Independent QA: obtain the newly committed ZIP bytes, verify this exact digest and revised associations; retain prior unchanged-runtime QA. Security/Licensing: assess actual required terms and correspondence, including missing evidence. PMO: arrange qualified human review privately; no reviewer identity is requested for public posting. Human legal sufficiency, residual acceptance, external HTTP/final-host source access, native AT/device testing and release gates remain OPEN/HOLD.
