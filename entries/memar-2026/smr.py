"""Loading and measures for testing Ostadsharif Memar & Dehghani (2026), "Spatially Masked
Regression", on AJILE12 (DANDI:000055).

Where each parameter comes from:

- Trials. 2 s windows centred on the start of each wrist movement event of the `reaches` table
  (the same times as processing/behavior/ReachEvents), every session of a subject pooled. Claims
  file, opening comment, "Which movement events", reading (a), and "Which recording days".
- Preprocessing. The steps and their order are the paper's (Methods II A a): DC removal and linear
  detrending, 0.5 to 150 Hz Butterworth band-pass, 60 Hz notch, 120 Hz low-pass, |z| > 5 replaced
  by the channel median, common average reference, per-channel z-scoring across time. Filter
  orders (4th-order Butterworth, zero phase with filtfilt; notch Q = 30) are the paper's code
  (utils.preprocess_iEEG), which the claims file read. The code's median filter and Hilbert
  envelope are left out, as the claims file says.
  Where preprocessing is applied is open (claims file, readings a and b):
  (a) `continuous`: the paper's order (preprocess, then segment). The whole recording is 16 GB a
      file, so each event is read with 5 s of padding on each side, filtered, and cut to its
      centre; the statistics of the |z| > 5 step and of the z-scoring are taken over all the
      event windows of the session, standing in for the whole recording. An approximation of
      reading (a), stated as such.
  (b) `epoch`: every step applied to each 2 s epoch on its own.
- Electrodes. All electrodes; none excluded (claims file, "Trial and electrode exclusion").
- Neighbourhood. The 9 electrodes nearest in the (x, z) projection of the MNI coordinates, the
  electrode itself excluded (Methods II B).
- Mask. ceil(m |N(i)|) neighbours drawn at random and masked with i (Results III D); `round` is
  the code's variant (neighborhood.find_index_mask).
- Model and training. Eq. 1 with a bias; loss mean absolute error + 1e-5 L1 + 1e-4 squared L2 on
  all parameters with the bias (Eq. 2, Methods II F); Adam (betas 0.9, 0.999, eps 1e-8, PyTorch's
  defaults, which the code uses), learning rate 0.01, batches of 32 trials, patience 200 epochs on
  the epoch-averaged validation loss, at most 10000 epochs, best validation checkpoint kept
  (claims file, from configs/settings.yaml and train.py). Weights start uniform in
  +-1/sqrt(fan_in), as PyTorch's nn.Linear (standard choice). All electrodes are trained at once
  as independent rows of one weight matrix; Adam's updates are per parameter and each row's loss
  is its own, so this is the same as one model per electrode, except that the batches are shared.
  `decim` keeps every k-th time sample of each trial for the gradient steps and the validation
  loss (a speed deviation, stated in the notebook); the test score uses every sample.
- Split. z-score across trials (each channel and time sample), then 64/16/20 by two nested 80/20
  random splits (Methods II D 1; sklearn train_test_split with random_state 42 in the code).
- Score. Distance correlation (Eqs. 8 to 14) per test trial, averaged over trials; computed with
  the exact O(n log n) algorithm of the `dcor` package (the same V-statistic as the paper's
  double-centred matrices).
- Lagged model. Lags 0, 20, 30, 50, 60 ms, offsets ceil(tau fs / 1000) samples, zero before the
  trial start (Methods II E, Eq. 6; model.LaggedReconModelConfigurable). One bias in place of the
  code's one per lag (a standard choice; a sum of biases is one bias).
- Surrogates. Per trial and channel (Algorithm 4; Load_preprocess_data): phase permutation with
  Hermitian symmetry and DC kept (shuffle_phase), IAAFT with 5 iterations (iaaft_1d), blocks of
  0.5 s (block_shuffle_1d default).
- Cross-subject (Methods II D 2, Algorithm 2; Test_new_subject_iEEG.py): see `cross_subject`.
"""
from __future__ import annotations

import math
import os
from concurrent.futures import ProcessPoolExecutor

import h5py
import numpy as np
import remfile
import requests
from scipy import signal
from scipy.optimize import linear_sum_assignment

DANDISET = "000055"
VERSION = "0.220127.0436"
API = "https://api.dandiarchive.org/api"
FS = 500.0
HALF = 500          # samples on each side of the event: 2 s trials
PAD = 2500          # 5 s of padding for reading (a)
L1, L2 = 1e-5, 1e-4
LAGS_MS = (0, 20, 30, 50, 60)


