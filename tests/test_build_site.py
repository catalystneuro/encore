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


def test_claims_using_outside_data_are_counted_apart():
    attempt = {"outcomes": [{"claim": "a", "outcome": "reproduced", "data": "dandiset"},
                            {"claim": "b", "outcome": "not_reproduced", "data": "with_inputs"},
                            {"claim": "c", "outcome": "blocked"}]}
    alone, outside = site.outcome_counts(attempt), site.outcome_counts(attempt, "with_inputs")
    assert alone["reproduced"] == 1 and alone["blocked"] == 1 and alone["not_reproduced"] == 0
    assert outside["not_reproduced"] == 1 and sum(outside.values()) == 1
    assert "1 claim that also uses data" in site.outside_note([attempt])


def test_claims_are_accordions_grouped_by_notebook_with_a_filter(built):
    data, out = built
    for dandiset, attempts in site.current_attempts(data).items():
        page = (out / "dandisets" / dandiset / "index.html").read_text()
        assert 'id="claim-filter"' in page and 'id="claim-pager"' in page
        for attempt in attempts:
            for o in attempt["outcomes"]:
                assert f'id="claim-{o["claim"]}" data-outcome="{o["outcome"]}"><details><summary>' in page
            for nb in attempt["notebooks"]:
                if any(o.get("notebook") == nb["path"] for o in attempt["outcomes"]):
                    assert f'Notebook <code>{nb["path"]}</code>' in page


def test_claims_with_outside_names_count_as_the_dandiset():
    attempt = {"outcomes": [{"claim": "a", "outcome": "reproduced", "data": "with_labels"},
                            {"claim": "b", "outcome": "reproduced", "data": "with_inputs"}]}
    assert site.outcome_counts(attempt)["reproduced"] == 1
    assert site.outcome_counts(attempt, "with_inputs")["reproduced"] == 1


def test_claims_on_data_in_other_archives_are_counted_on_their_own():
    attempt = {"outcomes": [{"claim": "a", "outcome": "reproduced", "data": "dandiset"},
                            {"claim": "b", "outcome": "blocked", "data": "elsewhere"},
                            {"claim": "c", "outcome": "reproduced", "data": "with_inputs"}]}
    assert sum(site.outcome_counts(attempt).values()) == 1
    assert site.outcome_counts(attempt, "elsewhere")["blocked"] == 1
    assert sum(site.outcome_counts(attempt, "with_inputs").values()) == 1
    note = site.outside_note([attempt])
    assert "1 claim on data the paper deposited in another archive" in note
    assert "1 claim that also uses data from outside the dandiset" in note


def test_dandisets_converted_by_catalystneuro_can_be_filtered(built):
    data, out = built
    rows = json.loads((out / "data" / "dandisets.json").read_text())
    ours = {t["dandiset"] for t in data["targets"] if t["catalystneuro"]}
    assert ours and {r["id"] for r in rows if r["converted"] == "catalystneuro"} == ours
    assert ("converted", "Converted by") in site.LISTS["dandisets"]["facets"]


def test_the_dashboard_counts_each_dandiset_from_its_first_attempt():
    claims = [{"claim": "a", "outcome": "reproduced", "data": "dandiset"}]
    data = {"targets": [{"dandiset": "000001", "catalystneuro": ["repo"]}, {"dandiset": "000002", "catalystneuro": []}],
            "attempts": [
                {"id": "x-01", "dandiset": "000001", "paper": "p1", "date": "2026-10-13", "outcomes": claims, "findings": []},
                {"id": "y-01", "dandiset": "000002", "paper": "p2", "date": "2026-10-13", "outcomes": claims,
                 "findings": [{"kind": "other"}]},
                {"id": "x-02", "dandiset": "000001", "paper": "p1", "date": "2026-10-15", "outcomes": claims * 2,
                 "findings": []}]}
    p = site.progress_data(data)
    assert p["days"] == ["2026-10-13", "2026-10-14", "2026-10-15"]
    every = p["series"]["all"]
    assert every["dandisets"] == [2, 0, 0] and every["attempts"] == [2, 0, 1]
    # Claims and findings come from each dandiset's current attempt, on its date.
    assert every["claims"] == [1, 0, 2] and every["findings"] == [1, 0, 0]
    assert p["series"]["catalystneuro"]["dandisets"] == [1, 0, 0]
    assert 'data-metric="findings"' in site.progress_panel(data)


