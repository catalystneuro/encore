"""Loading and LN-model measures for the head-fixed recordings of dandiset 000053.

Mallory, Hardcastle, Campbell, Attinger, Low, Raymond & Giocomo (2021), Nat Commun 12, 671,
doi:10.1038/s41467-021-20936-8.

Files are streamed from the archive at the pinned version, and the paper's deposit on figshare
(Dataset 3, doi:10.6084/m9.figshare.13426103.v1) is read in place only to say which dandiset files
are the paper's 11 recordings. Nothing is written to disk.

Where the parameters come from (the claims file's opening comment fixes the "LN pipeline", citing the
Methods, "LN model framework", and the spline code at github.com/khardcastle/spline-lnp-model commit
34b470f):

- 20 ms bins: the behaviour in the files is already at 50 Hz (Methods, "Spike sorting and
  synchronization": VR data resampled to a constant 50 Hz); spikes are counted in the 20 ms bin of
  each behaviour sample.
- Inner 98% (1st to 99th percentile) of each variable (Methods, "Data pre-processing"). The claims
  file leaves open whether out-of-range bins are dropped (reading a, `RANGE_DROP`) or each variable is
  clipped (reading b, `RANGE_CLIP`); both are run.
- Cardinal splines, tension s = 0.5 (spline_1d.m; Methods eq. 9), with control points 20 for
  position, 5 cm/s wide for speed and 5 for each eye variable (Methods, "Model formulation"). The
  claims file gives no rule for where the speed control points start; spacing them evenly over the
  inner range at about 5 cm/s, as spline_1d.m does from 0 with `spdVec`, is a standard choice.
- Poisson likelihood with an L2 penalty of weight 1 on all parameters, intercept included
  (glm_model.m). The fits are solved by Newton's method until the predicted fall of the objective
  is below 1e-6 (fminunc's default function tolerance); the per-fold fits start from the
  full-session solution and use the training Hessian there (a way to speed up the same fit, not a
  change of the objective).
- 10-fold cross-validation from 10-s sections, assigned to folds in turn (compute_test_train_ind.m;
  reading a, `FOLDS_TURN`) or at random (reading b, `FOLDS_RANDOM`), both named in the claims file.
- Performance is compute_llh.m: (log-likelihood of the model minus that of the test fold's mean
  rate) per spike, multiplied by log(2) as the code does. `BITS` converts it to bits per spike
  (dividing by log 2 in place of multiplying), a variant shown where the value itself is a claim.
- Forward search as forward_search_kfold.m: the first variable enters against a base of -5, each
  next one when a one-sided signed-rank test over the folds gives P < 0.05, and the cell encodes the
  selected variables when the selected model's folds exceed 0 by a one-sided signed-rank test
  (P < 0.05; the claims file's reading of the code's final test).
- Model-derived tuning curves by Methods eq. 10 with M = 200 bins over the variable's inner range,
  from the mean of the fold parameters (fit_model_kfold.m returns `param_mean`).
- Visualizing ranges (Methods, "Visualizing tuning curves") for the eye variables, in % of eye
  width (claims file, opening comment).
"""

from __future__ import annotations

import math
import os
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import remfile
from scipy import stats

DANDISET_ID = "000053"
DANDISET_VERSION = "0.210819.0345"
FIGSHARE_HEADFIXED_DOI = "10.6084/m9.figshare.13426103.v1"
# Files of figshare Dataset 3 (article 13426103, version 1), by the session number in their names.
FIGSHARE_FILES = {1: 25829867, 2: 25829879, 3: 25829885, 4: 25829918, 5: 25830317, 6: 25829999,
                  7: 25830023, 8: 25830032, 9: 25830044, 10: 25830065, 11: 25830074}

DT = 0.02
VARS = ["B", "Bs", "Eh", "Ev", "Ehd", "Evd"]
EYE = ["Eh", "Ev", "Ehd", "Evd"]
N_CPTS = {"B": 20, "Eh": 5, "Ev": 5, "Ehd": 5, "Evd": 5}
SPEED_STEP = 5.0
TENSION = 0.5
PCT = (1.0, 99.0)
NFOLDS = 10
SECTION = 500  # 10 s at 50 Hz
ALPHA = 0.05
M_BINS = 200
# Methods, "Visualizing tuning curves": preset bounds for the eye variables (eye units = % of eye width).
PRESET = {"Eh": (-3.0, 3.0), "Ev": (-2.0, 2.0), "Ehd": (-3.0, 3.0), "Evd": (-2.0, 2.0)}
EXPLORED_MIN = 0.8  # Methods, "Quantifying tuning curve shape": 80% of the range for eye variables
FEE_MIN = 0.9

RANGE_DROP, RANGE_CLIP = "drop", "clip"
FOLDS_TURN, FOLDS_RANDOM = "turn", "random"
LOG2 = math.log(2)


