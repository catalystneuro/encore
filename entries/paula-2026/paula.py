"""Loading and measures for de Paula et al. (2026), PRX Life 4, 023018, on DANDI:000713.

The paper analyses the population firing rate of "local populations" (the units of one
brain subregion in one session) of the Allen Visual Behavior Neuropixels dataset in 100-s
windows of four conditions. This module streams each session's NWB file from the archive
(remfile and h5py, nothing written to disk), builds the windows and returns one row per
window with every measure the claims use. Sources of each parameter:

- Population rate r(t): spike counts of the N units in nonoverlapping 50 ms bins divided by
  N times 50 ms (Methods II.B, Eq. 1; nonoverlap from Methods II.C, T = 2000 points per 100 s).
- CV: the standard deviation over the mean of r(t) in each nonoverlapping 10-s window, averaged
  over the ten (Methods II.B, Eq. 2). A 10-s window with no spike has no CV and is left out of
  the mean (a standard choice; it occurs only in near-silent populations).
- Bandt and Pompe patterns, D = 6, tau = 1, ties ranked higher for the later element (Methods
  II.C: "In cases of equal values (ties), we assigned higher ranks to later-occurring
  elements"), done with a stable argsort. H normalised by ln(D!) (Eq. 6). C = Q0 DJS[P, Pe] H
  with DJS as in Eq. 9 in natural logs and Q0 the standard MPR constant of Ref. 29 for D!
  states (the claims file's reading of "normalization constant").
- Surrogate: each neuron's interspike intervals within the window shuffled independently
  (Methods II.E); the first spike stays in place (claims file, opening comment; a standard
  choice). Generators are seeded from the claim (protocol) and the session index.
- Active behavior: the first stimulus block of the session (the change detection task with
  `active` true), from its first flash onset, cut into nonoverlapping 100-s windows, at most
  36 (Methods II.A: "The approximately 3600 s ... were divided into 36 nonoverlapping 100-s
  windows (sessions shorter than 3600 s yielded fewer windows)"). Starting at the first flash
  is a standard choice.
- Natural images: per image, its non-omitted flashes of the active block, [start, stop)
  pieces concatenated with shifted spike times, central 100 s (Methods II.A). Blanks: the
  500 ms after each such flash, [stop, min(stop + 0.5, next onset)); reading 'a' every flash,
  reading 'b' only flashes followed by a non-omitted flash (claims file, opening comment).
- Spontaneous: the longest `spontaneous` presentation after the active block (the ~5 min gray
  screen, Methods II.A); reading 'a' the first two 100-s windows from its start, reading 'b'
  two consecutive windows centred in it (claims file, opening comment).
- Unit readings: 'all', every unit of the units table, and 'qc', ISI violations < 0.5,
  amplitude cutoff < 0.1 and presence ratio > 0.9 (the claims file's two readings); 'vbn',
  snr > 1, ISI violations < 1 and firing rate > 0.1 spikes/s, the "good_unit_filter" of the
  Allen Institute's Visual Behavior Neuropixels quickstart tutorial (AllenSDK, commit
  a56bd8ea7613a812334602b64746cdd30c325a96, doc_template/examples_root/examples/nb/
  visual_behavior_neuropixels_quickstart.ipynb). 'vbn' is the adopted reading, an assumption:
  the paper states no filter, and of the filters tried it is the one whose neuron counts per
  population match Table I (see the notebook, claim table1-sample). Unit counts per subregion
  are also kept for 'good' (quality label 'good'), 'qc95' (as 'qc' with presence ratio > 0.95)
  and 'good_pr95' ('good' with presence ratio > 0.95), for the count comparison only.
- Brain structure of a unit: the `location` of its peak channel in the electrodes table.
- Mean pairwise correlation (supplement Sec. III): the mean Pearson correlation over all unit
  pairs of spike counts in 50 ms and 20 ms bins, units without spikes in the window left out
  (claims file; a standard choice). Computed for visual cortex and midbrain populations only,
  the areas the claims on it concern.
- Robustness (Supplemental Sec. II): C and H for bin 20 ms with (D, tau) = (3, 4), (5, 1),
  (6, 1) and bin 50 ms with (4, 2), (5, 3), the combinations the claims file lists.
"""
import math
import os
import time
import zlib

