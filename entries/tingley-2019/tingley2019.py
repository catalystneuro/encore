"""Loading and shared measures for Tingley and Buzsaki (2019) on dandiset 000218.

Everything is streamed from the DANDI Archive (remfile + h5py); nothing is written to disk.

Where each parameter comes from:
- Event tables. The lab's own detections stored in each file (processing/ecephys): LS HFOs in
  `LSRipples`, CA1 ripples in `CA1Ripples`. The claims file's opening comment, open detail (i),
  reading (a): "where the dataset holds the events or their parameters, they are used". The
  earlier LS detections (`ls_ripples`, `ripples_ls`) and the hippocampal `ripplesALL` are used
  only as variants, where a recording lacks the main table (stated in the notebook).
- Event time. `peak_time` of the tables, which is bz_FindRipples' peak: the trough of the
  filtered signal (claims file, opening comment, open detail iv).
- Epochs. The dataset does not mark PRE, BEHAV and POST. The paper says "Each recording
  consisted of three periods of time recorded continuously; 1) pre-behavior home cage, 2) maze
  traversal, and 3) post-behavior home cage" (STAR Methods, Experimental model). Assumption:
  PRE is the recording before the first trial's start, BEHAV from the first trial's start to
  the last trial's stop, POST after the last trial's stop. Maze traversal in the narrow sense
  is inside trials (the claims' reading iv of fig4b).
- CCG bins and windows: 1 ms bins, +-200 ms (STAR Methods, Excess correlation analysis);
  +-120 ms and 241 points for compression (STAR Methods, Temporal compression analysis).
- Gaussian smoothing for excess correlation: 5 and 200 ms (STAR Methods), read as SD or as
  full width at half maximum (claims, fig4b reading ii); edges are handled by dividing by the
  kernel mass inside the window (claims, a standard choice).
"""
from __future__ import annotations

import json
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field

import h5py
import numpy as np
import pandas as pd
import remfile

DANDISET = "000218"
VERSION = "0.261110.1911"
API = f"https://api.dandiarchive.org/api/dandisets/{DANDISET}/versions/{VERSION}"
FS_LFP = 1250.0

HPC_REGIONS = ("hpc", "ca1", "ca3")


def list_assets() -> pd.DataFrame:
    """Every NWB asset of the pinned version, with its S3 URL."""
    url, rows = f"{API}/assets/?page_size=200&metadata=1", []
    while url:
        page = json.load(urllib.request.urlopen(url))
        for a in page["results"]:
            s3 = [u for u in a["metadata"]["contentUrl"] if "s3" in u][0]
            rows.append({"path": a["path"], "asset_id": a["asset_id"], "size_gb": a["size"] / 1e9, "url": s3})
        url = page["next"]
    df = pd.DataFrame(rows).sort_values("path").reset_index(drop=True)
    df["subject"] = df.path.str.extract(r"sub-(DT\d+)")[0]
    df["session"] = df.path.str.extract(r"_ses-(.+?)_(?:behavior\+)?ecephys")[0]
    return df


def _s(x):
    return x.decode() if isinstance(x, bytes) else str(x)


def open_nwb(url: str) -> h5py.File:
    return h5py.File(remfile.File(url), "r")


