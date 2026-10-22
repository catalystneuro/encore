"""One `encore check`: the registry's protocol run on a dataset, on this machine, with the user's own Claude login.

A run lives in its output directory:

    <out>/registry/      a copy of the registry, on a branch of its own: the protocol, the prompts, the tools,
                         and what the run writes (claims, entry, attempt record, transcripts)
    <out>/registry/paper the paper's text and PDF; never committed
    <out>/logs/          each role's stream from Claude Code (<role>.jsonl)
    <out>/work-<role>/   what a verifier is given, outside the registry
    <out>/state.json     which roles are done; a second `encore check` with the same --out goes on from there
    <out>/report.md      the outcome of every claim and the findings about the data

Each role is one `claude -p` with the same prompt, tools and limits as in the registry's workflows
(.github/workflows/attempt.yml and papers.yml), in Claude Code's sandbox: its commands may write only inside the
run's directory and reach only the hosts in NETWORK.
"""

from __future__ import annotations

import datetime
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

REPO_URL = "https://github.com/catalystneuro/encore.git"
TOOLS = "Bash,Read,Write,Edit,Glob,Grep,WebFetch,WebSearch,Agent,TodoWrite"
NOT_TOOLS = "ScheduleWakeup,CronCreate,CronDelete,CronList,Monitor,RemoteTrigger,Workflow"
QUICK = ("claims", "claims-check", "author")
FULL = QUICK + ("answer", "author-answers", "verifier-1", "author-revise-1", "verifier-2", "author-revise-2",
                "verifier-3", "author-revise-3")
# The hosts an agent's commands may reach: the archives, Python packages, and the paper's DOI.
NETWORK = ["dandiarchive.org", "*.dandiarchive.org", "*.amazonaws.com", "crcns.org", "*.ebrains.eu",
           "pypi.org", "files.pythonhosted.org", "github.com", "*.githubusercontent.com", "doi.org", "*.doi.org"]
DOI = re.compile(r"\b(10\.[0-9]{4,9}/[^\s\"<>]+)")
# The one finished attempt the prompts point to for file formats. Every other dataset's work is taken out of a
# run's copy of the registry, so that no agent can read another attempt on the same paper or data.
EXAMPLE = {"claims": "001453", "entries": "001453-fouke-2025", "attempts": "001453-fouke-2025-01.yaml"}


class Stop(Exception):
    """The run cannot go on; the message says why and what to do."""


@dataclass
class Dataset:
    archive: str        # local, remote, or an archive the registry knows (dandi, crcns, ebrains)
    id: str
    location: str       # the directory or URL; for an archive, its key
    fingerprint: str    # stands in for a version; "" for an archive
    version: str = ""   # for an archive: a version, or draft

    @property
    def folder(self) -> str:
        return self.id if self.archive == "dandi" else f"{self.archive}-{self.id}"


def git(*args: str, cwd: Path | None = None) -> str:
    return subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True, text=True).stdout


def slug(name: str) -> str:
    """A dataset's id from a directory's or URL's last part: lower case letters, digits and hyphens."""
    s = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return s[:40].strip("-") or "dataset"


def fingerprint(directory: Path) -> str:
    """A short hash of a directory's files: their paths, sizes, and first and last megabyte. Cheap on large
    NWB files, and changed by any rewrite of a file that a conversion would make."""
    h = hashlib.sha256()
    for path in sorted(p for p in directory.rglob("*") if p.is_file() and not p.name.startswith(".")):
        size = path.stat().st_size
        h.update(f"{path.relative_to(directory).as_posix()}\0{size}\0".encode())
        with path.open("rb") as f:
            h.update(f.read(1 << 20))
            if size > 2 << 20:
                f.seek(-(1 << 20), os.SEEK_END)
                h.update(f.read())
    return "files-" + h.hexdigest()[:12]


