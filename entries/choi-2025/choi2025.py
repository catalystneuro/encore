"""Loading and measures for Choi et al. (2025), J Neurosci Methods 110467, on dandiset 002014.

The dandiset holds one NWB file, session 09/27/2024 of monkey T. Everything is streamed from
the archive at the pinned version (remfile and h5py); nothing is written to disk.

Where each parameter comes from:

- Trial classes, the value cue V (code 23) and the reward RW (codes 101 and 100): the claims
  file's opening comment. A trial is the span from its trial-start event (code 128, the trials
  table's midpoint_time) to the next code-128 event; large (small) successful trials hold a
  big (small) reward event and no error event. The last row, which has no next trial start,
  is not classed: the paper's Zenodo lists leave it out (verifier round 1).
- The dopamine window (V to RW), the reference at V, the 5 s windows of fig8a, the spike
  windows, bins and random alignments of fig9a, the refractory and waveform tests of fig9bc,
  the beta band, filter, windows and measure of fig9d: the claims' criteria.
- The time of a dopamine sample: the trial-aligned table states 601 samples at 10 Hz from
  30 s before to 30 s after the trial midpoint (its description and start_time/stop_time).
- The paper's large and small trial ids (1-based, "tr1-1411"): its Zenodo deposit
  (doi:10.5281/zenodo.14825992), named in the paper's Data availability statement; used only
  to check the trial classes.
- A 4th order Butterworth band-pass is designed with N = 4 (scipy's and MATLAB's convention);
  this is a standard choice and is stated in the claim's criterion.
"""

from __future__ import annotations

import io
import urllib.parse
import zlib

import h5py
import numpy as np
import pandas as pd
import remfile
import requests
from scipy import signal, stats

DANDISET_ID = "002014"
DANDISET_VERSION = "0.261120.0528"
API = "https://api.dandiarchive.org/api"
ZENODO_RECORD = "14825992"
PAPER_KEY = "choi-2025"

ERROR_PREFIX = "error"
DA_RATE = 10.0  # Hz, trial-aligned FSCV (table description and its `rate` column)
DA_PRE = 30.0  # s before the trial midpoint at which each trial-aligned series starts


def seed(claim_id: str, offset: int = 0) -> int:
    """The claim's seed (docs/protocol.md): crc32 of "<paper>/<claim>", plus an offset."""
    return zlib.crc32(f"{PAPER_KEY}/{claim_id}".encode()) + offset


def list_assets() -> list[dict]:
    r = requests.get(f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/",
                     params={"page_size": 100}, timeout=60)
    r.raise_for_status()
    return r.json()["results"]


