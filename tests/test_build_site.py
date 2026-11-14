"""Tests for tools/build_site.py: the dashboard built from the registry's files."""

from __future__ import annotations

import html
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
    pages = sorted(root.rglob("*.html"))
    texts = {page: page.read_text() for page in pages}
    # Each page's anchors, by its resolved path, which is how links are resolved below.
    ids = {page.resolve(): set(re.findall(r'\bid="([^"]+)"', text)) for page, text in texts.items()}
    found: dict[Path, Path | None] = {}   # a resolved link -> the file it reaches, or None

    def reach(target: Path) -> Path | None:
        if target not in found:
            file = target / "index.html" if target.is_dir() else target
            found[target] = file if file.is_file() else None
        return found[target]

    broken = []
    for page, text in texts.items():
        for href in re.findall(r'<a\b[^>]*\bhref="([^"]+)"', text):
            href = href.replace("&amp;", "&")
            if re.match(r"[a-z]+:", href):
                continue                                   # external
            path, _, fragment = href.partition("#")
            path = path.split("?")[0]
            if path.startswith("/"):                       # from the site's root (the 404 page)
                target = reach((root / path.lstrip("/")).resolve())
            else:
                target = reach((page.parent / path).resolve() if path else page.resolve())
            if target is None:
                broken.append(f"{page.relative_to(root)}: {href}")
            elif fragment and target.suffix == ".html" and fragment not in ids.get(target, set()):
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
        assert site.BEACON_SRC not in text   # no analytics token was given


def test_page_views_are_counted_only_on_the_published_site():
    data = {"demo": False, "noindex": False, "analytics": "abc123"}
    assert 'data-cf-beacon=\'{&quot;token&quot;: &quot;abc123&quot;}\'' in site.beacon(data)
    assert site.beacon({**data, "analytics": ""}) == ""
    assert site.beacon({**data, "noindex": True}) == ""
    assert site.beacon({**data, "demo": True}) == ""


def test_crawlers_get_the_sitemap_and_skip_the_previews(built):
    _, out = built
    robots = (out / "robots.txt").read_text()
    assert "Disallow: /pr-preview/" in robots and f"Sitemap: {site.SITE_URL}sitemap.xml" in robots
    assert site.robots({"demo": False, "noindex": True}) == "User-agent: *\nDisallow: /\n"


def test_the_not_found_page_works_at_any_depth_and_is_not_indexed(built):
    _, out = built
    text = (out / "404.html").read_text()
    assert '<meta name="robots" content="noindex">' in text
    assert 'href="/assets/' in text and 'href="/datasets/"' in text


def _paper_page(data, out, attempt):
    """The page of the paper an attempt is on: claims belong to the paper."""
    q = next(q for q in site.papers_of(data) if q["doi"] == attempt["paper"].lower() and q["attempts"])
    return (out / "papers" / q["key"] / "index.html").read_text()


def test_every_claim_has_an_anchor_on_its_papers_page_and_none_on_a_datasets(built):
    data, out = built
    for dandiset, attempts in site.current_attempts(data).items():
        dataset_page = (out / site.page_of(dandiset) / "index.html").read_text()
        assert 'id="claim-' not in dataset_page
        for attempt in attempts:
            page = _paper_page(data, out, attempt)
            for outcome in attempt["outcomes"]:
                assert f'id="claim-{outcome["claim"]}"' in page


def test_the_caution_is_on_the_overview_and_not_on_dandiset_pages(built):
    data, out = built
    assert site.CAUTION in (out / "index.html").read_text()
    for dandiset in site.current_attempts(data):
        assert site.CAUTION not in (out / site.page_of(dandiset) / "index.html").read_text()


def test_the_caution_shows_its_lead_and_keeps_the_rest_behind_a_disclosure(built):
    _, out = built
    home = (out / "index.html").read_text()
    block = home[home.index('<div class="caution" id="caution">'):]
    block = block[:block.index("</details>") + len("</details>")]
    lead, details = block.split("<details>", 1)
    assert site.CAUTION in lead and "It may be a failure of the attempt." in lead
    assert "<details open" not in block
    assert "An outcome says what one attempt could recover" in details
    assert "Most attempts are made by AI agents." in details and site.RESPOND_URL in details
    assert site.CAUTION_JS in home and "#caution" in site.CAUTION_JS


def test_a_papers_page_lists_every_notebook_of_every_entry_that_uses_its_datasets(built):
    data, out = built
    for dandiset, attempts in site.current_attempts(data).items():
        page = _paper_page(data, out, attempts[-1])
        entries = site.entries_for(data, dandiset)
        assert entries, dandiset
        for entry in entries:
            if entry["name"] != attempts[-1]["entry"]:
                continue
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
        assert ((out / href.lstrip("/")) if href.startswith("/") else (page.parent / href)).resolve().is_file(), page


def test_findings_are_on_the_datasets_page_and_counted_in_its_row(built):
    data, out = built
    assert not (out / "findings").exists() and not (out / "claims").exists()
    rows = json.loads((out / "data" / "dandisets.json").read_text())
    for dandiset, attempts in site.current_attempts(data).items():
        row = next(r for r in rows if r["id"] == dandiset)
        attempts = [a for a in attempts if not a.get("deprecated")]
        assert row["findings"] == sum(len(a["findings"]) for a in attempts)
        assert row["found"] == sorted({f["kind"] for a in attempts for f in a["findings"]})
        page = (out / row["page"] / "index.html").read_text()
        assert "Open findings about the data" in page and "Papers tested on this dataset" in page
        for a in attempts:
            for f in a["findings"]:
                assert site.e(f["statement"]) in page
        # The findings are under the version of the dataset they were found on, and the row has what a curator
        # reads: the versions tested, the open findings by kind, and the papers tested.
        assert page.count('<h3 class="vhead">') == len({site.version_text(a) for a in attempts})
        assert all(site.version_text(a) in page for a in attempts)
        assert sum(row["found_counts"].values()) == row["findings"] and sorted(row["found_counts"]) == row["found"]
        assert row["versions"] == list(dict.fromkeys(
            site.version_plain(a) for a in sorted(attempts, key=site.version_order, reverse=True)))
        assert row["n_tested"] == len({a["paper"].lower() for a in attempts})
        assert '<a href="../../../datasets/">Datasets</a> / ' in page


def test_the_pipeline_chart_has_a_bar_per_step_whose_segments_sum_to_the_targets():
    counts = {key: {"done": 3, "waiting": 1} if key == "paper" else {"todo": 2, "none": 2}
              for key, _ in site.PAPER_STEPS}
    chart = site.pipeline_chart(counts, 4)
    assert chart.count('class="frow"') == len(site.CHART_STEPS)
    assert 'class="seg st-done" style="width:75.00%"' in chart and 'class="seg st-waiting" style="width:25.00%"' in chart
    assert 'aria-label="Paper: 3 of 4 done, 1 waiting on a person"' in chart


def test_the_chart_counts_a_step_not_reached_as_to_do_and_old_claims_as_made_before_checks():
    assert site.chart_state("verified", "none", "") == "todo"
    assert site.chart_state("check", "none", "before checks") == "older"
    assert site.chart_state("paper", "waiting", "not in store") == "waiting"


def test_claims_checked_since_an_attempt_was_deprecated_count_as_read_again():
    target = {"key": "dandi:000001", "label": "DANDI:000001", "name": "x"}
    attempt = {"key": "dandi:000001", "paper": "p", "date": "2026-10-01", "id": "x-01", "tier": "runs",
               "deprecated": "From the abstract.", "deprecated_on": "2026-10-20", "outcomes": []}
    def row(check_date):
        data = {"targets": [target], "attempts": [attempt],
                "pipeline": {"papers": {}, "questions": {},
                             "checks": {"dandi:000001": {"ready": True, "date": check_date}}}}
        return site.pipeline_rows(data)[0]["state"]
    old, new = row("2026-10-12"), row("2026-10-21")
    assert old["claims"] == ("todo", "to read again") and old["check"][0] == "todo"
    assert new["claims"] == ("done", "read again") and new["check"] == ("done", "ready")
    assert old["attempt"][0] == new["attempt"][0] == "deprecated"


def test_a_named_paper_the_manifest_has_not_checked_is_not_called_unnamed():
    def paper(target):
        data = {"targets": [{"key": "figshare:1", "label": "FIGSHARE:1", "name": "x", **target}], "attempts": [],
                "pipeline": {"papers": {}, "questions": {}, "checks": {}}}
        return site.pipeline_rows(data)[0]["state"]["paper"]
    assert paper({"papers": ["10.1038/x"]}) == ("waiting", "not checked")
    assert paper({"papers": []}) == ("waiting", "no paper named")

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
            # Its claims are to be read again, until a claims file checked since then is merged.
            assert row["state"]["attempt"][0] == "deprecated"
            assert tuple(row["state"]["claims"]) in (("todo", "to read again"), ("done", "read again"))
        else:
            assert row["state"]["attempt"][0] == "done"
    assert "Pipeline" in (out / "pipeline" / "index.html").read_text()


def test_the_pipeline_says_when_it_was_last_updated(built):
    data, out = built
    page = (out / "pipeline" / "index.html").read_text()
    assert f'<time id="updated" datetime="{data["generated"]}">' in page
    assert "Last updated <time" in page


def test_a_deprecated_attempt_counts_for_nothing():
    kept = {"outcomes": [{"claim": "a", "outcome": "reproduced"}]}
    dropped = {"deprecated": "Claims written from the abstract only.",
               "outcomes": [{"claim": "b", "outcome": "not_reproduced"}]}
    counts = site.outcome_counts([kept, dropped])
    assert counts["reproduced"] == 1 and counts["not_reproduced"] == 0
    assert site.outcome_counts(dropped) == {k: 0 for k in site.OUTCOMES}