def dataset_of(spec: str, version: str = "") -> Dataset:
    """A local directory, a URL, or a dataset in an archive (DANDI:000147, CRCNS:ret-1)."""
    if re.match(r"^[a-z][a-z0-9+.-]*://", spec):
        name = spec.rstrip("/").rsplit("/", 1)[-1]
        return Dataset("remote", slug(name), spec, "url-" + hashlib.sha256(spec.encode()).hexdigest()[:12])
    path = Path(spec).expanduser()
    if path.is_dir():
        path = path.resolve()
        return Dataset("local", slug(path.name), str(path), fingerprint(path))
    if path.exists():
        raise Stop(f"{spec} is a file; give the directory that holds the dataset's files.")
    m = re.fullmatch(r"([A-Za-z][A-Za-z0-9]*):([A-Za-z0-9._-]+)|([0-9]{6})", spec.strip())
    if not m:
        raise Stop(f"{spec} is not a directory, a URL, or a dataset in an archive (such as DANDI:000147).")
    archive, id_ = (m.group(1).lower(), m.group(2)) if m.group(1) else ("dandi", m.group(3))
    return Dataset(archive, id_, f"{archive}:{id_}", "", version)


def registry_source(ref: str) -> Path:
    """The registry to copy for a run: the clone this package sits in, when it is installed from one; else a
    cached clone of the public repository at REF, brought up to date."""
    here = Path(__file__).resolve().parents[1]
    if (here / "docs" / "protocol.md").is_file() and (here / ".git").exists():
        return here
    cache = Path(os.environ.get("ENCORE_CACHE") or Path.home() / ".cache" / "encore") / "registry"
    if (cache / ".git").exists():
        git("fetch", "-q", "--depth", "1", "origin", ref, cwd=cache)
        git("checkout", "-q", "-f", "FETCH_HEAD", cwd=cache)
    else:
        cache.parent.mkdir(parents=True, exist_ok=True)
        git("clone", "-q", "--depth", "1", "--branch", ref, REPO_URL, str(cache))
    return cache


def paper_text(path: Path) -> tuple[str, list[str]]:
    """A paper's text, page by page as the paper store keeps it, and the pages' text for finding its DOI."""
    if path.suffix.lower() in (".txt", ".md"):
        text = path.read_text(errors="replace")
        return text, [text[:20000]]
    if path.suffix.lower() != ".pdf":
        raise Stop(f"{path.name}: give the paper as a PDF or a text file.")
    import pymupdf  # as the paper store uses
    pages = [page.get_text() for page in pymupdf.open(path)]
    return "".join(f"\n=== page {n} ===\n{t}" for n, t in enumerate(pages, 1)), pages[:2]


def find_doi(texts: list[str]) -> str | None:
    for t in texts:
        m = DOI.search(t)
        if m:
            return m.group(1).rstrip(".,;)]").lower()
    return None


