"""Loading and measures for Yang et al. (2025) on DANDI:001212.

Paper: Yang, Ni, Sun, Xing, Wang, Zhang, Zhu & Xu (2025), Individualized target selection of
closed-loop electrical stimulation for the treatment of spontaneous temporal lobe epilepsy,
IEEE TNSRE 33:4008-4016, doi:10.1109/TNSRE.2025.3614867. Claims: claims/yang-2025.yaml.

The dandiset holds, for each of 7 rats and 8 groups (4 baseline, 4 stimulation), one NWB file
whose acquisition holds one ElectricalSeries per seizure clip: 600 s at 1 kHz, 4 channels
(DG, CA1, CA3, ANT), in microvolts. It holds no seizure onset or end times, no stimulation
times, no interictal recordings and no recording durations.

Where each parameter comes from is said where it is defined. The tags are:
  [paper]      the paper's Methods, with the section cited;
  [criterion]  the claim's criterion in claims/yang-2025.yaml;
  [assumption] a choice the paper leaves open that could change a result, stated in the
               attempt record as an assumption;
  [standard]   a standard choice for a detail that cannot change a result.

The data are streamed from the archive (remfile + h5py) and reduced, clip by clip, to the
quantities the claims use (`process_clip`), so no raw clip is held after it is processed.
"""

import hashlib
import json
import re
import urllib.request

import h5py
import numpy as np
import remfile
from scipy import signal, stats
from scipy.ndimage import median_filter

DANDISET_ID = "001212"
DANDISET_VERSION = "0.241023.0931"
API = "https://api.dandiarchive.org/api"

FS = 1000.0  # Hz; the series' rate attribute and Methods A ("sampling frequency of 1 kHz")
CHANNELS = ["DG", "CA1", "CA3", "ANT"]  # order of the electrodes table, checked in the notebook

# ---------------------------------------------------------------------------------------------
# Loading


def list_assets():
    """Assets of the pinned version: list of dicts with path, asset_id, size."""
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/?page_size=500"
    out = []
    while url:
        with urllib.request.urlopen(url) as r:
            d = json.load(r)
        out += [{"path": a["path"], "asset_id": a["asset_id"], "size": a["size"]} for a in d["results"]]
        url = d.get("next")
    return sorted(out, key=lambda a: a["path"])


