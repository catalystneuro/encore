"""Loading and measures for dandiset 001960 (Qi, Parot, Wang, Pomeroy, Lavis and Cohen 2026).

Wide-area all-optical electrophysiology of about 320 layer 1 interneurons in each of two
NDNF-Cre::NPY-GFP mice (M-YQ0201-27 and M-YQ0201-29), with three sessions per mouse:
``behavior`` (spontaneous activity), ``sparseOpto`` (intrinsic excitability mapping) and
``sparsePulseHad`` (connectivity mapping), plus a raw-movie excerpt of one behavior session.

Files are streamed from the DANDI Archive with remfile and h5py; nothing is downloaded to disk.
The large voltage arrays are stored time x cell in blocks of 10,000 frames, so they are read in
time blocks over all cells, and reduced as they are read.

Where a parameter comes from is said at each function: "claims" for the claim's criterion
(which cites the paper or its code), "paper" with the passage for a detail taken from the paper
(protocol, author step 1.6), "code" for the paper's code, https://github.com/adamcohenlab/
Qi2026WideAreaL1 at commit 181ad475520224c44d27903e7522d3e2aa76857d, "assumption" for a choice
the paper leaves open, and "standard" for a detail that cannot change a result.
"""
from __future__ import annotations

import functools

import h5py
import numpy as np
import remfile
import requests

DANDISET = "001960"
VERSION = "0.261013.2016"
API = "https://api.dandiarchive.org/api"
MICE = ("M-YQ0201-27", "M-YQ0201-29")
SESSIONS = ("behavior", "sparseOpto", "sparsePulseHad")
DT = 1.27e-3  # s per voltage frame (dandiset description; checked against timestamps)
PIXEL_UM = 6.5  # um per pixel (file notes, /general/notes; code uses the same)


@functools.lru_cache(maxsize=None)
def assets() -> dict:
    """Map asset path to asset id for the pinned version."""
    out, url = {}, f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=100"
    while url:
        r = requests.get(url, timeout=60)
        r.raise_for_status()
        d = r.json()
        out.update({a["path"]: a["asset_id"] for a in d["results"]})
        url = d.get("next")
    return out


def asset_path(mouse: str, session: str) -> str:
    return f"sub-{mouse}/sub-{mouse}_ses-{session}_behavior+ophys.nwb"


@functools.lru_cache(maxsize=None)
def open_file(mouse: str, session: str) -> h5py.File:
    aid = assets()[asset_path(mouse, session)]
    s3 = requests.head(f"{API}/assets/{aid}/download/", allow_redirects=True, timeout=60).url
    return h5py.File(remfile.File(s3), "r")


def _ragged(f, name):
    data = f[f"units/{name}"][:]
    index = f[f"units/{name}_index"][:]
    return np.split(data, index[:-1].astype(int))


@functools.lru_cache(maxsize=None)
def units(mouse: str, session: str) -> dict:
    """The units table as arrays (all 320 cells), with spike times as a list of arrays.
    Cached: callers must not modify the returned arrays."""
    f = open_file(mouse, session)
    out = {"id": f["units/id"][:]}
    for name in f["units"].attrs["colnames"]:
        if name in ("spike_times", "spike_times_no_blue", "hadamard_orthogonal_spike_times"):
            out[name] = _ragged(f, name)
        else:
            out[name] = f[f"units/{name}"][:]
    out["passed_qc"] = out["passed_qc"].astype(bool)
    out["gfp_positive"] = out["gfp_positive"].astype(bool)
    return out


PROPERTIES = ["adp_blue_norm", "optical_rheobase_norm", "max_firing_rate_hz",
              "pulse_adaptation", "membrane_time_constant_ms"]
"""The five intrinsic properties, in the column order of the code's Figure 2 (fig2_ephys.m):
V_adp, rheobase, maximum rate, adaptation, membrane time constant."""


def intrinsic_properties(mouse: str) -> np.ndarray:
    u = units(mouse, "sparseOpto")
    return np.column_stack([u[p] for p in PROPERTIES]).astype(float)


# ------------------------------------------------------------------ pairwise connectivity
PAIR_COLUMNS = ["synaptic_connection", "ipsp_amplitude_norm_per_presynaptic_spike",
                "ipsp_decay_source_units", "ipsp_decay_standard_error_source_units",
                "distance_pixels", "gap_junction_connection", "spikelet_amplitude_normalized"]


@functools.lru_cache(maxsize=None)
def pair_matrices(mouse: str) -> dict:
    """Pairwise metrics of the sparsePulseHad session as 320 x 320 matrices [pre, post].

    Row k of the table is pre = k mod 320, post = k // 320 (the MATLAB column-major order, with
    the presynaptic index fastest). The notebook checks this against the table's own id columns
    and against the presynaptic spike times stored per row.
    """
    f = open_file(mouse, "sparsePulseHad")
    g = f["analysis/pairwise_connectivity_metrics"]
    n = len(f["units/id"])
    pre = g["presynaptic_unit_id"][:].astype(int)
    post = g["postsynaptic_unit_id"][:].astype(int)
    out = {}
    for c in PAIR_COLUMNS:
        m = np.full((n, n), np.nan)
        m[pre, post] = g[c][:]
        out[c] = m
    out["synaptic_connection"] = out["synaptic_connection"] == 1
    out["gap_junction_connection"] = out["gap_junction_connection"] == 1
    out["distance_um"] = out["distance_pixels"] * PIXEL_UM
    out["table_pre"], out["table_post"] = pre, post
    return out


def pair_series(mouse: str, name: str) -> np.ndarray:
    """A connectivity_mapping series as an array [pre, post, lag] (float32).

    On disk the arrays are lag x post x pre (the code's loader: "generic HDF5 readers report the
    physical on-disk order as time x post x pre"); the notebook checks the orientation.
    """
    f = open_file(mouse, "sparsePulseHad")
    d = f[f"processing/connectivity_mapping/{name}/data"]
    return np.transpose(d[:].astype(np.float32), (2, 1, 0))


def correlation_series(mouse: str, name: str, state: str) -> np.ndarray:
    """A behavior-session state_dependent_correlations series as [trigger, target, lag].

    The cell axes index the passed_qc cells in ascending unit order (file description). On disk
    the order is lag x target x trigger (MATLAB trigger x target x lag, reversed by HDF5).
    """
    f = open_file(mouse, "behavior")
    d = f[f"processing/state_dependent_correlations/{name}_{state}/data"]
    return np.transpose(d[:].astype(np.float32), (2, 1, 0))


def distance_matrix_um(x_um, y_um):
    xy = np.column_stack([x_um, y_um])
    return np.sqrt(((xy[:, None, :] - xy[None, :, :]) ** 2).sum(-1))


# ------------------------------------------------------------------ time series
def series_timestamps(mouse, session, path="processing/optical_voltage/normalized_voltage"):
    return open_file(mouse, session)[f"{path}/timestamps"][:]


