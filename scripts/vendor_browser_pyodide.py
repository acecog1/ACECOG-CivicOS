"""Build-time-only Pyodide vendor copier; browser runtime loads from SAME origin.

The upstream runtime is version-pinned, but the upstream root lock SHA still
requires independent verification and acceptance before public release.
No CDN use is allowed from browser JS, and no silent external fallback.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import sys
import urllib.request

VERSION = "314.0.7"
PINNED_LOCK_SHA256 = "5dc2fc119108bc148c7457dc86e7675b5c87e1cafd420b9c34c1eaef7b36c010"
UPSTREAM = f"https://cdn.jsdelivr.net/pyodide/v{VERSION}/full/"
DEST = Path(__file__).resolve().parents[1] / "build" / "browser-lab" / "vendor" / "pyodide"
ROOT_ASSETS = (
    "pyodide.mjs", "pyodide.asm.mjs", "pyodide.asm.wasm",
    "python_stdlib.zip", "pyodide-lock.json",
)
PACKAGE_ROOTS = ("numpy", "scipy", "jsonschema")
MAX_DOWNLOAD = 80 * 1024 * 1024  # bound every upstream response
MAX_TOTAL = 240 * 1024 * 1024   # staging safety ceiling


def download(name: str, destination: Path) -> str:
    if not name or "/" in name or "\\" in name or name.startswith("."):
        raise ValueError("Unsafe upstream filename")
    req = urllib.request.Request(UPSTREAM + name, headers={"User-Agent":"ACECOG-Pyodide-vendor-PoC"})
    # nosec B310: req URL is a fixed HTTPS allowlist host plus validated filename;
    # redirects are checked against that same host and versioned path before use.
    with urllib.request.urlopen(req, timeout=60) as response:  # nosec B310
        from urllib.parse import urlsplit
        final = urlsplit(response.geturl())
        if (final.scheme != "https" or final.hostname != "cdn.jsdelivr.net"
                or final.path != f"/pyodide/v{VERSION}/full/{name}"):
            raise RuntimeError("Unexpected upstream redirect")
        data = response.read(MAX_DOWNLOAD + 1)
    if len(data) > MAX_DOWNLOAD:
        raise RuntimeError(f"Upstream asset oversized: {name}")
    destination.parent.mkdir(parents=True,exist_ok=True)
    destination.write_bytes(data)
    return hashlib.sha256(data).hexdigest()


def normalized(name: str) -> str:
    return re.split(r"[<>=!; \[]", name.strip(), maxsplit=1)[0].lower().replace("_","-")


def vendor(dest: Path = DEST) -> dict:
    dest.mkdir(parents=True,exist_ok=True)
    observed = {name: download(name,dest/name) for name in ROOT_ASSETS}
    if observed["pyodide-lock.json"] != PINNED_LOCK_SHA256:
        raise RuntimeError("Pinned Pyodide root package lock digest mismatch")
    lock = json.loads((dest/"pyodide-lock.json").read_text(encoding="utf-8"))
    packages = lock.get("packages")
    if not isinstance(packages,dict):
        raise RuntimeError("Unexpected Pyodide lock format")
    lookup = {normalized(n):n for n in packages}
    selected: set[str] = set()
    frontier = list(PACKAGE_ROOTS)
    while frontier:
        name = normalized(frontier.pop())
        if name in selected:
            continue
        if name not in lookup:
            raise RuntimeError(f"Missing Pyodide dependency in lock: {name}")
        selected.add(name)
        info = packages[lookup[name]]
        frontier.extend(info.get("depends",[]))
    total = sum((dest/k).stat().st_size for k in ROOT_ASSETS)
    for name in sorted(selected):
        entry = packages[lookup[name]]
        file_name = entry.get("file_name")
        expected_sha = entry.get("sha256")
        if not isinstance(file_name,str) or not isinstance(expected_sha,str):
            raise RuntimeError(f"Package metadata missing: {name}")
        digest = download(file_name,dest/file_name)
        if digest.lower()!=expected_sha.lower():
            raise RuntimeError(f"Pyodide package checksum mismatch: {name}")
        observed[file_name] = digest
        total += (dest/file_name).stat().st_size
        if total > MAX_TOTAL:
            raise RuntimeError("Vendor output larger than staging cap")
    manifest = {
        "distribution":"Pyodide",
        "version":VERSION,
        "build_source":"version-pinned upstream CDN downloaded only during controlled build",
        "root_lock_sha256":observed["pyodide-lock.json"],
        "lock_sha_status":"PINNED_DIGEST_OBSERVED_IN_FEASIBILITY_RUN_PENDING_INDEPENDENT_RELEASE_QA",
        "package_roots":list(PACKAGE_ROOTS),
        "packages":sorted(selected),
        "bytes":total,
        "files_sha256":observed
    }
    (dest/"acecog-runtime-manifest.json").write_text(json.dumps(manifest,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    return manifest


if __name__=="__main__":
    try:
        info=vendor()
        print(json.dumps({"version":info["version"],"bytes":info["bytes"],
                          "lock_sha256":info["root_lock_sha256"],
                          "packages":info["packages"]}))
    except Exception as ex:
        print(f"Runtime vendor build failed ({type(ex).__name__}).",file=sys.stderr)
        raise SystemExit(1) from None
