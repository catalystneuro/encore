"""Loading and measures for the evoked gastric mill data of Zenodo record 3924718.

Powell, Haddad, Gorur-Shandilya & Marder (2021), eLife 10, e60454, doi:10.7554/elife.60454.

The record holds `evoked_data.mat` (MATLAB 7.3, HDF5), the spike annotations of the ten evoked
preparations, and zip files of raw ABF recordings. `evoked_data.mat` is a 10 x 1 struct `data`
with, per preparation, the spike times of PD, LG and DG (seconds), the saline temperature and a
mask sampled at 1 kHz, and two MATLAB `categorical` arrays: `experiment_idx` (the preparation's
name) and `filename` (per 1 kHz sample, the ABF file it comes from). The categoricals are stored
as MCOS objects; `load` decodes them from the file's `#subsystem#/MCOS` cell, where each object's
category names are followed by its codes. The file is streamed into memory from the archive and
its MD5 checked; nothing is written to disk.

Where the parameters come from:

- Burst detection is crabsort.computePeriods (https://github.com/sg-s/crabsort, +crabsort/
  computePeriods.m at commit 79bf337631b16b3de141d4d4ba065170caeda578, the last change before
  the paper's code commit), called by the paper's figure scripts with ISI thresholds of 0.18 s
  (PD) and 1 s (LG, DG) and minimum counts of 2 (PD) and 5 (LG, DG) (claims file header; the
  1 s threshold and the counts are the Methods, "Detection of bursts and measurement of burst
  metrics"). computePeriods compares the count with the number of ISIs in the burst (burst end
  index minus start index), so "5" keeps bursts of at least 6 spikes. The Methods say "at least n
  spikes per burst". `bursts(..., count="spikes")` follows the Methods (the claims' main
  reading) and `count="isis"` the code (a variant).
- The temperature of an event is the temperature channel at sample round(t * 1000) (1-based in
  the code, `data.temperature(round(t*1e3))`), claims file header.
- Temperature bins are centred on 7, 9, ..., 23 C, an event belonging to a bin when its
  temperature lies within 1 C of the centre (gastric.groupAndPlotErrorBars, bin width half the
  2 C spacing; claims file header).
- The integer coupling measures follow gastric.integerCoupling and gastric.plotIntegerCoupling
  (https://github.com/marderlab/gastric at fa07d36a7e57fc7787a9a8e2fed72300b1a8e6e2), as the
  claims' criteria cite: mean PD period per LG cycle from the PD burst starts closest to the two
  LG burst starts; mean PD periods above 5 s, then above 2 s or below 0, and gastric periods
  above 30 s or below 0, removed.
- PD phase follows gastric.measurePhase: the time since the last PD burst start before the
  event over that PD burst's period, the first and last event of each preparation skipped, the
  temperature taken at the PD burst start (Methods, "Estimation of gastric mill spike and burst
  start probability in PD phase").
- The Rayleigh test is circ_rtest of the CircStat toolbox (Berens 2009), cited in the Methods.
"""

from __future__ import annotations

import hashlib
import io
import time
import zipfile

import fsspec
import h5py
import numpy as np

RECORD = "3924718"
FILE_KEY = "evoked_data.mat"
FILE_MD5 = "7b4062371133a07e373900cde8c42b15"   # from the record's file list
URL = f"https://zenodo.org/api/records/{RECORD}/files/{{key}}/content"

# The preparations in getEvokedData.m, sorted (the order of the struct in the file).
PREPS = ["901_005", "901_046", "901_049", "901_052", "901_062", "901_080", "901_086",
         "901_095", "901_098", "932_151"]

# Burst parameters (module docstring).
IBI = {"PD": 0.18, "LG": 1.0, "DG": 1.0}
MIN_N = {"PD": 2, "LG": 5, "DG": 5}

BIN_CENTRES = np.arange(7, 24, 2)
BIN_HALF_WIDTH = 1.0


