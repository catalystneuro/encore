"""Loading and measures for Zhuang, Lemak, Sridhar & Nelson (2025), Brain, doi:10.1093/brain/awaf312.

Two sources are read, both streamed and held in memory, never written to disk:

- DANDI:001177 at version 0.250902.2127, the in vivo electrophysiology (Figure 4, 6F-K, S5, S8).
  Only metadata, array shapes and the two `units` tables are read; the claims on these data are
  blocked (see the notebook), so no voltage is streamed.
- Zenodo record 15258978 (doi:10.5281/zenodo.15258978), the paper's deposit of its behaviour,
  histology and slice data. The claims file names it as the data of every `data: elsewhere` claim.

Where each parameter comes from:

- Delay discounting events. The block and event names follow the paper's analysis code,
  UCSF-Nelson-Lab/ICD-Cognitive-Analysis at commit 5528e222 (delay_discounting_task.py,
  processCsv_1): the free choice blocks are B3, B6, B9 and B12, events are counted only inside
  them, "l reward delivery" and "s reward delivery" mark delayed/large and immediate/small
  choices, "center omi" and "side omi" omissions. The delays of these blocks, 0, 3, 6 and 9 s,
  are from the Supplementary methods ("Operant Training and Assessment": the delay "increased
  across a session (between blocks) from 0 s (block 1) to 3 s (block 2), to 6 s (block 3) to 9 s
  (block 4)").
- Choice measure. "the percentage of free choice trials (excluding omissions) on which mice chose
  the delayed/large reward" (Supplementary methods, Experimental design, Behavior).
- Choice latency. "the interval between the illumination of the nosepoke (side) cue light and a
  nosepoke (side) response, excluding side omissions" (same passage). The code marks the side cue
  light by "cen tri" and the response by the first "np_B in" or "np_D in" after it.
- Hyperbolic fit. V = A/(1 + K D) fitted by least squares from A = 1, K = 0.5 without bounds, on
  the fraction of delayed/large choices, and AUC the trapezoidal integral of the fitted values at
  D = 0, 3, 6, 9 s, as Summary_Cognitive.m does (claims file, fig1ijk-ppx-a-k-auc).
- Stability rule for baseline reading (b). "CV < 20% in at least 3 blocks for three consecutive
  sessions, or CV < 20% in each block for two consecutive sessions" (Supplementary methods,
  Behavior). Which stable run is used, when there are several, is not stated; the last one before
  the first drug session is taken (an assumption, stated in the notebook).
- Groups. The control and parkinsonian, mCherry, hM4Di and hM3Dq mouse lists are those of the
  deposit's README_ICD_CognitiveAssessment.txt, parsed at run time.
- Two-way "repeated measures" ANOVA. The degrees of freedom the paper prints (F(1, 60) for 16
  control mice, F(1, 120) for 31 parkinsonian mice, F(1, 44) for 12 DREADD mice) are those of a
  split-plot design in which each mouse and delay pair is the unit measured under both
  treatments, with delay between units: error df = (mice x 4 - 4) x (treatments - 1). This is the
  layout `split_plot_anova` computes. The per-delay Bonferroni comparisons use the pooled
  within-unit error of that ANOVA, as GraphPad Prism does, and multiply p by the number of delays.
  A paired t test per delay, Bonferroni corrected, is the variant.
- Between-group two-way ANOVA (Figure 1F-G baseline, F(1, 180) for 47 mice): ordinary two-way
  ANOVA on group and delay with every mouse and delay value an observation, type III sums of
  squares; per-delay Bonferroni comparisons use the pooled error.
- Friedman with Dunn's comparisons, "between baseline and PPX ON or OFF conditions"
  (Supplementary methods, Behavior): Dunn's z on mean ranks, Bonferroni over the two comparisons
  with baseline.
"""

from __future__ import annotations

import io
import json
import re
import urllib.parse
import urllib.request
import zipfile
from functools import lru_cache

import fsspec
import numpy as np
import pandas as pd
from scipy import optimize, stats

