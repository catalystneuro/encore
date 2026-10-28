"""Loading and measures for OpenNeuro ds000228, snapshot 1.1.1 (Richardson et al. 2018).

Richardson, Lisandrelli, Riobueno-Naylor & Saxe (2018), "Development of the social brain from
age three to twelve years", Nature Communications 9, 1027, doi:10.1038/s41467-018-03399-2.

The snapshot holds, for 155 participants, the raw BOLD and T1 images and the paper's own
preprocessed data under derivatives/preprocessed_data (SPM8, normalized to MNI, 2 mm voxels,
5 mm smoothing; `*_swrf_bold.nii.gz`), with the ART artifact indicators and five CompCor
regressors of each run (`*_ART_and_CompCor_nuisance_regressors.mat`, matrix R, one row per
regressor), and the group ROIs under derivatives/ROIs. Behaviour and demographics are in
participants.tsv. Every file is read from its URL pinned to the snapshot (urls[0] of the
OpenNeuro GraphQL listing) into memory; nothing is written to disk.

Where the parameters come from (claims file: claims/openneuro-ds000228/; the labels P1 to P9
and O1 to O9 are those of its header):

- ROI voxels: the masks deposited in derivatives/ROIs (reading O1a), in MNI mm; their sizes
  equal those of Supplementary Table 2. M1 (right_primotor, left_primotor), V1 (right_CS,
  left_CS), face (rSTS_masked, lSTS, rOFA, lOFA, rFFA, lFFA) and scene (rRSC, lRSC, rTOS, lTOS,
  rPPA, lPPA) are named as in derivatives/README.txt.
- Timecourse preprocessing (P4, Methods, fMRI data analysis, paragraph 4: "We applied nearest
  neighbor interpolation over artifact timepoints ... regressed out two kinds of nuisance
  covariates ... The residual timecourses were then high-pass filtered with a cutoff of 100 s.
  Timecourses from all voxels within an ROI were averaged ... and artifact timepoints were
  subsequently excluded (NaNed)"). Every step is linear and the same for each voxel, so it is
  applied to the ROI's mean timecourse, which gives the same result as per voxel then average.
  Nearest-neighbour ties (an artifact run with good timepoints at equal distance on both
  sides) take the earlier timepoint, a standard choice that cannot change a result beyond
  rounding. The regression includes an intercept (standard). The 100 s high-pass is SPM's
  discrete cosine basis (spm_filter: order fix(2 * n * TR / cutoff) + 1, constant included),
  the standard SPM8 filter, which the paper used.
- Artifact regressors (O2): the deposited R matrix has one indicator per artifact timepoint
  (reading O2a); `single_artifact_regressor=True` gives reading O2b.
- M1 regression for the inter-region correlation (P4, Methods paragraph 5: "we additionally
  regressed out the raw timecourse extracted from bilateral primary motor cortex"): the mean
  raw timecourse over the voxels of both M1 ROIs.
- Inter-region correlation (P5, Methods paragraph 7): Pearson r of every ROI pair over
  non-artifact timepoints, Fisher z, averaged within ToM, within Pain, across.
- Network timecourse (P6, Methods paragraph 9): z-normalized ROI timecourses averaged over the
  network's ROIs; the span of the z-normalization is reading O6 (TRs 11 to 168, or all).
- Reverse correlation (P7, Methods paragraph 9): one-tailed one-sample t-test against 0 at each
  TR from 11, events are runs of two or more significant TRs; the alpha is reading O5.
- Partial correlations: Spearman partial correlation as R's ppcor (Pearson partial correlation
  of the ranks, t test with n - 2 - k degrees of freedom); partial Kendall tau as ppcor
  (reading O8), its p from ppcor's normal approximation.
- Williams' test: Williams' T2 for two dependent correlations sharing one variable (Steiger
  1980, eq. 7), with its t on n - 3 degrees of freedom; Steiger's Z (eq. 14) is also given.
"""

