"""Cochlear model and short-term correlations for Sadeghi et al. (2019), from the Methods
("Auditory model", "Nonstationary spectro-temporal correlation statistics", "Stationarity and
ensemble diversity indices") and the paper's MATLAB code in the data set
(Code/AuditoryModelCorr: cochleogram.m, cochleogramdyncorr.m, xcorrst.m, xcorrstsym.m,
fdesignkdt.m, finddtdfw.m, gammatonefilter.m, lowpass.m, fdesignh.m, h.m).

Where each parameter comes from:
- 58 gammatone filters of order 3, phase 0, centre frequencies from 100 Hz to 16 kHz in 1/8
  octave steps (Methods; centres placed as cochleogram.m does, Xc = (0.5 .. L-0.5)/L log2(fN/f1)).
- Bandwidths b = 25 + 75 (1 + 1.4 f^2)^0.69, f in kHz (Methods). The code's ModelExample.m uses
  criticalbandwidth.m, 94 + 71 f^1.5, which differs; the Methods are followed (protocol, reader
  step 2) and the difference is recorded as a finding.
- Passband gain 1 (Methods; gammatonefilter.m divides by the peak of |FFT|).
- Envelope: magnitude of the analytic signal, low-pass at 500 Hz with 125 Hz transition and 60 dB
  attenuation (Methods), designed as lowpass.m/fdesignh.m/h.m do, negative values set to 0
  (cochleogram.m), then resampled to 1 kHz (Methods; the code's ModelExample.m keeps 3675 Hz).
- The sound is normalised to unit SD first (cochleogramdyncorr.m).
- Short-term correlation: Kaiser window, beta from 40 dB attenuation (fdesignkdt.m gives 3.395,
  the Methods say 3.4), length chosen so that two SDs of the window (finddtdfw.m) equal tau_W;
  normalised as a correlation coefficient with time- and delay-dependent means and variances
  (xcorrst.m, RxyN), symmetrised over the two channel orders (xcorrstsym.m).
- Delays: up to half the window resolution tau_W (Methods); for SI and CDI, M = 99 lags (Methods),
  that is -49 to 49 ms at tau_W = 100 ms.
- Time step of the short-term correlation: tau_W / 4. The code steps at 8 x 4 x the window's 3 dB
  bandwidth (xcorrst.m with OFc = 8), finer than this; a time average of a slowly varying
  quantity does not depend on the step once it is below the window length, so this is a
  standard choice made for speed.
"""
import io

import numpy as np
from scipy import signal
from scipy.io import wavfile

FS_SOUND = 44100
FS_ENV = 1000


def read_wav(raw):
    fs, x = wavfile.read(io.BytesIO(raw))
    x = x.astype(np.float64)
    if x.ndim > 1:
        x = x[:, 0]
    return fs, x


def centre_frequencies(f1=100.0, fN=16000.0, dx=1 / 8):
    XN = np.log2(fN / f1)
    L = int(np.floor(XN / dx))
    return f1 * 2 ** ((np.arange(L) + 0.5) / L * XN)


def bandwidth_methods(fc):
    f = fc / 1000
    return 25 + 75 * (1 + 1.4 * f ** 2) ** 0.69


def gammatone(fc, b, fs=FS_SOUND, n=3):
    t = np.arange(0, int(0.05 * fs) + 1) / fs
    h = t ** (n - 1) * np.exp(-2 * np.pi * b * t) * np.cos(2 * np.pi * fc * t)
    return h / np.abs(np.fft.fft(h, 1024 * 64)).max()


def lowpass_fir(fc=500.0, tw=125.0, fs=FS_SOUND, att=60.0):
    """lowpass.m / fdesignh.m / h.m."""
    wc = 2 * np.pi * fc / fs
    TW = 2 * np.pi * tw / fs
    P = 13 / (1 + (126 / att) ** 1.6) - .7
    N = int(round(max((24.3 / (1 + (149 / att) ** 1.6) - 0.085) / TW * np.pi - 1, P * np.pi / wc / 0.95)))
    alpha = P * np.pi / (N + 1) / wc
    n = np.arange(-N, N + 1)
    H = wc / np.pi * np.sinc(wc * n / np.pi)
    W = np.sinc(alpha * wc * n / P / np.pi) ** P
    return H * W


def cochleogram(x, fs=FS_SOUND):
    """(58 channels, samples at 1 kHz) envelopes."""
    x = x / x.std()
    fc = centre_frequencies()
    bw = bandwidth_methods(fc)
    he = lowpass_fir(fs=fs)
    ne = (len(he) - 1) // 2
    out = []
    for f, b in zip(fc, bw):
        y = signal.fftconvolve(x, gammatone(f, b, fs))[: len(x)]
        y = np.abs(signal.hilbert(y))
        y = np.maximum(0, signal.fftconvolve(y, he)[ne: ne + len(x)])
        out.append(y)
    S = np.array(out)
    S = signal.resample_poly(S, FS_ENV, fs, axis=1)
    return np.maximum(S, 0)


