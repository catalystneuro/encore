"""Loading and measures for dandiset 000689 (Li, Namburi, Olson et al. 2022, Nature 608, 586-592).

Every file is streamed from the DANDI Archive at the pinned version (remfile + h5py); nothing is
written to disk. Where each parameter comes from is said next to it:

- "criterion": the claim's criterion in claims/000689/10.1038-s41586-022-04964-y.yaml, which
  cites the paper;
- "Methods, <section>": a passage of the paper taken by the author (protocol, author step 1.6);
- "standard choice": a detail that the paper does not fix and that cannot change a result;
- "reading": one of several readings run side by side in the notebook.
"""
from __future__ import annotations

import numpy as np
import requests
import remfile
import h5py
from scipy import ndimage

DANDISET = "000689"
VERSION = "0.240530.1923"
API = "https://api.dandiarchive.org/api"

_ASSETS = None


def assets():
    """All assets of the pinned version: list of dicts with path, size and asset_id."""
    global _ASSETS
    if _ASSETS is None:
        out, url = [], f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=200"
        while url:
            r = requests.get(url, timeout=60).json()
            out += r["results"]
            url = r.get("next")
        _ASSETS = out
    return _ASSETS


def open_h5(path):
    """Open one NWB file of the pinned version by streaming it."""
    a = {x["path"]: x for x in assets()}[path]
    url = f"{API}/assets/{a['asset_id']}/download/"
    return h5py.File(remfile.File(url), "r")


def _s(v):
    return v.decode() if isinstance(v, bytes) else v


# ----------------------------------------------------------------------------------------------
# Fiber photometry (GRAB-NTS1.0 in the BLA, Figure 3j-l)
# ----------------------------------------------------------------------------------------------

def _bouts(x, gap):
    """Group sorted event times into bouts separated by more than `gap` seconds."""
    if len(x) == 0:
        return np.zeros((0, 2))
    x = np.sort(x)
    b = np.where(np.diff(x) > gap)[0]
    return np.c_[np.r_[x[0], x[b + 1]], np.r_[x[b], x[-1]]]


def load_photometry(path):
    """One photometry session.

    The file's single RoiResponseSeries interleaves three frame types at 60 Hz, in a fixed order.
    The LabeledEvents labels are exclusive per frame ("LED470", "Cued stimulus while LED470",
    "Lick while LED470", "Cued stimulus and lick while LED470", and the same for 415), so every
    415 or 470 frame carries one of four labels. Each channel is one phase of the three-frame
    order (20 Hz each, Methods, Fiber photometry, Data acquisition: "each LED was modulated at 20 Hz
    in an alternating fashion"): the phase that the 415 or 470 labels mark (timestamps matched
    within 4 ms) before the first irregular frame interval (below 10 ms). In one session (Mouse6,
    late sucrose) the labels move by one frame after such an interval while the data keep their
    order (the mean of each phase is the same before and after it, printed in the notebook), so
    taking the frames the labels mark after it would read the constant third frame type as the
    470 nm channel; the frame order is used instead. The third frame type is not described and is
    not used. CS onsets are the starts of bouts of the "Cued stimulus"
    frames (with or without lick), bouts separated by more than 1 s (standard choice; cues are at
    least 29 s apart).
    """
    h = open_h5(path)
    e = h["acquisition/LabeledEvents"]
    lab = e["label"][:].astype(str)
    idx = e["event_times_index"][:]
    et = e["event_times"][:]
    ev = {l: et[s:i] for l, s, i in zip(lab, np.r_[0, idx[:-1]], idx)}
    ts = h["acquisition/RoiResponseSeriesRegion0G/timestamps"][:]
    d = h["acquisition/RoiResponseSeriesRegion0G/data"][:]
    out = {"path": path, "session_id": _s(h["general/session_id"][()]),
           "subject": _s(h["general/subject/subject_id"][()]),
           "fluorophore": _s(h["general/fiber_photometry/fluorophores/label"][0]),
           "fiber_location": _s(h["general/fiber_photometry/fibers/location"][0]),
           "wavelengths": h["general/fiber_photometry/excitation_sources/peak_wavelength"][:].tolist(),
           "n_frames": len(ts), "events": {k: len(v) for k, v in ev.items()}}
    irr = np.where(np.diff(ts) < 0.010)[0]
    first_irregular = int(irr[0]) if len(irr) else len(ts)
    out["first_irregular_frame"] = first_irregular
    for ch in ("415", "470"):
        t = np.sort(np.concatenate([v for k, v in ev.items()
                                    if k == "LED" + ch or k.endswith("while LED" + ch)]))
        i = np.clip(np.searchsorted(ts, t - 0.004), 0, len(ts) - 1)
        ok = np.abs(ts[i] - t) < 0.004
        ph, cnt = np.unique(i[ok] % 3, return_counts=True)
        out["phase_agree" + ch] = float(cnt.max() / cnt.sum())
        pre = ok & (i < first_irregular)
        ph0, cnt0 = np.unique(i[pre] % 3, return_counts=True)
        out["phase" + ch] = int(ph0[np.argmax(cnt0)])
        out["labels_moved" + ch] = int(np.sum(ok & (i > first_irregular) & (i % 3 != out["phase" + ch])))
        fr = np.arange(out["phase" + ch], len(ts), 3)
        out["labelled" + ch] = int(ok.sum())
        out["t" + ch] = ts[fr]
        out["f" + ch] = d[fr]
    n = np.arange(len(ts))
    out["phase_means"] = [float(d[k::3].mean()) for k in range(3)]
    out["phase_means_after_irregular"] = [float(np.mean(d[(n % 3 == k) & (n > first_irregular)])) if first_irregular < len(ts) - 3 else np.nan for k in range(3)]
    out["frame_dt"] = (float(np.diff(ts).min()), float(np.diff(ts).max()))
    cue = np.r_[ev["Cued stimulus while LED470"], ev["Cued stimulus and lick while LED470"]]
    b = _bouts(cue, 1.0)
    out["cs_on"] = b[:, 0]
    out["cs_dur"] = b[:, 1] - b[:, 0] + 0.05
    out["licks"] = np.sort(np.r_[ev["Lick while LED470"], ev["Cued stimulus and lick while LED470"]])
    return out


