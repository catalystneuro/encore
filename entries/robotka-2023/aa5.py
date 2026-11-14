"""Loading and measures for CRCNS aa-5, the awake playback data of Robotka et al. (2023).

Robotka, Thomas, Yu, Wood, Elie, Gahr & Theunissen (2023), Cell Reports 42, 112034,
doi:10.1016/j.celrep.2023.112034. Data set: CRCNS aa-5, doi:10.6080/K0TT4P5Q (unversioned).

The data set holds one tar.gz per recording site, each with one pickle per spike-sorted unit
(`goodPlayback-e<electrode>-c<cluster>.pkl`, data descriptor v0.6). A pickle holds a unit
dictionary and two pandas tables written with pandas 1.x; `pandas.compat.pickle_compat` reads
them. A tar.gz cannot be read out of order, so each site file is streamed once from the bucket
(decompressed with isal, which is faster than zlib), and each unit is reduced as it is read to
what the analysis uses: spike times per trial, the stored KDE (first 1000 samples), labels, and
the stimulus waveform of each stimulus once. The microphone recordings, most of every file, are
dropped. Nothing is written to disk.

Where the parameters come from (the claims file's common methods C1 to C11 cite the paper and
its code, github.com/ftheunissen/Ensemble-Code-Cell-Reports-2022 at commit f2d2376):

- `SNR_MIN = 5`: units with spike SNR above 5 (C1; GenerateDataBase.ipynb skips SpikeSNR < 5).
- `P_AUD = 0.01` and the 0 to 0.5 s minus -0.5 to 0 s spike-count difference (C1, SI Figure 2A
  legend; GenerateReport.ipynb calc_zscore_all, which uses all stimuli of the pickle, song
  included). A unit with no call-type label in its pickle (song-only sites) is skipped, as the
  code does (`if ncalls == 0: continue`).
- `N_KDE = 1000`, `MIN_TRIALS_KDE = 5`: the PCA of the trial-averaged responses uses the stored
  spikeKDE, first 1000 samples, of stimuli with 5 or more trials (C4; GenerateDataBase.ipynb).
- The PC weight of a trial is 1000 per spike at its nearest KDE sample, minus the mean, projected
  on the first five PCs (C4; GenerateDataBase.ipynb cell 17).
- Decoder: GaussianNB with uniform priors (C5; decoders.naiveBayes).
"""

from __future__ import annotations

import hashlib
import io
import re
import time
from concurrent.futures import ProcessPoolExecutor, as_completed

import numpy as np
import pandas as pd

BUCKET = "https://crcnsarchive.s3-us-west-2.amazonaws.com/"
PREFIX = "aa-5/live/"
DOI = "10.6080/K0TT4P5Q"

SNR_MIN = 5.0
P_AUD = 0.01
N_KDE = 1000
MIN_TRIALS_KDE = 5
N_PC = 5
CALL_TYPES = ["Ag", "Be", "DC", "Di", "LT", "Ne", "So", "Te", "Th", "Wh"]


# ----------------------------------------------------------------------------------------------
# Listing and streaming


def list_files():
    """Every object of the data set in the bucket, as (key, size)."""
    import requests

    out, token = [], None
    while True:
        params = {"list-type": "2", "prefix": PREFIX}
        if token:
            params["continuation-token"] = token
        t = requests.get(BUCKET, params=params, timeout=60).text
        out += [(k, int(s)) for k, s in re.findall(r"<Key>(.*?)</Key>.*?<Size>(\d+)</Size>", t, re.S)]
        m = re.search(r"<NextContinuationToken>(.*?)</NextContinuationToken>", t)
        if not m:
            return out
        token = m.group(1)


def checksums():
    """The data set's checksums.md5, as {path relative to aa-5/live/: md5}."""
    import requests

    t = requests.get(BUCKET + PREFIX + "checksums.md5", timeout=60).text
    return {p.strip(): h for h, p in (ln.split(None, 1) for ln in t.splitlines() if ln.strip())}


def _unpickle(fobj):
    from pandas.compat import pickle_compat

    return pickle_compat.Unpickler(fobj).load()


