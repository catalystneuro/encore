"""Loading and measures for Wei et al. (2023) on dandiset 000021 (Allen Brain Observatory Visual
Coding Neuropixels, Brain Observatory 1.1 stimulus set).

Wei, Nandi, Jia, Siegle, Denman, Lee, Buchin, Van Geit, Mosher, Olsen & Anastassiou (2023),
Nature Communications 14, 2344, doi:10.1038/s41467-023-37844-8.

Files are streamed from the archive at the pinned version with remfile and h5py; nothing is
written to disk. The paper's code (https://github.com/yinawei/Mouse_V1_EAP_Analysis at commit
1e35126f1e521b4c98e9ba5fd6a4a8abce70530a, "the code" below) is cited by file and function.

Where the parameters come from:

- Sessions: the 25 wild-type sessions of NP_EAP_FeatureAnalysis.ipynb, cell 3 (the claims file,
  opening comment); 13 of them are in this dandiset.
- Units: VISp units, by the CCF structure of the unit's peak channel in the electrodes table
  (Methods, "we analyzed recordings from the primary visual cortex (V1)"). Isolation is open
  (claim fig1d-unit-count): reading (a) the AllenSDK default filter (isi_violations < 0.5,
  amplitude_cutoff < 0.1, presence_ratio > 0.9) on units of quality "good"; reading (b) every
  VISp unit the units table lists, of quality "good" or "noise", as the criterion words it;
  reading (c), an assumption used for the claims after fig1d-unit-count, reading (a) with at
  least 100 spikes in the first 5-min gray screen (see assemble). The code's list of 38
  excluded unit ids is applied in all three (NP_EAP_FeatureAnalysis.ipynb, cell 4).
- Waveforms: the 40 channels from the peak channel minus 20 to plus 19 of the units table's
  mean waveforms (the code's per-session arrays are units x 82 samples x 40 channels with the
  peak at channel 20, as its check maxCh0 != 10 on every second channel implies). Units whose
  window does not fit on the 384 channels are dropped and counted (a standard choice; the code
  does not show how such units were handled). The values are in microvolts although the file
  says volts (amplitudes of 15 to 300 in the code's exclusions fit microvolts).
- Features (TPW, REP, 1/V below and above, spread, symmetry index), exclusions and K-means
  are ported from ecp_func.py and NP_EAP_FeatureAnalysis.ipynb cells 5 to 21, as the claims
  file's opening comment lists them.
- Spike-train measures: Methods, "Single unit firing properties" (units with EAP amplitude
  above 50 uV and at least 100 spikes, rate N / T, CV, LV), with the period of each claim's
  criterion.
- Phase locking: Methods, "Phase-locking analysis" (bands, Hilbert phase, Rayleigh p < 0.001,
  at most 10,000 spikes); the band-pass is ecp_func.butter_bandpass_filter (5th order, sosfiltfilt)
  as the claims file reads it.
- Opto-tagging: Methods, "Detection of opto-tagged neurons" (1 ms bins, 10 ms square pulses,
  spikes 2 to 8 ms after onset, above 25 Hz and 2.5 times the rate just before onset).
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache

import h5py
import numpy as np
import pandas as pd
import remfile
from scipy import fft as sp_fft
from scipy import signal, stats
from scipy.interpolate import make_interp_spline

DANDISET_ID = "000021"
DANDISET_VERSION = "0.251116.2246"
API = "https://api.dandiarchive.org/api"

# NP_EAP_FeatureAnalysis.ipynb, cell 3
PAPER_WT_SESSIONS = [int(x) for x in """
    732592105 739448407 744228101 750332458 750749662 754312389 754829445 757216464 757970808
    759883607 761418226 763673393 766640955 767871931 768515987 771160300 771990200 774875821
    778240327 778998620 779839471 781842082 793224716 799864342 847657808""".split()]
# NP_EAP_FeatureAnalysis.ipynb, cell 4
BAD_UNITS = {int(x) for x in """
    915960371 915961088 915960802 915960838 951868026 951868229 951868527 951869594 951816073
    951002808 951814989 951815653 951815724 951815709 951816276 951816492 951877391 951796229
    951768170 951013844 951026044 951027930 951896781 951896911 951800909 950938909 950935800
    950929267 950927995 950935732 950929283 950930487 950931566 951801768 951762773 951095926
    951768557 950928046""".split()}

FS_HZ = 30000.0
T_STA = np.arange(82) / FS_HZ * 1000 - 0.6      # ms, cell 5
DIST = np.arange(-100, 101, 20)                  # um, cell 5
TH_AMP = 5                                       # Th, cell 5

BANDS_RESULTS = {"theta": (3, 8), "alpha": (8, 12.5), "beta": (12.5, 30),
                 "low_gamma": (30, 50), "high_gamma": (50, 90)}   # Results
BANDS_METHODS = {"theta": (3, 8), "alpha": (8, 12), "beta": (12, 30),
                 "low_gamma": (30, 50), "high_gamma": (50, 90)}   # Methods


# ----------------------------------------------------------------------------- archive

@lru_cache(maxsize=1)
def _dandiset():
    from dandi.dandiapi import DandiAPIClient
    return DandiAPIClient().get_dandiset(DANDISET_ID, DANDISET_VERSION)


@lru_cache(maxsize=1)
def assets() -> list[dict]:
    """Every asset of the pinned version (path, asset_id, size)."""
    return [{"path": a.path, "asset_id": a.identifier, "size": a.size}
            for a in _dandiset().get_assets()]


def session_paths() -> dict[int, str]:
    """Session id -> path of its session NWB file."""
    return {int(a["path"].split("ses-")[1].split(".")[0]): a["path"] for a in assets()
            if "probe" not in a["path"] and a["path"].endswith(".nwb")}


def probe_paths(session: int) -> dict[int, str]:
    """Probe id -> path of the session's probe (LFP) file."""
    out = {}
    for a in assets():
        p = a["path"]
        if f"ses-{session}_probe-" in p:
            out[int(p.split("probe-")[1].split("_")[0])] = p
    return out


def s3_url(path: str) -> str:
    return _dandiset().get_asset_by_path(path).get_content_url(follow_redirects=1,
                                                                 strip_query=True)


def open_nwb(path: str) -> h5py.File:
    return h5py.File(remfile.File(s3_url(path)), "r")


# ----------------------------------------------------------------------------- units

def session_info(f: h5py.File) -> dict:
    s = f["general/subject"]
    return {"genotype": s["genotype"][()].decode(), "sex": s["sex"][()].decode(),
            "subject_id": s["subject_id"][()].decode()}


