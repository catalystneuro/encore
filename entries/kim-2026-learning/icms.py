"""Loading and measures for dandiset 001868 (Kim et al. 2026, ICMS learning).

Streams the NWB files of the pinned version from the DANDI archive with remfile and h5py; nothing is
written to disk. Where each parameter comes from is said beside it: the claims file (which cites the
paper's Methods or code), a passage of the paper (author, step 1.6), an assumption, or a standard
choice that cannot change a result.
"""
import re
from datetime import date

import h5py
import numpy as np
import pandas as pd
import remfile
import requests
from scipy import stats

DANDISET = "001868"
VERSION = "0.260715.2016"
API = "https://api.dandiarchive.org/api"

# The six behavioural mice, with the paper's numbering (claims file header: the code calls them
# ICMS83, 92, 93, 98, 100, 101, shown as Mouse 6, 1, 2, 3, 4, 5).
BEHAVIOUR_MICE = ["ICMS92", "ICMS93", "ICMS98", "ICMS100", "ICMS101", "ICMS83"]
MOUSE_NUMBER = {"ICMS92": 1, "ICMS93": 2, "ICMS98": 3, "ICMS100": 4, "ICMS101": 5, "ICMS83": 6}
CONTROL_MICE = ["ICMS43", "ICMS45", "ICMS48", "ICMS54", "ICMS56", "ICMS57"]
CURRENTS = (4.0, 5.0, 6.0)  # Methods, Analysis of behavioral data: only 4, 5 and 6 uA analysed.


def list_assets():
    """All assets of the pinned version, as a DataFrame with subject, session date and kinds."""
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/"
    out, params = [], {"page_size": 200}
    while url:
        r = requests.get(url, params=params, timeout=60).json()
        out += r["results"]
        url, params = r.get("next"), None
    rows = []
    for a in out:
        m = re.match(r"sub-(\w+)/sub-\w+_ses-(\d{4}-\d{2}-\d{2})_(.+)\.nwb", a["path"])
        rows.append(dict(path=a["path"], asset_id=a["asset_id"], size=a["size"], subject=m.group(1),
                         session=m.group(2), kinds=m.group(3)))
    return pd.DataFrame(rows).sort_values(["subject", "session"]).reset_index(drop=True)


def open_nwb(asset_id):
    """Open one asset by streaming (remfile over the S3 URL), as an h5py File."""
    url = requests.head(f"{API}/assets/{asset_id}/download/", allow_redirects=True, timeout=60).url
    return h5py.File(remfile.File(url), "r")


def _table(g):
    cols = {}
    for k in g.keys():
        o = g[k]
        if (isinstance(o, h5py.Dataset) and o.ndim == 1 and k != "id"
                and o.attrs.get("neurodata_type") != "VectorIndex"):
            v = o[:]
            if v.dtype == object:
                v = np.array([x.decode() if isinstance(x, bytes) else x for x in v])
            cols[k] = v
    return pd.DataFrame(cols)


def week_of(session, first):
    """Week of a session: ceil(days since the mouse's first session / 7), so week 0 is the first
    day only (claims file header, 'Week', from the paper's code)."""
    days = (date.fromisoformat(session) - date.fromisoformat(first)).days
    return int(np.ceil(days / 7))


def phase_of(week):
    """Early is weeks 0 and 1, late weeks 2 to 4, later weeks dropped (claims file header)."""
    return "early" if week <= 1 else ("late" if week <= 4 else None)


