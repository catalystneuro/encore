"""Loading and measures for CRCNS data set bst-3 (Strickland and McDannald 2022, Nat Commun 13:6192).

The data set (doi:10.6080/K0Q23XGR) is not versioned (version "unversioned"); it is read from the
public bucket at https://crcnsarchive.s3-us-west-2.amazonaws.com/bst-3/live/data.zip, a zip opened in
place over range requests. It holds one MATLAB file per single unit (data/singleUnits, 1812 files),
the cube file built from them by the paper's cubeScript.m (data/cubeFile/cubeFile.mat) and the
paper's analysis scripts (data/scripts). The paper's Code availability ("Code for single-unit
analyses is available at https://crcns.org/") points at these scripts, so where the Methods leave a
detail open and a script settles it, the script is followed (protocol, reader step 2 and author
step 1.6) and the script and line are cited here.

Where each parameter comes from:
- Trial rows 1-4 danger, 5-6 uncertainty shock, 7-12 uncertainty omission, 13-16 safety: the data
  descriptor and cubeScript.m (time.cue = [cue100; cueSPR; cueNsPR; cue0]).
- Time stamps are in samples at 30 kHz: cubeScript.m (30000 samples per 1-s bin).
- Cue matrix, 1-s bins 9:22 of the 40-s window from 10 s before cue onset (2 s before onset to 2 s
  after offset), per cue danger, uncertainty (rows 5-12), safety: cueAnalysis.m (pcaVarCue).
- Outcome matrix, 500-ms bins 46:65 (12.5 to 22.5 s after cue onset, the 10 s from shock offset),
  per trial type: outcomeAnalysis.m (pcaVarOutcome).
- Normalization: per trial, firing minus that trial's 2-s pre-cue rate (base2, rounded down),
  z-scored over all trials and bins of the 40-s window at each bin size: cubeScript.m ("find
  differential firing", "find z firing"). The claims file's readings n-a/n-b and w-a/w-b are also
  computed from the spike times for the link claim.
- Suppression ratio per trial, (base - cue)/(base + cue), pokes in the 20 s before cue x 3 and in
  the 10-s cue x 6, a trial with no pokes set to 1: cubeScript.m (poke.SR(isnan(poke.SR)) = 1). The
  claims file's sr-a (set to 0) and sr-b (left out) are shown beside it.
- Regression with an intercept, cluster mean firing per trial row on threat probability (1, 0.25,
  0) and the mean over member units of the trial's suppression ratio: cueAnalysis.m ("Cluster
  regression"). Outcome: regressors signed prediction error (0, .75, -.25, 0) and shock (1, 1, 0,
  0), beta columns 1-20 prediction error and 21-40 shock: outcomeRegression.m.
- PCA as MATLAB pca with defaults (columns centred, not scaled), percent variance from the
  eigenvalues: all scripts.
- PC1 contribution shuffle, each unit's row of the cluster permuted across its columns, 1000
  times: cueAnalysis.m (Shuffle(..., 2)); the claims file's reading s-a.
- Cue lesion, each trial row of a shuffled cluster's mean firing permuted across the 14
  intervals before regression, betas averaged over 1000 iterations: cueRegression.m
  (Shuffle(regData, 2)); the claims file's s-c. Outcome lesion, the shuffled cluster's firing
  permuted across the 16 trial rows (Shuffle(regData, 1)): outcomeRegression.m; the claims file's
  s-d. Whether the same row permutation is used for every interval is not settled by the script
  (it depends on the Shuffle function, which is not included); both are run.
- Outcome hub measure, squared Pearson correlation of a unit's 80-value row with the mean row of
  each other cluster of its network, averaged: outcomeAnalysis.m.
- Region numbers and names, and the merges 21 -> 2 (CIC to DpWh) and 24 -> 11 (x/scp):
  cueAnalysis.m and the region list in cubeScript.m.
- Subject numbers 1-10 for animals js10, 11, 13, 14, 15, 21, 22, 24, 25, 27 and sex (js10, 11,
  13, 27 female): cueAnalysis.m.
- Random seeds and the number of k-means seeds are standard choices that the claims file states.
"""
from __future__ import annotations

