"""The intake of runs made from encore-runner or a fork of it (tools/intake.py)."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import intake  # noqa: E402
from intake import Branch, Refused, Run, Signer  # noqa: E402

FORK = Run("acme-lab/encore-runner", "42")
OWN = Run("encorescience/encore-runner", "7")
BASE = "a" * 40
HEAD = "b" * 40
SIGNER = "https://github.com/encorescience/encore-protocol/.github/workflows/{wf}.yml@refs/tags/v0.2.0"
# Real records of the registry, so that they meet the protocol's schemas: a claims file checked as ready, and an
# attempt record without its verification rounds, as the author's run leaves it.
READY = (ROOT / "claims" / "alasfour-2024.yaml").read_bytes()
BASE_RECORD = yaml.safe_load((ROOT / "attempts" / "amjad-2025-01.yaml").read_text())
for key in ("verifications", "findings_review"):
    BASE_RECORD.pop(key, None)
SCHEMAS = ROOT / "schemas"
needs_schemas = pytest.mark.skipif(not (SCHEMAS / "attempt.schema.json").is_file(),
                                   reason="the protocol is not laid over this checkout (tools/protocol.sh)")


def attestation(run=FORK, wf="attempt", sha="c" * 40, **over):
    cert = {"buildSignerURI": SIGNER.format(wf=wf), "buildSignerDigest": sha,
            "sourceRepositoryURI": f"https://github.com/{run.repo}", "runInvocationURI": f"{run.url}/attempts/1"}
    cert.update(over)
    return [{"verificationResult": {"signature": {"certificate": cert}}}]


def manifest(role="author", run=FORK, **over):
    m = {"format": 1, "paper": "demo-2020", "role": role, "result": "success", "registry": intake.REGISTRY,
         "repository": run.repo, "run_id": run.id, "run_url": run.url, "base_sha": BASE, "removed": []}
    m.update(over)
    return m


def record(run=FORK, **over) -> bytes:
    rec = yaml.safe_load(yaml.safe_dump(BASE_RECORD))
    rec.update(id="demo-2020-02", entry="demo-2020")
    rec["provenance"]["accountable"]["name"] = "Acme Lab"
    rec["provenance"]["runner"]["url"] = run.url
    for k, v in over.items():
        if k == "accountable":
            rec["provenance"]["accountable"]["name"] = v
        elif k == "url":
            rec["provenance"]["runner"]["url"] = v
        else:
            rec[k] = v
    return yaml.safe_dump(rec).encode()


AT_BASE = {"claims/demo-2020.yaml": READY, "attempts/demo-2020-01.yaml": record(id="demo-2020-01"),
           "transcripts/demo-2020/author.md": b"the first attempt\n"}
ATTEMPT = {"attempts/demo-2020-02.yaml": record(), "entries/demo-2020/demo-2020.ipynb": b"{}",
           "questions/demo-2020/q1.yaml": b"q: 1\n", "transcripts/demo-2020/author.md": b"run\n",
           "transcripts/demo-2020/author-report.md": b"report\n"}


def changes(files=None, base=None, run=FORK, **m):
    at_base = AT_BASE if base is None else base
    return intake.check_changes(manifest(run=run, **m), ATTEMPT if files is None else files, at_base.get, run,
                                SCHEMAS)


# The run's address.

def test_the_run_is_read_from_an_issue_body():
    run = intake.parse_run(f"### Run\n\n{FORK.url}/job/9\n")
    assert (run.repo, run.id, run.url) == (FORK.repo, "42", FORK.url)


def test_a_body_with_no_run_is_refused():
    with pytest.raises(Refused):
        intake.parse_run("please take my run")


@pytest.mark.parametrize("repo, setting, straight", [
    ("encorescience/encore-runner", None, True),
    ("encorescience/encore-runner", "", True),
    ("acme-lab/encore-runner", None, False),
    ("acme-lab/encore-runner", "encorescience/encore-runner acme-lab/encore-runner", True),
    ("Acme-Lab/Encore-Runner", "acme-lab/encore-runner", True),
    ("acme-lab/encore-runner", "*", True),
    ("encorescience/encore-runner", "acme-lab/encore-runner", False),
])
def test_who_goes_straight_on(repo, setting, straight):
    assert intake.goes_straight_on(repo, setting) is straight


# The signature.

def test_a_signature_from_the_protocol_in_the_run_passes():
    assert intake.check_signature(attestation(), FORK) == Signer("attempt", "refs/tags/v0.2.0", "c" * 40)


@pytest.mark.parametrize("over", [
    {"buildSignerURI": "https://github.com/acme-lab/encore-runner/.github/workflows/run.yml@refs/heads/main"},
    {"buildSignerURI": "https://github.com/encorescience/encore-protocol/.github/workflows/pipeline.yml@refs/heads/main"},
    {"buildSignerURI": "https://github.com/acme-lab/encore-protocol/.github/workflows/attempt.yml@refs/heads/main"},
    {"sourceRepositoryURI": "https://github.com/someone/else"},
    {"runInvocationURI": "https://github.com/acme-lab/encore-runner/actions/runs/421/attempts/1"},
    {"buildSignerDigest": "main"},
])
def test_a_signature_from_anywhere_else_is_refused(over):
    with pytest.raises(Refused):
        intake.check_signature(attestation(**over), FORK)


def test_no_signature_is_refused():
    with pytest.raises(Refused):
        intake.check_signature([], FORK)


# The manifest.

def signer(wf="attempt"):
    return Signer(wf, "refs/tags/v0.2.0", "c" * 40)


def test_a_good_manifest_passes():
    assert intake.check_manifest(manifest(), FORK, signer(), intake.REGISTRY) == []
    assert intake.check_manifest(manifest("claims"), FORK, signer("papers"), intake.REGISTRY) == []


@pytest.mark.parametrize("m, wf", [
    (manifest("verifier"), "attempt"),
    (manifest("claims"), "attempt"),
    (manifest(registry="acme-lab/encore-registry"), "attempt"),
    (manifest(repository="other/repo"), "attempt"),
    (manifest(run_id="43"), "attempt"),
    (manifest(base_sha=""), "attempt"),
    (manifest(result="failure"), "attempt"),
])
def test_a_manifest_that_does_not_fit_is_refused(m, wf):
    assert intake.check_manifest(m, FORK, signer(wf), intake.REGISTRY)


# The base.

def test_a_new_attempt_starts_from_main():
    assert intake.check_base(manifest("claims"), FORK, Branch("attempt/demo-2020", None, None, True)) == []


def test_a_new_attempt_from_a_commit_not_on_main_is_refused():
    assert intake.check_base(manifest("claims"), FORK, Branch("attempt/demo-2020", None, None, False))


def test_a_claims_check_needs_the_claims_runs_branch():
    assert intake.check_base(manifest("claims-check"), FORK, Branch("attempt/demo-2020", None, None, True))


def test_a_run_continues_its_own_attempt_from_its_head():
    branch = Branch("attempt/demo-2020", BASE, FORK.repo, False)
    assert intake.check_base(manifest("claims-check"), FORK, branch) == []


def test_a_run_from_an_old_commit_of_the_branch_is_refused():
    branch = Branch("attempt/demo-2020", HEAD, FORK.repo, False)
    assert any("now at" in p for p in intake.check_base(manifest(), FORK, branch))


@pytest.mark.parametrize("source", [None, "encorescience/encore-runner"])
def test_a_run_cannot_continue_an_attempt_another_began(source):
    branch = Branch("attempt/demo-2020", BASE, source, False)
    assert any("wait for it to finish" in p for p in intake.check_base(manifest(), FORK, branch))


# What the run changed.

@needs_schemas
def test_a_good_attempt_passes():
    assert changes() == []


@needs_schemas
def test_good_claims_pass():
    files = {"claims/demo-2020.yaml": READY, "transcripts/demo-2020/claims.md": b"read\n",
             "transcripts/demo-2020/claims-report.md": b"report\n"}
    assert changes(files, base={}, role="claims") == []


@needs_schemas
def test_a_claims_check_that_only_adds_a_transcript_passes():
    files = {"transcripts/demo-2020/claims-check.md": b"checked\n"}
    assert changes(files, role="claims-check") == []


def test_claims_bring_nothing_else():
    files = {"claims/demo-2020.yaml": READY, "entries/demo-2020/demo-2020.ipynb": b"{}"}
    assert any("changes only" in p for p in changes(files, base={}, role="claims"))


def test_claims_bring_no_author_transcripts():
    files = {"claims/demo-2020.yaml": READY, "transcripts/demo-2020/author.md": b"x\n"}
    assert any("not a transcript of the claims run" in p for p in changes(files, base={}, role="claims"))


def test_the_author_leaves_the_claims_alone():
    assert any("as it found it" in p for p in changes({**ATTEMPT, "claims/demo-2020.yaml": READY + b"# more\n"}))


def test_the_author_starts_from_ready_claims():
    not_ready = yaml.safe_load(READY)
    not_ready["checks"][-1]["ready"] = False
    base = {**AT_BASE, "claims/demo-2020.yaml": yaml.safe_dump(not_ready).encode()}
    assert any("does not say it is ready" in p for p in changes(base=base))
    assert any("no claims" in p for p in changes(base={}))


def test_the_author_adds_one_attempt_and_changes_no_earlier_one():
    two = {**ATTEMPT, "attempts/demo-2020-03.yaml": record(id="demo-2020-03")}
    assert any("adds 2 attempt records" in p for p in changes(two))
    earlier = {**ATTEMPT, "attempts/demo-2020-01.yaml": record(id="demo-2020-01", accountable="Someone")}
    assert any("changes no earlier one" in p for p in changes(earlier))


@pytest.mark.parametrize("name", ["verifier-1.md", "author-revise-1.md", "reconcile.md", "recorder.md"])
def test_the_author_brings_no_later_runs(name):
    assert any("not a transcript of the author run" in p
               for p in changes({**ATTEMPT, f"transcripts/demo-2020/{name}": b"x\n"}))


@needs_schemas
def test_an_earlier_attempts_transcripts_may_be_moved_aside():
    files = {**ATTEMPT, "transcripts/demo-2020/attempt-01/author.md": b"the first attempt\n"}
    assert changes(files) == []
    # A transcript the new attempt does not write again is removed from where it was.
    base = {**AT_BASE, "transcripts/demo-2020/author-answers.md": b"answers\n"}
    files["transcripts/demo-2020/attempt-01/author-answers.md"] = b"answers\n"
    assert changes(files, base=base, removed=["transcripts/demo-2020/author-answers.md"]) == []


@pytest.mark.parametrize("copy, removed", [
    (b"made up\n", []),
    (b"the first attempt\n", ["transcripts/demo-2020/claims.md"]),
])
def test_a_transcript_moved_aside_must_be_the_earlier_one(copy, removed):
    files = {**ATTEMPT, "transcripts/demo-2020/attempt-01/author.md": copy}
    assert changes(files, removed=removed)


def test_an_earlier_archive_is_not_changed():
    base = {**AT_BASE, "transcripts/demo-2020/attempt-01/author.md": b"older\n"}
    files = {**ATTEMPT, "transcripts/demo-2020/attempt-01/author.md": b"the first attempt\n"}
    assert any("moved aside" in p for p in changes(files, base=base))


def test_only_transcripts_are_removed():
    assert any("removed" in p for p in changes(removed=["attempts/demo-2020-01.yaml"]))


@pytest.mark.parametrize("over, words", [
    ({"accountable": ""}, "is empty"),
    ({"accountable": "CatalystNeuro"}, "Set ENCORE_ACCOUNTABLE"),
    ({"url": "https://github.com/acme-lab/encore-runner/actions/runs/41"}, "not the run it came from"),
    ({"verifications": [{"kind": "rerun"}]}, "has verifications"),
])
def test_the_record_names_who_ran_it_and_where(over, words):
    assert any(words in p for p in changes({**ATTEMPT, "attempts/demo-2020-02.yaml": record(**over)}))


def test_catalystneuro_may_name_itself_from_its_own_runner():
    files = {**ATTEMPT, "attempts/demo-2020-02.yaml": record(OWN, accountable="CatalystNeuro")}
    assert not any("ENCORE_ACCOUNTABLE" in p for p in changes(files, run=OWN))


# The report.

def test_the_report_says_what_waits_and_why():
    t = intake.Taken(FORK, manifest(), waiting=True)
    assert "`approved`" in intake.report(t, False)
    t = intake.Taken(FORK, manifest(), problems=["a reason"])
    assert "Not taken" in intake.report(t, False) and "a reason" in intake.report(t, False)
    t = intake.Taken(FORK, manifest("claims"), committed=HEAD)
    assert "Next: claims-check" in intake.report(t, False)


# The whole intake, against a registry in a temporary folder, with GitHub's answers made up.

needs_submission = pytest.mark.skipif(not (ROOT / "tools" / "submission.py").is_file(),
                                      reason="the protocol laid over this checkout has no tools/submission.py")


def git(cwd, *args):
    import subprocess
    return subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True, text=True).stdout.strip()


@pytest.fixture
def registry(tmp_path, monkeypatch):
    """A registry whose main holds ready claims for demo-2020, and a submission of the author's run made from it."""
    import importlib.util
    import json
    import shutil
    origin, work, clone = tmp_path / "origin.git", tmp_path / "work", tmp_path / "clone"
    git(tmp_path, "init", "-q", "--bare", "-b", "main", str(origin))
    git(tmp_path, "clone", "-q", str(origin), str(work))
    for k, v in (("user.name", "t"), ("user.email", "t@t")):
        git(work, "config", k, v)
    (work / "claims").mkdir()
    (work / "claims" / "demo-2020.yaml").write_bytes(READY)
    git(work, "add", "-A")
    git(work, "commit", "-q", "-m", "claims")
    git(work, "push", "-q", "origin", "main")
    base = git(work, "rev-parse", "HEAD")
    spec = importlib.util.spec_from_file_location("submission", ROOT / "tools" / "submission.py")
    sub = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(sub)
    for path, data in ATTEMPT.items():
        (work / path).parent.mkdir(parents=True, exist_ok=True)
        (work / path).write_bytes(data)
    git(work, "add", "-A")
    meta = {k: v for k, v in manifest(base_sha=base).items() if k not in ("format", "paper", "removed")}
    sub.pack(work, "demo-2020", meta, tmp_path / "out")
    git(tmp_path, "clone", "-q", str(origin), str(clone))
    for k, v in (("user.name", "t"), ("user.email", "t@t")):
        git(clone, "config", k, v)

    calls = []

    def sh(*args, cwd=None, check=True):
        calls.append(args)
        if args[:3] == ("gh", "attestation", "verify"):
            return json.dumps(attestation())
        if args[:2] == ("gh", "api"):
            return json.dumps({"status": "ahead"})
        return real_sh(*args, cwd=cwd, check=check)

    real_sh = intake.sh
    monkeypatch.setattr(intake, "ROOT", clone)
    monkeypatch.setattr(intake, "sh", sh)
    monkeypatch.setattr(intake, "submission_module", lambda sha: sub)

    def download(run, dest):
        dest.mkdir(parents=True)
        return Path(shutil.copy(tmp_path / "out" / "submission.tar.gz", dest))

    monkeypatch.setattr(intake, "download", download)
    return origin, base, calls


