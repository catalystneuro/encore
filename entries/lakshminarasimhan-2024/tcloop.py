"""Loading and measures for Lakshminarasimhan et al. (2024) on DANDI:000009.

The paper (Cell Reports 43, 114059) reanalysed the ALM and thalamus recordings of
Guo et al. (2017), deposited as dandiset 000009. This module streams the NWB files
of that dandiset at a pinned version, builds trial-averaged delay-period rates, and
holds the regressions of the paper's STAR Methods ("Estimation of readout weights",
"Analysis of corticothalamic communication", "Alignment between weights").

Where each parameter comes from. "Claims W<n>" refers to the numbered method notes
in the header of claims/lakshminarasimhan-2024.yaml, which cite the paper.

- Trials: correct trials only, grouped by choice (claims W2; Methods, "We restricted
  out analysis to trials in which the choice was correct"). Readings T1 (no
  photostimulation) and T2 (all correct trials) are both given (claims W2).
- Alignment: delay onset, which is the trial table's `pole_out_time` (claims W3;
  Methods, "We aligned spike trains of ALM neurons to the onset of the delay
  period"). Window: delay onset to the go cue (claims W3). The go cue
  (`cue_start_time`) is 1.3 s after delay onset in most trials and never earlier,
  so a fixed window of 1.3 s is used (WINDOW).
- Bin: 10 ms (claims W3, a standard choice that cannot change the outcome beyond
  the smoothing).
- Smoothing: Gaussian, sigma chosen on the validation set from 10, 25, 50, 100 and
  200 ms (claims W4; Methods, "width sigma as hyperparameter"). The spike trains
  are binned over a window padded by PAD on each side before smoothing and then
  cut to the analysis window, so that the edges are not set to zero (standard
  choice).
- Split: 80% training, 10% validation, 10% test, at random within each choice
  (claims W5; Methods, "Estimation of readout weights"). Larger test fractions
  (the training set shrinks to match) are run only as diagnostics.
- Activity: per choice, trial-averaged rates, left then right concatenated in time
  (claims W6; Methods).
- Readout: OLS of c(t) (-1 left, +1 right) on h(t) with an intercept (claims W7).
- PCs: eigendecomposition of the covariance of the training h(t), top K = 16
  (claims W8; Methods).
- R2: 1 - Var[y - yhat] / Var[y], variances over time (Methods, "Task
  performance", the paper's definition of R2).
- Thalamic regressions: OLS of r(t) on h(t) U_1:k, k = 1 to 16, and on all
  cortical units (claims W10; Methods, "Analysis of corticothalamic
  communication").
- Unit span. The files give no interval over which each unit was recorded, and
  most units fire only in part of the session. Reading U1 (main) uses every
  selected trial for every unit, as the files are; reading U2 (an assumption,
  shown as a variant) uses for each unit only the trials whose delay onset lies
  between its first and last spike, and leaves a unit out of a split when it has
  no such trial in one of the sets.
"""

import json
import zlib
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import remfile
import requests
from scipy.ndimage import gaussian_filter1d

DANDISET = "000009"
VERSION = "0.220126.1903"
API = "https://api.dandiarchive.org/api"
PAPER_KEY = "lakshminarasimhan-2024"

BIN = 0.01  # s, claims W3 (standard choice)
WINDOW = 1.3  # s, delay onset to go cue (claims W3)
PAD = 0.8  # s, padding for smoothing, 4 x the largest sigma (standard choice)
SIGMAS_MS = (10, 25, 50, 100, 200)  # claims W4 (standard grid)
K = 16  # number of PCs (Methods)
NT = int(round(WINDOW / BIN))  # bins per choice


def seed(claim_id, offset=0):
    """The claim's seed (docs/protocol.md): crc32 of '<paper key>/<claim id>'."""
    return zlib.crc32(f"{PAPER_KEY}/{claim_id}".encode()) + offset


def list_assets():
    """All assets of the pinned version, from the DANDI API."""
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=1000"
    out = []
    while url:
        r = requests.get(url, timeout=60)
        r.raise_for_status()
        d = r.json()
        out += d["results"]
        url = d["next"]
    return out


def version_info():
    r = requests.get(f"{API}/dandisets/{DANDISET}/versions/{VERSION}/info/", timeout=60)
    r.raise_for_status()
    return r.json()


