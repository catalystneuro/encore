"""Loading and measures for CRCNS fcx-2 (Johnson et al. 2018, PLoS Biology 16, e2004274).

The data set holds, per subject, a tar.gz with the filtered continuous data (data_primary.mat),
the preprocessed bipolar data (data_derived.mat, MATLAB 7.3, FieldTrip structures data_pre,
data_encmain and data_proc), a per-trial table (summary_file_trial.csv) and electrode
coordinates. The tar files are streamed from the public S3 bucket and read member by member in
memory; nothing is written to disk. Only the derived data of the analysed channels
(docs/summary_channel_analysis.csv) are kept.

Where the parameters come from. "Code" is the analysis code deposited with the data
(analysis_scripts.tar.gz in the data set, scripts dated 2018-02-22 to 2018-04-03); "Methods" is
the paper's Materials and methods; M1 to M10 are the shared method details of the claims file.

- Segment windows (M1): the code (power_compute.m, psi_compute.m, cspsi_compute.m,
  "cfgt.latency") takes encoding and precue as [0, 1.5] s of data_encmain, the precue delay as
  [0.6, 1.5] s of data_encmain (M1 reading (a)), the postcue delay as [0.3, 1.2] s of data_proc
  and the baseline as [0.65, 0.85] s of data_pre (`WIN_CODE`). The trial table and the
  descriptor place each segment's first sample (-1.5 s) at the table's epoch start, which puts
  the same events 1.5 s earlier: encoding [-1.5, 0], precue [-0.9, 0], postcue [-1.2, -0.3],
  baseline [-0.85, -0.65] s (`WIN`). The main reading is the table's placement, an assumption
  resting on the data: the 900 and 1150 ms delay trials part where it puts the first event that
  depends on the delay, in all three segments, and not where the code's windows put it
  (sanity_subject). ERPs, power, PLV and both PSI measures are also computed in the code's
  windows (`WIN_ALT`), as a variant; PAC is computed in the main windows only. The table's
  windows start 0 to 0.65 s after a segment's first sample, inside the low filters' edge
  transient; `edge_check` measures this for power by joining the three segments of a trial.
- Filter bank (M2): the 24 band edges of power_compute.m (`BANDS`), the last band dropped for the
  512 Hz subjects s8 and s9 (code). Two-pass FIR filters designed as FieldTrip's default for
  `bpfilttype = 'fir'` (fir1 with a Hamming window, order 3 * fix(fs / low edge), capped at a
  third of the padded length); this design is FieldTrip's, which the code calls. Segments are zero
  padded to 7.5 s (Methods, Spectral decomposition; code `padding = 7.5`). Analytic amplitude by
  the Hilbert transform; power is its square (Methods).
- Baseline z (M3): bootstrap of the pooled baseline power, r = number of correct trials, 1000
  draws without replacement (code zbaseline.m, `randsample`), z = (power - mean) / SD of the
  bootstrap means. The z is affine in power per channel and frequency, so the trial mean of z
  equals the z of the trial mean (M3 readings (a) and (b) give the same number).
- Down-sampling to 50 ms: polyphase resampling with a Kaiser window (beta 5, 100 * max(p, q)
  taps each side), which is what MATLAB's resample(x, p, q, 100) in resamplemtx.m does.
- Cluster permutation (M4): FieldTrip's montecarlo cluster test as configured in
  erp_compute.m and power_compute.m: independent-samples t (two-tailed, cluster threshold at
  t for p = 0.025 each tail) or F (one-tailed, threshold at p = 0.05), cluster statistic the sum
  of t or F, 1000 permutations of the condition labels, cluster p doubled for the two-tailed t
  test (`correcttail = 'prob'`), significant at p < 0.05. Clusters never join electrodes
  (`neighbours = []`). The null is the maximum cluster sum per permutation either over all of a
  subject's electrodes tested together (what the code does, as it passes all channels at once)
  or per electrode (Methods, "clustered per electrode"); both are returned.
- ERPs: 30 Hz low-pass two-pass FIR, order 3 * fix(fs / 30), segments zero padded to 7.5 s
  (Methods, ERPs; code erp_compute.m).
- ERP subtraction for phase measures: the mean over correct trials is subtracted from each
  correct trial (code subtracterp.m with ncond = 1; for PAC per condition, ncond = 3, Methods,
  PAC paragraph 2).
- Theta spectra for PSI (M5): the code (psi_compute.m) runs FieldTrip mtmfft with a Hanning
  taper over the whole 900 ms window, zero padded to 4 s, at 3 to 7 Hz; FieldTrip ignores
  `t_ftimwin` for mtmfft. The Methods describe sliding 3-cycle windows (M5 of the claims file),
  which cannot be placed inside a 900 ms segment at 3 Hz (a 1 s window); they are the reading
  the claims are judged on, run into the zero padding, and the code's single window is a
  variant (`theta_fourier`).
- PSI (Nolte et al. 2008, ref. 30 of the paper): coherency from the cross-spectrum averaged over
  trials (and windows), PSI = Im(sum_f conj(C_f) C_(f+1)), positive when the first signal leads.
  Null: the frequencies of the second signal shuffled, 1000 times; z = (PSI - mean) / SD
  (Methods, PSI paragraph 2). The code's own form (`psianalysis.m`: the trial mean of per-trial
  PSI, z-scored against frequency-shuffled trial-mean coherency) is a variant (`psi_code`).
- Cross-spectral PSI (M6): theta Fourier coefficients of the amplitude envelopes of the 17 bands
  centred at 9.5 to 152.5 Hz (16 for s8 and s9) of the code (cspsi_compute.m), z per band, then
  averaged over bands.
- PAC (M9): circular-linear correlation (code circ_corrcl.m) across the trials of a condition at
  each time point and amplitude band, 100 surrogates, z = (PAC - mean) / SD. Surrogate reading
  (a): the amplitudes permuted across trials, a new permutation per band (code pacanalysis.m,
  `ampvec(randperm(...), :)`); reading (b): the amplitude bands shuffled within each trial.
"""

from __future__ import annotations

import io
import tarfile
import time

import h5py
import numpy as np
import pandas as pd
import requests
from scipy import fft as sfft
from scipy import ndimage, signal, stats

DATASET = "fcx-2"
VERSION = "unversioned"   # CRCNS data sets are not versioned; the files read are under live/
BASE = "https://crcnsarchive.s3-us-west-2.amazonaws.com/fcx-2/live"
SUBJECTS = [f"s{i}" for i in range(1, 11)]

BANDS = np.array([[1, 3], [1.5, 4], [2, 5], [3, 6], [4, 7], [5, 8], [6, 10], [7, 12], [9, 14],
                  [10, 17], [12, 20], [15, 24], [17, 28], [20, 33], [24, 40], [29, 48], [34, 57],
                  [40, 67], [47, 81], [57, 96], [67, 114], [80, 135], [94, 162], [113, 192]])
CENTRES = BANDS.mean(axis=1)
AMP_BANDS = np.arange(7, 24)        # 7-12 ... 113-192 Hz, centres 9.5 to 152.5 Hz
PLV_BANDS = np.arange(0, 11)        # 1-3 ... 12-20 Hz (code plv_compute.m)
PEAK_BANDS = np.arange(1, 7)        # 1.5-4 ... 6-10 Hz, the 6 ranges of M8
THETA_FREQS = np.arange(3, 8)       # 3 to 7 Hz (M5)

# The deposited code's windows (cfgt.latency in every *_compute.m script).
WIN_CODE = {"enc": ("encmain", 0.0, 1.5), "pre": ("encmain", 0.6, 1.5), "post": ("proc", 0.3, 1.2),
            "base": ("pre", 0.65, 0.85)}
# The same windows placed by the trial table and the descriptor: the first sample of each
# segment (time -1.5 s) is the table's epoch start (encmain at column H, first stimulus onset;
# proc 0.3 s before column I, test cue offset; pre about 0.1 s after column G, 1 s before the
# start screen), so every window lies 1.5 s earlier than the code takes it. The main reading:
# the 900 and 1150 ms delay trials part where this placement puts the first event that depends
# on the delay, in each segment (sanity_subject, "jitter_t").
SHIFT_TABLE = -1.5
WIN = {k: (s, t0 + SHIFT_TABLE, t1 + SHIFT_TABLE) for k, (s, t0, t1) in WIN_CODE.items()}
WIN_ALT = WIN_CODE
PAD_S = 7.5


# ---------------------------------------------------------------- loading

