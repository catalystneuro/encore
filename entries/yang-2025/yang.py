"""Loading and measures for dandiset 001212 (Yang et al. 2025, doi:10.1109/tnsre.2025.3614867).

The dandiset holds, for each of 7 rats (R1 to R7), 8 NWB files: four baseline groups (`00base0`,
`02base1`, `04base2`, `06base3`) and four stimulation groups (`01<site>-stim`, ...), in the
order of the file names. Each file holds one ElectricalSeries per seizure, 600 s of 4-channel LFP
(DG, CA1, CA3, ANT, in microvolts) at 1 kHz, named `<rat>_<date>-ictal<k>`. The files carry no
seizure times, no stimulation times and no interictal recordings, so seizure onset and end and the
stimulation trains are found here from the LFP.

Where each parameter comes from:

- Sampling rate 1 kHz, channel order DG, CA1, CA3, ANT: the files (and Methods A).
- Stimulation: 130 Hz biphasic pulses in 5 s trains with 5 s pauses (Methods C). The trains are
  found from the comb of the pulse frequency and its aliases; this is a method of this attempt
  (the files have no stimulation times), checked in the notebook against the 5 s train length.
- Seizure onset and end: the paper gives no rule (claims file, opening comment, reading (b)).
  Assumption: line length in 1 s windows with 0.5 s steps on each channel, scaled by the channel's
  median over the 600 s; the seizure is the run in which the largest scaled line length of the
  four channels is above `SZ_THRESH` (or a stimulation train is on), runs less than `SZ_GAP` s
  apart merged, extended while it stays above a lower threshold (see `detect_seizure`). The
  thresholds are a choice; the notebook shows other values.
- GC: conditional time-domain Granger causality between the 4 channels (MVGC, Methods B, ref. 37),
  from VAR models fitted by OLS, model order by BIC up to `GC_MAXORDER` (MVGC's own selection,
  claims file, a standard choice), over the first 5 s after onset in 1 s windows with 0.5 s
  overlap (9 windows, Methods B). cf_w is computed per window and averaged; as cf_w is linear in
  the GC matrix, averaging the matrices first gives the same value (claims file readings (a) and
  (b) of combining coincide).
- PSD: Welch, bands of Methods D; window lengths a standard choice (claims file).
- IIS: Methods F rules (200 ms minimum interval keeping the larger peak, width at most 100 ms,
  |height| above mean + 5 SD of a baseline stretch); width at half prominence is a standard
  choice (claims file).
- HFO: short line length detector (Methods E, refs 50 and 51); parameters are listed with
  `hfo_rate` and are the HFO App's defaults as far as the paper allows (claims file).
"""

import hashlib
import re

import h5py
import numpy as np
import remfile
import requests
from scipy import signal

DANDISET = "001212"
VERSION = "0.241023.0931"
API = "https://api.dandiarchive.org/api"
FS = 1000.0
CHANNELS = ["DG", "CA1", "CA3", "ANT"]
BANDS = {"delta": (0.5, 4), "theta": (4, 8), "alpha": (8, 12), "beta": (12, 30),
         "gamma": (30, 90), "high_gamma": (90, 120)}

# seizure detection (assumption, see module docstring)
SZ_WIN = 1.0
SZ_STEP = 0.5
SZ_THRESH = 2.0
SZ_GAP = 7.0  # trains are 5 s with 5 s pauses (Methods C), so runs between trains are about 6 s apart
SZ_MINDUR = 5.0
# GC (standard choice)
GC_MAXORDER = 20
GC_DOWNSAMPLE = 1


def list_assets():
    """All assets of the pinned version, with rat, group index, group kind and site."""
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=200"
    out = []
    for a in requests.get(url, timeout=60).json()["results"]:
        m = re.search(r"ses-Rat(R\d)-(\d\d)(base\d|[A-Z0-9]+-stim)", a["path"])
        rat, idx, name = m.group(1), int(m.group(2)), m.group(3)
        kind = "baseline" if name.startswith("base") else "stim"
        site = name.replace("-stim", "") if kind == "stim" else None
        out.append(dict(path=a["path"], asset_id=a["asset_id"], size=a["size"], rat=rat,
                        index=idx, kind=kind, site=site, group=f"{rat}-{idx:02d}"))
    return sorted(out, key=lambda x: (x["rat"], x["index"]))