# ----------------------------------------------------------------------------- archive
def assets():
    """Every asset of the pinned version: list of dicts with path, asset_id, size."""
    out, url = [], f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=200"
    while url:
        r = requests.get(url, timeout=60).json()
        out += r["results"]
        url = r["next"]
    return sorted(out, key=lambda a: a["path"])


def s3_url(asset_id):
    r = requests.get(f"{API}/assets/{asset_id}/download/", allow_redirects=False, timeout=60)
    return r.headers["Location"]


def open_nwb(asset_id):
    return h5py.File(remfile.File(s3_url(asset_id)), "r")


# ----------------------------------------------------------------------------- preprocessing
_B_BP = signal.butter(4, [0.5 / (FS / 2), 150 / (FS / 2)], btype="band")
_B_NOTCH = signal.iirnotch(60 / (FS / 2), 30)
_B_LP = signal.butter(4, 120 / (FS / 2), btype="low")


def filter_steps(x):
    """DC removal, linear detrend, band-pass, notch and low-pass on (time, channels)."""
    x = x - x.mean(axis=0)
    x = signal.detrend(x, axis=0, type="linear")
    x = signal.filtfilt(*_B_BP, x, axis=0)
    x = signal.filtfilt(*_B_NOTCH, x, axis=0)
    x = signal.filtfilt(*_B_LP, x, axis=0)
    return x


def stat_steps(x, mean, std, med):
    """|z| > 5 replaced by the channel median, common average reference, z-score across time.

    x: (..., time, channels); mean, std, med: per channel statistics of the filtered signal.
    """
    x = x.copy()
    z = np.abs((x - mean) / std)
    x = np.where(z > 5, med, x)
    x = x - x.mean(axis=-1, keepdims=True)
    return x


_WORKER = {}


def _init_worker(url):
    # remfile keeps up to 1 GB of cache by default; 16 workers would exhaust the memory
    _WORKER["d"] = h5py.File(remfile.File(url, _max_cache_size=64e6), "r")[
        "acquisition/ElectricalSeries/data"]


def _read_event(i0):
    """One event: the filtered padded centre (reading a) and the filtered bare epoch (reading b)."""
    d = _WORKER["d"]
    raw = d[i0 - HALF - PAD:i0 + HALF + PAD, :].astype(np.float64)
    fin = np.isfinite(raw)
    if not fin.all():
        return None, None, (~fin[PAD:PAD + 2 * HALF]).any(), (~fin).any(0)
    a = filter_steps(raw)[PAD:PAD + 2 * HALF]
    b = filter_steps(raw[PAD:PAD + 2 * HALF])
    return a.astype(np.float32), b.astype(np.float32), False, None


def load_session(asset_id, workers=32):
    """Events of one session, preprocessed under both readings.

    Returns dict with 'a' and 'b' (trials, channels, time) float32, the event times kept, the
    number of events dropped at the file's edges, the number dropped for non-finite samples in
    the padded window (`nan_pad`) and, of these, in the 2 s epoch itself (`nan_epoch`).
    """
    url = s3_url(asset_id)
    f = h5py.File(remfile.File(url), "r")
    n_samp = f["acquisition/ElectricalSeries/data"].shape[0]
    t = f["intervals/reaches/start_time"][:]
    i0 = np.round(t * FS).astype(int)
    keep = (i0 - HALF - PAD >= 0) & (i0 + HALF + PAD <= n_samp)
    with ProcessPoolExecutor(workers, initializer=_init_worker, initargs=(url,)) as ex:
        # consecutive events to the same worker, so events in the same HDF5 chunk share its cache
        res = list(ex.map(_read_event, i0[keep], chunksize=4))
    ok = [r[0] is not None for r in res]
    a = np.stack([r[0] for r in res if r[0] is not None])            # (trials, time, ch)
    b = np.stack([r[1] for r in res if r[1] is not None])
    nan_pad = int(len(ok) - sum(ok))
    nan_epoch = int(sum(r[2] for r in res))
    # reading (a): statistics over all event windows of the session
    flat = a.reshape(-1, a.shape[-1])
    mean, std, med = flat.mean(0), flat.std(0), np.median(flat, 0)
    a = stat_steps(a, mean, std, med)
    flat = a.reshape(-1, a.shape[-1])
    a = (a - flat.mean(0)) / flat.std(0)
    # reading (b): every statistic within the epoch
    mean, std, med = b.mean(1, keepdims=True), b.std(1, keepdims=True), np.median(b, 1, keepdims=True)
    b = stat_steps(b, mean, std, med)
    b = (b - b.mean(1, keepdims=True)) / b.std(1, keepdims=True)
    return dict(a=np.ascontiguousarray(a.transpose(0, 2, 1), dtype=np.float32),
                b=np.ascontiguousarray(b.transpose(0, 2, 1), dtype=np.float32),
                times=t[keep][ok], dropped=int((~keep).sum()), nan_pad=nan_pad,
                nan_epoch=nan_epoch)


