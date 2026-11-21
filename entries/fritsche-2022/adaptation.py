"""Loading and adaptation measures for Fritsche, Solomon & de Lange (2022) on DANDI:000021.

The paper is "Brief Stimuli Cast a Persistent Long-Term Trace in Visual Cortex", J Neurosci
42(10):1999-2010, doi:10.1523/JNEUROSCI.1350-21.2021. The claims file is
claims/fritsche-2022.yaml; its header names the open details O1 to O6 used below.

Where each parameter comes from:

- Unit quality: ISI violations <= 0.5, amplitude cutoff <= 0.1, presence ratio >= 0.9 (Methods,
  "Unit exclusion", the AllenSDK defaults).
- Response windows: 0 to 100 ms from onset for drifting gratings, 0 to 250 ms for static
  gratings, and 0 to 100 ms for static gratings as a variant (Methods, "Unit exclusion" and
  "Orientation-specific adaptation to static gratings").
- Responsiveness: rate to the preferred orientation over 5 Hz (2.5 and 10 Hz as variants) and
  over 1 SD of the gray-screen rate in the same window (Methods, "Unit exclusion"). The readings
  of O4 are all computed (`responsive`).
- Regions kept: at least 50 responsive units (Methods, "Unit exclusion").
- Repeat is the same orientation (direction modulo 180 for drifting gratings), orthogonal is 90
  degrees apart, temporal frequency, spatial frequency and phase are ignored (Methods,
  "Orientation-specific adaptation to drifting gratings").
- The readings of O1 (ratio per unit) and O3 (how blanks and blocks enter the n-back sequence)
  are all computed (`nback_rates`, `ratios`).
- Exponential models and their bounds: Methods, equations 2 and 3 and the paragraph after them;
  the sign of the second term is O5, both readings are fitted (`fit_models`).
- Rates are spike counts divided by the window length (a standard choice; it cannot change a
  ratio).
"""
from __future__ import annotations

import json
import warnings
import urllib.request
from concurrent.futures import ProcessPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
from scipy import optimize, stats

DANDISET = "000021"
VERSION = "0.251116.2246"
API = "https://api.dandiarchive.org/api"

# Allen CCF acronyms of the regions the paper names (Figure 1 legend: V1, LM, AL, RL, PM, AM; LGN
# is the dorsolateral geniculate, LGd; LP).
AREA_NAMES = {"VISp": "V1", "VISl": "LM", "VISal": "AL", "VISrl": "RL", "VISpm": "PM",
              "VISam": "AM", "LGd": "LGN", "LP": "LP"}
CORTEX = ["V1", "LM", "AL", "RL", "PM", "AM"]
THALAMUS = ["LGN", "LP"]

DG_WIN = 0.1      # drifting gratings, 0 to 100 ms (Methods)
SG_WIN = 0.25     # static gratings, 0 to 250 ms (Methods)
SG_WIN_SHORT = 0.1


def session_assets():
    """The 32 session files (not the per-probe LFP files) of the pinned version."""
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=400"
    out = []
    while url:
        d = json.load(urllib.request.urlopen(url))
        out += d["results"]
        url = d["next"]
    return sorted([a for a in out if "_probe-" not in a["path"]], key=lambda a: a["path"])


