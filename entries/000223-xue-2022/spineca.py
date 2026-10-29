"""Loading and measures for dandiset 000223 (Xue, Buccino et al. 2022, J. Neural Eng.).

Paired dendritic spine Ca2+ imaging and HD-MEA recordings of rat cortical cultures. Each NWB
file holds the raw HD-MEA recording, the curated sorted units, the confocal image series, and
the ROIs of one target spine and its dendritic shaft (two pairs in one file) with their mean
traces.

Where each parameter comes from. "Claims" is the claims file
claims/000223/10.1088-1741-2552-ac8765.yaml, which cites the Methods and the paper's code
(github.com/starquakes/mea_spineca_mapping at commit 99c2a47, "the code" below). "Paper" is a
passage of the paper taken by the author (protocol, author step 1.6). "Assumption" and
"standard choice" are said where they apply.

- dF/F: 25th percentile baseline over 100 frames with scipy.ndimage.percentile_filter
  (Claims; Methods 2.4; imaging_tools.dff method "winperc2").
- Convolution: causal exponential kernel, decay 0.5 s, unit area (Claims; Methods 2.7 and
  Results 3.1; elephant ExponentialKernel(sigma=0.5 s) with center_kernel=False in the code),
  sampled at the first MEA sample at or after each frame time (np.searchsorted of the frame
  times into the MEA sample times, load_nwb_file in the code). The code computes the rate at
  every 20 kHz sample with elephant and then samples it; here the same sum is computed at the
  frame times directly (`convolve_at_frames`). The notebook compares the two for one recording.
  The convolved trace gets +1 and the same dF/F; NaN and inf set to 0 (Claims; notebook 1).
- Demixing: sklearn HuberRegressor with default settings, shaft dF/F against spine dF/F over
  all frames, slope and intercept subtracted (Claims; Methods 2.4; notebook 1).
- Network bursts (`detect_bursts`): Methods 2.6 and notebook 1, as in the claims file. Bins of
  10 ms, p_baseline 85, peaks of height at least the p_thresh percentile, at least 50 ms apart
  (the code's detect_peaks, copied below), prominence above the threshold (scipy
  peak_prominences, strict as in the code), edges where the smoothed rate falls to the baseline
  (index arithmetic of the code), bursts touching the start or end dropped (Methods: "Edge
  cases ... were excluded"; the code would stop with an error there), bursts without spikes
  dropped, bursts closer than 75 ms merged by the code's single pass (a variant merges every
  chain into one burst, as Methods 2.6 says, "merged into a single larger burst"), extended by
  0.1 s before and 0.5 s after. Smoothing by lowess over 5 points (Methods, n_span = 5, the claims' main
  reading) or with frac 0.0002 (the code, a variant). Hyperactive units: rate at or above the
  99.75th percentile ("pc", the code's default) or at or above 15 Hz ("hz"). p_thresh 96 to 99.
- Frames excluded: frames whose time on np.linspace(0, MEA duration, n_frames) lies strictly
  inside an extended burst; the last frame is never excluded (notebook 1, as the claims file
  says).
- Surrogates (`surrogate_block`): Claims; Methods 2.7; imaging_tools.generate_surrogates.
  ceil(Pr N) spikes kept at random (code), or a Bernoulli draw per spike (variant); trace
  divided by its SD, times the median over pixels of (signal pixel SD minus noise pixel SD),
  plus the median of the spine pixels' medians, plus white noise of SD the median noise pixel
  SD, then dF/F. Surrogate j of every unit uses release probability j, as in the code.
- Release probabilities: numpy lognormal(2.5, 0.6) / 100, values above 1 replaced by uniform
  values in 0 to 1, 1'000 of them (Claims; Methods 2.7).
- Noise and signal pixels (`noise_signal`): signal pixels are the spine ROI of the file; the
  noise region is a background square near the spine, its pixels subsampled at random to the
  spine's pixel count (Methods 2.7; notebook 2). The dataset holds no background ROI, so the
  squares are placed by `background_squares`, a rule fixed before any R was computed: 6 by 6
  pixel squares on a grid around the spine, at least 4 pixels from any ROI of the file, whose
  mean image intensity is at most the 25th percentile of the squares in the 96 by 96 pixel
  window around the spine (no visible cell structure); the three nearest to the spine are used.
  Square size, window and percentile are an assumption: the paper says only "a background ROI
  close to the spine" (Methods 2.7).
- Grid of quantiles: np.round(np.linspace(0, 1, 100), 3) for Q_test and Q_GT (Claims; notebook
  3). F with beta 0.5 (Methods 2.8).
- Random seeds: a standard choice, given per claim in the notebook.
"""

