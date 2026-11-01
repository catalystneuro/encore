"""Loading and measures for dandiset 001037 (Vinograd, Nair et al. 2024, Nature 634, 910-918).

Where each parameter comes from is said next to it:
- "claims" : the claim's criterion in claims/001037/10.1038-s41586-024-07915-x.yaml;
- "paper"  : a passage of the paper, cited (author, step 1.6);
- "code"   : the authors' sample code linked from the dandiset's description,
             github.com/neuralcomputation/hypothalamic-dynamics at commit 28fee70;
- "assumption" : a choice the paper leaves open (said what and why);
- "standard" : a choice that cannot change a result (a seed, a plotting detail).

Data are streamed from the DANDI Archive with remfile and h5py; nothing is written to disk.
"""
import os
from functools import lru_cache

import h5py
import numpy as np
import remfile
import requests
from scipy import stats

DANDISET = "001037"
VERSION = "0.260609.1402"
API = "https://api.dandiarchive.org/api"
RATE = 10.0  # Hz; SessionMetadata sample_rate_hz and every TimeSeries rate (checked in the notebook)

MINISCOPE = ["M30L", "M35R", "M36L", "M37R", "M38R"]
TWO_PHOTON = ["M70", "M168", "M174", "M179", "M18R", "M79RL", "M99RL"]

# Stimulation pulses last 2 s (paper, Methods, 2P imaging and holographic optogenetics:
# "holographic photostimulation (10 Hz, 2 s, 10 ms pulse width)").
PULSE_FRAMES = 20


@lru_cache(maxsize=None)
def assets(version=VERSION):
    """Map of path -> asset id for a version of the dandiset."""
    out, url = {}, f"{API}/dandisets/{DANDISET}/versions/{version}/assets/?page_size=200"
    while url:
        r = requests.get(url, timeout=60).json()
        out.update({a["path"]: a["asset_id"] for a in r["results"]})
        url = r.get("next")
    return out


def asset_path(subject, kind):
    """kind: 'miniscope', '2p' or 'legacy' (the older M70 file)."""
    paths = [p for p in assets() if p.startswith(f"sub-{subject}/")]
    if kind == "legacy":
        paths = [p for p in paths if p.endswith("ses-None_behavior.nwb")]
    elif kind == "miniscope":
        paths = [p for p in paths if "ses-2023" in p and subject in MINISCOPE]
    else:
        paths = [p for p in paths if not p.endswith("ses-None_behavior.nwb")]
    assert len(paths) == 1, (subject, kind, paths)
    return paths[0]


@lru_cache(maxsize=None)
def open_nwb(path):
    url = f"{API}/assets/{assets()[path]}/download/"
    s3 = requests.head(url, allow_redirects=True, timeout=60).url
    return h5py.File(remfile.File(s3), "r")


def _s(x):
    return x.decode() if isinstance(x, bytes) else x


def read_table(f, base):
    g = f[base]
    cols = [_s(c) for c in g.attrs["colnames"]]
    return {c: [_s(v) for v in g[c][:]] for c in cols}


def read_intervals(group):
    """IntervalSeries -> list of (start, stop) in seconds (data +1 start, -1 stop)."""
    d, t = group["data"][:], group["timestamps"][:]
    starts, out = None, []
    for v, ts in zip(d, t):
        if v > 0:
            starts = ts
        elif v < 0 and starts is not None:
            out.append((float(starts), float(ts)))
            starts = None
    return out


def raster(intervals, n_frames, rate=RATE):
    r = np.zeros(n_frames, bool)
    for a, b in intervals:
        r[int(round(a * rate)):int(round(b * rate)) + 1] = True
    return r[:n_frames]


