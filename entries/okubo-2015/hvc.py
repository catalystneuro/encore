"""Loading and measures for CRCNS am-3 (Okubo, Mackevicius, Payne, Lynch & Fee 2015, Nature 528,
352-357, doi:10.1038/nature15741).

Data. `Analysis_files.tar.gz` holds one MATLAB `dbase` structure per neuron (electro_gui format):
per song file the syllable segments (`SegmentTimes`, samples at `Fs` = 40 kHz), their labels
(`SegmentTitles`), whether each segment is selected for analysis (`SegmentIsSelected`; calls,
noise and introductory notes are unselected, data descriptor), the spike times (`EventTimes`) and
whether each spike is selected (`EventIsSelected`). `EventTimes` has two rows that hold the same
spikes, about 0.1 ms apart (two parts of one spike detector); row 0 is used. The spreadsheet
`docs/List_of_HVC_neurons.xls` gives per neuron its bird, date, age (dph), song stage and cell
type. Everything is streamed from the public bucket into memory; nothing is written to disk.

Where parameters come from is said at each constant below.
"""
from __future__ import annotations

import collections
import io
import re
import tarfile

import fsspec
import numpy as np
import pandas as pd
import scipy.io as sio

DATASET = "am-3"                 # CRCNS data set, doi:10.6080/K01N7Z2Z
DATASET_VERSION = "unversioned"  # CRCNS data sets are not versioned (docs/archives.md); the MD5 sums are printed
BASE = "https://crcnsarchive.s3-us-west-2.amazonaws.com/am-3/live/"
FS = 40000.0
BIRD_NUMBER = {  # Methods, Animals ("Bird identification key")
    "to3965": 1, "to3779": 2, "to3017": 3, "to5640": 4, "to3396": 5, "to2309": 6,
    "to3412": 7, "to3567": 8, "to2462": 9, "to2331": 10, "to2427": 11, "to3352": 12,
}
STAGES = ["subsong", "protosyll", "multi syll", "motif"]
STAGE_CODE = {s: i + 1 for i, s in enumerate(STAGES)}  # Methods, Statistics, Figure 1f


def read_bytes(path: str) -> bytes:
    with fsspec.open(BASE + path, "rb", block_size=2**22) as f:
        return f.read()


def read_md5() -> dict:
    txt = read_bytes("checksums.md5").decode()
    return {l.split()[1]: l.split()[0] for l in txt.splitlines() if l.strip()}


def neuron_sheet() -> pd.DataFrame:
    """The three tabs of List_of_HVC_neurons.xls, one row per neuron (header row dropped)."""
    xs = pd.read_excel(io.BytesIO(read_bytes("docs/List_of_HVC_neurons.xls")), sheet_name=None)
    rows = []
    for tab, df in xs.items():
        df = df.iloc[1:, :9].copy()
        df.columns = ["bird", "date", "age", "stage", "name", "ch", "iso", "files", "comment"][: df.shape[1]]
        df["tab"] = tab
        rows.append(df)
    out = pd.concat(rows, ignore_index=True)
    out = out[out["bird"].notna()].copy()
    out["date"] = pd.to_datetime(out["date"]).dt.strftime("%Y-%m-%d")
    out["age"] = out["age"].astype(int)
    out["stage"] = out["stage"].str.strip()
    out["key"] = out["bird"] + "_" + out["date"] + "_" + out["name"].str.strip()
    return out


def bird_sheet() -> pd.DataFrame:
    return pd.read_excel(io.BytesIO(read_bytes("docs/List_of_birds.xls")))


def _cells(x, n):
    """Per-file list from a MATLAB cell array squeezed by scipy."""
    if n == 1 and not (isinstance(x, np.ndarray) and x.dtype == object and x.size == 1):
        return [x]
    return list(np.atleast_1d(x))


def _parse(db) -> dict:
    fl = np.atleast_1d(db.FileLength).astype(float)
    n = len(fl)
    segt = _cells(db.SegmentTimes, n)
    titl = _cells(db.SegmentTitles, n)
    ssel = _cells(db.SegmentIsSelected, n)
    et = db.EventTimes
    es = db.EventIsSelected
    if n == 1:
        et = np.asarray(et, dtype=object).reshape(-1, 1)
        es = np.asarray(es, dtype=object).reshape(-1, 1)
    files = []
    for i in range(n):
        st = np.asarray(segt[i], dtype=float).reshape(-1, 2) / FS
        ti = [t if isinstance(t, str) else "" for t in np.atleast_1d(titl[i])] if st.shape[0] else []
        if len(ti) != st.shape[0]:
            ti = (ti + [""] * st.shape[0])[: st.shape[0]]
        se = np.atleast_1d(ssel[i]).astype(bool) if st.shape[0] else np.zeros(0, bool)
        sp = np.atleast_1d(et[0, i]).astype(float) / FS
        sps = np.atleast_1d(es[0, i]).astype(bool)
        sp = np.sort(sp[sps]) if sp.size else sp
        files.append(dict(on=st[:, 0], off=st[:, 1], title=np.array(ti, dtype=object), sel=se,
                          spikes=sp, dur=fl[i] / FS))
    return dict(times=np.atleast_1d(db.Times).astype(float), files=files)


def load_neurons() -> list:
    """All neurons of Analysis_files.tar.gz, parsed; one dict per neuron."""
    raw = read_bytes("Analysis_files.tar.gz")
    tf = tarfile.open(fileobj=io.BytesIO(raw), mode="r:gz")
    out = []
    for m in tf.getmembers():
        if not m.isfile() or not m.name.endswith(".mat"):
            continue
        db = sio.loadmat(io.BytesIO(tf.extractfile(m).read()), squeeze_me=True,
                         struct_as_record=False)["dbase"]
        key = m.name.split("/")[-1][:-4]
        bird, date, name = key.split("_", 2)
        d = _parse(db)
        d.update(key=key, bird=bird, date=date, name=name, folder=m.name.split("/")[1])
        sf = np.atleast_1d(db.SoundFiles)
        d["sound"] = [str(x.name) for x in sf]
        out.append(d)
    return out


