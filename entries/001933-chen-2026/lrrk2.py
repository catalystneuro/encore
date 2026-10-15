"""Loading and measures for dandiset 001933 (Chen, He et al. 2026, LRRK2 fiber photometry).

The dandiset holds one session per mouse: GRAB-DA3m fiber photometry in the dorsal striatum
during optogenetic stimulation of Anxa1+ (dorsolateral striatum) or Calb1+ (dorsomedial
striatum) SNc dopamine neurons, in LRRK2-WT and LRRK2-G2019S mice. Files are streamed from the
archive at a pinned version and reduced as they load to the 100 Hz series and the epochs table.

Where the parameters come from:

- The signal is the processed dF/F series (``FiberPhotometryResponseSeriesDfOverF``), the
  ``dff470`` trace that the paper's code (DombeckLab/lrrk2_photometry_analysis) analyses.
- Onsets: the first 100 Hz sample at or after an epoch's ``start_time``. The code takes the
  first binned TTL sample, which is what the epochs table was built from.
- Evoked integral, ``window="methods"``: the Methods' "integral of dF/F during the
  optogenetic-stimulation light-on period", from onset to the first sample at or after the
  epoch's ``stop_time``. The baseline (mean from 1.0 s to 0.1 s before onset) is the code's,
  as the Methods give none. ``window="code"``: the code's samples 91 to 200 of a chunk that
  starts 1 s before onset (0.1 s before to 1.0 s after). ``window="code_as_written"``: the
  same samples of the chunk that ``chunking_index.m`` computes as written, which starts 1 s
  after onset (``trigger - fs*ti`` with ``ti = -1``). ``window="fixed"``: 0 to 0.5 s.
  Integrals are in % dF/F times seconds (trapezoid rule, 10 ms steps); the code integrates
  in samples, 100 times larger.
- Spontaneous transients: the Methods and ``transient_by_threshold.m``. Samples from 1 s
  before to 1.5 s after every onset are removed (``exclusion="methods"``; the code as written
  removes 1 s to 3.5 s after onset, ``exclusion="code_as_written"``), the rest is
  concatenated and z-scored (sample standard deviation, as MATLAB's ``zscore``); a transient
  is a run of z > -1 that contains z > 1 (MATLAB ``imreconstruct``), runs touching either end
  are dropped as the code does, and the integral is the trapezoid integral of the unscaled
  dF/F over the run.
"""

import hashlib
import io
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import remfile
import requests
from dandi.dandiapi import DandiAPIClient
from scipy import stats

DANDISET_ID = "001933"
DANDISET_VERSION = "0.260825.1457"
FS = 100.0  # Hz, the processed series
SOURCE_DATA_URL = "https://zenodo.org/api/records/19930567/files/Source%20data.xlsx/content"
SOURCE_DATA_MD5 = "c26fe3de8f340a3db5fa29a40e5a8c10"
PAPER_POWERS = (0.1, 0.5, 1.0, 4.0)  # mW, the powers of Figure 6 and Supplementary 7 and 8

_OPHYS = "processing/ophys/FiberPhotometryResponseSeries"


def list_assets():
    client = DandiAPIClient()
    dandiset = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
    return sorted(dandiset.get_assets(), key=lambda a: a.path)


def _text(dataset):
    value = dataset[()]
    return value.decode() if isinstance(value, bytes) else str(value)


def _raw_lag(f, t, corrected, start_s=300.0, n_raw=60000, max_lag=20):
    """Lag (in 100 Hz samples) that best aligns the raw 470 nm signal, averaged into the
    processed series' bins, with the processed corrected signal, over about 37 s."""
    raw = f["acquisition/FiberPhotometryResponseSeriesRawSignal"]
    i0 = int(start_s * 2000 * 0.4)  # about 0.4 of the 2 kHz samples are kept for 470 nm
    ts = raw["timestamps"][i0:i0 + n_raw]
    rd = raw["data"][i0:i0 + n_raw]
    k0, k1 = np.searchsorted(t, ts[0]) + 5, np.searchsorted(t, ts[-1]) - 5
    edges = t[k0:k1 + 1]
    bins = np.searchsorted(edges, ts, side="right") - 1  # bin k holds [t_k, t_k+1)
    keep = (bins >= 0) & (bins < len(edges) - 1)
    sums = np.bincount(bins[keep], weights=rd[keep], minlength=len(edges) - 1)
    counts = np.bincount(bins[keep], minlength=len(edges) - 1)
    binned = sums / np.maximum(counts, 1)
    proc = corrected[k0:k1]
    m = max_lag + 5
    r = [np.corrcoef(np.roll(binned, lag)[m:-m], proc[m:-m])[0, 1] for lag in range(-max_lag, max_lag + 1)]
    return int(np.argmax(r)) - max_lag, float(r[max_lag]), float(np.diff(ts).min())


