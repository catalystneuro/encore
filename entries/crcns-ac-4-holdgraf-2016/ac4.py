"""Loading and measures for CRCNS ac-4 (Holdgraf et al. 2016, Nat Commun 7:13654).

The data set is a single zip, ``ac-4/live/data.zip`` in the public S3 bucket ``crcnsarchive``.
It is read in place over HTTP range requests (fsspec + zipfile); nothing is written to disk.
CRCNS data sets are unversioned; the MD5 of data.zip from the data set's checksums.md5 is
``DATA_ZIP_MD5`` and is checked against the archive's listing in the notebook.

Where each parameter comes from is said where it is defined:
- "claims" : the claim's criterion in claims/crcns-ac-4/10.1038-ncomms13654.yaml
- "Methods, <section>" : the paper's passage (author, step 1.6)
- "assumption" : a choice the paper leaves open that could change a result (stated in the record)
- "standard" : a choice that cannot change a result, or the claims file's named standard choice
"""

from __future__ import annotations

import io
import json

import fsspec
import numpy as np
import pandas as pd
import scipy.signal as ss
from scipy.fft import next_fast_len

DATASET = "crcns:ac-4/unversioned"
DOI = "10.6080/K08S4N4J"
BASE = "https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-4/live"
ZIP_URL = f"{BASE}/data.zip"
DATA_ZIP_MD5 = "a3f4fc4396018c4336289aeae07f3a24"
SUBJECTS = ["S01", "S02", "S03", "S04", "S07", "S08", "S13"]

FS = 1000.0          # ECoG sampling rate (ieeg.json; checked in the notebook)
FS_OUT = 50.0        # Methods, Neural and auditory feature extraction: "down-sampled to 50 Hz"
BASELINE = (-0.8, -0.1)   # Methods, Evoked HFB: "times -800 to -100 ms relative to sound onset"
EPOCH = (-1.0, 3.5)       # window kept around each sound, s (standard: covers every window used)

# HFB: Methods, Neural and auditory feature extraction: 21 centre frequencies 70 to 140 Hz,
# zero-phase IIR band-pass, Hilbert modulus, averaged. Band edges are open (claims, open detail
# 4); standard choice: log-spaced centres, band width 10% of the centre, 2nd-order Butterworth
# applied forwards and backwards (its squared magnitude, applied in the frequency domain).
HFB_CENTRES = np.geomspace(70, 140, 21)
HFB_REL_WIDTH = 0.10
# Methods, Participants: band-pass 0.5 to 200 Hz, notch 60, 120, 180 Hz, zero-phase IIR,
# common average reference. Filter orders are a standard choice (4th-order Butterworth,
# notch stop band +/- 1 Hz).
PRE_BAND = (0.5, 200.0)
NOTCHES = (60.0, 120.0, 180.0)

# Auditory spectrogram: Methods, Neural and auditory feature extraction: 128 ERB-spaced
# gammatone bands 180 to 7000 Hz, half-wave rectification, compression, spectral sharpening,
# 8 ms leaky integrator, reduced to 32 bands, 50 Hz. Compression exponent (cube root) and the
# sharpening (rectified difference with the next lower band, as in the NSL model the Methods
# cite, ref. 3) are standard choices.
N_BANDS_FULL = 128
N_BANDS = 32
F_LO, F_HI = 180.0, 7000.0
TAU_LEAK = 0.008
MAX_LAG = 20         # Methods, eSTRF model formulation: lags 0 to 400 ms at 50 Hz -> 0..20


def open_zip():
    import zipfile
    f = fsspec.open(ZIP_URL, block_size=2**24).open()
    return zipfile.ZipFile(f)


def _p(subject, suffix):
    return f"data/sub-{subject}/ieeg/sub-{subject}_{suffix}"


def read_tables(z, subject):
    """Events, channels and electrodes tables and the sidecar json of one subject."""
    ev = pd.read_csv(io.BytesIO(z.read(_p(subject, "task-FilteredSpeech_events.tsv"))), sep="\t")
    ch = pd.read_csv(io.BytesIO(z.read(_p(subject, "task-FilteredSpeech_channels.tsv"))), sep="\t")
    el = pd.read_csv(io.BytesIO(z.read(_p(subject, "task-FilteredSpeech_electrodes.tsv"))), sep="\t")
    js = json.loads(z.read(_p(subject, "ieeg.json")))
    hdr = z.read(_p(subject, "task-FilteredSpeech_ieeg.vhdr")).decode()
    return ev, ch, el, js, hdr


