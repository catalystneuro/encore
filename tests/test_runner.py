"""Tests for tools/runner/describe.py: the choices the queue runner makes."""

from __future__ import annotations

import os
import subprocess
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


def test_one_chain_at_a_time_holds_a_paper(tmp_path):
    # Issue 749: two lanes took two datasets of one paper, and the second chain joined the first's attempt. A chain
    # holds $STATE/chain-<paper>.lock while it runs; another chain on the paper is refused, a replicate has a lock
    # of its own, and a lock whose process has died is taken over.
    chain = (REPO / "tools" / "runner" / "chain.sh").read_text()
    funcs = chain[chain.index('held=""\nhold(){'):chain.index("trap 'release; notify' EXIT")]
    def run(body):
        return subprocess.run(["bash", "-c", f"set -uo pipefail\nSTATE={tmp_path}\n{funcs}\n{body}"],
                              capture_output=True, text=True).stdout.split()
    # Another process (a bash of its own, with its own $$) is refused while this one holds the paper; a replicate
    # has a lock of its own; released, the lock is gone.
    other = f'bash -c "STATE={tmp_path}; $(declare -f hold); hold wirth-2017 && echo second || echo refused-\\$holder"'
    out = run(f"hold wirth-2017 && echo got-$$; {other}; hold wirth-2017/r1 && echo replicate; "
              "release; ls $STATE | grep -c wirth-2017 || true")
    assert out[0].startswith("got-") and out[1] == "refused-" + out[0][4:] and out[2] == "replicate", out
    # A lock left by a process that has died is taken over.
    (tmp_path / "chain-gao-2018.lock").mkdir()
    (tmp_path / "chain-gao-2018.lock" / "pid").write_text("999999\n")
    assert run("hold gao-2018 && echo took-over") == ["took-over"]
    # Both places a chain learns its paper take the lock before touching anything of it.
    body = chain[chain.index("set -uo pipefail"):]
    assert 'if [ -n "$is_paper" ] && ! hold "$tag"; then' in body
    switch = body.index('going on as $p"')
    assert switch < body.index('if ! hold "$p"; then') < body.index('mv "$mark" "$STATE/attempt-$p"')
    assert body.count("release; notify' EXIT") == 2


def test_a_failure_of_githubs_artifact_service_is_github_failing():
    # Issue 702: upload-artifact got a web page for JSON five times and failed the run; the chain then stopped for a
    # person. GitHub failing is retried every 15 minutes (chain.sh, GITHUB_DOWN).
    import re
    chain = (REPO / "tools" / "runner" / "chain.sh").read_text()
    down = re.search(r"^GITHUB_DOWN='(.*)'$", chain, re.M).group(1)
    log = ("Attempt 4 of 5 failed with error: Unexpected token '<', \"<!DOCTYPE \"... is not valid JSON.\n"
           "##[error]Failed to CreateArtifact: Failed to make request after 5 attempts: Unexpected token '<'")
    assert subprocess.run(["grep", "-qE", down], input=log, text=True).returncode == 0
    assert subprocess.run(["grep", "-qE", down], input="FAIL  reproduce.ipynb (3603 s)", text=True).returncode == 1


def test_a_repeat_authors_commit_may_remove_the_questions_filed_by_dataset():
    # Issues 658 and 664: blind.sh leaves out a repeat author's earlier questions, which before the cutover were
    # questions/<paper>/<dataset>.yaml; the commit job refused their removal as a change outside the paper.
    import re
    workflow = (REPO / ".github" / "workflows" / "attempt.yml").read_text()
    allowed = re.search(r'allowed="(\^\(attempts.*?)"', workflow).group(1).replace("$FOLDER", "pakhomov-2023")
    ok = lambda path: re.search(allowed, path) is not None
    assert ok("questions/pakhomov-2023/000686.yaml") and ok("questions/pakhomov-2023.yaml")
    assert not ok("questions/silkuniene-2025/001276.yaml") and not ok("questions/pakhomov-2023/a/b.yaml")
    assert not ok("claims/silkuniene-2025.yaml")