def fetch(key: str = FILE_KEY, md5: str | None = FILE_MD5) -> bytes:
    """Read a file of the record whole into memory and check its MD5 against the record's list."""
    with fsspec.open(URL.format(key=key), block_size=2**20) as f:
        raw = f.read()
    if md5 is not None:
        got = hashlib.md5(raw).hexdigest()
        if got != md5:
            raise ValueError(f"MD5 of {key} is {got}, the record gives {md5}")
    return raw


def _char(f, ref) -> str:
    return "".join(map(chr, f[ref][()].ravel()))


def _cellstr(f, ref) -> list[str]:
    return [_char(f, r) for r in f[ref][()].ravel()]


def load(raw: bytes | None = None) -> list[dict]:
    """The ten preparations of evoked_data.mat, each a dict of numpy arrays.

    Keys: name, PD, LG, DG (sorted spike times, s), temperature (C, 1 kHz), mask (bool, 1 kHz,
    True where the file's mask is 1), file_codes (uint8, 1 kHz, index into file_names, 1-based),
    file_names, and the raw sizes for the data check.
    """
    if raw is None:
        raw = fetch()
    f = h5py.File(io.BytesIO(raw), "r")
    d = f["data"]
    mcos = f["#subsystem#/MCOS"]
    # MCOS cell layout (checked in the notebook's data check): cell 0 is the metadata blob, cell 1
    # empty; then for objects 1-10 (experiment_idx) pairs (category names, codes); then for
    # objects 11-20 (filename) pairs (category names, codes); then class defaults.
    n = d["PD"].shape[0]
    preps = []
    for i in range(n):
        exp_names = _cellstr(f, mcos[0, 2 + 2 * i])
        exp_code = f[mcos[0, 3 + 2 * i]][()].ravel()
        file_names = _cellstr(f, mcos[0, 22 + 2 * i])
        file_codes = f[mcos[0, 23 + 2 * i]][()].ravel().astype(np.uint8)
        obj_exp = f[d["experiment_idx"][i, 0]][()].ravel()
        obj_file = f[d["filename"][i, 0]][()].ravel()
        p = {"name": exp_names[int(exp_code[0]) - 1], "experiment_object": int(obj_exp[4]),
             "filename_object": int(obj_file[4]), "file_names": file_names, "file_codes": file_codes}
        for k in ("PD", "LG", "DG"):
            o = f[d[k][i, 0]]
            if o.attrs.get("MATLAB_empty"):
                p[k] = np.array([])
            else:
                p[k] = np.sort(o[()].ravel())
        p["temperature"] = f[d["temperature"][i, 0]][()].ravel()
        p["mask"] = f[d["mask"][i, 0]][()].ravel() == 1
        p["empty_fields"] = [k for k in ("T", "time_offset")
                             if f[d[k][i, 0]].attrs.get("MATLAB_empty")]
        preps.append(p)
    f.close()
    return preps


def temp_at(prep: dict, t) -> np.ndarray:
    """Temperature at times t (s): data.temperature(round(t*1e3)), 1-based as in the code."""
    t = np.asarray(t, dtype=float)
    out = np.full(t.shape, np.nan)
    ok = np.isfinite(t)
    idx = np.round(t[ok] * 1e3).astype(int) - 1
    idx = np.clip(idx, 0, len(prep["temperature"]) - 1)
    out[ok] = prep["temperature"][idx]
    return out


def bursts(spikes: np.ndarray, ibi: float, min_n: int, count: str = "spikes") -> dict:
    """Bursts as crabsort.computePeriods finds them.

    A burst starts at the spike after an ISI above `ibi` and ends at the spike before the next
    such ISI. `count="isis"` keeps bursts with end index - start index >= min_n, as the code does;
    `count="spikes"` keeps bursts with at least min_n spikes, as the Methods say. Periods are the
    differences of the kept burst starts, the last NaN. MATLAB's circshift makes the first spike
    a burst start when the last ISI exceeds `ibi`; this is kept.
    """
    s = np.asarray(spikes, dtype=float)
    empty = {k: np.array([]) for k in ("starts", "ends", "periods", "n")}
    if len(s) < 2:
        return empty
    isis = np.diff(s)
    gap = isis > ibi
    starts = np.flatnonzero(np.roll(gap, 1))        # 0-based index of the first spike of a burst
    ends = np.flatnonzero(gap)                       # 0-based index of the last spike
    if len(starts) == 0 or len(ends) == 0:
        return empty
    ends = ends[ends >= starts[0]]
    if len(ends) == 0:
        return empty
    starts = starts[starts <= ends[-1]]
    if len(starts) != len(ends):
        raise ValueError("unpaired burst starts and ends")
    n_isis = ends - starts
    keep = n_isis >= min_n if count == "isis" else (n_isis + 1) >= min_n
    starts, ends = starts[keep], ends[keep]
    if len(starts) == 0:
        return empty
    st, en = s[starts], s[ends]
    return {"starts": st, "ends": en, "periods": np.append(np.diff(st), np.nan), "n": n_isis[keep] + 1}


