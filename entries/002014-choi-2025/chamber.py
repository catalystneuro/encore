"""Loading and measures for dandiset 002014: one session of monkey T (09/27/2024) recorded through
the aseptic semi-sealed chamber of Choi et al. (2025), J Neurosci Methods, doi:10.1016/j.jneumeth.2025.110467.

The single NWB file holds raw Neuralynx ephys (sites c7b, c5c, c5d, 32 kHz), a bipolar LFP (c7b
referenced to c5c, 1 kHz), threshold-detected spikes with waveforms and a Plexon-sorted unit (c5d),
raw FSCV current and the applied voltage (c8ds), a trial-aligned FSCV table (dopamine, pH, motion and
oxidation current, 10 Hz, 60 s per trial), a trials table and an event table. It is streamed from the
archive at the pinned version; nothing is written to disk.

Where the parameters come from:

- Trial classes follow the paper's Zenodo trial lists (doi:10.5281/zenodo.14825992, "value object
  start_big/small rew and success"): a successful trial holds a reward event and no error event.
  They are built here from the dandiset's own events.
- V, the value cue display, is the event "value object start" (code 23), the alignment of Figures 8
  and 9; RW is the reward event (codes 101 and 100).
- The trial-aligned FSCV rows run from 30 s before to 30 s after the trial-start event (the trials
  table's `midpoint_time`), at 10 Hz (601 samples); this is the conversion's layout
  (schwerdt-lab-to-nwb, TrialAlignedFSCVInterface).
- The beta band (13 to 30 Hz), the filter order and the windows are common choices, as the paper
  gives none; they are set in the claims file.
- `CLOCK_SEGMENTS` and the 1 to 8 Hz band used to locate the raw ephys on the trial clock are
  choices made here for the data check.
"""

from __future__ import annotations

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy import signal

DANDISET_ID = "002014"
DANDISET_VERSION = "0.261012.0921"
ASSET_PATH = "sub-Monkey-T/sub-Monkey-T_ses-09272024_ecephys.nwb"

RAW_RATE = 32000.0
LFP_RATE = 1000.0
FSCV_RATE = 10.0
FSCV_HALF_WINDOW_S = 30.0
FSCV_SAMPLES_PER_SCAN = 214

V_LABEL = "value object start"
CLOCK_SEGMENTS = 8          # raw segments located in the stored LFP
CLOCK_SEGMENT_S = 30.0
CLOCK_BAND = (1.0, 6.0)
BETA_BAND = (13.0, 30.0)


def open_file() -> h5py.File:
    """Open the NWB file of the pinned version for streaming."""
    with DandiAPIClient() as client:
        asset = client.get_dandiset(DANDISET_ID, DANDISET_VERSION).get_asset_by_path(ASSET_PATH)
        url = asset.get_content_url(follow_redirects=1, strip_query=True)
    return h5py.File(remfile.File(url), "r")


def _text(x):
    return x.decode() if isinstance(x, bytes) else x


def _ragged(group, column):
    """Split a ragged column (data plus index) into a list of arrays."""
    data, index = group[column][()], group[f"{column}_index"][()]
    return np.split(data, index[:-1])


def load_events(f) -> dict[str, np.ndarray]:
    """Event times per label. The file repeats events that fall in several trials' 60 s windows;
    each label's times are made unique and sorted here."""
    table = f["processing/events/events_table"]
    labels = [_text(x) for x in table["label"][()]]
    return {label: np.unique(times) for label, times in zip(labels, _ragged(table, "event_times"))}


def raw_event_counts(f) -> pd.DataFrame:
    """Event counts as stored (with repeats) and after removing repeats."""
    table = f["processing/events/events_table"]
    rows = []
    for label, code, times in zip(table["label"][()], table["event_description"][()],
                                  _ragged(table, "event_times")):
        rows.append({"label": _text(label), "description": _text(code), "stored": len(times),
                     "unique": len(np.unique(times)), "sorted": bool(np.all(np.diff(times) >= 0))})
    return pd.DataFrame(rows)


