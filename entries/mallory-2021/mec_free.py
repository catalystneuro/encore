"""Loading and LN-model measures for the freely moving cells of Cohort 1 (Mallory, Hardcastle et al.
2021), from the paper's figshare Dataset 1 (doi:10.6084/m9.figshare.13425392.v1,
Freely_moving_data_with_inertial_sensor.mat), which holds the head pitch and roll that dandiset
000053 lacks.

The file is one compressed MATLAB 5 variable, a struct of 179 cells, so it cannot be read in part: it
is streamed into memory (1.7 GB), read with scipy, and reduced as it loads to one copy of each
session's behaviour and each cell's spike counts in the 20 ms bins of that behaviour. Nothing is
written to disk.

The model fitting, the forward search and the shape measures are those of `mec_ln` (see its
docstring). Where the parameters for the open field come from:

- Inner 95% (2.5th to 97.5th percentile) of each variable per session (Methods, "Data
  pre-processing"), with the claims file's two readings of open detail (2), drop or clip. Azimuthal
  head direction is circular and its tuning curves are shown over 0 to 360 deg (Methods,
  "Visualizing tuning curves"), so it is not restricted; an assumption, as the Methods do not
  single it out.
- Control points as the claims file's opening comment gives them: position 2D (spline_2d.m), arena
  side x 15/100 per axis, rounded as MATLAB rounds; head direction 10, circular (spline_1d_circ.m);
  speed every 5 cm/s, as in `mec_ln`; 8 for pitch, roll, azimuthal head velocity and the pitch and
  roll velocities (the claims file's standard choice for the last two). Each spans the variable's
  inner range.
- Pitch and roll are stored in radians and are converted to degrees. Their velocities are not in the
  deposit; they are taken as the difference of the angle over time, the way the Methods compute
  azimuthal head velocity ("Angular azimuthal head velocity was calculated as the difference in
  azimuth head direction angles over time"), as a forward difference, the way the deposit's
  azimuthal head velocity is computed from its head direction (checked in the notebook).
- Visualizing ranges (Methods, "Visualizing tuning curves"): the larger of the 2.5th percentile and
  -50 deg for pitch and roll, -100 deg/s for azimuthal head velocity, and the matching upper bounds;
  0 to 360 deg for head direction.
- Shape (Methods, "Quantifying tuning curve shape"): pitch and roll curves first smoothed with a
  moving mean over 20 of the 200 bins (smoothdata's default method, width 20); classified only when
  the animal explored 50% of the preset range, under the two readings of open detail (4).
"""

from __future__ import annotations

import io
import math

import numpy as np

import mec_ln as L

FIGSHARE_DS1_DOI = "10.6084/m9.figshare.13425392.v1"
FIGSHARE_DS1_URL = "https://ndownloader.figshare.com/files/25829231"   # article 13425392, version 1

DT = 0.02
PCT = (2.5, 97.5)
VARS = ["B", "Bs", "Ha", "Hp", "Hr", "Had", "Hpd", "Hrd"]
HEAD = ["Ha", "Hp", "Hr", "Had", "Hpd", "Hrd"]
N_CPTS = {"Hp": 8, "Hr": 8, "Had": 8, "Hpd": 8, "Hrd": 8}
N_HD = 10
POS_RATIO = 15 / 100
PRESET = {"Hp": (-50.0, 50.0), "Hr": (-50.0, 50.0), "Had": (-100.0, 100.0)}
EXPLORED_MIN = 0.5   # Methods, "Quantifying tuning curve shape": 50% of the range for head variables
SMOOTH = 20


def round_half_up(x: float) -> int:
    return int(math.floor(x + 0.5))


# ----------------------------------------------------------------------------------------- loading
def fetch(url: str = FIGSHARE_DS1_URL) -> bytes:
    import requests
    buf = io.BytesIO()
    with requests.get(url, stream=True, timeout=120) as r:
        r.raise_for_status()
        for chunk in r.iter_content(chunk_size=1 << 24):
            buf.write(chunk)
    return buf.getvalue()


