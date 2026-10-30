"""Loading and measures for dandiset 000462 (Krishnan, Heer, Cherian & Sheffield 2022, Nat Commun 13, 6662).

The dandiset holds one NWB file per mouse. Each file has two arrays at 30 Hz:
`acquisition/Behaviordata` (frames x 3: track position in volts, reward solenoid in volts,
lick sensor in volts) and `acquisition/Cellxrawfluoresence` (frames x cells, raw suite2p
fluorescence). The conditions are stored back to back; their order and frame counts are only
given as text in the description of the fluorescence series, which `segments` parses.

Where each parameter comes from:
- 30 Hz, 40 bins of 5 cm on a 2 m track, running frames at speed >= 1 cm/s, the lick stop rule,
  the approach ratio (100 to 150 cm over 175 to 200 cm), the engagement threshold, the place field
  criteria and parameters, the decoder (Gaussian naive Bayes, first 60% of R laps): the claims
  file's opening comment and criteria, which cite the paper's Methods ("Licking behavior",
  "Position decoding", "Engagement with VR, approach behavior", "Defining place fields",
  "Place field parameters").
- Volts to cm: the files give no unit for position. The reward is delivered at the top of the
  voltage range and the paper puts the reward at the track end (Methods, "Behavior and virtual
  reality"), so 0 V is 0 cm and the 99.9th percentile of the R position is 200 cm. Assumption,
  stated in the notebook.
- dF/F baseline: the paper says only "baseline corrected dF/F ... as previously described
  (refs. 44, 67, 75)" (Methods, "Image processing and ROI selection"). Ref. 75 (Dombeck et al.
  2010) takes the 8th percentile in a sliding window of about 15 s; that is used here
  (`BASELINE_WINDOW`, `BASELINE_PCT`). Assumption.
- Significant transients: same passage; the rule of ref. 75 (start above 2 SD, end below 0.5 SD
  of the noise) with a minimum duration of 0.5 s is used, the noise SD taken robustly from the
  median absolute deviation (`transient_mask`). Assumption.
- Place field threshold: the paper lists the criteria but not how candidate regions are cut; ref.
  75 takes contiguous bins above 25% of the way from the baseline (mean of the lowest quarter of
  bins) to the peak. Assumption (`FIELD_FRACTION`).
- Bootstrap: ref. 75 shuffles the dF/F; here the running-frame trace is circularly shifted by a
  random offset, `N_SHUFFLE` = 100 times, and a cell passes when fewer than 5% of shuffles give a
  field passing criteria 1 to 4. The number of shuffles is a standard choice.
- Lick threshold (1 V) and reward threshold (4 V): standard choices on two-level TTL-like
  signals; the values are bimodal (checked in the notebook).
- Reward zone: the mean position of the first lick of each R lap, ignoring licks before 20 cm,
  which follow the teleport (Methods, Licking behavior; the 20 cm is an assumption).
- Approach ratio: over the whole lap, teleport to teleport (main reading), or over the traversal
  only (variant); the Methods say "lap velocity". Assumption, see the notebook.
- Transients outside a field are removed as whole transients that do not touch the field's bins
  (Methods, Place field parameters).
- DREADD offset: the DREADD files carry a constant offset of about 17000 counts, removed as the
  file minimum (`OFFSET_RULE`). Assumption.
- Missing behaviour rows of sub-014 are inserted where the notebook finds them (`BEHAVIOUR_GAPS`).
- Random generators: one per mouse (`SEEDS`), for the bootstrap; standard choice.
"""
import re

import h5py
import numpy as np
import remfile
import requests
from scipy import sparse

DANDISET = "000462"
VERSION = "0.230416.2132"
API = "https://api.dandiarchive.org/api"
FS = 30.0  # Hz, ImagingPlane imaging_rate and the series' rate
TRACK = 200.0  # cm
NBINS = 40
BIN = TRACK / NBINS
RUN_SPEED = 1.0  # cm/s, Methods
LICK_V = 1.0
REWARD_V = 4.0
BASELINE_WINDOW = 450  # frames, ~15 s (ref. 75), assumption
BASELINE_STEP = 75
BASELINE_PCT = 8
FIELD_FRACTION = 0.25
N_SHUFFLE = 100
OFFSET_RULE = 5000  # counts; files whose minimum exceeds it carry an offset (assumption)

WT_FULL = ["NR6", "NR14", "NR21", "NR23", "CFC4"]  # R, UR, RR, Novel
WT_RUR = ["NR32", "NR34", "CFC16", "CFC17", "CFC19"]  # R, UR
DREADD = ["009", "011", "012", "014"]

# Frames kept per condition in the paper's code (AnimalDetails/AnimalDetailsWT.py,
# task_framestokeep, seethakris/HPCrewardpaper at 5b3b22a). Positive: keep the first n frames;
# negative: drop the last n. Used only as a code variant for lap counts.
CODE_FRAMES_TO_KEEP = {
    "NR6": [11100, -2602, -2, -4], "NR14": [-1, -118, -6, -8], "NR21": [-8, -109, -170, -112],
    "NR23": [-3, -1, -7, -6], "NR32": [-10, -200], "NR34": [-145, -178],
    "CFC4": [-7, -270, -3, -6], "CFC16": [-31, -170], "CFC17": [-94, -14], "CFC19": [-10, -2],
}


