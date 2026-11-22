"""Loading and measures for dandiset 000458 (Claar et al. 2023), as used by Russo, Claar,
Furregoni et al. (2025), Nat Commun 16:3627, doi:10.1038/s41467-025-58717-2.

Each NWB file holds one session: 30-channel skull EEG (2500 Hz, int16, 0.195 uV per bit),
the raw LFP of up to three Neuropixels 1.0 probes (2500 Hz, 384 channels each), sorted units
with a CCF location and a waveform duration, the wheel speed (100 Hz, cm/s) and a trials table
(start time, current, target region and depth, behavioral epoch, `is_running`, `is_valid`).

Streaming. The signal arrays are stored in gzip chunks of about 34 s by 1 or 2 channels, so
reading any channel reads its whole time span. `read_array` opens the file once with remfile and
h5py to find the byte range of every chunk it needs, then fetches the chunks in parallel with
HTTP range requests and decompresses them; nothing is written to disk. Only the awake span of
the deep MOs stimulation trials is read.

Where the parameters come from (Methods of the paper unless said otherwise; "claims file" means
claims/russo-2025.yaml, whose criteria cite the paper's code):

- Trial selection: awake epoch, electrical stimulation of MOs at the deep target (Results,
  "targeting the deep layers of MOs (layer 5/6...)"). The three currents of a session are its
  low, intermediate and high intensities (Methods, three intensities per animal).
- State: rest when the mean wheel speed from -0.5 to +0.5 s is below 0.1 cm/s, active above
  (Methods, Evoked potentials analyses).
- EEG: the -3 to +3 ms artifact (at 2500 Hz, -3.2 to +2.4 ms) replaced by the reversed preceding
  signal of the same length, 0.5 Hz third-order
  Butterworth high-pass with filtfilt on the continuous signal, epochs -2 to +2 s (Methods, EEG
  quality control and pre-processing).
- LFP: epochs -2 to +2 s, linear detrend (Methods, Neuropixels EPs pre-processing); the 0 to 3 ms
  artifact replaced by the mirrored preceding signal and each channel and trial z-scored to -1 to
  -0.01 s (claims file, fig1d-lfp-late-rest-larger, from the code's CSD/LFP cell).
- CSD: channels exceeding 7 SD of the others interpolated, smoothing in time over 1.6 ms (4
  samples) and in depth over 26 then 4 channels, second spatial derivative, sigma 0.3 S/m
  (Methods). Assumption: the two sites of a Neuropixels row share a depth, so they are averaged
  into one site per 20 um row and the depth windows are applied in channels as 13 and 2 rows.
  The CSD is then z-scored per site and trial to -1 to -0.01 s like the LFP.
- Rectified amplitude: absolute value of the trial-averaged signal, averaged over the window
  and over channels (Methods). PLF: absolute value of the trial average of the unit phase
  vector of the Hilbert transform of each epoch, averaged over the window and channels
  (Methods, after Sinkkonen et al.). Windows early 3 to 50 ms and late 150 to 250 ms.
- Units: spikes in 0 to 2 ms after a pulse are removed (Methods). Cortical RS above 0.4 ms,
  FS at or below 0.4 ms; thalamic relay above 0.45 ms and TRN below 0.35 ms (Methods). Units
  under 0.35 ms located in RT itself form a class of their own (TRN-RT), added to TRN as a variant,
  since the Methods classify "thalamic units" by width and do not say which areas. SM-TH
  is the nuclei AV, CL, MD, PO, VAL, VPL, VPM and VM (Methods). Responsive: the trial-averaged
  rate in 3 to 500 ms leaves the baseline (-500 to -50 ms) mean by more than 7 SD (Methods).
  The paper estimates rates with an adaptive kernel; this module uses 10 ms bins, an assumption
  stated in the record.
- Latency: first spike in the window per trial; ISI the interval from the first spike to the
  next within the window; ROV the SD across units of the first-spike latency per trial (Methods,
  Unit analyses). Baseline rate the spike count in -1 to -0.01 s divided by 0.99 s (claims file,
  fig3e-baseline-rate-doubles, from the code's DFLoad_NSpikesWindow).
- Peak latency of EEG, LFP and CSD per trial: the largest peak of the global field power (SD
  across channels) in 75 to 250 ms whose prominence exceeds the mean plus 3 SD of the trial's
  baseline GFP (claims file, fig2b-thalamus-leads, from the code's FindResponsePeaks). The
  baseline is taken as -1 to -0.01 s, the baseline used elsewhere by the code (assumption). The GFP
  is computed over all channels and, as a variant, over the channels the file marks valid.
"""

