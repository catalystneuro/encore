"""Loading and measures for dandiset 000054 (Plitt & Giocomo 2021, Nature Neuroscience 24, 705-714).

Each NWB file is one imaging session of one mouse: the deconvolved activity of every Suite2P cell
(`processing/ophys/deconvolved activity`), the VR behaviour aligned to the imaging frames
(`processing/behavior/2P-aligned behavior`: position, speed, licks, reward, morph value, the three
jitters, trial number, trial start and teleport flags) and a JSON annotation
(`acquisition/trial_data`) with per-trial information and the place cells of the authors' 2026
code. Files are streamed from the archive at the pinned version; nothing is written to disk.

Where the parameters come from. M1 to M12 are the common methods in the opening comment of the
claims file, `claims/000054/10.1038-s41593-021-00816-6.yaml`, which cite the paper's Methods or its
code (https://github.com/GiocomoLab/PlittGiocomo_2021, commit dca5a57):

- Position bins, 10 cm from 0 to 450 cm (M3, Methods). Frames below 2 cm/s are left out of the trial
  matrices (M3, the code's speed_thr); place cells run with and without this exclusion (M3 a, b).
- Signal, the deconvolved activity (M2); the file's normalised series (each cell divided by its
  99th percentile, the 2026 code) is the variant.
- Smoothing, Gaussian of s.d. 2 bins along position (M5). Bins with no frames are handled by
  normalised convolution and then set to 0 (a standard choice; the claims file does not say).
- Spatial information as the code computes it (place-cell-fractions criterion,
  PlaceCellAnalysis.spatial_info): map minus its minimum over all cells and bins, plus 0.001,
  divided by its mean over bins, then sum of p log2 p weighted by occupancy. Null from 1,000
  shuffles circularly shifting activity against position within every trial; place cell when the
  fraction of shuffles with SI at least the real one is at most 0.05 (criterion).
- Stimulus axis, f_h, and the rescaled unit `wallmorphx` of the code (M6, UnityTransforms.py), on
  a grid of 1,000 points from -0.3 to 1.3 units.
- Priors from the trials before session 8 with a kernel exp(-d^2/0.1^2) in units (M7), likelihood
  of variance 8.23 f_h^2 (M8, Methods; the code widths 0.3 and 0.4 units are variants).
- SF (M9), Q with a kernel exp(-d^2/0.1^2) on both axes and the affine map to 10.86 and 37.715 f_h
  (M10), Delta D_KL over rows 0.1 to 1.1 units in bits (M11), mouse permutation test (M12).
"""

from __future__ import annotations

import itertools
import json
import re
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
from numba import njit, prange
from scipy.ndimage import gaussian_filter1d

DANDISET_ID = "000054"
DANDISET_VERSION = "0.260415.1712"

N_BINS = 45            # M3: 10 cm bins over 450 cm
BIN_CM = 10.0
SPEED_THR = 2.0        # M3: cm/s, the code's speed_thr
SMOOTH_SIGMA = 2.0     # M5: bins
N_SHUFFLES = 1000      # place-cell-fractions criterion
P_THR = 0.05
MORPHS = np.array([0.0, 0.25, 0.5, 0.75, 1.0])
GROUP_OF = {"R": "rare", "F": "frequent", "FD": "decision"}

BEHAVIOR = "processing/behavior/2P-aligned behavior"
DECONV = "processing/ophys/deconvolved activity/deconvolved activity/data"
NORM_ROWS = (10000, 10100)
NORM_DECONV = "processing/ophys/normalized deconvolved activity/normalized deconvolved activity/data"


# ----------------------------------------------------------------------------- listing and loading
def asset_table() -> pd.DataFrame:
    """Every NWB file at the pinned version, with mouse, group, session kind, day and part."""
    from dandi.dandiapi import DandiAPIClient

    rows = []
    with DandiAPIClient() as client:
        ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        for a in ds.get_assets():
            m = re.match(r"sub-(\w+?)/sub-\w+?_ses-(training|testing)-day(\d+)(?:-(\d+))?_", a.path)
            if not m:
                continue
            mouse = m.group(1)
            rows.append(dict(path=a.path, mouse=mouse, group=GROUP_OF[re.sub(r"\d", "", mouse)],
                             kind=m.group(2), day=int(m.group(3)), part=int(m.group(4) or 1),
                             size=a.size,
                             url=a.get_content_url(follow_redirects=1, strip_query=True)))
    return pd.DataFrame(rows).sort_values(["group", "mouse", "day", "part"]).reset_index(drop=True)


def _text(x):
    x = x[()]
    if isinstance(x, np.ndarray):
        x = x.ravel()[0]
    return x.decode() if isinstance(x, bytes) else str(x)


