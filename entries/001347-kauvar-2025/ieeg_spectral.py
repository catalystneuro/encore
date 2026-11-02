"""Human iEEG spectral analyses (Figs. 2G to 2J, 3B, 3C, fig. S13) of Kauvar, Richman, Liu et al. 2025.

All spectrograms are the dataset's own aggregated products in sub-H/ of DANDI:001347
(read through dandi_io): per-channel trial means split into train and test halves
(sub-H_ses-sgramPerChannel.nwb), per-channel per-trial spectrograms
(sub-H_ses-sgramPerChannelPerTrial.nwb), per-network and per-region per-trial
spectrograms (sub-H_ses-sgramPerYeoPerTrial.nwb, sub-H_ses-sgramPerRegionPerTrial.nwb). The
paper's deposited outputs (NMF factors and loadings, cluster-test maps) are read only to
compare with the results computed here.

Where each parameter comes from:
- NMF: scikit-learn NMF, solver 'mu', random_state 1, Frobenius loss, default init and
  iterations, 3 components on the positive part and 3 on the negative part of the
  pre/postinfusion training mean (claims file, Open G and fig2g criterion; code
  ketman/analyze/decode_utils.get_nmf and analyze_airpuff_ieeg_sgram_load_allpt.py lines
  381 to 389). The paper's code ran scikit-learn 1.4.1 (requirements.txt), whose default
  init for this shape is 'nndsvda', as in the version used here.
- CODE_ORDER [0, 2, 4, 5, 1, 3]: the code's fixed numbering of the fitted factors
  (analyze_airpuff_ieeg_sgram_load_allpt.py line 421; claims file Open G).
- Time bins 0 < t < 1.4 s for the NMF (same script, lines 230 to 231); -0.5 to 1.5 s for the
  cluster test (lines 74 to 75; the network and region files hold exactly this range).
- LOADING_THRESH 0.1 on the loading of the averaged pre/postinfusion test spectrogram
  (same script, lines 507 to 528; Methods, Factorization).
- Held-out explained variance: the code's nmf_k_determination (decode_utils lines 136 to
  291) compares the training reconstruction with the test data (do_refit_W_for_test =
  False); the refit of the loadings on the test data is a second reading.
- Elbow: the point of the test curve farthest from the chord joining its ends (a standard
  knee rule; the paper gives none).
- Cluster test: mne.stats.permutation_cluster_1samp_test on infusion minus preinfusion
  trials, threshold the two-tailed t at p = 0.01 with n - 1 degrees of freedom, 512
  permutations, seed 1; a cluster is significant below 0.01; a unit without one gets p = 1
  and the lowest cluster p per unit is Benjamini-Hochberg corrected across units
  (claims fig3b criterion; code trace_utils.permutation_cluster_test,
  permutation_cluster_thresh_t, fdr_correct_clusters_across_regions; PARAMS[0]).
- PLOT_REGIONS: the 21 regions of Fig. 3C (script lines 146 to 148; Table S3).
- YEO_REGIONS: the six Yeo7 networks of Fig. 2H and 3B (script lines 578 to 579).
- Channel Yeo7 labels are not in the dataset; they are read from the code record's
  anat/pts_ch_labels.pkl (pt_elec_yeos_bipo), matched to channels by participant and
  bipolar electrode name, as the code does (script lines 561 to 576).
- Resting spectra and band-limited oscillations (figs. S15 and S27) are computed from the
  per-participant 20-min LFP files (sub-SD*/..._ecephys.nwb) read with ieeg_cd.load_session;
  the timing, multitaper, FOOOF and clustering parameters are cited in the section
  "resting spectra" below.
"""
import hashlib
import io
import pickle
import re
import zipfile

import numpy as np
import pandas as pd
import requests
import scipy.stats as ss
from sklearn.decomposition import NMF
from statsmodels.stats.multitest import multipletests

import dandi_io

F_CH = "sub-H/sub-H_ses-sgramPerChannel.nwb"
F_CHTR = "sub-H/sub-H_ses-sgramPerChannelPerTrial.nwb"
F_YEO = "sub-H/sub-H_ses-sgramPerYeoPerTrial.nwb"
F_REG = "sub-H/sub-H_ses-sgramPerRegionPerTrial.nwb"
F_FAC = "sub-H/sub-H_ses-sgramNMFFactors.nwb"
F_LOAD = "sub-H/sub-H_ses-sgramNMFLoadings.nwb"
F_CLUST = "sub-H/sub-H_ses-ketChangePermutationClusterTest.nwb"