def _reduce_unit(info, dfabs, dfrel, member):
    """Keep what the analysis needs from one unit's pickle."""
    rows = []
    for _, r in dfrel.iterrows():
        st = [np.asarray(s, dtype=float) for s in r["spikeTimes"]]
        tk = np.asarray(r["tKDE"], dtype=float)
        rows.append(dict(
            file=r["file"], call_type=r["call_type"], relation_short=r["relation_short"],
            nTrials=int(r["nTrials"]), trialInd=np.asarray(r["trialInd"]), spikeTimes=st,
            kde=np.asarray(r["spikeKDE"], dtype=np.float32)[:N_KDE].copy(),
            tKDE0=float(tk[0]), dtKDE=float(tk[1] - tk[0]), nKDE=len(tk),
            tStim0=float(r["tStim"][0]), dtStim=float(r["tStim"][1] - r["tStim"][0]),
            stimLen=len(r["stimWav"]),
            stimHash=hashlib.md5(np.asarray(r["stimWav"], dtype=np.float32).tobytes()).hexdigest(),
            micShape=tuple(np.shape(r["micWav"])),
        ))
    spk_hash = hashlib.md5(b"".join(np.round(s, 6).tobytes() for row in rows for s in row["spikeTimes"])).hexdigest()
    unit = dict(
        member=member, pkl=member.split("/")[-1], Bird=info["Bird"], Site=info["Site"],
        Electrode=str(info["Electrode"]), Sort=int(info["Sort"]), SpikeSNR=float(info["SpikeSNR"]),
        nStim=int(info["nStim"]), KDE_BW=float(info["KDE_BW"]), RateThreshold=float(info["RateThreshold"]),
        info_keys=sorted(info.keys()), abs_columns=list(dfabs.columns), rel_columns=list(dfrel.columns),
        n_abs_rows=len(dfabs), spike_hash=spk_hash, rows=rows,
    )
    waves = {}
    for _, r in dfrel.iterrows():
        if r["call_type"] is not None and r["file"] not in waves:
            waves[r["file"]] = dict(wav=np.asarray(r["stimWav"], dtype=np.float32), tStim0=float(r["tStim"][0]),
                                    dt=float(r["tStim"][1] - r["tStim"][0]), call_type=r["call_type"])
    return unit, waves


def read_site(key, max_units=None):
    """Stream one site tar.gz and return (units, stimulus waveforms, other members, seconds)."""
    import tarfile

    import fsspec
    from isal import igzip

    t0 = time.time()
    units, waves, other = [], {}, []
    with fsspec.open(BUCKET + key, block_size=2**24).open() as f:
        gz = igzip.IGzipFile(fileobj=f, mode="rb")
        with tarfile.open(fileobj=gz, mode="r|") as tf:
            for m in tf:
                if not m.isfile():
                    continue
                base = m.name.split("/")[-1]
                if base.startswith("._") or not base.endswith(".pkl"):
                    other.append((m.name, m.size))
                    continue
                fo = tf.extractfile(m)
                buf = io.BufferedReader(fo, buffer_size=2**22)
                info = _unpickle(buf)
                dfabs = _unpickle(buf)
                dfrel = _unpickle(buf)
                u, w = _reduce_unit(info, dfabs, dfrel, m.name)
                del dfabs, dfrel
                units.append(u)
                for k, v in w.items():
                    waves.setdefault(k, v)
                if max_units and len(units) >= max_units:
                    break
    return units, waves, other, time.time() - t0


def read_all(keys, workers=4, max_units=None, log=print):
    """Stream every site in `keys` with `workers` processes; largest files first."""
    results = {}
    t0 = time.time()
    with ProcessPoolExecutor(workers) as ex:
        futs = {ex.submit(read_site, k, max_units): k for k in keys}
        for fu in as_completed(futs):
            k = futs[fu]
            results[k] = fu.result()
            log(f"{k.split('/')[-1]}: {len(results[k][0])} units, {results[k][3]:.0f} s "
                f"(elapsed {time.time() - t0:.0f} s, {len(results)}/{len(keys)})")
    units, waves, other = [], {}, []
    for k in keys:
        u, w, o, _ = results[k]
        units += u
        other += o
        for s, v in w.items():
            waves.setdefault(s, []).append(v)
    return units, waves, other


