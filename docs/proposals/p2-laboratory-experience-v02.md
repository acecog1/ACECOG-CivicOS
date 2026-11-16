# P2 — Laboratory Experience v0.2 (local usability prototype)

**Date:** 2026-11-11. **Founder directive:** "yes, P2 go", reaffirmed "agreed." **Authorization:** implement and test the visitor-experience slice on top of the already approved Q-39 *local proof-of-concept*. This is **not** a public BG-2 release decision, accepted WBS8 change, canonical-history certification, AI provider approval, or permission to contact a civic body.

## Experience hypothesis

A visitor who has never used a governance model should be able to:
1. Recognize an approachable fictional civic dilemma;
2. Choose water scarcity, financial limits or council vote reversal as a starter;
3. See the knobs and simulated votes underlying the experiment;
4. Run the **actual** CivicOS engine, compare authorization outcomes and resource allocations;
5. Read a deterministic explanation with explicit unknowns and retain reproducible evidence without an account.

The scenario is synthetic Riverbend, not a real municipality. **No outcome conveys a legal decision, measured social benefit or established ecological result.**

## Implemented candidate: P2-LAB-UX-01 through 06

| ID | User-visible behavior | Acceptance evidence |
| --- | --- | --- |
| UX-01 | Guided fictional civic dilemma and three labeled presets | Browser tests verify vote-preset changes and actual engine rejection |
| UX-02 | Guided/detailed exploration explanation; full parameter controls always available | Browser test verifies mode switching; keyboard/axe regression retained |
| UX-03 | Reference and alternative approvals, no phantom funding after rejection; accessible dollar-allocation bars plus exact-value table | Browser tests verify source-backed solver graphics and rejected-plan omission |
| UX-04 | Changes invalidate stale displayed output; history of at most 3 recent runs in memory with input restoration | Browser tests verify history controls and reset on reload |
| UX-05 | Opt-in downloaded JSON evidence record and copied JSON recipe (manual fallback) | Browser test verifies real local download, hash and advisory label |
| UX-06 | 320px responsive design, no external scripts/cookies/telemetry or general public API | Browser no-external-requests, page-error, mobile tests; independent manual a11y still pending |

**Design details:** preset buttons only populate form inputs; they never quietly run a different outcome. "Surprise me" remains explicitly seeded; same random seed is only associated with a run when the visitor has not subsequently edited its values. Restoring an earlier run restores **inputs**, then requires a fresh engine execution. Session history lives in JavaScript memory only and disappears on reload. The local export contains reference and alternative receipts and model constraints; no authentication token is included. "Copy" produces a JSON recipe, **not** a hosted/shareable link. The numeric plots visualize existing solver receipts, do not add unmodeled benefit indicators or invented impact measures.

## Deliberately not implemented or not claimed

- **Public host:** existing `scripts/lab_preview_server.py` stays bound to `127.0.0.1`; no Internet-accessible service, user account, backend storage or infrastructure changes.
- **Canonical fork:** the fixture is abbreviated; it is **not** a fork of the verified published 279-event BG-1 chain. The v0.2 interface removes a confusing "canonical model inputs" description.
- **Independent QA:** test success is automated evidence, not an outside reviewer or BG-2 security/privacy/a11y sign-off.
- **True shareable replay:** a recipe/export can be copied to another tester but there is no server-hosted per-run URL or independently portable verification package for raw event bytes.
- **AI guide:** existing rule-based narrative stays in control; no LLM or founder strategy access.
- **WBS/FS:** this is a development candidate under Q-39; CL-084 and WBS8 incremental labor/operations delta remain subject to PMO/owner adoption.

## Review checklist and next gate

1. **Builder** verifies current commit, JS syntax, exact browser flows, consistency between bar graph/table and solver receipts, local-only served assets, and no residual CodeQL alerts.
2. **Skeptical QA** checks beginner comprehension, outcome status, recused vote refusal, stale-input state, history memory-only behavior, export data minimization, manual clipboard fallback, accessibility at browser 200% zoom with assistive technology, and 320px/keyboard navigation.
3. **PMO** maps the new UX slice to WBS8 1.7.1/1.7.5 and Q-39 C4. Estimate reuse vs net new work before changing the issued Excel master.
4. **Founder** reviews a working local preview and decides iteration priorities separately from BG-1 static beta or BG-2 hosted simulator.

**Disposition at authoring:** DEVELOPMENT CANDIDATE; DRAFT PR; MERGE / BG-2 PUBLICATION HOLD pending exact-head CI, independent review and later release decision.
