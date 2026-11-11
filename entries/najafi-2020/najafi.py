"""Loading and shared measures for Najafi et al. (2020) on DANDI:000016.

The dandiset holds one NWB file per imaging session. Each file has a trial
table, the ROI table (status good or bad, neuron type excitatory, inhibitory or
unknown) and, under processing/Ophys, trial-segmented traces of the good ROIs
aligned to trial events, one dataset per trial (frames x ROIs). The traces are
named dFoF_*, but their values are the normalised inferred spiking activity the
paper analyses (sparse, non-negative up to numerical noise, each neuron's
maximum 1); the notebook shows this.

Where the parameters come from:
- Bins of 3 frames (97 ms), aligned to the choice; bin -1 is the 3 frames
  before the choice frame: STAR Methods, "Quantification and statistical
  analysis", and the claims file's opening comment (code,
  svm_excInh_trainDecoder_eachFrame.py).
- Trials: the file's trial_is_good flag and a correct or incorrect response
  (claims file, opening comment, code setTrs2rmv.m / set_outcomes_allResp.m).
  The notebook shows that trial_is_good is exactly "response correct or
  incorrect", and the trial table has no column for helped trials or for the
  first trials of a session, so the code's other exclusions cannot be applied
  (a deviation). 16 Hz trials have no known choice side (see read_trials).
- ROC: AUC of high-rate against low-rate choice (the side labels are not in
  the files; AUC deviation from 0.5 does not depend on which choice is called
  left), 50 label shuffles, a neuron selective when the normal density ratio
  normpdf(AUC)/normpdf(mean) <= 0.05 (claims file, opening comment, code
  choicePref_ROC_exc_inh_plots_setVars.m).
- SVM: claims file, opening comment (LinearSVC, z-scoring with 5e-4 added to
  the SD, matched choices, 50 random 90/10 splits, C from 10^(-6..6, step
  0.2) / n_trials chosen by minimum mean test error).
- FSSPEC block size and thread counts are standard choices that cannot change
  a result.
"""
from __future__ import annotations

import concurrent.futures as cf
import os

import fsspec
import h5py
import numpy as np
import pandas as pd
import requests

DANDISET = "000016"
VERSION = "0.260915.2309"
API = "https://api.dandiarchive.org/api"
FRAMES_PER_BIN = 3
# paper mouse numbers, matched by session counts (45, 48, 7, 35); the notebook checks them
MOUSE = {"mouse1_fni16": 1, "mouse2_fni17": 2, "mouse3_fni18": 3, "mouse4_fni19": 4}
LEARNING_MICE = (1, 2, 4)  # Figure S1C and the claims file; same field of view through learning


def assets():
    """List the version's assets as a DataFrame (path, asset_id, size, subject)."""
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=400"
    rows = []
    while url:
        r = requests.get(url, timeout=60).json()
        rows += r["results"]
        url = r.get("next")
    df = pd.DataFrame(rows)[["path", "asset_id", "size"]]
    df["subject"] = df.path.str.split("/").str[0].str.replace("sub-", "").str.replace("-", "_")
    df["mouse"] = df.subject.map(MOUSE)
    return df.sort_values("path").reset_index(drop=True)


def s3_url(asset_id):
    r = requests.head(f"{API}/assets/{asset_id}/download/", allow_redirects=True, timeout=60)
    return r.url


def open_asset(asset_id):
    """Open an NWB file by streaming (HTTP range requests through an 8 MB block cache)."""
    fs = fsspec.filesystem("http")
    fo = fs.open(s3_url(asset_id), "rb", block_size=8 * 2**20, cache_type="blockcache",
                 cache_options={"maxblocks": 4})
    return h5py.File(fo, "r")


def _s(x):
    return x.decode() if isinstance(x, bytes) else x


def read_trials(f):
    tr = f["intervals/trials"]
    df = pd.DataFrame({c: tr[c][:] for c in tr.attrs["colnames"]})
    for c in df.columns:
        if df[c].dtype == object:
            df[c] = df[c].map(_s)
    high = df.trial_type.eq("High-rate")
    corr = df.trial_response.eq("correct")
    inc = df.trial_response.eq("incorrect")
    # 16 Hz trials are rewarded on a random side (STAR Methods, "Behavioral task") and all carry
    # trial_type "High-rate", so the side licked cannot be recovered from the outcome; their choice is
    # left unknown. Some files store measured, non-integer rates; a rate within 0.005 Hz of 16 counts
    # as 16 Hz (a standard choice: one trial in those files).
    df["at16"] = (df.trial_pulse_rate.astype(float) - 16).abs() < 0.005
    # choice: 1 = the high-rate side, 0 = the low-rate side
    df["choice"] = np.where(corr, high.astype(float), np.where(inc, (~high).astype(float), np.nan))
    df.loc[df.at16, "choice"] = np.nan
    df["outcome"] = np.where(corr, 1.0, np.where(inc, 0.0, np.nan))
    df["use"] = df.trial_is_good & df.choice.notna()
    return df