DANDISET = "001177"
DANDI_VERSION = "0.250902.2127"
ZENODO_RECORD = "15258978"
ZENODO_DOI = "10.5281/zenodo.15258978"
CODE_REPO = "https://github.com/UCSF-Nelson-Lab/ICD-Cognitive-Analysis"
CODE_COMMIT = "5528e2229f186e0785a676ae6f15219c47146930"

DELAYS = [0, 3, 6, 9]
FREE_BLOCKS = {"B3": 0, "B6": 3, "B9": 6, "B12": 9}
COGNITIVE_ZIP = "Data_ICD_Fig1&2&5&6_CognitiveAssay.zip"


# ---------------------------------------------------------------- DANDI

def dandi_assets() -> pd.DataFrame:
    url = (f"https://api.dandiarchive.org/api/dandisets/{DANDISET}/versions/{DANDI_VERSION}"
           "/assets/?page_size=200")
    rows = json.load(urllib.request.urlopen(url))["results"]
    return pd.DataFrame([{"path": r["path"], "asset_id": r["asset_id"], "size_gb": r["size"] / 1e9}
                         for r in rows]).sort_values("path").reset_index(drop=True)


def dandi_metadata() -> dict:
    url = f"https://api.dandiarchive.org/api/dandisets/{DANDISET}/versions/{DANDI_VERSION}/"
    return json.load(urllib.request.urlopen(url))


def open_nwb(asset_id: str):
    import h5py
    import remfile
    return h5py.File(remfile.File(f"https://api.dandiarchive.org/api/assets/{asset_id}/download/"), "r")


def survey_file(asset_id: str) -> dict:
    """What one NWB file holds, from its metadata and array shapes only."""
    f = open_nwb(asset_id)
    text = lambda p: f[p][()].decode("utf-8", "replace") if p in f else None
    acq = f["acquisition"]
    series = [k for k in acq if k.startswith("ElectricalSeries")]
    spike_events = [k for k in acq if k.startswith("SpikeEvents")]
    segments = [(float(acq[k]["starting_time"][()]) / 60, acq[k]["data"].shape[0] / 30000 / 60)
                for k in series]
    out = {
        "subject": text("general/subject/subject_id"),
        "genotype": text("general/subject/genotype"),
        "sex": text("general/subject/sex"),
        "lesion": ("6-OHDA" if "6-OHDA" in (text("general/subject/description") or "")
                   else "saline" if "saline" in (text("general/subject/description") or "") else "?"),
        "description_start": (text("general/subject/description") or "")[:40],
        "session_id": text("general/session_id"),
        "start": text("session_start_time"),
        "n_segments": len(series),
        "segments_min": "; ".join(f"{s:.1f}+{d:.1f}" for s, d in segments),
        "n_channels": acq[series[0]]["data"].shape[1] if series else 0,
        "n_spike_event_series": len(spike_events),
        "n_threshold_crossings": int(sum(acq[k]["timestamps"].shape[0] for k in spike_events)),
        "has_units": "units" in f,
        "units_columns": ",".join(f["units"].attrs["colnames"]) if "units" in f else "",
        "n_units": f["units"]["id"].shape[0] if "units" in f else 0,
        "intervals": ",".join(f["intervals"].keys()) if "intervals" in f else "",
        "stimulus": ",".join(f["stimulus/presentation"].keys()),
        "ogen": "ogen_sites" in f["general"] or "optogenetics" in f["general"],
        "processing": ",".join(f"{m}/{k}" for m in f["processing"] for k in f["processing"][m]),
        "behavior_in_file": any("behavior" in m.lower() for m in f["processing"]),
    }
    if out["has_units"]:
        idx = f["units"]["spike_times_index"][:]
        out["unit_spike_counts"] = np.diff(np.r_[0, idx]).tolist()
    return out


# ---------------------------------------------------------------- Zenodo

def zenodo_files() -> pd.DataFrame:
    d = json.load(urllib.request.urlopen(f"https://zenodo.org/api/records/{ZENODO_RECORD}"))
    return pd.DataFrame([{"key": f["key"], "size_mb": f["size"] / 1e6, "checksum": f["checksum"]}
                         for f in d["files"]])


