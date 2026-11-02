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
