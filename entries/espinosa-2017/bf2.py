"""Loading and measures for CRCNS bf-2 (Espinosa et al. 2017, Cereb Cortex, doi:10.1093/cercor/bhx302).

The data set is not versioned (docs/archives.md, CRCNS). Its files are tar.gz archives in the public
bucket crcnsarchive, under bf-2/live/. A gzip stream cannot be read at random, so each archive is
streamed once from start to end (tarfile mode "r|gz") and only the members the analysis needs are
kept in memory; the raw .rhd files and the videos are skipped without being stored.

Parameters and where they come from:

- Response classification ("shared method" in the opening comment of claims/espinosa-2017.yaml,
  from Methods, Unit cross-correlation analysis): 30-s window (15 s before to 15 s after onset),
  500-ms bins with the central bin from -250 to +250 ms, normalization by the spikes within the
  window (readings n1 and n2), 100 shuffles of inter-event intervals, P < 0.01 (above or below all
  100 shuffles), readings r1 to r3. The 250-ms bin is the Figure 1C variant named there.
- Pulse bins: the bins whose centres fall in (0, 5] s, so ten 500-ms bins (0.25 to 5.25 s) or
  twenty 250-ms bins (0.125 to 5.125 s). The claims file says "the bins of the 5-s pulse" without
  saying how the bin that straddles the end is treated; this is a standard choice of edge, which
  shifts the window by a quarter of a bin.
- Shuffles: the claims file (Methods) says spike times and pulse onsets are shuffled by exchanging
  their inter-event intervals; both interval sequences are permuted, keeping the first event.
  The seed is fixed per unit (a standard choice).
- Percent change: (mean normalized rate over the pulse - 1) x 100 (claims file, opening comment).
"""
import io
import tarfile

import fsspec
import h5py
import numpy as np
import scipy.io as sio
from scipy import stats
from scipy.optimize import curve_fit

BUCKET = "https://crcnsarchive.s3-us-west-2.amazonaws.com/bf-2/live"
DATASET = "crcns:bf-2/unversioned"  # CRCNS data sets are not versioned; doi:10.6080/K0MG7MQW
VP_ANIMALS = ["NE48", "NE52", "NE58", "NE69"]
# MD5 sums from bf-2/live/checksums.md5, read 2026-11-09.
MD5 = {
    "Electrophysiology/VP/NE48.tar.gz": "5f37e8df4e970fa84a481a9e63d9d2c8",
    "Electrophysiology/VP/NE52.tar.gz": "90620fda19c0a452426d7bf33cc0d27e",
    "Electrophysiology/VP/NE58.tar.gz": "089b2d7874cadedf443ab730801c4e40",
    "Electrophysiology/VP/NE69.tar.gz": "d8f888a0ca44d3d293f311e6d2997871",
    "Behavioral_tests/OPEN_FIELD/VP.tar.gz": "e4addaf02750ee36a60ecf779c596cb8",
    "Behavioral_tests/OPEN_FIELD/Control.tar.gz": "b60f5acafdac057130a6cb1a8edf9b9b",
    "Behavioral_tests/OPEN_FIELD/result_rapidez_all.mat": "1d1d14cdfe7460fa1046ebd34e1722b5",
}

# Columns of data_correlation.mat, as named in its header row (row 0).
CORR_COLS = {
    "experiment": 0, "rec": 1, "intensity": 2, "pulse": 3, "channel": 4, "frate": 5,
    "xcorr": 6, "waveform": 9, "int_real": 10, "rt_laser": 11, "rt_somatic": 12,
    "spikes": 14, "sig_laser": 17, "shuffle_laser": 18, "sig_somatic": 19,
}


def _arr(x):
    return np.atleast_1d(np.asarray(x, dtype=float)).ravel()


def _read_lan(raw):
    """The fields of a recxx_lan500.mat (MATLAB 7.3) that the analysis uses; LAN.data is not read."""
    h = h5py.File(io.BytesIO(raw), "r")
    L = h["LAN"]
    out = {
        "srate": float(np.array(L["srate"]).squeeze()),
        "pnts": int(np.array(L["pnts"]).squeeze()),
        "nbchan": int(np.array(L["nbchan"]).squeeze()),
        "ttl": np.array(L["ttl"]).T.astype(np.int8),  # samples x rows (laser, somatosensory)
        "selected": np.array(h[L["selected"][0, 0]]).ravel().astype(bool),
        "dur_pulso": _arr(h["dur_pulso"]) if "dur_pulso" in h else None,
        "data_shape": h[L["data"][0, 0]].shape,
    }
    for key in ("RT", "RTa", "RTb"):
        if key in L:
            out[key] = _arr(L[key]["laten"])
    return out


