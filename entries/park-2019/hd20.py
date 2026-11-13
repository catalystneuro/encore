"""Loading and measures for CRCNS hc-20, MEC head-direction cells on a stable and rotating arena.

Park, Keeley, Savin, Ranck & Fenton (2019), Neuron 101:285-293, doi:10.1016/j.neuron.2018.11.019.
Data set: CRCNS hc-20 (doi:10.6080/K0SF2TDN), file hc-20/live/data.zip, streamed from the public
S3 bucket crcnsarchive and opened in place with fsspec and zipfile; nothing is written to disk.

The zip holds, under data/TSD/, one TSD file per unit and trial in SA1 (stable1), SA2 (stable2),
RA_rm (rotating, room coordinates) and RA_ar (rotating, arena coordinates), with
FileNameList.xlsx giving one unit per row across the four, and under data/DAT/ the tracker's
ASCII files of each trial (room and arena tracks for the rotating trial). The TSD format is in
the data descriptor: an ASCII header, then per 30 Hz tracker sample x (1 byte), y (1 byte),
direction (4 bytes, degrees), the number of spikes (1 byte) and their times (4 bytes each, in
100 us units). A direction above 360 marks an untracked sample (HD_Max_likelihood.py drops them).

Where the parameters come from:

- 10 degree direction bins and rate = spikes over time in each bin: STAR Methods, Data Analysis
  ("Azimuthal directional tuning curves (10 deg resolution) ... dividing the total number of
  action potentials ... by the total time").
- Preferred direction (bin of maximum rate), directionality (Rayleigh vector length of the
  tuning curve) and KLD (resistor average of the two Kullback-Leibler divergences of the
  Krichevsky-Trofimov probabilities): STAR Methods, Quantifying Head-direction Signals. The
  natural logarithm is used; the base does not change any test (claims file).
- The decoder (`decode`) ports HD_Max_likelihood.py of
  https://github.com/FentonLab/PyCode_MEC_HDC-NeuronMS_Park at commit 545a738a: windows of 20
  tracker samples, the window direction the circular mean of its tracked samples, 36 bins, a
  Poisson rate per cell and bin (spikes in windows at the bin over the number of such windows),
  the summed log likelihood maximised, windows without spikes left undecoded.
- Internally referenced tuning (`internal_tuning`) ports Spike_triggered_FR_curve.py of the same
  commit: for each tracker sample with a cell 1 spike, the cell 1 direction minus the direction
  at each cell 2 spike sample in the window of `T` seconds that ends at the cell 1 spike, in 36
  bins from -180 degrees; the occupancy normalisation divides by the same differences over all
  tracked samples of the window. Each sample with spikes counts once, as in the code.
- Idir (`idir`): STAR Methods, Estimating momentary directional information, 133 ms intervals
  (4 tracker samples); the direction bins and the source of the probabilities are open and are
  arguments.
- Kendall correlations of spike counts in 40, 250 and 1000 ms bins: STAR Methods, Stability of
  a correlated network state.
- Rayleigh test p-value: the standard approximation of Zar (Biostatistical Analysis), a standard
  choice. Dunnett's test: scipy's, whose p-values come from a randomised integration, seeded (a
  standard choice that cannot change a result beyond the fourth decimal). Kuiper's two-sample test: the asymptotic distribution with Stephens' correction
  (Numerical Recipes, which the paper cites), a standard choice.
"""

from __future__ import annotations

import io
import re
import zipfile
from functools import lru_cache

import fsspec
import numpy as np
import pandas as pd

BUCKET = "https://crcnsarchive.s3-us-west-2.amazonaws.com/hc-20/live"
DATASET = "CRCNS hc-20"
DATASET_VERSION = "unversioned"   # CRCNS data sets are not versioned (docs/archives.md)
DATA_ZIP_MD5 = "b82c7b97b0ba3491f04ecc4dbcd48e83"   # checksums.md5 of hc-20/live, read 2026-11-13
TRIALS = ["SA1", "RA_rm", "RA_ar", "SA2"]
TRIAL_NAMES = {"SA1": "stable1", "RA_rm": "rotating room", "RA_ar": "rotating arena", "SA2": "stable2"}
NBINS = 36
BIN_DEG = 10.0
CENTRES = np.deg2rad(np.arange(NBINS) * BIN_DEG + BIN_DEG / 2)


