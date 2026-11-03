"""Loading and measures for dandiset 001678 (Bell Vila et al., "Parametrizing alternating current
stimulation for neuromodulation", Imaging Neuroscience, doi:10.1162/imag.a.1066).

The files are streamed from the DANDI archive at a pinned version (remfile and h5py); nothing is
written to disk.

What the files hold (checked in the notebook):
- 9 files of the 1-minute paradigm (subjects sub-2021-*), each with 15 to 23 one-channel series
  named "S1r 1", one per trial. The channel is the stimulation command (the TDT stream `uS1r` of
  the paper's MUAartrem.m): zero outside stimulation and a sinusoid during it, with a peak equal
  to the current amplitude in uA. No recording channel is stored.
- 13 files of the 20-minute paradigm (subjects sub-2023-*), each with 3 to 5 series of 16 channels
  ("aw_ 1" to "aw_ 16") at 12207.03 Hz: the LFP stream (0.3 to 300 Hz, Methods 2.3). The first
  series holds the baseline, the 20 minutes of stimulation and the time after it.

Where each parameter of the electric field estimate comes from:
- band-pass at the stimulation frequency, peak voltage per stimulation cycle averaged over the
  stimulation period, differences between neighbouring electrodes divided by their spacing along
  both axes, vector addition, Grubbs' test at alpha 0.05: Methods 2.8, as the claim's criterion
  gives them.
- 0.5 mm spacing: Methods 2.3 ("spaced 0.5 mm apart").
- decimation to 1.2 kHz before filtering: Methods 2.5 ("LFP signals were decimated to 1.2 kHz").
- zero-phase Butterworth band of +/- 1 Hz (order 2, second-order sections): the criterion's
  standard choice for a filter the paper does not name.
- the 4 x 4 order of channels "aw_ 1" to "aw_ 16": an assumption (row by row, four channels per
  row); the files and the paper give no map. The notebook tests it against other orders.
- stimulation onset and offset: found from the 40 Hz artifact, 1-s resolution (the files have no
  epochs). One second is dropped at each end, a standard choice that cannot change a field that is
  averaged over about 1200 s.
- values taken as volts as stored: the files' conversion factor (1e-6) is wrong, as the notebook
  shows; the field is then in mV/mm when voltages are in mV and the spacing in mm.
"""

from __future__ import annotations

import hashlib

import h5py
import numpy as np
import remfile
import requests
from scipy import signal, stats

DANDISET_ID = "001678"
DANDISET_VERSION = "0.260227.1824"
API = "https://api.dandiarchive.org/api"

SPACING_MM = 0.5  # Methods 2.3
LFP_DECIMATE = 10  # 12207 Hz to 1220.7 Hz, Methods 2.5 ("decimated to 1.2 kHz")
STIM_HZ_20MIN = 40.0  # Methods 2.4
BAND_HALF_WIDTH_HZ = 1.0  # criterion's standard choice
BUTTER_ORDER = 2  # standard choice
EDGE_S = 1.0  # standard choice, seconds dropped at each end of the stimulation period
GRUBBS_ALPHA = 0.05  # Methods 2.8


def assets() -> list[dict]:
    """Every asset of the pinned version, sorted by path."""
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/?page_size=200"
    out = []
    while url:
        page = requests.get(url, timeout=60).json()
        out += page["results"]
        url = page.get("next")
    return sorted(out, key=lambda a: a["path"])


