"""Loading and measures for dandiset 000252 (Guan et al., ten-finger press task).

The dandiset holds the ten-finger press task only: 10 sessions of participant N
(subject ``P1`` in the files, one PPC array) and 2 sessions of participant J
(subject ``N1`` in the files, a PPC and an MC array). Files are streamed from the
DANDI archive at the pinned version ``VERSION``; nothing is written to disk.

Where each parameter comes from:

- Firing rate is the spike count in a 500 ms window divided by its duration;
  the Go window starts 200 ms after the Go cue, the Delay window 200 ms after the
  Delay screen, the Cue window 200 ms after the Cue screen, and the ITI window is
  the last 500 ms of the ITI (paper, Methods, Feature Extraction). The Delay
  screen onset is the file's ``cue_off_time`` (the cue disappears at the start of
  the delay; Methods, Tasks, and Figure 3 legend: "A delay period separates the
  Cue phase from a condition-independent Go display").
- Neurons with mean rate below 0.5 Hz are excluded (Methods, Feature Extraction).
  Readings of "average firing rate" are claims-file O1: (a) spikes over the whole
  recorded session (the sum of the unit's ``obs_intervals``); (b) the mean of the
  Go-window rates over all trials. For (b) the Go window is taken as "the analysis
  window", since every ten-finger analysis uses it (claims file O11); this is a
  reading of O1 (b), stated as such.
- The classifier is diagonal-covariance LDA, one per session, stratified 8-fold
  cross-validation, predictions pooled over sessions (Methods, Offline
  classification with cross-validation). Fold assignment is claims-file O2: (a) no
  shuffling, (b) shuffled, seeds 0 to 9. The variance floor of 1e-9 times the
  largest variance (as scikit-learn's GaussianNB) is a standard choice that only
  guards against division by zero.
- Single-neuron selectivity is a one-way ANOVA, Benjamini-Hochberg FDR over the
  neurons of an array pooled across sessions, eta2 = between-group over total sum
  of squares (Methods, Single-neuron selectivity).
- Cross-validated Mahalanobis distances use rsatoolbox (Methods, Neural distance
  between fingers), which divides by the number of neurons. Readings are
  claims-file O3 (noise covariance estimator) and O4 (partition).
- CCGP pseudo-populations and decoders are claims-file O6 and O7; the permutation
  test uses 1001 label shuffles (Methods, Compositionality of finger
  representations).
"""

from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")

from dataclasses import dataclass, field

import h5py
import numpy as np
import pandas as pd
import remfile
import requests

DANDISET_ID = "000252"
VERSION = "0.230408.2207"
API = "https://api.dandiarchive.org/api"

# Paper names of the participants and arrays, and the file's subject and group.
ARRAYS = {"N-PPC": ("P1", "PPC"), "J-PPC": ("N1", "PPC"), "J-MC": ("N1", "MC")}
FINGER_TYPES = ["t", "i", "m", "r", "p"]
CONDITIONS = [h + f for h in "RL" for f in FINGER_TYPES]  # Rt..Rp, Lt..Lp

WINDOW = 0.5      # s, Methods, Feature Extraction
OFFSET = 0.2      # s, after the phase onset, Methods, Feature Extraction
MIN_RATE = 0.5    # Hz, Methods, Feature Extraction


def list_assets() -> list[dict]:
    """Assets of the pinned version, sorted by path."""
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{VERSION}/assets/?page_size=200"
    out = []
    while url:
        page = requests.get(url, timeout=60).json()
        out += page["results"]
        url = page.get("next")
    return sorted(out, key=lambda a: a["path"])


def version_metadata() -> dict:
    return requests.get(f"{API}/dandisets/{DANDISET_ID}/versions/{VERSION}/", timeout=60).json()


def s3_url(asset_id: str) -> str:
    r = requests.get(f"{API}/assets/{asset_id}/download/", allow_redirects=False, timeout=60)
    return r.headers["Location"]