def trial_table(f, events: dict[str, np.ndarray]) -> pd.DataFrame:
    """One row per trial: its trial-start time, V, RW, class and outcome. A trial's events are
    those from its trial-start event to the next trial's."""
    trials = f["intervals/trials"]
    start, stop = trials["start_time"][()], trials["stop_time"][()]
    mid = trials["midpoint_time"][()]
    edges = np.r_[mid, np.inf]
    per_trial = [dict() for _ in mid]
    for label, times in events.items():
        k = np.searchsorted(edges, times, side="right") - 1
        for kk, t in zip(k, times):
            if kk >= 0:
                per_trial[kk].setdefault(label, []).append(t)
    errors = [label for label in events if label.startswith("error")]
    rows = []
    for i, ev in enumerate(per_trial):
        big, small = "big reward" in ev, "small reward" in ev
        error = next((e for e in errors if e in ev), None)
        rw = ev.get("big reward", ev.get("small reward", [np.nan]))[0]
        rows.append({
            "trial": i + 1, "start_time": start[i], "stop_time": stop[i], "trial_start": mid[i],
            "trial_end": edges[i + 1] if np.isfinite(edges[i + 1]) else stop[i],
            "V": ev.get(V_LABEL, [np.nan])[0], "RW": rw,
            "n_V": len(ev.get(V_LABEL, [])),
            "reward": "large" if big else ("small" if small else None),
            "error": error,
            "success": (big or small) and error is None,
            "side": "left" if "left condition" in ev else ("right" if "right condition" in ev else None),
        })
    return pd.DataFrame(rows)


def load_fscv_table(f) -> dict[str, np.ndarray]:
    """The trial-aligned FSCV columns and the time of each sample relative to the trial start."""
    g = f["processing/fscv/trial_aligned_fscv_table"]
    out = {k: g[k][()] for k in ("da", "ph", "m", "iox", "good", "rate", "start_time", "stop_time")}
    n = out["da"].shape[1]
    out["t_rel_start"] = np.arange(n) / FSCV_RATE - FSCV_HALF_WINDOW_S
    return out


def reference_at(trace, t, t0, half=0.2):
    """The trace minus its value at t0: linear interpolation, or, when the interpolation meets a NaN,
    linear interpolation between the nearest non-NaN samples before and after t0, if both lie within
    `half` s. NaN otherwise."""
    v = np.interp(t0, t, trace)
    if np.isnan(v):
        ok = ~np.isnan(trace)
        before, after = ok & (t <= t0), ok & (t >= t0)
        if before.any() and after.any():
            tb, ta = t[before].max(), t[after].min()
            if t0 - tb <= half and ta - t0 <= half:
                v = np.interp(t0, t[ok], trace[ok])
    return trace - v


def dopamine_aligned(fscv, trials: pd.DataFrame, t_axis=np.arange(-10, 10.01, 0.1)):
    """Dopamine of each trial referenced to its value at V and resampled at `t_axis` s from V
    (linear interpolation between the 10 Hz samples; NaN stays NaN)."""
    out = np.full((len(trials), len(t_axis)), np.nan)
    for i, row in enumerate(trials.itertuples()):
        if np.isnan(row.V):
            continue
        t = row.trial_start + fscv["t_rel_start"] - row.V
        out[i] = np.interp(t_axis, t, reference_at(fscv["da"][row.trial - 1], t, 0.0))
    return t_axis, out


def load_lfp(f):
    """Timestamps (trial clock) and values of the stored bipolar LFP. The values are taken as
    stored; the data check shows they are already in volts."""
    g = f["processing/ecephys/FilteredEphys/bipolar_lfp_series"]
    return g["timestamps"][()], g["data"][:, 0]


def raw_segment(f, start_s, duration_s, channels=slice(None)):
    """Raw ephys in volts, from `start_s` s on the file's own clock (starting_time plus samples)."""
    es = f["acquisition/electrical_series"]
    rate = es["starting_time"].attrs["rate"]
    t0 = es["starting_time"][()]
    i0 = int(round((start_s - t0) * rate))
    x = es["data"][i0:i0 + int(duration_s * rate), channels].astype(np.float64)
    return x * es["data"].attrs["conversion"]


