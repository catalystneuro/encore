"""Loading and measures for the fiber photometry recordings of dandiset 001038.

Azcorra, Gaertner et al. (2023), Nature Neuroscience, doi:10.1038/s41593-023-01401-9.

Each NWB file is one photometry recording (one depth) from one mouse, with one or two fibers.
For each fiber the file holds a normalized dF/F trace at 470 nm and its isosbestic (405 nm)
control at 100 Hz, treadmill velocity (m/s) and acceleration (m/s2), and for sessions with
stimuli an `Events` table (rewards tagged long, short or rest; air puffs; light; licking;
movement bouts), the acceleration and deceleration onsets (`WheelEvents`) and transient peaks.
Files are streamed from the archive at the pinned version; nothing is written to disk.

Where the parameters come from. The paper's analysis code is
https://github.com/DombeckLab/Azcorra2023 at commit fad12b25313f21611dd70c0056fb8bee48beeda1
(MATLAB). Unless marked otherwise, every function here is a port of that code:

- `mov_on_off` and `run_mask` port selectSignals_paper.m (double threshold 0.0237 / 0.0101 m/s,
  rest periods of at least 0.5 s, running bouts longer than 0.5 s with mean velocity above
  0.2 m/s, trimmed by 0.1 s at each end, and 5 s after every consumed reward, air puff or light
  left out). The thresholds and the 5 s window are in the Methods; the trimming is in the code.
- `bad_405` ports the movement-artifact detection of exclusionCriteria_allFigs.m (noise from a
  10-bin sliding average, its 99.5th percentile as the noise ceiling, values above three times
  the ceiling, or above it for 0.2 s or longer, removed with 0.1 s on each side; a recording
  with more than 5% removed is excluded). The code also marks everything from the last noisy
  section to the end, and from the start to the first, which the Methods do not mention; it is
  kept here, as it decides which recordings pass.
- `crosscorr` is MATLAB's crosscorr (biased estimate, positive lags meaning the second series
  follows the first), `fastsmooth` is the sliding average of fastsmooth.m (Tom O'Haver) with
  zero ends, `select_acc_dec` ports selectAccDec of selectSignals_paper.m and
  AccDecSizeAnalysis.m (accelerations between zero crossings, longer than 0.05 s, peaks beyond
  2 m/s2, none other within 0.25 s).
- The minimum signal-to-noise ratio of 10, the 0.1 limit on the 405 nm cross-correlation with
  acceleration, the 100 s of running, the 1 s lag window and the 0.5 s response windows are in
  the Methods. The signal-to-noise ratios and the 405 nm cross-correlation maxima are read from
  the files (columns `signal_to_noise_ratio` and `cross_correlation_with_acceleration`); the
  latter is recomputed here as a check.
- Response windows. The Methods integrate from +0.05 to +0.55 s after a stimulus minus -0.5 to
  0 s before it; the code integrates 0 to +0.5 s minus -0.55 to -0.05 s. Both are returned
  (`resp_methods`, `resp_code`).
"""

from __future__ import annotations

import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")   # many small computations in parallel processes

import gzip
import hashlib
import io
from concurrent.futures import ProcessPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
import requests

DANDISET_ID = "001038"
DANDISET_VERSION = "0.241111.1719"
API = "https://api.dandiarchive.org/api"
HZ = 100

# Subtype names: file prefix -> name in the paper
SUBTYPE = {"VGlut": "Vglut2", "Calb": "Calb1", "Raldh": "Aldh1a1", "Anxa": "Anxa1", "Dat": "DAT"}

SNR_MIN = 10.0            # Methods: signal-to-noise ratio greater than 10
ACC405_MAX = 0.1          # Methods: peak 405 nm cross-correlation with acceleration
RUN_MIN_S = 100.0         # Methods: at least 100 s of locomotion
RG405_MAX = 0.12          # Methods: dual recordings, peak 405/470 cross-correlation
LAG = 100                 # 1 s of lags at 100 Hz
NEG = POS = 105           # code: 1 s around triggers plus 5 bins for plotting edges
N_EVENTS_MIN = 3          # code (plotAverages_paper.m): more than 2 events for an average

# Response windows, in bins relative to the trigger (inclusive ends)
WIN_METHODS = {"base": (-50, 0), "resp": (5, 55)}
WIN_CODE = {"base": (-55, -5), "resp": (0, 50)}


# ---------------------------------------------------------------- archive

