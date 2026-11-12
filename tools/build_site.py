"""Build the public dashboard: a static site from the registry's own files.

    python tools/build_site.py [--output site]
    python tools/build_site.py --demo 150 --output /tmp/demo-site

Reads targets/dandisets.json, targets/pilot.yaml, claims/, attempts/,
entries/ and transcripts/, and writes:

    index.html                    overview: numbers, breakdowns, latest attempts
    datasets/index.html           every target, filterable and paginated
    datasets/<archive>/<id>/      one static page per attempted dataset, and one per earlier attempt
    dandisets/<id>/               redirects to the dataset's page, for links made before
    data/dandisets.json           rows for the list page
    api/dandiset/<id>.json        one dandiset's results, for other sites
    registry.json                 everything, as before
    assets/                       app.css, list.js and progress.js from tools/site_assets/

If <output>/notebooks/<entry>/<notebook>.html exists (the executed notebooks
CI keeps on the `executed` branch), pages link to it.

The list pages are rendered in the browser by assets/list.js from the JSON
rows; filters, search, sort and page are kept in the URL, so every view is a
link. Dataset pages are complete HTML and need no JavaScript.

The trust tier of an attempt is derived from its verifications: the latest
verification decides, and it counts only if it agrees with every outcome.

`--demo N` builds from N made-up attempts on real targets, to see and test the
site at scale. A demo build says so on every page; never publish one.

Requires `pyyaml`.
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import html
import json
import random
import re
import shutil
import sys
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
ASSETS = Path(__file__).resolve().parent / "site_assets"
REPO_URL = "https://github.com/catalystneuro/encore"
CN_URL = "https://www.catalystneuro.com"
# Encore Science is the project: the `encore` tool (docs/encore.md) and this site, the Encore registry.
SITE_NAME = "Encore Science"
ENCORE_DOCS = REPO_URL + "/blob/main/docs/encore.md"
SITE_URL = "https://encorescience.org/"
SITE_DESCRIPTION = ("AI agents try to reproduce the key findings of papers from their open data, and record every "
                    "outcome and what they find about the data.")

sys.path.insert(0, str(Path(__file__).resolve().parent))
from datasets import ARCHIVES, archive_name, key_of, split_key, targets as all_targets  # noqa: E402
import paper_records  # noqa: E402
from datasets import folder as dir_of, key_of_folder as key_of_dir, label as dataset_label, url as archive_url  # noqa: E402,F401
import paper_match  # noqa: E402


def page_of(key: str) -> str:
    """A dataset's page on the site: datasets/<archive>/<id>/."""
    archive, id_ = split_key(key)
    return f"datasets/{archive}/{id_}/"


# GitHub's mark (Octicons, mark-github), drawn in the text colour.
# The site's mark, drawn like the favicon: a loop that comes back round, a result run again, with a tick inside it.
# The loop takes the text colour and the tick the brand colour, so it suits both themes.
ENCORE_MARK = ('<svg class="mark" viewBox="0 0 32 32" aria-hidden="true" focusable="false">'
               '<path d="M21.6 8.3A9.5 9.5 0 1 0 25.5 16" fill="none" stroke="currentColor" stroke-width="2.8" '
               'stroke-linecap="round"/><path d="M18.9 10.7 24.1 5.5 24.7 11.3z" fill="currentColor" '
               'stroke="currentColor" stroke-width="1.2" stroke-linejoin="round"/><path class="tick" '
               'd="M11.3 16.3l3.3 3.3 5.9-6.8" fill="none" stroke-width="3" stroke-linecap="round" '
               'stroke-linejoin="round"/></svg>')
GITHUB_MARK = ('<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M8 0c4.42 0 8 3.58 8 8a8.013 '
               '8.013 0 0 1-5.45 7.59c-.4.08-.55-.17-.55-.38 0-.27.01-1.13.01-2.2 0-.75-.25-1.23-.54-1.48 1.78-.2 '
               '3.65-.88 3.65-3.95 0-.88-.31-1.59-.82-2.15.08-.2.36-1.02-.08-2.12 0 0-.67-.22-2.2.82-.64-.18-1.32-.27-2'
               '-.27-.68 0-1.36.09-2 .27-1.53-1.03-2.2-.82-2.2-.82-.44 1.1-.16 1.92-.08 2.12-.51.56-.82 1.28-.82 2.15 0 '
               '3.06 1.86 3.75 3.64 3.95-.23.2-.44.55-.51 1.07-.46.21-1.61.55-2.33-.66-.15-.24-.6-.83-1.23-.82-.67.01'
               '-.27.38.01.53.34.19.73.9.82 1.13.16.45.68 1.31 2.69.94 0 .67.01 1.3.01 1.49 0 .21-.15.45-.55.38A7.995 '
               '7.995 0 0 1 0 8c0-4.42 3.58-8 8-8Z"/></svg>')

OUTCOMES = {  # key: (label, css class, icon)
    "reproduced": ("Reproduced", "good", "✓"),
    "partially_reproduced": ("Partially reproduced", "warning", "◐"),
    "not_reproduced": ("Not reproduced", "unresolved", "?"),
    "blocked": ("Blocked", "blocked", "⊘"),
}
BLOCKED_BY = {
    "data_missing": "Data missing from the dataset",
    "metadata_insufficient": "Metadata insufficient",
    "methods_underspecified": "Methods underspecified",
    "data_unreadable": "Data unreadable",
    "too_large": "Too large to analyse",
    "not_runnable": "Method cannot be run here",
    "other": "Other",
}
TIERS = {
    "runs": "Runs in CI, not yet verified",
    "agent_verified": "Verified by an independent agent",
    "human_verified": "Verified by a person",
    "author_endorsed": "Endorsed by a paper author",
}
FINDING_KINDS = {
    "metadata_error": "Metadata error",
    "data_missing": "Data missing",
    "identifier_missing": "Identifier missing",
    "metadata_insufficient": "Description missing",
    "selection_undocumented": "Selection not documented",
    "methods_unavailable": "Methods not available",
    "format_error": "File format error",
    "code_mismatch": "Published code disagrees",
    "paper_inconsistency": "Paper inconsistent",
    "other": "Other",
}
# What a finding is about when its record does not say (schemas/attempt.schema.json, `about`): the paper for these
# kinds, the data for the others. A finding about the data belongs to its dataset, one about the paper to the paper.
ABOUT_PAPER = {"methods_unavailable", "code_mismatch", "paper_inconsistency"}
STATUS = {"attempted": "Attempted", "pilot": "In the pilot", "open": "Not yet attempted",
          "no_match": "No matching paper"}
VERIFICATION_TIER = {"agent": "agent_verified", "person": "human_verified",
                     "paper_author": "author_endorsed"}
CAUTION = "A failure to reproduce is not a finding that the paper is wrong."


def load_yaml(path: Path):
    # libyaml when PyYAML has it: the site reads every claims file and record, and the pure-Python parser
    # takes most of the build.
    return yaml.load(path.read_text(), Loader=getattr(yaml, "CSafeLoader", yaml.SafeLoader))


def tier_of(attempt: dict) -> str:
    verifications = attempt.get("verifications") or []
    if not verifications:
        return "runs"
    latest = verifications[-1]
    claims = {o["claim"] for o in attempt["outcomes"]}
    agreed = {r["claim"] for r in latest.get("results", []) if r.get("agrees")}
    return VERIFICATION_TIER.get(latest["kind"], "runs") if claims <= agreed else "runs"


def squash(text) -> str:
    return " ".join((text or "").split())


def human_size(gb: float) -> str:
    """38464.5 -> '38.5 TB'; 0.05 -> '50 MB'."""
    value, unit = (gb / 1000, "TB") if gb >= 1000 else (gb, "GB") if gb >= 1 else (gb * 1000, "MB")
    return f"{value:.0f} {unit}" if value >= 100 else f"{value:.1f} {unit}"


def human_count(n: int, noun: str) -> str:
    """40982 -> '41k files'; 1 -> '1 file'."""
    text = f"{n / 1e6:.1f}M" if n >= 1e6 else f"{round(n / 1e3)}k" if n >= 1e4 else f"{n:,}"
    return f"{text} {noun}{'' if n == 1 else 's'}"


def short_species(name: str) -> str:
    return (name or "").split(" - ")[-1].strip()



def asset(name: str) -> str:
    """An asset's path with a hash of its contents, so that a browser never pairs a new page with a cached old
    stylesheet or script (GitHub Pages lets them be cached for ten minutes)."""
    digest = hashlib.sha256((ASSETS / name).read_bytes()).hexdigest()[:10]
    return f"assets/{name}?v={digest}"

# --- collecting ---------------------------------------------------------------

COLAB_URL = "https://colab.research.google.com/github/catalystneuro/encore/blob/colab/entries"


def environment_of(entry_dir: Path) -> dict:
    """An entry's environment, for its page: the Python version it runs on and how many packages its lock pins."""
    # As tools/entry.py's python_of, without importing it: it needs nbformat, which the site's workflows do not install.
    lock = entry_dir / "requirements.lock.txt"
    text = lock.read_text() if lock.is_file() else ""
    pinned = sum(1 for line in text.splitlines() if re.match(r"^[A-Za-z0-9]", line))
    entry = load_yaml(entry_dir / "entry.yaml") or {}
    locked_for = re.search(r"--python-version\s+(\d+\.\d+)", text[:2000])
    python = str(entry.get("python") or (locked_for.group(1) if locked_for else "3.13"))
    return {"python": python, "pinned": pinned, "hashed": "--hash=" in text}


def record_files(kind: str) -> list[tuple[Path, list[str]]]:
    """A kind of record (claims, questions) with the datasets each is about: a paper's own file,
    <kind>/<paper>.yaml, is about all the paper's datasets; one from before the cutover to paper-first records,
    <kind>/<paper>/<folder>.yaml, about that folder's dataset."""
    out = []
    for path in sorted((ROOT / kind).glob("*.yaml")):
        out.append((path, [d["key"] for d in paper_records.datasets_of(path.stem)]))
    for path in sorted((ROOT / kind).glob("*/*.yaml")):
        out.append((path, [key_of_dir(path.stem)]))
    return out


def transcript_folders() -> list[tuple[Path, list[str]]]:
    """Each transcripts folder with the datasets it is about: transcripts/<paper>/ for all the paper's datasets,
    transcripts/<paper>/<folder>/ for one."""
    out = []
    for d in sorted((ROOT / "transcripts").glob("*")):
        if not d.is_dir() or d.name == "match":
            continue
        out.append((d, [x["key"] for x in paper_records.datasets_of(d.name)]))
        for sub in sorted(d.glob("*")):
            if sub.is_dir() and not sub.name.startswith("attempt-"):
                out.append((sub, [key_of_dir(sub.name)]))
    return out


def attempt_rows() -> list[tuple[Path, dict, dict]]:
    """Each attempt record once for each dataset it used: the site's pages are by dataset."""
    out = []
    for path in sorted((ROOT / "attempts").glob("*.yaml")):
        a = load_yaml(path)
        for used in paper_records.record_datasets(a):
            out.append((path, a, used))
    return out


def paper_claims() -> dict[str, list[dict]]:
    """Each paper's claims files, by paper key, with all their claims: claims/<paper>.yaml, and from before the
    cutover to paper-first records claims/<paper>/<folder>.yaml."""
    out: dict = {}
    for path in sorted((ROOT / "claims").glob("*.yaml")) + sorted((ROOT / "claims").glob("*/*.yaml")):
        body = load_yaml(path) or {}
        key = path.stem if path.parent.name == "claims" else path.parent.name
        last = (body.get("checks") or [None])[-1]
        out.setdefault(key, []).append({
            "path": str(path.relative_to(ROOT)), "paper": str(body.get("paper", "")).removeprefix("doi:"),
            "check": None if last is None else {"ready": bool(last.get("ready")), "date": str(last.get("date"))},
            "claims": [{k: squash(c.get(k) or "") for k in ("id", "statement", "source", "quote", "criterion")}
                       for c in body.get("claims") or []]})
    return out


def collect(executed: Path | None = None) -> dict:
    queue = json.loads((ROOT / "targets" / "dandisets.json").read_text())
    pilot = {key_of("dandi", t["dandiset"]) for t in load_yaml(ROOT / "targets" / "pilot.yaml")["targets"]}
    claims, claim_files = {}, {}
    for path, keys in record_files("claims"):
        data = load_yaml(path)
        claims[path] = {c["id"]: c for c in data["claims"]}
        last = (data.get("checks") or [None])[-1]
        for key in keys:
            claim_files.setdefault(key, []).append({
            "path": str(path.relative_to(ROOT)), "paper": str(data["paper"]).removeprefix("doi:"),
            "check": None if last is None else {"ready": bool(last.get("ready")), "date": str(last.get("date"))},
            "claims": [{k: squash(c.get(k) or "") for k in ("id", "statement", "source", "quote", "criterion")}
                       for c in data["claims"]
                       if not c.get("datasets") or dir_of(key) in c["datasets"]]})
    entries = {}
    for path in sorted((ROOT / "entries").glob("*/entry.yaml")):
        data = load_yaml(path)
        entries[data["name"]] = data
    titles = {p["doi"]: p["title"] for t in queue["targets"] for p in t["papers"]}

    def notebooks_of(entry: dict) -> list[dict]:
        out = []
        for n in entry["notebooks"]:
            page = f'notebooks/{entry["name"]}/{Path(n["path"]).stem}.html'
            out.append({"path": n["path"], "title": n.get("title") or n["path"],
                        "executed": page if executed and (executed / entry["name"] / Path(page).name).is_file()
                        else None})
        return out

    attempts = []
    for path, a, used in attempt_rows():
        key = key_of(used["archive"], str(used["id"]))
        claims_path = paper_records.claims_for_attempt(a)
        known = claims.get(claims_path, {}) if claims_path else {}
        entry = entries.get(a.get("entry"))
        verifications = a.get("verifications") or []
        disagreed = {r["claim"] for v in verifications for r in v["results"] if not r.get("agrees")}
        attempts.append({
            "id": a["id"],
            "dataset": {k: str(v) for k, v in used.items()},
            "datasets": [key_of(d["archive"], str(d["id"])) for d in paper_records.record_datasets(a)],
            "missing_datasets": [{k: squash(str(v)) for k, v in m.items()} for m in a.get("missing_datasets") or []],
            "key": key, "label": dataset_label(key),
            "dataset_version": used.get("version"),
            "paper": a["paper"].removeprefix("doi:"),
            "paper_title": titles.get(a["paper"].removeprefix("doi:").lower()),
            "date": str(a["date"]),
            "kind": a["provenance"]["kind"],
            "accountable": a["provenance"]["accountable"]["name"],
            "agent": a["provenance"].get("agent"),
            "runner": a["provenance"].get("runner"),
            "tier": tier_of(a),
            "deprecated": squash((a.get("deprecated") or {}).get("reason")),
            "deprecated_on": str((a.get("deprecated") or {}).get("date") or "") or None,
            "entry": a.get("entry"),
            "entry_title": entry["title"] if entry else None,
            # The recorder's summary for the site (docs/agents/recorder.md, step 2), when the attempt has one.
            "summary": squash((ROOT / "summaries" / f"{a['id']}.md").read_text())
                       if (ROOT / "summaries" / f"{a['id']}.md").is_file() else None,
            "description": squash(entry.get("description")) if entry else None,
            "notebooks": notebooks_of(entry) if entry else [],
            "outcomes": [{
                "claim": o["claim"],
                "statement": squash(known.get(o["claim"], {}).get("statement", o["claim"])),
                "source": known.get(o["claim"], {}).get("source"),
                "quote": squash(known.get(o["claim"], {}).get("quote")),
                "statistics": known.get(o["claim"], {}).get("statistics") or [],
                "kind": known.get(o["claim"], {}).get("kind", "finding"),
                "inferred": squash(known.get(o["claim"], {}).get("inferred")),
                "outcome": o["outcome"],
                "blocked_by": o.get("blocked_by"),
                "notebook": o.get("notebook"),
                "notes": squash(o.get("notes")),
                "deviations": [squash(d) for d in o.get("deviations") or []],
                "assumed": bool(o.get("assumed")),
                "disagreed": o["claim"] in disagreed,
                "data": known.get(o["claim"], {}).get("data", "dataset"),
                "where": known.get(o["claim"], {}).get("where"),
                "proposed": o.get("proposed"),
            } for o in a["outcomes"]],
            # Every finding of the record, numbered as the record has them (a reconciliation names them by number);
            # split after reconcile() into those about the data (`findings`) and about the paper (`paper_notes`).
            "findings": [{"kind": f["kind"], "statement": squash(f["statement"]), "found": f.get("found"),
                          "status": None, "n": n,
                          "about": f.get("about") or ("paper" if f["kind"] in ABOUT_PAPER else "data"),
                          "datasets": [str(x) for x in f.get("datasets") or []]}
                         for n, f in enumerate(a.get("findings") or [], 1)],
            "reconciliation": a.get("reconciliation"),
            "verifications": [{
                "date": str(v["date"]), "kind": v["kind"], "by": squash(v.get("by")),
                "reviewed": squash(v.get("reviewed")),
                "agreed": sum(1 for r in v["results"] if r.get("agrees")),
                "of": len(v["results"]),
                "disagreements": [{"claim": r["claim"], "outcome": r.get("outcome"),
                                   "reason": squash(r.get("reason"))}
                                  for r in v["results"] if not r.get("agrees")],
            } for v in verifications],
        })

    reconcile(attempts)
    # Findings about the data belong to a dataset: `findings` is from here on those about this row's dataset (a record
    # is a row for each dataset it used; a finding that names its datasets is on those rows only). Those about the
    # paper are `paper_notes`, for the paper's page.
    for a in attempts:
        every = a["findings"]
        a["paper_notes"] = [f for f in every if f["about"] == "paper"]
        a["findings"] = [f for f in every if f["about"] == "data"
                         and (not f["datasets"] or dir_of(a["key"]) in f["datasets"])]
    attempted = {a["key"] for a in attempts}
    targets = []
    fixes = paper_match.triage()
    for t in all_targets():
        key = t["key"]
        # The paper an attempt uses (papers/triage.yaml, papers/match/), else the archive's first publication.
        match, chosen = paper_match.choose(t, fixes.get(t["folder"], {}), paper_match.load(t["folder"]))
        titles = {paper_match.clean_doi(p["doi"]): p["title"] for p in t["papers"]}
        first = ([{"doi": p["doi"], "title": p.get("title") or titles.get(p["doi"])} for p in chosen]
                 or [p for p in t["papers"] if not p["preprint"]] or t["papers"])[0]
        status = ("attempted" if key in attempted else "pilot" if key in pilot
                  else "no_match" if match == "no_match" else "open")
        targets.append({
            "key": key, "label": dataset_label(key), "name": t["name"], "size_gb": t["size_gb"],
            "files": t["asset_count"], "status": status, "match": match,
            "paper": first["doi"], "paper_title": first["title"] or t["name"],
            "papers": [p["doi"] for p in t["papers"]],
            "n_papers": len(t["papers"]),
            "technique": sorted({part.replace(" approach", "").strip()
                                 for a in t["approaches"] if a for part in a.split(";") if part.strip()}),
            "species": sorted({short_species(s) for s in t["species"] if s}),
            "catalystneuro": t.get("catalystneuro") or [],
        })
    # A dataset that only a paper reusing it names, outside every archive's list (its own metadata names no paper):
    # a target of the site all the same, so that an attempt on it has its rows and pages. Described in
    # targets/reuse_datasets.json (tools/build_reuse_targets.py). The runner's queue does not take it as a target:
    # it is reached through its paper (targets/reuse.yaml).
    outside_path = ROOT / "targets" / "reuse_datasets.json"
    outside = ({key_of("dandi", t["dandiset"]): t for t in json.loads(outside_path.read_text())["targets"]}
               if outside_path.is_file() else {})
    have = {t["key"] for t in targets}
    for paper_key, body in sorted(paper_records.listed().items()):
        for d in body.get("datasets") or []:
            if d["key"] in have:
                continue
            have.add(d["key"])
            t, doi = outside.get(d["key"], {}), paper_records.doi_of(paper_key)
            targets.append({
                "key": d["key"], "label": dataset_label(d["key"]), "name": t.get("name") or dataset_label(d["key"]),
                "size_gb": t.get("size_gb") or 0.0, "files": t.get("asset_count") or 0,
                "status": "attempted" if d["key"] in attempted else "open", "match": "matched", "reuse_only": True,
                "paper": doi, "paper_title": body.get("title") or t.get("name") or dataset_label(d["key"]),
                "papers": [doi], "n_papers": 1,
                "technique": sorted({part.replace(" approach", "").strip()
                                     for a in t.get("approaches") or [] if a for part in a.split(";") if part.strip()}),
                "species": sorted({short_species(x) for x in t.get("species") or [] if x}),
                "catalystneuro": [],
            })
    entry_list = []
    for entry in entries.values():
        related = entry.get("related", [])
        entry_list.append({
            "name": entry["name"], "type": entry["type"], "title": entry["title"],
            "description": squash(entry.get("description")),
            "datasets": sorted({key_of(*r["id"].split("/")[0].split(":", 1)) for r in related
                                if not r["id"].startswith(("doi:", "entry:"))}),
            "papers": [r["id"].split(":", 1)[1] for r in related if r["id"].startswith("doi:")],
            "derived_from": [r["id"].split(":", 1)[1] for r in related
                             if r["id"].startswith("entry:") and r["relation"] == "derived_from"],
            "notebooks": notebooks_of(entry),
            **environment_of(ROOT / "entries" / entry["name"]),
        })
    # Each dataset's transcripts (its paper's, transcripts/<paper>/, or before the cutover, a paper's on several
    # datasets, transcripts/<paper>/<folder>/), and an earlier attempt's, moved aside to attempt-NN/ by
    # tools/archive_transcripts.sh. Keyed by dataset, or dataset and attempt-NN; each with the folder it is in.
    transcripts, transcript_dirs = {}, {}
    for d, keys in transcript_folders():
        for key in keys:
            transcripts[key] = sorted(p.name for p in d.glob("*.md"))
            transcript_dirs[key] = d.relative_to(ROOT / "transcripts").as_posix()
            for a in sorted(d.glob("attempt-*")):
                if a.is_dir():
                    transcripts[f"{key}/{a.name}"] = sorted(p.name for p in a.glob("*.md"))
                    transcript_dirs[f"{key}/{a.name}"] = a.relative_to(ROOT / "transcripts").as_posix()
    archived = {}
    return finish({
        "pipeline": pipeline_inputs(),
        "claim_files": claim_files,
        # Claims belong to a paper (claims/<paper>.yaml): each paper's claims files with every claim, for its page.
        "paper_claims": paper_claims(),
        # Each paper's authors in order, with their ORCID iDs (papers/authors.yaml, tools/authors.py).
        "authors": ((load_yaml(ROOT / "papers" / "authors.yaml") or {}).get("papers", {})
                    if (ROOT / "papers" / "authors.yaml").is_file() else {}),
        "transcripts": {**transcripts, **archived},
        "transcript_dirs": transcript_dirs,
        "generated": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
        "queue_generated": queue["generated"],
        "queue_counts": {**queue["counts"], "with_a_paper": len(targets)},   # every archive's targets
        "attempts": attempts,
        "entries": entry_list,
        "targets": targets,
        "demo": False,
    })


def pipeline_inputs() -> dict:
    """What the Pipeline page reads besides the attempts: which papers are in the paper store
    (papers/manifest.yaml), each claims file's last check, and each attempt's open questions."""
    manifest = ROOT / "papers" / "manifest.yaml"
    papers = (load_yaml(manifest) or {}).get("targets", {}) if manifest.is_file() else {}
    checks, questions, items, paper_checks, paper_questions = {}, {}, {}, {}, {}
    # A record is a paper's: <kind>/<paper>.yaml, or from before the cutover <kind>/<paper>/<folder>.yaml.
    paper_key = lambda path: path.stem if path.parent.name in ("claims", "questions") else path.parent.name
    for path, keys in record_files("claims"):
        last = ((load_yaml(path) or {}).get("checks") or [None])[-1]
        found = {"ready": None if last is None else bool(last.get("ready")),
                 "date": None if last is None else str(last.get("date"))}
        for key in keys:
            checks[key] = found
        # Several files of one paper (one per dataset, before the cutover): ready when all are.
        had = paper_checks.get(paper_key(path))
        paper_checks[paper_key(path)] = found if had is None else {
            "ready": False if False in (had["ready"], found["ready"]) else None if None in (had["ready"], found["ready"])
            else True, "date": max(had["date"] or "", found["date"] or "") or None}
    for path, keys in record_files("questions"):
        q = load_yaml(path) or []
        q = q.get("questions", []) if isinstance(q, dict) else q
        n_open = sum(1 for x in q if not x.get("answered"))
        for key in keys:
            questions[key] = n_open
            items[key] = json.loads(json.dumps(q, default=str))   # YAML dates as text, for the JSON
        paper_questions[paper_key(path)] = paper_questions.get(paper_key(path), 0) + n_open
    return {"papers": {key_of_dir(str(k)): v for k, v in papers.items()}, "checks": checks, "questions": questions,
            "question_items": items, "paper_checks": paper_checks, "paper_questions": paper_questions}


