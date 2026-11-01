"""Loading and measures for dandiset 001260 (dataset KI of Le Merre, Heining et al., 2026).

Le Merre, Heining et al., "A prefrontal cortex map based on single-neuron activity",
Nature Neuroscience, doi:10.1038/s41593-025-02190-z. Claims file:
claims/001260/10.1038-s41593-025-02190-z.yaml ("claims header" below). The paper's code is
https://github.com/hejDMC/pfcmap at commit 9ae52eddc47fbb590ef4e1b1949507334707a0f1 ("code").

Where each parameter comes from:

- Spontaneous epochs, [onset - 3 s, onset]: Methods, Epoch selection. Which stimulus series give
  the onsets per behavioral setting (all stimuli in Passive, the 10-kHz tone in Context,
  Detection and Opto, tone and blue noise in Aversion, trial starts in the working-memory
  setting the code calls "Attention"): code, extract_prepost_quietactive.py, stimdict.
- Epochs overlapping licking or spike-band saturation are dropped: Methods, Epoch selection.
  Licking is read from LickOnset/LickOffset in the files; saturation from the "spike saturation
  start/stop" series.
- Sleep-like periods: Methods, Detection of sleep-like periods (10-ms bins of all cortical
  spikes, Savitzky-Golay 11 points order 3, troughs below 0.2 of the geometric mean for longer
  than 5 ms, extended to the geometric mean, merged within 1.5 s, padded by 1 s around merged
  and 0.3 s around single off periods). The geometric mean is taken over the bins with a
  positive smoothed rate (assumption: the geometric mean of a vector with zeros is zero, which
  would make the threshold meaningless). The probe whose cortical units are used for a probe
  without enough of them is the code's table (config/datatables/allrecs_allprobes.xlsx,
  quietdet_src, "from-other"); hippocampal recordings are not checked ("ignore" in that table).
  Active epochs lie at least 1 s from a sleep-like period (Methods; code active_buff = [-1, 1]);
  sleep-like epochs overlap one.
- Per-epoch metrics: log10 FR of the count over 3 s, B and M from ISIs (Methods, equations 2
  and 3), B and M only in epochs with at least 6 spikes; units need at least 12 such active
  epochs; log10 FR averaged over epochs with at least one spike (claims header, from the code).
  The s.d. of ISIs is the population s.d. (ddof 0, numpy's default, as in the code's
  interval_fns): a standard choice.
- Region and layer from the location of the unit's electrode, split at the first digit (code,
  settings.py decompose_area_layer); PFC subregions and parent regions as code settings.py
  (pfc_set, parent_dict). Deep layers: a layer label containing 5 or 6 (claims header).
- Waveform classes: Peak_to_Trough < 0.38 ms nw, > 0.43 ms ww (Methods, Waveform
  classification).
- SOM: hexagonal grid, shape from the ratio of the two largest eigenvalues of the feature
  covariance, linear PCA initialization, batch training for 200 iterations with Gaussian
  neighborhood exp(-d^2/sigma^2), sigma decaying from the largest to the smallest node distance
  (Methods, SOM analysis; code utils/som_helpers.py get_kshape, getInitialMap_pca and
  utils/my_somz.py, batch branch). Deterministic, so no seed.
- Categories: Ward linkage of node prototypes standardized across nodes (Methods, Hierarchical
  clustering analyses), cut at 8 (ww) or 5 (nw) clusters (code settings.py nclust_dict).
- E-scores: Methods, Enrichment statistics, equation 5, shuffling the population labels within
  each group; P = 1 - max(f-, f+), significant at P < 0.05 (claims header). 1,000 shuffles.
"""
import json
import re
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
import requests
from scipy.signal import savgol_filter

DANDISET = "001260"
VERSION = "0.250911.0744"
API = "https://api.dandiarchive.org/api"

PFC_SUBREGIONS = ["MOs", "ACAd", "ACAv", "PL", "ILA", "ORBm", "ORBvl", "ORBl", "AId", "AIv", "FRP"]
# code settings.py, parent_dict
PARENT = {
    "PFC": ["MOs", "ACAd", "ACAv", "PL", "ILA", "FRP", "ACA", "ORBl", "ORBvl", "ORBm", "ORB", "AId", "AIv"],
    "DP": ["DP"], "TT": ["TTd", "TTv"], "LS": ["LSr", "SH", "LSv", "LSc"], "CP": ["CP"],
    "ACB": ["ACB"], "HPF": ["CA1", "CA2", "CA3", "DG-mo", "DG-po", "DG-sg", "HPF"], "MO": ["MOp"],
    "AON": ["AON"], "PIR": ["PIR"],
    "SS": ["SSp-bfd", "SSp-m", "SSs", "SSp-tr", "SSp-n", "SSp-ul", "SSp-ll", "SSp-un"],
    "VIS": ["VISa", "VISal", "VISli", "VISp", "VISpm", "VISam", "VISpor", "VISpl", "VISl", "VISrl"],
    "AUD": ["AUDpo", "AUDd", "AUDp"], "EPd": ["EPd"],
    "TH": ["RT", "VPM", "LP", "LGv", "LD", "VPL", "Eth", "PO", "LGd-co"],
}
AREA2PARENT = {a: p for p, areas in PARENT.items() for a in areas}
# isocortical areas, whose spikes enter the sleep-like detection ("all cortical spikes")
CORTICAL = set(PARENT["PFC"] + PARENT["MO"] + PARENT["SS"] + PARENT["VIS"] + PARENT["AUD"]) | {
    "MOs", "SSp", "AUDv", "VISC", "GU", "AIp", "RSPv", "RSPd", "RSPagl", "PTLp", "TEa", "ECT", "PERI"}
NUMBERED = {"CA1", "CA2", "CA3"}

