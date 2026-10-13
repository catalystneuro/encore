"""Tests for tools/build_site.py: the dashboard built from the registry's files."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "tools"))

import build_site as site  # noqa: E402

OUTCOMES = [{"claim": "a", "outcome": "reproduced"}, {"claim": "b", "outcome": "blocked"}]


def verification(kind, agreed):
    return {"date": "2026-10-13", "kind": kind,
            "results": [{"claim": c, "agrees": c in agreed} for c in ("a", "b")]}


def test_an_unverified_attempt_only_runs():
    assert site.tier_of({"outcomes": OUTCOMES}) == "runs"


def test_the_latest_verification_decides_the_tier():
    attempt = {"outcomes": OUTCOMES,
               "verifications": [verification("agent", {"a"}), verification("agent", {"a", "b"})]}
    assert site.tier_of(attempt) == "agent_verified"
    attempt["verifications"].append(verification("person", {"a", "b"}))
    assert site.tier_of(attempt) == "human_verified"


def test_a_verification_that_disagrees_on_any_claim_does_not_count():
    attempt = {"outcomes": OUTCOMES,
               "verifications": [verification("agent", {"a", "b"}), verification("person", {"a"})]}
    assert site.tier_of(attempt) == "runs"


def broken_links(root: Path) -> list[str]:
    """Internal links and anchors in the built site that do not resolve."""
    ids = {}
    pages = sorted(root.rglob("*.html"))
    for page in pages:
        ids[page] = set(re.findall(r'\bid="([^"]+)"', page.read_text()))
    broken = []
    for page in pages:
        for href in re.findall(r'<a\b[^>]*\bhref="([^"]+)"', page.read_text()):
            href = href.replace("&amp;", "&")
            if re.match(r"[a-z]+:", href):
                continue                                   # external
            path, _, fragment = href.partition("#")
            path = path.split("?")[0]
            target = (page.parent / path).resolve() if path else page.resolve()
            if target.is_dir():
                target = target / "index.html"
            if not target.is_file():
                broken.append(f"{page.relative_to(root)}: {href}")
            elif fragment and target.suffix == ".html" and fragment not in ids.get(target, ids.get(
                    next((p for p in pages if p.resolve() == target), page), set())):
                broken.append(f"{page.relative_to(root)}: {href} (no such anchor)")
    return broken


@pytest.fixture(scope="module")
def built(tmp_path_factory):
    out = tmp_path_factory.mktemp("site")
    data = site.collect()
    site.build(data, out)
    return data, out


def test_every_page_is_built(built):
    data, out = built
    for page in ("index.html", "dandisets/index.html", "claims/index.html", "findings/index.html",
                 "assets/app.css", "assets/list.js", "registry.json"):
        assert (out / page).is_file(), page
    for dandiset in {a["dandiset"] for a in data["attempts"]}:
        assert (out / "dandisets" / dandiset / "index.html").is_file()
        api = json.loads((out / "api" / "dandiset" / f"{dandiset}.json").read_text())
        assert api["dandiset"] == dandiset and "caution" in api


def test_rows_match_the_attempts(built):
    data, out = built
    latest = site.latest_attempts(data)
    rows = {kind: json.loads((out / "data" / f"{kind}.json").read_text()) for kind in site.LISTS}
    assert len(rows["dandisets"]) == data["queue_counts"]["with_a_paper"]
    assert len(rows["claims"]) == sum(len(a["outcomes"]) for a in latest.values())
    assert len(rows["findings"]) == sum(len(a["findings"]) for a in latest.values())
    assert sum(1 for r in rows["dandisets"] if r["status"] == "attempted") == len(latest)


def test_no_internal_link_is_broken(built):
    _, out = built
    assert broken_links(out) == []


def test_pages_load_nothing_from_other_sites(built):
    _, out = built
    for page in out.rglob("*.html"):
        text = page.read_text()
        assert "<script src=\"http" not in text and "<link rel=\"stylesheet\" href=\"http" not in text


def test_every_claim_has_an_anchor_on_its_dandiset_page(built):
    data, out = built
    for dandiset, attempt in site.latest_attempts(data).items():
        page = (out / "dandisets" / dandiset / "index.html").read_text()
        for outcome in attempt["outcomes"]:
            assert f'id="claim-{outcome["claim"]}"' in page
        assert site.CAUTION in page or not any(
            o["outcome"] in ("not_reproduced", "partially_reproduced") for o in attempt["outcomes"])


def test_the_overview_stays_small_at_scale(tmp_path):
    data = site.demo(site.collect(), 150)
    site.build(data, tmp_path)
    assert len(list((tmp_path / "dandisets").glob("*/index.html"))) == 150
    assert (tmp_path / "index.html").stat().st_size < 100_000
    assert "Demo data" in (tmp_path / "index.html").read_text()
    assert broken_links(tmp_path) == []
