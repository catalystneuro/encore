"""Loading and measures for Grosmark & Buzsaki (2016), Science 351:1440, on DANDI:000044 and CRCNS hc-11.

Where each parameter comes from:

- "claims": the criterion of a claim in claims/grosmark-2016.yaml, which cites the paper.
- "Methods": the paper's supplementary Materials and Methods, cited by section.
- "assumption": a choice the paper leaves open; the notebook says what it is and why.
- "standard": a choice that cannot change an outcome (a smoothing epsilon, a plotting bin).

Data sources. Spike times, unit ids, putative cell types, position and the lab's state epochs come
from the CRCNS sessInfo files (NoveltySessInfoMatFiles.tar.gz, streamed). The NWB files of
DANDI:000044 hold the same units and states (checked in the notebook) and are the source of the LFP
used to detect sharp wave-ripples and of the lab's lap directions (trials).
"""

from __future__ import annotations

import io
import tarfile

import fsspec
import h5py
import numpy as np
import numba
import remfile
import requests
from scipy import ndimage, signal, stats

DANDISET = "000044"
DANDI_VERSION = "0.261106.0236"
CRCNS = "hc-11"
CRCNS_VERSION = "unversioned"   # CRCNS data sets are not versioned (docs/archives.md)
CRCNS_BASE = "https://crcnsarchive.s3-us-west-2.amazonaws.com/hc-11/live/"
SESSINFO_TAR = CRCNS_BASE + "data/NoveltySessInfoMatFiles.tar.gz"

# Methods, Place Field Analysis
BIN_CM = 2.0            # 2 cm position bins
SMOOTH_CM = 5.0         # 5 cm Gaussian kernel, read as its SD (claims, opening comment)
RUN_SPEED = 0.05        # m/s, running at 5 cm/s or more
N_PF_NULL = 5000        # null rate vectors
PF_MIN_BINS = 5         # consecutive bins above the null 99th percentile
PF_MIN_PEAK = 1.0       # Hz, in-field peak
# Methods, Ripple Event Detection
POP_SD_MS = 15.0        # Gaussian kernel of the population rate, read as SD (claims)
POP_Z = 3.0             # trigger at mean + 3 SD of the NREM 1 ms bins
EV_MIN, EV_MAX = 0.05, 0.5
EV_MIN_PYR = 5
RIPPLE_BAND = (150.0, 250.0)   # Figure S4 legend
# Methods, Bayesian Replay Analysis
DEC_BIN = 0.02
REPLAY_MIN_DUR = 0.1
N_SHUF = 1000          # Methods; the notebook uses fewer for time (see N_NULL, N_PCC)
N_NULL = 200           # null templates per event used here (deviation: the paper uses 1,000)
N_PCC = 100            # cell-specific shuffles per cell and event used here (deviation: paper 1,000)
EPS_RATE = 1e-3         # Hz added to rate maps before the log (standard: avoids log 0)
POS_SMOOTH_S = 0.1      # s, Gaussian SD for smoothing the tracked position before speed (standard)


# ----------------------------------------------------------------------------- loading

def _mat_str(a):
    return bytes(np.array(a).ravel().astype("uint8")).decode()


def _parse_sessinfo(raw: bytes) -> dict:
    f = h5py.File(io.BytesIO(raw), "r")
    S = f["sessInfo/Spikes"]
    P = f["sessInfo/Position"]
    E = f["sessInfo/Epochs"]
    st = np.array(S["SpikeTimes"]).ravel()
    sid = np.array(S["SpikeIDs"]).ravel().astype(int)
    out = {
        "pyr_ids": np.array(S["PyrIDs"]).ravel().astype(int),
        "int_ids": np.array(S["IntIDs"]).ravel().astype(int),
        "maze": _mat_str(P["MazeType"]),
        "pos_t": np.array(P["TimeStamps"]).ravel(),
        "pos_1d": np.array(P["OneDLocation"]).ravel(),
        "pos_2d": np.array(P["TwoDLocation"]).T,
        "epochs": {k: np.array(E[k]).T.reshape(-1, 2) for k in ["PREEpoch", "MazeEpoch", "POSTEpoch"]},
        "states": {k: np.array(E[k]).T.reshape(-1, 2) for k in ["Wake", "Drowsy", "NREM", "Intermediate", "REM"]
                   if k in E and np.array(E[k]).size >= 2},
        "duration": float(np.array(E["sessDuration"]).ravel()[0]),
    }
    order = np.argsort(sid, kind="stable")
    sid, st = sid[order], st[order]
    uids, starts = np.unique(sid, return_index=True)
    ends = np.r_[starts[1:], len(sid)]
    out["spikes"] = {int(u): np.sort(st[a:b]) for u, a, b in zip(uids, starts, ends)}
    out["spike_ids_all"] = uids
    out["n_spikes_total"] = len(st)
    out["unsorted_units"] = int(sum(np.any(np.diff(st[a:b]) < 0) for a, b in zip(starts, ends)))
    f.close()
    return out


def load_crcns_sessions() -> dict:
    """Stream NoveltySessInfoMatFiles.tar.gz from the CRCNS bucket and parse each session's sessInfo."""
    sessions = {}
    with fsspec.open(SESSINFO_TAR, block_size=2**22).open() as fh:
        tf = tarfile.open(fileobj=fh, mode="r|gz")
        for m in tf:
            if m.isfile() and m.name.endswith("_sessInfo.mat"):
                name = m.name.split("/")[-1].replace("_sessInfo.mat", "")
                sessions[name] = _parse_sessinfo(tf.extractfile(m).read())
    return dict(sorted(sessions.items()))


def dandi_assets() -> list[dict]:
    url = f"https://api.dandiarchive.org/api/dandisets/{DANDISET}/versions/{DANDI_VERSION}/assets/?page_size=200"
    return requests.get(url, timeout=60).json()["results"]


def dandi_url(asset_id: str) -> str:
    return requests.head(f"https://api.dandiarchive.org/api/assets/{asset_id}/download/",
                         allow_redirects=True, timeout=60).url


def open_nwb(asset_id: str) -> h5py.File:
    return h5py.File(remfile.File(dandi_url(asset_id)), "r")


def _dec(a):
    return np.array([x.decode() if isinstance(x, bytes) else x for x in a])


def read_nwb_meta(f: h5py.File) -> dict:
    """Units, states, epochs and trials of one NWB file (no LFP)."""
    u = f["units"]
    idx = u["spike_times_index"][:]
    st = u["spike_times"]
    starts = np.r_[0, idx[:-1]]
    spikes = {}
    allst = st[:]
    for i, (a, b) in enumerate(zip(starts, idx)):
        spikes[int(u["id"][i])] = allst[a:b]
    out = {
        "unit_ids": u["id"][:], "cell_type": _dec(u["cell_type"][:]), "spike_group": u["spike_group"][:],
        "spikes": spikes,
        "epochs": dict(zip(_dec(f["intervals/epochs/label"][:]),
                           zip(f["intervals/epochs/start_time"][:], f["intervals/epochs/stop_time"][:]))),
        "subject": f["general/subject/subject_id"][()].decode(),
        "session_id": f["general/session_id"][()].decode(),
    }
    for key in ["sleep_states", "sleep_states_buzcode"]:
        g = f[f"processing/behavior/{key}"]
        out[key] = (_dec(g["label"][:]), g["start_time"][:], g["stop_time"][:])
    if "intervals/trials" in f:
        t = f["intervals/trials"]
        out["trials"] = (_dec(t["direction"][:]), t["start_time"][:], t["stop_time"][:])
    lfp = f["processing/ecephys/LFP/lfp"]
    out["lfp_shape"] = lfp["data"].shape
    out["lfp_rate"] = float(lfp["starting_time"].attrs["rate"])
    out["lfp_conversion"] = float(lfp["data"].attrs["conversion"])
    el = f["general/extracellular_ephys/electrodes"]
    out["electrode_group"] = el["spike_group"][:]
    out["bad_electrode"] = el["bad_electrode"][:]
    return out


# ----------------------------------------------------------------------------- intervals

def merge_intervals(iv):
    iv = np.asarray(iv, float).reshape(-1, 2)
    if len(iv) == 0:
        return iv
    iv = iv[np.argsort(iv[:, 0])]
    out = [iv[0].copy()]
    for a, b in iv[1:]:
        if a <= out[-1][1]:
            out[-1][1] = max(out[-1][1], b)
        else:
            out.append(np.array([a, b]))
    return np.array(out)


