"""Loading and measures for Vijayan et al. (2022), Sci Adv 8:eabn3852, on DANDI:000212.

Every NWB file of the dandiset holds one fly: at 2 frames per second, the xy
position of its centroid (mm), the island it is on, the sucrose concentration
under it (mM) and a 0/1 egg series. The files are streamed from the archive
(each file is read into memory in one request and opened with h5py); nothing is
written to disk.

Where each parameter comes from is given beside it:
  [claim]  the claims file's shared methods M1 to M8 (claims/vijayan-2022.yaml),
           which cite the paper;
  [paper]  a passage of the paper taken by the author (protocol, author 1.6);
  [assume] an assumption, with the reason;
  [std]    a standard choice for a detail that cannot change a result.
"""
import io
import re
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import requests
from scipy import stats

DANDISET = "000212"
# No published version of 000212 exists; the draft is used, and its
# modification time is recorded (docs/archives.md, DANDI, "Versions").
VERSION = "draft"
API = "https://api.dandiarchive.org/api"
FPS = 2.0  # [paper] "videos were recorded at 2 frames per second" (Methods, rate)
DT = 1.0 / FPS

# [claim] M4: bin edges read from the x-axis ticks of fig. S2 (s).
RATE_EDGES = np.array([0, 5, 10, 15, 20, 25, 30, 45, 60, 90, 150, 300, 600, 1200, 7200], float)


def version_info():
    r = requests.get(f"{API}/dandisets/{DANDISET}/versions/{VERSION}/info/", timeout=60).json()
    return {"version": r["version"], "modified": r["modified"], "asset_count": r["asset_count"],
            "size": r["size"]}


def list_assets():
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=1000"
    out = []
    while url:
        r = requests.get(url, timeout=60).json()
        out += r["results"]
        url = r["next"]
    return out


def group_of(path):
    """Chamber/genotype group from the subject folder name, e.g. '0-500-200-CS'."""
    sub = path.split("/")[0]
    return re.sub(r"^sub-", "", re.sub(r"-fly#-\d+$", "", sub))


def _s3_url(asset_id):
    r = requests.get(f"{API}/assets/{asset_id}/", timeout=60).json()
    return [u for u in r["contentUrl"] if "s3" in u][0]


def read_fly(asset):
    """Stream one NWB file and reduce it to compact arrays."""
    url = _s3_url(asset["asset_id"])
    # The files are small (7 to 10 MB) and every series is read whole, so each
    # is fetched into memory in one request (no file is written to disk).
    buf = io.BytesIO(requests.get(url, timeout=300).content)
    with h5py.File(buf, "r") as f:
        b = f["processing/behavior"]
        pos = b["Position/SpatialSeries/data"][:].astype(np.float32)
        t = b["Position/SpatialSeries/timestamps"][:]
        isl = b["Island/data"][:]
        suc = b["Sucrose_Concentration/data"][:]
        egg = b["Egg/data"][:]
        t_e = b["Egg/timestamps"]
        same_t = (t_e.shape == t.shape) and bool(np.array_equal(t_e[:], t))
        subj = f["general/subject"]
        desc = subj["description"][()].decode() if "description" in subj else ""
        geno = subj["genotype"][()].decode() if "genotype" in subj else ""
        units = {k: b[k + "/data"].attrs.get("unit", "") for k in ("Egg", "Island", "Sucrose_Concentration")}
        units["Position"] = b["Position/SpatialSeries/data"].attrs.get("unit", "")
    dts = np.diff(t)
    egg_vals = np.unique(egg[np.isfinite(egg)])
    return {
        "path": asset["path"], "group": group_of(asset["path"]), "description": desc,
        "genotype": geno, "units": units,
        "n": len(t), "t0": float(t[0]), "dt_min": float(dts.min()), "dt_max": float(dts.max()),
        "same_t": same_t, "egg_values": egg_vals.tolist(),
        "pos": pos,
        "island": np.where(np.isfinite(isl), isl, -1).astype(np.int8),
        "sucrose": np.where(np.isfinite(suc), suc, -1).astype(np.float32),
        "eggs": np.flatnonzero(egg > 0.5),
        "egg_sum": float(np.nansum(egg)),
        "pos_nan": int(np.isnan(pos).any(axis=1).sum()),
    }


def load_all(assets, workers=16):
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(read_fly, assets))


# ---------------------------------------------------------------- measures