import hashlib
import io
import zipfile

import fsspec
import h5py
import numpy as np
import scipy.io as sio
from scipy import stats

DATASET = "bst-3"
VERSION = "unversioned"
DOI = "10.6080/K0Q23XGR"
BASE_URL = "https://crcnsarchive.s3-us-west-2.amazonaws.com/bst-3/live/"
ZIP_URL = BASE_URL + "data.zip"
SOURCE_DATA_URL = ("https://static-content.springer.com/esm/art%3A10.1038%2Fs41467-022-34021-1/"
                   "MediaObjects/41467_2022_34021_MOESM4_ESM.xlsx")
SOURCE_DATA_MD5 = "4df716fd6739ee3de3b0df81c4175be8"

FS = 30000  # samples per second (cubeScript.m)
RATS = ["10", "11", "13", "14", "15", "21", "22", "24", "25", "27"]   # subjects 1-10 (cueAnalysis.m)
FEMALE = {"10", "11", "13", "27"}
REGIONS = ["DPG", "DpWh", "DLPAG", "LPAG", "VLPAG", "me5", "DRL", "DRD", "DRV", "PDR", "mlf", "isRt",
           "Pa4", "x/scp", "SPTg", "PnO", "VTg", "DMTg", "ts", "PMnR", "MnR"]
# cube region number -> dorsal-ventral order 1-21 (cueAnalysis.m, lines 15-38)
REGION_REMAP = {1: 1, 2: 2, 21: 2, 3: 3, 4: 4, 5: 5, 27: 6, 6: 7, 7: 8, 8: 9, 9: 10, 10: 11, 20: 12,
                23: 13, 11: 14, 24: 14, 12: 15, 16: 16, 13: 17, 17: 18, 22: 19, 14: 20, 15: 21}
TYPES = {"danger": slice(0, 4), "unc_shock": slice(4, 6), "unc_omission": slice(6, 12),
         "safety": slice(12, 16), "uncertainty": slice(4, 12)}
PROB = np.array([1] * 4 + [0.25] * 8 + [0] * 4, float)
PE = np.array([0] * 4 + [0.75] * 2 + [-0.25] * 6 + [0] * 4, float)
SHOCK = np.array([1] * 6 + [0] * 10, float)


# --- reading -----------------------------------------------------------------------------------

def open_zip():
    f = fsspec.open(ZIP_URL, block_size=2 ** 25, cache_type="readahead").open()
    return zipfile.ZipFile(f)


def read_text(name):
    with fsspec.open(BASE_URL + name, "rt") as f:
        return f.read()


CUBE_FIELDS = ["fire/z/s1/interval", "fire/z/ms500/interval", "fire/z/ms250/interval", "fire/raw/s1/interval",
               "fire/raw/base2",
               "poke/SR", "poke/base", "poke/cue", "anatomy/regionNum", "anatomy/ID", "anatomy/x",
               "anatomy/y", "anatomy/z"]


def load_cube(zf):
    """The cube's arrays as (unit, bin, trial); h5py reads MATLAB's (trial, bin, unit) transposed."""
    with h5py.File(io.BytesIO(zf.read("data/cubeFile/cubeFile.mat")), "r") as h:
        c = h["cube"]
        out = {k: c[k][()] for k in CUBE_FIELDS}
    out["ID"] = np.array(["".join(map(chr, r)) for r in out.pop("anatomy/ID")[:, :, 0]])
    return out


