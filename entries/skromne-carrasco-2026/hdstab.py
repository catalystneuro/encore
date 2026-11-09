"""Loading and measures for the head-direction imaging and electrophysiology of dandiset 001676.

Skromne Carrasco, Viejo & Peyrache (2026), "Months-long stability of the head-direction system",
Nature 652, 167-173, doi:10.1038/s41586-025-10096-w. The claims are in
claims/001676/10.1038-s41586-025-10096-w.yaml; "Methods" below means the paper's Methods.

Each imaging file is one 20-min session of one mouse. It holds dF/F of the CNMF_E ROIs
(`processing/ophys/DfOverF/ROI_dFF`, 30 Hz), head direction (`acquisition/head-direction`,
radians, 120 Hz), position, ROI masks, tuning curves in 120 bins of 3 degrees, and the CellReg
table of its protocol (`scratch/Cell registration`: one row per registered cell, one column per
session of the protocol, the ROI index or -1) with one score per row. The protocol and the
session's place in it are in `experiment_description` and `session_description` ("session k of
N"). Files are streamed from the archive at the pinned version; nothing is written to disk.

Where the parameters come from:

- Tuning curves: mean dF/F in 3 degree bins of head direction (dF/F summed per bin divided by
  the time in the bin), smoothed with a circular Gaussian kernel "(sigma = 12° bins)" (Methods,
  HD cell classification by Miniscope). The sigma is open in the claims file; both readings are
  kept, `SIGMAS` = 4 bins (12 degrees) and 12 bins (36 degrees). Head direction is interpolated
  at the imaging timestamps (a standard choice that cannot change a result at 120 Hz against
  30 Hz).
- HD cell: split-half tuning curve correlation >= 0.4, HDI averaged across sessions > 0.1, and
  sessions with HDI < 0.11 dropped; CellReg score > 0.8 (> 0.6 for Fig. 3); registered in at least
  six sessions (Figs. 1, 2) or two (Figs. 3, 4) (Methods, same section). HDI is Skaggs'
  information (Methods ref. 59) with mean dF/F in place of rate and log2 (claims file, opening
  comment), on the raw or the smoothed tuning curve (both readings, `hdi_raw`, `hdi_s_*`). The
  main reading in the notebooks is the 12 degree kernel with HDI on the smoothed curve, an
  assumption: the stored tuning curves match a 4-bin kernel, and this reading gives the paper's
  numbers of compared sessions (Figs. 1f,g, Extended Data Fig. 4a) and of offset values (Extended
  Data Fig. 4g). Which
  sessions enter the average HDI is not stated: the sessions where the ROI is registered and passes
  the split-half rule (an assumption; the average over all registered sessions is the variant
  `avg_all`). "Detected" in a session is read as registered by CellReg in it (an assumption).
- Change in preferred direction: shift at the maximum of the circular cross-correlation of the
  two tuning curves, circular mean over cells (Methods, Change in the preferred tuning).
  `pd_change(table, a, b)` and `shift_matrix` give the preferred direction in b minus that in a.
  The Methods do not fix the sign; the notebook says which sign each signed claim uses (the
  earlier session minus the later one, an assumption).
- Pairwise offset: shift at the maximum of the cross-correlation of two cells' tuning curves;
  its change is the minimum circular difference between two sessions (Methods, Change in the
  angular offset). Whether the offset is signed (-180 to 180 degrees) or unsigned (0 to 180) is not
  stated; both readings are run (`unsigned`). The paper's shuffle medians (51 to 57 degrees,
  Extended Data Figs. 4g, 6b, 7e) are those of unsigned offsets (for independent uniform offsets
  the median absolute difference is 180 (1 - 1/sqrt 2) = 52.7 degrees on 0-180, and 90 degrees for
  signed offsets), so unsigned is the main reading, an assumption.
- Decoding: XGBoost multiclass on 32 head-direction bins, dF/F smoothed with a Gaussian of sigma
  133 ms, normalized, averaged in 0.09 s bins, top 50% of population activity bins kept, z-scored;
  error the minimum circular difference; chance from time-reversed head direction (Methods,
  Decoding using extreme gradient-boosted trees). Library defaults for XGBoost (claims file).
  "Normalized" is read as division by each cell's maximum and population activity as the sum of
  the normalized activity (claims file, opening comment).
"""

from __future__ import annotations

