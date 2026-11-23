"""Notes from a paper's authors, for its next attempt (docs/author-responses.md, "Notes for the next attempt").

    python tools/author_notes.py add ISSUE      # take a confirmed author response into papers/author-notes/<paper>.yaml
    python tools/author_notes.py show PAPER     # print a paper's notes

An author's response (the "Respond to an attempt" form, an issue labelled `author-response`) can say how something
was computed, link the paper's code, or say where data are. `add` copies that into the paper's notes file, where the
next attempt's author reads it with the paper (docs/protocol.md, "Author", step 1.6). Only a response whose writer
is confirmed (`author-confirmed` or `confirmed`) is taken. The notes are public, as the issue is.

A notes file:

    paper: doi:10.1016/j.neuron.2020.05.023
    notes:
    - issue: https://github.com/encorescience/encore-registry/issues/900
      date: 2026-11-20
      from: A. Author
      role: first author
      orcid: 0000-0002-1825-0097      # when the form gave one
      author: true                     # false for a confirmed writer who is not an author
      claims: [fig2h-theta-power, all] # as the form gave them
      text: The response, as written.
      links: [https://github.com/lab/code]
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import paper_records  # noqa: E402

REPO = "encorescience/encore-registry"
NOTES = ROOT / "papers" / "author-notes"
CONFIRMED = {"author-confirmed": True, "confirmed": False}   # label -> whether the writer is an author


def form(body: str) -> dict[str, str]:
    """The answers of an issue form, by the label of each field."""
    fields, name = {}, None
    for line in (body or "").splitlines():
        if line.startswith("### "):
            name = line[4:].strip()
            fields[name] = ""
        elif name is not None:
            fields[name] += line + "\n"
    return {k: ("" if v.strip() == "_No response_" else v.strip()) for k, v in fields.items()}


def path(key: str) -> Path:
    return NOTES / f"{key}.yaml"


def load(key: str) -> list[dict]:
    """A paper's notes, oldest first; none when it has no notes file."""
    return (yaml.safe_load(path(key).read_text()) or {}).get("notes") or [] if path(key).is_file() else []


def note_of(issue: dict) -> tuple[str, dict]:
    """The paper's key and the note an issue gives. Raises ValueError when it is not a confirmed response to a
    paper the registry lists, or says nothing to take."""
    labels = {lab["name"] for lab in issue.get("labels") or []}
    if "author-response" not in labels:
        raise ValueError("not an author response (no `author-response` label)")
    which = next((lab for lab in CONFIRMED if lab in labels), None)
    if which is None:
        raise ValueError("its writer is not confirmed yet: add `author-confirmed` or `confirmed` first "
                         "(docs/author-responses.md)")
    answers = form(issue.get("body") or "")
    key = paper_records.resolve(re.sub(r"^https?://(dx\.)?doi\.org/", "", answers.get("Paper", "").strip()))
    text = answers.get("Your response", "")
    links = re.findall(r"https?://[^\s)>\]]+", answers.get("Supporting links", ""))
    if not text and not links:
        raise ValueError("the response has no text and no links")
    note = {"issue": issue["url"], "date": issue["createdAt"][:10], "from": answers.get("Your name", ""),
            "role": answers.get("Your role in the paper", ""), "author": CONFIRMED[which]}
    orcid = re.search(r"\d{4}-\d{4}-\d{4}-\d{3}[\dX]", answers.get("ORCID iD", ""))
    if orcid:
        note["orcid"] = orcid.group(0)
    claims = [c for c in re.split(r"[\s,;]+", answers.get("Claims you are responding to", "")) if c]
    if claims:
        note["claims"] = claims
    if text:
        note["text"] = text
    if links:
        note["links"] = links
    return key, note


def add(issue: dict) -> Path:
    key, note = note_of(issue)
    notes = [n for n in load(key) if n.get("issue") != note["issue"]] + [note]   # taken again: replaced
    NOTES.mkdir(parents=True, exist_ok=True)
    body = {"paper": "doi:" + paper_records.doi_of(key), "notes": sorted(notes, key=lambda n: (n["date"], n["issue"]))}
    path(key).write_text(yaml.safe_dump(body, sort_keys=False, allow_unicode=True, width=100))
    return path(key)


def main(argv: list[str]) -> int:
    if len(argv) != 2 or argv[0] not in ("add", "show"):
        print(__doc__, file=sys.stderr)
        return 2
    if argv[0] == "show":
        print(yaml.safe_dump({"notes": load(paper_records.resolve(argv[1]))}, sort_keys=False, allow_unicode=True))
        return 0
    out = subprocess.run(["gh", "issue", "view", argv[1].lstrip("#"), "--repo", REPO, "--json",
                          "url,createdAt,body,labels"], capture_output=True, text=True, check=True).stdout
    try:
        written = add(json.loads(out))
    except ValueError as err:
        print(f"error: {err}", file=sys.stderr)
        return 1
    print(f"wrote {written.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
