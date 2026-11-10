"""Sharp-wave ripple (SWR) and SWR-triggered slow gamma (SG) measures for CRCNS hc-26.

The LFP of hc-26 (Jones et al. 2019) is in nine tar.gz files, one per cohort, age and
genotype, 6 to 22 GB each. A tar.gz can only be read from the start, so each file is
streamed once (fsspec, one HTTP request, ``tarfile`` in stream mode) and each session is
reduced as it arrives to a few small tables: the candidate SWRs on the detection site, the
SG power of each region's sites in the 100 ms after each SWR, the SG power of the
immobile LFP for z-scoring, and (Cohort 1) multi-unit spike counts around each SWR.
Selections that the claims vary (threshold, immobility, per-session or pooled averages)
are applied afterwards, in :func:`animal_measures`, so every reading is computed from the
same pass.

Where each parameter comes from. "Claims (A)" and "Claims (B)" are the methods fixed in
the header of claims/jones-2019.yaml; "code" is the paper's code,
https://github.com/emilyasterjones/Jones_2019 (formerly SWR-predictions), commit
ca056a835631a8fea44a30cbf9845b53457dcbd1, file named.

- Ripple filter: the equiripple 150-250 Hz kernel of the code (Preprocessing/
  agripplefilter.mat, 199 taps) and the 125-250 Hz kernel (agripplefilter3.mat, 396
  taps), read from the repository at that commit (Claims (A)). Applied forward and
  backward (zero phase), as filtereeg2 of the Frank lab framework does; the envelope is
  the magnitude of the analytic signal. Samples below -30000 are bridged linearly before
  filtering (code, ej_rippledayprocess.m).
- Envelope smoothed with a Gaussian of 4 ms SD (code, ag_extractripples.m); baseline and
  SD are the mean and SD of the smoothed envelope over the whole session (same file;
  Claims (A)).
- Events (code, extracteventsnew.cpp as called by ag_extractripples.m with 3 SD and
  0.015 s): the envelope at or above 3 SD for at least 15 samples; an event runs from the
  last sample at or below baseline before the crossing to the last sample above baseline
  after it; ``maxthresh`` is the highest level, in SD above baseline, that the envelope
  holds for 15 consecutive samples around the event's peak (computed here as the maximum
  over 15-sample windows inside the event of the window's minimum, a standard choice
  that differs from the C code's greedy search from the peak only when two lobes tie).
  "Envelope above 5 SD for at least 15 ms" (the Methods) is thus ``maxthresh >= 5``.
- Noise rule (code, getvalidrips.m): an event is dropped when 16 or more channels hold
  an event (at their own 3 SD) whose midpoint falls inside it and whose sustained level
  exceeds the detection site's baseline + 5 SD. Events within 0.4 s of the session's
  start or end are dropped (same file, called with [0.4 0.4]).
- Immobility (code, runcalcriprates.m: get2dstate, immobilecutoff 1, immobilitytime >
  30): the deposited velocity (pos.vel, already smoothed with a 500 ms Gaussian, data
  descriptor) below 1 cm/s, counted only after it has lasted 30 s. An SWR counts when
  its start and end are both in such time (getvalidrips.m).
- Detection site: the chinfo site with area 'ca1' whose layer contains 'pyr 1' (code,
  runcalcriprates.m; Claims (A)).
- SG power (code, RTspecgram3.m and runRTS.m; Claims (B)): multitaper spectra with
  time-bandwidth 3 and 5 tapers (Chronux tapers [3 5]) of 100 ms windows, FFT length 128
  (Chronux default pad 0), so a 7.8125 Hz grid. SWR window: the 100 ms starting at the
  SWR's threshold crossing (the code's window 5 of 8 non-overlapping windows from -0.4 s,
  centred at +50 ms). Z-scored per frequency against the mean and SD over the immobile
  LFP's non-overlapping 100 ms windows (here, the windows lying wholly in immobile time;
  the code concatenates the immobile samples first, a standard choice that cannot change
  a result materially). Bins 31.25, 39.06, 46.88 Hz (Methods' 30-50 Hz) and the code's
  bins 4-7, which add 54.69 Hz, are both kept.
- Regions (code, plotRTSstats.m location string; Claims (B)): CA3 = area 'ca3' with
  layer containing 'pyr' or 'sr'; CA1-sr = area 'ca1' with layer containing 'sr'; DG =
  area 'dg' with layer containing 'gc' or 'hil'. The Methods restrict DG to sites "with
  confirmed dentate spikes"; that check is not run here (see the notebook).
- MUA (Cohort 1; code, RTMUA.m): spike counts of the detection site's deposited spike
  times in 0-100 ms after the SWR's threshold crossing, in the 400 ms before it, and in
  -400 to -300 ms.
"""
from __future__ import annotations