def test_a_run_flagged_on_the_unverified_account_is_queued_on_the_verified_one(tmp_path):
    # RUNNER_FALLBACK=queue:<file>: the paper goes first in the verified lanes' queue file (once), the rest of its
    # roles are marked for the verified account, and the chain ends QUEUED ON VERIFIED (exit 0), not STOPPED.
    chain = (REPO / "tools" / "runner" / "chain.sh").read_text()
    block = chain[chain.index('      if [[ "${RUNNER_FALLBACK:-verified}" == queue:* ]]'):
                  chain.index('      if [ "${RUNNER_FALLBACK:-verified}" = none ]; then')]
    (tmp_path / "resume-verified.txt").write_text("other-2020\njacobsen-2022\n")
    (tmp_path / "flagged-jacobsen-2022").touch()
    script = ("set -uo pipefail\nSTATE=%s; d=jacobsen-2022; role=claims; REPLICATE=''; why='FLAGGED on the unverified "
              "account'\nRUNNER_FALLBACK=queue:resume-verified.txt\nlog(){ :; }\nf(){\n%s\nreturn 0; }\nf; echo rc=$? $queued_at"
              % (tmp_path, block))
    out = subprocess.run(["bash", "-c", script], capture_output=True, text=True).stdout.split()
    assert out == ["rc=3", "claims"]
    assert (tmp_path / "resume-verified.txt").read_text() == "jacobsen-2022\nother-2020\n"
    assert (tmp_path / "verified-jacobsen-2022").exists() and not (tmp_path / "flagged-jacobsen-2022").exists()
    body = chain[chain.index("set -uo pipefail"):]
    assert 'queued(){ end "$d QUEUED ON VERIFIED at $queued_at: $last_why"; exit 0; }' in body
    assert body.count("3) queued;;") == 2   # every role, the recorder too


def test_a_paper_with_no_questions_file_has_no_open_questions(tmp_path):
    # chain.sh counted "0\n0" for a paper with no questions file, which is not 0: the answer and author-answers roles
    # ran for nothing on every such paper, and the first replicates hung at the answer role (2026-11-14).
    chain = (REPO / "tools" / "runner" / "chain.sh").read_text()
    lines = chain[chain.index("open_questions=$({ on_branch"):chain.index('if [ "${open_questions:-0}" != 0 ]')]
    def count(on_branch):
        script = f"set -uo pipefail\nd=x\non_branch(){{ {on_branch}; }}\npython(){{ {sys.executable} \"$@\"; }}\n{lines}\necho \"[$open_questions]\""
        return subprocess.run(["bash", "-c", script], capture_output=True, text=True).stdout.strip()
    assert count("return 1") == "[0]"
    assert count("printf 'questions:\\n- {id: a}\\n- {id: b, answered: true}\\n'") == "[1]"
    # A replicate's answer run goes to the papers workflow with its name, and commits to the replicate's branch.
    papers = (REPO / ".github" / "workflows" / "papers.yml").read_text()
    assert 'BRANCH="replicate/$FOLDER/$REPLICATE"' in papers and "format('-{0}', inputs.replicate)" in papers


def test_an_authors_large_scratch_files_are_left_out_of_its_changes():
    # petersen-2020, 2026-11-15: two pickles of 1.4 and 2.6 GB in the entry made a patch git refused to apply. New
    # files over 20 MB are removed before the changes are collected, with a warning.
    workflow = (REPO / ".github" / "workflows" / "attempt.yml").read_text()
    drop = workflow.index('git ls-files --others --exclude-standard -z -- "${paths[@]}"')
    assert '-gt 20000000' in workflow[drop:drop + 400] and "::warning::Left out of the changes" in workflow[drop:drop + 400]
    assert drop < workflow.index('git add -A -- "${paths[@]}" && git diff --cached --binary')


