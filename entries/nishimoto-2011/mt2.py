"""Loading CRCNS mt-2 and fitting the V1 filter bank model of Nishimoto and Gallant (2011).

Each of the 45 files holds one MT neuron: `rawStims` (frames x 128 x 128, uint8, the movie
patch around the receptive field), `psths` (spike counts per 83 Hz frame, averaged over
repeats; NaN where responses were removed), and `ranges` with `crange` (training frames),
`vrange` (validation frames) and, in 15 files, `nrange` (an undocumented subset of
`vrange`). The files are streamed from the public S3 bucket; nothing is written to disk.

Where each parameter comes from (P = the paper, with its passage; C = the claims file;
A = an assumption, with why; S = a standard choice that cannot change a result; D = a
deviation forced by compute, stated in the attempt record):

- cRF = half the stored patch (C, opening comment, reading (a); the data descriptor says the
  patch covers "around 2 times the receptive field", so readings (a) and (b) coincide).
- Frames are block-averaged from 128 x 128 to 32 x 32 pixels (16 px per cRF), which keeps
  the highest filter frequency, 6 cycles per cRF, below the Nyquist limit of 8 (S).
- Filter bank (P, Materials and Methods, "The V1 filter bank"): spatial frequencies 0, 0.75,
  1.5, 3 and 6 cycles per cRF ("log distributed from zero to six"; the four non-zero values
  are an octave apart, A); envelope SD = half a carrier cycle ("one cycle of the sine wave
  was two sigma"); grid spacing 2.2 sigma; 12 directions; simple cells only up to 2 cycles
  per cRF; complex cells as the quadrature amplitude (Eq. 4). Temporal frequencies 0, 3.75,
  7.5, 15 and 30 Hz (the paper gives "log distributed from 0 to 30 Hz" and six velocities;
  five values an octave apart, A). Temporal envelope: 11 frames, SD 2 frames (the paper
  gives no temporal width, A). The SF 0 filter is a Gaussian blob of SD 0.5 cRF (A).
- Regression weights are constrained to be spatially pooled (D): complex outputs of the full
  bank are summed with Gaussian weights (SD 0.5 cRF) onto 4 regions centred at
  (+-0.5, +-0.5) cRF for 3 and 6 cycles per cRF, and onto one central region for 0.75 and
  1.5; simple cells enter at 0.75 cycles per cRF (one position) and SF 0. This keeps
  the regression near 800 channels so that 12 models x 45 neurons fit in the time limit.
  Two finer poolings of the main model (`pooling`, levels "3x3" and "fine") measure what
  this constraint costs.
- Static nonlinearity HR(x)^alpha (Eq. 13) on every filter output (C), then divisive
  normalization by the sum of all filter outputs, each scaled to unit SD over the training
  frames, plus sigma (Eq. 14; C: order as in Figure 2A).
- Luminance and contrast normalization (Eqs. 10-12) per frame over the patch (P).
- Delays 0 to 10 frames (C, reading (a)); reading (b), 1 to 10, is a sub-block of the same fit.
- Boosting (P, "Regression by boosting", Eqs. 6-9) on features z-scored over the training
  frames (S), step 0.01 SD of the response (C: "a standard small value"), stopped when the
  error on the held-out 20% has not fallen below its minimum for 50 steps, and the weights at
  the minimum kept (S: "terminated when prediction errors ... began to increase"); five
  contiguous held-out blocks (C, reading (a)); the five weight sets averaged (P).
  The Gram matrix of the lagged design is assembled from lag cross-products of the unlagged
  features over the same rows, which is exact up to the 10 frames at block edges and the
  removed frames (S, numerical).
- Validation response smoothed with a Gaussian of SD 1 frame (12 ms; C, reading (a)); the
  first 20 frames of each validation set, whose features reach back before the set, are
  left out of the correlation (S).
"""

import re
import time

import fsspec
import h5py
import numpy as np
import requests
from scipy.ndimage import gaussian_filter1d
from scipy.stats import pearsonr

DATASET = "crcns:mt-2/unversioned"  # CRCNS data sets are not versioned; checksums.md5 pins the files
BUCKET = "https://crcnsarchive.s3-us-west-2.amazonaws.com/"
DATA = BUCKET + "mt-2/live/data/"
FPS = 83.0
NPIX = 32  # pixels after block averaging; 2 cRF
CRF = NPIX / 2.0
SFS = [0.75, 1.5, 3.0, 6.0]  # cycles per cRF (plus SF 0)
TFS = [3.75, 7.5, 15.0, 30.0]  # Hz (plus TF 0)
NORI = 6
KT = 11  # temporal filter taps
SIG_T = 2.0  # frames
DELAYS = 11  # 0..10
FIRST = 20  # frames of history a feature needs
LAST = 5  # frames ahead a feature reads (the temporal envelope is centred on the frame)
CENTRED = True


# ---------------------------------------------------------------- archive

def list_files():
    t = requests.get(BUCKET + "?list-type=2&prefix=mt-2/live/data/", timeout=60).text
    return sorted(k.split("/")[-1] for k in re.findall(r"<Key>(mt-2/live/data/[^<]+\.mat)</Key>", t))


def checksums():
    t = requests.get(BUCKET + "mt-2/live/checksums.md5", timeout=60).text
    return {ln.split()[1].split("/")[-1]: ln.split()[0] for ln in t.splitlines() if ln.strip()}


def _range(h, k):
    d = h["ranges"][k]
    if d.attrs.get("MATLAB_empty", 0):
        return np.zeros(0, int)
    return d[:].ravel().astype(int) - 1  # MATLAB indices are 1-based


def read_meta(name):
    """Everything but the frames."""
    with fsspec.open(DATA + name, block_size=2**20).open() as f, h5py.File(f, "r") as h:
        out = dict(name=name, cellid="".join(chr(c) for c in h["cellid"][:].ravel()),
                   psth=h["psths"][0].astype(np.float64), stim_shape=h["rawStims"].shape,
                   stim_dtype=str(h["rawStims"].dtype))
        for k in ["crange", "vrange", "nrange", "trange"]:
            out[k] = _range(h, k)
    return out


