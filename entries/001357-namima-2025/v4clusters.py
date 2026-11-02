"""Loading and measures for dandiset 001357 (Namima et al. 2025, J Neurosci 45 e1893232024).

Where each parameter comes from:

- DANDISET and VERSION: the most recent published version, the only one (the paper cites none).
- WINDOW = (0.030, 0.200) s after the photodiode onset (`pdOnTS`): Materials and Methods, Data
  analysis, Firing rate computation ("computed within a 30-200 ms window after stimulus onset");
  photodiode onset from Experimental design ("Stimulus onset times were based on photodiode
  detection").
- Baseline: the same window on blank presentations (`cond_ID` 0), same passage ("Baseline FRs were
  similarly computed during blank stimulus presentations").
- RESPONSIVE_RATE = 5 spikes/s above baseline for one stimulus at either contrast: Materials and
  Methods, Dataset and data inclusion criteria, paragraph 2.
- Dark and bright shapes are `luminance` 4 and 12 cd/m2 (Visual stimuli: "darker or brighter than
  the background luminance (4 or 12 cd/m2)"). The files also hold `luminance` 8, which the paper
  does not use; it is left out.
- Texture versions: `mode` 0 original, 1 contrast-reversed, 2 spectral noise (the column's own
  description); mode 2 is not used in the paper and is left out.
- Depth: the files give `depth`, "distance from the electrode tip", in 20 um steps (the position of
  the unit's best channel), not the template center of mass of the Methods (Depth from the most
  superficial neuron). Depth from the most superficial neuron is the largest `depth` of all good
  units in the file minus the unit's `depth`; all units in the files are `is_sua` = 1 (good).
- Noise-corrected correlation: Materials and Methods, Tuning similarity and contrast invariance,
  after Pospisil and Bair (2021). Square-root transformed counts; the bias of the squared covariance
  and of each variance is estimated from the trial-to-trial variance and subtracted; the root of
  the quotient takes the sign of Pearson's r of the means and is truncated to [-1, 1]. The bias
  terms are written here for unequal numbers of repeats per stimulus (the files have 3 to 10); with
  equal repeats they reduce to the published terms. The noise variance of a neuron is the pooled
  within-stimulus variance. Noise is taken as independent between the two response vectors, as in
  Pospisil and Bair.
- Bootstrap: 500 resamples of the repeats of each stimulus, with replacement (same passage). The
  same repeat indices are used for all neurons of a session, since they were recorded together.
  The interval is the 2.5 to 97.5 percentile, an assumption (the paper gives no level; 95% is the
  level it uses for its regressions, as the claims file says). A value is unreliable when the
  interval's width (reading a) or half-width (reading b) exceeds 0.5 (claims file, opening comment).
- Isimilarity and Ssimilarity: ordinary least squares of a neuron's reliable similarities with the
  other responsive neurons of its penetration against distance; 95% t intervals (MATLAB `confint`),
  three or more points (Clusters of similarly tuned neurons).
- Random seeds: each session and stimulus set has its own generator, seeded from its name, a
  standard choice that cannot change a result beyond bootstrap noise.
"""

from __future__ import annotations

import zlib
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
import requests
from scipy import stats

DANDISET = "001357"
VERSION = "0.261006.2007"
API = "https://api.dandiarchive.org/api"
WINDOW = (0.030, 0.200)
SHIFT = -1.3  # s; onsets moved off the stimuli for the clock check, a standard choice
RESPONSIVE_RATE = 5.0
N_BOOT = 500
CI = (2.5, 97.5)
DARK, BRIGHT = 4, 12
MONKEY = {"Z08115": "M1", "Z11111": "M2"}


def list_assets() -> pd.DataFrame:
    """Every asset of the pinned version: path, asset id, size, subject, date and test kind."""
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=500"
    rows = []
    while url:
        page = requests.get(url, timeout=60).json()
        rows += page["results"]
        url = page.get("next")
    df = pd.DataFrame([{"path": r["path"], "asset_id": r["asset_id"], "size": r["size"]} for r in rows])
    ses = df.path.str.extract(r"sub-(\w+)_ses-(\d{8})(\w\w)_")
    df["subject"], df["date"], df["kind"] = ses[0], ses[1], ses[2]
    df["monkey"] = df.subject.map(MONKEY)
    return df.sort_values(["subject", "date", "kind"]).reset_index(drop=True)