def list_assets() -> pd.DataFrame:
    """Path, S3 URL, subject and genotype of every asset at the pinned version."""
    url = (f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/"
           "?metadata=true&page_size=1000")
    rows = []
    while url:
        r = requests.get(url, timeout=120)
        r.raise_for_status()
        page = r.json()
        url = page["next"]
        for a in page["results"]:
            md = a["metadata"]
            s3 = [u for u in md["contentUrl"] if "s3.amazonaws.com" in u][0]
            subj = (md.get("wasAttributedTo") or [{}])[0]
            rows.append({"path": a["path"], "url": s3, "size": a["size"],
                         "subject": subj.get("identifier"), "genotype": subj.get("genotype")})
    return pd.DataFrame(rows).sort_values("path").reset_index(drop=True)


def _s(x):
    return x.decode() if isinstance(x, bytes) else x


# ---------------------------------------------------------------- MATLAB ports

def mround(x):
    """MATLAB round (half away from zero) for non-negative values."""
    return int(np.floor(x + 0.5))


def fastsmooth(y, w):
    """Sliding average of width w with zero ends (fastsmooth.m, type 1, ends 0)."""
    y = np.asarray(y, float)
    L = len(y)
    w = mround(w)
    out = np.zeros(L)
    if L < w:
        return out
    halfw = mround(w / 2)
    c = np.concatenate([[0.0], np.cumsum(y)])
    sums = c[w:] - c[:-w]                       # sums[m] = sum(y[m:m+w]), m = 0..L-w
    out[halfw - 1: halfw - 1 + len(sums)] = sums
    return out / w


def smooth_keep_ends(y, w=5):
    """fastsmooth with the zero ends replaced by the input, as the code does after smoothing."""
    s = fastsmooth(y, w)
    s[s == 0] = np.asarray(y, float)[s == 0]
    return s


def matlab_smooth(y, span=6):
    """MATLAB smooth(y, span), moving average; an even span is reduced by one, ends shrink."""
    y = np.asarray(y, float)
    if span % 2 == 0:
        span -= 1
    h = span // 2
    L = len(y)
    i = np.arange(L)
    k = np.minimum(np.minimum(h, i), L - 1 - i)
    c = np.concatenate([[0.0], np.cumsum(y)])
    return (c[i + k + 1] - c[i - k]) / (2 * k + 1)


def crosscorr(x, y, lags):
    """MATLAB crosscorr(x, y, lags): r(k) = cov(x_t, y_{t+k}) / (sd_x sd_y), biased."""
    x = np.asarray(x, float) - np.mean(x)
    y = np.asarray(y, float) - np.mean(y)
    T = len(x)
    den = np.sqrt(np.dot(x, x) * np.dot(y, y))
    out = np.empty(2 * lags + 1)
    for k in range(-lags, lags + 1):
        if k >= 0:
            out[k + lags] = np.dot(x[:T - k], y[k:])
        else:
            out[k + lags] = np.dot(y[:T + k], x[-k:])
    return out / den


def zero_x(y):
    """ZeroX.m: indices (0-based) of the samples closest to each zero crossing."""
    y = np.asarray(y, float)
    zi = np.where(y * np.roll(y, -1) <= 0)[0]
    zi = zi[zi + 1 < len(y)]                      # the code drops the wrap-around pair
    zc = np.where(np.abs(y[zi]) < np.abs(y[zi + 1]), zi, zi + 1)
    return np.unique(zc).astype(int)


def double_thresh_updown(v, t1=0.0237, t2=0.0101):
    """double_thresh_updown.m: 1 while moving, entering above t1 and leaving below t2."""
    v = np.asarray(v, float)
    st = np.zeros(len(v), dtype=np.int8)
    s = 0 if (-t2 < v[0] < t2) else 1
    st[0] = s
    above1 = (v > t1) | (v < -t1)
    below2 = (v < t2) & (v > -t2)
    for i in range(1, len(v)):
        if s == 0:
            if above1[i]:
                s = 1
        elif below2[i]:
            s = 0
        st[i] = s
    return st


def mov_on_off(vel):
    """MovOnOff of selectSignals_paper.m: 0 at rest (at least 0.5 s still), 1 otherwise."""
    pre = double_thresh_updown(vel)
    L = len(pre)
    st = pre.copy()
    s5 = np.convolve(pre, np.ones(5, dtype=int), mode="same")
    iso = (pre == 1) & (s5 == 1)
    iso[:2] = False
    iso[L - 2:] = False
    st[iso] = 0                                   # single-bin "movements"
    out = np.ones(L, dtype=np.int8)
    ones = np.where(st == 1)[0]
    if len(ones) == 0:
        return np.zeros(L, dtype=np.int8)
    f = ones[0]
    if f != 0:
        out[:f] = 0                               # 1-based out(1:firstRun-1)
        start0 = f - 1
    else:
        start0 = 0
    last = ones[-1]
    out[last + 1:] = 0
    stop1 = min(last + 2, L - 50)                 # 1-based lastRun
    T = 50
    c = np.concatenate([[0], np.cumsum(st)])
    starts = np.arange(start0, stop1)             # 0-based timeBin
    starts = starts[starts + T + 1 <= L]
    ok = starts[(c[starts + T + 1] - c[starts]) == 0]
    if len(ok):
        mark = np.zeros(L + 1, dtype=int)
        np.add.at(mark, ok, 1)
        np.add.at(mark, ok + T + 1, -1)
        out[np.cumsum(mark)[:L] > 0] = 0
    return out


