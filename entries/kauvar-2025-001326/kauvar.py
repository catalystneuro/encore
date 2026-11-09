"""Loading and measures for dandiset 001326 (Kauvar, Richman, Liu et al. 2025, Science 388, eadt3971).

The dandiset holds the mouse Neuropixels sessions of the paper: per session, curated single units
(spike times, Allen CCFv3 acronym, SNR, spike count), the onsets of eyepuffs, tones and lights in
the table "Stimulus presentations", and the time of the ketamine infusion. Files are streamed from
the archive at the pinned version; nothing is written to disk.

Where each parameter comes from:

- Rates. "Firing rates were binned at 10 ms resolution and smoothed with a causal moving average
  filter over 50 ms" (Methods, Neuropixels recording and processing). Rates are in Hz as in
  brainwide-npix (refs. 17, 94) `firing_rates_over_recording` (count / 0.01 s), with its causal
  `moving_avg_filter` (first 4 bins left unsmoothed), then z-scored per unit over the session, as
  the paper's code works on session z-scored rates (claims file, opening comment).
- Peri-stimulus windows. -1 to 2 s around each onset, starting at
  `searchsorted(bins, onset) - 100` (analysis.py, get_cell_clusters).
- Epochs. Pre is puff series 1 to 20, Ketamine series 23 to 32, Post series 35 to 40 (claims file,
  opening comment, from analysis.py); the onset of ketamine in the code is 30 s after the last
  puff of series 20 (analysis.py ket_start_ts).
- Puff-modulated units. analysis.py `selective` (p <= 0.01, paired t-tests over the 160 Pre
  puffs or 20 Pre series) and `has_min_spikes` (summed Pre rate above 250).
- Coding dimensions. Mean difference over the per-neuron variance in both windows (Methods,
  "Coding dimension, mouse peri-puff"), the pooled variance of analysis.py compute_cd_cov as a
  variant; normalized to a unit vector (Methods) or by the sum of absolute values (code).
- Emotion-like dimension. Methods, "Emotion-like neural dimension", with analysis.py
  get_affective_projections for the eye-reflex dimension, the QR step and the sign.
- Timescale fits. analysis.py extract_timescale (fit_time 2.5 s, initial b 0.2).
- Model. analysis.py model_system, theoretical_* and compare_model.
- Verification checks (added after the first verification round, not the paper's method): the series
  onsets against the file's infusion time, tone and light onsets inside the analysis windows, the
  correlation structure from the file's infusion time, persistent weights from half the Pre series,
  and the bounded and mean-removed timescale fits of `extract_timescale`.

Cite Kauvar, Richman, Liu et al., Science (2025) for the methods reimplemented here.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

import h5py
import numpy as np
import pandas as pd
import remfile
import scipy.signal
import scipy.stats
from scipy.optimize import curve_fit

DANDISET = "001326"
VERSION = "0.250528.1957"          # dandi:001326/0.250528.1957, the only published version
BIN = 0.01                          # s, Methods
SMOOTH = 5                          # bins, 50 ms causal moving average, Methods
ALLEN_CSV = ("https://raw.githubusercontent.com/cortex-lab/allenCCF/"
             "e5a57fe7e1c9fb333fec51c29a8471131c233a76/structure_tree_safe_2017.csv")
# brainwide-npix anatomy.py, the paper's top-level divisions
TOP_LEVEL = ["Isocortex", "OLF", "HPF", "CTXsp", "STR", "PAL", "TH", "HY", "MB", "HB", "CB"]


def asset_urls():
    """(path, S3 url) of every NWB file in the pinned version, sorted by path."""
    from dandi.dandiapi import DandiAPIClient
    with DandiAPIClient() as client:
        ds = client.get_dandiset(DANDISET, VERSION)
        out = [(a.path, a.get_content_url(follow_redirects=1, strip_query=True)) for a in ds.get_assets()]
    return sorted(out)


def _str(a):
    return np.array([x.decode() if isinstance(x, bytes) else str(x) for x in a])


@dataclass
class Session:
    path: str
    subject: str
    spikes: list
    regions: np.ndarray
    snr: np.ndarray
    n_spikes: np.ndarray
    quality: np.ndarray
    stim: pd.DataFrame
    ket_infusion: float
    maxt: float
    n_unsorted_units: int
    n_spikes_total: int
    meta: dict = field(default_factory=dict)

    @property
    def name(self):
        return self.path.split("/")[-1].replace("_ecephys.nwb", "")

    def onsets(self, kind):
        return self.stim.loc[self.stim.stimulus == kind, "start_time"].to_numpy()


def load_session(path, url):
    """Stream one file and return its units, stimulus table and infusion time."""
    f = h5py.File(remfile.File(url), "r")
    st = f["units/spike_times"][:]
    idx = f["units/spike_times_index"][:]
    spikes = np.split(st, idx[:-1])
    n_unsorted = int(sum(np.any(np.diff(s) < 0) for s in spikes))
    spikes = [np.sort(s) for s in spikes]
    g = f["intervals/Stimulus presentations"]
    stim = pd.DataFrame({"start_time": g["start_time"][:], "stop_time": g["stop_time"][:],
                         "stimulus": _str(g["stimulus"][:])}).sort_values("start_time").reset_index(drop=True)
    sess = Session(
        path=path,
        subject=str(_str([f["general/subject/subject_id"][()]])[0]),
        spikes=spikes,
        regions=_str(f["units/brain_region"][:]),
        snr=f["units/snr"][:],
        n_spikes=f["units/n_spikes"][:],
        quality=_str(f["units/quality"][:]),
        stim=stim,
        ket_infusion=float(f["acquisition/Ketamine infusion start/timestamps"][0]),
        maxt=float(st.max()),
        n_unsorted_units=n_unsorted,
        n_spikes_total=len(st),
    )
    sess.meta = {
        "age": str(_str([f["general/subject/age"][()]])[0]),
        "sex": str(_str([f["general/subject/sex"][()]])[0]),
        "devices": sorted(f["general/devices"].keys()),
        "ket_desc": str(_str([f["acquisition/Ketamine infusion start"].attrs.get("description", "")])[0]),
    }
    f.close()
    return sess


def rates(sess):
    """Session z-scored rates (units x bins, float32) and the per-unit mean and sd of the Hz rates.

    10 ms bins from 0 to the last spike, rate = count / 0.01 s, causal 50 ms moving average as
    brainwide-npix moving_avg_filter (the first 4 bins unsmoothed), z-scored per unit.
    """
    nb = int(np.ceil(sess.maxt / BIN))
    z = np.empty((len(sess.spikes), nb), dtype=np.float32)
    mu = np.empty(len(sess.spikes))
    sd = np.empty(len(sess.spikes))
    for i, s in enumerate(sess.spikes):
        c = np.bincount(np.minimum((s / BIN).astype(np.int64), nb - 1), minlength=nb).astype(np.float64) / BIN
        cs = np.cumsum(np.concatenate([[0.0], c]))
        sm = c.copy()
        sm[SMOOTH - 1:] = (cs[SMOOTH:] - cs[:-SMOOTH]) / SMOOTH
        mu[i] = sm.mean()
        sd[i] = sm.std()
        z[i] = (sm - mu[i]) / sd[i]
    return z, mu, sd


def onset_bins(onsets, nb):
    """Bin index of each onset as analysis.py: searchsorted(bins, t)."""
    bins = np.arange(nb) * BIN
    return np.searchsorted(bins, onsets)


def windows(z, start_bins, length):
    """z[:, s:s+length] for each start, as (units, n_starts, length)."""
    out = np.empty((z.shape[0], len(start_bins), length), dtype=np.float32)
    for k, s in enumerate(start_bins):
        out[:, k] = z[:, s:s + length]
    return out


def selective(r, cutoff=0.01):
    """analysis.py selective(); r is (units, series, 8, 300) of -1..2 s windows. Returns mask and per-test masks."""
    n = r.shape[0]
    flat = r.reshape(n, -1, r.shape[-1])
    pre = flat[..., :100].mean(-1)
    ref = flat[..., 100:120].mean(-1)
    aff = flat[..., 130:180].mean(-1)
    lng = flat[..., 200:300].mean(-1)
    eb = r[:, :, 0, :100].mean(-1)
    lb = r[:, :, -1, :100].mean(-1)
    er = r[:, :, 0, 100:200].mean(-1)
    lr = r[:, :, -1, 100:200].mean(-1)
    tests = {
        "pre vs 0-200 ms": scipy.stats.ttest_rel(pre, ref, axis=1).pvalue <= cutoff,
        "pre vs 300-800 ms": scipy.stats.ttest_rel(pre, aff, axis=1).pvalue <= cutoff,
        "pre vs 1-2 s": scipy.stats.ttest_rel(pre, lng, axis=1).pvalue <= cutoff,
        "baseline first vs last puff": scipy.stats.ttest_rel(eb, lb, axis=1).pvalue <= cutoff,
        "response first vs last puff": scipy.stats.ttest_rel(er, lr, axis=1).pvalue <= cutoff,
    }
    m = np.zeros(n, bool)
    for v in tests.values():
        m |= v
    return m, tests


def cd_weights(x, y, var="unit", scale="unit"):
    """Coding dimension from x, y (units x trials) of target and reference window means.

    var 'unit': per-neuron variance of both windows (Methods); 'pooled': np.var over all units and
    trials (analysis.py compute_cd_cov). scale 'unit': unit vector (Methods); 'l1': sum of |w| (code).
    """
    if var == "unit":
        den = np.sqrt(x.var(1) + y.var(1))
        den[den == 0] = np.inf
    else:
        den = np.sqrt(np.var(x) + np.var(y))
    v = (x.mean(1) - y.mean(1)) / den
    return v / (np.linalg.norm(v) if scale == "unit" else np.sum(np.abs(v)))


def my_qr(mat):
    """analysis.py my_qr: QR with the sign correction of the code."""
    q, r = np.linalg.qr(mat)
    for i in range(1, r.shape[0]):
        if np.any(r[i, :] < 0):
            q[:, i] = -q[:, i]
    return q, r


def extract_timescale(signal, fit_time=2.5, t0=0.2, demean=False, bounded=False):
    """analysis.py extract_timescale: autocorrelation (scipy.signal.correlate) from lag 1, normalized to
    its maximum, a*exp(-x/b)+c fitted over fit_time with p0 (1, t0, 0). Returns b, or nan if the fit fails.

    Verification variants, not in the code: `demean` subtracts the signal's mean before the autocorrelation
    (the code does not, so a mean level adds a constant that the fit must absorb); `bounded` limits b to
    0.001 to 2.5 s (the fit window), where the code's fit is unbounded."""
    def curve(x, a, b, c):
        return a * np.exp(-x / b) + c
    signal = np.asarray(signal, float)
    if demean:
        signal = signal - signal.mean()
    sig = scipy.signal.correlate(signal, signal)[len(signal):][:int(round(fit_time / BIN))]
    sig = sig / sig.max()
    x = np.arange(len(sig)) * BIN
    kw = dict(bounds=([-np.inf, 0.001, -np.inf], [np.inf, fit_time, np.inf])) if bounded else {}
    try:
        popt, _ = curve_fit(curve, x, sig, p0=[1, t0, 0], maxfev=2000, **kw)
        return popt[1]
    except RuntimeError:
        return np.nan


