"""Take an attempt made from encore-runner, or a fork of it, into the registry (encore-protocol docs/outside-runs.md).

    python tools/intake.py RUN_URL --what start --paper P [--approved-by USER] [--issue N] [--dry-run]
    python tools/intake.py RUN_URL --what attempt --paper P [--approved-by USER] [--issue N] [--dry-run]
    python tools/intake.py --issue-body-env ISSUE_BODY [--approved-by USER] [--issue N] [--dry-run]
    python tools/intake.py RUN_URL [--approved-by USER] [--issue N] [--dry-run]      (one run, the earlier way)

A runner makes a whole attempt in its own repository, from the claims to the recorder's notes, and keeps the
attempt's state between runs on its own branch, attempt/<paper>. It touches the registry twice.

`--what start`: the runner says it has begun an attempt on a paper. The intake makes the registry's branch
attempt/<paper>, one empty commit on main that names the runner (Encore-Source) and its run (Encore-Start), so that
the registry shows who is attempting the paper and no one else starts on it.

`--what attempt`: the runner sends the finished attempt. The intake reads the ledger on the runner's branch
(.encore/attempt.json), which lists the attempt's runs in order, and for each run:

1. downloads its submission and checks its signature: GitHub's, for encore-protocol's own papers.yml or attempt.yml,
   made in that run and in the runner's repository;
2. reads it with the encore-protocol tools/submission.py of the commit that signed it;
3. checks that it started from the state the run before it left (`state_before`, a digest of the paper's files),
   beginning from the commit of main the attempt began at, so that nothing was edited between runs;
4. checks its changes against what its role may change;
5. lays it over the runs before it, as one commit that names the runner and the run.

When every run passes, it pushes the commits as attempt/<paper>. A repository listed in ENCORE_INTAKE_AUTO goes
straight on; any other waits until someone in queue/priority.yaml approves it.

The rest of this text describes taking one run at a time, as attempts begun before 2026-11-25 were taken; it stays
until those are finished.

The runs that begin an attempt (claims, claims-check and the author's first run) can be made from encore-runner, or
from another organization's fork of it, with that repository's own API key. Such a run reads this registry and writes
nothing to it. It ends by uploading `submission.tar.gz`, what it changed in one paper's files, signed by GitHub as
made by encore-protocol's papers.yml or attempt.yml in that run.

This script takes one such run, given its address:

1. It downloads the submission and checks its signature: GitHub's, for encore-protocol's own workflow, made in the
   run it was given and in that run's repository.
2. It reads the submission with the encore-protocol tools/submission.py of the commit that signed it, which checks
   that the files are one paper's and match their manifest.
3. It checks the base: the run started from the attempt branch's current commit, which the same repository's runs
   made, or, for a new attempt, from a commit on main.
4. It checks the changes against what the run's role may change, and the author's record.
5. When everything passes, it commits the submission to the attempt's branch, attempt/<paper>, naming the source
   repository and run (Encore-Source, Encore-Run), and pushes. A repository listed in ENCORE_INTAKE_AUTO goes straight
   on; any other waits until someone in queue/priority.yaml approves it (--approved-by, which intake.yml passes for
   their dispatch, their issue, or their `approved` label on someone else's issue).

It never runs anything from a submission. With --dry-run it checks and reports, and pushes nothing.
"""

from __future__ import annotations

import argparse
import base64
import datetime
import importlib.util
import json
import os
import re
import subprocess
import sys
import tempfile
import zipfile
from dataclasses import dataclass, field
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = "encorescience/encore-registry"
PROTOCOL = "encorescience/encore-protocol"
AUTO_DEFAULT = "encorescience/encore-runner"
CENTRAL_OWNERS = ("encorescience", "catalystneuro")
RUN_URL = re.compile(r"https://github\.com/(?P<repo>[A-Za-z0-9-]+/[A-Za-z0-9._-]+)/actions/runs/(?P<id>[0-9]+)")
SIGNER = re.compile(rf"https://github\.com/{re.escape(PROTOCOL)}/\.github/workflows/(?P<wf>attempt|papers)\.yml"
                    r"@(?P<ref>refs/[A-Za-z0-9._/-]+)")
ROLES = {"claims": "papers", "claims-check": "papers", "author": "attempt"}
# Every role of an attempt, and the workflow that makes it (a whole attempt, `--what attempt`).
LATER = re.compile(r"author-answers|author-revise-[1-3]|verifier-[1-3]|reconcile|recorder")
KEY = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
LEDGER = ".encore/attempt.json"
WHAT = {"start": "start", "attempt": "attempt", "run": "run"}


def workflow_of(role: str) -> str | None:
    """papers or attempt: the protocol's workflow that makes a role's run. None for no role of an attempt."""
    if role in ("claims", "claims-check", "answer"):
        return "papers"
    return "attempt" if role == "author" or LATER.fullmatch(role or "") else None
# The reader's transcripts, which come with the claims, and the author's.
READER = re.compile(r"(claims|claims-check)(-report)?\.md")
AUTHOR = re.compile(r"author(-report)?\.md")
MOVED = re.compile(r"attempt-[0-9]{2}/[^/]+")