def run_mask(vel, movonoff, stim):
    """Run of selectSignals_paper.m: strict running bouts, without 5 s after stimuli.

    `stim` is a boolean array marking every sample of consumed rewards, air puffs and lights.
    """
    L = len(vel)
    m = np.asarray(movonoff, int)
    d = np.diff(m)
    on1 = np.where(d == 1)[0] + 1                  # 1-based onset indices (last rest bin)
    off1 = np.concatenate([np.where(d == -1)[0] + 1, [L]])
    mark = np.zeros(L + 1)
    for o in on1:
        later = off1[off1 > o]
        if not len(later):
            continue
        f = later[0]
        if np.nanmean(vel[o - 1:f]) > 0.2 and (f - o) > 50:
            mark[o + 10 - 1] = 1                  # Run(on+10) = 1
            if f - 10 - 1 < L:
                mark[f - 10 - 1] = -1             # Run(off-10) = -1
    run = np.cumsum(mark[:L]) > 0
    idx = np.where(stim)[0]
    if len(idx):
        block = np.zeros(L + 1, dtype=int)
        np.add.at(block, idx, 1)
        np.add.at(block, np.minimum(idx + 501, L), -1)
        run &= ~(np.cumsum(block[:L]) > 0)
    return run


def bad_405(iso):
    """Bad405G of exclusionCriteria_allFigs.m: samples with movement artifacts in 405 nm.

    Returns the boolean mask and whether more than 5% of the recording is marked. The scale
    of the trace does not matter, so the normalized trace is used.
    """
    x = np.asarray(iso, float).copy()
    L = len(x)
    nan = np.where(np.isnan(x))[0]
    if len(nan):
        nxt = np.minimum(nan + 1, L - 1)
        x[nan] = x[nxt]
        x[np.isnan(x)] = 0.0
    sm = fastsmooth(x, 10)
    noise = np.sort(np.abs(x - sm))
    max_noise = noise[mround(L * (1 - 0.005)) - 1]
    very = (x > 3 * max_noise) | (x < -3 * max_noise)
    bad = ((x > max_noise) | (x < -max_noise)).astype(int)
    d = np.diff(bad)
    on = np.where(d == 1)[0] + 1                  # 1-based, as in the code
    off = np.where(d == -1)[0] + 1
    if len(on) and len(off):
        if on[0] < off[0] and len(on) == len(off):
            pass
        elif on[0] < off[0] and len(on) > len(off):
            on = on[:-1]
        elif on[0] > off[0] and len(on) < len(off):
            off = off[1:]
        elif on[0] > off[0] and len(on) == len(off):
            off = off[1:]
            on = on[:-1]
        if len(on) and len(off):
            if on[-1] <= L - 20:
                very[on[-1] - 1:] = True
            if off[0] >= 20:
                very[:off[0]] = True
            n = min(len(on), len(off))
            dur = off[:n] - on[:n]
            for i in np.where(dur >= 20)[0]:
                a = max(on[i] - 10, 1)
                b = min(off[i] + 10, L)
                very[a - 1:b] = True
    return very, bool(very.mean() > 0.05)


def select_acc_dec(acc, acc_min=2.0):
    """selectAccDec: onsets (0-based) and peak values of isolated accelerations/decelerations."""
    acc = np.asarray(acc, float)
    L = len(acc)
    on = zero_x(acc)
    on = on[1:] if len(on) else on               # accOn(1) = []
    dur = np.concatenate([np.diff(on), [np.nan]])
    is_acc = np.zeros(L, bool)
    is_dec = np.zeros(L, bool)
    peaks = np.full(L, np.nan)
    remove = np.zeros(L, bool)
    for i in range(len(on) - 1):
        if dur[i] > 5:
            seg = acc[on[i]:on[i + 1] + 1]
            pv = seg[np.argmax(np.abs(seg))]
            if pv > acc_min:
                is_acc[on[i]] = True
                peaks[on[i]] = pv
            elif pv < -acc_min:
                is_dec[on[i]] = True
                peaks[on[i]] = pv
            if abs(pv) > 2:
                remove[on[i]] = True
    # drop events with another large one within 25 bins on either side
    c = np.concatenate([[0], np.cumsum(remove)])
    idx = np.arange(L)
    lo = np.maximum(idx - 25, 0)
    hi = np.minimum(idx + 25, L - 1)
    near = (c[hi + 1] - c[lo]) - remove.astype(int)
    keep = near == 0
    return is_acc & keep, is_dec & keep, peaks


