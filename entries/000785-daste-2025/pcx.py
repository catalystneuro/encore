"""Loading and measures for dandiset 000785 (Daste, Pierre et al., piriform projection neurons).

Where each parameter comes from:

- Normalized fluorescence is the paper code's "percdFF" (config/preprocess.yml and
  src/nwb_processor.py of https://gitlab.com/fleischmann-lab/calcium-imaging/projection-difference
  at commit f478b34c79606c3109f259d24add0256fb0b3b67, as the claims file reads it): F with no
  neuropil subtraction (k_neu 0), median filter over 1 s, F0 the running 10th percentile over
  30 s, then (F - F0) / std(F - F0) over the session, per cell. Filter widths in frames are
  2 * round(Fs * tau / 2) + 1 with Fs from the plane's timestamps, as in
  norm_F_matrix_running_percentile.
- Cells are suite2p cells (iscell[:, 0]); red cells are is_redcell_finalized. A plane with no
  red cell is skipped entirely, as compute_dFF0 does ("a plane w/o any red cell tends to have
  issues, such as duplicated planes").
- Trials are cut around odor onset (stim_onset_timestamp located on plane-0 timestamps, all
  planes taking the same frame index, as split_by_trial uses plane-0 times for every plane).
- Binarization (Methods, "Determination of odor-responsive (active) neurons"): 1000 baseline
  points from the 4 s before onset across all trials; a one-sided Mann-Whitney U test of each
  0.7 s window against them; forward-active when p < 0.01 for at least 8 consecutive forward
  frames; backward-active when p < 0.01 for any of 4 backward frames; active when
  forward-active and, for windows starting at onset, not backward-active. How the windows sit
  on the frames is open (claims file header): reading "start" puts each window at its frame and
  extending 0.7 s forward (backward windows ending at each of the 4 frames before onset);
  reading "centre" centres each window on its frame. The p-value is exact for windows of fewer
  than 8 frames and the normal approximation with continuity correction otherwise, which is what
  scipy.stats.mannwhitneyu does by default (a standard choice). The 1000-point sample is drawn
  without replacement with a fixed seed (a standard choice).
- Lifetime and population sparseness follow Vinje and Gallant (2000) and mutual information is
  computed from empirical frequencies in bits (claims file header; the paper's formulas are lost
  from the text).
- Pseudo-populations (Methods, "Pseudo-population construction"): bad and control trials
  removed, trials matched across mice by stimulus and by order of presentation of that stimulus,
  truncated to the smallest count across mice (claims file header).
- Decoders are sklearn.svm.SVC(kernel='linear') with default parameters (Methods, "Decoding
  analysis": "a linear SVM with all default parameters as given by sklearn"; the code's demo
  uses SVC), 5-fold stratified cross-validation with shuffling seeded per repeat (the fold
  shuffle is a standard choice).
"""
from __future__ import annotations

import functools
import os
import warnings

import h5py
import numpy as np
import pandas as pd
import remfile
import requests
from scipy import ndimage, stats

DANDISET = "000785"
VERSION = "0.260520.1603"
API = "https://api.dandiarchive.org/api"

PRE_S = 5.0     # seconds kept before odor onset
POST_S = 15.0   # seconds kept after odor onset


# ----------------------------------------------------------------------------- archive

@functools.lru_cache(None)
def assets() -> pd.DataFrame:
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=200"
    rows = []
    while url:
        d = requests.get(url, timeout=60).json()
        rows += d["results"]
        url = d.get("next")
    df = pd.DataFrame(rows)[["asset_id", "path", "size"]]
    df["subject"] = df.path.str.extract(r"sub-(\d+)/")[0]
    df["session"] = df.path.str.extract(r"ses-(\w+?)_ophys")[0]
    return df.sort_values("path").reset_index(drop=True)


def s3_url(asset_id: str) -> str:
    r = requests.head(f"{API}/assets/{asset_id}/download/", allow_redirects=True, timeout=60)
    return r.url