# ---------------------------------------------------------------------------------------------
# Syllables, bouts and bursts

BOUT_GAP = 0.300      # s; Methods, Syllable segmentation and bout extraction ("gaps no longer than 300 ms")
BURST_ISI = 0.030     # s; Methods, Definition of bursts ("intervals of 30 ms or less")
MIN_SINGING = 5.0     # s; Methods, Chronic neural recordings ("less than 5 s of singing were excluded")


def syllables(n: dict, labels=None):
    """Selected syllables of a neuron: arrays (file index, onset s, offset s, label).

    Unselected segments (calls, cage noise, introductory notes; data descriptor) are left out.
    `labels`, when given, keeps only syllables whose label is in it.
    """
    fi, on, off, lab = [], [], [], []
    for i, f in enumerate(n["files"]):
        k = f["sel"].copy()
        if labels is not None:
            k &= np.isin(f["title"].astype(str), list(labels))
        fi.append(np.full(k.sum(), i)); on.append(f["on"][k]); off.append(f["off"][k])
        lab.append(f["title"][k].astype(str))
    return (np.concatenate(fi).astype(int), np.concatenate(on), np.concatenate(off),
            np.concatenate(lab))


def bouts(n: dict):
    """Song bouts per file: list over files of an (k, 2) array of bout onset and offset (s).

    A bout is a run of selected syllables separated by gaps of at most BOUT_GAP; onset is the
    first syllable's onset, offset the last one's offset (Methods).
    """
    out = []
    for f in n["files"]:
        on, off = f["on"][f["sel"]], f["off"][f["sel"]]
        o = np.argsort(on); on, off = on[o], off[o]
        if on.size == 0:
            out.append(np.zeros((0, 2))); continue
        b = [[on[0], off[0]]]
        for a, z in zip(on[1:], off[1:]):
            if a - b[-1][1] <= BOUT_GAP:
                b[-1][1] = max(b[-1][1], z)
            else:
                b.append([a, z])
        out.append(np.array(b))
    return out


def singing_time(n: dict) -> float:
    return float(sum((b[:, 1] - b[:, 0]).sum() for b in bouts(n)))


def burst_groups(sp: np.ndarray):
    """Indices splitting a sorted spike train into bursts (ISI <= BURST_ISI; a lone spike is a burst)."""
    if sp.size == 0:
        return []
    cut = np.where(np.diff(sp) > BURST_ISI)[0] + 1
    return np.split(np.arange(sp.size), cut)


def singing_spikes(n: dict):
    """Per bout, the spikes between bout onset and offset, relative to bout onset; with the bout length."""
    out = []
    for f, bb in zip(n["files"], bouts(n)):
        for a, z in bb:
            s = f["spikes"]
            out.append((s[(s >= a) & (s <= z)] - a, z - a))
    return out


# ---------------------------------------------------------------------------------------------
# Event-aligned histograms and the shift test (Methods, Syllable-related neural activity)

HIST_HALF = 0.5   # s; "range: +/- 0.5 s from syllable onsets"
BIN = 0.001       # s; "1 ms bin"
SMOOTH = 20       # bins; "smoothed over 20 bins"; a centred 20-bin moving average (standard choice)
N_SHIFT = 1000    # surrogates; "repeated 1,000 times"
NB = int(round(2 * HIST_HALF / BIN))


def aligned(n: dict, events, files, warp=None, half=2 * HIST_HALF):
    """Spike times relative to each event (s), within +/- `half`; returns (rel, trial index).

    `events` are event times and `files` their file indices; `warp` an optional per-trial factor
    multiplying relative times (linear time-warping of each rendition to the mean duration,
    Methods, Shared and specific neurons, and the population raster plots).
    """
    rel, tri = [], []
    for j, (t, fi) in enumerate(zip(events, files)):
        s = n["files"][fi]["spikes"]
        r = s[(s >= t - half) & (s <= t + half)] - t
        if warp is not None:
            r = r * warp[j]
        rel.append(r); tri.append(np.full(r.size, j))
    if not rel:
        return np.zeros(0), np.zeros(0, int)
    return np.concatenate(rel), np.concatenate(tri)


