"""Build the public dashboard: one static page from the registry's own files.

    python tools/build_site.py [--output site]

Reads targets/dandisets.json, targets/pilot.yaml, claims/, attempts/ and
entries/, and writes <output>/index.html (self-contained, no external
resources) and <output>/registry.json (the same data, for other sites).

The trust tier of an attempt is derived from its verifications: the latest
verification decides, and it counts only if it agrees with every outcome.

Requires `pyyaml`.
"""

from __future__ import annotations

import argparse
import datetime
import html
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
REPO_URL = "https://github.com/catalystneuro/reproduction-registry"

OUTCOMES = {  # key: (label, css class, icon)
    "reproduced": ("Reproduced", "good", "✓"),
    "partially_reproduced": ("Partially reproduced", "warning", "◐"),
    "not_reproduced": ("Not reproduced", "critical", "✕"),
    "blocked": ("Blocked", "blocked", "⊘"),
}
BLOCKED_BY = {
    "data_missing": "data missing from the dandiset",
    "metadata_insufficient": "metadata insufficient",
    "methods_underspecified": "methods underspecified",
    "data_unreadable": "data unreadable",
    "too_large": "too large to analyse",
    "other": "other",
}
TIERS = {
    "runs": "Runs in CI",
    "agent_verified": "Verified by an independent agent",
    "human_verified": "Verified by a person",
    "author_endorsed": "Endorsed by a paper author",
}
FINDING_KINDS = {
    "metadata_error": "Metadata error",
    "data_missing": "Data missing",
    "identifier_missing": "Identifier missing",
    "selection_undocumented": "Selection not documented",
    "methods_unavailable": "Methods not available",
    "other": "Other",
}
VERIFICATION_TIER = {"agent": "agent_verified", "person": "human_verified",
                     "paper_author": "author_endorsed"}


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


def collect() -> dict:
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

    attempts = []
    for path in sorted((ROOT / "attempts").glob("*.yaml")):
        a = load_yaml(path)
        known = claims.get((a["dandiset"], a["paper"]), {})
        entry = entries.get(a.get("entry"))
        attempts.append({
            "id": a["id"],
            "dandiset": a["dandiset"],
            "dandiset_version": a.get("dandiset_version"),
            "paper": a["paper"].removeprefix("doi:"),
            "date": str(a["date"]),
            "kind": a["provenance"]["kind"],
            "accountable": a["provenance"]["accountable"]["name"],
            "tier": tier_of(a),
            "entry": a.get("entry"),
            "entry_title": entry["title"] if entry else None,
            "notebooks": [n["path"] for n in entry["notebooks"]] if entry else [],
            "outcomes": [{
                "claim": o["claim"],
                "statement": known.get(o["claim"], {}).get("statement", o["claim"]),
                "source": known.get(o["claim"], {}).get("source"),
                "outcome": o["outcome"],
                "blocked_by": o.get("blocked_by"),
                "notes": " ".join((o.get("notes") or "").split()),
                "deviations": [" ".join(d.split()) for d in o.get("deviations") or []],
            } for o in a["outcomes"]],
            "findings": [{"kind": f["kind"], "statement": " ".join(f["statement"].split())}
                         for f in a.get("findings") or []],
            "verifications": [{
                "date": str(v["date"]), "kind": v["kind"],
                "agreed": sum(1 for r in v["results"] if r.get("agrees")),
                "of": len(v["results"]),
            } for v in a.get("verifications") or []],
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
            "n_papers": len(t["papers"]),
            "approach": "; ".join(a.replace(" approach", "") for a in t["approaches"][:2]),
        })

    counts = {k: 0 for k in OUTCOMES}
    for a in attempts:
        for o in a["outcomes"]:
            counts[o["outcome"]] += 1
    return {
        "generated": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
        "queue_generated": queue["generated"],
        "queue_counts": queue["counts"],
        "outcome_counts": counts,
        "attempts": attempts,
        "targets": targets,
    }


# --- rendering ----------------------------------------------------------------

def e(text) -> str:
    return html.escape(str(text if text is not None else ""), quote=True)


def chip(outcome: str) -> str:
    label, css, icon = OUTCOMES[outcome]
    return f'<span class="chip {css}"><span class="icon" aria-hidden="true">{icon}</span>{label}</span>'