def _s3_url(asset_id):
    r = requests.head(f"{API}/assets/{asset_id}/download/", allow_redirects=False, timeout=60)
    if r.status_code not in (301, 302, 307):
        r.raise_for_status()
        raise RuntimeError(f"no redirect for asset {asset_id}: {r.status_code}")
    return r.headers["Location"]


def _dec(a):
    return np.array([x.decode() if isinstance(x, bytes) else x for x in a])


def read_session(asset):
    """Stream one NWB file and return its units, electrode region and trial table."""
    f = h5py.File(remfile.File(_s3_url(asset["asset_id"])), "r")
    st = f["units/spike_times"][:]
    idx = f["units/spike_times_index"][:]
    starts = np.r_[0, idx[:-1]]
    spikes = [st[s:e] for s, e in zip(starts, idx)]
    eg = f["general/extracellular_ephys"]
    locs = sorted({eg[k].attrs["location"] for k in eg
                   if isinstance(eg[k], h5py.Group) and "location" in eg[k].attrs})
    locs = [x.decode() if isinstance(x, bytes) else x for x in locs]
    region = ";".join(sorted({l.split(";")[0].replace("brain_region:", "").strip() for l in locs}))
    tr = f["intervals/trials"]
    cols = [c.decode() if isinstance(c, bytes) else str(c) for c in tr.attrs["colnames"]]
    trials = {c: (_dec(tr[c][:]) if tr[c].dtype.kind in "OSU" else tr[c][:]) for c in cols}
    trials["id"] = tr["id"][:]
    units = {
        "id": f["units/id"][:],
        "cell_type": _dec(f["units/cell_type"][:]),
        "unit_x": f["units/unit_x"][:],
        "unit_y": f["units/unit_y"][:],
        "unit_z": f["units/unit_z"][:],
    }
    out = dict(path=asset["path"], subject=asset["path"].split("/")[0].replace("sub-", ""),
               region=region, location=locs, spikes=spikes, units=units, trials=trials,
               rate_hz=float(f["units/sampling_rate"][0]) if "sampling_rate" in f["units"] else None)
    f.close()
    return out


def read_sessions(assets, workers=8):
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(read_session, assets))


def select_trials(sess, reading="T1"):
    """Correct trials (claims W2): T1 without photostimulation, T2 all correct.

    Returns trial indices, choice (0 left, 1 right) and delay onset times. For a
    correct trial the lick direction is the trial type."""
    t = sess["trials"]
    ok = (t["response"] == "correct") & np.isfinite(t["pole_out_time"])
    if reading == "T1":
        ok &= t["stim_present"] == 0
    idx = np.flatnonzero(ok)
    choice = (t["type"][idx] == "lick right").astype(int)
    return idx, choice, t["pole_out_time"][idx]


def binned(sess, onsets):
    """Spike counts in BIN bins from onset - PAD to onset + WINDOW + PAD.

    Returns an array (trials, units, bins)."""
    nb = int(round((WINDOW + 2 * PAD) / BIN))
    edges = np.arange(nb + 1) * BIN - PAD
    out = np.zeros((len(onsets), len(sess["spikes"]), nb), dtype=np.float32)
    for u, sp in enumerate(sess["spikes"]):
        for i, t0 in enumerate(onsets):
            lo, hi = np.searchsorted(sp, [t0 - PAD, t0 + WINDOW + PAD])
            if hi > lo:
                out[i, u] = np.histogram(sp[lo:hi] - t0, edges)[0]
    return out


def smooth(counts, sigma_ms):
    """Gaussian smoothing of binned counts, in spikes/s, cut to the delay window."""
    x = gaussian_filter1d(counts / BIN, sigma_ms / 1000 / BIN, axis=-1, mode="nearest")
    p = int(round(PAD / BIN))
    return x[..., p:p + NT]


def in_span(sess, onsets):
    """(trials, units) True where the delay onset lies between the unit's first and
    last spike (reading U2)."""
    lo = np.array([s[0] if len(s) else np.inf for s in sess["spikes"]])
    hi = np.array([s[-1] if len(s) else -np.inf for s in sess["spikes"]])
    return (onsets[:, None] >= lo[None]) & (onsets[:, None] <= hi[None])