from __future__ import annotations

import math
import warnings
from concurrent.futures import ProcessPoolExecutor

import h5py
import numpy as np
import remfile
import requests
import scipy.ndimage as ndimg
import scipy.signal as ss
import scipy.sparse as sp
import statsmodels.api as sm
from sklearn.linear_model import HuberRegressor

DANDISET_ID = "000223"
DANDISET_VERSION = "0.260528.0906"
API = "https://api.dandiarchive.org/api"
MEA_FS = 20000.0
TAU = 0.5
PLEN, PPRCTL = 100, 25

# Table 1 of the paper, row by row: culture ID, spine ID, best_R, GT_Q, GT_thr, test_Q, test_thr,
# max_F, accept?, total #units, OUT/IN ratio, spike contrast. Used only as the reference values
# that the claims compare with; no analysis uses them as input except the Table 1 quantiles,
# reading (a) of claim acceptance-9-of-20.
TABLE1_COLUMNS = ["culture", "spine", "best_R", "GT_Q", "GT_thr", "test_Q", "test_thr", "max_F",
                  "accept", "units", "out_in", "spike_contrast"]
TABLE1 = [
    (1, 1, 0.523, 0.091, 0.214, 0.960, 0.296, 0.787, True, 78, 0.733, 0.38),
    (1, 2, 0.516, 0.162, 0.291, 0.960, 0.271, 0.854, True, 132, 2.003, 0.17),
    (1, 3, 0.217, 0.172, 0.112, 0.960, 0.190, 0.835, True, 66, 1.717, 0.17),
    (1, 4, 0.644, 0.162, 0.311, 0.949, 0.489, 0.850, True, 185, 0.588, 0.23),
    (1, 5, 0.429, 0.162, 0.358, 0.929, 0.520, 0.797, False, 159, 0.318, 0.26),
    (2, 6, 0.647, 0.192, 0.448, 0.929, 0.619, 0.599, True, 50, 0.189, 0.41),
    (2, 7, 0.346, 0.152, 0.503, 0.929, 0.585, 0.604, False, 55, 0.269, 0.48),
    (2, 8, 0.340, 0.030, 0.227, 0.929, 0.475, 0.544, False, 66, 0.060, 0.62),
    (3, 9, 0.671, 0.222, 0.507, 0.949, 0.639, 0.795, True, 179, 0.425, 0.28),
    (3, 10, 0.765, 0.222, 0.507, 0.949, 0.639, 0.795, True, 179, 0.425, 0.28),
    (3, 11, 0.148, 0.232, 0.354, 0.939, 0.351, 0.775, False, 99, 0.783, 0.20),
    (4, 12, 0.597, 0.152, 0.353, 0.960, 0.544, 0.870, True, 114, 0.719, 0.29),
    (4, 13, 0.160, 0.172, 0.267, 0.960, 0.068, 0.860, False, 128, 0.425, 0.36),
    (5, 14, 0.394, 0.111, 0.456, 0.869, 0.435, 0.485, False, 133, 0.289, 0.64),
    (5, 15, 0.400, 0.091, 0.436, 0.879, 0.604, 0.520, False, 133, 0.222, 0.69),
    (6, 16, 0.676, 0.424, 0.383, 0.545, 0.666, 0.525, True, 58, 0.171, 0.43),
    (7, 17, 0.602, 0.232, 0.500, 0.889, 0.707, 0.537, False, 50, 0.534, 0.31),
    (8, 18, 0.311, 0.182, 0.214, 0.949, 0.324, 0.723, False, 100, 0.464, 0.25),
    (9, 19, 0.219, 0.182, 0.233, 0.909, 0.298, 0.610, False, 87, 0.272, 0.50),
    (10, 20, 0.294, 0.121, 0.414, 0.879, 0.364, 0.577, False, 59, 0.112, 0.53),
]


# ---------------------------------------------------------------------------------------------
# Archive access


def list_assets(version=DANDISET_VERSION):
    """Assets of a version: list of dicts with asset_id, path, size, blob."""
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{version}/assets/?page_size=200"
    out = []
    while url:
        page = requests.get(url, timeout=60).json()
        out += page["results"]
        url = page.get("next")
    return out


def version_info(version=DANDISET_VERSION):
    return requests.get(f"{API}/dandisets/{DANDISET_ID}/versions/{version}/info/", timeout=60).json()


def s3_url(asset_id):
    meta = requests.get(f"{API}/assets/{asset_id}/", timeout=60)
    meta.raise_for_status()
    return next(u for u in meta.json()["contentUrl"] if "s3.amazonaws.com" in u)