def _read_corr(raw):
    c = sio.loadmat(io.BytesIO(raw), squeeze_me=True)["correlation"]
    header = [str(x) if isinstance(x, str) else "" for x in c[0]]
    units = []
    for row in c[1:]:
        u = {}
        for name, j in CORR_COLS.items():
            v = row[j]
            if name in ("experiment", "rec"):
                u[name] = str(v)
            elif name in ("intensity", "channel", "frate", "int_real"):
                u[name] = float(v)
            elif name in ("sig_laser", "sig_somatic"):
                v = np.asarray(v).ravel()
                u[name] = int(v[0]) if v.size else None
            elif name == "xcorr":
                v = np.asarray(v, dtype=float)
                u["xcorr_axis"], u["xcorr"] = (v[0], v[1]) if v.ndim == 2 else (None, None)
            else:
                u[name] = _arr(v)
        units.append(u)
    return header, units


def stream_animal(animal, folder="Electrophysiology/VP"):
    """Stream one animal's archive once; return its unit table and per-recording fields.

    Keeps data_correlation.mat, bad_channel.mat, and for each recording the LAN fields of
    recxx_lan500.mat and the name (with depth and laser setting) of its .rhd file.
    """
    url = f"{BUCKET}/{folder}/{animal}.tar.gz"
    recs, header, units, bad = {}, None, None, None
    with fsspec.open(url, block_size=2**24) as f:
        with tarfile.open(fileobj=f, mode="r|gz") as tf:
            for m in tf:
                if not m.isfile():
                    continue
                parts = m.name.split("/")
                base = parts[-1]
                if base == "data_correlation.mat":
                    header, units = _read_corr(tf.extractfile(m).read())
                elif base == "bad_channel.mat":
                    bad = _arr(sio.loadmat(io.BytesIO(tf.extractfile(m).read()))["bad_channel"])
                elif len(parts) == 3:
                    rec = recs.setdefault(parts[1], {"files": {}})
                    rec["files"][base] = m.size
                    if base.endswith("lan500.mat"):
                        rec["lan"] = _read_lan(tf.extractfile(m).read())
                    elif base.endswith(".rhd"):
                        rec["rhd"] = base
    return {"animal": animal, "header": header, "units": units, "recs": recs, "bad_channel": bad}


def stream_behavior(path):
    """Stream a behavior archive once: the list of its members (name, size), and the contents of
    its small .mat files outside the per-frame segmentation folders (segm/), kept as raw bytes."""
    members, small = [], {}
    with fsspec.open(f"{BUCKET}/{path}", block_size=2**24) as f:
        with tarfile.open(fileobj=f, mode="r|gz") as tf:
            for m in tf:
                if not m.isfile():
                    continue
                members.append((m.name, m.size))
                if m.name.endswith(".mat") and "/segm/" not in m.name and m.size < 5e7:
                    small[m.name] = tf.extractfile(m).read()
    return {"path": path, "members": members, "mats": small}


def read_mat_any(raw):
    """A .mat file's variables, whether MATLAB 5 (scipy) or 7.3 (h5py); 7.3 numeric datasets only."""
    try:
        d = sio.loadmat(io.BytesIO(raw), squeeze_me=True)
        return {k: v for k, v in d.items() if not k.startswith("__")}
    except NotImplementedError:
        h = h5py.File(io.BytesIO(raw), "r")
        return {k: np.array(h[k]).squeeze() for k in h.keys()
                if isinstance(h[k], h5py.Dataset) and h[k].dtype.kind in "fiu"}


# ---------------------------------------------------------------- responses to light


def onsets_from_ttl(ttl_row, srate):
    """Onset and offset times (s) of the 1 periods of a 0/1 TTL row."""
    d = np.diff(np.r_[0, ttl_row.astype(int), 0])
    return np.flatnonzero(d == 1) / srate, np.flatnonzero(d == -1) / srate


def shuffle_intervals(times, rng):
    """Permute the inter-event intervals, keeping the first event (Methods, via the claims file)."""
    if len(times) < 3:
        return times.copy()
    isi = np.diff(times)
    return times[0] + np.r_[0, np.cumsum(rng.permutation(isi))]