def dprime_trace(p):
    """analysis.py calculate_dprime on (trials, 300): each bin against the 1 s baseline."""
    bm = p[:, :100].mean()
    bs = p[:, :100].flatten().std()
    return (p.mean(0) - bm) / np.sqrt(0.5 * (bs ** 2 + p.std(0) ** 2))


def reduce_region(s):
    """analysis.py reduce_region: merge cortical layers."""
    m = re.match(r"(?!CA[123])(.*?)(2/3|1|5|6a|6b|pc)$", s)
    return m.groups()[0] if m else s


def allen_tree():
    """Allen CCFv3 2017 structure tree (the file brainwide-npix loads), from cortex-lab/allenCCF at a commit."""
    t = pd.read_csv(ALLEN_CSV)
    acr = dict(zip(t.id, t.acronym))
    paths = {a: [acr[int(i)] for i in p.strip("/").split("/")] for a, p in zip(t.acronym, t.structure_id_path)}
    return paths


def top_level(acronym, paths):
    """brainwide-npix get_acronym(level='top'): the first of TOP_LEVEL among the ancestors, else 'NA'."""
    anc = paths.get(acronym)
    if anc is None:
        return "NA"
    for a in TOP_LEVEL:
        if a in anc:
            return a
    return "NA"


def under(acronym, parent, paths):
    anc = paths.get(acronym)
    return anc is not None and parent in anc