CODE_ORDER = [0, 2, 4, 5, 1, 3]
LOADING_THRESH = 0.1
PLOT_REGIONS = ['ORB', 'IFG', 'MFG', 'INS', 'ACC', 'MCC', 'PMC', 'MOT', 'SS', 'SMG', 'PHG',
                'STG', 'STS', 'MTG', 'ITG', 'TP', 'HIPP', 'BG', 'AMY', 'THAL ANT', 'THAL POS']
YEO_REGIONS = ['Frontoparietal', 'Default', 'Dorsal Attention', 'Limbic',
               'Ventral Attention', 'Somatomotor']
SPLITS = ['pre_train', 'pre_test', 'post_train', 'post_test', 'inf_train', 'inf_test']

ZENODO_URL = ("https://zenodo.org/api/records/14920570/files/"
              "kauvar-richman-liu-2025_zenodo.zip/content")
ZENODO_MD5 = "bd1fb567121aaf0291337783df57bcfc"


def _str(x):
    return x.decode() if isinstance(x, bytes) else str(x)


# ---------------------------------------------------------------- loading
def load_channel_means():
    """Per-channel trial means (458 channels x 65 freq x 28 time) for the six splits."""
    s = dandi_io.open_h5(F_CH)["scratch"]
    out = {k: s[f"puff_sgram_{k}_trials"][:] for k in SPLITS}
    out["channels"] = np.array([_str(c) for c in s["channel/channel"][:]])
    out["ff"] = s["freq_hz/frequency"][:]
    out["tt"] = s["time_sec/time"][:]
    return out


def load_deposited_nmf():
    """The paper's deposited factors (6 x 65 x 28) and loadings."""
    f = dandi_io.open_h5(F_FAC)["scratch"]
    fac = np.stack([f[f"factor_{i}"][:] for i in range(6)])
    L = dandi_io.open_h5(F_LOAD)["scratch"]
    load = {k: L[f"channel_loading_mtx_{k}"][:] for k in ["pre", "inf", "post"]}
    load["channels"] = np.array([_str(c) for c in L["channel/channel"][:]])
    load["yeo"] = [_str(c) for c in L["yeo/yeo_network"][:]]
    load["yeo_pre"] = L["yeo_loading_mtx_pre"][:]
    load["yeo_inf_minus_pre"] = L["yeo_loading_mtx_inf_minus_pre"][:]
    return fac, load


def open_trial_file():
    h = dandi_io.open_h5(F_CHTR)
    s = h["scratch"]
    names = np.array([_str(c) for c in s["channel/channel"][:]])
    return s, names, s["time_sec/time"][:]


def read_channel_trials(s, idx, session):
    """Per-trial spectrograms of one channel (trials x 65 x 80), NaN padding removed.

    Each channel is a contiguous block in the file, so whole blocks are read.
    """
    x = s[f"puff_sgram_{session}"][idx]
    valid = ~np.isnan(x[:, 0, 0])
    return x[valid]


def load_group_file(path):
    """Per-trial network or region spectrograms with their participant and trial labels."""
    h = dandi_io.open_h5(path)
    sc, a = h["scratch"], h["acquisition"]
    units = [_str(r) for r in sc["region/region"][:]]
    sess_pts, sess_tri = {}, {}
    for r, c, p in zip(a["session_patient_data/region"][:], a["session_patient_data/condition"][:],
                       a["session_patient_data/patient_data"][:]):
        sess_pts[(_str(r), _str(c))] = np.array(re.findall(r"'([^']*)'", _str(p)))
    for r, c, p in zip(a["session_trial_data/region"][:], a["session_trial_data/condition"][:],
                       a["session_trial_data/trial_data"][:]):
        sess_tri[(_str(r), _str(c))] = np.array([int(v) for v in _str(p).strip("[]").split()])
    anat = pd.DataFrame({k: [_str(v) for v in a[f"anatomy_data/{k}"][:]]
                         for k in ["region", "patient", "anat"]})
    anat["nelec"] = a["anatomy_data/nelec"][:]
    return dict(h=h, units=units, sess_pts=sess_pts, sess_tri=sess_tri, anat=anat,
                tt=a["tt/data"][:], ff=a["ff/data"][:])