# ----------------------------------------------------------------------------------------- archive
def asset_urls(pattern: str = "") -> dict[str, str]:
    """{path: streaming URL} of the NWB files at the pinned version whose path contains `pattern`."""
    from dandi.dandiapi import DandiAPIClient
    with DandiAPIClient() as client:
        ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        return {a.path: a.get_content_url(follow_redirects=1, strip_query=True)
                for a in ds.get_assets() if pattern in a.path}


def _open(url: str) -> h5py.File:
    return h5py.File(remfile.File(url), "r")


def _text(v) -> str:
    v = v[()] if hasattr(v, "shape") else v
    return v.decode() if isinstance(v, bytes) else str(v)


def file_summary(url: str) -> dict:
    """Metadata and array shapes of one file, without reading its data."""
    f = _open(url)
    out = {"session_description": _text(f["session_description"]),
           "experiment_description": _text(f["general/experiment_description"]) if "general/experiment_description" in f else "",
           "subject_id": _text(f["general/subject/subject_id"]),
           "session_start": _text(f["session_start_time"]),
           "n_units": int(f["units/id"].shape[0]) if "units" in f else 0,
           "unit_columns": [c.decode() if isinstance(c, bytes) else c for c in f["units"].attrs["colnames"]] if "units" in f else [],
           "behavior": {}, "has_ecephys": "acquisition/ElectricalSeries" in f}
    if "processing/behavior" in f:
        def visit(name, obj):
            if isinstance(obj, h5py.Dataset) and name.endswith("data"):
                unit = obj.attrs.get("unit", "")
                out["behavior"][name[:-5]] = (obj.shape, unit.decode() if isinstance(unit, bytes) else unit)
        f["processing/behavior"].visititems(visit)
    for key in ["processing/behavior/Position/position/timestamps"]:
        if key in f:
            out["n_frames"] = int(f[key].shape[0])
    if "intervals/trials" in f:
        out["trial_columns"] = [c.decode() if isinstance(c, bytes) else c for c in f["intervals/trials"].attrs["colnames"]]
    if "general/extracellular_ephys/electrodes/location" in f:
        out["locations"] = sorted({_text(x) if not isinstance(x, (bytes, str)) else (x.decode() if isinstance(x, bytes) else x)
                                   for x in f["general/extracellular_ephys/electrodes/location"][:]})
    if "general/devices/Device" in f:
        out["device"] = f["general/devices/Device"].attrs.get("description", "")
    return out


def figshare_session(number: int) -> dict:
    """Cell count, animal, session name, frame count and the first cell's spikes and behaviour of one
    file of figshare Dataset 3, read in place over HTTP range requests."""
    import fsspec
    fh = fsspec.open(f"https://ndownloader.figshare.com/files/{FIGSHARE_FILES[number]}", block_size=2 ** 20).open()
    h = h5py.File(fh, "r")
    g = h["cell_info"]

    def get(name, i=0):
        a = h[g[name][i, 0]][()]
        return "".join(map(chr, a.ravel())) if a.dtype == np.uint16 else np.ravel(a)
    out = {"session": number, "n_cells": int(g["cell_id"].shape[0]), "animal": get("animal_id"),
           "name": get("session_id"), "time": get("time"), "spikes0": get("spike_times"),
           "Eh": get("horizontal_eye_position"), "Ev": get("vertical_eye_position"),
           "B": get("body_position"), "Bs": get("body_speed")}
    out["n_frames"] = len(out["time"])
    return out


def load_session(url: str) -> dict:
    """Behaviour at 50 Hz and spike counts per 20 ms bin for every unit of one head-fixed file."""
    f = _open(url)
    b = f["processing/behavior"]
    t = b["Position/position/timestamps"][:]
    eye = b["EyeTracking/eye_position/data"][:]
    vel_key = "eye_velocity/data" if "eye_velocity" in b else "eye velocity/data"
    eyev = b[vel_key][:]
    beh = {"B": b["Position/position/data"][:].ravel(), "Bs": b["body_speed/data"][:].ravel(),
           "Eh": eye[:, 0], "Ev": eye[:, 1], "Ehd": eyev[:, 0], "Evd": eyev[:, 1]}
    st = f["units/spike_times"][:]
    idx = f["units/spike_times_index"][:].astype(np.int64)
    trains = split_units(st, idx)
    repaired = trains["repaired"]
    # each behaviour sample stands for the 20 ms that follow it; spikes in gaps of the timestamps
    # (where the next sample is more than 20 ms later) fall in no bin
    counts = np.zeros((len(idx), len(t)), dtype=np.uint8)
    n_spikes, n_outside, max_count = [], [], 0
    for i, s in enumerate(trains["units"]):
        j = np.searchsorted(t, s, side="right") - 1
        ok = (j >= 0) & (s - t[np.clip(j, 0, None)] < DT)
        c = np.bincount(j[ok], minlength=len(t))
        max_count = max(max_count, int(c.max()) if len(c) else 0)
        counts[i] = np.minimum(c, 255)
        n_spikes.append(len(s))
        n_outside.append(int((~ok).sum()))
    trials = {}
    if "intervals/trials" in f:
        tr = f["intervals/trials"]
        trials = {k: tr[k][:] for k in ["start_time", "stop_time", "visual_contrast", "running_wheel_gain"] if k in tr}
    return {"t": t, "beh": beh, "counts": counts, "n_spikes": np.array(n_spikes),
            "n_outside": np.array(n_outside), "max_count": max_count, "trials": trials, "repaired": repaired,
            "subject": _text(f["general/subject/subject_id"]), "pos_unit": b["Position/position/data"].attrs.get("unit")}


