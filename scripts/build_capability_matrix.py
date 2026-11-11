"""Generate technical capability evidence from the actual engine scenario and public status input."""
import csv, io, os, re, sys, json
from collections import defaultdict

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.insert(0, os.path.join(ROOT, "src"))
sys.path.insert(0, os.path.join(ROOT, "tests"))
from acecog.contract import API_VERSION, COMMANDS, QUERIES, SPEC_VERSION  # noqa: E402

OUT_MD = os.path.join(ROOT, "docs", "capabilities", "capability-matrix.md")
OUT_CSV = os.path.join(ROOT, "docs", "capabilities", "capability-matrix.csv")
REGISTER = os.path.join(ROOT, "docs", "capabilities", "implementation-status.json")

# Gates every mutating public capability waits on (plan section 7, "preinteractive launch gates").
SANDBOX_GATES = "G-041 auth; B-1 tenancy; B-2 quotas; G-042 threat model"

# ---- proposed exposure (owner approval pending) --------------------------------------------------
# mode: P-1 = public read-only reference walkthrough (real engine output, no mutation by visitors)
#       P-2 = interactive isolated sandbox with a demo role grant
#       P-3 = later milestone; Eval = evaluator workspaces only; Off = not exposed publicly
MEMBER = ("P-2", "Any demo member of the visitor's own sandbox body")
OFFICER = ("P-2", "Demo role holding that authority, granted by the sandbox Governance Process")
EXPOSURE = {
    "civic-bodies.create": ("P-3", "Exploration lab; founding moves to an External Convener case with G-023"),
    "governance-processes.adopt": OFFICER, "authorities.grant": OFFICER, "delegation-envelopes.adopt": OFFICER,
    "legal-effect-declarations.adopt": ("Off", "Never in the public sandbox: a declaration turns 'Advisory' into a legal "
                                        "label (PUB-009). Shown read-only in the reference walkthrough"),
    "compliance-packs.adopt": ("Eval", "Fictional packs only; real-law modules (G-025) never in a sandbox"),
    "credentials.issue": OFFICER, "interest-declarations.record": MEMBER, "delegations.assign": MEMBER,
    "delegations.revoke": MEMBER, "propositions.submit": MEMBER, "propositions.amend": MEMBER,
    "deliberation.post": ("P-2", "Any demo member; moderation and content-abuse controls apply (B-3)"),
    "votes.cast": MEMBER, "decisions.close": OFFICER, "evidence.record": MEMBER, "constraints.attach-evidence": OFFICER,
    "optimization-runs.request": ("P-2", "Any demo member; per-session solver quota (PUB-012, B-2)"),
    "baselines.create": OFFICER, "commitments.reserve": OFFICER, "actuals.post": OFFICER,
    "rebalances.propose": OFFICER, "exceptions.resolve": OFFICER, "change-requests.put-in-force": OFFICER,
    "exports.create": ("P-2", "Own sandbox only; verifiable and rehydratable (PUB-013)"),
    "retention-schedules.adopt": ("Eval", "Records administration; evaluator workspaces"),
    "records.delete": ("Eval", "Records administration; evaluator workspaces. Sandbox reset is a separate operator job"),
    "configuration.set": ("Off", "Deployment setting; operator only"),
}
QUERY_EXPOSURE = {"/v0/queries/feed/{actor_id}": ("P-2", "The visitor's own demo identity")}
QUERY_DEFAULT = ("P-1", "Anyone, on the reference body; own sandbox in P-2")

# Showcases (plan section 6) -> the backlog rows they depend on.
SHOWCASES = [
    ("Riverbend Commons reference case (26.1-26.2)", [], "P-1"),
    ("Civic Authority Continuity (17.9, 26.3)", ["G-023"], "P-3"),
    ("Upper Rio Verde Ecosystem Endowment (42)", ["G-037"], "P-3"),
]
# Beta platform capabilities that are not engine features (plan sections 3-4, 7, 10).
PLATFORM = [
    ("Caller authentication and authorization", "G-041", "PUB-005"),
    ("Threat model incl. prompt injection and solver abuse", "G-042", "PUB-004"),
    ("Desktop structured surface", "G-044", "PUB-007"),
    ("Resident mobile PWA", "G-045", "PUB-010"),
    ("Guest Proposer fit-check preview", "G-046", "PUB-007"),
    ("Conversational drafting parity", "G-039", "PUB-010"),
    ("AI-generated text labelled", "G-040", "PUB-003"),
    ("Accessibility WCAG 2.2 AA", "G-031", "PUB-011"),
    ("Per-visitor sandbox tenancy, reset, cleanup (B-1)", None, "PUB-006, PUB-013"),
    ("Quotas and rate limits for solver and AI (B-2)", None, "PUB-012"),
    ("Content moderation and abuse controls (B-3)", None, "PUB-004"),
    ("AI role/story onboarding guide (B-4)", None, "PUB-003, PUB-004"),
    ("Public hosting, observability, incident response (B-5)", None, "PUB-001"),
    ("Capability manifest published in the beta (B-6, this file)", None, "PUB-002, PUB-015"),
]
STATUS = {"✅": "Met", "🟡": "Partial", "❌": "Missing", "◻": "Interface only"}