def finish(data: dict) -> dict:
    """Totals, and each target's status, derived from the attempts."""
    data["outcome_counts"] = outcome_counts(data["attempts"])
    data["outcome_counts_with_outside_data"] = outcome_counts(data["attempts"], "with_inputs")
    data["outcome_counts_elsewhere"] = outcome_counts(data["attempts"], "elsewhere")
    data["outcome_counts_links"] = outcome_counts(data["attempts"], "link")
    attempted = {a["key"] for a in data["attempts"]}
    for t in data["targets"]:
        if t["key"] in attempted:
            t["status"] = "attempted"
    return data


def demo(data: dict, n: int, seed: int = 1) -> dict:
    """Replace the attempts with n made-up ones on real targets, to test at scale."""
    rng = random.Random(seed)
    figures = ["Figure 1C", "Figure 2A", "Figure 2D", "Figure 3B", "Figure 4E", "Figure 5", "Extended Data 2",
               "Results, section 2"]
    words = ("firing rate tuning population response selectivity latency decoding accuracy correlation "
             "modulation trial stimulus cells neurons layer region session behaviour choice reward").split()

    def sentence(k):
        return " ".join(rng.choice(words) for _ in range(k)).capitalize() + "."

    attempts = []
    for t in data["targets"][:n]:
        n_claims = rng.randint(4, 20)
        weights = rng.choice([(6, 2, 1, 2), (3, 2, 1, 6), (8, 1, 0, 1), (2, 3, 3, 4)])
        outcomes = []
        for i in range(n_claims):
            outcome = rng.choices(list(OUTCOMES), weights)[0]
            outcomes.append({
                "claim": f"claim-{i + 1}", "statement": sentence(rng.randint(10, 24)),
                "source": rng.choice(figures), "outcome": outcome,
                "blocked_by": rng.choice(list(BLOCKED_BY)) if outcome == "blocked" else None,
                "notebook": None if outcome == "blocked" else rng.choice(["figures.ipynb", "behaviour.ipynb"]),
                "notes": sentence(rng.randint(20, 50)),
                "deviations": [sentence(rng.randint(8, 16)) for _ in range(rng.randint(0, 3))]
                if outcome != "blocked" else [],
                "disagreed": rng.random() < 0.08,
            })
        tier = rng.choices(list(TIERS), (3, 6, 2, 1))[0]
        date = (datetime.date(2026, 10, 13) + datetime.timedelta(days=rng.randint(0, 200))).isoformat()
        attempts.append({
            "id": f"{split_key(t['key'])[1]}-demo-01", "dataset": {"archive": "dandi", "id": split_key(t["key"])[1], "version": "draft"},
            "key": t["key"], "label": t["label"], "dataset_version": "draft",
            "paper": t["paper"], "paper_title": t["paper_title"], "date": date, "kind": "agent",
            "accountable": "Demo",
            "agent": {"harness": "demo", "model": "demo", "protocol": "demo"}, "tier": tier,
            "entry": f"{split_key(t['key'])[1]}-demo", "entry_title": t["paper_title"],
            "description": sentence(30),
            "notebooks": [{"path": "figures.ipynb", "title": "Figures", "executed": None},
                          {"path": "behaviour.ipynb", "title": "Behaviour", "executed": None}],
            "outcomes": outcomes,
            "findings": [{"kind": rng.choice(list(FINDING_KINDS)), "statement": sentence(rng.randint(12, 30))}
                         for _ in range(rng.randint(1, 10))],
            "verifications": [] if tier == "runs" else [{
                "date": date, "kind": "agent", "by": "Demo verifier", "reviewed": "Demo",
                "agreed": n_claims, "of": n_claims, "disagreements": []}],
        })
    entries = [{"name": a["entry"], "type": "reproduction", "title": a["entry_title"],
                "description": a["description"], "datasets": [a["key"]], "papers": [a["paper"]],
                "derived_from": [], "notebooks": a["notebooks"]} for a in attempts]
    out = dict(data, attempts=attempts, entries=entries, demo=True, claim_files={},
               targets=[dict(t, status="pilot" if t["status"] == "pilot" else "open") for t in data["targets"]])
    return finish(out)


# --- flat rows for the list pages ----------------------------------------------

TIER_ORDER = list(TIERS)


FINDING_STATUS = {"new": "New", "still_present": "Still present", "partly_fixed": "Partly fixed"}


def reconcile(attempts: list[dict]) -> None:
    """Give a repeat attempt's findings their status against the attempt before it, from its reconciliation
    (docs/protocol.md, "Repeat attempts"), and list the earlier findings it found fixed or could not check."""
    by_id = {a["id"]: a for a in attempts}
    for a in attempts:
        rec = a.get("reconciliation")
        if not rec:
            continue
        earlier = by_id.get(rec["earlier"], {"findings": []})
        now = {f["now"]: f["status"] for f in rec["findings"] if f.get("now")}
        for i, f in enumerate(a["findings"], 1):
            f["status"] = now.get(i, "new")
        then = earlier["findings"]
        a["reconciliation"] = {
            "earlier": rec["earlier"], "blind": rec["blind"], "blind_note": squash(rec.get("blind_note")),
            "gone": [{"status": f["status"], "note": squash(f["note"]),
                      "statement": then[f["finding"] - 1]["statement"] if f["finding"] <= len(then) else "",
                      "kind": then[f["finding"] - 1]["kind"] if f["finding"] <= len(then) else "other",
                      "about": then[f["finding"] - 1].get("about", "data") if f["finding"] <= len(then) else "data"}
                     for f in rec["findings"] if f["status"] in ("fixed", "not_checked")],
            "outcomes": [{"claim": o["claim"], "earlier": o["earlier"], "note": squash(o["note"])}
                         for o in rec.get("outcomes") or []],
        }


def current_attempts(data: dict) -> dict[str, list[dict]]:
    """For each dandiset, the latest attempt on each of its papers, oldest first."""
    latest: dict = {}
    for a in sorted(data["attempts"], key=lambda a: (a["date"], a["id"])):
        latest[(a["key"], a["paper"])] = a
    out: dict = {}
    for a in sorted(latest.values(), key=lambda a: (a["date"], a["id"])):
        out.setdefault(a["key"], []).append(a)
    return out


def outcome_counts(attempts, group: str = "dataset") -> dict:
    """Outcome totals over one attempt or a list of them, for one group of claims.

    The groups are the paper's findings that rest on the dataset ("dataset"), those that also use
    data from elsewhere ("with_inputs"), those on data the paper deposited in another archive
    ("elsewhere"), and the registry's checks that the dataset is the paper's data ("link"), which are
    not findings of the paper. They are never added together, so that an outcome that may reflect
    outside data, or a link, does not count as a judgement of the paper's findings on the dandiset.
    """
    attempts = [attempts] if isinstance(attempts, dict) else attempts
    # A deprecated attempt stays on its page but counts for nothing.
    attempts = [a for a in attempts if not a.get("deprecated")]
    # Names for the dandiset's own codes taken from elsewhere (`with_labels`) count as the dandiset.
    groups = {"with_labels": "dataset", None: "dataset"}

    def group_of(o):
        return "link" if o.get("kind") == "link" else groups.get(o.get("data"), o.get("data"))
    return {k: sum(1 for a in attempts for o in a["outcomes"]
                   if o["outcome"] == k and group_of(o) == group) for k in OUTCOMES}


def outside_note(attempts, root: str = "", collapsed: bool = False) -> str:
    """Lines with the outcomes of the claims that use outside data or other archives, when there are any.
    Collapsed (the overview), they sit in a details block that names each group and its count."""
    out, labels = "", []
    for group, one, many, label in (
            ("with_inputs", "1 claim that also uses data from outside the dataset",
             "claims that also use data from outside the dataset", "claims using outside data"),
            ("elsewhere", "1 claim on data the paper deposited in another archive",
             "claims on data the paper deposited in other archives", "claims on data in other archives"),
            ("link", "1 check that the dataset is the data behind the paper",
             "checks that the dataset is the data behind the paper", "checks of the link to the paper")):
        counts = outcome_counts(attempts, group)
        m = sum(counts.values())
        if not m:
            continue
        text = one if m == 1 else f"{m} {many}"
        labels.append(f"{label} ({m:,})")
        lead = text[0].upper() + text[1:] if collapsed else f"Counted separately: {text}"
        out += (f'<p class="sub small" style="margin-top:8px">{lead}.</p>'
                f'<div class="summary">{bar(counts, f"Outcomes of {m} {label}", "bar mini")}'
                f'{legend(counts, compact=True)}</div>')
    if collapsed and out:
        names = labels[0] if len(labels) == 1 else ", ".join(labels[:-1]) + " and " + labels[-1]
        out = f'<details class="separate"><summary class="sub small">Counted separately: {names}</summary>{out}</details>'
    return out


def reproduced_share(counts: dict | None) -> float | None:
    """The share of the claims tested that reproduced, a partial reproduction counting as half; None when no claim
    was tested. It ranks the overview's most reproduced attempts and the datasets list's "Most reproduced" sort."""
    n = sum(counts.values()) if counts else 0
    return (counts["reproduced"] + counts["partially_reproduced"] / 2) / n if n else None


# The overview's most reproduced attempts: verified ones only, so that an unchecked attempt cannot top the list, and
# with enough claims that one claim reproduced is not a perfect score.
TOP_MIN_CLAIMS = 5


def weakest_tier(attempts: list[dict]) -> str:
    """A dandiset is only as verified as its least verified attempt."""
    return min((a["tier"] for a in attempts), key=TIER_ORDER.index)


PIPELINE_STEPS = [("paper", "Paper"), ("claims", "Claims"), ("check", "Claims check"),
                  ("attempt", "Attempt"), ("questions", "Questions"), ("verified", "Verified")]


def queue_estimates(q: dict, name=None) -> dict[str, dict]:
    """Each queued dataset's place in its runner's queue, and how many hours from now it should be done.
    `name` turns a queue's entry into the key of the result (a dataset's key from its folder, unless given).

    The lanes take the datasets in order, each taking the median time of a recent chain (the runs' times,
    `tools/runner/describe.py queue`). A lane is free when the chain it has going now should be done
    (q["running"]), and without those times the chains going now are taken to be half done. A dataset in
    both queues gets the full runner's estimate."""
    out = {}
    for kind in ("claims", "full"):
        hours = (q.get("hours") or {}).get(kind)
        n = max(1, (q.get("lanes") or {}).get(kind, 1))
        if "running" in q:
            going = sorted(r["hours"] or 0.0 for r in q["running"].values() if r["kind"] == kind)
            free = (going + [0.0] * n)[:n]
        else:
            free = [hours / 2 if hours else 0.0] * n
        for place, folder in enumerate(q.get(kind, []), 1):
            lane = free.index(min(free))
            free[lane] += hours or 0.0
            out[(name or key_of_dir)(folder)] = {"kind": kind, "place": place, "hours": free[lane] if hours else None}
    return out


def in_hours(hours: float | None) -> str:
    if hours is None:
        return ""
    if hours < 1:
        return "within the hour"
    if hours < 1.5:
        return "about an hour"
    return f"about {round(hours)} hours" if hours < 48 else f"about {round(hours / 24)} days"


def pipeline_rows(data: dict) -> list[dict]:
    """One row per target: the state of each step of docs/pipeline.md, read from the repository.

    A state is "done", "waiting" (on a person: a paper to supply, a claims file its check did not
    pass), "todo", "deprecated", or "none" (a step that does not apply)."""
    inputs = data.get("pipeline") or {"papers": {}, "checks": {}, "questions": {}}
    current = current_attempts(data)
    queued = queue_estimates(data.get("queue") or {})
    branches = {key_of_dir(f) for f in (data.get("queue") or {}).get("branches", [])}
    going = {key_of_dir(f): r for f, r in ((data.get("queue") or {}).get("running") or {}).items()}
    out = []
    for t in data["targets"]:
        d = t["key"]
        papers = inputs["papers"].get(d, [])
        missing = [p["doi"] for p in papers if p["status"] == "missing"]
        stored = sum(1 for p in papers if p["status"] == "stored")
        found = inputs["checks"].get(d)
        check = "absent" if found is None else found["ready"]
        atts = current.get(d, [])
        open_q = inputs["questions"].get(d, 0)
        # A deprecated attempt's claims are to be read again from the paper, unless a claims file checked
        # since it was deprecated has been merged (the checkpoint in docs/pipeline.md).
        deprecated_on = max((a["deprecated_on"] or "" for a in atts if a.get("deprecated")), default="")
        reread = bool(deprecated_on) and found is not None and (found["date"] or "") >= deprecated_on
        rerun = bool(deprecated_on) and not reread
        state = {
            "paper": ("done", f"{stored} of {len(papers)}") if papers and not missing
            else ("waiting", f"{len(missing)} not in store") if papers
            # The manifest is rewritten from the private store every hour (manifest.yml,
            # tools/papers_manifest.py), so a target added since its last run names papers it has not checked yet.
            else ("waiting", "not checked") if t.get("papers") else ("waiting", "no paper named"),
            "claims": ("todo", "to read again") if rerun else ("done", "read again" if reread else "")
            if check != "absent" else ("todo", ""),
            "check": ("todo", "") if rerun else ("done", "ready") if check is True
            else ("waiting", "not ready") if check is False
            else ("none", "before checks") if check is None else ("todo", ""),
            "attempt": ("deprecated", "rerun due") if deprecated_on
            else ("done", atts[-1]["date"]) if atts else ("todo", ""),
            "questions": ("todo", f"{open_q} open") if open_q else ("none", ""),
            "verified": ("done", "") if atts and all(a["tier"] != "runs" for a in atts)
            else ("todo", "") if atts else ("none", ""),
        }
        nxt = next((label for key, label in PIPELINE_STEPS if state[key][0] in ("todo", "waiting", "deprecated")), "")
        out.append({"dataset": t["label"], "key": d, "name": t["name"], "state": state, "next": nxt,
                    "issue": data.get("issues", {}).get(t["label"]),
                    "waiting": [label for key, label in PIPELINE_STEPS if state[key][0] == "waiting"],
                    "missing": missing, "page": page_of(d) if atts or d in data.get("claim_files", {}) else None,
                    "queue": queued.get(d), "branch": d in branches, "running": going.get(d)})
    return out


# The Pipeline page goes by paper (docs/paper-first.md): the paper match comes first, and lists a dataset for
# its paper.
PAPER_STEPS = [("match", "Paper match")] + PIPELINE_STEPS


def paper_pipeline_rows(data: dict) -> list[dict]:
    """One row per paper, for the Pipeline page: each paper listed for datasets (papers/datasets/), with the state
    of each step read from the paper's own records, then the targets no paper is listed for yet, by the paper their
    archive names (several datasets naming one paper share a row). States are as in pipeline_rows."""
    inputs = data.get("pipeline") or {}
    manifest, checks, open_qs = inputs.get("papers", {}), inputs.get("paper_checks", {}), inputs.get("paper_questions", {})
    current, claim_files = current_attempts(data), data.get("claim_files", {})
    listed = paper_records.listed()
    q = data.get("queue") or {}
    # The queue names papers, and datasets not matched yet by their folders (describe.py queue, "papers"); one
    # written before that names datasets only, and a paper is then found by its datasets.
    by_paper = q.get("papers")
    names = by_paper or q
    est = queue_estimates({**q, "full": names.get("full", []), "claims": names.get("claims", []),
                           **({"running": names["running"]} if "running" in names else {})}, name=str)
    going, branches = names.get("running") or {}, set(names.get("branches") or [])
    issues, issues_by_name = data.get("issues", {}), data.get("issues_by_name", {})

    def queued(ids: list[str]) -> dict:
        places = [est[i] for i in ids if i in est]
        return {"running": next((going[i] for i in ids if i in going), None), "branch": any(i in branches for i in ids),
                "queue": min(places, key=lambda x: (x["kind"] != "full", x["place"])) if places else None}

    def dataset_cell(k: str) -> dict:
        return {"key": k, "label": dataset_label(k), "page": page_of(k) if current.get(k) or k in claim_files else None}

    fixes = paper_match.triage()

    def text_state(doi: str | None, keys: list[str]) -> tuple[str, str]:
        if not doi:
            return ("waiting", "no paper named")
        doi = paper_match.clean_doi(doi)   # an eLife version (.1) names the article, as in the manifest
        found = [r["status"] for k in keys for r in manifest.get(k, []) if paper_match.clean_doi(r["doi"]) == doi]
        if not found:
            # A paper listed under a DOI the triage has since replaced (a preprint by its publication, a data
            # DOI by the paper): its text is the replacement's, which the triage names for the dataset.
            for k in keys:
                fix = fixes.get(dir_of(k), {})
                if doi in {paper_match.clean_doi(x) for x in fix.get("not_papers", {})}:
                    named = {paper_match.clean_doi(x) for x in fix.get("papers", {})}
                    found += [r["status"] for r in manifest.get(k, []) if paper_match.clean_doi(r["doi"]) in named]
        return (("done", "stored") if "stored" in found else ("none", "unavailable") if "unavailable" in found
                else ("waiting", "not in store") if found else ("waiting", "not checked"))

    def finish_row(row: dict) -> dict:
        state = row["state"]
        row["next"] = next((label for key, label in PAPER_STEPS if state[key][0] in ("todo", "waiting", "deprecated")), "")
        row["waiting"] = [label for key, label in PAPER_STEPS if state[key][0] == "waiting"]
        row["missing"] = [row["doi"]] if state["paper"] == ("waiting", "not in store") else []
        return row

    out, primary, by_doi = [], set(), {}
    for p in papers_of(data):
        key, doi = p["key"], p["doi"]
        body = listed.get(key) or {}
        primary |= {d["key"] for d in body.get("datasets") or [] if d.get("relation", "primary") == "primary"}
        need = [d["key"] for d in body.get("datasets") or [] if d.get("available", True)] or p["datasets"]
        atts, live, chk = p["attempts"], p["live"], checks.get(key)
        check = "absent" if chk is None else chk["ready"]
        # As for a dataset: a deprecated attempt's claims are to be read again, unless checked since.
        deprecated_on = max((a.get("deprecated_on") or "" for a in atts if a.get("deprecated")), default="")
        reread = bool(deprecated_on) and chk is not None and (chk["date"] or "") >= deprecated_on
        rerun = bool(deprecated_on) and not reread
        covered = {k for k in need for a in current.get(k, [])
                   if a["paper"].lower() == doi and not a.get("deprecated")}
        open_q = open_qs.get(key, 0)
        state = {
            "match": ("done", ""),
            "paper": text_state(doi, p["datasets"]),
            "claims": ("todo", "to read again") if rerun else ("done", "read again" if reread else "")
            if check != "absent" else ("todo", ""),
            "check": ("todo", "") if rerun else ("done", "ready") if check is True
            else ("waiting", "not ready") if check is False
            else ("none", "before checks") if check is None else ("todo", ""),
            # A dataset added to a paper opens it again: its attempt is done when every dataset has been used.
            "attempt": ("deprecated", "rerun due") if deprecated_on
            else ("done", p["date"]) if need and covered == set(need)
            else ("todo", f"{len(covered)} of {len(need)} datasets") if covered else ("todo", ""),
            "questions": ("todo", f"{open_q} open") if open_q else ("none", ""),
            "verified": ("done", "") if live and all(a["tier"] != "runs" for a in live)
            else ("todo", "") if live else ("none", ""),
        }
        folders = [dir_of(k) for k in p["datasets"]]
        row = finish_row({
            "paper": key, "byline": p["byline"], "title": p["title"], "doi": doi, "relation": p["relation"],
            "datasets": [dataset_cell(k) for k in p["datasets"]], "state": state,
            "issue": issues_by_name.get(key) or next((issues[dataset_label(k)] for k in p["datasets"]
                                                      if dataset_label(k) in issues), None),
            "page": f"papers/{key}/" if atts or p["status"] == "claims" else None,
            **queued([key] + ([] if by_paper else folders))})
        by_doi[doi] = row
        out.append(row)

    groups: dict[str, list[dict]] = {}
    for t in data["targets"]:
        # A dataset its own paper is listed for, or one that only a paper reusing it names: in that paper's row.
        if t["key"] in primary or t.get("reuse_only"):
            continue
        doi = paper_match.clean_doi(t["paper"]) if t.get("paper") else None
        match = t.get("match", "unchecked")
        if doi in by_doi and match != "no_match":
            # Another dataset of a paper that has its row: it joins the paper once its match is made.
            row = by_doi[doi]
            row["datasets"].append(dataset_cell(t["key"]))
            if row["state"]["match"][0] == "done" or match == "held":
                row["state"]["match"] = (("waiting", "verdicts to confirm") if match == "held"
                                         else ("todo", "a dataset to match"))
            finish_row(row)
            continue
        groups.setdefault(f"{doi}|{'no_match' if match == 'no_match' else ''}" if doi else t["key"], []).append(t)
    for ts in groups.values():
        doi = paper_match.clean_doi(ts[0]["paper"]) if ts[0].get("paper") else None
        matches = {t.get("match", "unchecked") for t in ts}
        keys = [t["key"] for t in ts]
        if matches == {"no_match"}:
            state = {key: ("none", "") for key, _ in PAPER_STEPS}
            state["match"] = ("none", "no paper matches")
        else:
            state = {"match": ("waiting", "verdicts to confirm") if "held" in matches
                     else ("todo", "to list") if matches == {"matched"} else ("todo", ""),
                     "paper": text_state(doi, keys), "claims": ("todo", ""), "check": ("todo", ""),
                     "attempt": ("todo", ""), "questions": ("none", ""), "verified": ("none", "")}
        out.append(finish_row({
            "paper": None, "byline": "", "title": ts[0].get("paper_title") or ts[0]["name"], "doi": doi,
            "relation": ["primary"], "datasets": [dataset_cell(k) for k in keys], "state": state,
            "issue": next((issues[t["label"]] for t in ts if t["label"] in issues), None), "page": None,
            **queued([dir_of(k) for k in keys])}))
    return out


def entries_for(data: dict, dandiset: str) -> list[dict]:
    """Every entry whose metadata says it uses this dataset."""
    return [en for en in data["entries"] if dandiset in en["datasets"]]


def notebook_of(attempt: dict, path: str | None) -> dict | None:
    return next((n for n in attempt["notebooks"] if n["path"] == path), None)


TOP_JOURNALS = 25


_JOURNALS: dict = {}


def journals_known() -> dict:
    """The papers of papers/journals.yaml, by DOI: read once for each state of the file (a page of every paper and
    of every author asks for a journal)."""
    path = ROOT / "papers" / "journals.yaml"
    if not path.is_file():
        return {}
    stamp = (str(path), path.stat().st_mtime_ns)
    if stamp not in _JOURNALS:
        _JOURNALS.clear()
        _JOURNALS[stamp] = (load_yaml(path) or {}).get("papers", {})
    return _JOURNALS[stamp]


def journals_of(targets: list[dict]) -> dict[str, str]:
    """Each target's journal for the datasets list's filter (papers/journals.yaml, tools/journals.py): one of the
    TOP_JOURNALS journals with the most datasets, "Preprint", "Other journals", or "Not recorded"."""
    known = journals_known()
    norm = lambda d: re.sub(r"^(10\.1101/[\d.]+)v\d+$", r"\1", (d or "").strip().lower())
    raw = {t["key"]: (known.get(norm(t.get("paper"))) or {}).get("journal") for t in targets}
    counts: dict = {}
    for j in raw.values():
        if j and j != "Preprint":
            counts[j] = counts.get(j, 0) + 1
    top = {j for j, _ in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:TOP_JOURNALS]}
    return {k: (j if j in top or j == "Preprint" else "Other journals" if j else "Not recorded") for k, j in raw.items()}


def journal_order(rows: list[dict]) -> list[str]:
    """The journal filter's order: the journals by number of datasets, then the groups that are not one journal."""
    groups = ["Preprint", "Other journals", "Not recorded"]
    counts: dict = {}
    for r in rows:
        if r.get("journal") and r["journal"] not in groups:
            counts[r["journal"]] = counts.get(r["journal"], 0) + 1
    return [j for j, _ in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))] + groups


