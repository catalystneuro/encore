"""Human iEEG coding dimension, timescale and phase locking (DANDI:001347).

Reimplements, without importing it, the analysis of the paper's code (Zenodo
10.5281/zenodo.14920570, commit b873ca5): human_ieeg/scripts/analyze_airpuff_ieeg_cd.py,
ketman/analyze/trace_utils.py (load_raw_traces, reference, load_patients_erp,
get_erp_cd, compute_cd_cov, compute_all_cd, get_cd_timescales, extract_timescale),
ketman/analyze/cd_utils.py (plot_cd_projection_summary, plot_cd_weights, cd_pctile)
and ketman/analyze/airpuff_utils.process_led. Function docstrings cite the function
followed. Data are streamed through dandi_io; nothing is written to disk.

Where each parameter comes from
- Participants (PARTICIPANTS): the claims file header (the 7 included participants).
- Session used as "preinfusion" (PRE_SESSION_CODE): ketman/DATASETS.py, airpuff_sessions
  (SD168 and SD172 list 'baseline' first, lines 29 and 48); load_and_organize_raw_traces and
  load_patients_erp rename 'baseline' to 'preinfusion', which for SD245 (sessions
  ['baseline', 'preinfusion', ...], line 140) overwrites the Preinfusion session with the
  Baseline one. SD245's behaviour file holds only 'baseline' events, consistent with this.
  PRE_SESSION_ALT uses the Preinfusion file for SD245 (a reading shown as a variant).
- Puff times: TTL on DC channel index 2 (named 'CCEP' in the file), threshold 10e3, closing
  of 32 samples, onsets at least 1 s apart, only the second half of the epoch, first 40
  (process_led and load_raw_traces; DATASETS airpuff_ttl_thresh = 10e3 for all 7).
- Trials used: which_trials of each participant's behaviour file (claims header H-EYE).
- Channels: bipolar re-reference between neighbouring contacts of a shank (electrode group;
  claims header and trace_utils.reference). Pairs whose contacts include a location label
  'OUT OF BRAIN', 'EXCLUDE' or 'EXCLUDE AREA' are dropped (load_pt_elec_locs drops these
  labels). Bad channels are not marked in the dataset; the code's list (utils.bad_ch) can
  be passed as `bad` (a variant). White matter (Open D): a pair is white matter when either
  contact's location is 'WM' (the code tests str.contains('WM') on the pair's joined label).
- Notch 60 Hz, Q = 20, forward and backward (Methods, iEEG preprocessing; the code uses
  Q = 30, which changes nothing at the bands used).
- Band power: 5th-order Butterworth band-pass, sosfiltfilt, |Hilbert|^2 (Methods, Coding
  Dimension; power_over_time.compute_power_over_time), z-scored over the 20-min epoch.
  Broadband is the z-scored LFP (code: convert_to_power_band None).
- Epochs: 2 s before to 2 s after each puff; each trial baseline-subtracted by its mean over
  the 2 s before the puff (load_patients_erp do_baseline_sub = True; a code detail the
  Methods do not state, shown with and without).
- Coding dimension: windows open intervals (-0.5, 0) and (0.5, 1.5) or (0.05, 0.10)
  (get_cd_window, get_erp_cd); weight (mean post - mean pre) / sqrt(var post + var pre),
  variance over trials with ddof 0, divided by the sum of absolute weights (compute_cd_cov).
- Projection normalisation (Open C): reading 'methods' z-scores within (-0.5, 1.5), subtracts
  the mean of (-0.5, 0) and averages the summary window on the recorded time axis; reading
  'code' z-scores within (-1.0, 1.5), subtracts the mean of (-1.0, 0) and evaluates the
  summary window on the axis shifted by origin_shift_s = 0.05 s.
- Timescale: power of the z-scored LFP (not z-scored again) projected on the weights,
  scipy.signal.correlate, normalised to the maximum of the fitted part, fit
  a*exp(-x/b)+c over 2.5 s, p0 = (1, 0.2, 0), maxfev 2000 (get_cd_timescales,
  extract_timescale). Open E: 10 min (the first 10 min of the epoch, code) or 8 min before
  the first puff (Methods); fit from lag one sample (code) or lag 0 (Methods).
- Phase locking: phase of the 5th-order Butterworth band-passed (sosfiltfilt) bipolar
  voltage via Hilbert; PLV = |mean(exp(i(phi_a - phi_b)))| in 5-s windows (Methods: "we used
  sliding 5-second windows to compute phase locking value"). The Methods do not give the
  stride. The main reading uses non-overlapping windows (stride 5 s): the fig. S38 code
  describes its input as "5 sec w+s plv data" (analyze_airpuff_ieeg_top_cd_network.py,
  line 230), read here as window and stride of 5 s, and coh_over_time.roll_spec_sync steps
  windows by a stride argument. Strides of 2.5 s and 1 s (STRIDES) are variants. Phase is
  computed only for the preinfusion and infusion sessions (the only ones the claims use).
- Fig. S38 band edges: BANDS (Table S3 bands, gamma 30 to 50 Hz) in the main reading; the
  fig. S38 code (analyze_airpuff_ieeg_top_cd_network.py, main(), lines 88 to 89) uses
  CODE_BANDS, (1, 4), (5, 8), (9, 12), (13, 30), (31, 70), (71, 95), as a variant, with
  weights, sites and PLV all computed in those bands.
- Fig. S38 sites (S38_SELECTIONS). 'int': top and bottom int(10 % of kept channels) of
  |weight| (cd_utils.cd_pctile); 'ceil': the same with ceil; 'rank_wm_kept': ranked with
  white matter kept (weights computed over all non-excluded channels), then white-matter
  sites removed from the two sets (Methods: "the top and bottom tenth percentile of sites per
  patient were classified ... and white matter contacts were excluded"; only for the
  white-matter-excluded reading). Weight source (S38_WEIGHTS): 'band', the persistent weights
  computed in the band of the PLV (fig. S38B legend: "for CDs computed using power in each
  spectral band"); 'beta', the beta persistent weights for every band (code comment, lines 231
  to 232: "version 24-06-07 uses beta CD weights 0.5-1.5 to sort top v bot CD electrodes").
  The code reads the edges from a precomputed file (top_v_bot_cd_plv_edges.h5), so its
  selection cannot be checked. An edge filter dropping pairs of bipolar channels on the same
  shank whose first contact numbers differ by at most 1 (plot_utils, to_mask_adj_contacts,
  used there for a heatmap) is a further variant.
"""
import ast
import hashlib
import io
import zipfile

