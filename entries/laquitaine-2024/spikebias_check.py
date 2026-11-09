"""Loading and measures for dandiset 001250 (Laquitaine et al., "Spike sorting biases and
information loss in a detailed cortical model", bioRxiv doi:10.1101/2024.12.04.626805).

The dandiset holds the fitted simulated traces (Neuropixels spontaneous NS, evoked E, dense probe
DS at three depths), the ground truth spike times of the model neurons within 50 um of the probe,
the in vivo traces the paper compares with (Marques-Smith M, Horvath H at three depths), and the
paper's own sortings (Kilosort, 2, 2.5, 3, 4 and herdingspikes) as NWB Units tables. Every file is
streamed from the archive at the pinned version; nothing is written to disk.

Where the parameters come from (claims file claims/001250/10.1101-2024.12.04.626805.yaml, whose
opening comment cites the paper and the code, github.com/steevelaquitaine/spikebias at commit
6e9af03b81c3892aafa94b2d10b724ef59fdb247):

- `DELTA_TIME_MS` = 1.3 ms, the coincidence window of the agreement score (claims file, opening
  comment; Methods, Agreement Score). Agreement scores use SpikeInterface
  `compare_sorter_to_ground_truth(exhaustive_gt=True)`, as the code's `get_scores` does.
- `chance_scores` follows the code's `_compute_chance_score` (claims file, opening comment).
- `qualify_units` follows the code's `qualify_sorted_units` (src/nodes/metrics/quality.py).
- `THR_GOOD` = 0.8, well sorted (claims file, opening comment).
- `DURATION_S` = 600, the first 10 minutes (claims file, opening comment); 240 s for the
  Kilosort2 sorting of the evoked recording (`SORT_DURATION_S`, Methods, Spike sorting).
- `std_layer` merges L2 and L3 into L2/3, as the code's `standardize_layers` (src/nodes/utils.py)
  does; WM and Outside are outside the cortex.
- Preprocessing: a 300 Hz high-pass and a global common median reference (Methods,
  Preprocessing). The filter is SpikeInterface's default high-pass (Butterworth of order 5,
  second order sections, forward and backward), applied here with scipy; the code also casts the
  traces to int16 before filtering, which is not done here (a detail of the code that cannot
  change a per-layer comparison by more than a rounding of 1 uV).
- Trace statistics are computed on `N_BLOCKS` blocks of `BLOCK_S` seconds spread over the first
  10 minutes, not on the whole 10 minutes: holding the whole 10 minutes of every recording
  (about 110 GB) does not fit the run. This is a deviation, recorded in the attempt; the block
  layout is a choice made here. The extremes (maxima, ANR range), which grow with duration, are
  also streamed over the whole first 600 s by `trace_extremes`.
- Noise per site: the mean absolute deviation in 1 s segments, minimum over segments (code,
  src/nodes/validation/noise.py, `measure_trace_noise`); the median absolute deviation is the
  variant of the Methods (Amplitude-to-noise ratio).
- Power spectra: Welch, Hann window, 1 Hz resolution (nperseg = sampling rate), Methods, Spectral
  composition.
"""

from __future__ import annotations

from concurrent.futures import ProcessPoolExecutor
from functools import lru_cache

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy import signal

DANDISET_ID = "001250"
DANDISET_VERSION = "0.251012.1648"

DELTA_TIME_MS = 1.3
THR_GOOD = 0.8
DURATION_S = 600.0
FREQ_MIN = 300.0
BLOCK_S = 10.0
N_BLOCKS = 6
LAYERS = ["L1", "L2/3", "L4", "L5", "L6"]