def rows(data: dict) -> dict[str, list]:
    current = current_attempts(data)
    by_id = {t["key"]: t for t in data["targets"]}
    dandisets, claims, findings = [], [], []
    journal = journals_of(data["targets"])
    for t in data["targets"]:
        atts = current.get(t["key"])
        outcomes = [o for a in atts or [] if not a.get("deprecated") for o in a["outcomes"]]
        dandisets.append({
            "id": t["key"], "label": t["label"], "name": t["name"], "paper": t["paper"], "paper_title": t["paper_title"],
            "archive": split_key(t["key"])[0], "technique": t["technique"], "species": t["species"], "size_gb": t["size_gb"], "files": t["files"],
            "status": t["status"], "tier": weakest_tier(atts) if atts else None,
            "date": max(a["date"] for a in atts) if atts else None,
            "counts": outcome_counts(atts) if atts else None,
            # The paper's claims on data outside the dataset, counted apart (outcome_counts), links aside.
            "elsewhere": sum(sum(outcome_counts(atts, g).values()) for g in ("with_inputs", "elsewhere")) if atts else None,
            "claims": len(outcomes) if atts else None,
            "failures": sum(1 for o in outcomes if o["outcome"] == "not_reproduced") if atts else None,
            "reproduced": (round(share, 4) if (share := reproduced_share(outcome_counts(
                [a for a in atts if not a.get("deprecated")]))) is not None else None) if atts else None,
            "has": sorted({o["outcome"] for o in outcomes}),
            "blocked_by": sorted({o["blocked_by"] for o in outcomes if o["blocked_by"]}),
            "notebooks": sum(len(en["notebooks"]) for en in entries_for(data, t["key"])),
            "page": page_of(t["key"]) if atts else None, "url": archive_url(t["key"]),
            "findings": sum(len(a["findings"]) for a in atts if not a.get("deprecated")) if atts else None,
            "found": sorted({f["kind"] for a in atts or [] if not a.get("deprecated") for f in a["findings"]}),
            # For the datasets list, which a curator reads: the open findings by kind (most first), the versions
            # the attempts ran on, and how many papers were tested on the dataset.
            "found_counts": dict(Counter(f["kind"] for a in atts or [] if not a.get("deprecated")
                                         for f in a["findings"]).most_common()),
            "versions": list(dict.fromkeys(version_plain(a) for a in sorted(
                atts or [], key=version_order, reverse=True) if not a.get("deprecated"))),
            "tested": sorted({version_state(a) for a in atts or [] if not a.get("deprecated")}),
            "n_tested": len({a["paper"].lower() for a in atts or [] if not a.get("deprecated")}),
            "deprecated": any(a.get("deprecated") for a in atts or []),
            "converted": "catalystneuro" if t["catalystneuro"] else "other",
            "journal": journal.get(t["key"], "Not recorded"),
        })
    for atts in current.values():
        for a in atts:
            if a.get("deprecated"):
                continue
            t = by_id.get(a["key"], {})
            common = {"dataset": a["label"], "key": a["key"], "page": page_of(a["key"]), "tier": a["tier"],
                      "technique": t.get("technique", []), "species": t.get("species", []),
                      "paper_title": a.get("paper_title") or t.get("paper_title") or a["entry_title"],
                      "date": a["date"]}
            for o in a["outcomes"]:
                nb = notebook_of(a, o.get("notebook"))
                claims.append({**common, "claim": o["claim"], "statement": o["statement"], "source": o["source"],
                               "quote": o.get("quote"), "statistics": o.get("statistics"),
                               "outcome": o["outcome"], "blocked_by": o["blocked_by"], "notes": o["notes"],
                               "deviations": o["deviations"], "disagreed": o["disagreed"],
                               "verifier": "disagreed" if o["disagreed"] else None,
                               "notebook": nb["executed"] if nb else None,
                               "notebook_title": nb["title"] if nb else None})
            for f in a["findings"]:
                findings.append({**common, "kind": f["kind"], "statement": f["statement"]})
    return {"papers": paper_rows(data), "datasets": dandisets, "claims": claims, "findings": findings,
            "authors": author_rows(data)}


_PAPERS: dict = {}


def journal_name(doi: str) -> str | None:
    """The paper's journal as papers/journals.yaml names it (tools/journals.py), for its page; None when not recorded."""
    known = journals_known()
    return (known.get(re.sub(r"^(10\.1101/[\d.]+)v\d+$", r"\1", (doi or "").strip().lower())) or {}).get("journal")


def paper_journals(dois: list[str]) -> dict[str, str]:
    """Each paper's journal for the papers list's filter (papers/journals.yaml): one of the TOP_JOURNALS journals with
    the most papers, "Preprint", "Other journals", or "Not recorded"."""
    known = journals_known()
    norm = lambda d: re.sub(r"^(10\.1101/[\d.]+)v\d+$", r"\1", (d or "").strip().lower())
    raw = {d: (known.get(norm(d)) or {}).get("journal") for d in dois}
    counts: dict = {}
    for j in raw.values():
        if j and j != "Preprint":
            counts[j] = counts.get(j, 0) + 1
    top = {j for j, _ in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:TOP_JOURNALS]}
    return {d: (j if j in top or j == "Preprint" else "Other journals" if j else "Not recorded") for d, j in raw.items()}


def byline(key: str) -> str:
    """"Tingley et al. 2021" from a paper key (tingley-2021, daume-2024-phase)."""
    m = re.match(r"^(.+?)-(\d{4})(?:-|$)", key)
    if not m:
        return key
    surname = " ".join(w.capitalize() for w in m.group(1).split("-"))
    return f"{surname} et al. {m.group(2)}"


def papers_of(data: dict) -> list[dict]:
    """Every paper with records, or listed for a dataset (papers/datasets/), with its datasets and latest attempts:
    for each of its datasets, the latest attempt on the paper (current_attempts), each attempt once."""
    if id(data) in _PAPERS:
        return _PAPERS[id(data)]
    current = current_attempts(data)
    by_key = {t["key"]: t for t in data["targets"]}
    claim_papers = {f["paper"].lower() for fs in data.get("claim_files", {}).values() for f in fs}
    out = []
    for key, body in sorted(paper_records.listed().items()):
        doi = paper_records.doi_of(key)
        ds = [d["key"] for d in body.get("datasets") or []]
        atts, seen = [], set()
        for k in ds:
            for a in current.get(k, []):
                if a["paper"].lower() == doi and a["id"] not in seen:
                    seen.add(a["id"])
                    atts.append(a)
        atts.sort(key=lambda a: (a["date"], a["id"]))
        live = [a for a in atts if not a.get("deprecated")]
        title = (body.get("title") or next((a.get("paper_title") for a in atts if a.get("paper_title")), None)
                 or next((by_key[k]["paper_title"] for k in ds if k in by_key and by_key[k].get("paper") == doi), None)
                 or byline(key))
        out.append({
            "key": key, "doi": doi, "title": title, "byline": byline(key), "datasets": ds,
            "relation": sorted({d.get("relation", "primary") for d in body.get("datasets") or []}),
            "attempts": atts, "live": live,
            "status": "attempted" if atts else "claims" if doi in claim_papers else "open",
            "date": max(a["date"] for a in atts) if atts else None,
        })
    _PAPERS.clear()
    _PAPERS[id(data)] = out
    return out


AUTHORS_SHOWN = 12   # a paper's page names this many authors, and the rest on request
_AUTHORS: dict = {}


def authors_of(data: dict, doi: str) -> list[dict]:
    """A paper's authors in order (papers/authors.yaml): name, and ORCID iD or none."""
    key = re.sub(r"^(10\.1101/[\d.]+)v\d+$", r"\1", (doi or "").strip().lower())
    return (data.get("authors") or {}).get(key) or []


def author_index(data: dict) -> dict[str, dict]:
    """Every author with an ORCID iD, by iD: the name (the one most of their papers print) and their papers in the
    registry (papers_of), newest first. An author without an iD has no entry: a name alone does not say who it is."""
    if id(data) in _AUTHORS:
        return _AUTHORS[id(data)]
    names: dict = {}
    out: dict = {}
    for q in papers_of(data):
        for a in authors_of(data, q["doi"]):
            if a.get("orcid"):
                names.setdefault(a["orcid"], Counter())[a["name"]] += 1
                out.setdefault(a["orcid"], {"orcid": a["orcid"], "papers": []})["papers"].append(q)
    for orcid, entry in out.items():
        entry["name"] = sorted(names[orcid].items(), key=lambda kv: (-kv[1], -len(kv[0]), kv[0]))[0][0]
        entry["papers"].sort(key=lambda q: (q["key"].rsplit("-", 1)[-1], q["key"]), reverse=True)
    _AUTHORS.clear()
    _AUTHORS[id(data)] = out
    return out


def authors_html(data: dict, doi: str, root: str) -> str:
    """A paper's authors for its page: each with an ORCID iD opens the author's page; the names past the first
    AUTHORS_SHOWN open on request."""
    people = authors_of(data, doi)
    if not people:
        return ""
    known = author_index(data)
    names = [f'<a href="{root}authors/{e(a["orcid"])}/">{e(a["name"])}</a>' if a.get("orcid") in known else e(a["name"])
             for a in people]
    if len(names) <= AUTHORS_SHOWN + 2:
        return f'<p class="authors">{", ".join(names)}</p>'
    rest = len(names) - AUTHORS_SHOWN
    return (f'<div class="authors"><p>{", ".join(names[:AUTHORS_SHOWN])},</p><details><summary>and {rest} more '
            f'authors</summary><p>{", ".join(names[AUTHORS_SHOWN:])}</p></details></div>')


def author_rows(data: dict) -> list[dict]:
    """The authors list's rows: every author with an ORCID iD and their papers in the registry."""
    out = []
    for orcid, a in author_index(data).items():
        attempted = [q for q in a["papers"] if q["attempts"]]
        out.append({
            "id": orcid, "name": a["name"], "family": a["name"].split()[-1] + ", " + " ".join(a["name"].split()[:-1]),
            "page": f"authors/{orcid}/", "n_papers": len(a["papers"]), "n_attempted": len(attempted),
            "attempted": "yes" if attempted else "no",
            "papers": [{"byline": q["byline"], "page": f'papers/{q["key"]}/' if q["attempts"] or q["status"] == "claims"
                        else None, "doi": q["doi"]} for q in a["papers"]],
        })
    return sorted(out, key=lambda r: (-r["n_papers"], r["family"].lower()))


def paper_card(data: dict, q: dict, root: str, note: str = "", under: str = "") -> str:
    """A paper as a row: its byline (and `note`) over its title, which opens its page, then its outcomes or where
    it stands, and `under`; its verification and the date of its latest attempt on the right."""
    r = next((x for x in rows_cache(data)["papers"] if x["id"] == q["key"]), {})
    state = ("attempted" if q["attempts"] else "claims read, not yet attempted" if q["status"] == "claims"
             else "not yet attempted")
    outcome = (f'<div class="meta" style="margin-top:6px">{bar(r["counts"], "Outcomes", "bar mini")}'
               + '<span class="small muted">' + e(" · ".join(f"{n} {OUTCOMES[k][0].lower()}" for k, n in r["counts"].items() if n))
               + '</span></div>') if r.get("counts") else f'<div class="meta"><span class="muted">{e(state.capitalize())}</span></div>'
    title = (f'<a href="{root}{e(r["page"])}">{e(q["title"])}</a>' if r.get("page")
             else f'<a href="https://doi.org/{e(q["doi"])}">{e(q["title"])}</a>')
    return (f'<div class="row drow prow"><div><p class="byline">{e(q["byline"])}'
            + (f'<span class="sep" aria-hidden="true">·</span>{note}' if note else "") + '</p>'
            f'<p class="title">{title}</p>{outcome}{under}</div>'
            f'<div class="right">{quiet_tier(r["tier"]) if r.get("tier") else ""}'
            f'<span class="small muted">{e(r.get("date") or "")}</span></div></div>')


def page_author(data: dict, author: dict) -> str:
    """An author's page, by ORCID iD: every paper in the registry they are an author of."""
    root = "../../"
    orcid, name = author["orcid"], author["name"]
    cards = "".join(paper_card(data, q, root, note=e(journal_name(q["doi"]) or "")) for q in author["papers"])
    n, tried = len(author["papers"]), sum(1 for q in author["papers"] if q["attempts"])
    body = f'''<header class="page">
  <p class="crumbs"><a href="{root}authors/">Authors</a> / {e(name)}</p>
  <div class="dhead"><h1>{e(name)}</h1></div>
  <p class="sub">ORCID iD <a href="https://orcid.org/{e(orcid)}" rel="noopener">{e(orcid)}</a> ·
  {n} paper{"" if n == 1 else "s"} in the registry, {tried} attempted</p>
</header>
<main>
  <section class="panel"><h2>Papers <span class="count">{n}</span></h2>
    <p class="sub small" style="margin-top:12px">Every paper in the registry that names this ORCID iD among its
    authors, as OpenAlex records them. An outcome says what one attempt could reproduce from the paper&rsquo;s open
    data; a failure to reproduce may be a failure of the attempt.</p>
    <div class="results" style="margin-top:12px">{cards}</div></section>
</main>'''
    structured = {"@context": "https://schema.org", "@type": "Person", "name": name,
                  "identifier": f"https://orcid.org/{orcid}", "sameAs": f"https://orcid.org/{orcid}"}
    return shell(data, f"{name} · {SITE_NAME}", root, "authors", body, path=f"authors/{orcid}/",
                 description=f"Papers by {name} (ORCID {orcid}) in the Encore registry, and what attempts to "
                             f"reproduce them from their open data found.", structured=structured)


def paper_of(data: dict, attempt: dict) -> dict | None:
    """The paper (papers_of) an attempt is on."""
    return next((q for q in papers_of(data) if q["doi"] == attempt["paper"].lower()), None)


def paper_attempts(data: dict, paper: dict) -> list[dict]:
    """Every attempt on a paper, current or replaced, each once (an attempt on several datasets is a row for each
    in data["attempts"]), oldest first."""
    seen, out = set(), []
    for a in sorted(data["attempts"], key=lambda a: (a["date"], a["id"])):
        if a["paper"].lower() == paper["doi"] and a["id"] not in seen:
            seen.add(a["id"])
            out.append(a)
    return out


def attempt_sets(data: dict, attempt: dict) -> list[dict]:
    """An attempt's rows, one for each dataset it used: each has that dataset's version and the findings about it."""
    return [a for a in data["attempts"] if a["id"] == attempt["id"]]


def attempt_own_path(data: dict, attempt: dict) -> str | None:
    """The address of an attempt's own page, under its paper: papers/<paper>/<attempt>/."""
    q = paper_of(data, attempt)
    return f'papers/{q["key"]}/{attempt["id"]}/' if q else None


def attempt_path(data: dict, attempt: dict) -> str:
    """Where to read an attempt: its own page, or its paper's page when it is the paper's one current attempt (its
    own address then leads there). An attempt whose paper is not listed is read on its dataset's pages."""
    q = paper_of(data, attempt)
    if not q:
        current = current_attempts(data).get(attempt["key"], [])
        return page_of(attempt["key"]) + ("" if attempt in current else f'{attempt["id"]}/')
    if [a["id"] for a in q["attempts"]] == [attempt["id"]]:
        return f'papers/{q["key"]}/'
    return f'papers/{q["key"]}/{attempt["id"]}/'


def used_html(data: dict, attempt: dict, root: str) -> str:
    """The datasets an attempt used, each a link to the dataset's page, with the version it ran on."""
    return "; ".join(f'<a href="{root}{e(page_of(x["key"]))}">{e(x["label"])}</a> {version_text(x)}'
                     for x in attempt_sets(data, attempt))


def paper_rows(data: dict) -> list[dict]:
    by_key = {t["key"]: t for t in data["targets"]}
    papers = papers_of(data)
    journal = paper_journals([p["doi"] for p in papers])
    rows_ = []
    for p in papers:
        live, atts = p["live"], p["attempts"]
        outcomes = [o for a in live for o in a["outcomes"]]
        counts = outcome_counts(live) if live else None
        rows_.append({
            "id": p["key"], "title": p["title"], "byline": p["byline"], "doi": p["doi"],
            "journal": journal.get(p["doi"], "Not recorded"),
            "datasets": [{"key": k, "label": dataset_label(k), "name": by_key.get(k, {}).get("name"),
                          "page": page_of(k) if k in {a["key"] for a in atts}
                          or k in data.get("claim_files", {}) else None} for k in p["datasets"]],
            "n_datasets": len(p["datasets"]),
            "archive": sorted({split_key(k)[0] for k in p["datasets"]}),
            "relation": p["relation"],
            "technique": sorted({x for k in p["datasets"] for x in by_key.get(k, {}).get("technique", [])}),
            "species": sorted({x for k in p["datasets"] for x in by_key.get(k, {}).get("species", [])}),
            "status": p["status"], "tier": weakest_tier(live) if live else None, "date": p["date"],
            "counts": counts, "claims": len(outcomes) if live else None,
            "elsewhere": sum(sum(outcome_counts(live, g).values()) for g in ("with_inputs", "elsewhere")) if live else None,
            "failures": sum(1 for o in outcomes if o["outcome"] == "not_reproduced") if live else None,
            "reproduced": (round(share, 4) if (share := reproduced_share(counts)) is not None else None) if live else None,
            "has": sorted({o["outcome"] for o in outcomes}),
            "blocked_by": sorted({o["blocked_by"] for o in outcomes if o["blocked_by"]}),
            "findings": sum(len(a["findings"]) for a in live) if live else None,
            # What the datasets list had, now that the papers are the one list: what was found about the data, and
            # whether CatalystNeuro converted any of the paper's datasets.
            "found": sorted({f["kind"] for a in live for f in a["findings"]}),
            "converted": "catalystneuro" if any(by_key.get(k, {}).get("catalystneuro") for k in p["datasets"]) else "other",
            "missing": sum(len(a.get("missing_datasets") or []) for a in live),
            "page": f"papers/{p['key']}/" if atts or p["status"] == "claims" else None,
        })
    return rows_


# --- html pieces ---------------------------------------------------------------

def e(text) -> str:
    return html.escape(str(text if text is not None else ""), quote=True)


def chip(outcome: str, href: str | None = None) -> str:
    label, css, icon = OUTCOMES[outcome]
    inner = f'<span class="icon" aria-hidden="true">{icon}</span>{label}'
    return (f'<a class="chip {css}" href="{e(href)}">{inner}</a>' if href
            else f'<span class="chip {css}">{inner}</span>')


def bar(counts: dict, label: str, css: str = "bar", href=None) -> str:
    """A stacked bar of outcomes. With `href`, each segment links to a filtered list."""
    total = sum(counts.values())
    segments = []
    for k, n in counts.items():
        if not n:
            continue
        attrs = f'class="seg {OUTCOMES[k][1]}" style="flex:{n}" title="{OUTCOMES[k][0]}: {n} of {total}"'
        segments.append(f'<a {attrs} href="{e(href(k))}" aria-label="{OUTCOMES[k][0]}: {n}"></a>' if href
                        else f'<span {attrs}></span>')
    return f'<div class="{css}" role="img" aria-label="{e(label)}">{"".join(segments)}</div>'


def legend(counts: dict, compact: bool = False, href=None) -> str:
    items = []
    for key, (label, css, icon) in OUTCOMES.items():
        n = counts[key]
        if compact and not n:
            continue
        text = f'<strong>{n}</strong> {label.lower() if compact else label}'
        if href:
            text = f'<a href="{e(href(key))}">{text}</a>'
        items.append(f'<li><span class="swatch {css}" aria-hidden="true">{icon}</span>{text}</li>')
    return f'<ul class="legend{" compact" if compact else ""}">{"".join(items)}</ul>'


def deprecated_badge() -> str:
    return '<span class="tier pending">Deprecated</span>'


def tier_badge(tier: str, href: str | None = None) -> str:
    verified = tier != "runs"
    text = ("✓ " if verified else "") + (TIERS[tier] if verified else "Not yet verified")
    css = "tier" + ("" if verified else " pending")
    return f'<a class="{css}" href="{e(href)}">{e(text)}</a>' if href else f'<span class="{css}">{e(text)}</span>'


SUPERSCRIPT = str.maketrans("-0123456789", "⁻⁰¹²³⁴⁵⁶⁷⁸⁹")


def p_text(p: float) -> str:
    """0.002 stays as it is; 2.4e-05 becomes 2.4 × 10⁻⁵."""
    if p == 0 or p >= 0.001:
        return f"{p:g}"
    mantissa, exponent = f"{p:.1e}".split("e")
    mantissa, exponent = mantissa.removesuffix(".0"), str(int(exponent)).translate(SUPERSCRIPT)
    return f"10{exponent}" if mantissa == "1" else f"{mantissa} × 10{exponent}"


def statistic_text(s: dict) -> str:
    """One reported test or interval in a line, e.g. 'Onsets: Wilcoxon rank-sum, p = 2.4 × 10⁻⁵ (n = 385 units)'."""
    parts = [x for x in (s.get("test"), s.get("statistic")) if x]
    if "p" in s:
        parts.append(f'p {s.get("p_relation", "=")} {p_text(s["p"])}')
    if s.get("corrected"):
        parts.append(f'{s["corrected"]}-corrected')
    if "ci" in s:
        ci = s["ci"]
        level = f'{ci["level"] * 100:g}% CI' if "level" in ci else "CI"
        unit = f' {ci["unit"]}' if ci.get("unit") else ""
        parts.append(f'{level} {ci["low"]:g} to {ci["high"]:g}{unit}')
    text = ", ".join(parts)
    if s.get("about"):
        text = f'{s["about"]}: {text}'
    return text + (f' (n = {s["n"]})' if s.get("n") else "")


def by_outcome(outcomes: list[dict], root: str, attempt: dict | None = None, asked: dict | None = None) -> str:
    """Claims under a heading for each outcome, reproduced first, then partially, not reproduced and blocked."""
    html = ""
    for outcome in ("reproduced", "partially_reproduced", "not_reproduced", "blocked"):
        mine = [o for o in outcomes if o["outcome"] == outcome]
        if mine:
            html += (f'<div class="outcome-group" data-outcome="{outcome}"><h4 class="outcome-head">{chip(outcome)}'
                     f'<span class="count">{len(mine)}</span></h4>'
                     f'<ul class="claims">{"".join(claim_item(o, root, attempt, asked) for o in mine)}</ul></div>')
    return html


def claim_item(o: dict, root: str, attempt: dict | None = None, asked: dict | None = None) -> str:
    """One claim as an accordion: the outcome and statement show, the explanation opens on a click."""
    blocked = f'<span class="why">· {e(BLOCKED_BY.get(o["blocked_by"], o["blocked_by"]))}</span>' \
        if o["blocked_by"] else ""
    source = f'<span class="source">{e(o["source"])}</span>' if o["source"] else ""
    tags = '<span class="tag">verifier disagreed at first</span>' if o["disagreed"] else ""
    if o.get("assumed"):
        tags += '<span class="tag">rests on an assumption</span>'
    if asked and o["claim"] in asked:
        tags += f'<a class="tag" href="#question-{asked[o["claim"]]}">question to the reader</a>'
    if o.get("kind") == "link":
        tags += '<span class="tag">checks the link to the paper’s data</span>'
    elif o.get("data") == "with_inputs":
        tags += '<span class="tag">uses data from outside the dataset</span>'
    elif o.get("data") == "elsewhere":
        tags += f'<span class="tag">data in {e(o.get("where") or "another archive")}</span>'
    elif o.get("data") == "with_labels":
        tags += '<span class="tag">names its codes from outside the dataset</span>'
    if o.get("proposed"):
        tags += (f'<span class="tag">change to {e(OUTCOMES[o["proposed"]["outcome"]][0].lower())} '
                 f'proposed</span>')
    body = f'<p class="notes">{e(o["notes"])}</p>' if o["notes"] else ""
    if o.get("proposed"):
        body += (f'<p class="notes"><strong>Proposed after the last verification, not yet verified:</strong> '
                 f'{e(OUTCOMES[o["proposed"]["outcome"]][0].lower())}. {e(squash(o["proposed"]["reason"]))}</p>')
    changed = next((c for c in ((attempt or {}).get("reconciliation") or {}).get("outcomes", [])
                    if c["claim"] == o["claim"]), None)
    if changed:
        then = attempt["reconciliation"]["earlier"].rsplit("-", 1)[1]
        tags += f'<span class="tag">was {e(OUTCOMES[changed["earlier"]][0].lower())} in attempt {e(then)}</span>'
        body += (f'<p class="notes"><strong>Attempt {e(then)}:</strong> '
                 f'{e(OUTCOMES[changed["earlier"]][0].lower())}. {e(changed["note"])}</p>')
    if o["deviations"]:
        items = "".join(f"<li>{e(d)}</li>" for d in o["deviations"])
        body += (f'<p class="deviations-title">How the test differed from the paper’s method</p>'
                 f'<ul class="deviations">{items}</ul>')
    if not body:
        body = '<p class="notes muted">No explanation recorded.</p>'
    if o.get("statistics"):
        items = "".join(f"<li>{e(statistic_text(s))}</li>" for s in o["statistics"])
        body = f'<p class="deviations-title">What the paper reports</p><ul class="stats">{items}</ul>' + body
    if o.get("inferred"):
        body = f'<p class="inferred"><strong>Not quoted:</strong> {e(o["inferred"])}</p>' + body
    if o.get("quote"):
        cite = f'<cite>{e(o["source"])}</cite>' if o["source"] else ""
        body = f'<blockquote class="quote"><p>{e(o["quote"])}</p>{cite}</blockquote>' + body
    # The chip is not a link here: inside the summary a click should open the claim.
    return (f'<li class="claim" id="claim-{e(o["claim"])}" data-outcome="{e(o["outcome"])}"><details><summary>'
            f'<div class="claim-head">{chip(o["outcome"])}{source}{blocked}{tags}</div>'
            f'<p class="statement">{e(o["statement"])}</p></summary>'
            f'<div class="claim-body">{body}</div></details></li>')