import numpy as np
import pandas as pd
import requests
import scipy.signal as ss
import scipy.stats as st
from scipy.ndimage import binary_closing

import dandi_io

FS = 200
PARTICIPANTS = ["SD168", "SD172", "SD181", "SD185", "SD186", "SD211", "SD245"]
CONDITIONS = ["preinfusion", "infusion", "postinfusion"]
PRE_SESSION_CODE = {"SD168": "Baseline", "SD172": "Baseline", "SD181": "Preinfusion",
                    "SD185": "Preinfusion", "SD186": "Preinfusion", "SD211": "Preinfusion",
                    "SD245": "Baseline"}
PRE_SESSION_ALT = dict(PRE_SESSION_CODE, SD245="Preinfusion")
BEHAVIOUR_PRE = {"Baseline": "baseline", "Preinfusion": "preinfusion"}
BANDS = {"delta": (1, 4), "theta": (4, 8), "alpha": (8, 12), "beta": (12, 30),
         "low gamma": (30, 50), "high gamma": (65, 95), "broadband": None}
PLV_BANDS = {k: v for k, v in BANDS.items() if v is not None}
CODE_BANDS = {"delta": (1, 4), "theta": (5, 8), "alpha": (9, 12), "beta": (13, 30),
              "gamma": (31, 70), "high gamma": (71, 95)}
STRIDES = (5.0, 2.5, 1.0)
S38_SELECTIONS = ("int", "ceil", "rank_wm_kept")
S38_WEIGHTS = ("band", "beta")
EXCLUDE_LOCATIONS = {"OUT OF BRAIN", "EXCLUDE", "EXCLUDE AREA"}
WINDOWS = {"persistent": (0.5, 1.5), "fast": (0.05, 0.10)}
PRE_WINDOW = (-0.5, 0.0)
EPOCH_S = 2.0
TT = np.arange(int(2 * EPOCH_S * FS)) / FS - EPOCH_S

CODE_URL = ("https://zenodo.org/api/records/14920570/files/"
            "kauvar-richman-liu-2025_zenodo.zip/content")
CODE_MD5 = "bd1fb567121aaf0291337783df57bcfc"
CODE_ROOT = "kauvar-richman-liu-2025_zenodo/"


def fetch_code_zip():
    """Fetch the paper's code record from Zenodo into memory and check its md5."""
    r = requests.get(CODE_URL, timeout=300)
    r.raise_for_status()
    md5 = hashlib.md5(r.content).hexdigest()
    if md5 != CODE_MD5:
        raise ValueError(f"md5 {md5} differs from {CODE_MD5}")
    return zipfile.ZipFile(io.BytesIO(r.content))


def code_bad_channels(zf):
    """utils.bad_ch of the code record (ketman/analyze/utils.py), parsed, not imported."""
    src = zf.read(CODE_ROOT + "ketman/analyze/utils.py").decode()
    for node in ast.parse(src).body:
        if isinstance(node, ast.Assign) and getattr(node.targets[0], "id", "") == "bad_ch":
            return ast.literal_eval(node.value)
    raise KeyError("bad_ch not found")


def code_channel_labels(zf):
    """anat/pts_ch_labels.pkl of the code record: per participant, bipolar channel names
    with their region and Yeo7 labels, and monopolar names with region labels."""
    import pickle
    return pickle.loads(zf.read(CODE_ROOT + "anat/pts_ch_labels.pkl"))


def _s(x):
    return x.decode() if isinstance(x, bytes) else str(x)


def detect_puffs(ttl, thresh=10e3, fps=FS):
    """Puff onsets from the TTL trace (airpuff_utils.process_led, just_second_half=True)."""
    b = (ttl > thresh).astype(float)
    b = binary_closing(b, structure=np.ones(32)).astype(float)
    bd = np.diff(b, prepend=b[0])
    on = ss.find_peaks(bd, height=0.99, distance=fps)[0]
    on = on[on >= len(ttl) / 2 - 1 - 100]
    return on[:40]


def read_behaviour(pt):
    """which_trials, puff onsets (video frames) and per-trial affective eye closure."""
    f = dandi_io.open_h5(f"sub-{pt}/sub-{pt}_ses-puff_behavior.nwb")
    acq = f["acquisition"]
    out = {"which_trials": acq["which_trials/data"][:].astype(int), "events": {},
           "affective": {}, "affective_normed": {}}
    for k in acq:
        if k.startswith("events-") and k.endswith("-on"):
            out["events"][k.split("-")[1].replace("_puffeye", "")] = acq[k]["data"][:]
        elif k.startswith("affective-"):
            out["affective"][k.split("-")[1].replace("_puffeye", "")] = acq[k]["data"][:]
        elif k.startswith("affective_normed-"):
            out["affective_normed"][k.split("-")[1].replace("_puffeye", "")] = acq[k]["data"][:]
    return out