@dataclass
class Session:
    path: str
    subject: str
    session: str
    url: str
    duration: float = 0.0
    lfp_shape: tuple = ()
    spikes: list = field(default_factory=list)          # one sorted float64 array per unit
    unit_region: np.ndarray = None
    unit_shank: np.ndarray = None
    events: dict = field(default_factory=dict)          # table name -> DataFrame
    event_desc: dict = field(default_factory=dict)
    sleep: pd.DataFrame = None
    trials: pd.DataFrame = None
    electrodes: pd.DataFrame = None
    units_desc: str = ""

    @property
    def has_trials(self):
        return self.trials is not None and len(self.trials) > 0

    def units_in(self, regions):
        return np.flatnonzero(np.isin(self.unit_region, regions))

    def epochs(self, behav="span"):
        """PRE, BEHAV, POST intervals (see the module docstring for the assumption). behav='span'
        gives BEHAV as one interval, first trial start to last trial stop; behav='trials' gives the
        trial intervals themselves."""
        if not self.has_trials:
            return None
        t0, t1 = float(self.trials.start_time.min()), float(self.trials.stop_time.max())
        out = {"PRE": np.array([[0.0, t0]]), "POST": np.array([[t1, self.duration]])}
        if behav == "span":
            out["BEHAV"] = np.array([[t0, t1]])
        else:
            out["BEHAV"] = merge_intervals(self.trials[["start_time", "stop_time"]].to_numpy())
        return out

    def state_intervals(self, label):
        if self.sleep is None:
            return np.zeros((0, 2))
        s = self.sleep[self.sleep.label == label]
        return merge_intervals(s[["start_time", "stop_time"]].to_numpy())


def load_session(row) -> Session:
    """Spikes, units, event tables, sleep states, trials and electrode flags of one file. The LFP is
    not read; only its shape (for the recording's duration)."""
    f = open_nwb(row["url"])
    s = Session(path=row["path"], subject=row["subject"], session=row["session"], url=row["url"])
    lfp = f["processing/ecephys/LFP/lfp/data"]
    s.lfp_shape = lfp.shape
    s.duration = lfp.shape[0] / FS_LFP
    if "units" in f:
        u = f["units"]
        st = u["spike_times"][:]
        idx = u["spike_times_index"][:]
        starts = np.r_[0, idx[:-1]]
        s.spikes = [np.sort(st[a:b]) for a, b in zip(starts, idx)]
        s.unit_region = np.array([_s(x).lower() for x in u["region"][:]])
        s.unit_shank = u["shank"][:]
        s.units_desc = _s(u.attrs.get("description", ""))
    else:
        s.unit_region = np.array([], dtype=str)
        s.unit_shank = np.array([], dtype=int)
    if "processing/ecephys" in f:
        for k, g in f["processing/ecephys"].items():
            if _s(g.attrs.get("neurodata_type", "")) == "TimeIntervals":
                cols = {c: g[c][:] for c in g.keys() if c not in ("id",) and g[c].ndim == 1}
                s.events[k] = pd.DataFrame(cols).sort_values("start_time").reset_index(drop=True)
                s.event_desc[k] = _s(g.attrs.get("description", ""))
    if "processing/behavior/sleep_states" in f:
        g = f["processing/behavior/sleep_states"]
        s.sleep = pd.DataFrame({"label": [_s(x) for x in g["label"][:]],
                                "start_time": g["start_time"][:], "stop_time": g["stop_time"][:]})
    if "intervals/trials" in f:
        g = f["intervals/trials"]
        s.trials = pd.DataFrame({"start_time": g["start_time"][:], "stop_time": g["stop_time"][:]})
    el = f["general/extracellular_ephys/electrodes"]
    s.electrodes = pd.DataFrame({
        "region": [_s(x).lower() for x in el["region"][:]],
        "group_name": [_s(x) for x in el["group_name"][:]],
        "ls_channel": el["ls_channel"][:], "ca1_channel": el["ca1_channel"][:],
        "ca3_channel": el["ca3_channel"][:],
        "ripple_detection_channel": [_s(x) for x in el["ripple_detection_channel"][:]],
    })
    f.close()
    return s


def load_all(assets: pd.DataFrame, workers: int = 8) -> list[Session]:
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(load_session, [r for _, r in assets.iterrows()]))


# --- intervals ---------------------------------------------------------------

def merge_intervals(iv: np.ndarray) -> np.ndarray:
    iv = np.asarray(iv, float).reshape(-1, 2)
    if len(iv) == 0:
        return iv
    iv = iv[np.argsort(iv[:, 0])]
    out = [iv[0].copy()]
    for a, b in iv[1:]:
        if a <= out[-1][1]:
            out[-1][1] = max(out[-1][1], b)
        else:
            out.append(np.array([a, b]))
    return np.array(out)