# code, config/datatables/allrecs_allprobes.xlsx, column quietdet_src: probes whose sleep-like
# periods are taken from another probe of the same session, and probes not checked.
QUIET_FROM_OTHER = {
    "PL062_20200420-probe0": "probe1", "PL064_20200422-probe0": "probe1",
    "PL079_20230621-probe1": "probe0", "PL081_20230621-probe1": "probe0",
    "PL082_20230912-probe0": "probe1", "PL027_20190511-probe1": "probe0",
    "PL028_20190517-probe1": "probe0", "PL030_20190518-probe1": "probe0",
    "PL031_20190524-probe1": "probe0", "PL032_20190524-probe1": "probe0",
    "PL051_20191121-probe1": "probe0", "PL062_20200420-probe2": "probe1",
    "PL055_20200302-probe1": "probe0", "PL056_20200303-probe1": "probe0",
    "PL057_20200203-probe1": "probe0", "PL080_20230621-probe1": "probe0",
    "PL081_20230620-probe1": "probe0", "PL082_20230911-probe1": "probe0",
}
QUIET_IGNORE = {"711179_20230907-probe0", "708078_20231002-probe0", "708078_20231002-probe1",
                "708078_20231003-probe0"}

EPOCH = 3.0          # s, Methods
MIN_SPIKES = 6       # Methods
MIN_EPOCHS = 12      # Methods
NW_MAX, WW_MIN = 0.38, 0.43  # ms, Methods


def dec(v):
    return v.decode() if isinstance(v, bytes) else v


# The other dandiset the paper names for dataset KI (Data availability); used for counts only.
OTHER_DANDISET, OTHER_VERSION = "000473", "0.230417.1502"


def list_assets(dandiset=DANDISET, version=VERSION):
    url = f"{API}/dandisets/{dandiset}/versions/{version}/assets/?page_size=200"
    out = []
    while url:
        r = requests.get(url).json()
        out += r["results"]
        url = r["next"]
    return out


def version_metadata(dandiset=DANDISET, version=VERSION):
    return requests.get(f"{API}/dandisets/{dandiset}/versions/{version}/").json()


def s3_url(asset_id):
    return requests.head(f"{API}/assets/{asset_id}/download/", allow_redirects=True).url


def open_asset(asset_id):
    return h5py.File(remfile.File(s3_url(asset_id)), "r")


def split_area_layer(loc):
    """code settings.py decompose_area_layer"""
    m = re.search(r"\d", loc)
    if loc in NUMBERED or m is None:
        return loc, "NA"
    return loc[: m.start()], loc[m.start():]


def setting_from_metadata(desc, keywords):
    """Behavioral setting from the session description and keywords, named as the code names it."""
    d = desc.lower()
    if "aversive" in d:
        return "Aversion"
    if "detection" in d:
        return "Detection"
    if "contextual" in d:
        return "Context"
    if "working memory" in d:
        return "Attention"
    if "Optotagging" in keywords:
        return "Opto"
    return "Passive"


STIMS = {"Context": ["AudStim_10kHz"], "Opto": ["AudStim_10kHz"], "Detection": ["AudStim_10kHz"],
         "Aversion": ["AudStim_10kHz", "passive_bluenoise"]}


def onset_times(f, setting):
    pres = f["stimulus/presentation"]
    if setting == "Attention":
        return np.sort(f["intervals/trials/start_time"][:])
    names = list(pres.keys()) if setting == "Passive" else [n for n in STIMS[setting] if n in pres]
    return np.sort(np.concatenate([pres[n]["timestamps"][:] for n in names]))


def tone_times(f):
    """10-kHz tone onsets (Methods: 10-kHz pure tones), None when a file has no such series."""
    pres = f["stimulus/presentation"]
    for n in ["AudStim_10kHz", "passive_10kHz"]:
        if n in pres:
            return np.sort(pres[n]["timestamps"][:])
    return None


def intervals(f, start, stop):
    if start not in f or stop not in f:
        return np.empty((0, 2))
    a, b = f[start]["timestamps"][:], f[stop]["timestamps"][:]
    ok = np.isfinite(a) & np.isfinite(b)
    return np.c_[a[ok], b[ok]]


def overlaps(ep, iv, pad=0.0):
    """for each epoch [s, e], whether it overlaps any interval of iv widened by pad."""
    if len(iv) == 0:
        return np.zeros(len(ep), bool)
    iv = iv[np.argsort(iv[:, 0])]
    lo, hi = iv[:, 0] - pad, iv[:, 1] + pad
    cmax = np.maximum.accumulate(hi)
    k = np.searchsorted(lo, ep[:, 1], side="left") - 1  # last interval starting before epoch end
    out = np.zeros(len(ep), bool)
    ok = k >= 0
    out[ok] = cmax[k[ok]] > ep[ok, 0]
    return out


def epoch_metrics(st, idx_end, ep):
    """Per unit and epoch: spike count, burstiness B and memory M (NaN below 6 spikes).

    st: concatenated spike times, idx_end: spike_times_index, ep: (n, 2) epochs."""
    nu, ne = len(idx_end), len(ep)
    cnt = np.zeros((nu, ne), np.int32)
    B = np.full((nu, ne), np.nan, np.float32)
    M = np.full((nu, ne), np.nan, np.float32)
    start = 0
    for u in range(nu):
        s = np.sort(st[start: idx_end[u]])
        start = idx_end[u]
        i0 = np.searchsorted(s, ep[:, 0])
        i1 = np.searchsorted(s, ep[:, 1])
        n = i1 - i0
        cnt[u] = n
        if len(s) < 2:
            continue
        isi = np.diff(s)
        c1 = np.r_[0, np.cumsum(isi)]
        c2 = np.r_[0, np.cumsum(isi ** 2)]
        x, y = isi[:-1], isi[1:]
        cx, cy = np.r_[0, np.cumsum(x)], np.r_[0, np.cumsum(y)]
        cxx, cyy, cxy = np.r_[0, np.cumsum(x * x)], np.r_[0, np.cumsum(y * y)], np.r_[0, np.cumsum(x * y)]
        ok = n >= MIN_SPIKES
        a, b = i0[ok], i1[ok] - 1          # ISIs a .. b-1 lie inside the epoch
        k = (b - a).astype(float)
        mu = (c1[b] - c1[a]) / k
        sd = np.sqrt(np.maximum((c2[b] - c2[a]) / k - mu ** 2, 0))
        B[u, ok] = (sd - mu) / (sd + mu)
        pb = b - 1                         # pairs a .. b-2
        kp = (pb - a).astype(float)
        sx, sy = cx[pb] - cx[a], cy[pb] - cy[a]
        sxx, syy, sxy = cxx[pb] - cxx[a], cyy[pb] - cyy[a], cxy[pb] - cxy[a]
        cov = sxy / kp - sx * sy / kp ** 2
        vx, vy = sxx / kp - (sx / kp) ** 2, syy / kp - (sy / kp) ** 2
        with np.errstate(invalid="ignore", divide="ignore"):
            r = cov / np.sqrt(vx * vy)
        r[(vx <= 1e-15) | (vy <= 1e-15)] = np.nan
        M[u, ok] = r
    return cnt, B, M