def intersect_intervals(a, b):
    a, b = merge_intervals(a), merge_intervals(b)
    out = []
    i = j = 0
    while i < len(a) and j < len(b):
        lo, hi = max(a[i, 0], b[j, 0]), min(a[i, 1], b[j, 1])
        if lo < hi:
            out.append((lo, hi))
        if a[i, 1] < b[j, 1]:
            i += 1
        else:
            j += 1
    return np.array(out).reshape(-1, 2)


def in_intervals(t, iv):
    iv = merge_intervals(iv)
    if len(iv) == 0:
        return np.zeros(len(t), bool)
    k = np.searchsorted(iv[:, 0], t, side="right") - 1
    ok = k >= 0
    res = np.zeros(len(t), bool)
    res[ok] = t[ok] <= iv[k[ok], 1]
    return res


def total(iv):
    iv = merge_intervals(iv)
    return float(np.sum(iv[:, 1] - iv[:, 0])) if len(iv) else 0.0


def first_T(iv, T):
    """The first T seconds of an interval set."""
    out, acc = [], 0.0
    for a, b in merge_intervals(iv):
        if acc + (b - a) >= T:
            out.append((a, a + T - acc))
            break
        out.append((a, b))
        acc += b - a
    return np.array(out).reshape(-1, 2)


def last_T(iv, T):
    iv = merge_intervals(iv)
    flipped = np.column_stack([-iv[::-1, 1], -iv[::-1, 0]])
    r = first_T(flipped, T)
    return np.column_stack([-r[::-1, 1], -r[::-1, 0]])


# ----------------------------------------------------------------------------- behaviour

def position_kinematics(s):
    """Speed (m/s, from the smoothed 2D position) and 1D velocity (m/s) at each position sample.
    Smoothing SD POS_SMOOTH_S is a standard choice."""
    t = s["pos_t"]
    dt = np.median(np.diff(t))
    sd = POS_SMOOTH_S / dt
    xy = s["pos_2d"].copy()
    good = ~np.isnan(xy).any(1)
    xs = np.full_like(xy, np.nan)
    for k in range(2):
        v = np.interp(t, t[good], xy[good, k])
        xs[:, k] = ndimage.gaussian_filter1d(v, sd)
    speed = np.r_[0, np.hypot(*np.diff(xs, axis=0).T) / np.diff(t)]
    speed[~good] = np.nan
    x1 = s["pos_1d"]
    g1 = ~np.isnan(x1)
    v1 = np.full(len(t), np.nan)
    if g1.sum() > 2:
        xi = np.interp(t, t[g1], x1[g1])
        xi = ndimage.gaussian_filter1d(xi, sd)
        v1 = np.gradient(xi, t)
        v1[~g1] = np.nan
    return speed, v1


def directions(s):
    """Running directions: two on the linear mazes (increasing and decreasing 1D position), one on
    the circular maze (Methods, Place Field Analysis)."""
    return ["inc", "dec"] if "Linear" in s["maze"] else ["cw"]


def run_mask(s, d, speed, v1):
    """Samples of running at >= 5 cm/s on the track (1D position defined) in direction d."""
    ok = ~np.isnan(s["pos_1d"]) & (speed >= RUN_SPEED) & ~np.isnan(v1)
    if d == "inc":
        ok &= v1 > 0
    elif d == "dec":
        ok &= v1 < 0
    return ok


# ----------------------------------------------------------------------------- place fields

def track_bins(s):
    L = np.nanmax(s["pos_1d"])
    nb = int(np.ceil(L * 100 / BIN_CM - 1e-6))
    return nb


def smooth(v, axis=-1, sd_cm=SMOOTH_CM):
    return ndimage.gaussian_filter1d(v, sd_cm / BIN_CM, axis=axis, mode="nearest")


def occupancy_and_counts(s, d, speed, v1, unit_ids):
    t = s["pos_t"]
    dt = np.median(np.diff(t))
    ok = run_mask(s, d, speed, v1)
    nb = track_bins(s)
    b = np.clip((s["pos_1d"] / (BIN_CM / 100)).astype(int, copy=False) if False else
                np.floor(np.nan_to_num(s["pos_1d"]) / (BIN_CM / 100)).astype(int), 0, nb - 1)
    occ = np.bincount(b[ok], minlength=nb) * dt
    counts = np.zeros((len(unit_ids), nb))
    for i, u in enumerate(unit_ids):
        sp = s["spikes"][u]
        sp = sp[(sp >= t[0]) & (sp <= t[-1])]
        k = np.clip(np.searchsorted(t, sp), 1, len(t) - 1)
        k = np.where(np.abs(t[k - 1] - sp) < np.abs(t[k] - sp), k - 1, k)
        keep = ok[k] & (np.abs(t[k] - sp) < dt)
        counts[i] = np.bincount(b[k[keep]], minlength=nb)
    return occ, counts


def rate_maps(occ, counts):
    so = smooth(occ)
    with np.errstate(invalid="ignore", divide="ignore"):
        sm = np.where(so > 0, smooth(counts) / so, 0.0)
        raw = np.where(occ > 0, counts / np.where(occ > 0, occ, 1), 0.0)
    return sm, raw


def place_field_test(occ, count_row, rng, sd_cm=SMOOTH_CM, min_peak=PF_MIN_PEAK):
    """Methods, Place Field Analysis: 5,000 nulls drawn from the unsmoothed occupancy; a field is
    >= 5 consecutive bins above the null 99th percentile with an in-field peak >= 1 Hz.
    Returns (is_place_cell, list of fields as (start, stop) bin ranges). sd_cm and min_peak allow the
    variants of the notebook (the 5 cm kernel read as its full width at half maximum; no 1 Hz rule)."""
    n = int(count_row.sum())
    so = smooth(occ, sd_cm=sd_cm)
    with np.errstate(invalid="ignore", divide="ignore"):
        obs = np.where(so > 0, smooth(count_row, sd_cm=sd_cm) / so, 0.0)
    if n == 0:
        return False, []
    p = occ / occ.sum()
    null = rng.multinomial(n, p, size=N_PF_NULL).astype(float)
    with np.errstate(invalid="ignore", divide="ignore"):
        null = np.where(so > 0, smooth(null, axis=1, sd_cm=sd_cm) / so, 0.0)
    thr = np.percentile(null, 99, axis=0)
    above = (obs > thr) & (so > 0)
    fields = []
    lab, nl = ndimage.label(above)
    for k in range(1, nl + 1):
        idx = np.flatnonzero(lab == k)
        if len(idx) >= PF_MIN_BINS and obs[idx].max() >= min_peak:
            fields.append((idx[0], idx[-1] + 1))
    return len(fields) > 0, fields


def spatial_info(sm, occ):
    """Skaggs information per spike and per second (reference 32, Mizuseki et al. 2012)."""
    p = occ / occ.sum()
    lam = np.sum(p * sm)
    with np.errstate(invalid="ignore", divide="ignore"):
        r = sm / lam
        terms = np.where(r > 0, p * r * np.log2(r), 0.0)
    ips = float(np.sum(terms))
    return ips, ips * lam


def spatial_coherence(raw, occ):
    """Correlation of each bin's rate with the mean of its neighbours (Muller and Kubie 1989), on
    visited bins; the Fisher z of r, as in reference 32."""
    v = occ > 0
    nb = np.full(len(raw), np.nan)
    for i in range(len(raw)):
        nbr = [j for j in (i - 1, i + 1) if 0 <= j < len(raw) and v[j]]
        if nbr:
            nb[i] = np.mean(raw[nbr])
    ok = v & ~np.isnan(nb)
    if ok.sum() < 3 or np.std(raw[ok]) == 0:
        return np.nan
    r = np.corrcoef(raw[ok], nb[ok])[0, 1]
    return float(np.arctanh(np.clip(r, -0.999999, 0.999999)))


# ----------------------------------------------------------------------------- LFP ripples

