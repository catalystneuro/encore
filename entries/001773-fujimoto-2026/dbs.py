"""Loading and statistics for the source data of dandiset 001773.

Fujimoto, Fujimoto, Elorette et al. (2026), Nature Neuroscience, doi:10.1038/s41593-026-02301-4.

The dandiset holds no NWB files: Excel sheets of derived values (voxel FA, voxel seed
connectivity, ROI-by-ROI connectomes, cell counts, g-ratios, behavior bins) and the paper's
MATLAB scripts under `code/`. Each sheet is read from the archive into memory at the pinned
version; nothing is written to disk.

Where the parameters come from:

- The ANOVAs follow the paper's scripts in the dandiset. FA (Fig2A, Fig2B, Fig6A, Fig6B
  scripts) and seed connectivity (Fig5BCandE9, Fig6DandE10D scripts) use MATLAB `anovan` with
  the model matrix `model_mat2`: main effects of monkey, PrePost, side and tract (or subregion,
  ROI, network) and every interaction of the last three, but none with monkey. Behavior,
  CC1/DAPI and g-ratio (FigE1, Fig3CandE5, Fig3F, FigE6A, FigE6B scripts) use `anovan` with
  `"Model","full"` on monkey and condition, that is condition, monkey and their interaction.
  `anovan` uses type III sums of squares and sum-to-zero constraints by default; `anova` does
  the same, and type II is available as the variant the claims file asks for.
- The post hoc tests are MATLAB `multcompare` on the `anovan` statistics, whose default is the
  Tukey-Kramer method on the population marginal means, over the cells of the dimensions the
  scripts name (`"Dimension",[2 3 4]`, PrePost x side x tract). `tukey_kramer` computes the same:
  each mean is the model's prediction with the other factors averaged over their levels, its
  covariance comes from the model, and P is the studentized range tail for the number of means
  and the error df.
- Monkey D's CC1/DAPI test is MATLAB `ttest(x1, x2)` on the row-paired lead-side and control-side
  columns (Fig6C script).
- The network hubs are the ROI lists of the Fig5BCandE9 script: DMN 1 2 3, SAN 4 5, CEN 6 7,
  LIM 1 5 8 9 10 11 12, SMN 13 14 15, VIS 16 17 (ROI numbers of FC_ROI_label.xlsx).
- The per-ROI connectome test of the Fig4 script is `ranksum` of each ROI's off-diagonal changes
  against a vector of zeros at 0.05 / nrois; the cortical block is the first 54 ROIs (its
  `plot([54 54], ...)` and the circular plot's `1:54`).
"""

from __future__ import annotations

import io
import itertools
from functools import lru_cache

import numpy as np
import pandas as pd
import requests
from scipy import stats

DANDISET_ID = "001773"
DANDISET_VERSION = "0.260416.1939"
API = "https://api.dandiarchive.org/api"

N_CORTICAL = 54   # Fig4 script: cortical (CHARM) ROIs come first, then SARM
NETWORKS = {      # Fig5BCandE9 script
    "DMN": [1, 2, 3],
    "SAN": [4, 5],
    "CEN": [6, 7],
    "LIM": [1, 5, 8, 9, 10, 11, 12],
    "SMN": [13, 14, 15],
    "VIS": [16, 17],
}
AREA25 = 8


@lru_cache(maxsize=None)
def asset_ids() -> dict:
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/?page_size=200"
    out = {}
    while url:
        r = requests.get(url, timeout=60)
        r.raise_for_status()
        j = r.json()
        out.update({a["path"]: a["asset_id"] for a in j["results"]})
        url = j["next"]
    return out


@lru_cache(maxsize=None)
def fetch(path: str) -> bytes:
    """The bytes of one asset, read into memory."""
    r = requests.get(f"{API}/assets/{asset_ids()[path]}/download/", timeout=120)
    r.raise_for_status()
    return r.content


def sheet(path: str, sheet_name=0, header=None) -> pd.DataFrame:
    return pd.read_excel(io.BytesIO(fetch(path)), sheet_name=sheet_name, header=header)


def text(path: str) -> str:
    return fetch(path).decode("utf-8", errors="replace")


# ---------------------------------------------------------------- loaders

def behavior() -> pd.DataFrame:
    d = sheet("source_data/dbs_behavior_data_a.xlsx", header=0).iloc[:, :6].dropna()
    return d.astype({"sec": int, "movement": int, "foraging": int, "mk": int, "stim": int, "group": int})


def fa_wholetract() -> pd.DataFrame:
    d = sheet("source_data/dbs_FA_wholetract_data_a.xlsx", header=0).iloc[:, :5].dropna()
    return d.astype({"mk": int, "prepost": int, "side": int, "tract": int})


def fa_subpart() -> pd.DataFrame:
    d = sheet("source_data/dbs_FA_CB_subpart_data_a.xlsx", header=0).iloc[:, :5].dropna()
    d = d.rename(columns={"hemi": "side"})
    return d.astype({"mk": int, "prepost": int, "side": int, "part": int})