def visp_units(f: h5py.File) -> pd.DataFrame:
    """Units table of the units whose peak channel is in VISp, with their peak channel."""
    U = f["units"]
    E = f["general/extracellular_ephys/electrodes"]
    el = pd.DataFrame({"peak_channel_id": E["id"][:], "location": E["location"][:].astype(str),
                       "local_index": E["local_index"][:], "probe_id": E["probe_id"][:],
                       "vpos": E["probe_vertical_position"][:],
                       "hpos": E["probe_horizontal_position"][:]})
    cols = ["peak_channel_id", "quality", "isi_violations", "amplitude_cutoff", "presence_ratio",
            "firing_rate", "amplitude", "snr"]
    df = pd.DataFrame({c: U[c][:] for c in cols})
    df["quality"] = df["quality"].astype(str)
    df["unit_id"] = U["id"][:]
    df["row"] = np.arange(len(df))
    df = df.merge(el, on="peak_channel_id", how="left")
    df = df[df.location == "VISp"].copy()
    df["allensdk_filter"] = ((df.isi_violations < 0.5) & (df.amplitude_cutoff < 0.1)
                             & (df.presence_ratio > 0.9))
    return df.set_index("unit_id")


def read_waveforms(f: h5py.File, rows) -> dict[int, np.ndarray]:
    """Mean waveform (384 channels x 82 samples, microvolts) for each units-table row."""
    U = f["units"]
    idx = U["waveform_mean_index"][:]
    ds = U["waveform_mean"]
    out = {}
    for r in rows:
        start = 0 if r == 0 else idx[r - 1]
        out[r] = ds[start:idx[r]]
    return out


def read_spikes(f: h5py.File, rows) -> dict[int, np.ndarray]:
    U = f["units"]
    idx = U["spike_times_index"][:]
    ds = U["spike_times"]
    return {r: ds[(0 if r == 0 else idx[r - 1]):idx[r]] for r in rows}


def window40(wave384: np.ndarray, local_peak: int):
    """The 40 channels peak-20 to peak+19 as 82 x 40 (the code's array layout), or None."""
    lo = local_peak - 20
    if lo < 0 or lo + 40 > wave384.shape[0]:
        return None
    return wave384[lo:lo + 40].T


# ----------------------------------------------------------------------------- EAP features
# Ported from ecp_func.py (functions of the same names) and NP_EAP_FeatureAnalysis.ipynb cell 7.

def _spline(x, y, xs):
    return make_interp_spline(x, y)(xs)


def butter_highpass_filter(data, cutoff=300, fs=FS_HZ, order=5):
    b, a = signal.butter(order, cutoff / (0.5 * fs), btype="high")
    return signal.filtfilt(b, a, data)


def butter_bandpass_filter(data, low, high, fs, order=5):
    sos = signal.butter(order, [low / (0.5 * fs), high / (0.5 * fs)], btype="band", output="sos")
    return signal.sosfiltfilt(sos, data, axis=0)


def _neg_peak_indx(w, t):
    ind = np.where((t >= -1) & (t <= 2.5))[0]
    return w[ind].argmin() + ind[0]


def _nearest(a, v):
    return np.abs(a - v).argmin()


def _calc_width(w0, t0):
    w0 = w0 - w0[0]
    t = np.linspace(t0.min(), t0.max(), 10000)
    w = _spline(t0, w0, t)
    i1 = _neg_peak_indx(w, t)
    i2 = w[i1:].argmax() + i1
    amp = abs(w[i1])
    m1 = _nearest(w[:i1], -0.5 * amp) if i1 > 0 else 0
    m2 = _nearest(w[i1:i2], -0.5 * amp) + i1 if i2 > i1 else i1
    return amp, t[m2] - t[m1], t[i2] - t[i1], t[i1]


def cal_EAP_features(t, ve, th=0.01):
    n = ve.shape[0]
    A, W, TPW, tneg = (np.zeros(n) for _ in range(4))
    for i in range(n):
        e = ve[i] - ve[i, 0]
        if abs(e.min()) >= th:
            A[i], W[i], TPW[i], tneg[i] = _calc_width(e, t)
        else:
            A[i], W[i], TPW[i], tneg[i] = abs(e.min()), np.nan, np.nan, np.nan
    return A, W, TPW, tneg


def cal_one_ch_features(t0, w0):
    w0 = w0 - w0[0]
    t = np.linspace(t0.min(), t0.max(), 10000)
    w = _spline(t0, w0, t)
    i1 = _neg_peak_indx(w, t)
    i2 = w[i1:].argmax() + i1
    i3 = w[i2:].argmin() + i2
    amp = abs(w[i1])
    tpw = t[i2] - t[i1]
    pt = abs(w[i2]) / abs(w[i1])
    m1 = _nearest(w[:i1], -amp / 2) if i1 > 0 else 0
    m2 = _nearest(w[i1:i2], -amp / 2) + i1 if i2 > i1 else i1
    m3 = _nearest(w[i2:i3], w[i2] / 2) + i2 if i3 > i2 else i2
    rep = t[m3] - t[i2]
    width = t[m2] - t[m1]
    sel = (t >= t[i1]) & (t <= t[i1] + 0.03)
    rslope = stats.linregress(t[sel], w[sel]).slope
    return [amp, width, tpw, rslope, rep]


def _outlier_below(x, y, th, npnt=3):
    # ecp_func.outlier_below: its flag is never set, so every point off the line is dropped
    idx = np.arange(-npnt + 1, 1) + len(x) - 1
    r = stats.linregress(x[idx], y[idx])
    for i in range(len(y) - 1 - npnt, -1, -1):
        if abs(y[i] - (r.slope * x[i] + r.intercept)) > th:
            y[i] = np.nan
    return y


def _outlier_above(x, y, th, npnt=3):
    # ecp_func.outlier_above: after the first point off the line, all further points are dropped
    idx = np.arange(npnt)
    r = stats.linregress(x[idx], y[idx])
    flag = 0
    for i in range(npnt - 1, len(y)):
        if flag == 1:
            y[i] = np.nan
        elif abs(y[i] - (r.slope * x[i] + r.intercept)) > th:
            y[i] = np.nan
            flag = 1
    return y


def _linregress(x, y):
    m = ~np.isnan(x) & ~np.isnan(y)
    if m.sum() < 2:
        return np.nan, np.nan
    r = stats.linregress(x[m], y[m])
    return r.slope, r.intercept


