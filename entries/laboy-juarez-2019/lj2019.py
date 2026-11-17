"""Loading and measures for CRCNS ssc-9 (Laboy-Juarez, Langberg, Ahn & Feldman 2019).

The data set is one zip, ``ssc-9/live/data.zip``, in the public S3 bucket ``crcnsarchive``.
It is opened in place over range requests (fsspec and zipfile, docs/archives.md, "CRCNS"); each
MATLAB file is read into memory, reduced to spike counts per trial, and dropped.

Where each parameter comes from:

- Response window, 0 to 125 ms after the onset of the first deflected whisker: claims file,
  "Common method" (Methods, "Analysis of neuronal data" and "dt smoothing").
- Whisker labels: the data descriptor (paper/ssc-9.data-description.txt and its PDF figure).
  Experiments 1 and 2 use the grid 1 4 7 / 2 5 8 / 3 6 9 (columns caudal to rostral, rows
  dorsal to ventral), CW = 5; experiment 3 uses 6 7 8 / 3 4 5 / 1 2 9, CW = 4.
- dt sign: negative dt means the SW leads the CW (Fig. 1c legend, "negative dt (SW precedes
  CW)"), so dt = t_SW - t_CW.
- Experiment 3 epochs have no deflection times. DeltaT is the time of the second whisker in
  DeflectedWs minus that of the first, and epoch time 0 is the first deflection in time; this is
  shown from the latency of the CW response in the notebook's data check (a finding, the data
  descriptor does not say it).
- Poisson likelihood ratio test of responsiveness across the nine whiskers and sham: Methods,
  "Analysis of neuronal data".
- Lifetime sparseness: claims file header, Vinje and Gallant (ref. 28).
- dt smoothing: Methods, "dt smoothing" (claims file, common method). Kernels with SD 0.5 to 30 ms
  in 0.2 ms steps, tenfold cross-validation repeated 50 times.
- Combination selectivity shuffle: Methods, "Combination selectivity" (5000 shuffles,
  Mahalanobis distance, FDR control at 0.05).
- Decoders: Methods, "Neural decoders".
"""

import hashlib
import io
import zipfile

import fsspec
import numpy as np
import pandas as pd
import scipy.io as sio
from scipy import stats

DATASET = "ssc-9"
# CRCNS data sets are not versioned (docs/archives.md); the file read is pinned by its MD5 sum
# from the data set's checksums.md5.
VERSION = "unversioned"
DATA_MD5 = "2e7a774017619e76c46db85722587be3"
URL = "https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-9/live/data.zip"
WINDOW = 125.0  # ms, Methods, "Analysis of neuronal data"

# Positions (row, column) of each label: row 0 dorsal to 2 ventral, column 0 caudal to 2 rostral.
POS12 = {1: (0, 0), 2: (1, 0), 3: (2, 0), 4: (0, 1), 5: (1, 1), 6: (2, 1), 7: (0, 2), 8: (1, 2), 9: (2, 2)}
POS3 = {6: (0, 0), 3: (1, 0), 1: (2, 0), 7: (0, 1), 4: (1, 1), 2: (2, 1), 8: (0, 2), 5: (1, 2), 9: (2, 2)}
CW12, CW3 = 5, 4
# Face position names, by (row offset, column offset) from the CW.
POSNAME = {(0, 1): "rostral within-row", (0, -1): "caudal within-row",
           (-1, 0): "dorsal same-arc", (1, 0): "ventral same-arc",
           (-1, 1): "dorsal rostral", (-1, -1): "dorsal caudal",
           (1, 1): "ventral rostral", (1, -1): "ventral caudal", (0, 0): "CW"}
# Layer bounds in um below pia, Methods, "Surgical preparation".
LAYERS = [("L2/3", 100, 417), ("L4", 418, 587), ("L5", 588, 889), ("L6", 890, 1154)]


def open_zip():
    return zipfile.ZipFile(fsspec.open(URL, block_size=2 ** 20).open())


def mat_names(z, experiment):
    return sorted(i.filename for i in z.infolist()
                  if i.filename.startswith(f"Experiment{experiment}/") and i.filename.endswith(".mat"))