def s3_url(asset_id):
    return requests.head(f"{API}/assets/{asset_id}/download/", allow_redirects=True,
                         timeout=60).url


def open_asset(asset_id):
    return h5py.File(remfile.File(s3_url(asset_id)), "r")


def iter_epochs(asset):
    """Yield (name, data, attrs) for each seizure epoch of an asset, streamed one at a time."""
    with open_asset(asset["asset_id"]) as f:
        for name, es in f["acquisition"].items():
            d = es["data"][:]
            attrs = dict(rate=float(es["starting_time"].attrs["rate"]),
                         start=float(es["starting_time"][()]),
                         unit=es["data"].attrs["unit"],
                         description=es.attrs["description"])
            yield name, d, attrs


def epoch_date(name):
    m = re.match(r"R\d_(\d{4})_(\d+)[_-](\d+)", name)
    return f"{int(m.group(1)):04d}-{int(m.group(2)):02d}-{int(m.group(3)):02d}"


def md5(a):
    return hashlib.md5(np.ascontiguousarray(a).tobytes()).hexdigest()


# ---------------------------------------------------------------- stimulation trains
def _alias(f):
    f = f % FS
    return FS - f if f > FS / 2 else f


def stim_score(x, win=0.5, step=0.25, f0_grid=np.arange(120.0, 145.01, 0.25)):
    """Comb score per window: mean log power at the aliased harmonics (1 to 11) of the pulse
    rate minus the median log power of 60-490 Hz, on each channel; the best pulse rate is chosen
    over the epoch, and the score is the largest over channels. Returns window centres (s), the
    score, the pulse rate, and the score per channel (channels x windows)."""
    n = int(win * FS)
    f, t, S = signal.spectrogram(x.T, fs=FS, nperseg=n, noverlap=n - int(step * FS),
                                 detrend="constant")
    L = np.log10(S + 1e-12)  # (channel, freq, time)
    band = (f >= 60) & (f <= 490)
    med = np.median(L[:, band], 1)
    best, best_f0, best_v = None, None, -np.inf
    for f0 in f0_grid:
        idx = sorted({int(np.argmin(np.abs(f - _alias(k * f0)))) for k in range(1, 12)})
        sc = L[:, idx].mean(1) - med
        v = np.percentile(sc.max(0), 99)
        if v > best_v:
            best, best_f0, best_v = sc, f0, v
    return t, best.max(0), best_f0, best


def find_trains(x, thresh=1.0, min_len=4.0):
    """Stimulation trains as (start, end) in s: runs of comb score above `thresh` lasting at least
    `min_len` s (trains are 5 s, Methods C)."""
    t, sc, f0, _ = stim_score(x)
    on = sc > thresh
    runs = _runs(on)
    step = t[1] - t[0]
    out = []
    for a, b in runs:
        s, e = t[a] - step, t[b - 1] + step
        if e - s >= min_len:
            out.append((float(s), float(e)))
    return out, f0


def _runs(mask):
    m = np.concatenate([[False], mask, [False]]).astype(int)
    d = np.diff(m)
    return list(zip(np.where(d == 1)[0], np.where(d == -1)[0]))


# ---------------------------------------------------------------- seizure onset and end
SZ_BAND = (1.0, 45.0)  # band of the seizure line length (below the 50 Hz mains; a choice)


def line_length(x, win=SZ_WIN, step=SZ_STEP, band=SZ_BAND):
    """Line length per window and channel of the signal band-passed to `band` (none if None);
    times are window starts (s)."""
    n, s = int(win * FS), int(step * FS)
    if band is not None:
        sos = signal.butter(4, band, btype="band", fs=FS, output="sos")
        x = signal.sosfiltfilt(sos, x, axis=0)
    dx = np.abs(np.diff(x, axis=0))
    c = np.concatenate([np.zeros((1, x.shape[1])), np.cumsum(dx, 0)])
    starts = np.arange(0, x.shape[0] - n, s)
    ll = c[starts + n - 1] - c[starts]
    return starts / FS, ll