for _v in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")  # many small fits run in parallel processes

import h5py
import numpy as np
import pandas as pd
import remfile
import requests

DANDISET = "000713"
VERSION = "0.240702.1725"
PAPER = "paula-2026"
API = f"https://api.dandiarchive.org/api/dandisets/{DANDISET}/versions/{VERSION}"

BIN = 0.05
WIN = 100.0
CV_WIN = 10.0
D, TAU = 6, 1
ROBUST = [(0.02, 3, 4), (0.02, 5, 1), (0.02, 6, 1), (0.05, 4, 2), (0.05, 5, 3)]
SURR_SEED_OFFSETS = [0, 1000, 2000, 3000, 4000]
SURR_CLAIM = "fig1c-cv-above-surrogate"
MIN_UNITS = 30
MIN_SESSIONS = 8
UNIT_READINGS = ["vbn", "all", "qc"]  # 'vbn' adopted; the surrogate is drawn under five seeds for it only
MAIN_UNITS = "vbn"
COUNT_FILTERS = ["all", "qc", "vbn", "good", "qc95", "good_pr95"]


def unit_filters(units):
    """Boolean selections of the unit readings and of the filters used for counts only."""
    q = (units.isi_violations < 0.5) & (units.amplitude_cutoff < 0.1)
    good = units.quality == "good"
    return {"all": pd.Series(True, index=units.index),
            "qc": q & (units.presence_ratio > 0.9),
            "vbn": (units.snr > 1) & (units.isi_violations < 1) & (units.firing_rate > 0.1),
            "good": good,
            "qc95": q & (units.presence_ratio > 0.95),
            "good_pr95": good & (units.presence_ratio > 0.95)}

AREAS = {
    "VIS": ["VISal", "VISam", "VISl", "VISp", "VISpm", "VISrl"],
    "TH": ["LGd", "LP", "MGd", "MGm", "MGv", "PIL", "POL", "PoT", "SGN"],
    "HP": ["CA1", "CA3", "DG", "POST", "ProS", "SUB"],
    "MB": ["APN", "NB", "NOT", "MRN", "SCig"],
}
REGION_AREA = {r: a for a, rs in AREAS.items() for r in rs}
REGION_ORDER = [r for rs in AREAS.values() for r in rs]


def seed(claim):
    """The claim's seed, zlib.crc32(b"<paper>/<claim>") (protocol, author step 3)."""
    return zlib.crc32(f"{PAPER}/{claim}".encode())


def list_sessions():
    """The ecephys session files of the pinned version (not the probe LFP files and not the
    behavior-only `_image.nwb` files), sorted by path."""
    url = f"{API}/assets/?page_size=1000"
    assets = []
    while url:
        r = requests.get(url, timeout=60)
        r.raise_for_status()
        r = r.json()
        assets += r["results"]
        url = r["next"]
    s = [a for a in assets if "probe" not in a["path"] and not a["path"].endswith("_image.nwb")]
    return sorted(s, key=lambda a: a["path"]), len(assets)


def s3_url(asset):
    b = asset["blob"]
    return f"https://dandiarchive.s3.amazonaws.com/blobs/{b[:3]}/{b[3:6]}/{b}"


def _str(a):
    return np.array([v.decode() if isinstance(v, bytes) else str(v) for v in a])


# ---------------------------------------------------------------- ordinal measures

def _q0(n):
    return -2.0 / (((n + 1.0) / n) * math.log(n + 1.0) - 2.0 * math.log(2.0 * n) + math.log(n))