import io
import re
import tarfile
import time
from concurrent.futures import ProcessPoolExecutor

import fsspec
import numpy as np
import scipy.io as sio
from scipy.io.matlab import mat_struct
from scipy.signal import oaconvolve
from scipy.signal.windows import dpss
from numpy.lib.stride_tricks import sliding_window_view

DATASET = "hc-26"
VERSION = "unversioned"      # CRCNS data sets are not versioned (docs/archives.md); MD5 sums in the notebook header
BASE = "https://crcnsarchive.s3-us-west-2.amazonaws.com/hc-26/live/data/"
CODE = ("https://raw.githubusercontent.com/emilyasterjones/Jones_2019/"
        "ca056a835631a8fea44a30cbf9845b53457dcbd1/Preprocessing/")
TARS = {  # (cohort, age group, genotype) -> path under BASE
    (1, "12-18mo", "E3"): "Cohort_1/E3KI.tar.gz",
    (1, "12-18mo", "E4"): "Cohort_1/E4KI.tar.gz",
    (2, "5-8mo", "E3"): "Cohort_2/5-8mo/E3KI.tar.gz",
    (2, "5-8mo", "E4"): "Cohort_2/5-8mo/E4KI.tar.gz",
    (2, "9-11mo", "E3"): "Cohort_2/9-11mo/E3KI.tar.gz",
    (2, "9-11mo", "E4"): "Cohort_2/9-11mo/E4KI.tar.gz",
    (2, "13-17mo", "E3"): "Cohort_2/13-17mo/E3KI.tar.gz",
    (2, "13-17mo", "E4"): "Cohort_2/13-17mo/E4KI.tar.gz",
}
FS = 1000
NSTD_DETECT = 3.0          # code, dayprocess_trodes.m -> ag_extractripples(..., .015, 3)
MINDUR = 15                # samples, 15 ms
SMOOTH_SD = 4              # samples, 4 ms
EDGE = 0.4                 # s, getvalidrips win [0.4 0.4]
NOISE_CHANNELS = 16        # getvalidrips.m
IMMOBILE_CM_S = 1.0        # get2dstate immobilecutoff
IMMOBILE_MIN_S = 30.0      # immobilitytime > 30
SG_BINS = np.array([4, 5, 6, 7])   # FFT bins of a 128-point FFT at 1 kHz: 31.25-54.69 Hz
WIN = 100                  # samples, 100 ms spectral window
TAPERS = dpss(WIN, 3, 5)   # Chronux tapers [3 5]


def conv(o):
    """MATLAB structs and cell arrays (scipy.io) to dicts and lists."""
    if isinstance(o, mat_struct):
        return {k: conv(getattr(o, k)) for k in o._fieldnames}
    if isinstance(o, np.ndarray) and o.dtype == object:
        return [conv(x) for x in o.ravel()]
    return o


def _h5(obj, f):
    """MATLAB 7.3 (HDF5) object to dicts, lists and arrays."""
    import h5py
    if isinstance(obj, h5py.Group):
        return {k: _h5(obj[k], f) for k in obj.keys() if not k.startswith("#")}
    if obj.dtype == object or h5py.check_dtype(ref=obj.dtype) is not None:
        return [_h5(f[r], f) if r else None for r in obj[()].ravel(order="F")]
    a = obj[()]
    if obj.attrs.get("MATLAB_class", b"") == b"char":
        return "".join(map(chr, np.asarray(a).ravel()))
    a = np.asarray(a)
    return a.item() if a.size == 1 else a.ravel()


def loadmat_bytes(b: bytes) -> dict:
    if b[:128].find(b"MATLAB 7.3") >= 0 or b[512:520] == b"\x89HDF\r\n\x1a\n":
        import h5py
        with h5py.File(io.BytesIO(b), "r") as f:
            return {k: _h5(f[k], f) for k in f.keys() if not k.startswith("#")}
    d = sio.loadmat(io.BytesIO(b), squeeze_me=True, struct_as_record=False)
    return {k: conv(v) for k, v in d.items() if not k.startswith("__")}