@dataclass
class Session:
    path: str
    subject: str
    sex: str
    date: str
    description: str
    trials: pd.DataFrame
    spikes: list            # one sorted array of spike times per unit (s)
    group: np.ndarray       # electrode group name per unit
    obs_duration: np.ndarray  # total observed time per unit (s)
    n_unsorted: int = 0     # units whose stored spike times are not in time order
    n_outside_obs: int = 0  # spikes outside the unit's obs_intervals
    extra: dict = field(default_factory=dict)


def _s(x):
    return x.decode() if isinstance(x, bytes) else str(x)


def load_session(asset: dict) -> Session:
    """Stream one NWB file and keep trials, spike times, groups and observed time."""
    f = h5py.File(remfile.File(s3_url(asset["asset_id"])), "r")
    t = f["intervals/trials"]
    cols = ["Run", "TrialNumber", "finger", "hand", "finger_type", "start_time",
            "stop_time", "cue_on_time", "cue_off_time", "go_on_time"]
    trials = pd.DataFrame({c: t[c][:] for c in cols})
    for c in ["finger", "hand", "finger_type"]:
        trials[c] = [_s(v) for v in trials[c]]
    st = f["units/spike_times"][:]
    idx = f["units/spike_times_index"][:]
    oi = f["units/obs_intervals"][:]
    oidx = f["units/obs_intervals_index"][:]
    groups_ref = f["units/electrode_group"][:]
    group = np.array([f[r].name.split("/")[-1] for r in groups_ref])
    starts = np.r_[0, idx[:-1]]
    ostarts = np.r_[0, oidx[:-1]]
    spikes, obs, n_unsorted, n_out = [], [], 0, 0
    for i, (s, e) in enumerate(zip(starts, idx)):
        x = st[s:e]
        if np.any(np.diff(x) < 0):
            n_unsorted += 1
        x = np.sort(x)
        iv = oi[ostarts[i]:oidx[i]]
        inside = np.zeros(len(x), bool)
        for a, b in iv:
            inside |= (x >= a) & (x <= b)
        n_out += int((~inside).sum())
        spikes.append(x)
        obs.append(float(np.sum(iv[:, 1] - iv[:, 0])))
    subj = f["general/subject"]
    sess = Session(
        path=asset["path"],
        subject=_s(subj["subject_id"][()]),
        sex=_s(subj["sex"][()]),
        date=_s(f["general/session_id"][()]),
        description=_s(f["session_description"][()]),
        trials=trials,
        spikes=spikes,
        group=group,
        obs_duration=np.array(obs),
        n_unsorted=n_unsorted,
        n_outside_obs=n_out,
    )
    sess.extra["electrode_groups"] = pd.Series(
        [_s(v) for v in f["general/extracellular_ephys/electrodes/group_name"][:]]
    ).value_counts().to_dict()
    sess.extra["electrode_locations"] = sorted(
        {_s(v) for v in f["general/extracellular_ephys/electrodes/location"][:]})
    sess.extra["epochs"] = len(f["intervals/epochs/start_time"])
    f.close()
    return sess


def load_all() -> list[Session]:
    return [load_session(a) for a in list_assets()]


def counts(spikes: list, align: np.ndarray, start: float = OFFSET, dur: float = WINDOW) -> np.ndarray:
    """Spike counts (trials x units) in [align + start, align + start + dur)."""
    lo, hi = align + start, align + start + dur
    out = np.empty((len(align), len(spikes)))
    for j, x in enumerate(spikes):
        out[:, j] = np.searchsorted(x, hi) - np.searchsorted(x, lo)
    return out


def rates(sess: Session, window: str = "go", dur: float = WINDOW, start: float = OFFSET) -> np.ndarray:
    """Firing rates (trials x units, Hz) in an analysis window (Methods, Feature Extraction)."""
    tr = sess.trials
    if window == "go":
        align = tr.go_on_time.values
    elif window == "delay":
        align = tr.cue_off_time.values
    elif window == "cue":
        align = tr.cue_on_time.values
    elif window == "iti":
        align, start = tr.cue_on_time.values, -dur
    else:
        raise ValueError(window)
    return counts(sess.spikes, align, start, dur) / dur