class Refused(Exception):
    """A submission the registry does not take, with the reasons."""

    def __init__(self, problems: list[str]):
        super().__init__("; ".join(problems))
        self.problems = problems


@dataclass
class Run:
    repo: str
    id: str

    @property
    def url(self) -> str:
        return f"https://github.com/{self.repo}/actions/runs/{self.id}"

    @property
    def owner(self) -> str:
        return self.repo.split("/")[0].lower()


def parse_run(text: str) -> Run:
    """The first run address in `text`: a dispatch's input, or an issue's body."""
    m = RUN_URL.search(text or "")
    if not m:
        raise Refused(["No run address (https://github.com/OWNER/REPO/actions/runs/ID) was given."])
    return Run(m.group("repo"), m.group("id"))


def steer() -> set[str]:
    """The users in queue/priority.yaml, read from main so that a branch cannot widen the list (docs/queue.md)."""
    r = subprocess.run(["git", "show", "origin/main:queue/priority.yaml"], cwd=ROOT, capture_output=True, text=True)
    text = r.stdout if r.returncode == 0 else (ROOT / "queue" / "priority.yaml").read_text()
    return {str(u).lower() for u in (yaml.safe_load(text) or {}).get("priority") or []}


def goes_straight_on(repo: str, setting: str | None) -> bool:
    """Whether a repository's submissions are committed without a person's approval (ENCORE_INTAKE_AUTO)."""
    listed = (setting if setting and setting.strip() else AUTO_DEFAULT).split()
    return "*" in listed or repo.lower() in (x.lower() for x in listed)


@dataclass
class Signer:
    workflow: str   # attempt or papers
    ref: str        # the ref of encore-protocol the caller named
    sha: str        # the commit of encore-protocol that signed


def check_signature(results: list[dict], run: Run) -> Signer:
    """What `gh attestation verify --format json` says, held against the run the intake was given."""
    problems = []
    for r in results or []:
        cert = ((r.get("verificationResult") or {}).get("signature") or {}).get("certificate") or {}
        m = SIGNER.fullmatch(cert.get("buildSignerURI") or "")
        if not m:
            problems.append(f"Signed by {cert.get('buildSignerURI')!r}, not encore-protocol's papers.yml or attempt.yml.")
            continue
        if (cert.get("sourceRepositoryURI") or "").lower() != f"https://github.com/{run.repo}".lower():
            problems.append(f"Signed in {cert.get('sourceRepositoryURI')!r}, not {run.repo}.")
            continue
        if not (cert.get("runInvocationURI") or "").startswith(run.url + "/"):
            problems.append(f"Signed in run {cert.get('runInvocationURI')!r}, not {run.url}.")
            continue
        sha = cert.get("buildSignerDigest") or ""
        if not re.fullmatch(r"[0-9a-f]{40}", sha):
            problems.append(f"The signature names no commit of encore-protocol ({sha!r}).")
            continue
        return Signer(m.group("wf"), m.group("ref"), sha)
    raise Refused(problems or ["The submission has no signature."])


def check_manifest(manifest: dict, run: Run, signer: Signer, registry: str) -> list[str]:
    problems = []
    role = manifest.get("role")
    if role not in ROLES:
        problems.append(f"The run's role is {role!r}. From encore-runner the registry takes claims, claims-check and "
                        f"the author's first run; the rest run here.")
    elif ROLES[role] != signer.workflow:
        problems.append(f"A {role} run is made by {ROLES[role]}.yml, but this one was signed by {signer.workflow}.yml.")
    if (manifest.get("registry") or "").lower() != registry.lower():
        problems.append(f"The run read {manifest.get('registry')!r}, not {registry}.")
    if (manifest.get("repository") or "").lower() != run.repo.lower() or str(manifest.get("run_id")) != run.id:
        problems.append(f"The submission says it is from {manifest.get('repository')} run {manifest.get('run_id')}, "
                        f"not {run.repo} run {run.id}.")
    if not re.fullmatch(r"[0-9a-f]{40}", str(manifest.get("base_sha") or "")):
        problems.append("The submission names no commit it started from (base_sha).")
    if manifest.get("result") not in ("success", None):
        problems.append(f"The run ended as {manifest.get('result')!r}; the registry takes a run that succeeded.")
    return problems


@dataclass
class Branch:
    """The attempt's branch as the registry has it now, and where the run started."""
    name: str
    head: str | None           # None: there is no such branch
    head_source: str | None    # the Encore-Source of its head commit
    base_on_main: bool         # whether the run's base is a commit on main


def check_base(manifest: dict, run: Run, branch: Branch) -> list[str]:
    base = manifest.get("base_sha")
    if branch.head is None:
        if not branch.base_on_main:
            return [f"The run started from {base}, which is not on main, and the registry has no {branch.name}."]
        if manifest.get("role") == "claims-check":
            return [f"The registry has no {branch.name}: a claims-check run continues from a claims run it took."]
        return []
    problems = []
    if (branch.head_source or "").lower() != run.repo.lower():
        problems.append(f"{branch.name} is an attempt {branch.head_source or 'begun in the registry'} is making, not "
                        f"{run.repo}; wait for it to finish.")
    if branch.head != base:
        problems.append(f"The run started from {base}, but {branch.name} is now at {branch.head}. Run it again from "
                        f"the branch as it is.")
    return problems