def offperiod_sleep(st_cortical, n_units, t0, t1, binw=0.01):
    """Sleep-like periods from the pooled spikes of cortical units (Methods)."""
    if n_units == 0 or len(st_cortical) == 0:
        return np.empty((0, 2))
    edges = np.arange(t0, t1 + binw, binw)
    fr = np.histogram(st_cortical, edges)[0] / n_units / binw
    frs = savgol_filter(fr.astype(float), 11, 3)
    pos = frs[frs > 0]
    gmean = np.exp(np.mean(np.log(pos)))
    thr = 0.2 * gmean
    below = frs < thr
    # troughs: runs below thr longer than 5 ms (any run of >= 1 bin of 10 ms)
    above_g = frs >= gmean
    d = np.diff(np.r_[0, below.astype(int), 0])
    a_idx, b_idx = np.where(d == 1)[0], np.where(d == -1)[0]
    if len(a_idx) == 0:
        return np.empty((0, 2))
    # extend each trough backward and forward to where FR reaches the geometric mean
    n = len(frs)
    ii = np.arange(n)
    last_above = np.maximum.accumulate(np.where(above_g, ii, -1))
    next_above = np.minimum.accumulate(np.where(above_g, ii, n)[::-1])[::-1]
    lo = last_above[a_idx] + 1
    hi = next_above[np.minimum(b_idx, n - 1)]
    hi = np.where(b_idx >= n, n, hi)
    offs = list(zip(edges[lo], edges[np.minimum(hi, n)]))
    offs = np.array(sorted(set(offs)))
    # merge off periods closer than 1.5 s
    groups = [[offs[0][0], offs[0][1], 1]]
    for a, b in offs[1:]:
        if a - groups[-1][1] < 1.5:
            groups[-1][1] = max(groups[-1][1], b)
            groups[-1][2] += 1
        else:
            groups.append([a, b, 1])
    out = np.array([[a - (1.0 if n > 1 else 0.3), b + (1.0 if n > 1 else 0.3)] for a, b, n in groups])
    # merge overlapping padded periods
    res = [list(out[0])]
    for a, b in out[1:]:
        if a <= res[-1][1]:
            res[-1][1] = max(res[-1][1], b)
        else:
            res.append([a, b])
    return np.array(res)


def offperiod_sleep_code(st_cortical, n_units, t0, t1, binw=0.01):
    """Variant: the code's detector (utils/statedet_helpers.py get_detdict with
    config/config_statedet/offdetection_defaultparams.yaml): off periods are runs below the
    geometric mean whose minimum is at most 0.2 of it, lasting more than 50 ms (mindur_trough
    0.05 s, where the Methods say 5 ms) and at most 0.6 s (maxdur_off); merged within 1.5 s;
    groups of at least 3 off periods padded by 1 s, others by 0.3 s; free gaps of 1.5 s or less
    filled. The Savitzky-Golay output is clipped at 0."""
    if n_units == 0 or len(st_cortical) == 0:
        return np.empty((0, 2))
    edges = np.arange(0, t1, binw)
    fr = np.histogram(st_cortical, edges)[0] / n_units / binw
    v = np.clip(savgol_filter(fr.astype(float), 11, 3), 0, None)
    gm = np.exp(np.mean(np.log(v[v > 0])))
    sg = np.diff(np.sign(v - gm))
    starts0, stops0 = np.where(sg < 0)[0], np.where(sg > 0)[0]
    if len(starts0) == 0 or len(stops0) == 0:
        return np.empty((0, 2))
    stops = stops0[stops0 > starts0[0]]
    starts = starts0[starts0 < stops0[-1]]
    ci = np.c_[starts, stops]
    mins = np.array([v[a:b].min() for a, b in ci])
    dur = ci[:, 1] - ci[:, 0]
    tr = ci[(mins <= 0.2 * gm) & (dur > 5) & (dur <= 60)]
    if len(tr) == 0:
        return np.empty((0, 2))
    # merge within 1.5 s (150 points)
    gaps = tr[1:, 0] - tr[:-1, 1]
    si = np.r_[0, np.where(gaps >= 150)[0] + 1]
    ei = np.r_[np.where(gaps >= 150)[0], len(tr) - 1]
    sb = np.c_[tr[si, 0], tr[ei, 1]]
    nev = ei - si + 1
    pad = np.where(nev >= 3, 100, 30)
    bm = np.c_[sb[:, 0] - pad, sb[:, 1] + pad]
    # merge overlapping, then fill free gaps of 1.5 s or less
    res = [list(bm[0])]
    for a, b in bm[1:]:
        if a - res[-1][1] <= 150:
            res[-1][1] = max(res[-1][1], b)
        else:
            res.append([a, b])
    return np.array(res) * binw