def zenodo_url(name: str) -> str:
    return f"https://zenodo.org/records/{ZENODO_RECORD}/files/{urllib.parse.quote(name)}?download=1"


@lru_cache(maxsize=None)
def zenodo_bytes(name: str) -> bytes:
    with fsspec.open(zenodo_url(name), block_size=2**22) as fh:
        return fh.read()


def read_excel(name: str, **kw) -> dict:
    return pd.read_excel(io.BytesIO(zenodo_bytes(name)), sheet_name=None, header=None, **kw)


@lru_cache(maxsize=None)
def readme_groups() -> dict:
    """Mouse lists per experiment and group, from README_ICD_CognitiveAssessment.txt."""
    text = zenodo_bytes("README_ICD_CognitiveAssessment.txt").decode("utf-8", "replace")
    names = {"Control": "control", "Parkinsonian": "parkinsonian", "mCherry": "mCherry",
             "Inhibitory DREADD (hM4Di)": "hM4Di", "Excitatory DREADD (hM3Dq)": "hM3Dq"}
    groups, experiment, key = {}, None, None
    for line in text.splitlines():
        line = line.strip()
        if line.endswith("related experiments"):
            experiment, key = line.split("-")[0].strip(), None
            continue
        m = re.match(r"^(" + "|".join(re.escape(n) for n in names) + r"):\s*(.*)$", line)
        if m and experiment:
            key = (experiment, names[m.group(1)])
            groups[key] = [x.strip() for x in m.group(2).split(",") if x.strip()]
        elif key and line and ":" not in line and "," in line:
            groups[key] += [x.strip() for x in line.split(",") if x.strip()]
        elif not line:
            key = None if key and groups.get(key) and not line else key
    return groups


@lru_cache(maxsize=None)
def cognitive_archives() -> dict:
    """The three inner zips of the cognitive assay deposit, opened in memory."""
    outer = zipfile.ZipFile(io.BytesIO(zenodo_bytes(COGNITIVE_ZIP)))
    out = {}
    for name in outer.namelist():
        if name.endswith(".zip") and not name.startswith("__MACOSX"):
            key = name.split("/")[-1].replace("Data_ICD_", "").replace(".zip", "")
            out[key] = zipfile.ZipFile(io.BytesIO(outer.read(name)))
    return out


DELAY_FILE = re.compile(r"^(?P<mouse>[^_]+)_delay(?: discounting)?(?:_(?P<cond>[^_]*?))?_(?P<date>[^_]+)\.CSV$",
                        re.IGNORECASE)


def condition_of(tag: str | None) -> str | None:
    tag = (tag or "").replace(" ", "").lower()
    if tag == "":
        return "baseline"
    if "washout" in tag or "washont" in tag:
        return "off"
    if tag in ("ppx", "a77636", "cno"):
        return "on"
    return None


def _ms(t: str) -> float:
    h, m, s, ms = (int(x) for x in t.strip().split(":"))
    return ((h * 60 + m) * 60 + s) * 1000 + ms


def parse_session(text: str) -> dict:
    """Per free choice block: choices, omissions and choice latencies (ms), and the session date."""
    blocks = {d: {"large": 0, "small": 0, "center_om": 0, "side_om": 0, "trials": 0,
                  "lat_large": [], "lat_small": []} for d in DELAYS}
    current = None
    labels = {}
    cue_time = None
    first_side = None
    date = None
    for line in text.splitlines()[1:]:
        parts = [p.strip().strip('"') for p in line.split(",")]
        if len(parts) < 3:
            continue
        stamp, event, t = parts[0], parts[1], parts[2]
        if date is None and stamp:
            date = stamp.split(" ")[0]
        b = re.match(r"B(\d+)_", event)
        if b:
            current = FREE_BLOCKS.get("B" + b.group(1))
            if current is not None:
                labels[current] = event
            continue
        if current is None:
            continue
        blk = blocks[current]
        if event == "trial start":
            blk["trials"] += 1
            cue_time, first_side = None, None
        elif event == "cen tri":
            cue_time, first_side = _ms(t), None
        elif event in ("np_B in", "np_D in") and cue_time is not None and first_side is None:
            first_side = _ms(t) - cue_time
        elif event == "l reward delivery":
            blk["large"] += 1
            if first_side is not None:
                blk["lat_large"].append(first_side)
        elif event == "s reward delivery":
            blk["small"] += 1
            if first_side is not None:
                blk["lat_small"].append(first_side)
        elif event == "center omi":
            blk["center_om"] += 1
        elif event == "side omi":
            blk["side_om"] += 1
    return {"date": pd.to_datetime(date, format="%Y/%m/%d", errors="coerce") if date else pd.NaT,
            "blocks": blocks, "labels": labels}