def _spread2(A0, d0, th=0.12):
    d = np.linspace(d0.min(), d0.max(), 10000)
    A = _spline(d0, A0, d)
    mid = A.max() * th
    am = A.argmax()
    i1 = _nearest(A[:am], mid) if am > 0 else 0
    i2 = _nearest(A[am:], mid) + am
    return abs(d[i1]), abs(d[i2])


def unit_features(eap82x40: np.ndarray) -> dict:
    """The code's features of one unit from its 82 x 40 mean waveform (cell 7)."""
    n_rows = 20
    one = np.array([butter_highpass_filter(eap82x40[:, i * 2]) for i in range(n_rows)])
    max_ch = 10
    max_ch0 = np.unravel_index(one.argmin(), one.shape)[0]
    dist0 = np.arange(n_rows) * 20.0 - max_ch * 20.0
    A, W, TPW, tneg = cal_EAP_features(T_STA, one, 0.01)
    tneg = tneg - tneg[max_ch]
    with np.errstate(invalid="ignore"):
        dth = 100
        ib = np.where((dist0 <= 0) & (dist0 >= -dth) & (A >= 0.0001))[0]
        ia = np.where((dist0 >= 0) & (dist0 <= dth) & (A >= 0.0001))[0]
        for arr in (W, TPW, tneg):
            arr[ib] = _outlier_below(dist0[ib], arr[ib].copy(), 0.3)
            arr[ia] = _outlier_above(dist0[ia], arr[ia].copy(), 0.3)
    peak = one[max_ch] / abs(one[max_ch].min())
    peak = peak - peak[0]
    amp, width, tpw, rslope, rep = cal_one_ch_features(T_STA, one[max_ch])
    # cal_multi_ch_features
    thr = max(A[max_ch] * 0.005, TH_AMP)
    ib = np.where((dist0 <= 0) & (dist0 >= -dth) & (A >= thr))[0]
    ia = np.where((dist0 >= 0) & (dist0 <= dth) & (A >= thr))[0]
    if len(ib) < 3:
        ib = max_ch + np.arange(-2, 1)
    if len(ia) < 3:
        ia = max_ch + np.arange(3)
    wb, _ = _linregress(dist0[ib], W[ib])
    wa, _ = _linregress(dist0[ia], W[ia])
    pb, _ = _linregress(dist0[ib], tneg[ib])
    pa, _ = _linregress(dist0[ia], tneg[ia])
    sb, sa = _spread2(A, dist0, 0.12)
    tt = np.linspace(T_STA.min(), T_STA.max(), 10000)
    neg_time = tt[_neg_peak_indx(_spline(T_STA, peak, tt), tt)]
    return {"A": amp, "W": width, "TPW": tpw, "PTratio": rslope, "REP": rep,
            "spread_below": sb, "spread_above": sa, "W_below": wb * 1000, "W_above": wa * 1000,
            "PL_below": pb * 1000, "PL_above": pa * 1000, "peak_off_centre": max_ch0 != max_ch,
            "neg_time": neg_time}


def symmetry_index(inv_below, inv_above):
    """Methods eq. 1, distance of (1/V below, 1/V above) from y = -x (ecp_func.sym_dist_fc)."""
    return np.abs(np.asarray(inv_below) + np.asarray(inv_above)) / np.sqrt(2)


def outlier_index(x, nan_aware=True):
    """ecp_func.outlier_index: values beyond 3 SD of the mean. The code uses np.mean and
    np.std, so one NaN disables the exclusion for that feature; nan_aware=True takes the mean
    and SD over the values present (an assumption, see code_exclusions)."""
    x = np.asarray(x, float)
    m, s = (np.nanmean(x), np.nanstd(x)) if nan_aware else (np.mean(x), np.std(x))
    return np.where((x > m + 3 * s) | (x < m - 3 * s))[0]


def code_exclusions(df: pd.DataFrame, nan_aware: bool = True) -> pd.Series:
    """True for the units the code keeps (NP_EAP_FeatureAnalysis.ipynb, cell 8).

    Assumption: the 3 SD exclusions ignore NaN. The Source Data features have no NaN, so on the
    paper's units the code's np.mean and np.std excluded outliers; here 1/V above and W above are
    NaN for a few units (too few channels left after the code's outlier step), which would turn
    the code's exclusion off for those features. nan_aware=False runs the code literally."""
    out = set()
    for c in ["W", "TPW", "REP", "W_below", "W_above", "PL_below", "PL_above"]:
        out |= set(outlier_index(df[c].values, nan_aware))
    pos = np.arange(len(df))
    bad = (df.peak_off_centre.values | (np.abs(df.neg_time.values) > 0.1)
           | (df.A.values < 15) | (df.A.values > 300) | np.isin(pos, list(out)))
    return pd.Series(~bad, index=df.index)


# ----------------------------------------------------------------------------- clustering

def pre_process(X):
    """ecp_func.pre_process: median imputation, then z-score."""
    X = np.array(X, dtype=float)
    med = np.nanmedian(X, axis=0)
    i = np.where(np.isnan(X))
    X[i] = np.take(med, i[1])
    return (X - X.mean(0)) / X.std(0)


def _alpha(k, nd):
    return 1 - 3 / (4 * nd) if k == 2 else _alpha(k - 1, nd) + (1 - _alpha(k - 1, nd)) / 6


def selection_k(X, numk=9, n_init=1000, seed=10):
    """ecp_func.selectionK_kmeans: WCSS and f(K) for K = 1..numk."""
    from sklearn.cluster import KMeans
    nd = X.shape[1]
    wcss, fk, prev = [], [], 0
    for k in range(1, numk + 1):
        s = KMeans(n_clusters=k, init="k-means++", n_init=n_init, random_state=seed).fit(X).inertia_
        wcss.append(s)
        fk.append(1.0 if (k == 1 or prev == 0) else s / (_alpha(k, nd) * prev))
        prev = s
    return np.array(wcss), np.array(fk)


def find_elbow(wcss):
    """ecp_func.findElbow; returns K (index + 1)."""
    rate = np.diff(wcss)
    return int((rate[:-1] / rate[1:]).argmax() + 1) + 1


def kmeans_labels(X, k, seed, n_init=1000):
    from sklearn.cluster import KMeans
    return KMeans(n_clusters=k, init="k-means++", n_init=n_init, random_state=seed).fit(X).labels_


# ----------------------------------------------------------------------------- spike trains

