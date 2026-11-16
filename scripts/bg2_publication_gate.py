"""Publication is unavailable for the current provisional review-only format.

This gate is intentionally separate from verify_review_zip. Matching external
GO strings can never turn unapproved redistribution evidence into a release.
An accepted artifact format/notice packet must be implemented and independently
reviewed before enabling any positive publication path.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from zipfile import ZipFile


def require_publication_artifact(path: Path) -> None:
    with ZipFile(path) as archive:
        manifest = json.loads(archive.read("release-manifest.json"))
        disposition = json.loads(archive.read("third_party/bg2-license-disposition.json"))
        if (manifest.get("releasable") is not True or
                manifest.get("license_sbom_approved") is not True or
                manifest.get("independent_qa_go") is not True or
                manifest.get("publication_authorization") is not True or
                disposition.get("acceptance") != "GO"):
            raise RuntimeError("PUBLICATION HOLD: provisional/unapproved review artifact")
        # Reject even a forged flag flip: no approved packet verifier exists yet.
        # The current review verifier requires HOLD and releasable:false.
        raise RuntimeError("PUBLICATION HOLD: approved artifact format is not implemented or independently accepted")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--zip", type=Path, required=True)
    require_publication_artifact(parser.parse_args().zip)
