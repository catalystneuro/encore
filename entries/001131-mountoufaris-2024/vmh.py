"""Loading and measures for the miniscope ("CRISPRoscopy") data of dandiset 001131.

Mountoufaris, Nair, Yang, Kim, Vinograd, Kim, Linderman & Anderson (2024), Cell 187, 5998-6015,
doi:10.1016/j.cell.2024.08.015.

Each NWB file holds one male resident imaged in VMHvl during the resident-intruder assay: a
frames x units trace (`processing/ophys/NeuralTrace`, 10 Hz, z-scored over the file) and
interval series of annotated behaviour towards the male intruder (`Ch1_sniffing`, `Ch1_attack`,
`Ch1_dominance_mounting`; in two files only `Ch1: sniffing`). Two files also hold the weight of
each unit on "latent factor 1" of the authors' rSLDS fit (`analysis/rSLDS`). Group (control,
scrambled gRNA, or experimental, Oxtr/Avpr1a gRNAs) is read from the subject id (`ctrl...`,
`mut...`). Files are streamed from the archive at the pinned version; nothing is written to disk.

Where the parameters come from:

- Pre-intruder baseline. The STAR Methods (Micro-endoscopic data extraction) normalize traces "in
  units of sigma relative to the baseline fluorescence (during 7sec or more) of the neuron before
  the first trial", and say a 5-min baseline alone in the home cage starts every session
  (Behavior annotations). The files mark neither the baseline nor the intruder's entry. Assumption
  (stated in the notebook): the frames before the first annotated behaviour are the pre-intruder
  period, and mice with fewer than `MIN_BASELINE_S` (7 s, the Methods' "7sec or more") before it
  are left out of sigma-based measures. Readings, from the claims file: (a) all frames before the
  first annotated behaviour, (b) the last 7 s of them. A variant ending 10 s before the first
  behaviour (`BASELINE_GAP_S`) is shown in the notebook, as the population rises a few seconds
  before the first annotation in some mice; it is a check, not a reading.
- Start of the interaction, for "the first 1 or 2 minutes" windows: assumption, the onset of the
  first annotated behaviour (the intruder's entry is not marked).
- Sigma-normalized trace = (z - mean of z over the baseline) / SD of z over the baseline. As the
  file's z-score is an affine map of the unit's dF/F, this equals the Methods' normalization of
  dF/F. The 2-sigma thresholds are the Results' and legends' (Figures 4G, 5B, 5D).
- "Nested" tests, from the claims file: (a) pooled over units of all mice of a group, (b) on
  per-mouse means (for KS claims, a Mann-Whitney test on per-mouse medians).
- ACHW: the claims file's criterion, the lag at which the unit's autocorrelation first falls to
  half its zero-lag value, linearly interpolated between frames, in seconds. The estimator of the
  autocorrelation is not given; three are run (`ACHW_ESTIMATORS`, see `achw`).
- Behaviour decoder (Figure S5E): STAR Methods, Decoding behavior from neural activity; linear SVM
  on frames, equal numbers of sniff and attack frames, 20 repeats; the claims file supplies the
  stratified five-fold cross-validation. The SVM's C is not given: C = 1 (scikit-learn's default)
  is a standard choice, with 0.1 and 10 shown.
- rSLDS: the claims file's settings (fig6-rslds-fit-quality) from the ssm notebook the paper's
  code links: K = 3 states, D = 5 latent dimensions, transitions recurrent_only, dynamics
  diagonal_gaussian, emissions gaussian_orthog, single subspace, Laplace-EM with a structured
  mean-field posterior, 100 iterations, and alpha = 0 (a full parameter update at each iteration,
  as in the fit call of that notebook; ssm's default is 0.5); seeds 0 to 3. Time constants tau = |1 / log|lambda||
  times the 0.1 s bin (STAR Methods, Estimation of time constants).
"""

from __future__ import annotations

import os
import warnings
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pynwb
import remfile
import requests
from scipy import stats

DANDISET_ID = "001131"
DANDISET_VERSION = "0.260601.1203"
EARLIER_VERSION = "0.240826.1647"
API = "https://api.dandiarchive.org/api"

RATE_HZ = 10.0
MIN_BASELINE_S = 7.0       # STAR Methods: baseline "during 7sec or more"
BASELINE_GAP_S = 10.0      # variant only (see docstring)
ACTIVE_SIGMA = 2.0         # Results and legends of Figures 4G, 5B, 5D: ">= 2 sigma"