class Run:
    def __init__(self, out: Path, dataset: Dataset, paper: Path | None, doi: str | None, title: str | None,
                 full: bool, model: str, ref: str, sandbox: bool = True):
        self.out, self.dataset, self.paper, self.doi, self.title = out.resolve(), dataset, paper, doi, title
        self.full, self.model, self.ref, self.sandbox = full, model, ref, sandbox
        self.registry = self.out / "registry"
        self.logs = self.out / "logs"
        self.state_path = self.out / "state.json"
        self.state = json.loads(self.state_path.read_text()) if self.state_path.is_file() else {}

    # Setting up -------------------------------------------------------------------------------------------

    def prepare(self) -> None:
        if self.state.get("prepared"):
            say(f"Going on with the run in {self.out}")
            return
        if self.paper is None:
            raise Stop("Give the paper with --paper (a PDF or a text file).")
        text, first_pages = paper_text(self.paper)
        doi = (self.doi or find_doi(first_pages) or "").lower().removeprefix("doi:").removeprefix("https://doi.org/")
        if not doi:
            raise Stop("Found no DOI in the paper. Give it with --doi; a preprint's DOI is fine.")
        title = self.title or self.paper.stem

        self.out.mkdir(parents=True, exist_ok=True)
        self.logs.mkdir(exist_ok=True)
        shutil.rmtree(self.registry, ignore_errors=True)   # a setup that stopped part-way
        source = registry_source(self.ref)
        say(f"Copying the registry's protocol from {source}")
        git("clone", "-q", str(source), str(self.registry))
        git("checkout", "-q", "-b", f"encore/{self.dataset.folder}", cwd=self.registry)
        git("config", "user.name", "encore", cwd=self.registry)
        git("config", "user.email", "encore@localhost", cwd=self.registry)
        self.prune()
        protocol = (self.registry / "docs" / "protocol.md").read_text().split("Version: `", 1)[1].split("`", 1)[0]
        name = doi.replace("/", "-")
        paper_dir = self.registry / "paper"
        paper_dir.mkdir()
        header = (f"DOI: {doi}\nVersion: as supplied\nSource: given to encore check ({self.paper.name})\n"
                  f"Stored: {datetime.date.today().isoformat()}\nExtracted: "
                  f"{'PyMuPDF' if self.paper.suffix.lower() == '.pdf' else 'as given'}\n" + "-" * 72 + "\n")
        (paper_dir / f"{name}.txt").write_text(header + text)
        if self.paper.suffix.lower() == ".pdf":
            shutil.copy(self.paper, paper_dir / f"{name}.pdf")

        d = self.dataset
        if d.archive in ("local", "remote"):
            target = {"archive": d.archive, "id": d.id, "name": title, "fingerprint": d.fingerprint,
                      "papers": [{"doi": doi, "title": title, "preprint": False}]}
            target["path" if d.archive == "local" else "url"] = d.location
            (self.registry / "targets" / "local.json").write_text(json.dumps({"targets": [target]}, indent=1))
        self.state = {"prepared": True, "dataset": d.__dict__, "folder": d.folder, "doi": doi, "title": title,
                      "mode": "full" if self.full else "quick", "model": self.model, "protocol": protocol,
                      "source": str(source), "started": now(), "roles": {}}
        self.save()

    def prune(self) -> None:
        """Take every other dataset's claims, entries, attempts, questions and transcripts out of the copy."""
        for kind in ("claims", "entries", "attempts", "questions", "transcripts"):
            for path in (self.registry / kind).glob("*"):
                if path.name != EXAMPLE.get(kind) and path.name != ".gitkeep":
                    shutil.rmtree(path) if path.is_dir() else path.unlink()
        # The notes on earlier attempts, and the README's table of their outcomes, go too.
        stub = "Left out of an `encore check`: this page describes other attempts.\n"
        shutil.rmtree(self.registry / "docs" / "pilot-notes", ignore_errors=True)
        for name in ("docs/pilot-notes.md", "docs/conversion-tracker.md"):
            if (self.registry / name).is_file():
                (self.registry / name).write_text(stub)
        readme = self.registry / "README.md"
        if readme.is_file():
            readme.write_text("".join(line for line in readme.read_text().splitlines(keepends=True)
                                      if not re.match(r"^\| \[", line)))
        git("add", "-A", "--", *[p for p in ("claims", "entries", "attempts", "questions", "transcripts", "docs",
                                              "README.md") if (self.registry / p).exists()], cwd=self.registry)
        git("commit", "-q", "-m", "encore check: only the example attempt", cwd=self.registry)

    def save(self) -> None:
        self.state_path.write_text(json.dumps(self.state, indent=1))

    # Running roles ----------------------------------------------------------------------------------------

    def env(self) -> dict:
        env = dict(os.environ, CLAUDE_CODE_SUBPROCESS_ENV_SCRUB="1", CLAUDE_CODE_DISABLE_AUTO_MEMORY="1",
                   DISABLE_AUTOUPDATER="1", DISABLE_TELEMETRY="1", CLAUDE_CODE_DISABLE_BACKGROUND_TASKS="1",
                   BASH_DEFAULT_TIMEOUT_MS="3600000", BASH_MAX_TIMEOUT_MS="7200000")
        if self.dataset.archive == "local":
            env["ENCORE_LOCAL_DATA"] = self.dataset.location
        return env

    def settings(self, cwd: Path) -> str:
        """Claude Code settings for a role: the sandbox, writable only inside the run's directory."""
        network = list(NETWORK)
        if self.dataset.archive == "remote":
            network.append(re.sub(r"^[a-z0-9+.-]+://([^/:]+).*$", r"\1", self.dataset.location))
        caches = [str(Path.home() / p) for p in (".cache", "Library/Caches", ".local/share/jupyter", "Library/Jupyter")]
        return json.dumps({"sandbox": {
            "enabled": self.sandbox, "autoAllowBashIfSandboxed": True, "allowUnsandboxedCommands": False,
            "filesystem": {"allowWrite": [str(self.out), str(cwd), "/tmp", os.environ.get("TMPDIR", "/tmp"), *caches]},
            "network": {"allowedDomains": network}}})

    def prompt(self, role: str) -> str:
        args = [sys.executable, "tools/agent_run.py", "prompt", role, self.dataset.folder, "--model", self.model]
        if self.dataset.version and role == "author":
            args += ["--version", self.dataset.version]
        return subprocess.run(args, cwd=self.registry, check=True, capture_output=True, text=True,
                              env=self.env()).stdout

    def claude(self, role: str, prompt: str, cwd: Path) -> int:
        """Run one role and keep its stream; print one line per step as it goes."""
        if shutil.which("claude") is None:
            raise Stop("Claude Code is not installed: see https://docs.claude.com/en/docs/claude-code")
        stream = self.logs / f"{role}.jsonl"
        cmd = ["claude", "-p", prompt, "--model", self.model, "--output-format", "stream-json", "--verbose",
               "--forward-subagent-text", "--permission-prompts", "none", "--allowedTools", TOOLS,
               "--disallowedTools", NOT_TOOLS, "--settings", self.settings(cwd)]
        progress = subprocess.Popen([sys.executable, str(self.registry / "tools" / "progress.py")],
                                    stdin=subprocess.PIPE, text=True)
        with stream.open("w") as log, open(self.logs / f"{role}.stderr", "w") as err:
            agent = subprocess.Popen(cmd, cwd=cwd, env=self.env(), stdout=subprocess.PIPE, stderr=err, text=True)
            for line in agent.stdout:
                log.write(line)
                log.flush()
                try:
                    progress.stdin.write(line)
                    progress.stdin.flush()
                except BrokenPipeError:
                    pass
            agent.wait()
        progress.stdin.close()
        progress.wait()
        return agent.returncode

    def transcript(self, role: str) -> None:
        dest = self.registry / "transcripts" / self.dataset.folder
        dest.mkdir(parents=True, exist_ok=True)
        subprocess.run([sys.executable, str(self.registry / "tools" / "transcript.py"), str(self.logs / f"{role}.jsonl"),
                        str(dest / f"{role}.md"), "--omit", "paper/", "--report", str(dest / f"{role}-report.md"),
                        "--home", str(Path.home()), "--title", f"{self.dataset.folder} · {role} · encore check"],
                       cwd=self.registry, check=True, capture_output=True, text=True)

    def commit(self, role: str) -> None:
        paths = [p for p in ("attempts", "claims", "entries", "questions", "transcripts", "README.md")
                 if (self.registry / p).exists()]
        git("add", "-A", "--", *paths, cwd=self.registry)
        if subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=self.registry).returncode:
            git("commit", "-q", "-m", f"encore check: {role}", cwd=self.registry)

    def role(self, role: str) -> None:
        done = self.state["roles"].get(role, {})
        if done.get("status") == "success":
            return
        say(f"\n{role}: starting")
        cwd = self.registry
        if role.startswith("verifier"):
            cwd = self.verifier_package(role)
        self.state["roles"][role] = {"status": "running", "started": now()}
        self.save()
        code = self.claude(role, self.prompt(role), cwd)
        self.transcript(role)
        self.commit(role)
        self.state["roles"][role].update(status="success" if code == 0 else "failed", finished=now())
        self.save()
        if code != 0:
            tail = (self.logs / f"{role}.stderr").read_text()[-800:]
            limit = "limit" in tail.lower() or "limit" in (self.logs / f"{role}.jsonl").read_text()[-3000:].lower()
            raise Stop(f"{role} stopped (Claude Code exited with {code})."
                       + (" It looks like a usage limit: run the same command again once it resets, and the run "
                          "goes on from this role." if limit else f" The end of its log:\n{tail}"))
        say(f"{role}: done")

    def sandboxed(self, command: str, cwd: Path, name: str) -> None:
        """Run one shell command of ours inside the same sandbox as the agents, by asking Claude Code to run it:
        the notebooks it executes were written by an agent."""
        prompt = (f"Use the Bash tool to run exactly this command, once, and wait for it to finish:\n\n{command}\n\n"
                  "Then reply with only the last line it printed and its exit status.")
        if self.claude(name, prompt, cwd) != 0:
            raise Stop(f"Running `{command}` failed; see {self.logs / (name + '.jsonl')}.")

    def verifier_package(self, role: str) -> Path:
        """What a verifier is given, in a directory outside the registry, as attempt.yml prepares it."""
        entry = subprocess.run([sys.executable, "tools/agent_run.py", "entry", role, self.dataset.folder],
                               cwd=self.registry, check=True, capture_output=True, text=True).stdout.strip()
        if role == "verifier-1":
            self.sandboxed(f"{sys.executable} tools/entry.py run entries/{entry} && "
                           f"{sys.executable} tools/entry.py handover entries/{entry}", self.registry, "entry-run")
        work = self.out / f"work-{role}"
        shutil.rmtree(work, ignore_errors=True)
        subprocess.run([sys.executable, "tools/agent_run.py", "package", role, self.dataset.folder, str(work)],
                       cwd=self.registry, check=True, capture_output=True, text=True)
        shutil.copytree(self.registry / "paper", work / "paper")
        return work

    # The sequence -----------------------------------------------------------------------------------------

    def claims_ready(self) -> bool:
        import yaml
        files = sorted((self.registry / "claims" / self.dataset.folder).glob("*.yaml"))
        if not files:
            return False
        checks = (yaml.safe_load(files[0].read_text()) or {}).get("checks") or [{}]
        return bool(checks[-1].get("ready"))

    def open_questions(self) -> int:
        import yaml
        path = self.registry / "questions" / f"{self.dataset.folder}.yaml"
        if not path.is_file():
            return 0
        q = yaml.safe_load(path.read_text()) or []
        q = q.get("questions", []) if isinstance(q, dict) else q
        return sum(1 for x in q if not x.get("answered"))

    def proposals(self) -> bool:
        out = subprocess.run([sys.executable, "tools/agent_run.py", "proposals", "author", self.dataset.folder],
                             cwd=self.registry, capture_output=True, text=True).stdout.strip()
        return out == "true"

    def go(self) -> Path:
        self.prepare()
        # The claims, unless the registry already has a checked claims file for this dataset (an archive's).
        if not self.claims_ready() or self.state["roles"].get("claims"):
            self.role("claims")
            if not (self.registry / "claims" / self.dataset.folder).is_dir():
                raise Stop("The reader wrote no claims file: see "
                           f"{self.registry / 'transcripts' / self.dataset.folder / 'claims-report.md'}.")
            self.role("claims-check")
            if not self.claims_ready():
                raise Stop("The claims check says the claims file is not ready: see "
                           f"{self.registry / 'transcripts' / self.dataset.folder / 'claims-check-report.md'}.")
        self.role("author")
        if self.full:
            if self.open_questions() or self.state["roles"].get("answer"):
                self.role("answer")
                self.role("author-answers")
            for role in ("verifier-1", "author-revise-1", "verifier-2", "author-revise-2"):
                self.role(role)
            if self.proposals():
                self.role("verifier-3")
                self.role("author-revise-3")
        from .report import write_report
        self.state["finished"] = now()
        self.save()
        return write_report(self.out, self.registry, self.state)


def now() -> str:
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def say(text: str) -> None:
    print(text, flush=True)