def load_subject(sub, readings=("a", "b"), workers=32):
    """All sessions of one subject ('sub-01'), pooled. Returns the trials of each reading
    (reading b kept as float16 to save memory), the electrode table of the first session, and
    per-session counts."""
    ss = [a for a in assets() if a["path"].startswith(sub + "/")]
    out = {r: [] for r in readings}
    info = []
    for a in ss:
        s = load_session(a["asset_id"], workers)
        for r in readings:
            out[r].append(s[r].astype(np.float16 if r == "b" else np.float32))
        info.append(dict(path=a["path"], trials=len(s["times"]), dropped_edge=s["dropped"],
                         dropped_nan=s["nan_pad"], nan_in_epoch=s["nan_epoch"]))
    res = {r: np.concatenate(v) for r, v in out.items()}
    res["el"] = electrodes(ss[0]["asset_id"])
    res["sessions"] = info
    return res


def electrodes(asset_id):
    """Electrode table of one file as a dict of arrays."""
    f = open_nwb(asset_id)
    el = f["general/extracellular_ephys/electrodes"]
    out = {}
    for k in ("x", "y", "z", "good", "location", "group_name"):
        v = el[k][:]
        out[k] = np.array([s.decode() for s in v]) if v.dtype.kind == "O" else v
    return out


# ----------------------------------------------------------------------------- neighbourhood
def neighbours(xyz, k=9):
    """N(i): the k electrodes nearest to i in the (x, z) projection, i excluded (Methods II B)."""
    p = xyz[:, [0, 2]]
    d = np.sqrt(((p[:, None, :] - p[None, :, :]) ** 2).sum(-1))
    np.fill_diagonal(d, np.inf)
    return np.argsort(d, axis=1, kind="stable")[:, :k]


def mask_matrix(nbr, m, rng, rule="ceil", mode="mask"):
    """Boolean (N, N) matrix of allowed predictors: True where j may predict i.

    mode 'mask': i and ceil(m |N|) random neighbours excluded (Results III D).
    mode 'local': only N(i) allowed (Results III E, "Local").
    """
    n = nbr.shape[0]
    allow = np.ones((n, n), bool)
    if mode == "local":
        allow[:] = False
        for i in range(n):
            allow[i, nbr[i]] = True
        return allow
    k = nbr.shape[1]
    n_mask = math.ceil(m * k - 1e-9) if rule == "ceil" else int(round(m * k))
    for i in range(n):
        allow[i, i] = False
        if n_mask:
            allow[i, rng.choice(nbr[i], n_mask, replace=False)] = False
    return allow


# ----------------------------------------------------------------------------- data split
def zscore_trials(x):
    """z-score each channel and time sample across trials (scipy.stats.zscore, axis 0)."""
    sd = x.std(0)
    sd[sd == 0] = 1
    return ((x - x.mean(0)) / sd).astype(np.float32)


def split_64_16_20(n, seed=42):
    """Two nested 80/20 splits as sklearn train_test_split(..., random_state=seed)."""
    from sklearn.model_selection import train_test_split
    idx = np.arange(n)
    trval, te = train_test_split(idx, test_size=0.2, random_state=seed)
    tr, va = train_test_split(trval, test_size=0.2, random_state=seed)
    return tr, va, te


# ----------------------------------------------------------------------------- model
def lag_samples():
    return [math.ceil(t / 1000 * FS - 1e-9) for t in LAGS_MS]


def features(x, lagged=False):
    """(trials, ch, time) -> (trials, time, ch * n_lags) predictors, zero before trial start."""
    xt = x.transpose(0, 2, 1)
    if not lagged:
        return xt
    out = np.zeros(xt.shape[:2] + (xt.shape[2] * len(LAGS_MS),), np.float32)
    n = xt.shape[2]
    for k, s in enumerate(lag_samples()):
        if s == 0:
            out[:, :, :n] = xt
        else:
            out[:, s:, k * n:(k + 1) * n] = xt[:, :-s]
    return out