def load_session(asset_id, wheel=False):
    """Read what the ephys and behaviour analyses use from one session file.

    Returns a dict with the trials table, the stimulation table (one row per train or burst), the
    units table (cell type, peak channel, depth, trough-to-peak from the mean waveform) and a list of
    spike-time arrays, the electrode depths by Ripple channel, and optionally the processed wheel.
    """
    f = open_nwb(asset_id)
    s = dict(subject=f["general/subject/subject_id"][()].decode(),
             session=f["general/session_id"][()].decode())
    s["trials"] = _table(f["intervals/trials"]) if "intervals/trials" in f else None
    s["stim"] = (_table(f["intervals/electrical_stimulation"])
                 if "intervals/electrical_stimulation" in f else None)
    e = f["general/extracellular_ephys/electrodes"] if "general/extracellular_ephys/electrodes" in f else None
    if e is not None:
        ch = np.array([int(x) for x in e["channel_name"][:].astype(str)])
        s["electrode_depth"] = dict(zip(ch, e["rel_y"][:]))
    if "units" in f:
        u = f["units"]
        st = u["spike_times"][:]
        idx = u["spike_times_index"][:]
        s["spikes"] = np.split(st, idx[:-1])
        n = len(idx)
        col = lambda k, d: u[k][:] if k in u else np.full(n, d)
        ut = pd.DataFrame(dict(unit_id=u["id"][:], cell_type=col("cell_type", b"").astype(str),
                               peak_channel_index=col("peak_channel_index", -1),
                               y_um=col("unit_y_um", np.nan)))
        wf = u["waveform_mean"][:]
        s["waveforms"] = wf
        ut["t2p_ms"] = [trough_to_peak_ms(w) for w in wf]
        if e is not None and (ut.peak_channel_index >= 0).all():
            ut["peak_channel"] = ch[ut["peak_channel_index"].to_numpy()]
        s["units"] = ut
    else:
        s["spikes"], s["units"] = [], None
    if wheel and "processing/behavior/wheel/wheel_position_processed" in f:
        w = f["processing/behavior/wheel/wheel_position_processed"]
        s["wheel"] = w["data"][:]
        s["wheel_rate"] = float(w["starting_time"].attrs["rate"])
        s["wheel_t0"] = float(w["starting_time"][()])
    f.close()
    return s


def trough_to_peak_ms(w, fs=30000.0):
    """Trough-to-peak interval of a mean waveform: time from the minimum to the following maximum."""
    w = np.asarray(w, float)
    i = int(np.argmin(w))
    if i >= len(w) - 1:
        return np.nan
    j = i + int(np.argmax(w[i:]))
    return (j - i) / fs * 1000.0


# ---------------------------------------------------------------------------------------------
# Responses: one unit at one stimulation channel and current in one session (Methods,
# Quantifying neuromodulation metrics).

TRAIN_S = 0.7      # 700 ms train of 70 pulses at 100 Hz (Methods, Behavioral task; file metadata).
PRE_S = 0.7        # Pre-stimulus window as long as the train, before onset. Assumption: the Methods
                   # (Quantifying neuromodulation metrics) say "pre-stimulus" without a length. The
                   # Results define the delta spikes of Figure 6 with "pre-stimulation spikes in the
                   # preceding 700-ms window", and 700 ms lies within the 1 to 1.5 s pre-stimulus
                   # period in which the mouse must hold still (Methods, Behavioral task). The
                   # notebook shows 300 and 500 ms as variants.
IPI_S = 0.010      # 10 ms interpulse interval (Methods).
BIN_S = 0.0005     # 0.5 ms bins (Methods).
BLANK_START = 3    # first 1.5 ms blanked (Methods) = 3 bins
BLANK_END = 1      # last 0.5 ms blanked (Methods) = 1 bin
N_BOOT = 500       # bootstrap draws of 20% of pulses (claims file header, from the code)
BOOT_FRAC = 0.2
N_NULL = 100       # null sets of uniformly drawn spike times (claims file header, from the code)