def read_rois(f):
    ps = f["processing/Ophys/ImageSegmentation/PlaneSegmentation"]
    nt = np.array([_s(x) for x in ps["neuron_type"][:]])
    st = np.array([_s(x) for x in ps["roi_status"][:]])
    return pd.DataFrame({"neuron_type": nt, "roi_status": st, "roi_id": ps["roi_id"][:]})


def read_aligned(f, name):
    """Return (array trials x frames x rois float32, index of the event frame, frame interval s, rois)."""
    grp = f["processing/Ophys/" + name]
    keys = sorted(grp.keys(), key=lambda s: int(s.split("_")[1]))
    first = grp[keys[0]]
    st = float(first["starting_time"][()])
    # the attribute named "rate" holds the frame interval in seconds
    dt = float(first["starting_time"].attrs["rate"])
    ev = int(round(-st / dt))
    rois = first["rois"][:]
    X = np.stack([grp[k]["data"][:].astype(np.float32) for k in keys])
    # the event frame is taken from the first trial; the largest difference of any trial's
    # starting_time (and frame interval) from the first trial's is returned so the notebook can check it
    dev = max(max(abs(float(grp[k]["starting_time"][()]) - st),
                  abs(float(grp[k]["starting_time"].attrs["rate"]) - dt)) for k in keys)
    return X, ev, dt, rois, dev