def open_h5(asset_id: str) -> h5py.File:
    return h5py.File(remfile.File(s3_url(asset_id)), "r")


def _s(x):
    x = x[()] if hasattr(x, "shape") and getattr(x, "shape", None) == () else x
    return x.decode() if isinstance(x, bytes) else x


def _col(g, name):
    """Read a (possibly ragged) column of a DynamicTable as a list or array."""
    if name + "_index" in g:
        data = g[name][:]
        idx = g[name + "_index"][:]
        starts = np.r_[0, idx[:-1]]
        out = [data[a:b] for a, b in zip(starts, idx)]
        return [[_s(v) for v in o] if o.dtype == object else o for o in out]
    v = g[name][:]
    if v.dtype == object:
        v = np.array([_s(x) for x in v], dtype=object)
    return v


def session_metadata(f: h5py.File) -> dict:
    lm = {k: _s(v) for k, v in f["general/lab_metadata"].attrs.items()
          if k not in ("namespace", "object_id", "neurodata_type")}
    return dict(
        experiment_name=lm["experiment_name"], task=lm["experiment_task"],
        projection_area=lm["projection_area"], subject=_s(f["general/subject/subject_id"]),
        start=_s(f["session_start_time"]), imaging_rate_meta=float(f["general/optophysiology/ImagingPlane/imaging_rate"][()]),
    )


def odor_table(f: h5py.File) -> pd.DataFrame:
    g = f["acquisition/odor_table"]
    df = pd.DataFrame({k: _col(g, k) for k in ["raw_id", "stim_id", "stim_name", "stim_types",
                                              "chemical_concentration"]})
    df["raw_id"] = df.raw_id.astype(str)
    return df


def trials_table(f: h5py.File) -> pd.DataFrame:
    g = f["intervals/trials"]
    cols = [c.decode() if isinstance(c, bytes) else c for c in g.attrs["colnames"]]
    out = {}
    for c in cols:
        if c.endswith("_index"):
            continue
        out[c] = _col(g, c)
    df = pd.DataFrame(out)
    ot = odor_table(f).set_index("raw_id")
    df["odor_raw_id"] = df.odor_raw_id.astype(str)
    df["stim_name"] = df.odor_raw_id.map(ot.stim_name)
    df["stim_types"] = df.odor_raw_id.map(ot.stim_types)
    df["conc"] = df.odor_raw_id.map(ot.chemical_concentration)
    df["is_control"] = df.stim_types.apply(lambda x: "control" in list(x))
    return df


# ----------------------------------------------------------------------------- normalization

def percdff(F: np.ndarray, fs: float, tau_m=1.0, tau_p=30.0, p=10) -> np.ndarray:
    """The code's norm_F_matrix_running_percentile with norm_type 'dFF' (time x cells)."""
    k_m = 2 * round(fs * tau_m / 2) + 1
    k_p = 2 * round(fs * tau_p / 2) + 1
    F = ndimage.median_filter(F, (k_m, 1))
    F0 = ndimage.percentile_filter(F, p, (k_p, 1))
    d = F - F0
    return d / d.std(axis=0, keepdims=True)


