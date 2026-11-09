"""Loading and measures for the rat context-dependent evidence accumulation task of dandiset 001550.

Pagan, Tang, Aoi, Pillow, Mante, Sussillo & Brody (2025), Nature 639, 421-429,
doi:10.1038/s41586-024-08433-6.

Each NWB file holds one behavioural session of one rat. The trials table holds, per trial, the
context (`HistorySection_task_history`, 'd' for location and 'f' for frequency), the correct side
(`HistorySection_side_history`), the outcome (`HistorySection_hit_history`: 1 correct, 0 error,
NaN violation), the generative evidence strengths (`gamma_dir`, `gamma_freq`) and the times of
every pulse, split by side and frequency (`left_hi`, `right_hi`, `left_lo`, `right_lo`, seconds
from the start of the pulse train). Files are streamed from the archive at the pinned version:
each file (0.5 to 2 MB) is read whole into memory and opened there; nothing is written to disk.

Where the parameters come from:

- Session selection (the paper's Methods): sessions with at least 100 valid trials, a fraction
  correct of at least 0.7 and a feature selection index of at least 0.7. The paper's code
  (https://github.com/Brody-Lab/flexible_decision_making_rats at commit
  0ea8fdb7c56d755d99155171cc314dbbc24393ac) applies the same thresholds through
  compute_logistic_regression.m, adds a per-session `good` flag that the dandiset does not hold,
  and uses 0.65 and 0.6 for the seven recorded rats (compute_logistic_regression_all_ephys_rats.m).
- Feature selection index (Methods, equations 4 to 8): one logistic regression per context of
  choice on the location and frequency strengths, the relative weight of the relevant feature,
  averaged over the two contexts. The Methods use rate differences; the dandiset stores the
  generative log rate ratios (`gamma_dir`, `gamma_freq`), which are used here.
- Behavioural kernels (Methods, equation 9, and compute_logistic_regression.m): pulses counted in
  26 bins of 50 ms over the 1.3 s train; per bin the natural log of the ratio of right to left
  (high to low) counts, each count plus machine epsilon as in the code (`EPS`); one logistic
  regression per context with an intercept and 26 location and 26 frequency weights. The
  Methods call it ridge regression with the regulariser chosen by cross-validation; the code
  (costFunction.m) adds 200 times the squared differences of neighbouring weights to the mean
  log loss. `kernels` uses the code's penalty form with its weight chosen by 3-fold
  cross-validation over `CV_LAMS` (grid and folds chosen here), or a fixed weight such as 200.
- Neural slope indices and choice-axis angles (`neural_slopes`, `choice_axis_angle`) port
  get_neural_slope.m and ExtDataFigure5ag.m (both of its angles), applied to the paper's fitted per-neuron kernels
  (data/combined_kernels*.mat in the repository above, read with `paper_mat`).
- Slope index (Methods, and compute_slope.m / plot_logistic_regression.m): the differential
  kernel (relevant minus irrelevant context weights) divided by its largest absolute value, as
  the code does, and the slope of a least-squares line against the bin centres in seconds.
- Trial position in a block (`nta`, used by compute_taskswitch.m) counts all trials since the
  last change of context, violations included, as in the paper's data.
"""

from __future__ import annotations

import re
import io
import multiprocessing as mp
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import requests
from dandi.dandiapi import DandiAPIClient
from scipy.optimize import minimize

DANDISET_ID = "001550"
DANDISET_VERSION = "0.260916.0811"
TASK_PROTOCOLS = ("TaskSwitch4", "TaskSwitch4new", "TaskSwitch6")  # those in the paper's data

