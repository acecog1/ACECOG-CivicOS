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


def test_pinned_review_packet_contains_exact_notice_sbom_and_fails_on_tamper(tmp_path,monkeypatch):
    import json
    from scripts import package_bg2_candidate as pack
    folder,wheel,state=_wheel(tmp_path,monkeypatch)
    state["root_lock_sha256"]=vendor.PINNED_LOCK_SHA256
    site=tmp_path/"site"
    (site/"vendor").mkdir(parents=True)
    # The actual vendor directory must live within this source-relative site.
    folder.rename(site/"vendor"/"pyodide")
    folder=site/"vendor"/"pyodide"
    monkeypatch.setattr(pack.license_sbom, "build_inventory",
                        lambda _folder:({"bomFormat":"CycloneDX","specVersion":"1.6"},
                                       {"acceptance":"HOLD","package_count":1}))
    pack._make_unapproved_license_packet(site)
    files=pack._listed_files(site)
    names={
      "third_party/bg2-exact-wheel-notice-probe.json":"license_probe_sha256",
      "third_party/bg2-sbom.cdx.json":"sbom_sha256",
      "third_party/bg2-license-disposition.json":"license_disposition_sha256",
      "third_party/THIRD_PARTY_NOTICES_CANDIDATE.txt":"notices_candidate_sha256"
    }
    manifest={key:pack.sha256(files[path]) for path,key in names.items()}
    manifest["license_sbom_approved"]=False
    pack._verify_unapproved_license_packet(files,manifest,state)
    bad=dict(files)
    bad.pop("third_party/bg2-sbom.cdx.json")
    with pytest.raises(RuntimeError,match="third-party notice evidence"):
        pack._verify_unapproved_license_packet(bad,manifest,state)
    bad=dict(files)
    bad["third_party/THIRD_PARTY_NOTICES_CANDIDATE.txt"]+=b"unauthorized notice"
    with pytest.raises(RuntimeError,match="mismatched pinned notice"):
        pack._verify_unapproved_license_packet(bad,manifest,state)
    assert b"NOT AN APPROVED NOTICE SET" in files["third_party/THIRD_PARTY_NOTICES_CANDIDATE.txt"]
    probe_receipt=json.loads(files["third_party/bg2-exact-wheel-notice-probe.json"])
    assert probe_receipt["wheels"][0]["wheel_sha256"]==state["files_sha256"][wheel.name]