def read_channel_table():
    """docs/summary_channel_analysis.csv as one row per analysed channel."""
    text = requests.get(f"{BASE}/docs/summary_channel_analysis.csv", timeout=60).text
    df = pd.read_csv(io.StringIO(text), header=None, skiprows=2)
    df[0] = df[0].ffill()
    cols = {1: ("MTL", "L"), 2: ("MTL", "R"), 3: ("PFC", "L"), 4: ("PFC", "R"),
            5: ("OFC", "L"), 6: ("OFC", "R")}
    rows = []
    for _, r in df.iterrows():
        for c, (reg, hemi) in cols.items():
            if isinstance(r[c], str) and r[c].strip():
                rows.append({"subject": r[0].lower(), "region": reg, "hemi": hemi, "label": r[c].strip()})
    return pd.DataFrame(rows)


def read_summary_file():
    text = requests.get(f"{BASE}/docs/summary_file.csv", timeout=60).text
    names = ["subject", "age", "sex", "acc_identity", "acc_spatial", "acc_temporal",
             "rt_identity", "rt_spatial", "rt_temporal"]
    df = pd.read_csv(io.StringIO(text), header=None, names=names)
    df["subject"] = df.subject.str.lower()
    return df


def read_scripts():
    """The deposited analysis scripts (analysis_scripts.tar.gz), as {file name: text}; read to
    quote the lines a method detail is taken from, not run."""
    raw = requests.get(f"{BASE}/analysis_scripts.tar.gz", timeout=120).content
    out = {}
    with tarfile.open(fileobj=io.BytesIO(raw), mode="r:gz") as tf:
        for m in tf:
            if m.isfile() and m.name.endswith(".m"):
                out[m.name.split("/")[-1]] = tf.extractfile(m).read().decode("latin-1")
    return out


TRIAL_COLS = ["trial", "accuracy", "trial_type", "condition", "jitter", "rt",
              "pre_start", "enc_start", "post_start"]


def _h5str(f, ref):
    return "".join(map(chr, f[ref][()].ravel()))


def load_subject(sid, channels):
    """Stream one subject's tar.gz and return its trial table and the analysed channels' data.

    `channels` is the list of analysed labels for this subject. Returns a dict with the trial
    table, the derived structures' labels, fsample, trialinfo, sampleinfo and time axes, and per
    segment an array (trials, channels, samples) in float32.
    """
    t0 = time.time()
    url = f"{BASE}/data_indiv/{sid}.tar.gz"
    out = {"subject": sid, "members": {}}
    with requests.get(url, stream=True, timeout=120) as resp:
        resp.raise_for_status()
        tf = tarfile.open(fileobj=resp.raw, mode="r|gz", bufsize=2 ** 20)
        for m in tf:
            if not m.isfile():
                continue
            out["members"][m.name] = m.size
            if m.name.endswith("summary_file_trial.csv"):
                out["trials"] = pd.read_csv(tf.extractfile(m), header=None, names=TRIAL_COLS)
            elif m.name.endswith("data_derived.mat"):
                raw = tf.extractfile(m).read()
                out.update(_read_derived(raw, channels))
                del raw
    out["load_s"] = time.time() - t0
    return out


def _read_derived(raw, channels):
    res = {}
    with h5py.File(io.BytesIO(raw), "r") as f:
        for seg in ["pre", "encmain", "proc"]:
            g = f[f"data_{seg}"]
            labels = [_h5str(f, r) for r in g["label"][()].ravel()]
            idx = [labels.index(c) for c in channels]
            trefs = g["trial"][()].ravel()
            tms = [f[r][()].ravel() for r in g["time"][()].ravel()]
            # trials can differ in length by a few samples; keep the samples all trials share,
            # from the common first time
            starts = np.array([t[0] for t in tms])
            nmin = min(len(t) for t in tms)
            tm = tms[0][:nmin]
            x = np.stack([f[r][()][:nmin, idx].T for r in trefs]).astype(np.float32)
            res[seg] = {
                "labels": labels, "fs": float(g["fsample"][()].ravel()[0]),
                "trialinfo": g["trialinfo"][()].T, "sampleinfo": g["sampleinfo"][()].T,
                "time": tm, "x": x,
                "hdr_fs": float(g["hdr"]["Fs"][()].ravel()[0]),
                "same_start": bool(np.allclose(starts, starts[0])),
                "n_samples": np.array([len(t) for t in tms]),
            }
    return {"seg": res}


# ---------------------------------------------------------------- spectral tools

def fir_order(fs, low, npad):
    n = 3 * int(np.fix(fs / low))
    return int(min(n, np.floor((npad - 1) / 3)))


def _twopass_gain(b, nfft):
    h = np.fft.fft(b, nfft)
    return np.abs(h) ** 2


def bandpass_gain(lo, hi, fs, nfft, npad):
    n = fir_order(fs, lo, npad)
    b = signal.firwin(n + 1, [lo, hi], pass_zero=False, fs=fs)
    return _twopass_gain(b, nfft)


def lowpass_gain(hi, fs, nfft, npad):
    n = 3 * int(np.fix(fs / hi))
    n = int(min(n, np.floor((npad - 1) / 3)))
    b = signal.firwin(n + 1, hi, fs=fs)
    return _twopass_gain(b, nfft)


