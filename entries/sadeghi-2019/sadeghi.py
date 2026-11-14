"""Loading and measures for Sadeghi, Zhai, Stevenson & Escabi (2019) on CRCNS bst-2.

The data set is one gzip-compressed tar file (bst-2/live/data.tar.gz, 5.3 GB) in the public
S3 bucket crcnsarchive. A gzip stream cannot be read at random, so `stream_members` reads it
once from the start over HTTP and hands each wanted member to the caller in memory; nothing
is written to disk. The neural files are MATLAB 7.3 (HDF5) files, read with h5py from memory.

Where each parameter comes from:

- Correlations (`window_corr`) port the paper's own MATLAB code in the data set,
  Code/MUACorrAnalysis/rastermuashuffledxcorrwinfast.m and rastermuashuffledxcovwinfast.m
  (Materials and methods, "Neural ensemble stimulus-driven correlation" and "Neural ensemble
  noise correlation", whose equations the text lost): square window of Nw samples centred at
  T0, PSTH-based shuffled correlogram with the within-trial terms removed, noise correlogram
  as unshuffled minus shuffled, all normalised by the unshuffled (signal plus noise) variances
  (R12_sh, R12_ush, R12_noise of the code). Maximum delay 100 ms (Noiseless neural classifier,
  paragraph 6, and NeuralExample.m).
- Single-trial correlations (`single_trial_features`) are the same code applied to one trial
  with the within-trial terms kept (the "unshuffled correlations for individual trials" of
  "Single-trial neural classifier").
- Classifier (`classify`): half split, 1000 ms model windows for the single-trial and 500 ms
  for the noiseless classifier, validation windows of 62.5 to 1000 ms in half octave steps,
  100 random time samples, PCA fitted on the model data, naive Bayes with axis-aligned
  Gaussians, equal priors, MAP (claims file, opening comment, citing "Noiseless neural
  classifier" and "Single-trial neural classifier"). The readings (1) to (5) of the claims file
  are options of `classify`. The PC grid (1 to 40) and the variance floor of the Gaussians
  (1e-9 of the largest feature variance, as scikit-learn's GaussianNB) are standard choices.
- Random seeds are standard choices; each caller passes its own generator.
"""
import io
import tarfile

import fsspec
import h5py
import numpy as np

DATASET = "crcns:bst-2/unversioned"  # CRCNS data sets are not versioned (docs/archives.md)
URL = "https://crcnsarchive.s3-us-west-2.amazonaws.com/bst-2/live/data.tar.gz"
P1_SOUNDS = ["fire", "bird", "crowd", "water", "snake"]  # data description, paradigm 1
P3_CATEGORIES = ["fire", "water", "speech"]  # data description, paradigm 3
DURATIONS_MS = 62.5 * 2 ** (np.arange(9) / 2)  # 62.5 to 1000 ms in half octave steps
FS = 12207.03125 / 6  # aMUA sampling rate of the files (2034.5 Hz); the paper says 2 kHz
# (Electrophysiology, paragraph 3). The notebook checks every file against this value.


def stream_members(want, url=URL, block_size=2**24):
    """Yield (name, bytes) for each tar member for which want(name) is true, streaming once."""
    f = fsspec.open(url, block_size=block_size).open()
    tf = tarfile.open(fileobj=f, mode="r|gz")
    for m in tf:
        if m.isfile() and want(m.name):
            yield m.name, tf.extractfile(m).read()
    f.close()


def _chars(ds):
    return "".join(chr(c) for c in np.asarray(ds[()]).ravel())


def _channels(h, group_ref):
    """Read a Channel struct array: returns (rasters list of (trials, samples) float32, fs list)."""
    g = h[group_ref]
    ras = [np.asarray(h[r][()], dtype=np.float32).T for r in g["RAS"][()].ravel()]
    fs = [float(np.asarray(h[r][()]).ravel()[0]) for r in g["Fs"][()].ravel()]
    return ras, fs


def read_site(name, raw):
    """Parse one P<x>_Site<zz>.mat file. Returns a dict with param, fs and
    ras[(a, b)] = array (16 channels, trials, samples), where (a, b) is (sound, 0) for
    paradigm 1, (sound, condition) for paradigm 2 (condition 0 = 1/f, 1 = original; data
    description) and (category, exemplar) for paradigm 3, all indices from 0."""
    h = h5py.File(io.BytesIO(raw), "r")
    D = h["Data"]
    P = D["Param"]
    out = {"name": name.split("/")[-1][:-4],
           "param": {k: _chars(P[k]) for k in P.keys()}, "ras": {}, "fs": set(), "ntrials_ch": {},
           "fields": {"Data": sorted(D.keys()), "Data.Param": sorted(P.keys()), "Data.Sound": sorted(D["Sound"].keys())}}
    snd = D["Sound"]
    sub = [k for k in snd.keys()][0]  # 'Channel', 'Condition' or 'Exemplar'
    for a, ref in enumerate(snd[sub][()].ravel()):
        if sub == "Channel":
            items = [(0, ref)]
        else:
            items = list(enumerate(h[ref]["Channel"][()].ravel()))
        for b, r in items:
            ras, fs = _channels(h, r)
            nt = [x.shape[0] for x in ras]
            ns = [x.shape[1] for x in ras]
            out["ntrials_ch"][(a, b)] = (nt, ns)
            n, s = min(nt), min(ns)
            out["ras"][(a, b)] = np.stack([x[:n, :s] for x in ras])
            out["fs"].update(fs)
    h.close()
    return out


