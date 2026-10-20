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
    for page in ("index.html", "datasets/index.html",
                 "assets/app.css", "assets/list.js", "assets/favicon.svg", "assets/favicon-32.png",
                 "assets/favicon-180.png", "registry.json"):
        assert (out / page).is_file(), page
    for dandiset in {a["key"] for a in data["attempts"]}:
        assert (out / site.page_of(dandiset) / "index.html").is_file()
        api = json.loads((out / "api" / f"{site.page_of(dandiset).rstrip('/')}.json").read_text())
        assert site.key_of(api["dataset"]["archive"], api["dataset"]["id"]) == dandiset and "caution" in api
        assert api["attempts"] and "entries" in api


def test_rows_match_the_attempts(built):
    data, out = built
    current = site.current_attempts(data)
    attempts = [a for atts in current.values() for a in atts if not a.get("deprecated")]
    rows = {kind: json.loads((out / "data" / f"{kind}.json").read_text()) for kind in site.LISTS}
    assert len(rows["datasets"]) == data["queue_counts"]["with_a_paper"]
    assert sum(r["claims"] or 0 for r in rows["datasets"]) == sum(len(a["outcomes"]) for a in attempts)
    assert sum(r["findings"] or 0 for r in rows["datasets"]) == sum(len(a["findings"]) for a in attempts)
    assert sum(1 for r in rows["datasets"] if r["status"] == "attempted") == len(current)


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
        page = (out / site.page_of(dandiset) / "index.html").read_text()
        for attempt in attempts:
            for outcome in attempt["outcomes"]:
                assert f'id="claim-{outcome["claim"]}"' in page


def test_the_caution_is_on_the_overview_and_not_on_dandiset_pages(built):
    data, out = built
    assert site.CAUTION in (out / "index.html").read_text()
    for dandiset in site.current_attempts(data):
        assert site.CAUTION not in (out / site.page_of(dandiset) / "index.html").read_text()


def test_a_dandiset_page_lists_every_notebook_of_every_entry_that_uses_it(built):
    data, out = built
    for dandiset in site.current_attempts(data):
        page = (out / site.page_of(dandiset) / "index.html").read_text()
        entries = site.entries_for(data, dandiset)
        assert entries, dandiset
        for entry in entries:
            for notebook in entry["notebooks"]:
                assert notebook["path"] in page
        assert "Open the executed notebook" not in page


def test_a_dandiset_can_have_attempts_on_several_papers():
    def attempt(i, paper, date):
        return {"id": f"x-{i}", "key": "dandi:000001", "paper": paper, "date": date, "tier": "runs",
                "outcomes": [{"claim": f"c{i}", "outcome": "reproduced"}], "findings": []}
    data = {"attempts": [attempt(1, "10.1/a", "2026-01-01"), attempt(2, "10.1/b", "2026-01-02"),
                         attempt(3, "10.1/a", "2026-01-03")]}
    current = site.current_attempts(data)["dandi:000001"]
    assert [a["id"] for a in current] == ["x-2", "x-3"]          # the latest per paper
    assert site.outcome_counts(current)["reproduced"] == 2


def test_the_overview_stays_small_at_scale(tmp_path):
    data = site.demo(site.collect(), 150)
    site.build(data, tmp_path)
    assert len(list((tmp_path / "datasets" / "dandi").glob("*/index.html"))) == 150
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
    for page in list(out.glob("*.html")) + list(out.glob("*/index.html")) + list(out.glob("datasets/*/*/index.html")):
        text = page.read_text()
        if 'http-equiv="refresh"' in text:      # a redirect from where a page used to be
            continue
        href = re.search(r'<link rel="icon" href="([^"]+)"', text).group(1)
        assert (page.parent / href).resolve().is_file(), page