def test_the_claims_checkpoint_waits_when_it_would_drop_a_claim_the_attempt_on_main_records(tmp_path):
    # 2026-11-16: a new reading of tingley-2018 renamed a claim; put on main ahead of its attempt, it broke the check
    # of the attempt already there, and with it every attempt's pull request. The checkpoint runs this script in a
    # checkout of main that has the new claims file, and waits when it prints anything.
    script_file = (REPO / "tools" / "runner" / "merge_claims.sh").read_text()
    start = script_file.index("dropped=$(cd")
    code = script_file[script_file.index("<<'PY'\n", start) + 6:script_file.index("\nPY\n)", start)]
    (tmp_path / "attempts").mkdir(); (tmp_path / "claims").mkdir()
    (tmp_path / "attempts" / "x-2018-01.yaml").write_text("outcomes:\n- {claim: old-only}\n")
    (tmp_path / "attempts" / "x-2018-02.yaml").write_text("outcomes:\n- {claim: kept}\n- {claim: renamed}\n")
    (tmp_path / "attempts" / "x-2018-phase-01.yaml").write_text("outcomes:\n- {claim: another-papers}\n")
    def dropped(ids):
        (tmp_path / "claims" / "x-2018.yaml").write_text("claims:\n" + "".join(f"- {{id: {i}}}\n" for i in ids))
        return subprocess.run([sys.executable, "-c", code, "x-2018"], cwd=tmp_path, capture_output=True, text=True).stdout.strip()
    assert dropped(["kept", "renamed", "new"]) == ""            # claims added: fine; an earlier record does not count
    assert dropped(["kept", "renamed-differently"]) == "renamed"
    assert 'if [ -n "$dropped" ]; then' in script_file and "left for the attempt's merge" in script_file


def test_a_repeat_authors_commit_moves_a_finished_earlier_attempts_transcripts_aside(tmp_path):
    # A repeat attempt that does not read the claims again found the earlier attempt's transcripts still in the
    # folder, and its blind author's revision runs could read the earlier verifiers' reports (three replicates did).
    # The author's commit now archives them whenever a finished attempt's are there (its recorder's transcript).
    workflow = (REPO / ".github" / "workflows" / "attempt.yml").read_text()
    line = next(x.strip() for x in workflow.splitlines() if 'if [ "$ROLE" = author ] && {' in x)
    def archives(role, files):
        d = tmp_path / f"{role}-{len(files)}-{'-'.join(sorted(files))[:40]}"; (d / "transcripts" / "x").mkdir(parents=True)
        for f in files: (d / "transcripts" / "x" / f).write_text("t")
        script = f'ROLE={role}; FOLDER=x\n{line} echo yes; else echo no; fi'
        return subprocess.run(["bash", "-c", script], cwd=d, capture_output=True, text=True).stdout.strip()
    assert archives("author", ["claims.md", "author.md", "verifier-2-report.md", "recorder.md"]) == "yes"   # the hole
    assert archives("author", ["author.md", "recorder.md"]) == "yes"
    assert archives("author", ["claims.md", "claims-check.md"]) == "no"       # this attempt's own claims runs stay
    assert archives("author", ["claims.md", "author.md"]) == "no"             # its own failed first author run stays
    assert archives("author-revise-1", ["claims.md", "recorder.md"]) == "no"
    # The reconcile run follows the instructions as they are now, not as the branch had them when its attempt began.
    assert '[ "$ROLE" != reconcile ] || git restore --worktree --source "$GITHUB_SHA" -- docs/agents/reconcile.md' in workflow


def test_the_reconcile_run_is_given_the_earlier_attempts_entry():
    # It reads both attempts' code to say why an outcome differs; the earlier entry is copied from main, outside the
    # folders whose changes are collected.
    workflow = (REPO / ".github" / "workflows" / "attempt.yml").read_text()
    step = workflow[workflow.index("name: Put the earlier attempt's entry under earlier-entry/"):]
    assert "if: inputs.role == 'reconcile'" in step[:200] and 'git archive FETCH_HEAD "entries/$FOLDER"' in step[:500]
    assert "earlier-entry" not in workflow[workflow.index("paths=(attempts claims entries README.md)"):][:300]
    assert "`earlier-entry/`" in (REPO / "docs" / "agents" / "reconcile.md").read_text()