# --------------------------------------------------------------------------------------
# Loading
def load_miniscope(subject):
    """Both sessions of a miniscope mouse: {'engage'|'observe': {'Y': frames x cells, 'beh': {...}}}."""
    f = open_nwb(asset_path(subject, "miniscope"))
    out = {}
    for key, short in [("engagement_of_aggression", "engage"), ("observation_of_aggression", "observe")]:
        Y = f[f"processing/ophys/{key}_NeuralTrace/data"][:]
        beh = {k: read_intervals(v) for k, v in f[f"processing/behavior/{key}_BehavioralEpochs"].items()}
        out[short] = {"Y": Y, "beh": beh, "rate": float(f[f"processing/ophys/{key}_NeuralTrace/starting_time"].attrs["rate"])}
    out["meta"] = read_table(f, "analysis/SessionMetadata")
    return out


def miniscope_labels(sess, which):
    """Intervals for a behaviour whatever its spelling in the file.

    which: 'attack' (engaged attack), 'watch_attack' (observed attack), 'balbc' (BALB/c in cage),
    'sw' (SW in cage), 'watch_sniff'. Spellings differ between files (M30L uses balb_c_in_cage, the
    others balb_c); criteria compare identity, not spelling (protocol, author step 1.4)."""
    names = {"attack": ["attack"], "watch_attack": ["watch_attack"], "balbc": ["balb_c_in_cage", "balb_c"],
             "sw": ["sw_in_cage", "sw"], "watch_sniff": ["watch_sniff"], "sniff": ["sniff"]}[which]
    for n in names:
        if n in sess["beh"]:
            return sess["beh"][n]
    return None


def load_2p(subject):
    f = open_nwb(asset_path(subject, "2p"))
    W = read_table(f, "analysis/rSLDS_factor_weights")
    order = np.argsort(W["cell_index"])
    weights = np.c_[np.array(W["rSLDS_factor_1"])[order], np.array(W["rSLDS_factor_2"])[order]]
    pm = read_table(f, "analysis/ProjectionMetadata")
    an = read_table(f, "analysis/ActivatedNeurons")
    sessions = {}
    for k in f["processing/ophys"]:
        key = k.replace("_zscored_activity", "")
        sessions[key] = f[f"processing/ophys/{k}/data"][:]
    stim = {}
    for k in f["stimulus/presentation"]:
        if k.endswith("_stim_frames"):
            stim[k.replace("_stim_frames", "")] = np.round(f[f"stimulus/presentation/{k}/timestamps"][:] * RATE).astype(int)
    entry = float(f["stimulus/presentation/observation_balbc_entry/timestamps"][0])
    beh = {}
    if "processing/behavior/observation_BehavioralEpochs" in f:
        beh = {k: read_intervals(v) for k, v in f["processing/behavior/observation_BehavioralEpochs"].items()}
    proj = {}
    for s, n, fac, b0, b1, sm in zip(pm["session_key"], pm["projection_name"], pm["projection_factor"],
                                     pm["baseline_start_frame"], pm["baseline_end_frame"],
                                     pm["post_projection_smooth_window"]):
        proj[(s, "x1" if n == "integration_projection" else "x2")] = dict(factor=int(fac), b0=int(b0), b1=int(b1), smooth=float(sm))
    activated = {}
    for s, i in zip(an["session_key"], an["neuron_index"]):
        activated.setdefault(s, []).append(int(i) - 1)  # stored 1-based
    return dict(subject=subject, W=weights, sessions=sessions, stim=stim, entry_s=entry, beh=beh,
                proj=proj, activated=activated)


def projection(d, session, dim):
    """x1 or x2 projection of a 2P session (code: compute_projection_from_simplified_nwb).

    Factor weights times the z-scored activity, moving average over the stored window, minus the
    mean over the stored 1-based inclusive baseline window."""
    m = d["proj"][(session, dim)]
    tr = d["sessions"][session] @ d["W"][:, m["factor"] - 1]
    w = int(round(m["smooth"]))
    if w > 1:
        tr = np.convolve(tr, np.ones(w) / w, mode="same")
    tr = tr - tr[m["b0"] - 1:m["b1"]].mean()
    return tr


def x1_x2_factor(d):
    """Column index (0-based) of the x1 and x2 factor, from ProjectionMetadata of the observation session."""
    return d["proj"][("observation", "x1")]["factor"] - 1, d["proj"][("observation", "x2")]["factor"] - 1


