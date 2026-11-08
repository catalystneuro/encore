"""Loading and measures for CRCNS data set ssc-10 (LeMessurier & Feldman, doi:10.6080/K0DB801M).

LeMessurier, Laboy-Juarez, McLain, Chen, Nguyen & Feldman (2019), eLife 8:e46321,
doi:10.7554/eLife.46321.

The data set is one gzipped tar file, `ssc-10/live/data.tar.gz` (4.7 GB), in the public S3 bucket
crcnsarchive. It is streamed once, member by member, with fsspec and tarfile; each imaging field's
three MATLAB files (reduced_data.mat, settings.mat, processed_data.mat) are read into memory,
reduced to the arrays below, and dropped. Nothing is written to disk.

Where the parameters come from:

- Evoked response of a trial: mean dF/F over `framesEvoked` (the 30 frames after onset, 1 s at
  30 Hz) minus the mean over the 15 frames before onset (0.5 s), in the trial-aligned traces
  `traceByStim` and `sponTrace` (Methods, "Quantification of whisker responses": "(mean dF/F in
  the 1 s period following whisker train onset) - (mean dF/F in the 0.5 s prior to the
  stimulus)"). `framesEvoked` and `bl_length` are read from each field's settings.mat.
- Whisker codes in `Stimuli.Label`: label k is `whisk[k]` of settings.mat for k = 0 to 8, and 9
  is a blank trial; onset frame is floor(Time * sampRate). Both were checked against the frame
  lists stored per whisker in `Stimuli` (notebook, data check).
- Responsiveness (claims file, opening comment; Methods): a one-sided permutation test of the
  difference in means of the per-trial evoked responses on whisker trials against blank trials,
  10,000 shuffles, p = (number of shuffled differences >= observed + 1) / 10,001, then
  Benjamini-Hochberg over the nine whiskers at 0.05. To make the test fast, one set of 10,000
  random relabellings is drawn per field and whisker and applied to every ROI of the field (the
  ROIs of a field share their trials); each ROI's test is still an exact permutation test.
  The data set's own sample code (sample_code.zip, find_sigROIs.m and MultControl.m) instead
  takes the stored `permTestResults` p-values, BH-corrects them over the nine whiskers at 0.05,
  and drops ROIs whose traces contain NaN; that is the claims file's variant.
- The dF/F of the neuropil-subtraction analysis (Figure 5 S2) is rebuilt from processed_data.mat:
  the raw and neuropil traces are each filtered by a 5-frame moving median, then F = raw - r *
  neuropil (the data descriptor: subtracted "after temporal filtering and before deltaF/F
  calculation"), F0 the 5th percentile of each movie, then the same trial alignment. The stored
  dF/F matches a 5-frame median and F0 the 5th percentile, not the 4 frames and 20th percentile
  of the Methods, and the filter-first order for L4; both are shown in the notebook.
- Barrel radius per field and barrel: `ROI_pos_barrel` divided by `ROI_pos_barrel_norm`, which
  the data set describes as positions "normalized to barrel radius for each individual barrel".
- Blank trials are the stored `sponTrace` segments, cut like `traceByStim` (106 frames from 0.5 s
  before onset). In one field (ScENR10b/20180105/f2) `sponTrace` holds 76-frame segments starting
  0.5 s after onset; there the blank trials are cut from the stored dF/F at every Label 9 onset.
- Seeds: each analysis passes its own `numpy.random.Generator`; the seed is a standard choice.
"""

from __future__ import annotations

import hashlib
import io
import re
import tarfile

import fsspec
import numpy as np
import scipy.io as sio
from scipy.ndimage import median_filter
from scipy.optimize import linear_sum_assignment

DATASET = "ssc-10"
VERSION = "unversioned"   # CRCNS data sets have no versions; the MD5 below pins the file read
URL = "https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-10/live/data.tar.gz"
DATA_MD5 = "80bcef52304d27c9e039e7027fe09ff4"   # checksums.md5 of the data set, data.tar.gz
WHISKERS = ["c1", "c2", "c3", "d1", "d2", "d3", "e1", "e2", "e3"]
NP_WEIGHTS = (0.0, 0.3, 0.7)
N_PERM = 10_000


