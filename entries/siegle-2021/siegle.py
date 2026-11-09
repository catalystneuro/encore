"""Loading and unit measures for Siegle, Jia et al. (2021) on the Allen Visual Coding Neuropixels data.

The paper's 58 passive viewing experiments are on DANDI as dandisets 000021 (Brain Observatory 1.1
stimulus set, 32 sessions) and 000022 (Functional Connectivity stimulus set, 26 sessions); the
paper's Data availability names both. Dandiset 000253, the target, holds a different experiment
(the OpenScope Global/Local Oddball project) and is only surveyed here.

Every file is streamed with remfile and h5py; nothing is written to disk. Spike times are read
only for the non-noise units of the eight visual areas, the other visual cortical areas (VIS*, for
the layer comparison, which pools all cortical units) and the hippocampus, in contiguous blocks.

Where each parameter comes from:

- Unit quality filters, areas and the Figure 3 unit selection: the claims' criteria, which cite
  ExtDataFigure1jk.py, Figure1g.py and Figure3.py of github.com/AllenInstitute/
  neuropixels_platform_paper at commit 4f8bcc26 (the paper's figure code).
- Receptive fields: Methods, "Receptive field analysis" (spike counts in the 250 ms Gabor
  presentation at 81 locations, chi-square against the grand mean, 1,000 location shuffles,
  Gaussian smoothing sigma 1, threshold max - std, largest contiguous region times 100 deg2).
  Contiguity uses scipy.ndimage.label's default 4-connectivity, a standard choice. The p-value is
  the fraction of shuffled statistics at least as large as the observed one, a standard choice.
  As the AllenSDK's ReceptiveFieldMapping (the code the paper names for stimulus metrics; v2.0.0,
  minimum_spike_count=10.0), a unit with fewer than 10 spikes over all Gabor presentations gets no
  p-value (p_value_rf is NaN, so it never counts as significant); the p-value before this rule is
  kept as p_value_rf_all, a variant. The AllenSDK uses spike counts per presentation, as here.
- Time to first spike: Methods, "Response latency" (first spike from 30 ms after onset, trials
  without a spike within 250 ms excluded, median over trials) and functions/time_to_first_spike.py
  (1 ms bins, default end 500 ms, a variant). Figure3/get_flash_PSTH.py, which wrote the paper's
  data/time_to_first_spike.csv, ends the window at 200 ms, a further variant. The spontaneous control uses the same procedure on
  the 1 s grey interval before each flash (same passage).
- Modulation index: Methods, "Modulation index" (Welch spectrum of the 10 ms binned PSTH of the
  preferred condition, MI formula) and functions/modulation_index.py (nperseg 256, the power at
  the frequency nearest the grating's temporal frequency). The preferred condition is the
  stimulus condition (orientation, temporal frequency, and contrast where it varies) with the
  highest mean spike count; blank presentations are left out. This is an assumption: the paper
  takes the metric from the AllenSDK and does not define the preferred condition.
  firing_rate_dg is the spike count over all drifting grating presentations divided by their
  summed duration, an assumption with the same basis.
- Intrinsic and response decay timescales: Methods, "Intrinsic timescale and response decay
  timescale", and Figure3/timescale_calculation.py (10 ms bins, exponential a exp(-t/b) + c with
  b bounded to 1 to 1,000 ms, p0 = (5, 20, 0.1), 2D autocorrelation with scipy.signal.correlate
  'same', middle row removed, mean over trials, second half). Response decay window 0 to 250 ms
  (Methods; the claim's main reading) and 40 to 290 ms (the code, a variant). Intrinsic timescale
  on the 1 s before each flash, lags 1 to 50 (Methods), and the code's variant, 1.0 to 2.0 s after
  onset with lags 2 to 50.
- Gaze: processing/filtered_gaze_mapping/screen_coordinates_spherical (degrees), the AllenSDK
  gaze_mapping output the Methods name; raw_gaze_mapping is a variant.
"""

import concurrent.futures as cf
import time
import warnings

import h5py
import numpy as np
import pandas as pd
import remfile
import requests
from scipy import ndimage, signal
from scipy.optimize import curve_fit