def test_findings_are_reached_from_the_dandisets_list(built):
    data, out = built
    assert not (out / "findings").exists() and not (out / "claims").exists()
    rows = json.loads((out / "data" / "dandisets.json").read_text())
    for dandiset, attempts in site.current_attempts(data).items():
        row = next(r for r in rows if r["id"] == dandiset)
        attempts = [a for a in attempts if not a.get("deprecated")]
        assert row["findings"] == sum(len(a["findings"]) for a in attempts)
        assert row["found"] == sorted({f["kind"] for a in attempts for f in a["findings"]})
        assert 'id="findings"' in (out / row["page"] / "index.html").read_text()
    assert "#findings" in (REPO / "tools" / "site_assets" / "list.js").read_text()



def test_the_pipeline_chart_has_a_bar_per_step_whose_segments_sum_to_the_targets():
    counts = {key: {"done": 3, "waiting": 1} if key == "paper" else {"todo": 2, "none": 2}
              for key, _ in site.PIPELINE_STEPS}
    chart = site.pipeline_chart(counts, 4)
    assert chart.count('class="frow"') == len(site.CHART_STEPS)
    assert 'class="seg st-done" style="width:75.00%"' in chart and 'class="seg st-waiting" style="width:25.00%"' in chart
    assert 'aria-label="Paper: 3 of 4 done, 1 waiting on a person"' in chart


def test_the_chart_counts_a_step_not_reached_as_to_do_and_old_claims_as_made_before_checks():
    assert site.chart_state("verified", "none", "") == "todo"
    assert site.chart_state("check", "none", "before checks") == "older"
    assert site.chart_state("paper", "waiting", "not in store") == "waiting"

def test_the_pipeline_has_a_row_per_target(built):
    data, out = built
    rows = json.loads((out / "data" / "pipeline.json").read_text())
    assert [r["key"] for r in rows] == [t["key"] for t in data["targets"]]
    steps = [key for key, _ in site.PIPELINE_STEPS]
    states = {"done", "waiting", "todo", "deprecated", "none"}
    assert all(set(r["state"]) == set(steps) and {v[0] for v in r["state"].values()} <= states for r in rows)
    for dandiset, attempts in site.current_attempts(data).items():
        row = next(r for r in rows if r["key"] == dandiset)
        if any(a.get("deprecated") for a in attempts):
            assert row["state"]["attempt"][0] == "deprecated" and row["state"]["claims"][0] == "todo"
        else:
            assert row["state"]["attempt"][0] == "done"
    assert "Pipeline" in (out / "pipeline" / "index.html").read_text()


def test_a_deprecated_attempt_counts_for_nothing():
    kept = {"outcomes": [{"claim": "a", "outcome": "reproduced"}]}
    dropped = {"deprecated": "Claims written from the abstract only.",
               "outcomes": [{"claim": "b", "outcome": "not_reproduced"}]}
    counts = site.outcome_counts([kept, dropped])
    assert counts["reproduced"] == 1 and counts["not_reproduced"] == 0
    assert site.outcome_counts(dropped) == {k: 0 for k in site.OUTCOMES}


def test_a_deprecated_attempt_is_marked_on_its_page(built):
    data, out = built
    for dandiset, attempts in site.current_attempts(data).items():
        if any(a.get("deprecated") for a in attempts):
            assert "Deprecated:" in (out / site.page_of(dandiset) / "index.html").read_text()



def test_an_earlier_attempt_has_its_own_page_linked_from_the_dandiset(built):
    data, out = built
    pages = 0
    for dandiset in site.current_attempts(data):
        for a in site.earlier_attempts(data, dandiset):
            pages += 1
            current = (out / site.page_of(dandiset) / "index.html").read_text()
            assert f'href="../../../{site.page_of(dandiset)}{a["id"]}/"' in current
            page = (out / site.page_of(dandiset) / a["id"] / "index.html").read_text()
            assert "An earlier attempt." in page and f'href="../../../../{site.page_of(dandiset)}"' in page
            for o in a["outcomes"]:
                assert f'id="claim-{o["claim"]}" data-outcome="{o["outcome"]}"' in page
    assert pages