def field_info(path):
    """Mouse, group (NH or EN), layer and field name from a member path data/<mouse>/<date>/[f#]/."""
    parts = path.split("/")
    mouse = parts[1]
    m = re.match(r"(Sc|D)(NH|ENR)", mouse)
    layer = "L4" if m.group(1) == "Sc" else "L23"
    group = "NH" if m.group(2) == "NH" else "EN"
    field = "/".join(parts[1:-1])
    return dict(field=field, mouse=mouse, group=group, layer=layer, date=parts[2])


def _load(b):
    return sio.loadmat(io.BytesIO(b), squeeze_me=True, simplify_cells=True)


def _segments(trace, frames, pre, total):
    """Rows trace[f - 1 - pre : f - 1 - pre + total] for 1-based onset frames f that fit."""
    rows = []
    for f in frames:
        a = int(f) - 1 - pre
        if a >= 0 and a + total <= len(trace):
            rows.append(trace[a:a + total])
    return rows


def _filt(x):
    """The pipeline's 5-frame moving median; it leaves the first and last two frames at zero."""
    y = median_filter(x, size=(1, 5), mode="nearest")
    y[:, :2] = 0.0
    y[:, -2:] = 0.0
    return y


def _dff(raw, npil, r, order="filter_first"):
    """dF/F as the stored data have it: 5-frame moving median, F0 the 5th percentile of the movie.

    order 'filter_first' filters the ROI and neuropil traces and then subtracts r times the
    neuropil, as the data descriptor says for L4 ("subtracted from ROI signal ... after temporal
    filtering and before deltaF/F calculation"); 'subtract_first' subtracts and then filters, shown
    in the notebook as the order that does not reproduce the stored L4 traces.
    """
    if order == "filter_first":
        f = _filt(raw) - r * _filt(npil)
    else:
        f = _filt(raw - r * npil)
    f0 = np.percentile(f, 5, axis=1, keepdims=True)
    return (f - f0) / f0


