"""Loading and measures for DANDI:001687 (Xiao, Severson et al. 2026, Neuron).

Streams the processed NWB files ("...sp-session-N.nwb") of the pinned version
and reduces each unit to per-pass spike counts in the windows the analyses use.

Where each parameter comes from:
- Wall window 3 to 11 s and baseline -4.5 to 0 s after wall-movement onset:
  claims file opening comment (Methods, Wall Distance Tuning Curve Calculation).
- Nine 2-mm distance bins with edges 6, 8, ..., 24 mm; passes outside are
  dropped: claims file opening comment (same Methods passage; the deposit's
  distance_axis description gives the same edges).
- Onset 2.5-4.5 s, sustained 4.5-9.5 s, offset 9.5-11.5 s: claims file
  (Methods, Characterizing Wall Distance Tuning).
- Low-firing rule (largest per-distance mean wall rate and mean baseline rate
  both below 1 Hz): claims file opening comment (Fig2DEF_Pop_Heatmap_Hist_Pie.m).
- Responsiveness: one-tailed signed-rank of each pass's wall rate against its
  own baseline, per distance, with BH-FDR over the nine distances per
  direction, q < 0.05 (code, main reading), or p < 0.05 uncorrected (variant):
  claims file, as amended after questions/001687.yaml.
- Tuning: two-tailed signed-rank over all 36 distance pairs, BH-FDR, any
  q < 0.05; the k-th pass at one distance paired with the k-th at the other
  (claims file; code). Where distance bins hold unequal numbers of passes,
  each bin is truncated to the smallest count across bins, in time order. The
  paper does not state this; the code truncates the two sessions it names
  (20221213_sp_session_2 to 17 and 20230131_sp_session_2 to 19 repetitions,
  Fig2DEF_Pop_Heatmap_Hist_Pie.m), and MATLAB's paired signrank needs equal
  lengths. Taken from the code.
- Map test: one-tailed signed-rank of each farther bin against the closest,
  BH-FDR over the eight, any q < 0.05 (claims file; Methods; code).
- Signed-rank p-values follow MATLAB signrank: zero differences dropped, exact
  distribution for up to 15 non-zero pairs, else the normal approximation with
  continuity correction. A standard choice made to match the code's software.
- Decoders: see decode_mcc and single_neuron_decoder.
"""
import json
import concurrent.futures as cf

import h5py
import numpy as np
import remfile
import requests
from scipy import stats

DANDISET = "001687"
VERSION = "0.260821.2126"
API = "https://api.dandiarchive.org/api"

EDGES = np.arange(6, 25, 2)          # 2-mm bin edges, 6..24 mm
CENTERS = np.arange(7, 24, 2)        # 7, 9, ..., 23 mm
WINDOWS = {"wall": (3.0, 11.0), "base": (-4.5, 0.0), "onset": (2.5, 4.5),
           "sustained": (4.5, 9.5), "offset": (9.5, 11.5)}
DEC_BIN, DEC_STEP, DEC_T1 = 0.150, 0.050, 14.0   # population decoder binning
SN_BIN = 0.200                                    # single-neuron decoder bins


def list_assets():
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=1000"
    out = []
    while url:
        r = requests.get(url, timeout=60).json()
        out += r["results"]
        url = r.get("next")
    return out


def asset_url(asset_id):
    return f"{API}/assets/{asset_id}/download/"


def _s(x):
    return x.decode() if isinstance(x, bytes) else str(x)


def _ragged(g, name):
    data = g[name][:]
    idx = g[name + "_index"][:]
    starts = np.r_[0, idx[:-1]]
    return [data[a:b] for a, b in zip(starts, idx)]