def read_file(url: str, neural: bool = True) -> dict:
    """Behaviour, trial annotation and (optionally) deconvolved activity of one file."""
    with h5py.File(remfile.File(url), "r") as f:
        b = f[BEHAVIOR]
        beh = {k: b[k]["data"][:] for k in b}
        ts = b["position/timestamps"][:]
        same_ts = all(np.array_equal(b[k]["timestamps"][:], ts) for k in b)
        units = {k: b[k]["data"].attrs.get("unit") for k in b}
        info = json.loads(f["acquisition/trial_data/data"][0])
        d = f[DECONV]
        out = dict(beh=beh, ts=ts, same_ts=same_ts, units=units, info=info,
                   shape=d.shape,
                   rate=float(f["processing/ophys/deconvolved activity/deconvolved activity/"
                                "starting_time"].attrs["rate"]),
                   imaging_rate=float(f["general/optophysiology/ImagingPlane/imaging_rate"][()]),
                   subject={k: _text(f["general/subject"][k]) for k in f["general/subject"]},
                   session_id=_text(f["general/session_id"]),
                   description=_text(f["general/experiment_description"]),
                   start_time=_text(f["session_start_time"]))
        out["fingerprint"] = float(np.asarray(d[1000:1010, :], np.float64).sum())
        if neural:
            # The series is stored contiguous and uncompressed; read its bytes with parallel range
            # requests into memory (nothing is written to disk), or through h5py otherwise.
            if d.chunks is None and d.compression is None:
                out["act"] = _read_contiguous(url, d.id.get_offset(), d.shape, d.dtype)
                out["act_check"] = d[500:503, :]
            else:
                out["act"] = d[:]
            # a block of the file's normalised series, to check its description
            out["norm_block"] = f[NORM_DECONV][NORM_ROWS[0]:NORM_ROWS[1], :]
    return out


def _read_contiguous(url, offset, shape, dtype, part=8 * 2**20, workers=16):
    import requests

    nbytes = int(np.prod(shape)) * np.dtype(dtype).itemsize
    buf = bytearray(nbytes)
    starts = list(range(0, nbytes, part))

    def get(s):
        e = min(s + part, nbytes) - 1
        for attempt in range(5):
            try:
                r = requests.get(url, headers={"Range": f"bytes={offset + s}-{offset + e}"}, timeout=120)
                r.raise_for_status()
                buf[s:e + 1] = r.content
                return
            except Exception:
                if attempt == 4:
                    raise

    with ThreadPoolExecutor(workers) as ex:
        list(ex.map(get, starts))
    return np.frombuffer(bytes(buf), dtype=dtype).reshape(shape)


def trial_table(raw: dict) -> pd.DataFrame:
    """One row per trial from the JSON annotation, checked against the behaviour series."""
    ti = raw["info"]["trial_info"]
    st = np.asarray(raw["info"]["trial_start_inds"])
    tp = np.asarray(raw["info"]["teleport_inds"])
    df = pd.DataFrame(dict(start=st, stop=tp, morph=np.asarray(ti["morphs"], float),
                           wall=np.asarray(ti["wallJitter"], float),
                           tower=np.asarray(ti["towerJitter"], float),
                           background=np.asarray(ti["bckgndJitter"], float),
                           reward_pos=np.asarray(ti["reward_pos"], float),
                           omission=np.asarray(ti["omissions"], float),
                           rewarded=np.asarray(ti["rewards"], float),
                           effective_morph=np.asarray(ti["effective_morph"], float)))
    df["S"] = df["morph"] + df["wall"]              # M4: S is S-tilde plus the wall jitter
    df["fh"] = xfreq(df["S"].to_numpy())
    df["unit"] = wallmorphx(df["S"].to_numpy())
    return df


# ----------------------------------------------------------------------------- stimulus axis (M6)
def getf(s):
    return s * 2.5 + (1 - s) * 3.5


def gettheta(s):
    return (s * 60.0 + (1 - s) * 10.0) * np.pi / 180


def xfreq(s):
    """f_h, the horizontal component of wall frequency (UnityTransforms.xfreq)."""
    s = np.asarray(s, float)
    return np.abs(getf(s) * 1500 / 120 * (np.cos(gettheta(s) + np.pi / 4) - np.sin(gettheta(s) + np.pi / 4)))


_X0, _X1 = float(xfreq(-0.1)), float(xfreq(1.1))
UNIT_FH = (_X1 - _X0) / 1.2       # f_h per unit


def wallmorphx(s):
    """S to the code's rescaled unit, linear in f_h (UnityTransforms.wallmorphx)."""
    return 1.2 * (xfreq(s) - _X0) / (_X1 - _X0) - 0.1


def fh_to_unit(fh):
    return (np.asarray(fh, float) - _X0) / UNIT_FH - 0.1


def unit_to_fh(u):
    return (np.asarray(u, float) + 0.1) * UNIT_FH + _X0


GRID = np.linspace(-0.3, 1.3, 1000)                   # M6
LIK_SD_FH = np.sqrt(8.23)                             # M8, Methods: variance 8.23 f_h^2
LIKELIHOODS = {"methods var 8.23": ("gauss_sd", LIK_SD_FH / UNIT_FH),
               "code 0.3 units": ("exp_sigma", 0.3),
               "code 0.4 units": ("exp_sigma", 0.4)}
KDE_SIGMA = 0.1                                      # M7, M10: exp(-d^2/0.1^2) in units
ROWS = (GRID >= 0.1) & (GRID <= 1.1)                 # M11


def kernel(d, kind, w):
    if kind == "gauss_sd":
        return np.exp(-0.5 * (d / w) ** 2)
    return np.exp(-(d / w) ** 2)


def prior_from_units(units: np.ndarray) -> np.ndarray:
    """M7: normalised smoothed histogram of the trials' stimulus values on the grid."""
    h = np.exp(-((GRID[:, None] - np.asarray(units)[None, :]) / KDE_SIGMA) ** 2).sum(1)
    return h / h.sum()


def group_prior(mouse_priors) -> np.ndarray:
    """M7: mean of the mouse priors, renormalised."""
    p = np.mean(np.vstack(list(mouse_priors)), axis=0)
    return p / p.sum()