BEHAVIOURS = {"sniff": ("Ch1_sniffing", "Ch1: sniffing"),
              "attack": ("Ch1_attack",),
              "mount": ("Ch1_dominance_mounting",)}


# --- loading -------------------------------------------------------------------------------------

def assets(version: str = DANDISET_VERSION) -> list[dict]:
    r = requests.get(f"{API}/dandisets/{DANDISET_ID}/versions/{version}/assets/",
                     params={"page_size": 200}, timeout=60)
    r.raise_for_status()
    return sorted(r.json()["results"], key=lambda a: a["path"])


def _url(asset_id: str) -> str:
    r = requests.get(f"{API}/assets/{asset_id}/download/", allow_redirects=False, timeout=60)
    return r.headers["Location"]


def load_asset(asset: dict) -> dict:
    """Read one file with pynwb, streaming it; returns a dict of what the analysis uses."""
    h5 = h5py.File(remfile.File(_url(asset["asset_id"])), "r")
    with pynwb.NWBHDF5IO(file=h5, mode="r", load_namespaces=True) as io:
        nwb = io.read()
        trace = nwb.processing["ophys"]["NeuralTrace"]
        Y = np.asarray(trace.data[:], dtype=float)
        series = nwb.processing["behavior"]["BehavioralEpochs"].interval_series
        raw = {}
        for name, s in series.items():
            raw[name] = (np.asarray(s.data[:]), np.asarray(s.timestamps[:]))
        weights = None
        if "rSLDS" in nwb.analysis:
            weights = nwb.analysis["rSLDS"].to_dataframe()["latent factor 1"].to_numpy()
        sid = nwb.subject.subject_id
        out = {
            "path": asset["path"], "asset_id": asset["asset_id"], "size": asset["size"],
            "mouse": sid, "group": "control" if sid.lower().startswith("ctrl") else
            ("experimental" if sid.lower().startswith("mut") else sid),
            "Y": Y, "rate": float(trace.rate), "starting_time": float(trace.starting_time),
            "trace_unit": trace.unit, "trace_description": trace.description,
            "trace_comments": trace.comments,
            "ophys_description": nwb.processing["ophys"].description,
            "behavior_description": nwb.processing["behavior"].description,
            "session_description": nwb.session_description,
            "session_start": str(nwb.session_start_time), "keywords": list(nwb.keywords[:]),
            "age": nwb.subject.age, "sex": nwb.subject.sex, "series": raw,
            "rslds_weights": weights,
        }
    h5.close()
    out["bouts"], out["bout_series"] = {}, {}
    for beh, names in BEHAVIOURS.items():
        for n in names:
            if n in raw:
                d, t = raw[n]
                out["bouts"][beh] = np.column_stack([t[d == 1], t[d == -1]])
                out["bout_series"][beh] = n
    return out


def load_all(version: str = DANDISET_VERSION) -> list[dict]:
    with ThreadPoolExecutor(5) as ex:
        mice = list(ex.map(load_asset, assets(version)))
    return sorted(mice, key=lambda m: (m["group"], m["mouse"]))


# --- frames, baselines and normalization ---------------------------------------------------------

def frames(bouts: np.ndarray, n: int, rate: float = RATE_HZ) -> np.ndarray:
    """Boolean mask of frames inside any bout [onset, offset)."""
    mask = np.zeros(n, bool)
    for on, off in bouts:
        mask[int(round(on * rate)):int(round(off * rate))] = True
    return mask


def first_behaviour_s(m: dict) -> float:
    return float(min(b[0, 0] for b in m["bouts"].values() if len(b)))


def baseline_frames(m: dict, reading: str) -> np.ndarray | None:
    """Indices of baseline frames; None when fewer than 7 s precede the first behaviour.

    reading 'all': all frames before the first annotated behaviour; '7s': the last 7 s of them;
    'gap10': all frames up to 10 s before it (a variant, not a reading)."""
    i0 = int(round(first_behaviour_s(m) * m["rate"]))
    n7 = int(MIN_BASELINE_S * m["rate"])
    if i0 < n7:
        return None
    if reading == "all":
        return np.arange(0, i0)
    if reading == "7s":
        return np.arange(i0 - n7, i0)
    if reading == "gap10":
        end = i0 - int(BASELINE_GAP_S * m["rate"])
        return np.arange(0, end) if end >= n7 else None
    raise ValueError(reading)