_ROWS: dict = {}


def rows_cache(data: dict) -> dict:
    key = id(data)
    if key not in _ROWS:
        _ROWS.clear()
        _ROWS[key] = rows(data)
    return _ROWS[key]


def head_tags(data: dict, title: str, path: str, description: str, structured: dict | None) -> str:
    """The description, canonical link and social-card tags of one page.

    Links are absolute and point at the published site, also in a preview, so search engines and link previews
    resolve them to the real page. Demo and preview builds are kept out of search results.
    """
    url = SITE_URL + path
    card = SITE_URL + "assets/social-card.png"
    tags = [
        f'<meta name="description" content="{e(description)}">',
        f'<link rel="canonical" href="{e(url)}">',
        '<meta property="og:type" content="website">',
        f'<meta property="og:site_name" content="{SITE_NAME}">',
        f'<meta property="og:title" content="{e(title)}">',
        f'<meta property="og:description" content="{e(description)}">',
        f'<meta property="og:url" content="{e(url)}">',
        f'<meta property="og:image" content="{card}">',
        '<meta property="og:image:width" content="1200">',
        '<meta property="og:image:height" content="630">',
        f'<meta property="og:image:alt" content="{SITE_NAME}: can the findings of a paper be reproduced '
        'from its open data?">',
        '<meta name="twitter:card" content="summary_large_image">',
        f'<meta name="twitter:title" content="{e(title)}">',
        f'<meta name="twitter:description" content="{e(description)}">',
        f'<meta name="twitter:image" content="{card}">',
    ]
    if data["demo"] or data.get("noindex"):
        tags.append('<meta name="robots" content="noindex">')
    if structured:
        tags.append('<script type="application/ld+json">' + json.dumps(structured).replace("</", "<\\/") + "</script>")
    return "\n".join(tags)


# Page views are counted by Cloudflare Web Analytics: no cookies and nothing that identifies a visitor, so no
# consent banner. Its script is the one thing the site loads from another site, and only in a build given the
# site's token (--analytics; the publish workflow passes the CF_ANALYTICS_TOKEN repository variable), so that
# previews, demo builds and local builds count nothing.
BEACON_SRC = "https://static.cloudflareinsights.com/beacon.min.js"


def beacon(data: dict) -> str:
    token = data.get("analytics")
    if not token or data["demo"] or data.get("noindex"):
        return ""
    return f"<script defer src=\"{BEACON_SRC}\" data-cf-beacon='{e(json.dumps({'token': token}))}'></script>"


def shell(data: dict, title: str, root: str, active: str, body: str, scripts: str = "", path: str = "",
          description: str = SITE_DESCRIPTION, structured: dict | None = None) -> str:
    r = rows_cache(data)
    n_papers = sum(1 for p in papers_of(data) if p["attempts"])
    n_datasets = sum(1 for d in r["datasets"] if d["status"] == "attempted")
    tabs = [("overview", "Overview", root or "./", None), ("papers", "Papers", f"{root}papers/", n_papers),
            ("datasets", "Datasets", f"{root}datasets/", n_datasets),
            ("authors", "Authors", f"{root}authors/", None),
            ("pipeline", "Pipeline", f"{root}pipeline/", None),
            ("about", "About", f"{root}about/", None)]
    nav = ""
    for key, label, href, n in tabs:
        current = ' aria-current="page"' if key == active else ""
        count = f'<span class="n">{n:,}</span>' if n is not None else ""
        nav += f'<a class="tab" href="{href}"{current}>{label}{count}</a>'
    banner = '<div class="demo">Demo data: made-up attempts, for testing the site only</div>' if data["demo"] else ""
    home = root or "./"
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title>
{head_tags(data, title, path, description, structured)}
<script>try{{var t=localStorage.getItem("theme");if(t==="light"||t==="dark")document.documentElement.dataset.theme=t;}}catch(e){{}}</script>
<link rel="icon" href="{root}assets/favicon.svg" type="image/svg+xml">
<link rel="alternate icon" href="{root}assets/favicon-32.png" type="image/png" sizes="32x32">
<link rel="apple-touch-icon" href="{root}assets/favicon-180.png">
<link rel="stylesheet" href="{root}{asset("app.css")}"></head><body>
{banner}<nav class="top" aria-label="Sections"><div class="wrap">
  <a class="brand" href="{home}">{ENCORE_MARK}<span>{SITE_NAME}</span></a><a class="by" href="{CN_URL}">by CatalystNeuro</a><div class="tabrow" id="tabrow">{nav}
  <a class="tab icon" href="{REPO_URL}" aria-label="The registry on GitHub" title="The registry on GitHub">{GITHUB_MARK}</a>
  <a class="tab ext" href="{ENCORE_DOCS}" title="Run the same check on your own data with the encore command">Check your data</a>
  <a class="tab ext runs" href="{REPO_URL}/actions" title="The workflows that run the agents and check the entries">Agent runs</a></div>
  <button class="navtoggle" id="navtoggle" type="button" aria-expanded="false" aria-controls="tabrow" aria-label="Menu"><span aria-hidden="true"></span></button>
  <button class="theme" id="theme" type="button" aria-label="Colour theme: auto. Change theme" title="Colour theme"><span aria-hidden="true">◐</span><span class="t">Auto</span></button>
</div></nav>
<div class="wrap">
{body}
<footer>{SITE_NAME} is developed by <a href="{CN_URL}">CatalystNeuro</a>. Generated {e(data["generated"][:10])} from the registry's files ·
<a href="{root}registry.json">Data as JSON</a> · <a href="{REPO_URL}">Repository</a> ·
<a href="{REPO_URL}/actions">Agent runs</a> ·
<a href="{REPO_URL}/blob/main/docs/design.md">How it works</a>. Outcomes describe what one attempt could reproduce from
the data in the dataset, with the methods available. A failure to reproduce may be a failure of the agent, and is not
a judgement of the paper.</footer>
</div>
{THEME_JS}
{scripts}{beacon(data)}
</body></html>
'''


THEME_JS = """<script>(function(){
var b=document.getElementById('theme'),order=['auto','light','dark'],icon={auto:'\u25d0',light:'\u2600',dark:'\u263e'},
name={auto:'Auto',light:'Light',dark:'Dark'};
function get(){try{var t=localStorage.getItem('theme');return t==='light'||t==='dark'?t:'auto';}catch(e){return 'auto';}}
function show(t){b.firstChild.textContent=icon[t];b.lastChild.textContent=name[t];
b.setAttribute('aria-label','Colour theme: '+name[t].toLowerCase()+'. Change theme');b.title='Colour theme: '+name[t];}
b.addEventListener('click',function(){var t=order[(order.indexOf(get())+1)%3];
try{t==='auto'?localStorage.removeItem('theme'):localStorage.setItem('theme',t);}catch(e){}
if(t==='auto')delete document.documentElement.dataset.theme;else document.documentElement.dataset.theme=t;show(t);});
show(get());})();
(function(){var n=document.getElementById('navtoggle'),bar=n&&n.closest('nav.top');if(!n)return;
function set(o){bar.classList.toggle('open',o);n.setAttribute('aria-expanded',String(o));}
n.addEventListener('click',function(){set(!bar.classList.contains('open'));});
document.addEventListener('keydown',function(ev){if(ev.key==='Escape')set(false);});})();</script>"""


def caution_block() -> str:
    return f'''<div class="caution" id="caution">
  <p class="lead"><strong>{CAUTION}</strong> It may be a failure of the attempt.</p>
  <div class="body">
    <p>An outcome says what one attempt could recover from the data in a dataset, with the methods available to it. A
    “not reproduced” or “partially reproduced” outcome can come from a mistake or a limitation in the agent’s analysis,
    from methods the paper does not describe fully, from data that is not in the dataset, or from a dataset that
    differs from what the paper analysed. “Blocked” means the claim could not be tested at all.</p>
    <p>Most attempts are made by AI agents. Where a page says so, the attempt has been checked by a second, independent
    agent, but neither is infallible. Every attempt links to its code, its reasoning and the ways its analysis differs
    from the paper’s. Authors who think an attempt is wrong can <a href="{REPO_URL}/issues">open an issue</a>.</p>
  </div>
</div>'''


# --- pages ---------------------------------------------------------------------

def breakdown(title: str, items: list[tuple[str, int, str]], more: str | None = None) -> str:
    """A panel of horizontal bars: (label, count, link) per row."""
    if not items:
        return ""
    top = max(n for _, n, _ in items)
    body = "".join(
        f'<a class="label" href="{e(href)}">{e(label)}</a>'
        f'<div class="track"><a class="hbar" href="{e(href)}" style="width:{100 * n / top:.1f}%" '
        f'aria-label="{e(label)}: {n}"></a></div><span class="num">{n:,}</span>'
        for label, n, href in items)
    link = f'<a class="more" href="{e(more)}">See all</a>' if more else ""
    return f'<div class="panel"><h2>{link}{e(title)}</h2><div class="rows">{body}</div></div>'


def quiet_tier(tier: str) -> str:
    """Verification as the papers list shows it (list.js, check): a quiet mark when verified, its tier on hover; only
    the exception, not yet verified, spelled out."""
    if tier == "runs":
        return '<span class="tier pending">Not yet verified</span>'
    return f'<span class="verified" title="{e(TIERS[tier])}"><span aria-hidden="true">✓</span> Verified</span>'


def attempt_row(a: dict, root: str, share: bool = False, paper: dict | None = None, data: dict | None = None) -> str:
    """One attempt in a list; with `share`, the share of its claims reproduced in place of its date. Given its
    paper (papers_of), the row is the paper's, laid out as in the papers list (list.js, papers): the byline and
    journal above the title, which opens the paper's page, then its datasets and the outcomes."""
    counts = outcome_counts(a)
    side = (f'<span class="small"><b>{reproduced_share(counts):.0%}</b> reproduced</span>' if share
            else f'<span class="small muted">{e(a["date"])}</span>')
    mark = deprecated_badge() if a.get("deprecated") else quiet_tier(a["tier"]) if paper else tier_badge(a["tier"])
    if not paper:
        page = f'{root}{page_of(a["key"])}'
        return (f'<div class="row drow"><div class="id"><a href="{page}">{e(a["label"])}</a></div>'
                f'<div><p class="title"><a href="{page}">{e(a["entry_title"] or a["id"])}</a></p>'
                f'<div class="meta">{bar(counts, "Outcomes", "bar mini")}{legend(counts, compact=True)}</div></div>'
                f'<div class="right">{mark}{side}</div></div>')
    row = next((r for r in rows_cache(data)["papers"] if r["id"] == paper["key"]), {}) if data else {}
    page = f'{root}papers/{paper["key"]}/'
    sets = ", ".join(f'<a href="{root}{e(d["page"])}">{e(d["label"])}</a>' if d.get("page") else e(d["label"])
                     for d in row.get("datasets") or [])
    said = " · ".join(f"{n} {OUTCOMES[k][0].lower()}" for k, n in counts.items() if n)
    journal = f'<span class="sep" aria-hidden="true">·</span>{e(row["journal"])}' if row.get("journal") else ""
    return (f'<div class="row drow prow"><div><p class="byline">{e(paper["byline"])}{journal}</p>'
            f'<p class="title"><a href="{page}">{e(paper.get("title") or a["entry_title"] or a["id"])}</a></p>'
            + (f'<div class="meta"><span>{sets}</span></div>' if sets else "")
            + f'<div class="meta" style="margin-top:6px">{bar(counts, "Outcomes", "bar mini")}'
            f'<span class="small muted">{e(said)}</span></div></div>'
            f'<div class="right">{mark}{side}</div></div>')


def most_reproduced(attempts: list[dict], n: int = 6) -> list[dict]:
    """The verified attempts with the largest share of claims reproduced, then the most claims reproduced."""
    ranked = [a for a in attempts if not a.get("deprecated") and a["tier"] != "runs"
              and sum(outcome_counts(a).values()) >= TOP_MIN_CLAIMS]
    return sorted(ranked, key=lambda a: (-reproduced_share(outcome_counts(a)), -outcome_counts(a)["reproduced"],
                                         a["key"]))[:n]


# The archives with a colour of their own in the progress charts; the rest share one (progress_data).
OWN_COLOUR = ("dandi", "crcns")

# In the order of the Overview's tiles: papers first, as the papers are the registry's primary index.
PROGRESS_METRICS = {
    "papers": "Papers attempted",
    "claims": "Claims tested",
    "attempts": "Attempts",
    "findings": "Findings about the data",
    "datasets": "Datasets attempted",
}
PROGRESS_DEFAULT = "papers"   # the measure the charts show first


def progress_data(data: dict) -> dict:
    """Daily counts for the overview's dashboard.

    Each series is a list over the days of what was new that day: dandisets and papers on the date of their first attempt, attempts
    on their own date, and the claims (those resting on the dandiset) and findings of each dandiset's
    current attempts on the date of those attempts.
    """
    current = [a for atts in current_attempts(data).values() for a in atts]
    if not data["attempts"]:
        return {"days": [], "series": {}}
    # Attempts are also counted by the protocol version they followed, oldest version first.
    def protocol(a):
        return (a.get("agent") or {}).get("protocol") or "not recorded"

    def version_order(v):
        m = re.fullmatch(r"([a-z]+)-(\d+)", v)
        return (0, m[1], int(m[2])) if m else (1, v, 0)
    protocols = sorted({protocol(a) for a in data["attempts"]}, key=version_order)
    # Datasets are also counted by their archive. DANDI and CRCNS have a colour each (slots 1 and 2); every other
    # archive, with a few datasets each, is counted in one "other archives" series (slot 3), so that the chart
    # needs three colours, none of them an outcome's. The slot follows the archive, not its rank.
    order = list(ARCHIVES)
    present = sorted({split_key(a["key"])[0] for a in data["attempts"]}, key=lambda k: (order.index(k) if k in order else 99, k))
    archives = [k for k in OWN_COLOUR if k in present]
    others = [k for k in present if k not in OWN_COLOUR]
    if others:
        archives.append("other")
    group = lambda k: k if k in OWN_COLOUR else "other"
    start = datetime.date.fromisoformat(min(a["date"] for a in data["attempts"]))
    end = datetime.date.fromisoformat(max(a["date"] for a in data["attempts"]))
    days = [(start + datetime.timedelta(n)).isoformat() for n in range((end - start).days + 1)]
    series = {}
    for subset, keep in (("all", lambda d: True),):
        new = {day: {**{m: 0 for m in PROGRESS_METRICS}, **{k: 0 for k in OUTCOMES},
                     **{f"protocol:{v}": 0 for v in protocols}, **{f"archive:{k}": 0 for k in archives}} for day in days}
        first_dandiset: dict = {}
        first_paper: dict = {}
        for a in data["attempts"]:
            if not keep(a["key"]):
                continue
            new[a["date"]]["attempts"] += 1
            new[a["date"]][f"protocol:{protocol(a)}"] += 1
            first_dandiset[a["key"]] = min(first_dandiset.get(a["key"], a["date"]), a["date"])
            first_paper[a["paper"]] = min(first_paper.get(a["paper"], a["date"]), a["date"])
        for key, day in first_dandiset.items():
            new[day]["datasets"] += 1
            new[day][f"archive:{group(split_key(key)[0])}"] += 1
        for day in first_paper.values():
            new[day]["papers"] += 1
        for a in current:
            if not keep(a["key"]) or a.get("deprecated"):
                continue
            counts = outcome_counts(a)
            for k, n in counts.items():
                new[a["date"]][k] += n
            new[a["date"]]["claims"] += sum(counts.values())
            new[a["date"]]["findings"] += len(a["findings"])
        series[subset] = {k: [new[day][k] for day in days] for k in new[days[0]]}
    return {"days": days, "series": series, "metrics": PROGRESS_METRICS,
            "outcomes": {k: {"label": label, "css": css} for k, (label, css, _) in OUTCOMES.items()},
            "protocols": protocols,
            "archives": [{"key": k, "slot": OWN_COLOUR.index(k) + 1 if k in OWN_COLOUR else len(OWN_COLOUR) + 1,
                          "label": (ARCHIVES[k]["name"].removeprefix("the ") if k != "other" else
                                    "Other archives (" + ", ".join(ARCHIVES[o]["name"].removeprefix("the ")
                                                                   if o in ARCHIVES else o for o in others) + ")")}
                         for k in archives]}


def progress_panel(data: dict) -> str:
    """The dashboard at the top of the overview: totals and two charts of the effort over time.

    The page draws the charts from the JSON it carries (assets/progress.js); without scripts, the table
    below them gives the same numbers.
    """
    p = progress_data(data)
    if len(p["days"]) < 2:
        return ""
    totals = {m: sum(p["series"]["all"][m]) for m in PROGRESS_METRICS}
    tiles = "".join(
        f'<button class="tile metric" type="button" data-metric="{m}" aria-pressed="{str(m == PROGRESS_DEFAULT).lower()}">'
        f'<div class="n">{totals[m]:,}</div><div class="l">{e(label)}</div><div class="delta"></div></button>'
        for m, label in PROGRESS_METRICS.items())
    rows = "".join(
        f"<tr><td>{day}</td>" + "".join(f"<td>{p['series']['all'][m][i]:,}</td>" for m in PROGRESS_METRICS) + "</tr>"
        for i, day in enumerate(p["days"]))
    head = "".join(f"<th>{e(label)}</th>" for label in PROGRESS_METRICS.values())
    return f'''<section class="progress" aria-label="Progress over time">
  <div class="progress-bar">
    <span class="muted small">Totals so far; the small line is the last 7 days.</span>
  </div>
  <div class="tiles metrics">{tiles}</div>
  <div class="panel progress-charts">
    <div class="grid2">
      <div><h2 id="progress-title">{e(PROGRESS_METRICS[PROGRESS_DEFAULT])} over time</h2>
        <p class="small muted" style="margin:0">Running total, by day.</p>
        <div class="chart" id="progress-line"></div></div>
      <div><h2 id="progress-day-title">{e(PROGRESS_METRICS[PROGRESS_DEFAULT])}, new each day</h2>
        <p class="small muted" style="margin:0" id="progress-day-note">Each paper on the date of its first attempt.</p>
        <div class="chart" id="progress-outcomes"></div></div>
    </div>
    <div id="progress-legend" class="progress-legend"></div>
  </div>
  <details class="table-view panel"><summary>Table: new each day</summary>
    <div class="scroll"><table><thead><tr><th>Date</th>{head}</tr></thead><tbody>{rows}</tbody></table></div>
  </details>
  <script type="application/json" id="progress-data">{json.dumps(p, separators=(",", ":"))}</script>
</section>'''


def page_overview(data: dict) -> str:
    r = rows_cache(data)
    current = current_attempts(data)
    attempts = [a for atts in current.values() for a in atts]
    counts = outcome_counts(attempts)
    n_claims = sum(counts.values())
    in_queue = data["queue_counts"]["with_a_paper"]
    verified = sum(1 for atts in current.values() if weakest_tier(atts) != "runs")
    n_papers = sum(1 for q in papers_of(data) if q["attempts"])
    tiles = [
        (f"{n_papers:,}", "papers attempted", "papers/?status=attempted"),
        (f'{len(current):,} <span class="of">of {in_queue}</span>', "datasets attempted", "datasets/"),
        (f"{n_claims:,}", "claims attempted", "papers/?status=attempted"),
        (f"{verified:,}", "datasets independently verified",
         "papers/?tier=agent_verified,human_verified,author_endorsed"),
        (f'{len(r["findings"]):,}', "findings about the data", "datasets/"),
    ]
    tile_html = "".join(f'<a class="tile" href="{href}"><div class="n">{n}</div><div class="l">{e(label)}</div></a>'
                        for n, label, href in tiles)

    if n_claims:
        outcomes = (bar(counts, f"Outcomes of {n_claims} claims", href=lambda k: f"papers/?has={k}")
                    + legend(counts, href=lambda k: f"papers/?has={k}"))
    else:
        outcomes = '<p class="muted">No claims attempted yet.</p>'

    by_technique: dict = {}
    for c in r["claims"]:
        for t in c["technique"] or ["(none)"]:
            by_technique.setdefault(t, {k: 0 for k in OUTCOMES})[c["outcome"]] += 1
    technique_rows = ""
    for t, c in sorted(by_technique.items(), key=lambda kv: -sum(kv[1].values()))[:8]:
        label = "Not stated" if t == "(none)" else t
        technique_rows += (
            f'<a class="label" href="papers/?status=attempted&technique={e(t)}">{e(label)}</a>'
            + bar(c, f"{label}: {sum(c.values())} claims", href=lambda k, t=t: f"papers/?technique={t}&has={k}")
            + f'<span class="num">{sum(c.values()):,}</span>')
    technique_panel = (f'<div class="panel"><h2>Outcomes by technique</h2><div class="rows">{technique_rows}</div></div>'
                       if technique_rows else "")

    blocked: dict = {}
    for c in r["claims"]:
        if c["outcome"] == "blocked":
            blocked[c["blocked_by"]] = blocked.get(c["blocked_by"], 0) + 1
    kinds: dict = {}
    for f in r["findings"]:
        kinds[f["kind"]] = kinds.get(f["kind"], 0) + 1
    tiers: dict = {}
    for atts in current.values():
        tier = weakest_tier(atts)
        tiers[tier] = tiers.get(tier, 0) + 1

    def ordered(counts_by_key, labels, link):
        return [(labels.get(k, k), n, link(k)) for k, n in sorted(counts_by_key.items(), key=lambda kv: -kv[1])]

    panels = "".join([
        technique_panel,
        breakdown("Why claims could not be tested",
                  ordered(blocked, BLOCKED_BY, lambda k: f"papers/?blocked_by={k}"),
                  "papers/?has=blocked"),
        breakdown("Findings about the data", ordered(kinds, FINDING_KINDS, lambda k: f"datasets/?found={k}"),
                  "datasets/"),
        breakdown("Verification of attempted datasets",
                  ordered(tiers, TIERS, lambda k: f"papers/?status=attempted&tier={k}"),
                  "papers/?status=attempted"),
    ])

    paper_for = {q["doi"]: q for q in papers_of(data) if q["attempts"]}
    its = lambda a: paper_for.get(a["paper"].lower())

    def once_a_paper(rows: list[dict], n: int = 6) -> list[dict]:
        """The first n, a paper once: an attempt on several datasets is a row for each of them here."""
        seen, out = set(), []
        for a in rows:
            key = (its(a) or {}).get("key") or a["id"]
            if key not in seen:
                seen.add(key)
                out.append(a)
        return out[:n]
    recent = once_a_paper(sorted(attempts, key=lambda a: (a["date"], a["key"]), reverse=True))
    recent_html = "".join(attempt_row(a, "", paper=its(a), data=data) for a in recent) or '<p class="empty">No attempts yet.</p>'
    top_html = ("".join(attempt_row(a, "", share=True, paper=its(a), data=data)
                        for a in once_a_paper(most_reproduced(attempts, n=24)))
                or '<p class="empty">No verified attempt yet.</p>')

    dashboard = progress_panel(data)
    redirect = json.dumps({a["id"]: attempt_path(data, a) for a in data["attempts"]})
    body = f'''<header class="page" id="top">
  <div class="eyebrow">The Encore registry</div>
  <h1>Can the findings of a paper be reproduced from its open data?</h1>
  <p class="lede">AI agents try to reproduce the key findings of papers from their open data. Independent agents check
  each attempt, and every finding gets
  an outcome, whether or not it reproduced. <a href="about/">How it works</a> ·
  <a href="{ENCORE_DOCS}">Run the same check on your own data</a></p>
  {"" if dashboard else f'<div class="tiles">{tile_html}</div>'}
