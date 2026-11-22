"""Loading and measures for the MAP recordings of dandiset 000363, as Hasnain, Han & Economo (2025)
use them for Figure 4 (bioRxiv doi:10.1101/2025.10.17.682917).

Each NWB file holds one session: units with spike times, a quality label (`unit_quality`, good or
multi), a classification (`classification`, good or unlabelled) and a CCF annotation (`anno_name`,
filled only for units classified good); electrodes whose `location` JSON names the probe's target
("left ALM", "right Medulla"); a trial table; go cue times (`go_start_times`); and side-camera
keypoint tracking of the jaw and nose (about 294 Hz, one segment per trial). Files are streamed from
the archive at the pinned version; nothing is written to disk.

Where the parameters come from. "Claims" is the claims file `claims/hasnain-2025.yaml`, whose header
items M1 to M10 cite the paper; "Methods" is a passage of the paper's Methods.

- Session and unit selection (M1, M2; Methods, "Curation of Mesoscale Activity Map Dataset"): units
  classified 'good' whose CCF label is MOs on a probe described as targeting ALM, and units in IRN,
  GRN or PARN; sessions with at least 30 such units in each region of interest.
- Trials. "X moving and X stationary contained data from all correct and error trials" (Methods,
  "Subspace identification"): outcome hit or miss. Ignore trials, photostimulation trials and
  early-lick trials are left out: an assumption, as the paper's own task has no photostimulation and
  the paper does not say how MAP's early-lick and photostimulation trials were treated.
- Rates: 5 ms bins, causal Gaussian kernel of 20 ms s.d. (Methods, both sections). The kernel is
  truncated at 4 s.d., a standard choice.
- Z-scoring: baseline -2.1 to -1.85 s before the go cue (Methods, "Subspace identification"); mean and
  s.d. over the baseline bins of all trials. A unit with zero baseline s.d. is scaled by its s.d. over
  all bins (a standard choice, counted in the notebook). `zscore_mode="all"` is example.m's z-score
  over all bins and trials (claims, M3 variant).
- Trial windows (claims, M3): W1 -2.15 to +1.5 s around the go cue, W2 -1.8 to +1.5 s.
- Movement (claims, M4; Methods, "Curation..."): the mean of the jaw and nose speed, binned at 5 ms.
  Keypoint positions are first smoothed with a Gaussian of 3 frames s.d. (about 10 ms), a standard
  choice: unsmoothed, the frame-to-frame jitter of the tracking makes the speed histogram unimodal
  around 150 pixels/s, and no threshold separates movement from rest.
  The threshold sits between the two modes of the session's histogram; here Otsu's threshold on
  log10 speed, a standard automatic choice for the value separating two modes (the paper set it by
  hand). Bouts are runs of at least 100 ms; bouts 50 ms or less apart are merged. B1: shorter
  supra-threshold runs are stationary; B2: they are moving.
- Subspaces (claims, M5; Methods; subspaceID orthogonal_subspaces.m at commit d593949): maximise the
  Methods' objective on the Stiefel manifold with pymanopt's trust regions, each term normalised by
  the sum of the top-d eigenvalues of its covariance, from a random start drawn from the claim's seed.
- Dimensionality (claims, M5 and M9; Methods, "Dimensionality of subspaces"): eigenvalues above the
  95th percentile of eigenvalues from data with each neuron's time bins shuffled. To fit the time
  limit the shuffle uses `N_SHUFFLE` = 100 shuffles (the paper uses 1000) and every 4th 5 ms bin (20
  ms apart, the kernel's s.d.); both are deviations, recorded in the attempt.
- Variance explained (claims, M6): readings V1, V2, V3.
- Decoding (claims, M8; Methods, "Cross-region decoding"): ridge, lambda 0.01, source projections at t
  and the 8 preceding bins, 70/30 split of trials, R2 per bin over -1.8 to +1.5 s, averaged.
- Selectivity (claims, M7; Methods, "Identifying selective neurons"): AUROC per epoch, 1000 label
  shuffles, equal random samples of correct left and right trials.
"""

from __future__ import annotations

import json
import warnings
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy.ndimage import gaussian_filter1d
from scipy.signal import lfilter

DANDISET_ID = "000363"
DANDISET_VERSION = "0.231012.2129"

BIN = 0.005
SIGMA = 0.020
BASELINE = (-2.1, -1.85)
WINDOWS = {"W1": (-2.15, 1.5), "W2": (-1.8, 1.5)}
TASK_SPAN = (-1.8, 1.5)
EPOCHS = {"sample": (-1.8, -1.2), "early_delay": (-1.2, -0.5), "late_delay": (-0.5, 0.0),
          "early_response": (0.0, 0.5), "late_response": (0.5, 1.5)}
