"""Loading and reusable measures for the Allen Visual Behavior Neuropixels dandiset (DANDI:000713).

Written for the attempt on Souza et al. (2026), "Reward coding across mouse visual cortical areas",
doi:10.3389/fnbeh.2026.1944695. Files are streamed from the archive with remfile and h5py; nothing is
written to disk.

Where each parameter comes from is said beside it: "claims" for the claims file's criterion (which
cites the paper), "M&M x.y" for a passage of the paper's Materials and methods taken under protocol
author step 1.6, "assumption" for a choice the paper leaves open, and "standard" for a detail that
cannot change a result.
"""
import concurrent.futures as cf
import numpy as np
import pandas as pd
import h5py
import remfile
import requests

DANDISET = "000713"
VERSION = "0.240702.1725"  # the version the paper cites (M&M 2.1)
API = "https://api.dandiarchive.org/api"
AREAS = ["VISp", "VISl", "VISrl", "VISal", "VISpm", "VISam"]  # order of the paper's Results 3.1

# Allen default quality thresholds (AllenSDK VBN defaults), used for reading (b) of the link claim.
QC = dict(amplitude_cutoff=0.1, presence_ratio=0.95, isi_violations=0.5)


def list_sessions():
    """The session files of the pinned version (one per ecephys session; probe LFP and behavior-only
    files left out), as a DataFrame with path, asset_id and size."""
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=1000"
    rows = []
    while url:
        r = requests.get(url, timeout=60).json()
        rows += r["results"]
        url = r["next"]
    df = pd.DataFrame(rows)
    keep = df.path.str.endswith(".nwb") & ~df.path.str.contains("_image.nwb") & ~df.path.str.contains("probe-")
    return df[keep][["path", "asset_id", "size"]].sort_values("path").reset_index(drop=True), df


def s3_url(asset_id):
    r = requests.head(f"{API}/assets/{asset_id}/download/", allow_redirects=False, timeout=60)
    return r.headers["Location"]


def open_nwb(asset_id):
    return h5py.File(remfile.File(s3_url(asset_id)), "r")


def _s(x):
    return x.decode() if isinstance(x, bytes) else str(x)


def read_meta(asset_id):
    """Everything about a session except spike times and waveforms."""
    f = open_nwb(asset_id)
    out = {"asset_id": asset_id}
    out["subject"] = _s(f["general/subject/subject_id"][()])
    out["genotype"] = _s(f["general/subject/genotype"][()])
    out["session_type"] = _s(f["session_description"][()])
    out["identifier"] = _s(f["identifier"][()])
    out["session_start_time"] = _s(f["session_start_time"][()])[:10]
    md = f["general/metadata"].attrs
    out["behavior_session_id"] = int(md["behavior_session_id"])
    # units
    u = f["units"]
    e = f["general/extracellular_ephys/electrodes"]
    eid = e["id"][:]
    el = pd.DataFrame({"id": eid, "location": [_s(x) for x in e["location"][:]],
                       "probe_channel_number": e["probe_channel_number"][:],
                       "probe_vertical_position": e["probe_vertical_position"][:],
                       "x": e["x"][:], "y": e["y"][:], "z": e["z"][:],
                       "group_name": [_s(x) for x in e["group_name"][:]]}).set_index("id")
    cols = ["amplitude_cutoff", "presence_ratio", "isi_violations", "firing_rate", "waveform_duration",
            "snr", "peak_channel_id", "PT_ratio"]
    ud = pd.DataFrame({c: u[c][:] for c in cols})
    ud["unit_id"] = u["id"][:]
    ud["quality"] = [_s(x) for x in u["quality"][:]]
    idx = u["spike_times_index"][:].astype(np.int64)
    ud["st_start"] = np.r_[0, idx[:-1]]
    ud["st_stop"] = idx
    widx = u["waveform_mean_index"][:].astype(np.int64)
    ud["wf_start"] = np.r_[0, widx[:-1]]
    ud["wf_stop"] = widx
    j = el.loc[ud.peak_channel_id.values]
    for c in ["location", "probe_channel_number", "probe_vertical_position", "x", "y", "z", "group_name"]:
        ud[c] = j[c].values
    ud["row"] = np.arange(len(ud))
    out["units"] = ud
    # trials
    t = f["intervals/trials"]
    tcols = ["start_time", "stop_time", "go", "catch", "hit", "miss", "false_alarm", "correct_reject",
             "aborted", "auto_rewarded", "is_change", "change_time_no_display_delay", "response_time",
             "reward_time", "reward_volume"]
    out["trials"] = pd.DataFrame({c: t[c][:] for c in tcols})
    out["licks"] = f["processing/licking/licks/timestamps"][:]
    out["reward_times"] = f["processing/rewards/volume/timestamps"][:]
    out["reward_auto"] = f["processing/rewards/autorewarded/data"][:]
    # stimulus presentations of the natural-image blocks
    key = [k for k in f["intervals"].keys() if k.startswith("Natural_Images")][0]
    p = f["intervals/" + key]
    pcols = ["start_time", "stop_time", "stimulus_block", "active", "is_change", "rewarded", "omitted",
             "flashes_since_change", "trials_id", "is_sham_change"]
    pr = pd.DataFrame({c: p[c][:] for c in pcols})
    pr["image_name"] = [_s(x) for x in p["image_name"][:]]
    out["presentations"] = pr
    blocks = {}
    for k in f["intervals"].keys():
        if not k.endswith("_presentations"):
            continue
        q = f["intervals/" + k]
        b = q["stimulus_block"][:]
        st = q["start_time"][:]
        sp = q["stop_time"][:]
        for bb in np.unique(b):
            s = b == bb
            blocks[int(bb)] = (k.replace("_presentations", ""), float(st[s].min()), float(sp[s].max()), int(s.sum()))
    out["blocks"] = blocks
    out["probes"] = sorted(set(el.group_name))
    f.close()
    return out


