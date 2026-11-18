"""Loading and measures for DANDI:000978 (Single Day W-Track Learning, Shin and Jadhav), as used by
Wakhloo, Slatton and Chung (2026), "Neural population geometry and optimal coding of tasks with
shared latent structure", Nat Neurosci, doi:10.1038/s41593-025-02183-y.

Every parameter below comes from one of these sources, named where it is set:
- the claims file (claims/wakhloo-2026.yaml), whose opening comment gives the shared pipeline;
- the paper's Methods, "Spatial representations in rat PFC and CA1" (Rat data processing,
  Generalized linear model analysis, Readout analysis);
- the paper's code, github.com/awakhloo/population_geometry_optimal_coding at commit
  9674a6cb0c39926d70746024ce17de35f87df8f9 (code/process_rats.py, code/rat_utils.py,
  code/utils.py, code/run-pfc-hp-analysis-rats.py, code/fit-GLMs-rat.py), where the Methods are
  silent (protocol, author step 1.6, and reader step 2: the Methods first, then the code);
- standard choices, said to be one, for details that cannot change a result (seeds).

The files are streamed from the archive with remfile and h5py; nothing is written to disk.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

DANDISET = "000978"
VERSION = "0.240511.0307"   # the version the paper cites (ref. 67) and the latest published one
API = "https://api.dandiarchive.org/api"

# Rats in the order of the paper's code (process_rats.py); ZT2 has two files whose sessions it joins.
RATS = ["KL8", "ER1", "JS34", "JS14", "JS17", "JS21", "JS15", "ZT2"]
ZT2_FILES = ["sub-JDS-SingleDay-ZT2_obj-u40err_behavior+ecephys.nwb",
             "sub-JDS-SingleDay-ZT2_obj-1dss6zi_behavior+ecephys.nwb"]   # order of process_rats.py

# Methods, Rat data processing: 500 ms bins, speed of at least 4 cm/s, units of at least 0.1 Hz.
DT = 0.5
VMIN = 4.0
XMIN = 0.1
# Code (rat_utils.process_single_epoch): Nadaraya-Watson bandwidths, the Methods give no value.
SIGMA_POS = 0.05
SIGMA_VEL = 0.7
# Methods, Readout analysis: regulariser 0.02 Hz, i.e. 0.01 counts per 500 ms bin (code, eps = 0.01).
EPS = 0.01
N_SESSIONS = 8          # Methods: eight sessions; the code keeps the first eight (n_sesh = 8, [:S])
P_TRAIN = 300           # Methods: p = 300 training points
N_BINS_SUBSET = 500     # Methods: a random subset of 500 time bins per neuronal subset
N_TASKS = 500           # code (utils.emp_error): 500 Gaussian task vectors
MAX_BIAS = 0.25         # code (utils.emp_error): keep tasks with |mean label| < 0.25
N_UNITS = {"PFC": 19, "CA1": 24}   # Methods; the code uses 19 for both (a variant for CA1)

# GLM (Methods, Generalized linear model analysis; the code's chosen basis, figure notebook).
GLM_BIN_POS = 10        # cm
GLM_BIN_VEL = 3         # cm/s
GLM_VAR_POS = 100       # cm^2, variance of the isotropic position bases
GLM_VAR_VEL = 40        # (cm/s)^2
GLM_MIN_COUNT = 20      # Methods: centres of bins holding more than 20 time bins
GLM_ALPHAS = np.logspace(-0.5, 2, 10)   # code: param_grid; Methods: 10 values
GLM_CV = 10             # Methods: 10-fold cross-validation (sklearn KFold, unshuffled, as GridSearchCV)


# ----------------------------------------------------------------------------------------------
# Archive access

def asset_urls() -> dict[str, str]:
    """Map each asset path of the pinned version to its S3 URL."""
    import requests
    out, url = {}, f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=100"
    while url:
        r = requests.get(url, timeout=60).json()
        for a in r["results"]:
            meta = requests.get(f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/{a['asset_id']}/",
                                timeout=60).json()
            s3 = [u for u in meta["contentUrl"] if "s3" in u][0]
            out[a["path"]] = s3
        url = r.get("next")
    return out


def open_nwb(url: str):
    import h5py
    import remfile
    return h5py.File(remfile.File(url), "r")


def _str(x):
    return x.decode() if isinstance(x, bytes) else str(x)


def read_file(url: str) -> dict:
    """Read from one NWB file only what the analysis needs: trials, epochs, position, the spike
    times of every unit and the area of each unit (from its electrode's location)."""
    f = open_nwb(url)
    tr = f["intervals/trials"]
    trials = pd.DataFrame({k: tr[k][:] for k in ["start_time", "stop_time", "correct",
                                                   "trajectory_type", "start_well", "end_well"]})
    ep = f["intervals/epoch intervals"]
    epochs = pd.DataFrame({"start_time": ep["start_time"][:], "stop_time": ep["stop_time"][:]})
    pos = f["processing/behavior/Position/SpatialSeries"]
    pos_t = pos["timestamps"][:]
    pos_d = pos["data"][:]
    st = f["units/spike_times"][:]
    idx = f["units/spike_times_index"][:].astype(int)
    spikes = np.split(st, idx[:-1])
    el_loc = np.array([_str(s) for s in f["general/extracellular_ephys/electrodes/location"][:]])
    el_id = f["general/extracellular_ephys/electrodes/id"][:]
    unit_el = f["units/electrodes"][:]
    # units/electrodes holds row indices into the electrodes table
    unit_loc = el_loc[unit_el]
    info = {"subject_id": _str(f["general/subject/subject_id"][()]),
            "session_id": _str(f["general/session_id"][()]),
            "pos_unit": _str(pos["data"].attrs.get("unit", "")),
            "n_electrodes": len(el_id),
            "ephys_shape": f["acquisition/ElectricalSeries/data"].shape}
    f.close()
    return dict(trials=trials, epochs=epochs, pos_t=pos_t, pos_d=pos_d, spikes=spikes,
                unit_loc=unit_loc, info=info)


# ----------------------------------------------------------------------------------------------
# Binning (code: rat_utils.get_trl_dat and process_single_epoch)

def assign_epochs(trials: pd.DataFrame, epochs: pd.DataFrame) -> pd.Series:
    """Epoch index of each trial, as rat_utils.get_trl_dat: a trial gets index i (i >= 1) of the
    epoch interval that contains it, and 0 otherwise."""
    ep = np.zeros(len(trials))
    for i in range(1, len(epochs)):
        m = (trials.start_time >= epochs.start_time[i]) & (trials.stop_time <= epochs.stop_time[i])
        ep[m.values] = i
    return pd.Series(ep, index=trials.index)


def nadaraya(x, y, x_eval, h, width=10.0):
    """One-dimensional Nadaraya-Watson smoothing with a Gaussian kernel of bandwidth h, as
    rat_utils.nadaraya. Samples beyond `width` bandwidths are left out; their weight is below
    exp(-50) relative to the centre, so this changes nothing (a standard choice for speed)."""
    lo = np.searchsorted(x, x_eval - width * h)
    hi = np.searchsorted(x, x_eval + width * h)
    out = np.full(len(x_eval), np.nan)
    for k in range(len(x_eval)):
        xs = x[lo[k]:hi[k]]
        if len(xs) == 0:
            continue
        w = np.exp(-0.5 * ((x_eval[k] - xs) / h) ** 2)
        out[k] = np.sum(w * y[lo[k]:hi[k]]) / np.sum(w)
    return out


def bin_session(trials_ep, spikes, pos_t, pos_d, dt=DT):
    """Bin one session (epoch), as rat_utils.process_single_epoch. Returns the counts (bins x
    units) and the latents per bin: x, y, speed (smoothed with SIGMA_POS), x and y velocity (from
    position differences, smoothed with SIGMA_VEL), correct and trajectory type of the trial."""
    start, stop = trials_ep.start_time.min(), trials_ep.stop_time.max()
    gaps = trials_ep.start_time.values[1:] - trials_ep.stop_time.values[:-1]
    T = start + np.arange(int((stop - start) / dt)) * dt
    counts = np.stack([np.histogram(s, bins=T)[0] for s in spikes], axis=1).astype(float)
    m = (pos_t >= start) & (pos_t <= stop)
    tt, b = pos_t[m], pos_d[m]
    bt = T[:-1] + dt / 2
    nx, ny, nv = (nadaraya(tt, b[:, k], bt, SIGMA_POS) for k in range(3))
    dtt = tt[1:] - tt[:-1]
    dx, dy = (b[1:, 0] - b[:-1, 0]) / dtt, (b[1:, 1] - b[:-1, 1]) / dtt
    vt = (tt[1:] + tt[:-1]) / 2
    ndx, ndy = nadaraya(vt, dx, bt, SIGMA_VEL), nadaraya(vt, dy, bt, SIGMA_VEL)
    acc = np.full(len(bt), np.nan)
    traj = acc.copy()
    for _, r in trials_ep.iterrows():
        mm = (bt >= r.start_time) & (bt < r.stop_time)
        acc[mm] = r.correct
        traj[mm] = r.trajectory_type
    z = np.stack([nx, ny, nv, ndx, ndy, acc, traj], axis=1)
    return counts, z, float(np.max(np.abs(gaps))) if len(gaps) else 0.0


def load_rat(rat: str, urls: dict) -> dict:
    """All sessions of one rat, in order. For ZT2 the sessions of its two files are joined, as
    process_rats.py does; each file has its own units."""
    if rat == "ZT2":
        paths = [f"sub-JDS-SingleDay-ZT2/{f}" for f in ZT2_FILES]
    else:
        paths = [f"sub-JDS-SingleDay-{rat}/sub-JDS-SingleDay-{rat}_behavior+ecephys.nwb"]
    sessions, raw = [], []
    for fi, p in enumerate(paths):
        d = read_file(urls[p])
        trials = d["trials"].copy()
        trials["epoch"] = assign_epochs(trials, d["epochs"])
        for e in pd.unique(trials.epoch):
            te = trials[trials.epoch == e].sort_values("start_time")
            counts, z, gap = bin_session(te, d["spikes"], d["pos_t"], d["pos_d"])
            sessions.append(dict(counts=counts, z=z, loc=d["unit_loc"], epoch=int(e), file=fi,
                                 n_trials=len(te), frac_correct=float(te.correct.mean()),
                                 max_gap=gap, start=te.start_time.min(), stop=te.stop_time.max()))
        raw.append(dict(path=p, info=d["info"], trials=trials, epochs=d["epochs"],
                        n_units=len(d["spikes"]), unit_loc=d["unit_loc"],
                        n_spikes=np.array([len(s) for s in d["spikes"]]),
                        spike_hashes=[hash(np.round(s, 4).tobytes()) for s in d["spikes"]],
                        pos_hash=hash(np.round(d["pos_d"][:2000], 3).tobytes()),
                        spikes_sorted=all(np.all(np.diff(s) >= 0) for s in d["spikes"]),
                        pos_range=(np.nanmin(d["pos_d"], 0), np.nanmax(d["pos_d"], 0)),
                        pos_dt=np.median(np.diff(d["pos_t"])),
                        pos_t_range=(d["pos_t"][0], d["pos_t"][-1]),
                        spike_t_range=(min(s.min() for s in d["spikes"] if len(s)),
                                       max(s.max() for s in d["spikes"] if len(s)))))
    return dict(rat=rat, sessions=sessions, raw=raw)


# ----------------------------------------------------------------------------------------------
# Readout analysis (Methods, Readout analysis; code: rat_utils.process_dat, utils.*)

def process_session(counts, z, loc, area, speed="velocity"):
    """Locomotion bins, units of the area above XMIN Hz, units normalised and latents z-scored,
    as rat_utils.process_dat. Speed is the norm of the smoothed velocity (code); `speed="column"`
    uses the dataset's speed column, as the GLM code does. Returns x (bins x units) and the
    latents x, y position and x, y velocity (bins x 4), z-scored."""
    sp = np.linalg.norm(z[:, 3:5], axis=1) if speed == "velocity" else z[:, 2]
    m = sp > VMIN
    x, zz = counts[m][:, loc == area], z[m]
    keep = x.mean(0) / DT > XMIN
    x = x[:, keep]
    x = (x - x.mean(0)) / (EPS + x.std(0))
    zz = zz[:, [0, 1, 3, 4]]
    zz = (zz - zz.mean(0)) / zz.std(0)
    return x, zz


def covariances(x, z):
    n = x.shape[1]
    X = np.concatenate([x, z], axis=1)
    X = X - X.mean(0)
    C = X.T @ X / X.shape[0]
    return C[:n, :n], C[:n, n:], C[n:, n:]


def geometry(Psi, Phi, Omega):
    """Eqs. 6 to 9 (code: utils.get_geometry): total dimension, neural-latent correlation, SNF and
    SSF."""
    Om_inv = np.linalg.inv(Omega)
    tPP = np.trace(Phi @ Phi.T)
    dim = np.trace(Psi) ** 2 / np.sum(Psi ** 2)
    ssf = tPP ** 2 / np.trace(Omega) / np.trace(Phi.T @ Phi @ Om_inv @ Phi.T @ Phi)
    snf = tPP ** 2 / np.trace(Omega) / np.trace(Phi.T @ (Psi - Phi @ Om_inv @ Phi.T) @ Phi)
    c = tPP / np.trace(Psi) / np.trace(Omega)
    return dim, c, snf, ssf


def theory_error(Psi, Phi, Omega, P):
    """Eq. 5 (code: utils.theory_part)."""
    T1 = np.pi / P * np.trace(Psi @ Psi.T) * np.trace(Omega)
    T2 = 2 * (np.trace(Phi.T @ Psi @ Phi) - np.trace(Phi.T @ Phi) ** 2 / np.trace(Omega))
    T3 = np.sqrt(2) * np.trace(Phi @ Phi.T)
    return 1 / np.pi * np.arctan(np.sqrt(np.trace(Omega) * (T1 + T2)) / T3)


def tasks(z, rng, n_task=N_TASKS):
    """Random Gaussian task vectors and their labels, keeping tasks with |mean label| < MAX_BIAS
    (code: utils.emp_error)."""
    teach = rng.standard_normal((z.shape[1], n_task))
    lab = np.sign(z @ teach)
    return lab[:, np.abs(lab.mean(0)) < MAX_BIAS]


def hebbian_error(x, lab, train, test, P):
    """Empirical error of the Hebbian readout of Eq. 3, mean over tasks (code: utils.emp_error)."""
    W = lab[train].T @ x[train] / P
    yhat = np.sign(x[test] @ W.T)
    return float(np.mean(-lab[test] * yhat > 0))


def svc_error(x, lab, train, test):
    """Error of a linear SVC per task on the same split (code: utils.emp_error, LinearSVC with
    dual='auto', max_iter=10000, labels cast to 0 and 1)."""
    from sklearn.svm import LinearSVC
    errs = []
    for k in range(lab.shape[1]):
        clf = LinearSVC(dual="auto", max_iter=10_000).fit(x[train], lab[train, k])
        errs.append(np.mean(clf.predict(x[test]) != lab[test, k]))
    return float(np.mean(errs))


def readout_subsets(x, z, n_units, rng, n_subsets, P=P_TRAIN, n_bins=N_BINS_SUBSET, svc_every=0):
    """For each random subset of n_units units and n_bins bins (Methods, Readout analysis):
    theoretical error (Eq. 5), empirical Hebbian error, dimension, correlation, SNF, SSF, and the
    SVC error on every `svc_every`-th subset (nan elsewhere). Returns an array (n_subsets x 7)."""
    out = np.full((n_subsets, 7), np.nan)
    for g in range(n_subsets):
        bi = rng.choice(x.shape[0], size=n_bins, replace=False)
        ui = rng.choice(x.shape[1], size=n_units, replace=False)
        xs, zs = x[bi][:, ui], z[bi]
        Psi, Phi, Omega = covariances(xs, zs)
        lab = tasks(zs, rng)
        train = rng.choice(n_bins, size=P, replace=False)
        test = np.setdiff1d(np.arange(n_bins), train)
        out[g, 0] = theory_error(Psi, Phi, Omega, P)
        out[g, 1] = hebbian_error(xs, lab, train, test, P)
        out[g, 2:6] = geometry(Psi, Phi, Omega)
        if svc_every and g % svc_every == 0:
            out[g, 6] = svc_error(xs, lab, train, test)
    return out


# ----------------------------------------------------------------------------------------------
# GLM (Methods, Generalized linear model analysis; code: fit-GLMs-rat.py, rat_utils)

def glm_session_data(counts, z, loc, area):
    """As rat_utils.get_all_lat: bins with the dataset's speed column above VMIN, units of the
    area, positions centred within the session, velocities in cm/s."""
    m = z[:, 2] > VMIN
    x, zz = counts[m][:, loc == area], z[m].copy()
    zz[:, :2] = zz[:, :2] - zz[:, :2].mean(0)
    return x, zz


def basis_centres(flat_z):
    """Basis centres from all of a rat's sessions (rat_utils.bin_positions, bin_velocities)."""
    def bins(v, size):
        b, c = np.unique((v / size).round(0) * size, axis=0, return_counts=True)
        return b[c > GLM_MIN_COUNT]
    return bins(flat_z[:, :2], GLM_BIN_POS), bins(flat_z[:, 3], GLM_BIN_VEL), bins(flat_z[:, 4], GLM_BIN_VEL)


def glm_covariates(z, centres):
    """Isotropic Gaussian position bases, separate for inbound and outbound trajectories, and
    one-dimensional Gaussian velocity bases (rat_utils.get_covs, iso_gauss, gauss_basis),
    standardised per column as fit-GLMs-rat.py does."""
    cp, cvx, cvy = centres
    s, sv = GLM_VAR_POS, GLM_VAR_VEL
    d2 = ((z[:, None, :2] - cp[None]) ** 2).sum(-1)
    pc = np.exp(-d2 / (2 * s)) / (2 * np.pi * s)
    vx = np.exp(-(z[:, 3:4] - cvx[None]) ** 2 / (2 * sv)) / np.sqrt(2 * np.pi * sv)
    vy = np.exp(-(z[:, 4:5] - cvy[None]) ** 2 / (2 * sv)) / np.sqrt(2 * np.pi * sv)
    traj = z[:, 6]
    p0, p1 = pc.copy(), pc.copy()
    p0[traj == 1] = 0
    p1[traj == 0] = 0
    covs = np.concatenate([p0, p1, vx, vy], axis=1)
    sd = covs.std(0)
    return (covs - covs.mean(0)) / sd, int(np.sum(~(sd > 0)))


def fit_unit_glm(covs, y, alphas=GLM_ALPHAS, cv=GLM_CV):
    """10-fold cross-validated l2 penalty for one unit, as fit-GLMs-rat.py: GridSearchCV over
    PoissonRegressor with cv=10 (sklearn's unshuffled KFold for a regressor, so the folds are
    fixed) and the code's refit rule (the best nan-mean of the fold scores). Scores are D2, the
    default score of PoissonRegressor (nan when a fold cannot be scored). Returns the mean fold
    score per alpha, the number of valid folds per alpha, and the prediction of the refitted
    best model (code: get_test_scores, model.predict)."""
    from functools import partial
    from sklearn.linear_model import PoissonRegressor
    from sklearn.model_selection import GridSearchCV
    import warnings
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        search = GridSearchCV(PoissonRegressor(), {"alpha": alphas}, cv=cv, error_score=np.nan,
                              refit=partial(_refit, cv=cv))
        search.fit(covs, y)
    scores = np.stack([search.cv_results_[f"split{i}_test_score"] for i in range(cv)])
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        mean = np.nanmean(scores, axis=0)
    return mean, np.sum(np.isfinite(scores), axis=0), search.predict(covs)


def _refit(cv_results, cv):
    """The code's refit_strategy: the alpha with the best nan-mean fold score."""
    import warnings
    s = np.stack([cv_results[f"split{i}_test_score"] for i in range(cv)])
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        m = np.nanmean(s, axis=0)
    return int(np.nanargmax(m)) if np.any(np.isfinite(m)) else 0


def glm_session(counts, z, loc, area, centres):
    """Fit every unit of one session and area (fit-GLMs-rat.py). Units are those above XMIN Hz in
    the bins kept. Returns the counts, the predictions, the mean fold scores (units x alphas) and
    the valid fold counts."""
    x, zz = glm_session_data(counts, z, loc, area)
    covs, nbad = glm_covariates(zz, centres)
    x = x[:, x.mean(0) / DT > XMIN]
    res = [fit_unit_glm(covs, x[:, u]) for u in range(x.shape[1])]
    return dict(x=x, xhat=np.stack([r[2] for r in res], axis=1),
                scores=np.stack([r[0] for r in res]), nvalid=np.stack([r[1] for r in res]),
                n_covariates=covs.shape[1], n_constant_covariates=nbad)


def glm_summary(res, n_units, rng, n_subsets=500, frac_val=0.9, cv=GLM_CV):
    """As rat_utils.format_glm_results: each unit's best mean fold D2, chosen with np.argmax over
    the alphas as the code does, so a unit with a nan mean score at any alpha gets a nan best
    score. The population D2 is the mean over units (nan when a unit's best score is nan, as the
    code's mean); further readings are the nan-mean over units, and the mean with the scores of
    units replaced by the null model set to 0. Units whose best score is <= 0, nan, or with fewer
    than 90% valid folds are replaced by the null model (a constant), and the task-relevant
    dimension is the mean participation ratio of the z-scored predictions over random sets of
    n_units units."""
    sc = res["scores"]
    bi = np.argmax(sc, axis=1)   # as the code: np.argmax picks a nan entry when a unit has one
    best = sc[np.arange(len(sc)), bi]
    nv = res["nvalid"][np.arange(len(sc)), bi]
    zero = (best <= 0) | (nv < frac_val * cv) | np.isnan(best)
    xh = res["xhat"].copy()
    xh[:, zero] = 0.0
    n_units = min(n_units, xh.shape[1])   # every session has enough units in the full run; printed
    prs = [participation_ratio(xh[:, rng.choice(xh.shape[1], size=n_units, replace=False)])
           for _ in range(n_subsets)]
    with np.errstate(invalid="ignore"):
        d2_nan = float(np.nanmean(best))
    return dict(d2=float(np.mean(best)), d2_unit_nanmean=d2_nan, d2_null0=float(np.mean(np.where(zero, 0.0, best))),
                n_units=len(best), n_null=int(zero.sum()), n_sub=n_units, task_dim=float(np.mean(prs)))


def participation_ratio(xh, eps=EPS):
    """rat_utils.get_pr: participation ratio after z-scoring with a small regulariser."""
    if np.all(xh.std(0) == 0.0):
        return 0.0
    xh = (xh - xh.mean(0)) / (xh.std(0) + eps)
    Psi = xh.T @ xh / xh.shape[0]
    return float(np.trace(Psi) ** 2 / np.sum(Psi ** 2))


# ----------------------------------------------------------------------------------------------
# Statistics (Methods, Readout analysis: y_it = beta_i + gamma t + eta t^2; figure notebook
# Fig-readout-with-learning-hp-pfc.ipynb, fit_quad_mixed and fit_lin_mixed)

def fit_mixed(g, quad=True, t0=0, sessions=None):
    """Mixed model with a random intercept per rat (statsmodels mixedlm, REML, Wald P values).
    g is rats x sessions; sessions are coded t0, t0 + 1, ... (the code uses t0 = 0). Returns
    (gamma, eta, p_gamma, p_eta); eta and p_eta are nan for the linear model."""
    import warnings
    import statsmodels.formula.api as smf
    if sessions is not None:
        g = g[:, sessions]
    nr, ns = g.shape
    df = pd.DataFrame({"Y": g.reshape(-1), "time": np.tile(np.arange(ns) + t0, nr).astype(float),
                       "subject": np.repeat(np.arange(nr), ns).astype(str)})
    df["time_squared"] = df.time ** 2
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        res = smf.mixedlm("Y ~ time + time_squared" if quad else "Y ~ time", df,
                          groups=df["subject"]).fit()
    if quad:
        return (res.params["time"], res.params["time_squared"], res.pvalues["time"],
                res.pvalues["time_squared"])
    return res.params["time"], np.nan, res.pvalues["time"], np.nan


def decode_r2(x, y, shift=0, folds=5, ridge=1.0):
    """Cross-validated R2 of a ridge regression of y (bins x k) on x (bins x units), with x
    shifted by `shift` bins (circularly) against y; contiguous folds. Used only for the clock
    check, a standard choice."""
    if shift:
        x = np.roll(x, shift, axis=0)
    n = len(y)
    pred = np.zeros_like(y)
    edges = np.linspace(0, n, folds + 1).astype(int)
    for a, b in zip(edges[:-1], edges[1:]):
        tr = np.r_[0:a, b:n]
        xm, ym = x[tr].mean(0), y[tr].mean(0)
        X = x[tr] - xm
        W = np.linalg.solve(X.T @ X + ridge * len(tr) * np.eye(x.shape[1]), X.T @ (y[tr] - ym))
        pred[a:b] = (x[a:b] - xm) @ W + ym
    return float(1 - np.sum((y - pred) ** 2) / np.sum((y - y.mean(0)) ** 2))