def list_keys(name):
    """Every group and dataset in one file, with shape, type and MATLAB attributes."""
    out = []
    with fsspec.open(DATA + name, block_size=2**20).open() as f, h5py.File(f, "r") as h:
        h.visititems(lambda k, o: out.append((k, getattr(o, "shape", None), str(getattr(o, "dtype", "group")),
                                              str(o.attrs.get("MATLAB_class", b"").decode()),
                                              int(o.attrs.get("MATLAB_empty", 0)))))
    return out


def load(name):
    """Metadata plus the frames, block-averaged to 32 x 32 as they stream."""
    with fsspec.open(DATA + name, block_size=8 * 2**20).open() as f, h5py.File(f, "r") as h:
        d = h["rawStims"]
        T = d.shape[0]
        stim = np.empty((T, NPIX, NPIX), np.float32)
        b = 128 // NPIX
        for s in range(0, T, 2000):
            x = d[s:s + 2000].astype(np.float32)
            stim[s:s + len(x)] = x.reshape(-1, NPIX, b, NPIX, b).mean((2, 4))
    m = read_meta(name)
    m["stim"] = stim
    return m


# ---------------------------------------------------------------- filter bank

def _grid(sf):
    s = 2.2 / (2 * sf)  # 2.2 sigma in cRF units, sigma = 1/(2 sf)
    n = max(1, int(np.floor(2.0 / s)))
    return (np.arange(n) - (n - 1) / 2) * s


def build_bank():
    """The full bank: spatial quadrature pairs at grid positions, temporal filters, and the
    descriptors of every complex and simple channel, with the pooling onto regressors."""
    xs = (np.arange(NPIX) - (NPIX - 1) / 2) / CRF  # cRF units
    X, Y = np.meshgrid(xs, xs)
    spat, spos = [], []  # each entry: (sf, ori index, cx, cy)
    for sf in SFS:
        sig = 1 / (2 * sf)
        g = _grid(sf)
        for cy in g:
            for cx in g:
                env = np.exp(-((X - cx) ** 2 + (Y - cy) ** 2) / (2 * sig**2))
                for o in range(NORI):
                    th = np.pi * o / NORI
                    ph = 2 * np.pi * sf * ((X - cx) * np.cos(th) + (Y - cy) * np.sin(th))
                    for fn in (np.cos, np.sin):
                        k = env * fn(ph)
                        k -= env * (k.sum() / env.sum())  # remove any DC leak
                        spat.append(k / np.linalg.norm(k))
                    spos.append((sf, o, cx, cy))
    blob = np.exp(-(X**2 + Y**2) / (2 * 0.5**2))
    spat.append(blob / np.linalg.norm(blob))
    S = np.stack([k.ravel() for k in spat], 1).astype(np.float32)  # pixels x filters

    tau = np.arange(KT)
    et = np.exp(-((tau - (KT - 1) / 2) ** 2) / (2 * SIG_T**2))
    temps = [et / np.linalg.norm(et)]
    for tf in TFS:
        for fn in (np.cos, np.sin):
            k = et * fn(2 * np.pi * tf * (tau - (KT - 1) / 2) / FPS)
            temps.append(k / np.linalg.norm(k))
    Tm = np.stack(temps, 0).astype(np.float32)  # 9 x KT

    return dict(S=S, Tm=Tm, spos=spos)


def bank_outputs(stim, bank, lumnorm, chunk=4000, ms=None):
    """Complex amplitudes (Eq. 4) and half-wave rectified simple outputs (Eq. 3) of the full
    bank, frames x channels, and the channel descriptors (sf, direction, tf, x, y)."""
    T = stim.shape[0]
    I = stim.reshape(T, -1).astype(np.float32)
    if lumnorm:  # Eqs. 10-12
        I = I - I.mean(1, keepdims=True)
        I = I / (np.sqrt((I**2).sum(1, keepdims=True)) + 1e-6)
    else:
        if ms is None:
            ms = (float(I.mean()), float(I.std()))
        I = (I - ms[0]) / ms[1]
    Tm = bank["Tm"]
    spos = np.array(bank["spos"])
    nsp = len(spos)
    cosi, sini = np.arange(nsp) * 2, np.arange(nsp) * 2 + 1
    th = 180.0 * spos[:, 1] / NORI
    lowsf = np.where(spos[:, 0] <= 2.0)[0]
    # descriptors, in the order the blocks are written below
    desc_c, desc_s = [], []
    blocks = [(0.0, 0)] + [(tf, s) for tf in TFS for s in (+1, -1)]
    for tf, s in blocks:
        d = th if s >= 0 else th + 180.0
        desc_c += [(spos[j, 0], d[j] % 360, tf, spos[j, 2], spos[j, 3]) for j in range(nsp)]
        for _ in range(4):
            desc_s += [(spos[j, 0], d[j] % 360, tf, spos[j, 2], spos[j, 3]) for j in lowsf]
    desc_c += [(0.0, 0.0, 0.0, 0.0, 0.0)] + [(0.0, 0.0, tf, 0.0, 0.0) for tf in TFS]
    desc_s += [(0.0, 0.0, 0.0, 0.0, 0.0)] * 2
    C = np.empty((T, len(desc_c)), np.float32)
    Sm = np.empty((T, len(desc_s)), np.float32)
    for c0 in range(0, T, chunk):
        a0 = max(0, c0 - (KT - 1))
        R = I[a0:c0 + chunk] @ bank["S"]
        pad = (KT - 1) - (c0 - a0)
        R = np.concatenate([np.zeros((pad, R.shape[1]), np.float32), R], 0)
        n = R.shape[0] - (KT - 1)
        conv = np.zeros((Tm.shape[0], n, R.shape[1]), np.float32)
        for tau in range(KT):  # out[t] = sum_tau k[tau] R[t - tau]
            seg = R[KT - 1 - tau:KT - 1 - tau + n]
            for q in range(Tm.shape[0]):
                conv[q] += Tm[q, tau] * seg
        cc, sc = 0, 0
        for tf, s in blocks:
            if tf == 0:
                L0, L90 = conv[0][:, cosi], conv[0][:, sini]
            else:
                ti = TFS.index(tf)
                Tc, Ts = 1 + 2 * ti, 2 + 2 * ti
                L0 = conv[Tc][:, cosi] - s * conv[Ts][:, sini]
                L90 = conv[Tc][:, sini] + s * conv[Ts][:, cosi]
            C[c0:c0 + n, cc:cc + nsp] = np.sqrt(L0**2 + L90**2)
            cc += nsp
            for p in (L0[:, lowsf], L90[:, lowsf], -L0[:, lowsf], -L90[:, lowsf]):
                Sm[c0:c0 + n, sc:sc + len(lowsf)] = np.maximum(p, 0)
                sc += len(lowsf)
        b = conv[0][:, -1]
        C[c0:c0 + n, cc] = np.abs(b)
        for ti in range(len(TFS)):
            C[c0:c0 + n, cc + 1 + ti] = np.sqrt(conv[1 + 2 * ti][:, -1] ** 2 + conv[2 + 2 * ti][:, -1] ** 2)
        Sm[c0:c0 + n, sc] = np.maximum(b, 0)
        Sm[c0:c0 + n, sc + 1] = np.maximum(-b, 0)
    if CENTRED:  # centre the temporal envelope on frame t: output t reads frames t-5..t+5
        h = (KT - 1) // 2
        C[:-h] = C[h:]
        C[-h:] = 0
        Sm[:-h] = Sm[h:]
        Sm[-h:] = 0
    return C, Sm, np.array(desc_c), np.array(desc_s), ms