def load_dataset1(raw: bytes) -> dict:
    """Sessions of Dataset 1: one copy of the behaviour of each session (the cells of a session carry
    identical copies; `same_behaviour` says whether they were), and each cell's spike counts in the
    20 ms bins of the behaviour samples."""
    import scipy.io as sio
    m = sio.loadmat(io.BytesIO(raw), squeeze_me=True, struct_as_record=False)
    cells = m.pop("cell_info")
    sessions = {}
    for c in cells:
        sid = c.cell_id.rsplit("_T", 1)[0]
        if sid not in sessions:
            t = np.asarray(c.time, float)
            beh = {"x": c.body_position_x, "y": c.body_position_y, "Bs": c.body_speed,
                   "Ha": c.azimuthal_head_direction, "Had": c.azimuthal_head_velocity,
                   "Hp": np.degrees(c.pitch), "Hr": np.degrees(c.roll)}
            beh = {k: np.asarray(v, float) for k, v in beh.items()}
            sessions[sid] = {"animal": str(c.animal_id), "arena": float(c.arena_size_cm), "t": t,
                             "beh": beh, "cells": [], "Y": [], "same_behaviour": True,
                             "_ref": (np.asarray(c.body_position_x), np.asarray(c.pitch))}
        s = sessions[sid]
        ref = s["_ref"]
        s["same_behaviour"] &= bool(np.array_equal(ref[0], c.body_position_x, equal_nan=True)
                                    and np.array_equal(ref[1], c.pitch, equal_nan=True))
        t = s["t"]
        edges = np.concatenate([t, [t[-1] + DT]])
        st = np.atleast_1d(np.asarray(c.spike_times, float))
        s["cells"].append(str(c.cell_id))
        s["Y"].append(np.histogram(st, edges)[0].astype(np.int16))
        s.setdefault("n_spikes", []).append(len(st))
    del cells, m
    for s in sessions.values():
        s.pop("_ref")
        s["Y"] = np.vstack(s["Y"])
        b = s["beh"]
        for v, src in (("Hpd", "Hp"), ("Hrd", "Hr")):
            b[v] = np.append(np.diff(b[src]), np.nan) / DT
    return sessions


# ----------------------------------------------------------------------------------------- design
def spline_circ(y: np.ndarray, n: int = N_HD) -> np.ndarray:
    """spline_1d_circ.m with n control points evenly over 0 to 2 pi."""
    h = 2 * math.pi / n
    yy = np.mod(y, 2 * math.pi)
    j = np.floor(yy / h).astype(int) % n
    u = (yy - j * h) / h
    p = np.stack([u ** 3, u ** 2, u, np.ones_like(u)], axis=1) @ L._S
    X = np.zeros((len(y), n))
    rows = np.arange(len(y))
    for k in range(4):
        X[rows, (j - 1 + k) % n] += p[:, k]
    return X


def spline_2d(x, y, cx, cy):
    """spline_2d.m: the outer product of the two 1D spline rows (column order differs from the
    code's, which does not change a fit)."""
    X1 = L.spline_1d(x, cx)
    X2 = L.spline_1d(y, cy)
    return (X1[:, :, None] * X2[:, None, :]).reshape(len(x), -1)


def cpts_1d(name, lo, hi):
    if name == "Bs":
        n = max(2, int(round((hi - lo) / L.SPEED_STEP)) + 1)
    else:
        n = N_CPTS[name]
    c = np.linspace(lo, hi, n)
    c[0] -= 1e-6 * max(1.0, abs(hi - lo))
    return c


def basis(name, values, cpts):
    if name == "Ha":
        return spline_circ(values)
    return L.spline_1d(np.clip(values, cpts[0] + 1e-9, cpts[-1]), cpts)


def prepare(sess: dict, range_mode: str = L.RANGE_DROP, variables=VARS) -> dict:
    """Bins kept for the model, the variables' inner ranges and the spline blocks of one session."""
    beh = sess["beh"]
    dims = [k for k in ("x", "y", "Bs", "Ha", "Hp", "Hr", "Had", "Hpd", "Hrd") if k in beh]
    valid = np.ones(len(sess["t"]), bool)
    for k in dims:
        valid &= np.isfinite(beh[k])
    lims = {k: tuple(np.percentile(beh[k][valid], PCT)) for k in dims if k != "Ha"}
    lims["Ha"] = (0.0, 2 * math.pi)
    if range_mode == L.RANGE_DROP:
        keep = valid.copy()
        for k in dims:
            if k != "Ha":
                keep &= (beh[k] >= lims[k][0]) & (beh[k] <= lims[k][1])
        vals = {k: beh[k][keep] for k in dims}
    else:
        keep = valid
        vals = {k: (np.clip(beh[k][keep], *lims[k]) if k != "Ha" else beh[k][keep]) for k in dims}
    n_pos = round_half_up(sess["arena"] * POS_RATIO)
    cpts = {k: cpts_1d(k, *lims[k]) for k in dims if k not in ("x", "y", "Ha")}
    cpts["x"] = _even(lims["x"], n_pos)
    cpts["y"] = _even(lims["y"], n_pos)
    blocks = {}
    for v in variables:
        if v == "B":
            blocks[v] = spline_2d(vals["x"], vals["y"], cpts["x"], cpts["y"])
        elif v == "Ha":
            blocks[v] = spline_circ(vals["Ha"])
        else:
            blocks[v] = L.spline_1d(vals[v], cpts[v])
    return {"keep": keep, "lims": lims, "cpts": cpts, "blocks": blocks, "vals": vals,
            "n_valid": int(valid.sum()), "n_keep": int(keep.sum()), "variables": list(variables)}