def open_h5(asset_id):
    return h5py.File(remfile.File(s3_url(asset_id)), "r")


def load_session(asset_id):
    """Everything the analysis uses from one file, except the image series."""
    with open_h5(asset_id) as f:
        units = f["units"]
        st = units["spike_times"][:]
        idx = units["spike_times_index"][:].astype(np.int64)
        trains = np.split(st, idx[:-1])
        ps = f["processing/ophys/ImageSegmentation/PlaneSegmentation"]
        es = f["acquisition/ElectricalSeries_raw"]
        tps = f["acquisition/TwoPhotonSeries"]
        s = {
            "asset_id": asset_id,
            "subject_id": f["general/subject/subject_id"][()].decode(),
            "species": f["general/subject/species"][()].decode(),
            "session_start": f["session_start_time"][()].decode(),
            "unit_ids": units["id"][:],
            "unit_cols": [c.decode() if isinstance(c, bytes) else str(c) for c in units.attrs["colnames"]],
            "trains": trains,
            "spike_index_dtype": str(units["spike_times_index"].dtype),
            "n_mea_samples": es["data"].shape[0],
            "n_channels": es["data"].shape[1],
            "mea_rate": float(es["starting_time"].attrs["rate"]),
            "mea_start": float(es["starting_time"][()]),
            "mea_conversion": float(es["data"].attrs["conversion"]),
            "frame_times": tps["timestamps"][:],
            "image_shape": tps["data"].shape,
            "image_chunks": tps["data"].chunks,
            "imaging_rate": float(f["general/optophysiology/ImagingPlane/imaging_rate"][()]),
            "indicator": f["general/optophysiology/ImagingPlane/indicator"][()].decode(),
            "roi_traces": f["processing/ophys/Fluorescence/RoiResponseSeries/data"][:],
            "roi_rate": float(f["processing/ophys/Fluorescence/RoiResponseSeries/starting_time"].attrs["rate"]),
            "dff_stored": f["processing/ophys/Fluorescence/Dff/data"][:],
            "masks": ps["image_mask"][:],
            "centroids": ps["RoiCentroid"][:],
            "roi_ids": ps["id"][:],
            "accepted": ps["Accepted"][:],
        }
    s["mea_duration"] = s["n_mea_samples"] / MEA_FS
    s["n_frames"] = len(s["frame_times"])
    return s


def _read_block(args):
    asset_url, t0, t1, r0, r1, c0, c1 = args
    with h5py.File(remfile.File(asset_url), "r") as f:
        return f["acquisition/TwoPhotonSeries/data"][t0:t1, r0:r1, c0:c1]


def read_patches(requests_list, workers=16, frames_per_block=150):
    """Read image patches over all frames, in parallel blocks of frames.

    requests_list: list of (key, asset_id, n_frames, (r0, r1, c0, c1)). Returns {key: array}.
    """
    jobs, keys = [], []
    for key, asset_id, n_frames, (r0, r1, c0, c1) in requests_list:
        url = s3_url(asset_id)
        for t0 in range(0, n_frames, frames_per_block):
            jobs.append((url, t0, min(n_frames, t0 + frames_per_block), r0, r1, c0, c1))
            keys.append(key)
    with ProcessPoolExecutor(workers) as ex:
        blocks = list(ex.map(_read_block, jobs))
    out = {}
    for key, b in zip(keys, blocks):
        out.setdefault(key, []).append(b)
    return {k: np.concatenate(v) for k, v in out.items()}


# ---------------------------------------------------------------------------------------------
# Traces


def dff(trace, window=PLEN, percentile=PPRCTL):
    """dF/F with a moving percentile baseline (imaging_tools.dff, method winperc2)."""
    baseline = ndimg.percentile_filter(trace, percentile, window)
    return (trace - baseline) / baseline


def dff_rows(x, window=PLEN, percentile=PPRCTL):
    """dff for each row of a 2-D array (row by row: the 1-D filter is much faster)."""
    out = np.empty_like(x, dtype=float)
    for i in range(x.shape[0]):
        out[i] = dff(x[i], window, percentile)
    return out


def frame_sample_times(s):
    """Time of the MEA sample used for each frame: np.searchsorted(mea_times, frame_times)."""
    idx = np.ceil(np.round(s["frame_times"] * MEA_FS, 6)).astype(np.int64)
    idx = np.minimum(idx, s["n_mea_samples"] - 1)
    return idx / MEA_FS