def name_date(token: str):
    """The session date written in a file name as mmddyy; NaT when it is not six digits."""
    return pd.to_datetime(token, format="%m%d%y", errors="coerce") if re.fullmatch(r"\d{6}", token) else pd.NaT


@lru_cache(maxsize=None)
def sessions() -> pd.DataFrame:
    """One row per delay discounting session and free choice block, for the three experiments."""
    groups = readme_groups()
    rows, skipped = [], []
    for experiment, zf in cognitive_archives().items():
        exp = {"PPX": "PPX", "A77636": "A77636", "DREADD": "DREADD"}[experiment]
        for name in zf.namelist():
            base = name.split("/")[-1]
            if name.startswith("__MACOSX") or "_delay" not in base:
                continue
            m = DELAY_FILE.match(base.replace("CSV.CSV", ".CSV"))
            if not m:
                skipped.append((experiment, base, "name"))
                continue
            cond = condition_of(m.group("cond"))
            if cond is None:
                skipped.append((experiment, base, "condition"))
                continue
            mouse = m.group("mouse")
            group = [g for (e, g), ids in groups.items() if e == exp and mouse in ids]
            s = parse_session(zf.read(name).decode("latin-1"))
            date = name_date(m.group("date"))
            date_from = "name"
            if pd.isna(date):
                date, date_from = s["date"], "log"
            for d, blk in s["blocks"].items():
                rows.append({"experiment": exp, "mouse": mouse, "group": group[0] if group else None,
                             "file": base, "condition": cond, "date": date, "date_from": date_from,
                             "log_date": s["date"], "delay": d,
                             "large": blk["large"], "small": blk["small"],
                             "center_om": blk["center_om"], "side_om": blk["side_om"],
                             "trials": blk["trials"], "block_label": s["labels"].get(d, ""),
                             "lat_large": np.mean(blk["lat_large"]) / 1000 if blk["lat_large"] else np.nan,
                             "lat_small": np.mean(blk["lat_small"]) / 1000 if blk["lat_small"] else np.nan,
                             "lat_all": (np.mean(blk["lat_large"] + blk["lat_small"]) / 1000
                                         if blk["lat_large"] + blk["lat_small"] else np.nan)})
    df = pd.DataFrame(rows)
    chosen = df["large"] + df["small"]
    df["pct_large"] = np.where(chosen > 0, 100 * df["large"] / chosen.where(chosen > 0, 1), np.nan)
    df["pct_center_om"] = 100 * df["center_om"] / df["trials"].where(df["trials"] > 0)
    df["pct_side_om"] = 100 * df["side_om"] / df["trials"].where(df["trials"] > 0)
    df.attrs["skipped"] = skipped
    return df


def wide(df: pd.DataFrame, value: str = "pct_large") -> pd.DataFrame:
    """Sessions by delay: one row per session file."""
    return df.pivot_table(index=["experiment", "group", "mouse", "condition", "date", "file"],
                          columns="delay", values=value, aggfunc="first").reset_index()