def _even(lim, n):
    c = np.linspace(lim[0], lim[1], n)
    c[0] -= 1e-6 * max(1.0, abs(lim[1] - lim[0]))
    return c


# ----------------------------------------------------------------------------------------- measures
def tuning_curve(param, blocks, variables, var, grid, cpts):
    """Methods eq. 10, as mec_ln.tuning_curve, for a 1D or circular head variable."""
    lay = L._layout(blocks, variables)
    gamma = math.exp(param[0])
    for v in variables:
        if v != var:
            gamma *= float(np.mean(np.exp(blocks[v] @ param[lay[v]])))
    return np.exp(basis(var, grid, cpts) @ param[lay[var]]) * gamma / DT


def grid_of(var, lims):
    if var == "Ha":
        return np.linspace(0, 2 * math.pi, L.M_BINS, endpoint=False)
    return np.linspace(*lims[var], L.M_BINS)


def vis_range(var, lims):
    if var == "Ha":
        return 0.0, 2 * math.pi
    lo, hi = lims[var]
    if var in PRESET:
        return max(lo, PRESET[var][0]), min(hi, PRESET[var][1])
    return lo, hi


def explored(var, lims, values):
    """Open detail (4) for head variables: (a) the fraction of the preset range covered by the
    visualizing range; (b) the fraction of 20 bins over the preset range with any occupancy."""
    plo, phi = PRESET[var]
    lo, hi = vis_range(var, lims)
    a = max(0.0, hi - lo) / (phi - plo)
    occ, _ = np.histogram(values, np.linspace(plo, phi, 21))
    return a, float((occ > 0).mean())


def movmean(c, w=SMOOTH):
    """MATLAB smoothdata(c, 'movmean', w): centred window of w points (w even: w/2 before, w/2 - 1
    after), shrunk at the ends."""
    n = len(c)
    before, after = w // 2, w // 2 - 1 if w % 2 == 0 else w // 2
    cs = np.concatenate([[0.0], np.cumsum(c)])
    i = np.arange(n)
    a = np.maximum(0, i - before)
    b = np.minimum(n, i + after + 1)
    return (cs[b] - cs[a]) / (b - a)


def analyse_cell(prep, y, with_extras=True):
    """Forward search over the session's variables, then for cells that encode a head variable the
    model-derived tuning curves (on the inner range) and the stability across session halves."""
    blocks, bounds, variables = prep["blocks"], prep["bounds"], prep["variables"]
    fs = L.forward_search(blocks, y, bounds, variables)
    out = {"selected": fs["selected"], "encoded": fs["encoded"], "final_p": fs["final_p"],
           "encoded_code": fs["encoded_code"], "n_spikes": int(y.sum())}
    enc = fs["encoded"]
    if not enc or not with_extras:
        return out
    out["perf"] = float(np.nanmean(fs["sel_fits"]))
    head = [v for v in enc if v in ("Ha", "Hp", "Hr", "Had")]
    curves = {}
    for v in head:
        g = grid_of(v, prep["lims"])
        curves[v] = (g, tuning_curve(fs["sel_param"], blocks, enc, v, g, prep["cpts"].get(v)))
    out["curves"] = curves
    if not head:
        return out
    n = len(y)
    half = prep["order"] < n // 2
    Xs = L.design(blocks, enc)
    halves = []
    for m in (half, ~half):
        th = L.fit_full(Xs[m], y[m], fs["sel_full"])
        hb = {v: blocks[v][m] for v in enc}
        cs = {}
        for v in head:
            g = grid_of(v, prep["lims"])
            vals = prep["vals"][v][m]
            cs[v] = (g, tuning_curve(th, hb, enc, v, g, prep["cpts"].get(v)), vals.min(), vals.max())
        halves.append(cs)
    stab = {}
    for v in head:
        g, c1, a1, b1 = halves[0][v]
        _, c2, a2, b2 = halves[1][v]
        lo, hi = vis_range(v, prep["lims"])
        msk = (g >= max(lo, a1, a2)) & (g <= min(hi, b1, b2))
        ok = msk.sum() > 2 and np.std(c1[msk]) > 0 and np.std(c2[msk]) > 0
        stab[v] = float(np.corrcoef(c1[msk], c2[msk])[0, 1]) if ok else np.nan
    out["stability"] = stab
    return out


