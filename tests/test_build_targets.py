"""Tests for tools/build_targets.py: papers named in a dandiset's description."""

from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "tools"))

import build_targets as tool  # noqa: E402


def test_a_paper_named_in_the_description_is_added_after_the_metadata_papers():
    found = [{"doi": "10.1/a", "title": "A", "relation": "IsDescribedBy", "resource_type": "JournalArticle",
              "preprint": False}]
    extra = [{"doi": "10.1/A", "title": "A again"}, {"doi": "10.1101/2024.01.01.1", "title": "B"}]
    papers = tool.with_described(found, extra)
    assert [p["doi"] for p in papers] == ["10.1/a", "10.1101/2024.01.01.1"]
    assert papers[1]["source"] == "description" and papers[1]["preprint"] is True


def test_the_hand_made_list_names_each_dandiset_once_with_a_doi_and_a_note():
    listed = tool.described()
    assert listed, "targets/description_papers.yaml is empty"
    for dandiset, papers in listed.items():
        assert len(dandiset) == 6 and dandiset.isdigit()
        assert all(p["doi"].startswith("10.") and p.get("title") and p.get("note") for p in papers)