class Prepared:
    """Smoothed single-trial rates of one session for every sigma."""

    def __init__(self, sess, reading="T1"):
        self.path = sess["path"]
        self.region = sess["region"]
        idx, self.choice, self.onsets = select_trials(sess, reading)
        self.trial_ids = sess["trials"]["id"][idx]
        c = binned(sess, self.onsets)
        self.rates = {s: smooth(c, s) for s in SIGMAS_MS}  # (trials, units, NT)
        self.span = in_span(sess, self.onsets)
        self.n_units = c.shape[1]


def split(choice, rng, test_frac=0.1):
    """80/10/10 split within each choice (claims W5). Returns three index arrays.

    test_frac other than 0.1 (a diagnostic) takes the extra test trials from the
    training set; validation stays at 10%."""
    sets = [[], [], []]
    for c in (0, 1):
        i = rng.permutation(np.flatnonzero(choice == c))
        n = len(i)
        nv = max(1, int(round(0.1 * n)))
        nt = max(1, int(round(test_frac * n)))
        sets[0].append(i[nv + nt:])
        sets[1].append(i[:nv])
        sets[2].append(i[nv:nv + nt])
    return [np.concatenate(s) for s in sets]


def average(prep, trials, sigma, span=False):
    """Trial-averaged rates h(t) = [h_l(t) h_r(t)], shape (2 NT, units).

    With span=True (reading U2) each unit is averaged over its in-span trials only;
    a unit with none in a choice gets NaN."""
    x = prep.rates[sigma][trials]
    ch = prep.choice[trials]
    out = []
    for c in (0, 1):
        sel = ch == c
        if span:
            w = prep.span[trials][sel].astype(float)  # (trials, units)
            n = w.sum(0)
            with np.errstate(invalid="ignore", divide="ignore"):
                m = np.einsum("tu,tub->ub", w, x[sel]) / n[:, None]
            m[n == 0] = np.nan
        else:
            m = x[sel].mean(0)
        out.append(m.T)
    return np.vstack(out)


def choice_target():
    return np.r_[-np.ones(NT), np.ones(NT)]


def r2(y, yhat):
    """1 - Var[y - yhat] / Var[y], over time, per column (Methods, Task performance).

    NaN where y does not vary (a unit with no spike in the set)."""
    y = np.asarray(y)
    yhat = np.asarray(yhat)
    v = np.var(y, axis=0)
    with np.errstate(invalid="ignore", divide="ignore"):
        return np.where(v > 0, 1 - np.var(y - yhat, axis=0) / np.where(v > 0, v, 1), np.nan)


def ols(X, Y):
    """OLS with an intercept. Returns (weights, intercept)."""
    Xa = np.column_stack([X, np.ones(len(X))])
    b = np.linalg.lstsq(Xa, Y, rcond=None)[0]
    return b[:-1], b[-1]


def pcs(H, k=K):
    """Eigenvectors of the covariance of H (time x units), largest first, top k
    (all of them with k=None)."""
    Hc = H - H.mean(0)
    C = Hc.T @ Hc / (len(H) - 1)
    ev, U = np.linalg.eigh(C)
    o = np.argsort(ev)[::-1]
    return U[:, o[:k]], ev[o]


def chance_alignment(d):
    """Mean |z . u| / ||z|| of a random direction z with a fixed unit vector u in d
    dimensions: Gamma(d/2) / (sqrt(pi) Gamma((d+1)/2))."""
    from scipy.special import gammaln
    return float(np.exp(gammaln(d / 2) - gammaln((d + 1) / 2)) / np.sqrt(np.pi))


def half_correlation(a, b):
    """Correlation over time between the averages of two halves of a set, per
    column. The Spearman-Brown reliability of the whole set's average is
    2 r / (1 + r), applied in the notebook to the mean r."""
    a = a - a.mean(0)
    b = b - b.mean(0)
    with np.errstate(invalid="ignore", divide="ignore"):
        return (a * b).sum(0) / np.sqrt((a ** 2).sum(0) * (b ** 2).sum(0))