def curve_features(result, var, lims, values):
    """Shape measures of an encoded pitch or roll curve on the visualizing range: polynomial class
    after smoothing, the two readings of "explored" (open detail 4) and the preference under the two
    readings of open detail (5), as in mec_ln.curve_features."""
    grid, curve = result["curves"][var]
    lo, hi = vis_range(var, lims)
    msk = (grid >= lo) & (grid <= hi)
    x, c = grid[msk], curve[msk]
    if var in ("Hp", "Hr"):
        c = movmean(c)
    ex_a, ex_b = explored(var, lims, values)
    order = L.classify_shape(x, c) if len(x) > 6 else 0
    slope = np.polyfit(x, c, 1)[0] if len(x) > 2 else np.nan
    sl_neg, sl_pos = L.side_slopes(x, c) if len(x) > 6 else (np.nan, np.nan)
    x_max = float(x[np.argmax(c)]) if len(x) else np.nan
    pref_a = (1 if slope > 0 else -1) if order == 1 else (1 if x_max > 0 else -1)
    pref_b = (1 if sl_pos >= -sl_neg else -1) if np.isfinite(sl_neg) and np.isfinite(sl_pos) else pref_a
    return {"order": order, "explored_a": ex_a, "explored_b": ex_b, "slope": slope, "x_max": x_max,
            "pref_a": pref_a, "pref_b": pref_b, "stability": result.get("stability", {}).get(var, np.nan)}


_WORK = {}


def _worker(i):
    prep, Y, extras = _WORK["args"]
    return i, analyse_cell(prep, Y[i, prep["keep"]][prep["order"]].astype(float), extras)


def analyse_session(prep, Y, processes=4, with_extras=True):
    """Every cell of one session (rows of Y over all bins of the session) in forked workers sharing
    the design; `prep` comes from mec_ln.by_fold."""
    import multiprocessing as mp
    from threadpoolctl import threadpool_limits
    _WORK["args"] = (prep, Y, with_extras)
    ctx = mp.get_context("fork")
    n_proc = max(1, min(processes, Y.shape[0]))
    with threadpool_limits(1):
        with ctx.Pool(n_proc, initializer=L._init_worker) as pool:
            res = dict(pool.imap_unordered(_worker, range(Y.shape[0])))
    _WORK.clear()
    return [res[i] for i in range(Y.shape[0])]


# ----------------------------------------------------------------------------------------- Dataset 2
FIGSHARE_DS2_DOI = "10.6084/m9.figshare.13425017.v1"
FIGSHARE_DS2_URL = "https://ndownloader.figshare.com/files/25829228"   # article 13425017, version 1


def _open_ds2():
    import fsspec
    import h5py
    fh = fsspec.open(FIGSHARE_DS2_URL, block_size=2 ** 22, cache_type="blockcache").open()
    return h5py.File(fh, "r")


def dataset2_index() -> list[dict]:
    """Cell id, mouse, session and arena of every cell of Dataset 2 (a MATLAB 7.3 file, read in place
    over HTTP range requests)."""
    h = _open_ds2()
    ci = h["cell_info"]
    refs = {k: ci[k][:, 0] for k in ("cell_id", "animal_id", "arena_size_cm")}

    def text(ref):
        return "".join(chr(c) for c in np.ravel(h[ref][()]))
    # field by field: the referenced objects of one field lie together in the file
    ids = [text(r) for r in refs["cell_id"]]
    animals = [text(r) for r in refs["animal_id"]]
    arenas = [float(np.ravel(h[r][()])[0]) for r in refs["arena_size_cm"]]
    out = [{"row": i, "cell": c, "animal": a, "session": c.rsplit("_T", 1)[0], "arena": ar}
           for i, (c, a, ar) in enumerate(zip(ids, animals, arenas))]
    return out


def dataset2_series(rows: list[int], field: str, threads: int = 8) -> dict:
    """One field (e.g. azimuthal_head_velocity) of the given cells of Dataset 2, read in place, in
    `threads` threads with a file handle each."""
    from concurrent.futures import ThreadPoolExecutor
    chunks = [rows[k::threads] for k in range(threads)]

    def work(chunk):
        h = _open_ds2()
        refs = h["cell_info"][field][:, 0]
        return {i: np.ravel(h[refs[i]][()]).astype(float) for i in chunk}
    out = {}
    with ThreadPoolExecutor(threads) as ex:
        for d in ex.map(work, chunks):
            out.update(d)
    return out
