"""Loading and measures for the hippocampus and lateral septum recordings of dandiset 000213.

Tingley & Buzsaki (2018), Neuron 98, 1229-1242, doi:10.1016/j.neuron.2018.04.028.

Each NWB file is one session of one rat: sorted units with a brain-region label (`ls`, `hpc`,
`ca3` and a few others), LFP at 1250 Hz, head position, and a trials table (start, stop and, for
the alternation tasks, `direction` and `trial_type`). Files are streamed from the archive at the
pinned version; nothing is written to disk. Only what the analyses need is kept: spike times
inside trials, positions inside trials, and the LFP of two channels inside trials (with 1 s of
padding on each side for filtering). Most files chunk the LFP as 500 samples by all channels, so
reading one channel of a whole session means reading all of it; reading only the trials keeps a
session to tens to hundreds of megabytes.

Where the parameters come from:

- The paper's analysis code: https://github.com/DavidTingley/papers (LS_phasecoding, commit
  9f4cd48a44f211956954558b66d776ccbb74d693), and the buzcode functions it calls,
  https://github.com/buzsakilab/buzcode at commit e615663b2b100782d1f378580f6d7aaa35c12937
  (bz_firingMap1D, bz_phaseMap1D, circ_smoothTS, bz_getPlaceFields1D, and the classifier
  max_correlation_coefficient_CL of the Neural Decoding Toolbox it bundles). The per-cell
  decoder is in DavidTingley/scratch, scratch_07_11_17_spatialBinnedMaxCorr.m, commit
  2f804532290774f52a442bf0f3ec23dd5398d58d.
  * Spike theta phase: 3rd-order Butterworth band-pass 6 to 9 Hz, zero phase, Hilbert angle
    (bz_phaseMap1D).
  * Rate maps: spike counts and occupancy (position samples, 5-bin median filter, floor of 1)
    per trial and position bin; for decoding, both box-smoothed over 20 bins (MATLAB `smooth`,
    which uses 19 for an even span) and divided (bz_firingMap1D `rateMaps_box`).
  * Phase maps: the circular mean of the spike phases in each trial and bin (bz_phaseMap2Bins is
    not public; this is the reading taken here), then a 20-bin circular box mean that ignores
    empty bins and leaves bins with no spike within reach at 0 (circ_smoothTS).
  * Decoder: all trial-by-bin samples of one cell and condition pooled, 10 random 60/40 splits
    of the samples; the template of a bin is the mean training feature of the samples in it,
    and a test sample is assigned the bin whose template is closest (ties broken at random);
    the score is the mean squared error in bins squared. The rate feature is the smoothed rate;
    the phase feature is the cosine of the smoothed phase (`mse_phase_cos`, the one makeFig2.m
    uses). Chance: the same with the test features permuted.
  * Inclusion of a cell and condition: at least 10 trials, and at least 1.5 spikes per trial
    (makeFig2.m; Methods).
  * Place fields (bz_getPlaceFields1D with a 20% threshold, the file name the code loads): the
    trial-mean rate map (5-bin smoothing), RMS-smoothed over 5 bins for peak finding; peaks of
    at least 2 Hz (Methods); peaks whose mean is below the across-trial SD are dropped; the
    field extends while the mean rate is above 20% of the peak; width limits 8 cm and 120 cm
    (Methods), taken here as 5 and 80 bins at the paper's 1.5 cm per bin.
- The Methods: 1250 Hz LFP; CA1 pyramidal layer theta as reference; LFP coherence from 4 to
  12 Hz phases in 150 ms windows moved in 50 ms steps; gamma power as the 50 ms RMS of the 40
  to 200 Hz band.
- Choices made here, where neither fixes them:
  * Position bins: `N_BINS` = 200 per trial, by the fraction of the trial's path length
    covered. The paper's bins are about 1.5 cm on a maze of about 3 m, and its Figure 6E has
    200 bins; its linearization template (behavior.events.map) is not in the dandiset.
  * Conditions: trials with the same `trial_type`, `direction`, start site and end site. Sites
    are found by clustering the start and end points of the session's trials (average linkage,
    cut at 30% of the extent of the trial positions). The paper's trial conditions are not in
    the dandiset.
  * Theta reference channel: among the hippocampal channels whose 6 to 9 Hz power ratio (to
    1 to 4 Hz) is at least the median, the one with the most 100 to 250 Hz power (spiking in
    the pyramidal layer), measured on the first trials. The dandiset does not say which
    channel is in the pyramidal layer.
  * LS LFP channel (for Figure 6): the middle channel of the first LS electrode group.
"""

from __future__ import annotations

import re

import h5py
import numpy as np
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy.cluster.hierarchy import fcluster, linkage
from scipy.ndimage import convolve1d
from scipy.sparse import csr_matrix
from scipy.signal import butter, find_peaks, hilbert, sosfiltfilt
from scipy.stats import ttest_ind

DANDISET_ID = "000213"
DANDISET_VERSION = "0.250624.0438"

FS_LFP = 1250.0
PAD_S = 1.0
N_BINS = 200
SMOOTH_BINS = 20
MAP_SMOOTH = 5
N_ITER = 10
TRAIN_FRACTION = 0.6
MIN_TRIALS = 10
MIN_SPIKES_PER_TRIAL = 1.5
PF_MIN_PEAK_HZ = 2.0
PF_THRESHOLD = 0.2
PF_MIN_WIDTH, PF_MAX_WIDTH = 5, 80
SITE_CUT = 0.3
N_SELECT_TRIALS = 8
HPC_LABELS = ("hpc", "ca1", "ca3")
DOWN = 10   # LFP-derived series for Figure 6 are kept at 125 Hz
TRIAL_SHIFTS_S = (-3.0, -2.0, -1.0, -0.5, 0.0, 0.5, 1.0, 2.0, 3.0)

_SOS = {}


def _sos(lo, hi):
    if (lo, hi) not in _SOS:
        _SOS[(lo, hi)] = butter(3, [lo, hi], btype="bandpass", fs=FS_LFP, output="sos")
    return _SOS[(lo, hi)]