# experiment -> recording file, sampling rate
RECORDINGS = {
    "NS": "sub-001-fitted/sub-001-fitted_ecephys.nwb",
    "E": "sub-002-fitted/sub-002-fitted_ecephys.nwb",
    "E40": "sub-npx-evoked-sf-40Hz-fitted/sub-npx-evoked-sf-40Hz-fitted_ecephys.nwb",
    "DS1": "sub-003-fitted/sub-003-fitted_ecephys.nwb",
    "DS2": "sub-004-fitted/sub-004-fitted_ecephys.nwb",
    "DS3": "sub-005-fitted/sub-005-fitted_ecephys.nwb",
    "M": "sub-vivo-marques-smith/sub-vivo-marques-smith_ecephys.nwb",
    "H1": "sub-vivo-horvath-depth-1/sub-vivo-horvath-depth-1_ecephys.nwb",
    "H2": "sub-vivo-horvath-depth-2/sub-vivo-horvath-depth-2_ecephys.nwb",
    "H3": "sub-vivo-horvath-depth-3/sub-vivo-horvath-depth-3_ecephys.nwb",
    "S": "sub-mearec-synthetics-buccino-rep/sub-mearec-synthetics-buccino-rep_ecephys.nwb",
}
# ground truth tables with the neurons' properties (the fitted files repeat the spike times only)
GROUND_TRUTH = {
    "NS": "sub-001/sub-001_ecephys.nwb",
    "E": "sub-002/sub-002_ecephys.nwb",
    "E40": "sub-npx-evoked-sf-40Hz/sub-npx-evoked-sf-40Hz_ecephys.nwb",
    "DS1": "sub-003/sub-003_ecephys.nwb",
    "DS2": "sub-004/sub-004_ecephys.nwb",
    "DS3": "sub-005/sub-005_ecephys.nwb",
    "S": "sub-mearec-synthetics-buccino-rep/sub-mearec-synthetics-buccino-rep_ecephys.nwb",
}
# Kilosort2 sorted only the first 4 minutes of the evoked recording: "We report results from
# Kilosort2 for 4 minutes of evoked recordings, as it failed to process longer durations"
# (Methods, Spike sorting); the deposited 10-minute Kilosort2 sorting of E ends at 240 s (data
# check). Its rates and scores use 240 s (verifier round 1, problem 4).
SORT_DURATION_S = {("E", "KS2"): 240.0}


def sort_duration(exp: str, sorter: str) -> float:
    return SORT_DURATION_S.get((exp, sorter), DURATION_S)


SORTER_TAGS = {"KS4": "ks4", "KS3": "ks3", "KS2.5": "ks25", "KS2": "ks2", "KS": "ks", "HS": "hs"}
SORTING_SUBJECT = {
    "NS": "sub-001-fitted", "E": "sub-002-fitted", "M": "sub-vivo-marques-smith",
    "DS1": "sub-003-fitted", "DS2": "sub-004-fitted", "DS3": "sub-005-fitted",
    "H1": "sub-vivo-horvath-depth-1", "H2": "sub-vivo-horvath-depth-2",
    "H3": "sub-vivo-horvath-depth-3",
}
SAMPLING_HZ = {"NS": 40000, "E": 20000, "E40": 40000, "M": 30000, "S": 32000,
               "DS1": 20000, "DS2": 20000, "DS3": 20000, "H1": 20000, "H2": 20000, "H3": 20000}


def sorting_path(exp: str, sorter: str, ten_min: bool = True) -> str:
    sub = SORTING_SUBJECT[exp]
    return f"{sub}/{sub}_ses-{SORTER_TAGS[sorter]}{'-10m' if ten_min else ''}.nwb"


@lru_cache(maxsize=None)
def asset_table() -> pd.DataFrame:
    with DandiAPIClient() as client:
        ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        rows = [{"path": a.path, "size": a.size, "asset_id": a.identifier} for a in ds.get_assets()]
    return pd.DataFrame(rows).set_index("path")


def asset_url(path: str) -> str:
    aid = asset_table().loc[path, "asset_id"]
    return f"https://api.dandiarchive.org/api/assets/{aid}/download/"


def open_nwb(path: str) -> h5py.File:
    return h5py.File(remfile.File(asset_url(path)), "r")


def _decode(v):
    if v.dtype.kind in "OS":
        return np.array([x.decode() if isinstance(x, bytes) else str(x) for x in v])
    return v


def std_layer(layers) -> np.ndarray:
    m = {"1": "L1", "2": "L2/3", "3": "L2/3", "4": "L4", "5": "L5", "6": "L6",
         "L2": "L2/3", "L3": "L2/3", "L2_3": "L2/3", "WM": "Outside", "Out": "Outside"}
    return np.array([m.get(str(x), str(x)) for x in layers])