def pooling(desc_c, desc_s, level="2x2"):
    """Weights that pool full-bank channels onto regressors (the spatial constraint, D).
    Returns the matrix for complex and simple channels and the regressor descriptors
    (sf, direction, tf, region x, region y, is_simple). Complex channels of one SF,
    direction and TF are summed with Gaussian weights onto a grid of regions spanning the
    2 cRF patch.
    level "2x2" (every model): 3 and 6 cycles per cRF onto 2 x 2 regions (SD 0.5 cRF), 0.75
    and 1.5 summed over their positions; simple cells at 0.75 cycles per cRF and SF 0 (763
    regressors). "3x3", a reading of the main model that measures what the pooling costs: 3
    and 6 onto 3 x 3 regions (SD 1/3 cRF) and 1.5 at each of its 4 grid positions (1465).
    "fine", the same on 4 x 4 regions (SD 0.25 cRF) and with every simple channel of the
    bank, up to 2 cycles per cRF, each at its position (3085)."""
    ng = {"2x2": 2, "3x3": 3, "fine": 4}[level]
    gc = (np.arange(ng) - (ng - 1) / 2) * (2.0 / ng)
    gr = [(x, y) for y in gc for x in gc]
    g15 = _grid(1.5)
    regions = {3.0: (gr, 1.0 / ng), 6.0: (gr, 1.0 / ng),
               1.5: ([(x, y) for y in g15 for x in g15], 0.0) if level != "2x2" else ([(0.0, 0.0)], None),
               0.75: ([(0.0, 0.0)], None), 0.0: ([(0.0, 0.0)], None)}
    rdesc = []
    keys_c = [tuple(d[:3]) for d in desc_c]
    uniq = sorted(set(keys_c), key=lambda k: (k[0], k[1], k[2]))
    Pc = []
    for k in uniq:
        idx = [i for i, kk in enumerate(keys_c) if kk == k]
        cen, sdr = regions[k[0]]
        for (rx, ry) in cen:
            w = np.zeros(len(desc_c))
            if sdr is None:
                w[idx] = 1.0
            else:
                d2 = (desc_c[idx, 3] - rx) ** 2 + (desc_c[idx, 4] - ry) ** 2
                w[idx] = (d2 < 1e-9) if sdr == 0 else np.exp(-d2 / (2 * sdr**2))
            Pc.append(w / w.sum())
            rdesc.append((*k, rx, ry, 0))
    # simple cells, phases kept apart
    Ps = []
    sel = [i for i, d in enumerate(desc_s) if level == "fine" or d[0] in (0.0, 0.75)]
    for i in sel:
        w = np.zeros(len(desc_s))
        w[i] = 1.0
        Ps.append(w)
        rdesc.append((*desc_s[i][:3], *(desc_s[i][3:5] if level == "fine" else (0.0, 0.0)), 1))
    nc, ns = len(Pc), len(Ps)
    Pc = np.array(Pc).T.astype(np.float32)  # full complex x regressors
    Ps = np.array(Ps).T.astype(np.float32)
    return Pc, Ps, np.array(rdesc), nc, ns


def features(C, Sm, train_rows, Pc, Ps, alpha, divisive, sigma_frac=0.01, norm=None, chunk=4000):
    """Regressors for one model: static nonlinearity (Eq. 13), divisive normalization
    (Eq. 14) by all full-bank channels scaled to unit SD over the training frames, then
    pooling. Returns frames x regressors and the normalization constants (unit SDs and
    sigma), which `norm` reuses for other stimuli."""
    T = C.shape[0]

    def nl(x):
        return x**alpha if alpha != 1 else x

    if divisive and norm is None:
        s1c = np.zeros(C.shape[1]); s2c = np.zeros(C.shape[1])
        s1s = np.zeros(Sm.shape[1]); s2s = np.zeros(Sm.shape[1])
        for c0 in range(0, len(train_rows), chunk):
            r = train_rows[c0:c0 + chunk]
            a, b = nl(C[r]).astype(np.float64), nl(Sm[r]).astype(np.float64)
            s1c += a.sum(0); s2c += (a**2).sum(0); s1s += b.sum(0); s2s += (b**2).sum(0)
        n = len(train_rows)
        sc = np.sqrt(np.maximum(s2c / n - (s1c / n) ** 2, 0)) + 1e-9
        ss = np.sqrt(np.maximum(s2s / n - (s1s / n) ** 2, 0)) + 1e-9
        mp = (s1c / sc).sum() / n + (s1s / ss).sum() / n
        norm = dict(sc=sc.astype(np.float32), ss=ss.astype(np.float32), sigma=sigma_frac * mp)
    F = np.empty((T, Pc.shape[1] + Ps.shape[1]), np.float32)
    for c0 in range(0, T, chunk):
        a, b = nl(C[c0:c0 + chunk]), nl(Sm[c0:c0 + chunk])
        f = np.concatenate([a @ Pc, b @ Ps], 1)
        if divisive:
            f /= (a @ (1 / norm["sc"]) + b @ (1 / norm["ss"]) + norm["sigma"])[:, None]
        F[c0:c0 + chunk] = f
    return F, norm