def load_deposited_clusters():
    s = dandi_io.open_h5(F_CLUST)["scratch"]
    names = sorted({k.rsplit("_", 1)[0] for k in s.keys() if k.endswith("_contour")})
    return {n: (s[f"{n}_change"][:], s[f"{n}_contour"][:]) for n in names}


def fetch_code_labels():
    """Electrode atlas labels from the paper's code record (Zenodo 14920570), md5-checked."""
    r = requests.get(ZENODO_URL, timeout=300)
    r.raise_for_status()
    md5 = hashlib.md5(r.content).hexdigest()
    if md5 != ZENODO_MD5:
        raise ValueError(f"md5 {md5} differs from {ZENODO_MD5}")
    z = zipfile.ZipFile(io.BytesIO(r.content))
    name = [n for n in z.namelist() if n.endswith("anat/pts_ch_labels.pkl")][0]
    return pickle.loads(z.read(name)), md5, name


def yeo_labels(channels, labels):
    """Yeo7 label and atlas region of each [region]_[pt]_[elec] channel (code lines 561 to 576)."""
    yeo, anat = [], []
    for ch in channels:
        _, pt, el = ch.split("_")
        names = np.array([x.upper() for x in labels["pt_elec_names_bipo"][pt]])
        ind = np.where(names == el.upper())[0]
        if len(ind) == 0:
            yeo.append("Missing")
            anat.append("Missing")
        else:
            yeo.append(str(labels["pt_elec_yeos_bipo"][pt][ind][0]))
            anat.append(str(labels["pt_elec_anats_bipo"][pt][ind][0]))
    return np.array(yeo), np.array(anat)


# ---------------------------------------------------------------- NMF
def split_pos_neg(X):
    return np.clip(X, 0, None), np.clip(-X, 0, None)


def fit_nmf_pair(X_flat, k):
    pos, neg = split_pos_neg(X_flat)
    mp = NMF(n_components=k, solver="mu", random_state=1).fit(pos)
    mn = NMF(n_components=k, solver="mu", random_state=1).fit(neg)
    return mp, mn


def components(mp, mn, shape):
    """Factors in the code's fitted order: positive part first, negative part negated."""
    return np.concatenate([mp.components_, -mn.components_]).reshape(-1, *shape)


def transform(mp, mn, X_flat):
    pos, neg = split_pos_neg(X_flat)
    return np.hstack([mp.transform(pos), mn.transform(neg)])


def r2(orig, recon):
    o, r_ = orig.ravel(), recon.ravel()
    return 1 - np.sum((o - r_) ** 2) / np.sum((o - o.mean()) ** 2)


def explained_variance_curve(train_flat, test_flat, ks):
    """Train and test R2 per k (k components per part, 2k in all), two readings for test."""
    rows = []
    for k in ks:
        mp, mn = fit_nmf_pair(train_flat, k)
        H = np.vstack([mp.components_, -mn.components_])
        W_tr = transform(mp, mn, train_flat)
        W_te = transform(mp, mn, test_flat)
        rec_tr = W_tr @ H
        rec_te = W_te @ H
        rows.append(dict(k=k, n_components=2 * k, r2_train=r2(train_flat, rec_tr),
                         r2_test_code=r2(test_flat, rec_tr), r2_test_refit=r2(test_flat, rec_te),
                         iter_pos=mp.n_iter_, iter_neg=mn.n_iter_))
    return pd.DataFrame(rows)


def elbow(x, y):
    """Point of y(x) farthest from the straight line joining its first and last points."""
    x, y = np.asarray(x, float), np.asarray(y, float)
    xn = (x - x[0]) / (x[-1] - x[0])
    yn = (y - y[0]) / (y[-1] - y[0])
    return x[np.argmax(np.abs(yn - xn))]