def relpos(label, exp):
    pos, cw = (POS3, CW3) if exp == 3 else (POS12, CW12)
    r, c = pos[label]
    r0, c0 = pos[cw]
    return (r - r0, c - c0)


def layer_of(depth):
    for name, lo, hi in LAYERS:
        if lo <= depth <= hi:
            return name
    return "outside"


def _vec(x):
    return np.atleast_1d(np.asarray(x, dtype=float)).ravel()


def _trial_table_12(u):
    """Trial table of experiments 1 and 2 from one unit's struct."""
    rows = []
    for d, t, r in zip(u.DeflectedWs, u.timeWs, u.directionWs):
        d, t, r = _vec(d), _vec(t), _vec(r)
        if d.size == 1 and np.isnan(d[0]):
            rows.append(("sham", 0, 0, np.nan, 0, 0, np.nan))
            continue
        onset = np.nanmin(t)
        if d.size == 1:
            rows.append(("single", int(d[0]), 0, 0.0, int(r[0]), 0, onset))
        elif d.size == 2:
            if CW12 in d:
                i = int(np.where(d == CW12)[0][0])
                j = 1 - i
                # a = CW, b = SW, dt = t_SW - t_CW
                rows.append(("cwsw", CW12, int(d[j]), t[j] - t[i], int(r[i]), int(r[j]), onset))
            else:
                i, j = (0, 1) if d[0] < d[1] else (1, 0)
                rows.append(("swsw", int(d[i]), int(d[j]), t[j] - t[i], int(r[i]), int(r[j]), onset))
        else:
            rows.append(("triple", 0, 0, np.nan, 0, 0, onset))
    return pd.DataFrame(rows, columns=["kind", "a", "b", "dt", "da", "db", "onset"])


def _trial_table_3(u):
    rows = []
    for d, dt in zip(u.DeflectedWs, u.DeltaT):
        d = _vec(d)
        if d.size == 1 and np.isnan(d[0]):
            rows.append(("sham", 0, 0, np.nan, 1, 1, 0.0))
        elif d.size == 1:
            rows.append(("single", int(d[0]), 0, 0.0, 1, 0, 0.0))
        else:
            # DeltaT = t(second listed) - t(first listed) (shown in the data check).
            t = np.array([0.0, dt])
            if CW3 in d:
                i = int(np.where(d == CW3)[0][0])
                j = 1 - i
                rows.append(("cwsw", CW3, int(d[j]), t[j] - t[i], 1, 1, 0.0))
            else:
                i, j = (0, 1) if d[0] < d[1] else (1, 0)
                rows.append(("swsw", int(d[i]), int(d[j]), t[j] - t[i], 1, 1, 0.0))
    return pd.DataFrame(rows, columns=["kind", "a", "b", "dt", "da", "db", "onset"])


def _spikes(u, exp):
    """All spike times of a unit with their trial index."""
    cells = [np.atleast_2d(np.asarray(s, dtype=float))[:, 0] if exp == 3 and np.size(s)
             else _vec(s) if np.size(s) else np.zeros(0) for s in u.spkTime]
    n = np.fromiter((len(c) for c in cells), int, len(cells))
    t = np.concatenate(cells) if n.sum() else np.zeros(0)
    tri = np.repeat(np.arange(len(cells)), n)
    return t, tri


