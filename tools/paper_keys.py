"""Paper keys: the short name each paper's records are filed under (docs/paper-first.md).

    python tools/paper_keys.py            # add keys for papers that have none, to papers/keys.yaml
    python tools/paper_keys.py --check    # exit 1 if a paper with records has no key

A key is the first author's surname and the year, lower case ASCII: `tingley-2021`. When two
papers would share one, the paper that already has it keeps it and the other takes the first
distinctive word of its title: `daume-2024-hippocampal`. Keys are assigned once and kept; a key in
papers/keys.yaml is never recomputed, so records and URLs filed under it stay where they are.

Where the surname and year come from, in order: the name of the paper's entry
(`000233-tingley-2021`), the first line of its claims file ("Claims for Tingley, ... (2021)"), and
Crossref.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
KEYS = ROOT / "papers" / "keys.yaml"
HEADER = """\
# The key each paper's records are filed under (tools/paper_keys.py, docs/paper-first.md).
# Assigned once and never recomputed: change a key only together with every path that uses it.
"""
# A dataset folder at the start of an entry name: 000233, crcns-hc-14, ebrains-q0fg-1x8, dryad-bvq83bkk9...
ENTRY = re.compile(r"^(?:\d{6}|crcns-[a-z]+-\d+|[a-z]+-[a-z0-9.]+(?:-[a-z0-9]+)*?)-([a-z]+(?:-[a-z]+)*-\d{4})$")
CLAIMS_FOR = re.compile(r"^# Claims for (?:the )?(.+?)(?:,| et al| & | and |\s*\().*?\((\d{4})\)", re.S)
STOP = {"a", "an", "the", "of", "in", "on", "and", "for", "to", "by", "with", "from", "during", "at",
        "is", "are", "its", "their", "into", "via", "between", "across", "after", "before", "under"}


def ascii_slug(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def doi_of(paper: str) -> str:
    return paper.removeprefix("doi:").lower()


def load(path: Path):
    return yaml.safe_load(path.read_text())


def crossref(doi: str) -> dict:
    req = urllib.request.Request(f"https://api.crossref.org/works/{doi}",
                                 headers={"User-Agent": "encore-paper-keys/1"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)["message"]


def papers_with_records() -> dict[str, dict]:
    """Every paper some record names: its DOI → the surname, year and title found, and when its
    first record was made (to decide which of two clashing papers keeps the plain key)."""
    found: dict[str, dict] = {}

    def note(doi: str, date: str, **kw):
        p = found.setdefault(doi, {"date": date})
        p["date"] = min(p["date"], date)
        for k, v in kw.items():
            p.setdefault(k, v)

    for path in sorted((ROOT / "attempts").glob("*.yaml")):
        a = load(path)
        doi = doi_of(a["paper"])
        m = ENTRY.match(a.get("entry") or "")
        note(doi, str(a["date"]), **({"name": m.group(1)} if m else {}))
    for path in sorted((ROOT / "entries").glob("*/entry.yaml")):
        en = load(path)
        dois = [doi_of(r["id"]) for r in en.get("related") or [] if r.get("relation") == "reproduces"]
        m = ENTRY.match(en["name"])
        for doi in dois:
            note(doi, "9999", title=en.get("title"), **({"name": m.group(1)} if m else {}))
    for path in sorted((ROOT / "claims").glob("*/*.yaml")):
        text = path.read_text()
        data = yaml.safe_load(text)
        doi = doi_of(data["paper"])
        # Only the opening paragraph names the paper; a year further down may be a cited work's.
        m = CLAIMS_FOR.match(text.split("\n#\n", 1)[0])
        date = re.search(r"\b(20\d\d-\d\d-\d\d)\b", text[:2000])
        kw = {"surname": m.group(1).strip(), "year": m.group(2)} if m else {}
        note(doi, date.group(1) if date else "9999", **kw)
    return found


def base_key(doi: str, p: dict) -> tuple[str, str]:
    """The surname-year key and the title, from records if they have them, else Crossref."""
    if "name" in p:
        key = p["name"]
    elif "surname" in p:
        key = f'{ascii_slug(p["surname"])}-{p["year"]}'
    else:
        key = None
    title = p.get("title") or ""
    if key is None or not title:
        try:
            msg = crossref(doi)
        except Exception as exc:  # noqa: BLE001 - reported, not fatal
            if key is None:
                raise SystemExit(f"{doi}: no surname and year in its records, and Crossref failed: {exc}")
            msg = {}
        if key is None:
            author = (msg.get("author") or [{}])[0]
            surname = author.get("family") or author.get("name") or "anon"
            year = ((msg.get("issued") or {}).get("date-parts") or [[None]])[0][0]
            key = f"{ascii_slug(surname.split()[-1])}-{year}"
        title = title or " ".join(msg.get("title") or [])
    return key, title


def distinguish(key: str, title: str, taken: set[str]) -> str:
    for word in ascii_slug(re.sub(r"\(.*?\)", " ", title)).split("-"):
        if word in STOP or len(word) < 4 or word.isdigit():
            continue
        if f"{key}-{word}" not in taken:
            return f"{key}-{word}"
    n = 2
    while f"{key}-{n}" in taken:
        n += 1
    return f"{key}-{n}"


def assign(keys: dict[str, str], found: dict[str, dict]) -> dict[str, str]:
    keys = dict(keys)
    taken = set(keys.values())
    for doi, p in sorted(found.items(), key=lambda kv: (kv[1]["date"], kv[0])):
        if doi in keys:
            continue
        key, title = base_key(doi, p)
        if key in taken:
            key = distinguish(key, title, taken)
        keys[doi] = key
        taken.add(key)
    return keys


def read_keys() -> dict[str, str]:
    return (load(KEYS) or {}).get("keys", {}) if KEYS.is_file() else {}


def key_of(paper: str) -> str:
    """The key of a paper (`doi:10...` or `10...`); KeyError if it has none yet."""
    return read_keys()[doi_of(paper)]


def write_keys(keys: dict[str, str]) -> None:
    body = yaml.safe_dump({"schema_version": 1, "keys": dict(sorted(keys.items()))},
                          sort_keys=False, allow_unicode=True, width=100)
    KEYS.write_text(HEADER + body)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    keys = read_keys()
    found = papers_with_records()
    missing = sorted(set(found) - set(keys))
    if args.check:
        for doi in missing:
            print(f"no key: {doi}", file=sys.stderr)
        return 1 if missing else 0
    new = assign(keys, found)
    write_keys(new)
    print(f"{len(new)} keys, {len(new) - len(keys)} new")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