def photometry_trials(s, pre=5.0, post=10.0, zmode="trial", fit="average", return_fit=False):
    """Trial matrix of the z-scored, reference-corrected NT sensor signal at 5 Hz.

    Methods, Fiber photometry, Data analysis: both channels "down-sampled to 5Hz and filtered ...
    using a median filter with a span of 200 ms"; a 200 ms span at 5 Hz is one sample, which does
    nothing, so the median filter is applied at the native 20 Hz (5 samples, 200 ms) before
    averaging into 200 ms bins (standard choice). "Regression coefficients were computed using
    data averaged across trials in a session in a time window of -5 s to 0 s from the start of the
    CS"; "Residuals ... were z-transformed using ... a baseline window of -5 s to 0 s". Whether the
    z-transform uses each trial's own baseline (zmode="trial") or the session's pooled baseline
    (zmode="session") is not said: a reading, both run. The 470 nm trace is regressed on the 415 nm
    trace. fit="average" fits the trial-averaged -5 to 0 s traces, as the Methods say;
    fit="pooled" fits the -5 to 0 s bins of every trial pooled (a variant: averaging can leave too
    little variance in the baseline to estimate the slope).
    Returns time bin starts (s from CS onset), an array trials x bins and the trials kept, and with
    return_fit=True also the slope, the intercept and the correlation of the fitted traces.
    """
    edges = np.arange(-pre, post + 1e-9, 0.2)
    chans = {}
    for ch in ("415", "470"):
        f = ndimage.median_filter(s["f" + ch], size=5, mode="nearest")
        t = s["t" + ch]
        M = np.full((len(s["cs_on"]), len(edges) - 1), np.nan)
        for k, c in enumerate(s["cs_on"]):
            lo, hi = np.searchsorted(t, [c - pre, c + post])
            tt, ff = t[lo:hi] - c, f[lo:hi]
            j = np.digitize(tt, edges) - 1
            ok = (j >= 0) & (j < len(edges) - 1)
            sums = np.bincount(j[ok], ff[ok], minlength=len(edges) - 1)
            cnt = np.bincount(j[ok], minlength=len(edges) - 1)
            with np.errstate(invalid="ignore", divide="ignore"):
                M[k] = sums / cnt
        chans[ch] = M
    keep = ~(np.isnan(chans["415"]).any(1) | np.isnan(chans["470"]).any(1))
    R, G = chans["415"][keep], chans["470"][keep]
    tb = edges[:-1]
    base = tb < 0
    x, y = (R[:, base].mean(0), G[:, base].mean(0)) if fit == "average" else (R[:, base].ravel(), G[:, base].ravel())
    a, b = np.polyfit(x, y, 1)
    r = float(np.corrcoef(x, y)[0, 1])
    res = G - (a * R + b)
    if zmode == "trial":
        mu = res[:, base].mean(1, keepdims=True)
        sd = res[:, base].std(1, ddof=1, keepdims=True)
    else:
        mu = res[:, base].mean()
        sd = res[:, base].std(ddof=1)
    if return_fit:
        return tb, (res - mu) / sd, keep, (float(a), float(b), r)
    return tb, (res - mu) / sd, keep


