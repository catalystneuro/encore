"""Loading and measures for CRCNS hc-28 (Jadhav & Frank), used to test Jadhav, Rothschild, Roumis
& Frank (2016), Neuron 90:113-127, doi:10.1016/j.neuron.2016.02.010.

The data set holds three rats (HPa, HPb, HPc) on the W-track, days 1 to 8, as one tar.gz per
animal in the public bucket crcnsarchive (hc-28/live/data/). Each archive is streamed once and
read in memory; nothing is written to disk. Inside, MATLAB files hold nested cells
{day}{epoch}{tetrode}{unit} (data descriptor, "Data organization").

Where the parameters come from (claims file = claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml,
SEP = the paper's Supplemental Experimental Procedures):

- Epochs. Awake SWRs are those of run epochs on the W-track (claims file, opening comment). The
  task files name W-track runs 'wtr1' and, on days 6 to 8, 'wtr2'; the paper pools "all sessions
  within a day" and says the animals "performed 2 sessions on the W-track every day for a total
  of 8 days" (SEP, Behavioral Tasks), so both W-track runs of a day are used. The linear-track run
  of day 1 ('lin') is not a W-track session and is left out. Pre-rest is the rest epoch before
  the day's first run (claims file; SEP, Task and rest period comparisons), epoch 1 of each day.
- SWR detection (SEP, SWR Detection): ripple band 150-250 Hz on the CA1 ripple tetrodes (marked
  'riptet' in tetinfo; in HPa and HPb these include intermediate-CA1 tetrodes), 3 SD power criterion, speed < 4 cm/s, SWRs within 1 s of a previously
  detected SWR discarded. Not given by the paper (standard choices of the cited Karlsson & Frank
  2009 lab practice, stated as assumptions in the notebook): a 4th-order Butterworth band-pass
  applied forward and back, the Hilbert envelope smoothed with a Gaussian of SD 4 ms, mean and SD
  over the epoch, at least 15 ms above threshold, event bounds extended to where the envelope
  returns to its mean. Reading (a) of the claims file: an event on any one ripple tetrode (the
  SEP's theta periods exclude "SWRs detected on any of the CA1 tetrodes with a 3 s.d.
  criterion"); reading (b): the mean of the tetrodes' z-scored envelopes crosses 3 SD; reading
  'dca1': an event on any one dorsal-CA1 ripple tetrode (the paper detects SWRs "on multiple CA1
  tetrodes" and names intermediate CA1 apart).
- Theta (SEP, Theta Phase Locking): LFP of the CA1 reference tetrode ('CA1Ref' in tetinfo, the
  tetrode in the corpus callosum) down-sampled to 150 Hz and filtered 6-12 Hz; theta periods at
  speed > 5 cm/s outside any SWR detected on any CA1 ripple tetrode at 3 SD (regardless of
  speed). A 3rd-order Butterworth band-pass applied forward and back and the Hilbert phase
  (0 deg at the peak, 180 deg at the trough) are standard choices (claims file). A spike's phase is
  interpolated linearly on the unwrapped phase between the 150 Hz samples (standard choice).
- Units (SEP, SWR Modulation): fast-spiking cells excluded (width < 0.3 ms and rate > 17 Hz in
  PFC, > 7 Hz in CA1); the width is tetinfo/cellinfo 'spikewidth' in 30 kHz samples, divided by
  30 (the data descriptor says ms for cellinfo; the values are samples, see the notebook). The
  rate is the cell's spike count over the duration of the day's W-track run epochs (a standard
  choice). A unit is a cell on one day, sessions pooled (reading a of the claims file).
- Rate maps: the wtr2 runs of days 6 to 8 are on a different track, so each environment has bins of
  its own. Replay (SEP, Replay analysis): see the constants and docstrings near the end.
"""

from __future__ import annotations

import io
import os
import tarfile

import fsspec
import numpy as np
import scipy.io as sio
from scipy.ndimage import gaussian_filter1d
from scipy.signal import butter, hilbert, resample_poly, sosfiltfilt

DATASET, VERSION = "hc-28", "unversioned"   # CRCNS data sets are not versioned (docs/archives.md)
BUCKET = "https://crcnsarchive.s3-us-west-2.amazonaws.com/hc-28/live/data/"
ANIMALS = ["HPa", "HPb", "HPc"]
# MD5 sums from hc-28/live/checksums.md5 (the data set is unversioned)
MD5 = {"HPa": "ca6a313b9936db3aff62f60597da34a3", "HPb": "2126599d004cdaca2fa2426f364453e3",
       "HPc": "f9bddd6fe2c5c9c9dd0e406df1cf7ede"}

RIPPLE_BAND = (150.0, 250.0)   # SEP, SWR Detection
SWR_SD = 3.0                   # SEP
SWR_MAX_SPEED = 4.0            # cm/s, SEP
SWR_MIN_GAP = 1.0              # s, SEP
ENV_SMOOTH_SD = 0.004          # s, assumption (Frank-lab practice)
MIN_SUPRA = 0.015              # s, assumption (Frank-lab practice)
THETA_BAND = (6.0, 12.0)       # SEP
THETA_FS = 150.0               # SEP
THETA_SPEED = 5.0              # cm/s, SEP


# ---------------------------------------------------------------- MATLAB helpers
def _mat(b):
    d = sio.loadmat(io.BytesIO(b), squeeze_me=False, struct_as_record=False)
    return [v for k, v in d.items() if not k.startswith("__")][0]


def _cells(x):
    if isinstance(x, np.ndarray) and x.dtype == object:
        return list(x.ravel())
    return []


def _struct(x):
    """The struct in a 1x1 struct array, or None for an empty cell."""
    if isinstance(x, np.ndarray):
        if x.size == 0:
            return None
        x = x.ravel()[0]
    return x if hasattr(x, "_fieldnames") else None


