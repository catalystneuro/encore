"""Loading and measures for dandiset 002013 (shaft-assisted microinvasive probes in monkeys).

Amjad, Mahajan, Choi, Shrivastav, Murray, Somich, Coyne & Schwerdt (2025), ACS Chemical
Neuroscience 16:2237-2247, doi:10.1021/acschemneuro.5c00071.

The dandiset holds three NWB files, streamed here from the archive at the pinned version;
nothing is written to disk:

- Monkey T, 09/13/2024 (shape task): raw FSCV current and applied voltage from site c8dg, a
  trials table, an events table, and trial-aligned FSCV series (dopamine `da`, `ph`, motion `m`,
  oxidation current `iox`; 10 Hz, 60 s per trial, trial start at sample 300).
- Monkey T, 09/26/2024 (direction task): raw broadband ephys from sites c3bs and c3a (32 kHz), a
  bipolar LFP (c3bs referenced to c3a, 1 kHz), a trials table and an events table.
- Monkey P, 08/13/2018: raw broadband ephys from one site (30 kHz), Plexon-sorted units and
  threshold-detected spikes with waveforms. No trials or events.

The trials tables hold only times. Conditions are decoded from the events table, in which each
event is repeated once for every 60 s trial window that contains it; `load_events` keeps each
distinct time once.

Where the parameters come from:

- Trial structure, codes and their names: the files' events tables. A trial runs from one
  "intended trial start" (code 128) to the next; its value cue is the first "value object start"
  (code 23). Reward size and side codes are listed in `CODES`. The choice that a forced shape-task
  trial with feedback but without the big-reward code is a small-reward trial is made here (the
  session has no small-reward code); `shape_task_trials` reports how it agrees with the cue
  condition codes.
- Beta power: the Methods (band 13 to 28 Hz, squared, enveloped, smoothed with a 0.25 s Hanning
  window). The filter type and order are not given; a 4th-order Butterworth run forwards and
  backwards and the squared Hilbert envelope are common choices.
- Dopamine re-referencing at the value cue: the Methods (background subtraction at the value cue).
- Spike sorting conventions: the paper's spikes_PCA.m (Zenodo doi:10.5281/zenodo.10397773) takes
  Plexon unit 1 as the sorted unit and unit 0 as unsorted.
- Monkey P's clock offset: the time of the first event ("Starting Recording") in the session's
  Neuralynx events file on Zenodo (doi:10.5281/zenodo.14826579, session126_events.mat), read by
  `zenodo_events`.
- Burst threshold (75th percentile, at least 50 ms) and the noise estimate for spikes (median
  absolute deviation / 0.6745 of the 300 to 6000 Hz band) are common choices; the paper gives
  none.
"""

from __future__ import annotations

import io
import urllib.parse
import urllib.request

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy import io as sio
from scipy import signal

DANDISET_ID = "002013"
DANDISET_VERSION = "0.261012.0921"

PATHS = {
    "T-0913": "sub-Monkey-T/sub-Monkey-T_ses-09132024_ecephys.nwb",
    "T-0926": "sub-Monkey-T/sub-Monkey-T_ses-09262024_ecephys.nwb",
    "P-0813": "sub-Monkey-P/sub-Monkey-P_ses-08132018_ecephys.nwb",
}

CODES = {
    "trial_start": 128, "value_cue": 23, "feedback": 21, "big_reward": 101, "small_reward": 100,
    "left": 117, "right": 118, "forced": 119, "choice": 120, "image_1": 81, "image_8": 88,
    "cue_reward_1": 35, "cue_reward_2": 36,
}

TRIAL_HALF_WINDOW_S = 30.0      # trials table: start = trial start - 30 s, stop = + 30 s
FSCV_RATE = 10.0                # trial-aligned FSCV, samples per second
FSCV_ZERO_SAMPLE = 300          # trial start within the 601-sample trial-aligned FSCV series
LFP_RATE = 1000.0
BETA_BAND = (13.0, 28.0)        # Methods
BETA_ORDER = 4                  # common choice
BETA_SMOOTH_S = 0.25            # Methods, Hanning window
BURST_PERCENTILE = 75.0         # common choice
BURST_MIN_S = 0.05              # one cycle at 20 Hz
SPIKE_BAND = (300.0, 6000.0)    # common choice for the noise estimate