def checksums() -> dict:
    """The data set's checksums.md5, as published."""
    with fsspec.open(f"{BUCKET}/checksums.md5", "rt") as f:
        return {line.split()[1]: line.split()[0] for line in f if line.strip()}


@lru_cache(maxsize=1)
def open_zip() -> zipfile.ZipFile:
    f = fsspec.open(f"{BUCKET}/data.zip", block_size=2**22).open()
    return zipfile.ZipFile(f)


def parse_tsd(raw: bytes) -> dict:
    """Parse one TSD file into per-sample arrays and spike times (100 us units)."""
    end = raw.index(b"%%ENDHEADER")
    header = raw[:end].decode("latin1")
    pos = raw.index(b"\n", end) + 1
    fs = float(re.search(r"SAMPLING_INTERVAL\(samps/sec\)\s+([\d.]+)", header).group(1))
    first = float(re.search(r"FIRST_TIMESTAMP\(100usUnits\)\s+([\d.]+)", header).group(1))
    n_max = (len(raw) - pos) // 7
    x = np.empty(n_max, np.uint8)
    y = np.empty(n_max, np.uint8)
    d = np.empty(n_max, np.uint32)
    ns = np.empty(n_max, np.uint8)
    starts = np.empty(n_max, np.int64)
    k = 0
    L = len(raw)
    while pos + 7 <= L:
        n = raw[pos + 6]
        starts[k] = pos
        ns[k] = n
        pos += 7 + 4 * n
        k += 1
    starts = starts[:k]
    ns = ns[:k].astype(np.int64)
    buf = np.frombuffer(raw, np.uint8)
    x = buf[starts].copy()
    y = buf[starts + 1].copy()
    d = (buf[starts + 2].astype(np.uint32) | (buf[starts + 3].astype(np.uint32) << 8)
         | (buf[starts + 4].astype(np.uint32) << 16) | (buf[starts + 5].astype(np.uint32) << 24))
    nsp = int(ns.sum())
    spk_sample = np.repeat(np.arange(k), ns)
    # offset of spike j within its sample
    first_idx = np.repeat(np.cumsum(ns) - ns, ns)
    within = np.arange(nsp) - first_idx
    off = np.repeat(starts + 7, ns) + 4 * within
    t = (buf[off].astype(np.uint32) | (buf[off + 1].astype(np.uint32) << 8)
         | (buf[off + 2].astype(np.uint32) << 16) | (buf[off + 3].astype(np.uint32) << 24))
    return {"fs": fs, "first_ts": first, "x": x, "y": y, "d": d, "n": ns,
            "spike_sample": spk_sample, "spike_t": t.astype(np.int64), "trailing": L - pos}


def file_list() -> pd.DataFrame:
    """FileNameList.xlsx, Sheet1: one unit per row, its file in each of the four trial folders."""
    z = open_zip()
    x = pd.read_excel(io.BytesIO(z.read("data/TSD/FileNameList.xlsx")), sheet_name="Sheet1", header=None)
    x = x.iloc[1:].reset_index(drop=True)
    x.columns = ["SA1", "RA_rm", "RA_ar", "SA2"]
    return x.astype(str).apply(lambda c: c.str.strip())


def unit_key(name: str) -> dict:
    m = re.match(r"(\d{4})(SA1|SA2|RA|TF|RA)R?(\d+)-(R?cl\d?)\.P(\d+)C(\d+)(Rm|Ar)", name)
    return m


def file_key(name: str) -> tuple:
    """(date, rat, tetrode, cluster) of a TSD file name."""
    m = re.search(r"^(\d{4}).*?R(\d{3}).*\.P(\d+)C(\d+)", name)
    return m.groups()