MIN_UNITS = 30
MEDULLA_NUCLEI = ("Intermediate reticular nucleus", "Gigantocellular reticular nucleus",
                  "Parvicellular reticular nucleus")
MIN_BOUT_BINS = 20      # 100 ms
MERGE_GAP_BINS = 10     # 50 ms
N_SHUFFLE = 100
SHUFFLE_STEP = 4
RIDGE_LAMBDA = 0.01
N_LAGS = 9
D_CAP = 20
TRACK_SMOOTH_FRAMES = 3   # Gaussian s.d. in frames (about 10 ms) on keypoint positions


def _dec(values):
    return [v.decode() if isinstance(v, bytes) else v for v in values]


def asset_urls():
    """(path, S3 url) of every asset of the pinned version."""
    ds = DandiAPIClient().get_dandiset(DANDISET_ID, DANDISET_VERSION)
    return [(a.path, a.get_content_url(follow_redirects=1, strip_query=True)) for a in ds.get_assets()]


def open_file(url):
    return h5py.File(remfile.File(url), "r")


def unit_table(url):
    """Per unit: probe target, classification, quality, CCF annotation, from the units table."""
    f = open_file(url)
    loc = _dec(f["general/extracellular_ephys/electrodes/location"][:])
    u = f["units"]
    el = u["electrodes"][:]
    idx = u["electrodes_index"][:]
    first = el[np.r_[0, idx[:-1]]]
    target = [json.loads(loc[i])["brain_regions"] for i in first]
    anno = [a if isinstance(a, str) else "" for a in _dec(u["anno_name"][:])]
    tr = f["intervals/trials"]
    classification = [c if isinstance(c, str) else "missing" for c in _dec(u["classification"][:])]
    return dict(target=target, classification=classification,
                quality=_dec(u["unit_quality"][:]), anno=anno,
                n_trials=int(tr["start_time"].shape[0]),
                subject=f["general/subject/subject_id"][()].decode())


def survey(assets, threads=8):
    with ThreadPoolExecutor(threads) as ex:
        tables = list(ex.map(lambda pa: unit_table(pa[1]), assets))
    return {p: t for (p, _), t in zip(assets, tables)}


def region_of(target, anno):
    """'left ALM', 'right ALM' or 'medulla' under the paper's CCF rule, else None."""
    if "ALM" in target and anno.startswith("Secondary motor area"):
        return target
    if anno in MEDULLA_NUCLEI:
        return "medulla"
    return None


def select_sessions(tables, min_units=MIN_UNITS):
    """Sessions and units under M1 and M2 (U1): units classified good with a CCF region."""
    bilateral, alm_med = {}, {}
    for path, t in tables.items():
        regions = {}
        for i, (tg, cl, an) in enumerate(zip(t["target"], t["classification"], t["anno"])):
            if cl != "good":
                continue
            r = region_of(tg, an)
            if r:
                regions.setdefault(r, []).append(i)
        n = {r: len(v) for r, v in regions.items()}
        if n.get("left ALM", 0) >= min_units and n.get("right ALM", 0) >= min_units:
            bilateral[path] = {"right ALM": regions["right ALM"], "left ALM": regions["left ALM"]}
        alm = [r for r in ("left ALM", "right ALM") if n.get(r, 0) >= min_units]
        if n.get("medulla", 0) >= min_units and alm:
            alm_med[path] = {"ALM": sorted(sum((regions[r] for r in alm), [])),
                             "medulla": regions["medulla"], "alm_sides": alm}
    return bilateral, alm_med


def load_session(url, unit_ids):
    """Spike times of the given units, the trial table, go cue times and jaw and nose tracking."""
    f = open_file(url)
    u = f["units"]
    idx = u["spike_times_index"][:]
    st_all = u["spike_times"]
    spikes = {}
    lo = min(unit_ids)
    hi = max(unit_ids)
    a0 = 0 if lo == 0 else int(idx[lo - 1])
    block = st_all[a0:int(idx[hi])]
    for i in unit_ids:
        s0 = (0 if i == 0 else int(idx[i - 1])) - a0
        spikes[i] = np.sort(block[s0:int(idx[i]) - a0])
    tr = f["intervals/trials"]
    trials = {k: _dec(tr[k][:]) for k in ("outcome", "trial_instruction", "early_lick", "photostim_duration")}
    trials["start_time"] = tr["start_time"][:]
    trials["stop_time"] = tr["stop_time"][:]
    go = f["acquisition/BehavioralEvents/go_start_times/timestamps"][:]
    bts = f["acquisition/BehavioralTimeSeries"]
    track = {}
    for part in ("Jaw", "Nose"):
        g = bts[f"Camera0_side_{part}Tracking"]
        track[part] = (g["timestamps"][:], g["data"][:, :2])
    return dict(spikes=spikes, trials=trials, go=go, track=track)