# ---------------------------------------------------------------- regression

OFFSETS = (0, 3, 6)


def shift_rows(F, s):
    """Move the delay window s frames earlier: row t of the result holds the features of
    frame t + s, so delays 0 to 10 become -s to 10 - s (A: the alignment of the files)."""
    if s == 0:
        return F
    out = np.zeros_like(F)
    out[:-s] = F[s:]
    return out


def rows(m):
    """Training rows (frames in crange with a response) and the validation sets."""
    T = len(m["psth"])
    cr = m["crange"]
    tr = cr[(cr >= FIRST) & ~np.isnan(m["psth"][cr])]
    v = m["vrange"]
    nat = m["nrange"]
    sets = {}
    if len(nat):
        me = np.setdiff1d(v, nat)
        sets["natural"] = nat
        sets["enhanced"] = me
    else:
        sets["enhanced"] = v
    return tr, sets


def zscore_stats(F, tr):
    mu = F[tr].mean(0)
    sd = F[tr].std(0) + 1e-9
    return mu, sd


def lagged(F, rws, delays=DELAYS):
    return np.concatenate([F[rws - d] for d in range(delays)], 1)


class Lagged:
    """The lagged design of some rows, read one column at a time, so that it is never held
    whole in memory (S, numerical)."""

    def __init__(self, F, rws, delays=DELAYS):
        self.F, self.rws, self.P, self.D = F, rws, F.shape[1], delays

    def __getitem__(self, key):
        _, j = key
        d, i = divmod(j, self.P)
        return self.F[self.rws - d, i]

    def tdot(self, y):
        """X'y, delay-major."""
        return np.concatenate([self.F[self.rws - d].T @ y for d in range(self.D)])


class Fold:
    """The training-set Gram matrix of the lagged design for one held-out block, kept as
    lag cross-products C_k[i, j] = sum_t F[t, i] F[t - k, j] summed over the other blocks.
    G[(a, i), (b, j)] is C_{b-a}[i, j] for b >= a and C_{a-b}[j, i] otherwise; its rows
    are built when boosting asks for them."""

    def __init__(self, tot, held, P, delays):
        self.tot, self.held, self.P, self.D = tot, held, P, delays  # C = tot - held, by row
        self.cache = {}

    def row(self, r):
        if r not in self.cache:
            a, i = divmod(r, self.P)
            self.cache[r] = np.concatenate(
                [self.tot[b - a][i] - self.held[b - a][i] if b >= a else
                 self.tot[a - b][:, i] - self.held[a - b][:, i] for b in range(self.D)])
        return self.cache[r]


def block_stats(F, blocks, delays=DELAYS):
    """Lag cross-products and lagged sums of each block."""
    out = []
    for b in blocks:
        Fb = F[b]
        out.append(np.stack([Fb.T @ F[b - k] for k in range(delays)]))
    return out


def boost(G, c, Xh, yh, eps, patience=50, maxit=20000, active=None):
    """Coordinate gradient boosting (Eqs. 6-9) with early stopping on a held-out set.
    G: training Gram (a Fold), c: X'y (centered), Xh: the held-out design (a `Lagged`),
    yh: the centered held-out response. `active` restricts the channels that may be
    chosen."""
    P = len(c)
    w = np.zeros(P, np.float64)
    g = c.astype(np.float64).copy()  # = X'(y - Xw), minus the gradient of E/2
    pred = np.zeros(len(yh))
    best, bestw, bad = np.mean(yh**2), w.copy(), 0
    mask = None
    if active is not None:
        mask = np.full(P, -np.inf)
        mask[active] = 0.0
    it = 0
    for it in range(maxit):
        a = np.abs(g) if mask is None else np.abs(g) + mask
        j = int(np.argmax(a))
        s = eps * np.sign(g[j])
        w[j] += s
        g -= s * G.row(j)
        pred += s * Xh[:, j]
        err = np.mean((yh - pred) ** 2)
        if err < best:
            best, bestw, bad = err, w.copy(), 0
        else:
            bad += 1
            if bad >= patience:
                break
    return bestw, it + 1, best


def make_blocks(tr, nfold=5, rng=None):
    """Held-out blocks: five contiguous parts of the training rows (reading (a)), or, with a
    generator, five random partitions of the frames (reading (b))."""
    if rng is None:
        return np.array_split(tr, nfold)
    perm = rng.permutation(len(tr))
    return [np.sort(tr[perm[i::nfold]]) for i in range(nfold)]


