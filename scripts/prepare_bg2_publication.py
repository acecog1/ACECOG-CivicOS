"""Assemble a reviewable full Pages candidate; never grant approval or deploy.

BG-1 input must be an archived actual previous deployment, not a rebuild. Exact
runtime verification is executed against its source checkout before assembly.
"""
from __future__ import annotations
import argparse
import json
import subprocess
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED
from scripts.bg2_publication_gate import digest, read_archive, SCHEMA, hold

ROOT = Path(__file__).resolve().parents[1]


def assemble(previous: Path, runtime: Path, source_sha: str, output: Path,
             recipient_packet: Path | None = None) -> dict:
    from scripts.package_bg2_candidate import verify_review_zip
    verify_review_zip(runtime, source_sha)
    files = read_archive(previous)
    if "index.html" not in files or any(n.startswith("beta/") for n in files):
        hold("initial publication requires an actual BG-1 snapshot without beta")
    baseline = {n: digest(b) for n, b in files.items()}
    if "publication-manifest.json" in files:
        hold("BG-1 snapshot contains reserved publication manifest")
    app = read_archive(runtime)
    old_index = app["index.html"]
    if old_index.count(b"</footer>") != 1:
        hold("application footer changed")
    app["index.html"] = old_index.replace(b"</footer>",
        b'<a href="./legal/index.html">Release notices and source access</a></footer>')
    files.update({"beta/" + n: b for n, b in app.items()})
    evidence = ROOT / "docs/evidence"
    supplement = evidence / "bg2-beta-packet-20261113/licensing-source-review.zip"
    recovery = evidence / "bg2-mandatory-groups-20261113/review-addendum.zip"
    for prefix, archive in (("beta/legal/original/", supplement),
                            ("beta/legal/recovered/", recovery)):
        files.update({prefix + n: b for n, b in read_archive(archive).items()})
    # This packet is deliberately still pending independent sufficiency review.
    # Recovered exact texts do not automatically settle selected-code applicability.
    files["beta/legal/index.html"] = b'''<!doctype html><html lang="en"><meta charset="utf-8">
<title>BG-2 notices and source access</title><main><h1>Notices and source access</h1>
<p>Candidate for independent review. No licensing approval is asserted.</p>
<ul><li><a href="THIRD_PARTY_NOTICES.txt">Recipient notice index</a></li>
<li><a href="SOURCE_ACCESS.txt">Source and modifications</a></li>
<li><a href="original/index.html">Original notice and component crosswalk</a></li>
<li><a href="recovered/index.html">Recovered CPython, SDK, Rust and patch evidence</a></li>
<li><a href="claims.json">Finite claim disposition</a></li></ul></main></html>'''
    files["beta/legal/THIRD_PARTY_NOTICES.txt"] = (
        b"BG-2 recipient notice candidate: independent sufficiency review pending.\n"
        b"Original full notice texts: ./original/THIRD_PARTY_NOTICES.txt\n"
        b"Recovered original texts and source/patch matrix: ./recovered/index.html\n"
        b"Rust 1.97.1 standard-library copyright text:\n"
        b"./recovered/upstream/rust-1.97.1/rustc/share/doc/rust/COPYRIGHT-library.html\n")
    files["beta/legal/SOURCE_ACCESS.txt"] = (
        "ACECOG source and modifications at exact candidate revision:\n"
        f"https://github.com/acecog1/ACECOG-CivicOS/tree/{source_sha}\n"
        "Covered upstream source archive pins and patch receipts:\n"
        "./recovered/source-archives.json\n./recovered/component-source-matrix.json\n"
        "Recipe patches: ./recovered/upstream/recipes/packages/\n"
        "Public source access is not proof of complete covered modifications.\n"
        "Matching-source sufficiency remains pending independent disposition.\n"
    ).encode()
    original_claims = json.loads(files["beta/legal/original/dispositions.json"])
    files["beta/legal/claims.json"] = json.dumps({"claims": [
        {"id": c["id"], "classification": c["classification"],
         "disposition": "PENDING", "claim": c["claim"],
         "evidence_paths": ["beta/legal/original/dispositions.json",
                            "beta/legal/recovered/component-source-matrix.json"]}
        for c in original_claims]}, indent=2).encode()
    # A later independently curated packet can replace the pending recipient
    # documents. Original evidence stays intact; no decision is fabricated.
    if recipient_packet is not None:
        folder = recipient_packet.resolve()
        folder.relative_to(ROOT.resolve())
        for item in sorted(folder.rglob('*')):
            if item.is_symlink():
                hold('symlink in recipient packet')
            if item.is_file():
                relative = item.relative_to(folder).as_posix()
                if relative.startswith(('original/', 'recovered/')):
                    hold('recipient packet cannot overwrite original evidence')
                repo_path = item.relative_to(ROOT.resolve()).as_posix()
                original = subprocess.check_output(['git', 'show', source_sha + ':' + repo_path], cwd=ROOT)
                if original != item.read_bytes():
                    hold('recipient packet differs from exact Git source')
                files['beta/legal/' + relative] = original
    manifest = {"schema": SCHEMA, "source_sha": source_sha,
        "runtime_archive_sha256": digest(runtime.read_bytes()),
        "previous_site_sha256": digest(previous.read_bytes()),
        "bg1_file_sha256": baseline,
        "supplement_sha256": digest(supplement.read_bytes()),
        "recovery_sha256": digest(recovery.read_bytes()),
        "index_transformation": "append-release-notices-link-v1",
        "file_sha256": {n: digest(b) for n, b in sorted(files.items())}}
    files["publication-manifest.json"] = json.dumps(manifest, sort_keys=True, indent=2).encode()
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.exists():
        hold("candidate output already exists")
    with ZipFile(output, "w", compression=ZIP_DEFLATED) as z:
        for name, data in sorted(files.items()):
            info = ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            z.writestr(info, data)
    return {"archive_sha256": digest(output.read_bytes()), "manifest": manifest,
            "status": "REVIEW_REQUIRED_NOT_APPROVED"}


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--previous-site", type=Path, required=True)
    p.add_argument("--runtime", type=Path, required=True)
    p.add_argument("--source-sha", required=True)
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--recipient-packet", type=Path)
    a = p.parse_args()
    print(json.dumps(assemble(a.previous_site, a.runtime, a.source_sha, a.output,
                             a.recipient_packet), sort_keys=True))