def window_measure(tb, Z, lo, hi, measure="auc"):
    """Area under the z-scored curve (sum x 0.2 s) or mean z in [lo, hi) s from CS onset."""
    m = (tb >= lo - 1e-9) & (tb < hi - 1e-9)
    return Z[:, m].sum(1) * 0.2 if measure == "auc" else Z[:, m].mean(1)


# ----------------------------------------------------------------------------------------------
# Electrophysiology (Figure 4)
# ----------------------------------------------------------------------------------------------

CS_TYPES = {"sucrose": "reward_stimulus_presentation",
            "neutral": "neutral_stimulus_presentation",
            "shock": "shock_stimulus_presentation"}


def load_ephys(path):
    """Spike times per unit and the trial table of one session (no raw voltage is read)."""
    h = open_h5(path)
    st = h["units/spike_times"][:]
    ix = h["units/spike_times_index"][:]
    spikes = np.split(st, ix[:-1])
    tt = h["intervals/trials/trial_type"][:].astype(str)
    t0 = h["intervals/trials/start_time"][:]
    t1 = h["intervals/trials/stop_time"][:]
    trials = {k: (t0[tt == k], t1[tt == k]) for k in np.unique(tt)}
    return {"path": path, "subject": _s(h["general/subject/subject_id"][()]),
            "session_id": _s(h["general/session_id"][()]),
            "genotype": _s(h["general/subject/genotype"][()]),
            "spikes": spikes, "trials": trials,
            "n_channels": h["acquisition/ElectricalSeries/data"].shape[1],
            "duration": h["acquisition/ElectricalSeries/data"].shape[0] / 30000.0}


def psth(sp, onsets, pre=1.0, post=1.0, binw=0.02):
    """Trial-averaged firing rate (Hz) in bins of `binw` from -pre to +post around onsets.

    Methods, Analysis for in vivo recordings: "PSTHs were computed with 20 ms bins for 1s before
    and after the onsets of sucrose, neutral, and shock CS".
    """
    edges = np.arange(-pre, post + binw / 2, binw)
    c = np.zeros(len(edges) - 1)
    for o in onsets:
        lo, hi = np.searchsorted(sp, [o - pre, o + post])
        c += np.histogram(sp[lo:hi] - o, edges)[0]
    return c / (len(onsets) * binw)


def zscore_psth(p, nbase=50):
    """z-score with the mean and SD of the 1 s baseline bins (Methods, Functional hierarchical
    clustering: "Z-scores were calculated using the mean and standard deviation during the
    baseline period (-1 sec to cue onset) individually for each neuron")."""
    mu, sd = p[:nbase].mean(), p[:nbase].std(ddof=1)
    return (p - mu) / sd if sd > 0 else np.full_like(p, np.nan)


def gauss_smooth(x, window):
    """Gaussian-weighted moving average along time, as MATLAB smoothdata(...,'gaussian',w): the
    window w spans about 5 SD of the Gaussian. The paper's "smoothing factor of 0.85" sets the
    window by a MATLAB heuristic that the paper does not give, so the window is a reading
    (several are run in the notebook)."""
    if window <= 1:
        return x
    sigma = window / 5.0
    half = window // 2
    k = np.exp(-0.5 * (np.arange(-half, half + 1) / sigma) ** 2)
    k /= k.sum()
    return ndimage.convolve1d(x, k, axis=-1, mode="nearest")


def photoresponsive(sp, pulses, fake=None):
    """Methods, Analysis for in vivo recordings: 1 ms PSTH 50 ms around light onset, z-scored
    against the 50 ms before; photo-responsive when (1) some bin within 6 ms after onset has z
    above 1.98, (2) a 6 ms moving average of z is not significant (|z| < 1.98) 7 to 50 ms after
    onset, (3) no significant response in the fake session (not applied when fake is None)."""
    edges = np.arange(-0.05, 0.0505, 0.001)
    c = np.zeros(len(edges) - 1)
    for o in pulses:
        lo, hi = np.searchsorted(sp, [o - 0.05, o + 0.05])
        c += np.histogram(sp[lo:hi] - o, edges)[0]
    base = c[:50]
    sd = base.std(ddof=1)
    if sd == 0:
        return False, np.nan
    z = (c - base.mean()) / sd
    early = z[50:56].max()
    ma = np.convolve(z[57:100], np.ones(6) / 6, mode="valid")
    ok = early > 1.98 and np.all(np.abs(ma) < 1.98)
    if ok and fake is not None:
        ok = not photoresponsive(sp, fake)[0]
    return ok, early