STIM_DURATION = 1.3            # s, Methods
BIN_S = 0.05                   # s, Methods and code
N_BINS = 26
BIN_CENTRES = (np.arange(N_BINS) + 0.5) * BIN_S
EPS = np.finfo(float).eps      # compute_logistic_regression.m adds eps to every count
MIN_VALID, MIN_HIT, MIN_FSI = 100, 0.7, 0.7          # Methods
CV_LAMS = (20.0, 200.0, 2000.0)  # chosen here around the code's 200
LOOSE_HIT, LOOSE_FSI = 0.6, 0.6  # bins are kept for sessions passing these, below every variant
PULSE_KEYS = ("right_hi", "left_hi", "right_lo", "left_lo")
REQUIRED = ("HistorySection_result_history", "HistorySection_task_history",
            "HistorySection_side_history", "gamma_dir", "gamma_freq") + PULSE_KEYS


def asset_table() -> pd.DataFrame:
    """Every NWB file at the pinned version: path, subject, protocol, session id and S3 URL,
    from one paginated listing with metadata (one request per 1000 assets)."""
    rows = []
    with DandiAPIClient() as client:
        listing = client.paginate(
            f"/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/",
            params={"metadata": "true", "page_size": 1000})
        for a in listing:
            m = re.match(r"sub-([^/]+)/sub-[^_]+_ses-(.+)-(\d{6}[a-z])\.nwb$", a["path"])
            url = [u for u in a["metadata"]["contentUrl"] if "s3.amazonaws.com" in u][0]
            rows.append(dict(path=a["path"], subject=m.group(1), protocol=m.group(2),
                             session=f"{m.group(2)}-{m.group(3)}", date=m.group(3)[:6],
                             size=a["size"], url=url))
    return pd.DataFrame(rows).sort_values(["subject", "session"]).reset_index(drop=True)


def _ragged(group, key):
    data = group[key][:]
    index = group[f"{key}_index"][:].astype(np.int64)
    return np.split(data, index[:-1])


def _text(arr):
    return np.array([x.decode() if isinstance(x, bytes) else str(x) for x in arr])


def bin_pulses(group, key, trial_idx, bin_s=BIN_S, n_bins=N_BINS):
    """Counts of the pulse times of ragged column `key` for the trials `trial_idx`, in bins of
    `bin_s` seconds from 0 (trials x bins), with the number of pulses outside the bins. A pulse
    at exactly n_bins * bin_s goes in the last bin, as the code's eps on the last edge does."""
    data = group[key][:]
    index = group[f"{key}_index"][:].astype(np.int64)
    counts = np.diff(np.concatenate([[0], index]))
    owner = np.repeat(np.arange(len(index)), counts)
    pos = np.full(len(index), -1)
    pos[trial_idx] = np.arange(len(trial_idx))
    keep = pos[owner] >= 0
    t, row = data[keep], pos[owner[keep]]
    b = np.floor(np.round(t / bin_s, 9)).astype(np.int64)
    b[np.isclose(t, n_bins * bin_s)] = n_bins - 1
    inside = (b >= 0) & (b < n_bins)
    out = np.bincount(row[inside] * n_bins + b[inside], minlength=len(trial_idx) * n_bins)
    return out.reshape(len(trial_idx), n_bins).astype(np.uint8), int((~inside).sum()), t


def relative_weights(choice, task, gdir, gfreq):
    """Methods equations 4 to 8: relative weight of location in the location context, of
    frequency in the frequency context, and their mean (the feature selection index)."""
    out = {}
    for ctx in ("d", "f"):
        m = task == ctx
        if m.sum() < 10 or np.std(gdir[m]) == 0 or np.std(gfreq[m]) == 0:
            out[ctx] = (np.nan, np.nan)
            continue
        X = np.column_stack([np.ones(m.sum()), gdir[m], gfreq[m]])
        w = _irls(X, choice[m].astype(float))
        out[ctx] = (w[1], w[2])
    wdd, wfd = out["d"]
    wdf, wff = out["f"]
    rel_loc = wdd / (wdd + wfd)
    rel_frq = wff / (wdf + wff)
    return rel_loc, rel_frq, (rel_loc + rel_frq) / 2