def read_units(path: str, columns=None):
    """Units table (scalar columns) and the spike trains, in seconds."""
    with open_nwb(path) as f:
        u = f["units"]
        cols = [c for c in u.attrs["colnames"] if c != "spike_times"]
        if columns is not None:
            cols = [c for c in cols if c in columns]
        df = pd.DataFrame({c: _decode(u[c][:]) for c in cols if u[c].ndim == 1})
        df.index = u["id"][:]
        st = u["spike_times"][:]
        idx = u["spike_times_index"][:].astype(np.int64)
    trains = np.split(st, idx[:-1])
    return df, trains


def read_electrodes(path: str) -> pd.DataFrame:
    with open_nwb(path) as f:
        e = f["general/extracellular_ephys/electrodes"]
        cols = [k for k in e.keys() if k not in ("group",) and e[k].ndim == 1]
        df = pd.DataFrame({c: _decode(e[c][:]) for c in cols})
    if "layers" in df:
        df["layer"] = std_layer(df["layers"])
    return df


def load_sorting(exp: str, sorter: str, ten_min: bool = True, t_max: float | None = DURATION_S):
    """A deposited sorting: table with `single` (KSLabel good for Kilosort 2 to 4, every unit for
    Kilosort and herdingspikes, claims file opening comment), `layer` and `rate` over `t_max`."""
    df, trains = read_units(sorting_path(exp, sorter, ten_min))
    if t_max is not None:
        trains = [t[t < t_max] for t in trains]
    if "KSLabel" in df:
        df["single"] = df["KSLabel"].values == "good"
    else:
        df["single"] = True
    if "layer" in df:
        df["layer"] = std_layer(df["layer"])
    dur = t_max if t_max is not None else max(t.max() for t in trains if len(t))
    df["n_spikes"] = [len(t) for t in trains]
    df["rate"] = df["n_spikes"] / dur
    return df, trains


def load_ground_truth(exp: str, t_max: float | None = DURATION_S):
    df, trains = read_units(GROUND_TRUTH[exp])
    if t_max is not None:
        trains = [t[t < t_max] for t in trains]
    if "layer" in df:
        df["layer_std"] = std_layer(df["layer"])
    df["n_spikes"] = [len(t) for t in trains]
    return df, trains


# --- agreement scores -------------------------------------------------------------------------

def _numpy_sorting(trains, ids, fs):
    from spikeinterface.core import NumpySorting
    d = {int(i): np.round(np.asarray(t) * fs).astype(np.int64) for i, t in zip(ids, trains)}
    return NumpySorting.from_unit_dict(d, sampling_frequency=fs)


def agreement_scores(gt_trains, gt_ids, s_trains, s_ids, fs) -> pd.DataFrame:
    """Agreement scores, rows sorted units, columns ground truth units (SpikeInterface
    compare_sorter_to_ground_truth, exhaustive_gt=True, delta_time 1.3 ms)."""
    from spikeinterface import comparison
    gt = _numpy_sorting(gt_trains, gt_ids, fs)
    st = _numpy_sorting(s_trains, s_ids, fs)
    comp = comparison.compare_sorter_to_ground_truth(gt, st, exhaustive_gt=True,
                                                     delta_time=DELTA_TIME_MS)
    sc = comp.agreement_scores  # rows ground truth, columns sorted
    return sc.T


def chance_scores(n_gt: np.ndarray, n_s: np.ndarray, duration: float) -> np.ndarray:
    """Chance agreement per pair (code _compute_chance_score): rows sorted, columns ground truth."""
    fr_g = np.asarray(n_gt, float) / duration
    fr_s = np.asarray(n_s, float) / duration
    lam = 2 * DELTA_TIME_MS * np.minimum(fr_s[:, None], fr_g[None, :]) / 1000.0
    p = 1.0 - np.exp(-lam)
    ng = fr_g[None, :] * duration
    ns = fr_s[:, None] * duration
    nh = p * np.minimum(ng, ns)
    denom = nh + (ng - nh) + (ns - nh)
    with np.errstate(invalid="ignore", divide="ignore"):
        return nh / denom