def keep_mask(sess: Session, reading: str) -> np.ndarray:
    """Units kept by the 0.5 Hz exclusion under a reading of claims-file O1 ('none', 'a', 'b')."""
    n = len(sess.spikes)
    if reading == "none":
        return np.ones(n, bool)
    if reading == "a":
        total = np.array([len(x) for x in sess.spikes])
        return total / sess.obs_duration >= MIN_RATE
    if reading == "b":
        return rates(sess, "go").mean(axis=0) >= MIN_RATE
    raise ValueError(reading)


def array_data(sess: Session, array: str, o1: str, window: str = "go", **kw):
    """Rates (trials x kept units) of one array, and condition labels."""
    _, grp = ARRAYS[array]
    m = (sess.group == grp) & keep_mask(sess, o1)
    X = rates(sess, window, **kw)[:, m]
    y = sess.trials.finger.values
    return X, y


# ---------------------------------------------------------------- classifier

class DiagLDA:
    """Diagonal-covariance LDA: class means, one variance per feature pooled over
    classes (Methods, Offline classification: Gaussian naive Bayes with a single
    shared covariance)."""

    def fit(self, X, y):
        self.classes_ = np.unique(y)
        self.mu_ = np.array([X[y == c].mean(axis=0) for c in self.classes_])
        resid = X - self.mu_[np.searchsorted(self.classes_, y)]
        dof = max(len(y) - len(self.classes_), 1)
        var = (resid ** 2).sum(axis=0) / dof
        var = var + 1e-9 * max(var.max(), 1e-12)  # standard floor (as GaussianNB)
        self.var_ = var
        self.logprior_ = np.log(np.array([(y == c).mean() for c in self.classes_]))
        return self

    def decision_function(self, X):
        d = ((X[:, None, :] - self.mu_[None]) ** 2 / self.var_).sum(axis=2)
        return -0.5 * d + self.logprior_

    def predict(self, X):
        return self.classes_[np.argmax(self.decision_function(X), axis=1)]


def make_decoder(kind: str):
    """Linear decoder of claims-file O7: 'lda' (diagonal LDA) or 'svm' (linear SVM on
    z-scored rates; C = 1 is scikit-learn's default, a standard choice)."""
    if kind == "lda":
        return DiagLDA()
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler
    from sklearn.svm import LinearSVC
    return make_pipeline(StandardScaler(), LinearSVC(C=1.0, dual="auto", max_iter=20000))


def cv_predict(X, y, o2: str = "a", seed: int = 0, decoder: str = "lda", k: int = 8):
    """Stratified k-fold predictions on held-out trials (Methods, K = 8).
    o2 'a': folds in trial order; 'b': shuffled with the given seed."""
    from sklearn.model_selection import StratifiedKFold
    skf = StratifiedKFold(k, shuffle=(o2 == "b"), random_state=seed if o2 == "b" else None)
    pred = np.empty(len(y), dtype=object)
    for tr, te in skf.split(X, y):
        pred[te] = make_decoder(decoder).fit(X[tr], y[tr]).predict(X[te])
    return pred


def error_kinds(true, pred):
    """Counts of errors that are adjacent (same hand, neighbouring finger in t,i,m,r,p)
    or matching (same finger type, other hand)."""
    err = true != pred
    adj = match = 0
    for t, p in zip(true[err], pred[err]):
        ft, fp = FINGER_TYPES.index(t[1]), FINGER_TYPES.index(p[1])
        if t[0] == p[0] and abs(ft - fp) == 1:
            adj += 1
        elif t[0] != p[0] and ft == fp:
            match += 1
    return int(err.sum()), adj, match


# ---------------------------------------------------------------- selectivity

