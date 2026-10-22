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


def test_a_target_with_a_journal_paper_has_a_publication():
    preprint = {"papers": [{"doi": "10.1101/2024.01.01.000001", "preprint": True}]}
    journal = {"papers": [{"doi": "10.1038/s41586-024-00001-1", "preprint": False}]}
    assert describe.has_publication(journal, {})
    assert not describe.has_publication(preprint, {})
    # papers/triage.yaml can replace the preprint with its publication, or rule a paper out.
    assert describe.has_publication(preprint, {"not_papers": {"10.1101/2024.01.01.000001": ""},
                                               "papers": {"10.7554/elife.00001": ""}})
    assert not describe.has_publication(journal, {"not_papers": {"10.1038/s41586-024-00001-1": ""}})


def test_a_chain_takes_from_its_first_run_to_its_last():
    def run(dataset, role, start, end, conclusion="success"):
        return {"displayTitle": f"Agent run: {dataset} {role}", "createdAt": f"2026-10-21T{start}:00Z",
                "updatedAt": f"2026-10-21T{end}:00Z", "conclusion": conclusion}
    runs = [run("000001", "author", "01:00", "02:00"), run("000001", "recorder", "04:00", "05:00"),
            run("000002", "claims", "01:00", "01:10"), run("000002", "claims-check", "01:10", "01:20")]
    runs[3]["displayTitle"] = "Paper run: 000002 claims-check (unverified)"
    assert describe.chain_hours(runs) == {"full": 4.0, "claims": 20 / 60}
    # Two lists written one after the other, as two `gh run list` calls write them.
    assert describe.json_lists('[1, 2]\n[3]\n') == [1, 2, 3]


def test_a_running_chain_has_left_what_the_rest_of_a_chain_usually_takes():
    import datetime
    def run(dataset, role, start, end, status="completed"):
        return {"displayTitle": f"Agent run: {dataset} {role}", "createdAt": f"2026-10-21T{start}:00Z",
                "updatedAt": f"2026-10-21T{end}:00Z", "conclusion": "success" if status == "completed" else "",
                "status": status}
    runs = [run("000001", "author", "01:00", "02:00"), run("000001", "verifier-1", "02:00", "03:00"),
            run("000001", "recorder", "04:00", "05:00"),
            run("000002", "author", "10:00", "11:00"), run("000002", "verifier-1", "11:00", "11:30", "in_progress"),
            run("000003", "claims", "11:00", "11:10", "in_progress"), run("000004", "claims", "11:00", "11:10", "queued")]
    now = datetime.datetime(2026, 10, 21, 11, 30, tzinfo=datetime.timezone.utc)
    going = describe.running(runs, {"000002", "000003"}, {"full": 1, "claims": 1}, now)
    # A finished chain's end came 3 hours after its verifier started; this verifier has run half an hour.
    assert going["000002"] == {"kind": "full", "hours": 2.5}
    # The one full lane is taken, so a chain only reading claims is the claims runner's; with no finished
    # claims chain to go by, it has no estimate. A dataset with no open branch is left out.
    assert going["000003"] == {"kind": "claims", "hours": None} and "000004" not in going
