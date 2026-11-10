"""Per-mouse tables for Jones et al. (2019) on CRCNS hc-26: SWR measures from
:mod:`swr`, behavior metrics from :mod:`behavior`, performance scores, and the
correlation rule shared by most claims. Sources of each choice are given where it is
made ("Claims (X)" = the method X in the header of claims/jones-2019.yaml).
"""
from __future__ import annotations

import numpy as np
import pandas as pd

import behavior
import stats
from swr import FS

FAIL = "FAIL"


def session_table(rows: list) -> pd.DataFrame:
    """Sessions with the inclusion flags: the code's epoch filter (task env and descript
    not 'FAIL', runcalcriprates.m) and the Methods' 10 min of immobility."""
    d = pd.DataFrame(rows)
    d["fail"] = (d.task_env == FAIL) | (d.task_descript == FAIL)
    d["short_immobility"] = d.immobile_s < 600
    d["used"] = ~d.fail & ~d.short_immobility
    for k in ("5sd", "3sd", "direct5", "125_5sd", "125_3sd"):
        c = "n_swr_" + k
        if c in d:
            d["rate_" + k] = d[c] / d.immobile_s
    return d


def _pooled(g: pd.DataFrame, col: str) -> float:
    """Code reading (plotRTSstats.m): per site, the mean over all SWRs of all sessions;
    then the mean over sites."""
    acc = {}
    for _, r in g.iterrows():
        sites, sums, ns = r.get("sites_" + col.split("_")[1]), r.get(col + "_sitesum"), r.get(col + "_siten")
        if not isinstance(sums, list):
            continue
        for s, a, n in zip(sites, sums, ns):
            t = acc.setdefault(s, [0.0, 0])
            t[0] += a
            t[1] += n
    vals = [a / n for a, n in acc.values() if n > 0]
    return float(np.mean(vals)) if vals else np.nan


def mouse_table(sess: pd.DataFrame) -> pd.DataFrame:
    """One row per mouse and recording age. Abundance is SWRs per second of immobility
    per session, averaged over sessions (Claims (A)); SG power per region is averaged
    over sessions (Methods reading, 'sg_*') and pooled over SWRs per site (code reading,
    'sgpool_*') (Claims (B))."""
    d = sess[sess.used]
    sg_cols = [c for c in d.columns if c.startswith("sg_") and not c.endswith(("_sitesum", "_siten"))]
    out = []
    for (c, a, g, k), grp in d.groupby(["cohort", "age_group", "genotype", "key"]):
        row = {"cohort": c, "age_group": a, "genotype": g, "key": k,
               "animal": grp.animal.iloc[0], "n_sessions": len(grp),
               "age_months": grp.age_months.mean(), "immobile_s": grp.immobile_s.mean()}
        for col in [x for x in grp.columns if x.startswith("rate_")] + [
                "base", "sd", "ca3_sg_base", "ca3_sg_sd", "mua_during", "mua_pre400",
                "mua_pre400_300", "mua_immobile_rate"]:
            if col in grp:
                row[col] = grp[col].mean()
        for col in sg_cols:
            row[col] = grp[col].mean()
            row[col.replace("sg_", "sgpool_", 1)] = _pooled(grp, col)
        out.append(row)
    return pd.DataFrame(out)


# ------------------------------------------------------------------ behavior metrics
def mwm_metrics(cohort: int, age: str | None = None) -> pd.DataFrame:
    """The 22 MWM metrics of Table S2 per mouse (Claims (C), Methods 'Analysis of
    Behavioral Data'): slope of the daily mean latency over days 1-k (first-degree
    polynomial, k = 2..5), mean latency days 1-5, overnight change ('Night k': day k+1
    trial 1 minus day k trial 4, Figure S1C), and per probe 1-3 the percent time in the
    target quadrant, target crossings and area under the distance curve over the first
    5 s."""
    tr = behavior.mwm_hidden(cohort, age)
    tr = tr[tr.day <= 5]
    daily = tr.groupby(["mouse", "day"]).latency_s.mean().unstack()
    info = tr.groupby("mouse")[["name", "genotype"]].first()
    m = pd.DataFrame(index=daily.index)
    for k in (2, 3, 4, 5):
        days = np.arange(1, k + 1)
        m[f"slope_1_{k}"] = [np.polyfit(days, r[days].values, 1)[0]
                             if r[days].notna().all() else np.nan for _, r in daily.iterrows()]
    for k in range(1, 6):
        m[f"latency_d{k}"] = daily[k]
    t = tr.set_index(["mouse", "day", "trial"]).latency_s
    for k in range(1, 5):
        m[f"night_{k}"] = [t.get((ms, k + 1, 1), np.nan) - t.get((ms, k, 4), np.nan)
                           for ms in m.index]
    pr = behavior.mwm_probe(cohort, age)
    for p in (1, 2, 3):
        q = pr[pr.probe == p].set_index("mouse")
        m[f"pct_quadrant_p{p}"] = q.pct_time_target_quadrant
        m[f"crossings_p{p}"] = q.target_crossings
        m[f"auc_p{p}"] = q.auc_first5s
    m = info.join(m)
    m["key"] = m.name.map(lambda s: behavior.norm_name(s) if isinstance(s, str) else None)
    return m.reset_index()