def load_session(asset_id: str, pre_s=PRE_S, post_s=POST_S, deconv=False) -> dict:
    """Stream one NWB file and return its cells, trials and onset-aligned normalized traces.

    X has shape (cells, trials, frames); t is time from onset (s) of each frame.
    """
    f = open_h5(asset_id)
    meta = session_metadata(f)
    ps = f["processing/ophys/ImageSegmentation/PlaneSegmentation"]
    iscell = ps["iscell"][:, 0] > 0
    red = ps["is_redcell_finalized"][:].astype(bool)
    plane = ps["plane"][:]
    has_muse = "subject_global_roi_muse" in ps
    muse = ps["subject_global_roi_muse"][:] if has_muse else np.full(len(plane), -1)
    tr = trials_table(f)
    planes = sorted(f["processing/ophys/Fluorescence"].keys(), key=lambda k: int(k.split("_")[1]))
    t0 = f[f"processing/ophys/Fluorescence/{planes[0]}/timestamps"][:]
    fs = 1.0 / np.median(np.diff(t0))
    n_pre, n_post = int(round(pre_s * fs)), int(round(post_s * fs))
    on_idx = np.searchsorted(t0, tr.stim_onset_timestamp.to_numpy() - 1e-9)
    Xs, cells, Ds = [], [], []
    roi0 = 0
    for p in planes:
        ds = f[f"processing/ophys/Fluorescence/{p}/data"]
        n = ds.shape[1]
        pi = int(p.split("_")[1])
        sl = slice(roi0, roi0 + n)
        roi0 += n
        cm, rm = iscell[sl], red[sl]
        if not (cm & rm).any():          # the code skips planes with no red cell
            continue
        F = ds[:][:, cm].astype(np.float64)
        Z = percdff(F, fs)
        idx = on_idx[:, None] + np.arange(-n_pre, n_post)[None, :]
        idx = np.clip(idx, 0, Z.shape[0] - 1)
        Xs.append(Z[idx].transpose(2, 0, 1).astype(np.float32))
        if deconv:
            Dd = f[f"processing/ophys/Deconvolved/{p}/data"][:][:, cm]
            Ds.append(Dd[idx].transpose(2, 0, 1).astype(np.float32))
        cells.append(pd.DataFrame(dict(plane=pi, roi=np.where(cm)[0], red=rm[cm],
                                       muse=muse[sl][cm])))
    cells = pd.concat(cells, ignore_index=True)
    cells["projection"] = np.where(cells.red, meta["projection_area"], "untagged")
    out = dict(meta=meta, cells=cells, trials=tr, X=np.concatenate(Xs, 0),
               t=np.arange(-n_pre, n_post) / fs, fs=fs, n_pre=n_pre,
               n_frames_session=len(t0), n_cells_all=int(iscell.sum()))
    if deconv:
        out["D"] = np.concatenate(Ds, 0)
    return out


def survey(asset_id: str) -> dict:
    """Metadata, counts and shapes of one file, without reading its traces."""
    f = open_h5(asset_id)
    meta = session_metadata(f)
    ps = f["processing/ophys/ImageSegmentation/PlaneSegmentation"]
    iscell = ps["iscell"][:, 0] > 0
    red = ps["is_redcell_finalized"][:].astype(bool)
    plane = ps["plane"][:]
    kept = [p for p in np.unique(plane) if (iscell & red & (plane == p)).any()]
    tr = f["intervals/trials"]
    t0 = f["processing/ophys/Fluorescence/Plane_0/timestamps"][:]
    meta.update(
        n_rois=len(iscell), n_cells=int(iscell.sum()), n_red=int((iscell & red).sum()),
        n_red_not_cell=int((red & ~iscell).sum()),
        n_cells_kept_planes=int((iscell & np.isin(plane, kept)).sum()),
        n_planes=len(np.unique(plane)), n_planes_without_red=len(np.unique(plane)) - len(kept),
        n_trials=len(tr["id"]), n_bad=int(tr["is_bad_trial"][:].sum()),
        fs_timestamps=1.0 / np.median(np.diff(t0)), n_frames=len(t0),
        has_muse="subject_global_roi_muse" in ps,
        n_redcell_table=len(f["processing/cell_tag/is_redcell/id"]),
    )
    return meta


# ----------------------------------------------------------------------------- binarization

