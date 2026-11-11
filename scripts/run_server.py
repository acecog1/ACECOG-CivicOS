"""Start a local ACECOG installation.

    python scripts/run_server.py                     # data in var/acecog.sqlite, port 8765
    python scripts/run_server.py --db my.sqlite --port 9000

Everything the system knows lives in that one file. Copy it to back it up.
"""
import argparse, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))
from acecog import server, contract
from acecog.engine import Engine

ap = argparse.ArgumentParser()
ap.add_argument("--db", default=os.path.join("var", "acecog.sqlite"))
ap.add_argument("--port", type=int, default=8765)
a = ap.parse_args()
os.makedirs(os.path.dirname(os.path.abspath(a.db)), exist_ok=True)
eng = Engine.open(a.db)
print(f"ACECOG MVP API {contract.API_VERSION} on http://127.0.0.1:{a.port}")
print(f"Data file: {os.path.abspath(a.db)} ({len(eng.events)} events loaded, hash chain verified)")
server.serve(eng, a.port).serve_forever()