# ---------------------------------------------------------------- correlations (paper's code)

def _xcorr(a, b, maxlag):
    """MATLAB xcorr(a, b, maxlag) along the last axis: R(m) = sum_n a(n+m) b(n), m = -maxlag..maxlag."""
    n = a.shape[-1]
    nfft = 1 << int(np.ceil(np.log2(2 * n)))
    A = np.fft.rfft(a, nfft)
    B = np.fft.rfft(b, nfft)
    r = np.fft.irfft(A * np.conj(B), nfft)
    return np.concatenate([r[..., nfft - maxlag:], r[..., :maxlag + 1]], axis=-1)


def window_geometry(T0_ms, Tw_ms, maxtau_ms=100.0, fs=FS):
    maxlag = int(np.ceil(maxtau_ms / 1000 * fs))
    N0 = int(round(T0_ms / 1000 * fs))
    Nw = int(np.floor(fs * Tw_ms / 1000 / 2) * 2 + 1)
    N1 = N0 - int(np.ceil(Nw / 2)) - maxlag
    N2 = N0 + int(np.ceil(Nw / 2)) + maxlag
    return maxlag, Nw, N1 - 1, N2  # python slice [N1-1:N2] equals MATLAB N1:N2


def window_corr(R1, R2, T0_ms, Tw_ms, maxtau_ms=100.0, fs=FS):
    """Port of rastermuashuffledxcorrwinfast + rastermuashuffledxcovwinfast with
    Mean='y', Diag='y', DiagVar='n'. R1, R2: (..., trials, samples); leading axes broadcast.
    Returns dict of R12_sh, R12_ush, R12_noise over lags -maxlag..maxlag (last axis)."""
    maxlag, Nw, s0, s1 = window_geometry(T0_ms, Tw_ms, maxtau_ms, fs)
    if s0 < 0 or s1 > R1.shape[-1]:
        raise ValueError("window plus lags outside the raster")
    X = R1[..., s0:s1].astype(np.float64)
    Y = R2[..., s0:s1].astype(np.float64)
    L = X.shape[-1]
    Nw2 = (Nw - 1) // 2
    c = (L - 1) // 2
    W = np.zeros(L)
    W[c - Nw2:c + Nw2 + 1] = 1.0
    X = X * W
    NT = X.shape[-2]
    P1 = X.sum(-2)
    P2 = Y.sum(-2)
    FX = np.fft.rfft(X, 1 << int(np.ceil(np.log2(2 * L))))
    FY = np.fft.rfft(Y, FX.shape[-1] * 2 - 2)
    nfft = FX.shape[-1] * 2 - 2

    def back(F):
        r = np.fft.irfft(F, nfft)
        return np.concatenate([r[..., nfft - maxlag:], r[..., :maxlag + 1]], axis=-1)

    R12 = back(FX.sum(-2) * np.conj(FY.sum(-2)))
    Rdiag = back((FX * np.conj(FY)).sum(-2))
    R12 = R12 - Rdiag
    R12noise = Rdiag / NT / Nw - R12 / NT / (NT - 1) / Nw
    R12 = R12 / NT / (NT - 1) / Nw
    R12diag = Rdiag / NT / Nw
    M1 = P1.sum(-1) / Nw
    E21diag = (X ** 2).sum((-1, -2)) / (Nw - 1)
    M2 = _xcorr(np.broadcast_to(W, P2.shape), P2, maxlag) / Nw
    E22diag = _xcorr(np.broadcast_to(W, Y.shape), Y ** 2, maxlag).sum(-2) / (Nw - 1)
    Var1diag = (E21diag * NT - M1 ** 2) / NT ** 2
    Var2diag = (E22diag * NT - M2 ** 2) / NT ** 2
    M1 = M1 / NT
    M2 = M2 / NT
    R12 = R12 - M1[..., None] * M2
    R12diag = R12diag - M1[..., None] * M2
    den = np.sqrt(Var1diag[..., None] * Var2diag)
    return {"sh": R12 / den, "ush": R12diag / den, "noise": R12noise / den,
            "tau_ms": np.arange(-maxlag, maxlag + 1) / fs * 1000}