def _shannon(p):
    p = p[p > 0]
    return -np.sum(p * np.log(p))


def bandt_pompe(x, d=D, tau=TAU):
    """Normalised permutation entropy H and MPR complexity C of series x (Eqs. 3 to 9)."""
    x = np.asarray(x, float)
    n = len(x) - (d - 1) * tau
    if n <= 0:
        return np.nan, np.nan
    emb = np.stack([x[i * tau:i * tau + n] for i in range(d)], axis=1)
    perm = np.argsort(emb, axis=1, kind="stable")
    code = (perm * (d ** np.arange(d))).sum(axis=1)
    _, counts = np.unique(code, return_counts=True)
    nstates = math.factorial(d)
    p = np.zeros(nstates)
    p[:len(counts)] = counts / counts.sum()
    s = _shannon(p)
    h = s / math.log(nstates)
    pe = np.full(nstates, 1.0 / nstates)
    djs = _shannon((p + pe) / 2) - s / 2 - math.log(nstates) / 2
    return h, _q0(nstates) * djs * h


def cv_windows(r, per=int(CV_WIN / BIN)):
    """CV of r in nonoverlapping windows of `per` bins (Eq. 2); NaN where the mean is 0."""
    m = len(r) // per
    x = r[:m * per].reshape(m, per)
    mu = x.mean(axis=1)
    sd = x.std(axis=1)
    with np.errstate(invalid="ignore", divide="ignore"):
        return np.where(mu > 0, sd / mu, np.nan)


def js_divergence(a, b, bins, base=2.0):
    """JS divergence of the histograms of a and b, `bins` equal bins over their pooled range."""
    a = np.asarray(a, float)
    b = np.asarray(b, float)
    a = a[np.isfinite(a)]
    b = b[np.isfinite(b)]
    if len(a) == 0 or len(b) == 0:
        return np.nan
    lo, hi = min(a.min(), b.min()), max(a.max(), b.max())
    if hi <= lo:
        return 0.0
    pa = np.histogram(a, bins=bins, range=(lo, hi))[0].astype(float)
    pb = np.histogram(b, bins=bins, range=(lo, hi))[0].astype(float)
    pa /= pa.sum()
    pb /= pb.sum()
    m = (pa + pb) / 2

    def kl(p):
        k = p > 0
        return np.sum(p[k] * np.log(p[k] / m[k]))

    return (kl(pa) + kl(pb)) / 2 / math.log(base)


# ---------------------------------------------------------------- windows

def _concat(times, owners, pieces):
    """Spikes inside the [a, b) pieces, mapped onto a time axis where the pieces abut."""
    pieces = np.asarray(pieces, float)
    if len(pieces) == 0:
        return np.array([]), np.array([], int), 0.0
    a, b = pieces[:, 0], pieces[:, 1]
    offs = np.concatenate([[0.0], np.cumsum(b - a)])
    k = np.searchsorted(a, times, side="right") - 1
    ok = (k >= 0) & (times < b[np.clip(k, 0, None)])
    k = k[ok]
    return times[ok] - a[k] + offs[k], owners[ok], offs[-1]


def _window(times, owners, t0, t1):
    m = (times >= t0) & (times < t1)
    return times[m] - t0, owners[m]


def group_by_unit(t, own):
    """Spike times regrouped by unit (each unit's spikes in time order) and group bounds."""
    o = np.argsort(own, kind="stable")
    ts, os_ = t[o], own[o]
    bounds = np.flatnonzero(np.r_[True, os_[1:] != os_[:-1], True])
    return ts, bounds


def shuffle_isi(grouped, rng):
    """Each unit's interspike intervals shuffled independently, its first spike kept in place
    (Methods II.E; the start is the claims file's standard choice)."""
    ts, bounds = grouped
    out = np.empty_like(ts)
    for i in range(len(bounds) - 1):
        x = ts[bounds[i]:bounds[i + 1]]
        d = np.diff(x)
        rng.shuffle(d)
        out[bounds[i]] = x[0]
        out[bounds[i] + 1:bounds[i + 1]] = x[0] + np.cumsum(d)
    return out


