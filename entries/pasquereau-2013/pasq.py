"""Loading and measures for the torque perturbation data of dandiset 001636 (monkey V).

Pasquereau & Turner (2013), Front. Syst. Neurosci. 7:98, doi:10.3389/fnsys.2013.00098.

Each NWB file holds one recording (one or two units) with a trials table whose
`torque_perturbation_type` and `torque_perturbation_onset_time` mark the perturbations, the elbow
angle and the torque command at 1 kHz, and up to six EMG channels. Files are streamed from the
archive at the pinned version with remfile and h5py (reading the NWB paths directly is much
faster than building the pynwb objects of 291 files); nothing is written to disk. Only windows
around each perturbation are kept.

Where the parameters come from. "Claims" means the opening comment and criteria of
claims/pasquereau-2013.yaml, which cite the paper's Methods; "Methods" means the paper's
Methods, Data analysis.

- Cells studied: units with at least 5 perturbations of each direction (Methods, "for neurons
  studied during at least 5 repetitions of each torque direction"; claims).
- SDF: spikes convolved at 1 ms with a gamma kernel, k = 1.5, theta = 20 ms (Methods). The
  kernel is truncated at 400 ms, where its tail is below 1e-7 of its mass (a standard choice
  that cannot change a result).
- Baseline: the 500 ms before onset (Methods; claims). Detection: the trial-averaged SDF of one
  direction against its baseline mean +/- t * SD of its 500 baseline values, t the two-tailed
  critical value at p = 0.002 with 499 degrees of freedom (claims; the degrees of freedom are a
  standard choice for 500 samples). A response starts where the SDF leaves the threshold band
  between 20 and 60 ms, having been inside it the ms before (claims; Methods, "between 20-60-ms").
- Offset: the first ms after onset where the SDF is back inside the band, searched to the end of
  the 200 ms post-torque epoch (Methods: "the time point at which the SDF first returned within
  the p = 0.002 threshold"; the 200 ms limit is the Methods' post-torque epoch, and a response
  still outside the band at 200 ms ends there).
- Magnitudes over onset to offset, signed so that a response's own direction is positive (claims):
  mean change from baseline, maximum change, area (spikes), and the mean SDF (the Methods' "mean
  firing rate during the response"). FWHM: the contiguous span around the response's peak, within
  0 to 400 ms, where the signed change is at least half the peak change (claims; "full-width
  half-maximum" in the Methods).
- DSI = |1 - NP/P|, NP and P the signed maximum changes from baseline over 0 to 200 ms of the two
  directions, P the larger in absolute value (Methods).
- Kinematics (claims): 25 Hz low-pass FIR with a Hamming window applied forwards and backwards
  (101 taps at 1 kHz, a standard choice), velocity by differences, onset where the velocity first
  exceeds 5 deg/s in the torque's direction within 0 to 200 ms, peak velocity over 0 to 200 ms,
  amplitude the largest displacement over 0 to 300 ms, all signed so that the torque's direction
  is positive. Flexion torque moves the angle to positive values (checked in the notebook).
- EMG (claims): session-average trace for flexion torques less its mean over the 200 ms before
  onset; m1 = mean over 15 to 40 ms, m2 = mean over 41 to 80 ms; a response starts at the first
  ms from 10 to 150 ms above 2 SD of the baseline and lasts while it stays above.
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy import signal, stats

DANDISET_ID = "001636"
DANDISET_VERSION = "0.261124.1906"

MIN_PERTURBATIONS = 5
GAMMA_K, GAMMA_THETA_MS = 1.5, 20.0
KERNEL_MS = 400
BASELINE_MS = 500
EPOCH_MS = 200
ONSET_WINDOW_MS = (20, 60)
P_THRESHOLD = 0.002
T_CRIT = float(stats.t.ppf(1 - P_THRESHOLD / 2, BASELINE_MS - 1))
PSEUDO_SHIFT_MS = 600          # claims, false-positive-rate: pseudo onset 600 ms before torque

# Spike windows kept around each perturbation, ms relative to torque onset. The earliest time is
# the pseudo onset's baseline (-1100 ms) less the kernel's reach.
SPIKE_WINDOW_MS = (-1500, 500)
ANGLE_WINDOW_MS = (-200, 400)
EMG_WINDOW_MS = (-300, 300)
TORQUE_WINDOW_MS = (-50, 100)
EMG_CHANNELS = ["EMGTricepsLongus1", "EMGTricepsLongus2", "EMGTricepsLateralis",
                "EMGDeltoidPosterior", "EMGTrapezius", "EMGBrachioradialis"]
TRICEPS = ["EMGTricepsLongus1", "EMGTricepsLongus2", "EMGTricepsLateralis"]

LOWPASS_HZ, FIR_TAPS = 25.0, 101
VELOCITY_THRESHOLD = 5.0       # deg/s, Methods
EMG_BASELINE_MS = 200
M1_MS, M2_MS = (15, 40), (41, 80)
EMG_SEARCH_MS = (10, 150)


def asset_urls(subject: str = "sub-Venus") -> list[tuple[str, str]]:
    """(path, streaming URL) of every NWB file of a subject at the pinned version."""
    with DandiAPIClient() as client:
        dandiset = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        return sorted((a.path, a.get_content_url(follow_redirects=1, strip_query=True))
                      for a in dandiset.get_assets()
                      if a.path.endswith(".nwb") and a.path.startswith(subject + "/"))


def _str(values) -> np.ndarray:
    return np.array([v.decode() if isinstance(v, bytes) else str(v) for v in values])


def _ragged(h, name):
    data, index = h[name][:], h[name + "_index"][:]
    starts = np.r_[0, index[:-1]]
    return [data[s:e] for s, e in zip(starts, index)]


def _windows(ts, data, onsets, window_ms):
    """Samples of a 1 kHz series from onset + window[0] to onset + window[1] (ms), NaN outside."""
    n = window_ms[1] - window_ms[0]
    out = np.full((len(onsets), n), np.nan)
    for i, t in enumerate(onsets):
        j = np.searchsorted(ts, t + window_ms[0] / 1000 - 1e-7)
        seg = data[j:j + n]
        tseg = ts[j:j + n]
        if len(seg) == n and abs(tseg[-1] - tseg[0] - (n - 1) / 1000) < 1e-6:
            out[i] = seg
    return out


def load_file(path: str, url: str) -> dict:
    """Trials, units and perturbation-aligned windows of one file."""
    with h5py.File(remfile.File(url), "r") as h:
        tr = h["intervals/trials"]
        trials = pd.DataFrame({
            "start": tr["start_time"][:], "stop": tr["stop_time"][:],
            "center": tr["center_target_appearance_time"][:],
            "torque": _str(tr["torque_perturbation_type"][:]),
            "onset": tr["torque_perturbation_onset_time"][:],
            "movement": _str(tr["movement_type"][:]),
            "source_file": _str(tr["source_file"][:]),
        })
        u = h["units"]
        spikes = _ragged(u, "spike_times")
        obs = [o.reshape(-1, 2) for o in _ragged(u, "obs_intervals")]
        units = pd.DataFrame({
            "unit_name": _str(u["unit_name"][:]),
            "ptype": _str(u["neuron_projection_type"][:]),
            "post": u["is_post_mptp"][:].astype(bool),
            "latency": u["antidromic_latency_ms"][:],
            "latency_2": u["antidromic_latency_2_ms"][:],
        })
        pert = trials[trials.torque.isin(["flexion", "extension"])].reset_index(drop=True)
        acq = h["acquisition"]
        out = {"path": path, "session": h["general/session_id"][()].decode(),
               "date": h["session_start_time"][()].decode()[:10], "trials": trials,
               "units": units, "pert": pert, "emg": {}, "angle": None, "torque_cmd": None}
        if "ElbowAngle" in acq:
            ts = acq["ElbowAngle/timestamps"][:]
            out["angle"] = _windows(ts, acq["ElbowAngle/data"][:, 0], pert.onset.values,
                                    ANGLE_WINDOW_MS)
            out["torque_cmd"] = _windows(ts, acq["ElbowTorque/data"][:], pert.onset.values,
                                         TORQUE_WINDOW_MS)
            for ch in EMG_CHANNELS:
                if ch in acq:
                    out["emg"][ch] = _windows(acq[ch + "/timestamps"][:], acq[ch + "/data"][:],
                                              pert.onset.values, EMG_WINDOW_MS)
    # Spike times relative to each perturbation, kept only where the unit was observed over the
    # whole spike window.
    w0, w1 = SPIKE_WINDOW_MS[0] / 1000, SPIKE_WINDOW_MS[1] / 1000
    rel, observed = [], []
    for st, ob in zip(spikes, obs):
        r, o = [], []
        for t in pert.onset.values:
            inside = np.any((ob[:, 0] <= t + w0) & (ob[:, 1] >= t + w1))
            o.append(inside)
            r.append(st[(st >= t + w0) & (st < t + w1)] - t)
        rel.append(r)
        observed.append(np.array(o))
    out["rel_spikes"], out["observed"] = rel, observed
    out["n_spikes"] = [len(s) for s in spikes]
    out["spikes_all"] = spikes
    out["obs"] = obs
    return out


def load_all(paths_urls, workers: int = 8) -> list[dict]:
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(lambda pu: load_file(*pu), paths_urls))


# ---------------------------------------------------------------- spike density functions

def gamma_kernel() -> np.ndarray:
    t = np.arange(KERNEL_MS) + 0.5
    k = stats.gamma.pdf(t, GAMMA_K, scale=GAMMA_THETA_MS)
    return k / k.sum() * 1000.0       # spikes/s for one spike


KERNEL = gamma_kernel()


def sdf_trials(rel_spikes: list[np.ndarray]) -> np.ndarray:
    """Single-trial SDFs (spikes/s) at 1 ms over SPIKE_WINDOW_MS, causal gamma kernel."""
    n = SPIKE_WINDOW_MS[1] - SPIKE_WINDOW_MS[0]
    out = np.zeros((len(rel_spikes), n))
    for i, s in enumerate(rel_spikes):
        idx = np.floor(s * 1000).astype(int) - SPIKE_WINDOW_MS[0]
        idx = idx[(idx >= 0) & (idx < n)]
        train = np.bincount(idx, minlength=n).astype(float)
        out[i] = np.convolve(train, KERNEL)[:n]
    return out


def ms_index(t_ms: int) -> int:
    return t_ms - SPIKE_WINDOW_MS[0]


def detect(mean_sdf: np.ndarray, zero_ms: int = 0) -> dict:
    """Response of one trial-averaged SDF around `zero_ms` (0 = torque onset, -600 = pseudo)."""
    z = ms_index(zero_ms)
    base = mean_sdf[z - BASELINE_MS:z]
    mu, sd = base.mean(), base.std(ddof=1)
    lo, hi = mu - T_CRIT * sd, mu + T_CRIT * sd
    post = mean_sdf[z:z + EPOCH_MS + 200]
    outside = (post > hi) | (post < lo)
    res = {"baseline": mu, "sd": sd, "responds": False, "any_crossing": bool(outside[:EPOCH_MS].any())}
    # signed max change over 0-200 ms for the DSI
    ch = post[:EPOCH_MS] - mu
    res["max_change_signed"] = float(ch[np.argmax(np.abs(ch))])
    for t in range(ONSET_WINDOW_MS[0], ONSET_WINDOW_MS[1] + 1):
        if outside[t] and not outside[t - 1]:
            sign = 1.0 if post[t] > hi else -1.0
            end = t
            while end < EPOCH_MS and outside[end] and np.sign(post[end] - mu) == sign:
                end += 1
            seg = sign * (post[t:end] - mu)
            peak = t + int(np.argmax(seg))
            half = seg.max() / 2
            full = sign * (post - mu)
            a = peak
            while a > 0 and full[a - 1] >= half:
                a -= 1
            b = peak
            while b < len(full) - 1 and full[b + 1] >= half:
                b += 1
            res.update(responds=True, onset=t, offset=end, sign=sign,
                       mean_change=float(seg.mean()), max_change=float(seg.max()),
                       area=float(seg.sum() / 1000.0), mean_rate=float(post[t:end].mean()),
                       fwhm=float(b - a + 1))
            break
    return res


# ---------------------------------------------------------------- kinematics and EMG

_FIR = signal.firwin(FIR_TAPS, LOWPASS_HZ, fs=1000.0, window="hamming")


def kinematics(angle_windows: np.ndarray, directions: np.ndarray) -> pd.DataFrame:
    """Per perturbation: onset latency (ms), peak velocity (deg/s), amplitude (deg)."""
    z = -ANGLE_WINDOW_MS[0]
    rows = []
    for a, d in zip(angle_windows, directions):
        if np.isnan(a).any():
            rows.append((np.nan, np.nan, np.nan))
            continue
        s = 1.0 if d == "flexion" else -1.0
        filt = signal.filtfilt(_FIR, [1.0], a)
        vel = s * np.gradient(filt) * 1000.0
        disp = s * (filt - filt[z])
        above = np.where(vel[z:z + 200] > VELOCITY_THRESHOLD)[0]
        rows.append((float(above[0]) if len(above) else np.nan,
                     float(vel[z:z + 200].max()), float(disp[z:z + 300].max())))
    return pd.DataFrame(rows, columns=["latency", "peak_velocity", "amplitude"])


def emg_measures(windows: np.ndarray) -> dict:
    """m1, m2, response onset and duration of a session-average EMG trace (flexion torques)."""
    z = -EMG_WINDOW_MS[0]
    trace = windows.mean(axis=0)
    base = trace[z - EMG_BASELINE_MS:z]
    trace = trace - base.mean()
    sd = base.std(ddof=1)
    out = {"m1": float(trace[z + M1_MS[0]:z + M1_MS[1] + 1].mean()),
           "m2": float(trace[z + M2_MS[0]:z + M2_MS[1] + 1].mean()),
           "baseline_sd": float(sd),
           "onset": np.nan, "duration": np.nan}
    above = trace[z:z + 300] > 2 * sd
    for t in range(EMG_SEARCH_MS[0], EMG_SEARCH_MS[1] + 1):
        if above[t]:
            e = t
            while e < len(above) and above[e]:
                e += 1
            out["onset"], out["duration"] = float(t), float(e - t)
            break
    return out


def load_meta(path: str, url: str) -> dict:
    """Trials' perturbation columns and the units table of one file, without the signals."""
    with h5py.File(remfile.File(url), "r") as h:
        tr = h["intervals/trials"]
        u = h["units"]
        acq = h["acquisition"]
        torque = [k for k in acq if k.endswith("Torque")]
        tq = acq[torque[0] + "/data"][:] if torque else np.array([np.nan])
        return {"path": path,
                "torque_type": _str(tr["torque_perturbation_type"][:]),
                "onset": tr["torque_perturbation_onset_time"][:],
                "torque_cmd_finite": int(np.isfinite(tq).sum()),
                "torque_cmd_steps": int((np.abs(np.diff(tq[np.isfinite(tq)])) > 20).sum()),
                "units": pd.DataFrame({"unit_name": _str(u["unit_name"][:]),
                                       "ptype": _str(u["neuron_projection_type"][:]),
                                       "post": u["is_post_mptp"][:].astype(bool),
                                       "latency": u["antidromic_latency_ms"][:]})}


