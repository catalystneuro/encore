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
        m["u_columns"] = sorted(u.keys())
        m["wf_shape"] = list(u["waveform_mean"].shape) if "waveform_mean" in u else None
        el = f["general/extracellular_ephys/electrodes"]
        m["n_electrodes"] = int(el["id"].shape[0])
        m["probe_sides"] = (sorted(set(_s(x) for x in el["probe_side"][:]))
                            if "probe_side" in el else [])
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
        # rounded before the floor, so that a lag of exactly k bins is not truncated into bin k - 1
        b = np.floor(np.round(d[m] / binsize, 6)).astype(int)
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

def boot_kw(groups, n_boot=5000, rng=None, chunk=500):
    """Bootstrap Kruskal-Wallis (Methods, Statistical analysis): pool, reassign to groups of the
    same sizes with replacement, p is the fraction of null H at or above the observed. The null
    statistics are computed in blocks of resamplings at once (kw_rows)."""
    from scipy.stats import kruskal
    groups = [np.asarray(g, float)[np.isfinite(g)] for g in groups]
    h = kruskal(*groups).statistic
    pool = np.concatenate(groups)
    sizes = [len(g) for g in groups]
    null = np.concatenate([kw_rows(pool[rng.integers(0, len(pool), (min(chunk, n_boot - i), len(pool)))],
                                   sizes) for i in range(0, n_boot, chunk)])
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
    """Shank of each electrode row (electrodes table, shank; chanMap kcoords). Files with 128
    channels have probe_side Front and Back: electrodes on both faces of the same four shanks
    (the same rel_x on both faces), so a shank is the shank number whatever the face. The
    paper's pair counts by shank distance (Figure 5d, Extended Data Figure 10d) are found only
    this way (notebook, fig5d)."""
    return f["general/extracellular_ephys/electrodes/shank"][:].astype(int)


def electrode_columns(f):
    """One column of electrodes per shank face: shank + 100 on the Back face. Used for the LFP
    depth profiles (pick_theta_channel), so that each profile runs along one column."""
    el = f["general/extracellular_ephys/electrodes"]
    sh = el["shank"][:].astype(int)
    if "probe_side" in el:
        side = np.array([_s(x) for x in el["probe_side"][:]])
        sh = sh + 100 * (side == "Back")
    return sh