def reduce_field(info, red, settings, proc=None):
    """Reduce one field's MATLAB structures to arrays per ROI, whisker and trial."""
    whisk = [str(w) for w in np.atleast_1d(settings["whisk"])]
    fe = np.atleast_1d(settings["framesEvoked"]).astype(int) - 1          # 0-based, 15..44
    fs = float(np.atleast_1d(settings["sampRate"])[0])
    n_pre = int(np.ceil(float(settings["bl_length"]) * fs))              # 15 frames
    tbs, spon = red["traceByStim"], red["sponTrace"]
    rois = list(tbs.keys())
    R = len(rois)
    out = dict(info)
    out.update(rois=rois, n_rois=R, fs=fs, n_pre=n_pre, frames_evoked=fe,
               npSub=int(settings["npSub"]), permTestType=str(settings["permTestType"]),
               n_movies=len(red["deltaF"]), n_movies_stim=len(red["Stimuli"]), whisk_order=whisk)
    pre = slice(0, n_pre)
    ev, post_only = {}, {}
    nan = np.zeros(R, bool)
    out["missing_whiskers"] = [w for w in WHISKERS if w not in tbs[rois[0]]]
    for w in WHISKERS:
        if w in out["missing_whiskers"]:
            post_only[w] = ev[w] = np.zeros((R, 0))
            continue
        T = np.stack([np.atleast_2d(tbs[r][w]) for r in rois])               # R x trials x 106
        nan |= np.isnan(T).any(axis=(1, 2))
        post_only[w] = T[:, :, fe].mean(2)
        ev[w] = post_only[w] - T[:, :, pre].mean(2)
    S = np.stack([np.atleast_2d(spon[r]) for r in rois])
    out["spon_len"], out["trace_len"] = S.shape[2], T.shape[2]
    out["ev"], out["ev_post"] = ev, post_only
    if S.shape[2] == T.shape[2]:
        nan |= np.isnan(S).any(axis=(1, 2))
        out["bl"], out["bl_post"] = S[:, :, fe].mean(2) - S[:, :, pre].mean(2), S[:, :, fe].mean(2)
    # else: sponTrace is not cut like traceByStim (one field); the blank trials are cut from the
    # stored dF/F at the Label 9 onsets below.
    out["has_nan"] = nan
    out["mean_trace_stim"] = np.nanmean(np.concatenate([np.stack([np.atleast_2d(tbs[r][w]) for r in rois]) for w in WHISKERS if w in tbs[rois[0]]], axis=1), axis=(0, 1))
    out["mean_trace_blank"] = np.nanmean(S, axis=(0, 1))
    pt = red["permTestResults"]
    out["p_stored"] = np.array([[float(pt[r].get(w, np.nan)) for w in WHISKERS] for r in rois])
    pos, posn = red["ROI_pos_barrel"], red["ROI_pos_barrel_norm"]
    nan2 = [np.nan, np.nan]
    out["pos"] = np.array([[np.asarray(pos.get(w, {}).get(r, nan2), float) for w in WHISKERS] for r in rois])
    out["posn"] = np.array([[np.asarray(posn.get(w, {}).get(r, nan2), float) for w in WHISKERS] for r in rois])
    barrel = np.array([""] * R, dtype=object)
    for w in WHISKERS:
        for r in np.atleast_1d(red["ROIsInBarrel"].get(w, [])):
            if isinstance(r, str) and r in rois:
                barrel[rois.index(r)] = w
    out["barrel"] = barrel

    # Stimulus table, and a check of the label code against the stored frame lists.
    # Movie names carry a leading "m" in some structures and fields and not in others.
    stim = {k.lstrip("m"): v for k, v in red["Stimuli"].items()}
    dff = {k.lstrip("m"): v for k, v in red["deltaF"].items()}
    movies = [mv for mv in dff if mv in stim]
    out["movies_without_stimuli"] = sorted(set(dff) - set(stim))
    out["stimuli_without_movie"] = sorted(set(stim) - set(dff))
    label_ok, n_frames_listed, blank_onsets = True, 0, {}
    long_trace = []   # population mean dF/F around whisker and blank onsets, -150..+149 frames
    for mv in movies:
        st = stim[mv]
        lab = np.atleast_1d(st["Label"]).astype(int)
        onset = np.floor(np.atleast_1d(st["Time"]).astype(float) * fs).astype(int)
        for k, w in enumerate(whisk):
            listed = np.atleast_1d(st.get(w, [])).astype(int)
            n_frames_listed += len(listed)
            if not set(listed) <= set(onset[lab == k]):
                label_ok = False
        blank_onsets[mv] = onset[lab == 9]
    out["label_code_ok"] = label_ok
    out["n_blank_label9"] = int(sum(len(b) for b in blank_onsets.values()))

    # Population mean dF/F around onsets, to check the stimulus timing against the traces.
    lags = np.arange(-150, 150)
    acc_s, acc_b, ns, nb = np.zeros(len(lags)), np.zeros(len(lags)), 0, 0
    for mv in movies:
        st = stim[mv]
        D = np.stack([np.asarray(dff[mv][r], float) for r in rois]).mean(0)
        lab = np.atleast_1d(st["Label"]).astype(int)
        onset = np.floor(np.atleast_1d(st["Time"]).astype(float) * fs).astype(int)
        for o, l in zip(onset, lab):
            a = o - 1 + lags[0]
            if a < 2 or a + len(lags) > len(D) - 2:
                continue
            if l == 9:
                acc_b += D[a:a + len(lags)]; nb += 1
            else:
                acc_s += D[a:a + len(lags)]; ns += 1
    # Absolute dF/F level on blank trials (no baseline subtraction), from the stored dF/F: the
    # median over blank trials (Label 9) of the mean over the evoked window.
    lvl = [[] for _ in rois]
    for mv in movies:
        D = np.stack([np.asarray(dff[mv][r], float) for r in rois])
        for o in blank_onsets[mv]:
            a = o - 1
            if a - n_pre >= 0 and a + fe[-1] - n_pre + 1 <= D.shape[1]:
                v = D[:, a - n_pre + fe].mean(1)
                for i in range(R):
                    lvl[i].append(v[i])
    out["spont_level"] = np.array([np.median(v) if v else np.nan for v in lvl])
    if "bl" not in out:
        segs = []
        for mv in movies:
            D = np.stack([np.asarray(dff[mv][r], float) for r in rois])
            segs += _segments(D.T, blank_onsets[mv], n_pre, T.shape[2])
        B = np.stack([g.T for g in segs], axis=1)                          # R x trials x 106
        out["has_nan"] = out["has_nan"] | np.isnan(B).any(axis=(1, 2))
        out["bl"], out["bl_post"] = B[:, :, fe].mean(2) - B[:, :, pre].mean(2), B[:, :, fe].mean(2)
    out["onset_lags"] = lags
    out["onset_trace_stim"] = acc_s / max(ns, 1)
    out["onset_trace_blank"] = acc_b / max(nb, 1)

    if proc is not None:
        raw = {k.lstrip("m"): v for k, v in proc["rawTimeSeries"].items()}
        npl = {k.lstrip("m"): v for k, v in proc["rawTimeSeriesNP_corr"].items()}
        out["movies_without_raw"] = sorted(set(movies) - set(raw))
        movies = [mv for mv in movies if mv in raw]
        out["n_rois_raw"] = len(raw[movies[0]])
        # check: the stored dF/F against the rebuilt one at r = 0, first movie
        F = np.stack([np.asarray(raw[movies[0]][r], float) for r in rois])
        D0 = np.stack([np.asarray(dff[movies[0]][r], float) for r in rois])
        N0 = np.stack([np.asarray(npl[movies[0]][r], float) for r in rois])
        r_own = 0.3 if out["npSub"] else 0.0   # the field's own weight (Methods: r = 0.3 for L4)
        out["dff_rebuild_maxdiff"] = float(np.nanmax(np.abs(_dff(F, N0, r_own) - D0)[:, 2:-2]))
        out["dff_subtract_first_maxdiff"] = float(np.nanmax(np.abs(_dff(F, N0, r_own, "subtract_first") - D0)[:, 2:-2]))
        D20 = (median_filter(F, size=(1, 4), mode="nearest"))
        D20 = (D20 - np.percentile(D20, 20, axis=1, keepdims=True)) / np.percentile(D20, 20, axis=1, keepdims=True)
        out["dff_methods_maxdiff"] = float(np.nanmax(np.abs(D20 - D0)[:, 2:-2]))
        npres = {}
        for rw in NP_WEIGHTS:
            ev_r = {w: [[] for _ in rois] for w in WHISKERS}
            bl_r = [[] for _ in rois]
            for mv in movies:
                st = stim[mv]
                F = np.stack([np.asarray(raw[mv][r], float) for r in rois])
                N = np.stack([np.asarray(npl[mv][r], float) for r in rois])
                D = _dff(F, N, rw)
                for w in WHISKERS:
                    fr = np.atleast_1d(st.get(w, [])).astype(int)
                    for f in fr:
                        a = f - 1 - n_pre
                        if a < 0 or a + 106 > D.shape[1]:
                            continue
                        seg = D[:, a:a + 106]
                        e = seg[:, fe].mean(1) - seg[:, pre].mean(1)
                        for i in range(R):
                            ev_r[w][i].append(e[i])
                for f in blank_onsets[mv]:
                    a = f - 1 - n_pre
                    if a < 0 or a + 106 > D.shape[1]:
                        continue
                    seg = D[:, a:a + 106]
                    e = seg[:, fe].mean(1) - seg[:, pre].mean(1)
                    for i in range(R):
                        bl_r[i].append(e[i])
            npres[rw] = dict(ev={w: np.array(ev_r[w]) for w in WHISKERS}, bl=np.array(bl_r))
        # sponTrace keeps fewer blank trials than Label 9 lists; keep the rebuilt blank trials that
        # match the stored ones, at the field's own weight, one to one (an assignment minimising
        # the summed squared difference over ROIs), so all weights use the stored set.
        # ROIs whose rebuilt or stored traces are not finite (F0 of zero) are left out of the match.
        b0 = npres[r_own]["bl"]
        good = np.isfinite(b0).all(1) & np.isfinite(out["bl"]).all(1)
        dist = (((out["bl"][good].T[:, None, :] - b0[good].T[None, :, :]) ** 2).sum(-1))
        _, keep = linear_sum_assignment(dist)
        out["np_blank_match_maxdiff"] = float(np.abs(b0[good][:, keep] - out["bl"][good]).max())
        out["np_nonfinite_rois"] = int((~good).sum())
        out["np_blank_n"] = (out["bl"].shape[1], b0.shape[1])
        for rw in NP_WEIGHTS:
            npres[rw]["bl"] = npres[rw]["bl"][:, keep]
        out["np"] = npres
    return out


