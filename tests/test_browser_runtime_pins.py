"""BG-2 core runtime digest checks. No network or accepted release pins."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pytest

from scripts import vendor_browser_pyodide as v


def test_core_pinset_requires_exact_asset_inventory_and_expected_version(tmp_path):
    example={k:hashlib.sha256(k.encode()).hexdigest() for k in v.CORE_ROOT_ASSETS}
    doc={"schema":v.PINSET_SCHEMA,"pyodide_version":v.VERSION,
         "root_lock_sha256":v.PINNED_LOCK_SHA256,"sha256":example}
    f=tmp_path/"pinset.json"
    f.write_text(json.dumps(doc))
    assert v.load_root_pinset(f)==example
    for field,value in [("pyodide_version","0.0.0"),
                        ("root_lock_sha256","0"*64),
                        ("schema","not-reviewed")]:
        bad={**doc,field:value}
        f.write_text(json.dumps(bad))
        with pytest.raises(RuntimeError):
            v.load_root_pinset(f)
    for invalid in [{**example,"unknown.mjs":"a"*64},
                    {k:val for k,val in example.items() if k!="pyodide.asm.wasm"},
                    {**example,"pyodide.asm.wasm":"from-current-download"}]:
        f.write_text(json.dumps({**doc,"sha256":invalid}))
        with pytest.raises(RuntimeError):
            v.load_root_pinset(f)


def test_sha256_mismatch_is_fail_closed():
    expected=hashlib.sha256(b"pre-reviewed-core-file").hexdigest()
    v.verify_digest("pyodide.mjs",expected,expected)
    with pytest.raises(RuntimeError,match="mismatch"):
        v.verify_digest("pyodide.mjs",hashlib.sha256(b"modified").hexdigest(),expected)
    with pytest.raises(RuntimeError,match="mismatch"):
        v.verify_digest("pyodide.mjs",expected,"INVALID_SHA")


def test_download_checks_digest_before_any_disk_write(tmp_path,monkeypatch):
    upstream=b"fixture only, not a Pyodide release"
    class Response:
        def geturl(self):
            return v.UPSTREAM+"pyodide.mjs"
        def read(self,size):
            return upstream
        def __enter__(self):
            return self
        def __exit__(self,*_args):
            return None
    monkeypatch.setattr(v.urllib.request,"urlopen",lambda *_a,**_kw: Response())
    target=tmp_path/"root"/"pyodide.mjs"
    with pytest.raises(RuntimeError,match="mismatch"):
        v.download("pyodide.mjs",target,"0"*64)
    assert not target.exists(), "No tampered download should be written"
    actual=hashlib.sha256(upstream).hexdigest()
    assert v.download("pyodide.mjs",target,actual)==actual
    assert target.read_bytes()==upstream


def test_upstream_path_rejects_unsafe_filename_and_redirect(tmp_path,monkeypatch):
    with pytest.raises(ValueError):
        v.download("../pyodide.mjs",tmp_path/"escape")
    class Redirect:
        def geturl(self):
            return "https://evil.example/pyodide.mjs"
        def read(self,size):
            return b"evil"
        def __enter__(self):
            return self
        def __exit__(self,*_args):
            return None
    monkeypatch.setattr(v.urllib.request,"urlopen",lambda *_a,**_kw: Redirect())
    with pytest.raises(RuntimeError,match="redirect"):
        v.download("pyodide.mjs",tmp_path/"target")
    assert not (tmp_path/"target").exists()


def test_manifest_maintains_nonrelease_flag_without_pinset():
    # This test asserts that a local feasibility build cannot quietly claim
    # an independently reviewed bundle simply because it has calculated hashes.
    source=Path(v.__file__).read_text()
    assert "UNPINNED_OBSERVED_ONLY_BLOCK_RELEASE" in source
    assert "NOT_YET_INDEPENDENTLY_CERTIFIED" in source
    assert "--approved-root-pinset" in source


def test_transient_upstream_error_retries_only_same_pinned_https_url(tmp_path,monkeypatch):
    from urllib.error import URLError
    payload=b"stable bytes"
    attempts=[]
    class Response:
        def geturl(self):
            return v.UPSTREAM+"pyodide.mjs"
        def read(self,limit):
            return payload
        def __enter__(self):
            return self
        def __exit__(self,*args):
            return None
    def retry(req,timeout):
        attempts.append(req.full_url)
        if len(attempts)<3:
            raise URLError("simulated transient network failure")
        return Response()
    monkeypatch.setattr(v.urllib.request,"urlopen",retry)
    monkeypatch.setattr(v.time,"sleep",lambda _: None)
    expected=hashlib.sha256(payload).hexdigest()
    dest=tmp_path/"pyodide.mjs"
    assert v.download("pyodide.mjs",dest,expected)==expected
    assert attempts==[v.UPSTREAM+"pyodide.mjs"]*3
    assert dest.read_bytes()==payload


def test_permanent_network_error_leaves_no_vendor_asset(tmp_path,monkeypatch):
    from urllib.error import URLError
    attempts=[]
    def fail(req,timeout):
        attempts.append(req.full_url)
        raise URLError("unavailable")
    monkeypatch.setattr(v.urllib.request,"urlopen",fail)
    monkeypatch.setattr(v.time,"sleep",lambda _: None)
    target=tmp_path/"pyodide.asm.wasm"
    with pytest.raises(RuntimeError,match="after bounded retries"):
        v.download("pyodide.asm.wasm",target,"a"*64)
    assert len(attempts)==3
    assert not target.exists()