def stim_events(s):
    """Stimulation trains of the ephys blocks, joined to the trial outcome. Planar-block trials are
    left out: "A fifth block was presented for planar imaging; this block was not used for
    electrophysiological analysis" (Methods, Behavioral task)."""
    st = s["stim"].copy()
    tr = s["trials"]
    cols = [c for c in ["trial_index", "is_hit", "response_time", "imaging_modality"] if c in tr]
    st = st.drop(columns=[c for c in cols if c != "trial_index" and c in st]).merge(
        tr[cols], on="trial_index", how="left")
    if "imaging_modality" in st:
        st = st[st.imaging_modality != "planar"]
    return st.sort_values("start_time").reset_index(drop=True)


def window_counts(spk, starts, a, b):
    """Spike counts of one sorted spike train in [start + a, start + b) for each start."""
    return np.searchsorted(spk, starts + b) - np.searchsorted(spk, starts + a)


def relative_spikes(spk, starts, a, b):
    """Spike times relative to each start within [a, b), with the trial number of each."""
    lo = np.searchsorted(spk, starts + a)
    hi = np.searchsorted(spk, starts + b)
    trial = np.repeat(np.arange(len(starts)), hi - lo)
    idx = np.concatenate([np.arange(l, h) for l, h in zip(lo, hi)]) if len(starts) else np.array([], int)
    return spk[idx.astype(int)] - starts[trial], trial


def time_to_max(rel, n_trials, t_end=TRAIN_S, bin_s=0.010, sigma_s=0.020):
    """Time to maximum firing rate: PSTH of the stimulation window in 10 ms bins smoothed with a
    Gaussian of sigma 20 ms (claims file header, from the code); time of the bin centre."""
    from scipy.ndimage import gaussian_filter1d
    edges = np.arange(0, t_end + 1e-9, bin_s)
    h = np.histogram(rel, edges)[0] / n_trials / bin_s
    hs = gaussian_filter1d(h.astype(float), sigma_s / bin_s, mode="nearest")
    return (np.argmax(hs) + 0.5) * bin_s * 1000.0  # ms


def pulse_histogram(rel, trial, n_trials, n_pulses=70, ipi=IPI_S):
    """Per-pulse histogram (n_trials * n_pulses, 20 bins of 0.5 ms) of spikes after each pulse."""
    k = np.floor(rel / ipi).astype(int)
    ok = (k >= 0) & (k < n_pulses)
    b = np.floor((rel[ok] - k[ok] * ipi) / BIN_S).astype(int)
    nb = int(round(ipi / BIN_S))
    b = np.clip(b, 0, nb - 1)
    g = trial[ok] * n_pulses + k[ok]
    H = np.zeros((n_trials * n_pulses, nb))
    np.add.at(H, (g, b), 1)
    return H


def pli(curve):
    """Pulse-locked index of a spike-probability curve over the valid bins: mean of the 3 bins
    around the peak minus the median of the valid bins (claims file header, from the code)."""
    curve = np.atleast_2d(curve)
    p = np.argmax(curve, axis=1)
    n = curve.shape[1]
    lo = np.clip(p - 1, 0, n - 3)
    idx = lo[:, None] + np.arange(3)[None, :]
    top = np.take_along_axis(curve, idx, axis=1).mean(1)
    return top - np.median(curve, axis=1)


def pulse_locking(H, n_trials, rng, n_pulses=70):
    """Pulse-locking of one response from its per-pulse histogram H.

    The curve is the mean of N_BOOT bootstrap draws of 20% of pulses with replacement, in spikes per
    bin per trial (Methods: "the number of spikes per bin normalized by the number of trials"); a
    draw of m pulses is scaled by n_pulses / m so that it is per trial. Only bins 1.5 to 9.5 ms are
    valid. The null is N_NULL sets of the same number of spikes drawn uniformly over the valid bins
    (claims file header, the code's reading of "shuffled"). Returns (is_pl, pli, null99,
    peak spike probability, peak time in ms).
    """
    V = H[:, BLANK_START:H.shape[1] - BLANK_END]
    n_all = V.shape[0]
    m = max(1, int(round(BOOT_FRAC * n_all)))
    idx = rng.integers(0, n_all, size=(N_BOOT, m))
    # The mean of the N_BOOT draw curves, each V[idx[b]].sum(0) * n_pulses / m, computed at once from
    # how often each pulse was drawn (the same draws, the same value).
    curve = np.bincount(idx.ravel(), minlength=n_all) @ V * (n_pulses / m) / N_BOOT
    obs = float(pli(curve)[0])
    n_sp = int(V.sum())
    nb = V.shape[1]
    null = rng.multinomial(n_sp, np.full(nb, 1.0 / nb), size=N_NULL) / n_trials
    thr = float(np.percentile(pli(null), 99))
    pk = int(np.argmax(curve))
    return obs > thr, obs, thr, float(curve.max()), (BLANK_START + pk + 0.5) * BIN_S * 1000.0


