"""Public beta site (WBS 1.7.2): the promises the site makes are checked on every change (beta gate BG-1)."""
import glob, hashlib, json, os, re, sys
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts"))
import build_site  # noqa: E402

D = build_site.build()
OUT = build_site.OUT


def test_every_page_says_synthetic_and_no_legal_effect():   # PUB-009
    for f in glob.glob(os.path.join(OUT, "*.html")):
        text = open(f, encoding="utf-8").read()
        assert "fictional community, and nothing on this site has legal effect" in text, f
        assert "Binding" not in text, f


def test_no_automatic_third_party_resources_or_forms():
    # The founder-approved GitHub privacy-policy hyperlink is clicked only
    # by a visitor; it does not load any third-party runtime dependency.
    for f in glob.glob(os.path.join(OUT, "*.html")) + glob.glob(os.path.join(OUT, "*.css")) + glob.glob(os.path.join(OUT, "*.js")):
        text = open(f, encoding="utf-8").read()
        assert not re.search(r"(?:src|action)=[\\\"']?https?://", text), f
        assert not any(token in text for token in ('url(https://', 'url(http://',
                    'url("https://', 'url("http://', "url('https://", "url('http://")), f
        assert "<form" not in text and "document.cookie" not in text, f
    about = (Path(OUT) / "about.html").read_text(encoding="utf-8")
    url = "https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement"
    assert url in about
    assert about.count('href="https://') == 1


def test_owner_approved_public_notice_without_private_review_notes():
    about = (Path(OUT) / "about.html").read_text(encoding="utf-8")
    for phrase in ("Accelerated Ecological Governance", "morgan@acecog.org",
                   "synthetic", "Advisory", "no legal effect", "GitHub Pages",
                   "record checker", "Privacy Statement"):
        assert phrase in about
    for private in ("Internal integration and assurance notes",
                    "provisional internal approval", "counsel sign-off"):
        assert private not in about


def test_published_record_verifies_from_its_bytes():       # ASR-04, as a visitor's browser checks it
    rec = json.load(open(os.path.join(OUT, "events.json"), encoding="utf-8"))
    prev = "0" * 64
    for ev in rec["events"]:
        assert json.loads(ev["text"])["prev_hash"] == prev
        assert hashlib.sha256((prev + ev["text"]).encode()).hexdigest() == ev["hash"]
        prev = ev["hash"]
    assert prev == rec["chain_head"] == D["chain_head"]


def test_walkthrough_numbers_come_from_the_engine():       # PUB-001, PUB-015
    index = open(os.path.join(OUT, "index.html"), encoding="utf-8").read()
    assert D["replay"]["reproduced"] and D["replay"]["replayed_result_hash"] in index
    t = D["dec"]["tally"]
    assert f"{t['participating']} of {t['eligible']} members take part" in index
