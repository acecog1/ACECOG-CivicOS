"""BG-2 synthetic-only staging gateway (WSGI), NOT a general civic command API.

Served behind a TLS reverse proxy by a *single* gthread Gunicorn worker.
No accounts, cookies, persistent scenarios, real civic authority, private data,
arbitrary CivicOS routes, or cross-origin API access. Every compare runs in a
short-lived child process with a hard timeout. This is a production CANDIDATE
requiring independent security/a11y/privacy/abuse QA before public exposure.
"""
from __future__ import annotations

from collections import deque
import hashlib
import hmac
import json
import os
from pathlib import Path
import secrets
import subprocess
import sys
from threading import BoundedSemaphore, Lock
import time
from urllib.parse import parse_qs

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import experiment_riverbend as lab  # noqa: E402

ASSETS = HERE.parent / "build" / "bg2-assets"
WORKER = HERE / "bg2_compute_worker.py"
MAX_BODY = 4096
MAX_REPLY = 524288
WINDOW_SECONDS = 60.0
WINDOW_REQUESTS = 16
COMPUTE_TIMEOUT_SECONDS = 12
TOKEN_TTL_SECONDS = 900
rate_lock = Lock()
recent_requests = deque()
inflight = BoundedSemaphore(1)

ASSET_PATHS = {
    "/": ("index.html", "text/html; charset=utf-8"),
    "/lab.js": ("lab.js", "text/javascript; charset=utf-8"),
    "/lab.css": ("lab.css", "text/css; charset=utf-8"),
    "/experience.js": ("experience.js", "text/javascript; charset=utf-8"),
}

HEADERS = (
    ("Cache-Control", "no-store"),
    ("X-Content-Type-Options", "nosniff"),
    ("Referrer-Policy", "no-referrer"),
    ("X-Frame-Options", "DENY"),
    ("Cross-Origin-Resource-Policy", "same-origin"),
    ("Permissions-Policy", "camera=(), microphone=(), geolocation=()"),
    ("Strict-Transport-Security", "max-age=31536000"),
    ("Content-Security-Policy",
     "default-src 'none'; script-src 'self'; style-src 'self'; connect-src 'self'; "
     "img-src 'self'; object-src 'none'; base-uri 'none'; form-action 'none'; "
     "frame-ancestors 'none'"),
)
STATUS = {
    200: "OK", 400: "Bad Request", 403: "Forbidden", 404: "Not Found",
    405: "Method Not Allowed", 413: "Payload Too Large",
    415: "Unsupported Media Type", 429: "Too Many Requests",
    500: "Internal Server Error", 503: "Service Unavailable",
    504: "Gateway Timeout",
}


def configured() -> bool:
    host = os.environ.get("BG2_PUBLIC_HOST") or os.environ.get("RENDER_EXTERNAL_HOSTNAME", "")
    signing = os.environ.get("BG2_SIGNING_KEY", "")
    mode = os.environ.get("BG2_MODE", "staging")
    return (
        bool(host) and host == host.strip().lower()
        and ":" not in host and "/" not in host and "." in host
        and len(signing) >= 32
        and mode in {"staging", "public"}
    )


def sign_token(timestamp: int | None = None) -> str:
    now = int(time.time()) if timestamp is None else timestamp
    value = str(now) + "." + secrets.token_urlsafe(16)
    signature = hmac.new(
        os.environ["BG2_SIGNING_KEY"].encode("utf-8"),
        value.encode("ascii"), hashlib.sha256
    ).hexdigest()
    return value + "." + signature


def token_ok(token: str) -> bool:
    if len(token) > 256 or len(token) < 32:
        return False
    try:
        stamp, nonce, signature = token.split(".")
        created = int(stamp)
        if not nonce or not signature or len(signature) != 64:
            return False
        now = int(time.time())
        if created > now + 15 or created < now - TOKEN_TTL_SECONDS:
            return False
        prefix = stamp + "." + nonce
        expected = hmac.new(
            os.environ["BG2_SIGNING_KEY"].encode("utf-8"),
            prefix.encode("ascii"), hashlib.sha256
        ).hexdigest()
        return hmac.compare_digest(signature, expected)
    except (ValueError, UnicodeEncodeError):
        return False


def rate_ok() -> bool:
    """A conservative *global per-process* bound, not an IP-based abuse solution."""
    now = time.monotonic()
    with rate_lock:
        while recent_requests and recent_requests[0] < now - WINDOW_SECONDS:
            recent_requests.popleft()
        if len(recent_requests) >= WINDOW_REQUESTS:
            return False
        recent_requests.append(now)
        return True


def send(start_response, code: int, body: bytes, ctype: str = "application/json; charset=utf-8"):
    headers = [("Content-Type", ctype), ("Content-Length", str(len(body)))]
    headers.extend(HEADERS)
    start_response(str(code) + " " + STATUS[code], headers)
    return [body]