def s3_url(asset_id):
    d = json.load(urllib.request.urlopen(
        f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/{asset_id}/"))
    return [u for u in d["contentUrl"] if "s3" in u][0]


def _counts(spk, starts, width):
    return (np.searchsorted(spk, starts + width) - np.searchsorted(spk, starts)).astype(np.int32)


def _bins(intervals, width):
    """Start times of consecutive bins of `width` s inside each interval."""
    out = [np.arange(a, b - width, width) for a, b in intervals]
    return np.concatenate(out) if out else np.zeros(0)


def load_session(path_and_id):
    """Stream one session file and reduce it to spike counts per unit and presentation.

    Returns a dict with the unit table (quality metrics, area), the drifting and static grating
    tables, the spontaneous epochs, and count matrices (units x presentations). Every unit in the
    file is described; counts are computed for units that pass the quality metrics.
    """
    path, asset_id = path_and_id
    url = s3_url(asset_id)
    rf = remfile.File(url, _max_cache_size=150_000_000, _max_threads=4)
    with h5py.File(rf, "r") as f:
        u = f["units"]
        units = pd.DataFrame({k: u[k][:] for k in [
            "id", "isi_violations", "amplitude_cutoff", "presence_ratio", "peak_channel_id",
            "firing_rate", "quality"]})
        units["quality"] = units["quality"].astype(str)
        idx = u["spike_times_index"][:]
        e = f["general/extracellular_ephys/electrodes"]
        loc = pd.Series(e["location"][:].astype(str), index=e["id"][:])
        units["location"] = loc.reindex(units.peak_channel_id).values
        units["area"] = units["location"].map(AREA_NAMES)
        units["passes_quality"] = ((units.isi_violations <= 0.5) & (units.amplitude_cutoff <= 0.1)
                                   & (units.presence_ratio >= 0.9))

        def table(name, cols):
            g = f[f"intervals/{name}"]
            return pd.DataFrame({c: g[c][:] for c in cols})
        dg = table("drifting_gratings_presentations", [
            "id", "start_time", "stop_time", "orientation", "temporal_frequency",
            "stimulus_block", "contrast"])
        sg = table("static_gratings_presentations", [
            "id", "start_time", "stop_time", "orientation", "spatial_frequency", "phase",
            "stimulus_block"])
        sg["phase"] = pd.to_numeric(sg["phase"].astype(str), errors="coerce")
        sp = table("spontaneous_presentations", ["start_time", "stop_time"])
        inv = (table("invalid_times", ["start_time", "stop_time"])
               if "invalid_times" in f["intervals"] else pd.DataFrame())
        meta = {k: f[f"general/subject/{k}"][()].decode() for k in
                ["subject_id", "genotype", "sex", "age"]}
        meta["session_id"] = f["general/session_id"][()].decode()
        meta["path"] = path

        sel = np.flatnonzero(units.passes_quality.values)
        starts = np.r_[0, idx[:-1]]
        sp_iv = list(zip(sp.start_time, sp.stop_time))
        bins100 = _bins(sp_iv, DG_WIN)
        bins250 = _bins(sp_iv, SG_WIN)
        n = len(sel)
        dg_c = np.zeros((n, len(dg)), np.int32)
        dg_pre = np.zeros((n, len(dg)), np.int32)
        sg_c = np.zeros((n, len(sg)), np.int32)
        sg_c100 = np.zeros((n, len(sg)), np.int32)
        sp100 = np.zeros((n, len(bins100)), np.int32)
        sp250 = np.zeros((n, len(bins250)), np.int32)
        st = u["spike_times"]
        # Read runs of consecutive selected units in one request each (at most 15M spikes).
        i = 0
        while i < n:
            j = i
            while (j + 1 < n and sel[j + 1] == sel[j] + 1
                   and idx[sel[j + 1]] - starts[sel[i]] < 15_000_000):
                j += 1
            a, b = starts[sel[i]], idx[sel[j]]
            block = st[a:b]
            for k in range(i, j + 1):
                s = block[starts[sel[k]] - a: idx[sel[k]] - a]
                dg_c[k] = _counts(s, dg.start_time.values, DG_WIN)
                dg_pre[k] = _counts(s, dg.start_time.values - DG_WIN, DG_WIN)
                sg_c[k] = _counts(s, sg.start_time.values, SG_WIN)
                sg_c100[k] = _counts(s, sg.start_time.values, SG_WIN_SHORT)
                sp100[k] = _counts(s, bins100, DG_WIN)
                sp250[k] = _counts(s, bins250, SG_WIN)
            i = j + 1
    return dict(meta=meta, units=units, sel=sel, dg=dg, sg=sg, spont=sp, invalid=inv,
                dg_counts=dg_c, dg_pre=dg_pre, sg_counts=sg_c, sg_counts100=sg_c100,
                sp100=sp100, sp250=sp250)


def load_all(assets, workers=4):
    items = [(a["path"], a["asset_id"]) for a in assets]
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(load_session, items))


# ---------------------------------------------------------------------------------------------
# Trial sequences


def sequence(table, kind, blanks="hold", blocks="within"):
    """The presentation sequence used to form n-back pairs (O3).

    Returns (ori, blk, keep): the orientation modulo 180 (NaN for blanks), the block of each
    position, and the indices into `table` of the positions. blanks="hold" keeps blank trials as
    positions (O3a), "remove" drops them first (O3b); blocks="within" forms pairs within each
    stimulus block (O3c), "across" over the concatenated sequence (O3d).
    """
    t = table.sort_values("start_time")
    order = t.index.values
    ori = np.mod(t["orientation"].values, 180.0)
    blk = t["stimulus_block"].values.copy()
    if blanks == "remove":
        ok = ~np.isnan(ori)
        order, ori, blk = order[ok], ori[ok], blk[ok]
    if blocks == "across":
        blk = np.zeros_like(blk)
    return ori, blk, order


def pair_masks(ori, blk, n):
    """Masks over current positions i (with i-n valid) for repeat and orthogonal at n-back."""
    cur = ori[n:]
    prev = ori[:-n]
    same_blk = blk[n:] == blk[:-n]
    valid = same_blk & ~np.isnan(cur) & ~np.isnan(prev)
    d = np.abs(cur - prev)
    d = np.minimum(d, 180 - d)
    rep = valid & (d < 1e-6)
    orth = valid & (np.abs(d - 90) < 1e-6)
    blank_prev = same_blk & ~np.isnan(cur) & np.isnan(prev)
    return rep, orth, blank_prev


def nback_rates(counts, table, n_max=50, blanks="hold", blocks="within", win=DG_WIN, valid=None):
    """Per unit, n and current orientation: summed counts and trial numbers for repeat and
    orthogonal pairs. Returns arrays (units x n_max x n_ori) of rep_sum, rep_n, orth_sum, orth_n
    and the orientation list. `valid` (one flag per row of `table`) leaves out current trials
    whose response is not to be used; they still count as the n-back stimulus."""
    ori, blk, order = sequence(table, None, blanks, blocks)
    c = counts[:, order].astype(float)
    ok_cur = np.ones(len(order), bool) if valid is None else np.asarray(valid)[order]
    oris = np.unique(ori[~np.isnan(ori)])
    U = c.shape[0]
    out = {k: np.zeros((U, n_max, len(oris))) for k in ["rs", "rn", "os", "on"]}
    for n in range(1, n_max + 1):
        rep, orth, _ = pair_masks(ori, blk, n)
        rep, orth = rep & ok_cur[n:], orth & ok_cur[n:]
        cur_ori = ori[n:]
        cc = c[:, n:]
        for j, o in enumerate(oris):
            m = cur_ori == o
            out["rs"][:, n - 1, j] = cc[:, rep & m].sum(1)
            out["rn"][:, n - 1, j] = (rep & m).sum()
            out["os"][:, n - 1, j] = cc[:, orth & m].sum(1)
            out["on"][:, n - 1, j] = (orth & m).sum()
    return out, oris


def ratios(nb, how="pooled"):
    """Adaptation ratio per unit and n (O1). how="pooled": mean rate over all repeat trials over
    mean over all orthogonal trials (O1a); "per_ori": ratio per current orientation, averaged
    arithmetically (O1b); "per_ori_geo": geometric mean over orientations (O1b, geometric)."""
    if how == "pooled":
        r = nb["rs"].sum(2) / nb["rn"].sum(2)
        o = nb["os"].sum(2) / nb["on"].sum(2)
        with np.errstate(divide="ignore", invalid="ignore"):
            return r / o
    with np.errstate(divide="ignore", invalid="ignore"):
        rr = (nb["rs"] / nb["rn"]) / (nb["os"] / nb["on"])
    if how == "per_ori":
        rr = np.where(np.isfinite(rr), rr, np.nan)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", RuntimeWarning)
            return np.nanmean(rr, 2)
    with np.errstate(divide="ignore", invalid="ignore"):
        lr = np.log(rr)
    lr = np.where(np.isfinite(lr), lr, np.nan)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", RuntimeWarning)
        return np.exp(np.nanmean(lr, 2))


def region_value(ar, how="geo"):
    """Region ratio from unit ratios (O2): "geo" exp(mean log ratio) (O2a), "mean" (O2b).
    Units with a non-finite or zero ratio are left out (counted by `finite_log`)."""
    with np.errstate(divide="ignore", invalid="ignore"):
        lr = np.log(ar)
    ok = np.isfinite(lr)
    if how == "geo":
        return float(np.exp(lr[ok].mean()))
    return float(ar[ok].mean())


def ttest_log(ar):
    """Two-tailed one-sample t test of unit log ratios against zero (Methods)."""
    with np.errstate(divide="ignore", invalid="ignore"):
        lr = np.log(ar)
    lr = lr[np.isfinite(lr)]
    t, p = stats.ttest_1samp(lr, 0.0)
    return float(t), float(p), int(lr.size)


def fdr(p, alpha=0.05):
    """Benjamini-Hochberg (Methods). Returns adjusted p values and the rejections."""
    p = np.asarray(p, float)
    m = p.size
    o = np.argsort(p)
    adj = np.empty(m)
    adj[o] = np.minimum.accumulate((p[o] * m / np.arange(1, m + 1))[::-1])[::-1]
    adj = np.minimum(adj, 1)
    return adj, adj < alpha


# ---------------------------------------------------------------------------------------------
# Exponential decay models (Methods, equations 2 and 3)


def model_double(n, af, tf, as_, ts, sign=-1):
    """Double exponential. sign=-1: both terms reduce the response (O5a, as Tables 1 and 2 give
    both amplitudes as response reductions); sign=+1: as printed (O5b)."""
    return 1 - af * np.exp(-(n - 1) / tf) + sign * as_ * np.exp(-(n - 1) / ts)


def model_single(n, a, t):
    return 1 - a * np.exp(-(n - 1) / t)


# Bounds of the Methods: a <= 0.5 (lower -Inf), tau in [-50, 50]. A tau of exactly 0 is
# undefined; the fits start from positive values.
B_D = ([-np.inf, -50, -np.inf, -50], [0.5, 50, 0.5, 50])
B_S = ([-np.inf, -50], [0.5, 50])
STARTS_D = [(0.15, 0.8, 0.04, 6.0), (0.1, 0.3, 0.05, 3.0), (0.1, 1.5, 0.02, 15.0),
            (0.05, 0.1, 0.05, 25.0)]
STARTS_S = [(0.1, 0.5), (0.1, 2.0), (0.05, 5.0)]


def _fit(fun, n, y, starts, bounds):
    best = None
    for p0 in starts:
        try:
            with np.errstate(all="ignore"):
                p, _ = optimize.curve_fit(lambda x, *q: np.log(np.clip(fun(x, *q), 1e-9, None)),
                                          n, y, p0=p0, bounds=bounds, maxfev=20000)
        except (RuntimeError, ValueError):
            continue
        rss = float(np.sum((y - np.log(np.clip(fun(n, *p), 1e-9, None))) ** 2))
        if best is None or rss < best[1]:
            best = (p, rss)
    return best


def on_bound(p, bounds, tol=1e-3):
    lo, hi = np.asarray(bounds[0]), np.asarray(bounds[1])
    return bool(np.any(np.isfinite(lo) & (np.abs(p - lo) < tol)) or
                np.any(np.abs(p - hi) < tol))


def fit_models(mean_log, sign=-1):
    """Least-squares fits to the region's mean log ratio at n = 1 to len(mean_log) (O5a; the
    unit-level fit O5b has the same estimates when every unit has every n)."""
    n = np.arange(1, len(mean_log) + 1, dtype=float)
    d = _fit(lambda x, *q: model_double(x, *q, sign=sign), n, mean_log, STARTS_D, B_D)
    s = _fit(model_single, n, mean_log, STARTS_S, B_S)
    return d, s


def ftest(rss_s, rss_d, n_obs, k_s=2, k_d=4):
    """F test of nested models (Methods)."""
    df1, df2 = k_d - k_s, n_obs - k_d
    if rss_d <= 0:
        return np.inf, 0.0
    F = ((rss_s - rss_d) / df1) / (rss_d / df2)
    return float(F), float(stats.f.sf(F, df1, df2))


# ---------------------------------------------------------------------------------------------
# Responsiveness (Methods, "Unit exclusion"; readings O4)


def preferred(counts, table, win, by="orientation"):
    """Preferred orientation and its mean rate. by="orientation": orientation (modulo 180) with
    the highest mean rate over all its trials (O4e); by="condition": the single stimulus
    condition with the highest mean rate (O4f; direction and temporal frequency for drifting
    gratings, orientation, spatial frequency and phase for static gratings), and its
    orientation. Returns (pref_ori, pref_rate, rate_by_ori, oris)."""
    ori = np.mod(table["orientation"].values, 180.0)
    ok = ~np.isnan(ori)
    rate = counts[:, ok] / win
    o = ori[ok]
    oris = np.unique(o)
    by_ori = np.stack([rate[:, o == x].mean(1) for x in oris], 1)
    if by == "orientation":
        k = by_ori.argmax(1)
        return oris[k], by_ori[np.arange(len(k)), k], by_ori, oris
    if "temporal_frequency" in table:
        keys = table.loc[ok, ["orientation", "temporal_frequency"]].astype(str).agg("|".join, 1)
    else:
        keys = table.loc[ok, ["orientation", "spatial_frequency", "phase"]].astype(str).agg(
            "|".join, 1)
    codes, uniq = pd.factorize(keys)
    cond_rate = np.stack([rate[:, codes == c].mean(1) for c in range(len(uniq))], 1)
    k = cond_rate.argmax(1)
    cond_ori = np.array([o[codes == c][0] for c in range(len(uniq))])
    return cond_ori[k], cond_rate[np.arange(len(k)), k], by_ori, oris


def gray_stats(counts, table, spont_counts, win, source="blank"):
    """Mean and SD of the gray-screen rate in the response window: source="blank" from the blank
    presentations of the same stimulus set (O4c), "spont" from consecutive bins of the
    spontaneous epochs (O4d)."""
    if source == "blank":
        g = counts[:, np.isnan(table["orientation"].values)] / win
    else:
        g = spont_counts / win
    return g.mean(1), g.std(1, ddof=1)


def responsive(pref_rate, gray_mean, gray_sd, threshold=5.0, rule="mean_plus_sd"):
    """Rate over `threshold` Hz and over 1 SD of the gray rate: rule="mean_plus_sd" reads it as
    over the gray mean plus 1 SD (O4a), "sd" as over the SD itself (O4b)."""
    ref = gray_mean + gray_sd if rule == "mean_plus_sd" else gray_sd
    return (pref_rate > threshold) & (pref_rate > ref)


# ---------------------------------------------------------------------------------------------
# Mixed ANOVA (Methods: 3 x 3 mixed ANOVA, relative orientation within units, OSI tertile
# between units). Sums of squares as in the usual split-plot decomposition, without a
# sphericity correction (the paper names none).


def mixed_anova(Y, group):
    """Y: units x levels; group: tertile label per unit. Returns dict of F and p for the
    within factor ("within"), the between factor ("between") and their interaction."""
    Y = np.asarray(Y, float)
    group = np.asarray(group)
    N, J = Y.shape
    gs = np.unique(group)
    G = len(gs)
    grand = Y.mean()
    m_i = Y.mean(1)
    m_j = Y.mean(0)
    ss_bs = J * np.sum((m_i - grand) ** 2)
    ss_g = sum(J * (group == g).sum() * (Y[group == g].mean() - grand) ** 2 for g in gs)
    ss_sw = ss_bs - ss_g
    ss_within = np.sum((Y - m_i[:, None]) ** 2)
    ss_rel = N * np.sum((m_j - grand) ** 2)
    ss_cells = sum((group == g).sum() * np.sum((Y[group == g].mean(0) - grand) ** 2) for g in gs)
    ss_int = ss_cells - ss_g - ss_rel
    ss_err = ss_within - ss_rel - ss_int
    df_rel, df_int, df_err = J - 1, (J - 1) * (G - 1), (J - 1) * (N - G)
    df_g, df_sw = G - 1, N - G
    F_rel = (ss_rel / df_rel) / (ss_err / df_err)
    F_int = (ss_int / df_int) / (ss_err / df_err)
    F_g = (ss_g / df_g) / (ss_sw / df_sw)
    return {"within": (F_rel, stats.f.sf(F_rel, df_rel, df_err), df_rel, df_err),
            "interaction": (F_int, stats.f.sf(F_int, df_int, df_err), df_int, df_err),
            "between": (F_g, stats.f.sf(F_g, df_g, df_sw), df_g, df_sw)}


# ---------------------------------------------------------------------------------------------
# Bootstrap of the decay fits (Methods: units resampled with replacement 1000 times, fits on a
# bound discarded, 2.5 and 97.5 percentiles)


def bootstrap_fits(lr, model, seed, n_boot=1000, sign=-1):
    """lr: units x n log ratios of one region. model "double" or "single". Returns the array of
    accepted parameter sets and the number discarded on a bound or failed."""
    rng = np.random.default_rng(seed)
    U = lr.shape[0]
    out, dropped = [], 0
    n = np.arange(1, lr.shape[1] + 1, dtype=float)
    p0d, p0s = fit_models(lr.mean(0), sign)
    for _ in range(n_boot):
        m = lr[rng.integers(0, U, U)].mean(0)
        if model == "double":
            r = _fit(lambda x, *q: model_double(x, *q, sign=sign), n, m,
                     [tuple(p0d[0])] + STARTS_D[:2], B_D)
            bounds = B_D
        else:
            r = _fit(model_single, n, m, [tuple(p0s[0])] + STARTS_S[:1], B_S)
            bounds = B_S
        if r is None or on_bound(r[0], bounds):
            dropped += 1
            continue
        out.append(r[0])
    return np.array(out), dropped


def _boot_task(args):
    lr, model, seed, *rest = args
    return bootstrap_fits(lr, model, seed, sign=rest[0] if rest else -1)


def bootstrap_many(tasks, workers=4):
    """Run several (lr, model, seed) or (lr, model, seed, sign) bootstraps in parallel
    processes; the sign of the double exponential's slow term is -1 (O5a) unless given."""
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(_boot_task, tasks))