def isi_stats(parts) -> dict:
    """CV (Methods eq. 7) and LV (Methods eq. 8, Shinomoto's local variation) of ISIs, given
    as one array per interval (isis_within). CV is over the pooled ISIs; LV is over pairs of
    consecutive ISIs of the same interval, so no pair straddles two intervals."""
    parts = [np.asarray(x, float) for x in parts]
    isis = np.concatenate(parts) if parts else np.zeros(0)
    if len(isis) < 2:
        return {"cv": np.nan, "lv": np.nan}
    terms = [((x[:-1] - x[1:]) / (x[:-1] + x[1:])) ** 2 for x in parts if len(x) > 1]
    n_pairs = sum(len(t) for t in terms)
    lv = 3.0 / n_pairs * np.sum(np.concatenate(terms)) if n_pairs else np.nan
    return {"cv": np.std(isis) / np.mean(isis), "lv": lv}


def isis_within(spikes: np.ndarray, starts, stops) -> list:
    """ISIs between consecutive spikes inside each interval, one array per interval with at
    least two spikes (pairs never cross intervals)."""
    out = []
    for s, e in zip(starts, stops):
        x = spikes[np.searchsorted(spikes, s):np.searchsorted(spikes, e)]
        if len(x) > 1:
            out.append(np.diff(x))
    return out


def count_within(spikes, starts, stops) -> int:
    return int(sum(np.searchsorted(spikes, e) - np.searchsorted(spikes, s)
                   for s, e in zip(starts, stops)))


def dg_metrics(spikes: np.ndarray, dg: pd.DataFrame) -> dict:
    """f1/f0, modulation index and lifetime sparseness of drifting gratings as AllenSDK v2.16.2
    defines them (allensdk/brain_observatory/ecephys/stimulus_analysis/drifting_gratings.py,
    f1_f0 and modulation_index, and stimulus_analysis.py, lifetime_sparseness and
    _get_preferred_condition): 2 s trials, 1 ms bins, the preferred condition the one of
    highest mean spike count, the blank condition left out."""
    from scipy.fft import fft
    dg = dg[dg.orientation.notna() & dg.temporal_frequency.notna()]
    edges = np.arange(0, 2.0, 0.001)
    starts = dg.start_time.values
    counts = np.array([np.histogram(spikes[np.searchsorted(spikes, s):np.searchsorted(spikes, s + 2.0)] - s,
                                    bins=edges)[0] for s in starts])
    # whole-presentation counts (presentationwise statistics count over start to stop)
    total = np.array([np.searchsorted(spikes, e) - np.searchsorted(spikes, s)
                      for s, e in zip(dg.start_time.values, dg.stop_time.values)])
    cond = list(zip(dg.orientation.values, dg.temporal_frequency.values))
    keys = sorted(set(cond))
    cidx = np.array([keys.index(c) for c in cond])
    mean_cnt = np.array([total[cidx == k].mean() for k in range(len(keys))])
    sum_cnt = np.array([total[cidx == k].sum() for k in range(len(keys))])
    pref = int(mean_cnt.argmax())
    tf = keys[pref][1]
    arr = counts[cidx == pref]
    trial_duration = edges[:-1].max()           # as AllenSDK: time_relative_to_stimulus_onset.max()
    num_trials, num_bins = arr.shape
    cyc = int(tf * trial_duration)
    bpc = int(num_bins / cyc) if cyc > 0 else 0
    f1f0 = np.nan
    if bpc > 0:
        a = arr[:, :cyc * bpc].reshape(num_trials, cyc, bpc).mean(1)
        amp = 2 * np.abs(fft(a, bpc, axis=1)) / bpc
        f0, f1 = 0.5 * amp[:, 0], amp[:, 1]
        sel = f0 > 0
        if sel.any():
            f1f0 = np.nanmean(f1[sel] / f0[sel])
    psth = arr.mean(0)
    fr, psd = signal.welch(psth, fs=1000.0, nperseg=1024)
    mpsd = psd.mean()
    if mpsd == 0:
        mi = 0.0
    else:
        i = np.searchsorted(fr, tf)
        mi = abs((psd[i] - mpsd) / np.sqrt(np.mean(psd ** 2) - mpsd ** 2)) if i < psd.size else np.nan
    n = len(sum_cnt)
    ls = ((1 - (1 / n) * sum_cnt.sum() ** 2 / np.sum(sum_cnt ** 2)) / (1 - 1 / n)
          if np.sum(sum_cnt ** 2) > 0 else np.nan)
    return {"f1_f0_dg": f1f0, "mod_idx_dg": mi, "lifetime_sparseness_dg": ls}


# ----------------------------------------------------------------------------- circular statistics
# Ported from pycircstat (https://github.com/circstat/pycircstat), which the Methods name.

def resultant_length(alpha):
    return np.abs(np.mean(np.exp(1j * alpha)))


def circ_kappa(alpha):
    """pycircstat.kappa: the von Mises concentration estimate from the resultant length."""
    n = len(alpha)
    R = resultant_length(alpha)
    if R < 0.53:
        k = 2 * R + R ** 3 + 5 * R ** 5 / 6
    elif R < 0.85:
        k = -0.4 + 1.39 * R + 0.43 / (1 - R)
    else:
        k = 1 / (R ** 3 - 4 * R ** 2 + 3 * R)
    if 1 < n < 15:
        k = max(k - 2 / (n * k), 0) if k < 2 else (n - 1) ** 3 * k / (n ** 3 + n)
    return k


def rayleigh_p(alpha):
    """pycircstat.rayleigh p-value."""
    n = len(alpha)
    Rn = resultant_length(alpha) * n
    return float(np.exp(np.sqrt(1 + 4 * n + 4 * (n ** 2 - Rn ** 2)) - (1 + 2 * n)))


def mean_phase_deg(alpha):
    """Circular mean in degrees, 0 to 360, with the Hilbert phase convention (0 at the peak,
    180 at the trough, as the Methods mark it)."""
    return float(np.degrees(np.angle(np.mean(np.exp(1j * alpha)))) % 360)