def anova_eta2(X, y):
    """One-way ANOVA per unit across conditions; returns p (NaN for a constant unit) and eta2."""
    from scipy.stats import f_oneway
    groups = [X[y == c] for c in np.unique(y)]
    p = np.full(X.shape[1], np.nan)
    eta = np.full(X.shape[1], np.nan)
    grand = X.mean(axis=0)
    sst = ((X - grand) ** 2).sum(axis=0)
    ssb = sum(len(g) * (g.mean(axis=0) - grand) ** 2 for g in groups)
    ok = sst > 0
    if ok.any():
        p[ok] = f_oneway(*[g[:, ok] for g in groups]).pvalue
        eta[ok] = ssb[ok] / sst[ok]
    return p, eta


def fdr_bh(p):
    """Benjamini-Hochberg adjusted p (q); NaN p (constant units) are kept as not significant
    but counted in m, the number of neurons (Methods: m = N)."""
    p = np.asarray(p, float)
    m = len(p)
    pp = np.where(np.isnan(p), 1.0, p)
    order = np.argsort(pp)
    q = pp[order] * m / np.arange(1, m + 1)
    q = np.minimum.accumulate(q[::-1])[::-1]
    out = np.empty(m)
    out[order] = np.minimum(q, 1)
    return out


# ---------------------------------------------------------------- distances

def _resid(Xs, ys):
    mu = {c: Xs[ys == c].mean(axis=0) for c in np.unique(ys)}
    return Xs - np.array([mu[c] for c in ys]), len(ys) - len(mu)


def crossnobis_rdm(X, y, o3: str = "shrinkage_diag", o4: str = "a"):
    """10 x 10 cross-validated squared Mahalanobis distances (rsatoolbox), rows/cols CONDITIONS.
    Returns the matrix and the number of units dropped for zero residual variance.

    o3: noise covariance estimator of rsatoolbox ('shrinkage_diag', 'shrinkage_eye', 'diag').
    o4 'a': two partitions A and B (odd and even repetitions of each condition), each with
    the noise precision of its own trials, combined as rsatoolbox does for a list of noises
    (Methods: "incorporating the noise covariances of both folds"). For a list of noises,
    rsatoolbox's calc_rdm_crossnobis documents that each "is the precision of the mean from
    the corresponding crossvalidation fold, i.e. if multiple measurements enter a fold, please
    compute the resulting noise precision in advance", so the single-trial precision is
    multiplied by the number of trials per condition in the fold (5). This follows the
    toolbox the paper names (Methods, ref 57); it is an assumption about how the paper called
    it. o4 'a1': the same, with the single-trial precision passed unscaled (a variant).
    o4 'b': leave one repetition out, one single-trial precision from all residuals.

    Units with zero residual variance in a partition (no spikes, or the same count, in every
    trial of it) make the covariance singular and are dropped from that session's distance;
    the count is returned."""
    import rsatoolbox
    from rsatoolbox.data.noise import prec_from_residuals
    rep = np.zeros(len(y), int)
    for c in np.unique(y):
        rep[y == c] = np.arange((y == c).sum())
    half = rep % 2
    ok = np.ones(X.shape[1], bool)
    for h in (0, 1):
        r, _ = _resid(X[half == h], y[half == h])
        ok &= r.var(axis=0) > 0
    X = X[:, ok]
    cond_idx = np.array([CONDITIONS.index(c) for c in y])

    if o4 in ("a", "a1"):
        noises = []
        for h in (0, 1):
            r, dof = _resid(X[half == h], y[half == h])
            n_per = (half == h).sum() / len(np.unique(y[half == h]))
            prec = prec_from_residuals(r, dof=dof, method=o3)
            noises.append(prec * n_per if o4 == "a" else prec)
        cv, noise = half, noises
    else:
        r, dof = _resid(X, y)
        cv, noise = rep, prec_from_residuals(r, dof=dof, method=o3)
    ds = rsatoolbox.data.Dataset(X, obs_descriptors={"cond": cond_idx, "cv": cv})
    rdm = rsatoolbox.rdm.calc_rdm(ds, method="crossnobis", descriptor="cond",
                                  cv_descriptor="cv", noise=noise)
    return rdm.get_matrices()[0], int((~ok).sum())