def notch(x, f0=60.0, q=20.0):
    b, a = ss.iirnotch(f0, q, FS)
    return ss.filtfilt(b, a, x, axis=0)


def bandpass(x, lo, hi):
    """5th-order Butterworth band-pass, sosfiltfilt along time (trace_utils.bandpass)."""
    sos = ss.butter(5, [lo / (FS / 2), hi / (FS / 2)], btype="bandpass", output="sos")
    return ss.sosfiltfilt(sos, x, axis=0)


def band_power(x, band):
    if band is None:
        return x
    return np.abs(ss.hilbert(bandpass(x, *band), axis=0)) ** 2


def load_session(pt, ses):
    """Stream one session: bipolar within-shank LFP after notch, channel table, puffs.

    Returns dict with 'lfp' (time x pairs, float64), 'pairs' DataFrame (name, contacts,
    locations, white matter, excluded), 'puffs' (sample indices), 'n_ttl' (all onsets in
    the second half), 'raw_range' (1st and 99th percentile of the monopolar data)."""
    f = dandi_io.open_h5(f"sub-{pt}/sub-{pt}_ses-puff{ses}_ecephys.nwb")
    e = f["general/extracellular_ephys/electrodes"]
    lab = [_s(x) for x in e["label"][:]]
    loc = [_s(x) for x in e["location"][:]]
    grp = [_s(x) for x in e["group_name"][:]]
    data = f["processing/ecephys/LFP/v_trace/data"][:]
    ttl = f["acquisition/dc_trace/data"][:, 2]
    dc_name = _s(f["acquisition/dc_channels/channel_name"][2])
    rate = float(f["processing/ecephys/LFP/v_trace/starting_time"].attrs["rate"])
    assert rate == FS
    rows, idx = [], []
    for i in range(len(lab) - 1):
        if grp[i] != grp[i + 1]:
            continue
        rows.append({"name": f"{lab[i]}-{lab[i + 1]}", "a": lab[i], "b": lab[i + 1],
                     "loc_a": loc[i], "loc_b": loc[i + 1], "shank": grp[i],
                     "wm": "WM" in (loc[i], loc[i + 1]),
                     "excluded": bool({loc[i], loc[i + 1]} & EXCLUDE_LOCATIONS)})
        idx.append(i)
    idx = np.array(idx)
    lfp = data[:, idx] - data[:, idx + 1]
    raw_range = np.percentile(data[::50], [1, 99])
    del data
    lfp = notch(lfp)
    on_all = detect_puffs(ttl)
    return {"lfp": lfp, "pairs": pd.DataFrame(rows), "puffs": on_all, "dc_name": dc_name,
            "n_mono": len(lab), "raw_range": raw_range, "ttl": ttl}


def channel_mask(pairs, pt, wm_excluded, bad=None):
    """Pairs kept: not out of brain or excluded, optionally not white matter (Open D) and
    not containing a contact of the code's bad-channel list (exclude_bad_ch_from_raw)."""
    keep = ~pairs["excluded"].values
    if wm_excluded:
        keep &= ~pairs["wm"].values
    if bad is not None:
        badset = set(bad.get(pt, []))
        keep &= ~(pairs["a"].isin(badset) | pairs["b"].isin(badset)).values
    return keep


def epochs(x, puffs, trials):
    """(channels, time, trials) epochs of 2 s before to 2 s after each puff
    (get_puff_trace_matrix), for the trial indices `trials` of the 40 detected puffs."""
    n = int(EPOCH_S * FS)
    return np.stack([x[puffs[t] - n:puffs[t] + n].T for t in trials], axis=2)


def _win(tt, w):
    return (tt > w[0]) & (tt < w[1])


def cd_weights(ep, target, base_sub=True):
    """Coding dimension weights (get_erp_cd, compute_cd_cov)."""
    if base_sub:
        ep = ep - ep[:, :int(EPOCH_S * FS)].mean(1, keepdims=True)
    pre = ep[:, _win(TT, PRE_WINDOW)].mean(1)
    post = ep[:, _win(TT, target)].mean(1)
    v = (post.mean(1) - pre.mean(1)) / np.sqrt(post.var(1) + pre.var(1))
    return v / np.sum(np.abs(v))


def erp(ep, base_sub=True):
    if base_sub:
        ep = ep - ep[:, :int(EPOCH_S * FS)].mean(1, keepdims=True)
    return ep.mean(2)


def normalise_projection(proj, reading):
    """Open C: z-score and baseline-subtract a projection (compute_all_cd)."""
    if reading == "code":
        zwin, bwin = (-1.0, 1.5), (-1.0, 0.0)
    else:
        zwin, bwin = (-0.5, 1.5), (-0.5, 0.0)
    z = (proj - proj[_win(TT, zwin)].mean()) / proj[_win(TT, zwin)].std()
    return z - z[_win(TT, bwin)].mean()


def summary_value(projz, window, reading):
    """Mean over the summary window; 'code' evaluates it on tt - 0.05 s (origin_shift_s)."""
    tt = TT - 0.05 if reading == "code" else TT
    return projz[_win(tt, window)].mean()