def iter_blocks(dataset, block=100_000, start=0, stop=None, cols=None):
    """Yield (first_frame, array) over time blocks of a time x cell dataset."""
    stop = dataset.shape[0] if stop is None else stop
    for a in range(start, stop, block):
        b = min(stop, a + block)
        x = dataset[a:b]
        if cols is not None:
            x = x[:, cols]
        yield a, x


def spike_frames(spike_times, timestamps):
    """Frame index of each spike, by lookup in the stored timestamps (code README: "Use the
    stored timestamps"; chunks do not join on a regular grid)."""
    idx = np.searchsorted(timestamps, spike_times)
    idx = np.clip(idx, 1, len(timestamps) - 1)
    left = timestamps[idx - 1]
    right = timestamps[idx]
    idx = np.where(np.abs(spike_times - left) <= np.abs(right - spike_times), idx - 1, idx)
    return idx.astype(np.int64)


def running_guard(speed, half_width=1000, threshold=1e-3):
    """Frames within half_width frames of |running speed| > threshold (code, Figures 4 to 6,
    buildTimeMasks: conv(abs(speed) > 1e-3, ones(2001)) > 0)."""
    run = np.abs(np.asarray(speed).ravel()) > threshold
    c = np.concatenate([[0], np.cumsum(run)])
    n = len(run)
    i = np.arange(n)
    lo = np.clip(i - half_width, 0, n)
    hi = np.clip(i + half_width + 1, 0, n)
    return (c[hi] - c[lo]) > 0


def chunk_guard(n_frames, frames_per_chunk, half_width):
    """Frames within half_width of an acquisition-chunk boundary (code, chunkBoundaryGuard)."""
    g = np.zeros(n_frames, bool)
    for b in range(0, n_frames + 1, frames_per_chunk):
        g[max(0, b - half_width):min(n_frames, b + half_width + 1)] = True
    return g


# ------------------------------------------------------------------ small measures
def exp_length_constant_loglinear(r, p):
    """Length constant from a line fitted to log(p) against r (claims, reading (b); code,
    Figure 4 STATS for the correlation length constants): -1/slope."""
    r, p = np.asarray(r, float), np.asarray(p, float)
    ok = np.isfinite(p) & (p > 0)
    slope = np.polyfit(r[ok], np.log(p[ok]), 1)[0]
    return -1.0 / slope


def exp_fit_least_squares(r, p):
    """p(r) = A exp(-r/lambda) by least squares on the binned values (claims, reading (a))."""
    from scipy.optimize import curve_fit
    r, p = np.asarray(r, float), np.asarray(p, float)
    ok = np.isfinite(p)
    lam0 = abs(exp_length_constant_loglinear(r[ok], np.clip(p[ok], 1e-6, None)))
    popt, _ = curve_fit(lambda x, a, lam: a * np.exp(-x / lam), r[ok], p[ok],
                        p0=[p[ok].max() * 2, lam0], maxfev=20000)
    return popt[0], popt[1]


def bh_reject(p, alpha=0.05):
    p = np.asarray(p)
    order = np.argsort(p)
    ranked = p[order] * len(p) / (np.arange(len(p)) + 1)
    ok = np.zeros(len(p), bool)
    below = np.nonzero(ranked <= alpha)[0]
    if len(below):
        ok[order[:below.max() + 1]] = True
    return ok


# ------------------------------------------------------------------ behavior sessions
def load_behavior(mouse: str, cells="qc", subthreshold=True) -> dict:
    """Spontaneous-activity session: QC cells, their subthreshold voltage held in memory
    (frames x cells, float32, about 3 GB), spike frames, behaviour masks.

    Cells are the passed_qc cells, the axis of the stored correlation arrays (file description
    of /analysis/correlation_cell_index; claims header). Masks follow the code's Figure 4
    buildTimeMasks: running guard |speed| > 1e-3 dilated by +/-1000 frames, chunk-boundary guard
    +/-1000 frames, and the analysed window frames 5000 to round(2000/dt).
    """
    f = open_file(mouse, "behavior")
    u = units(mouse, "behavior")
    sel = np.nonzero(u["passed_qc"])[0] if cells == "qc" else np.arange(len(u["id"]))
    ts = f["processing/optical_voltage/subthreshold_voltage/timestamps"][:]
    n = len(ts)
    out = {"mouse": mouse, "cells": sel, "ts": ts, "n_frames": n,
           "x_um": u["x_um"][sel], "y_um": u["y_um"][sel], "gfp": u["gfp_positive"][sel]}
    out["spike_frames"] = [spike_frames(u["spike_times"][i], ts) for i in sel]
    b = "processing/behavior/behavioral_time_series"
    out["quiet"] = f[f"{b}/quiet_mask/data"][:, 0].astype(bool)
    out["whisk"] = f[f"{b}/whisking_mask/data"][:, 0].astype(bool)
    out["speed"] = f[f"{b}/running_speed/data"][:, 0]
    out["run_guard"] = running_guard(out["speed"])
    chunks = f["intervals/recording_chunks/start_time"][:]
    out["chunk_start_frames"] = np.searchsorted(ts, chunks)
    fpc = int(np.median(np.diff(out["chunk_start_frames"])))
    out["frames_per_chunk"] = fpc
    out["chunk_guard_1000"] = chunk_guard(n, fpc, 1000)
    base = np.zeros(n, bool)
    base[5000 - 1:int(round(2000 / DT))] = True
    out["base"] = base
    out["whisk_motion"] = f[f"{b}/whisking_motion/data"][:, 0]
    out["face_ts"] = f[f"{b}/whisking_motion/timestamps"][:]
    if "whisking_motion_reconstruction" in f[b]:
        out["whisk_rec"] = f[f"{b}/whisking_motion_reconstruction/data"][:]
    if subthreshold:
        d = f["processing/optical_voltage/subthreshold_voltage/data"]
        V = np.empty((n, len(sel)), np.float32)
        for a, x in iter_blocks(d, 100_000):
            V[a:a + len(x)] = x[:, sel]
        out["V"] = V
    return out


def spike_train_matrix(spike_frames_list, n_frames):
    """Boolean frames x cells spike matrix."""
    S = np.zeros((n_frames, len(spike_frames_list)), bool)
    for k, fr in enumerate(spike_frames_list):
        S[fr, k] = True
    return S