import json
import re
import urllib.request
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import remfile
from scipy import stats
from scipy.ndimage import gaussian_filter1d

DANDISET_ID = "001676"
DANDISET_VERSION = "0.251205.2137"
API = "https://api.dandiarchive.org/api"

NBINS = 120            # 3 degree bins (Methods)
SIGMAS = {"12deg": 4.0, "12bins": 12.0}   # the two readings of "sigma = 12° bins"
SPLIT_MIN = 0.4
HDI_AVG_MIN = 0.1
HDI_SESSION_MIN = 0.11
DEC_SIGMA_S = 0.133
DEC_BIN_S = 0.09
DEC_NCLASS = 32

PROTOCOLS = {
    "4 consecutive weeks in a circular environment": "circular",
    "2 consecutive weeks in each environment, for a total of 4 environments": "multi",
    "4 environments are visited weekly in a random order, for 4 weeks": "random",
    "2 environments, one visited weekly and one visited monthly, for 5 weeks": "single",
}


def list_assets():
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/?page_size=1000"
    out = []
    while url:
        with urllib.request.urlopen(url) as r:
            page = json.load(r)
        out += page["results"]
        url = page["next"]
    return out


def asset_url(asset):
    return f"{API}/assets/{asset['asset_id']}/download/"


def _open(asset):
    last = None
    for _ in range(4):
        try:
            return h5py.File(remfile.File(asset_url(asset)), "r")
        except Exception as e:  # network hiccup; retried, then raised
            last = e
    raise last


def _s(f, key):
    v = f[key][()]
    return v.decode() if isinstance(v, bytes) else v


def circ_interp(t_new, t, ang):
    """Interpolate an angle (radians) at new times through its unit vector."""
    c = np.interp(t_new, t, np.cos(ang))
    s = np.interp(t_new, t, np.sin(ang))
    return np.mod(np.arctan2(s, c), 2 * np.pi)


def bin_tuning(dff, hd):
    """Raw tuning curves (cells x NBINS): mean dF/F per 3 degree bin, and occupancy (frames)."""
    b = np.minimum((hd / (2 * np.pi) * NBINS).astype(int), NBINS - 1)
    occ = np.bincount(b, minlength=NBINS).astype(float)
    tot = np.zeros((dff.shape[1], NBINS))
    np.add.at(tot.T, b, dff)
    with np.errstate(invalid="ignore", divide="ignore"):
        tc = tot / occ
    tc[:, occ == 0] = np.nan
    return tc, occ


def fill_nan_circ(tc):
    """Fill empty bins by circular linear interpolation (rare; empty bins only)."""
    tc = tc.copy()
    x = np.arange(NBINS)
    for i in range(tc.shape[0]):
        bad = np.isnan(tc[i])
        if bad.any() and (~bad).sum() > 1:
            tc[i, bad] = np.interp(x[bad], x[~bad], tc[i, ~bad], period=NBINS)
    return tc


def smooth(tc, sigma):
    return gaussian_filter1d(fill_nan_circ(tc), sigma, axis=1, mode="wrap")


def hdi(tc, occ):
    """Skaggs information (bits) of tuning curves with occupancy weights."""
    tc = fill_nan_circ(tc)
    p = occ / occ.sum()
    mean = (tc * p).sum(1, keepdims=True)
    with np.errstate(invalid="ignore", divide="ignore"):
        r = tc / mean
        v = np.where(r > 0, p * r * np.log2(r), 0.0)
    return v.sum(1)


def row_corr(a, b):
    a = a - a.mean(1, keepdims=True)
    b = b - b.mean(1, keepdims=True)
    with np.errstate(invalid="ignore", divide="ignore"):
        return (a * b).sum(1) / np.sqrt((a * a).sum(1) * (b * b).sum(1))


def decoder_features(dff, ts, hd_t, hd):
    """Binned, normalized population activity and head direction for decoding (Methods)."""
    fs = 1 / np.median(np.diff(ts))
    x = gaussian_filter1d(dff, DEC_SIGMA_S * fs, axis=0)
    mx = x.max(0)
    mx[mx == 0] = 1
    x = x / mx
    edges = np.arange(ts[0], ts[-1], DEC_BIN_S)
    idx = np.searchsorted(edges, ts, side="right") - 1
    n = len(edges) - 1
    keep = (idx >= 0) & (idx < n)
    cnt = np.bincount(idx[keep], minlength=n).astype(float)
    xb = np.zeros((n, dff.shape[1]))
    np.add.at(xb, idx[keep], x[keep])
    ok = cnt > 0
    xb = xb[ok] / cnt[ok, None]
    centers = (edges[:-1] + DEC_BIN_S / 2)[ok]
    hb = circ_interp(centers, hd_t, hd)
    return xb.astype(np.float32), hb.astype(np.float32)


