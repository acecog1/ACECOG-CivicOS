"""Review evidence and publication authorization cannot be conflated."""
import json
from pathlib import Path
from zipfile import ZipFile
import pytest
from scripts.bg2_publication_gate import require_publication_artifact


@pytest.mark.parametrize("flags,acceptance", [
    ({}, "HOLD"),
    ({"releasable": False}, "GO"),
    ({"releasable": True}, "HOLD"),
    ({key: True for key in ("releasable", "license_sbom_approved",
      "independent_qa_go", "publication_authorization")}, "GO"),
])
def test_provisional_or_forged_approval_never_passes(tmp_path, flags, acceptance):
    archive = tmp_path / "candidate.zip"
    with ZipFile(archive, "w") as z:
        z.writestr("release-manifest.json", json.dumps(flags))
        z.writestr("third_party/bg2-license-disposition.json",
                   json.dumps({"acceptance": acceptance}))
    with pytest.raises(RuntimeError, match="PUBLICATION HOLD"):
        require_publication_artifact(archive)


def test_review_workflow_never_reads_release_go_variables():
    root = Path(__file__).resolve().parents[1]
    review = (root / ".github/workflows/bg2-review-integrity.yml").read_text()
    assert "NO APPROVAL" in review
    assert "vars.BG2_" not in review
    assert "environment: bg2-publication" not in review
    assert "uses: actions/deploy-pages" not in review
    publication = (root / ".github/workflows/bg2-release-gated.yml").read_text()
    gate = publication.index("python -m scripts.bg2_publication_gate")
    assert gate < publication.index("name: Archive preflight receipt")