def kaiser_for(tau_w_s, fs=FS_ENV, att=40.0):
    """fdesignkdt.m: Kaiser window whose 2 SD width (finddtdfw.m) is closest to tau_w."""
    beta = .5842 * (att - 21) ** .4 + .07886 * (att - 21)
    TW = 2 / tau_w_s / fs
    N = int(np.ceil((att - 7.95) / 14.36 / TW * np.pi))
    best = None
    for n in range(N - int(np.ceil(0.25 * N)), N + 1):
        w = np.kaiser(n, beta)
        wn = w / np.sqrt((w ** 2).sum() / fs)
        t = np.arange(1, n + 1) / fs
        m = (t * wn ** 2).sum() / fs
        dT = 2 * np.sqrt(((t - m) ** 2 * wn ** 2).sum() / fs)
        if best is None or abs(dT - tau_w_s) < best[0]:
            best = (abs(dT - tau_w_s), n)
    n = best[1] // 2 * 2 + 1
    return np.kaiser(n, beta), beta


def short_term(S, tau_w_ms, maxlag, step=None, pairs="all"):
    """Short-term correlation c_kl(t, tau) of xcorrst.m (RxyN), symmetrised as xcorrstsym.m.
    pairs = "all" gives (T, C, C, 2 maxlag + 1); "auto" gives the autocorrelations (T, C, lags);
    "zero" gives the zero-lag matrices (T, C, C). Yields one time point at a time when
    iterate=True is used through short_term_iter."""
    return np.array(list(short_term_iter(S, tau_w_ms, maxlag, step, pairs)))


def short_term_iter(S, tau_w_ms, maxlag, step=None, pairs="all"):
    K, _ = kaiser_for(tau_w_ms / 1000)
    W = np.sqrt(K)
    N = (len(W) - 1) // 2
    maxlag = min(maxlag, N)
    nw = 2 * N + 1
    step = step or max(1, int(round(tau_w_ms / 4)))
    C, T = S.shape
    lags = np.arange(-maxlag, maxlag + 1)
    # sliding sums over every window start s: sum_j W[j] S[c, s + j] and sum_j K[j] S[c, s + j]^2
    SW = signal.fftconvolve(S, W[None, ::-1], mode="valid", axes=1) / nw
    SK2 = signal.fftconvolve(S ** 2, K[None, ::-1], mode="valid", axes=1) / nw
    L = nw + 2 * maxlag
    nfft = 1 << int(np.ceil(np.log2(L + nw)))
    for k in range(2 * N, T - 2 * N, step):
        X = S[:, k - N: k + N + 1]
        XW = X * W
        MX = XW.mean(1)
        VX = XW.var(1, ddof=1)
        st = k - N - lags  # window start of Y shifted by each lag
        MY = SW[:, st].T  # lags, C
        VY = SK2[:, st].T - MY ** 2
        XK = X * K
        if pairs == "all":
            idx = (k - N + np.arange(nw))[None, :] - lags[:, None]
            Ysh = S[:, idx].transpose(1, 0, 2)  # lags, C, nw
            R = (XK @ Ysh.reshape(-1, nw).T).reshape(C, len(lags), C) / nw  # k, lag, l
            c = (R - MX[:, None, None] * MY[None]) / np.sqrt(VX[:, None, None] * VY[None])
            c = c.transpose(0, 2, 1)  # k, l, lag
            yield (c + c.transpose(1, 0, 2)[:, :, ::-1]) / 2
        elif pairs == "zero":
            i0 = maxlag
            R = XK @ S[:, k - N: k + N + 1].T / nw
            c = (R - np.outer(MX, MY[i0])) / np.sqrt(np.outer(VX, VY[i0]))
            yield (c + c.T) / 2
        else:
            seg = S[:, k - N - maxlag: k + N + maxlag + 1]
            r = np.fft.irfft(np.fft.rfft(seg, nfft) * np.conj(np.fft.rfft(XK, nfft)), nfft)
            # r[c, d] = sum_j XK[c, j] seg[c, j + d]; lag tau = maxlag - d
            R = r[:, :2 * maxlag + 1][:, ::-1] / nw  # C, lags (-maxlag..maxlag)
            c = (R - MX[:, None] * MY.T) / np.sqrt(VX[:, None] * VY.T)
            yield (c + c[:, ::-1]) / 2


def long_term_auto(S, maxlag):
    """Long-term normalised autocorrelation of each whole envelope (mean removed), lags
    -maxlag..maxlag."""
    X = S - S.mean(1, keepdims=True)
    n = X.shape[1]
    nfft = 1 << int(np.ceil(np.log2(2 * n)))
    F = np.fft.rfft(X, nfft)
    r = np.fft.irfft(F * np.conj(F), nfft)
    r = np.concatenate([r[:, nfft - maxlag:], r[:, : maxlag + 1]], 1)
    return r / r[:, maxlag: maxlag + 1]


def width_at(curve, lags_ms, frac=0.5):
    i0 = int(np.argmax(curve))
    thr = frac * curve[i0]
    def cross(step):
        i = i0
        while 0 <= i + step < len(curve) and curve[i + step] >= thr:
            i += step
        if not (0 <= i + step < len(curve)):
            return lags_ms[i]
        a, b = curve[i], curve[i + step]
        return lags_ms[i] + (lags_ms[i + step] - lags_ms[i]) * (a - thr) / (a - b)
    return cross(1) - cross(-1)