class Padder:
    """Zero pad a segment (..., T) to `PAD_S` s, centred, and FFT it."""

    def __init__(self, T, fs, pad_s=PAD_S):
        self.T, self.fs = T, fs
        self.npad = max(int(round(pad_s * fs)), T)
        self.left = (self.npad - T) // 2
        self.nfft = sfft.next_fast_len(self.npad + 2 * 3 * int(fs) + 2)
        f = np.fft.fftfreq(self.nfft, 1 / fs)
        self.hil = np.where(f > 0, 2.0, 0.0)
        self.hil[0] = 1.0
        if self.nfft % 2 == 0:
            self.hil[self.nfft // 2] = 1.0

    def fft(self, x):
        buf = np.zeros(x.shape[:-1] + (self.nfft,), dtype=np.float64)
        buf[..., self.left:self.left + self.T] = x
        return np.fft.fft(buf, axis=-1)

    def back(self, X, analytic):
        y = np.fft.ifft(X * self.hil if analytic else X, axis=-1)
        y = y[..., self.left:self.left + self.T]
        return y if analytic else y.real


def window_index(time_axis, t0, t1):
    """Samples of `time_axis` from t0 to t1, as ft_selectdata picks them (nearest samples)."""
    i0 = int(np.argmin(np.abs(time_axis - t0)))
    i1 = int(np.argmin(np.abs(time_axis - t1)))
    return np.arange(i0, i1 + 1)


def hilbert_bands(x, fs, bands, sel, analytic=True, pad=None):
    """Analytic signal of x (trials, ch, T) in each band, kept at samples `sel`.

    Returns complex64 (trials, ch, nband, len(sel)).
    """
    pad = pad or Padder(x.shape[-1], fs)
    X = pad.fft(x)
    out = np.empty(x.shape[:2] + (len(bands), len(sel)), dtype=np.complex64)
    for k, (lo, hi) in enumerate(bands):
        g = bandpass_gain(lo, hi, fs, pad.nfft, pad.npad)
        y = pad.back(X * g, analytic=True)
        out[:, :, k, :] = y[..., sel]
    return out


_RESAMPLE_CACHE = {}


def resample_20hz(x, fs):
    """Down-sample the last axis to 20 Hz as MATLAB resample(x, p, q, 100) (resamplemtx.m).

    The resampler is linear, so it is applied as a matrix built once per length and rate.
    """
    T = x.shape[-1]
    key = (T, fs)
    if key not in _RESAMPLE_CACHE:
        from fractions import Fraction
        fr = Fraction(20, int(round(fs))).limit_denominator(1000)
        p, q = fr.numerator, fr.denominator
        m = max(p, q)
        h = signal.firwin(2 * 100 * m + 1, 1.0 / m, window=("kaiser", 5.0))  # resample_poly scales by p
        n_new = int(np.floor((T - 1) / fs * 20)) + 1
        if n_new % 2 == 0:
            n_new += 1
        R = signal.resample_poly(np.eye(T), p, q, axis=-1, window=h)[:, :n_new]
        _RESAMPLE_CACHE[key] = R
    R = _RESAMPLE_CACHE[key]
    return x @ R.astype(x.dtype if x.dtype in (np.float32, np.float64) else np.float64)


def baseline_bootstrap(base_pow, ntrials, rng, nperm=1000):
    """Mean and SD of the bootstrap distribution of baseline means (zbaseline.m).

    base_pow: (trials, ch, band, T). Returns two arrays (ch, band).
    """
    _, nch, nb, _ = base_pow.shape
    pool = base_pow.transpose(1, 2, 0, 3).reshape(nch, nb, -1)
    npool = pool.shape[-1]
    dist = np.empty((nch, nb, nperm))
    for z in range(nperm):
        pick = rng.choice(npool, size=ntrials, replace=False)
        dist[:, :, z] = pool[:, :, pick].mean(axis=-1)
    return dist.mean(axis=-1), dist.std(axis=-1, ddof=1)


# ---------------------------------------------------------------- cluster permutation test

def _stat(X, groups, kind):
    """t (two groups) or F (k groups) for each column of X (n, M); groups is (P, n) int labels."""
    P = groups.shape[0]
    labels = np.unique(groups[0])
    sums, sq, ns = [], [], []
    X2 = X * X
    for g in labels:
        G = (groups == g).astype(X.dtype)
        sums.append(G @ X)
        sq.append(G @ X2)
        ns.append(G.sum(axis=1)[:, None])
    if kind == "t":
        m1, m2 = sums[0] / ns[0], sums[1] / ns[1]
        v1 = (sq[0] - ns[0] * m1 ** 2) / (ns[0] - 1)
        v2 = (sq[1] - ns[1] * m2 ** 2) / (ns[1] - 1)
        sp = ((ns[0] - 1) * v1 + (ns[1] - 1) * v2) / (ns[0] + ns[1] - 2)
        return (m1 - m2) / np.sqrt(sp * (1 / ns[0] + 1 / ns[1]))
    n = X.shape[0]
    grand = X.sum(axis=0) / n
    ssb = sum(ns[k] * (sums[k] / ns[k] - grand) ** 2 for k in range(len(labels)))
    ssw = sum(sq[k] - sums[k] ** 2 / ns[k] for k in range(len(labels)))
    k = len(labels)
    return (ssb / (k - 1)) / (ssw / (n - k))


_STRUCT = None


def _cluster_sums(stat, thr, sign, shape):
    """Cluster sums per electrode for one map. stat: (ch, *dims). Returns list per channel of sums."""
    mask = (stat * sign) > thr
    nd = len(shape)
    struct = np.zeros((3,) * (nd + 1), dtype=bool)
    c = (1,) * (nd + 1)
    struct[c] = True
    for ax in range(1, nd + 1):
        for d in (0, 2):
            idx = list(c)
            idx[ax] = d
            struct[tuple(idx)] = True
    lab, nlab = ndimage.label(mask, structure=struct)
    if nlab == 0:
        return np.zeros(0), np.zeros(0, dtype=int)
    sums = np.bincount(lab.ravel(), weights=(stat * sign).ravel(), minlength=nlab + 1)[1:]
    chan_of = np.array([sl[0].start for sl in ndimage.find_objects(lab)])
    return sums, chan_of


def cluster_test(data, labels, kind, rng, nperm=1000, chunk=50):
    """FieldTrip-style cluster permutation test, independently per electrode (no neighbours).

    data: (trials, ch, *dims). labels: (trials,) condition codes.
    Returns a DataFrame with, per electrode, the smallest cluster p under the subject-wide max
    null (`p_subject`, what the code does) and under the per-electrode max null (`p_electrode`),
    and the number of observed clusters.
    """
    n, nch = data.shape[:2]
    dims = data.shape[2:]
    X = data.reshape(n, -1).astype(np.float64)
    lab = np.asarray(labels)
    ulab = np.unique(lab)
    codes = np.searchsorted(ulab, lab)
    if kind == "t":
        df = n - 2
        thr = stats.t.ppf(1 - 0.025, df)
        signs = (1, -1)
    else:
        thr = stats.f.ppf(1 - 0.05, len(ulab) - 1, n - len(ulab))
        signs = (1,)
    obs = _stat(X, codes[None, :], kind)[0].reshape((nch,) + dims)
    null_subj = {s: np.zeros(nperm) for s in signs}
    null_chan = {s: np.zeros((nperm, nch)) for s in signs}
    done = 0
    while done < nperm:
        P = min(chunk, nperm - done)
        perms = np.stack([rng.permutation(codes) for _ in range(P)])
        st = _stat(X, perms, kind).reshape((P, nch) + dims)
        for i in range(P):
            for s in signs:
                sums, chan = _cluster_sums(st[i], thr, s, dims)
                if len(sums):
                    null_subj[s][done + i] = sums.max()
                    mx = np.zeros(nch)
                    np.maximum.at(mx, chan, sums)
                    null_chan[s][done + i] = mx
        done += P
    rows = []
    factor = 2.0 if kind == "t" else 1.0
    best_s, best_e, ncl = np.ones(nch), np.ones(nch), np.zeros(nch, dtype=int)
    for s in signs:
        sums, chan = _cluster_sums(obs, thr, s, dims)
        for v, c in zip(sums, chan):
            ncl[c] += 1
            ps = (np.sum(null_subj[s] >= v) + 1) / (nperm + 1) * factor
            pe = (np.sum(null_chan[s][:, c] >= v) + 1) / (nperm + 1) * factor
            best_s[c], best_e[c] = min(best_s[c], ps), min(best_e[c], pe)
    for c in range(nch):
        rows.append({"ch": c, "p_subject": min(best_s[c], 1.0), "p_electrode": min(best_e[c], 1.0),
                     "n_clusters": int(ncl[c])})
    return pd.DataFrame(rows)


# ---------------------------------------------------------------- theta Fourier and PSI

def hanning_matlab(n):
    k = np.arange(1, n + 1)
    return 0.5 * (1 - np.cos(2 * np.pi * k / (n + 1)))


def theta_fourier(x, fs, mode="mtmfft", step_s=0.05):
    """Fourier coefficients at 3 to 7 Hz of x (trials, ch, T), demeaned per trial.

    mode "mtmfft": one Hanning window over the segment, zero padded to 4 s (code).
    mode "sliding": 3-cycle Hanning windows centred every `step_s` over the segment, the data
    zero padded to 4 s so that a window may run into the padding (Methods' sliding windows).
    Returns complex (trials, ch, 5, nwin).
    """
    if mode != "mtmfft" and x.shape[1] > 32:
        return np.concatenate([theta_fourier(x[:, i:i + 32], fs, mode, step_s)
                               for i in range(0, x.shape[1], 32)], axis=1)
    x = x - x.mean(axis=-1, keepdims=True)
    T = x.shape[-1]
    if mode == "mtmfft":
        nfft = int(round(4 * fs))
        tap = hanning_matlab(T)
        X = np.fft.rfft(x * tap, n=nfft, axis=-1)
        fr = np.fft.rfftfreq(nfft, 1 / fs)
        idx = [int(np.argmin(np.abs(fr - f))) for f in THETA_FREQS]
        return X[..., idx][..., None]
    npad = int(round(4 * fs))
    left = (npad - T) // 2
    buf = np.zeros(x.shape[:-1] + (npad,))
    buf[..., left:left + T] = x
    centres = left + np.arange(0, T, int(round(step_s * fs)))
    out = []
    for f in THETA_FREQS:
        L = int(round(3 / f * fs))
        tap = hanning_matlab(L)
        kern = tap * np.exp(-2j * np.pi * f * np.arange(L) / fs)
        cols = []
        for c in centres:
            a = c - L // 2
            cols.append(buf[..., a:a + L] @ kern)
        out.append(np.stack(cols, axis=-1))
    return np.stack(out, axis=-2)


def cross_spectra(A, B):
    """Trial- and window-averaged cross-spectra between frequencies.

    A: (trials, na, 5, w), B: (trials, nb, 5, w). Returns S (na, nb, 5, 5) with
    S[a, b, f, g] = mean over trials and windows of A[a, f] conj(B[b, g]), and the powers
    PA (na, 5), PB (nb, 5).
    """
    S = np.einsum("rafw,rbgw->abfg", A, np.conj(B)) / (A.shape[0] * A.shape[-1])
    PA = (np.abs(A) ** 2).mean(axis=(0, 3))
    PB = (np.abs(B) ** 2).mean(axis=(0, 3))
    return S, PA, PB


def cross_spectra_x(th, the):
    """Trial- and window-averaged cross-spectra of theta (n, a, 5, w) with envelope theta
    (n, b, c, 5, w). Returns (a, b, c, 5, 5), as cross_spectra, one matrix product per
    frequency pair."""
    n, na, nf, nw = th.shape
    nb, nc = the.shape[1:3]
    A2 = th.transpose(2, 1, 0, 3).reshape(nf, na, n * nw)
    B2 = np.conj(the).transpose(3, 0, 4, 1, 2).reshape(nf, n * nw, nb * nc)
    S = np.empty((na, nb * nc, nf, nf), dtype=complex)
    for f in range(nf):
        for g in range(nf):
            S[:, :, f, g] = A2[f] @ B2[g]
    return S.reshape(na, nb, nc, nf, nf) / (n * nw)


def psi_z(S, PA, PB, rng, nperm=1000):
    """Nolte PSI and its z against shuffles of the second signal's frequencies.

    S: (..., 5, 5) cross-spectra between frequencies; PA (..., 5), PB (..., 5).
    Returns raw PSI (...) and z (...).
    """
    nf = S.shape[-1]
    diag = np.arange(nf)

    def psi_for(perm):
        C = S[..., diag, perm] / np.sqrt(PA * PB[..., perm])
        return np.imag(np.conj(C[..., :-1]) * C[..., 1:]).sum(axis=-1)

    raw = psi_for(diag)
    null = np.stack([psi_for(rng.permutation(nf)) for _ in range(nperm)], axis=-1)
    return raw, (raw - null.mean(axis=-1)) / null.std(axis=-1, ddof=1)


def psi_code(A, B, rng, nperm=1000):
    """The deposited code's form of PSI (psianalysis.m), with the cross-spectrum conjugated.

    Observed: the trial mean of per-trial PSI from per-trial normalised cross-spectra. Null:
    trial-mean normalised cross-spectra with both frequency axes shuffled independently. A and B
    are (trials, n, 5, 1) for the pairs to compute (A[:, i] with B[:, i]).
    """
    cs = A[..., 0] * np.conj(B[..., 0])                      # (trials, n, 5)
    pp = cs / np.abs(cs)
    per_trial = np.imag(np.conj(pp[..., :-1]) * pp[..., 1:]).sum(axis=-1)
    obs = per_trial.mean(axis=0)
    ppm = pp.mean(axis=0)                                    # (n, 5)
    nf = ppm.shape[-1]
    null = np.stack([np.imag(np.conj(ppm[:, rng.permutation(nf)]) * ppm[:, rng.permutation(nf)]).sum(axis=-1)
                     for _ in range(nperm)], axis=-1)
    return obs, (obs - null.mean(axis=-1)) / null.std(axis=-1, ddof=1)


def _psi_code_pairs(th, ij, shape, rng, perm=None):
    """psi_code for the electrode pairs `ij` of theta coefficients th (n, ch, 5, 1), as
    (ch, ch) arrays of raw and z (NaN off the pairs). `perm` shuffles the second signal's trials."""
    out = {"raw": np.full(shape, np.nan), "z": np.full(shape, np.nan)}
    if ij:
        ia, ib = np.array(ij).T
        B = th[:, ib] if perm is None else th[perm][:, ib]
        out["raw"][ia, ib], out["z"][ia, ib] = psi_code(th[:, ia], B, rng)
    return out


# ---------------------------------------------------------------- PAC

def circ_corrcl_trials(phase, amp):
    """Circular-linear correlation across trials (axis 0), as circ_corrcl.m.

    phase: (trials, T); amp: (P, trials, F, T). Returns (P, F, T).
    """
    n = phase.shape[0]

    def zs(v, axis):
        v = v - v.mean(axis=axis, keepdims=True)
        return v / np.sqrt((v * v).sum(axis=axis, keepdims=True))

    s, c = zs(np.sin(phase), 0), zs(np.cos(phase), 0)
    rcs = (s * c).sum(axis=0)                               # (T,)
    za = zs(amp, 1)
    rxs = np.einsum("prft,rt->pft", za, s)
    rxc = np.einsum("prft,rt->pft", za, c)
    rho2 = (rxc ** 2 + rxs ** 2 - 2 * rxc * rxs * rcs) / (1 - rcs ** 2)
    return np.sqrt(np.clip(rho2, 0, None))


def pac_z(phase, amp, rng, reading="a", nsurr=100, chunk=25):
    """PAC z per amplitude band and time. phase (trials, T); amp (trials, F, T)."""
    n, F, T = amp.shape
    obs = circ_corrcl_trials(phase, amp[None])[0]
    surr = np.empty((nsurr, F, T), dtype=np.float32)
    for a in range(0, nsurr, chunk):
        P = min(chunk, nsurr - a)
        if reading == "a":
            # one trial permutation per surrogate and band
            perm = np.stack([np.stack([rng.permutation(n) for _ in range(F)], axis=1) for _ in range(P)])  # (P, n, F)
            sh = amp[perm, np.arange(F)[None, None, :], :]
        else:
            # the amplitude bands shuffled within each trial
            perm = np.stack([np.stack([rng.permutation(F) for _ in range(n)]) for _ in range(P)])  # (P, n, F)
            sh = amp[np.arange(n)[None, :, None], perm, :]
        surr[a:a + P] = circ_corrcl_trials(phase, sh)
    return (obs - surr.mean(axis=0)) / surr.std(axis=0, ddof=1)


# ---------------------------------------------------------------- balanced split-plot F tests

def within_unit_anova(Y, groups=None):
    """F tests of the within-unit effects of a balanced factorial table, per unit.

    Y: (units, a, b, c) with factors in that order (condition, frequency, time). With random
    intercepts for unit (and subject) and a balanced design, a linear mixed model's F tests of
    the within-unit effects equal these (the unit intercepts absorb all between-unit variance).
    `groups` (units,) of 0/1 adds a between-unit factor (direction): its interactions with the
    within effects are tested here (sum-to-zero coding, type III), its main effect separately.
    Returns a DataFrame of effect, df, F, p, and the residual df.
    """
    U = Y.shape[0]
    dims = Y.shape[1:]
    letters = "abc"[: len(dims)]
    Yc = Y - Y.mean(axis=tuple(range(1, Y.ndim)), keepdims=True)
    # projections onto effect subspaces by inclusion-exclusion of marginal means
    from itertools import combinations
    effects = []
    for k in range(1, len(dims) + 1):
        effects += list(combinations(range(len(dims)), k))

    def marg(Z, keep):
        axes = tuple(i + 1 for i in range(len(dims)) if i not in keep)
        return Z.mean(axis=axes, keepdims=True) if axes else Z

    proj = {}
    for e in effects:
        p = np.zeros_like(Yc)
        for k in range(0, len(e) + 1):
            for sub in combinations(e, k):
                sgn = (-1) ** (len(e) - k)
                p = p + sgn * np.broadcast_to(marg(Yc, sub), Yc.shape)
        proj[e] = p
    ncell = int(np.prod(dims))
    rows = []
    if groups is None:
        res_ss, res_df = 0.0, 0
        for e in effects:
            m = proj[e].mean(axis=0)
            res_ss += ((proj[e] - m) ** 2).sum()
            res_df += (U - 1) * int(np.prod([dims[i] - 1 for i in e]))
        for e in effects:
            df = int(np.prod([dims[i] - 1 for i in e]))
            ss = U * (proj[e].mean(axis=0) ** 2).sum()
            F = (ss / df) / (res_ss / res_df)
            rows.append({"effect": e, "df": df, "ss": ss, "F": F, "p": stats.f.sf(F, df, res_df)})
        out = pd.DataFrame(rows)
        out.attrs.update(res_ss=res_ss, res_df=res_df)
        return out, res_df
    g = np.asarray(groups)
    n1, n2 = (g == 0).sum(), (g == 1).sum()
    vf = (1 / n1 + 1 / n2) / 4
    res_ss, res_df = 0.0, 0
    for e in effects:
        m1, m2 = proj[e][g == 0].mean(axis=0), proj[e][g == 1].mean(axis=0)
        res_ss += ((proj[e][g == 0] - m1) ** 2).sum() + ((proj[e][g == 1] - m2) ** 2).sum()
        res_df += (U - 2) * int(np.prod([dims[i] - 1 for i in e]))
    for e in effects:
        df = int(np.prod([dims[i] - 1 for i in e]))
        m1, m2 = proj[e][g == 0].mean(axis=0), proj[e][g == 1].mean(axis=0)
        for name, c in [(e, (m1 + m2) / 2), (("D",) + e, (m1 - m2) / 2)]:
            ss = (c ** 2).sum() / vf
            F = (ss / df) / (res_ss / res_df)
            rows.append({"effect": name, "df": df, "ss": ss, "F": F, "p": stats.f.sf(F, df, res_df)})
    out = pd.DataFrame(rows)
    out.attrs.update(res_ss=res_ss, res_df=res_df)
    return out, res_df


# ---------------------------------------------------------------- per-subject analysis

def seed_for(name, sid):
    """A fixed seed per analysis and subject, so each claim's numbers have their own generator."""
    return int.from_bytes(f"{name}|{sid}".encode(), "little") % (2 ** 32)


def _filter_chunks(x, fs, sel, bands, out_kind, chunk=6):
    """Band-filtered Hilbert outputs of x (trials, ch, T) at samples `sel`, channel chunks.

    out_kind: "power" (amplitude squared), "abs", "angle" or "complex". Returns float32 or
    complex64 (trials, ch, nband, len(sel)); with a list of index arrays for `sel`, a list of
    such arrays from one filtering pass.
    """
    sels = sel if isinstance(sel, list) else [sel]
    pad = Padder(x.shape[-1], fs)
    dtype = np.complex64 if out_kind == "complex" else np.float32
    outs = [np.empty(x.shape[:2] + (len(bands), len(s)), dtype=dtype) for s in sels]
    gains = [bandpass_gain(lo, hi, fs, pad.nfft, pad.npad) for lo, hi in bands]
    for c0 in range(0, x.shape[1], chunk):
        X = pad.fft(x[:, c0:c0 + chunk].astype(np.float64))
        for k, g in enumerate(gains):
            yall = pad.back(X * g, analytic=True)
            for s, out in zip(sels, outs):
                y = yall[..., s]
                if out_kind == "power":
                    y = np.abs(y) ** 2
                elif out_kind == "abs":
                    y = np.abs(y)
                elif out_kind == "angle":
                    y = np.angle(y)
                out[:, c0:c0 + chunk, k, :] = y
    return outs if isinstance(sel, list) else outs[0]


def lowpass_erp(x, fs, sel, hi=30.0, chunk=8):
    pad = Padder(x.shape[-1], fs)
    g = lowpass_gain(hi, fs, pad.nfft, pad.npad)
    out = np.empty(x.shape[:2] + (len(sel),), dtype=np.float32)
    for c0 in range(0, x.shape[1], chunk):
        X = pad.fft(x[:, c0:c0 + chunk].astype(np.float64))
        out[:, c0:c0 + chunk] = pad.back(X * g, analytic=False)[..., sel]
    return out


def continuous_trials(sub, correct):
    """The pre, encmain and proc segments of each correct trial joined into one trace by their
    sampleinfo (their overlapping samples are equal, sanity_subject). Returns the traces
    (trials, ch, L) in float32, zero after a trial's last sample, the per-trial offsets of the
    three segments from the start of pre, and the number of samples inside a trace that no
    segment covers."""
    segs = [sub["seg"][k] for k in ("pre", "encmain", "proc")]
    si = [s["sampleinfo"][correct, 0].astype(np.int64) for s in segs]
    offs = [s - si[0] for s in si]
    L = max(int((o + s["x"].shape[-1]).max()) for o, s in zip(offs, segs))
    xs = [s["x"][correct] for s in segs]
    n, nch = xs[0].shape[:2]
    out = np.zeros((n, nch, L), np.float32)
    filled = np.zeros((n, L), bool)
    for i in range(n):
        for o, x in zip(offs, xs):
            out[i, :, o[i]:o[i] + x.shape[-1]] = x[i]
            filled[i, o[i]:o[i] + x.shape[-1]] = True
    last = np.array([np.where(f)[0].max() for f in filled])
    gaps = int(sum((~filled[i, :last[i] + 1]).sum() for i in range(n)))
    return out, offs, gaps


def power_at(x, fs, bands, idxs, chunk=6):
    """Hilbert power of x (trials, ch, T) in each band at per-trial samples: each of `idxs` is
    (trials, k). Returns a list of float32 (trials, ch, nband, k)."""
    pad = Padder(x.shape[-1], fs)
    n, nch = x.shape[:2]
    gains = [bandpass_gain(lo, hi, fs, pad.nfft, pad.npad) for lo, hi in bands]
    outs = [np.empty((n, nch, len(bands), ix.shape[1]), np.float32) for ix in idxs]
    tr = np.arange(n)[:, None]
    for c0 in range(0, nch, chunk):
        X = pad.fft(x[:, c0:c0 + chunk].astype(np.float64))
        for k, g in enumerate(gains):
            y = pad.back(X * g, analytic=True)
            for ix, out in zip(idxs, outs):
                out[:, c0:c0 + chunk, k, :] = (np.abs(y[tr, :, ix]) ** 2).transpose(0, 2, 1)
    return outs


EDGE_BANDS = np.arange(0, 9)       # 1-3 ... 9-14 Hz: the theta, alpha and peak-search bands


def edge_check(sub, correct, bmean, bsd, keep):
    """Filter edge effects of the trial table's windows, which start 0.65 s (baseline), 0 s
    (encoding) and 0.3 s (postcue) after the first sample of their segment.

    - Encoding and postcue: power at the same samples filtered from their own segment (as in
      the main analysis) and from the joined trace, which has 1.8 s (encoding) and about 2.3 s
      (postcue) of data before them. The baseline z of the joined trace's power (main baseline
      mean and SD) is the edge-reduced variant of power-theta-sustained and theta-peak-bands.
    - Baseline: no data precede it, so its edge effect is measured where it can be, at an
      interior window of the same length 1.0 s into encmain: power from the joined trace against
      power from a 4.5 s cut of it that starts as far before the window as pre starts before the
      baseline.
    """
    fs = sub["seg"]["encmain"]["fs"]
    bands = BANDS[EDGE_BANDS]
    tr, offs, gaps = continuous_trials(sub, correct)
    n = tr.shape[0]
    _, esel = segment(sub, "enc")
    _, psel = segment(sub, "post")
    _, bsel = segment(sub, "base")
    ref0 = offs[1] + int(round(1.0 * fs))
    idx = {"enc": offs[1][:, None] + esel[None], "post": offs[2][:, None] + psel[None],
           "ref": ref0[:, None] + np.arange(len(bsel))[None]}
    p_tr = dict(zip(idx, power_at(tr, fs, bands, list(idx.values()))))
    Tpre = sub["seg"]["pre"]["x"].shape[-1]
    start = ref0 - bsel[0]
    cut = np.stack([tr[i, :, start[i]:start[i] + Tpre] for i in range(n)])
    p_cut = power_at(cut, fs, bands, [np.tile(bsel, (n, 1))])[0]
    del tr, cut
    p_seg = {"enc": _filter_chunks(sub["seg"]["encmain"]["x"][correct], fs, esel, bands, "power"),
             "post": _filter_chunks(sub["seg"]["proc"]["x"][correct], fs, psel, bands, "power")}
    out = {"gaps": gaps, "bands": bands}
    # trial-mean power, segment (or cut) over joined trace, per electrode and band
    pb_cut, pb_ref = p_cut.mean(axis=(0, 3)), p_tr["ref"].mean(axis=(0, 3))
    out["base_ratio"] = pb_cut / pb_ref                                         # (ch, band)
    out["base_sd_ratio"] = p_cut.mean(axis=3).std(axis=0) / p_tr["ref"].mean(axis=3).std(axis=0)
    nb = int(round(0.25 * fs))
    for w in ("enc", "post"):
        a, b = p_seg[w].mean(axis=0), p_tr[w].mean(axis=0)                     # (ch, band, T)
        T = a.shape[-1]
        out[f"{w}_ratio_bins"] = np.stack([a[..., i:i + nb].mean(-1) / b[..., i:i + nb].mean(-1)
                                           for i in range(0, T - nb // 2, nb)], axis=-1)
    zc = {}
    for w in ("enc", "post"):
        z = (p_tr[w] - bmean[None, :, :len(bands), None]) / bsd[None, :, :len(bands), None]
        if w == "enc":
            pk = z.mean(axis=(0, 3))[keep][:, PEAK_BANDS].mean(axis=0)
            out["peak_curve_all"], out["peak_band_all"] = pk, int(PEAK_BANDS[np.argmax(pk)])
        zc[w] = resample_20hz(z, fs).astype(np.float32).mean(axis=0)
    out["power_z_mean"] = zc
    return out


def segment(sub, name, win=WIN):
    segname, t0, t1 = win[name]
    d = sub["seg"][segname]
    return d, window_index(d["time"], t0, t1)


def n_amp_bands(fs):
    return len(AMP_BANDS) - (1 if fs < 600 else 0)


def _make_pairs(regions, hemis, keep):
    """Same-hemisphere pairs of kept electrodes: MTL-MTL, MTL-PFC and MTL-OFC (PLV section)."""
    pairs = {"MTL-MTL": [], "MTL-PFC": [], "MTL-OFC": []}
    for a in np.where((regions == "MTL") & keep)[0]:
        for b in np.where(keep & (hemis == hemis[a]))[0]:
            if regions[b] == "MTL" and b > a:
                pairs["MTL-MTL"].append((a, b))
            elif regions[b] in ("PFC", "OFC"):
                pairs[f"MTL-{regions[b]}"].append((a, b))
    return pairs


def _plv(wins, pairs, fs):
    """PLV readings per window and pair group (plv_compute.m bands 1-3 ... 12-20 Hz)."""
    plv = {}
    for w, (x, sel) in wins.items():
        A = _filter_chunks(x, fs, sel, BANDS[PLV_BANDS], "complex")
        U = A / np.abs(A)
        out = {}
        for g, pl in pairs.items():
            vals = {"implv": [], "pli": [], "code": []}
            for a, b in pl:
                d = U[:, a] * np.conj(U[:, b])                   # (trials, band, T)
                vals["implv"].append(np.abs(np.imag(d.mean(axis=0))).mean(axis=-1))
                vals["pli"].append(np.abs(np.sign(np.imag(d)).mean(axis=0)).mean(axis=-1))
                dd = np.exp(1j * (np.imag(A[:, a]) - np.imag(A[:, b])))
                vals["code"].append(np.abs(dd.mean(axis=0)).mean(axis=-1))
            out[g] = {k: np.array(v) for k, v in vals.items()}
        plv[w] = out
        del A, U
    return plv


def _psi_block(wins, pairs, fs, amp_bands, sid, tag, calibrate):
    """Theta PSI (M5) and cross-spectral PSI (M6) in the two delay windows, single window
    (mtmfft) and sliding windows, the code's form for the MTL-frontal pairs, and, when
    `calibrate`, the same with the second signal's trials shuffled."""
    psi, cs, keep_th, cs_shuf, keep_shuf = {}, {}, {}, {}, None
    ij = [(a, b) for g in ("MTL-PFC", "MTL-OFC") for a, b in pairs[g]]
    for w, (x, sel) in wins.items():
        env = _filter_chunks(x, fs, sel, amp_bands, "abs")   # filtered on the full segment
        for mode in ("mtmfft", "sliding"):
            rng = np.random.default_rng(seed_for(f"psi|{w}|{mode}{tag}", sid))
            th = theta_fourier(x[..., sel].astype(np.float64), fs, mode)          # (n, ch, 5, w)
            S, PA, PB = cross_spectra(th, th)
            raw, z = psi_z(S, PA[:, None, :], PB[None, :, :], rng)              # (ch, ch)
            psi[(w, mode)] = {"raw": raw, "z": z}
            if mode == "mtmfft":
                psi[(w, "code")] = _psi_code_pairs(th, ij, raw.shape, rng)
            # cross-spectral: theta of each amplitude envelope
            rng = np.random.default_rng(seed_for(f"cspsi|{w}|{mode}{tag}", sid))
            n, nch, nbb, T = env.shape
            the = theta_fourier(env.reshape(n, nch * nbb, T).astype(np.float64), fs, mode)
            the = the.reshape(n, nch, nbb, 5, the.shape[-1])
            Sx = cross_spectra_x(th, the)
            PBx = (np.abs(the) ** 2).mean(axis=(0, 4))                          # (ch, nbb, 5)
            rawx, zx = psi_z(Sx, PA[:, None, None, :], PBx[None, :, :, :], rng)  # (ch, ch, nbb)
            cs[(w, mode)] = {"raw": rawx, "z": zx}
            if mode == "mtmfft":
                keep_th[w] = (th, the)
            if w == "post" and calibrate:
                # calibration: the second signal's trials shuffled against the first's, which
                # removes any trial-by-trial coupling; z should then fall above 1.96 in about
                # 2.5% of pairs
                rng = np.random.default_rng(seed_for(f"psi-shuffle|{mode}", sid))
                perm = rng.permutation(n)
                S0, _, PB0 = cross_spectra(th, th[perm])
                psi[(w, mode, "shuf")] = dict(zip(("raw", "z"), psi_z(S0, PA[:, None, :], PB0[None, :, :], rng)))
                if mode == "mtmfft":
                    psi[(w, "code", "shuf")] = _psi_code_pairs(th, ij, raw.shape, rng, perm)
                the_p = the[perm]
                cs_shuf[mode] = psi_z(cross_spectra_x(th, the_p), PA[:, None, None, :],
                                      PBx[None, :, :, :], rng)[1]
                if mode == "mtmfft":
                    keep_shuf = (th, the_p)
                del the_p
            del the
        del env
    return psi, cs, keep_th, cs_shuf, keep_shuf


def _make_units(regions, hemis, labels, keep, pairs, cs, keep_th, cs_shuf, keep_shuf, sid, tag):
    """Units for cross-spectral directionality and PAC: each kept electrode (phase and
    amplitude from it) and each MTL-frontal pair in both directions, with their mean z and raw
    cross-spectral PSI per window and form."""
    units = []
    for e in np.where(keep)[0]:
        units.append({"system": regions[e], "ph": e, "amp": e})
    for g in ("MTL-PFC", "MTL-OFC"):
        fr = g.split("-")[1]
        for a, b in pairs[g]:
            units.append({"system": f"MTL->{fr}", "ph": a, "amp": b})
            units.append({"system": f"{fr}->MTL", "ph": b, "amp": a})
    extra = [("post_shuf", keep_shuf)] if keep_shuf is not None else []
    for u in units:
        for (w, mode), d in cs.items():
            u[f"z_{w}_{mode}"] = float(d["z"][u["ph"], u["amp"], :].mean())
            u[f"raw_{w}_{mode}"] = float(d["raw"][u["ph"], u["amp"], :].mean())
        u["zf_post_mtmfft"] = cs[("post", "mtmfft")]["z"][u["ph"], u["amp"], :16].copy()
        u["zf_post_sliding"] = cs[("post", "sliding")]["z"][u["ph"], u["amp"], :16].copy()
        for mode, zsh in cs_shuf.items():
            u[f"z_post_{mode}_shuf"] = float(zsh[u["ph"], u["amp"], :].mean())
        for w, (th, the) in list(keep_th.items()) + extra:
            rng = np.random.default_rng(seed_for(f"cspsi-code|{w}|{u['ph']}|{u['amp']}{tag}", sid))
            nbb = the.shape[2]
            A = np.repeat(th[:, [u["ph"]]], nbb, axis=1)
            o, zc = psi_code(A, the[:, u["amp"]], rng)
            u[f"z_{w}_code"], u[f"raw_{w}_code"] = float(zc.mean()), float(o.mean())
            if w == "post":
                u["zf_post_code"] = zc[:16].copy()
        if extra:
            u["z_post_code_shuf"] = u.pop("z_post_shuf_code")
            u.pop("raw_post_shuf_code")
        u["ph_label"], u["amp_label"] = labels[u["ph"]], labels[u["amp"]]
        u["hemi"] = hemis[u["ph"]]
    return units


def analyse_subject(sub, chans, nperm_cluster=1000, pac=True, pac_readings=("a", "b"), log=print):
    """Every per-subject measure the claims use, from one subject's loaded data.

    chans: the subject's rows of the channel table (region, hemi, label), in the order of the
    loaded arrays. Returns a dict of compact results; the raw arrays are not kept.
    """
    sid = sub["subject"]
    res = {"subject": sid, "timing": {}}
    T0 = time.time()
    pre, enc, proc = (sub["seg"][k] for k in ("pre", "encmain", "proc"))
    fs = enc["fs"]
    ti = enc["trialinfo"]
    correct = ti[:, 1] == 1
    res["trialinfo"] = ti
    regions = chans.region.to_numpy()
    hemis = chans.hemi.to_numpy()
    labels = chans.label.tolist()
    nb_all = len(BANDS) - (1 if fs < 600 else 0)
    bands = BANDS[:nb_all]

    xs = {k: sub["seg"][s]["x"][correct] for k, s in (("pre", "pre"), ("enc", "encmain"), ("proc", "proc"))}
    tic = ti[correct]

    # ---- ERPs (erp_compute.m): 30 Hz low-pass, baseline from the trial mean of [0.65, 0.85] s
    # (the code subtracts nanmean(pretrial.trial), the mean over trials of the per-trial baseline
    # means). Variants: each trial's own baseline mean subtracted, and the windows of WIN_ALT.
    _, bsel = segment(sub, "base")
    _, esel = segment(sub, "enc")
    _, psel = segment(sub, "post")
    lp = {k: lowpass_erp(xs[k], fs, np.arange(xs[k].shape[-1])) for k in ("pre", "enc", "proc")}
    for tag, win in (("", WIN), ("_alt", WIN_ALT)):
        sl = {k: window_index(sub["seg"][s]["time"], t0, t1) for k, (s, t0, t1) in win.items()}
        btr = lp["pre"][..., sl["base"]].mean(axis=-1)                     # (trials, ch)
        for btag, base in (("", btr.mean(axis=0)[None, :, None]), ("_trial", btr[:, :, None])):
            if tag == "_alt" and btag:
                continue
            erp_enc = lp["enc"][..., sl["enc"]] - base
            erp_post = lp["proc"][..., sl["post"]] - base
            rng = np.random.default_rng(seed_for(f"erp-no-condition-difference{tag}{btag}", sid)
                                        if tag or btag else seed_for("erp-no-condition-difference", sid))
            res[f"erp_enc{tag}{btag}"] = cluster_test(erp_enc[:, :, None, :], tic[:, 2], "t", rng, nperm_cluster)
            res[f"erp_post{tag}{btag}"] = cluster_test(erp_post[:, :, None, :], tic[:, 3], "F", rng, nperm_cluster)
            if not tag and not btag:
                res["erp_mean"] = {"enc": erp_enc.mean(axis=0), "post": erp_post.mean(axis=0)}
            del erp_enc, erp_post
    del lp
    res["timing"]["erp"] = time.time() - T0

    # ---- power (power_compute.m): Hilbert power, bootstrap baseline z, 50 ms
    # the windows of WIN_ALT come from the same filtering pass
    _, bsel_d = segment(sub, "base", WIN_ALT)
    _, esel_d = segment(sub, "enc", WIN_ALT)
    _, psel_d = segment(sub, "post", WIN_ALT)
    rng = np.random.default_rng(seed_for("power", sid))
    rng_d = np.random.default_rng(seed_for("power|alt", sid))
    bpow, bpow_d = _filter_chunks(xs["pre"], fs, [bsel, bsel_d], bands, "power")
    bmean, bsd = baseline_bootstrap(bpow, int(correct.sum()), rng)
    bmean_d, bsd_d = baseline_bootstrap(bpow_d, int(correct.sum()), rng_d)
    del bpow, bpow_d
    zs, zs_d = {}, {}
    for name, x, sel, sel_d in (("enc", xs["enc"], esel, esel_d), ("post", xs["proc"], psel, psel_d)):
        p, p_d = _filter_chunks(x, fs, [sel, sel_d], bands, "power")
        z = (p - bmean[None, :, :, None]) / bsd[None, :, :, None]
        del p
        zs[name] = resample_20hz(z, fs).astype(np.float32)
        if name == "enc":
            res["enc_time_mean_z"] = z.mean(axis=(0, 3))          # (ch, band), trials and time
        del z
        p_d -= bmean_d[None, :, :, None]
        p_d /= bsd_d[None, :, :, None]
        if name == "enc":
            res["enc_time_mean_z_alt"] = p_d.mean(axis=(0, 3))
        zs_d[name] = resample_20hz(p_d, fs).astype(np.float32)
        del p_d
    res["power_z_mean"] = {k: v.mean(axis=0) for k, v in zs.items()}  # (ch, band, t20)
    res["power_z_mean_alt"] = {k: v.mean(axis=0) for k, v in zs_d.items()}
    res["timing"]["power"] = time.time() - T0
    rng = np.random.default_rng(seed_for("power-condition-exclusions", sid))
    res["pow_enc"] = cluster_test(zs["enc"], tic[:, 2], "t", rng, nperm_cluster)
    res["pow_post"] = cluster_test(zs["post"], tic[:, 3], "F", rng, nperm_cluster)
    rng = np.random.default_rng(seed_for("power-condition-exclusions|alt", sid))
    res["pow_enc_alt"] = cluster_test(zs_d["enc"], tic[:, 2], "t", rng, nperm_cluster)
    res["pow_post_alt"] = cluster_test(zs_d["post"], tic[:, 3], "F", rng, nperm_cluster)
    del zs, zs_d
    res["timing"]["power_test"] = time.time() - T0
    excl = (np.minimum(res["pow_enc"].p_subject, res["pow_post"].p_subject) < 0.05).to_numpy()
    res["excluded"] = excl
    res["excluded_alt"] = (np.minimum(res["pow_enc_alt"].p_subject, res["pow_post_alt"].p_subject) < 0.05).to_numpy()
    keep = ~excl

    # ---- individual theta peak (M8), reading (a): all kept analysed electrodes
    pk = res["enc_time_mean_z"][keep][:, PEAK_BANDS].mean(axis=0)
    res["peak_curve_all"] = pk
    res["peak_band_all"] = int(PEAK_BANDS[np.argmax(pk)])
    pk = res["enc_time_mean_z_alt"][~res["excluded_alt"]][:, PEAK_BANDS].mean(axis=0)
    res["peak_band_all_alt"] = int(PEAK_BANDS[np.argmax(pk)])
    res["edge"] = edge_check(sub, correct, bmean, bsd, keep)
    res["timing"]["edge"] = time.time() - T0

    # ---- phase measures on ERP-subtracted delay data (subtracterp.m, ncond = 1), in the main
    # windows (with the main exclusions) and in the code's windows (with that placement's own)
    xe = {k: v - v.mean(axis=0, keepdims=True) for k, v in (("enc", xs["enc"]), ("proc", xs["proc"]))}
    nab = n_amp_bands(fs)
    amp_bands = BANDS[AMP_BANDS[:nab]]
    for tag, win, kp in (("", WIN, keep), ("_alt", WIN_ALT, ~res["excluded_alt"])):
        _, pre_sel = segment(sub, "pre", win)
        _, post_sel = segment(sub, "post", win)
        wins = {"pre": (xe["enc"], pre_sel), "post": (xe["proc"], post_sel)}
        pairs = _make_pairs(regions, hemis, kp)
        res["pairs" + tag] = pairs
        res["plv" + tag] = _plv(wins, pairs, fs)
        res["timing"]["plv" + tag] = time.time() - T0
        psi, cs, keep_th, cs_shuf, keep_shuf = _psi_block(wins, pairs, fs, amp_bands, sid, tag, calibrate=not tag)
        res["psi" + tag], res["cspsi" + tag] = psi, cs
        res["units" + tag] = _make_units(regions, hemis, labels, kp, pairs, cs, keep_th, cs_shuf, keep_shuf, sid, tag)
        res["timing"]["psi" + tag] = time.time() - T0
    pairs, units = res["pairs"], res["units"]

    # theta peak reading (b): phase-directing electrodes only (any electrode in a directing unit)
    pdir = sorted({i for u in units if u["z_post_mtmfft"] > 1.96 for i in (u["ph"], u["amp"])})
    if pdir:
        pkb = res["enc_time_mean_z"][pdir][:, PEAK_BANDS].mean(axis=0)
        res["peak_curve_dir"], res["peak_band_dir"] = pkb, int(PEAK_BANDS[np.argmax(pkb)])
    else:
        res["peak_curve_dir"], res["peak_band_dir"] = None, None
    for key in ("code", "sliding"):
        pdir = sorted({i for u in units if u[f"z_post_{key}"] > 1.96 for i in (u["ph"], u["amp"])})
        if pdir:
            pkb = res["enc_time_mean_z"][pdir][:, PEAK_BANDS].mean(axis=0)
            res[f"peak_curve_dir_{key}"], res[f"peak_band_dir_{key}"] = pkb, int(PEAK_BANDS[np.argmax(pkb)])
        else:
            res[f"peak_curve_dir_{key}"], res[f"peak_band_dir_{key}"] = None, None

    # ---- PAC (M9) on the phase-directing units, postcue, per condition
    res["pac"] = []
    if pac:
        pb = res["peak_band_all"]
        if pb == 1:      # 1.5-4 Hz maximum: the nearest 3 Hz wide band, 2-5 Hz
            pb = 2
        if pb == 6:      # 6-10 Hz maximum: the nearest 3 Hz wide band, 5-8 Hz
            pb = 5
        res["theta_band_used"] = BANDS[pb].tolist()
        for u in units:
            u["dir_main"] = u["z_post_mtmfft"] > 1.96
            u["dir_code"] = u["z_post_code"] > 1.96
        dir_units = [i for i, u in enumerate(units) if u["dir_main"] or u["dir_code"]]
        need = sorted({units[i][k] for i in dir_units for k in ("ph", "amp")})
        xp = xs["proc"]
        for cond in (1, 2, 3):
            m = tic[:, 3] == cond
            xc = xp[m] - xp[m].mean(axis=0, keepdims=True)
            sub_idx = np.array(need, dtype=int)
            if len(sub_idx) == 0:
                continue
            ph = _filter_chunks(xc[:, sub_idx], fs, psel, BANDS[[pb]], "angle")[:, :, 0]   # (n, k, T)
            am = _filter_chunks(xc[:, sub_idx], fs, psel, amp_bands, "abs")                # (n, k, F, T)
            pos = {c: i for i, c in enumerate(need)}
            for i in dir_units:
                u = units[i]
                for rd in pac_readings:
                    rng = np.random.default_rng(seed_for(f"pac|{rd}|{cond}|{u['ph']}|{u['amp']}", sid))
                    z = pac_z(ph[:, pos[u["ph"]]].astype(np.float64), am[:, pos[u["amp"]]], rng, rd)
                    z20 = resample_20hz(z, fs)[:, :19]
                    res["pac"].append({"unit": i, "system": u["system"], "cond": cond, "reading": rd,
                                       "z": z20.astype(np.float32), "n_trials": int(m.sum())})
            del ph, am
    res["timing"]["pac"] = time.time() - T0
    log(f"{sid}: analysed in {time.time() - T0:.0f} s; " + ", ".join(f"{k} {v:.0f}" for k, v in res["timing"].items()))
    return res


def sanity_subject(sub):
    """Checks of the derived data against the trial table and against each other.

    - offsets of each segment's sampleinfo from the trial table's epoch columns;
    - whether overlapping samples of the pre, encmain and proc segments of a trial are equal
      when placed by sampleinfo (one shared clock);
    - whether trialinfo is the same in the three segments and equals the trial table's columns;
    - the trial-averaged evoked signal (RMS over the analysed channels) in 50 ms bins, to show
      where the responses to the start screen, the stimuli and the test cue fall.
    """
    out = {}
    tr = sub["trials"].set_index("trial")
    seg = sub["seg"]
    ti = seg["encmain"]["trialinfo"]
    T = tr.loc[ti[:, 0].astype(int)]
    out["offsets"] = {
        "pre - pre_start": np.unique(seg["pre"]["sampleinfo"][:, 0] - T.pre_start.to_numpy()),
        "encmain - enc_start": np.unique(seg["encmain"]["sampleinfo"][:, 0] - T.enc_start.to_numpy()),
        "proc - post_start": np.unique(seg["proc"]["sampleinfo"][:, 0] - T.post_start.to_numpy()),
    }
    out["trialinfo_same_segments"] = all(np.array_equal(seg[k]["trialinfo"], ti) for k in ("pre", "proc"))
    out["trialinfo_matches_table"] = bool(np.array_equal(
        ti[:, 1:6], T[["accuracy", "trial_type", "condition", "jitter", "rt"]].to_numpy()))
    diffs, overl = [], []
    for a, b in (("pre", "encmain"), ("encmain", "proc")):
        xa, xb = seg[a]["x"], seg[b]["x"]
        md, nov = 0.0, []
        for i in range(xa.shape[0]):
            sa = seg[a]["sampleinfo"][i, 0] + np.arange(xa.shape[-1])
            sb = seg[b]["sampleinfo"][i, 0] + np.arange(xb.shape[-1])
            _, ia, ib = np.intersect1d(sa, sb, return_indices=True)
            nov.append(len(ia))
            if len(ia):
                md = max(md, float(np.abs(xa[i][:, ia] - xb[i][:, ib]).max()))
        diffs.append(md)
        overl.append((min(nov), max(nov)))
    out["overlap_maxdiff"] = dict(zip(["pre/encmain", "encmain/proc"], diffs))
    out["overlap_samples"] = dict(zip(["pre/encmain", "encmain/proc"], overl))
    ev = {}
    for k in ("pre", "encmain", "proc"):
        d = seg[k]
        m = d["x"].mean(axis=0)                              # (ch, T)
        m = m - m[:, d["time"] < -1.0].mean(axis=1, keepdims=True)
        rms = np.sqrt((m ** 2).mean(axis=0))
        edges = np.arange(-1.5, 3.0001, 0.05)
        idx = np.digitize(d["time"], edges) - 1
        ev[k] = np.array([rms[idx == j].mean() if np.any(idx == j) else np.nan for j in range(len(edges) - 1)])
    out["evoked_rms"] = ev
    # high-gamma (70-150 Hz) amplitude, all trials, per delay length (jitter), 50 ms bins,
    # relative to the mean over the segment: the test cue comes 250 ms later after the long
    # delay, so the two time courses must part where the test cue appears
    hg = {}
    for k in ("pre", "encmain", "proc"):
        d = seg[k]
        a = _filter_chunks(d["x"], d["fs"], np.arange(d["x"].shape[-1]), np.array([[70.0, 150.0]]), "abs")[:, :, 0]
        a = a / a.mean(axis=(0, 2), keepdims=True)
        edges = np.arange(-1.5, 3.0001, 0.05)
        idx = np.digitize(d["time"], edges) - 1
        for jit in (900, 1150):
            m = a[d["trialinfo"][:, 4] == jit].mean(axis=(0, 1))
            hg[(k, jit)] = np.array([m[idx == j].mean() if np.any(idx == j) else np.nan for j in range(len(edges) - 1)])
    out["hg"] = hg
    # per electrode: t of the 900 against the 1150 ms trials in each 50 ms bin, for log high-gamma
    # amplitude and the 30 Hz low-passed signal. The test cue comes 250 ms later after the long
    # delay, so an electrode that responds to it parts the two groups from the cue's onset on:
    # at 0 s of encmain under the trial table's placement, at 1.5 s under the code's.
    jt = {}
    for k in ("pre", "encmain", "proc"):
        d = seg[k]
        x = d["x"]
        ln = np.log(_filter_chunks(x, d["fs"], np.arange(x.shape[-1]), np.array([[70.0, 150.0]]), "abs")[:, :, 0])
        lp = lowpass_erp(x, d["fs"], np.arange(x.shape[-1]))
        edges = np.arange(-1.5, 3.0001, 0.05)
        idx = np.digitize(d["time"], edges) - 1
        j9 = d["trialinfo"][:, 4] == 900
        rng = np.random.default_rng(seed_for(f"jitter|{k}", sub["subject"]))
        perms = [rng.permutation(j9) for _ in range(200)]
        for name, v in (("hg", ln), ("erp", lp)):
            b = np.stack([v[..., idx == j].mean(axis=-1) for j in range(len(edges) - 1)], axis=-1)
            jt[(k, name)] = stats.ttest_ind(b[j9], b[~j9], axis=0).statistic.astype(np.float32)
            # null: the same count of electrode bins with |t| > 1.96 per bin, jitter labels permuted
            jt[(k, name, "null")] = np.stack([(np.abs(stats.ttest_ind(b[p], b[~p], axis=0).statistic) > 1.96).sum(axis=0)
                                              for p in perms]).astype(np.int16)        # (200, bins)
            if name == "hg":
                # trial-mean log amplitude per electrode and bin, minus its segment mean
                m = b.mean(axis=0)
                jt[(k, "hg_mean")] = (m - m.mean(axis=-1, keepdims=True)).astype(np.float32)
        del ln, lp
    out["jitter_t"] = jt
    out["evoked_edges"] = np.arange(-1.5, 3.0001, 0.05)
    out["fs"] = seg["encmain"]["fs"]
    out["n_labels"] = len(seg["encmain"]["labels"])
    out["labels"] = seg["encmain"]["labels"]
    out["time_range"] = {k: (float(seg[k]["time"][0]), float(seg[k]["time"][-1]), len(seg[k]["time"])) for k in seg}
    out["n_samples"] = {k: (int(seg[k]["n_samples"].min()), int(seg[k]["n_samples"].max())) for k in seg}
    out["same_start"] = {k: seg[k]["same_start"] for k in seg}
    out["hdr_fs"] = {k: seg[k]["hdr_fs"] for k in seg}
    out["n_trials_derived"] = int(ti.shape[0])
    out["members"] = sub["members"]
    out["trials"] = sub["trials"]
    out["x_range"] = (float(min(seg[k]["x"].min() for k in seg)), float(max(seg[k]["x"].max() for k in seg)))
    out["load_s"] = sub["load_s"]
    return out


def process_subject(sid, chtab, log=print, **kw):
    """Load one subject, check it and run every per-subject measure; the raw data are dropped."""
    chans = chtab[chtab.subject == sid].reset_index(drop=True)
    sub = load_subject(sid, chans.label.tolist())
    san = sanity_subject(sub)
    res = analyse_subject(sub, chans, log=log, **kw)
    res["sanity"] = san
    res["chans"] = chans
    del sub
    return res
