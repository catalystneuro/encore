"""Build the public dashboard: a static site from the registry's own files.

    python tools/build_site.py [--output site]
    python tools/build_site.py --demo 150 --output /tmp/demo-site

Reads targets/dandisets.json, targets/pilot.yaml, claims/, attempts/,
entries/ and transcripts/, and writes:

    index.html                    overview: numbers, breakdowns, latest attempts
    dandisets/index.html          every target, filterable and paginated
    dandisets/<id>/index.html     one static page per attempted dandiset
    data/dandisets.json           rows for the list page
    api/dandiset/<id>.json        one dandiset's results, for other sites
    registry.json                 everything, as before
    assets/                       app.css and list.js from tools/site_assets/

If <output>/notebooks/<entry>/<notebook>.html exists (the executed notebooks
CI keeps on the `executed` branch), pages link to it.

The list pages are rendered in the browser by assets/list.js from the JSON
rows; filters, search, sort and page are kept in the URL, so every view is a
link. Dandiset pages are complete HTML and need no JavaScript.

The trust tier of an attempt is derived from its verifications: the latest
verification decides, and it counts only if it agrees with every outcome.

`--demo N` builds from N made-up attempts on real targets, to see and test the
site at scale. A demo build says so on every page; never publish one.

Requires `pyyaml`.
"""

from __future__ import annotations

import argparse
import datetime
import html
import json
import random
import shutil
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
ASSETS = Path(__file__).resolve().parent / "site_assets"
REPO_URL = "https://github.com/catalystneuro/reproduction-registry"