def _irls(X, y, n_iter=25):
    w = np.zeros(X.shape[1])
    for _ in range(n_iter):
        p = 1 / (1 + np.exp(-np.clip(X @ w, -30, 30)))
        g = X.T @ (y - p)
        H = (X * (p * (1 - p))[:, None]).T @ X + 1e-9 * np.eye(X.shape[1])
        step = np.linalg.solve(H, g)
        w += step
        if np.max(np.abs(step)) < 1e-8:
            break
    return w


_http = None


def fetch(url: str) -> bytes:
    """The whole file, read into memory (nothing is written to disk)."""
    global _http
    if _http is None:
        _http = requests.Session()
        _http.mount("https://", requests.adapters.HTTPAdapter(pool_maxsize=16, max_retries=5))
    r = _http.get(url, timeout=120)
    r.raise_for_status()
    return r.content


def load_session(url: str, keep_bins: bool = True, bin_s: float = BIN_S, n_bins: int = N_BINS,
                 all_bins: bool = False) -> dict:
    """One session: per-trial outcome, context, evidence and position in block; session
    summaries; and the pulse counts of valid trials in bins of `bin_s` (valid trials x 4 x
    n_bins, in the order of `PULSE_KEYS`), kept only for sessions that pass the loose criteria
    unless `all_bins`."""
    with h5py.File(io.BytesIO(fetch(url)), "r") as f:
        tr = f["intervals/trials"]
        cols = set(tr.keys())
        missing = [c for c in REQUIRED if c not in cols]
        if missing:
            return dict(session=dict(missing=",".join(missing), n_trials=len(tr["id"])),
                        trials=None, pulses=None, opto=None)
        result = tr["HistorySection_result_history"][:].astype(int)
        n = len(result)
        # outcome from the result codes, as the hit_history description defines it
        hit = np.select([result == 1, np.isin(result, (2, 5, 6))], [1.0, 0.0], np.nan)
        has_hit_history = "HistorySection_hit_history" in cols
        hit_history_mismatch = (int(np.sum(~np.isclose(tr["HistorySection_hit_history"][:], hit,
                                                        equal_nan=True)))
                                if has_hit_history else -1)
        task = _text(tr["HistorySection_task_history"][:])
        side = _text(tr["HistorySection_side_history"][:])
        gdir = tr["gamma_dir"][:].astype(float)
        gfreq = tr["gamma_freq"][:].astype(float)
        hist_gfreq_dtype = str(tr["HistorySection_gammafreq_history"].dtype)
        hist_gfreq = tr["HistorySection_gammafreq_history"][:].astype(float)
        start = tr["start_time"][:]
        stop = tr["stop_time"][:]
        cpoke = tr["cpoke_start_time"][:]
        duration = tr["duration"][:]
        sess = dict(
            missing="",
            session_start=f["session_start_time"][()].decode(),
            date_of_birth=f["general/subject/date_of_birth"][()].decode(),
            sex=f["general/subject/sex"][()].decode(),
            strain=f["general/subject/strain"][()].decode(),
            n_trials=n, hist_gfreq_dtype=hist_gfreq_dtype, has_hit_history=has_hit_history,
            hit_history_mismatch=hit_history_mismatch,
            hist_gfreq_mismatch=int(np.sum(np.abs(hist_gfreq - gfreq) > 1e-9)),
        )
        opto_type = _text(tr["OptoSection_opto_type"][:]) if "OptoSection_opto_type" in cols else None
        opto_conn = (tr["OptoSection_opto_connected"][:].astype(int)
                     if "OptoSection_opto_connected" in cols else None)
        opto_lr = ({k: tr[f"HistorySection_opto_{k}_history"][:].astype(float) for k in ("left", "right")}
                   if "HistorySection_opto_left_history" in cols else None)
        opto = None
        if "opto_epochs" in f["intervals"]:
            oe = f["intervals/opto_epochs"]
            sites = _ragged(oe, "optogenetic_sites")
            opto = dict(start=oe["start_time"][:], stop=oe["stop_time"][:],
                        sites=[tuple(sorted(s.tolist())) for s in sites],
                        wavelength=oe["wavelength_in_nm"][:], power=oe["power_in_mW"][:])
        valid = ~np.isnan(hit)
        choice = np.where(valid, ((side == "r") == (hit == 1)).astype(float), np.nan)
        rel_loc, rel_frq, fsi = relative_weights(choice[valid].astype(int), task[valid],
                                                 gdir[valid], gfreq[valid])
        sess.update(valid=int(valid.sum()), hit=float(np.nanmean(hit)) if valid.any() else np.nan,
                    rel_loc=rel_loc, rel_frq=rel_frq, fsi=fsi)
        loose = bool(sess["valid"] >= MIN_VALID and sess["hit"] >= LOOSE_HIT
                     and np.nan_to_num(fsi) >= LOOSE_FSI)
        pulses = None
        sess.update(pulse_min=np.nan, pulse_max=np.nan, pulses_outside=0, pulses_per_trial=np.nan)
        if keep_bins and (loose or all_bins):
            vidx = np.flatnonzero(valid)
            parts = [bin_pulses(tr, k, vidx, bin_s, n_bins) for k in PULSE_KEYS]
            pulses = np.stack([p[0] for p in parts], 1)
            allt = np.concatenate([p[2] for p in parts])
            if allt.size:
                sess.update(pulse_min=float(allt.min()), pulse_max=float(allt.max()),
                            pulses_outside=sum(p[1] for p in parts),
                            pulses_per_trial=allt.size / max(len(vidx), 1))
    # trial position in block: all trials since the last change of context
    block = np.concatenate([[0], np.cumsum(task[1:] != task[:-1])])
    first = np.concatenate([[0], np.flatnonzero(task[1:] != task[:-1]) + 1])
    nta = np.arange(n) - first[block] + 1
    trials = pd.DataFrame(dict(hit=hit, task=task, side=side, result=result, gdir=gdir,
                               gfreq=gfreq, choice=choice, nta=nta, block=block, start=start,
                               stop=stop, cpoke=cpoke, duration=duration))
    if opto_type is not None:
        trials["opto_type"] = opto_type
    if opto_conn is not None:
        trials["opto_connected"] = opto_conn
    if opto_lr is not None:
        trials["opto_left"], trials["opto_right"] = opto_lr["left"], opto_lr["right"]
    sess["loose"] = loose
    return dict(session=sess, trials=trials, pulses=pulses, opto=opto)