def test_an_outcome_reached_outside_the_notebooks_does_not_stop_the_site(tmp_path):
    # A record that gives a tested claim no notebook (andrews-2024 did) must not stop the build: the paper's page
    # lists the claim with those no notebook tests, and says the record names none.
    data = site.collect()
    q = next(q for q in site.papers_of(data) if len(q["attempts"]) == 1 and q["attempts"][0]["notebooks"])
    a = q["attempts"][0]
    moved = next(o for o in a["outcomes"] if o["outcome"] == "reproduced" and o.get("notebook"))
    moved["notebook"] = None
    page = site.page_paper(data, q)
    assert "Not tested in a notebook" in page and "with no notebook named in the record" in page
    assert f'id="claim-{moved["claim"]}"' in page


def test_a_person_has_two_more_badges_with_all_the_outcomes(built):
    data, out = built
    papers = {x["id"]: x for x in json.loads((out / "data" / "papers.json").read_text())}
    seen = none = zeros = 0
    for orcid, author in list(site.author_index(data).items())[:400]:
        counts = {k: sum((papers[q["key"]].get("counts") or {}).get(k, 0) for q in author["papers"]) for k in site.OUTCOMES}
        every = site.author_outcomes(data, author)
        line, card = (out / "badge" / "authors" / f"{orcid}-{kind}.svg" for kind in ("outcomes", "card"))
        api = json.loads((out / "api" / "authors" / f"{orcid}.json").read_text())
        assert (every is None) == (sum(counts.values()) == 0) and line.is_file() == card.is_file() == bool(every)
        assert api["outcome_counts"] == (counts if every else None)
        assert api["badges"] == {"reproduced": (site.author_badge(data, author) or {}).get("svg"),
                                 "outcomes": every["svg_outcomes"] if every else None, "card": every["svg_card"] if every else None}
        if not every:
            none += 1
            continue
        seen += 1
        assert every["counts"] == counts and every["claims"] == sum(counts.values())
        # All four outcomes are on both, by count, a word and a dot in the outcome's colour: one with no claim as 0.
        for svg in (line.read_text(), card.read_text()):
            for k, n in counts.items():
                assert f">{n} {site.OUTCOME_SHORT[k]}</text>" in svg and f'<circle' in svg
                assert f'fill="{site.OUTCOME_FILL[k]}"' in svg
            assert svg.count("<circle") >= 4 and site.e(every["alt"]) in svg
        zeros += any(n == 0 for n in counts.values())
        assert site.e(author["name"]) in card.read_text() and card.read_text().count("<rect") == 1 + sum(1 for n in counts.values() if n)
        page = (out / "authors" / orcid / "index.html").read_text()
        assert every["svg_outcomes"] in page and every["svg_card"] in page and 'class="badge-pick"' in page
    assert seen and none and zeros


def test_a_deprecated_attempt_is_marked_on_its_page(built):
    data, out = built
    for dandiset, attempts in site.current_attempts(data).items():
        for a in attempts:
            if a.get("deprecated"):
                assert "Deprecated:" in _paper_page(data, out, a)


def test_every_attempt_has_a_page_under_its_paper_naming_the_dataset_versions_it_used(built):
    data, out = built
    replaced = several = 0
    for q in site.papers_of(data):
        current = {a["id"] for a in q["attempts"]}
        for a in site.paper_attempts(data, q):
            own = site.attempt_own_path(data, a)
            assert own == f'papers/{q["key"]}/{a["id"]}/'
            page = (out / own / "index.html").read_text()
            if current == {a["id"]}:
                # The paper's one current attempt is read on the paper's page; its address leads there.
                assert site.attempt_path(data, a) == f'papers/{q["key"]}/' and f'url=../../../papers/{q["key"]}/"' in page
                page = (out / "papers" / q["key"] / "index.html").read_text()
                up = "../../"
            else:
                assert site.attempt_path(data, a) == own and f'/ Attempt {a["id"]}</p>' in page
                assert ("An earlier attempt." in page) == (a["id"] not in current)
                replaced += a["id"] not in current
                several += a["id"] in current
                up = "../../../"
                for o in a["outcomes"]:
                    assert (f'id="claim-{o["claim"]}"' if o.get("kind") == "link"
                            else f'id="claim-{o["claim"]}" data-outcome="{o["outcome"]}"') in page
                # The paper's page leads to each of its attempts.
                assert f'href="../../{own}"' in (out / "papers" / q["key"] / "index.html").read_text()
            # An attempt links to every dataset it used, with the version it ran on.
            for x in site.attempt_sets(data, a):
                assert (f'<th scope="row"><a href="{up}{site.page_of(x["key"])}">{x["label"]}</a></th>'
                        f'<td>{site.version_text(x)}</td>') in page
                # And the dataset's page links back to the attempt, unless a later one replaced it there.
                if a["id"] in current:
                    dataset = (out / site.page_of(x["key"]) / "index.html").read_text()
                    assert f'Attempt <a href="../../../{site.attempt_path(data, a)}">{a["id"]}</a> on {site.version_text(x)}' in dataset
    assert replaced and several
    # The attempts behind a paper's results are closed until asked for, under a bar that counts them.
    semenov = (out / "papers" / "semenov-2026" / "index.html").read_text()
    assert '<details class="panel timeline-panel"><summary><h2>Attempts <span class="count">7</span></h2>' in semenov
    assert '<span class="muted small">7 current</span></summary>' in semenov and "timeline-panel\" open" not in semenov
    assert "1 current, 1 replaced</span></summary>" in (out / "papers" / "kim-2022" / "index.html").read_text()
    # An attempt on two datasets names both, each with its version.
    kim = (out / "papers" / "kim-2022" / "index.html").read_text()
    assert "DANDI:000489</a></th><td>version" in kim and "DANDI:000448</a></th><td>version" in kim
    # A dataset of the paper that no attempt used is in the table too, and why is on request.
    assert 'DANDI:000548</a></th><td><span class="muted">not used by an attempt</span>' in kim
    assert '<details class="sets-why"><summary>3 datasets the attempt could not use, and why</summary>' in kim
    # Where an earlier attempt's page was, under its dataset, leads to its page under the paper.
    for dandiset in site.current_attempts(data):
        for a in site.earlier_attempts(data, dandiset):
            old = (out / site.page_of(dandiset) / a["id"] / "index.html").read_text()
            assert f'url=../../../../{site.attempt_own_path(data, a)}"' in old


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
        for attempt in attempts:
            page = _paper_page(data, out, attempt)
            assert 'id="claim-filter"' in page and 'id="claim-pager"' in page
            for o in attempt["outcomes"]:
                if o.get("kind") == "link":   # a check of the link to the paper is under Provenance, not a claim
                    assert f'id="claim-{o["claim"]}"' in page
                    continue
                assert f'id="claim-{o["claim"]}" data-outcome="{o["outcome"]}"><details><summary>' in page
            for nb in attempt["notebooks"]:
                if any(o.get("notebook") == nb["path"] for o in attempt["outcomes"]):
                    assert f'Notebook <code>{nb["path"]}</code>' in page


def test_each_outcome_has_its_own_mark_and_not_reproduced_is_not_a_question_or_a_cross():
    icons = [icon for _, _, icon in site.OUTCOMES.values()]
    assert len(set(icons)) == len(icons)
    assert all("?" not in icon for icon in icons)
    differs = site.OUTCOMES["not_reproduced"][2]
    assert differs == site.DIFFERS_MARK and not any(c in differs for c in "✗✕×!")
    # The mark is decorative: a screen reader hears the label next to it, not the symbol.
    assert 'aria-hidden="true"' in differs
    assert site.chip("not_reproduced").startswith('<span class="chip unresolved"><span class="icon" aria-hidden="true">')
    assert all(f'aria-hidden="true">{icon}</span>' in site.legend({k: 1 for k in site.OUTCOMES}) for icon in icons)


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
    # The overview no longer splits out CatalystNeuro conversions; the datasets page's filter still does.
    assert list(p["series"]) == ["all"]
    panel = site.progress_panel(data)
    assert 'data-metric="findings"' in panel and "data-subset" not in panel
    # Attempts are also counted by protocol version, in version order, with "not recorded" last.
    data["attempts"][0]["agent"] = {"protocol": "pilot-10"}
    data["attempts"][2]["agent"] = {"protocol": "pilot-9"}
    p = site.progress_data(data)
    assert p["protocols"] == ["pilot-9", "pilot-10", "not recorded"]
    every = p["series"]["all"]
    assert every["protocol:pilot-10"] == [1, 0, 0] and every["protocol:pilot-9"] == [0, 0, 1]
    assert every["protocol:not recorded"] == [1, 0, 0]


def test_the_overview_shows_the_dashboard(built):
    data, out = built
    if len(site.progress_data(data)["days"]) > 1:
        page = (out / "index.html").read_text()
        assert 'id="progress-data"' in page and "assets/progress.js" in page
        assert (out / "assets" / "progress.js").is_file()


def test_the_overview_leads_with_outcomes_and_a_paper_search(built):
    data, out = built
    page = (out / "index.html").read_text()
    # A plain form, so it works without scripts: the papers list reads q from the URL.
    assert re.search(r'<form class="home-search" method="get" action="papers/"[^>]*>\s*<input name="q" type="search"', page)
    # Under the lede, then the outcomes (with the caution attached), then the counters and charts.
    order = [page.index('class="lede"'), page.index('class="home-search"'), page.index("claims that rest on the dataset alone"),
             page.index('id="caution"'), page.index('class="progress"' if 'class="progress"' in page else 'class="tiles"')]
    assert order == sorted(order)


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
    assert f'href="{site.SITE_URL}{site.page_of(dandiset)}"' in page and "found about its data" in page


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