def paired_tests(pre, ket, post):
    """Paired t-tests pre vs ketamine and post vs ketamine, BH over the two
    (plot_cd_projection_summary)."""
    from statsmodels.stats.multitest import multipletests
    t1, p1 = st.ttest_rel(pre, ket)
    t2, p2 = st.ttest_rel(post, ket)
    pc = multipletests([p1, p2], method="fdr_bh")[1]
    return {"t_pre_ket": t1, "p_pre_ket": p1, "pcorr_pre_ket": pc[0],
            "t_post_ket": t2, "p_post_ket": p2, "pcorr_post_ket": pc[1]}


def extract_timescale(signal, fit_time=2.5, t0=0.2, start_lag=1):
    """extract_timescale: autocorrelation (scipy.signal.correlate), normalised to the max of
    the fitted part, fit a*exp(-x/b)+c; start_lag 1 is the code, 0 the Methods' peak."""
    from scipy.optimize import curve_fit
    full = ss.correlate(signal, signal, method="fft")
    zero = len(signal) - 1
    sig = full[zero + start_lag:][:int(fit_time * FS)].copy()
    sig /= sig.max()
    tt = np.arange(len(sig)) / FS
    popt, _ = curve_fit(lambda x, a, b, c: a * np.exp(-x / b) + c, tt, sig,
                        p0=[1, t0, 0], maxfev=2000)
    return popt[1]


def plv_windows(phase_a, phase_b, win_s=5.0, stride_s=None):
    """PLV in 5-s windows starting every stride_s seconds (default: non-overlapping) that fit
    in the segment; phase arrays (time, n) -> (windows, n). Window sums by cumulative sum."""
    n = int(win_s * FS)
    step = n if stride_s is None else int(round(stride_s * FS))
    d = np.exp(1j * (phase_a - phase_b).astype(np.float64))
    cs = np.concatenate([np.zeros((1, d.shape[1]), complex), np.cumsum(d, axis=0)])
    starts = np.arange(0, d.shape[0] - n + 1, step)
    return np.abs(cs[starts + n] - cs[starts]) / n


def edge_plv(phase, sites, win_s=5.0, stride_s=None):
    """Per edge among `sites` (indices into phase columns): PLV per window (windows, edges)."""
    sites = np.asarray(sites)
    ia, ib = np.triu_indices(len(sites), 1)
    return plv_windows(phase[:, sites[ia]], phase[:, sites[ib]], win_s, stride_s)


def top_bottom(w, pct=10, rounding="int"):
    """Indices of the top and bottom pct % of |w| (cd_utils.cd_pctile uses int; 'ceil' is a
    variant)."""
    order = np.argsort(np.abs(w))
    x = pct / 100.0 * len(w)
    k = int(np.ceil(x)) if rounding == "ceil" else int(x)
    return order[-k:], order[:k]


def s38_sites(weights, masks, pairs, key, wm, bad, sel):
    """High and low sites for fig. S38 as indices into `pairs` (see the module docstring for
    the readings). key is the (band key, window) of the weights."""
    if sel == "rank_wm_kept":
        if not wm:
            return None
        m = masks[(False, bad)]
        top, bot = top_bottom(weights[key + (False, bad, True)])
        g = np.where(m)[0]
        keep = ~pairs["wm"].values
        return g[top][keep[g[top]]], g[bot][keep[g[bot]]]
    g = np.where(masks[(wm, bad)])[0]
    top, bot = top_bottom(weights[key + (wm, bad, True)], rounding=sel)
    return g[top], g[bot]


def edge_stats(z, sites):
    """Per edge among `sites`: for each stride in STRIDES, mean and SD (ddof 0) of the PLVs of
    5-s windows (as plv_windows, computed from 0.5-s block sums); z is exp(i phase) of the
    sites, (time, len(sites)). Also returns the sites and the two sites of each edge."""
    sites = np.asarray(sites)
    ia, ib = np.triu_indices(len(sites), 1)
    out = {"edges": (sites[ia], sites[ib]), "sites": sites}
    blk = FS // 2
    nb = z.shape[0] // blk
    d = (z[:nb * blk, ia] * z[:nb * blk, ib].conj()).reshape(nb, blk, len(ia))
    cs = np.concatenate([np.zeros((1, len(ia)), complex), np.cumsum(d.sum(1, dtype=complex), 0)])
    for s in STRIDES:
        starts = np.arange(0, nb - 10 + 1, int(round(s * 2)))
        p = np.abs(cs[starts + 10] - cs[starts]) / (10 * blk)
        out[s] = (p.mean(0), p.std(0))
    return out


def adjacent(pairs, ia, ib):
    """True for edges whose bipolar channels are on the same shank with first contact numbers
    differing by at most 1 (plot_utils, to_mask_adj_contacts)."""
    import re
    shank = np.array([re.findall("[A-Za-z]+", a)[0] for a in pairs["a"]])
    num = np.array([int(re.findall("[0-9]+", a)[0]) for a in pairs["a"]])
    return (shank[ia] == shank[ib]) & (np.abs(num[ia] - num[ib]) <= 1)