def read_meta_many(asset_ids, workers=6):
    with cf.ThreadPoolExecutor(workers) as ex:
        return list(ex.map(read_meta, asset_ids))


# ---------------------------------------------------------------------------------------------
# Per-session processing: streams the spike times of the selected units and reduces them to the
# per-unit quantities the claims use. Parameters:
BIN = 0.010          # PSTH bin, 10 ms (M&M 2.2)
SIGMA = 0.025        # Gaussian kernel sigma, 25 ms (M&M 2.2); truncated at 4 sigma (standard)
WIN = (-0.5, 2.0)    # peri-reward window of the split-half test (M&M 2.2)
WIDE = (-2.1, 2.1)   # stored PSTH span: covers the M baselines to -2.0 s (M&M 2.5) and NMF padding
RESP = 0.75          # response window 0 to 0.75 s (M&M 2.4)
BASE = 0.5           # baseline 0.5 s before the image change (M&M 2.4)
CVBIN = 0.050        # population count bin, 50 ms (M&M 2.6)
PP = (-0.75, 0.75)   # stored span around image changes for the pre/post CV (claim fig2f-pre-post-cv)


def gauss_kernel(sigma_bins, truncate=4.0):
    r = int(np.ceil(truncate * sigma_bins))
    x = np.arange(-r, r + 1)
    k = np.exp(-0.5 * (x / sigma_bins) ** 2)
    return k / k.sum()


def smooth(x, sigma_bins=SIGMA / BIN, axis=-1):
    """Convolve with a normalised Gaussian kernel, zero outside the window ('same' length)."""
    from scipy.ndimage import convolve1d
    return convolve1d(x, gauss_kernel(sigma_bins), axis=axis, mode="constant", cval=0.0)


def rowcorr(a, b):
    a = a - a.mean(-1, keepdims=True)
    b = b - b.mean(-1, keepdims=True)
    den = np.sqrt((a * a).sum(-1) * (b * b).sum(-1))
    with np.errstate(invalid="ignore", divide="ignore"):
        return np.where(den > 0, (a * b).sum(-1) / den, np.nan)


def counts_in(st, starts, width):
    """Spike counts of sorted spike times st in [s, s + width) for each s."""
    return np.searchsorted(st, starts + width) - np.searchsorted(st, starts)


def split_psth(pos, ev, nb, odd, lut=None):
    """Odd and even PSTH counts (P, 2, nb) of spike positions pos (P, N) or (N,) for windows starting
    at ev (sorted, non-overlapping), nb bins of BIN each. lut, from make_lut, speeds up the search for
    the event each spike falls in; the bin is then computed exactly."""
    pos = np.atleast_2d(pos)
    P = pos.shape[0]
    rowi = np.broadcast_to(np.arange(P)[:, None], pos.shape)
    if lut is not None:
        t0, step, tab = lut
        g = ((pos - t0) / step).astype(np.int64)
        inr = (g >= 0) & (g < len(tab))
        k = np.full(pos.shape, -1, np.int64)
        k[inr] = tab[g[inr]]
        sel = k >= 0
        p = pos[sel]
        kk = k[sel]
        rr = rowi[sel]
    else:
        k = np.searchsorted(ev, pos, side="right") - 1
        sel = k >= 0
        p = pos[sel]
        kk = k[sel]
        rr = rowi[sel]
    b = np.floor((p - ev[kk]) / BIN).astype(np.int64)
    ok = (b >= 0) & (b < nb)
    flat = (rr[ok] * 2 + odd[kk[ok]].astype(np.int64)) * nb + b[ok]
    return np.bincount(flat, minlength=P * 2 * nb).reshape(P, 2, nb)


def make_lut(ev, nb, step=BIN):
    """Table over a 10 ms grid giving, for each grid cell, the window it overlaps (or -1)."""
    t0 = ev[0] - step
    n = int(np.ceil((ev[-1] + nb * BIN - t0) / step)) + 2
    tab = np.full(n, -1, np.int64)
    for k, e in enumerate(ev):
        i0 = int(np.floor((e - t0) / step))
        i1 = int(np.floor((e + nb * BIN - t0) / step))
        tab[i0:i1 + 1] = k
    return t0, step, tab


