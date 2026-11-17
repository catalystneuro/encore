"""Loading and measures for CRCNS hc-31 (Rich, Liaw & Lee 2014, Science 345:814).

The data set holds one MATLAB file, `resSave.mat`, a struct array whose elements 5 to 9 are the
five rats of the paper (resSave_readme.txt). It is streamed from the public CRCNS bucket into
memory and never written to disk. Spike times are in microseconds; track positions are in
inches (`unitsPerCm` = 0.3937), linearized from 0 at the start; open-field positions are in
camera pixels (`unitsPerCm` per animal).

Where the parameters come from (S = the supplement's Materials and Methods, "Place field
determination", unless stated; "claims" = the shared method of claims/rich-2014.yaml):

- Cells: rows of `ID` with every epoch <= 2 (resSave_readme.txt: "NB have to exclude
  interneurons ... valid = all(ID <= 2, 2)").
- Novel exploration: samples of `posMazeLinNov` (finite only on the novel section) inside each
  `sectInt` epoch of RUN1 (S, first paragraph; readme, "used for most of the analysis").
- Velocity: net linear displacement in a 1 s window, centred (S; centring is a standard
  choice, claims). Speed above 5 cm/s, direction from the sign (S).
- Rate maps: 1 cm bins, spikes and occupancy each smoothed by a Gaussian of SD 10 cm, bins with
  smoothed occupancy not above 0.001 s/cm dropped (S). The data set's own maps use 1 inch
  bins; this module follows the paper's 1 cm.
- Fields: at least 15 contiguous cm above 2 Hz, bounded where the rate falls below 2 Hz; at
  least one spike in at least 50% of passes in that direction (S). Pass readings P-a (a run in
  one direction that crosses the whole field) and P-b (any visit to the field's bins while
  moving in that direction, moving meaning above the maps' 5 cm/s) are those the claims file
  names. Spikes counted in a pass are those the maps use (speed above 5 cm/s). A run is a
  stretch of novel-section samples with the same direction of travel, broken at gaps over 1 s
  (a standard choice). Under P-a a field that reaches the end of the positions visited in the
  epoch's novel section cannot be crossed beyond that end, so an edge of the field within
  EDGE_CM (20 cm, two smoothing SDs) of either end is taken as reached when the run gets within
  EDGE_CM of that end (a standard choice; verifier round 1, problem 2). `edge_cm=False` gives
  the first version, which dropped such fields.
- Merging: an outbound and an inbound field merge when the overlap is at least 50% of either
  one's extent (S); the location is the peak of the mean of the two maps over the union (S).
- Open field (RUN3): 1 cm2 bins, Gaussian SD 5 cm, fields of at least 100 contiguous bins
  above 2 Hz (S, open field paragraph); speed and occupancy readings O-a and O-b from the
  claims file. Contiguity is 4-connectivity (a standard choice).
- Negative binomial: P(X = x) = Gamma(x + r) / (Gamma(r) x!) p^r (1 - p)^x, fitted by maximum
  likelihood (claims, opening comment; S, Population models).
"""

from __future__ import annotations

import io

import fsspec
import numpy as np
import pandas as pd
import scipy.io as sio
from scipy import optimize, special, stats
from scipy.ndimage import gaussian_filter, gaussian_filter1d, label

DATASET = "crcns:hc-31/unversioned"  # doi:10.6080/K0BV7DT2
URL = "https://crcnsarchive.s3-us-west-2.amazonaws.com/hc-31/live/data/resSave.mat"
MD5 = "f97e58107878c688854474519fa6be72"  # checksums.md5 of hc-31/live
PAPER_ELEMENTS = [4, 5, 6, 7, 8]  # resSave(5:9), zero-based
CM_PER_INCH = 2.54
TRACK_M = 48.0

SPEED_CM_S = 5.0
BIN_CM = 1.0
SMOOTH_CM = 10.0
MIN_OCC_S = 0.001
RATE_HZ = 2.0
MIN_WIDTH_CM = 15
PASS_FRACTION = 0.5
MERGE_OVERLAP = 0.5
RUN_GAP_S = 1.0
EDGE_CM = 20.0
OF_SMOOTH_CM = 5.0
OF_MIN_BINS = 100