def spike_weights(train, t_frames, tau=TAU):
    """For each spike, the first frame at or after it and the kernel value at that frame."""
    t = np.round(np.asarray(train) * MEA_FS) / MEA_FS  # spike times on the 20 kHz grid
    b = np.searchsorted(t_frames, t, side="left")
    keep = b < len(t_frames)
    b, t = b[keep], t[keep]
    w = np.exp(-(t_frames[b] - t) / tau) / tau
    return b, w


def convolve_at_frames(counts_by_frame, t_frames, tau=TAU):
    """Exponential filter of per-frame kernel sums: rate(t_f) = sum over spikes s <= t_f of
    exp(-(t_f - s) / tau) / tau. counts_by_frame: (..., n_frames)."""
    decay = np.exp(-np.diff(t_frames) / tau)
    y = np.array(counts_by_frame, dtype=float, copy=True)
    for f in range(1, y.shape[-1]):
        y[..., f] += y[..., f - 1] * decay[f - 1]
    return y


def convolved_traces(s, tau=TAU):
    """Convolved, sampled, +1 and dF/F trace of every unit (notebook 1). Returns (rates, dff)."""
    t_frames = frame_sample_times(s)
    n_f = len(t_frames)
    sums = np.zeros((len(s["trains"]), n_f))
    for i, tr in enumerate(s["trains"]):
        b, w = spike_weights(tr, t_frames, tau)
        np.add.at(sums[i], b, w)
    rates = convolve_at_frames(sums, t_frames, tau)
    with np.errstate(divide="ignore", invalid="ignore"):
        d = dff_rows(rates + 1.0)
    d[~np.isfinite(d)] = 0
    return rates, d


def demix(spine_dff, shaft_dff):
    """Huber regression of the spine dF/F on the shaft dF/F; returns demixed trace, slope, offset."""
    h = HuberRegressor().fit(shaft_dff.reshape(-1, 1), spine_dff)
    slope, offset = h.coef_[0], h.intercept_
    return spine_dff - (slope * shaft_dff + offset), slope, offset


def zscore_rows(x):
    x = x - x.mean(axis=-1, keepdims=True)
    sd = np.sqrt((x ** 2).sum(axis=-1, keepdims=True))
    with np.errstate(invalid="ignore", divide="ignore"):
        return x / sd


def pearson_with_units(trace, unit_dff, keep):
    """Pearson R of one trace with every unit's convolved trace over the kept frames."""
    a = zscore_rows(trace[keep][None, :])[0]
    b = zscore_rows(unit_dff[:, keep])
    return b @ a


def rank_units(r):
    """Units by decreasing R; units whose R is undefined (a constant trace over the kept
    frames) are left out, as the code's argsort would otherwise rank NaN first."""
    ok = np.where(np.isfinite(r))[0]
    return ok[np.argsort(r[ok])[::-1]]


# ---------------------------------------------------------------------------------------------
# Network bursts (Methods 2.6, notebook 1)


def detect_peaks(x, mph=None, mpd=1):
    """The code's detect_peaks (imaging_tools.py), for edge='rising', threshold 0, no NaN."""
    x = np.atleast_1d(x).astype("float64")
    if x.size < 3:
        return np.array([], dtype=int)
    dx = x[1:] - x[:-1]
    ind = np.where((np.hstack((dx, 0)) <= 0) & (np.hstack((0, dx)) > 0))[0]
    ind = np.unique(ind)
    if ind.size and ind[0] == 0:
        ind = ind[1:]
    if ind.size and ind[-1] == x.size - 1:
        ind = ind[:-1]
    if ind.size and mph is not None:
        ind = ind[x[ind] >= mph]
    if ind.size and mpd > 1:
        ind = ind[np.argsort(x[ind])][::-1]
        idel = np.zeros(ind.size, dtype=bool)
        for i in range(ind.size):
            if not idel[i]:
                idel = idel | (ind >= ind[i] - mpd) & (ind <= ind[i] + mpd)
                idel[i] = 0
        ind = np.sort(ind[~idel])
    return ind


def unit_rates(s):
    return np.array([len(t) for t in s["trains"]]) / s["mea_duration"]


def hyperactive(s, strategy):
    r = unit_rates(s)
    if strategy == "pc":
        return np.where(r >= np.percentile(r, 99.75))[0]
    if strategy == "hz":
        return np.where(r >= 15)[0]
    raise ValueError(strategy)