def p_spk_given_v(V, spike_frames_list, mask, edges, offset=0, window=0):
    """P(spk|V) per cell: histogram of V at spike frames over histogram of all V in the mask,
    divided by the 1.27 ms exposure (paper, Methods, P(spk|V); code Figure 4E-F). Spike frames
    are kept when the frame is in the mask; with ``offset`` the voltage is read ``offset``
    frames before the spike. With ``window`` > 0 the voltage of every frame, spike frames and
    all frames alike, is the mean over the ``window`` frames before it (the Results' and Fig. 4E
    legend's "10 ms interval before" reading, 8 frames = 10.2 ms)."""
    nb = len(edges) - 1
    allc = np.zeros((V.shape[1], nb))
    spkc = np.zeros((V.shape[1], nb))
    if window:
        mask = mask.copy()
        mask[:window] = False
    for k in range(V.shape[1]):
        if window:
            cs = np.concatenate([[0.0], np.cumsum(V[:, k], dtype=np.float64)])
            vk = np.full(V.shape[0], np.nan)
            vk[window:] = (cs[window:-1] - cs[:-window - 1]) / window  # frames t - window .. t - 1
            v = vk[mask]
            fr = spike_frames_list[k]
            fr = fr[mask[fr]]
            allc[k] = np.histogram(v, edges)[0]
            spkc[k] = np.histogram(vk[fr], edges)[0]
            continue
        v = V[mask, k]
        allc[k] = np.histogram(v, edges)[0]
        fr = spike_frames_list[k]
        fr = fr[mask[fr]]
        fr = fr[fr - offset >= 0] - offset
        spkc[k] = np.histogram(V[fr, k], edges)[0]
    with np.errstate(invalid="ignore", divide="ignore"):
        rate = spkc / allc / DT
    return rate, allc, spkc


def whisking_onsets(beh: dict):
    """Whisking onsets as in the code (reproduce_figure6_from_nwb.m, selectWhiskingOnsets,
    after Methods "lasso deconvolution"): for each of the 15 stored reconstructions, onsets
    are rises above 1e-3; the one whose onset-triggered whisking average has the smallest s.d.
    over the 2 s before onset is kept; it is put on the voltage clock and onsets closer than
    1.5 s to the previous one are dropped.

    The code lifts the reconstruction with a bilinear imresize over the whole session; here
    each face frame is mapped to the voltage frame nearest its timestamp, which places onsets
    within a face frame (25 ms) of the code's (a standard choice)."""
    rec, wm = beh["whisk_rec"], beh["whisk_motion"]
    nb, nf = int(round(2 / 25e-3)), int(round(3 / 25e-3))
    sds = []
    for j in range(rec.shape[1]):
        act = rec[:, j] > 1e-3
        on = np.nonzero(np.diff(act.astype(int)) > 0)[0] + 1
        on = on[(on >= nb) & (on < len(wm) - nf)]
        if len(on) == 0:
            sds.append(np.nan)
            continue
        avg = np.mean([wm[o - nb:o + nf + 1] for o in on], axis=0)
        s = np.std(avg[:nb], ddof=1)
        sds.append(s if s != 0 else np.nan)
    j = int(np.nanargmin(sds))
    act = rec[:, j] > 1e-3
    on = np.nonzero(np.diff(act.astype(int)) > 0)[0] + 1
    fr = spike_frames(beh["face_ts"][on], beh["ts"])
    keep = np.concatenate([[True], np.diff(fr) > 1.5 / DT])
    return fr[keep], j, np.array(sds)


# ------------------------------------------------------------------ Figure 4 stored correlations
def correlation_cells(mouse):
    f = open_file(mouse, "behavior")
    uid = f["analysis/correlation_cell_index/unit_id"][:].astype(int)
    u = units(mouse, "behavior")
    return uid, u["x_um"][uid], u["y_um"][uid], u["gfp_positive"][uid]


def fig4_stage2(mouse):
    """Distance-binned averages of the stored state-dependent correlation arrays, as the code's
    reproduce_figure4_from_nwb.m distanceBinnedCorrelations: 31 distance columns with edges
    [0 1 linspace(60,1800,30)] in pixels, column 2 (6.5 to 60 um) blanked; zero-lag summary
    vectors with column 1 (self pairs) blanked; synchrony = max over lags -1..1 minus the larger
    of the means over lags -5..-3 and 3..5. Also the quiet cross-STA depolarization: range of
    each pair's quiet STA over lags -100..-2, mean over pairs 60 to 400 um."""
    uid, x, y, _ = correlation_cells(mouse)
    D = distance_matrix_um(x, y) / PIXEL_UM
    edges = np.concatenate([[0, 1], np.linspace(60, 1800, 30)]) / PIXEL_UM
    centers_um = (edges[:-1] + edges[1:]) / 2 * PIXEL_UM
    nb = len(edges) - 1
    masks = [(D >= edges[i]) & (D < edges[i + 1]) for i in range(nb)]
    avg, extra = {}, {}
    for key, name in [("xcorrV", "voltage_cross_correlation"), ("staV", "spike_triggered_voltage"),
                      ("staRate", "spike_triggered_spike_rate")]:
        out = np.zeros((281, nb, 2))
        for s, state in enumerate(["quiet", "whisking"]):
            X = correlation_series(mouse, name, state)  # trigger x target x lag
            for i, mk in enumerate(masks):
                out[:, i, s] = np.nanmean(X[mk], axis=0) if mk.any() else np.nan
            if key == "staV" and state == "quiet":
                pm = (D > 60 / PIXEL_UM) & (D < 400 / PIXEL_UM)
                rng_ = np.ptp(X[:, :, 140 + np.arange(-100, -1)], axis=2)
                extra["cross_sta_depolarization"] = np.nanmean(rng_[pm])
                extra["staV_quiet"] = X
            del X
        avg[key] = out
    avg["staRate"][140, 0, :] = 0
    for k in avg:
        avg[k][:, 1, :] = np.nan
    def zl(a, lag=140):
        v = a[lag].T.copy()  # state x bin
        v[:, 0] = np.nan
        return v
    summ = {"xcorrV0": zl(avg["xcorrV"]), "staFR2": zl(avg["staRate"], 142)}
    peak = avg["staRate"][139:142].max(0)
    base = np.maximum(avg["staRate"][135:138].mean(0), avg["staRate"][143:146].mean(0))
    sync = (peak - base).T.copy()
    sync[:, 0] = np.nan
    summ["sync"] = sync
    return {"avg": avg, "summary": summ, "centers_um": centers_um, "D_pix": D, **extra,
            "unit_id": uid}


def fig4_statistics(st):
    """Per-session numbers of the code's reportedStatistics: short-range (bin 3, 60 to 120 um)
    zero-lag correlation; length constants 1/slope of polyfit(r, log value) over non-blank bins
    (synchrony restricted to centres < 800 um); quiet voltage FWHM (median over bins, half
    level between the edge of the lag window and the peak); whisking spike half-width in the
    60 to 120 um bin."""
    c = st["centers_um"]
    s = st["summary"]
    out = {"short_range": s["xcorrV0"][:, 2]}
    for key, src, mask_src, lim in [("lambda_V", "xcorrV0", "xcorrV0", np.inf),
                                    ("lambda_lag2", "staFR2", "sync", np.inf),
                                    ("lambda_sync", "sync", "sync", 800)]:
        lam = []
        for state in range(2):
            ok = ~np.isnan(s[mask_src][state]) & (c < lim)
            vals = s[src][state, ok]
            lam.append(1 / np.polyfit(c[ok], np.log(vals), 1)[0] if np.all(vals > 0) else np.nan)
        out[key] = np.array(lam)
    tr = st["avg"]["xcorrV"][:141, :, 0]
    hm = tr[0] + (tr[140] - tr[0]) / 2
    dev = np.abs(tr - hm)
    # MATLAB min() over an all-NaN column returns index 1; the code keeps that column
    half = np.where(np.all(np.isnan(dev), 0), 0, np.argmin(np.nan_to_num(dev, nan=np.inf), axis=0))
    out["fwhm_V_quiet_ms"] = np.median((140 - half) * DT * 2) * 1e3
    for state, nm in [(1, "spike_halfwidth_whisk_ms"), (0, "spike_halfwidth_quiet_ms")]:
        tr = st["avg"]["staRate"][:141, 2, state]
        hm = tr[0] + (tr[140] - tr[0]) / 2
        out[nm] = (140 - np.argmin(np.abs(tr - hm))) * DT * 1e3
    return out