def isi_null(st_block, ev, nb, odd, nperm, rng, chunk=2_000_000, lut=None):
    """r_split of ISI-shuffled spike trains (M&M 2.3): ISIs permuted, the train rebuilt from its
    first spike. Given the active block's spikes this is reading (1a) of claim fig1e-cohort-size's
    criterion; given the whole recording's spikes, reading (1b)."""
    n = len(st_block)
    out = np.full(nperm, np.nan)
    if n < 3:
        return out
    isi = np.diff(st_block).astype(np.float64)
    step = max(1, chunk // n)
    for s in range(0, nperm, step):
        P = min(step, nperm - s)
        X = rng.permuted(np.broadcast_to(isi, (P, n - 1)), axis=1)
        pos = np.empty((P, n))
        pos[:, 0] = st_block[0]
        np.cumsum(X, axis=1, out=pos[:, 1:])
        pos[:, 1:] += st_block[0]
        h = split_psth(pos, ev, nb, odd, lut).astype(float)
        sm = smooth(h)
        out[s:s + P] = rowcorr(sm[:, 0], sm[:, 1])
    return out


def select_units(units):
    """Units of the six areas with quality 'good' and presence ratio >= 0.95 (the reading of claim
    data-sessions-units that matches the paper's count; an assumption)."""
    return units[units.location.isin(AREAS) & (units.quality == "good") & (units.presence_ratio >= 0.95)]


def wf_measures(w, dt=1 / 30000.0):
    """Trough-to-peak duration and half-width (ms) of a mean waveform (M&M 2.5): trough = minimum;
    duration = trough to the following maximum; half-width = width of the trough at half its minimum
    amplitude (linear interpolation; standard)."""
    w = np.asarray(w, float)
    i = int(np.argmin(w))
    if i >= len(w) - 1:
        return np.nan, np.nan
    j = i + int(np.argmax(w[i:]))
    dur = (j - i) * dt * 1e3
    h = w[i] / 2.0
    l = i
    while l > 0 and w[l] < h:
        l -= 1
    r = i
    while r < len(w) - 1 and w[r] < h:
        r += 1
    if w[l] >= h and l < i:
        lt = l + (h - w[l]) / (w[l + 1] - w[l])
    else:
        lt = np.nan
    if w[r] >= h and r > i:
        rt = r - 1 + (h - w[r - 1]) / (w[r] - w[r - 1])
    else:
        rt = np.nan
    hw = (rt - lt) * dt * 1e3
    return dur, hw


def first_after(x, t):
    """First element of sorted x after each t (nan when none)."""
    i = np.searchsorted(x, t, side="right")
    out = np.full(len(t), np.nan)
    ok = i < len(x)
    out[ok] = x[i[ok]]
    return out


def bouts(licks, gap):
    """Lick bouts: runs of licks with inter-lick gaps <= gap (an assumption; claim hits-vs-lick-bouts).
    Returns (onset, offset) arrays."""
    if len(licks) == 0:
        return np.array([]), np.array([])
    br = np.where(np.diff(licks) > gap)[0]
    on = np.r_[licks[0], licks[br + 1]]
    off = np.r_[licks[br], licks[-1]]
    return on, off


def session_events(meta):
    """Behavioural events of a session, all in the session clock (seconds)."""
    pr = meta["presentations"]
    tr = meta["trials"]
    b = meta["blocks"]
    a0, a1 = b[0][1], b[0][2]
    p0, p1 = b[5][1], b[5][2]
    ev = {"a0": a0, "a1": a1, "p0": p0, "p1": p1}
    rt = meta["reward_times"]
    auto = meta["reward_auto"].astype(bool)
    ev["rew_all"] = rt
    ev["rew_auto"] = auto
    earned = np.sort(rt[~auto])
    ev["earned"] = earned
    # rewards whose whole window lies in the active block (M&M 2.2)
    ok = (earned + WIN[0] >= a0) & (earned + WIN[1] <= a1)
    ev["rew"] = earned[ok]
    # image change of each trial: the change presentation of block 0 with that trial id
    ch = pr[(pr.stimulus_block == 0) & (pr.is_change == 1)]
    chg = dict(zip(ch.trials_id, ch.start_time))
    sh = pr[(pr.stimulus_block == 0) & (pr.is_sham_change.astype(bool))]
    shm = dict(zip(sh.trials_id, sh.start_time))
    tid = np.arange(len(tr))
    tr = tr.assign(change=[chg.get(i, np.nan) for i in tid], sham=[shm.get(i, np.nan) for i in tid])
    hit = tr[tr.hit & np.isfinite(tr.reward_time) & ~tr.auto_rewarded & np.isfinite(tr.change)]
    ev["hit_change"] = hit.change.values
    ev["hit_change_nodelay"] = hit.change_time_no_display_delay.values
    ev["hit_reward"] = hit.reward_time.values
    ev["latency"] = hit.reward_time.values - hit.change.values
    ev["med_lat"] = float(np.median(ev["latency"])) if len(hit) else np.nan
    miss = tr[tr.miss & np.isfinite(tr.change)]
    ev["miss_change"] = miss.change.values
    fa = tr[tr.false_alarm]
    # sham change of each false-alarm trial: the start of its sham-change presentation, the clock of
    # the hit trials' change presentations. Trials without one are counted and left out, so that no
    # time comes from change_time_no_display_delay, a clock about 44 ms earlier (verifier round 1).
    ev["fa_change"] = fa.sham.values[np.isfinite(fa.sham.values)]
    ev["n_fa_trials"] = int(len(fa))
    ev["n_fa_no_sham"] = int((~np.isfinite(fa.sham.values)).sum())
    ev["n_hit_all"] = int(tr.hit.sum())
    ev["n_hit_auto"] = int((tr.hit & tr.auto_rewarded.astype(bool)).sum())
    ev["n_hit_no_reward"] = int((tr.hit & ~np.isfinite(tr.reward_time)).sum())
    ev["n_hit_no_change"] = int((tr.hit & ~np.isfinite(tr.change)).sum())
    ev["n_hit_trials"] = int(tr.hit.sum())
    licks = np.sort(meta["licks"])
    ev["licks"] = licks
    ev["fa_lick"] = first_after(licks, ev["fa_change"])
    ev["hit_lick"] = first_after(licks, ev["hit_change"])
    # all image changes of each block (fig2f) and replayed changes of block 5 (Family A)
    ev["act_changes"] = ch.start_time.values
    ev["act_change_hitmiss"] = np.isin(ch.trials_id.values, np.r_[hit.index.values, miss.index.values])
    pc = pr[(pr.stimulus_block == 5) & (pr.is_change == 1)]
    ev["pas_changes"] = pc.start_time.values
    # lick bouts within the active block
    la = licks[(licks >= a0) & (licks <= a1)]
    for gap in (0.25, 0.5):
        on, off = bouts(la, gap)
        allr = np.sort(rt)
        i0 = np.searchsorted(allr, on)
        i1 = np.searchsorted(allr, off + 1e-9, side="right")
        unr = (i1 - i0) == 0
        on = on[unr]
        on = on[(on - BASE >= a0) & (on + RESP <= a1)]
        ev[f"bout_on_{int(gap*1000)}"] = on
    return ev


def _amp(st, event, base_t):
    """Per-trial amplitude: mean rate in [event, event + 0.75) minus mean rate in the 0.5 s before
    base_t (the trial's image change) (M&M 2.4)."""
    return counts_in(st, event, RESP) / RESP - counts_in(st, base_t - BASE, BASE) / BASE


def unit_tests(a1, a2):
    """Family statistics for one unit: Wilcoxon of each condition against zero (responsiveness,
    M&M 2.4), two-sided Mann-Whitney, and SI = (A1 - A2) / (|A1| + |A2|) (eq. 3)."""
    from scipy.stats import wilcoxon, mannwhitneyu
    def wp(x):
        x = x[np.isfinite(x)]
        if len(x) < 1 or np.all(x == 0):
            return np.nan
        try:
            return wilcoxon(x).pvalue
        except ValueError:
            return np.nan
    p1, p2 = wp(a1), wp(a2)
    if len(a1) and len(a2):
        pm = mannwhitneyu(a1, a2, alternative="two-sided").pvalue
    else:
        pm = np.nan
    m1, m2 = np.mean(a1) if len(a1) else np.nan, np.mean(a2) if len(a2) else np.nan
    den = abs(m1) + abs(m2)
    si = (m1 - m2) / den if den > 0 else np.nan
    return p1, p2, pm, si


def _wilcoxon_rows(X):
    """Two-sided Wilcoxon signed-rank test of each row against zero, vectorised: zeros dropped
    (scipy's default zero_method), normal approximation with tie correction (scipy's 'approx'
    method; scipy uses an exact test only for n <= 50 without ties or zeros: a standard choice)."""
    from scipy.stats import rankdata, norm
    out = np.full(X.shape[0], np.nan)
    if X.shape[1] == 0:
        return out
    a = np.abs(X)
    nz = X != 0
    nr = nz.sum(1)
    r = rankdata(a, axis=1)            # zeros rank lowest
    r = r - (~nz).sum(1, keepdims=True)  # ranks among the non-zero values
    wplus = np.where(X > 0, r, 0).sum(1)
    mean = nr * (nr + 1) / 4.0
    var = nr * (nr + 1) * (2 * nr + 1) / 24.0
    tie = np.zeros(X.shape[0])
    for i in np.where(nr > 0)[0]:
        _, c = np.unique(a[i][nz[i]], return_counts=True)
        tie[i] = ((c ** 3 - c).sum()) / 48.0
    var = var - tie
    ok = (nr > 0) & (var > 0)
    z = (wplus[ok] - mean[ok]) / np.sqrt(var[ok])
    out[ok] = 2 * norm.sf(np.abs(z))
    return out


def family_tests(X1, X2):
    """Vectorised over units (rows): Wilcoxon signed-rank of each condition's per-trial amplitudes
    against zero (responsiveness, M&M 2.4), two-sided Mann-Whitney U between conditions (M&M 2.4) and
    SI = (A1 - A2) / (|A1| + |A2|) (eq. 3), A1 the rewarded condition."""
    from scipy.stats import mannwhitneyu
    p1, p2 = _wilcoxon_rows(X1), _wilcoxon_rows(X2)
    if X1.shape[1] and X2.shape[1]:
        pm = mannwhitneyu(X1, X2, axis=1, alternative="two-sided").pvalue
    else:
        pm = np.full(X1.shape[0], np.nan)
    m1 = X1.mean(1) if X1.shape[1] else np.full(X1.shape[0], np.nan)
    m2 = X2.mean(1) if X2.shape[1] else np.full(X1.shape[0], np.nan)
    den = np.abs(m1) + np.abs(m2)
    with np.errstate(all="ignore"):
        si = np.where(den > 0, (m1 - m2) / den, np.nan)
    return p1, p2, pm, si


UPS = 200  # samples of the upsampled waveform (variant of reading (a), claim waveform-ambiguous-band)


def process_session(meta, nperm, seed_null, seed_jit, n_jit=20):
    """Stream one session's selected units and reduce them. Returns (units DataFrame of scalar
    per-unit results, dict of arrays)."""
    from scipy.signal import resample
    ev = session_events(meta)
    units = select_units(meta["units"]).copy()
    f = open_nwb(meta["asset_id"])
    U = f["units"]
    W = U["waveform_mean"]
    rew = ev["rew"]
    nb = int(round((WIN[1] - WIN[0]) / BIN))
    nbw = int(round((WIDE[1] - WIDE[0]) / BIN))
    evs = rew + WIN[0]
    odd = (np.arange(len(rew)) % 2).astype(np.int64)  # chronological interleave (M&M 2.3)
    rng_null = np.random.default_rng(seed_null)
    lut = make_lut(evs, nb) if len(evs) else None
    rng_jit = np.random.default_rng(seed_jit)
    med = ev["med_lat"]
    lat = ev["latency"]
    pas = ev["pas_changes"]
    pas = pas[(pas - BASE >= ev["p0"]) & (pas + med + RESP <= ev["p1"])]
    jit_lat = rng_jit.choice(lat, size=(n_jit, len(pas)), replace=True) if len(lat) else np.zeros((n_jit, 0))
    a0, a1 = ev["a0"], ev["a1"]
    ncv = int(np.floor((a1 - a0) / CVBIN))
    ppn = int(round((PP[1] - PP[0]) / CVBIN))
    actc, pasc = ev["act_changes"], ev["pas_changes"]
    res = []
    psth = np.zeros((len(units), nbw), np.float32)
    nulls = np.zeros((len(units), nperm), np.float32)
    cvbins = np.zeros((len(units), ncv), np.uint8)
    pp_act = np.zeros((len(units), len(actc), ppn), np.uint8)
    pp_pas = np.zeros((len(units), len(pasc), ppn), np.uint8)
    # read contiguous runs of units in one request each
    fa_ok = np.isfinite(ev["fa_lick"])
    hl_ok = np.isfinite(ev["hit_lick"])
    hl = ev["hit_lick"][hl_ok]
    hc = ev["hit_change"][hl_ok]
    amps = {}
    rows = units.row.values
    runs = np.split(np.arange(len(rows)), np.where(np.diff(rows) > 1)[0] + 1)
    for run in runs:
        r0, r1 = rows[run[0]], rows[run[-1]]
        s0 = int(units.st_start.iloc[run[0]])
        s1 = int(units.st_stop.iloc[run[-1]])
        block = U["spike_times"][s0:s1]
        for ii in run:
            r = units.iloc[ii]
            st = block[int(r.st_start) - s0:int(r.st_stop) - s0]
            if np.any(np.diff(st) < 0):
                st = np.sort(st)
            d = {"unit_id": int(r.unit_id)}
            d["n_spikes"] = len(st)
            d["t_first"] = st[0] if len(st) else np.nan
            d["t_last"] = st[-1] if len(st) else np.nan
            isi = np.diff(st)
            d["median_isi_all"] = np.median(isi) if len(isi) else np.nan
            sa = st[(st >= a0) & (st <= a1)]
            d["n_active"] = len(sa)
            isa = np.diff(sa)
            d["median_isi_active"] = np.median(isa) if len(isa) else np.nan
            # PSTH and split-half reliability
            h = split_psth(sa, evs, nb, odd)[0].astype(float)
            sm = smooth(h)
            d["r_split"] = float(rowcorr(sm[0], sm[1]))
            wide = split_psth(sa, rew + WIDE[0], nbw, np.zeros(len(rew), np.int64))[0, 0]
            psth[ii] = wide
            nl = isi_null(sa, evs, nb, odd, nperm, rng_null, lut=lut)
            nulls[ii] = nl
            if np.isfinite(d["r_split"]):
                d["p_split"] = (1 + np.sum(nl >= d["r_split"])) / (nperm + 1)  # eq. (2)
            else:
                d["p_split"] = np.nan
            # amplitudes (M&M 2.4); tests are run for all units at once after the loop
            amps.setdefault("hit", []).append(_amp(st, ev["hit_reward"], ev["hit_change"]))
            amps.setdefault("pas", []).append(_amp(st, pas + med, pas))
            amps.setdefault("miss", []).append(_amp(st, ev["miss_change"] + med, ev["miss_change"]))
            # latency jitter control (M&M 2.4): pseudo-reward latencies drawn from the hit latencies
            for j in range(n_jit):
                amps.setdefault(f"J{j}", []).append(_amp(st, pas + jit_lat[j], pas))
            # hits against false alarms (Discussion, paragraph 6)
            amps.setdefault("FAa", []).append(_amp(st, ev["fa_lick"][fa_ok], ev["fa_change"][fa_ok]))
            amps.setdefault("FAb", []).append(_amp(st, ev["fa_change"] + med, ev["fa_change"]))
            # hits against unrewarded lick bouts (Discussion, paragraph 7)
            amps.setdefault("HLa", []).append(_amp(st, hl, hl))
            amps.setdefault("HLb", []).append(_amp(st, hl, hc))
            for gap in (250, 500):
                on = ev[f"bout_on_{gap}"]
                amps.setdefault(f"LB{gap}", []).append(_amp(st, on, on))
            # population counts (M&M 2.6)
            c = np.bincount(((sa - a0) / CVBIN).astype(np.int64), minlength=ncv + 1)[:ncv]
            cvbins[ii] = np.minimum(c, 255)
            for arr, ch in ((pp_act, actc), (pp_pas, pasc)):
                if len(ch):
                    k = np.searchsorted(ch + PP[0], st, side="right") - 1
                    ok = k >= 0
                    kk = np.where(ok, k, 0)
                    b = np.floor((st - (ch[kk] + PP[0])) / CVBIN).astype(np.int64)
                    ok &= (b >= 0) & (b < ppn)
                    hh = np.bincount(kk[ok] * ppn + b[ok], minlength=len(ch) * ppn).reshape(len(ch), ppn)
                    arr[ii] = np.minimum(hh, 255)
            # waveform on the peak channel (M&M 2.5)
            w = W[int(r.wf_start) + int(r.probe_channel_number)]
            d["wf_dur"], d["wf_hw"] = wf_measures(w)
            # variant: the waveform resampled to 200 points (Fourier), the upsampling of the Allen
            # waveform-metrics code (ecephys_spike_sorting, mean_waveforms; an assumption)
            d["wf_dur_up"], d["wf_hw_up"] = wf_measures(resample(w, UPS), dt=len(w) / UPS / 30000.0)
            res.append(d)
    f.close()
    df = pd.DataFrame(res)
    M = {k: np.array(v, dtype=float).reshape(len(res), -1) for k, v in amps.items()}
    tests = [("A", "hit", "pas"), ("B", "hit", "miss"), ("FAa", "hit", "FAa"), ("FAb", "hit", "FAb")]
    tests += [(f"J{j}", "hit", f"J{j}") for j in range(n_jit)]
    tests += [(f"LB{g}{b}", "HL" + b, f"LB{g}") for g in (250, 500) for b in ("a", "b")]
    for name, k1, k2 in tests:
        p1, p2, pm, si = family_tests(M[k1], M[k2])
        df[f"{name}_p1"], df[f"{name}_p2"], df[f"{name}_pmw"], df[f"{name}_si"] = p1, p2, pm, si
    for k in ("hit", "pas", "miss", "FAa", "LB250", "LB500"):
        df[f"n_{k}"] = M[k].shape[1]
    df = units.reset_index(drop=True).join(df.drop(columns=["unit_id"]))
    arrays = dict(psth=psth, nulls=nulls, cvbins=cvbins, pp_act=pp_act, pp_pas=pp_pas,
                  act_hitmiss=ev["act_change_hitmiss"], n_rew=len(rew))
    return df, arrays, ev


def _job(args):
    asset_id, k, nperm, seed_null, seed_jit = args
    import warnings
    warnings.filterwarnings("ignore")
    for attempt in range(3):
        try:
            meta = read_meta(asset_id)
            df, arr, ev = process_session(meta, nperm, seed_null + k, seed_jit + k)
            df = df.copy()
            df["session"] = k
            meta.pop("units")
            return k, meta, df, arr, ev
        except Exception as e:  # network errors: retry
            err = e
    raise err


def _rec_job(args):
    """p_split under reading (1b) of the null (ISIs shuffled over the whole recording, the train rebuilt
    from the recording's first spike) for the selected units of one session, in the order of
    process_session. Its generator is the claim seed + 200 + k (reading 1a uses the claim seed + k)."""
    asset_id, k, nperm, seed_null = args
    import warnings
    warnings.filterwarnings("ignore")
    for attempt in range(3):
        try:
            meta = read_meta(asset_id)
            ev = session_events(meta)
            units = select_units(meta["units"])
            f = open_nwb(asset_id)
            rew = ev["rew"]
            nb = int(round((WIN[1] - WIN[0]) / BIN))
            evs = rew + WIN[0]
            odd = (np.arange(len(rew)) % 2).astype(np.int64)
            lut = make_lut(evs, nb) if len(evs) else None
            rng = np.random.default_rng(seed_null + 200 + k)
            out = []
            for r in units.itertuples():
                st = f["units/spike_times"][int(r.st_start):int(r.st_stop)]
                if np.any(np.diff(st) < 0):
                    st = np.sort(st)
                sa = st[(st >= ev["a0"]) & (st <= ev["a1"])]
                h = split_psth(sa, evs, nb, odd)[0].astype(float)
                sm = smooth(h)
                rs = float(rowcorr(sm[0], sm[1]))
                nl = isi_null(st, evs, nb, odd, nperm, rng, lut=lut)
                out.append((1 + np.sum(nl >= rs)) / (nperm + 1) if np.isfinite(rs) else np.nan)
            f.close()
            return k, np.array(out)
        except Exception as e:  # network errors: retry
            err = e
    raise err


def run_rec_null(asset_ids, ks, nperm, seed_null, workers=6):
    """Reading (1b) of the ISI null for sessions ks (indices into asset_ids); returns {k: p values}."""
    import multiprocessing as mp
    ctx = mp.get_context("spawn")
    jobs = [(asset_ids[k], k, nperm, seed_null) for k in ks]
    with cf.ProcessPoolExecutor(workers, mp_context=ctx) as ex:
        return dict(ex.map(_rec_job, jobs))


def run_sessions(asset_ids, nperm, seed_null, seed_jit, workers=6):
    """Process sessions in parallel (spawned processes). Session k uses generators seeded seed + k (protocol: a further
    generator for the same claim adds 1 to the seed)."""
    import multiprocessing as mp
    ctx = mp.get_context("spawn")
    jobs = [(a, k, nperm, seed_null, seed_jit) for k, a in enumerate(asset_ids)]
    out = [None] * len(jobs)
    with cf.ProcessPoolExecutor(workers, mp_context=ctx) as ex:
        for k, meta, df, arr, ev in ex.map(_job, jobs):
            out[k] = (meta, df, arr, ev)
    return out


def read_light(asset_id):
    """Genotype and the units' area and quality columns only (for counting sessions and units)."""
    f = open_nwb(asset_id)
    e = f["general/extracellular_ephys/electrodes"]
    loc = dict(zip(e["id"][:], [_s(x) for x in e["location"][:]]))
    u = f["units"]
    df = pd.DataFrame({"location": [loc[p] for p in u["peak_channel_id"][:]],
                       "quality": [_s(x) for x in u["quality"][:]],
                       "presence_ratio": u["presence_ratio"][:],
                       "amplitude_cutoff": u["amplitude_cutoff"][:],
                       "isi_violations": u["isi_violations"][:]})
    out = dict(asset_id=asset_id, subject=_s(f["general/subject/subject_id"][()]),
               genotype=_s(f["general/subject/genotype"][()]),
               session_type=_s(f["session_description"][()]),
               session_start_time=_s(f["session_start_time"][()])[:10], units=df)
    f.close()
    return out


# ---------------------------------------------------------------------------------------------
# Measures used after all sessions are processed.

def bh(p, q=0.05):
    """Benjamini-Hochberg: boolean array of rejections at level q (M&M 2.3, 2.4, 2.8); nan never
    rejected."""
    p = np.asarray(p, float)
    out = np.zeros(len(p), bool)
    ok = np.isfinite(p)
    pv = p[ok]
    m = len(pv)
    if m == 0:
        return out
    o = np.argsort(pv)
    thr = q * np.arange(1, m + 1) / m
    below = pv[o] <= thr
    if below.any():
        kmax = np.where(below)[0].max()
        rej = np.zeros(m, bool)
        rej[o[:kmax + 1]] = True
        out[np.where(ok)[0]] = rej
    return out


def bh_by(df, pcol, groupcol, mask=None, q=0.05):
    """BH applied separately within each group (area), over the rows in mask."""
    out = np.zeros(len(df), bool)
    if mask is None:
        mask = np.ones(len(df), bool)
    for g, idx in df.groupby(groupcol).indices.items():
        idx = idx[mask[idx]]
        out[idx] = bh(df[pcol].values[idx], q)
    return out


def family_pass(df, fam, sh_pos, q=0.05, responsive=True):
    """Units significant in family fam: split-half positive, responsive in at least one condition
    (Wilcoxon p < 0.05, M&M 2.4), BH at q per area over those units' Mann-Whitney p."""
    resp = (df[f"{fam}_p1"] < 0.05) | (df[f"{fam}_p2"] < 0.05)
    elig = sh_pos & (resp.values if responsive else True) & np.isfinite(df[f"{fam}_pmw"].values)
    return bh_by(df, f"{fam}_pmw", "location", elig, q), elig


def cv_windows(n, win_bins=200):
    """CV of summed counts n (..., T) in non-overlapping windows of win_bins bins (10 s of 50 ms
    bins, M&M 2.6): SD / mean of the bin counts in each window; nan when the mean is 0."""
    T = n.shape[-1] // win_bins * win_bins
    x = n[..., :T].reshape(n.shape[:-1] + (-1, win_bins)).astype(float)
    m = x.mean(-1)
    s = x.std(-1)
    with np.errstate(all="ignore"):
        return np.where(m > 0, s / m, np.nan)


def rank_biserial(d):
    """Matched-pairs rank-biserial correlation of differences d: (R+ - R-) / (R+ + R-)."""
    from scipy.stats import rankdata
    d = np.asarray(d, float)
    d = d[np.isfinite(d) & (d != 0)]
    if len(d) == 0:
        return np.nan
    r = rankdata(np.abs(d))
    return (r[d > 0].sum() - r[d < 0].sum()) / r.sum()


def effective_number(w):
    w = np.asarray(w, float)
    s = w.sum(1, keepdims=True)
    with np.errstate(all="ignore"):
        p = np.where(s > 0, w / s, np.nan)
        h = -np.nansum(np.where(p > 0, p * np.log(p), 0.0), axis=1)
    return np.exp(h), p


# ---------------------------------------------------------------------------------------------
# Cortical layers (M&M 2.5), from the Allen CCFv3 25 um annotation volume (Wang et al., 2020) as
# packaged by BrainGlobe (allen_mouse_25um v1.2), an outside input pinned by the GIN repository's
# commit and the file's SHA-256 (the paper gives no release; the 2017 annotation is the standard one).
ATLAS_URL = "https://gin.g-node.org/brainglobe/atlases/raw/master/allen_mouse_25um_v1.2.tar.gz"
ATLAS_COMMIT = "78272d68aacb9d0b2a7d00806d6305544924df4b"
ATLAS_SHA256 = "696276744cc6552e3be87b236498aebeb2de79be3b66ebffc1a620ee75a9c0a9"
LAYERS = ["1", "2/3", "4", "5", "6a", "6b"]
LAYER_GROUP = {"1": "supragranular", "2/3": "supragranular", "4": "granular", "5": "infragranular",
               "6a": "infragranular", "6b": "infragranular"}  # M&M 2.5


# The same annotation from the Allen Institute's own download (CCFv3, 2017 release, the volume BrainGlobe
# packages), with the structure ontology from the Allen API. Their paths carry no version, so each file is
# pinned by its SHA-256 (Last-Modified 2025-02-19 for the volume). Used when GIN refuses the request: on
# 2026-11-21 it answered 403 Forbidden to this runner for the whole site.
ALLEN_ANN_URL = ("https://download.alleninstitute.org/informatics-archive/current-release/mouse_ccf/"
                 "annotation/ccf_2017/annotation_25.nrrd")
ALLEN_ANN_SHA256 = "c620cbcc562183e4dcd40250d440130501781f74b41de35b1c1bdabace290c42"
ALLEN_ONT_URL = "http://api.brain-map.org/api/v2/structure_graph_download/1.json"
ALLEN_ONT_SHA256 = "b5f0d024d1df09ee18aef15093f55240f4a70b3924ee9689add612dadff80386"


def _laminar(name):
    return ", layer" in name.lower()


def _load_atlas_allen():
    """The Allen Institute's annotation_25.nrrd (gzip-encoded uint32, axes AP, DV, ML with AP fastest)
    and the structure graph, each checked against its SHA-256."""
    import gzip, hashlib, json
    raw = requests.get(ALLEN_ANN_URL, timeout=600).content
    sha = hashlib.sha256(raw).hexdigest()
    if sha != ALLEN_ANN_SHA256:
        raise ValueError(f"Allen annotation file changed: sha256 {sha}")
    k = raw.index(b"\n\n")
    head = dict(l.split(": ", 1) for l in raw[:k].decode().splitlines()[1:] if ": " in l)
    sizes = [int(v) for v in head["sizes"].split()]
    assert head["type"] == "unsigned int" and head["encoding"] == "gzip" and head["endian"] == "little"
    vol = np.frombuffer(gzip.decompress(raw[k + 2:]), "<u4").reshape(sizes[::-1]).transpose(2, 1, 0)
    ont = requests.get(ALLEN_ONT_URL, timeout=600).content
    sha2 = hashlib.sha256(ont).hexdigest()
    if sha2 != ALLEN_ONT_SHA256:
        raise ValueError(f"Allen structure graph changed: sha256 {sha2}")
    acr, stack = {}, list(json.loads(ont)["msg"])
    while stack:
        d = stack.pop()
        acr[d["id"]] = (d["acronym"], _laminar(d["name"]))
        stack += d.get("children", [])
    meta = dict(name="allen_mouse_25um (Allen Institute download, ccf_2017)", version="CCFv3 2017",
                orientation="AP, DV, ML", shape=list(vol.shape), resolution=[25, 25, 25])
    return np.ascontiguousarray(vol), acr, meta, sha + " / " + sha2


def load_atlas():
    """Annotation volume (AP, DV, ML at 25 um) and id -> (acronym, laminar), read in memory: BrainGlobe's
    package from GIN, or the Allen Institute's files when GIN cannot be reached."""
    import hashlib, io, json, tarfile
    import tifffile
    r = requests.get(ATLAS_URL, timeout=600)
    if r.status_code != 200:
        print("GIN answered %d; using the Allen Institute's files" % r.status_code)
        return _load_atlas_allen()
    raw = r.content
    sha = hashlib.sha256(raw).hexdigest()
    if sha != ATLAS_SHA256:
        raise ValueError(f"atlas file changed: sha256 {sha}")
    ann, acr, meta = None, None, None
    with tarfile.open(fileobj=io.BytesIO(raw), mode="r|gz") as t:
        for m in t:
            if m.name.endswith("annotation.tiff"):
                with tifffile.TiffFile(io.BytesIO(t.extractfile(m).read())) as tf:
                    ann = tf.asarray()  # the annotation volume (data, not a figure)
            elif m.name.endswith("structures.json"):
                # a structure is laminar only when its name says so ("Primary visual area, layer 4"),
                # so that "CA1" or "CA3" never reads as layer 1 or 3 (verifier round 1)
                acr = {d["id"]: (d["acronym"], _laminar(d["name"])) for d in json.load(t.extractfile(m))}
            elif m.name.endswith("metadata.json"):
                meta = json.load(t.extractfile(m))
            if ann is not None and acr is not None and meta is not None:
                break
    del raw
    return ann, acr, meta, sha


def split_layer(acronym, laminar=True):
    """'VISp2/3' -> ('VISp', '2/3'); a structure without a layer suffix, or whose name names no
    layer (laminar False), -> (acronym, None)."""
    if acronym is None:
        return None, None
    if not laminar:
        return acronym, None
    for L in sorted(LAYERS, key=len, reverse=True):
        if acronym.endswith(L) and len(acronym) > len(L):
            return acronym[: -len(L)], L
    return acronym, None


def unit_layers(ann, acr, x, y, z, max_steps=20):
    """CCF area, layer and the smallest displacement (um) along the three CCF axes that changes the
    laminar label (M&M 2.5), for unit coordinates x (AP), y (DV), z (ML) in um. Coordinates outside
    the volume, or non-positive, give no layer."""
    n = len(x)
    area = np.full(n, None, object)
    layer = np.full(n, None, object)
    dist = np.full(n, np.nan)
    ijk = np.round(np.c_[x, y, z] / 25.0).astype(int)
    shp = np.array(ann.shape)
    ok = np.all((ijk >= 0) & (ijk < shp), 1) & (np.asarray(x) > 0) & (np.asarray(y) > 0) & (np.asarray(z) > 0)
    lab_cache = {}

    def lab(v):
        if v not in lab_cache:
            a_ = acr.get(int(v))
            lab_cache[v] = split_layer(*a_) if a_ is not None else (None, None)
        return lab_cache[v]
    for i in np.where(ok)[0]:
        a, L = lab(ann[tuple(ijk[i])])
        area[i], layer[i] = a, L
        if L is None:
            continue
        best = np.inf
        for ax in range(3):
            for sgn in (-1, 1):
                p = ijk[i].copy()
                for s in range(1, max_steps + 1):
                    p[ax] += sgn
                    if p[ax] < 0 or p[ax] >= shp[ax]:
                        break
                    if lab(ann[tuple(p)])[1] != L:
                        best = min(best, s * 25.0)
                        break
        dist[i] = best
    return area, layer, dist