def cross_hand_elements(rdm: np.ndarray):
    """Matching (5) and non-matching (20) different-hand elements (Methods, Shared
    representations across hands)."""
    match, non = [], []
    for i, f1 in enumerate(FINGER_TYPES):
        for j, f2 in enumerate(FINGER_TYPES):
            d = rdm[i, 5 + j]
            (match if i == j else non).append(d)
    return np.array(match), np.array(non)


# ---------------------------------------------------------------- CCGP

def pseudo_population(sessions_X: list, sessions_y: list, o6: str, rng=None):
    """Stack neurons of several sessions into pseudo-trials of each condition.
    o6 'a': trials matched by repetition index within condition; 'b': matched at random
    within condition (one draw; callers repeat it)."""
    n_rep = min(min((y == c).sum() for c in CONDITIONS) for y in sessions_y)
    blocks = []
    for X, y in zip(sessions_X, sessions_y):
        rows = []
        for c in CONDITIONS:
            ix = np.flatnonzero(y == c)[:n_rep] if o6 == "a" else rng.permutation(np.flatnonzero(y == c))[:n_rep]
            rows.append(X[ix])
        blocks.append(np.concatenate(rows))
    labels = np.repeat(CONDITIONS, n_rep)
    return np.concatenate(blocks, axis=1), labels


def ccgp_hand(X, cond, decoder="lda"):
    """Left-vs-right decoder trained on 4 finger types, tested on the held-out one; mean of 5 folds."""
    hand = np.array([c[0] for c in cond])
    ft = np.array([c[1] for c in cond])
    acc = []
    for f in FINGER_TYPES:
        te = ft == f
        m = make_decoder(decoder).fit(X[~te], hand[~te])
        acc.append(np.mean(m.predict(X[te]) == hand[te]))
    return float(np.mean(acc))


def ccgp_finger(X, cond, decoder="lda"):
    """5-class finger-type decoder trained on one hand, tested on the other; mean of both directions."""
    hand = np.array([c[0] for c in cond])
    ft = np.array([c[1] for c in cond])
    acc = []
    for h in "RL":
        tr = hand == h
        m = make_decoder(decoder).fit(X[tr], ft[tr])
        acc.append(np.mean(m.predict(X[~tr]) == ft[~tr]))
    return float(np.mean(acc))


def standard_accuracy(X, cond, target, decoder="lda", o2="a", seed=0):
    """Cross-validated (stratified 8-fold) accuracy without leaving conditions out.
    target 'hand'; 'finger_within' (claims-file O8 a, per hand, mean of hands);
    'finger_both' (O8 b, finger type over both hands)."""
    hand = np.array([c[0] for c in cond])
    ft = np.array([c[1] for c in cond])
    if target == "hand":
        return float(np.mean(cv_predict(X, hand, o2, seed, decoder) == hand))
    if target == "finger_both":
        return float(np.mean(cv_predict(X, ft, o2, seed, decoder) == ft))
    accs = []
    for h in "RL":
        m = hand == h
        accs.append(np.mean(cv_predict(X[m], ft[m], o2, seed, decoder) == ft[m]))
    return float(np.mean(accs))


def shuffle_conditions(cond, rng):
    """A label shuffle for the permutation test: condition labels permuted across pseudo-trials."""
    return rng.permutation(cond)


N_SHUFFLES = 1001     # Methods, Compositionality of finger representations
N_PAIRINGS = 100      # claims-file O6 (b): random pseudo-trial matchings averaged