def test_the_about_page_names_the_archives_draws_the_steps_and_points_authors_and_archives_on(built):
    data, out = built
    about = (out / "about" / "index.html").read_text()
    archives = {site.split_key(a["key"])[0] for a in data["attempts"]}
    assert archives and site.attempted_archives(data)
    for k in archives:
        assert html.escape(site.ARCHIVES[k]["name"]) in about
    assert "the only archive" not in about
    # The diagram: one box a step, labelled for screen readers, and the list still in full.
    assert 'id="flow"' in about and 'role="img" aria-label="The six steps of an attempt' in about
    for head, _ in site.ABOUT_STEPS:
        assert about.count(f">{html.escape(head)}<") >= 2
    assert html.escape(site.RESPOND_URL) in about and "docs/badges.md" in about
    assert 'href="../authors/"' in about and 'href="../datasets/"' in about
    # The badge shown is a real one, of the first dataset with a badge.
    shown = re.search(r'src="\.\./badge/([a-z]+)/([^"]+)\.svg"', about)
    assert shown and (out / "badge" / shown[1] / f"{shown[2]}.svg").exists()


def test_the_bar_is_for_readers_and_check_your_data_is_its_button(built):
    """Pipeline is the maintainers' page: in the footer, the phone menu (menuonly, hidden on a wide screen) and the
    About page, not among the bar's tabs. "Check your data" is the bar's one button."""
    import re
    data, out = built
    home = (out / "index.html").read_text()
    bar = home[home.index('<nav class="top"'):home.index("</nav>")]
    footer = home[home.index("<footer>"):home.index("</footer>")]
    assert 'href="pipeline/">Pipeline</a>' in footer
    shown = [m for m in re.findall(r'<a class="(tab[^"]*)" href="([^"]*)"', bar) if "menuonly" not in m[0]]
    assert [h for _, h in shown][:5] == ["./", "papers/", "datasets/", "authors/", "about/"]
    assert not any("pipeline" in h for _, h in shown)
    assert '<a class="tab menuonly" href="pipeline/">Pipeline</a>' in bar
    assert re.search(rf'<a class="tab ext cta" href="{re.escape(site.ENCORE_DOCS)}" title="Run the same check', bar)
    # The menu-only links are hidden in the bar and shown in the phone menu; the button is filled in the accent.
    css = (site.ASSETS / "app.css").read_text()
    wide = css[:css.index("@media (max-width:920px)")]
    assert "nav.top a.tab.menuonly{display:none}" in wide and "nav.top a.tab.menuonly{display:flex}" in css
    assert "background:var(--accent);color:var(--surface)" in wide[wide.index("nav.top a.tab.cta{"):]
    pipeline = (out / "pipeline" / "index.html").read_text()
    assert '<a class="tab menuonly" href="../pipeline/" aria-current="page">Pipeline</a>' in pipeline
    assert 'href="../pipeline/">pipeline</a>' in (out / "about" / "index.html").read_text()


def test_a_claim_shows_the_papers_own_words_when_quoted():
    claim = {"claim": "fig2", "statement": "Rates rise.", "source": "Figure 2B", "quote": "Firing rates rose <sharply>.",
             "outcome": "reproduced", "blocked_by": None, "notes": "It rose.", "deviations": [], "disagreed": False}
    html = site.claim_item(claim, "../")
    assert '<blockquote class="quote"><p>Firing rates rose &lt;sharply&gt;.</p><cite>Figure 2B</cite>' in html
    body = html.split("</summary>")[1]
    assert body.index("blockquote") < body.index("It rose.")
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
    body = html.split("</summary>")[1]
    assert '<ul class="stats"><li>Onsets: Wilcoxon rank-sum' in body and body.index("stats") < body.index("N.")


def test_link_claims_are_counted_apart_from_the_papers_findings():
    attempt = {"outcomes": [{"claim": "a", "outcome": "reproduced", "data": "dataset"},
                            {"claim": "l", "outcome": "reproduced", "data": "with_inputs", "kind": "link"},
                            {"claim": "w", "outcome": "blocked", "data": "with_inputs"}]}
    assert sum(site.outcome_counts(attempt).values()) == 1
    assert sum(site.outcome_counts(attempt, "with_inputs").values()) == 1
    assert site.outcome_counts(attempt, "link")["reproduced"] == 1
    # A check of the link is a step of the work, not a result: the page's note of what is counted apart leaves it
    # out, and has the claims on outside data.
    note = site.outside_note([attempt])
    assert "check that the dataset" not in note and "1 claim that also uses data from outside the dataset" in note
    assert site.outside_note([{"outcomes": attempt["outcomes"][:2]}]) == ""
    # The overview folds them into a details block that names each group and its count.
    folded = site.outside_note([attempt], collapsed=True)
    assert folded.startswith('<details class="separate">')
    assert "Counted separately: claims using outside data (1)</summary>" in folded and "link" not in folded
    assert "<details" not in note


def test_a_check_of_the_link_is_under_provenance_and_not_among_the_claims(built):
    data, out = built
    seen = 0
    for q in site.papers_of(data):
        for a in q["attempts"]:
            links = [o for o in a["outcomes"] if o.get("kind") == "link"]
            if not links or len(q["attempts"]) > 1:
                continue
            seen += 1
            page = (out / "papers" / q["key"] / "index.html").read_text()
            claims, provenance = page.split('id="provenance"')[0], page.split('id="provenance"')[1]
            for o in links:
                # Its anchor is kept, under Provenance; it is not a claim in the list, and the page's counts of
                # outcomes do not mention it.
                assert f'id="claim-{o["claim"]}"' in provenance and f'id="claim-{o["claim"]}"' not in claims
                assert site.e(o["statement"]) in provenance
            assert "check that the dataset is the data behind the paper" not in page.lower()
            shown = [o for o in a["outcomes"] if o.get("kind") != "link"]
            assert claims.count('<li class="claim') == len(shown)
    assert seen


def test_a_claim_shows_its_id_which_the_response_form_asks_for():
    claim = {"claim": "fig2-rates", "statement": "Rates rise.", "source": "Figure 2B", "outcome": "reproduced",
             "blocked_by": None, "notes": "It rose.", "deviations": [], "disagreed": False}
    html = site.claim_item(claim, "../")
    # In view without opening the claim, and not a link there (a click on the summary opens the claim).
    head = html.split("</summary>")[0]
    assert '<code class="claim-id" title="The id of this claim">fig2-rates</code>' in head and "<a " not in head
    # Open, the claim gives its id again with a link to itself.
    assert 'Claim id <code>fig2-rates</code>' in html and '<a href="#claim-fig2-rates">link to this claim</a>' in html
    # The form's hint names ids as the page shows them, not numbers the page does not have.
    form = (REPO / ".github" / "ISSUE_TEMPLATE" / "author-response.yml").read_text()
    assert "C3, C7" not in form and "end of the claim's first line" in form


def test_a_closed_claim_gives_the_first_sentence_of_its_notes():
    notes = ("GC median latency 0.710 ms against MC 0.740 ms (Mann-Whitney P = 2.3e-14, Fig. 1E). The stored "
             "waveforms are cut off.")
    claim = {"claim": "fig1", "statement": "Rates <rise>.", "source": "Figure 1E", "outcome": "reproduced",
             "blocked_by": None, "notes": notes, "deviations": [], "disagreed": False}
    head, body = site.claim_item(claim, "../").split("</summary>")
    # In the summary, after the statement, whose markup is unchanged; the full notes are in the body.
    assert ('<p class="statement">Rates &lt;rise&gt;.</p><p class="gist">GC median latency 0.710 ms against MC '
            '0.740 ms (Mann-Whitney P = 2.3e-14, Fig. 1E).</p>') in head
    assert f'<p class="notes">{site.e(notes)}</p>' in body
    # A long first sentence is cut at a word, with an ellipsis; a short label is joined by the next sentence.
    long = site.gist("In " + "many long words " * 20 + "the rate rose. Then more.")
    assert long == "In " + "many long words " * 6 + "many long…"
    assert site.gist("Reading (b). The rate is 3 Hz in 9 sessions. More.") == "Reading (b). The rate is 3 Hz in 9 sessions."
    # No notes, no line.
    assert 'class="gist"' not in site.claim_item({**claim, "notes": ""}, "../")


def test_a_claim_not_stated_in_the_paper_says_it_is_inferred():
    claim = {"claim": "t", "statement": "Few respond.", "source": "Table S1", "inferred": "Numbers from Table S1.",
             "outcome": "reproduced", "blocked_by": None, "notes": "N.", "deviations": [], "disagreed": False}
    html = site.claim_item(claim, "../")
    assert '<p class="inferred"><strong>Not quoted:</strong> Numbers from Table S1.</p>' in html
    link = site.claim_item({**claim, "inferred": None, "kind": "link"}, "../")
    assert "checks the link to the paper’s data" in link



def test_an_outcome_that_rests_on_an_assumption_says_so():
    claim = {"claim": "t", "statement": "Few respond.", "source": "Figure 2", "outcome": "reproduced",
             "blocked_by": None, "notes": "N.", "deviations": ["Assumed a 1 s window, the paper's Figure 3."],
             "disagreed": False}
    assert "rests on an assumption" in site.claim_item({**claim, "assumed": True}, "../")
    assert "rests on an assumption" not in site.claim_item(claim, "../")

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


def test_stylesheets_and_scripts_are_named_by_their_contents(built):
    data, out = built
    page = (out / "pipeline" / "index.html").read_text()
    assert re.search(r'href="\.\./assets/app\.css\?v=[0-9a-f]{10}"', page)
    assert re.search(r'src="assets/progress\.js\?v=[0-9a-f]{10}"', (out / "index.html").read_text())


def test_old_dandiset_links_redirect_to_the_dataset_pages(built):
    data, out = built
    for key in site.current_attempts(data):
        archive, ident = site.split_key(key)
        if archive != "dandi":   # only DANDI datasets had pages under dandisets/
            assert not (out / "dandisets" / ident).exists()
            continue
        old = (out / "dandisets" / ident / "index.html").read_text()
        assert f'url=../../{site.page_of(key)}"' in old
        for a in site.earlier_attempts(data, key):
            moved = (out / "dandisets" / ident / a["id"] / "index.html").read_text()
            assert f'url=../../../{site.attempt_own_path(data, a)}"' in moved
    assert 'url=../datasets/"' in (out / "dandisets" / "index.html").read_text()


