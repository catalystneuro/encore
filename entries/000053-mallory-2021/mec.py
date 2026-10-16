"""Loading and the LN model for dandiset 000053 (Mallory, Hardcastle et al. 2021).

Mallory CS, Hardcastle K, Campbell MG, Attinger A, Low IIC, Raymond JL, Giocomo LM (2021). Mouse
entorhinal cortex encodes a diverse repertoire of self-motion signals. Nature Communications 12,
671. doi:10.1038/s41467-021-20936-8.

The dandiset holds two kinds of file. Freely moving tetrode sessions (`*_behavior.nwb` of the
named mice) hold body position, body speed, azimuthal head direction and azimuthal head velocity
at 50 Hz, and the sorted units. Head-fixed virtual reality sessions of the `np*` mice hold track
position, running speed, eye position and eye velocity (horizontal and vertical) at 50 Hz, and the
sorted Neuropixels units; the `*_behavior+ecephys.nwb` files add the raw voltage, LFP, licks,
rewards and a trial table. Files are streamed from the archive at the pinned version; nothing is
written to disk.

Where the parameters come from:

- The model is the linear-nonlinear Poisson model of the Methods ("LN model framework"), as coded
  in https://github.com/khardcastle/spline-lnp-model at commit
  34b470fd452b3f6b9e4066d74efbc1fa7182f4b5 (the code the paper names): cardinal spline bases with
  tension `SPLINE_S` = 0.5 (Methods: 0.5 to 0.7; the code uses 0.5), an L2 penalty `ALPHA` = 1 on
  every parameter including the intercept (Methods: beta = 1; code: `glm_model.m`), Newton fits
  to the minimum of the penalised Poisson negative log-likelihood (the code uses MATLAB's
  fminunc trust-region with the exact Hessian; the optimum is the same, as the objective is
  strictly convex), and the forward search of `forward_search_kfold.m` with a one-sided Wilcoxon
  signed-rank test at 0.05 at every step.
- Ten folds, each made of every tenth 10 s section of the session (Methods: "chosen from 10-s
  sections"; the code uses 3 s sections; the Methods are followed).
- Bins (Methods): open field, round(arena side x 15 / 100) position control points per side,
  10 head direction, 8 azimuthal head velocity, speed every 5 cm/s; virtual reality, 20 position,
  speed every 5 cm/s, 5 for each eye variable. Control points span the kept range of the variable,
  with the lowest moved just below the minimum, as the code does.
- Kept time bins (Methods, "Data pre-processing"): those in which every variable lies between its
  2.5th and 97.5th percentiles (open field) or 1st and 99th percentiles (virtual reality).
- Model performance is the log-likelihood increase over a mean rate model on held-out data, per
  spike, in bits (`compute_llh.m` uses the mean rate of the test fold). The spline code multiplies
  the value in nats by log(2) where conversion to bits divides by it; `LLH_SCALES` gives both.
- Tuning curves, their ranges, their shape classes and stability follow the Methods sections
  "Model-derived tuning curves", "Visualizing tuning curves", "Quantifying tuning curve shape" and
  "Calculating tuning curve stability". `CURVE_POINTS` = 200 (Methods: default M = 200).
"""

from __future__ import annotations

import os
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy import linalg, sparse, stats
from scipy.linalg import blas

DANDISET_ID = "000053"
DANDISET_VERSION = "0.210819.0345"

DT = 0.02                 # s, 50 Hz behaviour samples; Methods: 20 ms bins
SPLINE_S = 0.5
ALPHA = 1.0
N_FOLDS = 10
SECTION_S = 10.0
P_STEP = 0.05
CURVE_POINTS = 200
LLH_SCALES = {"bits": 1 / np.log(2), "spline code (nats x log 2)": np.log(2), "nats": 1.0}

# Head-fixed variables, in the paper's order and names.
VR_VARS = ["B", "Bs", "Eh", "Ev", "Ehdot", "Evdot"]
VR_KEEP = (1.0, 99.0)
VR_BINS = {"B": 20, "Eh": 5, "Ev": 5, "Ehdot": 5, "Evdot": 5}
SPEED_STEP = 5.0          # cm/s
# Methods, "Visualizing tuning curves": preset bounds of the plotted and classified range.
VR_PRESET = {"Eh": (-3.0, 3.0), "Ev": (-2.0, 2.0), "Ehdot": (-3.0, 3.0), "Evdot": (-2.0, 2.0)}
EYE_COVERAGE = 0.8        # Methods: classify the shape only if 80% of the preset range was explored

# Freely moving variables: Cohort 2 has the first four, Cohort 1 all eight.
OF_VARS = ["B", "Bs", "Ha", "Hadot"]
OF_VARS_IMU = ["B", "Bs", "Ha", "Hp", "Hr", "Hadot", "Hpdot", "Hrdot"]
OF_IMU_BINS = 8           # Methods: 8 bins for pitch, roll (and azimuthal head velocity); used for their velocities too
OF_KEEP = (2.5, 97.5)
OF_POS_PER_CM = 15 / 100
OF_HD_BINS = 10
OF_AHV_BINS = 8
OF_PRESET = {"Hadot": (-100.0, 100.0), "Hp": (-50.0, 50.0), "Hr": (-50.0, 50.0)}   # deg/s, deg
SMOOTH_PR = 20            # Methods: pitch and roll curves smoothed (MATLAB smoothdata, Gaussian, width 20)
HEAD_COVERAGE = 0.5


# ---------------------------------------------------------------- archive

def asset_table() -> list[dict]:
    """Path, size, asset id and streaming URL of every file at the pinned version."""
    with DandiAPIClient() as client:
        dandiset = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        return sorted(({"path": a.path, "size": a.size, "asset_id": a.identifier,
                        "url": a.get_content_url(follow_redirects=1, strip_query=True)}
                       for a in dandiset.get_assets()), key=lambda a: a["path"])


def open_file(url: str) -> h5py.File:
    return h5py.File(remfile.File(url), "r")


def _text(value) -> str:
    value = value[()]
    return value.decode() if isinstance(value, bytes) else str(value)


def _spikes(f) -> list[np.ndarray]:
    times = f["units/spike_times"][:]
    index = f["units/spike_times_index"][:]
    return np.split(times, index[:-1])


def describe_file(url: str) -> dict:
    """Metadata, series and unit counts of one file, without reading large arrays."""
    with open_file(url) as f:
        b = f["processing/behavior"]
        out = {"identifier": _text(f["identifier"]), "session_description": _text(f["session_description"]),
               "experiment_description": _text(f["general/experiment_description"]),
               "session_start": _text(f["session_start_time"])[:10],
               "subject_id": _text(f["general/subject/subject_id"]),
               "species": _text(f["general/subject/species"]) if "species" in f["general/subject"] else None,
               "behavior": sorted(b.keys()), "acquisition": sorted(f["acquisition"].keys()),
               "units": len(f["units/id"]), "unit_columns": sorted(f["units"].keys()),
               "n_samples": b["Position/position/timestamps"].shape[0],
               "has_trials": "intervals/trials" in f}
        out["units_of"] = {k: (b[k]["data"].attrs.get("unit") if "data" in b[k] else None)
                           for k in b if k not in ("Position", "EyeTracking")}
        out["units_of"]["position"] = b["Position/position/data"].attrs.get("unit")
        if "EyeTracking" in b:
            out["units_of"]["eye_position"] = b["EyeTracking/eye_position/data"].attrs.get("unit")
        if out["has_trials"]:
            tr = f["intervals/trials"]
            out["trial_columns"] = sorted(tr.keys())
            out["n_trials"] = len(tr["id"])
            out["contrast"] = np.unique(tr["visual_contrast"][:]).tolist()
            out["gain"] = np.unique(tr["running_wheel_gain"][:]).tolist()
            out["electrode_location"] = sorted({x.decode() if isinstance(x, bytes) else x for x in
                                                f["general/extracellular_ephys/electrodes/location"][:]})
            out["ap_seconds"] = f["acquisition/ElectricalSeries/data"].shape[0] / 30000.0
            out["ap_meta"] = str(f["general/devices/Device"].attrs["description"])
        st = f["units/spike_times"]
        out["n_spikes"] = st.shape[0]
    return out