def _list(x):
    if isinstance(x, np.ndarray) and x.dtype == object:
        return list(x.ravel())
    if np.size(x) == 0:
        return []
    return [x]


def load_raw():
    """Stream resSave.mat into memory; return the struct array and the MD5 of the bytes."""
    import hashlib
    with fsspec.open(URL, block_size=2**22) as f:
        data = f.read()
    md5 = hashlib.md5(data).hexdigest()
    m = sio.loadmat(io.BytesIO(data), squeeze_me=True, struct_as_record=False)
    return m["resSave"], md5


def centred_velocity(t_s, x_cm, window_s=1.0):
    """Net displacement over a centred window, divided by the window (cm/s)."""
    ok = np.isfinite(x_cm)
    xp = np.interp(t_s + window_s / 2, t_s[ok], x_cm[ok])
    xm = np.interp(t_s - window_s / 2, t_s[ok], x_cm[ok])
    v = (xp - xm) / window_s
    v[~ok] = np.nan
    return v


def _sample_dt(t_s):
    dt = np.diff(t_s, append=t_s[-1])
    med = np.median(dt[dt > 0])
    return np.clip(dt, 0, 2 * med)


def load_animals():
    """Per animal, the reduced data the analyses use."""
    res, md5 = load_raw()
    animals = []
    for el in PAPER_ELEMENTS:
        s = res[el]
        ID = np.asarray(s.ID, float)
        valid = np.all(ID <= 2, axis=1)
        idx = np.flatnonzero(valid)
        pl = s.posMazeLin[0].data
        pn = s.posMazeLinNov.data
        t = pl[:, 0] / 1e6
        x_cm = pl[:, 1] * CM_PER_INCH
        v = centred_velocity(t, x_cm)
        run3 = s.posMaze[2]
        a = dict(
            element=el + 1, animal=s.spAll[0].animal, n_units=len(valid), cells=idx,
            ID=ID[valid], sectInt=np.asarray(s.sectInt, float) / 1e6,
            sectExt_cm=np.asarray(s.sectExt, float) * CM_PER_INCH,
            t=t, x_cm=x_cm, x_nov_cm=pn[:, 1] * CM_PER_INCH, v=v, dt=_sample_dt(t),
            v_dataset=pl[:, 3] / s.posMazeLin[0].unitsPerCm * 1e6, dir_dataset=pl[:, 4],
            xy_room=s.posMaze[0].data[:, 1:3],
            run1=[np.asarray(s.spEpochSep[c, 1].timeStamps, float).ravel() / 1e6 for c in idx],
            pre=[np.asarray(s.spEpochSep[c, 0].timeStamps, float).ravel() / 1e6 for c in idx],
            run3=[np.asarray(s.spEpochSep[c, 3].timeStamps, float).ravel() / 1e6 for c in idx],
            run1_features=[np.asarray(s.spEpochSep[c, 1].features, float) for c in idx],
            mean_amplitude=np.array([[np.asarray(s.spEpochSep[c, k].features, float).reshape(-1, 4).mean(axis=0)
                                      if np.size(s.spEpochSep[c, k].features) else np.full(4, np.nan)
                                      for k in (0, 1, 3)] for c in idx]),
            run1_epoch=np.asarray(s.spEpochSep[idx[0], 1].clustInf.epochTimes, float) / 1e6,
            pre_epoch=np.asarray(s.spEpochSep[idx[0], 0].clustInf.epochTimes, float) / 1e6,
            tetrode=np.array([int(s.spAll[c].clustInf.TT) for c in idx]),
            tetrode_all=np.array([int(s.spAll[c].clustInf.TT) for c in range(len(valid))]),
            region=[s.spAll[c].clustInf.region for c in idx],
            region_all=[s.spAll[c].clustInf.region for c in range(len(valid))],
            lratio=np.array([np.nanmax(np.atleast_1d(s.spAll[c].clustInf.Lratio).astype(float))
                             if np.isfinite(np.atleast_1d(s.spAll[c].clustInf.Lratio).astype(float)).any()
                             else np.nan for c in idx]),
            isod=np.array([np.nanmax(np.atleast_1d(s.spAll[c].clustInf.IsoD).astype(float))
                           if np.isfinite(np.atleast_1d(s.spAll[c].clustInf.IsoD).astype(float)).any()
                           else np.nan for c in idx]),
            # finite L-ratio / isolation distance in each epoch's own cluster info (spEpochSep
            # columns PRE, RUN1, RUN2, RUN3), counted over the valid units
            cq_epochs={k: (int(sum(np.isfinite(np.atleast_1d(s.spEpochSep[c, k].clustInf.Lratio).astype(float)).any() for c in idx)),
                           int(sum(np.isfinite(np.atleast_1d(s.spEpochSep[c, k].clustInf.IsoD).astype(float)).any() for c in idx)))
                       for k in range(s.spEpochSep.shape[1])},
            cq_fieldnames=list(s.spEpochSep[idx[0], 1].clustInf._fieldnames),
            numFieldNovel=np.asarray(s.numFieldNovel, float)[valid],
            numField=np.asarray(s.numField, float)[valid],
            st=np.array([float(s.histo[c].st) for c in idx]),
            pd=np.array([float(s.histo[c].pd) for c in idx]),
            sws=np.asarray(s.intSWS.data, float).reshape(-1, 2) / 1e6,
            swr=np.asarray(s.intSWR.data, float).reshape(-1, 2) / 1e6,
            of_t=run3.data[:, 0] / 1e6, of_xy_cm=run3.data[:, 1:3] / run3.unitsPerCm,
            of_speed=run3.data[:, 3] / run3.unitsPerCm * 1e6, of_units_per_cm=run3.unitsPerCm,
            fields_dataset=_dataset_fields(s, idx),
        )
        animals.append(a)
    return animals, md5