def split_units(st: np.ndarray, idx: np.ndarray) -> dict:
    """Spike trains of the units from the ragged `spike_times` and its index. Within a unit the spike
    times must increase. Where unit i + 1's times fall back once, its leading run belongs to unit i:
    the index entry of unit i has wrapped at 2**16 (found in two files, where the spikes of unit 0
    after the wrap sit at the start of unit 1; the paper's figshare deposit has them in unit 0). Such
    units are repaired and reported."""
    bounds = np.concatenate([[0], idx])
    units = [st[bounds[i]:bounds[i + 1]] for i in range(len(idx))]
    repaired = []
    for i in range(1, len(units)):
        d = np.flatnonzero(np.diff(units[i]) < 0)
        if len(d) == 1 and len(units[i - 1]) and units[i][d[0]] > units[i - 1][-1]:
            k = d[0] + 1
            repaired.append({"unit": i - 1, "moved": int(k), "index_was": int(idx[i - 1]),
                             "index_now": int(idx[i - 1] + k)})
            units[i - 1] = np.concatenate([units[i - 1], units[i][:k]])
            units[i] = units[i][k:]
    return {"units": units, "repaired": repaired}


# ----------------------------------------------------------------------------------------- design
_S = np.array([[-TENSION, 2 - TENSION, TENSION - 2, TENSION],
               [2 * TENSION, TENSION - 3, 3 - 2 * TENSION, -TENSION],
               [-TENSION, 0, TENSION, 0],
               [0, 1, 0, 0]])


def spline_1d(y: np.ndarray, cpts: np.ndarray) -> np.ndarray:
    """Cardinal spline regressors as spline_1d.m: one padded control point on each side; values must
    lie above the first control point (the code lowers it slightly, as here)."""
    c = np.concatenate([[cpts[0] - (cpts[1] - cpts[0])], cpts, [cpts[-1] + (cpts[-1] - cpts[-2])]])
    j = np.searchsorted(c, y, side="left") - 1          # largest index with c[j] < y
    j = np.clip(j, 1, len(c) - 3)
    u = (y - c[j]) / (c[j + 1] - c[j])
    p = np.stack([u ** 3, u ** 2, u, np.ones_like(u)], axis=1) @ _S
    X = np.zeros((len(y), len(c)))
    rows = np.arange(len(y))
    for k in range(4):
        X[rows, j - 1 + k] = p[:, k]
    return X


def control_points(name: str, lo: float, hi: float) -> np.ndarray:
    if name == "Bs":
        n = max(2, int(round((hi - lo) / SPEED_STEP)) + 1)
    else:
        n = N_CPTS[name]
    c = np.linspace(lo, hi, n)
    c[0] -= 1e-6 * max(1.0, abs(hi - lo))
    return c


def prepare(sess: dict, range_mode: str = RANGE_DROP, mask: np.ndarray | None = None) -> dict:
    """Bins kept for the model, the variables' inner ranges and the spline blocks."""
    beh = sess["beh"]
    valid = np.ones(len(sess["t"]), bool)
    for v in VARS:
        valid &= np.isfinite(beh[v])
    if mask is not None:
        valid &= mask
    lims = {v: tuple(np.percentile(beh[v][valid], PCT)) for v in VARS}
    if range_mode == RANGE_DROP:
        keep = valid.copy()
        for v in VARS:
            keep &= (beh[v] >= lims[v][0]) & (beh[v] <= lims[v][1])
        vals = {v: beh[v][keep] for v in VARS}
    else:
        keep = valid
        vals = {v: np.clip(beh[v][keep], *lims[v]) for v in VARS}
    cpts = {v: control_points(v, *lims[v]) for v in VARS}
    blocks = {v: spline_1d(vals[v], cpts[v]) for v in VARS}
    return {"keep": keep, "lims": lims, "cpts": cpts, "blocks": blocks, "vals": vals,
            "n_valid": int(valid.sum()), "n_keep": int(keep.sum())}