def exclude_after(mask, stim, win=500):
    """excludeRew: zero `mask` from every stimulus sample to 5 s after it."""
    out = mask.copy()
    idx = np.where(stim)[0]
    if len(idx):
        L = len(mask)
        block = np.zeros(L + 1, dtype=int)
        np.add.at(block, idx, 1)
        np.add.at(block, np.minimum(idx + win + 1, L), -1)
        out[np.cumsum(block[:L]) > 0] = 0
    return out


# ---------------------------------------------------------------- events

def onsets(binary):
    """0-based indices where a binary trace turns on ([0; diff(sig)] > 0)."""
    b = np.asarray(binary, float)
    b[b < 0] = 0
    return np.where(np.concatenate([[0.0], np.diff(b)]) > 0)[0]


def triggered(trace, binary, neg=NEG, pos=POS):
    """Snippets of `trace` around each onset of `binary` (alignSignals_paper.m).

    The trigger sits at column neg - 1 (0-based); onsets closer than neg or pos to the
    ends are dropped, as in the code.
    """
    idx = onsets(binary)
    idx1 = idx + 1
    idx = idx[(idx1 >= neg) & (idx1 <= len(binary) - pos)]
    if not len(idx):
        return np.empty((0, neg + pos))
    cols = np.arange(-neg + 1, pos + 1)
    return np.asarray(trace, float)[idx[:, None] + cols[None, :]]


def responses(snips, win):
    """Per-event integral after minus before the trigger, averaged (RewardPuffAnalysis.m)."""
    if snips.shape[0] == 0:
        return np.nan
    x = snips.copy()
    if np.isnan(x).any():
        shifted = np.roll(x, 1, axis=1)          # circshift(x, 1, 2), which wraps, as in the code
        x[np.isnan(x)] = shifted[np.isnan(x)]
    t0 = NEG - 1
    b = x[:, t0 + win["base"][0]: t0 + win["base"][1] + 1]
    r = x[:, t0 + win["resp"][0]: t0 + win["resp"][1] + 1]
    return float(np.nanmean(np.trapezoid(r, dx=1 / HZ, axis=1) - np.trapezoid(b, dx=1 / HZ, axis=1)))


def _size_amps(g, idx, peaks, desc):
    """Transient amplitude after the events of each quintile of event size (AccDecSizeAnalysis.m).

    Five values, NaN for a quintile with fewer than 3 events; None with fewer than 5 events.
    """
    if len(idx) < 5:
        return None
    L = len(g)
    vals = peaks[idx]
    srt = np.sort(vals)[::-1] if desc else np.sort(vals)
    n = len(srt)
    amps = []
    for q in range(5):
        lo = srt[mround(0.2 * q * n)]
        hi = srt[mround(0.2 * (q + 1) * n) - 1]
        if desc:
            sel = idx[(vals <= lo) & (vals >= hi)]
        else:
            sel = idx[(vals >= lo) & (vals <= hi)]
        b = np.zeros(L, bool)
        b[sel] = True
        sn = triggered(g, b, 100, 100)
        if sn.shape[0] >= N_EVENTS_MIN:
            avg = smooth_keep_ends(np.nanmean(sn, 0), 5)
            up = np.max(avg[99:]) - avg[99]
            dn = np.min(avg[99:]) - avg[99]
            amps.append(up if abs(up) >= abs(dn) else dn)
        else:
            amps.append(np.nan)
    return amps


# ---------------------------------------------------------------- one file

def _intervals(f, kind):
    """Start and stop sample indices of Events rows of one type, with their tags."""
    if "Events" not in f["processing/behavior"]:
        return []
    e = f["processing/behavior/Events"]
    et = np.array([_s(x) for x in e["event_type"][()]])
    st, sp = e["start_time"][()], e["stop_time"][()]
    tags = [_s(x) for x in e["tags"][()]]
    ti = e["tags_index"][()]
    out = []
    for i in np.where(et == kind)[0]:
        tg = tags[(ti[i - 1] if i else 0):ti[i]]
        out.append((st[i], sp[i], tuple(tg)))
    return out


def _binary(L, t0, ivals, shift=0):
    b = np.zeros(L, bool)
    for s, e, _ in ivals:
        a = int(round((s - t0) * HZ)) + shift
        z = int(round((e - t0) * HZ)) + shift
        b[max(a, 0):min(z + 1, L)] = True
    return b