def blocks_for(f, onsets):
    """Block index of each epoch (Methods, Stability analyses). Inherent blocks are runs of the
    trials table's Block column, matched to each onset by the nearest trial start; runs of more
    than 75 epochs are split in two. When the column is constant or alternates (median run below
    20 epochs) the epochs are cut into consecutive blocks of 50. Assumption, see the notebook."""
    tr = f["intervals/trials"]
    blk = None
    if "Block" in tr:
        bv = tr["Block"][:].astype(float)
        ts = tr["start_time"][:]
        j = np.clip(np.searchsorted(ts, onsets), 1, len(ts) - 1)
        j = np.where(np.abs(ts[j - 1] - onsets) < np.abs(ts[j] - onsets), j - 1, j)
        v = bv[j]
        run = np.r_[0, np.cumsum(np.diff(v) != 0)]
        lens = np.bincount(run)
        if len(lens) > 1 and np.median(lens) >= 20:
            blk = []
            nb = 0
            for r in range(len(lens)):
                n = lens[r]
                if n > 75:
                    h = n // 2
                    blk += [nb] * h + [nb + 1] * (n - h)
                    nb += 2
                else:
                    blk += [nb] * n
                    nb += 1
            return np.array(blk), "inherent"
    return np.arange(len(onsets)) // 50, "fifty"


def load_file(asset):
    """Read one NWB file and reduce it to what the analyses use."""
    f = open_asset(asset["asset_id"])
    sess = dec(f["general/session_id"][()])
    desc = dec(f["session_description"][()])
    kw = [dec(k) for k in f["general/keywords"][:]]
    setting = setting_from_metadata(desc, kw)
    subj = dec(f["general/subject/subject_id"][()]).split("_")[0]
    e = f["general/extracellular_ephys/electrodes"]
    loc = np.array([dec(x) for x in e["location"][:]])
    ap, dv, ml = e["AP"][:], e["DV"][:], e["ML"][:]
    u = f["units"]
    el = u["electrodes"][:]
    q = u["quality"][:]
    units = pd.DataFrame({
        "session": sess, "subject": subj, "setting": setting, "unit_id": u["id"][:],
        "ptt": u["Peak_to_Trough"][:], "location": loc[el], "AP": ap[el], "DV": dv[el], "ML": ml[el],
        "q_isi": q[:, 0], "q_fp": q[:, 1],
    })
    al = units.location.map(split_area_layer)
    units["area"] = [a for a, _ in al]
    units["layer"] = [l for _, l in al]
    st = u["spike_times"][:]
    idx = u["spike_times_index"][:].astype(np.int64)
    units["n_spikes"] = np.diff(np.r_[0, idx])
    t0, t1 = float(np.nanmin(st)), float(np.nanmax(st))
    onsets = onset_times(f, setting)
    ep = np.c_[onsets - EPOCH, onsets]
    lick = intervals(f, "processing/behavior/LickOnset/lick_onset_data",
                     "processing/behavior/LickOffset/lick_offset_data")
    sat = intervals(f, "analysis/spike saturation start", "analysis/spike saturation stop")
    cnt, B, M = epoch_metrics(st, idx, ep)
    # cortical spikes for the sleep-like detection
    cort = units.area.isin(CORTICAL).values
    starts = np.r_[0, idx[:-1]]
    cst = np.concatenate([st[a:b] for a, b, c in zip(starts, idx, cort) if c]) if cort.any() else np.empty(0)
    sleep = offperiod_sleep(np.sort(cst), int(cort.sum()), t0, t1)
    sleep_code = offperiod_sleep_code(np.sort(cst), int(cort.sum()), t0, t1)
    blk, blkmode = blocks_for(f, onsets)
    tones = tone_times(f)
    out = dict(path=asset["path"], session=sess, subject=subj, setting=setting, desc=desc,
               units=units, onsets=onsets, epochs=ep, lick=lick, sat=sat, cnt=cnt, B=B, M=M,
               sleep_own=sleep, sleep_own_code=sleep_code, n_cortical=int(cort.sum()), t0=t0, t1=t1, blocks=blk,
               blockmode=blkmode, tones=tones, asset_id=asset["asset_id"],
               n_trials=len(f["intervals/trials/start_time"]))
    f.close()
    return out


PSTH_BIN = 0.0005  # s, Methods (0.5 ms)
PRE, POST = 2.0, 0.7


def tone_counts(st, idx, tones):
    """Spike times relative to each tone, as per-unit histograms of 0.5-ms bins over [-2, 0.7] s,
    one row per tone epoch kept as a sparse list (unit, tone, bin)."""
    edges = np.arange(-PRE, POST + PSTH_BIN / 2, PSTH_BIN)
    nb = len(edges) - 1
    out = []
    start = 0
    for u in range(len(idx)):
        s = np.sort(st[start: idx[u]])
        start = idx[u]
        i0 = np.searchsorted(s, tones - PRE)
        i1 = np.searchsorted(s, tones + POST)
        rows = []
        for k in range(len(tones)):
            if i1[k] > i0[k]:
                b = ((s[i0[k]:i1[k]] - tones[k] + PRE) / PSTH_BIN).astype(int)
                b = b[(b >= 0) & (b < nb)]
                rows.append(np.c_[np.full(len(b), k), b])
        out.append(np.vstack(rows).astype(np.int32) if rows else np.empty((0, 2), np.int32))
    return out


def load_all(assets, workers=12):
    with ThreadPoolExecutor(workers) as ex:
        recs = list(ex.map(load_file, assets))
    return sorted(recs, key=lambda r: r["path"])


def classify_epochs(recs, detector="methods"):
    """Adds to each record its sleep-like periods (own or from the probe the code's table names)
    and the epoch states: 'active', 'sleep', 'near_sleep' (within 1 s of a sleep-like period) or
    'excluded' (licking or saturation). detector 'methods' (main) or 'code' (variant)."""
    key = "sleep_own" if detector == "methods" else "sleep_own_code"
    by_sess = {r["session"]: r for r in recs}
    for r in recs:
        sid = r["session"]
        if sid in QUIET_IGNORE:
            r["sleep"] = None
        elif sid in QUIET_FROM_OTHER:
            other = sid.rsplit("-", 1)[0] + "-" + QUIET_FROM_OTHER[sid]
            r["sleep"] = by_sess[other][key] if other in by_sess else r[key]
        else:
            r["sleep"] = r[key]
        ep = r["epochs"]
        bad = overlaps(ep, r["lick"]) | overlaps(ep, r["sat"])
        if r["sleep"] is None or len(r["sleep"]) == 0:
            sl = np.zeros(len(ep), bool)
            near = np.zeros(len(ep), bool)
        else:
            sl = overlaps(ep, r["sleep"])
            near = overlaps(ep, r["sleep"], pad=1.0)
        state = np.where(bad, "excluded", np.where(sl, "sleep", np.where(near, "near_sleep", "active")))
        r["state"] = state
    return recs