def _load_chunk(args):
    urls, kw = args
    with ThreadPoolExecutor(8) as ex:
        return list(ex.map(lambda u: load_session(u, **kw), urls))


def load_many(urls, processes: int = 8, chunk: int = 40, **kw):
    """load_session over many URLs: `processes` worker processes, each fetching with 8 threads.
    Results come back in the order of `urls`; a failed read raises."""
    urls = list(urls)
    chunks = [(urls[i:i + chunk], kw) for i in range(0, len(urls), chunk)]
    with ProcessPoolExecutor(processes, mp_context=mp.get_context("fork")) as ex:
        return [r for part in ex.map(_load_chunk, chunks) for r in part]


def evidence_features(pulses: np.ndarray) -> np.ndarray:
    """Per bin log((right + eps) / (left + eps)) and log((high + eps) / (low + eps)), as in
    compute_logistic_regression.m; pulses are trials x 4 x 26 in the order of PULSE_KEYS."""
    p = pulses.astype(float)
    right = p[:, 0] + p[:, 2]
    left = p[:, 1] + p[:, 3]
    high = p[:, 0] + p[:, 1]
    low = p[:, 2] + p[:, 3]
    return np.hstack([np.log((right + EPS) / (left + EPS)), np.log((high + EPS) / (low + EPS))])