def _mkD(path: str, last: str) -> pd.DataFrame:
    # These sheets have no header row; the legend (columns O onwards) names columns A to D.
    d = sheet(path).iloc[:, :4].dropna()
    d.columns = ["FA", "prepost", "side", last]
    return d.astype({"prepost": int, "side": int, last: int})


def fa_wholetract_mkD() -> pd.DataFrame:
    return _mkD("source_data/dbs_FA_wholetract_mkD_data_a.xlsx", "tract")


def fa_subpart_mkD() -> pd.DataFrame:
    return _mkD("source_data/dbs_FA_CB_subpart_mkD_data_a.xlsx", "part")


def cc1(region: str) -> pd.DataFrame:
    """region: 'MCC_CB', 'dACC_CB' or 'UF-FMoverlap'."""
    d = sheet(f"source_data/CC1_{region}_data_a.xlsx", header=0).iloc[:, :7].dropna(subset=["CC1"])
    d.columns = ["CC1", "DAPI", "ratio", "mk", "side", "section", "location"]
    return d.astype({"CC1": float, "DAPI": float, "ratio": float, "mk": int, "side": int, "location": int})


def cc1_mkD() -> pd.DataFrame:
    return sheet("source_data/CC1_mkD_MCC_CB_data_a.xlsx", header=0).iloc[:, :8].dropna(subset=["CC1_leadside"])


def gratio() -> pd.DataFrame:
    d = sheet("source_data/dbs_EMgratio_MCC_CB_data_a.xlsx").iloc[2:, :15]
    d.columns = ["n", "label", "n_in_image", "d_long", "d_short", "m_thick", "m_thin", "radius",
                 "myelin", "g", "aspect", "aspect_ok", "mk", "side", "diameter_nm"]
    d["label"] = d["label"].ffill()
    num = [c for c in d.columns if c != "label"]
    d[num] = d[num].astype(float)
    return d.astype({"mk": int, "side": int})


def seed_fc(which: str = "mkNT") -> pd.DataFrame:
    d = sheet(f"source_data/dbs_FC25norm_{which}_concatenated_all_data_a.xlsx", header=0).dropna(subset=["fc"])
    return d.astype({"subject": int, "roi": int, "time_condition": int, "side": int, "date": int})


def roi_labels() -> dict:
    d = sheet("source_data/FC_ROI_label.xlsx", header=0)
    return dict(zip(d.ROI_Number.astype(int), d.ROI_Name))


def network_data(fc: pd.DataFrame, lim_with_area25: bool = True) -> pd.DataFrame:
    """Voxels of each network's hubs, with repeats (Fig5BCandE9 script)."""
    parts = []
    for i, (name, rois) in enumerate(NETWORKS.items(), start=1):
        if name == "LIM" and not lim_with_area25:
            rois = [r for r in rois if r != AREA25]
        p = fc[fc.roi.isin(rois)].copy()
        p["network"] = i
        parts.append(p)
    return pd.concat(parts, ignore_index=True)


def connectomes(sheet_name: str) -> dict:
    """Pre, post and post-minus-pre ROI x ROI matrices from 'Source Data FC matrix.xlsx'."""
    d = sheet("source_data/Source Data FC matrix.xlsx", sheet_name=sheet_name)
    n = d.shape[1]
    out = {}
    for key, start in zip(["pre", "post", "diff"], [1, 1 + n + 2, 1 + 2 * (n + 2)]):
        out[key] = d.iloc[start:start + n, :n].astype(float).values
    out["titles"] = [d.iloc[0, 0], d.iloc[n + 2, 0], d.iloc[2 * (n + 2), 0]]
    return out


def offdiag(m: np.ndarray, i: int, keep_diag: bool = False) -> np.ndarray:
    return m[:, i] if keep_diag else np.delete(m[:, i], i)


# ---------------------------------------------------------------- ANOVA as MATLAB anovan

def _sum_coding(x: np.ndarray, levels) -> np.ndarray:
    cols = np.zeros((len(x), len(levels) - 1))
    for j, lev in enumerate(levels[:-1]):
        cols[:, j] = (x == lev).astype(float)
    cols[x == levels[-1], :] = -1.0
    return cols


def _term_columns(codes: dict, term: tuple) -> np.ndarray:
    blocks = [codes[f] for f in term]
    out = blocks[0]
    for b in blocks[1:]:
        out = np.einsum("ni,nj->nij", out, b).reshape(len(out), -1)
    return out