def _str(s, f, default=""):
    if s is None or f not in s._fieldnames:
        return default
    v = getattr(s, f)
    if isinstance(v, np.ndarray):
        if v.dtype.kind == "U":
            return str(v[0]) if v.size else default
        if v.size == 1:
            return v.item()
    return v


def _num(s, f):
    v = _str(s, f, np.nan)
    return float(np.asarray(v, dtype=float).ravel()[0]) if np.size(v) else np.nan


def _meta(s):
    """Small fields of a struct (scalars and short strings), for the data check."""
    out = {}
    for f in s._fieldnames:
        v = getattr(s, f)
        if isinstance(v, np.ndarray) and v.dtype.kind == "U" and v.size:
            out[f] = str(v.ravel()[0])
        elif isinstance(v, np.ndarray) and v.dtype.kind in "iuf" and 0 < v.size <= 4:
            out[f] = v.ravel().astype(float).tolist()
    return out


# ---------------------------------------------------------------- streaming
def stream_members(animal, keep_eeg):
    """Stream the animal's archive once; return {file name: bytes} for the non-LFP files and for
    the LFP files whose (day, epoch, tetrode) `keep_eeg` accepts."""
    f = fsspec.open(BUCKET + f"{animal}_data.tar.gz", block_size=2**22).open()
    out = {}
    with tarfile.open(fileobj=f, mode="r|gz") as tf:
        for m in tf:
            if not m.isfile():
                continue
            name = os.path.basename(m.name)
            if "/EEG/" in m.name:
                d, e, t = (int(v) for v in name[len(animal) + 3:-4].split("-"))
                if not keep_eeg(d, e, t):
                    continue
            out[name] = tf.extractfile(m).read()
    f.close()
    return out


def _eeg(b):
    x = _mat(b)
    while _struct(x) is None:
        x = [c for c in _cells(x) if isinstance(c, np.ndarray) and c.size][-1]
    s = _struct(x)
    return float(_num(s, "starttime")), float(_num(s, "samprate")), np.asarray(s.data, dtype=np.float64).ravel()


# ---------------------------------------------------------------- SWR detection
def ripple_envelope(x, fs):
    sos = butter(4, RIPPLE_BAND, btype="band", fs=fs, output="sos")
    env = np.abs(hilbert(sosfiltfilt(sos, x)))
    return gaussian_filter1d(env, ENV_SMOOTH_SD * fs)


def detect_events(env, fs, sd=SWR_SD):
    """Events on one smoothed envelope: runs above mean + sd*SD lasting >= MIN_SUPRA, bounds
    extended to the mean. Returns arrays (start_ext, thr_cross, end_ext, peak) in samples."""
    mu, s = env.mean(), env.std()
    above = env > mu + sd * s
    edges = np.diff(np.r_[0, above.astype(np.int8), 0])
    st, en = np.flatnonzero(edges == 1), np.flatnonzero(edges == -1)
    ok = (en - st) >= MIN_SUPRA * fs
    st, en = st[ok], en[ok]
    base = env > mu
    bedges = np.diff(np.r_[0, base.astype(np.int8), 0])
    bst, ben = np.flatnonzero(bedges == 1), np.flatnonzero(bedges == -1)
    i = np.searchsorted(bst, st, side="right") - 1
    j = np.searchsorted(ben, en, side="left")
    sx = bst[np.clip(i, 0, None)]
    ex = ben[np.clip(j, 0, len(ben) - 1)]
    pk = np.array([a + np.argmax(env[a:b]) for a, b in zip(st, en)], dtype=int)
    return sx, st, ex, pk


def _merge(intervals):
    """Union of intervals given as rows (start_ext, thr, end_ext); merged on the extended bounds."""
    if len(intervals) == 0:
        return np.zeros((0, 3))
    iv = intervals[np.argsort(intervals[:, 0])]
    out = [iv[0].copy()]
    for r in iv[1:]:
        if r[0] <= out[-1][2]:
            out[-1][1] = min(out[-1][1], r[1])
            out[-1][2] = max(out[-1][2], r[2])
        else:
            out.append(r.copy())
    return np.array(out)


def swr_epoch(lfps, t0, fs, pos_t, pos_v, dorsal=None):
    """SWRs of one epoch from the ripple tetrodes' LFPs (equal length, common start t0).

    Returns a dict with, for each reading ('any', 'mean'), an array of rows
    (onset_ext, onset_thr, end_ext) in seconds of all detected events, and 'kept_any' /
    'kept_mean' boolean masks of the events passing the speed and 1 s rules. 'all_any' holds
    every event on any tetrode at any speed (used to exclude SWRs from theta periods)."""
    envs = [ripple_envelope(x, fs) for x in lfps]
    rows = []
    for env in envs:
        sx, st, ex, _ = detect_events(env, fs)
        rows.append(np.c_[sx, st, ex])
    any_ev = _merge(np.vstack(rows)) / fs + t0 if rows else np.zeros((0, 3))
    dors = rows if dorsal is None else [r for r, dd in zip(rows, dorsal) if dd]
    dca1_ev = _merge(np.vstack(dors)) / fs + t0 if dors else np.zeros((0, 3))
    z = np.mean([(e - e.mean()) / e.std() for e in envs], axis=0)
    sx, st, ex, _ = detect_events(z, fs)
    mean_ev = np.c_[sx, st, ex] / fs + t0
    out = {"all_any": any_ev, "n_per_tet": [len(r) for r in rows],
           "n_low_per_tet": [int(np.sum(np.interp(r[:, 1] / fs + t0, pos_t, pos_v) < SWR_MAX_SPEED)) for r in rows]}
    for key, ev in (("any", any_ev), ("dca1", dca1_ev), ("mean", mean_ev)):
        v = np.interp(ev[:, 1], pos_t, pos_v) if len(ev) else np.zeros(0)
        low = v < SWR_MAX_SPEED
        on = ev[low, 1]
        prev = np.r_[-np.inf, on[:-1]]
        keep_low = (on - prev) >= SWR_MIN_GAP
        keep = np.zeros(len(ev), bool)
        keep[np.flatnonzero(low)[keep_low]] = True
        out[key] = ev
        out["kept_" + key] = keep
    return out