def test_a_papers_other_datasets_have_their_paper_match_before_its_claims_are_read():
    # pelot-2020 was listed on one of its seven datasets, and its attempt read the others as outside data. A chain
    # now runs the paper match of every target that names the paper and has no verdict, before the claims.
    targets = [
        {"key": "sparc:60", "folder": "sparc-60", "archive": "sparc", "papers": [{"doi": "10.1/P", "relation": "IsDescribedBy"}]},
        {"key": "sparc:64", "folder": "sparc-64", "archive": "sparc", "papers": [{"doi": "10.1/p", "relation": "IsDescribedBy"}]},
        {"key": "sparc:65", "folder": "sparc-65", "archive": "sparc", "papers": [{"doi": "10.1/p", "relation": "IsDescribedBy"}]},
        {"key": "sparc:70", "folder": "sparc-70", "archive": "sparc", "papers": [{"doi": "10.1/p", "relation": "References"}]},
        {"key": "sparc:71", "folder": "sparc-71", "archive": "sparc", "papers": [{"doi": "10.1/other", "relation": "IsDescribedBy"}]},
        {"key": "dandi:000001", "folder": "000001", "archive": "dandi", "published_version": None,
         "papers": [{"doi": "10.1/p", "relation": "IsDescribedBy"}]},
    ]
    status = lambda t: "no_match" if t["folder"] == "sparc-65" else "unchecked"
    found = describe.siblings("p-2020", targets=targets, listed={"p-2020": ["sparc:60"]}, doi="doi:10.1/P", status=status)
    # Not the one it is listed on, one already judged, one that only cites the paper, another paper's, or a draft.
    assert found == ["sparc-64"]
    chain = (REPO / "tools" / "runner" / "chain.sh").read_text()
    body = chain[chain.index("set -uo pipefail"):]
    step = body.index('python "$here/describe.py" siblings "$d"')
    assert body.index("esac", body.index('case "$match" in')) < step < body.index('deprecated=$(python "$here/describe.py" deprecated "$d")')
    assert 'SIBLINGS=0 MATCH_ONLY=1 RUNNER_NOTIFY=none "$here/chain.sh" "$sib"' in body
    assert '[ -z "$REPLICATE" ] && [ "${SIBLINGS:-1}" != 0 ]' in body


def test_a_replicate_has_its_own_branch_and_runs_and_never_reconciles_or_merges():
    # docs/replicates.md: every reference to the chain's branch goes through $br, which a replicate sets to
    # replicate/<paper>/<rN>; its runs are found by the name <paper>/<rN>; it ends before the reconcile step and the
    # finish, and it never reads the claims again.
    chain = (REPO / "tools" / "runner" / "chain.sh").read_text()
    body = chain[chain.index("set -uo pipefail"):]
    assert body.count("attempt/$d") == body.count('br="attempt/$d"') == 2
    assert 'br="replicate/$d/$REPLICATE"; tag="$d/$REPLICATE"' in body and 'run "$tag" "$1"' in body
    assert body.count('${REPLICATE:+-f replicate="$REPLICATE"}') == 2
    done = body.index('end "$d REPLICATE $REPLICATE DONE"')
    assert done < body.index("step reconcile") < body.index('log "finishing"')
    assert body.index('log "replicate $REPLICATE: the claims on main"') < body.index("step claims\n")
    workflow = (REPO / ".github" / "workflows" / "attempt.yml").read_text()
    assert 'BRANCH="replicate/$FOLDER/$REPLICATE"' in workflow and "format('replicate/{0}/{1}'" in workflow
    assert "format('-{0}', inputs.replicate)" in workflow   # its own concurrency group: one waits for no other


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
    script = ('set -uo pipefail\nd=x\nbr=attempt/x\nwork=$(mktemp -d)\nnotify(){ :; }\n'
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