def assets():
    r = requests.get(f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/",
                     params={"page_size": 200}).json()
    return {a["path"].split("/")[0].replace("sub-", ""): a for a in r["results"]}


def open_file(asset_id):
    url = requests.head(f"{API}/assets/{asset_id}/download/", allow_redirects=True).url
    return h5py.File(remfile.File(url), "r")


def segments(description):
    """Condition names and frame counts from the fluorescence series description."""
    pairs = re.findall(r"([A-Za-z]+)\s*:\s*(\d+)", description.split("session:")[-1])
    names = [p[0] for p in pairs]
    counts = [int(p[1]) for p in pairs]
    edges = np.cumsum([0] + counts)
    return [(n, int(a), int(b)) for n, a, b in zip(names, edges[:-1], edges[1:])]


# Behaviour frames missing from a file, found in the notebook by decoding position with the
# behaviour shifted against the fluorescence: (behaviour index where the gap is, frames missing).
# sub-014 has 129000 behaviour frames for 135000 fluorescence frames; from fluorescence frame
# 77000 on, the fluorescence matches the behaviour 6000 frames earlier, and up to frame 71000 it
# matches with no shift, so 6000 behaviour frames are missing at the start of BeforeCNO.
BEHAVIOUR_GAPS = {"014": (71000, 6000)}


def load(subject, fluorescence=True, fix_gaps=True):
    a = assets()[subject]
    f = open_file(a["asset_id"])
    beh = f["acquisition/Behaviordata/data"][:]
    valid = np.ones(len(beh), bool)
    if subject in BEHAVIOUR_GAPS and fix_gaps:
        at, n = BEHAVIOUR_GAPS[subject]
        beh = np.concatenate([beh[:at], np.zeros((n, 3)), beh[at:]])
        valid = np.r_[valid[:at], np.zeros(n, bool), valid[at:]]
    fl = f["acquisition/Cellxrawfluoresence"]
    out = {
        "subject": subject,
        "path": a["path"],
        "behaviour": beh,
        "behaviour_valid": valid,
        "behaviour_rows_in_file": int(valid.sum()),
        "segments": segments(fl.attrs["description"]),
        "f_shape": fl["data"].shape,
        "subject_description": f["general/subject/description"][()].decode(),
    }
    if fluorescence:
        F = fl["data"][:].astype(np.float32)
        out["F_min"], out["F_median"] = float(F.min()), float(np.median(F[::50]))
        # The DREADD files carry a constant offset of about 17000 counts (minimum near 17000,
        # transients a few thousand above it); the WT files do not (minimum near 0). Without
        # removing it dF/F is ~10x too small. Assumption: the offset is the file's minimum.
        out["offset"] = out["F_min"] if out["F_min"] > OFFSET_RULE else 0.0
        F -= out["offset"]
        F[F < 1] = 1
        out["F"] = F
    f.close()
    return out


# ---------------------------------------------------------------- behaviour

def position_cm(volts, scale):
    return np.clip(volts / scale * TRACK, 0, TRACK)


def find_laps(pos):
    """Laps as (start, end) frame pairs, split at teleports (drops of more than half the track).

    A teleport may take two frames at 30 Hz (the behaviour was downsampled); consecutive drop
    frames are merged. Returns all segments; `complete` flags those that start in the first
    10 cm and reach the last 5 cm.
    """
    d = np.diff(pos)
    drops = np.where(d < -TRACK / 4)[0]
    if len(drops):
        drops = drops[np.r_[True, np.diff(drops) > 2]]
        # the lap ends after the last frame of the drop
        ends = []
        for t in drops:
            e = t + 1
            while e < len(pos) - 1 and pos[e] - pos[e + 1] > 1.0 and pos[e] > 10:
                e += 1
            ends.append(e)
        ends = np.array(ends)
    else:
        ends = np.array([], int)
    starts = np.r_[0, ends]
    stops = np.r_[ends, len(pos)]
    laps = []
    for s, e in zip(starts, stops):
        if e - s < 10:
            continue
        p = pos[s:e]
        laps.append((int(s), int(e), bool(p[:5].min() < 10 and p.max() > TRACK - 5)))
    return laps


def speed_cm_s(pos, laps):
    """Instantaneous speed from position, within laps (teleports excluded), 5-frame smoothing."""
    v = np.zeros(len(pos))
    for s, e, _ in laps:
        p = pos[s:e]
        g = np.gradient(p) * FS if len(p) > 1 else np.zeros(len(p))
        k = np.ones(5) / 5
        v[s:e] = np.convolve(g, k, mode="same")
    return v


def onsets(x, thr):
    return np.where(np.diff((x > thr).astype(np.int8)) == 1)[0] + 1


def condition(sess, name, scale=None):
    """Behaviour of one condition: laps, position, speed, lick and reward onsets (frame indices
    relative to the condition start)."""
    seg = {n: (a, b) for n, a, b in sess["segments"]}[name]
    a, b = seg
    beh = sess["behaviour"][a:b]
    if scale is None:
        scale = sess["scale"]
    pos = position_cm(beh[:, 0], scale)
    laps = find_laps(pos)
    if "behaviour_valid" in sess:
        ok = sess["behaviour_valid"][a:b]
        laps = [(s, e, c and bool(ok[s:e].all())) for s, e, c in laps]
    v = speed_cm_s(pos, laps)
    return {
        "name": name, "start": a, "stop": b, "pos": pos, "speed": v, "laps": laps,
        "licks": onsets(beh[:, 2], LICK_V), "rewards": onsets(beh[:, 1], REWARD_V),
        "n_frames": len(beh),
    }