def version_metadata() -> dict:
    return requests.get(f"{API}/dandisets/{DANDISET}/versions/{VERSION}/", timeout=60).json()


def _s(x):
    return x.decode() if isinstance(x, bytes) else x


def load_file(asset_id: str) -> dict:
    """Stream one NWB file and reduce it to spike counts in WINDOW for every unit and presentation."""
    f = h5py.File(remfile.File(f"{API}/assets/{asset_id}/download/"), "r")
    t = f["intervals/trials"]
    trials = pd.DataFrame({c: t[c][:] for c in t.keys() if c != "id" and t[c].ndim == 1})
    for c in ("ses_ID", "pen_ID", "sub_ID"):
        trials[c] = trials[c].map(_s)
    u = f["units"]
    units = pd.DataFrame({c: u[c][:] for c in ("unit_ID", "depth", "best_ch", "is_sua", "probe_num")})
    for c in ("ses_ID", "pen_ID", "sub_ID"):
        units[c] = [_s(x) for x in u[c][:]]
    idx = u["spike_times_index"][:]
    st = u["spike_times"][:]
    onset = trials.pdOnTS.to_numpy()
    counts = np.zeros((len(idx), len(onset)), dtype=np.int32)
    shifted = np.zeros_like(counts)
    sorted_ok = True
    start = 0
    for k, stop in enumerate(idx):
        s = st[start:stop]
        if np.any(np.diff(s) < 0):
            sorted_ok = False
            s = np.sort(s)
        counts[k] = np.searchsorted(s, onset + WINDOW[1]) - np.searchsorted(s, onset + WINDOW[0])
        shifted[k] = np.searchsorted(s, onset + SHIFT + WINDOW[1]) - np.searchsorted(s, onset + SHIFT + WINDOW[0])
        start = stop
    meta = {
        "session_id": _s(f["general/session_id"][()]),
        "description": _s(f["session_description"][()]),
        "subject": _s(f["general/subject/subject_id"][()]),
        "sex": _s(f["general/subject/sex"][()]),
        "start": _s(f["session_start_time"][()]),
        "device": f["general/devices/Neuropixels"].attrs.get("description"),
        "n_spikes": int(len(st)),
        "spike_range": (float(st.min()) if len(st) else np.nan, float(st.max()) if len(st) else np.nan),
        "trial_range": (float(trials.start_time.min()), float(trials.stop_time.max())),
        "spikes_sorted": sorted_ok,
        "depth_unit": u["depth"].attrs.get("description"),
        "acquisition": sorted(f["acquisition"].keys()),
        "processing": sorted(f["processing"].keys()),
        "templates": sorted(f["stimulus/templates"].keys()),
        "electrode_columns": sorted(f["general/extracellular_ephys/electrodes"].keys()),
        "electrode_locations": sorted({_s(x) for x in f["general/extracellular_ephys/electrodes/location"][:]}),
    }
    units["depth0"] = units.depth.max() - units.depth
    meta["unit_spikes"] = tuple(np.diff(np.r_[0, idx]).tolist())
    return {"meta": meta, "trials": trials, "units": units, "counts": counts, "shifted": shifted}


def load_many(asset_ids, threads: int = 16) -> list[dict]:
    with ThreadPoolExecutor(threads) as ex:
        return list(ex.map(load_file, asset_ids))


# ---------------------------------------------------------------- stimulus arrays


def stim_array(counts: np.ndarray, keys: pd.DataFrame, order: list) -> tuple[np.ndarray, np.ndarray]:
    """Counts arranged as (unit, stimulus, repeat), NaN-padded, for the stimuli in `order`.

    `keys` holds one hashable stimulus key per presentation (a Series); returns the array and the
    number of repeats per stimulus."""
    key = keys.to_numpy()
    pos = {k: [] for k in order}
    for i, k in enumerate(key):
        if k in pos:
            pos[k].append(i)
    nrep = np.array([len(pos[k]) for k in order])
    R = nrep.max()
    out = np.full((counts.shape[0], len(order), R), np.nan)
    for j, k in enumerate(order):
        out[:, j, : nrep[j]] = counts[:, pos[k]]
    return out, nrep


