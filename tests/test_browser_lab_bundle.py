"""Static source-fidelity and negative-contract tests for browser-only CivicOS lab.

Passing these does NOT establish actual Pyodide/SciPy runtime parity, browser
performance, independent QA, or a public Pages deployment.
"""
from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path

from scripts import build_browser_lab as build


def test_model_extraction_excludes_http_and_preserves_reference_source(tmp_path):
    text = build.stripped_model()
    ast.parse(text)
    assert "from acecog import server" not in text
    assert "urllib" not in text
    ns = {}
    exec(compile(text, "<reviewed-scenario-extract>", "exec"), ns)  # trusted code from same repo
    import scenario as original
    for budget, water in ((900000,20),(600000,12),(1400000,36)):
        assert ns["model"](budget=budget,water=water) == original.model(budget=budget,water=water)


def test_static_bundle_is_self_hosted_and_source_pinned(tmp_path):
    target = tmp_path / "dist"
    build.build(target)
    html = (target/"index.html").read_text(encoding="utf-8")
    assert 'src="./browser-api.js"' in html
    assert 'src="./lab.js"' in html
    assert 'src="./experience.js"' in html
    assert "wasm-unsafe-eval" in html
    assert "worker-src 'self'" in html
    assert "connect-src 'self'" in html
    assert "without legal effect" in html.lower()
    for disclosure in ("visitor-controlled simulation", "no legal or municipal authority",
                       "not a fork of BG-1", "not independently authenticated institutional records"):
        assert disclosure in html
    assert not (target/"api").exists()
    code = (target/"lab.js").read_text(encoding="utf-8")
    assert "window.AcecogBrowserLab.fetch" in code
    assert "await fetch(url" not in code
    assert "new Worker(" in (target/"browser-api.js").read_text(encoding="utf-8")
    worker = (target/"browser-engine-worker.mjs").read_text(encoding="utf-8")
    assert '"./vendor/pyodide/"' in worker
    assert "lab.compare(" in worker
    assert "cdn.jsdelivr.net" not in worker
    assert "cloud" not in worker.lower()
    scenario = (target/"python/tests/scenario.py").read_text(encoding="utf-8")
    assert "def model(" in scenario
    assert "ThreadingHTTPServer" not in scenario
    assert "urllib" not in scenario
    manifest = json.loads((target/"source-manifest.json").read_text(encoding="utf-8"))
    assert manifest["scenario_kind"] == "abbreviated-isolated-synthetic-not-279-event-fork"
    for filename, digest in manifest["files"].items():
        assert hashlib.sha256((target/filename).read_bytes()).hexdigest() == digest


def test_no_browser_executable_runtime_external_host_references(tmp_path):
    target = tmp_path / "dist"
    build.build(target)
    for name in ["index.html","lab.js","experience.js","browser-api.js",
                 "browser-engine-worker.mjs"]:
        code=(target/name).read_text(encoding="utf-8")
        assert "https://cdn" not in code
        assert "http://cdn" not in code
        assert "render.com" not in code
    assert not (target/"vendor/pyodide").exists(), "Runtime vendoring must be a separate explicit build"


def test_generated_browser_lab_carries_manifest_bound_evidence_and_honest_scope(tmp_path):
    target = tmp_path / "dist"
    build.build(target)
    worker = (target / "browser-engine-worker.mjs").read_text(encoding="utf-8")
    experience = (target / "experience.js").read_text(encoding="utf-8")
    for field in ("source_revision", "source_manifest_sha256",
                  "runtime_manifest_sha256", "core_root_status",
                  "independently_authenticated"):
        assert field in worker
    assert "bundle-manifest" not in worker, "Placeholder SHA must never be exported"
    for field in ("raw_chain_events_included:false", "independent_verifier_included:false",
                  "user_generated_content_is_authentic:false", "source_checkout_revision",
                  "runtime_manifest_sha256", "source_manifest_sha256"):
        assert field in experience
    assert "Visitor-generated synthetic summaries are editable" in experience


def test_generated_browser_exposes_pending_legal_source_bundle_to_visitor(tmp_path):
    target=tmp_path/"dist"
    build.build(target)
    html=(target/"index.html").read_text(encoding="utf-8")
    assert 'href="./third_party/THIRD_PARTY_NOTICES_CANDIDATE.txt"' in html
    assert "Third-party license source evidence (NOT YET APPROVED)" in html
    assert "No legal or municipal authority" in html or "no legal or municipal authority" in html