def check_changes(manifest: dict, files: dict[str, bytes], base, run: Run, schemas: Path | None) -> list[str]:
    """What the run changed, against what its role may change. `base(path)` reads a file at the run's base."""
    p, role = manifest["paper"], manifest.get("role")
    removed = manifest.get("removed") or []
    problems = []
    claims_path = f"claims/{p}.yaml"
    tdir = f"transcripts/{p}/"

    # A new attempt moves the last one's transcripts aside, into attempt-NN/, unchanged.
    moved = {x for x in files if x.startswith(tdir) and MOVED.fullmatch(x[len(tdir):])}
    for x in removed:
        kept = [y for y in moved if y.rsplit("/", 1)[1] == x[len(tdir):]]
        if not x.startswith(tdir) or "/" in x[len(tdir):] or not kept:
            problems.append(f"{x}: removed. A run adds to the record; only an earlier attempt's transcripts are moved "
                            f"aside, into {tdir}attempt-NN/.")
    for x in sorted(files):
        if x in moved:
            was = tdir + x[len(tdir):].split("/", 1)[1]
            if base(x) is not None or base(was) is None or base(was) != files[x]:
                problems.append(f"{x}: not an earlier transcript moved aside ({was} as it was).")
        elif x.startswith(tdir):
            name = x[len(tdir):]
            if not (READER if role in ("claims", "claims-check") else AUTHOR).fullmatch(name):
                problems.append(f"{x}: not a transcript of the {role} run.")

    if role in ("claims", "claims-check"):
        allowed = {claims_path, f"questions/{p}.yaml"}
        for x in sorted(files):
            if not x.startswith(tdir) and x not in allowed:
                problems.append(f"{x}: a {role} run changes only the claims file, the questions and its transcripts.")
        claims = files.get(claims_path) or base(claims_path)
        if claims is None:
            problems.append(f"{claims_path}: the {role} run left no claims file.")
        else:
            problems += schema_problems(load(claims), "claims", schemas)
        return problems

    # The author.
    if claims_path in files or claims_path in removed:
        problems.append(f"{claims_path}: the author leaves the claims file as it found it.")
    at_base = base(claims_path)
    if at_base is None:
        problems.append(f"{claims_path}: the run started from a commit with no claims.")
    elif not ((load(at_base) or {}).get("checks") or [{}])[-1].get("ready"):
        problems.append(f"{claims_path}: its last check, where the run started, does not say it is ready.")
    records = sorted(x for x in files if re.fullmatch(rf"attempts/{re.escape(p)}-[0-9]{{2}}\.yaml", x))
    new = [x for x in records if base(x) is None]
    for x in records:
        if base(x) is not None:
            problems.append(f"{x}: an earlier attempt. The author adds a new attempt and changes no earlier one.")
    if len(new) != 1:
        problems.append(f"The run adds {len(new)} attempt records for {p}; the author adds one.")
    for x in new:
        problems += record_problems(x, load(files[x]) or {}, manifest, run, schemas)
    return problems


def later_changes(manifest: dict, files: dict[str, bytes], base) -> list[str]:
    """What a run after the author's first changed, against what its role may change (a whole attempt)."""
    p, role = manifest["paper"], manifest.get("role")
    key = re.escape(p)
    tdir, claims_path = f"transcripts/{p}/", f"claims/{p}.yaml"
    own = {f"{tdir}{role}.md", f"{tdir}{role}-report.md"}
    notes = re.compile(rf"(docs/pilot-notes|summaries)/{key}-[0-9]{{2}}\.md")
    record = re.compile(rf"attempts/{key}-([0-9]{{2}})\.yaml")
    authoring = role.startswith("author") or role == "reconcile"
    problems = []
    for x in sorted(files):
        if x.startswith(tdir):
            if x not in own:
                problems.append(f"{x}: not a transcript of the {role} run.")
        elif role.startswith("verifier"):
            problems.append(f"{x}: a verification round brings its transcripts and nothing else.")
        elif role == "recorder":
            if not notes.fullmatch(x):
                problems.append(f"{x}: the recorder writes the attempt's notes and summary only.")
        elif role == "answer":
            if x not in (claims_path, f"questions/{p}.yaml"):
                problems.append(f"{x}: the reader's answers change the claims file and the questions only.")
        elif x == claims_path:
            problems.append(f"{claims_path}: the author leaves the claims file as it found it.")
        elif record.fullmatch(x):
            n = int(record.fullmatch(x).group(1))
            if base(x) is None:
                problems.append(f"{x}: a new attempt record. Only the author's first run adds one.")
            elif base(f"attempts/{p}-{n + 1:02d}.yaml") is not None:
                problems.append(f"{x}: an earlier attempt. A run changes the record of the attempt it is part of.")
        elif not (x.startswith(f"entries/{p}/") or x == f"questions/{p}.yaml" or x.startswith(f"questions/{p}/")):
            problems.append(f"{x}: the {role} run changes the attempt's record, its entry and its questions only.")
    for x in manifest.get("removed") or []:
        if not (authoring and (x.startswith(f"entries/{p}/") or x.startswith(f"questions/{p}/"))):
            problems.append(f"{x}: removed. The {role} run removes nothing"
                            + (" but files of its own entry." if authoring else "."))
    return problems


