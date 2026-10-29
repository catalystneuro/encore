"""Prepare one agent run on a target: its prompt, and for a verifier its materials.

    python tools/agent_run.py prompt  ROLE DATASET [--model M] > prompt.md
    python tools/agent_run.py package ROLE DATASET DEST
    python tools/agent_run.py entry   ROLE DATASET        # the entry directory's name, if any
    python tools/agent_run.py proposals ROLE DATASET      # "true" if the attempt has proposed changes
    python tools/agent_run.py repeat ROLE DATASET         # "true" if the attempt in progress has one before it

DATASET is written any way tools/datasets.py accepts (000003, DANDI:000003, ebrains:<id>); the
functions below take its folder name.

ROLE is paper-match, which judges whether each paper the archive names is the paper behind the data
(docs/pipeline.md, step 1; papers.yml runs it, with claims, claims-check and answer), or one of
author, verifier-1, author-revise-1, verifier-2, author-revise-2, the order in which an attempt goes through docs/protocol.md, and verifier-3 and
author-revise-3, the third round that settles changes proposed after the second. A repeat attempt
then has reconcile, which compares it with the attempt before it: until then its runs are blind to
earlier attempts (tools/blind.sh). A last role, recorder, writes the finished attempt's notes in docs/pilot-notes/<attempt>.md. The prompts are
docs/agents/<role>.md with the target's details filled in. A run's transcript
and final report are kept as transcripts/<folder>/<role>.md and
<role>-report.md (tools/transcript.py writes them).

`package` copies what a verifier is given into DEST: for round 1, the output
of `tools/entry.py handover` (run the entry and the handover first); for round
2, the executed notebooks, helpers, entry README, claims file, attempt record
and the round-1 report. Used by .github/workflows/attempt.yml.
"""

from __future__ import annotations

import argparse
import datetime
import json
import os
import shutil
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import datasets  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)   # libyaml when PyYAML has it: records_of reads every record
TEMPLATES = {"paper-match": "paper-match", "claims": "claims", "claims-check": "claims-check", "answer": "answer",
             "author": "author", "author-answers": "author-answers",
             "verifier-1": "verifier-1", "author-revise-1": "author-revise",
             "verifier-2": "verifier-2", "author-revise-2": "author-revise",
             "verifier-3": "verifier-3", "author-revise-3": "author-revise-3",
             "reconcile": "reconcile", "recorder": "recorder"}   # role -> docs/agents/<name>.md
ROLES = tuple(TEMPLATES)
READER_ROLES = ("claims", "claims-check", "answer")   # the runs that write the claims file (papers.yml)


def target(dandiset: str) -> dict:
    """The paper of the target in a dataset's folder."""
    key = datasets.key_of_folder(dandiset)
    for t in yaml.safe_load((ROOT / "targets" / "pilot.yaml").read_text())["targets"]:
        if datasets.key_of("dandi", t["dandiset"]) == key:
            return {"paper": t["paper"].removeprefix("doi:"), "title": t["title"]}
    # The papers the archive names, corrected by hand in papers/triage.yaml and judged in papers/match/
    # (tools/paper_match.py): a paper triage names comes first, then the primary papers, then the partial ones.
    import paper_match
    for t in datasets.targets():
        if t["key"] == key:
            folder = datasets.folder(key)
            status, papers = paper_match.choose(t, paper_match.triage().get(folder, {}), paper_match.load(folder))
            if not papers:
                raise SystemExit(f"error: no paper matches dataset {datasets.label(key)} ({status}): "
                                 f"see papers/match/{folder}.yaml")
            titles = {paper_match.clean_doi(p["doi"]): p.get("title") for p in t["papers"]}
            p = papers[0]
            return {"paper": p["doi"], "title": p["title"] or titles.get(p["doi"]) or t["name"]}
    raise SystemExit(f"error: dataset {datasets.label(key)} is not in the queue")


def record_key(record: dict) -> str | None:
    ds = record.get("dataset") or {}
    return datasets.key_of(ds["archive"], ds["id"]) if ds.get("archive") and ds.get("id") else None