def _str(values):
    return [v.decode() if isinstance(v, bytes) else str(v) for v in values]


def asset_urls():
    """Path and content URL of every asset in the pinned version."""
    with DandiAPIClient() as client:
        ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        return {a.path: a.get_content_url(follow_redirects=1, strip_query=True) for a in ds.get_assets()}


def parse_depths(session_id):
    """The two depths in the session name (um): the first is taken as the LS probe's (see the notebook)."""
    m = re.search(r"(\d+)um[-_](\d+)um", session_id)
    return (int(m.group(1)), int(m.group(2))) if m else (None, None)


def _select_channels(d, hpc_cols, starts, stops):
    """Theta reference: high theta ratio, then most 100 to 250 Hz power, on the first trials."""
    segs = []
    for a, b in list(zip(starts, stops))[:N_SELECT_TRIALS]:
        i0, i1 = int(a * FS_LFP), int(b * FS_LFP)
        if i1 - i0 > FS_LFP:
            segs.append(np.asarray(d[i0:i1, min(hpc_cols):max(hpc_cols) + 1], dtype=np.float64)[:, np.array(hpc_cols) - min(hpc_cols)])
    x = np.concatenate(segs)
    x = x - x.mean(0)
    theta = sosfiltfilt(_sos(6, 9), x, axis=0).var(0)
    delta = sosfiltfilt(_sos(1, 4), x, axis=0).var(0)
    high = sosfiltfilt(_sos(100, 250), x, axis=0).var(0)
    ratio = theta / np.maximum(delta, 1e-12)
    ok = ratio >= np.median(ratio)
    k = int(np.argmax(np.where(ok, high, -np.inf)))
    return hpc_cols[k], {"theta_ratio": float(ratio[k]), "median_theta_ratio": float(np.median(ratio)),
                         "high_power_rank": int((high > high[k]).sum())}


