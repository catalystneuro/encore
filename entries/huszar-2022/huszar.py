"""Loading and measures for Huszar et al. (2022) on DANDI:000552.

Streams the processed NWB files of the pinned version with remfile and h5py; nothing is
written to disk. Where a parameter comes from is said beside it:

- "claims" means the criterion of the claim in claims/huszar-2022.yaml, which cites the paper or
  its code (github.com/rhuszar/optotagCA1_final, commit 51320d4);
- "Methods" or a legend means the passage of the paper it was taken from (protocol, author 1.6);
- "assumption" means a choice the paper leaves open, with the reason;
- "standard" means a detail that cannot change a result.
"""
import concurrent.futures as cf
import json
import re

import h5py
import numpy as np
import remfile
import requests

DANDISET = "000552"
VERSION = "0.261113.1035"  # most recent published version; see the notebook header
API = "https://api.dandiarchive.org/api"

# Supplementary Table 1: mice and the analyses they enter (claims file, opening comment).
HOMECAGE_EXCLUDED = {"e15_13f1", "e16_3m2"}  # not in the homecage analyses (Figs 1-4, 7)
FAMILIAR_MICE = {"e13_16f1", "e13_26m1", "e14_2m2", "e14_2m3", "e15_9f1", "e15_10m1",
                 "e16_1f1", "e16_2m1", "e16_3m1"}  # Figure 5 column
NOVEL_MICE = {"e13_26m1", "e15_13f1", "e16_3m2"}  # Figure 6 column
# Supplementary Table 1 session and light-responsive counts, in the table's row order
# (claims file, st1-animal-sessions, inferred note; row order read from the image of the
# table in the Supplementary Information PDF, page 2).
ST1_ORDER = ["e13_1m1", "e13_1f1", "e14_1m1", "e15_4m1", "e15_4m2", "e15_5m1", "e13_16f1",
             "e14_2m2", "e14_2m3", "e15_9f1", "e15_10m1", "e16_1f1", "e16_2m1", "e16_3m1",
             "e13_26m1", "e15_13f1", "e16_3m2"]  # row order of the table's image
ST1_SESSIONS = [12, 5, 12, 3, 4, 3, 9, 4, 8, 7, 7, 9, 5, 4, 4, 4, 4]
ST1_LIGHT = [14, 6, 56, 35, 68, 19, 124, 9, 67, 67, 44, 49, 23, 43, 40, 53, 69]

BIRTHDATES = ["E13.5", "E14.5", "E15.5", "E16.5"]
BD_DAY = {"E13.5": 13.5, "E14.5": 14.5, "E15.5": 15.5, "E16.5": 16.5}


def birthdate(subject_id):
    """Electroporation day from the subject id (e13_ is E13.5 and so on), as the files describe."""
    return {"13": "E13.5", "14": "E14.5", "15": "E15.5", "16": "E16.5"}[subject_id[1:3]]


def assets():
    """Processed NWB assets of the pinned version (raw wide-band files left out)."""
    out, url = [], f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=200"
    while url:
        r = requests.get(url, timeout=60).json()
        out += r["results"]
        url = r["next"]
    return sorted([a for a in out if a["path"].endswith("behavior+ecephys.nwb")],
                  key=lambda a: a["path"])


def s3_url(asset):
    r = requests.head(f"{API}/assets/{asset['asset_id']}/download/", allow_redirects=True,
                      timeout=60)
    return r.url


def open_nwb(asset):
    return h5py.File(remfile.File(s3_url(asset)), "r")


def _s(x):
    return x.decode() if isinstance(x, bytes) else x


def _col(g, name):
    v = g[name][:]
    return np.array([_s(x) for x in v], dtype=object) if v.dtype == object else v


def table(g, cols=None):
    """A TimeIntervals or DynamicTable group as a dict of arrays (ragged columns left out)."""
    out = {}
    for k, v in g.items():
        if isinstance(v, h5py.Dataset) and (cols is None or k in cols) and not k.endswith("_index"):
            if k + "_index" in g:
                continue
            out[k] = _col(g, k)
    return out


def session_meta(asset):
    """Metadata and small arrays of one session: no spike times, no LFP samples."""
    with open_nwb(asset) as f:
        sub = f["general/subject"]
        m = {"path": asset["path"], "session_id": _s(f["general/session_id"][()]),
             "subject_id": _s(sub["subject_id"][()]), "sex": _s(sub["sex"][()]),
             "age": _s(sub["age"][()])}
        m["birthdate"] = birthdate(m["subject_id"])
        u = f["units"]
        m["n_units"] = int(u["id"].shape[0])
        m["has_cell_type"] = "putative_cell_type" in u
        for c in ["putative_cell_type", "light_responsive", "opto_p_salt", "opto_h_reliable",
                  "shank_id", "max_electrode", "trough_to_peak", "firing_rate", "unit_name"]:
            if c in u:
                v = _col(u, c)
                m["u_" + c] = v.tolist() if not isinstance(v, np.ndarray) or v.dtype != object \
                    else list(v)
        idx = u["spike_times_index"][:]
        m["u_n_spikes"] = np.diff(np.r_[0, idx]).tolist()
        st = u["spike_times"]

        m["last_spike"] = float(st[idx[-1] - 1]) if len(idx) else np.nan
        ec = f["processing/ecephys"]
        if "LFP" in ec:
            lfp = ec["LFP/LFP"]
            rate = float(lfp["starting_time"].attrs["rate"])
            m["lfp_shape"] = list(lfp["data"].shape)
            m["lfp_rate"] = rate
            m["lfp_duration_s"] = lfp["data"].shape[0] / rate
        else:
            m["lfp_duration_s"] = np.nan
        if "Ripples" in ec:
            r = ec["Ripples"]
            m["rip_start"] = r["start_time"][:].tolist()
            m["rip_stop"] = r["stop_time"][:].tolist()
            m["rip_dur"] = r["ripple_durations"][:].tolist()
        beh = f["processing"].get("behavior")
        m["sleep"] = None
        if beh is not None and "SleepStates" in beh:
            m["sleep"] = {k: (v.tolist() if not isinstance(v[0], str) else list(v))
                          for k, v in table(beh["SleepStates"]).items() if k != "id"}
        m["series"] = {}
        if beh is not None:
            for pos in ["LinearizedPosition", "SubjectPosition"]:
                if pos in beh:
                    for k, v in beh[pos].items():
                        ts = v["timestamps"]
                        m["series"][pos + "/" + k] = {
                            "desc": _s(v.attrs.get("description", "")),
                            "n": int(ts.shape[0]), "t0": float(ts[0]), "t1": float(ts[-1]),
                            "unit": _s(v["data"].attrs.get("unit", ""))}
        iv = f["intervals"]
        m["epochs"] = {k: list(v) if v.dtype == object else v.tolist()
                       for k, v in table(iv["epochs"]).items()} if "epochs" in iv else None
        m["trials"] = {k: list(v) if v.dtype == object else v.tolist()
                       for k, v in table(iv["trials"]).items()} if "trials" in iv else None
        m["pulse_periods"] = ({k: v.tolist() for k, v in
                               table(iv["OptogeneticPulsePeriods"]).items()}
                              if "OptogeneticPulsePeriods" in iv else None)
        m["n_pulses"] = int(iv["OptogeneticPulses/id"].shape[0]) if "OptogeneticPulses" in iv \
            else 0
        if "OptogeneticPulses" in iv:
            m["pulse_t0"] = float(iv["OptogeneticPulses/start_time"][0])
            m["pulse_t1"] = float(iv["OptogeneticPulses/stop_time"][-1])
    return m