OUTCOMES = {  # key: (label, css class, icon)
    "reproduced": ("Reproduced", "good", "✓"),
    "partially_reproduced": ("Partially reproduced", "warning", "◐"),
    "not_reproduced": ("Not reproduced", "critical", "✕"),
    "blocked": ("Blocked", "blocked", "⊘"),
}
BLOCKED_BY = {
    "data_missing": "Data missing from the dandiset",
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


# --- collecting ---------------------------------------------------------------

def collect(executed: Path | None = None) -> dict:
    queue = json.loads((ROOT / "targets" / "dandisets.json").read_text())
    pilot = {t["dandiset"] for t in load_yaml(ROOT / "targets" / "pilot.yaml")["targets"]}
    claims = {}
    for path in sorted((ROOT / "claims").glob("*/*.yaml")):
        data = load_yaml(path)
        claims[(data["dandiset"], data["paper"])] = {c["id"]: c for c in data["claims"]}
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
        known = claims.get((a["dandiset"], a["paper"]), {})
        entry = entries.get(a.get("entry"))
        verifications = a.get("verifications") or []
        disagreed = {r["claim"] for v in verifications for r in v["results"] if not r.get("agrees")}
        attempts.append({
            "id": a["id"],
            "dandiset": a["dandiset"],
            "dandiset_version": a.get("dandiset_version"),
            "paper": a["paper"].removeprefix("doi:"),
            "paper_title": titles.get(a["paper"].removeprefix("doi:").lower()),
            "date": str(a["date"]),
            "kind": a["provenance"]["kind"],
            "accountable": a["provenance"]["accountable"]["name"],
            "agent": a["provenance"].get("agent"),
            "tier": tier_of(a),
            "entry": a.get("entry"),
            "entry_title": entry["title"] if entry else None,
            "description": squash(entry.get("description")) if entry else None,
            "notebooks": notebooks_of(entry) if entry else [],
            "outcomes": [{
                "claim": o["claim"],
                "statement": squash(known.get(o["claim"], {}).get("statement", o["claim"])),
                "source": known.get(o["claim"], {}).get("source"),
                "outcome": o["outcome"],
                "blocked_by": o.get("blocked_by"),
                "notebook": o.get("notebook"),
                "notes": squash(o.get("notes")),
                "deviations": [squash(d) for d in o.get("deviations") or []],
                "disagreed": o["claim"] in disagreed,
                "data": known.get(o["claim"], {}).get("data", "dandiset"),
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

    attempted = {a["dandiset"] for a in attempts}
    targets = []
    for t in queue["targets"]:
        papers = [p for p in t["papers"] if not p["preprint"]] or t["papers"]
        status = "attempted" if t["dandiset"] in attempted else "pilot" if t["dandiset"] in pilot else "open"
        targets.append({
            "dandiset": t["dandiset"], "name": t["name"], "size_gb": t["size_gb"],
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
            "dandisets": sorted({r["id"].split(":", 1)[1].split("/")[0] for r in related
                                 if r["id"].startswith("dandi:")}),
            "papers": [r["id"].split(":", 1)[1] for r in related if r["id"].startswith("doi:")],
            "derived_from": [r["id"].split(":", 1)[1] for r in related
                             if r["id"].startswith("entry:") and r["relation"] == "derived_from"],
            "notebooks": notebooks_of(entry),
        })
    transcripts = {d.name: sorted(p.name for p in d.glob("*.md"))
                   for d in sorted((ROOT / "transcripts").glob("*")) if d.is_dir()}
    return finish({
        "transcripts": transcripts,
        "generated": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
        "queue_generated": queue["generated"],
        "queue_counts": queue["counts"],
        "attempts": attempts,
        "entries": entry_list,
        "targets": targets,
        "demo": False,
    })


def finish(data: dict) -> dict:
    """Totals, and each target's status, derived from the attempts."""
    data["outcome_counts"] = outcome_counts(data["attempts"])
    data["outcome_counts_with_outside_data"] = outcome_counts(data["attempts"], outside=True)
    attempted = {a["dandiset"] for a in data["attempts"]}
    for t in data["targets"]:
        if t["dandiset"] in attempted:
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
            "id": f"{t['dandiset']}-demo-01", "dandiset": t["dandiset"], "dandiset_version": "draft",
            "paper": t["paper"], "paper_title": t["paper_title"], "date": date, "kind": "agent",
            "accountable": "Demo",
            "agent": {"harness": "demo", "model": "demo", "protocol": "demo"}, "tier": tier,
            "entry": f"{t['dandiset']}-demo", "entry_title": t["paper_title"],
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
                "description": a["description"], "dandisets": [a["dandiset"]], "papers": [a["paper"]],
                "derived_from": [], "notebooks": a["notebooks"]} for a in attempts]
    out = dict(data, attempts=attempts, entries=entries, demo=True,
               targets=[dict(t, status="pilot" if t["status"] == "pilot" else "open") for t in data["targets"]])
    return finish(out)


# --- flat rows for the list pages ----------------------------------------------

TIER_ORDER = list(TIERS)


def current_attempts(data: dict) -> dict[str, list[dict]]:
    """For each dandiset, the latest attempt on each of its papers, oldest first."""
    latest: dict = {}
    for a in sorted(data["attempts"], key=lambda a: (a["date"], a["id"])):
        latest[(a["dandiset"], a["paper"])] = a
    out: dict = {}
    for a in sorted(latest.values(), key=lambda a: (a["date"], a["id"])):
        out.setdefault(a["dandiset"], []).append(a)
    return out


def outcome_counts(attempts, outside: bool = False) -> dict:
    """Outcome totals over one attempt or a list of them.

    By default only the claims that rest on the dandiset alone; with `outside`, only the claims that
    also use data from elsewhere. The two are never added together, so that an outcome that may
    reflect the outside data does not count as a judgement of the dandiset.
    """
    attempts = [attempts] if isinstance(attempts, dict) else attempts
    # Names for the dandiset's own codes taken from elsewhere (`with_labels`) count as the dandiset.
    return {k: sum(1 for a in attempts for o in a["outcomes"]
                   if o["outcome"] == k and (o.get("data") == "with_inputs") == outside) for k in OUTCOMES}


def outside_note(attempts, root: str = "") -> str:
    """A line with the outcomes of the claims that also use outside data, when there are any."""
    counts = outcome_counts(attempts, outside=True)
    m = sum(counts.values())
    if not m:
        return ""
    claims = "1 claim that also uses" if m == 1 else f"{m} claims that also use"
    return (f'<p class="sub small" style="margin-top:8px">Counted separately: {claims} data from outside '
            f'the dandiset.</p>'
            f'<div class="summary">{bar(counts, f"Outcomes of {m} claims using outside data", "bar mini")}'
            f'{legend(counts, compact=True)}</div>')


def weakest_tier(attempts: list[dict]) -> str:
    """A dandiset is only as verified as its least verified attempt."""
    return min((a["tier"] for a in attempts), key=TIER_ORDER.index)


def entries_for(data: dict, dandiset: str) -> list[dict]:
    """Every entry whose metadata says it uses this dandiset."""
    return [en for en in data["entries"] if dandiset in en["dandisets"]]


def notebook_of(attempt: dict, path: str | None) -> dict | None:
    return next((n for n in attempt["notebooks"] if n["path"] == path), None)


def rows(data: dict) -> dict[str, list]:
    current = current_attempts(data)
    by_id = {t["dandiset"]: t for t in data["targets"]}
    dandisets, claims, findings = [], [], []
    for t in data["targets"]:
        atts = current.get(t["dandiset"])
        outcomes = [o for a in atts or [] for o in a["outcomes"]]
        dandisets.append({
            "id": t["dandiset"], "name": t["name"], "paper": t["paper"], "paper_title": t["paper_title"],
            "technique": t["technique"], "species": t["species"], "size_gb": t["size_gb"], "files": t["files"],
            "status": t["status"], "tier": weakest_tier(atts) if atts else None,
            "date": max(a["date"] for a in atts) if atts else None,
            "counts": outcome_counts(atts) if atts else None,
            "claims": len(outcomes) if atts else None,
            "failures": sum(1 for o in outcomes if o["outcome"] == "not_reproduced") if atts else None,
            "has": sorted({o["outcome"] for o in outcomes}),
            "blocked_by": sorted({o["blocked_by"] for o in outcomes if o["blocked_by"]}),
            "notebooks": sum(len(en["notebooks"]) for en in entries_for(data, t["dandiset"])),
            "page": f'dandisets/{t["dandiset"]}/' if atts else None,
            "findings": sum(len(a["findings"]) for a in atts) if atts else None,
            "found": sorted({f["kind"] for a in atts or [] for f in a["findings"]}),
            "converted": "catalystneuro" if t["catalystneuro"] else "other",
        })
    for atts in current.values():
        for a in atts:
            t = by_id.get(a["dandiset"], {})
            common = {"dandiset": a["dandiset"], "page": f'dandisets/{a["dandiset"]}/', "tier": a["tier"],
                      "technique": t.get("technique", []), "species": t.get("species", []),
                      "paper_title": a.get("paper_title") or t.get("paper_title") or a["entry_title"],
                      "date": a["date"]}
            for o in a["outcomes"]:
                nb = notebook_of(a, o.get("notebook"))
                claims.append({**common, "claim": o["claim"], "statement": o["statement"], "source": o["source"],
                               "outcome": o["outcome"], "blocked_by": o["blocked_by"], "notes": o["notes"],
                               "deviations": o["deviations"], "disagreed": o["disagreed"],
                               "verifier": "disagreed" if o["disagreed"] else None,
                               "notebook": nb["executed"] if nb else None,
                               "notebook_title": nb["title"] if nb else None})
            for f in a["findings"]:
                findings.append({**common, "kind": f["kind"], "statement": f["statement"]})
    return {"dandisets": dandisets, "claims": claims, "findings": findings}


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


def tier_badge(tier: str, href: str | None = None) -> str:
    verified = tier != "runs"
    text = ("✓ " if verified else "") + (TIERS[tier] if verified else "Not yet verified")
    css = "tier" + ("" if verified else " pending")
    return f'<a class="{css}" href="{e(href)}">{e(text)}</a>' if href else f'<span class="{css}">{e(text)}</span>'


def claim_item(o: dict, root: str, attempt: dict | None = None) -> str:
    """One claim as an accordion: the outcome and statement show, the explanation opens on a click."""
    blocked = f'<span class="why">· {e(BLOCKED_BY.get(o["blocked_by"], o["blocked_by"]))}</span>' \
        if o["blocked_by"] else ""
    source = f'<span class="source">{e(o["source"])}</span>' if o["source"] else ""
    tags = '<span class="tag">verifier disagreed at first</span>' if o["disagreed"] else ""
    if o.get("data") == "with_inputs":
        tags += '<span class="tag">uses data from outside the dandiset</span>'
    elif o.get("data") == "with_labels":
        tags += '<span class="tag">names its codes from outside the dandiset</span>'
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


def shell(data: dict, title: str, root: str, active: str, body: str, scripts: str = "") -> str:
    r = rows_cache(data)
    tabs = [("overview", "Overview", root or "./", None),
            ("dandisets", "Dandisets", f"{root}dandisets/", len({a["dandiset"] for a in data["attempts"]}))]
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
<meta name="description" content="Which findings of papers can be reproduced from the open data on the DANDI Archive.">
<script>try{{var t=localStorage.getItem("theme");if(t==="light"||t==="dark")document.documentElement.dataset.theme=t;}}catch(e){{}}</script>
<link rel="icon" href="{root}assets/favicon.svg" type="image/svg+xml">
<link rel="alternate icon" href="{root}assets/favicon-32.png" type="image/png" sizes="32x32">
<link rel="apple-touch-icon" href="{root}assets/favicon-180.png">
<link rel="stylesheet" href="{root}assets/app.css"></head><body>
{banner}<nav class="top" aria-label="Sections"><div class="wrap">
  <a class="brand" href="{home}">Reproduction registry</a>{nav}
  <a class="tab ext" href="{REPO_URL}">GitHub</a>
  <a class="tab ext" href="{REPO_URL}/actions" title="The workflows that run the agents and check the entries">Agent runs</a>
  <button class="theme" id="theme" type="button" aria-label="Colour theme: auto. Change theme" title="Colour theme"><span aria-hidden="true">◐</span><span class="t">Auto</span></button>
</div></nav>
<div class="wrap">
{body}
<footer>Generated {e(data["generated"][:10])} from the registry's files ·
<a href="{root}registry.json">Data as JSON</a> · <a href="{REPO_URL}">Repository</a> ·
<a href="{REPO_URL}/blob/main/docs/design.md">How it works</a>. Outcomes describe what one attempt could reproduce from
the data in the dandiset, with the methods available. A failure to reproduce may be a failure of the agent, and is not
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
    <p>An outcome says what one attempt could recover from the data in a dandiset, with the methods available to it. A
    “not reproduced” or “partially reproduced” outcome can come from a mistake or a limitation in the agent’s analysis,
    from methods the paper does not describe fully, from data that is not in the dandiset, or from a dandiset that
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
    page = f'{root}dandisets/{e(a["dandiset"])}/'
    return (f'<div class="row drow"><div class="id"><a href="{page}">{e(a["dandiset"])}</a></div>'
            f'<div><p class="title"><a href="{page}">{e(a["entry_title"] or a["id"])}</a></p>'
            f'<div class="meta">{bar(counts, "Outcomes", "bar mini")}{legend(counts, compact=True)}</div></div>'
            f'<div class="right">{tier_badge(a["tier"])}<span class="small muted">{e(a["date"])}</span></div></div>')


def page_overview(data: dict) -> str:
    r = rows_cache(data)
    current = current_attempts(data)
    attempts = [a for atts in current.values() for a in atts]
    counts = outcome_counts(attempts)
    n_claims = sum(counts.values())
    in_queue = data["queue_counts"]["with_a_paper"]
    verified = sum(1 for atts in current.values() if weakest_tier(atts) != "runs")
    tiles = [
        (f'{len(current):,} <span class="of">of {in_queue}</span>', "dandisets attempted", "dandisets/?status=attempted"),
        (f"{n_claims:,}", "claims attempted", "dandisets/?status=attempted"),
        (f"{verified:,}", "dandisets independently verified",
         "dandisets/?tier=agent_verified,human_verified,author_endorsed"),
        (f'{len(r["findings"]):,}', "findings about the data", "dandisets/?status=attempted"),
    ]
    tile_html = "".join(f'<a class="tile" href="{href}"><div class="n">{n}</div><div class="l">{e(label)}</div></a>'
                        for n, label, href in tiles)

    if n_claims:
        outcomes = (bar(counts, f"Outcomes of {n_claims} claims", href=lambda k: f"dandisets/?has={k}")
                    + legend(counts, href=lambda k: f"dandisets/?has={k}"))
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
            f'<a class="label" href="dandisets/?status=attempted&technique={e(t)}">{e(label)}</a>'
            + bar(c, f"{label}: {sum(c.values())} claims", href=lambda k, t=t: f"dandisets/?technique={t}&has={k}")
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
                  ordered(blocked, BLOCKED_BY, lambda k: f"dandisets/?blocked_by={k}"),
                  "dandisets/?has=blocked"),
        breakdown("Findings about the data", ordered(kinds, FINDING_KINDS, lambda k: f"dandisets/?found={k}"),
                  "dandisets/?status=attempted"),
        breakdown("Verification of attempted dandisets",
                  ordered(tiers, TIERS, lambda k: f"dandisets/?status=attempted&tier={k}"),
                  "dandisets/?status=attempted"),
    ])

    recent = sorted(attempts, key=lambda a: (a["date"], a["dandiset"]), reverse=True)[:6]
    recent_html = "".join(attempt_row(a, "") for a in recent) or '<p class="empty">No attempts yet.</p>'

    redirect = json.dumps({a["id"]: a["dandiset"] for a in data["attempts"]})
    body = f'''<header class="page" id="top">
  <h1>Can the findings of a paper be reproduced from its open data?</h1>
  <p class="lede">Agents and people take papers whose data is on the <a href="https://dandiarchive.org">DANDI Archive</a>
  and try to reproduce their key findings from that data alone. Every finding gets an outcome, whether or not it
  worked, and every attempt records what it learned about the data. The notebooks are a starting point for new analyses.</p>
  <div class="tiles">{tile_html}</div>
</header>
<main>
  <div class="panel">
    <h2>Outcomes of the {n_claims:,} claims that rest on the dandiset alone</h2>
    {outcomes}{outside_note(attempts)}
    {caution_block()}
  </div>
  <div class="grid2" style="margin-top:16px">{panels}</div>
  <div class="panel" style="padding:0">
    <h2 style="padding:18px 20px 0"><a class="more" href="dandisets/?status=attempted">See all</a>Latest attempts</h2>
    <div class="results" style="border:0;border-radius:0 0 10px 10px">{recent_html}</div>
  </div>
</main>'''
    scripts = ('<script>(function(){var m=' + redirect + ',h=location.hash.match(/^#attempt-(.+)$/);'
               'if(h&&m[h[1]])location.replace("dandisets/"+m[h[1]]+"/");})();</script>')
    return shell(data, "Reproduction registry", "", "overview", body, scripts)


