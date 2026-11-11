"""Build the minimal public beta site (WBS 1.7.2, milestone M-18): a read-only walkthrough of the Riverbend
Commons reference case, generated from a fresh run of the real engine.

Nothing on the site is hand-written data. Every name, number, vote, refusal and hash comes from the engine run that
this script performs, and the full hash-chained event log ships with the site so a visitor's browser can re-check it.
The site is static and read-only: no forms, no accounts, no cookies, no third-party requests (fonts are self-hosted
when present in site_assets/fonts; otherwise the system font is used).

    python scripts/build_site.py                 # writes build/site/
    SITE_CONTACT=morgan@acecog.org python scripts/build_site.py
"""
import html, json, os, shutil, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.insert(0, os.path.join(ROOT, "src"))
sys.path.insert(0, os.path.join(ROOT, "tests"))
from acecog.contract import API_VERSION, COMMANDS, QUERIES, SPEC_VERSION  # noqa: E402
from acecog.engine import Engine, canon, verify_chain  # noqa: E402

OUT = os.path.join(ROOT, "build", "site")
ASSETS = os.path.join(ROOT, "scripts", "site_assets")
E = html.escape


def money(x):
    return f"${x:,.0f}"


def run():
    import scenario as S
    eng = Engine()
    S.run_all(eng)
    return eng, S


def collect(eng, S):
    T = lambda t: [o for o in eng.obj.values() if o["object_type"] == t]  # noqa: E731
    V = lambda oid: eng.versions[oid]  # noqa: E731
    name = lambda a: eng.actors.get(a, {}).get("display_name", a)  # noqa: E731
    cb = T("civic_body")[0]
    proc = V(T("governance_process")[0]["id"])[0]
    model_versions = V(T("portfolio_model")[0]["id"])
    model = model_versions[0]
    nodes = {n["id"]: n for n in model["nodes"]}
    cons = {c["id"]: c for c in model["constraints"]}
    props = {p["id"]: p for p in T("proposition")}
    dec = eng.obj["decision-0001"]
    run_ = next(r for r in T("optimization_run") if r.get("commit_eligible"))
    base_versions = V(T("baseline")[0]["id"])
    env = next(x for x in T("delegation_envelope") if x["decision_class"] == "routine_rebalance")
    refusals = [ev for ev in eng.events if ev["type"] == "command.refused"]
    escalations = [ev for ev in eng.events if ev["type"] == "command.escalated"]
    resolved = [x for x in T("exception_proposition") if x["state"] == "Closed"]
    ok, n = verify_chain(eng.events)
    assert ok, "hash chain must verify before publishing"
    return dict(
        cb=cb, members=[name(a) for a in eng.actors if eng.actors[a].get("civic_body_id") == cb["id"]][:6],
        name=name, proc=proc, model=model, model_versions=model_versions, nodes=nodes, cons=cons, props=props, dec=dec,
        run=run_, base_versions=base_versions, commitment=T("commitment")[0], actual=T("actual")[0], env=env,
        refusals=refusals, escalations=escalations, resolved=resolved, replay=eng.q_replay(dec["id"]),
        results=S.RESULTS, events=eng.events, chain_head=eng.events[-1]["hash"], NODES=S.NODES)


# ------------------------------------------------------------------ page shell
NAV = [("index.html", "Walkthrough"), ("verify.html", "Check the record"), ("built.html", "What's built"),
       ("about.html", "About")]