def speed(pos):
    """[claim] M2: frame-to-frame centroid displacement times 2 frames/s (mm/s).
    The first frame repeats the second."""
    d = np.sqrt((np.diff(pos, axis=0) ** 2).sum(axis=1)) * FPS
    return np.concatenate([d[:1], d]).astype(np.float32)


def boxcar(x, seconds):
    """Centred moving average over round(seconds*FPS) frames (MATLAB smooth-like;
    [std] the edges average over the frames available)."""
    n = int(round(seconds * FPS))
    k = np.ones(n)
    num = np.convolve(x, k, mode="same")
    den = np.convolve(np.ones_like(x), k, mode="same")
    return num / den


SEARCH_BOX_S = 18.5   # [paper] Methods, Automated determination of egg-laying search
SEARCH_THR = 0.1      # mm/s, same passage
HALF_BOX = int(round(SEARCH_BOX_S * FPS)) // 2  # 18 frames = 9 s


def search_starts(spd, eggs, half=HALF_BOX):
    """[claim] M3. For each egg frame e, the start of its search: going back from
    the egg, the first frame j where the 18.5-s centred boxcar of speed is below
    0.1 mm/s. [assume] Only frames whose centred window ends before the egg
    (j <= e - 9 s) are considered, which is what makes "the minimum search
    duration ... 9 s because of the length of the boxcar filter" (same passage).
    The variant half=1 starts the scan at the frame before the egg. When no such
    frame exists, the search starts at the first frame of the recording."""
    sm = boxcar(spd.astype(float), SEARCH_BOX_S)
    below = np.flatnonzero(sm < SEARCH_THR)
    out = np.empty(len(eggs), int)
    for k, e in enumerate(eggs):
        lim = e - half
        i = np.searchsorted(below, lim, side="right") - 1
        out[k] = below[i] if i >= 0 else 0
    return out


def pause_times(spd, eggs):
    """[paper] Methods, Statistics: pause time is "the time difference between egg
    deposition and when the 1-s boxcar smoothed locomotor speed increases above
    0.1 mm/s before egg deposition"; read as the time from the last frame before
    the egg with smoothed speed above 0.1 mm/s to the egg (s)."""
    sm = boxcar(spd.astype(float), 1.0)
    above = np.flatnonzero(sm > SEARCH_THR)
    out = np.full(len(eggs), np.nan)
    for k, e in enumerate(eggs):
        i = np.searchsorted(above, e, side="left") - 1
        if i >= 0:
            out[k] = (e - above[i]) * DT
    return out


def search_windows(starts, eggs, n, mode="working", prev_eggs=None):
    """Search period [start, egg] per egg, in frames, for the rate functions.
    working: M3 with searches shorter than 30 s set to 30 s ([paper] Methods,
             Calculation of egg-laying rate; [claim] M3: extended back to 30 s).
    alt1:    no 30-s minimum (fig. S2 legend, alternate definition 1).
    alt2:    the 90 s before each egg, shortened so as not to reach back past
             the previous egg plus 1 min (alternate definition 2).
    alt3:    as alt2 with 15 min (alternate definition 3)."""
    eggs = np.asarray(eggs)
    if mode == "working":
        s = np.minimum(starts, eggs - int(30 * FPS))
    elif mode == "alt1":
        s = np.asarray(starts).copy()
    else:
        L = int((90 if mode == "alt2" else 900) * FPS)
        s = eggs - L
        prev = np.concatenate([[-10 ** 9], eggs[:-1]]) + int(60 * FPS)
        s = np.maximum(s, prev)
    s = np.clip(s, 0, n - 1)
    return s, eggs


def time_since_left(label, value):
    """For each frame, seconds since the last frame on which label == value
    (np.inf when never yet). Frames on the value itself get 0."""
    idx = np.arange(len(label))
    last = np.where(label == value, idx, -1)
    last = np.maximum.accumulate(last)
    t = (idx - last) * DT
    t[last < 0] = np.inf
    return t