def description_order(cc, ff, tt):
    """Open G reading (b): factor 1 the positive factor with the largest share of energy above
    50 Hz, factor 2 the negative factor with the largest share below 20 Hz; the other two of
    each part numbered by peak time, earliest first (positive: 0 then 4; negative: 3 then 5).

    cc are the six fitted factors, positive part first (indices 0 to 2), negative 3 to 5.
    """
    e = cc ** 2
    hi = e[:, ff > 50].sum((1, 2)) / e.sum((1, 2))
    lo = e[:, ff < 20].sum((1, 2)) / e.sum((1, 2))
    peak_t = tt[np.argmax(np.abs(cc).max(1), axis=1)]
    pos, neg = [0, 1, 2], [3, 4, 5]
    f1 = pos[int(np.argmax(hi[pos]))]
    f2 = neg[int(np.argmax(lo[neg]))]
    rp = sorted([p for p in pos if p != f1], key=lambda i: peak_t[i])
    rn = sorted([n for n in neg if n != f2], key=lambda i: peak_t[i])
    order = [rp[0], f1, f2, rn[0], rp[1], rn[1]]
    return order, dict(share_above_50Hz=hi, share_below_20Hz=lo, peak_time_s=peak_t)


def threshold_loadings(W_dict, W_prepost, thresh=LOADING_THRESH):
    """Set a factor's loadings to NaN on channels whose pre/post test loading is below thresh."""
    out = {}
    excl = W_prepost < thresh
    for k, W in W_dict.items():
        W = W.copy()
        if W.shape[0] == W_prepost.shape[0]:
            W[excl] = np.nan
        out[k] = W
    return out, excl


def mixedlm_compare(W_a, W_b, pts):
    """Mixed model W ~ X (X = 0 for a, 1 for b), channels grouped by participant.

    Follows decode_utils.compare_nmf_loadings_by_condition; returns coefficient (b - a), p and
    the counts of channels and participants.
    """
    import statsmodels.formula.api as smf
    keep = ~np.isnan(W_a) & ~np.isnan(W_b)
    df = pd.DataFrame(dict(W=np.r_[W_a[keep], W_b[keep]],
                           X=np.r_[np.zeros(keep.sum()), np.ones(keep.sum())],
                           pt=np.r_[pts[keep], pts[keep]]))
    import warnings
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")  # convergence is returned in the result
        res = smf.mixedlm("W ~ X", df, groups=df["pt"]).fit()
    return dict(coef=res.params["X"], p=res.pvalues["X"], n_ch=int(keep.sum()),
                n_pt=int(len(np.unique(pts[keep]))), converged=bool(res.converged))


def group_means(W, groups, names, normalize_row=False):
    """Mean over channels of each group (nanmean), optionally each row divided by its sum."""
    df = pd.DataFrame(W)
    df["g"] = groups
    m = df.groupby("g").agg(np.nanmean).reindex(names)
    if normalize_row:
        m = m.div(m.sum(axis=1, skipna=True), axis=0)
    return m


# ---------------------------------------------------------------- cluster test
def cluster_test(pre, inf, thresh_p=0.01, clust_p=0.01, n_perm=512):
    """Paired cluster test of infusion minus preinfusion trials (trials x freq x time)."""
    import mne
    mne.set_log_level("WARNING")
    X = inf - pre
    th = ss.t.ppf(1 - thresh_p / 2, X.shape[0] - 1)
    T, cl, pv, _ = mne.stats.permutation_cluster_1samp_test(
        X, threshold=th, seed=1, n_permutations=n_perm, n_jobs=1, out_type="mask", verbose=False)
    contour = np.zeros(T.shape)
    for c, p in zip(cl, pv):
        if p < clust_p:
            contour[c] = 1
    minp = float(pv.min()) if len(pv) else np.nan
    return dict(T=T, contour=contour, min_p=minp, n_clusters=len(pv),
                n_signif=int(np.sum(pv < clust_p)), n_trials=X.shape[0],
                p_for_fdr=minp if (len(pv) and minp < clust_p) else 1.0)


def fdr_units(res, units):
    p = np.array([res[u]["p_for_fdr"] for u in units])
    return dict(zip(units, multipletests(p, method="fdr_bh")[1]))