def stable_window(base: pd.DataFrame) -> list:
    """The files of the last stable run of baseline sessions (reader's rule, see module docstring).

    `base` is one mouse's baseline sessions in `wide` form, ordered by date. Returns [] when no run
    meets the rule."""
    base = base.sort_values("date")
    vals = base[DELAYS].to_numpy(float)
    files = base["file"].tolist()
    found = []
    for i in range(len(files)):
        for n, need in ((3, 3), (2, 4)):
            if i + n <= len(files):
                w = vals[i:i + n]
                mean = np.nanmean(w, axis=0)
                cv = np.where(mean > 0, np.nanstd(w, axis=0, ddof=1) / mean * 100, np.inf)
                if np.sum(cv < 20) >= need:
                    found.append(files[i:i + n])
    return found[-1] if found else []


# ---------------------------------------------------------------- fits

def hyperbolic(d, a, k):
    return a / (1 + k * d)


def fit_curve(values) -> tuple:
    """A, K and AUC of V = A/(1 + K D) on fractions at D = 0, 3, 6, 9 s; NaN when the fit fails."""
    y = np.asarray(values, float)
    if np.isnan(y).any():
        return np.nan, np.nan, np.nan
    try:
        (a, k), _ = optimize.curve_fit(hyperbolic, np.array(DELAYS, float), y, p0=[1, 0.5],
                                       maxfev=1000)
    except (RuntimeError, optimize.OptimizeWarning):
        return np.nan, np.nan, np.nan
    pred = hyperbolic(np.array(DELAYS, float), a, k)
    return a, k, np.trapezoid(pred, DELAYS)


# ---------------------------------------------------------------- statistics

def split_plot_anova(data: pd.DataFrame, value: str, treat: str, levels: list) -> dict:
    """Two-way ANOVA with delay between units and treatment within units (unit = mouse x delay).

    `data` has columns mouse, delay, `treat` and `value`; units missing a level are dropped.
    Returns the treatment, delay and interaction F tests and Bonferroni per-delay comparisons of
    each level against the first."""
    piv = data.pivot_table(index=["mouse", "delay"], columns=treat, values=value)[levels].dropna()
    y = piv.to_numpy(float)
    delays = piv.index.get_level_values("delay").to_numpy()
    k = len(levels)
    n_units = len(piv)
    grand = y.mean()
    unit_mean = y.mean(axis=1)
    lev_mean = y.mean(axis=0)
    d_levels = sorted(set(delays))
    ss_t = n_units * np.sum((lev_mean - grand) ** 2)
    ss_d = ss_dt = ss_err_b = ss_err_w = 0.0
    for d in d_levels:
        sel = delays == d
        yd = y[sel]
        nd = sel.sum()
        md = yd.mean()
        mdt = yd.mean(axis=0)
        ss_d += nd * k * (md - grand) ** 2
        ss_dt += nd * np.sum((mdt - md - lev_mean + grand) ** 2)
        ss_err_b += k * np.sum((yd.mean(axis=1) - md) ** 2)
        ss_err_w += np.sum((yd - yd.mean(axis=1, keepdims=True) - mdt + md) ** 2)
    df_t, df_d = k - 1, len(d_levels) - 1
    df_dt = df_t * df_d
    df_eb = n_units - len(d_levels)
    df_ew = df_eb * (k - 1)
    ms_ew = ss_err_w / df_ew
    out = {"n_mice": piv.index.get_level_values("mouse").nunique(), "n_units": n_units,
           "treat_F": (ss_t / df_t) / ms_ew, "treat_df": (df_t, df_ew),
           "delay_F": (ss_d / df_d) / (ss_err_b / df_eb), "delay_df": (df_d, df_eb),
           "inter_F": (ss_dt / df_dt) / ms_ew, "inter_df": (df_dt, df_ew)}
    out["treat_p"] = stats.f.sf(out["treat_F"], df_t, df_ew)
    out["delay_p"] = stats.f.sf(out["delay_F"], df_d, df_eb)
    out["inter_p"] = stats.f.sf(out["inter_F"], df_dt, df_ew)
    comps = []
    n_comp = len(d_levels) * (k - 1)
    for d in d_levels:
        yd = y[delays == d]
        for j in range(1, k):
            diff = yd[:, j] - yd[:, 0]
            t_pool = diff.mean() / np.sqrt(2 * ms_ew / len(diff))
            p_pool = min(1.0, 2 * stats.t.sf(abs(t_pool), df_ew) * n_comp)
            t_pair, p_pair = stats.ttest_rel(yd[:, j], yd[:, 0])
            comps.append({"delay": d, "level": levels[j], "n": len(diff),
                          "mean_" + str(levels[0]): yd[:, 0].mean(), "mean_level": yd[:, j].mean(),
                          "diff": diff.mean(), "p_bonf_pooled": p_pool,
                          "p_bonf_paired": min(1.0, p_pair * n_comp)})
    out["per_delay"] = pd.DataFrame(comps)
    return out