def shape_arrays(sess: dict) -> dict:
    """Dark and bright arrays over the 120 shapes (stim_ID x rotation), and the blank counts."""
    tr = sess["trials"]
    key = pd.Series(list(zip(tr.stim_ID, tr.rotation)))
    order = sorted({(s, r) for s, r in zip(tr.stim_ID, tr.rotation) if not np.isnan(s)})
    out = {"order": order}
    for name, lum in (("dark", DARK), ("bright", BRIGHT)):
        sel = (tr.luminance == lum).to_numpy()
        out[name] = stim_array(sess["counts"][:, sel], key[sel].reset_index(drop=True), order)
    out["blank"] = sess["counts"][:, (tr.cond_ID == 0).to_numpy()]
    return out


def texture_arrays(sess: dict) -> dict:
    tr = sess["trials"]
    order = sorted(set(tr.stim_ID.dropna()))
    out = {"order": order}
    for name, mode in (("original", 0), ("reversed", 1)):
        sel = (tr["mode"] == mode).to_numpy()
        out[name] = stim_array(sess["counts"][:, sel], tr.stim_ID[sel].reset_index(drop=True), order)
    out["blank"] = sess["counts"][:, (tr.cond_ID == 0).to_numpy()]
    return out


def position_arrays(sess: dict) -> dict:
    tr = sess["trials"]
    order = sorted(set(tr.stim_ID.dropna()))
    out = {"order": order, "positions": sorted(set(tr.position.dropna()))}
    for p in out["positions"]:
        sel = (tr.position == p).to_numpy()
        out[int(p)] = stim_array(sess["counts"][:, sel], tr.stim_ID[sel].reset_index(drop=True), order)
    out["blank"] = sess["counts"][:, (tr.cond_ID == 0).to_numpy()]
    return out


def rates(arr: np.ndarray) -> np.ndarray:
    """Mean firing rate (spikes/s) per unit and stimulus."""
    return np.nanmean(arr, axis=2) / (WINDOW[1] - WINDOW[0])


def baseline(blank: np.ndarray) -> np.ndarray:
    return blank.mean(axis=1) / (WINDOW[1] - WINDOW[0])


def responsive(arrays: list[np.ndarray], blank: np.ndarray) -> np.ndarray:
    """Responsive when one stimulus of any of `arrays` drives the mean rate RESPONSIVE_RATE above baseline."""
    base = baseline(blank)
    peak = np.max([np.nanmax(rates(a), axis=1) for a in arrays], axis=0)
    return peak - base >= RESPONSIVE_RATE


# ---------------------------------------------------------------- noise-corrected correlation


def _moments(arr: np.ndarray, nrep: np.ndarray):
    """Means of sqrt counts (unit, stim), pooled noise variance (unit,), 1/n per stimulus."""
    x = np.sqrt(arr)
    m = np.nanmean(x, axis=2)
    v = np.nanvar(x, axis=2, ddof=1) if x.shape[2] > 1 else np.zeros_like(m)
    df = nrep - 1
    ok = df > 0
    s2 = (v[:, ok] * df[ok]).sum(1) / df[ok].sum()
    return m, s2, 1.0 / nrep


def nc_corr(mx, sx2, ix, my, sy2, iy, pairwise=True):
    """Noise-corrected correlation between rows of mx (a, m) and rows of my (b, m).

    ix, iy: 1/n per stimulus, (m,) or one row per unit (a, m) and (b, m). pairwise=True gives the
    (a, b) matrix; False gives row by row (a == b). NaN where a variance estimate is not positive."""
    m = mx.shape[1]
    ix = np.broadcast_to(ix, mx.shape)
    iy = np.broadcast_to(iy, my.shape)
    xc = mx - mx.mean(1, keepdims=True)
    yc = my - my.mean(1, keepdims=True)
    sxx = (xc**2).sum(1) - sx2 * (1 - 1 / m) * ix.sum(1)
    syy = (yc**2).sum(1) - sy2 * (1 - 1 / m) * iy.sum(1)
    if pairwise:
        sxy = xc @ yc.T
        bias = (sx2[:, None] * (ix @ (yc**2).T) + sy2[None, :] * ((xc**2) @ iy.T)
                - sx2[:, None] * sy2[None, :] * (ix @ iy.T))
        den = sxx[:, None] * syy[None, :]
    else:
        sxy = (xc * yc).sum(1)
        bias = sx2 * (ix * yc**2).sum(1) + sy2 * (iy * xc**2).sum(1) - sx2 * sy2 * (ix * iy).sum(1)
        den = sxx * syy
    num = sxy**2 - bias
    with np.errstate(invalid="ignore", divide="ignore"):
        r2 = np.where(den > 0, num / den, np.nan)
    r = np.sign(sxy) * np.sqrt(np.clip(r2, 0, None))
    return np.clip(r, -1, 1)