def latency_jitter(H):
    """Spike latency and jitter of a pulse-locked response, two readings (claims file,
    figs4b-conduction-velocity): (a) mean and variance of the first valid spike after each pulse,
    over pulses with one; (b) the peak time of the spike-probability curve and the variance of the
    valid spike times about it. Times in ms from the pulse."""
    V = H[:, BLANK_START:H.shape[1] - BLANK_END]
    t = (BLANK_START + np.arange(V.shape[1]) + 0.5) * BIN_S * 1000.0
    has = V.sum(1) > 0
    first = t[np.argmax(V[has] > 0, axis=1)] if has.any() else np.array([np.nan])
    w = V.sum(0)
    pk = t[np.argmax(w)]
    var_b = float((w * (t - pk) ** 2).sum() / w.sum()) if w.sum() else np.nan
    return float(np.mean(first)), float(np.var(first)), float(pk), var_b


def session_responses(s, rng, currents=CURRENTS, starts_col="start_time", stim_s=TRAIN_S, pre_s=PRE_S,
                      n_pulses=70, keep_spikes=False, ttm_bin=0.010, ttm_sigma=0.020, trial_counts=False,
                      pulse=True):
    """All responses of one session at the given currents, with the modulation test and measures.

    Modulated (Methods): paired t-test of spike counts in the stimulation against the pre-stimulus
    window across trials gives a significant increase, p < 0.05 two-sided with the stimulation count
    higher (column p_two); the one-sided p is kept as a variant (p_one). At least 50 spikes in the
    stimulation window summed over trials and a baseline rate of at least 0.5 Hz (Methods).
    With trial_counts, the per-trial stimulation and pre-stimulus counts and hit labels of each
    modulated response are kept (for the delta spikes of Figure 6B, C). With pulse=False the
    pulse-locking, latency and jitter are not computed and no random numbers are drawn.
    """
    ev = stim_events(s)
    rows, keep = [], {}
    for (ch, cur), g in ev.groupby(["stim_channel", "current_uA"]):
        if cur not in currents:
            continue
        starts = g[starts_col].to_numpy()
        nt = len(starts)
        for ui, spk in enumerate(s["spikes"]):
            c_stim = window_counts(spk, starts, 0.0, stim_s)
            c_pre = window_counts(spk, starts, -pre_s, 0.0)
            r_stim, r_pre = c_stim / stim_s, c_pre / pre_s
            sd = r_pre.std(ddof=1) if nt > 1 else np.nan
            z = (r_stim.mean() - r_pre.mean()) / sd if sd > 0 else np.inf
            if nt > 1 and np.any(c_stim != c_pre):
                t, p2 = stats.ttest_rel(c_stim, c_pre)
                p1 = p2 / 2 if t > 0 else 1 - p2 / 2
            else:
                t, p2, p1 = 0.0, 1.0, 1.0
            mod = (p2 < 0.05) and (t > 0) and c_stim.sum() >= 50 and r_pre.mean() >= 0.5
            mod1 = (p1 < 0.05) and c_stim.sum() >= 50 and r_pre.mean() >= 0.5
            row = dict(subject=s["subject"], session=s["session"], unit=ui, stim_channel=int(ch),
                       current=float(cur), n_trials=nt, n_spikes=int(c_stim.sum()),
                       base_rate=r_pre.mean(), stim_rate=r_stim.mean(), z=z, p_two=p2, p_one=p1,
                       modulated=bool(mod), modulated_one=bool(mod1))
            if mod or mod1:
                rel, tr = relative_spikes(spk, starts, 0.0, stim_s)
                row["ttm_ms"] = time_to_max(rel, nt, stim_s, ttm_bin, ttm_sigma)
                if pulse:
                    H = pulse_histogram(rel, tr, nt, n_pulses)
                    pl, obs, thr, pk, pkt = pulse_locking(H, nt, rng, n_pulses)
                    la, ja, lb, jb = latency_jitter(H)
                    row.update(pl=bool(pl), pli=obs, pli_null99=thr, peak_prob=pk, peak_ms=pkt,
                               lat_a=la, jit_a=ja, lat_b=lb, jit_b=jb)
                if keep_spikes:
                    keep[(int(ch), float(cur), ui)] = (rel, tr)
                if trial_counts:
                    row["c_stim"], row["c_pre"] = c_stim, c_pre
                    row["hit"] = g.is_hit.to_numpy().astype(bool) if "is_hit" in g else None
            rows.append(row)
    out = pd.DataFrame(rows)
    return (out, keep) if keep_spikes else out