def finished_problems(tree: Path, paper: str, repo: str, schemas: Path | None) -> list[str]:
    """What the registry asks of a whole attempt once its runs are laid over one another."""
    records = sorted((tree / "attempts").glob(f"{paper}-[0-9][0-9].yaml")) if (tree / "attempts").is_dir() else []
    if not records:
        return [f"The attempt left no record (attempts/{paper}-NN.yaml)."]
    path = f"attempts/{records[-1].name}"
    record = load(records[-1].read_bytes()) or {}
    problems = [f"{path}: {x}" for x in schema_problems(record, "attempt", schemas)]
    who = " ".join((((record.get("provenance") or {}).get("accountable") or {}).get("name") or "").split())
    if not who:
        problems.append(f"{path}: provenance.accountable.name is empty. It names who ran the attempt.")
    elif who.lower() == "catalystneuro" and repo.split("/")[0].lower() not in CENTRAL_OWNERS:
        problems.append(f"{path}: provenance.accountable.name is CatalystNeuro, but the attempt is {repo}'s. Set "
                        f"ENCORE_ACCOUNTABLE in the fork.")
    if not (tree / "entries" / paper).is_dir():
        problems.append(f"The attempt left no entry (entries/{paper}/).")
    return problems


def record_problems(path: str, record: dict, manifest: dict, run: Run, schemas: Path | None) -> list[str]:
    problems = schema_problems(record, "attempt", schemas)
    prov = record.get("provenance") or {}
    who = " ".join(((prov.get("accountable") or {}).get("name") or "").split())
    if not who:
        problems.append(f"{path}: provenance.accountable.name is empty. It names who ran the attempt.")
    elif who.lower() == "catalystneuro" and run.owner not in CENTRAL_OWNERS:
        problems.append(f"{path}: provenance.accountable.name is CatalystNeuro, but the run is {run.repo}'s. Set "
                        f"ENCORE_ACCOUNTABLE in the fork.")
    if record.get("verifications"):
        problems.append(f"{path}: has verifications. They are made here, after the author's run.")
    url = ((prov.get("runner") or {}).get("url") or "").rstrip("/")
    if not (url == run.url or url.startswith(run.url + "/")):
        problems.append(f"{path}: provenance.runner.url is {url or 'missing'!r}, not the run it came from ({run.url}).")
    return problems


def load(data):
    if data is None:
        return None
    try:
        return yaml.safe_load(data)
    except yaml.YAMLError as e:
        raise Refused([f"A file is not valid YAML: {str(e).splitlines()[0]}"]) from e


def plain(value):
    """YAML dates as strings, as the protocol's entry check reads them, so that the schemas' string formats apply."""
    if isinstance(value, dict):
        return {k: plain(v) for k, v in value.items()}
    if isinstance(value, list):
        return [plain(v) for v in value]
    return value.isoformat() if isinstance(value, (datetime.date, datetime.datetime)) else value


def schema_problems(doc, name: str, schemas: Path | None) -> list[str]:
    """Problems against the protocol's schema, when tools/protocol.sh has laid it over the checkout."""
    path = (schemas or ROOT / "schemas") / f"{name}.schema.json"
    if not path.is_file():
        return []
    import jsonschema
    validator = jsonschema.Draft202012Validator(json.loads(path.read_text()))
    return [f"{name} schema: {'/'.join(map(str, e.path)) or '(top)'}: {e.message}"
            for e in sorted(validator.iter_errors(plain(doc)), key=lambda e: list(map(str, e.path)))][:10]


# What the script asks of git and GitHub.

def sh(*args: str, cwd: Path | None = None, check: bool = True) -> str:
    r = subprocess.run(list(args), cwd=cwd or ROOT, capture_output=True, text=True)
    if check and r.returncode != 0:
        raise Refused([f"{' '.join(args[:3])} failed: {(r.stderr or '').strip()[:500]}"])
    return r.stdout


def gh_json(*args: str):
    return json.loads(sh("gh", *args))


@dataclass
class Taken:
    run: Run
    manifest: dict = field(default_factory=dict)
    problems: list[str] = field(default_factory=list)
    committed: str | None = None
    waiting: bool = False
    what: str = "run"             # run, start or attempt
    paper: str = ""
    runs: list[str] = field(default_factory=list)    # the roles of a whole attempt's runs, in order
    notes: list[str] = field(default_factory=list)   # what a reviewer should know, when nothing is wrong