def pearson_rows(mx, my):
    xc = mx - mx.mean(1, keepdims=True)
    yc = my - my.mean(1, keepdims=True)
    with np.errstate(invalid="ignore", divide="ignore"):
        return (xc @ yc.T) / np.sqrt(np.outer((xc**2).sum(1), (yc**2).sum(1)))


def _resample(arr, nrep, rng):
    m, R = arr.shape[1], arr.shape[2]
    u = rng.random((m, R))
    idx = np.floor(u * nrep[:, None]).astype(int)
    out = arr[:, np.arange(m)[:, None], idx]
    out[:, np.arange(R)[None, :] >= nrep[:, None]] = np.nan
    return out


def seed_for(name: str) -> int:
    return zlib.crc32(name.encode())


def similarity(arr, nrep, name, n_boot=N_BOOT):
    """Similarity matrix of all units of a session over one stimulus set, with its bootstrap interval.

    Returns r (u, u), lo, hi (percentile interval)."""
    rng = np.random.default_rng(seed_for(name))
    mx, s2, inv = _moments(arr, nrep)
    r = nc_corr(mx, s2, inv, mx, s2, inv)
    boots = np.empty((n_boot,) + r.shape)
    for b in range(n_boot):
        mb, sb, _ = _moments(_resample(arr, nrep, rng), nrep)
        boots[b] = nc_corr(mb, sb, inv, mb, sb, inv)
    with np.errstate(invalid="ignore"):
        lo, hi = np.nanpercentile(boots, CI, axis=0)
    nan_frac = np.isnan(boots).mean(0)
    lo[nan_frac > 0.5] = np.nan
    hi[nan_frac > 0.5] = np.nan
    return r, lo, hi


def invariance(arr_x, n_x, arr_y, n_y, name, n_boot=N_BOOT):
    """Tuning invariance: noise-corrected correlation of each unit's responses to two versions."""
    rng = np.random.default_rng(seed_for(name))
    mx, sx, ix = _moments(arr_x, n_x)
    my, sy, iy = _moments(arr_y, n_y)
    r = nc_corr(mx, sx, ix, my, sy, iy, pairwise=False)
    boots = np.empty((n_boot, len(r)))
    for b in range(n_boot):
        a, sa, _ = _moments(_resample(arr_x, n_x, rng), n_x)
        c, sc, _ = _moments(_resample(arr_y, n_y, rng), n_y)
        boots[b] = nc_corr(a, sa, ix, c, sc, iy, pairwise=False)
    with np.errstate(invalid="ignore"):
        lo, hi = np.nanpercentile(boots, CI, axis=0)
    nan_frac = np.isnan(boots).mean(0)
    lo[nan_frac > 0.5] = np.nan
    hi[nan_frac > 0.5] = np.nan
    return r, lo, hi


def reliable(r, lo, hi, reading: str) -> np.ndarray:
    """Reading 'a': interval width <= 0.5; reading 'b': half-width <= 0.5."""
    width = hi - lo
    limit = 0.5 if reading == "a" else 1.0
    with np.errstate(invalid="ignore"):
        return np.isfinite(r) & np.isfinite(width) & (width <= limit)


# ---------------------------------------------------------------- Isimilarity


