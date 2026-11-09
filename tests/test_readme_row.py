"""Tests for tools/readme_row.py: the README row of a dandiset's latest attempt."""

from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "tools"))

import readme_row as tool  # noqa: E402


def test_the_row_counts_the_findings_on_the_dataset():
    assert tool.row("001933").startswith("| [001933](")
    # 001933's one claim with outside data is its link to the paper's source data, which the table leaves out.
    assert "(+" not in tool.row("001933")
    assert "| 6 (+1) |" not in tool.row("000004") and "| 8 (+1) |" in tool.row("000004")


def test_a_deprecated_attempts_row_has_no_counts(monkeypatch):
    record, entry_dir = tool.attempt_of("001933")
    monkeypatch.setattr(tool, "attempt_of", lambda _: (dict(record, deprecated=True), entry_dir))
    assert "| – | – | – | – |" in tool.row("001933") and tool.row("001933").endswith("(deprecated) |")