def complete_laps(c):
    return [(s, e) for s, e, ok in c["laps"] if ok]


def lap_time(c, s, e):
    """Seconds from leaving 0 cm (last frame below 1 cm) to first reaching 200 cm (>= 199 cm)."""
    p = c["pos"][s:e]
    top = np.where(p >= TRACK - 1)[0]
    if not len(top):
        return np.nan
    low = np.where(p[: top[0]] < 1)[0]
    t0 = low[-1] if len(low) else 0
    return (top[0] - t0) / FS


def reward_zone_start(c_r, min_pos=20.0):
    """Start of the reward zone (Methods, Licking behavior): the mean over R laps of the position
    of the first lick in the lap, ignoring licks before `min_pos` cm, which follow the teleport and
    belong to the previous reward (assumption)."""
    firsts = []
    for s, e in complete_laps(c_r):
        lk = c_r["licks"][(c_r["licks"] >= s) & (c_r["licks"] < e)]
        lk = lk[c_r["pos"][lk] >= min_pos]
        if len(lk):
            firsts.append(c_r["pos"][lk[0]])
    return float(np.mean(firsts)), firsts


def reward_zone_start_code(c_r):
    """Code variant: first 5 cm bin where the summed R licks exceed the number of R laps."""
    laps = complete_laps(c_r)
    lk = np.concatenate([c_r["licks"][(c_r["licks"] >= s) & (c_r["licks"] < e)] for s, e in laps])
    h = np.bincount(np.minimum((c_r["pos"][lk] / BIN).astype(int), NBINS - 1), minlength=NBINS)
    over = np.where(h > len(laps))[0]
    return float(over[0] * BIN) if len(over) else np.nan


def licks_in_zone(c, zone, whole_lap=False):
    """Per complete lap, number of lick onsets in the zone (zone start to the teleport)."""
    out = []
    for s, e in complete_laps(c):
        lk = c["licks"][(c["licks"] >= s) & (c["licks"] < e)]
        if not whole_lap:
            lk = lk[c["pos"][lk] >= zone]
        out.append(len(lk))
    return np.array(out)


def lick_stop(has_lick, n_consec=2, reading="L1"):
    """Index of the first RE low lap. The run of `n_consec` laps without licks starting at i:
    L1 -> i, L2 -> i + n_consec - 1 (the Nth lap), L3 -> i + n_consec (the lap after)."""
    nl = ~np.asarray(has_lick, bool)
    for i in range(len(nl) - n_consec + 1):
        if nl[i:i + n_consec].all():
            return {"L1": i, "L2": i + n_consec - 1, "L3": i + n_consec}[reading]
    return len(nl)


def binned_lap_velocity(c, s, e, traversal=False):
    """Mean instantaneous speed per 5 cm bin over the lap's frames, teleport to teleport (main
    reading), or over its traversal only, from its start to the first frame at the track end
    (>= 199 cm), which leaves out the pause at the end (variant). The paper does not say which;
    see the notebook (approach-ratio, engaged-lap-counts)."""
    p = c["pos"][s:e]
    v = c["speed"][s:e]
    if traversal:
        top = np.where(p >= TRACK - 1)[0]
        stop = top[0] if len(top) else len(p)
        p, v = p[:stop], v[:stop]
    idx = np.minimum((p / BIN).astype(int), NBINS - 1)
    tot = np.bincount(idx, v, NBINS)
    n = np.bincount(idx, minlength=NBINS)
    with np.errstate(invalid="ignore"):
        return tot / n


def approach_ratio(c, s, e, traversal=False):
    vb = binned_lap_velocity(c, s, e, traversal)
    mid = np.nanmean(vb[20:30])  # 100 to 150 cm
    end = np.nanmean(vb[35:40])  # 175 to 200 cm
    return mid / end if end > 0 else np.nan


def approach_ratio_code(c, s, e, traversal=False):
    """Code variant (define_attentivelaps.py): velocity normalised to its peak, 2 bins trimmed at
    each end, mean of the first 10 over the last 10 bins from bin 20 on."""
    vb = binned_lap_velocity(c, s, e, traversal)
    vb = vb / np.nanmax(vb)
    vb = vb[2:-2]
    x = vb[20 - 2:]
    return np.nanmean(x[:10]) / np.nanmean(x[-10:])


# ---------------------------------------------------------------- fluorescence

def dff(F):
    """Baseline-corrected dF/F: 8th percentile in a sliding ~15 s window (ref. 75), evaluated
    every BASELINE_STEP frames and interpolated."""
    T = F.shape[0]
    centers = np.arange(0, T, BASELINE_STEP)
    base = np.empty((len(centers), F.shape[1]), np.float32)
    h = BASELINE_WINDOW // 2
    for i, c in enumerate(centers):
        base[i] = np.percentile(F[max(0, c - h):min(T, c + h)], BASELINE_PCT, axis=0)
    full = np.empty_like(F)
    t = np.arange(T)
    for j in range(F.shape[1]):
        full[:, j] = np.interp(t, centers, base[:, j])
    return (F - full) / full