from __future__ import annotations

import zlib
from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache

import h5py
import numpy as np
import pandas as pd
import remfile
import requests
from dandi.dandiapi import DandiAPIClient
from scipy import signal

DANDISET_ID = "000458"
DANDISET_VERSION = "0.230317.0039"

FS = 2500.0
EEG_UV_PER_BIT = None  # read from the file's conversion attribute
SM_TH = ["AV", "CL", "MD", "PO", "VAL", "VPL", "VPM", "VM"]
SPEED_THRESHOLD = 0.1          # cm/s, Methods
EARLY = (0.003, 0.050)         # s, Methods
LATE = (0.150, 0.250)          # s, Methods
REBOUND = (0.075, 0.250)       # s, code's DetectionTimeWindow (claims file)
BASELINE_Z = (-1.0, -0.01)     # s, code (claims file)
EPOCH = (-2.0, 2.0)            # s, Methods
KEEP = (-1.0, 0.5)             # s, part of each epoch kept after detrending and filtering
RS_MIN_MS, RELAY_MIN_MS, TRN_MAX_MS = 0.40, 0.45, 0.35
RESP_SD = 7.0
RESP_BIN = 0.010               # s, assumption (the paper uses an adaptive kernel)
N_THREADS = 32

_session = requests.Session()
_session.mount("https://", requests.adapters.HTTPAdapter(pool_connections=N_THREADS, pool_maxsize=N_THREADS))


@lru_cache(maxsize=1)
def asset_urls() -> dict:
    """Path to S3 URL of every asset of the pinned version."""
    ds = DandiAPIClient().get_dandiset(DANDISET_ID, DANDISET_VERSION)
    return {a.path: a.get_content_url(follow_redirects=1, strip_query=True) for a in ds.get_assets()}


def open_file(path: str):
    url = asset_urls()[path]
    return url, h5py.File(remfile.File(url), "r")


def _get(url, offset, size):
    for attempt in range(5):
        r = _session.get(url, headers={"Range": f"bytes={offset}-{offset + size - 1}"}, timeout=120)
        if r.status_code in (200, 206) and len(r.content) == size:
            return r.content
    raise IOError(f"range request failed for {url} at {offset}")