def bin3(X, ev, lo=None, hi=None):
    """Non-overlapping 3-frame means aligned to frame ev.

    Bin k covers frames ev+3k .. ev+3k+2; bin -1 is the 3 frames before ev.
    Returns (array trials x bins x rois, bin indices k).
    """
    nf = X.shape[1]
    kmin = -(ev // FRAMES_PER_BIN)
    kmax = (nf - ev) // FRAMES_PER_BIN - 1
    if lo is not None:
        kmin = max(kmin, lo)
    if hi is not None:
        kmax = min(kmax, hi)
    ks = np.arange(kmin, kmax + 1)
    out = np.stack([X[:, ev + 3 * k: ev + 3 * k + 3].mean(1) for k in ks], 1)
    return out, ks


# what is kept from each alignment: (bins lo, hi) relative to the event, or None for all bins
KEEP = {
    "dFoF_firstSideTryAl": (None, None),   # choice
    "dFoF_initToneAl": (-5, -1),           # before the initiation tone
    "dFoF_stimAl_noEarlyDec": (-1, 11),    # stimulus onset to just after offset
    "dFoF_rewardAl": (-3, None),           # reward (confirmation lick, correct trials)
    "dFoF_commitIncorrAl": (-3, None),     # confirmation lick on incorrect trials
}


def load_session(asset_id, alignments=("dFoF_firstSideTryAl",), behaviour=False, means=()):
    """Load one session: trial table, ROI types of the traced ROIs and binned aligned traces.

    means: alignments for which the trial average over correct trials (frames x rois) is kept.
    """
    with open_asset(asset_id) as f:
        out = {"asset_id": asset_id}
        out["subject"] = _s(f["general/subject/subject_id"][()])
        out["mouse"] = MOUSE[out["subject"]]
        out["session_id"] = _s(f["general/session_id"][()])
        out["description"] = _s(f["session_description"][()])
        out["start"] = _s(f["session_start_time"][()])
        out["imaging_rate"] = float(f["general/optophysiology/ImagingPlane/imaging_rate"][()])
        out["trials"] = read_trials(f)
        out["trial_columns"] = [_s(c) for c in f["intervals/trials"].attrs["colnames"]]
        out["ophys_keys"] = sorted(f["processing/Ophys"].keys())
        out["behaviour_keys"] = {k: sorted(f["processing/Behavior"][k].keys()) for k in f["processing/Behavior"].keys()}
        rois = read_rois(f)
        out["rois_all"] = rois
        out["al"] = {}
        traced = None
        for name in set(alignments) | set(means):
            X, ev, dt, r, dev = read_aligned(f, name)
            if traced is None:
                traced = r
            else:
                assert np.array_equal(traced, r)
            info = {"ev": ev, "dt": dt, "nframes": X.shape[1], "start_dev": dev,
                    "nan_trials": np.isnan(X).all(axis=(1, 2)),
                    "max": np.nanmax(X, axis=(0, 1))}
            if name in alignments:
                lo, hi = KEEP.get(name, (None, None))
                info["B"], info["k"] = bin3(X, ev, lo, hi)
                if name == "dFoF_firstSideTryAl":
                    # frames from 7 before to 10 after the choice frame (Figure S3C window readings)
                    a, b = max(ev - 7, 0), min(ev + 11, X.shape[1])
                    info["frames"] = X[:, a:b].copy()
                    info["frames_t"] = (np.arange(a, b) - ev) * dt
            if name in means:
                m = out["trials"].outcome.eq(1).to_numpy() & ~info["nan_trials"]
                info["mean_corr"] = np.nanmean(X[m], 0)
            out["al"][name] = info
            del X
        out["roi_index"] = traced
        out["type"] = rois.neuron_type.to_numpy()[traced]
        out["status"] = rois.roi_status.to_numpy()[traced]
        if behaviour:
            b = f["processing/Behavior/Epoched_behavioral_series"]
            # kept: licks in the 250 ms and the wheel in the 200 ms before the choice
            lt = b["firstSideTryAl_lick/timestamps"][:]
            m = (lt >= -0.25) & (lt < 0)
            out["lick"] = b["firstSideTryAl_lick/data"][m, :]
            out["lick_t"] = lt[m]
            out["lick_range"] = (float(np.nanmin(lt)), float(np.nanmax(lt)))
            wt = b["firstSideTryAl_wheelRev/timestamps"][:]
            m = (wt >= -0.2) & (wt <= 0.0001)
            out["wheel"] = b["firstSideTryAl_wheelRev/data"][m, :]
            out["wheel_t"] = wt[m]
    return out


def load_all(table, workers=6, **kw):
    """Load every session of an asset table in parallel threads (network bound)."""
    with cf.ThreadPoolExecutor(workers) as ex:
        res = list(ex.map(lambda a: load_session(a, **kw), table.asset_id))
    return res


# ---------------------------------------------------------------- single neurons

def auc_matrix(x, y):
    """AUC per column of x (trials x neurons) for labels y (1 positive), ties counted half."""
    from scipy.stats import rankdata
    r = rankdata(x, axis=0)
    n1 = y.sum()
    n0 = len(y) - n1
    return (r[y == 1].sum(0) - n1 * (n1 + 1) / 2) / (n1 * n0)


def roc_selective(x, y, rng, nshuf=50):
    """AUC, selectivity and significance per neuron (claims file, opening comment).

    Returns auc, selectivity 2|AUC-0.5|, significant (normal-fit rule), empirical p
    (two-sided, fraction of shuffles at least as far from 0.5).
    """
    auc = auc_matrix(x, y)
    sh = np.stack([auc_matrix(x, rng.permutation(y)) for _ in range(nshuf)])
    mu, sd = sh.mean(0), sh.std(0, ddof=1)
    with np.errstate(divide="ignore", invalid="ignore"):
        z = (auc - mu) / sd
    # normpdf(auc)/normpdf(mu) = exp(-z^2/2) <= 0.05
    sig = np.exp(-z**2 / 2) <= 0.05
    emp = (np.abs(sh - 0.5) >= np.abs(auc - 0.5)).mean(0)
    return auc, 2 * np.abs(auc - 0.5), sig, emp


# ---------------------------------------------------------------- decoders

CGRID = 10 ** np.arange(-6, 6.0001, 0.2)


def zscore(X):
    """z-score each neuron over trials, with 5e-4 added to the SD (claims file, code)."""
    return (X - X.mean(0)) / (X.std(0) + 5e-4)


def balanced_index(y, rng):
    """Subsample the larger class so both choices have equal numbers."""
    i0 = np.flatnonzero(y == 0)
    i1 = np.flatnonzero(y == 1)
    n = min(len(i0), len(i1))
    return np.sort(np.concatenate([rng.choice(i0, n, replace=False), rng.choice(i1, n, replace=False)]))


def svm_cv(X, y, rng, nrep=50, cgrid=CGRID, extra_test=None, shuffle_trials=None):
    """The paper's decoder at one bin.

    X trials x neurons (already z-scored), y labels 0/1 (already balanced).
    For each of nrep random 90/10 splits and each C (cgrid / n_trials), fit LinearSVC and
    record test error; the C with minimum mean test error is chosen, and the returned
    accuracy is the mean over splits at that C (Methods, "smallest error").
    The shuffled control scores the same predictions against permuted test labels.
    extra_test: optional (Xe, ye) scored at every split with the training-set decoder
    (incorrect trials, Figure S6D).
    shuffle_trials: callable(Xtrain, ytrain, rng) -> Xtrain, to build pseudo populations.
    Returns a dict.
    """
    from sklearn.svm import LinearSVC
    import warnings
    from sklearn.exceptions import ConvergenceWarning
    warnings.filterwarnings("ignore", category=ConvergenceWarning)
    n = len(y)
    ntest = max(1, int(round(0.1 * n)))
    nc = len(cgrid)
    err = np.zeros((nrep, nc))
    errsh = np.zeros((nrep, nc))
    errx = np.zeros((nrep, nc)) if extra_test is not None else None
    W = np.zeros((nrep, nc, X.shape[1]))
    B0 = np.zeros((nrep, nc))
    errxsh = np.zeros((nrep, nc))
    TE = []
    for r in range(nrep):
        perm = rng.permutation(n)
        te, trn = perm[:ntest], perm[ntest:]
        TE.append(te)
        Xr = shuffle_trials(X, y, rng) if shuffle_trials is not None else X
        Xtr, ytr = Xr[trn], y[trn]
        yperm = rng.permutation(y[te])
        if extra_test is not None:
            yxperm = rng.permutation(extra_test[1])
        for j, c in enumerate(cgrid):
            # max_iter 1000: a standard choice; at the largest C the fit stops before full convergence
            m = LinearSVC(C=c / n, loss="squared_hinge", penalty="l2", dual=True, max_iter=1000, tol=1e-4)
            if len(np.unique(ytr)) < 2:
                err[r, j] = np.nan
                continue
            m.fit(Xtr, ytr)
            p = m.predict(Xr[te])
            err[r, j] = np.mean(p != y[te])
            errsh[r, j] = np.mean(p != yperm)
            W[r, j] = m.coef_[0]
            B0[r, j] = m.intercept_[0]
            if extra_test is not None:
                px = m.predict(extra_test[0])
                errx[r, j] = np.mean(px != extra_test[1])
                errxsh[r, j] = np.mean(px != yxperm)
    me = np.nanmean(err, 0)
    jb = int(np.nanargmin(me))
    out = {"acc": 100 * (1 - me[jb]), "acc_sh": 100 * (1 - errsh[:, jb].mean()),
           "acc_reps": 100 * (1 - err[:, jb]), "acc_sh_reps": 100 * (1 - errsh[:, jb]),
           "C": cgrid[jb] / n, "w": W[:, jb].mean(0), "ntrials": n,
           "W": W[:, jb], "b": B0[:, jb], "te": TE}
    if errx is not None:
        out["acc_extra"] = 100 * (1 - errx[:, jb].mean())
        out["acc_extra_sh"] = 100 * (1 - errxsh[:, jb].mean())
    return out


def test_other_bins(res, Xbins, y):
    """Accuracy (percent) per repetition and bin of the decoders of res (trained at one bin) tested on
    the held-out trials of each repetition at other bins. Xbins: trials x bins x neurons."""
    nrep = len(res["te"])
    acc = np.zeros((nrep, Xbins.shape[1]))
    for r, te in enumerate(res["te"]):
        p = (Xbins[te] @ res["W"][r] + res["b"][r]) > 0
        acc[r] = 100 * (p == y[te][:, None]).mean(0)
    return acc


def pseudo_shuffle(Xtr, ytr, rng):
    """Shuffle trial order independently for each neuron within each choice (Methods, Noise correlations)."""
    Xs = Xtr.copy()
    for lab in (0, 1):
        idx = np.flatnonzero(ytr == lab)
        for j in range(Xs.shape[1]):
            Xs[idx, j] = Xtr[rng.permutation(idx), j]
    return Xs


# ---------------------------------------------------------------- correlations

def noise_corr(X, y):
    """Pearson r between neurons after subtracting each choice's mean (Methods, Noise correlations)."""
    R = X.astype(float).copy()
    for lab in np.unique(y):
        R[y == lab] -= R[y == lab].mean(0)
    with np.errstate(invalid="ignore", divide="ignore"):
        return np.corrcoef(R.T)


def mean_partner_r(C, a, b):
    """Each neuron of mask a: its mean r with the neurons of mask b (itself excluded)."""
    sub = C[np.ix_(a, b)].copy()
    ia, ib = np.flatnonzero(a), np.flatnonzero(b)
    same = ia[:, None] == ib[None, :]
    sub[same] = np.nan
    return np.nanmean(sub, 1)


def max_bin_match(med, types, nbins=50):
    """Neurons whose median activity falls in the 50-bin histogram bin holding most inhibitory neurons
    (Methods, Noise correlations; the bins span the range of the medians of both types)."""
    keep = np.isin(types, ["excitatory", "inhibitory"])
    lo, hi = np.nanmin(med[keep]), np.nanmax(med[keep])
    edges = np.linspace(lo, hi, nbins + 1)
    b = np.clip(np.digitize(med, edges) - 1, 0, nbins - 1)
    inh = types == "inhibitory"
    cnt = np.bincount(b[inh], minlength=nbins)
    mb = int(np.argmax(cnt))
    return keep & (b == mb)


# ---------------------------------------------------------------- learning

def easy_performance(tr):
    """Fraction correct on easy trials (claims file, fig8ab criterion; code
    svm_excInh_trainDecoder_eachFrame_stabAngles_setVars_behCA.py, thQStimStrength = [3]):
    wid = floor(min(max rate - 16, 16 - min rate)) / 4 over the session's rates; easy trials
    are those at 16 + 3 wid or above and below 16 - 3 wid."""
    cb = 16
    rate = tr.trial_pulse_rate.astype(float)
    wid = np.floor(min(rate.max() - cb, cb - rate.min())) / 4
    easy = (rate >= cb + 3 * wid) | (rate < cb - 3 * wid)
    t = tr[tr.use & easy]
    return t.outcome.mean(), len(t)


def early_late(perf, order):
    """Early and late days (Methods, Learning analysis): readings (a) every day below the 20th or above the
    80th percentile of performance, (b) only the run of such days at the start (early) or end (late)."""
    perf = np.asarray(perf, float)
    lo, hi = np.nanpercentile(perf, 20), np.nanpercentile(perf, 80)
    a_early = perf < lo
    a_late = perf > hi
    srt = np.argsort(order)
    b_early = np.zeros_like(a_early)
    for i in srt:
        if a_early[i]:
            b_early[i] = True
        else:
            break
    b_late = np.zeros_like(a_late)
    for i in srt[::-1]:
        if a_late[i]:
            b_late[i] = True
        else:
            break
    return {"a": (a_early, a_late), "b": (b_early, b_late)}


# ---------------------------------------------------------------- per-session measures

CHOICE = "dFoF_firstSideTryAl"
INIT = "dFoF_initToneAl"
TYPES = ("excitatory", "inhibitory")
MIN_TRIALS = 10  # per choice (claims file, opening comment; code thMinTrs = 10)


def trial_mask(s, outcome=(1,), alignment=CHOICE, no16=False):
    """Usable trials with the given outcomes (1 correct, 0 incorrect) and traces present."""
    tr = s["trials"]
    m = tr.use.to_numpy() & tr.outcome.isin(outcome).to_numpy() & ~s["al"][alignment]["nan_trials"]
    if no16:
        m &= tr.trial_pulse_rate.to_numpy() != 16
    return m


def bin_index(s, k, alignment=CHOICE):
    ks = s["al"][alignment]["k"]
    w = np.flatnonzero(ks == k)
    return int(w[0]) if len(w) else None


def roc_session(s, rng, outcome=(1,), nshuf=50, bins=None, X=None):
    """ROC of choice per neuron and bin, on trials of the given outcome, 16 Hz trials left out
    (claims file, opening comment). Returns None when a choice has fewer than 10 trials.
    bins: list of bin indices k (default all); X: optional trials x neurons array in place of bins.
    """
    m = trial_mask(s, outcome, no16=True)
    y = s["trials"].choice.to_numpy()[m].astype(int)
    if min(y.sum(), len(y) - y.sum()) < MIN_TRIALS:
        return None
    if X is None:
        a = s["al"][CHOICE]
        ks = a["k"] if bins is None else np.asarray(bins)
        idx = [int(np.flatnonzero(a["k"] == k)[0]) for k in ks]
        D = a["B"][m][:, idx, :]
    else:
        ks = np.array([0])
        D = X[m][:, None, :]
    nt, nb, nn = D.shape
    auc, sel, sig, emp = roc_selective(D.reshape(nt, nb * nn), y, rng, nshuf)
    sh = lambda v: v.reshape(nb, nn)
    return {"k": ks, "auc": sh(auc), "sel": sh(sel), "sig": sh(sig), "emp": sh(emp), "n": (int(len(y) - y.sum()), int(y.sum()))}


def corr_session(s, alignment=CHOICE, k=-1, subtract=True):
    """Noise (subtract=True) or spontaneous correlation matrix at one bin, trials with a choice."""
    m = s["trials"].use.to_numpy() & ~s["al"][alignment]["nan_trials"]
    i = bin_index(s, k, alignment)
    X = s["al"][alignment]["B"][m][:, i, :].astype(float)
    y = s["trials"].choice.to_numpy()[m]
    if subtract:
        return noise_corr(X, y)
    with np.errstate(invalid="ignore", divide="ignore"):
        return np.corrcoef(X.T)


# ---------------------------------------------------------------- per-session decoders (bin -1)

CGRID_RUN = 10 ** np.arange(-6, 6.0001, 1.0)  # coarser than the paper's steps of 0.2, for runtime (a deviation)
NSUB = 5  # excitatory subsamples (the paper's 50, reduced for runtime; a deviation)


def _xy(s, outcome, k=-1, rng=None, balance=True):
    m = trial_mask(s, outcome)
    y = s["trials"].choice.to_numpy()[m].astype(int)
    if min(y.sum(), len(y) - y.sum()) < MIN_TRIALS:
        return None
    a = s["al"][CHOICE]
    Xall = a["B"][m].astype(float)  # trials x bins x neurons
    idx = balanced_index(y, rng) if balance else np.arange(len(y))
    return Xall[idx], y[idx], m


def zscore_bins(Xb, ref=None):
    ref = Xb if ref is None else ref
    return (Xb - ref.mean(0)) / (ref.std(0) + 5e-4)


def stability(acc, kidx, train_i, nsd=2.0, se=False):
    """Stable bins of a decoder trained at bin train_i: test accuracy at least the training-bin accuracy
    minus nsd SD (or SE) across repetitions (Methods, Figure 4C). Returns (n stable bins, n contiguous)."""
    mu = acc.mean(0)
    sd = acc[:, train_i].std(ddof=1)
    if se:
        sd = sd / np.sqrt(acc.shape[0])
    st = mu >= mu[train_i] - nsd * sd
    n = int(st.sum())
    lo = train_i
    while lo - 1 >= 0 and st[lo - 1]:
        lo -= 1
    hi = train_i
    while hi + 1 < len(st) and st[hi + 1]:
        hi += 1
    return n, hi - lo + 1


def _stab_summary(acc, ti, acc_reps, sh_reps):
    from scipy import stats as st
    p1 = st.ttest_ind(acc_reps, sh_reps, alternative="greater").pvalue
    return {"sd": stability(acc, None, ti, 2, False), "se": stability(acc, None, ti, 2, True), "p_train": p1}


def decode_session(s, seed, cgrid=CGRID_RUN, nsub=NSUB, nrep=50):
    """All decoders of 02_decoders.ipynb for one session, at bin -1 (0-97 ms before choice).

    Correct trials, choices matched by random subsampling (Methods). Populations: all neurons,
    inhibitory, nsub subsamples of as many excitatory neurons, mixed (all n inhibitory + n excitatory)
    and 2n excitatory (code excInhHalf, allExc2inhSize), pseudo populations of all neurons.
    Decoders are tested on held-out correct trials, on incorrect trials (Figure S6D), and at every
    bin (stability, Figure 4). A second all-neuron decoder, real and pseudo, uses all trials with a choice.
    """
    rng = np.random.default_rng(seed)
    out = {"mouse": s["mouse"], "session": s["session_id"]}
    xy = _xy(s, (1,), rng=rng)
    if xy is None:
        return out
    Xall, y, m = xy
    a = s["al"][CHOICE]
    ti = int(np.flatnonzero(a["k"] == -1)[0])
    out["k"] = a["k"]
    Z = zscore_bins(Xall)  # trials x bins x neurons, z-scored per bin
    X = Z[:, ti]
    # incorrect trials, z-scored with the correct-trial statistics
    mi = trial_mask(s, (0,))
    yi = s["trials"].choice.to_numpy()[mi].astype(int)
    Xi = (a["B"][mi][:, ti].astype(float) - Xall[:, ti].mean(0)) / (Xall[:, ti].std(0) + 5e-4)
    extra = (Xi, yi) if len(yi) and 0 < yi.sum() < len(yi) else None
    out["n_incorr"] = (int((yi == 0).sum()), int((yi == 1).sum()))
    t = s["type"]
    E, I = np.flatnonzero(t == "excitatory"), np.flatnonzero(t == "inhibitory")
    nI = len(I)
    out["nI"], out["nE"], out["nN"], out["ntr"] = nI, len(E), len(t), len(y)

    def run(cols, shuffle=None, stab=False):
        ex = (extra[0][:, cols], extra[1]) if extra is not None else None
        r = svm_cv(X[:, cols], y, rng, nrep=nrep, cgrid=cgrid, extra_test=ex, shuffle_trials=shuffle)
        res = {k: r[k] for k in ("acc", "acc_sh", "C") if k in r}
        res["acc_inc"] = r.get("acc_extra", np.nan)
        res["acc_inc_sh"] = r.get("acc_extra_sh", np.nan)
        res["p_vs_sh"] = None
        if stab:
            acc = test_other_bins(r, Z[:, :, cols], y)
            res["stab"] = _stab_summary(acc, ti, r["acc_reps"], r["acc_sh_reps"])
            res["stab_acc"] = acc.mean(0)
        return res, r

    allr, rall = run(np.arange(len(t)))
    w = rall["w"] / np.linalg.norm(rall["w"])
    out["all"] = allr
    out["w_E"], out["w_I"] = np.abs(w[E]), np.abs(w[I])
    out["inh"], _ = run(I, stab=True)
    subs = []
    for _ in range(nsub):
        subs.append(run(rng.choice(E, nI, replace=False), stab=True)[0])
    out["exc_subs"] = subs
    if len(E) >= 2 * nI:
        mix, e2 = [], []
        for _ in range(nsub):
            ee = rng.choice(E, 2 * nI, replace=False)
            mix.append(run(np.concatenate([I, ee[:nI]]))[0]["acc"])
            e2.append(run(ee)[0]["acc"])
        out["mixed"], out["exc2n"] = mix, e2
    out["pseudo"], _ = run(np.arange(len(t)), shuffle=pseudo_shuffle)
    # all trials with a choice (fig7 second reading)
    xy2 = _xy(s, (0, 1), rng=rng)
    if xy2 is not None:
        X2, y2, _ = xy2
        Z2 = zscore_bins(X2)[:, ti]
        r1 = svm_cv(Z2, y2, rng, nrep=nrep, cgrid=cgrid)
        r2 = svm_cv(Z2, y2, rng, nrep=nrep, cgrid=cgrid, shuffle_trials=pseudo_shuffle)
        out["all_alltr"] = {"acc": r1["acc"], "acc_sh": r1["acc_sh"]}
        out["pseudo_alltr"] = {"acc": r2["acc"], "acc_sh": r2["acc_sh"]}
    # running: wheel revolutions over the bin before the choice, per used trial
    if "wheel" in s:
        wt = s["wheel_t"]
        i0, i1 = int(np.argmin(np.abs(wt + 0.097))), int(np.argmin(np.abs(wt)))
        d = s["wheel"][i1] - s["wheel"][i0]
        mm = s["trials"].use.to_numpy() & ~np.isnan(d)
        out["run"] = (d[mm], s["trials"].choice.to_numpy()[mm])
    return out


# ---------------------------------------------------------------- learning decoders (all bins)

def timecourse(Z, y, C, rng, nrep=50, return_w=False):
    """Decoders trained and tested at every bin with one C (chosen at bin -1). Z trials x bins x neurons.
    Returns accuracy and shuffled-label accuracy per repetition and bin (percent), and with return_w the
    weights per bin averaged over the repetitions (bins x neurons)."""
    from sklearn.svm import LinearSVC
    import warnings
    from sklearn.exceptions import ConvergenceWarning
    warnings.filterwarnings("ignore", category=ConvergenceWarning)
    n, nb, nn = Z.shape
    ntest = max(1, int(round(0.1 * n)))
    acc = np.zeros((nrep, nb)); sh = np.zeros((nrep, nb))
    W = np.zeros((nb, nn))
    for r in range(nrep):
        perm = rng.permutation(n)
        te, trn = perm[:ntest], perm[ntest:]
        yp = rng.permutation(y[te])
        for b in range(nb):
            m = LinearSVC(C=C, dual=True, max_iter=1000, tol=1e-4).fit(Z[trn, b], y[trn])
            p = m.predict(Z[te, b])
            acc[r, b] = 100 * np.mean(p == y[te]); sh[r, b] = 100 * np.mean(p == yp)
            W[b] += m.coef_[0] / nrep
    if return_w:
        return acc, sh, W
    return acc, sh


def timecourse_perbin(Z, y, rng, bins, nrep=50, cgrid=None):
    """The paper's decoder at each of the given bins (indices into Z's bin axis), with C chosen at that bin
    by svm_cv (claims file, opening comment: C chosen separately per bin, 50 splits). Returns mean accuracy
    and mean shuffled accuracy per bin (percent)."""
    cgrid = CGRID_RUN if cgrid is None else cgrid
    acc, sh = [], []
    for b in bins:
        r = svm_cv(Z[:, b], y, rng, nrep=nrep, cgrid=cgrid)
        acc.append(r["acc"]); sh.append(r["acc_sh"])
    return np.array(acc), np.array(sh)


def onset(acc, sh, ks, alpha=0.05, run=5):
    """Choice-signal onset (Methods, Learning analysis): start of the first run of at least `run` bins
    (500 ms; code th1) where accuracy differs from the shuffle by a t-test across repetitions."""
    from scipy import stats as st
    p = st.ttest_ind(acc, sh, axis=0).pvalue
    sig = (p < alpha) & (acc.mean(0) > sh.mean(0))
    c = 0
    for i, v in enumerate(sig):
        c = c + 1 if v else 0
        if c >= run:
            return float(ks[i - run + 1] * 97)
    return np.nan


def _eq_corr_incorr(s, rng):
    """Reading (b) of fig8ab: equal numbers of correct and incorrect trials within each choice, then
    equal numbers of choices (code decodeChoiceEqCorrIncorr)."""
    tr = s["trials"]
    m = trial_mask(s, (0, 1))
    ch, oc = tr.choice.to_numpy(), tr.outcome.to_numpy()
    pick = {}
    for c in (0, 1):
        ic = np.flatnonzero(m & (ch == c) & (oc == 1)); ii = np.flatnonzero(m & (ch == c) & (oc == 0))
        pick[c] = (ic, ii, min(len(ic), len(ii)))
    n = min(pick[0][2], pick[1][2])
    if 2 * n < MIN_TRIALS:
        return None
    idx = np.sort(np.concatenate([np.concatenate([rng.choice(pick[c][0], n, replace=False), rng.choice(pick[c][1], n, replace=False)]) for c in (0, 1)]))
    return idx


def learn_session(s, seed, n_equal=None, cgrid=CGRID_RUN, nsub=3, nrep=50, learning=True, nrep_tc=25):
    """Decoders of 03_learning_decoders.ipynb for one session.

    Always: the all-neuron decoder on correct trials at every bin (fig3b), C chosen at bin -1.
    For learning mice (learning=True): readings (a) all trials with a choice and (b) equal correct and
    incorrect trials within each choice; all neurons, inhibitory and nsub excitatory subsamples; accuracy
    at bin -1 with C by the paper's rule, then every bin at that C for the onset; pseudo populations at
    bin -1 for reading (a); and the all-neuron decoder on n_equal correct trials of each choice (fig S13C).
    The time courses use nrep_tc = 25 random splits per bin (the paper 50; for runtime, a deviation).
    """
    rng = np.random.default_rng(seed)
    out = {"mouse": s["mouse"], "session": s["session_id"]}
    a = s["al"][CHOICE]
    ks = a["k"]; ti = int(np.flatnonzero(ks == -1)[0])
    out["k"] = ks
    t = s["type"]
    E, I = np.flatnonzero(t == "excitatory"), np.flatnonzero(t == "inhibitory")
    xy = _xy(s, (1,), rng=rng)
    if xy is not None:
        Z = zscore_bins(xy[0]); y = xy[1]
        r = svm_cv(Z[:, ti], y, rng, nrep=nrep, cgrid=cgrid)
        acc, sh, W = timecourse(Z, y, r["C"], rng, nrep_tc, return_w=True)
        out["tc_corr"] = (acc.mean(0), sh.mean(0))
        # fig3df per bin: |w| of the unit-length weight vector of each bin, by cell type
        Wn = np.abs(W) / np.linalg.norm(W, axis=1, keepdims=True)
        out["w_bins"] = (Wn[:, E].mean(1), Wn[:, I].mean(1))
    if not learning:
        return out
    tr = s["trials"]
    sets = {}
    xa = _xy(s, (0, 1), rng=rng)
    if xa is not None:
        sets["a"] = (zscore_bins(xa[0]), xa[1])
    ib = _eq_corr_incorr(s, rng)
    if ib is not None:
        sets["b"] = (zscore_bins(a["B"][ib].astype(float)), tr.choice.to_numpy()[ib].astype(int))
    for rd, (Z, y) in sets.items():
        pops = {"all": np.arange(len(t)), "inh": I}
        for j in range(nsub):
            pops[f"exc{j}"] = rng.choice(E, len(I), replace=False)
        res = {}
        for p, cols in pops.items():
            r = svm_cv(Z[:, ti][:, cols], y, rng, nrep=nrep, cgrid=cgrid)
            acc, sh = timecourse(Z[:, :, cols], y, r["C"], rng, nrep_tc)
            res[p] = {"acc": r["acc"], "acc_sh": r["acc_sh"], "on05": onset(acc, sh, ks, 0.05), "on001": onset(acc, sh, ks, 0.001)}
            if rd == "a":
                rp = svm_cv(Z[:, ti][:, cols], y, rng, nrep=nrep, cgrid=cgrid, shuffle_trials=pseudo_shuffle)
                res[p]["pseudo"] = rp["acc"]
        out[rd] = res
        out["ntr_" + rd] = len(y)
    if n_equal is not None:
        m = trial_mask(s, (1,))
        ch = tr.choice.to_numpy()
        i0, i1 = np.flatnonzero(m & (ch == 0)), np.flatnonzero(m & (ch == 1))
        if min(len(i0), len(i1)) >= n_equal:
            idx = np.sort(np.concatenate([rng.choice(i0, n_equal, replace=False), rng.choice(i1, n_equal, replace=False)]))
            Z = zscore_bins(a["B"][idx][:, [ti]].astype(float))[:, 0]
            r = svm_cv(Z, ch[idx].astype(int), rng, nrep=nrep, cgrid=cgrid)
            out["equal"] = {"acc": r["acc"], "acc_sh": r["acc_sh"], "n": n_equal}
    return out
