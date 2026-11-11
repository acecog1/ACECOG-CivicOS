"""BG-2 staging gateway negative/security and real-engine smoke tests.

Automated checks provide development evidence, NOT independent BG-2 release QA.
"""
from __future__ import annotations

from io import BytesIO
import json
from pathlib import Path
import time

import pytest

from scripts import bg2_prepare_assets as assets
from scripts import bg2_wsgi as gateway


@pytest.fixture(autouse=True)
def isolate(monkeypatch, tmp_path):
    monkeypatch.setenv("BG2_PUBLIC_HOST", "sandbox.example.org")
    monkeypatch.setenv("BG2_SIGNING_KEY", "test-only-key-012345678901234567890123456789")
    monkeypatch.setenv("BG2_MODE", "staging")
    target = tmp_path / "public-assets"
    assets.make_assets(target)
    monkeypatch.setattr(gateway, "ASSETS", target)
    with gateway.rate_lock:
        gateway.recent_requests.clear()


def request(method="GET", path="/", data=b"", **headers):
    e = {
        "REQUEST_METHOD": method,
        "PATH_INFO": path,
        "QUERY_STRING": "",
        "HTTP_HOST": "sandbox.example.org",
        "HTTP_ORIGIN": "https://sandbox.example.org",
        "CONTENT_LENGTH": str(len(data)),
        "CONTENT_TYPE": "application/json",
        "wsgi.input": BytesIO(data),
    }
    e.update(headers)
    seen = {}

    def start(status, response_headers):
        seen["status"] = int(status.split()[0])
        seen["headers"] = dict(response_headers)

    seen["body"] = b"".join(gateway.app(e, start))
    return seen


def get_token():
    result = request(path="/api/config")
    assert result["status"] == 200
    return json.loads(result["body"])["token"]


def test_configuration_fail_closed_and_health(monkeypatch):
    assert request(path="/healthz")["status"] == 200
    monkeypatch.delenv("BG2_SIGNING_KEY")
    assert request(path="/healthz")["status"] == 503
    assert request(path="/api/config")["status"] == 503
    monkeypatch.setenv("BG2_SIGNING_KEY", "test-only-key-012345678901234567890123456789")
    monkeypatch.setenv("BG2_PUBLIC_HOST", "*")
    assert request(path="/api/config")["status"] == 503
    monkeypatch.delenv("BG2_PUBLIC_HOST")
    monkeypatch.setenv("RENDER_EXTERNAL_HOSTNAME", "sandbox.example.org")
    assert request(path="/api/config")["status"] == 200
    monkeypatch.delenv("RENDER_EXTERNAL_HOSTNAME")


def test_hosted_assets_and_browser_safety_headers():
    page = request(path="/")
    assert page["status"] == 200
    content = page["body"].decode()
    assert "Synthetic demonstration only" in content
    assert "A bounded hosted worker process" in content
    assert "Development preview only." not in content
    assert "not an official civic service" in content
    assert page["headers"]["X-Frame-Options"] == "DENY"
    assert "frame-ancestors 'none'" in page["headers"]["Content-Security-Policy"]
    assert "Access-Control-Allow-Origin" not in page["headers"]
    assert "Set-Cookie" not in page["headers"]
    assert request(path="/experience.js")["status"] == 200
    assert request(path="/lab.js")["status"] == 200
    assert request(path="/lab.css")["status"] == 200
    assert request(path="/unknown")["status"] == 404


def test_exact_host_origin_and_signed_token():
    assert request(path="/api/config", HTTP_HOST="somewhere.invalid")["status"] == 403
    token = get_token()
    assert gateway.token_ok(token)
    assert not gateway.token_ok(token + "0")
    assert not gateway.token_ok(gateway.sign_token(int(time.time()) - 2000))
    params = json.dumps(gateway.lab.parameters()).encode()
    assert request("POST", "/api/compare", params, HTTP_ORIGIN="https://malicious.example.org",
                   HTTP_X_LAB_TOKEN=token)["status"] == 403
    assert request("POST", "/api/compare", params, HTTP_X_LAB_TOKEN="wrong")["status"] == 403


def test_input_hard_limits_and_recusal():
    token = get_token()
    bad = json.dumps({"budget": 10}).encode()
    assert request("POST", "/api/compare", bad, HTTP_X_LAB_TOKEN=token)["status"] == 400
    recused = json.dumps({"votes": {"eli": "yes"}}).encode()
    assert request("POST", "/api/compare", recused, HTTP_X_LAB_TOKEN=token)["status"] == 400
    oversized = request("POST", "/api/compare", b"z" * 5000, HTTP_X_LAB_TOKEN=token)
    assert oversized["status"] == 413
    assert request("PUT", "/api/compare")["status"] == 405


def test_rate_ceiling_is_bounded_not_claimed_as_full_abuse_solution():
    for _ in range(gateway.WINDOW_REQUESTS):
        assert gateway.rate_ok()
    assert not gateway.rate_ok()


def test_real_engine_vote_flip_through_one_shot_worker():
    p = gateway.lab.parameters(votes={"cara": "no", "dev": "no"})
    result = gateway.compare_worker(p)
    assert result["reference"]["decision"]["result"] == "approved"
    assert result["alternative"]["decision"]["result"] == "rejected"
    assert result["alternative"]["optimization"] is None
    assert result["alternative"]["synthetic_commitment_created"] is False
    assert result["alternative"]["baseline_created"] is False


def test_wsgi_successful_approved_response_without_persistence():
    p = gateway.lab.parameters(budget=700000, water=14)
    token = get_token()
    res = request("POST", "/api/compare", json.dumps(p).encode(), HTTP_X_LAB_TOKEN=token)
    assert res["status"] == 200, res["body"][:200]
    out = json.loads(res["body"])
    assert out["alternative"]["inputs"]["budget"] == 700000
    assert out["alternative"]["inputs"]["water"] == 14
    assert out["alternative"]["chain_head"]
    assert out["reference"]["chain_head"]
    assert "Set-Cookie" not in res["headers"]

def test_timeout_returns_504_and_releases_compute_gate(monkeypatch):
    import subprocess

    def slow(_):
        raise subprocess.TimeoutExpired(cmd="synthetic-worker", timeout=12)

    monkeypatch.setattr(gateway, "compare_worker", slow)
    token = get_token()
    body = json.dumps(gateway.lab.parameters()).encode()
    out = request("POST", "/api/compare", body, HTTP_X_LAB_TOKEN=token)
    assert out["status"] == 504
    # The semaphore must be released so the next visitor is not blocked forever.
    assert gateway.inflight.acquire(blocking=False)
    gateway.inflight.release()
