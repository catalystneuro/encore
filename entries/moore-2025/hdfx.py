"""Loading and head-direction measures for dandiset 001699.

Moore, Duszkiewicz, Asiminas, Dudchenko, Peyrache & Wood, "Age-dependent alterations in the
head-direction signal in a rat model of Fragile X Syndrome", bioRxiv
doi:10.1101/2025.01.09.632139 (version 1, January 2025; version 2, January 2026, is a revision).

Each NWB file holds one recording day of one rat: spike times and mean waveforms of every
curated unit (`units`), head direction (radians) and head position (centimetres in most files)
at about 40 Hz, an `epochs` table, `sleep_stages` intervals tagged wake, nrem or rem, a
pseudo-EMG, the LFP and the raw signal. Files are streamed from the archive at the pinned
version; only the units, tracking, intervals and pseudo-EMG are read, and nothing is written to
disk.

Where the parameters come from:

- Paper, version 1 Methods: putative excitatory cells by trough-to-peak duration (> 0.5 ms in
  juveniles, > 0.4 ms in adults); at least 100 spikes in the analysed epoch; contamination
  score from the autocorrelogram (0 to 1 ms bin over the maximum within 0 to 100 ms); periods
  of more than 1 s without tracking excluded; tuning curves in 1 degree bins smoothed with a
  6 degree SD Gaussian, from times when speed exceeds 1 cm/s (2 cm/s for decoding and Isomap);
  half-width; HD information with occupancy; tuning-curve cross-correlation offsets; Isomap
  population vectors (200 ms bins, 400 ms SD smoothing, square root, z-score, unit norm),
  kernel PCA with a Laplacian kernel to 6 components, Isomap with 30 neighbours to 2
  dimensions, directionality by the smaller circular variance of the error, Isomap tuning
  curves in 6 degree bins with 12 degree SD smoothing, real-HD comparison curves from HD
  downsampled to 200 ms.
- Paper, version 2 Methods (the same paper revised; version 1 does not describe the decoder):
  Bayesian decoding on 200 ms bins smoothed with a 400 ms SD Gaussian, tuning curves from the
  first half of the exploration epoch, decoding of the second half, decoder error denoised with
  a Hampel filter (5 s window, 1 SD) and smoothed with a 0.8 s SD Gaussian, sessions with fewer
  than 6 cells excluded; speed as the difference of successive positions smoothed with a 0.25 s
  moving average. Version 2 uses uniform occupancy for HD information
  (`hd_info(..., uniform=True)`), shown as a variant.
- The lab's package woodcode (https://github.com/Wood-Dudchenko-lab/woodcode, commit
  61ee1784ef8bdeed1befa4d2dd2dd71dc8befd60), linked from the dandiset: trough-to-peak duration
  on the channel with the largest waveform energy, with waveforms whose first quarter is lower
  on average than their second quarter treated as positive (no duration); circular smoothing
  of tuning curves with NaN bins interpolated; Skaggs information; Rayleigh vector length;
  the Poisson decoder.
- Common choices where neither says: the half maximum is half the peak rate; a curve that
  never falls below it has half-width 360 degrees; tracking gaps up to 1 s are interpolated;
  for the two files with positions in pixels, the scale makes the x extent of the exploration
  tracking equal to the 73 cm arena diameter; each exploration session is the first 20 min (`SESSION_S`, the paper's session
  length) of its tracking block. This departs from the claims file, which cuts only blocks over 30 min
  (to 1300 s); its definition is computed as a variant (`rule="claims"`).
"""

from __future__ import annotations

from concurrent.futures import ProcessPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy import stats
from scipy.ndimage import gaussian_filter1d

DANDISET_ID = "001699"
DANDISET_VERSION = "0.260917.2322"

ARENA_DIAMETER_CM = 73.0
TTP_THRESHOLD_MS = {"juvenile": 0.5, "adult": 0.4}
MIN_SPIKES = 100
MAX_GAP_S = 1.0
SPEED_TC = 1.0            # cm/s, tuning curves (v1)
SPEED_POP = 2.0           # cm/s, decoding and Isomap (v1)
SPEED_SMOOTH_S = 0.25     # moving average (v2)
TC_BINS, TC_SIGMA = 360, 6.0          # 1 degree bins, 6 degree SD
ISO_BINS, ISO_SIGMA = 60, 2.0         # 6 degree bins, 12 degree SD (2 bins)
POP_BIN_S, POP_SMOOTH_S = 0.2, 0.4
ISOMAP_NEIGHBOURS, KPCA_COMPONENTS = 30, 6
ISOMAP_FIT_MAX = None     # fit on every bin, as in the paper; a number fits on that many bins
MIN_CELLS_POP = 6
HAMPEL_WINDOW_S, DRIFT_SMOOTH_S = 5.0, 0.8
SESSION_S = 1200.0        # 20 min sessions (paper v1); longer tracking blocks are cut
MIN_SESSION_S = 600.0
CLAIMS_CUT = (1800.0, 1300.0)   # the claims file's rule: a block over 30 min is cut to its first 1300 s


# --- loading --------------------------------------------------------------------------------

def list_assets():
    """NWB assets of the pinned version: path and asset id."""
    with DandiAPIClient() as client:
        ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        rows = [{"path": a.path, "asset_id": a.identifier, "size": a.size}
                for a in ds.get_assets() if a.path.endswith(".nwb")]
    return pd.DataFrame(rows).sort_values("path").reset_index(drop=True)


def _url(asset_id):
    return f"https://api.dandiarchive.org/api/assets/{asset_id}/download/"