def theta_phase(x, fs):
    """Theta phase (degrees, 0 at the peak) of an LFP down-sampled to 150 Hz; returns (t_rel, phase)."""
    q = int(round(fs / THETA_FS))
    y = resample_poly(x, 1, q)
    sos = butter(3, THETA_BAND, btype="band", fs=fs / q, output="sos")
    ph = np.degrees(np.angle(hilbert(sosfiltfilt(sos, y)))) % 360
    return np.arange(len(y)) / (fs / q), ph.astype(np.float32)


# ---------------------------------------------------------------- one animal
def _epoch_kinds(task_day):
    kinds = {}
    for e, t in enumerate(_cells(task_day), start=1):
        s = _struct(t)
        kinds[e] = (_str(s, "type"), _str(s, "environment"))
    return kinds


def reduce_animal(animal, members=None, days=range(1, 9)):
    """Stream one animal and reduce it to what the analyses use (see module docstring)."""
    if members is None:
        # Run epochs are the even epochs and pre-rest is epoch 1 in this data set; the task
        # files are read after the stream and the choice is checked below.
        members = stream_members(animal, lambda d, e, t: e == 1 or e % 2 == 0)
    tetinfo = _cells(_mat(members[f"{animal}tetinfo.mat"]))
    cellinfo = _cells(_mat(members[f"{animal}cellinfo.mat"]))
    res = {"animal": animal, "days": {}}
    for d in days:
        task = _epoch_kinds(_cells(_mat(members[f"{animal}task{d:02d}.mat"]))[d - 1])
        pos = _cells(_cells(_mat(members[f"{animal}pos{d:02d}.mat"]))[d - 1])
        spk = _cells(_cells(_mat(members[f"{animal}spikes{d:02d}.mat"]))[d - 1])
        tet_day = _cells(tetinfo[d - 1])
        runs = [e for e, (ty, env) in task.items() if ty == "run" and str(env).startswith("wtr")]
        pre = 1 if task[1][0] == "sleep" else None
        assert all(e % 2 == 0 for e in runs) and pre == 1, (animal, d, task)
        day = {"task": task, "runs": runs, "pre": pre, "epochs": {}, "tets": {}}
        # tetrode areas and roles (taken from the first run epoch's tetinfo)
        tinfo = _cells(tet_day[runs[0] - 1])
        for t, x in enumerate(tinfo, start=1):
            s = _struct(x)
            if s is not None:
                day["tets"][t] = (_str(s, "area"), _str(s, "descrip"))
        rip = [t for t, (a, ds) in day["tets"].items() if ds == "riptet" and a in ("CA1", "iCA1")]
        ref = [t for t, (a, ds) in day["tets"].items() if ds == "CA1Ref"]
        day["riptets"], day["reftet"] = rip, ref
        for e in [pre] + runs:
            ps = _struct(pos[e - 1])
            fields = str(_str(ps, "fields")).split()
            P = np.asarray(ps.data, float)
            ix = {f: i for i, f in enumerate(fields)}
            xc, yc, vc = (ix.get("x-sm", ix["x"]), ix.get("y-sm", ix["y"]), ix.get("vel-sm", ix["vel"]))
            ep = {"pos": np.c_[P[:, 0], P[:, xc], P[:, yc], P[:, vc]].astype(np.float64),
                  "pos_fields": fields, "pos_meta": _meta(ps)}
            # LFPs: ripple tetrodes and reference
            lfp, starts, fss = [], [], []
            for t in rip:
                t0, fs, x = _eeg(members.pop(f"{animal}eeg{d:02d}-{e}-{t:02d}.mat"))
                lfp.append(x); starts.append(t0); fss.append(fs)
            # tetrodes of an epoch may start at slightly different times: align on the latest start
            assert np.ptp(fss) < 1e-3, fss
            fs0, t00 = fss[0], max(starts)
            offs = [int(round((t00 - s0) * fs0)) for s0 in starts]
            n = min(len(x) - o for x, o in zip(lfp, offs))
            ep["lfp_t0"], ep["lfp_fs"], ep["lfp_n"] = t00, fs0, n
            ep["lfp_start_spread"] = float(np.ptp(starts))
            ep["swr"] = swr_epoch([x[o:o + n] for x, o in zip(lfp, offs)], t00, fs0, ep["pos"][:, 0], ep["pos"][:, 3],
                                  dorsal=[day["tets"][t][0] == "CA1" for t in rip])
            del lfp
            if ref:
                t0, fs, x = _eeg(members.pop(f"{animal}eeg{d:02d}-{e}-{ref[0]:02d}.mat"))
                tt, ph = theta_phase(x, fs)
                ep["theta_t"], ep["theta_ph"] = tt + t0, ph
            if e in runs:
                tk = _struct(_cells(_cells(_mat(members[f"{animal}task{d:02d}.mat"]))[d - 1])[e - 1])
                lc = _cells(tk.linearcoord)
                ep["linearcoord"] = [np.asarray(c, float)[:, :, 0] for c in lc]
                ep["task_meta"] = _meta(tk)
            ep["start"], ep["end"] = ep["pos"][0, 0], ep["pos"][-1, 0]
            day["epochs"][e] = ep
        # units
        units = {}
        ci_day = _cells(cellinfo[d - 1])
        for e in [pre] + runs:
            tets = _cells(spk[e - 1])
            cie = _cells(ci_day[e - 1]) if e - 1 < len(ci_day) else []
            for t, tt in enumerate(tets, start=1):
                for u, x in enumerate(_cells(tt), start=1):
                    s = _struct(x)
                    if s is None:
                        continue
                    data = np.asarray(s.data, float)
                    times = data[:, 0] if data.size else np.zeros(0)
                    ci = None
                    if t - 1 < len(cie):
                        cu = _cells(cie[t - 1])
                        if u - 1 < len(cu):
                            ci = _struct(cu[u - 1])
                    rec = units.setdefault((t, u), {"times": {}, "area": None, "width": [], "ci_width": [], "tag": None})
                    rec["times"][e] = times
                    rec["tag"] = rec["tag"] or _str(s, "tag", None)
                    if ci is not None and "area" in ci._fieldnames:
                        rec["area"] = rec["area"] or _str(ci, "area")
                    w = _num(s, "spikewidth")
                    if np.isfinite(w):
                        rec["width"].append(w)
                    if ci is not None and "spikewidth" in ci._fieldnames:
                        rec["ci_width"].append(_num(ci, "spikewidth"))
        for (t, u), rec in units.items():
            if rec["area"] is None:
                rec["area"] = day["tets"].get(t, (rec["tag"], ""))[0]
        day["units"] = units
        res["days"][d] = day
        for k in [k for k in members if k.startswith(f"{animal}eeg{d:02d}-")]:
            del members[k]
    return res