def likelihood_matrix(lik: str = "methods var 8.23") -> np.ndarray:
    """L[i, j] = P(fhat = GRID[i] | f = GRID[j]), unnormalised Gaussian in the observation."""
    kind, w = LIKELIHOODS[lik]
    return kernel(GRID[:, None] - GRID[None, :], kind, w)


def posterior(prior: np.ndarray, lik: str = "methods var 8.23") -> np.ndarray:
    """M8: rows fhat, columns f; each row normalised over f."""
    p = likelihood_matrix(lik) * prior[None, :]
    return p / p.sum(1, keepdims=True)


def map_estimate(post: np.ndarray, units_obs: np.ndarray) -> np.ndarray:
    """Argmax over f of the posterior at the grid row nearest each observed value (units)."""
    rows = np.abs(GRID[None, :] - np.asarray(units_obs)[:, None]).argmin(1)
    return GRID[post[rows].argmax(1)]


MAP_ANCHORS_FH = (10.86, 37.715)      # M10: means of the paper's MAP estimates


def transform_sf(sf: np.ndarray, morph: np.ndarray, anchors_fh=MAP_ANCHORS_FH) -> np.ndarray:
    """M10: affine map of SF so the S-tilde = 0 and 1 medians go to the anchors; units, clipped."""
    a0, a1 = fh_to_unit(anchors_fh[0]), fh_to_unit(anchors_fh[1])
    m0, m1 = np.nanmedian(sf[morph == 0]), np.nanmedian(sf[morph == 1])
    t = (sf - m0) / (m1 - m0) * (a1 - a0) + a0
    return np.clip(t, GRID[0], GRID[-1])


def q_unnorm(t_units: np.ndarray, fhat_units: np.ndarray) -> np.ndarray:
    """M10: sum over trials of a 2D Gaussian at (fhat, transformed SF); rows fhat, columns f."""
    ok = np.isfinite(t_units) & np.isfinite(fhat_units)
    kf = np.exp(-((GRID[:, None] - t_units[ok][None, :]) / KDE_SIGMA) ** 2)
    kh = np.exp(-((GRID[:, None] - fhat_units[ok][None, :]) / KDE_SIGMA) ** 2)
    return kh @ kf.T


def normalise_rows(q: np.ndarray) -> np.ndarray:
    return q / q.sum(1, keepdims=True)


def dkl_rows(p: np.ndarray, q: np.ndarray) -> tuple[np.ndarray, int]:
    """Row-wise D_KL(P || Q) in bits; grid points with Q = 0 and P > 0 are left out (M11)."""
    bad = (q <= 0) & (p > 0)
    with np.errstate(divide="ignore", invalid="ignore"):
        terms = np.where((p > 0) & ~bad, p * np.log2(p / q), 0.0)
    return terms.sum(1), int(bad.sum())


def delta_dkl(q: np.ndarray, post_rare: np.ndarray, post_freq: np.ndarray) -> float:
    """M11: mean over rows 0.1 to 1.1 units of D_KL(P_rare||Q) - D_KL(P_freq||Q)."""
    dr, _ = dkl_rows(post_rare[ROWS], q[ROWS])
    df, _ = dkl_rows(post_freq[ROWS], q[ROWS])
    return float(np.mean(dr - df))


def mean_dkl(q: np.ndarray, post: np.ndarray) -> float:
    d, _ = dkl_rows(post[ROWS], q[ROWS])
    return float(np.mean(d))


def reconstruct_prior(qu: np.ndarray, lik: str = "methods var 8.23") -> np.ndarray:
    """fig6d criterion: R(f) = sum_fhat Q(f|fhat) / sum_fhat L(fhat|f)/Z(fhat), normalised."""
    z = qu.sum(1)
    q = qu / z[:, None]
    lik_m = likelihood_matrix(lik)
    r = q.sum(0) / (lik_m / z[:, None]).sum(0)
    return r / r.sum()


def dkl(p: np.ndarray, q: np.ndarray) -> float:
    d, _ = dkl_rows(p[None, :], q[None, :])
    return float(d[0])


# ----------------------------------------------------------------------------- mouse permutations (M12)
def mouse_permutation(values: dict, rare: list, freq: list):
    """M12: observed rare minus frequent difference of across-mouse means, and the 923 others.

    `values` maps mouse to a scalar or an array; the permutations keep 6 mice per group."""
    mice = list(rare) + list(freq)
    arr = np.array([np.asarray(values[m], float) for m in mice])
    obs = arr[: len(rare)].mean(0) - arr[len(rare):].mean(0)
    perms = []
    for combo in itertools.combinations(range(len(mice)), len(rare)):
        if set(combo) == set(range(len(rare))):
            continue
        mask = np.zeros(len(mice), bool)
        mask[list(combo)] = True
        perms.append(arr[mask].mean(0) - arr[~mask].mean(0))
    perms = np.array(perms)
    return obs, perms


def outside_range(obs, perms):
    """'P < 0.0011': the observed difference lies outside the range of all permutations."""
    return (obs > perms.max(0)) | (obs < perms.min(0))


def outside_95(obs, perms):
    """'P < 0.05, two-sided': outside the 2.5 to 97.5 percentiles of the permutations."""
    lo, hi = np.percentile(perms, [2.5, 97.5], axis=0)
    return (obs > hi) | (obs < lo)