def last_cell(v):
    """The filter framework stores session s at cell s; earlier cells are empty."""
    if isinstance(v, list):
        vals = [x for x in v if isinstance(x, (dict, list)) and len(x)]
        return last_cell(vals[-1]) if vals else None
    return v


def ripple_kernels() -> dict:
    """The paper's ripple filters, from its repository at the pinned commit."""
    out = {}
    for key, fn in (("150-250", "agripplefilter.mat"), ("125-250", "agripplefilter3.mat")):
        with fsspec.open(CODE + fn, "rb") as f:
            k = sio.loadmat(io.BytesIO(f.read()), squeeze_me=True,
                            struct_as_record=False)["ripplefilter"]
        out[key] = (np.asarray(k.kernel, float), str(k.descript))
    return out


def _bridge(x: np.ndarray) -> np.ndarray:
    """Linear fill of runs below -30000 (code, ej_rippledayprocess.m)."""
    bad = x < -30000
    x = x.astype(np.float64)
    if bad.any():
        good = np.flatnonzero(~bad)
        x[bad] = np.interp(np.flatnonzero(bad), good, x[good])
    return x, bad


def envelope(x: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    """Zero-phase FIR band-pass (forward and backward) and analytic-signal magnitude.

    The forward-backward filter is the kernel convolved with its reverse; the analytic
    signal is obtained in one complex convolution with that kernel's analytic version
    (zero-padded, so the band edges are exact to within the padding)."""
    kk = np.convolve(kernel, kernel[::-1])
    n = 4096
    pad = np.zeros(n)
    c = n // 2 - len(kk) // 2
    pad[c:c + len(kk)] = kk
    F = np.fft.fft(pad)
    h = np.zeros(n)
    h[0] = 1
    h[1:n // 2] = 2
    h[n // 2] = 1
    ka = np.fft.ifft(F * h)
    ka = ka[c - 64:c + len(kk) + 64]           # keep the kernel and a margin of its tail
    y = oaconvolve(x, ka, mode="same")
    return np.abs(y)


def extract_events(renv: np.ndarray, base: float, sd: float, nstd: float = NSTD_DETECT,
                   mindur: int = MINDUR):
    """Events as extracteventsnew.cpp with minsep 0 (see module docstring).

    Returns a dict of arrays: start, end (inclusive sample indices), thresh (first sample
    at or above threshold), peak (index), mid (energy midpoint index), maxthresh (SD)."""
    thr = base + nstd * sd
    above = renv >= thr
    d = np.diff(above.astype(np.int8), prepend=0, append=0)
    on = np.flatnonzero(d == 1)
    off = np.flatnonzero(d == -1)            # first sample below
    keep = (off - on) >= mindur
    on, off = on[keep], off[keep]
    if len(on) == 0:
        return {k: np.zeros(0, int if k != "maxthresh" else float)
                for k in ("start", "end", "thresh", "peak", "mid", "maxthresh")}
    below = np.flatnonzero(renv <= base)
    # event extends back to the last sample <= baseline and forward to the last > baseline
    i0 = np.searchsorted(below, on) - 1
    start = np.where(i0 >= 0, below[np.clip(i0, 0, None)] + 1, 0)
    i1 = np.searchsorted(below, off)
    end = np.where(i1 < len(below), below[np.clip(i1, 0, len(below) - 1)] - 1, len(renv) - 1)
    # merge crossings that share one supra-baseline excursion
    first = np.r_[True, start[1:] > end[:-1]]
    grp = np.cumsum(first) - 1
    ng = grp[-1] + 1
    s = np.zeros(ng, int); e = np.zeros(ng, int); t = np.zeros(ng, int)
    s[grp[::-1]] = start[::-1]
    t[grp[::-1]] = on[::-1]
    np.maximum.at(e, grp, end)
    # drop events touching the data's edges (allowstartend 0)
    ok = (s > 0) & (e < len(renv) - 1)
    s, e, t = s[ok], e[ok], t[ok]
    peak = np.zeros(len(s), int); mid = np.zeros(len(s), int); mt = np.zeros(len(s))
    for j in range(len(s)):
        seg = renv[s[j]:e[j] + 1]
        peak[j] = s[j] + int(np.argmax(seg))
        en = np.cumsum(seg * seg)
        mid[j] = s[j] + int(np.searchsorted(en, en[-1] / 2))
        mt[j] = (sliding_window_view(seg, mindur).min(axis=1).max()
                 if len(seg) >= mindur else seg.min())
    return {"start": s, "end": e, "thresh": t, "peak": peak, "mid": mid,
            "maxthresh": (mt - base) / sd}


_G = np.exp(-0.5 * (np.arange(-4 * SMOOTH_SD, 4 * SMOOTH_SD + 1) / SMOOTH_SD) ** 2)
_G /= _G.sum()


def smooth(env: np.ndarray) -> np.ndarray:
    """Gaussian smoothing, 4 ms SD, kernel +-4 SD (code, ag_extractripples.m: gaussian(4,
    32) and smoothvect)."""
    return oaconvolve(env, _G, mode="same")


def mt_power(x: np.ndarray, starts: np.ndarray) -> np.ndarray:
    """Multitaper power (Chronux mtspectrumc: mean over tapers of |FFT|^2, 128-point
    FFT) of the 100 ms windows beginning at ``starts``, at the SG bins. (n, 4)."""
    if len(starts) == 0:
        return np.zeros((0, len(SG_BINS)))
    idx = starts[:, None] + np.arange(WIN)[None, :]
    seg = x[idx]                                     # (n, 100)
    J = np.fft.rfft(seg[:, None, :] * TAPERS[None, :, :], n=128, axis=-1)[..., SG_BINS]
    return (np.abs(J) ** 2).mean(axis=1)


def immobile_mask(pos: dict, t0: float, n: int) -> np.ndarray:
    """Boolean per LFP sample: immobile (vel < 1 cm/s) for more than 30 s so far."""
    pt = np.asarray(pos["time"], float)
    vel = np.asarray(pos["vel"], float)
    imm = vel < IMMOBILE_CM_S
    d = np.diff(imm.astype(np.int8), prepend=0)
    starts = np.flatnonzero(d == 1)                                      # first immobile
    ends = np.flatnonzero(np.diff(imm.astype(np.int8), append=0) == -1)  # last immobile
    mask = np.zeros(n, bool)
    for a, b in zip(starts, ends):
        ta = pt[a] + IMMOBILE_MIN_S
        tb = pt[b]
        if tb <= ta:
            continue
        i0 = int(np.ceil((ta - t0) * FS)); i1 = int(np.floor((tb - t0) * FS))
        i0 = max(i0, 0); i1 = min(i1, n - 1)
        if i1 >= i0:
            mask[i0:i1 + 1] = True
    return mask


def _site_groups(chinfo_sess: list) -> dict:
    """Site numbers (1-based) by role, from one session's chinfo (see docstring)."""
    g = {"detect": [], "ca3": [], "ca1sr": [], "dg": [], "dead": [], "labels": []}
    for c in chinfo_sess:
        if not isinstance(c, dict):
            continue
        area = str(c.get("area", "")).lower()
        layer = c.get("layer", "")
        layer = "" if isinstance(layer, np.ndarray) else str(layer).lower()
        site = int(c["site"])
        g["labels"].append((site, area, layer))
        if area == "dead":
            g["dead"].append(site)
        if area == "ca1" and "pyr 1" in layer:
            g["detect"].append(site)
        if area == "ca3" and ("pyr" in layer or "sr" in layer):
            g["ca3"].append(site)
        if area == "ca1" and "sr" in layer:
            g["ca1sr"].append(site)
        if area == "dg" and ("gc" in layer or "hil" in layer):
            g["dg"].append(site)
    return g


def process_session(chans: dict, groups: dict, kernels: dict, variant_filter: bool) -> dict:
    """Reduce one session's 32 LFP channels (dict site -> eeg struct) to small tables."""
    det = groups["detect"][0]
    e0 = chans[det]
    t0 = float(e0["starttime"])
    n = min(len(c["data"]) for c in chans.values())
    k150 = kernels["150-250"][0]
    chan_ev = {}
    out = {"t0": t0, "n": n, "sites": {}}
    raw_det = None
    for site, c in sorted(chans.items()):
        if site in groups["dead"]:
            continue
        x, bad = _bridge(np.asarray(c["data"][:n]))
        renv = smooth(envelope(x, k150))
        base, sd = float(renv.mean()), float(renv.std(ddof=1))
        ev = extract_events(renv, base, sd)
        chan_ev[site] = (ev["mid"], ev["maxthresh"] * sd + base)
        if site == det:
            out["det_events"] = ev
            out["det_base"], out["det_sd"] = base, sd
            raw_det = x
            # direct detection at 5 SD (the Methods' wording), for a variant
            out["det_events_5sd"] = extract_events(renv, base, sd, nstd=5.0)
            if variant_filter:
                renv3 = smooth(envelope(x, kernels["125-250"][0]))
                b3, s3 = float(renv3.mean()), float(renv3.std(ddof=1))
                out["det_events_125"] = extract_events(renv3, b3, s3)
                out["det_base_125"], out["det_sd_125"] = b3, s3
        is_probe = site in groups["ca3"] or site in groups["ca1sr"] or site in groups["dg"]
        if is_probe:
            out["sites"][site] = {"x": x.astype(np.float32)}
    # noise rule: count channels with an event whose midpoint lies inside the detection
    # event and whose sustained level exceeds the detection site's baseline + 5 SD
    lvl = out["det_base"] + 5 * out["det_sd"]
    for key in ("det_events", "det_events_5sd", "det_events_125"):
        if key not in out:
            continue
        ev = out[key]
        cnt = np.zeros(len(ev["start"]), int)
        for site, (mid, lev) in chan_ev.items():
            m = np.sort(mid[lev > lvl])
            if len(m) == 0:
                continue
            a = np.searchsorted(m, ev["start"], side="left")
            b = np.searchsorted(m, ev["end"], side="right")
            cnt += (b - a) > 0
        ev["noise_channels"] = cnt
    # SG: per probe site, power after each candidate SWR (all 3 SD events and the 5 SD
    # direct detections) and power of every 100 ms window of the session
    nwin = n // WIN
    allstarts = np.arange(nwin) * WIN
    for site, d in out["sites"].items():
        x = d.pop("x").astype(np.float64)
        d["win_power"] = mt_power(x, allstarts).astype(np.float32)
        for key in ("det_events", "det_events_5sd"):
            st = out[key]["thresh"]
            ok = st + WIN <= n
            p = np.full((len(st), len(SG_BINS)), np.nan)
            p[ok] = mt_power(x, st[ok])
            d["swr_power_" + key] = p.astype(np.float32)
    out["det_site"] = det
    return out


def intervals(mask: np.ndarray) -> np.ndarray:
    """(k, 2) array of [start, end) sample indices of the True runs of ``mask``."""
    d = np.diff(mask.astype(np.int8), prepend=0, append=0)
    return np.c_[np.flatnonzero(d == 1), np.flatnonzero(d == -1)]


def reduce_with_position(ses: dict, pos: dict | None) -> None:
    """Once the session's position is read: the immobile time (as intervals of LFP
    samples) and, per probe site, the mean and SD of the SG power over the 100 ms
    windows lying wholly in immobile time (the z-scoring reference, RTspecgram3.m).
    The per-window powers are then dropped to keep the result small."""
    if "det_site" not in ses:
        return
    n = ses["n"]
    if pos is None:
        ses["no_position"] = True
        mask = np.zeros(n, bool)
    else:
        mask = immobile_mask(pos, ses["t0"], n)
        ses["pos_range"] = (float(pos["time"][0]), float(pos["time"][-1]), len(pos["time"]))
        ses["vel_range"] = (float(np.nanmin(pos["vel"])), float(np.nanmax(pos["vel"])))
    ses["immobile"] = intervals(mask)
    nwin = n // WIN
    win_imm = mask[:nwin * WIN].reshape(nwin, WIN).all(axis=1)
    ses["n_immobile_windows"] = int(win_imm.sum())
    for site, d in ses["sites"].items():
        wp = d.pop("win_power").astype(np.float64)
        sel = wp[win_imm]
        d["imm_mean"] = sel.mean(axis=0) if len(sel) > 1 else np.full(len(SG_BINS), np.nan)
        d["imm_sd"] = sel.std(axis=0, ddof=1) if len(sel) > 1 else np.full(len(SG_BINS), np.nan)


MUA_SCALES = {"s": 1.0, "ms": 1e-3, "samples at 30 kHz": 1 / 30000}


def reduce_mua(ses: dict, mu: dict) -> dict:
    """Spike counts of the detection site around each candidate SWR's threshold crossing.

    The descriptor gives spike times in ms; RTMUA.m divides them by 30000. The unit is
    taken as the one that puts the spikes inside the recording's time range, and
    reported."""
    st = np.sort(np.asarray(mu["spiketimes"], float).ravel())
    out = {"n_spikes": len(st), "raw_range": (float(st[0]), float(st[-1])) if len(st) else None,
           "mua_range": (float(mu["starttime"]), float(mu["endtime"])), "ref": mu.get("ref")}
    if not len(st) or "det_site" not in ses:
        return out
    lo, hi = float(mu["starttime"]), float(mu["endtime"])
    fits = {k: ((st[0] * v >= lo - 1) and (st[-1] * v <= hi + 1)) for k, v in MUA_SCALES.items()}
    unit = next((k for k, ok in fits.items() if ok), None)
    out["unit_fits"] = fits
    out["unit"] = unit
    if unit is None:
        return out
    t = st * MUA_SCALES[unit]
    trig = ses["t0"] + ses["det_events"]["thresh"] / FS
    for name, (a, b) in {"during": (0.0, 0.1), "pre400": (-0.4, 0.0),
                         "pre400_300": (-0.4, -0.3)}.items():
        out[name] = (np.searchsorted(t, trig + b) - np.searchsorted(t, trig + a)).astype(np.int32)
    # spikes in immobile time, for the rate of the whole immobile period
    imm = ses.get("immobile", np.zeros((0, 2), int))
    ts = ses["t0"] + imm / FS
    out["immobile_spikes"] = int(sum(np.searchsorted(t, b) - np.searchsorted(t, a) for a, b in ts))
    out["immobile_s"] = float((imm[:, 1] - imm[:, 0]).sum() / FS) if len(imm) else 0.0
    return out


def _parse_name(nm: str):
    """'E4KI/Alpha/Alphaeeg01-1-07.mat' -> (animal, kind, session, channel)."""
    parts = nm.split("/")
    if len(parts) < 3 or not nm.endswith(".mat"):
        return None
    animal, fn = parts[-2], parts[-1]
    rest = fn[len(animal):] if fn.startswith(animal) else fn
    m = re.match(r"(eeg|mua)(\d+)-1-(\d+)\.mat$", rest)
    if m:
        return animal, m.group(1), int(m.group(2)), int(m.group(3))
    m = re.match(r"(pos|task|chinfo)(\d*)\.mat$", rest)
    if m:
        return animal, m.group(1), int(m.group(2)) if m.group(2) else None, None
    return animal, "other:" + rest, None, None


class ResumableStream(io.RawIOBase):
    """A sequential HTTP stream (fsspec, one GET) that reopens at the current offset
    with a Range request when the connection fails. aiohttp's default 5 min total
    timeout is lifted, since one file takes longer than that to read."""

    def __init__(self, url: str, retries: int = 20):
        import aiohttp
        self.url, self.pos, self.retries, self.reopened = url, 0, retries, 0
        self.fs = fsspec.filesystem("http", client_kwargs={"timeout": aiohttp.ClientTimeout(
            total=None, sock_connect=60, sock_read=300)})
        self.f = self.fs.open(url, block_size=0)

    def readable(self):
        return True

    def readinto(self, b):
        for attempt in range(self.retries):
            try:
                data = self.f.read(len(b))
                break
            except Exception:
                if attempt == self.retries - 1:
                    raise
                time.sleep(2 + 2 * attempt)
                self.reopened += 1
                try:
                    self.f.close()
                except Exception:
                    pass
                self.f = self.fs.open(self.url, block_size=0,
                                      headers={"Range": f"bytes={self.pos}-"})
        n = len(data)
        b[:n] = data
        self.pos += n
        return n

    def close(self):
        try:
            self.f.close()
        finally:
            super().close()


def process_tar(key, limit_animals: int | None = None, limit_sessions: int | None = None):
    """Stream one tar.gz and reduce every animal. Returns {animal: raw results}."""
    t_start = time.time()
    kernels = ripple_kernels()
    url = BASE + TARS[key]
    f = io.BufferedReader(ResumableStream(url), buffer_size=2 ** 22)
    tf = tarfile.open(fileobj=f, mode="r|gz")
    results = {}
    state = {"animal": None}

    def finish_session(a):
        st = state
        if st.get("chans"):
            s = st["sess"]
            g = _site_groups(st["chinfo"][s - 1])
            if g["detect"]:
                st["sessions"][s] = process_session(st["chans"], g, kernels,
                                                    variant_filter=key[0] == 1)
                st["sessions"][s]["groups"] = g
            else:
                st["sessions"][s] = {"missing_detect_site": True, "groups": g}
        st["chans"] = {}

    def finish_animal():
        st = state
        if st["animal"] is None:
            return
        finish_session(st["animal"])
        for s, ses in st["sessions"].items():
            reduce_with_position(ses, st["pos"].get(s))
            if s in st["mua"]:
                st["mua"][s] = reduce_mua(ses, st["mua"][s])
        results[st["animal"]] = {"sessions": st["sessions"],
                                 "task": st["task"], "mua": st["mua"],
                                 "files": st["files"]}

    n_animals = 0
    for m in tf:
        if not m.isfile():
            continue
        p = _parse_name(m.name)
        if p is None:
            continue
        animal, kind, sess, ch = p
        if animal != state["animal"]:
            finish_animal()
            n_animals += 1
            if limit_animals and n_animals > limit_animals:
                break
            state.update(animal=animal, sessions={}, pos={}, task=None, mua={},
                         chinfo=None, chans={}, sess=None, files={})
        state["files"][kind] = state["files"].get(kind, 0) + 1
        if kind == "chinfo":
            state["chinfo"] = loadmat_bytes(tf.extractfile(m).read())["chinfo"]
        elif kind == "eeg":
            if limit_sessions and sess > limit_sessions:
                continue
            if sess != state["sess"]:
                finish_session(animal)
                state["sess"] = sess
            e = last_cell(loadmat_bytes(tf.extractfile(m).read())["eeg"])
            state["chans"][ch] = e
        elif kind == "mua":
            if state["chans"]:
                finish_session(animal)
            ses = state["sessions"].get(sess)
            if ses is None or "det_site" not in ses or ch != ses["det_site"]:
                continue
            mu = last_cell(loadmat_bytes(tf.extractfile(m).read())["mua"])
            state["mua"][sess] = {k: mu[k] for k in ("spiketimes", "starttime", "endtime",
                                                     "samprate", "ref") if k in mu}
        elif kind == "pos":
            if state["chans"]:
                finish_session(animal)
            pv = last_cell(loadmat_bytes(tf.extractfile(m).read())["pos"])
            state["pos"][sess] = {k: np.asarray(pv[k]) for k in ("time", "vel", "x", "y")}
        elif kind == "task":
            state["task"] = loadmat_bytes(tf.extractfile(m).read())["task"]
    else:
        finish_animal()
    if limit_animals and n_animals > limit_animals:
        pass
    elif state["animal"] not in results:
        finish_animal()
    f.close()
    return {"key": key, "animals": results, "seconds": time.time() - t_start,
            "reopened": f.raw.reopened if hasattr(f, "raw") else None}


def run_all(keys=None, workers: int = 4, **kw):
    """Process tars in parallel (one process per tar, largest first)."""
    keys = keys or sorted(TARS, key=lambda k: -{"Cohort_1/E4KI.tar.gz": 22,
                                                "Cohort_1/E3KI.tar.gz": 18}.get(TARS[k], 10))
    with ProcessPoolExecutor(workers) as ex:
        futs = [ex.submit(process_tar, k, **kw) for k in keys]
        return [fu.result() for fu in futs]


# ---------------------------------------------------------------------------------------
# Measures per session and per mouse, from the reduced tables.
MIN_IMMOBILE_S = 600.0     # Methods: sessions with less than 10 min of immobility excluded
BANDS = {"30-50": [0, 1, 2], "bins4-7": [0, 1, 2, 3]}   # indices into SG_BINS


def _in_intervals(idx: np.ndarray, iv: np.ndarray) -> np.ndarray:
    if len(iv) == 0:
        return np.zeros(len(idx), bool)
    k = np.searchsorted(iv[:, 0], idx, side="right") - 1
    return (k >= 0) & (idx < iv[np.clip(k, 0, None), 1])


def valid_events(ses: dict, key: str = "det_events") -> np.ndarray:
    """getvalidrips.m: start and end in immobile time, 0.4 s from the session's edges,
    fewer than 16 channels with a coincident event."""
    ev = ses[key]
    iv = ses["immobile"]
    edge = int(EDGE * FS)
    return (_in_intervals(ev["start"], iv) & _in_intervals(ev["end"], iv)
            & (ev["start"] >= edge) & (ev["end"] <= ses["n"] - 1 - edge)
            & (ev["noise_channels"] < NOISE_CHANNELS))


def session_rows(res: list) -> list:
    """One dict per recorded session with every per-session measure and reading."""
    rows = []
    for r in res:
        cohort, age_group, geno = r["key"]
        for animal, a in r["animals"].items():
            tasks = a["task"] if isinstance(a["task"], list) else [a["task"]]
            tasks = [t for t in tasks if isinstance(t, dict)]
            for s, ses in sorted(a["sessions"].items()):
                t = next((x for x in tasks if int(x.get("sess", -1)) == s), {})
                row = {"cohort": cohort, "age_group": age_group, "genotype": geno,
                       "animal": animal, "key": animal.lower().replace("_", ""),
                       "session": s, "age_months": float(t.get("age", np.nan)),
                       "task_env": str(t.get("env", "")),
                       "task_descript": "" if isinstance(t.get("descript"), np.ndarray)
                       else str(t.get("descript", ""))}
                if "det_site" not in ses:
                    row["no_detection_site"] = True
                    rows.append(row)
                    continue
                g = ses["groups"]
                iv = ses["immobile"]
                imm_s = float((iv[:, 1] - iv[:, 0]).sum() / FS) if len(iv) else 0.0
                row.update(det_site=ses["det_site"], duration_s=ses["n"] / FS,
                           immobile_s=imm_s, base=ses["det_base"], sd=ses["det_sd"],
                           n_candidates=len(ses["det_events"]["start"]),
                           no_position=ses.get("no_position", False),
                           vel_max=ses.get("vel_range", (np.nan, np.nan))[1])
                v = valid_events(ses)
                mt = ses["det_events"]["maxthresh"]
                row["n_noise"] = int(((ses["det_events"]["noise_channels"] >= NOISE_CHANNELS)
                                      & (mt >= 5)).sum())
                row["n_swr_5sd"] = int((v & (mt >= 5)).sum())
                row["n_swr_3sd"] = int(v.sum())
                v5 = valid_events(ses, "det_events_5sd")
                row["n_swr_direct5"] = int(v5.sum())
                if "det_events_125" in ses:
                    v1 = valid_events(ses, "det_events_125")
                    m1 = ses["det_events_125"]["maxthresh"]
                    row["n_swr_125_5sd"] = int((v1 & (m1 >= 5)).sum())
                    row["n_swr_125_3sd"] = int(v1.sum())
                # SG power per region, per reading
                for trig, sel in (("5sd", v & (mt >= 5)), ("3sd", v)):
                    for region in ("ca3", "ca1sr", "dg", "dgval"):
                        if region == "dgval":
                            sites = [s_ for s_ in g["dg"] if any(
                                lab[0] == s_ and lab[2].startswith("val") for lab in g["labels"])]
                        else:
                            sites = g[region]
                        for band, bi in BANDS.items():
                            vals, sums, ns = [], [], []
                            for site in sites:
                                d = ses["sites"].get(site)
                                if d is None:
                                    continue
                                z = (d["swr_power_det_events"][sel][:, bi].astype(float)
                                     - d["imm_mean"][bi]) / d["imm_sd"][bi]
                                zm = np.nanmean(z, axis=1)
                                zm = zm[np.isfinite(zm)]
                                vals.append(zm.mean() if len(zm) else np.nan)
                                sums.append(zm.sum()); ns.append(len(zm))
                            k = f"sg_{region}_{trig}_{band}"
                            row[k] = float(np.nanmean(vals)) if vals else np.nan
                            row[k + "_sitesum"] = sums
                            row[k + "_siten"] = ns
                            row[f"sites_{region}"] = list(sites)
                # CA3 SG baseline and SD (immobile spectrogram), Methods bins
                bi = BANDS["30-50"]
                bm = [float(np.mean(ses["sites"][s_]["imm_mean"][bi])) for s_ in g["ca3"]
                      if s_ in ses["sites"]]
                bs = [float(np.mean(ses["sites"][s_]["imm_sd"][bi])) for s_ in g["ca3"]
                      if s_ in ses["sites"]]
                row["ca3_sg_base"] = float(np.mean(bm)) if bm else np.nan
                row["ca3_sg_sd"] = float(np.mean(bs)) if bs else np.nan
                mu = a["mua"].get(s)
                if mu and "during" in mu:
                    sel = v & (mt >= 5)
                    row["mua_unit"] = mu["unit"]
                    row["mua_during"] = float(mu["during"][sel].mean() / 0.1) if sel.any() else np.nan
                    row["mua_pre400"] = float(mu["pre400"][sel].mean() / 0.4) if sel.any() else np.nan
                    row["mua_pre400_300"] = float(mu["pre400_300"][sel].mean() / 0.1) if sel.any() else np.nan
                    row["mua_immobile_rate"] = mu["immobile_spikes"] / max(mu["immobile_s"], 1e-9)
                rows.append(row)
    return rows
