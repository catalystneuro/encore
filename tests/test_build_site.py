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
    for page in ("index.html", "dandisets/index.html",
                 "assets/app.css", "assets/list.js", "assets/favicon.svg", "assets/favicon-32.png",
                 "assets/favicon-180.png", "registry.json"):
        assert (out / page).is_file(), page
    for dandiset in {a["dandiset"] for a in data["attempts"]}:
        assert (out / "dandisets" / dandiset / "index.html").is_file()
        api = json.loads((out / "api" / "dandiset" / f"{dandiset}.json").read_text())
        assert api["dandiset"] == dandiset and "caution" in api
        assert api["attempts"] and "entries" in api


def test_rows_match_the_attempts(built):
    data, out = built
    current = site.current_attempts(data)
    attempts = [a for atts in current.values() for a in atts]
    rows = {kind: json.loads((out / "data" / f"{kind}.json").read_text()) for kind in site.LISTS}
    assert len(rows["dandisets"]) == data["queue_counts"]["with_a_paper"]
    assert sum(r["claims"] or 0 for r in rows["dandisets"]) == sum(len(a["outcomes"]) for a in attempts)
    assert sum(r["findings"] or 0 for r in rows["dandisets"]) == sum(len(a["findings"]) for a in attempts)
    assert sum(1 for r in rows["dandisets"] if r["status"] == "attempted") == len(current)


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
    for dandiset, attempts in site.current_attempts(data).items():
        page = (out / "dandisets" / dandiset / "index.html").read_text()
        for attempt in attempts:
            for outcome in attempt["outcomes"]:
                assert f'id="claim-{outcome["claim"]}"' in page


def test_the_caution_is_on_the_overview_and_not_on_dandiset_pages(built):
    data, out = built
    assert site.CAUTION in (out / "index.html").read_text()
    for dandiset in site.current_attempts(data):
        assert site.CAUTION not in (out / "dandisets" / dandiset / "index.html").read_text()


def test_a_dandiset_page_lists_every_notebook_of_every_entry_that_uses_it(built):
    data, out = built
    for dandiset in site.current_attempts(data):
        page = (out / "dandisets" / dandiset / "index.html").read_text()
        entries = site.entries_for(data, dandiset)
        assert entries, dandiset
        for entry in entries:
            for notebook in entry["notebooks"]:
                assert notebook["path"] in page
        assert "Open the executed notebook" not in page


def test_a_dandiset_can_have_attempts_on_several_papers():
    def attempt(i, paper, date):
        return {"id": f"x-{i}", "dandiset": "000001", "paper": paper, "date": date, "tier": "runs",
                "outcomes": [{"claim": f"c{i}", "outcome": "reproduced"}], "findings": []}
    data = {"attempts": [attempt(1, "10.1/a", "2026-01-01"), attempt(2, "10.1/b", "2026-01-02"),
                         attempt(3, "10.1/a", "2026-01-03")]}
    current = site.current_attempts(data)["000001"]
    assert [a["id"] for a in current] == ["x-2", "x-3"]          # the latest per paper
    assert site.outcome_counts(current)["reproduced"] == 2


def test_the_overview_stays_small_at_scale(tmp_path):
    data = site.demo(site.collect(), 150)
    site.build(data, tmp_path)
    assert len(list((tmp_path / "dandisets").glob("*/index.html"))) == 150
    assert (tmp_path / "index.html").stat().st_size < 100_000
    assert "Demo data" in (tmp_path / "index.html").read_text()
    assert broken_links(tmp_path) == []


@pytest.mark.parametrize("gb, text", [(38464.5, "38.5 TB"), (1379.1, "1.4 TB"), (352.1, "352 GB"),
                                      (17.2, "17.2 GB"), (1.86, "1.9 GB"), (0.05, "50.0 MB"), (0.57, "570 MB")])
def test_sizes_are_shown_in_a_readable_unit(gb, text):
    assert site.human_size(gb) == text


@pytest.mark.parametrize("n, text", [(40982, "41k files"), (3855, "3,855 files"), (1, "1 file"),
                                     (1234567, "1.2M files")])
def test_file_counts_are_shortened_when_large(n, text):
    assert site.human_count(n, "file") == text


def test_every_page_declares_the_favicon(built):
    _, out = built
    for page in list(out.glob("*.html")) + list(out.glob("*/index.html")) + list(out.glob("dandisets/*/index.html")):
        href = re.search(r'<link rel="icon" href="([^"]+)"', page.read_text()).group(1)
        assert (page.parent / href).resolve().is_file(), page


def test_findings_are_reached_from_the_dandisets_list(built):
    data, out = built
    assert not (out / "findings").exists() and not (out / "claims").exists()
    rows = json.loads((out / "data" / "dandisets.json").read_text())
    for dandiset, attempts in site.current_attempts(data).items():
        row = next(r for r in rows if r["id"] == dandiset)
        assert row["findings"] == sum(len(a["findings"]) for a in attempts)
        assert row["found"] == sorted({f["kind"] for a in attempts for f in a["findings"]})
        assert 'id="findings"' in (out / row["page"] / "index.html").read_text()
    assert "#findings" in (REPO / "tools" / "site_assets" / "list.js").read_text()