</header>
<main>
  {dashboard}
  <div class="panel">
    <h2>Outcomes of the {n_claims:,} claims that rest on the dataset alone</h2>
    {outcomes}{outside_note(attempts, collapsed=True)}
    {caution_block()}
  </div>
  <div class="grid2" style="margin-top:16px">{panels}</div>
  <div class="panel attempts" style="padding:0">
    <div class="tabs" role="tablist"><button type="button" role="tab" data-panel="most-reproduced" aria-selected="true">Most
      reproduced</button><button type="button" role="tab" data-panel="latest" aria-selected="false">Latest</button></div>
    <section class="tabpanel" id="most-reproduced"><h2>Most reproduced</h2>
      <p class="sub small"><a class="more" href="papers/?status=attempted&amp;sort=-reproduced">See all</a>Verified
      attempts with at least {TOP_MIN_CLAIMS} claims on the dataset, by the share of claims reproduced; a partial
      reproduction counts as half.</p>
      <div class="results">{top_html}</div></section>
    <section class="tabpanel" id="latest"><h2>Latest attempts</h2>
      <p class="sub small"><a class="more" href="papers/?status=attempted&amp;sort=-date">See all</a>The most recent attempts,
      verified or not.</p>
      <div class="results">{recent_html}</div></section>
  </div>
</main>'''
    scripts = ('<script>(function(){var m=' + redirect + ',h=location.hash.match(/^#attempt-(.+)$/);'
               'if(h&&m[h[1]])location.replace(m[h[1]]);})();</script>'
               + TABS_JS + (f'<script src="{asset("progress.js")}"></script>' if dashboard else ""))
    structured = {
        "@context": "https://schema.org", "@type": "WebSite", "name": SITE_NAME, "alternateName": "The Encore registry",
        "url": SITE_URL, "description": SITE_DESCRIPTION,
        "publisher": {"@type": "Organization", "name": "CatalystNeuro", "url": "https://www.catalystneuro.com"},
    }
    return shell(data, f"{SITE_NAME}: can the findings of a paper be reproduced from its open data?", "",
                 "overview", body, scripts, path="", structured=structured)


ABOUT_STEPS = [
    ("Choose a target",
     "The queue holds every public dataset whose metadata names a paper; so far all come from the DANDI Archive, the only archive the registry reads yet. Datasets converted "
     "by CatalystNeuro go first."),
    ("Write down the claims",
     "An author agent reads the paper and records its key findings as claims, each with the numbers it rests on, a "
     "tolerance, and the test that will decide it. The claims are written before any analysis is run."),
    ("Check the data and test each claim",
     "The author checks the dataset against its own description, then writes a notebook that streams the data from "
     "the archive and tests each claim. Every claim gets an outcome: reproduced, partially reproduced, not reproduced, "
     "or blocked, with the reason. What the author learns about the data along the way is recorded as findings."),
    ("First verification",
     "A second agent, in a separate run that has not seen the author's reasoning or conclusions, reviews the notebook "
     "and the paper and decides its own outcome for each claim. The author then answers each point, revising the "
     "analysis where needed."),
    ("Second verification",
     "The verifier sees the author's conclusions, checks every sentence of them against the outputs, and says whether "
     "it agrees with each outcome. The author revises once more. Any change of outcome proposed after this goes to a "
     "third round that reviews only those changes."),
    ("Record and publish",
     "The attempt is added to the registry's records. The notebook runs again in a clean environment, "
     "and once the checks pass the attempt is merged and appears here."),
]


PIPELINE_STATES = [("done", "Done"), ("older", "Made before the step existed"), ("waiting", "Waiting on a person"),
                   ("deprecated", "To redo"), ("todo", "To do")]
# Questions arise only during an attempt, so they are in the table, not the chart.
CHART_STEPS = [(k, label) for k, label in PAPER_STEPS if k != "questions"]


def chart_state(key: str, state: str, note: str) -> str:
    """A cell's state as the chart counts it: a step not reached yet is still to do."""
    if key == "check" and state == "none" and note == "before checks":
        return "older"
    return "todo" if state == "none" else state


def pipeline_chart(counts: dict, total: int) -> str:
    """One bar per step, out of every paper: done, made before the step, waiting on a person, to redo, to do."""
    rows = ""
    for key, label in CHART_STEPS:
        c = counts[key]
        segs = "".join(f'<span class="seg st-{st}" style="width:{100 * c[st] / total:.2f}%" '
                       f'data-tip="{e(name)}: {c[st]:,}"></span>' for st, name in PIPELINE_STATES if c.get(st))
        parts = ", ".join(f"{c[st]:,} {name.lower()}" for st, name in PIPELINE_STATES[1:] if c.get(st))
        done = c.get("done", 0) + c.get("older", 0)
        rows += (f'<div class="frow"><span class="flabel">{e(label)}</span>'
                 f'<span class="fbar" role="img" aria-label="{e(label)}: {c.get("done", 0):,} of {total:,} done'
                 f'{", " + parts if parts else ""}">{segs}</span>'
                 f'<span class="fcount"><strong>{done:,}</strong> of {total:,}</span></div>')
    legend = "".join(f'<span><i class="seg st-{st}"></i>{e(name)}</span>' for st, name in PIPELINE_STATES)
    return (f'<div class="panel"><h2>Papers at each step</h2><div class="funnel">{rows}</div>'
            f'<p class="flegend small">{legend}</p></div>')


TABLE_STATES = [("done", "Done"), ("waiting", "Waiting on a person"), ("deprecated", "To redo"),
                ("todo", "To do"), ("none", "Not applicable")]

# Filters, sorts and pages the pipeline table in place. Sorting a step's column orders its rows by state
# (done first), then by the cell's note.
PIPELINE_TABLE_JS = r"""
(function(){
var table=document.querySelector('table.pipeline'),tools=document.querySelector('.pipeline-tools');
if(!table||!tools)return;tools.hidden=false;
var tbody=table.tBodies[0],rows=[].slice.call(tbody.rows),ths=[].slice.call(table.tHead.rows[0].cells);
var steps=[].slice.call(document.getElementById('pstep').options,1).map(function(o){return o.value;});
var rank={done:0,waiting:1,deprecated:2,todo:3,none:4};
var state={q:'',step:'',st:'',col:-1,dir:1,page:1,size:50};
var $=function(id){return document.getElementById(id);};
function key(tr,col){var td=tr.cells[col],t=td.textContent.trim();
  if(td.dataset.sort!==undefined)return [0,td.dataset.sort];
  return td.classList.contains('ps')?[rank[td.className.split(' ')[1]],t]:[0,t];}
function cmp(a,b){return a[0]-b[0]||a[1].localeCompare(b[1],undefined,{numeric:true,sensitivity:'base'});}
function shown(tr){
  if(state.q&&(tr.cells[0].textContent+' '+tr.cells[1].textContent+' '+tr.cells[2].textContent).toLowerCase().indexOf(state.q)<0)return false;
  var keys=state.step?[state.step]:steps;
  if(state.st)return keys.some(function(k){return tr.dataset[k]===state.st;});
  return true;}
function draw(){
  var list=rows.filter(shown);
  if(state.col>=0)list.sort(function(a,b){return state.dir*cmp(key(a,state.col),key(b,state.col));});
  var pages=Math.max(1,Math.ceil(list.length/state.size));if(state.page>pages)state.page=pages;
  var start=(state.page-1)*state.size,page=list.slice(start,start+state.size);
  rows.forEach(function(tr){tr.hidden=true;});
  page.forEach(function(tr){tr.hidden=false;tbody.appendChild(tr);});
  ths.forEach(function(th,i){if(i===state.col)th.setAttribute('aria-sort',state.dir>0?'ascending':'descending');
    else th.removeAttribute('aria-sort');});
  $('pcount').textContent=list.length===rows.length?rows.length.toLocaleString()+' papers'
    :list.length.toLocaleString()+' of '+rows.length.toLocaleString()+' papers';
  var el=$('ppager');if(!list.length){el.innerHTML='';return;}
  var nums=[1,pages,state.page-1,state.page,state.page+1].filter(function(p,i,a){return p>=1&&p<=pages&&a.indexOf(p)===i;})
    .sort(function(a,b){return a-b;}),last=0,buttons='';
  nums.forEach(function(p){if(p-last>1)buttons+='<span class="muted">…</span>';
    buttons+='<button type="button" data-page="'+p+'"'+(p===state.page?' aria-current="page"':'')+'>'+p+'</button>';last=p;});
  el.innerHTML='<span class="muted">'+(start+1)+'–'+(start+page.length)+' of '+list.length.toLocaleString()+'</span><span class="grow"></span>'
    +'<button type="button" data-page="'+(state.page-1)+'"'+(state.page===1?' disabled':'')+' aria-label="Previous page">‹</button>'+buttons
    +'<button type="button" data-page="'+(state.page+1)+'"'+(state.page===pages?' disabled':'')+' aria-label="Next page">›</button>'
    +'<select class="ghost" id="psize" aria-label="Rows per page">'+[25,50,100,250].map(function(s){
      return '<option value="'+s+'"'+(s===state.size?' selected':'')+'>'+s+' per page</option>';}).join('')+'</select>';}
var timer;
$('pq').addEventListener('input',function(){clearTimeout(timer);timer=setTimeout(function(){
  state.q=$('pq').value.trim().toLowerCase();state.page=1;draw();},120);});
$('pstep').addEventListener('change',function(){state.step=this.value;state.page=1;draw();});
$('pstate').addEventListener('change',function(){state.st=this.value;state.page=1;draw();});
table.tHead.addEventListener('click',function(ev){var b=ev.target.closest('button.sort');if(!b)return;
  var col=ths.indexOf(b.closest('th'));state.dir=col===state.col?-state.dir:1;state.col=col;state.page=1;draw();});
$('ppager').addEventListener('click',function(ev){var b=ev.target.closest('[data-page]');if(!b||b.disabled)return;
  state.page=+b.dataset.page;draw();table.scrollIntoView({block:'start'});});
$('ppager').addEventListener('change',function(ev){if(ev.target.id==='psize'){state.size=+ev.target.value;state.page=1;draw();}});
draw();
})();
"""


def sort_button(label: str) -> str:
    return f'<button class="sort" type="button">{e(label)}</button>'


def page_pipeline(data: dict) -> str:
    """Where every paper stands in the pipeline, and what is waiting on a person."""
    root = "../"
    rows = paper_pipeline_rows(data)
    counts = {key: {} for key, _ in PAPER_STEPS}
    for r in rows:
        for key, _ in PAPER_STEPS:
            st = r["state"][key][0]
            counts[key][st] = counts[key].get(st, 0) + 1
    # Claims files made before the check existed count as checked, as in the chart.
    older = {key: sum(1 for r in rows if chart_state(key, *r["state"][key]) == "older") for key, _ in PAPER_STEPS}
    head = "".join(f'<th>{sort_button(label)}<div class="small muted">{counts[key].get("done", 0) + older[key]:,} done'
                   + (f', {counts[key]["waiting"]:,} waiting' if counts[key].get("waiting") else "")
                   + "</div></th>" for key, label in PAPER_STEPS)
    body = ""
    for r in rows:
        label = r["byline"] or r["paper"] or "Not matched yet"
        name = (f'<a href="{root}{e(r["page"])}">{e(label)}</a>' if r["page"]
                else e(label) if r["paper"] else f'<span class="muted">{e(label)}</span>')
        sets = ", ".join(f'<a href="{root}{e(d["page"])}">{e(d["label"])}</a>' if d["page"] else e(d["label"])
                         for d in r["datasets"])
        if r["relation"] == ["reuses"]:
            sets += ' <span class="muted">(reused)</span>'
        cells = "".join(f'<td class="ps {e(r["state"][key][0])}" title="{e(r["state"][key][0])}">'
                        f'{e(r["state"][key][1])}</td>' for key, _ in PAPER_STEPS)
        states = " ".join(f'data-{key}="{e(r["state"][key][0])}"' for key, _ in PAPER_STEPS)
        q = r["queue"]
        if r["running"]:
            place, sort = "running now", -1
            when, hours = in_hours(r["running"]["hours"]), r["running"]["hours"]
        elif r["branch"]:
            place, sort, when, hours = "branch open", 0, "", None
        elif q:
            place = f'{q["place"]:,} for {"an attempt" if q["kind"] == "full" else "claims"}'
            sort = q["place"] + (0 if q["kind"] == "full" else 100000)
            when, hours = in_hours(q["hours"]), q["hours"]
        else:
            place, sort, when, hours = "", 999999, "", None
        body += (f'<tr {states}><td>{name}</td>'
                 f'<td class="pname">{e(r["title"])}</td><td class="small psets">{sets}</td>{cells}<td class="small">{e(r["next"])}'
                 + (f' · <a href="{e(r["issue"])}">waiting on you</a>' if r["issue"] else "") + '</td>'
                 f'<td class="small" data-sort="{sort}">{e(place)}</td>'
                 f'<td class="small" data-sort="{999999 if hours is None else round(hours * 10)}">{e(when)}</td></tr>')
    waiting = [r for r in rows if r["waiting"]]
    papers_missing = sum(len(r["missing"]) for r in waiting)
    charted = {key: {} for key, _ in PAPER_STEPS}
    # A dataset no paper matches (confirmed) stays in the table and out of the chart: it has no step to do.
    in_chart = [r for r in rows if r["state"]["match"][0] != "none"]
    for r in in_chart:
        for key, _ in PAPER_STEPS:
            st = chart_state(key, *r["state"][key])
            charted[key][st] = charted[key].get(st, 0) + 1
    chart = pipeline_chart(charted, max(len(in_chart), 1))
    step_opts = "".join(f'<option value="{key}">{e(label)}</option>' for key, label in PAPER_STEPS)
    state_opts = "".join(f'<option value="{st}">{e(name)}</option>' for st, name in TABLE_STATES)
    updated = datetime.datetime.fromisoformat(data["generated"]).strftime("%Y-%m-%d %H:%M UTC")
    q = data.get("queue") or {}
    queue_note = ""
    if q.get("full") is not None:
        hours, lanes = q.get("hours") or {}, q.get("lanes") or {}
        named = q.get("papers") or q   # the queue by paper, when it is given so
        def part(kind: str, what: str) -> str:
            n, h, k = len(named.get(kind, [])), hours.get(kind), lanes.get(kind, 1)
            each = (f", at about {h:.1f} hours each" if h and h >= 1 else f", at about {round(h * 60)} minutes each" if h
                    else "")
            return (f'{n:,} paper{" waits" if n == 1 else "s wait"} for {what} on {k} lane{"s" if k != 1 else ""}{each}'
                    + (f', about {in_hours(n * h / k).removeprefix("about ")} in all' if h and n else ""))
        n_going = len(named.get("running") or {})
        going_note = (f' {n_going:,} chain{" is" if n_going == 1 else "s are"} running now, and the Done in column '
                      'estimates when each will finish from how long the rest of a chain usually takes after the '
                      'role it is on. A branch with nothing running is waiting, on a person or a merge, and has no '
                      'estimate.' if "running" in q else "")
        queue_note = (f' {part("full", "an attempt")}, and {part("claims", "their claims to be read")}. '
                      'The Queue and Done in columns give each paper’s place and a rough estimate of when it '
                      f'will be done, counted from the last update.{going_note}')
    n_issues = len(data.get("issues_by_name") or data.get("issues", {}))
    issues_note = (f' The runner has stopped on <a href="{REPO_URL}/issues?q=is%3Aissue+is%3Aopen+label%3Aneeds-you">'
                   f'{n_issues:,} paper{"s" if n_issues != 1 else ""}</a> that need{"s" if n_issues == 1 else ""} a '
                   'person.' if n_issues else "")
    html_ = f'''<header class="page">
  <h1>Pipeline</h1>
  <p class="lede">Every paper, and where it stands in the
  <a href="{REPO_URL}/blob/main/docs/pipeline.md">pipeline</a>: the match to its datasets, its text, the claims
  read from it and their check, the attempt, the questions it raised, and verification. A dataset whose paper
  match is still to make is listed under the paper its archive names. {len(waiting):,}
  paper{"s are" if len(waiting) != 1 else " is"} waiting on a person, {papers_missing:,} of them for a text to
  supply; the list of missing texts is in
  <a href="{REPO_URL}/blob/main/papers/manifest.yaml">papers/manifest.yaml</a>.{issues_note}{queue_note}</p>
  <p class="small muted">Last updated <time id="updated" datetime="{e(data["generated"])}">{e(updated)}</time>.
  The page is rebuilt whenever main changes.</p>
</header>
<main>{chart}
<div class="listbar pipeline-tools" style="margin-top:16px" hidden>
  <input id="pq" type="search" placeholder="Search papers and datasets" aria-label="Search papers and datasets">
  <select class="ghost" id="pstep" aria-label="Step"><option value="">Any step</option>{step_opts}</select>
  <select class="ghost" id="pstate" aria-label="State"><option value="">Any state</option>{state_opts}</select>
  <strong id="pcount" aria-live="polite"></strong>
</div>
<div class="panel pipeline-wrap"><table class="pipeline">
<thead><tr><th>{sort_button("Paper")}</th><th>{sort_button("Title")}</th><th>{sort_button("Datasets")}</th>{head}<th>{sort_button("Next")}</th><th>{sort_button("Queue")}</th><th>{sort_button("Done in")}</th></tr></thead>
<tbody>{body}</tbody></table></div>
<nav class="pager" id="ppager" aria-label="Pages"></nav></main>
<script>
(function(){{var t=document.getElementById("updated");if(!t)return;
var m=Math.round((Date.now()-new Date(t.getAttribute("datetime")))/60000);if(isNaN(m)||m<0)return;
var ago=m<1?"just now":m<60?m+" minute"+(m==1?"":"s")+" ago":m<2880?Math.round(m/60)+" hours ago":Math.round(m/1440)+" days ago";
t.textContent+=" ("+ago+")";}})();
</script>
<script>{PIPELINE_TABLE_JS}</script>'''
    return shell(data, "Pipeline", root, "pipeline", html_, path="pipeline/",
                 description="Where every paper of the reproduction registry stands in its pipeline.")


def page_about(data: dict) -> str:
    """How an attempt is made: the agents, their roles, and where they run."""
    root = "../"
    steps = "".join(f'<li><h3>{e(head)}</h3><p>{e(text)}</p></li>' for head, text in ABOUT_STEPS)
    body = f'''<header class="page">
  <h1>How the registry works</h1>
  <p class="lede">Every attempt here is made by AI agents, in a fixed sequence of roles, following a
  <a href="{REPO_URL}/blob/main/docs/protocol.md">written protocol</a>. The author and the verifiers are separate runs
  that do not share their reasoning.</p>
</header>
<main class="about">
  <div class="panel"><h2>An attempt, step by step</h2><ol class="steps">{steps}</ol></div>
  <div class="grid2" style="margin-top:16px">
    <div class="panel"><h2>Where the agents run</h2>
      <p>Each role runs in GitHub Actions on a fresh machine with no personal configuration. The agent's commands
      cannot see the credentials it runs on, and a verifier sees only the materials it is given: the repository is
      removed before it starts. Each run commits its work, its cleaned transcript and its report, so every step can
      be read afterwards in the <a href="{REPO_URL}/tree/main/transcripts">transcripts</a> and the
      <a href="{REPO_URL}/actions">agent runs</a>.</p></div>
    <div class="panel"><h2>Reading an outcome</h2>
      <p>An outcome says what one attempt could recover from the data in a dataset, with the methods available to it.
      A failure to reproduce may be a failure of the attempt, and is not a finding that the paper is wrong. Claims that
      also use data from outside the dataset, or that rest on data the paper deposited in another archive, are counted
      apart. <a href="{root}#caution">More on reading outcomes</a></p></div>
    <div class="panel"><h2>Repeat attempts</h2>
      <p>When a dataset changes, for example after its data are corrected, or when the protocol changes, a new attempt
      can be made on the same paper. The author agent then reports, for each earlier finding, whether it is fixed,
      partly fixed or still present. Earlier attempts stay in the record.</p></div>
    <div class="panel"><h2>Disagreeing with an attempt</h2>
      <p>The agents make mistakes. If you are an author of a paper here, or know the data, and think an attempt is
      wrong, <a href="{REPO_URL}/issues">open an issue</a> on the registry. Every attempt links to its notebook, its
      claims and the reasoning behind each outcome.</p></div>
  </div>
</main>'''
    return shell(data, f"How the registry works · {SITE_NAME}", root, "about", body, path="about/",
                 description="How AI agents attempt to reproduce papers from their open data on the DANDI Archive: "
                             "the claims, the author and verifier roles, and where the agents run.")


# The site's lists. Only the papers list is a page (INDEX_LISTS): since 2026-11-11 the papers are the one index,
# and a dataset's page is reached from its papers. The datasets rows are still written as data (data/datasets.json).
INDEX_LISTS = ("papers", "datasets", "authors")
LISTS = {
    "papers": {
        "title": "Papers", "noun": "papers", "data": "data/papers.json",
        "intro": "Every paper the registry tests, on the datasets its data are in: the paper the data were published "
                 "with, or a paper that reuses them. Each opens the page of its results: every claim and its "
                 "outcome, the notebooks, what was found about the data, and the verification. Search finds a "
                 "paper by its datasets too, by identifier or by name.",
        "facets": [("status", "Status"), ("journal", "Journal"), ("relation", "Data"), ("archive", "Archive"),
                   ("has", "Has a claim that is"), ("blocked_by", "Has a claim blocked by"), ("tier", "Verification"),
                   ("found", "Findings about the data"), ("converted", "Converted by"),
                   ("technique", "Technique"), ("species", "Species")],
        "sorts": [("-reproduced", "Most reproduced"), ("-date", "Most recently attempted"), ("byline", "First author"),
                  ("-failures", "Most claims not reproduced"), ("-n_datasets", "Most datasets"), ("title", "Title")],
        "csv": None,
    },
    # The datasets list is for the people who look after the data: a dataset's owner, or a curator of its archive.
    # It has the datasets an attempt has used (`only`), each with the version tested and the open findings about its
    # data. The papers list is where a reader looks for results.
    "datasets": {
        "title": "Datasets", "noun": "datasets", "data": "data/datasets.json", "only": {"status": ["attempted"]},
        "intro": "Every dataset an attempt has used, with the version it was tested on and what the attempts found "
                 "about the data themselves: a missing identifier, an error in the metadata, a file that does not "
                 "read. For a dataset&rsquo;s owner and the curators of its archive. Results on a paper&rsquo;s "
                 "claims are in the <a href=\"../papers/\">papers list</a>.",
        "facets": [("archive", "Archive"), ("found", "Open findings"), ("tested", "Tested on"),
                   ("converted", "Converted by"), ("technique", "Technique"), ("species", "Species")],
        "sorts": [("-findings", "Most open findings"), ("-date", "Most recently tested"), ("id", "Identifier"),
                  ("-id", "Identifier, newest first"), ("-size_gb", "Largest"), ("size_gb", "Smallest"),
                  ("name", "Title")],
        "csv": None,
    },
}


# The authors list: everyone with an ORCID iD among the authors of a paper in the registry.
LISTS["authors"] = {
    "title": "Authors", "noun": "authors", "data": "data/authors.json",
    "intro": "Everyone with an ORCID iD among the authors of a paper in the registry. Each opens a page with all of "
             "their papers here. Authors are found by ORCID iD, as OpenAlex records them: a name alone does not say "
             "who it is, so an author without an iD is named on the paper&rsquo;s page and has no page here.",
    "facets": [("attempted", "Papers")],
    "sorts": [("-n_papers", "Most papers"), ("family", "Family name"), ("name", "Given name"),
              ("-n_attempted", "Most papers attempted")],
    "csv": None,
}


def page_list(data: dict, kind: str) -> str:
    spec = LISTS[kind]
    outcome_labels = {k: v[0] for k, v in OUTCOMES.items()}
    config = {
        "kind": kind, "root": "../", "data": spec["data"], "noun": spec["noun"], "csv": spec["csv"],
        "only": spec.get("only"),
        "facets": [{"key": k, "label": label} for k, label in spec["facets"]],
        "sorts": [{"key": k, "label": label} for k, label in spec["sorts"]],
        "outcomes": {k: list(v) for k, v in OUTCOMES.items()},
        "order": {"outcome": list(OUTCOMES), "has": list(OUTCOMES), "tier": list(TIERS),
                  "status": ["attempted", "claims", "open"] if kind == "papers" else list(STATUS),
                  "journal": journal_order(rows_cache(data)[kind])},
        "labels": {
            "outcome": outcome_labels, "has": {**outcome_labels, "(none)": "Not attempted"},
            "blocked_by": {**BLOCKED_BY, "(none)": "No blocked claim"},
            "tier": {**TIERS, "runs": "Not yet verified", "(none)": "Not attempted"},
            "status": {**STATUS, "claims": "Claims read, not yet attempted"} if kind == "papers" else STATUS,
            "found": {**FINDING_KINDS, "(none)": "None recorded"},
            "tested": {**VERSION_STATES, "(none)": "Attempt set aside, to redo"},
            "attempted": {"yes": "Has a paper attempted", "no": "None attempted yet"},
            "relation": {"primary": "Its own data", "reuses": "Reused data"},
            "converted": {"catalystneuro": "CatalystNeuro", "other": "Others or not stated"},
            "verifier": {"disagreed": "Disagreed at first", "(none)": "No disagreement"},
            "technique": {"(none)": "Not stated"}, "species": {"(none)": "Not stated"},
            "archive": {k: a["name"].removeprefix("the ") for k, a in ARCHIVES.items()},
        },
    }
    export = '<button class="ghost" id="export" type="button">Download CSV</button>' if spec["csv"] else ""
    body = f'''<header class="page">
  <h1>{e(spec["title"])}</h1>
  <p class="sub">{spec["intro"]}</p>