def qualify_units(scores: np.ndarray, chances: np.ndarray, thr_good: float = THR_GOOD):
    """Quality tags per sorted unit (rows), as the code's qualify_sorted_units, in the claims
    file's words (opening comment): false positive when every score is at or below chance;
    otherwise good when a score is 0.8 or more, merged ("overmerger") when more than one ground
    truth neuron scores above chance, partial ("oversplitter") when another sorted unit also
    scores above chance with one of the unit's above-chance neurons. Pass the scores of every
    sorted unit (rows), so that "another sorted unit" is any unit of the sorting; select the
    single units afterwards (verifier round 1, problem 5)."""
    out = []
    above = scores > chances
    for i in range(scores.shape[0]):
        g = np.where(above[i])[0]
        tags = set()
        if len(g) == 0:
            tags.add("false_positive")
        else:
            if (scores[i, g] >= thr_good).any():
                tags.add("good")
            if len(g) > 1:
                tags.add("overmerger")
            others = np.delete(above[:, g], i, axis=0)
            if others.any():
                tags.add("oversplitter")
        out.append(tags)
    return out


# --- traces -----------------------------------------------------------------------------------

def block_starts(duration_s: float = DURATION_S, n: int = N_BLOCKS, block_s: float = BLOCK_S):
    """Block onsets spread evenly over the first `duration_s` seconds (a choice made here)."""
    return np.linspace(0, duration_s - block_s, n)


def _read_block(args):
    path, start_s, block_s, fs, chans = args
    margin = int(0.05 * fs)
    with open_nwb(path) as f:
        d = f["acquisition/ElectricalSeriesRaw/data"]
        a = int(start_s * fs)
        lo = max(0, a - margin)
        hi = a + int(block_s * fs) + margin
        x = d[lo:hi, :].astype(np.float32)
    raw = x[a - lo:a - lo + int(block_s * fs)]
    sos = signal.butter(5, FREQ_MIN, btype="highpass", fs=fs, output="sos")
    y = signal.sosfiltfilt(sos, x, axis=0).astype(np.float32)
    y = y - np.median(y, axis=1, keepdims=True)
    y = y[a - lo:a - lo + int(block_s * fs)]
    raw = raw[:, chans]
    raw_c = raw - raw.mean(axis=0, keepdims=True)
    fr, p_raw = signal.welch(raw_c, fs=fs, window="hann", nperseg=int(fs), axis=0)
    return {"pre": y[:, chans], "raw_absmax": np.abs(raw).max(axis=0), "raw_psd": p_raw, "f": fr}


def trace_blocks(exp: str, chans: np.ndarray, uv_per_unit: float = 1.0, workers: int = 3):
    """Preprocessed traces (cortical sites `chans`) of the blocks, the raw maxima and the raw
    PSD averaged over blocks, all in uV."""
    path = RECORDINGS[exp]
    fs = SAMPLING_HZ[exp]
    args = [(path, s, BLOCK_S, fs, chans) for s in block_starts()]
    with ProcessPoolExecutor(workers) as ex:
        res = list(ex.map(_read_block, args))
    pre = np.concatenate([r["pre"] for r in res], axis=0) * uv_per_unit
    raw_absmax = np.max([r["raw_absmax"] for r in res], axis=0) * uv_per_unit
    raw_psd = np.mean([r["raw_psd"] for r in res], axis=0) * uv_per_unit ** 2
    return pre, raw_absmax, raw_psd, res[0]["f"]


def site_noise_mean_ad(pre: np.ndarray, fs: int) -> np.ndarray:
    """Mean absolute deviation in 1 s segments, minimum over segments (code noise.py)."""
    n = pre.shape[0] // fs
    seg = pre[: n * fs].reshape(n, fs, -1)
    mad = np.abs(seg - seg.mean(axis=1, keepdims=True)).mean(axis=1)
    return mad.min(axis=0)


def site_noise_median_ad(pre: np.ndarray) -> np.ndarray:
    med = np.median(pre, axis=0)
    return np.median(np.abs(pre - med), axis=0)