def phase_lock(phases) -> dict:
    """Rayleigh p, pycircstat kappa, resultant length and mean phase of spike phases."""
    n = len(phases)
    if n < 2:
        return {"n": n, "p": np.nan, "kappa": np.nan, "R": np.nan, "phase": np.nan}
    m = np.mean(np.exp(1j * phases))
    R = float(np.abs(m))
    if R < 0.53:
        k = 2 * R + R ** 3 + 5 * R ** 5 / 6
    elif R < 0.85:
        k = -0.4 + 1.39 * R + 0.43 / (1 - R)
    else:
        k = 1 / (R ** 3 - 4 * R ** 2 + 3 * R)
    if 1 < n < 15:
        k = max(k - 2 / (n * k), 0) if k < 2 else (n - 1) ** 3 * k / (n ** 3 + n)
    Rn = R * n
    p = float(np.exp(np.sqrt(1 + 4 * n + 4 * (n ** 2 - Rn ** 2)) - (1 + 2 * n)))
    return {"n": n, "p": p, "kappa": k, "R": R, "phase": float(np.degrees(np.angle(m)) % 360)}


# ----------------------------------------------------------------------------- statistics

def holm(p):
    p = np.asarray(p, float)
    o = np.argsort(p)
    m = len(p)
    adj = np.empty(m)
    run = 0
    for r, i in enumerate(o):
        run = max(run, (m - r) * p[i])
        adj[i] = min(run, 1.0)
    return adj


def kruskal_holm(groups: dict) -> dict:
    """Kruskal-Wallis across groups, then Holm-corrected two-sided Mann-Whitney U tests
    (the non-normal branch of ecp_func.three_sample_test)."""
    names = list(groups)
    vals = [np.asarray(groups[k], float)[~np.isnan(np.asarray(groups[k], float))] for k in names]
    H, p = stats.kruskal(*vals)
    pairs = [(i, j) for i in range(len(names)) for j in range(i + 1, len(names))]
    raw = [stats.mannwhitneyu(vals[i], vals[j], alternative="two-sided").pvalue for i, j in pairs]
    adj = holm(raw)
    return {"H": H, "p": p, "post": {f"{names[i]}-{names[j]}": a for (i, j), a in zip(pairs, adj)},
            "medians": {k: float(np.median(v)) for k, v in zip(names, vals)},
            "n": {k: len(v) for k, v in zip(names, vals)}}


def two_prop_z(k1, n1, k2, n2):
    """Two-sample z test for proportions (pooled), two-sided."""
    p = (k1 + k2) / (n1 + n2)
    se = np.sqrt(p * (1 - p) * (1 / n1 + 1 / n2))
    if se == 0:
        return np.nan, 1.0
    z = (k1 / n1 - k2 / n2) / se
    return z, 2 * stats.norm.sf(abs(z))


def circ_ww_or_mw(a, b):
    """Two-sided Mann-Whitney U test on preferred phases in degrees (the legends' test)."""
    return stats.mannwhitneyu(a, b, alternative="two-sided").pvalue


# ----------------------------------------------------------------------------- one session

def _table(f, name) -> pd.DataFrame:
    g = f[name]
    cols = {}
    for k in g:
        d = g[k]
        if not isinstance(d, h5py.Dataset) or d.ndim != 1 or k in ("timeseries", "tags", "id"):
            continue
        if k.endswith("_index") or len(d) != len(g["start_time"]):
            continue
        v = d[:]
        cols[k] = v.astype(str) if v.dtype == object else v
    return pd.DataFrame(cols)


def _lfp_channels(pf: h5py.File):
    """LFP series of a probe file: (dataset, timestamps dataset, electrodes frame)."""
    acq = pf["acquisition"]
    key = next(k for k in acq if k.endswith("_lfp"))
    grp = acq[key][f"{key}_data"] if f"{key}_data" in acq[key] else acq[key]
    E = pf["general/extracellular_ephys/electrodes"]
    el = pd.DataFrame({"id": E["id"][:], "vpos": E["probe_vertical_position"][:],
                       "hpos": E["probe_horizontal_position"][:],
                       "location": E["location"][:].astype(str)})
    rows = grp["electrodes"][:]
    lf = el.iloc[rows].reset_index(drop=True)
    lf["col"] = np.arange(len(lf))
    return grp["data"], grp["timestamps"], lf


def lfp_pick(lf: pd.DataFrame, peak_id: int, peak_vpos: float, min_far: float = 100.0):
    """LFP columns for a unit: (a) the nearest LFP channel other than the peak channel,
    (b) the nearest one on the other side of the peak channel from (a), (c) the nearest one at
    least min_far um from the peak channel along the probe, above or below (a check that the
    unit's own spikes do not carry the phase locking, asked by the round-1 verifier; a tie goes
    to the channel above)."""
    c = lf[lf.id != peak_id]
    dz = c.vpos.values - peak_vpos
    order = np.lexsort((-dz, np.abs(dz)))       # nearest; a tie goes to the channel above
    a = order[0]
    side = np.sign(dz[a]) if dz[a] != 0 else 1.0
    other = np.where(np.sign(dz) == -side)[0]
    b = other[np.argmin(np.abs(dz[other]))] if len(other) else a
    far = np.where(np.abs(dz) >= min_far)[0]
    far = far[np.lexsort((-dz[far], np.abs(dz[far])))]
    cc = far[0] if len(far) else order[-1]
    return int(c.col.values[a]), int(c.col.values[b]), int(c.col.values[cc])


def nearest_sample(t, v):
    """Index of the LFP sample nearest each spike time (t sorted)."""
    if len(t) < 2:
        return np.zeros(len(v), int)
    i = np.clip(np.searchsorted(t, v), 1, len(t) - 1)
    return np.where(np.abs(v - t[i - 1]) <= np.abs(t[i] - v), i - 1, i)


def _read_cols(data, ts, cols, t0, t1):
    i0, i1 = np.searchsorted(ts, [t0, t1])
    t = ts[i0:i1]
    x = np.stack([data[i0:i1, c] for c in cols], axis=1).astype(np.float64)
    return t, x