def all_bursts(preps: list[dict], count: str = "spikes", min_n: dict | None = None) -> list[dict]:
    """Bursts of PD, LG and DG for every preparation, with the module's parameters."""
    min_n = {**MIN_N, **(min_n or {})}
    return [{k: bursts(p[k], IBI[k], min_n[k], count) for k in ("PD", "LG", "DG")} for p in preps]


def in_bin(temps, centre) -> np.ndarray:
    return np.abs(np.asarray(temps) - centre) < BIN_HALF_WIDTH


def integer_coupling(prep: dict, b: dict, slow: str = "LG") -> dict:
    """gastric.integerCoupling with the filters of gastric.plotIntegerCoupling.

    For each slow burst j (but the last), the PD burst starts closest to slow start j and j+1 (the
    first of equal distances, as corelib.closest takes the minimum) give the number of PD cycles
    and the mean PD period. Returns the slow periods (y), mean PD periods (x), temperature at the
    slow burst start, and the ratio y/x and its significand, NaN where a filter removes the cycle.
    """
    ss, pd = b[slow]["starts"], b["PD"]["starts"]
    n = len(ss)
    x = np.full(n, np.nan)
    if n and len(pd):
        a = np.array([np.argmin(np.abs(pd - t)) for t in ss])
        ncyc = a[1:] - a[:-1]
        with np.errstate(invalid="ignore", divide="ignore"):
            x[:-1] = (pd[a[1:]] - pd[a[:-1]]) / ncyc
    y = b[slow]["periods"].copy() if n else np.array([])
    temp = temp_at(prep, ss)
    x = x.copy()
    with np.errstate(invalid="ignore"):
        x[x > 5] = np.nan                 # this_x(this_x>5) = NaN
        y[(y > 30) | (y < 0)] = np.nan    # all_y(all_y>30), all_y<0
        x[(x < 0) | (x > 2)] = np.nan     # all_x<0, all_x>2
        ratio = y / x
    return {"x": x, "y": y, "temp": temp, "ratio": ratio, "rem": np.mod(ratio, 1)}