def survey(workers=8):
    """session_meta for every processed file, in parallel threads (metadata only)."""
    a = assets()
    with cf.ThreadPoolExecutor(workers) as ex:
        return list(ex.map(session_meta, a))


def spike_trains(f, keep=None):
    """List of spike-time arrays (s), one per unit, for the unit indices in keep (all if None)."""
    u = f["units"]
    idx = u["spike_times_index"][:]
    st = u["spike_times"][:]
    starts = np.r_[0, idx[:-1]]
    rows = range(len(idx)) if keep is None else keep
    return [st[starts[i]:idx[i]] for i in rows]


# ---------- intervals ----------

def merge(iv):
    iv = sorted([tuple(x) for x in iv if x[1] > x[0]])
    out = []
    for a, b in iv:
        if out and a <= out[-1][1]:
            out[-1][1] = max(out[-1][1], b)
        else:
            out.append([a, b])
    return np.array(out).reshape(-1, 2)


def subtract(base, cut):
    """Intervals of base minus the union of cut."""
    cut = merge(cut)
    out = []
    for a, b in merge(base):
        cur = a
        for c, d in cut:
            if d <= cur or c >= b:
                continue
            if c > cur:
                out.append([cur, c])
            cur = max(cur, d)
        if cur < b:
            out.append([cur, b])
    return np.array(out).reshape(-1, 2)


def in_intervals(t, iv):
    """Boolean mask of times t inside any of the (sorted, disjoint) intervals iv."""
    if len(iv) == 0:
        return np.zeros(len(t), bool)
    i = np.searchsorted(iv[:, 0], t, side="right") - 1
    ok = i >= 0
    ok[ok] = t[ok] < iv[i[ok], 1]
    return ok


def homecage_intervals(m):
    """The homecage period of a session (claims file, opening comment; getHomecageMetrics.m):
    the recording up to the start of the second behavioural subsession when there is one, else
    the whole recording, without the optogenetic pulse periods and the maze epochs.

    Behavioural subsessions are the epochs with an environment other than 'none'. The pulse
    periods are OptogeneticPulsePeriods, widened to the first and last pulse (standard)."""
    end = m["lfp_duration_s"] if np.isfinite(m["lfp_duration_s"]) else m["last_spike"]
    beh = []
    if m["epochs"]:
        e = m["epochs"]
        beh = [(s, t) for s, t, env in zip(e["start_time"], e["stop_time"], e["environment"])
               if env != "none"]
    beh = sorted(beh)
    if len(beh) >= 2:
        end = beh[1][0]
    cut = list(beh)
    if m["pulse_periods"]:
        cut += list(zip(m["pulse_periods"]["start_time"], m["pulse_periods"]["stop_time"]))
    if m.get("n_pulses"):
        cut.append((m["pulse_t0"] - 1.0, m["pulse_t1"] + 1.0))
    return subtract([[0.0, end]], cut)


# ---------- single-cell measures ----------

def acg_counts(t, lo, hi, binsize=0.001, maxlag=0.3):
    """Autocorrelogram counts in bins of binsize up to maxlag (positive lags), from spikes t."""
    t = np.sort(t)
    nb = int(round(maxlag / binsize))
    counts = np.zeros(nb, np.int64)
    j0 = 0
    # pairwise differences within maxlag, vectorised over lag offsets
    for k in range(1, len(t)):
        d = t[k:] - t[:-k]
        m = d < maxlag
        if not m.any():
            break
        b = (d[m] / binsize).astype(int)
        counts += np.bincount(b, minlength=nb)[:nb]
    return counts


def burst_index(t, short=(0.002, 0.005)):
    """Burst index of the Figure 1h legend: ACG count at short lags (2-5 ms in the legend; the
    code's 3-5 ms is the variant) over the count at 200-300 ms, ACG in 1 ms bins
    (getHomecageMetrics.m, claims)."""
    c = acg_counts(t, 0, 0.3)
    s = c[int(round(short[0] * 1000)):int(round(short[1] * 1000))].sum()
    l = c[200:300].sum()
    return s / l if l > 0 else np.nan, c


