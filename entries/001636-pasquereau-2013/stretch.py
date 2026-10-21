"""Loading and measures for the torque perturbation (muscle stretch) trials of dandiset 001636.

Pasquereau & Turner (2013), Frontiers in Systems Neuroscience 7:98, doi:10.3389/fnsys.2013.00098.

Each NWB file holds one recording session of one or more single units in M1 of monkey Venus (V,
elbow task) or Leu (L, wrist task): a trials table with the task events and the torque
perturbations, the manipulandum angle, the torque command and, in many Venus sessions, rectified
EMG. Files are streamed from the archive at the pinned version; nothing is written to disk.

Sessions. In the draft of 2026-10-21, source files recorded on the same day and linked in the
lab's metadata table are merged into one session, and a unit is observed only during the trials
of its own source files (its obs_intervals). A unit's perturbations are therefore the perturbation
trials inside its obs_intervals (`load_session` stores them per unit).

Clocks. The source files were trialized; the conversion placed the trials one after another with
3 s gaps. In version 0.260518.1819 the analog streams (angle, torque, EMG) were laid end to end by
their own sample counts and fell further behind the trials table with every trial. `realign` puts
each analog segment back at the start time of its trial; in the draft it moves nothing, which the
notebook shows (the lag it would correct is printed in the data check).

Where the parameters come from:

- The paper's Methods: spike density functions (SDF) made with a causal gamma kernel (k = 1.5,
  theta = 20 ms) at 1 ms resolution; at least 5 perturbations per direction (`MIN_REPS`); the
  baseline as the mean SDF over the 500 ms before torque onset; detection over the 200 ms after
  onset at p < 0.002, two-tailed; responses kept only when they begin 20 to 60 ms after onset;
  the offset where the SDF returns within the threshold; the three magnitude measures and the
  FWHM; the DSI and its categories; the 25 Hz low-pass (Hamming window) and 5 deg/s velocity
  threshold for the joint movement; the EMG baseline (200 ms before onset); the m1 (15 to 40 ms)
  and m2 (41 to 80 ms) windows, from the Results.
- Chosen here, where the Methods leave it open (fixed in the claims file before the analysis):
  the threshold is applied to the trial-averaged SDF, as the mean +/- t * SD of its values over
  the baseline, with t the two-tailed critical value at p = 0.002 (main; Figure 3's horizontal
  threshold lines); the variant is a one-sample t-test of the single-trial SDFs against the
  baseline mean at each ms (`detect(..., method="trials")`). A response begins where the SDF
  crosses the threshold between 20 and 60 ms, having been inside it the ms before. Offsets are
  searched up to 600 ms. The FIR low-pass has 101 taps at 1 kHz (21 at 100 Hz) and is applied
  forwards and backwards. Movement onset is the first time after torque onset that the velocity
  in the torque's direction exceeds 5 deg/s; peak velocity is its maximum over 0 to 200 ms and
  amplitude the largest displacement over 0 to 300 ms from the mean angle of the 50 ms before
  onset. An EMG response lasts while the session-average trace, less its baseline mean, exceeds
  2 SD of the baseline (`EMG_SD`), from its first crossing between 10 and 150 ms.
- Chosen here for the checks and variants added after the first verification: the torque
  command excursion threshold (`COMMAND_EXCURSION`, under half the smallest monkey V pulse), the
  window for measuring active movements (`ACTIVE_WINDOW_MS`), and the causal velocity average for
  the movement latency variant (`CAUSAL_MS`).
"""

from __future__ import annotations

from concurrent.futures import ProcessPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy import signal, stats

DANDISET_ID = "001636"
DANDISET_VERSION = "draft"            # asked for; its modification time is printed by the notebook

MIN_REPS = 5
GAMMA_K, GAMMA_THETA_MS = 1.5, 20.0
KERNEL_MS = 400                 # kernel length; holds more than 99.9% of its mass
SPIKE_WINDOW_S = (-1.8, 0.7)    # spikes kept around each torque onset
GRID_MS = (-1400, 600)          # SDF grid around onset (the kernel needs 400 ms before)
BASELINE_MS = (-500, 0)
DETECT_MS = (0, 200)
ONSET_RANGE_MS = (20, 60)
P_THRESHOLD = 0.002
PSEUDO_ONSET_MS = -600          # pseudo onset for the false-positive check, inside the hold