def load_experiment(z, exp, files=None, log=print):
    """Return (units, tables, psth).

    units: DataFrame, one row per unit (file, recording, depth, waveform hash, spike hash).
    tables: dict recording -> trial table, with a column per unit of spike counts in the response
    window (``c<k>``), counts over the whole trial (``w<k>``), counts in the 100 ms before onset
    (``p<k>``), and spikes after the epoch (``o<k>``); psth: dict recording -> counts in 10 ms
    bins from -50 to +200 ms around onset for the single and sham trials (all trials in
    experiment 3), with the trial mask ``rows``.
    """
    key = f"UnitInfoExp{exp}"
    units, tables, extras = [], {}, {}
    for name in files or mat_names(z, exp):
        U = np.atleast_1d(sio.loadmat(io.BytesIO(z.read(name)), squeeze_me=True,
                                      struct_as_record=False)[key])
        for u in U:
            # Units are grouped by their trial sequence (stimuli and their times), not by
            # recName: in 20160803 the recName of some units names another recording than the
            # one whose trials they carry (reported in the data check).
            h = hashlib.md5()
            for d in list(u.DeflectedWs) + list(u.DeltaT if exp == 3 else u.timeWs):
                h.update(_vec(d).tobytes())
            dhash = h.hexdigest()
            rec = f"{name.split('/')[1][:-4]}:{dhash[:6]}"
            if rec not in tables:
                tab = _trial_table_3(u) if exp == 3 else _trial_table_12(u)
                tab.attrs["dhash"] = dhash
                tables[rec] = tab
                extras[rec] = {}
            tab = tables[rec]
            assert tab.attrs["dhash"] == dhash and len(tab) == len(u.DeflectedWs), (name, rec)
            k = len(units)
            t, tri = _spikes(u, exp)
            onset = tab["onset"].to_numpy()
            on = onset[tri]
            # Sham trials have no onset: reading (a) of O1 places the window where single
            # deflections occur in that recording's trials.
            sham_on = np.nanmedian(tab.loc[tab.kind == "single", "onset"]) if exp != 3 else 0.0
            on = np.where(np.isnan(on), sham_on, on)
            rel = t - on
            ntr = len(tab)
            c = np.bincount(tri[(rel >= 0) & (rel < WINDOW)], minlength=ntr)
            p = np.bincount(tri[(rel >= -100) & (rel < 0)], minlength=ntr)
            maxt = 600.0 if exp != 3 else 300.0
            w = np.bincount(tri[(t >= 0) & (t < maxt)], minlength=ntr)
            sel = tab.kind.isin(["single", "sham"]).to_numpy() | (exp == 3)
            keep = sel[tri] & (rel >= -50) & (rel < 200)
            psth = np.zeros((ntr, 25), np.int16)
            np.add.at(psth, (tri[keep], ((rel[keep] + 50) // 10).astype(int)), 1)
            extras[rec][f"c{k}"] = c.astype(np.int16)
            extras[rec][f"p{k}"] = p.astype(np.int16)
            extras[rec][f"w{k}"] = w.astype(np.int16)
            # Spikes after the end of the epoch (experiment 3 epochs are about 300 ms long).
            extras[rec][f"o{k}"] = np.bincount(tri[t >= maxt], minlength=ntr).astype(np.int32)
            extras[rec][f"h{k}"] = psth[sel]
            if exp == 3:
                e = u.experiment
                depth, animal, whiskers = float(e.Tip_Depth), str(e.Animal_ID), str(e.Whiskers)
            else:
                depth, animal, whiskers = float(u.recDepth), name.split("/")[1][:8], ""
            units.append(dict(unit=k, file=name, recording=rec, recName=str(u.recName), depth=depth, animal=animal,
                              whiskers=whiskers, n_spikes=len(t),
                              n_out=int(np.sum((t < 0) | (t > maxt))),
                              max_t=float(t.max()) if len(t) else np.nan,
                              spike_hash=hashlib.md5(np.round(t, 3).tobytes()).hexdigest()))
        del U
        log(f"{name}: {sum(1 for x in units if x['file'] == name)} units")
    psth = {}
    for rec, tab in tables.items():
        ex = extras[rec]
        cols = {key_: v for key_, v in ex.items() if not key_.startswith("h")}
        tab.attrs = {}  # pandas copies attrs into every derived object
        tables[rec] = pd.concat([tab, pd.DataFrame(cols)], axis=1)
        psth[rec] = dict(rows=tab.kind.isin(["single", "sham"]).to_numpy() | (exp == 3),
                         **{key_: v for key_, v in ex.items() if key_.startswith("h")})
    return pd.DataFrame(units), tables, psth


# ---------------------------------------------------------------- measures

def sparseness(r, axis=-1):
    """Lifetime sparseness (Vinje and Gallant 2000), the claims file's reading of the Methods."""
    r = np.asarray(r, float)
    n = r.shape[axis]
    m1 = r.mean(axis=axis)
    m2 = (r ** 2).mean(axis=axis)
    with np.errstate(invalid="ignore", divide="ignore"):
        s = (1 - m1 ** 2 / m2) / (1 - 1 / n)
    return np.where(m2 > 0, s, 0.0)


def gaussian_kernels(n, sds):
    """Row-normalised Gaussian smoothing matrices (n x n) for each SD (renormalised at edges)."""
    x = np.arange(n)
    d = x[:, None] - x[None, :]
    K = np.exp(-0.5 * (d[None] / np.asarray(sds)[:, None, None]) ** 2)
    return K / K.sum(axis=2, keepdims=True)


def gaussian_kernels_zeropad(n, sds):
    """As gaussian_kernels but with zero padding at the edges (kernel normalised on the full line)."""
    x = np.arange(n)
    d = x[:, None] - x[None, :]
    sds = np.asarray(sds)[:, None, None]
    K = np.exp(-0.5 * (d[None] / sds) ** 2)
    full = np.sqrt(2 * np.pi) * sds  # integral; sums over the infinite integer line are close
    return K / full


SDS = np.round(np.arange(0.5, 30.0 + 1e-9, 0.2), 1)  # Methods, "dt smoothing"


def mahalanobis_p(measured, shuffled):
    """P-value of the measured trace's Mahalanobis distance from the shuffled mean (Methods)."""
    mu = shuffled.mean(axis=0)
    C = np.cov(shuffled, rowvar=False)
    P = np.linalg.pinv(C, rcond=1e-10, hermitian=True)
    d = shuffled - mu
    ds = np.einsum("ij,jk,ik->i", d, P, d)
    dm = (measured - mu) @ P @ (measured - mu)
    return (1 + np.sum(ds >= dm)) / (1 + len(ds)), dm


def bh(p, q=0.05):
    """Benjamini-Hochberg false discovery rate control; returns the rejected mask."""
    p = np.asarray(p)
    n = len(p)
    o = np.argsort(p)
    thr = q * np.arange(1, n + 1) / n
    ok = p[o] <= thr
    k = np.max(np.where(ok)[0]) + 1 if ok.any() else 0
    rej = np.zeros(n, bool)
    rej[o[:k]] = True
    return rej


def trial_length(units, rec):
    """Trial length in ms of a recording: the largest spike time rounded up to 100 ms."""
    return float(np.ceil(units.loc[units.recording == rec, "max_t"].max() / 100.0) * 100.0)


def lrt_responsive(tab, k, single_mask, sham_reading, length):
    """Poisson LRT across the nine whiskers and sham (Methods, "Analysis of neuronal data").

    single_mask selects the single-whisker trials used (for example one direction, O2).
    Sham reading (O1): 'a' counts sham spikes in the 125 ms window at the singles' onset;
    'b' uses the whole sham trial, with its exposure (length / 125 windows), so the rate is the
    whole-trial rate scaled to 125 ms. Recordings without sham trials are tested on the nine
    whiskers alone. Returns (G, p).
    """
    s = tab[single_mask]
    counts = list(s[f"c{k}"].to_numpy(float))
    groups = list(s["a"].to_numpy())
    expo = [1.0] * len(s)
    sh = tab[tab.kind == "sham"]
    if len(sh):
        if sham_reading == "a":
            counts += list(sh[f"c{k}"].to_numpy(float))
            expo += [1.0] * len(sh)
        else:
            counts += list(sh[f"w{k}"].to_numpy(float))
            expo += [length / WINDOW] * len(sh)
        groups += [0] * len(sh)
    counts, groups, expo = np.array(counts), np.array(groups), np.array(expo)
    labels, g = np.unique(groups, return_inverse=True)
    S = np.bincount(g, weights=counts)
    E = np.bincount(g, weights=expo)
    lam0 = counts.sum() / expo.sum()
    with np.errstate(divide="ignore", invalid="ignore"):
        term = np.where(S > 0, S * np.log(S / (E * lam0)), 0.0)
    G = 2 * term.sum()
    return G, stats.chi2.sf(G, len(labels) - 1)


def spont_rate(tab, k, sham_reading, length):
    """Spontaneous rate in Hz from sham trials (O1 readings as in lrt_responsive)."""
    sh = tab[tab.kind == "sham"]
    if not len(sh):
        return np.nan
    if sham_reading == "a":
        return sh[f"c{k}"].mean() / (WINDOW / 1000.0)
    return sh[f"w{k}"].mean() / (length / 1000.0)


# ---------------------------------------------------------------- experiment 2

DT_GRID = np.arange(-50, 51)  # the files hold 101 dt values, -50 to +50 ms (data check)
SWS12 = [1, 2, 3, 4, 6, 7, 8, 9]


def set_mask(tab, which):
    """CW-SW trials of the correlated (same direction) or anti-correlated set."""
    m = tab.kind == "cwsw"
    same = tab.da == tab.db
    return m & (same if which == "corr" else ~same)


def set_dirs(tab, which):
    """Directions each whisker takes in a set's CW-SW trials: {whisker: set of directions} (O2 a)."""
    s = tab[set_mask(tab, which)]
    out = {CW12: set(s.da.unique())}
    for w in SWS12:
        out[w] = set(s.loc[s.b == w, "db"].unique())
    return out


def single_mask_for(tab, dirs):
    m = np.zeros(len(tab), bool)
    for w, ds in dirs.items():
        m |= ((tab.kind == "single") & (tab.a == w) & tab.da.isin(list(ds))).to_numpy()
    return m


def fast_dt_smooth(y, dti, rng, kernels, reps=50, folds=10, ndt=101, floor=1e-3, return_ll=False):
    """Cross-validated Gaussian smoothing of a dt tuning curve (Methods, "dt smoothing").

    y: single-trial counts; dti: index of each trial's dt on the 1 ms grid (0..ndt-1). Tenfold
    cross-validation repeated ``reps`` times; the held-out Poisson log likelihood of the unsmoothed
    training curve and of the curve smoothed with each kernel, summed over folds and repeats.
    Returns (curve, kernel index, status, raw curve); status is 'monotonic' (the likelihood is
    largest at the largest kernel), 'unsmoothed' (the unsmoothed likelihood beats every smoothed
    one) or 'modulated', and the curve is the mean over dt for the first two.

    A held-out dt with no training trials takes the training mean in the unsmoothed curve
    (claims file, methods-dt-modulation reading (a)); zero rates are floored at 1e-3 spikes so
    the log likelihood stays finite (a standard choice; it affects only zero-count bins).
    With ``return_ll`` the likelihoods are also returned, as a dict, under two other ways of
    scoring held-out trials at a dt without training trials, which the Methods do not settle
    (an assumption shown as a variant): 'drop', left out of every likelihood, and 'nan_raw', left
    out of the unsmoothed likelihood only (as a sum that skips the undefined values of the
    unsmoothed curve would do).
    """
    y = np.asarray(y, float)
    n = len(y)
    ranks = np.argsort(np.argsort(rng.random((reps, n)), axis=1), axis=1)
    fold = ranks % folds  # (reps, n)
    fid = (np.arange(reps)[:, None] * folds + fold).ravel()  # fold id 0..reps*folds-1
    F = reps * folds
    dd = np.tile(dti, reps)
    yy = np.tile(y, reps)
    S_te = np.bincount(fid * ndt + dd, weights=yy, minlength=F * ndt).reshape(F, ndt)
    N_te = np.bincount(fid * ndt + dd, minlength=F * ndt).reshape(F, ndt).astype(float)
    S_all = np.bincount(dti, weights=y, minlength=ndt)
    N_all = np.bincount(dti, minlength=ndt).astype(float)
    S_tr, N_tr = S_all - S_te, N_all - N_te
    mtr = S_tr.sum(1, keepdims=True) / N_tr.sum(1, keepdims=True)
    raw = np.where(N_tr > 0, S_tr / np.maximum(N_tr, 1), mtr)  # (F, ndt)
    lam = np.maximum(raw, floor)
    ll_raw_terms = S_te * np.log(lam) - N_te * lam
    ll_raw = np.sum(ll_raw_terms)
    K = kernels.shape[0]
    sm = (kernels.reshape(K * ndt, ndt) @ raw.T).reshape(K, ndt, F)  # (K, ndt, F)
    lam = np.maximum(sm, floor)
    ll_sm = (np.log(lam).reshape(K, -1) @ S_te.T.ravel()) - (lam.reshape(K, -1) @ N_te.T.ravel())
    ll = None
    if return_ll:
        has = (N_tr > 0).T.ravel()
        ll_sm_drop = ((np.log(lam).reshape(K, -1) @ (S_te.T.ravel() * has))
                      - (lam.reshape(K, -1) @ (N_te.T.ravel() * has)))
        ll_raw_drop = np.sum(ll_raw_terms[N_tr > 0])
        ll = dict(sm=ll_sm, raw=ll_raw, sm_drop=ll_sm_drop, raw_drop=ll_raw_drop)
    raw_all = np.where(N_all > 0, S_all / np.maximum(N_all, 1), y.mean())
    best = int(np.argmax(ll_sm))
    if best == K - 1:
        out = np.full(ndt, y.mean()), None, "monotonic", raw_all
    elif ll_raw > ll_sm.max():
        out = np.full(ndt, y.mean()), None, "unsmoothed", raw_all
    else:
        out = kernels[best] @ raw_all, best, "modulated", raw_all
    return out + (ll,) if return_ll else out


def dt_status(ll_sm, ll_raw):
    """Status of a curve from its likelihoods, by the rules of fast_dt_smooth."""
    if int(np.argmax(ll_sm)) == len(ll_sm) - 1:
        return "monotonic"
    if ll_raw > ll_sm.max():
        return "unsmoothed"
    return "modulated"


def permute_within_dt(y, comb, dti, rng):
    """Counts permuted across combinations within each dt: a null with no combination tuning."""
    y = np.asarray(y, float)
    out = y.copy()
    for j in np.unique(dti):
        ii = np.where(dti == j)[0]
        out[ii] = y[rng.permutation(ii)]
    return out


def shuffle_test(y, comb, dti, rng, kernels, n_shuf=5000, ncomb=8):
    """The whole selectivity test on one response set: smoothing of each combination's curve with
    its cross-validated kernel, the measured CSI trace, the shuffles and the Mahalanobis p-value
    (Methods, "dt smoothing" and "Combination selectivity"). Returns (p, distance)."""
    curves, kidx = np.zeros((ncomb, kernels.shape[1])), []
    for c in range(ncomb):
        m = comb == c
        cv, ki = fast_dt_smooth(y[m], dti[m], rng, kernels)[:2]
        curves[c] = cv
        kidx.append(ki)
    csi = sparseness(curves.T)
    sh = shuffle_csi(y, comb, dti, kidx, kernels, rng, n_shuf=n_shuf, ncomb=ncomb)
    return mahalanobis_p(csi, sh)


def shuffle_csi(y, comb, dti, kern_idx, kernels, rng, n_shuf=5000, ncomb=8, ndt=101, chunk=500):
    """CSI traces of shuffles of single-trial counts across combinations within each dt (Methods).

    kern_idx[c] is the kernel index of combination c, or None for a curve set constant across dt;
    a shuffled curve of such a combination is set to its mean over dt (the measured curve's
    treatment carried over to the shuffles; the Methods do not say).
    """
    y = np.asarray(y, float)
    n = len(y)
    order = np.argsort(dti, kind="stable")
    y, comb, dti = y[order], comb[order], dti[order]
    N = np.bincount(comb * ndt + dti, minlength=ncomb * ndt).reshape(ncomb, ndt).astype(float)
    out = []
    for start in range(0, n_shuf, chunk):
        m = min(chunk, n_shuf - start)
        keys = dti[None, :] + rng.random((m, n))
        perm = np.argsort(keys, axis=1)  # a permutation within each dt group
        c_sh = comb[perm]
        idx = (np.arange(m)[:, None] * ncomb * ndt + c_sh * ndt + dti[None, :]).ravel()
        S = np.bincount(idx, weights=np.tile(y, m), minlength=m * ncomb * ndt).reshape(m, ncomb, ndt)
        cm = S.sum(2) / N.sum(1)[None, :]
        raw = np.where(N[None] > 0, S / np.maximum(N[None], 1), cm[:, :, None])
        sm = np.empty_like(raw)
        for c in range(ncomb):
            if kern_idx[c] is None:
                sm[:, c, :] = (S[:, c, :].sum(1) / N[c].sum())[:, None]
            else:
                sm[:, c, :] = raw[:, c, :] @ kernels[kern_idx[c]].T
        out.append(sparseness(np.transpose(sm, (0, 2, 1))))  # (m, ndt)
    return np.vstack(out)


# ---------------------------------------------------------------- decoders (Methods, "Neural decoders")

def fit_logistic_1d(x, Y, iters=1000, ridge=1e-4, tol=1e-8):
    """Logistic regressions of each column of the binary matrix Y on one feature x, by Newton's method.

    "Logistic functions were fit over 1,000 iterations" (Methods) is read as the iteration limit
    (claims file, O6). The small ridge keeps the fit finite when a class is perfectly separated
    (a standard choice; it cannot change which class wins except at exact ties).
    Returns params (K, 2): intercept and slope.
    """
    x = np.asarray(x, float)
    X = np.c_[np.ones_like(x), x]
    K = Y.shape[1]
    w = np.zeros((K, 2))
    for _ in range(iters):
        eta = X @ w.T  # (n, K)
        p = 1 / (1 + np.exp(-eta))
        g = X.T @ (Y - p) - ridge * w.T  # (2, K)
        Wt = p * (1 - p)
        H00 = Wt.sum(0) + ridge
        H01 = (Wt * x[:, None]).sum(0)
        H11 = (Wt * x[:, None] ** 2).sum(0) + ridge
        det = H00 * H11 - H01 ** 2
        d0 = (H11 * g[0] - H01 * g[1]) / det
        d1 = (-H01 * g[0] + H00 * g[1]) / det
        w[:, 0] += d0
        w[:, 1] += d1
        if np.max(np.abs(np.r_[d0, d1])) < tol:
            break
    return w


def heldout_prob_rows(x, y, ncls, rng, folds=10):
    """Tenfold cross-validated one-versus-all probabilities for each trial (Methods).

    x: counts, y: class labels 0..ncls-1. Each trial's row comes from the classifiers fitted on the
    other nine folds.
    """
    x = np.asarray(x, float)
    out = np.zeros((len(x), ncls))
    perm = rng.permutation(len(x))
    fold = np.empty(len(x), int)
    fold[perm] = np.arange(len(x)) % folds
    for f in range(folds):
        tr = fold != f
        Y = (y[tr][:, None] == np.arange(ncls)[None, :]).astype(float)
        w = fit_logistic_1d(x[tr], Y)
        out[~tr] = 1 / (1 + np.exp(-(w[:, 0][None, :] + np.outer(x[~tr], w[:, 1]))))
    return out


class Pool:
    """Held-out probability rows of many units, for population decoding by summed probabilities."""

    def __init__(self, probs, labels, ncls):
        self.ncls = ncls
        rows, off, cnt = [], [], []
        start = 0
        for P, lab in zip(probs, labels):
            o, c = [], []
            for k in range(ncls):
                ii = np.where(lab == k)[0]
                rows.append(P[ii])
                o.append(start)
                c.append(len(ii))
                start += len(ii)
            off.append(o)
            cnt.append(c)
        self.P = np.vstack(rows)
        self.off = np.array(off)
        self.cnt = np.array(cnt)

    def accuracy(self, N, n_ens, rng, units=None, chunk=250):
        """Per-ensemble, per-class accuracy (n_ens, ncls); units sampled with replacement."""
        pool = np.arange(len(self.off)) if units is None else np.asarray(units)
        res = []
        for s in range(0, n_ens, chunk):
            m = min(chunk, n_ens - s)
            u = pool[rng.integers(0, len(pool), (m, N))]  # (m, N)
            r = rng.random((m, N, self.ncls))
            idx = self.off[u] + np.minimum((r * self.cnt[u]).astype(int), self.cnt[u] - 1)  # (m, N, ncls)
            tot = self.P[idx].sum(axis=1)  # (m, ncls_true, ncls_prob)
            res.append(np.argmax(tot, axis=2) == np.arange(self.ncls)[None, :])
        return np.vstack(res)