API = "https://api.dandiarchive.org/api"
TARGET = ("000253", "0.240923.1441")
SOURCES = {"000021": "0.251116.2246", "000022": "0.251116.2247"}
CODE_COMMIT = "4f8bcc26fa6fbec1ae687c650bacc9ea67a7036d"
CODE_RAW = f"https://raw.githubusercontent.com/AllenInstitute/neuropixels_platform_paper/{CODE_COMMIT}"

# Figure3.py and Figure4.py; LGN is LGd in the files
AREAS = ["LGd", "VISp", "VISl", "VISrl", "LP", "VISal", "VISpm", "VISam"]
NAMES = {"LGd": "LGN", "VISp": "V1", "VISl": "LM", "VISrl": "RL", "LP": "LP", "VISal": "AL",
         "VISpm": "PM", "VISam": "AM"}
HIERARCHY = {"LGd": -0.515, "VISp": -0.357, "VISl": -0.093, "VISrl": -0.059, "LP": 0.105,
             "VISal": 0.152, "VISpm": 0.327, "VISam": 0.441}
HPC = ["CA1", "CA3", "DG"]
UNIT_COLUMNS = ["quality", "snr", "isi_violations", "amplitude_cutoff", "presence_ratio",
                "firing_rate", "peak_channel_id"]


def list_assets(dandiset, version):
    url = f"{API}/dandisets/{dandiset}/versions/{version}/assets/"
    out, params = [], {"page_size": 1000}
    while url:
        r = requests.get(url, params=params, timeout=60).json()
        out += r["results"]
        url, params = r["next"], None
    return pd.DataFrame([{"dandiset": dandiset, "path": a["path"], "asset_id": a["asset_id"],
                          "size_gb": a["size"] / 1e9} for a in out])


def open_asset(asset_id):
    url = requests.head(f"{API}/assets/{asset_id}/download/", allow_redirects=True, timeout=60).url
    return h5py.File(remfile.File(url), "r")


def _intervals(f, name, cols):
    g = f["intervals"][name]
    d = {"start_time": g["start_time"][:], "stop_time": g["stop_time"][:]}
    for c in cols:
        if c in g:
            v = g[c][:]
            d[c] = v.astype(str) if v.dtype.kind in "OS" else v
    return pd.DataFrame(d)


# ---------------------------------------------------------------- per-unit measures

def window_counts(st, starts, width):
    return np.searchsorted(st, starts + width) - np.searchsorted(st, starts)


def first_spike(st, onsets, start=0.030, end=0.250):
    """Median time to first spike (s) from `start` after onset, trials without one before `end` left out."""
    i = np.searchsorted(st, onsets + start)
    t = np.full(len(onsets), np.nan)
    ok = i < len(st)
    t[ok] = st[i[ok]] - onsets[ok]
    t[t >= end] = np.nan
    t = np.floor(t * 1000) / 1000  # 1 ms bins, as functions/time_to_first_spike.py
    return np.nanmedian(t) if np.isfinite(t).any() else np.nan


def binned(st, onsets, t0, nbins, binw=0.010):
    edges = np.arange(nbins + 1) * binw + t0
    idx = np.searchsorted(st, onsets[:, None] + edges[None, :])
    return np.diff(idx, axis=1)


def rf_test(counts, loc, n_loc, perms, batch=100, stop=10):
    """Chi-square statistic of the Methods and its shuffle p-value; the mean response per location.

    Shuffles run in batches of 100 and stop once 10 shuffled statistics reach the observed one,
    when p >= 0.01 is settled; the p-value is then the fraction over the shuffles run, which only
    the threshold p < 0.01 uses.
    """
    m = np.bincount(loc, minlength=n_loc)
    E = counts.mean()
    if E == 0:
        return np.nan, np.zeros(n_loc)
    O = np.bincount(loc, minlength=n_loc, weights=counts) / m
    chi = np.sum((E - O) ** 2 / E)
    n_sh = len(perms)
    hits, done = 0, 0
    while done < n_sh:
        P = perms[done:done + batch]
        k = len(P)
        lab = (P + (np.arange(k) * n_loc)[:, None]).ravel()
        Os = np.bincount(lab, weights=np.tile(counts, k), minlength=k * n_loc).reshape(k, n_loc) / m
        hits += int(np.sum(np.sum((E - Os) ** 2 / E, axis=1) >= chi))
        done += k
        if hits >= stop:
            break
    return hits / done, O