# ----------------------------------------------------------------------------------------------
# Single-unit measures


def spike_diff(spike_times):
    """Spike count in [0, 0.5) s minus count in [-0.5, 0) s for one trial (C1)."""
    s = spike_times
    return float(np.sum((s >= 0) & (s < 0.5)) - np.sum((s >= -0.5) & (s < 0)))


def unit_table(units):
    """One row per unit with SNR, auditory test (Methods and code readings) and labels."""
    from scipy import stats

    recs = []
    for u in units:
        d_all = np.array([spike_diff(s) for r in u["rows"] for s in r["spikeTimes"]])
        calls = sorted({r["call_type"] for r in u["rows"] if r["call_type"] is not None})
        n = len(d_all)
        sd = d_all.std(ddof=1) if n > 1 else 0.0
        if n > 1 and sd == 0:
            d_all = d_all.copy()
            d_all[0] += 1  # the code adds a spike when the SD is zero (calc_zscore_all)
            sd = d_all.std(ddof=1)
        z = d_all.mean() / sd if n > 1 else 0.0
        # Methods reading: standard one-sample t-test, n - 1 df
        p_methods = stats.ttest_1samp(d_all, 0.0).pvalue if n > 1 else 1.0
        # Code reading: t = z sqrt(n) with n df (calc_zscore_all)
        p_code = 2 * stats.t.sf(abs(z) * np.sqrt(n), n) if n > 1 else 1.0
        recs.append(dict(
            uid=u["Site"] + "_" + u["pkl"], bird=u["Bird"], site=u["Site"], electrode=u["Electrode"],
            sort=u["Sort"], snr=u["SpikeSNR"], n_calls=len(calls), n_trials_all=n, zAud=z,
            meanD=d_all.mean() if n else np.nan, p_methods=p_methods, p_code=p_code,
            n_voc_stim=len({r["file"] for r in u["rows"] if r["call_type"] is not None}),
            spike_hash=u["spike_hash"],
        ))
    return pd.DataFrame(recs)


def voc_rows(u):
    return [r for r in u["rows"] if r["call_type"] is not None]


def trial_table(u):
    """Vocalization trials of one unit: stim, call, d, and Z (C2, both readings)."""
    recs = []
    for r in voc_rows(u):
        for it, s in enumerate(r["spikeTimes"]):
            recs.append((r["file"], r["call_type"], it, spike_diff(s)))
    df = pd.DataFrame(recs, columns=["stim", "call", "trial", "R"])
    sd = df["R"].std(ddof=0)
    if sd == 0:
        sd = 1.0 / len(df)
    df["z"] = df["R"] / sd                       # code reading (b): d / SD, ddof 0
    df["z_a"] = (df["R"] - df["R"].mean()) / sd  # Methods reading (a): z-scored
    return df


def zct_unit(u, trials):
    """Per-call-type Z of one unit: (a) mean trial Z (C2 b) per type; (b) code's mean(d)/sd(d)."""
    za, zb = {}, {}
    for c, g in trials.groupby("call"):
        za[c] = g["z"].mean()
        d = g["R"].to_numpy().astype(float)
        if len(d) > 1:
            sd = d.std(ddof=1)
            if sd == 0:
                d = d.copy()
                d[0] += 1
                sd = d.std(ddof=1)
            zb[c] = d.mean() / sd
        else:
            zb[c] = 0.0
    return za, zb


def selectivity_index(z):
    z = np.asarray(list(z), dtype=float)
    n = len(z)
    return (1 - z.mean() ** 2 / (z ** 2).mean()) / (1 - 1 / n)


def kde_matrix(u):
    """Stored KDE (first 1000 samples) of each vocalization stimulus with >= 5 trials (C4)."""
    out = []
    for r in voc_rows(u):
        if r["nTrials"] >= MIN_TRIALS_KDE:
            k = r["kde"][:N_KDE].astype(float)
            if not np.sum(np.concatenate(r["spikeTimes"]) if r["spikeTimes"] else [0.0]):
                k = np.zeros(N_KDE)  # the code leaves rows of stimuli with no spikes at zero
            out.append(k)
    return np.array(out).reshape(-1, N_KDE)


