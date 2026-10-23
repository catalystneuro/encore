"""Write manuscript/analysis.ipynb, the numbers and figures for a paper on the registry.

    python manuscript/make_notebook.py && jupyter nbconvert --to notebook --execute --inplace manuscript/analysis.ipynb

The notebook reads the registry through tools/build_site.py, the loader the site uses, so that every number
matches encorescience.org at the same commit. Edit the cells here, not in the notebook.
"""

from pathlib import Path

import nbformat as nbf

cells = []
md = lambda s: cells.append(nbf.v4.new_markdown_cell(s.strip()))
code = lambda s: cells.append(nbf.v4.new_code_cell(s.strip()))

md("""
# Encore: the registry in numbers

Every number and figure a paper on the registry would cite, computed from the registry's own files at one commit.
The counts follow the site's rules (`tools/build_site.py`): an attempt that was deprecated counts for nothing, a
dataset's current attempt is its latest on each paper, and the paper's findings that rest on the dataset alone are
counted apart from those that also use data from elsewhere and from the registry's checks that the dataset is the
paper's data.

Not here yet: the human validation of a sample of outcomes and findings, run-to-run reliability, and the cost
of a run (in the Actions logs, not in the records).
""")

code("""
import collections, json, subprocess, sys
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path.cwd().parent if Path.cwd().name == "manuscript" else Path.cwd()
sys.path.insert(0, str(ROOT / "tools"))
import build_site as bs  # noqa: E402

data = bs.finish(bs.collect())
git = lambda *a: subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True).stdout.strip()
COMMIT, WHEN = git("rev-parse", "--short", "HEAD"), git("log", "-1", "--format=%cI")
OUT = ROOT / "manuscript" / "out"
OUT.mkdir(exist_ok=True)
numbers = {"commit": COMMIT, "date": WHEN}
ORDER = ["reproduced", "partially_reproduced", "not_reproduced", "blocked"]
LABEL = {k: v[0] for k, v in bs.OUTCOMES.items()}
COLOUR = {"reproduced": "#0ca30c", "partially_reproduced": "#fab219", "not_reproduced": "#d03b3b", "blocked": "#898781"}
pct = lambda a, b: f"{100 * a / b:.0f}%" if b else "n/a"
print(f"Registry at {COMMIT}, committed {WHEN}")
""")

md("## 1. The sample")
code("""
targets = data["targets"]
attempts = data["attempts"]
current = bs.current_attempts(data)
live = [a for v in current.values() for a in v if not a.get("deprecated")]
cn = {t["key"] for t in targets if t["catalystneuro"]}
attempted = {a["key"] for a in live}
sample = {
    "targets (public datasets that name a paper)": len(targets),
    "  of them converted by CatalystNeuro": len(cn),
    "datasets with a current attempt": len(attempted),
    "  of them converted by CatalystNeuro": len(attempted & cn),
    "papers attempted (dataset, paper pairs)": len(live),
    "attempt records in all": len(attempts),
    "  deprecated": sum(1 for a in attempts if a.get("deprecated")),
    "  repeat attempts (a dataset's second or later)": len(attempts) - len({(a["key"], a["paper"]) for a in attempts}),
}
numbers["sample"] = sample
pd.Series(sample, name="count").to_frame()
""")
md("""
CatalystNeuro's conversions were attempted first, so the attempted set is not a random sample of the targets:
report the two groups apart (section 3), or attempt a random sample of the rest before freezing.
""")

md("## 2. Outcomes of the claims")
code("""
GROUPS = {"dataset": "Findings on the dataset alone", "with_inputs": "Findings that also use outside data",
          "elsewhere": "Findings on data in another archive", "link": "Checks that the dataset is the paper's data"}
rows = []
for g, name in GROUPS.items():
    c = bs.outcome_counts(live, g)
    n = sum(c.values())
    if n:
        rows.append({"claims": name, "n": n, **{LABEL[k]: f"{c[k]} ({pct(c[k], n)})" for k in ORDER}})
numbers["outcomes"] = {g: bs.outcome_counts(live, g) for g in GROUPS}
pd.DataFrame(rows).set_index("claims")
""")
code("""
c = numbers["outcomes"]["dataset"]
tested = c["reproduced"] + c["partially_reproduced"] + c["not_reproduced"]
numbers["of_tested"] = {k: c[k] / tested for k in ORDER[:3]}
print(f"Of the {sum(c.values())} findings that rest on the dataset alone, {tested} could be tested "
      f"({pct(tested, sum(c.values()))}); {c['blocked']} were blocked.")
print(f"Of those tested: {pct(c['reproduced'], tested)} reproduced, {pct(c['partially_reproduced'], tested)} "
      f"partially, {pct(c['not_reproduced'], tested)} not reproduced.")
""")