def page(fname, title, body, contact, chain_head, event_count):
    nav = "".join(f'<a href="{h}"{" aria-current=page" if h == fname else ""}>{E(t)}</a>' for h, t in NAV)
    foot_contact = f' Contact: <a href="mailto:{E(contact)}">{E(contact)}</a>.' if contact else ""
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title><meta name="description" content="ACECOG public beta: a synthetic community's decisions, made on the real engine and open to checking.">
<link rel="stylesheet" href="style.css"></head>
<body data-expected-head="{chain_head}" data-expected-count="{event_count}"><a class="skip" href="#main">Skip to content</a>
<header class="top"><a class="mark" href="index.html">ACECOG</a><nav aria-label="Site">{nav}</nav></header>
<p class="status" role="note">Public beta. Riverbend Commons is a fictional community, and nothing on this site has legal effect.</p>
<main id="main">{body}</main>
<footer><p>ACECOG {E(SPEC_VERSION.split()[-1])} specification, engine API {E(API_VERSION)}. Read-only demonstration: no accounts,
no application analytics or cookies; hosting requests may be logged.{foot_contact}</p></footer>
<script src="verify.js" defer></script></body></html>
"""


# ------------------------------------------------------------------ pages
def index(d):
    dec, run_, nodes, cons = d["dec"], d["run"], d["nodes"], d["cons"]
    t = dec["tally"]
    pa, pb = d["props"]["proposition-0001"], d["props"]["proposition-0002"]
    minority = next((m["text"] for m in dec["minority_positions"] if "text" in m), "")
    alloc = run_["solution"]["allocations"]
    rows = "".join(
        f"<tr><td>{E(nodes[k]['name'])}</td><td class=num>{money(nodes[k]['cost'])}</td><td class=num>{money(v)}</td>"
        f"<td class=num>{v / nodes[k]['cost']:.0%}</td></tr>" for k, v in alloc.items())
    binding = [cons[b]["name"] if b in cons else "The budget" for b in run_["solution"]["binding_constraints"]]
    b0, b1 = d["base_versions"][:2]
    moved = [k for k in b0["allocations"] if b0["allocations"][k] != b1["allocations"][k]]
    reb_from = next(k for k in moved if b1["allocations"][k] < b0["allocations"][k])
    reb_to = next(k for k in moved if k != reb_from)
    act, com = d["actual"], d["commitment"]
    relaxed = next(c for c in d["model_versions"][-1]["constraints"] if c.get("previous_limit") is not None)
    classes = "".join(f"<li><b>{E(c['name'].replace('_', ' ').capitalize())}</b>: {E(c['method'].replace('_', ' '))}, "
                      f"{c['approval_threshold']:.0%} to pass, {c['quorum']:.0%} must take part</li>"
                      for c in d["proc"]["decision_classes"])
    ref = {}
    for ev in d["refusals"]:
        ref.setdefault(ev["data"]["refusal"]["code"], ev)

    def said_no(code):
        ev = ref[code]
        return (f'<p class="refused"><span>Refused</span> {E(ev["data"]["refusal"]["reason"].capitalize())}. '
                f'<a href="verify.html#e{ev["seq"]}">Record {ev["seq"]}</a></p>')

    def step(title, body):
        return f"<li><h3>{E(title)}</h3>{body}</li>"

    steps = [
        step("Riverbend writes its rules", f"<p>{E(d['cb']['name'])} has {len(d['members'])} founding members: "
             f"{E(', '.join(d['members']))}. Before anything is decided, they adopt the rules for each kind of decision.</p>"
             f"<ul class=plain>{classes}</ul>{said_no('PARTICIPATION_FEE')}"),
        step("Two plans compete", f"<p><b>{E(pa['title'])}</b> and <b>{E(pb['title'])}</b> go to the members. Plan A is "
             "amended during debate. The amendment becomes a new version, and the original stays on the record.</p>"),
        step("The debate happens in public", "<p>Under the state open-meetings rule the members adopted, private "
             "member-to-member threads are blocked. Eli owns property next to the trail project, declares it, and "
             f"sits out the vote.</p>{said_no('OPEN_MEETING_GUARD')}{said_no('RECUSED')}"),
        step("The members vote", f"<p>{t['participating']} of {t['eligible']} members take part: "
             f"{t['choices'].get('yes', 0)} yes, {t['choices'].get('no', 0)} no. Plan A passes and Plan B fails. The minority "
             f"view stays attached to the decision:</p><blockquote>{E(minority)}</blockquote>"
             f"<p>The decision is labelled <b>{E(dec['lifecycle_state'])}</b> and <b>{E(dec['legal_status']['value'])}</b>: "
             "no law has given this body's decisions legal effect, so the label says so.</p>"),
        step("The solver proposes an allocation", f"<p>With a {money(d['model']['budget'])} budget, a watershed limit and "
             f"limited crew time, the solver finds the best feasible mix. What's holding it back: "
             f"{E(', '.join(b[0].lower() + b[1:] for b in binding))}.</p><div class=scroll role=region aria-label='Allocation table' tabindex=0><table><caption>Allocation from run {E(run_['id'])}"
             "</caption><thead><tr><th scope=col>Initiative</th><th scope=col class=num>Full cost</th>"
             f"<th scope=col class=num>Allocated</th><th scope=col class=num>Funded</th></tr></thead><tbody>{rows}"
             f"</tbody></table></div><p>It also reports a near-optimal alternative without "
             f"{E(nodes[run_['alternative']['excluded']]['name'].lower())}, so people can see what that choice costs. "
             "The solver advises. It can't commit anything.</p>"),
        step("The plan is frozen and funded", f"<p>The approved result becomes the baseline, and {money(com['amount'])} "
             f"is reserved against it. Trying to reserve it twice fails.</p>{said_no('DOUBLE_ALLOCATION')}"),
        step("Reality arrives", f"<p>{E(nodes[act['node_id']]['name'])} costs {money(act['actual_cost'])}, "
             f"{money(act['variance'])} over plan. The actual is recorded beside the baseline, never over it.</p>"
             f"{said_no('BASELINE_IMMUTABLE')}"),
        step("A small change, inside the rules", f"<p>{E(d['name'](d['env']['authorized_resolver']))} may move up to "
             f"{money(d['env']['tolerance'])} on his own, under limits the members set. He moves "
             f"{money(b1['allocations'][reb_to] - b0['allocations'][reb_to])} from "
             f"{E(nodes[reb_from]['name'])} to {E(nodes[reb_to]['name'])}, and it's recorded as baseline "
             f"version 2.</p>"),
        step("A big change goes back to the members", f"<p>A move that would breach the {E(cons['eco-water-ceiling']['name'][0].lower() + cons['eco-water-ceiling']['name'][1:])} "
             "isn't his to make. It becomes an exception the members must decide. They approve a smaller move instead "
             "(baseline version 3). When they later choose to raise the limit itself, the decision has to say so, and "
             f"the new limit is recorded with the old one: {relaxed['previous_limit']} becomes {relaxed['limit']} "
             f"(baseline version 4).</p>{said_no('HARD_CONSTRAINT')}"),
        step("Anyone can replay the decision", f"<p>Re-running the solver from the decision's recorded inputs gives "
             f"the same result, hash for hash.</p><p class=hash>Original <code>{E(d['replay']['original_result_hash'])}"
             f"</code><br>Replayed <code>{E(d['replay']['replayed_result_hash'])}</code></p>"),
        step("The community can leave with everything", "<p>The whole record exports as one package. A fresh copy of "
             "the engine loads it, checks every link in the chain, and replays to the same outcomes. A tampered "
             "package is caught.</p>"),
    ]
    n = len(d["events"])
    return f"""