def alignment(m, n):
    """|m . n| / (||m|| ||n||) (Methods, Alignment between weights; absolute value as
    for the readout in the PC basis, claims W8)."""
    return abs(m @ n) / (np.linalg.norm(m) * np.linalg.norm(n))


def readout_fit(Htr, Hva, Hte):
    """Readout of choice: weights, validation and test R2 (claims W7)."""
    c = choice_target()
    w, b = ols(Htr, c)
    return w, b, float(r2(c, Hva @ w + b)), float(r2(c, Hte @ w + b))


def readout_pc_alignment(w, U):
    """Alignment of the readout with each PC i: |w . u_i| / ||w|| (claims W8).

    NaN for PCs beyond the number of units (possible under reading U2)."""
    a = np.full(K, np.nan)
    v = np.abs(w @ U) / np.linalg.norm(w)
    a[:len(v)] = v
    return a


def thalamic_regression(Htr, Hva, Hte, Rtr, Rva, Rte):
    """Regress every thalamic unit (columns of R) on the top k cortical PCs, k = 1
    to K, and on all cortical units (claims W10).

    Returns validation and test R2 of shape (K, units) for the PC regressions, the
    validation and test R2 of the regression on all units (units,), the
    corticothalamic weights from all K PCs mapped back to unit space (cortical
    units, thalamic units), those of the regression on all units, and U."""
    U, _ = pcs(Htr)
    mu = Htr.mean(0)
    Ztr, Zva, Zte = (Htr - mu) @ U, (Hva - mu) @ U, (Hte - mu) @ U
    r2va = np.zeros((K, Rtr.shape[1]))
    r2te = np.zeros((K, Rtr.shape[1]))
    r2tr = np.zeros((K, Rtr.shape[1]))
    for k in range(1, K + 1):
        b, c = ols(Ztr[:, :k], Rtr)
        r2va[k - 1] = r2(Rva, Zva[:, :k] @ b + c)
        r2te[k - 1] = r2(Rte, Zte[:, :k] @ b + c)
        r2tr[k - 1] = r2(Rtr, Ztr[:, :k] @ b + c)
    w_tc = U @ b  # weights of the k = K regression in unit space
    bf, cf = ols(Htr, Rtr)
    return dict(r2va=r2va, r2te=r2te, r2tr=r2tr, full_tr=r2(Rtr, Htr @ bf + cf),
                full_va=r2(Rva, Hva @ bf + cf),
                full_te=r2(Rte, Hte @ bf + cf), w_tc=w_tc, w_full=bf, U=U)


def normalized(r2k, full=None, how="N1"):
    """Normalized cumulative variance explained (claims W10).

    N1: R2(k) / R2(16). N2: R2(k) / R2 from all cortical units. N3: each unit's
    curve rescaled to run from 0 to 1 over k = 1 to 16."""
    if how == "N1":
        return r2k / r2k[-1]
    if how == "N2":
        return r2k / full
    lo, hi = r2k.min(0), r2k.max(0)
    return (r2k - lo) / (hi - lo)


def asset_sha256(asset_id):
    r = requests.get(f"{API}/assets/{asset_id}/", timeout=60)
    r.raise_for_status()
    return r.json().get("digest", {}).get("dandi:sha2-256")


def dumps(x):
    return json.dumps(x, indent=1, default=str)


# ---------------------------------------------------------------------------
# Analyses over splits (claims W5 to W10)

N_SPLITS = 10  # claims W5
N_SUB = 20  # claims W7 (R2) and W9 (P1)
N_KEEP = 53  # claims W7 and W9; Figure S6 legend, "subsampled to match ... (n=53 +/- 9)"


def _halves(test, choice):
    """The test trials in two halves within each choice, by alternate position in
    the (already random) test set, so that no random draw is added."""
    a, b = [], []
    for c in (0, 1):
        i = test[choice[test] == c]
        a.append(i[0::2])
        b.append(i[1::2])
    return np.concatenate(a), np.concatenate(b)