# ----------------------------------------------------------------------------- binning and place cells
def frame_layout(raw: dict, trials: pd.DataFrame):
    """In-trial frames concatenated: their source index, bin, speed flag and trial offsets."""
    pos = raw["beh"]["position"]
    speed = raw["beh"]["speed"]
    idx, offs = [], [0]
    for s, e in zip(trials["start"], trials["stop"]):
        idx.append(np.arange(s, e))
        offs.append(offs[-1] + e - s)
    idx = np.concatenate(idx)
    p = pos[idx]
    b = np.floor(p / BIN_CM).astype(np.int64)
    b[(p < 0) | (p > N_BINS * BIN_CM)] = -1
    b[b == N_BINS] = N_BINS - 1
    keep_a = (speed[idx] >= SPEED_THR)
    return idx, b, keep_a, np.asarray(offs, np.int64)


def trial_matrix(act: np.ndarray, frame_idx, bins, keep, offsets) -> tuple[np.ndarray, np.ndarray]:
    """Trials x bins x cells mean activity, and trials x bins occupancy (frames); NaN where empty."""
    n_tr = len(offsets) - 1
    tr = np.repeat(np.arange(n_tr), np.diff(offsets))
    ok = (bins >= 0) & keep
    code = tr[ok] * N_BINS + bins[ok]
    occ = np.bincount(code, minlength=n_tr * N_BINS).astype(float)
    from scipy.sparse import csr_matrix
    m = csr_matrix((np.ones(ok.sum()), (code, np.arange(ok.sum()))), shape=(n_tr * N_BINS, ok.sum()))
    sums = m @ act[frame_idx[ok]].astype(np.float64)
    with np.errstate(invalid="ignore", divide="ignore"):
        tm = sums / occ[:, None]
    tm[occ == 0] = np.nan
    return tm.reshape(n_tr, N_BINS, -1), occ.reshape(n_tr, N_BINS)


def spatial_info(fmap: np.ndarray, occ: np.ndarray) -> np.ndarray:
    """The code's spatial_info: fmap bins x cells, occ bins (fractions). Empty bins left out."""
    ok = np.isfinite(fmap).all(1) & (occ > 0)
    p = fmap[ok] - np.min(fmap[ok]) + 0.001
    p = p / p.mean(0)
    o = occ[ok] / occ[ok].sum()
    return ((p * o[:, None]) * np.log2(p)).sum(0)


@njit(parallel=True, cache=True)
def _shuffle_counts(actT, offsets, run_off, run_t0, run_t1, run_bin, run_keep, morph_idx,
                    occ_a, occ_b, occf_a, occf_b, si_a, si_b, gmin_a, gmin_b, shifts,
                    n_morph, n_bins, stop):
    """Counts of shuffles with SI at least the real SI, per cell and morph, for both readings.

    Frames of a trial are grouped in runs of constant bin and speed flag; the shifted activity
    summed over a run is read from the cumulative sum of the trial's trace laid out twice.
    occf_* are the per-morph occupancy fractions (0 where a bin is empty). A cell stops once every
    morph and reading has more than `stop` exceedances; its decision (count at most `stop`) is
    then the same as after all shuffles."""
    n_cells = actT.shape[0]
    n_tr = offsets.shape[0] - 1
    n_sh = shifts.shape[0]
    cnt = np.zeros((2, n_cells, n_morph), np.int32)
    done = np.zeros(n_cells, np.int32)
    tot_len = 0
    for r in range(n_tr):
        tot_len += 2 * (offsets[r + 1] - offsets[r]) + 1
    for c in prange(n_cells):
        cs = np.zeros(tot_len)
        cs_off = np.zeros(n_tr, np.int64)
        p = 0
        for r in range(n_tr):
            o = offsets[r]
            T = offsets[r + 1] - o
            cs_off[r] = p
            cs[p] = 0.0
            for j in range(2 * T):
                jj = j if j < T else j - T
                cs[p + j + 1] = cs[p + j] + actT[c, o + jj]
            p += 2 * T + 1
        acc = np.zeros((2, n_morph, n_bins))
        num = np.zeros((2, n_morph, n_bins))
        sa = np.zeros(n_bins)
        sb = np.zeros(n_bins)
        for s in range(n_sh):
            acc[:] = 0.0
            num[:] = 0.0
            for r in range(n_tr):
                m = morph_idx[r]
                if m < 0:
                    continue
                T = offsets[r + 1] - offsets[r]
                k = shifts[s, r] % T
                base = cs_off[r] + k
                sa[:] = 0.0
                sb[:] = 0.0
                for q in range(run_off[r], run_off[r + 1]):
                    v = cs[base + run_t1[q]] - cs[base + run_t0[q]]
                    bb = run_bin[q]
                    sb[bb] += v
                    if run_keep[q]:
                        sa[bb] += v
                for bb in range(n_bins):
                    if occ_a[r, bb] > 0:
                        acc[0, m, bb] += sa[bb] / occ_a[r, bb]
                        num[0, m, bb] += 1.0
                    if occ_b[r, bb] > 0:
                        acc[1, m, bb] += sb[bb] / occ_b[r, bb]
                        num[1, m, bb] += 1.0
            alldone = True
            for g in range(2):
                for m in range(n_morph):
                    gmin = gmin_a[m] if g == 0 else gmin_b[m]
                    tot = 0.0
                    nv = 0
                    for bb in range(n_bins):
                        of = occf_a[m, bb] if g == 0 else occf_b[m, bb]
                        if of > 0:
                            tot += acc[g, m, bb] / num[g, m, bb] - gmin + 0.001
                            nv += 1
                    if nv == 0:
                        continue
                    mean = tot / nv
                    si = 0.0
                    for bb in range(n_bins):
                        of = occf_a[m, bb] if g == 0 else occf_b[m, bb]
                        if of > 0:
                            pv = (acc[g, m, bb] / num[g, m, bb] - gmin + 0.001) / mean
                            si += pv * of * np.log2(pv)
                    real = si_a[c, m] if g == 0 else si_b[c, m]
                    if si >= real:
                        cnt[g, c, m] += 1
                    if cnt[g, c, m] <= stop:
                        alldone = False
            done[c] = s + 1
            if alldone:
                break
    return cnt, done