@needs_submission
@needs_schemas
def test_a_forks_run_waits_and_then_is_taken(registry):
    origin, base, calls = registry
    t = intake.take(FORK, approved=False, dry_run=False, registry=intake.REGISTRY, setting=None)
    assert t.problems == [] and t.waiting
    assert not git(origin, "branch", "--list", "attempt/demo-2020")

    t = intake.take(FORK, approved=True, dry_run=False, registry=intake.REGISTRY, setting=None)
    assert t.problems == [] and t.committed
    head = git(origin, "rev-parse", "attempt/demo-2020")
    assert head == t.committed and git(origin, "rev-parse", f"{head}^") == base
    trailers = git(origin, "log", "-1", "--format=%(trailers)", head)
    assert f"Encore-Source: {FORK.repo}" in trailers and f"Encore-Run: {FORK.url}" in trailers
    files = git(origin, "show", "--name-only", "--format=", head).split()
    assert sorted(files) == sorted(ATTEMPT)


@needs_submission
@needs_schemas
def test_a_run_from_a_stale_base_is_not_taken(registry):
    origin, base, calls = registry
    assert intake.take(FORK, approved=True, dry_run=False, registry=intake.REGISTRY, setting=None).committed
    # The same submission again: the branch has moved on from where the run started.
    again = intake.take(FORK, approved=True, dry_run=False, registry=intake.REGISTRY, setting=None)
    assert any("now at" in p for p in again.problems) and again.committed is None