def transient_mask(D, min_frames=15, hi=2.0, lo=0.5):
    """Significant transients (ref. 75 rule): start above hi*sigma, end below lo*sigma, at least
    `min_frames` long. sigma is 1.4826 * MAD of each cell's dF/F (assumption)."""
    med = np.median(D, axis=0)
    sig = 1.4826 * np.median(np.abs(D - med), axis=0)
    above_lo = D > (med + lo * sig)
    above_hi = D > (med + hi * sig)
    mask = np.zeros(D.shape, bool)
    for j in range(D.shape[1]):
        lo_j = above_lo[:, j]
        d = np.diff(np.r_[0, lo_j.astype(np.int8), 0])
        st = np.where(d == 1)[0]
        en = np.where(d == -1)[0]
        hi_c = np.r_[0, np.cumsum(above_hi[:, j])]
        for s, e in zip(st, en):
            if e - s >= min_frames and hi_c[e] - hi_c[s] > 0:
                mask[s:e, j] = True
    return mask, sig


# ---------------------------------------------------------------- place fields

def lap_bin_matrix(pos, frames_by_lap, T):
    """Sparse (L*40 x T) averaging matrix: row l*40+b averages the given frames of lap l in bin b."""
    rows, cols, vals = [], [], []
    for l, fr in enumerate(frames_by_lap):
        b = np.minimum((pos[fr] / BIN).astype(int), NBINS - 1)
        n = np.bincount(b, minlength=NBINS)
        rows.append(l * NBINS + b)
        cols.append(fr)
        vals.append(1.0 / n[b])
    rows = np.concatenate(rows)
    cols = np.concatenate(cols)
    vals = np.concatenate(vals)
    return sparse.csr_matrix((vals, (rows, cols)), shape=(len(frames_by_lap) * NBINS, T))


def running_frames(c, lap_idx):
    """Frames (relative to condition) of the given complete laps with speed >= 1 cm/s."""
    laps = complete_laps(c)
    out = []
    for i in lap_idx:
        s, e = laps[i]
        fr = np.arange(s, e)
        fr = fr[c["speed"][fr] >= RUN_SPEED]
        out.append(fr)
    return out


def lap_maps(D, M, n_laps):
    """(cells x laps x 40) mean dF/F per lap and bin; empty bins are NaN-free zeros."""
    X = M @ D  # (L*40 x N)
    return np.asarray(X).reshape(n_laps, NBINS, -1).transpose(2, 0, 1)


def _regions(above):
    d = np.diff(np.r_[0, above.astype(np.int8), 0])
    return list(zip(np.where(d == 1)[0], np.where(d == -1)[0]))