def read_array(url: str, d: h5py.Dataset, sel: list[tuple[int, int]]) -> np.ndarray:
    """Read d[sel] (one (start, stop) per dimension) by fetching its chunks in parallel."""
    dtype = d.dtype.newbyteorder("<") if d.dtype.byteorder in "=|" else d.dtype
    if d.chunks is None:
        assert d.ndim == 1 and d.compression is None
        off = d.id.get_offset()
        a, b = sel[0]
        return np.frombuffer(_get(url, off + a * d.dtype.itemsize, (b - a) * d.dtype.itemsize), dtype=dtype).copy()
    assert d.compression in (None, "gzip") and not d.shuffle
    ch = d.chunks
    grids = [range(a // c * c, b, c) for (a, b), c in zip(sel, ch)]
    coords = [tuple(x) for x in np.array(np.meshgrid(*grids, indexing="ij")).reshape(d.ndim, -1).T]
    out = np.empty([b - a for a, b in sel], dtype=d.dtype)

    def one(coord):
        info = d.id.get_chunk_info_by_coord(tuple(int(x) for x in coord))
        raw = _get(url, info.byte_offset, info.size)
        if d.compression == "gzip" and info.filter_mask == 0:
            raw = zlib.decompress(raw)
        block = np.frombuffer(raw, dtype=dtype).reshape(ch)
        src, dst = [], []
        for c0, c, (a, b) in zip(coord, ch, sel):
            lo, hi = max(a, c0), min(b, c0 + c)
            src.append(slice(lo - c0, hi - c0))
            dst.append(slice(lo - a, hi - a))
        out[tuple(dst)] = block[tuple(src)]

    with ThreadPoolExecutor(N_THREADS) as ex:
        list(ex.map(one, coords))
    return out


def _s(x):
    return x.decode() if isinstance(x, bytes) else x


def session_index() -> pd.DataFrame:
    """One row per asset: subject, the awake electrical blocks it holds, probes, unit count."""
    rows = []
    for path in sorted(asset_urls()):
        url, f = open_file(path)
        t = read_trials(f)
        aw = t[(t.behavioral_epoch == "awake") & (t.stimulus_type == "electrical")]
        for (reg, dep), g in aw.groupby(["estim_target_region", "estim_target_depth"]):
            rows.append({"path": path, "subject": _s(f["general/subject/subject_id"][()]),
                         "region": reg, "depth": dep,
                         "currents": sorted(g.estim_current.astype(float).unique().tolist()),
                         "n_trials": len(g), "n_valid": int(g.is_valid.sum()),
                         "probes": [k for k in f["acquisition"] if k.startswith("LFP")],
                         "n_units": int(f["units/id"].shape[0]) if "units" in f else 0})
    return pd.DataFrame(rows)


def read_trials(f) -> pd.DataFrame:
    T = f["intervals/trials"]
    cols = ["start_time", "stimulus_type", "estim_current", "estim_target_region", "estim_target_depth",
            "behavioral_epoch", "is_running", "is_valid"]
    return pd.DataFrame({k: [_s(v) for v in T[k][:]] for k in cols})


def deep_mos_trials(f) -> pd.DataFrame:
    """Awake trials of deep MOs electrical stimulation, with intensity labels and wheel speed."""
    t = read_trials(f)
    t = t[(t.behavioral_epoch == "awake") & (t.stimulus_type == "electrical")
          & (t.estim_target_region == "MOs") & (t.estim_target_depth == "deep")].copy()
    t["current"] = t.estim_current.astype(float)
    levels = sorted(t.current.unique())
    names = {3: ["low", "medium", "high"]}.get(len(levels))
    t["intensity"] = t.current.map(dict(zip(levels, names)))
    rs = f["processing/behavior/BehavioralTimeSeries/running_speed"]
    speed = rs["data"][:]
    t0, rate = float(rs["starting_time"][()]), float(rs["starting_time"].attrs["rate"])
    st = np.arange(len(speed)) / rate + t0
    t["speed"] = [speed[(st >= s - 0.5) & (st <= s + 0.5)].mean() for s in t.start_time]
    t["active"] = t.speed > SPEED_THRESHOLD
    return t.reset_index(drop=True)


def electrodes(f) -> pd.DataFrame:
    el = f["general/extracellular_ephys/electrodes"]
    return pd.DataFrame({k: [_s(v) for v in el[k][:]] for k in
                         ["location", "group_name", "is_data_valid", "probe_vertical_position",
                          "probe_horizontal_position"]})


# ---------------------------------------------------------------- continuous signals

def _span(url, f, series, onsets, cols):
    """Read the samples of `series` covering every epoch, for column range cols."""
    g = f[series]
    ts_d = g["timestamps"]
    # Timestamps of the span; the first and last onsets give the bounds.
    n = ts_d.shape[0]
    guess0 = int((onsets.min() - ts_d[0] - 3) * FS)
    guess1 = int((onsets.max() - ts_d[0] + 3) * FS)
    a, b = max(0, guess0 - 5000), min(n, guess1 + 5000)
    ts = read_array(url, ts_d, [(a, b)])
    idx = np.searchsorted(ts, onsets)
    lo, hi = int(idx.min() + EPOCH[0] * FS - 10), int(idx.max() + EPOCH[1] * FS + 10)
    data = read_array(url, g["data"], [(a + lo, a + hi), cols])
    return data, idx - lo, ts[lo:hi], float(g["data"].attrs["conversion"])


def mask_artifact_reversed(x, idx):
    """EEG: replace -3 to +3 ms around each onset with the reversed preceding signal (Methods).

    At 2500 Hz the span is 15 samples, from 8 samples before the onset: -3.2 to +2.4 ms (last sample),
    replaced by the reversed -9.2 to -3.6 ms. Outside every analysis window (3 ms on)."""
    n = int(round(0.006 * FS))         # 15 samples at 2500 Hz
    a = int(np.ceil(0.003 * FS))       # the masked span starts 8 samples before the onset
    for i in idx:
        x[i - a:i - a + n] = x[i - a - n:i - a][::-1]
    return x


def eeg_epochs(url, f, onsets):
    """EEG epochs (trials, channels, samples) from -1 to +0.5 s in uV after the Methods' preprocessing."""
    data, idx, ts, conv = _span(url, f, "acquisition/ElectricalSeriesEEG", onsets, (0, 30))
    sos = signal.butter(3, 0.5, btype="highpass", fs=FS, output="sos")
    k0, k1 = int(KEEP[0] * FS), int(KEEP[1] * FS)
    out = np.empty((len(idx), 30, k1 - k0), dtype=np.float32)
    for c in range(30):
        x = data[:, c].astype(np.float64) * conv * 1e6
        x = mask_artifact_reversed(x, idx)
        x = signal.sosfiltfilt(sos, x)
        for j, i in enumerate(idx):
            out[j, c] = x[i + k0:i + k1]
    onset_err = ts[idx] - onsets
    return out, onset_err, data, idx


def lfp_epochs(url, f, onsets, probe, cols):
    """Detrended LFP epochs (-2 to +2 s, then cut to -1 to +0.5 s), in uV, for columns cols."""
    series = f"acquisition/LFP{probe}/ElectricalSeries{probe}"
    data, idx, ts, conv = _span(url, f, series, onsets, cols)
    e0, e1 = int(EPOCH[0] * FS), int(EPOCH[1] * FS)
    k0, k1 = int(KEEP[0] * FS), int(KEEP[1] * FS)
    out = np.empty((len(idx), data.shape[1], k1 - k0), dtype=np.float32)
    for j, i in enumerate(idx):
        ep = data[i + e0:i + e1].astype(np.float64).T * conv * 1e6
        ep = signal.detrend(ep, axis=1)
        out[j] = ep[:, k0 - e0:k1 - e0]
    return out, ts[idx] - onsets


def times(n=None):
    k0, k1 = int(KEEP[0] * FS), int(KEEP[1] * FS)
    return np.arange(k0, k1) / FS


def mask_artifact_mirrored(ep):
    """LFP and CSD: replace 0 to 3 ms with the mirror of the preceding 3 ms (code, claims file)."""
    t = times()
    i0 = np.searchsorted(t, 0.0)
    n = int(round(0.003 * FS))
    ep[..., i0:i0 + n] = ep[..., i0 - n:i0][..., ::-1]
    return ep


def zscore_baseline(ep):
    t = times()
    b = (t >= BASELINE_Z[0]) & (t < BASELINE_Z[1])
    m = ep[..., b].mean(-1, keepdims=True)
    s = ep[..., b].std(-1, keepdims=True)
    s[s == 0] = np.nan
    return (ep - m) / s


def rows_from_channels(ep, vpos):
    """Average the channels that share a depth (a Neuropixels row); return rows ordered by depth."""
    depths = np.unique(vpos)
    out = np.stack([ep[:, vpos == d].mean(1) for d in depths], axis=1)
    return out, depths


def csd(ep_rows, spacing_um=20.0, sigma=0.3):
    """CSD (Methods): outlier sites interpolated, smoothed in time and depth, second derivative.

    ep_rows: (trials, sites, samples) in uV, sites ordered by depth. Returns uA/mm^3 units up to
    a constant (the state comparison is on z-scored values)."""
    x = ep_rows.astype(np.float64)
    # Sites whose amplitude exceeds 7 SD of the others at any instant are interpolated, iteratively.
    for _ in range(3):
        mu = x.mean(1, keepdims=True)
        sd = x.std(1, keepdims=True)
        bad = (np.abs(x - mu) > 7 * sd).any(-1)  # (trials, sites)
        if not bad.any():
            break
        for j, ch in zip(*np.nonzero(bad)):
            good = np.nonzero(~bad[j])[0]
            if len(good) < 2:
                continue
            below, above = good[good < ch], good[good > ch]
            if len(below) and len(above):
                a, b = below[-1], above[0]
                w = (ch - a) / (b - a)
                x[j, ch] = (1 - w) * x[j, a] + w * x[j, b]
            else:
                x[j, ch] = x[j, (below[-1] if len(below) else above[0])]
    # Smoothing: 1.6 ms in time (4 samples), then 26 and 4 channels in depth (13 and 2 rows).
    from scipy.ndimage import uniform_filter1d
    x = uniform_filter1d(x, 4, axis=2, mode="nearest")
    x = uniform_filter1d(x, 13, axis=1, mode="nearest")
    x = uniform_filter1d(x, 2, axis=1, mode="nearest")
    h = spacing_um * 1e-3  # mm
    d2 = np.zeros_like(x)
    d2[:, 1:-1] = (x[:, 2:] - 2 * x[:, 1:-1] + x[:, :-2]) / h ** 2
    d2[:, 0], d2[:, -1] = d2[:, 1], d2[:, -2]
    return (-sigma * d2).astype(np.float32)


def window_mask(win):
    t = times()
    return (t >= win[0]) & (t < win[1])


def rectified_amplitude(ep, trials, win):
    """|trial average| averaged over the window and channels (Methods). ep: (trials, ch, samples)."""
    if trials.sum() == 0:
        return np.nan
    m = np.nanmean(ep[trials], axis=0)
    return float(np.nanmean(np.abs(m[:, window_mask(win)])))


def code_amplitude(ep_z, trials, win):
    """Code's variant (claims file): mean of |single-trial z-scored signal| over window, channels, trials."""
    if trials.sum() == 0:
        return np.nan
    return float(np.nanmean(np.abs(ep_z[trials][:, :, window_mask(win)])))


def phase_vectors(ep):
    """Unit phase vectors of the Hilbert transform of each trial (complex64)."""
    a = signal.hilbert(ep, axis=-1)
    a = a / np.abs(a)
    return a.astype(np.complex64)


def plf(ph, trials, win):
    if trials.sum() == 0:
        return np.nan
    m = np.abs(np.nanmean(ph[trials], axis=0))
    return float(np.nanmean(m[:, window_mask(win)]))


def gfp_peak_latency(ep, win=REBOUND):
    """Per trial, latency of the largest GFP peak in win whose prominence exceeds baseline mean + 3 SD."""
    t = times()
    gfp = np.nanstd(ep, axis=1)  # (trials, samples)
    b = (t >= BASELINE_Z[0]) & (t < BASELINE_Z[1])
    w = (t >= win[0]) & (t < win[1])
    tw = t[w]
    out = np.full(len(gfp), np.nan)
    for j, g in enumerate(gfp):
        thr = g[b].mean() + 3 * g[b].std()
        pk, pr = signal.find_peaks(g[w], prominence=thr)
        if len(pk):
            out[j] = tw[pk[np.argmax(g[w][pk])]]
    return out


# ---------------------------------------------------------------- units

def units_table(url, f) -> pd.DataFrame:
    U = f["units"]
    df = pd.DataFrame({k: [_s(v) for v in U[k][:]] for k in ["location", "waveform_duration"]})
    df["unit_id"] = U["id"][:]
    groups = U["electrode_group"][:]
    df["probe"] = [f[g].name.split("/")[-1] if isinstance(g, h5py.Reference) else _s(g) for g in groups]
    idx = U["spike_times_index"][:]
    df["i0"] = np.r_[0, idx[:-1]]
    df["i1"] = idx
    df["area"] = np.select([df.location.str.startswith("MOs"), df.location.isin(SM_TH), df.location == "RT"],
                           ["MOs", "SM-TH", "RT"], "other")
    w = df.waveform_duration  # milliseconds in the files
    # TRN-RT: units under 0.35 ms located in RT itself, a variant of the TRN class (Methods classify
    # "thalamic units" by width; the main TRN class keeps to the SM-TH nuclei)
    df["cls"] = np.select([(df.area == "MOs") & (w > RS_MIN_MS), (df.area == "MOs") & (w <= RS_MIN_MS),
                           (df.area == "SM-TH") & (w > RELAY_MIN_MS), (df.area == "SM-TH") & (w < TRN_MAX_MS),
                           (df.area == "RT") & (w < TRN_MAX_MS)],
                          ["RS", "FS", "relay", "TRN", "TRN-RT"], "other")
    return df


def spikes_relative(url, f, units, onsets, pre=1.0, post=0.5):
    """For each unit, spike times relative to each onset in [-pre, post), spikes in 0-2 ms removed.

    Returns a list (per unit) of (rel_times, trial_index) arrays."""
    st_d = f["units/spike_times"]
    keep = units.index[units.cls != "other"]
    out = {}
    lo_t, hi_t = onsets.min() - pre, onsets.max() + post

    def one(i):
        r = units.loc[i]
        s = read_array(url, st_d, [(int(r.i0), int(r.i1))])
        s = s[(s >= lo_t) & (s < hi_t)]
        j = np.searchsorted(onsets, s + pre, side="right") - 1
        rel = s - onsets[np.clip(j, 0, None)]
        ok = (j >= 0) & (rel < post) & (rel >= -pre) & ~((rel >= 0) & (rel < 0.002))
        return i, (rel[ok], j[ok])

    with ThreadPoolExecutor(8) as ex:
        for i, v in ex.map(one, keep):
            out[i] = v
    return out


def responsive(rel, trial, trials_mask):
    """Methods: trial-averaged rate in 3-500 ms leaves the -500 to -50 ms baseline by > 7 SD."""
    n = trials_mask.sum()
    if n == 0:
        return False
    sel = trials_mask[trial]
    edges = np.arange(-0.5, 0.5 + 1e-9, RESP_BIN)
    h = np.histogram(rel[sel], edges)[0] / n / RESP_BIN
    c = edges[:-1] + RESP_BIN / 2
    b = h[(c > -0.5) & (c < -0.05)]
    r = h[(c > 0.003) & (c < 0.5)]
    sd = b.std()
    if sd == 0:
        sd = 1.0 / n / RESP_BIN  # one spike per bin when the baseline is silent
    return bool(np.any(np.abs(r - b.mean()) > RESP_SD * sd))


def first_spikes(rel, trial, n_trials, win):
    """Per trial: first-spike latency and the interval to the next spike, within win (NaN if none)."""
    lat = np.full(n_trials, np.nan)
    isi = np.full(n_trials, np.nan)
    m = (rel >= win[0]) & (rel < win[1])
    r, t = rel[m], trial[m]
    order = np.lexsort((r, t))
    r, t = r[order], t[order]
    if len(r) == 0:
        return lat, isi
    first = np.r_[True, t[1:] != t[:-1]]
    fi = np.nonzero(first)[0]
    lat[t[fi]] = r[fi]
    nxt = fi + 1
    ok = (nxt < len(r))
    ok[ok] &= t[nxt[ok]] == t[fi[ok]]
    isi[t[fi[ok]]] = r[nxt[ok]] - r[fi[ok]]
    return lat, isi


def counts_in(rel, trial, n_trials, win):
    m = (rel >= win[0]) & (rel < win[1])
    return np.bincount(trial[m], minlength=n_trials)


# ---------------------------------------------------------------- one session

THRESHOLDS = [0.1, 0.5, 1.0, 2.0, 5.0]   # cm/s; claims file, speed-threshold-robust


def _windows():
    t = times()
    return {"early": window_mask(EARLY), "late": window_mask(LATE)}


def _reduce(ep, z=None, valid=None):
    """Keep only the early and late samples of the epochs, their phase vectors and the GFP latency
    (over all channels, and over the channels the file marks valid when `valid` is given)."""
    w = _windows()
    sel = w["early"] | w["late"]
    out = {"x": ep[..., sel].astype(np.float32), "ph": phase_vectors(ep)[..., sel],
           "early": w["early"][sel], "late": w["late"][sel], "lat": gfp_peak_latency(ep)}
    if valid is not None:
        out["lat_valid"] = gfp_peak_latency(ep[:, valid])
    if z is not None:
        out["z"] = z[..., sel].astype(np.float32)
    # trial average over all trials of each intensity, for plotting (-0.1 to 0.4 s, mean |x| over channels)
    return out


def amplitude_table(red, trials, chan_ok, valid_reading):
    """Rectified amplitude and PLF per intensity, threshold and state from reduced epochs."""
    rows = []
    x = red["x"][:, chan_ok]
    ph = red["ph"][:, chan_ok]
    z = red.get("z")
    if z is not None:
        z = z[:, chan_ok]
    for inten in ["low", "medium", "high"]:
        base = (trials.intensity == inten).to_numpy()
        if valid_reading:
            base = base & trials.is_valid.to_numpy().astype(bool)
        for thr in THRESHOLDS + ["file"]:
            act = (trials.is_running.to_numpy() if thr == "file" else (trials.speed > thr).to_numpy())
            for state, m in [("rest", base & ~act), ("active", base & act)]:
                for win in ["early", "late"]:
                    wm = red[win]
                    row = {"intensity": inten, "threshold": thr, "valid": valid_reading, "state": state,
                           "window": win, "n": int(m.sum())}
                    if m.sum():
                        avg = x[m].mean(0)[:, wm]
                        row["amp"] = float(np.nanmean(np.abs(avg)))
                        row["plf"] = float(np.nanmean(np.abs(ph[m].mean(0)[:, wm])))
                        if z is not None:
                            row["code_amp"] = float(np.nanmean(np.abs(z[m][:, :, wm])))
                    rows.append(row)
    return pd.DataFrame(rows)


def process_session(path: str, with_lfp: bool = True) -> dict:
    """Everything the notebook needs from one session, reduced to small tables."""
    url, f = open_file(path)
    trials = deep_mos_trials(f)
    onsets = trials.start_time.to_numpy()
    el = electrodes(f)
    res = {"path": path, "subject": _s(f["general/subject/subject_id"][()]), "trials": trials}
    eeg_rows = el.index[el.group_name == "EEG array"]
    eeg_valid = el.loc[eeg_rows, "is_data_valid"].to_numpy().astype(bool)
    ep, err, raw, idx = eeg_epochs(url, f, onsets)
    # clock check: where the stimulation artifact sits in the raw trial-averaged EEG
    seg = np.stack([raw[i - 25:i + 26].astype(float) for i in idx])
    d = np.abs(np.diff(seg.mean(0), axis=0)).mean(1)
    res["eeg_artifact_lag_ms"] = (np.argmax(d) - 25 + 0.5) / FS * 1e3
    res["eeg_onset_err_ms"] = float(np.abs(err).max() * 1e3)
    del raw
    z = zscore_baseline(ep.copy())
    red = _reduce(ep, z, eeg_valid)
    t = times()
    res["eeg_single_late"] = np.nanmean(np.abs(ep[:, eeg_valid][:, :, window_mask(LATE)]), axis=(1, 2))
    tw = (t >= -0.1) & (t < 0.4)
    res["eeg_trace"] = {(i, s): np.abs(ep[(trials.intensity == i).to_numpy() & (trials.active == (s == "active")).to_numpy()][:, eeg_valid].mean(0)).mean(0)[tw]
                        for i in ["low", "medium", "high"] for s in ["rest", "active"]}
    res["eeg_range_uv"] = (float(np.nanmin(ep)), float(np.nanmax(ep)))
    del ep, z
    res["eeg_lat"], res["eeg_lat_valid"] = red["lat"], red["lat_valid"]
    res["eeg"] = pd.concat([amplitude_table(red, trials, np.ones(30, bool), False).assign(chan="all"),
                            amplitude_table(red, trials, eeg_valid, True).assign(chan="valid")])
    res["n_eeg_valid"] = int(eeg_valid.sum())
    del red
    res["has_probes"] = "units" in f
    if not res["has_probes"] or not with_lfp:
        return res
    # MOs channels of the probe that records MOs
    mos = el[el.location.astype(str).str.startswith("MOs") & (el.group_name != "EEG array")]
    probe = mos.group_name.value_counts().index[0]
    series = f"acquisition/LFP{probe}/ElectricalSeries{probe}"
    region = f[series]["electrodes"][:]
    col_of = {r: c for c, r in enumerate(region)}
    mos_cols = np.array(sorted(col_of[r] for r in mos.index[mos.group_name == probe]))
    c0, c1 = max(0, mos_cols.min() - 26), min(len(region), mos_cols.max() + 27)
    lfp, lerr = lfp_epochs(url, f, onsets, probe, (c0, c1))
    res["lfp_onset_err_ms"] = float(np.abs(lerr).max() * 1e3)
    res["lfp_probe"], res["n_mos_channels"] = probe, len(mos_cols)
    vpos = el.loc[region[c0:c1], "probe_vertical_position"].to_numpy()
    lvalid = el.loc[region[c0:c1], "is_data_valid"].to_numpy().astype(bool)
    is_mos = np.isin(np.arange(c0, c1), mos_cols)
    # clock check on the LFP: artifact before masking
    k = np.searchsorted(t, 0.0)
    dd = np.abs(np.diff(lfp[:, is_mos][:, :, k - 25:k + 26].mean(0), axis=1)).mean(0)
    res["lfp_artifact_lag_ms"] = (np.argmax(dd) - 25 + 0.5) / FS * 1e3
    # CSD from the detrended LFP, row by row, in batches of trials
    rows_v = np.unique(vpos[is_mos])
    csd_parts = []
    for b0 in range(0, len(lfp), 60):
        r, depths = rows_from_channels(lfp[b0:b0 + 60], vpos)
        csd_parts.append(csd(r)[:, np.isin(depths, rows_v)])
    cs = np.concatenate(csd_parts)
    del csd_parts
    lz = zscore_baseline(mask_artifact_mirrored(lfp[:, is_mos]))
    del lfp
    red = _reduce(lz, valid=lvalid[is_mos])
    res["lfp_lat"], res["lfp_lat_valid"] = red["lat"], red["lat_valid"]
    res["lfp"] = pd.concat([amplitude_table(red, trials, np.ones(is_mos.sum(), bool), False).assign(chan="all"),
                            amplitude_table(red, trials, lvalid[is_mos], True).assign(chan="valid")])
    del red, lz
    cz = zscore_baseline(mask_artifact_mirrored(cs))
    del cs
    res["csd_depth_profile"] = {(i, s): cz[(trials.intensity == i).to_numpy() & (trials.active == (s == "active")).to_numpy()].mean(0)[:, tw]
                                for i in ["low", "medium", "high"] for s in ["rest", "active"]}
    res["csd_depths"] = rows_v
    red = _reduce(cz)
    del cz
    res["csd_lat"] = red["lat"]
    res["csd"] = pd.concat([amplitude_table(red, trials, np.ones(len(rows_v), bool), False).assign(chan="all"),
                            amplitude_table(red, trials, np.ones(len(rows_v), bool), True).assign(chan="valid")])
    del red
    units = units_table(url, f)
    res["units"] = units
    res["spikes"] = spikes_relative(url, f, units, onsets)
    return res


# ---------------------------------------------------------------- per unit and trial

def unit_trial_table(r) -> pd.DataFrame:
    """One row per unit and trial for MOs RS/FS and SM-TH relay/TRN units of a session.

    Columns: first-spike latency and the interval to the next spike in the early (3-50 ms), rebound
    (75-250 ms) and late (150-250 ms) windows; late rate (spikes in 150-250 ms / 0.1 s); baseline
    rate (spikes in -1 to -0.01 s / 0.99 s); and whether the unit is responsive at the trial's
    intensity (Methods' 7 SD rule, on all trials of that intensity)."""
    tr = r["trials"]
    n = len(tr)
    inten = tr.intensity.to_numpy()
    parts = []
    for i, (rel, trial) in r["spikes"].items():
        u = r["units"].loc[i]
        resp = {k: responsive(rel, trial, inten == k) for k in ["low", "medium", "high"]}
        le, ie = first_spikes(rel, trial, n, EARLY)
        lr, ir = first_spikes(rel, trial, n, REBOUND)
        ll, il = first_spikes(rel, trial, n, LATE)
        parts.append(pd.DataFrame({
            "subject": r["subject"], "unit": int(u.unit_id), "cls": u.cls, "location": u.location,
            "trial": np.arange(n), "intensity": inten, "speed": tr.speed.to_numpy(),
            "is_valid": tr.is_valid.to_numpy().astype(bool),
            "responsive": [resp[k] for k in inten],
            "lat_early": le, "isi_early": ie, "lat_reb": lr, "isi_reb": ir, "lat_late": ll, "isi_late": il,
            "rate_late": counts_in(rel, trial, n, LATE) / (LATE[1] - LATE[0]),
            "rate_base": counts_in(rel, trial, n, BASELINE_Z) / (BASELINE_Z[1] - BASELINE_Z[0]),
        }))
    return pd.concat(parts, ignore_index=True)


def population_psth(r, cls, inten="high", bin_s=0.001, active=None):
    """Mean rate (Hz) over responsive units of a class, 1 ms bins from -0.5 to 0.5 s."""
    tr = r["trials"]
    m = (tr.intensity == inten).to_numpy()
    if active is not None:
        m &= (tr.active == active).to_numpy()
    edges = np.arange(-0.5, 0.5 + 1e-9, bin_s)
    rates = []
    for i, (rel, trial) in r["spikes"].items():
        if r["units"].loc[i, "cls"] != cls or not responsive(rel, trial, (tr.intensity == inten).to_numpy()):
            continue
        sel = m[trial]
        rates.append(np.histogram(rel[sel], edges)[0] / m.sum() / bin_s)
    return edges[:-1] + bin_s / 2, (np.mean(rates, 0) if rates else None), len(rates)


def crosscorr_value(sp_a, sp_b, max_lag=0.010, bin_s=0.002):
    """Methods: histogram (2 ms bins) of |delays| between the spikes of two units, divided by the
    number of seed spikes; the value is the mean over the first 10 ms (5 bins).

    sp_a, sp_b: lists of per-trial spike-time arrays in the window."""
    edges = np.arange(0, max_lag + 1e-12, bin_s)
    h = np.zeros(len(edges) - 1)
    n_seed = 0
    for a, b in zip(sp_a, sp_b):
        n_seed += len(a)
        if len(a) and len(b):
            h += np.histogram(np.abs(a[:, None] - b[None, :]).ravel(), edges)[0]
    return np.nan if n_seed == 0 else float((h / n_seed).mean())