def outcome_bar(counts: dict) -> str:
    total = sum(counts.values())
    if not total:
        return '<p class="muted">No claims attempted yet.</p>'
    segments, legend = [], []
    for key, (label, css, icon) in OUTCOMES.items():
        n = counts[key]
        legend.append(f'<li><span class="swatch {css}" aria-hidden="true">{icon}</span>'
                      f'{label} <strong>{n}</strong></li>')
        if n:
            segments.append(f'<div class="seg {css}" style="flex:{n}" '
                            f'title="{label}: {n} of {total}"></div>')
    return (f'<div class="bar" role="img" aria-label="Outcomes of {total} claims attempted">'
            + "".join(segments) + f'</div><ul class="legend">{"".join(legend)}</ul>')


def attempt_card(a: dict) -> str:
    claims = []
    for o in a["outcomes"]:
        blocked = f' <span class="muted">({e(BLOCKED_BY.get(o["blocked_by"], o["blocked_by"]))})</span>' \
            if o["blocked_by"] else ""
        source = f'<span class="source">{e(o["source"])}</span>' if o["source"] else ""
        notes = f'<p class="notes">{e(o["notes"])}</p>' if o["notes"] else ""
        deviations = ""
        if o["deviations"]:
            items = "".join(f"<li>{e(d)}</li>" for d in o["deviations"])
            deviations = (f'<details class="deviations"><summary>{len(o["deviations"])} '
                          f'difference{"s" if len(o["deviations"]) != 1 else ""} from the paper\'s method'
                          f'</summary><ul>{items}</ul></details>')
        claims.append(f'<li><div class="claim-head">{chip(o["outcome"])}{blocked}{source}</div>'
                      f'<p class="statement">{e(o["statement"])}</p>{notes}{deviations}</li>')
    findings = "".join(
        f'<li><span class="kind">{e(FINDING_KINDS.get(f["kind"], f["kind"]))}</span> {e(f["statement"])}</li>'
        for f in a["findings"])
    findings_block = (f'<h4>Found about the dandiset</h4><ul class="findings">{findings}</ul>'
                      if findings else "")
    rounds = "; ".join(f'{e(v["date"])}, {"an agent" if v["kind"] == "agent" else "a person"} agreed '
                       f'with {v["agreed"]} of {v["of"]}' for v in a["verifications"])
    verification = f'<p class="muted small">Verification rounds: {rounds}.</p>' if rounds else ""
    links = [f'<a href="https://dandiarchive.org/dandiset/{e(a["dandiset"])}">Dandiset {e(a["dandiset"])}</a>',
             f'<a href="https://doi.org/{e(a["paper"])}">Paper</a>']
    if a["entry"]:
        links.append(f'<a href="{REPO_URL}/tree/main/entries/{e(a["entry"])}">Notebooks</a>')
    links.append(f'<a href="{REPO_URL}/blob/main/attempts/{e(a["id"])}.yaml">Attempt record</a>')
    who = "An agent" if a["kind"] == "agent" else "A person"
    return f'''<article class="card" id="attempt-{e(a["id"])}">
  <header>
    <h3>{e(a["entry_title"] or a["id"])}</h3>
    <p class="muted small">Dandiset {e(a["dandiset"])} · attempted {e(a["date"])} · {who}, run by {e(a["accountable"])}</p>
    <p><span class="tier tier-{e(a["tier"])}">{e(TIERS[a["tier"]])}</span></p>
  </header>
  <ul class="claims">{"".join(claims)}</ul>
  {findings_block}
  {verification}
  <p class="links">{" · ".join(links)}</p>
</article>'''