def bin_spikes(spikes: list[np.ndarray], t: np.ndarray) -> np.ndarray:
    """Spike counts of each unit in the bins [t_i, t_i + DT); shape (bins, units). Spikes in gaps
    between samples (where the timestamps jump) and outside the samples are dropped."""
    out = np.zeros((len(t), len(spikes)))
    for j, s in enumerate(spikes):
        i = np.searchsorted(t, s, side="right") - 1
        ok = (i >= 0) & (s - t[np.maximum(i, 0)] < DT)
        out[:, j] = np.bincount(i[ok], minlength=len(t))
    return out


def timestamp_gaps(t: np.ndarray) -> tuple[int, float]:
    """Number of intervals longer than 1.5 DT and their total length (s)."""
    d = np.diff(t)
    g = d > 1.5 * DT
    return int(g.sum()), float(d[g].sum())


def load_vr(url: str) -> dict:
    """One head-fixed session: behaviour at 50 Hz and spike counts per bin.

    Eye position columns are (horizontal, vertical), in percent of the eye width, and eye velocity
    columns in percent of the eye width per second (the file says meters and unknown); the data
    check shows the ranges match those of Figure 4f-i.
    """
    with open_file(url) as f:
        b = f["processing/behavior"]
        t = b["Position/position/timestamps"][:]
        vel = b["eye velocity"] if "eye velocity" in b else b["eye_velocity"]
        eye = b["EyeTracking/eye_position/data"][:]
        ev = vel["data"][:]
        s = {"identifier": _text(f["identifier"]), "subject": _text(f["general/subject/subject_id"]),
             "t": t, "B": b["Position/position/data"][:].ravel(), "Bs": b["body_speed/data"][:].ravel(),
             "Eh": eye[:, 0], "Ev": eye[:, 1], "Ehdot": ev[:, 0], "Evdot": ev[:, 1],
             "units_of": {"position": b["Position/position/data"].attrs.get("unit"),
                          "position_conversion": float(b["Position/position/data"].attrs.get("conversion")),
                          "body_speed": b["body_speed/data"].attrs.get("unit"),
                          "eye_position": b["EyeTracking/eye_position/data"].attrs.get("unit"),
                          "eye_velocity": vel["data"].attrs.get("unit")},
             "same_timestamps": all(np.array_equal(x, t) for x in (
                 b["EyeTracking/eye_position/timestamps"][:], vel["timestamps"][:], b["body_speed/timestamps"][:])),
             "spikes": _spikes(f)}
    s["counts"] = bin_spikes(s["spikes"], t)
    return s


def load_trials(url: str) -> dict:
    """Trial table, licks and rewards of a head-fixed behavior+ecephys file."""
    with open_file(url) as f:
        tr = f["intervals/trials"]
        return {k: tr[k][:] for k in ("start_time", "stop_time", "visual_contrast", "running_wheel_gain", "reward")} | {
            "licks": f["processing/behavior/licks/timestamps"][:],
            "rewards": f["processing/behavior/rewards/timestamps"][:]}


def raw_samples(url: str, start: int, n: int) -> np.ndarray:
    """n samples of the raw AP band of all channels, from sample `start`."""
    with open_file(url) as f:
        return f["acquisition/ElectricalSeries/data"][start:start + n]


def spike_summary(url: str) -> dict:
    """Unit count, spike count, first and last spike, and the first 1000 spike times."""
    with open_file(url) as f:
        st = f["units/spike_times"]
        n = st.shape[0]
        return {"units": len(f["units/id"]), "spikes": n, "head": st[:1000], "tail": st[max(0, n - 1000):],
                "index": f["units/spike_times_index"][:]}


def load_open_field(url: str) -> dict:
    """One freely moving session: position (cm), speed (cm/s), head direction (rad), azimuthal
    head velocity (deg/s; the file says rad/s), spike counts per bin, and for Cohort 1 pitch and
    roll (deg) and their velocities (deg/s)."""
    with open_file(url) as f:
        b = f["processing/behavior"]
        t = b["Position/position/timestamps"][:]
        pos = b["Position/position/data"][:]
        s = {"identifier": _text(f["identifier"]), "subject": _text(f["general/subject/subject_id"]),
             "arena": _text(f["general/experiment_description"]), "session_start": _text(f["session_start_time"])[:10],
             "species": _text(f["general/subject/species"]), "description": _text(f["session_description"]),
             "behavior": sorted(b.keys()),
             "units_of": {"position": b["Position/position/data"].attrs.get("unit"),
                          "position_conversion": float(b["Position/position/data"].attrs.get("conversion")),
                          **{k: b[k]["data"].attrs.get("unit") for k in ("body_speed", "head_direction", "azimuthal_head_velocity")}},
             "t": t, "x": pos[:, 0], "y": pos[:, 1], "Bs": b["body_speed/data"][:].ravel(),
             # labelled rad/s; the values are deg/s (the notebook compares them with head direction)
             "Hadot": b["azimuthal_head_velocity/data"][:].ravel(),
             "hd_description": str(b["head_direction"].attrs.get("description")),
             "shapes": {k: b[k]["data"].shape for k in ("body_speed", "head_direction", "azimuthal_head_velocity")},
             "cell_id": [x.decode() if isinstance(x, bytes) else x for x in f["units/cell_id"][:]],
             "spikes": _spikes(f)}
        hd = b["head_direction/data"][:]
    if hd.ndim == 1:
        s["Ha"] = hd
    else:
        # Cohort 1: columns azimuth, pitch, roll (the series' description), in radians
        s["Ha"] = hd[:, 0]
        s["Hp"], s["Hr"] = np.degrees(hd[:, 1]), np.degrees(hd[:, 2])
        s["Hpdot"], s["Hrdot"] = angular_velocity(s["Hp"]), angular_velocity(s["Hr"])
    s["counts"] = bin_spikes(s["spikes"], t)
    return s


def angular_velocity(angle_deg: np.ndarray) -> np.ndarray:
    """deg/s from an angle in degrees sampled every DT: the change to the next sample, wrapped to
    (-180, 180] (the files store no pitch or roll velocity)."""
    d = np.full_like(angle_deg, np.nan)
    d[:-1] = np.angle(np.exp(1j * np.radians(np.diff(angle_deg))), deg=True) / DT
    return d


def load_many(loader, urls: list[str], workers: int = 8) -> list[dict]:
    with ThreadPoolExecutor(workers) as pool:
        return list(pool.map(loader, urls))


# ---------------------------------------------------------------- spline bases

def _s_matrix(s: float) -> np.ndarray:
    return np.array([[-s, 2 - s, s - 2, s], [2 * s, s - 3, 3 - 2 * s, -s], [-s, 0, s, 0], [0, 1, 0, 0]])