def load_session(asset):
    """Stream one file and return what the analysis uses, as a dict."""
    url = asset.get_content_url(follow_redirects=1, strip_query=True)
    with h5py.File(remfile.File(url), "r") as f:
        subject = f["general/subject"]
        s = {k: _text(subject[k]) for k in ("subject_id", "sex", "genotype", "date_of_birth", "species", "strain")}
        s["path"] = asset.path
        s["url"] = url
        s["session_start"] = _text(f["session_start_time"])
        s["session_description"] = _text(f["session_description"])
        s["mouse"] = int(s["subject_id"].split("-")[0])
        s["line"] = "Anxa1" if "-anxa-" in s["subject_id"] else "Calb1"
        s["group"] = "GS" if s["genotype"].endswith("G2019S") else "WT"
        dff = f[_OPHYS + "DfOverF"]
        s["t"] = dff["timestamps"][:]
        s["dff"] = dff["data"][:]
        s["dff_unit"] = dff["data"].attrs["unit"]
        s["dff_description"] = dff.attrs["description"]
        s["dff405"] = f[_OPHYS + "DfOverFIsosbesticControl"]["data"][:]
        corrected = f[_OPHYS + "CorrectedSignal"]["data"][:]
        s["dff_recomputed"] = _dff_from_corrected(corrected)
        s["location"] = [_text_v(v) for v in f["general/fiber_photometry/fiber_photometry_table/location"][:]]
        s["dff_region"] = int(dff["fiber_photometry_table_region"][0])
        ot = f["intervals/OptogeneticEpochsTable"]
        s["opto_description"] = ot.attrs["description"]
        for col in ("start_time", "stop_time", "power_in_mW", "pulse_length_in_ms", "period_in_ms",
                    "number_pulses_per_pulse_train", "wavelength_in_nm"):
            s[col] = ot[col][:]
        s["onset"] = np.searchsorted(s["t"], s["start_time"])
        s["offset"] = np.searchsorted(s["t"], s["stop_time"])
        s["raw_lag"], s["raw_r"], s["raw_min_dt"] = _raw_lag(f, s["t"], corrected)
        s["raw_n"] = f["acquisition/FiberPhotometryResponseSeriesRawSignal/data"].shape[0]
        s["md5"] = hashlib.md5(s["dff"].tobytes()).hexdigest()
    return s


def _text_v(v):
    return v.decode() if isinstance(v, bytes) else str(v)


