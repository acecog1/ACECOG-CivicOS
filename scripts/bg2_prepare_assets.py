"""Create reviewed public/staging text assets without changing the localhost P2 UI.

Only deterministic replacement of known static strings. Run during Render BUILD,
then verify produced files (and fail rather than accidentally publishing local
wording). The generated files are build artifacts, not source or public release.
"""
from __future__ import annotations

from pathlib import Path
import sys

SOURCE = Path(__file__).resolve().parent / "lab_preview_assets"
DEST = Path(__file__).resolve().parents[1] / "build" / "bg2-assets"

COMMON = {
    "index.html": {
        "Riverbend Scenario Laboratory — Guided Local Preview": "Riverbend Scenario Laboratory — Hosted Synthetic Preview",
        "Local-only, fictional CivicOS governance simulator.": "Fictional CivicOS governance simulator; hosted synthetic demonstration.",
        "Development preview only.": "Synthetic demonstration only.",
        "This local application is not the public beta or an official civic service.": "This hosted sandbox is not an official civic service.",
        "A local Python process runs": "A bounded hosted worker process runs",
        "Local development evidence only · No telemetry, real civic records or external API calls. No public sharing service.":
            "Synthetic hosted laboratory · No user accounts or stored scenarios. Our host may process network metadata. No real civic records, analytics scripts or public sharing links.",
    },
    "lab.js": {
        "Local engine unavailable: ": "Simulator unavailable: ",
        "The local simulation failed.": "The simulation failed.",
    },
    "experience.js": {
        "ACECOG-LOCAL-EXPERIMENT-EVIDENCE-v0.2": "ACECOG-BG2-EXPERIMENT-EVIDENCE-v0.2",
        "ACECOG-LOCAL-SCENARIO-RECIPE-v0.2": "ACECOG-BG2-SCENARIO-RECIPE-v0.2",
        "FICTIONAL_LOCAL_ONLY_NO_LEGAL_EFFECT": "FICTIONAL_ADVISORY_NO_LEGAL_EFFECT",
        "Results came from the local CivicOS engine. Export or copy deliberately; nothing was saved remotely.":
            "Results came from a hosted synthetic CivicOS worker. No scenario history is stored by this app; hosting logs may include connection metadata.",
        "Scenario recipe copied. Paste it into a file or message; no data was uploaded.":
            "Scenario recipe copied. Paste it deliberately; this copy action did not upload new data.",
        "Local evidence export prepared.": "Evidence export prepared.",
    },
}


def make_assets(dest: Path = DEST) -> None:
    dest.mkdir(parents=True, exist_ok=True)
    for name in ("index.html", "lab.js", "lab.css", "experience.js"):
        text = (SOURCE / name).read_text(encoding="utf-8")
        for old, new in COMMON.get(name, {}).items():
            if text.count(old) != 1:
                raise RuntimeError(f"Hosting copy contract drift: {name} missing or repeated marker {old!r}")
            text = text.replace(old, new, 1)
        (dest / name).write_text(text, encoding="utf-8")
    html = (dest / "index.html").read_text(encoding="utf-8")
    if "Development preview only" in html or "A local Python process" in html:
        raise RuntimeError("Unsafe local-only wording remained in hosted HTML")
    if not all((dest / a).is_file() for a in ("lab.js", "experience.js", "lab.css")):
        raise RuntimeError("Hosted assets incomplete")


if __name__ == "__main__":
    try:
        make_assets()
    except RuntimeError as ex:
        sys.exit(str(ex))