def peth_counts(spikes, onsets, binsize, half=15.0):
    """Spike counts per pulse and bin; bins centred on 0 (central bin -binsize/2 to +binsize/2)."""
    nb = int(round(half / binsize))
    edges = (np.arange(-nb, nb + 2) - 0.5) * binsize
    centres = np.arange(-nb, nb + 1) * binsize
    idx = np.searchsorted(spikes, onsets[:, None] + edges[None, :])
    return np.diff(idx, axis=1), centres


def normalize(counts, reading):
    """n1: each pulse by its own window total, then averaged; n2: summed over pulses, then
    normalized. Scaled by the number of bins so a flat rate gives 1 (claims file)."""
    nbins = counts.shape[1]
    if reading == "n1":
        tot = counts.sum(axis=1)
        ok = tot > 0
        if not ok.any():
            return np.full(nbins, np.nan)
        return (counts[ok] / tot[ok, None]).mean(axis=0) * nbins
    s = counts.sum(axis=0)
    return s / s.sum() * nbins if s.sum() > 0 else np.full(nbins, np.nan)


def classify_unit(spikes, onsets, binsize, reading_n, n_shuffle=100, seed=0, pulse=5.0):
    """Normalized discharge and its shuffles for one unit, and the classes under r1, r2, r3.

    Returns dict with the normalized curve, the bin centres, the pulse mean, the percent change and
    the class (+1 excited, -1 inhibited, 0 unaffected) under each reading.
    """
    rng = np.random.default_rng(seed)
    counts, centres = peth_counts(spikes, onsets, binsize)
    curve = normalize(counts, reading_n)
    pb = (centres > 0) & (centres <= pulse + 1e-9)
    sh = np.empty((n_shuffle, len(centres)))
    for k in range(n_shuffle):
        s = shuffle_intervals(spikes, rng)
        o = shuffle_intervals(onsets, rng)
        c, _ = peth_counts(s, o, binsize)
        sh[k] = normalize(c, reading_n)
    m = np.nanmean(curve[pb])
    sh_m = np.nanmean(sh[:, pb], axis=1)
    r1 = 1 if m > np.nanmax(sh_m) else (-1 if m < np.nanmin(sh_m) else 0)
    above = (curve[pb] > np.nanmax(sh[:, pb], axis=0)).any()
    below = (curve[pb] < np.nanmin(sh[:, pb], axis=0)).any()
    sign = 1 if m > np.nanmean(sh_m) else -1
    r2 = sign if (above or below) else 0
    if np.isfinite(curve[pb]).all() and np.isfinite(sh[:, pb]).all():
        p3 = stats.ranksums(curve[pb], sh[:, pb].ravel()).pvalue
    else:
        p3 = np.nan
    r3 = (1 if np.median(curve[pb]) > np.median(sh[:, pb]) else -1) if p3 < 0.01 else 0
    return {"curve": curve, "centres": centres, "pulse_mean": m, "pct": (m - 1) * 100,
            "shuffle_mean": float(np.nanmean(sh_m)), "r1": r1, "r2": r2, "r3": r3, "p_r3": p3}


# ---------------------------------------------------------------- kinetics (fig1e)


def _expo(t, a, b, tau):
    return a + b * (1 - np.exp(-t / tau))


def fit_tau(curve, centres, window, pulse=5.0):
    """Time constant (ms) of a single exponential approaching a plateau, fitted to the normalized
    discharge from light onset: w1 up to the first extremum of the response (the bin of largest
    absolute deviation from 1 within the pulse), w2 over the whole pulse (claims file criterion).
    The bin before onset (centre <= 0, last pre-onset bin) gives the starting value at t = 0."""
    sel = (centres >= 0) & (centres <= pulse + 1e-9)
    t = centres[sel]
    y = curve[sel]
    if window == "w1":
        k = int(np.argmax(np.abs(y[1:] - 1))) + 1
        t, y = t[: k + 1], y[: k + 1]
    if len(t) < 3 or not np.isfinite(y).all():
        return np.nan
    try:
        p, _ = curve_fit(_expo, t, y, p0=[y[0], y[-1] - y[0], 0.3],
                         bounds=([-np.inf, -np.inf, 1e-3], [np.inf, np.inf, 20.0]), maxfev=5000)
    except (RuntimeError, ValueError):
        return np.nan
    return p[2] * 1000