ZENODO_DATA = "https://zenodo.org/api/records/14826579/files/{}/content"


def asset_url(key: str) -> str:
    with DandiAPIClient() as client:
        asset = client.get_dandiset(DANDISET_ID, DANDISET_VERSION).get_asset_by_path(PATHS[key])
        return asset.get_content_url(follow_redirects=1, strip_query=True)


def dandiset_metadata() -> dict:
    with DandiAPIClient() as client:
        return client.get_dandiset(DANDISET_ID, DANDISET_VERSION).get_raw_metadata()


def open_file(key: str) -> h5py.File:
    return h5py.File(remfile.File(asset_url(key)), "r")


def text(f: h5py.File, path: str) -> str:
    v = f[path][()]
    return v.decode() if isinstance(v, bytes) else str(v)


# ---------------------------------------------------------------------------------- events

def load_events(f: h5py.File) -> tuple[dict, pd.DataFrame]:
    """Distinct event times per code, and a table of codes, labels and counts."""
    e = f["processing/events/events_table"]
    ends = e["event_times_index"][:]
    times = e["event_times"][:]
    events, rows, start = {}, [], 0
    for i, label in enumerate(e["label"][:]):
        t = times[start:ends[i]]
        start = ends[i]
        code = int(e["event_description"][i].decode().split("'")[1])
        events[code] = np.unique(np.round(t, 6))
        rows.append({"code": code, "label": label.decode(), "n_stored": len(t), "n_distinct": len(events[code])})
    return events, pd.DataFrame(rows).sort_values("code").reset_index(drop=True)


def trial_starts(f: h5py.File) -> np.ndarray:
    return f["intervals/trials/midpoint_time"][:]


def codes_per_trial(events: dict, starts: np.ndarray) -> pd.DataFrame:
    """For each trial (start to next start) whether each code occurs, and the value cue time."""
    edges = np.r_[starts, np.inf]
    out = {}
    for code, t in events.items():
        k = np.searchsorted(edges, t, side="right") - 1
        out[code] = np.bincount(k[k >= 0], minlength=len(starts)) > 0
    df = pd.DataFrame(out)
    vc = events[CODES["value_cue"]]
    k = np.searchsorted(vc, starts)
    v = np.where(k < len(vc), vc[np.minimum(k, len(vc) - 1)], np.nan)
    nxt = np.r_[starts[1:], np.inf]
    df["value_cue"] = np.where(v < nxt, v, np.nan)
    fb = events.get(CODES["feedback"], np.array([]))
    k = np.searchsorted(fb, starts)
    w = np.where(k < len(fb), fb[np.minimum(k, len(fb) - 1)], np.nan) if len(fb) else np.full(len(starts), np.nan)
    df["feedback"] = np.where(w < nxt, w, np.nan)
    df["start"] = starts
    df.index = np.arange(1, len(starts) + 1)   # trial numbers as in the paper's lists
    df.index.name = "trial"
    return df


def direction_task_trials(f: h5py.File) -> pd.DataFrame:
    events, _ = load_events(f)
    c = codes_per_trial(events, trial_starts(f))
    big, small = c[CODES["big_reward"]], c[CODES["small_reward"]]
    return pd.DataFrame({
        "start": c["start"], "value_cue": c["value_cue"], "feedback": c["feedback"],
        "success": big | small, "big": big, "small": small,
        "left": c[CODES["left"]], "right": c[CODES["right"]],
    })


def shape_task_trials(f: h5py.File) -> pd.DataFrame:
    events, _ = load_events(f)
    c = codes_per_trial(events, trial_starts(f))
    forced = c[CODES["forced"]]
    success = forced & c[CODES["feedback"]]
    return pd.DataFrame({
        "start": c["start"], "value_cue": c["value_cue"], "feedback": c["feedback"],
        "forced": forced, "choice": c[CODES["choice"]], "success": success,
        "big": success & c[CODES["big_reward"]], "small": success & ~c[CODES["big_reward"]],
        "cue_reward_1": c[CODES["cue_reward_1"]], "cue_reward_2": c[CODES["cue_reward_2"]],
        "image_1": c[CODES["image_1"]], "image_8": c[CODES["image_8"]],
        "left": c[CODES["left"]], "right": c[CODES["right"]],
    })