def unit_metrics(r, mask):
    """Mean metrics over the epochs in mask; returns DataFrame with n_valid (epochs >= 6 spikes)."""
    cnt, B, M = r["cnt"][:, mask], r["B"][:, mask], r["M"][:, mask]
    with np.errstate(divide="ignore", invalid="ignore"):
        lfr = np.where(cnt > 0, np.log10(cnt / EPOCH), np.nan)
        out = pd.DataFrame({
            "log10FR": np.nanmean(lfr, axis=1) if lfr.shape[1] else np.nan,
            "B": np.nanmean(B, axis=1) if B.shape[1] else np.nan,
            "M": np.nanmean(M, axis=1) if M.shape[1] else np.nan,
            "n_valid": (cnt >= MIN_SPIKES).sum(axis=1),
            "n_epochs": mask.sum(),
        })
    return out


def unit_table(recs):
    rows = []
    for r in recs:
        u = r["units"].copy()
        act = unit_metrics(r, r["state"] == "active")
        slp = unit_metrics(r, r["state"] == "sleep")
        for c in act:
            u[c] = act[c].values
            u[c + "_sleep"] = slp[c].values
        rows.append(u)
    U = pd.concat(rows, ignore_index=True)
    U["utype"] = np.where(U.ptt < NW_MAX, "nw", np.where(U.ptt > WW_MIN, "ww", "na"))
    U["parent"] = U.area.map(AREA2PARENT).fillna("other")
    U["is_pfc"] = U.area.isin(PFC_SUBREGIONS)
    U["deep"] = U.layer.str.contains("5|6")
    U["cortical"] = U.area.isin(CORTICAL)
    # region unit for enrichment: PFC subregions, other areas by parent (code parent_dict)
    U["region"] = np.where(U.is_pfc, U.area, U.parent)
    return U


# ---------------------------------------------------------------- SOM
def hex_coords(nx, ny):
    """code utils/my_somz.py geometry('hex'): node k = jj*nx + ii."""
    dy = 0.8660254
    xs, ys = [], []
    for jj in range(ny):
        for ii in range(nx):
            xs.append(ii + (0.5 if jj % 2 == 1 else 0.0))
            ys.append(jj * dy)
    return np.c_[xs, ys]


def kshape(X, nnodes):
    """code utils/som_helpers.py get_kshape"""
    ev = np.sort(np.linalg.eigvalsh(np.cov(X.T)))
    er = ev[-2] / ev[-1]
    x = np.sqrt(nnodes / er)
    return int(np.ceil(x * er)), int(np.ceil(x))