# ------------------------------------------------------------------ crossed random-effects model
class CrossedLMM:
    """y = X b + Z_pre u + Z_post v + e, u ~ N(0, s_pre^2), v ~ N(0, s_post^2),
    e ~ N(0, s^2 / w): the model of the code's tutorial 5 (fitlme with (1|pre) + (1|post),
    'Weights' for the decay model), fitted here by profiled REML or ML on the two variance
    ratios. MATLAB's fitlme is not available; this is the same likelihood, written out with the
    sparse structure of the two crossed factors (a standard implementation)."""

    def __init__(self, y, X, pre, post, w=None):
        from scipy import sparse
        self.y, self.X = np.asarray(y, float), np.asarray(X, float)
        self.n, self.p = self.X.shape
        self.w = np.ones(self.n) if w is None else np.asarray(w, float)
        sw = np.sqrt(self.w)
        _, ip = np.unique(pre, return_inverse=True)
        _, jq = np.unique(post, return_inverse=True)
        self.ip, self.jq = ip, jq
        self.n1, self.n2 = ip.max() + 1, jq.max() + 1
        self.Z1 = sparse.csr_matrix((sw, (np.arange(self.n), ip)), shape=(self.n, self.n1))
        self.Z2 = sparse.csr_matrix((sw, (np.arange(self.n), jq)), shape=(self.n, self.n2))
        self.D1 = np.asarray(self.Z1.multiply(self.Z1).sum(0)).ravel()
        self.D2 = np.asarray(self.Z2.multiply(self.Z2).sum(0)).ravel()
        self.B = (self.Z1.T @ self.Z2).tocsr()
        self.Xt = self.X * sw[:, None]

    def _parts(self, lg, yt):
        from scipy.linalg import cho_factor, cho_solve
        g1, g2 = np.exp(lg)
        e2 = self.D2 + 1 / g2
        BE = self.B.multiply(1 / e2[None, :]).tocsr()
        S = np.diag(self.D1 + 1 / g1) - (BE @ self.B.T).toarray()
        cf = cho_factor(S, lower=True)
        logdetC = np.sum(np.log(e2)) + 2 * np.sum(np.log(np.diag(cf[0])))
        logdetV = self.n1 * np.log(g1) + self.n2 * np.log(g2) + logdetC

        def vinv(M):  # V^{-1} M in units of s^2, for M (n x k) in transformed space
            b1 = self.Z1.T @ M
            b2 = self.Z2.T @ M
            x1 = cho_solve(cf, b1 - BE @ b2)
            x2 = (b2 - self.B.T @ x1) / e2[:, None]
            return M - self.Z1 @ x1 - self.Z2 @ x2

        A = np.column_stack([self.Xt, yt])
        VA = vinv(A)
        XVX = self.Xt.T @ VA[:, :self.p]
        XVy = self.Xt.T @ VA[:, self.p]
        yVy = yt @ VA[:, self.p]
        beta = np.linalg.solve(XVX, XVy)
        r = yVy - beta @ XVy
        return logdetV, XVX, beta, r

    def objective(self, lg, yt, reml=True):
        logdetV, XVX, beta, r = self._parts(lg, yt)
        if reml:
            dof = self.n - self.p
            return dof * np.log(r / dof) + logdetV + np.linalg.slogdet(XVX)[1]
        return self.n * np.log(r / self.n) + logdetV

    def fit(self, y=None, reml=True, start=None):
        """Fit by L-BFGS-B over the log variance ratios. Without ``start`` the search starts
        from the best point of a 6 x 6 grid of log ratios (-8 to 2), since the likelihood can
        have more than one local optimum (the bootstrap starts from the point estimate)."""
        from scipy.optimize import minimize
        y = self.y if y is None else y
        yt = y * np.sqrt(self.w)
        if start is None:
            grid = [(a, b) for a in np.linspace(-8, 2, 6) for b in np.linspace(-8, 2, 6)]
            start = min(grid, key=lambda g: self.objective(np.array(g), yt, reml))
        res = minimize(lambda lg: self.objective(lg, yt, reml), np.asarray(start, float),
                       method="L-BFGS-B", bounds=[(-12, 6), (-12, 6)])
        logdetV, XVX, beta, r = self._parts(res.x, yt)
        s2 = r / ((self.n - self.p) if reml else self.n)
        g1, g2 = np.exp(res.x)
        out = {"beta": beta, "s2_resid": s2, "s2_pre": g1 * s2, "s2_post": g2 * s2,
               "lg": res.x, "converged": bool(res.success)}
        if not reml:
            n = self.n
            ll = -0.5 * (n * np.log(2 * np.pi) + n * np.log(r / n) + logdetV + n
                         - np.sum(np.log(self.w)))
            out["loglik"] = ll
            out["aic"] = -2 * ll + 2 * (self.p + 3)
        return out

    def simulate(self, fit, rng):
        u = rng.normal(0, np.sqrt(fit["s2_pre"]), self.n1)
        v = rng.normal(0, np.sqrt(fit["s2_post"]), self.n2)
        e = rng.normal(0, 1, self.n) * np.sqrt(fit["s2_resid"] / self.w)
        return self.X @ fit["beta"] + u[self.ip] + v[self.jq] + e


def bootstrap_variances(model, fit, n_boot, seed):
    """Parametric bootstrap of the variance components (code, bootstrapVarianceComponents.m:
    simulate from the fitted model, refit by REML, n_boot times). Returns rows of
    (s2_pre, s2_post, s2_resid, converged, s2_pre2, s2_post2, converged2), where the last three
    come from a second refit of the same simulated data started from the grid search, made
    only when the first did not report convergence (NaN otherwise)."""
    rng = np.random.default_rng(seed)
    out = []
    for _ in range(n_boot):
        ys = model.simulate(fit, rng)
        f = model.fit(ys, reml=True, start=fit["lg"])
        row = [f["s2_pre"], f["s2_post"], f["s2_resid"], f["converged"], np.nan, np.nan, np.nan]
        if not f["converged"]:
            g = model.fit(ys, reml=True)
            row[4:] = [g["s2_pre"], g["s2_post"], g["converged"]]
        out.append(row)
    return np.array(out, dtype=float)