def fit_neuron(F, ys, blocks, delays=DELAYS, stats=None, active=None, patience=50, lazy=False):
    """Fit one model to one or several responses on the same features.
    F: frames x regressors (z-scored), ys: list of responses per frame, blocks: held-out
    blocks of training rows. Returns, per response, the five-fold averaged weights
    (delays*P, delay-major), the intercept and the iterations per fold. lazy: read the
    held-out design a column at a time (`Lagged`), for the finer poolings, whose lagged
    design would not fit in memory; its sums are then taken in single precision, so the
    results differ from the default in the last digits."""
    nfold = len(blocks)
    P = F.shape[1]
    if stats is None:
        stats = block_stats(F, blocks, delays)
    tot = sum(stats)
    folds = [Fold(tot, stats[k], P, delays) for k in range(nfold)]
    if lazy:
        Xhs = [Lagged(F, blocks[k], delays) for k in range(nfold)]
        XS = [Xh.tdot(np.ones(len(Xh.rws), np.float32)).astype(np.float64) for Xh in Xhs]
    else:
        Xhs = [lagged(F, blocks[k], delays) for k in range(nfold)]
        XS = [Xh.sum(0, dtype=np.float64) for Xh in Xhs]
    res = []
    for yy in ys:
        if lazy:
            XY = [Xhs[k].tdot(yy[blocks[k]].astype(np.float32)).astype(np.float64) for k in range(nfold)]
        else:
            XY = [(Xhs[k].T @ yy[blocks[k]].astype(np.float32)).astype(np.float64) for k in range(nfold)]
        W, b0, its, herr = [], [], [], 0.0
        for k in range(nfold):
            others = [i for i in range(nfold) if i != k]
            n = sum(len(blocks[i]) for i in others)
            mu = sum(yy[blocks[i]].sum() for i in others) / n
            c = sum(XY[i] for i in others) - mu * sum(XS[i] for i in others)
            sdy = np.sqrt(sum(((yy[blocks[i]] - mu) ** 2).sum() for i in others) / n)
            w, nit, e = boost(folds[k], c, Xhs[k], yy[blocks[k]] - mu, 0.01 * sdy, patience=patience, active=active)
            herr += e * len(blocks[k])
            W.append(w)
            b0.append(mu)
            its.append(nit)
        res.append((np.mean(W, 0), float(np.mean(b0)), its, herr / sum(len(b) for b in blocks)))
    return res, stats


def predict(F, rws, w, b0, delays=DELAYS):
    return lagged(F, rws, delays) @ w.astype(np.float32) + b0


def val_corr(F, m, w, b0, smooth_sd=1.0, delays=DELAYS):
    """Correlation of prediction and smoothed mean response on each validation set."""
    _, sets = rows(m)
    out = {}
    for k, v in sets.items():
        obs = gaussian_filter1d(m["psth"][v], smooth_sd) if smooth_sd > 0 else m["psth"][v]
        obs, v = obs[FIRST:-LAST - max(OFFSETS)], v[FIRST:-LAST - max(OFFSETS)]
        p = predict(F, v, w, b0, delays)
        out[k] = pearsonr(p, obs)[0]
    return out


# ---------------------------------------------------------------- simulated neurons

def model_rate(F, rws, w, delays=DELAYS):
    return lagged(F, rws, delays) @ w.astype(np.float32)


def null_response(F, tr, mean_count, P, rng, rate_reading, delay_reading, delays=DELAYS):
    """A null model neuron (P, "Null hypotheses test for on-plane ratio"): weights from a
    normal distribution (mean 0, SD 1) on the compressive and divisive regressors, at every
    delay (C, reading (a)) or at one delay drawn at random (reading (b)); the rate made
    non-negative by rectification (reading (a)) or by an offset (reading (b)) and scaled to
    the recorded neuron's mean count; Poisson noise (P)."""
    w = np.zeros((delays, P))
    if delay_reading == "a":
        w[:] = rng.normal(0, 1, (delays, P))
    else:
        w[rng.integers(delays)] = rng.normal(0, 1, P)
    r = model_rate(F, tr, w.ravel(), delays)
    r = np.maximum(r, 0) if rate_reading == "a" else r - r.min()
    r = r * (mean_count / r.mean())
    y = np.full(len(F), np.nan)
    y[tr] = rng.poisson(r)
    return y


def sim_weights(rd, kind, rng, delays=DELAYS, delay=6):
    """The three simulated neurons of Figure 8 (excitatory weights only, on complex
    regressors): (A) a narrow band of SF and TF, (B) four directions at one SF and TF,
    (C) many channels at random direction and frequency. The paper gives no counts; these
    are standard choices (one SF and TF band, delay 6 frames)."""
    P = len(rd)
    w = np.zeros((delays, P))
    cx = rd[:, 5] == 0
    if kind == "A":
        sel = cx & (rd[:, 0] == 3.0) & (rd[:, 2] == 7.5) & np.isin(rd[:, 1], [0.0, 30.0, 330.0])
    elif kind == "B":
        sel = cx & (rd[:, 0] == 1.5) & (rd[:, 2] == 7.5) & np.isin(rd[:, 1], [0.0, 90.0, 180.0, 270.0])
    else:
        sel = np.zeros(P, bool)
        sel[rng.choice(np.where(cx)[0], 60, replace=False)] = True
    w[delay, sel] = rng.uniform(0.5, 1.0, sel.sum())
    return w.ravel()


# ---------------------------------------------------------------- gratings and plaids

def grating_movies(sf, tf, ms, sep_list=(120, 90), nfr=30):
    """Drifting gratings at 24 directions (15 degree steps, so that the component prediction
    of a 90 degree plaid can be read) and plaids at 12 directions (30 degree steps, C), each
    component at the RMS contrast of the training movie (S)."""
    xs = (np.arange(NPIX) - (NPIX - 1) / 2) / CRF
    X, Y = np.meshgrid(xs, xs)
    t = np.arange(nfr)[:, None, None] / FPS
    amp = np.sqrt(2) * ms[1]

    def g(d):
        th = np.deg2rad(d)
        return amp * np.cos(2 * np.pi * (sf * (X * np.cos(th) + Y * np.sin(th)) - tf * t))

    movies = [ms[0] + g(d) for d in np.arange(24) * 15.0]
    for sep in sep_list:
        for d in np.arange(12) * 30.0:
            movies.append(ms[0] + g(d - sep / 2) + g(d + sep / 2))
    return np.concatenate(movies, 0).astype(np.float32), nfr