def _split_all(preps, rng, span, test_frac=0.1, halves=False):
    """Split every session; return per sigma the averages (tr, va, te), pooled over
    the sessions' units, and a mask of units finite in all three sets. With
    halves=True the averages of the two halves of the test set follow (te_a, te_b)."""
    sets = [split(p.choice, rng, test_frac) for p in preps]
    if halves:
        sets = [st + list(_halves(st[2], p.choice)) for p, st in zip(preps, sets)]
    out = {}
    for s in SIGMAS_MS:
        H = [np.hstack([average(p, st[i], s, span) for p, st in zip(preps, sets)]) for i in range(len(sets[0]))]
        keep = np.all([np.all(np.isfinite(h), 0) for h in H[:3]], 0)
        out[s] = (H, keep)
    return out


def readout_per_session(alm, rng, span=False, n_splits=N_SPLITS):
    """Reading R1: readout per ALM session, sigma chosen on the validation set.

    Returns per session arrays over splits: test R2, training R2, validation R2,
    chosen sigma, alignment with PCs 1 to 16 (n_splits, K), the fraction of the
    readout's squared norm in the span of PCs 1 to 16, and units used."""
    res = []
    for p in alm:
        d = dict(test=[], train=[], val=[], sigma=[], align=[], top16=[], n=[], path=p.path)
        for _ in range(n_splits):
            A = _split_all([p], rng, span)
            best = None
            for s in SIGMAS_MS:
                H, keep = A[s]
                H = [h[:, keep] for h in H]
                w, b, rv, rt = readout_fit(*H)
                if best is None or rv > best[0]:
                    best = (rv, rt, s, w, H, keep.sum())
            rv, rt, s, w, H, n = best
            U, _ = pcs(H[0])
            d["top16"].append(float(np.sum((w @ U) ** 2) / (w @ w)))
            d["test"].append(rt)
            d["val"].append(rv)
            d["train"].append(float(r2(choice_target(), H[0] @ w + ols(H[0], choice_target())[1])))
            d["sigma"].append(s)
            d["align"].append(readout_pc_alignment(w, U))
            d["n"].append(n)
        res.append({k: (np.array(v) if k != "path" else v) for k, v in d.items()})
    return res


def readout_pooled(alm, rng, span=False, n_splits=N_SPLITS, n_sub=N_SUB, n_keep=N_KEEP,
                   test_frac=0.1):
    """Reading R2: readout on the ALM units pooled over the sessions, subsampled to
    n_keep units n_sub times per split, sigma chosen on the validation set.

    Returns arrays over (split, subsample): test R2, training R2, sigma, the
    alignment with PCs 1 to 16, the alignment with every PC (all n_keep of them),
    and the correlation between the readout's outputs on the two halves of the
    test set (for a noise ceiling, a diagnostic)."""
    d = dict(test=[], train=[], sigma=[], align=[], align_all=[], rel=[])
    for _ in range(n_splits):
        A = _split_all(alm, rng, span, test_frac, halves=True)
        avail = np.flatnonzero(np.all([A[s][1] for s in SIGMAS_MS], 0))
        for _ in range(n_sub):
            sub = rng.choice(avail, size=min(n_keep, len(avail)), replace=False)
            best = None
            for s in SIGMAS_MS:
                H = [h[:, sub] for h in A[s][0]]
                w, b, rv, rt = readout_fit(*H[:3])
                if best is None or rv > best[0]:
                    best = (rv, rt, s, w, H, b)
            rv, rt, s, w, H, b = best
            U, _ = pcs(H[0])
            Ua, _ = pcs(H[0], None)
            d["test"].append(rt)
            d["train"].append(float(r2(choice_target(), H[0] @ w + b)))
            d["sigma"].append(s)
            d["align"].append(readout_pc_alignment(w, U))
            d["align_all"].append(np.abs(w @ Ua) / np.linalg.norm(w))
            d["rel"].append(float(half_correlation(H[3] @ w, H[4] @ w)))
    return {k: np.array(v) for k, v in d.items()}