MWM22 = ([f"slope_1_{k}" for k in (2, 3, 4, 5)] + [f"latency_d{k}" for k in range(1, 6)]
         + [f"night_{k}" for k in range(1, 5)]
         + [f"{m}_p{p}" for p in (1, 2, 3) for m in ("pct_quadrant", "crossings", "auc")])
MWM_LEARN = ["slope_1_2", "slope_1_3", "latency_d3", "night_1"]
MWM_LEARN_INV = MWM_LEARN
MWM_MEM = ["pct_quadrant_p1", "pct_quadrant_p2", "crossings_p1", "auc_p1", "auc_p2"]
MWM_MEM_INV = ["auc_p1", "auc_p2"]
APA5 = ["entrances", "latency_first_entrance_s", "path_length_m", "pct_time_opp", "dpb"]


def apa_metrics(dpb: str = "dist_per_bout_walk_cm") -> pd.DataFrame:
    """APA metrics per mouse on training days 1-4 (Claims (D)); ``dpb`` picks the
    distance-per-bout column of pull_apa_metrics.py (all bouts or walk bouts). The
    mouse excluded in the data set's sheets is dropped."""
    a = behavior.apa()
    a = a[(a.day >= 1) & (a.day <= 4) & ~a.excluded.astype(bool)].copy()
    a["dpb"] = a[dpb]
    w = a.pivot_table(index="mouse", columns="day", values=APA5)
    w.columns = [f"{m}_d{d}" for m, d in w.columns]
    info = a.groupby("mouse")[["name", "genotype"]].first()
    w = info.join(w)
    w["key"] = w.name.map(lambda s: behavior.norm_name(s) if isinstance(s, str) else None)
    return w.reset_index()


def scores(tab: pd.DataFrame, metrics, invert, population: str, geno_col="genotype"):
    """Performance score (Claims (E)) under a z-score population reading: 'e4' (the E4
    mice with the SWR measure, i.e. the rows given with genotype E4 and a value of
    column 'x') or 'all' (all mice of the cohort in ``tab``)."""
    if population == "e4":
        pop = (tab[geno_col] == "E4") & tab["x"].notna() if "x" in tab else tab[geno_col] == "E4"
    else:
        pop = pd.Series(True, index=tab.index)
    s, info = stats.performance_score(tab, metrics, invert, population_index=pop[pop].index)
    return s


def corr_report(x, y, label: str = "") -> dict:
    """Pearson (Claims (F)) with leave-one-out p (loocv.m)."""
    r = stats.pearson(x, y)
    loo = stats.loo_pearson(x, y) if r["n"] > 3 else {"n_above_alpha": np.nan, "p": []}
    r["loo_fail"] = loo["n_above_alpha"]
    r["loo_max_p"] = float(np.nanmax(loo["p"])) if len(loo["p"]) else np.nan
    print(f"{label:55s} n={r['n']:2d} R={r['r']:+.3f} R2={r['r2']:.3f} "
          f"F({r['df'][0]},{r['df'][1]})={r['F']:.2f} p={r['p']:.4f} "
          f"LOO: {r['loo_fail']} removals p>0.05 (max p {r['loo_max_p']:.3f})")
    return r


def judge_corr(r: dict, expected_r: float, tol: float, p_key: str = "p") -> str:
    """The claims' rule for a correlation (fig2b-swr-slope-days-1-2): sign and p < 0.05
    and R within tolerance -> reproduced; sign and p but R outside -> partially;
    otherwise not reproduced."""
    if not np.isfinite(r["r"]) or np.sign(r["r"]) != np.sign(expected_r) or r[p_key] >= 0.05:
        return "not_reproduced"
    return "reproduced" if abs(r["r"] - expected_r) <= tol else "partially_reproduced"
