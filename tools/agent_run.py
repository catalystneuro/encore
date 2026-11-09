"""Prepare one agent run on a target: its prompt, and for a verifier its materials.

    python tools/agent_run.py prompt  ROLE PAPER [--model M] > prompt.md
    python tools/agent_run.py package ROLE PAPER DEST
    python tools/agent_run.py entry   ROLE PAPER          # the entry directory's name, if any
    python tools/agent_run.py proposals ROLE PAPER        # "true" if the attempt has proposed changes
    python tools/agent_run.py repeat ROLE PAPER           # "true" if the attempt in progress has one before it

PAPER is a paper key (tingley-2021; docs/paper-first.md), a DOI, or a dataset listed for a paper in
papers/datasets/. The paper match is the one role on a dataset: its target is written any way
tools/datasets.py accepts (000003, DANDI:000003, ebrains:<id>).

ROLE is paper-match, which judges whether each paper the archive names is the paper behind the data
(docs/pipeline.md, step 1; papers.yml runs it, with claims, claims-check and answer), or one of
author, verifier-1, author-revise-1, verifier-2, author-revise-2, the order in which an attempt goes through docs/protocol.md, and verifier-3 and
author-revise-3, the third round that settles changes proposed after the second. A repeat attempt
then has reconcile, which compares it with the attempt before it: until then its runs are blind to
earlier attempts (tools/blind.sh). A last role, recorder, writes the finished attempt's notes in docs/pilot-notes/<attempt>.md. The prompts are
docs/agents/<role>.md with the target's details filled in. A run's transcript
and final report are kept as transcripts/<paper key>/<role>.md and
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
import paper_records  # noqa: E402

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


def title_of(key: str) -> str:
    """The paper's title: from papers/datasets/<key>.yaml, else the archive's list of its datasets' papers."""
    body = paper_records.listed().get(key) or {}
    if body.get("title"):
        return body["title"]
    doi = paper_records.doi_of(key)
    for t in datasets.targets():
        for p in t.get("papers") or []:
            if paper_records.paper_keys.doi_of(p.get("doi") or "") == doi and p.get("title"):
                return p["title"]
    return key


def target(key: str) -> dict:
    """The paper behind a paper key: its DOI and title."""
    return {"paper": paper_records.doi_of(key), "title": title_of(key)}


def records_of(key: str) -> list[Path]:
    """The paper's attempt records, oldest first."""
    return paper_records.attempt_paths(key)


def attempt_of(key: str) -> tuple[dict, Path] | None:
    """The paper's latest attempt record, and its entry directory."""
    found = records_of(key)
    if not found:
        return None
    record = yaml.safe_load(found[-1].read_text())
    return record, ROOT / "entries" / record["entry"]


def data_details(key: str) -> dict:
    """What a prompt says about the paper's datasets: `dataset` (how they are named in a sentence), `datasets`
    (a list, one line each, with archive and how to read it), `archive` and `access`."""
    listed = paper_records.datasets_of(key)
    usable = [d for d in listed if d.get("available", True)]
    missing = [d for d in listed if not d.get("available", True)]
    if not usable:
        raise SystemExit(f"error: paper {key} lists no dataset that can be used (papers/datasets/{key}.yaml)")
    labels = [datasets.label(d["key"]) for d in usable]
    lines = []
    for d in usable:
        lines.append(f'- {datasets.label(d["key"])} on {datasets.archive_name(d["key"])}'
                     + (" (data the paper reuses)" if d.get("relation") == "reuses" else "")
                     + f'. {datasets.access(d["key"])}')
    for d in missing:
        lines.append(f'- {datasets.label(d["key"]) if d.get("id") else d.get("name", "a dataset")}: not available '
                     f'({d.get("why", "no reason given")}). Claims that need it are blocked with '
                     f'`blocked_by: missing-dataset` (docs/protocol.md).')
    if len(usable) == 1:
        sentence = labels[0]
        several = reader = ""
    else:
        folders = ", ".join(f'`{d["folder"]}`' for d in usable)
        reader = (f" The paper's data are in {len(usable)} datasets ({folders}): give each claim `datasets:`, the "
                  f"folder names of the ones it rests on (docs/protocol.md, \"Reader\").")
        sentence = f'{", ".join(labels[:-1])} and {labels[-1]}'
        several = (f" The paper's data are in {len(usable)} datasets: use every one of them that a claim needs, "
                   f"as each claim's `datasets` says.")
    return {"dataset": sentence, "datasets": "\n".join(lines), "several": several, "reader_several": reader,
            "archive": ", ".join(sorted({datasets.archive_name(d["key"]) for d in usable})),
            "access": " ".join(dict.fromkeys(datasets.access(d["key"]) for d in usable))}


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


