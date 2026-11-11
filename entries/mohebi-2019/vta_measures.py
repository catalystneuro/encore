"""Per-unit measures for the reproduction of Mohebi et al. (2019) on CRCNS vta-2.

One pass per unit computes, from its spikes and its session's events, the per-trial values and
mean traces that the claims use, so that the large spike density functions are held one unit at a
time. Windows and kernels are those of the claims file's criteria or of the passages cited in
`vta`'s docstring; each is named where it is set below.
"""

from __future__ import annotations

import numpy as np

import vta

TRACE_WIN = (-1.0, 1.5)        # mean traces for plots and alignment (a standard plotting window)
PEAK_WIN = 0.25                # Methods, Analysis, paragraph 2: peak in 250 ms after rewarded Side-In
VALLEY_WINS = {"methods_1to3s": (1.0, 3.0), "legend_0to2s": (0.0, 2.0)}  # Methods; ED Fig. 8 legend
PAUSE_WIN = 2.0                # ED Fig. 8 legend: maximum ISI within 2 s after unrewarded Side-In
EARLY_WIN = 0.5                # claims file, fig5a-early criterion
RAMP_WIN = 0.5                 # Methods, Analysis, paragraph 3
RAMP_SD = 0.050                # Methods: 50 ms Gaussian kernel, read as its SD
PAV_PEAK_WIN = 0.5             # Extended Data Fig. 5 legend
SHORT_LAT, LONG_LAT = 1.0, 2.0  # Results: short (< 1 s) and long (> 2 s) latencies


def max_gap(ts, a, b, edges=True):
    """Longest interval without spikes in [a, b]: with `edges`, the window bounds count as
    boundaries; without, only intervals between spikes in the window (NaN if fewer than 2)."""
    s = ts[(ts >= a) & (ts <= b)]
    if edges:
        pts = np.r_[a, s, b]
        return float(np.max(np.diff(pts)))
    if len(s) < 2:
        return np.nan
    return float(np.max(np.diff(s)))


