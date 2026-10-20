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
    key = datasets.parse("ebrains:abc-123")
    assert key == "ebrains:abc-123" and datasets.folder(key) == "ebrains-abc-123"
    assert datasets.parse("ebrains-abc-123") == key and datasets.label(key) == "EBRAINS:abc-123"


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