def top_neurons(w, n=5):
    """The n neurons with the largest absolute weight (claims, after Fig. 1i)."""
    return np.argsort(-np.abs(w))[:n]


# --------------------------------------------------------------------------------------
# Measures
def autocorr(y, max_lag):
    """Autocorrelation as in Methods eqs 7 and 8 (code: autocorr_matlab): r_k = c_k / c_0 with
    c_k = 1/T sum (y_t - ybar)(y_t+k - ybar) and c_0 the sample variance (ddof 1)."""
    y = np.asarray(y, float) - np.mean(y)
    T = len(y)
    c0 = (y ** 2).sum() / (T - 1)
    n = 1 << int(np.ceil(np.log2(2 * T)))
    F = np.fft.rfft(y, n)
    ac = np.fft.irfft(F * np.conj(F), n)[:max_lag + 1] / T
    return ac / c0


def achw(y, rate=RATE, max_lag=None):
    """Autocorrelation half-width: first lag at which the autocorrelation falls to 0.5 or below,
    in seconds (claims, ed3e). NaN when it never does within the trace."""
    max_lag = len(y) - 1 if max_lag is None else max_lag
    r = autocorr(y, max_lag)
    idx = np.nonzero(r <= 0.5)[0]
    return idx[0] / rate if idx.size else np.nan


def time_constants(A, rate=RATE):
    """Time constants of a dynamics matrix, abs(1/log(abs(lambda))) / rate, in seconds (code;
    the Methods give 1/log(lambda) in frames)."""
    w = np.linalg.eigvals(A)
    return np.abs(1 / np.log(np.abs(w))) / rate


def line_attractor_score(taus):
    """log2 of the largest over the second largest time constant (paper, Methods eq. 6)."""
    t = np.sort(np.asarray(taus))[::-1]
    return float(np.log2(t[0] / t[1]))


def subspace_angle(a, b):
    """Angle in degrees between two weight vectors (unsigned, 0 to 90)."""
    c = abs(a @ b) / np.linalg.norm(a) / np.linalg.norm(b)
    return float(np.degrees(np.arccos(np.clip(c, -1, 1))))


# --------------------------------------------------------------------------------------
# rSLDS
def fit_rslds(Y, K, D=2, l2_A=820, l2=100, alpha=0.9, iters=150, seed=0, inputs=None):
    """Fit an rSLDS as the sample code's rslds() does (code, analysis/analysis_functions.py):
    recurrent_only transitions, gaussian dynamics and emissions, single subspace, initialize then
    Laplace-EM with a structured mean-field posterior. Returns a dict of numpy results.

    Settings (claims header, from the code): 2P K=2, l2_penalty_A 820, l2_penalty 100, alpha 0.9,
    150 iterations; miniscope K=3, l2_penalty_A 10, l2_penalty 500, alpha 0.5, 100 iterations.
    The seed is a standard choice (the code's 0)."""
    import autograd.numpy.random as npr
    import ssm
    npr.seed(seed)
    np.random.seed(seed)
    M = 0 if inputs is None else inputs.shape[1]
    m = ssm.SLDS(N=Y.shape[1], K=K, D=D, M=M, transitions="recurrent_only", dynamics="gaussian",
                 emissions="gaussian", single_subspace=True,
                 dynamics_kwargs=dict(l2_penalty_A=l2_A), transitions_kwargs=dict(l2_penalty=l2))
    kw = {} if inputs is None else dict(inputs=inputs)
    m.initialize(Y, **kw)
    elbos, post = m.fit(Y, method="laplace_em", variational_posterior="structured_meanfield",
                        initialize=False, num_iters=iters, alpha=alpha, verbose=0, **kw)
    xhat = post.mean_continuous_states[0]
    zhat = m.most_likely_states(xhat, Y, **({} if inputs is None else dict(input=inputs)))
    return dict(As=np.array(m.dynamics.As), bs=np.array(m.dynamics.bs), Vs=np.array(m.dynamics.Vs),
                C=np.array(m.emissions.Cs[0]), d=np.array(m.emissions.ds[0]),
                Rs=np.array(m.transitions.Rs), r=np.array(m.transitions.r),
                xhat=xhat, zhat=zhat, elbo_last=float(elbos[-1]), K=K)