def _parse_unit(b):
    """id, spike times and event times of one single-unit file (MATLAB 5 or 7.3)."""
    if b[:10] == b"MATLAB 5.0":
        m = sio.loadmat(io.BytesIO(b), squeeze_me=True, struct_as_record=False)
        t = m["time"]
        ev = {k: np.atleast_1d(getattr(t, k)).astype(float) for k in t._fieldnames}
        return str(m["id"]), np.asarray(m["spike"]).ravel().astype(np.int64), ev
    with h5py.File(io.BytesIO(b), "r") as h:
        uid = "".join(map(chr, h["id"][()].ravel()))
        spike = h["spike"][()].ravel().astype(np.int64)
        ev = {}
        for k in h["time"].keys():
            v = h["time"][k][()]
            ev[k] = np.array([], float) if v.dtype == np.uint64 else v.ravel().astype(float)
    return uid, spike, ev


def _count(spike, starts, width):
    """Spikes in (start, start + width], as cubeScript.m counts them (spike > a & spike <= b)."""
    return (np.searchsorted(spike, starts + width, side="right")
            - np.searchsorted(spike, starts, side="right"))


def scan_units(zf, limit=None):
    """One pass over the single-unit files, keeping only what the analyses need.

    Per unit: spike counts in 250-ms bins from 20 s before to 40 s after cue onset (240 bins) for
    the 16 trials; counts in the cube's 1-s bins (40 s from 10 s before onset) and the 2-s
    baseline, to check the cube against the spikes; the summed danger-trial spike count in 1-ms
    bins from 2 s before onset to the end of the 10-s cue (12000 bins), for the latency; and per
    session the cue, shock and poke times.
    """
    infos = sorted([i for i in zf.infolist() if i.filename.startswith("data/singleUnits/")
                    and i.filename.endswith(".mat")], key=lambda i: i.header_offset)
    if limit:
        infos = infos[:limit]
    ids, c250, c1s, base2, ms1, n_spk, n_dup, unsorted, fmt, sessions = [], [], [], [], [], [], [], [], [], {}
    for info in infos:
        b = zf.read(info.filename)
        uid, spike, ev = _parse_unit(b)
        n_dup.append(spike.size - np.unique(spike).size)
        n_spk.append(spike.size)
        unsorted.append(bool(np.any(np.diff(spike) < 0)))
        # cubeScript.m counts with intersect(), which keeps each spike time once
        spike = np.unique(spike)
        fmt.append(b[:10].decode())
        cue = np.concatenate([ev["cue100"], ev["cueSPR"], ev["cueNsPR"], ev["cue0"]])
        ids.append(uid)
        w = FS // 4
        starts = cue[:, None] - 20 * FS + w * np.arange(240)[None, :]
        c250.append(_count(spike, starts, w).astype(np.int16))
        starts = cue[:, None] - 10 * FS + FS * np.arange(40)[None, :]
        c1s.append(_count(spike, starts, FS).astype(np.int16))
        base2.append(np.floor(_count(spike, cue - 2 * FS, 2 * FS) / 2))
        starts = ev["cue100"][:, None] - 2 * FS + 30 * np.arange(12000)[None, :]
        ms1.append(_count(spike, starts, 30).sum(0).astype(np.int16))
        key = uid[:10]
        if key not in sessions:
            sessions[key] = {"cue": cue, "poke": np.sort(ev["poke"]), "shock": np.sort(ev["shock"]),
                             "reward": ev["reward"], "file_id": uid}
        else:
            s = sessions[key]
            same = (np.array_equal(s["cue"], cue) and np.array_equal(s["poke"], np.sort(ev["poke"])))
            if not same:
                s.setdefault("differing_units", []).append(uid)
    return {"ID": np.array(ids), "c250": np.stack(c250), "c1s": np.stack(c1s), "base2": np.stack(base2),
            "ms1": np.stack(ms1), "n_spikes": np.array(n_spk),
            "n_duplicate_spikes": np.array(n_dup), "unsorted": np.array(unsorted), "format": np.array(fmt),
            "sessions": sessions}