def load_session(asset, decoding=False, masks=False, protocols=None):
    """Read one imaging session and reduce it to what the analyses use (see load_sessions).
    A session whose protocol is not in `protocols` (when given) is returned with its protocol,
    mouse and place in the protocol only, and `skipped` set."""
    f = _open(asset)
    d = {"path": asset["path"]}
    d["protocol"] = PROTOCOLS[_s(f, "general/experiment_description")]
    if protocols is not None and d["protocol"] not in protocols:
        d["mouse"] = int(_s(f, "general/subject/description").split()[-1])
        d["k"], d["n"] = [int(x) for x in re.match(r".*session (\d+) of (\d+)", _s(f, "session_description")).groups()]
        d["start"] = _s(f, "session_start_time")
        d["skipped"] = True
        f.close()
        return d
    d["mouse"] = int(_s(f, "general/subject/description").split()[-1])
    desc = _s(f, "session_description")
    m = re.match(r".*environment: (.*), session (\d+) of (\d+)", desc)
    d["env"], d["k"], d["n"] = m.group(1), int(m.group(2)), int(m.group(3))
    d["start"] = _s(f, "session_start_time")
    dff = f["processing/ophys/DfOverF/ROI_dFF/data"][:]
    ts = f["processing/ophys/DfOverF/ROI_dFF/timestamps"][:]
    hd = f["acquisition/head-direction/data"][:]
    hts = f["acquisition/head-direction/timestamps"][:]
    good = np.isfinite(hd)
    hd, hts = np.mod(hd[good], 2 * np.pi), hts[good]
    inside = (ts >= hts[0]) & (ts <= hts[-1])
    ts_i, dff_i = ts[inside], dff[inside]
    hdi_ = circ_interp(ts_i, hts, hd)
    d["nroi"] = dff.shape[1]
    d["nframes"] = dff.shape[0]
    d["fs"] = 1 / np.median(np.diff(ts))
    d["duration_s"] = ts[-1] - ts[0]
    d["hd_range"] = (float(hd.min()), float(hd.max()))
    d["dff_range"] = (float(np.nanmin(dff)), float(np.nanmax(dff)))
    tc, occ = bin_tuning(dff_i, hdi_)
    half = len(ts_i) // 2
    tc1, occ1 = bin_tuning(dff_i[:half], hdi_[:half])
    tc2, occ2 = bin_tuning(dff_i[half:], hdi_[half:])
    d["tc_raw"], d["occ"] = tc.astype(np.float32), occ
    d["tc_raw_halves"] = (tc1.astype(np.float32), tc2.astype(np.float32))
    d["occ_halves"] = (occ1, occ2)
    d["tc_stored"] = f["processing/ophys/tuning_curves/tuning_values"][:].astype(np.float32)
    d["tc_stored_roi"] = f["processing/ophys/tuning_curves/roi_id"][:]
    d["cellreg"] = f["scratch/Cell registration"][:]
    d["cellreg_score"] = f["scratch/Cell registration scores"][:]
    if decoding and d["protocol"] in ("multi", "single"):
        d["dec_x"], d["dec_hd"] = decoder_features(dff, ts, hts, hd)
    if masks and d["protocol"] == "circular" and d["k"] in (1, d["n"]):
        im = f["processing/ophys/ImageSegmentation/PlaneSegmentation/image_mask"][:]
        w = im.sum((1, 2))
        yy, xx = np.mgrid[: im.shape[1], : im.shape[2]]
        d["centroid"] = np.stack([(im * yy).sum((1, 2)) / w, (im * xx).sum((1, 2)) / w], 1)
        d["pixel_mm"] = f["general/optophysiology/ImagingPlane/grid_spacing"][:]
    d["hd_ts"] = (hts[0], hts[-1])
    f.close()
    for sig_name, sig in SIGMAS.items():
        s = smooth(tc, sig)
        s1, s2 = smooth(tc1, sig), smooth(tc2, sig)
        d[f"split_{sig_name}"] = row_corr(s1, s2)
        d[f"tc_{sig_name}"] = s.astype(np.float32)
        d[f"hdi_s_{sig_name}"] = hdi(s, occ)
    d["hdi_raw"] = hdi(tc, occ)
    return d