def slow_fast(fit, rate=RATE):
    """x1 and x2 time constants of a fit (claims, ed1n): in the state with the largest time
    constant, x1 is the larger and x2 the smaller of its two time constants. Also returns the
    unit eigenvector of the slow mode in latent space and the slow state."""
    taus = [time_constants(A, rate) for A in fit["As"]]
    k = int(np.argmax([t.max() for t in taus]))
    w, V = np.linalg.eig(fit["As"][k])
    tk = np.abs(1 / np.log(np.abs(w))) / rate
    i = int(np.argmax(tk))
    v = np.real(V[:, i])
    return dict(state=k, tau_x1=float(tk.max()), tau_x2=float(tk.min()), taus=taus, v1=v / np.linalg.norm(v),
                las=line_attractor_score(tk))


def x1_weights(fit):
    """Neuron weights of x1 and x2: the emission matrix C mapped onto the slow and the other
    eigenvector of the slow state's dynamics (paper, Methods: 'we then used the columns of the
    emission matrix C to identify neurons that contributed to the two separate dimensions')."""
    sf = slow_fast(fit)
    A = fit["As"][sf["state"]]
    w, V = np.linalg.eig(A)
    if np.iscomplexobj(w) and np.any(np.abs(np.imag(w)) > 1e-12):
        # complex pair: both modes share one time constant, so no eigenvector is the slow one;
        # take C's columns, the column whose diagonal entry of A is larger first (assumption)
        o = np.argsort(-np.abs(np.diag(A)))
        w1, w2 = fit["C"][:, o[0]], fit["C"][:, o[1]]
    else:
        V = np.real(V)
        order = np.argsort(-np.abs(1 / np.log(np.abs(np.real(w)))))
        w1, w2 = fit["C"] @ V[:, order[0]], fit["C"] @ V[:, order[1]]
    return w1 / np.linalg.norm(w1), w2 / np.linalg.norm(w2)


# --------------------------------------------------------------------------------------
# Photostimulation periods
def periods(trace, onsets, reading, isi=None):
    """Mean of a trace over the baseline and the four ISIs.

    Baseline: all frames before the first onset (claims header, ISI windows).
    Wa: each ISI from the end of the 2 s pulse to the next onset; the last pulse, the same length
        after it. Wb: from one onset to the next; the last, the same length after it."""
    onsets = list(onsets)
    isi = isi or (onsets[1] - onsets[0])
    out = [trace[:onsets[0]].mean()]
    for i, o in enumerate(onsets):
        end = onsets[i + 1] if i + 1 < len(onsets) else o + isi
        start = o + PULSE_FRAMES if reading == "Wa" else o
        out.append(trace[start:min(end, len(trace))].mean())
    return np.array(out)


def dunn(groups, pairs):
    """Kruskal-Wallis over groups and Dunn's test for the given pairs, Bonferroni-adjusted over
    the number of pairs (Dunn's multiple-comparison correction as GraphPad applies it). Returns
    (H, p_kw, [adjusted p per pair])."""
    groups = [np.asarray(g, float) for g in groups]
    H, pkw = stats.kruskal(*groups)
    allv = np.concatenate(groups)
    ranks = stats.rankdata(allv)
    N = len(allv)
    _, counts = np.unique(allv, return_counts=True)
    tie = 1 - (counts ** 3 - counts).sum() / (N ** 3 - N)
    idx = np.cumsum([0] + [len(g) for g in groups])
    rbar = [ranks[idx[i]:idx[i + 1]].mean() for i in range(len(groups))]
    ps = []
    for i, j in pairs:
        se = np.sqrt(tie * N * (N + 1) / 12 * (1 / len(groups[i]) + 1 / len(groups[j])))
        z = (rbar[i] - rbar[j]) / se
        ps.append(min(1.0, 2 * stats.norm.sf(abs(z)) * len(pairs)))
    return float(H), float(pkw), ps