def rf_area(rf9):
    """Area (deg2) of the largest contiguous region of the smoothed RF above max - std."""
    filt = ndimage.gaussian_filter(rf9, 1.0)
    lab, n = ndimage.label(filt > filt.max() - filt.std())
    if n == 0:
        return np.nan
    sizes = np.bincount(lab.ravel())[1:]
    return sizes.max() * 100.0


def modulation_index(psth, tf, fs=100.0, nperseg=256):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        f, psd = signal.welch(psth, fs=fs, nperseg=nperseg)
    k = np.argmin(np.abs(f - tf))
    sd = np.sqrt(np.mean(psd ** 2) - np.mean(psd) ** 2)
    return np.abs(psd[k] - np.mean(psd)) / sd if sd > 0 else np.nan


def _exp(t, a, b, c):
    return a * np.exp(-1 / b * t) + c


def _exp_jac(t, a, b, c):
    e = np.exp(-t / b)
    return np.stack([e, a * e * t / b ** 2, np.ones_like(t)], axis=1)


def fit_exp(t, y):
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            p, cov = curve_fit(_exp, t, y, p0=(5, 20, 0.1), method="trf",
                               bounds=([0, 1, -np.inf], [np.inf, 1000, np.inf]), jac=_exp_jac,
                               max_nfev=10000)
        return p[1], np.sqrt(np.diag(cov))[1]
    except (ValueError, RuntimeError):
        return np.nan, np.nan


def intrinsic_timescale(X):
    """X: trials x 100 bins of 10 ms. Diagonal means of the bin-by-bin Pearson matrix, fit to lags 1 to 50."""
    with np.errstate(invalid="ignore", divide="ignore"):
        C = np.corrcoef(X.T)
    T = np.array([np.nanmean(np.diag(C, k)) if np.isfinite(np.diag(C, k)).any() else np.nan
                  for k in range(1, X.shape[1])])
    t = np.arange(1, 51) * 10.0
    y = T[:50]
    if not np.isfinite(y).all():
        return np.nan, np.nan
    return fit_exp(t, y)