def by_fold(prep: dict, folds: np.ndarray) -> dict:
    """The kept bins reordered by fold (the fits do not depend on the order of the bins), with each
    fold's row range and each row's position in the session (`order`, for the session halves)."""
    order = np.argsort(folds, kind="stable")
    counts = np.bincount(folds, minlength=NFOLDS)
    ends = np.cumsum(counts)
    out = dict(prep)
    out["order"] = order
    out["bounds"] = [(int(e - c), int(e)) for c, e in zip(counts, ends)]
    out.setdefault("seed", 0)
    out["blocks"] = {v: b[order] for v, b in prep["blocks"].items()}
    out["vals"] = {v: x[order] for v, x in prep["vals"].items()}
    return out


def fold_labels(n: int, mode: str = FOLDS_TURN, seed: int = 0) -> np.ndarray:
    """Fold of each kept bin: 10-s sections assigned to folds 1 to 10 in turn
    (compute_test_train_ind.m) or at random, balanced."""
    sec = np.arange(n) // SECTION
    n_sec = sec.max() + 1
    if mode == FOLDS_TURN:
        lab = np.arange(n_sec) % NFOLDS
    else:
        rng = np.random.default_rng(seed)
        lab = rng.permutation(np.resize(np.arange(NFOLDS), n_sec))
    return lab[sec]


# ----------------------------------------------------------------------------------------- fitting
def _llh(rate_test, n_test):
    """compute_llh.m: per-spike log-likelihood increase over the test fold's mean rate, times log 2."""
    s = n_test.sum()
    if s == 0:
        return np.nan
    m = n_test.mean()
    ll_model = np.sum(rate_test - n_test * np.log(rate_test))
    ll_mean = np.sum(m - n_test * np.log(m))
    return (-ll_model + ll_mean) / s * LOG2


DECREMENT_TOL = 1e-6   # half the Newton decrement, the predicted fall of the objective; fminunc's
#                       default FunctionTolerance is 1e-6


def _hess(X32, r):
    """X' diag(r) X in single precision (it sets only the step direction; the gradient, and so the
    optimum, stays in double precision)."""
    return ((X32 * r.astype(np.float32)[:, None]).T @ X32).astype(np.float64)


def newton(X, y, theta0, tol=DECREMENT_TOL, max_iter=50, X32=None):
    theta = theta0.copy()
    p = X.shape[1]
    X32 = X.astype(np.float32) if X32 is None else X32
    for _ in range(max_iter):
        r = np.exp(X @ theta)
        g = X.T @ (r - y) + theta
        H = _hess(X32, r)
        H[np.diag_indices(p)] += 1.0
        step = np.linalg.solve(H, g)
        dec = 0.5 * float(g @ step)
        mx = np.abs(step).max()
        if mx > 5:   # damp very large steps (a guard; fminunc's trust region does the same job)
            step *= 5 / mx
        theta -= step
        if dec < tol:
            break
    return theta


def fit_kfold(X, y, bounds, theta0, tol=DECREMENT_TOL):
    """10-fold fits of one model, the rows ordered by fold so that fold k is X[a:b] for
    (a, b) = bounds[k]. Each fold's fit starts from the full-session solution with the training
    Hessian there, and is iterated until the Newton decrement is below `tol`. Returns test llh per
    fold, the mean fold parameters, and the full-session parameters."""
    X32 = X.astype(np.float32)
    theta_full = newton(X, y, theta0, tol=tol, X32=X32)
    r = np.exp(X @ theta_full)
    p = X.shape[1]
    resid = r - y
    Hdata = _hess(X32, r)
    test_fit = np.full(len(bounds), np.nan)
    params = np.zeros((len(bounds), p))
    for k, (a, b) in enumerate(bounds):
        Xk, yk = X[a:b], y[a:b]
        Hk = _hess(X32[a:b], r[a:b])
        Htr = Hdata - Hk
        Htr[np.diag_indices(p)] += 1.0
        theta = theta_full.copy()
        g = -(Xk.T @ resid[a:b])          # gradient of the training objective at theta_full
        ok = False
        for it in range(6):
            step = np.linalg.solve(Htr, g)
            dec = 0.5 * float(g @ step)
            if dec < tol:
                ok = True
                break
            theta -= step
            rr = np.exp(X @ theta) - y
            g = X.T @ rr - Xk.T @ rr[a:b] + theta
        if not ok:   # slow convergence with the fixed Hessian: full Newton on the training rows
            tr = np.ones(len(y), bool)
            tr[a:b] = False
            theta = newton(X[tr], y[tr], theta, tol=tol, X32=X32[tr])
        params[k] = theta
        test_fit[k] = _llh(np.exp(Xk @ theta), yk)
    return test_fit, params.mean(0), theta_full


def signrank_right(a, b):
    d = np.asarray(a) - np.asarray(b)
    d = d[np.isfinite(d)]
    d = d[d != 0]
    if len(d) == 0:
        return 1.0
    return float(stats.wilcoxon(d, alternative="greater").pvalue)


def design(blocks, variables):
    cols = [np.ones((next(iter(blocks.values())).shape[0], 1))] + [blocks[v] for v in variables]
    return np.hstack(cols)