def bandit_pass(u, tr, rng, n_shuffles=10000):
    ts = u["segments"]["RL"]["ts"]
    t_end = max(ts[-1], np.nanmax(tr["SideOut"]), np.nanmax(tr["FoodIn"])) + 5.0
    out = {}
    s20 = vta.sdf(ts, t_end, vta.SDF_SD)
    s4 = vta.sdf(ts, t_end, vta.SDF_SD_VARIANT)
    si = tr["SideIn"]
    for name, s in (("sd20", s20), ("sd4", s4)):
        out[f"peak_{name}"] = np.nanmax(vta.aligned(s, si, 0.0, PEAK_WIN), 1)
        for key, (a, b) in VALLEY_WINS.items():
            out[f"valley_{key}_{name}"] = np.nanmin(vta.aligned(s, si, a, b), 1)
    out["pause_edges"] = np.array([max_gap(ts, e, e + PAUSE_WIN, True) for e in si])
    out["pause_isi"] = np.array([max_gap(ts, e, e + PAUSE_WIN, False) for e in si])
    # mean traces (Hz) around events, all trials and by outcome or latency
    traces = {}
    for ev in ("LightOn", "CenterIn", "Go", "SideIn", "FoodIn"):
        m = vta.aligned(s20, tr[ev], *TRACE_WIN)
        traces[ev] = np.nanmean(m, 0)
        if ev == "SideIn":
            traces["SideIn_rew"] = np.nanmean(m[tr["outcome"] == 1], 0)
            traces["SideIn_unrew"] = np.nanmean(m[tr["outcome"] == 0], 0)
        if ev in ("LightOn", "CenterIn"):
            traces[ev + "_short"] = np.nanmean(m[tr["latency"] < SHORT_LAT], 0)
            traces[ev + "_long"] = np.nanmean(m[tr["latency"] > LONG_LAT], 0)
    out["traces"] = traces
    # Light-On response per trial (peak in 0.5 s) for the short/long comparison
    out["lighton_peak"] = np.nanmax(vta.aligned(s20, tr["LightOn"], 0.0, 0.5), 1)
    # reading (b) of "better aligned": time of the per-trial SDF maximum between Light-On and
    # Center-In + 0.5 s, for trials with latency under 5 s
    tp = np.full(len(si), np.nan)
    for k, (lo, ci) in enumerate(zip(tr["LightOn"], tr["CenterIn"])):
        if ci - lo < 5.0:
            i0, i1 = int(round(lo / vta.DT)), int(round((ci + 0.5) / vta.DT))
            tp[k] = (i0 + int(np.argmax(s20[i0:i1 + 1]))) * vta.DT
    out["trial_peak_time"] = tp
    # early-trial firing (spikes/s)
    lo, ci = tr["LightOn"], tr["CenterIn"]
    out["early_after_lighton"] = vta.counts_in(ts, lo, lo + EARLY_WIN) / EARLY_WIN
    out["early_before_centerin"] = vta.counts_in(ts, ci - EARLY_WIN, ci) / EARLY_WIN
    # ramp angles from the 50 ms smoothed mean rate in the 0.5 s before the event
    s50 = vta.sdf(ts, t_end, RAMP_SD)
    tt = np.arange(int(round(-RAMP_WIN / vta.DT)), 1) * vta.DT
    long = tr["latency"] > LONG_LAT
    m_ci = np.nanmean(vta.aligned(s50, ci[long], -RAMP_WIN, 0.0), 0)
    rew = tr["outcome"] == 1
    fi = tr["FoodIn"][rew]
    m_fi = np.nanmean(vta.aligned(s50, fi[np.isfinite(fi)], -RAMP_WIN, 0.0), 0)
    out["ramp_centerin_long"] = vta.ramp_angle(m_ci, tt)
    out["ramp_foodin"] = vta.ramp_angle(m_fi, tt)
    out["ramp_trace_centerin_long"], out["ramp_trace_foodin"] = m_ci, m_fi
    out["n_long"], out["n_short"] = int(long.sum()), int((tr["latency"] < SHORT_LAT).sum())
    del s20, s4, s50
    # time-to-cue-response shuffle tests
    cue = {}
    for ev, sel in (("LightOn", None), ("Go", None), ("SideIn_rew", rew)):
        e = tr[ev.split("_")[0]] if sel is None else tr["SideIn"][sel]
        for post in (0.5, 1.0):
            cue[(ev, post)] = vta.cue_response(ts, e, rng, post=post, n_shuffles=n_shuffles)
    out["cue"] = cue
    return out


def pav_pass(u):
    seg = u["segments"]["Pav"]
    ts, rex, box = seg["ts"], seg["rex"], seg["boxts"]
    tone = np.ravel(rex["Tone"])
    food = np.ravel(rex["Food"]).astype(int)
    cc = np.asarray(rex["Cue_Contingency"])
    prob = {float(f): float(p) for f, p in cc}
    onset = np.asarray(box["event"])[0]
    click = np.ravel(box["FoodDrop"])
    s20 = vta.sdf(ts, max(ts[-1], np.nanmax(onset) + 10) + 5, vta.SDF_SD)
    cue_peak = np.nanmax(vta.aligned(s20, onset, 0.0, PAV_PEAK_WIN), 1)
    click_peak = np.nanmax(vta.aligned(s20, click, 0.0, PAV_PEAK_WIN), 1)
    tones = sorted([f for f in prob if f != 0], key=lambda f: prob[f])  # zero, medium, high
    label = {tones[0]: "zero", tones[1]: "medium", tones[2]: "high", 0.0: "unpredicted"}
    cond = np.array([label[float(t)] for t in tone])
    tr_cue = {c: np.nanmean(vta.aligned(s20, onset[cond == c], -1.0, 4.0), 0) for c in ("zero", "medium", "high")}
    tr_click = {c: np.nanmean(vta.aligned(s20, click[(cond == c) & (food == 1)], -1.0, 1.5), 0)
                for c in ("unpredicted", "medium", "high")}
    return {"cond": cond, "food": food, "cue_peak": cue_peak, "click_peak": click_peak,
            "probs": {label[f]: prob[f] for f in prob}, "trace_cue": tr_cue, "trace_click": tr_click,
            "onset": onset, "click": click}