def test_the_overview_shows_the_dashboard(built):
    data, out = built
    if len(site.progress_data(data)["days"]) > 1:
        page = (out / "index.html").read_text()
        assert 'id="progress-data"' in page and "assets/progress.js" in page
        assert (out / "assets" / "progress.js").is_file()


def test_view_on_dandi_opens_a_new_window(built):
    data, out = built
    dandiset = next(iter(site.current_attempts(data)))
    page = (out / "dandisets" / dandiset / "index.html").read_text()
    assert (f'<a href="https://dandiarchive.org/dandiset/{dandiset}" target="_blank" rel="noopener">View on DANDI</a>'
            in page)


def test_pages_carry_a_description_canonical_link_and_social_card(built):
    data, out = built
    home = (out / "index.html").read_text()
    assert f'<link rel="canonical" href="{site.SITE_URL}">' in home
    assert f'<meta property="og:image" content="{site.SITE_URL}assets/social-card.png">' in home
    assert '"@type": "WebSite"' in home and 'name="robots"' not in home
    assert (out / "assets" / "social-card.png").is_file()
    dandiset = next(iter(site.current_attempts(data)))
    page = (out / "dandisets" / dandiset / "index.html").read_text()
    assert f'href="{site.SITE_URL}dandisets/{dandiset}/"' in page and "claims tested" in page


def test_the_sitemap_lists_every_dandiset_page(built):
    data, out = built
    sitemap = (out / "sitemap.xml").read_text()
    for dandiset in site.current_attempts(data):
        assert f"<loc>{site.SITE_URL}dandisets/{dandiset}/</loc>" in sitemap


def test_a_preview_is_kept_out_of_search_results(tmp_path):
    data = site.collect()
    data["noindex"] = True
    site.build(data, tmp_path)
    assert '<meta name="robots" content="noindex">' in (tmp_path / "index.html").read_text()


def test_the_about_page_explains_the_roles_and_is_in_the_nav(built):
    data, out = built
    about = (out / "about" / "index.html").read_text()
    assert "How the registry works" in about and "First verification" in about
    assert 'aria-current="page">About' in about
    assert 'href="about/">About' in (out / "index.html").read_text()
    assert f"<loc>{site.SITE_URL}about/</loc>" in (out / "sitemap.xml").read_text()


def test_a_claim_shows_the_papers_own_words_when_quoted():
    claim = {"claim": "fig2", "statement": "Rates rise.", "source": "Figure 2B", "quote": "Firing rates rose <sharply>.",
             "outcome": "reproduced", "blocked_by": None, "notes": "It rose.", "deviations": [], "disagreed": False}
    html = site.claim_item(claim, "../")
    assert '<blockquote class="quote"><p>Firing rates rose &lt;sharply&gt;.</p><cite>Figure 2B</cite>' in html
    assert html.index("blockquote") < html.index("It rose.")
    assert "blockquote" not in site.claim_item({**claim, "quote": None}, "../")


def test_small_p_values_are_written_as_powers_of_ten():
    assert site.p_text(0.002) == "0.002"
    assert site.p_text(2.4e-5) == "2.4 × 10⁻⁵"
    assert site.p_text(4.9e-4) == "4.9 × 10⁻⁴"
    assert site.p_text(4e-66) == "4 × 10⁻⁶⁶"
    assert site.p_text(1e-10) == "10⁻¹⁰"


def test_a_claim_lists_the_statistics_the_paper_reports():
    stats = [{"about": "Onsets", "test": "Wilcoxon rank-sum", "p": 2.4e-5, "n": "206 and 179 units"},
             {"test": "t-test", "p": 0.05, "p_relation": "<", "corrected": "Bonferroni"},
             {"ci": {"level": 0.95, "low": 0.1, "high": 0.4, "unit": "Hz"}}]
    lines = [site.statistic_text(s) for s in stats]
    assert lines == ["Onsets: Wilcoxon rank-sum, p = 2.4 × 10⁻⁵ (n = 206 and 179 units)",
                     "t-test, p < 0.05, Bonferroni-corrected", "95% CI 0.1 to 0.4 Hz"]
    claim = {"claim": "a", "statement": "S.", "source": None, "statistics": stats, "outcome": "reproduced",
             "blocked_by": None, "notes": "N.", "deviations": [], "disagreed": False}
    html = site.claim_item(claim, "../")
    assert '<ul class="stats"><li>Onsets: Wilcoxon rank-sum' in html and html.index("stats") < html.index("N.")