def load_sessions(assets, decoding=False, masks=False, protocols=None, workers=8):
    """Load sessions in parallel. `decoding` adds decoder features to the sessions of the
    multi-environment and single-visit protocols; `masks` adds ROI centroids to the first and last
    sessions of the circular protocol; `protocols` reads in full only the sessions of those
    protocols."""
    def one(a):
        return load_session(a, decoding=decoding, masks=masks, protocols=protocols)
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(one, assets))


# ---------------------------------------------------------------- circular statistics

def circ_mean(a, axis=None):
    return np.arctan2(np.sin(a).sum(axis), np.cos(a).sum(axis))


def resultant(a, axis=None):
    return np.hypot(np.cos(a).mean(axis), np.sin(a).mean(axis))


def wrap(a):
    """Wrap radians to (-pi, pi]."""
    return np.angle(np.exp(1j * np.asarray(a)))


def vtest(a, mu=0.0):
    """V-test as pycircstat.vtest: V = n R cos(mean - mu), one-sided p from u = V sqrt(2/n)."""
    a = np.asarray(a)
    n = len(a)
    V = n * resultant(a) * np.cos(circ_mean(a) - mu)
    u = V * np.sqrt(2 / n)
    return V, 1 - stats.norm.cdf(u)


def rayleigh(a):
    """Rayleigh test as pycircstat.rayleigh: z = n R^2 and Zar's p approximation."""
    a = np.asarray(a)
    n = len(a)
    Rn = n * resultant(a)
    z = Rn ** 2 / n
    p = np.exp(np.sqrt(1 + 4 * n + 4 * (n ** 2 - Rn ** 2)) - (1 + 2 * n))
    return z, p


def xcorr_shift(a, b):
    """Shift (radians, wrapped) at the maximum of the circular cross-correlation of rows of a and b.

    The shift s maximises sum_k a[k] b[k + s], so it is the change of preferred direction from
    a to b.
    """
    fa = np.fft.rfft(a - a.mean(-1, keepdims=True), axis=-1)
    fb = np.fft.rfft(b - b.mean(-1, keepdims=True), axis=-1)
    cc = np.fft.irfft(np.conj(fa) * fb, n=a.shape[-1], axis=-1)
    s = np.argmax(cc, axis=-1)
    return wrap(s * 2 * np.pi / a.shape[-1])


def pair_offsets(tc):
    """Angular offset (radians) of every ordered pair of rows of tc (cells x bins)."""
    n = tc.shape[0]
    i, j = np.triu_indices(n, 1)
    return i, j, xcorr_shift(tc[i], tc[j])


# ------------------------------------------------------------------- electrophysiology

def load_ephys(asset):
    """Spike times per unit, head direction and epochs of an electrophysiology file."""
    f = _open(asset)
    d = {"path": asset["path"], "mouse": _s(f, "general/subject/description")}
    st = f["units/spike_times"][:]
    idx = f["units/spike_times_index"][:]
    d["spikes"] = np.split(st, idx[:-1])
    d["unit_group"] = [g for g in f["units/electrode_group"][:]]
    d["group_names"] = [f[g].name.split("/")[-1] for g in d["unit_group"]]
    d["group_location"] = {k: f[f"general/extracellular_ephys/{k}"].attrs["location"]
                           for k in f["general/extracellular_ephys"] if k != "electrodes"}
    hd = f["acquisition/head-direction/data"][:]
    hts = f["acquisition/head-direction/timestamps"][:]
    pos = f["acquisition/Position/2D_position/data"][:]
    d["hd"], d["hd_t"], d["pos"] = hd, hts, pos
    ep = f["intervals/epochs"]
    tags = [t.decode() if isinstance(t, bytes) else t for t in ep["tags"][:]]
    ti = ep["tags_index"][:]
    d["epochs"] = [(float(a), float(b), tags[(ti[k - 1] if k else 0):ti[k]])
                   for k, (a, b) in enumerate(zip(ep["start_time"][:], ep["stop_time"][:]))]
    f.close()
    return d


# ------------------------------------------------------------------- HD cells per protocol