def between_anova(data: pd.DataFrame, value: str, factor: str) -> dict:
    """Ordinary two-way ANOVA of `value` on `factor` and delay (type III), with per-delay
    Bonferroni comparisons of the two factor levels on the pooled error."""
    import statsmodels.formula.api as smf
    from statsmodels.stats.anova import anova_lm
    d = data.dropna(subset=[value]).copy()
    model = smf.ols(f"{value} ~ C({factor}, Sum) * C(delay, Sum)", data=d).fit()
    table = anova_lm(model, typ=3)
    mse, df_e = model.mse_resid, model.df_resid
    levels = sorted(d[factor].unique())
    comps = []
    for dl in DELAYS:
        a = d[(d.delay == dl) & (d[factor] == levels[0])][value]
        b = d[(d.delay == dl) & (d[factor] == levels[1])][value]
        t = (b.mean() - a.mean()) / np.sqrt(mse * (1 / len(a) + 1 / len(b)))
        comps.append({"delay": dl, levels[0]: a.mean(), levels[1]: b.mean(), "n0": len(a), "n1": len(b),
                      "p_bonf": min(1.0, 2 * stats.t.sf(abs(t), df_e) * len(DELAYS))})
    row = lambda name: table.loc[[i for i in table.index if name in i and ":" not in i][0]]
    inter = table.loc[[i for i in table.index if ":" in i][0]]
    return {"factor_F": row(f"C({factor}")["F"], "factor_p": row(f"C({factor}")["PR(>F)"],
            "delay_F": row("C(delay")["F"], "delay_p": row("C(delay")["PR(>F)"],
            "inter_F": inter["F"], "inter_p": inter["PR(>F)"],
            "df": (1, int(df_e)), "delay_df": (3, int(df_e)), "per_delay": pd.DataFrame(comps),
            "n_mice": d.groupby(factor)["mouse"].nunique().to_dict()}


def friedman_dunn(table: pd.DataFrame, reference: str) -> dict:
    """Friedman test over the columns of `table` (one row per mouse, complete rows only) and
    Dunn's z for each column against `reference`, Bonferroni over those comparisons."""
    t = table.dropna()
    chi2, p = stats.friedmanchisquare(*[t[c] for c in t.columns])
    ranks = t.rank(axis=1)
    k, n = t.shape[1], len(t)
    se = np.sqrt(k * (k + 1) / (6 * n))
    others = [c for c in t.columns if c != reference]
    dunn = {}
    for c in others:
        z = (ranks[c].mean() - ranks[reference].mean()) / se
        dunn[c] = {"z": z, "p_bonf": min(1.0, 2 * stats.norm.sf(abs(z)) * len(others)),
                   "median_ref": t[reference].median(), "median": t[c].median()}
    return {"n": n, "chi2": chi2, "p": p, "dunn": dunn}