def fit_smr(x, tr, va, allow, rng, lagged=False, decim=1, lr=0.01, batch=32, patience=200,
            max_epoch=10000):
    """Train every electrode's masked linear model with Adam and early stopping.

    x: (trials, ch, time) z-scored across trials. allow: (ch, ch) predictors allowed.
    Returns weights W (ch, ch * n_lags), biases b (ch,), and the epoch at which each row's best
    validation loss was reached.
    """
    n = x.shape[1]
    nl = len(LAGS_MS) if lagged else 1
    A = np.tile(allow, (1, nl)).astype(np.float32)
    fan = A.sum(1, keepdims=True)
    bound = 1 / np.sqrt(fan)
    W = (rng.uniform(-1, 1, (n, n * nl)) * bound * A).astype(np.float32)
    b = (rng.uniform(-1, 1, (n, 1)) * bound).astype(np.float32).ravel()
    Xf = features(x, lagged)[:, ::decim]             # (trials, time', ch * nl)
    Y = x.transpose(0, 2, 1)[:, ::decim]              # (trials, time', ch)
    Xva, Yva = Xf[va].reshape(-1, n * nl), Y[va].reshape(-1, n)
    mW, vW = np.zeros_like(W), np.zeros_like(W)
    mb, vb = np.zeros_like(b), np.zeros_like(b)
    b1, b2, eps = 0.9, 0.999, 1e-8
    best = np.full(n, np.inf)
    bestW, bestb = W.copy(), b.copy()
    best_ep = np.zeros(n, int)
    wait = np.zeros(n, int)
    step = 0
    for ep in range(max_epoch):
        order = rng.permutation(tr)
        for s in range(0, len(order), batch):
            idx = order[s:s + batch]
            Xb = Xf[idx].reshape(-1, n * nl)
            Yb = Y[idx].reshape(-1, n)
            R = Xb @ W.T + b - Yb
            G = np.sign(R) / R.shape[0]
            gW = (G.T @ Xb + L1 * np.sign(W) + 2 * L2 * W) * A
            gb = G.sum(0) + L1 * np.sign(b) + 2 * L2 * b
            step += 1
            c1, c2 = 1 - b1 ** step, 1 - b2 ** step
            mW = b1 * mW + (1 - b1) * gW
            vW = b2 * vW + (1 - b2) * gW * gW
            W -= (lr * (mW / c1) / (np.sqrt(vW / c2) + eps)).astype(np.float32)
            mb = b1 * mb + (1 - b1) * gb
            vb = b2 * vb + (1 - b2) * gb * gb
            b -= (lr * (mb / c1) / (np.sqrt(vb / c2) + eps)).astype(np.float32)
        val = np.abs(Xva @ W.T + b - Yva).mean(0)
        better = val < best
        best[better] = val[better]
        bestW[better], bestb[better] = W[better], b[better]
        best_ep[better] = ep
        wait[better] = 0
        wait[~better] += 1
        if (wait >= patience).all():
            break
    return bestW, bestb, best_ep, ep + 1


def predict(x, W, b, lagged=False):
    """Reconstruction (trials, ch, time) from the full-rate predictors."""
    Xf = features(x, lagged)
    return (Xf @ W.T + b).transpose(0, 2, 1)


def _dcor_chunk(args):
    import dcor
    u, v = args
    return np.asarray(dcor.rowwise(dcor.distance_correlation, u, v, method="mergesort"))


_POOL = {}


def dcor_rows(u, v, workers=4):
    """Distance correlation of each row pair (Eqs. 8 to 14); 0 where a row is constant."""
    u = np.ascontiguousarray(u, dtype=np.float64)
    v = np.ascontiguousarray(v, dtype=np.float64)
    if len(u) < 400:
        out = _dcor_chunk((u, v))
    else:
        if "p" not in _POOL:
            _POOL["p"] = ProcessPoolExecutor(workers)
        parts = np.array_split(np.arange(len(u)), workers * 4)
        out = np.concatenate(list(_POOL["p"].map(_dcor_chunk, [(u[p], v[p]) for p in parts])))
    const = (u.std(1) == 0) | (v.std(1) == 0)
    out[const] = 0.0
    return np.nan_to_num(out)