def header_channels(hdr):
    names = []
    for line in hdr.splitlines():
        if line.startswith("Ch") and "=" in line and line.split("=")[0][2:].isdigit():
            names.append(line.split("=")[1].split(",")[0])
    return names


def read_eeg(z, subject, n_channels):
    """The raw float32 multiplexed BrainVision data, as (channels, samples)."""
    b = z.read(_p(subject, "task-FilteredSpeech_ieeg.eeg"))
    x = np.frombuffer(b, dtype="<f4").reshape(-1, n_channels).T
    return x


def trials(ev):
    """The sound events of the task, with their phase, triplet number, filter and pink noise flag.

    noise_stim == 'mid' marks triplets whose MIDDLE sound was pink noise (events.json:
    "Whether the middle sound was noise ... or unfiltered speech"). Sounds with trial_num -1
    are unfiltered sentences outside any triplet; they are kept apart.
    """
    t = ev[ev.trial_type == "trial"].copy()
    t["trial_num"] = t.trial_num.astype(float).astype(int)
    t["noise"] = t.noise_stim == "mid"
    t = t.sort_values("onset").reset_index(drop=True)
    bad = ev[ev.trial_type == "bad"][["onset", "duration"]].to_numpy(float)
    ov = np.zeros(len(t), bool)
    for o, d in bad:
        ov |= (t.onset + EPOCH[0] < o + d) & (t.onset + t.duration + 0.5 > o)
    t["overlaps_bad"] = ov
    return t


# ---------------------------------------------------------------- filters in the frequency domain

def _butter_gain(freqs, order, band, btype):
    sos = ss.butter(order, band, btype=btype, fs=FS, output="sos")
    _, h = ss.sosfreqz(sos, worN=freqs, fs=FS)
    return np.abs(h) ** 2          # forward-backward (zero-phase) application