<section class=hero aria-labelledby=h1>
<h1 id=h1>Every decision here can be checked.</h1>
<p class=lede>ACECOG is open civic software for communities that decide together. This page runs on the real engine.
A fictional town, Riverbend Commons, made the decisions below, and your browser is checking its record right now.</p>
<div class=chain data-chain aria-live=polite>
<div class=squares aria-hidden=true></div>
<p class=chain-status>This page checks {n} records with your browser. It needs JavaScript; the
<a href="events.json">raw record</a> works without it.</p>
</div>
<p><a class=button href="verify.html">See how the check works</a></p>
</section>
<section aria-labelledby=walk><h2 id=walk>How Riverbend decided its budget</h2>
<ol class=steps>{''.join(steps)}</ol></section>
<section aria-labelledby=no><h2 id=no>Where the engine said no</h2>
<p>{len(d['refusals'])} attempts in this record were refused, each with its reason. They include the engine's own
self-tests: people trying to grant themselves power, skip a vote, or rewrite a baseline. All of them are listed on
<a href="verify.html#refusals">the record page</a>.</p></section>
"""


def verify(d):
    rows = "".join(f'<tr id="e{ev["seq"]}"><td class=num>{ev["seq"]}</td><td>{E(ev["data"]["command"])}</td>'
                   f'<td>{E(ev["data"]["refusal"]["code"])}</td><td>{E(ev["data"]["refusal"]["reason"])}</td></tr>'
                   for ev in d["refusals"])
    return f"""