def detect_lfp_ripples(f, meta, channels_hint, nrem_iv, z_thresholds=(3.0, 5.0)):
    """LFP sharp wave-ripples from one pyramidal-layer channel (Methods, Ripple Event Detection;
    150-250 Hz band from Figure S4). The channel is the one with the highest ripple-band power among
    the 16 channels of the chunk column that holds the shank with most pyramidal cells (assumption:
    the paper does not say which channel). Envelope: Hilbert amplitude of the band-passed signal,
    smoothed with an 8 ms Gaussian (standard), z-scored over NREM. Peaks of supra-threshold
    stretches (>= 3 SD, reading L-a) are returned with their peak z, so that reading L-b (>= 5 SD)
    is a subset."""
    d = f["processing/ecephys/LFP/lfp/data"]
    fs = meta["lfp_rate"]
    n = d.shape[0]
    col0 = (channels_hint // 16) * 16
    chunk = d.chunks[0]
    # pick the channel on a NREM stretch
    nr = merge_intervals(nrem_iv)
    long_ = nr[np.argmax(nr[:, 1] - nr[:, 0])]
    a_seg = int(long_[0] * fs)
    seg = d[a_seg:a_seg + int(min(60, long_[1] - long_[0]) * fs), col0:col0 + 16].astype(float)
    sos = signal.butter(4, RIPPLE_BAND, btype="band", fs=fs, output="sos")
    bp = signal.sosfiltfilt(sos, seg, axis=0)
    pw = np.mean(bp ** 2, 0)
    bad = meta["bad_electrode"][col0:col0 + 16]
    pw[bad] = -1
    ch = int(np.argmax(pw))
    env = np.empty(n, np.float32)
    pad = 2000
    for a in range(0, n, chunk):
        b = min(n, a + chunk)
        lo, hi = max(0, a - pad), min(n, b + pad)
        x = d[lo:hi, col0 + ch].astype(float)
        y = np.abs(signal.hilbert(signal.sosfiltfilt(sos, x)))
        env[a:b] = y[a - lo:a - lo + (b - a)]
    env = ndimage.gaussian_filter1d(env, 0.008 * fs)
    t = np.arange(n) / fs
    m = in_intervals(t, nrem_iv)
    mu, sd = float(env[m].mean()), float(env[m].std())
    z = (env - mu) / sd
    above = z >= min(z_thresholds)
    lab, nl = ndimage.label(above)
    objs = ndimage.find_objects(lab)
    peaks, peakz = [], []
    for k, sl in enumerate(objs):
        zs = z[sl[0]]
        i = int(np.argmax(zs))
        peaks.append((sl[0].start + i) / fs)
        peakz.append(float(zs[i]))
    # check of the channel (verifier, round 1): ripple-triggered raw LFP (+-100 ms) on the 60 s NREM
    # segment used to pick it, around the peaks with z >= 5 that fall in the segment
    pk_ = np.array(peaks); pz_ = np.array(peakz)
    i_seg = ((pk_ * fs).astype(int) - a_seg)
    i_seg = i_seg[(pz_ >= 5.0) & (i_seg >= int(0.1 * fs)) & (i_seg < seg.shape[0] - int(0.1 * fs))]
    w = int(0.1 * fs)
    trig = np.array([seg[i - w:i + w + 1, ch] for i in i_seg]).mean(0) if len(i_seg) else np.full(2 * w + 1, np.nan)
    return {"channel": col0 + ch, "peak_t": pk_, "peak_z": pz_, "nrem_mean": mu, "nrem_sd": sd,
            "col_power": pw, "col_channel_index": ch, "trig_lfp": trig * meta["lfp_conversion"], "trig_n": len(i_seg),
            "fs": fs}


# ----------------------------------------------------------------------------- population events

def population_events(s, pyr_ids, nrem_iv):
    """Population synchrony events (Methods, Ripple Event Detection): pyramidal spikes in 1 ms bins,
    convolved with a 15 ms (SD) Gaussian; trigger mean + 3 SD of the NREM bins of PRE and POST;
    bounds where the rate returns to the NREM mean."""
    dur = s["duration"]
    last = max(float(s["spikes"][u].max()) for u in pyr_ids if len(s["spikes"][u]))
    nbin = int(np.ceil(max(dur, last) * 1000)) + 2
    cnt = np.zeros(nbin, np.float32)
    for u in pyr_ids:
        np.add.at(cnt, (s["spikes"][u] * 1000).astype(np.int64), 1)
    sm = ndimage.gaussian_filter1d(cnt, POP_SD_MS)
    del cnt
    t = (np.arange(nbin) + 0.5) / 1000
    m = in_intervals(t, nrem_iv)
    mu, sd = float(sm[m].mean()), float(sm[m].std())
    del m
    above_mean = sm > mu
    trig = sm > mu + POP_Z * sd
    lab, nl = ndimage.label(above_mean)
    has = np.unique(lab[trig])
    has = has[has > 0]
    objs = ndimage.find_objects(lab)
    ev = np.array([(objs[k - 1][0].start / 1000, objs[k - 1][0].stop / 1000) for k in has]).reshape(-1, 2)
    return ev, mu, sd


# ----------------------------------------------------------------------------- decoding kernels

@numba.njit(cache=True, fastmath=True)
def _wcorr(L, T, P):
    """Posterior from log-likelihood L (T x P), normalised per time bin, then weighted correlation of
    position and time (Methods, equations 2 to 5)."""
    post = np.empty((T, P))
    for t in range(T):
        mx = L[t, 0]
        for x in range(1, P):
            if L[t, x] > mx:
                mx = L[t, x]
        ssum = 0.0
        for x in range(P):
            v = np.exp(L[t, x] - mx)
            post[t, x] = v
            ssum += v
        for x in range(P):
            post[t, x] /= ssum
    W = 0.0
    mt = 0.0
    mp = 0.0
    for t in range(T):
        for x in range(P):
            w = post[t, x]
            W += w
            mt += w * t
            mp += w * x
    mt /= W
    mp /= W
    ctt = 0.0
    cpp = 0.0
    ctp = 0.0
    for t in range(T):
        for x in range(P):
            w = post[t, x]
            ctt += w * (t - mt) * (t - mt)
            cpp += w * (x - mp) * (x - mp)
            ctp += w * (t - mt) * (x - mp)
    if ctt <= 0 or cpp <= 0:
        return 0.0
    return ctp / np.sqrt(ctt * cpp)


@numba.njit(cache=True)
def _loglik(n, logf, S):
    C, T = n.shape
    P = logf.shape[1]
    L = np.empty((T, P))
    for t in range(T):
        for x in range(P):
            L[t, x] = -S[x]
        for c in range(C):
            if n[c, t] > 0:
                for x in range(P):
                    L[t, x] += n[c, t] * logf[c, x]
    return L


@numba.njit(cache=True, parallel=True)
def _null_r(n, logF_act, S_null):
    """r for each of K null templates. n: C x T counts of the active cells; logF_act: C x K x P;
    S_null: K x P (tau times the sum of all cells' null rates)."""
    C, T = n.shape
    K = S_null.shape[0]
    P = S_null.shape[1]
    out = np.empty(K)
    for k in numba.prange(K):
        L = np.empty((T, P))
        for t in range(T):
            for x in range(P):
                L[t, x] = -S_null[k, x]
            for c in range(C):
                if n[c, t] > 0:
                    for x in range(P):
                        L[t, x] += n[c, t] * logF_act[c, k, x]
        out[k] = _wcorr(L, T, P)
    return out


@numba.njit(cache=True, parallel=True)
def _cell_shuffle_r(n, logf_act, f_act, logF_act, F_act, L0, tau, K):
    """For each active cell j and shuffle k < K, r with only cell j's map replaced by its k-th
    shuffle (Methods, Per Cell Contribution)."""
    C, T = n.shape
    P = L0.shape[1]
    out = np.empty((C, K))
    for idx in numba.prange(C * K):
        j = idx // K
        k = idx % K
        L = np.empty((T, P))
        for t in range(T):
            for x in range(P):
                L[t, x] = L0[t, x] + n[j, t] * (logF_act[j, k, x] - logf_act[j, x]) \
                    - tau * (F_act[j, k, x] - f_act[j, x])
        out[j, k] = _wcorr(L, T, P)
    return out


class Template:
    """A decoding template for one session and running direction: the smoothed rate maps of its place
    cells, and N_SHUF circular place-field shuffles of each (Methods, Bayesian Replay Analysis)."""

    def __init__(self, cells, sm, raw, rng, n_shuf=N_SHUF):
        self.cells = np.asarray(cells)
        self.f = sm + EPS_RATE
        self.logf = np.log(self.f)
        C, P = sm.shape
        self.P = P
        shifts = rng.integers(1, P, size=(C, n_shuf))
        F = np.empty((C, n_shuf, P))
        for c in range(C):
            idx = (np.arange(P)[None, :] - shifts[c][:, None]) % P
            F[c] = smooth(raw[c][idx], axis=1)
        self.F = F + EPS_RATE
        self.logF = np.log(self.F)
        self.S = DEC_BIN * self.f.sum(0)
        self.S_null = DEC_BIN * self.F.sum(0)
        self.shifts = shifts


def bin_event(spk_by_cell, t0, t1):
    T = int(np.floor((t1 - t0) / DEC_BIN + 1e-9))
    n = np.zeros((len(spk_by_cell), T))
    for i, sp in enumerate(spk_by_cell):
        a, b = np.searchsorted(sp, [t0, t0 + T * DEC_BIN])
        if b > a:
            k = ((sp[a:b] - t0) / DEC_BIN).astype(int)
            np.add.at(n[i], np.minimum(k, T - 1), 1)
    return n


def score_event(tpl, n, pcc_k=0):
    """Observed r, null |r| mean and SD, rZ, and (when pcc_k > 0) PCC of each active cell.
    n: counts of all template cells (C x T)."""
    act = np.flatnonzero(n.sum(1) > 0)
    na = n[act]
    L0 = _loglik(na, tpl.logf[act], tpl.S)
    r = _wcorr(L0, n.shape[1], tpl.P)
    rn = np.abs(_null_r(na, tpl.logF[act], tpl.S_null))
    mu, sd = rn.mean(), rn.std(ddof=1)
    rz = (abs(r) - mu) / sd
    out = {"r": r, "null_mean": mu, "null_sd": sd, "rz": rz, "active": tpl.cells[act], "n_active": len(act),
           "null_sample": rn[:20].copy()}
    if pcc_k:
        rc = np.abs(_cell_shuffle_r(na, tpl.logf[act], tpl.f[act], tpl.logF[act], tpl.F[act], L0, DEC_BIN,
                                    pcc_k))
        rzc = (rc - mu) / sd
        out["rz_cellshuf_mean"] = rzc.mean(1)
        out["pcc"] = (rz - rzc.mean(1)) * len(act)
    return out


# ----------------------------------------------------------------------------- statistics

def tukey_kramer_ranks(groups: dict):
    """Kruskal-Wallis, then Tukey-Kramer comparisons of mean ranks (the post hoc test that MATLAB's
    multcompare applies to kruskalwallis output; the Figure 1C legend names Kruskal-Wallis followed by
    Tukey-Kramer). Returns the KW p and, per pair, (difference of mean ranks, p)."""
    names = list(groups)
    allv = np.concatenate([groups[k] for k in names])
    ranks = stats.rankdata(allv)
    N = len(allv)
    k = len(names)
    sizes = [len(groups[x]) for x in names]
    mr, pos = {}, 0
    for x, m in zip(names, sizes):
        mr[x] = ranks[pos:pos + m].mean()
        pos += m
    kw = stats.kruskal(*[groups[x] for x in names])
    # variance of ranks with tie correction
    _, cnt = np.unique(allv, return_counts=True)
    tie = 1 - np.sum(cnt ** 3 - cnt) / (N ** 3 - N)
    var = N * (N + 1) / 12 * tie
    res = {}
    for i in range(k):
        for j in range(i + 1, k):
            a, b = names[i], names[j]
            se = np.sqrt(var * (1 / sizes[i] + 1 / sizes[j]) / 2)
            q = abs(mr[a] - mr[b]) / se
            p = stats.studentized_range.sf(q, k, np.inf)
            res[(a, b)] = (mr[a] - mr[b], float(p))
    return float(kw.pvalue), res


def tukey_kramer_values(groups: dict):
    """Tukey-Kramer on the values themselves (variant)."""
    names = list(groups)
    k = len(names)
    sizes = np.array([len(groups[x]) for x in names])
    means = {x: np.mean(groups[x]) for x in names}
    df = sizes.sum() - k
    mse = sum(np.sum((groups[x] - means[x]) ** 2) for x in names) / df
    res = {}
    for i in range(k):
        for j in range(i + 1, k):
            a, b = names[i], names[j]
            se = np.sqrt(mse / 2 * (1 / sizes[i] + 1 / sizes[j]))
            q = abs(means[a] - means[b]) / se
            res[(a, b)] = (means[a] - means[b], float(stats.studentized_range.sf(q, k, df)))
    return res


def boot_diff_ci(a, b, rng, n=1000, fn=np.mean):
    """Bootstrap 95% interval of fn(a) - fn(b), resampling each group (standard)."""
    a, b = np.asarray(a), np.asarray(b)
    ia = rng.integers(0, len(a), (n, len(a)))
    ib = rng.integers(0, len(b), (n, len(b)))
    d = fn(a[ia], axis=1) - fn(b[ib], axis=1)
    return np.percentile(d, [2.5, 97.5])


def fisher_z_independent(r1, n1, r2, n2):
    z = (np.arctanh(r1) - np.arctanh(r2)) / np.sqrt(1 / (n1 - 3) + 1 / (n2 - 3))
    return float(z), float(2 * stats.norm.sf(abs(z)))


def fisher_z_dependent(rjk, rjh, rkh, n):
    """Steiger's (1980) test for two dependent correlations sharing variable j: r(j,k) against r(j,h)."""
    rm2 = (rjk ** 2 + rjh ** 2) / 2
    f = min((1 - rkh) / (2 * (1 - rm2)), 1.0)
    h = (1 - f * rm2) / (1 - rm2)
    z = (np.arctanh(rjk) - np.arctanh(rjh)) * np.sqrt((n - 3) / (2 * (1 - rkh) * h))
    return float(z), float(2 * stats.norm.sf(abs(z)))


def binned_counts(spk, iv, width):
    """Spike counts in non-overlapping bins of `width` s tiling each interval (partial bins dropped)."""
    edges = []
    for a, b in merge_intervals(iv):
        m = int((b - a) // width)
        if m > 0:
            edges.append(a + width * np.arange(m + 1))
    if not edges:
        return np.zeros(0)
    out = []
    for e in edges:
        out.append(np.histogram(spk, e)[0])
    return np.concatenate(out)


def ccg_bias(ref, cmp_, iv, half=0.15):
    """Coincident spikes within +-150 ms in intervals iv (Methods, Pair-Wise Temporal Interaction):
    (reference after comparison - reference before comparison) / all coincident, and the count."""
    ref = ref[in_intervals(ref, iv)]
    cmp_ = cmp_[in_intervals(cmp_, iv)]
    if len(ref) == 0 or len(cmp_) == 0:
        return np.nan, 0
    lo = np.searchsorted(cmp_, ref - half, side="left")
    mid_l = np.searchsorted(cmp_, ref, side="left")
    mid_r = np.searchsorted(cmp_, ref, side="right")
    hi = np.searchsorted(cmp_, ref + half, side="right")
    after = np.sum(mid_l - lo)     # comparison before reference: reference fired after
    before = np.sum(hi - mid_r)
    tot = after + before
    return ((after - before) / tot if tot else np.nan), int(tot)


# ----------------------------------------------------------------------------- one session

def offline_sets(s, speed, nwb):
    """Offline-state interval sets for the readings of the claims' opening comment.
    S-a: the lab's state epochs (sessInfo.Epochs; the paper's scoring, reference 31); NREM with the
    lab's 'Intermediate' (which the data description calls a sub-type of NREM) and 'Drowsy' (low
    movement and EMG; read as quiet waking, an assumption). S-b: the automatic buzcode scoring held
    in the NWB file (sleep_states_buzcode), NREM only. On the maze, both readings take immobility as
    speed below 5 cm/s with the position tracked (assumption: the Methods use 5 cm/s for running)."""
    E = s["epochs"]
    pre, maze, post = E["PREEpoch"][0], E["MazeEpoch"][0], E["POSTEpoch"][0]
    st = s["states"]
    lab_off = merge_intervals(np.vstack([st[k] for k in ["NREM", "Intermediate", "Drowsy"] if k in st]))
    lab_nrem = merge_intervals(st["NREM"])
    lab_, a_, b_ = nwb["sleep_states_buzcode"]
    bz_nrem = merge_intervals(np.column_stack([a_[lab_ == "NREM"], b_[lab_ == "NREM"]]))
    t = s["pos_t"]
    imm = (speed < RUN_SPEED) & ~np.isnan(speed)
    lab2, nl = ndimage.label(imm)
    objs = ndimage.find_objects(lab2)
    dt = np.median(np.diff(t))
    maze_imm = np.array([(t[o[0].start], t[o[0].stop - 1] + dt) for o in objs]).reshape(-1, 2)
    maze_imm = intersect_intervals(maze_imm, [maze])
    out = {}
    for key, base in [("S-a", lab_off), ("S-b", bz_nrem)]:
        out[key] = {"PRE": intersect_intervals(base, [pre]), "POST": intersect_intervals(base, [post]),
                    "MAZE": maze_imm}
    out["nrem_prepost"] = intersect_intervals(lab_nrem, np.array([pre, post]))
    return out


def yoke_windows(s, off):
    """Readings Y-a, Y-b and Y-c of the claims' opening comment: PRE and POST windows of the length
    T of the shorter epoch (Methods, Behavioral State Scoring, last paragraph)."""
    E = s["epochs"]
    pre, post = E["PREEpoch"][0], E["POSTEpoch"][0]
    T = min(pre[1] - pre[0], post[1] - post[0])
    w = {"Y-a": {"PRE": np.array([[pre[1] - T, pre[1]]]), "POST": np.array([[post[0], post[0] + T]])},
         "Y-b": {"PRE": np.array([[pre[0], pre[0] + T]]), "POST": np.array([[post[0], post[0] + T]])}}
    Toff = min(total(off["S-a"]["PRE"]), total(off["S-a"]["POST"]))
    w["Y-c"] = {"PRE": last_T(off["S-a"]["PRE"], Toff), "POST": first_T(off["S-a"]["POST"], Toff)}
    w["T"] = T
    w["T_off"] = Toff
    return w


def process_session(name, s, nwb_file, nwb_meta, rng_pf, rng_shuf, pcc_k=N_PCC, n_null=N_NULL, log=print):
    """Everything the claims need from one session that is not cheap to recompute."""
    import time
    t0 = time.time()
    pyr = [int(u) for u in s["pyr_ids"]]
    shank = {u: u // 100 for u in s["spikes"]}
    speed, v1 = position_kinematics(s)
    off = offline_sets(s, speed, nwb_meta)
    yk = yoke_windows(s, off)
    res = {"name": name, "maze": s["maze"], "pyr": pyr, "int": [int(u) for u in s["int_ids"]], "shank": shank,
           "speed": speed, "v1": v1, "off": off, "yoke": yk, "epochs": s["epochs"]}
    # place fields per direction
    res["dirs"] = {}
    for d in directions(s):
        occ, counts = occupancy_and_counts(s, d, speed, v1, pyr)
        sm, raw = rate_maps(occ, counts)
        pcs, fields = [], {}
        for i, u in enumerate(pyr):
            ok, fl = place_field_test(occ, counts[i], rng_pf)
            if ok:
                pcs.append(u)
                fields[u] = fl
        res["dirs"][d] = {"occ": occ, "counts": counts, "sm": sm, "raw": raw, "place_cells": pcs, "fields": fields}
    log(f"{name}: place fields {time.time() - t0:.0f} s")
    # LFP ripples (DANDI) and population events
    best_shank = max(set(shank[u] for u in pyr), key=lambda g: sum(shank[u] == g for u in pyr))
    chans = np.flatnonzero(nwb_meta["electrode_group"] == best_shank)
    rip = detect_lfp_ripples(nwb_file, nwb_meta, int(chans[0]), off["nrem_prepost"])
    res["lfp"] = rip
    log(f"{name}: LFP ripples {time.time() - t0:.0f} s (channel {rip['channel']}, {len(rip['peak_t'])} peaks)")
    ev, mu, sd = population_events(s, pyr, off["nrem_prepost"])
    res["pop_events_n"] = len(ev)
    res["pop_trigger"] = (mu, sd)
    dur = ev[:, 1] - ev[:, 0]
    pk, pz = rip["peak_t"], rip["peak_z"]
    a = np.searchsorted(pk, ev[:, 0])
    b = np.searchsorted(pk, ev[:, 1], side="right")
    cs = np.r_[0, np.cumsum(pz >= 5.0)]
    has3 = b > a
    has5 = (cs[b] - cs[a]) > 0
    npyr = np.zeros(len(ev), int)
    for u in pyr:
        sp = s["spikes"][u]
        npyr += (np.searchsorted(sp, ev[:, 1]) - np.searchsorted(sp, ev[:, 0])) > 0
    mid = ev.mean(1)
    E = s["epochs"]
    epoch = np.full(len(ev), "", dtype=object)
    for k, lab in [("PREEpoch", "PRE"), ("MazeEpoch", "MAZE"), ("POSTEpoch", "POST")]:
        epoch[(mid >= E[k][0][0]) & (mid < E[k][0][1])] = lab
    flags = {"has_lfp3": has3, "has_lfp5": has5, "dur_ok": (dur >= EV_MIN) & (dur <= EV_MAX), "npyr_ok": npyr >= EV_MIN_PYR}
    for S in ["S-a", "S-b"]:
        f_ = np.zeros(len(ev), bool)
        for ep in ["PRE", "MAZE", "POST"]:
            f_ |= (epoch == ep) & in_intervals(mid, off[S][ep])
        flags[S] = f_
    res["pop_flags_all"] = {k: v.copy() for k, v in flags.items()}
    keep = flags["has_lfp3"] & flags["dur_ok"] & flags["npyr_ok"] & (flags["S-a"] | flags["S-b"]) & (epoch != "")
    res["pop_events_with_lfp_frac"] = float(has3.mean()) if len(ev) else np.nan
    res["events"] = {"t": ev[keep], "epoch": epoch[keep], "dur": dur[keep], "npyr": npyr[keep],
                     **{k: v[keep] for k, v in flags.items()}}
    log(f"{name}: {len(ev)} population events, {keep.sum()} candidate ripple events {time.time() - t0:.0f} s")
    # direction decoder (Methods, equation 6) for reading D-b: mean running rate of all pyramidal cells
    evt = res["events"]["t"]
    if len(res["dirs"]) == 2:
        rates = []
        for d in ["inc", "dec"]:
            dd = res["dirs"][d]
            rates.append(dd["counts"].sum(1) / max(dd["occ"].sum(), 1e-9) + EPS_RATE)
        rates = np.array(rates)
        n_ev = np.array([[np.searchsorted(s["spikes"][u], b) - np.searchsorted(s["spikes"][u], a)
                          for u in pyr] for a, b in evt]).reshape(len(evt), len(pyr))
        tau = (evt[:, 1] - evt[:, 0])[:, None]
        ll = np.stack([(n_ev * np.log(rates[k])[None, :]).sum(1) - tau[:, 0] * rates[k].sum() for k in range(2)], 1)
        res["events"]["dir_b"] = np.where(ll[:, 0] >= ll[:, 1], "inc", "dec")
    else:
        res["events"]["dir_b"] = np.array(["cw"] * len(evt), dtype=object)
    # replay scoring per direction template
    for d, dd in res["dirs"].items():
        cells = dd["place_cells"]
        idx = [pyr.index(u) for u in cells]
        tpl = Template(cells, dd["sm"][idx], dd["raw"][idx], rng_shuf, n_shuf=n_null)
        dd["template"] = tpl
        need = max(5, int(np.ceil(0.1 * len(cells))))
        spk = [s["spikes"][u] for u in cells]
        scores = []
        for i, (a, b) in enumerate(evt):
            if b - a < REPLAY_MIN_DUR:
                continue
            n = bin_event(spk, a, b)
            if (n.sum(1) > 0).sum() < need:
                continue
            sc = score_event(tpl, n, pcc_k=pcc_k if res["events"]["epoch"][i] in ("PRE", "POST") else 0)
            sc["event"] = i
            scores.append(sc)
        dd["scores"] = scores
        dd["min_active"] = need
        log(f"{name} {d}: {len(cells)} place cells, {len(scores)} replay events {time.time() - t0:.0f} s")
    return res


# ----------------------------------------------------------------------------- tables across sessions

import pandas as pd  # noqa: E402

READINGS_Y = ["Y-a", "Y-b", "Y-c"]
READINGS_L = ["L-a", "L-b"]
READINGS_S = ["S-a", "S-b"]
READINGS_D = ["D-a", "D-b"]


def event_table(R):
    """One row per ripple event of every session (the candidate set of all readings), with the yoked
    windows each falls in."""
    rows = []
    for name, r in R.items():
        ev = r["events"]
        mid = ev["t"].mean(1)
        d = {"session": name, "ev": np.arange(len(mid)), "t0": ev["t"][:, 0], "t1": ev["t"][:, 1], "mid": mid,
             "epoch": ev["epoch"], "dur": ev["dur"], "npyr": ev["npyr"], "L-a": ev["has_lfp3"], "L-b": ev["has_lfp5"],
             "S-a": ev["S-a"], "S-b": ev["S-b"], "dir_b": ev["dir_b"]}
        df = pd.DataFrame(d)
        for Y in READINGS_Y:
            w = r["yoke"][Y]
            df[Y] = (df.epoch == "MAZE") | ((df.epoch == "PRE") & in_intervals(mid, w["PRE"])) | \
                ((df.epoch == "POST") & in_intervals(mid, w["POST"]))
        rows.append(df)
    return pd.concat(rows, ignore_index=True)


def score_table(R, ET):
    """One row per (event, direction template) scored by the Bayesian replay analysis."""
    rows = []
    for name, r in R.items():
        e = ET[ET.session == name].set_index("ev")
        for d, dd in r["dirs"].items():
            for sc in dd["scores"]:
                rows.append({"session": name, "dir": d, "ev": sc["event"], "r": sc["r"], "rz": sc["rz"],
                             "null_mean": sc["null_mean"], "null_sd": sc["null_sd"], "n_active": sc["n_active"],
                             "null_sample": sc.get("null_sample", np.full(1, sc["null_mean"])),
                             "n_place": len(dd["place_cells"])})
    st = pd.DataFrame(rows)
    st = st.merge(ET, on=["session", "ev"], how="left")
    st["absr"] = st.r.abs()
    st["D-a"] = True
    st["D-b"] = (st["dir"] == st["dir_b"]) | (st["dir"] == "cw")
    return st


def reading_mask(df, Y="Y-a", L="L-a", S="S-a", D=None):
    m = df[Y] & df[L] & df[S]
    if D is not None:
        m &= df[D]
    return m


def pcc_table(R, ST):
    """One row per (event, direction, active place cell) with the cell's PCC in that event and the
    event's observed and mean cell-shuffled rZ."""
    rows = []
    for name, r in R.items():
        for d, dd in r["dirs"].items():
            for sc in dd["scores"]:
                if "pcc" not in sc:
                    continue
                for u, p, rc in zip(sc["active"], sc["pcc"], sc["rz_cellshuf_mean"]):
                    rows.append((name, d, sc["event"], int(u), p, sc["rz"], rc))
    pt = pd.DataFrame(rows, columns=["session", "dir", "ev", "cell", "pcc", "rz", "rz_cs"])
    keep = ST[["session", "dir", "ev", "epoch", "Y-a", "Y-b", "Y-c", "L-a", "L-b", "S-a", "S-b", "D-a", "D-b"]]
    return pt.merge(keep, on=["session", "dir", "ev"], how="left")


def cell_pcc(PT, mask):
    """Per (session, direction, cell): PRE and POST PCC (means over the cell's events), dPCC, and the
    strongly-contributing tests P-a and P-b (Methods, Rigid and Plastic Cell Classification)."""
    sub = PT[mask]
    out = []
    for (s_, d, c), g in sub.groupby(["session", "dir", "cell"]):
        row = {"session": s_, "dir": d, "cell": c}
        for ep in ["PRE", "POST"]:
            x = g[g.epoch == ep]
            row[f"pcc_{ep}"] = x.pcc.mean() if len(x) else np.nan
            row[f"n_{ep}"] = len(x)
            if len(x) >= 2 and np.any(x.pcc != 0):
                row[f"pa_{ep}"] = stats.wilcoxon(x.pcc, alternative="greater").pvalue
                row[f"pb_{ep}"] = stats.ranksums(x.rz, x.rz_cs, alternative="greater").pvalue
            else:
                row[f"pa_{ep}"] = row[f"pb_{ep}"] = np.nan
            row[f"vals_{ep}"] = x.pcc.values
        out.append(row)
    C = pd.DataFrame(out)
    C["dpcc"] = C.pcc_POST - C.pcc_PRE
    return C


def classify(C, P="pa", place=None):
    """Strongly contributing (p < 0.05 in PRE or POST); rigid at or below each session and direction's
    median dPCC, plastic above; the median cell dropped for odd counts (Methods)."""
    C = C.copy()
    C["sig_PRE"] = C[f"{P}_PRE"] < 0.05
    C["sig_POST"] = C[f"{P}_POST"] < 0.05
    C["strong"] = C.sig_PRE | C.sig_POST
    C["group"] = ""
    for (s_, d), g in C[C.strong & C.dpcc.notna()].groupby(["session", "dir"]):
        g = g.sort_values("dpcc")
        n = len(g)
        idx = list(g.index)
        if n % 2 == 1:
            idx.pop(n // 2)
        h = len(idx) // 2
        C.loc[idx[:h], "group"] = "rigid"
        C.loc[idx[h:], "group"] = "plastic"
    return C


def rescore(r, s, d, cells_keep, shuffle_cells, rng, events, n_null, min_rule=True):
    """Rerun the replay analysis for one session and direction on the given events with a modified
    template: only `cells_keep` (exclusion), and with `shuffle_cells` circularly shuffled once in the
    'observed' template (Figure 2D; assumption: one shuffled template per percentage). The event
    criteria (>= 100 ms; >= max(5, 10%) of the kept place cells active) are applied after exclusion
    (Methods, Bayesian Replay Analysis)."""
    dd = r["dirs"][d]
    pcs = dd["place_cells"]
    pyr = r["pyr"]
    keep = [u for u in pcs if u in set(cells_keep)]
    if len(keep) < 5:
        return pd.DataFrame(columns=["ev", "rz"])
    idx = [pyr.index(u) for u in keep]
    raw = dd["raw"][idx].copy()
    sm = dd["sm"][idx].copy()
    P = sm.shape[1]
    for j, u in enumerate(keep):
        if u in shuffle_cells:
            sh = rng.integers(1, P)
            sm[j] = smooth(np.roll(raw[j], sh))
    tpl = Template(keep, sm, raw, rng, n_shuf=n_null)
    need = max(5, int(np.ceil(0.1 * len(keep))))
    spk = [s["spikes"][u] for u in keep]
    out = []
    for i, (a, b) in events:
        if b - a < REPLAY_MIN_DUR:
            continue
        n = bin_event(spk, a, b)
        if (n.sum(1) > 0).sum() < need:
            continue
        out.append((i, score_event(tpl, n)["rz"]))
    return pd.DataFrame(out, columns=["ev", "rz"])


# ----------------------------------------------------------------------------- laps and per-lap measures

def laps(s, speed, v1, min_frac=0.5, gap=0.5):
    """Laps as stretches in which the lab's 1D position is defined (it is defined only while the rat
    runs along the track), split at gaps > 0.5 s, kept when the net displacement exceeds half the
    track; direction from its sign (standard)."""
    t, x = s["pos_t"], s["pos_1d"]
    ok = ~np.isnan(x)
    idx = np.flatnonzero(ok)
    if len(idx) == 0:
        return []
    br = np.flatnonzero(np.diff(t[idx]) > gap)
    segs = np.split(idx, br + 1)
    L = np.nanmax(x)
    out = []
    circ = "Linear" not in s["maze"]
    for sg in segs:
        disp = x[sg[-1]] - x[sg[0]]
        if circ:
            if abs(disp) > min_frac * L:
                out.append(("cw", t[sg[0]], t[sg[-1]]))
        elif abs(disp) > min_frac * L:
            out.append(("inc" if disp > 0 else "dec", t[sg[0]], t[sg[-1]]))
    return out


def lap_measures(s, d, unit, fields, speed, v1, lap_list, nb):
    """Per lap of direction d: spikes, time, in-field spikes and time, running samples only."""
    t = s["pos_t"]
    dt = np.median(np.diff(t))
    ok = run_mask(s, d, speed, v1)
    b = np.clip(np.floor(np.nan_to_num(s["pos_1d"]) / (BIN_CM / 100)).astype(int), 0, nb - 1)
    infield = np.zeros(nb, bool)
    for a, c in fields:
        infield[a:c] = True
    sp = s["spikes"][unit]
    k = np.clip(np.searchsorted(t, sp), 1, len(t) - 1)
    k = np.where(np.abs(t[k - 1] - sp) < np.abs(t[k] - sp), k - 1, k)
    good = ok[k] & (np.abs(t[k] - sp) < dt)
    rows = []
    for dd, a, c in lap_list:
        if dd != d:
            continue
        m = ok & (t >= a) & (t <= c)
        ms = good & (sp >= a) & (sp <= c)
        n = ms.sum()
        nin = np.sum(infield[b[k[ms]]])
        T = m.sum() * dt
        Tin = np.sum(m & infield[b]) * dt
        rows.append((n, nin, T, Tin))
    return np.array(rows, float).reshape(-1, 4)


def spikes_in(sp, iv):
    iv = merge_intervals(iv)
    if len(iv) == 0:
        return 0
    return int(np.sum(np.searchsorted(sp, iv[:, 1]) - np.searchsorted(sp, iv[:, 0])))


def concat_isis(sp, iv, same_event=True):
    """ISIs of spikes inside interval set iv: (a) within one interval only; (b) over concatenated
    interval time (gaps removed)."""
    iv = merge_intervals(iv)
    k = np.searchsorted(iv[:, 0], sp, side="right") - 1
    ok = (k >= 0)
    ok[ok] = sp[ok] <= iv[k[ok], 1]
    x, kk = sp[ok], k[ok]
    if len(x) < 2:
        return np.zeros(0)
    if same_event:
        same = kk[1:] == kk[:-1]
        return np.diff(x)[same]
    gaps = np.r_[0, np.cumsum(iv[1:, 0] - iv[:-1, 1])]
    xa = x - gaps[kk]
    return np.diff(xa)


# ----------------------------------------------------------------------------- batched rescoring (reruns)
# The reruns of Figures 2D, 2E, 4D, 4E and S12 score tens of thousands of events per template; these
# kernels score many events in one call. They give the same r as _loglik/_null_r followed by _wcorr
# (checked against score_event on synthetic templates to 1e-15 while preparing; the notebook checks
# the baseline rerun against the main scores).

_LOG2E = 1.4426950408889634
_LN2_HI = 6.93147180369123816490e-01
_LN2_LO = 1.90821492927058770002e-10


@numba.njit(cache=True, fastmath=True)
def _exp_shift(row, mx, bits):
    """row[x] <- exp(row[x] - mx): Cody-Waite reduction and a degree-13 Taylor polynomial (relative
    error ~1e-16), vectorisable; arguments below -700 are clamped (exp(-700) ~ 1e-304)."""
    P = row.shape[0]
    for x in range(P):
        d = row[x] - mx
        if d < -700.0:
            d = -700.0
        n = np.floor(d * _LOG2E + 0.5)
        r = d - n * _LN2_HI - n * _LN2_LO
        p = 1.0 + r * (1.0 + r * (1 / 2 + r * (1 / 6 + r * (1 / 24 + r * (1 / 120 + r * (1 / 720 + r * (
            1 / 5040 + r * (1 / 40320 + r * (1 / 362880 + r * (1 / 3628800 + r * (1 / 39916800 + r * (
                1 / 479001600 + r / 6227020800))))))))))))
        row[x] = p
        bits[x] = (np.int64(n) + 1023) << 52
    sc = bits.view(np.float64)
    for x in range(P):
        row[x] *= sc[x]


@numba.njit(cache=True, fastmath=True)
def _wcorr_inplace(L, T, P):
    """_wcorr in one pass (each time bin's posterior sums to 1, so the weighted moments reduce to
    per-bin moments of position, taken about the track centre). L is overwritten."""
    bits = np.empty(P, np.int64)
    c0 = 0.5 * (P - 1)
    mt = 0.5 * (T - 1)
    sp1 = 0.0
    sp2 = 0.0
    ctp = 0.0
    ctt = 0.0
    for t in range(T):
        mx = L[t, 0]
        for x in range(1, P):
            if L[t, x] > mx:
                mx = L[t, x]
        _exp_shift(L[t, :P], mx, bits)
        s0 = 0.0
        s1 = 0.0
        s2 = 0.0
        for x in range(P):
            w = L[t, x]
            u = x - c0
            s0 += w
            s1 += w * u
            s2 += w * u * u
        s1 /= s0
        s2 /= s0
        sp1 += s1
        sp2 += s2
        ctp += (t - mt) * s1
        ctt += (t - mt) * (t - mt)
    mp = sp1 / T
    cpp = sp2 - T * mp * mp
    if ctt <= 0 or cpp <= 0:
        return 0.0
    return ctp / np.sqrt(ctt * cpp)


@numba.njit(cache=True, parallel=True, fastmath=True)
def _batch_events(N, st, ln, act, logF, Ssum, R):
    E = st.shape[0]
    C = N.shape[0]
    K, P = Ssum.shape
    for i in numba.prange(E):
        o = st[i]
        T = ln[i]
        if T < 1:
            for k in range(K):
                R[i, k] = np.nan
            continue
        L = np.empty((T, P))
        cidx = np.empty(T * C, np.int64)
        cnt = np.empty(T * C)
        nnz = np.empty(T + 1, np.int64)
        m = 0
        nnz[0] = 0
        for t in range(T):
            for c in range(C):
                if act[i, c]:
                    v = N[c, o + t]
                    if v > 0:
                        cidx[m] = c
                        cnt[m] = v
                        m += 1
            nnz[t + 1] = m
        for k in range(K):
            for t in range(T):
                for x in range(P):
                    L[t, x] = -Ssum[k, x]
                for j in range(nnz[t], nnz[t + 1]):
                    c = cidx[j]
                    v = cnt[j]
                    for x in range(P):
                        L[t, x] += v * logF[c, k, x]
            R[i, k] = _wcorr_inplace(L, T, P)


def batch_r(N, st, ln, act, logF, Ssum):
    """R[i, k], the signed weighted correlation of event i (columns st[i]:st[i]+ln[i] of the counts N,
    C x time bins) decoded with template k (log rates logF, C x K x P; Ssum, K x P, DEC_BIN times the
    summed rates of the template's cells); only cells with act[i, c] enter the spike term."""
    R = np.empty((len(st), Ssum.shape[0]))
    if len(st):
        _batch_events(np.ascontiguousarray(N, np.float64), np.ascontiguousarray(st, np.int64),
                      np.ascontiguousarray(ln, np.int64), np.ascontiguousarray(act, np.bool_),
                      np.ascontiguousarray(logF, np.float64), np.ascontiguousarray(Ssum, np.float64), R)
    return R


def prepare_counts(spk_list, ev):
    """Bin events as bin_event does, all events at once. Returns N (C x bins), start and length of each
    event's bins, and the spike counts per event and cell (E x C)."""
    ev = np.asarray(ev, float).reshape(-1, 2)
    t0, t1 = ev[:, 0], ev[:, 1]
    E = len(ev)
    T = np.maximum(np.floor((t1 - t0) / DEC_BIN + 1e-9).astype(np.int64), 0)
    st = np.r_[0, np.cumsum(T)[:-1]].astype(np.int64) if E else np.zeros(0, np.int64)
    N = np.zeros((len(spk_list), int(T.sum())))
    counts = np.zeros((E, len(spk_list)), np.int64)
    tend = t0 + T * DEC_BIN
    for c, sp in enumerate(spk_list):
        a = np.searchsorted(sp, t0)
        b = np.searchsorted(sp, tend)
        m = np.maximum(b - a, 0)
        counts[:, c] = m
        tot = int(m.sum())
        if tot == 0:
            continue
        e = np.repeat(np.arange(E), m)
        start = np.cumsum(m) - m
        idx = np.arange(tot) - start[e] + a[e]
        k = np.minimum(((sp[idx] - t0[e]) / DEC_BIN).astype(int), T[e] - 1)
        N[c] += np.bincount(st[e] + k, minlength=N.shape[1])
    return N, st, T, counts


def shuffled_maps(raw_rows, rng, n):
    """n circular place-field shuffles of each row's unsmoothed map, re-smoothed (Methods, Bayesian
    Replay Analysis), as in Template. Returns rates (C x n x P)."""
    C, P = raw_rows.shape
    shifts = rng.integers(1, P, size=(C, n))
    F = np.empty((C, n, P))
    for c in range(C):
        idx = (np.arange(P)[None, :] - shifts[c][:, None]) % P
        F[c] = smooth(raw_rows[c][idx], axis=1)
    return F


def rescore_batch(prep, keep_idx, rng, n_null, shuffle_idx=(), n_obs=1, rows=None, null=None):
    """Rerun the replay analysis on one session and direction with a modified template (batched).

    prep: dict with the template's smoothed and raw maps ('sm', 'raw', C x P), the binned events
    ('N', 'st', 'ln', 'counts') and 'dur'. keep_idx: template cells kept (exclusion, Figure S12, 2E,
    4D, 4E); the event criteria (>= 100 ms; >= max(5, 10%) of the kept cells active) are applied after
    exclusion (Methods, Bayesian Replay Analysis). shuffle_idx: cells whose maps are circularly
    shuffled in the decoding template (Figure 2D); n_obs such shuffled templates are drawn and each
    event's rZ is the mean over them (assumption, see the notebook). The null is n_null shuffles of
    all kept cells (equation 7); `null` may pass (mu, sd) per event computed beforehand for the same
    kept cells. rows: the events to score (bool mask). Returns (event rows, rZ, rZ per observed
    template, null mu, null sd)."""
    sm, raw = prep["sm"], prep["raw"]
    C, P = sm.shape
    keep = np.zeros(C, bool)
    keep[list(keep_idx)] = True
    E = len(prep["st"])
    rows = np.ones(E, bool) if rows is None else np.asarray(rows, bool)
    if keep.sum() < 5:
        return np.zeros(0, int), np.zeros(0), np.zeros((0, n_obs)), np.zeros(0), np.zeros(0)
    need = max(5, int(np.ceil(0.1 * keep.sum())))
    act = (prep["counts"] > 0) & keep[None, :]
    ok = rows & (prep["dur"] >= REPLAY_MIN_DUR) & (act.sum(1) >= need)
    ev = np.flatnonzero(ok)
    act = act[ev]
    st, ln = prep["st"][ev], prep["ln"][ev]
    if null is None:
        F = np.zeros((C, n_null, P))
        F[keep] = shuffled_maps(raw[keep], rng, n_null)
        F += EPS_RATE
        Ssum = DEC_BIN * F[keep].sum(0)
        Rn = np.abs(batch_r(prep["N"], st, ln, act, np.log(F), Ssum))
        mu, sd = Rn.mean(1), Rn.std(1, ddof=1)
    else:
        mu, sd = null[0][ev], null[1][ev]
    sh = np.zeros(C, bool)
    sh[list(shuffle_idx)] = True
    sh &= keep
    if sh.any():
        Fo = np.repeat((sm + EPS_RATE)[:, None, :], n_obs, axis=1)
        Fo[sh] = shuffled_maps(raw[sh], rng, n_obs) + EPS_RATE
    else:
        Fo = (sm + EPS_RATE)[:, None, :]
    So = DEC_BIN * Fo[keep].sum(0)
    Ro = np.abs(batch_r(prep["N"], st, ln, act, np.log(Fo), So))
    rzm = (Ro - mu[:, None]) / sd[:, None]
    return ev, rzm.mean(1), rzm, mu, sd


# ----------------------------------------------------------------------------- cluster quality (Figure S11)
# PCA features (.fet) and cluster ids (.clu) of hc-11 are only in the per-session tarballs
# (<session>.tar.gz, 0.8 to 2.3 GB). They are streamed (curl piped into gzip, read as a tar stream);
# nothing is written to disk. Unit ids are shank * 100 + cluster id (checked: the row count of each
# cluster equals the unit's spike count, and the .res times equal the spike times).

import itertools  # noqa: E402
import re  # noqa: E402
import subprocess  # noqa: E402
import xml.etree.ElementTree as _ET  # noqa: E402

FS_SPIKES = 20000.0
BURST_ISI = 0.006       # Figure S11 legend: first spikes of bursts (< 6 ms) only
CQ_MIN_N = 5            # standard: a condition with fewer selected spikes gives NaN


def _first_of_burst(t):
    m = np.ones(len(t), bool)
    if len(t) > 1:
        m[1:] = np.diff(t) >= BURST_ISI
    return m


def _cond_label(t, conds):
    lab = np.full(len(t), -1, np.int8)
    for k, (_, iv) in enumerate(conds):
        lab[(lab < 0) & in_intervals(t, iv)] = k
    return lab


def _mahal(X, mu, Pinv):
    D = X - mu
    return np.sqrt(np.maximum(np.einsum("ij,jk,ik->i", D, Pinv, D), 0))


def session_cluster_quality(name, spikes, units, cond_iv, chunk=500_000):
    """Figure S11 legend: cluster quality in a condition is the median Mahalanobis distance between the
    PCA features of each spike in that condition and the cluster centre (mean over all of the unit's
    spikes; the covariance of all its spikes is used, an assumption); stability between two
    conditions is the symmetrical distance between one condition's spikes and the other condition's
    centre: the mean of the two medians (assumption). First spikes of bursts only (a spike counts
    when the unit's previous spike is >= 6 ms earlier). PCA columns: nChannels x nFeatures of the
    shank's group in the session's .xml. Returns (table per unit, checks)."""
    conds = list(cond_iv.items())
    units = [int(u) for u in units]
    by_shank = {}
    for u in units:
        by_shank.setdefault(u // 100, []).append(u)
    checks = {"members": [], "count_mismatch": [], "res_maxerr": 0.0, "fet_rows_mismatch": []}
    clu, rowlab, acc, sel, xml_groups = {}, {}, {}, {}, None
    url = CRCNS_BASE + f"data/{name}.tar.gz"
    p_curl = subprocess.Popen(["curl", "-s", "--fail", url], stdout=subprocess.PIPE)
    p_gz = subprocess.Popen(["gzip", "-dc"], stdin=p_curl.stdout, stdout=subprocess.PIPE, bufsize=1 << 20)
    p_curl.stdout.close()
    tf = tarfile.open(fileobj=p_gz.stdout, mode="r|")
    for m in tf:
        base = m.name.split("/")[-1]
        checks["members"].append((base, m.size))
        if base.endswith(".xml"):
            root = _ET.fromstring(tf.extractfile(m).read())
            xml_groups = {gi: (len(grp.find("channels")), int(grp.find("nFeatures").text))
                          for gi, grp in enumerate(root.find("spikeDetection").find("channelGroups"), start=1)}
            continue
        mt = re.match(r".*\.(clu|fet|res)\.(\d+)$", base)
        if not mt or not m.isfile():
            continue
        kind, sh = mt.group(1), int(mt.group(2))
        f = tf.extractfile(m)
        if kind == "clu":
            c = pd.read_csv(f, header=None, dtype=np.int32, engine="c").values[1:, 0]
            clu[sh] = c
            urow = np.full(len(c), -1, np.int32)
            lab = np.full(len(c), -1, np.int8)
            for j, u in enumerate(by_shank.get(sh, [])):
                rws = np.flatnonzero(c == u % 100)
                t = spikes[u]
                if len(rws) != len(t):
                    checks["count_mismatch"].append((u, len(rws), len(t)))
                    continue
                urow[rws] = j
                lb = _cond_label(t, conds)
                lb[~_first_of_burst(t)] = -1
                lab[rws] = lb
            rowlab[sh] = (urow, lab)
        elif kind == "fet" and by_shank.get(sh):
            nf = int(f.readline())
            us = by_shank[sh]
            urow, lab = rowlab[sh]
            for u in us:
                acc[u] = [0, np.zeros(nf), np.zeros((nf, nf))]
                sel[u] = []
            off = 0
            for ch in pd.read_csv(f, sep=" ", header=None, dtype=np.int64, engine="c", chunksize=chunk,
                                  skipinitialspace=True):
                X = ch.values
                n = len(X)
                ur, lb = urow[off:off + n], lab[off:off + n]
                for j, u in enumerate(us):
                    ii = np.flatnonzero(ur == j)
                    if len(ii):
                        Xu = X[ii].astype(np.float64)
                        a = acc[u]
                        a[0] += len(ii)
                        a[1] += Xu.sum(0)
                        a[2] += Xu.T @ Xu
                        kk = ii[lb[ii] >= 0]
                        if len(kk):
                            sel[u].append((X[kk].astype(np.float64), lb[kk].copy()))
                off += n
            if off != len(clu[sh]):
                checks["fet_rows_mismatch"].append((sh, off, len(clu[sh])))
        elif kind == "res" and by_shank.get(sh):
            r = pd.read_csv(f, header=None, dtype=np.int64, engine="c").values[:, 0] / FS_SPIKES
            for u in by_shank[sh]:
                rr = r[clu[sh] == u % 100]
                if len(rr) == len(spikes[u]):
                    checks["res_maxerr"] = max(checks["res_maxerr"], float(np.abs(rr - spikes[u]).max()))
    tf.close()
    p_gz.wait()
    p_curl.wait()
    rows = []
    pairs = list(itertools.combinations(range(len(conds)), 2))
    for u in units:
        rec = {"session": name, "cell": u}
        if u not in acc or acc[u][0] < 2:
            rows.append(rec)
            continue
        nch, nfe = xml_groups[u // 100]
        npc = nch * nfe
        n, s1, s2 = acc[u]
        mu = s1 / n
        Cv = ((s2 / n - np.outer(mu, mu)) * n / (n - 1))[:npc, :npc]
        Pinv = np.linalg.pinv(Cv, hermitian=True)
        mu = mu[:npc]
        Xs = np.concatenate([s[0] for s in sel[u]])[:, :npc] if sel[u] else np.zeros((0, npc))
        L = np.concatenate([s[1] for s in sel[u]]) if sel[u] else np.zeros(0, np.int8)
        G = [Xs[L == k] for k in range(len(conds))]
        rec["n_pca"] = npc
        for k, (cn, _) in enumerate(conds):
            rec[f"n_{cn}"] = len(G[k])
            rec[f"q_{cn}"] = float(np.median(_mahal(G[k], mu, Pinv))) if len(G[k]) >= CQ_MIN_N else np.nan
        for a, b in pairs:
            na, nb = conds[a][0], conds[b][0]
            if len(G[a]) >= CQ_MIN_N and len(G[b]) >= CQ_MIN_N:
                dab = np.median(_mahal(G[a], G[b].mean(0), Pinv))
                dba = np.median(_mahal(G[b], G[a].mean(0), Pinv))
                rec[f"stab_{na}_{nb}"] = float((dab + dba) / 2)
            else:
                rec[f"stab_{na}_{nb}"] = np.nan
        rows.append(rec)
    return pd.DataFrame(rows), checks


def _cq_worker(args):
    return session_cluster_quality(*args)