def fit_logistic(X, y, penalty: str = "ridge", lam: float = 0.0, w0=None) -> np.ndarray:
    """Logistic regression with an intercept (column 0 of X is added here): mean log loss plus
    `lam` times the sum of squared weights ("ridge") or of squared differences of neighbouring
    weights within each of the two 26-weight kernels ("smooth", costFunction.m). The intercept
    is not penalised."""
    Xa = np.column_stack([np.ones(len(X)), X])
    y = y.astype(float)
    m, k = Xa.shape
    nk = (k - 1) // 2

    def f(w):
        z = Xa @ w
        loss = np.mean(np.logaddexp(0, z) - y * z)
        p = 1 / (1 + np.exp(-z))
        grad = Xa.T @ (p - y) / m
        if penalty == "ridge":
            loss += lam * np.sum(w[1:] ** 2)
            grad[1:] += 2 * lam * w[1:]
        else:
            for a in (1, 1 + nk):
                d = np.diff(w[a:a + nk])
                loss += lam * np.sum(d ** 2)
                g = np.zeros(nk)
                g[:-1] -= 2 * lam * d
                g[1:] += 2 * lam * d
                grad[a:a + nk] += g
        return loss, grad

    res = minimize(f, np.zeros(k) if w0 is None else w0, jac=True, method="L-BFGS-B",
                   options=dict(maxiter=2000, gtol=1e-10, ftol=1e-14))
    if not res.success and "ABNORMAL" not in str(res.message):
        raise RuntimeError(f"fit did not converge: {res.message}")
    return res.x


def fit_cv(X, y, lams=CV_LAMS, n_folds: int = 3, seed: int = 0, penalty: str = "smooth"):
    """Penalty weight chosen by `n_folds`-fold cross-validated mean log loss over `lams` (folds
    random over trials from `seed`; grid and folds chosen here, as the Methods give neither).
    Returns the weights refitted on all trials, the chosen weight, and the CV loss per weight."""
    rng = np.random.default_rng(seed)
    folds = rng.permutation(len(y)) % n_folds
    cv = []
    for lam in lams:
        losses = []
        for k in range(n_folds):
            tr, te = folds != k, folds == k
            w = fit_logistic(X[tr], y[tr], penalty, lam)
            z = w[0] + X[te] @ w[1:]
            losses.append(np.mean(np.logaddexp(0, z) - y[te] * z))
        cv.append(np.mean(losses))
    best = lams[int(np.argmin(cv))]
    return fit_logistic(X, y, penalty, best), best, np.array(cv)


def kernels(X, y, task, lam=None, seed: int = 0) -> dict:
    """Behavioural kernels per context with the code's smoothness penalty: its weight chosen by
    `fit_cv` when `lam` is None, else fixed (a number, or a dict by context). Returns dd
    (location weights in the location context), fd (frequency weights, location context), df and
    ff (the same in the frequency context), and the weights used."""
    out = {}
    for ctx in ("d", "f"):
        m = task == ctx
        if lam is None:
            w, chosen, cv = fit_cv(X[m], y[m], seed=seed)
            out[f"cv_{ctx}"] = cv
        else:
            chosen = lam[ctx] if isinstance(lam, dict) else lam
            w = fit_logistic(X[m], y[m], "smooth", chosen)
        out[f"lam_{ctx}"] = chosen
        out[f"w_{ctx}"] = w
    out["dd"], out["fd"] = out["w_d"][1:27], out["w_d"][27:]
    out["df"], out["ff"] = out["w_f"][1:27], out["w_f"][27:]
    return out


def slope_index(diff, x=BIN_CENTRES, normalise: bool = True) -> float:
    """Slope of the least-squares line through the differential kernel against time (s); the
    kernel is divided by its largest absolute value first, as the paper's code does."""
    y = np.asarray(diff, float)
    if normalise:
        y = y / np.max(np.abs(y))
    return float(np.polyfit(x, y, 1)[0])