def _fiber_rows(f):
    """Per fiber (column of the dF/F series): table row, device name and table values."""
    t = f["general/FiberPhotometry/FiberPhotometryTable"]
    path = "processing/ophys/DfOverFFiberPhotometryResponseSeries/fiber_photometry_table_region"
    if path in f:
        reg = f[path][()]
    elif "FiberPhotometryResponseSeries" in f["acquisition"]:
        reg = f["acquisition/FiberPhotometryResponseSeries/fiber_photometry_table_region"][()]
    else:
        n = f["processing/ophys/DfOverFFiberPhotometryResponseSeries/data"].shape
        reg = np.arange(n[1] if len(n) > 1 else 1)
    reg = np.atleast_1d(reg)
    coords = t["coordinates"][()]
    out = []
    for col, i in enumerate(reg):
        ref = t["optical_fiber"][i]
        dev = f[ref].name.split("/")[-1] if isinstance(ref, h5py.Reference) else _s(ref)
        out.append({"col": col, "row": int(i), "device": dev,
                    "location": _s(t["location"][i]), "target": _s(t["recording_target_type"][i]),
                    "depth": float(t["fiber_depth_in_mm"][i]), "snr": float(t["signal_to_noise_ratio"][i]),
                    "acc405_file": float(t["cross_correlation_with_acceleration"][i]),
                    "norm": np.atleast_1d(t["normalized_fluorescence"][i]).astype(float).tolist(),
                    "base": np.atleast_1d(t["baseline_fluorescence"][i]).astype(float).tolist(),
                    "coord": [float(v) for v in np.atleast_1d(coords[i])] if coords.ndim > 1 else [float(coords[i])] * 3})
    return out


def read_file(asset: dict) -> dict:
    """Open one file and compute every per-recording measure the notebook uses.

    The full traces are reduced here, in the worker, to per-recording values, triggered
    averages and per-event values; the notebook never holds the traces of all files.
    """
    last = None
    for _ in range(4):
        try:
            with h5py.File(remfile.File(asset["url"]), "r") as f:
                return _read(f, asset)
        except OSError as e:          # network hiccup: retry
            last = e
    raise RuntimeError(f"could not read {asset['path']}: {last}")


