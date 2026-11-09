"""Loading and measures for the LC and pupil data of dandiset 002034.

Thompson & Gold (2026), "Limitations of pupil diameter as a proxy for modes of locus coeruleus
activity", eLife reviewed preprint, doi:10.7554/elife.112525. A reanalysis of the data of
Joshi et al. (2016).

Each NWB file holds one session: a trial table (`correct`, `beep_time_ms`, `trial_time_index`,
start and stop times), the pupil trace of every trial flattened into one series
(`acquisition/pupil_value_channel4`, trial by 1 ms sample, NaN past the end of each trial), and
one to three sorted units whose spike times are given against trial anchors placed 100 s apart
(`spike_time_policy`). Files are streamed from the archive at the pinned version; nothing is
written to disk.

Where the parameters come from (claims file `claims/002034/10.7554-elife.112525.yaml`, opening
comment, which cites the Methods and the paper's code; the code is
https://github.com/lwthompson2/Thompson2026_LCPupilAnalysis at commit `CODE_COMMIT`):

- Trials. Correct trials only. Beep trials have a beep time. Methods reading (main): at least
  100 ms of baseline before the beep (Methods, Pupillometry and Neuronal Recordings: "minimum
  baseline duration of 100 ms"), and, as the evoked pupil is measured "following the onset of an
  auditory beep until 20 ms before the end of fixation" (Methods, Pupillometry), at least one 50
  ms window between the beep and 20 ms before the end of the trial (an implied requirement,
  stated here). Code reading (variant): beep more than 400 ms after the trial start and more than
  800 ms before the end of the pupil record (build_tables_from_nwb.m). Fixation-only trials are
  correct trials with no beep (the files hold no stimulation marker).
- Beep trials whose raw evoked firing rate, z-scored per unit over all of the unit's baseline,
  raw evoked and fixation-only rates, has absolute value 8 or more are dropped
  (build_tables_from_nwb.m; claims file).
- Pupil. The stored trace is used as is (the code does so). The notebook checks whether it
  already carries the Methods' preprocessing (z-scored per session, mean trace subtracted,
  smoothed).
- Baseline pupil: mean of the trace from the first sample of the trial to the beep (beep
  trials) or over the whole trial (fixation-only trials) (Methods, Pupillometry; the code takes
  the same samples).
- Evoked pupil. Methods: means in 50 ms windows slid in 10 ms steps from the beep to 20 ms
  before the end of fixation, minus the baseline; reading E1 takes the largest value, E2 the
  value of largest absolute size, sign kept (claims file). Code (variant, `C`): 0 to 800 ms
  after the beep, minus the baseline, a centred 50 sample moving mean (MATLAB movmean, which
  shrinks the window at the edges and omits NaN), the value of largest absolute size.
- Baseline firing rate: spikes from the trial start to the beep over that time (beep trials);
  fixation-only trials, from the trial start to 20 ms before its end (Methods, Neuronal
  Recordings), or to its end (code, variant).
- Evoked firing rate: rate from 0 to 200 ms after the beep, minus the trial's baseline rate
  (Methods, Neuronal Recordings; code).
- Drift residuals: per unit, the residuals of a linear regression of the baseline values on
  `trial_time_index` over its beep and fixation-only trials together (Results paragraph 2;
  Figure 1B legend; build_tables_from_nwb.m).
- The trial start is taken as fixation onset: the files give no other time, and the code
  measures every window from it.
"""

from __future__ import annotations

import io
import json
import urllib.request
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
from scipy import stats

DANDISET_ID = "002034"
DANDISET_VERSION = "0.261019.2146"
API = "https://api.dandiarchive.org/api"

CODE_REPO = "https://github.com/lwthompson2/Thompson2026_LCPupilAnalysis"
CODE_COMMIT = "cf3c0b70ccf17188f9094f130aa39aa0487ba7a6"
RAW = f"https://raw.githubusercontent.com/lwthompson2/Thompson2026_LCPupilAnalysis/{CODE_COMMIT}"
SESSION_LIST = f"{RAW}/Code/include_lists/manuscript_session_include.csv"
UNIT_LIST = f"{RAW}/Code/include_lists/manuscript_unit_include.csv"