def process_participant(pt, pre_ses, bad_code, beh, seed=0, light=False):
    """Everything the block needs from one participant, reduced as it loads.

    Weights are computed for every band x window x white matter (Open D) x bad-channel list
    ('none' or 'code') x per-trial baseline subtraction. Returns a dict of reduced results;
    keys are explained inline. light=True processes only the preinfusion session and keeps
    only the weights and ERPs (used for a variant session mapping)."""
    rng = np.random.default_rng(seed)
    sessions = {"preinfusion": pre_ses, "infusion": "Infusion", "postinfusion": "Postinfusion"}
    trials = beh["which_trials"]
    out = {"pt": pt, "pre_ses": pre_ses, "sessions": {}, "weights": {}, "erp": {},
           "ts_proj": {}, "plv6i": {}, "s38": {}, "s38h": {}, "clock": {}}
    badsets = {"none": None, "code": bad_code}
    loaded = {}
    if light:
        sessions = {"preinfusion": pre_ses}
    for cond, ses in sessions.items():
        s = load_session(pt, ses)
        pairs = s["pairs"]
        out["sessions"][cond] = {"file_session": ses, "n_mono": s["n_mono"],
                                 "n_pairs": len(pairs), "puffs": s["puffs"],
                                 "dc_name": s["dc_name"], "raw_range": s["raw_range"],
                                 "lfp_sd": np.median(s["lfp"].std(0))}
        if cond == "preinfusion":
            out["pairs"] = pairs
            masks = {(wm, b): channel_mask(pairs, pt, wm, badsets[b])
                     for wm in (True, False) for b in ("none", "code")}
            out["masks"] = masks
        else:
            assert list(pairs["name"]) == list(out["pairs"]["name"])
        puffs = s["puffs"]
        lfp = s["lfp"]
        dz = st.zscore(lfp, axis=0)
        # band power epochs
        for band, rng_hz in BANDS.items():
            pz = st.zscore(band_power(lfp, rng_hz), axis=0).astype(np.float32)
            ep = epochs(pz, puffs, trials)
            for bs in (True, False):
                out["erp"][(cond, band, bs)] = erp(ep, bs)
            if cond == "preinfusion":
                for (wm, b), m in masks.items():
                    for wname, wwin in WINDOWS.items():
                        for bs in (True, False):
                            out["weights"][(band, wname, wm, b, bs)] = cd_weights(ep[m], wwin, bs)
            if band == "beta":
                # single-trial projections on persistent beta weights (fig. S38H)
                tp = {}
                for (wm, b), m in masks.items():
                    w = out["weights"][("beta", "persistent", wm, b, True)]
                    tp[(wm, b)] = np.einsum("c,ctk->kt", w, ep[m])
                out["s38h"][(cond, "trial_proj")] = tp
            if band in ("beta", "broadband") and cond == "preinfusion":
                # clock check: puff-locked change (mean over the response window minus the
                # 0.5 s before), averaged over trials, |.| averaged over channels, at the TTL
                # times, at 20 sets of 40 random times before the assay, and at shifted times
                resp = (0.05, 1.5) if band == "beta" else (0.05, 0.5)

                def evoked(e):
                    d = e[:, _win(TT, resp)].mean(1) - e[:, _win(TT, PRE_WINDOW)].mean(1)
                    return np.abs(d.mean(1)).mean()
                null = [evoked(epochs(pz, np.sort(rng.integers(500, puffs[0] - 500, size=40)),
                                      trials)) for _ in range(20)]
                shifted = [evoked(epochs(pz, puffs + int(sh * FS), trials)) for sh in (-2.5, 2.5)]
                out["clock"][band] = {"true": evoked(ep), "null": np.array(null),
                                      "shift": shifted, "window": resp}
            del pz, ep
        if cond == "preinfusion" and not light:
            # persistent weights in the fig. S38 code's band edges (delta is the same band)
            for band, rng_hz in CODE_BANDS.items():
                if rng_hz == BANDS.get(band):
                    for (wm, b) in masks:
                        out["weights"][(("code", band), "persistent", wm, b, True)] = \
                            out["weights"][(band, "persistent", wm, b, True)]
                    continue
                pz = st.zscore(band_power(lfp, rng_hz), axis=0).astype(np.float32)
                ep = epochs(pz, puffs, trials)
                for (wm, b), m in masks.items():
                    out["weights"][(("code", band), "persistent", wm, b, True)] = \
                        cd_weights(ep[m], WINDOWS["persistent"], True)
                del pz, ep
        if light:
            continue
        # timescale traces: beta power of the z-scored LFP projected on persistent weights
        bp = band_power(dz, BANDS["beta"])
        for (wm, b), m in out["masks"].items():
            w = out["weights"][("beta", "persistent", wm, b, True)]
            out["ts_proj"][(cond, wm, b)] = (bp[:, m] @ w).astype(np.float64)
        del bp
        # phase for PLV in the 10 min before the first puff (preinfusion and infusion only)
        seg = slice(max(puffs[0] - 10 * 60 * FS, 0), puffs[0])
        pre_part = lfp[:puffs[0] + 2 * FS]
        base = np.where(out["masks"][(False, "none")])[0]
        pairs0 = out["pairs"]
        for bset, bands in (("main", PLV_BANDS), ("code", CODE_BANDS)):
            if cond == "postinfusion":
                break
            for band, rng_hz in bands.items():
                bkey = band if bset == "main" else ("code", band)
                ph_all = np.angle(ss.hilbert(bandpass(pre_part[:, base], *rng_hz),
                                             axis=0))[seg]
                z_all = np.exp(1j * ph_all).astype(np.complex64)
                for (wm, b) in out["masks"]:
                    for wsrc in S38_WEIGHTS:
                        if wsrc == "beta" and bkey == "beta":
                            continue      # the same sets as wsrc 'band'
                        wkey = (bkey if wsrc == "band" else "beta", "persistent")
                        for sel in S38_SELECTIONS:
                            sites = s38_sites(out["weights"], out["masks"], pairs0, wkey, wm, b, sel)
                            if sites is None:
                                continue
                            for hl, ss_ in zip(("high", "low"), sites):
                                out["s38"][(cond, bset, band, wm, b, wsrc, sel, hl)] = \
                                    edge_stats(z_all[:, np.searchsorted(base, ss_)], ss_)
                    if bset == "main" and band == "beta":
                        # fig 6I: persistent sites (top 10 % of |beta persistent weight|)
                        top, _ = s38_sites(out["weights"], out["masks"], pairs0,
                                           ("beta", "persistent"), wm, b, "int")
                        ph = ph_all[:, np.searchsorted(base, top)]
                        out["plv6i"][(cond, wm, b)] = {
                            st_: edge_plv(ph, np.arange(len(top)), 5.0, st_) for st_ in STRIDES}
                del ph_all, z_all
        phases = {"beta": np.angle(ss.hilbert(bandpass(lfp, *BANDS["beta"]), axis=0)).astype(np.float32)}
        # fig S38H: per-trial pre-puff beta PLV over all edges between kept channels
        n = int(0.5 * FS)
        for (wm, b), m in out["masks"].items():
            ph = phases["beta"][:, m]
            vals = []
            for t in trials:
                z = np.exp(1j * ph[puffs[t] - n:puffs[t]])
                c = np.abs(z.conj().T @ z) / n
                iu = np.triu_indices(c.shape[0], 1)
                vals.append(c[iu].mean())
            out["s38h"][(cond, "plv", wm, b)] = np.array(vals)
        del phases, lfp, dz, s
    return out