from __future__ import annotations

import gzip
import io
from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache

import h5py
import nibabel as nib
import numpy as np
import pandas as pd
import requests
from scipy import stats

DATASET_ID = "ds000228"
SNAPSHOT = "1.1.1"
SNAPSHOT_DOI = "10.18112/openneuro.ds000228.v1.1.1"
GRAPHQL = "https://openneuro.org/crn/graphql"

N_TR = 168
TR_S = 2.0
FIRST_MOVIE_TR = 11          # README and Methods: TRs 1-5 rest, 6-10 logos, movie from TR 11
HIGHPASS_S = 100.0
N_COMPCOR = 5

TOM_ROIS = ["RTPJ", "LTPJ", "PC", "DMPFC", "MMPFC", "VMPFC"]
PAIN_ROIS = ["RS2", "LS2", "RInsula", "LInsula", "RMFG", "LMFG", "AMCC"]
FACE_ROIS = ["rSTS_masked", "lSTS", "rOFA", "lOFA", "rFFA", "lFFA"]
SCENE_ROIS = ["rRSC", "lRSC", "rTOS", "lTOS", "rPPA", "lPPA"]
M1_ROIS = ["right_primotor", "left_primotor"]
V1_ROIS = ["right_CS", "left_CS"]
FFA_ROIS = ["rFFA", "lFFA"]
NETWORKS = {"ToM": TOM_ROIS, "Pain": PAIN_ROIS, "Face": FACE_ROIS, "Scene": SCENE_ROIS,
            "M1": M1_ROIS, "V1": V1_ROIS}
ALL_ROIS = TOM_ROIS + PAIN_ROIS + FACE_ROIS + SCENE_ROIS + M1_ROIS + V1_ROIS


AGE_GROUPS = ["3yo", "4yo", "5yo", "7yo", "8-12yo"]

# Supplementary Table 3 (the paper's reference, not data): event, start time in the stimulus
# (m:ss), duration (s) and peak TR. The claims file (rc-events) reads the event's TRs as onset
# TR = stimulus seconds / 2 + 8, for duration / 2 TRs; with it every peak TR falls inside.
SUPP_TABLE3 = pd.DataFrame(
    [("T01", "4:00", 10, 131), ("T02", "2:46", 16, 96), ("T03", "1:14", 6, 46),
     ("T04", "4:42", 14, 150), ("T05", "1:28", 8, 54), ("T06", "3:48", 10, 124),
     ("T07", "1:50", 4, 64),
     ("P01", "3:36", 10, 118), ("P02", "2:06", 18, 73), ("P03", "3:20", 12, 111),
     ("P04", "1:00", 6, 39), ("P05", "1:34", 6, 56), ("P06", "4:10", 10, 135),
     ("P07", "5:02", 4, 160), ("P08", "0:42", 4, 29), ("P09", "4:28", 4, 143),
     ("P10", "1:20", 4, 49), ("P11", "2:30", 4, 84), ("P12", "3:04", 4, 100)],
    columns=["event", "time", "duration_s", "peak_tr"])
SUPP_TABLE3["network"] = np.where(SUPP_TABLE3.event.str[0] == "T", "ToM", "Pain")
SUPP_TABLE3["onset_tr"] = SUPP_TABLE3.time.map(
    lambda s: int(s.split(":")[0]) * 60 + int(s.split(":")[1])) // 2 + 8