def rate_events(flies_lab, cur, prev, edges=RATE_EDGES, mode="working", pred_key=None):
    """[claim] M4 counting for one (current substrate, indicated substrate) pair.

    flies_lab: list of dicts with 'label' (per-frame substrate label), 'eggs',
    'starts' (M3 search starts), 'n'. Returns per-bin eggs, frames, visits, and
    the trial lists for the bin test M5: for reading (a) one 0/1 entry per visit
    to the bin during a search; for reading (b) one 0/1 entry per search that
    enters the bin. Overlapping searches (when a 30-s extension reaches into the
    previous search) are counted for each egg, as each search is its own
    trial ([assume]; the paper treats searches as independent). With pred_key,
    the per-frame values f[pred_key] (a model's predicted eggs per frame) are
    summed per bin as 'pred_sum', so that a model's rate function is binned
    exactly as the data's."""
    nb = len(edges) - 1
    eggs = np.zeros(nb, int); frames = np.zeros(nb, int); visits = np.zeros(nb, int)
    va = [[] for _ in range(nb)]; sb = [[] for _ in range(nb)]
    pred_sum = np.zeros(nb)
    for f in flies_lab:
        if len(f["eggs"]) == 0:
            continue
        lab = f["label"]
        ts = time_since_left(lab, prev)
        b = np.searchsorted(edges, ts, side="right") - 1
        b[(ts >= edges[-1]) | ~np.isfinite(ts)] = -1
        on = (lab == cur) & (b >= 0)
        s0, e0 = search_windows(f["starts"], f["eggs"], f["n"], mode)
        for s, e in zip(s0, e0):
            seg_on = on[s:e + 1]
            if not seg_on.any():
                continue
            seg_b = np.where(seg_on, b[s:e + 1], -1)
            frames += np.bincount(seg_b[seg_b >= 0], minlength=nb)
            if pred_key is not None:
                pv = f[pred_key][s:e + 1]
                pred_sum += np.bincount(seg_b[seg_b >= 0], weights=pv[seg_b >= 0], minlength=nb)
            egg_bin = seg_b[-1]
            if egg_bin >= 0:
                eggs[egg_bin] += 1
            # runs of constant bin while on cur
            chg = np.flatnonzero(np.diff(np.concatenate([[-1], seg_b])) != 0)
            run_b = seg_b[chg]
            ok = run_b >= 0
            visits += np.bincount(run_b[ok], minlength=nb)
            last_run = len(chg) - 1
            entered = set()
            for r, bb in enumerate(run_b):
                if bb < 0:
                    continue
                hit = int(r == last_run and egg_bin == bb)
                va[bb].append(hit)
                entered.add(bb)
            for bb in entered:
                sb[bb].append(int(bb == egg_bin))
    with np.errstate(invalid="ignore", divide="ignore"):
        rate = eggs / frames * 120.0
    return {"edges": edges, "eggs": eggs, "frames": frames, "visits": visits, "rate": rate, "pred_sum": pred_sum,
            "trials_visit": [np.array(x) for x in va], "trials_search": [np.array(x) for x in sb]}


def rate_ci(r, alpha=0.10):
    """[paper] 90% Clopper-Pearson interval on eggs/visits, times 120*visits/frames."""
    lo = np.full(len(r["eggs"]), np.nan); hi = lo.copy()
    for i, (k, v, fr) in enumerate(zip(r["eggs"], r["visits"], r["frames"])):
        if v == 0 or fr == 0:
            continue
        ci = stats.binomtest(int(min(k, v)), int(v)).proportion_ci(1 - alpha, method="exact")
        lo[i] = ci.low * 120 * v / fr; hi[i] = ci.high * 120 * v / fr
    return lo, hi


def ranksum(a, b):
    """[paper] Methods, Statistics: two-sided Wilcoxon rank sum test. The paper used
    MATLAB, whose ranksum corrects the normal approximation for ties; scipy's
    mannwhitneyu (asymptotic, tie-corrected, with continuity correction) does
    the same. scipy.stats.ranksums has no tie correction and would overstate p
    for 0/1 trials."""
    a = np.asarray(a, float); b = np.asarray(b, float)
    a = a[np.isfinite(a)]; b = b[np.isfinite(b)]
    if len(a) == 0 or len(b) == 0:
        return np.nan
    if np.ptp(np.concatenate([a, b])) == 0:
        return 1.0
    return float(stats.mannwhitneyu(a, b, alternative="two-sided", method="asymptotic",
                                    use_continuity=True).pvalue)


def ranksum01(a, b):
    """[paper] Methods, Statistics: two-sided Wilcoxon rank sum test on 0/1 trials."""
    return ranksum(a, b)


def bin_pvals(r1, r2, reading="visit"):
    key = "trials_visit" if reading == "visit" else "trials_search"
    return np.array([ranksum01(x, y) for x, y in zip(r1[key], r2[key])])


def merge_bin(r1, r2, reading="visit", edges=RATE_EDGES):
    """[claim] M5 / Fig. 5A legend: first bin past 5 s for which P > 0.05.
    Returns (left edge in s, index) or (None, None) when no bin merges."""
    p = bin_pvals(r1, r2, reading)
    for i in range(len(edges) - 1):
        if edges[i] >= 5 and np.isfinite(p[i]) and p[i] > 0.05:
            return edges[i], i
    return None, None