# ---------------------------------------------------------------- resting spectra (figs. S15, S27)
# Approximate tests on the per-participant 20-min LFP files (claims figs15 and figs27).
#
# Timing. The infusion eyepuff session started "at approximately 30 minutes after the infusion
# start" (Methods, iEEG ketamine infusion protocol: "The eyepuff assay was administered preceding
# infusion, at approximately 30 minutes after the infusion start, and 110 minutes after infusion
# start"). Each LFP file runs 10 min before to 10 min after the first puff, so the infusion file
# covers about minutes 20 to 40 of the infusion, and its second half (first puff to the end)
# is the 30 to 40 min window of figs. S15C and the figs27 criterion's fallback. This is an
# assumption ("approximately"); the first half (about 20 to 30 min) and the whole file are run
# as variants.
#
# Multitaper (both claims): time-half-bandwidth 30, 59 tapers, 30-s windows, 15-s stride
# (Methods, Band-limited oscillation detection). The paper gives no spectrogram parameters for
# fig. S15; the same spectrogram is used there (an assumption). Windows are mean-subtracted;
# power is averaged over tapers and over FFT bins into 0.5-Hz bins (bandwidth 2W = 2 Hz).
# Bipolar within-shank channels, notch and puff detection are those of ieeg_cd.load_session.
MT_NW, MT_K, MT_WIN_S, MT_STEP_S = 30, 59, 30.0, 15.0
SEG_S = 180.0              # 3-min segments (Methods)
FBIN = 0.5                 # Hz, width of the frequency bins kept
FOOOF_RANGE = (1.0, 40.0)  # Hz, FOOOF fit range (not given in the paper; an assumption)


def multitaper_spectrogram(x, fs=200, fmax=100.0):
    """Multitaper spectrogram of x (time x channels): returns window start times (s),
    bin centres (Hz) and power (windows x channels x bins, float32)."""
    import scipy.fft as sfft
    from numpy.lib.stride_tricks import sliding_window_view
    from scipy.signal.windows import dpss
    n, step = int(MT_WIN_S * fs), int(MT_STEP_S * fs)
    tap = dpss(n, MT_NW, MT_K).astype(np.float32)
    f = np.fft.rfftfreq(n, 1 / fs)
    centres = np.arange(FBIN, fmax, FBIN)
    bin_of = np.round(f / FBIN).astype(int) - 1          # bin index of each FFT frequency
    ok = (bin_of >= 0) & (bin_of < len(centres))
    counts = np.bincount(bin_of[ok], minlength=len(centres))
    starts = np.arange(0, x.shape[0] - n + 1, step)
    out = np.empty((len(starts), x.shape[1], len(centres)), np.float32)
    for c in range(x.shape[1]):
        w = sliding_window_view(x[:, c].astype(np.float32), n)[::step]
        w = w - w.mean(1, keepdims=True)
        X = sfft.rfft(w[:, None, :] * tap[None], axis=-1)
        P = (np.abs(X) ** 2).mean(1) / fs                 # windows x FFT bins
        acc = np.zeros((len(starts), len(centres)), np.float64)
        np.add.at(acc.T, bin_of[ok], P[:, ok].T)
        out[:, c] = acc / counts
    return starts / fs, centres, out


def rest_session(pt, ses, labels, bad):
    """Spectrogram of one 20-min file over the kept bipolar channels.

    Kept: pairs not out of brain or excluded (ieeg_cd.channel_mask), not containing a contact
    of the code's bad-channel list, and whose bipolar atlas label in anat/pts_ch_labels.pkl
    (pt_elec_anats_bipo) is a single one of the 21 regions of Fig. 3C. Returns the window starts,
    bins, power, channel names and regions, and the first and last puff (s)."""
    import ieeg_cd as cd
    d = cd.load_session(pt, ses)
    names = np.array(labels["pt_elec_names_bipo"][pt])
    anats = np.array([str(a) for a in labels["pt_elec_anats_bipo"][pt]])
    reg = {n.upper(): a for n, a in zip(names, anats)}
    pairs = d["pairs"]
    region = np.array([reg.get(n.upper(), "Missing") for n in pairs["name"]])
    keep = cd.channel_mask(pairs, pt, wm_excluded=True, bad=bad) & np.isin(region, PLOT_REGIONS)
    t, f, S = multitaper_spectrogram(d["lfp"][:, keep])
    p = d["puffs"] / cd.FS
    return dict(session=ses, t=t, f=f, S=S, ch=pairs["name"].values[keep], region=region[keep],
                first_puff=float(p[0]), last_puff=float(p[-1]), n_puffs=len(p),
                duration=d["lfp"].shape[0] / cd.FS, n_pairs=len(pairs))


def window_mask(t, lo, hi):
    """30-s windows lying wholly inside [lo, hi) seconds."""
    return (t >= lo) & (t + MT_WIN_S <= hi + 1e-9)


