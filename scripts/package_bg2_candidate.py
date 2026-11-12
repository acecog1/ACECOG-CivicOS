"""Create a review-only, transactionally promoted BG-2 static WASM artifact.

The output is a single deterministic ZIP. Never writes into a published BG-1
site, never deploys, and never asserts independent QA or operator authority.
An interrupted build preserves any previous complete output byte-for-byte.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

# Support both `python -m scripts.package_bg2_candidate` (preferred) and the
# direct CLI path used by operators; do not mask unrelated missing dependencies.
if __package__:
    from scripts import build_browser_lab as source
    from scripts import vendor_browser_pyodide as runtime
    from scripts import bg2_license_probe as license_probe
    from scripts import build_bg2_sbom as license_sbom
else:
    import build_browser_lab as source
    import vendor_browser_pyodide as runtime
    import bg2_license_probe as license_probe
    import build_bg2_sbom as license_sbom

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = "ACECOG-BG2-STATIC-REVIEW-PACK-v1"
MAX_BUNDLE_BYTES = 240 * 1024 * 1024
ZIP_DATE = (1980, 1, 1, 0, 0, 0)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical(obj: object) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=True).encode("utf-8")


def exact_checkout(expected: str) -> str:
    if not re.fullmatch(r"[0-9a-f]{40}", expected):
        raise RuntimeError("An exact approved-source-style SHA-40 is mandatory")
    actual = source.checked_out_source_revision()
    if actual != expected:
        raise RuntimeError("BG-2 source SHA differs from checked-out Git HEAD")
    return actual


def git_tree() -> str:
    value = subprocess.check_output(
        ["git", "rev-parse", "HEAD^{tree}"],
        cwd=ROOT, text=True, stderr=subprocess.DEVNULL, timeout=10,
    ).strip().lower()
    if not re.fullmatch(r"[a-f0-9]{40}", value):
        raise RuntimeError("Invalid Git source tree SHA")
    return value


def _build_input_paths() -> tuple[str, ...]:
    # The fixed, reviewable list of all tracked source inputs used to generate
    # visitor-visible runtime content (including extraction/packaging logic).
    files = {
        "scripts/lab_preview_assets/index.html",
        "scripts/lab_preview_assets/lab.js",
        "scripts/lab_preview_assets/lab.css",
        "scripts/lab_preview_assets/experience.js",
        "scripts/browser_lab/browser-api.js",
        "scripts/browser_lab/browser-engine-worker.mjs",
        "tests/scenario.py",
        "scripts/build_browser_lab.py",
        "scripts/vendor_browser_pyodide.py",
        "scripts/package_bg2_candidate.py",
        "scripts/verify_bg2_upstream.py",
        "scripts/build_bg2_sbom.py",
        "scripts/bg2_license_probe.py",
        "scripts/bg2_stage.py",
        "docs/evidence/bg2-pyodide-core-candidate-pins-v1.json",
    }
    files.update(name for name, _target in source.FILES)
    return tuple(sorted(files))


def _read_git_blob(path: str) -> bytes:
    result = subprocess.run(
        ["git", "show", "HEAD:" + path],
        cwd=ROOT, capture_output=True, timeout=10, check=False,
    )
    if result.returncode:
        raise RuntimeError("Missing exact Git source input: " + path)
    return result.stdout


def _source_input_hashes() -> dict[str, str]:
    result = {}
    for name in _build_input_paths():
        file = ROOT/name
        if not file.is_file() or file.is_symlink():
            raise RuntimeError("Missing/unsafe checked-out source: " + name)
        live = file.read_bytes()
        if live != _read_git_blob(name):
            raise RuntimeError("Source input differs from Git HEAD: " + name)
        result[name] = sha256(live)
    return result


def _verify_checkout_against_package(payload: dict[str, bytes],
                                     source_revision: str,
                                     source_tree: str,
                                     source_inputs: dict[str,str]) -> None:
    """Independently rebuild unvendored sources from the *exact* Git checkout.

    A self-consistent but forged release manifest must not pass this check.
    """
    exact_checkout(source_revision)
    if git_tree() != source_tree or _source_input_hashes() != source_inputs:
        raise RuntimeError("Exact Git source input/tree provenance mismatch")
    with tempfile.TemporaryDirectory(prefix=".bg2-rebuild-") as tmp:
        dest = Path(tmp)/"source"
        source.build(dest)
        rebuilt = _listed_files(dest)
        archived = {name:data for name,data in payload.items()
                    if not name.startswith(("vendor/pyodide/","third_party/"))}
        if rebuilt != archived:
            raise RuntimeError("Packaged application differs from reproducible Git source")


def _listed_files(directory: Path) -> dict[str, bytes]:
    files = {}
    for p in sorted(directory.rglob("*")):
        if p.is_symlink():
            raise RuntimeError("Symlink in BG-2 static artifact forbidden")
        if p.is_file():
            name = p.relative_to(directory).as_posix()
            if name.startswith(".") or ".." in Path(name).parts:
                raise RuntimeError("Unexpected static artifact path")
            files[name] = p.read_bytes()
    return files


def _verify_source_inventory(files: dict[str, bytes], manifest: dict) -> None:
    if manifest.get("schema") != "ACECOG-browser-lab-source-v0.1":
        raise RuntimeError("Unexpected source manifest schema")
    if manifest.get("scenario_kind") != "abbreviated-isolated-synthetic-not-279-event-fork":
        raise RuntimeError("Unapproved source history claim")
    source_files = manifest.get("files")
    if not isinstance(source_files, dict) or not source_files:
        raise RuntimeError("Missing source-file inventory")
    unvendored = {name for name in files
                  if not name.startswith(("vendor/pyodide/","third_party/"))}
    if unvendored != set(source_files) | {"source-manifest.json"}:
        raise RuntimeError("Unlisted or missing browser application asset")
    for name, expected in source_files.items():
        if not isinstance(name, str) or not isinstance(expected, str) or not re.fullmatch(r"[a-f0-9]{64}", expected):
            raise RuntimeError("Invalid source-file digest")
        if name not in files or sha256(files[name]) != expected:
            raise RuntimeError("Source-to-package hash mismatch: " + str(name))


def _verify_runtime_inventory(files: dict[str, bytes], manifest: dict) -> None:
    inventory = manifest.get("files_sha256")
    if not isinstance(inventory, dict) or not inventory:
        raise RuntimeError("Missing Pyodide runtime inventory")
    runtime_paths = {name for name in files if name.startswith("vendor/pyodide/")
                     and name != "vendor/pyodide/acecog-runtime-manifest.json"}
    expected_paths = {"vendor/pyodide/" + name for name in inventory}
    if runtime_paths != expected_paths:
        raise RuntimeError("Missing/extra packaged WASM files")
    total = 0
    for name, expected in inventory.items():
        if not isinstance(name, str) or "/" in name or "\\" in name or name.startswith("."):
            raise RuntimeError("Unsafe WASM asset path")
        key = "vendor/pyodide/" + name
        data = files[key]
        if sha256(data) != expected:
            raise RuntimeError("Source-to-runtime hash mismatch: " + name)
        total += len(data)
    if total != manifest.get("bytes") or manifest.get("version") != runtime.VERSION:
        raise RuntimeError("Packaged runtime footprint/version mismatch")
    if (manifest.get("root_lock_sha256") != runtime.PINNED_LOCK_SHA256 or
            inventory.get("pyodide-lock.json") != runtime.PINNED_LOCK_SHA256):
        raise RuntimeError("Unrecognized packaged runtime lock")


def _make_unapproved_license_packet(site: Path) -> None:
    """User-accessible *evidence* in pinned review ZIP, not a legal notice grant.

    Every contained wheel is verified against the Pyodide lock and inspected
    for real embedded notices. Absent SciPy/CPython/full MPL notices remain
    prominently unresolved. Distribution is permanently blocked until review.
    """
    root = site/"vendor"/"pyodide"
    inspection = license_probe.probe(root)
    sbom, disposition = license_sbom.build_inventory(root)
    if (disposition.get("acceptance") != "HOLD" or
            inspection.get("release_licensing_acceptance") != "HOLD"):
        raise RuntimeError("License review must remain explicitly unapproved")
    folder = site/"third_party"
    folder.mkdir(parents=True)
    (folder/"bg2-exact-wheel-notice-probe.json").write_text(
        json.dumps(inspection,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    (folder/"bg2-sbom.cdx.json").write_text(
        json.dumps(sbom,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    (folder/"bg2-license-disposition.json").write_text(
        json.dumps(disposition,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    text = [
        "ACECOG BG-2 — THIRD PARTY LICENSE EVIDENCE / NOT AN APPROVED NOTICE SET",
        "Public release prohibited: source, bundled components and redistribution",
        "conditions remain for independent qualified review.",
        "",
        "Runtime: Pyodide "+runtime.VERSION+" (MPL-2.0 and included CPython);",
        "root lock SHA-256: "+runtime.PINNED_LOCK_SHA256,
        "This fixture is fictional, visitor controlled, and not BG-1's 279-event fork.",
        "",
        "Exact-version upstream source reference links (review pending):"
    ]
    for label,url in sorted(inspection["source_of_truth_links"].items()):
        text.extend([label, url])
    text.extend(["", "Actual vendored wheel contents and license evidence:"])
    for wheel in inspection["wheels"]:
        text.extend(["", wheel["name"]+" "+wheel["version"],
                     "Wheel SHA-256 "+wheel["wheel_sha256"],
                     "Source package page "+wheel["source_package_page"],
                     "Wheel METADATA license expression: "+
                     (wheel["license_expression_from_wheel"] or "UNDETERMINED"),
                     "Embedded wheel notice count "+
                     str(len(wheel["embedded_notice_files"]))])
        for filename,info in sorted(wheel["embedded_notice_files"].items()):
            text.extend(["", "=== "+filename+" ===",
                         info["embedded_notice_utf8"] or
                         "Non-UTF8 or binary notice: consult wheel hash and extraction record"])
    text.extend(["", "CRITICAL UNRESOLVED REDISTRIBUTION REQUIREMENTS:"])
    text.extend("* "+item for item in inspection["still_missing"])
    text.extend(["", "No independent license or pinset approval was granted."])
    (folder/"THIRD_PARTY_NOTICES_CANDIDATE.txt").write_text(
        "\n".join(text)+"\n",encoding="utf-8")


def _verify_unapproved_license_packet(files: dict[str,bytes],
                                      manifest: dict, wasm: dict) -> None:
    """Pinned review candidates must include complete inspectable evidence.

    Presence is NOT qualified licensing approval: the release status stays HOLD.
    """
    keys = {
        "third_party/bg2-exact-wheel-notice-probe.json":"license_probe_sha256",
        "third_party/bg2-sbom.cdx.json":"sbom_sha256",
        "third_party/bg2-license-disposition.json":"license_disposition_sha256",
        "third_party/THIRD_PARTY_NOTICES_CANDIDATE.txt":"notices_candidate_sha256",
    }
    if set(n for n in files if n.startswith("third_party/")) != set(keys):
        raise RuntimeError("Incomplete/extra third-party notice evidence in pinned package")
    for path,field in keys.items():
        if manifest.get(field) != sha256(files[path]):
            raise RuntimeError("Missing/mismatched pinned notice/SBOM evidence: "+path)
    if "NOT AN APPROVED NOTICE SET" not in files[
            "third_party/THIRD_PARTY_NOTICES_CANDIDATE.txt"].decode("utf-8"):
        raise RuntimeError("Missing explicit redistribution HOLD")
    probe = json.loads(files["third_party/bg2-exact-wheel-notice-probe.json"])
    sbom = json.loads(files["third_party/bg2-sbom.cdx.json"])
    status = json.loads(files["third_party/bg2-license-disposition.json"])
    if (probe.get("release_licensing_acceptance") != "HOLD" or
            probe.get("pyodide_lock_sha256") != wasm.get("root_lock_sha256") or
            len(probe.get("wheels",[])) != len(wasm.get("packages",[])) or
            sbom.get("bomFormat") != "CycloneDX" or
            status.get("acceptance") != "HOLD" or
            status.get("package_count") != len(wasm.get("packages",[]))):
        raise RuntimeError("Incomplete or falsely approved license packet")
    hashes = wasm.get("files_sha256",{})
    actual = {w["wheel"]:w["wheel_sha256"] for w in probe["wheels"]}
    if any(hashes.get(name) != digest for name,digest in actual.items()):
        raise RuntimeError("Notice inventory is not bound to actual locked wheel bytes")
    if manifest.get("license_sbom_approved") is not False:
        raise RuntimeError("Do not infer legal approval from notice evidence")


def verify_review_zip(path: Path, expected_sha: str | None = None) -> dict:
    """Independent byte-level check, including all inner source/runtime hashes."""
    with ZipFile(path, "r") as z:
        members = z.infolist()
        names = [x.filename for x in members]
        if len(names) != len(set(names)) or any(
                not n or n.startswith("/") or "\\" in n or ".." in Path(n).parts
                or n.endswith("/") for n in names):
            raise RuntimeError("Unsafe/duplicate BG-2 archive member")
        if sum(x.file_size for x in members) > MAX_BUNDLE_BYTES:
            raise RuntimeError("Oversize BG-2 artifact")
        files = {name: z.read(name) for name in names}
    required = {"release-manifest.json", "source-manifest.json",
                "vendor/pyodide/acecog-runtime-manifest.json"}
    if not required.issubset(files):
        raise RuntimeError("Incomplete BG-2 release package")
    manifest = json.loads(files["release-manifest.json"])
    if manifest.get("schema") != SCHEMA:
        raise RuntimeError("Unknown BG-2 release manifest")
    if expected_sha is not None and manifest.get("source_revision") != expected_sha:
        raise RuntimeError("BG-2 release SHA differs from approved expected SHA")
    if not re.fullmatch(r"[0-9a-f]{40}", manifest.get("source_revision","")):
        raise RuntimeError("BG-2 release has no exact source commit")
    payload = {k:v for k,v in files.items() if k != "release-manifest.json"}
    observed = {k:sha256(v) for k,v in payload.items()}
    if observed != manifest.get("file_sha256"):
        raise RuntimeError("BG-2 artifact/file manifest digest mismatch")
    if sha256(canonical(observed)) != manifest.get("artifact_tree_sha256"):
        raise RuntimeError("BG-2 package tree digest mismatch")
    if sha256(files["source-manifest.json"]) != manifest.get("source_manifest_sha256"):
        raise RuntimeError("Packaged source manifest digest mismatch")
    if sha256(files["vendor/pyodide/acecog-runtime-manifest.json"]) != manifest.get("runtime_manifest_sha256"):
        raise RuntimeError("Packaged runtime manifest digest mismatch")
    src = json.loads(files["source-manifest.json"])
    wasm = json.loads(files["vendor/pyodide/acecog-runtime-manifest.json"])
    if src.get("source_revision") != manifest.get("source_revision"):
        raise RuntimeError("Git checkout/source manifest/release identity mismatch")
    _verify_source_inventory(payload, src)
    _verify_runtime_inventory(payload, wasm)
    if wasm.get("core_root_status") == "EXACT_PINSET_VERIFIED_PENDING_INDEPENDENT_QA":
        _verify_unapproved_license_packet(payload,manifest,wasm)
    elif any(k.startswith("third_party/") for k in payload):
        raise RuntimeError("Unpinned feasibility candidate may not claim notice packet")
    if (wasm.get("core_root_status") not in (
            "EXACT_PINSET_VERIFIED_PENDING_INDEPENDENT_QA",
            "UNPINNED_OBSERVED_ONLY_BLOCK_RELEASE") or
            wasm.get("core_root_status") != manifest.get("runtime_pin_status")):
        raise RuntimeError("Runtime pin approval claim disagrees with asset manifest")
    if manifest.get("releasable") is not False:
        raise RuntimeError("BG-2 candidate must not self-authorize public publication")
    if manifest.get("scenario_kind") != src.get("scenario_kind"):
        raise RuntimeError("BG-2 noncanonical scenario lineage mismatch")
    inputs = manifest.get("git_source_inputs_sha256")
    if (not isinstance(inputs,dict) or set(inputs) != set(_build_input_paths()) or
            not all(isinstance(value,str) and re.fullmatch(r"[a-f0-9]{64}",value)
                    for value in inputs.values())):
        raise RuntimeError("BG-2 exact Git source input inventory absent")
    if expected_sha is not None:
        _verify_checkout_against_package(payload,expected_sha,
                                         manifest["source_tree_sha"],inputs)
    return manifest


def build_candidate(output: Path, expected_sha: str, vendor_source: Path) -> dict:
    """Clean staging -> verify -> deterministic archive -> one atomic replace."""
    sha = exact_checkout(expected_sha)
    source_input_hashes = _source_input_hashes()
    output = Path(output)
    vendor_source = Path(vendor_source)
    if output.is_symlink() or (output.exists() and not output.is_file()):
        raise RuntimeError("Unsafe BG-2 output location")
    # Validate the previously built vendor closure; no partially downloaded
    # files from a previous attempt can be copied into the next candidate.
    runtime.verify_vendor_directory(vendor_source)
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".bg2-package-stage-", dir=output.parent) as tmp:
        temp = Path(tmp)
        site = temp/"site"
        source.build(site)
        shutil.copytree(vendor_source, site/"vendor"/"pyodide")
        runtime_manifest = runtime.verify_vendor_directory(site/"vendor"/"pyodide")
        if runtime_manifest.get("core_root_status") == "EXACT_PINSET_VERIFIED_PENDING_INDEPENDENT_QA":
            _make_unapproved_license_packet(site)
        files = _listed_files(site)
        src_manifest = json.loads(files["source-manifest.json"])
        if src_manifest.get("source_revision") != sha:
            raise RuntimeError("Builder manifest was not generated from exact checkout")
        _verify_source_inventory(files, src_manifest)
        _verify_runtime_inventory(files, runtime_manifest)
        digests = {name:sha256(data) for name,data in files.items()}
        record = {
            "schema":SCHEMA,
            "state":"REVIEW_ARTIFACT_ONLY_PUBLICATION_HOLD",
            "source_revision":sha,
            "source_tree_sha":git_tree(),
            "git_source_inputs_sha256":source_input_hashes,
            "source_manifest_sha256":digests["source-manifest.json"],
            "runtime_manifest_sha256":digests["vendor/pyodide/acecog-runtime-manifest.json"],
            "runtime_pin_status":runtime_manifest["core_root_status"],
            "license_probe_sha256":digests.get("third_party/bg2-exact-wheel-notice-probe.json"),
            "sbom_sha256":digests.get("third_party/bg2-sbom.cdx.json"),
            "license_disposition_sha256":digests.get("third_party/bg2-license-disposition.json"),
            "notices_candidate_sha256":digests.get("third_party/THIRD_PARTY_NOTICES_CANDIDATE.txt"),
            "scenario_kind":src_manifest["scenario_kind"],
            "artifact_tree_sha256":sha256(canonical(digests)),
            "file_sha256":digests,
            "releasable":False,
            "license_sbom_approved":False,
            "independent_qa_go":False,
            "publication_authorization":False,
            "note":"Synthetic browser-controlled shortened fixture, NOT BG-1's 279-event fork; package is never a live civic authority",
        }
        files["release-manifest.json"] = canonical(record)+b"\n"
        staged_zip = temp/"candidate.zip"
        with ZipFile(staged_zip, "w", compression=ZIP_DEFLATED, compresslevel=6) as zipout:
            for name,data in sorted(files.items()):
                entry = ZipInfo(name, date_time=ZIP_DATE)
                entry.compress_type = ZIP_DEFLATED
                entry.external_attr = (0o100644 << 16)
                zipout.writestr(entry,data,compress_type=ZIP_DEFLATED,compresslevel=6)
        checked = verify_review_zip(staged_zip, expected_sha=sha)
        os.replace(staged_zip,output)  # atomic for an existing ZIP on same filesystem
        return {"source_revision":sha,"archive_sha256":sha256(output.read_bytes()),
                "artifact_tree_sha256":checked["artifact_tree_sha256"],
                "files":len(checked["file_sha256"]),
                "runtime_pin_status":checked["runtime_pin_status"],
                "bytes":output.stat().st_size}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("action", choices=["build", "verify"])
    ap.add_argument("--output",type=Path,required=True)
    ap.add_argument("--source-sha",required=True,
                    help="Exact 40-character checked-out source commit, not PR merge event SHA")
    ap.add_argument("--vendor-source",type=Path,
                    help="Existing fully verified WASM directory; required for build")
    args = ap.parse_args()
    if args.action == "build":
        if args.vendor_source is None:
            ap.error("--vendor-source is required for build")
        result = build_candidate(args.output,args.source_sha,args.vendor_source)
    else:
        result = verify_review_zip(args.output,args.source_sha)
    print(json.dumps(result,sort_keys=True,default=str))


if __name__ == "__main__":
    main()