def trial_pcs(u, pca):
    """PC weights T1..T5 of every vocalization trial (C4; GenerateDataBase.ipynb cell 17)."""
    comps = pca.components_[:N_PC, :N_KDE]
    base = comps @ (-pca.mean_)
    out = []
    for r in voc_rows(u):
        tk = r["tKDE0"] + r["dtKDE"] * np.arange(r["nKDE"])
        for s in r["spikeTimes"]:
            v = base.copy()
            if len(s):
                idx = np.searchsorted(tk, s)
                idx = np.clip(idx, 1, len(tk) - 1)
                left = tk[idx - 1]
                right = tk[idx]
                idx = np.where(np.abs(s - left) <= np.abs(right - s), idx - 1, idx)
                idx = idx[idx < N_KDE]
                if len(idx):
                    v = v + 1000.0 * comps[:, idx].sum(axis=1)
            out.append(v)
    return np.array(out).reshape(-1, N_PC)


# ----------------------------------------------------------------------------------------------
# Decoding (C5)


def unit_features(trials, T, stims):
    """Array [n_stims, max_trials, 6] of (Z, T1..T5) per trial, NaN padded, and counts [n_stims]."""
    feats = np.column_stack([trials["z"].to_numpy(), T])
    groups = {s: feats[idx] for s, idx in trials.groupby("stim").indices.items()}
    tmax = max(len(groups.get(s, [])) for s in stims)
    F = np.full((len(stims), max(tmax, 1), 6), np.nan)
    C = np.zeros(len(stims), dtype=int)
    for i, s in enumerate(stims):
        g = groups.get(s)
        if g is not None:
            F[i, :len(g)] = g
            C[i] = len(g)
    return F, C


def _gnb_posterior(Xtr, ytr, Xte, nc):
    """sklearn GaussianNB (ML variances plus 1e-9 times the largest feature variance) with
    uniform priors, written out in numpy for speed; returns posteriors of the test rows."""
    eps = 1e-9 * Xtr.var(axis=0).max()
    mu = np.zeros((nc, Xtr.shape[1]))
    var = np.zeros((nc, Xtr.shape[1]))
    for c in range(nc):
        Xc = Xtr[ytr == c]
        mu[c] = Xc.mean(axis=0)
        var[c] = Xc.var(axis=0) + eps
    ll = -0.5 * (np.log(2 * np.pi * var).sum(axis=1)[None, :]
                 + (((Xte[:, None, :] - mu[None]) ** 2) / var[None]).sum(axis=2))
    ll -= ll.max(axis=1, keepdims=True)
    p = np.exp(ll)
    return p / p.sum(axis=1, keepdims=True)


def _rows(F, C, rng, skip=None):
    """Training rows of one ensemble for every stimulus (decoders.naiveBayes): row i joins the
    i-th trial of each unit (skipping its held-out trial, skip >= 0; -1 for none), and units with fewer trials are
    padded with random redraws of their own trials. Returns X [S, n, U*6] and n per stimulus."""
    U, S, Tm, nf = F.shape
    if skip is None:
        skip = np.full(C.shape, -1)
    R = np.maximum(C - (skip >= 0), 0)
    n = R.max(axis=0)
    i = np.arange(Tm)[None, None, :]
    rnd = (rng.random((U, S, Tm)) * np.maximum(R, 1)[:, :, None]).astype(int)
    idx = np.where(i < R[:, :, None], i, rnd)
    idx = idx + ((skip[:, :, None] >= 0) & (idx >= skip[:, :, None]))
    idx = np.minimum(idx, Tm - 1)
    X = np.take_along_axis(F, idx[..., None], axis=2)      # U, S, Tm, 6
    X = np.transpose(X, (1, 2, 0, 3)).reshape(S, Tm, U * nf)
    return X, n