def thalamic_analysis(alm, thal, rng, pool="P1", span=False, n_splits=N_SPLITS,
                      n_sub=N_SUB, n_keep=N_KEEP, test_frac=0.1):
    """Regressions of every thalamic unit on the pooled ALM population (claims W9,
    W10), with the alignments of figs6f-ct-alignment-not-significant.

    pool P1: the pooled ALM units subsampled to n_keep, n_sub times per split; P2:
    all pooled ALM units. Sigma is chosen per thalamic unit on the validation set:
    on R2(16) for the PC regressions and on the regression's own validation R2 for
    the regression on all units. Returns per thalamic unit the means over (split,
    subsample) of the test R2(k), k = 1 to 16 (K, units), the test R2 from all
    cortical units, the alignment of the corticothalamic weights (all 16 PCs, mapped
    back to units) with PC 1 and with the readout, the same for the weights of the
    regression on all units, the training-set R2 of both (a diagnostic, not a
    reading of any claim), and the number of fits that entered each mean.

    Diagnostics for the alignments: a_ro_same, the alignment with the readout fitted
    at the thalamic unit's own sigma (the main a_ro takes the readout at its own
    best sigma); c_ro and c_ro_same, the mean alignment of a random direction in the
    span of PCs 1 to 16 with the readout, chance_alignment(16) times the fraction of
    the readout's norm in that span (with PC 1 it is chance_alignment(16)); and
    ro16, that fraction."""
    n_t = sum(p.n_units for p in thal)
    acc = {k: [] for k in ("r2k", "full", "a_pc", "a_ro", "a_pc_full", "a_ro_full",
                           "r2k_train", "full_train", "a_ro_same", "c_ro", "c_ro_same", "ro16")}
    c16 = chance_alignment(K)
    for _ in range(n_splits):
        A = _split_all(alm, rng, span, test_frac)
        T = _split_all(thal, rng, span, test_frac)
        avail = np.flatnonzero(np.all([A[s][1] for s in SIGMAS_MS], 0))
        tkeep = np.all([T[s][1] for s in SIGMAS_MS], 0)
        subs = ([rng.choice(avail, size=min(n_keep, len(avail)), replace=False) for _ in range(n_sub)]
                if pool == "P1" else [avail])
        for sub in subs:
            fits, ro, w_s = {}, None, {}
            for s in SIGMAS_MS:
                H = [h[:, sub] for h in A[s][0]]
                R = [r[:, tkeep] for r in T[s][0]]
                fits[s] = thalamic_regression(*H, *R)
                w, b, rv, rt = readout_fit(*H)
                w_s[s] = w
                if ro is None or rv > ro[0]:
                    ro = (rv, w)
            w_ro = ro[1]
            va16 = np.array([fits[s]["r2va"][-1] for s in SIGMAS_MS])
            vaf = np.array([fits[s]["full_va"] for s in SIGMAS_MS])
            bs, bf = va16.argmax(0), vaf.argmax(0)
            out = {k: np.full((K, n_t) if k.startswith("r2k") else n_t, np.nan) for k in acc}
            cols = np.flatnonzero(tkeep)
            for j, u in enumerate(cols):
                f = fits[SIGMAS_MS[bs[j]]]
                out["r2k"][:, u] = f["r2te"][:, j]
                out["r2k_train"][:, u] = f["r2tr"][:, j]
                out["a_pc"][u] = alignment(f["w_tc"][:, j], f["U"][:, 0])
                out["a_ro"][u] = alignment(f["w_tc"][:, j], w_ro)
                w_same = w_s[SIGMAS_MS[bs[j]]]
                out["a_ro_same"][u] = alignment(f["w_tc"][:, j], w_same)
                frac = np.linalg.norm(f["U"].T @ w_ro) / np.linalg.norm(w_ro)
                out["ro16"][u] = frac
                out["c_ro"][u] = c16 * frac
                out["c_ro_same"][u] = c16 * np.linalg.norm(f["U"].T @ w_same) / np.linalg.norm(w_same)
                g = fits[SIGMAS_MS[bf[j]]]
                out["full"][u] = g["full_te"][j]
                out["full_train"][u] = g["full_tr"][j]
                out["a_pc_full"][u] = alignment(g["w_full"][:, j], g["U"][:, 0])
                out["a_ro_full"][u] = alignment(g["w_full"][:, j], w_ro)
            for k in acc:
                acc[k].append(out[k])
    res = {k: np.nanmean(np.array(v), 0) for k, v in acc.items()}
    res["n_fits"] = np.sum(np.isfinite(np.array(acc["full"])), 0)
    return res


