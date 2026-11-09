"""Tests for tools/notify.py: the needs-you issue a runner chain opens, updates or closes."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "tools"))

import notify  # noqa: E402


def run(*args: str) -> str:
    return subprocess.run([sys.executable, str(REPO / "tools" / "notify.py"), *args, "--dry-run"],
                          check=True, capture_output=True, text=True).stdout


def test_an_issue_is_named_by_the_dataset():
    assert notify.title("000147") == "DANDI:000147: waiting on you"
    assert notify.title("crcns-ret-1") == "CRCNS:ret-1: waiting on you"


def test_a_stop_opens_an_issue_that_says_what_stopped_it(monkeypatch):
    monkeypatch.setattr(notify, "branch_file", lambda folder, path: None)
    text = notify.body("000147", "000147 STOPPED at author", "the run of author failed", "123", "someone")
    assert text.startswith("@someone The runner stopped on DANDI:000147")
    assert "**What stopped it:** at author" in text and "**Why:** the run of author failed" in text
    assert "/actions/runs/123)" in text and "tools/runner/chain.sh 000147" in text
    assert "@" not in notify.body("000147", "000147 STOPPED at author", "", "", "").split("\n")[0]


def test_a_stop_at_the_claims_quotes_the_readers_report(monkeypatch):
    files = {"transcripts/000147/claims-report.md": "I wrote no claims: the supplement is missing."}
    monkeypatch.setattr(notify, "branch_file", lambda folder, path: files.get(path))
    text = notify.body("000147", "000147 STOPPED: the reader wrote no claims file; see ...", "", "", "")
    assert "The reader's report" in text and "the supplement is missing" in text


def test_a_merge_closes_the_issue_and_a_failed_check_links_the_pull_request():
    assert "would close" in run("000147", "000147 MERGED https://github.com/o/r/pull/9")
    assert "would close" in run("000147", "000147 CLAIMS MERGED")
    out = run("000147", "000147 CHECKS FAILED https://github.com/o/r/pull/9")
    assert "would open" in out and "[the pull request](https://github.com/o/r/pull/9)" in out
