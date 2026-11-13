# ACECOG BG-2 — Owner's lean beta acceptance card

**Staging entry:** https://acecog.org/beta (Owner-selected GoDaddy Websites + Marketing route). **Status:** test plan only. This page is NOT asserted to currently serve BG-2; no staging/publication or owner GO occurs from this document.

**Before the Owner test (Release Engineer + working QA):**
- Write exact Git SHA, archived ZIP SHA-256 and staging version onto a single receipt; verify served files match the reviewed candidate and retain the before-state/restoration instructions. Preserve BG-1 reference.
- Verify the /beta landing path opens the same reviewed version, a full-tab fallback (if embedded), HTTPS, expected requests only, privacy/CSP and repeatable rollback. If GoDaddy cannot host the approximately 30.9 MB static runtime, record its limitation; don't silently buy or substitute hosting.
- Make license/source/notice packet and residual native screen-reader/low-memory coverage plainly visible. A working synthetic demo does not confer civic authority.

**Owner runs these six steps at the final beta gate:**
1. Open `/beta` in a fresh/private browser window; note device, browser and whether the page says BG-2 plus the supplied candidate version. If only BG-1 appears, stop: BG-2 is not staged.
2. Start the fictional Riverbend laboratory and run the default case. Confirm the page distinguishes a **synthetic proposal** from a civic act and shows the outcome/explanation.
3. Change two fictional votes (Cara + Dev) and run again. The outcome should reverse; reset/refresh should visibly restore the initial synthetic inputs.
4. Attempt another run while one is pending. Verify progress, no stale results and understandable retry/help if it fails.
5. Navigate with keyboard, enlarge browser to 200% and try a narrow mobile width. Ensure votes are explicitly linked to each person's name, recusal is clear, and the results can be read; record actual screen-reader behavior only if exercised.
6. Inspect the displayed change summary/export/history and use the documented rollback/revert check with Release Engineer. It must never claim a real vote, approved public funding, or signed governance decision.

**Record one result:** `exact SHA | device/browser | checks passed | issues (steps/screenshots) | PASS/RECYCLE/HOLD | Owner signature/date`. Final beta QA PASS and any separate Owner publication GO are distinct. Qualified license/redistribution review and protected release gate remain separate prerequisites. No unperformed device/AT test is represented as PASS.