def _layout(blocks, variables):
    out, i = {}, 1
    for v in variables:
        w = blocks[v].shape[1]
        out[v] = slice(i, i + w)
        i += w
    return out


def forward_search(blocks, y, bounds, variables=None):
    """forward_search_kfold.m. Returns the selected variables (sorted as in `variables`, by default
    VARS), every model's fold fits, the selected model's folds and parameters, and the final P
    against 0."""
    names = variables or VARS
    selected = []
    base = np.full(NFOLDS, -5.0)
    fits = {}
    best_theta = {(): np.array([math.log(max(y.mean(), 1e-6))])}
    sel_fits, sel_param, sel_full = None, None, None
    pvals = []
    while len(selected) < len(names):
        cand = [v for v in names if v not in selected]
        results = {}
        for v in cand:
            vs = [x for x in names if x in selected or x == v]
            X = design(blocks, vs)
            # warm start: previous model's parameters, zeros for the new variable
            prev = best_theta[tuple(selected)]
            lay_prev = _layout(blocks, selected)
            lay = _layout(blocks, vs)
            th0 = np.zeros(X.shape[1])
            th0[0] = prev[0]
            for w in selected:
                th0[lay[w]] = prev[lay_prev[w]]
            tf, pm, pf = fit_kfold(X, y, bounds, th0)
            results[v] = (tf, pm, pf, vs)
            fits[tuple(vs)] = tf
        top = max(cand, key=lambda v: np.nanmean(results[v][0]) if np.isfinite(results[v][0]).any() else -np.inf)
        tf, pm, pf, vs = results[top]
        last_top = tf
        p = signrank_right(tf, base)
        pvals.append(p)
        if p < ALPHA:
            selected = vs
            best_theta[tuple(vs)] = pf
            sel_fits, sel_param, sel_full = tf, pm, pf
            base = tf
        else:
            break
    final_p = signrank_right(sel_fits, np.zeros(NFOLDS)) if sel_fits is not None else 1.0
    encoded = selected if final_p < ALPHA else []
    # forward_search_kfold.m itself tests the last model it tried (`topModel`), which is the rejected
    # larger model when the search stopped on a failed addition; a variant
    final_p_code = signrank_right(last_top, np.zeros(NFOLDS))
    return {"selected": selected, "encoded": encoded, "final_p": final_p, "fits": fits,
            "encoded_code": selected if final_p_code < ALPHA else [],
            "sel_fits": sel_fits, "sel_param": sel_param, "sel_full": sel_full, "pvals": pvals}


# ----------------------------------------------------------------------------------------- measures
def tuning_curve(param, blocks, variables, var, grid, cpts):
    """Methods eq. 10: exp(Y_i(m) w_i) * gamma / dt, gamma = exp(b0) * prod over the other encoded
    variables of their mean contribution over the session's bins."""
    lay = _layout(blocks, variables)
    gamma = math.exp(param[0])
    for v in variables:
        if v != var:
            gamma *= float(np.mean(np.exp(blocks[v] @ param[lay[v]])))
    Y = spline_1d(np.clip(grid, cpts[0] + 1e-9, cpts[-1]), cpts)
    return np.exp(Y @ param[lay[var]]) * gamma / DT


def vis_range(var, lims):
    lo, hi = lims[var]
    if var in PRESET:
        return max(lo, PRESET[var][0]), min(hi, PRESET[var][1])
    return lo, hi


def explored(var, lims, values):
    """Open detail (4). (a) the fraction of the preset range covered by the visualizing range;
    (b) the fraction of 20 bins over the preset range with any occupancy."""
    if var not in PRESET:
        return 1.0, 1.0
    plo, phi = PRESET[var]
    lo, hi = vis_range(var, lims)
    a = max(0.0, hi - lo) / (phi - plo)
    edges = np.linspace(plo, phi, 21)
    occ, _ = np.histogram(values, edges)
    return a, float((occ > 0).mean())


def classify_shape(x, curve, max_order=5):
    """Lowest polynomial order (1 to 5) whose fraction of error explained over a flat line exceeds
    0.9, on the range-normalized curve (Methods, "Quantifying tuning curve shape"). 0 when none does."""
    c = (curve - curve.min()) / (np.ptp(curve) if np.ptp(curve) > 0 else 1.0)
    xs = (x - x.min()) / (np.ptp(x) if np.ptp(x) > 0 else 1.0)
    base = np.mean((c - c.mean()) ** 2)
    if base == 0:
        return 0
    for order in range(1, max_order + 1):
        fit = np.polyval(np.polyfit(xs, c, order), xs)
        if (base - np.mean((c - fit) ** 2)) / base > FEE_MIN:
            return order
    return 0


