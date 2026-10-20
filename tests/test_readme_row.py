"""Tests for tools/readme_row.py: the README row of a dandiset's latest attempt."""

from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "tools"))

import readme_row as tool  # noqa: E402


def test_the_row_matches_the_readme():
    readme = (REPO / "README.md").read_text()
    assert tool.row("001933") in readme
    # 001933's one claim with outside data is its link to the paper's source data, which the table leaves out.
    assert "(+" not in tool.row("001933")
    assert "| 6 (+1) |" not in tool.row("000004") and "| 8 (+1) |" in tool.row("000004")


def test_a_deprecated_attempts_row_has_no_counts(monkeypatch):
    record, entry_dir = tool.attempt_of("001933")
    monkeypatch.setattr(tool, "attempt_of", lambda _: (dict(record, deprecated=True), entry_dir))
    assert "| – | – | – | – |" in tool.row("001933") and tool.row("001933").endswith("(deprecated) |")


def test_writing_replaces_a_dandisets_row_or_adds_one(tmp_path):
    readme = tmp_path / "README.md"
    readme.write_text((REPO / "README.md").read_text().replace(tool.row("001933"), tool.row("001933").replace(
        "| 6 |", "| 0 |")))
    tool.write("001933", readme)
    text = readme.read_text()
    assert text.count("dandiarchive.org/dandiset/001933)") == 1 and tool.row("001933") in text
    lines = [line for line in text.splitlines() if "dandiarchive.org/dandiset/002013)" not in line]
    readme.write_text("\n".join(lines) + "\n")
    tool.write("002013", readme)
    rows = [line for line in readme.read_text().splitlines() if line.startswith("| [")]
    assert rows[-1] == tool.row("002013")