def pca_init(X, rows, cols):
    """code utils/som_helpers.py getInitialMap_pca (exact PCA in place of randomized PCA)."""
    n = rows * cols
    coord = np.c_[np.arange(n) // cols, np.arange(n) % cols].astype(float)
    coord = (coord - coord.min(0)) / (coord.max(0) - coord.min(0))
    coord = (coord - 0.5) * 2
    me = X.mean(0)
    Xc = X - me
    w, V = np.linalg.eigh(np.cov(Xc.T))
    order = np.argsort(w)[::-1][:2]
    eigvec = V[:, order].T * w[order][:, None]  # unit eigenvectors scaled by eigenvalue
    return me + coord @ eigvec  # (n, d)


def train_som(X, nnodes, niter=200):
    """Batch SOM as code utils/my_somz.py (batch branch). X standardized (n, d)."""
    nx, ny = kshape(X, nnodes)
    pos = hex_coords(nx, ny)
    D = np.sqrt(((pos[:, None, :] - pos[None, :, :]) ** 2).sum(-1))
    W = pca_init(X, ny, nx)
    s0, sf = D.max(), D[D > 0].min()
    for it in range(niter):
        sigma = s0 * (sf / s0) ** (it / niter)
        bmu = bmus(X, W)
        H = np.exp(-(D[bmu] ** 2) / sigma ** 2)  # (n, nodes)
        W = (H.T @ X) / H.sum(0)[:, None]
    return dict(W=W, pos=pos, shape=(nx, ny), D=D)


def bmus(X, W):
    d = (X ** 2).sum(1)[:, None] - 2 * X @ W.T + (W ** 2).sum(1)[None, :]
    return np.argmin(d, axis=1)


def ward_clusters(W, k):
    from scipy.cluster.hierarchy import fcluster, linkage
    Z = (W - W.mean(0)) / W.std(0)
    return fcluster(linkage(Z, method="ward"), k, "maxclust") - 1


# ---------------------------------------------------------------- enrichment
def escore(pop, attr, group, n_shuffle=1000, seed=0, pops=None, attrs=None):
    """E-scores (Methods, equation 5): counts of attribute in population against counts after
    shuffling the population labels within each group. Returns E, P, counts (pops x attrs)."""
    rng = np.random.default_rng(seed)
    pops = np.array(sorted(pd.unique(pop))) if pops is None else np.asarray(pops)
    attrs = np.array(sorted(pd.unique(attr))) if attrs is None else np.asarray(attrs)
    pi = pd.Index(pops).get_indexer(pop)
    ai = pd.Index(attrs).get_indexer(attr)
    keep = (pi >= 0) & (ai >= 0)
    pi, ai, g = pi[keep], ai[keep], np.asarray(group)[keep]
    npop, nat = len(pops), len(attrs)
    X = np.bincount(pi * nat + ai, minlength=npop * nat).reshape(npop, nat)
    gidx = [np.where(g == gv)[0] for gv in pd.unique(g)]
    S = np.zeros((n_shuffle, npop, nat), np.int32)
    for s in range(n_shuffle):
        pp = pi.copy()
        for ix in gidx:
            pp[ix] = pp[ix][rng.permutation(len(ix))]
        S[s] = np.bincount(pp * nat + ai, minlength=npop * nat).reshape(npop, nat)
    mu, sd = S.mean(0), S.std(0)
    with np.errstate(invalid="ignore", divide="ignore"):
        E = (X - mu) / sd
    fm, fp = (S < X[None]).mean(0), (S > X[None]).mean(0)
    P = 1 - np.maximum(fm, fp)
    return (pd.DataFrame(E, pops, attrs), pd.DataFrame(P, pops, attrs), pd.DataFrame(X, pops, attrs))


# ---------------------------------------------------------------- categories
# code SOM/clusterSOM/relabel_clusters.py label_sorter (8 ww and 5 nw clusters), applied to Ward
# clusters first ranked by decreasing median memory of their node prototypes (cluster_SOM.py).
CODE_SORTER = {8: np.array([4, 1, 6, 2, 3, 7, 8, 5]) - 1, 5: np.array([1, 2, 4, 5, 3]) - 1}


def category_maps(W, lab, mu, sd, k):
    """Category number (1..k) of each Ward cluster under the two readings of G2.

    (a) the code's: clusters ranked by decreasing median memory of their (standardized)
        prototypes, then the code's fixed permutation.
    (b) matching the text's descriptions (ww only): the three clusters with the highest median
        log10FR are 4 to 6 in order of increasing median B; of the other five, the three with
        the lowest median B are 1 to 3 and the other two 7 and 8, each in order of increasing B.
        For nw (5 clusters) reading (b) is not defined by the text and returns None."""
    Wd = W * sd + mu
    med = pd.DataFrame({c: [np.median(Wd[lab == c, j]) for c in range(k)] for j, c in
                        zip(range(3), ["log10FR", "B", "M"])})
    rank = (-np.array([np.median(W[lab == c, 2]) for c in range(k)])).argsort().argsort()
    a = np.zeros(k, int)
    for new, old in enumerate(CODE_SORTER[k]):
        a[np.where(rank == old)[0][0]] = new + 1
    b = None
    if k == 8:
        b = np.zeros(k, int)
        hi = np.argsort(med.log10FR.values)[-3:]
        lo = np.argsort(med.log10FR.values)[:5]
        for i, c in enumerate(hi[np.argsort(med.B.values[hi])]):
            b[c] = 4 + i
        lob = lo[np.argsort(med.B.values[lo])]
        for i, c in enumerate(lob):
            b[c] = [1, 2, 3, 7, 8][i]
    med["n_nodes"] = np.bincount(lab, minlength=k)
    return a, b, med


def fit_categories(units, nnodes, k):
    """Standardize, train the SOM, cluster its nodes; returns a dict with everything."""
    F = ["log10FR", "B", "M"]
    X = units[F].values
    mu, sd = X.mean(0), X.std(0)
    Z = (X - mu) / sd
    som = train_som(Z, nnodes)
    lab = ward_clusters(som["W"], k)
    a, b, med = category_maps(som["W"], lab, mu, sd, k)
    node = bmus(Z, som["W"])
    return dict(som=som, mu=mu, sd=sd, lab=lab, map_a=a, map_b=b, med=med, node=node,
                cat_a=a[lab[node]], cat_b=None if b is None else b[lab[node]])


# ---------------------------------------------------------------- stability
def block_categories(recs, units, fit, min_valid=MIN_EPOCHS):
    """Per unit and block: metrics over the block's active epochs, standardized to the full-data
    SOM, and the block's category under both readings (Methods, Stability analyses)."""
    rows = []
    key = units.set_index(["session", "unit_id"]).index
    for r in recs:
        u = r["units"]
        sel = key.get_indexer(pd.MultiIndex.from_arrays([u.session, u.unit_id]))
        for b in np.unique(r["blocks"]):
            m = (r["state"] == "active") & (r["blocks"] == b)
            if m.sum() == 0:
                continue
            met = unit_metrics(r, m)
            ok = (sel >= 0) & (met.n_valid.values >= min_valid) & met[["log10FR", "B", "M"]].notna().all(1).values
            if not ok.any():
                continue
            Z = (met.loc[ok, ["log10FR", "B", "M"]].values - fit["mu"]) / fit["sd"]
            node = bmus(Z, fit["som"]["W"])
            cl = fit["lab"][node]
            rows.append(pd.DataFrame({"session": r["session"], "unit_id": u.unit_id.values[ok], "block": b,
                                      "cat_a": fit["map_a"][cl],
                                      "cat_b": fit["map_b"][cl] if fit["map_b"] is not None else 0,
                                      "n_epochs": met.n_valid.values[ok]}))
    return pd.concat(rows, ignore_index=True)


def transitions(bc, cat, k):
    """Transition count matrices M_t (t = 1 for block 1 to block 2, ...) summed over units;
    a transition is counted between consecutive blocks of a recording where the unit has both."""
    Ms = {}
    for (s, u), g in bc.sort_values("block").groupby(["session", "unit_id"]):
        bl, c = g.block.values, g[cat].values
        for i in range(len(bl) - 1):
            if bl[i + 1] == bl[i] + 1:
                t = int(bl[i]) + 1
                Ms.setdefault(t, np.zeros((k, k), int))[c[i] - 1, c[i + 1] - 1] += 1
    return dict(sorted(Ms.items()))


def stability(M):
    n = M.sum()
    E = np.outer(M.sum(1), M.sum(0)) / n
    return np.trace(M) / n, np.trace(E) / n


def coincidence(M):
    """Methods, equation 4."""
    n = M.sum()
    R, C = M.sum(1), M.sum(0)
    E = np.outer(R, C) / n
    X = np.where(M >= E, (M - E) / (np.minimum(R[:, None], C[None, :]) - E), (M - E) / E)
    return X


# ---------------------------------------------------------------- statistics
def mixed(df, formula, group="subject"):
    """Linear mixed model with a random intercept per mouse (statsmodels MixedLM, REML).
    Returns the fit and the marginal R2 (Nakagawa and Schielzeth): variance of the fixed-effect
    prediction over itself plus the random-intercept and residual variances."""
    import warnings

    import statsmodels.formula.api as smf
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        fit = smf.mixedlm(formula, df, groups=df[group]).fit(reml=True)
    fe = fit.model.exog @ fit.fe_params.values
    vf = np.var(fe)
    r2m = vf / (vf + float(fit.cov_re.iloc[0, 0]) + fit.scale)
    return fit, r2m


def gradient_angle(pos, v1, v2):
    """Angle (degrees) between the directions of steepest increase of two node values, from a
    linear fit of each on the node coordinates."""
    A = np.c_[pos, np.ones(len(pos))]
    g1 = np.linalg.lstsq(A, v1, rcond=None)[0][:2]
    g2 = np.linalg.lstsq(A, v2, rcond=None)[0][:2]
    c = g1 @ g2 / np.linalg.norm(g1) / np.linalg.norm(g2)
    return float(np.degrees(np.arccos(np.clip(c, -1, 1)))), g1, g2


# ---------------------------------------------------------------- outside inputs
ZENODO_RECORD = "14205018"  # doi:10.5281/zenodo.14205018, the paper's intermediate files


def zenodo_bytes(name):
    r = requests.get(f"https://zenodo.org/api/records/{ZENODO_RECORD}/files/{name}/content")
    r.raise_for_status()
    return r.content


def paper_unit_table():
    """The paper's per-unit metrics files (Zenodo metrics_files.zip, dataset KI): recording,
    unit id, flatmap (U, V), location, quality flags and ww/nw labels."""
    import io
    import zipfile
    z = zipfile.ZipFile(io.BytesIO(zenodo_bytes("metrics_files.zip")))
    rows = []
    for n in z.namelist():
        if "metric_files_Carlen/metrics_" not in n or not n.endswith(".h5") or "MACOSX" in n:
            continue
        rec = n.split("metrics_")[-1][:-3]
        with h5py.File(io.BytesIO(z.read(n)), "r") as f:
            rows.append(pd.DataFrame({
                "session": rec, "unit_id": f["uids"][:], "U": f["anatomy/U"][:], "V": f["anatomy/V"][:],
                "z_location": [dec(x) for x in f["anatomy/location"][:]],
                "z_quality": f["quality/quality"][:], "z_wquality": f["waveform_metrics/waveform_quality"][:],
                "z_ww": f["unit_type/ww"][:], "z_nw": f["unit_type/nw"][:],
                "z_p2t_ms": f["waveform_metrics/peak2Trough"][:] * 1000, "z_task": dec(f["Task"][()])}))
    return pd.concat(rows, ignore_index=True)


def harris_table():
    """Harris et al. 2019 hierarchy scores as the code reads them (connectivity_correlations/
    harris_vs_enrichment.py: sheet hierarchy_all_regions, column 'CC+TC+CT iterated', cortex rows;
    AId, AIp, AIv are spelled Aid, Aip, Aiv in the table)."""
    import io
    df = pd.read_excel(io.BytesIO(zenodo_bytes("hierarchy_summary_CreConf.xlsx")), sheet_name="hierarchy_all_regions")
    df = df[df["CortexThalamus"] == "C"]
    ren = {"Aid": "AId", "Aip": "AIp", "Aiv": "AIv"}
    return pd.Series(df["CC+TC+CT iterated"].values, index=[ren.get(a, a) for a in df["areas"]])


def flatmap_polygons(name):
    """Polygons from the Zenodo flatmaps.zip: 'flatmap_PFCregions.h5' (subregions),
    'flatmap_PFCrois.h5' (the 60 GaoROIs), 'flatmap_PFC_ntesselated_obeyRegions_res200.h5'
    (the paper's dataROIs)."""
    import io
    import zipfile
    z = zipfile.ZipFile(io.BytesIO(zenodo_bytes("flatmaps.zip")))
    with h5py.File(io.BytesIO(z.read("flatmaps/" + name)), "r") as f:
        return {k: f[k][()] for k in f.keys()}


def gao_hierarchy():
    import io
    t = pd.read_csv(io.BytesIO(zenodo_bytes("ROI_Gao_hierarchy_index.csv")))
    return pd.Series(t["hierarchy index"].values, index=t["roi"].astype(int))


def in_polygons(uv, polys):
    """Name of the polygon containing each point (first match), or None."""
    import shapely
    out = np.array([None] * len(uv), dtype=object)
    pts = [shapely.Point(p) for p in uv]
    for k, c in polys.items():
        pg = shapely.Polygon(c)
        m = np.array([pg.contains(p) for p in pts])
        out[(out == None) & m] = k  # noqa: E711
    return out


def parcellate(uv, region, per=200, bounds=(160, 240), seed=0):
    """Methods, Parcellation into ROIs of similar unit count: n = int(count / 200) ROIs per
    subregion by constrained k-means of the flatmap positions, FRP not split; a subregion with no
    more units than the upper bound is one ROI, and the upper bound is raised when n ROIs cannot
    hold the units (code utils/tessellation_tools.py get_clusters). Units take the ROI of the
    nearest cluster center in their subregion (the Voronoi cell). Returns ROI labels."""
    from k_means_constrained import KMeansConstrained
    lab = np.array([None] * len(uv), dtype=object)
    for reg in pd.unique(region):
        idx = np.where(region == reg)[0]
        X = uv[idx]
        n = int(len(X) / per)
        lo, hi = bounds
        if reg == "FRP" or len(X) <= hi or n <= 1:
            lab[idx] = f"{reg}-1"
            continue
        if n * hi < len(X):
            hi = int(np.ceil(len(X) / n))
        km = KMeansConstrained(n_clusters=n, size_min=lo, size_max=hi, random_state=seed).fit(X)
        d = ((X[:, None, :] - km.cluster_centers_[None]) ** 2).sum(-1)
        lab[idx] = [f"{reg}-{k + 1}" for k in d.argmin(1)]
    return lab


# ---------------------------------------------------------------- tone responses
def tone_epoch_ok(r):
    """Tone response epochs [-2, 0.7] s around 10-kHz tones, dropping those with licking,
    sleep-like periods or spike-band saturation (Methods, Epoch selection)."""
    t = r["tones"]
    ep = np.c_[t - PRE, t + POST]
    bad = overlaps(ep, r["lick"]) | overlaps(ep, r["sat"])
    if r["sleep"] is not None and len(r["sleep"]):
        bad |= overlaps(ep, r["sleep"])
    return ~bad


def tone_traces(r):
    """Per unit: smoothed PSTH (0.5-ms bins, Gaussian kernel s.d. 10 ms over an 80-ms window),
    overall and prestimulus rates, z-scored trace 0 to 0.65 s (Methods, Extraction of PSTHs).
    Also returns the relative spike times of each unit (for the ZETA test)."""
    ok = tone_epoch_ok(r)
    tones = r["tones"][ok]
    f = open_asset(r["asset_id"])
    st = f["units/spike_times"][:]
    idx = f["units/spike_times_index"][:].astype(np.int64)
    f.close()
    edges = np.arange(-PRE, POST + PSTH_BIN / 2, PSTH_BIN)
    nb = len(edges) - 1
    x = np.arange(-80, 81) * PSTH_BIN
    ker = np.exp(-0.5 * (x / 0.01) ** 2)
    ker /= ker.sum()
    pre = edges[:-1] < 0
    post = (edges[:-1] >= 0) & (edges[:-1] < 0.65 - 1e-9)
    out = np.full((len(idx), int(post.sum())), np.nan, np.float32)
    rate_all = np.zeros(len(idx))
    rate_pre = np.zeros(len(idx))
    start = 0
    for u in range(len(idx)):
        s = np.sort(st[start: idx[u]])
        start = idx[u]
        if len(tones) == 0:
            continue
        i0 = np.searchsorted(s, tones - PRE)
        i1 = np.searchsorted(s, tones + POST)
        n = i1 - i0
        if n.sum() == 0:
            continue
        rep = np.repeat(np.arange(len(tones)), n)
        pos = np.concatenate([np.arange(a, b) for a, b in zip(i0, i1) if b > a])
        rel = s[pos] - tones[rep]
        h = np.histogram(rel, edges)[0] / len(tones) / PSTH_BIN
        rate_all[u] = h.mean()
        rate_pre[u] = h[pre].mean()
        sm = np.convolve(h, ker, mode="same")
        mu, sd = sm[pre].mean(), sm[pre].std()
        if sd > 0:
            out[u] = (sm[post] - mu) / sd
    return dict(trace=out, rate_all=rate_all, rate_pre=rate_pre, n_tones=len(tones))


def zeta_unit(args):
    """ZETA test on the 700 ms after tone onset (Methods, ZETA test); zetapy defaults (100
    resamplings), seeded. The onset is the first crossing of half the peak height of the
    instantaneous rate, above its value at the first time point, as older zetapy versions
    computed it (zetapy 4 no longer returns it): a standard choice."""
    import logging

    import zetapy
    logging.getLogger().setLevel(logging.ERROR)
    spikes, tones, seed = args
    np.random.seed(seed)
    if len(spikes) < 3:
        return np.nan, np.nan
    try:
        p, d, rate = zetapy.zetatest(spikes, tones, max_duration=0.7, return_rate=True)
        v, t = np.asarray(rate["rate_vector"]), np.asarray(rate["timestamps"])
        if len(v) < 2:
            return p, np.nan
        k = int(np.argmax(v))
        thr = v[0] + (v[k] - v[0]) / 2
        onset = t[np.argmax(v[: k + 1] >= thr)]
        return p, float(onset)
    except Exception:
        return np.nan, np.nan


def zeta_for(r, unit_ids, seed=0):
    """ZETA p and onset for the given units of one recording, over its kept tone epochs."""
    f = open_asset(r["asset_id"])
    st = f["units/spike_times"][:]
    idx = f["units/spike_times_index"][:].astype(np.int64)
    ids = f["units/id"][:]
    f.close()
    tones = r["tones"][tone_epoch_ok(r)]
    starts = np.r_[0, idx[:-1]]
    pos = pd.Index(ids).get_indexer(unit_ids)
    return [(np.sort(st[starts[i]: idx[i]]), tones, seed + int(ids[i])) for i in pos]


def raster_rois(uv, region, roi, regpolys, step=2.0):
    """Pixels of the PFC flatmap (grid of `step` flatmap units: a standard choice), each given
    the dataROI of the nearest unit-weighted ROI center within its subregion polygon (the
    Voronoi cells of the parcellation). Returns pixel coordinates and ROI labels."""
    import shapely
    allc = np.vstack(list(regpolys.values()))
    xs = np.arange(allc[:, 0].min(), allc[:, 0].max(), step)
    ys = np.arange(allc[:, 1].min(), allc[:, 1].max(), step)
    gx, gy = np.meshgrid(xs, ys)
    gx, gy = gx.ravel(), gy.ravel()
    lab = np.array([None] * len(gx), dtype=object)
    cen = pd.DataFrame({"u": uv[:, 0], "v": uv[:, 1], "roi": roi, "reg": region}).groupby(["reg", "roi"])[["u", "v"]].mean()
    for reg, c in regpolys.items():
        inside = shapely.contains_xy(shapely.Polygon(c), gx, gy)
        if reg not in cen.index.get_level_values(0) or not inside.any():
            continue
        cc = cen.loc[reg]
        d = (gx[inside, None] - cc.u.values[None]) ** 2 + (gy[inside, None] - cc.v.values[None]) ** 2
        lab[inside] = cc.index.values[d.argmin(1)]
    keep = lab != None  # noqa: E711
    return np.c_[gx[keep], gy[keep]], lab[keep]