def _read(f, asset):
    rec = {"path": asset["path"], "subject": _s(f["general/subject/subject_id"][()]),
           "sex": _s(f["general/subject/sex"][()]), "genotype": _s(f["general/subject/genotype"][()]),
           "age": _s(f["general/subject/age"][()]), "session_id": _s(f["general/session_id"][()]),
           "start": _s(f["session_start_time"][()])}
    rec["prefix"] = asset["path"].split("/")[0].split("-")[1]
    fibers = _fiber_rows(f)
    rec["fibers"] = fibers
    rec["has_events"] = "Events" in f["processing/behavior"]
    good = [fb for fb in fibers if fb["snr"] > SNR_MIN]
    rec["loaded"] = bool(good)
    if not good:
        return rec

    dset = f["processing/ophys/DfOverFFiberPhotometryResponseSeries"]
    t0 = float(dset["starting_time"][()])
    dff = dset["data"][()]
    iso = f["processing/ophys/DfOverFFiberPhotometryResponseSeriesIsosbestic/data"][()]
    iso = iso[:, None] if iso.ndim == 1 else iso
    dff = dff[:, None] if dff.ndim == 1 else dff
    vel = f["processing/behavior/Velocity/data"][()]
    acc = f["processing/behavior/Acceleration/data"][()]
    L = len(vel)
    rec["n_samples"] = L
    rec["t0"] = t0
    rec["vel_range"] = (float(np.nanmin(vel)), float(np.nanmax(vel)))
    rec["acc_range"] = (float(np.nanmin(acc)), float(np.nanmax(acc)))
    rec["dff_max"] = [float(np.nanmax(dff[:, c])) for c in range(dff.shape[1])]
    rec["dff_nan"] = [float(np.isnan(dff[:, c]).mean()) for c in range(dff.shape[1])]
    rec["vel_hash"] = hashlib.md5(np.ascontiguousarray(vel).tobytes()).hexdigest()
    rec["dff_hash"] = [hashlib.md5(np.ascontiguousarray(dff[:, c]).tobytes()).hexdigest() for c in range(dff.shape[1])]
    # data checks: acceleration from velocity, as data_processing.m computes it
    acc_re = np.concatenate([[0.0], np.diff(matlab_smooth(vel, 6)) * HZ])
    rec["acc_check_maxabs"] = float(np.nanmax(np.abs(acc_re - acc)))

    # events
    rew_ls = _intervals(f, "Reward")
    longs = [x for x in rew_ls if "long" in x[2]]
    shorts = [x for x in rew_ls if "short" in x[2]]
    rests = [x for x in rew_ls if "rest" in x[2] and "long" not in x[2] and "short" not in x[2]]
    puffs = _intervals(f, "AirPuff")
    lights = _intervals(f, "Light")
    licks = _intervals(f, "Licking")
    movs = _intervals(f, "MovOnOff")
    rew_long = _binary(L, t0, longs)
    rew_short = _binary(L, t0, shorts)
    reward = _binary(L, t0, longs + shorts, shift=1)      # 'Reward' starts one bin later
    # RewardLong and RewardShort stay one bin before Reward, as selectSignals_paper.m sets them
    # at find(diff(Reward) == 1); the rest rows already sit on Reward's bins
    rew_rest = _binary(L, t0, rests)
    puff = _binary(L, t0, puffs)
    light = _binary(L, t0, lights)
    lick = _binary(L, t0, licks)
    rec["n_events"] = {"reward": len(longs) + len(shorts), "long": len(longs), "short": len(shorts),
                       "rest": len(rests), "airpuff": len(puffs), "light": len(lights), "lick": len(licks)}
    if rests:
        # rest rows against the consumed rewards they tag: durations, start offsets, and the
        # onsets left in RewardNoRest (reward & ~rest, as RewardPuffAnalysis.m builds it)
        rs = np.array([x[0] for x in rests])
        ls = np.array([x[0] for x in longs + shorts])
        j = np.abs(ls[None, :] - rs[:, None]).argmin(1)
        rec["rest_check"] = {
            "rewards": len(onsets(reward)), "rest": len(onsets(rew_rest)),
            "norest": len(onsets(reward & ~rew_rest)),
            "rest_outside_reward": int((rew_rest & ~reward).sum()),
            "start_offset_s": [float(v) for v in rs - ls[j]],
            "dur_rest_s": [float(x[1] - x[0]) for x in rests],
            "dur_reward_s": [float((longs + shorts)[i][1] - (longs + shorts)[i][0]) for i in j]}
    stim = reward | puff | light

    # movement and running, recomputed from velocity
    movonoff = mov_on_off(vel)
    if movs:
        stored = _binary(L, t0, movs)
        rec["movonoff_agree"] = float((stored == movonoff.astype(bool)).mean())
    run = run_mask(vel, movonoff, stim)
    rec["time_run"] = float(run.sum() / HZ)

    # wheel events stored in the file, and recomputed
    wacc = np.zeros(L, bool)
    wdec = np.zeros(L, bool)
    if "WheelEvents" in f["processing/behavior"]:
        we = f["processing/behavior/WheelEvents"]
        names = [_s(x) for x in f["processing/behavior/WheelEventTypes/event_name"][()]]
        ts, ty = we["timestamp"][()], we["event_type"][()]
        for t, k in zip(ts, ty):
            i = int(round((t - t0) * HZ))
            if 0 <= i < L:
                (wacc if names[k].startswith("Acc") else wdec)[i] = True
    a_re, d_re, peaks = select_acc_dec(acc)
    a_re = exclude_after(a_re, stim)
    d_re = exclude_after(d_re, stim)
    rec["wheel_check"] = {"acc_file": int(wacc.sum()), "dec_file": int(wdec.sum()),
                          "acc_re": int(a_re.sum()), "dec_re": int(d_re.sum()),
                          "acc_both": int((wacc & a_re).sum()), "dec_both": int((wdec & d_re).sum())}

    # clock check: licking and acceleration around consumed rewards, true and shifted times
    if reward.any():
        ron = onsets(reward)
        rng = np.random.default_rng(len(ron) * 7919 + L)
        shift = rng.integers(500, 1500, size=len(ron)) * rng.choice([-1, 1], size=len(ron))

        def contrast(idx, x):
            idx = idx[(idx >= 100) & (idx < L - 100)]
            if not len(idx):
                return np.nan
            return float(np.mean([x[i:i + 100].mean() - x[i - 100:i].mean() for i in idx]))
        rec["clock"] = {"lick_true": contrast(ron, lick.astype(float)),
                        "lick_shift": contrast(ron + shift, lick.astype(float)),
                        "acc_true": contrast(ron, acc), "acc_shift": contrast(ron + shift, acc)}

    out = []
    for fb in fibers:
        if fb["snr"] <= SNR_MIN:
            continue
        c = fb["col"]
        g, g405 = dff[:, c], iso[:, c]
        r = dict(fb)
        bad, bad_all = bad_405(g405)
        r["bad_frac"] = float(bad.mean())
        r["bad_all"] = bad_all
        # 405 nm cross-correlation with acceleration over running, as exclusionCriteria does
        if rec["time_run"] > RUN_MIN_S:
            ok = ~(np.isnan(g405) | np.isnan(acc))
            sel = ok & run
            r["acc405_re"] = float(np.max(np.abs(crosscorr(acc[sel], g405[sel], 50))))
        else:
            r["acc405_re"] = np.nan
        # remove the artifact samples from every series, as the analysis scripts do
        keep = ~bad
        G, G405, A, V = g[keep], g405[keep], acc[keep], vel[keep]
        RUN = run[keep]
        ser = {"Reward": reward[keep], "RewardShort": rew_short[keep], "RewardLong": rew_long[keep],
               "RewardRest": rew_rest[keep], "AirPuff": puff[keep], "Light": light[keep],
               "RewardNoRest": (reward & ~rew_rest)[keep],
               "AccOn": wacc[keep], "DecOn": wdec[keep]}
        # cross-correlation with acceleration over running (crossCorr2.m)
        if RUN.sum() > 2 * LAG:
            okn = ~(np.isnan(G) | np.isnan(G405) | np.isnan(A))
            runk = RUN & okn
            cc = crosscorr(A[runk], G[runk], LAG)
            cc4 = crosscorr(A[runk], G405[runk], LAG)
            r["cc470"] = smooth_keep_ends(cc, 5)
            r["cc405"] = smooth_keep_ends(cc4, 5)
        # triggered averages on accelerations and decelerations (code: AccOn / DecOn)
        for name in ("AccOn", "DecOn"):
            sn = triggered(G, ser[name])
            r[f"n_{name}"] = sn.shape[0]
            if sn.shape[0] >= N_EVENTS_MIN:
                r[f"avg_{name}"] = smooth_keep_ends(np.nanmean(sn, 0), 5)
                d = sn[:, NEG - 1:NEG - 1 + 76] - sn[:, [NEG - 1]]
                integ = np.trapezoid(d, dx=1 / HZ, axis=1)
                r[f"pos_{name}"] = float((integ > 0).mean() * 100)
        # stimulus responses
        if rec["has_events"]:
            for name in ("Reward", "AirPuff", "RewardShort", "RewardLong", "RewardRest", "RewardNoRest"):
                sn = triggered(G, ser[name])
                r[f"n_{name}"] = sn.shape[0]
                if sn.shape[0] >= N_EVENTS_MIN:
                    r[f"resp_methods_{name}"] = responses(sn, WIN_METHODS)
                    r[f"resp_code_{name}"] = responses(sn, WIN_CODE)
                    if name in ("Reward", "AirPuff"):
                        r[f"avg_{name}"] = smooth_keep_ends(np.nanmean(sn, 0), 5)
        # acceleration size (AccDecSizeAnalysis.m): no artifact removal there. The code
        # excludes 5 s after every reward, consumed or not; the stored onsets carry that
        # exclusion, so `size_amps` uses the recomputed onsets that are also stored, and
        # `size_amps_all` every recomputed onset (only consumed rewards excluded).
        r["size_amps"] = {"acc": _size_amps(g, np.where(a_re & wacc)[0], peaks, False),
                          "dec": _size_amps(g, np.where(d_re & wdec)[0], peaks, True)}
        r["size_amps_all"] = {"acc": _size_amps(g, np.where(a_re)[0], peaks, False),
                              "dec": _size_amps(g, np.where(d_re)[0], peaks, True)}
        out.append(r)
    rec["good_fibers"] = out

    # simultaneous SNc and striatum (SNcVsStrAnalysis.m)
    if len(fibers) == 2 and all(fb["snr"] > SNR_MIN for fb in fibers):
        tg = [fb["target"] for fb in fibers]
        if sorted(tg) == ["axons in striatum", "cell bodies in SNc"]:
            s = tg.index("cell bodies in SNc")
            k = 1 - s
            bs, bas = bad_405(iso[:, s])
            bk, bak = bad_405(iso[:, k])
            G1, R1, G1i, R1i = dff[:, s], dff[:, k], iso[:, s], iso[:, k]
            ok = ~(np.isnan(G1) | np.isnan(R1) | np.isnan(G1i) | np.isnan(R1i))
            # RG405 is computed before artifact removal in exclusionCriteria_allFigs.m
            c1 = crosscorr(R1i[ok], G1[ok], 50)
            c2 = crosscorr(R1[ok], G1i[ok], 50)
            rg405 = float(np.max(np.abs((c1 + c2) / 2)))
            keep = ~(bs | bk) & ok
            cc = smooth_keep_ends(crosscorr(G1[keep], R1[keep], LAG), 5)
            cci = smooth_keep_ends((crosscorr(G1[keep], R1i[keep], LAG) + crosscorr(G1i[keep], R1[keep], LAG)) / 2, 5)
            rec["dual"] = {"rg405": rg405, "bad_any": bool(bas or bak), "cc": cc, "cc405": cci,
                           "peak": float(np.max(cc))}
    return rec