def zero_lag_all(X):
    """Zero-lag R12_sh, R12_ush and R12_noise of the code for all channel pairs at once.
    X: (channels, trials, Nw + 2) segment (MaxLag = 0), the square window in the middle."""
    C, NT, L = X.shape
    Nw = L - 2
    X = X.astype(np.float64).copy()
    X[..., 0] = 0
    X[..., -1] = 0
    P = X.sum(1)
    Rdiag = np.einsum("ktn,ltn->kl", X, X)
    R12 = (P @ P.T - Rdiag) / NT / (NT - 1) / Nw
    Rd = Rdiag / NT / Nw
    noise = Rd - R12
    M1 = P.sum(-1) / Nw
    E2diag = (X ** 2).sum((1, 2)) / (Nw - 1)
    var = (E2diag * NT - M1 ** 2) / NT ** 2
    M1 = M1 / NT
    den = np.sqrt(np.outer(var, var))
    mm = np.outer(M1, M1)
    return {"sh": (R12 - mm) / den, "ush": (Rd - mm) / den, "noise": noise / den}


def site_correlations(ras, T0_ms, Tw_ms, maxtau_ms=100.0):
    """Spectral (zero-lag, channels x channels) and temporal (channels x lags) shuffled
    (stimulus-driven), unshuffled (total) and noise correlations for ras (channels, trials,
    samples), one square window of Tw_ms centred at T0_ms (paper's code)."""
    tem = window_corr(ras, ras, T0_ms, Tw_ms, maxtau_ms)
    _, _, s0, s1 = window_geometry(T0_ms, Tw_ms, 0.0)
    spec = zero_lag_all(ras[:, :, s0:s1])
    return {"spec": spec, "temp": {k: tem[k] for k in ("sh", "ush", "noise")}, "tau_ms": tem["tau_ms"]}


WINDOW_READINGS = ("whole", "w1000", "code_half")


def correlation_readings(ras):
    """Readings of the window T (claims file, fig1k-example-temporal-widths (ii)):
    whole = one window over the whole response (lags kept inside the raster);
    w1000 = 1000 ms windows centred at 0.61, 1.5 and 2.39 s, averaged (standard choice of
    centres); code_half = the first half of the raster, as NeuralExample.m computes Fig 1."""
    NS = ras.shape[-1]
    out = {}
    T0, Tw = whole_window(NS)
    out["whole"] = site_correlations(ras, T0, Tw)
    parts = [site_correlations(ras, c, 1000.0) for c in (610.0, 1500.0, 2390.0)]
    out["w1000"] = {"spec": {k: np.mean([p["spec"][k] for p in parts], 0) for k in parts[0]["spec"]},
                    "temp": {k: np.mean([p["temp"][k] for p in parts], 0) for k in parts[0]["temp"]},
                    "tau_ms": parts[0]["tau_ms"]}
    NS2 = NS // 2
    T0, Tw = whole_window(NS2)
    out["code_half"] = site_correlations(ras[:, :, :NS2], T0, Tw)
    return out


def split_half(ras):
    """Split-half reliability of the stimulus-driven (shuffled) correlations of one raster
    (channels, trials, samples), for the aMUA part of S10 Fig F ("comparing neural correlations
    across halves of the data"). Halves are read two ways: (time) the first and second 1.5 s, as
    NeuralExample.m splits the raster (sA, sB), each with its whole-window correlation; (trial)
    odd and even trials, each over the whole response. Returns {half: (r spectral with the
    diagonal, r spectral off the diagonal, r temporal)}, Pearson r between the two halves."""
    NS = ras.shape[-1]
    NS2 = NS // 2
    T0h, Twh = whole_window(NS2)
    T0, Tw = whole_window(NS)
    pairs = {"time": (site_correlations(ras[:, :, :NS2], T0h, Twh), site_correlations(ras[:, :, NS2:2 * NS2], T0h, Twh)),
             "trial": (site_correlations(ras[:, 0::2], T0, Tw), site_correlations(ras[:, 1::2], T0, Tw))}
    off = ~np.eye(ras.shape[0], dtype=bool)
    out = {}
    for k, (a, b) in pairs.items():
        out[k] = (float(np.corrcoef(a["spec"]["sh"].ravel(), b["spec"]["sh"].ravel())[0, 1]),
                  float(np.corrcoef(a["spec"]["sh"][off], b["spec"]["sh"][off])[0, 1]),
                  float(np.corrcoef(a["temp"]["sh"].ravel(), b["temp"]["sh"].ravel())[0, 1]))
    return out


