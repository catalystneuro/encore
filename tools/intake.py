"""Take a run made from encore-runner, or a fork of it, into the registry (encore-protocol docs/outside-runs.md).

    python tools/intake.py RUN_URL [--approved-by USER] [--issue N] [--dry-run]
    python tools/intake.py --issue-body-env ISSUE_BODY [--approved-by USER] [--issue N] [--dry-run]

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


def download(run: Run, dest: Path) -> Path:
    """The run's `submission` artifact, through the API, which serves it as soon as it is uploaded, while encore-runner
    is still waiting on this intake."""
    listed = gh_json("api", f"repos/{run.repo}/actions/runs/{run.id}/artifacts?name=submission")
    found = [a for a in listed.get("artifacts") or [] if a.get("name") == "submission" and not a.get("expired")]
    if not found:
        raise Refused([f"{run.url} has no submission. Was it run from encore-runner with the input `registry`, and "
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


def report(t: Taken, dry_run: bool) -> str:
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
    args = ap.parse_args(argv)
    text = args.run_url or os.environ.get(args.issue_body_env or "", "")
    try:
        run = parse_run(text)
        approved = bool(args.approved_by) and args.approved_by.lower() in steer()
        t = take(run, approved, args.dry_run, args.registry, os.environ.get("ENCORE_INTAKE_AUTO"))
    except Refused as e:
        t = Taken(Run("?", "?"), problems=e.problems)
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
        if t.committed and not args.dry_run:
            subprocess.run(["gh", "issue", "close", str(args.issue), "-R", args.registry], cwd=ROOT)
    for p in t.problems:
        print(f"::error::{p}")
    return 1 if t.problems else 0


if __name__ == "__main__":
    sys.exit(main())