def thalamic_ceiling(thal, rng, n_splits=N_SPLITS, test_frac=0.1):
    """Noise ceilings of the thalamic test-set averages (a diagnostic, not a
    reading of any claim), per sigma, as means over splits per unit:
    'train', the R2 of the test-set average r(t) predicted by the unit's own
    training-set average (what a perfect model of the training average reaches);
    'half', the correlation between the averages of the two halves of the test set."""
    acc = {s: {"train": [], "half": []} for s in SIGMAS_MS}
    for _ in range(n_splits):
        T = _split_all(thal, rng, False, test_frac, halves=True)
        for s in SIGMAS_MS:
            R, keep = T[s]
            acc[s]["train"].append(np.where(keep, r2(R[2], R[0]), np.nan))
            acc[s]["half"].append(np.where(keep, half_correlation(R[3], R[4]), np.nan))
    return {s: {k: np.nanmean(np.array(v), 0) for k, v in d.items()} for s, d in acc.items()}


# ---------------------------------------------------------------------------
# Clock check and the cost of the paper's simulations


def choice_decoding(prep_sess, onsets, choice, edges, rng, n_folds=5):
    """Cross-validated accuracy of a nearest-class-mean decoder of choice from the
    spike counts of all units in windows [edges[i], edges[i+1]) around each onset
    (a standard choice for the clock check of docs/protocol.md, Author step 2)."""
    X = np.zeros((len(onsets), len(prep_sess["spikes"]), len(edges) - 1))
    for u, sp in enumerate(prep_sess["spikes"]):
        for i, t0 in enumerate(onsets):
            lo, hi = np.searchsorted(sp, [t0 + edges[0], t0 + edges[-1]])
            X[i, u] = np.histogram(sp[lo:hi] - t0, edges)[0]
    folds = np.array_split(rng.permutation(len(onsets)), n_folds)
    acc = np.zeros(len(edges) - 1)
    for f in folds:
        trn = np.setdiff1d(np.arange(len(onsets)), f)
        mu = X[trn].mean(0)
        sd = X[trn].std(0) + 1e-9
        Z = (X - mu) / sd
        m0 = Z[trn][choice[trn] == 0].mean(0)
        m1 = Z[trn][choice[trn] == 1].mean(0)
        d0 = ((Z[f] - m0) ** 2).sum(1)
        d1 = ((Z[f] - m1) ** 2).sum(1)
        acc += ((d1 < d0).astype(int) == choice[f][:, None]).sum(0)
    return acc / len(onsets)


def rflo_motor(n_epochs, M, rng, N=256, g=1.5, dt=0.1, lr=0.1, duration=20, cycles=2):
    """The motor control model of the paper's code (thalamocortical__motor.py at
    commit 2aa94dd, tc_type 'random'): RFLO on thalamocortical and readout weights,
    fixed random corticothalamic weights. Used here only to time an epoch.
    Returns the error of each epoch."""
    f = np.tanh
    df = lambda x: 1 - np.tanh(x) ** 2
    wcc = g * rng.standard_normal((N, N)) / np.sqrt(N)
    wct = g * rng.standard_normal((N, M)) / np.sqrt(M)
    wr = (2 * rng.random((1, N)) - 1) / np.sqrt(N)
    wtc = g * rng.standard_normal((M, N)) / np.sqrt(N)
    B = rng.standard_normal((N, 1))
    z0 = rng.standard_normal((N, 1))
    h0 = f(z0)
    r0 = f(wtc @ h0)
    NT = int(duration / dt)
    k = np.arange(NT)
    ustar = sum(a * np.sin(m * 2 * np.pi * k * cycles / (NT - 1))
                for a, m in ((1, 1), (0.75, 2), (0.5, 4), (0.25, 6)))
    ustar /= ustar.std()
    errs = []
    for _ in range(n_epochs):
        h, r = h0, r0
        q = np.zeros((N, M))
        err = np.zeros(NT)
        for ti in range(NT):
            z = wcc @ h + wct @ r
            q = dt * df(z) * r.T + (1 - dt) * q
            h = (1 - dt) * h + dt * f(z)
            r = f(wtc @ h)
            u = (wr @ h)[0, 0]
            err[ti] = ustar[ti] - u
            wr += (lr / NT) * h.T * err[ti]
            wct += (lr / NT) * B * err[ti] * q
        errs.append((err ** 2).mean() / 2)
    return np.array(errs)