def zscore_to_baseline(S_base, S_ket, log=True):
    """Each channel and frequency z-scored to the baseline windows, then averaged over the
    ketamine windows (figs. S15B and C). Inputs are windows x channels x bins."""
    if log:
        S_base, S_ket = np.log10(S_base), np.log10(S_ket)
    mu, sd = S_base.mean(0), S_base.std(0)
    return ((S_ket - mu) / sd).mean(0)


def region_magnitude(z, regions, f, fsel):
    """Per region, mean over channels of the mean |z| over the selected bins (claims fig. S15
    reading)."""
    m = np.abs(z[:, fsel]).mean(1)
    return pd.Series(m).groupby(regions).mean()


# ---- band-limited oscillations (fig. S27)
def segment_psds(t, S, lo, hi):
    """Mean spectrum of the 30-s windows inside each whole 3-min segment of [lo, hi)."""
    n = int((hi - lo) // SEG_S)
    return [S[window_mask(t, lo + i * SEG_S, lo + (i + 1) * SEG_S)].mean(0) for i in range(n)]


def flat_spectrum(f, psd):
    """FOOOF ('fixed' aperiodic, default settings) fitted on FOOOF_RANGE; returns the fit
    frequencies and the log10 spectrum minus the aperiodic fit."""
    import contextlib
    with contextlib.redirect_stderr(io.StringIO()):     # fooof prints a deprecation notice
        from fooof import FOOOF
    fm = FOOOF(verbose=False)
    fm.fit(f, psd, list(FOOOF_RANGE))
    return fm.freqs, fm.power_spectrum - fm._ap_fit


def find_spectral_peaks(freqs, flat, prominence):
    """scipy.signal.find_peaks on the aperiodic-removed spectrum, peaks above the aperiodic fit
    with at least the given prominence (log10 units; the paper gives no threshold). Widths at
    half prominence give each peak's frequency interval."""
    from scipy.signal import find_peaks
    pk, pr = find_peaks(flat, height=0, prominence=prominence, width=0, rel_height=0.5)
    df = freqs[1] - freqs[0]
    lo = freqs[0] + pr["left_ips"] * df
    hi = freqs[0] + pr["right_ips"] * df
    return np.c_[freqs[pk], lo, hi, flat[pk]]           # centre, low, high, height


def cluster_peaks(peaks, overlap_of="min", frac=0.8):
    """Cluster peaks (rows: segment, centre, low, high, height) by >= 80 % overlap of peak width
    (single linkage). overlap_of 'min': overlap at least 80 % of the narrower peak's width;
    'max': of the wider one's (both are readings; the Methods do not say). Returns a list of
    index arrays."""
    n = len(peaks)
    if n == 0:
        return []
    lo, hi = peaks[:, 2], peaks[:, 3]
    w = hi - lo
    ov = np.clip(np.minimum(hi[:, None], hi[None]) - np.maximum(lo[:, None], lo[None]), 0, None)
    ref = np.minimum(w[:, None], w[None]) if overlap_of == "min" else np.maximum(w[:, None], w[None])
    adj = ov >= frac * ref
    from scipy.sparse.csgraph import connected_components
    _, lab = connected_components(adj, directed=False)
    return [np.where(lab == k)[0] for k in range(lab.max() + 1)]


def consistent_clusters(peaks, n_seg, overlap_of="min", min_frac=0.4):
    """Clusters present in at least 40 % of the segments: (median centre, per-segment heights)."""
    out = []
    for idx in cluster_peaks(peaks, overlap_of):
        seg = peaks[idx, 0].astype(int)
        useg = np.unique(seg)
        if len(useg) / n_seg < min_frac:
            continue
        h = np.array([peaks[idx, 4][seg == u].max() for u in useg])   # highest peak per segment
        out.append((float(np.median(peaks[idx, 1])), h))
    return out


def ketamine_unique(base_peaks, n_base, ket_peaks, n_ket, overlap_of="min", fmax=10.0,
                    alpha=0.001):
    """Ketamine clusters below fmax that are new (no baseline cluster within 2 Hz) or amplified
    (one-sided rank-sum of peak heights, p < alpha). Returns a list of (centre, kind, p)."""
    base = consistent_clusters(base_peaks, n_base, overlap_of)
    ket = consistent_clusters(ket_peaks, n_ket, overlap_of)
    res = []
    for fc, h in ket:
        if fc >= fmax:
            continue
        near = [hb for fb, hb in base if abs(fb - fc) <= 2.0]
        if not near:
            res.append((fc, "new", np.nan))
            continue
        p = min(ss.mannwhitneyu(h, hb, alternative="greater").pvalue for hb in near)
        if p < alpha:
            res.append((fc, "amplified", p))
    return res


# ---- per-participant data and the two analyses
REST_WINDOWS = {"before": "first half of the file (0 s to the first puff)",
                "after": "second half (first puff to the end), about 30 to 40 min of the infusion",
                "after_no_puffs": "second half from 2 s after the last puff (fig. S15 only)",
                "whole": "the whole 20-min file"}


def _rest_job(args):
    pt, role, ses, labels, bad = args
    return pt, role, rest_session(pt, ses, labels, bad)


def rest_all(participants, labels, bad, max_workers=4):
    """Spectrograms of each participant's preinfusion file (the code's session,
    ieeg_cd.PRE_SESSION_CODE), infusion and postinfusion files, and of SD245's Preinfusion file
    (ieeg_cd.PRE_SESSION_ALT, key 'pre_alt'), one file per process."""
    from concurrent.futures import ProcessPoolExecutor
    import ieeg_cd as cd
    jobs = []
    for pt in participants:
        lab = {k: {pt: labels[k][pt]} for k in ("pt_elec_names_bipo", "pt_elec_anats_bipo")}
        sess = {"pre": cd.PRE_SESSION_CODE[pt], "inf": "Infusion", "post": "Postinfusion"}
        if cd.PRE_SESSION_ALT[pt] != cd.PRE_SESSION_CODE[pt]:
            sess["pre_alt"] = cd.PRE_SESSION_ALT[pt]
        jobs += [(pt, role, ses, lab, bad) for role, ses in sess.items()]
    out = {pt: {} for pt in participants}
    with ProcessPoolExecutor(max_workers) as ex:
        for pt, role, R in ex.map(_rest_job, jobs):
            out[pt][role] = R
    for pt, d in out.items():
        for k, v in d.items():
            assert (v["ch"] == d["inf"]["ch"]).all(), (pt, k, "channel lists differ")
    return out


def window_bounds(R, which):
    """[lo, hi) seconds of a named part of a 20-min file (REST_WINDOWS). The first puff is
    rounded to the 15-s window grid (it lies at 600.0 s in every file)."""
    fp = round(R["first_puff"] / MT_STEP_S) * MT_STEP_S
    return {"before": (0.0, fp), "after": (fp, R["duration"]),
            "after_no_puffs": (R["last_puff"] + 2.0, R["duration"]),
            "whole": (0.0, R["duration"])}[which]


def s15_magnitudes(rest, base_key, base_win, ket_win, log=True, fband=(1.0, 100.0),
                   notch=(58.0, 62.0)):
    """Fig. S15 magnitude per participant (rows) and region (columns)."""
    out = {}
    for pt, d in rest.items():
        B, K = d.get(base_key, d["pre"]), d["inf"]
        mb = window_mask(B["t"], *window_bounds(B, base_win))
        mk = window_mask(K["t"], *window_bounds(K, ket_win))
        f = K["f"]
        fsel = (f >= fband[0]) & (f <= fband[1]) & ~((f >= notch[0]) & (f <= notch[1]))
        z = zscore_to_baseline(B["S"][mb], K["S"][mk], log=log).astype(float)
        out[pt] = region_magnitude(z, K["region"], f, fsel)
    return pd.DataFrame(out).T


def s15_verdict(mag):
    """Median over participants per region, ranking, and the two parts of the criterion."""
    med = mag.median(0).sort_values(ascending=False)
    rank = {r: int(i) + 1 for i, r in enumerate(med.index)}
    m = med.median()
    return dict(median=med, rank=rank, n_regions=len(med), orb_first=med.index[0] == "ORB",
                frontal_above=all(med[r] > m for r in ["ORB", "IFG", "MFG"]),
                n_pts=mag.notna().sum(0))


def _flats_job(args):
    import warnings
    warnings.filterwarnings("ignore")  # fooof's deprecation notice
    key, f, psd = args
    fl = [flat_spectrum(f, psd[c]) for c in range(psd.shape[0])]
    return key, (fl[0][0], np.array([x[1] for x in fl]))


def s27_flats(rest, segments, max_workers=4):
    """FOOOF-flattened spectra of every kept channel and 3-min segment.

    segments: {session key: [window names]}. Returns {(pt, session, segment start s):
    (freqs, flats channels x bins)}, each segment computed once, in parallel processes."""
    from concurrent.futures import ProcessPoolExecutor
    jobs = {}
    for pt, d in rest.items():
        for key, wins in segments.items():
            if key not in d:
                continue
            R = d[key]
            for w in wins:
                for s0 in seg_starts(R, w):
                    if (pt, key, s0) not in jobs:
                        psd = R["S"][window_mask(R["t"], s0, s0 + SEG_S)].mean(0)
                        jobs[(pt, key, s0)] = (R["f"], psd)
    with ProcessPoolExecutor(max_workers) as ex:
        return dict(ex.map(_flats_job, [(k, f, p) for k, (f, p) in jobs.items()]))


def seg_starts(R, w):
    lo, hi = window_bounds(R, w)
    return [lo + i * SEG_S for i in range(int((hi - lo) // SEG_S))]


_PEAKS = {}


def _channel_peaks(flats, key, c, prominence):
    k = (key, c, prominence)
    if k not in _PEAKS:
        fr, fl = flats[key]
        _PEAKS[k] = find_spectral_peaks(fr, fl[c], prominence)
    return _PEAKS[k]


def s27_channels(rest, flats, base, ket_win, prominence, overlap_of, ket_key="inf"):
    """Per participant, channels with a ketamine-unique oscillation below 10 Hz.

    base: list of (session key, window) pooled as the baseline (Methods: pre- and post-infusion
    windows combined). ket_key names the session tested against it (the infusion file; the
    postinfusion file gives a reference without ketamine). Returns {pt: dict(n_ch, n_osc,
    n_base_seg, n_ket_seg, hits)}, hits a list of (channel, region, [(centre Hz, kind, p)])."""
    out = {}
    for pt, d in rest.items():
        def keys_of(key, w):
            key = key if key in d else "pre"
            return [(pt, key, s0) for s0 in seg_starts(d[key], w)]
        b_keys = [k for key, w in base for k in keys_of(key, w)]
        k_keys = keys_of(ket_key, ket_win)
        n_ch = len(d["inf"]["ch"])
        hits = []
        for c in range(n_ch):
            pb = _stack([_channel_peaks(flats, k, c, prominence) for k in b_keys])
            pk = _stack([_channel_peaks(flats, k, c, prominence) for k in k_keys])
            u = ketamine_unique(pb, len(b_keys), pk, len(k_keys), overlap_of)
            if u:
                hits.append((d["inf"]["ch"][c], d["inf"]["region"][c], u))
        out[pt] = dict(n_ch=n_ch, n_osc=len(hits), n_base_seg=len(b_keys), n_ket_seg=len(k_keys),
                       hits=hits)
    return out


def _stack(per_segment):
    """Rows (segment, centre, low, high, height) from per-segment peak arrays."""
    rows = [np.c_[np.full(len(p), i), p] for i, p in enumerate(per_segment) if len(p)]
    return np.vstack(rows) if rows else np.zeros((0, 5))


def label_permutation(n_osc, n_ch, high):
    """Difference in channel fraction (high minus low CADSS) and its exact permutation p over
    every assignment of the high label to the same number of participants (the Methods shuffle
    the label across participants without replacement, 10,000 times; with 7 participants all
    assignments can be enumerated)."""
    from itertools import combinations
    pts = list(n_osc)
    o = np.array([n_osc[p] for p in pts], float)
    n = np.array([n_ch[p] for p in pts], float)
    h = np.array([p in high for p in pts])

    if h.all() or not h.any():
        return np.nan, np.nan, 0

    def diff(m):
        return o[m].sum() / n[m].sum() - o[~m].sum() / n[~m].sum()
    obs = diff(h)
    null = []
    for comb in combinations(range(len(pts)), int(h.sum())):
        m = np.zeros(len(pts), bool)
        m[list(comb)] = True
        null.append(diff(m))
    null = np.array(null)
    return obs, float(np.mean(null >= obs - 1e-12)), len(null)