def _burst_counts(s, strategy, smoothing, bin_s=10e-3):
    """Population spike counts per bin and their lowess smoothing, cached on the session."""
    cache = s.setdefault("_burst_cache", {})
    if (strategy, smoothing) not in cache:
        drop = set(hyperactive(s, strategy).tolist())
        spikes = np.sort(np.concatenate([t for i, t in enumerate(s["trains"]) if i not in drop]))
        bins = np.arange(0, np.round(s["mea_duration"]) + bin_s, bin_s)
        tvec = np.convolve(bins, [0.5, 0.5])[1:-1]
        n = np.histogram(spikes, bins=bins)[0]
        frac = 5 / len(n) if smoothing == "span5" else 0.0002
        sm_n = sm.nonparametric.lowess(n, np.arange(len(n)), frac=frac)[:, 1]
        cache[(strategy, smoothing)] = (spikes, tvec, n, sm_n, len(drop))
    return cache[(strategy, smoothing)]


def detect_bursts(s, p_thresh=97, strategy="pc", smoothing="span5", p_baseline=85,
                  bin_s=10e-3, t_ipi=50e-3, t_ibi=75e-3, merge="code"):
    """Network bursts as (start, end) arrays in seconds, before the 0.1 s / 0.5 s extension.

    merge="code" is the code's single pass, which keeps the first two bursts of a chain of three
    or more closer than t_ibi and drops the rest (counted in info["chain_lost"]); merge="full"
    merges every chain into one burst, as Methods 2.6 says (a variant)."""
    spikes, tvec, n, sm_n, n_drop = _burst_counts(s, strategy, smoothing, bin_s)
    thr = np.percentile(n, p_thresh)
    base = np.percentile(n, p_baseline)
    peaks = detect_peaks(n, mph=thr, mpd=t_ipi / bin_s)
    if len(peaks) == 0:
        return np.array([]), np.array([]), {"threshold": thr, "baseline": base, "n_peaks": 0,
                                            "n_hyperactive": n_drop, "n_bursts": 0}
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        prom = ss.peak_prominences(n, peaks)[0]
    peaks = peaks[prom > thr]
    starts, ends, edge = [], [], 0
    for p in peaks:
        left = np.where(np.flipud(sm_n[:p]) <= base)[0]
        right = np.where(sm_n[p:] <= base)[0]
        if len(left) == 0 or len(right) == 0:
            edge += 1
            continue
        starts.append(tvec[p - left[0] + 1])
        ends.append(tvec[min(p + right[0] - 1, len(tvec) - 1)])
    starts, ends = np.array(starts), np.array(ends)
    cnt = np.array([np.count_nonzero((spikes >= a) & (spikes <= b)) for a, b in zip(starts, ends)])
    empty = int(np.sum(cnt == 0))
    starts, ends = starts[cnt > 0], ends[cnt > 0]
    chain_lost = 0
    if len(starts) > 1:
        ibi = starts[1:] - ends[:-1]
        i_neg = np.where(ibi < t_ibi)[0]
        chain_lost = int(np.sum(np.isin(i_neg - 1, i_neg)))
    if merge == "full" and len(starts) > 1:
        group = np.concatenate([[0], np.cumsum(ibi >= t_ibi)])
        starts = np.array([starts[group == k].min() for k in np.unique(group)])
        ends = np.array([ends[group == k].max() for k in np.unique(group)])
    elif len(starts) > 1:  # the code's single merging pass
        ends = ends.copy()
        starts = starts.copy()
        ends[i_neg] = ends[i_neg + 1]
        starts[i_neg + 1] = np.nan
        ends[i_neg + 1] = np.nan
        ok = ~np.isnan(starts)
        starts, ends = starts[ok], ends[ok]
    info = {"threshold": thr, "baseline": base, "n_peaks": int(len(peaks)), "edge_dropped": edge,
            "empty_dropped": empty, "n_hyperactive": n_drop, "n_bursts": int(len(starts)),
            "chain_lost": chain_lost}
    return starts, ends, info


def keep_frames(s, starts, ends, pre=0.1, post=0.5):
    """Frames outside the extended bursts, on the code's frame times linspace(0, duration, n)."""
    ts = np.linspace(0, s["mea_duration"], s["n_frames"])
    ex = np.zeros(len(ts), dtype=bool)
    for a, b in zip(starts - pre, ends + post):
        ex[:-1] |= (ts[:-1] > a) & (ts[:-1] < b)
    return np.where(~ex)[0]


def out_in_ratio(trains, starts, ends, t0, t1):
    spikes = np.concatenate(trains)
    spikes = spikes[(spikes >= t0) & (spikes <= t1)]
    inside = np.zeros(len(spikes), dtype=bool)
    order = np.argsort(spikes)
    sp_sorted = spikes[order]
    for a, b in zip(starts, ends):
        i0 = np.searchsorted(sp_sorted, a, side="left")
        i1 = np.searchsorted(sp_sorted, b, side="right")
        inside[order[i0:i1]] = True
    n_in = inside.sum()
    return (len(spikes) - n_in) / n_in if n_in else np.nan


