"""Tests for tools/runner/describe.py: the choices the queue runner makes."""

from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "tools" / "runner"))

import describe  # noqa: E402


def test_a_role_that_never_ran_has_no_run():
    runs = [{"databaseId": 1, "displayTitle": "Agent run: 001636 author", "status": "completed"}]
    assert describe.newest_run(runs, "001636", "recorder") == ""
    assert describe.newest_run([], "001636", "author") == ""


def test_the_newest_run_of_a_role_is_found():
    runs = [{"databaseId": 3, "displayTitle": "Agent run: 001636 recorder", "status": "in_progress"},
            {"databaseId": 2, "displayTitle": "Agent run: 001933 recorder", "status": "completed"},
            {"databaseId": 1, "displayTitle": "Agent run: 001636 recorder", "status": "completed"}]
    assert describe.newest_run(runs, "001636", "recorder") == "3 in_progress"


def test_a_run_on_either_account_is_found():
    runs = [{"databaseId": 5, "displayTitle": "Paper run: 001636 claims", "status": "queued"},
            {"databaseId": 4, "displayTitle": "Paper run: 001636 claims (unverified)", "status": "completed"}]
    assert describe.newest_run(runs, "001636", "claims") == "5 queued"
    assert describe.newest_run(runs[1:], "001636", "claims") == "4 completed"
    assert describe.newest_run(runs, "001636", "claims-check") == ""


def test_only_published_datasets_are_taken():
    assert describe.published({"archive": "dandi", "published_version": "0.260521.2201"})
    assert not describe.published({"archive": "dandi", "published_version": None})
    # The other archives publish every dataset they list, and have no versions of this kind.
    assert describe.published({"archive": "crcns"})


def test_a_dataset_whose_latest_attempt_is_deprecated_is_open_again(monkeypatch):
    records = ["000001-demo-2020-01.yaml", "000001-demo-2020-02.yaml", "000002-demo-2021-01.yaml"]
    deprecated = {"attempts/000001-demo-2020-01.yaml", "attempts/000002-demo-2021-01.yaml"}
    monkeypatch.setattr(describe, "main_yaml", lambda path: {"deprecated": {"date": "2026-10-21"}} if path in deprecated else {})
    # 000001 has a newer attempt that stands; 000002's only attempt is deprecated.
    assert not describe.latest_deprecated("000001", records)
    assert describe.latest_deprecated("000002", records)
    assert not describe.latest_deprecated("000003", records)
