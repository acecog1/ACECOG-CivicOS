"""Build an audit-friendly static sovereign browser lab from exact CivicOS source.

No backend, dynamic script/eval, analytics or third-party browser dependencies.
This creates only the source bundle; a separately reviewed vendoring step provides
the pinned local WebAssembly runtime and wheels. Never publishes anything.
"""
from __future__ import annotations

import ast
import hashlib
import json
import os
import re
import subprocess
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "build" / "browser-lab"
PUBLIC = ROOT / "scripts" / "lab_preview_assets"
STATIC = ROOT / "scripts" / "browser_lab"

BROWSER_COPIES = {
    "Development preview only.": "Browser-only synthetic laboratory.",
    "This local application is not the public beta or an official civic service.":
        "This is a fictional, visitor-controlled simulation with no legal or municipal authority. It does not represent a real government; it is not a fork of BG-1's canonical 279-event history. Exported results are not independently authenticated institutional records.",
    "A local Python process runs": "Your browser runs",
    "Local development evidence only · No telemetry, real civic records or external API calls. No public sharing service.":
        "Browser-only civic laboratory · No simulation requests leave this device. Static hosting still receives ordinary page requests. No accounts, cookies, real civic records, or public sharing service.",
}
FILES = [
    ("src/acecog/__init__.py", "python/src/acecog/__init__.py"),
    ("src/acecog/engine.py", "python/src/acecog/engine.py"),
    ("src/acecog/contract.py", "python/src/acecog/contract.py"),
    ("scripts/experiment_riverbend.py", "python/scripts/experiment_riverbend.py"),
]


def find_named_node(tree: ast.Module, predicate, label: str):
    found = [node for node in tree.body if predicate(node)]
    if len(found) != 1:
        raise RuntimeError(f"Expected exactly one {label} in scenario source")
    return found[0]


def stripped_model() -> str:
    """Use the actual scenario model, without its HTTP-server/testing imports."""
    parsed = ast.parse((ROOT / "tests" / "scenario.py").read_text(encoding="utf-8"))
    nodes = find_named_node(
        parsed,
        lambda n: isinstance(n, ast.Assign) and any(
            isinstance(t, ast.Name) and t.id == "NODES" for t in n.targets
        ), "NODES assignment",
    )
    model = find_named_node(
        parsed,
        lambda n: isinstance(n, ast.FunctionDef) and n.name == "model",
        "model() function",
    )
    out = "'''Source-extracted synthetic Riverbend model, no HTTP server imports.'''\n"
    return out + ast.unparse(nodes) + "\n\n" + ast.unparse(model) + "\n"


def replace_one(content: str, old: str, new: str, file: str):
    if content.count(old) != 1:
        raise RuntimeError(f"Upstream UI changed; required exact marker count not one: {file}: {old[:60]!r}")
    return content.replace(old, new, 1)


def checked_out_source_revision() -> str:
    try:
        sha = subprocess.check_output(
            ["git", "rev-parse", "--verify", "HEAD"],
            cwd=ROOT, text=True, stderr=subprocess.DEVNULL, timeout=10,
        ).strip().lower()
    except (OSError, subprocess.SubprocessError):
        return "unrecorded-local-build"
    if not re.fullmatch(r"[0-9a-f]{40}", sha):
        raise RuntimeError("Git checkout has invalid source revision")
    return sha


def build(dest: Path = DEST) -> None:
    dest.mkdir(parents=True, exist_ok=True)
    html = (PUBLIC / "index.html").read_text(encoding="utf-8")
    for old, new in BROWSER_COPIES.items():
        html = replace_one(html, old, new, "index.html")
    html = replace_one(
        html, '<meta name="viewport" content="width=device-width,initial-scale=1">',
        '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
        '  <meta http-equiv="Content-Security-Policy" '
        'content="default-src \'self\'; connect-src \'self\'; '
        'script-src \'self\' \'wasm-unsafe-eval\'; worker-src \'self\'; '
        'style-src \'self\'; img-src \'self\'; object-src \'none\'; '
        'base-uri \'none\'; form-action \'none\'">',
        "index.html",
    )
    html = replace_one(html, 'href="/lab.css"', 'href="./lab.css"', "index.html")
    html = replace_one(html, 'src="/lab.js"', 'src="./lab.js"', "index.html")
    html = replace_one(html, 'src="/experience.js"', 'src="./experience.js"', "index.html")
    html = replace_one(
        html, '<script src="./lab.js" defer></script>',
        '<script src="./browser-api.js" defer></script>\n  <script src="./lab.js" defer></script>',
        "index.html",
    )
    html = replace_one(
        html, "<title>Riverbend Scenario Laboratory — Guided Local Preview</title>",
        "<title>Riverbend Scenario Laboratory — Browser-only Synthetic Lab</title>",
        "index.html",
    )
    html = replace_one(
        html, "<p class=\"subtle\">Select <strong>Run with CivicOS engine</strong> to compare the local reference fixture with your alternative.",
        "<p class=\"subtle\">Select <strong>Run with CivicOS engine</strong> to compare the embedded synthetic reference fixture with your alternative.",
        "index.html",
    )
    html = replace_one(
        html, '<footer class="container subtle">',
        '<footer class="container subtle">'
        '<a href="./third_party/THIRD_PARTY_NOTICES_CANDIDATE.txt">'
        'Third-party license source evidence (NOT YET APPROVED)</a> · ',
        "index.html",
    )
    (dest / "index.html").write_text(html, encoding="utf-8")
    js = (PUBLIC / "lab.js").read_text(encoding="utf-8")
    js = replace_one(
        js,
        "const response = await fetch(url, Object.assign({cache:\"no-store\"}, options || {}));",
        "const response = await window.AcecogBrowserLab.fetch(url, options || {});",
        "lab.js",
    )
    js = js.replace("Local engine unavailable:", "Browser engine unavailable:")
    (dest / "lab.js").write_text(js, encoding="utf-8")
    for name in ("lab.css", "experience.js"):
        shutil.copyfile(PUBLIC / name, dest / name)
    for name in ("browser-api.js", "browser-engine-worker.mjs"):
        shutil.copyfile(STATIC / name, dest / name)
    for src, target in FILES:
        to = dest / target
        to.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / src, to)
    target = dest / "python" / "tests" / "scenario.py"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(stripped_model(), encoding="utf-8")
    files = sorted(p for p in dest.rglob("*") if p.is_file() and "vendor/" not in str(p))
    manifest = {
        "schema": "ACECOG-browser-lab-source-v0.1",
        "mode": "synthetic-advisory-no-legal-effect",
        "scenario_kind": "abbreviated-isolated-synthetic-not-279-event-fork",
        # GitHub pull_request GITHUB_SHA may be a synthetic merge commit;
        # bind the manifest to actual checked-out HEAD, not the event SHA.
        "source_revision": checked_out_source_revision(),
        "runtime": "Pyodide version pinned by vendor manifest; solver output parity still needs proof",
        "files": {str(p.relative_to(dest)): hashlib.sha256(p.read_bytes()).hexdigest() for p in files},
    }
    (dest / "source-manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if any("https://cdn" in (dest / item).read_text(encoding="utf-8") for item in
           ("index.html", "lab.js", "browser-api.js", "browser-engine-worker.mjs")):
        raise RuntimeError("Browser executable must not request an external CDN")
    assert (dest / "python/tests/scenario.py").is_file()


if __name__ == "__main__":
    build()