def in_intervals(t: np.ndarray, iv: np.ndarray) -> np.ndarray:
    """Boolean mask of times inside merged, sorted intervals [start, stop]."""
    iv = merge_intervals(iv)
    if len(iv) == 0:
        return np.zeros(len(t), bool)
    i = np.searchsorted(iv[:, 0], t, side="right") - 1
    ok = i >= 0
    out = np.zeros(len(t), bool)
    out[ok] = t[ok] <= iv[i[ok], 1]
    return out


def intersect(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    a, b = merge_intervals(a), merge_intervals(b)
    out, i, j = [], 0, 0
    while i < len(a) and j < len(b):
        lo, hi = max(a[i, 0], b[j, 0]), min(a[i, 1], b[j, 1])
        if lo < hi:
            out.append((lo, hi))
        if a[i, 1] < b[j, 1]:
            i += 1
        else:
            j += 1
    return np.array(out).reshape(-1, 2)


def total(iv) -> float:
    iv = merge_intervals(iv)
    return float((iv[:, 1] - iv[:, 0]).sum()) if len(iv) else 0.0


def state_at(t: np.ndarray, sess: Session) -> np.ndarray:
    """Sleep state label at each time ('' where none is scored)."""
    out = np.full(len(t), "", dtype=object)
    if sess.sleep is None:
        return out
    for lab in sess.sleep.label.unique():
        out[in_intervals(t, sess.state_intervals(lab))] = lab
    return out


# --- cross-correlograms ------------------------------------------------------

def ccg_all(spikes: list, maxlag: float, binsize: float = 0.001, chunk: int = 200_000) -> np.ndarray:
    """Counts of spike pairs (i spike at t, j spike at t + lag) for every ordered unit pair, lags
    -maxlag..+maxlag in bins of binsize (centred, 2L+1 bins). Returns array [n, n, 2L+1] (int64)."""
    n = len(spikes)
    L = int(round(maxlag / binsize))
    nb = 2 * L + 1
    if n == 0:
        return np.zeros((0, 0, nb), np.int64)
    t = np.concatenate(spikes)
    u = np.concatenate([np.full(len(s), k, np.int64) for k, s in enumerate(spikes)])
    o = np.argsort(t, kind="stable")
    t, u = t[o], u[o]
    out = np.zeros(n * n * nb, np.int64)
    lo = np.searchsorted(t, t - (L + 0.5) * binsize, side="left")
    hi = np.searchsorted(t, t + (L + 0.5) * binsize, side="right")
    for c0 in range(0, len(t), chunk):
        c1 = min(len(t), c0 + chunk)
        cnt = hi[c0:c1] - lo[c0:c1]
        src = np.repeat(np.arange(c0, c1), cnt)
        # index of partners: lo[k] + 0..cnt-1
        offs = np.arange(cnt.sum()) - np.repeat(np.cumsum(cnt) - cnt, cnt)
        dst = np.repeat(lo[c0:c1], cnt) + offs
        keep = src != dst
        src, dst = src[keep], dst[keep]
        lag = np.rint((t[dst] - t[src]) / binsize).astype(np.int64) + L
        ok = (lag >= 0) & (lag < nb)
        idx = (u[src[ok]] * n + u[dst[ok]]) * nb + lag[ok]
        out += np.bincount(idx, minlength=n * n * nb)
    return out.reshape(n, n, nb)


def gauss_smooth(c: np.ndarray, width_ms: float, kind: str = "sd") -> np.ndarray:
    """Convolve CCGs (last axis, 1 ms bins) with a Gaussian; width is the SD (kind='sd') or the full
    width at half maximum ('fwhm'). Edges: divided by the kernel mass inside the window."""
    sd = width_ms if kind == "sd" else width_ms / 2.3548
    half = int(np.ceil(4 * sd))
    x = np.arange(-half, half + 1)
    k = np.exp(-0.5 * (x / sd) ** 2)
    k /= k.sum()
    from scipy.signal import fftconvolve
    shape = [1] * (c.ndim - 1) + [len(k)]
    num = fftconvolve(c, k.reshape(shape), mode="same", axes=-1)
    den = fftconvolve(np.ones(c.shape[-1]), k, mode="same")
    return num / den


def jitter(spikes: list, rng, width: float = 0.2) -> list:
    """Every spike moved by a uniform random amount in +-width (STAR Methods, Excess correlation)."""
    return [np.sort(s + rng.uniform(-width, width, len(s))) for s in spikes]


def restrict(spikes: list, iv: np.ndarray) -> list:
    return [s[in_intervals(s, iv)] for s in spikes]


def triggered_counts(spikes: np.ndarray, times: np.ndarray, maxlag: float, binsize: float) -> np.ndarray:
    """Spike counts of one unit around each trigger time: array [n_triggers, n_bins], bins centred on
    lags -maxlag..maxlag."""
    L = int(round(maxlag / binsize))
    edges = (np.arange(-L, L + 2) - 0.5) * binsize
    lo = np.searchsorted(spikes, times + edges[0])
    hi = np.searchsorted(spikes, times + edges[-1])
    out = np.zeros((len(times), 2 * L + 1), np.int32)
    for k in np.flatnonzero(hi > lo):
        d = spikes[lo[k]:hi[k]] - times[k]
        out[k] = np.histogram(d, edges)[0]
    return out


def count_in(spikes: np.ndarray, starts: np.ndarray, stops: np.ndarray) -> np.ndarray:
    return np.searchsorted(spikes, stops, side="right") - np.searchsorted(spikes, starts, side="left")


# --- LFP ---------------------------------------------------------------------
# Parameters (STAR Methods, Phase locking analysis): 120-200 Hz, 4th-order Butterworth, 7 ms RMS smoothing,
# epochs continuously above 2 SD of the mean, Hilbert phase, more than 50 spikes, Rayleigh p < 0.05, null of
# 10 circular shifts of the LFP phases. Detection (STAR Methods, Ripple detection): 120-200 Hz, Butterworth
# order 3, normalized squared signal (NSS). Zero-phase filtering (filtfilt) is a standard choice.

def block_rows(url: str, row: int) -> np.ndarray:
    """Electrode-table rows of the 16-channel storage block (the file's chunking) that holds row `row`."""
    f = open_nwb(url)
    d = f["processing/ecephys/LFP/lfp/data"]
    el = f["processing/ecephys/LFP/lfp/electrodes"][:]
    col = int(np.flatnonzero(el == row)[0]); cw = d.chunks[1]
    out = el[(col // cw) * cw:min(d.shape[1], (col // cw + 1) * cw)]
    f.close()
    return out


def read_lfp_block(url: str, row: int, keep_rows=None, t_chunks=None):
    """The storage block (16 channels, the file's chunking) that holds electrode-table row `row`, read whole
    (reading one channel costs the same); only the columns of `keep_rows` are kept (int16; whole recording,
    or only the listed time chunks, concatenated). Returns the data, the rows kept, and the sample offset of
    each time chunk read."""
    f = open_nwb(url)
    d = f["processing/ecephys/LFP/lfp/data"]
    el = f["processing/ecephys/LFP/lfp/electrodes"][:]
    col = int(np.flatnonzero(el == row)[0])
    cw = d.chunks[1]
    c0, c1 = (col // cw) * cw, min(d.shape[1], (col // cw + 1) * cw)
    ch = d.chunks[0]
    rows = el[c0:c1]
    sel = np.arange(len(rows)) if keep_rows is None else np.flatnonzero(np.isin(rows, keep_rows))
    ks = list(range(int(np.ceil(d.shape[0] / ch)))) if t_chunks is None else list(t_chunks)
    pieces = [d[k * ch:min(d.shape[0], (k + 1) * ch), c0:c1][:, sel] for k in ks]
    f.close()
    return np.concatenate(pieces), rows[sel], [k * ch for k in ks]


def read_lfp_all(url: str, t_chunks):
    """Every channel of the listed time chunks (int16), with the electrode-table row of each column."""
    f = open_nwb(url)
    d = f["processing/ecephys/LFP/lfp/data"]
    el = f["processing/ecephys/LFP/lfp/electrodes"][:]
    ch = d.chunks[0]
    pieces = [(k * ch, d[k * ch:min(d.shape[0], (k + 1) * ch), :]) for k in t_chunks]
    f.close()
    return pieces, el


def electrode_spike_groups(url: str) -> np.ndarray:
    f = open_nwb(url)
    g = f["general/extracellular_ephys/electrodes/spike_group"][:]
    f.close()
    return g


def bandpass(x, lo, hi, order, fs=FS_LFP):
    from scipy.signal import butter, sosfiltfilt
    sos = butter(order, [lo, hi], btype="band", fs=fs, output="sos")
    return sosfiltfilt(sos, x).astype(np.float32)


def analytic(x, seg=1 << 22, pad=1 << 12):
    """Analytic signal (Hilbert transform) computed in overlapping segments, to bound memory."""
    from scipy.signal import hilbert
    n = len(x)
    out = np.empty(n, np.complex64)
    for a in range(0, n, seg):
        b = min(n, a + seg)
        lo, hi = max(0, a - pad), min(n, b + pad)
        h = hilbert(x[lo:hi].astype(np.float64))
        out[a:b] = h[a - lo:a - lo + (b - a)]
    return out


def high_power_epochs(filt, fs=FS_LFP, rms_ms=7.0, sd=2.0):
    """Mask of samples where the RMS-smoothed band power is above mean + sd * SD (continuous runs)."""
    w = max(int(round(rms_ms / 1000 * fs)), 1)
    p = np.sqrt(np.convolve(filt.astype(np.float64) ** 2, np.ones(w) / w, mode="same"))
    return p > p.mean() + sd * p.std()


def rayleigh(ph):
    """Rayleigh test (Zar; as CircStat's circ_rtest). Returns p, mean resultant length, mean angle."""
    n = len(ph)
    if n == 0:
        return np.nan, np.nan, np.nan
    C, S_ = np.cos(ph).sum(), np.sin(ph).sum()
    R = np.hypot(C, S_)
    r = R / n
    z = R ** 2 / n
    p = np.exp(np.sqrt(1 + 4 * n + 4 * (n ** 2 - R ** 2)) - (1 + 2 * n))
    return float(min(p, 1.0)), float(r), float(np.arctan2(S_, C))


def nss(filt):
    """Normalized squared signal: the squared filtered LFP, z-scored over the recording."""
    sq = filt.astype(np.float64) ** 2
    return ((sq - sq.mean()) / sq.std()).astype(np.float32)


def lock_units(spk_list, ph, mask, rng, n_null=10, min_spikes=50, fs=FS_LFP):
    """Per unit: spikes inside the mask, Rayleigh p, resultant length and mean phase, and the Rayleigh p-values
    under `n_null` circular shifts of the phase (STAR Methods, Phase locking analysis: 10 iterations); the shifts
    are drawn from `rng` (the claim's seed)."""
    n = len(ph)
    shifts = rng.integers(int(fs * 1), n - int(fs * 1), n_null)
    res = []
    for sp in spk_list:
        idx = np.rint(sp * fs).astype(np.int64)
        idx = idx[(idx >= 0) & (idx < n)]
        idx = idx[mask[idx]]
        p, r, a = rayleigh(ph[idx].astype(np.float64))
        pn = [rayleigh(ph[(idx + k) % n].astype(np.float64))[0] for k in shifts] if len(idx) > min_spikes else [np.nan] * n_null
        res.append(dict(n=len(idx), p=p, r=r, angle=a, p_null=pn))
    return res


def lfp_columns(url: str):
    """The LFP's electrode-table row of each column and the storage block width (channels per chunk)."""
    f = open_nwb(url)
    d = f["processing/ecephys/LFP/lfp/data"]
    el = f["processing/ecephys/LFP/lfp/electrodes"][:]
    cw = d.chunks[1]
    f.close()
    return el, cw