def fill(role: str, target_name: str, model: str, version: str | None = None) -> str:
    """The prompt for a role. An author's ends with its time: the run is stopped at AGENT_TIME_LIMIT_MIN minutes
    (300, the workflow's limit), and the author is told to finish by AGENT_TIME_BUDGET_MIN (255), leaving time to
    write the record and run the entry's checks (docs/protocol.md, "Author", "Time")."""
    prompt = _fill(role, target_name, model, version)
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


def _fill(role: str, target_name: str, model: str, version: str | None = None) -> str:
    if role == "paper-match":
        return paper_match_prompt(datasets.folder(datasets.parse(target_name)), model)
    key = paper_records.resolve(target_name)
    # `key` and `folder` name the paper in the repository (its records' paths); `dataset` names its datasets.
    details = {"key": key, "folder": key, "claims": paper_records.claims_file(key).relative_to(ROOT).as_posix(),
               "questions": paper_records.questions_file(key).relative_to(ROOT).as_posix(),
               "model": model, "date": datetime.date.today().isoformat(),
               **data_details(key), **target(key), **runner()}
    first = paper_records.datasets_of(key, available_only=True)[0]
    if version:
        details["version_rule"] = (f"Use version {version} of {datasets.label(first['key'])}"
                                   + (" (the draft: say in the notebook header when it was last modified, since a "
                                      "draft can change)" if version == "draft" else "")
                                   + ", and say in the notebook header that this version was asked for.")
    else:
        details["version_rule"] = ("Use a pinned published version of each dataset and record in the notebook "
                                   "header why you chose it.")
    for d in paper_records.datasets_of(key, available_only=True):
        if datasets.split_key(d["key"])[0] in ("local", "remote"):
            # A dataset `encore check` runs on has no versions: its files as they are, named by their fingerprint.
            fingerprint = next((t.get("fingerprint") for t in datasets.targets() if t["key"] == d["key"]),
                               None) or "unversioned"
            details["version_rule"] = (f"The dataset has no versions: use its files as they are now, and give "
                                       f"`{fingerprint}`, the fingerprint of its files, wherever the protocol asks "
                                       f"for the version.")
    if role == "author" and attempt_of(key):
        # A repeat attempt. Its author is blind to the earlier attempts (tools/blind.sh hides them), so the prompt
        # names none of them and says only why the paper is tested again.
        record, entry_dir = attempt_of(key)
        n = int(record["id"].rsplit("-", 1)[1]) + 1
        earlier_protocol = record["provenance"]["agent"]["protocol"]
        earlier_keys = set(paper_records.record_dataset_keys(record))
        now_keys = {d["key"] for d in paper_records.datasets_of(key, available_only=True)}
        earlier_version = (paper_records.record_datasets(record) or [{}])[0].get("version")
        if record.get("deprecated"):
            why = ("An earlier attempt was withdrawn, and a reader has since written the claims file again from "
                   "the full text.")
        elif now_keys - earlier_keys:
            why = ("The paper has datasets the earlier attempts did not test together; this attempt tests the "
                   "claims on all of them.")
        elif version in (None, earlier_version) and earlier_protocol != protocol_version():
            why = f"The data are unchanged; the protocol has changed since, and this attempt applies {protocol_version()}."
        else:
            why = "The data have changed since, and this attempt tests what they hold now."
        details.update(entry=key, why=why, next_attempt=f"{key}-{n:02d}")
        return (ROOT / "docs" / "agents" / "author-again.md").read_text().format(**details)
    if role == "reconcile":
        found = records_of(key)
        if len(found) < 2:
            raise SystemExit(f"error: {key} has no earlier attempt to reconcile with")
        record, earlier = (yaml.safe_load(p.read_text()) for p in found[-2:][::-1])
        protocols = (earlier["provenance"]["agent"]["protocol"], record["provenance"]["agent"]["protocol"])
        details.update(attempt=record["id"], earlier=earlier["id"], entry=record["entry"],
                       earlier_entry=earlier["entry"],
                       version=", ".join(str(d.get("version")) for d in paper_records.record_datasets(record)),
                       earlier_version=", ".join(str(d.get("version")) for d in paper_records.record_datasets(earlier)),
                       protocol_note=(f"The protocol changed from {protocols[0]} to {protocols[1]}: read what changed "
                                      f"in docs/pilot-notes.md, under the headings for the versions after "
                                      f"{protocols[0]}, and say under `protocol` what the changes did."
                                      if protocols[0] != protocols[1] else "Both ran under the same protocol."))
        return (ROOT / "docs" / "agents" / "reconcile.md").read_text().format(**details)
    if role in READER_ROLES:
        existing = paper_records.claims_files(key)
        found = attempt_of(key)
        if role != "claims":
            note = ""
        elif existing and paper_records.claims_file(key) not in existing:
            listed = ", ".join(f"`{p.relative_to(ROOT)}`" for p in existing)
            note = (f"Claims were read for this paper before, one file per dataset: {listed}. Write one claims file "
                    f"for the paper, `{details['claims']}`, across all its datasets, from the full text; reuse those "
                    f"files' ids where a finding is the same, so the outcomes can be compared.")
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
        found = attempt_of(key)
        if found is None:
            raise SystemExit(f"error: no attempt on {key} yet; run the author first")
        record, entry_dir = found
        details.update(attempt=record["id"], entry=entry_dir.name,
                       version=", ".join(f'{datasets.label(datasets.key_of(d["archive"], str(d["id"])))} version '
                                         f'{d.get("version")}' for d in paper_records.record_datasets(record)))
    if role.startswith("author-revise"):
        n = role.rsplit("-", 1)[1]
        report = Path("transcripts") / key / f"verifier-{n}-report.md"
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