def load_session(asset):
    """Read one processed file, reduced to what the analyses need."""
    f = h5py.File(remfile.File(asset_url(asset["asset_id"])), "r")
    t = f["intervals/trials"]
    start = t["start_time"][:]
    dist = t["wall_distance_mm"][:]
    cond = [_s(c) for c in t["trial_condition"][:]]
    u = f["units"]
    n = u["id"].shape[0]
    spikes = _ragged(u, "spike_times")
    incl = np.asarray(u["trial_include"][:]).reshape(n, -1).astype(bool)
    lab = dict(
        unit_label=[_s(x) for x in u["unit_label"][:]],
        tuning_type=[_s(x) for x in u["tuning_type"][:]],
        wall_responsive=u["wall_responsive"][:].astype(bool),
        wall_tuned=u["wall_tuned"][:].astype(bool),
        activated=u["activated"][:].astype(bool),
        suppressed=u["suppressed"][:].astype(bool),
        low_firing=u["low_firing"][:].astype(bool),
        pref_dist_mm=u["pref_dist_mm"][:],
    )
    tc = f["processing/wall_tuning/tuning_curves"]
    dep_fr = np.array(_ragged(tc, "fr_mean"), dtype=object)
    dep_base = tc["fr_base_mean"][:]
    ti = f["processing/trial_log/trial_info"]
    rep = ti["repetition_idx"][:]
    g = f["general"]
    sub = g["subject"]
    meta = dict(path=asset["path"], session_id=_s(g["session_id"][()]),
                subject=_s(sub["subject_id"][()]), strain=_s(sub["strain"][()]),
                sex=_s(sub["sex"][()]), session_description=_s(f["session_description"][()]),
                probe=_s(sub["description"][()]))
    f.close()
    return dict(meta=meta, start=start, dist=dist, cond=cond, rep=rep, spikes=spikes,
                incl=incl, labels=lab, dep_fr=dep_fr, dep_base=dep_base)


def load_all(assets, workers=12):
    proc = sorted([a for a in assets if a["path"].endswith(".nwb") and "_ecephys" not in a["path"]],
                  key=lambda a: a["path"])
    with cf.ThreadPoolExecutor(workers) as ex:
        return list(ex.map(load_session, proc))


def counts_in(spk, starts, t0, t1):
    """Spike counts of one unit in [start+t0, start+t1) for each pass."""
    a = np.searchsorted(spk, starts + t0)
    b = np.searchsorted(spk, starts + t1)
    return b - a


def binned_counts(spk, starts, t0, t1, width, step):
    """Counts in sliding windows [t0+k*step, t0+k*step+width) per pass: (passes, bins)."""
    lefts = np.arange(t0, t1 - width + 1e-9, step)
    edges_a = starts[:, None] + lefts[None, :]
    a = np.searchsorted(spk, edges_a)
    b = np.searchsorted(spk, edges_a + width)
    return (b - a), lefts


def dist_bin(d):
    """Index 0..8 of the 2-mm bin, or -1 outside 6-24 mm."""
    k = np.digitize(d, EDGES) - 1
    k[(d < EDGES[0]) | (d >= EDGES[-1])] = -1
    return k


def unit_table(sessions, pass_mask=None):
    """Per-unit per-pass rates. pass_mask(session) -> bool per trial, or None for all.

    Returns a list of dicts, one per unit, with per-bin lists of pass rates in
    time order for each window, and the unit's labels from the deposit."""
    units = []
    for s in sessions:
        dbin = dist_bin(s["dist"])
        m = dbin >= 0
        if pass_mask is not None:
            m &= pass_mask(s)
        n_bins = len(np.unique(dbin[m]))
        for i, spk in enumerate(s["spikes"]):
            mi = m & s["incl"][i]
            rates = {}
            for w, (t0, t1) in WINDOWS.items():
                c = counts_in(spk, s["start"], t0, t1) / (t1 - t0)
                rates[w] = [c[mi & (dbin == k)] for k in range(9)]
            u = dict(session=s["meta"]["session_id"], subject=s["meta"]["subject"],
                     path=s["meta"]["path"], idx=i, n_bins=n_bins, rates=rates,
                     starts=[s["start"][mi & (dbin == k)] for k in range(9)])
            for k, v in s["labels"].items():
                u[k] = v[i]
            units.append(u)
    return units


# ---------- statistics ----------

def signrank(x, y, alternative="two-sided"):
    """MATLAB-style signrank p-value (see module docstring)."""
    d = np.asarray(x, float) - np.asarray(y, float)
    d = d[d != 0]
    n = d.size
    if n == 0:
        return 1.0
    method = "exact" if n <= 15 else "approx"
    return float(stats.wilcoxon(d, alternative=alternative, method=method,
                                correction=(method == "approx"), zero_method="wilcox").pvalue)