def go_times(sess):
    """Go cue time per trial: the go_start_time inside each trial's interval."""
    st, sp, go = sess["trials"]["start_time"], sess["trials"]["stop_time"], sess["go"]
    j = np.searchsorted(go, st)
    out = np.full(len(st), np.nan)
    ok = j < len(go)
    jj = j[ok]
    inside = (go[jj] >= st[ok]) & (go[jj] <= sp[ok])
    out[np.where(ok)[0][inside]] = go[jj[inside]]
    return out


def trial_mask(sess, correct_only=False):
    t = sess["trials"]
    out = np.array(t["outcome"])
    ok = np.isin(out, ["hit"] if correct_only else ["hit", "miss"])
    ok &= np.array(t["photostim_duration"]) == "N/A"
    ok &= np.array(t["early_lick"]) == "no early"
    ok &= np.isfinite(go_times(sess))
    return ok


def causal_kernel():
    lags = np.arange(0, int(4 * SIGMA / BIN) + 1)
    k = np.exp(-0.5 * (lags * BIN / SIGMA) ** 2)
    return k / k.sum()


def rates(spike_list, align, window):
    """Smoothed single-trial rates (Hz), array (trials, bins, units), bins of BIN from window[0]."""
    k = causal_kernel()
    pad = len(k)
    nb = int(round((window[1] - window[0]) / BIN))
    edges = align[:, None] + window[0] + BIN * np.arange(-pad, nb + 1)[None, :]
    out = np.empty((len(align), nb, len(spike_list)), dtype=np.float32)
    for j, s in enumerate(spike_list):
        c = np.diff(np.searchsorted(s, edges.ravel()).reshape(edges.shape), axis=1) / BIN
        out[:, :, j] = lfilter(k, [1.0], c, axis=1)[:, pad:]
    return out


def speed_bins(sess, align, window):
    """Mean jaw and nose speed (pixels/s) per 5 ms bin; NaN where there is no tracking."""
    nb = int(round((window[1] - window[0]) / BIN))
    per_part = []
    for part in ("Jaw", "Nose"):
        ts, xy = sess["track"][part]
        dt = np.diff(ts)
        seg = np.r_[0, np.where(dt > 0.05)[0] + 1, len(ts)]
        xs = np.empty_like(xy)
        for a, b in zip(seg[:-1], seg[1:]):
            xs[a:b] = gaussian_filter1d(xy[a:b], TRACK_SMOOTH_FRAMES, axis=0, mode="nearest")
        sp = np.hypot(*np.diff(xs, axis=0).T) / dt
        sp[dt > 0.05] = np.nan
        tmid = ts[1:]
        res = np.full((len(align), nb), np.nan)
        for i, a in enumerate(align):
            lo, hi = np.searchsorted(tmid, [a + window[0], a + window[1]])
            if hi <= lo:
                continue
            b = ((tmid[lo:hi] - a - window[0]) / BIN).astype(int)
            v = sp[lo:hi]
            good = np.isfinite(v) & (b >= 0) & (b < nb)
            s = np.bincount(b[good], v[good], minlength=nb)
            n = np.bincount(b[good], minlength=nb)
            with np.errstate(invalid="ignore", divide="ignore"):
                res[i] = np.where(n > 0, s / n, np.nan)
        per_part.append(res)
    with np.errstate(invalid="ignore"), warnings.catch_warnings():
        warnings.simplefilter("ignore", RuntimeWarning)
        return np.nanmean(np.stack(per_part), axis=0)


def otsu_threshold(values, nbins=200):
    """Otsu's threshold of a 1-d sample."""
    h, e = np.histogram(values, nbins)
    c = 0.5 * (e[1:] + e[:-1])
    w0 = np.cumsum(h)
    w1 = w0[-1] - w0
    m0 = np.cumsum(h * c) / np.maximum(w0, 1)
    m1 = (np.sum(h * c) - np.cumsum(h * c)) / np.maximum(w1, 1)
    between = w0 * w1 * (m0 - m1) ** 2
    return c[np.argmax(between[:-1])]


def _runs(b):
    """Start and end (exclusive) of runs of True in a 1-d bool array."""
    d = np.diff(np.r_[0, b.astype(int), 0])
    return np.where(d == 1)[0], np.where(d == -1)[0]


