"""Tests for tools/runner/describe.py: the choices the queue runner makes."""

from __future__ import annotations

import os
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
    # Any account's runs carry its name, the API key's too; another dataset's runs are not taken.
    runs = [{"databaseId": 7, "displayTitle": "Agent run: 001636 author (api)", "status": "in_progress"},
            {"databaseId": 6, "displayTitle": "Agent run: 0016361 author", "status": "completed"}]
    assert describe.newest_run(runs, "001636", "author") == "7 in_progress"
    assert describe.newest_run(runs[1:], "001636", "author") == ""


def test_only_published_datasets_are_taken():
    assert describe.published({"archive": "dandi", "published_version": "0.260521.2201"})
    assert not describe.published({"archive": "dandi", "published_version": None})
    # The other archives publish every dataset they list, and have no versions of this kind.
    assert describe.published({"archive": "crcns"})


def test_the_queue_is_of_papers(monkeypatch):
    t = lambda id_: {"archive": "dandi", "id": id_, "key": f"dandi:{id_}", "folder": id_, "published_version": "1",
                     "papers": [{"doi": "10.1038/x", "preprint": False}]}
    # 000001 and 000002 hold one paper's data; 000003 another's; 000004 is not matched yet; 000005's paper has
    # its only attempt deprecated.
    monkeypatch.setattr(describe, "main_targets", lambda: [t(f"00000{i}") for i in range(1, 6)])
    monkeypatch.setattr(describe, "main_papers", lambda: (
        {"dandi:000001": "a-2020", "dandi:000002": "a-2020", "dandi:000003": "b-2021", "dandi:000005": "c-2022"},
        {"a-2020": ["dandi:000001", "dandi:000002"], "b-2021": ["dandi:000003"], "c-2022": ["dandi:000005"],
         "r-2024": ["dandi:000003"]}))
    attempts = {"a-2020": [{"id": "a-2020-01", "deprecated": False, "datasets": {"dandi:000001"}}],
                "b-2021": [{"id": "b-2021-01", "deprecated": False, "datasets": {"dandi:000003"}}],
                "c-2022": [{"id": "c-2022-01", "deprecated": True, "datasets": {"dandi:000005"}}]}
    monkeypatch.setattr(describe, "main_attempts", lambda: attempts)
    monkeypatch.setattr(describe, "branches", lambda: set())
    monkeypatch.setattr(describe, "matched_on_main", lambda: {"000001", "000002", "000003", "000005"})
    monkeypatch.setattr(describe, "main_yaml", lambda path: {"papers": [{"key": "r-2024"}]} if path == "targets/reuse.yaml" else {})
    # a-2020 is open, once, for its untested dataset; b-2021 is done; the unmatched dataset goes by its folder;
    # c-2022 is open again; the reuse paper comes last.
    assert describe.queue() == ["a-2020", "000004", "c-2022", "r-2024"]
    # Once a-2020's attempt has used both datasets it is done, and a paper with a branch is taken.
    attempts["a-2020"].append({"id": "a-2020-02", "deprecated": False, "datasets": {"dandi:000001", "dandi:000002"}})
    monkeypatch.setattr(describe, "branches", lambda: {"c-2022"})
    assert describe.queue() == ["000004", "r-2024"]
    assert describe.as_folders(["a-2020", "000004"], describe.main_papers()[1]) == ["000001", "000002", "000004"]


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


def _git(cwd, *args):
    import subprocess
    return subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@example.org", *args], cwd=cwd, check=True,
                          capture_output=True, text=True).stdout


def _finish_sandbox(tmp_path, branch_change, main_change):
    """An origin with main and attempt/x, a clone of it, and chain.sh's merge_main run in the clone."""
    import subprocess
    origin, clone = tmp_path / "origin.git", tmp_path / "clone"
    _git(tmp_path, "init", "-q", "--bare", "-b", "main", str(origin))
    _git(tmp_path, "clone", "-q", str(origin), str(clone))
    (clone / "claims").mkdir()
    (clone / "README.md").write_text("registry\n")
    _git(clone, "add", "-A"); _git(clone, "commit", "-q", "-m", "start"); _git(clone, "push", "-q", "origin", "HEAD:main")
    _git(clone, "checkout", "-q", "-b", "attempt/x")
    for name, text in branch_change.items():
        (clone / name).parent.mkdir(exist_ok=True); (clone / name).write_text(text)
    _git(clone, "add", "-A"); _git(clone, "commit", "-q", "-m", "attempt"); _git(clone, "push", "-q", "origin", "attempt/x")
    _git(clone, "checkout", "-q", "main")
    for name, text in main_change.items():
        (clone / name).parent.mkdir(exist_ok=True); (clone / name).write_text(text)
    _git(clone, "add", "-A"); _git(clone, "commit", "-q", "-m", "main moves"); _git(clone, "push", "-q", "origin", "main")
    # The clone's own checkout is left on another branch, as the runner's is, and must not be touched.
    _git(clone, "checkout", "-q", "-b", "elsewhere")
    chain = (REPO / "tools" / "runner" / "chain.sh").read_text()
    body = chain[chain.index("drop_work(){"):chain.index('log "finishing"')]
    script = ('set -uo pipefail\nd=x\nwork=$(mktemp -d)\nnotify(){ :; }\n'
              'fetch(){ git fetch -q origin main "attempt/$d"; }\n' + body + 'merge_main; rc=$?\n'
              'echo "rc=$rc"; [ $rc = 0 ] && git -C "$work" log -1 --format=%s; drop_work\n')
    out = subprocess.run(["bash", "-c", script], cwd=clone, capture_output=True, text=True,
                         env={**os.environ, "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@example.org",
                              "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@example.org"}).stdout
    _git(clone, "fetch", "-q", "origin")
    return out, clone


def test_finishing_merges_main_in_a_worktree_and_leaves_the_clone_alone(tmp_path):
    out, clone = _finish_sandbox(tmp_path, {"entries/x.txt": "entry\n"}, {"docs/other.md": "another attempt\n"})
    assert "rc=0" in out
    files = _git(clone, "ls-tree", "-r", "--name-only", "origin/attempt/x").split()
    assert "entries/x.txt" in files and "docs/other.md" in files       # main is merged in, and pushed
    assert _git(clone, "rev-parse", "--abbrev-ref", "HEAD").strip() == "elsewhere"   # the clone's checkout is as it was
    assert len(_git(clone, "worktree", "list").strip().splitlines()) == 1            # and the worktree is gone


def test_finishing_keeps_the_branchs_claims_file_and_stops_on_any_other_conflict(tmp_path):
    # Main has the checked claims already (the checkpoint); the branch's file is the same or later, and is kept.
    (tmp_path / "a").mkdir()
    out, clone = _finish_sandbox(tmp_path / "a", {"claims/x.yaml": "claims: later\n"}, {"claims/x.yaml": "claims: checkpoint\n"})
    assert "rc=0" in out and _git(clone, "show", "origin/attempt/x:claims/x.yaml") == "claims: later\n"
    (tmp_path / "b").mkdir()
    out, clone = _finish_sandbox(tmp_path / "b", {"README.md": "branch\n"}, {"README.md": "main\n"})
    assert "rc=1" in out
    assert _git(clone, "show", "origin/attempt/x:README.md") == "branch\n"          # nothing was pushed