def candidate_fields(mean_map):
    """Contiguous bins above baseline + 25% of (peak - baseline); baseline = mean of the lowest
    10 of 40 bins (ref. 75, scaled from 20 of 80)."""
    base = np.mean(np.sort(mean_map)[:NBINS // 4])
    thr = base + FIELD_FRACTION * (mean_map.max() - base)
    return _regions(mean_map > thr), base


def field_passes(mean_map, lap_tr, s, e, base):
    """Criteria 1 to 4 (Methods, Defining place fields) for the field covering bins s..e-1.
    lap_tr: (laps x 40) bool, a significant transient in the bin on that lap."""
    width_ok = (e - s) * BIN > 10 or e == NBINS
    inside = mean_map[s:e].mean()
    out_bins = np.r_[mean_map[:s], mean_map[e:]]
    outside = out_bins.mean() if len(out_bins) else 0.0
    amp_ok = inside - base > 0.10
    ratio_ok = inside > 4 * outside if outside > 0 else inside > 0
    laps_ok = lap_tr[:, s:e].any(axis=1).mean() > 0.30
    return bool(width_ok and amp_ok and ratio_ok and laps_ok)


def shuffle_pass_fraction(Drun, Trun, M, n_laps, rng, n_shuffle=N_SHUFFLE):
    """Fraction of circular shifts of the running-frame traces for which the cell's peak field
    passes criteria 1 to 4. Drun, Trun: (frames x cells) dF/F and transient mask on running frames
    in lap order; M: lap-bin matrix over those frames."""
    T, N = Drun.shape
    passes = np.zeros(N)
    for _ in range(n_shuffle):
        k = rng.integers(T // 10, T - T // 10)
        Ds = np.roll(Drun, k, axis=0)
        Ts = np.roll(Trun, k, axis=0).astype(np.float32)
        maps = lap_maps(Ds, M, n_laps)
        trs = lap_maps(Ts, M, n_laps) > 0
        mm = maps.mean(axis=1)
        for j in range(N):
            m = mm[j]
            regs, base = candidate_fields(m)
            pk = int(np.argmax(m))
            for s, e in regs:
                if s <= pk < e:
                    if field_passes(m, trs[j], s, e, base):
                        passes[j] += 1
                    break
    return passes / n_shuffle


def place_fields(D, TR, c, lap_idx, rng, bootstrap=True):
    """Place fields of one condition over the given complete laps (running frames only).

    Returns (fields, maps): fields is a list of dicts (cell, start bin, end bin, parameters),
    maps the (cells x laps x 40) lap maps of dF/F with transients only (TR applied)."""
    frames = running_frames(c, lap_idx)
    allfr = np.concatenate(frames)
    n_laps = len(frames)
    # dF/F filtered for significant transients (Methods)
    Dt = np.where(TR, D, 0).astype(np.float32)
    Drun = Dt[allfr]
    Trun = TR[allfr]
    # lap-bin matrix over the concatenated running frames
    offs = np.cumsum([0] + [len(f) for f in frames])
    local = [np.arange(offs[i], offs[i + 1]) for i in range(n_laps)]
    posrun = c["pos"][allfr]
    M = lap_bin_matrix(posrun, local, len(allfr))
    maps = lap_maps(Drun, M, n_laps)
    trs = lap_maps(Trun.astype(np.float32), M, n_laps) > 0
    mm = maps.mean(axis=1)
    cand = []
    for j in range(D.shape[1]):
        regs, base = candidate_fields(mm[j])
        for s, e in regs:
            if field_passes(mm[j], trs[j], s, e, base):
                cand.append((j, s, e))
    cells = sorted({j for j, _, _ in cand})
    if bootstrap and cells:
        pf = shuffle_pass_fraction(Drun[:, cells], Trun[:, cells], M, n_laps, rng)
        pmap = dict(zip(cells, pf))
    else:
        pmap = {j: 0.0 for j in cells}
    binrun = bin_of(posrun)
    fields = []
    for j, s, e in cand:
        if pmap[j] >= 0.05:
            continue
        fmap = field_only_map(Drun[:, j], Trun[:, j], binrun, s, e, M, n_laps)
        fields.append(dict(cell=j, start=s, end=e, **field_parameters(maps[j], trs[j], s, e, fmap)))
    return fields, maps, trs


def field_only_map(d, t, bins, s, e, M, n_laps):
    """(laps x 40) map of one cell with the transients outside the field removed (Methods, Place
    field parameters): a transient (a run of significant frames) is kept when any of its frames
    falls in the field's bins s..e-1."""
    dd = np.diff(np.r_[0, t.astype(np.int8), 0])
    keep = np.zeros(len(d), bool)
    for a, b in zip(np.where(dd == 1)[0], np.where(dd == -1)[0]):
        if ((bins[a:b] >= s) & (bins[a:b] < e)).any():
            keep[a:b] = True
    return np.asarray(M @ np.where(keep, d, 0)).reshape(n_laps, NBINS)


def field_parameters(lmap, ltr, s, e, fmap=None):
    """Place field parameters (Methods). lmap: (laps x 40) transient-only dF/F of the cell, used for
    the out/in ratio; fmap: the same with the transients outside the field removed, used for the
    other parameters. Without fmap (fields measured on laps other than those that defined them),
    the contiguous active bins around the field stand in for it."""
    L = lmap.shape[0]
    mean_all = lmap.mean(axis=0)
    out_bins = np.r_[mean_all[:s], mean_all[e:]]
    in_mean = mean_all[s:e].mean()
    out_in = (out_bins.mean() / in_mean) if len(out_bins) and in_mean > 0 else np.nan
    # transients outside the field removed: keep the contiguous active stretch around the field
    f = lmap.copy() if fmap is None else fmap.copy()
    keep = np.zeros(NBINS, bool)
    m = mean_all if fmap is None else fmap.mean(axis=0)
    a, b = s, e
    while a > 0 and m[a - 1] > 0:
        a -= 1
    while b < NBINS and m[b] > 0:
        b += 1
    keep[a:b] = True
    f[:, ~keep] = 0
    mf = f.mean(axis=0)
    width = (b - a) * BIN
    intensity = float(mf.max())
    x = (np.arange(NBINS) + 0.5) * BIN
    com = float((mf * x).sum() / mf.sum()) if mf.sum() > 0 else np.nan
    # reliability: mean lap-by-lap correlation x fraction of laps with a transient in the field
    with np.errstate(invalid="ignore", divide="ignore"):
        C = np.corrcoef(f)
    iu = np.triu_indices(L, 1)
    r = np.nanmean(C[iu]) if L > 1 and np.isfinite(C[iu]).any() else np.nan
    frac = ltr[:, s:e].any(axis=1).mean()
    return dict(reliability=float(r * frac) if np.isfinite(r) else 0.0, out_in=float(out_in),
                width=float(width), intensity=intensity, com=com, frac_laps=float(frac))


# ---------------------------------------------------------------- decoder

def bin_of(pos):
    return np.minimum((pos / BIN).astype(int), NBINS - 1)


def r2(y, yhat):
    y = np.asarray(y, float)
    yhat = np.asarray(yhat, float)
    ss = ((y - y.mean()) ** 2).sum()
    return 1 - ((y - yhat) ** 2).sum() / ss if ss > 0 else np.nan


def unwrap(y, yhat):
    """Code variant: circular unwrapping of the prediction before R2."""
    d = yhat - y
    yhat = yhat.copy()
    yhat[d > NBINS / 2] -= NBINS
    yhat[d < -NBINS / 2] += NBINS
    return yhat


def circ_err_cm(y, yhat):
    d = np.abs(yhat - y)
    return np.minimum(d, NBINS - d) * BIN


# ---------------------------------------------------------------- per-mouse processing

LICK_READINGS = ["L1", "L2", "L3"]


def behaviour_summary(sess):
    """Laps, licks, lick stops, approach ratios and engagement for one mouse."""
    a, b = sess["segments"][0][1:]
    sess["scale"] = float(np.percentile(sess["behaviour"][a:b, 0], 99.9))
    conds = {n: condition(sess, n) for n, _, _ in sess["segments"]}
    first = sess["segments"][0][0]
    cR = conds[first]
    zone, firsts = reward_zone_start(cR)
    out = {"conds": conds, "zone": zone, "zone_code": reward_zone_start_code(cR),
           "first_lick_positions": firsts}
    ratios = {n: np.array([approach_ratio(c, s, e) for s, e in complete_laps(c)])
              for n, c in conds.items()}
    ratios_code = {n: np.array([approach_ratio_code(c, s, e) for s, e in complete_laps(c)])
                   for n, c in conds.items()}
    out["ratios"], out["ratios_code"] = ratios, ratios_code
    out["ratios_trav"] = {n: np.array([approach_ratio(c, s, e, True) for s, e in complete_laps(c)])
                          for n, c in conds.items()}
    out["ratios_code_trav"] = {n: np.array([approach_ratio_code(c, s, e, True) for s, e in complete_laps(c)])
                               for n, c in conds.items()}
    rt = out["ratios_trav"][first]
    out["engage_thr_trav"] = float(np.nanmean(rt) - 1.5 * np.nanstd(rt, ddof=1))
    rr = ratios[first]
    out["engage_thr"] = float(np.nanmean(rr) - 1.5 * np.nanstd(rr, ddof=1))
    out["lap_times"] = {n: np.array([lap_time(c, s, e) for s, e in complete_laps(c)])
                        for n, c in conds.items()}
    if "Unrewarded" in conds:
        cU = conds["Unrewarded"]
        nz = licks_in_zone(cU, zone)
        out["ur_zone_licks"] = nz
        out["ur_any_licks"] = licks_in_zone(cU, zone, whole_lap=True)
        out["ur_zone_licks_code"] = licks_in_zone(cU, out["zone_code"]) if np.isfinite(
            out["zone_code"]) else nz
        out["lick_stop"] = {L: lick_stop(nz > 0, 2, L) for L in LICK_READINGS}
        out["engaged_ur"] = ratios["Unrewarded"] >= out["engage_thr"]
        out["engaged_ur_trav"] = out["ratios_trav"]["Unrewarded"] >= out["engage_thr_trav"]
    return out


def decode(Dc, conds, first="Rewarded", train_frac=0.6, mode="methods"):
    """Gaussian naive Bayes position decoder (Methods, Position decoding): dF/F of all cells,
    running frames, 40 bins of 5 cm.

    mode "methods": trained on the first 60% of R laps, the track treated as a circle (the
    prediction is unwrapped to the nearest copy of the true bin before R2 and error);
    mode "code": the code's variant (RunControlmodelonothertasks.py), trained on the first 50% of
    R running frames, unwrapped, laps with 100 frames or fewer dropped;
    mode "linear": as "methods" without the circular treatment (shown for comparison only).
    Returns per condition a list of per-lap dicts (lap index, R2, true bins, error in cm)."""
    from sklearn.naive_bayes import GaussianNB
    cR = conds[first]
    lapsR = complete_laps(cR)
    frs = running_frames(cR, range(len(lapsR)))
    if mode == "code":
        allr = np.concatenate(frs)
        tr = allr[: len(allr) // 2]
        test_from = None
    else:
        ntr = int(np.floor(train_frac * len(lapsR)))
        tr = np.concatenate(frs[:ntr])
        test_from = ntr
    model = GaussianNB().fit(Dc[first][tr], bin_of(cR["pos"][tr]))
    res = {}
    for n, c in conds.items():
        laps = complete_laps(c)
        out = []
        for i, f in enumerate(running_frames(c, range(len(laps)))):
            if n == first:
                if mode == "code" and np.isin(f, tr).any():
                    continue
                if mode != "code" and i < test_from:
                    continue
            if mode == "code" and len(f) <= 100:
                continue
            if len(f) < 2:
                continue
            y = bin_of(c["pos"][f])
            yh = model.predict(Dc[n][f]).astype(float)
            if mode != "linear":
                yh = unwrap(y, yh)
            out.append({"lap": i, "r2": r2(y, yh), "bins": y, "err_cm": np.abs(yh - y) * BIN,
                        "n_frames": len(f)})
        res[n] = out
    if mode == "methods":
        # training laps, predicted by the model they trained (for the pooled R laps of Supp. Fig. 4f)
        tr_out = []
        for i, f in enumerate(frs[:test_from]):
            y = bin_of(cR["pos"][f])
            yh = unwrap(y, model.predict(Dc[first][f]).astype(float))
            tr_out.append({"lap": i, "r2": r2(y, yh)})
        res[first + "_train"] = tr_out
    return res


def lap_maps_all(D, TR, c):
    """(cells x laps x 40) mean transient-filtered dF/F per complete lap (running frames)."""
    laps = complete_laps(c)
    frames = running_frames(c, range(len(laps)))
    allfr = np.concatenate(frames)
    offs = np.cumsum([0] + [len(f) for f in frames])
    local = [np.arange(offs[i], offs[i + 1]) for i in range(len(frames))]
    M = lap_bin_matrix(c["pos"][allfr], local, len(allfr))
    Dt = np.where(TR, D, 0).astype(np.float32)[allfr]
    return lap_maps(Dt, M, len(frames))


def process_mouse(sub, seed, decoder=True, field_sets=None):
    """Load one mouse, compute behaviour, dF/F, transients, decoder and place fields.

    field_sets: function(beh) -> dict name -> (condition, lap indices) of the lap sets in which
    place fields are defined. Returns a dict without the raw arrays."""
    rng = np.random.default_rng(seed)
    sess = load(sub)
    beh = behaviour_summary(sess)
    conds = beh["conds"]
    F = sess.pop("F")
    import hashlib
    fingerprints = {"behaviour_md5": hashlib.md5(sess["behaviour"][sess["behaviour_valid"]].tobytes()).hexdigest()[:12],
                    "fluorescence_md5": hashlib.md5(F[:3000].tobytes()).hexdigest()[:12]}
    beh_raw = sess["behaviour"][sess["behaviour_valid"]]
    volts = {"position_V": (float(beh_raw[:, 0].min()), float(beh_raw[:, 0].max())),
             "reward_V": (float(beh_raw[:, 1].min()), float(beh_raw[:, 1].max())),
             "lick_V": (float(beh_raw[:, 2].min()), float(beh_raw[:, 2].max())),
             "reward_frac_between_0.5_and_4V": float(((beh_raw[:, 1] > 0.5) & (beh_raw[:, 1] < REWARD_V)).mean()),
             "lick_frac_between_0.5_and_4V": float(((beh_raw[:, 2] > 0.5) & (beh_raw[:, 2] < 4)).mean())}
    D, TR, sig = {}, {}, {}
    for n, c in conds.items():
        Fc = F[c["start"]:c["stop"]]
        D[n] = dff(Fc)
        TR[n], sig[n] = transient_mask(D[n])
    del F
    out = {"subject": sub, "segments": sess["segments"], "offset": sess["offset"],
           "F_min": sess["F_min"], "F_median": sess["F_median"], "fingerprints": fingerprints,
           "volts": volts, "scale": sess["scale"], "subject_description": sess["subject_description"],
           "behaviour_rows_in_file": sess["behaviour_rows_in_file"], "behaviour_shape": sess["behaviour"].shape,
           "f_shape": sess["f_shape"], "beh": beh, "n_cells": D[sess["segments"][0][0]].shape[1],
           "dff_pct": {n: np.percentile(D[n][::10], [1, 50, 99]).tolist() for n in D},
           "transient_frac": {n: float(TR[n].mean()) for n in TR},
           "noise_sd_median": {n: float(np.median(sig[n])) for n in sig}}
    if decoder:
        out["dec"] = decode(D, conds)
        out["dec_var"] = decode(D, conds, mode="code")
        out["dec_lin"] = decode(D, conds, mode="linear")
        # clock check: decoder with labels shifted by 10 s
        out["dec_shift"] = decode_shifted(D, conds)
        if "Novel" in conds:
            nmin = min(len(complete_laps(conds[n])) for n in ["Rewarded", "ReRewarded", "Novel"])
            out["dec_cv"] = {n: decode_cv(D[n], conds[n], nmin) for n in ["Rewarded", "ReRewarded", "Novel"]}
            nN = len(complete_laps(conds["Novel"]))
            out["dec_cv_novel_all"] = decode_cv(D["Novel"], conds["Novel"], nN)
    out["maps"] = {n: lap_maps_all(D[n], TR[n], c) for n, c in conds.items()}
    out["fields"] = {}
    if field_sets is not None:
        for name, (cn, idx) in field_sets(beh).items():
            if len(idx) < 3:
                out["fields"][name] = None
                continue
            f, _, _ = place_fields(D[cn], TR[cn], conds[cn], list(idx), rng)
            out["fields"][name] = {"fields": f, "laps": list(idx), "cond": cn}
    return out


def decode_shifted(D, conds, shift_s=10.0, first="Rewarded"):
    """Clock check: train and test on R with the position labels shifted by `shift_s` seconds
    against the fluorescence. With aligned clocks the true labels decode far better."""
    from sklearn.naive_bayes import GaussianNB
    c = conds[first]
    laps = complete_laps(c)
    frs = running_frames(c, range(len(laps)))
    ntr = int(np.floor(0.6 * len(laps)))
    out = {}
    for k in [0, int(shift_s * FS)]:
        tr = np.concatenate(frs[:ntr])
        te = np.concatenate(frs[ntr:])
        trk = tr[(tr + k) < len(c["pos"])]
        tek = te[(te + k) < len(c["pos"])]
        m = GaussianNB().fit(D[first][trk], bin_of(c["pos"][trk + k]))
        out[k] = r2(bin_of(c["pos"][tek + k]), m.predict(D[first][tek]))
    return out


def wt_sets(beh):
    """Lap sets for place fields in the WT mice: R (all laps), RE low engaged and RE low all
    laps under each lick stop reading, RR."""
    conds = beh["conds"]
    nR = len(complete_laps(conds["Rewarded"]))
    nU = len(complete_laps(conds["Unrewarded"]))
    sets = {"R": ("Rewarded", range(nR))}
    for L in LICK_READINGS:
        ls = beh["lick_stop"][L]
        eng = beh["engaged_ur"]
        sets[f"RElow_eng_{L}"] = ("Unrewarded", [i for i in range(ls, nU) if eng[i]])
        sets[f"RElow_all_{L}"] = ("Unrewarded", list(range(ls, nU)))
    if "ReRewarded" in conds:
        sets["RR"] = ("ReRewarded", range(len(complete_laps(conds["ReRewarded"]))))
    if "Novel" in conds:
        nN = len(complete_laps(conds["Novel"]))
        sets["N"] = ("Novel", range(nN))
        # Supplementary Fig. 13b: early = first 12 laps, late = last 12 laps of the novel session
        sets["N_early"] = ("Novel", range(min(12, nN)))
        sets["N_late"] = ("Novel", range(max(0, nN - 12), nN))
    return sets


def decode_cv(Dn, c, n_laps, test_frac=0.2):
    """Decoder trained and tested within one condition (Methods, Position decoding): the first
    `n_laps` complete laps (down-sampled to the condition with the fewest laps), a block of 20% of
    the laps tested and the other 80% used for training, the block slid by one lap at a time.
    Returns the mean R2 of each lap over the blocks that tested it (circular treatment as in
    `decode`)."""
    from sklearn.naive_bayes import GaussianNB
    frs = running_frames(c, range(n_laps))
    k = max(1, int(round(test_frac * n_laps)))
    scores = [[] for _ in range(n_laps)]
    for start in range(0, n_laps - k + 1):
        test = list(range(start, start + k))
        train = [i for i in range(n_laps) if i not in test]
        tr = np.concatenate([frs[i] for i in train])
        m = GaussianNB().fit(Dn[tr], bin_of(c["pos"][tr]))
        for i in test:
            f = frs[i]
            if len(f) < 2:
                continue
            y = bin_of(c["pos"][f])
            scores[i].append(r2(y, unwrap(y, m.predict(Dn[f]).astype(float))))
    return np.array([np.mean(x) if x else np.nan for x in scores])


def dreadd_sets(beh):
    """Lap sets in the DREADD mice: every condition on all laps, and RE low (engaged and all)
    under each lick stop reading on day 1."""
    sets = {}
    for n, c in beh["conds"].items():
        if n != "Unrewarded":
            sets[n] = (n, range(len(complete_laps(c))))
    nU = len(complete_laps(beh["conds"]["Unrewarded"]))
    for L in LICK_READINGS:
        ls = beh["lick_stop"][L]
        sets[f"RElow_eng_{L}"] = ("Unrewarded", [i for i in range(ls, nU) if beh["engaged_ur"][i]])
        sets[f"RElow_all_{L}"] = ("Unrewarded", list(range(ls, nU)))
    # Supplementary Fig. 18a: before saline laps above the 60th percentile of lap speed, after
    # saline laps below (reading a) or above (reading b, as printed) the 40th percentile; within
    # each mouse
    for n, key, pct, above in [("BeforeSaline", "Sal_fast", 60, True), ("AfterSaline", "Sal_slow_a", 40, False),
                               ("AfterSaline", "Sal_slow_b", 40, True)]:
        if n in beh["conds"]:
            sp = lap_speeds(beh["conds"][n])
            thr = np.nanpercentile(sp, pct)
            sets[key] = (n, [i for i, v in enumerate(sp) if (v > thr if above else v < thr)])
    return sets


def lap_speeds(c):
    """Lap speed (cm/s) = 200 cm over the lap time from 0 to 200 cm."""
    return np.array([TRACK / lap_time(c, s, e) for s, e in complete_laps(c)])


def gap_check(sub="014", train="BeforeSaline", lo=65000, hi=83000, lag=6000, win=1000):
    """Locate missing behaviour frames: decode position from the fluorescence in windows of
    `win` frames, with the behaviour as stored (lag 0) and shifted by `lag` frames. A model
    trained on an aligned condition before the windows gives the error of each alignment."""
    from sklearn.naive_bayes import GaussianNB
    sess = load(sub, fix_gaps=False)
    F = sess.pop("F")
    beh = sess["behaviour"]
    a, b = {n: (x, y) for n, x, y in sess["segments"]}[train]
    scale = float(np.percentile(beh[:sess["segments"][0][2], 0], 99.9))
    pos = position_cm(beh[:, 0], scale)
    v = np.r_[0, np.abs(np.diff(pos))] * FS
    run = (v > RUN_SPEED) & (v < 100)
    D = dff(F[a - 2000:hi + lag])
    off = a - 2000
    fr = np.arange(a, b)
    fr = fr[run[fr]]
    m = GaussianNB().fit(D[fr - off], bin_of(pos[fr]))
    rows = []
    for w in range(lo, hi, win):
        fr = np.arange(w, min(w + win, len(pos)))
        fr = fr[run[fr]]
        row = {"behaviour frames": f"{w}-{w + win}"}
        for k in [0, lag]:
            g = fr[fr + k - off < len(D)]
            row[f"error, fluorescence lag {k} (cm)"] = float(np.mean(circ_err_cm(bin_of(pos[g]), m.predict(D[g + k - off])))) if len(g) > 50 else np.nan
        rows.append(row)
    return rows


SEEDS = {s: 1000 + i for i, s in enumerate(WT_FULL + WT_RUR + DREADD)}


def process_one(sub):
    """Everything the notebook needs from one mouse, with that mouse's own random generator."""
    dr = sub in DREADD
    return process_mouse(sub, SEEDS[sub], decoder=not dr, field_sets=dreadd_sets if dr else wt_sets)


def process_all(subjects, workers=2):
    import multiprocessing
    from concurrent.futures import ProcessPoolExecutor
    ctx = multiprocessing.get_context("fork")
    with ProcessPoolExecutor(workers, mp_context=ctx) as ex:
        return dict(zip(subjects, ex.map(process_one, subjects)))