def _job(args):
    import os
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    pt, pre_ses, bad, light = args
    beh = read_behaviour(pt)
    return process_participant(pt, pre_ses, bad, beh, light=light), beh


def run_all(bad, max_workers=3):
    """Process the 7 participants (code session mapping) and SD245 with its Preinfusion
    file as preinfusion (light), in parallel processes. Returns (results, alt, behaviour)."""
    from concurrent.futures import ProcessPoolExecutor
    jobs = [(pt, PRE_SESSION_CODE[pt], bad, False) for pt in PARTICIPANTS]
    jobs.append(("SD245", PRE_SESSION_ALT["SD245"], bad, True))
    with ProcessPoolExecutor(max_workers=max_workers) as ex:
        res = list(ex.map(_job, jobs))
    results = {pt: r for (pt, _, _, light), (r, _) in zip(jobs, res) if not light}
    alt = res[-1][0]
    beh = {pt: b for (pt, _, _, light), (_, b) in zip(jobs, res) if not light}
    return results, alt, beh


def cd_summary(res, alt, band, window, wm, bad, bs, reading, sd245="code", traces=False):
    """Per-participant summary values (or normalised projections) for each condition.

    sd245 'code' takes SD245's Baseline file as preinfusion (the code's behaviour), 'alt' its
    Preinfusion file (weights and preinfusion ERP from `alt`)."""
    vals = {c: [] for c in CONDITIONS}
    for pt in PARTICIPANTS:
        r = res[pt]
        wsrc = alt if (pt == "SD245" and sd245 == "alt") else r
        w = wsrc["weights"][(band, window, wm, bad, bs)]
        m = wsrc["masks"][(wm, bad)]
        for c in CONDITIONS:
            src = wsrc if c == "preinfusion" else r
            pz = normalise_projection(w @ src["erp"][(c, band, bs)][m], reading)
            vals[c].append(pz if traces else summary_value(pz, WINDOWS[window], reading))
    return {c: np.array(v) for c, v in vals.items()}


def readings_table(res, alt, band, window, bads=("none", "code"), sd245s=("code", "alt"),
                   bsubs=(True, False)):
    """Every combination of Open C, Open D, bad-channel list, SD245 session and per-trial
    baseline subtraction, with the paired tests."""
    import itertools
    rows = []
    for rd, wm, bad, bs, sd in itertools.product(("methods", "code"), (True, False), bads,
                                                 bsubs, sd245s):
        v = cd_summary(res, alt, band, window, wm, bad, bs, rd, sd)
        t = paired_tests(v["preinfusion"], v["infusion"], v["postinfusion"])
        rows.append(dict(open_c=rd, wm_excluded=wm, bad_list=bad, trial_baseline=bs,
                         sd245_pre=sd, pre=v["preinfusion"].mean(), ket=v["infusion"].mean(),
                         post=v["postinfusion"].mean(), **t))
    return pd.DataFrame(rows)


def extra_session(r, ses):
    """For participant result r, load another session file and compute, with r's weights,
    the timescale projections and the fig. 6I persistent-site PLV (as process_participant).
    Used for SD245, whose code takes the Baseline file for the coding dimension and the
    Preinfusion file for the timescale (load_raw_traces_and_merge_to_anat)."""
    s = load_session(r["pt"], ses)
    assert list(s["pairs"]["name"]) == list(r["pairs"]["name"])
    lfp, puffs = s["lfp"], s["puffs"]
    bp = band_power(st.zscore(lfp, axis=0), BANDS["beta"])
    out = {"ts_proj": {}, "plv6i": {}, "puffs": puffs}
    seg = slice(max(puffs[0] - 10 * 60 * FS, 0), puffs[0])
    for (wm, b), m in r["masks"].items():
        w = r["weights"][("beta", "persistent", wm, b, True)]
        out["ts_proj"][(wm, b)] = bp[:, m] @ w
        top, _ = top_bottom(w)
        idx = np.where(m)[0][top]
        ph = np.angle(ss.hilbert(bandpass(lfp[:puffs[0] + 2 * FS, idx], *BANDS["beta"]),
                                 axis=0))[seg]
        out["plv6i"][(wm, b)] = {s: edge_plv(ph, np.arange(len(idx)), 5.0, s) for s in STRIDES}
    return out


# ---------------------------------------------------------------------------------------------
# Across-participant summaries

