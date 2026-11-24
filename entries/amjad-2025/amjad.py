"""Loading and measures for Amjad et al. (2025) on DANDI:002013.

Every parameter says where it comes from: the claims file (claims/amjad-2025.yaml, which cites the
paper), a passage of the paper (author, step 1.6), an assumption, or a standard choice that cannot
change a result.
"""

import io
import re

import h5py
import numpy as np
import pandas as pd
import remfile
import requests
import scipy.io
from scipy import signal

DANDISET_ID = "002013"
DANDISET_VERSION = "0.261120.1306"  # the version this attempt was asked to test
API = "https://api.dandiarchive.org/api"

PATHS = {
    "shape": "sub-Monkey-T/sub-Monkey-T_ses-09132024_ecephys.nwb",      # 09/13/2024, FSCV c8dg
    "direction": "sub-Monkey-T/sub-Monkey-T_ses-09262024_ecephys.nwb",  # 09/26/2024, LFP c3bs-c3a
    "monkey_p": "sub-Monkey-P/sub-Monkey-P_ses-08132018_ecephys.nwb",   # 08/13/2018, spikes
}

# Zenodo deposit of the paper's processed data (Data Availability Statement,
# doi:10.5281/zenodo.14826579), used by zenodo-link only.
ZENODO_RECORD = "14826579"
ZENODO_LISTS = {
    "large": "09262024_trialids_value object start_big rew and success_tr1-1501.mat",
    "small": "09262024_trialids_value object start_small rew and success_tr1-1501.mat",
    "left": "09262024_trialids_value object start_left and success_tr1-1501.mat",
    "right": "09262024_trialids_value object start_right and success_tr1-1501.mat",
}
ZENODO_EXAMPLE = "09262024_c3bs-c3a_data_trial35bigrewardexample.mat"

# Event codes, from the claims file's method choices (the events table names each code in its
# description).
TRIAL_START = 128       # "intended trial start"; a trial runs from one to the next
VALUE_CUE = 23          # "value object start"; the first one in a trial is its value cue
FEEDBACK = 21
BIG_REWARD, SMALL_REWARD = 101, 100
LEFT, RIGHT = 117, 118
FORCED = 119
IMAGES = (81, 88)

FSCV_RATE = 10.0        # trial-aligned FSCV table, 10 Hz; trial start at sample 300 (claims file)
FSCV_T0_SAMPLE = 300
LFP_RATE = 1000.0       # bipolar LFP, 1 kHz (paper, Methods, FSCV and EPhys Recordings, para 4)


def assets():
    """Path -> (asset id, size) for every asset of the pinned version."""
    r = requests.get(f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/",
                     params={"page_size": 100}).json()
    return {a["path"]: (a["asset_id"], a["size"]) for a in r["results"]}


def open_file(path):
    """Stream one NWB file of the pinned version as an h5py File (no download to disk)."""
    asset_id = assets()[path][0]
    url = requests.get(f"{API}/assets/{asset_id}/download/", allow_redirects=False).headers["Location"]
    return h5py.File(remfile.File(url), "r")


def _str(x):
    return x.decode() if isinstance(x, bytes) else str(x)


def events(f):
    """Events table as ({code: sorted times}, {code: label}). The code of each row is read from its
    description ("The event times for code N")."""
    g = f["processing/events/events_table"]
    desc = [_str(d) for d in g["event_description"][:]]
    labels = [_str(d) for d in g["label"][:]]
    times = g["event_times"][:]
    idx = g["event_times_index"][:]
    out, names, lo = {}, {}, 0
    for d, lab, hi in zip(desc, labels, idx):
        code = int(re.search(r"code (\d+)", d).group(1))
        out[code] = times[lo:hi]
        names[code] = lab
        lo = hi
    return out, names