def run_scenario():
    """Run the contract scenario, recording which calls each check exercised."""
    import scenario as S
    calls, per_check = [], []
    stats = defaultdict(lambda: {"calls": 0, "accepted": 0, "refused": 0, "escalated": 0})
    orig_cmd, orig_q, orig_check = S.cmd, S.q, S.check

    def cmd(name, *a, **k):
        r = orig_cmd(name, *a, **k)
        st = stats[name]; st["calls"] += 1
        if r.get("outcome") in ("accepted", "refused", "escalated"):
            st[r["outcome"]] += 1
        calls.append(name)
        return r

    def q(path):
        key = next((t for t in QUERIES if re.fullmatch(re.sub(r"\{[^}]+\}", "[^/?]+", t) + r"(\?.*)?", path)), path)
        stats[key]["calls"] += 1
        calls.append(key)
        return orig_q(path)

    def check(test_id, title, cond, detail=""):
        per_check.append((test_id, bool(cond), set(calls)))
        calls.clear()
        return orig_check(test_id, title, cond, detail)

    S.cmd, S.q, S.check = cmd, q, check
    try:
        S.run_all()
    finally:
        S.cmd, S.q, S.check = orig_cmd, orig_q, orig_check
    tests = defaultdict(set)
    failed = defaultdict(set)
    for tid, ok, used in per_check:
        for u in used:
            (tests if ok else failed)[u].add(tid)
    passed = sum(1 for _, ok, _ in per_check if ok)
    return stats, tests, failed, passed, len(per_check)


def read_register():
    data = json.load(open(REGISTER, encoding="utf-8"))
    return data["gap_states"], data["acceptance_coverage"]


def short(s, n=90):
    s = re.sub(r"\s+", " ", s)
    return s if len(s) <= n else s[:n - 1].rstrip() + "…"


def build():
    stats, tests, failed, passed, total = run_scenario()
    gaps, coverage = read_register()
    manifest = []
    for name, (summary, refs, rules) in COMMANDS.items():
        st, t = stats.get(name, {}), sorted(tests.get(name, ()))
        status = "Tested" if t and not failed.get(name) else ("Implemented" if name in COMMANDS else "Specified")
        mode, scope = EXPOSURE[name]
        paths = [k for k in ("accepted", "refused", "escalated") if st.get(k)]
        gate = "" if mode in ("Off",) else (SANDBOX_GATES if mode in ("P-2", "P-3", "Eval") else "")
        manifest.append({"capability": name, "kind": "command", "summary": summary, "spec": refs, "rules": ", ".join(rules),
                         "status": status, "scenario_calls": st.get("calls", 0), "paths": "/".join(paths),
                         "proof": ", ".join(t), "exposure": mode, "scope": scope,
                         "gates": gate + ("; " if gate and mode == "P-3" else "") + ("G-023" if name == "civic-bodies.create" else "")})
    for path, (summary, refs) in QUERIES.items():
        st, t = stats.get(path, {}), sorted(tests.get(path, ()))
        mode, scope = QUERY_EXPOSURE.get(path, QUERY_DEFAULT)
        manifest.append({"capability": "GET " + path, "kind": "query", "summary": summary, "spec": refs, "rules": "",
                         "status": "Tested" if t and not failed.get(path) else "Implemented",
                         "scenario_calls": st.get("calls", 0), "paths": "read" if st.get("calls") else "",
                         "proof": ", ".join(t), "exposure": mode, "scope": scope,
                         "gates": "Public read-only deployment (B-5)" if mode == "P-1" else SANDBOX_GATES})
    return manifest, gaps, coverage, passed, total


def render(manifest, gaps, coverage, passed, total):
    tested = sum(m["status"] == "Tested" for m in manifest)
    lines = ["# Technical capability evidence", "",
        f"API {API_VERSION}; {SPEC_VERSION}. Scenario: {passed}/{total} checks. "
        f"Exercised API capabilities: {tested}/{len(manifest)}.", "",
        "These are bounded scenario checks, not full Phase 1 acceptance. Source inclusion does not enable "
        "a public service or civic authority. Exposure modes remain proposed; mutable operations require "
        "their authentication, isolation, abuse and release gates.", "",
        "| Capability | Summary | Spec | Status | Scenario proof | Proposed mode | Release blockers |",
        "|---|---|---|---|---|---|---|"]
    for m in manifest:
        lines.append(f"| `{m['capability']}` | {short(m['summary'], 80)} | {m['spec']} | {m['status']} | "
                     f"{m['proof'] or 'not exercised'} | {m['exposure']} | {m['gates'] or 'none claimed'} |")
    lines += ["", "## Acceptance coverage", "",
              "Dated technical coverage snapshot; not a claim that every requirement has been implemented.", "",
              "| Family | In scope | Covered |", "|---|---:|---:|"]
    lines += [f"| {a} | {b} | {c} |" for a,b,c,_ in coverage]
    lines += ["", "## Remaining implementation limits", "",
              "| Gap | Technical requirement | State |", "|---|---|---|"]
    for gid,g in sorted(gaps.items()):
        if g["status"] != "Met":
            lines.append(f"| {gid} | {g['req']} | {g['status']} |")
    return "\n".join(lines)+"\n"


def render_csv(manifest):
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=list(manifest[0]), lineterminator="\n")
    w.writeheader(); w.writerows(manifest)
    return buf.getvalue()


def outputs():
    manifest, gaps, coverage, passed, total = build()
    return {OUT_MD: render(manifest, gaps, coverage, passed, total), OUT_CSV: render_csv(manifest)}


if __name__ == "__main__":
    for path, text in outputs().items():
        open(path, "w", encoding="utf-8").write(text)
        print("wrote", os.path.relpath(path, ROOT))