# ---------------------------------------------------------------------------------------------
# Noise and signal estimate (Methods 2.7, notebook 2)


def patch_bounds(s, roi, half=48):
    """96 by 96 pixel window around an ROI's centre, inside the image."""
    yy, xx = np.nonzero(s["masks"][roi])
    cy, cx = int(round(yy.mean())), int(round(xx.mean()))
    H, W = s["image_shape"][1:]
    r0 = min(max(cy - half, 0), H - 2 * half)
    c0 = min(max(cx - half, 0), W - 2 * half)
    return r0, r0 + 2 * half, c0, c0 + 2 * half


def background_squares(s, roi, bounds, mean_img, side=6, margin=4, pct=25, n=3):
    """Background squares near the spine with no visible structure (rule in the docstring)."""
    r0, r1, c0, c1 = bounds
    yy, xx = np.nonzero(s["masks"][roi])
    cy, cx = yy.mean() - r0, xx.mean() - c0
    any_roi = s["masks"].any(axis=0)[r0:r1, c0:c1]
    near = ndimg.binary_dilation(any_roi, iterations=margin)
    cand = []
    for i in range(0, r1 - r0 - side + 1, side):
        for j in range(0, c1 - c0 - side + 1, side):
            if near[i:i + side, j:j + side].any():
                continue
            cand.append((i, j, mean_img[i:i + side, j:j + side].mean(),
                         math.hypot(i + side / 2 - cy, j + side / 2 - cx)))
    cut = np.percentile([c[2] for c in cand], pct)
    dim = sorted([c for c in cand if c[2] <= cut], key=lambda c: c[3])
    return [(i, j, side, m, d) for i, j, m, d in dim[:n]], cut, len(cand)


def noise_signal(patch, s, roi, bounds, square, rng):
    """Signal and noise pixel SDs (equal counts), the baseline, from a patch (frames, rows, cols)."""
    r0, _, c0, _ = bounds
    yy, xx = np.nonzero(s["masks"][roi])
    sig = patch[:, yy - r0, xx - c0].astype(float).T          # pixels x frames
    i, j, side = square[:3]
    noi = patch[:, i:i + side, j:j + side].reshape(len(patch), -1).astype(float).T
    pick = np.sort(rng.permutation(len(noi))[:len(sig)])
    std_noise = noi[pick].std(axis=1)
    std_signal = sig.std(axis=1)
    baseline = np.median(np.median(sig, axis=1))
    return {"std_signal": std_signal, "std_noise": std_noise, "baseline": baseline,
            "amp": np.median(std_signal - std_noise), "sigma": np.median(std_noise)}


# ---------------------------------------------------------------------------------------------
# Surrogates (Methods 2.7, imaging_tools.generate_surrogates)


def release_probabilities(rng, n=1000):
    pr = rng.lognormal(2.5, 0.6, n) / 100
    big = pr > 1
    pr[big] = rng.random(big.sum())
    return pr


def surrogate_block(train, t_frames, pr, est, rng, bernoulli=False, tau=TAU):
    """dF/F surrogates of one unit, one per release probability: array (len(pr), n_frames)."""
    b, w = spike_weights(train, t_frames, tau)
    N, F, S = len(b), len(t_frames), len(pr)
    if N == 0:
        return np.full((S, F), np.nan)
    W = sp.csr_matrix((w, (np.arange(N), b)), shape=(N, F))
    M = np.zeros((S, N), dtype=np.float32)
    for j, p in enumerate(pr):
        if bernoulli:
            M[j, rng.random(N) < p] = 1
        else:
            M[j, rng.permutation(N)[:int(np.ceil(p * N))]] = 1
    sums = np.asarray((W.T @ M.T).T)
    rate = convolve_at_frames(sums, t_frames, tau)
    with np.errstate(invalid="ignore", divide="ignore"):
        k = rate / rate.std(axis=1, keepdims=True) * est["amp"]
    k = k + est["baseline"] + rng.normal(0, 1, (S, F)) * est["sigma"]
    return dff_rows(k)