def sigma_trace(m: dict, reading: str) -> np.ndarray | None:
    idx = baseline_frames(m, reading)
    if idx is None:
        return None
    base = m["Y"][idx]
    sd = base.std(0, ddof=1)
    sd[sd == 0] = np.nan
    return (m["Y"] - base.mean(0)) / sd


def window_frames(m: dict, minutes: float) -> np.ndarray:
    """The first `minutes` of interaction, from the first annotated behaviour."""
    i0 = int(round(first_behaviour_s(m) * m["rate"]))
    return np.arange(i0, min(len(m["Y"]), i0 + int(minutes * 60 * m["rate"])))


# --- tests ---------------------------------------------------------------------------------------

def mw(a, b, alternative="two-sided"):
    a, b = np.asarray(a, float), np.asarray(b, float)
    a, b = a[np.isfinite(a)], b[np.isfinite(b)]
    if len(a) == 0 or len(b) == 0:
        return np.nan, np.nan
    r = stats.mannwhitneyu(a, b, alternative=alternative)
    return float(r.statistic), float(r.pvalue)


def ks(a, b):
    a, b = np.asarray(a, float), np.asarray(b, float)
    r = stats.ks_2samp(a[np.isfinite(a)], b[np.isfinite(b)])
    return float(r.statistic), float(r.pvalue)


def nested_tests(values: dict[str, np.ndarray], groups: dict[str, str]) -> dict:
    """Per-unit values by mouse -> the two readings of the 'nested' Mann-Whitney and KS tests.

    Returns pooled means, per-mouse means, and p-values of: MW pooled (a), MW on per-mouse means
    (b), KS pooled (a), MW on per-mouse medians (b, for KS claims)."""
    ctl = [m for m in values if groups[m] == "control"]
    exp = [m for m in values if groups[m] == "experimental"]
    pc = np.concatenate([values[m] for m in ctl]); pe = np.concatenate([values[m] for m in exp])
    pc, pe = pc[np.isfinite(pc)], pe[np.isfinite(pe)]
    mc = [np.nanmean(values[m]) if len(values[m]) else np.nan for m in ctl]
    me = [np.nanmean(values[m]) if len(values[m]) else np.nan for m in exp]
    dc = [np.nanmedian(values[m]) for m in ctl]; de = [np.nanmedian(values[m]) for m in exp]
    return {
        "n_mice_c": len(ctl), "n_mice_e": len(exp), "n_units_c": len(pc), "n_units_e": len(pe),
        "pooled_mean_c": pc.mean(), "pooled_mean_e": pe.mean(),
        "mouse_mean_c": np.nanmean(mc), "mouse_mean_e": np.nanmean(me),
        "p_mw_pooled": mw(pc, pe)[1], "p_mw_mice": mw(mc, me)[1],
        "ks_D": ks(pc, pe)[0], "p_ks_pooled": ks(pc, pe)[1], "p_mw_mouse_medians": mw(dc, de)[1],
    }


# --- autocorrelation half-width ------------------------------------------------------------------

ACHW_ESTIMATORS = {"window_mean_biased": (True, False), "window_mean_unbiased": (True, True),
                   "file_mean_unbiased": (False, True)}


def achw(x: np.ndarray, rate: float = RATE_HZ, estimator: str = "window_mean_biased") -> np.ndarray:
    """ACHW in seconds for each column of x (frames x units); NaN if it never falls to half.

    The paper does not give the estimator of the autocorrelation (it cites Remedios et al. 2017).
    Estimators: 'window_mean_biased' removes the mean over the window and divides each lag's sum
    by n (the standard sample autocorrelation); 'window_mean_unbiased' divides by n - k;
    'file_mean_unbiased' removes nothing, so the mean is the file's (0 for a trace z-scored over
    the file), and divides by n - k. Over windows of 1 to 2 min the window's mean takes up much of
    a slow unit's fluctuation, which shortens the ACHW (see the synthetic check in the notebook)."""
    demean, unbiased = ACHW_ESTIMATORS[estimator]
    x = np.asarray(x, float)
    if demean:
        x = x - x.mean(0)
    n = len(x)
    f = np.fft.rfft(x, n=2 * n, axis=0)
    ac = np.fft.irfft(f * np.conj(f), axis=0)[:n]
    if unbiased:
        ac = ac / (n - np.arange(n))[:, None]
    with np.errstate(invalid="ignore", divide="ignore"):
        ac = ac / ac[0]
    out = np.full(x.shape[1], np.nan)
    for j in range(x.shape[1]):
        below = np.nonzero(ac[:, j] < 0.5)[0]
        if len(below) == 0 or not np.isfinite(ac[0, j]):
            continue
        k = below[0]
        a0, a1 = ac[k - 1, j], ac[k, j]
        out[j] = ((k - 1) + (a0 - 0.5) / (a0 - a1)) / rate
    return out