CSS = """
:root{--surface:#fcfcfb;--panel:#ffffff;--line:#e4e3de;--text:#0b0b0b;--text2:#52514e;--muted:#898781;
--good:#0ca30c;--warning:#fab219;--critical:#d03b3b;--blocked:#898781;--link:#1d5fb8;--goodtext:#006300}
@media (prefers-color-scheme:dark){:root{--surface:#1a1a19;--panel:#232322;--line:#3a3a37;--text:#ffffff;
--text2:#c3c2b7;--muted:#898781;--link:#8ab4f0;--goodtext:#0ca30c}}
*{box-sizing:border-box}
body{margin:0;background:var(--surface);color:var(--text);font:16px/1.5 system-ui,-apple-system,"Segoe UI",sans-serif}
main,header.top{max-width:1040px;margin:0 auto;padding:0 16px}
header.top{padding-top:40px}
h1{font-size:1.9rem;line-height:1.2;margin:0 0 8px}
h2{font-size:1.25rem;margin:48px 0 12px}
h3{font-size:1.05rem;margin:0 0 4px}
h4{font-size:.9rem;margin:20px 0 6px;color:var(--text2);font-weight:600}
p{margin:0 0 10px}
a{color:var(--link)}
.lede{color:var(--text2);max-width:68ch}
.muted{color:var(--muted)}.small{font-size:.85rem}
.tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:12px;margin:24px 0}
.tile{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:14px 16px}
.tile .n{font-size:1.9rem;font-weight:650;line-height:1.1}
.tile .l{color:var(--text2);font-size:.9rem}
.bar{display:flex;gap:2px;height:14px;margin:8px 0 10px}
.seg{border-radius:4px;min-width:6px}
.seg.good,.swatch.good{background:var(--good)}.seg.warning,.swatch.warning{background:var(--warning)}
.seg.critical,.swatch.critical{background:var(--critical)}.seg.blocked,.swatch.blocked{background:var(--blocked)}
.legend{list-style:none;display:flex;flex-wrap:wrap;gap:6px 18px;padding:0;margin:0;color:var(--text2);font-size:.9rem}
.legend strong{color:var(--text)}
.swatch{display:inline-grid;place-items:center;width:18px;height:18px;border-radius:4px;margin-right:6px;
color:#fff;font-size:.7rem;vertical-align:-3px}
.swatch.warning{color:#0b0b0b}
.card{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:18px 20px;margin:0 0 16px}
.claims,.findings{list-style:none;padding:0;margin:0}
.claims li{border-top:1px solid var(--line);padding:12px 0}
.claim-head{display:flex;flex-wrap:wrap;align-items:center;gap:8px;margin-bottom:4px}
.chip{display:inline-flex;align-items:center;gap:6px;border:1px solid var(--line);border-radius:999px;
padding:1px 10px 1px 4px;font-size:.82rem;font-weight:600;white-space:nowrap}
.chip .icon{display:inline-grid;place-items:center;width:18px;height:18px;border-radius:50%;color:#fff;font-size:.7rem}
.chip.good .icon{background:var(--good)}.chip.warning .icon{background:var(--warning);color:#0b0b0b}
.chip.critical .icon{background:var(--critical)}.chip.blocked .icon{background:var(--blocked)}
.source{color:var(--muted);font-size:.82rem}
.statement{margin:0 0 4px;font-weight:500}
.notes{color:var(--text2);font-size:.9rem;margin:0}
.deviations{font-size:.85rem;color:var(--text2);margin-top:6px}
.deviations summary{cursor:pointer;color:var(--muted)}
.deviations ul{margin:6px 0 0;padding-left:20px}
.findings li{padding:6px 0;font-size:.92rem;color:var(--text2)}
.kind{display:inline-block;font-size:.75rem;font-weight:600;color:var(--text);border:1px solid var(--line);
border-radius:4px;padding:0 6px;margin-right:6px}
.tier{display:inline-block;font-size:.8rem;font-weight:600;border:1px solid var(--line);border-radius:4px;padding:1px 8px}
.links{font-size:.9rem;margin:14px 0 0}
.controls{display:flex;flex-wrap:wrap;gap:10px;margin:0 0 12px}
.controls input,.controls select{font:inherit;padding:6px 10px;border:1px solid var(--line);border-radius:6px;
background:var(--panel);color:var(--text)}
.controls input{flex:1;min-width:200px}
.table-wrap{overflow-x:auto;border:1px solid var(--line);border-radius:10px;background:var(--panel)}
table{border-collapse:collapse;width:100%;font-size:.88rem}
th,td{text-align:left;padding:8px 12px;border-bottom:1px solid var(--line);vertical-align:top}
th{color:var(--text2);font-weight:600;white-space:nowrap}
td.num{text-align:right;white-space:nowrap;font-variant-numeric:tabular-nums}
tr:last-child td{border-bottom:0}
.status{font-size:.78rem;font-weight:600;border:1px solid var(--line);border-radius:4px;padding:0 6px;white-space:nowrap}
footer{max-width:1040px;margin:48px auto 40px;padding:0 16px;color:var(--muted);font-size:.85rem}
"""

JS = """
const rows=[...document.querySelectorAll('#queue tbody tr')];
const q=document.getElementById('q'),st=document.getElementById('st'),shown=document.getElementById('shown');
function apply(){const t=q.value.trim().toLowerCase(),s=st.value;let n=0;
rows.forEach(r=>{const ok=(!t||r.dataset.text.includes(t))&&(!s||r.dataset.status===s);r.hidden=!ok;if(ok)n++;});
shown.textContent=n+' of '+rows.length+' shown';}
q.addEventListener('input',apply);st.addEventListener('change',apply);apply();
"""

STATUS_LABEL = {"attempted": "Attempted", "pilot": "In the pilot", "open": "Not yet attempted"}


