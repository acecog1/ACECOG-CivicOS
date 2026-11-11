# BG-2 hosted P2 scenario lab — staged candidate and operational gates

**2026-11-11 | Change authority:** Founder gave P2 public-release direction ("approved for release"), followed by "proceed". This authorizes release preparation. **It does not eliminate separate operational, host-cost, independent security/accessibility/privacy QA, and exact-source release checks**. Current public CivicOS main, the BG-1 279-event static walkthrough, and GoDaddy W+M must remain untouched until independent gate closure.

**Branch dependency:** feature/bg2-hosted-staging-gateway → P2 feature/p2-laboratory-experience-v02 (PR #6) → local simulator feature/riverbend-counterfactual-lab-poc (PR #5). This is a source candidate. Public BG-2 URL and actual Render service ID are **NOT YET KNOWN**.

## What has been implemented for staging

- `scripts/bg2_wsgi.py`: separate restrictive WSGI interface; supports only `GET /`, asset GETs, `GET /healthz`, `GET /api/config`, `GET /api/random`, and `POST /api/compare`. No arbitrary engine commands, auth or binding civic rights. Secure base host is an exact environment-provided FQDN, including Render-provided `RENDER_EXTERNAL_HOSTNAME`; HTTPS Origin match, no CORS access, no cookies/telemetry, CSP and anti-framing headers. `BG2_SIGNING_KEY` must be a generated >=32-character secret or service refuses requests.
- HMAC short-lived bearer-style synthetic form token returned on GET config (not a real civic identity credential). Numeric and fictional-vote parameters validated against original strict library, 4096-byte request and 512-KiB response ceilings, synchronous single-compute semaphore and conservative per-process global rate window, computation offloaded to a short-lived subprocess with bounded timeout. This is controlled *anonymous* compute, not a multi-tenant accounts platform.
- `scripts/bg2_compute_worker.py`: reads only bounded typed synthetic assumptions, executes original real CivicOS engine compare and closes. Never launches a public generic `server.py` or mutates real civic state.
- `scripts/bg2_prepare_assets.py`: uses the existing tested P2 source, generates explicitly labeled hosted copy with real host-logging caveat; static output fails if expected markers drift. The original localhost P2 workflow remains independently testable.
- `tests/test_bg2_wsgi.py`: configuration fail-closed; correct hosted copy; security headers; exact Host/Origin/token; invalid values/recusal and oversized-body rejection; global per-process throttle; real vote-flip child and approved-candidate execution.
- `requirements-bg2.txt` pins the runtime plus original engine/test dependencies. `docs/deploy/bg2-render-staging.yaml.example` is **an intentionally inactive template**, not an autodeploy root blueprint.

## Provisioning when Render is connected

1. Independent QA inspects the exact source and control boundaries **before** public exposure. If first service creation would expose a URL to the Internet, record a bounded staged-publication risk decision and monitoring/rollback plan first.
2. Create a Render web service (not the existing BG-1 GitHub Pages site) linked to the **immutable reviewed source commit**, using the staging template: single Gunicorn gthread worker / four web threads, 12-second compute child timeout, 30-second request worker timeout, no automatic deploys, initial `BG2_MODE=staging`, generated signing secret. Set Python 3.13 explicitly. Check full service specification against Render's current UI and quotation before committing to a paid plan.
3. For its `onrender.com` hostname, use Render's `RENDER_EXTERNAL_HOSTNAME`; custom domains are not part of this release. Configure HTTPS-only and provider request/abuse ceilings. **App's local global throttle is not a WAF, distributed limiter or independent DoS certification**.
4. Record actual service URL, host response headers, origin behavior, certificate, provider logs, privacy and retention details, resource consumption, concurrency, scaling and shutdown behavior. The app does not store visitor scenarios itself, but the hosting provider may process connection metadata.
5. Independent QA confirms P2 walkthrough flows (run, reject, no ghost funding, budget/water sensitivity, narrative, downloadable raw evidence) at real 320/390px and 200% zoom with keyboard/native AT and assistive users as feasible. Verify no analytics/third-party telemetry; prove anonymous request cost ceilings and abuse recovery, replay integrity, and no leak of system secrets.
6. Only after exact deployed SHA QA GO and owner/PMO reconciliation, change `BG2_MODE` to public and expose a prominent **Open interactive laboratory (new tab)** link from the existing GoDaddy `acecog.org/beta` wrapper. Do **not** weaken frame-ancestors or rely on an iframe; embed is intentionally disallowed. Verify the external live URL before modifying the W+M page. GoDaddy edit is a separate, auditable operation.
7. Keep a one-click service suspend/delete/rollback path. Monitor high error or overload rates, unexpected host-level logs, memory, and costs; fail closed if the signed token key is absent.

## Outstanding blocking risks / independent QA handback

| ID | Remaining gate | Status |
| --- | --- | --- |
| HOST-01 | Render app connected, exact deploy SHA and service/provider configuration verified, monthly expense approved | **OPEN** |
| SEC-01 | Independent review of host/origin handling, HMAC replay, nonbrowser abuse, whole-site cross-origin, logging privacy, rate-limit bypass, proxy, and deployment pipeline | **OPEN** |
| SEC-02 | Provider-edge anti-abuse, capacity exhaustion, forced process timeouts, load test, infrastructure monitoring/rollback | **OPEN** |
| UX-01 | Browser integration tests with real hosted HTTPS network; manual 200% zoom and assistive technology | **OPEN** |
| PROV-01 | Release evidence with model/source/solver versions; genuine canonical 279-event predecision snapshot/replay not implemented | **OPEN (disclose gap)** |
| CIVIC-01 | Fictional/no-legal-effect disclosure and prohibition on real roles/votes/funding; independent claim review | **OPEN** |
| PMO-01 | WBS8 net change impact and actual recurring provider cost/risk decision; original XLSX remains controlling | **OPEN** |
| BG-1 | Static first-publication state and any existing W+M embed verified without altering BG-1 source | **OPEN** |
| BG-2 | Independent exact-SHA release QA, publication GO and verified public endpoint | **HOLD** |

**Substantial limitations:** single-process rate counter is deliberately conservative and does not protect against distributed adversaries by itself; request tokens are anonymous browser-bound bearer-style anti-cross-origin affordances, not user authentication; no database, no durable or cross-session restore, no independent third-party event-chain export, no LLM, no measured real social/ecological outcomes. A successful CI status alone does not close these gaps.

## Current pricing reference (quotation only, NOT approved spend)

As of 2026-11-11 the Render public pricing page lists a 1 CPU / 2 GB web instance at roughly **$25/month** before any applicable bandwidth or additional usage charges. See https://render.com/pricing and the current Render account quote. This is a **candidate** resource class; performance and billing require verification and explicit operational approval. No paid service was created by committing this file.