md("### Why claims were blocked")
code("""
blocked = collections.Counter(o["blocked_by"] or "unstated" for a in live for o in a["outcomes"]
                              if o["outcome"] == "blocked" and o.get("kind") != "link"
                              and o.get("data") in (None, "dataset", "with_labels"))
numbers["blocked_by"] = dict(blocked)
s = pd.Series({bs.BLOCKED_BY.get(k, k): v for k, v in blocked.most_common()}, name="claims")
ax = s.iloc[::-1].plot.barh(color="#898781", figsize=(7, 0.35 * len(s) + 1))
ax.set_xlabel("Blocked findings on the dataset alone"); ax.set_ylabel("")
plt.tight_layout(); plt.savefig(OUT / "blocked_by.png", dpi=200); plt.show()
s.to_frame()
""")

md("## 3. By dataset")
code("""
per = []
for a in live:
    c = bs.outcome_counts(a, "dataset")
    n = sum(c.values())
    if n:
        per.append({"dataset": a["label"], "paper": a.get("paper_title") or a["paper"], "n": n,
                    "catalystneuro": a["key"] in cn, "tier": a["tier"], "findings_about_data": len(a["findings"]),
                    **{k: c[k] for k in ORDER}})
per = pd.DataFrame(per)
per["reproduced_of_tested"] = per["reproduced"] / (per[ORDER[:3]].sum(axis=1)).replace(0, float("nan"))
per.to_csv(OUT / "per_dataset.csv", index=False)
per[["n"] + ORDER + ["findings_about_data"]].describe().round(1)
""")
code("""
p = per.assign(share=per["reproduced"] / per["n"]).sort_values(["share", "n"])
fig, ax = plt.subplots(figsize=(7, 0.2 * len(p) + 1))
left = 0
for k in ORDER:
    frac = p[k] / p["n"]
    ax.barh(range(len(p)), frac, left=left, color=COLOUR[k], label=LABEL[k], height=0.8)
    left = left + frac
ax.set_yticks(range(len(p)), p["dataset"], fontsize=6); ax.set_xlim(0, 1)
ax.set_xlabel("Share of the paper's findings on the dataset alone")
ax.legend(loc="lower center", bbox_to_anchor=(0.5, 1.0), ncol=4, fontsize=7, frameon=False)
plt.tight_layout(); plt.savefig(OUT / "outcomes_by_dataset.png", dpi=200); plt.show()
""")
code("""
g = per.groupby("catalystneuro")[ORDER + ["n", "findings_about_data"]].sum()
g.index = g.index.map({True: "Converted by CatalystNeuro", False: "Converted by others"})
g["datasets"] = per.groupby("catalystneuro").size().values
g["reproduced, of tested"] = (g["reproduced"] / g[ORDER[:3]].sum(axis=1)).map("{:.0%}".format)
g["findings per dataset"] = (g["findings_about_data"] / g["datasets"]).round(1)
numbers["by_converter"] = g.drop(columns=["reproduced, of tested"]).to_dict(orient="index")
g
""")

md("## 4. Verification")
code("""
tiers = collections.Counter(a["tier"] for a in live)
disagreed = sum(1 for a in live for o in a["outcomes"] if o["disagreed"])
n_out = sum(len(a["outcomes"]) for a in live)
proposed = sum(1 for a in live for o in a["outcomes"] if o.get("proposed"))
numbers["verification"] = {"tiers": dict(tiers), "outcomes": n_out, "verifier_disagreed": disagreed,
                           "proposed_unverified": proposed}
print(f"Trust tiers of the current attempts: {dict(tiers)}")
print(f"An independent verifier disagreed at first with {disagreed} of {n_out} outcomes ({pct(disagreed, n_out)}); "
      f"{proposed} changes proposed after the last round are not yet verified.")
""")