def side_slopes(x, curve):
    """Slopes of lines fitted to the curve below and above 0 (Methods, "Quantifying head and eye
    velocity tuning curves"); NaN where a side has fewer than 3 points."""
    out = []
    for m in (x < 0, x > 0):
        out.append(np.polyfit(x[m], curve[m], 1)[0] if m.sum() >= 3 else np.nan)
    return tuple(out)


def peaks_valleys(x, curve):
    """findpeaks on the curve and its negative, keeping those that take the curve's maximum or
    minimum (Methods, "Quantifying head and eye velocity tuning curves")."""
    from scipy.signal import find_peaks
    out = []
    pk, _ = find_peaks(curve)
    for i in pk:
        if curve[i] == curve.max():
            out.append(x[i])
    vl, _ = find_peaks(-curve)
    for i in vl:
        if curve[i] == curve.min():
            out.append(x[i])
    return out


def fit_full(X, y, theta0=None):
    return newton(X, y, np.zeros(X.shape[1]) if theta0 is None else theta0)


def ll_perf(theta, X, y):
    return _llh(np.exp(X @ theta), y)


# ----------------------------------------------------------------------------------------- per cell
def analyse_cell(prep, y, with_extras=True):
    """Forward search for one cell, then (for encoding cells) the reduced models for the contribution,
    the model-derived tuning curves and the half-session refits for stability."""
    blocks = prep["blocks"]
    bounds = prep["bounds"]
    fs = forward_search(blocks, y, bounds)
    out = {"selected": fs["selected"], "encoded": fs["encoded"], "final_p": fs["final_p"],
           "encoded_code": fs["encoded_code"],
           "sel_fits": fs["sel_fits"], "n_spikes": int(y.sum())}
    enc = fs["encoded"]
    if not enc or not with_extras:
        return out
    lay = _layout(blocks, enc)
    full_perf = float(np.nanmean(fs["sel_fits"]))
    out["perf"] = full_perf
    # contribution: reduced models (selected minus one variable), 10 folds, mean performance
    contrib = {}
    if len(enc) > 1:
        for v in enc:
            red = [w for w in enc if w != v]
            key = tuple(red)
            if key in fs["fits"]:
                tf = fs["fits"][key]
            else:
                X = design(blocks, red)
                th0 = np.concatenate([[fs["sel_full"][0]]] + [fs["sel_full"][lay[w]] for w in red])
                tf, _, _ = fit_kfold(X, y, bounds, th0)
            contrib[v] = (fs["sel_fits"], tf)
    out["contrib"] = contrib
    # tuning curves over the inner range, M = 200 bins
    curves = {}
    for v in enc:
        lo, hi = prep["lims"][v]
        grid = np.linspace(lo, hi, M_BINS)
        curves[v] = (grid, tuning_curve(fs["sel_param"], blocks, enc, v, grid, prep["cpts"][v]))
    out["curves"] = curves
    # stability: the selected model refitted on each half of the kept bins
    n = len(y)
    half = prep["order"] < n // 2
    Xs = design(blocks, enc)
    stab_curves = []
    for m in (half, ~half):
        th = fit_full(Xs[m], y[m], fs["sel_full"])
        hb = {v: blocks[v][m] for v in enc}
        cs = {}
        for v in enc:
            lo, hi = prep["lims"][v]
            grid = np.linspace(lo, hi, M_BINS)
            vals = prep["vals"][v][m]
            cs[v] = (grid, tuning_curve(th, hb, enc, v, grid, prep["cpts"][v]), vals.min(), vals.max())
        stab_curves.append(cs)
    stab = {}
    for v in enc:
        g, c1, a1, b1 = stab_curves[0][v]
        _, c2, a2, b2 = stab_curves[1][v]
        lo, hi = vis_range(v, prep["lims"])
        m = (g >= max(lo, a1, a2)) & (g <= min(hi, b1, b2))
        stab[v] = float(np.corrcoef(c1[m], c2[m])[0, 1]) if m.sum() > 2 and np.std(c1[m]) > 0 and np.std(c2[m]) > 0 else np.nan
    out["stability"] = stab
    # open detail (6), reading b: correlation of firing with velocity below and above 0 against 500
    # circular shifts of the spike train by more than 20 s (Methods, "Comparison between LN and
    # shuffling-based methods")
    inv = np.argsort(prep["order"])
    for v in ("Ehd", "Evd"):
        if v in enc:
            out.setdefault("shuffle", {})[v] = side_shuffle(prep["vals"][v][inv], y[inv], prep["seed"])
    return out


