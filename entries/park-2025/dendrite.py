"""Loading and measures for dandiset 001266 (Park, Wong-Campos et al. 2025, Nat Commun 16, 1333).

The dandiset holds raw camera movies of Voltron2 fluorescence (`acquisition/camera_1`, uint16
counts) and the DAQ channels recorded with them (100 kHz): the 594 nm and 488 nm laser
modulation, the EFS trigger, and, in the patch clamp files, the amplifier outputs. It holds no
regions of interest, structural images, stimulus masks or pixel size, so every region here is
found from the movie's mean image.

Where each parameter comes from:

- UM_PER_PX = 0.65: Methods, Kymographs, "Typical segment size was 10 pixels (6.5 µm with 10x
  objective)" (camera pixel 6.5 µm, 10x objective, Methods, Optical system).
- SEGMENT_PX = 10: the same passage (kymograph segments of 10 pixels).
- Bleach correction: Methods, Extracting fluorescence from movies, "Photobleaching was corrected
  by dividing the frames by a regression fit to the mean fluorescence". The form of the fit is
  not given; a cubic polynomial in time fitted to frames outside the stimulus epochs is a
  standard choice. Depolarization is -dF/F (claims file header; Voltron2 fluorescence falls).
- High-pass filter: the claims file header, open item (1). Reading "median": subtract a 20 ms
  moving median; reading "butter": zero-phase 2nd order Butterworth high-pass at 20 Hz.
- Somatic spike threshold: claims file header, item (4), 5 times the robust s.d. (1.4826 MAD) of
  the filtered trace, with peaks at least 3 ms apart (a standard refractory choice); 4 s.d. is
  run as a variant, and assumed for the Fig. 3 counts (see the attempt record).
- dSpike threshold: claims file header, item (2), trough of the distal amplitude histogram
  (here `first_min_threshold`, the first minimum of a Gaussian kernel density above its lowest
  mode; an assumption, see its docstring), with the FWHM < 5 ms rule (Methods, Counting bAPs
  and dSpikes). Where the density has no minimum above the failure mode the threshold is
  undefined (nan).
- bAP to distal event: claims file header, item (3), the distal peak within 5 ms after the
  somatic peak.
- Distal region: trunk segments more than 300 µm from the soma along the traced trunk (Methods,
  Counting bAPs and dSpikes, "typically > 300 µm from soma"); for AUC, more than 200 µm (Fig. 5c
  legend). The trunk is traced on the mean image as the brightest ridge upward from the soma,
  in place of the line the authors drew by hand (Methods, Kymographs).
"""

import json
import os
from concurrent.futures import ProcessPoolExecutor

import h5py
import numpy as np
import remfile
import requests
from scipy import ndimage, signal, stats

DANDISET = "001266"
VERSION = "0.250710.0758"
API = "https://api.dandiarchive.org/api"
UM_PER_PX = 0.65
SEGMENT_PX = 10
CHUNK_FRAMES = 334
N_WORKERS = 16

_ASSETS = None


def assets():
    """All assets of the pinned version: list of dicts with path, asset_id, size."""
    global _ASSETS
    if _ASSETS is None:
        out, url = [], f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=200"
        while url:
            r = requests.get(url, timeout=60).json()
            out += r["results"]
            url = r["next"]
        _ASSETS = out
    return _ASSETS


def norm_name(name):
    """A file name as the index gives it (underscores, spaces, quotes) in DANDI's spelling."""
    n = name.strip().strip("'").strip()
    n = n[4:] if n.startswith("sub-") else n
    return n.replace("_", "-").replace(" ", "-")


def assets_for(key):
    """Assets whose subject folder is `sub-<key>`, or starts with it when key is a 6-digit stem."""
    k = norm_name(key)
    hits = [a for a in assets() if a["path"].split("/")[0] == "sub-" + k]
    if not hits:
        hits = [a for a in assets() if a["path"].split("/")[0].startswith("sub-" + k)]
    return sorted(hits, key=lambda a: a["path"])


def asset_for(key):
    """One asset for key; where a subject has two files, the one named with a session."""
    hits = assets_for(key)
    if not hits:
        raise KeyError(key)
    with_ses = [a for a in hits if "_ses-" in a["path"]]
    return (with_ses or hits)[0]