def group(sessions, mouse, protocol):
    """The sessions of one mouse and protocol, ordered by their number in the protocol."""
    g = sorted([s for s in sessions if s["mouse"] == mouse and s["protocol"] == protocol],
               key=lambda s: s["k"])
    return g


def registration_check(g):
    """Whether every file of a protocol carries the same CellReg table, and whether each column's
    ROI indices fit the session of that number."""
    same = all(np.array_equal(s["cellreg"], g[0]["cellreg"]) for s in g)
    R = g[0]["cellreg"]
    fits = [int(R[:, s["k"] - 1].max()) < s["nroi"] for s in g]
    covered = [len(set(R[:, s["k"] - 1][R[:, s["k"] - 1] >= 0])) == s["nroi"] for s in g]
    return {"same_table": same, "columns_fit": all(fits), "all_rois_registered": all(covered),
            "n_columns": R.shape[1], "n_sessions": len(g), "n_rows": R.shape[0]}


def hd_table(g, sigma="12deg", hdi_kind="raw", score_min=0.8, min_sessions=6, avg="pass"):
    """Registered cells x sessions of one protocol: which entries are usable HD cell sessions.

    Returns dict with `valid` (cells x sessions bool), `tc` (cells x sessions x NBINS, NaN where
    not valid), `R` (CellReg rows kept), the HD cell flag and the score. `avg` = "pass" averages
    HDI over sessions passing the split-half rule, "all" over all registered sessions.
    """
    R = g[0]["cellreg"]
    score = g[0]["cellreg_score"]
    ns = len(g)
    cols = [s["k"] - 1 for s in g]
    R = R[:, cols]
    reg = R >= 0
    split = np.full(R.shape, np.nan)
    hdiv = np.full(R.shape, np.nan)
    hkey = "hdi_raw" if hdi_kind == "raw" else f"hdi_s_{sigma}"
    for j, s in enumerate(g):
        r = R[:, j]
        ok = r >= 0
        split[ok, j] = s[f"split_{sigma}"][r[ok]]
        hdiv[ok, j] = s[hkey][r[ok]]
    passes = reg & (split >= SPLIT_MIN)
    use = passes if avg == "pass" else reg
    with np.errstate(invalid="ignore"):
        mean_hdi = np.nanmean(np.where(use, hdiv, np.nan), axis=1)
    is_hd = mean_hdi > HDI_AVG_MIN
    valid = passes & (hdiv >= HDI_SESSION_MIN) & is_hd[:, None]
    valid &= (score > score_min)[:, None] & (reg.sum(1) >= min_sessions)[:, None]
    return {"R": R, "valid": valid, "reg": reg, "passes": passes, "hdi": hdiv, "split": split,
            "is_hd": is_hd, "score": score, "sessions": g, "sigma": sigma}


def tc_of(table, i, j):
    s = table["sessions"][j]
    return s[f"tc_{table['sigma']}"][table["R"][i, j]].astype(float)


def pd_change(table, j_ref, j, shuffle_rng=None):
    """Per-cell change in preferred direction from session j_ref to j (radians) over HD cells
    valid in both; with `shuffle_rng`, cell identities in session j are permuted first."""
    both = np.where(table["valid"][:, j_ref] & table["valid"][:, j])[0]
    if len(both) == 0:
        return np.array([])
    a = np.stack([tc_of(table, i, j_ref) for i in both])
    b = np.stack([tc_of(table, i, j) for i in both])
    if shuffle_rng is not None:
        b = b[shuffle_rng.permutation(len(both))]
    return xcorr_shift(a, b)


def session_dates(g):
    import datetime as _dt
    return np.array([_dt.date.fromisoformat(s["start"][:10]) for s in g])


def day_diff(g):
    d = session_dates(g)
    return np.array([[(b - a).days for b in d] for a in d])


# --------------------------------------------------------------------- per-claim measures

def session_changes(table, ref, rng=None, n_shuffle=0):
    """Session-level change in preferred direction (circular mean over cells) of each session
    against session `ref` (an index, or "previous"); with n_shuffle, the shuffled values of each
    session (cell identity shuffled within the day), shape (sessions, n_shuffle).

    Returns arrays over the compared sessions: index, change (radians), number of cells, shuffles.
    """
    ns = table["valid"].shape[1]
    out_j, out_c, out_n, out_sh = [], [], [], []
    for j in range(ns):
        r = (j - 1) if ref == "previous" else ref
        if j == r or r < 0:
            continue
        d = pd_change(table, r, j)
        if len(d) == 0:
            continue
        out_j.append(j)
        out_c.append(circ_mean(d))
        out_n.append(len(d))
        if n_shuffle:
            out_sh.append([circ_mean(pd_change(table, r, j, shuffle_rng=rng)) for _ in range(n_shuffle)])
    return np.array(out_j), np.array(out_c), np.array(out_n), np.array(out_sh)