def score(x, xhat, te):
    """Per-electrode mean over test trials of the per-trial DistCorr."""
    n = x.shape[1]
    u = x[te].reshape(-1, x.shape[2])
    v = xhat[te].reshape(-1, x.shape[2])
    return dcor_rows(u, v).reshape(len(te), n).mean(0)


def run_smr(x, nbr, m, rng, *, lagged=False, decim=1, rule="ceil", mode="mask", split_seed=42,
            max_epoch=10000):
    """One intra-subject SMR run. x: preprocessed trials (trials, ch, time), not yet z-scored
    across trials; rng: the claim's generator (mask draws, initial weights, batch order).
    Returns per-electrode test DistCorr, W, b, and fit diagnostics."""
    xz = zscore_trials(x)
    tr, va, te = split_64_16_20(len(x), split_seed)
    allow = mask_matrix(nbr, m, rng, rule=rule, mode=mode)
    W, b, best_ep, n_ep = fit_smr(xz, tr, va, allow, rng, lagged=lagged, decim=decim,
                                   max_epoch=max_epoch)
    xhat = predict(xz[te], W, b, lagged)
    dc = score(xz[te], xhat, np.arange(len(te)))
    return dict(dc=dc, W=W, b=b, best_ep=best_ep, n_ep=n_ep, allow=allow)


# ----------------------------------------------------------------------------- surrogates
def shuffle_phase(sig, rng):
    """Load_preprocess_data.shuffle_phase, with a seeded generator."""
    n = len(sig)
    F = np.fft.fft(sig)
    amp, ph = np.abs(F), np.angle(F)
    half = n // 2
    pos = np.arange(1, half)
    rp = rng.permutation(ph[pos])
    ph2 = ph.copy()
    ph2[pos] = rp
    ph2[-pos] = -rp
    return np.fft.ifft(amp * np.exp(1j * ph2)).real


def iaaft(sig, rng, n_iter=5):
    """Load_preprocess_data.iaaft_1d, with a seeded generator."""
    s = np.sort(sig)
    mag = np.abs(np.fft.fft(sig))
    z = rng.permutation(sig)
    for _ in range(n_iter):
        Z = np.fft.fft(z)
        zn = np.fft.ifft(mag * np.exp(1j * np.angle(Z))).real
        z = s[np.argsort(np.argsort(zn))]
    return z


def block_shuffle(sig, rng, block=250):
    """Load_preprocess_data.block_shuffle_1d with 0.5 s blocks at 500 Hz."""
    nb = len(sig) // block
    rem = len(sig) % block
    blocks = [sig[i * block:(i + 1) * block] for i in range(nb)]
    out = np.concatenate([blocks[i] for i in rng.permutation(nb)])
    return np.concatenate([out, sig[-rem:]]) if rem else out