def submission_module(sha: str):
    """encore-protocol's tools/submission.py at the commit that signed the submission."""
    out = gh_json("api", f"repos/{PROTOCOL}/contents/tools/submission.py?ref={sha}")
    path = Path(tempfile.mkdtemp()) / "submission.py"
    path.write_bytes(base64.b64decode(out["content"]))
    spec = importlib.util.spec_from_file_location("submission", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def branch_state(registry: str, name: str, base: str) -> Branch:
    head = sh("git", "ls-remote", "origin", f"refs/heads/{name}").split()
    head = head[0] if head else None
    source = None
    if head:
        sh("git", "fetch", "-q", "--depth", "1", "origin", head)
        source = sh("git", "log", "-1", "--format=%(trailers:key=Encore-Source,valueonly)", head).strip() or None
    try:
        compare = gh_json("api", f"repos/{registry}/compare/{base}...main")
        on_main = compare.get("status") in ("ahead", "identical")
    except Refused:
        on_main = False
    return Branch(name, head, source, on_main)


def download(run: Run, dest: Path, name: str = "submission", artifact: str = "") -> Path:
    """The run's submission artifact, through the API, which serves it as soon as it is uploaded, while encore-runner
    is still waiting on this intake. A whole attempt's runs name theirs submission-<paper>-<role>; the newest of a
    name is taken, since a role run again in the same workflow run uploads again."""
    if artifact:
        # The artifact the ledger names, when it is that run's.
        one = gh_json("api", f"repos/{run.repo}/actions/artifacts/{artifact}")
        found = [one] if str((one.get("workflow_run") or {}).get("id")) == run.id and not one.get("expired") else []
    else:
        listed = gh_json("api", f"repos/{run.repo}/actions/runs/{run.id}/artifacts?name={name}")
        found = [a for a in listed.get("artifacts") or [] if a.get("name") == name and not a.get("expired")]
        found.sort(key=lambda a: a.get("created_at") or "", reverse=True)
    if not found:
        raise Refused([f"{run.url} has no {name}. Was it run from encore-runner with the input `registry`, and "
                       f"did it finish?"])
    dest.mkdir(parents=True, exist_ok=True)
    archive = dest / "submission.zip"
    with open(archive, "wb") as f:
        r = subprocess.run(["gh", "api", f"repos/{run.repo}/actions/artifacts/{found[0]['id']}/zip"], stdout=f,
                           stderr=subprocess.PIPE, text=False)
    if r.returncode != 0:
        raise Refused([f"Could not download the submission of {run.url}: {r.stderr.decode()[:300]}"])
    # Only the one file is taken out, by name, into memory; nothing else in the archive is written anywhere.
    with zipfile.ZipFile(archive) as z:
        if "submission.tar.gz" not in z.namelist():
            raise Refused([f"The submission of {run.url} holds no submission.tar.gz."])
        data = z.read("submission.tar.gz")
    (dest / "submission.tar.gz").write_bytes(data)
    return dest / "submission.tar.gz"


def take(run: Run, approved: bool, dry_run: bool, registry: str, setting: str | None) -> Taken:
    t = Taken(run)
    work = Path(tempfile.mkdtemp())
    tarball = download(run, work / "s")
    verified = json.loads(sh("gh", "attestation", "verify", str(tarball), "-R", run.repo,
                             "--signer-repo", PROTOCOL, "--format", "json"))
    signer = check_signature(verified, run)
    module = submission_module(signer.sha)
    try:
        manifest, files = module.read(tarball)
    except SystemExit as e:
        raise Refused([str(e)]) from e
    t.manifest = manifest
    t.problems += check_manifest(manifest, run, signer, registry)
    if t.problems:
        return t
    p, base_sha = manifest["paper"], manifest["base_sha"]
    branch = branch_state(registry, f"attempt/{p}", base_sha)
    t.problems += check_base(manifest, run, branch)
    if t.problems:
        return t
    sh("git", "fetch", "-q", "--depth", "1", "origin", base_sha)

    def base(path: str) -> bytes | None:
        r = subprocess.run(["git", "show", f"{base_sha}:{path}"], cwd=ROOT, capture_output=True)
        return r.stdout if r.returncode == 0 else None

    t.problems += check_changes(manifest, files, base, run, None)
    if t.problems:
        return t
    if not (approved or goes_straight_on(run.repo, setting)):
        t.waiting = True
        return t
    tree = work / "tree"
    sh("git", "worktree", "add", "-q", "--detach", str(tree), base_sha)
    module.apply(tarball, tree, p)
    sh("git", "add", "-A", "--", "claims", "attempts", "entries", "questions", "transcripts", cwd=tree)
    sh("git", "-c", "user.name=github-actions[bot]", "-c", "user.email=github-actions[bot]@users.noreply.github.com",
       "commit", "-q", "-m", f"{manifest['role'].capitalize()} run on {p}, from {run.repo}",
       "-m", f"Run: {run.url}\nAccount: {manifest.get('account')}\nProtocol: {PROTOCOL}@{signer.ref} ({signer.sha})",
       "-m", f"Encore-Source: {run.repo}\nEncore-Run: {run.url}", cwd=tree)
    t.committed = sh("git", "rev-parse", "HEAD", cwd=tree).strip()
    if not dry_run:
        # A plain push: it fails, and takes nothing, if the branch moved since the checks.
        sh("git", "push", "-q", "origin", f"HEAD:refs/heads/attempt/{p}", cwd=tree)
    return t


def commit(tree: Path, subject: str, body: str, trailers: str, allow_empty: bool = False) -> str:
    sh("git", "-c", "user.name=github-actions[bot]", "-c", "user.email=github-actions[bot]@users.noreply.github.com",
       "commit", "-q", *(["--allow-empty"] if allow_empty else []), "-m", subject, *(["-m", body] if body else []),
       "-m", trailers, cwd=tree)
    return sh("git", "rev-parse", "HEAD", cwd=tree).strip()


def registry_branch(name: str) -> tuple[str | None, str | None, str | None]:
    """The registry's branch of that name: its head, the repository it names (Encore-Source), and the run that
    announced the attempt (Encore-Start) when the head is the commit a start notice made."""
    head = sh("git", "ls-remote", "origin", f"refs/heads/{name}").split()
    if not head:
        return None, None, None
    sh("git", "fetch", "-q", "--depth", "1", "origin", head[0])
    trailer = lambda key: sh("git", "log", "-1", f"--format=%(trailers:key={key},valueonly)", head[0]).strip() or None
    return head[0], trailer("Encore-Source"), trailer("Encore-Start")


def on_main(registry: str, sha: str) -> bool:
    try:
        return gh_json("api", f"repos/{registry}/compare/{sha}...main").get("status") in ("ahead", "identical")
    except Refused:
        return False


def start(run: Run, paper: str, approved: bool, dry_run: bool, registry: str, setting: str | None) -> Taken:
    """Record that a runner has begun an attempt on a paper: the registry's branch attempt/<paper>, one empty commit
    on main that names the runner and its run."""
    t = Taken(run, what="start", paper=paper)
    if not KEY.fullmatch(paper or ""):
        t.problems.append(f"Not a paper key: {paper!r}.")
        return t
    sh("git", "fetch", "-q", "origin", "main")
    main = sh("git", "rev-parse", "FETCH_HEAD").strip()
    if subprocess.run(["git", "cat-file", "-e", f"{main}:papers/datasets/{paper}.yaml"], cwd=ROOT,
                      capture_output=True).returncode != 0:
        t.problems.append(f"The registry does not list {paper} (papers/datasets/{paper}.yaml). Ask for it with a run "
                          f"request first.")
    try:
        gh_json("api", f"repos/{run.repo}/actions/runs/{run.id}")
    except Refused:
        t.problems.append(f"{run.url} is not a run the registry can read.")
    head, source, _ = registry_branch(f"attempt/{paper}")
    if head and (source or "").lower() == run.repo.lower():
        t.committed = head
        t.notes.append(f"attempt/{paper} already names {run.repo}.")
        return t
    if head:
        t.problems.append(f"attempt/{paper} is an attempt {source or 'begun in the registry'} is making; wait for it "
                          f"to finish.")
    if t.problems:
        return t
    if not (approved or goes_straight_on(run.repo, setting)):
        t.waiting = True
        return t
    tree = Path(tempfile.mkdtemp()) / "tree"
    sh("git", "worktree", "add", "-q", "--detach", str(tree), main)
    t.committed = commit(tree, f"Attempt on {paper} begun by {run.repo}", "",
                         f"Encore-Source: {run.repo}\nEncore-Start: {run.url}", allow_empty=True)
    if not dry_run:
        # A plain push: it fails, and records nothing, if someone else began on the paper meanwhile.
        sh("git", "push", "-q", "origin", f"HEAD:refs/heads/attempt/{paper}", cwd=tree)
    return t


def read_ledger(repo: str, paper: str, registry: str) -> dict:
    try:
        text = sh("gh", "api", f"repos/{repo}/contents/{LEDGER}?ref=attempt/{paper}",
                  "-H", "Accept: application/vnd.github.raw")
        ledger = json.loads(text)
    except (Refused, ValueError) as e:
        raise Refused([f"{repo} has no attempt on {paper}: its branch attempt/{paper} has no {LEDGER}."]) from e
    problems = []
    if ledger.get("paper") != paper:
        problems.append(f"The ledger is for {ledger.get('paper')!r}, not {paper}.")
    if (ledger.get("registry") or "").lower() != registry.lower():
        problems.append(f"The attempt read {ledger.get('registry')!r}, not {registry}.")
    if not re.fullmatch(r"[0-9a-f]{40}", str(ledger.get("base_sha") or "")):
        problems.append("The ledger names no commit of main the attempt began at (base_sha).")
    if not ledger.get("runs"):
        problems.append("The ledger lists no runs.")
    if problems:
        raise Refused(problems)
    return ledger


def other_runs(repo: str, paper: str, listed: set[str]) -> list[str]:
    """The runner's runs on the paper that the ledger does not list, for whoever reviews the attempt: a run made and
    left out shows here. A note, not a check; the listing is the runner's own."""
    try:
        found = gh_json("api", f"repos/{repo}/actions/runs?per_page=100").get("workflow_runs") or []
    except Refused:
        return []
    return sorted(r["html_url"] for r in found
                  if (r.get("display_title") or "").split(" ")[0] == paper and r.get("html_url") not in listed)


def take_attempt(repo: str, paper: str, approved: bool, dry_run: bool, registry: str, setting: str | None,
                 schemas: Path | None = None) -> Taken:
    """Take a whole attempt from a runner's branch: every run's signature, each run from the state the one before
    it left, each role's changes, and then the commits, pushed as the registry's attempt/<paper>."""
    t = Taken(Run(repo, "0"), what="attempt", paper=paper)
    if not KEY.fullmatch(paper or ""):
        raise Refused([f"Not a paper key: {paper!r}."])
    ledger = read_ledger(repo, paper, registry)
    base_sha = ledger["base_sha"]
    if not on_main(registry, base_sha):
        raise Refused([f"The attempt began at {base_sha}, which is not a commit of main."])
    head, source, announced = registry_branch(f"attempt/{paper}")
    if head and not ((source or "").lower() == repo.lower() and announced):
        raise Refused([f"attempt/{paper} is an attempt {source or 'begun in the registry'} is making here; "
                       f"{repo}'s cannot take its place."])
    work = Path(tempfile.mkdtemp())
    tree = work / "tree"
    sh("git", "fetch", "-q", "--depth", "1", "origin", base_sha)
    sh("git", "worktree", "add", "-q", "--detach", str(tree), base_sha)

    def at(path: str) -> bytes | None:
        f = tree / path
        return f.read_bytes() if f.is_file() else None

    last = None
    for n, entry in enumerate(ledger["runs"], 1):
        role = str(entry.get("role"))
        where = f"Run {n} ({role})"
        try:
            run = parse_run(str(entry.get("run_url")))
        except Refused:
            raise Refused([f"{where}: the ledger gives no run address."]) from None
        if run.repo.lower() != repo.lower():
            raise Refused([f"{where}: made in {run.repo}, not {repo}."])
        t.run = run
        tarball = download(run, work / f"s{n}", f"submission-{paper}-{role}", str(entry.get("artifact") or ""))
        verified = json.loads(sh("gh", "attestation", "verify", str(tarball), "-R", run.repo,
                                 "--signer-repo", PROTOCOL, "--format", "json"))
        signer = check_signature(verified, run)
        module = submission_module(signer.sha)
        try:
            manifest, files = module.read(tarball, paper)
        except SystemExit as e:
            raise Refused([f"{where}: {e}"]) from e
        t.manifest = last = manifest
        problems = []
        if manifest.get("role") != role:
            problems.append(f"the ledger calls it {role}, and its submission {manifest.get('role')!r}.")
        if workflow_of(role) is None:
            problems.append(f"{role!r} is not a role of an attempt.")
        elif workflow_of(role) != signer.workflow:
            problems.append(f"a {role} run is made by {workflow_of(role)}.yml, but this one was signed by "
                            f"{signer.workflow}.yml.")
        if (manifest.get("registry") or "").lower() != registry.lower():
            problems.append(f"it read {manifest.get('registry')!r}, not {registry}.")
        if (manifest.get("repository") or "").lower() != repo.lower() or str(manifest.get("run_id")) != run.id:
            problems.append(f"its submission says it is from {manifest.get('repository')} run "
                            f"{manifest.get('run_id')}, not {run.repo} run {run.id}.")
        if manifest.get("base_sha") != base_sha:
            problems.append(f"it began at {manifest.get('base_sha')}, and the attempt at {base_sha}.")
        # The chain: the run started from the paper's files as the runs before it left them.
        here = module.digest(tree, paper)
        if manifest.get("state_before") != here:
            problems.append(f"it started from a state ({manifest.get('state_before')}) that is not the one the runs "
                            f"before it left ({here}). A run is missing from the ledger, or the branch was edited "
                            f"between runs.")
        if not problems:
            # The author's first run adds the attempt's record; the author run again, after one that failed, goes
            # on with the record that one left, as a revision does.
            if role in ROLES and not (role == "author" and "author" in t.runs):
                problems += check_changes(manifest, files, at, run, schemas)
            else:
                problems += later_changes(manifest, files, at)
        if problems:
            t.problems += [f"{where}: {x}" for x in problems]
            return t
        module.apply(tarball, tree, paper)
        sh("git", "add", "-A", "--", ".", cwd=tree)
        commit(tree, f"{role.capitalize()} run on {paper}, from {repo}",
               f"Run: {run.url}\nResult: {manifest.get('result')}\nAccount: {manifest.get('account')}\n"
               f"Protocol: {PROTOCOL}@{signer.ref} ({signer.sha})",
               f"Encore-Source: {repo}\nEncore-Run: {run.url}", allow_empty=True)
        t.runs.append(role)
    if last.get("result") != "success":
        t.problems.append(f"The last run ({t.runs[-1]}) ended as {last.get('result')!r}; the registry takes an attempt "
                          f"whose last run succeeded.")
    t.problems += finished_problems(tree, paper, repo, schemas)
    if t.problems:
        return t
    unlisted = other_runs(repo, paper, {str(r.get("run_url")) for r in ledger["runs"]})
    if unlisted:
        t.notes.append("Runs of the runner on this paper that the attempt does not list: " + ", ".join(unlisted))
    t.committed = sh("git", "rev-parse", "HEAD", cwd=tree).strip()
    if not (approved or goes_straight_on(repo, setting)):
        t.waiting = True
        return t
    if not dry_run:
        # Over the commit the start notice made, and nothing else: with a lease on that commit when there is one,
        # and a plain push when there is none, so that a branch that moved since the checks is never replaced.
        lease = [f"--force-with-lease=refs/heads/attempt/{paper}:{head}"] if head else []
        sh("git", "push", "-q", *lease, "origin", f"HEAD:refs/heads/attempt/{paper}", cwd=tree)
    return t


def issue_fields(text: str) -> dict[str, str]:
    """The fields of an issue made from a form: each a `### Label` heading and the text under it."""
    fields, label = {}, None
    for line in (text or "").splitlines():
        if line.startswith("### "):
            label = line[4:].strip().lower()
            fields[label] = ""
        elif label is not None:
            fields[label] = (fields[label] + "\n" + line).strip()
    return fields


def asked(text: str) -> tuple[str, str]:
    """What an issue asks the intake for (run, start or attempt) and the paper it names."""
    fields = issue_fields(text)
    said = fields.get("what", "").lower()
    what = "start" if "start" in said else "attempt" if "finish" in said else "run"
    return what, fields.get("paper", "").strip()


def report(t: Taken, dry_run: bool) -> str:
    if t.what in ("start", "attempt"):
        return report_attempt(t, dry_run)
    return report_run(t, dry_run)


def report_attempt(t: Taken, dry_run: bool) -> str:
    where = f"attempt/{t.paper}"
    title = "the start of an attempt" if t.what == "start" else "an attempt"
    head = f"## Intake: {title} on {t.paper}, from {t.run.repo}\n"
    if t.runs:
        head += "\nRuns checked, in order: " + ", ".join(t.runs) + ".\n"
    notes = "".join(f"\n{n}\n" for n in t.notes)
    if t.problems:
        return head + "\nNot taken:\n\n" + "\n".join(f"- {p}" for p in t.problems) + "\n"
    if t.waiting:
        return head + notes + ("\nEvery check passed. It comes from a repository whose attempts wait for a person: "
                               "someone in queue/priority.yaml takes it by adding the label `approved` to this "
                               "issue, or by starting the intake with `approve` ticked.\n")
    if dry_run:
        return head + notes + f"\nEvery check passed. A dry run: nothing was pushed to {where}.\n"
    if t.what == "start":
        return head + notes + (f"\nRecorded: {where} names {t.run.repo} ({t.committed}). Send the attempt when its "
                               f"last run has finished.\n")
    return head + notes + (f"\nTaken: {where} is at {t.committed}, one commit for each run. Next: its pull request, "
                           f"which the registry's check runs on.\n")


def report_run(t: Taken, dry_run: bool) -> str:
    m = t.manifest
    what = f"{m.get('role')} run on {m.get('paper')}" if m else "run"
    head = f"## Intake: {what}, from {t.run.repo}\n\nRun: {t.run.url}\n"
    if t.problems:
        return head + "\nNot taken:\n\n" + "\n".join(f"- {p}" for p in t.problems) + "\n"
    if t.waiting:
        return head + ("\nEvery check passed. It comes from a repository whose runs wait for a person: someone in "
                       "queue/priority.yaml takes it by adding the label `approved` to this issue, or by starting the "
                       "intake for this run with `approve` ticked.\n")
    where = f"attempt/{m['paper']}"
    if dry_run:
        return head + f"\nEvery check passed. A dry run: nothing was pushed to {where}.\n"
    nxt = {"claims": "claims-check", "claims-check": "the author, once the last check says the claims are ready",
           "author": "the verification rounds, here"}[m["role"]]
    return head + f"\nTaken: committed to {where} ({t.committed}). Next: {nxt}.\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("run_url", nargs="?")
    ap.add_argument("--issue-body-env", help="read the run's address from this environment variable")
    ap.add_argument("--issue", type=int)
    ap.add_argument("--approved-by", default="", metavar="USER",
                    help="the GitHub user who approved the run; it counts if they are in queue/priority.yaml")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--registry", default=os.environ.get("GITHUB_REPOSITORY", REGISTRY))
    ap.add_argument("--what", choices=sorted(WHAT), default="",
                    help="start: a runner has begun an attempt; attempt: a finished attempt; run: one run")
    ap.add_argument("--paper", default="", help="the paper's key, for start and attempt")
    args = ap.parse_args(argv)
    text = args.run_url or os.environ.get(args.issue_body_env or "", "")
    what, paper = args.what, args.paper
    if not what:
        what, paper = asked(text) if not args.run_url else ("run", paper)
    setting = os.environ.get("ENCORE_INTAKE_AUTO")
    try:
        run = parse_run(text)
        approved = bool(args.approved_by) and args.approved_by.lower() in steer()
        if what == "start":
            t = start(run, paper, approved, args.dry_run, args.registry, setting)
        elif what == "attempt":
            t = take_attempt(run.repo, paper, approved, args.dry_run, args.registry, setting)
        else:
            t = take(run, approved, args.dry_run, args.registry, setting)
    except Refused as e:
        t = Taken(Run("?", "?"), problems=e.problems, what=what, paper=paper)
        try:
            t.run = parse_run(text)
        except Refused:
            pass
    out = report(t, args.dry_run)
    print(out)
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a") as f:
            f.write(out)
    if args.issue:
        subprocess.run(["gh", "issue", "comment", str(args.issue), "-R", args.registry, "--body", out], cwd=ROOT)
        if t.committed and not t.waiting and not args.dry_run:
            subprocess.run(["gh", "issue", "close", str(args.issue), "-R", args.registry], cwd=ROOT)
    for p in t.problems:
        print(f"::error::{p}")
    return 1 if t.problems else 0


if __name__ == "__main__":
    sys.exit(main())