def load_units() -> tuple[pd.DataFrame, dict]:
    """Parse the four TSD files of every unit in FileNameList.xlsx.

    Units are named by the SA1 file of each row. The other three files are those of the same row
    when their date, rat, tetrode and cluster agree with the SA1 file, and otherwise the file of
    the same column whose name agrees (the SA2 column of session 1121R157 is shifted by one row;
    see the data check). A header whose sampling rate is implausible (above 100 samples/s; one
    file states 2000) is given the rate of the other files of the same session and trial.
    Returns the unit table and a dict unit -> trial -> parsed file."""
    z = open_zip()
    members = set(z.namelist())
    fl = file_list()
    by_key = {tr: {file_key(n): n for n in fl[tr]} for tr in TRIALS}
    units, data = [], {}
    for i, r in fl.iterrows():
        key = file_key(r["SA1"])
        uid = f"{key[0]}R{key[1]}-P{key[2]}C{key[3]}"
        data[uid] = {}
        row = {"unit": uid, "session": f"{key[0]}R{key[1]}", "rat": f"R{key[1]}", "row": i}
        for tr in TRIALS:
            name = r[tr] if file_key(r[tr]) == key else by_key[tr][key]
            row[f"file_{tr}"] = name
            row[f"listed_{tr}"] = r[tr]
            path = f"data/TSD/{tr}/{name}"
            if path not in members:
                raise FileNotFoundError(path)
            data[uid][tr] = parse_tsd(z.read(path))
            data[uid][tr]["fs_header"] = data[uid][tr]["fs"]
        units.append(row)
    units = pd.DataFrame(units)
    for s, g in units.groupby("session"):
        for tr in TRIALS:
            rates = [data[u][tr]["fs"] for u in g.unit if data[u][tr]["fs"] <= 100]
            for u in g.unit:
                if data[u][tr]["fs"] > 100:
                    data[u][tr]["fs"] = float(np.median(rates)) if rates else 30.0219
    return units, data


def parse_dat(raw: bytes) -> tuple[dict, pd.DataFrame]:
    """Parse a Tracker .dat file: header fields of interest and the sample table."""
    text = raw.decode("latin1")
    head, body = text.split("%%END_HEADER", 1)
    info = {}
    for key in ["Frame", "ReinforcedSector", "RoomTrackReinforcedSector", "ArenaTrackReinforcedSector",
                "ArenaCenterXY", "TrackerResolution_PixPerCM", "ArenaDiameter_m", "ElapsedTime_ms",
                "Paradigm", "ShockParameters"]:
        m = re.search(r"%" + key + r"\.0 \(\s*(.*?)\s*\)", head)
        info[key] = m.group(1) if m else None
    names = re.search(r"%Sample\.0 \(\s*(.*?)\s*\)", head).group(1).split()
    info["columns"] = names
    df = pd.read_csv(io.StringIO(body), sep=r"\s+", header=None, names=names, na_values=["*"])
    df = df.rename(columns={"FrameCount": "frame", "1msTimeStamp": "t_ms", "RoomX": "x", "RoomY": "y",
                            "ArenaX": "x", "ArenaY": "y", "Sectors": "sectors", "State": "state",
                            "Angle": "angle"})
    return info, df


def dat_files() -> pd.DataFrame:
    """The .dat files in the zip, with session (date and rat), trial and frame."""
    rows = []
    for n in open_zip().namelist():
        if not n.endswith(".dat"):
            continue
        base = n.split("/")[-1]
        m = re.match(r"(\d{4})(SA1|SA2|RA|TF)R?(\d{2,3})(RoomTrack|ArenaTrack)", base)
        trial = {"SA1": "SA1", "SA2": "SA2", "RA": "RA", "TF": "RA"}[m.group(2)]
        rows.append({"path": n, "session": f"{m.group(1)}R{int(m.group(3)):03d}", "trial": trial,
                     "frame": "room" if m.group(4) == "RoomTrack" else "arena"})
    return pd.DataFrame(rows)


# ---------------------------------------------------------------- tuning measures

def valid(tr: dict) -> np.ndarray:
    return tr["d"] <= 360


def tuning(tr: dict, sl: slice | None = None) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """10 degree tuning curve: spikes, time (s) and rate per bin, tracked samples only."""
    d, n = tr["d"], tr["n"].astype(float)
    if sl is not None:
        d, n = d[sl], n[sl]
    ok = d <= 360
    b = (d[ok] % 360) // 10
    spikes = np.bincount(b, weights=n[ok], minlength=NBINS)
    time = np.bincount(b, minlength=NBINS) / tr["fs"]
    with np.errstate(invalid="ignore", divide="ignore"):
        rate = np.where(time > 0, spikes / time, 0.0)
    return spikes, time, rate