def _dataset_fields(s, idx):
    """The data set's own fields (fieldInfoC, RUN1 columns), variant F-b."""
    rows = []
    for k, c in enumerate(idx):
        for e in range(4):
            for f in _list(s.fieldInfoC[c, e]):
                fc = np.atleast_1d(f.fieldCentre).astype(float)
                edge = np.atleast_1d(f.fieldEdge).astype(float)
                rows.append(dict(cell=k, epoch=e, isnov=int(f.isnov), sect=int(f.sect),
                                 loc_m=fc[0] * CM_PER_INCH / 100, direction=int(fc[2]),
                                 start_cm=edge[0] * CM_PER_INCH, end_cm=edge[1] * CM_PER_INCH,
                                 size_cm=float(f.size) * CM_PER_INCH, rate=float(f.inFieldRate),
                                 n_pass=int(np.size(f.passStart)),
                                 pass_start=np.atleast_1d(f.passStart).astype(float) / 1e6))
    return pd.DataFrame(rows)


# ---------------------------------------------------------------- linear track fields

def _runs(mask):
    """Start and end (exclusive) of runs of True."""
    m = np.concatenate([[False], mask, [False]]).astype(int)
    d = np.diff(m)
    return np.flatnonzero(d == 1), np.flatnonzero(d == -1)


def epoch_samples(a, e):
    t0, t1 = a["sectInt"][e]
    return np.flatnonzero((a["t"] >= t0) & (a["t"] <= t1) & np.isfinite(a["x_nov_cm"]))


def epoch_bins(a, e):
    lo, hi = a["sectExt_cm"][e]
    lo = max(lo, np.nanmin(a["x_nov_cm"][epoch_samples(a, e)]) - 1)
    return np.arange(np.floor(lo), np.ceil(hi) + BIN_CM, BIN_CM)


def _passes(a, samp, sign):
    """Runs of novel samples moving in one direction (sign of the centred velocity)."""
    t = a["t"][samp]
    d = np.sign(a["v"][samp]) == sign
    gap = np.diff(t, prepend=t[0]) > RUN_GAP_S
    out = []
    starts, ends = _runs(d)
    for s0, e0 in zip(starts, ends):
        cut = np.flatnonzero(gap[s0 + 1:e0]) + s0 + 1
        bounds = [s0, *cut, e0]
        for b0, b1 in zip(bounds[:-1], bounds[1:]):
            out.append(samp[b0:b1])
    return out