MIN_BASELINE_MS = 100     # Methods, minimum baseline duration
END_MARGIN_MS = 20        # Methods, "until 20 ms before the end of fixation"
WIN_MS, STEP_MS = 50, 10  # Methods, evoked pupil windows
EVOKED_FR_MS = 200        # Methods, evoked firing rate window
CODE_PRE_MS, CODE_POST_MS = 400, 800   # build_tables_from_nwb.m, beep trial limits
CODE_PUPIL_MS = 800       # build_tables_from_nwb.m, evoked pupil window 0..800 ms
Z_MAX = 8                 # build_tables_from_nwb.m, |z| of raw evoked rate
LLR_CRIT = 3.841          # chi-square(1) at 0.05 (Results, paragraph 7)
ALPHA = 0.05              # Figure 2 legend
MONKEYS = ("Oz", "Cicero")
SHORT = {"Oz": "Oz", "Cicero": "Ci"}


# ----------------------------------------------------------------------------- loading

def _get_json(url):
    with urllib.request.urlopen(url, timeout=120) as r:
        return json.loads(r.read())


def list_assets():
    """All assets of the pinned version, with their S3 URLs."""
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/?page_size=200"
    out = []
    while url:
        page = _get_json(url)
        out += page["results"]
        url = page["next"]
    rows = []
    for a in out:
        meta = _get_json(f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/{a['asset_id']}/")
        s3 = [u for u in meta["contentUrl"] if "s3" in u][0]
        rows.append(dict(path=a["path"], size=a["size"], asset_id=a["asset_id"], url=s3))
    return pd.DataFrame(rows).sort_values("path").reset_index(drop=True)


def version_metadata():
    return _get_json(f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/")


def _str(x):
    x = x[()]
    return x.decode() if isinstance(x, bytes) else str(x)


def load_session(path, url):
    """One file: trial table, pupil matrix (trials x ms), units with spike times."""
    with h5py.File(remfile.File(url), "r") as h:
        tr = h["intervals/trials"]
        cols = [c.decode() if isinstance(c, bytes) else c for c in tr.attrs["colnames"]]
        trials = pd.DataFrame({c: tr[c][:] for c in cols})
        ps = h["acquisition/pupil_value_channel4"]
        flat = ps["data"][:]
        pupil_attrs = dict(unit=ps["data"].attrs.get("unit"), rate=ps["starting_time"].attrs.get("rate"),
                           description=ps.attrs.get("description"))
        n = len(trials)
        if flat.size % n:
            raise ValueError(f"{path}: pupil length {flat.size} is not a multiple of {n} trials")
        # The conversion flattened the [trial x time] matrix row by row (build_tables_from_nwb.m).
        pupil = flat.reshape(n, -1)
        un = h["units"]
        idx = un["spike_times_index"][:]
        st = un["spike_times"][:]
        starts = np.r_[0, idx[:-1]]
        units = []
        policies = [p.decode() if isinstance(p, bytes) else str(p) for p in un["spike_time_policy"][:]]
        for k, (a, b) in enumerate(zip(starts, idx)):
            units.append(dict(source_unit_index=int(un["source_unit_index"][k]), policy=policies[k],
                              spikes=st[a:b]))
        return dict(path=path, monkey=_str(h["general/subject/subject_id"]),
                    session=_str(h["general/session_id"]), trials=trials, pupil=pupil,
                    pupil_attrs=pupil_attrs, units=units, trial_columns=cols)


def load_all(assets, threads=8):
    with ThreadPoolExecutor(threads) as ex:
        return list(ex.map(lambda r: load_session(r.path, r.url), assets.itertuples()))


def include_lists():
    """The code's include lists (session_file has a .mat suffix; unit = source_unit_index - 1)."""
    def get(u):
        with urllib.request.urlopen(u, timeout=120) as r:
            return pd.read_csv(io.BytesIO(r.read()))
    return get(SESSION_LIST), get(UNIT_LIST)


# ----------------------------------------------------------------------------- measures

def _window_means(x, start, stop, width=WIN_MS, step=STEP_MS):
    """Means of x over [s, s+width) for s = start, start+step, ... with s+width <= stop."""
    out = []
    s = start
    while s + width <= stop:
        seg = x[s:s + width]
        out.append(np.nanmean(seg) if np.isfinite(seg).any() else np.nan)
        s += step
    return np.array(out, float)


def _movmean_omitnan(x, k=50):
    """MATLAB movmean(x, k, 'omitnan') for even k: window [i-k/2, i+k/2-1], shrunk at edges."""
    n = len(x)
    v = np.isfinite(x)
    cs = np.r_[0, np.cumsum(np.where(v, x, 0.0))]
    cn = np.r_[0, np.cumsum(v)]
    i = np.arange(n)
    lo = np.clip(i - k // 2, 0, n)
    hi = np.clip(i + k // 2, 0, n)   # exclusive: i + k/2 - 1 inclusive
    cnt = cn[hi] - cn[lo]
    with np.errstate(invalid="ignore", divide="ignore"):
        return np.where(cnt > 0, (cs[hi] - cs[lo]) / cnt, np.nan)


def _signed_absmax(v):
    v = v[np.isfinite(v)]
    if not v.size:
        return np.nan
    mx, mn = v.max(), v.min()
    return mx if abs(mx) > abs(mn) else mn


def pupil_trial_measures(sess):
    """Per trial: duration, beep, baseline pupil and the evoked pupil under E1, E2 and C."""
    t = sess["trials"]
    P = sess["pupil"]
    ncol = P.shape[1]
    dur = np.round((t.stop_time - t.start_time).values * 1000).astype(int)
    beep = t.beep_time_ms.values
    rows = []
    for i in range(len(t)):
        x = P[i]
        d = dur[i]
        r = dict(trial=i, dur_ms=d, beep_ms=beep[i], trial_time=t.trial_time_index.values[i],
                 correct=t.correct.values[i] == 1)
        if np.isfinite(beep[i]):
            b = int(round(beep[i]))
            seg = x[:b]
            r["pb"] = np.nanmean(seg) if np.isfinite(seg).any() else np.nan
            # Code's baseline: samples 1..round(beep)+1 in MATLAB, that is 0..b inclusive.
            seg = x[:min(ncol, b + 1)]
            r["pb_code"] = np.nanmean(seg) if np.isfinite(seg).any() else np.nan
            w = _window_means(x, b, d - END_MARGIN_MS)
            r["n_windows"] = int(np.isfinite(w).sum())
            dw = w - r["pb"]
            r["pe_E1"] = np.nanmax(dw) if np.isfinite(dw).any() else np.nan
            r["pe_E2"] = dw[np.nanargmax(np.abs(dw))] if np.isfinite(dw).any() else np.nan
            ev = np.arange(b, b + CODE_PUPIL_MS + 1)
            ev = ev[(ev >= 0) & (ev < ncol)]
            if ev.size and np.isfinite(r["pb_code"]):
                r["pe_C"] = _signed_absmax(_movmean_omitnan(x[ev] - r["pb_code"]))
            else:
                r["pe_C"] = np.nan
            r["methods_ok"] = (b >= MIN_BASELINE_MS) and r["n_windows"] > 0
            r["code_ok"] = (beep[i] > CODE_PRE_MS) and (beep[i] < ncol - CODE_POST_MS)
        else:
            seg = x[:min(ncol, d + 1)]
            r["pb"] = r["pb_code"] = np.nanmean(seg) if np.isfinite(seg).any() else np.nan
        rows.append(r)
    return pd.DataFrame(rows)


def unit_trial_rates(sess, unit, ptab):
    """Per trial firing rates of one unit: baseline (Methods and code windows) and raw evoked."""
    t = sess["trials"]
    sp = np.sort(unit["spikes"])
    start = t.start_time.values
    out = []
    for r in ptab.itertuples():
        a = start[r.trial]
        def count(lo, hi, closed=False):
            if closed:
                return np.searchsorted(sp, a + hi, "right") - np.searchsorted(sp, a + lo, "left")
            return np.searchsorted(sp, a + hi, "left") - np.searchsorted(sp, a + lo, "left")
        d = dict(trial=r.trial)
        if np.isfinite(r.beep_ms):
            bt = r.beep_ms / 1000
            d["sb"] = count(0, bt) / bt if bt > 0 else np.nan
            d["sb_code"] = d["sb"]
            d["se_raw"] = count(bt, bt + EVOKED_FR_MS / 1000, closed=True) / (EVOKED_FR_MS / 1000)
        else:
            T = r.dur_ms / 1000
            Tm = (r.dur_ms - END_MARGIN_MS) / 1000
            d["sb"] = count(0, Tm) / Tm if Tm > 0 else np.nan
            d["sb_code"] = count(0, T, closed=True) / T if T > 0 else np.nan
        out.append(d)
    return pd.DataFrame(out)


def build_tables(sessions, reading="methods", pupil_reading="E1"):
    """Beep-trial and fixation-trial tables over all units.

    reading 'methods': the Methods' trial rule, baseline and fixation windows (main);
    reading 'code': build_tables_from_nwb.m's trial rule and windows (variant).
    pupil_reading: 'E1', 'E2' (Methods) or 'C' (code's evoked pupil).
    """
    beeps, fixes = [], []
    for s in sessions:
        pt = pupil_trial_measures(s)
        is_beep = pt.correct & np.isfinite(pt.beep_ms)
        ok = pt["methods_ok" if reading == "methods" else "code_ok"].fillna(False).astype(bool)
        bsel = pt[is_beep & ok]
        fsel = pt[pt.correct & ~np.isfinite(pt.beep_ms)]
        pbcol = "pb" if reading == "methods" else "pb_code"
        for u in s["units"]:
            rates = unit_trial_rates(s, u, pt).set_index("trial")
            sbcol = "sb" if reading == "methods" else "sb_code"
            b = pd.DataFrame(dict(trial=bsel.trial.values, trial_time=bsel.trial_time.values,
                                  pb=bsel[pbcol].values, pe=bsel[f"pe_{pupil_reading}"].values,
                                  sb=rates.loc[bsel.trial, "sb"].values,
                                  se_raw=rates.loc[bsel.trial, "se_raw"].values))
            f = pd.DataFrame(dict(trial=fsel.trial.values, trial_time=fsel.trial_time.values,
                                  pb=fsel[pbcol].values, sb=rates.loc[fsel.trial, sbcol].values))
            # z-score exclusion (build_tables_from_nwb.m): over baseline, raw evoked and fixation rates.
            allfr = np.r_[b.sb.values, b.se_raw.values, f.sb.values]
            v = np.isfinite(allfr)
            z = np.full(allfr.size, np.nan)
            if v.sum() > 1:
                z[v] = (allfr[v] - allfr[v].mean()) / allfr[v].std(ddof=1)
            ez = z[len(b):2 * len(b)]
            b["z_evoked_raw"] = ez
            keep = (np.isfinite(b.sb) & np.isfinite(b.pb) & np.isfinite(b.pe) & np.isfinite(ez)
                    & (np.abs(ez) < Z_MAX))
            b["dropped_z"] = np.isfinite(ez) & (np.abs(ez) >= Z_MAX)
            nb_all = len(b)
            b = b[keep].copy()
            f = f[np.isfinite(f.sb) & np.isfinite(f.pb)].copy()
            b["se"] = b.se_raw - b.sb
            key = f"{s['monkey']}|{s['session']}|{u['source_unit_index'] - 1}"
            for df, kind in ((b, "beep"), (f, "fix")):
                df["monkey"] = s["monkey"]
                df["session"] = s["session"]
                df["unit"] = u["source_unit_index"] - 1
                df["unit_key"] = key
                df["kind"] = kind
            b["n_beep_candidates"] = nb_all
            beeps.append(b)
            fixes.append(f)
    B = pd.concat(beeps, ignore_index=True)
    F = pd.concat(fixes, ignore_index=True)
    add_residuals(B, F)
    return B, F


def add_residuals(B, F, pcol="pb", scol="sb"):
    """Per unit, residuals of baseline pupil and rate regressed on trial time (beep + fixation)."""
    B["pb_res"] = np.nan
    B["sb_res"] = np.nan
    F["pb_res"] = np.nan
    F["sb_res"] = np.nan
    for key in B.unit_key.unique():
        ib = (B.unit_key == key).values
        jf = (F.unit_key == key).values
        tt = np.r_[B.trial_time.values[ib], F.trial_time.values[jf]]
        for col, rc in ((pcol, "pb_res"), (scol, "sb_res")):
            y = np.r_[B[col].values[ib], F[col].values[jf]]
            if len(y) < 2:
                continue
            slope, icpt = np.polyfit(tt, y, 1)
            res = y - (icpt + slope * tt)
            B.loc[ib, rc] = res[:ib.sum()]
            F.loc[jf, rc] = res[ib.sum():]


def unit_order(B):
    """The code's unit order (compute_data.m): Oz first, then by session file and unit."""
    keys = B[["monkey", "session", "unit", "unit_key"]].drop_duplicates()
    keys["mo"] = keys.monkey.map({"Oz": 1, "Cicero": 2})
    keys["sf"] = keys.session + ".mat"
    keys = keys.sort_values(["mo", "sf", "unit"]).reset_index(drop=True)
    keys["legacy_row"] = np.arange(1, len(keys) + 1)
    return keys


def code_removed_units(B):
    """Units the code drops as rows 43 and 65 of its per-unit stats table (build_stats)."""
    k = unit_order(B)
    return list(k.loc[k.legacy_row.isin([43, 65]), "unit_key"])


def session_rows(B):
    """Beep trials of each session once: the first unit's row of each trial (compute_manuscript_stats.m)."""
    k = unit_order(B)
    order = dict(zip(k.unit_key, k.legacy_row))
    X = B.assign(_o=B.unit_key.map(order)).sort_values(["_o", "trial"], kind="stable")
    return X.drop_duplicates(["session", "trial"]).drop(columns="_o")


# ----------------------------------------------------------------------------- statistics

def spearman(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    v = np.isfinite(x) & np.isfinite(y)
    if v.sum() < 3:
        return np.nan, np.nan
    r = stats.spearmanr(x[v], y[v])
    return float(r.statistic), float(r.pvalue)


def partial_spearman(x, y, z):
    """Spearman partial correlation of x and y given z, as MATLAB partialcorr(..., 'Type', 'Spearman').

    Ranks each variable, takes the Pearson partial correlation of the ranks, and a t test on
    n - 3 degrees of freedom.
    """
    x, y, z = (np.asarray(a, float) for a in (x, y, z))
    v = np.isfinite(x) & np.isfinite(y) & np.isfinite(z)
    n = int(v.sum())
    if n < 4:
        return np.nan, np.nan
    rx, ry, rz = (stats.rankdata(a[v]) for a in (x, y, z))
    Z = np.c_[np.ones(n), rz]
    ex = rx - Z @ np.linalg.lstsq(Z, rx, rcond=None)[0]
    ey = ry - Z @ np.linalg.lstsq(Z, ry, rcond=None)[0]
    r = float(np.sum(ex * ey) / np.sqrt(np.sum(ex ** 2) * np.sum(ey ** 2)))
    df = n - 3
    t = r * np.sqrt(df / max(1e-300, 1 - r ** 2))
    return r, float(2 * stats.t.sf(abs(t), df))


def signrank(vals):
    """T1: Wilcoxon signed-rank test of median = 0, two-sided.

    MATLAB's signrank (the code's test) uses the normal approximation with a tie correction and
    no continuity correction for n > 15; that is scipy's method='approx', correction=False.
    """
    v = np.asarray(vals, float)
    v = v[np.isfinite(v)]
    return float(stats.wilcoxon(v, method="approx", correction=False, zero_method="wilcox").pvalue)


def ranksum_vs_zero(vals):
    """T2 (variant): Wilcoxon rank-sum of the coefficients against as many zeros."""
    v = np.asarray(vals, float)
    v = v[np.isfinite(v)]
    return float(stats.ranksums(v, np.zeros_like(v)).pvalue)


def llr_quadratic(x, y):
    """2 x (log-likelihood of y ~ x + x^2 minus that of y ~ x), Gaussian maximum likelihood.

    As fitlme(y ~ x) against fitlme(y ~ x*x) without random effects, fit by ML (the default),
    in compute_manuscript_stats.m. Needs 4 valid points and 3 distinct x values, as the code.
    """
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    v = np.isfinite(x) & np.isfinite(y)
    x, y = x[v], y[v]
    n = len(x)
    if n < 4 or len(np.unique(x)) < 3:
        return np.nan
    def rss(X):
        beta = np.linalg.lstsq(X, y, rcond=None)[0]
        return float(np.sum((y - X @ beta) ** 2))
    r1 = rss(np.c_[np.ones(n), x])
    r2 = rss(np.c_[np.ones(n), x, x ** 2])
    if r2 <= 0:
        return np.inf
    return float(n * np.log(r1 / r2))


# ----------------------------------------------------------------------------- Figure 2

ROWS = {
    1: "baseline LC vs baseline pupil (partial Spearman, given trial time)",
    2: "evoked LC vs evoked pupil",
    3: "evoked pupil vs baseline pupil residual (per session)",
    4: "evoked LC vs baseline LC residual",
    5: "evoked pupil vs baseline LC residual",
    6: "evoked LC vs baseline pupil residual",
}


def figure2_coefficients(B, F, baseline="residual"):
    """Per unit (rows 1, 2, 4, 5, 6) and per session (row 3) coefficients.

    baseline='residual' uses drift residuals (Figure 2); 'raw' uses the raw baselines
    (Supplemental Figure 1; row 1 stays the partial correlation given trial time).
    """
    pcol, scol = ("pb_res", "sb_res") if baseline == "residual" else ("pb", "sb")
    out = []
    for key, b in B.groupby("unit_key", sort=False):
        f = F[F.unit_key == key]
        m = b.monkey.iloc[0]
        r1 = partial_spearman(np.r_[b.sb, f.sb], np.r_[b.pb, f.pb], np.r_[b.trial_time, f.trial_time])
        rows = {1: r1, 2: spearman(b.pe, b.se), 4: spearman(b[scol], b.se),
                5: spearman(b[scol], b.pe), 6: spearman(b[pcol], b.se)}
        for k, (r, p) in rows.items():
            out.append(dict(row=k, monkey=m, session=b.session.iloc[0], unit_key=key, r=r, p=p,
                            n=len(b) + (len(f) if k == 1 else 0)))
    S = session_rows(B)
    for sess, b in S.groupby("session", sort=False):
        r, p = spearman(b[pcol], b.pe)
        out.append(dict(row=3, monkey=b.monkey.iloc[0], session=sess, unit_key=None, r=r, p=p, n=len(b)))
    return pd.DataFrame(out)


def population_tests(C, removed_units=(), removed_sessions=()):
    """Per row and monkey: n, median, T1 (signed rank) and T2 (rank sum against zeros)."""
    out = []
    for (row, m), g in C.groupby(["row", "monkey"]):
        if row == 3:
            g = g[~g.session.isin(removed_sessions)]
        else:
            g = g[~g.unit_key.isin(removed_units)]
        v = g.r.values[np.isfinite(g.r.values)]
        out.append(dict(row=row, monkey=SHORT[m], n=len(v), median=float(np.median(v)),
                        p_T1=signrank(v), p_T2=ranksum_vs_zero(v),
                        n_sig_pos=int(((g.p < ALPHA) & (g.r > 0)).sum()),
                        n_sig_neg=int(((g.p < ALPHA) & (g.r < 0)).sum())))
    return pd.DataFrame(out)


def zscore_rates(B, F, group="unit_key"):
    """Firing rates z-scored per group over [baseline, raw evoked, fixation] (zscore_tables.m).

    The evoked rate becomes z(raw evoked) - z(baseline). group='unit_key' is per unit (main);
    group='unit' reproduces the code, which groups by the within-session unit index.
    """
    B = B.copy()
    F = F.copy()
    for g in B[group].unique():
        ib = (B[group] == g).values
        jf = (F[group] == g).values
        allfr = np.r_[B.sb.values[ib], B.se_raw.values[ib], F.sb.values[jf]]
        mu, sd = np.nanmean(allfr), np.nanstd(allfr, ddof=1)
        zb = (B.sb.values[ib] - mu) / sd
        ze = (B.se_raw.values[ib] - mu) / sd
        B.loc[ib, "sb"] = zb
        B.loc[ib, "se_raw"] = ze
        B.loc[ib, "se"] = ze - zb
        F.loc[jf, "sb"] = (F.sb.values[jf] - mu) / sd
    add_residuals(B, F)
    return B, F


# ----------------------------------------------------------------------------- further analyses

def range_correlations(B, C):
    """Across units, per monkey: Spearman of the row 6 coefficient with the unit's range of evoked
    rates, and of the row 5 coefficient with its range of evoked pupil (compute_manuscript_stats.m,
    build_evoked_range_by_unit)."""
    out = []
    for m in MONKEYS:
        g = B[B.monkey == m].groupby("unit_key")
        rng_se = g.se.agg(lambda v: v.max() - v.min())
        rng_pe = g.pe.agg(lambda v: v.max() - v.min())
        for row, rng, what in ((6, rng_se, "row 6 vs evoked LC range"), (5, rng_pe, "row 5 vs evoked pupil range")):
            c = C[(C.row == row) & (C.monkey == m)].set_index("unit_key").r
            r, p = spearman(rng.loc[c.index], c)
            out.append(dict(monkey=SHORT[m], analysis=what, n=len(c), rho=r, p=p))
    return pd.DataFrame(out)


LLR_PAIRS = {
    "pupil": ("pb_res", "pe"),        # evoked pupil on baseline pupil residual, per session
    "lc": ("sb_res", "se"),           # evoked rate on baseline rate residual, per unit
    "pupil_on_lc": ("sb_res", "pe"),  # evoked pupil on baseline rate residual, per unit
    "lc_on_pupil": ("pb_res", "se"),  # evoked rate on baseline pupil residual, per unit
}


def llr_counts(B, removed_units=(), removed_sessions=()):
    """Counts of LLR > 3.841, per monkey and comparison, over sessions (pupil) or units."""
    out = []
    S = session_rows(B)
    for m in MONKEYS:
        for name, (x, y) in LLR_PAIRS.items():
            if name == "pupil":
                groups = [(k, b) for k, b in S[S.monkey == m].groupby("session") if k not in removed_sessions]
            else:
                groups = [(k, b) for k, b in B[B.monkey == m].groupby("unit_key") if k not in removed_units]
            v = np.array([llr_quadratic(b[x], b[y]) for _, b in groups])
            out.append(dict(monkey=SHORT[m], comparison=name, n_above=int(np.sum(v > LLR_CRIT)),
                            n=int(np.isfinite(v).sum()), n_groups=len(v),
                            max_llr=float(np.nanmax(v)) if np.isfinite(v).any() else np.nan))
    return pd.DataFrame(out)


FIG3_COLUMNS = {
    1: "baseline LC residual vs baseline pupil residual (beep + fixation trials)",
    2: "evoked LC vs evoked pupil",
    3: "evoked pupil vs baseline pupil residual (each session trial once)",
    4: "evoked LC vs baseline LC residual",
    5: "baseline LC residual vs evoked pupil",
    6: "evoked LC vs baseline pupil residual",
}


def fig3_pooled(B, F, C, group="unit_key"):
    """Figure 3: rates z-scored (zscore_rates), residuals recomputed, Spearman over pooled trials
    per monkey; columns 5 and 6 also within the units whose row 1 partial correlation is
    significant (p < 0.05) and positive, or negative (Figure 3 legend)."""
    Bz, Fz = zscore_rates(B, F, group)
    r1 = C[C.row == 1].set_index("unit_key")
    groups = {"positive": set(r1.index[(r1.p < ALPHA) & (r1.r > 0)]),
              "negative": set(r1.index[(r1.p < ALPHA) & (r1.r < 0)])}
    out = []
    for m in MONKEYS:
        b = Bz[Bz.monkey == m]
        f = Fz[Fz.monkey == m]
        s = session_rows(b)
        cols = {1: (np.r_[b.sb_res, f.sb_res], np.r_[b.pb_res, f.pb_res]), 2: (b.se, b.pe),
                3: (s.pb_res, s.pe), 4: (b.sb_res, b.se), 5: (b.sb_res, b.pe), 6: (b.pb_res, b.se)}
        for k, (x, y) in cols.items():
            r, p = spearman(x, y)
            out.append(dict(monkey=SHORT[m], group="all", n_units=b.unit_key.nunique(), column=k,
                            n=int(np.isfinite(np.asarray(x, float)).sum()), rho=r, p=p))
        for gname, keys in groups.items():
            bb = b[b.unit_key.isin(keys)]
            for k, (x, y) in {5: ("sb_res", "pe"), 6: ("pb_res", "se")}.items():
                r, p = spearman(bb[x], bb[y])
                out.append(dict(monkey=SHORT[m], group=gname, n_units=bb.unit_key.nunique(), column=k,
                                n=len(bb), rho=r, p=p))
    return pd.DataFrame(out)


def clock_check(sessions, shift_ms=-600):
    """Per session, the LC and pupil response to the beep, at the true beep times and at times
    shifted by `shift_ms` (still inside the trial).

    LC: rate 0-200 ms after the time minus rate 200 ms before it. Pupil: mean 300-800 ms after
    minus mean 100 ms before. Only beep trials with the beep at least 800 ms after the trial start
    and 800 ms before its end, so both times have the same windows. Returns per session the mean
    response and a one-sided Wilcoxon signed-rank p for each.
    """
    rows = []
    for s in sessions:
        t = s["trials"]
        P = s["pupil"]
        dur = (t.stop_time - t.start_time).values * 1000
        bt = t.beep_time_ms.values
        sel = np.where(np.isfinite(bt) & (bt >= 800) & (bt + 800 <= dur))[0]
        if len(sel) < 6:
            rows.append(dict(session=s["session"], monkey=SHORT[s["monkey"]], n=len(sel)))
            continue
        r = dict(session=s["session"], monkey=SHORT[s["monkey"]], n=len(sel))
        for lab, off in (("true", 0), ("shifted", shift_ms)):
            tt = bt[sel] + off
            pu = np.array([np.nanmean(P[i, int(a) + 300:int(a) + 800]) - np.nanmean(P[i, int(a) - 100:int(a)])
                           for i, a in zip(sel, tt)])
            lc = []
            for u in s["units"]:
                sp = np.sort(u["spikes"])
                a0 = t.start_time.values[sel] + tt / 1000
                post = np.searchsorted(sp, a0 + 0.2) - np.searchsorted(sp, a0)
                pre = np.searchsorted(sp, a0) - np.searchsorted(sp, a0 - 0.2)
                lc.append((post - pre) / 0.2)
            lc = np.mean(lc, axis=0)
            r[f"lc_{lab}"] = float(np.mean(lc))
            r[f"pupil_{lab}"] = float(np.nanmean(pu))
            r[f"p_lc_{lab}"] = float(stats.wilcoxon(lc, alternative="greater").pvalue) if np.any(lc != 0) else 1.0
            pv = pu[np.isfinite(pu)]
            r[f"p_pupil_{lab}"] = float(stats.wilcoxon(pv, alternative="greater").pvalue) if len(pv) > 5 else np.nan
        rows.append(r)
    return pd.DataFrame(rows)


def pupil_preprocessing_check(sessions):
    """Per session: mean and SD of all stored samples, the largest absolute value of the mean
    trace across trials over the first second, and how much a 151 ms boxcar changes the trace
    (SD of the difference over SD of the trace), as checks of the Methods' preprocessing."""
    from scipy.ndimage import uniform_filter1d
    rows = []
    for s in sessions:
        P = s["pupil"]
        v = P[np.isfinite(P)]
        mt = np.nanmean(P[:, :1000], axis=0)
        ch = []
        for x in P:
            x = x[np.isfinite(x)]
            if len(x) > 400:
                ch.append(np.std(x - uniform_filter1d(x, 151, mode="nearest")) / np.std(x)
                          if np.std(x) > 0 else np.nan)
        rows.append(dict(session=s["session"], monkey=SHORT[s["monkey"]], mean=v.mean(), sd=v.std(),
                         mean_trace_absmax=float(np.nanmax(np.abs(mt))),
                         boxcar_change=float(np.nanmedian(ch)) if ch else np.nan))
    return pd.DataFrame(rows)


def code_stats_text():
    """The printed output of the paper's code on this dandiset (Code/Results/manuscript_stats_nwb.txt)."""
    with urllib.request.urlopen(f"{RAW}/Code/Results/manuscript_stats_nwb.txt", timeout=120) as r:
        return r.read().decode()