def load_meta_all(paths_urls, workers: int = 8) -> list[dict]:
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(lambda pu: load_meta(*pu), paths_urls))


# ---------------------------------------------------------------- per-cell responses

DIRECTIONS = ["flexion", "extension"]


def cell_responses(files: list[dict]) -> pd.DataFrame:
    """One row per unit: perturbation counts, baseline rate, and the response to each direction
    at the torque onset and at the pseudo onset (prefix `pse_`)."""
    rows = []
    for fi, x in enumerate(files):
        p = x["pert"]
        for ui, u in x["units"].iterrows():
            obs = x["observed"][ui]
            r = {"file": fi, "session": x["session"], "date": x["date"], **u.to_dict()}
            sdfs = []
            for dname in DIRECTIONS:
                d = dname[:3]
                sel = np.where((p.torque == dname).values & obs)[0]
                r[f"n_{d}"] = len(sel)
                if len(sel) == 0:
                    continue
                S = sdf_trials([x["rel_spikes"][ui][i] for i in sel])
                sdfs.append(S)
                m = S.mean(0)
                for k, v in detect(m, 0).items():
                    r[f"{d}_{k}"] = v
                for k, v in detect(m, -PSEUDO_SHIFT_MS).items():
                    r[f"pse_{d}_{k}"] = v
                # Variant of the claims file: one-sample t-test of the single-trial SDFs against
                # the baseline mean at each ms (not deciding).
                z = ms_index(0)
                sig = stats.ttest_1samp(S[:, z:z + EPOCH_MS], r[f"{d}_baseline"], axis=0).pvalue < P_THRESHOLD
                on = [t for t in range(ONSET_WINDOW_MS[0], ONSET_WINDOW_MS[1] + 1) if sig[t] and not sig[t - 1]]
                r[f"{d}_ttest_responds"] = bool(on)
            if sdfs:
                z = ms_index(0)
                r["baseline_rate"] = float(np.vstack(sdfs)[:, z - BASELINE_MS:z].mean())
            rows.append(r)
    return pd.DataFrame(rows)