def directional_maps(a, cell, e):
    """Rate maps (Hz) for outbound (+1) and inbound (-1) travel on epoch e's novel section."""
    samp = epoch_samples(a, e)
    edges = epoch_bins(a, e)
    centres = edges[:-1] + BIN_CM / 2
    spikes = a["run1"][cell]
    t = a["t"]
    near = np.clip(np.searchsorted(t, spikes), 1, len(t) - 1)
    near = np.where(np.abs(t[near - 1] - spikes) < np.abs(t[near] - spikes), near - 1, near)
    in_ep = np.zeros(len(t), bool)
    in_ep[samp] = True
    close = np.abs(t[near] - spikes) < 0.1
    maps = {}
    for sign in (1, -1):
        use = in_ep & (np.abs(a["v"]) > SPEED_CM_S) & (np.sign(a["v"]) == sign)
        occ, _ = np.histogram(a["x_nov_cm"][use], edges, weights=a["dt"][use])
        sp_ok = close & use[near]
        cnt, _ = np.histogram(a["x_nov_cm"][near[sp_ok]], edges)
        sigma = SMOOTH_CM / BIN_CM
        occ_s = gaussian_filter1d(occ, sigma, mode="constant")
        cnt_s = gaussian_filter1d(cnt.astype(float), sigma, mode="constant")
        rate = np.full(len(centres), np.nan)
        ok = occ_s > MIN_OCC_S * BIN_CM
        rate[ok] = cnt_s[ok] / occ_s[ok]
        maps[sign] = dict(rate=rate, occ=occ, spike_times=spikes[sp_ok],
                          spike_x=a["x_nov_cm"][near[sp_ok]])
    return centres, maps, samp


def _reach_bounds(a, samp, x0, x1, edge_cm=None):
    """Field edges a P-a pass must reach: an edge within edge_cm of the end of the positions
    visited in the epoch's novel section is moved to edge_cm from that end."""
    if edge_cm is False:  # the first version: the field's own edges
        return x0, x1
    edge_cm = EDGE_CM if edge_cm is None else edge_cm
    xs = a["x_nov_cm"][samp]
    lo, hi = np.nanmin(xs), np.nanmax(xs)
    y0 = min(max(x0, lo + edge_cm), x1)
    y1 = max(min(x1, hi - edge_cm), y0)
    return y0, y1


def _detect(centres, m, a, samp, sign, pass_rule, edge_cm=None, keep_all=False):
    """Fields of one directional map. keep_all=True returns every stretch above 2 Hz with
    its width and passes and the step that rejects it (`rejected`: width, passes or none)."""
    rate = m["rate"]
    above = np.nan_to_num(rate, nan=0.0) > RATE_HZ
    starts, ends = _runs(above)
    fields = []
    passes = _passes(a, samp, sign)
    for s0, e0 in zip(starts, ends):
        if (e0 - s0) * BIN_CM < MIN_WIDTH_CM:
            if keep_all:
                fields.append(dict(i0=s0, i1=e0, n_pass=0, n_hit=0, rejected="width"))
            continue
        x0, x1 = centres[s0] - BIN_CM / 2, centres[e0 - 1] + BIN_CM / 2
        n_pass = n_hit = 0
        if pass_rule == "P-a":
            y0, y1 = _reach_bounds(a, samp, x0, x1, edge_cm)
            visits = [p for p in passes
                      if np.nanmin(a["x_nov_cm"][p]) <= y0 and np.nanmax(a["x_nov_cm"][p]) >= y1]
        else:
            visits = []
            for p in passes:
                xp = a["x_nov_cm"][p]
                inside = (xp >= x0) & (xp <= x1) & (np.abs(a["v"][p]) > SPEED_CM_S)
                for b0, b1 in zip(*_runs(inside)):
                    visits.append(p[b0:b1])
        st, sx = m["spike_times"], m["spike_x"]
        for p in visits:
            n_pass += 1
            tp0, tp1 = a["t"][p[0]], a["t"][p[-1]] + a["dt"][p[-1]]
            if np.any((st >= tp0) & (st <= tp1) & (sx >= x0) & (sx <= x1)):
                n_hit += 1
        bad = n_pass == 0 or n_hit < PASS_FRACTION * n_pass
        if bad and not keep_all:
            continue
        fields.append(dict(i0=s0, i1=e0, n_pass=n_pass, n_hit=n_hit, rejected="passes" if bad else "none"))
    return fields