<h1>Check the record yourself</h1>
<p class=lede>Every action in Riverbend is an event. Each event carries a fingerprint (a SHA-256 hash) of itself and of
the event before it, so changing any past event breaks every fingerprint after it. Your browser recomputes all of them
below after downloading the record. Verification results stay in your browser; ordinary hosting requests still occur.</p>
<div class=chain data-chain data-full aria-live=polite>
<div class=squares aria-hidden=true></div>
<p class=chain-status>Checking needs JavaScript. You can also download <a href="events.json">the record</a> and check it
with any SHA-256 tool: each hash is SHA-256 of the previous hash followed by the event's exact text.</p>
</div>
<p><button type=button class=button data-tamper hidden>Change one old record and check again</button></p>
<h2 id=refusals>Every refusal in the record</h2>
<p>{len(d['refusals'])} refused commands, as the engine recorded them. Refusals are kept, not hidden.</p>
<div class=scroll role=region aria-label='Refusal evidence table' tabindex=0><table><thead><tr><th scope=col class=num>Record</th><th scope=col>Command</th>
<th scope=col>Rule</th><th scope=col>Reason given</th></tr></thead><tbody>{rows}</tbody></table></div>
"""


def built(d, matrix_rows):
    passed = sum(1 for r in d["results"] if r[2])
    checks = "".join(f"<tr><td>{E(t)}</td><td>{E(title)}</td><td>{'Passed' if ok else 'Failed'}</td></tr>"
                     for t, title, ok, _ in d["results"])
    caps = "".join(f"<tr><td><code>{E(r['capability'])}</code></td><td>{E(r['summary'])}</td><td>{E(r['status'])}</td>"
                   f"<td>{E(EXPOSE.get(r['exposure'], r['exposure']))}</td></tr>" for r in matrix_rows)
    return f"""
<h1>What's built, and what isn't yet</h1>
<p class=lede>This beta shows only what the engine actually does. It has {len(COMMANDS)} commands and {len(QUERIES)}
views, and it checks itself against the specification on every change. This build passed {passed} of
{len(d['results'])} checks.</p>
<h2>What visitors can do, and when</h2>
<div class=scroll role=region aria-label='Capability table' tabindex=0><table><thead><tr><th scope=col>Capability</th><th scope=col>What it does</th>
<th scope=col>Status</th><th scope=col>In this beta</th></tr></thead><tbody>{caps}</tbody></table></div>
<h2>The checks this build passed</h2>
<div class=scroll role=region aria-label='Acceptance checks table' tabindex=0><table><thead><tr><th scope=col>Test</th><th scope=col>What it checks</th><th scope=col>Result</th>
</tr></thead><tbody>{checks}</tbody></table></div>
"""


EXPOSE = {"P-1": "Shown in this walkthrough", "P-2": "Shown here; hands-on in the interactive beta",
          "P-3": "Later", "Eval": "Evaluators only", "Off": "Never public: shown read-only"}


def about():
    # Q-31 founder-approved Public copy only. No internal notes.
    # W+M outer-page host facts are subject to a separate privacy amendment.
    return """
