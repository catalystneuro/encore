"""Exploratory: what predicts whether a claim can be tested, and whether it reproduces? First pass, not final."""

import collections
import json
import re
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from sklearn.cluster import KMeans
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import build_site as bs  # noqa: E402

OUT = ROOT / "manuscript" / "out" / "explore"
OUT.mkdir(parents=True, exist_ok=True)
data = bs.finish(bs.collect())
live = [a for v in bs.current_attempts(data).values() for a in v if not a.get("deprecated")]
targets = {t["key"]: t for t in data["targets"]}


def section(src: str) -> str:
    s = (src or "").lower()
    if re.search(r"\b(extended data|supplementary|supplemental|table s|figure s|fig\. s)", s): return "supplement"
    if s.startswith(("results", "main text")): return "results"
    if re.search(r"method|materials|data records|technical validation", s[:40]): return "methods"
    if s.startswith(("figure", "fig", "table")): return "figure/table"
    if s.startswith(("discussion", "abstract", "introduction", "summary")): return "abstract/discussion"
    return "other"


rows = []
for a in live:
    t = targets.get(a["key"], {})
    tech = set(t.get("technique") or [])
    year = re.search(r"-(\d{4})-\d\d$", a["id"])
    for o in a["outcomes"]:
        if o.get("kind") == "link" or o.get("data") not in (None, "dataset", "with_labels"):
            continue
        st = o["statement"] or ""
        rows.append({
            "dataset": a["label"], "claim": o["claim"], "outcome": o["outcome"], "blocked_by": o["blocked_by"],
            "statement": st, "notes": o["notes"] or "",
            "tested": o["outcome"] != "blocked",
            "reproduced": {"reproduced": 1.0, "partially_reproduced": 0.0, "not_reproduced": 0.0}.get(o["outcome"]),
            "section": section(o["source"]),
            "has_stats": bool(o["statistics"]),
            "n_numbers": len(re.findall(r"\d+(?:\.\d+)?", st)),
            "words": len(st.split()),
            "ephys": "electrophysiological" in tech, "imaging": "cell population imaging" in tech or "microscopy" in tech,
            "behavior": "behavioral" in tech,
            "log_size": np.log10((t.get("size_gb") or 0) + 0.01), "log_files": np.log10((t.get("files") or 0) + 1),
            "paper_year": int(year.group(1)) if year else np.nan,
        })
df = pd.DataFrame(rows)
tested = df[df.tested].copy()
report = {}

# 1. How much is the dataset, how much the claim? Between-dataset share of variance (linear probability ICC).
for name, frame, y in (("tested", df, "tested"), ("reproduced", tested, "reproduced")):
    f = frame.assign(y=frame[y].astype(float))
    m = smf.mixedlm("y ~ 1", f, groups=f["dataset"]).fit()
    icc = float(m.cov_re.iloc[0, 0] / (m.cov_re.iloc[0, 0] + m.scale))
    report[f"icc_{name}"] = round(icc, 3)

# 2. Rates by claim features.
def rates(col):
    g = df.groupby(col).agg(claims=("tested", "size"), tested=("tested", "mean"))
    g["reproduced_of_tested"] = tested.groupby(col)["reproduced"].mean()
    return g.round(2)
report["by_section"] = rates("section").to_dict(orient="index")
report["by_has_stats"] = rates("has_stats").to_dict(orient="index")
df["numbers_bin"] = pd.cut(df.n_numbers, [-1, 0, 2, 5, 100], labels=["0", "1-2", "3-5", "6+"])
tested["numbers_bin"] = df.loc[tested.index, "numbers_bin"]
report["by_numbers"] = rates("numbers_bin").to_dict(orient="index")