def pass_counts(a, e, sign, x0, x1):
    """Passes through [x0, x1] cm in one direction of epoch e under P-a and P-b."""
    samp = epoch_samples(a, e)
    passes = _passes(a, samp, sign)
    y0, y1 = _reach_bounds(a, samp, x0, x1)
    n_a = sum(1 for p in passes
              if np.nanmin(a["x_nov_cm"][p]) <= y0 and np.nanmax(a["x_nov_cm"][p]) >= y1)
    n_b = 0
    for p in passes:
        xp = a["x_nov_cm"][p]
        inside = (xp >= x0) & (xp <= x1) & (np.abs(a["v"][p]) > SPEED_CM_S)
        n_b += len(_runs(inside)[0])
    return n_a, n_b


def candidate_fields(a, cell, e, pass_rule="P-a", edge_cm=None):
    """Every stretch above 2 Hz of both directional maps, before the width and pass rules, with
    the step that rejects it (diagnostic, verifier round 1, problem 3)."""
    centres, maps, samp = directional_maps(a, cell, e)
    rows = []
    for sign in (1, -1):
        for f in _detect(centres, maps[sign], a, samp, sign, pass_rule, edge_cm, keep_all=True):
            rows.append(dict(sign=sign, start_cm=centres[f["i0"]] - BIN_CM / 2,
                             end_cm=centres[f["i1"] - 1] + BIN_CM / 2, n_pass=f["n_pass"],
                             n_hit=f["n_hit"], rejected=f["rejected"]))
    return rows


def cell_epoch_fields(a, cell, e, pass_rule="P-a", edge_cm=None):
    """Merged fields of one cell in one epoch's novel section."""
    centres, maps, samp = directional_maps(a, cell, e)
    det = {sign: _detect(centres, maps[sign], a, samp, sign, pass_rule, edge_cm) for sign in (1, -1)}
    items = [(sign, f) for sign in (1, -1) for f in det[sign]]
    # union-find over overlapping opposite-direction fields
    parent = list(range(len(items)))

    def find(i):
        while parent[i] != i:
            i = parent[i]
        return i
    for i, (si, fi) in enumerate(items):
        for j, (sj, fj) in enumerate(items):
            if j <= i or si == sj:
                continue
            ov = min(fi["i1"], fj["i1"]) - max(fi["i0"], fj["i0"])
            if ov > 0 and (ov >= MERGE_OVERLAP * (fi["i1"] - fi["i0"])
                           or ov >= MERGE_OVERLAP * (fj["i1"] - fj["i0"])):
                parent[find(j)] = find(i)
    groups = {}
    for i in range(len(items)):
        groups.setdefault(find(i), []).append(items[i])
    out = []
    for g in groups.values():
        signs = {s for s, _ in g}
        i0 = min(f["i0"] for _, f in g)
        i1 = max(f["i1"] for _, f in g)
        if len(signs) == 2:
            mean_map = np.nanmean(np.vstack([maps[1]["rate"], maps[-1]["rate"]]), axis=0)
            seg = mean_map[i0:i1]
            direction = 3
            widths = [(f["i1"] - f["i0"]) * BIN_CM for _, f in g]
            rates = [np.nanmean(maps[s]["rate"][f["i0"]:f["i1"]]) for s, f in g]
            size_b, rate_b = float(np.mean(widths)), float(np.mean(rates))
        else:
            sign = g[0][0]
            seg = maps[sign]["rate"][i0:i1]
            direction = 1 if sign == 1 else 2
            size_b = (i1 - i0) * BIN_CM
            rate_b = float(np.nanmean(seg))
        peak = i0 + int(np.nanargmax(seg))
        # the field reaches an end of its map: the first or last bin, or a bin dropped for occupancy
        touches = bool(i0 == 0 or i1 == len(centres) or any(
            not np.isfinite(maps[s]["rate"][i0 - 1]) or not np.isfinite(maps[s]["rate"][i1])
            for s in signs))
        out.append(dict(epoch=e, loc_m=centres[peak] / 100, direction=direction, touches_end=touches,
                        start_cm=centres[i0] - BIN_CM / 2, end_cm=centres[i1 - 1] + BIN_CM / 2,
                        size_cm=(i1 - i0) * BIN_CM, rate=float(np.nanmean(seg)),
                        size_b=size_b, rate_b=rate_b, peak_rate=float(np.nanmax(seg))))
    return out