def rate(t, n_units, length=WIN, bw=BIN):
    nb = int(round(length / bw))
    c = np.bincount(np.minimum((t / bw).astype(int), nb - 1), minlength=nb)[:nb]
    return c / (n_units * bw)


def mean_corr(t, own, n_units, bw, length=WIN):
    nb = int(round(length / bw))
    b = np.minimum((t / bw).astype(int), nb - 1)
    m = np.bincount(own * nb + b, minlength=n_units * nb).reshape(n_units, nb).astype(np.float32)
    m = m[m.std(axis=1) > 0]
    if len(m) < 2:
        return np.nan
    m -= m.mean(axis=1, keepdims=True)
    m /= np.linalg.norm(m, axis=1, keepdims=True)
    c = m @ m.T
    k = len(m)
    return float((c.sum() - np.trace(c)) / (k * (k - 1)))


def window_measures(t, own, n_units, surr_rngs, do_corr, full=True):
    """All measures of one 100-s window of a population (t in 0..100 s, own in 0..N-1).
    With full False, only CV, H, C and the surrogate."""
    r = rate(t, n_units)
    cv10 = cv_windows(r)
    h, c = bandt_pompe(r)
    out = {"cv": np.nanmean(cv10) if np.isfinite(cv10).any() else np.nan, "H": h, "C": c,
           "rate": len(t) / (n_units * WIN), "cv10": cv10}
    grouped = group_by_unit(t, own) if len(t) else None
    for bw, d, tau in (ROBUST if full else []):
        rr = r if bw == BIN else rate(t, n_units, bw=bw)
        hh, cc = bandt_pompe(rr, d, tau)
        out[f"C_{int(bw*1000)}_{d}_{tau}"] = cc
        out[f"H_{int(bw*1000)}_{d}_{tau}"] = hh
    if do_corr and full:
        out["corr50"] = mean_corr(t, own, n_units, 0.05)
        out["corr20"] = mean_corr(t, own, n_units, 0.02)
    for j, rng in enumerate(surr_rngs):
        ts = shuffle_isi(grouped, rng) if grouped is not None else t
        ts = ts[(ts >= 0) & (ts < WIN)]
        rs = rate(ts, n_units)
        cvs = cv_windows(rs)
        hs, cs = bandt_pompe(rs)
        sfx = "" if j == 0 else f"_s{SURR_SEED_OFFSETS[j]}"
        out["s_cv" + sfx] = np.nanmean(cvs) if np.isfinite(cvs).any() else np.nan
        out["s_H" + sfx] = hs
        out["s_C" + sfx] = cs
        out["s_cv10" + sfx] = cvs
    return out


# ---------------------------------------------------------------- one session