def test_claims_using_outside_data_are_counted_apart():
    attempt = {"outcomes": [{"claim": "a", "outcome": "reproduced", "data": "dataset"},
                            {"claim": "b", "outcome": "not_reproduced", "data": "with_inputs"},
                            {"claim": "c", "outcome": "blocked"}]}
    alone, outside = site.outcome_counts(attempt), site.outcome_counts(attempt, "with_inputs")
    assert alone["reproduced"] == 1 and alone["blocked"] == 1 and alone["not_reproduced"] == 0
    assert outside["not_reproduced"] == 1 and sum(outside.values()) == 1
    assert "1 claim that also uses data" in site.outside_note([attempt])


def test_claims_are_accordions_grouped_by_notebook_with_a_filter(built):
    data, out = built
    for dandiset, attempts in site.current_attempts(data).items():
        page = (out / site.page_of(dandiset) / "index.html").read_text()
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
    attempt = {"outcomes": [{"claim": "a", "outcome": "reproduced", "data": "dataset"},
                            {"claim": "b", "outcome": "blocked", "data": "elsewhere"},
                            {"claim": "c", "outcome": "reproduced", "data": "with_inputs"}]}
    assert sum(site.outcome_counts(attempt).values()) == 1
    assert site.outcome_counts(attempt, "elsewhere")["blocked"] == 1
    assert sum(site.outcome_counts(attempt, "with_inputs").values()) == 1
    note = site.outside_note([attempt])
    assert "1 claim on data the paper deposited in another archive" in note
    assert "1 claim that also uses data from outside the dataset" in note


def test_dandisets_converted_by_catalystneuro_can_be_filtered(built):
    data, out = built
    rows = json.loads((out / "data" / "dandisets.json").read_text())
    ours = {t["key"] for t in data["targets"] if t["catalystneuro"]}
    assert ours and {r["id"] for r in rows if r["converted"] == "catalystneuro"} == ours
    assert ("converted", "Converted by") in site.LISTS["datasets"]["facets"]


def test_the_dashboard_counts_each_dandiset_from_its_first_attempt():
    claims = [{"claim": "a", "outcome": "reproduced", "data": "dataset"}]
    data = {"targets": [{"key": "dandi:000001", "catalystneuro": ["repo"]}, {"key": "dandi:000002", "catalystneuro": []}],
            "attempts": [
                {"id": "x-01", "key": "dandi:000001", "paper": "p1", "date": "2026-10-13", "outcomes": claims, "findings": []},
                {"id": "y-01", "key": "dandi:000002", "paper": "p2", "date": "2026-10-13", "outcomes": claims,
                 "findings": [{"kind": "other"}]},
                {"id": "x-02", "key": "dandi:000001", "paper": "p1", "date": "2026-10-15", "outcomes": claims * 2,
                 "findings": []}]}
    p = site.progress_data(data)
    assert p["days"] == ["2026-10-13", "2026-10-14", "2026-10-15"]
    every = p["series"]["all"]
    assert every["datasets"] == [2, 0, 0] and every["attempts"] == [2, 0, 1]
    # Claims and findings come from each dandiset's current attempt, on its date.
    assert every["claims"] == [1, 0, 2] and every["findings"] == [1, 0, 0]
    assert p["series"]["catalystneuro"]["datasets"] == [1, 0, 0]
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
    page = (out / site.page_of(dandiset) / "index.html").read_text()
    assert (f'<a href="https://dandiarchive.org/dandiset/{site.split_key(dandiset)[1]}" target="_blank" '
            f'rel="noopener">View on DANDI</a>' in page)


def test_pages_carry_a_description_canonical_link_and_social_card(built):
    data, out = built
    home = (out / "index.html").read_text()
    assert f'<link rel="canonical" href="{site.SITE_URL}">' in home
    assert f'<meta property="og:image" content="{site.SITE_URL}assets/social-card.png">' in home
    assert '"@type": "WebSite"' in home and 'name="robots"' not in home
    assert (out / "assets" / "social-card.png").is_file()
    dandiset = next(iter(site.current_attempts(data)))
    page = (out / site.page_of(dandiset) / "index.html").read_text()
    assert f'href="{site.SITE_URL}{site.page_of(dandiset)}"' in page and "claims tested" in page