def message(start_response, code: int, msg: str):
    return send(start_response, code, json.dumps({"error": msg}).encode("utf-8"))


def json_reply(start_response, obj):
    raw = json.dumps(obj, ensure_ascii=False, allow_nan=False).encode("utf-8")
    if len(raw) > MAX_REPLY:
        return message(start_response, 503, "Result exceeds capacity")
    return send(start_response, 200, raw)


def compare_worker(params: dict):
    # No shell, no private signing key passed to the worker, no persistent state.
    env = {"PATH": os.environ.get("PATH", "/usr/bin"), "PYTHONNOUSERSITE": "1"}
    payload = json.dumps(params, allow_nan=False).encode("utf-8")
    completed = subprocess.run(
        [sys.executable, str(WORKER)],
        input=payload, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
        cwd=str(HERE.parent), env=env, check=False,
        timeout=COMPUTE_TIMEOUT_SECONDS
    )
    if completed.returncode != 0 or len(completed.stdout) > MAX_REPLY:
        raise RuntimeError("Worker failed or response too large")
    return json.loads(completed.stdout)


def app(environ, start_response):
    method = environ.get("REQUEST_METHOD", "")
    path = environ.get("PATH_INFO", "")
    if path == "/healthz":
        if method != "GET":
            return message(start_response, 405, "Method not allowed")
        if not configured() or not ASSETS.joinpath("index.html").is_file():
            return message(start_response, 503, "Not configured")
        return json_reply(start_response, {"status": "ready", "mode": os.environ.get("BG2_MODE", "staging")})
    if not configured():
        return message(start_response, 503, "Service not configured")
    host = os.environ.get("BG2_PUBLIC_HOST") or os.environ["RENDER_EXTERNAL_HOSTNAME"]
    if environ.get("HTTP_HOST") != host:
        return message(start_response, 403, "Invalid host")
    origin = "https://" + host
    if method == "GET":
        if path == "/api/config":
            return json_reply(start_response, {
                "token": sign_token(),
                "defaults": lab.parameters(),
                "voters": list(lab.VOTERS),
                "recused": lab.RECUSAL,
                "constraints": {"budget": [400000, 1400000], "water": [5, 40],
                                "crew": [10, 50], "appropriation": [250000, 850000]},
                "disclaimer": "Fictional / advisory / no legal effect. Hosting network metadata may be processed."
            })
        if path == "/api/random":
            query = parse_qs(environ.get("QUERY_STRING", ""), keep_blank_values=True)
            try:
                if set(query) != {"seed"} or len(query["seed"]) != 1:
                    raise ValueError("Seed required")
                number = int(query["seed"][0])
                sampled = lab.surprise(number)
            except (ValueError, TypeError):
                return message(start_response, 400, "Seed must be from 0 to 4294967295")
            return json_reply(start_response, {"seed": number, "parameters": sampled})
        if path in ASSET_PATHS:
            name, ctype = ASSET_PATHS[path]
            try:
                data = ASSETS.joinpath(name).read_bytes()
            except OSError:
                return message(start_response, 503, "Staged assets unavailable")
            return send(start_response, 200, data, ctype)
        return message(start_response, 404, "Not found")

    if method != "POST" or path != "/api/compare":
        return message(start_response, 405, "Method not allowed")
    if environ.get("HTTP_ORIGIN") != origin:
        return message(start_response, 403, "Invalid origin")
    if not token_ok(environ.get("HTTP_X_LAB_TOKEN", "")):
        return message(start_response, 403, "Invalid session token")
    if environ.get("CONTENT_TYPE", "").split(";")[0].strip().lower() != "application/json":
        return message(start_response, 415, "JSON required")
    try:
        size = int(environ.get("CONTENT_LENGTH", "0"))
    except (TypeError, ValueError):
        return message(start_response, 400, "Invalid length")
    if not 1 <= size <= MAX_BODY:
        return message(start_response, 413, "Payload too large")
    try:
        obj = json.loads(environ["wsgi.input"].read(size))
        if type(obj) is not dict or set(obj) - {"budget", "water", "crew", "appropriation", "votes"}:
            raise ValueError("Unknown inputs")
        params = lab.parameters(**obj)
    except (KeyError, ValueError, TypeError, json.JSONDecodeError, UnicodeDecodeError):
        return message(start_response, 400, "Invalid synthetic inputs")
    if not rate_ok():
        return message(start_response, 429, "Laboratory capacity reached")
    if not inflight.acquire(blocking=False):
        return message(start_response, 429, "Laboratory is busy")
    try:
        try:
            output = compare_worker(params)
        except subprocess.TimeoutExpired:
            return message(start_response, 504, "Simulation timed out")
        except (RuntimeError, ValueError, TypeError, json.JSONDecodeError):
            return message(start_response, 503, "Simulation unavailable")
        return json_reply(start_response, output)
    finally:
        inflight.release()