<h1>About this demonstration</h1>
<p class=lede><strong>Accelerated Ecological Governance (ACECOG)</strong> is developing software to help communities
make and explain decisions under rules they adopt. This beta is a read-only demonstration of the fictional
Riverbend Commons community, generated by the ACECOG engine.</p>
<p>All people, decisions and amounts in the example are synthetic. Results are Advisory and have no legal effect.
This is not a government service, a way to cast an official vote, or legal or financial advice. The software is
under development and may contain errors.</p>
<p>You can explore the example and check its record. The record checker detects inconsistent or incomplete event
data by comparing it with the expected fingerprint in the page. It cannot authenticate a site whose pages and
fingerprints have all been replaced. No visitor can change civic state through this demonstration.</p>
<h2>Your privacy</h2>
<p>This demonstration has no application accounts, submission forms, analytics, advertising or application cookies.
Fonts and example records are served with the site. The record check runs in your browser; its result is not
uploaded.</p>
<p>The site is hosted on GitHub Pages. Loading pages, fonts and example records sends ordinary web requests to
GitHub. GitHub states that it logs and stores visitors' IP addresses for security, whether or not they are signed
in. GitHub's handling and retention are described in its
<a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement"
target="_blank" rel="noopener noreferrer">Privacy Statement</a>. We do not promise a fixed deletion period for
GitHub's security logs.</p>
<p>Please do not send personal or confidential civic records through this demonstration. For a question,
accessibility issue, suspected security problem or correction, contact
<a href="mailto:morgan@acecog.org">morgan@acecog.org</a>. If you email us, your message and contact details
are used to respond and handle the issue. Avoid sending passwords or other secrets by email.</p>
"""


def build(contact=None, domain=None):
    eng, S = run()
    d = collect(eng, S)
    sys.path.insert(0, os.path.join(ROOT, "scripts"))
    import csv
    with open(os.path.join(ROOT, "docs", "capabilities", "capability-matrix.csv"), encoding="utf-8") as f:
        matrix_rows = list(csv.DictReader(f))
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    pages = {"index.html": ("ACECOG public beta: Riverbend Commons", index(d)),
             "verify.html": ("Check the record: ACECOG", verify(d)),
             "built.html": ("What's built: ACECOG", built(d, matrix_rows)),
             "about.html": ("About: ACECOG", about())}
    for fname, (title, body) in pages.items():
        with open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
            f.write(page(fname, title, body, contact, d["chain_head"], len(d["events"])))
    # The record: each event's exact hashed text, so any SHA-256 tool can re-check it.
    record = {"event_count": len(d["events"]), "chain_head": d["chain_head"], "rule": "hash = sha256(prev_hash + text)", "events": [
        {"seq": ev["seq"], "type": ev["type"], "hash": ev["hash"],
         "text": canon({k: v for k, v in ev.items() if k != "hash"})} for ev in d["events"]]}
    with open(os.path.join(OUT, "events.json"), "w", encoding="utf-8") as f:
        json.dump(record, f, separators=(",", ":"))
    for name in ("style.css", "verify.js"):
        shutil.copy(os.path.join(ASSETS, name), OUT)
    fonts = os.path.join(ASSETS, "fonts")
    if os.path.isdir(fonts):
        shutil.copytree(fonts, os.path.join(OUT, "fonts"))
    if domain:
        open(os.path.join(OUT, "CNAME"), "w").write(domain + "\n")
    open(os.path.join(OUT, ".nojekyll"), "w").close()
    return d


if __name__ == "__main__":
    d = build(os.environ.get("SITE_CONTACT"), os.environ.get("SITE_DOMAIN"))
    print(f"wrote {os.path.relpath(OUT, ROOT)}: {len(d['events'])} events, chain head {d['chain_head'][:12]}…")
    if not os.environ.get("SITE_CONTACT"):
        print("note: SITE_CONTACT not set; the public contact line is omitted (beta gate BG-1 needs one)")
