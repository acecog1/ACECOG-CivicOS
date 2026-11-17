# Riverbend local interactive laboratory (development preview)

**NOT a public site, NOT a production API, NOT the canonical BG-1 Riverbend record.**  
This feature branch adds a local-only browser frontend over the real CivicOS counterfactual engine. It does not modify GitHub Pages, the existing 279-event Riverbend source artifact, or GoDaddy W+M.

## Run the preview

From a local CivicOS checkout with the pinned Python dependencies installed:

    python scripts/lab_preview_server.py --port 8767

Then open **http://127.0.0.1:8767** in a browser. The server binds only to numeric IPv4 loopback, refuses requests with mismatched Host headers, disallows cross-origin POSTs, and requires a process-local session token. It does not open any general CivicOS command endpoint.

Change the annual investment budget, watershed draw ceiling, crew capacity, non-grant appropriation ceiling and fictional Plan A votes. Recused Eli is not selectable. Click **Run with CivicOS engine** to execute two fresh, independent governance branches through the actual Python engine. See the decision tally, actual optimizer allocations where a hypothetical plan is approved, baseline/commitment effects, evidence digests and the deterministic impact narrative. **Surprise me** selects seeded input assumptions; it does not automatically calculate or randomize the page on refresh. Inputs reset when the page reloads.

The browser calls only the local preview service. It does not retain visitor input or transcripts, and it contains no external scripts, cookies, analytics or LLM connection. Engine state is in memory and discarded when a run ends. Users should not submit personally identifiable information: this interface accepts bounded numeric and fictional-vote parameters only.

## Reproduce the tests

    python -m pytest -q tests/test_riverbend_counterfactual.py tests/test_lab_preview_server.py

The regular GitHub Site build workflow runs the full browser suite (including
\`scripts/site_checks/lab_browser.test.cjs\`) through Chromium/Playwright and axe-core.
Browser checks cover vote reversals, actual allocations, explicit randomization,
no accidental random refresh, mobile root reflow, no external network requests
and basic accessibility scanning. The broader \`npm test --prefix scripts/site_checks\`
also checks the published static BG-1 source artifact.

## Deliberately incomplete

1. **No full 279-event fork:** The lab reuses the Riverbend 10-project fixture and existing CivicOS governance rules, but creates a shorter isolated synthetic history. Full canonical predecision snapshot lineage remains L3 work.
2. **Not a public session service:** A locally guarded endpoint is not a production security boundary. No live-user isolation/tenant authentication, audit/retention policy, WAF, service quotas or hosting assurance is claimed. Do not change the bind address or deploy this server to an internet-facing host.
3. **No AI narration:** The explanation is deterministic and evidence-based. A future Q-25-constrained language model may summarize accepted receipts, but may not create calculations, authority, or claims of external impacts.
4. **No real-world civic effect:** Synthetic votes, advisory legal status, fictional authority grants, and in-memory funding reservations cannot be treated as public decisions or real appropriations.
5. **No release Go:** This branch is a draft PoC. Live public BG-2 requires a separately reviewed host, source/engine provenance, true session isolation, threat model, privacy terms, accessibility evidence, independent QA and founder exact-SHA publication authorization.

**Control links:** Private change packet Q-39 in ACECOG-Internal; public CivicOS draft PR #5; historical BG-1 remains frozen on public main.