# ---------------------------------------------------------------------------------------------
# Behaviour

def behaviour_blocks(s):
    """Ephys-block trials of a behavioural session with a block number.

    The Methods give four blocks of 100 trials (Behavioral task); trial_index counts trials from 1
    within the session, so block = (trial_index - 1) // 100 for the 400 ephys-block trials. ICMS83's
    files have no catch trials and other trial counts (180 to 480, trial_index up to 625), so their
    blocks cannot be read from the files; their whole session is one block (a deviation).
    """
    tr = s["trials"].copy()
    if "imaging_modality" in tr:
        tr = tr[tr.imaging_modality != "planar"]
    if (tr.current_uA == 0).any():
        tr["block"] = (tr.trial_index - 1) // 100
    else:
        tr["block"] = 0
    return tr


def fit_threshold(x, k, n, fa, reading):
    """50% detection threshold of a cumulative Gaussian fitted with psignifit 4 (Methods, Analysis
    of behavioral data). Reading (a): guess rate fixed at the block's catch-trial false-alarm rate,
    threshold where the fitted curve gives 50% hits. Reading (b): hit proportions corrected for false
    alarms, (p - fa) / (1 - fa), then a fit with guess rate 0 (claims file, fig2a-threshold-decrease).
    The lapse rate keeps psignifit's default prior. Returns (threshold, parameter): the 50% point of
    the fitted curve, and psignifit's own threshold parameter, the midpoint of the sigmoid before the
    guess and lapse rates are applied (a variant); NaN when the fit fails."""
    import psignifit as ps
    x = np.asarray(x, float); k = np.asarray(k, float); n = np.asarray(n, float)
    if reading == "b":
        p = np.clip((k / n - fa) / (1 - fa), 0, 1) if fa < 1 else k / n
        k = np.round(p * n)
        gamma = 0.0
    else:
        gamma = float(fa)
    data = np.column_stack([x, k, n])
    import warnings
    warnings.filterwarnings("ignore")
    try:
        r = ps.psignifit(data, sigmoid="norm", experiment_type="yes/no",
                         fixed_parameters={"gamma": min(gamma, 0.99)}, verbose=False)
        return (float(r.threshold([0.5], return_ci=False)[0]),
                float(r.threshold([0.5], unscaled=True, return_ci=False)[0]))
    except Exception:
        return np.nan, np.nan


def _fit_job(job):
    return job[:-1], fit_threshold(*job[-1])