# ---------------------------------------------------------------- per-session reduction

def series_onsets(t, gap=10.0):
    """Split onsets into series at gaps above `gap` s; returns a list of arrays."""
    br = np.where(np.diff(t) > gap)[0] + 1
    return np.split(t, br)


def process_session(sess, paths, top_frac=0.1):
    """Everything the notebook needs from one session, reduced as it loads.

    Returns a dict. Arrays of puff-modulated units only, unless said otherwise.
    """
    out = {"name": sess.name, "subject": sess.subject, "n_units": len(sess.spikes)}
    z, mu, sd = rates(sess)
    nb = z.shape[1]
    puffs = sess.onsets("puff")
    ser = series_onsets(puffs)
    out["series_sizes"] = [len(s) for s in ser]
    P = puffs.reshape(-1, 8)
    nser = P.shape[0]
    out["n_series"] = nser
    ket_start = P[19, -1] + 30
    out["ket_start_code"] = ket_start
    out["ket_infusion_nwb"] = sess.ket_infusion
    # first and last puff of every series relative to the file's infusion time (verification check of the epochs)
    out["series_rel_infusion"] = np.c_[P[:, 0], P[:, -1]] - sess.ket_infusion
    # tone and light onsets inside the windows the analyses use: the 30 s before each puff series (timescale,
    # coupling) and the 50 s post-series window from 1 s before the last puff (emotion-like dimension)
    def n_in(t, lo, hi):
        return int(((t >= lo) & (t < hi)).sum())
    out["stim_in_windows"] = {kind: {"30 s before series": np.array([n_in(sess.onsets(kind), a - 30, a) for a in P[:, 0]]),
                                     "50 s after series": np.array([n_in(sess.onsets(kind), b - 1, b + 49) for b in P[:, -1]])}
                              for kind in ("tone", "light")}
    pb = onset_bins(puffs, nb)
    sta = pb - 100
    W = windows(z, sta, 300).reshape(z.shape[0], nser, 8, 300)       # all units, all series
    pre = W[:, :20]
    # clock check: population response 0-200 ms after each puff against the 1 s before, at the table's onsets
    # and at onsets shifted by 1.5 s (between puffs), over all units and all puffs
    resp = lambda w: float((w[..., 100:120].mean(-1) - w[..., :100].mean(-1)).mean())
    Wsh = windows(z, onset_bins(puffs + 1.5, nb) - 100, 300)
    out["clock_puff"] = {"true": resp(W), "shifted 1.5 s": resp(Wsh)}
    del Wsh
    m, tests = selective(pre)
    # has_min_spikes: summed Hz rate over Pre (analysis.py), and the spike-count reading
    s0, s1 = sta[0], sta[160] + 3
    hz_sum = np.array([((sp >= s0 * BIN) & (sp < s1 * BIN)).sum() for sp in sess.spikes]) / BIN
    out["has_min_hz"] = hz_sum > 250
    out["has_min_count"] = hz_sum * BIN > 250
    out["n_selective"] = int(m.sum())
    out["n_test"] = {k: int(v.sum()) for k, v in tests.items()}
    sel = m & out["has_min_hz"]
    out["sel_count_reading"] = int((m & out["has_min_count"]).sum())
    out["sel"] = sel
    idx = np.where(sel)[0]
    out["regions_all"] = sess.regions
    out["regions"] = sess.regions[idx]
    Wm = W[idx]
    del W
    out["pre_avg"] = Wm[:, :20].mean((1, 2))
    ket = Wm[:, 22:32]
    post = Wm[:, 34:40]
    out["ket_avg"] = ket.mean((1, 2))
    out["first2_pre"] = Wm[:, :20, :2].copy()
    out["first2_ket"] = ket[:, :, :2].copy()
    out["first2_ket_lit"] = Wm[:, 21:32, :2].copy()      # Methods-literal 22 to 32
    n = len(idx)
    out["n_mod"] = n
    # ---- coding dimensions (puff)
    cds = {}
    for var in ("unit", "pooled"):
        # persistent: per series mean over puffs (analysis.py), target 0.5-1 s, ref -1-0 s
        x = Wm[:, :20, :, 150:200].mean(2).mean(-1)
        y = Wm[:, :20, :, :100].mean(2).mean(-1)
        wP = cd_weights(x, y, var, "unit")
        cds[("persist", var)] = wP
        # fast: per puff, target 0-70 ms, ref 1 s (Methods) or 70 ms (code)
        xf = Wm[:, :20, :, 100:107].mean(-1).reshape(n, -1)
        for ref in ("1s", "70ms"):
            yf = (Wm[:, :20, :, :100] if ref == "1s" else Wm[:, :20, :, 93:100]).mean(-1).reshape(n, -1)
            cds[("fast", var, ref)] = cd_weights(xf, yf, var, "unit")
    out["cd"] = cds
    proj = {}
    for key, w in cds.items():
        for cond, block in (("pre", Wm[:, :20]), ("ket", ket), ("post", post), ("ket_lit", Wm[:, 21:32]), ("post_lit", Wm[:, 33:40])):
            pr = np.tensordot(w, block, axes=([0], [0]))      # (series, 8, 300)
            proj[key + (cond,)] = {"first": pr[:, 0].mean(0), "all": pr.mean((0, 1))}
    out["cd_proj"] = proj
    # held-out check: persistent weights from the odd Pre series (1, 3, ..., 19), projections of the even Pre
    # series (2, 4, ..., 20), which the weights never saw, and of Ketamine and Post with the same weights
    ho = {}
    for var in ("unit", "pooled"):
        tr = Wm[:, 0:20:2]
        w = cd_weights(tr[:, :, :, 150:200].mean(2).mean(-1), tr[:, :, :, :100].mean(2).mean(-1), var, "unit")
        for cond, block in (("pre_train", Wm[:, 0:20:2]), ("pre_test", Wm[:, 1:20:2]), ("ket", ket), ("post", post)):
            ho[(var, cond)] = np.tensordot(w, block, axes=([0], [0]))[:, 0].mean(0)
    out["cd_proj_heldout"] = ho
    # ---- baseline windows (30 s before the first puff of each series): timescale and coupling
    first = P[:, 0]
    fb = onset_bins(first, nb)
    base_pre = list(range(0, 20))
    base_ket = list(range(22, 32))
    ts = {}
    for var in ("unit", "pooled"):
        w = cds[("persist", var)]
        sigs_pre = np.array([w @ z[idx, fb[k] - 3000:fb[k]] for k in base_pre])
        sigs_ket = np.array([w @ z[idx, fb[k] - 3000:fb[k]] for k in base_ket])
        ts[var] = {"pre_sigs": sigs_pre, "ket_sigs": sigs_ket}
    out["base_sigs"] = ts
    # coupling: persistent neurons (top 10% of |w|, Methods; signed w above the 90th percentile of |w|, code)
    coup = {}
    for var in ("unit", "pooled"):
        w = cds[("persist", var)]
        aw = np.abs(w)
        thr = np.percentile(aw, 90)
        sets = {"methods": idx[aw >= thr], "code": idx[w > thr]}
        for sname, units in sets.items():
            res = {}
            for cond, ks in (("pre", list(range(0, 10))), ("ket", base_ket), ("pre20", base_pre)):
                per = []
                for k in ks:
                    c = np.corrcoef(z[units, fb[k] - 3000:fb[k]])
                    iu = np.triu_indices(len(units), 1)
                    per.append(np.nanmean(c[iu]))
                cat = np.hstack([z[units, fb[k] - 3000:fb[k]] for k in ks])
                c = np.abs(np.corrcoef(cat))
                off = ~np.eye(len(units), dtype=bool)
                res[cond] = {"per_series_mean_r": np.array(per), "concat_median_abs_r": float(np.nanmedian(c[off]))}
            res["n_units"] = len(units)
            coup[(var, sname)] = res
    out["coupling"] = coup
    out["top_units_regions"] = {var: sess.regions[idx[np.abs(cds[("persist", var)]) >= np.percentile(np.abs(cds[("persist", var)]), 90)]] for var in ("unit", "pooled")}
    # ---- emotion-like dimension
    lb = onset_bins(P[:, -1], nb) - 100                       # post window starts 1 s before the last puff
    post_len = 5000
    S8 = Wm.reshape(n, nser, 2400)                            # 8 puff windows concatenated, -1 s to 23 s
    PW = np.empty((n, nser, post_len), dtype=np.float32)
    for k in range(nser):
        seg = z[idx, lb[k]:lb[k] + post_len]
        PW[:, k, :seg.shape[1]] = seg
        if seg.shape[1] < post_len:
            PW[:, k, seg.shape[1]:] = np.nan
    emo = {}
    groups = {"all": np.ones(n, bool)}
    tl = np.array([top_level(r, paths) for r in out["regions"]])
    out["top_level_mod"] = tl
    for a in TOP_LEVEL:
        if (tl == a).sum() >= 20:
            groups[a] = tl == a
    for gname, gm in groups.items():
        variants = [("methods", "unit")] if gname != "all" else [(t, v) for t in ("methods", "code") for v in ("unit", "pooled")]
        if gname != "all":
            variants = [("methods", "unit"), ("code", "unit")]
        for tw, var in variants:
            sl = slice(600, 700) if tw == "methods" else slice(400, 500)
            x = PW[gm, :20, sl].mean(-1)
            y = Wm[gm, :20, 0, 0:75].mean(-1)
            ca = cd_weights(x, y, var, "unit")
            xe = Wm[gm, :20, 4:, 100:120].mean(-1).reshape(gm.sum(), -1)
            ye = Wm[gm, :20, 4:, 80:100].mean(-1).reshape(gm.sum(), -1)
            ce = cd_weights(xe, ye, var, "unit")
            q, _ = my_qr(np.vstack((ce, ca)).T)
            w = q[:, 1]
            tmp = np.tensordot(w, Wm[gm, :20], axes=([0], [0])).mean(0)   # (8, 300)
            if tmp.mean(-1)[7] < tmp.mean(-1)[0]:
                w = -w
            res = {"w": w, "l1_factor": 1.0 / np.sum(np.abs(w))}   # multiply by l1_factor for the code's scaling
            for cond, ks in (("pre", slice(0, 20)), ("ket", slice(22, 32)), ("ket_lit", slice(21, 32))):
                s8 = np.tensordot(w, S8[gm, ks], axes=([0], [0]))      # (series, 2400)
                pw = np.tensordot(w, PW[gm, ks], axes=([0], [0]))      # (series, 5000)
                res[cond] = {"s8": s8.mean(0), "post": np.nanmean(pw, 0), "s8_series": s8}
            emo[(gname, tw, var)] = res
    out["emotion"] = emo
    out["emo_groups_n"] = {g: int(v.sum()) for g, v in groups.items()}
    del PW, S8
    # ---- tones
    tones = sess.onsets("tone")
    if len(tones):
        out["tone_series_sizes"] = [len(s) for s in series_onsets(tones)]
        T = tones.reshape(-1, 8)
        tb = onset_bins(tones, nb) - 100
        TW = windows(z[idx], tb, 300).reshape(n, T.shape[0], 8, 300)
        tfb = onset_bins(T[:, 0], nb)
        Tsh = windows(z[idx], onset_bins(tones + 1.5, nb) - 100, 300)
        resp = lambda w: float((w[..., 100:120].mean(-1) - w[..., :100].mean(-1)).mean())
        out["clock_tone"] = {"true": resp(TW), "shifted 1.5 s": resp(Tsh)}
        del Tsh
        out["tone"] = {}
        # 'infusion': Pre is the 10 tone series before the infusion time of the file and Ketamine and
        # Post count from the infusion (claims file); 'code': both split at ket_start_ts as analysis.py.
        for reading, split in (("infusion", sess.ket_infusion), ("code", ket_start)):
            pre_t = np.where(T[:, 0] < split)[0][:10]
            post_t = np.where(T[:, 0] > split)[0][:10]
            out["tone"][reading] = _tone_block(z, idx, n, TW, tfb, pre_t, post_t, fb, base_ket, Wm, cds)
        del TW
    # ---- resting correlation structure (fig. S30), all units
    b_ket = int(ket_start / BIN)
    pre_seg = z[:, :b_ket]
    ket_seg = z[:, b_ket:b_ket + 60000]
    def corr(a):
        a = a - a.mean(1, keepdims=True)
        a /= np.linalg.norm(a, axis=1, keepdims=True)
        return a @ a.T
    out["corr_pre"] = corr(pre_seg.copy()).astype(np.float32)
    out["corr_ket"] = corr(ket_seg.copy()).astype(np.float32)
    # variant: the 10 minutes from the file's infusion time (Methods, "the 10-minute period following the onset
    # of ketamine infusion"); Pre is then everything before the infusion
    b_inf = int(sess.ket_infusion / BIN)
    out["corr_pre_inf"] = corr(z[:, :b_inf].copy()).astype(np.float32)
    out["corr_ket_inf"] = corr(z[:, b_inf:b_inf + 60000].copy()).astype(np.float32)
    # ---- spectra (fig. S29): minute before infusion and minutes from 5 and 10 min after
    t_inf = sess.ket_infusion
    spec = {}
    for lab, t0 in (("before", t_inf - 60), ("after5", t_inf + 300), ("after10", t_inf + 600)):
        seg = z[:, int(t0 / BIN):int(t0 / BIN) + 6000].astype(np.float64)
        f, pxx = scipy.signal.welch(seg, fs=1 / BIN, nperseg=2048, axis=1)
        zz = scipy.stats.zscore(pxx, axis=1)
        band = (f > 0) & (f <= 7.5)
        spec[lab] = zz[:, band].max(1)
    out["spec_peak"] = spec
    out["spec_freqs"] = f
    del z
    return out