# ---------------------------------------------------------------- cells and SWRs
BIN = 0.010                 # s, PSTH bin; standard choice (claims file)
RESP = (0.0, 0.2)           # s, SWR response window (SEP, SWR Modulation)
BACKGROUND = (-0.5, -0.1)   # s, pre-SWR background window (SEP)
FS_WIDTH = 0.3              # ms (SEP)
FS_RATE = {"PFC": 17.0, "CA1": 7.0}   # Hz (SEP)
MIN_RASTER_SPIKES = 50      # SEP


def region(area):
    return {"CA1": "CA1", "iCA1": "CA1", "PFC": "PFC"}.get(area)


def swr_onsets(day, epochs, reading="any", onset="ext"):
    """Onsets (s) of the kept SWRs of the given epochs. onset='ext' (main) is the time the envelope
    last rose above its mean before the threshold crossing, the start of the event in the
    Frank-lab convention of the cited Karlsson & Frank (2009) (assumption); 'thr' is the threshold
    crossing."""
    col = {"ext": 0, "thr": 1}[onset]
    out = []
    for e in epochs:
        s = day["epochs"][e]["swr"]
        out.append(s[reading][s["kept_" + reading], col])
    return np.sort(np.concatenate(out)) if out else np.zeros(0)


def epoch_time(day, epochs):
    return sum(day["epochs"][e]["end"] - day["epochs"][e]["start"] for e in epochs)


def spikes_in(unit, epochs):
    x = [unit["times"].get(e, np.zeros(0)) for e in epochs]
    return np.sort(np.concatenate(x)) if x else np.zeros(0)


def aligned(st, onsets, w):
    """Spike times relative to each onset within [-w, w). Returns (rel, swr index)."""
    lo = np.searchsorted(st, onsets - w)
    hi = np.searchsorted(st, onsets + w)
    idx = np.repeat(np.arange(len(onsets)), hi - lo)
    rel = st[np.concatenate([np.arange(a, b) for a, b in zip(lo, hi)]).astype(int)] - onsets[idx] if len(idx) else np.zeros(0)
    keep = rel < w
    return rel[keep], idx[keep]


def cell_table(R, raster_w=0.5, reading="any", onset="ext"):
    """One row per cell-day (reading a of the claims file) of CA1, iCA1 and PFC units with spikes
    in the day's W-track runs."""
    rows = []
    for a, r in R.items():
        for d, day in r["days"].items():
            on = swr_onsets(day, day["runs"], reading, onset)
            T = epoch_time(day, day["runs"])
            for (t, u), un in day["units"].items():
                reg = region(un["area"])
                if reg is None:
                    continue
                st = spikes_in(un, day["runs"])
                if len(st) == 0:
                    continue
                width = np.mean(un["width"]) / 30.0 if un["width"] else np.nan
                rate = len(st) / T
                rel, _ = aligned(st, on, raster_w)
                rows.append(dict(animal=a, day=d, tet=t, unit=u, area=un["area"], region=reg,
                                 width_ms=width, rate=rate, n_raster=len(rel),
                                 fs=bool(width < FS_WIDTH and rate > FS_RATE[reg]),
                                 in_pre=len(un["times"].get(day["pre"], [])) > 0))
    import pandas as pd
    df = pd.DataFrame(rows)
    df["included"] = (~df.fs) & (df.n_raster >= MIN_RASTER_SPIKES)
    return df