def all_offsets(table):
    """Per session, the matrix of pairwise offsets (radians) of its valid HD cells, NaN elsewhere."""
    nc, ns = table["valid"].shape
    offs = np.full((ns, nc, nc), np.nan, dtype=np.float32)
    for j in range(ns):
        cells = np.where(table["valid"][:, j])[0]
        if len(cells) < 2:
            continue
        tc = np.stack([tc_of(table, i, j) for i in cells])
        a, b, o = pair_offsets(tc)
        offs[j, cells[a], cells[b]] = o
    return offs


OFF_BINS = np.arange(0, 181, 3)


def offset_changes(offs, pairs, rng=None, n_shuffle=0, unsigned=False):
    """Absolute change of pairwise offset (degrees) for the given session pairs.

    With `unsigned`, offsets are taken as their absolute value (0 to 180 degrees) before the
    difference; otherwise the change is the minimum circular difference of the signed offsets.

    Returns per session pair the array of changes over cell pairs valid in both sessions, and,
    with n_shuffle, a (n_shuffle, len(OFF_BINS)) histogram of the shuffled changes pooled over the
    session pairs (cell pair identity shuffled within the second day), from which shuffled
    medians are read.
    """
    per = []
    hist = np.zeros((n_shuffle, len(OFF_BINS)), dtype=np.int64) if n_shuffle else None
    for a, b in pairs:
        oa, ob = offs[a], offs[b]
        m = np.isfinite(oa) & np.isfinite(ob)
        va, vb = oa[m], ob[m]
        if unsigned:
            va, vb = np.abs(va), np.abs(vb)
        ch = np.degrees(np.abs(wrap(va - vb)))
        per.append(ch)
        if n_shuffle and len(va) > 1:
            perm = np.argsort(rng.random((n_shuffle, len(vb))), axis=1)
            sh = np.degrees(np.abs(wrap(va[None, :] - vb[perm])))
            k = np.clip(np.round(sh / 3).astype(int), 0, len(OFF_BINS) - 1)
            idx = k + (np.arange(n_shuffle) * len(OFF_BINS))[:, None]
            hist += np.bincount(idx.ravel(), minlength=n_shuffle * len(OFF_BINS)).reshape(n_shuffle, -1)
    return per, hist


def hist_median(hist):
    c = np.cumsum(hist, axis=1)
    half = c[:, -1] / 2
    return OFF_BINS[np.argmax(c >= half[:, None], axis=1)]


def drift_rates(x_days, y, per="day"):
    """Drift rate (degrees per week, or per unit of x when per="unit") by the three readings of
    the claims file: (a) least-squares slope over all values, (b) slope over the means per x,
    (c) slope through the origin over all values."""
    x_days, y = np.asarray(x_days, float), np.asarray(y, float)
    ok = np.isfinite(y)
    x_days, y = x_days[ok], y[ok]
    f = 7.0 if per == "day" else 1.0
    a = stats.linregress(x_days, y).slope * f
    ux = np.unique(x_days)
    my = np.array([y[x_days == u].mean() for u in ux])
    b = stats.linregress(ux, my).slope * f if len(ux) > 1 else np.nan
    c = (x_days @ y) / (x_days @ x_days) * f
    return {"a": a, "b": b, "c": c}


def jaccard(table, reading="pair"):
    """Jaccard index of HD-cell presence for every pair of sessions; ROIs registered in both
    sessions (reading "pair") or in every session (reading "all")."""
    v, reg = table["valid"], table["reg"]
    ns = v.shape[1]
    J = np.full((ns, ns), np.nan)
    for a in range(ns):
        for b in range(a + 1, ns):
            rows = (reg[:, a] & reg[:, b]) if reading == "pair" else reg.all(1)
            x, y = v[rows, a], v[rows, b]
            u = (x | y).sum()
            J[a, b] = J[b, a] = (x & y).sum() / u if u else np.nan
    return J