def preprocess_hfb(x, chunk=8):
    """CAR, pre-filter, then HFB amplitude at 1 kHz averaged over the 21 bands, down to 50 Hz.

    Returns (hfb50, raw) with raw the pre-filtered, re-referenced signal at 1 kHz (float32).
    """
    x = np.asarray(x, dtype=np.float64)
    x = x - x.mean(0, keepdims=True)                        # common average reference
    n = x.shape[1]
    nf = next_fast_len(n)
    freqs = np.fft.rfftfreq(nf, 1 / FS)
    g = _butter_gain(freqs, 4, PRE_BAND, "bandpass")
    for f0 in NOTCHES:
        g = g * _butter_gain(freqs, 2, (f0 - 1, f0 + 1), "bandstop")
    gains = [_butter_gain(freqs, 2, (c * (1 - HFB_REL_WIDTH / 2), c * (1 + HFB_REL_WIDTH / 2)),
                          "bandpass") for c in HFB_CENTRES]
    raw = np.empty(x.shape, np.float32)
    hfb = []
    for i in range(0, x.shape[0], chunk):
        X = np.fft.rfft(x[i:i + chunk], n=nf) * g
        raw[i:i + chunk] = np.fft.irfft(X, n=nf)[:, :n]
        env = np.zeros((X.shape[0], n))
        for gb in gains:
            Z = np.zeros((X.shape[0], nf), complex)
            Z[:, :len(freqs)] = X * gb
            Z[:, 1:(nf + 1) // 2] *= 2                    # analytic signal
            env += np.abs(np.fft.ifft(Z, axis=1)[:, :n])
        env /= len(gains)
        hfb.append(ss.resample_poly(env, 1, int(FS / FS_OUT), axis=1))
    return np.concatenate(hfb).astype(np.float32), raw


def hfb_amplitude(x, centres, fs=FS):
    """Mean Hilbert amplitude over bands (for PAC: 10 log-spaced bands, Supplementary Methods)."""
    n = x.shape[-1]
    nf = next_fast_len(n)
    freqs = np.fft.rfftfreq(nf, 1 / fs)
    X = np.fft.rfft(x, n=nf, axis=-1)
    env = 0
    for c in centres:
        gb = _butter_gain(freqs, 2, (c * (1 - HFB_REL_WIDTH / 2), c * (1 + HFB_REL_WIDTH / 2)), "bandpass")
        Z = np.zeros(X.shape[:-1] + (nf,), complex)
        Z[..., :len(freqs)] = X * gb
        Z[..., 1:(nf + 1) // 2] *= 2
        env = env + np.abs(np.fft.ifft(Z, axis=-1)[..., :n])
    return env / len(centres)


def band_phase(x, lo, hi, fs=FS):
    """Hilbert phase of a zero-phase band-passed signal (2nd-order Butterworth, standard)."""
    sos = ss.butter(2, (lo, hi), btype="bandpass", fs=fs, output="sos")
    return np.angle(ss.hilbert(ss.sosfiltfilt(sos, x, axis=-1), axis=-1))


# ---------------------------------------------------------------- audio

def read_audio(z, subject):
    """The subject's stimulus track (float64 WAV, mono), on the recording's clock."""
    from scipy.io import wavfile
    b = z.read(f"data/stimuli/{subject}_audio.wav")
    sr, a = wavfile.read(io.BytesIO(b))
    return sr, np.asarray(a, dtype=np.float64)


def erb_space(lo, hi, n):
    e = lambda f: 21.4 * np.log10(1 + 0.00437 * f)
    ie = lambda v: (10 ** (v / 21.4) - 1) / 0.00437
    return ie(np.linspace(e(lo), e(hi), n))


def auditory_spectrogram(seg, sr):
    """Auditory spectrogram of one audio segment, (32 bands, samples at 50 Hz)."""
    cfs = erb_space(F_LO, F_HI, N_BANDS_FULL)
    n = len(seg)
    nf = next_fast_len(n + int(0.05 * sr))
    S = np.fft.rfft(seg, n=nf)
    freqs = np.fft.rfftfreq(nf, 1 / sr)
    out = np.empty((N_BANDS_FULL, n))
    for k, cf in enumerate(cfs):
        b, a = ss.gammatone(cf, "iir", fs=sr)
        _, h = ss.freqz(b, a, worN=freqs, fs=sr)
        out[k] = np.fft.irfft(S * h, n=nf)[:n]
    out = np.maximum(out, 0) ** (1 / 3)                    # half-wave rectify, compress
    out = np.vstack([out[:1], np.maximum(np.diff(out, axis=0), 0)])   # spectral sharpening
    alpha = np.exp(-1 / (TAU_LEAK * sr))
    out = ss.lfilter([1 - alpha], [1, -alpha], out, axis=1)          # leaky integrator
    out = out.reshape(N_BANDS, N_BANDS_FULL // N_BANDS, n).mean(1)
    step = sr / FS_OUT
    m = int(n // step)
    idx = (np.arange(m)[:, None] * step + np.arange(int(step))[None]).astype(int)
    return out[:, idx].mean(-1)                           # boxcar average to 50 Hz


def speech_envelope(seg, sr, fs_out=FS):
    """Supplementary Methods, Electrode coherence with speech envelope: 64 log-spaced Gabor
    wavelets 500 to 2000 Hz, rectified, averaged. Wavelet width 7 cycles (standard)."""
    n = len(seg)
    nf = next_fast_len(n)
    S = np.fft.rfft(seg, n=nf)
    freqs = np.fft.rfftfreq(nf, 1 / sr)
    env = np.zeros(n)
    for f0 in np.geomspace(500, 2000, 64):
        sd = f0 / 7
        g = np.exp(-0.5 * ((freqs - f0) / sd) ** 2)
        Z = np.zeros(nf, complex)
        Z[:len(freqs)] = S * g * 2
        env += np.abs(np.fft.ifft(Z)[:n])
    env /= 64
    return ss.resample_poly(env, int(fs_out), int(sr))


# ---------------------------------------------------------------- per subject loading

def load_subject(z, subject, keep_raw=True):
    """Everything later analyses need from one subject, reduced as it loads."""
    ev, ch, el, js, hdr = read_tables(z, subject)
    names = header_channels(hdr)
    x = read_eeg(z, subject, len(names))
    good = ch.status.eq("good").to_numpy()
    assert list(ch.name) == names
    xg = x[good]
    stats = dict(n_samples=x.shape[1], raw_abs_median=float(np.median(np.abs(xg))),
                 car_residual=float(np.abs(xg.mean(0)).mean() / np.abs(xg).mean()))
    del x
    hfb, raw = preprocess_hfb(xg)
    del xg
    tr = trials(ev)
    sr, audio = read_audio(z, subject)
    # spectrogram and speech envelope per sound, from 0.5 s before onset to 0.5 s after offset
    spec, envs = [], []
    for _, r in tr.iterrows():
        a0 = int(round((r.onset - 0.5) * sr))
        a1 = int(round((r.onset + r.duration + 0.5) * sr))
        seg = audio[max(a0, 0):a1]
        spec.append(auditory_spectrogram(seg, sr))
        envs.append(speech_envelope(audio[int(round(r.onset * sr)):int(round((r.onset + 3) * sr))], sr))
    # audio clock check: rectified audio around onsets
    win = np.arange(int(-0.5 * sr), int(1.0 * sr))
    on = np.round(tr.onset.to_numpy() * sr).astype(int)
    aud = np.abs(audio[on[:, None] + win[None]]).mean(0)
    aud_t = win / sr
    # raw epochs at 1 kHz around each sound (for PAC, wavelet power, envelope coherence)
    e0, e1 = int(EPOCH[0] * FS), int(EPOCH[1] * FS)
    on1 = np.round(tr.onset.to_numpy() * FS).astype(int)
    raw_ep = None
    if keep_raw:
        raw_ep = np.stack([raw[:, o + e0:o + e1] for o in on1])
    del raw
    chg = ch[good].reset_index(drop=True)
    chg["subject"] = subject
    chg = chg.merge(el[["name", "x", "y"]], on="name", how="left")
    return dict(subject=subject, events=ev, trials=tr, channels=ch, good=chg, electrodes=el,
                json=js, hfb=hfb, spec=spec, env=envs, audio_sr=sr, audio_len=len(audio),
                audio_onset_profile=(aud_t, aud), raw_ep=raw_ep, stats=stats)


# ---------------------------------------------------------------- HFB epochs and z-scores

def hfb_epochs(d, t0=EPOCH[0], t1=EPOCH[1]):
    """(trials, channels, time) HFB at 50 Hz around each sound onset, and its times."""
    i0, i1 = int(round(t0 * FS_OUT)), int(round(t1 * FS_OUT))
    on = np.round(d["trials"].onset.to_numpy() * FS_OUT).astype(int)
    ep = np.stack([d["hfb"][:, o + i0:o + i1] for o in on])
    return ep, np.arange(i0, i1) / FS_OUT


def zscore_epochs(d, ep, times, mode):
    """z-score HFB over baseline (claims, open detail 3):
    'trial'  each trial by the mean and s.d. of its own -800 to -100 ms baseline;
    'pooled' by the mean and s.d. of all baseline samples of the electrode;
    'nonevent' the whole series z-scored by its samples outside any sound (ecogtools
               zscore_by_non_events), then epoched.
    """
    b = (times >= BASELINE[0]) & (times <= BASELINE[1])
    if mode == "trial":
        m = ep[..., b].mean(-1, keepdims=True)
        s = ep[..., b].std(-1, keepdims=True)
        return (ep - m) / s
    if mode == "pooled":
        m = ep[..., b].mean((0, 2), keepdims=True)
        s = ep[..., b].std((0, 2), keepdims=True)
        return (ep - m) / s
    if mode == "nonevent":
        h = d["hfb"]
        mask = np.ones(h.shape[1], bool)
        for _, r in d["trials"].iterrows():
            mask[int(r.onset * FS_OUT):int((r.onset + r.duration) * FS_OUT) + 1] = False
        m = h[:, mask].mean(1)[None, :, None]
        s = h[:, mask].std(1)[None, :, None]
        return (ep - m) / s
    raise ValueError(mode)


def post_mean(zep, times, durations, window):
    """Mean post-stimulus HFB per trial and channel (claims, open detail 2):
    'sound' onset to the end of each sound; '2.5' 0 to 2.5 s."""
    out = np.empty(zep.shape[:2])
    for i, dur in enumerate(durations):
        end = dur if window == "sound" else 2.5
        sel = (times >= 0) & (times < end)
        out[i] = zep[i][:, sel].mean(-1)
    return out


def bootstrap_lower(vals, rng, n_boot=10000, q=0.5):
    """0.5th percentile of the bootstrap distribution of the mean over trials, per channel.
    Methods, Evoked HFB: 99% interval, lower bound the 0.5th percentile. 10,000 resamples:
    claims, open detail 5 (standard)."""
    n = vals.shape[0]
    counts = rng.multinomial(n, np.full(n, 1 / n), size=n_boot)   # resampling with replacement
    means = counts @ vals / n                                     # (n_boot, channels)
    return np.percentile(means, q, axis=0)


def signflip_test(diff, rng, n_perm=10000):
    """Methods, Between-condition permutation test statistics: signs flipped at random 10,000
    times, the mean as statistic, two-sided P from the null quantile of the true mean."""
    diff = np.asarray(diff, float)
    diff = diff[np.isfinite(diff)]
    signs = rng.choice([-1.0, 1.0], size=(n_perm, len(diff)))
    null = (signs * diff).mean(1)
    obs = diff.mean()
    p = (np.sum(np.abs(null) >= abs(obs)) + 1) / (n_perm + 1)
    return obs, p


# ---------------------------------------------------------------- eSTRF (ridge, leave-one-trial-out)

def lagged(spec_seg, start, stop, max_lag=MAX_LAG):
    """Design rows for samples start..stop-1 of a spectrogram segment, lags 0..max_lag."""
    rows = [spec_seg[:, start - l:stop - l] for l in range(max_lag + 1)]
    return np.concatenate(rows, axis=0).T          # (samples, bands*lags), lag-major


def trial_design(d, idx, window="sound", tmax_extra=0.4, xshift=0):
    """X, y blocks per trial for the trials idx (claims, open detail 7):
    'sound' samples from onset to offset; 'plus' onset to offset + 400 ms.
    xshift (a check of alignment only; 0 in every fit) reads the spectrogram xshift samples
    later against the same HFB samples, the segment padded with its edge values."""
    Xs, ys = [], []
    on = np.round(d["trials"].onset.to_numpy() * FS_OUT).astype(int)
    for i in idx:
        r = d["trials"].iloc[i]
        n = int(np.floor(r.duration * FS_OUT)) + (int(tmax_extra * FS_OUT) if window == "plus" else 0)
        s0 = int(0.5 * FS_OUT)                       # segment starts 0.5 s before onset
        seg = d["spec"][i]
        n = min(n, seg.shape[1] - s0)
        if xshift:
            pad = abs(xshift)
            seg = np.pad(seg, ((0, 0), (pad, pad)), mode="edge")
            s0 = s0 + pad + xshift
        Xs.append(lagged(seg, s0, s0 + n))
        ys.append(d["hfb"][:, on[i]:on[i] + n].T)
    return Xs, ys


def ridge_loto(Xs, ys, alphas):
    """Leave-one-trial-out ridge for all channels at once, inputs and outputs z-scored with
    the training trials' statistics (Methods, eSTRF model formulation).

    Returns coefs (folds, alphas, features, channels; only when one alpha is given) and r2 (folds, alphas, channels), R2
    on the held-out trial (coefficient of determination, as sklearn's r2_score).
    """
    n_tr = len(Xs)
    XtX = [X.T @ X for X in Xs]
    Xty = [X.T @ y for X, y in zip(Xs, ys)]
    sx = [X.sum(0) for X in Xs]
    sy = [y.sum(0) for y in ys]
    sxx = [(X ** 2).sum(0) for X in Xs]
    syy = [(y ** 2).sum(0) for y in ys]
    nn = np.array([len(X) for X in Xs])
    T = dict(XtX=sum(XtX), Xty=sum(Xty), sx=sum(sx), sy=sum(sy), sxx=sum(sxx), syy=sum(syy), n=nn.sum())
    p, c = Xs[0].shape[1], ys[0].shape[1]
    keep = len(alphas) == 1
    coefs = np.empty((n_tr, len(alphas), p, c), np.float32) if keep else None
    r2 = np.empty((n_tr, len(alphas), c))
    for k in range(n_tr):
        n = T["n"] - nn[k]
        mx = (T["sx"] - sx[k]) / n
        my = (T["sy"] - sy[k]) / n
        vx = (T["sxx"] - sxx[k]) / n - mx ** 2
        vy = (T["syy"] - syy[k]) / n - my ** 2
        dx = np.sqrt(np.maximum(vx, 1e-20))
        dy = np.sqrt(np.maximum(vy, 1e-20))
        C = (T["XtX"] - XtX[k]) - n * np.outer(mx, mx)
        C = C / np.outer(dx, dx)
        B = (T["Xty"] - Xty[k]) - n * np.outer(mx, my)
        B = B / np.outer(dx, dy)
        w, V = np.linalg.eigh(C)
        VB = V.T @ B
        Xt = (Xs[k] - mx) / dx
        yt = (ys[k] - my) / dy
        XV = Xt @ V
        sst = ((yt - yt.mean(0)) ** 2).sum(0)
        for a, al in enumerate(alphas):
            Wt = VB / (w + al)[:, None]
            if keep:
                coefs[k, a] = V @ Wt
            pred = XV @ Wt
            r2[k, a] = 1 - ((yt - pred) ** 2).sum(0) / sst
    return coefs, r2


def predict(coef, X, y):
    """Prediction of z-scored y from z-scored X (each by its own statistics), and R2 per channel."""
    Xz = (X - X.mean(0)) / X.std(0)
    yz = (y - y.mean(0)) / y.std(0)
    pred = Xz @ coef
    r2 = 1 - ((yz - pred) ** 2).sum(0) / ((yz - yz.mean(0)) ** 2).sum(0)
    return pred, r2


def partial_corr(a, b, c, intercept=False):
    """pcorr(a, b | c) = corr(a - a_hat_c, b) as in the Methods (eSTRF linear overlap) and the
    code's partial_corr (least squares on c, no intercept by default)."""
    C = np.column_stack([c, np.ones_like(c)]) if intercept else c[:, None]
    beta = np.linalg.lstsq(C, a, rcond=None)[0]
    res = a - C @ beta
    return np.corrcoef(res, b)[0, 1]


def mtf(strf, n_bands=N_BANDS, n_lags=MAX_LAG + 1):
    """Modulation transfer function: amplitude of the 2-D FFT of the eSTRF (bands x lags),
    centred. Methods, MTF of eSTRFs."""
    s = strf.reshape(n_lags, n_bands).T
    return np.abs(np.fft.fftshift(np.fft.fft2(s)))


# ---------------------------------------------------------------- multitaper coherence

def mt_coherence(x, y, fs, nw=2.0, jackknife=True):
    """Multitaper coherence of two 1-D signals over the last axis, with tapers DPSS(nw, 2nw-1).
    With jackknife=True the jackknife bias-corrected estimate over tapers (Thomson & Chave)
    on the Fisher-transformed coherency magnitude. Returns freqs, coherence (..., freqs)."""
    n = x.shape[-1]
    k = int(2 * nw - 1)
    tap = ss.windows.dpss(n, nw, k)
    X = np.fft.rfft(tap * x[..., None, :], axis=-1)
    Y = np.fft.rfft(tap * y[..., None, :], axis=-1)
    freqs = np.fft.rfftfreq(n, 1 / fs)

    def coh(sel):
        sxy = (X[..., sel, :] * np.conj(Y[..., sel, :])).mean(-2)
        sxx = (np.abs(X[..., sel, :]) ** 2).mean(-2)
        syy = (np.abs(Y[..., sel, :]) ** 2).mean(-2)
        return np.abs(sxy) ** 2 / (sxx * syy)

    full = coh(np.arange(k))
    if not jackknife:
        return freqs, full
    ft = lambda c: np.arctanh(np.sqrt(np.clip(c, 0, 1 - 1e-12)))
    loo = np.stack([ft(coh(np.delete(np.arange(k), i))) for i in range(k)])
    z = k * ft(full) - (k - 1) * loo.mean(0)
    return freqs, np.tanh(np.maximum(z, 0)) ** 2


def coh_to_bits(coh, freqs, fmax=None, fmin=None):
    """Normal mutual information, the integral over frequency of -log2(1 - coh) (Methods,
    Between-condition coherence; coh_to_bits in ecogtools), in bits/s. fmin, when given,
    leaves out the frequencies below it (a variant; by default every frequency above 0)."""
    sel = freqs > 0 if fmax is None else (freqs > 0) & (freqs <= fmax)
    if fmin is not None:
        sel = sel & (freqs >= fmin - 1e-9)
    df = freqs[1] - freqs[0]
    return (-np.log2(1 - np.clip(coh[..., sel], 0, 1 - 1e-9))).sum(-1) * df