def _bipolar_1khz(f, start_s, duration_s):
    raw = raw_segment(f, start_s, duration_s, slice(0, 2))
    return signal.decimate(signal.decimate(raw[:, 0] - raw[:, 1], 8), 4)


def _normalized_xcorr(signal_long, template):
    """Correlation of a template with every stretch of a longer signal, normalized by both
    energies. Stretches with no energy (NaN gaps set to 0) get 0."""
    m = len(template)
    c = signal.correlate(signal_long, template, mode="valid", method="fft")
    energy = np.cumsum(np.r_[0.0, signal_long ** 2])
    e = energy[m:] - energy[:-m]
    return np.where(e > 1e-3 * m * np.mean(signal_long ** 2),
                    c / np.sqrt(np.maximum(e, 1e-300) * np.sum(template ** 2)), 0.0)


def locate_raw_in_lfp(f, lfp_t, lfp_v, n=CLOCK_SEGMENTS, seg_s=CLOCK_SEGMENT_S, search_s=60.0):
    """Place the raw ephys on the trial clock. First, a raw segment of c7b minus c5c near the start
    of the recording is searched for in the whole stored LFP, which gives a candidate offset. Then,
    at `n` points across the session, a segment of the stored LFP is searched for in the raw
    signal within `search_s` s of where the candidate offset puts it. Raw segments far into the
    recording clip at the input range and carry the FSCV artefact, which is why the stored LFP is
    the template there. Returns the candidate and a table with the offset and correlation at each
    point, and the best correlation at least 1 s away from the peak."""
    sos = signal.butter(4, CLOCK_BAND, "bandpass", fs=LFP_RATE, output="sos")
    scale = np.nanstd(lfp_v)
    stored = signal.sosfiltfilt(sos, np.nan_to_num(lfp_v / scale))
    first = 60.0
    bip = signal.sosfiltfilt(sos, _bipolar_1khz(f, first, seg_s) / scale)
    r = _normalized_xcorr(stored, bip)
    k = int(np.argmax(r))
    candidate = {"raw_time": first, "offset": lfp_t[k] - first, "r": r[k]}
    rows = []
    for t in np.linspace(lfp_t[0] + 300, lfp_t[-1] - 300, n):
        i0 = int(np.searchsorted(lfp_t, t))
        tmpl = lfp_v[i0:i0 + int(seg_s * LFP_RATE)]
        while np.isnan(tmpl).any():  # step on to a stretch without NaN
            i0 += int(seg_s * LFP_RATE)
            tmpl = lfp_v[i0:i0 + int(seg_s * LFP_RATE)]
        tmpl = signal.sosfiltfilt(sos, tmpl / scale)
        raw_start = lfp_t[i0] - candidate["offset"] - search_s
        win = signal.sosfiltfilt(sos, _bipolar_1khz(f, raw_start, 2 * search_s + seg_s) / scale)
        r = _normalized_xcorr(win, tmpl)
        k = int(np.argmax(r))
        away = np.abs(np.arange(len(r)) - k) > LFP_RATE
        rows.append({"trial_clock_time": lfp_t[i0], "raw_time": raw_start + k / LFP_RATE,
                     "offset": lfp_t[i0] - (raw_start + k / LFP_RATE), "r": r[k],
                     "best_r_1s_away": r[away].max()})
    return candidate, pd.DataFrame(rows)


def spike_units(f, path):
    """Spike times and names of a Units table (as stored, on the file's clock)."""
    g = f[path]
    names = [_text(x) for x in g["unit_name"][()]]
    return dict(zip(names, _ragged(g, "spike_times")))


def thresholded_waveforms(f, unit_index, max_spikes=None):
    """Waveforms (spikes x 48 samples) of one unit of the thresholded table, as stored. The file
    states volts; the data check shows the values are in microvolts."""
    g = f["processing/ecephys/thresholded_units"]
    st_index = g["spike_times_index"][()]
    lo = 0 if unit_index == 0 else st_index[unit_index - 1]
    hi = st_index[unit_index]
    if max_spikes is not None:
        hi = min(hi, lo + max_spikes)
    wf_index = g["waveforms_index"][()]
    a = 0 if lo == 0 else wf_index[lo - 1]
    b = wf_index[hi - 1]
    return g["waveforms"][a:b, 0].reshape(hi - lo, -1)