def _runs(bins, keep_a, offsets):
    """Runs of frames with the same bin and speed flag within each trial (bin -1 left out)."""
    t0, t1, rb, rk, roff = [], [], [], [], [0]
    for r in range(len(offsets) - 1):
        o, e = offsets[r], offsets[r + 1]
        key = bins[o:e] * 2 + keep_a[o:e]
        starts = np.r_[0, np.nonzero(key[1:] != key[:-1])[0] + 1]
        ends = np.r_[starts[1:], e - o]
        good = bins[o:e][starts] >= 0
        t0.append(starts[good]); t1.append(ends[good])
        rb.append(bins[o:e][starts[good]]); rk.append(keep_a[o:e][starts[good]])
        roff.append(roff[-1] + good.sum())
    return (np.asarray(roff, np.int64), np.concatenate(t0).astype(np.int64),
            np.concatenate(t1).astype(np.int64), np.concatenate(rb).astype(np.int64),
            np.concatenate(rk).astype(np.bool_))


def place_cells(act, frame_idx, bins, keep_a, offsets, morph, seed, n_shuffles=N_SHUFFLES):
    """Place cells per S-tilde for reading (a) speed below 2 cm/s excluded and (b) no exclusion.

    Returns per reading: SI (5 x cells), the exceedance count, the shuffles run, the mask, the
    trial-averaged maps (5 x bins x cells) and the occupancy fractions, plus the global minima."""
    n_tr = len(offsets) - 1
    morph_idx = np.array([int(np.where(np.isclose(MORPHS, m))[0][0]) if np.any(np.isclose(MORPHS, m))
                          else -1 for m in morph], np.int64)
    out = {}
    real = {}
    for g, keep in (("a", keep_a), ("b", np.ones_like(keep_a))):
        tm, occ = trial_matrix(act, frame_idx, bins, keep, offsets)
        maps = np.full((len(MORPHS), N_BINS, tm.shape[2]), np.nan)
        occf = np.zeros((len(MORPHS), N_BINS))
        for i in range(len(MORPHS)):
            sel = morph_idx == i
            if sel.sum() == 0:
                continue
            maps[i] = np.nanmean(tm[sel], axis=0)
            o = occ[sel].sum(0)
            o[~np.isfinite(maps[i]).all(1)] = 0
            occf[i] = o / o.sum()
        gmin = np.array([np.nanmin(maps[i]) if np.isfinite(maps[i]).any() else 0.0 for i in range(len(MORPHS))])
        si = np.vstack([spatial_info(maps[i], occf[i]) if occf[i].sum() > 0 else np.full(tm.shape[2], np.nan)
                        for i in range(len(MORPHS))])
        real[g] = dict(tm_occ=occ, maps=maps, occf=occf, gmin=gmin, si=si)
    rng = np.random.default_rng(seed)
    lens = np.diff(offsets)
    shifts = (rng.random((n_shuffles, n_tr)) * lens[None, :]).astype(np.int64)
    actT = np.ascontiguousarray(act[frame_idx].T.astype(np.float64))
    run_off, run_t0, run_t1, run_bin, run_keep = _runs(bins, keep_a, offsets)
    cnt, done = _shuffle_counts(actT, offsets, run_off, run_t0, run_t1, run_bin, run_keep,
                                morph_idx, real["a"]["tm_occ"], real["b"]["tm_occ"], real["a"]["occf"], real["b"]["occf"],
                                np.nan_to_num(real["a"]["si"].T, nan=np.inf),
                                np.nan_to_num(real["b"]["si"].T, nan=np.inf),
                                real["a"]["gmin"], real["b"]["gmin"], shifts, len(MORPHS), N_BINS,
                                int(np.floor(P_THR * n_shuffles)))
    for gi, g in enumerate(("a", "b")):
        c = cnt[gi].T
        out[g] = dict(si=real[g]["si"], count=c, mask=(c <= np.floor(P_THR * n_shuffles)) & np.isfinite(real[g]["si"]),
                      maps=real[g]["maps"], occf=real[g]["occf"], gmin=real[g]["gmin"])
    out["shuffles_run"] = done
    return out


# ----------------------------------------------------------------------------- per-session measures
def nan_smooth(tm: np.ndarray, sigma: float = SMOOTH_SIGMA) -> np.ndarray:
    """Gaussian smoothing along position (axis 1) by normalised convolution; empty bins then 0."""
    ok = np.isfinite(tm)
    num = gaussian_filter1d(np.where(ok, tm, 0.0), sigma, axis=1)
    den = gaussian_filter1d(ok.astype(float), sigma, axis=1)
    with np.errstate(invalid="ignore", divide="ignore"):
        out = num / den
    return np.nan_to_num(out, nan=0.0)


def unit_rows(x: np.ndarray) -> np.ndarray:
    n = np.linalg.norm(x, axis=-1, keepdims=True)
    with np.errstate(invalid="ignore", divide="ignore"):
        return np.nan_to_num(x / n, nan=0.0)