def side_shuffle(x, y, seed, n_shift=500, min_shift=int(20 / DT)):
    """Pearson correlation of spike count with the variable over bins below 0 and above 0, and the
    5th and 95th percentiles of the same correlations under 500 circular shifts of the spike train
    by more than 20 s. Returns (r_neg, lo_neg, hi_neg, r_pos, lo_pos, hi_pos)."""
    rng = np.random.default_rng(seed)
    n = len(y)
    shifts = rng.integers(min_shift, n - min_shift, n_shift)
    out = []
    F = np.fft.rfft
    nfft = 1 << (2 * n - 1).bit_length()
    Yf = np.conj(F(y, nfft))
    Y2f = np.conj(F(y * y, nfft))
    for m in (x < 0, x > 0):
        xm = np.where(m, x, 0.0)
        mm = m.astype(float)
        k = mm.sum()
        # sums over the masked bins of y shifted by s: circular cross-correlation via FFT
        def cc(a_f, b):
            full = np.fft.irfft(F(b, nfft) * a_f, nfft)
            # circular correlation c[s] = sum_t b[t] y[(t + s) mod n]
            return full[:n] + np.concatenate([[0.0], full[nfft - n + 1:]])[:n] if nfft > n else full[:n]
        sy = cc(Yf, mm)
        sxy = cc(Yf, xm)
        syy = cc(Y2f, mm)
        sx, sxx = xm.sum(), (xm * xm).sum()
        vx = sxx / k - (sx / k) ** 2
        vy = syy / k - (sy / k) ** 2
        cov = sxy / k - (sx / k) * (sy / k)
        with np.errstate(invalid="ignore", divide="ignore"):
            r = cov / np.sqrt(vx * vy)
        out += [float(r[0]), float(np.nanpercentile(r[shifts], 5)), float(np.nanpercentile(r[shifts], 95))]
    return tuple(out)


_WORK = {}


def _init_worker():
    from threadpoolctl import threadpool_limits
    _WORK["limit"] = threadpool_limits(1)


def _worker(i):
    prep, Y, extras = _WORK["args"]
    return i, analyse_cell(prep, Y[i, prep["order"]].astype(float), extras)


def analyse_session(prep, Y, processes=4, with_extras=True):
    """Every unit of one session (rows of Y, over the kept bins in session order), in `processes`
    forked workers sharing the design; `prep` comes from by_fold."""
    import multiprocessing as mp
    from threadpoolctl import threadpool_limits
    _WORK["args"] = (prep, Y, with_extras)
    ctx = mp.get_context("fork")
    with threadpool_limits(1):
        with ctx.Pool(processes, initializer=_init_worker) as pool:
            res = dict(pool.imap_unordered(_worker, range(Y.shape[0]), chunksize=4))
    _WORK.clear()
    return [res[i] for i in range(Y.shape[0])]


# ----------------------------------------------------------------------------------------- tuning shape
def curve_features(result: dict, var: str, lims: dict, values: np.ndarray) -> dict:
    """Shape measures of one encoded variable's model-derived tuning curve, on the visualizing range:
    polynomial class, the two readings of "explored" (open detail 4), preference under the two
    readings of open detail (5), the slopes either side of 0, and for velocities the symmetric rule
    under the two readings of open detail (6)."""
    grid, curve = result["curves"][var]
    lo, hi = vis_range(var, lims)
    m = (grid >= lo) & (grid <= hi)
    x, c = grid[m], curve[m]
    ex_a, ex_b = explored(var, lims, values)
    order = classify_shape(x, c) if len(x) > 6 else 0
    out = {"order": order, "explored_a": ex_a, "explored_b": ex_b, "x": x, "curve": c,
           "stability": result.get("stability", {}).get(var, np.nan)}
    slope = np.polyfit(x, c, 1)[0] if len(x) > 2 else np.nan
    sl_neg, sl_pos = side_slopes(x, c) if len(x) > 6 else (np.nan, np.nan)
    out.update({"slope": slope, "slope_neg": sl_neg, "slope_pos": sl_pos, "x_max": float(x[np.argmax(c)]) if len(x) else np.nan})
    # preference, reading (a): sign of the slope for linear curves, side of the maximum otherwise
    out["pref_a"] = (1 if slope > 0 else -1) if order == 1 else (1 if out["x_max"] > 0 else -1)
    # reading (b): the side with the steeper rise away from 0 of the lines fitted either side of 0
    # (the rise towards + is the slope above 0, towards - minus the slope below 0)
    if np.isfinite(sl_neg) and np.isfinite(sl_pos):
        out["pref_b"] = 1 if sl_pos >= -sl_neg else -1
    else:
        out["pref_b"] = out["pref_a"]
    if var in ("Ehd", "Evd"):
        # (a): symmetric when the slopes either side of 0 have opposite signs (V or inverted V)
        sym_a = bool(np.isfinite(sl_neg) and np.isfinite(sl_pos) and np.sign(sl_neg) != np.sign(sl_pos))
        out["sym_a"] = sym_a
        out["sym_pos_a"] = bool(sym_a and sl_pos > 0)        # V: firing rises with speed
        sh = result.get("shuffle", {}).get(var)
        if sh is not None:
            r_neg, lo_neg, hi_neg, r_pos, lo_pos, hi_pos = sh
            v_shape = r_neg < lo_neg and r_pos > hi_pos
            inv_v = r_neg > hi_neg and r_pos < lo_pos
            out["sym_b"] = bool(v_shape or inv_v)
            out["sym_pos_b"] = bool(v_shape)
        else:
            out["sym_b"], out["sym_pos_b"] = False, False
    return out