def load_source_data():
    """The paper's Source Data workbook (Nature Communications, supplementary file MOESM4)."""
    import openpyxl
    with fsspec.open(SOURCE_DATA_URL, "rb") as f:
        b = f.read()
    md5 = hashlib.md5(b).hexdigest()
    wb = openpyxl.load_workbook(io.BytesIO(b), read_only=True, data_only=True)
    sheets = {ws.title: [list(r) for r in ws.iter_rows(values_only=True)] for ws in wb.worksheets}
    return sheets, md5


def sd_cue_cluster_rows(sheets, k):
    return np.array([r[:42] for r in sheets[f"Figure 2b k{k}"][1:] if r[0] is not None], float)


def sd_outcome_cluster_rows(sheets, k):
    return np.array([r[1:81] for r in sheets[f"Figure 4b k{k}"][2:] if r[1] is not None], float)


def sd_matrix(sheets, name, first_row, ncol, first_col=1):
    rows = [r for r in sheets[name][first_row:] if r[first_col] is not None]
    return np.array([r[first_col:first_col + ncol] for r in rows], float)


# --- rows of the cue and outcome matrices --------------------------------------------------------

def type_means(a, kinds):
    """Mean over the trials of each type; a is (unit, bin, trial)."""
    return [a[:, :, TYPES[k]].mean(2) for k in kinds]


def cue_matrix(z_s1):
    """1812 x 42: danger, uncertainty, safety, 1-s bins 9:22 (cueAnalysis.m, pcaVarCue)."""
    return np.hstack([m[:, 8:22] for m in type_means(z_s1, ["danger", "uncertainty", "safety"])])


def outcome_matrix(z_ms500):
    """1812 x 80: 500-ms bins 46:65 per trial type (outcomeAnalysis.m, pcaVarOutcome)."""
    return np.hstack([m[:, 45:65] for m in
                      type_means(z_ms500, ["danger", "unc_shock", "unc_omission", "safety"])])


def normalized_readings(c250):
    """Cue and outcome rows under the claims file's readings, from 250-ms counts (unit, trial, 240).

    n-a: each trial's own baseline (mean rate over the 2 s before onset); n-b: the mean baseline of
    that trial's type (danger, uncertainty, safety). w-a: z over 200 bins (-20 to +30 s); w-b:
    over all 240 bins. Rates are not rounded. Returns {reading: (cue rows, outcome rows)}.
    """
    rate = c250.astype(float) * 4                      # unit, trial, bin
    base = rate[:, :, 72:80].mean(2)                   # 2 s before onset (bins 72-79)
    base_type = base.copy()
    for sl in (slice(0, 4), slice(4, 12), slice(12, 16)):
        base_type[:, sl] = base[:, sl].mean(1, keepdims=True)
    out = {}
    for nname, b in (("n-a", base), ("n-b", base_type)):
        diff = rate - b[:, :, None]
        for wname, nb in (("w-a", 200), ("w-b", 240)):
            seg = diff[:, :, :nb]
            mu = seg.mean((1, 2), keepdims=True)
            sd = seg.std((1, 2), ddof=1, keepdims=True)
            sd[sd == 0] = np.nan
            z = (diff - mu) / sd                       # unit, trial, bin
            z = np.transpose(z, (0, 2, 1))             # unit, bin, trial
            s1 = z.reshape(z.shape[0], 60, 4, 16).mean(2)       # 1-s intervals from -20 s
            ms500 = z.reshape(z.shape[0], 120, 2, 16).mean(2)   # 500-ms intervals from -20 s
            cue = np.hstack([m[:, 18:32] for m in type_means(s1, ["danger", "uncertainty", "safety"])])
            outc = np.hstack([m[:, 65:85] for m in type_means(
                ms500, ["danger", "unc_shock", "unc_omission", "safety"])])
            out[f"{nname}, {wname}"] = (cue, outc)
    return out