SUPP_TABLE3["trs"] = [list(range(o, o + d // 2))
                      for o, d in zip(SUPP_TABLE3.onset_tr, SUPP_TABLE3.duration_s)]


def match_table_events(found_events, network: str) -> pd.Series:
    """For each Supplementary Table 3 event of a network, whether a found event overlaps it."""
    found = set(tr for e in found_events for tr in e)
    t = SUPP_TABLE3[SUPP_TABLE3.network == network]
    return pd.Series([bool(found & set(trs)) for trs in t.trs], index=t.event)


@lru_cache(maxsize=1)
def file_table() -> pd.DataFrame:
    """Every file of the snapshot: filename, size, annexed, id (checksum) and pinned url."""
    query = ('{ snapshot(datasetId: "%s", tag: "%s") { files(recursive: true) '
             '{ filename size annexed directory id urls } } }' % (DATASET_ID, SNAPSHOT))
    r = requests.post(GRAPHQL, json={"query": query}, timeout=300)
    r.raise_for_status()
    files = [f for f in r.json()["data"]["snapshot"]["files"] if not f["directory"]]
    df = pd.DataFrame(files).drop(columns="directory")
    df["url"] = df["urls"].str[0]
    return df.drop(columns="urls").set_index("filename")


def url(filename: str) -> str:
    return file_table().loc[filename, "url"]


def fetch(filename: str) -> bytes:
    for attempt in range(4):
        try:
            r = requests.get(url(filename), timeout=300)
            r.raise_for_status()
            return r.content
        except requests.RequestException:
            if attempt == 3:
                raise
    raise RuntimeError(filename)


def participants() -> pd.DataFrame:
    return pd.read_csv(io.BytesIO(fetch("participants.tsv")), sep="\t")


def text(filename: str) -> str:
    return fetch(filename).decode("utf-8", errors="replace")


def roi_mm(name: str) -> np.ndarray:
    """MNI mm coordinates (3 x n voxels) of a deposited ROI."""
    fn = f"derivatives/ROIs/{name}_9mm_sphere_xyz.mat" if name in TOM_ROIS + PAIN_ROIS \
        else f"derivatives/ROIs/{name}.mat"
    with h5py.File(io.BytesIO(fetch(fn)), "r") as h:
        return h["roi_XYZmm"][()] if "roi_XYZmm" in h else h["roi_xyz"][()]


@lru_cache(maxsize=1)
def all_roi_mm() -> dict:
    return {name: roi_mm(name) for name in ALL_ROIS}


def derivative(sub: str, suffix: str) -> str:
    return f"derivatives/preprocessed_data/{sub}/{sub}_{suffix}"


def nuisance(sub: str) -> tuple[np.ndarray, np.ndarray]:
    """(artifact indicators, n_artifacts x 168; CompCor regressors, 5 x 168) from matrix R."""
    with h5py.File(io.BytesIO(fetch(derivative(
            sub, "task-pixar_run-001_ART_and_CompCor_nuisance_regressors.mat"))), "r") as h:
        R = h["R"][()].astype(float)
    return R[:-N_COMPCOR], R[-N_COMPCOR:]


def extract_subject(sub: str) -> dict:
    """Raw ROI timecourses of one participant from its preprocessed (swrf) BOLD image.

    For each ROI: the mean over all its voxels, the mean over its voxels that hold data (no
    zero or non-finite value at any timepoint; reading O1c), and the count of such voxels.
    """
    raw = gzip.decompress(fetch(derivative(sub, "task-pixar_run-001_swrf_bold.nii.gz")))
    img = nib.Nifti1Image.from_bytes(raw)
    data = np.asanyarray(img.dataobj)
    inv = np.linalg.inv(img.affine)
    out = {"shape": img.shape, "zooms": img.header.get_zooms(), "affine": img.affine,
           "dtype": str(data.dtype)}
    rois = {}
    for name, mm in all_roi_mm().items():
        vox = np.rint(inv[:3, :3] @ mm + inv[:3, 3:4]).astype(int)
        inside = np.all((vox >= 0) & (vox < np.array(img.shape[:3])[:, None]), axis=0)
        ts = np.full((mm.shape[1], img.shape[3]), np.nan)
        ts[inside] = data[vox[0, inside], vox[1, inside], vox[2, inside], :].astype(float)
        good = np.all(np.isfinite(ts) & (ts != 0), axis=1)
        rois[name] = {"all": np.nanmean(ts, axis=0), "with_data": ts[good].mean(axis=0)
                      if good.any() else np.full(img.shape[3], np.nan),
                      "n_vox": mm.shape[1], "n_with_data": int(good.sum())}
    out["rois"] = rois
    out["artifacts"], out["compcor"] = nuisance(sub)
    return out


def extract_all(subjects, n_threads: int = 8) -> dict:
    all_roi_mm()
    with ThreadPoolExecutor(n_threads) as ex:
        return dict(zip(subjects, ex.map(extract_subject, subjects)))


# ---------------------------------------------------------------- timecourse preprocessing

def artifact_index(indicators: np.ndarray) -> np.ndarray:
    """0-based timepoints flagged by the ART indicator rows."""
    return np.sort(np.flatnonzero(indicators.sum(axis=0) > 0))


def nearest_neighbour_fill(ts: np.ndarray, bad: np.ndarray) -> np.ndarray:
    out = ts.copy()
    good = np.setdiff1d(np.arange(len(ts)), bad)
    for t in bad:
        out[t] = ts[good[np.argmin(np.abs(good - t))]]
    return out


def dct_highpass_basis(n: int = N_TR, tr: float = TR_S, cutoff: float = HIGHPASS_S) -> np.ndarray:
    """SPM's discrete cosine set for a high-pass cutoff (spm_filter), constant excluded."""
    order = int(np.fix(2 * (n * tr) / cutoff + 1))
    t = np.arange(n)
    return np.stack([np.sqrt(2 / n) * np.cos(np.pi * (2 * t + 1) * k / (2 * n))
                     for k in range(1, order)], axis=1)


def residualize(y: np.ndarray, X: np.ndarray) -> np.ndarray:
    X = np.column_stack([np.ones(len(y)), X])
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    return y - X @ beta


def clean(ts: np.ndarray, indicators: np.ndarray, compcor: np.ndarray, extra=None,
          single_artifact_regressor: bool = False) -> np.ndarray:
    """P4: interpolate over artifacts, regress nuisance, high-pass, NaN the artifacts."""
    bad = artifact_index(indicators)
    y = nearest_neighbour_fill(ts, bad) if len(bad) else ts.copy()
    art = indicators.T if not single_artifact_regressor else indicators.sum(axis=0)[:, None]
    parts = [compcor.T] + ([art] if len(bad) else [])
    if extra is not None:
        parts.append(np.asarray(extra).reshape(len(ts), -1))
    y = residualize(y, np.column_stack(parts))
    hp = dct_highpass_basis(len(ts))
    y = y - hp @ np.linalg.lstsq(hp, y, rcond=None)[0]
    y[bad] = np.nan
    return y


def subject_timecourses(sub_data: dict, rois, voxels: str = "with_data", m1: bool = False,
                        single_artifact_regressor: bool = False) -> dict:
    """Cleaned timecourse of each ROI; with m1=True the bilateral M1 raw mean is regressed out."""
    extra = None
    if m1:
        r, l = sub_data["rois"]["right_primotor"], sub_data["rois"]["left_primotor"]
        extra = (r[voxels] * r["n_with_data" if voxels == "with_data" else "n_vox"]
                 + l[voxels] * l["n_with_data" if voxels == "with_data" else "n_vox"]) / (
            r["n_with_data" if voxels == "with_data" else "n_vox"]
            + l["n_with_data" if voxels == "with_data" else "n_vox"])
    return {name: clean(sub_data["rois"][name][voxels], sub_data["artifacts"],
                        sub_data["compcor"], extra, single_artifact_regressor)
            for name in rois}


# ---------------------------------------------------------------- inter-region correlation

def fisher_corr(a: np.ndarray, b: np.ndarray, trs=None) -> float:
    ok = np.isfinite(a) & np.isfinite(b)
    if trs is not None:
        ok &= np.isin(np.arange(len(a)), trs)
    return float(np.arctanh(np.corrcoef(a[ok], b[ok])[0, 1]))


def irc_matrix(tcs: dict, rois, trs=None) -> pd.DataFrame:
    """Fisher z of the Pearson correlation of every ROI pair, over timepoints where all are
    finite (the artifact timepoints are NaN in every ROI) and, if given, within `trs`."""
    X = np.stack([tcs[r] for r in rois])
    ok = np.all(np.isfinite(X), axis=0)
    if trs is not None:
        ok &= np.isin(np.arange(X.shape[1]), trs)
    with np.errstate(divide="ignore"):
        z = np.arctanh(np.corrcoef(X[:, ok]))
    np.fill_diagonal(z, np.nan)
    return pd.DataFrame(z, index=rois, columns=rois)


def within(m: pd.DataFrame, rois, exclude_pairs=()) -> float:
    vals = [m.loc[a, b] for i, a in enumerate(rois) for b in rois[i + 1:]
            if {a, b} not in [set(p) for p in exclude_pairs]]
    return float(np.mean(vals))


def across(m: pd.DataFrame, rois_a, rois_b) -> float:
    return float(np.mean([m.loc[a, b] for a in rois_a for b in rois_b]))


# ---------------------------------------------------------------- network timecourses

def network_timecourse(tcs: dict, rois, z_span: str = "movie", z: bool = True) -> np.ndarray:
    """P6: each ROI timecourse z-normalized (over TRs 11-168, 'movie', or all 168, 'all';
    artifact NaNs left out), then averaged over the network's ROIs."""
    span = np.arange(FIRST_MOVIE_TR - 1, N_TR) if z_span == "movie" else np.arange(N_TR)
    out = []
    for r in rois:
        x = tcs[r].copy()
        if z:
            x = (x - np.nanmean(x[span])) / np.nanstd(x[span], ddof=1)
        out.append(x)
    return np.mean(out, axis=0)


def reverse_correlation(group_tcs: np.ndarray, alpha: float, fdr: bool = False):
    """P7. group_tcs: participants x 168. Returns per-TR (1-based TR, mean, t, p, significant)
    from TR 11, and the events as lists of 1-based TRs."""
    trs = np.arange(FIRST_MOVIE_TR, N_TR + 1)
    x = group_tcs[:, trs - 1]
    t, p = stats.ttest_1samp(x, 0, axis=0, nan_policy="omit", alternative="greater")
    t, p = np.asarray(t), np.asarray(p)
    if fdr:
        sig = stats.false_discovery_control(p) < alpha
    else:
        sig = p < alpha
    table = pd.DataFrame({"TR": trs, "mean": np.nanmean(x, axis=0), "t": t, "p": p, "sig": sig})
    events, run = [], []
    for tr, s in zip(trs, sig):
        if s:
            run.append(tr)
        else:
            if len(run) >= 2:
                events.append(run)
            run = []
    if len(run) >= 2:
        events.append(run)
    return table, events


def rank_events(events, table: pd.DataFrame):
    """Events ranked by the mean at their peak TR, highest first, with the peak TR."""
    mean = table.set_index("TR")["mean"]
    rows = [{"trs": e, "onset": e[0], "length_tr": len(e),
             "peak_tr": int(mean.loc[e].idxmax()), "peak_mean": float(mean.loc[e].max())}
            for e in events]
    return pd.DataFrame(rows).sort_values("peak_mean", ascending=False).reset_index(drop=True)


def overlap_permutation(lengths_a, lengths_b, zeros_a: int, zeros_b: int, n_perm: int,
                        rng: np.random.Generator) -> np.ndarray:
    """Methods paragraph 10: random timecourses with the same events in random order and a
    random split of the zeros between them (at least one between events). Returns the overlap
    (timepoints in both) of each permutation."""
    def one(lengths, n_zeros):
        lengths = rng.permutation(lengths)
        k = len(lengths)
        gaps = np.zeros(k + 1, int)
        gaps[1:k] = 1
        rest = n_zeros - (k - 1)
        gaps += rng.multinomial(rest, np.ones(k + 1) / (k + 1))
        seq = []
        for g, L in zip(gaps[:-1], lengths):
            seq += [0] * g + [1] * L
        seq += [0] * gaps[-1]
        return np.array(seq, bool)
    out = np.empty(n_perm, int)
    for i in range(n_perm):
        a, b = one(lengths_a, zeros_a), one(lengths_b, zeros_b)
        n = min(len(a), len(b))
        out[i] = int((a[:n] & b[:n]).sum())
    return out


# ---------------------------------------------------------------- statistics

def _resid(y, Z):
    return residualize(np.asarray(y, float), np.asarray(Z, float).reshape(len(y), -1))


def partial_spearman(x, y, covars) -> tuple[float, float, int]:
    """ppcor::pcor.test(method='spearman'): Pearson partial correlation of ranks."""
    x, y = stats.rankdata(x), stats.rankdata(y)
    Z = np.column_stack([stats.rankdata(c) for c in np.atleast_2d(np.asarray(covars).T)
                         ]) if np.ndim(covars) > 1 else stats.rankdata(covars)[:, None]
    r = np.corrcoef(_resid(x, Z), _resid(y, Z))[0, 1]
    n, k = len(x), Z.shape[1]
    df = n - 2 - k
    t = r * np.sqrt(df / (1 - r ** 2))
    return float(r), float(2 * stats.t.sf(abs(t), df)), df


def kendall(x, y) -> tuple[float, float]:
    res = stats.kendalltau(x, y, variant="b", method="asymptotic")
    return float(res.statistic), float(res.pvalue)


def partial_kendall(x, y, z) -> tuple[float, float]:
    """ppcor::pcor.test(method='kendall') with one covariate (reading O8)."""
    txy, tyz, txz = kendall(x, y)[0], kendall(y, z)[0], kendall(x, z)[0]
    r = (txy - txz * tyz) / np.sqrt((1 - txz ** 2) * (1 - tyz ** 2))
    n, gp = len(x), 1
    stat = r / np.sqrt(2 * (2 * (n - gp) + 5) / (9 * (n - gp) * (n - 1 - gp)))
    return float(r), float(2 * stats.norm.sf(abs(stat)))


def williams(r12: float, r13: float, r23: float, n: int) -> dict:
    """Difference of r12 and r13 (variable 1 shared). Williams' T2 and Steiger's Z."""
    detR = 1 - r12 ** 2 - r13 ** 2 - r23 ** 2 + 2 * r12 * r13 * r23
    rbar = (r12 + r13) / 2
    t2 = (r12 - r13) * np.sqrt((n - 1) * (1 + r23) / (
        2 * (n - 1) / (n - 3) * detR + rbar ** 2 * (1 - r23) ** 3))
    psi = r23 * (1 - 2 * rbar ** 2) - 0.5 * rbar ** 2 * (1 - 2 * rbar ** 2 - r23 ** 2)
    c = psi / (1 - rbar ** 2) ** 2
    z = (np.arctanh(r12) - np.arctanh(r13)) * np.sqrt(n - 3) / np.sqrt(2 - 2 * c)
    return {"t": float(t2), "p_t": float(2 * stats.t.sf(abs(t2), n - 3)),
            "z": float(z), "p_z": float(2 * stats.norm.sf(abs(z)))}


def ols(df: pd.DataFrame, y: str, xs, zscore: bool = False):
    """Ordinary least squares; with zscore=True the outcome and continuous predictors are
    z-scored (reading O4a). Returns the statsmodels result."""
    import statsmodels.api as sm
    d = df[[y] + list(xs)].dropna().astype(float)
    if zscore:
        for c in [y] + list(xs):
            if d[c].nunique() > 2:
                d[c] = (d[c] - d[c].mean()) / d[c].std(ddof=1)
    return sm.OLS(d[y], sm.add_constant(d[list(xs)])).fit()