def psth(spike_times, align, window=(-1.0, 3.0), bin_s=0.1):
    """Trial-by-bin spike counts around each alignment time, and the bin centres."""
    edges = np.arange(window[0], window[1] + bin_s / 2, bin_s)
    counts = np.zeros((len(align), len(edges) - 1))
    for i, a in enumerate(align):
        lo, hi = np.searchsorted(spike_times, [a + window[0], a + window[1]])
        counts[i] = np.histogram(spike_times[lo:hi] - a, edges)[0]
    return (edges[:-1] + edges[1:]) / 2, counts


def modulation(counts, bin_s=0.1):
    """Variance across bins of the trial-averaged firing rate (spikes/s, squared)."""
    return np.var(counts.mean(0) / bin_s)


def band_power_around(lfp_t, lfp_v, times, band=BETA_BAND, pad=3.0, order=4):
    """Squared Hilbert envelope of the band-passed LFP from `pad` s before to `pad` s after each
    time, filtered per trial. Rows with any NaN in the span are NaN. Returns the time axis
    (s from the event) and a trials x samples array."""
    sos = signal.butter(order, band, "bandpass", fs=LFP_RATE, output="sos")
    n = int(round(2 * pad * LFP_RATE)) + 1
    t_axis = np.arange(n) / LFP_RATE - pad
    out = np.full((len(times), n), np.nan)
    for i, t0 in enumerate(times):
        if np.isnan(t0):
            continue
        k = np.searchsorted(lfp_t, t0 - pad)
        seg = lfp_v[k:k + n]
        if len(seg) < n or np.isnan(seg).any() or abs(lfp_t[k] - (t0 - pad)) > 1.5 / LFP_RATE:
            continue
        out[i] = np.abs(signal.hilbert(signal.sosfiltfilt(sos, seg))) ** 2
    return t_axis, out


def window_mean(t_axis, values, lo, hi):
    """Mean over t_axis in [lo, hi), per row, ignoring NaN."""
    m = (t_axis >= lo) & (t_axis < hi)
    with np.errstate(all="ignore"):
        return np.nanmean(values[:, m], axis=1)


def spike_triggered_raw(f, spike_times, start_s, duration_s, channel, half_ms=20.0, band=(300.0, 6000.0)):
    """Mean of the band-passed raw channel around each spike time within a raw segment, with the
    lag axis in ms. Spike times and the segment are on the raw ephys clock."""
    x = raw_segment(f, start_s, duration_s, slice(channel, channel + 1))[:, 0]
    x = signal.sosfiltfilt(signal.butter(3, band, "bandpass", fs=RAW_RATE, output="sos"), x)
    w = int(half_ms / 1000 * RAW_RATE)
    inside = spike_times[(spike_times > start_s + 0.05) & (spike_times < start_s + duration_s - 0.05)]
    idx = np.round((inside - start_s) * RAW_RATE).astype(int)
    snippets = np.array([x[i - w:i + w] for i in idx])
    return (np.arange(-w, w) / RAW_RATE * 1000), snippets


def block_permutation_p(values, labels, blocks, statistic, n=2000, rng=None):
    """Two-sided permutation p-value of `statistic(values[labels], values[~labels])`, with the labels
    shuffled only within each block (consecutive trials), so that slow drift across the session is
    kept in the null. NaN values are dropped first. Returns the observed statistic and p."""
    ok = ~np.isnan(values)
    values, labels, blocks = values[ok], labels[ok], blocks[ok]
    obs = statistic(values[labels], values[~labels])
    groups = [np.where(blocks == b)[0] for b in np.unique(blocks)]
    null = np.empty(n)
    for j in range(n):
        perm = labels.copy()
        for g in groups:
            perm[g] = rng.permutation(labels[g])
        null[j] = statistic(values[perm], values[~perm])
    return obs, (np.sum(np.abs(null) >= abs(obs)) + 1) / (n + 1)