ANALOG_WINDOW_MS = (-500, 500)
LOWPASS_HZ = 25.0
VEL_THRESHOLD = 5.0             # deg/s
PEAK_VEL_MS, AMPLITUDE_MS = 200, 300
EMG_BASELINE_MS = (-200, 0)
M1_MS, M2_MS = (15, 40), (41, 80)
EMG_SEARCH_MS = (10, 150)
EMG_SD = 2.0
EMG_CHANNELS = ("EMGTricepsLongus1", "EMGTricepsLongus2", "EMGTricepsLateralis",
                "EMGBrachioradialis", "EMGDeltoidPosterior", "EMGTrapezius")
SIGN = {"flexion": 1.0, "extension": -1.0}   # flexion torque raises the stored angle (checked)
HOLD_WINDOW_S = (1.0, 2.5)      # after the center target appears; holds the torque onsets
ACTIVE_WINDOW_MS = (-200, 800)  # around derived_movement_onset_time, for the angle scale check
COMMAND_EXCURSION = 20.0        # torque command units from rest; the smallest monkey V pulse is ~46
CAUSAL_MS = 10                  # causal moving average of the unfiltered velocity (latency variant)


EARLIER_VERSION = "0.260518.1819"  # used by attempt 001636-pasquereau-2013-01; compared in the data check


def asset_urls(version: str = DANDISET_VERSION) -> list[tuple[str, str]]:
    """(path, streaming URL) of every NWB file at a version (the pinned one by default)."""
    with DandiAPIClient() as client:
        dandiset = client.get_dandiset(DANDISET_ID, version)
        return sorted((a.path, a.get_content_url(follow_redirects=1, strip_query=True))
                      for a in dandiset.get_assets() if a.path.endswith(".nwb"))


def version_info() -> dict:
    """The pinned version's identifier, modification time and asset count, from the archive."""
    with DandiAPIClient() as client:
        d = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        v = d.version
        return {"version": v.identifier, "modified": str(v.modified), "assets": v.asset_count}


def _text(value) -> str:
    return value.decode() if isinstance(value, bytes) else str(value)


