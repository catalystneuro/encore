"""Tests for tools/paper_match.py: whether each paper a dataset names is the paper behind its data."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "tools"))

import agent_run  # noqa: E402
import paper_match as pm  # noqa: E402

TITLE = "Responses of pyramidal cell somata and apical dendrites in mouse visual cortex over multiple days"


def target(papers, id_="000336"):
    return {"archive": "dandi", "id": id_, "key": f"dandi:{id_}", "folder": id_, "name": "A dataset",
            "papers": papers}


def paper(doi, relation="IsDescribedBy", title=TITLE, preprint=False):
    return {"doi": doi, "title": title, "relation": relation, "preprint": preprint}


def text(body):
    return f"{TITLE}\nGillon, Lecoq et al.\n\n{body}"


def test_the_datasets_a_paper_names_are_found():
    found = pm.archives_named("deposited on DANDI (https://dandiarchive.org/dandiset/000037), see also DANDI:000021, "
                              "dandiset 000022, doi:10.48324/dandi.000037/0.230426.0054 and OpenNeuro ds003374")
    assert found == ["DANDI:000037", "DANDI:000021", "DANDI:000022", "OpenNeuro:ds003374"]
    assert pm.archives_named("recorded in 2023 from 120 mice") == []


def test_a_paper_that_names_only_this_dataset_is_primary():
    row = pm.check(target([]), paper("10.1/a", relation="Describes"), text("Data are on DANDI:000336."))
    assert row["verdict"] == "primary" and row["by"] == "checks"


def test_a_paper_described_by_the_dataset_that_names_no_dataset_is_primary():
    row = pm.check(target([]), paper("10.1/a"), text("Data are available from the authors."))
    assert row["verdict"] == "primary"
    # The same paper under a looser relation is left for the agent.
    assert "verdict" not in pm.check(target([]), paper("10.1/a", relation="IsSupplementTo"), text("No data named."))


def test_a_paper_that_names_another_dataset_is_left_for_the_agent():
    # DANDI:000336 names Gillon et al. 2023, whose data are DANDI:000037.
    row = pm.check(target([]), paper("10.1/a", relation="Describes"),
                   text("The full dataset is on the DANDI Archive (https://dandiarchive.org/dandiset/000037)."))
    assert "verdict" not in row and row["checks"]["names_others"] == ["DANDI:000037"]
    # Named with others, it is still for the agent to say whether the match is partial.
    row = pm.check(target([]), paper("10.1/a"), text("Data are in DANDI:000336 and DANDI:000337."))
    assert "verdict" not in row


def test_a_paper_whose_text_does_not_carry_its_title_is_left_for_the_agent():
    # A mistyped DOI: the text is another paper.
    row = pm.check(target([]), paper("10.1/a"), "Energy complexity of convolutional neural networks\n\nNo data.")
    assert "verdict" not in row and row["checks"]["title_in_text"] is False
    assert pm.check(target([]), paper("10.1/a"), None) == {"doi": "10.1/a", "relation": "IsDescribedBy",
                                                           "checks": {"text": False}}


def test_the_checks_keep_earlier_verdicts(tmp_path):
    (tmp_path / "10.1-a.txt").write_text(text("Data are on DANDI:000336."))
    t = target([paper("10.1/a"), paper("10.1/b")])
    earlier = {"papers": [{"doi": "10.1/b", "verdict": "background", "by": "agent", "reason": "A review.",
                           "evidence": [{"source": "abstract"}], "confirmed": True}]}
    rows = pm.run_checks(t, {}, tmp_path, earlier)["papers"]
    assert rows[0]["verdict"] == "primary" and rows[1] == earlier["papers"][0]


def test_the_match_status_and_the_papers_to_use():
    t = target([paper("10.1/review", relation="Describes"), paper("10.1/pre", preprint=True), paper("10.1/pub")])
    status, papers = pm.choose(t, {}, None)
    assert status == "unchecked" and [p["doi"] for p in papers] == ["10.1/review", "10.1/pub", "10.1/pre"]
    verdict = lambda doi, v, **kw: {"doi": doi, "verdict": v, **kw}
    match = {"papers": [verdict("10.1/review", "background"), verdict("10.1/pre", "primary"),
                        verdict("10.1/pub", "partial")]}
    status, papers = pm.choose(t, {}, match)
    assert status == "matched" and [p["doi"] for p in papers] == ["10.1/pre", "10.1/pub"]
    # No usable paper: held until a person confirms every verdict.
    match = {"papers": [verdict("10.1/review", "background"), verdict("10.1/pre", "other_data", confirmed=True),
                        verdict("10.1/pub", "other_data")]}
    assert pm.choose(t, {}, match) == ("held", [])
    match["papers"][0]["confirmed"] = match["papers"][2]["confirmed"] = True
    assert pm.choose(t, {}, match) == ("no_match", [])
    # A paper not yet judged: unchecked.
    assert pm.choose(t, {}, {"papers": match["papers"][:2]})[0] == "unchecked"
    # A paper a person names in triage is used whatever the match says.
    status, papers = pm.choose(t, {"papers": {"10.1/right": "The paper."}}, match)
    assert status == "matched" and papers[0]["doi"] == "10.1/right"


def test_the_schema_wants_evidence_for_a_verdict_that_sets_a_paper_aside():
    schema = Draft202012Validator(json.loads((REPO / "schemas" / "paper-match.schema.json").read_text()))
    base = {"schema_version": 1, "dataset": {"archive": "dandi", "id": "000336"}, "date": "2026-10-28"}
    good = {**base, "papers": [
        {"doi": "10.1038/s41597-023-02214-y", "relation": "Describes", "verdict": "other_data", "by": "agent",
         "reason": "Its data are dandiset 000037.", "data_in": ["DANDI:000037"],
         "evidence": [{"source": "Data Records", "quote": "https://dandiarchive.org/dandiset/000037"}]},
        {"doi": "10.1/a", "verdict": "primary", "by": "checks", "reason": "Names only this dataset."}]}
    assert not list(schema.iter_errors(good))
    bad = {**base, "papers": [{"doi": "10.1/a", "verdict": "other_data", "by": "agent"}]}
    assert list(schema.iter_errors(bad))


def test_the_paper_match_prompt_lists_the_papers():
    text = agent_run.fill("paper-match", "000336", "m")
    assert "doi:10.1038/s41597-023-02214-y" in text and "papers/match/000336.yaml" in text
    assert "api.dandiarchive.org/api/dandisets/000336/versions/" in text
    # Triage set the reviews aside: they are not listed.
    assert "10.1016/j.tins.2012.11.006" not in text and "{" not in text.replace("{source, quote}", "")


def test_an_attempt_uses_the_matched_paper(monkeypatch):
    match = {"papers": [{"doi": "10.1038/s41597-023-02214-y", "verdict": "other_data"}]}
    monkeypatch.setattr(pm, "load", lambda folder: match)
    import pytest
    with pytest.raises(SystemExit, match="no paper matches dataset DANDI:000336"):
        agent_run.target("000336")
    match["papers"][0]["verdict"] = "primary"
    assert agent_run.target("000336")["paper"] == "10.1038/s41597-023-02214-y"


def test_every_match_file_validates():
    files = sorted((REPO / "papers" / "match").glob("*.yaml"))
    if files:
        assert pm.validate(files) == 0
    for f in files:
        assert yaml.safe_load(f.read_text())["dataset"]["id"] == f.stem.split("-", 1)[-1]