def main_effect_pairs(data: pd.DataFrame, value: str, treat: str, levels: list) -> pd.DataFrame:
    """Bonferroni comparisons of treatment levels pooled over delays, on the pooled within-unit
    error of `split_plot_anova` (the 'first against fourth session' tests of Figure 6B-E)."""
    piv = data.pivot_table(index=["mouse", "delay"], columns=treat, values=value)[levels].dropna()
    res = split_plot_anova(data, value, treat, levels)
    df_ew = res["treat_df"][1]
    # recompute the pooled within-unit mean square
    y = piv.to_numpy(float)
    delays = piv.index.get_level_values("delay").to_numpy()
    ss = 0.0
    for d in sorted(set(delays)):
        yd = y[delays == d]
        ss += np.sum((yd - yd.mean(axis=1, keepdims=True) - yd.mean(axis=0) + yd.mean()) ** 2)
    mse = ss / df_ew
    pairs = [(a, b) for i, a in enumerate(levels) for b in levels[i + 1:]]
    rows = []
    for a, b in pairs:
        diff = piv[b].mean() - piv[a].mean()
        t = diff / np.sqrt(2 * mse / len(piv))
        rows.append({"pair": f"{a} vs {b}", "mean_a": piv[a].mean(), "mean_b": piv[b].mean(),
                     "diff": diff, "n_units": len(piv),
                     "p_bonf": min(1.0, 2 * stats.t.sf(abs(t), df_ew) * len(pairs))})
    return pd.DataFrame(rows)


def rm_oneway(table: pd.DataFrame, reference: str) -> dict:
    """Repeated measures one-way ANOVA over the columns of `table` (complete rows), with
    Bonferroni-corrected paired t tests between every pair of columns (Table 1's reading), and as
    a variant Bonferroni comparisons on the ANOVA's pooled residual error, as GraphPad Prism makes
    them by default (`pairs_pooled`)."""
    t = table.dropna()
    y = t.to_numpy(float)
    n, k = y.shape
    grand = y.mean()
    ss_c = n * np.sum((y.mean(axis=0) - grand) ** 2)
    ss_s = k * np.sum((y.mean(axis=1) - grand) ** 2)
    ss_e = np.sum((y - grand) ** 2) - ss_c - ss_s
    df_c, df_e = k - 1, (k - 1) * (n - 1)
    F = (ss_c / df_c) / (ss_e / df_e)
    cols = list(t.columns)
    pairs = [(a, b) for i, a in enumerate(cols) for b in cols[i + 1:]]
    comps = {f"{a} vs {b}": min(1.0, stats.ttest_rel(t[a], t[b]).pvalue * len(pairs)) for a, b in pairs}
    se = np.sqrt(2 * (ss_e / df_e) / n)
    pooled = {f"{a} vs {b}": min(1.0, 2 * stats.t.sf(abs(t[b].mean() - t[a].mean()) / se, df_e) * len(pairs))
              for a, b in pairs}
    return {"n": n, "F": F, "df": (df_c, df_e), "p": stats.f.sf(F, df_c, df_e), "pairs": comps,
            "pairs_pooled": pooled}


# ---------------------------------------------------------------- histology

HISTOLOGY = "Data_ICD_Fig3_HistologyQuantification_striatum_raw.xlsx"


def striatal_th() -> pd.DataFrame:
    """Corrected total fluorescence (CTF) per mouse and subregion, from the histology workbook.

    CTF = (RawIntDen - Area x mean background) / Area, the background the mean of the four
    'background' ROIs of the section (Supplementary methods, Histology, quantification and
    microscopy). DLS and DMS average the left and right ROIs; VS averages VLS and VMS of both
    sides ("VLS and VMS were then combined into ventral striatum (VS)"). Sections are averaged per
    mouse within each staining cohort."""
    rows = []
    for sheet, d in read_excel(HISTOLOGY).items():
        starts = [i for i in range(len(d)) if isinstance(d.iat[i, 0], str) and "sections" in d.iat[i, 0].lower()]
        for s in starts:
            group = "parkinsonian" if d.iat[s, 0].lower().startswith("park") else "control"
            labels = d.iloc[s + 2:s + 20, 0].tolist()
            for c in range(1, d.shape[1] - 2):
                name = d.iat[s, c]
                if not isinstance(name, str) or d.iat[s + 1, c] != "Area":
                    continue
                mouse = re.split(r"[_-]sl", name.strip())[0].strip()
                blk = d.iloc[s + 2:s + 20, c:c + 3].apply(pd.to_numeric, errors="coerce").to_numpy(float)
                roi = dict(zip(labels, blk))
                bg = np.nanmean([v[1] for k, v in roi.items() if str(k).startswith("background")])
                ctf = {str(k).replace("-", ""): (v[2] - v[0] * bg) / v[0] for k, v in roi.items()
                       if not str(k).startswith(("blank", "background"))}
                rows.append({"cohort": sheet.replace("Striatum_TH_", ""), "group": group, "mouse": mouse,
                             "section": name.strip(),
                             "DLS": np.nanmean([ctf.get("DLS2", np.nan), ctf.get("DLS7", np.nan)]),
                             "DMS": np.nanmean([ctf.get("DMS3", np.nan), ctf.get("DMS8", np.nan)]),
                             "VS": np.nanmean([ctf.get(k, np.nan) for k in ("VLS4", "VMS5", "VLS9", "VMS10")])})
    sec = pd.DataFrame(rows)
    return sec