def surrogate(x, kind, rng, batch=20000):
    """Surrogate of every trial and channel independently (Algorithm 4), vectorised over rows:
    the same operations as `shuffle_phase`, `iaaft` and `block_shuffle`, with each row's
    permutation drawn by `rng.permuted` (the draws differ from a per-row loop; a standard choice).
    x: (trials, ch, time)."""
    shp = x.shape
    rows = x.reshape(-1, shp[-1]).astype(np.float64)
    out = np.empty_like(rows)
    n = shp[-1]
    for s in range(0, len(rows), batch):
        r = rows[s:s + batch]
        if kind == "phase":
            F = np.fft.fft(r, axis=1)
            amp, ph = np.abs(F), np.angle(F)
            pos = np.arange(1, n // 2)
            rp = rng.permuted(ph[:, pos], axis=1)
            ph[:, pos] = rp
            ph[:, n - pos] = -rp
            out[s:s + batch] = np.fft.ifft(amp * np.exp(1j * ph), axis=1).real
        elif kind == "iaaft":
            srt = np.sort(r, axis=1)
            mag = np.abs(np.fft.fft(r, axis=1))
            z = rng.permuted(r, axis=1)
            for _ in range(5):
                zn = np.fft.ifft(mag * np.exp(1j * np.angle(np.fft.fft(z, axis=1))), axis=1).real
                z = np.empty_like(zn)
                np.put_along_axis(z, np.argsort(zn, axis=1), srt, axis=1)
            out[s:s + batch] = z
        elif kind == "block":
            B = 250
            nb, rem = n // B, n % B
            perm = np.argsort(rng.random((len(r), nb)), axis=1)
            idx = (perm[:, :, None] * B + np.arange(B)).reshape(len(r), nb * B)
            if rem:
                idx = np.concatenate([idx, np.broadcast_to(np.arange(nb * B, n), (len(r), rem))], 1)
            out[s:s + batch] = np.take_along_axis(r, idx, axis=1)
    return out.reshape(shp).astype(np.float32)


# ----------------------------------------------------------------------------- cross-subject
def corr_matrix_paired(xs, xd):
    """Eq. 3: Pearson correlation of target electrode i and donor electrode j on paired trials
    1..min(R_s, R_s'), averaged over trials, NaN trials left out. xs, xd: (trials, ch, time)."""
    r = min(len(xs), len(xd))
    acc = np.zeros((xs.shape[1], xd.shape[1]))
    cnt = np.zeros_like(acc)
    for t in range(r):
        a = xs[t] - xs[t].mean(1, keepdims=True)
        c = xd[t] - xd[t].mean(1, keepdims=True)
        na, nc = np.linalg.norm(a, axis=1), np.linalg.norm(c, axis=1)
        with np.errstate(invalid="ignore", divide="ignore"):
            C = (a @ c.T) / np.outer(na, nc)
        ok = np.isfinite(C)
        acc[ok] += C[ok]
        cnt += ok
    with np.errstate(invalid="ignore"):
        return acc / cnt


def corr_matrix_concat(xs, xd):
    """The code's variant (similarity.cross_subject_pearson): trial-concatenated series, truncated
    to the common length."""
    a = xs.transpose(1, 0, 2).reshape(xs.shape[1], -1)
    c = xd.transpose(1, 0, 2).reshape(xd.shape[1], -1)
    L = min(a.shape[1], c.shape[1])
    a, c = a[:, :L], c[:, :L]
    a = a - a.mean(1, keepdims=True)
    c = c - c.mean(1, keepdims=True)
    return (a @ c.T) / np.outer(np.linalg.norm(a, axis=1), np.linalg.norm(c, axis=1))


def transfer(C, M):
    """Hungarian assignment maximising summed correlation, M_est = P M P^T (Eqs. 4, 5).

    Returns M_est (Ns, Ns) and the rows of the target that were matched."""
    safe = np.where(np.isfinite(C), C, np.nanmin(C))
    r, c = linear_sum_assignment(-safe)
    P = np.zeros(C.shape)
    P[r, c] = 1
    matched = np.zeros(C.shape[0], bool)
    matched[r] = True
    return P @ M @ P.T, matched


def _z(v):
    sd = v.std(-1, keepdims=True)
    sd[sd == 0] = 1
    return (v - v.mean(-1, keepdims=True)) / sd


def cross_subject(target, donors, which_c="all", corr="paired", split_seed=42):
    """Per-electrode donor selection (Algorithm 2) on trial-averaged signals.

    target: preprocessed trials (trials, ch, time) of the target, not z-scored across trials (as
    Test_new_subject_iEEG.py, which averages the stored trials). donors: list of (trials_d, W_d),
    each donor's preprocessed trials and its m = 1.0 intra-subject weight matrix.
    which_c: 'all' trials of the target enter C (code), or 'val' only.
    Returns per-electrode test DistCorr (NaN where no donor matched) and the donor chosen.
    """
    from sklearn.model_selection import train_test_split
    idx = np.arange(len(target))
    va, te = train_test_split(idx, test_size=0.5, random_state=split_seed)
    vmean, tmean = target[va].mean(0), target[te].mean(0)
    n = target.shape[1]
    val_dc = np.full((len(donors), n), np.nan)
    test_dc = np.full((len(donors), n), np.nan)
    src = target if which_c == "all" else target[va]
    for k, (xd, Wd) in enumerate(donors):
        C = corr_matrix_paired(src, xd) if corr == "paired" else corr_matrix_concat(src, xd)
        Mest, matched = transfer(C, Wd)
        rv = _z(Mest @ vmean)
        rt = _z(Mest @ tmean)
        val_dc[k, matched] = dcor_rows(_z(vmean)[matched], rv[matched])
        test_dc[k, matched] = dcor_rows(_z(tmean)[matched], rt[matched])
    has = np.isfinite(val_dc).any(0)
    choice = np.full(n, -1)
    choice[has] = np.nanargmax(val_dc[:, has], axis=0)
    out = np.full(n, np.nan)
    out[has] = test_dc[choice[has], np.where(has)[0]]
    return out, choice


# ----------------------------------------------------------------------------- survey and checks
def survey_file(a):
    """Metadata and array shapes of one file (no signal is read)."""
    f = open_nwb(a["asset_id"])
    es = f["acquisition/ElectricalSeries"]
    el = f["general/extracellular_ephys/electrodes"]
    xyz = np.c_[el["x"][:], el["y"][:], el["z"][:]]
    loc = sorted({s.decode() for s in el["location"][:]})
    return dict(path=a["path"], subject=a["path"].split("/")[0], samples=es["data"].shape[0],
                channels=es["data"].shape[1], rate=float(es["starting_time"].attrs["rate"]),
                conversion=float(es["data"].attrs["conversion"]), unit=es["data"].attrs["unit"],
                hours=es["data"].shape[0] / float(es["starting_time"].attrs["rate"]) / 3600,
                reaches=len(f["intervals/reaches/start_time"]),
                reach_events=len(f["processing/behavior/ReachEvents/timestamps"]),
                good=int(el["good"][:].sum()), no_coords=int(np.isnan(xyz).any(1).sum()),
                x_pos=int((xyz[:, 0] > 0).sum()), x_neg=int((xyz[:, 0] < 0).sum()),
                locations=",".join(loc), times=f["intervals/reaches/start_time"][:],
                reaches_after_end=int((f["intervals/reaches/start_time"][:] * FS
                                       >= es["data"].shape[0]).sum()),
                reach_vs_events_max_diff_s=float(np.abs(
                    f["intervals/reaches/start_time"][:]
                    - f["processing/behavior/ReachEvents/timestamps"][:]).max()))


def survey(workers=16):
    from concurrent.futures import ThreadPoolExecutor
    import pandas as pd
    with ThreadPoolExecutor(workers) as ex:
        rows = list(ex.map(survey_file, assets()))
    return pd.DataFrame(rows)


def hg_power(x, lo=70, hi=110):
    """High-gamma power (band-pass 70 to 110 Hz, squared) of trials (trials, ch, time)."""
    b, a = signal.butter(4, [lo / (FS / 2), hi / (FS / 2)], btype="band")
    return signal.filtfilt(b, a, x.astype(np.float64), axis=-1) ** 2


def clock_check(x, rng, n_perm=200):
    """Event-locked change: per electrode, high-gamma power 0 to 0.75 s after the event minus
    0.75 to 0 s before, paired over trials (t statistic). The largest |t| over electrodes is
    compared with a null in which the pre and post labels are swapped at random per trial.
    Returns the observed max |t|, the null 95th percentile, and the electrode count with |t| > 4."""
    p = hg_power(x)
    pre = np.log(p[:, :, 125:500].mean(-1))
    post = np.log(p[:, :, 500:875].mean(-1))
    d = post - pre

    def tmax(d):
        t = d.mean(0) / (d.std(0, ddof=1) / np.sqrt(len(d)))
        return np.abs(t).max(), t
    obs, t = tmax(d)
    null = np.array([tmax(d * rng.choice([-1, 1], (len(d), 1)))[0] for _ in range(n_perm)])
    return obs, np.percentile(null, 95), int((np.abs(t) > 4).sum()), t


def drop_uncoordinated(S):
    """Drop electrodes with no MNI coordinates: they have no (x, z) neighbourhood (Methods II B).
    The paper names no such exclusion; it is this attempt's choice for a rare input."""
    el = S["el"]
    xyz = np.c_[el["x"], el["y"], el["z"]]
    keep = np.isfinite(xyz).all(1)
    S = dict(S)
    for r in ("a", "b"):
        if r in S:
            S[r] = S[r][:, keep]
    S["el"] = {k: v[keep] for k, v in el.items()}
    S["xyz"] = xyz[keep]
    S["n_dropped_el"] = int((~keep).sum())
    return S


def list_file(asset_id):
    """Every group and dataset of one file, with shapes; the columns of each table are its
    datasets."""
    f = open_nwb(asset_id)
    lines = []
    f.visititems(lambda name, obj: lines.append(
        f"{name}  {obj.shape} {obj.dtype}" if isinstance(obj, h5py.Dataset) else f"{name}/"))
    return lines