LISTS = {
    "dandisets": {
        "title": "Dandisets", "noun": "dandisets", "data": "data/dandisets.json",
        "intro": "Every public dandiset on DANDI whose metadata names a paper. Attempted ones open a page with the "
                 "claims tested, what was found about the data, and the executed notebook.",
        "facets": [("status", "Status"), ("has", "Has a claim that is"), ("blocked_by", "Has a claim blocked by"),
                   ("tier", "Verification"), ("found", "Findings about the data"),
                   ("converted", "Converted by"), ("technique", "Technique"), ("species", "Species")],
        "sorts": [("-date", "Most recently attempted"), ("id", "Dandiset number"),
                  ("-id", "Dandiset number, newest first"), ("-failures", "Most claims not reproduced"),
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
               f'<script src="../assets/list.js"></script>')
    return shell(data, f'{spec["title"]} · Reproduction registry', "../", kind, body, scripts)


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
[].slice.call(panel.querySelectorAll('.claim-group')).forEach(function(g){
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
        return '<p class="muted" style="margin-top:14px">No notebooks use this dandiset yet.</p>', 0
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
        others = [d for d in en["dandisets"] if d != dandiset]
        also = (" Also uses " + ", ".join(f"dandiset {e(d)}" for d in others) + ".") if others else ""
        built_on = (" Builds on " + ", ".join(e(x) for x in en["derived_from"]) + ".") if en["derived_from"] else ""
        code = ("" if data["demo"] else
                f' <a href="{REPO_URL}/tree/main/entries/{e(en["name"])}">All files</a>')
        out += (f'<div class="entry"><p style="margin:18px 0 2px"><span class="tag">{e(ENTRY_TYPES.get(en["type"], en["type"]))}</span> '
                f'<strong>{e(en["title"])}</strong></p>'
                f'<p class="sub small">{e(en["description"])}{also}{built_on}{code}</p>'
                f'<ul class="plain">{items}</ul></div>')
    return out, count


def page_dandiset(data: dict, dandiset: str) -> str:
    root = "../../"
    atts = current_attempts(data)[dandiset]
    earlier = [a for a in data["attempts"] if a["dandiset"] == dandiset and a not in atts]
    target = next((t for t in data["targets"] if t["dandiset"] == dandiset), None)
    counts = outcome_counts(atts)
    n = sum(counts.values())
    order = {"not_reproduced": 0, "partially_reproduced": 1, "reproduced": 2}

    # Claims, grouped by paper when the dandiset has attempts on more than one.
    claims_html = ""
    for a in atts:
        paper = a.get("paper_title") or a["paper"]
        claims_html += (f'<p class="sub small" style="margin:14px 0 0">From the paper '
                        f'<a href="https://doi.org/{e(a["paper"])}">{e(paper)}</a></p>')
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
                            f'</p><ul class="claims">{"".join(claim_item(o, root, a) for o in mine)}</ul></div>')
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
                            f'<ul class="claims">{"".join(claim_item(o, root, a) for o in blocked)}</ul></details>')

    all_findings = [f for a in atts for f in a["findings"]]
    findings_html = "".join(
        f'<li><span><a class="kind" href="{root}dandisets/?found={e(f["kind"])}">'
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
                 ("Dandiset version", e(a["dandiset_version"] or "not recorded"))]
        if a["kind"] == "agent":
            rows_ += [("Harness", e(agent.get("harness", "not recorded"))),
                      ("Model", e(agent.get("model", "not recorded"))),
                      ("Protocol", e(agent.get("protocol", "not recorded")))]
        provenance_html += ('<dl class="kv" style="margin-top:14px">'
                            + "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in rows_) + "</dl>")
    runs = data.get("transcripts", {}).get(dandiset, [])
    if runs and not data["demo"]:
        items = "".join(f'<li><a href="{REPO_URL}/blob/main/transcripts/{e(dandiset)}/{e(name)}">{e(name)}</a></li>'
                        for name in runs)
        provenance_html += ('<h3 style="margin-top:18px">Transcripts of the agent runs</h3>'
                            '<p class="sub small">Each run’s prompt, messages and tool calls, with long output cut '
                            'and the text of the paper left out, and its final report.</p>'
                            f'<ul style="margin:6px 0 0;padding-left:20px">{items}</ul>')
    if earlier:
        provenance_html += ('<p class="sub small" style="margin-top:14px">Earlier attempts: ' + ", ".join(
            f'{e(x["id"])} ({e(x["date"])})' for x in earlier) + "</p>")

    actions = [f'<a href="https://dandiarchive.org/dandiset/{e(dandiset)}">View on DANDI</a>']
    actions += [f'<a href="https://doi.org/{e(a["paper"])}">Paper</a>' for a in atts] if len(atts) == 1 else []
    actions += [f'<a href="{root}api/dandiset/{e(dandiset)}.json">JSON</a>',
                f'<a href="{root}#caution">How to read outcomes</a>']

    tags = ""
    if target:
        tags = " ".join(
            [f'<a class="tag" href="{root}dandisets/?technique={e(t)}">{e(t)}</a>' for t in target["technique"]]
            + [f'<a class="tag" href="{root}dandisets/?species={e(s)}">{e(s)}</a>' for s in target["species"]]
            + ([f'<a class="tag" href="{root}dandisets/?converted=catalystneuro" '
                f'title="{e("; ".join(target["catalystneuro"]))}">Converted by CatalystNeuro</a>']
               if target["catalystneuro"] else [])
            + [f'<span class="tag" title="{target["size_gb"]:,.1f} GB">{human_size(target["size_gb"])}</span>',
               f'<span class="tag" title="{target["files"]:,} files">{human_count(target["files"], "file")}</span>'])

    current = current_attempts(data)
    same_paper = [t for t in data["targets"] if target and t["dandiset"] != dandiset
                  and set(t["papers"]) & set(target["papers"])]
    related = ""
    if same_paper:
        links = ""
        for t in same_paper:
            if t["dandiset"] in current:
                links += f'<a href="../{e(t["dandiset"])}/">Dandiset {e(t["dandiset"])}</a> '
            else:
                links += (f'<span><a href="https://dandiarchive.org/dandiset/{e(t["dandiset"])}">Dandiset '
                          f'{e(t["dandiset"])}</a> <span class="muted">(not attempted)</span></span> ')
        related = (f'<div class="panel" style="margin-top:28px"><h2>Other dandisets that name the same paper</h2>'
                   f'<div class="related">{links}</div></div>')
    ids = sorted(current)
    i = ids.index(dandiset)
    prev_link = f'<a href="../{ids[i - 1]}/">← Dandiset {ids[i - 1]}</a>' if i > 0 else "<span></span>"
    next_link = f'<a href="../{ids[i + 1]}/">Dandiset {ids[i + 1]} →</a>' if i < len(ids) - 1 else "<span></span>"

    tab_defs = [("claims", "Claims", n), ("findings", "Findings about the data", len(all_findings)),
                ("notebooks", "Notebooks", n_notebooks), ("verification", "Verification", n_rounds),
                ("differences", "Method differences", len(deviations)), ("provenance", "Provenance", None)]
    tab_buttons = ""
    for key, label, c in tab_defs:
        count = f' <span class="count">{c}</span>' if c is not None else ""
        tab_buttons += f'<button type="button" role="tab" data-panel="{key}" aria-selected="false">{label}{count}</button>'

    name = (target or {}).get("name") or atts[-1]["entry_title"] or dandiset
    tier = weakest_tier(atts)
    tier_link = f'{root}dandisets/?status=attempted&tier={tier}'
    body = f'''<header class="page">
  <p class="crumbs"><a href="{root}dandisets/">Dandisets</a> / {e(dandiset)}</p>
  <div class="dhead"><h1>Dandiset {e(dandiset)}</h1>{tier_badge(tier, tier_link)}</div>
  <p class="sub">{e(name)}</p>
  <div style="display:flex;flex-wrap:wrap;gap:6px 8px;margin-top:8px">{tags}</div>
  <div class="summary">{bar(counts, f"Outcomes of {n} claims", "bar mini")}{legend(counts, compact=True)}</div>
  {outside_note(atts)}
  <p class="actions">{" ".join(actions)}</p>
</header>
<main>
  <div class="tabs" role="tablist">{tab_buttons}</div>
  <section class="tabpanel" id="claims"><h2>Claims</h2>
    <div class="subtabs" id="claim-filter" role="group" aria-label="Show claims by outcome"></div>
    {claims_html}
    <nav class="pager" id="claim-pager" aria-label="Pages of claims"></nav></section>
  <section class="tabpanel" id="findings"><h2>Findings about the data</h2>
    <p class="sub small" style="margin-top:12px">What attempts found about the dandiset itself, for its owner and the
    archive.</p>
    <ul class="findings">{findings_html}</ul></section>
  <section class="tabpanel" id="notebooks"><h2>Notebooks</h2>
    <p class="sub small" style="margin-top:12px">Every registered entry that uses this dandiset. An entry can hold
    several notebooks, and can use more than one dandiset.</p>
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
    return shell(data, f"Dandiset {dandiset} · Reproduction registry", root, "dandisets", body,
                 CLAIMS_JS + TABS_JS)


# --- writing -------------------------------------------------------------------

def build(data: dict, output: Path) -> None:
    r = rows_cache(data)
    output.mkdir(parents=True, exist_ok=True)
    shutil.copytree(ASSETS, output / "assets", dirs_exist_ok=True)
    for sub in ("dandisets", "data", "api/dandiset"):
        (output / sub).mkdir(parents=True, exist_ok=True)
    (output / "index.html").write_text(page_overview(data))
    for kind in LISTS:
        (output / kind / "index.html").write_text(page_list(data, kind))
        (output / "data" / f"{kind}.json").write_text(json.dumps(r[kind], separators=(",", ":")) + "\n")
    for dandiset, attempts in current_attempts(data).items():
        page = output / "dandisets" / dandiset
        page.mkdir(exist_ok=True)
        (page / "index.html").write_text(page_dandiset(data, dandiset))
        (output / "api" / "dandiset" / f"{dandiset}.json").write_text(json.dumps({
            "dandiset": dandiset, "page": f"dandisets/{dandiset}/", "generated": data["generated"],
            "caution": CAUTION + " It may be a failure of the attempt.",
            "outcome_counts": outcome_counts(attempts),
            "outcome_counts_with_outside_data": outcome_counts(attempts, outside=True), "attempts": attempts,
            "entries": entries_for(data, dandiset),
        }, indent=1) + "\n")
    (output / "registry.json").write_text(json.dumps(data, indent=1) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--output", type=Path, default=ROOT / "site")
    parser.add_argument("--demo", type=int, metavar="N",
                        help="build from N made-up attempts, to test the site at scale; never publish")
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    data = collect(args.output / "notebooks")
    if args.demo:
        data = demo(data, args.demo)
    build(data, args.output)
    print(f"wrote {args.output} ({len(data['attempts'])} attempts, {len(data['targets'])} targets"
          f"{', DEMO DATA' if data['demo'] else ''})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
