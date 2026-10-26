"""Tests for tools/datasets.py: how datasets are named, keyed and filed."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "tools"))

import datasets  # noqa: E402


@pytest.mark.parametrize("text", ["000003", "dandi:000003", "DANDI:000003", "Dandi:000003"])
def test_every_way_of_writing_a_dandi_dataset_gives_one_key(text):
    assert datasets.parse(text) == "dandi:000003"


def test_another_archive_is_filed_under_archive_and_id():
    key = datasets.parse("example:abc-123")
    assert key == "example:abc-123" and datasets.folder(key) == "example-abc-123"
    assert datasets.parse("example-abc-123") == key and datasets.label(key) == "EXAMPLE:abc-123"


def test_dandi_keeps_its_bare_folders_and_links():
    assert datasets.folder("dandi:000003") == "000003" and datasets.key_of_folder("000003") == "dandi:000003"
    assert datasets.url("dandi:000003") == "https://dandiarchive.org/dandiset/000003"


@pytest.mark.parametrize("text", ["3", "dandi:", "../000003", "dandi:00 3", "x"])
def test_anything_else_is_refused(text):
    with pytest.raises(ValueError):
        datasets.parse(text)


def test_targets_carry_their_key_and_folder():
    found = datasets.targets()
    assert found and all(t["key"] == f"{t['archive']}:{t['id']}" and t["folder"] == datasets.folder(t["key"])
                         for t in found)


def test_a_crcns_dataset_is_a_target_with_its_own_page():
    ret = next(t for t in datasets.targets() if t["key"] == "crcns:ret-1")
    assert ret["folder"] == "crcns-ret-1" and datasets.label(ret["key"]) == "CRCNS:ret-1"
    assert datasets.url(ret["key"]) == "https://crcns.org/data-sets/retina/ret-1"
    assert "crcnsarchive" in datasets.access(ret["key"])


def test_an_ebrains_dataset_is_named_by_its_doi_and_read_by_its_kg_id():
    key = datasets.parse("EBRAINS:Q0FG-1X8")
    found = next(t for t in datasets.targets() if t["key"] == key)
    assert key == "ebrains:q0fg-1x8" and found["folder"] == "ebrains-q0fg-1x8"
    assert datasets.label(key) == "EBRAINS:Q0FG-1X8" and datasets.parse("ebrains-q0fg-1x8") == key
    assert f'/public/datasets/{found["kg_id"]}/' in datasets.access(key)


def test_a_key_ignores_the_case_of_an_identifier_that_ignores_case():
    assert datasets.key_of("ebrains", "Q0FG-1X8") == datasets.key_of("ebrains", "q0fg-1x8") == "ebrains:q0fg-1x8"
    assert datasets.key_of("crcns", "ret-1") == "crcns:ret-1"


def test_a_dryad_dataset_is_named_by_its_doi_and_pinned_by_its_version_id():
    key = datasets.parse("DRYAD:BVQ83BKK9")
    found = next(t for t in datasets.targets() if t["key"] == key)
    assert key == "dryad:bvq83bkk9" and found["folder"] == "dryad-bvq83bkk9"
    assert datasets.label(key) == "DRYAD:bvq83bkk9" and datasets.parse("dryad-bvq83bkk9") == key
    assert found["doi"] == "10.5061/dryad.bvq83bkk9"
    assert f'/versions/{found["published_version"]}/files' in datasets.access(key)