def records_of(dandiset: str) -> list[Path]:
    """The attempt records on the dataset in a folder, oldest first."""
    key = datasets.key_of_folder(dandiset)
    return sorted(p for p in (ROOT / "attempts").glob("*.yaml")
                  if record_key(yaml.load(p.read_text(), Loader=LOADER) or {}) == key)


def attempt_of(dandiset: str) -> tuple[dict, Path] | None:
    """The latest attempt record on the dataset in a folder, and its entry directory."""
    found = records_of(dandiset)
    if not found:
        return None
    record = yaml.safe_load(found[-1].read_text())
    return record, ROOT / "entries" / record["entry"]


def runner() -> dict:
    """Where this run is going on, for the record's provenance: the platform, and a link to the run."""
    env = os.environ
    if env.get("GITHUB_ACTIONS") == "true" and env.get("GITHUB_RUN_ID"):
        url = f'{env.get("GITHUB_SERVER_URL", "https://github.com")}/{env["GITHUB_REPOSITORY"]}/actions/runs/{env["GITHUB_RUN_ID"]}'
        return {"runner": "GitHub Actions", "runner_url": f', url "{url}"'}
    return {"runner": "local", "runner_url": ""}


def protocol_version() -> str:
    """The protocol version stated at the top of docs/protocol.md."""
    text = (ROOT / "docs" / "protocol.md").read_text()
    return text.split("Version: `", 1)[1].split("`", 1)[0]


def fill(role: str, dandiset: str, model: str, version: str | None = None) -> str:
    """The prompt for a role. An author's ends with its time: the run is stopped at AGENT_TIME_LIMIT_MIN minutes
    (300, the workflow's limit), and the author is told to finish by AGENT_TIME_BUDGET_MIN (255), leaving time to
    write the record and run the entry's checks (docs/protocol.md, "Author", "Time")."""
    prompt = _fill(role, dandiset, model, version)
    if role.startswith("author") or role == "reconcile":
        limit = int(os.environ.get("AGENT_TIME_LIMIT_MIN", "300"))
        budget = int(os.environ.get("AGENT_TIME_BUDGET_MIN", "255"))
        start = datetime.datetime.now(datetime.timezone.utc)
        finish, stop = (start + datetime.timedelta(minutes=m) for m in (budget, limit))
        prompt += (f"\n\nTime: this run started at {start:%H:%M} UTC and is stopped at {stop:%H:%M} UTC, {limit // 60} h "
                   f"{limit % 60:02d} min after it started; work not recorded by then is lost. Check the clock with "
                   f"`date -u` between steps. At {finish:%H:%M} UTC stop analysing and finish, as docs/protocol.md says "
                   f"under \"Author\", \"Time\": record each claim not yet tested as blocked (`too_large` where the "
                   f"computation stopped it, with how far it got), write the record, and run the entry's checks.\n")
    return prompt