def realign(timestamps: np.ndarray, trial_starts: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Analog timestamps moved so that each trial's segment begins at its trial's start time.

    Segments are separated by gaps over 1 s. Returns the moved timestamps and the index of each
    segment's first sample. Raises if the number of segments differs from the number of trials.
    """
    first = np.r_[0, np.flatnonzero(np.diff(timestamps) > 1.0) + 1]
    if len(first) != len(trial_starts):
        raise ValueError(f"{len(first)} analog segments for {len(trial_starts)} trials")
    shift = np.repeat(trial_starts - timestamps[first], np.diff(np.r_[first, len(timestamps)]))
    return timestamps + shift, first


def _window(t: np.ndarray, x: np.ndarray, t0: float, ms: tuple[int, int], step_ms: int) -> np.ndarray:
    """x sampled on t, read at t0 + ms[0] .. ms[1] in steps of step_ms (nearest sample, NaN outside)."""
    grid = t0 + np.arange(ms[0], ms[1] + 1, step_ms) / 1000
    i = np.clip(np.searchsorted(t, grid), 1, len(t) - 1)
    i = np.where(np.abs(t[i - 1] - grid) < np.abs(t[i] - grid), i - 1, i)
    out = x[i].astype(float)
    out[np.abs(t[i] - grid) > step_ms / 2000 + 1e-6] = np.nan
    return out


def load_session(path: str, url: str) -> dict:
    """One file: metadata, trials, units (with spikes around each perturbation), analog windows."""
    with h5py.File(remfile.File(url), "r") as f:
        session_id = _text(f["general/session_id"][()])
        tr = f["intervals/trials"]
        trials = pd.DataFrame({
            "start": tr["start_time"][:], "stop": tr["stop_time"][:],
            "center_on": tr["center_target_appearance_time"][:],
            "lateral_on": tr["lateral_target_appearance_time"][:],
            "reward": tr["reward_time"][:],
            "torque": [_text(v) for v in tr["torque_perturbation_type"][:]],
            "source_file": ([_text(v) for v in tr["source_file"][:]] if "source_file" in tr
                            else [path] * len(tr["start_time"])),
            "onset": tr["torque_perturbation_onset_time"][:],
            "movement": [_text(v) for v in tr["movement_type"][:]],
            "end_position": tr["derived_end_position"][:],
            "target_amplitude": tr["target_amplitude_degrees"][:],
            "derived_onset": tr["derived_movement_onset_time"][:],
            "derived_amplitude": tr["derived_movement_amplitude"][:],
            "derived_peak_velocity": tr["derived_peak_velocity"][:],
        })
        un = f["units"]
        data, index = un["spike_times"][:], un["spike_times_index"][:]
        spikes = np.split(data, index[:-1])
        obs = np.split(un["obs_intervals"][:], un["obs_intervals_index"][:-1]) if "obs_intervals" in un else None
        units = [{"unit_name": _text(un["unit_name"][i]),
                  "type": _text(un["neuron_projection_type"][i]),
                  "antidromic_latency_ms": float(un["antidromic_latency_ms"][i]),
                  "also_in": _text(un["unit_also_in_session_id"][i]) if "unit_also_in_session_id" in un else "",
                  "is_post_mptp": bool(un["is_post_mptp"][i]),
                  "obs": obs[i] if obs is not None else None,
                  "spikes": spikes[i]} for i in range(len(un["id"]))]
        has_also_in = "unit_also_in_session_id" in un
        acq = sorted(f["acquisition"].keys())
        raw = {}
        joint = "Elbow" if "ElbowAngle" in acq else "Wrist" if "WristAngle" in acq else None
        frame = None
        if joint:
            raw["t"] = f[f"acquisition/{joint}Angle/timestamps"][:]
            raw["angle"] = f[f"acquisition/{joint}Angle/data"][:, 0]
            raw["torque_cmd"] = f[f"acquisition/{joint}Torque/data"][:]
            if "reference_frame" in f[f"acquisition/{joint}Angle"]:
                frame = _text(f[f"acquisition/{joint}Angle/reference_frame"][()])
            raw["emg_same_clock"] = True
            for name in EMG_CHANNELS:
                if name in acq:
                    raw[name] = f[f"acquisition/{name}/data"][:]
                    ts = f[f"acquisition/{name}/timestamps"][:]
                    raw["emg_same_clock"] &= bool(np.array_equal(ts, raw["t"]))
    subject, _, state, depth, date = session_id.split("++")
    s = {"path": path, "session_id": session_id, "subject": subject, "post": state == "PostMPTP",
         "date": pd.Timestamp(date), "acq": acq, "trials": trials, "units": units,
         "has_also_in_column": has_also_in, "joint": joint, "angle_reference_frame": frame}
    pert = trials[trials.torque.isin(["flexion", "extension"])]
    for u in units:
        sp = u["spikes"]
        u["sorted"] = bool(np.all(np.diff(sp) >= 0))
        k = np.searchsorted(trials.start.values, sp, side="right") - 1
        u["outside_trials"] = int(np.sum((k < 0) | (sp > trials.stop.values[np.clip(k, 0, None)] + 1e-6)))
        isi = np.diff(sp)[np.diff(k) == 0]
        u["isi_below_2ms"] = float(np.mean(isi < 0.002)) if len(isi) else np.nan
        # trials inside the unit's observation intervals (all trials when the file gives none)
        if u["obs"] is None or len(u["obs"]) == 0:
            seen = np.ones(len(trials), bool)
        else:
            seen = np.zeros(len(trials), bool)
            for a, b in u["obs"]:
                seen |= (trials.start.values >= a - 1e-6) & (trials.stop.values <= b + 1e-6)
            inside = np.zeros(len(sp), bool)
            for a, b in u["obs"]:
                inside |= (sp >= a - 1e-6) & (sp <= b + 1e-6)
            u["outside_obs"] = int((~inside).sum())
        u["observed_trials"] = seen
        p = pert[seen[pert.index.values]]
        u["pert_direction"] = p.torque.values
        u["pert_trial"] = p.index.values
        u["pert"] = [np.round((sp[(sp >= t0 + SPIKE_WINDOW_S[0]) & (sp < t0 + SPIKE_WINDOW_S[1])] - t0) * 1000)
                     for t0 in p.onset.values]
    s["pert_direction"] = pert.torque.values
    s["pert_trial"] = pert.index.values
    if not raw:
        return s
    t = raw["t"]
    s["analog_dt_ms"] = float(np.median(np.diff(t)) * 1000)
    s["angle_all_nan"] = bool(np.isnan(raw["angle"]).all())
    s["torque_all_nan"] = bool(np.isnan(raw["torque_cmd"]).all())
    s["emg_same_clock"] = raw["emg_same_clock"]
    s["emg_channels"] = [c for c in EMG_CHANNELS if c in raw]
    t_al, first = realign(t, trials.start.values)
    s["analog_lag_ms"] = (trials.start.values - t[first]) * 1000
    # largest excursion of the angle from its median in the hold window of every trial, and the
    # angle change over each active movement (lateral target to reward)
    exc, move = [], []
    for c, lat, rew in zip(trials.center_on.values, trials.lateral_on.values, trials.reward.values):
        m = (t_al >= c + HOLD_WINDOW_S[0]) & (t_al < min(c + HOLD_WINDOW_S[1], lat))
        a = raw["angle"][m]
        exc.append(float(np.nanmax(np.abs(a - np.nanmedian(a)))) if m.sum() > 2 and not np.isnan(a).all() else np.nan)
        i0, i1 = np.searchsorted(t_al, [lat, rew])
        move.append(float(raw["angle"][min(i1, len(t_al) - 1)] - raw["angle"][min(i0, len(t_al) - 1)])
                    if np.isfinite(lat) and np.isfinite(rew) else np.nan)
    trials["hold_excursion_deg"] = exc
    trials["active_angle_change"] = move
    step = max(1, int(round(s["analog_dt_ms"])))
    s["analog_step_ms"] = step
    # active movements measured as the torque-induced ones are, around the file's own movement onset
    act = [active_movement(_window(t_al, raw["angle"], t0, ACTIVE_WINDOW_MS, step), step)
           if np.isfinite(t0) else (np.nan, np.nan) for t0 in trials.derived_onset.values]
    trials["active_peak_velocity"] = [a for a, _ in act]
    trials["active_amplitude"] = [b for _, b in act]
    if not s["torque_all_nan"]:
        s["command_excursions"] = command_excursions(t_al, raw["torque_cmd"], trials)
    w = {}
    for name in ["angle", "torque_cmd", *s["emg_channels"]]:
        w[name] = np.array([_window(t_al, raw[name], t0, ANALOG_WINDOW_MS, step) for t0 in pert.onset.values])
    # the torque command on the stored clock, for the data check
    w["torque_cmd_stored"] = np.array([_window(t, raw["torque_cmd"], t0, ANALOG_WINDOW_MS, step)
                                       for t0 in pert.onset.values])
    s["windows"] = w
    return s


def command_excursions(t: np.ndarray, cmd: np.ndarray, trials: pd.DataFrame) -> pd.DataFrame:
    """Every excursion of the torque command more than COMMAND_EXCURSION units from the file's
    median, on the realigned clock: its trial, start relative to the center and lateral targets'
    appearance, duration, signed peak, and whether it starts in the hold window (HOLD_WINDOW_S
    after the center target, before the lateral target)."""
    rest = np.nanmedian(cmd)
    out = np.abs(cmd - rest) > COMMAND_EXCURSION
    edges = np.diff(np.r_[False, out, False].astype(int))
    starts, stops = np.flatnonzero(edges == 1), np.flatnonzero(edges == -1)
    k = np.searchsorted(trials.start.values, t[starts], side="right") - 1
    ok = k >= 0
    starts, stops, k = starts[ok], stops[ok], k[ok]
    rel_center = t[starts] - trials.center_on.values[k]
    rel_lateral = t[starts] - trials.lateral_on.values[k]
    peak = [float((cmd[a:b] - rest)[np.nanargmax(np.abs(cmd[a:b] - rest))]) for a, b in zip(starts, stops)]
    return pd.DataFrame({
        "trial": k, "from_center_s": rel_center, "from_lateral_s": rel_lateral,
        "duration_ms": (t[np.minimum(stops, len(t) - 1)] - t[starts]) * 1000, "peak": peak,
        "in_hold": (rel_center >= HOLD_WINDOW_S[0]) & (rel_center < HOLD_WINDOW_S[1])
                   & ~(rel_lateral >= 0),
        "torque_label": trials.torque.values[k]})


def load_units_brief(path: str, url: str) -> list[dict]:
    """Units of one file with their perturbations per direction, without spikes or analog data
    (for comparing versions). Perturbations are counted within the unit's obs_intervals when the
    file merges source files (a trials column source_file), and over the whole file otherwise."""
    with h5py.File(remfile.File(url), "r") as f:
        session_id = _text(f["general/session_id"][()])
        tr = f["intervals/trials"]
        torque = np.array([_text(v) for v in tr["torque_perturbation_type"][:]])
        start, stop = tr["start_time"][:], tr["stop_time"][:]
        merged = "source_file" in tr
        un = f["units"]
        obs = np.split(un["obs_intervals"][:], un["obs_intervals_index"][:-1]) if merged else None
        out = []
        for i in range(len(un["id"])):
            seen = np.ones(len(start), bool)
            if merged:
                seen = np.zeros(len(start), bool)
                for a, b in obs[i]:
                    seen |= (start >= a - 1e-6) & (stop <= b + 1e-6)
            name = _text(un["unit_name"][i])
            code = session_id.split("++")[1]
            out.append({"path": path, "code": code, "subject": session_id.split("++")[0],
                        "post": session_id.split("++")[2] == "PostMPTP",
                        "unit_name": name if merged else f"{code}.{name}",
                        "type": _text(un["neuron_projection_type"][i]),
                        "n_flex": int((torque[seen] == "flexion").sum()),
                        "n_ext": int((torque[seen] == "extension").sum())})
    return out


def _load_brief(pu):
    return load_units_brief(*pu)


def load_all_brief(paths_urls, workers: int = 16) -> list[dict]:
    with ProcessPoolExecutor(workers) as pool:
        return [u for f in pool.map(_load_brief, paths_urls, chunksize=4) for u in f]


def _load(pu):
    return load_session(*pu)


def load_all(paths_urls, workers: int = 16) -> list[dict]:
    """Every file, in parallel processes (h5py serializes calls within a process)."""
    with ProcessPoolExecutor(workers) as pool:
        return list(pool.map(_load, paths_urls, chunksize=2))


# ---------------------------------------------------------------- spike density and detection

def gamma_kernel() -> np.ndarray:
    """Causal gamma kernel (k = 1.5, theta = 20 ms) at 1 ms steps, in spikes/s per spike."""
    t = np.arange(KERNEL_MS) + 0.5
    k = stats.gamma.pdf(t, a=GAMMA_K, scale=GAMMA_THETA_MS)
    return 1000 * k / k.sum()


_KERNEL = gamma_kernel()
GRID = np.arange(*GRID_MS)


def sdfs(rel_ms: list[np.ndarray]) -> np.ndarray:
    """Single-trial SDFs (trials x GRID) from spike times in whole ms relative to onset."""
    lo, n = GRID_MS[0] - KERNEL_MS, GRID_MS[1] - GRID_MS[0] + KERNEL_MS
    out = np.empty((len(rel_ms), len(GRID)))
    for i, r in enumerate(rel_ms):
        r = r[(r >= lo) & (r < GRID_MS[1])].astype(int) - lo
        counts = np.bincount(r, minlength=n)
        out[i] = np.convolve(counts, _KERNEL)[KERNEL_MS:n]
    return out


def _mask(lo, hi, shift=0):
    return (GRID >= lo + shift) & (GRID < hi + shift)


def detect(trial_sdfs: np.ndarray, shift_ms: int = 0, method: str = "mean", tcrit: float | None = None) -> dict:
    """Response of one cell to one torque direction.

    method "mean" (main): the trial-averaged SDF against mean +/- t_crit * SD of its own values
    over the 500 ms baseline; tcrit replaces the critical value (for the calibrated variant).
    method "trials" (variant): one-sample two-tailed t-test of the single-trial SDFs against the
    baseline mean, at each ms. shift_ms moves the onset (for the false-positive check). Returns
    the baseline, the baseline SD of the mean SDF, the signed largest change over 0 to 200 ms and
    its size in baseline SDs, the first threshold crossing in 0 to 200 ms, and for a response its
    sign, onset, offset, magnitudes and FWHM.
    """
    m = trial_sdfs.mean(0)
    b = m[_mask(*BASELINE_MS, shift_ms)]
    mu = float(b.mean())
    post = GRID >= shift_ms
    mp = m[post]
    if method == "mean":
        if tcrit is None:
            tcrit = stats.t.ppf(1 - P_THRESHOLD / 2, len(b) - 1)
        thr = tcrit * b.std(ddof=1)
        up, down = mp > mu + thr, mp < mu - thr
        if thr == 0:          # no spikes in the baseline: any spike is not a test
            up = down = np.zeros_like(mp, bool)
    else:
        with np.errstate(all="ignore"):
            p = stats.ttest_1samp(trial_sdfs[:, post], mu, axis=0).pvalue
        sig = np.where(np.isfinite(p), p, 1.0) < P_THRESHOLD
        up, down = sig & (mp > mu), sig & (mp < mu)
    d = mp[:DETECT_MS[1]] - mu
    sd = float(b.std(ddof=1))
    crossing = up[:DETECT_MS[1]] | down[:DETECT_MS[1]]
    out = {"baseline": mu, "baseline_sd": sd, "n_trials": len(trial_sdfs), "responds": False,
           "max_change_signed": float(d[np.argmax(np.abs(d))]),
           "max_abs_z": float(np.abs(d).max() / sd) if sd > 0 else np.nan,
           "any_crossing_0_200": bool(crossing.any()),
           "first_crossing": int(np.argmax(crossing)) if crossing.any() else np.nan}
    start = None
    for t in range(ONSET_RANGE_MS[0], ONSET_RANGE_MS[1] + 1):
        if up[t] and not up[t - 1]:
            start, sign, beyond = t, 1.0, up
            break
        if down[t] and not down[t - 1]:
            start, sign, beyond = t, -1.0, down
            break
    if start is None:
        return out
    rest = np.flatnonzero(~beyond[start:])
    off = start + int(rest[0]) if len(rest) else len(mp)
    ch = (mp - mu) * sign
    resp = ch[start:off]
    peak = start + int(np.argmax(resp))
    half = ch[peak] / 2
    left, right = peak, peak
    while left > 0 and ch[left - 1] >= half:
        left -= 1
    while right < len(ch) - 1 and ch[right + 1] >= half:
        right += 1
    out.update(responds=True, sign=sign, latency=start, offset=off,
               mean_rate=float(mp[start:off].mean()), mean_change=float(resp.mean()),
               max_change=float(resp.max()), auc=float(resp.sum() / 1000),
               fwhm=float(right - left + 1))
    return out


def dsi(flex: dict, ext: dict) -> tuple[float, str]:
    """Directional selectivity index |1 - NP/P| and the cell's category.

    P and NP are the signed largest changes from baseline over 0 to 200 ms in the preferred
    (larger absolute change) and the other direction. Category, for a torque-related cell:
    unidirectional when only one direction has a response; with both, reciprocal when they have
    opposite signs, bidirectional when DSI > 0.5, otherwise non-directional.
    """
    a, b = flex["max_change_signed"], ext["max_change_signed"]
    p, nonp = (a, b) if abs(a) >= abs(b) else (b, a)
    index = abs(1 - nonp / p) if p != 0 else np.nan
    if flex["responds"] and ext["responds"]:
        if flex["sign"] != ext["sign"]:
            cat = "reciprocal"
        else:
            cat = "bidirectional" if index > 0.5 else "non-directional"
    elif flex["responds"] or ext["responds"]:
        cat = "unidirectional"
    else:
        cat = "none"
    return float(index), cat


# ---------------------------------------------------------------- kinematics and EMG

def _lowpass(angle: np.ndarray, step_ms: int) -> np.ndarray:
    fs = 1000 / step_ms
    taps = 101 if step_ms == 1 else 21
    fir = signal.firwin(taps, LOWPASS_HZ, fs=fs, window="hamming")
    return signal.filtfilt(fir, [1.0], angle)


def kinematics(angle: np.ndarray, direction: str, step_ms: int) -> dict:
    """Torque-evoked displacement of one trial from its angle window (ANALOG_WINDOW_MS).

    latency_causal_ms is a variant onset: the unfiltered velocity averaged over the preceding
    CAUSAL_MS (causal, so it cannot move the onset earlier; it delays it by up to CAUSAL_MS / 2).
    """
    if np.isnan(angle).any():
        return {"valid": False}
    fs = 1000 / step_ms
    smooth = _lowpass(angle, step_ms)
    ax = np.arange(ANALOG_WINDOW_MS[0], ANALOG_WINDOW_MS[1] + 1, step_ms)
    s = SIGN[direction]
    vel = np.gradient(smooth) * fs * s
    rel = (smooth - smooth[(ax >= -50) & (ax < 0)].mean()) * s
    after = ax >= 0
    v, a, t = vel[after], rel[after], ax[after]
    cross = np.flatnonzero((v > VEL_THRESHOLD) & (t <= 150))
    n = max(1, CAUSAL_MS // step_ms)
    raw_v = np.r_[0.0, np.diff(angle)] * fs * s
    causal = np.convolve(raw_v, np.ones(n) / n)[:len(raw_v)]
    cross_c = np.flatnonzero((causal[after] > VEL_THRESHOLD) & (t <= 150))
    return {"valid": True,
            "moving_before": bool(np.abs(vel[(ax >= -50) & (ax < 0)]).max() > VEL_THRESHOLD),
            "latency_ms": float(t[cross[0]]) if len(cross) else np.nan,
            "latency_causal_ms": float(t[cross_c[0]]) if len(cross_c) else np.nan,
            "peak_velocity": float(v[t <= PEAK_VEL_MS].max()),
            "amplitude": float(a[t <= AMPLITUDE_MS].max())}


def active_movement(angle: np.ndarray, step_ms: int) -> tuple[float, float]:
    """Peak absolute velocity (deg/s) and largest displacement from the 100 ms before onset (deg)
    of an active movement, from its angle window (ACTIVE_WINDOW_MS), filtered as in kinematics."""
    if np.isnan(angle).any():
        return np.nan, np.nan
    smooth = _lowpass(angle, step_ms)
    ax = np.arange(ACTIVE_WINDOW_MS[0], ACTIVE_WINDOW_MS[1] + 1, step_ms)
    vel = np.gradient(smooth) * 1000 / step_ms
    disp = smooth - smooth[(ax >= -100) & (ax < 0)].mean()
    after = ax >= 0
    return float(np.abs(vel[after]).max()), float(np.abs(disp[after]).max())


def emg_response(traces: np.ndarray, step_ms: int, sd: float = EMG_SD) -> dict:
    """Session-average EMG response from trials x window traces, baseline subtracted."""
    ax = np.arange(ANALOG_WINDOW_MS[0], ANALOG_WINDOW_MS[1] + 1, step_ms)
    mean = np.nanmean(traces, axis=0)
    b = (ax >= EMG_BASELINE_MS[0]) & (ax < EMG_BASELINE_MS[1])
    norm = mean - mean[b].mean()
    thr = sd * mean[b].std(ddof=1)
    above = (norm > thr) & (ax >= EMG_SEARCH_MS[0])
    cand = np.flatnonzero(above & (ax <= EMG_SEARCH_MS[1]))
    out = {"m1": float(norm[(ax >= M1_MS[0]) & (ax <= M1_MS[1])].mean()),
           "m2": float(norm[(ax >= M2_MS[0]) & (ax <= M2_MS[1])].mean()),
           "onset_ms": np.nan, "duration_ms": np.nan, "trace": norm, "ax": ax}
    if len(cand):
        i0 = cand[0]
        rest = np.flatnonzero(~above[i0:])
        i1 = i0 + int(rest[0]) if len(rest) else len(ax)
        out.update(onset_ms=float(ax[i0]), duration_ms=float((i1 - i0) * step_ms))
    return out


def short_type(t: str) -> str:
    return {"pyramidal_tract_neuron": "PTN", "corticostriatal_neuron": "CSN",
            "pyramidal_tract_and_corticostriatal_neuron": "dual"}.get(t, "NA")