def test_the_sitemap_lists_every_dandiset_page(built):
    data, out = built
    sitemap = (out / "sitemap.xml").read_text()
    for dandiset in site.current_attempts(data):
        assert f"<loc>{site.SITE_URL}{site.page_of(dandiset)}</loc>" in sitemap


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
    assert site.p_text(0) == "0"
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


def test_link_claims_are_counted_apart_from_the_papers_findings():
    attempt = {"outcomes": [{"claim": "a", "outcome": "reproduced", "data": "dataset"},
                            {"claim": "l", "outcome": "reproduced", "data": "with_inputs", "kind": "link"},
                            {"claim": "w", "outcome": "blocked", "data": "with_inputs"}]}
    assert sum(site.outcome_counts(attempt).values()) == 1
    assert sum(site.outcome_counts(attempt, "with_inputs").values()) == 1
    assert site.outcome_counts(attempt, "link")["reproduced"] == 1
    assert "1 check that the dataset is the data behind the paper" in site.outside_note([attempt])


def test_a_claim_not_stated_in_the_paper_says_it_is_inferred():
    claim = {"claim": "t", "statement": "Few respond.", "source": "Table S1", "inferred": "Numbers from Table S1.",
             "outcome": "reproduced", "blocked_by": None, "notes": "N.", "deviations": [], "disagreed": False}
    html = site.claim_item(claim, "../")
    assert '<p class="inferred"><strong>Not quoted:</strong> Numbers from Table S1.</p>' in html
    link = site.claim_item({**claim, "inferred": None, "kind": "link"}, "../")
    assert "checks the link to the paper’s data" in link


def test_the_schema_keeps_quotes_inferences_and_links_apart():
    from jsonschema import Draft202012Validator
    schema = Draft202012Validator(json.loads((REPO / "schemas" / "claims.schema.json").read_text()))
    base = {"schema_version": 2, "dataset": {"archive": "dandi", "id": "000001"}, "paper": "doi:10.1000/x"}
    claim = {"id": "a", "statement": "S.", "source": "Figure 1"}
    assert schema.is_valid({**base, "claims": [{**claim, "quote": "Q."}]})
    assert schema.is_valid({**base, "claims": [{**claim, "inferred": "From Table 1."}]})
    assert not schema.is_valid({**base, "claims": [{**claim, "quote": "Q.", "inferred": "From Table 1."}]})
    assert not schema.is_valid({**base, "claims": [{**claim, "kind": "link", "inferred": "From code."}]})
    assert schema.is_valid({**base, "claims": [{**claim, "statistics": [{"p": 0}]}]})


def test_old_dandiset_links_redirect_to_the_dataset_pages(built):
    data, out = built
    for key in site.current_attempts(data):
        old = (out / "dandisets" / site.split_key(key)[1] / "index.html").read_text()
        assert f'url=../../{site.page_of(key)}"' in old
        for a in site.earlier_attempts(data, key):
            moved = (out / "dandisets" / site.split_key(key)[1] / a["id"] / "index.html").read_text()
            assert f'url=../../../{site.page_of(key)}{a["id"]}/"' in moved
    assert 'url=../datasets/"' in (out / "dandisets" / "index.html").read_text()


def test_datasets_are_named_by_archive_and_id():
    assert site.dataset_label("dandi:000003") == "DANDI:000003"
    assert site.page_of("dandi:000003") == "datasets/dandi/000003/"
    assert site.dir_of("dandi:000003") == "000003" and site.dir_of("ebrains:abc") == "ebrains-abc"
    assert site.key_of_dir("000003") == "dandi:000003" and site.key_of_dir("ebrains-abc") == "ebrains:abc"