PAIRS = {"Ca": [(0, 1), (0, 2), (0, 3), (0, 4)], "Cb": [(0, 1), (1, 2), (2, 3), (3, 4)]}


def mwu(a, b):
    """Two-tailed Mann-Whitney U test, exact when there are no ties (scipy's default)."""
    return float(stats.mannwhitneyu(a, b, alternative="two-sided").pvalue)


def wsr(a, b):
    """Two-tailed paired Wilcoxon signed-rank test (exact for small n)."""
    return float(stats.wilcoxon(a, b, alternative="two-sided").pvalue)


def limit_threads():
    for k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
        os.environ[k] = "1"


# --------------------------------------------------------------------------------------
# Installing ssm and running many fits
SSM_REPO = "https://github.com/lindermanlab/ssm"
SSM_COMMIT = "eb6c8aa33e5311d3564075807dec340759dd8081"  # the commit the claims file read


def ensure_ssm():
    """Install the rSLDS library ssm at a pinned commit if it is missing.

    ssm's setup.py imports numpy and Cython, so it cannot be built in an isolated build
    environment, which is how `tools/entry.py run` installs the lock file. Its build and runtime
    dependencies (numpy, Cython, setuptools, autograd, numba, scikit-learn, tqdm) are locked in
    requirements.lock.txt; ssm itself is built here against them, without its own dependencies."""
    try:
        import ssm  # noqa: F401
        return "already installed"
    except ImportError:
        pass
    import shutil
    import subprocess
    import sys
    spec = f"ssm @ git+{SSM_REPO}@{SSM_COMMIT}"
    if shutil.which("uv"):
        cmd = ["uv", "pip", "install", "--quiet", "--python", sys.executable, "--no-build-isolation", "--no-deps", spec]
    else:
        cmd = [sys.executable, "-m", "pip", "install", "--quiet", "--no-build-isolation", "--no-deps", spec]
    subprocess.run(cmd, check=True)
    return f"installed ssm at {SSM_COMMIT}"


def model_prediction(fit, inputs=None):
    """Forward prediction of the latents from the first inferred point, following the inferred
    discrete states (code: calculate_model_prediction)."""
    x = [fit["xhat"][0]]
    for t in range(len(fit["xhat"]) - 1):
        k = fit["zhat"][t]
        nxt = fit["As"][k] @ x[-1] + fit["bs"][k]
        if inputs is not None:
            nxt = nxt + fit["Vs"][k] @ inputs[t]
        x.append(nxt)
    return np.array(x)


def code_r2(fit, inputs=None):
    """The sample code's R2 (report_r_squred_value): mean over latent dimensions of the R2 of the
    inferred latents against the forward prediction."""
    from sklearn.metrics import r2_score
    pred = model_prediction(fit, inputs)
    return float(np.mean([r2_score(fit["xhat"][:, d], pred[:, d]) for d in range(pred.shape[1])]))


def _fit_job(key, Y, kw, inputs):
    limit_threads()
    ensure_ssm()
    import time
    t = time.time()
    f = fit_rslds(Y, inputs=inputs, **kw)
    f["seconds"] = time.time() - t
    f["code_r2"] = code_r2(f, inputs)
    return key, f


def run_fits(jobs, n_jobs=None):
    """jobs: list of (key, Y, kwargs, inputs). Fits in parallel processes, one thread each."""
    from joblib import Parallel, delayed
    n_jobs = n_jobs or min(4, os.cpu_count() or 1)
    return dict(Parallel(n_jobs=n_jobs)(delayed(_fit_job)(*j) for j in jobs))


MINI_KW = dict(K=3, l2_A=10, l2=500, alpha=0.5, iters=100)
TWO_P_KW = dict(K=2, l2_A=820, l2=100, alpha=0.9, iters=150)
CODE_SEEDS = [0, 1, 137, 1337]  # the seeds the sample code's notebooks try (code)