# ------------------------------------------------------------------ sparseOpto pass (Figure 5A-C)
def imresize_bilinear_1d(x, n_out):
    """MATLAB imresize(x, [n_out 1], 'bilinear') for enlargement of a 1-D signal."""
    n_in = len(x)
    pos = (np.arange(n_out) + 0.5) * n_in / n_out - 0.5
    return np.interp(pos, np.arange(n_in), x)


def median_quiet_mask(whisk_motion, n_chunks, frames_per_chunk):
    """The code's median-rule quiet mask (reproduce_figure5_from_nwb.m medianQuietMask): 8-sample
    moving median of the whisking trace, lifted to the voltage clock chunk by chunk, quiet where
    a 100-frame moving mean of (trace > median) is 0."""
    from scipy.ndimage import median_filter, uniform_filter1d
    sm = median_filter(np.asarray(whisk_motion, float), size=8, mode="nearest")
    per = len(sm) // n_chunks
    lifted = np.concatenate([imresize_bilinear_1d(sm[k * per:(k + 1) * per], frames_per_chunk)
                             for k in range(n_chunks)])
    above = (lifted > np.median(lifted)).astype(float)
    return ~(uniform_filter1d(above, 100, mode="nearest") > 0)


def opto_pass(mouse, block_chunks=40):
    """One streaming pass over a sparseOpto session for Figure 5A-C (code,
    reproduce_figure5_from_nwb.m accumulateOptoStatistics), for all 320 cells:

    - spontaneous P(spk|V): frames 5000 to 2e6 outside +/-100 frames of a chunk boundary, stored
      quiet mask, no running, in chunks where no QC cell within 80 um (itself included) received
      blue; no-blue spike times; V bins linspace(-1, 1.5, 51);
    - evoked P(spk|V) on the first half of the ramp: blue rising by less than the smallest step
      and below half the largest step; spikes with blue on;
    - joint (V, dV/dt) counts with the code's dV/dt (8-frame centred difference shifted by 4
      frames), median-rule quiet, frames 5000 to 2000 s, +/-140 frame guard, no running; V bins
      linspace(-1, 1.5, 11), dV/dt bins linspace(-0.5, 1, 51); and the Methods' variant (dV/dt
      shifted 6 ms = 5 frames, V between 0.2 and 0.8, stored quiet mask);
    - spontaneous spike frames for the autocorrelogram triggers (quiet, and any state).
    """
    f = open_file(mouse, "sparseOpto")
    u = units(mouse, "sparseOpto")
    ts = f["processing/optical_voltage/subthreshold_voltage/timestamps"][:]
    n = len(ts)
    nchunk = len(f["intervals/recording_chunks/start_time"])
    fpc = n // nchunk
    b = "processing/behavior/behavioral_time_series"
    quiet = f[f"{b}/quiet_mask/data"][:, 0].astype(bool)
    run = running_guard(f[f"{b}/running_speed/data"][:, 0])
    mq = median_quiet_mask(f[f"{b}/whisking_motion/data"][:, 0], nchunk, fpc)
    maskA = np.zeros(n, bool); maskA[5000 - 1:int(2e6)] = True
    maskA &= ~chunk_guard(n, fpc, 100)
    base_any = maskA.copy()
    maskA &= quiet & ~run
    maskB = np.zeros(n, bool); maskB[5000 - 1:int(round(2000 / DT))] = True
    maskB &= ~chunk_guard(n, fpc, 140) & ~run
    maskBm = maskB & quiet       # Methods variant, stored quiet mask
    maskB &= mq
    sf = [spike_frames(x, ts) for x in u["spike_times"]]
    snb = [spike_frames(x, ts) for x in u["spike_times_no_blue"]]
    D = distance_matrix_um(u["x_um"], u["y_um"])
    pool = u["passed_qc"][None, :] | np.eye(320, dtype=bool)
    neigh = (D < 80) & pool
    vE = np.linspace(-1, 1.5, 51); vEj = np.linspace(-1, 1.5, 11); dE = np.linspace(-0.5, 1, 51)
    out = {k: np.zeros((320, 50)) for k in ("spont_all", "spont_spk", "ramp_all", "ramp_spk")}
    out["joint_all"] = np.zeros((320, 10, 50)); out["joint_spk"] = np.zeros((320, 10, 50))
    out["jm_all"] = np.zeros((320, 50)); out["jm_spk"] = np.zeros((320, 50))
    quiet_spikes = [[] for _ in range(320)]
    any_spikes = [[] for _ in range(320)]
    dblue = f["stimulus/presentation/blue_stimulation_per_cell/data"]
    dv = f["processing/optical_voltage/subthreshold_voltage/data"]
    # step levels from the first QC cell's held blue values in the first 20 chunks (code)
    c0 = int(np.nonzero(u["passed_qc"])[0][0])
    bl0 = dblue[:20 * fpc, c0]
    held = np.concatenate([[True], np.diff(bl0) == 0])
    levels = np.unique(bl0[(bl0 > 0) & held])
    small, large = levels.min(), levels.max()
    out["levels"] = levels
    halo = 8
    for c_start in range(0, nchunk, block_chunks):
        c_end = min(nchunk, c_start + block_chunks)
        a, e = c_start * fpc, c_end * fpc
        ha, he = max(0, a - halo), min(n, e + halo)
        Vh = dv[ha:he].astype(np.float64)
        Bh = dblue[ha:he].astype(np.float64)
        dvdt = np.zeros_like(Vh)
        dvdt[4:-4] = Vh[8:] - Vh[:-8]
        core = slice(a - ha, a - ha + (e - a))
        dv4 = np.roll(dvdt, 4, axis=0)[core]
        dv5 = np.roll(dvdt, 5, axis=0)[core]
        V = Vh[core]; Bl = Bh[core]
        bdiff = np.diff(Bh, axis=0, prepend=Bh[:1])[core]
        had = (Bl.reshape(c_end - c_start, fpc, 320) > 0).any(1)  # chunk x cell
        mA, mB, mBm, ba = maskA[a:e], maskB[a:e], maskBm[a:e], base_any[a:e]
        for c in range(320):
            usable = ~had[:, neigh[c]].any(1)
            us = np.repeat(usable, fpc)
            cm = mA & us
            v = V[:, c]
            out["spont_all"][c] += np.histogram(v[cm], vE)[0]
            s_nb = snb[c]; s_nb = s_nb[(s_nb >= a) & (s_nb < e)] - a
            s_q = s_nb[cm[s_nb]]
            out["spont_spk"][c] += np.histogram(v[s_q], vE)[0]
            quiet_spikes[c].append(s_q + a)
            any_spikes[c].append(s_nb[(ba & us)[s_nb]] + a)
            rm = (bdiff[:, c] > 0) & (bdiff[:, c] < small) & (Bl[:, c] < 0.5 * large)
            out["ramp_all"][c] += np.histogram(v[rm], vE)[0]
            s_a = sf[c]; s_a = s_a[(s_a >= a) & (s_a < e)] - a
            s_r = s_a[rm[s_a] & (Bl[s_a, c] > 0)]
            out["ramp_spk"][c] += np.histogram(v[s_r], vE)[0]
            out["joint_all"][c] += np.histogram2d(v[mB], dv4[mB, c], [vEj, dE])[0]
            s_b = s_nb[mB[s_nb]]
            out["joint_spk"][c] += np.histogram2d(v[s_b], dv4[s_b, c], [vEj, dE])[0]
            inw = mBm & (v >= 0.2) & (v <= 0.8)
            out["jm_all"][c] += np.histogram(dv5[inw, c], dE)[0]
            s_m = s_nb[inw[s_nb]]
            out["jm_spk"][c] += np.histogram(dv5[s_m, c], dE)[0]
        del Vh, Bh, dvdt, V, Bl, bdiff, dv4, dv5
    out["quiet_spikes"] = [np.concatenate(x) for x in quiet_spikes]
    out["any_spikes"] = [np.concatenate(x) for x in any_spikes]
    out["no_blue_spikes"] = snb
    out["n_frames"] = n
    out["median_vs_stored_quiet_agreement"] = float(np.mean(mq == quiet))
    return out