def version_metadata() -> dict:
    r = requests.get(f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/", timeout=60)
    r.raise_for_status()
    return r.json()


def open_nwb(asset: dict) -> h5py.File:
    """Open the asset by streaming its S3 object."""
    url = requests.head(f"{API}/assets/{asset['asset_id']}/download/", allow_redirects=True,
                        timeout=60).url
    return h5py.File(remfile.File(url), "r")


def text(x) -> str:
    return x.decode() if isinstance(x, bytes) else str(x)


def load_events(f: h5py.File) -> dict[str, np.ndarray]:
    """Event times by label, from the AnnotatedEventsTable."""
    ev = f["processing/events/events_table"]
    idx = ev["event_times_index"][()]
    times = ev["event_times"][()]
    labels = [text(x) for x in ev["label"][()]]
    out, start = {}, 0
    for lab, stop in zip(labels, idx):
        out[lab] = times[start:stop]
        start = stop
    return out


def event_descriptions(f: h5py.File) -> pd.DataFrame:
    ev = f["processing/events/events_table"]
    idx = ev["event_times_index"][()]
    return pd.DataFrame({"label": [text(x) for x in ev["label"][()]],
                         "description": [text(x) for x in ev["event_description"][()]],
                         "n": np.diff(np.r_[0, idx])})


def _first_in(times: np.ndarray, a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """First event time in [a, b) for each span, NaN when there is none."""
    i = np.searchsorted(times, a, side="left")
    out = np.full(len(a), np.nan)
    ok = i < len(times)
    t = np.where(ok, times[np.minimum(i, len(times) - 1)], np.inf)
    hit = ok & (t < b)
    out[hit] = t[hit]
    return out


def _any_in(times: np.ndarray, a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return np.searchsorted(times, b, side="left") > np.searchsorted(times, a, side="left")


def trial_table(f: h5py.File, events: dict[str, np.ndarray]) -> pd.DataFrame:
    """One row per row of the trials table, classed from the events (claims file, opening comment).

    `index` is 0-based (the row of the trials table and of the trial-aligned FSCV table);
    `trial_id` is 1-based, as in the paper's Zenodo trial lists.
    """
    mid = f["intervals/trials/midpoint_time"][()]
    starts = np.sort(events["intended trial start"])
    j = np.searchsorted(starts, mid, side="right")
    nxt = np.where(j < len(starts), starts[np.minimum(j, len(starts) - 1)], np.inf)
    errors = np.sort(np.concatenate([v for k, v in events.items() if k.startswith(ERROR_PREFIX)]))
    df = pd.DataFrame({"index": np.arange(len(mid)), "trial_id": np.arange(1, len(mid) + 1),
                       "start": mid, "next_start": nxt})
    df["V"] = _first_in(events["value object start"], mid, nxt)
    df["big"] = _any_in(events["big reward"], mid, nxt)
    df["small"] = _any_in(events["small reward"], mid, nxt)
    df["error"] = _any_in(errors, mid, nxt)
    rw_big = _first_in(events["big reward"], mid, nxt)
    rw_small = _first_in(events["small reward"], mid, nxt)
    df["RW"] = np.where(df["big"], rw_big, rw_small)
    # the last row has no next trial start, so its span is open; the paper's lists leave it out
    closed = np.isfinite(nxt)
    df["large_success"] = df["big"] & ~df["error"] & closed
    df["small_success"] = df["small"] & ~df["error"] & closed
    df["success"] = df["large_success"] | df["small_success"]
    df["cls"] = np.select([df["large_success"], df["small_success"]], ["large", "small"], "other")
    return df


def zenodo_trial_ids() -> dict[str, np.ndarray]:
    """The paper's 1-based ids of large and small successful trials (Zenodo record, small .mat files)."""
    from scipy.io import loadmat
    names = {"large": "09272024_nlx_c8c_value object start_big rew and success_tr1-1411.mat",
             "small": "09272024_nlx_c8c_value object start_small rew and success_tr1-1411.mat"}
    out = {}
    for k, name in names.items():
        url = (f"https://zenodo.org/api/records/{ZENODO_RECORD}/files/"
               f"{urllib.parse.quote(name)}/content")
        r = requests.get(url, timeout=120)
        r.raise_for_status()
        out[k] = np.asarray(loadmat(io.BytesIO(r.content), squeeze_me=True)["trids_out"]).astype(int)
    return out


def zenodo_files() -> pd.DataFrame:
    r = requests.get(f"https://zenodo.org/api/records/{ZENODO_RECORD}", timeout=60)
    r.raise_for_status()
    return pd.DataFrame([{"key": x["key"], "size": x["size"], "checksum": x["checksum"]}
                         for x in r.json()["files"]])


# ---------------------------------------------------------------- dopamine (trial-aligned FSCV)

def load_fscv(f: h5py.File) -> dict[str, np.ndarray]:
    g = f["processing/fscv/trial_aligned_fscv_table"]
    return {k: g[k][()] for k in ["da", "ph", "m", "iox", "good", "rate", "start_time",
                                  "stop_time", "trial_index"]}


def da_times(n: int = 601) -> np.ndarray:
    """Time of each trial-aligned sample relative to the trial midpoint (s)."""
    return np.arange(n) / DA_RATE - DA_PRE


def value_at(trace: np.ndarray, t: np.ndarray, t0: float) -> float:
    """Linear interpolation of the trace at t0 (NaN samples left out)."""
    ok = ~np.isnan(trace)
    if ok.sum() < 2:
        return np.nan
    return float(np.interp(t0, t[ok], trace[ok], left=np.nan, right=np.nan))


def window_mean(trace: np.ndarray, t: np.ndarray, a: float, b: float) -> float:
    m = (t >= a) & (t <= b)
    v = trace[m]
    return float(np.nanmean(v)) if np.isfinite(v).any() else np.nan


def window_sd(trace: np.ndarray, t: np.ndarray, a: float, b: float, closed: str) -> float:
    """SD of the samples in (a, b] (closed='right') or [a, b) (closed='left')."""
    m = ((t > a) & (t <= b)) if closed == "right" else ((t >= a) & (t < b))
    v = trace[m]
    v = v[np.isfinite(v)]
    return float(np.std(v, ddof=1)) if len(v) > 2 else np.nan


# ---------------------------------------------------------------- spikes

def load_units(f: h5py.File, path: str) -> dict[str, np.ndarray]:
    u = f[path]
    idx = u["spike_times_index"][()]
    st = u["spike_times"][()]
    names = [text(x) for x in u["unit_name"][()]]
    out, a = {}, 0
    for n, b in zip(names, idx):
        out[n] = st[a:b]
        a = b
    return out


def thresholded_waveforms(f: h5py.File, unit_row: int) -> np.ndarray:
    """Waveforms (spikes x 48 samples, volts) of one row of the thresholded_units table."""
    u = f["processing/ecephys/thresholded_units"]
    si = u["spike_times_index"][()]
    wi = u["waveforms_index"][()]
    a_sp = 0 if unit_row == 0 else si[unit_row - 1]
    b_sp = si[unit_row]
    a = 0 if a_sp == 0 else wi[a_sp - 1]
    b = wi[b_sp - 1]
    w = u["waveforms"][a:b, 0]
    return w.reshape(b_sp - a_sp, -1)


def psth(spikes: np.ndarray, align: np.ndarray, edges: np.ndarray) -> np.ndarray:
    """Spike counts per trial (rows) and bin (columns) around each alignment time."""
    out = np.zeros((len(align), len(edges) - 1))
    for i, t0 in enumerate(align):
        a, b = np.searchsorted(spikes, [t0 + edges[0], t0 + edges[-1]])
        out[i] = np.histogram(spikes[a:b] - t0, edges)[0]
    return out


def psth_variance(spikes: np.ndarray, align: np.ndarray, edges: np.ndarray) -> float:
    """Variance across bins of the trial-averaged firing rate (spikes/s)."""
    rate = psth(spikes, align, edges).mean(0) / np.diff(edges)
    return float(np.var(rate))


# ---------------------------------------------------------------- LFP

def load_lfp(f: h5py.File) -> tuple[np.ndarray, np.ndarray]:
    g = f["processing/ecephys/FilteredEphys/bipolar_lfp_series"]
    return g["timestamps"][()], g["data"][:, 0]


def lfp_segment(t: np.ndarray, x: np.ndarray, t0: float, pre: float, post: float,
                fs: float = 1000.0) -> np.ndarray:
    """The stored LFP from t0 - pre to t0 + post on a regular 1 kHz grid (linear interpolation of
    the stored samples; NaN where a stored sample within 2 ms is missing or NaN)."""
    grid = t0 + np.arange(-pre, post, 1 / fs)
    a, b = np.searchsorted(t, [grid[0] - 0.01, grid[-1] + 0.01])
    tt, xx = t[a:b], x[a:b]
    if len(tt) < 2:
        return np.full(len(grid), np.nan)
    y = np.interp(grid, tt, xx)
    j = np.clip(np.searchsorted(tt, grid), 1, len(tt) - 1)
    gap = np.minimum(np.abs(tt[j] - grid), np.abs(tt[j - 1] - grid)) > 0.002
    y[gap] = np.nan  # np.interp already gives NaN next to a NaN sample
    return y


def band_power(seg: np.ndarray, band: tuple[float, float], fs: float = 1000.0,
               order: int = 4) -> np.ndarray:
    """Squared Hilbert envelope of the zero-phase Butterworth band-passed segment."""
    sos = signal.butter(order, band, btype="bandpass", fs=fs, output="sos")
    return np.abs(signal.hilbert(signal.sosfiltfilt(sos, seg))) ** 2


def beta_suppression(seg: np.ndarray, pre: float, band, win: float, base: float,
                     fs: float = 1000.0) -> float:
    """log10(mean power over 0..win after V / mean power over base before V); NaN if the
    segment has any NaN. `seg` starts `pre` s before V."""
    if np.isnan(seg).any():
        return np.nan
    p = band_power(seg, band, fs)
    i0 = int(round(pre * fs))
    return float(np.log10(p[i0:i0 + int(round(win * fs))].mean() /
                          p[i0 - int(round(base * fs)):i0].mean()))


def mannwhitney(a, b) -> tuple[float, float]:
    a = np.asarray(a, float)
    b = np.asarray(b, float)
    a, b = a[np.isfinite(a)], b[np.isfinite(b)]
    r = stats.mannwhitneyu(a, b, alternative="two-sided")
    return float(r.statistic), float(r.pvalue)
