# BG-2 browser-only laboratory — sovereign/serverless architecture decision

**Executive direction, 2026-11-11:** Founder explicitly selected "**serverless and sovereignty oriented please**" over Render-hosted Python. This amends the BG-2 *deployment architecture*; it is not authorization to merge into public `main`, claim independence of QA, modify WBS8 master, publish a live application, or represent a synthetic decision as legally operative.

## Design thesis and limits

Serve everything as static files. GoDaddy W+M stays ACECOG's public entrance; GitHub Pages distributes the immutable existing BG-1 scenario/evidence and, after separate BG-2 approval, the downloadable visitor interface and its **self-hosted** browser runtime. The hypothetical Riverbend case is computed in the visitor's own browser through a dedicated Web Worker running Pyodide (WASM CPython), NumPy, SciPy and JSONSchema, invoking the **actual** CivicOS engine with an isolated synthetic model. No central compute API, no visitor account, no database, no cookies, no server-stored scenario history, no outside computation calls.

**Caveat:** Browser computation is controlled by the visitor. Results are *reproducible evidence candidates*, not authoritative civic records. They can be edited or forged by their owner; only independent bundle verification and the eventual true civic governance layer can establish authenticity/authority. The current local demonstration is an **abbreviated branch**, not an exact 279-event BG-1 predecision fork.

## Provenance and source design

The `scripts/build_browser_lab.py` static builder copies source from exact Git checkout, extracts only `NODES` and `scenario.model` from the historical Python test source without pulling in the test HTTP server, and packages the unchanged `acecog.engine`, `contract`, and `experiment_riverbend` modules. It emits a SHA-256 manifest for source assets and declares the shortened synthetic lineage. P2 display and form controls are reused, with the HTTP-call site redirected to an allowlisted in-tab Web Worker bridge. Explicit manual export stays local.

The Web Worker uses `import("./vendor/pyodide/pyodide.mjs")` and loads SciPy/JSONSchema/NumPy from the same static host only. No runtime CDN, general-purpose command endpoint, arbitrary Python supplied by visitors, real actors/authority, authenticated role or billing account. Only validated synthetic comparison/randomization methods are exposed to the UI. A computation watchdog fails closed and terminates an unresponsive Worker.

At build time only, the Python vendoring script pulls **Pyodide 314.0.7** core and selected dependency-closed packages from a fixed HTTPS upstream path. It pins the observed release lock SHA-256 `5dc2fc119108bc148c7457dc86e7675b5c87e1cafd420b9c34c1eaef7b36c010`, verifies each package wheel against the lock, records an artifact manifest, and enforces a 240 MiB build cap. More independent provenance/attestation and license notice work is required before publication. No vendor libraries are committed to `main` by this PR.

## Release and validation acceptance

| Gate | Required evidence | Current status |
|---|---|---|
| Browser real engine | Actual CivicOS governance and SciPy solver executes inside Chromium/Pyodide Web Worker; approved/rejected vote case and no phantom funding | **One Chromium test passed** at first proof; additional numerical parity under test |
| Source fidelity | Model extraction agrees with source; manifest hashes complete; strict self-only CSP; no active HTTP server | 3 bundle tests passed |
| Reproducibility | Same seed/same input match per browser build; event-chain verification; solver fingerprint displayed; compare native SciPy and WASM dollar allocations with defensible numeric tolerance | Acceptance test submitted; **do not assume raw chain heads match across solver version changes** |
| Supply chain | Self-hosted runtime/assets; lock and wheel SHA verification; core asset digest pin; license inventory; no third-party browser requests | Package vendor succeeded with ~30.9 MB assets; additional audit open |
| UX and accessibility | Prompt narrative, budget/water/crew/vote controls, exact numeric table and chart, keyboard, 320px, actual 200% zoom, native screen reader | P2 automated tests passed; real manual accessible acceptance open |
| Privacy and sovereignty | No simulation payloads sent to hosts, no third-party CDN/analytics; ordinary static web hosting sees page retrieval metadata; browser memory and downloads user-controlled | Local Chromium test detected no third-party calls; independent host/network review open |
| Hosting and release | BG-1 frozen 279-event evidence unchanged, GitHub Pages exact-release SHA and deployment gates verified, full-page fallback from GoDaddy W+M | **HOLD** — no Pages/GoDaddy updates |
| PMO and operating cost | Reconcile WBS8: remove Render Python service and related OPEX; add vendoring, browser compatibility, QA and runtime provenance work; capacity/critical-path delta | Planning change pending net estimate; XLSX unchanged |
| Independent QA | Security/supply chain, abuse, privacy, disability access, replay truth, cross-browser and rollback signoff | **HOLD** |

## Known economic and user considerations

- Python scientific WASM runtime and transitive package files currently total **30.9 MB** in the proof artifact. The actual transfer size, cache behavior and cold-start on low-memory phones require measurement. The client does the computation; GitHub Pages still serves the bytes and is subject to site and bandwidth limits.
- GitHub Pages documentation currently states a maximum published site size of 1 GB and a soft 100 GB/month bandwidth allowance; monitor real requests and choose a portable alternative static host before exceeding the service's terms.
- Offline packaging **after downloading static assets** is plausible, but remains separately gated. Standard GitHub Pages is not itself an offline-first distribution mechanism; no automatic service-worker caching is being added here.
- Browser-only model calculations are not an adequate replacement for multi-person authoritative civic state, identity, deliberation rights, legally binding records or signed institutional governance. These remain future modules with their own evidence/authority/hosting design.

## Disposition

**BG-2 architecture choice: browser-only / sovereign / static distribution GO.** Render PR #8 was closed unmerged and retained as superseded evidence. Builder PoC [PR #10](https://github.com/acecog1/ACECOG-CivicOS/pull/10), owner issue [#9](https://github.com/acecog1/ACECOG-CivicOS/issues/9). Owner earlier approved release intent, but actual public launch remains **HOLD pending stage-specific independent QA, source pin, cost reconciliation and verified Pages/GoDaddy workflow**. No real civic effects or public APIs authorized.

## P2 source integration — local computation input lock (11 Nov 2026)

The browser-only distribution now **inherits** the P2 input-lock correction from
`feature/p2-laboratory-experience-v02` at commit `7af2a2e90299569b516e4128d6049bcb78731c1f`.
While a compare or seeded random selection is pending, number fields, fictional
vote radios, presets, reset, randomize, run and in-tab history restoration are
temporarily disabled; `aria-busy` identifies the pending state. A separate
input revision and serialized-parameter equality check discards any late result
if assumptions somehow changed despite the UI lock, and no previous scenario
remains exportable during a new run. Failure and stale-reply paths unlock the UI.

The deterministic delayed-route Playwright cases cover success, error, stale
forced input and stale random response. The true WebAssembly/Chromium test also
asserts busy/restore behavior through the self-hosted cold-start worker path.
This resolves **one** QA defect in P2; it does **not** resolve the other BG-2
supply-chain, evidence, performance/accessibility and publication holds. No
static Pages deployment, Render service or real civic state is enabled.
