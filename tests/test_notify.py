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
    monkeypatch.setattr(notify, "failed_run", lambda run, lines=30: {"steps": [], "log": ""})
    text = notify.body("000147", "000147 STOPPED at author", "the run of author failed", "123", "someone")
    assert text.startswith("@someone The runner stopped on DANDI:000147")
    assert "**What stopped it:** at author" in text and "**Why:** The run of `author` failed." in text
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



def test_a_failed_run_says_which_step_failed_shows_its_log_and_what_to_do(monkeypatch):
    monkeypatch.setattr(notify, "branch_file", lambda folder, path: None)
    monkeypatch.setattr(notify, "failed_run", lambda run, lines=30: {
        "steps": ['job `run`, step "Run the agent"'], "log": "the agent timed out after 240 minutes"})
    text = notify.body("000147", "000147 STOPPED at author-revise-1", "the run of author-revise-1 failed", "5", "")
    assert 'ran out of time in `author-revise-1` (job `run`, step "Run the agent")' in text
    assert "**What you can do:**\n1. " in text and "put `000147` first in the runner's queue" in text
    assert "the agent timed out after 240 minutes" in text and "The end of the failed step's log" in text


def test_failed_checks_are_named_and_a_failing_repository_test_is_told_apart_from_the_entry(monkeypatch):
    monkeypatch.setattr(notify, "branch_file", lambda folder, path: None)
    pr = "https://github.com/o/r/pull/9"
    monkeypatch.setattr(notify, "failed_checks", lambda url: [
        {"name": "check", "workflow": "Check entries", "link": "https://github.com/o/r/actions/runs/7/job/8", "run": "7"}])
    logs = {"own": "FAILED tests/test_build_site.py::test_x - StopIteration", "entry": "FAIL  reproduce.ipynb  (8 s)"}
    for kind, told in (("own", "one of the repository's own tests"), ("entry", "fix it on the branch `attempt/000147`")):
        monkeypatch.setattr(notify, "failed_run", lambda run, lines=30: {
            "steps": ['job `check`, step "Unit tests"'], "log": logs[kind]})
        text = notify.body("000147", f"000147 CHECKS FAILED {pr}", "", "", "")
        assert "[Check entries / check](https://github.com/o/r/actions/runs/7/job/8) failed" in text
        assert told in text and "`gh run rerun 7 --failed`" in text and f"merge {pr}" in text and logs[kind] in text


def test_each_stop_that_needs_a_person_says_what_to_do(monkeypatch):
    monkeypatch.setattr(notify, "branch_file", lambda folder, path: None)
    for status, told in (
            ("STOPPED: the reader wrote no claims file; see transcripts/000147/claims-report.md", "paper store"),
            ("STOPPED: the claims check says the claims file is not ready", "claims/000147.yaml"),
            ("STOPPED: no paper matches the dataset; see papers/match/000147.yaml", "confirmed: true"),
            ("STOPPED: most claims are on data elsewhere", "papers/datasets/000147.yaml"),
            ("STOPPED: the pull request conflicts with main (https://github.com/o/r/pull/9)", "Merge `main` into"),
            ("STOPPED: could not push attempt/000147 after merging main", "GitHub is up")):
        text = notify.body("000147", f"000147 {status}", "", "", "")
        assert "**Why:** " in text and "**What you can do:**" in text and told in text, status
