"""Exploratory: does the strength of a paper's reported evidence predict whether the finding reproduces from the
same data? Uses the p-values the claims files record from the paper (one entry per test)."""

import json
import math
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import build_site as bs  # noqa: E402

OUT = ROOT / "manuscript" / "out" / "explore"
OUT.mkdir(parents=True, exist_ok=True)
data = bs.finish(bs.collect())
live = [a for v in bs.current_attempts(data).values() for a in v if not a.get("deprecated")]


def as_float(p):
    try:
        x = float(str(p).replace("×10^", "e").replace("x10^", "e"))
        return x if 0 < x <= 1 else None
    except (TypeError, ValueError):
        return None


rows, all_p = [], []
for a in live:
    for o in a["outcomes"]:
        if o.get("kind") == "link" or o.get("data") not in (None, "dataset", "with_labels") or not o["statistics"]:
            continue
        sig, null = [], []
        for s in o["statistics"]:
            p, rel = as_float(s.get("p")), (s.get("p_relation") or "=").strip()
            if p is None:
                continue
            all_p.append((p, rel))
            (null if rel in (">", ">=", "≥") or (rel == "=" and p >= 0.05) else sig).append(p)
        if not sig and not null:
            continue
        kind = "significant" if sig else "null"
        p = min(sig) if sig else min(null)
        rows.append({"dataset": a["label"], "claim": o["claim"], "outcome": o["outcome"], "kind": kind, "p": p,
                     "bound": any((s.get("p_relation") or "").strip() in ("<", "<=", "≤") for s in o["statistics"]),
                     "corrected": any(s.get("corrected") for s in o["statistics"]),
                     "tested": o["outcome"] != "blocked",
                     "reproduced": {"reproduced": 1.0, "partially_reproduced": 0.0, "not_reproduced": 0.0}.get(o["outcome"]),
                     "strict": {"reproduced": 1.0, "partially_reproduced": 1.0, "not_reproduced": 0.0}.get(o["outcome"])})
df = pd.DataFrame(rows)
sig = df[df.kind == "significant"].copy()
sig["log10p"] = np.log10(sig.p.clip(lower=1e-8))  # a few p near 1e-300 would otherwise set the scale
bins = [0, 1e-3, 1e-2, 0.05 + 1e-12]
labels = ["p < 0.001", "0.001 to 0.01", "0.01 to 0.05"]
sig["band"] = pd.cut(sig.p, bins, labels=labels, right=True)
t = sig[sig.tested]
report = {"claims_with_p": len(df), "significant": len(sig), "null": int((df.kind == "null").sum()),
          "datasets": df.dataset.nunique()}

band = sig.groupby("band", observed=False).agg(claims=("tested", "size"), tested=("tested", "mean"))
band["tested_n"] = t.groupby("band", observed=False).size()
band["reproduced"] = t.groupby("band", observed=False)["reproduced"].mean()
band["reproduced_or_partial"] = t.groupby("band", observed=False)["strict"].mean()
nulls = df[(df.kind == "null") & df.tested]
band.loc["reported null (p > 0.05)"] = [int((df.kind == "null").sum()), (df[df.kind == "null"].tested.mean()),
                                         len(nulls), nulls.reproduced.mean(), nulls.strict.mean()]
report["by_band"] = band.round(2).to_dict(orient="index")

# Logistic regressions, standard errors clustered by dataset: log10 p predicting reproduction, among tested.
for y in ("reproduced", "strict"):
    f = t.dropna(subset=[y])
    m = smf.logit(f"{y} ~ log10p", f).fit(disp=0, cov_type="cluster", cov_kwds={"groups": pd.factorize(f.dataset)[0]})
    report[f"logit_{y}"] = {"coef_per_log10p": round(m.params["log10p"], 3), "p": round(m.pvalues["log10p"], 4),
                            "n": int(m.nobs)}
    m2 = smf.logit(f"{y} ~ log10p + bound + corrected", f).fit(disp=0, cov_type="cluster",
                                                                cov_kwds={"groups": pd.factorize(f.dataset)[0]})
    report[f"logit_{y}_adjusted"] = {k: {"coef": round(m2.params[k], 3), "p": round(m2.pvalues[k], 4)}
                                     for k in m2.params.index}

# The reported p-values themselves: exact values near the threshold (a p-curve), against bounds like p < 0.05.
exact = np.array([p for p, rel in all_p if rel in ("=", "") and p < 0.1])
report["exact_p_counts"] = {f"{lo}-{hi}": int(((exact > lo) & (exact <= hi)).sum())
                            for lo, hi in [(0, .01), (.01, .02), (.02, .03), (.03, .04), (.04, .05), (.05, .1)]}

fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))
x = np.arange(len(band))
axes[0].bar(x - 0.2, band["reproduced"], 0.4, color="#0ca30c", label="reproduced")
axes[0].bar(x + 0.2, band["reproduced_or_partial"], 0.4, color="#fab219", label="reproduced or partially")
for i, (n, tn) in enumerate(zip(band["claims"], band["tested_n"])):
    axes[0].text(i, 0.02, f"n={int(tn)}", ha="center", fontsize=8, color="white")
axes[0].set_xticks(x, band.index, fontsize=8); axes[0].set_ylim(0, 1); axes[0].set_ylabel("Share of tested claims")
axes[0].set_title("Reproduction by the paper's reported p-value"); axes[0].legend(fontsize=8)
binsp = np.linspace(0, 0.1, 21)
axes[1].hist(exact, bins=binsp, color="#6a3d8f")
axes[1].axvline(0.05, color="#d03b3b", lw=1, ls="--")
axes[1].set_xlabel("Exact p-values reported (p < 0.1)"); axes[1].set_ylabel("Tests"); axes[1].set_title("Reported p-values")
plt.tight_layout(); plt.savefig(OUT / "pvalues.png", dpi=160)
sig.to_csv(OUT / "claims_with_p.csv", index=False)
(OUT / "pvalues.json").write_text(json.dumps(report, indent=1, default=str))
print(json.dumps(report, indent=1, default=str))