def version_metadata():
    with urllib.request.urlopen(f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/") as r:
        return json.load(r)


def parse_session(path):
    """Rat, group index, kind and stimulated site from a file name such as
    sub-RatR1/sub-RatR1_ses-RatR1-03CA3-stim_ecephys.nwb."""
    m = re.search(r"ses-Rat(R\d)-(\d\d)(base\d|[A-Z0-9]+-stim)_", path)
    rat, idx, tag = m.group(1), int(m.group(2)), m.group(3)
    if tag.startswith("base"):
        return {"rat": rat, "index": idx, "kind": "baseline", "site": None, "group": f"base{tag[4:]}"}
    site = tag.split("-")[0]
    return {"rat": rat, "index": idx, "kind": "stim", "site": site, "group": f"{site}-stim"}


def open_asset(asset_id):
    url = f"{API}/assets/{asset_id}/download/"
    return h5py.File(remfile.File(url), "r")


def file_metadata(h):
    """Everything the file holds besides the clips' data, for the data check."""
    g = h["general"]
    el = g["extracellular_ephys/electrodes"]
    meta = {
        "session_id": h["general/session_id"][()].decode(),
        "session_start_time": h["session_start_time"][0].decode(),
        "session_description": h["session_description"][()].decode(),
        "electrode_labels": [x.decode() for x in el["label"][:]],
        "electrode_locations": [x.decode() for x in el["location"][:]],
        "electrode_group_names": [x.decode() for x in el["group_name"][:]],
        "subject": {k: g["subject"][k][()].decode() for k in g["subject"]},
        "top_level": sorted(h.keys()),
        "intervals": sorted(h["intervals"].keys()),
        "processing": sorted(h["processing"].keys()),
        "analysis": sorted(h["analysis"].keys()),
        "stimulus": sorted(h["stimulus/presentation"].keys()) + sorted(h["stimulus/templates"].keys()),
        "clips": [],
    }
    for k in h["acquisition"]:
        s = h["acquisition"][k]
        meta["clips"].append({
            "name": k, "shape": s["data"].shape, "dtype": str(s["data"].dtype),
            "unit": s["data"].attrs["unit"], "conversion": float(s["data"].attrs["conversion"]),
            "rate": float(s["starting_time"].attrs["rate"]), "starting_time": float(s["starting_time"][()]),
            "description": s.attrs["description"],
        })
    return meta


def clip_date(name):
    """Date in a clip name such as R1_2023_7_16-ictal1 or R4_2023_9-11-ictal1 (both forms occur)."""
    m = re.match(r"R\d_(\d{4})_(\d{1,2})[_-](\d{1,2})-ictal(\d+)", name)
    return (int(m.group(1)), int(m.group(2)), int(m.group(3))), int(m.group(4))


# ---------------------------------------------------------------------------------------------
# Stimulation trains, from the artefact they leave in the recording.
#
# The files hold no stimulation times. The 130 Hz pulse trains (Methods C: 5 s trains, 5 s
# pause) leave narrow spectral lines in the 1 kHz recording (130 Hz and its aliased harmonics,
# their exact place depending on the clock). A 0.5 s window, stepped by 0.25 s, is scored by
# the number of bins in 100-495 Hz, away from the 50 Hz mains harmonics, whose log power is
# more than 10 times above both the local spectral median (15 bins) and that bin's median over
# the clip. A train is a run of windows scoring at least TRAIN_SCORE that lasts at least
# TRAIN_MIN_S. [standard] These settings were chosen by inspecting spectrograms of a few
# clips; the notebook shows that they find trains of about 5 s in stimulation groups and none
# in baseline groups.

TRAIN_WIN, TRAIN_STEP = 500, 250
TRAIN_SCORE = 5
TRAIN_MIN_S = 2.0
TRAIN_GAP_S = 0.5


def line_score(x):
    n = (len(x) - TRAIN_WIN) // TRAIN_STEP + 1
    idx = np.arange(TRAIN_WIN)[None, :] + TRAIN_STEP * np.arange(n)[:, None]
    f = np.fft.rfftfreq(TRAIN_WIN, 1 / FS)
    keep = (f >= 100) & (f <= 495) & (np.abs(((f + 25) % 50) - 25) > 3)
    win = np.hanning(TRAIN_WIN)
    out = np.zeros((n, x.shape[1]))
    for c in range(x.shape[1]):
        X = x[idx, c]
        X = X - X.mean(1, keepdims=True)
        P = np.log10(np.abs(np.fft.rfft(X * win, axis=1)) ** 2 + 1e-12)
        E = P - median_filter(P, size=(1, 15), mode="nearest")
        E = E - np.median(E, 0, keepdims=True)
        out[:, c] = (E[:, keep] > 1.0).sum(1)
    return out


def runs(mask, gap=0):
    """Start and end indices (inclusive) of runs of True, merging gaps of up to `gap` False."""
    idx = np.flatnonzero(mask)
    if len(idx) == 0:
        return []
    out, s, p = [], idx[0], idx[0]
    for i in idx[1:]:
        if i - p > gap + 1:
            out.append((s, p))
            s = i
        p = i
    out.append((s, p))
    return out


def find_trains(x):
    """Stimulation trains as (start_s, end_s), and the per-channel line scores."""
    sc = line_score(x)
    m = sc.max(1) >= TRAIN_SCORE
    trains = []
    for a, b in runs(m, gap=int(TRAIN_GAP_S / (TRAIN_STEP / FS))):
        t0 = a * TRAIN_STEP / FS + 0.25 * TRAIN_WIN / FS
        t1 = b * TRAIN_STEP / FS + 0.75 * TRAIN_WIN / FS
        if t1 - t0 >= TRAIN_MIN_S:
            trains.append((t0, t1))
    return trains, sc


# ---------------------------------------------------------------------------------------------
# Seizure onset and end. [assumption] The paper gives no rule for marking them offline (claims
# file, opening comment, reading (b)), and the files hold none. Line length (sum of absolute
# differences) of the 1-40 Hz band-passed LFP (4th order Butterworth, zero phase; this keeps
# the seizure discharges and drops the high-frequency noise floor and the 50 Hz harmonics) per
# channel in 1 s windows stepped by 0.25 s, divided by the channel's median over the clip (a
# clip is mostly interictal), and the largest over the 4 channels (seizures that stay at one
# site, as some do at ANT, are then found). Windows that overlap a detected stimulation train
# are left out, as the artefact inflates line length; they bridge gaps inside a seizure. A
# seizure is a run of windows above SZ_LOW, merging gaps up to SZ_GAP_S, that reaches SZ_HIGH
# and lasts at least SZ_MIN_S (hysteresis). The clip's seizure is the run with the largest
# excess line length or, in a clip with stimulation trains, the run that holds the first train
# (Methods C: "Once the signal from any channel detects seizure onset, the neurostimulator
# immediately triggers electrical stimulation"), when there is one. Onset is the centre of the run's first window, end the centre of its
# last. The thresholds were chosen, before any claim was computed, on 42 stimulation-group
# clips so that the stimulation trains, which the closed-loop detector starts on seizure
# onset, follow the onset (notebook, data check); the notebook shows every result also at
# (2, 1.5) and (4, 2.5).

LL_WIN, LL_STEP = 1000, 250
LL_BAND = (1.0, 40.0)
SZ_HIGH, SZ_LOW = 3.0, 2.0
SZ_VARIANTS = ((3.0, 2.0), (2.0, 1.5), (4.0, 2.5))
SZ_GAP_S = 5.0
SZ_MIN_S = 5.0


def line_length(x):
    sos = signal.butter(4, LL_BAND, btype="band", fs=FS, output="sos")
    xf = signal.sosfiltfilt(sos, x, axis=0)
    d = np.abs(np.diff(xf, axis=0))
    c = np.vstack([np.zeros((1, x.shape[1])), np.cumsum(d, axis=0)])
    starts = np.arange(0, len(x) - LL_WIN, LL_STEP)
    return (c[starts + LL_WIN - 1] - c[starts]), (starts + LL_WIN / 2) / FS


def detect_seizure(ll, centres, trains, high=SZ_HIGH, low=SZ_LOW):
    score = (ll / np.median(ll, axis=0, keepdims=True)).max(1)
    stim = np.zeros(len(centres), bool)
    for t0, t1 in trains:
        stim |= (centres + 0.5 >= t0) & (centres - 0.5 <= t1)
    hi = (score > high) & ~stim
    lo = (score > low) & ~stim
    step = LL_STEP / FS
    best, best_ex, with_train = None, 0.0, None
    first_train = trains[0][0] if trains else None
    for a, b in runs(lo | stim, gap=int(SZ_GAP_S / step)):
        seg = np.arange(a, b + 1)
        if not hi[seg].any():
            continue
        real = seg[lo[seg]]
        a2, b2 = real[0], real[-1]
        if centres[b2] - centres[a2] < SZ_MIN_S:
            continue
        ex = np.sum((score[a2:b2 + 1] - 1)[~stim[a2:b2 + 1]])
        if ex > best_ex:
            best, best_ex = (centres[a2], centres[b2]), ex
        if first_train is not None and with_train is None and centres[a] - 1 <= first_train <= centres[b] + 1:
            with_train = (centres[a2], centres[b2]), ex
    if with_train is not None:
        best, best_ex = with_train
    if best is None:
        return None
    return {"onset": float(best[0]), "end": float(best[1]), "excess": float(best_ex),
            "by_train": with_train is not None}


# ---------------------------------------------------------------------------------------------
# Granger causality and weighted causal flow (Methods B).
#
# [paper, Methods B] conditional multivariate GC (MVGC toolbox) between the 4 channels, first
# 5 s after onset, 1 s windows with 0.5 s overlap (9 windows). The toolbox's time-domain
# conditional GC from j to i is ln(Sigma_ii of the VAR without j / Sigma_ii of the full VAR),
# from OLS fits; reproduced here in numpy. [standard] Each window is demeaned; the model order
# is chosen per window by BIC up to GC_MAX_ORDER (the toolbox's own selection; AIC is shown as
# a variant). cf_w: Methods B says "difference between the weighted in-degree and out-degree";
# both signs are kept (claims file, readings (a) out minus in, (b) in minus out). As cf_w is
# linear in the GC matrix, averaging cf_w over windows and computing cf_w of the averaged
# matrix give the same value, so the two window-combination readings coincide.

GC_WINDOWS = [(0.5 * i, 0.5 * i + 1.0) for i in range(9)]
GC_MAX_ORDER = 20


def _lagged(X, p):
    T, k = X.shape
    Y = X[p:]
    Z = np.hstack([X[p - l:T - l] for l in range(1, p + 1)])
    return Y, Z


def _resid_cov(Y, Z):
    beta, *_ = np.linalg.lstsq(Z, Y, rcond=None)
    E = Y - Z @ beta
    return E.T @ E / len(Y)


def select_order(X, max_order=GC_MAX_ORDER, crit="bic"):
    X = X - X.mean(0)
    T, k = X.shape
    best, best_v = 1, np.inf
    for p in range(1, max_order + 1):
        Y, Z = _lagged(X[max_order - p:], p)  # same sample for every order
        S = _resid_cov(Y, Z)
        n = len(Y)
        pen = (np.log(n) if crit == "bic" else 2.0) * p * k * k / n
        v = np.log(np.linalg.det(S)) + pen
        if v < best_v:
            best, best_v = p, v
    return best


def conditional_gc(X, p):
    """F[i, j] = conditional GC from j to i given the other channels."""
    X = X - X.mean(0)
    T, k = X.shape
    Y, Z = _lagged(X, p)
    S_full = _resid_cov(Y, Z)
    F = np.zeros((k, k))
    for j in range(k):
        keep = [c for c in range(k) if c != j]
        Yr, Zr = _lagged(X[:, keep], p)
        S_red = _resid_cov(Yr, Zr)
        for a, i in enumerate(keep):
            F[i, j] = np.log(S_red[a, a] / S_full[i, i])
    return F


def onset_gc(x, onset, crit="bic", max_order=GC_MAX_ORDER):
    """Mean GC matrix over the 9 windows of the first 5 s after onset, and the orders used."""
    Fs, orders = [], []
    for a, b in GC_WINDOWS:
        i0, i1 = int(round((onset + a) * FS)), int(round((onset + b) * FS))
        X = x[i0:i1].astype(float)
        p = select_order(X, max_order=max_order, crit=crit)
        Fs.append(conditional_gc(X, p))
        orders.append(p)
    return np.mean(Fs, axis=0), orders


def cfw(F, sign="out_minus_in"):
    """Weighted causal flow per node from a GC matrix F[i, j] (j to i)."""
    out_s = F.sum(0)  # column sums: what node j sends
    in_s = F.sum(1)  # row sums: what node i receives
    return out_s - in_s if sign == "out_minus_in" else in_s - out_s


def targets_top(cf):
    """Reading (a): the node with the largest mean cf_w over a group's seizures. cf: (n, 4)."""
    return {CHANNELS[int(np.argmax(cf.mean(0)))]}


def targets_test(cf, alpha=0.05):
    """Reading (b): Kruskal-Wallis across the 4 nodes, then the top node together with every
    node not significantly below it by Mann-Whitney (ties allowed); empty when KW is not
    significant."""
    if stats.kruskal(*[cf[:, c] for c in range(4)]).pvalue >= alpha:
        return set()
    top = int(np.argmax(cf.mean(0)))
    out = {CHANNELS[top]}
    for c in range(4):
        if c != top and stats.mannwhitneyu(cf[:, top], cf[:, c], alternative="greater").pvalue >= alpha:
            out.add(CHANNELS[c])
    return out


# ---------------------------------------------------------------------------------------------
# PSD ratio (Methods D). [paper] Welch PSD; bands delta 0.5-4, theta 4-8, alpha 8-12, beta
# 12-30, gamma 30-90, high gamma 90-120 Hz; band sum over the total sum. Windows: stimulation
# group, pre from onset to the start of the first train, post the 5 s after the first train
# ([assumption] "5s after the first stimulation train" read as the 5 s from the train's end,
# the pause before the next detection); baseline group, pre 0 to 5 s after onset, post 10 to
# 15 s. The windows are computed under three readings (psd_windows): as worded, "guarded" (the
# main one, clear of the trains; added after verification round 1, which found post windows
# reaching the next train) and "guarded_pre5". Open [criterion]: segment length 1 s or 0.5 s
# (Hann, 50% overlap), total 0.5-120 Hz or 0-500 Hz.

BANDS = {"delta": (0.5, 4), "theta": (4, 8), "alpha": (8, 12), "beta": (12, 30),
         "gamma": (30, 90), "high_gamma": (90, 120)}
PSD_NPERSEG = (1000, 500)
PSD_TOTALS = {"0.5-120": (0.5, 120), "0-500": (0, 500)}
WINDOW_READINGS = ("guarded", "guarded_pre5", "paper")


def psd_ratios(seg):
    """{(nperseg, total): (4 channels, 6 bands)} band ratios for one window (samples, 4)."""
    out = {}
    for nps in PSD_NPERSEG:
        n = min(nps, len(seg))
        f, P = signal.welch(seg, fs=FS, window="hann", nperseg=n, noverlap=n // 2, axis=0)
        for tname, (lo, hi) in PSD_TOTALS.items():
            tot = P[(f >= lo) & (f <= hi)].sum(0)
            r = np.zeros((seg.shape[1], len(BANDS)))
            for b, (blo, bhi) in enumerate(BANDS.values()):
                sel = (f >= blo) & (f < bhi) if bhi < 120 else (f >= blo) & (f <= bhi)
                r[:, b] = P[sel].sum(0) / tot
            out[(nps, tname)] = r
    return out


TRAIN_GUARD_S = 0.25  # [standard] the train edges are known to one step of find_trains (0.25 s)
PRE_CAP_S = 5.0  # [assumption] variant: the pre window limited to the 5 s before the first train


def psd_windows(kind, onset, trains, reading="guarded"):
    """Pre and post windows (s) of one seizure, or None when a stimulation clip has no train after
    onset. Readings: "paper", Methods D as worded (stimulation group: onset to the first train,
    and the 5 s from the end of the first train); "guarded" (main), the same with TRAIN_GUARD_S
    kept clear of each train edge and the post window cut where the next train starts, so that no
    window holds train artefact; "guarded_pre5", as guarded with the pre window limited to the
    PRE_CAP_S before the first train (onsets detected long before the first train put pre-ictal
    signal in the pre window). Baseline groups: 0 to 5 s and 10 to 15 s after onset in all."""
    if kind == "baseline":
        return (onset, onset + 5.0), (onset + 10.0, onset + 15.0)
    after = [t for t in trains if t[1] > onset]
    if not after:
        return None
    t0, t1 = after[0]
    if reading == "paper":
        return (onset, t0), (t1, t1 + 5.0)
    g = TRAIN_GUARD_S
    nxt = after[1][0] - g if len(after) > 1 else np.inf
    pre0 = onset if reading == "guarded" else max(onset, t0 - g - PRE_CAP_S)
    return (pre0, t0 - g), (t1 + g, min(t1 + g + 5.0, nxt))


def in_trains(t, trains, guard=TRAIN_GUARD_S):
    """True for times t (s) within a train or within `guard` of one."""
    t = np.asarray(t, float)
    m = np.zeros(t.shape, bool)
    for a, b in trains:
        m |= (t >= a - guard) & (t <= b + guard)
    return m


# ---------------------------------------------------------------------------------------------
# Interictal spikes (Methods F). [paper] positive or negative peaks; peaks closer than 200 ms
# keep the larger; peak width at most 100 ms; absolute height above mean + 5 SD of baseline.
# [criterion] baseline reading (a), the 180 s before onset (the interictal segments of reading
# (b) are not in the dataset); width at half prominence [criterion, standard choice]. Applied to
# the raw LFP of each channel, demeaned by the baseline mean.

IIS_MIN_DIST_S = 0.2
IIS_MAX_WIDTH_S = 0.1
IIS_SD = 5.0
IIS_SPAN_S = 180.0


def detect_iis(xc, base):
    """IIS sample indices in the 1-D signal xc, with the threshold from the samples `base`."""
    mu, sd = base.mean(), base.std()
    y = np.abs(xc - mu)
    pk, prop = signal.find_peaks(y, height=IIS_SD * sd, distance=int(IIS_MIN_DIST_S * FS))
    if len(pk) == 0:
        return pk
    w = signal.peak_widths(y, pk, rel_height=0.5)[0] / FS
    return pk[w <= IIS_MAX_WIDTH_S]


# ---------------------------------------------------------------------------------------------
# HFOs during seizures (Methods E). [paper] short line length detector of the HFO App (ref. 50,
# Zhou et al. 2021, github.com/zelanolab/hfoapp at commit 1ccff19, Functions/HFOAutoDetectorSLL.m,
# modified from RIPPLELAB's f_findHFOxSLL); ripples 80-250 Hz, fast ripples 250-490 Hz (below the
# 500 Hz Nyquist limit [criterion]). [criterion: fig6cd, "the HFO App defaults are used"] The
# defaults of its detector dialog (GUIs/ConfigAutoDetector.mlapp): window 5 ms, threshold
# percentile 97.5, minimum duration 12 ms, no equalization filter, and an epoch equal to the
# displayed range, here the 600 s clip. The band-pass is FieldTrip's default Butterworth (4th
# order, two-pass), as HFOFiltData calls it. As in HFOAutoDetectorSLL: energy = 10 x the mean of
# |diff| over the window, centred; the first and last 0.5% of the clip tapered by a Gaussian
# window (1% of the length, alpha 5.25); threshold the percentile of the energy over the epoch;
# an event is a run at or above the threshold longer than the minimum duration. The manual review
# of the paper cannot be repeated; in its place [assumption] events within TRAIN_GUARD_S of a
# stimulation train are removed as artefact, and a variant takes the threshold from the samples
# outside the trains.

HFO_BANDS = {"ripple": (80, 250), "fast_ripple": (250, 490)}
HFO_WIN_S = 0.005
HFO_PCT = 97.5
HFO_MIN_DUR_S = 0.012
HFO_THRESH = ("clip", "outside_trains")


def _sll_energy(xc, band):
    lo, hi = HFO_BANDS[band]
    sos = signal.butter(4, [lo, hi], btype="band", fs=FS, output="sos")
    v = signal.sosfiltfilt(sos, xc.astype(float))
    w = int(round(HFO_WIN_S * FS))
    d = np.abs(np.diff(np.r_[v[0], v]))
    m = signal.lfilter(np.ones(w), 1, d) / w
    e = np.zeros(len(m))
    h = int(np.ceil(w / 2))
    e[:len(m) - h + 1] = 10 * m[h - 1:]
    n = int(round(len(e) * 0.01))
    g = signal.windows.gaussian(n, std=(n - 1) / (2 * 5.25))
    c = int(np.argmax(g))
    taper = np.r_[g[:c + 1], np.ones(len(e) - n), g[c + 1:]]
    return e * taper


def hfo_events(xc, band, trains):
    """HFO event centres (s) in the 1-D signal xc, per threshold reading, with the events within
    TRAIN_GUARD_S of a train removed."""
    e = _sll_energy(xc, band)
    keep = ~in_trains(np.arange(len(e)) / FS, trains)
    out = {}
    for th in HFO_THRESH:
        thr = np.percentile(e if th == "clip" or not keep.any() else e[keep], HFO_PCT)
        ev = []
        for a, b in runs(e >= thr):
            if (b - a + 1) > HFO_MIN_DUR_S * FS:
                ev.append((a, b))
        ev = np.array([(a / FS, b / FS) for a, b in ev]).reshape(-1, 2)
        bad = np.array([any(s <= t1 + TRAIN_GUARD_S and e_ >= t0 - TRAIN_GUARD_S for t0, t1 in trains)
                        for s, e_ in ev], bool)
        out[th] = ev[~bad].mean(1) if len(ev) else np.array([])
    return out


# ---------------------------------------------------------------------------------------------
# One pass per clip.


def process_clip(x, kind):
    """Reduce one clip (samples, 4) to what the claims use."""
    out = {"md5": hashlib.md5(np.ascontiguousarray(x).tobytes()).hexdigest(),
           "n_samples": len(x), "min": x.min(0), "max": x.max(0), "sd": x.std(0),
           "n_nan": int(np.isnan(x).sum())}
    trains, sc = find_trains(x)
    out["trains"] = trains
    out["line_score_max"] = sc.max(0)
    ll, centres = line_length(x)
    out["ll_env"] = (ll / np.median(ll, 0, keepdims=True)).max(1).astype(np.float32)
    out["seizures"] = {v: detect_seizure(ll, centres, trains, *v) for v in SZ_VARIANTS}
    sz = out["seizures"][(SZ_HIGH, SZ_LOW)]
    if sz is None:
        return out
    on, end = sz["onset"], sz["end"]
    # GC at onset (both order criteria), baseline groups only (Methods C), where the 5 s after
    # onset are in the clip
    if kind == "baseline" and on + 5.0 <= len(x) / FS:
        out["gc_bic"], out["orders_bic"] = onset_gc(x, on, "bic")
        out["gc_aic"], out["orders_aic"] = onset_gc(x, on, "aic")
        out["gc_aic30"], out["orders_aic30"] = onset_gc(x, on, "aic", max_order=30)
    # PSD and HFO windows, under each window reading
    i = lambda t: int(round(t * FS))
    out["psd_windows"], out["psd_pre"], out["psd_post"] = {}, {}, {}
    ev = {(band, c): hfo_events(x[:, c], band, trains) for band in HFO_BANDS for c in range(4)}
    out["hfo_counts"] = {}
    for reading in WINDOW_READINGS:
        win = psd_windows(kind, on, trains, reading)
        out["psd_windows"][reading] = win
        if win is None:
            continue
        (a0, a1), (b0, b1) = win
        if a1 - a0 >= 0.5 and b1 - b0 >= 0.5 and b1 <= len(x) / FS:
            out["psd_pre"][reading] = psd_ratios(x[i(a0):i(a1)])
            out["psd_post"][reading] = psd_ratios(x[i(b0):i(b1)])
        hfo = {(band, th): np.zeros((4, 2), int) for band in HFO_BANDS for th in HFO_THRESH}
        for (band, c), e in ev.items():
            for th, t in e.items():
                hfo[(band, th)][c] = [((t >= a0) & (t < a1)).sum(), ((t >= b0) & (t < b1)).sum()]
        out["hfo_counts"][reading] = hfo
    # IIS around the seizure, times relative to onset (pre) and to end (post)
    i0 = int(max(0.0, on - IIS_SPAN_S) * FS)
    i_on, i_end = int(on * FS), int(end * FS)
    i1 = int(min(len(x) / FS, end + IIS_SPAN_S) * FS)
    out["iis_span"] = (i0 / FS - on, i1 / FS - end)
    if i_on - i0 >= 30 * FS:
        pre, post = [], []
        for c in range(4):
            # [assumption] samples within TRAIN_GUARD_S of a train are left out of the threshold
            # baseline; spikes found there are dropped in the notebook
            tb = np.arange(i0, i_on) / FS
            base = x[i0:i_on, c][~in_trains(tb, trains)] if trains else x[i0:i_on, c]
            pk_pre = detect_iis(x[i0:i_on, c], base) + i0
            pk_post = detect_iis(x[i_end:i1, c], base) + i_end
            pre.append(pk_pre / FS - on)
            post.append(pk_post / FS - end)
        out["iis_pre"], out["iis_post"] = pre, post
    return out


def process_file(a):
    """Stream one file and reduce each of its clips; one clip is held in memory at a time."""
    s = parse_session(a["path"])
    h = open_asset(a["asset_id"])
    meta = file_metadata(h)
    meta.update(s, path=a["path"], asset_id=a["asset_id"], size=a["size"])
    clips = []
    for c in meta["clips"]:
        x = h["acquisition"][c["name"]]["data"][:]
        rec = process_clip(x, s["kind"])
        rec.update(s, clip=c["name"], path=a["path"])
        clips.append(rec)
        del x
    h.close()
    return meta, clips


def load_all(assets=None, workers=4):
    """Stream every file of the pinned version (or `assets`) and reduce each clip, `workers`
    files at a time (each worker holds one clip, about 20 MB, at a time). Returns the files'
    metadata and one record per clip."""
    import multiprocessing
    import os
    from concurrent.futures import ProcessPoolExecutor
    # one linear-algebra thread per worker; the workers are spawned, not forked, so that they load
    # numpy with this setting (a forked worker keeps the parent's thread pool, and the VAR fits of
    # several workers then compete for the CPUs: 44 min against 10 min for the whole dandiset)
    for k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
        os.environ[k] = "1"
    assets = list_assets() if assets is None else assets
    files, clips = [], []
    with ProcessPoolExecutor(workers, mp_context=multiprocessing.get_context("spawn")) as ex:
        for meta, cl in ex.map(process_file, assets):
            files.append(meta)
            clips += cl
    return files, clips