# --------------------------------------------------------------------------------------
# Decoding observed attack from x1 (paper, Methods, Decoding behaviour from integration dimension)
def merge_bouts(iv, gap=5.0):
    """Merge bouts separated by less than 5 s into trials (paper, Methods)."""
    out = []
    for a, b in sorted(iv):
        if out and a - out[-1][1] < gap:
            out[-1] = (out[-1][0], max(b, out[-1][1]))
        else:
            out.append((a, b))
    return out


def decoder_trials(sig, iv, rng, rate=RATE):
    """Balanced trials: each merged attack trial with as many non-attack frames, drawn at random
    without replacement from the session's non-attack frames (assumption: the paper says only
    'balancing the data'). Returns a list of (attack values, non-attack values)."""
    T = len(sig)
    att = raster(iv, T, rate)
    pool = np.nonzero(~att)[0]
    rng.shuffle(pool)
    k, out = 0, []
    for a, b in merge_bouts(iv):
        fr = np.arange(int(round(a * rate)), min(T, int(round(b * rate)) + 1))
        neg = pool[k:k + len(fr)]
        k += len(fr)
        out.append((sig[fr], sig[neg]))
    return out


def fit_threshold(pos, neg):
    """A linear SVM on the one-dimensional signal, that is a threshold (paper, Methods)."""
    from sklearn.svm import LinearSVC
    X = np.r_[pos, neg][:, None]
    y = np.r_[np.ones(len(pos)), np.zeros(len(neg))]
    return LinearSVC(C=1.0, dual=False).fit(X, y)


def accuracy(clf, trial):
    X = np.r_[trial[0], trial[1]][:, None]
    y = np.r_[np.ones(len(trial[0])), np.zeros(len(trial[1]))]
    return float((clf.predict(X) == y).mean())


def shuffle_trials(trials, rng):
    """Behaviour labels assigned at random to the bouts of each trial (paper, Methods)."""
    return [(b, a) if rng.random() < 0.5 else (a, b) for a, b in trials]


def decode(trials, reading):
    """Mean held-out accuracy. Readings (claims, ed3g): 'one' trains on one trial and tests on all
    others; 'loto' leaves one trial out; '5fold' is fivefold over trials (leave-one-out when there
    are fewer than five trials)."""
    n, accs = len(trials), []
    if reading == "one":
        for i in range(n):
            clf = fit_threshold(*trials[i])
            accs += [accuracy(clf, trials[j]) for j in range(n) if j != i]
    else:
        folds = [[i] for i in range(n)] if (reading == "loto" or n < 5) else [list(f) for f in np.array_split(np.arange(n), 5)]
        for f in folds:
            trn = [trials[j] for j in range(n) if j not in f]
            clf = fit_threshold(np.concatenate([a for a, b in trn]), np.concatenate([b for a, b in trn]))
            accs += [accuracy(clf, trials[j]) for j in f]
    return float(np.mean(accs))


# --------------------------------------------------------------------------------------
# Baseline calcium transients (paper, Extended Data Fig. 4g-i)
TRANSIENT_SD = 1.5  # "above 1.5 sigma in z-score activity" (legend of Extended Data Fig. 4g)


def transients(y, rate=RATE, thr=TRANSIENT_SD):
    """Upward crossings of thr in a z-scored trace. Returns (onsets, peak values, peak frames);
    a transient runs from the crossing up to the next crossing down."""
    above = y > thr
    on = np.nonzero(above[1:] & ~above[:-1])[0] + 1
    if above[0]:
        on = np.r_[0, on]
    peaks, pk_idx = [], []
    for o in on:
        off = o + np.argmax(~above[o:]) if (~above[o:]).any() else len(y)
        i = o + int(np.argmax(y[o:off]))
        peaks.append(y[i])
        pk_idx.append(i)
    return on, np.array(peaks), np.array(pk_idx, int)