def pooled_trials(r, lo, hi, reading="visit", edges=RATE_EDGES):
    """Rate and 0/1 trials pooled over the bins with lo <= left edge < hi."""
    key = "trials_visit" if reading == "visit" else "trials_search"
    sel = [i for i in range(len(edges) - 1) if edges[i] >= lo and edges[i + 1] <= hi]
    e = r["eggs"][sel].sum(); fr = r["frames"][sel].sum()
    tr = np.concatenate([r[key][i] for i in sel]) if sel else np.array([])
    return (e / fr * 120 if fr else np.nan), tr, int(e), int(fr)


def clopper(k, n, alpha=0.05):
    if n == 0:
        return (np.nan, np.nan)
    ci = stats.binomtest(int(k), int(n)).proportion_ci(1 - alpha, method="exact")
    return (ci.low, ci.high)


# ---------------------------------------------------------------- per group

def prepare(fly):
    """Add speed, M3 search starts and M7 pause times to a loaded fly; drop
    the position array once its range is noted (memory)."""
    spd = speed(fly["pos"])
    fly["speed"] = spd
    fly["starts"] = search_starts(spd, fly["eggs"])
    fly["pause"] = pause_times(spd, fly["eggs"])
    p = fly.pop("pos")
    fly["xy_min"] = np.nanmin(p, axis=0); fly["xy_max"] = np.nanmax(p, axis=0)
    fly["y_island"] = {int(i): (float(np.percentile(p[fly["island"] == i, 1], 1)),
                                float(np.percentile(p[fly["island"] == i, 1], 99)))
                       for i in np.unique(fly["island"])}
    return fly


def labelled(flies, key="sucrose"):
    """Inputs for rate_events with substrate label `key` ('sucrose' or 'island')."""
    return [dict(label=f[key], eggs=f["eggs"], starts=f["starts"], n=f["n"]) for f in flies]


def entry_label(f, cur):
    """Label array where frames on `cur` keep it and all others become -999, so
    that 'time since leaving -999' is the time since entering `cur`."""
    lab = np.where(f["sucrose"] == cur, cur, -999).astype(np.float32)
    return lab


def visits(label):
    """Runs of constant label: (start frame, end frame inclusive, value)."""
    chg = np.flatnonzero(np.diff(label) != 0)
    st = np.concatenate([[0], chg + 1]); en = np.concatenate([chg, [len(label) - 1]])
    return st, en, label[st]


def in_search_mask(f, mode="alt1"):
    """Frames inside any search period (default: M3 without the 30-s minimum)."""
    m = np.zeros(f["n"], bool)
    s0, e0 = search_windows(f["starts"], f["eggs"], f["n"], mode)
    for s, e in zip(s0, e0):
        m[s:e + 1] = True
    return m


def transits(f, mode="alt1"):
    """[claim] fig4a: island visits lying wholly inside one search period (M3,
    M1 by the island series). Returns a list of (island, duration s,
    from-island, to-island). The visit at the start or end of the recording is
    left out. [assume] A visit must start and end within the same search, and
    the visit that ends with the egg is not a transit. Returns (island, duration s,
    from-island, to-island, sucrose)."""
    st, en, val = visits(f["island"])
    s0, e0 = search_windows(f["starts"], f["eggs"], f["n"], mode)
    sid = np.full(f["n"], -1)
    for k, (s, e) in enumerate(zip(s0, e0)):
        sid[s:e + 1] = k
    out = []
    for i in range(1, len(st) - 1):
        a, b = st[i], en[i]
        if sid[a] >= 0 and sid[a] == sid[b] and b < e0[sid[a]]:
            out.append((int(val[i]), (b - a + 1) * DT, int(val[i - 1]), int(val[i + 1]),
                        float(f["sucrose"][a])))
    return out


def fast_eggs(f, good=0, bad=200, within_s=10.0):
    """[claim] fig3d: eggs laid on `good` within `within_s` s of entering it from
    `bad`; the dwell time is the duration of the preceding visit to `bad`.
    The sucrose series switches label at the boundary and has no barrier state,
    so 'from crossing the midline' and 'from leaving 200 mM' are the same frame
    here."""
    st, en, val = visits(f["sucrose"])
    out = []
    for e in f["eggs"]:
        i = np.searchsorted(st, e, side="right") - 1
        if val[i] != good or i == 0 or val[i - 1] != bad:
            continue
        t_in = (e - st[i]) * DT
        if t_in <= within_s:
            out.append({"egg": int(e), "t_in": t_in, "dwell": (en[i - 1] - st[i - 1] + 1) * DT,
                        "first_visit": i - 1 == 0})
    return out


