"""Verified original notice-source evidence; never a legal acceptance claim."""
import hashlib
import json
from pathlib import Path, PurePosixPath
import re

SOURCE = "docs/evidence/bg2-compiled-notices"
PREFIX = "third_party/compiled_notice_evidence/"


def records(raw: bytes) -> list[dict]:
    manifest = json.loads(raw)
    if (manifest.get("schema") != "ACECOG-BG2-COMPILED-NOTICE-EVIDENCE-v1"
            or manifest.get("acceptance") != "HOLD"
            or manifest.get("human_legal_review") != "NOT_RETAINED_NOT_ACCEPTED"):
        raise RuntimeError("Compiled notice evidence must remain unapproved")
    result = manifest.get("records", [])
    seen = set()
    if not result:
        raise RuntimeError("Empty compiled notice evidence")
    for item in result:
        name = item.get("path", "")
        path = PurePosixPath(name)
        if (not name or path.is_absolute() or path.as_posix() != name
                or ".." in path.parts or ":" in name or "\\" in name
                or name in seen or name == "manifest.json"
                or not re.fullmatch(r"[0-9a-f]{64}", item.get("sha256", ""))):
            raise RuntimeError("Unsafe/duplicate compiled notice source")
        seen.add(name)
    return result


def source_inputs(root: Path) -> list[str]:
    raw = (root/SOURCE/"manifest.json").read_bytes()
    return [SOURCE+"/manifest.json"] + [SOURCE+"/"+r["path"] for r in records(raw)]


def copy_verified(root: Path, folder: Path) -> None:
    raw = (root/SOURCE/"manifest.json").read_bytes()
    expected = records(raw)
    actual = {p.relative_to(root/SOURCE).as_posix() for p in (root/SOURCE).rglob("*") if p.is_file()}
    if actual != {"manifest.json"} | {r["path"] for r in expected}:
        raise RuntimeError("Extra/missing compiled notice source")
    dest = folder/"compiled_notice_evidence"
    dest.mkdir(parents=True, exist_ok=False)
    (dest/"manifest.json").write_bytes(raw)
    for item in expected:
        src = root/SOURCE/item["path"]
        if src.is_symlink() or hashlib.sha256(src.read_bytes()).hexdigest() != item["sha256"]:
            raise RuntimeError("Compiled notice source checksum mismatch: "+item["path"])
        target = dest/item["path"]
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(src.read_bytes())


def verify_packet(files: dict[str, bytes], root: Path) -> set[str]:
    raw = files.get(PREFIX+"manifest.json")
    if raw is None or raw != (root/SOURCE/"manifest.json").read_bytes():
        raise RuntimeError("Missing/forged compiled notice provenance")
    required = {PREFIX+"manifest.json"}
    for item in records(raw):
        name = PREFIX+item["path"]
        if name not in files or hashlib.sha256(files[name]).hexdigest() != item["sha256"]:
            raise RuntimeError("Missing/altered compiled notice text: "+item["path"])
        required.add(name)
    if {name for name in files if name.startswith(PREFIX)} != required:
        raise RuntimeError("Extra compiled notice evidence")
    return required