</header>
<main class="layout">
  <details class="facets" id="facets" open><summary>Filters</summary><div id="facet-list"></div></details>
  <div>
    <div class="listbar">
      <input id="q" type="search" placeholder="Search {e(spec["noun"])}" aria-label="Search {e(spec["noun"])}">
      <select class="ghost" id="sort" aria-label="Sort by"></select>
      {export}
    </div>
    <div class="listbar"><strong id="count" aria-live="polite"></strong><span class="grow"></span>
      <button class="ghost" id="clear" type="button" hidden>Clear filters</button></div>
    <div class="active" id="active"></div>
    <div class="results" id="results"><p class="empty">Loading…</p></div>
    <nav class="pager" id="pager" aria-label="Pages"></nav>
    <noscript><p class="empty">This list needs JavaScript. The same data is in
    <a href="../{spec["data"]}">{spec["data"]}</a>.</p></noscript>
  </div>
</main>'''
    scripts = (f'<script type="application/json" id="list-config">{json.dumps(config)}</script>'
               f'<script src="../{asset("list.js")}"></script>')
    return shell(data, f'{spec["title"]} · {SITE_NAME}', "../", kind, body, scripts, path=f"{kind}/",
                 description=html.unescape(re.sub(r"<[^>]+>", "", spec["intro"])))


CLAIMS_JS = """<script>(function(){
// Claims tab: show claims by outcome and 20 to a page. Without this script every claim shows.
var panel=document.getElementById('claims'),bar=document.getElementById('claim-filter'),
pager=document.getElementById('claim-pager');if(!panel||!bar)return;
var PER=20,items=[].slice.call(panel.querySelectorAll('li.claim')),state={f:'all',p:0},
labels=[['all','All'],['reproduced','Reproduced'],['partially_reproduced','Partially reproduced'],
['not_reproduced','Not reproduced'],['blocked','Blocked']];
function match(li){return state.f==='all'||li.dataset.outcome===state.f;}
function n(k){return items.filter(function(li){return k==='all'||li.dataset.outcome===k;}).length;}
bar.innerHTML=labels.filter(function(l){return l[0]==='all'||n(l[0]);}).map(function(l){
return '<button type="button" data-f="'+l[0]+'">'+l[1]+' <span class="count">'+n(l[0])+'</span></button>';}).join('');
function draw(){var shown=items.filter(match),pages=Math.max(1,Math.ceil(shown.length/PER));
if(state.p>=pages)state.p=pages-1;var page=shown.slice(state.p*PER,(state.p+1)*PER);
items.forEach(function(li){li.hidden=page.indexOf(li)<0;});
[].slice.call(panel.querySelectorAll('.claim-group,.outcome-group')).forEach(function(g){
g.hidden=!g.querySelector('li.claim:not([hidden])');});
[].slice.call(bar.querySelectorAll('button')).forEach(function(b){b.setAttribute('aria-pressed',b.dataset.f===state.f);});
if(pages<2){pager.innerHTML='';return;}
var html='<span class="muted">'+(state.p*PER+1)+'–'+(state.p*PER+page.length)+' of '+shown.length+'</span><span class="grow"></span>'+
'<button type="button" data-p="'+(state.p-1)+'"'+(state.p===0?' disabled':'')+' aria-label="Previous page">‹</button>';
for(var i=0;i<pages;i++)html+='<button type="button" data-p="'+i+'"'+(i===state.p?' aria-current="page"':'')+'>'+(i+1)+'</button>';
pager.innerHTML=html+'<button type="button" data-p="'+(state.p+1)+'"'+(state.p===pages-1?' disabled':'')+' aria-label="Next page">›</button>';}
bar.addEventListener('click',function(ev){var b=ev.target.closest('button');if(!b)return;state.f=b.dataset.f;state.p=0;draw();});
pager.addEventListener('click',function(ev){var b=ev.target.closest('button');if(!b||b.disabled)return;
state.p=+b.dataset.p;draw();panel.scrollIntoView();});
window.revealClaim=function(li){state.f='all';state.p=Math.floor(items.indexOf(li)/PER);draw();};
draw();})();</script>"""


TABS_JS = """<script>(function(){
document.documentElement.classList.add('js');
var tabs=[].slice.call(document.querySelectorAll('.tabs button')),
panels=tabs.map(function(t){return document.getElementById(t.dataset.panel);});
function show(id,push){tabs.forEach(function(t,i){var on=t.dataset.panel===id;t.setAttribute('aria-selected',on);
panels[i].hidden=!on;});if(push)history.replaceState(null,'','#'+id);}
function fromHash(){var h=location.hash.slice(1),el=h&&document.getElementById(h);
if(!el){show(tabs[0].dataset.panel);return;}
var panel=el.closest('.tabpanel');if(!panel){show(tabs[0].dataset.panel);return;}
show(panel.id);if(el!==panel){if(window.revealClaim&&el.matches('li.claim'))window.revealClaim(el);[el.closest('details'),el.querySelector('details')].forEach(function(d){
if(d)d.open=true;});var g=el.parentElement&&el.parentElement.closest('details');if(g)g.open=true;el.scrollIntoView();}}
tabs.forEach(function(t){t.addEventListener('click',function(){show(t.dataset.panel,true);});});
addEventListener('hashchange',fromHash);fromHash();})();</script>"""


ENTRY_TYPES = {"orientation": "Orientation", "reproduction": "Reproduction", "analysis": "Analysis"}


def notebooks_panel(data: dict, dandiset: str, root: str) -> tuple[str, int]:
    """The entries that use this dandiset, each with all of its notebooks."""
    entries = entries_for(data, dandiset)
    count = sum(len(en["notebooks"]) for en in entries)
    if not entries:
        return '<p class="muted" style="margin-top:14px">No notebooks use this dataset yet.</p>', 0
    out = ""
    for en in entries:
        items = ""
        for nb in en["notebooks"]:
            links = []
            if nb["executed"]:
                links.append(f'<a href="{data.get("notebooks_root") or root}{e(nb["executed"])}">Executed, with outputs</a>')
            if not data["demo"]:
                links.append(f'<a href="{REPO_URL}/blob/main/entries/{e(en["name"])}/{e(nb["path"])}">Source</a>')
                links.append(f'<a href="{COLAB_URL}/{e(en["name"])}/{e(nb["path"])}" target="_blank" rel="noopener" '
                             f'title="Open the notebook in Google Colab, which fetches the entry and installs its '
                             f'pinned packages">Open in Colab</a>')
            items += (f'<li style="grid-template-columns:1fr max-content"><span><strong>{e(nb["title"])}</strong><br>'
                      f'<span class="muted small">{e(nb["path"])}</span></span>'
                      f'<span>{" · ".join(links) or "Not yet executed"}</span></li>')
        others = [d for d in en["datasets"] if d != dandiset]
        also = (" Also uses " + ", ".join(e(dataset_label(d)) for d in others) + ".") if others else ""
        built_on = (" Builds on " + ", ".join(e(x) for x in en["derived_from"]) + ".") if en["derived_from"] else ""
        code = ("" if data["demo"] else
                f' <a href="{REPO_URL}/tree/main/entries/{e(en["name"])}">All files</a>')
        env = ("" if data["demo"] or not en.get("pinned") else
               f'<p class="small muted" style="margin:2px 0 0">Environment: Python {e(en["python"])}, '
               f'{en["pinned"]} packages pinned{" with their hashes" if en.get("hashed") else ""} in '
               f'<a href="{REPO_URL}/blob/main/entries/{e(en["name"])}/requirements.lock.txt">requirements.lock.txt</a>; '
               f'CI runs each notebook from a new environment built from it.</p>')
        out += (f'<div class="entry"><p style="margin:18px 0 2px"><span class="tag">{e(ENTRY_TYPES.get(en["type"], en["type"]))}</span> '
                f'<strong>{e(en["title"])}</strong></p>'
                f'<p class="sub small">{e(en["description"])}{also}{built_on}{code}</p>{env}'
                f'<ul class="plain">{items}</ul></div>')
    return out, count


def dandiset_title(dandiset: str, atts: list[dict]) -> str:
    """The page title: the paper when there is one, then the dandiset."""
    titles = {a["paper_title"] for a in atts if a.get("paper_title")}
    paper = titles.pop() if len(titles) == 1 else None
    return f"{paper} ({dataset_label(dandiset)}) · {SITE_NAME}" if paper else f"{dataset_label(dandiset)} · {SITE_NAME}"


def dandiset_description(dandiset: str, atts: list[dict]) -> str:
    """One sentence with what was tested and what came of it, for search results and link previews."""
    counts = outcome_counts(atts)
    n, findings = sum(counts.values()), sum(len(a["findings"]) for a in atts)
    parts = [f"{counts[k]:,} {OUTCOMES[k][0].lower()}" for k in OUTCOMES if counts[k]]
    return (f"An attempt to reproduce the findings of a paper from dataset {dataset_label(dandiset)} on {archive_name(dandiset)}: "
            f"{n:,} claims tested ({', '.join(parts)}) and {findings:,} findings about the data.")


def earlier_attempts(data: dict, dandiset: str) -> list[dict]:
    """The dandiset's attempts that a later attempt on the same paper replaced, oldest first."""
    current = current_attempts(data).get(dandiset, [])
    return sorted((a for a in data["attempts"] if a["key"] == dandiset and a not in current),
                  key=lambda a: (a["date"], a["id"]))


VERSION_STATES = {"published": "A published version", "draft": "An unpublished draft",
                  "unversioned": "Unversioned files", "unknown": "Version not recorded"}


def version_state(a: dict) -> str:
    """What kind of version of its dataset an attempt ran on: a key of VERSION_STATES."""
    v = a["dataset_version"]
    return "unknown" if not v else v if v in ("draft", "unversioned") else "published"


def version_order(a: dict) -> tuple:
    """Sorts attempts by the version of the dataset they ran on, oldest first: a draft is newer than any published
    version (DANDI's are dated, so they sort as text), and attempts on one version go by their date."""
    return ({"draft": 2, "published": 1}.get(version_state(a), 0), str(a["dataset_version"] or ""), a["date"], a["id"])


def version_plain(a: dict) -> str:
    """The dataset version an attempt ran on, in words, for a list's row."""
    v = a["dataset_version"]
    return {"unknown": "a version not recorded", "draft": "the unpublished draft",
            "unversioned": "unversioned files"}.get(version_state(a)) or f"version {v}"


def version_text(a: dict) -> str:
    """The dataset version an attempt ran on, linked to its DOI when it has one; a draft says so."""
    v = a["dataset_version"]
    if not v:
        return "version not recorded"
    if v == "unversioned":
        return "unversioned files (the archive keeps no versions)"
    if v == "draft":
        modified = a["dataset"].get("modified")
        return "unpublished draft" + (f" (modified {e(str(modified)[:10])})" if modified else "")
    doi = a["dataset"].get("doi")
    return (f'version <a href="https://doi.org/{e(doi)}">{e(v)}</a>' if doi else f"version {e(v)}")


def summary_block(atts: list[dict], name=None) -> str:
    """The recorder's summary of each attempt shown, at the top of the page, with who wrote it. Several are told
    apart by their paper, or by what `name` gives for an attempt (html)."""
    shown = [a for a in atts if a.get("summary")]
    if not shown:
        return ""
    name = name or (lambda a: e(a.get("paper_title") or a["paper"]))
    paras = "".join((f'<p class="lede"><em>{name(a)}:</em> ' if len(shown) > 1 else '<p class="lede">')
                    + f'{e(a["summary"])}</p>' for a in shown)
    return (f'<div class="attempt-summary">{paras}<p class="sub small">Summary written by the agent that recorded the attempt, '
            f'from its claims and the agents&rsquo; reports. A failure to reproduce may be a failure of the agent.</p></div>')


def attempts_timeline(data: dict, dandiset: str, root: str, shown: list[dict], paper: dict | None = None) -> str:
    """A panel with every attempt on the dataset, or given a paper every attempt on the paper, oldest first, when
    there is more than one. Each opens the attempt's page and names the datasets it used, with their versions."""
    if paper:
        all_atts = paper_attempts(data, paper)
        current = paper["attempts"]
    else:
        all_atts = sorted((a for a in data["attempts"] if a["key"] == dandiset), key=lambda a: (a["date"], a["id"]))
        current = current_attempts(data).get(dandiset, [])
    if len(all_atts) < 2:
        return ""
    current_ids = {a["id"] for a in current}
    shown_ids = {a["id"] for a in shown}
    one_shown = len(shown_ids) == 1
    papers = {a["paper"] for a in all_atts}
    items = ""
    for a in all_atts:
        sets = attempt_sets(data, a) if paper else [a]
        # Counted here even when deprecated, which the totals leave out.
        counts = {k: sum(1 for o in a["outcomes"] if o["outcome"] == k) for k in OUTCOMES}
        n = sum(counts.values())
        n_found = sum(len(x["findings"]) for x in sets)
        href = f'{root}{attempt_path(data, a)}'
        is_current = a["id"] in current_ids
        # On a paper's page every current attempt is shown, so none is marked; on an attempt's page, the one.
        here = a["id"] in shown_ids and (one_shown or not paper)
        notes = [f'{n} claims', f'{n_found} findings about the data']
        protocol = (a.get("agent") or {}).get("protocol")
        if protocol:
            notes.append(f'protocol {e(protocol)}')
        title = (f'<span class="muted small">{e(a.get("paper_title") or a["paper"])}</span>'
                 if len(papers) > 1 else "")
        name = f'Attempt {e(a["id"].rsplit("-", 1)[1])}'
        viewing = '<span class="t-viewing">Viewing</span>' if here else ""
        name = f'<strong>{name}</strong>' if here else f'<a href="{href}"><strong>{name}</strong></a>'
        used = ("; ".join(f'<a href="{root}{e(page_of(x["key"]))}">{e(x["label"])}</a> {version_text(x)}' for x in sets)
                if paper else f'Dataset {version_text(a)}')
        card = (f'<div class="t-head">{name}{viewing}<span class="muted small">{e(a["date"])}</span>'
                + f'<span class="tag">{"current" if is_current else "replaced"}</span>'
                + ('<span class="tag">deprecated</span>' if a.get("deprecated") else "")
                + f'</div>{title}<span class="t-version">{used}</span>'
                f'<div class="t-bar">{bar(counts, f"Outcomes of {n} claims", "bar mini")}</div>'
                f'<span class="muted small">{" · ".join(notes)}</span>')
        card = f'<div class="t-card">{card}</div>'
        classes = " ".join(c for c, on in (("current", is_current), ("here", here),
                                           ("deprecated", bool(a.get("deprecated")))) if on)
        current_attr = ' aria-current="page"' if here else ""
        items += (f'<li class="{classes}"{current_attr}>'
                  f'<span class="dot" aria-hidden="true"></span>{card}</li>')
    intro = ("Every attempt on the paper, each with the datasets it used and their versions. An attempt on a dataset "
             "replaces the one before it on that dataset; the paper&rsquo;s page shows the current ones." if paper else
             "Each attempt tests the paper again, usually on a newer version of the dataset or a newer protocol, and "
             "reports which earlier findings are fixed. The latest attempt on each paper is the current one.")
    # Closed until asked for: the page is about the paper's results, and the attempts behind them are detail. The
    # bar says how many there are, and how many of them a later attempt replaced.
    n_replaced = sum(1 for a in all_atts if a["id"] not in current_ids)
    said = f'{len(all_atts) - n_replaced} current' + (f', {n_replaced} replaced' if n_replaced else "")
    return (f'<details class="panel timeline-panel"><summary><h2>Attempts{"" if paper else " over time"} '
            f'<span class="count">{len(all_atts)}</span></h2><span class="muted small">{said}</span></summary>'
            f'<p class="sub small" style="margin-top:10px">{intro}</p><ol class="timeline">{items}</ol></details>')


def finding_tags(f: dict) -> str:
    tags = (f'<span class="tag status-{e(f["status"])}">{FINDING_STATUS[f["status"]]}</span>'
            if f.get("status") else "")
    if f.get("found") == "on_prompt":
        tags += ('<span class="tag" title="Not found by the blind attempt; found when the reconcile step '
                 'checked the earlier finding">found on prompt</span>')
    return tags


def findings_list(findings: list[dict], root: str, note=None) -> str:
    """Findings about the data as a list, each with its kind (a link to the datasets with an open finding of that
    kind) and, given `note`, a line under it (which attempt found it)."""
    return "".join(
        f'<li><span><a class="kind" href="{root}datasets/?found={e(f["kind"])}">'
        f'{e(FINDING_KINDS.get(f["kind"], f["kind"]))}</a></span><span>{finding_tags(f)}{e(f["statement"])}'
        + (f'<br><span class="muted small">{note(f)}</span>' if note else "") + '</span></li>'
        for f in findings) or '<li><span></span><span class="muted">None recorded.</span></li>'


def page_dataset(data: dict, key: str) -> str:
    """A dataset's page. Findings about the data belong to the dataset, claims to a paper: the page has the dataset,
    what every attempt that used it found about its data, and the papers tested on it, each opening the page of its
    claims and outcomes."""
    root = "../../../"
    target = next((t for t in data["targets"] if t["key"] == key), None)
    atts = [a for a in current_attempts(data).get(key, []) if not a.get("deprecated")]
    papers = [q for q in papers_of(data) if key in q["datasets"]]
    by_doi = {q["doi"]: q for q in papers}

    def found_by(a, f):
        q = by_doi.get(a["paper"].lower())
        name = f'<a href="{root}papers/{e(q["key"])}/">{e(q["byline"])}</a>' if q else e(a["paper"])
        others = [k for k in a.get("datasets") or [a["key"]] if k != key]
        named = f.get("datasets") or []
        return (f'Found by the attempt on {name} (<a href="{root}{e(attempt_path(data, a))}">{e(a["id"])}</a>, '
                f'{e(a["date"])})'
                # An attempt on several datasets says which of them a finding is about (`datasets`): one that
                # does not is listed for each, and one about several says so.
                + (f'; that attempt also used {e(", ".join(dataset_label(k) for k in others))}, and the finding '
                   'does not say which dataset it is about' if others and not named else
                   f'; also about {e(", ".join(dataset_label(key_of_dir(x)) for x in named if key_of_dir(x) != key))}'
                   if len(named) > 1 else ""))
    findings = [(f, a) for a in atts for f in a["findings"]]
    # Open findings under the version of the dataset they were found on, the newest version first: a finding on
    # an older version has not been checked on a newer one unless a later attempt on the same paper says so.
    by_version: dict = {}
    for a in sorted(atts, key=version_order, reverse=True):
        by_version.setdefault(version_text(a), []).append(a)
    findings_html = ""
    for i, (version, group) in enumerate(by_version.items()):
        n = sum(len(a["findings"]) for a in group)
        dates = sorted({a["date"] for a in group})
        when = dates[0] if len(dates) == 1 else f"{dates[0]} to {dates[-1]}"
        older = ("" if i == 0 else ' <span class="tag" title="A newer version was tested too; these findings were '
                 'not checked on it">an older version</span>')
        findings_html += (f'<h3 class="vhead">Dataset {version}{older}<span class="muted small"> · tested {e(when)} · '
                          f'{n} open finding{"" if n == 1 else "s"}</span></h3><ul class="findings">'
                          + ("".join(findings_list([f], root, note=lambda f, a=a: found_by(a, f))
                                     for a in group for f in a["findings"]) or findings_list([], root)) + "</ul>")
    if not atts:
        findings_html = f'<ul class="findings">{findings_list([], root)}</ul>'
    # Findings of an earlier attempt that a repeat attempt found fixed, on the version it ran on.
    fixed = [(g, a) for a in atts for g in (a.get("reconciliation") or {}).get("gone", [])
             if g["status"] == "fixed" and g.get("about", "data") == "data"]
    fixed_html = ""
    if fixed:
        fixed_html = (f'<section class="panel"><h2>Fixed since an earlier attempt <span class="count">{len(fixed)}</span></h2>'
                      '<ul class="findings">' + "".join(
                          f'<li><span>{e(FINDING_KINDS.get(g["kind"], g["kind"]))}</span><span>'
                          f'<span class="tag status-fixed">Fixed</span>{e(g["statement"])}'
                          f'<br><span class="muted small">{e(g["note"])} Found fixed on dataset {version_text(a)} by '
                          f'{e(a["id"])}, {e(a["date"])}.</span></span></li>' for g, a in fixed) + "</ul></section>")

    paper_rows_html = ""
    for q in papers:
        rel = next((d.get("relation", "primary") for d in paper_records.datasets_of(q["key"]) if d["key"] == key), "primary")
        # The attempts on the paper that used this dataset, each with the version it ran on.
        mine = [a for a in current_attempts(data).get(key, []) if a["paper"].lower() == q["doi"]]
        under = ('<div class="meta" style="margin-top:6px"><span class="small">' + "; ".join(
            f'Attempt <a href="{root}{e(attempt_path(data, a))}">{e(a["id"])}</a> on {version_text(a)}'
            + (" (set aside, to redo: its findings are not listed here)" if a.get("deprecated") else "")
            for a in mine) + '</span></div>') if mine else ""
        paper_rows_html += paper_card(data, q, root, note="its own data" if rel == "primary" else "reuses the data",
                                      under=under)

    tags = ""
    if target:
        tags = " ".join(
            [f'<a class="tag" href="{root}papers/?technique={e(t)}">{e(t)}</a>' for t in target["technique"]]
            + [f'<a class="tag" href="{root}papers/?species={e(x)}">{e(x)}</a>' for x in target["species"]]
            + ([f'<a class="tag" href="{root}papers/?converted=catalystneuro" '
                f'title="{e("; ".join(target["catalystneuro"]))}">Converted by CatalystNeuro</a>']
               if target.get("catalystneuro") else [])
            + [f'<span class="tag" title="{target["size_gb"]:,.1f} GB">{human_size(target["size_gb"])}</span>',
               f'<span class="tag" title="{target["files"]:,} files">{human_count(target["files"], "file")}</span>'])
    versions = sorted({version_text(a) for a in atts})
    actions = [f'<a href="{e(archive_url(key))}" target="_blank" rel="noopener">View on '
               f'{e(ARCHIVES.get(split_key(key)[0], {}).get("label", split_key(key)[0]))}</a>']
    if atts:
        actions.append(f'<a href="{root}api/{page_of(key).rstrip("/")}.json">JSON</a>')
    name = (target or {}).get("name") or dataset_label(key)
    body = f'''<header class="page">
  <p class="crumbs"><a href="{root}datasets/">Datasets</a> / {e(dataset_label(key))}</p>
  <div class="dhead"><h1>{e(dataset_label(key))}</h1></div>
  <p class="sub">{e(name)}</p>
  <div style="display:flex;flex-wrap:wrap;gap:6px 8px;margin-top:8px">{tags}</div>
  {f'<p class="sub small" style="margin-top:8px">Tested on dataset {"; ".join(versions)}</p>' if versions else ""}
  <p class="actions">{" ".join(actions)}</p>
</header>
<main>
  <section class="panel" id="findings"><h2>Open findings about the data <span class="count">{len(findings)}</span></h2>
    <p class="sub small" style="margin-top:12px">What the attempts that used this dataset found about the data
    themselves, for its owner and the archive, under the version of the dataset each was found on. The claims and
    their outcomes are on each paper&rsquo;s page.</p>
    {findings_html}</section>
  {fixed_html}
  <section class="panel"><h2>Papers tested on this dataset <span class="count">{len(papers)}</span></h2>
    <div class="results" style="margin-top:12px">{paper_rows_html or '<p class="empty">None yet.</p>'}</div></section>