def package(role: str, key: str, dest: Path) -> None:
    found = attempt_of(key)
    if found is None:
        raise SystemExit(f"error: no attempt on {key}")
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
    for path in paper_records.claims_files(key)[:1]:
        shutil.copy(path, dest / path.name)
    shutil.copy(ROOT / "attempts" / f"{record['id']}.yaml", dest / f"{record['id']}.yaml")
    shutil.copy(ROOT / "transcripts" / key / "verifier-1-report.md", dest / "round-1-report.md")
    if role == "verifier-3":
        shutil.copy(ROOT / "transcripts" / key / "verifier-2-report.md", dest / "round-2-report.md")


def repeat(key: str) -> bool:
    """Whether the attempt in progress on a paper (its newest record) has an earlier one to reconcile with."""
    return len(records_of(key)) > 1


def proposals(key: str) -> list[str]:
    """The claims of the paper's latest attempt that carry a proposed change of outcome."""
    found = attempt_of(key)
    return [o["claim"] for o in (found[0]["outcomes"] if found else []) if o.get("proposed")]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("command", choices=["prompt", "package", "entry", "proposals", "repeat"])
    parser.add_argument("role", choices=ROLES)
    parser.add_argument("target", help="a paper key (a dataset, for paper-match)")
    parser.add_argument("dest", nargs="?", type=Path)
    parser.add_argument("--model", default="claude-opus-5-5")
    parser.add_argument("--version", help="the dataset version the author should use, e.g. draft")
    args = parser.parse_args()
    if args.command == "prompt":
        sys.stdout.write(fill(args.role, args.target, args.model, args.version))
        return 0
    try:
        args.key = paper_records.resolve(args.target)
    except ValueError as err:
        parser.error(str(err))
    if args.command == "proposals":
        print("true" if proposals(args.key) else "false")
    elif args.command == "repeat":
        print("true" if repeat(args.key) else "false")
    elif args.command == "entry":
        found = attempt_of(args.key)
        print(found[1].name if found else "")
    else:
        if args.dest is None:
            parser.error("package needs DEST")
        package(args.role, args.key, args.dest)
    return 0


if __name__ == "__main__":
    sys.exit(main())