# ---------------------------------------------------------------- open field

def open_field(zip_name: str) -> pd.DataFrame:
    """Velocity (cm/s) per frame of every open field session in one deposit zip, with its mouse."""
    import openpyxl  # noqa: F401  (imported before reading, so the engine loads once)
    zf = zipfile.ZipFile(io.BytesIO(zenodo_bytes(zip_name)))
    out = []
    for name in zf.namelist():
        if not name.endswith(".xlsx") or name.startswith("__MACOSX"):
            continue
        d = pd.read_excel(io.BytesIO(zf.read(name)), header=None)
        t = pd.to_numeric(d[0], errors="coerce").to_numpy(float)
        v = pd.to_numeric(d[3], errors="coerce").to_numpy(float)
        out.append({"file": name.split("/")[-1], "mouse": name.split("/")[-1].split("_")[0],
                    "t_min": t / 60, "velocity": v})
    return pd.DataFrame(out)


def tracking_gaps(t_min, v, near=(15, 25), min_frames=5) -> list:
    """Runs of at least `min_frames` untracked frames starting between `near` minutes."""
    miss = np.isnan(v)
    runs, start = [], None
    for i, m in enumerate(miss):
        if m and start is None:
            start = i
        if (not m or i == len(miss) - 1) and start is not None:
            end = i if not m else i + 1
            if end - start >= min_frames and near[0] <= t_min[start] <= near[1]:
                runs.append((t_min[start], end - start))
            start = None
    return runs


# ---------------------------------------------------------------- instrumental learning

INSTRUMENTAL = "Data_ICD_FigS1_SNcTH_CellCounting_RawImages.xlsx"


def instrumental_tables() -> pd.DataFrame:
    """Per mouse and session, success and latency of the blocked (Figure S1H-I) and random
    (Figure S1K-L) learning phases, read from the two sheets of the workbook as labelled."""
    sheets = read_excel(INSTRUMENTAL)
    rows = []
    for sheet, cols in (("Fig. S1H&I", {"success": 13, "latency": 14}),
                        ("Fig. S1K&L", {"success": 5, "latency": 8})):
        d = sheets[sheet]
        label = None
        for i in range(len(d)):
            first = d.iat[i, 0]
            if isinstance(first, str):
                m = re.match(r"Session\s*(\d+)_(Ctrl|Park)", first.strip())
                label = (int(m.group(1)), "control" if m.group(2) == "Ctrl" else "parkinsonian", i) if m else None
                continue
            if label is None or any(isinstance(v, str) for v in d.iloc[i].tolist()):
                continue
            vals = pd.to_numeric(d.iloc[i, list(cols.values())], errors="coerce").to_numpy(float)
            if np.isnan(vals).all():
                continue
            rows.append({"phase": "blocked" if "H&I" in sheet else "random", "session": label[0],
                         "group": label[1], "header_row": label[2], "row": i,
                         "success": vals[0], "latency": vals[1]})
    return pd.DataFrame(rows)