def spline_1d(y: np.ndarray, cpts: np.ndarray, s: float = SPLINE_S):
    """Cardinal spline basis of `spline_1d.m`: (columns, values) of the four non-zero entries per
    sample, and the number of columns (control points plus one at each end)."""
    call = np.r_[cpts[0] - (cpts[1] - cpts[0]), cpts, cpts[-1] + (cpts[-1] - cpts[-2])]
    j = np.searchsorted(call, y, side="left") - 1
    j = np.clip(j, 1, len(call) - 3)
    u = (y - call[j]) / (call[j + 1] - call[j])
    vals = np.stack([u ** 3, u ** 2, u, np.ones_like(u)], 1) @ _s_matrix(s)
    cols = (j - 1)[:, None] + np.arange(4)
    return cols, vals, len(call)


def spline_1d_circ(y: np.ndarray, n: int, s: float = SPLINE_S):
    """Circular basis of `spline_1d_circ.m` on [0, 2 pi) with n control points."""
    width = 2 * np.pi / n
    y = np.mod(y, 2 * np.pi)
    j = np.minimum((y // width).astype(int), n - 1)
    u = (y - j * width) / width
    vals = np.stack([u ** 3, u ** 2, u, np.ones_like(u)], 1) @ _s_matrix(s)
    cols = np.mod((j - 1)[:, None] + np.arange(4), n)
    return cols, vals, n


def spline_2d(x: np.ndarray, y: np.ndarray, cx: np.ndarray, cy: np.ndarray, s: float = SPLINE_S):
    """Tensor product of two 1-D bases, as `spline_2d.m` (column order differs, which does not
    change the fit)."""
    colx, valx, nx = spline_1d(x, cx, s)
    coly, valy, ny = spline_1d(y, cy, s)
    cols = (coly[:, :, None] * nx + colx[:, None, :]).reshape(len(x), 16)
    vals = (valy[:, :, None] * valx[:, None, :]).reshape(len(x), 16)
    return cols, vals, nx * ny


def dense(block) -> np.ndarray:
    cols, vals, n = block
    out = np.zeros((cols.shape[0], n))
    np.add.at(out, (np.repeat(np.arange(cols.shape[0]), cols.shape[1]), cols.ravel()), vals.ravel())
    return out


def control_points(lo: float, hi: float, n: int) -> np.ndarray:
    c = np.linspace(lo, hi, n)
    c[0] = lo - 1e-6 * max(1.0, abs(hi - lo))
    return c


def speed_points(lo: float, hi: float) -> np.ndarray:
    """Every 5 cm/s from the lowest kept speed, the last at the highest (as `create_glm.m`)."""
    c = np.arange(lo, hi + SPEED_STEP, SPEED_STEP)
    c = c[c < hi + 1e-9]
    c = np.r_[c[:-1], hi] if c[-1] < hi else c
    if len(c) < 3:
        c = np.linspace(lo, hi, 3)
    c[0] = lo - 1e-6
    return c


# ---------------------------------------------------------------- sessions to designs

def keep_mask(values: dict, names: list[str], pct: tuple[float, float]) -> np.ndarray:
    keep = np.ones(len(values[names[0]]), bool)
    for k in names:
        v = values[k]
        keep &= np.isfinite(v)
    for k in names:
        v = values[k]
        lo, hi = np.percentile(v[keep], pct)
        keep &= (v >= lo) & (v <= hi)
    return keep


def vr_keep(session: dict) -> np.ndarray:
    return keep_mask(session, VR_VARS, VR_KEEP)


def of_keep(session: dict) -> np.ndarray:
    lin = [k for k in of_vars(session) if k not in ("B", "Ha")]
    v0 = {"x": session["x"], "y": session["y"], **{k: session[k] for k in lin}}
    return keep_mask(v0, ["x", "y"] + lin, OF_KEEP) & np.isfinite(session["Ha"])


def vr_design(session: dict, values: dict | None = None) -> dict:
    """Spline blocks of the six head-fixed variables over the kept bins.

    `values` replaces variables (for shuffles); the kept bins are those of the original values.
    """
    keep = vr_keep(session)
    vals = {k: session[k][keep] for k in VR_VARS}
    if values:
        for k, v in values.items():
            vals[k] = v
    blocks, cpts = {}, {}
    for k in VR_VARS:
        v = vals[k]
        lo, hi = np.min(session[k][keep]), np.max(session[k][keep])
        cp = speed_points(lo, hi) if k == "Bs" else control_points(lo, hi, VR_BINS[k])
        blocks[k] = dense(spline_1d(np.clip(v, cp[0] + 1e-9, cp[-1]), cp))
        cpts[k] = cp
    return {"keep": keep, "blocks": blocks, "cpts": cpts, "values": vals,
            "fold": fold_ids(int(keep.sum()))}


def arena_side(session: dict) -> float:
    return float(session["arena"].split("[")[1].split("]")[0])


def of_vars(session: dict) -> list[str]:
    return OF_VARS_IMU if "Hp" in session else OF_VARS


def of_design(session: dict, values: dict | None = None) -> dict:
    """Spline blocks of position (2-D), speed, head direction, azimuthal head velocity and, in
    Cohort 1, pitch, roll and their velocities.

    The number of position control points per side is round(extent x 15 / 100), the extent
    taken from the kept positions, as the files give one arena size even for rectangles."""
    names = of_vars(session)
    lin = [k for k in names if k not in ("B", "Ha")]
    v0 = {"x": session["x"], "y": session["y"], "Ha": session["Ha"], **{k: session[k] for k in lin}}
    keep = of_keep(session)
    vals = {k: v[keep] for k, v in v0.items()}
    if values:
        for k, v in values.items():
            vals[k] = v
    ex = np.ptp(v0["x"][keep])
    ey = np.ptp(v0["y"][keep])
    x0, y0 = vals["x"] - np.min(v0["x"][keep]), vals["y"] - np.min(v0["y"][keep])
    cx = control_points(0, ex, max(3, int(round(ex * OF_POS_PER_CM))))
    cy = control_points(0, ey, max(3, int(round(ey * OF_POS_PER_CM))))
    b2 = spline_2d(np.clip(x0, cx[0] + 1e-9, cx[-1]), np.clip(y0, cy[0] + 1e-9, cy[-1]), cx, cy)
    blocks = {"B": dense(b2)}
    blocks["Ha"] = dense(spline_1d_circ(vals["Ha"], OF_HD_BINS))
    cpts = {"x": cx, "y": cy}
    for k in lin:
        lo, hi = np.min(v0[k][keep]), np.max(v0[k][keep])
        cp = speed_points(lo, hi) if k == "Bs" else control_points(lo, hi, OF_AHV_BINS if k == "Hadot" else OF_IMU_BINS)
        blocks[k] = dense(spline_1d(np.clip(vals[k], cp[0] + 1e-9, cp[-1]), cp))
        cpts[k] = cp
    return {"keep": keep, "blocks": blocks, "cpts": cpts, "values": vals, "names": names,
            "fold": fold_ids(int(keep.sum())), "B_sparse": b2[:2]}


def fold_ids(n: int) -> np.ndarray:
    """Fold of each kept bin: consecutive 10 s sections assigned to folds 0..9 in turn."""
    per = int(round(SECTION_S / DT))
    return (np.arange(n) // per) % N_FOLDS


# ---------------------------------------------------------------- fitting

TOL = 3e-4                # largest parameter change at convergence
HUB_TOL = 1e-3            # for the fit to all bins, which only starts the fold fits


def _rate(eta):
    return np.exp(np.minimum(eta, 30.0))


def _hessian(Xh, r):
    """X' diag(r) X + ALPHA I, upper triangle (as Cholesky factorisation reads it) by a symmetric
    rank-k update; designs with a 2-D position block (many columns, few non-zero) as sparse
    products."""
    if sparse.issparse(Xh):
        H = (Xh.T.multiply(r[None, :]) @ Xh).toarray()
    else:
        H = blas.dsyrk(1.0, Xh * np.sqrt(r)[:, None], trans=1)
    H[np.diag_indices_from(H)] += ALPHA
    return H


def _objective(X, y, w):
    eta = X @ w
    return float(np.sum(_rate(eta) - y * eta) + 0.5 * ALPHA * w @ w)


def _newton(X, y, w, mask=None, max_iter=100, tol=TOL, hess=None):
    """Minimise sum(exp(Xw) - y Xw) + ALPHA/2 |w|^2 over the rows in mask by Newton steps with
    backtracking; returns w and the Hessian at w. `hess` (a function of the rates of all bins)
    replaces the dense or sparse product."""
    Xm, ym = (X, y) if mask is None else (X[mask], y[mask])
    Xmh = sparse.csr_matrix(Xm) if Xm.shape[1] > 120 and hess is None else Xm

    def H_at(r):
        if hess is None:
            return _hessian(Xmh, r)
        full = np.zeros(len(X))
        if mask is None:
            full[:] = r
        else:
            full[mask] = r
        return hess(full)

    f = _objective(Xm, ym, w)
    for _ in range(max_iter):
        r = _rate(Xm @ w)
        step = linalg.cho_solve(linalg.cho_factor(H_at(r)), Xm.T @ (r - ym) + ALPHA * w)
        t = 1.0
        while True:
            w_new = w - t * step
            f_new = _objective(Xm, ym, w_new)
            if f_new <= f or t < 1e-6:
                break
            t /= 2
        w, f = w_new, f_new
        if np.max(np.abs(t * step)) < tol:
            break
    return w, H_at(_rate(Xm @ w))


def _hub(X, Xs, XsT, Xh, Y, W, H, hess=None):
    """Fits to all bins, to a coarse tolerance, for all cells at once, by steps with the Hessians
    H given for the start (a chord Newton method), each recomputed where its steps stop shrinking;
    rates and gradients in single precision. Returns the fits and the Hessians there."""
    W0 = W
    W = W.copy()
    n = Y.shape[1]
    H = list(H)
    Xs32, XsT32, Y32 = Xs.astype(np.float32), XsT.astype(np.float32), Y.astype(np.float32)
    chos = [linalg.cho_factor(h) for h in H]
    active = np.arange(n)
    last = np.full(n, np.inf)
    refresh, refreshes = np.zeros(n, bool), np.zeros(n, int)
    slow = []
    for i in range(60):
        R = np.exp(np.minimum(Xs32 @ W[:, active].astype(np.float32), 30.0))
        for j, c in enumerate(active):
            if refresh[c]:
                H[c] = hess(R[:, j].astype(np.float64)) if hess else _hessian(Xh, R[:, j].astype(np.float64))
                chos[c] = linalg.cho_factor(H[c])
                last[c], refresh[c] = np.inf, False
        G = (XsT32 @ (R - Y32[:, active])).astype(np.float64) + ALPHA * W[:, active]
        done = []
        for j, c in enumerate(active):
            step = linalg.cho_solve(chos[c], G[:, j], check_finite=False)
            size = np.max(np.abs(step))
            if not np.isfinite(size) or size > 0.9 * last[c]:
                if last[c] < 3 * HUB_TOL:
                    done.append(j)
                elif refreshes[c] < 4:
                    refresh[c] = True       # the Hessian is stale: recompute it here
                    refreshes[c] += 1
                else:
                    slow.append(c)
                    done.append(j)
                if np.isfinite(size) and size <= 1.5 * last[c]:
                    W[:, c] -= step
                continue
            W[:, c] -= step
            last[c] = size
            if size < HUB_TOL:
                done.append(j)
        active = np.delete(active, done)
        if len(active) == 0:
            break
    for c in list(active) + slow:
        W[:, c], _ = _newton(X, Y[:, c], W0[:, c], tol=HUB_TOL, hess=hess)
    R = _rate(Xs @ W)
    return W, [hess(R[:, c]) if hess else _hessian(Xh, R[:, c]) for c in range(n)]


def _test_llh(r, n):
    """Log-likelihood increase over the test fold's mean rate, nats per spike (`compute_llh.m`)."""
    total = n.sum(0)
    m = n.mean(0)
    with np.errstate(divide="ignore", invalid="ignore"):
        model = np.sum(n * np.log(r) - r, 0)
        mean = np.sum(np.where(n > 0, n * np.log(np.where(m > 0, m, 1)), 0), 0) - len(n) * m
        out = (model - mean) / total
    return np.where(total > 0, out, np.nan)


def fit_cv(X, Y, fold, W0, H0=None, hess=None, Xs=None):
    """Ten-fold fits of one model for several cells (columns of Y).

    Returns the test log-likelihood increase (nats/spike, folds x cells), the mean of the fold
    parameters and a fit to all bins. The fit to all bins (to a coarse tolerance) starts from W0
    with the Hessians H0 there (computed if not given); each fold's fit starts from it and steps
    with nine tenths of the Hessian there (the fold's share of the bins), recomputed at the
    current point where steps grow, to convergence: a chord Newton method, which reaches the same
    optimum a Newton fit reaches; a fold that does not converge is finished by Newton. Rates and
    gradients of the steps are in single precision, which moves the optimum by less than the
    tolerance (checked against double precision in the notebook).
    """
    T, p = X.shape
    n = Y.shape[1]
    Xs = sparse.csr_matrix(X) if Xs is None else Xs
    Xh = Xs if p > 120 else X
    XsT = Xs.T.tocsr()
    if H0 is None:
        R0 = _rate(Xs @ W0)
        H0 = [hess(R0[:, c]) if hess else _hessian(Xh, R0[:, c]) for c in range(n)]
    W, H = _hub(X, Xs, XsT, Xh, Y, W0, H0, hess)
    Xs32, XsT32 = Xs.astype(np.float32), XsT.astype(np.float32)
    chos = [linalg.cho_factor((1 - 1 / N_FOLDS) * h + ALPHA / N_FOLDS * np.eye(p)) for h in H]
    # every fold of every cell at once: column j is cell j // N_FOLDS, fold j % N_FOLDS
    K = N_FOLDS
    cell_of = np.repeat(np.arange(n), K)
    fold_of = np.tile(np.arange(K), n)
    M = (fold[:, None] != np.arange(K)[None, :]).astype(np.float32)
    Mall = M[:, fold_of]
    Ytr = Y.astype(np.float32)[:, cell_of] * Mall
    Wf = np.repeat(W, K, axis=1)
    active = np.arange(n * K)
    last = np.full(n * K, np.inf)
    own = {}                                # columns whose anchor was recomputed
    refreshes = np.zeros(n * K, int)
    failed = []
    for _ in range(100):
        Ra = np.exp(np.minimum(Xs32 @ Wf[:, active].astype(np.float32), 30.0)) * Mall[:, active] - Ytr[:, active]
        G = (XsT32 @ Ra).astype(np.float64) + ALPHA * Wf[:, active]
        del Ra
        done = []
        for jj, j in enumerate(active):
            step = linalg.cho_solve(own.get(j, chos[cell_of[j]]), G[:, jj], check_finite=False)
            size = np.max(np.abs(step))
            if not np.isfinite(size) or size > 1.5 * last[j]:
                if last[j] < 3 * TOL:
                    done.append(jj)         # a step that grows within 3 TOL is rounding: stop
                elif refreshes[j] < 4:      # the anchor is poor here: use this fold's Hessian at this point
                    r = _rate(Xs @ Wf[:, j]) * M[:, fold_of[j]]
                    if hess:
                        own[j] = linalg.cho_factor(hess(r))
                    else:
                        tr = M[:, fold_of[j]] > 0
                        own[j] = linalg.cho_factor(_hessian(Xh[tr], r[tr]))
                    refreshes[j] += 1
                    last[j] = np.inf
                else:
                    failed.append(j)
                    done.append(jj)
                continue
            Wf[:, j] -= step
            last[j] = size
            if size < TOL:
                done.append(jj)
        active = np.delete(active, done)
        if len(active) == 0:
            break
    for j in list(active) + failed:
        Wf[:, j], _ = _newton(X, Y[:, cell_of[j]], W[:, cell_of[j]], mask=M[:, fold_of[j]] > 0, hess=hess)
    llh = np.full((K, n), np.nan)
    psum = np.zeros((p, n))
    for k in range(K):
        test = fold == k
        Wk = Wf[:, fold_of == k]
        psum += Wk
        llh[k] = _test_llh(_rate(X[test] @ Wk), Y[test])
    return llh, psum / K, W


def _signrank_greater(a, b) -> float:
    d = np.asarray(a) - np.asarray(b)
    d = d[np.isfinite(d)]
    d = d[d != 0]
    if len(d) == 0:
        return 1.0
    return float(stats.wilcoxon(d, alternative="greater").pvalue)


class Design:
    """The blocks of one session in a fixed variable order, with columns for any subset."""

    def __init__(self, design: dict, names: list[str]):
        self.names = names
        self.design = design
        self.fold = design["fold"]
        mats = [np.ones((len(self.fold), 1))] + [design["blocks"][k] for k in names]
        self.X = np.hstack(mats)
        sizes = [m.shape[1] for m in mats]
        starts = np.cumsum([0] + sizes)
        self.cols = {k: np.arange(starts[i + 1], starts[i + 2]) for i, k in enumerate(names)}

    def sparse_columns(self, cols: np.ndarray):
        """The columns `cols` of the design as a sparse row matrix."""
        if getattr(self, "_csc", None) is None or self._csc_of is not self.X:
            self._csc, self._csc_of = sparse.csc_matrix(self.X), self.X
        return self._csc[:, cols].tocsr()

    def key(self, model) -> tuple[str, ...]:
        return tuple(sorted(model, key=self.names.index))

    def columns(self, model) -> np.ndarray:
        return np.r_[0, *[self.cols[k] for k in self.names if k in model]].astype(int)


class Block2D:
    """Hessians X' diag(r) X of designs with a 2-D position block, grouping bins by the spline
    cell they fall in (where the 16 non-zero position columns are the same), so that each group
    is a small dense product."""

    def __init__(self, design: Design):
        cols, vals = design.design["B_sparse"]
        start = design.cols["B"][0]
        key = cols[:, 0]
        order = np.argsort(key, kind="stable")
        bounds = np.flatnonzero(np.diff(key[order])) + 1
        self.groups = [(g, cols[g[0]] + start) for g in np.split(order, bounds)]
        self.vals = vals
        self.X = design.X
        self.bset = set(design.cols["B"].tolist())

    def hessian(self, cols: np.ndarray, r: np.ndarray) -> np.ndarray:
        """Hessian (full, symmetric) over the columns `cols` (sorted, of the full design) with
        rates r per bin."""
        pos = {c: i for i, c in enumerate(cols)}
        rest = np.array([c for c in cols if c not in self.bset])
        ri = np.array([pos[c] for c in rest])
        H = np.zeros((len(cols), len(cols)))
        sr = np.sqrt(r)
        Xr = self.X[:, rest] * sr[:, None]
        RR = blas.dsyrk(1.0, Xr, trans=1)
        H[np.ix_(ri, ri)] = np.triu(RR) + np.triu(RR, 1).T
        if len(ri) < len(cols):
            for rows, c16 in self.groups:
                bi = np.array([pos[c] for c in c16])
                A = self.vals[rows] * sr[rows, None]
                H[np.ix_(bi, bi)] += A.T @ A
                H[np.ix_(bi, ri)] += A.T @ Xr[rows]
            bi_all = np.array([pos[c] for c in cols if c in self.bset])
            H[np.ix_(ri, bi_all)] = H[np.ix_(bi_all, ri)].T
        H[np.diag_indices_from(H)] += ALPHA
        return H


def _start(design: Design, model, parent, rec, y) -> np.ndarray:
    """Starting parameters: the parent model's fit, zeros for the added variable; with no parent
    fit, the mean rate."""
    cols = design.columns(model)
    w = np.zeros(len(cols))
    if rec is not None:
        pc = design.columns(parent)
        pos = {c: i for i, c in enumerate(cols)}
        for i, c in enumerate(pc):
            w[pos[c]] = rec["w_all"][i]
    else:
        w[0] = np.log(max(y.mean(), 1e-6))
    return w


def _full_start(design: Design, model, rec, y) -> np.ndarray:
    """A parent fit placed in the columns of the model with every variable."""
    w = np.zeros(design.X.shape[1])
    if rec is None:
        w[0] = np.log(max(y.mean(), 1e-6))
    else:
        w[design.columns(model)] = rec["w_all"]
    return w


def fit_models(design: Design, Y: np.ndarray, jobs: dict, fits: list[dict], other: Design | None = None,
               shuffled: str | None = None) -> None:
    """Fit each model in `jobs` (model -> list of (cell, parent)) for its cells, in place into
    `fits[cell][model]`. Models that contain `shuffled` are fitted on `other`.

    The Hessian of the model with every variable is computed once per cell at its parent fit, and
    each candidate model starts from its block of it."""
    anchors = {}
    for model, items in jobs.items():
        d = other if (shuffled is not None and shuffled in model) else design
        for c, parent in items:
            if (c, id(d)) not in anchors:
                w = _full_start(d, parent, fits[c].get(parent), Y[:, c])
                anchors[(c, id(d))] = _full_hessian(d, _rate(d.X @ w))
    for model, items in jobs.items():
        d = other if (shuffled is not None and shuffled in model) else design
        cells = [c for c, _ in items]
        cols = d.columns(model)
        W0 = np.stack([_start(d, model, parent, fits[c].get(parent), Y[:, c]) for c, parent in items], 1)
        H0 = [anchors[(c, id(d))][np.ix_(cols, cols)] for c in cells]
        for h in H0:                        # the block was cut from an upper triangle: make it symmetric
            h[:] = np.triu(h) + np.triu(h, 1).T
        llh, pm, W = fit_cv(d.X[:, cols], Y[:, cells], d.fold, W0, H0, _hess_for(d, cols), d.sparse_columns(cols))
        for j, c in enumerate(cells):
            fits[c][model] = {"llh": llh[:, j], "param": pm[:, j], "w_all": W[:, j]}


def _block(d: Design):
    if "B_sparse" not in d.design:
        return None
    if getattr(d, "_block", None) is None or d._block.X is not d.X:
        d._block = Block2D(d)
    return d._block


def _hess_for(d: Design, cols: np.ndarray):
    """The Hessian function of a model's columns: grouped for 2-D position designs, else None
    (dense products)."""
    blk = _block(d)
    if blk is None:
        return None
    return lambda r, blk=blk, cols=cols: blk.hessian(cols, r)


def _full_hessian(d: Design, r: np.ndarray) -> np.ndarray:
    blk = _block(d)
    if blk is not None:
        return blk.hessian(np.arange(d.X.shape[1]), r)
    H = _hessian(d.X, r)
    return np.triu(H) + np.triu(H, 1).T


def forward_search(design: Design, Y: np.ndarray, fits: list[dict] | None = None, other: Design | None = None,
                   shuffled: str | None = None) -> tuple[list[dict], list[dict]]:
    """Forward search of `forward_search_kfold.m` for every cell (column of Y), models batched.

    Per cell: `selected`, the encoded variables (empty when the selected model is not better than
    the mean rate model by the one-sided signed-rank test, as the Methods state), and
    `code_selected`, the code's variant, whose final test uses the last model compared (the one
    that failed to improve on the selected model) in place of the selected one. `fits` holds every
    model fitted per cell. With `shuffled`, models that contain that variable are fitted on `other`
    (the design with that variable shuffled in time) and the rest are reused from `fits`.
    """
    n = Y.shape[1]
    if fits is None:
        fits = [dict() for _ in range(n)]
    else:
        fits = [{m: r for m, r in f.items() if shuffled is None or shuffled not in m} for f in fits]
    selected = [() for _ in range(n)]
    base = [np.full(N_FOLDS, -5.0) for _ in range(n)]
    last_top = [None] * n
    active = list(range(n))
    while active:
        jobs: dict = {}
        cands = {}
        for c in active:
            cands[c] = [design.key(selected[c] + (v,)) for v in design.names if v not in selected[c]]
            for m in cands[c]:
                if m not in fits[c]:
                    jobs.setdefault(m, []).append((c, selected[c]))
        fit_models(design, Y, jobs, fits, other, shuffled)
        still = []
        for c in active:
            top = max(cands[c], key=lambda m: np.nanmean(fits[c][m]["llh"]))
            last_top[c] = top
            if _signrank_greater(fits[c][top]["llh"], base[c]) < P_STEP:
                selected[c] = top
                base[c] = fits[c][top]["llh"]
                if len(top) < len(design.names):
                    still.append(c)
        active = still
    out = []
    for c in range(n):
        p_sel = _signrank_greater(fits[c][selected[c]]["llh"], np.zeros(N_FOLDS)) if selected[c] else 1.0
        p_code = _signrank_greater(fits[c][last_top[c]]["llh"], np.zeros(N_FOLDS))
        out.append({"selected": selected[c] if p_sel < P_STEP else (), "path": selected[c],
                    "code_selected": selected[c] if p_code < P_STEP else (), "final_p": p_sel})
    return out, fits


def reselect(all_llh: dict, names: list[str], alpha: float) -> tuple[str, ...] | None:
    """The forward search's selection at another step threshold, from the models already fitted;
    None when it needs a model that was not fitted (a looser threshold than the run's)."""
    key = lambda m: tuple(sorted(m, key=names.index))
    selected, base = (), np.full(N_FOLDS, -5.0)
    while len(selected) < len(names):
        cands = [key(selected + (v,)) for v in names if v not in selected]
        if any(c not in all_llh for c in cands):
            return None
        top = max(cands, key=lambda m: np.nanmean(all_llh[m]))
        if _signrank_greater(all_llh[top], base) < alpha:
            selected, base = top, all_llh[top]
        else:
            break
    if selected and _signrank_greater(all_llh[selected], np.zeros(N_FOLDS)) < alpha:
        return selected
    return ()


def knn_clustering_p(coords: np.ndarray, labels: np.ndarray, ks=range(1, 11), n_perm: int = 1000,
                     rng: np.random.Generator | None = None) -> dict:
    """P of the mean distance of labelled points to their k nearest labelled neighbours, against
    label permutations (fraction of permuted distances smaller than observed); Methods, "Using PCA
    to identify neural clusters"."""
    rng = rng or np.random.default_rng(0)
    D = np.sqrt(((coords[:, None, :] - coords[None, :, :]) ** 2).sum(-1))
    m = int(labels.sum())
    if m < 2:
        return {}
    kmax = min(max(ks), m - 1)

    def stat(idx):
        sub = D[np.ix_(idx, idx)]
        part = np.sort(np.partition(sub, kmax, axis=1)[:, :kmax + 1], axis=1)[:, 1:]
        return np.array([part[:, :min(k, kmax)].mean() for k in ks])

    obs = stat(np.where(labels)[0])
    null = np.array([stat(rng.choice(len(labels), m, replace=False)) for _ in range(n_perm)])
    return {k: float(np.mean(null[:, i] < obs[i])) for i, k in enumerate(ks)}


def reduced_models(design: Design, Y: np.ndarray, results: list[dict], fits: list[dict]) -> list[dict]:
    """For cells with two or more encoded variables, the ten-fold fit of the selected model with
    each variable removed; returns per cell {variable: contribution} where the contribution is
    1 - LLH(reduced) / LLH(selected), LLH the mean test value over folds (Methods, "Computing
    contribution to model performance"), and the literal reading LLH(reduced) / LLH(selected)."""
    jobs: dict = {}
    for c, r in enumerate(results):
        sel = r["selected"]
        if len(sel) >= 2:
            for v in sel:
                m = tuple(x for x in sel if x != v)
                if m not in fits[c]:
                    jobs.setdefault(m, []).append((c, sel))
    # start each reduced model from the selected fit without the removed block
    for model, items in jobs.items():
        cells = [c for c, _ in items]
        cols = design.columns(model)
        W0 = []
        for c, sel in items:
            sc = design.columns(sel)
            w = dict(zip(sc, fits[c][sel]["w_all"]))
            W0.append(np.array([w[k] for k in cols]))
        llh, pm, W = fit_cv(design.X[:, cols], Y[:, cells], design.fold, np.stack(W0, 1), hess=_hess_for(design, cols))
        for j, c in enumerate(cells):
            fits[c][model] = {"llh": llh[:, j], "param": pm[:, j], "w_all": W[:, j]}
    out = []
    for c, r in enumerate(results):
        sel = r["selected"]
        d = {}
        if len(sel) >= 2:
            full = np.nanmean(fits[c][sel]["llh"])
            for v in sel:
                red = np.nanmean(fits[c][tuple(x for x in sel if x != v)]["llh"])
                d[v] = (1 - red / full, red / full)
        out.append(d)
    return out


def half_fits(design: Design, Y: np.ndarray, results: list[dict], fits: list[dict]) -> list[dict]:
    """Parameters of the selected model fitted on the first and on the second half of the kept
    bins (Methods, "Calculating tuning curve stability")."""
    T = len(design.fold)
    halves = [np.arange(T) < T // 2, np.arange(T) >= T // 2]
    out = []
    for c, r in enumerate(results):
        sel = r["selected"]
        if not sel:
            out.append({})
            continue
        cols = design.columns(sel)
        X = design.X[:, cols]
        w0 = fits[c][sel]["w_all"]
        out.append({"halves": [_newton(X, Y[:, c], w0, mask=h, hess=_hess_for(design, cols))[0] for h in halves]})
    return out


# ---------------------------------------------------------------- tuning curves

def model_curve(design: Design, model: tuple[str, ...], w: np.ndarray, var: str, grid: np.ndarray,
                rows: np.ndarray | None = None) -> np.ndarray:
    """Model-derived tuning curve (spikes/s) of a 1-D variable at the values `grid` (Methods,
    eq. 10): exp(Y(m) w_var) times gamma, gamma = exp(b0) times the mean over bins (`rows`) of
    each other variable's factor."""
    cols = design.columns(model)
    wd = dict(zip(cols, w))
    gamma = np.exp(wd[0])
    for v in model:
        if v == var:
            continue
        factor = np.exp(design.X[:, design.cols[v]] @ np.array([wd[c] for c in design.cols[v]]))
        gamma *= np.mean(factor if rows is None else factor[rows])
    if var == "Ha":
        Y = dense(spline_1d_circ(grid, OF_HD_BINS))
    else:
        cp = design.design["cpts"][var]
        Y = dense(spline_1d(np.clip(grid, cp[0] + 1e-9, cp[-1]), cp))
    return np.exp(Y @ np.array([wd[c] for c in design.cols[var]])) * gamma / DT


def curve_range(values: np.ndarray, pct: tuple[float, float], preset: tuple[float, float] | None):
    """Range of a tuning curve (Methods, "Visualizing tuning curves") and the fraction of the
    preset range it covers."""
    lo, hi = np.percentile(values[np.isfinite(values)], pct)
    if preset is None:
        return float(lo), float(hi), 1.0
    a, b = max(lo, preset[0]), min(hi, preset[1])
    return float(a), float(b), float(max(b - a, 0) / (preset[1] - preset[0]))


def shape_order(x: np.ndarray, curve: np.ndarray, max_order: int = 5, threshold: float = 0.9) -> int:
    """Lowest polynomial order (1 to 5) whose fraction of error explained, relative to a flat line,
    exceeds 0.9 on the range-normalised curve; 0 when none does."""
    c = (curve - curve.min()) / (curve.max() - curve.min()) if curve.max() > curve.min() else curve * 0
    base = np.mean((c - c.mean()) ** 2)
    if base == 0:
        return 0
    xs = (x - x.mean()) / x.std()
    for order in range(1, max_order + 1):
        fit = np.polyval(np.polyfit(xs, c, order), xs)
        if (base - np.mean((c - fit) ** 2)) / base > threshold:
            return order
    return 0


def side_slopes(x: np.ndarray, curve: np.ndarray) -> tuple[float, float]:
    """Slopes of lines fit to the curve below and above zero (Methods)."""
    neg, pos = x < 0, x > 0
    s_neg = np.polyfit(x[neg], curve[neg], 1)[0] if neg.sum() > 2 else np.nan
    s_pos = np.polyfit(x[pos], curve[pos], 1)[0] if pos.sum() > 2 else np.nan
    return float(s_neg), float(s_pos)


def velocity_class(x, curve, order, ratio=0.5) -> str:
    """Las, NLas, NLs-pos or NLs-neg (see the claims file for the rule); '' when not well fit or
    when the range does not span zero."""
    if order == 0:
        return ""
    if order == 1:
        return "Las"
    s_neg, s_pos = side_slopes(x, curve)
    if not (np.isfinite(s_neg) and np.isfinite(s_pos)):
        return ""
    if np.sign(s_neg) != np.sign(s_pos) and min(abs(s_neg), abs(s_pos)) >= ratio * max(abs(s_neg), abs(s_pos)):
        return "NLs-pos" if s_pos > 0 else "NLs-neg"
    return "NLas"


def stability(c1: np.ndarray, c2: np.ndarray) -> float:
    return float(np.corrcoef(c1, c2)[0, 1]) if np.std(c1) > 0 and np.std(c2) > 0 else np.nan


# ---------------------------------------------------------------- one session, in parallel

_SESSIONS: list[dict] = []
_DESIGNS: dict = {}


def prepare(sessions: list[dict], kind: str) -> None:
    """Hold the sessions for the worker processes (shared by fork): the kept bins and the spike
    counts in them. The spline designs are built when a session is analysed (`design`)."""
    _SESSIONS.clear()
    _DESIGNS.clear()
    for s in sessions:
        names = VR_VARS if kind == "vr" else of_vars(s)
        keep = vr_keep(s) if kind == "vr" else of_keep(s)
        _SESSIONS.append({"kind": kind, "session": s, "names": names, "Y": s["counts"][keep],
                          "full": {k: s[k] for k in names if k in s}, "keep": keep})


def design(si: int) -> Design:
    """The design of session si, kept for the last session asked for."""
    if si not in _DESIGNS:
        _DESIGNS.clear()
        e = _SESSIONS[si]
        d = vr_design(e["session"]) if e["kind"] == "vr" else of_design(e["session"])
        _DESIGNS[si] = Design(d, e["names"])
    return _DESIGNS[si]


def _shuffled(design: Design, var: str, seed) -> Design:
    if var == "B" and "B_sparse" in design.design:
        raise ValueError("shuffling the 2-D position block is not supported")
    perm = np.random.default_rng(seed).permutation(design.X.shape[0])
    other = Design.__new__(Design)
    other.names, other.design, other.fold, other.cols = design.names, design.design, design.fold, design.cols
    other.X = design.X.copy()
    other.X[:, design.cols[var]] = design.X[perm][:, design.cols[var]]
    return other


def _ranges(entry: dict, var: str, rows=None):
    kind = entry["kind"]
    if var == "Ha":
        return 0.0, 2 * np.pi, 1.0
    pct = VR_KEEP if kind == "vr" else OF_KEEP
    preset = (VR_PRESET if kind == "vr" else OF_PRESET).get(var)
    v = entry["full"][var] if rows is None else entry["full"][var][entry["keep"]][rows]
    return curve_range(v, pct, preset)


def analyse(task) -> list[dict]:
    """Selection, contributions, tuning curves and their stability, and false detections under
    shuffles, for some cells of one session. `task` = (session index, cell indices, variables to
    shuffle, cells (of these) to run the shuffles on, seed)."""
    set_threads(1)
    si, cells, shuffle_vars, shuffle_cells, seed = task
    entry = _SESSIONS[si]
    D, Y = design(si), entry["Y"][:, cells]
    results, fits = forward_search(D, Y)
    contrib = reduced_models(D, Y, results, fits)
    halves = half_fits(D, Y, results, fits)
    T = Y.shape[0]
    rows = [np.arange(T) < T // 2, np.arange(T) >= T // 2]
    out = []
    for j, c in enumerate(cells):
        sel = results[j]["selected"]
        rec = {"cell": int(c), "selected": sel, "code_selected": results[j]["code_selected"],
               "path": results[j]["path"], "llh": float(np.nanmean(fits[j][sel]["llh"])) if sel else np.nan,
               "llh_folds": fits[j][sel]["llh"] if sel else None, "contrib": contrib[j], "curves": {},
               "all_llh": {m: r["llh"] for m, r in fits[j].items()}}
        for v in sel:
            if v == "B" and entry["kind"] == "of":
                continue
            lo, hi, cover = _ranges(entry, v)
            grid = np.linspace(lo, hi, CURVE_POINTS)
            curve = model_curve(D, sel, fits[j][sel]["param"], v, grid)
            r1, r2 = _ranges(entry, v, rows[0]), _ranges(entry, v, rows[1])
            a, b = max(lo, r1[0], r2[0]), min(hi, r1[1], r2[1])
            st = np.nan
            if b > a:
                g = np.linspace(a, b, CURVE_POINTS)
                st = stability(model_curve(D, sel, halves[j]["halves"][0], v, g, rows[0]),
                               model_curve(D, sel, halves[j]["halves"][1], v, g, rows[1]))
            rec["curves"][v] = {"grid": grid, "curve": curve, "cover": cover, "stability": st}
        out.append(rec)
    if shuffle_vars and len(shuffle_cells):
        idx = [list(cells).index(c) for c in shuffle_cells]
        sub_fits = [fits[i] for i in idx]
        Ys = Y[:, idx]
        for vi, v in enumerate(shuffle_vars):
            other = _shuffled(D, v, [seed, si, vi])
            res_s, _ = forward_search(D, Ys, sub_fits, other=other, shuffled=v)
            for i, r in zip(idx, res_s):
                out[i].setdefault("shuffle", {})[v] = v in r["selected"]
    return out


def run(tasks: list, workers: int = 4) -> list[dict]:
    """Run `analyse` over tasks in forked worker processes, largest first."""
    import multiprocessing as mp
    order = sorted(range(len(tasks)), key=lambda i: -_SESSIONS[tasks[i][0]]["Y"].shape[0] * len(tasks[i][1]))
    with mp.get_context("fork").Pool(workers) as pool:
        parts = pool.map(analyse, [tasks[i] for i in order], chunksize=1)
    out = []
    for i, part in zip(order, parts):
        for rec in part:
            rec["session"] = tasks[i][0]
        out.extend(part)
    return sorted(out, key=lambda r: (r["session"], r["cell"]))


def tasks_for(chunk: int = 24, shuffle_vars=(), shuffle_fraction: float = 0.0, shuffle_cells=None,
              seed: int = 0) -> list:
    """Chunks of cells per session; `shuffle_fraction` of each session's cells (seeded), or the
    sessions listed in `shuffle_cells` (session index -> all), get the shuffle runs."""
    tasks = []
    for si, entry in enumerate(_SESSIONS):
        n = entry["Y"].shape[1]
        if shuffle_cells is not None:
            chosen = set(range(n)) if si in shuffle_cells else set()
        else:
            k = int(round(shuffle_fraction * n))
            chosen = set(np.random.default_rng([seed, si]).choice(n, k, replace=False).tolist()) if k else set()
        for start in range(0, n, chunk):
            cells = list(range(start, min(n, start + chunk)))
            tasks.append((si, cells, list(shuffle_vars), [c for c in cells if c in chosen], seed))
    return tasks


# ---------------------------------------------------------------- groups of the freely moving mice

# The files carry no cohort or study label. The groups below are read from the files (subject
# names, identifiers, arena sizes); the notebook shows the features and compares each group's unit
# total with the count the Methods give for each study ("Animals", freely moving dataset).
OF_GROUPS = {
    "Cohort 1": ["Carnation", "Daisy", "Fuschia", "Jasmine", "Orchid", "Rose"],     # 50 and 70 cm arenas only
    "Cohort 2, unpublished": ["Azalea", "Camelia", "Crocus", "Lupine", "Magnolia"],  # 'rectangle_'/'square_' identifiers, 75 cm
    "Cohort 2, Campbell et al.": ["Barbara", "Ella"],                                # 91.4 cm arena
    "Cohort 2, Eggink et al.": ["Case", "Dorian", "Ford Prefect", "James", "Japie", "Lukas", "Pinky"],  # 'o' identifiers, 100 cm
    "Cohort 2, Munn et al.": ["Flip", "Rascal", "Reeves", "Ringo", "Snoopy"],         # the rest, mostly 100 cm
}
METHODS_GROUPS = {"Cohort 1": (6, 179), "Cohort 2, unpublished": (5, 228), "Cohort 2, Campbell et al.": (2, 122),
                  "Cohort 2, Eggink et al.": (7, 389), "Cohort 2, Munn et al.": (6, 282)}


def group_of(subject: str) -> str:
    return next(g for g, subs in OF_GROUPS.items() if subject in subs)


def is_vr_paper_session(identifier: str) -> bool:
    """The head-fixed sessions of the paper: identifiers containing 'baseline' (see the notebook)."""
    return "baseline" in identifier


def lap_reliability(session: dict, lag_s: float = 0.0, nbins: int = 40) -> float:
    """Median over units (100 spikes or more) of the correlation between the track rate maps of
    odd and even laps, with spikes paired to the behaviour `lag_s` later (positive: spikes lead)."""
    B = session["B"]
    wraps = np.where(np.diff(B) < -200)[0] + 1
    lap = np.searchsorted(wraps, np.arange(len(B)), side="right")
    bins = np.clip((B / 400 * nbins).astype(int), 0, nbins - 1)
    C = np.roll(session["counts"], int(round(lag_s / DT)), axis=0)
    sel = [(lap % 2) == p for p in (0, 1)]
    occ = [np.bincount(bins[m], None, nbins) for m in sel]
    rs = []
    for c in np.where(session["counts"].sum(0) >= 100)[0]:
        maps = [np.bincount(bins[m], C[m, c], nbins) / np.maximum(o, 1) for m, o in zip(sel, occ)]
        if np.std(maps[0]) > 0 and np.std(maps[1]) > 0:
            rs.append(np.corrcoef(maps[0], maps[1])[0, 1])
    return float(np.median(rs)) if rs else np.nan


def spatial_reliability(session: dict, lag_s: float = 0.0, bin_cm: float = 5.0) -> float:
    """Median over units (100 spikes or more) of the correlation between the 2-D rate maps of the
    first and second half of a freely moving session, with spikes paired to the behaviour `lag_s`
    later; unvisited bins left out."""
    ok = np.isfinite(session["x"]) & np.isfinite(session["y"])
    x = np.where(ok, session["x"] - np.nanmin(session["x"]), 0)
    y = np.where(ok, session["y"] - np.nanmin(session["y"]), 0)
    nx, ny = int(np.ptp(x[ok]) // bin_cm) + 1, int(np.ptp(y[ok]) // bin_cm) + 1
    idx = (x // bin_cm).astype(int) * ny + (y // bin_cm).astype(int)
    T = len(x)
    halves = [ok & (np.arange(T) < T // 2), ok & (np.arange(T) >= T // 2)]
    C = np.roll(session["counts"], int(round(lag_s / DT)), axis=0)
    occ = [np.bincount(idx[h], None, nx * ny) for h in halves]
    both = (occ[0] > 0) & (occ[1] > 0)
    rs = []
    for c in np.where(session["counts"].sum(0) >= 100)[0]:
        maps = [np.bincount(idx[h], C[h, c], nx * ny)[both] / o[both] for h, o in zip(halves, occ)]
        if np.std(maps[0]) > 0 and np.std(maps[1]) > 0:
            rs.append(np.corrcoef(maps[0], maps[1])[0, 1])
    return float(np.median(rs)) if rs else np.nan


def mutual_information(a: np.ndarray, b: np.ndarray, bins: int = 20) -> float:
    """Mutual information (bits) between two variables, each cut into equal-width bins."""
    h, _, _ = np.histogram2d(a, b, bins)
    p = h / h.sum()
    pa, pb = p.sum(1, keepdims=True), p.sum(0, keepdims=True)
    nz = p > 0
    return float(np.sum(p[nz] * np.log2(p[nz] / (pa @ pb)[nz])))


def set_threads(n: int = 1) -> None:
    """Limit linear-algebra threads (many small fits run in parallel processes)."""
    for k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
        os.environ[k] = str(n)
    try:
        from threadpoolctl import threadpool_limits
        threadpool_limits(n)
    except ImportError:
        pass