def _smooth_rows(h):
    k = np.ones(SMOOTH) / SMOOTH
    c = np.cumsum(np.pad(h, ((0, 0), (SMOOTH // 2, SMOOTH - SMOOTH // 2 - 1)), mode="constant"), axis=1)
    c = np.concatenate([np.zeros((h.shape[0], 1)), c], axis=1)
    return c[:, SMOOTH:] - c[:, :-SMOOTH]  # sum over a 20-bin window centred on each bin


def histogram(rel, ntrial):
    """Rate histogram (Hz), 1 ms bins over +/- 0.5 s, smoothed; with the bin centres (s)."""
    keep = np.abs(rel) < HIST_HALF
    b = np.floor((rel[keep] + HIST_HALF) / BIN).astype(int)
    h = np.bincount(b, minlength=NB)[None, :NB].astype(float)
    centres = -HIST_HALF + BIN * (np.arange(NB) + 0.5)
    return _smooth_rows(h)[0] / SMOOTH / max(ntrial, 1) / BIN, centres


def shift_test(rel, tri, ntrial, window, rng, n_surr=N_SHIFT, reading="wide", exclude=None):
    """Peak of the smoothed aligned histogram in `window` (s, s) and its shift-test P.
    `exclude` (s, s), when given, is left out of the window for the real and surrogate peaks.

    Surrogates add one random shift per trial, uniform over +/- 0.5 s (Methods). The Methods do
    not say what happens to spikes shifted past the +/- 0.5 s range (claims header, OPEN ii):
    reading "wide" takes spikes from +/- 1 s and bins those that land within +/- 0.5 s;
    reading "circular" shifts spikes within +/- 0.5 s and wraps them around. P is the fraction
    of surrogate peaks larger than the real one. Returns (peak rate Hz, peak latency s, P).
    """
    centres = -HIST_HALF + BIN * (np.arange(NB) + 0.5)
    win = (centres >= window[0]) & (centres <= window[1])
    if exclude is not None:
        win &= ~((centres >= exclude[0]) & (centres <= exclude[1]))
    h, _ = histogram(rel, ntrial)
    hw = np.where(win, h, -np.inf)
    i = int(np.argmax(hw)); peak = h[i]
    if reading == "circular":
        r0 = rel[np.abs(rel) < HIST_HALF]; t0 = tri[np.abs(rel) < HIST_HALF]
    else:
        r0, t0 = rel, tri
    larger = 0
    chunk = max(1, min(n_surr, int(4e7 // max(r0.size, 1))))
    done = 0
    while done < n_surr:
        k = min(chunk, n_surr - done)
        u = rng.uniform(-HIST_HALF, HIST_HALF, size=(k, ntrial))
        x = r0[None, :] + u[:, t0]
        if reading == "circular":
            x = (x + HIST_HALF) % (2 * HIST_HALF) - HIST_HALF
        ok = np.abs(x) < HIST_HALF
        b = np.floor((x + HIST_HALF) / BIN).astype(int)
        rows = np.broadcast_to(np.arange(k)[:, None], x.shape)
        hh = np.bincount((rows[ok] * NB + b[ok]), minlength=k * NB)[: k * NB].reshape(k, NB)
        sm = _smooth_rows(hh.astype(float)) / SMOOTH / max(ntrial, 1) / BIN
        larger += int((sm[:, win].max(axis=1) > peak).sum())
        done += k
    return float(peak), float(centres[i]), larger / n_surr


# ---------------------------------------------------------------------------------------------
# Rhythmicity (Methods, Quantification of the rhythmic neural activity)

LAG_RANGE = (0.080, 1.000)   # s; IBI, autocorrelation and cepstrum peaks "between 80-1,000 ms"
FREQ_RANGE = (2.0, 15.0)     # Hz; spectrum peak "within the range 2-15 Hz"
MT_WIN = 1.5                 # s; "non-overlapping analysis windows of 1.5 s long"
MT_NW, MT_K = 1.5, 2         # "time-bandwidth product NW = 3/2 and the number of tapers K = 2"
MT_FS = 1000.0               # Hz; spike trains binned at 1 ms for the multitaper estimate (standard choice)
MT_NFFT = 2048               # Chronux's default padding to the next power of 2 (standard choice)
N_SURR_IBI_AC = 1000         # "1,000 times for the IBI and autocorrelation"
N_SURR_SPEC = 100            # "100 times for the spectrum and cepstrum"
ALPHA = 0.05                 # Methods, Statistics


def _tapers():
    from scipy.signal.windows import dpss
    n = int(round(MT_WIN * MT_FS))
    return dpss(n, MT_NW, Kmax=MT_K) * np.sqrt(MT_FS)  # Chronux scales tapers by sqrt(Fs)


_TAPERS = None


def _bout_bursts(n):
    """Per bout: (bout length, list of bursts as arrays of spike times relative to bout onset)."""
    out = []
    for sp, T in singing_spikes(n):
        out.append((T, [sp[g] for g in burst_groups(sp)]))
    return out


def _surrogate_bout(T, bursts, rng, k):
    """`k` surrogate spike trains of one bout: the bursts placed at random within the bout, kept
    whole, with more than BURST_ISI between bursts (Methods). Placement is drawn uniformly over
    all non-overlapping arrangements (bursts in random order, free time split by sorted uniform
    draws), which gives the same arrangements as the paper's sequential placement with
    re-drawing; an implementation choice. Returns an array (k, nspikes), each row sorted."""
    nb = len(bursts)
    if nb == 0:
        return np.zeros((k, 0))
    offs = [b - b[0] for b in bursts]
    w = np.array([o[-1] for o in offs])
    free = T - w.sum() - (nb - 1) * BURST_ISI
    if free <= 0:  # too dense to rearrange; keep the bout as it is
        sp = np.concatenate(bursts)
        return np.broadcast_to(np.sort(sp), (k, sp.size)).copy()
    u = np.sort(rng.uniform(0, free, size=(k, nb)), axis=1)
    order = np.argsort(rng.random((k, nb)), axis=1)
    wo = w[order] + BURST_ISI
    starts = u + np.concatenate([np.zeros((k, 1)), np.cumsum(wo, axis=1)[:, :-1]], axis=1)
    sizes = np.array([o.size for o in offs])
    flat_off = np.concatenate(offs)
    first = np.concatenate([[0], np.cumsum(sizes)[:-1]])
    out = np.empty((k, flat_off.size))
    for r in range(k):
        # place burst order[r, j] at starts[r, j]
        st = np.empty(nb); st[order[r]] = starts[r]
        out[r] = np.repeat(st, sizes) + flat_off
    out.sort(axis=1)
    return out


def _lag_hist(trains_per_bout, kind, nbin_ms):
    """Histograms (k, nb) of IBIs (kind 'ibi', of burst times) or of spike-pair lags (kind 'ac')
    from k parallel trains per bout; bins of 1 ms over 0 to 1 s."""
    k = trains_per_bout[0].shape[0] if trains_per_bout else 1
    nb = 1000
    H = np.zeros((k, nb))
    nspk = 0
    for x in trains_per_bout:
        if x.shape[1] < 2:
            nspk += x.shape[1]; continue
        if kind == "ibi":
            # burst times: centre of mass of spike groups, per train
            for r in range(k):
                g = burst_groups(x[r])
                bt = np.array([x[r][i].mean() for i in g])
                d = np.diff(bt)
                b = np.floor(d / 0.001).astype(int); b = b[b < nb]
                H[r] += np.bincount(b, minlength=nb)[:nb]
        else:
            nspk += x.shape[1]
            d = x[:, None, :] - x[:, :, None]          # (k, m, m), positive above the diagonal
            iu = np.triu_indices(x.shape[1], 1)
            d = d[:, iu[0], iu[1]]
            b = np.floor(d / 0.001).astype(int)
            ok = (b >= 0) & (b < nb)
            rows = np.broadcast_to(np.arange(k)[:, None], b.shape)
            H += np.bincount(rows[ok] * nb + b[ok], minlength=k * nb)[: k * nb].reshape(k, nb)
    if kind == "ac":
        H = H / max(nspk, 1) / 0.001   # conditional firing rate (Hz) given a spike at lag 0
    return H


def _lag_peak(H, reading):
    """Peak height and lag (s) in LAG_RANGE. Reading 'a': 1 ms bins smoothed over 20 bins;
    reading 'b': 10 ms bins (claims header, OPEN bin widths)."""
    if reading == "a":
        Hs = _smooth_rows(H) / SMOOTH
        lags = (np.arange(H.shape[1]) + 0.5) * 0.001
    else:
        Hs = H[:, : (H.shape[1] // 10) * 10].reshape(H.shape[0], -1, 10).sum(axis=2) / 10
        lags = (np.arange(Hs.shape[1]) + 0.5) * 0.010
    m = (lags >= LAG_RANGE[0]) & (lags <= LAG_RANGE[1])
    i = np.argmax(Hs[:, m], axis=1)
    return Hs[:, m].max(axis=1), lags[m][i]


def _spectra(trains_per_bout_T):
    """Multitaper spectra of 1.5 s windows (k, nwin, nfreq) from k parallel trains per bout."""
    global _TAPERS
    if _TAPERS is None:
        _TAPERS = _tapers()
    n = _TAPERS.shape[1]
    segs = []
    for x, T in trains_per_bout_T:
        nw = int(T // MT_WIN)   # windows shorter than 1.5 s at the end of a bout are dropped
        for j in range(nw):
            a = j * MT_WIN
            k = x.shape[0]
            cnt = np.zeros((k, n))
            ok = (x >= a) & (x < a + MT_WIN)
            rows = np.broadcast_to(np.arange(k)[:, None], x.shape)[ok]
            b = np.floor((x[ok] - a) * MT_FS).astype(int)
            np.add.at(cnt, (rows, b), 1.0)
            segs.append(cnt)
    if not segs:
        return None
    X = np.stack(segs, axis=1)                       # (k, nwin, n)
    X = X - X.mean(axis=2, keepdims=True)            # point-process mean subtraction (Chronux)
    J = np.fft.rfft(X[:, :, None, :] * _TAPERS[None, None], n=MT_NFFT, axis=3)
    return (np.abs(J) ** 2).mean(axis=2) / MT_FS     # (k, nwin, nfreq)


def _spec_cep_peaks(S):
    f = np.fft.rfftfreq(MT_NFFT, 1 / MT_FS)
    fm = (f >= FREQ_RANGE[0]) & (f <= FREQ_RANGE[1])
    Sm = S.mean(axis=1)
    spec_peak = Sm[:, fm].max(axis=1)
    q = np.arange(MT_NFFT) / MT_FS
    qm = (q >= LAG_RANGE[0]) & (q <= LAG_RANGE[1])
    eps = 1e-12
    cep_a = np.fft.irfft(np.log(Sm + eps), n=MT_NFFT, axis=1)[:, qm].max(axis=1)
    cep_b = np.fft.irfft(np.log(S + eps), n=MT_NFFT, axis=2).mean(axis=1)[:, qm].max(axis=1)
    return spec_peak, cep_a, cep_b


def rhythmicity(n: dict, rng, n_ibi_ac=N_SURR_IBI_AC, n_spec=N_SURR_SPEC) -> dict:
    """The four rhythm measures of a neuron with their surrogate P values, under both readings of
    the histogram bins (a, b) and of the cepstrum (a: of the mean spectrum, b: mean of window
    cepstra). Rhythmic when at least two of the four are significant; period is the lag of the
    largest autocorrelation peak in 80 to 1,000 ms."""
    bb = _bout_bursts(n)
    real = [np.sort(np.concatenate(b))[None, :] if b else np.zeros((1, 0)) for T, b in bb]
    Ts = [T for T, b in bb]
    out = {}
    Hi = _lag_hist(real, "ibi", 1); Ha = _lag_hist(real, "ac", 1)
    for rd in "ab":
        out[f"ibi_peak_{rd}"], out[f"ibi_lag_{rd}"] = [float(v[0]) for v in _lag_peak(Hi, rd)]
        out[f"ac_peak_{rd}"], out[f"period_{rd}"] = [float(v[0]) for v in _lag_peak(Ha, rd)]
    S = _spectra(list(zip(real, Ts)))
    out["n_windows"] = 0 if S is None else S.shape[1]
    if S is not None:
        sp, ca, cb = _spec_cep_peaks(S)
        out["spec_peak"], out["cep_peak_a"], out["cep_peak_b"] = float(sp[0]), float(ca[0]), float(cb[0])
        f = np.fft.rfftfreq(MT_NFFT, 1 / MT_FS); fm = (f >= FREQ_RANGE[0]) & (f <= FREQ_RANGE[1])
        out["spec_freq"] = float(f[fm][np.argmax(S.mean(axis=1)[0, fm])])
    # surrogates
    sur = [_surrogate_bout(T, b, rng, n_ibi_ac) for T, b in bb]
    Hi_s = _lag_hist(sur, "ibi", 1); Ha_s = _lag_hist(sur, "ac", 1)
    for rd in "ab":
        out[f"p_ibi_{rd}"] = float((_lag_peak(Hi_s, rd)[0] > out[f"ibi_peak_{rd}"]).mean())
        out[f"p_ac_{rd}"] = float((_lag_peak(Ha_s, rd)[0] > out[f"ac_peak_{rd}"]).mean())
    if S is not None:
        sur2 = [s[:n_spec] for s in sur]
        S2 = _spectra(list(zip(sur2, Ts)))
        sp2, ca2, cb2 = _spec_cep_peaks(S2)
        out["p_spec"] = float((sp2 > out["spec_peak"]).mean())
        out["p_cep_a"] = float((ca2 > out["cep_peak_a"]).mean())
        out["p_cep_b"] = float((cb2 > out["cep_peak_b"]).mean())
    else:
        out["p_spec"] = out["p_cep_a"] = out["p_cep_b"] = np.nan
    for rb in "ab":          # bins reading
        for rc in "ab":      # cepstrum reading
            sig = [out[f"p_ibi_{rb}"] < ALPHA, out[f"p_ac_{rb}"] < ALPHA,
                   out["p_spec"] < ALPHA, out[f"p_cep_{rc}"] < ALPHA]
            out[f"rhythmic_{rb}{rc}"] = int(sum(bool(s) for s in sig) >= 2)
    return out


def burst_shape(n: dict):
    """Median burst width (s) and median within-burst firing rate (Hz) over singing bursts of
    two or more spikes (Methods, Definition of bursts); with the number of such bursts."""
    w, r = [], []
    for sp, T in singing_spikes(n):
        for g in burst_groups(sp):
            if g.size >= 2:
                s = sp[g]; w.append(s[-1] - s[0]); r.append(1.0 / np.mean(np.diff(s)))
    if not w:
        return np.nan, np.nan, 0
    return float(np.median(w)), float(np.median(r)), len(w)


# ---------------------------------------------------------------------------------------------
# Per-neuron summary: locking, bout-related activity, rhythmicity, burst shape

LOCK_WINDOW = (-0.050, 0.200)    # s; Methods, Syllable-related neural activity
PRE_BOUT_WINDOW = (-0.300, 0.0)  # s; Methods, Bout-related neural activity ("300 ms window before bout onset")
POST_BOUT_WINDOW = (0.0, 0.300)  # s; "in a 300 ms window after bout-offset"
SAME_LATENCY = 0.025             # s; "a peak at a similar latency (less than 25 ms apart)"
SEED = 20151217                  # fixed seed (standard choice); each neuron and analysis has its own stream


def neuron_rng(key: str, analysis: str):
    import zlib
    return np.random.default_rng([SEED, zlib.crc32(key.encode()), zlib.crc32(analysis.encode())])


def neuron_summary(n: dict, rhythm=True) -> dict:
    """Locking to syllable onsets, pre- and post-bout activity (both shift readings), rhythmicity
    and burst shape of one neuron."""
    out = dict(key=n["key"], singing_s=singing_time(n))
    fi, on, off, lab = syllables(n)
    out["n_syll"] = int(on.size)
    rel, tri = aligned(n, on, fi)
    for rd in ("wide", "circular"):
        pk, lat, p = shift_test(rel, tri, on.size, LOCK_WINDOW, neuron_rng(n["key"], "lock" + rd), reading=rd)
        out[f"lock_peak_{rd}"], out[f"lock_lat_{rd}"], out[f"lock_p_{rd}"] = pk, lat, p
    bb = bouts(n)
    bfi = np.concatenate([np.full(len(b), i) for i, b in enumerate(bb)]).astype(int)
    bon = np.concatenate([b[:, 0] for b in bb]); boff = np.concatenate([b[:, 1] for b in bb])
    out["n_bouts"] = int(bon.size)
    for name, ev, win in (("pre", bon, PRE_BOUT_WINDOW), ("post", boff, POST_BOUT_WINDOW)):
        rel, tri = aligned(n, ev, bfi)
        for rd in ("wide", "circular"):
            pk, lat, p = shift_test(rel, tri, ev.size, win, neuron_rng(n["key"], name + rd), reading=rd)
            out[f"{name}_peak_{rd}"], out[f"{name}_lat_{rd}"], out[f"{name}_p_{rd}"] = pk, lat, p
    w, r, nb = burst_shape(n)
    out.update(burst_width=w, burst_rate=r, n_bursts2=nb)
    if rhythm:
        out.update(rhythmicity(n, neuron_rng(n["key"], "rhythm")))
    return out


def summarise_all(neurons, processes=3, rhythm=True):
    """neuron_summary over all neurons, in `processes` worker processes."""
    import multiprocessing as mp
    from functools import partial
    ctx = mp.get_context("fork")
    with ctx.Pool(processes) as pool:
        rows = pool.map(partial(neuron_summary, rhythm=rhythm), neurons, chunksize=4)
    return pd.DataFrame(rows)


# ---------------------------------------------------------------------------------------------
# Shared and specific neurons (Methods, Shared and specific neurons)

PRE_ONSET = 0.030    # s; "between 30 ms before syllable onset
POST_OFFSET = 0.010  # s; and 10 ms after syllable offset"


def type_test(n: dict, labels, align="onset", reading="wide", tag="", adjust=False, inner=False, exclude=None):
    """Shift test of one neuron for one syllable type (a set of dataset labels).

    Spike times are linearly time-warped to the type's mean duration (factor mean/duration
    applied to times relative to the alignment point) and the 1 ms, 20-bin smoothed histogram's
    peak is taken between 30 ms before onset and 10 ms after offset of the mean syllable, then
    tested as for syllable locking. Returns dict(n_syll, mean_dur, peak, lat, p) or None when the
    neuron has no rendition of the type. `inner=True` searches and tests the peak within the
    syllable itself (onset to mean offset), the window used when the paper's adjustment applies
    (see `pair_table`). `adjust=True` is the "margin rule" variant: every peak in the 30 ms before
    onset or the 10 ms after offset is searched again within the syllable, whether or not the
    neighbouring syllable also detects the burst (the author's first rule, kept as a variant).
    `exclude` (s from onset, s from onset) leaves that part out of the window (see `_double`)."""
    fi, on, off, lab = syllables(n, labels)
    if on.size == 0:
        return None
    dur = off - on
    md = float(dur.mean())
    warp = md / dur
    if align == "onset":
        ev, win = on, ((0.0, md) if inner else (-PRE_ONSET, md + POST_OFFSET))
    else:
        ev, win = off, ((-md, 0.0) if inner else (-(md + PRE_ONSET), POST_OFFSET))
    rel, tri = aligned(n, ev, fi, warp=warp)
    stream = f"{'adj' if inner else 'excl' if exclude is not None else 'type'}{tag}{''.join(sorted(labels))}{align}{reading}"
    ex = None if exclude is None else ((exclude[0], exclude[1]) if align == "onset" else (exclude[0] - md, exclude[1] - md))
    pk, lat, p = shift_test(rel, tri, on.size, win, neuron_rng(n["key"], stream), reading=reading, exclude=ex)
    if align == "offset":
        lat = lat + md  # latency from (mean) onset, so onset- and offset-aligned latencies compare
    if adjust and not inner and not (0.0 <= lat <= md):
        return type_test(n, labels, align, reading, tag, inner=True)
    return dict(n_syll=int(on.size), mean_dur=md, peak=pk, lat=lat, p=p)


def neighbour(n: dict, labels, side):
    """The syllable next to the renditions of a type: for side 'after' the next selected syllable
    in the same bout (gap at most BOUT_GAP), for 'before' the previous one. Returns (most common
    label, median gap in s, fraction of renditions with that neighbour) or None."""
    found = []
    for f in n["files"]:
        k = f["sel"]
        on, off, ti = f["on"][k], f["off"][k], f["title"][k].astype(str)
        o = np.argsort(on); on, off, ti = on[o], off[o], ti[o]
        for j in np.flatnonzero(np.isin(ti, list(labels))):
            if side == "after" and j + 1 < on.size and on[j + 1] - off[j] <= BOUT_GAP:
                found.append((ti[j + 1], on[j + 1] - off[j]))
            if side == "before" and j > 0 and on[j] - off[j - 1] <= BOUT_GAP:
                found.append((ti[j - 1], on[j] - off[j - 1]))
    if not found:
        return None
    lab = collections.Counter(x for x, _ in found).most_common(1)[0][0]
    gaps = [g for x, g in found if x == lab]
    nrend = int(syllables(n, labels)[1].size)
    return lab, float(np.median(gaps)), len(gaps) / max(nrend, 1)


EDGE = 0.003   # s; a peak this close to the window's edge is the tail of a burst outside it (standard choice)


def _double(n, X, rX, label_sets, align, reading, cache):
    """The paper's adjustment, as a rule (assumption): "adjusted the interval if necessary to
    avoid the same burst being detected twice (that is, being associated with an offset of one
    syllable and an onset of the next syllable)" (Methods, Shared and specific neurons).

    When type X's peak lies outside the syllable (in the 30 ms before onset or the 10 ms after
    offset), the neighbouring syllable Y on that side (`neighbour`) is tested with the same test.
    The burst is detected twice when Y's test is significant and its peak lies within SAME_LATENCY
    (25 ms; the Methods' "similar latency" of the bout-related analysis) of the time of X's peak,
    measured from Y's onset with the median gap between them. The burst's time is taken from the
    peak that is not at the edge of its window (EDGE), and the burst is left to the syllable whose
    window [-30 ms, offset + 10 ms] holds it furthest from an edge. The other syllable's window
    then leaves out SAME_LATENCY on either side of the burst, and its peak is searched and tested
    again. Returns dict(dbl, owner 'X' or 'Y', Y label set, burst time from X's and from Y's onset)
    or None when the burst is not detected twice."""
    if rX is None:
        return None
    md, L = rX["mean_dur"], rX["lat"]
    if 0.0 <= L <= md:
        return None
    side = "after" if L > md else "before"
    nb = neighbour(n, X, side)
    if nb is None:
        return None
    ylab, gap, frac = nb
    Y = next((s for s in label_sets if ylab in s), {ylab})
    key = "".join(sorted(Y))
    if key not in cache:
        cache[key] = type_test(n, Y, align, reading)
    rY = cache[key]
    if rY is None or not rY["p"] < ALPHA:
        return None
    mdY = rY["mean_dur"]
    shift = -(md + gap) if side == "after" else mdY + gap      # time from Y's onset = time from X's onset + shift
    if abs(rY["lat"] - (L + shift)) > SAME_LATENCY:
        return None
    def edge(lat, m):
        return min(lat + PRE_ONSET, m + POST_OFFSET - lat) < EDGE
    eX, eY = edge(L, md), edge(rY["lat"], mdY)
    tX = L if (eY or not eX) and not (eX and not eY) else rY["lat"] - shift
    if eX and eY:
        tX = (L + rY["lat"] - shift) / 2
    tY = tX + shift
    dX = min(tX + PRE_ONSET, md + POST_OFFSET - tX)
    dY = min(tY + PRE_ONSET, mdY + POST_OFFSET - tY)
    return dict(owner="X" if dX >= dY else "Y", Y=Y, tX=tX, tY=tY, nb=ylab)


def pair_table(neurons, A, B, align="onset", reading="wide", adjust=False):
    """For each neuron, the type test for syllable types A and B (sets of labels); class
    'shared' (both significant), 'specific_A', 'specific_B' or 'none'.

    `adjust`: False (no adjustment, "raw"), "double" (the main reading: the window is adjusted
    only when the same burst is detected in the neighbouring syllable, `_double`), or "margin"
    (variant: every peak outside the syllable is searched again inside it, `type_test(adjust=True)`).
    Columns out_X, dbl_X and adj_X say, per type, whether the peak lay outside the syllable,
    whether the neighbouring syllable detected the same burst, and whether X's window was adjusted;
    lat0_X and p0_X are the unadjusted peak latency and P."""
    rows = []
    for n in neurons:
        res = {"A": type_test(n, A, align, reading), "B": type_test(n, B, align, reading)}
        raw = dict(res)
        sets = {"A": A, "B": B}
        inf = {nm: dict(out=False, dbl=False, adj=False, nb="") for nm in "AB"}
        for nm in "AB":
            r = raw[nm]
            inf[nm]["out"] = r is not None and not (0.0 <= r["lat"] <= r["mean_dur"])
        if adjust == "margin":
            res = {nm: type_test(n, sets[nm], align, reading, adjust=True) for nm in "AB"}
            for nm in "AB":
                inf[nm]["adj"] = inf[nm]["out"]
        elif adjust == "double":
            cache = {"".join(sorted(A)): raw["A"], "".join(sorted(B)): raw["B"]}
            for nm, other in (("A", "B"), ("B", "A")):
                if inf[nm]["adj"]:
                    continue
                d = _double(n, sets[nm], raw[nm], (A, B), align, reading, cache)
                if d is None:
                    continue
                inf[nm]["dbl"] = True; inf[nm]["nb"] = d["nb"]
                if d["owner"] == "Y":
                    tgt, t = nm, d["tX"]
                elif d["Y"] == sets[other]:
                    tgt, t = other, d["tY"]
                    inf[other]["dbl"] = True
                else:
                    continue
                if not inf[tgt]["adj"]:
                    res[tgt] = type_test(n, sets[tgt], align, reading, exclude=(t - SAME_LATENCY, t + SAME_LATENCY))
                    inf[tgt]["adj"] = True
        sa = res["A"] is not None and res["A"]["p"] < ALPHA; sb = res["B"] is not None and res["B"]["p"] < ALPHA
        cls = "shared" if sa and sb else "specific_A" if sa else "specific_B" if sb else "none"
        row = dict(key=n["key"], cls=cls)
        for nm in "AB":
            r = res[nm]
            for k in ("n_syll", "mean_dur", "peak", "lat", "p"):
                row[f"{k}_{nm}"] = np.nan if r is None else r[k]
            row[f"lat0_{nm}"] = np.nan if raw[nm] is None else raw[nm]["lat"]
            row[f"p0_{nm}"] = np.nan if raw[nm] is None else raw[nm]["p"]
            for k in ("out", "dbl", "adj", "nb"):
                row[f"{k}_{nm}"] = inf[nm][k]
        rows.append(row)
    return pd.DataFrame(rows)


def bias(r1, r2):
    """Bias = 1 - min(r1, r2) / max(r1, r2) (Methods, Quantification of the activity level difference)."""
    return 1.0 - np.minimum(r1, r2) / np.maximum(r1, r2)


# ---------------------------------------------------------------------------------------------
# Protosyllables (Methods, Syllable classification and labelling)

EXP_FIT_RANGE = (0.200, 0.400)  # s; "best-fit exponential distribution (using 200-400 ms)"
PROTO_SD = 2.0                  # "within two standard deviations from the mean of this Gaussian"
DUR_BIN = 0.005                 # s; duration histogram bin (standard choice)


def protosyllable_range(durations):
    """Duration range (s) of protosyllables: fit an exponential to the duration histogram over
    200-400 ms, subtract it, fit a Gaussian to the residual, keep mean +/- 2 s.d. (Methods).
    Returns (lo, hi, mu, sd) or None when no fit is possible."""
    from scipy.optimize import curve_fit
    d = np.asarray(durations)
    edges = np.arange(0, 0.6 + DUR_BIN, DUR_BIN)
    h, _ = np.histogram(d, edges)
    c = edges[:-1] + DUR_BIN / 2
    m = (c >= EXP_FIT_RANGE[0]) & (c <= EXP_FIT_RANGE[1])
    try:
        pe, _ = curve_fit(lambda x, a, k: a * np.exp(-k * x), c[m], h[m], p0=(max(h[m].max(), 1) * 10, 10), maxfev=10000)
        res = h - pe[0] * np.exp(-pe[1] * c)
        pg, _ = curve_fit(lambda x, a, mu, s: a * np.exp(-0.5 * ((x - mu) / s) ** 2), c, res,
                          p0=(max(res.max(), 1), c[np.argmax(res)], 0.03), maxfev=10000)
    except Exception:
        return None
    mu, sd = pg[1], abs(pg[2])
    return mu - PROTO_SD * sd, mu + PROTO_SD * sd, mu, sd


def participation(n: dict, fi, on, off):
    """1 for each syllable with at least one spike from 30 ms before onset to 10 ms after offset
    (Methods, Quantification of the probabilistic neural activity), else 0."""
    out = np.zeros(on.size, int)
    for j, (f, a, z) in enumerate(zip(fi, on, off)):
        s = n["files"][f]["spikes"]
        out[j] = int(np.any((s >= a - PRE_ONSET) & (s <= z + POST_OFFSET)))
    return out


def burst_latencies(n: dict, fi, on, window=LOCK_WINDOW):
    """Burst times (centre of mass) relative to each syllable onset, within `window`, pooled."""
    out = []
    for f, a in zip(fi, on):
        s = n["files"][f]["spikes"]
        s = s[(s >= a + window[0] - 0.1) & (s <= a + window[1] + 0.1)]
        for g in burst_groups(s):
            t = s[g].mean() - a
            if window[0] <= t <= window[1]:
                out.append(t)
    return np.array(out)


def type_lock_any(n: dict, bonferroni=False):
    """Reading (iii b) of syllable locking: each labelled syllable type tested on its own
    (onset-aligned, as for locking); locked when any type is significant, optionally with
    Bonferroni over types. Returns (number of types tested, locked)."""
    fi, on, off, lab = syllables(n)
    types = [t for t in np.unique(lab) if t]
    if not types:
        return 0, np.nan
    ps = []
    for t in types:
        k = lab == t
        rel, tri = aligned(n, on[k], fi[k])
        ps.append(shift_test(rel, tri, int(k.sum()), LOCK_WINDOW, neuron_rng(n["key"], "locktype" + t))[2])
    thr = ALPHA / len(types) if bonferroni else ALPHA
    return len(types), int(min(ps) < thr)


def type_lock_all(neurons, processes=3):
    import multiprocessing as mp
    with mp.get_context("fork").Pool(processes) as pool:
        a = pool.map(type_lock_any, neurons, chunksize=4)
    return a


def simultaneous_pairs(neurons):
    """Pairs of neurons of the same bird and day that share song files (the same sound file
    names), i.e. recorded simultaneously on different channels."""
    by = {}
    for n in neurons:
        by.setdefault((n["bird"], n["date"]), []).append(n)
    out = []
    for (b, d), ns in by.items():
        for i in range(len(ns)):
            for j in range(i + 1, len(ns)):
                fa = {f for f in ns[i]["sound"]}; fb = {f for f in ns[j]["sound"]}
                common = fa & fb
                if common:
                    out.append((ns[i]["key"], ns[j]["key"], len(common)))
    return out


# ---------------------------------------------------------------------------------------------
# Coverage (Methods, Analysis of coverage by HVC projection neuron bursts)

COV_SMOOTH = 0.009            # s; "9 ms sliding square window, 1 ms steps"
COV_THRESH = {"protosyll": 2.0, "older": 10.0}   # Hz; "2 Hz for protosyllable stage birds; 10 Hz ... older juveniles"
COV_MIN_RENDITIONS = 0.25     # "at least one spike ... on at least 25% of the renditions"
COV_PULSE = 0.005             # s; "5 ms postsynaptic square pulse (beginning at the spike time)"
COV_OVERLAP = 3               # "at least three of these post-synaptic pulses overlapped"
COV_MIN_NEURONS = 10          # "more than 10 neurons bursting within the syllable window"
COV_N_SURR = 1000             # "1,000 surrogate data sets"


def coverage_patches(n: dict, labels, thresh, fi_on_off=None, md_common=None):
    """Covered patches (boolean over 1 ms steps of the window from 30 ms before onset to 10 ms
    after the mean offset) of one neuron for one syllable type, one patch per kept burst
    window. Spikes are time-warped to the mean duration, as in the paper's population rasters
    (the coverage Methods do not say; an assumption). `md_common`, when given, is the duration
    every rendition is warped to (one window shared by all neurons of a syllable, as in a
    population raster); otherwise the neuron's own mean duration is used. Returns (list of
    patches, window length)."""
    if fi_on_off is None:
        fi, on, off, _ = syllables(n, labels)
    else:
        fi, on, off = fi_on_off
    if on.size == 0:
        return [], 0
    md = float((off - on).mean()) if md_common is None else float(md_common)
    t0, t1 = -PRE_ONSET, md + POST_OFFSET
    nb = int(round((t1 - t0) / BIN))
    rel, tri = aligned(n, on, fi, warp=md / (off - on), half=1.0)
    k = (rel >= t0) & (rel < t1)
    rel, tri = rel[k], tri[k]
    b = np.floor((rel - t0) / BIN).astype(int).clip(0, nb - 1)
    h = np.bincount(b, minlength=nb)[:nb] / on.size / BIN
    w = int(round(COV_SMOOTH / BIN))
    hs = np.convolve(h, np.ones(w) / w, mode="same")
    above = hs > thresh
    patches = []
    i = 0
    while i < nb:
        if not above[i]:
            i += 1; continue
        j = i
        while j < nb and above[j]:
            j += 1
        m = (b >= i) & (b < j)
        if np.unique(tri[m]).size >= COV_MIN_RENDITIONS * on.size:
            cnt = np.zeros(nb + 10)
            for s in b[m]:
                cnt[s: s + int(round(COV_PULSE / BIN))] += 1
            patches.append(cnt[:nb] >= COV_OVERLAP)
        i = j
    return patches, nb


def coverage(patch_lists, nb, rng, n_surr=COV_N_SURR):
    """Covered fraction (patches of all neurons combined by OR) and the 2.5 and 97.5 percentiles
    of the fraction when each patch is circularly shifted by a random offset."""
    allp = [p for ps in patch_lists for p in ps]
    if not allp:
        return np.nan, np.nan, np.nan
    real = np.any(np.array(allp), axis=0).mean()
    P = np.array(allp)
    sur = np.empty(n_surr)
    for s in range(n_surr):
        sh = rng.integers(0, nb, size=len(allp))
        idx = (np.arange(nb)[None, :] - sh[:, None]) % nb
        sur[s] = np.any(np.take_along_axis(P, idx, axis=1), axis=0).mean()
    return float(real), float(np.percentile(sur, 2.5)), float(np.percentile(sur, 97.5))


def peak_latency(n: dict, labels, align="onset", warp=True):
    """Latency (s) of the peak of the smoothed histogram aligned to onset or offset, in the window
    from 30 ms before onset to 10 ms after offset of the mean syllable, relative to the alignment
    point; with or without linear time-warping (a variant for the latency correlations, whose
    Methods passage speaks of "syllable onset- or offset-aligned histograms" without warping)."""
    fi, on, off, _ = syllables(n, labels)
    if on.size == 0:
        return np.nan
    md = float((off - on).mean())
    ev = on if align == "onset" else off
    rel, tri = aligned(n, ev, fi, warp=(md / (off - on)) if warp else None)
    h, c = histogram(rel, on.size)
    win = (-PRE_ONSET, md + POST_OFFSET) if align == "onset" else (-(md + PRE_ONSET), POST_OFFSET)
    w = (c >= win[0]) & (c <= win[1])
    lat = float(c[w][np.argmax(h[w])])
    inner = (0.0, md) if align == "onset" else (-md, 0.0)
    if not (inner[0] <= lat <= inner[1]):   # the same adjustment as type_test(adjust=True)
        w = (c >= inner[0]) & (c <= inner[1])
        lat = float(c[w][np.argmax(h[w])])
    return lat
