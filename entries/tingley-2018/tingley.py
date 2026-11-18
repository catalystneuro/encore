"""Loading and measures for Tingley and Buzsaki (2018) on DANDI:000213.

Everything is streamed from the archive at the pinned version (VERSION) with
remfile and h5py; nothing is written to disk. Each session is reduced as it
loads to what the claims use: the units' in-trial spikes with their linearized
position bin, CA1 theta phase, instantaneous rate and running speed, the trial
table, and a few LFP measures per trial (Figure 6).

Where each parameter comes from (C = the claim's criterion in
claims/tingley-2018.yaml, which cites the paper or its code; P = a passage of
the paper taken under protocol author step 1.6; A = an assumption; S = a
standard choice that cannot change a result):

- Included condition: >= 10 trials and summed spikes >= 1.5 x trials (C, shared
  methods; STAR Methods, place field definition item 5 and position prediction).
- Spike phase: CA1 pyramidal-layer channel (the electrodes table's ca1_channel,
  sessionInfo.ca1), 3rd-order Butterworth 6-9 Hz, zero phase (filtfilt), Hilbert
  angle (C, shared methods, following buzcode bz_phaseMap1D); 4-12 Hz variant (C).
  Zero-phase filtering is A (bz_Filter uses filtfilt; not stated in the paper).
- Rate map: per trial and bin, spike count over occupancy (C). Bins a trial did
  not occupy are set to 0 Hz before smoothing (A: buzcode bz_firingMap1D sets
  NaN rates to 0). Box smoothing over 20 bins, a centred moving mean that
  shrinks at the edges (C; S for the edge handling).
- Phase map: circular mean of the bin's spike phases; box smoothing by circular
  mean over non-empty bins (C). Bins with no spike within the window are
  undefined; they are set to phase 0 for decoding and information, as a
  zero-initialised phase map would give (A, see decode_unit()). Leaving them
  out is a variant; it lets phase decoding read where the cell fires (the
  phase-shift null of shift_phases() passes it as often as the real data).
- Bins, reading (a): one bin per point of the condition's template
  (trial_conditions, 201 points; the claims' "200 bins"); reading (b): bins of
  1.5 cm of template path length (C). Reading (b) needs a metric template; the
  LED sessions (DT2) are in pixels and keep reading (a) (A).
- Single-cell decoder: template = mean of the training samples per bin;
  prediction = the bin whose template value is nearest the test value; MSE of
  predicted against true bin (C; STAR Methods, position prediction). 10 random
  60/40 splits (C); chance permutes the feature vector against positions (C).
  Splits, reading (a) whole trials, (b) pooled trial-by-bin samples (C). Ties
  between equally near template bins are broken at random (A; the lowest bin,
  as MATLAB's min returns, is a variant).
- Place fields: peaks of the trial-mean rate map >= 2 Hz, edges where the rate
  falls below 20% of the peak, width 8-120 cm at 1.5 cm per bin, peak mean rate
  above the SD over trials, merged peaks dropped (C, after buzcode
  bz_getPlaceFields1D). Rate map reading (a) Gaussian smoothing (S: sigma of 5
  bins, the bz_firingMap1D default is not in the paper or claims; A), (b) box.
  The "first field" is the field with the highest peak (A).
- Olypher information: values discretized into 7 levels, (a) equal widths over
  the map's range, (b) equal counts (C); I(x) = sum_k P(k|x) log2 P(k|x)/P(k) (C).
  Best smoothing: argmax of the curve smoothed as MATLAB smooth(y, 5) (S).
- Peer prediction (Figure 5): windows of +/- 1 to 150 ms, 10 trial-order
  shuffles, strength as makeFig5.m (C); a normal GLM solved by least squares,
  one fit per trial with intercept, CA1 theta sine, cosine and angle, position
  and speed (C, STAR Methods); trials of unequal length cut to the shorter in
  the shuffles (A).
"""

from __future__ import annotations

import re
import time

import h5py
import numpy as np
import remfile
import requests
from scipy import signal, stats

DANDISET = "000213"
VERSION = "0.261109.2219"
API = "https://api.dandiarchive.org/api"
LFP_RATE = 1250.0
CM_PER_BIN = 1.5          # Results, paragraph 2 (C)
SMOOTH = 20               # STAR Methods, position prediction (C)
N_SPLITS = 10             # STAR Methods, position prediction (C)
TRAIN_FRAC = 0.6          # STAR Methods, position prediction (C)
MIN_TRIALS = 10           # STAR Methods, place field definition (C)
MIN_SPIKES_PER_TRIAL = 1.5  # STAR Methods, position prediction (C)
HPC_LABELS = ("hpc", "ca1", "ca3")


# ----------------------------------------------------------------- archive
def list_assets(version: str = VERSION) -> list[dict]:
    url = f"{API}/dandisets/{DANDISET}/versions/{version}/assets/?page_size=500"
    out = []
    while url:
        r = requests.get(url, timeout=60).json()
        out += r["results"]
        url = r.get("next")
    return sorted(out, key=lambda a: a["path"])


def s3_url(asset: dict, version: str = VERSION) -> str:
    info = requests.get(
        f"{API}/dandisets/{DANDISET}/versions/{version}/assets/{asset['asset_id']}/", timeout=60).json()
    return [u for u in info["contentUrl"] if "s3" in u][0]


def open_asset(asset: dict, version: str = VERSION) -> h5py.File:
    for attempt in range(4):
        try:
            return h5py.File(remfile.File(s3_url(asset, version)), "r")
        except Exception:
            if attempt == 3:
                raise
            time.sleep(5)


def _str(a):
    return np.array([x.decode() if isinstance(x, bytes) else str(x) for x in a])


def _ragged(group, name):
    data = group[name][:]
    idx = group[name + "_index"][:]
    starts = np.r_[0, idx[:-1]]
    return [data[s:e] for s, e in zip(starts, idx)]


def session_depths(path: str):
    """The two depths in the session name (um); sessionInfo.depth is the first."""
    m = re.findall(r"(\d+)um", path)
    return (int(m[0]), int(m[1])) if len(m) >= 2 else (np.nan, np.nan)


# ----------------------------------------------------------------- LFP
def theta_phase(x, band=(6.0, 9.0), fs=LFP_RATE):
    b, a = signal.butter(3, [band[0] / (fs / 2), band[1] / (fs / 2)], btype="band")
    return np.angle(signal.hilbert(signal.filtfilt(b, a, x.astype(float))))


def _read_channel(lfp, ch, a, b):
    return lfp[a:b, ch].astype(np.float32)