def read_session(asset):
    """Stream one session: metadata, epochs and the spike times of units in candidate
    regions (a region with at least 30 units under the 'all' reading), up to the end of
    the spontaneous epoch."""
    f = h5py.File(remfile.File(s3_url(asset)), "r")
    meta = {"path": asset["path"], "session_description": f["session_description"][()].decode(),
            "subject": f["general/subject/subject_id"][()].decode(),
            "genotype": f["general/subject/genotype"][()].decode(),
            "session_start_time": f["session_start_time"][()].decode()}
    e = f["general/extracellular_ephys/electrodes"]
    loc = pd.Series(_str(e["location"][:]), index=e["id"][:])
    u = f["units"]
    units = pd.DataFrame({
        "region": loc.loc[u["peak_channel_id"][:]].values,
        "isi_violations": u["isi_violations"][:], "amplitude_cutoff": u["amplitude_cutoff"][:],
        "presence_ratio": u["presence_ratio"][:], "quality": _str(u["quality"][:]),
        "firing_rate": u["firing_rate"][:], "snr": u["snr"][:]})
    pc = u["peak_channel_id"][:]
    if "group_name" in e:
        meta["n_probes"] = int(pd.Series(_str(e["group_name"][:]), index=e["id"][:]).loc[pc].nunique())
    else:
        meta["n_probes"] = -1
    idx = u["spike_times_index"][:].astype(np.int64)
    meta["n_units"] = len(units)
    meta["n_spikes"] = int(idx[-1])

    ni_name = [k for k in f["intervals"].keys() if k.startswith("Natural_Images")]
    meta["image_table"] = ni_name
    ni = f["intervals"][ni_name[0]]
    stim = pd.DataFrame({"start": ni["start_time"][:], "stop": ni["stop_time"][:],
                         "image": _str(ni["image_name"][:]), "block": ni["stimulus_block"][:],
                         "active": ni["active"][:], "omitted": ni["omitted"][:],
                         "is_change": ni["is_change"][:], "novel": ni["is_image_novel"][:]})
    act_block = stim[stim.active].block.min()
    stim = stim[stim.block == act_block].sort_values("start").reset_index(drop=True)
    stim["omitted"] = stim.omitted.astype(bool) | (stim.image == "omitted")
    sp = f["intervals/spontaneous_presentations"]
    spont = pd.DataFrame({"start": sp["start_time"][:], "stop": sp["stop_time"][:]})
    act_end = stim.stop.max()
    spont = spont[spont.start >= act_end - 1]
    spont["dur"] = spont.stop - spont.start
    meta["spont_epochs"] = spont[["start", "stop"]].values.tolist()
    sp_best = spont.sort_values("dur").iloc[-1] if len(spont) else None
    meta["active_start"] = float(stim.start.min())
    meta["active_end"] = float(act_end)
    cutoff = float(sp_best.stop) if sp_best is not None else act_end
    meta["cutoff"] = cutoff

    counts = units.region.value_counts()  # 'all' holds every other reading, so its counts bound them
    cand = counts[counts >= MIN_UNITS].index
    keep = np.flatnonzero(units.region.isin(cand).values & units.region.isin(REGION_AREA).values)
    # also keep all visual-cortex units, for the clock check
    vis = np.flatnonzero(units.region.isin(AREAS["VIS"]).values)
    keep = set(np.union1d(keep, vis).tolist())
    starts = np.r_[0, idx[:-1]]
    st = u["spike_times"]
    spikes = {}
    # read contiguous blocks of units, about 40 MB at a time, keeping spikes before the cutoff
    i = 0
    n = len(units)
    while i < n:
        j = i
        while j < n and idx[j] - starts[i] < 5_000_000:
            j += 1
        j = max(j, i + 1)
        block = st[starts[i]:idx[j - 1]]
        for k in range(i, j):
            if k not in keep:
                continue
            x = block[starts[k] - starts[i]:idx[k] - starts[i]]
            spikes[k] = x[x < cutoff + 1].copy()
        i = j
    meta["fingerprint"] = [float(x) for x in st[:5]] + [float(st[idx[-1] - 1])]
    f.close()
    return meta, units, stim, sp_best, spikes


def flash_table(stim):
    """Per presentation of the active block: image piece [start, stop) and blank piece
    [stop, min(stop + 0.5, next onset)); blank reading 'b' keeps only flashes followed by a
    non-omitted flash."""
    st = stim.copy()
    nxt = np.r_[st.start.values[1:], np.inf]
    st["bstop"] = np.minimum(st.stop.values + 0.5, nxt)
    st["next_shown"] = np.r_[~st.omitted.values[1:], False]
    return st