def self_correlogram(trigger, target, n_frames, n_back=140, n_front=140):
    """Mean of the target spike train in windows around each trigger (code, selfCorrelogram)."""
    trigger = trigger[(trigger >= n_back) & (trigger < n_frames - n_front)]
    if len(trigger) == 0 or len(target) == 0:
        return np.zeros(n_back + n_front + 1)
    tgt = np.sort(target)
    lags = np.arange(-n_back, n_front + 1)
    counts = np.array([np.sum(np.isin(trigger + l, tgt, assume_unique=False)) for l in lags])
    return counts / len(trigger)


def pair_sets(mouse):
    """Pairwise matrices of a sparsePulseHad session with the QC selection: (matrices, QC flags,
    ordered pairs of distinct QC cells, distance in um, {"within 400 um", "60 to 400 um"} masks).
    Tested pairs are ordered pairs of distinct QC cells within 400 um (claims file); the 60 to
    400 um band is the code's (loadFigure5SessionFromNWB.m) and the Results' exclusion of pairs
    under 60 um."""
    M = pair_matrices(mouse)
    q = units(mouse, "sparsePulseHad")["passed_qc"]
    QQ = q[:, None] & q[None, :] & ~np.eye(len(q), dtype=bool)
    D = M["distance_um"]
    return M, q, QQ, D, {"within 400 um": QQ & (D <= 400), "60 to 400 um": QQ & (D > 60) & (D < 400)}


def matlab_prctile(x, p):
    """MATLAB prctile (midpoint interpolation), used where the code takes percentiles."""
    x = np.sort(np.asarray(x, float)[np.isfinite(x)])
    n = len(x)
    pos = np.clip(n * p / 100 + 0.5, 1, n)
    lo = int(np.floor(pos))
    hi = min(lo + 1, n)
    return x[lo - 1] + (pos - lo) * (x[hi - 1] - x[lo - 1])


# ------------------------------------------------------------------ wave propagation (Supplementary Fig. 21)
def wave_events(V, x_um, y_um, quiet, whisk, segment="extrema"):
    """Wave propagation events (paper, Methods, Wave propagation analysis): peaks of the first
    derivative of the population-average subthreshold voltage above 3.5 times its s.d. over the
    whisking frames, in quiet frames. ``quiet`` and ``whisk`` are the frames analysed in each state.

    The Methods leave open the parts that set the count and the speed, so each is a reading
    (assumption, the notebook runs them all): the derivative is the centred difference of the
    population average, which is already smooth (the stored subthreshold voltage is smoothed);
    each event spans the voltage minimum and maximum flanking the peak, read as ``"extrema"``, the
    adjacent turning points of the average (the run of positive derivative holding the peak), or
    ``"window"``, the minimum in the 250 ms before and the maximum in the 250 ms after the peak.
    Events are counted per derivative peak and per distinct span (peaks sharing a span merged).

    Returns the threshold and a list of events (peak frame, first and last frame of the span)."""
    from scipy.signal import find_peaks
    pop = V.mean(1, dtype=np.float64)
    d = np.gradient(pop)
    thr = 3.5 * np.std(d[whisk])
    pk, _ = find_peaks(d, height=thr)
    pk = pk[quiet[pk]]
    n = len(pop)
    w = int(round(0.25 / DT))
    pos = d > 0
    ev = []
    for p in pk:
        if segment == "extrema":
            lo = p
            while lo > 0 and pos[lo - 1]:
                lo -= 1
            hi = p
            while hi < n - 1 and pos[hi + 1]:
                hi += 1
        else:
            a, b = max(0, p - w), min(n, p + w + 1)
            lo = a + int(np.argmin(pop[a:p + 1]))
            hi = p + int(np.argmax(pop[p:b]))
        if quiet[lo:hi + 1].all():
            ev.append((p, lo, hi))
    return thr, ev


def event_lags(X):
    """Lag (frames, signed: positive when the second cell lags the first) of the maximum of the
    cross-correlation of every pair of columns of an event snippet X (frames x cells), over all
    lags the snippet allows (Methods: "the lag-time with the maximum correlation for each pair")."""
    X = X - X.mean(0)
    L_ = X.shape[0]
    nf = 2 * L_
    F = np.fft.rfft(X, nf, axis=0)
    nc = X.shape[1]
    lag = np.zeros((nc, nc))
    lags = np.r_[np.arange(0, L_), np.arange(-L_ + 1, 0)]
    idx = np.r_[np.arange(0, L_), np.arange(nf - L_ + 1, nf)]
    for i in range(nc):
        cc = np.fft.irfft(np.conj(F[:, i:i + 1]) * F, nf, axis=0)[idx]
        lag[i] = lags[np.argmax(cc, axis=0)]
    return lag


def wave_speed(lag, x_um, y_um):
    """Speeds of one event from its pair lags (frames) and the cell positions: (a) distance
    regressed on absolute lag, (b) absolute lag regressed on distance, inverted (the claims file's
    two readings of "the slope of the line relating lag-time to separation"), and (c) a plane-wave
    fit of signed lag on the displacement vector, which also gives a direction (a variant). Speeds
    in mm/s, direction in radians in the image frame (x, y of the units table)."""
    iu = np.triu_indices(len(x_um), 1)
    dx = (x_um[None, :] - x_um[:, None])[iu]
    dy = (y_um[None, :] - y_um[:, None])[iu]
    dist = np.hypot(dx, dy)
    tl = lag[iu] * DT  # s
    at = np.abs(tl)
    out = {}
    if np.ptp(at) > 0:
        out["a"] = np.polyfit(at, dist, 1)[0] * 1e-3  # um/s -> mm/s
        sl = np.polyfit(dist, at, 1)[0]
        out["b"] = (1 / sl) * 1e-3 if sl > 0 else np.nan
    else:
        out["a"] = out["b"] = np.nan
    s, *_ = np.linalg.lstsq(np.column_stack([dx, dy]), tl, rcond=None)
    ns = np.hypot(*s)
    out["c"] = (1 / ns) * 1e-3 if ns > 0 else np.nan
    out["c_dir"] = np.arctan2(s[1], s[0])
    return out