# ----------------------------------------------------------------- session
def load_session(asset: dict, lfp_measures=None, read_lfp=True) -> dict:
    """Reduce one session to what the claims use.

    lfp_measures: optional callable(trial_segments dict) -> dict, run on the
    trial LFP of the CA1, CA3 and LS channels when a session has them.
    """
    path = asset["path"]
    f = open_asset(asset)
    S = {"path": path, "subject": path.split("/")[0].replace("sub-", ""),
         "session": path.split("_ses-")[1].split("_behavior")[0]}
    S["depth"], S["depth2"] = session_depths(path)
    S["description"] = f["session_description"][()].decode()
    S["phase_ref"] = None
    # electrodes
    e = f["general/extracellular_ephys/electrodes"]
    chan = e["channel_id"][:]
    S["elec_region"] = _str(e["region"][:])
    S["elec_site"] = e["shank_electrode_number"][:]
    S["elec_group"] = e["spike_group"][:]
    S["chan"] = {k: chan[e[k + "_channel"][:].astype(bool)].tolist() for k in ("ca1", "ca3", "ls", "theta")}
    # trials
    tr = f["intervals/trials"]
    T = {"start": tr["start_time"][:], "stop": tr["stop_time"][:], "condition": tr["condition"][:]}
    for k in ("condition_type", "trial_type", "direction"):
        T[k] = _str(tr[k][:]) if k in tr else np.array([""] * len(T["start"]))
    T["linpos"] = _ragged(tr, "linearized_position")
    T["lints"] = _ragged(tr, "linearized_position_timestamps")
    order = np.argsort(T["start"])
    for k in list(T):
        T[k] = [T[k][i] for i in order] if isinstance(T[k], list) else T[k][order]
    S["trials"] = T
    S["trials_description"] = str(tr.attrs.get("description", ""))
    tc = f["processing/behavior/trial_conditions"]
    conds = tc["condition"][:]
    tmpl = np.stack([tc[c][:] for c in ("template_x", "template_y", "template_z") if c in tc], -1)
    S["template_points"] = tmpl.shape[1]
    S["template_len"] = {int(c): float(np.nansum(np.linalg.norm(np.diff(tmpl[i], axis=0), axis=1)))
                         for i, c in enumerate(conds)}
    ctype = _str(tc["condition_type"][:]) if "condition_type" in tc else np.array([""] * len(conds))
    S["template_type"] = dict(zip(conds.tolist(), ctype.tolist()))
    # position (speed)
    hp = f["processing/behavior/position/head_position"]
    S["pos_unit"] = hp["data"].attrs["unit"]
    if "starting_time" in hp:
        rate = hp["starting_time"].attrs["rate"]
        t0 = hp["starting_time"][()]
        n = hp["data"].shape[0]
        pt = t0 + np.arange(n) / rate
    else:
        pt = hp["timestamps"][:]
    S["pos_rate"] = float(1 / np.median(np.diff(pt[:1000])))
    a = max(np.searchsorted(pt, T["start"].min() - 1) - 1, 0)
    b = np.searchsorted(pt, T["stop"].max() + 1) + 1
    xyz = hp["data"][a:b, :2].astype(float)
    ptt = pt[a:b]
    # speed from x, y (units per s), smoothed over 0.25 s (S)
    v = np.r_[0, np.linalg.norm(np.diff(xyz, axis=0), axis=1)] * S["pos_rate"]
    k = max(int(round(0.25 * S["pos_rate"])), 1)
    v = np.convolve(np.nan_to_num(v), np.ones(k) / k, mode="same")
    S["speed_t"], S["speed"] = ptt, v.astype(np.float32)
    # units
    if "units" not in f:
        S["units"] = None
        S["n_units_total"] = 0
        f.close()
        return S
    u = f["units"]
    region = _str(u["region"][:])
    n_u = len(region)
    maxch = u["max_waveform_channel"][:] if "max_waveform_channel" in u else np.full(n_u, -1)
    shank = u["shank"][:] if "shank" in u else np.full(n_u, -1)
    st_all = _ragged(u, "spike_times")
    S["n_units_total"] = len(region)
    # trial windows
    starts, stops = T["start"], T["stop"]
    units = []
    for i in range(len(region)):
        st = st_all[i]
        st = st[(st >= starts.min()) & (st <= stops.max())]
        ti = np.searchsorted(starts, st, side="right") - 1
        ok = (ti >= 0) & (st <= stops[np.clip(ti, 0, None)])
        units.append({"region": region[i], "shank": int(shank[i]), "maxch": int(maxch[i]),
                      "site": int(S["elec_site"][np.where(chan == maxch[i])[0][0]]) if (chan == maxch[i]).any() else -1,
                      "t": st[ok], "trial": ti[ok], "n_all": len(st_all[i])})
    S["units"] = units
    # linearized bin and IFR of each in-trial spike
    for U in units:
        lb = np.zeros(len(U["t"]), int)
        lbs = np.full(len(U["t"]), -1)
        ifr = np.zeros(len(U["t"]))
        for j in np.unique(U["trial"]):
            m = U["trial"] == j
            ts, lp = T["lints"][j], T["linpos"][j]
            if len(ts) == 0:
                lb[m] = -1
                continue
            k = np.clip(np.searchsorted(ts, U["t"][m]), 1, len(ts) - 1)
            k = np.where(np.abs(ts[k - 1] - U["t"][m]) < np.abs(ts[k] - U["t"][m]), k - 1, k)
            lb[m] = lp[k] - 1
            # clock check: the bin 1 s later in the same trial (-1 past its end)
            ks = np.searchsorted(ts, U["t"][m] + 1.0)
            ok1 = ks < len(ts)
            bs = np.full(m.sum(), -1)
            bs[ok1] = lp[ks[ok1]] - 1
            lbs[m] = bs
            tt = np.r_[starts[j], U["t"][m], stops[j]]
            isi = np.diff(tt)
            ifr[m] = 1.0 / ((isi[:-1] + isi[1:]) / 2)   # Harris et al. 2003 (P, STAR Methods)
        U["bin"] = lb
        U["bin_shift"] = lbs
        U["ifr"] = ifr
        U["speed"] = np.interp(U["t"], S["speed_t"], S["speed"]) if len(U["t"]) else np.zeros(0)
    # LFP: CA1 theta phase at each spike, and per-trial LFP measures
    if read_lfp:
        lfp = f["processing/ecephys/LFP/lfp/data"]
        a = max(int((starts.min() - 5) * LFP_RATE), 0)
        b = min(int((stops.max() + 5) * LFP_RATE), lfp.shape[0])
        S["lfp_window"] = (a, b)
        segs = {}
        for key in ("ca1", "ca3", "ls"):
            if S["chan"][key]:
                segs[key] = _read_channel(lfp, S["chan"][key][0], a, b)
        # phase reference: the CA1 channel; where none is flagged, the hippocampal
        # probe's theta channel (A: in five DT9 sessions only a CA3 probe was recorded)
        ref = None
        if "ca1" in segs:
            ref, S["phase_ref"] = segs["ca1"], "ca1"
        else:
            th = [c for c in S["chan"]["theta"] if S["elec_region"][np.where(chan == c)[0][0]] in HPC_LABELS]
            if th:
                ref, S["phase_ref"] = _read_channel(lfp, th[0], a, b), "hippocampal theta channel %d" % th[0]
        if ref is not None:
            ph69 = theta_phase(ref, (6, 9))
            ph412 = theta_phase(ref, (4, 12))
            # reference phase at 1 ms steps within each trial (peer prediction covariates)
            S["trial_phase_ms"] = []
            for j in range(len(starts)):
                tt = np.arange(starts[j], stops[j], 0.001)
                kk = np.clip(np.round(tt * LFP_RATE).astype(int) - a, 0, b - a - 1)
                S["trial_phase_ms"].append(ph69[kk].astype(np.float32))
            for U in units:
                k = np.clip(np.round(U["t"] * LFP_RATE).astype(int) - a, 0, b - a - 1)
                U["phase"] = ph69[k].astype(np.float32)
                U["phase412"] = ph412[k].astype(np.float32)
                # clock check: CA1 phase 1 s after each spike
                U["phase_shift"] = ph69[np.clip(k + int(LFP_RATE), 0, b - a - 1)].astype(np.float32)
            del ph69, ph412
        if lfp_measures is not None:
            S["lfp"] = lfp_measures(segs, a, T)
        del segs
    f.close()
    return S


# ----------------------------------------------------------------- maps
def included_conditions(S, unit):
    """Conditions with >= 10 trials in which the unit fires >= 1.5 spikes per trial."""
    T = S["trials"]
    out = []
    for c in np.unique(T["condition"]):
        tid = np.where(T["condition"] == c)[0]
        if len(tid) < MIN_TRIALS:
            continue
        n = np.isin(unit["trial"], tid).sum()
        if n >= MIN_SPIKES_PER_TRIAL * len(tid):
            out.append(int(c))
    return out