def match_rows(sd_rows, rows, tol=0.01):
    """For each Source Data row, the units whose row is within tol everywhere (max abs difference),
    and the unit with the highest Pearson correlation."""
    rows = np.nan_to_num(rows, nan=1e9)
    hits, best_r, best_i = [], [], []
    rz = (rows - rows.mean(1, keepdims=True))
    rz /= np.linalg.norm(rz, axis=1, keepdims=True) + 1e-300
    for r in sd_rows:
        d = np.abs(rows - r).max(1)
        hits.append(np.flatnonzero(d < tol))
        q = r - r.mean()
        q /= np.linalg.norm(q) + 1e-300
        c = rz @ q
        best_i.append(int(np.argmax(c)))
        best_r.append(float(np.max(c)))
    return hits, np.array(best_r), np.array(best_i)


# --- behaviour -----------------------------------------------------------------------------------

def suppression_ratios(cue, poke, empty="code"):
    """Per trial (cubeScript.m): pokes in (t-20 s, t] x 3 and in (t, t+10 s] x 6.
    empty: 'code' sets a trial with no pokes to 1 (the script), 'zero' to 0 (sr-a), 'drop' to NaN (sr-b)."""
    base = 3 * (np.searchsorted(poke, cue, "right") - np.searchsorted(poke, cue - 20 * FS, "right"))
    cue_n = 6 * (np.searchsorted(poke, cue + 10 * FS, "right") - np.searchsorted(poke, cue, "right"))
    with np.errstate(invalid="ignore", divide="ignore"):
        sr = (base - cue_n) / (base + cue_n)
    fill = {"code": 1.0, "zero": 0.0, "drop": np.nan}[empty]
    sr[np.isnan(sr)] = fill
    return sr


def mixed_anova_cue_by_group(Y, group):
    """F for the within factor (columns of Y) in a within x between mixed ANOVA, subjects as rows.
    Error is cue x subjects within groups, df (J - 1)(N - G). Also the one-way repeated-measures F."""
    Y = np.asarray(Y, float)
    N, J = Y.shape
    gm = Y.mean()
    subj = Y.mean(1, keepdims=True)
    ss_within = ((Y - subj) ** 2).sum()
    ss_cue = N * ((Y.mean(0) - gm) ** 2).sum()
    groups = np.unique(group)
    ss_int = 0.0
    for g in groups:
        Yg = Y[group == g]
        ss_int += len(Yg) * ((Yg.mean(0) - Yg.mean() - Y.mean(0) + gm) ** 2).sum()
    df1 = J - 1
    df_mixed = (J - 1) * (N - len(groups))
    ss_err_mixed = ss_within - ss_cue - ss_int
    F_mixed = (ss_cue / df1) / (ss_err_mixed / df_mixed)
    df_rm = (J - 1) * (N - 1)
    F_rm = (ss_cue / df1) / ((ss_within - ss_cue) / df_rm)
    return {"F_mixed": F_mixed, "df_mixed": (df1, df_mixed), "p_mixed": stats.f.sf(F_mixed, df1, df_mixed),
            "F_rm": F_rm, "df_rm": (df1, df_rm), "p_rm": stats.f.sf(F_rm, df1, df_rm)}


# --- PCA, k-means, shuffles ----------------------------------------------------------------------

def pca(X):
    """MATLAB pca defaults: centre columns, no scaling. Returns (coeff columns, percent explained)."""
    Xc = X - X.mean(0)
    _, s, vt = np.linalg.svd(Xc, full_matrices=False)
    v = s ** 2
    return vt.T, 100 * v / v.sum()


def pc1_percent(X):
    Xc = X - X.mean(0)
    w = np.linalg.eigvalsh(Xc.T @ Xc)
    return 100 * w[-1] / w.sum()


def kmeans_sizes(X, k, seeds):
    from sklearn.cluster import KMeans
    out = []
    for s in seeds:
        km = KMeans(n_clusters=k, init="k-means++", n_init=1, random_state=int(s)).fit(X)
        out.append((np.bincount(km.labels_, minlength=k), km.inertia_, km.labels_))
    return out