def resultant(weights: np.ndarray, angles: np.ndarray = CENTRES) -> tuple[float, float]:
    """Length and angle of the mean resultant vector of weighted angles."""
    w = np.asarray(weights, float)
    if w.sum() <= 0:
        return np.nan, np.nan
    c = (w * np.exp(1j * angles)).sum() / w.sum()
    return float(abs(c)), float(np.angle(c))


def rayleigh_p(r: float, n: float) -> float:
    """Rayleigh test p-value, Zar's approximation."""
    if not n or np.isnan(r):
        return np.nan
    z = n * r * r
    p = np.exp(np.sqrt(1 + 4 * n + 4 * (n * n - (r * n) ** 2)) - (1 + 2 * n))
    return float(min(max(p, 0.0), 1.0))


def kuiper_two_sample(a: np.ndarray, b: np.ndarray) -> tuple[float, float]:
    """Kuiper's two-sample test on circular data (degrees), asymptotic p with Stephens' correction."""
    a = np.sort(np.asarray(a, float) % 360)
    b = np.sort(np.asarray(b, float) % 360)
    allv = np.concatenate([a, b])
    fa = np.searchsorted(a, allv, side="right") / len(a)
    fb = np.searchsorted(b, allv, side="right") / len(b)
    v = (fa - fb).max() + (fb - fa).max()
    ne = len(a) * len(b) / (len(a) + len(b))
    lam = (np.sqrt(ne) + 0.155 + 0.24 / np.sqrt(ne)) * v
    if lam < 0.4:
        return float(v), 1.0
    j = np.arange(1, 101)
    p = 2 * np.sum((4 * j**2 * lam**2 - 1) * np.exp(-2 * j**2 * lam**2))
    return float(v), float(min(max(p, 0.0), 1.0))


def kuiper_binned(w1: np.ndarray, w2: np.ndarray, n1: float, n2: float) -> tuple[float, float]:
    """Kuiper's two-sample test on two weighted distributions over the same direction bins.

    V is the Kuiper statistic of the two cumulative distributions over the bins, and n1, n2 the
    sample sizes behind them, with the asymptotic p of `kuiper_two_sample`. Used for reading (i) of
    fig5-error-inhomogeneous, where the error distribution is a set of weights over head-direction
    bins; the paper does not say how it applied Kuiper's test, so this is an assumption.
    """
    f1 = np.cumsum(w1) / np.sum(w1)
    f2 = np.cumsum(w2) / np.sum(w2)
    v = (f1 - f2).max() + (f2 - f1).max()
    ne = n1 * n2 / (n1 + n2)
    lam = (np.sqrt(ne) + 0.155 + 0.24 / np.sqrt(ne)) * v
    if lam < 0.4:
        return float(v), 1.0
    j = np.arange(1, 101)
    p = 2 * np.sum((4 * j**2 * lam**2 - 1) * np.exp(-2 * j**2 * lam**2))
    return float(v), float(min(max(p, 0.0), 1.0))


def preferred(rate: np.ndarray) -> float:
    """Preferred direction, degrees: the centre of the bin of maximum rate."""
    return float(np.argmax(rate) * BIN_DEG + BIN_DEG / 2)


def circ_absdiff(a, b):
    """Absolute circular difference in degrees, 0 to 180."""
    d = (np.asarray(a, float) - np.asarray(b, float)) % 360
    return np.minimum(d, 360 - d)


def kld(p_counts: np.ndarray, q_counts: np.ndarray) -> float:
    """Resistor-average KLD of two curves after the Krichevsky-Trofimov estimate."""
    p = np.asarray(p_counts, float)
    q = np.asarray(q_counts, float)
    P = (p + 0.5) / (p.sum() + 0.5 * len(p))
    Q = (q + 0.5) / (q.sum() + 0.5 * len(q))
    d12 = float(np.sum(P * np.log(P / Q)))
    d21 = float(np.sum(Q * np.log(Q / P)))
    if d12 + d21 == 0:
        return 0.0
    return d12 * d21 / (d12 + d21)