# ----------------------------------------------------------------------------------------------
# Pose (Figure 5d-i)
# ----------------------------------------------------------------------------------------------

POSE_PARTS = ("Head", "Electrode", "LeftEar", "RightEar", "Tail", "Port")


def load_pose(h):
    """DeepLabCut positions (pixels) of the parts used, the frame rate and the starting time."""
    g = h["processing/behavior/PoseEstimation"]
    out = {}
    for p in POSE_PARTS:
        s = g[f"{p}PoseEstimationSeries"]
        out[p] = s["data"][:]
        out["rate"] = float(s["starting_time"].attrs["rate"])
        out["t0"] = float(s["starting_time"][()])
    return out


def pose_measures(pose):
    """The eight measures of Methods, Unsupervised trial-based classification of behaviors, per
    frame: velocity, distance to port, direction, direction relative to the port, and the change
    of each per second (acceleration and so on). The paper does not say which body point gives the
    position or direction; standard choices: position is the head; direction is the angle of the
    tail-to-head vector; the port is the session median of the tracked port; direction relative
    to the port is the angle (degrees) between the heading and the head-to-port vector."""
    r = pose["rate"]
    head, tail = pose["Head"], pose["Tail"]
    port = np.nanmedian(pose["Port"], axis=0)
    vel = np.r_[0, np.linalg.norm(np.diff(head, axis=0), axis=1) * r]
    dist = np.linalg.norm(head - port, axis=1)
    hv = head - tail
    direc = np.arctan2(hv[:, 1], hv[:, 0])
    pv = port - head
    rel = np.degrees(np.angle(np.exp(1j * (np.arctan2(pv[:, 1], pv[:, 0]) - direc))))
    dd = lambda x: np.r_[0, np.diff(x)] * r
    dang = lambda x, unit: np.r_[0, np.angle(np.exp(1j * np.diff(x if unit == "rad" else np.radians(x))))] * r * (1 if unit == "rad" else 180 / np.pi)
    return {"velocity": vel, "distance_to_port": dist, "direction": direc, "rel_direction": rel,
            "acceleration": dd(vel), "d_distance_to_port": dd(dist),
            "d_direction": dang(direc, "rad"), "d_rel_direction": dang(rel, "deg")}


def _median_at(dist, rate, t0, times):
    """Median of a per-frame measure at the frames of `times` (rows: one set of times each)."""
    f = np.round((np.atleast_2d(times) - t0) * rate).astype(int)
    ok = (f >= 0) & (f < len(dist))
    v = np.where(ok, dist[np.clip(f, 0, len(dist) - 1)], np.nan)
    med = np.nanmedian(v, axis=1)
    med[ok.sum(1) <= 5] = np.nan
    return med


def fit_pose_clock(dist, rate, t0, events, max_lag=300.0):
    """Map trial-clock times onto the pose clock: pose time = T + offset + factor * (t - T), with T
    the median event time. At each port entry (`events`, trial clock) the head should be at the
    port, so the map is the one that minimises the median head-to-port distance at port entries.
    The pose series give only a start time and a nominal 15 frames/s, so this map is estimated from
    the data (an assumption, stated in the notebook). Steps: a grid of factors from 0.96 to 1.04 (step
    0.0005) and offsets within +/- max_lag (step 0.5 s), on at most 250 port entries spread over the session; then a finer grid around the best (factor
    +/- 0.002 in steps of 0.0001, offset +/- 3 s in steps of 0.1 s). Search ranges and steps are standard
    choices. Returns the map and, as checks, the best extra lag left in each third of the session
    (zero when the map holds throughout) and the median distance under the map, at lag 0 and over
    the whole session."""
    events = np.sort(events)
    T = float(np.median(events))
    sub = events[np.unique(np.linspace(0, len(events) - 1, min(len(events), 250)).astype(int))]
    offsets = np.arange(-max_lag, max_lag + 1e-9, 0.5)
    best = (np.inf, 1.0, 0.0)
    for f in np.arange(0.96, 1.04 + 1e-9, 0.0005):
        med = _median_at(dist, rate, t0, T + offsets[:, None] + f * (sub - T)[None, :])
        if np.all(np.isnan(med)):
            continue
        k = int(np.nanargmin(med))
        if med[k] < best[0]:
            best = (med[k], f, offsets[k])
    _, factor0, offset0 = best
    grid = [(f, o) for f in np.arange(factor0 - 0.002, factor0 + 0.002 + 1e-9, 0.0001)
            for o in np.arange(offset0 - 3, offset0 + 3 + 1e-9, 0.1)]
    tt = np.array([T + o + f * (events - T) for f, o in grid])
    med = _median_at(dist, rate, t0, tt)
    factor, offset = grid[int(np.nanargmin(med))]
    resid = []
    small = np.arange(-20, 20 + 1e-9, 0.2)
    for seg in np.array_split(events, 3):
        m = _median_at(dist, rate, t0, (T + offset + factor * (seg - T))[None, :] + small[:, None])
        resid.append(float(small[np.nanargmin(m)]))
    return {"T": T, "offset": float(offset), "factor": float(factor), "resid_lag_thirds": resid,
            "med_dist_fit": float(np.nanmin(med)),
            "med_dist_lag0": float(_median_at(dist, rate, t0, events[None, :])[0]),
            "med_dist_all": float(np.nanmedian(dist))}