def shuffle_rows(B, rng):
    """Each row permuted independently across its columns (reading s-a)."""
    return np.take_along_axis(B, rng.random(B.shape).argsort(1), 1)


def shuffle_block(B, rng):
    """All entries of the block permuted together (reading s-b)."""
    return rng.permutation(B.ravel()).reshape(B.shape)


def pc1_contribution(X, labels, ks, rng, n_iter=1000, mode="s-a"):
    """Drop in PC1 percent when one cluster's rows are shuffled, averaged over n_iter, per unit
    (cueAnalysis.m, "pca with single cluster shuffled")."""
    base = pc1_percent(X)
    f = shuffle_rows if mode == "s-a" else shuffle_block
    out = {}
    for k in ks:
        m = labels == k
        B = X[m]
        Y = X.copy()
        vals = np.empty(n_iter)
        for i in range(n_iter):
            Y[m] = f(B, rng)
            vals[i] = pc1_percent(Y)
        out[k] = (base - vals.mean()) / m.sum()
    return out


# --- latency -------------------------------------------------------------------------------------

def change_point(x):
    """MATLAB findchangepts(x) with its defaults: the one change in mean that most reduces the
    residual sum of squares; returns the 1-based index of the first sample after the change, or
    None when no split reduces it (a constant signal)."""
    x = np.asarray(x, float)
    n = x.size
    c1 = np.cumsum(x)
    c2 = np.cumsum(x ** 2)
    k = np.arange(1, n)
    left = c2[:-1] - c1[:-1] ** 2 / k
    right = (c2[-1] - c2[:-1]) - (c1[-1] - c1[:-1]) ** 2 / (n - k)
    cost = left + right
    total = c2[-1] - c1[-1] ** 2 / n
    i = int(np.argmin(cost))
    if not cost[i] < total - 1e-9 * max(total, 1):
        return None
    return i + 2          # first sample of the second segment, 1-based


# --- regression ----------------------------------------------------------------------------------

def regress_betas(Y, regressors, intercept=True):
    """Least squares per column of Y (16 trial rows x intervals); returns betas of the regressors."""
    X = np.column_stack(([np.ones(len(regressors[0]))] if intercept else []) + list(regressors))
    b, *_ = np.linalg.lstsq(X, Y, rcond=None)
    return b[1:] if intercept else b


def cue_betas(z_s1, sr, labels, ks, mode="r-a", intercept=True, firing=None):
    """Cluster x 28 betas, columns 1-14 threat probability, 15-28 behaviour (cueAnalysis.m).
    r-a: one regression on the cluster's mean firing, behaviour the mean member suppression ratio.
    r-b: one regression per unit on its own trials and ratios, betas averaged in the cluster."""
    F = z_s1[:, 8:22, :] if firing is None else firing    # unit, 14, 16
    rows = []
    for k in ks:
        m = labels == k
        if mode == "r-a":
            Y = F[m].mean(0).T                              # 16 x 14
            b = regress_betas(Y, [PROB, sr[m].mean(0)], intercept)
        else:
            bs = [regress_betas(F[u].T, [PROB, sr[u]], intercept) for u in np.flatnonzero(m)]
            b = np.mean(bs, 0)
        rows.append(np.concatenate([b[0], b[1]]))
    return np.array(rows)


def outcome_betas(z_ms500, labels, ks, mode="r-a", intercept=True):
    """Cluster x 40 betas, columns 1-20 prediction error, 21-40 shock (outcomeRegression.m)."""
    F = z_ms500[:, 45:65, :]
    rows = []
    for k in ks:
        m = labels == k
        if mode == "r-a":
            b = regress_betas(F[m].mean(0).T, [PE, SHOCK], intercept)
        else:
            b = np.mean([regress_betas(F[u].T, [PE, SHOCK], intercept) for u in np.flatnonzero(m)], 0)
        rows.append(np.concatenate([b[0], b[1]]))
    return np.array(rows)