def test_datasets_are_named_by_archive_and_id():
    assert site.dataset_label("dandi:000003") == "DANDI:000003"
    assert site.page_of("dandi:000003") == "datasets/dandi/000003/"
    assert site.dir_of("dandi:000003") == "000003" and site.dir_of("ebrains:abc") == "ebrains-abc"
    assert site.key_of_dir("000003") == "dandi:000003" and site.key_of_dir("ebrains-abc") == "ebrains:abc"


def test_a_dataset_with_claims_and_no_attempt_has_a_page_leading_to_its_papers_claims(built):
    data, out = built
    rows = json.loads((out / "data" / "pipeline.json").read_text())
    targets = {t["key"] for t in data["targets"]}
    for key in site.claims_only(data):
        # The pipeline lists the archives' targets. A dataset only a reuse paper names (targets/reuse.yaml) can be
        # outside them: it has its page, and no row.
        row = next((r for r in rows if r["key"] == key), None)
        assert (row is not None) == (key in targets)
        if row:
            assert row["page"] == site.page_of(key)
        page = (out / site.page_of(key) / "index.html").read_text()
        assert 'id="claim-' not in page and "Papers tested on this dataset" in page
        # Its paper's claims, read: the paper is attempted on its other datasets, or not yet at all.
        papers = [q for q in site.papers_of(data) if key in q["datasets"] and q["status"] in ("claims", "attempted")]
        assert papers and any(f'papers/{q["key"]}/"' in page for q in papers)


def test_a_dataset_waiting_on_a_person_links_its_issue():
    data = site.collect()
    label = data["targets"][0]["label"]
    data["issues"] = {label: "https://github.com/catalystneuro/encore/issues/1"}
    row = next(r for r in site.pipeline_rows(data) if r["dataset"] == label)
    assert row["issue"] == data["issues"][label]
    page = site.page_pipeline(data)
    assert f'<a href="{data["issues"][label]}">waiting on you</a>' in page
    assert "has stopped on" in page and "1 paper</a>" in page


def test_the_queue_estimates_fill_the_lanes_in_order():
    q = {"full": ["000001", "000002", "000003", "000004"], "claims": ["000004", "000005"],
         "lanes": {"full": 2, "claims": 1}, "hours": {"full": 4.0, "claims": 0.5}}
    est = site.queue_estimates(q)
    # The lanes' current attempts are half done: the first two start in 2 hours, the next two in 6.
    assert [est[site.key_of_dir(f)]["hours"] for f in q["full"]] == [6.0, 6.0, 10.0, 10.0]
    assert est[site.key_of_dir("000005")] == {"kind": "claims", "place": 2, "hours": 1.25}
    # A dataset in both queues gets the full runner's estimate.
    assert est[site.key_of_dir("000004")]["kind"] == "full"
    # With the running chains' times, a lane is free when its chain should be done.
    q["running"] = {"000009": {"kind": "full", "hours": 1.0}}
    assert [site.queue_estimates(q)[site.key_of_dir(f)]["hours"] for f in q["full"]] == [4.0, 5.0, 8.0, 9.0]
    assert site.in_hours(0.4) == "within the hour" and site.in_hours(10.2) == "about 10 hours"
    assert site.in_hours(100) == "about 4 days" and site.in_hours(None) == ""


def test_the_pipeline_shows_each_queued_dataset_and_when_it_should_be_done():
    data = site.collect()
    first, second = (t["key"] for t in data["targets"][:2])
    third, fourth = (t["key"] for t in data["targets"][2:4])
    data["queue"] = {"full": [site.dir_of(first)], "claims": [],
                     "branches": [site.dir_of(second), site.dir_of(third), site.dir_of(fourth)],
                     "lanes": {"full": 3, "claims": 1}, "hours": {"full": 4.0, "claims": 0.25},
                     "running": {site.dir_of(third): {"kind": "full", "hours": 2.4},
                                 site.dir_of(fourth): {"kind": "full", "hours": 0.5}}}
    rows = {r["key"]: r for r in site.pipeline_rows(data)}
    assert rows[first]["queue"]["place"] == 1 and rows[second]["branch"] and rows[third]["running"]
    page = site.page_pipeline(data)
    # The first in the queue takes the lane that is free now.
    assert ">1 for an attempt</td>" in page and ">about 4 hours</td>" in page and ">branch open</td>" in page
    assert page.count(">running now</td>") == 2 and ">about 2 hours</td>" in page and ">within the hour</td>" in page
    assert "2 chains are running now" in page
    assert "1 paper waits for an attempt on 3 lanes, at about 4.0 hours each" in page


def test_the_pipeline_page_goes_by_paper(built):
    data, out = built
    rows = site.paper_pipeline_rows(data)
    steps = [key for key, _ in site.PAPER_STEPS]
    assert steps[0] == "match"
    states = {"done", "waiting", "todo", "deprecated", "none"}
    assert all(set(r["state"]) == set(steps) and {v[0] for v in r["state"].values()} <= states for r in rows)
    # Each listed paper once, whatever the number of its datasets, and every target under some paper.
    listed = [r["paper"] for r in rows if r["paper"]]
    assert sorted(listed) == sorted(site.paper_records.listed())
    shown = {d["key"] for r in rows for d in r["datasets"]}
    assert {t["key"] for t in data["targets"]} <= shown
    several = next(r for r in rows if r["paper"] and len(site.paper_records.listed()[r["paper"]]["datasets"]) > 1)
    assert len([r for r in rows if r["paper"] == several["paper"]]) == 1
    # A listed paper's match is made; a target no paper is listed for has it still to do (or has none).
    assert all(r["state"]["match"][0] in ("done", "todo", "waiting") for r in rows if r["paper"])
    assert all(r["state"]["match"][0] != "done" for r in rows if not r["paper"])
    page = (out / "pipeline" / "index.html").read_text()
    assert "Papers at each step" in page and ">Paper match</button>" in page and ">Datasets</button>" in page
    assert page.count("<tr data-match=") == len(rows)


def test_a_paper_is_attempted_when_each_of_its_datasets_has_been_used():
    data = site.collect()
    rows = {r["paper"]: r for r in site.paper_pipeline_rows(data) if r["paper"]}
    current = site.current_attempts(data)
    for key, body in site.paper_records.listed().items():
        doi = site.paper_records.doi_of(key)
        need = [d["key"] for d in body["datasets"] if d.get("available", True)]
        used = {k for k in need for a in current.get(k, []) if a["paper"].lower() == doi and not a.get("deprecated")}
        state = rows[key]["state"]["attempt"]
        if state[0] == "done":
            assert used == set(need)
        elif state[0] == "todo" and used:
            assert state[1] == f"{len(used)} of {len(need)} datasets"


def test_the_queue_by_paper_places_a_paper_once():
    data = site.collect()
    paper = next(r for r in site.paper_pipeline_rows(data) if r["paper"] and len(r["datasets"]) > 1)
    data["queue"] = {"full": [site.dir_of(d["key"]) for d in paper["datasets"]], "claims": [], "branches": [],
                     "lanes": {"full": 1, "claims": 1}, "hours": {"full": 4.0, "claims": 0.25},
                     "papers": {"full": [paper["paper"]], "claims": [], "branches": [], "running": {}}}
    row = next(r for r in site.paper_pipeline_rows(data) if r["paper"] == paper["paper"])
    assert row["queue"]["place"] == 1
    assert "1 paper waits for an attempt on 1 lane" in site.page_pipeline(data)


def test_a_reconciled_attempt_marks_its_findings_and_the_fixed_ones():
    earlier = {"id": "000001-demo-01", "findings": [{"kind": "data_missing", "statement": "No position."},
                                                    {"kind": "metadata_error", "statement": "Wrong age."}]}
    later = {"id": "000001-demo-02", "findings": [{"kind": "data_missing", "statement": "Position missing.", "found": None},
                                                  {"kind": "other", "statement": "Duplicates.", "found": None}],
             "reconciliation": {"earlier": "000001-demo-01", "blind": True, "findings": [
                 {"finding": 1, "status": "still_present", "now": 1, "note": "Same files."},
                 {"finding": 2, "status": "fixed", "note": "Age is set."}],
                 "outcomes": [{"claim": "c", "earlier": "reproduced", "note": "New version."}]}}
    site.reconcile([earlier, later])
    assert [f["status"] for f in later["findings"]] == ["still_present", "new"]
    assert later["reconciliation"]["gone"] == [{"status": "fixed", "note": "Age is set.", "statement": "Wrong age.",
                                                "kind": "metadata_error", "about": "data"}]
    assert later["reconciliation"]["outcomes"][0]["earlier"] == "reproduced"


def _response(name, labels, attempt="tingley-2021-01", paper="tingley-2021", orcid="_No response_"):
    body = (f"### Paper\n\n{paper}\n\n### Attempt\n\n{attempt}\n\n### Your name\n\n{name}\n\n"
            f"### Your role in the paper\n\nfirst author\n\n### ORCID iD\n\n{orcid}\n\n"
            "### Your view of the attempt\n\nSome outcomes are wrong\n\n### Claims you are responding to\n\nC3\n\n"
            "### Your response\n\nThe intervals in Figure 3 are bootstrapped.\n\n### Supporting links\n\n_No response_\n")
    return {"url": "https://github.com/x/y/issues/" + "".join(str(ord(c)) for c in name)[:12], "body": body, "state": "OPEN",
            "createdAt": "2026-11-07T00:00:00Z", "labels": [{"name": n} for n in ["author-response", *labels]]}


TINGLEY = {"key": "tingley-2021", "byline": "Tingley et al. 2021"}


def test_the_response_link_fills_in_the_paper_and_the_attempt():
    url = site.respond_link(TINGLEY, {"id": "tingley-2021-01"})
    assert "template=author-response.yml" in url and "paper=tingley-2021" in url and "attempt=tingley-2021-01" in url
    assert "title=Author+response%3A+Tingley+et+al.+2021" in url and "attempt=" not in site.respond_link(TINGLEY)