def detect_seizure(x, trains=(), thresh=SZ_THRESH, gap=SZ_GAP, mindur=SZ_MINDUR,
                   last_train=True):
    """Onset and end (s) of the seizure in a 600 s epoch, from z = the largest over channels of
    line length / channel median (1 s windows, 0.5 s steps).

    Core windows are those with z above `thresh`, and, in stimulation groups, the windows of a
    stimulation train (the closed-loop detector fired, Methods C; the artifact hides the LFP).
    Core runs less than `gap` s apart are merged. The seizure is the run holding the first train
    when there are trains, and otherwise the run with the largest summed excess. Its boundaries are then extended outwards
    while z stays above 1 + (thresh - 1) / 2 (hysteresis). When the run ends with a train after
    which z is low, the seizure ends at the end of that train if `last_train` (default), or at the
    last non-train window above threshold otherwise. Returns (onset, end) or (nan, nan)."""
    t, ll = line_length(x)
    z = (ll / np.median(ll, 0)).max(1)
    intrain = np.zeros(len(t), bool)
    for s, e in trains:
        intrain |= (t + SZ_WIN > s) & (t < e)
    core = (z > thresh) | intrain
    runs = [[a, b] for a, b in _runs(core)]  # window indices [a, b)
    step = t[1] - t[0]
    merged = []
    for a, b in runs:
        if merged and (t[a] - (t[merged[-1][1] - 1] + SZ_WIN)) < gap:
            merged[-1][1] = b
        else:
            merged.append([a, b])
    if not merged:
        return np.nan, np.nan

    def mass(r):
        k = np.zeros(len(t), bool)
        k[r[0]:r[1]] = True
        return np.sum(np.clip(z[k & ~intrain] - thresh, 0, None)) + np.sum(k & intrain)

    with_train = [r for r in merged if intrain[r[0]:r[1]].any()]
    if with_train:
        # the closed-loop detector fired at the seizure: take the run holding the first train
        a, b = with_train[0]
    else:
        a, b = max(merged, key=mass)
    if not last_train:
        # drop trailing train windows not followed by ictal activity
        while b - 1 > a and intrain[b - 1]:
            b -= 1
        while b - 1 > a and not (z[b - 1] > thresh) and not intrain[b - 1]:
            b -= 1
    lower = 1 + (thresh - 1) / 2
    while a > 0 and z[a - 1] > lower and not intrain[a - 1]:
        a -= 1
    while b < len(t) and z[b] > lower and not intrain[b]:
        b += 1
    onset, end = float(t[a]), float(t[b - 1] + SZ_WIN)
    if end - onset < mindur:
        return np.nan, np.nan
    return onset, end


# ---------------------------------------------------------------- Granger causality
def _lagmat(x, p):
    """Rows t = p..T-1, columns lag 1..p of each variable."""
    T, n = x.shape
    return np.hstack([x[p - k:T - k] for k in range(1, p + 1)])


def var_bic_order(x, maxorder=GC_MAXORDER):
    T, n = x.shape
    best, bo = np.inf, 1
    for p in range(1, maxorder + 1):
        X = _lagmat(x[maxorder - p:], p)  # same sample for every order
        Y = x[maxorder:]
        X = np.hstack([np.ones((len(X), 1)), X])
        B, *_ = np.linalg.lstsq(X, Y, rcond=None)
        E = Y - X @ B
        S = E.T @ E / len(Y)
        bic = np.linalg.slogdet(S)[1] + np.log(len(Y)) * p * n * n / len(Y)
        if bic < best:
            best, bo = bic, p
    return bo


def cond_gc(x, p):
    """Conditional time-domain GC matrix F[i, j] = GC from j to i (MVGC convention: row target,
    column source), from full and reduced OLS VAR(p) fits."""
    T, n = x.shape
    x = x - x.mean(0)
    Y = x[p:]
    L = _lagmat(x, p)  # columns: lag k var v at (k-1)*n + v
    F = np.zeros((n, n))
    Bf, *_ = np.linalg.lstsq(L, Y, rcond=None)
    Ef = Y - L @ Bf
    vf = (Ef ** 2).mean(0)
    for j in range(n):
        keep = [c for c in range(L.shape[1]) if c % n != j]
        Lr = L[:, keep]
        Br, *_ = np.linalg.lstsq(Lr, Y, rcond=None)
        vr = ((Y - Lr @ Br) ** 2).mean(0)
        for i in range(n):
            if i != j:
                F[i, j] = np.log(vr[i] / vf[i])
    return F