def reward_blocks(trials: pd.DataFrame) -> pd.DataFrame:
    """Blocks of the shape task: runs in which the same image signals the large reward."""
    s = trials[trials.success]
    big_image = np.where(s.big, np.where(s.image_1, 1, 8), np.where(s.image_1, 8, 1))
    change = np.where(np.diff(big_image) != 0)[0]
    first = [int(trials.index[0])] + [int(s.index[i]) + 1 for i in change]
    last = [b - 1 for b in first[1:]] + [int(trials.index[-1])]
    images = [big_image[0]] + [big_image[i + 1] for i in change]
    n = len(first)
    return pd.DataFrame({"first_trial": first, "last_trial": last,
                         "n_trials": np.array(last) - np.array(first) + 1, "large_reward_image": images,
                         "complete": [0 < i < n - 1 for i in range(n)]})


# ------------------------------------------------------------------------------------ FSCV

def fscv_table(f: h5py.File) -> dict:
    """Trial-aligned FSCV series, with the trial number of each row (matched by start time)."""
    t = f["processing/fscv/trial_aligned_fscv_table"]
    starts = f["intervals/trials/start_time"][:]
    rs = t["start_time"][:]
    k = np.searchsorted(starts, rs)
    if not np.allclose(starts[k], rs):
        raise ValueError("trial-aligned FSCV rows do not match trial start times")
    return {"trial": k + 1, "start": rs, "good": t["good"][:], "rate": t["rate"][:],
            **{name: t[name][:] for name in ("da", "ph", "m", "iox")}}


def rereference(series: np.ndarray, rows: np.ndarray, at_s: np.ndarray) -> np.ndarray:
    """Each row minus its value at `at_s` seconds from the trial start (nearest sample)."""
    idx = np.round(FSCV_ZERO_SAMPLE + at_s * FSCV_RATE).astype(int)
    x = series[rows]
    return x - x[np.arange(len(rows)), idx][:, None]


def fscv_window_mean(x: np.ndarray, cue_s: np.ndarray, a: float, b: float) -> np.ndarray:
    """Mean of each row over [a, b) seconds after the cue (cue given in s from trial start)."""
    out = np.empty(len(x))
    for j in range(len(x)):
        i0 = int(round(FSCV_ZERO_SAMPLE + (cue_s[j] + a) * FSCV_RATE))
        i1 = int(round(FSCV_ZERO_SAMPLE + (cue_s[j] + b) * FSCV_RATE))
        out[j] = np.nanmean(x[j, i0:i1])
    return out


def fscv_aligned(x: np.ndarray, cue_s: np.ndarray, pre_s: float, post_s: float) -> tuple[np.ndarray, np.ndarray]:
    """Rows re-cut around the cue, on a 10 Hz grid from -pre_s to post_s."""
    n0, n1 = int(round(pre_s * FSCV_RATE)), int(round(post_s * FSCV_RATE))
    out = np.full((len(x), n0 + n1 + 1), np.nan)
    for j in range(len(x)):
        c = int(round(FSCV_ZERO_SAMPLE + cue_s[j] * FSCV_RATE))
        out[j] = x[j, c - n0:c + n1 + 1]
    return np.arange(-n0, n1 + 1) / FSCV_RATE, out