def acceptance_distributions(s, unit_dff, keep, best, second, pr, est, rng, bernoulli=False):
    """GT-Rs (surrogates of the best unit against its trace) and test-Rs (surrogates of the
    second-best unit against the best unit's trace), over the kept frames (notebook 2)."""
    t_frames = frame_sample_times(s)
    ref = zscore_rows(unit_dff[best][keep][None, :])[0]
    gt = surrogate_block(s["trains"][best], t_frames, pr, est, rng, bernoulli)
    te = surrogate_block(s["trains"][second], t_frames, pr, est, rng, bernoulli)
    return zscore_rows(gt[:, keep]) @ ref, zscore_rows(te[:, keep]) @ ref


def r_tensor(s, unit_dff, keep, pr, est, seed):
    """R of every surrogate of every unit with every unit's trace: array (units, surrogates,
    units), float32 (notebook 3, compute_corr_r). Unit i's surrogates use the generator
    seeded by (seed, i)."""
    t_frames = frame_sample_times(s)
    Z = zscore_rows(unit_dff[:, keep]).astype(np.float32)
    Z[~np.isfinite(Z)] = 0
    n = len(s["trains"])
    out = np.empty((n, len(pr), n), dtype=np.float32)
    for i in range(n):
        rng = np.random.default_rng([seed, i])
        sur = surrogate_block(s["trains"][i], t_frames, pr, est, rng)
        zs = zscore_rows(sur[:, keep]).astype(np.float32)
        out[i] = zs @ Z.T
    return out


def weighted_quantile(values, weights, q):
    """np.quantile (linear) of the multiset in which values[k] appears weights[k] times; NaN
    values are left out, as np.nanquantile does."""
    ok = np.isfinite(values)
    values, weights = values[ok], weights[ok]
    o = np.argsort(values, kind="stable")
    v, cw = values[o], np.cumsum(weights[o])
    h = (cw[-1] - 1) * np.asarray(q)
    lo, hi = np.floor(h).astype(np.int64), np.ceil(h).astype(np.int64)
    vlo = v[np.searchsorted(cw, lo, side="right")]
    vhi = v[np.searchsorted(cw, hi, side="right")]
    return vlo + (h - lo) * (vhi - vlo)


def fscore_grid(R, q=None, beta=0.5):
    """F-score over the grid (Q_test, Q_GT) from the R tensor (notebook 3), under both readings.

    For unit i: GT-Rs are R[i, :, i]; test-Rs are pooled over its surrogates k, the R of all
    surrogates of surrogate k's second-best unit with unit i's trace (compute_test_r). With
    unit i present, a surrogate whose best unit is i is TP when its R passes, else FN; one whose
    best unit is another is FP if its best R passes and TN if not (Methods 2.8, "methods") or
    FN (the code, "code"). With unit i removed, the best R of the other units passing is FP,
    else TN. Threshold: the larger of the two quantiles.
    Returns {reading: (F, counts)}, F indexed [Q_test, Q_GT], and "stats"."""
    if q is None:
        q = np.round(np.linspace(0, 1, 100), 3)
    n, S, _ = R.shape
    zeros = lambda: np.zeros((len(q), len(q)))
    c = {k: zeros() for k in ["TP", "FN_m", "FP_m", "TN_m", "FN_c", "FP_rem", "TN_rem"]}
    n_hit, gt_med, test_med = 0, [], []
    for i in range(n):
        Ri = R[i].astype(float)                      # surrogates x units
        Ri = np.where(np.isfinite(Ri), Ri, -np.inf)
        order = np.argsort(Ri, axis=1)
        best, second = order[:, -1], order[:, -2]
        best_r = Ri[np.arange(S), best]
        hit = best == i
        Rno = Ri.copy()
        Rno[:, i] = -np.inf
        nogt = Rno.max(axis=1)
        sb_counts = np.bincount(second, minlength=n)
        js = np.where(sb_counts > 0)[0]
        r1 = weighted_quantile(R[js, :, i].astype(float).ravel(), np.repeat(sb_counts[js], S), np.append(q, 0.5))
        r1, test_r_median = r1[:-1], r1[-1]
        r2 = np.nanquantile(R[i, :, i].astype(float), q)
        n_hit += int(hit.sum())
        gt_med.append(np.nanmedian(R[i, :, i].astype(float)))
        test_med.append(test_r_median)
        thr = np.maximum(r1[:, None], r2[None, :])  # [Q_test, Q_GT]

        def n_above(vals):
            vals = np.sort(vals)
            return len(vals) - np.searchsorted(vals, thr, side="right")

        tp = n_above(best_r[hit])
        miss_pass = n_above(best_r[~hit])
        fp_rem = n_above(nogt)
        c["TP"] += tp
        c["FN_m"] += hit.sum() - tp
        c["FP_m"] += miss_pass
        c["TN_m"] += (~hit).sum() - miss_pass
        c["FN_c"] += S - tp
        c["FP_rem"] += fp_rem
        c["TN_rem"] += S - fp_rem
    out = {}
    for reading in ["methods", "code"]:
        TP = c["TP"]
        if reading == "methods":
            FN, FP, TN = c["FN_m"], c["FP_m"] + c["FP_rem"], c["TN_m"] + c["TN_rem"]
        else:
            FN, FP, TN = c["FN_c"], c["FP_rem"], c["TN_rem"]
        with np.errstate(invalid="ignore", divide="ignore"):
            prec = TP / (TP + FP)
            rec = TP / (TP + FN)
            F = (1 + beta ** 2) * prec * rec / (beta ** 2 * prec + rec)
        out[reading] = (F, {"TP": TP, "FN": FN, "FP": FP, "TN": TN, "q": q})
    # share of surrogates whose best unit is their own unit (Methods 2.8 calls the others "rare"),
    # and the median over units of each unit's median GT-R and median test-R
    out["stats"] = {"hit_fraction": n_hit / (n * S), "gt_r_median": float(np.nanmedian(gt_med)),
                    "test_r_median": float(np.nanmedian(test_med))}
    return out