def regress(x, y):
    """OLS of y on x: intercept, slope and their 95% t intervals; None when fewer than 3 points."""
    n = len(x)
    if n < 3 or np.ptp(x) == 0:
        return None
    X = np.column_stack([np.ones(n), x])
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    resid = y - X @ beta
    dof = n - 2
    s2 = resid @ resid / dof if dof > 0 else np.nan
    cov = s2 * np.linalg.inv(X.T @ X)
    se = np.sqrt(np.diag(cov))
    t = stats.t.ppf(0.975, dof) if dof > 0 else np.nan
    return {"n": n, "intercept": beta[0], "slope": beta[1],
            "i_lo": beta[0] - t * se[0], "i_hi": beta[0] + t * se[0],
            "s_lo": beta[1] - t * se[1], "s_hi": beta[1] + t * se[1]}


def isimilarity(r, rel, depth0, keep):
    """One row per unit in `keep`: its regression of reliable similarities with the other kept units
    on distance. NaN fields when it has fewer than three points."""
    idx = np.flatnonzero(keep)
    rows = []
    for i in idx:
        others = idx[(idx != i) & rel[i, idx]]
        fit = regress(np.abs(depth0[others] - depth0[i]), r[i, others])
        row = {"unit": i, "n_points": len(others)}
        if fit:
            row.update(fit)
        rows.append(row)
    df = pd.DataFrame(rows)
    for c in ("intercept", "slope", "i_lo", "i_hi", "s_lo", "s_hi"):
        if c not in df:
            df[c] = np.nan
    df["has_line"] = df.intercept.notna()
    df["sig_pos"] = df.i_lo > 0
    df["sig_any"] = (df.i_lo > 0) | (df.i_hi < 0)
    df["slope_sig_pos"] = df.s_lo > 0
    return df


# ---------------------------------------------------------------- AUC


def auc(pos, neg):
    """Area under the ROC curve: P(pos > neg) + P(tie)/2."""
    pos, neg = np.asarray(pos, float), np.asarray(neg, float)
    if len(pos) == 0 or len(neg) == 0:
        return np.nan
    u = stats.mannwhitneyu(pos, neg, alternative="two-sided").statistic
    return u / (len(pos) * len(neg))


# ---------------------------------------------------------------- per-session analyses


def analyse_pair_sets(arrays: dict, names: tuple, keep: np.ndarray, depth0: np.ndarray, tag: str) -> dict:
    """Similarity matrices, reliability and Isimilarity tables for two stimulus versions of a session
    (dark and bright shapes, or original and reversed textures), and the invariance across them."""
    out = {"keep": keep, "depth0": depth0}
    for name in names:
        arr, nrep = arrays[name]
        r, lo, hi = similarity(arr[keep], nrep, f"{tag}-{name}")
        out[name] = {"r": r, "lo": lo, "hi": hi, "mean_sqrt": _moments(arr[keep], nrep)[0],
                     "rate": rates(arr[keep])}
        for rd in "ab":
            rel = reliable(r, lo, hi, rd)
            out[name][f"isim_{rd}"] = isimilarity(r, rel, depth0[keep], np.ones(keep.sum(), bool))
    (ax, nx), (ay, ny) = arrays[names[0]], arrays[names[1]]
    inv, ilo, ihi = invariance(ax[keep], nx, ay[keep], ny, f"{tag}-invariance")
    out["invariance"] = {"r": inv, "lo": ilo, "hi": ihi}
    return out


def neuron_table(res: dict, names: tuple) -> pd.DataFrame:
    """One row per kept neuron of a session: Isimilarity fields under each version and reliability
    reading, and the invariance with its reliability."""
    keep = res["keep"]
    df = pd.DataFrame({"unit": np.flatnonzero(keep), "depth0": res["depth0"][keep]})
    for name in names:
        for rd in "ab":
            t = res[name][f"isim_{rd}"].reset_index(drop=True)
            for c in ("intercept", "slope", "has_line", "sig_pos", "sig_any", "slope_sig_pos", "i_lo", "s_hi"):
                df[f"{c}_{name}_{rd}"] = t[c].to_numpy()
    inv = res["invariance"]
    df["invariance"] = inv["r"]
    for rd in "ab":
        df[f"inv_rel_{rd}"] = reliable(inv["r"], inv["lo"], inv["hi"], rd)
    return df