def run_ccgp(Xs: list, ys: list, o6: str, decoder: str, rng, n_shuffles: int = N_SHUFFLES):
    """Hand and finger-type CCGP, standard accuracies and permutation p-values on a
    pseudo-population. For o6 'b' the observed values are averaged over N_PAIRINGS random
    matchings, and each shuffle of the null uses a fresh matching (an assumption: the
    paper does not say how its null treats the pseudo-trials). p = (1 + #null >= observed)
    / (1 + n_shuffles)."""
    pairings = 1 if o6 == "a" else N_PAIRINGS
    obs = {k: [] for k in ["hand", "finger", "std_hand", "std_within", "std_both"]}
    for _ in range(pairings):
        X, c = pseudo_population(Xs, ys, o6, rng)
        obs["hand"].append(ccgp_hand(X, c, decoder))
        obs["finger"].append(ccgp_finger(X, c, decoder))
        obs["std_hand"].append(standard_accuracy(X, c, "hand", decoder))
        obs["std_within"].append(standard_accuracy(X, c, "finger_within", decoder))
        obs["std_both"].append(standard_accuracy(X, c, "finger_both", decoder))
    out = {k: float(np.mean(v)) for k, v in obs.items()}
    null_h, null_f = [], []
    X, c = pseudo_population(Xs, ys, o6, rng)
    for _ in range(n_shuffles):
        if o6 == "b":
            X, c = pseudo_population(Xs, ys, o6, rng)
        cs = shuffle_conditions(c, rng)
        null_h.append(ccgp_hand(X, cs, decoder))
        null_f.append(ccgp_finger(X, cs, decoder))
    null_h, null_f = np.array(null_h), np.array(null_f)
    out["p_hand"] = float((1 + (null_h >= out["hand"]).sum()) / (1 + n_shuffles))
    out["p_finger"] = float((1 + (null_f >= out["finger"]).sum()) / (1 + n_shuffles))
    out["n_null_ge_hand"] = int((null_h >= out["hand"]).sum())
    out["n_null_ge_finger"] = int((null_f >= out["finger"]).sum())
    out["null_hand_mean"], out["null_hand_max"] = float(null_h.mean()), float(null_h.max())
    out["null_finger_mean"], out["null_finger_max"] = float(null_f.mean()), float(null_f.max())
    out["n_neurons"] = int(sum(x.shape[1] for x in Xs))
    return out


def ndc_finger(Xs: list, ys: list, sizes, n_sub: int, o6: str, decoder: str, rng):
    """Finger-type CCGP for random subsets of the pooled neurons (Methods, Offline
    classification: neuron-dropping curves from random subsets of neurons stacked across
    sessions). For o6 'b' each subset gets a fresh random matching."""
    X, c = pseudo_population(Xs, ys, o6, rng)
    res = {}
    for n in sizes:
        v = []
        for _ in range(n_sub):
            if o6 == "b":
                X, c = pseudo_population(Xs, ys, o6, rng)
            cols = rng.choice(X.shape[1], n, replace=False)
            v.append(ccgp_finger(X[:, cols], c, decoder))
        res[n] = (float(np.mean(v)), float(np.std(v)))
    return res


def classical_mds(D2: np.ndarray, k: int = 2) -> np.ndarray:
    """Classical MDS of squared distances (negative cross-validated values clipped at 0)."""
    D2 = np.clip(D2, 0, None)
    n = len(D2)
    J = np.eye(n) - 1 / n
    B = -0.5 * J @ D2 @ J
    w, v = np.linalg.eigh(B)
    i = np.argsort(w)[::-1][:k]
    return v[:, i] * np.sqrt(np.clip(w[i], 0, None))


def gpa(configs: list, n_iter: int = 20) -> list:
    """Generalized Procrustes analysis with scaling: each configuration centred and
    rotated/scaled to the running mean (used only to draw Figure 8d)."""
    from scipy.linalg import orthogonal_procrustes
    Y = [c - c.mean(axis=0) for c in configs]
    Y = [y / np.linalg.norm(y) for y in Y]
    ref = Y[0]
    for _ in range(n_iter):
        out = []
        for y in Y:
            R, s = orthogonal_procrustes(y, ref)
            out.append(y @ R * s / (np.linalg.norm(y) ** 2))
        ref = np.mean(out, axis=0)
        ref = ref / np.linalg.norm(ref)
    return out
