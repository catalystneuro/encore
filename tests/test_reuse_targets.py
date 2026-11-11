"""Tests for tools/build_reuse_targets.py: which reuse papers become targets."""

from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "tools"))

import build_reuse_targets as tool  # noqa: E402


def pair(doi, ds="000469", **kw):
    base = {"classification": "REUSE", "confidence": 10, "same_lab": False, "source_archive": "DANDI Archive",
            "reuse_type": "NOVEL_ANALYSIS", "citing_doi": doi, "dandiset_id": ds, "title": "T",
            "reasoning": "r", "evidence_quotes": [{"quote": "q", "verbatim": True}]}
    return {**base, **kw}


def test_only_papers_that_took_one_dandiset_from_dandi_for_a_finding_are_taken():
    found = [pair("10.1/a"),
             pair("10.1/crcns", source_archive="CRCNS"),          # the same recordings from another archive
             pair("10.1/lab", same_lab=True),                       # the data's own lab
             pair("10.1/tool", reuse_type="TOOL_DEMO"),             # claims about a method
             pair("10.1/two"), pair("10.1/two", ds="000055"),      # reuses two dandisets
             pair("10.1/other", ds="999999"),                       # not a target
             pair("10.1/primary"),                                  # already a primary paper
             pair("10.1/a")]                                        # the same pair twice
    picked = tool.candidates(found, {"000469", "000055"}, {"10.1/primary"})
    assert [p["doi"] for p in picked] == ["10.1/a"] and picked[0]["quote"] == "q"
