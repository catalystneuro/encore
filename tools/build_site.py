"""Build the public dashboard: one static page from the registry's own files.

    python tools/build_site.py [--output site]

Reads targets/dandisets.json, targets/pilot.yaml, claims/, attempts/ and
entries/, and writes <output>/index.html (self-contained, no external
resources) and <output>/registry.json (the same data, for other sites).

If <output>/notebooks/<entry>/<notebook>.html exists (the executed notebooks
CI keeps on the `executed` branch), the page links to it.

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
            "executed": [f'notebooks/{a["entry"]}/{Path(n["path"]).stem}.html'
                         for n in (entry["notebooks"] if entry else [])
                         if executed and (executed / a["entry"] / f'{Path(n["path"]).stem}.html').is_file()],
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


def bar(counts: dict, label: str, css: str = "bar") -> str:
    """A single stacked bar of outcomes. Segments are separated by a small gap."""
    total = sum(counts.values())
    segments = "".join(
        f'<div class="seg {OUTCOMES[k][1]}" style="flex:{n}" title="{OUTCOMES[k][0]}: {n} of {total}"></div>'
        for k, n in counts.items() if n)
    return f'<div class="{css}" role="img" aria-label="{e(label)}">{segments}</div>'


def legend(counts: dict, compact: bool = False) -> str:
    items = []
    for key, (label, css, icon) in OUTCOMES.items():
        n = counts[key]
        if compact and not n:
            continue
        text = label.lower() if compact else label
        items.append(f'<li><span class="swatch {css}" aria-hidden="true">{icon}</span>'
                     f'<strong>{n}</strong> {text}</li>')
    return f'<ul class="legend{" compact" if compact else ""}">{"".join(items)}</ul>'


def claim_item(o: dict) -> str:
    blocked = f'<span class="why">{e(BLOCKED_BY.get(o["blocked_by"], o["blocked_by"]))}</span>' \
        if o["blocked_by"] else ""
    source = f'<span class="source">{e(o["source"])}</span>' if o["source"] else ""
    notes = f'<p class="notes">{e(o["notes"])}</p>' if o["notes"] else ""
    deviations = ""
    if o["deviations"]:
        items = "".join(f"<li>{e(d)}</li>" for d in o["deviations"])
        deviations = (f'<details class="deviations"><summary>{len(o["deviations"])} '
                      f'difference{"s" if len(o["deviations"]) != 1 else ""} from the paper\'s method'
                      f'</summary><ul>{items}</ul></details>')
    caveat = ('<p class="caveat">This may reflect a limit of the attempt, not of the paper. '
              'Check the reasoning and the differences in method.</p>'
              if o["outcome"] in ("not_reproduced", "partially_reproduced") else "")
    return (f'<li class="claim" data-outcome="{o["outcome"]}">'
            f'<div class="claim-head">{chip(o["outcome"])}{source}{blocked}</div>'
            f'<p class="statement">{e(o["statement"])}</p>{notes}{caveat}{deviations}</li>')


def attempt_card(a: dict) -> str:
    counts = {k: sum(1 for o in a["outcomes"] if o["outcome"] == k) for k in OUTCOMES}
    tested = [o for o in a["outcomes"] if o["outcome"] != "blocked"]
    blocked = [o for o in a["outcomes"] if o["outcome"] == "blocked"]
    order = {"not_reproduced": 0, "partially_reproduced": 1, "reproduced": 2}
    tested.sort(key=lambda o: order[o["outcome"]])

    sections = []
    if tested:
        sections.append(f'<h4>Claims tested <span class="count">{len(tested)}</span></h4>'
                        f'<ul class="claims">{"".join(claim_item(o) for o in tested)}</ul>')
    if blocked:
        reasons = {}
        for o in blocked:
            reasons[o["blocked_by"]] = reasons.get(o["blocked_by"], 0) + 1
        why = ", ".join(f"{n} {BLOCKED_BY.get(k, k)}" for k, n in reasons.items())
        sections.append(
            f'<details class="group"><summary><h4>Claims that could not be tested '
            f'<span class="count">{len(blocked)}</span></h4><span class="muted small">{e(why)}</span></summary>'
            f'<ul class="claims">{"".join(claim_item(o) for o in blocked)}</ul></details>')
    if a["findings"]:
        items = "".join(
            f'<li><span class="kind">{e(FINDING_KINDS.get(f["kind"], f["kind"]))}</span>'
            f'<span>{e(f["statement"])}</span></li>' for f in a["findings"])
        sections.append(
            f'<details class="group"><summary><h4>Found about the dandiset '
            f'<span class="count">{len(a["findings"])}</span></h4>'
            f'<span class="muted small">for the data owner and the archive</span></summary>'
            f'<ul class="findings">{items}</ul></details>')

    if a["verifications"]:
        rounds = "; ".join(f'{e(v["date"])}, agreed with {v["agreed"]} of {v["of"]} outcomes'
                           for v in a["verifications"])
        verification = (f'<p class="muted small">Checked by {"an independent agent" if a["verifications"][-1]["kind"] == "agent" else "a person"} '
                        f'in {len(a["verifications"])} round{"s" if len(a["verifications"]) != 1 else ""}: {rounds}.</p>')
    else:
        verification = '<p class="muted small">Not yet checked by an independent verifier.</p>'

    actions = [f'<a class="button" href="{e(p)}">Open the executed notebook</a>' for p in a["executed"][:1]]
    actions += [f'<a href="https://doi.org/{e(a["paper"])}">Paper</a>',
                f'<a href="https://dandiarchive.org/dandiset/{e(a["dandiset"])}">Dandiset {e(a["dandiset"])}</a>']
    if a["entry"]:
        actions.append(f'<a href="{REPO_URL}/tree/main/entries/{e(a["entry"])}">Code</a>')
    actions.append(f'<a href="{REPO_URL}/blob/main/attempts/{e(a["id"])}.yaml">Attempt record</a>')

    verified = a["tier"] != "runs"
    tier = (f'<span class="tier {"ok" if verified else "pending"}">'
            f'{"✓ " if verified else ""}{e(TIERS[a["tier"]] if verified else "Not yet verified")}</span>')
    who = "an agent" if a["kind"] == "agent" else "a person"
    n = len(a["outcomes"])
    return f'''<details class="card" id="attempt-{e(a["id"])}">
  <summary>
    <div class="card-title">
      <h3>{e(a["entry_title"] or a["id"])}</h3>
      {tier}
    </div>
    <p class="muted small">Dandiset {e(a["dandiset"])} · {n} claim{"s" if n != 1 else ""} · attempted {e(a["date"])} by {who}</p>
    <div class="card-outcomes">{bar(counts, f"Outcomes of {n} claims", "bar mini")}{legend(counts, compact=True)}</div>
  </summary>
  <div class="card-body">
    <p class="actions">{" ".join(actions)}</p>
    {"".join(sections)}
    {verification}
  </div>
</details>'''


CSS = """
:root{--surface:#fcfcfb;--panel:#ffffff;--line:#e4e3de;--text:#0b0b0b;--text2:#52514e;--muted:#898781;
--good:#0ca30c;--warning:#fab219;--critical:#d03b3b;--blocked:#898781;--link:#1d5fb8;--accent:#1d5fb8;--hover:#f4f3ef}
@media (prefers-color-scheme:dark){:root{--surface:#1a1a19;--panel:#232322;--line:#3a3a37;--text:#ffffff;
--text2:#c3c2b7;--muted:#898781;--link:#8ab4f0;--accent:#8ab4f0;--hover:#2b2b29}}
*{box-sizing:border-box}
html{scroll-behavior:smooth;scroll-padding-top:64px}
body{margin:0;background:var(--surface);color:var(--text);font:16px/1.5 system-ui,-apple-system,"Segoe UI",sans-serif}
a{color:var(--link)}
.wrap{max-width:1040px;margin:0 auto;padding:0 16px}
nav.top{position:sticky;top:0;z-index:5;background:var(--surface);border-bottom:1px solid var(--line)}
nav.top .wrap{display:flex;align-items:center;gap:20px;height:52px}
nav.top .brand{font-weight:650;color:var(--text);text-decoration:none;margin-right:auto;white-space:nowrap}
nav.top a.link{color:var(--text2);text-decoration:none;font-size:.92rem;white-space:nowrap}
nav.top a.link:hover{color:var(--text)}
@media (max-width:560px){nav.top a.link.optional{display:none}}
header.hero{padding:36px 0 8px}
h1{font-size:2rem;line-height:1.15;margin:0 0 10px;letter-spacing:-.01em}
h2{font-size:1.3rem;margin:0 0 6px}
h3{font-size:1.05rem;margin:0;line-height:1.35}
h4{font-size:.92rem;margin:0;font-weight:650;display:inline}
p{margin:0 0 10px}
section{margin-top:48px}
.lede{color:var(--text2);max-width:66ch;font-size:1.05rem}
.sub{color:var(--text2);max-width:70ch;margin-bottom:16px}
.muted{color:var(--muted)}.small{font-size:.85rem}
.count{display:inline-block;min-width:1.5em;padding:0 6px;margin-left:4px;border-radius:999px;background:var(--hover);
color:var(--text2);font-size:.78rem;font-weight:600;text-align:center}
.tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:12px;margin:22px 0 0}
.tile{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:14px 16px}
.tile .n{font-size:1.9rem;font-weight:650;line-height:1.1;font-variant-numeric:tabular-nums}
.tile .l{color:var(--text2);font-size:.88rem}
.overview{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:18px 20px}
.bar{display:flex;gap:2px;height:14px;margin:10px 0}
.bar.mini{height:8px;width:160px;flex:none;margin:0}
.seg{border-radius:4px;min-width:5px}
.seg.good,.swatch.good{background:var(--good)}.seg.warning,.swatch.warning{background:var(--warning)}
.seg.critical,.swatch.critical{background:var(--critical)}.seg.blocked,.swatch.blocked{background:var(--blocked)}
.legend{list-style:none;display:flex;flex-wrap:wrap;gap:6px 18px;padding:0;margin:0;color:var(--text2);font-size:.9rem}
.legend strong{color:var(--text);font-variant-numeric:tabular-nums}
.legend.compact{gap:4px 14px;font-size:.84rem}
.swatch{display:inline-grid;place-items:center;width:18px;height:18px;border-radius:4px;margin-right:6px;
color:#fff;font-size:.7rem;vertical-align:-3px}
.legend.compact .swatch{width:14px;height:14px;font-size:.58rem;margin-right:5px;vertical-align:-2px}
.swatch.warning{color:#0b0b0b}
.caution{margin:16px 0 0;padding:0;border-top:1px solid var(--line);font-size:.92rem;color:var(--text2)}
.caution summary{cursor:pointer;padding:12px 0 0;list-style:none;display:flex;gap:10px;align-items:baseline}
.caution summary::-webkit-details-marker{display:none}
.caution summary::before{content:"!";flex:none;display:inline-grid;place-items:center;width:18px;height:18px;border-radius:50%;
background:var(--warning);color:#0b0b0b;font-size:.72rem;font-weight:700}
.caution summary strong{color:var(--text)}
.caution .more{color:var(--link);white-space:nowrap}
.caution[open] .more{display:none}
.caution .body{padding:8px 0 0 28px;max-width:74ch}
.toolbar{display:flex;flex-wrap:wrap;align-items:center;gap:10px;margin:0 0 12px}
.toolbar .spacer{flex:1}
button.ghost{font:inherit;font-size:.85rem;color:var(--text2);background:none;border:1px solid var(--line);border-radius:6px;
padding:4px 10px;cursor:pointer}
button.ghost:hover{background:var(--hover);color:var(--text)}
.card{background:var(--panel);border:1px solid var(--line);border-radius:10px;margin:0 0 12px;overflow:hidden}
.card>summary{list-style:none;cursor:pointer;padding:16px 20px 16px 44px;position:relative}
.card>summary::-webkit-details-marker{display:none}
.card>summary::before{content:"";position:absolute;left:20px;top:22px;width:8px;height:8px;border-right:2px solid var(--muted);
border-bottom:2px solid var(--muted);transform:rotate(-45deg);transition:transform .15s}
.card[open]>summary::before{transform:rotate(45deg)}
.card>summary:hover{background:var(--hover)}
.card>summary:focus-visible,.group>summary:focus-visible,.caution summary:focus-visible{outline:2px solid var(--accent);outline-offset:-2px}
.card-title{display:flex;flex-wrap:wrap;align-items:baseline;gap:6px 12px;margin-bottom:2px}
.card-title h3{flex:1 1 320px}
.card-outcomes{display:flex;flex-wrap:wrap;align-items:center;gap:8px 14px;margin-top:8px}
.card-body{padding:4px 20px 18px 44px;border-top:1px solid var(--line)}
@media (max-width:560px){.card>summary{padding-left:38px;padding-right:14px}.card>summary::before{left:15px}
.card-body{padding-left:14px;padding-right:14px}}
.tier{font-size:.78rem;font-weight:600;border-radius:999px;padding:1px 10px;white-space:nowrap;border:1px solid var(--line)}
.tier.ok{color:var(--text)}.tier.pending{color:var(--text2);border-style:dashed}
.actions{display:flex;flex-wrap:wrap;align-items:center;gap:8px 16px;margin:14px 0 6px;font-size:.9rem}
a.button{display:inline-block;background:var(--accent);color:var(--surface);text-decoration:none;font-weight:600;
border-radius:6px;padding:6px 12px}
a.button:hover{filter:brightness(1.1)}
.card-body>h4,.group>summary{display:block;margin:20px 0 4px}
.group>summary{cursor:pointer;list-style:none;padding:6px 0;display:flex;flex-wrap:wrap;align-items:baseline;gap:4px 10px}
.group>summary::-webkit-details-marker{display:none}
.group>summary::before{content:"+";color:var(--muted);font-weight:600;width:10px}
.group[open]>summary::before{content:"−"}
.claims,.findings{list-style:none;padding:0;margin:0}
.claim{border-top:1px solid var(--line);padding:12px 0}
.claims .claim:first-child{border-top:0}
.claim-head{display:flex;flex-wrap:wrap;align-items:center;gap:6px 10px;margin-bottom:4px}
.chip{display:inline-flex;align-items:center;gap:6px;border:1px solid var(--line);border-radius:999px;
padding:1px 10px 1px 4px;font-size:.8rem;font-weight:600;white-space:nowrap}
.chip .icon{display:inline-grid;place-items:center;width:18px;height:18px;border-radius:50%;color:#fff;font-size:.7rem}
.chip.good .icon{background:var(--good)}.chip.warning .icon{background:var(--warning);color:#0b0b0b}
.chip.critical .icon{background:var(--critical)}.chip.blocked .icon{background:var(--blocked)}
.source,.why{color:var(--muted);font-size:.82rem}
.why::before{content:"· "}
.statement{margin:0 0 4px;font-weight:500;max-width:80ch}
.notes{color:var(--text2);font-size:.9rem;margin:0;max-width:80ch}
.caveat{font-size:.82rem;color:var(--muted);margin:4px 0 0}
.deviations{font-size:.85rem;color:var(--text2);margin-top:6px}
.deviations summary{cursor:pointer;color:var(--muted)}
.deviations ul{margin:6px 0 0;padding-left:20px;max-width:78ch}
.findings li{display:grid;grid-template-columns:170px 1fr;gap:4px 12px;padding:8px 0;border-top:1px solid var(--line);
font-size:.9rem;color:var(--text2)}
.findings li:first-child{border-top:0}
@media (max-width:640px){.findings li{grid-template-columns:1fr}}
.kind{font-size:.76rem;font-weight:600;color:var(--text);align-self:start;justify-self:start;border:1px solid var(--line);
border-radius:4px;padding:1px 6px}
.controls{display:flex;flex-wrap:wrap;gap:10px;margin:0 0 12px;align-items:center}
.controls input,.controls select{font:inherit;padding:7px 10px;border:1px solid var(--line);border-radius:6px;
background:var(--panel);color:var(--text)}
.controls input{flex:1;min-width:200px}
.table-wrap{overflow-x:auto;border:1px solid var(--line);border-radius:10px;background:var(--panel)}
table{border-collapse:collapse;width:100%;font-size:.88rem}
th,td{text-align:left;padding:8px 12px;border-bottom:1px solid var(--line);vertical-align:top}
th{color:var(--text2);font-weight:600;white-space:nowrap;position:sticky;top:0;background:var(--panel)}
th button{font:inherit;font-weight:600;color:inherit;background:none;border:0;padding:0;cursor:pointer}
th button:hover{color:var(--text)}
th[aria-sort="ascending"] button::after{content:" ↑"}th[aria-sort="descending"] button::after{content:" ↓"}
td.num,th.num{text-align:right;white-space:nowrap;font-variant-numeric:tabular-nums}
tbody tr:hover{background:var(--hover)}
tr:last-child td{border-bottom:0}
.status{font-size:.78rem;font-weight:600;border:1px solid var(--line);border-radius:4px;padding:0 6px;white-space:nowrap;
color:var(--text2);text-decoration:none}
a.status{color:var(--link)}
.empty{padding:20px;text-align:center;color:var(--muted)}
footer{margin:56px 0 40px;color:var(--muted);font-size:.85rem;border-top:1px solid var(--line);padding-top:16px}
"""

JS = """
const cards=[...document.querySelectorAll('details.card')];
function openFromHash(){const el=location.hash&&document.getElementById(location.hash.slice(1));
if(el&&el.tagName==='DETAILS'){el.open=true;el.scrollIntoView();}}
addEventListener('hashchange',openFromHash);openFromHash();
const toggle=document.getElementById('toggle-all');
if(toggle)toggle.addEventListener('click',()=>{const open=cards.some(c=>!c.open);cards.forEach(c=>c.open=open);
toggle.textContent=open?'Collapse all':'Expand all';});
const tbody=document.querySelector('#queue tbody'),rows=[...tbody.rows];
const q=document.getElementById('q'),st=document.getElementById('st'),shown=document.getElementById('shown'),
empty=document.getElementById('empty');
function apply(){const t=q.value.trim().toLowerCase(),s=st.value;let n=0;
rows.forEach(r=>{const ok=(!t||r.dataset.text.includes(t))&&(!s||r.dataset.status===s);r.hidden=!ok;if(ok)n++;});
shown.textContent=n+' of '+rows.length;empty.hidden=n>0;}
q.addEventListener('input',apply);st.addEventListener('change',apply);apply();
document.querySelectorAll('#queue th[data-key]').forEach(th=>th.querySelector('button').addEventListener('click',()=>{
const dir=th.getAttribute('aria-sort')==='ascending'?-1:1,key=th.dataset.key,num=th.classList.contains('num');
document.querySelectorAll('#queue th').forEach(h=>h.removeAttribute('aria-sort'));
th.setAttribute('aria-sort',dir===1?'ascending':'descending');
rows.sort((a,b)=>{const x=a.dataset[key],y=b.dataset[key];return dir*(num?x-y:x.localeCompare(y));});
rows.forEach(r=>tbody.appendChild(r));}));
"""

STATUS_LABEL = {"attempted": "Attempted", "pilot": "In the pilot", "open": "Not yet attempted"}


def render(data: dict) -> str:
    attempts, targets = data["attempts"], data["targets"]
    n_claims = sum(data["outcome_counts"].values())
    attempted = len({a["dandiset"] for a in attempts})
    findings = sum(len(a["findings"]) for a in attempts)
    in_queue = data["queue_counts"]["with_a_paper"]
    tiles = [
        (f"{attempted} <span class='of'>of {in_queue}</span>", "dandisets attempted"),
        (n_claims, "claims attempted"),
        (sum(1 for a in attempts if a["tier"] != "runs"), "attempts independently verified"),
        (findings, "findings about the data"),
    ]
    tile_html = "".join(f'<div class="tile"><div class="n">{n}</div><div class="l">{e(label)}</div></div>'
                        for n, label in tiles)
    ordered = sorted(attempts, key=lambda a: (a["date"], a["dandiset"]), reverse=True)
    cards = "".join(attempt_card(a) for a in ordered) or '<p class="muted">No attempts yet.</p>'
    by_dandiset = {a["dandiset"]: a["id"] for a in ordered}
    order = {"attempted": 0, "pilot": 1, "open": 2}
    body_rows = []
    for t in sorted(targets, key=lambda t: (order[t["status"]], t["dandiset"])):
        text = e(f'{t["dandiset"]} {t["name"]} {t["paper_title"]} {t["approach"]}'.lower())
        more = f' <span class="muted">+{t["n_papers"] - 1}</span>' if t["n_papers"] > 1 else ""
        status = (f'<a class="status" href="#attempt-{e(by_dandiset[t["dandiset"]])}">Attempted →</a>'
                  if t["dandiset"] in by_dandiset else f'<span class="status">{STATUS_LABEL[t["status"]]}</span>')
        body_rows.append(
            f'<tr data-status="{t["status"]}" data-text="{text}" data-dandiset="{e(t["dandiset"])}" '
            f'data-paper="{e((t["paper_title"] or "").lower())}" data-size="{t["size_gb"]}" data-files="{t["files"]}">'
            f'<td><a href="https://dandiarchive.org/dandiset/{e(t["dandiset"])}">{e(t["dandiset"])}</a></td>'
            f'<td><a href="https://doi.org/{e(t["paper"])}">{e(t["paper_title"])}</a>{more}</td>'
            f'<td>{e(t["approach"])}</td><td class="num">{t["size_gb"]:,.1f} GB</td>'
            f'<td class="num">{t["files"]:,}</td><td>{status}</td></tr>')
    overview = (bar(data["outcome_counts"], f"Outcomes of {n_claims} claims attempted") + legend(data["outcome_counts"])
                if n_claims else '<p class="muted">No claims attempted yet.</p>')
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Reproduction registry</title>
<meta name="description" content="Which findings of papers can be reproduced from the open data on the DANDI Archive.">
<style>{CSS}.tile .of{{font-size:1rem;font-weight:500;color:var(--muted)}}</style></head><body>
<nav class="top" aria-label="Sections"><div class="wrap">
  <a class="brand" href="#top">Reproduction registry</a>
  <a class="link" href="#attempts">Attempts</a>
  <a class="link" href="#queue-section">Queue</a>
  <a class="link optional" href="{REPO_URL}/blob/main/docs/design.md">How it works</a>
  <a class="link optional" href="{REPO_URL}">GitHub</a>
</div></nav>
<div class="wrap" id="top">
<header class="hero">
  <h1>Can the findings of a paper be reproduced from its open data?</h1>
  <p class="lede">Agents and people take papers whose data is on the <a href="https://dandiarchive.org">DANDI Archive</a>
  and try to reproduce their key findings from that data alone. Every finding gets an outcome, whether or not it
  worked, and every attempt records what it learned about the data. The notebooks are a starting point for new analyses.</p>
  <div class="tiles">{tile_html}</div>
</header>
<main>
  <section aria-labelledby="h-outcomes" style="margin-top:28px">
    <div class="overview">
      <h2 id="h-outcomes">Outcomes of the {n_claims} claims attempted</h2>
      {overview}
      <details class="caution">
        <summary><span><strong>A failure to reproduce is not a finding that the paper is wrong.</strong>
        It may be a failure of the attempt. <span class="more">Read more</span></span></summary>
        <div class="body">
          <p>An outcome says what one attempt could recover from the data in a dandiset, with the methods available
          to it. A “not reproduced” or “partially reproduced” outcome can come from a mistake or a limitation in the
          agent’s analysis, from methods the paper does not describe fully, from data that is not in the dandiset, or
          from a dandiset that differs from what the paper analysed. “Blocked” means the claim could not be tested at all.</p>
          <p>Most attempts are made by AI agents. Where a card says so, the attempt has been checked by a second,
          independent agent, but neither is infallible. Every attempt links to its code, its reasoning and the ways
          its analysis differs from the paper’s. Authors who think an attempt is wrong can
          <a href="{REPO_URL}/issues">open an issue</a>.</p>
        </div>
      </details>
    </div>
  </section>
  <section aria-labelledby="attempts">
    <div class="toolbar"><h2 id="attempts">Attempts</h2><span class="spacer"></span>
      <button class="ghost" id="toggle-all" type="button">Expand all</button></div>
    <p class="sub">One card per dandiset attempted. Open a card for each claim’s outcome and reasoning, what was found
    about the data, and the executed notebook.</p>
    {cards}
  </section>
  <section aria-labelledby="queue-section">
    <h2 id="queue-section">The queue</h2>
    <p class="sub">Of {data["queue_counts"]["public_dandisets"]} public dandisets on DANDI, {in_queue} name a paper in
    their metadata (as of {e(data["queue_generated"][:10])}). These are the targets.</p>
    <div class="controls">
      <input id="q" type="search" placeholder="Search by dandiset, paper or technique" aria-label="Search the queue">
      <select id="st" aria-label="Filter by status"><option value="">All statuses</option>
        <option value="attempted">Attempted</option><option value="pilot">In the pilot</option>
        <option value="open">Not yet attempted</option></select>
      <span id="shown" class="muted small" aria-live="polite"></span>
    </div>
    <div class="table-wrap"><table id="queue">
      <thead><tr><th data-key="dandiset"><button type="button">Dandiset</button></th>
      <th data-key="paper"><button type="button">Paper</button></th><th>Technique</th>
      <th class="num" data-key="size"><button type="button">Size</button></th>
      <th class="num" data-key="files"><button type="button">Files</button></th><th>Status</th></tr></thead>
      <tbody>{"".join(body_rows)}</tbody></table>
      <p class="empty" id="empty" hidden>No targets match.</p></div>
  </section>
</main>
<footer>Generated {e(data["generated"][:10])} from the registry's files · <a href="registry.json">Data as JSON</a> ·
<a href="{REPO_URL}">Repository</a>. Outcomes describe what one attempt could reproduce from the data in the dandiset,
with the methods available. A failure to reproduce may be a failure of the agent, and is not a judgement of the paper.</footer>
</div>
<script>{JS}</script>
</body></html>
'''


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--output", type=Path, default=ROOT / "site")
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    data = collect(args.output / "notebooks")
    (args.output / "index.html").write_text(render(data))
    (args.output / "registry.json").write_text(json.dumps(data, indent=1) + "\n")
    print(f"wrote {args.output / 'index.html'} ({len(data['attempts'])} attempts, "
          f"{len(data['targets'])} targets)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