def slopes(k: dict, bins=slice(None), normalise: bool = True) -> tuple[float, float]:
    """(location, frequency) slope indices of a kernel dict, over the bins `bins`."""
    loc = k["dd"][bins] - k["df"][bins]
    frq = k["ff"][bins] - k["fd"][bins]
    x = BIN_CENTRES[bins]
    return slope_index(loc, x, normalise), slope_index(frq, x, normalise)


# ---- the paper's published data and code outputs (GitHub, pinned commit) ----

PAPER_REPO = "Brody-Lab/flexible_decision_making_rats"
PAPER_COMMIT = "0ea8fdb7c56d755d99155171cc314dbbc24393ac"
PAPER_EPHYS_RATS = ("P049", "P055", "P059", "P095", "P100", "P101", "P102")  # Figure5d.m


def paper_file(path: str) -> bytes:
    """A file of the paper's data repository at the pinned commit, read into memory."""
    return fetch(f"https://raw.githubusercontent.com/{PAPER_REPO}/{PAPER_COMMIT}/{path}")


def paper_mat(path: str, **kw) -> dict:
    from scipy.io import loadmat
    return loadmat(io.BytesIO(paper_file(path)), squeeze_me=True, struct_as_record=False, **kw)


def paper_session_name(source_file: str) -> str:
    """'data_@TaskSwitch4_Marino_P124_180709a.mat' -> 'TaskSwitch4-180709a'."""
    m = re.match(r"data_@(.+?)_[A-Za-z]+_\w+?_(\d{6}[a-z])\.mat$", source_file)
    return f"{m.group(1)}-{m.group(2)}"


def matlab_pc1(X: np.ndarray) -> np.ndarray:
    """First principal component coefficients of X (observations x variables) as MATLAB's pca
    gives them: columns centred, sign such that the largest absolute coefficient is positive."""
    Xc = X - X.mean(0)
    v = np.linalg.svd(Xc, full_matrices=False)[2][0]
    return v * np.sign(v[np.argmax(np.abs(v))])


KERNEL_T = np.arange(0.01, 0.66 + 1e-9, 0.02)      # get_neural_slope.m, 33 lags of 20 ms
CHOICE_T = np.arange(-1, 2 + 1e-9, 0.02)           # time of the choice kernels


def neural_slopes(k, rat_numbers, rat: int) -> tuple[float, float]:
    """get_neural_slope.m: choice axis as the first PC of the rat's neurons' choice kernels from
    0 to 1.3 s (sign so the projection at 1.3 s is positive); location and frequency
    differential pulse responses projected on it, time-reversed, divided by their largest
    absolute value; slope of a least-squares line against KERNEL_T."""
    ind = np.flatnonzero(rat_numbers == rat)
    i1, i2 = np.argmin(np.abs(CHOICE_T)), np.argmin(np.abs(CHOICE_T - 1.3))
    ch = k.glm_choice[i1:i2 + 1, ind]
    c = matlab_pc1(ch)
    if np.sign(ch[-1] @ c) < 0:
        c = -c
    out = []
    for rel, irr in ((k.glm_dd, k.glm_df), (k.glm_ff, k.glm_fd)):
        y = (c @ rel[:, ind].T - c @ irr[:, ind].T)[::-1]
        out.append(slope_index(y, KERNEL_T))
    return out[0], out[1]


def _angle(a, b) -> float:
    return float(np.degrees(np.arccos(np.clip(a @ b / np.linalg.norm(a) / np.linalg.norm(b), -1, 1))))