def session_thresholds(sessions, processes=4):
    """Block thresholds of every channel, both readings, and the session threshold as the mean of
    the block thresholds (Methods). Runs the fits in a process pool."""
    from multiprocessing import Pool
    jobs = []
    for s in sessions:
        tr = behaviour_blocks(s)
        for b, g in tr.groupby("block"):
            catch = g[g.current_uA == 0]
            fa = catch.is_hit.mean() if len(catch) else 0.0
            for ch, gc in g[g.current_uA > 0].groupby("stim_channel"):
                agg = gc.groupby("current_uA").is_hit.agg(["sum", "count"])
                if len(agg) < 2:
                    continue
                for rd in "ab":
                    jobs.append((s["subject"], s["session"], int(ch), int(b), rd, float(fa),
                                 (agg.index.to_numpy(), agg["sum"].to_numpy(), agg["count"].to_numpy(),
                                  fa, rd)))
    with Pool(processes) as p:
        res = p.map(_fit_job, jobs, chunksize=4)
    out = pd.DataFrame([dict(subject=a[0], session=a[1], stim_channel=a[2], block=a[3], reading=a[4],
                             fa=a[5], threshold=t[0], threshold_param=t[1]) for a, t in res])
    return out


def movement_onsets(s, scale=1.0):
    """Wheel-movement onset of each hit trial of the ephys blocks, in ms from stimulation onset.

    Onset is the first time after onset that the absolute wheel deviation from its value at onset
    exceeds half the angular response threshold and stays above it for 50 ms (claims file,
    figs5-movement-onset, from the code). The threshold is not in the files or the paper; it is
    estimated per session as the median deviation at the recorded response time of hit trials (an
    assumption: the response time is when the wheel crossed the threshold, Methods, Behavioral task).
    scale multiplies the estimated threshold, to show how the onsets depend on it.
    """
    w, fs, t0 = s["wheel"], s["wheel_rate"], s["wheel_t0"]
    ev = stim_events(s)
    h = ev[(ev.is_hit == True) & np.isfinite(ev.response_time)]
    i0 = np.round((h.start_time.to_numpy() - t0) * fs).astype(int)
    ir = np.round((h.start_time.to_numpy() + h.response_time.to_numpy() - t0) * fs).astype(int)
    ok = ir < len(w)
    thr = scale * float(np.median(np.abs(w[ir[ok]] - w[i0[ok]]))) if ok.any() else np.nan
    hold = int(round(0.050 * fs))
    out = []
    for a, cur, ch, rt in zip(i0, h.current_uA, h.stim_channel, h.response_time):
        if a + int(0.7 * fs) + hold > len(w):  # trial after the end of the stored wheel trace
            out.append(dict(current=cur, stim_channel=ch, onset_ms=np.nan, rt_ms=rt * 1000.0,
                            threshold=thr, beyond_wheel=True))
            continue
        seg = np.abs(w[a:a + int(0.7 * fs) + hold] - w[a]) > thr / 2
        on = np.nan
        if seg.any():
            run = np.convolve(seg.astype(int), np.ones(hold, int), "valid") == hold
            if run.any():
                on = np.argmax(run) / fs * 1000.0
        out.append(dict(current=cur, stim_channel=ch, onset_ms=on, rt_ms=rt * 1000.0, threshold=thr,
                        beyond_wheel=False))
    return pd.DataFrame(out)


