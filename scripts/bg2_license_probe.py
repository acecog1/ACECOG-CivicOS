"""Exact Pyodide wheel-byte license evidence probe; a review aide, NOT a license grant.

Extracts actual embedded license/notice files and precise wheel SHA-256, never
substitutes a PyPI classifier for required third-party copyright texts.
"""
from __future__ import annotations
import argparse
from email.parser import Parser
import hashlib
import json
from pathlib import Path
import re
from zipfile import ZipFile

from scripts import vendor_browser_pyodide as runtime

SOURCE_LINKS = {
    "Pyodide MPL-2.0": "https://github.com/pyodide/pyodide/blob/b1e4fcc2488962f6360a97f19b9982d6fdb5d16f/LICENSE",
    "SciPy 1.18.0 BSD and copyright": "https://github.com/scipy/scipy/blob/v1.18.0/LICENSE.txt",
    "SciPy 1.18.0 bundled components": "https://github.com/scipy/scipy/blob/v1.18.0/LICENSES_bundled.txt",
    "Python/PSF CPython licensing": "https://docs.python.org/3.14/license.html",
}


def probe(vendor_dir: Path) -> dict:
    manifest = runtime.verify_vendor_directory(vendor_dir)
    packages = manifest["package_lock_metadata"]
    if set(packages) != set(manifest["packages"]):
        raise RuntimeError("Incomplete Pyodide wheel dependency graph")
    listing = []
    for key in sorted(packages):
        name = packages[key]["package_file"]
        archive = vendor_dir / name
        expected = manifest["files_sha256"][name]
        actual = hashlib.sha256(archive.read_bytes()).hexdigest()
        if actual != expected:
            raise RuntimeError("Wheel changed after vendoring: " + key)
        with ZipFile(archive) as z:
            metanames = [n for n in z.namelist() if n.endswith(".dist-info/METADATA")]
            if len(metanames) != 1:
                raise RuntimeError("Missing/ambiguous wheel metadata: " + key)
            metadata = Parser().parsestr(z.read(metanames[0]).decode("utf-8","replace"))
            real_name = metadata.get("Name",key)
            version = metadata.get("Version")
            if not version or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.+!-]*", version):
                raise RuntimeError("Invalid wheel version: " + key)
            license_files = {}
            for n in z.namelist():
                lower = n.lower()
                if not (".dist-info/" in lower and (
                    "/licenses/" in lower or lower.endswith(
                        ("/license", "/license.txt", "/license.md", "/copying", "/notice", "/notice.txt")))):
                    continue
                data = z.read(n)
                if len(data) > 1000000:
                    raise RuntimeError("Oversize wheel license document: " + key)
                license_files[n] = {"sha256": hashlib.sha256(data).hexdigest(),
                                    "bytes": len(data),
                                    "utf8_usable": bool(data and data.count(b"\x00") == 0),
                                    "embedded_notice_utf8": data.decode("utf-8", errors="replace")
                                    if data and data.count(b"\x00") == 0 else None}
        expression = metadata.get("License-Expression") or metadata.get("License") or ""
        listing.append({"package_key":key, "wheel":name, "name":real_name,
                        "version":version, "wheel_sha256":expected,
                        "source_package_page":"https://pypi.org/project/"+real_name+"/"+version+"/",
                        "license_expression_from_wheel":expression,
                        "license_classifiers":[c for c in metadata.get_all("Classifier",[])
                                               if c.startswith("License ::")],
                        "embedded_notice_files":license_files,
                        "review_status":"SOURCE_WHEEL_ATTRIBUTION_PENDING"})
    if not listing:
        raise RuntimeError("Empty wheel closure")
    return {
        "schema":"ACECOG-BG2-LICENSE-WHEEL-PROBE-v1",
        "distribution":"Pyodide",
        "version":runtime.VERSION,
        "pyodide_lock_sha256":runtime.PINNED_LOCK_SHA256,
        "core_root_status":manifest["core_root_status"],
        "wheels":listing,
        "source_of_truth_links":SOURCE_LINKS,
        "still_missing":[
            "Complete distributable Pyodide MPL license text and source-access notice",
            "Exact runtime CPython/PSF and compiled-in third-party stdlib attribution",
            "SciPy 1.18.0 source license and only bundled notices actually present in WASM wheel",
            "Any missing exact-wheel license texts beyond wheel metadata",
            "Qualified independent source-root rehash and full license/redistribution approval",
        ],
        "release_licensing_acceptance":"HOLD"
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vendor",type=Path,required=True)
    ap.add_argument("--output",type=Path,required=True)
    args=ap.parse_args()
    result=probe(args.vendor)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print("Exact vendored wheels:",len(result["wheels"]),
          "license disposition: HOLD; source/reference gaps:",len(result["still_missing"]))


if __name__=="__main__":
    main()