def test_a_response_names_its_paper_by_key_doi_or_page():
    doi = site.paper_records.doi_of("tingley-2021")
    for said in ("tingley-2021", doi, f"https://doi.org/{doi}", "https://encorescience.org/papers/tingley-2021/"):
        assert list(site.responses_by_paper([_response("A", ["author-confirmed"], paper=said)])) == ["tingley-2021"], said
    assert site.responses_by_paper([_response("A", [], paper="no such paper")]) == {}


def test_only_confirmed_author_responses_are_shown():
    rs = site.responses_by_paper([_response("A. Author", ["author-confirmed"]), _response("Someone", [])])
    assert list(rs) == ["tingley-2021"] and [r["shown"] for r in rs["tingley-2021"]] == [True, False]
    html = site.responses_block({"responses": rs}, TINGLEY)
    assert "A. Author" in html and "bootstrapped" in html and "Someone" not in html
    assert "1 response from someone who says they are an author awaits confirmation" in html
    assert "attempt tingley-2021-01" in html and "template=author-response.yml" not in html   # the form is linked once, under it


def test_a_paper_without_responses_has_no_responses_section():
    assert site.responses_block({"responses": {}}, TINGLEY) == ""


def test_an_attempts_page_shows_the_responses_to_it_and_to_the_paper_in_general():
    mine, other, general = (_response("A. Author", ["author-confirmed"]),
                            _response("Be Author", ["author-confirmed"], attempt="tingley-2021-02"),
                            _response("Cee Author", ["author-confirmed"], attempt="_No response_"))
    rs = site.responses_by_paper([mine, other, general, mine])
    page = site.responses_block({"responses": rs}, TINGLEY)
    assert page.count("A. Author") == 1 and "Be Author" in page and "Cee Author" in page
    one = site.responses_block({"responses": rs}, TINGLEY, {"id": "tingley-2021-01"})
    assert "A. Author" in one and "Cee Author" in one and "Be Author" not in one


def test_responses_are_on_the_papers_page_and_the_writers_page_and_not_the_datasets(tmp_path):
    data = site.collect()
    person = next(a for a in site.authors_of(data, site.paper_records.doi_of("tingley-2021")) if a.get("orcid"))
    data["responses"] = site.responses_by_paper([_response(person["name"], ["author-confirmed"], orcid=person["orcid"])])
    site.build(data, tmp_path)
    paper = (tmp_path / "papers" / "tingley-2021" / "index.html").read_text()
    # On the paper's page, under the summary: the writer's name opens their page, as their ORCID iD has one.
    assert "Responses from the paper&rsquo;s authors" in paper and "bootstrapped" in paper
    assert f'<strong><a href="../../authors/{person["orcid"]}/">{site.e(person["name"])}</a></strong>' in paper
    assert paper.count("Respond to this attempt</a>") == 1 and "attempt=tingley-2021-" in paper
    # Their own page has a Responses tab with it, naming the paper.
    theirs = (tmp_path / "authors" / person["orcid"] / "index.html").read_text()
    assert 'data-panel="responses"' in theirs and "bootstrapped" in theirs and 'papers/tingley-2021/">Tingley et al. 2021</a>' in theirs
    # A dataset's page has neither the responses nor the form: a response is to a paper's attempt.
    dataset = (tmp_path / "datasets" / "dandi" / "000233" / "index.html").read_text()
    assert "bootstrapped" not in dataset and "Respond to" not in dataset


def test_the_response_form_is_on_paper_and_attempt_pages(built):
    data, out = built
    paper = (out / "papers" / "tingley-2021" / "index.html").read_text()
    assert "Respond to this attempt</a>" in paper and "paper=tingley-2021&amp;" in paper and "attempt=tingley-2021-" in paper
    # A paper with several current attempts does not choose one for the writer; each attempt's page does.
    several = (out / "papers" / "semenov-2026" / "index.html").read_text()
    assert "Respond to an attempt</a>" in several and "attempt=semenov-2026" not in several
    assert "attempt=semenov-2026-03" in (out / "papers" / "semenov-2026" / "semenov-2026-03" / "index.html").read_text()
    assert "Respond to" not in (out / "datasets" / "dandi" / "000233" / "index.html").read_text()
    # No one has a Responses tab while there are no responses.
    assert 'data-panel="responses"' not in (out / "authors" / next(iter(site.author_index(data))) / "index.html").read_text()


def test_the_journal_filter_names_at_most_the_top_journals(built):
    _, out = built
    rows = json.loads((out / "data" / "datasets.json").read_text())
    named = {r["journal"] for r in rows} - {"Preprint", "Other journals", "Not recorded"}
    assert len(named) <= site.TOP_JOURNALS and all(r["journal"] for r in rows)


def test_each_attempted_paper_has_a_page_listed_under_results(built):
    import json
    _, site = built
    papers = json.loads((site / "data" / "papers.json").read_text())
    attempted = [p for p in papers if p["status"] == "attempted"]
    assert attempted and all((site / p["page"] / "index.html").is_file() for p in attempted)
    page = (site / "papers" / "tingley-2021" / "index.html").read_text()
    assert "A metabolic function of the hippocampal sharp wave-ripple" in page and "tingley-2021-01" in page
    # The paper's page stands on its own: its claims, with their outcomes, tests and notes, are on the page, and no
    # claim sends the reader to a dataset's page. So are the findings, notebooks, verification and provenance.
    assert 'id="claim-' in page and "/#claim-" not in page
    for panel in ("claims", "notebooks", "verification", "differences", "provenance"):
        assert f'<section class="tabpanel" id="{panel}">' in page
    # Findings about the data belong to the dataset: the paper's page points to them.
    assert 'id="findings"' not in page and 'datasets/dandi/000233/#findings">' in page
    # The header has one table of the paper's datasets, each with its version, findings and links, once.
    assert page.count('<div class="sets">') == 1 and ">Paper</a>" not in page and "JSON (" not in page
    assert '<a href="../../papers/">Papers</a>' in page and 'href="../../datasets/dandi/000233/"' in page
    # Every attempted paper's page has each claim of its latest attempts, once.
    import build_site
    for q in build_site.papers_of(_):
        if q["attempts"]:
            text = (site / "papers" / q["key"] / "index.html").read_text()
            for a in q["attempts"]:
                assert all(text.count(f'id="claim-{o["claim"]}"') >= 1 for o in a["outcomes"]), q["key"]
    # And a dataset's page names the paper's page.
    assert 'papers/tingley-2021/">' in (site / "datasets" / "dandi" / "000233" / "index.html").read_text()
    # The result leads: under the title, the full outcome bar and the summary come before the datasets, which
    # sit with the paper's DOI, tags and verification badge in the side column. So on an attempt's page.
    for path in (("papers", "tingley-2021"), ("papers", "kim-2022", "kim-2022-01")):
        text = site.joinpath(*path, "index.html").read_text()
        head = text[text.index('<header class="page"'):text.index("</header>")]
        result, summary = head.index('<div class="result">'), head.index('<div class="attempt-summary">')
        side, sets = head.index('<aside class="phead-side"'), head.index('<div class="sets">')
        assert head.index("<h1>") < result < summary < side < sets, path
        assert '<div class="bar" role="img" aria-label="Outcomes of ' in head[result:summary]
        assert 'class="tier' in head[side:] and "doi:" in head[side:] and "doi:" not in head[:side]
    # A paper on several datasets lists them all; the tab bar leads to the papers and to the datasets.
    semenov = (site / "papers" / "semenov-2026" / "index.html").read_text()
    assert all(f"DANDI:{d}" in semenov for d in ("001515", "001516", "001526"))
    nav = (site / "index.html").read_text()
    assert 'href="papers/"' in nav and 'href="datasets/"' in nav and 'class="menu"' not in nav


def test_links_are_underlined_except_where_nearly_every_word_is_one():
    """Links keep the browser's underline by default. Only the dense areas (the datasets table, list rows, crumbs,
    attempts, footer) quiet it, each with one scoped rule, and there it comes back on hover and keyboard focus."""
    css = (site.ROOT / "tools" / "site_assets" / "app.css").read_text()
    # The base rule colours links and does not remove their underline.
    assert re.search(r"^a\{color:var\(--link\)\}$", css, re.M)
    assert not re.search(r"^a\{[^}]*text-decoration", css, re.M)
    quiet = re.search(r"^:where\((.*?)\) a:not\(\[class\]\)\{text-decoration:none\}$", css, re.M)
    thin = re.search(r"^:where\((.*?)\) a:not\(\[class\]\)\{text-decoration:underline;", css, re.M)
    back = re.search(r"^:where\((.*?)\) a:not\(\[class\]\):is\(:hover,:focus-visible\)\{text-decoration:underline", css, re.M)
    assert quiet and thin and back
    assert {".sets th", ".row .id", ".row .meta"} <= set(quiet[1].split(","))
    assert {".crumbs", "footer"} <= set(thin[1].split(","))
    assert {".sets", ".row .meta", ".crumbs", ".timeline", "footer"} <= set(back[1].split(","))
    # Running text is never in the scope, and keyboard focus keeps its outline.
    for prose in (".lede", ".notes", ".caution", ".about", ".claim", ".sub"):
        assert prose not in quiet[1] + thin[1] + back[1]
    assert ":focus-visible{outline:2px solid var(--accent)" in css and "outline:none" not in css


def test_a_dataset_only_a_reuse_paper_names_is_a_target_of_the_site():
    """DANDI:000978 names no paper, so no archive list has it; wakhloo-2026 reuses it (targets/reuse.yaml)."""
    data = site.collect()
    archive = {t["key"] for t in site.all_targets()}
    outside = [t for t in data["targets"] if t["key"] not in archive]
    assert outside and all(t.get("reuse_only") and t["match"] == "matched" for t in outside)
    for t in outside:
        # Its paper is one of those listed for it (several papers can reuse one dataset).
        papers = {site.paper_records.doi_of(key) for key, body in site.paper_records.listed().items()
                  if t["key"] in {d["key"] for d in body["datasets"]}}
        assert t["paper"] in papers and t["name"] != t["label"]
        assert isinstance(t["size_gb"], float) and isinstance(t["files"], int)
    # Each has its row in the pipeline and in the datasets list, as the tests of both expect of an attempted dataset.
    assert {t["key"] for t in outside} <= {r["key"] for r in site.pipeline_rows(data)}
    assert data["queue_counts"]["with_a_paper"] == len(data["targets"])