def bh(p):
    """Benjamini-Hochberg adjusted p-values (MATLAB mafdr 'BHFDR')."""
    p = np.asarray(p, float)
    n = p.size
    o = np.argsort(p)
    q = p[o] * n / np.arange(1, n + 1)
    q = np.minimum.accumulate(q[::-1])[::-1]
    out = np.empty(n)
    out[o] = np.minimum(q, 1)
    return out


def equalize(lists):
    """Truncate each bin to the smallest number of passes across bins (time order)."""
    m = min(len(x) for x in lists)
    return [np.asarray(x[:m]) for x in lists], m


def classify(u, window="wall", resp_window=None, alpha=0.05):
    """Classify one unit as in the claims file's opening comment.

    window: the window whose rate is the wall response for tuning and map tests;
    resp_window: the window used for responsiveness (default: same as window).
    Returns a dict with the classification under the code's BH-FDR
    responsiveness test ('c_', the claims file's main reading) and the
    uncorrected p < 0.05 variant ('m_')."""
    resp_window = resp_window or window
    base = u["rates"]["base"]
    wr = u["rates"][resp_window]
    w = u["rates"][window]
    if min(len(x) for x in w) < 2:
        return None
    bd, m = equalize(base)
    wrd, _ = equalize(wr)
    wd, _ = equalize(w)
    p_act = np.array([signrank(wrd[k], bd[k], "greater") for k in range(9)])
    p_sup = np.array([signrank(wrd[k], bd[k], "less") for k in range(9)])
    pairs = [(i, j) for i in range(9) for j in range(i + 1, 9)]
    p_t = np.array([signrank(wd[j], wd[i]) for i, j in pairs])
    q_t = bh(p_t)
    tuned = bool(np.any(q_t < alpha))
    mean_w = np.array([np.mean(x) for x in w])      # mean over all passes in each bin
    pref = int(np.argmax(mean_w))
    trough = int(np.argmin(mean_w))
    p_map = np.array([signrank(wd[k], wd[0], "greater") for k in range(1, 9)])
    q_map = bh(p_map)
    out = dict(tuned=tuned, pref=pref, trough=trough, mean_w=mean_w,
               min_q_map=float(q_map.min()), reps=m)
    for tag, (pa, ps) in {"m": (p_act, p_sup), "c": (bh(p_act), bh(p_sup))}.items():
        act = bool(np.any(pa < alpha))
        sup = bool(np.any(ps < alpha))
        resp = act or sup
        if not resp:
            cat = "unresponsive"
        elif not tuned:
            cat = "untuned"
        elif act:
            if pref == 0:
                cat = "proximity"
            elif np.any(q_map < alpha):
                cat = "map"
            else:
                cat = "ambiguous"
        else:
            cat = "suppressed_only"
        out.update({f"{tag}_act": act, f"{tag}_sup": sup, f"{tag}_resp": resp, f"{tag}_cat": cat})
    return out


def low_firing(u):
    mean_w = [np.mean(x) if len(x) else np.nan for x in u["rates"]["wall"]]
    base_all = np.concatenate(u["rates"]["base"])
    return bool(np.nanmax(mean_w) < 1 and np.mean(base_all) < 1)


def isi_fa(spk, thr=0.0008):
    """Percent of inter-spike intervals shorter than 0.8 ms (Methods, Isolation)."""
    if len(spk) < 2:
        return 0.0
    return 100.0 * np.mean(np.diff(spk) < thr)


def ks(x, y, alternative="two-sided"):
    """Two-sample K-S test with MATLAB kstest2 tail names mapped to scipy.

    MATLAB kstest2(x1, x2, 'Tail','larger') tests that the CDF of x1 is larger
    than that of x2 (x1 tends to be smaller); scipy's 'greater' is the same
    statement about the empirical CDFs of its first and second arguments."""
    return stats.ks_2samp(x, y, alternative=alternative)