md("## 5. Findings about the data")
code("""
kinds = collections.Counter(f["kind"] for a in live for f in a["findings"])
numbers["findings"] = {"total": sum(kinds.values()), "kinds": dict(kinds),
                       "datasets_with_any": int((per["findings_about_data"] > 0).sum()), "datasets": len(per)}
s = pd.Series({bs.FINDING_KINDS.get(k, k): v for k, v in kinds.most_common()}, name="findings")
ax = s.iloc[::-1].plot.barh(color="#6a3d8f", figsize=(7, 0.35 * len(s) + 1))
ax.set_xlabel("Findings about the data, over all current attempts"); ax.set_ylabel("")
plt.tight_layout(); plt.savefig(OUT / "findings_by_kind.png", dpi=200); plt.show()
print(f"{sum(kinds.values())} findings about the data; {numbers['findings']['datasets_with_any']} of "
      f"{len(per)} datasets have at least one.")
s.to_frame()
""")

md("""
## 6. Repeat attempts

A dataset is attempted again for one of three reasons: its data changed (a new version or the draft, after a
fix), its earlier attempt was deprecated and its claims re-read from the full text, or the protocol changed. Only
the first is a before and after of the data. Claims are matched by id; a claim that changed id is not compared.
""")
code("""
by_pair = collections.defaultdict(list)
for a in sorted(attempts, key=lambda a: (a["date"], a["id"])):
    by_pair[(a["key"], a["paper"])].append(a)
moves, data_moves, rows = collections.Counter(), collections.Counter(), []
for (key, paper), seq in by_pair.items():
    for before, after in zip(seq, seq[1:]):
        b = {o["claim"]: o["outcome"] for o in before["outcomes"]}
        why = ("data changed" if after["dataset_version"] != before["dataset_version"]
               else "claims re-read" if before.get("deprecated") else "protocol changed")
        n = 0
        for o in after["outcomes"]:
            if o["claim"] in b:
                moves[(b[o["claim"]], o["outcome"])] += 1; n += 1
                if why == "data changed":
                    data_moves[(b[o["claim"]], o["outcome"])] += 1
        rows.append({"dataset": after["label"], "why": why, "before": before["id"], "after": after["id"],
                     "version before": before["dataset_version"], "version after": after["dataset_version"],
                     "claims compared": n, "findings before": len(before["findings"]),
                     "findings after": len(after["findings"]), "before deprecated": bool(before.get("deprecated"))})
numbers["repeats"] = {"pairs": len(rows), "why": dict(collections.Counter(r["why"] for r in rows)),
                      "transitions_all": {f"{a}->{b}": v for (a, b), v in moves.items()},
                      "transitions_data_changed": {f"{a}->{b}": v for (a, b), v in data_moves.items()}}

def matrix(counter):
    m = pd.DataFrame(0, index=[LABEL[k] for k in ORDER], columns=[LABEL[k] for k in ORDER])
    for (a, b), v in counter.items():
        m.loc[LABEL[a], LABEL[b]] = v
    return m.rename_axis(index="before", columns="after")

display(pd.DataFrame(rows))
print("Outcomes of the same claims, where the data changed between the attempts:")
display(matrix(data_moves))
print("All repeat attempts:")
matrix(moves)
""")

md("## Numbers for the manuscript")
code("""
(OUT / "numbers.json").write_text(json.dumps(numbers, indent=1, default=str))
print(f"Wrote manuscript/out/numbers.json, per_dataset.csv and three figures, at commit {COMMIT}.")
""")

nb = nbf.v4.new_notebook(cells=cells, metadata={"kernelspec": {"name": "python3", "display_name": "Python 3",
                                                                "language": "python"}})
nbf.write(nb, Path(__file__).with_name("analysis.ipynb"))
print("wrote manuscript/analysis.ipynb")