def measure_phase(prep: dict, b: dict, things: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """gastric.measurePhase: PD phase of each event, and temperature at that PD burst start.

    The first and last events are skipped (NaN), as the code loops over 2:end-1.
    """
    things = np.asarray(things, dtype=float)
    phase = np.full(len(things), np.nan)
    temp = np.full(len(things), np.nan)
    st, per = b["PD"]["starts"], b["PD"]["periods"]
    if len(things) < 3 or len(st) == 0:
        return phase, temp
    idx = np.searchsorted(st, things, side="left") - 1     # last start strictly before the event
    inner = np.zeros(len(things), bool)
    inner[1:-1] = True
    ok = inner & (idx >= 0)
    phase[ok] = (things[ok] - st[idx[ok]]) / per[idx[ok]]
    temp[ok] = temp_at(prep, st[idx[ok]])
    return phase, temp


def rayleigh(phases01: np.ndarray) -> tuple[float, float]:
    """circ_rtest (Berens 2009) on phases in cycles: returns (p, z), z = R^2 / n."""
    a = np.asarray(phases01, dtype=float) * 2 * np.pi
    n = len(a)
    r = np.abs(np.mean(np.exp(1j * a)))
    R = n * r
    z = R**2 / n
    p = float(np.exp(np.sqrt(1 + 4 * n + 4 * (n**2 - R**2)) - (1 + 2 * n)))
    return p, float(z)


def circ_mean01(phases01: np.ndarray) -> float:
    """Circular mean of phases in cycles, in [0, 1) (circ_mean, then wrapped as the code does)."""
    a = np.asarray(phases01, dtype=float)
    a = a[np.isfinite(a)]
    if len(a) == 0:
        return np.nan
    m = np.angle(np.mean(np.exp(2j * np.pi * a))) / (2 * np.pi)
    return m + 1 if m < 0 else m


def ks_2samp_asymp(a: np.ndarray, b: np.ndarray) -> tuple[float, float]:
    """Two-sample Kolmogorov-Smirnov D and asymptotic p, as MATLAB's kstest2 computes them."""
    a, b = np.sort(a), np.sort(b)
    n1, n2 = len(a), len(b)
    allv = np.concatenate([a, b])
    cdf1 = np.searchsorted(a, allv, side="right") / n1
    cdf2 = np.searchsorted(b, allv, side="right") / n2
    d = float(np.max(np.abs(cdf1 - cdf2)))
    ne = n1 * n2 / (n1 + n2)
    lam = max((np.sqrt(ne) + 0.12 + 0.11 / np.sqrt(ne)) * d, 0.0)
    j = np.arange(1, 101)
    p = float(np.clip(2 * np.sum((-1) ** (j - 1) * np.exp(-2 * lam**2 * j**2)), 0, 1))
    return d, p


def integerness(rem: np.ndarray, rng: np.random.Generator, n_boot: int = 100) -> float:
    """Area between the significand c.d.f. and the diagonal, as gastric.plotIntegerCoupling.

    Mean over `n_boot` bootstrap resamples of sum(|XX - YY|) / 100, YY the c.d.f. interpolated at
    100 points on [0, 1] from the sorted resample (first of tied values, as MATLAB's unique), NaN
    outside its range left out (nansum).
    """
    rem = np.asarray(rem, dtype=float)
    n = len(rem)
    XX = np.linspace(0, 1, 100)
    Y = np.linspace(0, 1, n)
    total = 0.0
    for _ in range(n_boot):
        X = np.sort(rem[rng.integers(0, n, n)])
        ux, idx = np.unique(X, return_index=True)
        YY = np.interp(XX, ux, Y[idx], left=np.nan, right=np.nan)
        total += np.nansum(np.abs(XX - YY) / 100)
    return total / n_boot


def held_seconds(prep: dict) -> dict:
    """Seconds of recording whose temperature lies in each bin."""
    return {int(c): float(in_bin(prep["temperature"], c).sum() / 1e3) for c in BIN_CENTRES}


def q10_methods(prep: dict, b: dict, neuron: str, limit: float, bins=None) -> tuple[float, dict]:
    """Q10 as the Methods define it ("Estimation and comparison of Q10s").

    f_T is the mean burst frequency (mean of 1 / period) of the bursts starting in the bin of T,
    f_11 that of the 11 C bin, Q10 = (f_T / f_11)^(10 / (T - 11)) with T the bin centre, one Q10
    per bin other than 11 C, averaged per preparation. Periods above `limit` are removed first, as
    fig_burst_period.m does (5 s for PD, 50 s for LG). `bins` restricts the bins used.
    """
    per = b[neuron]["periods"].copy()
    per[per > limit] = np.nan
    temps = temp_at(prep, b[neuron]["starts"])
    f = 1 / per
    use = BIN_CENTRES if bins is None else [c for c in BIN_CENTRES if c in bins]
    fbin = {}
    for c in use:
        v = f[in_bin(temps, c) & np.isfinite(f)]
        if len(v):
            fbin[int(c)] = float(np.mean(v))
    if 11 not in fbin:
        return np.nan, {}
    q = {c: (fbin[c] / fbin[11]) ** (10 / (c - 11)) for c in fbin if c != 11}
    return (float(np.mean(list(q.values()))) if q else np.nan), q


def q10_code(prep: dict, b: dict, neuron: str, limit: float) -> float:
    """Q10 as fig_burst_period.m computes it: one per burst against the mean frequency of the
    bursts within 0.1 C of 11 C, at the burst's own temperature, Q10s above 10 removed, mean per
    preparation."""
    per = b[neuron]["periods"].copy()
    per[per > limit] = np.nan
    temps = temp_at(prep, b[neuron]["starts"])
    f = 1 / per
    f0 = np.nanmean(f[np.abs(temps - 11) < 0.1])
    with np.errstate(over="ignore", invalid="ignore", divide="ignore"):
        q = (f / f0) ** (10 / (temps - 11))
    q[q > 10] = np.nan
    return float(np.nanmean(q))


def stretches_after_stimulation(prep: dict, lg: dict) -> list[dict]:
    """gastric.BurstPeriodsVsTime: LG burst periods against time in each evoked stretch.

    Stimulation samples are those where the mask is 0; a stimulation ends at the last such sample
    before a gap of more than 120 s, and at the last one of the file. The stretch's temperature is
    the rounded mean over the 5 s after; it lasts until the rounded temperature changes or the next
    stimulation, and is kept when that is at least 120 s. Time runs from the first LG burst start
    after the stimulation; periods above 30 s are removed. Indices are 1-based as in the code.
    """
    temperature = np.round(prep["temperature"])
    stim = np.flatnonzero(~prep["mask"]) + 1
    if len(stim) == 0:
        return []
    ends = stim[np.append(np.diff(stim), np.inf) > 120e3]
    if ends[-1] != stim[-1]:
        ends = np.append(ends, stim[-1])
    out = []
    for s in ends:
        stim_temp = np.round(np.mean(prep["temperature"][s - 1:s + 5000]))
        later = stim[stim > s]
        if len(later):
            nxt = later[0]
            off = np.flatnonzero(temperature[s - 1:nxt] != stim_temp)
            z = off[0] + 1 + s if len(off) else nxt - 1
        else:
            # temperature(stim:[]) is empty in MATLAB, so the stretch runs to the end of the file
            z = len(temperature)
        if (z - s) * 1e-3 < 120:
            continue
        bs = lg["starts"]
        u = (bs > s * 1e-3) & (bs < z * 1e-3)
        if not u.any():
            continue
        y = lg["periods"][u].copy()
        y[y > 30] = np.nan
        out.append({"temperature": float(stim_temp), "time": bs[u] - bs[u][0], "periods": y,
                    "stim_end_s": s * 1e-3, "until_s": z * 1e-3})
    return out


def ks_shuffled(obs: np.ndarray, x: np.ndarray, y: np.ndarray, rng: np.random.Generator,
                reading: str, n_rep: int = 1000) -> np.ndarray:
    """D and p of the two-sample KS test of observed significands against shuffled ones.

    reading "draw": as plotIntegerCoupling.m, 100 gastric periods and 100 mean PD periods drawn
    independently with replacement from the bin (datasample). reading "perm": the bin's mean PD
    periods permuted against its gastric periods. Repeated `n_rep` times; returns (n_rep, 2).
    """
    res = np.empty((n_rep, 2))
    for k in range(n_rep):
        if reading == "draw":
            sh = np.mod(y[rng.integers(0, len(y), 100)] / x[rng.integers(0, len(x), 100)], 1)
        else:
            sh = np.mod(y / x[rng.permutation(len(x))], 1)
        res[k] = ks_2samp_asymp(obs, sh)
    return res


def zip_listing(key: str, tries: int = 4) -> tuple[zipfile.ZipFile, object]:
    """Open a zip of the record in place (its central directory only), retrying a server error.

    Returns the ZipFile and the open file handle, which the caller closes.
    """
    for attempt in range(tries):
        fh = fsspec.open(URL.format(key=key), block_size=2**20).open()
        try:
            return zipfile.ZipFile(fh), fh
        except Exception:
            fh.close()
            if attempt == tries - 1:
                raise
            time.sleep(10 * (attempt + 1))
