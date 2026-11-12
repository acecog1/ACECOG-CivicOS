"""Generate review-only CycloneDX dependency graph and license disposition.

Parses each installed vendored wheel's distribution METADATA, the verified
Pyodide lock closure and checksums. No missing license silently passes.
Never certifies the legal adequacy of license obligations.
"""
from __future__ import annotations
import argparse
from email.parser import Parser
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import quote
from zipfile import ZipFile
from scripts import vendor_browser_pyodide as vendor

def build_inventory(directory: Path) -> tuple[dict,dict]:
    manifest=vendor.verify_vendor_directory(directory)
    components=[]
    dependencies=[]
    issues=[]
    by_file=manifest["files_sha256"]
    components.append({
        "type":"framework","name":"Pyodide","version":vendor.VERSION,
        "bom-ref":"pkg:npm/pyodide@"+vendor.VERSION,
        "licenses":[{"license":{"id":"MPL-2.0"}}],
        "properties":[
            {"name":"acecog:license-status","value":"manual-review-required (includes bundled runtimes/CPython)"},
            {"name":"acecog:root-pin-status","value":manifest["core_root_status"]}],
    })
    for root in vendor.CORE_ROOT_ASSETS:
        components.append({"type":"file","name":root,
            "bom-ref":"file:pyodide/"+root,
            "hashes":[{"alg":"SHA-256","content":by_file[root]}],
            "properties":[{"name":"acecog:parent","value":"Pyodide "+vendor.VERSION}]})
    packages=manifest["package_lock_metadata"]
    for short in manifest["packages"]:
        metadata=packages.get(short)
        if not isinstance(metadata,dict):
            raise RuntimeError("Missing dependency graph for "+short)
        name=metadata["package_file"]
        if name not in by_file:
            raise RuntimeError("Missing wheel checksum for "+short)
        archive=directory/name
        with ZipFile(archive) as z:
            candidates=[n for n in z.namelist() if n.endswith(".dist-info/METADATA")]
            if len(candidates)!=1:
                raise RuntimeError("Wheel METADATA missing/ambiguous: "+name)
            mail=Parser().parsestr(z.read(candidates[0]).decode("utf-8","replace"))
            wheel_license_files=[n for n in z.namelist() if (
                ".dist-info/licenses/" in n or n.endswith(".dist-info/LICENSE")
                or n.endswith(".dist-info/COPYING"))]
        package_name=mail.get("Name",short)
        version=mail.get("Version")
        if not version:
            raise RuntimeError("Missing wheel version: "+name)
        expression=mail.get("License-Expression")
        simple=mail.get("License")
        classifiers=[str(x) for x in (mail.get_all("Classifier") or [])
                     if str(x).startswith("License ::")]
        license_value=(expression or simple or "")
        has_usable_license=bool(license_value.strip() and len(license_value)<256)
        license_cdx=([{"expression":license_value}] if has_usable_license
                    else [{"license":{"name":"UNDETERMINED—REVIEW_REQUIRED"}}])
        ref="pkg:pypi/"+quote(package_name.lower().replace("_","-"))+"@"+version
        component={"type":"library","name":package_name,"version":version,
          "bom-ref":ref,"purl":ref,
          "hashes":[{"alg":"SHA-256","content":by_file[name]}],
          "licenses":license_cdx,
          "properties":[
            {"name":"acecog:locked-package-key","value":short},
            {"name":"acecog:wheel-name","value":name},
            {"name":"acecog:wheel-license-files","value":json.dumps(wheel_license_files)},
            {"name":"acecog:wheel-license-classifiers","value":json.dumps(classifiers)},
            {"name":"acecog:legal-review","value":"INDEPENDENT_REVIEW_REQUIRED"}]}
        components.append(component)
        dependencies.append({"ref":ref,"dependsOn":[]})
        if not has_usable_license:
            issues.append({"name":package_name,"version":version,
                           "issue":"License expression absent/ambiguous in wheel METADATA",
                           "classifiers":classifiers,"license_files":wheel_license_files})
    pkg_lookup={c["name"].lower().replace("_","-"):c["bom-ref"] for c in components
                if c["type"]=="library"}
    for node in dependencies:
        component=next(c for c in components if c["bom-ref"]==node["ref"])
        key=next(k for k in manifest["packages"] if
                 packages[k]["package_file"]==next(
                 p["value"] for p in component["properties"]
                 if p["name"]=="acecog:wheel-name"))
        for dep in packages[key].get("depends",[]):
            d=vendor.normalized(dep)
            if d not in pkg_lookup:
                raise RuntimeError("Undisclosed transitive package: "+d)
            node["dependsOn"].append(pkg_lookup[d])
        node["dependsOn"].sort()
    dependencies.append({"ref":"pkg:npm/pyodide@"+vendor.VERSION,
                         "dependsOn":sorted(pkg_lookup.values())})
    for root in vendor.CORE_ROOT_ASSETS:
        dependencies.append({"ref":"file:pyodide/"+root,"dependsOn":[]})
    sbom={
        "bomFormat":"CycloneDX","specVersion":"1.6","version":1,
        "metadata":{"component":{"type":"application","name":"ACECOG-BG2-review-only"},
            "properties":[{"name":"acecog:verification","value":"NOT_INDEPENDENTLY_APPROVED"},
              {"name":"acecog:runtime-manifest-sha256",
               "value":hashlib.sha256((directory/"acecog-runtime-manifest.json").read_bytes()).hexdigest()}]},
        "components":components,"dependencies":dependencies}
    disposition={"schema":"ACECOG-BG2-LICENSE-DISPOSITION-v1",
      "runtime_version":vendor.VERSION,
      "package_count":len(manifest["packages"]),
      "direct_dependency_roots":manifest["package_roots"],
      "transitive_package_count":len(manifest["packages"])-len(manifest["package_roots"]),
      "all_package_names":sorted(manifest["packages"]),
      "undetermined_license_items":issues,
      "core_runtime_mpl2_plus_cpython_bundled_licenses_review":"PENDING",
      "wheel_license_attribution_and_republication_review":"PENDING",
      "independent_legal_or_security_license_review":"PENDING",
      "acceptance":"HOLD"}
    return sbom,disposition

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--vendor",type=Path,required=True)
    ap.add_argument("--output-dir",type=Path,required=True)
    args=ap.parse_args()
    sbom,disposition=build_inventory(args.vendor)
    args.output_dir.mkdir(parents=True,exist_ok=True)
    for name,obj in [("bg2-sbom.cdx.json",sbom),
                     ("bg2-license-disposition.json",disposition)]:
        (args.output_dir/name).write_text(json.dumps(obj,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print("Undetermined wheel licenses:",json.dumps(disposition["undetermined_license_items"],sort_keys=True))
    print("SBOM package count:",disposition["package_count"],
          "unknown license items:",len(disposition["undetermined_license_items"]),
          "independent license disposition: PENDING")

if __name__=="__main__":
    main()