def binned_similarity(C: np.ndarray, morph: np.ndarray) -> np.ndarray:
    """Mean of C over trial pairs binned by S-tilde, diagonal entries left out (5 x 5)."""
    E = (np.asarray(morph)[:, None] == MORPHS[None, :]).astype(float)
    num = E.T @ (C - np.diag(np.diag(C))) @ E
    n = E.sum(0)
    cnt = np.outer(n, n) - np.diag(n)
    with np.errstate(invalid="ignore", divide="ignore"):
        return np.where(cnt > 0, num / np.where(cnt > 0, cnt, 1), np.nan)


def zscore_matrix(B: np.ndarray) -> np.ndarray:
    return (B - np.nanmean(B)) / np.nanstd(B)


def similarity_fraction(A: np.ndarray, morph: np.ndarray) -> np.ndarray:
    """M9: SF of each row of A against the S-tilde = 0 and = 1 centroids, own trial left out."""
    is0, is1 = morph == 0, morph == 1
    s0, s1 = A[is0].sum(0), A[is1].sum(0)
    n0, n1 = is0.sum(), is1.sum()
    c0 = (s0[None, :] - np.where(is0[:, None], A, 0)) / (n0 - is0)[:, None]
    c1 = (s1[None, :] - np.where(is1[:, None], A, 0)) / (n1 - is1)[:, None]
    an = np.linalg.norm(A, axis=1)
    with np.errstate(invalid="ignore", divide="ignore"):
        g0 = (A * c0).sum(1) / (an * np.linalg.norm(c0, axis=1))
        g1 = (A * c1).sum(1) / (an * np.linalg.norm(c1, axis=1))
        return g1 / (g0 + g1)


def step_share(B: np.ndarray) -> float:
    """fig3ab reading: mean over the S-tilde = 0 and = 1 rows of a 5 x 5 binned matrix of the
    largest fall between neighbouring S-tilde values over the whole fall to the other extreme."""
    r0 = B[0]
    f0 = np.max(r0[:-1] - r0[1:]) / (r0[0] - r0[-1])
    r1 = B[-1][::-1]
    f1 = np.max(r1[:-1] - r1[1:]) / (r1[0] - r1[-1])
    return float(np.mean([f0, f1]))


def row_step_share(B: np.ndarray, row: int) -> float:
    r = B[row] if row == 0 else B[row][::-1]
    return float(np.max(r[:-1] - r[1:]) / (r[0] - r[-1]))


NMF_MAX_ITER = 2000   # a standard choice, high enough for the fits to converge


def nmf_session(tm_s: np.ndarray, trials: pd.DataFrame, seed: int, rank: int = 3) -> dict:
    """edf6 criterion: single-cell trial-by-trial cosine matrices (smoothed maps), upper triangles
    stacked over cells, NMF of rank 3; each factor's prototype is averaged over S-tilde blocks."""
    from sklearn.decomposition import NMF

    order = np.argsort(trials["S"].to_numpy(), kind="stable")
    x = tm_s[order]                                        # trials x bins x cells
    xn = unit_rows(np.transpose(x, (2, 0, 1)))             # cells x trials x bins
    iu = np.triu_indices(x.shape[0], 1)
    X = np.empty((xn.shape[0], len(iu[0])), np.float32)
    for c0 in range(0, xn.shape[0], 256):
        sims = np.einsum("ntj,nsj->nts", xn[c0:c0 + 256], xn[c0:c0 + 256])
        X[c0:c0 + 256] = sims[:, iu[0], iu[1]]
    X = np.clip(X, 0, None)
    model = NMF(n_components=rank, init="nndsvda", random_state=seed, max_iter=NMF_MAX_ITER)
    model.fit(X)
    morph = trials["morph"].to_numpy()[order]
    shares, blocks = [], []
    for h in model.components_:
        P = np.zeros((x.shape[0], x.shape[0]))
        P[iu] = h
        P = P + P.T
        B = binned_similarity(P, morph)
        blocks.append(B)
        k = np.unravel_index(np.nanargmax(B), B.shape)
        if k == (0, 0):
            shares.append(row_step_share(B, 0))
        elif k == (4, 4):
            shares.append(row_step_share(B, 4))
    return dict(blocks=blocks, shares=shares, step=float(np.mean(shares)) if shares else np.nan,
                n_iter=model.n_iter_, err=float(model.reconstruction_err_))


def umap_filter(tm: np.ndarray, trials: pd.DataFrame, seed: int, n_perm: int = 1000):
    """edf5 criterion: cells whose S-tilde 0 against 1 map distance exceeds the 99.9th percentile of
    1,000 label shuffles; their maps binned into ten S bins over -0.1 to 1.1 (450 values)."""
    morph = trials["morph"].to_numpy()
    sel = np.where((morph == 0) | (morph == 1))[0]
    X = np.nan_to_num(tm[sel], nan=0.0).reshape(len(sel), -1)      # trials x (bins*cells)
    lab = morph[sel] == 1
    n_cells = tm.shape[2]

    def dist(l):
        d = X[l].mean(0) - X[~l].mean(0)
        return np.sqrt((d.reshape(N_BINS, n_cells) ** 2).sum(0))

    real = dist(lab)
    rng = np.random.default_rng(seed)
    null = np.empty((n_perm, n_cells))
    for k in range(n_perm):
        null[k] = dist(rng.permutation(lab))
    sig = real > np.percentile(null, 99.9, axis=0)
    edges = np.linspace(-0.1, 1.1, 11)
    S = trials["S"].to_numpy()
    sbin = np.clip(np.digitize(S, edges) - 1, 0, 9)
    maps = np.zeros((10, N_BINS, sig.sum()))
    for k in range(10):
        if (sbin == k).any():
            maps[k] = np.nanmean(tm[sbin == k][:, :, sig], axis=0)
    maps = np.nan_to_num(maps, nan=0.0)
    return sig, np.transpose(maps, (2, 0, 1)).reshape(sig.sum(), -1)