STREAM_MD5 = {}


class _Hashing:
    """A read-only file wrapper that keeps the MD5 of everything read through it."""

    def __init__(self, f):
        self.f, self.md5 = f, hashlib.md5()

    def read(self, n=-1):
        b = self.f.read(n)
        self.md5.update(b)
        return b


def stream_fields(neuropil=True, limit=None, verbose=True, keep_going=False):
    """Stream data.tar.gz once and yield one reduced field at a time, in archive order."""
    pending = {}
    done = 0
    with fsspec.open(URL, block_size=2 ** 22) as raw:
        f = _Hashing(raw)
        tf = tarfile.open(fileobj=f, mode="r|gz")
        for m in tf:
            if not m.isfile():
                continue
            name = m.name.rsplit("/", 1)[1]
            key = m.name.rsplit("/", 1)[0]
            pending.setdefault(key, {})[name] = tf.extractfile(m).read()
            got = pending[key]
            if {"reduced_data.mat", "settings.mat", "processed_data.mat"} <= set(got):
                info = field_info(m.name)
                red, sett = _load(got["reduced_data.mat"]), _load(got["settings.mat"])
                proc = _load(got["processed_data.mat"]) if neuropil else None
                del pending[key]
                try:
                    out = reduce_field(info, red, sett, proc)
                except Exception as e:   # only when keep_going, for development
                    if not keep_going:
                        raise
                    out = dict(info, error=repr(e))
                out["sizes"] = {k: len(v) for k, v in got.items()}
                del red, proc, got
                if verbose:
                    print(f"{info['field']}: {out.get('n_rois')} ROIs", flush=True)
                yield out
                done += 1
                if limit and done >= limit:
                    return
        while f.read(2 ** 22):   # the rest of the stream, so the checksum covers the whole file
            pass
        STREAM_MD5["data.tar.gz"] = f.md5.hexdigest()