def cfw_onset(x, onset, order=None, win=1.0, step=0.5, dur=5.0, ds=GC_DOWNSAMPLE):
    """cf_w per node over the first `dur` s after onset (9 windows of 1 s, 0.5 s step, Methods B).
    Returns (out-strength minus in-strength averaged over windows, mean GC matrix, order).
    Reading (b) of the claims file (in minus out) is the negative of the first value."""
    i0 = int(round(onset * FS))
    seg = x[i0:i0 + int(dur * FS)]
    if ds > 1:
        seg = signal.decimate(seg, ds, axis=0, zero_phase=True)
    fs = FS / ds
    n, s = int(win * fs), int(step * fs)
    wins = [seg[k:k + n] for k in range(0, len(seg) - n + 1, s)]
    if order is None:
        order = int(np.median([var_bic_order(w - w.mean(0)) for w in wins]))
    Fs = np.array([cond_gc(w, order) for w in wins])
    G = Fs.mean(0)
    cf = np.array([F.sum(0) - F.sum(1) for F in Fs]).mean(0)  # out (column sums) - in (row sums)
    return cf, G, order


# ---------------------------------------------------------------- PSD ratio
def psd_ratio(seg, total=(0.5, 120.0), nperseg=1000):
    """Band PSD sums over the total PSD sum (Methods D), per channel: dict band -> array(4)."""
    nps = min(nperseg, len(seg))
    f, P = signal.welch(seg.T, fs=FS, nperseg=nps, noverlap=nps // 2, window="hann")
    tot = P[:, (f >= total[0]) & (f <= total[1])].sum(1)
    out = {}
    for b, (lo, hi) in BANDS.items():
        k = (f >= lo) & (f < hi) if b != "high_gamma" else (f >= lo) & (f <= hi)
        out[b] = P[:, k].sum(1) / tot
    return out


# ---------------------------------------------------------------- interictal spikes
def detect_iis(x, mu, sd, k=5.0, min_dist=0.2, max_width=0.1):
    """IIS times (s) on one channel by the rules of Methods F: positive or negative peaks with
    |height - mu| above k SD of a baseline stretch (mu and sd of the raw trace there), at least
    200 ms apart (the smaller removed), width at half prominence at most 100 ms."""
    y = x - mu
    thr = k * sd
    peaks = []
    for sgn in (1, -1):
        p, pr = signal.find_peaks(sgn * y, height=thr, width=(None, max_width * FS),
                                  rel_height=0.5)
        peaks += [(i, abs(y[i])) for i in p]
    peaks.sort()
    kept = []
    for i, h in peaks:
        if kept and i - kept[-1][0] < min_dist * FS:
            if h > kept[-1][1]:
                kept[-1] = (i, h)
            continue
        kept.append((i, h))
    return np.array([i for i, _ in kept]) / FS


# ---------------------------------------------------------------- HFO (short line length)
def hfo_events(x, band, win=0.005, thresh_sd=3.0, min_dur=0.006, merge=0.01):
    """HFO candidates on one channel by the short line length detector (Methods E, refs 50, 51;
    Gardner et al. 2007): band-pass `band`, line length in `win` s windows sliding by one sample,
    events where it exceeds mean + `thresh_sd` SD of the segment for at least `min_dur` s, events
    closer than `merge` s merged. Returns event start times (s). Parameters are a choice (the paper
    gives none); the notebook shows other thresholds."""
    hi = min(band[1], 0.49 * FS)
    sos = signal.butter(4, [band[0], hi], btype="band", fs=FS, output="sos")
    y = signal.sosfiltfilt(sos, x)
    n = max(2, int(win * FS))
    dl = np.abs(np.diff(y))
    ll = np.convolve(dl, np.ones(n), mode="same")
    thr = ll.mean() + thresh_sd * ll.std()
    runs = _runs(ll > thr)
    ev = []
    for a, b in runs:
        if (b - a) / FS >= min_dur:
            if ev and (a / FS - ev[-1][1]) < merge:
                ev[-1] = (ev[-1][0], b / FS)
            else:
                ev.append((a / FS, b / FS))
    return np.array([e[0] for e in ev])


# ---------------------------------------------------------------- one pass over an epoch
SZ_THRESH_VARIANTS = (1.5, 2.0, 3.0)
IIS_SPAN = 180.0  # s before onset and after end (Results D, Figure 5B)
RIPPLE = (80.0, 250.0)
FAST_RIPPLE = (250.0, 500.0)  # filtered to just below the 500 Hz Nyquist limit (claims file)


def psd_windows(kind, onset, trains):
    """Pre and post windows of Methods D. Stimulation groups: pre from onset to the start of the
    first train, post the 5 s after the first train. Baseline groups: pre 0 to 5 s after onset,
    post 10 to 15 s after onset. Returns ((a, b), (c, d)) in s, or None."""
    if kind == "baseline":
        return (onset, onset + 5.0), (onset + 10.0, onset + 15.0)
    later = [tr for tr in trains if tr[0] >= onset - 1.0]
    if not later:
        return None
    s, e = later[0]
    return (onset, s), (e, e + 5.0)


def epoch_features(d, kind, gc=True):
    """Everything the notebook needs from one 600 s epoch, computed in one pass, so that each
    epoch is streamed once. `d` is samples x 4 channels (DG, CA1, CA3, ANT)."""
    out = {"md5": md5(d), "md5_ch": [md5(d[:, c]) for c in range(4)],
           "n_at_extreme": int(np.sum(np.abs(d) >= np.abs(d).max() - 1e-9)),
           "std": d.std(0), "min": d.min(0), "max": d.max(0)}
    trains, f0 = find_trains(d)
    out["trains"] = trains
    out["pulse_rate"] = f0
    if trains:
        t, _, _, per = stim_score(d)
        k = np.zeros(len(t), bool)
        for s, e in trains:
            k |= (t >= s) & (t <= e)
        out["artifact_by_channel"] = per[:, k].mean(1)
    else:
        out["artifact_by_channel"] = np.full(4, np.nan)
    for th in SZ_THRESH_VARIANTS:
        out[f"sz_{th}"] = detect_seizure(d, trains, thresh=th)
    out["sz_notrainend"] = detect_seizure(d, trains, last_train=False)
    onset, end = out[f"sz_{SZ_THRESH}"]
    out["onset"], out["end"] = onset, end
    if not np.isfinite(onset):
        return out
    # trains relative to the seizure (clock check)
    out["trains_in_seizure"] = [bool(s < end + 1 and e > onset - 1) for s, e in trains]
    # GC at onset
    if gc and onset * FS + 5000 <= len(d):
        out["cfw"], out["gc"], out["gc_order"] = cfw_onset(d, onset)
        out["cfw_ds4"], _, out["gc_order_ds4"] = cfw_onset(d, onset, ds=4)
        for th in SZ_THRESH_VARIANTS:
            o2 = out[f"sz_{th}"][0]
            if th != SZ_THRESH and np.isfinite(o2) and o2 * FS + 5000 <= len(d):
                out[f"cfw_{th}"] = cfw_onset(d, o2)[0]
    # PSD ratio pre and post
    w = psd_windows(kind, onset, trains)
    out["psd_windows"] = w
    if w is not None and w[0][1] - w[0][0] >= 0.5 and w[1][1] * FS <= len(d):
        for lab, (a, b) in zip(("pre", "post"), w):
            seg = d[int(a * FS):int(b * FS)]
            for nps in (1000, 500):
                out[f"psd_{lab}_{nps}"] = psd_ratio(seg, nperseg=nps)
            out[f"psd_{lab}_{1000}_total500"] = psd_ratio(seg, total=(0.0, 500.0))
    # IIS 180 s before onset and after end, 1 s bins, per channel
    pre_a = max(0.0, onset - IIS_SPAN)
    ref = d[int(pre_a * FS):int(onset * FS)]
    if len(ref) > 10 * FS:
        mask = np.zeros(len(d), bool)
        for s, e in trains:
            mask[int(s * FS):int(e * FS)] = True
        nb = int(IIS_SPAN)
        pre_counts = np.full((4, nb), np.nan)
        post_counts = np.full((4, nb), np.nan)
        for c in range(4):
            mu, sd = ref[:, c].mean(), ref[:, c].std()
            ts = detect_iis(d[:, c], mu, sd)
            ts = ts[~mask[(ts * FS).astype(int)]]
            for arr, origin, sign in ((pre_counts, onset, -1), (post_counts, end, 1)):
                rel = (ts - origin) * sign
                h = np.histogram(rel, bins=np.arange(0, nb + 1))[0].astype(float)
                # bins outside the epoch are missing
                for b in range(nb):
                    tb = origin + sign * (b + 0.5)
                    if tb < 0 or tb > len(d) / FS:
                        h[b] = np.nan
                arr[c] = h
        out["iis_pre"], out["iis_post"] = pre_counts, post_counts  # pre: bin 0 is just before onset
        out["iis_thr"] = [ref[:, c].std() * 5 for c in range(4)]
    # ictal HFO in the PSD windows, threshold from the 180 s before onset
    if w is not None and len(ref) > 10 * FS and w[1][1] * FS <= len(d):
        for nm, band in (("ripple", RIPPLE), ("fr", FAST_RIPPLE)):
            for th in (3.0, 5.0):
                rates = {}
                for lab, (a, b) in zip(("pre", "post"), w):
                    r = []
                    for c in range(4):
                        r.append(hfo_rate(d[:, c], band, (a, b), (pre_a, onset), th))
                    rates[lab] = np.array(r)
                out[f"hfo_{nm}_{th}"] = rates
                # threshold from the seizure's own two windows pooled (a variant)
                rates = {}
                for lab, (a, b) in zip(("pre", "post"), w):
                    rates[lab] = np.array([hfo_rate(d[:, c], band, (a, b), w, th) for c in range(4)])
                out[f"hfo_{nm}_{th}_self"] = rates
    return out


def hfo_rate(x, band, window, ref_window, thresh_sd, win=0.005, min_dur=0.006, merge=0.01):
    """Rate (events/s) of short line length HFO detections inside `window` (s), the threshold
    being mean + `thresh_sd` SD of the short line length over `ref_window` (s), or over the union
    of the windows in `ref_window` when it is a pair of windows. Filtering is done on the stretch
    from the start of the reference to its end, padded by 1 s."""
    refs = list(ref_window) if isinstance(ref_window[0], (tuple, list)) else [ref_window]
    a0 = int(max(0, min([r[0] for r in refs] + [window[0]]) - 1) * FS)
    b0 = int(min(len(x) / FS, max([r[1] for r in refs] + [window[1]]) + 1) * FS)
    hi = min(band[1], 0.49 * FS)
    sos = signal.butter(4, [band[0], hi], btype="band", fs=FS, output="sos")
    y = signal.sosfiltfilt(sos, x[a0:b0])
    n = max(2, int(win * FS))
    ll = np.convolve(np.abs(np.diff(y, prepend=y[0])), np.ones(n), mode="same")
    tt = (np.arange(len(y)) + a0) / FS
    r = np.zeros(len(tt), bool)
    for ra, rb in refs:
        r |= (tt >= ra) & (tt < rb)
    thr = ll[r].mean() + thresh_sd * ll[r].std()
    k = (tt >= window[0]) & (tt < window[1])
    runs = _runs(ll[k] > thr)
    ev = []
    for a, b in runs:
        if (b - a) / FS >= min_dur:
            if ev and (a - ev[-1][1]) / FS < merge:
                ev[-1] = (ev[-1][0], b)
            else:
                ev.append((a, b))
    return len(ev) / (window[1] - window[0])


def process_asset(asset):
    """Stream every epoch of one asset and return one record per epoch (see `epoch_features`)."""
    import os
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    rows = []
    for name, d, attrs in iter_epochs(asset):
        r = epoch_features(d, asset["kind"], gc=(asset["kind"] == "baseline"))
        r.update(rat=asset["rat"], group=asset["group"], index=asset["index"],
                 kind=asset["kind"], site=asset["site"], epoch=name, date=epoch_date(name),
                 n_samples=d.shape[0], n_channels=d.shape[1], rate=attrs["rate"],
                 start=attrs["start"], unit=attrs["unit"], description=attrs["description"])
        rows.append(r)
    return rows


def process_all(assets, workers=4):
    """All assets, `workers` files at a time in separate processes (each holds one 19 MB epoch
    at a time)."""
    from concurrent.futures import ProcessPoolExecutor
    with ProcessPoolExecutor(workers) as ex:
        res = list(ex.map(process_asset, assets))
    return [r for rows in res for r in rows]