def paper_sessions(urls: dict, summaries: dict | None = None) -> tuple[list[str], list[dict]]:
    """The dandiset files that are the paper's 11 head-fixed recordings: for each file of figshare
    Dataset 3, the one ecephys file with the same subject, unit count and frame count."""
    with ThreadPoolExecutor(6) as ex:
        fsd = list(ex.map(figshare_session, sorted(FIGSHARE_FILES)))
    if summaries is None:
        ece = {p: u for p, u in urls.items() if "ecephys" in p}
        with ThreadPoolExecutor(10) as ex:
            summaries = dict(zip(ece, ex.map(file_summary, ece.values())))
    out = []
    for s in fsd:
        cand = [p for p, m in summaries.items() if m.get("has_ecephys") and m["subject_id"] == s["animal"]
                and m["n_units"] == s["n_cells"] and m.get("n_frames") == s["n_frames"]]
        out.append(cand[0] if len(cand) == 1 else None)
    return out, fsd


# ----------------------------------------------------------------------------------------- shuffles, raw curves
def shuffle_corr(x, y, rng, n_shift=500, min_shift=int(20 / DT)):
    """Pearson correlation of a variable with the spike count, and the same correlation for 500
    circular shifts of the spike train by more than 20 s (Methods, "Comparison between LN and
    shuffling-based methods"). Returns (r, shuffled r)."""
    n = len(y)
    xc, yc = x - x.mean(), y - y.mean()
    den = math.sqrt(float(xc @ xc) * float(yc @ yc))
    if den == 0:
        return np.nan, np.full(n_shift, np.nan)
    c = np.fft.irfft(np.conj(np.fft.rfft(xc)) * np.fft.rfft(yc), n)   # c[s] = sum_t x[t] y[t + s]
    shifts = rng.integers(min_shift, n - min_shift, n_shift)
    return float(c[0] / den), c[shifts] / den


def rlowess(y, span=7, iters=5):
    """MATLAB smooth(y, span, 'rlowess'): local linear fits with tricube weights over `span` points,
    then `iters` robust reweightings with bisquare weights at 6 median absolute deviations (a standard
    implementation of the Methods' "rlowess function (smoothing over 7 bins)")."""
    y = np.asarray(y, float)
    n = len(y)
    x = np.arange(n, dtype=float)
    half = span // 2
    rob = np.ones(n)
    out = y.copy()
    for it in range(iters + 1):
        for i in range(n):
            a = min(max(0, i - half), max(0, n - span))
            b = min(n, a + span)
            xs, ys, rs = x[a:b], y[a:b], rob[a:b]
            d = np.abs(xs - x[i])
            dmax = max(d.max(), 1e-12) * 1.0001
            w = (1 - (d / dmax) ** 3) ** 3 * rs
            if w.sum() <= 0 or len(xs) < 2:
                out[i] = y[i]
                continue
            W = np.sqrt(w)
            A = np.stack([np.ones_like(xs), xs - x[i]], 1) * W[:, None]
            coef, *_ = np.linalg.lstsq(A, ys * W, rcond=None)
            out[i] = coef[0]
        if it == iters:
            break
        r = y - out
        mad = np.median(np.abs(r))
        if mad == 0:
            break
        u = r / (6 * mad)
        rob = np.where(np.abs(u) < 1, (1 - u ** 2) ** 2, 0.0)
    return out


def raw_tuning(values, counts, lo, hi, nbins=20, dt=DT):
    """Raw tuning curve (Methods, "Raw tuning curves"): spikes over occupancy in 20 bins of the
    visualizing range, smoothed with rlowess over 7 bins. Bins never visited are left out before
    smoothing. Returns bin centres and the smoothed rate (spikes/s)."""
    edges = np.linspace(lo, hi, nbins + 1)
    m = (values >= lo) & (values <= hi)
    occ, _ = np.histogram(values[m], edges)
    spk, _ = np.histogram(values[m], edges, weights=counts[m])
    centres = (edges[:-1] + edges[1:]) / 2
    ok = occ > 0
    rate = spk[ok] / (occ[ok] * dt)
    return centres[ok], rlowess(rate) if ok.sum() >= 3 else rate


def model_raw_corr(grid, curve, centres, raw):
    """Pearson correlation of the raw tuning curve with the model-derived curve resampled at the raw
    curve's bin centres (linear interpolation, the claims file's standard choice)."""
    if len(centres) < 3 or np.std(raw) == 0:
        return np.nan
    mod = np.interp(centres, grid, curve)
    if np.std(mod) == 0:
        return np.nan
    return float(np.corrcoef(mod, raw)[0, 1])