def load_session(path, url, read_lfp=True):
    """Everything the analyses use from one file, as plain arrays."""
    f = h5py.File(remfile.File(url, _max_cache_size=200_000_000), "r")
    s = {"path": path, "subject": f["general/subject/subject_id"][()].decode(),
         "session_id": f["general/session_id"][()].decode()}
    s["ls_depth"], s["hpc_depth"] = parse_depths(s["session_id"])

    el = f["general/extracellular_ephys/electrodes"]
    el_loc = np.array(_str(el["location"][:]))
    el_group = np.array(_str(el["group_name"][:]))
    s["electrode_locations"] = {k: int(v) for k, v in zip(*np.unique(el_loc, return_counts=True))}

    t = f["intervals/trials"]
    cols = list(_str(t.attrs["colnames"]))
    starts, stops = t["start_time"][:], t["stop_time"][:]
    n = len(starts)
    s["trials"] = {"start": starts, "stop": stops,
                   "direction": np.array(_str(t["direction"][:])) if "direction" in cols else np.array([""] * n),
                   "trial_type": np.array(_str(t["trial_type"][:])) if "trial_type" in cols else np.array([""] * n)}

    beh = f["processing/behavior"]
    task = [k for k in beh if k != "allocentric_frame_tracking"][0]
    pos = beh[task]["position"]
    xyz = pos["data"][:]
    ts = pos["timestamps"][:]
    s["task"] = task
    s["position_unit_stated"] = pos["data"].attrs["unit"]
    s["position_z_equals_y"] = bool(np.allclose(xyz[:, 1], xyz[:, 2], equal_nan=True))
    good_xy = xyz[:, :2][~np.isnan(xyz[:, :2]).any(axis=1)]
    extent = float(np.max(np.percentile(good_xy, 99, axis=0) - np.percentile(good_xy, 1, axis=0)))
    if s["position_unit_stated"] == "pixels":
        scale, unit = 1.0, "pixels"
    elif extent < 10:
        scale, unit = 100.0, "cm"     # values in metres
    else:
        scale, unit = 0.1, "cm"       # values in millimetres
    s["position_extent_stated_units"] = extent
    s["position_unit_used"] = unit
    s["position_scale_to_used"] = scale
    s["position_dt_median"] = float(np.median(np.diff(ts)))
    s["position_nonincreasing_steps"] = int((np.diff(ts) <= 0).sum())
    # time per position sample; equals the median step when timestamps are regular, and stays right
    # when timestamps repeat (sub-DT2)
    s["position_dt"] = float((ts[-1] - ts[0]) / (len(ts) - 1))
    s["position_nan_fraction"] = float(np.isnan(xyz[:, 0]).mean())
    # clock check of positions against the trials table: mean speed in the trial windows, shifted
    good = ~np.isnan(xyz[:, :2]).any(axis=1) & np.r_[True, np.diff(ts) > 0]
    tg, pg = ts[good], xyz[good, :2] * scale
    speed = np.r_[np.nan, np.hypot(*np.diff(pg, axis=0).T) / np.diff(tg)]
    speed[speed > np.nanpercentile(speed, 99.5)] = np.nan   # tracking jumps
    s["clock_trial_speed"] = {}
    for sh in TRIAL_SHIFTS_S:
        m = np.zeros(len(tg), bool)
        for a, b in zip(starts + sh, stops + sh):
            m[np.searchsorted(tg, a):np.searchsorted(tg, b)] = True
        s["clock_trial_speed"][sh] = float(np.nanmean(speed[m])) if m.any() else np.nan
    in_trial = np.zeros(len(ts), bool)
    for a, b in zip(starts, stops):
        in_trial[np.searchsorted(ts, a):np.searchsorted(ts, b, side="right")] = True
    s["pos_t"] = ts[in_trial]
    s["pos_xy"] = xyz[in_trial, :2] * scale

    units = []
    s["clock_trial_rate"] = None
    if "units" in f:
        u = f["units"]
        ucols = list(_str(u.attrs["colnames"]))
        idx = u["spike_times_index"][:]
        st = u["spike_times"][:]
        loc = _str(u["location"][:]) if "location" in ucols else ["unlabelled"] * len(idx)
        grp = _str(u["group_id"][:]) if "group_id" in ucols else [""] * len(idx)
        bounds = np.r_[0, idx]
        allt = np.sort(st)
        dur = (stops - starts).sum()
        s["clock_trial_rate"] = {sh: float(sum(np.searchsorted(allt, b + sh) - np.searchsorted(allt, a + sh)
                                               for a, b in zip(starts, stops)) / dur / len(idx)) for sh in TRIAL_SHIFTS_S}
        for i in range(len(idx)):
            times = st[bounds[i]:bounds[i + 1]]
            sorted_ok = bool(np.all(np.diff(times) >= 0))
            times = np.sort(times)
            mask = np.zeros(len(times), bool)
            for a, b in zip(starts - PAD_S, stops + PAD_S):
                mask[np.searchsorted(times, a):np.searchsorted(times, b)] = True
            units.append({"location": loc[i], "group": grp[i], "n_spikes_total": len(times),
                          "sorted": sorted_ok, "times": times[mask],
                          "first": float(times[0]) if len(times) else np.nan,
                          "last": float(times[-1]) if len(times) else np.nan})
    s["units"] = units

    lfp = f["processing/ecephys/LFP/ElectricalSeries_lfp"]
    d = lfp["data"]
    s["lfp_shape"], s["lfp_chunks"] = d.shape, d.chunks
    s["lfp_rate"] = float(lfp["starting_time"].attrs["rate"])
    s["lfp_start"] = float(lfp["starting_time"][()])
    s["lfp_conversion"] = float(d.attrs["conversion"])
    lfp_el = lfp["electrodes"][:]
    col_loc, col_group = el_loc[lfp_el], el_group[lfp_el]
    hpc_cols = [j for j, l in enumerate(col_loc) if l in HPC_LABELS]
    ls_cols = [j for j, l in enumerate(col_loc) if l == "ls"]
    s["hpc_channels_from"] = "electrodes table"
    if not hpc_cols or not ls_cols:   # sub-DT2 labels every electrode 'unknown'; use the groups of its units
        hpc_groups = {x["group"] for x in units if x["location"] in HPC_LABELS}
        ls_groups = {x["group"] for x in units if x["location"] == "ls"}
        hpc_cols = hpc_cols or [j for j, g in enumerate(col_group) if g in hpc_groups]
        ls_cols = ls_cols or [j for j, g in enumerate(col_group) if g in ls_groups]
        s["hpc_channels_from"] = "groups of the units"
    s["n_hpc_channels"], s["n_ls_channels"] = len(hpc_cols), len(ls_cols)
    s["theta_channel"] = s["ls_channel"] = None
    s["segments"] = []
    if not read_lfp or not hpc_cols or n == 0:
        return s
    theta_col, sel = _select_channels(d, hpc_cols, starts, stops)
    s["theta_channel"], s["theta_channel_selection"] = int(theta_col), sel
    if ls_cols:
        groups = [g for g in dict.fromkeys(col_group[ls_cols])]
        first = [j for j in ls_cols if col_group[j] == groups[0]]
        s["ls_channel"] = int(first[len(first) // 2])
    read_cols = sorted({theta_col} | ({s["ls_channel"]} if s["ls_channel"] is not None else set()))
    contiguous = read_cols[-1] - read_cols[0] < 8
    for k, (a, b) in enumerate(zip(starts, stops)):
        i0 = max(int((a - PAD_S) * FS_LFP), 0)
        i1 = min(int((b + PAD_S) * FS_LFP), d.shape[0])
        if contiguous:
            raw = np.asarray(d[i0:i1, read_cols[0]:read_cols[-1] + 1], dtype=np.float64)[:, np.array(read_cols) - read_cols[0]]
        else:
            raw = np.asarray(d[i0:i1, read_cols], dtype=np.float64)
        hp = raw[:, read_cols.index(theta_col)]
        seg = {"trial": k, "t0": i0 / FS_LFP, "n": i1 - i0,
               "theta_phase": np.angle(hilbert(sosfiltfilt(_sos(6, 9), hp))).astype(np.float32)}
        wide_hp = np.angle(hilbert(sosfiltfilt(_sos(4, 12), hp)))
        seg["hpc_phase_4_12"] = wide_hp[::DOWN].astype(np.float32)
        if s["ls_channel"] is not None:
            ls = raw[:, read_cols.index(s["ls_channel"])]
            seg["ls_phase_4_12"] = np.angle(hilbert(sosfiltfilt(_sos(4, 12), ls)))[::DOWN].astype(np.float32)
            g = sosfiltfilt(_sos(40, 200), ls) ** 2
            w = int(0.05 * FS_LFP)
            rms = np.sqrt(np.convolve(g, np.ones(w) / w, mode="same"))
            seg["ls_gamma_rms"] = rms[::DOWN].astype(np.float32)
        s["segments"].append(seg)
    return s


def load_session_safe(args):
    path, url = args
    try:
        return load_session(path, url)
    except Exception as e:  # reported in the notebook, never silently dropped
        return {"path": path, "error": repr(e)}


# --- trials, conditions, linearization ------------------------------------------------------

def trial_sites(s):
    """Start and end site of each trial, by clustering the start and end points."""
    tr = s["trials"]
    pts, which = [], []
    t, xy = s["pos_t"], s["pos_xy"]
    for k, (a, b) in enumerate(zip(tr["start"], tr["stop"])):
        i0, i1 = np.searchsorted(t, a), np.searchsorted(t, b, side="right")
        seg = xy[i0:i1]
        seg = seg[~np.isnan(seg).any(axis=1)]
        if len(seg) < 2:
            pts += [[np.nan, np.nan]] * 2
        else:
            pts += [seg[0], seg[-1]]
        which.append(k)
    pts = np.array(pts, float)
    good = ~np.isnan(pts[:, 0])
    labels = np.full(len(pts), -1)
    valid = xy[~np.isnan(xy).any(axis=1)]
    extent = np.max(np.percentile(valid, 99, axis=0) - np.percentile(valid, 1, axis=0))
    if good.sum() >= 2:
        z = linkage(pts[good], method="average")
        labels[good] = fcluster(z, SITE_CUT * extent, criterion="distance")
    return labels[0::2], labels[1::2]


def conditions(s):
    """Condition label per trial: trial type, direction, start site and end site."""
    st, en = trial_sites(s)
    tr = s["trials"]
    keys = [f"{tt}|{d}|{a}->{b}" for tt, d, a, b in zip(tr["trial_type"], tr["direction"], st, en)]
    bad = (st < 0) | (en < 0)
    return np.array([("" if b else k) for k, b in zip(keys, bad)])


def linearize(s, k):
    """Times, bins and cumulative path of the position samples of trial k."""
    tr = s["trials"]
    t, xy = s["pos_t"], s["pos_xy"]
    i0, i1 = np.searchsorted(t, tr["start"][k]), np.searchsorted(t, tr["stop"][k], side="right")
    tt, p = t[i0:i1], xy[i0:i1]
    ok = ~np.isnan(p).any(axis=1)
    tt, p = tt[ok], p[ok]
    if len(tt) < 10:
        return None
    dts = np.diff(tt)
    w = max(int(round(0.1 / np.median(dts[dts > 0]))), 1)   # 100 ms moving average before measuring path
    ps = np.column_stack([np.convolve(np.pad(p[:, j], w, mode="edge"), np.ones(2 * w + 1) / (2 * w + 1), "same")[w:-w] for j in range(2)])
    step = np.r_[0, np.hypot(*np.diff(ps, axis=0).T)]
    cum = np.cumsum(step)
    if cum[-1] <= 0:
        return None
    b = np.minimum((cum / cum[-1] * N_BINS).astype(int), N_BINS - 1)
    return tt, b, cum[-1]


def spike_phases(s, times, k):
    """Theta phase (6 to 9 Hz) of the given spike times, from trial k's LFP segment."""
    seg = s["segments"][k]
    idx = np.round((times - seg["t0"]) * FS_LFP).astype(int)
    ok = (idx >= 0) & (idx < seg["n"])
    out = np.full(len(times), np.nan)
    out[ok] = seg["theta_phase"][idx[ok]]
    return out


def trial_maps(s, unit, trials, shift=0.0):
    """Counts, occupancy (samples) and per-bin circular-mean phase, each trials x N_BINS."""
    T = len(trials)
    counts = np.zeros((T, N_BINS))
    occ = np.zeros((T, N_BINS))
    phase = np.zeros((T, N_BINS))
    tr = s["trials"]
    for i, k in enumerate(trials):
        lin = s["_lin"][k]
        if lin is None:
            continue
        tt, b, _ = lin
        occ[i] = np.bincount(b, minlength=N_BINS)
        a, z = tr["start"][k], tr["stop"][k]
        st = unit["times"] + shift
        st = st[(st > a) & (st < z)]
        if not len(st):
            continue
        j = np.clip(np.searchsorted(tt, st), 1, len(tt) - 1)
        j = np.where(np.abs(tt[j - 1] - st) <= np.abs(tt[j] - st), j - 1, j)
        sb = b[j]
        counts[i] = np.bincount(sb, minlength=N_BINS)
        ph = spike_phases(s, st - shift, k)
        good = ~np.isnan(ph)
        if good.any():
            c = np.bincount(sb[good], weights=np.cos(ph[good]), minlength=N_BINS)
            sn = np.bincount(sb[good], weights=np.sin(ph[good]), minlength=N_BINS)
            has = np.bincount(sb[good], minlength=N_BINS) > 0
            phase[i, has] = np.arctan2(sn[has], c[has])
    occ = np.apply_along_axis(_medfilt5, 1, occ)
    occ[occ < 1] = 1
    return counts, occ, phase


def _medfilt5(x):
    p = np.pad(x, 2)   # MATLAB medfilt1 pads with zeros
    return np.median(np.lib.stride_tricks.sliding_window_view(p, 5), axis=1)


def matlab_smooth(x, span, axis=-1):
    """MATLAB `smooth` moving average: odd span (even spans lose one), shrinking at the edges."""
    span = span if span % 2 else span - 1
    h = span // 2
    x = np.moveaxis(np.asarray(x, float), axis, -1)
    n = x.shape[-1]
    c = np.concatenate([np.zeros(x.shape[:-1] + (1,)), np.cumsum(x, axis=-1)], axis=-1)
    i = np.arange(n)
    r = np.minimum(np.minimum(i, n - 1 - i), h)
    out = (c[..., i + r + 1] - c[..., i - r]) / (2 * r + 1)
    return np.moveaxis(out, -1, axis)


def circ_smooth(phase, span):
    """circ_smoothTS(..., 'method', 'mean', 'exclude', 0) over the last axis."""
    if span <= 1:
        return phase.copy()
    h = int(np.ceil(span / 2))
    has = phase != 0
    c = np.where(has, np.cos(phase), 0.0)
    sn = np.where(has, np.sin(phase), 0.0)
    k = np.ones(2 * h + 1)
    conv = lambda a: convolve1d(a, k, axis=-1, mode="constant")
    cs, ss, ns = conv(c), conv(sn), conv(has.astype(float))
    return np.where(ns > 0, np.arctan2(ss, cs), 0.0)


def rate_box(counts, occ, dt, span=SMOOTH_BINS):
    return matlab_smooth(counts, span) / (matlab_smooth(occ, span) * dt)


def rate_map(counts, occ, dt, span=MAP_SMOOTH):
    """Smoothed rate map used for place fields (bz_firingMap1D `rateMaps`, 5 bins)."""
    return matlab_smooth(counts, span) / (matlab_smooth(occ, span) * dt)


# --- decoder ---------------------------------------------------------------------------------

def _nearest_template(templates, labels, x, rng):
    """Bin whose template is closest to each x; ties among equal templates broken at random."""
    vals, inv = np.unique(templates, return_inverse=True)
    order = np.argsort(inv, kind="stable")
    counts = np.bincount(inv, minlength=len(vals))
    first = np.r_[0, np.cumsum(counts)[:-1]]
    j = np.clip(np.searchsorted(vals, x), 1, len(vals) - 1) if len(vals) > 1 else np.zeros(len(x), int)
    if len(vals) > 1:
        left = vals[j - 1]
        right = vals[j]
        dl, dr = np.abs(x - left), np.abs(right - x)
        g = np.where(dl < dr, j - 1, j)
        tie = dl == dr
        g = np.where(tie & (rng.random(len(x)) < 0.5), j - 1, g)
    else:
        g = j
    pick = first[g] + np.floor(rng.random(len(x)) * counts[g]).astype(int)
    return labels[order[pick]]


def decode_1d(feature, pos, rng, permute_test=False):
    """One 60/40 split: mean squared error (bins squared) of the template decoder."""
    n = len(feature)
    perm = rng.permutation(n)
    k = int(round(np.percentile(np.arange(1, n + 1), 60)))
    tr, te = perm[:k], perm[k:]
    lab, inv = np.unique(pos[tr], return_inverse=True)
    tmpl = np.bincount(inv, weights=feature[tr]) / np.bincount(inv)
    x = feature[te]
    if permute_test:
        x = x[rng.permutation(len(x))]
    pred = _nearest_template(tmpl, lab, x, rng)
    return float(np.mean((pos[te] - pred) ** 2))


def decode_cell(counts, occ, phase, dt, rng, n_iter=N_ITER, split="samples"):
    """MSE per iteration for rate, phase (cosine), and both chance controls."""
    T = counts.shape[0]
    r = rate_box(counts, occ, dt).ravel()
    p = np.cos(circ_smooth(phase, SMOOTH_BINS)).ravel()
    pos = np.tile(np.arange(1, N_BINS + 1), T).astype(float)
    out = {"rate": [], "phase": [], "chance_rate": [], "chance_phase": []}
    for _ in range(n_iter):
        if split == "samples":
            seed = rng.integers(2**32)
            for key, feat, perm in (("rate", r, False), ("phase", p, False),
                                    ("chance_rate", r, True), ("chance_phase", p, True)):
                out[key].append(decode_1d(feat, pos, np.random.default_rng(seed), permute_test=perm))
        else:   # whole trials held out, a variant
            tperm = rng.permutation(T)
            ntr = int(round(TRAIN_FRACTION * T))
            trm = np.zeros(T, bool)
            trm[tperm[:ntr]] = True
            mask = np.repeat(trm, N_BINS)
            for key, feat in (("rate", r), ("phase", p)):
                lab, inv = np.unique(pos[mask], return_inverse=True)
                tmpl = np.bincount(inv, weights=feat[mask]) / np.bincount(inv)
                pred = _nearest_template(tmpl, lab, feat[~mask], rng)
                out[key].append(float(np.mean((pos[~mask] - pred) ** 2)))
    return {k: np.array(v) for k, v in out.items() if v}


# --- place fields ----------------------------------------------------------------------------

def place_fields(rate_trials):
    """Fields of one cell in one condition, after bz_getPlaceFields1D with the Methods' limits."""
    mean = rate_trials.mean(0)
    sd = rate_trials.std(0, ddof=1)
    rms = np.sqrt(matlab_smooth(mean ** 2, MAP_SMOOTH))
    pks, _ = find_peaks(rms, height=PF_MIN_PEAK_HZ, width=PF_MIN_WIDTH)
    keep = list(pks)
    # adjacent peaks without a dip below threshold * their mean: keep the higher
    drop = set()
    for a, b in zip(keep[:-1], keep[1:]):
        if mean[a:b + 1].min() > (rms[a] + rms[b]) / 2 * PF_THRESHOLD:
            drop.add(b if rms[a] > rms[b] else a)
    keep = [p for p in keep if p not in drop and mean[p] >= sd[p]]
    fields = []
    for p in keep:
        inside = mean > rms[p] * PF_THRESHOLD
        a = p
        while a > 0 and inside[a]:
            a -= 1
        b = p
        while b < N_BINS - 1 and inside[b]:
            b += 1
        width = b - a
        if PF_MIN_WIDTH < width < PF_MAX_WIDTH:
            seg = mean[a:b + 1]
            com = a + int(np.searchsorted(np.cumsum(seg), seg.sum() / 2))
            fields.append({"start": a, "stop": b, "width": width, "peak_hz": float(rms[p]),
                           "peak_bin": int(p), "com": com,
                           "peak_sd": float(rate_trials[:, p].std(ddof=1)),
                           "peak_cv": float(rate_trials[:, p].std(ddof=1) / max(rate_trials[:, p].mean(), 1e-12))})
    return fields


# --- circular statistics ---------------------------------------------------------------------

def circ_mean(a):
    return float(np.angle(np.mean(np.exp(1j * np.asarray(a)))))


def circ_corrcl(alpha, x):
    """Circular-linear correlation and p-value (CircStat circ_corrcl)."""
    alpha, x = np.asarray(alpha, float), np.asarray(x, float)
    n = len(alpha)
    rxs = np.corrcoef(x, np.sin(alpha))[0, 1]
    rxc = np.corrcoef(x, np.cos(alpha))[0, 1]
    rcs = np.corrcoef(np.sin(alpha), np.cos(alpha))[0, 1]
    rho = np.sqrt((rxc ** 2 + rxs ** 2 - 2 * rxc * rxs * rcs) / (1 - rcs ** 2))
    from scipy.stats import chi2
    return float(rho), float(1 - chi2.cdf(n * rho ** 2, 2))


# --- per-session analysis --------------------------------------------------------------------

SEED_DECODE = 213001
SEED_ENSEMBLE = 213002
SEED_SITES = 213003
SPEED_LAGS_S = tuple(np.round(np.arange(-1.0, 1.01, 0.1), 1))
SPEED_BIN_S = 0.05
LFP_LAGS_MS = tuple(range(-200, 201, 25))
N_SEGMENTS = 10
ONSET_BINS = 15
INFO_SMOOTHINGS = tuple(range(1, 51))
INFO_LEVELS = 7
ENSEMBLE_SIZES = (15, 20, 25)
ENSEMBLE_DRAWS = 10
ENSEMBLE_LEVELS = 20


def region(location):
    return "ls" if location == "ls" else ("hpc" if location in HPC_LABELS else "other")


def _unit_trial_spikes(unit, starts, stops):
    t = unit["times"]
    return [t[np.searchsorted(t, a, side="right"):np.searchsorted(t, b)] for a, b in zip(starts, stops)]


def olypher_peak(values, levels_range):
    """Peak over bins of the positional information (bits) of trials x bins values."""
    lo, hi = levels_range
    if hi <= lo:
        return 0.0
    k = np.clip(((values - lo) / (hi - lo) * INFO_LEVELS).astype(int), 0, INFO_LEVELS - 1)
    T, B = k.shape
    pk = np.bincount(k.ravel(), minlength=INFO_LEVELS) / k.size
    joint = np.bincount(np.tile(np.arange(B), T) * INFO_LEVELS + k.ravel(), minlength=B * INFO_LEVELS)
    pkx = joint.reshape(B, INFO_LEVELS) / T
    with np.errstate(divide="ignore", invalid="ignore"):
        terms = np.where(pkx > 0, pkx * np.log2(pkx / pk), 0.0)
    return float(terms.sum(1).max())


def info_curves(counts, occ, phase, dt):
    rate_peak, phase_peak = [], []
    for w in INFO_SMOOTHINGS:
        r = rate_box(counts, occ, dt, span=w) if w > 1 else counts / (occ * dt)
        rate_peak.append(olypher_peak(r, (r.min(), r.max())))
        p = circ_smooth(phase, w)
        phase_peak.append(olypher_peak(p, (-np.pi, np.pi)))
    return np.array(rate_peak), np.array(phase_peak)


def _speed_xcorr(s, reg):
    """Correlation of the population spike count with running speed, spikes shifted by each lag.

    A clock check: firing in the hippocampus and LS rises with running speed with little delay, so
    the correlation should peak near zero lag if spikes and positions share a clock."""
    tr = s["trials"]
    t, xy = s["pos_t"], s["pos_xy"]
    times = np.sort(np.concatenate([u["times"] for u in s["units"] if region(u["location"]) == reg] or [np.array([])]))
    if not len(times):
        return {lag: np.nan for lag in SPEED_LAGS_S}
    speed_all, edges_all = [], []
    for a, b in zip(tr["start"], tr["stop"]):
        i0, i1 = np.searchsorted(t, a), np.searchsorted(t, b, side="right")
        tt, p = t[i0:i1], xy[i0:i1]
        ok = ~np.isnan(p).any(axis=1)
        if ok.sum() < 10:
            continue
        tt, p = tt[ok], p[ok]
        uniq = np.r_[True, np.diff(tt) > 0]
        tt, p = tt[uniq], p[uniq]
        edges = np.arange(a, b - SPEED_BIN_S, SPEED_BIN_S)
        if len(edges) < 4:
            continue
        cx = np.interp(edges + SPEED_BIN_S / 2, tt, p[:, 0])
        cy = np.interp(edges + SPEED_BIN_S / 2, tt, p[:, 1])
        v = np.hypot(np.gradient(cx), np.gradient(cy)) / SPEED_BIN_S
        speed_all.append(v)
        edges_all.append(edges)
    if not speed_all:
        return {lag: np.nan for lag in SPEED_LAGS_S}
    v = np.concatenate(speed_all)
    out = {}
    for lag in SPEED_LAGS_S:
        n = np.concatenate([np.searchsorted(times, e + lag + SPEED_BIN_S) - np.searchsorted(times, e + lag) for e in edges_all])
        out[lag] = float(np.corrcoef(n, v)[0, 1]) if n.std() > 0 else np.nan
    return out


def _ensemble_mse(feats, pos, rng):
    """Poisson naive Bayes over units (features: samples x units, integer levels), 10 splits."""
    n = len(pos)
    out = []
    for _ in range(N_ITER):
        perm = rng.permutation(n)
        k = int(round(TRAIN_FRACTION * n))
        tr, te = perm[:k], perm[k:]
        cnt = np.bincount(pos[tr], minlength=N_BINS).astype(float)
        onehot = csr_matrix((np.ones(len(tr)), (pos[tr], np.arange(len(tr)))), shape=(N_BINS, len(tr)))
        lam = np.asarray(onehot @ feats[tr])
        lam = np.maximum(lam / np.maximum(cnt, 1)[:, None], 1e-3)
        ll = feats[te] @ np.log(lam).T - lam.sum(1)[None, :]
        ll[:, cnt == 0] = -np.inf
        pred = np.argmax(ll + rng.random(ll.shape) * 1e-9, axis=1)
        out.append(np.mean((pred - pos[te]) ** 2))
    return float(np.mean(out))


def _levels(x, lo, hi):
    if hi <= lo:
        return np.ones_like(x, dtype=float)
    return np.clip(((x - lo) / (hi - lo) * ENSEMBLE_LEVELS).astype(int), 0, ENSEMBLE_LEVELS - 1).astype(float) + 1


def analyse_session(s, index):
    """Every per-cell and per-session result the notebook uses, for one loaded session."""
    out = {"summary": {k: s[k] for k in ("path", "subject", "session_id", "ls_depth", "hpc_depth", "task",
                                          "position_unit_stated", "position_unit_used",
                                          "position_extent_stated_units", "position_dt_median", "position_dt",
                                          "position_nan_fraction", "position_nonincreasing_steps",
                                          "position_z_equals_y", "electrode_locations", "lfp_shape",
                                          "lfp_chunks", "lfp_rate", "lfp_start", "lfp_conversion",
                                          "hpc_channels_from", "n_hpc_channels", "n_ls_channels",
                                          "theta_channel", "ls_channel", "clock_trial_speed", "clock_trial_rate")}}
    sm = out["summary"]
    sm["theta_channel_selection"] = s.get("theta_channel_selection")
    tr = s["trials"]
    starts, stops = tr["start"], tr["stop"]
    sm["n_trials"] = len(starts)
    sm["trial_s_median"] = float(np.median(stops - starts)) if len(starts) else np.nan
    sm["trial_types"] = sorted(set(tr["trial_type"]))
    sm["directions"] = sorted(set(tr["direction"]))
    sm["unit_locations"] = {}
    for u in s["units"]:
        sm["unit_locations"][u["location"]] = sm["unit_locations"].get(u["location"], 0) + 1
    sm["units_unsorted"] = int(sum(not u["sorted"] for u in s["units"]))
    sm["n_units"] = len(s["units"])
    sm["n_spikes_total"] = int(sum(u["n_spikes_total"] for u in s["units"]))
    sm["trial_starts_rounded"] = tuple(np.round(starts, 2).tolist())
    sm["has_hpc_units"] = any(region(u["location"]) == "hpc" for u in s["units"])
    sm["has_ca3_units"] = any(u["location"] == "ca3" for u in s["units"])
    sm["spikes_after_lfp_end"] = int(sum(u["last"] > s["lfp_shape"][0] / FS_LFP for u in s["units"] if np.isfinite(u["last"])))
    sm["trials_after_position_end"] = int((stops > (s["pos_t"][-1] if len(s["pos_t"]) else -1)).sum())
    has_theta = s["theta_channel"] is not None
    sm["has_theta"] = has_theta
    cond = conditions(s)
    s["_lin"] = [linearize(s, k) for k in range(len(starts))]
    lens = np.array([l[2] for l in s["_lin"] if l is not None])
    sm["path_length_median"] = float(np.median(lens)) if len(lens) else np.nan
    sm["trials_without_positions"] = int(sum(l is None for l in s["_lin"]))
    dt = s["position_dt"]
    labels, nper = np.unique(cond[cond != ""], return_counts=True)
    sm["conditions"] = dict(zip(labels.tolist(), nper.tolist()))
    use = [c for c, n in zip(labels, nper) if n >= MIN_TRIALS]
    sm["conditions_used"] = len(use)
    trials_of = {c: [k for k in np.flatnonzero(cond == c) if s["_lin"][k] is not None] for c in use}

    cells, info, ens_maps = [], [], {}
    has_hpc_units = any(region(u["location"]) == "hpc" for u in s["units"])
    lag_phases = {lag: [] for lag in LFP_LAGS_MS}
    for ui, u in enumerate(s["units"]):
        reg = region(u["location"])
        if reg == "other":
            continue
        per_trial = _unit_trial_spikes(u, starts, stops)
        for ci, c in enumerate(use):
            ks = trials_of[c]
            if len(ks) < MIN_TRIALS:
                continue
            nsp = sum(len(per_trial[k]) for k in ks)
            rec = {"unit": ui, "location": u["location"], "region": reg, "condition": c,
                   "n_trials": len(ks), "n_spikes": nsp, "active": nsp >= MIN_SPIKES_PER_TRIAL * len(ks)}
            if not rec["active"]:
                cells.append(rec)
                continue
            counts, occ, phase = trial_maps(s, u, ks) if has_theta else (*trial_maps_counts(s, u, ks), None)
            fields = place_fields(rate_map(counts, occ, dt))
            rec["n_fields"] = len(fields)
            if fields:
                f0 = fields[0]
                rec.update({"field_peak_hz": f0["peak_hz"], "field_width": f0["width"], "field_com": f0["com"],
                            "field_peak_sd": f0["peak_sd"], "field_peak_cv": f0["peak_cv"]})
                rec["field_peaks_hz"] = [f["peak_hz"] for f in fields]
                rec["field_widths"] = [f["width"] for f in fields]
            if has_theta:
                rng = np.random.default_rng([SEED_DECODE, index, ui, ci])
                res = decode_cell(counts, occ, phase, dt, rng)
                for key, v in res.items():
                    rec["mse_" + key] = float(v.mean())
                rec["p_phase_vs_chance"] = float(ttest_ind(res["phase"], res["chance_phase"]).pvalue)
                rec["p_phase_vs_rate"] = float(ttest_ind(res["phase"], res["rate"]).pvalue)
                rec["p_rate_vs_chance"] = float(ttest_ind(res["rate"], res["chance_rate"]).pvalue)
                rv = decode_cell(counts, occ, phase, dt, np.random.default_rng([SEED_DECODE + 1, index, ui, ci]), split="trials")
                rec["mse_rate_trialsplit"] = float(rv["rate"].mean())
                rec["mse_phase_trialsplit"] = float(rv["phase"].mean())
                rec["p_phase_vs_rate_trialsplit"] = float(ttest_ind(rv["phase"], rv["rate"]).pvalue)
                # onset phase: spikes in the first ONSET_BINS bins
                onset = []
                for i, k in enumerate(ks):
                    tt, b, _ = s["_lin"][k]
                    st = per_trial[k]
                    if not len(st):
                        continue
                    j = np.clip(np.searchsorted(tt, st), 0, len(tt) - 1)
                    ph = spike_phases(s, st, k)
                    sel = (b[j] < ONSET_BINS) & ~np.isnan(ph)
                    onset.extend(ph[sel].tolist())
                rec["onset_phase"] = circ_mean(onset) if onset else np.nan
                rec["onset_n_spikes"] = len(onset)
                if reg == "hpc" and fields:
                    rc, pc = info_curves(counts, occ, phase, dt)
                    info.append({"unit": ui, "condition": c, "rate": rc, "phase": pc, "n_trials": len(ks)})
                ens_maps.setdefault(c, []).append((reg, ui, counts, occ, phase))
            cells.append(rec)
        if has_theta and region(u["location"]) == "hpc":
            for k, st in enumerate(per_trial):
                seg = s["segments"][k]
                for lag in LFP_LAGS_MS:
                    idx = np.round((st - seg["t0"]) * FS_LFP).astype(int) + int(lag * FS_LFP / 1000)
                    ok = (idx >= 0) & (idx < seg["n"])
                    lag_phases[lag].append(seg["theta_phase"][idx[ok]])
    out["clock_speed"] = _speed_xcorr(s, "hpc" if has_hpc_units else "ls")
    out["cells"] = cells
    out["info"] = info
    out["clock_lfp"] = {lag: (float(np.abs(np.mean(np.exp(1j * np.concatenate(v))))) if v and sum(map(len, v)) else np.nan)
                        for lag, v in lag_phases.items()}
    out["fig6"] = _fig6(s) if has_theta and s["ls_channel"] is not None else None
    out["ensemble"] = _ensembles(ens_maps, dt, index)
    return out


def trial_maps_counts(s, unit, trials, shift=0.0):
    """Counts and occupancy only (no LFP needed)."""
    T = len(trials)
    counts = np.zeros((T, N_BINS))
    occ = np.zeros((T, N_BINS))
    tr = s["trials"]
    for i, k in enumerate(trials):
        tt, b, _ = s["_lin"][k]
        occ[i] = np.bincount(b, minlength=N_BINS)
        st = unit["times"] + shift
        st = st[(st > tr["start"][k]) & (st < tr["stop"][k])]
        if len(st):
            j = np.clip(np.searchsorted(tt, st), 1, len(tt) - 1)
            j = np.where(np.abs(tt[j - 1] - st) <= np.abs(tt[j] - st), j - 1, j)
            counts[i] = np.bincount(b[j], minlength=N_BINS)
    occ = np.apply_along_axis(_medfilt5, 1, occ)
    occ[occ < 1] = 1
    return counts, occ


def _fig6(s):
    """Per position segment: LS-hippocampus theta phase locking and theta-gamma coupling."""
    fs = FS_LFP / DOWN
    win, step = int(round(0.15 * fs)), int(round(0.05 * fs))
    plv = [[] for _ in range(N_SEGMENTS)]
    ph_seg = [[] for _ in range(N_SEGMENTS)]
    g_seg = [[] for _ in range(N_SEGMENTS)]
    tr = s["trials"]
    for k, seg in enumerate(s["segments"]):
        lin = s["_lin"][k]
        if lin is None or "ls_phase_4_12" not in seg:
            continue
        tt, b, _ = lin
        t = seg["t0"] + np.arange(len(seg["hpc_phase_4_12"])) / fs
        inside = (t >= tr["start"][k]) & (t <= tr["stop"][k])
        j = np.clip(np.searchsorted(tt, t), 0, len(tt) - 1)
        sg = np.where(inside, b[j] * N_SEGMENTS // N_BINS, -1)
        d = np.exp(1j * (seg["hpc_phase_4_12"] - seg["ls_phase_4_12"]))
        for w0 in range(0, len(t) - win, step):
            c = sg[w0 + win // 2]
            if c >= 0 and sg[w0] >= 0 and sg[w0 + win - 1] >= 0:
                plv[c].append(np.abs(d[w0:w0 + win].mean()))
        for c in range(N_SEGMENTS):
            m = sg == c
            ph_seg[c].append(seg["hpc_phase_4_12"][m])
            g_seg[c].append(seg["ls_gamma_rms"][m])
    coh = np.array([np.mean(v) if v else np.nan for v in plv])
    cfc = np.array([circ_corrcl(np.concatenate(p), np.concatenate(g))[0] if sum(map(len, p)) > 100 else np.nan
                    for p, g in zip(ph_seg, g_seg)])
    return {"coherence": coh, "cfc": cfc}


def _ensembles(ens_maps, dt, index):
    out = []
    for ci, (c, cells) in enumerate(sorted(ens_maps.items())):
        ls = [x for x in cells if x[0] == "ls"]
        hp = [x for x in cells if x[0] == "hpc"]
        if len(ls) < ENSEMBLE_SIZES[0] or len(hp) < ENSEMBLE_SIZES[0]:
            continue
        T = ls[0][2].shape[0]
        pos = np.tile(np.arange(N_BINS), T)

        def feats(group):
            r, p = [], []
            for _, _, counts, occ, phase in group:
                rr = rate_box(counts, occ, dt).ravel()
                pp = circ_smooth(phase, SMOOTH_BINS).ravel()
                r.append(_levels(rr, rr.min(), rr.max()))
                p.append(_levels(pp, -np.pi, np.pi))
            return np.array(r).T, np.array(p).T
        lr, lp = feats(ls)
        hr, hp_ = feats(hp)
        rng = np.random.default_rng([SEED_ENSEMBLE, index, ci])
        for n in ENSEMBLE_SIZES:
            if len(ls) < n or len(hp) < n:
                continue
            rec = {"condition": c, "size": n, "n_ls": len(ls), "n_hpc": len(hp), "ls_phase": [], "ls_rate": [],
                   "hpc_phase": [], "hpc_rate": []}
            for _ in range(ENSEMBLE_DRAWS):
                a = rng.choice(len(ls), n, replace=False)
                b = rng.choice(len(hp), n, replace=False)
                rec["ls_phase"].append(_ensemble_mse(lp[:, a], pos, rng))
                rec["ls_rate"].append(_ensemble_mse(lr[:, a], pos, rng))
                rec["hpc_phase"].append(_ensemble_mse(hp_[:, b], pos, rng))
                rec["hpc_rate"].append(_ensemble_mse(hr[:, b], pos, rng))
            out.append(rec)
    return out


def process(args):
    """Load and analyse one session in a worker; errors are returned, never dropped."""
    index, path, url = args
    try:
        s = load_session(path, url)
    except Exception as e:
        return {"summary": {"path": path}, "error": "load: " + repr(e)}
    try:
        return analyse_session(s, index)
    except Exception as e:
        import traceback
        return {"summary": {"path": path}, "error": "analyse: " + traceback.format_exc()}


def run_all(workers=4):
    """Every session of the pinned version, in parallel processes."""
    from concurrent.futures import ProcessPoolExecutor
    urls = asset_urls()
    jobs = [(i, p, urls[p]) for i, p in enumerate(sorted(urls))]
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(process, jobs))