</main>'''
    return shell(data, f"{dataset_label(key)}: {name} · {SITE_NAME}", root, "datasets", body, path=page_of(key),
                 description=f"What attempts to reproduce papers from {dataset_label(key)} on {archive_name(key)} found "
                             f"about its data, and the papers tested on it.")


def page_paper(data: dict, p: dict) -> str:
    """A paper's page. An attempted paper's is the full page of its results (page_dandiset, by paper): the papers
    are the site's primary index, and nothing on the page needs a dataset's page. A paper with claims and no attempt
    yet has its claims, as read and checked, and where it stands in the pipeline."""
    if p["attempts"]:
        return page_dandiset(data, p["attempts"][-1]["key"], paper=p)
    root = "../../"
    row = next(r for r in rows_cache(data)["papers"] if r["id"] == p["key"])
    datasets_html = "".join(
        f'<li><a href="{root}{e(d["page"])}">{e(d["label"])}</a>' if d["page"] else f'<li>{e(d["label"])}'
        for d in row["datasets"])
    relation = " (data the paper reuses)" if p["relation"] == ["reuses"] else ""
    head = (f'<header class="page"><p class="eyebrow">{e(p["byline"])}{(" · " + e(journal_name(p["doi"]))) if journal_name(p["doi"]) else ""}</p>'
            f'<h1>{e(p["title"])}</h1>{authors_html(data, p["doi"], root)}'
            f'<p class="sub"><a href="https://doi.org/{e(p["doi"])}">doi:{e(p["doi"])}</a> · paper key '
            f'<code>{e(p["key"])}</code></p></header>')
    parts = [f'<section class="panel"><h2>Datasets{relation}</h2><ul class="inline">{datasets_html}</ul></section>']
    if not p["attempts"]:
        # Claims read from the paper, before its first attempt: they belong to the paper (claims/<paper>.yaml).
        files = data.get("paper_claims", {}).get(p["key"], [])
        claims_html, n = claims_list(files, {p["doi"]: p["title"]})
        if n:
            prow = next((r for r in paper_pipeline_rows(data) if r.get("paper") == p["key"]), None)
            nxt = ("; next in the pipeline: " + e(prow["next"].lower())) if prow and prow["next"] else ""
            steps = "".join(f'<dt>{e(label)}</dt><dd>{e(prow["state"][k][0])}'
                            + (f' ({e(prow["state"][k][1])})' if prow["state"][k][1] else "") + "</dd>"
                            for k, label in PAPER_STEPS) if prow else ""
            parts.append(f'<p class="lede">Not attempted yet. These are the claims read from the paper, which an '
                         f'attempt will test{nxt}.</p>')
            parts.append(f'<section class="panel"><h2>Claims <span class="count">{n}</span></h2>{claims_html}</section>')
            if steps:
                parts.append(f'<section class="panel"><h2>Pipeline</h2><dl class="kv" style="margin-top:14px">{steps}</dl></section>')
    if p["live"]:
        # Each attempt's summary, named by the datasets it ran on when there are several.
        shown = [a for a in p["live"] if a.get("summary")]
        if shown:
            paras = "".join(
                (f'<p class="lede"><em>{e(", ".join(dataset_label(k) for k in a.get("datasets") or [a["key"]]))}:</em> '
                 if len(shown) > 1 else '<p class="lede">') + f'{e(a["summary"])}</p>' for a in shown)
            parts.append(f'<div class="attempt-summary">{paras}<p class="sub small">Summary written by the agent that '
                         f'recorded the attempt, from its claims and the agents&rsquo; reports. A failure to reproduce '
                         f'may be a failure of the agent.</p></div>')
        counts = row["counts"]
        spelled = " · ".join(f"{n} {OUTCOMES[k][0].lower()}" for k, n in counts.items() if n)
        parts.append(f'<section class="panel"><h2>Outcomes</h2>{bar(counts, "outcomes")}'
                     f'<p class="small muted">{spelled}: {row["claims"]} claims tested across {len(p["live"])} '
                     f'attempt{"s" if len(p["live"]) != 1 else ""}.</p></section>')
    for a in p["attempts"]:
        missing = a.get("missing_datasets") or []
        used = ", ".join(f'<a href="{root}{e(page_of(k))}">{e(dataset_label(k))}</a>' for k in a.get("datasets") or [a["key"]])
        items = "".join(
            f'<li>{chip(o["outcome"], root + page_of(a["key"]) + "#claim-" + o["claim"])} {e(o["statement"])}</li>'
            for o in a["outcomes"])
        flag = (f'<p class="small"><strong>Datasets it could not use:</strong> '
                + "; ".join(e((m.get("archive", "") + ":" + m.get("id", "")).strip(":") or m.get("name", "a dataset"))
                            + f' ({e(m.get("why", ""))})' for m in missing) + "</p>") if missing else ""
        dep = f'<p class="small muted">Deprecated: {e(a["deprecated"])}</p>' if a.get("deprecated") else ""
        parts.append(f'<section class="panel"><h2>Attempt <code>{e(a["id"])}</code></h2>'
                     f'<p class="small muted">{e(a["date"])} · on {used}</p>{dep}{flag}'
                     f'<ul class="paper-claims">{items}</ul></section>')
    if not p["attempts"] and len(parts) == 1:
        parts.append('<section class="panel"><p class="muted">No attempt on this paper yet, and no claims read from it.</p></section>')
    body = head + '<main class="paper">' + "".join(parts) + "</main>"
    return shell(data, f'{p["byline"]}: {p["title"]} · {SITE_NAME}', root, "papers", body,
                 path=f'papers/{p["key"]}/',
                 description=f'Reproduction attempts on {p["byline"]}, "{p["title"]}", from its open data.')


def page_dandiset(data: dict, dandiset: str, attempt: dict | None = None, paper: dict | None = None) -> str:
    """Given a paper (papers_of), the paper's page: its claims and their outcomes, from the paper's latest attempts
    on all its datasets, with `dandiset` the dataset of its latest attempt. Given a paper and one of its attempts,
    that attempt's page, under the paper: the same sections for the one attempt, current or replaced. Without a
    paper (an attempt whose paper is not listed), the dandiset's page from its current attempts, or an earlier
    attempt's page under it."""
    root = ("../../../" if attempt else "../../") if paper else "../../../../" if attempt else "../../../"
    current_atts = current_attempts(data)[dandiset]
    atts = [attempt] if attempt else paper["attempts"] if paper else current_atts
    one = attempt if paper else None                      # the page is one attempt's, under its paper
    replaced = bool(one) and one["id"] not in {a["id"] for a in paper["attempts"]}
    # The datasets the page is about: the paper's that its attempts used, or the one.
    about = list(dict.fromkeys(k for a in atts for k in a.get("datasets") or [a["key"]])) if paper else [dandiset]
    target = next((t for t in data["targets"] if t["key"] == dandiset), None)
    counts = outcome_counts(atts)
    n = sum(counts.values())
    order = {"reproduced": 0, "partially_reproduced": 1, "not_reproduced": 2}

    # Questions the author asked a reader about the claims file (docs/protocol.md, Author, step 1.6), with answers.
    question_items_ = (data.get("pipeline") or {}).get("question_items", {})
    questions, seen_q = [], set()
    for k in about:   # a paper's questions are filed once and read for each of its datasets
        for q in question_items_.get(k, []):
            if (q.get("claim"), q.get("question")) not in seen_q:
                seen_q.add((q.get("claim"), q.get("question")))
                questions.append(q)
    asked: dict = {}
    for i, q in enumerate(questions, 1):
        for c in [q.get("claim"), *(q.get("also") or [])]:
            if c:
                asked.setdefault(c, i)

    # Claims, grouped by paper when the dandiset has attempts on more than one.
    claims_html = ""
    for a in atts:
        if paper:   # the page is the paper's: an attempt is named by its datasets when there are several
            if len(atts) > 1:
                claims_html += (f'<p class="sub small" style="margin:14px 0 0">Attempt '
                                f'<a href="{root}{e(attempt_path(data, a))}"><code>{e(a["id"])}</code></a>, on '
                                + used_html(data, a, root) + '</p>')
        else:
            claims_html += (f'<p class="sub small" style="margin:14px 0 0">From the paper '
                            f'<a href="https://doi.org/{e(a["paper"])}">{e(a.get("paper_title") or a["paper"])}</a></p>')
        if a.get("deprecated"):
            claims_html += (f'<p class="deprecated"><strong>Deprecated:</strong> {e(a["deprecated"])} '
                            f'Its outcomes are shown but not counted.</p>')
        # One group per notebook, in the entry's order, then the claims no notebook tests.
        rank = {**order, "blocked": 3}
        for nb in a["notebooks"]:
            mine = sorted((o for o in a["outcomes"] if o.get("notebook") == nb["path"]),
                          key=lambda o: rank[o["outcome"]])
            if not mine:
                continue
            title = (f'<a href="{data.get("notebooks_root") or root}{e(nb["executed"])}">{e(nb["title"])}</a>' if nb["executed"]
                     else e(nb["title"]))
            claims_html += (f'<div class="claim-group"><h3 style="margin-top:18px">{title} '
                            f'<span class="count">{len(mine)}</span></h3>'
                            f'<p class="sub small" style="margin:2px 0 0">Notebook <code>{e(nb["path"])}</code>'
                            f'</p>{by_outcome(mine, root, a, asked)}</div>')
        listed = {n["path"] for n in a["notebooks"]}
        blocked = [o for o in a["outcomes"] if o.get("notebook") not in listed]
        if blocked:
            reasons: dict = {}
            for o in blocked:
                reasons[o["blocked_by"]] = reasons.get(o["blocked_by"], 0) + 1
            why = ", ".join(f"{count} {BLOCKED_BY.get(k, k).lower()}" for k, count in reasons.items())
            claims_html += (f'<details class="group claim-group" open><summary><h3>Not tested in a notebook '
                            f'<span class="count">{len(blocked)}</span></h3>'
                            f'<span class="muted small">{e(why)}</span></summary>'
                            f'{by_outcome(blocked, root, a, asked)}</details>')

    all_findings = [f for a in atts for f in a["findings"]]

    def finding_tags(f):
        tags = (f'<span class="tag status-{e(f["status"])}">{FINDING_STATUS[f["status"]]}</span>'
                if f.get("status") else "")
        if f.get("found") == "on_prompt":
            tags += ('<span class="tag" title="Not found by the blind attempt; found when the reconcile step '
                     'checked the earlier finding">found on prompt</span>')
        return tags
    findings_html = "".join(
        f'<li><span><a class="kind" href="{root}datasets/?found={e(f["kind"])}">'
        f'{e(FINDING_KINDS.get(f["kind"], f["kind"]))}</a></span><span>{finding_tags(f)}{e(f["statement"])}</span></li>'
        for f in all_findings) or '<li><span></span><span class="muted">None recorded.</span></li>'
    for a in atts:
        rec = a.get("reconciliation")
        if not rec:
            continue
        n_then = rec["earlier"].rsplit("-", 1)[1]
        findings_html += (f'</ul><h3 style="margin-top:22px">Compared with attempt {e(n_then)}</h3>'
                          f'<p class="sub small" style="margin-top:6px">This attempt was made without seeing attempt '
                          f'{e(n_then)}' + ("" if rec["blind"] else f' (except: {e(rec["blind_note"])})') +
                          f'. A separate step then compared the two: each finding above is marked new or still '
                          f'present, and these earlier findings are gone or could not be checked.</p>'
                          f'<ul class="findings">')
        findings_html += "".join(
            f'<li><span><span class="tag status-{e(g["status"])}">'
            f'{"Fixed" if g["status"] == "fixed" else "Not checked"}</span></span>'
            f'<span>{e(g["statement"])}<br><span class="muted small">{e(g["note"])}</span></span></li>'
            for g in rec["gone"]) or '<li><span></span><span class="muted">None: every earlier finding is still present.</span></li>'

    notebooks_html, n_notebooks, seen_nb = "", 0, set()
    for k in about:   # an entry that uses several of the paper's datasets is shown once
        html_, n_ = notebooks_panel(data, k, root)
        if html_ not in seen_nb:
            seen_nb.add(html_)
            notebooks_html += html_
            n_notebooks += n_

    verification_html, n_rounds = "", 0
    for a in atts:
        if len(atts) > 1:
            verification_html += f'<p class="sub small" style="margin:14px 0 0">Attempt {e(a["id"])}</p>'
        if not a["verifications"]:
            verification_html += ('<p class="muted" style="margin-top:14px">Not yet checked by an independent '
                                  'verifier.</p>')
            continue
        rounds = ""
        for i, v in enumerate(a["verifications"], 1):
            n_rounds += 1
            dis = ""
            for d in v["disagreements"]:
                theirs = OUTCOMES[d["outcome"]][0] if d["outcome"] in OUTCOMES else "not given"
                dis += (f'<li><a href="#claim-{e(d["claim"])}">{e(d["claim"])}</a>: the verifier’s outcome was '
                        f'“{e(theirs)}”. {e(d["reason"])}</li>')
            dis = f'<ul style="margin:6px 0 0;padding-left:20px">{dis}</ul>' if dis else ""
            reviewed = f' Reviewed: {e(v["reviewed"])}' if v["reviewed"] else ""
            rounds += (f'<li><span><strong>Round {i}</strong><br><span class="muted">{e(v["date"])}</span></span>'
                       f'<span>Agreed with {v["agreed"]} of {v["of"]} outcomes. {e(v["by"])}.{reviewed}{dis}</span></li>')
        verification_html += f'<ul class="plain">{rounds}</ul>'

    deviations: dict = {}
    for a in atts:
        for o in a["outcomes"]:
            for d in o["deviations"]:
                deviations.setdefault(d, []).append(o["claim"])
    if deviations:
        items = ""
        for d, cs in sorted(deviations.items(), key=lambda kv: -len(kv[1])):
            links = " ".join(f'<a class="tag" href="#claim-{e(c)}">{e(c)}</a>' for c in cs)
            items += f'<li style="grid-template-columns:1fr"><span>{e(d)}</span><span>{links}</span></li>'
        deviations_html = f'<ul class="plain">{items}</ul>'
    else:
        deviations_html = '<p class="muted" style="margin-top:14px">None recorded.</p>'

    provenance_html = ""
    for a in atts:
        agent = a.get("agent") or {}
        record = (e(a["id"]) if data["demo"] else
                  f'<a href="{REPO_URL}/blob/main/attempts/{e(a["id"])}.yaml">{e(a["id"])}</a>')
        rows_ = [("Attempt record", record), ("Paper", f'<a href="https://doi.org/{e(a["paper"])}">'
                                                     f'{e(a.get("paper_title") or a["paper"])}</a>'),
                 ("Date", e(a["date"])),
                 ("Made by", ("An agent" if a["kind"] == "agent" else "A person") + f', run by {e(a["accountable"])}')]
        # The datasets the attempt used, each with its version: a paper's attempt can use several.
        for x in (attempt_sets(data, a) if paper else [a]):
            rows_ += [("Dataset", (f'<a href="{root}{e(page_of(x["key"]))}">{e(x["label"])}</a> ' if paper else "")
                       + f'(<a href="{e(archive_url(x["key"]))}">on {e(ARCHIVES.get(split_key(x["key"])[0], {}).get("label", split_key(x["key"])[0]))}</a>)'),
                      ("Version", e(x["dataset_version"] or "not recorded")
                       + (f' (<a href="https://doi.org/{e(x["dataset"]["doi"])}">doi:{e(x["dataset"]["doi"])}</a>)'
                          if x["dataset"].get("doi") else "")
                       + (f', modified {e(x["dataset"]["modified"])}' if x["dataset"].get("modified") else ""))]
        if a["kind"] == "agent":
            runner = a.get("runner") or {}
            rows_ += [("Run on", (f'<a href="{e(runner["url"]) }">{e(runner.get("platform"))}</a>' if runner.get("url")
                                  else e(runner.get("platform", "not recorded"))))]
            rows_ += [("Harness", e(agent.get("harness", "not recorded"))),
                      ("Model", e(agent.get("model", "not recorded"))),
                      ("Protocol", e(agent.get("protocol", "not recorded")))]
        provenance_html += ('<dl class="kv" style="margin-top:14px">'
                            + "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in rows_) + "</dl>")
    folder = f'{dandiset}/attempt-{attempt["id"].rsplit("-", 1)[1]}' if attempt else dandiset
    if paper:   # the paper's runs are filed once; the first of its datasets that has them shows them
        aside = f'/attempt-{one["id"].rsplit("-", 1)[1]}' if replaced else ""   # a replaced attempt's are moved aside
        folder = next((k + aside for k in about if data.get("transcripts", {}).get(k + aside)), dandiset + aside)
    repo_folder = (data.get("transcript_dirs") or {}).get(folder, dir_of(dandiset))
    runs = data.get("transcripts", {}).get(folder, [])
    if runs and not data["demo"]:
        items = "".join(f'<li><a href="{REPO_URL}/blob/main/transcripts/{e(repo_folder)}/{e(name)}">{e(name)}</a></li>'
                        for name in runs)
        provenance_html += ('<h3 style="margin-top:18px">Transcripts of the agent runs</h3>'
                            '<p class="sub small">Each run’s prompt, messages and tool calls, with long output cut '
                            'and the text of the paper left out, and its final report.</p>'
                            f'<ul style="margin:6px 0 0;padding-left:20px">{items}</ul>')

    archive_link = lambda k, text: (f'<a href="{e(archive_url(k))}" target="_blank" rel="noopener">{text}</a>')
    archive_of = lambda k: e(ARCHIVES.get(split_key(k)[0], {}).get("label", split_key(k)[0]))
    if paper:
        actions = [f'<a href="https://doi.org/{e(paper["doi"])}">Paper</a>']
        actions += [archive_link(k, f"{e(dataset_label(k))} on {archive_of(k)}") for k in about]
        actions += [f'<a href="{root}api/{page_of(k).rstrip("/")}.json">JSON' + (f" ({e(dataset_label(k))})" if len(about) > 1
                                                                               else "") + "</a>" for k in about]
    else:
        actions = [archive_link(dandiset, f"View on {archive_of(dandiset)}")]
        actions += [f'<a href="https://doi.org/{e(a["paper"])}">Paper</a>' for a in atts] if len(atts) == 1 else []
        # The paper's page is the primary one: the same results for all its datasets.
        papers_here = {a["paper"].lower() for a in atts}
        actions += [f'<a href="{root}papers/{e(q["key"])}/">{e(q["byline"])}: the paper&rsquo;s page</a>'
                    for q in papers_of(data) if q["doi"] in papers_here and q["attempts"]]
        actions += [f'<a href="{root}api/{page_of(dandiset).rstrip("/")}.json">JSON</a>']
    actions += [f'<a href="{root}#caution">How to read outcomes</a>']

    tags = ""
    if paper:
        mine = [t for t in data["targets"] if t["key"] in about]
        tags = " ".join(
            [f'<a class="tag" href="{root}papers/?technique={e(x)}">{e(x)}</a>'
             for x in sorted({x for t in mine for x in t["technique"]})]
            + [f'<a class="tag" href="{root}papers/?species={e(x)}">{e(x)}</a>'
               for x in sorted({x for t in mine for x in t["species"]})]
            + [f'<span class="tag" title="{t["size_gb"]:,.1f} GB, {t["files"]:,} files">{e(t["label"])}: '
               f'{human_size(t["size_gb"])}</span>' for t in mine])
    elif target:
        tags = " ".join(
            [f'<a class="tag" href="{root}papers/?technique={e(t)}">{e(t)}</a>' for t in target["technique"]]
            + [f'<a class="tag" href="{root}papers/?species={e(s)}">{e(s)}</a>' for s in target["species"]]
            + ([f'<a class="tag" href="{root}papers/?converted=catalystneuro" '
                f'title="{e("; ".join(target["catalystneuro"]))}">Converted by CatalystNeuro</a>']
               if target["catalystneuro"] else [])
            + [f'<span class="tag" title="{target["size_gb"]:,.1f} GB">{human_size(target["size_gb"])}</span>',
               f'<span class="tag" title="{target["files"]:,} files">{human_count(target["files"], "file")}</span>'])

    current = current_attempts(data)
    same_paper = [] if paper else [t for t in data["targets"] if target and t["key"] != dandiset
                                    and set(t["papers"]) & set(target["papers"])]
    related = ""
    if same_paper:
        links = ""
        for t in same_paper:
            if t["key"] in current:
                links += f'<a href="{root}{page_of(t["key"])}">{e(t["label"])}</a> '
            else:
                links += (f'<span><a href="{e(archive_url(t["key"]))}">{e(t["label"])}</a> '
                          f'<span class="muted">(not attempted)</span></span> ')
        related = (f'<div class="panel" style="margin-top:28px"><h2>Other datasets that name the same paper</h2>'
                   f'<div class="related">{links}</div></div>')
    if one:   # an attempt's page: the attempts on its paper before and after it
        others = paper_attempts(data, paper)
        i = next(n for n, a in enumerate(others) if a["id"] == one["id"])
        link = lambda a, text: f'<a href="{root}{e(attempt_path(data, a))}">{text}</a>'
        prev_link = link(others[i - 1], f'← {e(others[i - 1]["id"])}') if i > 0 else "<span></span>"
        next_link = link(others[i + 1], f'{e(others[i + 1]["id"])} →') if i < len(others) - 1 else "<span></span>"
    elif paper:
        others = [q for q in papers_of(data) if q["attempts"]]
        i = next(n for n, q in enumerate(others) if q["key"] == paper["key"])
        link = lambda q, text: f'<a href="{root}papers/{e(q["key"])}/">{text}</a>'
        prev_link = link(others[i - 1], f'← {e(others[i - 1]["byline"])}') if i > 0 else "<span></span>"
        next_link = link(others[i + 1], f'{e(others[i + 1]["byline"])} →') if i < len(others) - 1 else "<span></span>"
    else:
        ids = sorted(current)
        i = ids.index(dandiset)
        prev_link = f'<a href="{root}{page_of(ids[i - 1])}">← {dataset_label(ids[i - 1])}</a>' if i > 0 else "<span></span>"
        next_link = (f'<a href="{root}{page_of(ids[i + 1])}">{dataset_label(ids[i + 1])} →</a>' if i < len(ids) - 1
                     else "<span></span>")
    superseded = ""
    if one:
        paper_link = f'<a href="{root}papers/{e(paper["key"])}/">the paper&rsquo;s page</a>'
        if replaced:
            later = next((a["id"] for a in reversed(paper["attempts"])
                          if set(a.get("datasets") or [a["key"]]) & set(one.get("datasets") or [one["key"]])),
                         paper["attempts"][-1]["id"])
            superseded = (f'<p class="deprecated"><strong>An earlier attempt.</strong> Attempt '
                          f'<a href="{root}{e(attempt_path(data, next(a for a in paper["attempts"] if a["id"] == later)))}">'
                          f'{e(later)}</a> replaced it; {paper_link} shows the current outcomes. Its notebooks link '
                          f'to the entry as it is now; the attempt record is as it was.</p>')
        else:
            n_cur = len(paper["attempts"])
            superseded = (f'<p class="sub small" style="margin-top:8px">One of the {n_cur} current attempts on this '
                          f'paper, each on its own datasets; {paper_link} has them all.</p>')
    elif attempt:
        later = next(a["id"] for a in current_atts if a["paper"] == attempt["paper"])
        same_entry = any(a["entry"] == attempt["entry"] for a in current_atts)
        superseded = (f'<p class="deprecated"><strong>An earlier attempt.</strong> Attempt {e(later)} replaced it; '
                      f'<a href="{root}{page_of(dandiset)}">the dataset’s page</a> shows the current '
                      f'outcomes.' + (" Its notebooks link to the entry as it is now, which the later attempt "
                                      "updated; the attempt record is as it was." if same_entry else "") + "</p>")

    claim_ids = {o["claim"] for a in atts for o in a["outcomes"]}
    question_items = ""
    for i, q in enumerate(questions, 1):
        claims = [c for c in [q.get("claim"), *(q.get("also") or [])] if c]
        links = ", ".join(f'<a href="#claim-{e(c)}"><code>{e(c)}</code></a>' if c in claim_ids else f"<code>{e(c)}</code>"
                          for c in claims)
        state = (f'<span class="tag">answered {e(str(q["answered"]))}</span>' if q.get("answered")
                 else '<span class="tag open">open</span>')
        answer = squash(q.get("answer") or "")
        question_items += (
            f'<li class="question" id="question-{i}"><div class="q-head">{state}'
            f'<span>asked {e(str(q.get("asked") or ""))}</span><span>about {links}</span></div>'
            f'<p class="q-text">{e(squash(q.get("question") or ""))}</p>'
            + (f'<p class="notes"><strong>Passage.</strong> {e(squash(q["passage"]))}</p>' if q.get("passage") else "")
            + (f'<p class="notes"><strong>Why it matters.</strong> {e(squash(q["why"]))}</p>' if q.get("why") else "")
            + (f'<div class="answer"><strong>The reader’s answer.</strong> {e(answer)}</div>' if answer
               else '<div class="answer open">No reader has answered it yet.</div>')
            + "</li>")
    questions_panel = (f'<section class="tabpanel" id="questions"><h2>Questions</h2>'
                       f'<p class="sub small" style="margin-top:12px">Where the author or a verifier believed the '
                       f'claims file misread the paper, they asked, citing the paper, and a reader who had not seen '
                       f'the data answered from the paper alone, amending the claims file where it was wrong. The '
                       f'author then ran the claim as answered. Attempts before protocol pilot-11 also asked here '
                       f'for method details the claims file did not give.</p>'
                       f'<ul class="questions">{question_items}</ul></section>') if questions else ""

    # What the attempts found about the paper itself (its methods, its code, its own consistency): on its page.
    notes = [f for a in atts for f in a.get("paper_notes") or []] if paper else []
    notes_panel = (f'<section class="tabpanel" id="notes"><h2>Notes on the paper</h2>'
                   f'<p class="sub small" style="margin-top:12px">What the attempts found about the paper itself: a '
                   f'method or rule it does not give, a place where it disagrees with itself, published code that '
                   f'does something else. What they found about the data is on each dataset&rsquo;s page.</p>'
                   f'<ul class="findings">' + "".join(
                       f'<li><span><span class="kind">{e(FINDING_KINDS.get(f["kind"], f["kind"]))}</span></span>'
                       f'<span>{finding_tags(f)}{e(f["statement"])}</span></li>' for f in notes)
                   + '</ul></section>') if notes else ""
    tab_defs = [("claims", "Claims", n),
                *([("notes", "Notes on the paper", len(notes))] if notes else []),
                *([] if paper else [("findings", "Findings about the data", len(all_findings))]),
                *([("questions", "Questions", len(questions))] if questions else []),
                ("notebooks", "Notebooks", n_notebooks), ("verification", "Verification", n_rounds),
                ("differences", "Method differences", len(deviations)), ("provenance", "Provenance", None)]
    # Findings about the data belong to the dataset: on a paper's page, a pointer to its datasets' pages.
    if paper:
        n_found = sum(len(x["findings"]) for a in atts for x in attempt_sets(data, a))
        findings_panel = ""
        found_note = (f'<p class="sub small" style="margin-top:8px">{n_found} finding{"s" if n_found != 1 else ""} '
                      f'about the data, on the page{"s" if len(about) > 1 else ""} of '
                      + ", ".join(f'<a href="{root}{e(page_of(k))}#findings">{e(dataset_label(k))}</a>' for k in about)
                      + '.</p>') if n_found else ""
    else:
        found_note = ""
        findings_panel = (f'<section class="tabpanel" id="findings"><h2>Findings about the data</h2>'
                          f'<p class="sub small" style="margin-top:12px">What attempts found about the dataset itself, '
                          f'for its owner and the archive.</p><ul class="findings">{findings_html}</ul></section>')
    tab_buttons = ""
    for key, label, c in tab_defs:
        count = f' <span class="count">{c}</span>' if c is not None else ""
        tab_buttons += f'<button type="button" role="tab" data-panel="{key}" aria-selected="false">{label}{count}</button>'

    if paper:   # the datasets the attempt used and their versions; several attempts are in the panel under it
        tested_on = used_html(data, atts[0], root) if len(atts) == 1 else ""
    else:
        tested_on = "; ".join((e(a.get("paper_title") or a["paper"]) + ": " if len(atts) > 1 else "")
                              + "dataset " + version_text(a) for a in atts)
    name = (target or {}).get("name") or atts[-1]["entry_title"] or dandiset
    tier = weakest_tier(atts)
    tier_link = f'{root}papers/?status=attempted&tier={tier}'
    crumb = (f'<a href="{root}{page_of(dandiset)}">{e(dataset_label(dandiset))}</a> / {e(attempt["id"])}' if attempt
             else e(dataset_label(dandiset)))
    if paper:
        row = next(r for r in rows_cache(data)["papers"] if r["id"] == paper["key"])
        sets = ", ".join(f'<a href="{root}{e(d["page"])}">{e(d["label"])}</a>' if d["page"] else e(d["label"])
                         for d in row["datasets"])
        missing = [m for a in atts for m in a.get("missing_datasets") or []]
        could_not = ("<br><strong>Datasets it could not use:</strong> " + "; ".join(
            e((m.get("archive", "") + ":" + m.get("id", "")).strip(":") or m.get("name", "a dataset"))
            + f' ({e(m.get("why", ""))})' for m in missing)) if missing else ""
        here = (f'<a href="{root}papers/{e(paper["key"])}/">{e(paper["byline"])}</a> / Attempt {e(one["id"])}'
                if one else e(paper["byline"]))
        top = (f'<p class="crumbs"><a href="{root}papers/">Papers</a> / {here}</p>'
               f'<p class="eyebrow">{e(paper["byline"])}{(" · " + e(journal_name(paper["doi"]))) if journal_name(paper["doi"]) else ""}'
               f'{(" · attempt " + e(one["id"])) if one else ""}</p>'
               f'<div class="dhead"><h1>{e(paper["title"])}</h1>{tier_badge(tier, tier_link)}</div>'
               f'{authors_html(data, paper["doi"], root)}'
               f'<p class="sub"><a href="https://doi.org/{e(paper["doi"])}">doi:{e(paper["doi"])}</a> · paper key '
               f'<code>{e(paper["key"])}</code></p>'
               f'<p class="sub">{"Data the paper reuses" if paper["relation"] == ["reuses"] else "Datasets"}: {sets}'
               f'{could_not}</p>')
    else:
        top = (f'<p class="crumbs"><a href="{root}papers/">Papers</a> / {crumb}</p>'
               f'<div class="dhead"><h1>{e(dataset_label(dandiset))}</h1>{tier_badge(tier, tier_link)}</div>'
               f'<p class="sub">{e(name)}</p>')
    body = f'''<header class="page">
  {top}
  <div style="display:flex;flex-wrap:wrap;gap:6px 8px;margin-top:8px">{tags}</div>
  <div class="summary">{bar(counts, f"Outcomes of {n} claims", "bar mini")}{legend(counts, compact=True)}</div>
  {outside_note(atts)}
  {summary_block(atts, name=(lambda a: "On " + ", ".join(e(x["label"]) for x in attempt_sets(data, a))) if paper else None)}
  {found_note}
  {f'<p class="sub small" style="margin-top:8px">Tested on {tested_on}</p>' if tested_on else ""}
  {superseded}
  <p class="actions">{" ".join(actions)}</p>