def pattern_index(g24, plaid12, sep):
    """Pattern index of Smith et al. (2005): Fisher-transformed partial correlations of the
    plaid tuning (12 directions) with the pattern prediction (the grating tuning at the same
    directions) and the component prediction (the sum of the grating responses at
    +-sep/2), Zp - Zc, with 12 - 3 degrees of freedom."""
    idx = np.arange(12) * 2
    k = int(round(sep / 2 / 15))
    pat = g24[idx]
    comp = g24[(idx + k) % 24] + g24[(idx - k) % 24]
    cl = lambda r: np.clip(r, -0.999999, 0.999999)  # a pure pattern or component cell stays finite
    rp = cl(np.corrcoef(plaid12, pat)[0, 1])
    rc = cl(np.corrcoef(plaid12, comp)[0, 1])
    rpc = cl(np.corrcoef(pat, comp)[0, 1])
    Rp = (rp - rc * rpc) / np.sqrt((1 - rc**2) * (1 - rpc**2))
    Rc = (rc - rp * rpc) / np.sqrt((1 - rp**2) * (1 - rpc**2))
    z = lambda r: np.arctanh(np.clip(r, -0.999999, 0.999999)) / np.sqrt(1 / (12 - 3))
    return z(Rp) - z(Rc)


def noisy_tuning(resp, n_rep, rng, frames=83):
    """Mean spike count over n_rep presentations of frames frames each, Poisson at the
    model's rate per frame (rectified): the tuning curve an experiment would measure (A:
    1 s presentations; the paper does not say whether its simulated responses had noise)."""
    lam = np.maximum(resp, 0) * frames
    return rng.poisson(lam, (n_rep, len(lam))).mean(0)


# ---------------------------------------------------------------- one neuron

MODELS = [(lum, alpha, div) for lum in (False, True) for div in (False, True) for alpha in (1.0, 0.5, 2.0)]
MAIN = (False, 0.5, True)


def process_neuron(name, null_specs=(), sim=False, seed=0, threads=2):
    """All fits for one neuron. null_specs: list of (id, rate_reading, delay_reading)
    null model neurons to simulate on this neuron's movies."""
    from threadpoolctl import threadpool_limits
    with threadpool_limits(threads):
        return _process(name, null_specs, sim, seed)