def phase_direction(Z, x_um, y_um, grid_um=160.0, fwhm_um=325.0):
    """Propagation direction of one event from the phase gradient (Methods, Wave propagation
    analysis): Z is the analytic (Hilbert) signal of each cell averaged over the event (cells),
    smoothed with a Gaussian of 325 um full width at half maximum (assumption: "325 um wide" read as
    the FWHM) onto a 160 um grid; the flow field is the phase gradient, and the wave travels down
    it. Returns the circular mean direction (radians, image frame) of the flow vectors."""
    sig = fwhm_um / 2.355
    gx = np.arange(x_um.min(), x_um.max() + grid_um, grid_um)
    gy = np.arange(y_um.min(), y_um.max() + grid_um, grid_um)
    GX, GY = np.meshgrid(gx, gy)
    w = np.exp(-((GX[..., None] - x_um) ** 2 + (GY[..., None] - y_um) ** 2) / (2 * sig ** 2))
    Zg = (w * Z).sum(-1) / w.sum(-1)
    dzy, dzx = np.gradient(Zg, grid_um)
    a2 = np.abs(Zg) ** 2
    phx = np.imag(np.conj(Zg) * dzx) / a2
    phy = np.imag(np.conj(Zg) * dzy) / a2
    u = -(phx + 1j * phy)
    u = u[np.isfinite(u) & (np.abs(u) > 0)]
    return float(np.angle(np.mean(u / np.abs(u))))


# ------------------------------------------------------------------ per-pulse responses (Supplementary Fig. 16)
PULSE_FRAMES = 16  # 20 ms blue pulses (Methods; 16 frames in blue_stimulation_per_cell, data check)


def pulse_responses(mouse, resp_window=(16, 48), base_window=(-20, 0), spike_window=(0, 20)):
    """One row per 20 ms blue pulse of the sparse_pulse_synaptic_mapping trials of a
    sparsePulseHad session, for the lasso correction of off-target spiking (paper, Methods,
    Analysis for mapping synaptic connections, paragraph 3; Supplementary Fig. 16).

    Pulses are the rising edges of ``blue_stimulation_per_cell``; the cells lit at an onset are its
    targets. Per pulse and cell: the response, mean normalized voltage over frames
    ``resp_window`` after onset (20 to 60 ms, around the IPSP peak of about 30 ms and its decay,
    Results and Fig. 3F; assumption) minus the mean over ``base_window`` (the 25 ms before onset);
    and the evoked spikes, spikes in frames ``spike_window`` (the pulse and 5 ms after) minus spikes
    in the 20 frames before onset (a standard choice). Returns onset frames, the target mask
    (pulses x cells), responses and evoked spike counts (pulses x cells, float32)."""
    f = open_file(mouse, "sparsePulseHad")
    ts = series_timestamps(mouse, "sparsePulseHad")
    tt = f["intervals/trials/trial_type"][:]
    st = np.searchsorted(ts, f["intervals/trials/start_time"][:])
    sp = np.searchsorted(ts, f["intervals/trials/stop_time"][:], side="right")
    pulse_trial = np.zeros(len(ts), bool)
    for t in np.nonzero(tt == b"sparse_pulse_synaptic_mapping")[0]:
        pulse_trial[st[t]:sp[t]] = True
    u = units(mouse, "sparsePulseHad")
    sfr = [np.sort(spike_frames(x, ts)) for x in u["spike_times"]]
    blue = f["stimulus/presentation/blue_stimulation_per_cell/data"]
    volt = f["processing/optical_voltage/normalized_voltage/data"]
    n = len(ts)
    pad_lo, pad_hi = -min(base_window[0], -20), max(resp_window[1], spike_window[1])
    onsets, targets, resp = [], [], []
    block = 100_000
    for a in range(0, n, block):
        b = min(n, a + block)
        a0, b0 = max(0, a - pad_lo - 1), min(n, b + pad_hi)
        x = blue[a0:b0] > 0
        rise = x[1:] & ~x[:-1]
        on_rows = np.nonzero(rise.any(1))[0] + 1 + a0
        on_rows = on_rows[(on_rows >= a) & (on_rows < b) & (on_rows - pad_lo >= 0) & (on_rows + pad_hi <= n)]
        on_rows = on_rows[pulse_trial[on_rows]]
        if len(on_rows) == 0:
            continue
        V = volt[a0:b0]
        for o in on_rows:
            k = o - a0
            onsets.append(o)
            targets.append(rise[k - 1])
            r_ = V[k + resp_window[0]:k + resp_window[1]].mean(0) - V[k + base_window[0]:k + base_window[1]].mean(0)
            resp.append(r_.astype(np.float32))
    onsets = np.array(onsets)
    evoked = np.zeros((len(onsets), len(sfr)), np.float32)
    for c, fr in enumerate(sfr):
        inn = np.searchsorted(fr, onsets + spike_window[1]) - np.searchsorted(fr, onsets + spike_window[0])
        pre = np.searchsorted(fr, onsets) - np.searchsorted(fr, onsets - (spike_window[1] - spike_window[0]))
        evoked[:, c] = inn - pre
    return onsets, np.array(targets), np.array(resp), evoked