def load_all(assets: pd.DataFrame, workers: int = 16) -> list[dict]:
    """Read every file in parallel processes (h5py serializes calls within a process)."""
    items = assets.to_dict("records")
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(read_file, items, chunksize=2))


# ---------------------------------------------------------------- tables

def recordings_table(recs: list[dict]) -> pd.DataFrame:
    """One row per fiber of every file, with the selection flags of the paper's code."""
    rows = []
    for rec in recs:
        good = {g["col"]: g for g in rec.get("good_fibers", [])}
        for fb in rec["fibers"]:
            row = {k: rec[k] for k in ("path", "subject", "sex", "prefix", "session_id", "has_events")}
            row.update({k: fb[k] for k in ("col", "device", "location", "target", "depth", "snr",
                                           "acc405_file", "norm", "coord")})
            row["subtype"] = SUBTYPE.get(rec["prefix"], rec["prefix"])
            row["time_run"] = rec.get("time_run", np.nan)
            g = good.get(fb["col"])
            row["passes_snr"] = fb["snr"] > SNR_MIN
            if g is not None:
                for k, v in g.items():
                    if k not in row:
                        row[k] = v
            rows.append(row)
    df = pd.DataFrame(rows)
    df["mouse"] = df.subject.str.rstrip("L")
    df["striatum"] = df.target == "axons in striatum"
    df["snc"] = df.target == "cell bodies in SNc"
    df["ml"] = df.coord.map(lambda c: c[0])
    df["ap"] = df.coord.map(lambda c: c[1])
    df["dv"] = df.coord.map(lambda c: c[2])
    # locomotion selection (LocomotionAnalysis.m): SNR, 405 cross-correlation, running, artifacts
    df["loco"] = (df.passes_snr & (df.acc405_file < ACC405_MAX) & (df.time_run > RUN_MIN_S)
                  & (df.get("bad_all") == False))  # noqa: E712
    # stimulus selection (RewardPuffAnalysis.m): SNR and a session with stimuli
    df["stim"] = df.passes_snr & df.has_events
    return df


