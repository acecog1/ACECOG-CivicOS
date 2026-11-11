"""HTTP front for the ACECOG engine. Python standard library only.

    python scripts/run_server.py [--db PATH] [--port 8765]

POST /v0/commands/<name>   body: CommandEnvelope   -> CommandResult
GET  /v0/queries/...                               -> query result
GET  /openapi.yaml                                 -> the contract
"""
import json, os, re, sys, threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

from . import contract
from .engine import Engine, Refuse

ENGINE = None          # set by serve()
LOCK = threading.Lock()  # one writer at a time: transactions are serialized (8.1)
HERE = os.path.dirname(os.path.abspath(__file__))
OPENAPI = os.path.join(HERE, "..", "..", "docs", "api", "openapi.yaml")
STATUS = {"accepted": 200, "escalated": 202, "refused": 422}

ROUTES = [
    (r"^/v0/queries/civic-bodies/([^/]+)$", lambda e, m, q: {"civic_body": e.get(m[1], "civic_body"),
        "governance_process": (e.of_type("governance_process", m[1]) or [None])[0],
        "compliance_packs": e.of_type("compliance_pack", m[1]),
        "members": sorted(k for k, v in e.actors.items() if v["civic_body_id"] == m[1])}),
    (r"^/v0/queries/propositions/([^/]+)$", lambda e, m, q: {"versions": e.versions[e.get(m[1], "proposition")["id"]],
        "deliberation": [x for x in e.of_type("deliberation_post") if x["proposition_id"] == m[1]],
        "votes": [x for x in e.of_type("vote") if x["proposition_id"] == m[1]]}),
    (r"^/v0/queries/decisions/([^/]+)/provenance$", lambda e, m, q: e.q_provenance(m[1])),
    (r"^/v0/queries/decisions/([^/]+)/replay$", lambda e, m, q: e.q_replay(m[1])),
    (r"^/v0/queries/decisions/([^/]+)$", lambda e, m, q: e.q_decision(m[1])),
    (r"^/v0/queries/baselines/([^/]+)$", lambda e, m, q: {"versions": e.versions[e.get(m[1], "baseline")["id"]]}),
    (r"^/v0/queries/portfolio/([^/]+)$", lambda e, m, q: {"model": (e.of_type("portfolio_model", m[1]) or [None])[0],
        "baseline": e.current_baseline(m[1]), "commitments": e.of_type("commitment", m[1]), "actuals": e.of_type("actual", m[1])}),
    (r"^/v0/queries/exceptions/([^/]+)$", lambda e, m, q: {"exception_proposition": e.get(m[1], "exception_proposition")}),
    (r"^/v0/queries/delegations/([^/]+)$", lambda e, m, q: e.q_delegations(m[1])),
    (r"^/v0/queries/feed/([^/]+)$", lambda e, m, q: e.q_feed(m[1])),
    (r"^/v0/queries/events$", lambda e, m, q: e.q_events(int(q.get("after", ["0"])[0]))),
    (r"^/v0/queries/exports/([^/]+)$", lambda e, m, q: e._exports[m[1]]),
]


class Handler(BaseHTTPRequestHandler):
    def _send(self, code, body, ctype="application/json"):
        data = body if isinstance(body, bytes) else json.dumps(body, indent=2, default=str).encode()
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_POST(self):
        m = re.match(r"^/v0/commands/([a-z\-]+\.[a-z\-]+)$", urlparse(self.path).path)
        if not m or m[1] not in contract.COMMANDS:
            return self._send(404, {"error": "unknown command"})
        try:
            env = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))) or b"{}")
        except json.JSONDecodeError:
            return self._send(400, {"error": "body is not JSON"})
        try:
            with LOCK:
                res = ENGINE.execute(m[1], env)
        except Exception as e:  # an engine defect, never a governance outcome
            import traceback; traceback.print_exc()
            return self._send(500, {"error": f"engine error: {type(e).__name__}: {e}"})
        code = 400 if res["refusal"] and res["refusal"]["code"] == "SCHEMA" else STATUS[res["outcome"]]
        self._send(code, res)

    def do_GET(self):
        u = urlparse(self.path)
        if u.path == "/openapi.yaml":
            return self._send(200, open(OPENAPI, "rb").read(), "application/yaml")
        for pat, fn in ROUTES:
            m = re.match(pat, u.path)
            if m:
                try:
                    with LOCK:
                        body = fn(ENGINE, m, parse_qs(u.query))
                    return self._send(200, body)
                except (Refuse, KeyError) as r:
                    return self._send(404, getattr(r, "refusal", {"code": "NOT_FOUND", "reason": str(r)}))
        self._send(404, {"error": "unknown query"})

    def log_message(self, *a):
        pass


def serve(engine, port=8765, host="127.0.0.1"):
    """Bind an HTTP server to an engine. The engine is single-writer: requests are serialized."""
    global ENGINE
    ENGINE = engine
    return ThreadingHTTPServer((host, port), Handler)