def to_pose_time(t, clock):
    """Trial-clock times to pose-clock times under a map from fit_pose_clock."""
    return clock["T"] + clock["offset"] + clock["factor"] * (np.asarray(t) - clock["T"])


POSE_MEASURES = ("velocity", "distance_to_port", "direction", "rel_direction",
                 "acceleration", "d_distance_to_port", "d_direction", "d_rel_direction")


def behavior_trials(measures, clock, rate, t0, onsets, n_frames=300):
    """The eight pose measures for the `n_frames` frames (20 s at 15 frames/s) after each CS onset
    (Methods, Unsupervised trial-based classification of behaviors: "Each of the eight
    measurements were extracted for 300 frames (20 seconds) following the sucrose and shock cue").
    Onsets are on the trial clock and are mapped to pose frames with fit_pose_clock. Returns an
    array trials x 8 x n_frames and the onsets kept (trials whose frames run past the pose are
    dropped)."""
    start = np.round((to_pose_time(onsets, clock) - t0) * rate).astype(int)
    n = len(measures["velocity"])
    ok = (start >= 0) & (start + n_frames <= n)
    X = np.stack([np.stack([measures[k][s:s + n_frames] for k in POSE_MEASURES]) for s in start[ok]])
    return X, np.asarray(onsets)[ok]


def density_peaks(Y, gridsize=200, cut=3.0, rel_floor=0.0):
    """Number of local maxima of a Gaussian kernel density over a 2-D embedding, as seaborn.kdeplot
    computes it by default (scipy gaussian_kde with Scott's bandwidth, a 200 x 200 grid extending
    3 bandwidths beyond the data); each maximum is one watershed marker, so the count is the number
    of watershed regions (Methods, Unsupervised trial-based classification of behaviors). Maxima
    below `rel_floor` times the highest density are not counted (0: all count; a variant)."""
    from scipy.stats import gaussian_kde
    kde = gaussian_kde(Y.T, bw_method="scott")
    bw = np.sqrt(np.diag(kde.covariance))
    xs = [np.linspace(Y[:, i].min() - cut * bw[i], Y[:, i].max() + cut * bw[i], gridsize) for i in range(2)]
    gx, gy = np.meshgrid(*xs, indexing="ij")
    D = kde(np.vstack([gx.ravel(), gy.ravel()])).reshape(gridsize, gridsize)
    peak = (D == ndimage.maximum_filter(D, size=3, mode="constant", cval=-np.inf)) & (D > rel_floor * D.max())
    return int(peak.sum()), D


class RangeFile:
    """Minimal read-only file over HTTP range requests, for reading a video container's header
    with PyAV without downloading the file. Reads past the end return what is left; at most
    `max_bytes` are fetched in all (an error after that), so a container whose index needs the
    whole file fails instead of downloading it."""

    def __init__(self, url, max_bytes=50_000_000):
        self.s = requests.Session()
        r = self.s.get(url, headers={"Range": "bytes=0-0"}, allow_redirects=True, timeout=60)
        self.url = r.url
        self.size = int(r.headers["Content-Range"].split("/")[1])
        self.pos, self.fetched, self.max_bytes = 0, 0, max_bytes

    def read(self, n=-1):
        if n is None or n < 0:
            n = self.size - self.pos
        end = min(self.pos + n, self.size) - 1
        if end < self.pos:
            return b""
        self.fetched += end - self.pos + 1
        if self.fetched > self.max_bytes:
            raise IOError("more than max_bytes read")
        b = self.s.get(self.url, headers={"Range": f"bytes={self.pos}-{end}"}, timeout=60).content
        self.pos += len(b)
        return b

    def seek(self, offset, whence=0):
        self.pos = {0: 0, 1: self.pos, 2: self.size}[whence] + offset
        return self.pos

    def tell(self):
        return self.pos