def boot_ci_half(x, rng, n=10000):
    """Half-width of the bootstrap 95% percentile CI of the mean (Methods)."""
    x = np.asarray(x, float)
    mb = rng.choice(x, size=(n, x.size), replace=True).mean(1)
    lo, hi = np.percentile(mb, [2.5, 97.5])
    return (hi - lo) / 2


def ztest_prop(x1, n1, x2, n2):
    """Pooled two-proportion Z = (p1 - p2) / SE (Methods)."""
    p1, p2 = x1 / n1, x2 / n2
    pp = (x1 + x2) / (n1 + n2)
    se = np.sqrt(pp * (1 - pp) * (1 / n1 + 1 / n2))
    return (p1 - p2) / se


# ---------- population decoding ----------

def unit_bins(spk, starts_by_bin, t0=0.0, t1=DEC_T1, width=DEC_BIN, step=DEC_STEP):
    """Sliding-window counts per pass for each distance bin: list of (passes, bins)."""
    out = []
    for st in starts_by_bin:
        c, lefts = binned_counts(spk, np.asarray(st), t0, t1, width, step)
        out.append(c.astype(np.float32))
    return out, lefts


def _pseudo(units_data, rng, n_per=15, shuffle=False):
    """Pseudo-population: for each unit and distance draw n_per passes.

    Returns X (9*n_per, units, bins) and y (9*n_per,)."""
    nb = units_data[0][0].shape[1]
    X = np.empty((9 * n_per, len(units_data), nb), np.float32)
    for j, ud in enumerate(units_data):
        if shuffle:
            # code: rows of the unit's whole trial matrix permuted, labels kept
            allp = np.concatenate([d for d in ud], 0)
            allp = allp[rng.permutation(allp.shape[0])]
            sizes = np.cumsum([d.shape[0] for d in ud])[:-1]
            ud = np.split(allp, sizes, 0)
        for k in range(9):
            sel = rng.choice(ud[k].shape[0], n_per, replace=False)
            X[k * n_per:(k + 1) * n_per, j] = ud[k][sel]
    y = np.repeat(np.arange(9), n_per)
    return X, y


def _mcc_predict(Xtr, ytr, Xte):
    """Max-correlation classifier per time bin after z-scoring on training data."""
    mu = Xtr.mean(0, keepdims=True)
    sd = Xtr.std(0, ddof=1, keepdims=True)
    sd[sd == 0] = 1
    Ztr = (Xtr - mu) / sd
    Zte = (Xte - mu) / sd
    T = np.stack([Ztr[ytr == c].mean(0) for c in range(9)], 0)   # (9, units, bins)
    Tc = T - T.mean(1, keepdims=True)
    Ec = Zte - Zte.mean(1, keepdims=True)
    num = np.einsum("tub,cub->tcb", Ec, Tc)
    den = np.sqrt((Ec ** 2).sum(1))[:, None, :] * np.sqrt((Tc ** 2).sum(1))[None, :, :]
    r = num / np.where(den == 0, np.nan, den)
    r = np.nan_to_num(r, nan=-np.inf)
    return r.argmax(1)                                              # (test, bins)


def _svm_predict(Xtr, ytr, Xte):
    from sklearn.svm import SVC
    mu = Xtr.mean(0, keepdims=True)
    sd = Xtr.std(0, ddof=1, keepdims=True)
    sd[sd == 0] = 1
    Ztr = (Xtr - mu) / sd
    Zte = (Xte - mu) / sd
    out = np.empty((Xte.shape[0], Xte.shape[2]), int)
    for b in range(Xte.shape[2]):
        clf = SVC(kernel="linear", C=1.0, decision_function_shape="ovo")
        clf.fit(Ztr[:, :, b], ytr)
        out[:, b] = clf.predict(Zte[:, :, b])
    return out