def process_session(session: int, seed: int, cap: int = 10000, n_seeds: int = 5,
                    with_lfp: bool = True, with_waveforms: bool = True) -> dict:
    """Everything the claims use from one session, reduced as it loads.

    seed is the generator seed of claim fig3c-fs-more-phase-locked, for the random
    10,000-spike reading; the generator of a session is SeedSequence(seed + 1000 * s,
    spawn_key=(session,)) for s = 0..n_seeds-1, so each session draws its own numbers."""
    import time as _time
    t_start = _time.time()
    f = open_nwb(session_paths()[session])
    info = session_info(f)
    info["session"] = session
    u = visp_units(f)
    info["visp_units"] = len(u)
    info["visp_noise_units"] = int((u.quality != "good").sum())
    E0 = f["general/extracellular_ephys/electrodes"]
    info["electrodes_xyz_nan"] = int(sum(np.isnan(E0[k][:]).sum() for k in ("x", "y", "z")))
    info["electrodes_n"] = len(E0["id"])
    _y, _z = E0["y"][:], E0["z"][:]
    _ok = ~np.isnan(_y) & ~np.isnan(_z)
    info["electrodes_y_eq_z"] = int((_y[_ok] == _z[_ok]).sum())
    u["bad_list"] = u.index.isin(BAD_UNITS)
    rows = u.row.values
    # ---- waveform features
    feats = []
    if with_waveforms:
        waves = read_waveforms(f, rows)
        for uid, r in u.iterrows():
            w = window40(waves[r.row], int(r.local_index))
            if w is None:
                feats.append({"unit_id": uid, "fits": False})
                continue
            d = unit_features(w)
            d.update(unit_id=uid, fits=True)
            feats.append(d)
        del waves
        u = u.join(pd.DataFrame(feats).set_index("unit_id"))
    spikes = read_spikes(f, rows)
    spikes = {uid: np.sort(spikes[r]) for uid, r in zip(u.index, rows)}
    # ---- stimulus tables
    I = f["intervals"]
    tabs = {k: _table(I, k) for k in I if k.endswith("_presentations")}
    t_first = min(t.start_time.min() for t in tabs.values())
    t_last = max(t.stop_time.max() for t in tabs.values())
    dg = tabs["drifting_gratings_presentations"]
    dg = dg[dg.stimulus_name == "drifting_gratings"].reset_index(drop=True)
    blocks = dg.groupby("stimulus_block").agg(start=("start_time", "min"), stop=("stop_time", "max"))
    sp = tabs["spontaneous_presentations"]
    sp = sp[(sp.stop_time - sp.start_time) >= 30].reset_index(drop=True)
    fl = tabs["flashes_presentations"]
    long_sp = sp[(sp.stop_time - sp.start_time) >= 200]
    sp5 = (long_sp.start_time.iloc[0], long_sp.stop_time.iloc[0])   # the first 5-min gray screen
    info.update(n_dg=len(dg), dg_time=float((dg.stop_time - dg.start_time).sum()),
                dg_block_time=float((blocks.stop - blocks.start).sum()),
                spont_time=float((sp.stop_time - sp.start_time).sum()), n_spont=len(sp),
                n_flashes=len(fl), spont5=(float(sp5[0]), float(sp5[1])), t_first=float(t_first), t_last=float(t_last))
    # ---- rates and spike-train measures
    rec = []
    isi_a, isi_b = {}, {}
    for uid in u.index:
        s = spikes[uid]
        d = {"unit_id": uid,
             "n_total": len(s),
             "rate_session": len(s[(s >= t_first) & (s <= t_last)]) / (t_last - t_first),
             "rate_first5min": count_within(s, [t_first], [t_first + 300]) / 300.0,
             "rate_spont": count_within(s, sp.start_time, sp.stop_time) / info["spont_time"],
             "rate_spont5": count_within(s, [sp5[0]], [sp5[1]]) / (sp5[1] - sp5[0]),
             "n_spont": count_within(s, sp.start_time, sp.stop_time),
             "n_dg": count_within(s, dg.start_time, dg.stop_time),
             "n_dg_blocks": count_within(s, blocks.start, blocks.stop)}
        d["rate_dg"] = d["n_dg"] / info["dg_time"]
        d["rate_dg_blocks"] = d["n_dg_blocks"] / info["dg_block_time"]
        ia = isis_within(s, dg.start_time.values, dg.stop_time.values)
        ib = isis_within(s, blocks.start.values, blocks.stop.values)
        isi_a[uid] = np.concatenate(ia).astype(np.float32) if ia else np.zeros(0, np.float32)
        isi_b[uid] = np.concatenate(ib).astype(np.float32) if ib else np.zeros(0, np.float32)
        for tag, x in (("a", ia), ("b", ib)):
            st = isi_stats(x)
            d[f"cv_dg_{tag}"], d[f"lv_dg_{tag}"] = st["cv"], st["lv"]
        d.update(dg_metrics(s, dg))
        rec.append(d)
    u = u.join(pd.DataFrame(rec).set_index("unit_id"))
    # ---- opto-tagging (10 ms square pulses)
    if "optotagging" in f["processing"]:
        o = _table(f["processing/optotagging"], "optogenetic_stimulation")
        pulses = o[(np.abs(o.duration - 0.01) < 1e-4)
                   & o.condition.str.contains("square")].start_time.values
        info["n_opto_pulses"] = len(pulses)
        opt = []
        for uid in u.index:
            s = spikes[uid]
            def rate(a, b):
                return count_within(s, pulses + a, pulses + b) / (len(pulses) * (b - a)) if len(pulses) else np.nan
            opt.append({"unit_id": uid, "opto_resp": rate(0.002, 0.008),
                        "opto_base6": rate(-0.006, 0.0), "opto_base10": rate(-0.010, 0.0)})
        u = u.join(pd.DataFrame(opt).set_index("unit_id"))
    else:
        info["n_opto_pulses"] = 0
    out = {"info": info, "units": u, "isi_a": isi_a, "isi_b": isi_b, "phase": [], "csd": []}
    if not with_lfp:
        return out
    # ---- LFP: CSD depth, and phase locking in drifting gratings and spontaneous activity
    plist = probe_paths(session)
    seqs = [np.random.SeedSequence(seed + 1000 * k, spawn_key=(session,)) for k in range(n_seeds)]
    rngs = [np.random.default_rng(sq) for sq in seqs]
    E = f["general/extracellular_ephys/electrodes"]
    vmap = dict(zip(E["id"][:], E["probe_vertical_position"][:]))
    phase_rows = []
    for probe, pu in u.groupby("probe_id"):
        pf = open_nwb(plist[int(probe)])
        data, tsd, lf = _lfp_channels(pf)
        ts = tsd[:]
        fs = 1.0 / np.median(np.diff(ts[:10000]))
        # CSD around flashes on the VISp LFP channels and one channel on either side
        vis = lf[lf.location == "VISp"].sort_values("vpos")
        if len(vis) >= 3 and len(fl):
            lo = max(vis.index.min() - 1, 0)
            hi = min(vis.index.max() + 1, len(lf) - 1)
            sel = lf.loc[lo:hi].sort_values("vpos")
            t, x = _read_cols(data, ts, sel.col.values, fl.start_time.min() - 1, fl.start_time.max() + 1)
            win = np.arange(int(-0.1 * fs), int(0.25 * fs))
            idx = np.searchsorted(t, fl.start_time.values)
            idx = idx[(idx + win[0] >= 0) & (idx + win[-1] < len(t))]
            erp = np.mean([x[i + win] - x[i + win[win < 0]].mean(0) for i in idx], axis=0)
            dz = np.median(np.diff(sel.vpos.values)) * 1e-6
            csd = -(erp[:, 2:] - 2 * erp[:, 1:-1] + erp[:, :-2]) / dz ** 2
            z = sel.vpos.values[1:-1]
            in_v1 = sel.location.values[1:-1] == "VISp"
            tt = win / fs
            post = (tt >= 0) & (tt <= 0.15)
            c = csd[post][:, in_v1]
            thr = 0.5 * c.min()
            first = np.array([np.argmax(c[:, j] <= thr) if (c[:, j] <= thr).any() else 10 ** 6
                              for j in range(c.shape[1])])
            centre = float(z[in_v1][first.argmin()]) if first.min() < 10 ** 6 else np.nan
            centre_min = float(z[in_v1][np.unravel_index(c.argmin(), c.shape)[1]])
            out["csd"].append({"probe": int(probe), "centre": centre, "centre_min": centre_min,
                               "csd": c.astype(np.float32), "z": z[in_v1], "t_ms": tt[post] * 1000,
                               "n_v1_lfp": int(in_v1.sum()), "t_first_ms": float(tt[post][first.min()] * 1000)
                               if first.min() < 10 ** 6 else np.nan})
            u.loc[pu.index, "depth_csd"] = pu.vpos.values - centre
            u.loc[pu.index, "depth_csd_min"] = pu.vpos.values - centre_min
        # phase locking
        picks = {uid: lfp_pick(lf, int(r.peak_channel_id), vmap[int(r.peak_channel_id)])
                 for uid, r in pu.iterrows()}
        cols = sorted({c for ab in picks.values() for c in ab})
        for period, starts, stops, keep_s, keep_e in (
                ("dg", blocks.start.values, blocks.stop.values, dg.start_time.values, dg.stop_time.values),
                ("spont", sp.start_time.values, sp.stop_time.values, sp.start_time.values, sp.stop_time.values)):
            # spikes of each unit in the kept intervals of the period
            sp_units = {}
            for uid in pu.index:
                s = spikes[uid]
                sp_units[uid] = (s[np.concatenate([np.arange(np.searchsorted(s, a), np.searchsorted(s, b))
                                                   for a, b in zip(keep_s, keep_e)])]
                                 if len(keep_s) else s[:0])
            keys = [("results", k) for k in BANDS_RESULTS] + [("methods", "alpha"), ("methods", "beta")]
            phs = {(uid, lr, key): [] for uid in pu.index for lr in "abc" for key in keys}
            for s0, s1 in zip(starts, stops):
                t, x = _read_cols(data, ts, cols, s0, s1)
                kidx = {uid: nearest_sample(t, v[(v >= s0) & (v < s1)]) for uid, v in sp_units.items()}
                for key in keys:
                    lo, hi = (BANDS_RESULTS if key[0] == "results" else BANDS_METHODS)[key[1]]
                    for c0 in range(0, len(cols), 8):
                        part = cols[c0:c0 + 8]
                        y = butter_bandpass_filter(x[:, c0:c0 + 8], lo, hi, fs)
                        nfft = sp_fft.next_fast_len(len(y))   # zero-padded to a fast FFT length
                        ph = np.angle(signal.hilbert(y, N=nfft, axis=0)[:len(y)]).astype(np.float32)
                        del y
                        for uid in pu.index:
                            for lr, colv in zip("abc", picks[uid]):
                                if colv in part:
                                    phs[(uid, lr, key)].append(ph[kidx[uid], part.index(colv)])
                        del ph
                del x
            for uid in pu.index:
                n_all = len(sp_units[uid])
                subsets = {"first": np.arange(min(cap, n_all))}
                for si, rg in enumerate(rngs):
                    subsets[f"random{si}"] = (np.sort(rg.choice(n_all, cap, replace=False))
                                              if n_all > cap else np.arange(n_all))
                for lr in "abc":
                    for key in keys:
                        a_ = np.concatenate(phs.pop((uid, lr, key))).astype(np.float64)
                        for cap_read, ix in subsets.items():
                            r = phase_lock(a_[ix])
                            r.update(unit_id=uid, period=period, lfp=lr, bands=key[0],
                                     band=key[1], cap=cap_read, n_period=n_all)
                            phase_rows.append(r)
        pf.close()
    out["phase"] = pd.DataFrame(phase_rows)
    out["units"] = u
    info["seconds"] = _time.time() - t_start
    return out


