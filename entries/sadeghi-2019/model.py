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


def bandwidth_code(fc):
    """criticalbandwidth.m of the deposit's code: 94 + 71 f^1.5, f in kHz (a variant)."""
    return 94 + 71 * (fc / 1000) ** 1.5


def cochleogram(x, fs=FS_SOUND, bandwidth=bandwidth_methods):
    """(58 channels, samples at 1 kHz) envelopes."""
    x = x / x.std()
    fc = centre_frequencies()
    bw = bandwidth(fc)
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


def short_term_iter(S, tau_w_ms, maxlag, step=None, pairs="all", centres=None):
    """centres: the window centres (samples) to use; by default every step from 2N to T - 2N."""
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
    for k in (range(2 * N, T - 2 * N, step) if centres is None else centres):
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


# ---------------------------------------------------------------- model classifier (Figs 9, 10)
#
# Methods, "Dimensionality reduction and distribution model", "Bayesian classifier", "Cross
# validation", "Optimal temporal resolution and integration time", "Spectrum-based classifier";
# claims file, opening comment (readings 6 and 7). Choices the paper does not make, each stated
# in the notebook as an assumption or a standard choice:
# - training observations are the short-term features at every tau_W / 4 (the step used above),
#   at most TRAIN_CAP per category by a seeded random subsample (standard choice, for speed);
# - the spectro-temporal feature vector is the spectral and temporal features of one time point
#   side by side (assumption: the Methods give it its own PCs and N_c, so it is one vector);
# - temporal observations are (time point, channel) pairs, and a window's temporal log-likelihood
#   is summed over its 58 channels (Methods: "both time points and different frequency channels
#   are treated as observations"; "features at each time sample are conditionally independent");
# - the spectrum feature is the Kaiser-weighted mean envelope of each channel in the window;
# - PCA is fitted once on the training observations of all 195 sounds (assumption; refitting it
#   in every fold is run as a variant).

TRAIN_CAP = 10000
RES_MS = 25 * 2 ** (np.arange(10) / 2)  # 25 to 566 ms in half octave steps (Methods)
REPORTED = {"spec": (26, 8), "temp": (8, 5), "st": (87, 13)}  # (PCs, N_c), Methods