def epoch_windows(stim, sp_best):
    """Windows in session time: active (36 at most) and spontaneous (readings a and b)."""
    out = []
    a0, a1 = stim.start.min(), stim.stop.max()
    nwin = min(36, int((a1 - a0) // WIN))
    for k in range(nwin):
        out.append(("active", "-", k, a0 + k * WIN))
    if sp_best is not None:
        s0, s1 = float(sp_best.start), float(sp_best.stop)
        if s1 - s0 >= 2 * WIN:
            for k in range(2):
                out.append(("spont", "a", k, s0 + k * WIN))
            mid = (s0 + s1) / 2
            for k in range(2):
                out.append(("spont", "b", k, mid - WIN + k * WIN))
    return out


def concat_windows(t, own, ft):
    """The natural-image and blank windows of a population: for each image its pieces
    concatenated (spike times shifted so the pieces abut) and the central 100 s kept
    (Methods II.A). Returns (condition, reading, k, image, t, own, series length)."""
    starts = ft.start.values
    k = np.searchsorted(starts, t, side="right") - 1
    ok = k >= 0
    t, own, k = t[ok], own[ok], k[ok]
    dt = t - starts[k]
    img_len = (ft.stop - ft.start).values
    blk_len = (ft.bstop - ft.stop).values
    shown = ~ft.omitted.values
    in_img = shown[k] & (dt < img_len[k])
    in_blk = shown[k] & (dt >= img_len[k]) & (dt < img_len[k] + blk_len[k])
    out = []
    names = sorted(ft.image[shown].unique())
    for i, img in enumerate(names):
        m_img = shown & (ft.image.values == img)
        for cond, rd, sel, inside, plen, shift in [
                ("images", "-", m_img, in_img, img_len, 0.0),
                ("blanks", "a", m_img, in_blk, blk_len, img_len),
                ("blanks", "b", m_img & ft.next_shown.values, in_blk, blk_len, img_len)]:
            off = np.full(len(ft), np.nan)
            off[sel] = np.r_[0.0, np.cumsum(plen[sel])[:-1]]
            L = plen[sel].sum()
            mk = inside & sel[k]
            sh = shift[k[mk]] if isinstance(shift, np.ndarray) else 0.0
            tc = off[k[mk]] + dt[mk] - sh
            lo = L / 2 - WIN / 2
            w = (tc >= lo) & (tc < lo + WIN)
            if L < WIN:
                out.append((cond, rd, i, img, None, None, L))
                continue
            tw = tc[w] - lo
            ow = own[mk][w]
            o = np.argsort(tw, kind="stable")
            out.append((cond, rd, i, img, tw[o], ow[o], L))
    return out


def clock_check(stim, vis_times):
    """Visual cortex response to flash onsets: mean spikes per flash in 30 to 130 ms after
    onset minus the 100 ms before, for the true onsets and for onsets shifted by 375 ms
    (the middle of the gray screen), and for omitted flashes."""
    on = stim.start.values[~stim.omitted.values]
    vt = np.sort(vis_times)

    def contrast(o):
        post = np.searchsorted(vt, o + 0.13) - np.searchsorted(vt, o + 0.03)
        pre = np.searchsorted(vt, o) - np.searchsorted(vt, o - 0.10)
        return float(np.mean(post - pre))

    om = stim.start.values[stim.omitted.values]
    return {"clock_true": contrast(on), "clock_shift": contrast(on + 0.375),
            "clock_omitted": contrast(om) if len(om) else np.nan}


def process_session(args):
    """Read one session and compute all windows of all its populations."""
    sess_i, asset = args
    return compute_session(sess_i, *read_session(asset))


def compute_session(sess_i, meta, units, stim, sp_best, spikes):
    """All windows of all populations of one session, under both unit readings."""
    meta["session_index"] = sess_i
    vis_k = [k for k in spikes if units.region.iat[k] in AREAS["VIS"]]
    meta.update(clock_check(stim, np.concatenate([spikes[k] for k in vis_k]) if vis_k
                            else np.array([])))
    meta["n_vis_units_clock"] = len(vis_k)
    filt = unit_filters(units)
    for name in COUNT_FILTERS:
        meta[f"region_counts_{name}"] = units.region[filt[name]].value_counts().to_dict()
    meta["n_flashes"] = int((~stim.omitted).sum())
    meta["n_omitted"] = int(stim.omitted.sum())
    meta["n_changes"] = int(np.nansum(stim.is_change.values))
    meta["n_images"] = int(stim[~stim.omitted].image.nunique())
    meta["novel_fraction"] = float(np.nanmean(stim.novel.values[~stim.omitted.values].astype(float)))
    ft = flash_table(stim)
    shown = ft[~ft.omitted]
    blk = (shown.bstop - shown.stop).values
    meta["flashes_per_image"] = shown.image.value_counts().to_dict()
    meta["changes_per_image"] = shown[np.asarray(shown.is_change, float) > 0].image.value_counts().to_dict()
    meta["blank_piece_full"] = int((blk >= 0.5 - 1e-6).sum())
    meta["blank_piece_short"] = int((blk < 0.5 - 1e-6).sum())
    meta["blank_piece_median"] = float(np.median(blk))
    meta["gray_after_flash_median"] = float(np.median((np.r_[ft.start.values[1:], np.nan] - ft.stop.values)[~ft.omitted.values][:-1]))
    ew = epoch_windows(stim, sp_best)
    meta["n_active_windows"] = sum(1 for w in ew if w[0] == "active")
    meta["n_spont_windows"] = sum(1 for w in ew if w[0] == "spont" and w[1] == "a")
    rows, cv10 = [], []
    base = seed(SURR_CLAIM)
    for ur in UNIT_READINGS:
        sel = filt[ur]
        for region in REGION_ORDER:
            ks = np.flatnonzero(sel.values & (units.region == region).values)
            if len(ks) < MIN_UNITS:
                continue
            n = len(ks)
            t_all = np.concatenate([spikes[k] for k in ks])
            o_all = np.concatenate([np.full(len(spikes[k]), j) for j, k in enumerate(ks)])
            o = np.argsort(t_all, kind="stable")
            t_all, o_all = t_all[o], o_all[o]
            do_corr = REGION_AREA[region] in ("VIS", "MB")
            wins = []
            for cond, rd, k, t0 in ew:
                a, b = np.searchsorted(t_all, [t0, t0 + WIN])
                wins.append((cond, rd, k, "", t_all[a:b] - t0, o_all[a:b], WIN))
            a, b = np.searchsorted(t_all, [stim.start.min() - 1, stim.stop.max() + 1])
            wins += concat_windows(t_all[a:b], o_all[a:b], ft)
            for wi, (cond, rd, k, img, t, ow, length) in enumerate(wins):
                if t is None:
                    continue
                nseeds = 5 if (cond == "active" and ur == MAIN_UNITS) else 1
                rngs = [np.random.default_rng([base + off, sess_i, wi, UNIT_READINGS.index(ur)])
                        for off in SURR_SEED_OFFSETS[:nseeds]]
                m = window_measures(t, ow, n, rngs, do_corr)
                c10 = m.pop("cv10")
                s10 = {k: m.pop(k) for k in [k for k in m if k.startswith("s_cv10")]}
                row = {"session": sess_i, "subject": meta["subject"], "units": ur,
                       "region": region, "area": REGION_AREA[region], "n": n,
                       "condition": cond, "reading": rd, "k": k, "image": img,
                       "series_length": length}
                row.update(m)
                rows.append(row)
                if cond == "active":
                    cv10.append({"session": sess_i, "units": ur, "region": region, "k": k,
                                 "cv10": c10, **s10})
    return meta, pd.DataFrame(rows), cv10


def _safe(args):
    for attempt in range(4):
        try:
            return process_session(args)
        except Exception as exc:  # network errors: retry, then report the failure
            err = repr(exc)
            time.sleep(10 * (attempt + 1))
    return {"session_index": args[0], "path": args[1]["path"], "error": err}, None, None


def run_all(assets, workers=4):
    """Process every session in parallel processes; returns the session table, the window
    table and the 10-s CV series of the active windows, and the sessions that failed."""
    import multiprocessing as mp
    from concurrent.futures import ProcessPoolExecutor
    metas, dfs, cv10, failed = [], [], [], []
    ctx = mp.get_context("fork")
    with ProcessPoolExecutor(workers, mp_context=ctx) as ex:
        for meta, df, c in ex.map(_safe, list(enumerate(assets))):
            if df is None:
                failed.append(meta)
                continue
            metas.append(meta)
            dfs.append(df)
            cv10 += c
    return pd.DataFrame(metas), pd.concat(dfs, ignore_index=True), cv10, failed


# ---------------------------------------------------------------- analysis helpers

CONDITIONS = ["images", "active", "blanks", "spont"]
COND_PAIRS = [("images", "active"), ("images", "blanks"), ("images", "spont"),
              ("active", "blanks"), ("active", "spont"), ("blanks", "spont")]


def conditions(windows, units="all", blanks="a", spont="a"):
    """The windows of the four conditions under one unit reading and one condition reading
    (blank reading 'a' or 'b', spontaneous reading 'a' or 'b'; claims file, opening comment)."""
    w = windows[windows.units == units]
    keep = ((w.condition == "active") | (w.condition == "images")
            | ((w.condition == "blanks") & (w.reading == blanks))
            | ((w.condition == "spont") & (w.reading == spont)))
    return w[keep]


def kept_regions(windows, units="all"):
    """Subregions with populations of at least 30 units in at least eight sessions
    (Methods II.A)."""
    p = windows[(windows.units == units) & (windows.condition == "active")]
    ns = p.groupby("region").session.nunique()
    return [r for r in REGION_ORDER if ns.get(r, 0) >= MIN_SESSIONS]


def js_matrix(w, value, regions, bins, base=2.0):
    """JS divergence between the distributions of `value` of every pair of subregions."""
    vals = {r: w.loc[w.region == r, value].values for r in regions}
    n = len(regions)
    m = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            m[i, j] = m[j, i] = js_divergence(vals[regions[i]], vals[regions[j]], bins, base)
    return pd.DataFrame(m, index=regions, columns=regions)


def summed_js(m, area, mode):
    """Sum of within-area JS values: mode 'all' every pair of the area's block above its
    diagonal; mode 'adjacent' the block's first off-diagonal (Table I order)."""
    rs = [r for r in m.index if REGION_AREA[r] == area]
    b = m.loc[rs, rs].values
    if mode == "all":
        return float(b[np.triu_indices(len(rs), 1)].sum())
    return float(np.diag(b, 1).sum())


def pct_diff(sa, sb, mode):
    """Percentage difference of two sums: 'second' |A - B| / B, 'mean' |A - B| / mean."""
    return 100 * abs(sa - sb) / (sb if mode == "second" else (sa + sb) / 2)


def trajectory(cv, c, width, min_count):
    """Mean C and its standard error in bins of CV of the given width (Fig. 5 legend)."""
    cv = np.asarray(cv)
    c = np.asarray(c)
    ok = np.isfinite(cv) & np.isfinite(c)
    cv, c = cv[ok], c[ok]
    b = np.floor(cv / width + 1e-9).astype(int)
    rows = []
    for k in np.unique(b):
        x = c[b == k]
        if len(x) < max(min_count, 1):
            continue
        rows.append({"lo": k * width, "hi": (k + 1) * width, "n": len(x), "mean": x.mean(),
                     "se": x.std(ddof=1) / np.sqrt(len(x)) if len(x) > 1 else 0.0})
    return pd.DataFrame(rows)