def _fill(role: str, dandiset: str, model: str, version: str | None = None) -> str:
    key = datasets.key_of_folder(dandiset)
    if role == "paper-match":
        return paper_match_prompt(dandiset, model)
    # `dandiset` and `folder` name the dataset's folder in the repository; `dataset` is how it is shown.
    details = {"dandiset": dandiset, "folder": dandiset, "dataset": datasets.label(key),
               "archive": datasets.archive_name(key), "access": datasets.access(key),
               "model": model, "date": datetime.date.today().isoformat(), **target(dandiset), **runner()}
    if version:
        details["version_rule"] = (f"Use version {version} of the dataset"
                                   + (" (the draft: say in the notebook header when it was last modified, since a "
                                      "draft can change)" if version == "draft" else "")
                                   + ", and say in the notebook header that this version was asked for.")
    else:
        details["version_rule"] = ("Use a pinned published version of the dataset and record in the notebook "
                                   "header why you chose it.")
    if datasets.split_key(key)[0] in ("local", "remote"):
        # A dataset `encore check` runs on has no versions: its files as they are, named by their fingerprint.
        fingerprint = next((t.get("fingerprint") for t in datasets.targets() if t["key"] == key), None) or "unversioned"
        details["version_rule"] = (f"The dataset has no versions: use its files as they are now, and give "
                                   f"`{fingerprint}`, the fingerprint of its files, wherever the protocol asks for "
                                   f"the version.")
    if role == "author" and attempt_of(dandiset):
        # A repeat attempt. Its author is blind to the earlier attempts (tools/blind.sh hides them), so the prompt
        # names none of them and says only why the dataset is tested again.
        record, entry_dir = attempt_of(dandiset)
        n = int(record["id"].rsplit("-", 1)[1]) + 1
        earlier_protocol = record["provenance"]["agent"]["protocol"]
        if record.get("deprecated"):
            why = ("An earlier attempt was withdrawn, and a reader has since written the claims file again from "
                   "the full text.")
        elif version in (None, record["dataset"].get("version")) and earlier_protocol != protocol_version():
            why = f"The dataset is unchanged; the protocol has changed since, and this attempt applies {protocol_version()}."
        else:
            why = "The dataset has changed since, and this attempt tests what it holds now."
        details.update(entry=entry_dir.name, why=why, next_attempt=f'{record["id"].rsplit("-", 1)[0]}-{n:02d}')
        return (ROOT / "docs" / "agents" / "author-again.md").read_text().format(**details)
    if role == "reconcile":
        found = records_of(dandiset)
        if len(found) < 2:
            raise SystemExit(f"error: {datasets.label(key)} has no earlier attempt to reconcile with")
        record, earlier = (yaml.safe_load(p.read_text()) for p in found[-2:][::-1])
        protocols = (earlier["provenance"]["agent"]["protocol"], record["provenance"]["agent"]["protocol"])
        details.update(attempt=record["id"], earlier=earlier["id"], entry=record["entry"],
                       earlier_entry=earlier["entry"],
                       version=record["dataset"].get("version"), earlier_version=earlier["dataset"].get("version"),
                       protocol_note=(f"The protocol changed from {protocols[0]} to {protocols[1]}: read what changed "
                                      f"in docs/pilot-notes.md, under the headings for the versions after "
                                      f"{protocols[0]}, and say under `protocol` what the changes did."
                                      if protocols[0] != protocols[1] else "Both ran under the same protocol."))
        return (ROOT / "docs" / "agents" / "reconcile.md").read_text().format(**details)
    if role in READER_ROLES:
        existing = sorted((ROOT / "claims" / dandiset).glob("*.yaml"))
        found = attempt_of(dandiset)
        if role != "claims":
            note = ""
        elif found and found[0].get("deprecated"):
            note = (f"A claims file exists, `{existing[0].relative_to(ROOT)}`, from an attempt that is now "
                    f"deprecated: {' '.join(found[0]['deprecated']['reason'].split())} Write it again from the full "
                    f"text. Keep a claim's id where its finding is the same, so the outcomes can be compared, and "
                    f"say in the opening comment what changed and why." if existing else "")
        elif existing:
            note = (f"A claims file exists, `{existing[0].relative_to(ROOT)}`. Bring it up to the current protocol "
                    f"from the full text, keeping ids where a finding is the same, and say what changed.")
        else:
            note = ""
        details.update(existing=note)
        return (ROOT / "docs" / "agents" / f"{TEMPLATES[role]}.md").read_text().format(**details)
    if role != "author":
        found = attempt_of(dandiset)
        if found is None:
            raise SystemExit(f"error: no attempt on {datasets.label(key)} yet; run the author first")
        record, entry_dir = found
        details.update(attempt=record["id"], entry=entry_dir.name, version=record["dataset"].get("version"))
    if role.startswith("author-revise"):
        n = role.rsplit("-", 1)[1]
        report = Path("transcripts") / dandiset / f"verifier-{n}-report.md"
        if not (ROOT / report).is_file():
            raise SystemExit(f"error: {report} does not exist; run verifier-{n} first")
        details.update(round=n, report=report.as_posix())
    return (ROOT / "docs" / "agents" / f"{TEMPLATES[role]}.md").read_text().format(**details)