</header>
<main>
  {attempts_timeline(data, dandiset, root, atts, paper=paper)}
  <div class="tabs" role="tablist">{tab_buttons}</div>
  <section class="tabpanel" id="claims"><h2>Claims</h2>
    <div class="subtabs" id="claim-filter" role="group" aria-label="Show claims by outcome"></div>
    {claims_html}
    <nav class="pager" id="claim-pager" aria-label="Pages of claims"></nav></section>
  {notes_panel}
  {findings_panel}
  {questions_panel}
  <section class="tabpanel" id="notebooks"><h2>Notebooks</h2>
    <p class="sub small" style="margin-top:12px">Every registered entry that uses {"the paper&rsquo;s datasets" if paper else "this dataset"}. An entry can hold
    several notebooks, and can use more than one dataset.</p>
    {notebooks_html}</section>
  <section class="tabpanel" id="verification"><h2>Verification</h2>{verification_html}</section>
  <section class="tabpanel" id="differences"><h2>Method differences</h2>
    <p class="sub small" style="margin-top:12px">How the tests differed from the paper’s method or data, and the claims
    each applies to.</p>
    {deviations_html}</section>
  <section class="tabpanel" id="provenance"><h2>Provenance</h2>{provenance_html}</section>
  {related}
  <div class="prevnext">{prev_link}{next_link}</div>
</main>'''
    if one:
        return shell(data, f'Attempt {one["id"]} · {paper["byline"]}: {paper["title"]} · {SITE_NAME}', root, "papers",
                     body, CLAIMS_JS + TABS_JS, path=f'papers/{paper["key"]}/{one["id"]}/',
                     description=f'Attempt {one["id"]} to reproduce {paper["byline"]}, "{paper["title"]}", from its '
                                 f'open data: {n} claims, their outcomes, notebooks and verification.')
    if paper:
        return shell(data, f'{paper["byline"]}: {paper["title"]} · {SITE_NAME}', root, "papers", body,
                     CLAIMS_JS + TABS_JS, path=f'papers/{paper["key"]}/',
                     description=f'Reproduction attempts on {paper["byline"]}, "{paper["title"]}", from its open data: '
                                 f'{n} claims, their outcomes, notebooks and verification.')
    path = f"{page_of(dandiset)}{attempt['id']}/" if attempt else page_of(dandiset)
    title = dandiset_title(dandiset, atts)
    return shell(data, f"{attempt['id']} (earlier attempt) · {title}" if attempt else title, root, "datasets",
                 body, CLAIMS_JS + TABS_JS, path=path, description=dandiset_description(dandiset, atts))


def claims_only(data: dict) -> list[str]:
    """The datasets with claims read from their paper but no attempt yet."""
    current = current_attempts(data)
    return sorted(k for k in data.get("claim_files", {}) if k not in current)


def claims_list(files: list[dict], titles: dict) -> tuple[str, int]:
    """Claims files as lists of claims, each with its quote and how it will be judged; and how many claims."""
    claims_html, n = "", 0
    for f in files:
        check = ("not yet checked" if f["check"] is None else
                 f'checked {e(f["check"]["date"])}: ' + ("ready" if f["check"]["ready"] else "not ready"))
        items = ""
        for c in f["claims"]:
            n += 1
            body = ""
            if c["quote"]:
                cite = f'<cite>{e(c["source"])}</cite>' if c["source"] else ""
                body += f'<blockquote class="quote"><p>{e(c["quote"])}</p>{cite}</blockquote>'
            if c["criterion"]:
                body += f'<p class="deviations-title">How it will be judged</p><p class="notes">{e(c["criterion"])}</p>'
            items += (f'<li class="claim" id="claim-{e(c["id"])}"><details><summary>'
                      f'<div class="claim-head"><span class="tag">{e(c["id"])}</span></div>'
                      f'<p class="statement">{e(c["statement"])}</p></summary>'
                      f'<div class="claim-body">{body or '<p class="notes muted">No quote recorded.</p>'}</div>'
                      f'</details></li>')
        paper = titles.get(f["paper"].lower()) or f["paper"]
        claims_html += (f'<p class="sub small" style="margin:14px 0 0">From the paper '
                        f'<a href="https://doi.org/{e(f["paper"])}">{e(paper)}</a> · '
                        f'<a href="{REPO_URL}/blob/main/{e(f["path"])}">claims file</a> · {check}</p>'
                        f'<ul class="claims">{items}</ul>')
    return claims_html, n


def page_claims(data: dict, key: str) -> str:
    """A dataset's page before its first attempt: the claims read from its paper, and where it stands."""
    root = "../../../"
    target = next((t for t in data["targets"] if t["key"] == key), None)
    row = next((r for r in pipeline_rows(data) if r["key"] == key), None)
    titles = {t["paper"].lower(): t["paper_title"] for t in data["targets"] if t.get("paper")}
    claims_html, n = claims_list(data["claim_files"][key], titles)
    steps = ""
    if row:
        steps = "".join(f'<dt>{e(label)}</dt><dd>{e(row["state"][k][0])}'
                        + (f' ({e(row["state"][k][1])})' if row["state"][k][1] else "") + "</dd>"
                        for k, label in PIPELINE_STEPS)
    tags = ""
    if target:
        tags = " ".join([f'<span class="tag">{e(t)}</span>' for t in target["technique"]]
                        + [f'<span class="tag">{e(x)}</span>' for x in target["species"]])
    actions = (f'<a href="{e(archive_url(key))}" target="_blank" rel="noopener">View on '
               f'{e(ARCHIVES.get(split_key(key)[0], {}).get("label", split_key(key)[0]))}</a> '
               f'<a href="{root}pipeline/">Pipeline</a>')
    name = (target or {}).get("name") or dataset_label(key)
    body = f'''<header class="page">
  <p class="crumbs"><a href="{root}datasets/">Datasets</a> / {e(dataset_label(key))}</p>
  <div class="dhead"><h1>{e(dataset_label(key))}</h1></div>
  <p class="sub">{e(name)}</p>
  <div style="display:flex;flex-wrap:wrap;gap:6px 8px;margin-top:8px">{tags}</div>
  <p class="lede">Not attempted yet. These are the claims read from its paper, which an attempt will
  test{("; next in the pipeline: " + e(row["next"].lower())) if row and row["next"] else ""}.</p>
  <p class="actions">{actions}</p>
</header>
<main>
  <section class="panel"><h2>Claims <span class="count">{n}</span></h2>{claims_html}</section>
  <section class="panel" style="margin-top:28px"><h2>Pipeline</h2><dl class="kv" style="margin-top:14px">{steps}</dl></section>
</main>'''
    return shell(data, f"{dataset_label(key)} · {SITE_NAME}", root, "datasets", body, path=page_of(key),
                 description=f"The claims read from the paper of dataset {dataset_label(key)} on "
                             f"{archive_name(key)}, before an attempt to reproduce them.")


# --- writing -------------------------------------------------------------------

def build(data: dict, output: Path) -> None:
    r = rows_cache(data)
    output.mkdir(parents=True, exist_ok=True)
    shutil.copytree(ASSETS, output / "assets", dirs_exist_ok=True)
    for sub in ("papers", "datasets", "dandisets", "data", "api/dandiset"):
        (output / sub).mkdir(parents=True, exist_ok=True)
    (output / "index.html").write_text(page_overview(data))
    (output / "about").mkdir(exist_ok=True)
    (output / "about" / "index.html").write_text(page_about(data))
    (output / "pipeline").mkdir(exist_ok=True)
    (output / "pipeline" / "index.html").write_text(page_pipeline(data))
    (output / "data" / "pipeline.json").write_text(json.dumps(pipeline_rows(data), separators=(",", ":")) + "\n")
    for kind in LISTS:
        (output / kind).mkdir(exist_ok=True)
        (output / kind / "index.html").write_text(page_list(data, kind))
        (output / "data" / f"{kind}.json").write_text(json.dumps(r[kind], separators=(",", ":")) + "\n")
    for key, attempts in current_attempts(data).items():
        page = output / page_of(key)
        page.mkdir(parents=True, exist_ok=True)
        (page / "index.html").write_text(page_dataset(data, key))
        for a in earlier_attempts(data, key):
            # An earlier attempt's page was under its dataset; it is under its paper now.
            (page / a["id"]).mkdir(exist_ok=True)
            own = attempt_own_path(data, a)
            (page / a["id"] / "index.html").write_text(
                redirect_page(own, "../" * (page_of(key).count("/") + 1)) if own else page_dandiset(data, key, a))
        api = json.dumps({
            "dataset": {"archive": split_key(key)[0], "id": split_key(key)[1], "label": dataset_label(key)},
            "page": page_of(key), "generated": data["generated"],
            "caution": CAUTION + " It may be a failure of the attempt.",
            "outcome_counts": outcome_counts(attempts),
            "outcome_counts_with_outside_data": outcome_counts(attempts, "with_inputs"),
            "outcome_counts_elsewhere": outcome_counts(attempts, "elsewhere"),
            "outcome_counts_links": outcome_counts(attempts, "link"), "attempts": attempts,
            "entries": entries_for(data, key),
        }, indent=1) + "\n"
        (output / "api" / page_of(key).rstrip("/")).parent.mkdir(parents=True, exist_ok=True)
        (output / "api" / f'{page_of(key).rstrip("/")}.json').write_text(api)
        # The DANDI pages and API files were at dandisets/<id>/ before; links to them are kept working.
        if split_key(key)[0] == "dandi":
            old = output / "dandisets" / split_key(key)[1]
            for sub, target in [("", page_of(key))] + [(a["id"] + "/", attempt_own_path(data, a) or page_of(key) + a["id"] + "/")
                                                       for a in earlier_attempts(data, key)]:
                (old / sub).mkdir(parents=True, exist_ok=True)
                (old / sub / "index.html").write_text(redirect_page(target, "../../" + ("../" if sub else "")))
            (output / "api" / "dandiset" / f"{split_key(key)[1]}.json").write_text(api)
    for p in papers_of(data):
        if p["attempts"] or p["status"] == "claims":
            (output / "papers" / p["key"]).mkdir(parents=True, exist_ok=True)
            (output / "papers" / p["key"] / "index.html").write_text(page_paper(data, p))
        # Every attempt on the paper has an address of its own, which stays when a later attempt replaces it. The
        # paper's one current attempt is read on the paper's page, and its address leads there.
        for a in paper_attempts(data, p):
            page = output / "papers" / p["key"] / a["id"]
            page.mkdir(parents=True, exist_ok=True)
            (page / "index.html").write_text(
                redirect_page(f'papers/{p["key"]}/', "../../../") if attempt_path(data, a) == f'papers/{p["key"]}/'
                else page_dandiset(data, a["key"], attempt=a, paper=p))
    for orcid, author in author_index(data).items():
        (output / "authors" / orcid).mkdir(parents=True, exist_ok=True)
        (output / "authors" / orcid / "index.html").write_text(page_author(data, author))
    for key in claims_only(data):
        # A dataset whose paper's claims are read and not yet attempted: the dataset's page, whose papers list
        # leads to the claims on the paper's page.
        page = output / page_of(key)
        page.mkdir(parents=True, exist_ok=True)
        (page / "index.html").write_text(page_dataset(data, key))
    renamed_redirects(data, output)
    (output / "dandisets" / "index.html").write_text(redirect_page("datasets/", "../"))
    (output / "data" / "dandisets.json").write_text((output / "data" / "datasets.json").read_text())
    (output / "registry.json").write_text(json.dumps(data, indent=1) + "\n")
    (output / "sitemap.xml").write_text(sitemap(data))
    (output / "robots.txt").write_text(robots(data))
    (output / "404.html").write_text(page_not_found(data))


def renamed_redirects(data: dict, output: Path) -> None:
    """Pages that moved when records went from dataset-first to paper-first names (papers/renamed.yaml): an earlier
    attempt's page, under its old id, and an executed notebook, under its entry's old name."""
    path = ROOT / "papers" / "renamed.yaml"
    if data["demo"] or not path.is_file():
        return
    renamed = load_yaml(path) or {}
    earlier = {a["id"]: a["key"] for key in current_attempts(data) for a in earlier_attempts(data, key)}
    for old, new in (renamed.get("attempts") or {}).items():
        if new in earlier:
            moved = next(a for a in data["attempts"] if a["id"] == new)
            target = attempt_own_path(data, moved) or page_of(earlier[new]) + new + "/"
            depth = page_of(earlier[new]).count("/") + 1
            (output / page_of(earlier[new]) / old).mkdir(parents=True, exist_ok=True)
            (output / page_of(earlier[new]) / old / "index.html").write_text(redirect_page(target, "../" * depth))
    for old, new in (renamed.get("entries") or {}).items():
        if old == new or not (output / "notebooks" / new).is_dir():
            continue
        (output / "notebooks" / old).mkdir(parents=True, exist_ok=True)
        for nb in (output / "notebooks" / new).glob("*.html"):
            stub = output / "notebooks" / old / nb.name
            if not stub.exists():
                stub.write_text(redirect_page(f"notebooks/{new}/{nb.name}", "../../"))


def redirect_page(target: str, root: str) -> str:
    """A page that sends the reader on to where its content moved, keeping the query and the anchor."""
    url = e(root + target)
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Moved</title>'
            f'<link rel="canonical" href="{e(SITE_URL + target)}"><meta name="robots" content="noindex">'
            f'<meta http-equiv="refresh" content="0; url={url}">'
            f'<script>location.replace("{url}"+location.search+location.hash)</script></head>'
            f'<body><p>This page moved to <a href="{url}">{e(target)}</a>.</p></body></html>\n')


def robots(data: dict) -> str:
    """Crawlers: everything but the pull-request previews (also on gh-pages, under pr-preview/), and the sitemap.
    A demo or preview build lets nothing be crawled."""
    if data["demo"] or data.get("noindex"):
        return "User-agent: *\nDisallow: /\n"
    return f"User-agent: *\nDisallow: /pr-preview/\n\nSitemap: {SITE_URL}sitemap.xml\n"


def page_not_found(data: dict) -> str:
    """The page GitHub Pages shows for any address that has no page. It can be shown at any depth, so its links
    start from the site's root, and it is kept out of search results."""
    body = f'''<header class="page">
  <h1>Page not found</h1>
  <p class="lede">There is no page at this address. It may have moved: the dataset pages are listed on the
  <a href="/datasets/">datasets page</a>, and the <a href="/">overview</a> has where every attempt stands.</p>
</header>'''
    return shell(dict(data, noindex=True), f"Page not found · {SITE_NAME}", "/", "", body, path="404.html")


def sitemap(data: dict) -> str:
    """Every page of the site, for search engines; each dataset page dated by its latest attempt."""
    pages = [("", data["generated"][:10]), ("about/", data["generated"][:10]), ("pipeline/", data["generated"][:10])]
    pages += [(f"{kind}/", data["generated"][:10]) for kind in INDEX_LISTS]
    pages += [(page_of(d), max(a["date"] for a in atts)) for d, atts in current_attempts(data).items()]
    pages += [(page_of(d), data["generated"][:10]) for d in claims_only(data)]
    pages += [(f'papers/{p["key"]}/', p["date"] or data["generated"][:10]) for p in papers_of(data)
              if p["attempts"] or p["status"] == "claims"]
    pages += [(f"authors/{orcid}/", max([q["date"] for q in a["papers"] if q["date"]] or [data["generated"][:10]]))
              for orcid, a in author_index(data).items()]
    urls = "".join(f"<url><loc>{html.escape(SITE_URL + p)}</loc><lastmod>{day}</lastmod></url>" for p, day in pages)
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--output", type=Path, default=ROOT / "site")
    parser.add_argument("--demo", type=int, metavar="N",
                        help="build from N made-up attempts, to test the site at scale; never publish")
    parser.add_argument("--issues", type=Path, metavar="JSON",
                        help="the open needs-you issues (gh issue list --json title,url), to link from the pipeline")
    parser.add_argument("--queue", type=Path, metavar="JSON",
                        help="the runners' queues and chain times (tools/runner/describe.py queue), for the pipeline")
    parser.add_argument("--noindex", action="store_true",
                        help="keep the pages out of search results, for a preview of a pull request")
    parser.add_argument("--notebooks-from", metavar="URL",
                        help="link executed notebooks under this site (e.g. the published one) rather than this "
                             "build's own notebooks/, for previews, which leave the notebooks out")
    parser.add_argument("--analytics", metavar="TOKEN", default="",
                        help="the Cloudflare Web Analytics token of the published site, to count page views; "
                             "for the publish workflow only")
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    data = collect(args.output / "notebooks")
    if args.demo:
        data = demo(data, args.demo)
    data["noindex"] = args.noindex
    data["analytics"] = args.analytics
    data["notebooks_root"] = args.notebooks_from
    if args.queue and args.queue.is_file():
        data["queue"] = json.loads(args.queue.read_text())
    if args.issues and args.issues.is_file():
        # An issue's title is "<dataset label>: waiting on you" (tools/notify.py).
        # An issue's title is "<dataset label or paper key>: waiting on you" (tools/notify.py); a paper's is shown
        # on each of its datasets.
        data["issues"], data["issues_by_name"] = {}, {}
        for i in json.loads(args.issues.read_text()):
            if not i["title"].endswith(": waiting on you"):
                continue
            name = i["title"].rsplit(": waiting on you", 1)[0]
            data["issues_by_name"][name] = i["url"]   # the Pipeline page goes by paper
            for label in [dataset_label(d["key"]) for d in paper_records.datasets_of(name)] or [name]:
                data["issues"][label] = i["url"]
    build(data, args.output)
    print(f"wrote {args.output} ({len(data['attempts'])} attempts, {len(data['targets'])} targets"
          f"{', DEMO DATA' if data['demo'] else ''})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