def whole_window(nsamples, maxtau_ms=100.0, fs=FS):
    """Window over the whole response, as NeuralExample.m sets it for a half raster:
    T0 at the centre, Tw = (NS - 2 MaxLag - 2) samples."""
    maxlag = int(np.ceil(maxtau_ms / 1000 * fs))
    T0 = np.floor(nsamples / fs * 1000 / 2)
    Tw = np.floor((nsamples - maxlag * 2 - 2) / fs * 1000) - 2  # 2 ms less, so that the
    return T0, Tw  # window plus lags stay inside the raster at the files' 2034.5 Hz rate


# ---------------------------------------------------------------- single-trial features

def _single(seg, Nw, maxlag):
    """seg: (channels, L) one trial, L = Nw + 2 + 2 maxlag. Code formulas with NT = 1 and
    the within-trial terms kept (unshuffled correlation). Returns spectral (C, C) zero-lag
    and temporal (C, 2 maxlag + 1) autocorrelations, and the window mean of each channel."""
    L = seg.shape[-1]
    Nw2 = (Nw - 1) // 2
    c = (L - 1) // 2
    x = seg[:, c - Nw2:c + Nw2 + 1]
    M1 = x.sum(-1) / Nw
    E21 = (x ** 2).sum(-1) / (Nw - 1)
    var1 = E21 - M1 ** 2
    # spectral, lag 0
    R0 = x @ x.T / Nw
    spec = (R0 - np.outer(M1, M1)) / np.sqrt(np.outer(var1, var1))
    # temporal, lags -maxlag..maxlag, shifted windows of the same channel
    W = np.zeros(L)
    W[c - Nw2:c + Nw2 + 1] = 1
    R = _xcorr(seg * W, seg, maxlag) / Nw
    cs = np.concatenate([np.zeros((seg.shape[0], 1)), np.cumsum(seg, -1)], -1)
    cs2 = np.concatenate([np.zeros((seg.shape[0], 1)), np.cumsum(seg ** 2, -1)], -1)
    lags = np.arange(-maxlag, maxlag + 1)
    st = (c - Nw2) - lags  # window over b shifted: indices j - m
    M2 = (cs[:, st + Nw] - cs[:, st]) / Nw
    E22 = (cs2[:, st + Nw] - cs2[:, st]) / (Nw - 1)
    var2 = E22 - M2 ** 2
    temp = (R - M1[:, None] * M2) / np.sqrt(var1[:, None] * var2)
    return spec, temp, M1


def single_trial_features(ras, n, Tw_ms, t_range_ms, rng, maxtau_ms=100.0, trial_pool=None):
    """n random (trial, time) samples; each a single-trial window of Tw_ms centred at a
    random time whose window plus lags lie inside t_range_ms = (start, end) of the raster.
    Returns spec (n, C*(C-1)/2) upper triangle without the diagonal (equal to 1 for one
    trial), temp (n, C, lags), rate (n, C)."""
    C, NT, NS = ras.shape
    maxlag = int(np.ceil(maxtau_ms / 1000 * FS))
    Nw = int(np.floor(FS * Tw_ms / 1000 / 2) * 2 + 1)
    L = Nw + 2 + 2 * maxlag
    lo = int(round(t_range_ms[0] / 1000 * FS))
    hi = int(round(t_range_ms[1] / 1000 * FS)) - L
    iu = np.triu_indices(C, 1)
    pool = np.arange(NT) if trial_pool is None else np.asarray(trial_pool)
    trials = rng.choice(pool, n)
    starts = rng.integers(lo, hi + 1, n)
    S = np.empty((n, len(iu[0])))
    T = np.empty((n, C, 2 * maxlag + 1), dtype=np.float32)
    Rt = np.empty((n, C))
    for i in range(n):
        seg = ras[:, trials[i], starts[i]:starts[i] + L].astype(np.float64)
        s, t, m = _single(seg, Nw, maxlag)
        S[i] = s[iu]
        T[i] = t
        Rt[i] = m
    return {"spec": S, "temp": T, "rate": Rt}


def shuffled_features(ras, n, Tw_ms, t_range_ms, rng, maxtau_ms=100.0):
    """Noiseless classifier features: shuffled (stimulus-driven) correlations over all trials
    (window_corr R12_sh), n random window centres. spec: upper triangle with diagonal."""
    C, NT, NS = ras.shape
    maxlag, Nw, _, _ = window_geometry(0, Tw_ms, maxtau_ms)
    half = (Nw + 1) / 2 + maxlag + 1
    lo = t_range_ms[0] + half / FS * 1000
    hi = t_range_ms[1] - half / FS * 1000
    iu = np.triu_indices(C)
    S, T = [], []
    for t0 in rng.uniform(lo, hi, n):
        t0 = round(t0 * FS / 1000) / FS * 1000
        tem = window_corr(ras, ras, t0, Tw_ms, maxtau_ms)["sh"]
        _, Nw_, s0, s1 = window_geometry(t0, Tw_ms, 0.0)
        sp = zero_lag_all(ras[:, :, s0:s1])["sh"]
        S.append(sp[iu])
        T.append(tem)
    return {"spec": np.array(S), "temp": np.array(T)}