def _tone_block(z, idx, n, TW, tfb, pre_t, post_t, fb, base_ket, Wm, cds):
    """Tone coding dimensions, projections, baseline signals and coupling for one split of the tone series."""
    o = {"pre_series": pre_t, "post_series": post_t}
    tpre, tpost = TW[:, pre_t], TW[:, post_t]
    tcd = {}
    for var in ("unit", "pooled"):
        x = tpre[..., 115:135].mean(2).mean(-1)
        y = tpre[..., :100].mean(2).mean(-1)
        tcd[("persist", var)] = cd_weights(x, y, var, "unit")
        xf = tpre[..., 100:107].mean(-1).reshape(n, -1)
        for ref in ("1s", "70ms"):
            yf = (tpre[..., :100] if ref == "1s" else tpre[..., 93:100]).mean(-1).reshape(n, -1)
            tcd[("fast", var, ref)] = cd_weights(xf, yf, var, "unit")
    tproj = {}
    for key, w in tcd.items():
        for cond, block in (("pre", tpre), ("ket", tpost[:, 1:6]), ("post", tpost[:, 7:10])):
            pr = np.tensordot(w, block, axes=([0], [0]))
            tproj[key + (cond,)] = {"all": pr.mean((0, 1)), "first": pr[:, 0].mean(0)}
    o["proj"] = tproj
    o["dprime_puff"] = {var: dprime_trace(np.tensordot(cds[("persist", var)], Wm[:, :20], axes=([0], [0])).mean(1)) for var in ("unit", "pooled")}
    o["dprime_tone"] = {var: dprime_trace(np.tensordot(tcd[("persist", var)], tpre, axes=([0], [0])).mean(1)) for var in ("unit", "pooled")}
    o["base_sigs"] = {var: {"pre_sigs": np.array([tcd[("persist", var)] @ z[idx, tfb[k] - 3000:tfb[k]] for k in pre_t]),
                            "post_sigs": np.array([tcd[("persist", var)] @ z[idx, tfb[k] - 3000:tfb[k]] for k in post_t])}
                      for var in ("unit", "pooled")}
    tcoup = {}
    for var in ("unit", "pooled"):
        w = tcd[("persist", var)]
        aw = np.abs(w)
        thr = np.percentile(aw, 90)
        for sname, units in {"methods": idx[aw >= thr], "code": idx[w > thr]}.items():
            res = {}
            for cond, ks in (("pre", list(pre_t)), ("ket", list(post_t[1:6]))):
                per = []
                for k in ks:
                    c = np.corrcoef(z[units, tfb[k] - 3000:tfb[k]])
                    per.append(np.nanmean(c[np.triu_indices(len(units), 1)]))
                cat = np.hstack([z[units, tfb[k] - 3000:tfb[k]] for k in ks])
                c = np.abs(np.corrcoef(cat))
                res[cond] = {"per_series_mean_r": np.array(per),
                             "concat_median_abs_r": float(np.nanmedian(c[~np.eye(len(units), dtype=bool)]))}
            # the code's coupling loop takes the windows before puff series 1-10 and 23-32 for any stimulus
            for cond, ks in (("pre_puffwin", list(range(10))), ("ket_puffwin", base_ket)):
                cat = np.hstack([z[units, fb[k] - 3000:fb[k]] for k in ks])
                c = np.abs(np.corrcoef(cat))
                res[cond] = {"concat_median_abs_r": float(np.nanmedian(c[~np.eye(len(units), dtype=bool)]))}
            res["n_units"] = len(units)
            tcoup[(var, sname)] = res
    o["coupling"] = tcoup
    return o