def timescales(res, ex, wm, bad, period, start_lag, sd245_pre="Preinfusion"):
    """Per-participant timescales (s) for preinfusion and infusion (get_cd_timescales).

    period '10min': the first 10 min of the epoch (code); '8min': the 8 min before the first
    puff (Methods). sd245_pre 'Preinfusion' uses SD245's Preinfusion file (the code's timescale
    path), 'Baseline' its Baseline file (the file its coding dimension uses)."""
    out = {"preinfusion": [], "infusion": []}
    for pt in PARTICIPANTS:
        r = res[pt]
        for c in out:
            x, p0 = r["ts_proj"][(c, wm, bad)], r["sessions"][c]["puffs"][0]
            if pt == "SD245" and c == "preinfusion" and sd245_pre == "Preinfusion":
                x, p0 = ex["ts_proj"][(wm, bad)], ex["puffs"][0]
            seg = x[:10 * 60 * FS] if period == "10min" else x[p0 - 8 * 60 * FS:p0]
            out[c].append(extract_timescale(np.asarray(seg, float), start_lag=start_lag))
    return {c: np.array(v) for c, v in out.items()}


def plv_ratio(res, ex, wm, bad, sd245_pre="Baseline", stride=5.0):
    """Fig. 6I: mean beta PLV over 5-s windows (starting every `stride` s) and persistent
    edges, ketamine / preinfusion, per participant; also the per-edge z-scored change
    (Methods), averaged over edges."""
    ratio, z, pre, ket = [], [], [], []
    for pt in PARTICIPANTS:
        P = res[pt]["plv6i"][("preinfusion", wm, bad)][stride]
        if pt == "SD245" and sd245_pre == "Preinfusion":
            P = ex["plv6i"][(wm, bad)][stride]
        K = res[pt]["plv6i"][("infusion", wm, bad)][stride]
        ratio.append(K.mean() / P.mean())
        pre.append(P.mean())
        ket.append(K.mean())
        z.append(((K.mean(0) - P.mean(0)) / P.std(0)).mean())
    return {"ratio": np.array(ratio), "z": np.array(z), "pre": np.array(pre),
            "ket": np.array(ket), "n_windows": [res[pt]["plv6i"][("infusion", wm, bad)][stride].shape[0]
                                                for pt in PARTICIPANTS],
            "n_edges": [res[pt]["plv6i"][("preinfusion", wm, bad)][stride].shape[1]
                        for pt in PARTICIPANTS]}


def edge_table(res, band, wm, bad, bset="main", wsrc="band", sel="int", stride=5.0,
               drop_adjacent=False):
    """Fig. S38: one row per edge within the high or within the low set, with preinfusion PLV,
    ketamine PLV, their difference and the difference z-scored by the preinfusion window SD.
    bset 'main' (BANDS) or 'code' (CODE_BANDS); wsrc, sel: see the module docstring;
    drop_adjacent removes edges between neighbouring bipolar channels (`adjacent`)."""
    rows = []
    for pt in PARTICIPANTS:
        for hl in ("high", "low"):
            ws = "band" if (bset, band) == ("main", "beta") else wsrc   # identical sets
            key = (bset, band, wm, bad, ws, sel, hl)
            P, K = res[pt]["s38"][("preinfusion",) + key], res[pt]["s38"][("infusion",) + key]
            keep = np.ones(len(P["edges"][0]), bool)
            if drop_adjacent:
                keep = ~adjacent(res[pt]["pairs"], *P["edges"])
            pm, ps = P[stride]
            km, _ = K[stride]
            for e in np.where(keep)[0]:
                rows.append(dict(pt=pt, top_cd=(hl == "high"), sync_base=pm[e], sync_ket=km[e],
                                 sync_change=km[e] - pm[e], sync_change_z=(km[e] - pm[e]) / ps[e]))
    return pd.DataFrame(rows)


def s38_counts(res, wm, bad, sel, drop_adjacent=False, bset="main", band="beta", wsrc="band"):
    """Per participant, numbers of high and low sites and of edges within each set. For 'int'
    and 'ceil' they depend only on the channel count, not on the band or weights; for
    'rank_wm_kept' and with drop_adjacent they depend on which sites are selected."""
    out = {}
    for pt in PARTICIPANTS:
        d = {}
        for hl in ("high", "low"):
            ws = "band" if (bset, band) == ("main", "beta") else wsrc   # identical sets
            P = res[pt]["s38"][("preinfusion", bset, band, wm, bad, ws, sel, hl)]
            ia, ib = P["edges"]
            keep = ~adjacent(res[pt]["pairs"], ia, ib) if drop_adjacent else np.ones(len(ia), bool)
            d[f"{hl}_sites"] = len(P["sites"])
            d[f"{hl}_edges"] = int(keep.sum())
        out[pt] = d
    return pd.DataFrame(out).T


def mixed(df, formula, term):
    """Mixed-effects linear model with a random intercept per participant (statsmodels
    mixedlm, as in analyze_airpuff_ieeg_top_cd_network.plot_top_v_bot_cd_plv)."""
    import warnings
    import statsmodels.formula.api as smf
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        f = smf.mixedlm(formula, df, groups=df["pt"]).fit()
    ci = f.conf_int().loc[term]
    return {"coef": f.params[term], "ci_low": ci[0], "ci_high": ci[1], "p": f.pvalues[term],
            "n": len(df), "converged": bool(f.converged)}