def track_fields(animals, pass_rule="P-a", edge_cm=None):
    """All novel fields of all cells (F-a), one row per merged field."""
    rows = []
    for ai, a in enumerate(animals):
        for k in range(len(a["cells"])):
            for e in range(4):
                for f in cell_epoch_fields(a, k, e, pass_rule, edge_cm):
                    rows.append(dict(animal=a["animal"], ai=ai, cell=k, **f))
    return pd.DataFrame(rows)


def cell_table(animals):
    rows = []
    for ai, a in enumerate(animals):
        for k in range(len(a["cells"])):
            rows.append(dict(animal=a["animal"], ai=ai, cell=k, tetrode=a["tetrode"][k],
                             st=a["st"][k], pd=a["pd"][k], nov_dataset=a["numFieldNovel"][k]))
    return pd.DataFrame(rows)


def counts(fields, cells):
    """Number of fields per cell, every cell included (zeros for cells with none)."""
    c = fields.groupby(["ai", "cell"]).size()
    key = list(zip(cells.ai, cells.cell))
    return np.array([c.get(k, 0) for k in key])


def dataset_field_table(animals):
    rows = []
    for ai, a in enumerate(animals):
        f = a["fields_dataset"]
        f = f[f.isnov == 1].copy()
        f.insert(0, "ai", ai)
        f.insert(0, "animal", a["animal"])
        rows.append(f)
    return pd.concat(rows, ignore_index=True)


# ---------------------------------------------------------------- open field

def open_field_fields(a, cell, reading="O-a"):
    """Number of open-field (RUN3) fields of a cell, and the peak rate."""
    t, xy = a["of_t"], a["of_xy_cm"]
    ok = np.all(np.isfinite(xy), axis=1)
    if reading == "O-a":
        ok &= a["of_speed"] > SPEED_CM_S
    dt = _sample_dt(t)
    lo = np.floor(np.nanmin(xy, axis=0)) - 10
    hi = np.ceil(np.nanmax(xy, axis=0)) + 10
    ex = np.arange(lo[0], hi[0] + 1, 1.0)
    ey = np.arange(lo[1], hi[1] + 1, 1.0)
    occ, _, _ = np.histogram2d(xy[ok, 0], xy[ok, 1], [ex, ey], weights=dt[ok])
    sp = a["run3"][cell]
    near = np.clip(np.searchsorted(t, sp), 1, len(t) - 1)
    near = np.where(np.abs(t[near - 1] - sp) < np.abs(t[near] - sp), near - 1, near)
    good = (np.abs(t[near] - sp) < 0.1) & ok[near]
    cnt, _, _ = np.histogram2d(xy[near[good], 0], xy[near[good], 1], [ex, ey])
    occ_s = gaussian_filter(occ, OF_SMOOTH_CM, mode="constant")
    cnt_s = gaussian_filter(cnt, OF_SMOOTH_CM, mode="constant")
    rate = np.where(occ_s > MIN_OCC_S, cnt_s / np.where(occ_s > 0, occ_s, 1), 0.0)
    lab, n = label(rate > RATE_HZ)
    if n == 0:
        return 0, float(rate.max())
    sizes = np.bincount(lab.ravel())[1:]
    return int((sizes >= OF_MIN_BINS).sum()), float(rate.max())


# ---------------------------------------------------------------- models and tests

def nb_logpmf(x, r, p):
    return special.gammaln(x + r) - special.gammaln(r) - special.gammaln(x + 1) + r * np.log(p) + x * np.log1p(-p)