def movement_mask(speed, log_threshold, short_runs_move=False):
    """1 moving, 0 stationary, -1 no tracking; per trial and bin (claims, M4)."""
    out = np.full(speed.shape, -1, dtype=np.int8)
    with np.errstate(invalid="ignore", divide="ignore"):
        above = np.log10(speed) > log_threshold
    for i in range(speed.shape[0]):
        valid = np.isfinite(speed[i])
        a = above[i] & valid
        s, e = _runs(a)
        long_ = (e - s) >= MIN_BOUT_BINS
        mv = np.zeros(len(a), bool)
        bs, be = s[long_], e[long_]
        for k in range(len(bs)):
            mv[bs[k]:be[k]] = True
            if k + 1 < len(bs) and bs[k + 1] - be[k] <= MERGE_GAP_BINS:
                mv[be[k]:bs[k + 1]] = True
        if short_runs_move:
            mv |= a
        out[i] = np.where(valid, mv.astype(np.int8), -1)
    return out


def zscore(r, window, mode="baseline"):
    """Z-score each unit (claims, M3). Returns z and the number of units scaled by the fallback."""
    if mode == "all":
        flat = r.reshape(-1, r.shape[2])
        mu, sd = flat.mean(0), flat.std(0)
        n_fallback = 0
    else:
        b0 = int(round((BASELINE[0] - window[0]) / BIN))
        b1 = int(round((BASELINE[1] - window[0]) / BIN))
        if b0 < 0:
            raise ValueError("window does not hold the baseline")
        base = r[:, b0:b1].reshape(-1, r.shape[2])
        mu, sd = base.mean(0), base.std(0)
        allsd = r.reshape(-1, r.shape[2]).std(0)
        bad = sd <= 1e-9
        n_fallback = int(bad.sum())
        sd = np.where(bad, allsd, sd)
    sd = np.where(sd <= 1e-9, 1.0, sd)
    return ((r - mu) / sd).astype(np.float32), n_fallback


def cov(x):
    x = x - x.mean(0)
    return (x.T @ x / (len(x) - 1)).astype(np.float64)


def eig_desc(c):
    return np.sort(np.linalg.eigvalsh(c))[::-1]


def shuffle_dimension(x, rng, n_shuffle=N_SHUFFLE, step=SHUFFLE_STEP):
    """Eigenvalues above the 95th percentile of the time-shuffled null, counted (Methods)."""
    x = np.asarray(x[::step], dtype=np.float32)
    ev = eig_desc(cov(x))
    null = np.empty((n_shuffle, x.shape[1]))
    xs = x.copy()
    for s in range(n_shuffle):
        for j in range(x.shape[1]):
            xs[:, j] = x[rng.permutation(len(x)), j]
        null[s] = eig_desc(cov(xs))
    thr = np.percentile(null, 95, axis=0)
    return int(np.sum(ev > thr)), ev


def cap_dims(d_null, d_pot, n, mode):
    """D1: d_null + d_pot no larger than n; D2: each capped at 20 as well."""
    if mode == "D2":
        d_null, d_pot = min(d_null, D_CAP), min(d_pot, D_CAP)
    d_null, d_pot = max(d_null, 1), max(d_pot, 1)
    while d_null + d_pot > n:
        if d_null >= d_pot:
            d_null -= 1
        else:
            d_pot -= 1
    return d_null, d_pot


def orthogonal_subspaces(c_stat, c_mov, d_null, d_pot, rng):
    """Q_null, Q_pot maximising the Methods' objective (subspaceID, orthogonal_subspaces.m)."""
    import pymanopt
    from pymanopt.manifolds import Stiefel
    from pymanopt.optimizers import TrustRegions

    n = c_stat.shape[0]
    norm_null = eig_desc(c_stat)[:d_null].sum()
    norm_pot = eig_desc(c_mov)[:d_pot].sum()
    a = c_mov / norm_pot
    b = c_stat / norm_null
    manifold = Stiefel(n, d_pot + d_null)

    @pymanopt.function.numpy(manifold)
    def cost(q):
        qp, qn = q[:, :d_pot], q[:, d_pot:]
        return -0.5 * np.trace(qp.T @ a @ qp) - 0.5 * np.trace(qn.T @ b @ qn)

    @pymanopt.function.numpy(manifold)
    def egrad(q):
        return -np.hstack([a @ q[:, :d_pot], b @ q[:, d_pot:]])

    @pymanopt.function.numpy(manifold)
    def ehess(q, u):
        return -np.hstack([a @ u[:, :d_pot], b @ u[:, d_pot:]])

    q0, _ = np.linalg.qr(rng.standard_normal((n, d_pot + d_null)))
    problem = pymanopt.Problem(manifold, cost, euclidean_gradient=egrad, euclidean_hessian=ehess)
    q = TrustRegions(verbosity=0).run(problem, initial_point=q0).point
    return q[:, d_pot:], q[:, :d_pot]