def test_the_overview_leads_with_papers():
    """The papers are the primary index: the first tile, and the measure the charts show first."""
    panel = site.progress_panel(site.collect())
    assert list(site.PROGRESS_METRICS)[0] == site.PROGRESS_DEFAULT == "papers"
    first = panel.index('data-metric="papers"')
    assert first < panel.index('data-metric="datasets"')
    assert 'data-metric="papers" aria-pressed="true"' in panel and 'data-metric="datasets" aria-pressed="false"' in panel
    assert ">Papers attempted over time</h2>" in panel and ">Papers attempted, new each day</h2>" in panel


def test_the_archive_charts_colour_dandi_and_crcns_and_fold_the_other_archives():
    """Three archive colours, none an outcome's: DANDI and CRCNS each have one, every other archive shares the third."""
    data = site.collect()
    p = site.progress_data(data)
    keys = [a["key"] for a in p["archives"]]
    assert keys[: len([k for k in keys if k in site.OWN_COLOUR])] == [k for k in site.OWN_COLOUR if k in keys]
    assert all(a["slot"] in (1, 2, 3) for a in p["archives"])
    present = {site.split_key(a["key"])[0] for a in data["attempts"]}
    if present - set(site.OWN_COLOUR):
        other = next(a for a in p["archives"] if a["key"] == "other")
        assert other["slot"] == 3 and other["label"].startswith("Other archives (")
    # Every dataset is counted once, in its archive's series or in the other archives'.
    rows = p["series"]["all"]
    assert sum(rows["datasets"]) == sum(sum(rows[f"archive:{k}"]) for k in keys)
    css = (site.ROOT / "tools" / "site_assets" / "app.css").read_text()
    assert "--archive-4" not in css


def test_muted_text_keeps_the_wcag_aa_contrast_in_both_themes():
    """Small gray text (dates, journals, claim sources, counts) needs 4.5:1 on every background it sits on, and must
    stay lighter than the secondary text so the two still read as two levels."""
    css = (site.ROOT / "tools" / "site_assets" / "app.css").read_text()

    def theme(selector):
        block = css.split(selector, 1)[1].split("}", 1)[0]
        return dict(re.findall(r"--([a-z0-9-]+):(#[0-9a-f]{6})", block))

    def ratio(a, b):
        def lum(h):
            c = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]
            c = [x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
            return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]
        hi, lo = sorted([lum(a), lum(b)], reverse=True)
        return (hi + 0.05) / (lo + 0.05)

    light = theme(":root{")
    dark_system = theme(":root:not([data-theme=light]){")
    dark_chosen = theme(":root[data-theme=dark]{")
    assert dark_system == dark_chosen  # the two copies of the dark theme stay in step
    for colours in (light, {**light, **dark_chosen}):
        for text in ("muted", "good-text"):
            for background in ("surface", "panel", "hover"):
                assert ratio(colours[text], colours[background]) >= 4.5, (text, background, colours[text])
        assert ratio(colours["muted"], colours["surface"]) < ratio(colours["text2"], colours["surface"]) - 2


def test_the_datasets_list_is_for_curators_and_the_papers_list_finds_a_paper_by_its_datasets(built):
    import json
    data, out = built
    # The datasets list has the datasets an attempt used, by what was found about their data; the old address of
    # the DANDI list leads to it.
    page = (out / "datasets" / "index.html").read_text()
    config = json.loads(page.split('id="list-config">')[1].split("</script>")[0])
    assert config["only"] == {"status": ["attempted"]} and config["sorts"][0]["key"] == "-findings"
    assert [f["key"] for f in config["facets"]][:3] == ["archive", "found", "tested"]
    assert set(config["labels"]["tested"]) >= set(site.VERSION_STATES)
    assert 'aria-current="page">Datasets' in page
    assert 'url=../datasets/"' in (out / "dandisets" / "index.html").read_text()
    assert "datasets/</loc>" in (out / "sitemap.xml").read_text()
    rows = json.loads((out / "data" / "datasets.json").read_text())
    tested = [r for r in rows if r["status"] == "attempted"]
    assert tested and all(set(r["tested"]) <= set(site.VERSION_STATES) for r in tested)
    assert f'<span class="n">{len(tested):,}</span>' in page
    # The papers list still finds a paper by its datasets, and filters by what was found about them.
    keys = [k for k, _ in site.LISTS["papers"]["facets"]]
    assert "found" in keys and "converted" in keys
    rows = json.loads((out / "data" / "papers.json").read_text())
    named = [r for r in rows if any(d.get("name") for d in r["datasets"])]
    assert named and all({"found", "converted"} <= set(r) for r in rows)
    # A finding's kind, on any page, opens the datasets with an open finding of that kind.
    assert 'datasets/?found=' in (out / "datasets" / "dandi" / "000233" / "index.html").read_text()
    assert 'papers/?found=' not in (out / "index.html").read_text()


def test_the_datasets_list_says_how_many_papers_each_dataset_has(built):
    data, out = built
    rows = json.loads((out / "data" / "datasets.json").read_text())
    theirs: dict = {}
    for q in site.papers_of(data):
        for k in q["datasets"]:
            theirs.setdefault(k, []).append(q)
    several = 0
    for r in rows:
        papers = theirs.get(r["id"], [])
        # Every paper associated with the dataset, attempted or not, those with an attempt first.
        assert r["n_papers"] == len(papers) == len(r["papers"])
        assert {q["byline"] for q in papers} == {x["byline"] for x in r["papers"]}
        assert [x["attempted"] for x in r["papers"]] == sorted((x["attempted"] for x in r["papers"]), reverse=True)
        assert r["paper_count"] == ("one" if len(papers) == 1 else "several" if papers else None)
        several += len(papers) > 1
    assert several
    config = json.loads((out / "datasets" / "index.html").read_text().split('id="list-config">')[1].split("</script>")[0])
    assert {"key": "-n_papers", "label": "Most papers"} in config["sorts"]
    assert {"key": "paper_count", "label": "Papers"} in config["facets"]
    js = (site.ASSETS / "list.js").read_text()
    assert "r.papers" in js and "not yet tested" in js


def test_a_version_is_said_in_words(built):
    a = {"dataset_version": "0.240101.0000", "dataset": {"doi": "10.48324/dandi.000001/0.240101.0000"}}
    assert site.version_state(a) == "published" and site.version_plain(a) == "version 0.240101.0000"
    assert 'href="https://doi.org/10.48324/dandi.000001/0.240101.0000"' in site.version_text(a)
    for v, state, words in (("draft", "draft", "the unpublished draft"), ("unversioned", "unversioned", "unversioned files"),
                            (None, "unknown", "a version not recorded")):
        a = {"dataset_version": v, "dataset": {}}
        assert site.version_state(a) == state and site.version_plain(a) == words
        assert "version unversioned" not in site.version_text(a)
    # Newest version first: a draft after every published version, which are dated.
    order = [{"dataset_version": v, "date": "2026-01-01", "id": "x"} for v in ("0.240101.0000", "draft", None, "0.230101.0000")]
    assert [a["dataset_version"] for a in sorted(order, key=site.version_order, reverse=True)] == [
        "draft", "0.240101.0000", "0.230101.0000", None]


def test_every_paper_has_a_page_and_every_list_links_to_it(built):
    # A paper not tested yet has a page too, which says so, so that the lists of datasets, papers and authors open
    # the paper's page in the registry, never the paper's DOI.
    data, out = built
    untested = 0
    for q in site.papers_of(data):
        page = (out / "papers" / q["key"] / "index.html").read_text()
        assert site.e(q["title"]) in page and f'https://doi.org/{site.e(q["doi"])}' in page
        if not q["attempts"] and q["status"] != "claims":
            untested += 1
            assert "Not tested yet." in page
    assert untested
    for name in ("datasets", "papers", "authors"):
        rows = json.loads((out / "data" / f"{name}.json").read_text())
        pages = [r["page"] for r in rows] if name == "papers" else [q["page"] for r in rows for q in r.get("papers") or []]
        assert pages and all(x and x.startswith("papers/") and (out / x / "index.html").is_file() for x in pages), name
    # The list opens each paper's page; the DOI is offered only as a link of its own, labelled "doi".
    js = (site.ASSETS / "list.js").read_text()
    assert "doi.org/${esc(q.doi)}" not in js and "r.page ? root + r.page : `https://doi.org" not in js


def test_a_paper_with_claims_and_no_attempt_shows_its_claims_on_its_page(built):
    data, out = built
    papers = [q for q in site.papers_of(data) if q["status"] == "claims"]
    assert papers
    for q in papers:
        page = (out / "papers" / q["key"] / "index.html").read_text()
        files = [f for k in q["datasets"] for f in data["claim_files"].get(k, []) if f["paper"].lower() == q["doi"]]
        ids = {c["id"] for f in files for c in f["claims"]}
        assert ids and all(f'id="claim-{i}"' in page for i in ids), q["key"]
        assert "Not attempted yet" in page and "No attempt on this paper yet" not in page


def test_a_finding_is_about_the_data_or_the_paper_and_shown_where_it_belongs(built):
    data, out = built
    # By its kind unless the record says: the paper for these three kinds.
    assert site.ABOUT_PAPER == {"methods_unavailable", "code_mismatch", "paper_inconsistency"}
    seen_notes = 0
    for dandiset, attempts in site.current_attempts(data).items():
        dataset_page = (out / site.page_of(dandiset) / "index.html").read_text()
        for a in attempts:
            assert all(f["about"] == "data" for f in a["findings"])
            assert all(f["about"] == "paper" for f in a["paper_notes"])
            if a.get("deprecated"):
                continue
            paper_page = _paper_page(data, out, a)
            for f in a["paper_notes"]:
                seen_notes += 1
                assert site.e(f["statement"]) in paper_page and site.e(f["statement"]) not in dataset_page
            for f in a["findings"]:
                assert site.e(f["statement"]) in dataset_page and site.e(f["statement"]) not in paper_page
    assert seen_notes