def _movmean(x, k=20):
    """MATLAB smoothdata(x, 'movmean', k) for even k: window [i - k/2, i + k/2 - 1], shrunk at edges."""
    c = np.concatenate([[0.0], np.cumsum(x)])
    i = np.arange(len(x))
    lo = np.clip(i - k // 2, 0, len(x))
    hi = np.clip(i + k // 2, 0, len(x))
    return (c[hi] - c[lo]) / (hi - lo)


def _dff_from_corrected(corrected):
    """The code's df_f (F0 = 8th percentile of the corrected trace, in %) and 20-sample movmean."""
    base = np.percentile(corrected, 8)
    return _movmean((corrected - base) / base * 100.0)


def load_all(workers=6):
    assets = list_assets()
    with ThreadPoolExecutor(workers) as pool:
        return list(pool.map(load_session, assets))


def evoked_integrals(s, window="methods", trace="dff"):
    """One integral per epoch (in table order), in % dF/F times seconds; NaN where the
    window leaves the recording. Only the samples the window and its baseline use must be
    recorded."""
    if window not in ("methods", "code", "code_as_written", "fixed"):
        raise ValueError(window)
    x = s[trace]
    out = np.full(len(s["onset"]), np.nan)
    for j, (on, off) in enumerate(zip(s["onset"], s["offset"])):
        start = on - 100 if window != "code_as_written" else on + 100
        a, b = {"code": (start + 90, start + 200), "code_as_written": (start + 90, start + 200),
                "methods": (on, off + 1), "fixed": (on, on + 51)}[window]
        if start < 0 or b > len(x):
            continue
        base = x[start:start + 90].mean()
        out[j] = np.trapezoid(x[a:b] - base) / FS
    return out


def code_chunk(s, j):
    """The 250-sample trace the code's intended chunk holds for epoch j (1 s before onset to 1.5 s after)."""
    on = s["onset"][j]
    out = np.full(250, np.nan)
    seg = s["dff"][max(on - 100, 0):on + 150]
    out[max(100 - on, 0):max(100 - on, 0) + len(seg)] = seg
    return out


def double_threshold(z, low=-1.0, high=1.0):
    """Runs of z > low that contain z > high, as (start, stop) inclusive index pairs.
    Runs that touch either end of the trace are dropped, as transient_by_threshold.m does."""
    above = z > low
    edges = np.diff(above.astype(int))
    starts = np.where(edges == 1)[0] + 1
    stops = np.where(edges == -1)[0]
    stops = stops[stops >= (starts[0] if len(starts) else len(z))]
    starts = starts[starts <= (stops[-1] if len(stops) else -1)]
    runs = [(a, b) for a, b in zip(starts, stops) if (z[a:b + 1] > high).any()]
    return runs


def spontaneous_trace(s, exclusion="methods"):
    x = s["dff"]
    drop = np.zeros(len(x), bool)
    for on in s["onset"]:
        a, b = (on - 100, on + 150) if exclusion == "methods" else (on + 100, on + 350)
        drop[max(a, 0):min(b, len(x))] = True
    kept = x[~drop]
    return kept[~np.isnan(kept)]


def spontaneous_transients(s, exclusion="methods"):
    """Integrals (% dF/F times seconds), peaks and means (% dF/F) of the spontaneous transients,
    in time order."""
    x = spontaneous_trace(s, exclusion)
    z = (x - x.mean()) / x.std(ddof=1)
    runs = double_threshold(z)
    auc = np.array([np.trapezoid(x[a:b + 1]) / FS for a, b in runs])
    peaks = np.array([x[a:b + 1].max() for a, b in runs])
    means = np.array([x[a:b + 1].mean() for a, b in runs])
    return auc, peaks, means


def raw_binned(s):
    """The raw 470 nm samples averaged into the processed series' 100 Hz bins, as the code's
    calib_binning_to_cam does: the 20 samples of 2 kHz from each camera trigger, here the
    processed timestamps, keeping the samples the demultiplexing retained."""
    with h5py.File(remfile.File(s["url"]), "r") as f:
        raw = f["acquisition/FiberPhotometryResponseSeriesRawSignal"]
        ts, d = raw["timestamps"][:], raw["data"][:].astype(float)
    lo, hi = np.searchsorted(ts, s["t"] - 0.25 / 2000), np.searchsorted(ts, s["t"] + 19.5 / 2000)
    c = np.concatenate([[0.0], np.cumsum(d)])
    return (c[hi] - c[lo]) / np.maximum(hi - lo, 1)


def _rolling_prctile(v, p=8, win=2001):
    """MATLAB prctile (midpoint positions) over a centred window; edges are not exact."""
    import pandas as pd

    q = (p / 100 * win - 0.5) / (win - 1)
    return pd.Series(v).rolling(win, center=True, min_periods=1).quantile(q).values


def dff_from_raw(binned, background=0.85):
    """The code's baselineCorrect (subtract ``background`` times the sliding 8th percentile,
    divide by a new sliding 8th percentile), df_f and 20-sample moving mean. The code uses
    0.85 of the baseline as background."""
    x = binned - background * _rolling_prctile(binned)
    corrected = x / _rolling_prctile(x)
    base = np.percentile(corrected, 8, method="hazen")
    return _movmean((corrected - base) / base * 100.0)


def one_tailed_less(a, b, equal_var=True):
    """t-test of a < b; returns t and the one-tailed p."""
    r = stats.ttest_ind(a, b, equal_var=equal_var, alternative="less")
    return float(r.statistic), float(r.pvalue)


def two_tailed(a, b, equal_var=True):
    r = stats.ttest_ind(a, b, equal_var=equal_var)
    return float(r.statistic), float(r.pvalue)


def cohens_d(wt, gs):
    """(mean WT - mean GS) / pooled standard deviation."""
    n1, n2 = len(wt), len(gs)
    sp = np.sqrt(((n1 - 1) * np.var(wt, ddof=1) + (n2 - 1) * np.var(gs, ddof=1)) / (n1 + n2 - 2))
    return float((np.mean(wt) - np.mean(gs)) / sp)


def load_source_data():
    """The paper's source data file (Zenodo 10.5281/zenodo.19930567), read in memory.

    Returns the md5 of the file and a dict of tables: triggered traces (6C, S7B, S8D), evoked
    integrals (6E, S7C, S8E) and spontaneous transient integrals (6F, S8C)."""
    import openpyxl

    content = requests.get(SOURCE_DATA_URL, timeout=300).content
    md5 = hashlib.md5(content).hexdigest()
    wb = openpyxl.load_workbook(io.BytesIO(content), read_only=True)

    def rows(name):
        return list(wb[name].iter_rows(values_only=True))

    def traces(rs, c0, first):
        out = []
        for r in rs[first:]:
            if len(r) > c0 and isinstance(r[c0], (int, float)):
                out.append(dict(mouse=int(r[c0]), group=r[c0 + 1], power=float(r[c0 + 2]),
                                trace=np.array(r[c0 + 3:c0 + 253], float)))
        return out

    def values(rs, c0, first, with_power):
        out = []
        for r in rs[first:]:
            if len(r) > c0 and isinstance(r[c0], (int, float)):
                d = dict(mouse=int(r[c0]), group=r[c0 + 1])
                if with_power:
                    d["power"] = float(r[c0 + 2])
                d["value"] = float(r[c0 + 3] if with_power else r[c0 + 2])
                out.append(d)
        return out

    f6cd, f6ef = rows("Fig. 6c-d"), rows("Fig. 6e-f")
    s7, s8 = rows("Suppl. Fig. 7b-c"), rows("Suppl. Fig. 8b-e")
    tables = {
        "6C": traces(f6cd, 0, 2),
        "6E": [dict(d, power=0.5) for d in values(f6ef, 4, 2, False)],
        "6F": values(f6ef, 8, 2, False),
        "S7B": traces(s7, 1, 1),
        "S7C": values(s7, 506, 1, True),
        "S8C": values(s8, 7, 1, False),
        "S8D": traces(s8, 12, 1),
        "S8E": values(s8, 517, 1, True),
    }
    return md5, tables