def site_psd(pre: np.ndarray, fs: int):
    """Welch PSD per site (1 Hz resolution, Hann), averaged over the blocks."""
    nb = pre.shape[0] // int(BLOCK_S * fs)
    ps = []
    for b in range(nb):
        seg = pre[b * int(BLOCK_S * fs):(b + 1) * int(BLOCK_S * fs)]
        f, p = signal.welch(seg, fs=fs, window="hann", nperseg=int(fs), axis=0)
        ps.append(p)
    return f, np.mean(ps, axis=0)


def loglog_fit(f: np.ndarray, p: np.ndarray, lo: float = 300.0, hi: float = 6000.0):
    """Slope and R2 of log10 power against log10 frequency in [lo, hi] (p: freq x sites)."""
    m = (f >= lo) & (f <= hi)
    x = np.log10(f[m])
    p = np.atleast_2d(p.T).T
    y = np.log10(p[m])
    A = np.vstack([x, np.ones_like(x)]).T
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    pred = A @ coef
    ss_res = ((y - pred) ** 2).sum(axis=0)
    ss_tot = ((y - y.mean(axis=0)) ** 2).sum(axis=0)
    return coef[0], 1 - ss_res / ss_tot


def layer_order_ok(medians: dict, max_inversions: int = 1):
    """Layer medians rising from L1 to L6 with at most `max_inversions` drops between neighbours
    (the claims file's reading of "increased with depth")."""
    vals = [medians[l] for l in LAYERS if l in medians and np.isfinite(medians[l])]
    inv = sum(1 for a, b in zip(vals[:-1], vals[1:]) if b < a)
    return inv <= max_inversions, inv


def soma_distances(gt: pd.DataFrame, elec: pd.DataFrame) -> np.ndarray:
    """Distance (um) of each soma to its nearest electrode (claims file, opening comment: the
    50 um rule is to at least one electrode)."""
    s = gt[["x", "y", "z"]].to_numpy(float)
    e = elec[["rel_x", "rel_y", "rel_z"]].to_numpy(float)
    d = np.sqrt(((s[:, None, :] - e[None, :, :]) ** 2).sum(-1))
    return d.min(axis=1)


def _block_extremes(args):
    path, start_s, block_s, fs = args
    margin = int(0.05 * fs)
    with open_nwb(path) as f:
        d = f["acquisition/ElectricalSeriesRaw/data"]
        a = int(round(start_s * fs))
        lo = max(0, a - margin)
        hi = a + int(round(block_s * fs)) + margin
        x = d[lo:hi, :].astype(np.float32)
    n = int(round(block_s * fs))
    raw = x[a - lo:a - lo + n]
    sos = signal.butter(5, FREQ_MIN, btype="highpass", fs=fs, output="sos")
    y = signal.sosfiltfilt(sos, x, axis=0).astype(np.float32)
    del x
    y = y - np.median(y, axis=1, keepdims=True)
    y = y[a - lo:a - lo + n]
    return np.abs(raw).max(axis=0), y.min(axis=0), y.max(axis=0)


def trace_extremes(exp: str, duration_s: float = DURATION_S, block_s: float = 2.5, workers: int = 8):
    """Extremes per site (all sites) over the whole first `duration_s` seconds, streamed in
    blocks of `block_s` seconds with the same preprocessing as `trace_blocks` (each block is
    filtered with 50 ms margins). Returns, per block and site, the raw maximum |trace|, and the
    minimum and maximum of the preprocessed trace, in the file's units. The block length is a
    standard choice that only bounds memory (verifier round 1 asked for 10-minute extremes)."""
    path = RECORDINGS[exp]
    fs = SAMPLING_HZ[exp]
    starts = np.arange(0, duration_s, block_s)
    args = [(path, s, min(block_s, duration_s - s), fs) for s in starts]
    with ProcessPoolExecutor(workers) as ex:
        res = list(ex.map(_block_extremes, args))
    return {"starts": starts, "raw_absmax": np.array([r[0] for r in res]),
            "pre_min": np.array([r[1] for r in res]), "pre_max": np.array([r[2] for r in res])}