def pseudo_readings(files: list[dict], studied: set) -> pd.DataFrame:
    """Any threshold crossing over 0 to 200 ms after the pseudo onset (600 ms before torque) and
    after the torque onset, per cell and direction, under four readings of the threshold:
    `mean_sd` the claims file's (SD of the trial-averaged SDF over the baseline), `ttest` the
    claims file's variant, `trial_se` the standard error of the single-trial baseline means,
    `trial_sd` the SD of all single-trial baseline values."""
    rows = []
    for fi, x in enumerate(files):
        p = x["pert"]
        for ui, u in x["units"].iterrows():
            if (fi, ui) not in studied:
                continue
            for dname in DIRECTIONS:
                sel = np.where((p.torque == dname).values & x["observed"][ui])[0]
                S = sdf_trials([x["rel_spikes"][ui][i] for i in sel])
                for label, zero in [("pseudo", -PSEUDO_SHIFT_MS), ("torque", 0)]:
                    z = ms_index(zero)
                    B, post = S[:, z - BASELINE_MS:z], S[:, z:z + EPOCH_MS]
                    mu, m = B.mean(), post.mean(0)
                    bm = B.mean(1)
                    t_n = stats.t.ppf(1 - P_THRESHOLD / 2, len(bm) - 1)
                    rows.append({"file": fi, "unit": ui, "direction": dname, "onset": label,
                                 "mean_sd": bool(np.any(np.abs(m - mu) > T_CRIT * S.mean(0)[z - BASELINE_MS:z].std(ddof=1))),
                                 "ttest": bool(np.any(stats.ttest_1samp(post, mu, axis=0).pvalue < P_THRESHOLD)),
                                 "trial_se": bool(np.any(np.abs(m - mu) > t_n * bm.std(ddof=1) / np.sqrt(len(bm)))),
                                 "trial_sd": bool(np.any(np.abs(m - mu) > T_CRIT * B.std(ddof=1)))})
    return pd.DataFrame(rows)