# ---------------------------------------------------------------- classifier

class GaussNB:
    """Naive Bayes with axis-aligned Gaussian likelihoods and equal priors."""

    def fit(self, X, y):
        self.classes = np.unique(y)
        self.mu = np.array([X[y == c].mean(0) for c in self.classes])
        v = np.array([X[y == c].var(0) for c in self.classes])
        self.var = v + 1e-9 * X.var(0).max()
        return self

    def loglik(self, X):
        """(n, classes) log-likelihoods."""
        return -0.5 * (((X[:, None, :] - self.mu) ** 2) / self.var + np.log(2 * np.pi * self.var)).sum(-1)


class PCA:
    def fit(self, X):
        self.mean = X.mean(0)
        U, s, Vt = np.linalg.svd(X - self.mean, full_matrices=False)
        self.comp = Vt
        self.evr = s ** 2 / (s ** 2).sum()
        return self

    def transform(self, X, k):
        return (X - self.mean) @ self.comp[:k].T


def flat(f, kind):
    if kind == "temp":
        return f["temp"].reshape(len(f["temp"]), -1)
    return f[kind]


def loglik_grid(Xm, ym, Xv, kmax=40):
    """Log-likelihoods of validation features for every number of PCs 1..kmax.
    Returns array (kmax, n_val, classes)."""
    p = PCA().fit(Xm)
    kmax = min(kmax, Xm.shape[1], Xm.shape[0] - 1)
    Zm = p.transform(Xm, kmax)
    Zv = p.transform(Xv, kmax)
    out = []
    for k in range(1, kmax + 1):
        nb = GaussNB().fit(Zm[:, :k], ym)
        out.append(nb.loglik(Zv[:, :k]))
    return np.array(out)


def log_posterior(ll):
    m = ll.max(-1, keepdims=True)
    return ll - (m + np.log(np.exp(ll - m).sum(-1, keepdims=True)))


KINDS = ("spec", "temp", "temp_shuf", "rate")


def _features(f, kind, rng=None):
    """Feature matrix of one kind. temp_shuf permutes the channels of each sample afresh
    (Noiseless neural classifier, paragraph 7: the validation channels are reordered at
    random, the model data keep their order)."""
    if kind == "temp_shuf":
        T = f["temp"]
        perm = np.argsort(rng.random((T.shape[0], T.shape[1])), axis=1)
        return np.take_along_axis(T, perm[:, :, None], 1).reshape(len(T), -1)
    if kind == "temp":
        return f["temp"].reshape(len(f["temp"]), -1)
    return f[kind]


def _acc_1a(ll, y):
    return (ll.argmax(-1) == y).mean(-1)


def _acc_1b(ll, y, groups):
    """Reading (1)(b): log-likelihoods summed over the samples of each group (a sound in a
    fold), one decision per group."""
    out = []
    for g in np.unique(groups):
        m = groups == g
        out.append((ll[..., m, :].sum(-2).argmax(-1) == y[m][0]))
    return np.mean(out, 0)