def population_coupling(unit_trains, n_bins, rng, pop_units=None, n_shuffle=200, sigma_ms=10):
    """Normalised population coupling of each unit (Methods, Population coupling).

    unit_trains: dict key -> sorted bin indices (1 ms bins) of the unit's spikes in the concatenated
    stimulation periods of one condition. The population trace sums the other units (or only those
    in pop_units), smoothed with a Gaussian of sigma 10 ms and mean-centred; PC is the trace at zero
    lag averaged over the unit's spikes, divided by the median absolute PC over 200 circular shifts
    of the trace. Units with fewer than 50 spikes are left out (Methods).
    """
    from scipy.ndimage import gaussian_filter1d
    keys = list(unit_trains)
    B = np.zeros((len(keys), n_bins))
    for i, k in enumerate(keys):
        np.add.at(B[i], unit_trains[k], 1)
    pool = np.array([pop_units is None or k in pop_units for k in keys])
    out = {}
    for i, k in enumerate(keys):
        sp = unit_trains[k]
        if len(sp) < 50:
            continue
        others = pool.copy(); others[i] = False
        if not others.any():
            continue
        pop = gaussian_filter1d(B[others].sum(0), sigma_ms, mode="wrap")
        pop = pop - pop.mean()
        pc = pop[sp].mean()
        sh = rng.integers(1, n_bins, size=n_shuffle)
        null = np.array([pop[(sp + d) % n_bins].mean() for d in sh])
        out[k] = pc / np.median(np.abs(null))
    return out


def kl_bootstrap(hit, miss, rng, n_boot=1000, prop=0.4, wins=0.01, bins=25, rng_lim=(-30, 50)):
    """Bootstrap KL(hit || miss) of delta-spike distributions (claims file, fig6c-kl-divergence,
    from the code): winsorise both at wins and 1 - wins of the pooled values, draw n_boot resamples of
    hit and of miss trials of size prop times the smaller count, 25-bin histograms over -30 to 50,
    natural log. Empty bins get 1e-10 (a standard choice that cannot change the direction)."""
    allv = np.r_[hit, miss]
    lo, hi = np.quantile(allv, [wins, 1 - wins])
    hit = np.clip(hit, lo, hi); miss = np.clip(miss, lo, hi)
    m = max(1, int(prop * min(len(hit), len(miss))))
    edges = np.linspace(rng_lim[0], rng_lim[1], bins + 1)
    out = np.empty(n_boot)
    for b in range(n_boot):
        ph = np.histogram(rng.choice(hit, m), edges)[0] + 1e-10
        pm = np.histogram(rng.choice(miss, m), edges)[0] + 1e-10
        ph = ph / ph.sum(); pm = pm / pm.sum()
        out[b] = np.sum(ph * np.log(ph / pm))
    return out


def cluster_test(hit, miss, rng, n_perm=1000, alpha=0.05):
    """Cluster-mass test of hit against miss traces across units (claims file,
    fig6d-npl-hit-miss-divergence, from the code): per bin a two-sided Mann-Whitney U test of hit
    against miss units, signed -log10 p; clusters are runs of bins over -log10 0.05, mass the sum;
    the null is the maximal mass after swapping each unit's hit and miss labels at random, n_perm
    times. Returns the clusters as (first bin, last bin, mass, p)."""
    def signed(h, m):
        u = stats.mannwhitneyu(h, m, axis=0, alternative="two-sided")
        sgn = np.sign(np.median(h, 0) - np.median(m, 0))
        return -np.log10(np.clip(u.pvalue, 1e-300, 1)) * sgn

    def clusters(sl):
        thr = -np.log10(alpha)
        sig = np.abs(sl) > thr
        out, i = [], 0
        while i < len(sig):
            if sig[i]:
                j = i
                while j + 1 < len(sig) and sig[j + 1] and np.sign(sl[j + 1]) == np.sign(sl[i]):
                    j += 1
                out.append((i, j, float(np.abs(sl[i:j + 1]).sum())))
                i = j + 1
            else:
                i += 1
        return out

    obs = clusters(signed(hit, miss))
    null = np.zeros(n_perm)
    for b in range(n_perm):
        sw = rng.random(len(hit)) < 0.5
        h = np.where(sw[:, None], miss, hit); m = np.where(sw[:, None], hit, miss)
        c = clusters(signed(h, m))
        null[b] = max([x[2] for x in c], default=0.0)
    return [(a, b, mass, float((null >= mass).mean())) for a, b, mass in obs]