LAGS = (-60, -30, -15, -8, -4, -2, 0, 2, 4, 8, 15, 30, 60)   # frames; a check of the clock


def lag_reliability(act, frame_idx, bins, offsets, n_frames, max_cells=300):
    """Median over the first cells of the correlation between odd-trial and even-trial mean maps
    when the activity is shifted by a lag (frames) against position, no speed exclusion. Running
    speed varies between trials, so maps from different trials line up only when activity and
    position share a clock; the peak is then at zero lag or slightly after (calcium)."""
    out = {}
    cells = act[:, :max_cells]
    for lag in LAGS:
        src = np.clip(frame_idx + lag, 0, n_frames - 1)
        tm, _ = trial_matrix(cells[src], np.arange(len(src)), bins, np.ones(len(src), bool), offsets)
        odd, even = np.nanmean(tm[1::2], axis=0), np.nanmean(tm[0::2], axis=0)
        ok = np.isfinite(odd).all(1) & np.isfinite(even).all(1)
        a, b = odd[ok] - odd[ok].mean(0), even[ok] - even[ok].mean(0)
        with np.errstate(invalid="ignore", divide="ignore"):
            r = (a * b).sum(0) / np.sqrt((a ** 2).sum(0) * (b ** 2).sum(0))
        out[lag] = float(np.nanmedian(r))
    return out


def label_shift_contrast(A, morph):
    """Mean SF of S-tilde = 1 minus S-tilde = 0 trials with the true trial labels, and with the
    labels moved by one trial (each trial given the next trial's S-tilde)."""
    out = {}
    for name, lab in (("true", morph), ("shifted by one trial", np.roll(morph, -1))):
        sf = similarity_fraction(A, lab)
        out[name] = float(np.nanmean(sf[lab == 1]) - np.nanmean(sf[lab == 0]))
    return out


def session_seed(mouse: str, day: int, part: int, salt: int) -> int:
    return int(salt * 1_000_003 + sum(ord(ch) * 31 ** i for i, ch in enumerate(mouse)) * 1009 + day * 17 + part)


def process_session(row, mode: str) -> dict:
    """Stream one file and reduce it to what the claims use.

    mode 'meta': trials, cell count and fingerprint. 'sf': also whole-trial SF (both signals).
    'place': also place cells, per-S-tilde maps, the UMAP filter, licks, speed, the clock check
    and NMF. 'population': SF (whole and by position, both signals) and population similarity
    matrices."""
    raw = read_file(row.url, neural=mode != "meta")
    trials = trial_table(raw)
    beh = raw["beh"]
    out = dict(path=row.path, mouse=row.mouse, group=row.group, kind=row.kind, day=row.day,
               part=row.part, n_frames=raw["shape"][0], n_cells=raw["shape"][1], trials=trials,
               rate=raw["rate"], imaging_rate=raw["imaging_rate"], subject=raw["subject"],
               session_id=raw["session_id"], description=raw["description"],
               start_time=raw["start_time"], fingerprint=raw["fingerprint"], units=raw["units"],
               same_ts=raw["same_ts"], json_day=raw["info"].get("day"), json_mouse=raw["info"].get("mouse"),
               dt=float(np.median(np.diff(raw["ts"]))),
               ranges={k: (float(np.nanmin(v)), float(np.nanmax(v))) for k, v in beh.items()},
               starts_match=bool(np.array_equal(np.nonzero(beh["trial start"] > 0)[0], trials["start"])),
               stops_match=bool(np.array_equal(np.nonzero(beh["teleport"] > 0)[0], trials["stop"])))
    tn = beh["trial number"]
    out["trial_numbers_match"] = bool(all(np.all(tn[s:e] == i) for i, (s, e) in enumerate(zip(trials["start"], trials["stop"]))))
    out["morph_series_match"] = bool(np.allclose([beh["morph value"][s] for s in trials["start"]], trials["morph"]))
    if mode == "meta":
        return out
    act = raw["act"]
    out["act_check"] = bool(np.array_equal(act[500:503], raw["act_check"])) if "act_check" in raw else None
    p99 = np.percentile(act, 99, axis=0)
    blk = act[NORM_ROWS[0]:NORM_ROWS[1]]
    with np.errstate(invalid="ignore", divide="ignore"):
        mine = np.where(p99 > 0, blk / p99, 0)
    out["norm_check"] = float(np.nanmax(np.abs(mine - np.nan_to_num(raw["norm_block"]))))
    out["p99_zero"] = int((p99 == 0).sum())
    out["act_min"], out["act_max"] = float(act.min()), float(act.max())
    idx, bins, keep_a, offs = frame_layout(raw, trials)
    out["frames_in_trials"] = len(idx)
    out["speed_kept"] = float(keep_a.mean())
    tm, occ = trial_matrix(act, idx, bins, keep_a, offs)
    out["empty_bins_a"] = float(np.mean(occ == 0))
    scale = np.where(p99 > 0, p99, np.inf)
    morph = trials["morph"].to_numpy()
    tm_s = nan_smooth(tm)
    A = tm_s.reshape(len(trials), -1)
    out["sf"] = similarity_fraction(A, morph)
    if mode in ("population", "sf"):
        tm_n = nan_smooth(tm / scale[None, None, :])
        out["sf_norm"] = similarity_fraction(tm_n.reshape(len(trials), -1), morph)
    if mode == "place":
        pc = place_cells(act, idx, bins, keep_a, offs, morph, seed=session_seed(row.mouse, row.day, row.part, 1))
        out["pc"] = pc
        sig, maps10 = umap_filter(tm, trials, seed=session_seed(row.mouse, row.day, row.part, 2))
        out["umap_sig"], out["umap_maps"] = sig, maps10
        out["lag_rel"] = lag_reliability(act, idx, bins, offs, n_frames=raw["shape"][0])
        out["label_shift"] = label_shift_contrast(A, morph)
        out["nmf"] = nmf_session(tm_s, trials, seed=session_seed(row.mouse, row.day, row.part, 3))
        for g, keep in (("a", keep_a), ("b", np.ones_like(keep_a))):
            lk, _ = trial_matrix(beh["licks"][:, None], idx, bins, keep, offs)
            sp, _ = trial_matrix(beh["speed"][:, None], idx, bins, keep, offs)
            out[f"licks_{g}"], out[f"speed_{g}"] = lk[:, :, 0], sp[:, :, 0]
    if mode == "population":
        for name, x in (("raw", tm_s), ("norm", tm_n), ("unsmoothed", np.nan_to_num(tm, nan=0.0))):
            Ab = unit_rows(x.reshape(len(trials), -1))
            C = Ab @ Ab.T
            out[f"C_{name}"] = binned_similarity(C, morph)
            if name == "raw":
                order = np.argsort(trials["S"].to_numpy(), kind="stable")
                out["C_full_sorted"] = C[np.ix_(order, order)].astype(np.float32)
        # position-wise SF (M9): one position bin at a time
        out["sf_pos"] = np.column_stack([similarity_fraction(tm_s[:, j, :], morph) for j in range(N_BINS)])
    return out