ALIGN_S = 120  # [std] egg-aligned window, +-120 s; eggs whose window leaves the recording are dropped (Fig. 3F legend)


def egg_aligned(f, eggs=None, before=ALIGN_S, after=ALIGN_S, smooth_s=5.0):
    """[claim] M8: speed (5-s boxcar, Fig. 1 legend) aligned to egg deposition."""
    eggs = f["eggs"] if eggs is None else np.asarray(eggs)
    sm = boxcar(f["speed"].astype(float), smooth_s)
    b = int(before * FPS); a = int(after * FPS)
    rows = [sm[e - b:e + a + 1] for e in eggs if e - b >= 0 and e + a < f["n"]]
    return np.array(rows) if rows else np.zeros((0, b + a + 1))


def speed_rise(f, win_s=60):
    """[claim] fig5gh: per egg, mean raw speed over the win_s before the pause
    onset (egg minus pause time) and over the win_s before that."""
    out = []
    w = int(win_s * FPS)
    for e, p in zip(f["eggs"], f["pause"]):
        if not np.isfinite(p):
            continue
        on = e - int(round(p * FPS))
        if on - 2 * w < 0:
            continue
        out.append((f["speed"][on - w:on].mean(), f["speed"][on - 2 * w:on - w].mean()))
    return np.array(out).reshape(-1, 2)


def frac_ci(k, n):
    lo, hi = clopper(k, n)
    return k / n if n else np.nan, lo, hi


# ---------------------------------------------------------------- fig. S4, model 1

# [assume] Lag boxes of the history kernel, in frames: 0, then doubling widths up
# to 4096 frames (34 min). The paper fits its kernel "using code and concepts
# from (82)", which it does not give; a piecewise-constant kernel on log-spaced
# lags is a standard basis for a long-tailed kernel.
KERNEL_BOXES = [(0, 1)] + [(2 ** k, 2 ** (k + 1)) for k in range(12)]


def kernel_features(sucrose, scale=200.0, boxes=KERNEL_BOXES):
    """x_j(t) = sum over lags k in box j of s(t - k), s = [sucrose]/scale.
    Frames before the recording count as s = 0; frames with t < the longest lag
    are flagged invalid."""
    s = sucrose.astype(float) / scale
    c = np.concatenate([[0.0], np.cumsum(s)])  # c[i] = sum s[:i]
    t = np.arange(len(s))
    X = np.empty((len(s), len(boxes)))
    for j, (lo, hi) in enumerate(boxes):
        a = np.clip(t - hi + 1, 0, None); b = np.clip(t - lo + 1, 0, None)
        X[:, j] = c[b] - c[a]
    valid = t >= boxes[-1][1]
    return X, valid


def fit_kernel(flies, mode="working", boxes=KERNEL_BOXES):
    """[claim] figs4 reading: least squares fit of the per-frame egg indicator,
    over search frames, to c + sum_j beta_j x_j(t) with zero kernel area
    (sum_j beta_j * width_j = 0, Methods, Mathematical models: "The area under
    the kernel is 0"). Returns (c, beta)."""
    widths = np.array([hi - lo for lo, hi in boxes], float)
    rows, ys = [], []
    for f in flies:
        if len(f["eggs"]) == 0:
            continue
        X, valid = kernel_features(f["sucrose"], boxes=boxes)
        m = np.zeros(f["n"], bool)
        s0, e0 = search_windows(f["starts"], f["eggs"], f["n"], mode)
        for s, e in zip(s0, e0):
            m[s:e + 1] = True
        m &= valid
        y = np.zeros(f["n"]); y[f["eggs"]] = 1
        rows.append(X[m]); ys.append(y[m])
    X = np.vstack(rows); y = np.concatenate(ys)
    # beta_last = -sum_{j<last} beta_j w_j / w_last
    Z = X[:, :-1] - np.outer(X[:, -1], widths[:-1] / widths[-1])
    A = np.column_stack([np.ones(len(Z)), Z])
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    beta = np.concatenate([coef[1:], [-(coef[1:] * widths[:-1]).sum() / widths[-1]]])
    return coef[0], beta, len(y)


def predict_kernel(f, c, beta, boxes=KERNEL_BOXES):
    X, valid = kernel_features(f["sucrose"], boxes=boxes)
    return c + X @ beta  # frames before the recording count as s = 0