def raw_fscv(f: h5py.File) -> dict:
    """Raw FSCV current per scan (scans x samples), scan start times and the applied waveform."""
    r = f["acquisition/fscv_response_series"]
    v = f["stimulus/presentation/fscv_excitation_series"]
    t = r["timestamps"][:]
    starts = np.r_[0, np.where(np.diff(t) > 1e-3)[0] + 1]
    n = int(np.median(np.diff(starts)))
    if not np.all(np.diff(starts) == n) or len(t) - starts[-1] != n:
        raise ValueError("scans of unequal length")
    return {"current": r["data"][:].reshape(-1, n), "scan_start": t[starts], "t": t,
            "volts": v["data"][:n], "volts_first": v["data"][:n * 50],
            "attrs": {k: r.attrs[k] for k in r.attrs if k not in ("object_id",)},
            "excitation_attrs": {k: v.attrs[k] for k in v.attrs if k not in ("object_id",)},
            "excitation_data_attrs": dict(v["data"].attrs), "current_data_attrs": dict(r["data"].attrs),
            "unit": r["data"].attrs["unit"]}


# ------------------------------------------------------------------------------------- LFP

def load_lfp(f: h5py.File) -> tuple[np.ndarray, np.ndarray, float]:
    """Bipolar LFP timestamps and values as stored, and the stored conversion factor."""
    s = f["processing/ecephys/FilteredEphys/bipolar_lfp_series"]
    return s["timestamps"][:], s["data"][:, 0], float(s["data"].attrs["conversion"])


def beta_power(x: np.ndarray, fs: float = LFP_RATE, band=BETA_BAND, order: int = BETA_ORDER,
               smooth_s: float = BETA_SMOOTH_S) -> np.ndarray:
    """Squared Hilbert envelope of the beta band, smoothed with a Hanning window of smooth_s
    seconds (none when smooth_s is 0)."""
    b, a = signal.butter(order, band, btype="band", fs=fs)
    y = signal.filtfilt(b, a, x)
    env = np.abs(signal.hilbert(y)) ** 2
    if smooth_s == 0:
        return env
    w = np.hanning(int(round(smooth_s * fs)))
    return np.convolve(env, w / w.sum(), mode="same")


def window_mean(ts: np.ndarray, x: np.ndarray, events: np.ndarray, a: float, b: float) -> np.ndarray:
    i0 = np.searchsorted(ts, events + a)
    i1 = np.searchsorted(ts, events + b)
    c = np.r_[0.0, np.cumsum(x)]
    return (c[i1] - c[i0]) / (i1 - i0)


def aligned(ts: np.ndarray, x: np.ndarray, events: np.ndarray, pre_s: float, post_s: float,
            fs: float = LFP_RATE) -> tuple[np.ndarray, np.ndarray]:
    i = np.searchsorted(ts, events)
    n0, n1 = int(pre_s * fs), int(post_s * fs)
    return np.arange(-n0, n1 + 1) / fs, np.stack([x[k - n0:k + n1 + 1] for k in i])


def burst_onsets(power: np.ndarray, threshold: float, min_len: int) -> np.ndarray:
    """Sample indices where power rises above threshold and stays there at least min_len samples."""
    above = np.r_[False, power > threshold, False]
    d = np.diff(above.astype(int))
    on, off = np.where(d == 1)[0], np.where(d == -1)[0]
    return on[(off - on) >= min_len]


def raw_bipolar_1khz(f: h5py.File, t0: float, t1: float) -> tuple[np.ndarray, np.ndarray]:
    """Raw c3bs minus c3a from t0 to t1 (s, by the series' own starting time and rate),
    averaged in 1 ms bins."""
    e = f["acquisition/electrical_series"]
    rate = float(e["starting_time"].attrs["rate"])
    st = float(e["starting_time"][()])
    i0, i1 = int((t0 - st) * rate), min(int((t1 - st) * rate), e["data"].shape[0])
    conv = float(e["data"].attrs["conversion"])
    k = int(rate / LFP_RATE)
    step = k * 200_000                     # read 200 s at a time
    out = []
    for i in range(i0, i1, step):
        d = e["data"][i:min(i + step, i1), :]
        bip = (d[:, 0].astype(np.float32) - d[:, 1].astype(np.float32)) * conv
        n = len(bip) // k
        out.append(bip[:n * k].reshape(n, k).mean(1))
    x = np.concatenate(out)
    return st + (i0 + np.arange(len(x)) * k) / rate, x