def electrode_xy(f):
    """Position of each electrode row on its probe (rel_x, rel_y, um; rel_y rises towards the
    top of the shank)."""
    el = f["general/extracellular_ephys/electrodes"]
    return el["rel_x"][:].astype(float), el["rel_y"][:].astype(float)


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
        cols = electrode_columns(f)
        ex, ey = electrode_xy(f)
        el = f["general/extracellular_ephys/electrodes"]
        bad = el["bad_channel"][:] if "bad_channel" in el else np.zeros(len(shanks), bool)
        maxel = f["units/max_electrode"][:]
        ct = np.array(m.get("u_putative_cell_type", [None] * m["n_units"]), dtype=object)
        pyr = np.where(ct == "Pyramidal Cell")[0]
        wf = f["units/waveform_mean"]
        wf = wf[:][pyr].astype(np.float32) if len(pyr) else None
    lr = np.array(m.get("u_light_responsive", [False] * m["n_units"]), bool)
    # mean waveforms as (units, channels, samples); the channel axis is the one as long as the
    # electrodes table
    if wf is not None and wf.shape[1] != len(shanks):
        wf = np.swapaxes(wf, 1, 2)
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
                      "col": int(cols[maxel[i]]), "x": float(ex[maxel[i]]), "y": float(ey[maxel[i]]),
                      "maxel": int(maxel[i])})
    lrk = [k for k, i in enumerate(pyr) if lr[i]]
    nrk = [k for k, i in enumerate(pyr) if not lr[i]]
    sbd = [(a, b) for n, a in enumerate(lrk) for b in lrk[n + 1:]]
    dbd = [(a, b) for a in lrk for b in nrk]
    pairs = sbd + dbd
    rc = pair_corr(counts, pairs)
    sync = [ccg_sync(trains[a], trains[b]) if ccgs else np.nan for a, b in pairs]
    # ed10: for same-shank pairs, the distance between the maximum-waveform channels and the
    # waveform profile distance, the L2 norm of the difference of the mean waveforms concatenated
    # over the shank's good channels (Extended Data Fig. 2d-f; the code's form divides it by the
    # number of good channels)
    wdist = []
    for a, b in pairs:
        ca, cb = cells[a], cells[b]
        if ca["shank"] != cb["shank"] or wf is None:
            wdist.append((np.nan, np.nan, np.nan))
            continue
        ch = np.where((shanks == ca["shank"]) & ~bad)[0]
        d = float(np.linalg.norm(wf[a][ch] - wf[b][ch]))
        wdist.append((d, d / len(ch), float(np.hypot(ca["x"] - cb["x"], ca["y"] - cb["y"]))))
    pr = [{"session": m["session_id"], "subject": m["subject_id"], "birthdate": m["birthdate"],
           "sbd": n < len(sbd), "a": int(pyr[a]), "b": int(pyr[b]), "rip_corr": rc[n],
           "sync": sync[n], "shank_a": cells[a]["shank"], "shank_b": cells[b]["shank"],
           "wf_dist": wdist[n][0], "wf_dist_code": wdist[n][1], "el_dist": wdist[n][2]}
          for n, (a, b) in enumerate(pairs)]
    with np.errstate(invalid="ignore", divide="ignore"):
        cm = np.corrcoef(counts.T.astype(float)) if len(pyr) > 1 else np.zeros((len(pyr), len(pyr)))
    info = {"session": m["session_id"], "rip_corr_mat": cm.astype(np.float32),
            "active": np.packbits(counts > 0, axis=0), "n_rip_rows": counts.shape[0],
            "lr_cols": np.array(lrk, int), "nr_cols": np.array(nrk, int),
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
        ex, ey = electrode_xy(f)
        maxel = f["units/max_electrode"][:]
        maps, occ, info, dt = linear_maps(f, m, t0, t1, tr)
    return {"session": m["session_id"], "subject": m["subject_id"], "birthdate": m["birthdate"],
            "env": env, "pyr": pyr, "lr": lr[pyr], "shank": shanks[maxel[pyr]], "x": ex[maxel[pyr]],
            "y": ey[maxel[pyr]], "unit": pyr, "maps": maps,
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
    (that is, above the center of the pyramidal layer)'. How it was picked among the channels
    that qualify is not given (assumption). In one LFP chunk of about 52 s of homecage non-REM
    sleep with the most SPW-Rs:
    - the pyramidal layer centre is the good channel with the largest ripple-band (130-200 Hz)
      power at the ripple peaks;
    - the sharp wave of a channel is its mean LFP (uV) 0 to 50 ms after the ripple peaks minus
      its mean 100 to 50 ms before them (a pre-ripple baseline, so that slow drift common to all
      channels does not set the sign);
    - the theta channel is a good channel on the centre's shank with a positive sharp wave and
      larger rel_y than the centre (above it: 320 of the 327 positive channels of the centres'
      shanks lie there, printed in the notebook), the one with the largest ripple power, that
      is, the qualifying channel nearest the centre. Both halves of the Methods' phrase are
      required (verifier, round 2: a positive channel below the centre does not follow it).
      When that shank has none, the same is done on the other shanks, each against its own
      centre. When no shank has one, the good channel next to the centre with larger rel_y is
      used and the session is flagged.
    The ripples are those in homecage non-REM sleep; in a session with 20 or fewer of them (the
    two sessions without non-REM sleep, e13_1f1_200305 and e13_1f1_200307) all ripples are used.
    Returns (theta channel row, pyramidal channel row, details)."""
    from scipy.signal import sosfiltfilt
    lfp = f["processing/ecephys/LFP/LFP/data"]
    conv = float(lfp.attrs.get("conversion", 1.0)) * 1e6
    fs = float(f["processing/ecephys/LFP/LFP/starting_time"].attrs["rate"])
    n = int(round(win_s * fs))
    peaks = f["processing/ecephys/Ripples/peaks"][:]
    nrem = state_intervals(m, "Non-REM")
    hc = homecage_intervals(m)
    ok = in_intervals(peaks, nrem) & in_intervals(peaks, hc)
    all_ripples = ok.sum() <= 20
    p = peaks if all_ripples else peaks[ok]
    blk = np.floor(p * fs / n).astype(int)
    b = np.bincount(blk).argmax()
    x = lfp[b * n:(b + 1) * n, :].astype(float) * conv
    t0 = b * n / fs
    pk = ((p[blk == b] - t0) * fs).astype(int)
    pk = pk[(pk > 130) & (pk < len(x) - 130)]
    rip = sosfiltfilt(_sos(130, 200, fs), x, axis=0)
    w = np.arange(-30, 31)
    rpow = np.array([np.mean(rip[pk[:, None] + w, c] ** 2) for c in range(x.shape[1])])
    post, pre = np.arange(0, 63), np.arange(-125, -62)
    swa = np.array([np.mean(x[pk[:, None] + post, c]) - np.mean(x[pk[:, None] + pre, c])
                    for c in range(x.shape[1])])
    el = f["general/extracellular_ephys/electrodes"]
    bad = el["bad_channel"][:] if "bad_channel" in el else np.zeros(x.shape[1], bool)
    shank = electrode_columns(f)
    _, y = electrode_xy(f)
    rp = np.where(bad, -np.inf, rpow)
    pyr_ch = int(np.argmax(rp))

    def above_positive(s):
        k = np.where((shank == s) & ~bad)[0]
        if not len(k):
            return None, None
        centre = k[np.argmax(rpow[k])]
        c = k[(y[k] > y[centre]) & (swa[k] > 0)]
        return (int(c[np.argmax(rpow[c])]) if len(c) else None), int(centre)

    th, centre = above_positive(shank[pyr_ch])
    where = "same shank"
    if th is None:
        best = None
        for s in np.unique(shank):
            if s == shank[pyr_ch]:
                continue
            c, cen = above_positive(s)
            if c is not None and (best is None or rpow[c] > rpow[best[0]]):
                best = (c, cen)
        if best is not None:
            th, centre = best
            where = "other shank"
    if th is None:
        k = np.where((shank == shank[pyr_ch]) & ~bad & (y > y[pyr_ch]))[0]
        th = int(k[np.argmin(y[k])]) if len(k) else pyr_ch
        centre = pyr_ch
        where = "none positive, next channel with larger rel_y"
    # SPW reversal per shank (ed3): between the two neighbouring good channels with the steepest
    # fall from a positive (upper) to a negative (lower) sharp wave, interpolated to zero; NaN
    # on a shank without such a pair. The ripple-power centre of each shank is kept too.
    rev, cen = {}, {}
    for s in np.unique(shank):
        k = np.where((shank == s) & ~bad)[0]
        if not len(k):
            continue
        k = k[np.argsort(-y[k])]
        cen[int(s)] = float(y[k[np.argmax(rpow[k])]])
        best, rv = 0.0, np.nan
        for u, d in zip(k[:-1], k[1:]):
            if swa[u] > 0 > swa[d] and swa[u] - swa[d] > best:
                best = swa[u] - swa[d]
                rv = y[u] + (y[d] - y[u]) * swa[u] / (swa[u] - swa[d])
        rev[int(s)] = float(rv)
    k = np.where((shank == shank[pyr_ch]) & ~bad)[0]
    up, down = k[y[k] > y[pyr_ch]], k[y[k] < y[pyr_ch]]
    return th, pyr_ch, {"rev": rev, "cen": cen, "n_ripples": int(len(pk)), "all_ripples": bool(all_ripples),
                        "sw_theta": float(swa[th]),
                        "sw_pyr": float(swa[pyr_ch]), "where": where,
                        "dy_theta": float(y[th] - y[centre]),
                        "n_pos_above": int(np.sum(swa[up] > 0)), "n_pos_below": int(np.sum(swa[down] > 0)),
                        "sw_above_mean": float(swa[up].mean()) if len(up) else np.nan,
                        "sw_below_mean": float(swa[down].mean()) if len(down) else np.nan,
                        "sw_next_above": float(swa[up[np.argmin(y[up])]]) if len(up) else np.nan,
                        "sw_next_below": float(swa[down[np.argmax(y[down])]]) if len(down) else np.nan}


def read_channels(f, chans, block=2 ** 16 * 16):
    """Whole-session LFP of the given channel rows, in microvolts, one row per channel."""
    lfp = f["processing/ecephys/LFP/LFP/data"]
    conv = float(lfp.attrs.get("conversion", 1.0))
    u = sorted(set(int(c) for c in chans))
    out = np.empty((len(u), lfp.shape[0]), np.float32)
    for s in range(0, lfp.shape[0], block):
        out[:, s:s + block] = lfp[s:s + block, u].T
    out *= conv * 1e6
    return [out[u.index(int(c))] for c in chans]


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


def _theta_measures(x, m, trains, lr, novel, ref, fs=1250.0):
    """Theta measures from one LFP channel x (see theta_session); ref names the channel."""
    amp, ph = theta_phase_amp(x)
    hc = homecage_intervals(m)
    wake = intersect(state_intervals(m, "Awake"), hc)
    rem = intersect(state_intervals(m, "REM"), hc)
    wake_hi = intersect(wake, _mask_intervals(amp > amp.mean(), fs))
    pyr = m["_pyr"]
    cells = []
    for k in np.where(lr)[0]:
        t = trains[k]
        row = {"session": m["session_id"], "subject": m["subject_id"],
               "birthdate": m["birthdate"], "unit": int(pyr[k]), "ref": ref}
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
    del amp, ph
    W = state_intervals(m, "Awake")
    cw = cyc[in_intervals(cyc[:, 0], intersect(W, hc)) & in_intervals(cyc[:, 1], intersect(W, hc))]
    out = {"n_cycles": len(cyc), "wake_s": float(np.sum(np.diff(wake, axis=1))),
           "n_cycles_hc_wake": len(cw)}
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
    pairs = [{"session": m["session_id"], "subject": m["subject_id"], "ref": ref,
              "birthdate": m["birthdate"], "sbd": n < len(sbd), "a": int(pyr[a]),
              "b": int(pyr[b]), "theta_corr": tc[n]} for n, (a, b) in enumerate(sbd + dbd)]
    with np.errstate(invalid="ignore", divide="ignore"):
        cmat = (np.corrcoef(counts.T.astype(float)) if len(pyr) > 1
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
                    rates.append({"session": m["session_id"], "unit": int(pyr[j]), "ref": ref,
                                  "lr": bool(lr[j]), "epoch": n_ep, "env": env,
                                  "wake_only": restrict, "n_cycles": len(c), "dur": dur,
                                  "spikes": int(np.sum(kk % 2 == 1)),
                                  "rate": np.sum(kk % 2 == 1) / dur if dur > 0 else np.nan})
    return cells, pairs, out, rates, cmat


def theta_session(asset, m, novel=False):
    """Theta measures of one session, on two channels: the theta channel of pick_theta_channel
    (ref 'rule', the Methods' reading) and the pyramidal layer centre (ref 'centre', a variant
    showing how much the phase reference matters). Homecage wake and REM (homecage_intervals
    with the lab's sleep states): for each light-responsive pyramidal cell the Rayleigh p,
    preferred phase and mean resultant length in wake (amplitude above its mean) and in REM
    (all); per SBD and DBD pair the theta-cycle cofiring (Methods, Cofiring analysis; cycles
    with both edges in homecage WAKE, get_corrHome_v2.m). For a novel session also the
    theta-related rate of every pyramidal cell in each behavioural subsession, with and without
    the wake restriction. The correlation matrix kept is the rule channel's."""
    with open_nwb(asset) as f:
        th, pch, det = pick_theta_channel(f, m)
        xs = read_channels(f, [th, pch])
        ct = np.array(m["u_putative_cell_type"], dtype=object)
        pyr = np.where(ct == "Pyramidal Cell")[0]
        trains = spike_trains(f, pyr)
    lr = np.array(m["u_light_responsive"], bool)[pyr]
    m = dict(m, _pyr=pyr)
    cells, pairs, rates = [], [], []
    out = {"session": m["session_id"], "theta_ch": th, "pyr_ch": pch, **det}
    for ref, x in (("rule", xs[0]), ("centre", xs[1])):
        c, p, o, r, cmat = _theta_measures(x, m, trains, lr, novel, ref)
        cells += c
        pairs += p
        rates += r
        out.update({k + ("" if ref == "rule" else "_centre"): v for k, v in o.items()})
        if ref == "rule":
            out["theta_corr_mat"] = cmat
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


# Variants of the connection test (assumptions; see mono_flags). The first is the main reading.
MONO_VARIANTS = {
    "main": {},
    "peak3": {"window": "peak"},
    "hollow0.4": {"hollow": 0.4},
    "hollow0.8": {"hollow": 0.8},
    "sd7ms": {"sd_s": 0.007},
    "sd10ms": {"sd_s": 0.010},
    "no_minimums": {"min_counts": 0, "min_pre": 0},
    "alpha1e-5": {"alpha": 1e-5},
}


def mono_flags(C, n_pre, window="fixed", hollow=0.6, sd_s=0.015, alpha=0.001, min_counts=50,
               min_pre=100):
    """Connection test on many CCGs at once (rows of C, 0.8 ms bins, lags -50..50 ms).
    window 'fixed': the bins at 0.8, 1.6 and 2.4 ms lag, the 0.8-2.8 ms window of the Methods'
    transmission measure (assumption). window 'peak': the Methods' reliability test read
    literally, 'spike counts in 3 bins surrounding [the bin] of peak' firing, with the peak taken
    in the 0.8-2.8 ms window and its two neighbours tested. In both, a bin must exceed the
    hollowed-Gaussian baseline (Poisson upper tail) and the peak bin must exceed the largest of
    the three bins before zero lag (Poisson), each at alpha Bonferroni corrected over 3 bins.
    min_counts (CCG counts in +-50 ms) and min_pre (presynaptic spikes) are minimums assumed
    here to skip pairs with too few spikes for any test."""
    from scipy.ndimage import convolve1d
    from scipy.stats import poisson
    C = np.asarray(C, float)
    nb = (C.shape[1] - 1) // 2
    base = convolve1d(C, hollow_gauss(sd_s / MONO_BIN, hollow), axis=1, mode="mirror")
    win = nb + np.arange(1, 4)
    pk = win[np.argmax(C[:, win], axis=1)]
    rows = np.arange(len(C))
    test = win[None, :] if window == "fixed" else pk[:, None] + np.arange(-1, 2)[None, :]
    test = np.broadcast_to(test, (len(C), 3))
    cb = C[rows[:, None], test]
    p_base = poisson.sf(cb - 1, np.maximum(base[rows[:, None], test], 1e-9)).min(1)
    mirror = nb - np.arange(1, 4)
    p_ant = poisson.sf(C[rows, pk] - 1, np.maximum(C[:, mirror].max(1), 1e-9))
    ok = (C.sum(1) >= max(min_counts, 1)) & (np.asarray(n_pre) >= max(min_pre, 1))
    return ok & (p_base < alpha / 3) & (p_ant < alpha / 3)


def mono_session(asset, m):
    """Pyramidal-to-interneuron connections of one session, from spikes outside the light pulse
    periods, under each of MONO_VARIANTS; per pair detected under any variant the transmission
    probability for presynaptic spikes with preceding ISI of 10 to 40 ms (claims, fig7ce) and
    per ISI bin (fig7d)."""
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
    nbins = 2 * int(round(MONO_LAG / MONO_BIN)) + 1
    C = np.zeros((len(pyr) * len(inn), nbins), np.int32)
    npre = np.zeros(len(pyr) * len(inn), np.int64)
    for p_, i in enumerate(pyr):
        for q, j in enumerate(inn):
            if len(tr[i]):
                C[p_ * len(inn) + q] = ccg_lags(tr[i], tr[j])[0]
            npre[p_ * len(inn) + q] = len(tr[i])
    flags = {k: mono_flags(C, npre, **v).reshape(len(pyr), len(inn))
             for k, v in MONO_VARIANTS.items()}
    anyf = np.any([v for v in flags.values()], axis=0)
    rows = []
    for p_, q in zip(*np.where(anyf)):
        i, j = pyr[p_], inn[q]
        a = tr[i]
        isi = np.r_[np.inf, np.diff(a)]
        sel = (isi >= 0.010) & (isi <= 0.040)
        rows.append({"session": m["session_id"], "subject": m["subject_id"],
                     "birthdate": m["birthdate"], "pre": int(i), "post": int(j),
                     "pre_lr": bool(lr[i]), "stp": transmission(a[sel], tr[j]),
                     "stp_isi": [transmission(a[(isi >= lo) & (isi < hi)], tr[j])
                                 for lo, hi in zip(ISI_EDGES[:-1], ISI_EDGES[1:])],
                     **{"v_" + k: bool(v[p_, q]) for k, v in flags.items()}})
    tested = (C.sum(1) >= 50) & (npre >= 100)
    return {"session": m["session_id"], "subject": m["subject_id"],
            "birthdate": m["birthdate"], "pyr": pyr, "inn": inn, "lr": lr[pyr],
            "conn": flags["main"], "flags": flags, "rows": rows, "n_tested": int(tested.sum())}


def convergence(conn, a, b):
    """Shared postsynaptic interneurons over the union of targets (Methods); NaN with none."""
    u = np.sum(conn[a] | conn[b])
    return np.sum(conn[a] & conn[b]) / u if u > 0 else np.nan


def open_field_maps(f, name, t0, t1, trains, cm_per_unit=1.0, smin=SPEED_MIN, fwhm_cm=4.5):
    """Two-dimensional rate maps of an open field (Methods, Spatial ratemap analyses): 1 cm x
    1 cm bins, samples with speed > 1.5 cm/s (speed from constant-velocity Kalman filters of x
    and y), spikes and time per bin smoothed with a 4.5 cm FWHM Gaussian, rate = smoothed spikes
    / smoothed time, never-visited bins NaN. The files give open-field positions in the lab's
    units without a scale; cm_per_unit is that scale, assumed 1 (see novel_session), with other
    values as variants. Returns maps (ncells, nbins) over the flattened grid and the raw
    occupancy (nbins,) in s."""
    from scipy.ndimage import gaussian_filter
    g = f["processing/behavior/" + name]
    xy = g["data"][:].astype(float) * cm_per_unit
    ts = g["timestamps"][:]
    k = np.where((ts >= t0) & (ts <= t1) & np.all(np.isfinite(xy), 1))[0]
    ts, xy = ts[k], xy[k]
    dt = float(np.median(np.diff(ts)))
    sp = np.hypot(kalman_speed(ts, xy[:, 0]), kalman_speed(ts, xy[:, 1]))
    run = sp > smin
    nx, ny = int(np.ceil(xy[:, 0].max())) + 1, int(np.ceil(xy[:, 1].max())) + 1
    bx = np.clip(np.floor(xy[:, 0]).astype(int), 0, nx - 1)
    by = np.clip(np.floor(xy[:, 1]).astype(int), 0, ny - 1)
    lin = bx * ny + by
    occ = np.bincount(lin[run], minlength=nx * ny) * dt
    sig = fwhm_cm / 2.3548
    so = gaussian_filter(occ.reshape(nx, ny), sig, mode="constant")
    maps = np.full((len(trains), nx * ny), np.nan)
    for c, t in enumerate(trains):
        t = t[(t >= ts[0]) & (t <= ts[-1])]
        j = np.clip(np.searchsorted(ts, t), 0, len(ts) - 1)
        ok = run[j]
        s = np.bincount(lin[j[ok]], minlength=nx * ny).reshape(nx, ny).astype(float)
        with np.errstate(invalid="ignore", divide="ignore"):
            r = (gaussian_filter(s, sig, mode="constant") / so).ravel()
        r[occ == 0] = np.nan
        maps[c] = r
    return maps, occ, dt


# cm per lab unit: the assumption (1) and variants; 0.85 is the scale that the simultaneous
# speeds give for the lab-unit series of two linear tracks (position_scale_check)
OPEN_SCALES = (1.0, 2.0, 0.5, 0.85)


def position_scale_check(asset, m, w=30):
    """Evidence on the scale of the 2D positions (SubjectPosition series) of one session's
    behavioural subsessions. Per series: its unit, extent and the 90th percentile of speed over
    1 s (w samples at 30 Hz) in its own units. Where a linearized series (cm) covers the same
    samples, the ratio of the two speeds at the same times estimates cm per 2D unit (the
    linearized path follows the 2D path, so on the familiar figure-eight, whose 2D series is in
    cm, the ratio shows what to expect)."""
    rows = []
    with open_nwb(asset) as f:
        for n, (t0, t1, env, name) in enumerate(behaviour_epochs(m)):
            sers = {k: v for k, v in m["series"].items() if v["t0"] >= t0 - 1 and v["t1"] <= t1 + 1}
            two = [k for k in sers if k.startswith("SubjectPosition/") and k.endswith("_" + env)]
            lin = [k for k in sers if k.startswith("LinearizedPosition/") and k.endswith("_" + env)]
            for k in two:
                g = f["processing/behavior/" + k]
                xy, ts = g["data"][:].astype(float), g["timestamps"][:]
                ok = np.all(np.isfinite(xy), 1)
                xy2, ts2 = xy[ok], ts[ok]
                sp = np.linalg.norm(xy2[w:] - xy2[:-w], axis=1) / (ts2[w:] - ts2[:-w])
                row = {"session": m["session_id"], "epoch": n, "env": env, "series": k.split("/")[1],
                       "unit": sers[k]["unit"], "x_min": xy2[:, 0].min(), "x_max": xy2[:, 0].max(),
                       "y_min": xy2[:, 1].min(), "y_max": xy2[:, 1].max(),
                       "speed_p90": float(np.percentile(sp, 90)), "lin_cm": np.nan,
                       "cm_per_unit_from_speed": np.nan}
                if lin:
                    gl = f["processing/behavior/" + lin[0]]
                    xl, tl = gl["data"][:].astype(float), gl["timestamps"][:]
                    if xl.ndim > 1:
                        xl = xl[:, 0]
                    if len(tl) == len(ts) and np.allclose(tl, ts):
                        okb = ok & np.isfinite(xl)
                        a, b, tt = xy[okb], xl[okb], ts[okb]
                        s2 = np.linalg.norm(a[w:] - a[:-w], axis=1) / (tt[w:] - tt[:-w])
                        sl = np.abs(b[w:] - b[:-w]) / (tt[w:] - tt[:-w])
                        mv = sl > np.percentile(sl, 50)   # moving samples, where both paths are runs
                        row["lin_cm"] = float(np.nanmax(xl))
                        row["cm_per_unit_from_speed"] = float(np.median(sl[mv]) / np.median(s2[mv]))
                rows.append(row)
    return rows


def novel_session(asset, m):
    """Rate maps of all pyramidal cells in the familiar figure-eight (first subsession) and in
    each later subsession. Linear tracks and the novel figure-eight use their linearized
    position, which the files give in centimeters, in 1 cm bins (as many as the series' largest
    value). Open fields use the 2D head position, whose x and y are in the lab's units with no
    scale; they are binned assuming one unit is 1 cm (assumption: where the files give a
    lab-unit 2D series beside a linearized one in cm, the lab units that are not normalized to
    0-1 are close to cm, position_scale_check), and at the other OPEN_SCALES as variants
    (open_field_maps)."""
    ep = behaviour_epochs(m)
    ct = np.array(m["u_putative_cell_type"], dtype=object)
    pyr = np.where(ct == "Pyramidal Cell")[0]
    lr = np.array(m["u_light_responsive"], bool)
    out = []
    with open_nwb(asset) as f:
        tr = spike_trains(f, pyr)
        for n, (t0, t1, env, name) in enumerate(ep):
            if env.startswith("openField"):
                ser = [k for k, v in m["series"].items() if k.startswith("SubjectPosition/")
                       and k.endswith("_" + env) and v["t0"] >= t0 - 1 and v["t1"] <= t1 + 1]
                if not ser:
                    out.append({"epoch": n, "env": env, "maps": None, "why": "no position series "
                                "inside the epoch"})
                    continue
                sc = {}
                for s in OPEN_SCALES:
                    maps, occ, dt = open_field_maps(f, ser[0], t0, t1, tr, cm_per_unit=s)
                    sc[s] = (maps[None], occ[None])
                v = m["series"][ser[0]]
                out.append({"epoch": n, "env": env, "kind": "open", "maps": sc[1.0][0],
                            "occ": sc[1.0][1], "scales": sc, "series": ser[0], "unit": v["unit"],
                            "nbins": sc[1.0][1].shape[1], "trial_counts": None})
                continue
            ser = linear_series_for(m, t0, t1, env)
            if ser is None:
                out.append({"epoch": n, "env": env, "maps": None, "why": "no linearized series "
                            "inside the epoch"})
                continue
            g = f["processing/behavior/" + ser]
            xmax = float(np.nanmax(g["data"][:]))
            nbins = NBINS if n == 0 else int(np.ceil(xmax))
            maps, occ, info, dt = linear_maps(f, m, t0, t1, tr, nbins=nbins, env=env)
            out.append({"epoch": n, "env": env, "kind": "linear", "maps": maps, "occ": occ,
                        "nbins": nbins, "series": ser, "unit": m["series"][ser]["unit"],
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


# ---------- resampling controls (ed3, ed5, ed10) ----------

def kw_rows(X, sizes):
    """Kruskal-Wallis H for each row of X (rows are pooled samples, split into groups of the
    given sizes in order), with the tie correction, as scipy.stats.kruskal gives it."""
    from scipy.stats import rankdata
    X = np.atleast_2d(X)
    B, N = X.shape
    R = rankdata(X, axis=1)
    cuts = np.r_[0, np.cumsum(sizes)]
    with np.errstate(invalid="ignore", divide="ignore"):
        H = sum(R[:, a:b].sum(1) ** 2 / (b - a) for a, b in zip(cuts[:-1], cuts[1:]))
    H = 12.0 / (N * (N + 1)) * H - 3 * (N + 1)
    S = np.sort(X, axis=1)
    new = np.ones((B, N), bool)
    new[:, 1:] = S[:, 1:] != S[:, :-1]
    run = np.cumsum(new, axis=1) - 1 + (np.arange(B) * N)[:, None]
    t = np.bincount(run.ravel(), minlength=B * N).astype(float)
    tie = np.bincount(np.repeat(np.arange(B), N), weights=(t ** 3 - t), minlength=B)
    return H / (1 - tie / (N ** 3 - N))


def boot_kw_fast(groups, n_boot=5000, rng=None):
    """boot_kw computed for all resamplings at once (same null: the pooled values reassigned to
    groups of the same sizes with replacement)."""
    groups = [np.asarray(g, float)[np.isfinite(g)] for g in groups]
    sizes = [len(g) for g in groups]
    pool = np.concatenate(groups)
    h = float(kw_rows(pool[None], sizes)[0])
    null = kw_rows(pool[rng.integers(0, len(pool), (n_boot, len(pool)))], sizes)
    return h, float(np.mean(null >= h))


def depth_match_draw(depth, group, ref, rng, binw=20.0):
    """One depth-matched resampling (ed3; resample_depth.m draws with subsample1D, whose binning
    is not in the repository, so bins of 20 um, the electrode pitch, are a standard choice):
    per group, n cells drawn with replacement with probabilities that give the group the depth
    distribution of ref. Returns indices into depth."""
    lo = min(depth.min(), ref.min())
    edges = np.arange(lo - binw / 2, max(depth.max(), ref.max()) + binw, binw)
    rp = np.histogram(ref, edges)[0] / len(ref)
    out = []
    for g in np.unique(group):
        k = np.where(group == g)[0]
        b = np.clip(np.digitize(depth[k], edges) - 1, 0, len(rp) - 1)
        gp = np.bincount(b, minlength=len(rp)) / len(k)
        w = rp[b] / gp[b]
        out.append(rng.choice(k, size=len(k), replace=True, p=w / w.sum()))
    return np.concatenate(out)


def subsample2d(sbd, dbd, size, rng, nbins=100):
    """subsample2D_local.m (claims, ed5): each pair's two values log10 transformed (zeros set to
    -2), the DBD points binned in a 100 x 100 histogram, bins drawn with the SBD pairs'
    probabilities in those bins (bins without DBD pairs dropped) and one DBD pair drawn per bin.
    One-dimensional values (ed10, waveform distance) use a 100-bin histogram. Returns indices
    into dbd."""
    def lg(v):
        v = np.asarray(v, float)
        with np.errstate(divide="ignore"):
            return np.where(v > 0, np.log10(np.where(v > 0, v, 1)), -2.0)
    s, d = lg(sbd), lg(dbd)
    if s.ndim == 1:
        s, d = s[:, None], d[:, None]
    edges = [np.linspace(min(d[:, j].min(), s[:, j].min()), max(d[:, j].max(), s[:, j].max()) + 1e-9,
                         nbins + 1) for j in range(d.shape[1])]
    def code(v):
        c = np.zeros(len(v), int)
        for j in range(v.shape[1]):
            c = c * nbins + np.clip(np.digitize(v[:, j], edges[j]) - 1, 0, nbins - 1)
        return c
    cs, cd = code(s), code(d)
    order = np.argsort(cd)
    cd_sorted = cd[order]
    ub, start, cnt = np.unique(cd_sorted, return_index=True, return_counts=True)
    ps = np.bincount(cs, minlength=nbins ** d.shape[1])[ub].astype(float)
    if ps.sum() == 0:
        return np.array([], int)
    pick = rng.choice(len(ub), size=size, replace=True, p=ps / ps.sum())
    return order[start[pick] + rng.integers(0, cnt[pick])]