# 3. Regressions, standard errors clustered by dataset.
X = "C(section) + has_stats + n_numbers + ephys + imaging + behavior + log_size + log_files"
for name, frame, y in (("tested", df, "tested"), ("reproduced", tested, "reproduced")):
    f = frame.dropna(subset=["log_size"]).assign(y=frame[y].astype(float))
    m = smf.logit(f"y ~ {X}", f).fit(disp=0, cov_type="cluster", cov_kwds={"groups": pd.factorize(f["dataset"])[0]})
    report[f"logit_{name}"] = {k: {"coef": round(m.params[k], 2), "p": round(m.pvalues[k], 3)} for k in m.params.index}

# 4. Claims by wording: TF-IDF, SVD, UMAP, k-means topics.
vec = TfidfVectorizer(stop_words="english", min_df=3, max_df=0.4, ngram_range=(1, 2),
                      token_pattern=r"(?u)\b[a-zA-Z][a-zA-Z-]{2,}\b")
Xt = vec.fit_transform(df.statement)
Z = TruncatedSVD(60, random_state=0).fit_transform(Xt)
Z = Z / np.linalg.norm(Z, axis=1, keepdims=True).clip(1e-9)
k = 10
km = KMeans(k, n_init=20, random_state=0).fit(Z)
df["topic"] = km.labels_
terms = np.array(vec.get_feature_names_out())
centroids = np.asarray(Xt.T.dot(np.eye(k)[km.labels_]) / np.bincount(km.labels_)).T  # mean tf-idf per topic
topics = {}
for c in range(k):
    top = terms[np.argsort(-centroids[c])[:7]]
    sub = df[df.topic == c]
    topics[c] = {"terms": ", ".join(top), "claims": len(sub), "datasets": sub.dataset.nunique(),
                 "tested": round(sub.tested.mean(), 2),
                 "reproduced_of_tested": round(sub[sub.tested].reproduced.mean(), 2) if sub.tested.any() else None}
report["topics"] = topics
import umap  # noqa: E402
emb = umap.UMAP(n_neighbors=20, min_dist=0.15, metric="cosine", random_state=0).fit_transform(Z)
df["u1"], df["u2"] = emb[:, 0], emb[:, 1]
COL = {"reproduced": "#0ca30c", "partially_reproduced": "#fab219", "not_reproduced": "#d03b3b", "blocked": "#898781"}
fig, axes = plt.subplots(1, 2, figsize=(13, 6))
for o, c in COL.items():
    s = df[df.outcome == o]
    axes[0].scatter(s.u1, s.u2, s=5, c=c, label=o.replace("_", " "), alpha=.7)
axes[0].legend(markerscale=3, fontsize=8); axes[0].set_title("Claims by wording, coloured by outcome")
cmap = plt.get_cmap("tab10")
for c in range(k):
    s = df[df.topic == c]
    axes[1].scatter(s.u1, s.u2, s=5, color=cmap(c), alpha=.7)
    axes[1].text(s.u1.median(), s.u2.median(), str(c), fontsize=11, weight="bold")
axes[1].set_title("Topics (k-means on the same space)")
for ax in axes: ax.set_xticks([]); ax.set_yticks([])
plt.tight_layout(); plt.savefig(OUT / "umap_claims.png", dpi=160)

# 5. What is missing, when a claim is blocked by missing data: frequent terms in the agents' notes.
miss = df[df.blocked_by == "data_missing"].notes
v2 = TfidfVectorizer(stop_words="english", min_df=4, ngram_range=(1, 2), token_pattern=r"(?u)\b[a-zA-Z][a-zA-Z-]{2,}\b")
M = v2.fit_transform(miss)
freq = np.asarray((M > 0).sum(axis=0)).ravel()
report["missing_terms"] = dict(sorted(zip(v2.get_feature_names_out(), freq.tolist()), key=lambda x: -x[1])[:45])
report["n"] = {"claims": len(df), "tested": int(df.tested.sum()), "datasets": df.dataset.nunique()}
(OUT / "report.json").write_text(json.dumps(report, indent=1, default=str))
df.drop(columns=["notes"]).to_csv(OUT / "claims.csv", index=False)
print(json.dumps(report, indent=1, default=str))