PVALB_SST = "Pvalb-IRES-Cre", "Sst-IRES-Cre"


def sessions_to_use() -> dict[str, list[int]]:
    """The paper's wild-type sessions held here, and the Pvalb and Sst opto-tagging sessions."""
    held = session_paths()
    out = {"wt": [s for s in PAPER_WT_SESSIONS if s in held], "Pvalb": [], "Sst": []}
    for s, p in sorted(held.items()):
        with open_nwb(p) as f:
            g = session_info(f)["genotype"]
        for name, tag in zip(("Pvalb", "Sst"), PVALB_SST):
            if g.startswith(tag):
                out[name].append(s)
    return out


def _worker(args):
    import os
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    session, seed = args
    return process_session(session, seed)


def process_all(sessions, seed, workers=3) -> dict:
    """process_session over sessions in worker processes (each holds about 2 GB at its peak)."""
    from concurrent.futures import ProcessPoolExecutor
    with ProcessPoolExecutor(workers) as ex:
        res = list(ex.map(_worker, [(s, seed) for s in sessions]))
    return dict(zip(sessions, res))


# ----------------------------------------------------------------------------- analysis helpers

def assemble(results: dict, groups: dict) -> pd.DataFrame:
    """One table of units over sessions, with session, genotype group and the isolation
    readings: (a) and (b) of the criterion of fig1d-unit-count, and (c), reading (a) with at
    least 100 spikes in the first 5-min gray screen. (c) is taken from the Results ("well-isolated
    ... during spontaneous activity", paragraph 1 of "EAP recordings from in vivo experiments")
    and the 100-spike rule of the Methods ("Single unit firing properties"); every unit of the
    code's unit tables has fr_5min at least 0.35 Hz, about 100 spikes in that block. It is an
    assumption, used for the claims after fig1d-unit-count."""
    frames = []
    for g, sess in groups.items():
        for s in sess:
            u = results[s]["units"].copy()
            u["session"], u["group"] = s, g
            a, b = results[s]["info"]["spont5"]
            u["n_spont5"] = np.round(u.rate_spont5 * (b - a)).astype(int)
            frames.append(u)
    u = pd.concat(frames)
    u["iso_a"] = u.allensdk_filter & (u.quality == "good") & ~u.bad_list
    u["iso_b"] = ~u.bad_list            # every VISp unit of the units table, good or noise
    # (c): (a) and at least 100 spikes in the first 5-min gray screen, the period of the code's
    # fr_5min column (see the docstring)
    u["iso_c"] = u.iso_a & (u.n_spont5 >= 100)
    return u