def decode(F, C, y, nc, rng, code="ZT", cv="trial", nperm=1):
    """Gaussian naive Bayes decoding of the labels y [S] from an ensemble (C5).

    F [U, S, Tmax, 6] and C [U, S] are the stacked unit_features of the ensemble's units over a
    common stimulus list. cv = "trial", the code (decoders.naiveBayes): for each repetition one
    random trial of every stimulus with at least 2 trials in every unit is held out and tested.
    cv = "exemplar", the Methods (STAR Methods, Naive Bayesian decoder: "for each call-type, the
    responses to one of the exemplar stimuli was removed from the fitting procedure and used (as a
    testing set)"): one random exemplar per label per repetition is held out; its trials are
    joined into test rows as the training rows are. Returns the summed posterior confusion
    matrix (true x predicted) and the number of test rows per class.
    """
    U, S, Tm, _ = F.shape
    feat = [0] if code == "Z" else list(range(6))
    Fx = F[..., feat]
    conf = np.zeros((nc, nc))
    ntest = np.zeros(nc)
    ok = C.min(axis=0) > 0
    for _ in range(nperm):
        if cv == "trial":
            testable = ok & (C.min(axis=0) >= 2)
            t = (rng.random((U, S)) * np.maximum(C, 1)).astype(int)
            Xs, n = _rows(Fx, C, rng, skip=np.where(testable[None, :], t, -1))
            mask = (np.arange(Tm)[None, :] < n[:, None]) & ok[:, None]
            Xtr = Xs[mask]
            ytr = np.repeat(y, Tm).reshape(S, Tm)[mask]
            ti = np.where(testable)[0]
            Xte = np.transpose(np.take_along_axis(Fx[:, ti], t[:, ti, None, None], axis=2)[:, :, 0], (1, 0, 2)).reshape(len(ti), -1)
            yte = y[ti]
        else:
            held = np.zeros(S, dtype=bool)
            for c in range(nc):
                cand = np.where((y == c) & ok)[0]
                if len(cand):
                    held[cand[rng.integers(len(cand))]] = True
            Xs, n = _rows(Fx, C, rng)
            valid = (np.arange(Tm)[None, :] < n[:, None]) & ok[:, None]
            yy = np.repeat(y, Tm).reshape(S, Tm)
            Xtr, ytr = Xs[valid & ~held[:, None]], yy[valid & ~held[:, None]]
            Xte, yte = Xs[valid & held[:, None]], yy[valid & held[:, None]]
        if len(np.unique(ytr)) != nc:
            continue
        P = _gnb_posterior(Xtr, ytr, Xte, nc)
        np.add.at(conf, yte, P)
        np.add.at(ntest, yte, 1)
    return conf, ntest


def pcc_code(conf, ntest):
    """PCC as the code: trace of the summed matrix over the number of test trials (C5 b)."""
    return 100.0 * np.trace(conf) / ntest.sum()


def pcc_methods(conf, ntest):
    """PCC as the Methods: mean of the diagonal of the row-normalized matrix (C5 a)."""
    ok = ntest > 0
    return 100.0 * np.mean(np.diag(conf)[ok] / ntest[ok])


def row_normalize(conf, ntest):
    out = np.zeros_like(conf)
    ok = ntest > 0
    out[ok] = conf[ok] / ntest[ok, None]
    return out


# ----------------------------------------------------------------------------------------------
# Ensemble-corrected statistics (C8)


def corrected_sem(x, ns, ne):
    """Ensemble-corrected SD and SEM and neff (Methods, Statistical analysis; C8)."""
    x = np.asarray(x, dtype=float)
    neff = ns - ne + 1
    sc = np.sqrt(ns / (ns - ne) * x.var(ddof=1))
    return sc, sc / np.sqrt(neff), neff


def corrected_ttest(x, y, ns, ne):
    """Two-sample t-test with ensemble-corrected SEMs and 2 neff - 2 df (C8)."""
    from scipy import stats

    _, sx, neff = corrected_sem(x, ns, ne)
    _, sy, _ = corrected_sem(y, ns, ne)
    t = (np.mean(x) - np.mean(y)) / np.sqrt(sx ** 2 + sy ** 2)
    df = 2 * neff - 2
    return t, df, 2 * stats.t.sf(abs(t), df)