# --- choice probability ------------------------------------------------------------------------

def _auc(Y: np.ndarray, a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Per column of Y, the area under the ROC curve of values in frames a against frames b,
    P(x_a > x_b) + P(x_a = x_b) / 2, from ranks (the same as the ROC built from the histograms)."""
    sel = np.concatenate([a, b])
    r = stats.rankdata(Y[sel], axis=0)
    na, nb = len(a), len(b)
    return (r[:na].sum(0) - na * (na + 1) / 2) / (na * nb)


def _labels(bouts_a, bouts_b, n):
    la, lb = frames(bouts_a, n), frames(bouts_b, n)
    return la & ~lb, lb & ~la                     # frames annotated as both are left out


def choice_probability(m: dict, beh_a: str, beh_b: str, rng: np.random.Generator,
                       shuffle: str = "circular", n_shuffles: int = 100) -> dict:
    """CP of every unit for behaviour a against b, with a bout-shuffled null.

    STAR Methods (Choice probability): the area under the ROC curve built from histograms of the
    unit's values in frames of the two behaviours; shuffled 100 times "by shuffling behavior bout
    timings"; tuned when CP > 0.7 and more than 2 shuffled SDs from the shuffled mean. Shuffle
    readings, from the claims file: 'circular', the bout sequence shifted circularly by a random
    offset within the interaction (first annotated behaviour to the end of the file);
    'reassign', each bout given a random onset within the interaction, keeping its duration and
    label. The AUC is unchanged by an increasing affine map of a unit's trace, so the z-scored and
    sigma-normalized traces give the same CP."""
    Y, n = m["Y"], len(m["Y"])
    i0 = int(round(first_behaviour_s(m) * m["rate"]))
    a, b = _labels(m["bouts"][beh_a], m["bouts"][beh_b], n)
    cp = _auc(Y, np.nonzero(a)[0], np.nonzero(b)[0])
    L = n - i0
    null = []
    for _ in range(n_shuffles):
        if shuffle == "circular":
            k = int(rng.integers(1, L))
            sa = np.r_[a[:i0], np.roll(a[i0:], k)]; sb = np.r_[b[:i0], np.roll(b[i0:], k)]
        elif shuffle == "reassign":
            new = {}
            for beh in (beh_a, beh_b):
                bo = m["bouts"][beh]
                d = bo[:, 1] - bo[:, 0]
                on = i0 / m["rate"] + rng.random(len(bo)) * np.maximum(L / m["rate"] - d, 0)
                new[beh] = np.column_stack([on, on + d])
            sa, sb = _labels(new[beh_a], new[beh_b], n)
        else:
            raise ValueError(shuffle)
        null.append(_auc(Y, np.nonzero(sa)[0], np.nonzero(sb)[0]))
    null = np.array(null)
    mu, sd = null.mean(0), null.std(0, ddof=1)
    return {"cp": cp, "tuned_a": (cp > 0.7) & (cp > mu + 2 * sd),
            "tuned_b": (cp < 0.3) & (cp < mu - 2 * sd), "null_mean": mu, "null_sd": sd}


# --- behaviour decoder ---------------------------------------------------------------------------

def decode_attack_vs_sniff(m: dict, rng: np.random.Generator, C: float = 1.0, repeats: int = 20,
                           shuffle: bool = False, by_bout: bool = False,
                           n_units: int | None = None) -> float:
    """Mean five-fold accuracy of a linear SVM on balanced sniff and attack frames.

    by_bout=False is the paper's frame-wise stratified five-fold split; by_bout=True keeps all
    frames of a bout in one fold (a variant, to show how much neighbouring frames of the same
    bout in training and test sets contribute). n_units: a random subset of that many units is
    drawn in each repeat (a variant, so that mice with different unit counts are compared on equal
    numbers; the paper does not subsample)."""
    from sklearn.model_selection import StratifiedGroupKFold, StratifiedKFold, cross_val_score
    from sklearn.svm import LinearSVC
    Y, n = m["Y"], len(m["Y"])
    bouts = [(b, 0) for b in m["bouts"]["sniff"]] + [(b, 1) for b in m["bouts"]["attack"]]
    accs = []
    for _ in range(repeats):
        labels = np.array([lab for _, lab in bouts])
        if shuffle:
            labels = rng.permutation(labels)
        idx, y, g = [], [], []
        for i, ((on, off), lab) in enumerate(zip([b for b, _ in bouts], labels)):
            f = np.arange(int(round(on * RATE_HZ)), min(n, int(round(off * RATE_HZ))))
            idx.append(f); y.append(np.full(len(f), lab)); g.append(np.full(len(f), i))
        idx, y, g = np.concatenate(idx), np.concatenate(y), np.concatenate(g)
        _, first = np.unique(idx, return_index=True)  # a frame in two bouts counts once
        idx, y, g = idx[first], y[first], g[first]
        k = min((y == 0).sum(), (y == 1).sum())
        if k < 10:
            return np.nan
        sel = np.concatenate([rng.choice(np.nonzero(y == c)[0], k, replace=False) for c in (0, 1)])
        units = (np.sort(rng.choice(Y.shape[1], n_units, replace=False)) if n_units
                 else np.arange(Y.shape[1]))
        seed = int(rng.integers(1 << 31))
        cv = (StratifiedGroupKFold(5, shuffle=True, random_state=seed) if by_bout
              else StratifiedKFold(5, shuffle=True, random_state=seed))
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            accs.append(cross_val_score(LinearSVC(C=C, max_iter=5000), Y[idx[sel]][:, units], y[sel],
                                        groups=g[sel] if by_bout else None, cv=cv).mean())
    return float(np.mean(accs))


# --- rSLDS ---------------------------------------------------------------------------------------

K_STATES, D_LATENT, NUM_ITERS = 3, 5, 100
SEEDS = (0, 1, 2, 3)


def fit_rslds(args):
    """Fit one rSLDS; args = (mouse, Y, seed, num_iters). Run in a worker process."""
    mouse, Y, seed, num_iters = args
    for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
        os.environ[v] = "1"
    warnings.filterwarnings("ignore")
    import ssm
    np.random.seed(seed)
    model = ssm.SLDS(Y.shape[1], K_STATES, D_LATENT, transitions="recurrent_only",
                     dynamics="diagonal_gaussian", emissions="gaussian_orthog",
                     single_subspace=True)
    model.initialize(Y)
    elbos, q = model.fit(Y, method="laplace_em", variational_posterior="structured_meanfield",
                         num_iters=num_iters, initialize=False, alpha=0.0, verbose=0)
    x = q.mean_continuous_states[0]
    z = model.most_likely_states(x, Y)
    C = model.emissions.Cs[0]
    d = model.emissions.ds[0]
    yhat = x @ C.T + d
    r2 = 1 - ((Y - yhat) ** 2).sum() / ((Y - Y.mean(0)) ** 2).sum()
    As, bs = model.dynamics.As, model.dynamics.bs
    return {"mouse": mouse, "seed": seed, "elbos": np.asarray(elbos), "x": x, "z": z, "C": C,
            "d": d, "As": As, "bs": bs, "r2": float(r2)}


def fit_heldout(args):
    """Fit with one fifth of the recording held out, and score the held-out frames.

    args = (mouse, Y, seed, num_iters). The recording is cut into 20 blocks of equal length;
    blocks 3, 8, 13 and 18 are held out (spread over the session, so that slow drifts over the
    session do not dominate the score) and the other 16 are fit as separate trials. The latents
    of each held-out block are inferred with the parameters fixed (ssm's approximate_posterior).
    Scores on the held-out neural activity, pooled over the four blocks, each as 1 - SSE / SST
    about the held-out mean: the R2 of the emissions reconstruction, and the R2 of forward
    predictions of the activity over 1 s and 5 s (the latent at t propagated with the dynamics
    of the state at t, then mapped through the emissions, against the activity at t + h). One
    fold, not the paper's unstated folds; a check, see the notebook."""
    mouse, Y, seed, num_iters = args
    for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
        os.environ[v] = "1"
    warnings.filterwarnings("ignore")
    import ssm
    blocks = np.array_split(np.arange(len(Y)), 20)
    test_ix = (2, 7, 12, 17)
    train = [Y[b] for i, b in enumerate(blocks) if i not in test_ix]
    test = [Y[blocks[i]] for i in test_ix]
    np.random.seed(seed)
    model = ssm.SLDS(Y.shape[1], K_STATES, D_LATENT, transitions="recurrent_only",
                     dynamics="diagonal_gaussian", emissions="gaussian_orthog",
                     single_subspace=True)
    model.initialize(train)
    model.fit(train, method="laplace_em", variational_posterior="structured_meanfield",
              num_iters=num_iters, initialize=False, alpha=0.0, verbose=0)
    _, q = model.approximate_posterior(test, method="laplace_em",
                                       variational_posterior="structured_meanfield",
                                       num_iters=25, verbose=0)
    C, d = model.emissions.Cs[0], model.emissions.ds[0]
    As, bs = model.dynamics.As, model.dynamics.bs
    mean_te = np.concatenate(test).mean(0)
    sse = {"recon": 0.0, 1.0: 0.0, 5.0: 0.0}
    sst = {"recon": 0.0, 1.0: 0.0, 5.0: 0.0}
    for Yb, x in zip(test, q.mean_continuous_states):
        z = model.most_likely_states(x, Yb)
        sse["recon"] += ((Yb - (x @ C.T + d)) ** 2).sum()
        sst["recon"] += ((Yb - mean_te) ** 2).sum()
        for h_s in (1.0, 5.0):
            h = int(round(h_s * RATE_HZ))
            T = len(x) - h
            pred = x[:T].copy()
            for _ in range(h):
                pred = np.einsum("tij,tj->ti", As[z[:T]], pred) + bs[z[:T]]
            sse[h_s] += ((Yb[h:] - (pred @ C.T + d)) ** 2).sum()
            sst[h_s] += ((Yb[h:] - mean_te) ** 2).sum()
    return {"mouse": mouse, "seed": seed, "test_frames": sum(len(b) for b in test),
            "test_r2": float(1 - sse["recon"] / sst["recon"]),
            "test_fwd_r2_1s": float(1 - sse[1.0] / sst[1.0]),
            "test_fwd_r2_5s": float(1 - sse[5.0] / sst[5.0])}


def time_constants(A: np.ndarray, dt: float = 1 / RATE_HZ) -> tuple[np.ndarray, np.ndarray]:
    """tau (s) of each eigenmode, sorted decreasing, and the matching eigenvectors (columns)."""
    lam, V = np.linalg.eig(A)
    with np.errstate(divide="ignore"):
        tau = np.abs(1 / np.log(np.abs(lam))) * dt
    order = np.argsort(-tau)
    return tau[order], V[:, order]


def forward_sim_score(fit: dict, horizon_s: float) -> float:
    """R2 of latent forward predictions over `horizon_s`, using the inferred states.

    From each time t, the inferred latent x(t) is propagated with the dynamics of the inferred
    state at t for h steps and compared with the inferred latent x(t + h); the score is
    1 - MSE / variance of x(t + h), over all times and latent dimensions (the Results call the
    paper's measure "cvR2"). In-sample, not the paper's held-out folds (see notebook)."""
    x, z, As, bs = fit["x"], fit["z"], fit["As"], fit["bs"]
    h = int(round(horizon_s * RATE_HZ))
    T = len(x) - h
    pred = x[:T].copy()
    for _ in range(h):
        pred = np.einsum("tij,tj->ti", As[z[:T]], pred) + bs[z[:T]]
    target = x[h:h + T]
    return float(1 - ((pred - target) ** 2).sum() / ((target - target.mean(0)) ** 2).sum())


def fit_all(mice: list[dict], seeds=SEEDS, num_iters: int = NUM_ITERS, workers: int = 4,
            traces: dict | None = None) -> dict:
    """Fit every mouse under every seed in worker processes, largest first; {(mouse, seed): fit}.

    traces: {mouse: frames x units} to fit in place of the file's z-scored trace (the
    sigma-normalized reading)."""
    from concurrent.futures import ProcessPoolExecutor
    Ys = {m["mouse"]: (traces[m["mouse"]] if traces else m["Y"]) for m in mice}
    jobs = sorted([(k, Y, s, num_iters) for k, Y in Ys.items() for s in seeds],
                  key=lambda j: -j[1].size)
    with ProcessPoolExecutor(workers) as ex:
        return {(f["mouse"], f["seed"]): f for f in ex.map(fit_rslds, jobs)}


def summarize_fit(fit: dict, m: dict) -> dict:
    """Measures of one fit used by the claims.

    attack_state: the state holding most attack frames (reading (a) of the claims file); for the
    two mice with no attack annotation, the state holding most annotated sniff frames, flagged by
    `state_from`. tau_a: time constants of that state's dynamics matrix; tau_b: the mean over the
    three states of each state's sorted time constants (reading (b)). Unit weights on dimension j
    are |C v_j|, v_j the j-th eigenvector (by decreasing tau) of the attack state's matrix, real
    part; for the second eigenvector of a complex pair, its imaginary part."""
    n = len(m["Y"])
    z = fit["z"]
    beh = "attack" if "attack" in m["bouts"] else "sniff"
    fr = frames(m["bouts"][beh], n)
    counts = np.bincount(z[fr], minlength=K_STATES)
    k = int(np.argmax(counts))
    taus = [time_constants(A)[0] for A in fit["As"]]
    tau_a, V = time_constants(fit["As"][k])
    tau_b = np.mean(taus, axis=0)
    W = np.abs(fit["C"] @ np.real(V))
    # A complex pair has conjugate eigenvectors with the same real part, so dimensions j and j + 1
    # would get the same weights; the second of the pair takes the imaginary part instead (the
    # real and imaginary parts span the plane in which the pair rotates).
    complex_pair = np.zeros(D_LATENT, bool)
    for j in range(D_LATENT - 1):
        if (abs(V[:, j].imag).max() > 1e-12 and not complex_pair[j]
                and np.allclose(V[:, j + 1], np.conj(V[:, j]))):
            W[:, j + 1] = np.abs(fit["C"] @ np.imag(V[:, j]))
            complex_pair[j] = complex_pair[j + 1] = True
    attack_counts = (np.bincount(z[frames(m["bouts"]["attack"], n)], minlength=K_STATES)
                     if "attack" in m["bouts"] else None)
    return {"mouse": m["mouse"], "group": m["group"], "seed": fit["seed"], "state_from": beh,
            "attack_state": k, "tau_a": tau_a, "tau_b": tau_b,
            "score_a": float(np.log2(tau_a[0] / tau_a[1])),
            "score_b": float(np.log2(tau_b[0] / tau_b[1])),
            "attack_frac_in_state": (float(attack_counts.max() / attack_counts.sum())
                                     if attack_counts is not None else np.nan),
            "weights": W, "complex_pair": complex_pair, "r2": fit["r2"],
            "state_occupancy": np.bincount(z, minlength=K_STATES) / len(z)}


def dunn_1_vs_2(tau_by_dim: np.ndarray) -> float:
    """Dunn's test (Bonferroni over the 10 pairs of 5 dimensions) of dimension 1 against 2.

    tau_by_dim: mice x dimensions. Ranks are over all values, with the tie correction."""
    x = tau_by_dim.ravel()
    g = np.tile(np.arange(tau_by_dim.shape[1]), tau_by_dim.shape[0])
    r = stats.rankdata(x)
    N = len(x)
    _, t = np.unique(x, return_counts=True)
    tie = (t ** 3 - t).sum() / (12 * (N - 1))
    n1 = (g == 0).sum(); n2 = (g == 1).sum()
    zval = (r[g == 0].mean() - r[g == 1].mean()) / np.sqrt((N * (N + 1) / 12 - tie) * (1 / n1 + 1 / n2))
    k = tau_by_dim.shape[1]
    return float(min(1.0, 2 * stats.norm.sf(abs(zval)) * k * (k - 1) / 2))


SSM_COMMIT = "eb6c8aa33e5311d3564075807dec340759dd8081"   # the commit the claims file read


def ensure_ssm() -> str:
    """Install ssm at SSM_COMMIT into this kernel's environment if it is not there.

    ssm's setup.py imports numpy and Cython but declares no build dependencies, so it cannot be
    built in the isolated build that installing the lock file uses; it is built here without
    isolation, against the locked numpy, Cython and setuptools."""
    import importlib.util
    import subprocess
    import sys
    if importlib.util.find_spec("ssm") is None:
        subprocess.run(["uv", "pip", "install", "--quiet", "--python", sys.executable,
                        "--no-build-isolation", "--no-deps",
                        f"ssm @ git+https://github.com/lindermanlab/ssm@{SSM_COMMIT}"], check=True)
    return SSM_COMMIT