def no_torque_crossings(files: list[dict], studied: set) -> pd.DataFrame:
    """The claims file's detection on trials without a perturbation, aligned where the file's
    perturbations fall after the centre target (its median delay): a null with no torque at all."""
    rows = []
    for fi, x in enumerate(files):
        t, p = x["trials"], x["pert"]
        if len(p) == 0:
            continue
        delay = np.nanmedian(p.onset - p.center)
        none = t[(t.torque == "none") & np.isfinite(t.center)]
        onsets = (none.center + delay).values
        for ui, u in x["units"].iterrows():
            if (fi, ui) not in studied:
                continue
            ob = x["obs"][ui]
            st = x["spikes_all"][ui]
            w0, w1 = SPIKE_WINDOW_MS[0] / 1000, SPIKE_WINDOW_MS[1] / 1000
            ok = [o for o in onsets if np.any((ob[:, 0] <= o + w0) & (ob[:, 1] >= o + w1))]
            if len(ok) < MIN_PERTURBATIONS:
                continue
            S = sdf_trials([st[(st >= o + w0) & (st < o + w1)] - o for o in ok])
            res = detect(S.mean(0), 0)
            rows.append({"file": fi, "unit": ui, "n_trials": len(ok),
                         "any_crossing": res["any_crossing"], "responds": res["responds"]})
    return pd.DataFrame(rows)