def paper_match_prompt(folder: str, model: str) -> str:
    """The prompt for the paper match: the papers to judge, and where the dataset's metadata is."""
    import paper_match
    key = datasets.key_of_folder(folder)
    t = paper_match.target_of(folder)
    papers = paper_match.listed(t, paper_match.triage().get(folder, {}))
    lines = "\n".join(f'- doi:{p["doi"]}, "{p["title"] or "(no title given)"}"; '
                      + ("named by a person in papers/triage.yaml: not to judge" if p["named"]
                         else f'relation {p["relation"] or "(none)"}') for p in papers)
    archive, id_ = datasets.split_key(key)
    if archive == "dandi":
        version = t.get("published_version") or "draft"
        metadata = f"`curl -s https://api.dandiarchive.org/api/dandisets/{id_}/versions/{version}/`"
        files = f"`curl -s 'https://api.dandiarchive.org/api/dandisets/{id_}/versions/{version}/assets/?page_size=1000'`, the `path` of each"
    else:
        metadata = f"the dataset's page, {datasets.url(key)}, and its entry in targets/ ({datasets.ARCHIVES[archive]['list']})"
        files = "the file list on its page"
    return (ROOT / "docs" / "agents" / "paper-match.md").read_text().format(
        dataset=datasets.label(key), folder=folder, papers=lines, metadata=metadata, files=files,
        model=model, date=datetime.date.today().isoformat(), **runner())


def package(role: str, dandiset: str, dest: Path) -> None:
    found = attempt_of(dandiset)
    if found is None:
        raise SystemExit(f"error: no attempt on {datasets.label(datasets.key_of_folder(dandiset))}")
    record, entry_dir = found
    executed = ROOT / "executed" / entry_dir.name
    dest.mkdir(parents=True, exist_ok=True)
    if role == "verifier-1":
        source = executed / "handover"
        if not source.is_dir():
            raise SystemExit(f"error: no {source}; run `tools/entry.py run` and `handover` first")
        for f in source.iterdir():
            shutil.copy(f, dest / f.name)
        return
    if role not in ("verifier-2", "verifier-3"):
        raise SystemExit("error: only verifier roles get a package")
    entry = yaml.safe_load((entry_dir / "entry.yaml").read_text())
    for n in entry["notebooks"]:
        shutil.copy(executed / n["path"], dest / n["path"])
    for h in entry.get("helpers", []):
        shutil.copy(entry_dir / h, dest / h)
    if (entry_dir / "README.md").is_file():   # the protocol does not require one
        shutil.copy(entry_dir / "README.md", dest / "README.md")
    for path in (ROOT / "claims" / dandiset).glob("*.yaml"):
        shutil.copy(path, dest / path.name)
    shutil.copy(ROOT / "attempts" / f"{record['id']}.yaml", dest / f"{record['id']}.yaml")
    shutil.copy(ROOT / "transcripts" / dandiset / "verifier-1-report.md", dest / "round-1-report.md")
    if role == "verifier-3":
        shutil.copy(ROOT / "transcripts" / dandiset / "verifier-2-report.md", dest / "round-2-report.md")


def repeat(dandiset: str) -> bool:
    """Whether the attempt in progress on a dataset (its newest record) has an earlier one to reconcile with."""
    return len(records_of(dandiset)) > 1


def proposals(dandiset: str) -> list[str]:
    """The claims of the latest attempt on a dandiset that carry a proposed change of outcome."""
    found = attempt_of(dandiset)
    return [o["claim"] for o in (found[0]["outcomes"] if found else []) if o.get("proposed")]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("command", choices=["prompt", "package", "entry", "proposals", "repeat"])
    parser.add_argument("role", choices=ROLES)
    parser.add_argument("dataset")
    parser.add_argument("dest", nargs="?", type=Path)
    parser.add_argument("--model", default="claude-opus-5-5")
    parser.add_argument("--version", help="the dataset version the author should use, e.g. draft")
    args = parser.parse_args()
    try:
        args.dandiset = datasets.folder(datasets.parse(args.dataset))
    except ValueError as err:
        parser.error(str(err))
    if args.command == "prompt":
        sys.stdout.write(fill(args.role, args.dandiset, args.model, args.version))
    elif args.command == "proposals":
        print("true" if proposals(args.dandiset) else "false")
    elif args.command == "repeat":
        print("true" if repeat(args.dandiset) else "false")
    elif args.command == "entry":
        found = attempt_of(args.dandiset)
        print(found[1].name if found else "")
    else:
        if args.dest is None:
            parser.error("package needs DEST")
        package(args.role, args.dandiset, args.dest)
    return 0


if __name__ == "__main__":
    sys.exit(main())