def decay_timescale(X):
    """X: trials x bins of 10 ms. 2D autocorrelation as Figure3/timescale_calculation.py."""
    nb = X.shape[1]
    ac = signal.correlate(X, X, mode="same")
    ac = np.delete(ac, [ac.shape[0] // 2], axis=0)
    acc = np.mean(ac, axis=0)[nb // 2:]
    t = np.linspace(0, nb / 2 * 10, len(acc))
    return fit_exp(t, acc)


# ---------------------------------------------------------------- one session

def load_session(asset, n_shuffles=1000, seed=0):
    """Tables, gaze and per-unit measures of one session of 000021 or 000022."""
    t_start = time.time()
    f = open_asset(asset.asset_id)
    u = f["units"]
    e = f["general/extracellular_ephys/electrodes"]
    U = pd.DataFrame({c: (u[c][:].astype(str) if c == "quality" else u[c][:]) for c in UNIT_COLUMNS})
    U["unit_id"] = u["id"][:]
    idx = u["spike_times_index"][:]
    U["i1"] = idx
    U["i0"] = np.r_[0, idx[:-1]]
    E = pd.DataFrame({"peak_channel_id": e["id"][:], "location": e["location"][:].astype(str),
                      "x": e["x"][:], "y": e["y"][:], "z": e["z"][:], "probe_id": e["probe_id"][:]})
    U = U.merge(E, on="peak_channel_id", how="left")
    subj = f["general/subject"]
    meta = {"dandiset": asset.dandiset, "path": asset.path,
            "subject": subj["subject_id"][()].decode(), "genotype": subj["genotype"][()].decode(),
            "sex": subj["sex"][()].decode(), "age": subj["age"][()].decode(),
            "session_type": f["general/stimulus"][()].decode(),
            "n_probes": len(f["general/devices"].keys()),
            "n_electrodes": len(E), "y_equals_z": bool(np.all((E.y == E.z) | E.y.isna())),
            "intervals": sorted(f["intervals"].keys()), "processing": sorted(f["processing"].keys())}
    U["session"] = meta["path"].split("ses-")[1].split(".")[0]
    U["subject"] = meta["subject"]
    U["session_type"] = meta["session_type"]

    # stimulus tables
    fl = _intervals(f, "flashes_presentations", ["color"])
    gb = _intervals(f, "gabors_presentations", ["x_position", "y_position"])
    dgname = ("drifting_gratings_presentations" if "drifting_gratings_presentations" in f["intervals"]
              else "drifting_gratings_75_repeats_presentations")
    dg = _intervals(f, dgname, ["orientation", "temporal_frequency", "contrast"])
    meta.update(n_flashes=len(fl), n_gabors=len(gb), dg_stimulus=dgname, n_dg=len(dg),
                flash_colors=dict(zip(*np.unique(fl.color, return_counts=True))),
                flash_duration=float(np.median(fl.stop_time - fl.start_time)),
                gabor_duration=float(np.median(gb.stop_time - gb.start_time)),
                flash_interval=float(np.median(np.diff(fl.start_time))),
                gabor_positions=int(len(gb.groupby(["x_position", "y_position"]))))

    # gaze
    gaze = {}
    for kind in ("filtered", "raw"):
        key = f"processing/{kind}_gaze_mapping/screen_coordinates_spherical"
        if key in f:
            gaze[kind] = f[key + "/data"][:]
    meta["has_gaze"] = "filtered" in gaze

    # spikes of the non-noise units of the eight areas and the hippocampus
    cortex = U.location.str.startswith("VIS")
    sel = U[(U.quality == "good") & (U.location.isin(AREAS + HPC) | cortex)].index.values
    fon = fl.start_time.values
    dark = fl.color.astype(float).values < 0
    xs = np.sort(gb.x_position.unique())
    ys = np.sort(gb.y_position.unique())
    loc = (np.searchsorted(ys, gb.y_position.values) * len(xs) + np.searchsorted(xs, gb.x_position.values))
    n_loc = len(xs) * len(ys)
    rng = np.random.default_rng(seed)
    perms = np.stack([rng.permutation(len(gb)) for _ in range(n_shuffles)])
    perms = loc[perms]  # shuffled location labels; the counts stay in place
    dg_valid = dg.orientation.notna().values
    cond_cols = ["orientation", "temporal_frequency"] + (["contrast"] if dg.contrast.nunique() > 1 else [])
    cond = np.array(["|".join(f"{v:g}" for v in row) for row in dg[cond_cols].fillna(-1).values])
    dg_dur = dg.stop_time.values - dg.start_time.values

    rows = []
    st_ds = u["spike_times"]
    # contiguous runs of selected units, in pieces of at most 8M spikes
    order = np.sort(sel)
    runs, cur = [], []
    for i in order:
        if cur and (i != cur[-1] + 1 or U.i1[i] - U.i0[cur[0]] > 8_000_000):
            runs.append(cur)
            cur = []
        cur.append(i)
    if cur:
        runs.append(cur)
    n_read = 0
    for run in runs:
        a, b = U.i0[run[0]], U.i1[run[-1]]
        block = st_ds[a:b]
        n_read += b - a
        for i in run:
            st = block[U.i0[i] - a:U.i1[i] - a]
            r = {"index": i}
            c = window_counts(st, gb.start_time.values, 0.25).astype(float)
            p, O = rf_test(c, loc, n_loc, perms)
            r["n_spikes_gabor"] = c.sum()
            r["p_value_rf_all"] = p
            r["p_value_rf"] = p if c.sum() >= 10 else np.nan
            r["area_rf"] = rf_area(O.reshape(len(ys), len(xs))) if np.isfinite(p) else np.nan
            for lab, m in (("all", slice(None)), ("dark", dark), ("light", ~dark)):
                r[f"tfs_{lab}_250"] = first_spike(st, fon[m], 0.030, 0.250)
                r[f"tfs_{lab}_500"] = first_spike(st, fon[m], 0.030, 0.500)
            r["tfs_all_200"] = first_spike(st, fon, 0.030, 0.200)
            r["tfs_spont"] = first_spike(st, fon - 1.0, 0.030, 0.250)
            r["rate_pre"] = window_counts(st, fon - 1.0, 1.0).mean()
            dgc = window_counts(st, dg.start_time.values, dg_dur)
            r["firing_rate_dg"] = dgc.sum() / dg_dur.sum()
            means = pd.Series(dgc[dg_valid]).groupby(cond[dg_valid]).mean()
            if means.max() > 0:
                pref = means.idxmax()
                trials = dg_valid & (cond == pref)
                tf = float(pref.split("|")[1])
                psth = binned(st, dg.start_time.values[trials], 0.0, 200).mean(axis=0)
                r["mod_idx_dg"] = modulation_index(psth, tf)
            else:
                r["mod_idx_dg"] = np.nan
            # timescales only for units that can enter Figure 3 (timescale_calculation.py selects them so)
            if ((U.location[i] in AREAS or cortex[i]) and r["p_value_rf"] < 0.01 and r["area_rf"] < 2500
                    and U.snr[i] > 1 and r["firing_rate_dg"] > 0.1):
                r.update(timescales(st, fon))
            rows.append(r)
    M = pd.DataFrame(rows).set_index("index")
    U = U.join(M)
    meta["spikes_read"] = int(n_read)
    meta["seconds"] = time.time() - t_start
    f.close()
    return U, meta, gaze


def intrinsic_timescale_code(X):
    """The code's variant: lags 2 to 50 against t = 10 to 500 ms (timescale_calculation.py)."""
    with np.errstate(invalid="ignore", divide="ignore"):
        C = np.corrcoef(X.T)
    T = np.array([np.nanmean(np.diag(C, k)) if np.isfinite(np.diag(C, k)).any() else np.nan
                  for k in range(1, X.shape[1])])
    y = T[1:50]
    if not np.isfinite(y).all():
        return np.nan, np.nan
    return fit_exp(np.linspace(10, 500, 49), y)


def timescales(st, fon):
    """Intrinsic and response decay timescales of one unit, from all flashes."""
    pre = binned(st, fon, -1.0, 100)
    late = binned(st, fon, 1.0, 100)
    itc, itc_err = intrinsic_timescale_code(late)
    resp = binned(st, fon, 0.0, 29)
    it, it_err = intrinsic_timescale(pre)
    ac, ac_err = decay_timescale(resp[:, 0:25])
    ac2, ac2_err = decay_timescale(resp[:, 4:29])
    return {"timescale_it": it, "err_it": it_err, "spike_count_it": pre.sum(),
            "timescale_it_code": itc, "err_it_code": itc_err, "spike_count_it_code": late.sum(),
            "timescale_ac": ac, "err_ac": ac_err, "spike_count_ac": resp[:, 0:25].sum(),
            "timescale_ac_code": ac2, "err_ac_code": ac2_err, "spike_count_ac_code": resp[:, 4:29].sum()}


def load_all(assets, workers=4):
    """All sessions, one process each (the fits hold the GIL)."""
    with cf.ProcessPoolExecutor(workers) as ex:
        return list(ex.map(load_session, [a for _, a in assets.iterrows()]))


# ---------------------------------------------------------------- statistics

def gaze_radius(xy, q=95):
    xy = xy[np.isfinite(xy).all(axis=1)]
    d = xy - xy.mean(axis=0)
    radial = np.percentile(np.hypot(d[:, 0], d[:, 1]), q)
    per_axis = max(np.percentile(np.abs(d[:, 0]), q), np.percentile(np.abs(d[:, 1]), q))
    return radial, per_axis, len(xy)


# ---------------------------------------------------------------- cross-correlograms
#
# Methods, "Cross-correlation analysis": drifting gratings of the Functional Connectivity set
# (orientations 0, 45, 90 and 135 degrees, 2 Hz, contrast 0.8, 75 repeats each); units of the six
# cortical areas with a mean rate above 2 Hz from 50 to 500 ms after onset; the CCG normalized by
# the triangular overlap theta(tau) = N - |tau| and the geometric mean rate, per orientation, then
# averaged over the four; jitter correction by the expected value of the CCG under jitter of both
# trains within 25 ms windows, which is the CCG of the window-averaged trains (computed exactly from
# the window counts); a sharp peak when the maximum within +/-10 ms exceeds 7 times the SD of the
# flanks at 50 to 100 ms. The bin is 1 ms (Figure2/compute_ccg.ipynb's example uses 2,000 samples
# per 2 s presentation). Window readings: 2 s (the presentation) and 3 s (presentation and grey).

CORTEX = ["VISp", "VISl", "VISrl", "VISal", "VISpm", "VISam"]
MAXLAG = 100
JW = 25


LAGS_USED = np.r_[np.arange(0, 11), np.arange(50, MAXLAG + 1)]  # the peak window and the flanks


def _binned(spikes, onsets, T, pad=MAXLAG):
    """Sparse units x (trials * (T + pad) + pad) matrix of 1 ms spike counts, trials separated by pad,
    and the counts in 25 ms windows, units x (trials * (T / 25 + padw) + padw)."""
    from scipy import sparse
    nW, padw = T // JW, MAXLAG // JW + 1
    rows, cols = [], []
    W = np.zeros((len(spikes), len(onsets), nW + padw), np.float32)
    for u, st in enumerate(spikes):
        i0 = np.searchsorted(st, onsets)
        i1 = np.searchsorted(st, onsets + T / 1000)
        for k in range(len(onsets)):
            b = np.floor((st[i0[k]:i1[k]] - onsets[k]) * 1000).astype(np.int64)
            b = b[(b >= 0) & (b < T)]
            cols.append(pad + k * (T + pad) + b)
            rows.append(np.full(len(b), u))
            W[u, k, :nW] = np.bincount(b // JW, minlength=nW)[:nW]
    rows = np.concatenate(rows) if rows else np.zeros(0, int)
    cols = np.concatenate(cols) if cols else np.zeros(0, int)
    L = len(onsets) * (T + pad) + pad
    A = sparse.csr_matrix((np.ones(len(rows), np.float32), (rows, cols)), shape=(len(spikes), L))
    A.sum_duplicates()
    W = np.concatenate([np.zeros((len(spikes), padw), np.float32), W.reshape(len(spikes), -1)], axis=1)
    return A, W


def ccg_group(spikes, onsets, T):
    """Jitter-corrected, normalized CCG for all pairs over one set of trials; lags -MAXLAG..MAXLAG.

    out[i, j, MAXLAG + tau] is the CCG at lag tau of unit j relative to unit i: a peak at tau > 0
    means unit j fires after unit i (i leads). Only the lags of the peak window and the flanks are
    computed (LAGS_USED); the others are NaN.
    """
    n, M = len(spikes), len(onsets)
    A, W = _binned(spikes, onsets, T)
    lam = np.asarray(A.sum(axis=1)).ravel() / (M * T)  # spikes per bin
    raw = np.full((n, n, 2 * MAXLAG + 1), np.nan, np.float32)
    Ac = A.tocsc()
    L = A.shape[1]
    for tau in LAGS_USED:
        C = (Ac[:, :L - tau] @ Ac[:, tau:].T).toarray()
        raw[:, :, MAXLAG + tau] = C
        raw[:, :, MAXLAG - tau] = C.T
    padw = MAXLAG // JW + 1
    LW = W.shape[1]
    G = {}
    for k in range(padw + 1):
        G[k] = W[:, :LW - k] @ W[:, k:].T  # G[k][i, j] = sum_t W_i[t] W_j[t + k]
    for k in range(1, padw + 1):
        G[-k] = G[k].T
    for tau in np.r_[-LAGS_USED[::-1], LAGS_USED[1:]]:
        k, r = tau // JW, tau % JW
        raw[:, :, MAXLAG + tau] -= ((JW - r) * G[k] + r * G[k + 1]) / JW ** 2
    theta = (T - np.abs(np.arange(-MAXLAG, MAXLAG + 1))).astype(np.float32)
    with np.errstate(invalid="ignore", divide="ignore"):
        raw /= M * theta[None, None, :]
        raw /= np.sqrt(np.outer(lam, lam))[:, :, None]
    return raw


def sharp_peaks(ccg, peak_window=10, flank=(50, 100), k_sd=7.0):
    """Pairs i < j with a sharp peak: (i, j, offset in ms, peak, flank SD)."""
    lags = np.arange(-MAXLAG, MAXLAG + 1)
    centre = np.abs(lags) <= peak_window
    fl = (np.abs(lags) >= flank[0]) & (np.abs(lags) <= flank[1])
    iu, ju = np.triu_indices(ccg.shape[0], 1)
    c = ccg[iu, ju]
    peak = np.nanmax(c[:, centre], axis=1)
    off = lags[centre][np.nanargmax(np.where(np.isfinite(c[:, centre]), c[:, centre], -np.inf), axis=1)]
    sd = np.std(c[:, fl], axis=1)
    sig = peak > k_sd * sd
    return pd.DataFrame({"i": iu[sig], "j": ju[sig], "offset": off[sig], "peak": peak[sig], "sd": sd[sig]}), len(iu)


def load_ccg_session(asset, windows=(2000, 3000), spont=True):
    """Units of the six cortical areas above 2 Hz and the sharp peaks of their CCGs, per reading."""
    t_start = time.time()
    f = open_asset(asset.asset_id)
    u = f["units"]
    e = f["general/extracellular_ephys/electrodes"]
    U = pd.DataFrame({c: (u[c][:].astype(str) if c == "quality" else u[c][:]) for c in UNIT_COLUMNS})
    U["unit_id"] = u["id"][:]
    idx = u["spike_times_index"][:]
    U["i1"] = idx
    U["i0"] = np.r_[0, idx[:-1]]
    E = pd.DataFrame({"peak_channel_id": e["id"][:], "location": e["location"][:].astype(str),
                      "x": e["x"][:], "y": e["y"][:], "z": e["z"][:]})
    U = U.merge(E, on="peak_channel_id", how="left")
    dg = _intervals(f, "drifting_gratings_75_repeats_presentations", ["orientation", "contrast", "temporal_frequency"])
    dg = dg[(dg.contrast == 0.8)].sort_values("start_time")
    sp = _intervals(f, "spontaneous_presentations", [])
    sp = sp[(sp.stop_time - sp.start_time) > 600]
    cand = U[(U.quality == "good") & U.location.isin(CORTEX)].copy()
    st_ds = u["spike_times"]
    spikes, rates = [], []
    on = dg.start_time.values
    for i, r in cand.iterrows():
        st = st_ds[r.i0:r.i1]
        n = window_counts(st, on + 0.05, 0.45).sum()
        rates.append(n / (0.45 * len(on)))
        spikes.append(st)
    cand["rate_dg"] = rates
    keep = np.where(cand.rate_dg.values > 2)[0]
    units = cand.iloc[keep].reset_index(drop=True)
    spikes = [spikes[k] for k in keep]
    out = {"units": units, "n_dg_trials": len(dg), "orientations": sorted(dg.orientation.unique()),
           "dg_onset_interval": float(np.median(np.diff(on))), "peaks": {}, "n_pairs": {}}
    for T in windows:
        acc = None
        for ori in sorted(dg.orientation.unique()):
            c = ccg_group(spikes, dg.start_time.values[dg.orientation.values == ori], T)
            acc = c if acc is None else acc + c
        acc /= len(dg.orientation.unique())
        out["peaks"][f"grating_{T}"], out["n_pairs"][f"grating_{T}"] = sharp_peaks(acc)
        del acc
    if spont and len(sp):
        a, b = sp.start_time.values[0], sp.stop_time.values[0]
        out["spont_duration"] = b - a
        for T in windows:
            segs = np.arange(a, b - T / 1000, T / 1000)
            c = ccg_group(spikes, segs, T)
            out["peaks"][f"spont_{T}"], out["n_pairs"][f"spont_{T}"] = sharp_peaks(c)
            out[f"n_spont_segments_{T}"] = len(segs)
            del c
    out["seconds"] = time.time() - t_start
    out["session"] = asset.path.split("ses-")[1].split(".")[0]
    out["subject"] = asset.path.split("/")[0].replace("sub-", "")
    f.close()
    return out


def load_ccg_all(assets, workers=4):
    with cf.ProcessPoolExecutor(workers) as ex:
        return list(ex.map(load_ccg_session, [a for _, a in assets.iterrows()]))
