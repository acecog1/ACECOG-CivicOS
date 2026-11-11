"""Public beta site (WBS 1.7.2): the promises the site makes are checked on every change (beta gate BG-1)."""
import glob, hashlib, json, os, re, sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts"))
import build_site  # noqa: E402

D = build_site.build()
OUT = build_site.OUT


def test_every_page_says_synthetic_and_no_legal_effect():   # PUB-009
    for f in glob.glob(os.path.join(OUT, "*.html")):
        text = open(f, encoding="utf-8").read()
        assert "fictional community, and nothing on this site has legal effect" in text, f
        assert "Binding" not in text, f


def test_no_third_party_requests_and_no_forms():           # privacy promise on the About page
    for f in glob.glob(os.path.join(OUT, "*.html")) + glob.glob(os.path.join(OUT, "*.css")) + glob.glob(os.path.join(OUT, "*.js")):
        text = open(f, encoding="utf-8").read()
        assert not re.search(r"(src|href)=[\"']?https?://", text), f
        assert not re.search(r"url\(\s*[\"']?https?://", text), f
        assert "<form" not in text and "document.cookie" not in text, f


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