def nbinfit(x):
    """Maximum likelihood r, p of the negative binomial (MATLAB nbinfit parameterization)."""
    x = np.asarray(x, float)
    m = x.mean()

    def nll(lr):
        r = np.exp(lr)
        p = r / (r + m)  # profile MLE of p given r
        return -np.sum(nb_logpmf(x, r, p))
    res = optimize.minimize_scalar(nll, bounds=(-8, 8), method="bounded", options={"xatol": 1e-8})
    r = float(np.exp(res.x))
    return r, r / (r + m), -res.fun


def lomax_cdf(x_m, r, p, length=TRACK_M):
    """Recruitment by distance x under the gamma-Poisson model: 1 - (beta/(beta+x))^r."""
    beta = length * p / (1 - p)
    return 1 - (beta / (beta + np.asarray(x_m, float))) ** r


def lomax_inverse(q, r, p, length=TRACK_M):
    beta = length * p / (1 - p)
    return beta * ((1 - q) ** (-1 / r) - 1)


def censored_ks(first_m, F, length):
    """KS distance between the observed recruitment curve (all cells, NaN = never recruited)
    and the predicted CDF F over [0, length]."""
    x = np.sort(first_m[np.isfinite(first_m) & (first_m <= length)])
    n = len(first_m)
    if len(x) == 0:
        return float(F(length))
    Fx = F(x)
    hi = np.arange(1, len(x) + 1) / n
    lo = np.arange(0, len(x)) / n
    d = max(np.max(np.abs(hi - Fx)), np.max(np.abs(lo - Fx)), abs(len(x) / n - F(length)))
    return float(d)


def ad_statistic(u):
    """Anderson-Darling A^2 of probability-integral-transformed values u (each row a sample)."""
    u = np.sort(np.clip(np.atleast_2d(u), 1e-12, 1 - 1e-12), axis=1)
    n = u.shape[1]
    i = np.arange(1, n + 1)
    s = np.sum((2 * i - 1) * (np.log(u) + np.log1p(-u[:, ::-1])), axis=1)
    return -n - s / n


def ad_uniform_p(x, lo, hi, rng, n_mc=20000):
    """AD test of x against uniform on [lo, hi], simple null; p by Monte Carlo."""
    a2 = ad_statistic((np.asarray(x) - lo) / (hi - lo))[0]
    null = ad_statistic(rng.random((n_mc, len(x))))
    return float(a2), float((np.sum(null >= a2) + 1) / (n_mc + 1))


def ad_exponential_p(x, rng, composite=True, n_mc=20000):
    """AD test of x against the exponential with the sample mean. composite=True: the null
    distribution re-estimates the mean in every sample (E-a, Lilliefors-type, as MATLAB's
    adtest); False: the simple null with the mean taken as known (E-b)."""
    x = np.asarray(x, float)
    a2 = ad_statistic(1 - np.exp(-x / x.mean()))[0]
    sim = rng.exponential(1.0, (n_mc, len(x)))
    if composite:
        sim = sim / sim.mean(axis=1, keepdims=True)
    null = ad_statistic(1 - np.exp(-sim))
    return float(a2), float((np.sum(null >= a2) + 1) / (n_mc + 1))


def bh(p):
    """Benjamini-Hochberg adjusted p-values."""
    p = np.asarray(p, float)
    n = len(p)
    o = np.argsort(p)
    adj = np.empty(n)
    cm = np.minimum.accumulate((p[o] * n / np.arange(1, n + 1))[::-1])[::-1]
    adj[o] = np.minimum(cm, 1)
    return adj


def first_field(fields, cells, start=0.0, reverse=False):
    """Per cell, the distance from `start` to its first field beyond it (NaN when none)."""
    out = np.full(len(cells), np.nan)
    key = {k: i for i, k in enumerate(zip(cells.ai, cells.cell))}
    for (ai, c), g in fields.groupby(["ai", "cell"]):
        loc = g.loc_m.values
        d = (start - loc) if reverse else (loc - start)
        d = d[d >= 0]
        if len(d):
            out[key[(ai, c)]] = d.min()
    return out


def sws_rates(a):
    """PRE slow-wave-sleep rate per cell, from the data set's intSWS periods."""
    iv = a["sws"]
    total = np.sum(iv[:, 1] - iv[:, 0])
    rates = []
    for sp in a["pre"]:
        n = sum(np.sum((sp >= s0) & (sp <= s1)) for s0, s1 in iv)
        rates.append(n / total)
    return np.array(rates), total