def classify(folds, classes, kinds=("spec", "temp", "temp_shuf"), rng=None, kmax=40,
             alphas=np.round(np.arange(0, 1.01, 0.1), 1)):
    """folds: list of (model, val) where model = (features dict, labels) and val is a list,
    one per duration, of (features dict, labels). Returns accuracies under readings
    (1)(a)/(b) x (2)(a)/(b), per duration and per class, the chosen PCs and the mixing
    coefficient a (claims file readings (1), (2), (5); a chosen on (a) model or (b)
    validation log-likelihood, claim figs9-mixing-coefficient)."""
    nd = len(folds[0][1])
    LL = {k: [] for k in kinds}       # per fold: (kmax, n_val_total, classes)
    LLin = {k: [] for k in kinds}     # in-sample model log-likelihoods, for a (a)
    LLinner = {k: [] for k in kinds}  # inner split of the model data, for reading (2)(b)
    Y, D, G = [], [], []
    Ym = []
    for fi, (model, vals) in enumerate(folds):
        fm, ym = model
        yv = np.concatenate([v[1] for v in vals])
        dv = np.concatenate([np.full(len(v[1]), i) for i, v in enumerate(vals)])
        Y.append(yv); D.append(dv); G.append(fi * 1000 + dv * 10 + yv)
        Ym.append(ym)
        half = np.zeros(len(ym), bool)
        for c in np.unique(ym):
            idx = np.flatnonzero(ym == c)
            half[rng.permutation(idx)[: len(idx) // 2]] = True
        base = [k for k in kinds if k != "temp_shuf"]
        for k in base:
            Xm = _features(fm, k)
            group = [k] + (["temp_shuf"] if k == "temp" and "temp_shuf" in kinds else [])
            Xvs = [np.concatenate([_features(v[0], g, rng) for v in vals]) for g in group]
            Xin_v = _features(fm, k, rng)
            grid = loglik_grid(Xm, ym, np.concatenate(Xvs + [Xin_v]), kmax)
            for gi, g in enumerate(group):
                LL[g].append(grid[:, gi * len(yv):(gi + 1) * len(yv)])
                LLin[g].append(grid[:, len(group) * len(yv):])
            inner = (loglik_grid(Xm[half], ym[half], Xin_v[~half], kmax), ym[~half])
            for g in group:
                LLinner[g].append(inner)
    kk = {k: min(x.shape[0] for x in LL[k]) for k in kinds}
    res = {"pcs": {}, "alpha": {}, "acc": {}, "acc_class": {}}
    Yc, Dc, Gc = np.concatenate(Y), np.concatenate(D), np.concatenate(G)

    def per_duration(ll, rule):
        a = np.zeros((ll.shape[0], nd)) if ll.ndim == 3 else np.zeros(nd)
        cls = np.zeros((nd, len(classes)))
        for d in range(nd):
            m = Dc == d
            if rule == "1a":
                a[..., d] = _acc_1a(ll[..., m, :], Yc[m])
                if ll.ndim == 2:
                    for ci in range(len(classes)):
                        mc = m & (Yc == ci)
                        cls[d, ci] = (ll[mc].argmax(-1) == ci).mean()
            else:
                a[..., d] = _acc_1b(ll[..., m, :], Yc[m], Gc[m])
                if ll.ndim == 2:
                    for ci in range(len(classes)):
                        mc = m & (Yc == ci)
                        cls[d, ci] = _acc_1b(ll[mc], Yc[mc], Gc[mc])
        return a, cls

    for rule in ("1a", "1b"):
        for sel in ("2a", "2b"):
            key = rule + sel
            chosen = {}
            for k in kinds:
                ll = np.concatenate([x[: kk[k]] for x in LL[k]], axis=1)
                if sel == "2a":
                    curve, _ = per_duration(ll, rule)
                    chosen[k] = int(curve.mean(1).argmax())
                else:
                    inner = np.mean([(g[: kk[k]].argmax(-1) == yy).mean(-1) for g, yy in LLinner[k]], 0)
                    chosen[k] = int(inner.argmax())
                a, cls = per_duration(ll[chosen[k]], rule)
                res["acc"][(key, k)] = a
                res["acc_class"][(key, k)] = cls
                res["pcs"][(key, k)] = chosen[k] + 1
            if "spec" in kinds and "temp" in kinds:
                ls = np.concatenate([x[chosen["spec"]] for x in LL["spec"]])
                lt = np.concatenate([x[chosen["temp"]] for x in LL["temp"]])
                lsi = np.concatenate([x[chosen["spec"]] for x in LLin["spec"]])
                lti = np.concatenate([x[chosen["temp"]] for x in LLin["temp"]])
                ymc = np.concatenate(Ym)
                for asel in ("a", "b"):
                    best, bestv = None, -np.inf
                    for al in alphas:
                        if asel == "a":
                            lp = log_posterior(al * lsi + (1 - al) * lti)
                            v = lp[np.arange(len(ymc)), ymc].sum()
                        else:
                            lp = log_posterior(al * ls + (1 - al) * lt)
                            v = lp[np.arange(len(Yc)), Yc].sum()
                        if v > bestv:
                            best, bestv = al, v
                    a, cls = per_duration(best * ls + (1 - best) * lt, rule)
                    res["acc"][(key, "st_" + asel)] = a
                    res["acc_class"][(key, "st_" + asel)] = cls
                    res["alpha"][(key, asel)] = best
    return res


def _cat(fs):
    return {k: np.concatenate([f[k] for f in fs]) for k in fs[0]}


def half_ranges(nsamples):
    """First and second halves of the raster in ms (NeuralExample.m: NS2 = floor(NS/2))."""
    h = np.floor(nsamples / 2) / FS * 1000
    return [(0.0, h), (h, nsamples / FS * 1000)]


def build_folds(model_ras, val_ras, model_ranges, val_ranges, rng, n=100, model_ms=1000.0,
                durations=DURATIONS_MS, maker=single_trial_features):
    """model_ras / val_ras: lists over classes of lists of rasters (channels, trials, samples)
    (one raster per sound, or several exemplars per category). Fold i uses model_ranges[i]
    of the model rasters and val_ranges[i] of the validation rasters. n samples per raster."""
    folds = []
    for mr, vr in zip(model_ranges, val_ranges):
        fm, ym = [], []
        for c, rs in enumerate(model_ras):
            for r in rs:
                fm.append(maker(r, n, model_ms, mr, rng))
                ym.append(np.full(n, c))
        vals = []
        for d in durations:
            fv, yv = [], []
            for c, rs in enumerate(val_ras):
                for r in rs:
                    fv.append(maker(r, n, d, vr, rng))
                    yv.append(np.full(n, c))
            vals.append((_cat(fv), np.concatenate(yv)))
        folds.append(((_cat(fm), np.concatenate(ym)), vals))
    return folds


def clock_check(ras, shift_ms=250.0):
    """Stimulus locking: per channel, Pearson r between the PSTHs of odd and even trials,
    with true alignment and with the even trials shifted circularly by shift_ms."""
    sh = int(round(shift_ms / 1000 * FS))
    a = ras[:, 0::2].mean(1)
    b = ras[:, 1::2].mean(1)
    r_true = [np.corrcoef(a[c], b[c])[0, 1] for c in range(len(a))]
    r_shift = [np.corrcoef(a[c], np.roll(b[c], sh))[0, 1] for c in range(len(a))]
    return np.median(r_true), np.median(r_shift)


def raster_hash(a):
    """Hash of a raster's values, to find recordings deposited more than once."""
    import hashlib
    return hashlib.md5(np.ascontiguousarray(a[:, :2]).tobytes()).hexdigest()


def describe(d):
    """Counts, ranges and hashes of one site, for the data check."""
    out = {"param": d["param"], "fs": sorted(d["fs"]), "cond": {}, "fields": d["fields"]}
    for key, r in d["ras"].items():
        nt, ns = d["ntrials_ch"][key]
        out["cond"][key] = {"channels": r.shape[0], "trials": r.shape[1], "samples": r.shape[2],
                            "trials_equal": len(set(nt)) == 1, "samples_equal": len(set(ns)) == 1,
                            "min": float(r.min()), "max": float(r.max()), "mean": float(r.mean()),
                            "hash": [raster_hash(r[c]) for c in range(r.shape[0])],
                            "clock": clock_check(r)}
    return out


def process_p1(d, rng, noiseless=False):
    """Paradigm 1 site: correlations under each window reading, and the single-trial
    classifier (spectral, temporal, temporal without tonotopy, spectrum) with the half split;
    the noiseless classifier at 1 s when asked (example site only)."""
    ras = [d["ras"][(k, 0)] for k in range(5)]
    out = {"corr": [correlation_readings(r) for r in ras]}
    hr = half_ranges(min(r.shape[-1] for r in ras))
    folds = build_folds([[r] for r in ras], [[r] for r in ras], hr, hr[::-1], rng)
    out["single"] = classify(folds, P1_SOUNDS, kinds=KINDS, rng=rng)
    if noiseless:
        folds = build_folds([[r] for r in ras], [[r] for r in ras], hr, hr[::-1], rng,
                            model_ms=500.0, durations=[1000.0], maker=shuffled_features)
        out["noiseless"] = classify(folds, P1_SOUNDS, kinds=("spec", "temp", "temp_shuf"), rng=rng)
    return out


def process_p2(d, rng):
    """Paradigm 2 site (condition 0 = 1/f, 1 = original). Models from the original sounds;
    validation on the 1/f sounds under reading (3)(a) (half split) and (3)(b) (whole
    responses), and on the original sounds with the half split (control)."""
    orig = [d["ras"][(k, 1)] for k in range(5)]
    eq = [d["ras"][(k, 0)] for k in range(5)]
    out = {"corr_orig": [correlation_readings(r) for r in orig],
           "corr_eq": [correlation_readings(r) for r in eq]}
    ns = min(r.shape[-1] for r in orig + eq)
    hr = half_ranges(ns)
    whole = [(0.0, ns / FS * 1000)]
    out["eq_3a"] = classify(build_folds([[r] for r in orig], [[r] for r in eq], hr, hr[::-1], rng),
                            P1_SOUNDS, kinds=KINDS, rng=rng)
    out["eq_3b"] = classify(build_folds([[r] for r in orig], [[r] for r in eq], whole, whole, rng),
                            P1_SOUNDS, kinds=KINDS, rng=rng)
    out["orig"] = classify(build_folds([[r] for r in orig], [[r] for r in orig], hr, hr[::-1], rng),
                           P1_SOUNDS, kinds=KINDS, rng=rng)
    return out


def summarize_classifier(res, duration_index=-1):
    """Accuracies (%) at one duration, by reading and classifier."""
    return {k: 100 * v[duration_index] for k, v in res["acc"].items()}


def process_p3(d, rng, n=100):
    """Paradigm 3 site: three categories, six exemplars, leave one exemplar out (five train,
    the sixth is tested, for every category at once). Reading (a): model and validation
    windows anywhere in the whole response; reading (b): the half split on top (model from
    one half of the training exemplars, validation from the other half of the held-out one)."""
    ras = {k: v for k, v in d["ras"].items()}
    ns = min(r.shape[-1] for r in ras.values())
    whole = (0.0, ns / FS * 1000)
    hr = half_ranges(ns)
    out = {}
    for reading, ranges in (("a", [whole]), ("b", hr)):
        fm = {(c, e, h): single_trial_features(ras[(c, e)], n, 1000.0, ranges[h], rng)
              for c in range(3) for e in range(6) for h in range(len(ranges))}
        fv = {(c, e, h, di): single_trial_features(ras[(c, e)], n, dd, ranges[h], rng)
              for c in range(3) for e in range(6) for h in range(len(ranges)) for di, dd in enumerate(DURATIONS_MS)}
        folds = []
        for e_out in range(6):
            for h in range(len(ranges)):
                hv = h if reading == "a" else 1 - h
                model = (_cat([fm[(c, e, h)] for c in range(3) for e in range(6) if e != e_out]),
                         np.concatenate([np.full(n, c) for c in range(3) for e in range(6) if e != e_out]))
                vals = [(_cat([fv[(c, e_out, hv, di)] for c in range(3)]), np.concatenate([np.full(n, c) for c in range(3)]))
                        for di in range(len(DURATIONS_MS))]
                folds.append((model, vals))
        out[reading] = classify(folds, P3_CATEGORIES, kinds=KINDS, rng=rng)
        del fm, fv, folds
    return out


def p3_example_pca(d, rng, n=100):
    """Variance explained by the first two PCs of the training-set feature vectors
    (100 observations x 6 exemplars x 3 categories, Fig 8 legend) under the readings of
    claim fig8b-example-pca-variance, and a nearest-centroid leave-one-exemplar-out accuracy
    in the two-PC space."""
    ras = d["ras"]
    ns = min(r.shape[-1] for r in ras.values())
    whole = (0.0, ns / FS * 1000)
    feats = {}
    for lab, maker, ms in (("a_sh500", shuffled_features, 500.0), ("b_st1000", single_trial_features, 1000.0),
                           ("b_sh1000", shuffled_features, 1000.0)):
        feats[lab] = {(c, e): maker(ras[(c, e)], n, ms, whole, rng) for c in range(3) for e in range(6)}
    C = 16
    iu_d = np.triu_indices(C)
    out = {}
    for lab, F in feats.items():
        for spec_r in ("c", "d"):
            for kind in ("spec", "temp"):
                def X_of(f):
                    if kind == "temp":
                        return f["temp"].reshape(len(f["temp"]), -1).astype(np.float64)
                    if lab.startswith("b_st"):  # single trial: upper triangle without the diagonal (all 1)
                        M = np.zeros((len(f["spec"]), C, C))
                        iu = np.triu_indices(C, 1)
                        M[:, iu[0], iu[1]] = f["spec"]
                        M = M + M.transpose(0, 2, 1) + np.eye(C)
                    else:
                        M = np.zeros((len(f["spec"]), C, C))
                        M[:, iu_d[0], iu_d[1]] = f["spec"]
                        M = M + np.triu(M, 1).transpose(0, 2, 1)
                    if spec_r == "c":
                        return M[:, iu_d[0], iu_d[1]]
                    return M.reshape(len(M), -1)
                if kind == "temp" and spec_r == "d":
                    continue
                Xs = {k: X_of(f) for k, f in F.items()}
                X = np.concatenate([Xs[(c, e)] for c in range(3) for e in range(6)])
                y = np.concatenate([np.full(len(Xs[(c, e)]), c) for c in range(3) for e in range(6)])
                ex = np.concatenate([np.full(len(Xs[(c, e)]), e) for c in range(3) for e in range(6)])
                ev_all = PCA().fit(X).evr[:2].sum()
                ev_f, acc = [], []
                for e_out in range(6):
                    p = PCA().fit(X[ex != e_out])
                    ev_f.append(p.evr[:2].sum())
                    Z = p.transform(X, 2)
                    cents = np.array([Z[(ex != e_out) & (y == c)].mean(0) for c in range(3)])
                    zt = Z[ex == e_out]
                    pred = np.argmin(((zt[:, None] - cents) ** 2).sum(-1), 1)
                    acc.append((pred == y[ex == e_out]).mean())
                out[(lab, spec_r, kind)] = {"ev_all6": 100 * ev_all, "ev_folds": 100 * np.mean(ev_f),
                                            "nc_acc": 100 * np.mean(acc)}
    return out