def s3_url(asset):
    r = requests.head(f"{API}/assets/{asset['asset_id']}/download/", allow_redirects=True, timeout=60)
    return r.url


def open_nwb(url):
    return h5py.File(remfile.File(url), "r")


def read_header(key):
    """Metadata, camera timestamps and DAQ channels (decimated to 10 kHz) of one file."""
    a = asset_for(key)
    url = s3_url(a)
    f = open_nwb(url)
    cam = f["acquisition/camera_1"]
    out = dict(key=key, path=a["path"], url=url,
               experiment=f["general/experiment_description"][()].decode(),
               shape=cam["data"].shape, chunks=cam["data"].chunks,
               cam_t=cam["timestamps"][:], daq={})
    for k in f["acquisition"]:
        if k.startswith("daq"):
            g = f["acquisition"][k]
            desc = g.attrs["description"]
            desc = desc.decode() if isinstance(desc, bytes) else desc
            rate = float(g["starting_time"].attrs["rate"])
            out["daq"][desc.split(":", 1)[1]] = dict(
                x=g["data"][::10].astype(np.float32), rate=rate / 10,
                t0=float(g["starting_time"][()]), unit=g["data"].attrs["unit"])
    f.close()
    return out


def _mean_job(args):
    url, a, b = args
    f = open_nwb(url)
    d = f["acquisition/camera_1/data"][a:b].astype(np.float64)
    return d.sum(0), d.shape[0]


def mean_image(hdr, n_frames=None):
    """Mean of the first n_frames frames (default one chunk)."""
    n = n_frames or hdr["chunks"][0]
    s, k = _mean_job((hdr["url"], 0, n))
    return s / k


def _extract_job(args):
    url, a, b, W, sta = args
    f = open_nwb(url)
    d = f["acquisition/camera_1/data"][a:b]
    d = d.reshape(d.shape[0], -1).astype(np.float32)
    tr = np.asarray(W @ d.T).T  # frames x rois
    if sta is None:
        return tr, None
    onset_frames, pre, post = sta
    acc = np.zeros((pre + post, d.shape[1]), np.float64)
    cnt = np.zeros(pre + post)
    for o in onset_frames:
        lo, hi = max(a, o - pre), min(b, o + post)
        if hi > lo:
            acc[lo - (o - pre):hi - (o - pre)] += d[lo - a:hi - a]
            cnt[lo - (o - pre):hi - (o - pre)] += 1
    return tr, (acc, cnt)


def extract(hdr, W, n_workers=N_WORKERS, sta=None):
    """Weighted ROI traces (frames x rois) from the whole movie, streamed in time slabs.

    W is a scipy.sparse matrix (rois x pixels) whose rows sum to 1. With sta = (onset frame
    indices, pre, post) it also returns the stimulus-triggered average movie (lags x pixels).
    """
    T = hdr["shape"][0]
    step = hdr["chunks"][0] * 2
    jobs = [(hdr["url"], a, min(a + step, T), W, sta) for a in range(0, T, step)]
    with ProcessPoolExecutor(n_workers) as ex:
        parts = list(ex.map(_extract_job, jobs))
    X = np.vstack([p[0] for p in parts])
    if sta is None:
        return X
    acc = sum(p[1][0] for p in parts)
    cnt = sum(p[1][1] for p in parts)
    return X, acc / np.maximum(cnt, 1)[:, None]


def _pixreg_job(args):
    url, a, b, r = args
    f = open_nwb(url)
    d = f["acquisition/camera_1/data"][a:b]
    dx = np.diff(d.reshape(d.shape[0], -1).astype(np.float64), axis=0)
    dr = np.diff(np.asarray(r[a:b], np.float64))
    return dx.T @ dr, (dx ** 2).sum(0), float(dr @ dr), len(dr)