def ripple_measures(trains, rip):
    """Per cell, SPW-R firing rate (spikes in ripples over total ripple duration) and
    participation (fraction of ripples with at least one spike) (getHomecageMetrics.m, claims),
    and the ripple-by-cell count matrix used for cofiring."""
    rip = np.asarray(rip).reshape(-1, 2)
    edges = rip.ravel()
    tot = np.sum(rip[:, 1] - rip[:, 0])
    counts = np.zeros((len(rip), len(trains)), np.int32)
    for j, t in enumerate(trains):
        k = np.searchsorted(edges, t, side="right")
        inside = (k % 2) == 1
        c = np.bincount((k[inside] - 1) // 2, minlength=len(rip))
        counts[:, j] = c[:len(rip)]
    rate = counts.sum(0) / tot if tot > 0 else np.full(len(trains), np.nan)
    part = (counts > 0).mean(0) if len(rip) else np.full(len(trains), np.nan)
    return rate, part, counts


def pair_corr(counts, pairs):
    """Pearson correlation of count vectors for index pairs (Methods, Cofiring analysis).
    A pair with a constant vector has no correlation (NaN), as corr gives in MATLAB."""
    x = counts.astype(float)
    x = x - x.mean(0)
    sd = np.sqrt((x ** 2).sum(0))
    out = np.full(len(pairs), np.nan)
    for n, (i, j) in enumerate(pairs):
        if sd[i] > 0 and sd[j] > 0:
            out[n] = (x[:, i] @ x[:, j]) / (sd[i] * sd[j])
    return out


# ---------- statistics ----------

def boot_kw(groups, n_boot=5000, rng=None):
    """Bootstrap Kruskal-Wallis (Methods, Statistical analysis): pool, reassign to groups of the
    same sizes with replacement, p is the fraction of null H at or above the observed."""
    from scipy.stats import kruskal
    groups = [np.asarray(g, float)[np.isfinite(g)] for g in groups]
    h = kruskal(*groups).statistic
    pool = np.concatenate(groups)
    sizes = [len(g) for g in groups]
    null = np.empty(n_boot)
    for b in range(n_boot):
        s = rng.choice(pool, size=len(pool), replace=True)
        null[b] = kruskal(*np.split(s, np.cumsum(sizes)[:-1])).statistic
    return h, float(np.mean(null >= h))


def boot_anova(groups, n_boot=5000, rng=None):
    """Bootstrap one-way ANOVA (Methods, Statistical analysis), as boot_kw with F."""
    from scipy.stats import f_oneway
    groups = [np.asarray(g, float)[np.isfinite(g)] for g in groups]
    F = f_oneway(*groups).statistic
    pool = np.concatenate(groups)
    sizes = [len(g) for g in groups]
    null = np.empty(n_boot)
    for b in range(n_boot):
        s = rng.choice(pool, size=len(pool), replace=True)
        null[b] = f_oneway(*np.split(s, np.cumsum(sizes)[:-1])).statistic
    return F, float(np.mean(null >= F))


def inverted_u(medians):
    """Inverted-U of the claims (fig1h): the highest median at E14.5 or E15.5, with E13.5 and
    E16.5 both below it."""
    k = int(np.argmax(medians))
    return k in (1, 2) and medians[0] < medians[k] and medians[3] < medians[k]


# ---------- rate maps ----------

def gauss_smooth_1d(x, fwhm_bins):
    """Gaussian smoothing with the FWHM of the Methods (9 cm on 1 cm bins), zero padded."""
    from scipy.ndimage import gaussian_filter1d
    return gaussian_filter1d(x, fwhm_bins / 2.3548, mode="constant")


def kalman_speed(t, x, q=50.0, r=1.0):
    """Speed from a constant-velocity Kalman filter of position (Methods: velocity by Kalman
    filter; its settings are not given, claims opening comment: a standard choice).
    q is the acceleration noise (cm^2/s^4 scale), r the measurement noise (cm^2)."""
    n = len(t)
    v = np.zeros(n)
    s = np.array([x[0], 0.0])
    P = np.eye(2) * 10
    for i in range(1, n):
        dt = max(t[i] - t[i - 1], 1e-3)
        F = np.array([[1, dt], [0, 1]])
        Q = q * np.array([[dt ** 4 / 4, dt ** 3 / 2], [dt ** 3 / 2, dt ** 2]])
        s = F @ s
        P = F @ P @ F.T + Q
        if np.isfinite(x[i]):
            y = x[i] - s[0]
            S = P[0, 0] + r
            K = P[:, 0] / S
            s = s + K * y
            P = P - np.outer(K, P[0])
        v[i] = s[1]
    return np.abs(v)


def skaggs_info(rate, occ):
    """Skaggs spatial information in bits/s (Methods, ref. 76): sum p_i r_i log2(r_i / r)."""
    ok = np.isfinite(rate) & (occ > 0)
    p = occ[ok] / occ[ok].sum()
    r = rate[ok]
    mr = np.sum(p * r)
    if mr <= 0:
        return np.nan
    nz = r > 0
    return float(np.sum(p[nz] * r[nz] * np.log2(r[nz] / mr)))


# ---------- per-session processing ----------

def electrode_shanks(f):
    """Physical shank of each electrode row (electrodes table, shank; chanMap kcoords)."""
    return f["general/extracellular_ephys/electrodes/shank"][:]


def ccg_pair(a, b, binsize=0.002, maxlag=0.3):
    """Cross-correlogram counts of b relative to a, bins of binsize centred on lags from -maxlag
    to +maxlag (Figure 2b: 2 ms bins over +-300 ms, extract_ccgs.m, claims)."""
    nb = int(round(maxlag / binsize))
    edges = (np.arange(-nb, nb + 2) - 0.5) * binsize
    lo = np.searchsorted(b, a - maxlag - binsize)
    hi = np.searchsorted(b, a + maxlag + binsize)
    n = hi - lo
    if n.sum() == 0:
        return np.zeros(len(edges) - 1)
    rep = np.repeat(np.arange(len(a)), n)
    start = np.repeat(lo - np.r_[0, np.cumsum(n)[:-1]], n)
    idx = np.arange(n.sum()) + start
    d = b[idx] - a[rep]
    return np.histogram(d, edges)[0].astype(float)


def ccg_sync(a, b):
    """Figure 2b synchrony of a pair (claims, fig2b reading b): the CCG z-scored against its
    outer 75 bins on each side, mean of the z-scores within +-50 ms."""
    c = ccg_pair(a, b)
    base = np.r_[c[:75], c[-75:]]
    sd = base.std()
    if sd == 0:
        return np.nan
    z = (c - base.mean()) / sd
    mid = len(c) // 2
    return float(z[mid - 25:mid + 26].mean())


def homecage_session(asset, m, ccgs=True):
    """Homecage measures of one session: per pyramidal cell the rate, burst index, SPW-R rate
    and participation; per SBD and DBD pair the SPW-R cofiring and the CCG synchrony.
    Spikes of the homecage period (homecage_intervals). Ripples are the dataset's
    (bz_FindRipples, as the Methods), kept when they start inside the homecage period."""
    with open_nwb(asset) as f:
        trains_all = spike_trains(f)
        shanks = electrode_shanks(f)
        maxel = f["units/max_electrode"][:]
        ids = f["electrodes"][:] if "electrodes" in f else None
    ct = np.array(m.get("u_putative_cell_type", [None] * m["n_units"]), dtype=object)
    lr = np.array(m.get("u_light_responsive", [False] * m["n_units"]), bool)
    pyr = np.where(ct == "Pyramidal Cell")[0]
    hc = homecage_intervals(m)
    hc_dur = float(np.sum(hc[:, 1] - hc[:, 0]))
    trains = [trains_all[i][in_intervals(trains_all[i], hc)] for i in pyr]
    rip = np.c_[m["rip_start"], m["rip_stop"]]
    keep = in_intervals(rip[:, 0], hc) & in_intervals(rip[:, 1], hc)
    rip_hc = rip[keep]
    rrate, rpart, counts = ripple_measures(trains, rip_hc)
    cells = []
    for k, i in enumerate(pyr):
        t = trains[k]
        b25, c = burst_index(t)
        s35 = c[3:5].sum()
        l = c[200:300].sum()
        cells.append({"session": m["session_id"], "subject": m["subject_id"],
                      "birthdate": m["birthdate"], "unit": int(i), "lr": bool(lr[i]),
                      "rate": len(t) / hc_dur, "burst": b25,
                      "burst35": s35 / l if l > 0 else np.nan,
                      "rip_rate": float(rrate[k]), "rip_part": float(rpart[k]),
                      "shank": int(shanks[maxel[i]]) if maxel[i] < len(shanks) else -1,
                      "maxel": int(maxel[i])})
    lrk = [k for k, i in enumerate(pyr) if lr[i]]
    nrk = [k for k, i in enumerate(pyr) if not lr[i]]
    sbd = [(a, b) for n, a in enumerate(lrk) for b in lrk[n + 1:]]
    dbd = [(a, b) for a in lrk for b in nrk]
    pairs = sbd + dbd
    rc = pair_corr(counts, pairs)
    sync = [ccg_sync(trains[a], trains[b]) if ccgs else np.nan for a, b in pairs]
    pr = [{"session": m["session_id"], "subject": m["subject_id"], "birthdate": m["birthdate"],
           "sbd": n < len(sbd), "a": int(pyr[a]), "b": int(pyr[b]), "rip_corr": rc[n],
           "sync": sync[n], "shank_a": cells[a]["shank"], "shank_b": cells[b]["shank"]}
          for n, (a, b) in enumerate(pairs)]
    with np.errstate(invalid="ignore", divide="ignore"):
        cm = np.corrcoef(counts.T.astype(float)) if len(pyr) > 1 else np.zeros((len(pyr), len(pyr)))
    info = {"session": m["session_id"], "rip_corr_mat": cm.astype(np.float32),
            "hc_dur": hc_dur, "n_rip_hc": int(keep.sum()),
            "n_rip": len(rip), "rip_hc_dur": (rip_hc[:, 1] - rip_hc[:, 0]).tolist()}
    return cells, pr, info


def behaviour_epochs(m):
    """Behavioural subsessions (epochs whose environment is not 'none'), in time order. The
    first is the familiar figure-eight (get_corrBeh_famnov.m, "1 is always familiar"; claims)."""
    e = m["epochs"] or {"environment": [], "start_time": [], "stop_time": [], "epoch_name": []}
    out = [(s, t, env, n) for s, t, env, n in zip(e["start_time"], e["stop_time"],
                                                     e["environment"], e["epoch_name"])
           if env != "none"]
    return sorted(out)


def linear_series_for(m, t0, t1, env=None):
    """Name of the LinearizedPosition series whose timestamps lie inside [t0, t1] and, when the
    series name carries an environment, whose environment is the epoch's."""
    for k, v in m["series"].items():
        if k.startswith("LinearizedPosition/") and v["t0"] >= t0 - 1 and v["t1"] <= t1 + 1:
            suffix = k.split("_", 1)[1] if "_" in k.split("/")[1] else None
            if env is not None and suffix is not None and suffix != env:
                continue
            return k
    return None


SPEED_MIN = 1.5  # cm/s, Methods, Spatial ratemap analyses
FWHM_LIN = 9.0  # cm, Methods
NBINS = 205  # 1 cm bins over the 205 cm trial (Methods, Behavior; get_corrBeh_v3.m, claims)


def linear_maps(f, m, t0, t1, trains, nbins=NBINS, fwhm=FWHM_LIN, smin=SPEED_MIN, env=None):
    """Left and right rate maps on a linearized maze between t0 and t1 (Methods, Spatial
    ratemap analyses): per trial, speed from a Kalman filter of the linearized position, samples
    with speed > 1.5 cm/s, spikes and time in 1 cm bins per trial type, each smoothed with a
    9 cm FWHM Gaussian, rate = smoothed spikes / smoothed time, never-visited bins NaN.
    Trial type is the trials table's visited_arm. Returns maps (2, ncells, nbins), the raw
    occupancy (2, nbins) in s, and per-trial bookkeeping."""
    name = linear_series_for(m, t0, t1, env)
    g = f["processing/behavior/" + name]
    x = g["data"][:].astype(float)
    if x.ndim > 1:
        x = x[:, 0]
    ts = g["timestamps"][:]
    dt = float(np.median(np.diff(ts)))
    tr = m["trials"]
    occ = np.zeros((2, nbins))
    spk = np.zeros((2, len(trains), nbins))
    info = []
    for s, e, arm in zip(tr["start_time"], tr["stop_time"], tr["visited_arm"]):
        if s < t0 - 1 or e > t1 + 1 or arm not in ("left", "right"):
            continue
        side = 0 if arm == "left" else 1
        k = np.where((ts >= s) & (ts <= e) & np.isfinite(x))[0]
        if len(k) < 5:
            continue
        sp = kalman_speed(ts[k], x[k])
        b = np.clip(np.floor(x[k]).astype(int), 0, nbins - 1)
        run = sp > smin
        occ[side] += np.bincount(b[run], minlength=nbins)[:nbins] * dt
        info.append({"arm": arm, "x0": float(np.nanmin(x[k])), "x1": float(np.nanmax(x[k])),
                     "dur": float(e - s)})
        for c, t in enumerate(trains):
            tt = t[(t >= ts[k[0]]) & (t <= ts[k[-1]])]
            if len(tt) == 0:
                continue
            j = np.clip(np.searchsorted(ts[k], tt), 0, len(k) - 1)
            ok = run[j]
            spk[side, c] += np.bincount(b[j[ok]], minlength=nbins)[:nbins]
    so = np.stack([gauss_smooth_1d(o, fwhm) for o in occ])
    ss = np.stack([[gauss_smooth_1d(s_, fwhm) for s_ in spk[side]] for side in range(2)])
    with np.errstate(invalid="ignore", divide="ignore"):
        maps = ss / so[:, None, :]
    for side in range(2):
        maps[side][:, occ[side] == 0] = np.nan
    return maps, occ, info, dt


def maze_session(asset, m):
    """Familiar figure-eight rate maps of all pyramidal cells of one session."""
    ep = behaviour_epochs(m)
    if not ep:
        return None
    t0, t1, env, name = ep[0]
    ct = np.array(m.get("u_putative_cell_type", [None] * m["n_units"]), dtype=object)
    pyr = np.where(ct == "Pyramidal Cell")[0]
    lr = np.array(m["u_light_responsive"], bool)
    with open_nwb(asset) as f:
        tr = spike_trains(f, pyr)
        shanks = electrode_shanks(f)
        maxel = f["units/max_electrode"][:]
        maps, occ, info, dt = linear_maps(f, m, t0, t1, tr)
    return {"session": m["session_id"], "subject": m["subject_id"], "birthdate": m["birthdate"],
            "env": env, "pyr": pyr, "lr": lr[pyr], "shank": shanks[maxel[pyr]], "maps": maps,
            "occ": occ, "trials": info, "dt": dt,
            "trial_counts": {a: sum(1 for i in info if i["arm"] == a) for a in ("left", "right")}}


def run_sessions(func, metas, workers=4):
    """Run func(asset, meta) over sessions in worker processes; results in the order given."""
    A = {a["path"]: a for a in assets()}
    with cf.ProcessPoolExecutor(workers) as ex:
        futs = [ex.submit(func, A[m["path"]], m) for m in metas]
        return [fu.result() for fu in futs]


# ---------- theta ----------

def _sos(lo, hi, fs=1250.0, order=4):
    """Fourth-order Chebyshev band-pass (Methods); type II with 20 dB stopband as buzcode's
    bz_Filter default (standard), applied forward and backward."""
    from scipy.signal import cheby2
    return cheby2(order, 20, [lo, hi], btype="band", fs=fs, output="sos")


def pick_theta_channel(f, m, win_s=52.4288):
    """The theta channel (Methods, Theta-cycle detection): 'a channel with a positive sharp wave
    (that is, above the center of the pyramidal layer)'. The paper does not say how it was
    picked from the channels that qualify (assumption): in one LFP chunk of about 52 s during
    homecage non-REM sleep with the most SPW-Rs, the pyramidal layer centre is the good channel
    with the largest ripple-band (130-200 Hz) power at the ripple peaks; the theta channel is
    the good channel with a positive mean sharp wave (2-40 Hz LFP at 0 to 50 ms after the
    peaks, against the chunk mean) that has the largest ripple power, so that it lies just
    above the centre, preferring the shank of the pyramidal layer centre and taking any shank
    when that shank has none. With no such channel at all, the pyramidal layer channel is used.
    Returns (theta channel row, pyramidal channel row, details)."""
    from scipy.signal import sosfiltfilt
    lfp = f["processing/ecephys/LFP/LFP/data"]
    fs = float(f["processing/ecephys/LFP/LFP/starting_time"].attrs["rate"])
    n = int(round(win_s * fs))
    peaks = f["processing/ecephys/Ripples/peaks"][:]
    ss = m["sleep"]
    nrem = np.array([(a, b) for a, b, l in zip(ss["start_time"], ss["stop_time"], ss["label"])
                     if l == "Non-REM"]).reshape(-1, 2)
    hc = homecage_intervals(m)
    ok = in_intervals(peaks, merge(nrem)) & in_intervals(peaks, hc)
    p = peaks[ok] if ok.sum() > 20 else peaks
    blk = np.floor(p * fs / n).astype(int)
    b = np.bincount(blk).argmax()
    x = lfp[b * n:(b + 1) * n, :].astype(float)
    t0 = b * n / fs
    pk = ((p[blk == b] - t0) * fs).astype(int)
    pk = pk[(pk > 100) & (pk < len(x) - 100)]
    rip = sosfiltfilt(_sos(130, 200, fs), x, axis=0)
    sw = sosfiltfilt(_sos(2, 40, fs), x, axis=0)
    w = np.arange(-30, 31)
    rpow = np.array([np.mean(rip[pk[:, None] + w, c] ** 2) for c in range(x.shape[1])])
    w2 = np.arange(0, 63)
    swa = np.array([np.mean(sw[pk[:, None] + w2, c]) - np.mean(sw[:, c])
                    for c in range(x.shape[1])])
    el = f["general/extracellular_ephys/electrodes"]
    bad = el["bad_channel"][:] if "bad_channel" in el else np.zeros(x.shape[1], bool)
    shank = el["shank"][:]
    rp = np.where(bad, -np.inf, rpow)
    pyr_ch = int(np.argmax(rp))
    cand = np.where((shank == shank[pyr_ch]) & ~bad & (swa > 0))[0]
    where = "same shank"
    if not len(cand):
        cand = np.where(~bad & (swa > 0))[0]
        where = "other shank"
    th = int(cand[np.argmax(rpow[cand])]) if len(cand) else pyr_ch
    return th, pyr_ch, {"n_ripples": int(len(pk)), "sw_theta": float(swa[th]),
                        "sw_pyr": float(swa[pyr_ch]), "positive_found": bool(len(cand)),
                        "where": where if len(cand) else "none, pyramidal channel"}


def read_channel(f, ch, block=2 ** 16 * 16):
    lfp = f["processing/ecephys/LFP/LFP/data"]
    conv = float(lfp.attrs.get("conversion", 1.0))
    out = np.empty(lfp.shape[0], np.float32)
    for s in range(0, lfp.shape[0], block):
        out[s:s + block] = lfp[s:s + block, ch]
    return out * conv * 1e6  # microvolts


def theta_phase_amp(x, fs=1250.0):
    """6-12 Hz band, Hilbert amplitude and phase (Methods); phase 0 at theta peaks."""
    from scipy.fft import next_fast_len
    from scipy.signal import hilbert, sosfiltfilt
    y = sosfiltfilt(_sos(6, 12, fs), x.astype(np.float64)).astype(np.float32)
    n = len(y)
    z = hilbert(y, N=next_fast_len(n))[:n]
    return np.abs(z).astype(np.float32), np.angle(z).astype(np.float32)


def theta_cycles(amp, ph, fs=1250.0):
    """Theta cycles (Methods): inside intervals with amplitude above mean + 1 SD, cycles between
    consecutive 0 degree crossings (peaks), both crossings inside one such interval."""
    hi = amp > amp.mean() + amp.std()
    cross = np.where((ph[:-1] < 0) & (ph[1:] >= 0) & (np.abs(ph[1:] - ph[:-1]) < np.pi))[0] + 1
    lab = np.cumsum(np.r_[0, np.diff(hi.astype(np.int8)) != 0])
    c0, c1 = cross[:-1], cross[1:]
    keep = hi[c0] & hi[c1] & (lab[c0] == lab[c1])
    return np.c_[c0[keep], c1[keep]] / fs


def rayleigh(ph):
    """Rayleigh test of circular uniformity (approximation of Zar, as CircStat circ_rtest)."""
    n = len(ph)
    if n < 2:
        return np.nan, np.nan, np.nan
    C, S = np.cos(ph).sum(), np.sin(ph).sum()
    R = np.hypot(C, S)
    r = R / n
    z = R ** 2 / n
    p = np.exp(np.sqrt(1 + 4 * n + 4 * (n ** 2 - R ** 2)) - (1 + 2 * n))
    return float(min(p, 1.0)), float(np.mod(np.arctan2(S, C), 2 * np.pi)), float(r)


def state_intervals(m, label):
    ss = m["sleep"]
    return merge([(a, b) for a, b, l in zip(ss["start_time"], ss["stop_time"], ss["label"])
                  if l == label])


def intersect(a, b):
    a, b = merge(a), merge(b)
    out = []
    for s, e in a:
        for c, d in b:
            lo, hi = max(s, c), min(e, d)
            if hi > lo:
                out.append([lo, hi])
    return np.array(out).reshape(-1, 2)


def _mask_intervals(mask, fs):
    d = np.diff(np.r_[0, mask.astype(np.int8), 0])
    s, e = np.where(d == 1)[0], np.where(d == -1)[0]
    return np.c_[s, e] / fs


def theta_session(asset, m, novel=False):
    """Theta measures of one session. Homecage wake and REM (homecage_intervals with the lab's
    sleep states): for each light-responsive pyramidal cell the Rayleigh p, preferred phase and
    mean resultant length in wake (amplitude above its mean) and in REM (all); per SBD and DBD
    pair the theta-cycle cofiring (Methods, Cofiring analysis; cycles with both edges in
    homecage WAKE, get_corrHome_v2.m). For a novel session also the theta-related rate of every
    pyramidal cell in each behavioural subsession, with and without the wake restriction."""
    fs = 1250.0
    with open_nwb(asset) as f:
        th, pch, det = pick_theta_channel(f, m)
        x = read_channel(f, th)
        ct = np.array(m["u_putative_cell_type"], dtype=object)
        pyr = np.where(ct == "Pyramidal Cell")[0]
        trains = spike_trains(f, pyr)
    lr = np.array(m["u_light_responsive"], bool)[pyr]
    amp, ph = theta_phase_amp(x)
    del x
    hc = homecage_intervals(m)
    wake = intersect(state_intervals(m, "Awake"), hc)
    rem = intersect(state_intervals(m, "REM"), hc)
    wake_hi = intersect(wake, _mask_intervals(amp > amp.mean(), fs))
    cells = []
    for k in np.where(lr)[0]:
        t = trains[k]
        row = {"session": m["session_id"], "subject": m["subject_id"],
               "birthdate": m["birthdate"], "unit": int(pyr[k])}
        for st, iv in (("wake", wake_hi), ("rem", rem)):
            tt = t[in_intervals(t, iv)]
            idx = np.clip((tt * fs).astype(int), 0, len(ph) - 1)
            p, mu, r = rayleigh(ph[idx].astype(float))
            row.update({st + "_p": p, st + "_phase": mu, st + "_mrl": r, st + "_n": len(tt)})
            # clock control: the same spikes against the phase 10.3 s later
            sh = np.clip(((tt + 10.3) * fs).astype(int), 0, len(ph) - 1)
            ps, _, rs = rayleigh(ph[sh].astype(float))
            row.update({st + "_p_shift": ps, st + "_mrl_shift": rs})
        cells.append(row)
    cyc = theta_cycles(amp, ph, fs)
    out = {"session": m["session_id"], "theta_ch": th, "pyr_ch": pch, **det,
           "n_cycles": len(cyc), "wake_s": float(np.sum(np.diff(wake, axis=1)))}
    W = state_intervals(m, "Awake")
    cw = cyc[in_intervals(cyc[:, 0], intersect(W, hc)) & in_intervals(cyc[:, 1], intersect(W, hc))]
    out["n_cycles_hc_wake"] = len(cw)
    counts = np.zeros((len(cw), len(pyr)), np.int32)
    edges = cw.ravel()
    for j, t in enumerate(trains):
        kk = np.searchsorted(edges, t, side="right")
        ins = kk % 2 == 1
        counts[:, j] = np.bincount((kk[ins] - 1) // 2, minlength=len(cw))[:len(cw)]
    lrk, nrk = np.where(lr)[0], np.where(~lr)[0]
    sbd = [(a, b) for n, a in enumerate(lrk) for b in lrk[n + 1:]]
    dbd = [(a, b) for a in lrk for b in nrk]
    tc = pair_corr(counts, sbd + dbd)
    pairs = [{"session": m["session_id"], "subject": m["subject_id"],
              "birthdate": m["birthdate"], "sbd": n < len(sbd), "a": int(pyr[a]),
              "b": int(pyr[b]), "theta_corr": tc[n]} for n, (a, b) in enumerate(sbd + dbd)]
    with np.errstate(invalid="ignore", divide="ignore"):
        out["theta_corr_mat"] = (np.corrcoef(counts.T.astype(float)) if len(pyr) > 1
                                 else np.zeros((len(pyr), len(pyr)))).astype(np.float32)
    rates = []
    if novel:
        for n_ep, (t0, t1, env, name) in enumerate(behaviour_epochs(m)):
            sel = (cyc[:, 0] >= t0) & (cyc[:, 1] <= t1)
            for restrict in (True, False):
                c = cyc[sel]
                if restrict:
                    c = c[in_intervals(c[:, 0], W) & in_intervals(c[:, 1], W)]
                dur = float(np.sum(c[:, 1] - c[:, 0]))
                e = c.ravel()
                for j, t in enumerate(trains):
                    kk = np.searchsorted(e, t, side="right")
                    rates.append({"session": m["session_id"], "unit": int(pyr[j]),
                                  "lr": bool(lr[j]), "epoch": n_ep, "env": env,
                                  "wake_only": restrict, "n_cycles": len(c), "dur": dur,
                                  "spikes": int(np.sum(kk % 2 == 1)),
                                  "rate": np.sum(kk % 2 == 1) / dur if dur > 0 else np.nan})
    return cells, pairs, out, rates


def theta_session_novel(asset, m):
    return theta_session(asset, m, novel=True)


# ---------- monosynaptic connections ----------

MONO_BIN = 0.0008  # s, Methods, Monosynaptic connection analyses
MONO_LAG = 0.05  # s, half-width of the CCG window (standard; wide enough for the baseline)


def hollow_gauss(sd_bins, hollow=0.6):
    """Hollowed Gaussian kernel (Stark and Abeles 2009, as English et al. 2017): the centre bin
    weight reduced by the hollow fraction, kernel normalised to sum 1."""
    half = int(np.ceil(3 * sd_bins))
    k = np.exp(-0.5 * (np.arange(-half, half + 1) / sd_bins) ** 2)
    k[half] *= (1 - hollow)
    return k / k.sum()


def ccg_lags(a, b, binsize=MONO_BIN, maxlag=MONO_LAG):
    """CCG counts of b around a, bins of binsize centred on 0, lags -maxlag..maxlag."""
    nb = int(round(maxlag / binsize))
    edges = (np.arange(-nb, nb + 2) - 0.5) * binsize
    lo = np.searchsorted(b, a - maxlag - binsize)
    hi = np.searchsorted(b, a + maxlag + binsize)
    n = hi - lo
    if n.sum() == 0:
        return np.zeros(len(edges) - 1), edges
    rep = np.repeat(np.arange(len(a)), n)
    start = np.repeat(lo - np.r_[0, np.cumsum(n)[:-1]], n)
    idx = np.arange(n.sum()) + start
    return np.histogram(b[idx] - a[rep], edges)[0].astype(float), edges


def _conv_reflect(c, k):
    h = len(k) // 2
    x = np.r_[c[h:0:-1], c, c[-2:-h - 2:-1]]
    return np.convolve(x, k, mode="valid")


def mono_test(c, sd_s=0.015, alpha=0.001):
    """Monosynaptic pyramidal-to-interneuron test (Methods: 'identical to the reliability test',
    English et al. 2017): baseline from a hollowed Gaussian (15 ms s.d., the reliability test's
    value) convolved with the CCG; the bins at 0.8 to 2.8 ms lags (the window of the spike
    transmission measure, Methods) must hold a count above baseline (Poisson, upper tail) and
    the peak bin a count above the largest of the mirror bins at negative lags (Poisson),
    each at alpha 0.001 Bonferroni corrected for the bins tested."""
    from scipy.stats import poisson
    nb = (len(c) - 1) // 2
    base = _conv_reflect(c, hollow_gauss(sd_s / MONO_BIN))
    win = nb + np.arange(1, 4)  # lags 0.8, 1.6, 2.4 ms (bin centres within 0.8 to 2.8 ms)
    a = alpha / len(win)
    p_base = poisson.sf(c[win] - 1, np.maximum(base[win], 1e-9))
    pk = win[np.argmax(c[win])]
    mirror = nb - np.arange(1, 4)
    p_ant = poisson.sf(c[pk] - 1, max(c[mirror].max(), 1e-9))
    return bool(np.any(p_base < a) and p_ant < a)


def mono_p(c, sd_s=0.015):
    """The two p values of mono_test (smallest baseline p over the window, and the peak against
    the mirror bins), so that the count can be shown at other alphas."""
    from scipy.stats import poisson
    nb = (len(c) - 1) // 2
    base = _conv_reflect(c, hollow_gauss(sd_s / MONO_BIN))
    win = nb + np.arange(1, 4)
    p_base = poisson.sf(c[win] - 1, np.maximum(base[win], 1e-9))
    pk = win[np.argmax(c[win])]
    mirror = nb - np.arange(1, 4)
    return float(p_base.min()), float(poisson.sf(c[pk] - 1, max(c[mirror].max(), 1e-9)))


def transmission(a, b, sd_s=0.008):
    """Spike transmission probability (Methods): CCG of presynaptic spikes a, divided by their
    number, minus the baseline from an 8 ms s.d. hollowed Gaussian, summed over 0.8-2.8 ms lags
    where it exceeds the baseline."""
    if len(a) < 20:
        return np.nan
    c, _ = ccg_lags(a, b, maxlag=0.03)
    pr = c / len(a)
    base = _conv_reflect(pr, hollow_gauss(sd_s / MONO_BIN))
    nb = (len(c) - 1) // 2
    win = nb + np.arange(1, 4)
    d = pr[win] - base[win]
    return float(np.sum(d[d > 0]))


ISI_EDGES = np.logspace(np.log10(0.005), np.log10(1.0), 16)  # 15 log bins, 5-1000 ms (claims)


def mono_session(asset, m):
    """Pyramidal-to-interneuron connections of one session, from spikes outside the light pulse
    periods; per connection the transmission probability for presynaptic spikes with preceding
    ISI of 10 to 40 ms (claims, fig7ce) and per ISI bin (fig7d)."""
    ct = np.array(m["u_putative_cell_type"], dtype=object)
    pyr = np.where(ct == "Pyramidal Cell")[0]
    inn = np.where(np.isin(ct, ["Narrow Interneuron", "Wide Interneuron"]))[0]
    lr = np.array(m["u_light_responsive"], bool)
    with open_nwb(asset) as f:
        tr = spike_trains(f)
    cut = []
    if m["pulse_periods"]:
        cut += list(zip(m["pulse_periods"]["start_time"], m["pulse_periods"]["stop_time"]))
    if m.get("n_pulses"):
        cut.append((m["pulse_t0"] - 1.0, m["pulse_t1"] + 1.0))
    keep = subtract([[0, m["last_spike"] + 1]], cut)
    tr = {i: tr[i][in_intervals(tr[i], keep)] for i in np.r_[pyr, inn]}
    conn = np.zeros((len(pyr), len(inn)), bool)
    rows, pvals = [], []
    for p_, i in enumerate(pyr):
        a = tr[i]
        if len(a) < 100:
            continue
        isi = np.r_[np.inf, np.diff(a)]
        for q, j in enumerate(inn):
            c, _ = ccg_lags(a, tr[j])
            if c.sum() < 50:
                continue
            pb, pa = mono_p(c)
            pvals.append((p_, q, pb, pa))
            if pb < 0.001 / 3 and pa < 0.001 / 3:
                conn[p_, q] = True
                sel = (isi >= 0.010) & (isi <= 0.040)
                st = transmission(a[sel], tr[j])
                by = [transmission(a[(isi >= lo) & (isi < hi)], tr[j])
                      for lo, hi in zip(ISI_EDGES[:-1], ISI_EDGES[1:])]
                rows.append({"session": m["session_id"], "subject": m["subject_id"],
                             "birthdate": m["birthdate"], "pre": int(i), "post": int(j),
                             "pre_lr": bool(lr[i]), "stp": st, "stp_isi": by})
    return {"session": m["session_id"], "subject": m["subject_id"],
            "birthdate": m["birthdate"], "pyr": pyr, "inn": inn, "lr": lr[pyr],
            "conn": conn, "rows": rows, "pvals": np.array(pvals).reshape(-1, 4)}


def convergence(conn, a, b):
    """Shared postsynaptic interneurons over the union of targets (Methods); NaN with none."""
    u = np.sum(conn[a] | conn[b])
    return np.sum(conn[a] & conn[b]) / u if u > 0 else np.nan


def novel_session(asset, m):
    """Rate maps of all pyramidal cells in the familiar figure-eight (first subsession) and in
    each later subsession with a linearized position in cm (novel figure-eight and linear
    tracks). Open fields are left out: their x and y are in the lab's units with no scale
    (dataset description), so the 1 cm bins of the Methods cannot be formed."""
    ep = behaviour_epochs(m)
    ct = np.array(m["u_putative_cell_type"], dtype=object)
    pyr = np.where(ct == "Pyramidal Cell")[0]
    lr = np.array(m["u_light_responsive"], bool)
    out = []
    with open_nwb(asset) as f:
        tr = spike_trains(f, pyr)
        for n, (t0, t1, env, name) in enumerate(ep):
            ser = linear_series_for(m, t0, t1, env)
            if ser is None:
                out.append({"epoch": n, "env": env, "maps": None, "why": "no linearized series "
                            "inside the epoch"})
                continue
            g = f["processing/behavior/" + ser]
            xmax = float(np.nanmax(g["data"][:]))
            nbins = NBINS if n == 0 else int(np.ceil(xmax))
            maps, occ, info, dt = linear_maps(f, m, t0, t1, tr, nbins=nbins, env=env)
            out.append({"epoch": n, "env": env, "maps": maps, "occ": occ, "nbins": nbins,
                        "trial_counts": {a: sum(1 for i in info if i["arm"] == a)
                                         for a in ("left", "right")}})
    return {"session": m["session_id"], "subject": m["subject_id"],
            "birthdate": m["birthdate"], "pyr": pyr, "lr": lr[pyr], "epochs": out}


def clock_checks(asset, m, shift=1.0):
    """Contrasts that show that spikes share the clock of the pulses, the ripples and the
    position (protocol, author step 2): for light-responsive cells, spikes in the 10 ms after
    each pulse onset against the 10 ms windows 'shift' s later; for pyramidal cells, the SPW-R
    rate with the ripple times as given against shifted by 'shift' s; for maze sessions, the
    median spatial information with spikes as given against spikes shifted by 30 s."""
    ct = np.array(m["u_putative_cell_type"], dtype=object)
    pyr = np.where(ct == "Pyramidal Cell")[0]
    lr = np.array(m["u_light_responsive"], bool)
    with open_nwb(asset) as f:
        tr = spike_trains(f)
        on = f["intervals/OptogeneticPulses/start_time"][:]
        out = {"session": m["session_id"]}
        lrc = [tr[i] for i in np.where(lr)[0]]
        def win_count(ts, starts):
            iv = np.c_[starts, starts + 0.010]
            return sum(int(in_intervals(t, iv).sum()) for t in ts)
        out["pulse_true"] = win_count(lrc, on)
        out["pulse_shift"] = win_count(lrc, on + shift)
        rip = np.c_[m["rip_start"], m["rip_stop"]]
        r0, _, _ = ripple_measures([tr[i] for i in pyr], rip)
        r1, _, _ = ripple_measures([tr[i] for i in pyr], rip + shift)
        out["rip_rate_true"] = float(np.median(r0))
        out["rip_rate_shift"] = float(np.median(r1))
        ep = behaviour_epochs(m)
        if ep and m["subject_id"] in FAMILIAR_MICE:
            t0, t1, env, name = ep[0]
            trains = [tr[i] for i in pyr]
            for lab, sh in (("true", 0.0), ("shift", 30.0)):
                tt = [t + sh for t in trains]
                maps, occ, info, dt = linear_maps(f, m, t0, t1, tt)
                si = [skaggs_info(np.r_[maps[0, c], maps[1, c]], np.r_[occ[0], occ[1]])
                      for c in range(len(trains))]
                out["si_" + lab] = float(np.nanmedian(si))
    return out