def _process(name, null_specs, sim, seed):
    t0 = time.time()
    m = load(name)
    tload = time.time() - t0
    tr, sets = rows(m)
    y = m["psth"]
    bank = build_bank()
    blocks = make_blocks(tr)
    out = dict(name=name, cellid=m["cellid"], n_frames=len(y), n_train=len(tr),
               n_crange=len(m["crange"]), sets={k: len(v) for k, v in sets.items()},
               nan_train=int(np.isnan(y[m["crange"]]).sum()), mean_count=float(np.nanmean(y[tr])),
               fits={}, t_load=tload)
    # motion content of each part of the movie: mean absolute frame difference over mean contrast
    s = m["stim"]
    dif = np.abs(np.diff(s, axis=0)).mean((1, 2))
    con = s.std((1, 2))
    parts = {"train": tr, **sets}
    out["motion"] = {k: float(dif[v[1:] - 1].mean() / con[v[1:]].mean()) for k, v in parts.items()}
    out["contrast"] = {k: float(con[v].mean()) for k, v in parts.items()}
    out["stim_range"] = (float(s.min()), float(s.max()))
    out["psth"] = y.astype(np.float32)
    # repeats: per frame, the smallest n that makes n times the mean count a whole number; the
    # largest over a validation set is a lower bound on its number of repeats
    rep = {}
    for k, v in sets.items():
        den = [next((n for n in range(1, 41) if abs(x * n - round(x * n)) < 1e-3), 0)
               for x in np.unique(y[v])]
        rep[k] = int(max(den))
    out["repeats"] = rep
    # the same with a tolerance of 1e-6 and denominators up to 100: the share of values whose
    # denominator is found, and the largest
    strict = {}
    for k, v in sets.items():
        u = np.unique(y[v][~np.isnan(y[v])])
        den = np.array([next((n for n in range(1, 101) if abs(x * n - round(x * n)) < 1e-6), 0) for x in u])
        strict[k] = (int(den.max()), float(np.mean(den > 0)))
    out["repeats_strict"] = strict
    # validation sets: contiguous frames, and frames without a response
    out["trange_len"] = len(m["trange"])
    out["val_check"] = {k: dict(contiguous=bool(np.all(np.diff(v) == 1)), n_nan=int(np.isnan(y[v]).sum()))
                        for k, v in sets.items()}
    vals = y[tr]
    out["train_denominators"] = sorted({n for x in np.unique(vals) for n in range(1, 41)
                                        if abs(x * n - round(x * n)) < 1e-3 and
                                        all(abs(x * q - round(x * q)) >= 1e-3 for q in range(1, n))})
    for lum in (False, True):
        C, Sm, dc, ds, ms = bank_outputs(s, bank, lum)
        Pc, Ps, rd, nc, ns = pooling(dc, ds)
        out["rd"] = rd
        if not lum:
            out["ms"] = ms
            # offset of the delay window, chosen by the held-out error of the main model on
            # the training data alone
            F, norm0 = features(C, Sm, tr, Pc, Ps, MAIN[1], MAIN[2])
            mu, sd = zscore_stats(F, tr)
            F = (F - mu) / sd
            off, kept = {}, {}
            for o in OFFSETS:
                Fo = shift_rows(F, o)
                res, st = fit_neuron(Fo, [y], blocks)
                off[o] = (res[0][3], val_corr(Fo, m, res[0][0], res[0][1]))
                kept[o] = (Fo, mu, sd, res, st, norm0)
            del F
            out["offsets"] = off
            out["offset"] = min(off, key=lambda o: off[o][0])
            kept = kept[out["offset"]]  # the main model's fit, reused below
        for (l2, alpha, div) in MODELS:
            if l2 != lum:
                continue
            if (lum, alpha, div) == MAIN:
                F, mu, sd, res, st, norm = kept
                kept = None
            else:
                F, norm = features(C, Sm, tr, Pc, Ps, alpha, div)
                mu, sd = zscore_stats(F, tr)
                F = shift_rows((F - mu) / sd, out["offset"])
                res, st = fit_neuron(F, [y], blocks)
            w, b0, its, herr = res[0]
            key = (lum, alpha, div)
            fit = dict(r=val_corr(F, m, w, b0), its=its, herr=herr)
            if key == MAIN:
                fit.update(w=w.astype(np.float32), b0=b0, mu=mu, sd=sd)
                # clock check: prediction against the validation response shifted in time
                vv = sets["enhanced"]
                pv = predict(F, vv[FIRST:], w, b0)
                ob = gaussian_filter1d(y[vv], 1.0)
                shifts = np.arange(-30, 31)
                fit["shift_r"] = (shifts, np.array([
                    np.corrcoef(pv[30:-30], ob[FIRST + 30 + k:len(vv) - 30 + k])[0, 1] for k in shifts]))
                fit["r_smooth_b"] = val_corr(F, m, w, b0, smooth_sd=12 / 2.3548 / 12)
                # early stopping with a patience of 500 steps in place of 50
                r2, _ = fit_neuron(F, [y], blocks, stats=st, patience=500)
                fit["patience500"] = dict(r=val_corr(F, m, r2[0][0], r2[0][1]), its=r2[0][2])
                P = F.shape[1]
                dl = np.repeat(np.arange(DELAYS), P)
                isc = np.tile(rd[:, 5] == 0, DELAYS)
                for nm, act in [("delays_b", np.where(dl >= 1)[0]), ("complex_only", np.where(isc)[0]),
                                ("simple_only", np.where(~isc)[0])]:
                    r2, _ = fit_neuron(F, [y], blocks, stats=st, active=act)
                    fit[nm] = dict(r=val_corr(F, m, r2[0][0], r2[0][1]), w=r2[0][0].astype(np.float32))
                # held-out folds as random partitions of frames (reading (b)); the Gram from lag
                # cross-products is an approximation here, as a shifted random subset differs
                r2, _ = fit_neuron(F, [y], make_blocks(tr, rng=np.random.default_rng(seed)))
                fit["folds_b"] = dict(r=val_corr(F, m, r2[0][0], r2[0][1]))
                # null model neurons on this neuron's movies
                rng = np.random.default_rng(seed + 1)
                nulls = []
                for (nid, ra, da) in null_specs:
                    yn = null_response(F, tr, out["mean_count"], P, rng, ra, da)
                    rn, _ = fit_neuron(F, [yn], blocks, stats=st)
                    nulls.append(dict(id=nid, rate=ra, delay=da, w=rn[0][0].astype(np.float32)))
                out["nulls"] = nulls
                if sim:
                    rng = np.random.default_rng(seed + 2)
                    sims = []
                    for kind in "ABC":
                        wt = sim_weights(rd, kind, rng)
                        rate = np.maximum(model_rate(F, tr, wt), 0)
                        rate = rate * (out["mean_count"] / rate.mean())
                        for noise in ("a", "b"):
                            ys = np.full(len(F), np.nan)
                            ys[tr] = rng.poisson(rate) if noise == "a" else rate
                            rs, _ = fit_neuron(F, [ys], blocks, stats=st)
                            sims.append(dict(kind=kind, noise=noise, w_true=wt.astype(np.float32),
                                             w=rs[0][0].astype(np.float32)))
                    out["sims"] = sims
                # gratings and plaids at every SF and TF pair of the bank
                wsum = w.reshape(DELAYS, -1).sum(0)
                pr = {}
                for sf in SFS:
                    for tf in TFS:
                        mov, nfr = grating_movies(sf, tf, ms)
                        Cg, Sg, *_ = bank_outputs(mov, bank, False, ms=ms)
                        Fg, _ = features(Cg, Sg, None, Pc, Ps, alpha, div, norm=norm)
                        Fg = (Fg - mu) / sd  # steady state: the offset does not matter
                        resp = Fg.reshape(-1, nfr, Fg.shape[1])[:, 10:nfr - 6].mean(1) @ wsum + b0
                        pr[(sf, tf)] = dict(grating=resp[:24], plaid120=resp[24:36], plaid90=resp[36:48])
                fit["plaid"] = pr
                fit["norm_sigma"] = norm["sigma"]
            out["fits"][key] = fit
            if key == MAIN:
                # sigma chosen on the held-out data (reading (a)) between 0.01 and 1 times
                # the mean pooled response; 0.01 is the fit above
                sig = {0.01: (herr, fit["r"])}
                for sfrac in (1.0,):
                    F2, _ = features(C, Sm, tr, Pc, Ps, alpha, div, sigma_frac=sfrac)
                    mu2, sd2 = zscore_stats(F2, tr)
                    F2 = shift_rows((F2 - mu2) / sd2, out["offset"])
                    r2, _ = fit_neuron(F2, [y], blocks)
                    sig[sfrac] = (r2[0][3], val_corr(F2, m, r2[0][0], r2[0][1]))
                    del F2
                out["sigma_a"] = sig
            del F
        del C, Sm
    out["t_total"] = time.time() - t0
    return out


def pooled_fit(C, Sm, dc, ds, tr, m, blocks, offset, level):
    """The compressive and divisive model with a finer pooling (`pooling(level=...)`), on
    the delay offset chosen with the 2 x 2 pooling, to measure what the pooling costs; also
    with complex or simple regressors only."""
    Pc, Ps, rd, nc, ns = pooling(dc, ds, level)
    F, _ = features(C, Sm, tr, Pc, Ps, MAIN[1], MAIN[2])
    mu, sd = zscore_stats(F, tr)
    F = shift_rows((F - mu) / sd, offset)
    res, st = fit_neuron(F, [m["psth"]], blocks, lazy=True)
    w, b0, its, _ = res[0]
    out = dict(n_complex=nc, n_simple=ns, r=val_corr(F, m, w, b0), its=its)
    isc = np.tile(rd[:, 5] == 0, DELAYS)
    for nm, act in [("complex_only", np.where(isc)[0]), ("simple_only", np.where(~isc)[0])]:
        r2, _ = fit_neuron(F, [m["psth"]], blocks, stats=st, active=act, lazy=True)
        out[nm] = val_corr(F, m, r2[0][0], r2[0][1])
    return out