def ml_weights(hdr, ref, n_workers=N_WORKERS):
    """Maximum-likelihood pixel weights (Methods, Extracting fluorescence from movies: "the
    fluorescence at each pixel was correlated with the whole-field average fluorescence. Pixels
    that showed stronger correlation to the mean were preferentially weighted", after Kralj et al.
    2012, ref. 33). Each pixel is regressed on the reference trace `ref` (the whole-field mean),
    x_i = a_i + b_i ref + e_i, and weighted by b_i / var(e_i), negative slopes set to zero. The
    regression uses frame-to-frame differences, so that the slow bleaching trend does not enter
    the slope or the noise variance (a choice made here; the paper gives no detail).
    Returns a 1 x pixels sparse matrix whose row sums to 1, for `extract`."""
    from scipy import sparse
    T = hdr["shape"][0]
    step = hdr["chunks"][0] * 2
    jobs = [(hdr["url"], a, min(a + step, T), ref) for a in range(0, T, step)]
    with ProcessPoolExecutor(n_workers) as ex:
        parts = list(ex.map(_pixreg_job, jobs))
    sxr = sum(p[0] for p in parts)
    sxx = sum(p[1] for p in parts)
    srr = sum(p[2] for p in parts)
    n = sum(p[3] for p in parts)
    b = sxr / srr
    var_e = np.maximum(sxx - b * sxr, 1e-12) / (2 * n)
    w = np.clip(b, 0, None) / var_e
    return sparse.csr_matrix((w / w.sum())[None, :].astype(np.float32))


def cell_traces(key, soma_lower=0.55, soma=None, sta=None, n_workers=N_WORKERS, trace=(4, 1.5)):
    """Header, mean image, soma, traced trunk, segment distances and traces of one file.

    Traces: column 0 is the soma (disk of radius 7 pixels), columns 1.. are the trunk segments,
    and the last column is the whole frame. `soma` (row, col) overrides the automatic soma, and
    `trace` = (window, sigma) sets the trunk tracer (a wider window follows a curved trunk).
    """
    h = read_header(key)
    m = mean_image(h)
    so = tuple(soma) if soma is not None else find_soma(m, lower=soma_lower)
    path = trace_trunk(m, so, window=trace[0], sigma=trace[1])
    masks, dist = segments(m, path)
    W = weights([soma_mask(m, so)] + masks + [np.ones(m.shape, bool)])
    out = dict(hdr=h, mean=m, soma=so, path=path, dist=dist)
    if sta is not None:
        X, movie = extract(h, W, n_workers, sta)
        out["sta_movie"] = movie
    else:
        X = extract(h, W, n_workers)
    out["X"] = X
    out["t"] = h["cam_t"]
    out["fs"] = 1 / np.median(np.diff(h["cam_t"]))
    return out


# ---------------------------------------------------------------- geometry

def find_soma(m, sigma=8, lower=0.55):
    """Soma centre: maximum of the mean image smoothed at sigma pixels, in the lower part of the
    frame (rows below `lower` of the height), where every cell here has its soma."""
    s = ndimage.gaussian_filter(m, sigma)
    r0 = int(lower * m.shape[0])
    r, c = np.unravel_index(np.argmax(s[r0:]), s[r0:].shape)
    return int(r + r0), int(c)


def trace_trunk(m, soma, start_offset=15, window=4, sigma=1.5, stop_row=0, waypoints=None):
    """Trace the apical trunk upward from the soma as the brightest ridge, row by row.

    Returns an array of (row, col) points, one per row, from the soma centre to stop_row.
    `waypoints` (row -> col) pins the trace at given rows, as a hand-drawn line would.
    """
    s = ndimage.gaussian_filter(m, sigma)
    r0, c = soma
    pts = [(r, c) for r in range(r0, r0 - start_offset, -1)]
    wp = dict(waypoints or {})
    for r in range(r0 - start_offset, stop_row - 1, -1):
        if r in wp:
            c = wp[r]
        else:
            lo, hi = max(0, c - window), min(m.shape[1], c + window + 1)
            c = lo + int(np.argmax(s[r, lo:hi]))
        pts.append((r, c))
    return np.array(pts)