def _str(x):
    return x.decode() if isinstance(x, bytes) else str(x)


def _tagged(group):
    tags = [_str(t) for t in group["tags"][:]]
    out, start = [], 0
    for stop in group["tags_index"][:]:
        out.append(",".join(tags[start:stop]))
        start = stop
    return pd.DataFrame({"start": group["start_time"][:], "stop": group["stop_time"][:], "tag": out})


def _series_times(series, n):
    if "timestamps" in series:
        return series["timestamps"][:]
    st = series["starting_time"]
    return st[()] + np.arange(n) / st.attrs["rate"]


def trough_to_peak(waveforms, sampling_rate):
    """woodcode get_waveform_features: duration in ms on the channel of largest energy; NaN
    for waveforms whose first quarter is lower on average than the second (positive). Channels
    stored as NaN are skipped; a unit whose waveform is NaN on every channel has no duration."""
    energy = np.nan_to_num((waveforms ** 2).sum(axis=1), nan=-1.0)  # NaN channels never chosen
    best = waveforms[np.arange(len(waveforms)), :, energy.argmax(axis=1)]
    n = best.shape[1]
    trough = best.argmin(axis=1)
    peak = np.array([t + best[i, t:].argmax() for i, t in enumerate(trough)])
    ttp = (peak - trough) / sampling_rate * 1000.0
    positive = best[:, : n // 4].mean(axis=1) < best[:, n // 4: n // 2].mean(axis=1)
    ttp[positive | np.isnan(best).any(axis=1)] = np.nan
    return ttp, positive


def contamination(spikes, max_lag=0.1, bin_s=0.001):
    """Autocorrelogram 0 to 1 ms bin over the largest bin within 0 to 100 ms (paper v1)."""
    counts = np.zeros(int(round(max_lag / bin_s)))
    k = 1
    while k < len(spikes):
        d = spikes[k:] - spikes[:-k]
        d = d[d < max_lag]
        if len(d) == 0:
            break
        counts += np.bincount((d / bin_s).astype(int), minlength=len(counts))[: len(counts)]
        k += 1
    return counts[0] / counts.max() if counts.max() > 0 else np.nan


def load_session(asset_id):
    """Everything the analysis uses from one file, reduced as it loads."""
    f = h5py.File(remfile.File(_url(asset_id)), "r")
    g = f["general/subject"]
    s = {"asset_id": asset_id,
         "subject": _str(g["subject_id"][()]), "genotype": _str(g["genotype"][()]),
         "date_of_birth": _str(g["date_of_birth"][()])[:10] if "date_of_birth" in g else None,
         "age": _str(g["age"][()]) if "age" in g else None,
         "session_id": _str(f["general/session_id"][()]),
         "session_start": _str(f["session_start_time"][()])[:10],
         "session_description": _str(f["session_description"][()])}
    acq = f.get("acquisition", {})
    s["histology"] = sorted(acq["histology_images"].keys()) if "histology_images" in acq else []
    s["epochs"] = _tagged(f["intervals/epochs"])
    s["sleep_stages"] = _tagged(f["intervals/sleep_stages"])
    tasks = f["processing/tasks"]
    s["task_epochs"] = {k: [_str(x) for x in tasks[k]["task_epochs"][:].ravel()] for k in tasks}
    hd = f["processing/behavior/CompassDirection/head-direction"]
    s["hd"] = hd["data"][:]
    s["t"] = _series_times(hd, len(s["hd"]))
    pos = f["processing/behavior/Position/position"]
    s["pos"] = pos["data"][:]
    s["pos_t"] = _series_times(pos, len(s["pos"]))
    s["pos_unit"] = _str(pos["data"].attrs["unit"])
    emg = f["processing/ecephys/pseudoEMG"]
    s["emg"] = emg["data"][:]
    s["emg_t"] = _series_times(emg, len(s["emg"]))
    u = f["units"]
    st, idx = u["spike_times"][:], u["spike_times_index"][:]
    raw = np.split(st, idx[:-1])
    s["n_unsorted_units"] = int(sum(bool(np.any(np.diff(x) < 0)) for x in raw))
    s["spikes"] = [np.sort(x) for x in raw]
    s["unit_ids"] = u["id"][:]
    s["unit_columns"] = sorted(u.keys())
    wf = u["waveform_mean"][:]
    sr = float(u["sampling_rate"][0])
    s["sampling_rate"] = sr
    s["ttp"], s["positive"] = trough_to_peak(wf, sr)
    s["n_channels"] = wf.shape[2]
    s["contamination"] = np.array([contamination(x) for x in s["spikes"]])
    s["n_spikes_total"] = int(len(st))
    s["spike_checksum"] = float(np.round(st[:: max(1, len(st) // 1000)].sum(), 6))
    return s


def load_all(asset_ids, workers=4):
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(load_session, asset_ids))


# --- tracking -------------------------------------------------------------------------------

def tracking(s, px_scale=None):
    """Frame times, HD (0 to 2 pi, short gaps interpolated), speed (cm/s) and a validity mask
    (False inside gaps longer than MAX_GAP_S). Frames whose timestamp does not increase are
    dropped."""
    order = np.r_[True, s["t"][1:] > np.maximum.accumulate(s["t"])[:-1]]  # drop repeated or backward frames
    t = s["t"][order]
    hd = np.mod(s["hd"][order], 2 * np.pi)
    ok = ~np.isnan(hd)
    valid = ok.copy()
    if (~ok).any():
        # runs of missing frames longer than MAX_GAP_S stay invalid; shorter ones are filled
        edges = np.diff(np.r_[0, (~ok).astype(int), 0])
        for a, b in zip(np.where(edges == 1)[0], np.where(edges == -1)[0]):
            lo, hi = max(a - 1, 0), min(b, len(t) - 1)
            if t[hi] - t[lo] <= MAX_GAP_S and ok[lo] and ok[hi]:
                valid[a:b] = True
        c = np.interp(t, t[ok], np.cos(hd[ok]))
        sn = np.interp(t, t[ok], np.sin(hd[ok]))
        hd = np.mod(np.arctan2(sn, c), 2 * np.pi)
    xy = s["pos"].astype(float)
    if np.array_equal(s["pos_t"], s["t"]):
        xy = xy[order]
    else:
        xy = np.column_stack([np.interp(t, s["pos_t"], xy[:, i]) for i in range(2)])
    pok = ~np.isnan(xy[:, 0])
    xy = np.column_stack([np.interp(t, t[pok], xy[pok, i]) for i in range(2)])
    if px_scale is not None:
        xy = xy / px_scale
    dt = np.median(np.diff(t))
    step = np.r_[0.0, np.hypot(*np.diff(xy, axis=0).T)] / np.maximum(np.r_[dt, np.diff(t)], 1e-9)
    w = max(1, int(round(SPEED_SMOOTH_S / dt)))
    speed = pd.Series(step).rolling(w, center=True, min_periods=1).mean().to_numpy()
    return {"t": t, "hd": hd, "xy": xy, "speed": speed, "valid": valid & pok, "dt": dt}


def tracking_blocks(t, gap=5.0):
    """Runs of tracking frames separated by gaps of more than `gap` seconds."""
    br = np.where(np.diff(t) > gap)[0]
    return list(zip(np.r_[t[0], t[br + 1]], np.r_[t[br], t[-1]]))


def exploration_sessions(s, rule="20min"):
    """The first tracking block of at least MIN_SESSION_S (session 1) and the first such block
    starting at least 60 min later (session 2, after the sleep), each cut to its first
    SESSION_S seconds (rule "20min"), or with rule "claims" cut to CLAIMS_CUT[1] seconds only
    when longer than CLAIMS_CUT[0], as the claims file defines them."""
    blocks = [(a, b) for a, b in tracking_blocks(s["t"]) if b - a >= MIN_SESSION_S]
    out = []
    if blocks:
        out.append(blocks[0])
        later = [blk for blk in blocks[1:] if blk[0] - blocks[0][0] >= 3600]
        if later:
            out.append(later[0])
    if rule == "claims":
        return [(a, a + CLAIMS_CUT[1] if b - a > CLAIMS_CUT[0] else b) for a, b in out]
    return [(a, min(b, a + SESSION_S)) for a, b in out]


def pixel_scale(s, sessions):
    """Pixels per cm for files whose positions are in pixels, from the arena diameter."""
    m = np.zeros(len(s["t"]), bool)
    for a, b in sessions:
        m |= (s["t"] >= a) & (s["t"] <= b)
    x = s["pos"][m, 0] if np.array_equal(s["pos_t"], s["t"]) else s["pos"][:, 0]
    return (np.nanmax(x) - np.nanmin(x)) / ARENA_DIAMETER_CM


# --- tuning ---------------------------------------------------------------------------------

def smooth_circular(arr, sigma_bins):
    """woodcode smooth_1d_tuning_curves(circular=True, nan_handling='interpolate'); rows are bins."""
    arr = np.array(arr, float, ndmin=2)
    if arr.shape[0] == 1:
        arr = arr.T
    x = np.arange(arr.shape[0])
    for i in range(arr.shape[1]):
        bad = np.isnan(arr[:, i])
        if bad.any() and (~bad).any():
            arr[:, i] = np.interp(x, x[~bad], arr[~bad, i])
    return gaussian_filter1d(arr, sigma_bins, axis=0, mode="wrap")


def frame_counts(spikes, t, dt):
    """Spike counts per tracking frame, frame i covering t[i] - dt/2 to t[i] + dt/2. Each frame
    is counted on its own window, so the frames need not be contiguous (speed-filtered)."""
    out = np.zeros((len(spikes), len(t)))
    for i, sp in enumerate(spikes):
        out[i] = np.searchsorted(sp, t + dt / 2) - np.searchsorted(sp, t - dt / 2)
    return out


def tuning_curves(angle, counts, dt, n_bins=TC_BINS, sigma_deg=TC_SIGMA):
    """Rate per angular bin (Hz), smoothed; and occupancy in seconds."""
    b = np.minimum((np.mod(angle, 2 * np.pi) / (2 * np.pi) * n_bins).astype(int), n_bins - 1)
    occ = np.bincount(b, minlength=n_bins) * dt
    sc = np.array([np.bincount(b, weights=c, minlength=n_bins) for c in counts]).T
    with np.errstate(invalid="ignore", divide="ignore"):
        rate = sc / occ[:, None]
    rate[occ == 0] = np.nan
    return smooth_circular(rate, sigma_deg / (360.0 / n_bins)), occ


def hd_info(tc, occ, uniform=False):
    """Skaggs information (bits per spike) per column; occupancy-weighted unless uniform."""
    p = np.full(tc.shape[0], 1.0 / tc.shape[0]) if uniform else occ / occ.sum()
    mean = p @ tc
    with np.errstate(invalid="ignore", divide="ignore"):
        r = tc / mean
        c = np.where(r > 0, p[:, None] * r * np.log2(r), 0.0)
    return np.nansum(c, axis=0)


def half_width(tc):
    """Twice the angle from the peak to the half-maximal rate on the mean of the two sides."""
    n = tc.shape[0]
    out = np.zeros(tc.shape[1])
    for i in range(tc.shape[1]):
        y = np.roll(tc[:, i], -int(np.argmax(tc[:, i])))
        side = (y[: n // 2 + 1] + np.r_[y[0], y[::-1][: n // 2]]) / 2
        below = np.where(side <= side[0] / 2)[0]
        out[i] = 2 * below[0] * 360.0 / n if len(below) else 360.0
    return out


def vector_length(tc):
    ang = (np.arange(tc.shape[0]) + 0.5) * 2 * np.pi / tc.shape[0]
    return np.abs(np.exp(1j * ang) @ tc) / tc.sum(axis=0)


def peak_rate(tc):
    return np.nanmax(tc, axis=0)


def offset_deg(tc1, tc2):
    """Absolute circular shift (degrees) of tc2 that maximises its Pearson correlation with tc1."""
    n = tc1.shape[0]
    with np.errstate(invalid="ignore", divide="ignore"):
        a = (tc1 - tc1.mean(0)) / tc1.std(0)
    out = np.zeros(tc1.shape[1])
    for i in range(tc1.shape[1]):
        b = tc2[:, i]
        if not np.isfinite(a[:, i]).all() or not np.all(np.isfinite(b)) or b.std() == 0:
            out[i] = np.nan
            continue
        b = (b - b.mean()) / b.std()
        # correlation for every circular shift through the FFT
        xc = np.real(np.fft.ifft(np.fft.fft(a[:, i]).conj() * np.fft.fft(b))) / n
        k = int(np.argmax(xc))
        out[i] = abs(((k + n / 2) % n) - n / 2) * 360.0 / n
    return out


# --- population -----------------------------------------------------------------------------

def pop_bins(spikes, a, b, bin_s=POP_BIN_S, smooth_s=POP_SMOOTH_S, raw=False):
    """Spike counts in bins of bin_s between a and b, smoothed with a Gaussian of SD smooth_s
    (and the raw counts if raw)."""
    edges = np.arange(a, b + bin_s / 2, bin_s)
    c = np.array([np.histogram(sp, edges)[0] for sp in spikes], float).T.reshape(len(edges) - 1, len(spikes))
    sm = gaussian_filter1d(c, smooth_s / bin_s, axis=0, mode="nearest")
    centres = (edges[:-1] + edges[1:]) / 2
    return (centres, sm, c) if raw else (centres, sm)


def bin_angle(track, centres, bin_s=POP_BIN_S):
    """Circular mean HD, mean speed and validity of the frames inside each population bin."""
    idx = np.searchsorted(centres - bin_s / 2, track["t"], side="right") - 1
    inside = (idx >= 0) & (idx < len(centres)) & (track["t"] < centres[np.clip(idx, 0, len(centres) - 1)] + bin_s / 2)
    n = len(centres)
    i = idx[inside]
    cs = np.bincount(i, np.cos(track["hd"][inside]), n)
    sn = np.bincount(i, np.sin(track["hd"][inside]), n)
    sp = np.bincount(i, track["speed"][inside], n)
    cnt = np.bincount(i, minlength=n)
    vcnt = np.bincount(i, track["valid"][inside].astype(float), n)
    with np.errstate(invalid="ignore", divide="ignore"):
        return np.mod(np.arctan2(sn, cs), 2 * np.pi), sp / cnt, (cnt > 0) & (vcnt == cnt)


def bayesian_decode(tc, counts, bin_s):
    """woodcode bayesian_decoder_1d (Poisson, flat prior): the posterior's maximum (paper v2)."""
    tc = np.clip(tc, 1e-12, None)
    log_p = -bin_s * tc.sum(1)[None, :] + counts @ np.log(tc).T
    ang = (np.arange(tc.shape[0]) + 0.5) * 2 * np.pi / tc.shape[0]
    return ang[np.argmax(log_p, axis=1)]


def hampel(x, window, n_sd=1.0):
    """Replace values more than n_sd scaled MADs from the running median by that median."""
    s = pd.Series(x)
    med = s.rolling(window, center=True, min_periods=1).median()
    mad = (s - med).abs().rolling(window, center=True, min_periods=1).median() * 1.4826
    out = s.where((s - med).abs() <= n_sd * mad, med)
    return out.to_numpy()


def drift(track, spikes, a, b, speed_min=SPEED_POP, tc_speed=SPEED_POP):
    """Decoder drift within one exploration session (paper v2 Methods): tuning curves from the
    first half, decoding of the second half; returns mean absolute drift and its SD (degrees)
    over bins with speed above speed_min, and the counts of second-half bins: all, with valid
    tracking, and valid with speed above speed_min (the bins averaged). The error is unwrapped
    over the valid bins and interpolated across the invalid ones."""
    mid = (a + b) / 2
    m1 = (track["t"] >= a) & (track["t"] < mid) & track["valid"] & (track["speed"] > tc_speed)
    counts = frame_counts(spikes, track["t"][m1], track["dt"])
    tc, _ = tuning_curves(track["hd"][m1], counts, track["dt"])
    centres, pv = pop_bins(spikes, mid, b)
    hd_b, sp_b, ok_b = bin_angle(track, centres)
    dec = bayesian_decode(tc, pv, POP_BIN_S)
    e = np.angle(np.exp(1j * (hd_b - dec)))
    good = np.where(ok_b)[0]
    e = np.interp(np.arange(len(e)), good, np.unwrap(e[good]))
    e = hampel(e, int(HAMPEL_WINDOW_S / POP_BIN_S))
    e = gaussian_filter1d(e, DRIFT_SMOOTH_S / POP_BIN_S, mode="nearest")
    e = np.angle(np.exp(1j * e))
    keep = ok_b & (sp_b > speed_min)
    d = np.degrees(np.abs(e[keep]))
    return (float(d.mean()), float(np.degrees(np.std(e[keep]))),
            {"bins": len(e), "valid": int(ok_b.sum()), "used": int(keep.sum()), "fast": int(np.sum(sp_b > speed_min))})


def isomap_angle(pv, seed, fit_max=ISOMAP_FIT_MAX):
    """Isomap angle of population vectors (paper v1): square root, z-score per cell, unit norm,
    Laplacian kernel PCA to 6 components, Isomap (30 neighbours, 2 dimensions), angle around
    the manifold's centre. Fitted on every bin, or on fit_max bins chosen with the seed and
    applied to all."""
    from sklearn.decomposition import KernelPCA
    from sklearn.manifold import Isomap
    from sklearn.metrics.pairwise import laplacian_kernel
    x = np.sqrt(pv)
    sd = x.std(0)
    x = (x - x.mean(0)) / np.where(sd > 0, sd, 1)
    norm = np.linalg.norm(x, axis=1)
    x = x / np.where(norm > 0, norm, 1)[:, None]
    rng = np.random.default_rng(seed)
    fit = np.sort(rng.choice(len(x), min(len(x), fit_max or len(x)), replace=False))
    kp = KernelPCA(n_components=KPCA_COMPONENTS, kernel="precomputed", random_state=seed).fit(laplacian_kernel(x[fit]))
    z = kp.transform(laplacian_kernel(x, x[fit]))
    np.random.seed(seed)  # Isomap's eigensolver draws its starting vector from the global generator
    iso = Isomap(n_neighbors=ISOMAP_NEIGHBOURS, n_components=2).fit(z[fit])
    y = iso.transform(z)
    y = y - y.mean(0)
    return np.mod(np.arctan2(y[:, 1], y[:, 0]), 2 * np.pi)


def align_direction(internal, real):
    """Flip the internal angle if real minus flipped internal has the smaller circular variance."""
    def cvar(d):
        return 1 - np.abs(np.mean(np.exp(1j * d)))
    if cvar(real + internal) < cvar(real - internal):
        return np.mod(-internal, 2 * np.pi), True
    return internal, False


def binned_tuning(angle, pv, bin_s=POP_BIN_S, n_bins=ISO_BINS):
    """Tuning curves (6 degree bins, 12 degree SD) from smoothed population bins."""
    return tuning_curves(angle, pv.T * 1.0, bin_s, n_bins=n_bins, sigma_deg=ISO_SIGMA * 360.0 / n_bins)


# --- statistics -----------------------------------------------------------------------------

def _ml_random_intercept(y, X, groups):
    """Maximum log-likelihood of y = X b + u_group + e with u ~ N(0, lam s2) and e ~ N(0, s2),
    profiled over b and s2 in closed form and over lam >= 0 numerically (lam = 0 included)."""
    from scipy.optimize import minimize_scalar
    codes, gi = np.unique(groups, return_inverse=True)
    n_g = np.bincount(gi)
    N = len(y)

    def negll(lam):
        c = lam / (1 + n_g * lam)                    # W_g = I - c_g J
        def w(v):                                    # W applied to the columns of v
            v = np.atleast_2d(v.T).T
            sums = np.array([np.bincount(gi, v[:, k], len(codes)) for k in range(v.shape[1])]).T
            return v - c[gi][:, None] * sums[gi]
        WX, Wy = w(X), w(y)[:, 0]
        b = np.linalg.solve(X.T @ WX, X.T @ Wy)
        r = y - X @ b
        s2 = r @ w(r)[:, 0] / N
        return 0.5 * (N * (np.log(2 * np.pi) + 1 + np.log(s2)) + np.sum(np.log1p(n_g * lam)))

    grid = np.r_[0.0, np.logspace(-6, 3, 37)]
    vals = [negll(g) for g in grid]
    k = int(np.argmin(vals))
    best, best_lam = vals[k], grid[k]
    lo, hi = grid[max(k - 1, 0)], grid[min(k + 1, len(grid) - 1)]
    if hi > lo:
        res = minimize_scalar(negll, bounds=(lo, hi), method="bounded", options={"xatol": 1e-10})
        if res.fun < best:
            best, best_lam = res.fun, res.x
    return -best, best_lam


def lme_lrt(df, value, group="genotype", animal="animal", log=False):
    """Linear mixed model with genotype as fixed effect and a random intercept per animal (the
    cell is the residual level, one value per cell), against the model without genotype, by a
    likelihood-ratio test on maximum-likelihood fits (paper v1 Methods). The likelihood is
    profiled exactly, so there is no convergence failure. Returns the coefficient (KO minus WT),
    p and the number of cells."""
    d = df[[value, group, animal]].dropna().copy()
    if log:
        d = d[d[value] > 0]
        d[value] = np.log(d[value])
    y = d[value].to_numpy(float)
    ko = (d[group] == "KO").to_numpy(float)
    X1 = np.column_stack([np.ones_like(y), ko])
    X0 = np.ones((len(y), 1))
    ll1, lam1 = _ml_random_intercept(y, X1, d[animal].to_numpy())
    ll0, _ = _ml_random_intercept(y, X0, d[animal].to_numpy())
    # coefficient at the full model's variance ratio
    codes, gi = np.unique(d[animal].to_numpy(), return_inverse=True)
    c = lam1 / (1 + np.bincount(gi) * lam1)
    WX = X1 - c[gi][:, None] * np.array([np.bincount(gi, X1[:, k]) for k in range(2)]).T[gi]
    Wy = y - c[gi] * np.bincount(gi, y)[gi]
    b = np.linalg.solve(X1.T @ WX, X1.T @ Wy)
    lr = max(2 * (ll1 - ll0), 0.0)
    return float(b[1]), float(stats.chi2.sf(lr, 1)), len(d)


# --- groups and per-recording analysis ------------------------------------------------------

JUVENILE_WT = ["H3001", "H3006", "H3009", "H3015", "H3022", "H3023", "H3029"]
JUVENILE_KO = ["H3003", "H3008", "H3016", "H3019", "H3026"]
ADULT_WT = ["H4813", "H4815", "H4820", "H4823", "H4826", "H4830"]
ADULT_KO = ["H4817", "H4819", "H4822", "H4824", "H4827"]
DUPLICATE_OF = {"H4825": "H4824"}   # H4825's file holds H4824's recording, re-timed


def group_of(subject, archive_genotype, archive_age_group):
    """(age group, genotype) in the main grouping, which matches the paper's unit counts; and in
    the archive's labels (the age group from the date of birth)."""
    for age, geno, ids in (("juvenile", "WT", JUVENILE_WT), ("juvenile", "KO", JUVENILE_KO),
                           ("adult", "WT", ADULT_WT), ("adult", "KO", ADULT_KO)):
        if subject in ids:
            return {"age_group": age, "genotype": geno,
                    "archive_age_group": archive_age_group, "archive_genotype": archive_genotype}
    return {"age_group": None, "genotype": None,
            "archive_age_group": archive_age_group, "archive_genotype": archive_genotype}


def _mask(t, intervals):
    m = np.zeros(len(t), bool)
    for a, b in intervals:
        m |= (t >= a) & (t < b)
    return m


def analyse(s, age_group, seed=0, fit_max=ISOMAP_FIT_MAX, rule="20min"):
    """Every per-cell and per-recording measure the claims use, for one recording. fit_max is
    the number of bins Isomap is fitted on (None: all); rule is the session definition."""
    out = {"cells": None, "rec": {}}
    sessions = exploration_sessions(s, rule)
    rec = out["rec"]
    rec["n_sessions"] = len(sessions)
    rec["session_s"] = [round(b - a, 1) for a, b in sessions]
    if not sessions:
        return out
    px = pixel_scale(s, sessions) if s["pos_unit"] != "centimeters" or np.nanmax(s["pos"]) > 200 else None
    rec["px_per_cm"] = px
    tr = tracking(s, px)
    t, dt = tr["t"], tr["dt"]
    thr = TTP_THRESHOLD_MS[age_group]
    exc = np.where((s["ttp"] > thr) & (s["contamination"] <= 0.5))[0]
    rec["n_units"] = len(s["spikes"])
    rec["n_exc_ttp"] = int(np.sum(s["ttp"] > thr))
    rec["n_exc"] = len(exc)

    # behaviour over both sessions
    mb = _mask(t, sessions) & tr["valid"]
    x, y = tr["xy"][mb, 0], tr["xy"][mb, 1]
    cx, cy = (x.min() + x.max()) / 2, (y.min() + y.max()) / 2
    sp = tr["speed"][mb]
    rec["inactive"] = float(np.mean(sp < SPEED_TC))
    rec["centre"] = float(np.mean(np.hypot(x - cx, y - cy) < ARENA_DIAMETER_CM / 4))
    rec["active_speed"] = float(sp[sp >= SPEED_TC].mean())
    # variants of the thresholds: 2 cm/s for inactive and active, a centre disc of a third of the diameter
    rec["inactive_2"] = float(np.mean(sp < SPEED_POP))
    rec["active_speed_2"] = float(sp[sp >= SPEED_POP].mean())
    rec["centre_third"] = float(np.mean(np.hypot(x - cx, y - cy) < ARENA_DIAMETER_CM / 3))

    a, b = sessions[0]
    spk = [s["spikes"][i] for i in exc]
    n1 = np.array([np.sum((x_ >= a) & (x_ < b)) for x_ in spk])
    keep = n1 >= MIN_SPIKES
    cells = pd.DataFrame({"unit": exc[keep], "ttp": s["ttp"][exc[keep]],
                          "contamination": s["contamination"][exc[keep]], "n_spikes_s1": n1[keep]})
    spk = [x_ for x_, k in zip(spk, keep) if k]
    rec["n_cells"] = len(spk)
    if len(spk) == 0:
        out["cells"] = cells
        return out
    cells["mean_rate"] = cells["n_spikes_s1"] / (b - a)

    m1 = (t >= a) & (t < b) & tr["valid"] & (tr["speed"] > SPEED_TC)
    c1 = frame_counts(spk, t[m1], dt)
    tc, occ = tuning_curves(tr["hd"][m1], c1, dt)
    cells["hd_info"] = hd_info(tc, occ)
    cells["hd_info_uniform"] = hd_info(tc, occ, uniform=True)
    cells["half_width"] = half_width(tc)
    cells["vector_length"] = vector_length(tc)
    cells["peak_rate"] = peak_rate(tc)

    mid = (a + b) / 2
    halves = []
    for lo, hi in ((a, mid), (mid, b)):
        m = m1 & (t >= lo) & (t < hi)
        halves.append(tuning_curves(tr["hd"][m], frame_counts(spk, t[m], dt), dt))
    cells["info_half1"] = hd_info(*halves[0])
    cells["info_half2"] = hd_info(*halves[1])
    cells["offset_halves"] = offset_deg(halves[0][0], halves[1][0])

    if len(sessions) > 1:
        a2, b2 = sessions[1]
        n2 = np.array([np.sum((x_ >= a2) & (x_ < b2)) for x_ in spk])
        m2 = (t >= a2) & (t < b2) & tr["valid"] & (tr["speed"] > SPEED_TC)
        tc2, occ2 = tuning_curves(tr["hd"][m2], frame_counts(spk, t[m2], dt), dt)
        cells["n_spikes_s2"] = n2
        cells["info_s2"] = np.where(n2 >= MIN_SPIKES, hd_info(tc2, occ2), np.nan)
        cells["offset_epochs"] = np.where(n2 >= MIN_SPIKES, offset_deg(tc, tc2), np.nan)

    if len(spk) >= MIN_CELLS_POP:
        rec["drift_mean"], rec["drift_sd"], nb = drift(tr, spk, a, b)
        rec["drift_bins_all"], rec["drift_bins_valid"], rec["drift_bins"] = nb["bins"], nb["valid"], nb["used"]
        rec["drift_bins_fast"] = nb["fast"]
        rec["drift_mean_v2"], rec["drift_sd_v2"], _ = drift(tr, spk, a, b, speed_min=1.5, tc_speed=1.5)

        # Isomap of the waking session
        centres, pv, raw = pop_bins(spk, a, b, raw=True)
        hd_b, sp_b, ok_b = bin_angle(tr, centres)
        iso = isomap_angle(pv, seed, fit_max)
        use = ok_b & (sp_b > SPEED_POP)
        iso_al, flipped = align_direction(iso, hd_b)
        rec["iso_flipped"] = bool(flipped)
        err = np.angle(np.exp(1j * (hd_b[use] - iso_al[use])))
        rec["iso_alignment"] = float(np.abs(np.mean(np.exp(1j * err))))
        tci, occi = binned_tuning(iso_al[use], raw[use])
        tcr, occr = binned_tuning(hd_b[use], raw[use])
        cells["iso_wake_info"] = hd_info(tci, occi)
        cells["real200_info"] = hd_info(tcr, occr)

        # Isomap of REM sleep on every REM interval of the file; a variant leaves out the REM
        # intervals that overlap an exploration session, computed only where there are any
        st = s["sleep_stages"]
        rem_all = st[st.tag == "rem"][["start", "stop"]].to_numpy()
        overlap = np.array([any(ra < sb and rb > sa for sa, sb in exploration_blocks(s)) for ra, rb in rem_all], bool)
        rec["rem_in_sessions"] = int(overlap.sum())
        rec["rem_in_sessions_s"] = float((rem_all[overlap, 1] - rem_all[overlap, 0]).sum()) if overlap.any() else 0.0
        for col, rem in (("iso_rem_info", rem_all), ("iso_rem_info_outside", rem_all[~overlap] if overlap.any() else None)):
            if rem is None:
                cells[col] = cells["iso_rem_info"] if "iso_rem_info" in cells else np.nan
                continue
            r = _rem_isomap(spk, rem, seed + 1, fit_max)
            if col == "iso_rem_info":
                rec["rem_s"], rec["n_cells_rem"], rec["rem_bins"] = r["rem_s"], r["n_cells"], r["bins"]
                cells["n_spikes_rem"] = r["n_spikes"]
            cells[col] = r["info"]
    out["cells"] = cells
    return out


def exploration_blocks(s):
    """The whole tracking blocks that hold the exploration sessions (before any cut)."""
    starts = {a for a, _ in exploration_sessions(s)}
    return [(a, b) for a, b in tracking_blocks(s["t"]) if a in starts]


def _rem_isomap(spk, rem, seed, fit_max):
    """HD information of the cells' tuning to the Isomap angle of REM population activity, for
    cells with at least MIN_SPIKES spikes in REM, when there are at least 60 s of REM and
    MIN_CELLS_POP such cells."""
    rem_s = float((rem[:, 1] - rem[:, 0]).sum()) if len(rem) else 0.0
    n_spk = np.array([np.sum(_mask(x_, rem)) for x_ in spk])
    rsel = np.where(n_spk >= MIN_SPIKES)[0]
    out = {"rem_s": rem_s, "n_cells": len(rsel), "n_spikes": n_spk, "bins": 0, "info": np.full(len(spk), np.nan)}
    if rem_s < 60 or len(rsel) < MIN_CELLS_POP:
        return out
    pvs, raws = [], []
    sub = [spk[i] for i in rsel]
    for ra, rb in rem:
        if rb - ra < 2 * POP_BIN_S:
            continue
        _, p_, r_ = pop_bins(sub, ra, rb, raw=True)
        pvs.append(p_)
        raws.append(r_)
    pv_r, raw_r = np.vstack(pvs), np.vstack(raws)
    ang = isomap_angle(pv_r, seed, fit_max)
    tcm, occm = binned_tuning(ang, raw_r)
    out["info"][rsel] = hd_info(tcm, occm)
    out["bins"] = len(pv_r)
    return out


CLOCK_LAGS = [-60.0, -2.0, -1.0, -0.5, -0.2, -0.1, 0.0, 0.1, 0.2, 0.5, 1.0, 2.0, 60.0]


def lag_check(s, age_group, sessions, tr):
    """Median HD information of the cells of session 1 with the spikes shifted against the
    tracking by each lag in CLOCK_LAGS (seconds): a shared clock puts the peak near zero."""
    a, b = sessions[0]
    m = (tr["t"] >= a) & (tr["t"] <= b) & tr["valid"] & (tr["speed"] > SPEED_TC)
    exc = np.where((s["ttp"] > TTP_THRESHOLD_MS[age_group]) & (s["contamination"] <= 0.5))[0]
    out = []
    for lag in CLOCK_LAGS:
        c = frame_counts([s["spikes"][i] for i in exc], tr["t"][m] + lag, tr["dt"])
        c = c[c.sum(1) >= MIN_SPIKES]
        tc, occ = tuning_curves(tr["hd"][m], c, tr["dt"])
        out.append(float(np.median(hd_info(tc, occ))) if len(c) else np.nan)
    return out


def process(asset_id, seed=0):
    """Load one file and return its metadata, checks and measures, without the raw spikes."""
    s = load_session(asset_id)
    dob, start = s["date_of_birth"], s["session_start"]
    age_days = (pd.Timestamp(start) - pd.Timestamp(dob)).days if dob else None
    archive_age = None if age_days is None or age_days < 0 else ("juvenile" if age_days < 35 else "adult")
    subject = DUPLICATE_OF.get(s["subject"], s["subject"])
    grp = group_of(subject, s["genotype"], archive_age)
    sessions = exploration_sessions(s)
    px = pixel_scale(s, sessions) if s["pos_unit"] != "centimeters" or np.nanmax(s["pos"]) > 200 else None
    tr = tracking(s, px)
    st = s["sleep_stages"]
    emg = {}
    for tag in ("wake", "nrem", "rem"):
        m = _mask(s["emg_t"], st[st.tag == tag][["start", "stop"]].to_numpy())
        emg[tag] = float(np.median(s["emg"][m])) if m.any() else np.nan
    rem = st[st.tag == "rem"][["start", "stop"]].to_numpy()
    meta = {
        "asset_id": asset_id, "subject": s["subject"], "session_id": s["session_id"],
        "archive_genotype": s["genotype"], "date_of_birth": dob, "session_start": start,
        "age_days": age_days, "archive_age_group": archive_age, "age_field": s["age"],
        "age_group": grp["age_group"], "genotype": grp["genotype"],
        "session_description": s["session_description"],
        "n_units": len(s["spikes"]), "n_spikes": s["n_spikes_total"], "spike_checksum": s["spike_checksum"],
        "unit_columns": ",".join(s["unit_columns"]), "n_unsorted_units": s["n_unsorted_units"],
        "n_channels": s["n_channels"], "n_positive": int(s["positive"].sum()),
        "histology_images": ", ".join(s["histology"]),
        "pos_unit": s["pos_unit"], "px_per_cm": px,
        "pos_x_range": (float(np.nanmin(s["pos"][:, 0])), float(np.nanmax(s["pos"][:, 0]))),
        "pos_y_range": (float(np.nanmin(s["pos"][:, 1])), float(np.nanmax(s["pos"][:, 1]))),
        "hd_range": (float(np.nanmin(s["hd"])), float(np.nanmax(s["hd"]))),
        "hd_nan_fraction": float(np.mean(np.isnan(s["hd"]))),
        "pos_nan_frames": int(np.isnan(s["pos"][:, 0]).sum()),
        "pos_y_zero_frames": int(np.sum(s["pos"][:, 1] == 0)), "pos_x_zero_frames": int(np.sum(s["pos"][:, 0] == 0)),
        "pos_y_zero_in_sessions": int(np.sum((s["pos"][:, 1] == 0) & _mask(s["pos_t"], sessions))),
        "pos_y_zero_hd_nan": int(np.sum((s["pos"][:, 1] == 0) & np.isnan(s["hd"]))) if len(s["hd"]) == len(s["pos"]) else None,
        "frame_rate": float(1 / np.median(np.diff(s["t"]))), "same_pos_hd_times": bool(np.array_equal(s["pos_t"], s["t"])),
        "epochs": s["epochs"], "task_epochs": s["task_epochs"], "blocks": tracking_blocks(s["t"]),
        "sessions": sessions, "emg_median": emg,
        "rem_in_exploration": int(sum(((rem[:, 0] < b) & (rem[:, 1] > a)).sum() for a, b in exploration_blocks(s))) if len(rem) else 0,
        "sleep_s": {tag: float((st.stop - st.start)[st.tag == tag].sum()) for tag in ("wake", "nrem", "rem")},
        "ttp": s["ttp"], "contamination": s["contamination"],
        "first_spikes": np.concatenate([x[:20] for x in s["spikes"]]),
        # fingerprints for the duplicate check: per unit, count and sum of spike times before 1248 s
        "early_fingerprint": np.array([[np.sum(x < 1248.0), x[x < 1248.0].sum()] for x in s["spikes"]]),
        "spikes_at_last_time": int(sum(np.sum(x == last) for x in s["spikes"]))
        if (last := max(x.max() for x in s["spikes"] if len(x))) else 0,
    }
    meta["non_increasing_frames"] = int(np.sum(np.diff(s["t"]) <= 0))
    if not sessions or grp["age_group"] is None or s["subject"] in DUPLICATE_OF:
        return {"meta": meta, "main": None, "other_age": None, "claims_rule": None}
    meta["lag_info"] = lag_check(s, grp["age_group"], sessions, tr)
    res = analyse(s, grp["age_group"], seed)
    other = None
    if archive_age is not None and archive_age != grp["age_group"]:
        other = analyse(s, archive_age, seed)
    claims_rule = analyse(s, grp["age_group"], seed, rule="claims")
    return {"meta": meta, "main": res, "other_age": other, "claims_rule": claims_rule}


def process_all(asset_ids, workers=4):
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(process, asset_ids, range(len(asset_ids))))