def select_wt(units: pd.DataFrame, reading: str, nan_aware: bool = True) -> pd.DataFrame:
    """Wild-type units of an isolation reading after the code's exclusions (cell 8), which
    are computed over the pooled units as the code does."""
    w = units[(units.group == "wt") & units[f"iso_{reading}"] & (units.fits == True)].copy()
    keep = code_exclusions(w, nan_aware)
    return w[keep.values]


def cluster_one_channel(df: pd.DataFrame, seed: int, n_init: int = 1000, numk: int = 9):
    """Fig 2 one-channel clustering (cells 11 and 13); FS is the cluster of lower median TPW."""
    X = pre_process(df[["TPW", "REP"]].values)
    wcss, fk = selection_k(X, numk, n_init=n_init, seed=seed)
    lab = kmeans_labels(X, 2, seed, n_init=n_init)
    fs = 0 if np.median(df.TPW.values[lab == 0]) < np.median(df.TPW.values[lab == 1]) else 1
    return {"wcss": wcss, "fk": fk, "elbow_k": find_elbow(wcss), "fk_k": int(fk.argmin() + 1),
            "fsrs": np.where(lab == fs, "FS", "RS")}


def cluster_multi_channel(df: pd.DataFrame, fsrs: np.ndarray, seed: int, n_init: int = 1000,
                          numk: int = 9, k_override=None):
    """Fig 2d multi-channel clustering (cells 17 to 21): 1/V below and above z-scored over all
    units, then K-means within FS and within RS with K = argmin f(K) + 1."""
    X = pre_process(df[["PL_below", "PL_above"]].values)
    out = {}
    for grp in ("FS", "RS"):
        m = fsrs == grp
        wcss, fk = selection_k(X[m], numk, n_init=n_init, seed=seed)
        k = int(fk.argmin() + 1) if k_override is None else k_override
        lab = kmeans_labels(X[m], k, seed, n_init=n_init)
        out[grp] = {"wcss": wcss, "fk": fk, "elbow_k": find_elbow(wcss), "fk_k": int(fk.argmin() + 1),
                    "k": k, "labels": lab, "index": df.index[m]}
    return out


def name_by_overlap(index, labels, ref: pd.Series, names):
    """Name each cluster by the reference label it shares most units with (one to one,
    greedy on the overlap counts). Only reference labels among names are used, so every
    cluster gets one of names."""
    shared = pd.Series(labels, index=index).loc[lambda s: s.index.isin(ref.index)]
    shared = shared[ref.loc[shared.index].isin(names).values]
    tab = pd.crosstab(shared.values, ref.loc[shared.index].values)
    mapping, used = {}, set()
    pairs = sorted(((tab.loc[i, j], i, j) for i in tab.index for j in tab.columns), reverse=True)
    for v, i, j in pairs:
        if i not in mapping and j not in used:
            mapping[i] = j
            used.add(j)
    for i in np.unique(labels):
        if i not in mapping:
            mapping[i] = next(n for n in names if n not in used)
            used.add(mapping[i])
    return np.array([mapping[l] for l in labels]), tab


def classifier(X, Y, newX, model_name, random_num, seed):
    """ecp_func.classifier: random_num stratified 75/25 splits, linear SVC (C = 1, balanced
    weights) or a random forest (20 trees, gini); returns the mean validation accuracy and,
    for every row of newX, the counts of each predicted label. The code seeds its splits with
    random.seed(100); here the split seeds come from the claim's generator."""
    from sklearn import svm
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import train_test_split
    rng = np.random.default_rng(seed)
    acc = []
    classes = np.unique(Y)
    votes = np.zeros((len(newX), len(classes)), int) if newX is not None else None
    for _ in range(random_num):
        Xtr, Xte, ytr, yte = train_test_split(X, Y, test_size=0.25, stratify=Y,
                                              random_state=int(rng.integers(1, 2 ** 31 - 1)))
        if model_name == "svm":
            m = svm.SVC(kernel="linear", C=1, class_weight="balanced")
        else:
            m = RandomForestClassifier(n_estimators=20, criterion="gini", max_features="sqrt",
                                       bootstrap=True, oob_score=True, random_state=0, n_jobs=1)
        m.fit(Xtr, ytr)
        acc.append(np.mean(m.predict(Xte) == yte))
        if newX is not None:
            p = m.predict(newX)
            for ci, c in enumerate(classes):
                votes[:, ci] += p == c
    return float(np.mean(acc)), votes, classes


def zscore(X):
    X = np.asarray(X, float)
    return (X - X.mean(0)) / X.std(0)


def upsample_index(labels, rng):
    """Every row, plus minority-class rows drawn with replacement up to the largest class
    (Exp_Model_Classifier.ipynb cell 7, ecp_func.upsampling_data)."""
    labels = np.asarray(labels)
    cls, cnt = np.unique(labels, return_counts=True)
    idx = [np.arange(len(labels))]
    for c, n in zip(cls, cnt):
        if n < cnt.max():
            idx.append(rng.choice(np.where(labels == c)[0], cnt.max() - n, replace=True))
    return np.concatenate(idx)


def two_sample_test(a, b):
    """ecp_func.two_sample_test: Shapiro-Wilk on each group at 0.05, then a two-sample t-test
    or a two-sided Mann-Whitney U test."""
    a, b = np.asarray(a, float), np.asarray(b, float)
    a, b = a[~np.isnan(a)], b[~np.isnan(b)]
    normal = stats.shapiro(a).pvalue > 0.05 and stats.shapiro(b).pvalue > 0.05
    if normal:
        return "t-test", stats.ttest_ind(a, b).pvalue
    return "Mann-Whitney U", stats.mannwhitneyu(a, b, alternative="two-sided").pvalue