# ----------------------------------------------------------------------------------------------
# The per-trial database of auditory units (C1, C2, C4)


def build_database(units, waves):
    """Auditory units (SNR >= 5, code's p <= 0.01, at least one call type; GenerateDataBase.ipynb),
    their vocalization trials with Z, the PCA of trial-averaged KDEs, and per-trial T1..T5."""
    from sklearn.decomposition import PCA

    ut = unit_table(units)
    by = {u["Site"] + "_" + u["pkl"]: u for u in units}
    aud = ut[(ut.n_calls > 0) & (ut.snr >= SNR_MIN) & (ut.p_code <= P_AUD)].reset_index(drop=True)
    K = np.vstack([kde_matrix(by[x]) for x in aud.uid])
    pca = PCA(n_components=10).fit(K)
    stims = sorted(waves)
    calls = {s: waves[s][0]["call_type"] for s in stims}
    labels = sorted(set(calls.values()))
    y = np.array([labels.index(calls[s]) for s in stims])
    trials, T, feat = {}, {}, {}
    for x in aud.uid:
        tr = trial_table(by[x])
        trials[x] = tr
        T[x] = trial_pcs(by[x], pca)
        feat[x] = unit_features(tr, T[x], stims)
    tmax = max(f[0].shape[1] for f in feat.values())
    return dict(ut=ut, aud=aud, pca=pca, n_kde_rows=K.shape[0], stims=stims, calls=calls, labels=labels,
                y=y, trials=trials, T=T, feat=feat, tmax=tmax)


def stack(db, uids, stim_idx=None):
    """F [U, S, Tmax, 6] and C [U, S] for an ensemble."""
    tm = db["tmax"]
    S = len(db["stims"])
    F = np.full((len(uids), S, tm, 6), np.nan)
    C = np.zeros((len(uids), S), dtype=int)
    for i, x in enumerate(uids):
        f, c = db["feat"][x]
        F[i, :, :f.shape[1]] = f
        C[i] = c
    if stim_idx is not None:
        F, C = F[:, stim_idx], C[:, stim_idx]
    return F, C


_DB = None


def _run_chunk(args):
    ensembles, code, cv, nperm, seed, y = args
    rng = np.random.default_rng(seed)
    nc = len(np.unique(y))
    out = []
    for e in ensembles:
        F, C = stack(_DB, e)
        conf, nt = decode(F, C, y, nc, rng, code=code, cv=cv, nperm=nperm)
        out.append((conf, nt))
    return out


def run_ensembles(db, ensembles, code="ZT", cv="trial", nperm=1, seed=0, workers=4, y=None, chunk=50):
    """Decode many ensembles in parallel (fork). Returns PCC (code), PCC (Methods), the confusion
    matrices summed per ensemble, and tests per class per ensemble."""
    import multiprocessing as mp

    global _DB
    _DB = db
    y = db["y"] if y is None else y
    ss = np.random.SeedSequence(seed)
    chunks = [ensembles[i:i + chunk] for i in range(0, len(ensembles), chunk)]
    seeds = ss.spawn(len(chunks))
    args = [(c, code, cv, nperm, s, y) for c, s in zip(chunks, seeds)]
    if workers > 1:
        with mp.get_context("fork").Pool(workers) as p:
            res = p.map(_run_chunk, args)
    else:
        res = [_run_chunk(a) for a in args]
    res = [r for rr in res for r in rr]
    confs = np.array([r[0] for r in res])
    nts = np.array([r[1] for r in res])
    pb = np.array([pcc_code(c, n) for c, n in zip(confs, nts)])
    pa = np.array([pcc_methods(c, n) for c, n in zip(confs, nts)])
    return dict(pcc_code=pb, pcc_methods=pa, conf=confs, ntest=nts)


def mean_confusion(res):
    """Average over ensembles of the row-normalized confusion matrices."""
    return np.mean([row_normalize(c, n) for c, n in zip(res["conf"], res["ntest"])], axis=0)