def features(S, tau_w_ms):
    """Short-term features of one cochleogram at resolution tau_w_ms, on a grid of window
    centres every tau_W / 4 where the window and every lag fit in the sound.
    Returns dict spec (n, 1653), temp (n, 58, maxlag), spectrum (n, 58), centres (ms), K."""
    K, _ = kaiser_for(tau_w_ms / 1000)
    N = (len(K) - 1) // 2
    maxlag = min(int(tau_w_ms // 2), N)
    step = max(1, int(round(tau_w_ms / 4)))
    C, T = S.shape
    centres = np.arange(N + maxlag, T - N - maxlag - 1, step)
    iu = np.triu_indices(C, 1)
    spec = np.array([z[iu] for z in short_term_iter(S, tau_w_ms, 0, pairs="zero", centres=centres)], np.float32)
    temp = np.array([a[:, maxlag + 1:] for a in short_term_iter(S, tau_w_ms, maxlag, pairs="auto", centres=centres)],
                    np.float32)
    SK = signal.fftconvolve(S, K[None, ::-1], mode="valid", axes=1) / K.sum()
    spectrum = SK[:, centres - N].T.astype(np.float32)
    return {"spec": spec, "temp": temp, "spectrum": spectrum, "centres": centres, "klen": len(K), "step": step}


def test_index(F, spacing_ms):
    """Grid indices of consecutive non-overlapping test windows from the start of the sound, at
    least spacing_ms apart (reading 6a: tau_W; 6b: the full Kaiser window length)."""
    stride = int(np.ceil(spacing_ms / F["step"] - 1e-9))
    return np.arange(0, len(F["centres"]), stride)


def n_steps(nmax):
    """N = 1 to the largest number of windows in half octave steps (Cross validation)."""
    ns = sorted({int(round(2 ** (j / 2))) for j in range(40) if round(2 ** (j / 2)) <= nmax})
    return ns if ns[-1] == nmax else ns + [nmax]


def obs_of(F, kind, idx=None):
    """Observations of one sound for a classifier: (n, m, d), m = 58 channels for temporal, else 1.
    idx selects grid points (all by default)."""
    sl = slice(None) if idx is None else idx
    if kind == "spec":
        return F["spec"][sl][:, None]
    if kind == "spectrum":
        return F["spectrum"][sl][:, None]
    if kind == "temp":
        return F["temp"][sl]
    t = F["temp"][sl]
    return np.concatenate([F["spec"][sl], t.reshape(len(t), -1)], 1)[:, None]


def fit_pca(Fs, kind, rng, nfit=15000, kmax=150):
    """PCA of the pooled observations of the sounds Fs (list of feature dicts), fitted on at most
    nfit rows drawn at random (standard choice). Returns mean, components (k, d), and the
    cumulative fraction of the total variance (trace) the components explain."""
    from sklearn.decomposition import PCA
    rows = []
    per = max(1, nfit // len(Fs))
    for F in Fs:
        X = obs_of(F, kind)
        X = X.reshape(-1, X.shape[-1])
        rows.append(X[rng.choice(len(X), min(per, len(X)), replace=False)])
    X = np.concatenate(rows).astype(np.float64)
    k = min(kmax, X.shape[1], X.shape[0] - 1)
    p = PCA(k, svd_solver="randomized" if X.shape[1] > 500 else "full", random_state=0).fit(X)
    total = X.var(0, ddof=1).sum()
    return p.mean_, p.components_.astype(np.float32), np.cumsum(p.explained_variance_) / total


def project(F, kind, mean, comps):
    X = obs_of(F, kind)
    n, m, d = X.shape
    return ((X.reshape(-1, d) - mean.astype(np.float32)) @ comps.T).reshape(n, m, -1)


def fit_gmm(X, nc, seed=0):
    """Diagonal GMM (Methods). scikit-learn's default variance floor (reg_covar 1e-6); a fit that
    fails on a collapsed component is refitted with 1e-4 (standard choice) and flagged."""
    from sklearn.mixture import GaussianMixture
    X = np.asarray(X, np.float64)
    try:
        gm = GaussianMixture(nc, covariance_type="diag", max_iter=200, random_state=seed).fit(X)
        gm.refitted_ = False
    except ValueError:
        gm = GaussianMixture(nc, covariance_type="diag", max_iter=200, random_state=seed, reg_covar=1e-4).fit(X)
        gm.refitted_ = True
    return gm


def train_rows(Zs, npc, rng, cap=TRAIN_CAP):
    """Training observations of the sounds Zs, at most cap, drawn at random in equal numbers from
    each sound (standard choice, for speed)."""
    per = int(np.ceil(cap / len(Zs)))
    out = []
    for z in Zs:
        X = z[:, :, :npc].reshape(-1, npc)
        out.append(X if len(X) <= per else X[rng.choice(len(X), per, replace=False)])
    return np.concatenate(out)


def window_ll(gm, Zw, npc):
    """Log-likelihood of each test window (n, m, d): summed over its m observations."""
    n, m, _ = Zw.shape
    return gm.score_samples(Zw[:, :, :npc].reshape(-1, npc).astype(np.float64)).reshape(n, m).sum(1)


def loso(Z, labels, npc, nc, tests, seed, n_jobs=4):
    """Leave one sound out (Cross validation). Z: per-sound observations (n, m, d); labels: class
    of each sound; tests: per-sound dict {name: window arrays (n_w, m, d)} to score. A fold
    changes only the held-out sound's class model, so each class is fitted once on all its
    sounds and refitted once per held-out sound. Returns {name: per-sound (n_w, classes) LL}
    and the fitted models (full per class, refit per sound)."""
    from joblib import Parallel, delayed
    labels = np.asarray(labels)
    classes = np.unique(labels)
    seeds = np.random.SeedSequence(seed).generate_state(len(Z) + len(classes))

    def rows(c, leave, s):
        idx = [i for i in np.flatnonzero(labels == c) if i != leave]
        return train_rows([Z[i] for i in idx], npc, np.random.default_rng(s))

    jobs = [(c, -1, seeds[len(Z) + k]) for k, c in enumerate(classes)] + [(labels[j], j, seeds[j]) for j in range(len(Z))]
    fits = Parallel(n_jobs=n_jobs)(delayed(fit_gmm)(rows(c, j, s), nc) for c, j, s in jobs)
    full, refit = fits[:len(classes)], fits[len(classes):]
    out = {}
    for name in tests[0]:
        LL = []
        for j in range(len(Z)):
            Zw = tests[j][name]
            LL.append(np.array([window_ll(refit[j] if c == labels[j] else full[k], Zw, npc) for k, c in enumerate(classes)]).T)
        out[name] = LL
    return out, full, refit


def accuracy_curve(LL, labels, classes, ns):
    """Fraction correct (per sound 0/1) after summing the log-likelihoods of the first N windows."""
    labels = np.asarray(labels)
    res = np.zeros((len(LL), len(ns)))
    for j, L in enumerate(LL):
        cs = np.cumsum(L, 0)
        for i, n in enumerate(ns):
            res[j, i] = classes[int(np.argmax(cs[min(n, len(cs)) - 1]))] == labels[j]
    return res