def process_many(rows, mode: str, workers: int = 2):
    """Process sessions, reading the next while the current one is reduced. Metadata-only reads
    run in separate processes, as h5py serialises reads within one process."""
    rows = list(rows)
    if mode == "meta":
        from concurrent.futures import ProcessPoolExecutor
        with ProcessPoolExecutor(workers) as ex:
            return list(ex.map(process_session, rows, [mode] * len(rows)))
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(lambda r: process_session(r, mode), rows))


# ----------------------------------------------------------------------------- edf5 classification
def _fit_logistic_batch(X, Y, W, C=1.0, n_iter=50, tol=1e-8):
    """L2 logistic regressions (intercept not penalised), one per row of Y, by Newton's method.

    X n x d, Y and W p x n (labels in {0, 1} and sample weights, 0 outside the training set).
    The objective is sklearn's: 0.5 |w|^2 + C sum_i W_i logloss_i."""
    n, d = X.shape
    Xa = np.hstack([X, np.ones((n, 1))])
    beta = np.zeros((Y.shape[0], d + 1))
    reg = np.eye(d + 1)
    reg[-1, -1] = 0.0
    for _ in range(n_iter):
        z = beta @ Xa.T
        p = 1.0 / (1.0 + np.exp(-z))
        g = C * ((W * (p - Y)) @ Xa) + beta @ reg
        h = C * np.einsum("pn,ni,nj->pij", W * p * (1 - p), Xa, Xa, optimize=True) + reg[None]
        step = np.linalg.solve(h, g[:, :, None])[:, :, 0]
        beta -= step
        if np.max(np.abs(step)) < tol:
            break
    return beta


def cv_accuracy_permutations(X, y, n_permutations, seed, n_folds=10, C=1.0):
    """10-fold cross-validated accuracy of balanced L2 logistic regression for the true labels and
    for label permutations, as sklearn's permutation_test_score does it: each permutation shuffles
    the labels over all cells, StratifiedKFold (no shuffling) splits on the permuted labels, and
    class weights are balanced within each training set. Returns (score, permutation scores)."""
    from sklearn.model_selection import StratifiedKFold

    rng = np.random.default_rng(seed)
    y = np.asarray(y, int)
    labels = np.vstack([y] + [rng.permutation(y) for _ in range(n_permutations)])
    P, n = labels.shape
    train = np.zeros((n_folds, P, n), bool)
    for pi in range(P):
        for k, (tr, te) in enumerate(StratifiedKFold(n_folds).split(X, labels[pi])):
            train[k, pi, tr] = True
    acc = np.zeros((n_folds, P))
    for k in range(n_folds):
        tr = train[k]
        n1 = (labels * tr).sum(1, keepdims=True)
        n0 = tr.sum(1, keepdims=True) - n1
        ntr = tr.sum(1, keepdims=True)
        w = np.where(labels == 1, ntr / (2 * n1), ntr / (2 * n0)) * tr
        beta = _fit_logistic_batch(X, labels.astype(float), w, C=C)
        z = beta[:, :-1] @ X.T + beta[:, -1:]
        pred = (z > 0).astype(int)
        te = ~tr
        acc[k] = ((pred == labels) & te).sum(1) / te.sum(1)
    scores = acc.mean(0)
    return scores[0], scores[1:]