def entropy_selectivity(conf, ntest, normalize=True):
    """ES = 1 - H/log2(n) of the diagonal (C11): (a) diagonal normalized to sum 1 (code),
    (b) the diagonal PCC per call type used directly (Methods formula)."""
    d = np.diag(row_normalize(conf, ntest)).copy()
    if normalize:
        d = d / d.sum()
    d = d[d > 0]
    return 1 - np.sum(-d * np.log2(d)) / np.log2(conf.shape[0])


def corrected_regression(X, y, ns, ne):
    """OLS of y on X with the ensemble-corrected F test (C8; GenerateMLFilters.ipynb)."""
    from scipy import stats

    X = np.atleast_2d(np.asarray(X, dtype=float).T).T
    y = np.asarray(y, dtype=float)
    n = len(y)
    A = np.column_stack([np.ones(n), X])
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    sse = np.sum((y - A @ coef) ** 2)
    sst = np.sum((y - y.mean()) ** 2)
    k = A.shape[1]
    r2adj = 1 - (sse / (n - k)) / (sst / (n - 1))
    neff = ns - ne + 1
    F = (neff / n) * ((sst - sse) / (k - 1)) / (sse / (n - k))
    df = (k - 1, neff - k)
    return dict(coef=coef, r2adj=r2adj, F=F, df=df, p=stats.f.sf(F, *df), n=n)


# ----------------------------------------------------------------------------------------------
# MPS, MRFs, LDA space and volume (C9, C10)


def stimulus_mps(wave, t0, dt, window="methods"):
    """MPS of one stimulus with soundsig BioSound, as GenerateMLFilters.ipynb (spectroCalc at 1 kHz,
    50 Hz spacing, 0 to 10 kHz; mpsCalc with a 100 ms window, Norm = True). window = "methods":
    the first 500 ms of the stimulus (STAR Methods, MRFs: "MPS were estimated for the first 500 ms
    of the stimulus"); "code": 500 ms before to 500 ms after onset (GenerateMLFilters.ipynb)."""
    from soundsig.sound import BioSound

    t = t0 + dt * np.arange(len(wave))
    lo, hi = (0.0, 0.5) if window == "methods" else (-0.5, 0.5)
    i0 = np.nonzero(t >= lo - 1e-9)[0][0]
    i1 = np.nonzero(t >= hi - 1e-9)[0][0]
    w = np.asarray(wave[i0:i1], dtype=float)
    fs = np.fix(1.0 / dt)
    b = BioSound(soundWave=w, fs=fs)
    b.spectroCalc(spec_sample_rate=1000, freq_spacing=50, min_freq=0, max_freq=10000)
    b.rms = b.sound.std()
    b.mpsCalc(window=0.1, Norm=True)
    return b.mps, b.wt, b.wf


def mps_window(wt, wf):
    """Temporal modulations -50 to 50 Hz, spectral 0 to 4 cyc/kHz (GenerateMLFilters.ipynb)."""
    it0 = np.argwhere(wt > -50)[0][0]
    it1 = np.argwhere(wt > 50)[0][0]
    if0 = np.argwhere(wf >= 0)[0][0]
    if1 = np.argwhere(wf * 1000 > 4)[0][0]
    return slice(if0, if1), slice(it0, it1)


def lda_axes(mps, y, rule="largest"):
    """LDA axes of the cropped MPS (C10): eigenvectors of pinv(within, rcond 1e-4) @ between.
    rule = "largest": the three of largest eigenvalue (Methods' "first three discriminant
    dimensions"); "eigh": the code's numpy eigh, first three columns (ascending eigenvalues)."""
    X = mps.reshape(len(mps), -1)
    classes = np.unique(y)
    means = np.array([X[y == c].mean(axis=0) for c in classes])
    between = np.cov(means.T)
    within = np.mean([np.cov((X[y == c] - X[y == c].mean(axis=0)).T) for c in classes], axis=0)
    M = np.linalg.pinv(within, rcond=1e-4, hermitian=True) @ between
    if rule == "eigh":
        val, vec = np.linalg.eigh(M)
        return vec[:, :3], val
    val, vec = np.linalg.eig(M)
    order = np.argsort(-val.real)
    return np.real(vec[:, order[:3]]), val.real[order]