def session_kinematics(files: list[dict]) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Per-perturbation kinematics with the torque command's pulse size, and session means per
    direction. The pulse size is the command over 10 to 50 ms after onset less its mean over the
    50 ms before, signed so that the torque's direction is positive (arbitrary units)."""
    rows = []
    for fi, x in enumerate(files):
        if x["angle"] is None or len(x["pert"]) == 0:
            continue
        dirs = x["pert"].torque.values
        k = kinematics(x["angle"], dirs)
        sign = np.where(dirs == "flexion", 1.0, -1.0)
        z = -TORQUE_WINDOW_MS[0]
        cmd = x["torque_cmd"]
        k["command"] = sign * (cmd[:, z + 10:z + 50].mean(1) - cmd[:, :z].mean(1))
        k["direction"], k["file"], k["session"] = dirs, fi, x["session"]
        k["post"] = bool(x["units"].post.iloc[0])
        rows.append(k)
    trials = pd.concat(rows, ignore_index=True)
    sessions = (trials.groupby(["file", "session", "post", "direction"])
                [["latency", "peak_velocity", "amplitude", "command"]].mean().reset_index())
    return trials, sessions


def session_emg(files: list[dict], channels=TRICEPS, direction: str = "flexion") -> pd.DataFrame:
    """EMG measures of each session and channel for one torque direction. A channel is used when
    no window holds a NaN; `baseline_sd` (of the session-average trace) and `raw_sd` (of the
    single-trial baseline samples) are given for the inclusion rule."""
    rows = []
    z = -EMG_WINDOW_MS[0]
    for fi, x in enumerate(files):
        sel = x["pert"].torque.values == direction
        if sel.sum() == 0:
            continue
        for ch in channels:
            if ch not in x["emg"]:
                continue
            w = x["emg"][ch][sel]
            has_nan = bool(np.isnan(w[:, z - EMG_BASELINE_MS:z + EMG_SEARCH_MS[1] + 1]).any())
            m = emg_measures(w) if not has_nan else {}
            rows.append({"file": fi, "session": x["session"], "post": bool(x["units"].post.iloc[0]),
                         "channel": ch, "n": int(sel.sum()), "has_nan": has_nan,
                         "raw_sd": float(np.nanstd(w[:, z - EMG_BASELINE_MS:z], ddof=1)), **m})
    return pd.DataFrame(rows)
