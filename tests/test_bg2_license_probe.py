"""Actual-wheel license inventory must be exact-source and fail closed."""
import hashlib
from pathlib import Path
from zipfile import ZipFile
import pytest
from scripts import bg2_license_probe as probe
from scripts import vendor_browser_pyodide as vendor


def _wheel(tmp_path, monkeypatch):
    folder=tmp_path/"vendor"
    folder.mkdir()
    wheel=folder/"fictional-1.2.3-py3-none-any.whl"
    with ZipFile(wheel,"w") as z:
        z.writestr("fictional-1.2.3.dist-info/METADATA",
                   "Metadata-Version: 2.4\nName: fictional\nVersion: 1.2.3\nLicense-Expression: MIT\n")
        z.writestr("fictional-1.2.3.dist-info/licenses/LICENSE","MIT original notice")
    digest=hashlib.sha256(wheel.read_bytes()).hexdigest()
    state={"files_sha256":{wheel.name:digest},
           "packages":["fictional"],
           "package_lock_metadata":{"fictional":{"package_file":wheel.name}},
           "core_root_status":"EXACT_PINSET_VERIFIED_PENDING_INDEPENDENT_QA"}
    monkeypatch.setattr(vendor,"verify_vendor_directory",lambda _folder:state)
    return folder,wheel,state


def test_exact_wheel_notice_contents_and_hold(tmp_path,monkeypatch):
    folder,wheel,state=_wheel(tmp_path,monkeypatch)
    out=probe.probe(folder)
    assert len(out["wheels"])==1
    assert out["release_licensing_acceptance"]=="HOLD"
    assert out["wheels"][0]["wheel_sha256"]==state["files_sha256"][wheel.name]
    assert out["wheels"][0]["license_expression_from_wheel"]=="MIT"
    notices=out["wheels"][0]["embedded_notice_files"]
    assert list(notices)==["fictional-1.2.3.dist-info/licenses/LICENSE"]
    assert notices[next(iter(notices))]["bytes"]==len("MIT original notice")
    assert notices[next(iter(notices))]["embedded_notice_utf8"]=="MIT original notice"
    assert "SciPy 1.18.0" in " ".join(out["source_of_truth_links"])


def test_changed_wheel_without_manifest_update_fails_closed(tmp_path,monkeypatch):
    folder,wheel,_state=_wheel(tmp_path,monkeypatch)
    wheel.write_bytes(b"changed")
    with pytest.raises(RuntimeError,match="changed after vendoring"):
        probe.probe(folder)


def test_empty_or_missing_dependency_set_rejected(tmp_path,monkeypatch):
    folder,wheel,state=_wheel(tmp_path,monkeypatch)
    state["packages"]=[]
    with pytest.raises(RuntimeError,match="Incomplete"):
        probe.probe(folder)