def anova(df: pd.DataFrame, y: str, factors: list, terms: list, sstype: int = 3) -> dict:
    """N-way ANOVA with sum-to-zero coding, as MATLAB anovan.

    terms: tuples of factor names, e.g. [("mk",), ("prepost",), ("prepost", "side")].
    Returns the table (SS, df, F, P, partial eta squared) and what `tukey_kramer` needs.
    """
    yv = df[y].to_numpy(float)
    levels = {f: sorted(df[f].unique()) for f in factors}
    codes = {f: _sum_coding(df[f].to_numpy(), levels[f]) for f in factors}
    blocks = {t: _term_columns(codes, t) for t in terms}

    def fit(ts):
        X = np.column_stack([np.ones(len(yv))] + [blocks[t] for t in ts])
        beta, *_ = np.linalg.lstsq(X, yv, rcond=None)
        r = yv - X @ beta
        return float(r @ r), X, beta

    sse, X, beta = fit(terms)
    dfe = len(yv) - np.linalg.matrix_rank(X)
    mse = sse / dfe
    rows = []
    for t in terms:
        if sstype == 3:
            reduced = [u for u in terms if u != t]
            full_ss = sse
        else:  # type II: the term against the terms that do not contain it
            reduced = [u for u in terms if not set(t) <= set(u)]
            full_ss = fit(reduced + [t])[0]
        ss = fit(reduced)[0] - full_ss
        dft = blocks[t].shape[1]
        F = (ss / dft) / mse
        rows.append({"term": " x ".join(t), "SS": ss, "df": dft, "F": F,
                     "P": stats.f.sf(F, dft, dfe), "eta_p2": ss / (ss + sse)})
    table = pd.DataFrame(rows).set_index("term")
    return {"table": table, "dfe": int(dfe), "mse": mse, "beta": beta, "X": X, "terms": terms,
            "levels": levels, "factors": factors, "n": len(yv)}


def tukey_kramer(fit: dict, dims: list, only_vary: str | None = None) -> pd.DataFrame:
    """Pairwise comparisons of population marginal means over `dims` (multcompare).

    The family is all pairs of the cells of `dims`, which sets the studentized range's number
    of means; `only_vary` returns only the pairs that differ in that factor alone (the pre
    against post pairs), which is faster and gives the same P values for those pairs.
    SciPy's studentized range tail loses accuracy below about 1e-7 and stops near 1e-11 (or
    returns 0), so P values that small are only read as far below 0.05.
    """
    levels, terms = fit["levels"], fit["terms"]
    combos = list(itertools.product(*[levels[f] for f in dims]))
    L = []
    for combo in combos:
        setting = dict(zip(dims, combo))
        row = [1.0]
        for t in terms:
            if all(f in setting for f in t):
                vecs = []
                for f in t:
                    lv = levels[f]
                    v = np.zeros(len(lv) - 1)
                    k = lv.index(setting[f])
                    if k < len(lv) - 1:
                        v[k] = 1.0
                    else:
                        v[:] = -1.0
                    vecs.append(v)
                out = vecs[0]
                for v in vecs[1:]:
                    out = np.outer(out, v).ravel()
                row.extend(out)
            else:
                row.extend(np.zeros(np.prod([len(levels[f]) - 1 for f in t])))
        L.append(row)
    L = np.array(L)
    XtX_inv = np.linalg.pinv(fit["X"].T @ fit["X"])
    means = L @ fit["beta"]
    cov = L @ XtX_inv @ L.T * fit["mse"]
    k = len(combos)
    out = []
    for i, j in itertools.combinations(range(k), 2):
        if only_vary is not None:
            diff = [f for f, a, b in zip(dims, combos[i], combos[j]) if a != b]
            if diff != [only_vary]:
                continue
        d = means[i] - means[j]
        se = np.sqrt(cov[i, i] + cov[j, j] - 2 * cov[i, j])
        q = abs(d) / se * np.sqrt(2)
        p = stats.studentized_range.sf(q, k, fit["dfe"])
        out.append({**{f"A_{f}": a for f, a in zip(dims, combos[i])},
                    **{f"B_{f}": b for f, b in zip(dims, combos[j])},
                    "A_mean": means[i], "B_mean": means[j], "A_minus_B": d, "P": p})
    return pd.DataFrame(out)


def prepost_pairs(tk: pd.DataFrame, by: str, prepost: str = "prepost") -> pd.DataFrame:
    """The pre against post comparison of each side and `by` level from `tukey_kramer`."""
    m = tk[(tk[f"A_{prepost}"] == 1) & (tk[f"B_{prepost}"] == 2)
           & (tk["A_side"] == tk["B_side"]) & (tk[f"A_{by}"] == tk[f"B_{by}"])]
    m = m.rename(columns={"A_side": "side", f"A_{by}": by, "A_mean": "pre", "B_mean": "post"})
    m["post_minus_pre"] = -m["A_minus_B"]
    return m[["side", by, "pre", "post", "post_minus_pre", "P"]].reset_index(drop=True)


def three_way_terms(mk: str | None, a: str, b: str, c: str) -> list:
    """`model_mat2` of the scripts: monkey main effect plus a full factorial of a, b, c."""
    t = [(a,), (b,), (c,), (a, b), (a, c), (b, c), (a, b, c)]
    return ([(mk,)] if mk else []) + t