def control_trials(s):
    """Control bursts in time order with a trial number. trial_index repeats across the recording
    blocks (rep_num of the trials table), so a trial is counted from each burst with
    burst_index_in_trial 0."""
    st = s["stim"].sort_values("start_time").reset_index(drop=True)
    st["trial"] = (st.burst_index_in_trial == 0).cumsum()
    return st


def control_responses(s, rng, currents=(5.0,), keep_spikes=False, n_bursts=3):
    """Responses of a passive control session, whose trials hold 3 bursts of 10 pulses at 50 Hz
    (file metadata) in place of the 700 ms train. Assumptions, as the paper gives no window for
    these mice: the stimulation count is the spikes inside the bursts (3 x 200 ms), the pre-stimulus
    window is 600 ms before the first burst, pulse-locking uses the 20 ms interpulse interval with
    the Methods' blanking (first 1.5 ms, last 0.5 ms), and the time to maximum is taken over the
    concatenated bursts. Other rules as in session_responses.

    With n_bursts=10 (a variant), the trial is taken as 10 bursts at 0.5 s spacing from the first
    tabled burst, the stimulation that the spikes follow (notebook, control sanity check), though
    the tables list 3; the pre-stimulus window is then 2 s (10 x 200 ms) before the first burst.
    """
    st = control_trials(s)
    rows, keep = [], {}
    for (ch, cur), g in st.groupby(["stim_channel", "current_uA"]):
        if cur not in currents:
            continue
        trials = g.groupby("trial")
        first = trials.start_time.min().to_numpy()
        if n_bursts == 3:
            bursts = g.start_time.to_numpy()
            bt = g.trial.map({t: i for i, t in enumerate(trials.groups)}).to_numpy()
        else:
            bursts = (first[:, None] + 0.5 * np.arange(n_bursts)[None, :]).ravel()
            bt = np.repeat(np.arange(len(first)), n_bursts)
        nt = len(first)
        dur = 0.2
        for ui, spk in enumerate(s["spikes"]):
            cb = window_counts(spk, bursts, 0.0, dur)
            c_stim = np.bincount(bt, cb, minlength=nt)
            c_pre = window_counts(spk, first, -n_bursts * dur, 0.0)
            r_stim, r_pre = c_stim / (n_bursts * dur), c_pre / (n_bursts * dur)
            sd = r_pre.std(ddof=1) if nt > 1 else np.nan
            z = (r_stim.mean() - r_pre.mean()) / sd if sd > 0 else np.inf
            if nt > 1 and np.any(c_stim != c_pre):
                t, p2 = stats.ttest_rel(c_stim, c_pre)
            else:
                t, p2 = 0.0, 1.0
            mod = (p2 < 0.05) and (t > 0) and c_stim.sum() >= 50 and r_pre.mean() >= 0.5
            row = dict(subject=s["subject"], session=s["session"], unit=ui, stim_channel=int(ch),
                       current=float(cur), n_trials=nt, n_spikes=int(c_stim.sum()), z=z, p_two=p2,
                       modulated=bool(mod))
            if mod:
                rel, tb = relative_spikes(spk, bursts, 0.0, dur)
                row["ttm_ms"] = time_to_max(rel, len(bursts), dur)
                H = pulse_histogram(rel, tb, len(bursts), n_pulses=10, ipi=0.020)
                pl, obs, thr, pk, pkt = pulse_locking(H, len(bursts), rng, n_pulses=10)
                row.update(pl=bool(pl), pli=obs, peak_prob=pk)
                if keep_spikes:
                    keep[(int(ch), float(cur), ui)] = (rel, tb)
            rows.append(row)
    out = pd.DataFrame(rows)
    return (out, keep) if keep_spikes else out