def best_lag(reference: np.ndarray, search: np.ndarray) -> tuple[int, float]:
    """Offset (samples) into `search` where it best correlates with `reference`, and that r."""
    ref = (reference - reference.mean()) / reference.std()
    s = search - search.mean()
    c = signal.correlate(s, ref, mode="valid")
    n = len(ref)
    cs = np.r_[0.0, np.cumsum(s.astype(float) ** 2)]
    r = c / (np.sqrt(cs[n:] - cs[:-n]) * np.sqrt(n))
    k = int(np.argmax(r))
    return k, float(r[k])


# ---------------------------------------------------------------------------------- spikes

def ragged(f: h5py.File, group: str, column: str) -> list[np.ndarray]:
    g = f[group]
    ends = g[f"{column}_index"][:]
    data = g[column][:]
    return np.split(data, ends[:-1])


def thresholded_waveforms(f: h5py.File) -> tuple[np.ndarray, np.ndarray]:
    """All stored waveforms (spikes x 48) and the row index where each unit's spikes end."""
    g = f["processing/ecephys/thresholded_units"]
    w = g["waveforms"][:, 0].reshape(-1, 48)
    return w, g["waveforms_index_index"][:]


def raw_slice(f: h5py.File, first_sample: int, n: int) -> tuple[np.ndarray, np.ndarray]:
    """Monkey P raw signal (µV) and its stored timestamps for n samples from first_sample."""
    e = f["acquisition/electrical_series"]
    x = e["data"][first_sample:first_sample + n, 0].astype(float) * float(e["data"].attrs["conversion"]) * 1e6
    return e["timestamps"][first_sample:first_sample + n], x


def timestamp_summary(f: h5py.File, chunk: int = 20_000_000) -> dict:
    """Median interval and gaps (intervals over 1.5 samples) of Monkey P's raw timestamps, read in chunks."""
    ts = f["acquisition/electrical_series/timestamps"]
    n = ts.shape[0]
    gaps, medians, last = [], [], None
    for i in range(0, n, chunk):
        t = ts[i:i + chunk]
        if last is not None:
            t = np.r_[last, t]
        d = np.diff(t)
        medians.append(np.median(d))
        g = np.where(d > 1.5 * medians[-1])[0]
        gaps += [(float(t[k]), float(d[k])) for k in g]
        last = t[-1]
    return {"n": n, "first": float(ts[0]), "last": float(last), "median_dt": float(np.median(medians)), "gaps": gaps}


def spike_band(x: np.ndarray, fs: float) -> np.ndarray:
    sos = signal.butter(3, SPIKE_BAND, btype="band", fs=fs, output="sos")
    return signal.sosfiltfilt(sos, x)


def spike_triggered_mean(t_raw: np.ndarray, x: np.ndarray, spikes: np.ndarray, offset: float,
                         pre: int = 8, post: int = 40) -> tuple[np.ndarray, int]:
    s = spikes - offset
    s = s[(s > t_raw[0] + 0.01) & (s < t_raw[-1] - 0.01)]
    if len(s) == 0:
        return np.full(pre + post, np.nan), 0
    i = np.searchsorted(t_raw, s)
    return np.stack([x[k - pre:k + post] for k in i]).mean(0), len(s)


# ---------------------------------------------------------------------------------- Zenodo

def zenodo_events(name: str) -> tuple[np.ndarray, np.ndarray, list[str]]:
    """A Neuralynx events file of the Zenodo deposit: times (s), TTL values and event strings."""
    m = zenodo_mat(name)
    strings = [x[0][0] if x[0].size else "" for x in m["dg_Nlx2Mat_EventStrings"]]
    return m["dg_Nlx2Mat_Timestamps"].ravel() / 1e6, m["dg_Nlx2Mat_TTL"].ravel().astype(int), strings


def zenodo_mat(name: str) -> dict:
    """A .mat file of the paper's Zenodo deposit, read in memory."""
    url = ZENODO_DATA.format(urllib.parse.quote(name))
    with urllib.request.urlopen(url, timeout=120) as r:
        return sio.loadmat(io.BytesIO(r.read()))