def grid_optimum(F, q=None):
    if q is None:
        q = np.round(np.linspace(0, 1, 100), 3)
    m = np.nanmax(F)
    a, b = np.where(F == m)
    return m, [(float(q[x]), float(q[y])) for x, y in zip(a, b)]   # (Q_test, Q_GT) pairs


def _tensor_rows(args):
    trains, t_frames, Z, pr, est, keep, seed, units = args
    out = np.empty((len(units), len(pr), Z.shape[0]), dtype=np.float32)
    for n, i in enumerate(units):
        rng = np.random.default_rng([seed, i])
        sur = surrogate_block(trains[i], t_frames, pr, est, rng)
        zs = zscore_rows(sur[:, keep]).astype(np.float32)
        out[n] = zs @ Z.T
    return out


def r_tensor_parallel(s, unit_dff, keep, pr, est, seed, workers=4, pool=None):
    """r_tensor computed in parallel over units; the same numbers as r_tensor."""
    t_frames = frame_sample_times(s)
    Z = zscore_rows(unit_dff[:, keep]).astype(np.float32)
    Z[~np.isfinite(Z)] = 0
    n = len(s["trains"])
    groups = [list(range(n))[g::workers * 2] for g in range(workers * 2)]
    jobs = [(s["trains"], t_frames, Z, pr, est, keep, seed, g) for g in groups if g]
    if pool is None:
        with ProcessPoolExecutor(workers) as ex:
            parts = list(ex.map(_tensor_rows, jobs))
    else:
        parts = list(pool.map(_tensor_rows, jobs))
    out = np.empty((n, len(pr), n), dtype=np.float32)
    for g, part in zip([g for g in groups if g], parts):
        out[g] = part
    return out


# ---------------------------------------------------------------------------------------------
# Readings of the best-R pipeline


P_THRESH = [96, 97, 98, 99]
STRATEGIES = ["pc", "hz"]


def spines(s):
    """Spine and shaft ROI indices of a file: ROIs come in the order spine, shaft (notebook 1)."""
    n = s["roi_traces"].shape[1]
    return [(k, 2 * k, 2 * k + 1) for k in range(n // 2)]


def best_r_readings(s, spine_roi, shaft_roi, smoothings=("span5", "frac")):
    """Best-R, best and second-best units, under every reading of the open burst details."""
    if "U" not in s:
        s["rates"], s["U"] = convolved_traces(s)
    tr = s["roi_traces"]
    dm, slope, offset = demix(dff(tr[:, spine_roi]), dff(tr[:, shaft_roi]))
    out = []
    for smo in smoothings:
        for strat in STRATEGIES:
            for p in P_THRESH:
                a, b, info = detect_bursts(s, p, strat, smo)
                keep = keep_frames(s, a, b)
                r = pearson_with_units(dm, s["U"], keep)
                order = rank_units(r)
                out.append({"smoothing": smo, "strategy": strat, "p_thresh": p,
                            "n_bursts": info["n_bursts"], "n_keep": len(keep),
                            "best": int(order[0]), "second": int(order[1]),
                            "best_R": float(r[order[0]]), "second_R": float(r[order[1]]),
                            "n_undefined": int(np.sum(~np.isfinite(r))),
                            "keep": keep, "r": r, "starts": a, "ends": b, "demixed": dm,
                            "slope": slope, "offset": offset})
    return out