def test_a_finding_that_names_its_datasets_is_on_those_datasets_only():
    import jsonschema, json
    schema = json.loads((REPO / "schemas" / "attempt.schema.json").read_text())["properties"]["findings"]
    ok = [{"kind": "other", "statement": "S.", "about": "data", "datasets": ["000001"]}]
    jsonschema.validate(ok, schema)
    for bad in ([{"kind": "other", "statement": "S.", "about": "both"}], [{"kind": "other", "statement": "S.", "datasets": []}]):
        try:
            jsonschema.validate(bad, schema)
        except jsonschema.ValidationError:
            continue
        raise AssertionError(bad)



def test_a_papers_page_names_its_authors_and_each_with_an_orcid_has_a_page_of_their_papers(built):
    data, out = built
    index = site.author_index(data)
    assert index and (out / "authors" / "index.html").is_file()
    # Every author with an ORCID iD has a page with all of their papers in the registry.
    rows = {r["id"]: r for r in json.loads((out / "data" / "authors.json").read_text())}
    assert set(rows) == set(index)
    theirs: dict = {}
    for q in site.papers_of(data):
        for a in site.authors_of(data, q["doi"]):
            if a.get("orcid"):
                theirs.setdefault(a["orcid"], []).append(q)
    for orcid, author in index.items():
        page = (out / "authors" / orcid / "index.html").read_text()
        assert f'href="https://orcid.org/{orcid}"' in page and site.e(author["name"]) in page
        papers = theirs.get(orcid, [])
        # Their datasets: every dataset in the registry that names the iD among its contributors, with their roles.
        sets = [(k["key"], c.get("roles") or []) for k in data["targets"]
                for c in site.contributors_of(data, k["key"]) if c.get("orcid") == orcid]
        assert [(d["key"], d["roles"]) for d in author["datasets"]] == sorted(sets)
        assert papers or sets
        assert rows[orcid]["n_datasets"] == len(sets)
        assert rows[orcid]["as"] == [k for k, on in (("author", papers), ("contributor", sets)) if on]
        for key, roles in sets:
            assert site.e(site.dataset_label(key)) in page and site.e(", ".join(roles)) in page
        assert ('data-panel="datasets"' in page) == bool(sets) and ('data-panel="papers"' in page) == bool(papers or not sets)
        # The outcomes of their papers' claims, summed.
        counted = {r["id"]: r["counts"] for r in json.loads((out / "data" / "papers.json").read_text())} if orcid == next(iter(index)) else None
        if counted is not None:
            total = sum(n for q in papers for n in (counted[q["key"]] or {}).values())
            assert (f"Outcomes of the {total:,} claims tested across" in page) == bool(total)
        assert {q["key"] for q in author["papers"]} == {q["key"] for q in papers}
        for q in papers:
            assert site.e(q["title"]) in page
            assert f'href="../../papers/{q["key"]}/"' in page
        assert rows[orcid]["n_papers"] == len(papers) and rows[orcid]["n_attempted"] == sum(1 for q in papers if q["attempts"])
    # A paper's page names its authors in order; one with an ORCID iD opens the author's page, one without is a name.
    linked = plain = long = 0
    for q in site.papers_of(data):
        page = (out / "papers" / q["key"] / "index.html").read_text()
        people = site.authors_of(data, q["doi"])
        at = 0
        for a in people:
            shown = (f'<a href="../../authors/{a["orcid"]}/">{site.e(a["name"])}</a>' if a.get("orcid") else site.e(a["name"]))
            at = page.index(shown, at)   # raises if a name is missing or out of order
            linked += bool(a.get("orcid")); plain += not a.get("orcid")
        if len(people) > site.AUTHORS_SHOWN + 2:
            long += 1
            assert f"and {len(people) - site.AUTHORS_SHOWN} more authors</summary>" in page
    assert linked and plain and long
    # A dataset's page names its contributors; each with an ORCID iD opens their page.
    page = (out / "datasets" / "dandi" / "000003" / "index.html").read_text()
    people = site.contributors_of(data, "dandi:000003")
    assert people and all(site.e(c["name"]) in page for c in people)
    assert any(f'<a href="../../../authors/{c["orcid"]}/"' in page for c in people if c.get("orcid"))
    # Someone who is only a contributor of datasets has a page too, with the Datasets tab alone.
    only = next(a for a in index.values() if a["datasets"] and not a["papers"])
    theirs_page = (out / "authors" / only["orcid"] / "index.html").read_text()
    assert 'data-panel="datasets"' in theirs_page and 'data-panel="papers"' not in theirs_page
    sitemap = (out / "sitemap.xml").read_text()
    assert "authors/</loc>" in sitemap and f"authors/{next(iter(index))}/</loc>" in sitemap
    assert 'href="authors/"' in (out / "index.html").read_text()


def test_the_authors_file_has_each_person_once_a_paper():
    import authors
    people = [{"name": "A B", "orcid": "0000-0001-0000-0001"}, {"name": "C D", "orcid": None},
              {"name": "E F", "orcid": None}, {"name": "A. B", "orcid": "0000-0001-0000-0001"}]
    assert [a["name"] for a in authors.once(people)] == ["A B", "C D", "E F"]
    assert authors.key("10.1101/2020.03.31.018820v2") == "10.1101/2020.03.31.018820"
    known = site.load_yaml(site.ROOT / "papers" / "authors.yaml")["papers"]
    for doi, listed in known.items():
        ids = [a["orcid"] for a in listed if a["orcid"]]
        assert len(ids) == len(set(ids)), doi
        assert all(a["name"] and (a["orcid"] is None or authors.ORCID.fullmatch(a["orcid"])) for a in listed), doi


def test_the_contributors_file_names_people_given_name_first_with_roles_in_words():
    import contributors
    assert contributors.given_first("Buzsáki, György") == "György Buzsáki" and contributors.given_first("IBL") == "IBL"
    assert contributors.role("dcite:ContactPerson") == "Contact person" and contributors.role("Creator") == "Creator"
    people = [{"name": "A B", "orcid": "0000-0001-0000-0001", "roles": ["Author"]},
              {"name": "A B", "orcid": "0000-0001-0000-0001", "roles": ["Author", "Data curator"]},
              {"name": "C D", "orcid": None, "roles": ["Creator"]}]
    assert contributors.once(people) == [{"name": "A B", "orcid": "0000-0001-0000-0001", "roles": ["Author", "Data curator"]},
                                         {"name": "C D", "orcid": None, "roles": ["Creator"]}]
    known = site.load_yaml(site.ROOT / "targets" / "contributors.yaml")["datasets"]
    for key, listed in known.items():
        ids = [p["orcid"] for p in listed if p["orcid"]]
        assert len(ids) == len(set(ids)), key
        assert all(p["name"] and "," not in p["name"] and (p["orcid"] is None or contributors.ORCID.fullmatch(p["orcid"]))
                   for p in listed), key


def test_a_lists_filters_open_again_when_a_narrow_window_is_widened():
    # Closed under their bar on a narrow screen; a wide screen has no bar, so they are opened whenever it is wide,
    # not only when the page loads (assets/list.js follows the media query).
    js = (site.ASSETS / "list.js").read_text()
    assert "narrow.addEventListener('change', fitFilters)" in js and "$('facets').open = !narrow.matches" in js


def test_a_dataset_has_a_badge_for_the_findings_reproduced_from_it_in_verified_attempts(built):
    data, out = built
    with_badge = 0
    for key, attempts in site.current_attempts(data).items():
        archive, ident = site.split_key(key)
        svg = out / "badge" / archive / f"{ident}.svg"
        api = json.loads((out / "api" / f'{site.page_of(key).rstrip("/")}.json').read_text())
        row = next(r for r in json.loads((out / "data" / "datasets.json").read_text()) if r["id"] == key) if with_badge < 3 else None
        # Only claims on the dataset, reproduced in full, in a current attempt a verifier has checked.
        counted = [a for a in attempts if not a.get("deprecated") and a["tier"] != "runs"]
        total = sum(site.outcome_counts(a)["reproduced"] for a in counted)
        badge = site.badge_of(data, key)
        assert (badge is None) == (total == 0) and svg.is_file() == bool(total) and api["badge"] == badge
        page = (out / site.page_of(key) / "index.html").read_text()
        assert ("Badges for this dataset" in page) == bool(site.dataset_outcomes(data, key)) and (not total or site.dataset_outcomes(data, key))
        if not total:
            continue
        with_badge += 1
        assert badge["reproduced"] == total == sum(q["reproduced"] for q in badge["papers"])
        assert badge["text"].startswith(f'{total} finding{"" if total == 1 else "s"} reproduced')
        assert badge["url"] == site.SITE_URL + site.page_of(key) and badge["svg"].endswith(f"badge/{archive}/{ident}.svg")
        text = svg.read_text()
        assert text.startswith("<svg ") and f">{site.e(badge['text'])}</text>" in text and ">Encore</text>" in text
        assert f"<strong>{total}</strong> finding" in page and site.e(badge["svg"]) in page
        if row is not None:
            assert row["badge"] == badge["text"]
    assert with_badge
    # A dataset's page leads with its papers; what was found about its data comes after.
    page = (out / "datasets" / "dandi" / "000233" / "index.html").read_text()
    assert page.index('id="papers"') < page.index('id="findings"')