def decode(units_data, rng, cv="15split", n_resample=5, n_per=15, shuffle=False,
           classifier="mcc"):
    """Cross-validated confusion counts per time bin: (9 actual, 9 predicted, bins).

    cv='15split': the code's num_cv_splits = 15 (one pseudo-trial per distance
    held out per split); cv='10fold': the Methods' 10-fold cross-validation,
    the 135 pseudo-trials split at random into 10 folds stratified by distance."""
    predict = _mcc_predict if classifier == "mcc" else _svm_predict
    nb = units_data[0][0].shape[1]
    cm = np.zeros((9, 9, nb))
    for _ in range(n_resample):
        X, y = _pseudo(units_data, rng, n_per, shuffle)
        if cv == "15split":
            fold = np.tile(np.arange(n_per), 9)                 # k-th draw of each distance
            folds = range(n_per)
        else:
            fold = np.empty(y.size, int)
            for c in range(9):
                ii = np.where(y == c)[0]
                fold[ii] = rng.permutation(np.arange(ii.size) % 10)
            folds = range(10)
        for k in folds:
            te = fold == k
            pred = predict(X[~te], y[~te], X[te])
            for a, p in zip(y[te], pred):
                cm[a, p, np.arange(nb)] += 1
    return cm


def summarize_cm(cm, lefts, t0=3.0, t1=11.0):
    """Accuracy (TPR) and error per true distance, averaged over bins starting in [t0, t1]."""
    sel = (lefts >= t0 - 1e-9) & (lefts <= t1 + 1e-9)
    c = cm[:, :, sel]
    tpr = np.array([c[k, k] / c[k].sum(0) for k in range(9)])      # (9, bins)
    derr = np.abs(CENTERS[:, None] - CENTERS[None, :])[:, :, None]
    err = (c * derr).sum(1) / c.sum(1)                              # per true distance
    return 100 * tpr.mean(1), err.mean(1)


# ---------- single-neuron decoder ----------

def single_neuron_decoder(counts_by_bin):
    """Euclidean nearest-template decoder, leave-two-out exhaustively (Methods).

    counts_by_bin: list of 9 arrays (passes, 40 bins of 200 ms over 3-11 s),
    truncated to equal numbers of passes. Returns accuracy per distance (%)."""
    X = np.stack(counts_by_bin, 0).astype(float)       # (9, n, b)
    n = X.shape[1]
    S = X.sum(1)                                       # (9, b)
    correct = np.zeros(9)
    total = 0
    for i in range(n):
        for j in range(i + 1, n):
            T = (S - X[:, i] - X[:, j]) / (n - 2)       # templates without the held-out pair
            for t in (i, j):
                d = ((X[:, t][:, None, :] - T[None, :, :]) ** 2).sum(2)   # (9 test, 9 templates)
                correct += (d.argmin(1) == np.arange(9))
            total += 2
    return 100 * correct / total


# ---------- whisker-cutting sessions ----------

def raw_asset_for(assets, session_path):
    stem = session_path[:-4]
    r = [a for a in assets if a["path"].startswith(stem + "_ecephys") and a["path"].endswith(".nwb")]
    return r[0] if r else None


def raw_pass_starts(asset):
    """Wall-pass start times of every pass in the raw file (wall_pass_epochs)."""
    f = h5py.File(remfile.File(asset_url(asset["asset_id"])), "r")
    st = f["intervals/wall_pass_epochs/start_time"][:]
    f.close()
    return st


def split_cut(pre_starts, all_starts):
    """Pre- and post-cut passes of a cutting session.

    The cut is taken as the longest gap between consecutive raw passes (the
    sessions' notes put the cutting in a gap of about 8 to 27 minutes). Pre-cut
    passes are the deposit's trials before that gap; post-cut passes are the
    raw passes after it. An assumption: the deposit has no condition label."""
    g = np.diff(all_starts)
    k = int(np.argmax(g))
    t_cut = (all_starts[k] + all_starts[k + 1]) / 2
    pre = pre_starts[pre_starts < t_cut]
    post = all_starts[all_starts > t_cut]
    return pre, post, t_cut, g[k], int((pre_starts > t_cut).sum())


# ---------- duplicate recordings ----------

def unit_signature(spk, n=50):
    return tuple(np.round(spk[:n], 4)) if len(spk) else ()


# ---------- circuit model (claim fig6-model-telc-loses-map) ----------

MODEL_REPO = "wanglab-neuro/2026_Xiao-Severson_Peri-head-distance"
MODEL_COMMIT = "b1a9f3c"


