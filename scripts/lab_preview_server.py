"""Local-only browser UI for Riverbend counterfactual lab.

This development preview MUST NOT be deployed as a public backend. The server
binds exclusively to IPv4 loopback, has no persistence or third-party requests,
uses exact localhost Host/Origin checks and a process-local anti-CSRF token.
No CivicOS server.py routes or arbitrary commands are exposed.

    python scripts/lab_preview_server.py --port 8767
"""
from __future__ import annotations

import argparse
import hmac
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import secrets
import sys
from threading import BoundedSemaphore
from urllib.parse import parse_qs, urlsplit

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import experiment_riverbend as lab  # noqa: E402

ASSETS = HERE / "lab_preview_assets"
MAX_BODY = 4096
MAX_RESPONSE = 512 * 1024
CONCURRENT_RUNS = 2


def create_server(port: int = 8767) -> ThreadingHTTPServer:
    if type(port) is not int or not 0 <= port <= 65535:
        raise ValueError("Invalid local preview port")
    token = secrets.token_urlsafe(32)
    limit = BoundedSemaphore(CONCURRENT_RUNS)

    class Handler(BaseHTTPRequestHandler):
        def _origin(self) -> str:
            return "http://127.0.0.1:" + str(self.server.server_port)

        def _host_ok(self) -> bool:
            # Exact numeric localhost rejects common DNS-rebinding techniques.
            return self.headers.get("Host", "") == "127.0.0.1:" + str(self.server.server_port)

        def _headers(self, status: int, content_type: str, size: int) -> None:
            self.send_response(status)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(size))
            self.send_header("Cache-Control", "no-store")
            self.send_header("Referrer-Policy", "no-referrer")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.send_header("X-Frame-Options", "DENY")
            self.send_header("Content-Security-Policy",
                             "default-src 'none'; script-src 'self'; style-src 'self'; "
                             "connect-src 'self'; img-src 'self'; base-uri 'none'; "
                             "form-action 'none'; frame-ancestors 'none'")
            self.end_headers()

        def _send(self, status: int, body: object, ctype: str = "application/json; charset=utf-8") -> None:
            payload = (body if isinstance(body, bytes)
                       else json.dumps(body, ensure_ascii=False, allow_nan=False).encode("utf-8"))
            if len(payload) > MAX_RESPONSE:
                payload = b'{"error":"Response exceeded local preview limit"}'
                status = 503
            self._headers(status, ctype, len(payload))
            self.wfile.write(payload)

        def _reject_host(self) -> bool:
            if not self._host_ok():
                self._send(403, {"error": "Invalid localhost host"})
                return True
            return False

        def do_GET(self) -> None:
            if self._reject_host():
                return
            path = urlsplit(self.path)
            if path.path == "/api/config":
                self._send(200, {
                    "token": token,
                    "defaults": lab.parameters(),
                    "voters": list(lab.VOTERS),
                    "recused": lab.RECUSAL,
                    "constraints": {
                        "budget": [400000, 1400000],
                        "water": [5, 40],
                        "crew": [10, 50],
                        "appropriation": [250000, 850000],
                    },
                    "disclaimer": "Synthetic local preview, no legal effect or public deployment",
                })
                return
            if path.path == "/api/random":
                values = parse_qs(path.query, keep_blank_values=True)
                try:
                    if set(values) != {"seed"} or len(values["seed"]) != 1:
                        raise ValueError("A single seed is required")
                    number = int(values["seed"][0])
                    params = lab.surprise(number)
                except (ValueError, TypeError):
                    return self._send(400, {"error": "Seed must be an integer from 0 to 4294967295"})
                self._send(200, {"seed": number, "parameters": params})
                return
            assets = {"/": ("index.html", "text/html; charset=utf-8"),
                      "/lab.js": ("lab.js", "text/javascript; charset=utf-8"),
                      "/lab.css": ("lab.css", "text/css; charset=utf-8")}
            if path.path not in assets:
                return self._send(404, {"error": "Not found"})
            name, ctype = assets[path.path]
            self._send(200, (ASSETS / name).read_bytes(), ctype)

        def do_POST(self) -> None:
            if self._reject_host():
                return
            if urlsplit(self.path).path != "/api/compare":
                return self._send(404, {"error": "Not found"})
            if self.headers.get("Origin") != self._origin():
                return self._send(403, {"error": "Cross-origin requests are disabled"})
            if not hmac.compare_digest(self.headers.get("X-Lab-Token", ""), token):
                return self._send(403, {"error": "Invalid local session token"})
            if self.headers.get("Content-Type", "").split(";")[0].strip().lower() != "application/json":
                return self._send(415, {"error": "JSON required"})
            try:
                length = int(self.headers.get("Content-Length", "0"))
            except ValueError:
                return self._send(400, {"error": "Malformed length"})
            if not 1 <= length <= MAX_BODY:
                return self._send(413, {"error": "Payload length outside local preview limit"})
            try:
                body = json.loads(self.rfile.read(length))
                if not isinstance(body, dict):
                    raise ValueError("Expected object")
                allowed = {"budget", "water", "crew", "appropriation", "votes"}
                if set(body) - allowed:
                    raise ValueError("Unrecognized parameter")
                params = lab.parameters(**body)
            except (UnicodeDecodeError, json.JSONDecodeError, ValueError, TypeError):
                return self._send(400, {"error": "Invalid, unknown or out-of-range synthetic inputs"})
            if not limit.acquire(blocking=False):
                return self._send(429, {"error": "Local simulator is busy; try again"})
            try:
                result = lab.compare(params)
            except Exception:
                # Engine exceptions are not part of the civic narrative. Do not leak a
                # traceback or local file contents into the browser.
                return self._send(500, {"error": "Simulation failed; no result was published"})
            finally:
                limit.release()
            self._send(200, result)

        def log_message(self, fmt, *args) -> None:
            # Avoid collecting visitor input, tokens, query parameters or headers.
            return

    return ThreadingHTTPServer(("127.0.0.1", port), Handler)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8767)
    args = parser.parse_args()
    server = create_server(args.port)
    print("Local Riverbend lab: http://127.0.0.1:" + str(server.server_port))
    print("Local-only; not production; Ctrl-C to exit.", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