def version_info() -> dict:
    return requests.get(f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/info/", timeout=60).json()


def open_asset(asset_id: str) -> h5py.File:
    url = requests.get(f"{API}/assets/{asset_id}/download/", allow_redirects=False, timeout=60).headers["Location"]
    return h5py.File(remfile.File(url), "r")


def paradigm(path: str) -> str:
    return "1-min" if path.startswith("sub-2021") else "20-min"


def file_summary(asset: dict) -> dict:
    """Metadata and array shapes of one file (no data read)."""
    f = open_asset(asset["asset_id"])
    subj = {k: f["general/subject"][k][()].decode() for k in f["general/subject"]}
    el = f["general/extracellular_ephys/electrodes"]
    series = []
    for name in sorted(f["acquisition"]):
        s = f["acquisition"][name]
        series.append({
            "series": name, "shape": s["data"].shape, "rate": float(s["starting_time"].attrs["rate"]),
            "start_s": float(s["starting_time"][()]), "conversion": float(s["data"].attrs["conversion"]),
            "unit": s["data"].attrs["unit"], "chunks": s["data"].chunks,
        })
    groups = {g: list(f[g].keys()) for g in ("processing", "analysis", "stimulus/presentation", "stimulus/templates")
              if g in f}
    return {
        "path": asset["path"], "size_GB": asset["size"] / 1e9, "paradigm": paradigm(asset["path"]),
        "subject_id": subj.get("subject_id"), "sex": subj.get("sex"), "age": subj.get("age"),
        "species": subj.get("species"), "session_start": f["session_start_time"][()].decode(),
        "session_description": f["session_description"][()].decode(),
        "channel_names": [c.decode() for c in el["channel_name"][:]],
        "locations": sorted({c.decode() for c in el["location"][:]}),
        "electrode_columns": list(el.attrs["colnames"]),
        "has_units": "units" in f, "has_intervals": "intervals" in f, "groups": groups,
        "series": series, "top_level": sorted(f.keys()),
    }


def stim_trials(asset: dict) -> list[dict]:
    """For a 1-min file: frequency, peak and timing of the waveform in each one-channel series."""
    f = open_asset(asset["asset_id"])
    rows = []
    for name in sorted(f["acquisition"]):
        s = f["acquisition"][name]
        fs = float(s["starting_time"].attrs["rate"])
        x = s["data"][:, 0].astype(np.float64)
        nz = np.flatnonzero(x != 0)
        seg = x[nz[0]:nz[-1] + 1]
        on, off = nz[0] / fs, nz[-1] / fs
        crossings = np.sum((seg[:-1] < 0) & (seg[1:] >= 0))
        spec = np.abs(np.fft.rfft(seg))
        fr = np.fft.rfftfreq(len(seg), 1 / fs)
        rows.append({
            "subject": asset["path"].split("/")[0], "series": name, "start_s": float(s["starting_time"][()]),
            "length_s": len(x) / fs, "onset_s": on, "offset_s": off, "duration_s": off - on,
            "freq_zero_cross_hz": crossings / (off - on), "freq_fft_hz": fr[np.argmax(spec[1:]) + 1],
            "peak": np.abs(seg).max(), "rms": seg.std(), "nonzero_outside": int(np.sum(x[:nz[0]] != 0) + np.sum(x[nz[-1] + 1:] != 0)),
        })
    return rows


def band_power_profile(asset: dict, seconds: float = 30.0, start_min: float = 5.0) -> dict:
    """For a 20-min file: Welch spectrum of all 16 channels over a stretch of baseline, by band, and
    how spike-like the 500 to 3000 Hz band is (threshold crossings at 6 MAD, kurtosis)."""
    f = open_asset(asset["asset_id"])
    d = f["acquisition/ElectricalSeries0/data"]
    fs = float(f["acquisition/ElectricalSeries0/starting_time"].attrs["rate"])
    y = d[int(start_min * 60 * fs):int((start_min * 60 + seconds) * fs), :].astype(np.float64)
    fr, p = signal.welch(y, fs, nperseg=4096, axis=0)
    edges = [(0.3, 4), (4, 30), (30, 100), (100, 200), (200, 300), (300, 500), (500, 1000), (1000, 3000), (3000, 6000)]
    bands = {f"{lo}-{hi} Hz": float(p[(fr >= lo) & (fr < hi)].mean()) for lo, hi in edges}
    sos = signal.butter(3, [500, 3000], btype="band", fs=fs, output="sos")
    h = signal.sosfiltfilt(sos, y, axis=0)
    mad = np.median(np.abs(h), axis=0) / 0.6745
    crossings = [int(np.sum((np.abs(h[1:, c]) > 6 * mad[c]) & (np.abs(h[:-1, c]) <= 6 * mad[c]))) for c in range(16)]
    pm = p.mean(axis=1)
    near = (fr > 50) & (fr < 70)
    line60 = float(pm[np.argmin(np.abs(fr - 60))] / np.median(pm[near]))
    events = [signal.find_peaks(-h[:, c], height=6 * mad[c], distance=int(0.001 * fs))[0] for c in range(16)]
    busiest = int(np.argmax([len(e) for e in events]))
    ev = events[busiest]
    others = np.sort(np.concatenate([events[k] for k in range(16) if k != busiest]))
    tol = int(0.0005 * fs)
    if len(ev) and len(others):
        j = np.clip(np.searchsorted(others, ev), 1, len(others) - 1)
        nearest = np.minimum(np.abs(others[j] - ev), np.abs(others[j - 1] - ev))
        coincident = float(np.mean(nearest <= tol))
    else:
        coincident = np.nan
    pre, post = int(0.001 * fs), int(0.0015 * fs)
    waves = np.array([y[t - pre:t + post, busiest] - y[t - pre:t + post, busiest].mean() for t in ev if pre <= t < len(y) - post])
    if len(waves):
        mw = waves.mean(axis=0)
        trough = float(mw.min())
        width = float(np.sum(mw < trough / 2) / fs * 1e3)
    else:
        trough, width = np.nan, np.nan
    return {
        "path": asset["path"], "fs": fs, "bands_psd": bands, "line60_ratio": line60,
        "events_per_s_max": len(ev) / seconds, "busiest_channel": busiest + 1, "coincident_share": coincident,
        "trough_uV": trough * 1e6, "trough_width_ms": width,
        "raw_median_abs": float(np.median(np.abs(y))), "raw_p99_abs": float(np.percentile(np.abs(y), 99)),
        "mua_band_std": float(np.median(h.std(axis=0))),
        "mua_crossings_per_s_median": float(np.median(crossings) / seconds),
        "mua_kurtosis_median": float(np.median(stats.kurtosis(h, axis=0, fisher=False))),
    }


def series_fingerprints(asset: dict) -> list[dict]:
    """SHA-1 of the first second of every series of a file, to find recordings deposited twice."""
    f = open_asset(asset["asset_id"])
    out = []
    for name in sorted(f["acquisition"]):
        s = f["acquisition"][name]
        fs = float(s["starting_time"].attrs["rate"])
        z = s["data"][: int(fs), :]
        out.append({"subject": asset["path"].split("/")[0], "series": name,
                    "sha1_first_second": hashlib.sha1(z.tobytes()).hexdigest()[:12],
                    "all_zero": bool(np.all(z == 0))})
    return out


def _line_ratio(z: np.ndarray, fs: float, f0: float) -> float:
    """Power at f0 against the median power from f0-10 to f0+10 Hz, in a 1-s spectrum."""
    fr = np.fft.rfftfreq(len(z), 1 / fs)
    p = np.abs(np.fft.rfft(z - z.mean())) ** 2
    near = (fr > f0 - 10) & (fr < f0 + 10)
    return float(p[np.argmin(np.abs(fr - f0))] / np.median(p[near]))


def find_stimulation(d: h5py.Dataset, fs: float, f0: float = STIM_HZ_20MIN, threshold: float = 1000.0) -> tuple[float, float]:
    """Onset and offset (s from the start of the series) of the f0 artifact, to 1 s.

    A coarse scan reads one second of all channels every 64 s; the transitions are then located to the
    second within the 64 s on either side."""
    n = d.shape[0]
    step = int(64 * fs)
    one = int(fs)

    def ratio(z: np.ndarray) -> float:
        # the largest line ratio over the 16 channels: some channels carry little artifact
        return max(_line_ratio(z[:, c], fs, f0) for c in range(z.shape[1]))

    def on_at(sample: int) -> bool:
        z = d[sample:sample + one, :].astype(np.float64)
        return len(z) == one and ratio(z) > threshold

    coarse = [(i, on_at(i)) for i in range(0, n - one, step)]
    hits = [i for i, h in coarse if h]
    if not hits:
        return np.nan, np.nan
    first, last = hits[0], hits[-1]

    def refine(lo: int, hi: int, rising: bool) -> int:
        z = d[max(lo, 0):min(hi, n), :].astype(np.float64)
        secs = len(z) // one
        flags = [ratio(z[k * one:(k + 1) * one]) > threshold for k in range(secs)]
        if rising:
            k = next((k for k, v in enumerate(flags) if v), secs)
            return max(lo, 0) + k * one
        k = max((k for k, v in enumerate(flags) if v), default=-1)
        return max(lo, 0) + (k + 1) * one

    onset = refine(first - step, first + one, rising=True)
    offset = refine(last, last + step + one, rising=False)
    return onset / fs, offset / fs


def grubbs(values, alpha: float = GRUBBS_ALPHA) -> tuple[np.ndarray, np.ndarray]:
    """Two-sided Grubbs' test, iterated until no outlier remains. Returns kept values and the
    removed ones."""
    x = np.asarray(values, dtype=float)
    removed = []
    while len(x) > 2:
        m, s = x.mean(), x.std(ddof=1)
        if s == 0:
            break
        i = int(np.argmax(np.abs(x - m)))
        g = abs(x[i] - m) / s
        n = len(x)
        t = stats.t.ppf(1 - alpha / (2 * n), n - 2)
        crit = (n - 1) / np.sqrt(n) * np.sqrt(t ** 2 / (n - 2 + t ** 2))
        if g > crit:
            removed.append(x[i])
            x = np.delete(x, i)
        else:
            break
    return x, np.array(removed)


def cycle_peaks(asset: dict, f0: float = STIM_HZ_20MIN, block_s: float = 60.0) -> dict:
    """Average peak voltage per stimulation cycle for each of the 16 channels of a 20-min file.

    The stimulation period of the first series is read in blocks (1 s of padding on each side),
    decimated to 1.2 kHz, band-passed at f0 +/- 1 Hz, and the largest absolute value in each cycle
    (1/f0 s, counted from the onset) is taken. Returns per-channel means and spreads in volts as
    stored."""
    f = open_asset(asset["asset_id"])
    d = f["acquisition/ElectricalSeries0/data"]
    fs = float(f["acquisition/ElectricalSeries0/starting_time"].attrs["rate"])
    onset, offset = find_stimulation(d, fs, f0)
    a, b = int((onset + EDGE_S) * fs), int((offset - EDGE_S) * fs)
    fs2 = fs / LFP_DECIMATE
    pad = int(fs)
    parts = []
    for s0 in range(a, b, int(block_s * fs)):
        s1 = min(s0 + int(block_s * fs), b)
        lo, hi = max(s0 - pad, 0), min(s1 + pad, d.shape[0])
        y = signal.decimate(d[lo:hi, :].astype(np.float64), LFP_DECIMATE, axis=0, zero_phase=True)
        i0 = (s0 - lo) // LFP_DECIMATE
        parts.append(y[i0:i0 + (s1 - s0) // LFP_DECIMATE])
    y = np.concatenate(parts)
    sos = signal.butter(BUTTER_ORDER, [f0 - BAND_HALF_WIDTH_HZ, f0 + BAND_HALF_WIDTH_HZ], btype="band", fs=fs2, output="sos")
    yb = signal.sosfiltfilt(sos, y, axis=0)
    per = fs2 / f0
    ncyc = int(len(yb) / per)
    idx = (np.arange(ncyc + 1) * per).astype(int)
    pk = np.maximum.reduceat(np.abs(yb), idx[:-1], axis=0)[:ncyc]
    raw_rms = y.std(axis=0)
    return {
        "path": asset["path"], "subject": asset["path"].split("/")[0], "fs": fs, "n_samples": d.shape[0],
        "onset_s": onset, "offset_s": offset, "series_s": d.shape[0] / fs, "n_cycles": ncyc,
        "peak_mean": pk.mean(axis=0), "peak_cv": pk.std(axis=0) / pk.mean(axis=0),
        "peak_first_half": pk[: ncyc // 2].mean(axis=0), "peak_second_half": pk[ncyc // 2:].mean(axis=0),
        "decimated_rms": raw_rms,
    }


def grid(values: np.ndarray, order: np.ndarray | None = None) -> np.ndarray:
    """16 channel values to a 4 x 4 grid. `order[k]` is the channel index at grid position k (row
    by row); the default is channels 1 to 16 row by row (the assumption)."""
    v = np.asarray(values)
    if order is not None:
        v = v[np.asarray(order)]
    return v.reshape(4, 4)


def roughness(g: np.ndarray) -> float:
    """Sum of squared differences between neighbours of a grid, a measure of how smooth a map is."""
    return float(np.sum(np.diff(g, axis=0) ** 2) + np.sum(np.diff(g, axis=1) ** 2))


SERPENTINE = np.array([0, 1, 2, 3, 7, 6, 5, 4, 8, 9, 10, 11, 15, 14, 13, 12])


def fields(g_volts: np.ndarray) -> dict:
    """Electric field estimates (mV/mm) from a 4 x 4 grid of average peak voltages (V).

    Neighbour differences along each axis divided by the spacing: 12 along rows (x) and 12 along
    columns (y). Reading (i): each of the 9 cells of 2 x 2 electrodes gives one vector, x from the
    mean of its two row differences and y from the mean of its two column differences, combined
    by vector addition. Reading (ii): the largest absolute difference along each axis, combined by
    vector addition, one value per grid."""
    mv = g_volts * 1e3
    ex = np.diff(mv, axis=1) / SPACING_MM  # 4 x 3
    ey = np.diff(mv, axis=0) / SPACING_MM  # 3 x 4
    cx = (ex[:-1, :] + ex[1:, :]) / 2  # 3 x 3
    cy = (ey[:, :-1] + ey[:, 1:]) / 2  # 3 x 3
    cells = np.hypot(cx, cy).ravel()
    maximal = float(np.hypot(np.abs(ex).max(), np.abs(ey).max()))
    return {"ex": ex, "ey": ey, "cells": cells, "maximal": maximal,
            "pairs_x": np.abs(ex).ravel(), "pairs_y": np.abs(ey).ravel()}


def sorting_timing(asset: dict, minutes: float, start_s: float = 300.0, n_jobs: int = 4, seed: int = 1678) -> dict:
    """Time SpyKING CIRCUS 2 (spikeinterface) on `minutes` of the first series of a 20-min file,
    streamed from the archive (the sorter's working files go to a temporary directory).

    Settings: the multi-unit band of Methods 2.3 (500 to 3000 Hz), the detection threshold of 6 of
    Methods 2.6, the sorter's whitening (Methods 2.6, "spatial whitening"); motion correction is
    off, a standard choice for an array fixed in the cortex for one session; other settings are the
    sorter's defaults, as the claims file's standard choice. SpyKING CIRCUS 1, which the paper
    used, needs MPI and is not installable here; version 2 is its successor in spikeinterface. The
    positions are the assumed 4 x 4 layout at 0.5 mm; with 0.5 mm between contacts each spike is
    seen on one contact, so the layout does not change the sorting."""
    import os
    import shutil
    import tempfile
    import time as _time

    import spikeinterface.extractors as se
    import spikeinterface.preprocessing as spre
    import spikeinterface.sorters as ss
    from probeinterface import Probe

    url = requests.get(f"{API}/assets/{asset['asset_id']}/download/", allow_redirects=False, timeout=60).headers["Location"]
    rec = se.read_nwb_recording(file_path=url, stream_mode="remfile", electrical_series_path="acquisition/ElectricalSeries0")
    fs = rec.get_sampling_frequency()
    rec = rec.frame_slice(int(start_s * fs), int((start_s + 60 * minutes) * fs))
    pos = np.array([[(k % 4) * 500.0, (k // 4) * 500.0] for k in range(16)])
    probe = Probe(ndim=2)
    probe.set_contacts(positions=pos, shapes="circle", shape_params={"radius": 30})
    probe.set_device_channel_indices(np.arange(16))
    rec = spre.bandpass_filter(rec.set_probe(probe), freq_min=500, freq_max=3000)
    tmp = tempfile.mkdtemp()
    t0 = _time.time()
    try:
        sorting = ss.run_sorter(
            "spykingcircus2", rec, folder=os.path.join(tmp, "sc2"), verbose=False, apply_preprocessing=False,
            apply_motion_correction=False,
            detection={"method": "matched_filtering", "method_kwargs": {"peak_sign": "neg", "detect_threshold": 6}},
            job_kwargs={"n_jobs": n_jobs}, seed=seed)
        seconds = _time.time() - t0
        counts = sorting.count_num_spikes_per_unit()
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return {"subject": asset["path"].split("/")[0], "minutes": minutes, "seconds": seconds, "units": len(counts),
            "spikes_per_unit": sorted(int(v) for v in counts.values())}