def segments(m, path, seg_px=SEGMENT_PX, half_width=3):
    """Masks of seg_px-long segments along the path; returns (masks, distance_um of centres)."""
    d = np.r_[0, np.cumsum(np.hypot(*np.diff(path, axis=0).T))]
    nseg = int(d[-1] // seg_px)
    rr, cc = np.mgrid[:m.shape[0], :m.shape[1]]
    masks, dist = [], []
    for i in range(nseg):
        sel = path[(d >= i * seg_px) & (d < (i + 1) * seg_px)]
        mk = np.zeros(m.shape, bool)
        for r, c in sel:
            mk[max(0, r - 1):r + 2, max(0, c - half_width):c + half_width + 1] = True
        masks.append(mk)
        dist.append((i + 0.5) * seg_px * UM_PER_PX)
    return masks, np.array(dist)


def soma_mask(m, soma, radius=7):
    rr, cc = np.mgrid[:m.shape[0], :m.shape[1]]
    return (rr - soma[0]) ** 2 + (cc - soma[1]) ** 2 <= radius ** 2


def weights(masks):
    from scipy import sparse
    M = np.array([mk.ravel() for mk in masks], dtype=np.float32)
    M /= M.sum(1, keepdims=True)
    return sparse.csr_matrix(M)


# ---------------------------------------------------------------- traces

def frame_times(hdr):
    return hdr["cam_t"]


def onsets(hdr, channel, thr=None):
    """Rising edges of a DAQ channel, in seconds."""
    ch = hdr["daq"][channel]
    x = ch["x"]
    thr = (x.max() + x.min()) / 2 if thr is None else thr
    on = np.flatnonzero(np.diff((x > thr).astype(int)) == 1) + 1
    off = np.flatnonzero(np.diff((x > thr).astype(int)) == -1) + 1
    return ch["t0"] + on / ch["rate"], ch["t0"] + off / ch["rate"]


def bleach_correct(F, t, exclude=None, deg=3):
    """-dF/F after dividing by a cubic fit to the trace (frames in `exclude` left out of the fit)."""
    keep = np.ones(len(t), bool) if exclude is None else ~exclude
    tt = (t - t.mean()) / t.std()
    out = np.empty_like(F, dtype=np.float64)
    F2 = F if F.ndim == 2 else F[:, None]
    out = out if F.ndim == 2 else out[:, None]
    for j in range(F2.shape[1]):
        p = np.polyfit(tt[keep], F2[keep, j], deg)
        fit = np.polyval(p, tt)
        out[:, j] = -(F2[:, j] / fit - 1)
    return out if F.ndim == 2 else out[:, 0]


def highpass(x, fs, reading="median"):
    """High-pass filter of a trace (or frames x rois): readings 'median' and 'butter'."""
    if reading == "median":
        k = int(round(0.020 * fs)) | 1
        if x.ndim == 1:
            return x - ndimage.median_filter(x, size=k, mode="nearest")
        return x - ndimage.median_filter(x, size=(k, 1), mode="nearest")
    b, a = signal.butter(2, 20, btype="highpass", fs=fs)
    return signal.filtfilt(b, a, x, axis=0)


def robust_sd(x):
    return 1.4826 * np.median(np.abs(x - np.median(x)))


def detect_spikes(x, fs, k=5.0, min_sep_ms=3.0):
    """Indices of peaks above k robust s.d. (threshold-and-maximum)."""
    thr = k * robust_sd(x)
    pk, _ = signal.find_peaks(x, height=thr, distance=max(1, int(min_sep_ms / 1000 * fs)))
    return pk, thr


def distal_events(xd, spikes, fs, win_ms=5.0):
    """For each somatic spike, the distal peak amplitude and its index within win_ms after it."""
    w = int(round(win_ms / 1000 * fs))
    amp, idx = [], []
    for s in spikes:
        seg = xd[s:s + w + 1]
        j = int(np.argmax(seg))
        amp.append(seg[j])
        idx.append(s + j)
    return np.array(amp), np.array(idx)


def fwhm_ms(x, i, fs, max_ms=30.0):
    """Full width at half maximum (ms) of the peak at index i of trace x (baseline 0), with the
    half-maximum crossings interpolated linearly between frames."""
    h = x[i] / 2
    w = int(max_ms / 1000 * fs)
    lo = i
    while lo > max(0, i - w) and x[lo] > h:
        lo -= 1
    hi = i
    while hi < min(len(x) - 1, i + w) and x[hi] > h:
        hi += 1
    left = lo + (h - x[lo]) / (x[lo + 1] - x[lo]) if x[lo + 1] != x[lo] else lo
    right = hi - 1 + (x[hi - 1] - h) / (x[hi - 1] - x[hi]) if x[hi - 1] != x[hi] else hi
    return (right - left) / fs * 1000


def trough_threshold(a, grid=512):
    """Threshold at the density minimum between the two highest modes of a KDE of amplitudes.

    Returns (threshold, n_modes). With fewer than two modes returns (nan, n_modes).
    """
    a = np.asarray(a, float)
    a = a[np.isfinite(a)]
    if len(a) < 5:
        return np.nan, 0
    kde = stats.gaussian_kde(a)
    g = np.linspace(a.min(), a.max(), grid)
    y = kde(g)
    pk, _ = signal.find_peaks(y)
    if len(pk) < 2:
        return np.nan, len(pk)
    top = np.sort(pk[np.argsort(y[pk])[-2:]])
    j = top[0] + int(np.argmin(y[top[0]:top[1] + 1]))
    return g[j], len(pk)


# ---------------------------------------------------------------- bAPs and dSpikes

def stim_onsets(hdr, channel="mod488"):
    on, off = onsets(hdr, channel)
    return on, off


def corrected(o, reading="median"):
    """(-dF/F, high-passed -dF/F) for every column of o['X']."""
    Y = bleach_correct(o["X"], o["t"])
    return Y, highpass(Y, o["fs"], reading)


def distal_trace(H, dist, lo_um=300.0, hi_um=np.inf):
    """Mean of the trunk segment columns of H (H[:, 1:-1]) whose distance is in [lo, hi)."""
    sel = (dist > lo_um) & (dist < hi_um)
    return H[:, 1:-1][:, sel].mean(1), int(sel.sum())


def bap_table(o, on, reading="median", window_s=(0.0, 0.06), distal_um=300.0, distal_hi_um=np.inf,
              k=5.0):
    """One row per somatic spike within `window_s` of a stimulus onset.

    Columns: trial, order (0 = first bAP of the trial), t_ms (peak after onset), soma (high-passed
    -dF/F at the peak), distal (largest high-passed distal -dF/F within 5 ms after the somatic
    peak), fwhm_ms (of that distal peak) and frame (somatic peak frame).
    """
    import pandas as pd
    Y, H = corrected(o, reading)
    fs, t = o["fs"], o["t"]
    pk, thr = detect_spikes(H[:, 0], fs, k=k)
    xd, nseg = distal_trace(H, o["dist"], distal_um, distal_hi_um)
    rows = []
    for i, s in enumerate(on):
        sel = pk[(t[pk] >= s + window_s[0]) & (t[pk] < s + window_s[1])]
        amp, idx = distal_events(xd, sel, fs)
        for j, (p, a, q) in enumerate(zip(sel, amp, idx)):
            rows.append(dict(trial=i, order=j, t_ms=(t[p] - s) * 1000, soma=H[p, 0], distal=a,
                             fwhm_ms=fwhm_ms(xd, q, fs), frame=int(p), distal_frame=int(q)))
    df = pd.DataFrame(rows, columns=["trial", "order", "t_ms", "soma", "distal", "fwhm_ms", "frame",
                                     "distal_frame"])
    df.attrs.update(soma_threshold=thr, n_soma_spikes=len(pk), n_distal_segments=nseg)
    return df


def first_min_threshold(a, bw="scott", grid=1000):
    """dSpike threshold: the first minimum of the amplitude density (Gaussian KDE) above its
    lowest mode, the trough that closes the failure mode (claims file header, item 2, "a threshold
    between the two modes"). The failure mode is the lowest-amplitude density peak at least a
    quarter as high as the highest peak (so that a few outlying low amplitudes are not taken
    for it, and a recording with more dSpikes than failures still gets its trough). Above the
    failure mode any density minimum counts, whatever the height of the bump beyond it: a
    small group of large amplitudes, which is what a few dSpikes among many failures look like
    (8 of 110 bAPs in Fig. 2), gets a threshold, and so do two outlying amplitudes (on 100
    failures around 0.4 and 2 values near 1, the threshold is about 0.7 to 0.8). `trough_support`
    reports, per recording, how many amplitudes lie above the threshold and how high the bump
    beyond it is, so that a threshold resting on a few outliers can be seen. Both choices are
    assumptions: the paper set its thresholds by hand.

    Returns nan when no density minimum lies above the failure mode (the density falls
    monotonically from it): then no trough separates dSpikes from failures, and the dSpike count
    of that recording is undefined (the notebook reports it as such, not as zero dSpikes)."""
    a = np.asarray(a, float)
    if len(a) < 5 or np.ptp(a) == 0:
        return np.nan
    kde = stats.gaussian_kde(a, bw_method=bw)
    g = np.linspace(a.min(), a.max(), grid)
    y = kde(g)
    modes, _ = signal.find_peaks(y)
    modes = modes[y[modes] >= 0.25 * y.max()]  # bumps of a few outlying amplitudes are not modes
    low = int(modes[0]) if len(modes) else int(np.argmax(y))
    mins, _ = signal.find_peaks(-y)
    mins = mins[mins > low]
    return (g[mins[0]] if len(mins) else np.nan)


def trough_support(a, thr, bw="scott", grid=1000):
    """What lies above a `first_min_threshold` trough: the number of amplitudes above it, and the
    highest density peak above it as a fraction of the highest peak overall (the rule's quarter
    applies to the failure mode only). nan, 0 when there is no threshold."""
    a = np.asarray(a, float)
    if not np.isfinite(thr) or len(a) < 5:
        return np.nan, 0
    kde = stats.gaussian_kde(a, bw_method=bw)
    g = np.linspace(a.min(), a.max(), grid)
    y = kde(g)
    return float(y[g > thr].max() / y.max()), int((a > thr).sum())


def mark_dspikes(df, threshold, max_fwhm_ms=5.0):
    """Flag bAPs whose distal amplitude exceeds threshold with a distal FWHM under 5 ms."""
    df = df.copy()
    df["dspike"] = (df.distal > threshold) & (df.fwhm_ms < max_fwhm_ms)
    return df


def calls(o, on, reading="median", k=5.0, distal_hi_um=np.inf, window_s=(0.0, 0.06),
          threshold=None):
    """bAP table with dSpike flags; the threshold is the recording's own trough unless given."""
    df = bap_table(o, on, reading, window_s, 300.0, distal_hi_um, k)
    thr = first_min_threshold(df.distal.values) if threshold is None else threshold
    df = mark_dspikes(df, thr)
    df.attrs["dspike_threshold"] = thr
    return df


READINGS = [(r, k, hi) for r in ("median", "butter") for k in (5.0, 4.0) for hi in (np.inf, 400.0)]


def reading_name(r, k, hi):
    return f"{r}, k={k:g}, distal {'>300' if not np.isfinite(hi) else '300-400'} um"


def frame_of(t, times):
    return np.searchsorted(t, times)


def segment_amplitudes(Y, df, on_frames, fs, peak_frames=3, pre_frames=10):
    """Per bAP and trunk segment: peak -dF/F (max over the somatic peak frame and the next
    `peak_frames` frames) and the reference amplitude (mean from 10 to 20 ms after the somatic
    peak, Fig. 1d legend), both relative to the trial's pre-stimulus baseline (mean of the
    `pre_frames` frames before onset). Y holds the segment columns only."""
    r0, r1 = int(round(0.010 * fs)), int(round(0.020 * fs))
    amp, ref = [], []
    for row in df.itertuples():
        o = on_frames[row.trial]
        base = Y[max(0, o - pre_frames):o].mean(0)
        amp.append(Y[row.frame:row.frame + peak_frames + 1].max(0) - base)
        ref.append(Y[row.frame + r0:row.frame + r1 + 1].mean(0) - base)
    return np.array(amp), np.array(ref)


def exp_fit(x, y, offset=False):
    """Least-squares fit of A exp(-x/lam) (+ c); returns lam (µm) or nan when it fails."""
    from scipy.optimize import curve_fit
    try:
        if offset:
            f = lambda x, A, lam, c: A * np.exp(-x / lam) + c
            p0 = [y[0] - y[-1], 200.0, y[-1]]
            bounds = ([-np.inf, 1.0, -np.inf], [np.inf, 1e5, np.inf])
        else:
            f = lambda x, A, lam: A * np.exp(-x / lam)
            p0 = [y[0], 200.0]
            bounds = ([-np.inf, 1.0], [np.inf, 1e5])
        p, _ = curve_fit(f, x, y, p0=p0, bounds=bounds, maxfev=5000)
        return p[1]
    except Exception:
        return np.nan


def independent_distal_events(H, dist, thr, fs, max_fwhm_ms=5.0, lo_um=300.0, hi_um=np.inf):
    """Distal events found without reference to the soma: peaks of the high-passed distal trace
    above `thr` with FWHM under 5 ms (at least 3 ms apart). Returns their frames."""
    xd, _ = distal_trace(H, dist, lo_um, hi_um)
    pk, _ = signal.find_peaks(xd, height=thr, distance=max(1, int(0.003 * fs)))
    return np.array([p for p in pk if fwhm_ms(xd, p, fs) < max_fwhm_ms], int)


def depolarization_onset(y, on_frames, fs, pre=20, post=60, nsd=2.0):
    """First frame after onset at which the stimulus-triggered average of y exceeds the mean of
    its pre-stimulus baseline by nsd s.d.; returns (ms after onset, average trace)."""
    seg = np.array([y[o - pre:o + post] for o in on_frames if o - pre >= 0 and o + post <= len(y)])
    a = seg.mean(0)
    b = a[:pre]
    above = np.flatnonzero(a[pre:] > b.mean() + nsd * b.std())
    return (above[0] / fs * 1000 if len(above) else np.nan), a


def stim_contrast(y, on_frames, fs, shift_ms=100.0, win_ms=(0, 30), pre_ms=10):
    """Mean response (y over win after onset minus y over pre_ms before) at the true onsets and at
    onsets shifted by shift_ms; a response locked to the stimulus appears only at the true ones."""
    def resp(frames):
        w0, w1 = int(win_ms[0] / 1000 * fs), int(win_ms[1] / 1000 * fs)
        p = int(pre_ms / 1000 * fs)
        v = [y[f + w0:f + w1].mean() - y[f - p:f].mean() for f in frames if f - p >= 0 and f + w1 <= len(y)]
        return float(np.mean(v)) if v else np.nan
    sh = (on_frames + int(shift_ms / 1000 * fs))
    return resp(on_frames), resp(sh)


def auc(y, t, t_on, t_end, reading="a", pre_s=0.1):
    """Area of -dF/F (y) from t_on, relative to the mean over pre_s before t_on (in %·s).

    Reading 'a': the maximum of the cumulative area before t_end (the cumulative curve of Fig.
    S22a stops rising); reading 'b': the area from t_on to t_end."""
    i0, i1 = np.searchsorted(t, [t_on, t_end])
    b0 = np.searchsorted(t, t_on - pre_s)
    base = y[b0:i0].mean()
    dt = np.median(np.diff(t))
    c = np.cumsum((y[i0:i1] - base) * dt) * 100
    return float(c.max()) if reading == "a" else float(c[-1])


def above_half_duration_ms(y, t, t_on, t_end, pre_s=0.1, smooth_ms=5.0):
    """Time (ms) the smoothed trace stays above half its peak (relative to pre-stimulus baseline)
    around its peak between t_on and t_end."""
    fs = 1 / np.median(np.diff(t))
    ys = ndimage.uniform_filter1d(y, max(1, int(smooth_ms / 1000 * fs)))
    i0, i1 = np.searchsorted(t, [t_on, t_end])
    b0 = np.searchsorted(t, t_on - pre_s)
    z = ys[i0:i1] - ys[b0:i0].mean()
    j = int(np.argmax(z))
    h = z[j] / 2
    lo = j
    while lo > 0 and z[lo] > h:
        lo -= 1
    hi = j
    while hi < len(z) - 1 and z[hi] > h:
        hi += 1
    return (hi - lo) / fs * 1000, z[j]
