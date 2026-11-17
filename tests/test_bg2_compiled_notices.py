import hashlib
import json
from pathlib import Path
import pytest
from scripts import bg2_compiled_notices as notices

ROOT = Path(__file__).resolve().parents[1]


def test_original_text_copy_and_tamper_rejection(tmp_path):
    notices.copy_verified(ROOT, tmp_path)
    files = {"third_party/"+p.relative_to(tmp_path).as_posix(): p.read_bytes()
             for p in tmp_path.rglob("*") if p.is_file()}
    assert len(notices.verify_packet(files, ROOT)) == 167
    libf2c = notices.PREFIX+"originals/clapack/F2CLIBS/libf2c/Notice"
    assert b"AT&T" in files[libf2c]
    for replacement in (None, b"generic BSD summary"):
        altered = dict(files)
        if replacement is None:
            altered.pop(libf2c)
        else:
            altered[libf2c] = replacement
        with pytest.raises(RuntimeError, match="Missing/altered"):
            notices.verify_packet(altered, ROOT)
    forged = dict(files)
    doc = json.loads(forged[notices.PREFIX+"manifest.json"])
    doc["acceptance"] = "GO"
    forged[notices.PREFIX+"manifest.json"] = json.dumps(doc).encode()
    with pytest.raises(RuntimeError, match="forged compiled notice provenance"):
        notices.verify_packet(forged, ROOT)


@pytest.mark.parametrize("path", ["../escape", "/absolute", "C:/escape", "a\\b", "a//b"])
def test_unsafe_source_paths_rejected(path):
    doc = json.loads((ROOT/notices.SOURCE/"manifest.json").read_bytes())
    doc["records"][0]["path"] = path
    with pytest.raises(RuntimeError, match="Unsafe/duplicate"):
        notices.records(json.dumps(doc).encode())


def test_all_native_members_have_explicit_pending_source_record():
    inventory = json.loads((ROOT/"docs/evidence/bg2-builder-20261112/locked-native-inventory.json").read_bytes())
    mapping = json.loads((ROOT/notices.SOURCE/"native-component-map.json").read_bytes())
    expected = {(w["wheel"], n["member_path"], n["sha256"])
                for w in inventory["wheels"] for n in w["native_members"]}
    actual = {(n["wheel"], n["member_path"], n["member_sha256"]) for n in mapping["members"]}
    assert actual == expected and len(actual) == 123
    assert all(n["status"] == "UNKNOWN_BLOCKING" for n in mapping["members"])
    assert mapping["acceptance"] == "HOLD"
    manifest = json.loads((ROOT/notices.SOURCE/"manifest.json").read_bytes())
    assert manifest["human_legal_review"] == "NOT_RETAINED_NOT_ACCEPTED"
    assert len(manifest["excluded"]) == 1
