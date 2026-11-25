"""Tests for tools/build_zenodo_targets.py: how records are named and what a record's metadata gives."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "tools"))

import build_zenodo_targets as tool  # noqa: E402


@pytest.mark.parametrize("text, expected", [
    ("3924718", ("3924718", "")),
    ("ZENODO:3924718", ("3924718", "")),
    ("10.5281/zenodo.17624449", ("17624449", "")),
    ("https://doi.org/10.5281/zenodo.17624449=10.7554/eLife.41877", ("17624449", "10.7554/elife.41877")),
    ("https://zenodo.org/records/17794764/", ("17794764", "")),
    ("https://zenodo.org/record/3924718=https://doi.org/10.1/X", ("3924718", "10.1/x")),
])
def test_the_zenodo_builder_takes_an_id_a_doi_or_a_page(text, expected):
    assert tool.parse(text) == expected


def test_anything_else_is_refused():
    with pytest.raises(SystemExit):
        tool.parse("https://osf.io/r7aes/")


def test_a_checksum_gives_an_md5_only_when_it_is_one():
    assert tool.md5_of("md5:" + "A" * 32) == "a" * 32
    assert tool.md5_of("sha256:" + "a" * 64) is None and tool.md5_of(None) is None


def test_papers_come_from_the_doi_given_and_related_articles_and_code_from_github(monkeypatch):
    monkeypatch.setattr(tool, "title_of", lambda doi: ("T", doi.startswith("10.1101/")))
    meta = {"related_identifiers": [
        {"identifier": "10.7554/eLife.41877", "relation": "isSupplementTo", "scheme": "doi"},
        {"identifier": "10.1101/2020.01.01.000001", "relation": "isDescribedBy", "scheme": "doi"},
        {"identifier": "10.5281/zenodo.111", "relation": "isSupplementTo", "scheme": "doi"},   # another record
        {"identifier": "https://github.com/lab/code/tree/v1", "relation": "isSupplementTo", "scheme": "url"},
        {"identifier": "10.1/cites", "relation": "cites", "scheme": "doi"}]}
    papers, code = tool.papers_of("10.1/given", meta)
    assert [p["doi"] for p in papers] == ["10.1/given", "10.7554/elife.41877", "10.1101/2020.01.01.000001"]
    assert papers[0]["relation"] == "given" and papers[2]["preprint"] and not papers[1]["preprint"]
    assert code == ["https://github.com/lab/code/tree/v1"]


def test_a_data_paper_the_record_is_published_in_is_a_paper(monkeypatch):
    # ZENODO:15878620 names its Data in Brief article this way.
    monkeypatch.setattr(tool, "title_of", lambda doi: ("T", False))
    meta = {"related_identifiers": [{"identifier": "10.1016/j.dib.2025.111305", "relation": "isPublishedIn",
                                     "scheme": "doi", "resource_type": "publication-article"}]}
    papers, _ = tool.papers_of("", meta)
    assert [(p["doi"], p["relation"]) for p in papers] == [("10.1016/j.dib.2025.111305", "isPublishedIn")]


def test_every_version_is_listed_oldest_first_page_by_page_at_most_25_to_a_page(monkeypatch):
    # Zenodo answers size=100 with 400 Bad Request, which left only the record itself in version_ids.
    first = f"{tool.API}/records/30/versions?size=25&sort=oldest"
    second = f"{tool.API}/records/30/versions?page=2&size=25&sort=oldest"
    responses = {first: {"hits": {"hits": [{"id": 10}, {"id": 20}]}, "links": {"next": second}},
                 second: {"hits": {"hits": [{"id": 30}]}, "links": {}}}
    monkeypatch.setattr(tool, "get", lambda url: responses[url])
    assert tool.version_ids({"id": 30}) == ["10", "20", "30"]