def n_bins(S, cond, reading="a"):
    scale = length_scale(S)
    if reading == "a" or not np.isfinite(scale):
        return S["template_points"]
    return max(int(round(S["template_len"][cond] * scale * 100 / CM_PER_BIN)), 10)


def _rebin(idx, npts, nb):
    return np.minimum((idx * nb) // npts, nb - 1)


def occupancy(S, cond, nb):
    T = S["trials"]
    tid = np.where(T["condition"] == cond)[0]
    occ = np.zeros((len(tid), nb))
    for r, j in enumerate(tid):
        lp = T["linpos"][j] - 1
        ts = T["lints"][j]
        if len(ts) < 2:
            continue
        dt = np.median(np.diff(ts))
        np.add.at(occ[r], _rebin(lp, S["template_points"], nb), dt)
    return tid, occ


def box(x, w, axis=-1):
    """Centred moving mean over w bins ignoring NaN; the window shrinks at the edges."""
    x = np.moveaxis(np.asarray(x, float), axis, -1)
    valid = ~np.isnan(x)
    xv = np.where(valid, x, 0.0)
    k = np.ones(w)
    num = np.apply_along_axis(lambda r: np.convolve(r, k, "same"), -1, xv)
    den = np.apply_along_axis(lambda r: np.convolve(r, k, "same"), -1, valid.astype(float))
    with np.errstate(invalid="ignore", divide="ignore"):
        out = num / den
    return np.moveaxis(out, -1, axis)


def box_fast(x, w):
    """box() along the last axis of a 2-D array via cumulative sums."""
    x = np.asarray(x, float)
    valid = ~np.isnan(x)
    xv = np.where(valid, x, 0.0)
    n = x.shape[-1]
    lo = np.arange(n) - (w // 2)
    hi = lo + w
    lo = np.clip(lo, 0, n)
    hi = np.clip(hi, 0, n)
    cs = np.concatenate([np.zeros(x.shape[:-1] + (1,)), np.cumsum(xv, -1)], -1)
    cv = np.concatenate([np.zeros(x.shape[:-1] + (1,)), np.cumsum(valid, -1)], -1)
    num = cs[..., hi] - cs[..., lo]
    den = cv[..., hi] - cv[..., lo]
    with np.errstate(invalid="ignore", divide="ignore"):
        return num / den


def circ_box(ph, w):
    """Circular mean over w bins of the non-empty bins (NaN = empty)."""
    c = box_fast(np.cos(ph), w)
    s = box_fast(np.sin(ph), w)
    out = np.arctan2(s, c)
    out[np.isnan(c)] = np.nan
    return out


def maps(S, unit, cond, reading="a", phase_key="phase"):
    """Raw count, rate and phase maps (trials x bins) of a unit in a condition."""
    nb = n_bins(S, cond, reading)
    tid, occ = occupancy(S, cond, nb)
    rows = {j: r for r, j in enumerate(tid)}
    m = np.isin(unit["trial"], tid) & (unit["bin"] >= 0)
    r = np.array([rows[j] for j in unit["trial"][m]], int)
    b = _rebin(unit["bin"][m], S["template_points"], nb)
    cnt = np.zeros_like(occ)
    np.add.at(cnt, (r, b), 1)
    with np.errstate(invalid="ignore", divide="ignore"):
        rate = np.where(occ > 0, cnt / occ, 0.0)
    ph = unit.get(phase_key)
    cs = np.zeros_like(occ)
    sn = np.zeros_like(occ)
    if ph is not None:
        np.add.at(cs, (r, b), np.cos(ph[m]))
        np.add.at(sn, (r, b), np.sin(ph[m]))
    phase = np.where(cnt > 0, np.arctan2(sn, cs), np.nan)
    return {"tid": tid, "occ": occ, "count": cnt, "rate": rate, "phase": phase, "nb": nb}


# ----------------------------------------------------------------- decoder
def _nearest(template, values, rng=None):
    """Index of the template entry nearest each value (template may hold NaN).

    Ties (several bins whose template value is equally near, as when many bins
    of a rate template are exactly 0 Hz) are broken at random when rng is given
    (A: a tie has no preferred bin; the first-index rule of a MATLAB min/max,
    which sends every tie to the lowest bin, is the variant rng=None)."""
    ok = np.where(~np.isnan(template))[0]
    if len(ok) == 0:
        return np.full(len(values), -1)
    tv = template[ok]
    o = np.argsort(tv, kind="stable")
    sv = tv[o]
    k = np.clip(np.searchsorted(sv, values), 1, len(sv) - 1) if len(sv) > 1 else np.zeros(len(values), int)
    if len(sv) > 1:
        k = np.where(np.abs(sv[k - 1] - values) <= np.abs(sv[k] - values), k - 1, k)
    if rng is not None and len(sv) > 1:
        lo = np.searchsorted(sv, sv[k], side="left")
        hi = np.searchsorted(sv, sv[k], side="right")
        k = lo + (rng.random(len(k)) * (hi - lo)).astype(int)
    return ok[o[k]]


def decode(feat, rng, split="a", n_splits=N_SPLITS, shuffle=False, ties="random"):
    """Maximum correlation decoder on one feature (trials x bins); MSE per split.

    Samples with an undefined feature (NaN; phase in bins without spikes nearby
    under the left-out reading) are left out of training and testing.
    ties: "random" (adopted, A) or "low" (lowest bin, variant); see _nearest.
    """
    ntr, nb = feat.shape
    pos = np.tile(np.arange(nb), (ntr, 1))
    trial = np.repeat(np.arange(ntr)[:, None], nb, 1)
    f = feat.ravel().copy()
    p = pos.ravel()
    t = trial.ravel()
    valid = ~np.isnan(f)
    f, p, t = f[valid], p[valid], t[valid]
    if shuffle:
        f = f[rng.permutation(len(f))]
    out = np.full(n_splits, np.nan)
    if len(f) < 10:
        return out
    for s in range(n_splits):
        if split == "a":
            tr_trials = rng.permutation(ntr)[: int(round(TRAIN_FRAC * ntr))]
            train = np.isin(t, tr_trials)
        else:
            train = np.zeros(len(f), bool)
            train[rng.permutation(len(f))[: int(round(TRAIN_FRAC * len(f)))]] = True
        test = ~train
        if test.sum() == 0 or train.sum() == 0:
            continue
        sums = np.bincount(p[train], f[train], minlength=nb)
        cnts = np.bincount(p[train], minlength=nb)
        with np.errstate(invalid="ignore", divide="ignore"):
            tmpl = np.where(cnts > 0, sums / cnts, np.nan)
        pred = _nearest(tmpl, f[test], rng if ties == "random" else None)
        out[s] = np.mean((pred - p[test]) ** 2)
    return out


def decode_unit(M, rng, split="a", smooth=SMOOTH, fill=0.0, full=False):
    """Rate and phase (cosine of the smoothed phase) MSEs over splits, with the
    phase chance; with full=True also the raw phase, the rate chance, and the
    rate and phase MSEs with ties sent to the lowest bin.

    fill: 0 sets bins whose smoothed phase is undefined (no spike within the
    smoothing window) to phase 0, as a zero-initialised phase map would
    (reading 1, adopted, A); None leaves them out (reading 0). Leaving them out
    lets the phase decoder read where the cell fires: phase shuffled within
    trials still beats chance and rate (the real-data null of the notebook).
    """
    rate = box_fast(M["rate"], smooth)
    ph = circ_box(M["phase"], smooth)
    defined = float(np.mean(~np.isnan(ph)))
    if fill is not None:
        ph = np.where(np.isnan(ph), fill, ph)
    res = {"rate": decode(rate, rng, split), "phase_cos": decode(np.cos(ph), rng, split),
           "chance_phase": decode(np.cos(ph), rng, split, shuffle=True), "phase_defined": defined}
    if full:
        res["phase_raw"] = decode(ph, rng, split)
        res["chance_rate"] = decode(rate, rng, split, shuffle=True)
        res["rate_low"] = decode(rate, rng, split, ties="low")
        res["phase_cos_low"] = decode(np.cos(ph), rng, split, ties="low")
        res["chance_phase_low"] = decode(np.cos(ph), rng, split, shuffle=True, ties="low")
    return res


def shift_phases(U, rng):
    """Copy of the unit whose spike phases are circularly shifted within each
    trial by a random offset (positions and spike times kept): a null with
    the cell's firing positions intact and no phase-position relation."""
    ph = U["phase"].copy()
    for j in np.unique(U["trial"]):
        idx = np.where(U["trial"] == j)[0]
        if len(idx) > 1:
            ph[idx] = np.roll(ph[idx], int(rng.integers(1, len(idx))))
    return dict(U, phase=ph)


def length_scale(S):
    """Metres per stored position unit: 1 for m, 1e-3 for sessions whose 'meters'
    values are millimetres (template paths over 100 units long), NaN for pixels."""
    if S["pos_unit"] != "meters":
        return np.nan
    L = np.median(list(S["template_len"].values()))
    return 1e-3 if L > 100 else 1.0


# readings: split (a whole trials, b pooled samples), bins (a template points,
# b 1.5 cm), undefined phase (1 set to 0, adopted; 0 left out, variant)
READINGS = ["aa1", "ba1", "ab1", "bb1", "aa0", "ba0"]
MAIN = "aa1"
NULL_READINGS = ["aa1", "ba1", "aa0", "ba0", "ab1", "bb1"]
NULL_FRAC = 0.25          # share of hippocampal unit-conditions given the phase-shift null; all LS ones (S)


def analyse_session(S, seed=0, readings=READINGS, info=True):
    """Per unit and included condition: decoders under every reading, place
    fields under both rate-map readings, and information curves. Returns rows."""
    rng = np.random.default_rng(seed)
    rng_null = np.random.default_rng(seed + 500000)
    rng_null_b = np.random.default_rng(seed + 600000)   # 1.5 cm null readings (added in round 2), own stream
    rows = []
    if not S.get("units"):
        return rows
    scale = length_scale(S)
    for ui, U in enumerate(S["units"]):
        if "phase" not in U:
            continue
        U_null = None
        for c in included_conditions(S, U):
            row = {"session": S["session"], "subject": S["subject"], "unit": ui, "region": U["region"],
                   "cond": c, "site": U["site"], "shank": U["shank"]}
            Ms = {}
            for rd in readings:
                split, bins, nan = rd
                if bins not in Ms:
                    Ms[bins] = maps(S, U, c, bins)
                if bins == "b" and Ms["b"]["nb"] == Ms["a"]["nb"]:
                    continue
                r = decode_unit(Ms[bins], rng, split, fill=(None if nan == "0" else 0.0), full=(rd == MAIN))
                for k, v in r.items():
                    row[f"{rd}_{k}"] = v
            M = Ms["a"]
            row["ntrials"] = M["rate"].shape[0]
            row["nbins_b"] = Ms["b"]["nb"] if "b" in Ms else np.nan
            cm_bin = (S["template_len"][c] * scale * 100 / M["nb"]) if np.isfinite(scale) else CM_PER_BIN
            row["cm_per_bin_a"] = cm_bin
            # place fields, rate map readings (a) Gaussian, (b) box 20
            for pr, sm in (("a", gauss_smooth(M["rate"])), ("b", box_fast(M["rate"], SMOOTH))):
                fl = place_fields(sm)
                row[f"pf{pr}_n"] = len(fl)
                if fl:
                    f0 = fl[0]
                    row[f"pf{pr}_peak"] = f0["peak_rate"]
                    row[f"pf{pr}_width"] = f0["width_bins"]
                    row[f"pf{pr}_com"] = f0["com"]
                    row[f"pf{pr}_sd"] = float(np.std(sm[:, f0["peak_bin"]], ddof=1))
                    row[f"pf{pr}_cv"] = 100 * row[f"pf{pr}_sd"] / max(np.mean(sm[:, f0["peak_bin"]]), 1e-12)
                    row[f"pf{pr}_peaks_all"] = [x["peak_rate"] for x in fl]
                    row[f"pf{pr}_widths_all"] = [x["width_bins"] for x in fl]
            is_hpc = U["region"] in HPC_LABELS
            # real-data null on a random share of unit-conditions: spike phases
            # circularly shifted within each trial, decoded under the null readings
            row["null"] = (U["region"] == "ls") or (is_hpc and bool(rng_null.random() < NULL_FRAC))
            Mn = None
            if row["null"]:
                if U_null is None:
                    U_null = shift_phases(U, rng_null)
                Mn = maps(S, U_null, c, "a")
                Mnb = maps(S, U_null, c, "b") if "b" in Ms and Ms["b"]["nb"] != Ms["a"]["nb"] else None
                for rd in NULL_READINGS:
                    MM = Mn if rd[1] == "a" else Mnb
                    if MM is None:
                        continue      # 1.5 cm map with 201 bins: the notebook takes the 201-bin result
                    r = decode_unit(MM, rng_null if rd[1] == "a" else rng_null_b, rd[0], fill=(None if rd[2] == "0" else 0.0))
                    for k in ("rate", "phase_cos", "chance_phase"):
                        row[f"null_{rd}_{k}"] = r[k]
            want = info and ((U["region"] == "ls") or (is_hpc and (row["pfa_n"] > 0 or row["pfb_n"] > 0)))
            if want:
                for mode in ("a", "b"):
                    rc, pc, pc0, pn, pn0 = [], [], [], [], []
                    for w in range(1, 51):
                        rc.append(olypher_peak(box_fast(M["rate"], w), mode=mode))
                        if is_hpc:
                            # phase information: undefined smoothed phase set to 0 (adopted,
                            # as in the decoder), and left out (variant)
                            for MM, a1, a0 in ((M, pc, pc0), (Mn, pn, pn0)):
                                if MM is None:
                                    continue
                                ph = circ_box(MM["phase"], w)
                                a1.append(olypher_peak(np.where(np.isnan(ph), 0.0, ph), mode=mode,
                                                       value_range=(-np.pi, np.pi)))
                                a0.append(olypher_peak(ph, mode=mode, value_range=(-np.pi, np.pi)))
                    row[f"info_rate_{mode}"] = np.array(rc)
                    if is_hpc:
                        row[f"info_phase_{mode}"] = np.array(pc)
                        row[f"info_phase0_{mode}"] = np.array(pc0)
                        if Mn is not None:
                            row[f"null_info_phase_{mode}"] = np.array(pn)
                            row[f"null_info_phase0_{mode}"] = np.array(pn0)
            # first 15 bins of the phase field: spikes and smoothed map (Figure 4E)
            m = np.isin(U["trial"], M["tid"]) & (U["bin"] >= 0) & (U["bin"] < 15)
            row["onset_spikes"] = circ_mean(U["phase"][m]) if m.any() else np.nan
            sm = circ_box(M["phase"], SMOOTH)[:, :15]
            row["onset_map"] = circ_mean(sm[~np.isnan(sm)]) if np.any(~np.isnan(sm)) else np.nan
            # trial-mean maps for Figure 3 (box 20, 201 bins)
            row["mean_rate_map"] = box_fast(M["rate"], SMOOTH).mean(0).astype(np.float32)
            ph = circ_box(M["phase"], SMOOTH)
            with np.errstate(invalid="ignore"):
                row["mean_phase_map"] = np.arctan2(np.nanmean(np.sin(ph), 0), np.nanmean(np.cos(ph), 0)).astype(np.float32)
            rows.append(row)
    return rows


def ttest_less(a, b):
    """Two-sample t test, p-value; True when mean(a) < mean(b)."""
    a, b = a[~np.isnan(a)], b[~np.isnan(b)]
    if len(a) < 2 or len(b) < 2:
        return np.nan, False
    t, p = stats.ttest_ind(a, b)
    return p, np.mean(a) < np.mean(b)


# ----------------------------------------------------------------- place fields
def gauss_smooth(x, sigma=5):
    from scipy.ndimage import gaussian_filter1d
    return gaussian_filter1d(x, sigma, axis=-1, mode="nearest")


def place_fields(rate_trials, cm_per_bin=CM_PER_BIN, min_peak=2.0, pct=0.2,
                 min_cm=8.0, max_cm=120.0):
    """Fields of a trials x bins rate map (already smoothed); list of dicts."""
    mean = np.nanmean(rate_trials, 0)
    sd = np.nanstd(rate_trials, 0)
    nb = len(mean)
    peaks, _ = signal.find_peaks(np.r_[-np.inf, mean, -np.inf])
    peaks = peaks - 1
    fields = []
    seen = set()
    for pk in sorted(peaks, key=lambda i: -mean[i]):
        if mean[pk] < min_peak or mean[pk] < sd[pk]:
            continue
        thr = pct * mean[pk]
        lo = pk
        while lo > 0 and mean[lo - 1] >= thr:
            lo -= 1
        hi = pk
        while hi < nb - 1 and mean[hi + 1] >= thr:
            hi += 1
        if (lo, hi) in seen:      # merged with a higher peak
            continue
        seen.add((lo, hi))
        w = (hi - lo + 1) * cm_per_bin
        if w < min_cm or w > max_cm:
            continue
        seg = mean[lo:hi + 1]
        com = lo + np.sum(seg * np.arange(len(seg))) / np.sum(seg)
        fields.append({"peak_bin": int(pk), "peak_rate": float(mean[pk]), "start": lo, "stop": hi,
                       "width_bins": hi - lo + 1, "com": float(com)})
    return fields


# ----------------------------------------------------------------- information
def olypher_peak(values, levels=7, mode="a", value_range=None):
    """Peak over bins of the Olypher information (bits) of trials x bins values."""
    v = values.copy()
    ok = ~np.isnan(v)
    if ok.sum() < 2:
        return np.nan
    if mode == "a":
        lo, hi = value_range if value_range is not None else (np.nanmin(v), np.nanmax(v))
        if hi <= lo:
            return 0.0
        k = np.clip(np.floor((np.where(ok, v, lo) - lo) / (hi - lo) * levels), 0, levels - 1).astype(int)
    else:
        q = np.nanquantile(v, np.linspace(0, 1, levels + 1)[1:-1])
        k = np.searchsorted(q, np.where(ok, v, 0), side="right")
    nb = v.shape[1]
    onehot = np.zeros((levels,) + v.shape)
    for L in range(levels):
        onehot[L] = (k == L) & ok
    pkx = onehot.sum(1) / np.maximum(ok.sum(0), 1)          # levels x bins
    pk = onehot.sum((1, 2)) / ok.sum()
    with np.errstate(divide="ignore", invalid="ignore"):
        term = np.where(pkx > 0, pkx * np.log2(pkx / pk[:, None]), 0.0)
    info = term.sum(0)
    info[ok.sum(0) == 0] = np.nan
    return float(np.nanmax(info))


def matlab_smooth(y, span=5):
    """MATLAB smooth(y, span): moving mean whose span shrinks symmetrically at
    the ends (1, 3, ... points), so the ends are not pulled towards zero (S:
    the default of the function makeFig1.m names; a zero-padded convolution
    pulls the last points down)."""
    y = np.asarray(y, float)
    n = len(y)
    h = span // 2
    out = np.empty(n)
    for i in range(n):
        r = min(h, i, n - 1 - i)
        out[i] = np.mean(y[i - r:i + r + 1])
    return out


def best_scale(curve):
    """Smoothing (1-based bins) of the peak of the 5-point smoothed information curve."""
    c = matlab_smooth(np.nan_to_num(np.asarray(curve, float)), 5)
    return int(np.argmax(c)) + 1


# ----------------------------------------------------------------- circular stats
def circ_kappa(R):
    """CircStat circ_kappa (no small-sample correction)."""
    if R < 0.53:
        return 2 * R + R ** 3 + 5 * R ** 5 / 6
    if R < 0.85:
        return -0.4 + 1.39 * R + 0.43 / (1 - R)
    return 1 / (R ** 3 - 4 * R ** 2 + 3 * R)


def circ_wwtest(groups):
    """CircStat circ_wwtest (Watson-Williams), one array of angles per group.
    Returns p, F and the pooled resultant length rw (the test assumes rw > 0.45)."""
    alpha = np.concatenate(groups)
    n, s = len(alpha), len(groups)
    pn = np.array([len(g) for g in groups], float)
    pr = np.array([np.abs(np.mean(np.exp(1j * g))) for g in groups])
    r = np.abs(np.mean(np.exp(1j * alpha)))
    rw = np.sum(pn * pr) / n
    kk = circ_kappa(rw)
    beta = 1 + 3 / (8 * kk)
    A = np.sum(pr * pn) - r * n
    B = n - np.sum(pr * pn)
    F = beta * (n - s) * A / (s - 1) / B
    return float(stats.f.sf(F, s - 1, n - s)), float(F), float(rw)
def circ_corrcl(alpha, x):
    """CircStat circ_corrcl: circular-linear correlation and its p-value."""
    alpha = np.asarray(alpha, float)
    x = np.asarray(x, float)
    n = len(alpha)
    rxs = np.corrcoef(x, np.sin(alpha))[0, 1]
    rxc = np.corrcoef(x, np.cos(alpha))[0, 1]
    rcs = np.corrcoef(np.sin(alpha), np.cos(alpha))[0, 1]
    rho = np.sqrt((rxc ** 2 + rxs ** 2 - 2 * rxc * rxs * rcs) / (1 - rcs ** 2))
    pval = 1 - stats.chi2.cdf(n * rho ** 2, 2)
    return rho, pval


def circ_mean(a):
    return float(np.angle(np.mean(np.exp(1j * np.asarray(a)))))


# ----------------------------------------------------------------- Figure 6 LFP measures
def _bp(x, lo, hi, fs=LFP_RATE, order=3):
    b, a = signal.butter(order, [lo / (fs / 2), hi / (fs / 2)], btype="band")
    return signal.filtfilt(b, a, x.astype(float))


def mt_coherence(x, y, win=int(0.150 * LFP_RATE), step=int(0.050 * LFP_RATE), band=(4, 12),
                 NW=3, K=5, fs=LFP_RATE):
    """Multitaper coherence in sliding windows, averaged over the band (chronux
    cohgramc with tapers [3 5], as bz_MTCoherogram; S for NW, K and the padding)."""
    n = len(x)
    starts = np.arange(0, n - win + 1, step)
    if len(starts) == 0:
        return np.zeros(0)
    tapers = signal.windows.dpss(win, NW, K)
    nfft = int(2 ** np.ceil(np.log2(win)))
    freqs = np.fft.rfftfreq(nfft, 1 / fs)
    fb = (freqs >= band[0]) & (freqs <= band[1])
    idx = starts[:, None] + np.arange(win)[None, :]
    X = np.fft.rfft(tapers[None] * (x[idx] - x[idx].mean(1, keepdims=True))[:, None, :], nfft)[..., fb]
    Y = np.fft.rfft(tapers[None] * (y[idx] - y[idx].mean(1, keepdims=True))[:, None, :], nfft)[..., fb]
    s12 = (X * Y.conj()).mean(1)
    s11 = (np.abs(X) ** 2).mean(1)
    s22 = (np.abs(Y) ** 2).mean(1)
    return (np.abs(s12) / np.sqrt(s11 * s22)).mean(-1)


def _roll_mean(x, half):
    n = len(x)
    cs = np.r_[0, np.cumsum(x)]
    lo = np.clip(np.arange(n) - half, 0, n)
    hi = np.clip(np.arange(n) + half + 1, 0, n)
    return (cs[hi] - cs[lo]) / (hi - lo)


def rolling_corrcl(phase, x, half=250):
    """circ_corrcl of phase and x in windows of +/- half samples, moved sample by sample."""
    s, c = np.sin(phase), np.cos(phase)
    m = {k: _roll_mean(v, half) for k, v in
         {"x": x, "s": s, "c": c, "xx": x * x, "ss": s * s, "cc": c * c, "xs": x * s, "xc": x * c, "sc": s * c}.items()}

    def corr(a, b, ab, aa, bb):
        with np.errstate(invalid="ignore", divide="ignore"):
            return (m[ab] - m[a] * m[b]) / np.sqrt((m[aa] - m[a] ** 2) * (m[bb] - m[b] ** 2))
    rxs = corr("x", "s", "xs", "xx", "ss")
    rxc = corr("x", "c", "xc", "xx", "cc")
    rcs = corr("s", "c", "sc", "ss", "cc")
    with np.errstate(invalid="ignore", divide="ignore"):
        return np.sqrt(np.clip((rxc ** 2 + rxs ** 2 - 2 * rxc * rxs * rcs) / (1 - rcs ** 2), 0, None))


def rms_power(x, win):
    return np.sqrt(np.convolve(x * x, np.ones(win) / win, "same"))


def _resample_z(curve, npts=1000):
    if len(curve) < 2 or np.all(np.isnan(curve)):
        return None, np.nan
    xi = np.linspace(0, 1, npts)
    r = np.interp(xi, np.linspace(0, 1, len(curve)), curve)
    sd = np.nanstd(r)
    return ((r - np.nanmean(r)) / sd if sd > 0 else r * 0).astype(np.float32), float(np.nanmean(curve))


def fig6_lfp_measures(segs, a, T):
    """Per trial (> 0.8 s), CA1-LS and CA3-LS theta phase coherence and theta-gamma coupling.

    STAR Methods (LFP theta phase coherence; cross-frequency coupling) and the
    claims' criteria (makeFig6.m): 4-12 Hz 3rd-order Butterworth, Hilbert angle;
    150 ms windows moved by 50 ms; LS gamma RMS in 50 ms windows of the 40-200 Hz
    band (variant 50-500 Hz, 60-sample window); circ_corrcl in +/- 250 samples;
    each trial resampled to 1000 points and z-scored.
    """
    if "ls" not in segs:
        return None
    out = {}
    ls_ph = np.angle(signal.hilbert(_bp(segs["ls"], 4, 12)))
    g1 = rms_power(_bp(segs["ls"], 40, 200), int(0.050 * LFP_RATE))
    g2 = rms_power(_bp(segs["ls"], 50, 500), 60)
    for reg in ("ca1", "ca3"):
        if reg not in segs:
            continue
        ph = np.angle(signal.hilbert(_bp(segs[reg], 4, 12)))
        rows = []
        for j in range(len(T["start"])):
            i0 = int(T["start"][j] * LFP_RATE) - a
            i1 = int(T["stop"][j] * LFP_RATE) - a
            if i1 - i0 < 1000 or i0 < 0 or i1 > len(ph):
                continue
            coh = mt_coherence(ph[i0:i1], ls_ph[i0:i1])
            cfc = rolling_corrcl(ph[i0:i1], g1[i0:i1])
            cfc2 = rolling_corrcl(ph[i0:i1], g2[i0:i1])
            zc, mc = _resample_z(coh)
            zf, mf = _resample_z(cfc)
            zf2, mf2 = _resample_z(cfc2)
            rows.append({"trial": j, "coh_z": zc, "coh_mean": mc, "cfc_z": zf, "cfc_mean": mf,
                         "cfc2_z": zf2, "cfc2_mean": mf2})
        out[reg] = rows
    return out


# ----------------------------------------------------------------- Figure S2: rate and phase
def _corrcl_rows(alpha, x):
    """circ_corrcl of each row of alpha (k x n) with x (n,), vectorised."""
    def cr(a, b):
        a = a - a.mean(-1, keepdims=True)
        b = b - b.mean(-1, keepdims=True)
        with np.errstate(invalid="ignore", divide="ignore"):
            return (a * b).sum(-1) / np.sqrt((a * a).sum(-1) * (b * b).sum(-1))
    s, c = np.sin(alpha), np.cos(alpha)
    xx = np.broadcast_to(x, alpha.shape)
    rxs, rxc, rcs = cr(xx, s), cr(xx, c), cr(s, c)
    with np.errstate(invalid="ignore", divide="ignore"):
        return np.sqrt(np.clip((rxc ** 2 + rxs ** 2 - 2 * rxc * rxs * rcs) / (1 - rcs ** 2), 0, None))


def ifr_phase_condition(S, U, cond, rng, n_shuffles=100, min_spikes=5):
    """Per trial, circ_corrcl of spike phase with instantaneous rate, and the same
    after circularly shifting the rate series by random offsets (STAR Methods,
    instantaneous firing rate and firing phase independence). Trials with fewer
    than 5 spikes are skipped (S)."""
    tid = np.where(S["trials"]["condition"] == cond)[0]
    act, sh = [], []
    for j in tid:
        m = U["trial"] == j
        n = m.sum()
        if n < min_spikes:
            continue
        ph = U["phase"][m].astype(float)
        x = U["ifr"][m]
        act.append(_corrcl_rows(ph[None], x)[0])
        offs = rng.integers(1, n, n_shuffles)
        idx = (np.arange(n)[None, :] + offs[:, None]) % n
        sh.append(_corrcl_rows(ph[idx], x))
    if not act:
        return None
    return np.array(act), np.array(sh)       # trials, trials x shuffles


# ----------------------------------------------------------------- running speed
def circ_lin_slope(phase, x, slopes=np.linspace(-2, 2, 201)):
    """Slope (cycles per unit x) maximising the mean resultant length of
    phase - 2 pi a x (Kempter et al. 2012; S)."""
    R = np.abs(np.exp(1j * (phase[None, :] - 2 * np.pi * slopes[:, None] * x[None, :])).mean(1))
    return slopes[np.argmax(R)]


def speed_precession_condition(S, U, cond, rng, n_shuffles=100, min_spikes=5):
    """Per trial: mean running speed, and the precession rate as (a) the
    circular-linear regression slope of phase on position (track fraction) and
    (b) circ_corrcl of phase and position; their Pearson r over trials, against
    100 trial-order shuffles of speed (claim's criterion)."""
    T = S["trials"]
    tid = np.where(T["condition"] == cond)[0]
    sp, sa, sb = [], [], []
    for j in tid:
        m = (U["trial"] == j) & (U["bin"] >= 0)
        if m.sum() < min_spikes:
            continue
        ms = (S["speed_t"] >= T["start"][j]) & (S["speed_t"] <= T["stop"][j])
        if not ms.any():
            continue
        x = U["bin"][m] / S["template_points"]
        ph = U["phase"][m].astype(float)
        sp.append(np.nanmean(S["speed"][ms]))
        sa.append(circ_lin_slope(ph, x))
        sb.append(circ_corrcl(ph, x)[0])
    if len(sp) < 5:
        return None
    sp, out = np.array(sp), {}

    def test(spv, v):
        if np.std(v) == 0 or np.std(spv) == 0:
            return (np.nan, np.nan)
        r = np.corrcoef(spv, v)[0, 1]
        null = np.array([np.corrcoef(spv[rng.permutation(len(spv))], v)[0, 1] for _ in range(n_shuffles)])
        null = null[np.isfinite(null)]
        if len(null) < 10 or null.std() == 0:
            return (r, np.nan)
        # two-sample t test of one value against the shuffles (pooled variance)
        t = (r - null.mean()) / (null.std(ddof=1) * np.sqrt(1 + 1 / len(null)))
        return (r, 2 * stats.t.sf(abs(t), len(null) - 1))
    for key, v in (("a", np.array(sa)), ("b", np.array(sb))):
        out[key] = test(sp, v)
        # calibration: the same test with speed first permuted over trials (no relation)
        out[key + "_null"] = test(sp[rng.permutation(len(sp))], v)
    return out


def rate_speed_condition(S, U, cond, rng, n_shuffles=100, bin_s=0.1):
    """(a) Pearson r of each spike's instantaneous rate with running speed at the
    spike, against 100 circular shifts of speed; (b) the same on 100 ms bins of
    count and speed. Returns (r, p) per reading, p the fraction of shifts with
    |r| at least as large (claim's criterion)."""
    T = S["trials"]
    tid = np.where(T["condition"] == cond)[0]
    ms = np.zeros(len(S["speed_t"]), bool)
    for j in tid:
        ms |= (S["speed_t"] >= T["start"][j]) & (S["speed_t"] <= T["stop"][j])
    st, sv = S["speed_t"][ms], S["speed"][ms].astype(float)
    if len(st) < 20:
        return None
    m = np.isin(U["trial"], tid)
    out = {}
    k = np.clip(np.searchsorted(st, U["t"][m]), 0, len(st) - 1)
    ifr = U["ifr"][m]
    if len(k) > 10 and np.std(ifr) > 0:
        r = np.corrcoef(ifr, sv[k])[0, 1]
        offs = rng.integers(1, len(st), n_shuffles)
        null = np.array([np.corrcoef(ifr, sv[(k + o) % len(st)])[0, 1] for o in offs])
        out["a"] = (r, float(np.mean(np.abs(null) >= abs(r))))
    # 100 ms bins
    cnt, spd = [], []
    for j in tid:
        edges = np.arange(T["start"][j], T["stop"][j], bin_s)
        if len(edges) < 2:
            continue
        cnt.append(np.histogram(U["t"][U["trial"] == j], edges)[0])
        spd.append(np.interp(edges[:-1] + bin_s / 2, S["speed_t"], S["speed"]))
    if cnt:
        c, s_ = np.concatenate(cnt).astype(float), np.concatenate(spd)
        if np.std(c) > 0:
            r = np.corrcoef(c, s_)[0, 1]
            offs = rng.integers(1, len(c), n_shuffles)
            null = np.array([np.corrcoef(c, np.roll(s_, o))[0, 1] for o in offs])
            out["b"] = (r, float(np.mean(np.abs(null) >= abs(r))))
    return out


# ----------------------------------------------------------------- Figure S7: ensembles
def ensemble_features(S, units, cond, feature):
    """Per unit, the box-20 smoothed rate or phase map (trials x bins), discretized
    into 20 levels (STAR Methods, ensemble position prediction); NaN where the
    phase is undefined."""
    out = []
    for U in units:
        M = maps(S, U, cond, "a")
        if feature == "rate":
            v = box_fast(M["rate"], SMOOTH)
            lo, hi = np.nanmin(v), np.nanmax(v)
        else:
            v = circ_box(M["phase"], SMOOTH)
            lo, hi = -np.pi, np.pi
        lev = np.floor((v - lo) / max(hi - lo, 1e-12) * 20)
        lev = np.clip(lev, 0, 19)
        out.append(lev)
    return np.stack(out, -1)         # trials x bins x units


def bayes_decode(L, rng, n_splits=N_SPLITS):
    """Naive Bayes with Poisson likelihoods whose means are the training mean
    level per unit and position; 60/40 splits of trials; mean MSE (bins^2).
    Undefined values drop the unit's term for that sample (A)."""
    ntr, nb, nu = L.shape
    pos = np.arange(nb)
    mse = []
    for _ in range(n_splits):
        perm = rng.permutation(ntr)
        ntrain = int(round(TRAIN_FRAC * ntr))
        tr, te = perm[:ntrain], perm[ntrain:]
        if len(te) == 0:
            continue
        lam = np.nanmean(L[tr], 0)                     # bins x units
        lam = np.where(np.isnan(lam), np.nanmean(lam), lam) + 0.01   # S: floor of 0.01
        X = L[te].reshape(-1, nu)
        mask = ~np.isnan(X)
        Xz = np.where(mask, X, 0)
        ll = Xz @ np.log(lam).T - mask @ lam.T             # samples x bins
        pred = np.argmax(ll, 1)
        true = np.tile(pos, len(te))
        mse.append(np.mean((pred - true) ** 2))
    return float(np.mean(mse))


# ----------------------------------------------------------------- Figure 5: cost of one pair
def peer_prediction_cost(n_samples, windows=150, shuffles=10, rng=None):
    """Seconds for the GLM fits of one pair: one normal-distribution GLM (least
    squares, the cheapest family the claim allows) on n_samples 1 ms bins with
    the predictor and the six covariates, times windows x (1 + shuffles). The
    inputs are random arrays of the right size: this measures cost only."""
    rng = rng or np.random.default_rng(0)
    X = np.column_stack([np.ones(n_samples), rng.random((n_samples, 7))])
    y = rng.random(n_samples)
    t = time.perf_counter()
    reps = 5
    for _ in range(reps):
        pred = np.convolve(rng.random(n_samples), np.ones(21) / 21, "same")
        X[:, 1] = pred
        beta, *_ = np.linalg.lstsq(X, y, rcond=None)
        float(np.sum((y - X @ beta) ** 2))
    per_fit = (time.perf_counter() - t) / reps
    return per_fit * windows * (1 + shuffles), per_fit


# ----------------------------------------------------------------- Figure 5: peer prediction
PP_WINDOWS = np.arange(1, 151)   # half-widths in ms, 1 to 150 (C, bz_peerPrediction)
PP_SHUFFLES = 10                 # trial-order shuffles (C)


def _ms_trains(S, U, j, n):
    """Spike counts of unit U in 1 ms bins of trial j (n bins)."""
    t0 = S["trials"]["start"][j]
    st = U["t"][U["trial"] == j]
    k = np.floor((st - t0) * 1000).astype(int)
    k = k[(k >= 0) & (k < n)]
    return np.bincount(k, minlength=n).astype(float)


def _covariates(S, j, n):
    """Intercept, CA1 theta phase (sine, cosine, angle), linearized position and
    speed at 1 ms steps of trial j (STAR Methods, peer prediction)."""
    T = S["trials"]
    tt = T["start"][j] + np.arange(n) / 1000.0
    ph = S["trial_phase_ms"][j][:n].astype(float)
    ts, lp = T["lints"][j], T["linpos"][j]
    pos = np.interp(tt, ts, lp.astype(float)) if len(ts) else np.zeros(n)
    vel = np.interp(tt, S["speed_t"], S["speed"].astype(float))
    if np.isfinite(length_scale(S)):
        vel = vel * length_scale(S)
    return np.column_stack([np.ones(n), np.sin(ph), np.cos(ph), ph, pos / 200.0, vel])


def _smoothed(x, windows=PP_WINDOWS):
    """x box-smoothed over +/- w bins for every w (n x len(windows)); the window
    shrinks at the ends (bz_peerPrediction averages over +/- w ms)."""
    n = len(x)
    cs = np.r_[0.0, np.cumsum(x)]
    t = np.arange(n)[:, None]
    lo = np.clip(t - windows[None, :], 0, n)
    hi = np.clip(t + windows[None, :] + 1, 0, n)
    return (cs[hi] - cs[lo]) / (hi - lo)


def _dev_windows(C, y, X):
    """Residual sum of squares (normal-GLM deviance) of y on [C, X[:, w]] for every w."""
    G = C.T @ C
    try:
        Gi = np.linalg.inv(G)
    except np.linalg.LinAlgError:
        Gi = np.linalg.pinv(G)
    Cy = C.T @ y
    CX = C.T @ X
    base = y @ y - Cy @ Gi @ Cy
    rxy = X.T @ y - CX.T @ (Gi @ Cy)
    rxx = np.einsum("ij,ij->j", X, X) - np.einsum("ij,ij->j", CX, Gi @ CX)
    with np.errstate(invalid="ignore", divide="ignore"):
        red = np.where(rxx > 1e-12, rxy ** 2 / rxx, 0.0)
    return base - red


def peer_prediction_pair(S, Uh, Ul, cond, rng, shuffles=PP_SHUFFLES):
    """Peer prediction of an LS unit (response) by a hippocampal unit (predictor)
    over the trials of one condition (STAR Methods, peer prediction; claim
    criterion). A normal GLM (least squares) per trial and window, with the
    covariates of _covariates; deviance summed over trials per window. The
    control pairs the predictor of one trial with the response (and covariates)
    of another, in a random trial order, 10 times; trials of unequal length are
    cut to the shorter (A). Strength as makeFig5.m: (mean - min) of the actual
    deviance curve over (mean - min) of the mean control curve."""
    tid = np.where(S["trials"]["condition"] == cond)[0]
    lens = [len(S["trial_phase_ms"][j]) for j in tid]
    Cs = [_covariates(S, j, n) for j, n in zip(tid, lens)]
    ys = [_ms_trains(S, Ul, j, n) for j, n in zip(tid, lens)]
    xs = [_ms_trains(S, Uh, j, n) for j, n in zip(tid, lens)]
    Xs = [_smoothed(x) for x in xs]
    dev = sum(_dev_windows(C, y, X) for C, y, X in zip(Cs, ys, Xs))
    ctrl = []
    for _ in range(shuffles):
        perm = rng.permutation(len(tid))
        d = 0.0
        for i, k in enumerate(perm):
            m = min(lens[i], lens[k])
            d = d + _dev_windows(Cs[k][:m], ys[k][:m], Xs[i][:m])
        ctrl.append(d)
    ctrl = np.array(ctrl)
    mc = ctrl.mean(0)
    red_a = dev.mean() - dev.min()
    red_c = mc.mean() - mc.min()
    return {"strength": float(red_a / red_c) if red_c > 0 else np.nan,
            "best_w": int(PP_WINDOWS[np.argmin(dev)]), "best_idx": int(np.argmin(dev)) + 1,
            "mean_dev": float(dev.mean()), "ntrials": len(tid),
            "spikes_h": int(sum(x.sum() for x in xs)), "spikes_l": int(sum(y.sum() for y in ys))}


def peer_session(S, picks, seed=0):
    """peer_prediction_pair for the sampled (LS unit, condition) picks of a
    session, against every hippocampal unit included in the same condition."""
    rng = np.random.default_rng(seed)
    out = []
    if not S.get("units") or "trial_phase_ms" not in S:
        return out
    for ul, c in picks:
        Ul = S["units"][ul]
        for uh, Uh in enumerate(S["units"]):
            if Uh["region"] not in HPC_LABELS or c not in included_conditions(S, Uh):
                continue
            r = peer_prediction_pair(S, Uh, Ul, c, rng)
            r.update({"session": S["session"], "subject": S["subject"], "ls": ul, "hpc": uh, "cond": c,
                      "region": Uh["region"]})
            out.append(r)
    return out


def speed_session(S, seed=0):
    """speed_precession_condition and rate_speed_condition for every included LS condition."""
    rng = np.random.default_rng(seed)
    rows = []
    if not S.get("units"):
        return rows
    for ui, U in enumerate(S["units"]):
        if U["region"] != "ls" or "phase" not in U:
            continue
        for c in included_conditions(S, U):
            a = speed_precession_condition(S, U, c, rng)
            b = rate_speed_condition(S, U, c, rng)
            rows.append({"session": S["session"], "subject": S["subject"], "unit": ui, "cond": c,
                         "prec": a, "ratespeed": b})
    return rows


def ifr_session(S, seed=0, regions=("ls",) + HPC_LABELS):
    """ifr_phase_condition for every included condition; per row the mean actual
    and the shuffled correlations summarised."""
    rng = np.random.default_rng(seed)
    rows = []
    if not S.get("units"):
        return rows
    for ui, U in enumerate(S["units"]):
        if U["region"] not in regions or "phase" not in U:
            continue
        for c in included_conditions(S, U):
            r = ifr_phase_condition(S, U, c, rng)
            if r is None:
                continue
            act, sh = r
            pa = stats.ttest_ind(act, sh.mean(1))
            rows.append({"session": S["session"], "subject": S["subject"], "unit": ui, "cond": c,
                         "region": U["region"], "ntr": len(act), "mean_act": float(act.mean()),
                         "mean_sh": float(sh.mean()), "t_p": float(pa.pvalue), "t_stat": float(pa.statistic),
                         "pct95": float(np.quantile(sh.mean(0), 0.95))})
    return rows


def ensemble_session(S, seed=0, draws=3):
    """Naive Bayes ensemble decoding (Figure S7) for every condition with >= 15 included
    units of a region, sizes 15-25: reading (b) one ensemble per size (all units at the
    largest), reading (a) `draws` random ensembles per size."""
    rng = np.random.default_rng(seed)
    out = []
    if not S["units"]:
        return out
    for c in np.unique(S["trials"]["condition"]):
        for reg, labels in (("LS", ("ls",)), ("HPC", HPC_LABELS)):
            us = [U for U in S["units"] if U["region"] in labels and "phase" in U and c in included_conditions(S, U)]
            if len(us) < 15:
                continue
            feats = {"phase": ensemble_features(S, us, c, "phase")}
            if reg == "HPC":
                feats["rate"] = ensemble_features(S, us, c, "rate")
            for size in range(15, min(25, len(us)) + 1):
                for reading, ndraw in (("b", 1), ("a", draws)):
                    for d in range(ndraw):
                        idx = np.arange(len(us)) if size == len(us) and reading == "b" else rng.choice(len(us), size, replace=False)
                        for fk, F in feats.items():
                            out.append({"session": S["session"], "cond": int(c), "region": reg, "feature": fk, "size": size,
                                        "reading": reading, "mse": bayes_decode(F[..., idx], rng)})
    return out