def choice_axis_angle(k_loc, k_frq, rat_numbers, rat: int) -> dict:
    """ExtDataFigure5ag.m, per rat. `full`: the angle (degrees) between the first PCs of the
    choice kernels from 0 s (66 time points) fitted in the location and in the frequency context,
    the code's first value of `ango`. `projected`: the value the code then writes over it and
    plots, the same two PCs projected on the first 3 PCs of both contexts' choice kernels from
    0 s (101 time points each, each divided by its matrix 2-norm as MATLAB's norm does, stacked),
    folded to at most 90 degrees. `var3`: the variance those 3 PCs explain."""
    good = ~np.isnan(k_loc.glm_choice.mean(0)) & ~np.isnan(k_frq.glm_choice.mean(0))
    ind = np.flatnonzero(good & (rat_numbers == rat))
    w1, w2 = k_loc.glm_choice[50:, ind], k_frq.glm_choice[50:, ind]
    a, b = matlab_pc1(w1[:66]), matlab_pc1(w2[:66])
    both = np.vstack([w1 / np.linalg.norm(w1, 2), w2 / np.linalg.norm(w2, 2)])
    _, sv, vt = np.linalg.svd(both - both.mean(0), full_matrices=False)
    pcs = vt[:3].T
    proj = _angle(a @ pcs, b @ pcs)
    return dict(full=_angle(a, b), projected=min(proj, 180 - proj), var3=float(np.sum(sv[:3] ** 2) / np.sum(sv ** 2)),
                units=len(ind))


def trial_symbols(task, gdir, gfreq, choice) -> str:
    """One character per trial coding context, both strengths and choice, to match runs."""
    levels = {-4.0: 0, -2.5: 1, -1.0: 2, 1.0: 3, 2.5: 4, 4.0: 5}
    gd = np.array([levels.get(float(g), 6) for g in gdir])
    gf = np.array([levels.get(float(g), 6) for g in gfreq])
    code = ((np.asarray(task) == "f") * 98 + gd * 14 + gf * 2 + np.asarray(choice).astype(int))
    return "".join(chr(0x100 + int(c)) for c in code)


def opto_trials(trials: pd.DataFrame, opto: dict) -> pd.DataFrame:
    """Each optogenetic epoch with the trial whose start and stop contain its start, its sites
    ('bilateral', 'left', 'right'), window ('full', 'first', 'second' half, from its length and
    its start relative to cpoke_start_time) and the offset from cpoke_start_time."""
    start = trials.start.values
    idx = np.searchsorted(start, opto["start"], side="right") - 1
    ok = (idx >= 0) & (opto["start"] <= trials.stop.values[np.clip(idx, 0, None)])
    names = {(0, 1): "bilateral", (0,): "left", (1,): "right"}
    dur = np.round(opto["stop"] - opto["start"], 3)
    offset = opto["start"] - trials.cpoke.values[np.clip(idx, 0, None)]
    window = np.where(dur > 1.0, "full", np.where(offset < 0.3, "first", "second"))
    return pd.DataFrame(dict(trial=idx, in_trial=ok, sites=[names.get(s, str(s)) for s in opto["sites"]],
                             duration=dur, offset=offset, window=window,
                             wavelength=opto["wavelength"], power=opto["power"]))


def is_subsequence(short: str, long: str) -> bool:
    """Whether `short` occurs in `long` in order, allowing gaps."""
    it = iter(long)
    return all(ch in it for ch in short)


def gap_match(cell_sym: str, sessions, window: int = 30) -> list:
    """Sessions (name, symbols) of which the cell's trials are an ordered subsequence. Candidates
    are the sessions that contain one of four windows of `window` trials taken from the cell."""
    n = len(cell_sym)
    starts = sorted({0, n // 4, n // 2, max(n - window, 0)})
    probes = [cell_sym[s:s + window] for s in starts if len(cell_sym[s:s + window]) == min(window, n)]
    cand = [(sid, s) for sid, s in sessions if any(p in s for p in probes)]
    return [sid for sid, s in cand if is_subsequence(cell_sym, s)]