# ---------------------------------------------------------------- model (analysis.py, Theoretical model)

_inputs = np.hstack([np.concatenate([np.zeros(100), np.ones(25), np.zeros(175)]) for _ in range(8)])
_inputs = np.hstack([_inputs, np.zeros(int(47 / BIN))])
_segments = np.hstack([np.hstack([(i * 300), (i * 300) + 100, (i * 300) + 100, (i * 300) + 125,
                                  (i * 300) + 125, (i * 300) + 300]) for i in range(8)])
_segments = np.hstack([_segments, [300 * 8, 300 * 8 + int(47 / BIN)]]).reshape((-1, 2))


def model_system(S, tB, tP, symmetric=False):
    Sin = S * _inputs
    output = np.zeros_like(Sin)
    x0 = Sin[0]
    for a, b in _segments:
        t = np.arange(0, b - a) * BIN
        if Sin[a] != 0:
            xt = (Sin[a] - x0) * (1 - np.exp(-t / tB)) + x0
        else:
            xt = x0 * np.exp(-t / (tB if symmetric else tP))
        output[a:b] = xt
        x0 = xt[-1]
    return output


def _cut(o):
    return np.hstack([o[75:300 * 8], o[300 * 8 + 200:300 * 8 + int(49 / BIN)]])


def theoretical(kind):
    def f(x, S, tB, tP, *c):
        tr = []
        for ci in c:
            if kind == "persist":
                o = model_system(S, tB, tP * ci)
            elif kind == "broadcast":
                o = model_system(S, tB * ci, tP)
            elif kind == "saturation":
                o = model_system(S * ci, tB, tP)
            else:
                o = model_system(S, tB * ci, tP, symmetric=True)
            tr.append(_cut(o) + (100 * tP if kind == "symmetric" else 0))
        return np.hstack(tr)
    return f


def compare_model(kind, data, conditions=2):
    """analysis.py compare_models for one model: fit and null fit, variance explained 1 - MSE/MSE_null."""
    model = theoretical(kind)
    p0 = [1, 1, 1] + [1] * conditions
    bounds = ([0, 0, 0] + [0] * conditions, [100, 100, 100] + [1] * conditions)
    bounds_null = ([0, 0, 0] + [0.99999] * conditions, [100, 100, 100] + [1] * conditions)
    x = np.arange(len(data))
    pm, _ = curve_fit(model, x, data, p0=p0, maxfev=5000, bounds=bounds)
    pred = model(1, *pm)
    pn, _ = curve_fit(model, x, data, p0=p0, maxfev=5000, bounds=bounds_null)
    predn = model(1, *pn)
    return {"varexp": 1 - np.mean((data - pred) ** 2) / np.mean((data - predn) ** 2), "fit": pm, "pred": pred, "null": predn}


def moving_avg(t, win=10):
    """analysis.py moving_avg_filter (causal): the first win-1 values unchanged."""
    out = np.asarray(t, float).copy()
    cs = np.cumsum(np.concatenate([[0.0], out]))
    out[win - 1:] = (cs[win:] - cs[:-win]) / win
    return out