@functools.lru_cache(None)
def _exact_mwu_sf(n1: int, n2: int) -> np.ndarray:
    """P(U >= u) for u = 0..n1*n2 under H0, exact (no ties), by counting subsets of ranks."""
    N = n1 + n2
    # c[k, s]: number of k-subsets of {1..m} with rank-sum s, built up over m
    maxs = n1 * N
    c = np.zeros((n1 + 1, maxs + 1))
    c[0, 0] = 1.0
    for m in range(1, N + 1):
        for k in range(min(m, n1), 0, -1):
            c[k, m:] += c[k - 1, :maxs + 1 - m]
    dist = c[n1, n1 * (n1 + 1) // 2: n1 * (n1 + 1) // 2 + n1 * n2 + 1]
    dist = dist / dist.sum()
    return np.cumsum(dist[::-1])[::-1]


def mwu_greater_p(U: np.ndarray, n1: int, n2: int) -> np.ndarray:
    """One-sided ('greater') Mann-Whitney p from U of the first sample, as scipy's default."""
    if n1 < 8:
        sf = _exact_mwu_sf(n1, n2)
        return sf[np.clip(np.ceil(U - 1e-9).astype(int), 0, n1 * n2)]
    mu = n1 * n2 / 2
    sd = np.sqrt(n1 * n2 * (n1 + n2 + 1) / 12)
    z = (U - mu - 0.5) / sd
    return stats.norm.sf(z)


def binarize(X: np.ndarray, t: np.ndarray, fs: float, win: tuple, starts_at_onset: bool,
             rng: np.random.Generator, reading="start", alpha=0.01, n_forward=8, n_backward=4,
             width_s=0.7, n_null=1000, trial_mask=None) -> np.ndarray:
    """Active (1) or not (0) per cell and trial for the response window win = (t0, t1) s.

    trial_mask selects the trials whose pre-onset frames form the baseline sample.
    """
    nc, nt, nf = X.shape
    w = max(1, int(round(width_s * fs)))
    base_frames = (t >= -4.0) & (t < 0)
    if trial_mask is None:
        trial_mask = np.ones(nt, bool)
    resp = np.where((t >= win[0]) & (t < win[1]))[0]
    out = np.zeros((nc, nt), np.int8)
    half = w // 2
    for c in range(nc):
        b = X[c][trial_mask][:, base_frames].ravel()
        nb = n_null
        b = np.sort(rng.choice(b, nb, replace=b.size < n_null))
        x = X[c]                                                   # trials x frames
        less = np.searchsorted(b, x, side="left")
        leq = np.searchsorted(b, x, side="right")
        r = (less + leq) / 2.0                                     # U contribution per frame
        cs = np.concatenate([np.zeros((nt, 1)), np.cumsum(r, 1)], 1)
        # window sums: window [a, a + w)
        if reading == "start":
            fa = resp[resp + w <= resp[-1] + 1]                  # windows inside the response window
        else:
            fa = resp[(resp - half >= resp[0]) & (resp - half + w <= resp[-1] + 1)] - half
        U = cs[:, fa + w] - cs[:, fa]
        sig = mwu_greater_p(U, w, nb) < alpha
        # consecutive run of at least n_forward significant frames
        k = n_forward
        if sig.shape[1] >= k:
            run = np.lib.stride_tricks.sliding_window_view(sig, k, axis=1).all(-1).any(1)
        else:
            run = np.zeros(nt, bool)
        act = run
        if starts_at_onset:
            i0 = np.searchsorted(t, 0.0)
            if reading == "start":
                ba = i0 - w - np.arange(n_backward)            # windows ending at i0-1 .. i0-4
            else:
                ba = i0 - 1 - np.arange(n_backward) - half
            ba = ba[ba >= 0]
            Ub = cs[:, ba + w] - cs[:, ba]
            back = (mwu_greater_p(Ub, w, nb) < alpha).any(1)
            act = act & ~back
        out[c] = act
    return out


# ----------------------------------------------------------------------------- metrics

def vinje_gallant(r: np.ndarray, axis=-1) -> np.ndarray:
    """(1 - (mean r)^2 / mean r^2) / (1 - 1/k) along axis; NaN where all r are 0."""
    k = r.shape[axis]
    m1 = r.mean(axis)
    m2 = (r ** 2).mean(axis)
    with np.errstate(invalid="ignore", divide="ignore"):
        s = (1 - m1 ** 2 / m2) / (1 - 1 / k)
    return s


def mutual_info_bits(b: np.ndarray, s: np.ndarray) -> float:
    """I(X; S) in bits for binary X and discrete S, from empirical frequencies."""
    mi = 0.0
    for sv in np.unique(s):
        ps = np.mean(s == sv)
        for xv in (0, 1):
            pxs = np.mean((s == sv) & (b == xv))
            px = np.mean(b == xv)
            if pxs > 0:
                mi += pxs * np.log2(pxs / (ps * px))
    return mi


def bonferroni(p, m):
    return np.minimum(np.asarray(p) * m, 1.0)


def mwu(a, b):
    a, b = np.asarray(a), np.asarray(b)
    a, b = a[np.isfinite(a)], b[np.isfinite(b)]
    return stats.mannwhitneyu(a, b, alternative="two-sided").pvalue


# ----------------------------------------------------------------------------- pseudo-populations

def trial_order(trials: pd.DataFrame, key: str, keep: np.ndarray) -> pd.DataFrame:
    """Index of kept trials with their label and the order of presentation of that label."""
    d = trials.loc[keep, [key]].copy()
    d["trial"] = d.index
    d["order"] = d.groupby(key).cumcount()
    return d


def pseudo_population(sessions: list, cell_masks: list, key: str, keeps: list, labels=None,
                      arrays=None):
    """Concatenate cells across sessions with trials matched by label and order.

    Returns the matched (label, order) table and an array (cells, pseudo-trials, ...), taken
    from each session's X or from `arrays` (one per session, cells x trials x ...).
    """
    if arrays is None:
        arrays = [s["X"] for s in sessions]
    orders = [trial_order(s["trials"], key, k) for s, k in zip(sessions, keeps)]
    if labels is None:
        labels = sorted(set.intersection(*[set(o[key]) for o in orders]))
    rows = []
    for lab in labels:
        n = min((o[key] == lab).sum() for o in orders)
        rows += [(lab, i) for i in range(n)]
    table = pd.DataFrame(rows, columns=[key, "order"])
    parts = []
    for A, m, o in zip(arrays, cell_masks, orders):
        if m.sum() == 0:
            continue
        idx = o.set_index([key, "order"]).loc[list(map(tuple, table.values)), "trial"].to_numpy()
        parts.append(A[m][:, idx])
    return table, np.concatenate(parts, 0)


def window_mean(P: np.ndarray, t: np.ndarray, a: float, b: float, agg="mean") -> np.ndarray:
    """Cells x trials response in [a, b) s after onset, as mean or max."""
    m = (t >= a) & (t < b)
    return P[:, :, m].mean(-1) if agg == "mean" else P[:, :, m].max(-1)


def cv_accuracy(Xtr, y, rng, n_splits=5):
    from sklearn.model_selection import StratifiedKFold
    from sklearn.svm import SVC
    skf = StratifiedKFold(n_splits, shuffle=True, random_state=int(rng.integers(2**31)))
    acc = []
    for tr_i, te_i in skf.split(Xtr, y):
        clf = SVC(kernel="linear").fit(Xtr[tr_i], y[tr_i])
        acc.append(np.mean(clf.predict(Xtr[te_i]) == y[te_i]))
    return float(np.mean(acc))


def decode_windows(P, y, t, windows, n_cells, n_rep, rng, agg="mean", n_splits=5):
    """Same-window decoding accuracy, repeats x windows; each repeat draws n_cells cells and
    one fold split shared by all windows (train and test never on the same trial)."""
    from sklearn.model_selection import StratifiedKFold
    from sklearn.svm import SVC
    out = np.zeros((n_rep, len(windows)))
    for r in range(n_rep):
        cells = rng.choice(P.shape[0], n_cells, replace=False)
        skf = StratifiedKFold(n_splits, shuffle=True, random_state=int(rng.integers(2**31)))
        folds = list(skf.split(np.zeros(len(y)), y))
        for wi, (a, b) in enumerate(windows):
            R = window_mean(P[cells], t, a, b, agg).T
            acc = []
            for tr_i, te_i in folds:
                clf = SVC(kernel="linear").fit(R[tr_i], y[tr_i])
                acc.append(np.mean(clf.predict(R[te_i]) == y[te_i]))
            out[r, wi] = np.mean(acc)
    return out


def survey_all(max_workers=12) -> pd.DataFrame:
    """Metadata of every file of the pinned version (no traces read)."""
    from concurrent.futures import ThreadPoolExecutor
    a = assets()
    with ThreadPoolExecutor(max_workers) as ex:
        rows = list(ex.map(survey, a.asset_id))
    S = pd.DataFrame(rows)
    S["asset_id"], S["path"] = a.asset_id.values, a.path.values
    S["date"] = S.start.str[:10]
    return S


def load_experiment(S: pd.DataFrame, name: str, max_workers=8) -> list:
    """Stream and load every session of one experiment (in the order of S)."""
    from concurrent.futures import ThreadPoolExecutor
    ids = S[S.experiment_name == name].asset_id.tolist()
    with ThreadPoolExecutor(max_workers) as ex:
        return list(ex.map(load_session, ids))


# ----------------------------------------------------------------------------- Go/NoGo

PHASES = {"odor": (0, 2), "delay": (2, 5), "act-early": (5, 10), "act-late": (10, 15)}  # Methods, Task-relevant phases
GEN_PERMS = [(("go1", "nogo1"), ("go2", "nogo2")), (("go2", "nogo2"), ("go1", "nogo1")),
             (("go1", "nogo2"), ("go2", "nogo1")), (("go2", "nogo1"), ("go1", "nogo2"))]  # Methods, generalized valence


def hit_relabel(trials: pd.DataFrame) -> pd.Series:
    """Outcome with Go trials counted as hits only when the reward came within 10 s after the
    delay, i.e. at most 15 s after odor onset (Methods, Animal behavior, last paragraph)."""
    out = trials.outcome.copy()
    late = (out == "hit") & ((trials.reward_onset - trials.stim_onset) > 15.0)
    out[late] = "miss"
    return out


def phase_features(P, t, phases, agg):
    """List over phases of (trials x cells) responses, mean or max over the phase."""
    return [window_mean(P, t, a, b, agg).T for a, b in phases]


def _svc():
    from sklearn.svm import SVC
    return SVC(kernel="linear")


def decode_scheme(R, ann, scheme, folds):
    """Accuracy of one decoder on responses R (trials x cells) with CS labels ann.

    scheme 'identity': 4 CS; 'valence': go against nogo, folds independent of odor;
    'generalized': train on one CS+/CS- pair, test on the other, mean over the 4 permutations."""
    val = np.array([a.startswith("go") for a in ann])
    if scheme == "generalized":
        acc = []
        for tr_set, te_set in GEN_PERMS:
            tr_i, te_i = np.isin(ann, tr_set), np.isin(ann, te_set)
            clf = _svc().fit(R[tr_i], val[tr_i])
            acc.append(np.mean(clf.predict(R[te_i]) == val[te_i]))
        return float(np.mean(acc))
    y = ann if scheme == "identity" else val
    acc = []
    for tr_i, te_i in folds[scheme]:
        clf = _svc().fit(R[tr_i], y[tr_i])
        acc.append(np.mean(clf.predict(R[te_i]) == y[te_i]))
    return float(np.mean(acc))


def decode_gng(P, ann, t, n_cells, n_rep, rng, schemes=("identity", "valence", "generalized"),
               phases=None, aggs=("mean", "max"), n_splits=5):
    """Pseudo-population decoding per task phase: dict (scheme, agg) -> repeats x phases."""
    from sklearn.model_selection import StratifiedKFold
    phases = list(PHASES.values()) if phases is None else phases
    out = {(s, a): np.zeros((n_rep, len(phases))) for s in schemes for a in aggs}
    val = np.array([a.startswith("go") for a in ann])
    for r in range(n_rep):
        cells = rng.choice(P.shape[0], n_cells, replace=False) if n_cells < P.shape[0] else np.arange(P.shape[0])
        folds = {}
        for s, y in [("identity", ann), ("valence", val)]:
            skf = StratifiedKFold(n_splits, shuffle=True, random_state=int(rng.integers(2**31)))
            folds[s] = list(skf.split(np.zeros(len(y)), y))
        for a in aggs:
            feats = phase_features(P[cells], t, phases, a)
            for pi, R in enumerate(feats):
                for s in schemes:
                    out[s, a][r, pi] = decode_scheme(R, ann, s, folds)
    return out


def transfer_matrix(resp, anns, scheme, rng, n_splits=5):
    """Train on (day i, phase p), test on (day j, phase q) for one mouse's tracked cells.

    resp[d][p] is (trials x cells) for day d and phase p, anns[d] the CS labels of day d's
    trials. Within a day, train and test trials are split by stratified 5-fold
    cross-validation (the same split for all phase pairs, so train and test are never the same
    trial); across days, all trials of day i train and all trials of day j test. Returns an
    array (days*phases) x (days*phases), rows the training (day, phase)."""
    from sklearn.model_selection import StratifiedKFold
    nd, npz = len(resp), len(resp[0])
    M = np.zeros((nd * npz, nd * npz))
    for i in range(nd):
        ann_i = np.asarray(anns[i])
        val_i = np.array([a.startswith("go") for a in ann_i])
        y_i = ann_i if scheme == "identity" else val_i
        skf = StratifiedKFold(n_splits, shuffle=True, random_state=int(rng.integers(2**31)))
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            folds = list(skf.split(np.zeros(len(y_i)), y_i if scheme != "generalized" else ann_i))
        for p in range(npz):
            for j in range(nd):
                ann_j = np.asarray(anns[j])
                val_j = np.array([a.startswith("go") for a in ann_j])
                for q in range(npz):
                    Rtr, Rte = resp[i][p], resp[j][q]
                    if scheme == "generalized":
                        acc = []
                        for tr_set, te_set in GEN_PERMS:
                            a_i, b_j = np.isin(ann_i, tr_set), np.isin(ann_j, te_set)
                            clf = _svc().fit(Rtr[a_i], val_i[a_i])
                            acc.append(np.mean(clf.predict(Rte[b_j]) == val_j[b_j]))
                        M[i * npz + p, j * npz + q] = np.mean(acc)
                        continue
                    y_j = ann_j if scheme == "identity" else val_j
                    if i == j:
                        acc = []
                        for tr_i, te_i in folds:
                            if len(np.unique(y_i[tr_i])) < 2:     # a fold without both classes is not fitted
                                continue
                            clf = _svc().fit(Rtr[tr_i], y_i[tr_i])
                            acc.append(np.mean(clf.predict(Rte[te_i]) == y_j[te_i]))
                        M[i * npz + p, j * npz + q] = np.mean(acc) if acc else np.nan
                    else:
                        if len(np.unique(y_i)) < 2:
                            M[i * npz + p, j * npz + q] = np.nan
                            continue
                        clf = _svc().fit(Rtr, y_i)
                        M[i * npz + p, j * npz + q] = np.mean(clf.predict(Rte) == y_j)
    return M


def fingerprint(asset_id: str) -> dict:
    """Small per-plane summaries for finding duplicated recordings: the mean image (block-averaged
    to 64 x 64), the first 300 frames of the plane's summed raw fluorescence, and the trial
    stimulus sequence."""
    f = open_h5(asset_id)
    out = dict(planes={}, stims=tuple(str(x) for x in _col(f["intervals/trials"], "odor_raw_id")))
    for p in sorted(f["processing/ophys/Fluorescence"].keys()):
        i = int(p.split("_")[1])
        img = f[f"processing/ophys/Backgrounds_{i}/meanImg"][:]
        img = img[: img.shape[0] // 8 * 8, : img.shape[1] // 8 * 8]
        img = img.reshape(img.shape[0] // 8, 8, img.shape[1] // 8, 8).mean((1, 3))
        tr = f[f"processing/ophys/Fluorescence/{p}/data"][:300].sum(1)
        out["planes"][i] = dict(img=img.ravel(), trace=tr)
    return out