# ---------------------------------------------------------------- statistics

def bh(p, alpha=0.05):
    """Benjamini-Hochberg step-up over the last axis; True where rejected."""
    p = np.asarray(p, float)
    n = p.shape[-1]
    order = np.argsort(p, axis=-1)
    ps = np.take_along_axis(p, order, -1)
    thr = alpha * np.arange(1, n + 1) / n
    below = ps <= thr
    k = np.where(below.any(-1), n - np.argmax(below[..., ::-1], -1), 0)   # largest index passing
    rej_sorted = np.arange(n) < k[..., None]
    rej = np.zeros_like(rej_sorted)
    np.put_along_axis(rej, order, rej_sorted, -1)
    return rej


def perm_masks(n1, n2, rng, n_perm=N_PERM):
    """n_perm random relabellings of n1 + n2 values: a 0/1 matrix marking the first group."""
    n = n1 + n2
    keys = rng.random((n_perm, n))
    idx = np.argsort(keys, axis=1)[:, :n1]
    M = np.zeros((n_perm, n), np.float32)
    np.put_along_axis(M, idx, 1.0, 1)
    return M


def perm_diff_many(A, B, rng, n_perm=N_PERM, tail="greater"):
    """Permutation test of mean(A) - mean(B) for many rows at once (rows share n1, n2).

    A is rows x n1, B rows x n2. p = (count of shuffled statistics at least as extreme + 1) /
    (n_perm + 1). tail 'greater' is one-sided; 'two' compares absolute differences, as
    permutationTest.m of the paper's code does.
    """
    A, B = np.asarray(A, float), np.asarray(B, float)
    n1, n2 = A.shape[1], B.shape[1]
    X = np.concatenate([A, B], axis=1)
    tot = X.sum(1)
    obs = A.mean(1) - B.mean(1)
    M = perm_masks(n1, n2, rng, n_perm)
    s1 = M @ X.T.astype(np.float32)                    # n_perm x rows
    d = s1 / n1 - (tot[None, :] - s1) / n2
    if tail == "greater":
        c = (d >= obs[None, :] - 1e-12).sum(0)
    else:
        c = (np.abs(d) >= np.abs(obs)[None, :] - 1e-12).sum(0)
    return obs, (c + 1) / (n_perm + 1)