def swr_modulation(st, onsets, rng, w=0.5, nshuf=5000):
    """SWR modulation of one cell (SEP, SWR Modulation).

    PSTH in 10 ms bins over [-w, w); 5000 shuffles, each shifting all spikes around one SWR
    circularly by one random amount, uniform over the raster span (claims file); measure = sum of
    squared differences between PSTH and mean shuffled PSTH over 0-200 ms; modulated when the
    measure exceeds 95% of the shuffled measures; excited when the 0-200 ms rate exceeds the
    -500 to -100 ms rate."""
    rel, idx = aligned(st, onsets, w)
    nb = int(round(2 * w / BIN))
    edges = np.linspace(-w, w, nb + 1)
    centers = edges[:-1] + BIN / 2
    n = len(onsets)
    psth = np.histogram(rel, edges)[0] / n / BIN
    win = (centers > RESP[0]) & (centers < RESP[1])
    sh = np.zeros((nshuf, nb))
    chunk = max(1, int(2e7 // max(len(rel), 1)))
    for c0 in range(0, nshuf, chunk):
        k = min(chunk, nshuf - c0)
        shifts = rng.uniform(0, 2 * w, size=(k, n))
        r2 = (rel[None, :] + w + shifts[:, idx]) % (2 * w)
        b = np.minimum((r2 / BIN).astype(int), nb - 1) + np.arange(k)[:, None] * nb
        sh[c0:c0 + k] = np.bincount(b.ravel(), minlength=k * nb).reshape(k, nb) / n / BIN
    m = sh.mean(0)
    real = np.sum((psth[win] - m[win]) ** 2)
    null = np.sum((sh[:, win] - m[win]) ** 2, axis=1)
    resp = np.mean(psth[win])
    bg = np.mean(psth[(centers > BACKGROUND[0]) & (centers < BACKGROUND[1])])
    return dict(psth=psth, centers=centers, measure=real, p=np.mean(null >= real),
                modulated=bool(real > np.quantile(null, 0.95)), excited=bool(resp > bg),
                mi_ratio=real / np.mean(null), mi_z=(real - np.mean(null)) / np.std(null),
                resp_rate=resp, bg_rate=bg)


def swr_counts(st, onsets, win=RESP):
    """Spike count of a cell in 0-200 ms after each SWR onset (SEP, SWR Correlations)."""
    return np.searchsorted(st, onsets + win[1]) - np.searchsorted(st, onsets + win[0])


def psth_timing(psth, centers, sign, search=(0.0, 0.2), sd_ref="baseline"):
    """Peak (sign +1) or trough (sign -1) time and modulation onset of an SWR-PSTH (SEP, Timing
    of SWR-response). Onset: first bin after 0 at which the PSTH is 1 SD above (below) the mean;
    mean and SD of the baseline -500 to -100 ms (reading a) or of the whole PSTH (reading b)."""
    w = (centers > search[0]) & (centers < search[1])
    i = np.argmax(sign * psth[w])
    peak = centers[w][i]
    ref = psth[(centers > BACKGROUND[0]) & (centers < BACKGROUND[1])] if sd_ref == "baseline" else psth
    mu, sd = ref.mean(), ref.std()
    after = centers > 0
    hit = np.flatnonzero(after & (sign * (psth - mu) >= sd))
    onset = centers[hit[0]] if len(hit) else np.nan
    return peak, onset


# ---------------------------------------------------------------- theta
def theta_mask_times(day, e, t, min_len=0.0):
    """True where time t (s) of run epoch e is in a theta period: speed > 5 cm/s and outside every
    SWR on any ripple tetrode (SEP). With min_len, only periods at least that long (s). Also
    returns the theta phase (deg) at t."""
    ep = day["epochs"][e]
    tt = ep["theta_t"]
    key = ("theta_mask", min_len)
    if key in ep:
        ok = ep[key]
        i = np.clip(np.round((t - tt[0]) * THETA_FS).astype(int), 0, len(tt) - 1)
        return ok[i] & (t >= tt[0]) & (t <= tt[-1]), _phase_at(ep, t)
    v = np.interp(tt, ep["pos"][:, 0], ep["pos"][:, 3])
    ok = v > THETA_SPEED
    ev = ep["swr"]["all_any"]
    if len(ev):
        a = np.searchsorted(tt, ev[:, 0]); b = np.searchsorted(tt, ev[:, 2], side="right")
        cover = np.zeros(len(tt) + 1, int)
        np.add.at(cover, a, 1); np.add.at(cover, b, -1)
        ok &= np.cumsum(cover)[:-1] == 0
    if min_len > 0:
        edges = np.diff(np.r_[0, ok.astype(np.int8), 0])
        s, en = np.flatnonzero(edges == 1), np.flatnonzero(edges == -1)
        ok = np.zeros(len(tt), bool)
        for a, b in zip(s, en):
            if (b - a) / THETA_FS >= min_len:
                ok[a:b] = True
    ep[key] = ok
    return theta_mask_times(day, e, t, min_len)


def _phase_at(ep, t):
    """Theta phase (deg) at times t, interpolated linearly on the unwrapped phase between the
    150 Hz samples (so that shifts smaller than a sample change the phase)."""
    if "theta_unwrapped" not in ep:
        ep["theta_unwrapped"] = np.unwrap(np.radians(ep["theta_ph"].astype(np.float64)))
    return np.degrees(np.interp(t, ep["theta_t"], ep["theta_unwrapped"])) % 360


def theta_spike_phases(day, unit, shift=0.0):
    """Theta phases (deg) of a unit's run spikes in theta periods; shift (s) reads the phase at
    spike time + shift."""
    out = []
    for e in day["runs"]:
        st = unit["times"].get(e, np.zeros(0))
        if "theta_t" not in day["epochs"][e] or len(st) == 0:
            continue
        m, _ = theta_mask_times(day, e, st)
        _, ph = theta_mask_times(day, e, st[m] + shift)
        out.append(ph)
    return np.concatenate(out) if out else np.zeros(0)


def rayleigh(ph_deg):
    a = np.radians(ph_deg); n = len(a)
    C, S = np.cos(a).sum(), np.sin(a).sum()
    Rbar = np.hypot(C, S) / n
    Rn = Rbar * n
    p = np.exp(np.sqrt(1 + 4 * n + 4 * (n ** 2 - Rn ** 2)) - (1 + 2 * n))
    return min(max(p, 0.0), 1.0), Rbar, np.degrees(np.arctan2(S, C)) % 360


def vm_kappa(ph_deg):
    """Maximum-likelihood von Mises concentration: solves I1(k)/I0(k) = Rbar."""
    from scipy.optimize import brentq
    from scipy.special import i0e, i1e
    _, R, _ = rayleigh(ph_deg)
    if R < 1e-9:
        return 0.0
    f = lambda k: i1e(k) / i0e(k) - R
    return brentq(f, 1e-9, 1e4) if f(1e4) > 0 else 1e4


def hist_peak_phase(ph_deg, binw=15):
    """Peak of the theta-phase histogram (bin centre). The paper gives no bin; 15 degrees divides
    the 45-degree bins of the claims file's group histogram evenly, so each of those receives the
    same number of possible peak values (a 20-degree bin does not)."""
    h, e = np.histogram(ph_deg % 360, np.arange(0, 360 + binw, binw))
    return e[np.argmax(h)] + binw / 2


# ---------------------------------------------------------------- cross-covariance
def ccg(t1, t2, maxlag, binw=BIN):
    """Histogram of t2 - t1 within +-maxlag (positive: cell 2 after cell 1)."""
    lo = np.searchsorted(t2, t1 - maxlag); hi = np.searchsorted(t2, t1 + maxlag)
    if (hi - lo).sum() == 0:
        nb = int(round(2 * maxlag / binw))
        return np.zeros(nb)
    idx = np.concatenate([np.arange(a, b) for a, b in zip(lo, hi)])
    d = t2[idx] - np.repeat(t1, hi - lo)
    nb = int(round(2 * maxlag / binw))
    return np.histogram(d, np.linspace(-maxlag, maxlag, nb + 1))[0].astype(float)


def gauss_smooth(x, sd_bins=1.67, half_len_bins=2.5):
    """Gaussian of length 50 ms and SD 16.7 ms at 10 ms bins (SEP, theta cross-covariance)."""
    k = np.arange(-int(np.floor(half_len_bins)), int(np.floor(half_len_bins)) + 1)
    g = np.exp(-0.5 * (k / sd_bins) ** 2); g /= g.sum()
    return np.convolve(x, g, mode="same")


def std_xcov(t1, t2, T, maxlag=0.505, binw=BIN, norm="z"):
    """Standardized cross-covariance (SEP; Siapas et al. 2005): CCG minus the coincidences
    expected from the mean rates, r1 r2 B T, divided by sqrt(r1 r2 B T) (norm 'z', reading a) or
    by r1 r2 B T (norm 'rel', reading b); smoothed. Lags in s, positive: cell 2 after cell 1."""
    c = ccg(t1, t2, maxlag, binw)
    E = len(t1) * len(t2) * binw / T
    x = (c - E) / (np.sqrt(E) if norm == "z" else E) if E > 0 else np.full_like(c, np.nan)
    lags = np.linspace(-maxlag, maxlag, len(c) + 1)[:-1] + binw / 2
    return lags, gauss_smooth(x)


def theta_period_spikes(day, unit, min_len=1.0):
    """Run spikes inside theta periods of at least 1 s (SEP) and the total theta time."""
    out = []
    for e in day["runs"]:
        st = unit["times"].get(e, np.zeros(0))
        if "theta_t" not in day["epochs"][e] or len(st) == 0:
            continue
        m, _ = theta_mask_times(day, e, st, min_len)
        out.append(st[m])
    return np.sort(np.concatenate(out)) if out else np.zeros(0)


def theta_time(day, min_len=1.0):
    T = 0.0
    for e in day["runs"]:
        ep = day["epochs"][e]
        if "theta_t" not in ep:
            continue
        m, _ = theta_mask_times(day, e, ep["theta_t"], min_len)
        T += m.sum() / THETA_FS
    return T


# ---------------------------------------------------------------- track, trials, rate maps
WELL_RADIUS = 15.0   # cm, zone around a reward well (claims file leaves it open; readings shown)
MAP_BIN = 2.0        # cm, standard choice (claims file)
MAP_SPEED = 5.0      # cm/s, the paper's movement criterion (claims file)


def wells(ep):
    lc = ep["linearcoord"]
    return {"C": lc[0][0], "L": lc[0][3], "R": lc[1][3]}


def well_visits(ep, radius=WELL_RADIUS):
    """Sequence of well visits (well, entry time, exit time) from position."""
    p = ep["pos"]; W = wells(ep)
    names = list(W)
    dist = np.stack([np.hypot(p[:, 1] - W[k][0], p[:, 2] - W[k][1]) for k in names])
    near = dist.min(0) < radius
    lab = np.where(near, dist.argmin(0), -1)
    visits = []
    cur, t_in = -1, None
    for i, l in enumerate(lab):
        if l != cur:
            if cur >= 0:
                visits.append((names[cur], t_in, p[i - 1, 0]))
            cur, t_in = l, p[i, 0]
    if cur >= 0:
        visits.append((names[cur], t_in, p[-1, 0]))
    # merge consecutive visits to the same well
    merged = []
    for v in visits:
        if merged and merged[-1][0] == v[0]:
            merged[-1] = (v[0], merged[-1][1], v[2])
        else:
            merged.append(v)
    return merged


def score_trials(visits):
    """W-track alternation rule (SEP, Behavioral Tasks; claims file): from a side well the
    correct next well is the centre; from the centre, the side opposite the previous side.
    Returns a list of (from, to, t_leave, t_arrive, kind, correct); the first outbound trial of
    an epoch, with no previous side, is left unscored."""
    out = []
    last_side = visits[0][0] if visits and visits[0][0] != "C" else None
    for (w0, _, t0), (w1, t1, _) in zip(visits[:-1], visits[1:]):
        if w0 == "C":
            ok = None if last_side is None else (w1 not in ("C", last_side))
            out.append((w0, w1, t0, t1, "out", ok))
        else:
            out.append((w0, w1, t0, t1, "in", w1 == "C"))
        if w1 != "C":
            last_side = w1
    return out


def linearize(ep):
    """Distance along each of the two centre-to-side polylines (task linearcoord: centre well,
    centre junction, side junction, side well) and the squared distance to each."""
    p = ep["pos"][:, 1:3]
    res = []
    for poly in ep["linearcoord"]:
        best_d = np.full(len(p), np.inf); best_l = np.zeros(len(p))
        cum = 0.0
        for a, b in zip(poly[:-1], poly[1:]):
            v = b - a; L = np.hypot(*v)
            s = np.clip(((p - a) @ v) / L ** 2, 0, 1)
            proj = a + s[:, None] * v
            dd = np.sum((p - proj) ** 2, 1)
            m = dd < best_d
            best_d[m] = dd[m]; best_l[m] = cum + s[m] * L
            cum += L
        res.append((best_l, best_d, cum))
    return res


def trajectory_labels(ep, radius=WELL_RADIUS):
    """Per position sample, the trajectory 0..3 (out-L, in-L, out-R, in-R) between leaving one
    well and arriving at the next, and the linear position on it; -1 elsewhere (at the wells, or
    side-to-side runs)."""
    t = ep["pos"][:, 0]
    lab = np.full(len(t), -1)
    lin = linearize(ep)
    for w0, w1, t0, t1 in [(a[0], b[0], a[2], b[1]) for a, b in zip(well_visits(ep, radius)[:-1], well_visits(ep, radius)[1:])]:
        key = {("C", "L"): 0, ("L", "C"): 1, ("C", "R"): 2, ("R", "C"): 3}.get((w0, w1))
        if key is None:
            continue
        lab[(t >= t0) & (t < t1)] = key
    linpos = np.where(lab <= 1, lin[0][0], lin[1][0])
    lengths = (lin[0][2], lin[1][2])
    return lab, linpos, lengths


def rate_maps(day, units, speed=MAP_SPEED, epochs=None):
    """Occupancy-normalized linearized rate maps on the 4 trajectories (SEP, Spatial and
    Behavioral Coding Properties), 2 cm bins, speed > 5 cm/s, pooled over the day's W-track runs
    (or the given epochs). Runs in different environments (wtr1, wtr2: different tracks) get bins
    of their own, laid end to end within each trajectory. Returns {unit key: list of 4 arrays}."""
    occ, cnt = {}, {k: {} for k in units}
    for e in (day["runs"] if epochs is None else epochs):
        ep = day["epochs"][e]; env = day["task"][e][1]
        lab, lin, lengths = trajectory_labels(ep)
        t = ep["pos"][:, 0]; dt = np.median(np.diff(t))
        v = ep["pos"][:, 3]
        if env not in occ:
            nbins = [int(np.ceil(lengths[j // 2] / MAP_BIN)) for j in range(4)]
            occ[env] = [np.zeros(n) for n in nbins]
            for k in units:
                cnt[k][env] = [np.zeros(n) for n in nbins]
        o = occ[env]
        ok = (lab >= 0) & (v > speed if speed else True)
        b = np.floor(lin / MAP_BIN).astype(int)
        for j in range(4):
            m = ok & (lab == j)
            o[j] += np.bincount(np.minimum(b[m], len(o[j]) - 1), minlength=len(o[j])) * dt
        for k, un in units.items():
            st = un["times"].get(e, np.zeros(0))
            st = st[(st >= t[0]) & (st <= t[-1])]
            i = np.clip(np.searchsorted(t, st), 0, len(t) - 1)
            for j in range(4):
                m = ok[i] & (lab[i] == j)
                cnt[k][env][j] += np.bincount(np.minimum(b[i][m], len(o[j]) - 1), minlength=len(o[j]))
    out = {}
    for k in units:
        out[k] = [np.concatenate([np.where(occ[env][j] > 0, cnt[k][env][j] / np.where(occ[env][j] > 0, occ[env][j], 1), np.nan)
                                  for env in occ]) for j in range(4)]
    return out


def coverage(maps, thr_frac=0.25, min_peak=3.0):
    allr = np.concatenate(maps)
    allr = allr[np.isfinite(allr)]
    pk = allr.max() if len(allr) else 0
    if pk <= min_peak:
        return np.nan
    return np.mean(allr > thr_frac * pk)


def arm_direction_index(maps, how="mean"):
    f = np.nanmean if how == "mean" else np.nanmax
    L = f(np.r_[maps[0], maps[1]]); R = f(np.r_[maps[2], maps[3]])
    O = f(np.r_[maps[0], maps[2]]); I = f(np.r_[maps[1], maps[3]])
    ai = abs(L - R) / (L + R) if L + R > 0 else np.nan
    di = abs(O - I) / (O + I) if O + I > 0 else np.nan
    return ai, di


def spatial_corr(m1, m2):
    a = np.concatenate(m1); b = np.concatenate(m2)
    ok = np.isfinite(a) & np.isfinite(b)
    if ok.sum() < 3 or np.std(a[ok]) == 0 or np.std(b[ok]) == 0:
        return np.nan
    return np.corrcoef(a[ok], b[ok])[0, 1]


# ---------------------------------------------------------------- GLM
GLM_SPLITS = 5000   # SEP, GLM


def poisson_fit(X, y, beta0=None, maxit=100, tol=1e-8, max_beta=15.0):
    """Poisson GLM with log link by iteratively reweighted least squares. X includes the
    intercept column. Returns (beta, converged); a fit whose coefficients pass max_beta (perfect
    separation) or that does not converge is reported as not converged (SEP: such cells are
    removed)."""
    beta = np.zeros(X.shape[1]) if beta0 is None else beta0.copy()
    if beta0 is None:
        beta[0] = np.log(max(y.mean(), 1e-3))
    for _ in range(maxit):
        eta = np.clip(X @ beta, -30, 30)
        mu = np.exp(eta)
        z = eta + (y - mu) / mu
        XtW = X.T * mu
        try:
            new = np.linalg.solve(XtW @ X + 1e-10 * np.eye(X.shape[1]), XtW @ z)
        except np.linalg.LinAlgError:
            return beta, False
        if not np.all(np.isfinite(new)):
            return beta, False
        done = np.max(np.abs(new - beta)) < tol * (1 + np.max(np.abs(beta)))
        beta = new
        if done:
            return beta, bool(np.max(np.abs(beta[1:])) < max_beta) if len(beta) > 1 else True
    return beta, False


def design(Xc):
    return np.c_[np.ones(len(Xc)), Xc]


def glm_cv(Xc, y, rng, splits=None):
    """Cross-validated prediction (SEP, GLM): train on a random 90%, predict the other 10%; error =
    mean absolute difference of predicted and actual counts; shuffled error from the predictions
    shuffled across SWRs. Returns dict(perf, frac_better, converged) where perf is the fractional
    improvement (shuffled - real) / shuffled of the mean errors over splits."""
    splits = splits or GLM_SPLITS
    Xc = Xc[:, Xc.sum(0) > 0]   # predictors that never spike carry no information
    X = design(Xc); n = len(y)
    beta_full, ok = poisson_fit(X, y)
    if not ok:
        return dict(perf=np.nan, frac_better=np.nan, converged=False)
    ntest = max(1, int(round(0.1 * n)))
    err, err_sh, better = [], [], 0
    nfail = 0
    for _ in range(splits):
        perm = rng.permutation(n)
        te, tr = perm[:ntest], perm[ntest:]
        b, ok = poisson_fit(X[tr], y[tr], beta_full, maxit=50)
        if not ok:
            nfail += 1
            continue
        pred = np.exp(np.clip(X[te] @ b, -30, 30))
        e = np.mean(np.abs(pred - y[te])); es = np.mean(np.abs(rng.permutation(pred) - y[te]))
        err.append(e); err_sh.append(es); better += e < es
    if len(err) < splits / 2:
        return dict(perf=np.nan, frac_better=np.nan, converged=False)
    return dict(perf=(np.mean(err_sh) - np.mean(err)) / np.mean(err_sh), frac_better=better / len(err), converged=True, failed_splits=nfail)


def glm_cross(Xtr, ytr, Xte, yte, rng, nshuf=1000):
    """Train on one data set, predict another (SEP, GLM; Task and rest period comparisons).
    Returns perf = (mean shuffled error - error) / mean shuffled error and the shuffle p-value
    (fraction of shuffles with error <= the real error)."""
    keep = Xtr.sum(0) > 0
    Xtr, Xte = Xtr[:, keep], Xte[:, keep]
    b, ok = poisson_fit(design(Xtr), ytr)
    if not ok:
        return dict(perf=np.nan, p=np.nan, converged=False)
    pred = np.exp(np.clip(design(Xte) @ b, -30, 30))
    e = np.mean(np.abs(pred - yte))
    es = np.array([np.mean(np.abs(rng.permutation(pred) - yte)) for _ in range(nshuf)])
    return dict(perf=(es.mean() - e) / es.mean(), p=np.mean(es <= e), converged=True)


# ---------------------------------------------------------------- replay (SEP, Replay analysis)
REPLAY_BIN = 0.015       # s, SEP
REPLAY_MIN_CELLS = 4     # CA1 cells spiking in the SWR, SEP
REPLAY_SHUFFLES = 500    # time-bin shuffles, SEP
DECODE_BIN = 2           # map bins (2 cm) per decoding bin, so 4 cm; standard choice
DECODE_SMOOTH = 1.0      # Gaussian SD of the place fields, in decoding bins; standard choice
RATE_FLOOR = 0.1         # Hz added to every place field so that no bin has zero probability; standard choice
LINE_HALF_WIDTH = 3      # decoding bins (+-12 cm) around the fitted line; standard choice (Davidson et al. 2009 use 15 cm)


def side_profiles(maps):
    """Per side (left, right) of the W-track, the linear rate profile from centre well to side well: the mean of
    the outbound and inbound maps (trajectories 0/1 and 2/3), in DECODE_BIN bins, smoothed, with RATE_FLOOR."""
    out = []
    for a, b in ((maps[0], maps[1]), (maps[2], maps[3])):
        ab = np.vstack([a, b]); ok = np.isfinite(ab)
        m = np.where(ok, ab, 0.0).sum(0) / np.maximum(ok.sum(0), 1)   # bins never visited count as 0 Hz
        n = len(m) // DECODE_BIN * DECODE_BIN
        m = m[:n].reshape(-1, DECODE_BIN).mean(1)
        out.append(gaussian_filter1d(m, DECODE_SMOOTH, mode="nearest") + RATE_FLOOR)
    return out


def decode(counts, fields):
    """Bayesian decoding with a Poisson model and a flat prior (SEP; Karlsson & Frank 2009). counts: (cells,
    time bins) spike counts in REPLAY_BIN bins; fields: (cells, positions) rates in Hz. Returns the posterior
    (time bins, positions), each row summing to 1."""
    lf = np.log(fields)
    ll = counts.T @ lf - REPLAY_BIN * fields.sum(0)[None, :]
    ll -= ll.max(1, keepdims=True)
    p = np.exp(ll)
    return p / p.sum(1, keepdims=True)


def line_fit_p(post, rng, nshuf=REPLAY_SHUFFLES):
    """Line-fit replay score (Karlsson & Frank 2009; Davidson et al. 2009): the largest mean, over time bins, of
    the posterior within LINE_HALF_WIDTH of a line, over lines of constant speed; p is the fraction of time-bin
    shuffles (SEP: shuffles of the time bins) scoring at least as high."""
    nt, ns = post.shape
    C = np.concatenate([np.zeros((nt, 1)), np.cumsum(post, 1)], 1)
    slopes = np.linspace(-ns / 2, ns / 2, 41)
    offs = np.arange(-ns, 2 * ns + 1)
    tt = np.arange(nt)
    ctr = offs[None, :, None] + slopes[:, None, None] * (tt - (nt - 1) / 2)[None, None, :]
    lo = np.clip(np.round(ctr - LINE_HALF_WIDTH).astype(int), 0, ns).reshape(-1, nt)
    hi = np.clip(np.round(ctr + LINE_HALF_WIDTH + 1).astype(int), 0, ns).reshape(-1, nt)
    perms = np.vstack([np.arange(nt)] + [rng.permutation(nt) for _ in range(nshuf)])
    sc = []
    for k in range(0, len(perms), 100):
        Cs = C[perms[k:k + 100]]                             # (shuffles, nt, ns + 1)
        sc.append((np.take_along_axis(Cs, hi.T[None].repeat(len(Cs), 0), 2) -
                   np.take_along_axis(Cs, lo.T[None].repeat(len(Cs), 0), 2)).mean(1).max(1))
    sc = np.concatenate(sc)
    return sc[0], float(np.mean(sc[1:] >= sc[0]))