def decode_trials(ev, n_trials):
    """One row per trial: its start (code 128), its value cue (first code 23 in it) and, for each
    code, whether the trial holds it (`has_<code>`). A trial runs from one code 128 to the next
    (claims file, method choices)."""
    starts = np.sort(ev[TRIAL_START])
    assert len(starts) == n_trials
    bounds = np.r_[starts, np.inf]
    which = {c: np.searchsorted(bounds, np.sort(t), side="right") - 1 for c, t in ev.items()}
    cols = {"trial": np.arange(n_trials), "start": starts}
    for c, w in which.items():
        has = np.zeros(n_trials, bool)
        has[w[(w >= 0) & (w < n_trials)]] = True
        cols[f"has_{c}"] = has
    vc = np.full(n_trials, np.nan)
    t23, w23 = np.sort(ev[VALUE_CUE]), which[VALUE_CUE]
    for t, w in zip(t23[::-1], w23[::-1]):   # reversed, so the first code 23 of a trial is kept
        if 0 <= w < n_trials:
            vc[w] = t
    cols["value_cue"] = vc
    return pd.DataFrame(cols)


# ---------------------------------------------------------------------------- FSCV (09/13/2024)

def fscv_scans(f):
    """Raw FSCV current and applied voltage reshaped to one row per scan. Scans are the runs of
    samples between gaps in the timestamps (214 samples at 25 kHz each). Returns
    (scan start times, current [scans x samples] in nA, voltage of the first scan in V,
    sampling interval in s). The current is read in blocks of whole scans to keep memory low."""
    ts_ds = f["acquisition/fscv_response_series/timestamps"]
    ts = ts_ds[:]
    gaps = np.where(np.diff(ts) > 1e-3)[0]
    starts = np.r_[0, gaps + 1]
    lengths = np.diff(np.r_[starts, len(ts)])
    n = int(np.median(lengths))
    assert (lengths == n).all(), "scans of unequal length"
    dt = float(np.median(np.diff(ts[:n])))
    t_scan = ts[starts]
    del ts
    data = f["acquisition/fscv_response_series/data"]
    conv = data.attrs["conversion"] / 1e-9           # to nA
    cur = np.empty((len(starts), n), np.float32)
    block = n * 25000
    for a in range(0, data.shape[0], block):
        cur[a // n:(a + block) // n] = data[a:a + block].reshape(-1, n) * conv
    volt = f["stimulus/presentation/fscv_excitation_series/data"][:n]
    return t_scan, cur, volt, dt


def waveform_parameters(volt, t_scan, dt):
    """Lowest and highest applied potential, sweep rate and scan frequency (fscv-waveform
    criterion: sweep rate = median absolute step of the rising ramp x sampling rate; scan frequency
    = 1 / median interval between scan starts)."""
    top = int(np.argmax(volt))
    rising = volt[:top + 1]
    return {
        "lowest_V": float(volt.min()),
        "highest_V": float(volt.max()),
        "sweep_V_per_s": float(np.median(np.abs(np.diff(rising))) / dt),
        "scan_Hz": float(1 / np.median(np.diff(t_scan))),
    }


def voltammograms(t_scan, cur, cue_times, post=(0.5, 2.0)):
    """Background-subtracted voltammogram per trial: mean of the scans starting `post` s after the
    cue minus the scan nearest the cue (fig3a-redox-peaks criterion)."""
    out = []
    for c in cue_times:
        ref = int(np.argmin(np.abs(t_scan - c)))
        sel = (t_scan >= c + post[0]) & (t_scan <= c + post[1])
        out.append(cur[sel].mean(0) - cur[ref])
    return np.array(out)


def fscv_table(f):
    g = f["processing/fscv/trial_aligned_fscv_table"]
    return {k: g[k][:] for k in ["da", "iox", "ph", "m", "trial_index", "start_time", "stop_time",
                                 "good", "rate"]}


def cue_sample(trials_rows):
    """Sample of the value cue in the trial-aligned series: trial start (code 128) at sample 300,
    10 Hz, nearest sample (claims file, method choices)."""
    i = np.rint(FSCV_T0_SAMPLE + (trials_rows.value_cue.values - trials_rows.start.values) * FSCV_RATE)
    return np.where(np.isfinite(i), i, -1).astype(int)   # -1: the trial has no value cue


def window_mean(x, i_cue, window, reref=True):
    """Mean of a 10 Hz trial-aligned series over `window` s after the cue, re-referenced to the
    sample at the cue (claims file: the Methods background-subtract at the value cue). The window
    takes the samples after the cue up to and including its end (0 to 3 s is samples +1 to +30); a
    standard choice. NaN samples are left out (claims file); a trial whose cue sample is NaN has
    no re-referenced value and is dropped."""
    a = int(round(window[0] * FSCV_RATE)) + (1 if window[0] == 0 else 0)
    b = int(round(window[1] * FSCV_RATE)) + 1
    out = np.full(len(x), np.nan)
    for r, i in enumerate(i_cue):
        if i < 0 or i >= x.shape[1]:
            continue
        y = x[r] - (x[r, i] if reref else 0.0)
        seg = y[i + a:i + b]
        if np.isfinite(seg).any():
            out[r] = np.nanmean(seg)
    return out


# ------------------------------------------------------------------------ LFP (09/26/2024)

def beta_power(x, fs=LFP_RATE, order="envelope_squared", smooth=True):
    """Beta power of the continuous bipolar LFP: 13 to 28 Hz 4th-order Butterworth run forwards and
    backwards, squared Hilbert envelope, smoothed with a 0.25 s Hanning window of unit sum
    (claims file, method choices; paper, Methods: "bandpass filtered around 13 to 28 Hz, squared,
    enveloped, and then smoothed with a Hanning window of 0.25 s"). Unit sum keeps the units V^2.

    order="squared_enveloped" is the paper's order read literally, a variant: the band-passed signal
    is squared and then enveloped as MATLAB's envelope() does by default (the magnitude of the
    analytic signal of the mean-removed input, plus the mean). smooth=False skips the Hanning
    window, a variant for the burst claim."""
    b, a = signal.butter(4, [13, 28], btype="bandpass", fs=fs)
    y = signal.filtfilt(b, a, x)
    if order == "envelope_squared":
        env = np.abs(signal.hilbert(y)) ** 2
    else:
        y2 = y ** 2
        env = y2.mean() + np.abs(signal.hilbert(y2 - y2.mean()))
    if not smooth:
        return env
    w = np.hanning(int(0.25 * fs))
    return np.convolve(env, w / w.sum(), mode="same")


def window_power(bp, t, cues, window, baseline=None):
    """Mean beta power over `window` s from each cue; divided by the mean over `baseline` when
    given (the variant of fig4b and fig4c)."""
    i0 = np.searchsorted(t, cues)
    a, b = int(window[0] * LFP_RATE), int(window[1] * LFP_RATE)
    v = np.array([bp[i + a:i + b].mean() for i in i0])
    if baseline is not None:
        c, d = int(baseline[0] * LFP_RATE), int(baseline[1] * LFP_RATE)
        v = v / np.array([bp[i + c:i + d].mean() for i in i0])
    return v


def burst_onsets(bp, threshold, min_len):
    """Onsets (sample indices) of runs of beta power above `threshold` lasting at least `min_len`
    samples (fig3b-beta-bursts criterion: 50 ms, one cycle at 20 Hz)."""
    above = np.r_[0, (bp > threshold).astype(np.int8), 0]
    d = np.diff(above)
    on, off = np.where(d == 1)[0], np.where(d == -1)[0]
    return on[(off - on) >= min_len]


# ------------------------------------------------------------------------ Zenodo (zenodo-link)

def zenodo_file(name):
    """Read one small file of the Zenodo deposit into memory."""
    url = f"https://zenodo.org/api/records/{ZENODO_RECORD}/files/{requests.utils.quote(name)}/content"
    r = requests.get(url, timeout=120)
    r.raise_for_status()
    return scipy.io.loadmat(io.BytesIO(r.content), squeeze_me=True)


# ------------------------------------------------------------------------ spikes (Monkey P)

def noise_level(x, fs):
    """Noise of the raw signal: median absolute deviation / 0.6745 of the 300 to 6000 Hz
    band-passed signal (fig5bc-unit-isolation criterion). The filter is a 4th-order Butterworth run
    forwards and backwards, a standard choice."""
    sos = signal.butter(4, [300, 6000], btype="bandpass", fs=fs, output="sos")
    y = signal.sosfiltfilt(sos, x)
    return float(np.median(np.abs(y - np.median(y))) / 0.6745), y