def variance_explained(q, c, d=None):
    """Tr(Q'CQ) / sum of the top-d eigenvalues of C (Methods); d defaults to Q's width."""
    d = q.shape[1] if d is None else d
    return float(np.trace(q.T @ c @ q) / eig_desc(c)[:d].sum())


def participation_ratio(c):
    ev = eig_desc(c)
    return float(ev.sum() ** 2 / (ev ** 2).sum())


def lagged(p, lags=N_LAGS):
    """Predictors at bin t: p[t], p[t-1], ..., p[t-lags+1]; (trials, bins, dims*lags)."""
    out = [np.roll(p, k, axis=1) for k in range(lags)]
    return np.concatenate(out, axis=2)


def ridge_r2(src, tgt, train, test, bins, standardize, pooled, lam=None):
    """R2 on the test trials at each bin (claims, M8). src, tgt: (trials, bins, dims)."""
    lam = RIDGE_LAMBDA if lam is None else lam
    xl = lagged(src)
    r2 = np.empty(len(bins))
    for k, t in enumerate(bins):
        xtr, ytr = xl[train, t].astype(np.float64), tgt[train, t].astype(np.float64)
        xte, yte = xl[test, t].astype(np.float64), tgt[test, t].astype(np.float64)
        mx, my = xtr.mean(0), ytr.mean(0)
        sx = xtr.std(0, ddof=1) if standardize else np.ones(xtr.shape[1])
        sx = np.where(sx > 0, sx, 1.0)
        z = (xtr - mx) / sx
        w = np.linalg.solve(z.T @ z + lam * np.eye(z.shape[1]), z.T @ (ytr - my))
        pred = ((xte - mx) / sx) @ w + my
        res = ((yte - pred) ** 2).sum(0)
        tot = ((yte - yte.mean(0)) ** 2).sum(0)
        r2[k] = 1 - res.sum() / tot.sum() if pooled else np.mean(1 - res / tot)
    return r2


def selectivity_p(x, is_right, rng, n_shuffle=1000):
    """AUROC and the share of label shuffles at least as far from 0.5 (Methods)."""
    from scipy.stats import rankdata
    r = rankdata(x)
    n1 = int(is_right.sum())
    n2 = len(x) - n1
    obs = (r[is_right].sum() - n1 * (n1 + 1) / 2) / (n1 * n2)
    perms = np.array([rng.permutation(len(x)) for _ in range(n_shuffle)])
    lab = is_right[perms]
    sh = ((r[None, :] * lab).sum(1) - n1 * (n1 + 1) / 2) / (n1 * n2)
    p = np.mean(np.abs(sh - 0.5) >= abs(obs - 0.5))
    return obs, p


def fit_region(z, mv, rng, dim_mode="D1", dims=None):
    """Subspaces of one region (claims, M5). z: (trials, bins, units) z-scored rates; mv: movement
    mask (trials, bins). `dims` reuses (d_null, d_pot) from the shuffle; else they are estimated."""
    x = z.reshape(-1, z.shape[2])
    m = mv.ravel()
    xs, xm = x[m == 0], x[m == 1]
    if dims is None:
        dn_raw, _ = shuffle_dimension(xs, rng)
        dp_raw, _ = shuffle_dimension(xm, rng)
    else:
        dn_raw, dp_raw = dims
    dn, dp = cap_dims(dn_raw, dp_raw, x.shape[1], dim_mode)
    cs, cm, c = cov(xs), cov(xm), cov(x)
    qn, qp = orthogonal_subspaces(cs, cm, dn, dp, rng)
    return dict(d_raw=(dn_raw, dp_raw), d=(dn, dp), qn=qn, qp=qp, C=c, Cs=cs, Cm=cm,
                n_stat=len(xs), n_mov=len(xm))


def ve_readings(fit):
    """Null, potent and both, under V1, V2 and V3 (claims, M6)."""
    qn, qp, c = fit["qn"], fit["qp"], fit["C"]
    both = np.hstack([qn, qp])
    tot = np.trace(c)
    return {"V1": (variance_explained(qn, c), variance_explained(qp, c), variance_explained(both, c)),
            "V2": tuple(float(np.trace(q.T @ c @ q) / tot) for q in (qn, qp, both)),
            "V3": (variance_explained(qn, fit["Cs"]), variance_explained(qp, fit["Cm"]), np.nan)}