def lasso_correction(targets, resp, evoked, dist_um, spikes_per_pulse, offtarget_um=100.0, seed=0):
    """Off-target correction of the IPSP matrix (paper, Methods, Analysis for mapping synaptic
    connections, paragraph 3; Supplementary Fig. 16A: R = S W, W by lasso).

    For each postsynaptic cell j, over the pulses that do not target j: the response of j is
    regressed on the spikes each candidate presynaptic cell k (within 400 um of j, k != j) fired
    in the pulse, with an intercept (the blue-flash response, which the Methods subtract as the
    mean response to faraway stimulation). Spikes of a targeted cell are its stored
    ``estimated_spikes_per_blue_pulse`` (Methods: the evoked count of bursting cells is estimated
    from the spectrum); spikes of a non-targeted cell are its detected evoked spikes when it lies
    within ``offtarget_um`` of a target (4 off-target firing length constants of 25 um, Results),
    and zero elsewhere (assumption: detected counts far from any target are spontaneous noise).
    Penalty by 10-fold cross-validation (scikit-learn LassoCV, 40 penalties, unstandardized
    predictors): (a) the penalty of least error, (b) the largest within one standard error of it
    (the claims file's readings); ordinary least squares is shown as a variant.

    The raw matrix ("assuming only on-target stimulation") is the mean response of j over pulses
    targeting i, minus its mean over pulses with no target within 400 um of j, divided by the spikes
    per pulse of i. All matrices are [pre, post] in SH per presynaptic spike."""
    from sklearn.linear_model import Lasso, LassoCV, LinearRegression
    T = np.asarray(targets, bool)
    n_cells = T.shape[1]
    Tf = T.astype(float)
    off = ((Tf @ (dist_um <= offtarget_um).astype(float)) > 0) & ~T
    S = np.where(T, spikes_per_pulse[None, :], np.where(off, evoked, 0.0)).astype(float)
    near400 = (Tf @ (dist_um <= 400).astype(float)) > 0
    raw, wa, wb, wo = (np.full((n_cells, n_cells), np.nan) for _ in range(4))
    alphas = np.zeros((n_cells, 2))
    for j in range(n_cells):
        cand = np.nonzero((dist_um[:, j] <= 400) & (np.arange(n_cells) != j))[0]
        rows = ~T[:, j]
        y = resp[rows, j].astype(float)
        art = resp[~near400[:, j], j].mean()
        for i in cand:
            raw[i, j] = (resp[T[:, i] & rows, j].mean() - art) / spikes_per_pulse[i]
        X = S[rows][:, cand]
        cv = LassoCV(cv=10, alphas=40, fit_intercept=True, random_state=seed).fit(X, y)
        mse = cv.mse_path_.mean(1)
        se = cv.mse_path_.std(1) / np.sqrt(cv.mse_path_.shape[1])
        k = int(np.argmin(mse))
        a1 = cv.alphas_[np.nonzero(mse <= mse[k] + se[k])[0][0]]  # alphas_ run from large to small
        wa[cand, j] = cv.coef_
        wb[cand, j] = Lasso(alpha=a1, fit_intercept=True).fit(X, y).coef_
        wo[cand, j] = LinearRegression().fit(X, y).coef_
        alphas[j] = cv.alpha_, a1
    return dict(raw=raw, cv_min=wa, one_se=wb, ols=wo, alphas=alphas, offtarget=off, S=S)


# ------------------------------------------------------------------ scattered fluorescence (Supplementary Fig. 17)
def scatter_sta(mouse="M-YQ0201-29", n_frames=32_000, start=0, bin_px=4, block=1600):
    """Cross-STA fluorescence of interstitial pixels in the raw-movie excerpt (paper, Methods,
    Analysis for mapping gap junction connections, paragraph 4), on a subset of frames.

    The movie is read for frames ``start`` to ``start + n_frames`` (a subset: the whole excerpt is
    1,152,000 frames) and averaged in ``bin_px`` x ``bin_px`` pixel bins (26 um; a computational
    choice, the scatter varies over tens of um). Interstitial bins are those holding no pixel of
    any cell's footprint (``image_mask`` > 0; Supplementary Fig. 17A: "Regions containing other
    cells were excluded"). For each cell (trigger), the STA of every interstitial bin over lags -6
    to 6 frames, and the STA of the trigger's own footprint (mask-weighted mean of its pixels).
    The STA fluorescence is normalized by the trigger's spike fluorescence, frame 0 minus frame
    -2 of its own STA, and the scatter amplitude is extracted as a spikelet: the mean of frames
    {0, 1} minus the mean of frames {-4, -3, -2, 4, 5, 6} (Methods). Returns per trigger cell and
    interstitial bin the normalized scatter amplitude, the distance (um), and spike counts."""
    from scipy import sparse
    f = open_file(mouse, "behavior-rawexcerpt")
    mov = f["acquisition/raw_voltage_movie/data"]
    ts = f["acquisition/raw_voltage_movie/timestamps"][:]
    H, Wd = mov.shape[1:]
    masks = f["processing/ophys/ImageSegmentation/plane_segmentation/image_mask"][:]
    u = units(mouse, "behavior-rawexcerpt")
    n_cells = masks.shape[0]
    hb, wb = H // bin_px, Wd // bin_px
    cellpix = (masks > 0).any(0)[:hb * bin_px, :wb * bin_px]
    inter = ~cellpix.reshape(hb, bin_px, wb, bin_px).any((1, 3)).ravel()
    gy, gx = np.meshgrid((np.arange(hb) + 0.5) * bin_px - 0.5, (np.arange(wb) + 0.5) * bin_px - 0.5, indexing="ij")
    gx, gy = gx.ravel()[inter], gy.ravel()[inter]
    dist = np.hypot(u["x_pixel"][:, None] - gx[None, :], u["y_pixel"][:, None] - gy[None, :]) * PIXEL_UM
    Mw = sparse.csr_matrix(masks.reshape(n_cells, -1).astype(np.float64))
    Mw = sparse.diags(1 / np.asarray(Mw.sum(1)).ravel()) @ Mw
    lags = np.arange(-6, 7)
    stop = start + n_frames
    sfr = [spike_frames(x, ts) for x in u["spike_times"]]
    sfr = [s_[(s_ >= start + 6) & (s_ < stop - 6)] for s_ in sfr]
    sta_pix = np.zeros((n_cells, len(lags), inter.sum()))
    sta_own = np.zeros((n_cells, len(lags)))
    for a in range(start, stop, block):
        a0, b0 = max(start, a - 6), min(stop, a + block + 6)
        X = mov[a0:b0].astype(np.float32)
        own = (Mw @ X.reshape(len(X), -1).T.astype(np.float64)).T  # frames x cells
        Xb = X[:, :hb * bin_px, :wb * bin_px].reshape(len(X), hb, bin_px, wb, bin_px).mean((2, 4)).reshape(len(X), -1)[:, inter]
        for k, l in enumerate(lags):
            rows, cols = [], []
            for c, s_ in enumerate(sfr):
                s_ = s_[(s_ >= a) & (s_ < min(a + block, stop))]
                rows.append(np.full(len(s_), c)); cols.append(s_ + l - a0)
            rows, cols = np.concatenate(rows), np.concatenate(cols)
            P = sparse.csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(n_cells, len(X)))
            sta_pix[:, k] += P @ Xb
            sta_own[:, k] += np.asarray(P.multiply(own.T).sum(1)).ravel()
    n_spk = np.array([len(s_) for s_ in sfr])
    with np.errstate(invalid="ignore", divide="ignore"):
        sta_pix /= n_spk[:, None, None]
        sta_own /= n_spk[:, None]
    z = 6
    spike_f = sta_own[:, z] - sta_own[:, z - 2]
    ext = lambda S: S[:, [z, z + 1]].mean(1) - S[:, [z - 4, z - 3, z - 2, z + 4, z + 5, z + 6]].mean(1)
    amp = ext(sta_pix) / spike_f[:, None]
    return dict(amp=amp, dist=dist, n_spikes=n_spk, spike_f=spike_f, own_sta=sta_own, n_bins=int(inter.sum()),
                qc=u["passed_qc"])