def trial_persistence(tp, reading, trial_baseline=True, prepuff_sub=False):
    """Single-trial persistent projection averaged over the summary window (compute_all_cd,
    do_trial_projections): z-scored with the mean and SD over all trials of the z-scoring
    window; trial_baseline subtracts each trial's mean over the 2 s before the puff (the
    epochs the code projects are baseline-subtracted); prepuff_sub subtracts each trial's mean
    over 0.5 to 0 s before the puff (the Methods' baseline step; commented out in the code)."""
    tp = np.asarray(tp, float)
    if trial_baseline:
        tp = tp - tp[:, :int(EPOCH_S * FS)].mean(1, keepdims=True)
    zwin = (-1.0, 1.5) if reading == "code" else (-0.5, 1.5)
    z = (tp - tp[:, _win(TT, zwin)].mean()) / tp[:, _win(TT, zwin)].std()
    if prepuff_sub:
        z = z - z[:, _win(TT, PRE_WINDOW)].mean(1, keepdims=True)
    tt = TT - 0.05 if reading == "code" else TT
    return z[:, _win(tt, WINDOWS["persistent"])].mean(1)


def trial_table(res, beh, wm_plv, wm_cd, bad, reading, trial_baseline, prepuff_sub,
                closure="affective"):
    rows = []
    for pt in PARTICIPANTS:
        r, b = res[pt], beh[pt]
        for c in ("preinfusion", "infusion"):
            key = BEHAVIOUR_PRE[r["pre_ses"]] if c == "preinfusion" else "infusion"
            y = trial_persistence(r["s38h"][(c, "trial_proj")][(wm_cd, bad)], reading,
                                  trial_baseline, prepuff_sub)
            plv = r["s38h"][(c, "plv", wm_plv, bad)]
            eye = b[closure][key][b["which_trials"]]
            for i in range(len(y)):
                rows.append(dict(pt=pt, cond=c, persistence=y[i], plv=plv[i], eye=eye[i]))
    return pd.DataFrame(rows)


YEO7 = ["Default", "Dorsal Attention", "Frontoparietal", "Limbic", "Somatomotor",
        "Ventral Attention"]


def yeo_table(res, labels, window, wm, bad):
    """Fig. S35: |weight| / participant max per bipolar channel with its Yeo7 label from the
    code record (pt_elec_yeos_bipo, matched by participant and pair name)."""
    rows = []
    for pt in PARTICIPANTS:
        r = res[pt]
        m = r["masks"][(wm, bad)]
        w = np.abs(r["weights"][("beta", window, wm, bad, True)])
        lab = dict(zip(labels["pt_elec_names_bipo"][pt], labels["pt_elec_yeos_bipo"][pt]))
        for n, x in zip(r["pairs"]["name"].values[m], w / w.max()):
            rows.append(dict(pt=pt, name=n, yeo7=str(lab.get(n, "unmatched")), w=x))
    return pd.DataFrame(rows)


def yeo_shuffle(df, n_boot=1000, seed=1):
    """Median per network against 1000 shuffles of the labels across channels; two-sided
    percentile p, BH across networks (cd_utils.plot_cd_weights, pval_from_boot)."""
    from statsmodels.stats.multitest import multipletests
    rng = np.random.default_rng(seed)
    stat = {k: np.median(df.w[df.yeo7 == k]) for k in YEO7}
    boots = {k: np.empty(n_boot) for k in YEO7}
    lab, w = df.yeo7.values, df.w.values
    for i in range(n_boot):
        sh = rng.permutation(lab)
        for k in YEO7:
            boots[k][i] = np.median(w[sh == k])
    p = [2 * min(np.mean(boots[k] >= stat[k]), np.mean(boots[k] <= stat[k])) for k in YEO7]
    pc = multipletests(p, method="fdr_bh")[1]
    return pd.DataFrame({"network": YEO7, "n": [(df.yeo7 == k).sum() for k in YEO7],
                         "median": [stat[k] for k in YEO7],
                         "mean": [df.w[df.yeo7 == k].mean() for k in YEO7],
                         "sem": [st.sem(df.w[df.yeo7 == k]) for k in YEO7],
                         "shuffle_2.5": [np.percentile(boots[k], 2.5) for k in YEO7],
                         "shuffle_97.5": [np.percentile(boots[k], 97.5) for k in YEO7],
                         "p": p, "p_bh": pc})


def s38_models(res, bset, wm, bad, wsrc="band", sel="int", stride=5.0, drop_adjacent=False,
               outcomes=("sync_base", "sync_change", "sync_change_z")):
    """Fig. S38 mixed models per band (analyze_airpuff_ieeg_top_cd_network.plot_top_v_bot_cd_plv):
    outcome ~ top_cd, random intercept per participant, BH (fdrcorrection, 'indep') over the
    six bands and Bonferroni (the code's 'pval_bonf')."""
    from statsmodels.stats.multitest import multipletests
    bands = PLV_BANDS if bset == "main" else CODE_BANDS
    tabs = {band: edge_table(res, band, wm, bad, bset, wsrc, sel, stride, drop_adjacent)
            for band in bands}
    rows = []
    for y in outcomes:
        g = pd.DataFrame([dict(outcome=y, band=band, **mixed(tabs[band], f"{y} ~ top_cd",
                                                               "top_cd[T.True]"))
                          for band in bands])
        g["p_bh"] = multipletests(g.p, method="fdr_bh")[1]
        g["p_bonf"] = np.minimum(g.p * len(bands), 1)
        rows.append(g)
    out = pd.concat(rows, ignore_index=True)
    for k, v in dict(bands=bset, wm_excluded=wm, bad_list=bad, weights=wsrc, sites=sel,
                     stride_s=stride, drop_adjacent=drop_adjacent).items().__reversed__():
        out.insert(0, k, v)
    return out
