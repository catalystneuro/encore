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
    415 or 470 frame carries one of four labels. The frames whose timestamps match a 415 label
    (within 4 ms) are the reference channel, those that match a 470 label the signal channel
    (20 Hz each, Methods, Fiber photometry, Data acquisition: "each LED was modulated at 20 Hz
    in an alternating fashion"). The labels are used, not the frame order, because the order
    shifts after an irregular frame interval in some sessions. The third frame type is not
    described and is not used. CS onsets are the starts of bouts of the "Cued stimulus"
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
    for ch in ("415", "470"):
        t = np.sort(np.concatenate([v for k, v in ev.items()
                                    if k == "LED" + ch or k.endswith("while LED" + ch)]))
        i = np.clip(np.searchsorted(ts, t - 0.004), 0, len(ts) - 1)
        ok = np.abs(ts[i] - t) < 0.004
        ph, cnt = np.unique(i[ok] % 3, return_counts=True)
        out["phase" + ch] = int(ph[np.argmax(cnt)])
        out["phase_agree" + ch] = float(cnt.max() / cnt.sum())
        fr = np.unique(i[ok])
        out["labelled" + ch] = len(fr)
        out["t" + ch] = ts[fr]
        out["f" + ch] = d[fr]
    out["phase_means"] = [float(d[k::3].mean()) for k in range(3)]
    out["frame_dt"] = (float(np.diff(ts).min()), float(np.diff(ts).max()))
    cue = np.r_[ev["Cued stimulus while LED470"], ev["Cued stimulus and lick while LED470"]]
    b = _bouts(cue, 1.0)
    out["cs_on"] = b[:, 0]
    out["cs_dur"] = b[:, 1] - b[:, 0] + 0.05
    out["licks"] = np.sort(np.r_[ev["Lick while LED470"], ev["Cued stimulus and lick while LED470"]])
    return out


def photometry_trials(s, pre=5.0, post=10.0, zmode="trial"):
    """Trial matrix of the z-scored, reference-corrected NT sensor signal at 5 Hz.

    Methods, Fiber photometry, Data analysis: both channels "down-sampled to 5Hz and filtered ...
    using a median filter with a span of 200 ms"; a 200 ms span at 5 Hz is one sample, which does
    nothing, so the median filter is applied at the native 20 Hz (5 samples, 200 ms) before
    averaging into 200 ms bins (standard choice). "Regression coefficients were computed using
    data averaged across trials in a session in a time window of -5 s to 0 s from the start of the
    CS"; "Residuals ... were z-transformed using ... a baseline window of -5 s to 0 s". Whether the
    z-transform uses each trial's own baseline (zmode="trial") or the session's pooled baseline
    (zmode="session") is not said: a reading, both run.
    Returns time bin starts (s from CS onset) and an array trials x bins.
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
    a, b = np.polyfit(R[:, base].mean(0), G[:, base].mean(0), 1)
    res = G - (a * R + b)
    if zmode == "trial":
        mu = res[:, base].mean(1, keepdims=True)
        sd = res[:, base].std(1, ddof=1, keepdims=True)
    else:
        mu = res[:, base].mean()
        sd = res[:, base].std(ddof=1)
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