def perm_test_means(a, b, rng, n_perm=N_PERM):
    """Two-sided permutation test of the difference in means of two samples (permutationTest.m)."""
    a, b = np.asarray(a, float), np.asarray(b, float)
    a, b = a[np.isfinite(a)], b[np.isfinite(b)]
    if len(a) == 0 or len(b) == 0:
        return np.nan, np.nan
    x = np.concatenate([a, b])
    obs = a.mean() - b.mean()
    n1 = len(a)
    cnt = 0
    for _ in range(n_perm // 1000):
        P = np.argsort(rng.random((1000, len(x))), axis=1)
        s = x[P[:, :n1]].mean(1) - x[P[:, n1:]].mean(1)
        cnt += (np.abs(s) >= abs(obs) - 1e-12).sum()
    return obs, (cnt + 1) / (n_perm + 1)


def perm_median_diff(a, b, rng, n_perm=1000):
    """Two-sided permutation test of the difference in medians (permutationTest_median.m)."""
    x = np.concatenate([a, b])
    n1 = len(a)
    obs = np.median(a) - np.median(b)
    P = np.argsort(rng.random((n_perm, len(x))), axis=1)
    s = np.median(x[P[:, :n1]], 1) - np.median(x[P[:, n1:]], 1)
    return obs, ((np.abs(s) >= abs(obs) - 1e-12).sum() + 1) / (n_perm + 1)


def sem(x):
    x = np.asarray(x, float)
    x = x[np.isfinite(x)]
    return x.std(ddof=1) / np.sqrt(len(x)) if len(x) > 1 else np.nan


# ---------------------------------------------------------------- per-ROI measures

def responsiveness(fields, rng):
    """Add `p_methods` (R x 9, one-sided test of the Methods) and the two responsive masks."""
    for f in fields:
        P = np.full((f["n_rois"], 9), np.nan)
        for j, w in enumerate(WHISKERS):
            if f["ev"][w].shape[1]:
                P[:, j] = perm_diff_many(f["ev"][w], f["bl"], rng)[1]
        f["p_methods"] = P
        f["resp_methods"] = bh(np.where(np.isnan(P), 1, P)).any(1)
        f["resp_stored"] = bh(np.where(np.isnan(f["p_stored"]), 1, f["p_stored"])).any(1) & ~f["has_nan"]


def ebw_sets(f, rows, best, rng, n_perm=N_PERM, tail="two"):
    """Equivalent best whiskers for ROIs `rows` of field f, whose best whisker index is `best`.

    Returns three R x 9 boolean arrays: E1 (two-sided permutation test of the difference in means
    against the BW, p >= 0.05 uncorrected), E2 (as E1, BH over the eight comparisons), and the
    p-values themselves (NaN on the BW). Readings E1 and E2 of the claims file. tail 'greater'
    tests BW > other whisker one-sided (an exploratory reading, not in the claims file).
    """
    P = np.full((len(rows), 9), np.nan)
    for b in range(9):
        sel = np.where(best == b)[0]
        if len(sel) == 0:
            continue
        A = f["ev"][WHISKERS[b]][rows[sel]]
        for j in range(9):
            if j == b or f["ev"][WHISKERS[j]].shape[1] == 0:
                continue
            P[sel, j] = perm_diff_many(A, f["ev"][WHISKERS[j]][rows[sel]], rng, n_perm, tail=tail)[1]
    e1 = np.where(np.isnan(P), False, P >= 0.05)
    e1[np.arange(len(rows)), best] = True
    Pf = np.where(np.isnan(P), 1.0, P)
    others = np.array([np.delete(Pf[i], best[i]) for i in range(len(rows))]) if len(rows) else np.zeros((0, 8))
    rej = bh(others) if len(rows) else np.zeros((0, 8), bool)
    e2 = np.zeros_like(e1)
    for i in range(len(rows)):
        idx = [j for j in range(9) if j != best[i]]
        e2[i, idx] = ~rej[i] & ~np.isnan(P[i, idx])
        e2[i, best[i]] = True
    return e1, e2, P


def ebw_median(f, rows, best, rng, n_perm=1000):
    """Reading E3: two-sided permutation test of the difference in medians, p >= 0.05."""
    e3 = np.zeros((len(rows), 9), bool)
    for i, r in enumerate(rows):
        a = f["ev"][WHISKERS[best[i]]][r]
        e3[i, best[i]] = True
        for j in range(9):
            if j != best[i] and f["ev"][WHISKERS[j]].shape[1]:
                e3[i, j] = perm_median_diff(a, f["ev"][WHISKERS[j]][r], rng, n_perm)[1] >= 0.05
    return e3


def roi_table(fields, resp="methods", rng=None, ebw=True, ebw_med=False, np_weight=None):
    """One record per responsive ROI with the measures the claims use.

    resp: 'methods' (the Methods' test) or 'stored' (the data set's permTestResults, BH).
    np_weight: use the dF/F rebuilt with this neuropil weight (Figure 5 S2) in place of the stored.
    """
    import pandas as pd
    recs, extra = [], []
    for fi, f in enumerate(fields):
        mask = f["resp_" + resp] if np_weight is None else f["resp_np"][np_weight]
        rows = np.where(mask)[0]
        if len(rows) == 0:
            continue
        evs = f["ev"] if np_weight is None else f["np"][np_weight]["ev"]
        bl = f["bl"] if np_weight is None else f["np"][np_weight]["bl"]
        med = np.array([[np.median(evs[w][r]) if evs[w].shape[1] else np.nan for w in WHISKERS] for r in rows])
        mean = np.array([[np.mean(evs[w][r]) if evs[w].shape[1] else np.nan for w in WHISKERS] for r in rows])
        bmean, bmed, bsd = bl[rows].mean(1), np.median(bl[rows], 1), bl[rows].std(1, ddof=1)
        z = (med - bmean[:, None]) / bsd[:, None]
        zmed = (med - bmed[:, None]) / bsd[:, None]
        best = np.nanargmax(mean, 1)
        best_med = np.nanargmax(med, 1)
        if ebw:
            g = dict(f, ev=evs)
            e1, e2, P = ebw_sets(g, rows, best, rng)
            e3 = ebw_median(g, rows, best, rng) if ebw_med else np.zeros_like(e1)
        else:
            e1 = e2 = e3 = np.zeros((len(rows), 9), bool)
        dist = np.sqrt((f["pos"][rows] ** 2).sum(-1))            # R x 9, um to each barrel centre
        distn = np.sqrt((f["posn"][rows] ** 2).sum(-1))
        for i, r in enumerate(rows):
            recs.append(dict(fi=fi, field=f["field"], mouse=f["mouse"], group=f["group"],
                             layer=f["layer"], roi=f["rois"][r], row=r, barrel=f["barrel"][r],
                             best=WHISKERS[best[i]], best_med=WHISKERS[best_med[i]],
                             spont=np.median(bl[r]), spont_level=f["spont_level"][r] if np_weight is None else np.nan))
            extra.append((z[i], zmed[i], med[i], mean[i], dist[i], distn[i], e1[i], e2[i], e3[i]))
    t = pd.DataFrame(recs)
    names = ["z", "zmed", "med", "mean", "dist", "distn", "e1", "e2", "e3"]
    arrs = {n: np.array([e[k] for e in extra]) for k, n in enumerate(names)}
    return t, arrs


# ---------------------------------------------------------------- correlations

def pair_table(fields, resp="methods", barrels=None, np_weight=None):
    """Signal and noise correlations of every pair of simultaneously imaged responsive ROIs that both
    lie over (L2/3) or in (L4) a barrel (Methods, Signal and noise correlation analysis).

    Signal: Pearson correlation of the two z-scored 9-element vectors of mean evoked response per
    whisker. Noise: for each whisker, Pearson correlation of the two ROIs' z-scored per-trial evoked
    responses, averaged over whiskers. Distance: Euclidean distance (um) between the two ROIs'
    positions relative to the same barrel centre (C1).
    """
    import pandas as pd
    out = []
    for fi, f in enumerate(fields):
        mask = (f["resp_" + resp] if np_weight is None else f["resp_np"][np_weight]) & (f["barrel"] != "")
        if barrels is not None:
            mask &= np.isin(f["barrel"], barrels)
        rows = np.where(mask)[0]
        if len(rows) < 2:
            continue
        evs = f["ev"] if np_weight is None else f["np"][np_weight]["ev"]
        ws = [w for w in WHISKERS if evs[w].shape[1] > 2]
        M = np.array([[evs[w][r].mean() for w in ws] for r in rows])
        sig = np.corrcoef(M)
        noise = np.nanmean([np.corrcoef(evs[w][rows]) for w in ws], axis=0)
        p = f["pos"][rows, 0, :]
        dist = np.sqrt(((p[:, None, :] - p[None, :, :]) ** 2).sum(-1))
        b = f["barrel"][rows]
        i, j = np.triu_indices(len(rows), 1)
        for a, c in zip(i, j):
            out.append(dict(fi=fi, field=f["field"], mouse=f["mouse"], group=f["group"], layer=f["layer"],
                            i=rows[a], j=rows[c], bi=b[a], bj=b[c], same=b[a] == b[c],
                            signal=sig[a, c], noise=noise[a, c], dist=dist[a, c]))
    return pd.DataFrame(out)


# ---------------------------------------------------------------- decoders

def fit_logistic_1d(x, y, iters=25, ridge=1e-6, mask=None):
    """Logistic regression of y (0/1) on scalar x, many fits at once: x, y are S x n.

    Newton-Raphson on intercept and slope; returns (b0, b1), each of length S. mask (S x n, 0/1)
    keeps only the trials marked 1 in each fit.
    """
    S = x.shape[0]
    m = np.ones_like(x, dtype=float) if mask is None else np.asarray(mask, float)
    b = np.zeros((S, 2))
    for _ in range(iters):
        eta = b[:, :1] + b[:, 1:] * x
        p = 1 / (1 + np.exp(-np.clip(eta, -30, 30)))
        w = p * (1 - p) * m
        g0 = ((y - p) * m).sum(1); g1 = ((y - p) * m * x).sum(1)
        h00 = w.sum(1) + ridge; h01 = (w * x).sum(1); h11 = (w * x * x).sum(1) + ridge
        det = h00 * h11 - h01 ** 2
        det = np.where(np.abs(det) < 1e-12, 1e-12, det)
        b[:, 0] += (h11 * g0 - h01 * g1) / det
        b[:, 1] += (-h01 * g0 + h00 * g1) / det
    return b[:, 0], b[:, 1]


def make_splits(n_stim, n_blank, rng, scheme="random", n_rep=500, balance=False):
    """Train/test masks over the stimulus-then-blank trials, S x n each.

    scheme 'random': n_rep random 80/20 splits; 'kfold': 5-fold cross-validation repeated
    n_rep // 5 times. balance: blank trials subsampled to the number of stimulus trials, afresh
    for each repetition (unused trials are in neither set).
    """
    n = n_stim + n_blank
    trains, tests = [], []
    reps = n_rep if scheme == "random" else n_rep // 5
    for _ in range(reps):
        use = np.ones(n, bool)
        if balance and n_blank > n_stim:
            drop = rng.choice(n_blank, n_blank - n_stim, replace=False) + n_stim
            use[drop] = False
        idx = np.where(use)[0]
        idx = idx[rng.permutation(len(idx))]
        if scheme == "random":
            k = int(round(0.2 * len(idx)))
            te = np.zeros(n, bool); te[idx[:k]] = True
            tr = use & ~te
            trains.append(tr); tests.append(te)
        else:
            for part in np.array_split(idx, 5):
                te = np.zeros(n, bool); te[part] = True
                trains.append(use & ~te); tests.append(te)
    return np.array(trains), np.array(tests)


def roi_probs(x, y, trains, tests):
    """Per split, the fitted P(stimulus) on every trial (S x n), and the test fraction correct (S)."""
    S, n = trains.shape
    X = np.broadcast_to(x, (S, n))
    Y = np.broadcast_to(y, (S, n)).astype(float)
    # fit on the training trials of each split only (the others get zero weight)
    b0, b1 = fit_logistic_1d(X, Y, mask=trains)
    P = 1 / (1 + np.exp(-np.clip(b0[:, None] + b1[:, None] * X, -30, 30)))
    correct = ((P > 0.5) == (Y > 0.5)) & tests
    return P, correct.sum(1) / tests.sum(1)
