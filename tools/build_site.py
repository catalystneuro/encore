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
from datasets import folder as dir_of, key_of_folder as key_of_dir, label as dataset_label, url as archive_url  # noqa: E402,F401


def page_of(key: str) -> str:
    """A dataset's page on the site: datasets/<archive>/<id>/."""
    archive, id_ = split_key(key)
    return f"datasets/{archive}/{id_}/"


# GitHub's mark (Octicons, mark-github), drawn in the text colour.
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
    "not_reproduced": ("Not reproduced", "critical", "✕"),
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
STATUS = {"attempted": "Attempted", "pilot": "In the pilot", "open": "Not yet attempted"}
VERIFICATION_TIER = {"agent": "agent_verified", "person": "human_verified",
                     "paper_author": "author_endorsed"}
CAUTION = "A failure to reproduce is not a finding that the paper is wrong."


def load_yaml(path: Path):
    return yaml.safe_load(path.read_text())


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

def collect(executed: Path | None = None) -> dict:
    queue = json.loads((ROOT / "targets" / "dandisets.json").read_text())
    pilot = {key_of("dandi", t["dandiset"]) for t in load_yaml(ROOT / "targets" / "pilot.yaml")["targets"]}
    claims, claim_files = {}, {}
    for path in sorted((ROOT / "claims").glob("*/*.yaml")):
        data = load_yaml(path)
        key = key_of(data["dataset"]["archive"], data["dataset"]["id"])
        claims[(key, data["paper"])] = {c["id"]: c for c in data["claims"]}
        last = (data.get("checks") or [None])[-1]
        claim_files.setdefault(key, []).append({
            "path": str(path.relative_to(ROOT)), "paper": str(data["paper"]).removeprefix("doi:"),
            "check": None if last is None else {"ready": bool(last.get("ready")), "date": str(last.get("date"))},
            "claims": [{k: squash(c.get(k) or "") for k in ("id", "statement", "source", "quote", "criterion")}
                       for c in data["claims"]]})
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
    for path in sorted((ROOT / "attempts").glob("*.yaml")):
        a = load_yaml(path)
        key = key_of(a["dataset"]["archive"], a["dataset"]["id"])
        known = claims.get((key, a["paper"]), {})
        entry = entries.get(a.get("entry"))
        verifications = a.get("verifications") or []
        disagreed = {r["claim"] for v in verifications for r in v["results"] if not r.get("agrees")}
        attempts.append({
            "id": a["id"],
            "dataset": {k: str(v) for k, v in a["dataset"].items()},
            "key": key, "label": dataset_label(key),
            "dataset_version": a["dataset"].get("version"),
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
                "disagreed": o["claim"] in disagreed,
                "data": known.get(o["claim"], {}).get("data", "dataset"),
                "where": known.get(o["claim"], {}).get("where"),
                "proposed": o.get("proposed"),
            } for o in a["outcomes"]],
            "findings": [{"kind": f["kind"], "statement": squash(f["statement"])}
                         for f in a.get("findings") or []],
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

    attempted = {a["key"] for a in attempts}
    targets = []
    for t in all_targets():
        papers = [p for p in t["papers"] if not p["preprint"]] or t["papers"]
        key = t["key"]
        status = "attempted" if key in attempted else "pilot" if key in pilot else "open"
        targets.append({
            "key": key, "label": dataset_label(key), "name": t["name"], "size_gb": t["size_gb"],
            "files": t["asset_count"], "status": status,
            "paper": papers[0]["doi"], "paper_title": papers[0]["title"] or t["name"],
            "papers": [p["doi"] for p in t["papers"]],
            "n_papers": len(t["papers"]),
            "technique": sorted({part.replace(" approach", "").strip()
                                 for a in t["approaches"] if a for part in a.split(";") if part.strip()}),
            "species": sorted({short_species(s) for s in t["species"] if s}),
            "catalystneuro": t.get("catalystneuro") or [],
        })
    entry_list = []
    for entry in entries.values():
        related = entry.get("related", [])
        entry_list.append({
            "name": entry["name"], "type": entry["type"], "title": entry["title"],
            "description": squash(entry.get("description")),
            "datasets": sorted({r["id"].split("/")[0] for r in related
                                if not r["id"].startswith(("doi:", "entry:"))}),
            "papers": [r["id"].split(":", 1)[1] for r in related if r["id"].startswith("doi:")],
            "derived_from": [r["id"].split(":", 1)[1] for r in related
                             if r["id"].startswith("entry:") and r["relation"] == "derived_from"],
            "notebooks": notebooks_of(entry),
        })
    transcripts = {key_of_dir(d.name): sorted(p.name for p in d.glob("*.md"))
                   for d in sorted((ROOT / "transcripts").glob("*")) if d.is_dir()}
    # An earlier attempt's transcripts, moved aside by tools/archive_transcripts.sh.
    archived = {f"{key_of_dir(d.name)}/{a.name}": sorted(p.name for p in a.glob("*.md"))
                for d in sorted((ROOT / "transcripts").glob("*")) if d.is_dir()
                for a in sorted(d.glob("attempt-*")) if a.is_dir()}
    return finish({
        "pipeline": pipeline_inputs(),
        "claim_files": claim_files,
        "transcripts": {**transcripts, **archived},
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
    checks, questions = {}, {}
    for path in sorted((ROOT / "claims").glob("*/*.yaml")):
        last = ((load_yaml(path) or {}).get("checks") or [None])[-1]
        checks[key_of_dir(path.parent.name)] = {"ready": None if last is None else bool(last.get("ready")),
                                                "date": None if last is None else str(last.get("date"))}
    for path in sorted((ROOT / "questions").glob("*.yaml")):
        q = load_yaml(path) or []
        q = q.get("questions", []) if isinstance(q, dict) else q
        questions[key_of_dir(path.stem)] = sum(1 for x in q if not x.get("answered"))
    return {"papers": {key_of_dir(str(k)): v for k, v in papers.items()}, "checks": checks, "questions": questions}


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


def outside_note(attempts, root: str = "") -> str:
    """Lines with the outcomes of the claims that use outside data or other archives, when there are any."""
    out = ""
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
        out += (f'<p class="sub small" style="margin-top:8px">Counted separately: {text}.</p>'
                f'<div class="summary">{bar(counts, f"Outcomes of {m} {label}", "bar mini")}'
                f'{legend(counts, compact=True)}</div>')
    return out


def weakest_tier(attempts: list[dict]) -> str:
    """A dandiset is only as verified as its least verified attempt."""
    return min((a["tier"] for a in attempts), key=TIER_ORDER.index)


PIPELINE_STEPS = [("paper", "Paper"), ("claims", "Claims"), ("check", "Claims check"),
                  ("attempt", "Attempt"), ("questions", "Questions"), ("verified", "Verified")]


def queue_estimates(q: dict) -> dict[str, dict]:
    """Each queued dataset's place in its runner's queue, and how many hours from now it should be done.

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
            out[key_of_dir(folder)] = {"kind": kind, "place": place, "hours": free[lane] if hours else None}
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
            else ("waiting", f"{len(missing)} not in store") if papers else ("waiting", "no paper named"),
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


def entries_for(data: dict, dandiset: str) -> list[dict]:
    """Every entry whose metadata says it uses this dataset."""
    return [en for en in data["entries"] if dandiset in en["datasets"]]


def notebook_of(attempt: dict, path: str | None) -> dict | None:
    return next((n for n in attempt["notebooks"] if n["path"] == path), None)


def rows(data: dict) -> dict[str, list]:
    current = current_attempts(data)
    by_id = {t["key"]: t for t in data["targets"]}
    dandisets, claims, findings = [], [], []
    for t in data["targets"]:
        atts = current.get(t["key"])
        outcomes = [o for a in atts or [] if not a.get("deprecated") for o in a["outcomes"]]
        dandisets.append({
            "id": t["key"], "label": t["label"], "name": t["name"], "paper": t["paper"], "paper_title": t["paper_title"],
            "technique": t["technique"], "species": t["species"], "size_gb": t["size_gb"], "files": t["files"],
            "status": t["status"], "tier": weakest_tier(atts) if atts else None,
            "date": max(a["date"] for a in atts) if atts else None,
            "counts": outcome_counts(atts) if atts else None,
            "claims": len(outcomes) if atts else None,
            "failures": sum(1 for o in outcomes if o["outcome"] == "not_reproduced") if atts else None,
            "has": sorted({o["outcome"] for o in outcomes}),
            "blocked_by": sorted({o["blocked_by"] for o in outcomes if o["blocked_by"]}),
            "notebooks": sum(len(en["notebooks"]) for en in entries_for(data, t["key"])),
            "page": page_of(t["key"]) if atts else None, "url": archive_url(t["key"]),
            "findings": sum(len(a["findings"]) for a in atts if not a.get("deprecated")) if atts else None,
            "found": sorted({f["kind"] for a in atts or [] if not a.get("deprecated") for f in a["findings"]}),
            "deprecated": any(a.get("deprecated") for a in atts or []),
            "converted": "catalystneuro" if t["catalystneuro"] else "other",
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
    return {"datasets": dandisets, "claims": claims, "findings": findings}


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


def by_outcome(outcomes: list[dict], root: str, attempt: dict | None = None) -> str:
    """Claims under a heading for each outcome, reproduced first, then partially, not reproduced and blocked."""
    html = ""
    for outcome in ("reproduced", "partially_reproduced", "not_reproduced", "blocked"):
        mine = [o for o in outcomes if o["outcome"] == outcome]
        if mine:
            html += (f'<div class="outcome-group" data-outcome="{outcome}"><h4 class="outcome-head">{chip(outcome)}'
                     f'<span class="count">{len(mine)}</span></h4>'
                     f'<ul class="claims">{"".join(claim_item(o, root, attempt) for o in mine)}</ul></div>')
    return html


def claim_item(o: dict, root: str, attempt: dict | None = None) -> str:
    """One claim as an accordion: the outcome and statement show, the explanation opens on a click."""
    blocked = f'<span class="why">· {e(BLOCKED_BY.get(o["blocked_by"], o["blocked_by"]))}</span>' \
        if o["blocked_by"] else ""
    source = f'<span class="source">{e(o["source"])}</span>' if o["source"] else ""
    tags = '<span class="tag">verifier disagreed at first</span>' if o["disagreed"] else ""
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


def shell(data: dict, title: str, root: str, active: str, body: str, scripts: str = "", path: str = "",
          description: str = SITE_DESCRIPTION, structured: dict | None = None) -> str:
    r = rows_cache(data)
    tabs = [("overview", "Overview", root or "./", None),
            ("datasets", "Datasets", f"{root}datasets/", len({a["key"] for a in data["attempts"]})),
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
  <a class="brand" href="{home}">{SITE_NAME}</a><a class="by" href="{CN_URL}">by CatalystNeuro</a>{nav}
  <a class="tab icon" href="{REPO_URL}" aria-label="The registry on GitHub" title="The registry on GitHub">{GITHUB_MARK}</a>
  <a class="tab ext" href="{ENCORE_DOCS}" title="Run the same check on your own data with the encore command">Check your data</a>
  <a class="tab ext" href="{REPO_URL}/actions" title="The workflows that run the agents and check the entries">Agent runs</a>
  <button class="theme" id="theme" type="button" aria-label="Colour theme: auto. Change theme" title="Colour theme"><span aria-hidden="true">◐</span><span class="t">Auto</span></button>
</div></nav>
<div class="wrap">
{body}
<footer>{SITE_NAME} is developed by <a href="{CN_URL}">CatalystNeuro</a>. Generated {e(data["generated"][:10])} from the registry's files ·
<a href="{root}registry.json">Data as JSON</a> · <a href="{REPO_URL}">Repository</a> ·
<a href="{REPO_URL}/blob/main/docs/design.md">How it works</a>. Outcomes describe what one attempt could reproduce from
the data in the dataset, with the methods available. A failure to reproduce may be a failure of the agent, and is not
a judgement of the paper.</footer>
</div>
{THEME_JS}
{scripts}
</body></html>
'''


THEME_JS = """<script>(function(){
var b=document.getElementById('theme'),order=['auto','light','dark'],icon={auto:'\u25d0',light:'\u2600',dark:'\u263e'},
name={auto:'Auto',light:'Light',dark:'Dark'};
function get(){try{var t=localStorage.getItem('theme');return t==='light'||t==='dark'?t:'auto';}catch(e){return 'auto';}}
function show(t){b.firstChild.textContent=icon[t];b.lastChild.textContent=name[t];
b.setAttribute('aria-label','Colour theme: '+name[t].toLowerCase()+'. Change theme');}
b.addEventListener('click',function(){var t=order[(order.indexOf(get())+1)%3];
try{t==='auto'?localStorage.removeItem('theme'):localStorage.setItem('theme',t);}catch(e){}
if(t==='auto')delete document.documentElement.dataset.theme;else document.documentElement.dataset.theme=t;show(t);});
show(get());})();</script>"""


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


def attempt_row(a: dict, root: str) -> str:
    counts = outcome_counts(a)
    page = f'{root}{page_of(a["key"])}'
    return (f'<div class="row drow"><div class="id"><a href="{page}">{e(a["label"])}</a></div>'
            f'<div><p class="title"><a href="{page}">{e(a["entry_title"] or a["id"])}</a></p>'
            f'<div class="meta">{bar(counts, "Outcomes", "bar mini")}{legend(counts, compact=True)}</div></div>'
            f'<div class="right">{deprecated_badge() if a.get("deprecated") else tier_badge(a["tier"])}'
            f'<span class="small muted">{e(a["date"])}</span></div></div>')


PROGRESS_METRICS = {
    "datasets": "Datasets attempted",
    "papers": "Papers",
    "attempts": "Attempts",
    "claims": "Claims tested",
    "findings": "Findings about the data",
}


def progress_data(data: dict) -> dict:
    """Daily counts for the overview's dashboard, for all datasets and for CatalystNeuro conversions.

    Each series is a list over the days of what was new that day: dandisets and papers on the date of their first attempt, attempts
    on their own date, and the claims (those resting on the dandiset) and findings of each dandiset's
    current attempts on the date of those attempts.
    """
    ours = {t["key"] for t in data["targets"] if t["catalystneuro"]}
    current = [a for atts in current_attempts(data).values() for a in atts]
    if not data["attempts"]:
        return {"days": [], "series": {}}
    start = datetime.date.fromisoformat(min(a["date"] for a in data["attempts"]))
    end = datetime.date.fromisoformat(max(a["date"] for a in data["attempts"]))
    days = [(start + datetime.timedelta(n)).isoformat() for n in range((end - start).days + 1)]
    series = {}
    for subset, keep in (("all", lambda d: True), ("catalystneuro", lambda d: d in ours)):
        new = {day: {**{m: 0 for m in PROGRESS_METRICS}, **{k: 0 for k in OUTCOMES}} for day in days}
        first_dandiset: dict = {}
        first_paper: dict = {}
        for a in data["attempts"]:
            if not keep(a["key"]):
                continue
            new[a["date"]]["attempts"] += 1
            first_dandiset[a["key"]] = min(first_dandiset.get(a["key"], a["date"]), a["date"])
            first_paper[a["paper"]] = min(first_paper.get(a["paper"], a["date"]), a["date"])
        for day in first_dandiset.values():
            new[day]["datasets"] += 1
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
            "outcomes": {k: {"label": label, "css": css} for k, (label, css, _) in OUTCOMES.items()}}


def progress_panel(data: dict) -> str:
    """The dashboard at the top of the overview: totals, a filter, and two charts of the effort over time.

    The page draws the charts from the JSON it carries (assets/progress.js); without scripts, the table
    below them gives the same numbers.
    """
    p = progress_data(data)
    if len(p["days"]) < 2:
        return ""
    totals = {m: sum(p["series"]["all"][m]) for m in PROGRESS_METRICS}
    tiles = "".join(
        f'<button class="tile metric" type="button" data-metric="{m}" aria-pressed="{str(m == "datasets").lower()}">'
        f'<div class="n">{totals[m]:,}</div><div class="l">{e(label)}</div><div class="delta"></div></button>'
        for m, label in PROGRESS_METRICS.items())
    rows = "".join(
        f"<tr><td>{day}</td>" + "".join(f"<td>{p['series']['all'][m][i]:,}</td>" for m in PROGRESS_METRICS) + "</tr>"
        for i, day in enumerate(p["days"]))
    head = "".join(f"<th>{e(label)}</th>" for label in PROGRESS_METRICS.values())
    return f'''<section class="progress" aria-label="Progress over time">
  <div class="progress-bar">
    <div class="segmented" role="group" aria-label="Which datasets">
      <button type="button" data-subset="all" aria-pressed="true">All datasets</button>
      <button type="button" data-subset="catalystneuro" aria-pressed="false">Converted by CatalystNeuro</button>
    </div>
    <span class="muted small">Totals so far; the small line is the last 7 days.</span>
  </div>
  <div class="tiles metrics">{tiles}</div>
  <div class="grid2" style="margin-top:16px">
    <div class="panel"><h2 id="progress-title">Datasets attempted over time</h2>
      <p class="small muted" style="margin:0">Running total, by day.</p>
      <div class="chart" id="progress-line"></div></div>
    <div class="panel"><h2 id="progress-day-title">Datasets attempted, new each day</h2>
      <p class="small muted" style="margin:0" id="progress-day-note">Each dataset on the date of its first attempt.</p>
      <div class="chart" id="progress-outcomes"></div><div id="progress-legend"></div></div>
  </div>
  <details class="table-view panel"><summary>Table: new each day, all datasets</summary>
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
    tiles = [
        (f'{len(current):,} <span class="of">of {in_queue}</span>', "datasets attempted", "datasets/?status=attempted"),
        (f"{n_claims:,}", "claims attempted", "datasets/?status=attempted"),
        (f"{verified:,}", "datasets independently verified",
         "datasets/?tier=agent_verified,human_verified,author_endorsed"),
        (f'{len(r["findings"]):,}', "findings about the data", "datasets/?status=attempted"),
    ]
    tile_html = "".join(f'<a class="tile" href="{href}"><div class="n">{n}</div><div class="l">{e(label)}</div></a>'
                        for n, label, href in tiles)

    if n_claims:
        outcomes = (bar(counts, f"Outcomes of {n_claims} claims", href=lambda k: f"datasets/?has={k}")
                    + legend(counts, href=lambda k: f"datasets/?has={k}"))
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
            f'<a class="label" href="datasets/?status=attempted&technique={e(t)}">{e(label)}</a>'
            + bar(c, f"{label}: {sum(c.values())} claims", href=lambda k, t=t: f"datasets/?technique={t}&has={k}")
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
                  ordered(blocked, BLOCKED_BY, lambda k: f"datasets/?blocked_by={k}"),
                  "datasets/?has=blocked"),
        breakdown("Findings about the data", ordered(kinds, FINDING_KINDS, lambda k: f"datasets/?found={k}"),
                  "datasets/?status=attempted"),
        breakdown("Verification of attempted datasets",
                  ordered(tiers, TIERS, lambda k: f"datasets/?status=attempted&tier={k}"),
                  "datasets/?status=attempted"),
    ])

    recent = sorted(attempts, key=lambda a: (a["date"], a["key"]), reverse=True)[:6]
    recent_html = "".join(attempt_row(a, "") for a in recent) or '<p class="empty">No attempts yet.</p>'

    dashboard = progress_panel(data)
    redirect = json.dumps({a["id"]: a["key"] for a in data["attempts"]})
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
    {outcomes}{outside_note(attempts)}
    {caution_block()}
  </div>
  <div class="grid2" style="margin-top:16px">{panels}</div>
  <div class="panel" style="padding:0">
    <h2 style="padding:18px 20px 0"><a class="more" href="datasets/?status=attempted">See all</a>Latest attempts</h2>
    <div class="results" style="border:0;border-radius:0 0 10px 10px">{recent_html}</div>
  </div>
</main>'''
    scripts = ('<script>(function(){var m=' + redirect + ',h=location.hash.match(/^#attempt-(.+)$/);'
               'if(h&&m[h[1]])location.replace(m[h[1]]);})();</script>'
               + (f'<script src="{asset("progress.js")}"></script>' if dashboard else ""))
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
CHART_STEPS = [(k, label) for k, label in PIPELINE_STEPS if k != "questions"]


def chart_state(key: str, state: str, note: str) -> str:
    """A cell's state as the chart counts it: a step not reached yet is still to do."""
    if key == "check" and state == "none" and note == "before checks":
        return "older"
    return "todo" if state == "none" else state


def pipeline_chart(counts: dict, total: int) -> str:
    """One bar per step, out of every target: done, made before the step, waiting on a person, to redo, to do."""
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
    return (f'<div class="panel"><h2>Targets at each step</h2><div class="funnel">{rows}</div>'
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
  if(state.q&&(tr.cells[0].textContent+' '+tr.cells[1].textContent).toLowerCase().indexOf(state.q)<0)return false;
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
  $('pcount').textContent=list.length===rows.length?rows.length.toLocaleString()+' targets'
    :list.length.toLocaleString()+' of '+rows.length.toLocaleString()+' targets';
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
    """Where every target stands in the pipeline, and what is waiting on a person."""
    root = "../"
    rows = pipeline_rows(data)
    counts = {key: {} for key, _ in PIPELINE_STEPS}
    for r in rows:
        for key, _ in PIPELINE_STEPS:
            st = r["state"][key][0]
            counts[key][st] = counts[key].get(st, 0) + 1
    # Claims files made before the check existed count as checked, as in the chart.
    older = {key: sum(1 for r in rows if chart_state(key, *r["state"][key]) == "older") for key, _ in PIPELINE_STEPS}
    head = "".join(f'<th>{sort_button(label)}<div class="small muted">{counts[key].get("done", 0) + older[key]:,} done'
                   + (f', {counts[key]["waiting"]:,} waiting' if counts[key].get("waiting") else "")
                   + "</div></th>" for key, label in PIPELINE_STEPS)
    body = ""
    for r in rows:
        name = (f'<a href="{root}{e(r["page"])}">{e(r["dataset"])}</a>' if r["page"] else e(r["dataset"]))
        cells = "".join(f'<td class="ps {e(r["state"][key][0])}" title="{e(r["state"][key][0])}">'
                        f'{e(r["state"][key][1])}</td>' for key, _ in PIPELINE_STEPS)
        states = " ".join(f'data-{key}="{e(r["state"][key][0])}"' for key, _ in PIPELINE_STEPS)
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
                 f'<td class="pname">{e(r["name"])}</td>{cells}<td class="small">{e(r["next"])}'
                 + (f' · <a href="{e(r["issue"])}">waiting on you</a>' if r["issue"] else "") + '</td>'
                 f'<td class="small" data-sort="{sort}">{e(place)}</td>'
                 f'<td class="small" data-sort="{999999 if hours is None else round(hours * 10)}">{e(when)}</td></tr>')
    waiting = [r for r in rows if r["waiting"]]
    papers_missing = sum(len(r["missing"]) for r in waiting)
    charted = {key: {} for key, _ in PIPELINE_STEPS}
    for r in rows:
        for key, _ in PIPELINE_STEPS:
            st = chart_state(key, *r["state"][key])
            charted[key][st] = charted[key].get(st, 0) + 1
    chart = pipeline_chart(charted, len(rows))
    step_opts = "".join(f'<option value="{key}">{e(label)}</option>' for key, label in PIPELINE_STEPS)
    state_opts = "".join(f'<option value="{st}">{e(name)}</option>' for st, name in TABLE_STATES)
    updated = datetime.datetime.fromisoformat(data["generated"]).strftime("%Y-%m-%d %H:%M UTC")
    q = data.get("queue") or {}
    queue_note = ""
    if q.get("full") is not None:
        hours, lanes = q.get("hours") or {}, q.get("lanes") or {}
        def part(kind: str, what: str) -> str:
            n, h, k = len(q.get(kind, [])), hours.get(kind), lanes.get(kind, 1)
            each = (f", at about {h:.1f} hours each" if h and h >= 1 else f", at about {round(h * 60)} minutes each" if h
                    else "")
            return (f'{n:,} dataset{" waits" if n == 1 else "s wait"} for {what} on {k} lane{"s" if k != 1 else ""}{each}'
                    + (f', about {in_hours(n * h / k).removeprefix("about ")} in all' if h and n else ""))
        n_going = len(q.get("running") or {})
        going_note = (f' {n_going:,} chain{" is" if n_going == 1 else "s are"} running now, and the Done in column '
                      'estimates when each will finish from how long the rest of a chain usually takes after the '
                      'role it is on. A branch with nothing running is waiting, on a person or a merge, and has no '
                      'estimate.' if "running" in q else "")
        queue_note = (f' {part("full", "an attempt")}, and {part("claims", "their claims to be read")}. '
                      'The Queue and Done in columns give each dataset’s place and a rough estimate of when it '
                      f'will be done, counted from the last update.{going_note}')
    n_issues = len(data.get("issues", {}))
    issues_note = (f' The runner has stopped on <a href="{REPO_URL}/issues?q=is%3Aissue+is%3Aopen+label%3Aneeds-you">'
                   f'{n_issues:,} dataset{"s" if n_issues != 1 else ""}</a> that need a person.' if n_issues else "")
    html_ = f'''<header class="page">
  <h1>Pipeline</h1>
  <p class="lede">Every target, and where it stands in the
  <a href="{REPO_URL}/blob/main/docs/pipeline.md">pipeline</a>: its paper, the claims read from it and their
  check, the attempt, the questions it raised, and verification. {len(waiting):,} targets are waiting on a person,
  with {papers_missing:,} papers to supply; the list of missing papers is in
  <a href="{REPO_URL}/blob/main/papers/manifest.yaml">papers/manifest.yaml</a>.{issues_note}{queue_note}</p>
  <p class="small muted">Last updated <time id="updated" datetime="{e(data["generated"])}">{e(updated)}</time>.
  The page is rebuilt whenever main changes.</p>
</header>
<main>{chart}
<div class="listbar pipeline-tools" style="margin-top:16px" hidden>
  <input id="pq" type="search" placeholder="Search datasets and names" aria-label="Search datasets and names">
  <select class="ghost" id="pstep" aria-label="Step"><option value="">Any step</option>{step_opts}</select>
  <select class="ghost" id="pstate" aria-label="State"><option value="">Any state</option>{state_opts}</select>
  <strong id="pcount" aria-live="polite"></strong>
</div>
<div class="panel pipeline-wrap"><table class="pipeline">
<thead><tr><th>{sort_button("Dataset")}</th><th>{sort_button("Name")}</th>{head}<th>{sort_button("Next")}</th><th>{sort_button("Queue")}</th><th>{sort_button("Done in")}</th></tr></thead>
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
                 description="Where every target of the reproduction registry stands in its pipeline.")


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


LISTS = {
    "datasets": {
        "title": "Datasets", "noun": "datasets", "data": "data/datasets.json",
        "intro": "Every public dataset whose metadata names a paper, so far all on the DANDI Archive. Attempted ones open a page with the "
                 "claims tested, what was found about the data, and the executed notebook.",
        "facets": [("status", "Status"), ("has", "Has a claim that is"), ("blocked_by", "Has a claim blocked by"),
                   ("tier", "Verification"), ("found", "Findings about the data"),
                   ("converted", "Converted by"), ("technique", "Technique"), ("species", "Species")],
        "sorts": [("-date", "Most recently attempted"), ("id", "Identifier"),
                  ("-id", "Identifier, newest first"), ("-failures", "Most claims not reproduced"),
                  ("size_gb", "Smallest"), ("-size_gb", "Largest"), ("paper_title", "Paper title")],
        "csv": None,
    },
}


def page_list(data: dict, kind: str) -> str:
    spec = LISTS[kind]
    outcome_labels = {k: v[0] for k, v in OUTCOMES.items()}
    config = {
        "kind": kind, "root": "../", "data": spec["data"], "noun": spec["noun"], "csv": spec["csv"],
        "facets": [{"key": k, "label": label} for k, label in spec["facets"]],
        "sorts": [{"key": k, "label": label} for k, label in spec["sorts"]],
        "outcomes": {k: list(v) for k, v in OUTCOMES.items()},
        "order": {"outcome": list(OUTCOMES), "has": list(OUTCOMES), "status": list(STATUS), "tier": list(TIERS)},
        "labels": {
            "outcome": outcome_labels, "has": {**outcome_labels, "(none)": "Not attempted"},
            "blocked_by": {**BLOCKED_BY, "(none)": "No blocked claim"},
            "tier": {**TIERS, "runs": "Not yet verified", "(none)": "Not attempted"},
            "status": STATUS, "found": {**FINDING_KINDS, "(none)": "None recorded"},
            "converted": {"catalystneuro": "CatalystNeuro", "other": "Others or not stated"},
            "verifier": {"disagreed": "Disagreed at first", "(none)": "No disagreement"},
            "technique": {"(none)": "Not stated"}, "species": {"(none)": "Not stated"},
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
                 description=spec["intro"])


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
                links.append(f'<a href="{root}{e(nb["executed"])}">Executed, with outputs</a>')
            if not data["demo"]:
                links.append(f'<a href="{REPO_URL}/blob/main/entries/{e(en["name"])}/{e(nb["path"])}">Source</a>')
            items += (f'<li style="grid-template-columns:1fr max-content"><span><strong>{e(nb["title"])}</strong><br>'
                      f'<span class="muted small">{e(nb["path"])}</span></span>'
                      f'<span>{" · ".join(links) or "Not yet executed"}</span></li>')
        others = [d for d in en["datasets"] if d != dandiset]
        also = (" Also uses " + ", ".join(e(dataset_label(d)) for d in others) + ".") if others else ""
        built_on = (" Builds on " + ", ".join(e(x) for x in en["derived_from"]) + ".") if en["derived_from"] else ""
        code = ("" if data["demo"] else
                f' <a href="{REPO_URL}/tree/main/entries/{e(en["name"])}">All files</a>')
        out += (f'<div class="entry"><p style="margin:18px 0 2px"><span class="tag">{e(ENTRY_TYPES.get(en["type"], en["type"]))}</span> '
                f'<strong>{e(en["title"])}</strong></p>'
                f'<p class="sub small">{e(en["description"])}{also}{built_on}{code}</p>'
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


def page_dandiset(data: dict, dandiset: str, attempt: dict | None = None) -> str:
    """The dandiset's page, from its current attempts; or, given an earlier attempt, that attempt's page."""
    root = "../../../../" if attempt else "../../../"
    current_atts = current_attempts(data)[dandiset]
    atts = [attempt] if attempt else current_atts
    earlier = [a for a in earlier_attempts(data, dandiset) if a is not attempt]
    target = next((t for t in data["targets"] if t["key"] == dandiset), None)
    counts = outcome_counts(atts)
    n = sum(counts.values())
    order = {"reproduced": 0, "partially_reproduced": 1, "not_reproduced": 2}

    # Claims, grouped by paper when the dandiset has attempts on more than one.
    claims_html = ""
    for a in atts:
        paper = a.get("paper_title") or a["paper"]
        claims_html += (f'<p class="sub small" style="margin:14px 0 0">From the paper '
                        f'<a href="https://doi.org/{e(a["paper"])}">{e(paper)}</a></p>')
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
            title = (f'<a href="{root}{e(nb["executed"])}">{e(nb["title"])}</a>' if nb["executed"]
                     else e(nb["title"]))
            claims_html += (f'<div class="claim-group"><h3 style="margin-top:18px">{title} '
                            f'<span class="count">{len(mine)}</span></h3>'
                            f'<p class="sub small" style="margin:2px 0 0">Notebook <code>{e(nb["path"])}</code>'
                            f'</p>{by_outcome(mine, root, a)}</div>')
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
                            f'{by_outcome(blocked, root, a)}</details>')

    all_findings = [f for a in atts for f in a["findings"]]
    findings_html = "".join(
        f'<li><span><a class="kind" href="{root}datasets/?found={e(f["kind"])}">'
        f'{e(FINDING_KINDS.get(f["kind"], f["kind"]))}</a></span><span>{e(f["statement"])}</span></li>'
        for f in all_findings) or '<li><span></span><span class="muted">None recorded.</span></li>'

    notebooks_html, n_notebooks = notebooks_panel(data, dandiset, root)

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
                 ("Made by", ("An agent" if a["kind"] == "agent" else "A person") + f', run by {e(a["accountable"])}'),
                 ("Dataset", f'<a href="{e(archive_url(a["key"]))}">{e(a["label"])}</a>'),
                 ("Version", e(a["dataset_version"] or "not recorded")
                  + (f' (<a href="https://doi.org/{e(a["dataset"]["doi"])}">doi:{e(a["dataset"]["doi"])}</a>)'
                     if a["dataset"].get("doi") else "")
                  + (f', modified {e(a["dataset"]["modified"])}' if a["dataset"].get("modified") else ""))]
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
    repo_folder = f'{dir_of(dandiset)}/attempt-{attempt["id"].rsplit("-", 1)[1]}' if attempt else dir_of(dandiset)
    runs = data.get("transcripts", {}).get(folder, [])
    if runs and not data["demo"]:
        items = "".join(f'<li><a href="{REPO_URL}/blob/main/transcripts/{e(repo_folder)}/{e(name)}">{e(name)}</a></li>'
                        for name in runs)
        provenance_html += ('<h3 style="margin-top:18px">Transcripts of the agent runs</h3>'
                            '<p class="sub small">Each run’s prompt, messages and tool calls, with long output cut '
                            'and the text of the paper left out, and its final report.</p>'
                            f'<ul style="margin:6px 0 0;padding-left:20px">{items}</ul>')
    if earlier:
        provenance_html += ('<p class="sub small" style="margin-top:14px">'
                            + ("Other earlier attempts: " if attempt else "Earlier attempts: ") + ", ".join(
            f'<a href="{root}{page_of(dandiset)}{e(x["id"])}/">{e(x["id"])}</a> ({e(x["date"])})'
            for x in earlier) + "</p>")

    actions = [f'<a href="{e(archive_url(dandiset))}" target="_blank" rel="noopener">View on '
               f'{e(ARCHIVES.get(split_key(dandiset)[0], {}).get("label", split_key(dandiset)[0]))}</a>']
    actions += [f'<a href="https://doi.org/{e(a["paper"])}">Paper</a>' for a in atts] if len(atts) == 1 else []
    actions += [f'<a href="{root}api/{page_of(dandiset).rstrip("/")}.json">JSON</a>',
                f'<a href="{root}#caution">How to read outcomes</a>']

    tags = ""
    if target:
        tags = " ".join(
            [f'<a class="tag" href="{root}datasets/?technique={e(t)}">{e(t)}</a>' for t in target["technique"]]
            + [f'<a class="tag" href="{root}datasets/?species={e(s)}">{e(s)}</a>' for s in target["species"]]
            + ([f'<a class="tag" href="{root}datasets/?converted=catalystneuro" '
                f'title="{e("; ".join(target["catalystneuro"]))}">Converted by CatalystNeuro</a>']
               if target["catalystneuro"] else [])
            + [f'<span class="tag" title="{target["size_gb"]:,.1f} GB">{human_size(target["size_gb"])}</span>',
               f'<span class="tag" title="{target["files"]:,} files">{human_count(target["files"], "file")}</span>'])

    current = current_attempts(data)
    same_paper = [t for t in data["targets"] if target and t["key"] != dandiset
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
    ids = sorted(current)
    i = ids.index(dandiset)
    prev_link = f'<a href="{root}{page_of(ids[i - 1])}">← {dataset_label(ids[i - 1])}</a>' if i > 0 else "<span></span>"
    next_link = (f'<a href="{root}{page_of(ids[i + 1])}">{dataset_label(ids[i + 1])} →</a>' if i < len(ids) - 1
                 else "<span></span>")
    superseded = ""
    if attempt:
        later = next(a["id"] for a in current_atts if a["paper"] == attempt["paper"])
        same_entry = any(a["entry"] == attempt["entry"] for a in current_atts)
        superseded = (f'<p class="deprecated"><strong>An earlier attempt.</strong> Attempt {e(later)} replaced it; '
                      f'<a href="{root}{page_of(dandiset)}">the dataset’s page</a> shows the current '
                      f'outcomes.' + (" Its notebooks link to the entry as it is now, which the later attempt "
                                      "updated; the attempt record is as it was." if same_entry else "") + "</p>")

    tab_defs = [("claims", "Claims", n), ("findings", "Findings about the data", len(all_findings)),
                ("notebooks", "Notebooks", n_notebooks), ("verification", "Verification", n_rounds),
                ("differences", "Method differences", len(deviations)), ("provenance", "Provenance", None)]
    tab_buttons = ""
    for key, label, c in tab_defs:
        count = f' <span class="count">{c}</span>' if c is not None else ""
        tab_buttons += f'<button type="button" role="tab" data-panel="{key}" aria-selected="false">{label}{count}</button>'

    name = (target or {}).get("name") or atts[-1]["entry_title"] or dandiset
    tier = weakest_tier(atts)
    tier_link = f'{root}datasets/?status=attempted&tier={tier}'
    crumb = (f'<a href="{root}{page_of(dandiset)}">{e(dataset_label(dandiset))}</a> / {e(attempt["id"])}' if attempt
             else e(dataset_label(dandiset)))
    body = f'''<header class="page">
  <p class="crumbs"><a href="{root}datasets/">Datasets</a> / {crumb}</p>
  <div class="dhead"><h1>{e(dataset_label(dandiset))}</h1>{tier_badge(tier, tier_link)}</div>
  <p class="sub">{e(name)}</p>
  <div style="display:flex;flex-wrap:wrap;gap:6px 8px;margin-top:8px">{tags}</div>
  <div class="summary">{bar(counts, f"Outcomes of {n} claims", "bar mini")}{legend(counts, compact=True)}</div>
  {outside_note(atts)}
  {superseded}
  <p class="actions">{" ".join(actions)}</p>
</header>
<main>
  <div class="tabs" role="tablist">{tab_buttons}</div>
  <section class="tabpanel" id="claims"><h2>Claims</h2>
    <div class="subtabs" id="claim-filter" role="group" aria-label="Show claims by outcome"></div>
    {claims_html}
    <nav class="pager" id="claim-pager" aria-label="Pages of claims"></nav></section>
  <section class="tabpanel" id="findings"><h2>Findings about the data</h2>
    <p class="sub small" style="margin-top:12px">What attempts found about the dataset itself, for its owner and the
    archive.</p>
    <ul class="findings">{findings_html}</ul></section>
  <section class="tabpanel" id="notebooks"><h2>Notebooks</h2>
    <p class="sub small" style="margin-top:12px">Every registered entry that uses this dataset. An entry can hold
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
    path = f"{page_of(dandiset)}{attempt['id']}/" if attempt else page_of(dandiset)
    title = dandiset_title(dandiset, atts)
    return shell(data, f"{attempt['id']} (earlier attempt) · {title}" if attempt else title, root, "datasets",
                 body, CLAIMS_JS + TABS_JS, path=path, description=dandiset_description(dandiset, atts))


def claims_only(data: dict) -> list[str]:
    """The datasets with claims read from their paper but no attempt yet."""
    current = current_attempts(data)
    return sorted(k for k in data.get("claim_files", {}) if k not in current)


def page_claims(data: dict, key: str) -> str:
    """A dataset's page before its first attempt: the claims read from its paper, and where it stands."""
    root = "../../../"
    target = next((t for t in data["targets"] if t["key"] == key), None)
    row = next((r for r in pipeline_rows(data) if r["key"] == key), None)
    titles = {t["paper"].lower(): t["paper_title"] for t in data["targets"] if t.get("paper")}
    claims_html, n = "", 0
    for f in data["claim_files"][key]:
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
    for sub in ("datasets", "dandisets", "data", "api/dandiset"):
        (output / sub).mkdir(parents=True, exist_ok=True)
    (output / "index.html").write_text(page_overview(data))
    (output / "about").mkdir(exist_ok=True)
    (output / "about" / "index.html").write_text(page_about(data))
    (output / "pipeline").mkdir(exist_ok=True)
    (output / "pipeline" / "index.html").write_text(page_pipeline(data))
    (output / "data" / "pipeline.json").write_text(json.dumps(pipeline_rows(data), separators=(",", ":")) + "\n")
    for kind in LISTS:
        (output / kind / "index.html").write_text(page_list(data, kind))
        (output / "data" / f"{kind}.json").write_text(json.dumps(r[kind], separators=(",", ":")) + "\n")
    for key, attempts in current_attempts(data).items():
        page = output / page_of(key)
        page.mkdir(parents=True, exist_ok=True)
        (page / "index.html").write_text(page_dandiset(data, key))
        for a in earlier_attempts(data, key):
            (page / a["id"]).mkdir(exist_ok=True)
            (page / a["id"] / "index.html").write_text(page_dandiset(data, key, a))
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
            for sub, target in [("", page_of(key))] + [(a["id"] + "/", page_of(key) + a["id"] + "/")
                                                       for a in earlier_attempts(data, key)]:
                (old / sub).mkdir(parents=True, exist_ok=True)
                (old / sub / "index.html").write_text(redirect_page(target, "../../" + ("../" if sub else "")))
            (output / "api" / "dandiset" / f"{split_key(key)[1]}.json").write_text(api)
    for key in claims_only(data):
        page = output / page_of(key)
        page.mkdir(parents=True, exist_ok=True)
        (page / "index.html").write_text(page_claims(data, key))
    (output / "dandisets" / "index.html").write_text(redirect_page("datasets/", "../"))
    (output / "data" / "dandisets.json").write_text((output / "data" / "datasets.json").read_text())
    (output / "registry.json").write_text(json.dumps(data, indent=1) + "\n")
    (output / "sitemap.xml").write_text(sitemap(data))


def redirect_page(target: str, root: str) -> str:
    """A page that sends the reader on to where its content moved, keeping the query and the anchor."""
    url = e(root + target)
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Moved</title>'
            f'<link rel="canonical" href="{e(SITE_URL + target)}"><meta name="robots" content="noindex">'
            f'<meta http-equiv="refresh" content="0; url={url}">'
            f'<script>location.replace("{url}"+location.search+location.hash)</script></head>'
            f'<body><p>This page moved to <a href="{url}">{e(target)}</a>.</p></body></html>\n')


def sitemap(data: dict) -> str:
    """Every page of the site, for search engines; each dataset page dated by its latest attempt."""
    pages = [("", data["generated"][:10]), ("about/", data["generated"][:10]), ("pipeline/", data["generated"][:10])]
    pages += [(f"{kind}/", data["generated"][:10]) for kind in LISTS]
    pages += [(page_of(d), max(a["date"] for a in atts)) for d, atts in current_attempts(data).items()]
    pages += [(page_of(d), data["generated"][:10]) for d in claims_only(data)]
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
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    data = collect(args.output / "notebooks")
    if args.demo:
        data = demo(data, args.demo)
    data["noindex"] = args.noindex
    if args.queue and args.queue.is_file():
        data["queue"] = json.loads(args.queue.read_text())
    if args.issues and args.issues.is_file():
        # An issue's title is "<dataset label>: waiting on you" (tools/notify.py).
        data["issues"] = {i["title"].rsplit(": waiting on you", 1)[0]: i["url"]
                          for i in json.loads(args.issues.read_text()) if i["title"].endswith(": waiting on you")}
    build(data, args.output)
    print(f"wrote {args.output} ({len(data['attempts'])} attempts, {len(data['targets'])} targets"
          f"{', DEMO DATA' if data['demo'] else ''})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