def pooling_neuron(name, fine=False, threads=2):
    """The main model of one neuron under the finer pooling (finer_pooling.ipynb). The delay
    offset is chosen as in `_process`, by the held-out error of the 2 x 2 model on the
    training data, so it is the same; the 2 x 2 fit at that offset is returned with it."""
    from threadpoolctl import threadpool_limits
    with threadpool_limits(threads):
        t0 = time.time()
        m = load(name)
        tr, sets = rows(m)
        y = m["psth"]
        blocks = make_blocks(tr)
        C, Sm, dc, ds, _ = bank_outputs(m["stim"], build_bank(), False)
        Pc, Ps, rd, nc, ns = pooling(dc, ds)
        F, _ = features(C, Sm, tr, Pc, Ps, MAIN[1], MAIN[2])
        mu, sd = zscore_stats(F, tr)
        F = (F - mu) / sd
        off = {}
        for o in OFFSETS:
            Fo = shift_rows(F, o)
            res, _ = fit_neuron(Fo, [y], blocks, lazy=True)
            off[o] = (res[0][3], val_corr(Fo, m, res[0][0], res[0][1]))
        del F, Fo
        o = min(off, key=lambda k: off[k][0])
        out = dict(name=name, cellid=m["cellid"], sets={k: len(v) for k, v in sets.items()}, offset=o,
                   r2x2=off[o][1], p3x3=pooled_fit(C, Sm, dc, ds, tr, m, blocks, o, "3x3"))
        if fine:
            out["fine"] = pooled_fit(C, Sm, dc, ds, tr, m, blocks, o, "fine")
        out["t_total"] = time.time() - t0
    return out


# ---------------------------------------------------------------- spectral receptive fields

TH0 = np.arange(0, 360, 5.0)  # plane azimuths, degrees (S: grid)
SPEEDS = np.r_[0.0, np.geomspace(0.5, 100, 40)]  # plane elevations as speeds, cRF/s (S: grid)


def list_sizes():
    t = requests.get(BUCKET + "?list-type=2&prefix=mt-2/live/data/", timeout=60).text
    return {k.split("/")[-1]: int(s) for k, s in
            re.findall(r"<Key>(mt-2/live/data/[^<]+\.mat)</Key>.*?<Size>(\d+)</Size>", t)}


def regressor_amplitude(rd):
    """Peak spectral amplitude of the unit-norm spatial and temporal filters behind each
    regressor, for the reading that weights the spectral receptive field by amplitude."""
    bank = build_bank()
    S, Tm = bank["S"], bank["Tm"]
    amp_s = {}
    for j, (sf, o, cx, cy) in enumerate(bank["spos"]):
        if sf not in amp_s:
            k = S[:, 2 * j] + 1j * S[:, 2 * j + 1]
            amp_s[sf] = np.abs(np.fft.fft2(k.reshape(NPIX, NPIX))).max()
    amp_s[0.0] = np.abs(np.fft.fft2(S[:, -1].reshape(NPIX, NPIX))).max()
    amp_t = {0.0: np.abs(np.fft.fft(Tm[0], 256)).max()}
    for i, tf in enumerate(TFS):
        amp_t[tf] = np.abs(np.fft.fft(Tm[1 + 2 * i] + 1j * Tm[2 + 2 * i], 256)).max()
    return np.array([amp_s[r[0]] * amp_t[r[2]] for r in rd])


def split_weights(w, sd=None, amp=None, quantity="a", sign="a"):
    """Excitatory and suppressive weight per regressor. quantity (a): the fitted weights;
    (b): weights on the unscaled regressors times the filter's spectral amplitude. sign (a):
    split per weight at each delay; (b): after summing over delays."""
    W = w.reshape(DELAYS, -1).astype(np.float64)
    if quantity == "b":
        W = W / sd[None, :] * amp[None, :]
    if sign == "a":
        return np.clip(W, 0, None).sum(0), np.clip(-W, 0, None).sum(0)
    s = W.sum(0)
    return np.clip(s, 0, None), np.clip(-s, 0, None)


def plane_geometry(rd):
    """For each regressor and plane (azimuth x speed): whether the regressor's temporal
    frequency is within 1 octave or 5 Hz of the plane, whichever is larger (P, "Optimal
    velocity plane"), and its side of the plane's azimuth (+1, -1; 0 for static and SF 0)."""
    sf, d, tf = rd[:, 0], rd[:, 1], rd[:, 2]
    th, v = np.meshgrid(TH0, SPEEDS, indexing="ij")
    th, v = th.ravel(), v.ravel()
    ang = np.deg2rad(d[:, None] - th[None, :])
    tfp = v[None, :] * sf[:, None] * np.cos(ang)
    T = tf[:, None]
    near = (np.abs(T - tfp) <= 5) | ((tfp > 0) & (T >= tfp / 2) & (T <= 2 * tfp))
    side = np.sign(np.sin(ang)) * ((tf > 0) & (sf > 0))[:, None]
    return near, side, th, v


def optimal_plane(E, near, side, balance="a"):
    """Index of the optimal plane. Coverage: excitatory weight near the plane. Symmetry: the
    negative of the absolute difference of the weight on the two sides of its azimuth (C).
    balance (a): coverage, symmetry breaking ties; (b): both over the total, summed."""
    cov = E @ near
    sym = -np.abs(E @ side)
    tot = E.sum() + 1e-12
    if balance == "a":
        cand = np.where(cov >= cov.max() * (1 - 1e-9))[0]
        return cand[np.argmax(sym[cand])]
    return int(np.argmax(cov / tot + sym / tot))


def on_plane_ratio(E, near_col):
    return float((E * near_col).sum() / (E.sum() + 1e-12))


def hv_ratio(E, rd, th0, near_col, reading="a"):
    """Horizontal over vertical excitatory weight in the optimal plane, with quadrant borders
    at 45 degrees (C). A regressor's place in the plane is read from its spatial frequency
    vector: along the optimal direction (vertical) or across it (horizontal). reading (a):
    regressors near the plane; (b): all excitatory weight projected onto the plane."""
    sel = rd[:, 0] > 0
    if reading == "a":
        sel = sel & near_col
    ang = np.deg2rad(rd[:, 1] - th0)
    horiz = np.abs(np.sin(ang)) > np.abs(np.cos(ang))
    h = (E * (sel & horiz)).sum()
    v = (E * (sel & ~horiz)).sum()
    return float(h / v) if v > 0 else np.inf