def cue_lesion_betas(z_s1, sr, labels, ks, shuffled, rng, n_iter=1000):
    """cueRegression.m, "Lesion regression": each shuffled cluster's 16 x 14 mean firing has each
    trial row permuted across the 14 intervals, then regression; betas averaged (reading s-c)."""
    F = z_s1[:, 8:22, :]
    means = {k: F[labels == k].mean(0).T for k in ks}     # 16 x 14
    srs = {k: sr[labels == k].mean(0) for k in ks}
    acc = np.zeros((len(ks), 28))
    for i in range(n_iter):
        for j, k in enumerate(ks):
            Y = shuffle_rows(means[k], rng) if k in shuffled else means[k]
            b = regress_betas(Y, [PROB, srs[k]])
            acc[j] += np.concatenate([b[0], b[1]])
    return acc / n_iter


def outcome_lesion_betas(z_ms500, labels, ks, shuffled, rng, n_iter=1000, same_perm=True):
    """outcomeRegression.m, "1-3 shuffled": the shuffled cluster's 16 x 20 mean firing permuted
    across trial rows (Shuffle(regData, 1)), the same permutation for every interval (same_perm) or
    one per interval; betas averaged (reading s-d)."""
    F = z_ms500[:, 45:65, :]
    means = {k: F[labels == k].mean(0).T for k in ks}     # 16 x 20
    acc = np.zeros((len(ks), 40))
    for i in range(n_iter):
        for j, k in enumerate(ks):
            Y = means[k]
            if k in shuffled:
                Y = Y[rng.permutation(16)] if same_perm else shuffle_rows(Y.T, rng).T
            b = regress_betas(Y, [PE, SHOCK])
            acc[j] += np.concatenate([b[0], b[1]])
    return acc / n_iter


def beta_shuffle_average(B, rows, rng, n_iter=1000, mode="s-a", ncol_per=None):
    """Variants s-a / s-b on a beta matrix: the given rows permuted (each row across its columns,
    or the block's entries together), averaged over n_iter."""
    acc = np.zeros_like(B)
    for i in range(n_iter):
        C = B.copy()
        C[rows] = shuffle_rows(B[rows], rng) if mode == "s-a" else shuffle_block(B[rows], rng)
        acc += C
    return acc / n_iter


def pca_per_iteration(make, n_iter, ref):
    """Reading v-b: PCA on each iteration's matrix, each PC sign-aligned to ref (positive dot
    product), weights and percentages averaged."""
    W = np.zeros((ref.shape[0], 2))
    P = np.zeros(2)
    for i in range(n_iter):
        c, e = pca(make(i))
        for j in range(2):
            v = c[:, j] * (1 if c[:, j] @ ref[:, j] >= 0 else -1)
            W[:, j] += v
        P += e[:2]
    return W / n_iter, P / n_iter


# --- correlations, anatomy -----------------------------------------------------------------------

def corr_matrix(P):
    return np.corrcoef(P)


def unit_cluster_corr(rows_unit, means_other, squared=False):
    """Mean over the other clusters of the Pearson r (or r squared) between a unit's row and each
    cluster's mean row."""
    rs = []
    for m in means_other:
        r = np.corrcoef(rows_unit, m)[0, 1]
        rs.append(r * r if squared else r)
    return float(np.nanmean(rs))


def differential(region, members_a, members_b, n_regions=21):
    """Per region, its share of network A's units minus its share of network B's, in percentage
    points (Source Data Fig. 3e and 5e right)."""
    a = np.bincount(region[members_a], minlength=n_regions + 1)[1:]
    b = np.bincount(region[members_b], minlength=n_regions + 1)[1:]
    return 100 * (a / a.sum() - b / b.sum()), a, b