# ---------------------------------------------------------------- PCA as MATLAB does it

def pca_uncentered(X):
    """pca(X, 'Centered', false): loadings with MATLAB's sign convention, % variance."""
    U, S, Vt = np.linalg.svd(X, full_matrices=False)
    coeff = Vt.T
    big = np.argmax(np.abs(coeff), axis=0)
    sign = np.sign(coeff[big, np.arange(coeff.shape[1])])
    coeff = coeff * sign
    explained = S ** 2 / np.sum(S ** 2) * 100
    return coeff, explained


# ---------------------------------------------------------------- snRNA-seq (GEO GSE222558)

GEO_SAMPLES = {
    "M2": "https://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6926nnn/GSM6926026/suppl/GSM6926026_SampleM2",
    "F2": "https://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6926nnn/GSM6926027/suppl/GSM6926027_SampleF2",
}


def load_geo_counts(genes=("Anxa1", "Aldh1a1", "Slc6a3", "Th")):
    """Per nucleus: number of detected genes, UMI count and counts of a few genes.

    Streams the 10x matrices of the two samples of GSE222558 into memory.
    """
    out = []
    for name, base in GEO_SAMPLES.items():
        feats = pd.read_csv(io.BytesIO(requests.get(base + "_features.tsv.gz", timeout=600).content),
                            sep="\t", header=None, compression="gzip")
        bars = pd.read_csv(io.BytesIO(requests.get(base + "_barcodes.tsv.gz", timeout=600).content),
                           header=None, compression="gzip")
        raw = requests.get(base + "_matrix.mtx.gz", timeout=1200).content
        with gzip.open(io.BytesIO(raw)) as fh:
            m = pd.read_csv(fh, sep=" ", comment="%", header=None, names=["g", "c", "v"],
                            dtype={"g": np.int32, "c": np.int32, "v": np.int32})
        shape = m.iloc[0]
        m = m.iloc[1:]
        n_cells = int(shape["c"])
        n_feat = np.bincount(m.c.values - 1, minlength=n_cells)
        n_umi = np.bincount(m.c.values - 1, weights=m.v.values, minlength=n_cells)
        df = pd.DataFrame({"sample": name, "barcode": bars[0].values, "n_features": n_feat, "n_umi": n_umi})
        sym = feats[1].values
        for gname in genes:
            gi = np.where(sym == gname)[0]
            col = np.zeros(n_cells)
            if len(gi):
                sel = m.g.values == gi[0] + 1
                np.add.at(col, m.c.values[sel] - 1, m.v.values[sel])
            df[gname] = col
        df.attrs["n_genes"] = int(shape["g"])
        out.append(df)
    return pd.concat(out, ignore_index=True)