@needs_submission
@needs_schemas
def test_a_dry_run_pushes_nothing(registry):
    origin, base, calls = registry
    t = intake.take(FORK, approved=True, dry_run=True, registry=intake.REGISTRY, setting=None)
    assert t.committed and not git(origin, "branch", "--list", "attempt/demo-2020")


def test_the_submission_is_taken_out_of_the_artifact_by_name(tmp_path, monkeypatch):
    import io
    import zipfile
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as z:
        z.writestr("submission.tar.gz", b"the submission")
        z.writestr("../elsewhere.sh", b"echo nothing runs")
    monkeypatch.setattr(intake, "gh_json", lambda *a: {"artifacts": [{"name": "submission", "id": 5}]})

    def run(args, stdout=None, **kw):
        stdout.write(buf.getvalue())
        return type("R", (), {"returncode": 0, "stderr": b""})()

    monkeypatch.setattr(intake.subprocess, "run", run)
    path = intake.download(FORK, tmp_path / "s")
    assert path.read_bytes() == b"the submission"
    assert sorted(x.name for x in (tmp_path / "s").iterdir()) == ["submission.tar.gz", "submission.zip"]
    assert not (tmp_path / "elsewhere.sh").exists()


def test_a_run_without_a_submission_is_refused(monkeypatch):
    monkeypatch.setattr(intake, "gh_json", lambda *a: {"artifacts": []})
    with pytest.raises(Refused):
        intake.download(FORK, Path("/nonexistent"))