def load_model_code():
    """The paper's PrV_simulation package at the pinned commit, as modules in memory."""
    import sys
    import types
    base = f"https://raw.githubusercontent.com/{MODEL_REPO}/{MODEL_COMMIT}/PrV_simulation/"
    mods = {}
    for name in ["analysis", "plot_figures", "simulate_prv"]:
        src = requests.get(base + name + ".py", timeout=60).text
        m = types.ModuleType(name)
        sys.modules[name] = m
        exec(compile(src, base + name + ".py", "exec"), m.__dict__)
        mods[name] = m
    return mods


def run_model(mods, outdir, **kw):
    """Run simulate_prv.main with plotting replaced by a capture of the counts.

    Also records every call of analysis() in order, with the number of distance
    points of the curves it classified: main() classifies the control curves on
    the nine-bin grid and then on the 99-point grid, then the same for the
    reduced-inhibition curves; only the nine-bin counts are passed to plot()."""
    sim = mods["simulate_prv"]
    captured = {"analysis_calls": []}
    orig = sim.analysis

    def analysis_logged(curves, **k):
        sel, counts = orig(curves, **k)
        captured["analysis_calls"].append(dict(points=int(np.asarray(curves).shape[1]),
                                               counts=[int(c) for c in counts]))
        return sel, counts
    sim.analysis = analysis_logged

    def capture(selected, counts, fine, out, suffix="", **k):
        captured[suffix or "control"] = dict(counts=[int(c) for c in counts], n_selected=len(selected),
                                             curves=np.asarray(selected))
    sim.plot = capture
    sim.main(path=str(outdir), fast=True, **kw)
    return captured


def decode_job(args):
    """Picklable wrapper for parallel decoding: (units_data, seed, kwargs) -> confusion counts."""
    units_data, seed, kw = args
    return decode(units_data, np.random.default_rng(seed), **kw)


# ---------- unit depth along the probe (claim figs4j-ventral-location) ----------

def unit_waveforms(asset, spikes, windows, n_chunks=16):
    """Mean and variance of each unit's waveform from the raw voltage, per time window.

    windows: list of (t_lo, t_hi). For each window the spikes in n_chunks storage
    chunks (5.2 s each) spread evenly over it are taken, after a 300-6000 Hz
    band-pass (a standard spike band), 60 samples (2 ms) around each spike on
    every channel. A deviation to fit the time limit: not over all spikes.
    Returns the electrode group, the electrodes' rel_y and probe_site, and per
    window a list of dicts (n_spikes, mean (60, channels), var (60, channels))."""
    from scipy import signal
    f = h5py.File(remfile.File(asset_url(asset["asset_id"])), "r")
    es = f["acquisition/ElectricalSeriesRaw"]
    d = es["data"]
    fs = 30000.0
    t_start = float(es["starting_time"][()])
    el = f["general/extracellular_ephys/electrodes"]
    rows = es["electrodes"][:]
    rel_y = el["rel_y"][:][rows]
    site = el["probe_site"][:][rows]
    group = _s(el["group_name"][0])
    c = d.chunks[0]
    b, a = signal.butter(3, [300, 6000], btype="band", fs=fs)
    out = []
    for t_lo, t_hi in windows:
        k0, k1 = int((t_lo - t_start) * fs) // c, int((t_hi - t_start) * fs) // c
        ks = np.unique(np.linspace(k0, max(k0, k1 - 1), n_chunks).astype(int))
        sums = [np.zeros((60, d.shape[1])) for _ in spikes]
        sq = [np.zeros((60, d.shape[1])) for _ in spikes]
        nsp = np.zeros(len(spikes), int)
        for k in ks:
            X = signal.filtfilt(b, a, d[k * c:(k + 1) * c, :].astype(np.float32), axis=0)
            t0 = t_start + k * c / fs
            for i, sp in enumerate(spikes):
                st = sp[(sp > t0 + 0.005) & (sp < t0 + c / fs - 0.005)]
                idx = np.round((st - t0) * fs).astype(int)
                if idx.size:
                    W = X[idx[:, None] + np.arange(-30, 30)[None, :]]
                    sums[i] += W.sum(0)
                    sq[i] += (W.astype(np.float64) ** 2).sum(0)
                nsp[i] += idx.size
        res = []
        for i in range(len(spikes)):
            n = max(nsp[i], 1)
            m = sums[i] / n
            res.append(dict(n_spikes=int(nsp[i]), mean=m, var=np.maximum(sq[i] / n - m ** 2, 0)))
        out.append(res)
    f.close()
    return group, rel_y, site, out