# ---------------------------------------------------------------- decoding

def window_directions(d: np.ndarray, w: int) -> np.ndarray:
    """Circular mean direction (degrees, 0-360) of the tracked samples in each window of w samples;
    NaN where no sample in the window is tracked."""
    nwin = len(d) // w
    dd = d[: nwin * w].astype(float).reshape(nwin, w)
    ok = dd <= 360
    z = np.where(ok, np.exp(1j * np.deg2rad(dd)), 0).sum(1)
    ang = np.rad2deg(np.angle(z)) % 360
    ang[~ok.any(1)] = np.nan
    return ang


def window_counts(n: np.ndarray, w: int) -> np.ndarray:
    nwin = len(n) // w
    return n[: nwin * w].astype(float).reshape(nwin, w).sum(1)


def fit_decoder(train_dirs: np.ndarray, train_counts: np.ndarray) -> np.ndarray:
    """Poisson rate per cell and 10 degree bin (spikes per window), as HD_Max_likelihood.py.

    train_dirs: (windows,), train_counts: (cells, windows). Windows with no tracked sample are
    dropped (the code would place them in bin 0)."""
    ok = ~np.isnan(train_dirs)
    b = (train_dirs[ok] // 10).astype(int) % NBINS
    occ = np.bincount(b, minlength=NBINS).astype(float)
    lam = np.stack([np.bincount(b, weights=c[ok], minlength=NBINS) for c in train_counts])
    with np.errstate(invalid="ignore", divide="ignore"):
        lam = lam / occ
    return lam


def decode(lam: np.ndarray, counts: np.ndarray) -> np.ndarray:
    """Maximum likelihood direction (degrees, bin start as in the code's `angs`) per window; NaN
    where no cell spiked. Poisson log likelihood; a bin with rate 0 and a spike gets -10 as in
    the code."""
    from scipy.special import gammaln
    lam = np.where(np.isnan(lam), 0.0, lam)
    out = np.full(counts.shape[1], np.nan)
    any_spk = counts.sum(0) > 0
    c = counts[:, any_spk]                     # cells x windows
    with np.errstate(divide="ignore"):
        loglam = np.where(lam > 0, np.log(np.where(lam > 0, lam, 1.0)), 0.0)
    ll = np.zeros((NBINS, c.shape[1]))
    for i in range(lam.shape[0]):
        term = c[i][None, :] * loglam[i][:, None] - lam[i][:, None] - gammaln(c[i] + 1)[None, :]
        # rate 0: probability 1 of no spike (log 0) and 0 of any spike, scored -10 as in the code
        zero = (lam[i][:, None] == 0) & (c[i][None, :] > 0)
        term = np.where(zero | (np.exp(term) == 0), -10.0, term)
        ll += term
    out[any_spk] = np.argmax(ll, axis=0) * BIN_DEG
    return out


def signed_error(decoded, actual):
    """Decoded minus actual direction, wrapped to [-180, 180)."""
    return (np.asarray(decoded) - np.asarray(actual) + 180) % 360 - 180


# ---------------------------------------------------------------- Idir

def idir(counts: np.ndarray, dirs: np.ndarray, ref_counts: np.ndarray, ref_dirs: np.ndarray,
         bin_deg: float) -> np.ndarray:
    """Idir = |p(n|d) log2(p(n|d)/p(n))| per interval, for one cell.

    counts, dirs: the cell's spike count and direction in each 133 ms interval of the trial
    analysed; the probabilities p(n|d) and p(n) are estimated from ref_counts, ref_dirs (the same
    trial, or stable1). Intervals with no tracked direction, or whose (n, d) never occurs in the
    reference, are NaN."""
    nb = int(round(360 / bin_deg))
    ok_r = ~np.isnan(ref_dirs)
    rb = (ref_dirs[ok_r] // bin_deg).astype(int) % nb
    rc = np.minimum(ref_counts[ok_r].astype(int), 50)
    nmax = 51
    joint = np.zeros((nb, nmax))
    np.add.at(joint, (rb, rc), 1)
    p_n = joint.sum(0) / joint.sum()
    with np.errstate(invalid="ignore", divide="ignore"):
        p_nd = joint / joint.sum(1, keepdims=True)
    out = np.full(len(counts), np.nan)
    ok = ~np.isnan(dirs)
    b = (dirs[ok] // bin_deg).astype(int) % nb
    c = np.minimum(counts[ok].astype(int), 50)
    pnd = p_nd[b, c]
    pn = p_n[c]
    with np.errstate(invalid="ignore", divide="ignore"):
        v = np.abs(pnd * np.log2(pnd / pn))
    v[(pnd == 0) | (pn == 0) | np.isnan(pnd)] = np.nan
    out[ok] = v
    return out


# ---------------------------------------------------------------- internally referenced tuning

def _cum_onehot(deg: np.ndarray, weights: np.ndarray) -> np.ndarray:
    """Cumulative (over samples) histogram of integer directions 0-359, shape (n+1, 360)."""
    n = len(deg)
    oh = np.zeros((n + 1, 360), np.int32)
    idx = np.nonzero(weights)[0]
    oh[idx + 1, deg[idx] % 360] = weights[idx]
    return np.cumsum(oh, axis=0, out=oh)


def internal_tuning(d: np.ndarray, spk1: np.ndarray, spk2: np.ndarray, fs: float,
                    windows_s, side: str = "before") -> dict:
    """Internally referenced tuning of cell 2 to the direction change since cell 1 spikes.

    d: per-sample direction (degrees; > 360 untracked); spk1, spk2: per-sample spike counts.
    For each tracked sample with a cell 1 spike (counted once, as in Spike_triggered_FR_curve.py)
    the cell 1 direction minus the direction at each tracked cell 2 spike sample in the window
    of T s ending at (side 'before', the code) or starting at (side 'after') the cell 1 spike.
    Returns, per window length T, the spike-difference histogram ('counts', 36 bins from -180)
    and the occupancy histogram over all tracked samples of the windows ('occ')."""
    ok = d <= 360
    deg = (d.astype(np.int64) % 360)
    w2 = ((spk2 > 0) & ok).astype(np.int32)
    wall = ok.astype(np.int32)
    C2 = _cum_onehot(deg, w2)
    CA = _cum_onehot(deg, wall)
    trig = np.nonzero((spk1 > 0) & ok)[0]
    n = len(d)
    out = {}
    # bin of (a - b) for a = trigger degree, b = 0..359: floor(36 * (diff + 180) / 360)
    for T in windows_s:
        m = int(round(T * fs))
        if side == "before":
            lo, hi = np.maximum(trig - m, 0), trig          # samples [lo, hi)
        else:
            lo, hi = trig + 1, np.minimum(trig + 1 + m, n)
        # h[k] = sum over triggers of the window's count at direction b = (a - k) mod 360,
        # i.e. the count at difference k = (a - b) mod 360
        idx = (deg[trig][:, None] - np.arange(360)[None, :]) % 360
        h2 = np.zeros(360, np.int64)
        ha = np.zeros(360, np.int64)
        for s in range(0, len(trig), 2000):
            sl = slice(s, s + 2000)
            h2 += np.take_along_axis(C2[hi[sl]] - C2[lo[sl]], idx[sl], 1).sum(0)
            ha += np.take_along_axis(CA[hi[sl]] - CA[lo[sl]], idx[sl], 1).sum(0)
        diffs = (np.arange(360) + 180) % 360 - 180
        bins = np.floor(36 * (diffs + 180) / 360).astype(int)
        out[T] = {"counts": np.bincount(bins, weights=h2, minlength=36),
                  "occ": np.bincount(bins, weights=ha, minlength=36)}
    return out


# ---------------------------------------------------------------- statistics

def rm_anova(wide: pd.DataFrame) -> dict:
    """One-way repeated-measures ANOVA (rows subjects, columns conditions), with Mauchly's test
    and the Greenhouse-Geisser correction applied when Mauchly's test has p < 0.05 (STAR
    Methods, Statistics). Rows with a missing value are dropped."""
    from scipy import stats
    X = wide.dropna().to_numpy(float)
    n, k = X.shape
    gm = X.mean()
    ss_cond = n * ((X.mean(0) - gm) ** 2).sum()
    ss_subj = k * ((X.mean(1) - gm) ** 2).sum()
    ss_err = ((X - gm) ** 2).sum() - ss_cond - ss_subj
    df1, df2 = k - 1, (k - 1) * (n - 1)
    F = (ss_cond / df1) / (ss_err / df2)
    S = np.cov(X, rowvar=False)
    # orthonormal contrasts
    C = np.linalg.qr(np.vstack([np.ones(k), np.eye(k)[:-1]]).T)[0][:, 1:]
    M = C.T @ S @ C
    eps = np.trace(M) ** 2 / ((k - 1) * np.trace(M @ M))
    if k > 2:
        W = np.linalg.det(M) / (np.trace(M) / (k - 1)) ** (k - 1)
        f = 1 - (2 * (k - 1) ** 2 + (k - 1) + 2) / (6 * (k - 1) * (n - 1))
        chi2 = -(n - 1) * f * np.log(W)
        dfm = k * (k - 1) / 2 - 1
        p_mauchly = float(stats.chi2.sf(chi2, dfm))
    else:
        W, p_mauchly = 1.0, 1.0
    gg = p_mauchly < 0.05
    e = eps if gg else 1.0
    p = float(stats.f.sf(F, df1 * e, df2 * e))
    return {"F": float(F), "df1": df1 * e, "df2": df2 * e, "p": p, "n": n, "gg_epsilon": float(eps),
            "mauchly_p": p_mauchly, "gg_applied": bool(gg),
            "p_uncorrected": float(stats.f.sf(F, df1, df2))}


def fmt_anova(r: dict) -> str:
    return (f"F({r['df1']:.2f}, {r['df2']:.2f}) = {r['F']:.2f}, p = {r['p']:.3g} (n = {r['n']}, "
            f"Mauchly p = {r['mauchly_p']:.3g}, GG {'applied' if r['gg_applied'] else 'not applied'}, "
            f"epsilon {r['gg_epsilon']:.2f})")


def oneway(groups: dict) -> dict:
    from scipy import stats
    vals = [np.asarray(v, float)[~np.isnan(np.asarray(v, float))] for v in groups.values()]
    F, p = stats.f_oneway(*vals)
    N = sum(len(v) for v in vals)
    return {"F": float(F), "df1": len(vals) - 1, "df2": N - len(vals), "p": float(p)}


def tukey(wide: pd.DataFrame) -> pd.DataFrame:
    """Tukey-Kramer HSD over the columns of `wide` (each column a condition)."""
    from statsmodels.stats.multicomp import pairwise_tukeyhsd
    long = wide.melt(var_name="cond", value_name="v").dropna()
    res = pairwise_tukeyhsd(long.v, long.cond)
    t = pd.DataFrame(res.summary().data[1:], columns=res.summary().data[0])
    return t[["group1", "group2", "meandiff", "p-adj", "reject"]]


def dunnett(groups: dict, control: str) -> pd.DataFrame:
    from scipy import stats
    names = [g for g in groups if g != control]
    r = stats.dunnett(*[np.asarray(groups[g], float) for g in names], random_state=0,
                      control=np.asarray(groups[control], float))
    return pd.DataFrame({"group": names, "mean": [np.nanmean(groups[g]) for g in names],
                         "control_mean": np.nanmean(groups[control]), "statistic": r.statistic,
                         "p": r.pvalue})


# ---------------------------------------------------------------- per-session helpers

def ensemble_windows(data: dict, cells: list, trial: str, w: int) -> tuple[np.ndarray, np.ndarray]:
    """Window directions and per-cell spike counts of an ensemble in one trial, over the samples
    all its files share (one stable2 file of session 1121R157 is 15 min long)."""
    n = min(len(data[c][trial]["d"]) for c in cells)
    dirs = window_directions(data[cells[0]][trial]["d"][:n], w)
    counts = np.stack([window_counts(data[c][trial]["n"][:n], w) for c in cells])
    return dirs, counts


def spike_count_series(x: dict, bin_s: float, t_end: float) -> np.ndarray:
    """Spike counts in bins of bin_s seconds from the trial's first timestamp to t_end (s)."""
    t = (x["spike_t"] - x["first_ts"]) / 1e4
    edges = np.arange(0, t_end + bin_s, bin_s)
    return np.histogram(t, edges)[0]