def render(data: dict) -> str:
    attempts, targets = data["attempts"], data["targets"]
    n_claims = sum(data["outcome_counts"].values())
    attempted = len({a["dandiset"] for a in attempts})
    findings = sum(len(a["findings"]) for a in attempts)
    tiles = [
        (data["queue_counts"]["with_a_paper"], "dandisets on DANDI that name a paper"),
        (attempted, "dandisets attempted"),
        (n_claims, "claims attempted"),
        (findings, "findings about the data"),
    ]
    tile_html = "".join(f'<div class="tile"><div class="n">{n}</div><div class="l">{e(label)}</div></div>'
                        for n, label in tiles)
    cards = "".join(attempt_card(a) for a in sorted(attempts, key=lambda a: a["date"], reverse=True)) \
        or '<p class="muted">No attempts yet.</p>'
    order = {"attempted": 0, "pilot": 1, "open": 2}
    body_rows = []
    for t in sorted(targets, key=lambda t: (order[t["status"]], t["dandiset"])):
        text = e(f'{t["dandiset"]} {t["name"]} {t["paper_title"]} {t["approach"]}'.lower())
        more = f' <span class="muted">+{t["n_papers"] - 1}</span>' if t["n_papers"] > 1 else ""
        body_rows.append(
            f'<tr data-status="{t["status"]}" data-text="{text}">'
            f'<td><a href="https://dandiarchive.org/dandiset/{e(t["dandiset"])}">{e(t["dandiset"])}</a></td>'
            f'<td><a href="https://doi.org/{e(t["paper"])}">{e(t["paper_title"])}</a>{more}</td>'
            f'<td>{e(t["approach"])}</td><td class="num">{t["size_gb"]:,.1f} GB</td>'
            f'<td class="num">{t["files"]:,}</td>'
            f'<td><span class="status">{STATUS_LABEL[t["status"]]}</span></td></tr>')
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Reproduction registry</title>
<meta name="description" content="Which findings of papers can be reproduced from the open data on the DANDI Archive.">
<style>{CSS}</style></head><body>
<header class="top">
  <h1>Reproduction registry</h1>
  <p class="lede">Agents and people try to reproduce the key findings of papers from the open data on the
  <a href="https://dandiarchive.org">DANDI Archive</a>. Each finding gets an outcome, whether or not it worked,
  and each attempt records what it found about the data. The notebooks are a starting point for new analyses.</p>
  <p class="muted small">Pilot stage. <a href="{REPO_URL}">Repository</a> ·
  <a href="{REPO_URL}/blob/main/docs/design.md">How it works</a> · <a href="registry.json">Data (JSON)</a></p>
</header>
<main>
  <div class="tiles">{tile_html}</div>
  <section aria-labelledby="h-outcomes">
    <h2 id="h-outcomes">Outcomes of the claims attempted</h2>
    {outcome_bar(data["outcome_counts"])}
  </section>
  <section aria-labelledby="h-attempts">
    <h2 id="h-attempts">Attempts</h2>
    {cards}
  </section>
  <section aria-labelledby="h-queue">
    <h2 id="h-queue">The queue</h2>
    <p class="lede">Public dandisets whose metadata names a paper, from the DANDI API on
    {e(data["queue_generated"][:10])}. Of {data["queue_counts"]["public_dandisets"]} public dandisets,
    {data["queue_counts"]["with_a_paper"]} name one.</p>
    <div class="controls">
      <input id="q" type="search" placeholder="Search dandiset, paper or technique" aria-label="Search the queue">
      <select id="st" aria-label="Filter by status"><option value="">All statuses</option>
        <option value="attempted">Attempted</option><option value="pilot">In the pilot</option>
        <option value="open">Not yet attempted</option></select>
      <span id="shown" class="muted small" style="align-self:center"></span>
    </div>
    <div class="table-wrap"><table id="queue">
      <thead><tr><th>Dandiset</th><th>Paper</th><th>Technique</th><th>Size</th><th>Files</th><th>Status</th></tr></thead>
      <tbody>{"".join(body_rows)}</tbody></table></div>
  </section>
</main>
<footer>Generated {e(data["generated"][:10])} from the registry's files. Outcomes describe what could be
reproduced from the data in the dandiset, with the methods available; they are not judgements of the papers.</footer>
<script>{JS}</script>
</body></html>
'''


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--output", type=Path, default=ROOT / "site")
    args = parser.parse_args()
    data = collect()
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / "index.html").write_text(render(data))
    (args.output / "registry.json").write_text(json.dumps(data, indent=1) + "\n")
    print(f"wrote {args.output / 'index.html'} ({len(data['attempts'])} attempts, "
          f"{len(data['targets'])} targets)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