def decay_tau(y, peak_idx, rate=RATE, window_s=10.0):
    """Decay constant of the mean transient: an exponential a*exp(-t/tau)+c fit to the mean trace
    from the peak over 10 s (claims, ed4hi: 'an exponential fit to the mean transient from its
    peak'; the 10 s window is a standard choice). NaN if there is no complete transient."""
    from scipy.optimize import curve_fit
    n = int(window_s * rate)
    segs = [y[i:i + n] for i in peak_idx if i + n <= len(y)]
    if not segs:
        return np.nan
    m = np.mean(segs, axis=0)
    t = np.arange(n) / rate
    try:
        p, _ = curve_fit(lambda t, a, tau, c: a * np.exp(-t / tau) + c, t, m,
                         p0=(max(m[0] - m[-1], 1e-3), 1.0, m[-1]), bounds=([0, 0.05, -np.inf], [np.inf, 100, np.inf]), maxfev=20000)
        return float(p[1])
    except RuntimeError:
        return np.nan


# --------------------------------------------------------------------------------------
# Fivefold cross-validation (paper, Methods: "We cross-validated the model using fivefold
# cross-validation, for which we trained the data on four arbitrary portions of the data and tested
# on a left out fifth portion"; "selecting the optimal number of states through fivefold
# cross-validation")
def _cv_job(key, Y, kw, fold, n_folds=5, test_iters=50):
    """Train on four contiguous blocks (as separate sequences), infer the latents of the held-out
    block with the parameters fixed, and score it two ways:
    neural R2: activity predicted from the inferred latents (C x + d) against the activity, pooled
    over neurons, against the held-out block's mean (claims, methods-cvr2), and against the session
    mean (neural_r2_session); latent R2: the sample code's R2 of the inferred latents
    against their forward prediction, on the held-out block."""
    limit_threads()
    ensure_ssm()
    import autograd.numpy.random as npr
    import ssm
    blocks = np.array_split(np.arange(len(Y)), n_folds)
    train = [Y[b] for i, b in enumerate(blocks) if i != fold]
    test = Y[blocks[fold]]
    npr.seed(kw.get("seed", 0))
    np.random.seed(kw.get("seed", 0))
    m = ssm.SLDS(N=Y.shape[1], K=kw["K"], D=2, transitions="recurrent_only", dynamics="gaussian",
                 emissions="gaussian", single_subspace=True,
                 dynamics_kwargs=dict(l2_penalty_A=kw["l2_A"]), transitions_kwargs=dict(l2_penalty=kw["l2"]))
    m.initialize(train)
    m.fit(train, method="laplace_em", variational_posterior="structured_meanfield", initialize=False,
          num_iters=kw["iters"], alpha=kw["alpha"], verbose=0)
    _, post = m.approximate_posterior(test, method="laplace_em", variational_posterior="structured_meanfield",
                                      num_iters=test_iters, verbose=0)
    x = post.mean_continuous_states[0]
    pred = x @ m.emissions.Cs[0].T + m.emissions.ds[0]
    neural = 1 - np.sum((test - pred) ** 2) / np.sum((test - test.mean(0)) ** 2)
    # the same error against the session mean of the z-scored activity (0) in place of the
    # held-out block's own mean, which differs from block to block
    neural_session = 1 - np.sum((test - pred) ** 2) / np.sum(test ** 2)
    z = m.most_likely_states(x, test)
    fit = dict(As=np.array(m.dynamics.As), bs=np.array(m.dynamics.bs), xhat=x, zhat=z)
    latent = code_r2(fit)
    return key, dict(neural_r2=float(neural), neural_r2_session=float(neural_session), latent_r2=float(latent))


def run_cv(jobs, n_jobs=None):
    """jobs: list of (key, Y, kwargs, fold)."""
    from joblib import Parallel, delayed
    n_jobs = n_jobs or min(4, os.cpu_count() or 1)
    return dict(Parallel(n_jobs=n_jobs)(delayed(_cv_job)(*j) for j in jobs))