def pv_corr(table, a, b, nbins=12, reading="bin"):
    """Population vector correlation of sessions a and b over cells valid in both, with tuning
    curves in `nbins` bins (raw curves averaged into coarser bins)."""
    cells = np.where(table["valid"][:, a] & table["valid"][:, b])[0]
    if len(cells) < 3:
        return np.nan
    g = table["sessions"]
    def pv(j):
        s = g[j]
        tc = fill_nan_circ(s["tc_raw"][table["R"][cells, j]].astype(float))
        return tc.reshape(len(cells), nbins, -1).mean(2)
    A, B = pv(a), pv(b)
    if reading == "bin":
        return np.nanmean([np.corrcoef(A[:, k], B[:, k])[0, 1] for k in range(nbins)])
    return np.corrcoef(A.ravel(), B.ravel())[0, 1]


def shift_matrix(table_a, ja, table_b=None, jb=None, cells=None):
    """Shifts of preferred direction from session ja to session jb between every pair of cells
    valid in both (rows: cell in ja, columns: cell in jb). The diagonal is each cell's own change;
    a permutation of the columns gives a cell identity shuffle within the second day."""
    table_b = table_a if table_b is None else table_b
    if cells is None:
        cells = np.where(table_a["valid"][:, ja] & table_b["valid"][:, jb])[0]
    if len(cells) == 0:
        return cells, np.zeros((0, 0))
    a = np.stack([tc_of(table_a, i, ja) for i in cells])
    b = np.stack([tc_of(table_b, i, jb) for i in cells])
    return cells, xcorr_shift(a[:, None, :], b[None, :, :])


def shuffled_means(M, rng, n_shuffle=1000):
    """Circular means over cells of the shifts after shuffling cell identity, n_shuffle times."""
    n = M.shape[0]
    perm = np.argsort(rng.random((n_shuffle, n)), axis=1)
    vals = M[np.arange(n)[None, :], perm]
    return circ_mean(vals, axis=1), resultant(vals, axis=1)


def load_raw(asset):
    """dF/F with its timestamps and head direction with its timestamps, unreduced."""
    f = _open(asset)
    out = (f["processing/ophys/DfOverF/ROI_dFF/data"][:], f["processing/ophys/DfOverF/ROI_dFF/timestamps"][:],
           f["acquisition/head-direction/data"][:], f["acquisition/head-direction/timestamps"][:])
    f.close()
    return out


def shifted_hdi(dff, ts, hd, hts, shifts_s, sigma=SIGMAS["12deg"]):
    """Median raw HDI and split-half correlation over ROIs with head direction shifted in time."""
    out = []
    for sh in shifts_s:
        inside = (ts + sh >= hts[0]) & (ts + sh <= hts[-1])
        h = circ_interp(ts[inside] + sh, hts, np.mod(hd, 2 * np.pi))
        tc, occ = bin_tuning(dff[inside], h)
        half = inside.sum() // 2
        t1, _ = bin_tuning(dff[inside][:half], h[:half])
        t2, _ = bin_tuning(dff[inside][half:], h[half:])
        out.append((sh, np.median(hdi(tc, occ)), np.median(row_corr(smooth(t1, sigma), smooth(t2, sigma)))))
    return out


def spike_tuning(spikes, t0, t1, hd_t, hd, sigma=SIGMAS["12deg"]):
    """Spike-count tuning curves (Hz) in 3 degree bins of one epoch, raw and smoothed, occupancy,
    and mean rates. Head direction samples are counted where the tracking has no gap."""
    m = (hd_t >= t0) & (hd_t <= t1)
    t, h = hd_t[m], np.mod(hd[m], 2 * np.pi)
    dt = np.median(np.diff(t))
    b = np.minimum((h / (2 * np.pi) * NBINS).astype(int), NBINS - 1)
    occ = np.bincount(b, minlength=NBINS) * dt
    tcs, rates = [], []
    for s in spikes:
        s = s[(s >= t[0]) & (s <= t[-1])]
        i = np.clip(np.searchsorted(t, s), 0, len(t) - 1)
        cnt = np.bincount(b[i], minlength=NBINS)
        with np.errstate(invalid="ignore", divide="ignore"):
            tcs.append(cnt / occ)
        rates.append(len(s) / (t[-1] - t[0]))
    tc = np.array(tcs)
    tc[:, occ == 0] = np.nan
    return tc, smooth(tc, sigma), occ, np.array(rates)
