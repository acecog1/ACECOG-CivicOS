"""Build-time-only Pyodide vendor copier; browser runtime loads from SAME origin.

The upstream runtime is version-pinned, but the upstream root lock SHA still
requires independent verification and acceptance before public release.
No CDN use is allowed from browser JS, and no silent external fallback.
"""
from __future__ import annotations

import hashlib
import json
import argparse
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
CORE_ROOT_ASSETS = ROOT_ASSETS[:-1]
PINSET_SCHEMA = "ACECOG-PYODIDE-CORE-PINSET-v1"
PACKAGE_ROOTS = ("numpy", "scipy", "jsonschema")
MAX_DOWNLOAD = 80 * 1024 * 1024  # bound every upstream response
MAX_TOTAL = 240 * 1024 * 1024   # staging safety ceiling


def verify_digest(name: str, actual: str, expected: str) -> None:
    if not re.fullmatch(r"[a-f0-9]{64}", expected) or actual != expected:
        raise RuntimeError(f"Upstream asset SHA-256 mismatch: {name}")


def load_root_pinset(path: Path) -> dict[str,str]:
    # Only a separately reviewed fixed hash list can permit strict release.
    # Never compute expected values from the just-downloaded candidate.
    doc = json.loads(path.read_text(encoding="utf-8"))
    if doc.get("schema") != PINSET_SCHEMA or doc.get("pyodide_version") != VERSION:
        raise RuntimeError("Unapproved Pyodide version or pinset schema")
    if doc.get("root_lock_sha256") != PINNED_LOCK_SHA256:
        raise RuntimeError("Core pinset package-lock reference mismatch")
    assets = doc.get("sha256")
    if not isinstance(assets, dict) or set(assets) != set(CORE_ROOT_ASSETS):
        raise RuntimeError("Core pinset requires all four root asset SHA-256 values")
    if not all(isinstance(v, str) and re.fullmatch(r"[a-f0-9]{64}", v) for v in assets.values()):
        raise RuntimeError("Invalid core root SHA-256 pin")
    return assets


def download(name: str, destination: Path, expected_sha: str | None = None) -> str:
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
    observed = hashlib.sha256(data).hexdigest()
    if expected_sha is not None:
        verify_digest(name, observed, expected_sha)
    destination.parent.mkdir(parents=True,exist_ok=True)
    destination.write_bytes(data)
    return observed


def normalized(name: str) -> str:
    return re.split(r"[<>=!; \[]", name.strip(), maxsplit=1)[0].lower().replace("_","-")


def vendor(dest: Path = DEST, core_pinset: Path | None = None) -> dict:
    # Feasibility mode inventories observed hashes but cannot authorize release.
    expected = load_root_pinset(core_pinset) if core_pinset is not None else None
    dest.mkdir(parents=True,exist_ok=True)
    observed = {
        "pyodide-lock.json": download(
            "pyodide-lock.json",dest/"pyodide-lock.json",PINNED_LOCK_SHA256)
    }
    for name in CORE_ROOT_ASSETS:
        observed[name] = download(name,dest/name,expected[name] if expected else None)
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
        digest = download(file_name,dest/file_name,expected_sha.lower())
        observed[file_name] = digest
        total += (dest/file_name).stat().st_size
        if total > MAX_TOTAL:
            raise RuntimeError("Vendor output larger than staging cap")
    manifest = {
        "distribution":"Pyodide",
        "version":VERSION,
        "build_source":"version-pinned upstream CDN downloaded only during controlled build",
        "root_lock_sha256":observed["pyodide-lock.json"],
        "lock_sha_status":"PINNED_SHA256_VERIFIED_BEFORE_DISK_WRITE",
        "core_root_status":("EXACT_PINSET_VERIFIED_PENDING_INDEPENDENT_QA" if expected
                            else "UNPINNED_OBSERVED_ONLY_BLOCK_RELEASE"),
        "core_root_sha256":{n:observed[n] for n in CORE_ROOT_ASSETS},
        "core_pinset_independently_approved":"NOT_ASSERTED_BY_BUILDER",
        "license_review_status":"NOT_YET_INDEPENDENTLY_CERTIFIED",
        "package_lock_metadata":{name:{
            "package_file":packages[lookup[name]].get("file_name"),
            "depends":packages[lookup[name]].get("depends",[]),
            "license":packages[lookup[name]].get("license","NOT_DISCLOSED_IN_LOCK")
        } for name in sorted(selected)},
        "package_roots":list(PACKAGE_ROOTS),
        "packages":sorted(selected),
        "bytes":total,
        "files_sha256":observed
    }
    (dest/"acecog-runtime-manifest.json").write_text(json.dumps(manifest,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    return manifest


if __name__=="__main__":
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("--approved-root-pinset",type=Path,
                            help="Pre-reviewed SHA-256 pinset; absent means feasibility-only")
        args = parser.parse_args()
        info=vendor(core_pinset=args.approved_root_pinset)
        print(json.dumps({"version":info["version"],"bytes":info["bytes"],
                          "lock_sha256":info["root_lock_sha256"],
                          "core_root_status":info["core_root_status"],
                          "core_root_sha256":info["core_root_sha256"],
                          "packages":info["packages"]},sort_keys=True))
    except Exception as ex:
        print(f"Runtime vendor build failed ({type(ex).__name__}).",file=sys.stderr)
        raise SystemExit(1) from None