def run_rate(a, cell, novel_only=True, speed=True):
    """RUN1 rate over time with speed above 5 cm/s (Fig. S5 legend); Z-a novel only, Z-b all
    track time of RUN1 epochs. speed=False with novel_only=False is a variant: all RUN1 track
    time, no speed threshold (verifier round 1)."""
    t = a["t"]
    in_ep = np.zeros(len(t), bool)
    for e in range(4):
        idx = epoch_samples(a, e) if novel_only else np.flatnonzero(
            (t >= a["sectInt"][e][0]) & (t <= a["sectInt"][e][1]) & np.isfinite(a["x_cm"]))
        in_ep[idx] = True
    use = in_ep & (np.abs(a["v"]) > SPEED_CM_S) if speed else in_ep
    sp = a["run1"][cell]
    near = np.clip(np.searchsorted(t, sp), 1, len(t) - 1)
    near = np.where(np.abs(t[near - 1] - sp) < np.abs(t[near] - sp), near - 1, near)
    ok = (np.abs(t[near] - sp) < 0.1) & use[near]
    return ok.sum() / np.sum(a["dt"][use])


def cluster_quality(features, noise):
    """L-ratio and isolation distance (Schmitzer-Torbert et al. 2005) of a cluster's peak
    amplitudes against a set of other spikes from the same tetrode."""
    X = np.asarray(features, float)
    N = np.asarray(noise, float)
    mu = X.mean(axis=0)
    cov = np.cov(X, rowvar=False)
    inv = np.linalg.pinv(cov)
    dN = np.einsum("ij,jk,ik->i", N - mu, inv, N - mu)
    df = X.shape[1]
    lratio = np.sum(stats.chi2.sf(dN, df)) / len(X)
    isod = float(np.sort(dN)[len(X) - 1]) if len(N) >= len(X) else np.nan
    return float(lratio), isod


def match_dataset_fields(animals, fields, pass_rule="P-a"):
    """For each of the data set's novel fields (F-b), whether a recomputed field (F-a) of the same
    cell and epoch overlaps it, and if not the step of the detection that rejects the stretch
    above 2 Hz in the same place (`rate` when the recomputed map has none). Diagnostic only."""
    fb = dataset_field_table(animals)
    rows = []
    cache = {}
    for _, r in fb.iterrows():
        g = fields[(fields.ai == r.ai) & (fields.cell == r.cell) & (fields.epoch == r.epoch)]
        ov = g[(g.start_cm < r.end_cm) & (g.end_cm > r.start_cm)]
        if len(ov):
            rows.append(dict(ai=r.ai, cell=r.cell, epoch=r.epoch, loc_m=r.loc_m, matched=True,
                             step="matched", shift_cm=100 * float(np.min(np.abs(ov.loc_m - r.loc_m)))))
            continue
        key = (r.ai, r.cell, r.epoch)
        if key not in cache:
            cache[key] = candidate_fields(animals[r.ai], r.cell, r.epoch, pass_rule)
        signs = {1: [-1], 2: [1], 3: [1, -1]}[r.direction]  # data set: 1 inbound, 2 outbound
        cand = [c for c in cache[key] if c["sign"] in signs and c["start_cm"] < r.end_cm
                and c["end_cm"] > r.start_cm]
        steps = {c["rejected"] for c in cand}
        step = "rate" if not cand else ("passes" if "passes" in steps else
                                         "width" if "width" in steps else "merged or other")
        rows.append(dict(ai=r.ai, cell=r.cell, epoch=r.epoch, loc_m=r.loc_m, matched=False, step=step,
                         shift_cm=np.nan))
    return pd.DataFrame(rows)


def track_fields_binned(animals, pass_rule, bin_cm):
    """track_fields with rate-map bins of bin_cm (variant: the data set's own maps use 1 inch,
    2.54 cm, where the Methods give 1 cm)."""
    global BIN_CM
    old = BIN_CM
    BIN_CM = bin_cm
    try:
        return track_fields(animals, pass_rule)
    finally:
        BIN_CM = old