def test_a_dataset_has_two_more_badges_with_all_the_outcomes(built):
    # Every outcome of the claims tested on the dataset, verified or not, as one line and as a card: a dataset whose
    # attempts no verifier has checked has these two and not the first.
    data, out = built
    seen = unverified = 0
    for key, attempts in site.current_attempts(data).items():
        archive, ident = site.split_key(key)
        live = [a for a in attempts if not a.get("deprecated")]
        counts = site.outcome_counts(live) if live else dict.fromkeys(site.OUTCOMES, 0)
        every = site.dataset_outcomes(data, key)
        line, card = (out / "badge" / archive / f"{ident}-{kind}.svg" for kind in ("outcomes", "card"))
        api = json.loads((out / "api" / f'{site.page_of(key).rstrip("/")}.json').read_text())
        assert (every is None) == (sum(counts.values()) == 0) and line.is_file() == card.is_file() == bool(every)
        assert api["badges"] == {"reproduced": (site.badge_of(data, key) or {}).get("svg"),
                                 "outcomes": every["svg_outcomes"] if every else None, "card": every["svg_card"] if every else None}
        if not every:
            continue
        seen += 1
        unverified += site.badge_of(data, key) is None
        assert every["counts"] == counts and list(counts) == list(site.OUTCOMES)
        assert every["papers"] == len({a["paper"].lower() for a in live})
        for svg in (line.read_text(), card.read_text()):
            for k, n in counts.items():
                assert f">{n} {site.OUTCOME_SHORT[k]}</text>" in svg and f'fill="{site.OUTCOME_FILL[k]}"' in svg
            assert site.e(every["alt"]) in svg
        assert site.e(site.dataset_label(key)) in card.read_text()
        assert f'· {every["papers"]} paper' in card.read_text()
        page = (out / site.page_of(key) / "index.html").read_text()
        assert every["svg_outcomes"] in page and every["svg_card"] in page and 'class="badge-pick"' in page
    assert seen and unverified


def test_a_paper_has_badges_and_a_json_file_of_its_results(built):
    # The same three styles as a dataset and a person, at badge/papers/<key>; the first only when a verified attempt
    # reproduced something. They are offered at the end of the paper's page, not on the page of one attempt.
    data, out = built
    rows = {r["id"]: r for r in json.loads((out / "data" / "papers.json").read_text())}
    seen = without = claims_only = 0
    for q in site.papers_of(data):
        key = q["key"]
        first, line, card = (out / "badge" / "papers" / f"{key}{kind}.svg" for kind in ("", "-outcomes", "-card"))
        file = out / "api" / "papers" / f"{key}.json"
        if not (q["attempts"] or q["status"] == "claims"):
            # A paper not tested yet has a page and a JSON file, and no badge.
            assert file.is_file() and not first.exists() and not card.exists()
            assert json.loads(file.read_text())["badges"] == {"reproduced": None, "outcomes": None, "card": None}
            continue
        api = json.loads(file.read_text())
        badge, every = site.paper_badge(data, q), site.paper_outcomes(data, q)
        total = sum(site.outcome_counts(a)["reproduced"] for a in q["live"] if a["tier"] != "runs")
        counts = {k: (rows[key].get("counts") or {}).get(k, 0) for k in site.OUTCOMES}
        assert (badge is None) == (total == 0) and first.is_file() == bool(total)
        assert (every is None) == (sum(counts.values()) == 0) and line.is_file() == card.is_file() == bool(every)
        assert api["badge"] == badge and api["outcome_counts"] == (counts if every else None)
        assert api["badges"] == {"reproduced": (badge or {}).get("svg"), "outcomes": every["svg_outcomes"] if every else None,
                                 "card": every["svg_card"] if every else None}
        assert api["doi"] == q["doi"] and api["url"] == site.SITE_URL + f"papers/{key}/"
        assert rows[key]["badge"] == (badge or {}).get("text")
        page = (out / "papers" / key / "index.html").read_text()
        assert ("for this paper</h2>" in page) == bool(badge or every)
        if not every:
            claims_only += 1
            continue
        seen += 1
        without += badge is None
        if badge:
            assert badge["reproduced"] == total and badge["text"] == f'{total} finding{"" if total == 1 else "s"} reproduced'
            assert f">{site.e(badge['text'])}</text>" in first.read_text() and badge["svg"] in page
        for svg in (line.read_text(), card.read_text()):
            for k, n in counts.items():
                assert f">{n} {site.OUTCOME_SHORT[k]}</text>" in svg
        # The card names the paper and says how many claims and datasets, not "1 paper".
        assert site.e(q["byline"]) in card.read_text() and f'{every["claims"]} claim' in card.read_text()
        assert " dataset" in card.read_text() and "1 paper" not in card.read_text()
        assert every["svg_outcomes"] in page and every["svg_card"] in page and 'class="badge-pick"' in page
        # One attempt's own page does not offer the paper's badges.
        for a in q["live"][:1]:
            own = site.attempt_own_path(data, a)
            if own and own.rstrip("/") != f"papers/{key}":
                assert "for this paper</h2>" not in (out / own / "index.html").read_text()
    assert seen and without and claims_only


def test_a_badge_sums_the_papers_and_leaves_out_what_is_not_verified():
    data = site.collect()
    key = next(k for k, atts in site.current_attempts(data).items()
               if len(atts) == 1 and atts[0]["tier"] != "runs" and not atts[0].get("deprecated")
               and site.outcome_counts(atts[0])["reproduced"] >= 2)
    first = site.current_attempts(data)[key][0]
    one = site.badge_of(data, key)
    assert "papers" not in one["text"] and len(one["papers"]) == 1 and one["papers"][0]["relation"] in ("primary", "reuses")
    # A second paper tested on the dataset, verified: its findings are added, and the badge says how many papers.
    n = site.outcome_counts(first)["reproduced"]
    second = {**first, "id": "another-2020-01", "paper": "10.1000/another"}
    data["attempts"].append(second)
    two = site.badge_of(data, key)
    assert two["reproduced"] == 2 * n and two["text"] == f"{2 * n} findings reproduced · 2 papers"
    assert "2 papers" in site.badge_svg(two) and two["alt"].endswith(f"from 2 papers, from {site.dataset_label(key)}")
    # Not yet verified, or set aside: not counted.
    second["tier"] = "runs"
    assert site.badge_of(data, key)["reproduced"] == n
    second["tier"], second["deprecated"] = first["tier"], "to redo"
    assert site.badge_of(data, key)["reproduced"] == n
    first["tier"] = "runs"
    assert site.badge_of(data, key) is None


def test_a_person_has_a_badge_for_the_findings_of_their_papers_reproduced_in_verified_attempts(built):
    data, out = built
    rows = {r["id"]: r for r in json.loads((out / "data" / "authors.json").read_text())}
    with_badge = without = 0
    for orcid, author in site.author_index(data).items():
        badge = site.author_badge(data, author)
        total = sum(site.outcome_counts(a)["reproduced"] for q in author["papers"] for a in q["live"] if a["tier"] != "runs")
        svg = out / "badge" / "authors" / f"{orcid}.svg"
        assert (badge is None) == (total == 0) and svg.is_file() == bool(total) and rows[orcid]["badge"] == (badge or {}).get("text")
        if with_badge + without > 60 and badge and with_badge > 5 and without > 5:
            continue   # the files of a sample of people are read; the rule is checked for everyone
        api = json.loads((out / "api" / "authors" / f"{orcid}.json").read_text())
        page = (out / "authors" / orcid / "index.html").read_text()
        assert api["badge"] == badge and api["orcid"] == orcid and api["name"] == author["name"]
        assert [q["key"] for q in api["papers"]] == [q["key"] for q in author["papers"]]
        assert [d["key"] for d in api["datasets"]] == [d["key"] for d in author["datasets"]]
        # The section is there when the person has any badge: this one, or those with all the outcomes.
        assert ("for this page</h2>" in page) == bool(badge or site.author_outcomes(data, author))
        assert (site.e(f'{orcid}.svg" alt=') in page) == bool(badge)
        if not badge:
            without += 1
            continue
        with_badge += 1
        assert badge["reproduced"] == total == sum(q["reproduced"] for q in badge["papers"])
        papers = len(badge["papers"])
        assert badge["text"] == f'{total} finding{"" if total == 1 else "s"} reproduced' + (f" · {papers} papers" if papers > 1 else "")
        assert badge["url"] == site.SITE_URL + f"authors/{orcid}/" and f">{site.e(badge['text'])}</text>" in svg.read_text()
        # The page has the badge and what to paste to show it, as HTML and as Markdown.
        assert f'[![{site.e(badge["alt"])}]({badge["svg"]})]({badge["url"]})' in page
        assert site.e(f'<a href="{badge["url"]}"><img src="{badge["svg"]}"') in page
    assert with_badge and without
    # A dataset's page offers both forms too.
    assert "Or as Markdown:" in (out / "datasets" / "dandi" / "000003" / "index.html").read_text()


def test_the_authors_list_sorts_by_findings_reproduced(built):
    data, out = built
    page = (out / "authors" / "index.html").read_text()
    config = json.loads(page.split('id="list-config">')[1].split("</script>")[0])
    assert {"key": "-n_reproduced", "label": "Most findings reproduced"} in config["sorts"]
    rows = json.loads((out / "data" / "authors.json").read_text())
    index = site.author_index(data)
    # The number is the one the row's bar shows: the claims reproduced across the person's papers.
    assert all(r["n_reproduced"] == (r["counts"] or {}).get("reproduced", 0) for r in rows)
    assert max(r["n_reproduced"] for r in rows) > 0 and any(r["n_reproduced"] == 0 for r in rows)
    # A row has the outcomes of all the person's papers as one bar, and their first few papers only.
    papers = {x["id"]: x for x in json.loads((out / "data" / "papers.json").read_text())}
    for r in rows[:200]:
        total = {k: sum((papers[q["key"]].get("counts") or {}).get(k, 0) for q in index[r["id"]]["papers"]) for k in site.OUTCOMES}
        assert r["counts"] == (total if sum(total.values()) else None)
    js = (site.ASSETS / "list.js").read_text()
    assert "miniBar(r.counts)" in js and "r.papers.slice(0, SHOWN)" in js and "and ${r.papers.length - SHOWN} more" in js
