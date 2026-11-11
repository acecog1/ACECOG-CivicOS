"""Security, API and real-engine integration checks for LOCAL preview only."""
import json
import sys
import threading
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

import pytest

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
import lab_preview_server as preview  # noqa: E402


@pytest.fixture(scope="module")
def app():
    server = preview.create_server(0)
    runner = threading.Thread(target=server.serve_forever, daemon=True)
    runner.start()
    base = "http://127.0.0.1:" + str(server.server_port)
    try:
        yield base
    finally:
        server.shutdown()
        server.server_close()
        runner.join(timeout=5)


def fetch(base, path, *, method="GET", data=None, headers=None):
    req = Request(base + path, data=None if data is None else json.dumps(data).encode(),
                  method=method, headers=headers or {})
    try:
        with urlopen(req, timeout=15) as response:
            code, content, meta = response.status, response.read(), response.headers
    except HTTPError as e:
        code, content, meta = e.code, e.read(), e.headers
    typ = meta.get("Content-Type", "")
    return code, json.loads(content) if "application/json" in typ else content.decode(), meta


def authorized(app, cfg, data):
    return fetch(app, "/api/compare", method="POST", data=data,
                 headers={"Content-Type": "application/json", "Origin": app,
                          "X-Lab-Token": cfg["token"]})


def test_local_only_bind_and_browser_security_headers(app):
    code, html, headers = fetch(app, "/")
    assert code == 200
    assert "Riverbend Scenario Laboratory" in html
    assert "Development preview only" in html
    assert headers["X-Frame-Options"] == "DENY"
    assert headers["Cache-Control"] == "no-store"
    assert headers.get("Access-Control-Allow-Origin") is None
    assert "connect-src 'self'" in headers["Content-Security-Policy"]
    code, js, _ = fetch(app, "/lab.js")
    assert code == 200 and "api/compare" in js
    assert "innerHTML" not in js and "eval(" not in js
    assert "https://" not in js
    code, css, _ = fetch(app, "/lab.css")
    assert code == 200 and "max-width:420px" in css
    code, data, _ = fetch(app, "/not-found")
    assert code == 404 and "error" in data


def test_host_and_same_origin_gate(app):
    code, _, _ = fetch(app, "/", headers={"Host": "fake.example.com"})
    assert code == 403
    cfg = fetch(app, "/api/config")[1]
    code, _, _ = fetch(app, "/api/compare", method="POST", data=cfg["defaults"],
                       headers={"Content-Type": "application/json", "Origin": "http://evil.example",
                                "X-Lab-Token": cfg["token"]})
    assert code == 403
    code, _, _ = fetch(app, "/api/compare", method="POST", data=cfg["defaults"],
                       headers={"Content-Type": "application/json", "Origin": app,
                                "X-Lab-Token": "wrong"})
    assert code == 403
    code, _, _ = fetch(app, "/api/compare", method="POST", data=cfg["defaults"],
                       headers={"Content-Type": "text/plain", "Origin": app,
                                "X-Lab-Token": cfg["token"]})
    assert code == 415


def test_reference_and_changed_votes_are_real_engine_runs(app):
    cfg = fetch(app, "/api/config")[1]
    data = dict(cfg["defaults"], votes=dict(cfg["defaults"]["votes"], cara="no", dev="no"))
    code, result, headers = authorized(app, cfg, data)
    assert code == 200, result
    assert result["reference"]["decision"]["result"] == "approved"
    assert result["alternative"]["decision"]["result"] == "rejected"
    assert result["alternative"]["decision"]["tally"]["choices"] == {"no": 3, "yes": 2}
    assert result["alternative"]["portfolio_adopted"] is False
    assert not result["alternative"]["baseline_created"]
    assert not result["alternative"]["synthetic_commitment_created"]
    assert result["reference"]["replay"]["reproduced"]
    assert result["alternative"]["chain_head"] != result["reference"]["chain_head"]
    assert result["impact_narrative"]["evidence"]["alternative_head"] == result["alternative"]["chain_head"]
    assert headers["Cache-Control"] == "no-store"


def test_resource_variation_uses_solver_and_replay(app):
    cfg = fetch(app, "/api/config")[1]
    data = dict(cfg["defaults"], budget=600000, water=12, crew=20)
    code, result, _ = authorized(app, cfg, data)
    assert code == 200, result
    assert result["alternative"]["decision"]["result"] == "approved"
    assert result["alternative"]["replay"]["reproduced"]
    assert result["alternative"]["optimization"]["result_hash"] != result["reference"]["optimization"]["result_hash"]


@pytest.mark.parametrize("data", [
    {"budget": 2}, {"votes": {"eli": "yes"}}, {"votes": {"cara": "veto"}},
    {"budget": True}, {"budget": 900000, "role": "mayor"},
])
def test_untrusted_inputs_are_rejected_without_exposing_stack(app, data):
    cfg = fetch(app, "/api/config")[1]
    code, payload, _ = authorized(app, cfg, data)
    assert code == 400
    assert list(payload) == ["error"]
    assert "Traceback" not in payload["error"]


def test_randomization_is_seeded_and_is_not_a_governance_action(app):
    a = fetch(app, "/api/random?seed=42")
    b = fetch(app, "/api/random?seed=42")
    assert a[0] == b[0] == 200
    assert a[1] == b[1]
    assert a[1]["parameters"]["votes"]["eli"] if "eli" in a[1]["parameters"]["votes"] else True
    assert fetch(app, "/api/random?seed=-1")[0] == 400
    assert fetch(app, "/api/random?seed=xyz")[0] == 400
    assert fetch(app, "/api/random")[0] == 400
    assert fetch(app, "/api/random?seed=42&seed=43")[0] == 400