def waveform_measures(w, rel_y, min_spikes=20):
    """Peak channel, depth and SNR of one unit's waveform (a dict from unit_waveforms).

    Methods (Unit Depth Along Silicon Probe): the peak channel is the channel of
    the mean waveform with the largest peak-to-trough amplitude; depth is that
    site's coordinate from the probe tip (rel_y; the electrodes table's
    probe_site column says site 1 is the tip, and the notebook shows that site 1
    has rel_y 0). Methods (Isolation of Single Unit Activity): SNR is 'the mean
    waveform amplitude divided by the standard deviation (SD) of waveform
    noise'. Taken here as the peak-to-trough amplitude on the peak channel over
    the SD of the single spikes about the mean waveform on that channel (the
    root of the variance averaged over the 60 samples), an assumption: the
    paper does not say how amplitude and noise are measured. Units with fewer
    than min_spikes spikes in the chunks get no measures."""
    if w["n_spikes"] < min_spikes:
        return dict(n_spikes=w["n_spikes"], peak_ch=-1, depth_um=np.nan, amp=np.nan, snr=np.nan)
    amp = w["mean"].max(0) - w["mean"].min(0)
    ch = int(amp.argmax())
    noise = float(np.sqrt(w["var"][:, ch].mean()))
    return dict(n_spikes=w["n_spikes"], peak_ch=ch, depth_um=float(rel_y[ch]), amp=float(amp[ch]),
                snr=float(amp[ch] / noise) if noise > 0 else np.nan)


def waveform_similarity(w1, w2, min_spikes=20):
    """Pearson correlation of two mean waveforms over all channels, and the ratio
    of their peak-to-trough amplitudes on the first one's peak channel. Used as a
    proxy for the paper's 'stable waveform properties both before and after
    cutting' (Methods), which the paper does not define: an assumption."""
    if min(w1["n_spikes"], w2["n_spikes"]) < min_spikes:
        return np.nan, np.nan
    a, b = w1["mean"], w2["mean"]
    amp1 = a.max(0) - a.min(0)
    ch = int(amp1.argmax())
    r = float(np.corrcoef(a.ravel(), b.ravel())[0, 1])
    return r, float((b[:, ch].max() - b[:, ch].min()) / amp1[ch])


# ---------- duplicate units ----------

def duplicate_pairs(spikes, t_end, thr=0.1, width=0.001):
    """Pairs of units of one session whose spike counts in 1-ms bins correlate above thr.

    Methods (Isolation of Single Unit Activity): 'Duplicate units, identified as
    those with high Pearson's correlation coefficients (> 0.1) in spike counts
    binned at 1 ms resolution, were excluded'. Bins span 0 to t_end. Returns
    (i, j, r) for each pair above thr."""
    nb = int(np.ceil(t_end / width))
    cnt = []
    for sp in spikes:
        k, c = np.unique((np.asarray(sp) / width).astype(np.int64), return_counts=True)
        cnt.append((k, c.astype(float)))
    stats_ = []
    for k, c in cnt:
        s1, s2 = c.sum(), (c ** 2).sum()
        stats_.append((s1 / nb, np.sqrt(max(s2 / nb - (s1 / nb) ** 2, 1e-30))))
    out = []
    for i in range(len(spikes)):
        for j in range(i + 1, len(spikes)):
            ki, ci = cnt[i]
            kj, cj = cnt[j]
            _, ia, ja = np.intersect1d(ki, kj, return_indices=True)
            exy = (ci[ia] * cj[ja]).sum() / nb
            r = (exy - stats_[i][0] * stats_[j][0]) / (stats_[i][1] * stats_[j][1])
            if r > thr:
                out.append((i, j, float(r)))
    return out
