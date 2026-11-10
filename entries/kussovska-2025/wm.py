"""Loading and shared measures for DANDI:000469 (Kyzar et al. 2024), as used by Kussovska, Kim and
Rungratsameetaweemana (2025), "Neural heterogeneity shapes the temporal structure of human working
memory" (bioRxiv doi:10.1101/2025.10.31.684900).

The data are streamed from the archive at a pinned version (DANDISET_VERSION, the version the paper
cites in Methods, Participants and data source). Only the Sternberg file of each subject is read
(sub-<n>_ses-2), as the paper's code does (01_data_extraction.py:417 of
github.com/dariakussovska/heterogeneitywm at commit 5144fe8); only the spike times, the electrode
locations and the trials table are read, not the waveforms or the stimulus images.
"""
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
import requests

DANDISET_ID = "000469"
DANDISET_VERSION = "0.231213.2047"
API = "https://api.dandiarchive.org/api"

TRIAL_COLUMNS = ["loads", "loadsEnc1_PicIDs", "loadsEnc2_PicIDs", "loadsEnc3_PicIDs",
                 "loadsProbe_PicIDs", "probe_in_out", "response_accuracy", "start_time", "stop_time",
                 "timestamps_FixationCross", "timestamps_Encoding1", "timestamps_Encoding1_end",
                 "timestamps_Encoding2", "timestamps_Encoding2_end", "timestamps_Encoding3",
                 "timestamps_Encoding3_end", "timestamps_Maintenance", "timestamps_Probe",
                 "timestamps_Response"]

# Region names: the dataset's location labels with the hemisphere removed (left and right merged,
# as main_1e,f.py:87-104 of the paper's code merges them).
REGION_OF = {"amygdala": "AMY", "hippocampus": "HPC", "dorsal_anterior_cingulate_cortex": "dACC",
             "pre_supplementary_motor_area": "preSMA", "ventral_medial_prefrontal_cortex": "vmPFC"}


def list_assets(version=DANDISET_VERSION):
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{version}/assets/?page_size=200"
    out = []
    while url:
        r = requests.get(url, timeout=60).json()
        out += r["results"]
        url = r["next"]
    return sorted(out, key=lambda a: a["path"])


def asset_url(asset_id):
    return requests.head(f"{API}/assets/{asset_id}/download/", allow_redirects=True, timeout=60).url


def region_of(location):
    loc = location.lower()
    for side in ("_left", "_right"):
        if loc.endswith(side):
            loc = loc[: -len(side)]
    return REGION_OF.get(loc, loc)


def _str(x):
    return x.decode() if isinstance(x, bytes) else str(x)


def load_session(asset):
    """Read one NWB file over HTTP: units (spike times, location), trials, subject."""
    f = h5py.File(remfile.File(asset_url(asset["asset_id"])), "r")
    st = f["units/spike_times"][:]
    idx = f["units/spike_times_index"][:]
    el = f["units/electrodes"][:]
    loc = np.array([_str(x) for x in f["general/extracellular_ephys/electrodes/location"][:]])
    el_ids = f["general/extracellular_ephys/electrodes/id"][:]
    pos = {e: i for i, e in enumerate(el_ids)}
    unit_ids = f["units/id"][:]
    starts = np.r_[0, idx[:-1]]
    spikes = [st[a:b] for a, b in zip(starts, idx)]
    trials = pd.DataFrame({c: f["intervals/trials/" + c][:] for c in TRIAL_COLUMNS})
    trials.insert(0, "trial_id", f["intervals/trials/id"][:])
    subj = {k: _str(f["general/subject/" + k][()]) for k in f["general/subject"].keys()}
    units = pd.DataFrame({"unit_id": unit_ids, "electrode": el,
                          "location": [loc[pos[e]] if e in pos else loc[e] for e in el]})
    units["region"] = units.location.map(region_of)
    units["n_spikes"] = [len(s) for s in spikes]
    events = f["acquisition/events/timestamps"][:] if "acquisition/events" in f else None
    sess = {"path": asset["path"], "asset_id": asset["asset_id"], "size": asset["size"],
            "subject": subj, "units": units, "spikes": spikes, "trials": trials,
            "session_description": _str(f["session_description"][()]),
            "session_id": _str(f["general/session_id"][()]) if "general/session_id" in f else "",
            "n_events": None if events is None else len(events)}
    f.close()
    return sess


def sternberg_assets(version=DANDISET_VERSION):
    return [a for a in list_assets(version) if "_ses-2_" in a["path"]]


def subject_number(path):
    return int(path.split("/")[0].split("-")[1])


def load_all(version=DANDISET_VERSION, workers=6):
    assets = sternberg_assets(version)
    with ThreadPoolExecutor(workers) as ex:
        sessions = list(ex.map(load_session, assets))
    for s in sessions:
        s["sub"] = subject_number(s["path"])
    return sorted(sessions, key=lambda s: s["sub"])


# ---------------------------------------------------------------------------------------------
# Trials and spike counts
# ---------------------------------------------------------------------------------------------

def trial_frame(sess):
    """The trials table with derived columns. trial is the 1-based row number, which is the
    trial_id of the paper's code (01_data_extraction.py:76, trial_id = i + 1). RT is probe onset to
    button press (Methods, Psychophysical task). img1..img3 are the picture ids (1 to 5) of the
    encoding periods; last is the last encoded image (Results, Fig. 2e paragraph)."""
    t = sess["trials"].copy()
    t["trial"] = np.arange(1, len(t) + 1)
    t["sub"] = sess["sub"]
    t["load"] = t["loads"].astype(int)
    t["rt"] = t["timestamps_Response"] - t["timestamps_Probe"]
    t["img1"] = t["loadsEnc1_PicIDs"].astype(int)
    t["img2"] = t["loadsEnc2_PicIDs"].astype(int)
    t["img3"] = t["loadsEnc3_PicIDs"].astype(int)
    t["last"] = np.where(t.load == 1, t.img1, np.where(t.load == 2, t.img2, t.img3))
    t["correct"] = t["response_accuracy"].astype(int)
    t["in_memory"] = t["probe_in_out"].astype(int)
    t["fix_start"] = t["timestamps_FixationCross"]
    t["enc1"] = t["timestamps_Encoding1"]
    t["maint"] = t["timestamps_Maintenance"]
    t["probe"] = t["timestamps_Probe"]
    t["maint_dur"] = t["probe"] - t["maint"]
    return t


def count_in(spikes, starts, ends):
    """Spike counts in [start, end) for each pair of window edges."""
    return np.searchsorted(spikes, ends, side="left") - np.searchsorted(spikes, starts, side="left")


def fixation_stats(spikes, t):
    """Mean and s.d. (ddof 1, as pandas std in the code) over trials of the fixation rate, fixation
    being fixation-cross onset to first encoding onset (Methods, Electrophysiology)."""
    dur = (t.enc1 - t.fix_start).to_numpy()
    r = count_in(spikes, t.fix_start.to_numpy(), t.enc1.to_numpy()) / dur
    return r.mean(), r.std(ddof=1)


def neuron_table(sessions):
    rows = []
    for s in sessions:
        for i, u in s["units"].iterrows():
            rows.append({"sub": s["sub"], "unit": i, "unit_id": int(u.unit_id), "region": u.region,
                         "location": u.location, "n_spikes": int(u.n_spikes)})
    df = pd.DataFrame(rows)
    df["nid"] = np.arange(len(df))
    return df


def spikes_of(sessions_by_sub, row):
    return sessions_by_sub[row["sub"]]["spikes"][row["unit"]]


# ---------------------------------------------------------------------------------------------
# Poisson GLM with one predictor, fitted by Newton's method for many predictor vectors at once
# ---------------------------------------------------------------------------------------------

def poisson_slopes(y, X, n_iter=50):
    """Maximum-likelihood slope of log E[y] = b0 + b1 x for each row of X (shape P x n), with no
    penalty; the same model as sklearn PoissonRegressor(alpha=0) in main_1e,f.py:147. A neuron with
    no spikes has slope 0."""
    y = np.asarray(y, float)
    X = np.atleast_2d(np.asarray(X, float))
    P = X.shape[0]
    if y.sum() == 0:
        return np.zeros(P)
    b0 = np.full(P, np.log(y.mean()))
    b1 = np.zeros(P)
    for _ in range(n_iter):
        eta = np.clip(b0[:, None] + b1[:, None] * X, -30, 30)
        mu = np.exp(eta)
        r = y[None, :] - mu
        g0, g1 = r.sum(1), (r * X).sum(1)
        h00, h01, h11 = mu.sum(1), (mu * X).sum(1), (mu * X * X).sum(1)
        det = h00 * h11 - h01 ** 2
        det = np.where(np.abs(det) < 1e-12, 1e-12, det)
        d0 = (h11 * g0 - h01 * g1) / det
        d1 = (-h01 * g0 + h00 * g1) / det
        step = np.minimum(1.0, 5.0 / np.maximum(np.abs(d1), 1e-12))
        b0 += step * d0
        b1 += step * d1
        if np.max(np.abs(d1)) < 1e-9:
            break
    return b1


def glm_fit(counts_by_neuron, x_by_neuron, perms_by_neuron):
    """Real and permutation-null slopes for each neuron (Methods, Generalized linear model encoding
    analysis; main_1e,f.py:150-170). counts_by_neuron and x_by_neuron are per-neuron arrays;
    perms_by_neuron gives for each neuron an index array (n_perm x n_trials) that permutes its
    predictor. The predictor is z-scored before fitting (main_1e,f.py:128)."""
    n = len(counts_by_neuron)
    real, null = np.empty(n), None
    for j in range(n):
        x = np.asarray(x_by_neuron[j], float)
        xz = (x - x.mean()) / (x.std() + 1e-12)
        real[j] = poisson_slopes(counts_by_neuron[j], xz[None, :])[0]
        nb = poisson_slopes(counts_by_neuron[j], xz[perms_by_neuron[j]])
        if null is None:
            null = np.empty((n, len(nb)))
        null[j] = nb
    return real, null


def glm_groups(real, null, groups, alpha=0.05):
    """A neuron is significant when |b1| is at or above the 95th percentile ('higher' quantile) of
    its |null|; a group's p is the fraction of null counts of significant neurons at or above the
    observed count (main_1e,f.py:172-205; no + 1, as in the code). groups: {name: index array}."""
    absn = np.abs(null)
    thr = np.quantile(absn, 1 - alpha, axis=1, method="higher")
    sig = np.abs(real) >= thr
    sig_null = absn >= thr[:, None]
    out = []
    for g, idx in groups.items():
        idx = np.asarray(idx)
        obs = int(sig[idx].sum())
        nc = sig_null[idx].sum(0)
        out.append({"group": g, "n": len(idx), "significant": obs,
                    "percent": 100 * obs / max(len(idx), 1), "null_mean": nc.mean(),
                    "p": float(np.mean(nc >= obs))})
    return pd.DataFrame(out), sig


# ---------------------------------------------------------------------------------------------
# Concept cells (Methods, Identification of concept cells; 04_concept_cells.py)
# ---------------------------------------------------------------------------------------------

def concept_test(rates, imgs, rng, n_boot=1000, reading="methods"):
    """rates: per-trial rate 200 to 1000 ms after first-encoding onset; imgs: first image per
    trial. Returns (preferred image, p, significant). Top two images by mean rate; bootstrap of the
    difference of means. reading 'methods' resamples each image's trials to its own number and
    takes p = 2 min(P(d > 0), P(d < 0)); reading 'code' resamples both to the smaller number and
    takes the minimum of the four terms at 04_concept_cells.py:86-90."""
    ims = np.unique(imgs)
    means = np.array([rates[imgs == i].mean() for i in ims])
    order = np.argsort(-means, kind="stable")
    i1, i2 = ims[order[0]], ims[order[1]]
    a, b = rates[imgs == i1], rates[imgs == i2]
    if reading == "methods":
        sa = a[rng.integers(0, len(a), (n_boot, len(a)))].mean(1)
        sb = b[rng.integers(0, len(b), (n_boot, len(b)))].mean(1)
        d = sa - sb
        p = min(1.0, 2 * min(np.mean(d > 0), np.mean(d < 0)))
    else:
        m = min(len(a), len(b))
        d = a[rng.integers(0, len(a), (n_boot, m))].mean(1) - b[rng.integers(0, len(b), (n_boot, m))].mean(1)
        m1 = 2 * np.sum(d > 0) / n_boot
        m2 = 1 - np.sum(d < 0) / n_boot
        m3 = 2 * np.sum(d < 0) / n_boot
        m4 = 1 - np.sum(d > 0) / n_boot
        p = min(m1, m2, m3, m4)
    sig = (p < 0.05) and len(a) > 1 and len(b) > 1 and means[order[0]] > 0
    return int(i1), float(p), bool(sig)


# ---------------------------------------------------------------------------------------------
# Linear SVM decoding with leave-one-out cross-validation
# ---------------------------------------------------------------------------------------------

def _svm_fit(K, y):
    """Linear SVM (C-SVC, C = 1, one-vs-one) on a precomputed linear kernel, through the libsvm
    wrapper that sklearn's SVC uses. It gives the same fits as SVC(kernel='linear', C=1) on the
    features (the code's classifier) without SVC's per-call overhead; the notebook checks the
    equality on the data."""
    from sklearn.svm import _libsvm
    _libsvm.set_verbosity_wrap(0)
    return _libsvm.fit(np.ascontiguousarray(K), np.asarray(y, float), svm_type=0,
                       kernel="precomputed", C=1.0, tol=1e-3, cache_size=200.0)


def _svm_predict(model, Ktest):
    from sklearn.svm import _libsvm
    sup, sv, nsv, dual, inter, pa, pb, _, _ = model
    return _libsvm.predict(np.ascontiguousarray(Ktest, dtype=float), sup, sv, nsv, dual, inter,
                           pa, pb, svm_type=0, kernel="precomputed")


def loo_correct(K, y):
    """Leave-one-out correctness of the linear SVM from the precomputed kernel K = X X^T."""
    y = np.asarray(y, float)
    n = len(y)
    out = np.zeros(n, bool)
    idx = np.arange(n)
    for i in range(n):
        tr = idx != i
        if len(np.unique(y[tr])) < 2:
            continue
        # libsvm, as sklearn calls it, expects the classes coded 0 to k-1 (SVC encodes them first)
        cls, yc = np.unique(y[tr], return_inverse=True)
        m = _svm_fit(K[np.ix_(tr, tr)], yc)
        out[i] = cls[int(_svm_predict(m, K[i, tr][None, :])[0])] == y[i]
    return out


def loo_correct_sklearn(X, y):
    """The same with sklearn SVC(kernel='linear') on the features, for the equality check."""
    from sklearn.svm import SVC
    n = len(y)
    idx = np.arange(n)
    return np.array([SVC(kernel="linear", C=1.0).fit(X[idx != i], y[idx != i]).predict(X[i:i + 1])[0] == y[i]
                     for i in range(n)])


def loo_cross_temporal(X, y):
    """Cross-temporal LOOCV accuracy matrix (train bin x test bin). X: trials x neurons x bins."""
    y = np.asarray(y, float)
    n, _, nb = X.shape
    G = np.einsum("inb,jnc->bcij", X, X)  # G[b, c] = X[:, :, b] @ X[:, :, c].T
    acc = np.zeros((nb, nb))
    idx = np.arange(n)
    for b in range(nb):
        for i in range(n):
            tr = idx != i
            cls, yc = np.unique(y[tr], return_inverse=True)
            m = _svm_fit(G[b, b][np.ix_(tr, tr)], yc)
            kt = G[:, b, i, :][:, tr]  # test trial i at every bin c against training trials at bin b
            acc[b] += cls[_svm_predict(m, kt).astype(int)] == y[i]
    return acc / n


# ---------------------------------------------------------------------------------------------
# Autocorrelograms and the CellExplorer fit (data/cell_analysis/*.m of the paper's code)
# ---------------------------------------------------------------------------------------------

def acg(spikes, bin_size, n_bins):
    """calc_ACG_metrics.m autocorrelogram: lags rounded to bins, |bin| <= n_bins // 2, self pairs
    removed, divided by spike count and bin width."""
    half = n_bins // 2
    maxlag = (half + 0.5) * bin_size
    out = np.zeros(n_bins)
    s = np.asarray(spikes, float)
    n = len(s)
    if n < 2:
        return np.full(n_bins, np.nan)
    k = 1
    while k < n:
        d = s[k:] - s[:-k]
        d = d[d <= maxlag]
        if d.size == 0:
            break
        b = np.round(d / bin_size).astype(int)
        b = b[b <= half]
        np.add.at(out, half + b, 1)
        np.add.at(out, half - b, 1)
        k += 1
    return out / (n * bin_size)


def _acg_model(p, x):
    a, b, c, d, e, f, g, h = p
    return np.maximum(c * (np.exp(-(x - f) / a) - d * np.exp(-(x - f) / b)) + h * np.exp(-(x - f) / g) + e, 0)


def fit_acg(acg_narrow):
    """fit_ACG.m of CellExplorer: bins -0.5 to +0.5 ms set to zero, the triple exponential fitted at
    lags 0.5 to 50 ms from the start point a0 within bounds lb, ub, by bounded nonlinear least
    squares (scipy's trust-region reflective, as MATLAB's fit uses). Returns tau_decay, tau_rise,
    R2 and the parameters."""
    from scipy.optimize import least_squares
    y_all = np.array(acg_narrow, float)
    y_all[99:102] = 0
    x = np.arange(1, 101) / 2
    y = y_all[(x * 2).astype(int) + 100]
    a0 = np.array([20, 1, 30, 2, 0.5, 5, 1.5, 2], float)
    lb = np.array([1, 0.1, 0, 0, -30, 0, 0.1, 0], float)
    ub = np.array([500, 50, 500, 15, 50, 20, 5, 100], float)
    if not np.all(np.isfinite(y)):
        return dict(tau_decay=np.nan, tau_rise=np.nan, r2=np.nan)
    res = least_squares(lambda p: _acg_model(p, x) - y, a0, bounds=(lb, ub), method="trf",
                        max_nfev=2000)
    sse = np.sum(res.fun ** 2)
    sst = np.sum((y - y.mean()) ** 2)
    r2 = 1 - sse / sst if sst > 0 else np.nan
    return dict(tau_decay=res.x[0], tau_rise=res.x[1], r2=r2, params=res.x)


def acg_features(spikes):
    """Features of one neuron: narrow and wide ACG, the fit, the mean of the max-normalised wide
    ACG with the zero-lag bin set to 0 (Mean_ACG.m, normalize_acg_to_unit.m), the Royer burst
    index mean(wide[+2..+4 ms]) / mean(wide[+199..+299 ms]) (calc_ACG_metrics.m:45), the firing
    rate as count over first-to-last spike (02_trial_info.py:37-40), the ISI CV (std/mean,
    02_trial_info.py:42-46) and Holt's CV2 (mean of 2|I(n+1) - I(n)| / (I(n+1) + I(n)))."""
    s = np.asarray(spikes, float)
    nar = acg(s, 0.0005, 201)
    wide = acg(s, 0.001, 1001)
    fit = fit_acg(nar)
    w = wide.copy()
    mx = np.nanmax(w) if np.any(np.isfinite(w)) else np.nan
    wn = w / mx if mx and mx > 0 else np.full_like(w, np.nan)
    wn[500] = 0
    isi = np.diff(s)
    cv2 = np.mean(2 * np.abs(isi[1:] - isi[:-1]) / (isi[1:] + isi[:-1])) if len(isi) > 1 else np.nan
    return {"tau_decay": fit["tau_decay"], "tau_rise": fit["tau_rise"], "r2": fit["r2"],
            "acg_norm": np.nanmean(wn), "burst_royer": np.mean(wide[502:505]) / np.mean(wide[699:800]),
            "firing_rate": len(s) / (s[-1] - s[0]) if len(s) > 1 else np.nan,
            "cv_isi": np.std(isi) / np.mean(isi) if len(isi) > 1 else np.nan, "cv2_holt": cv2}


def cv2_holt(isi):
    isi = np.asarray(isi, float)
    if len(isi) < 2:
        return np.nan
    return np.mean(2 * np.abs(isi[1:] - isi[:-1]) / (isi[1:] + isi[:-1]))


# ---------------------------------------------------------------------------------------------
# Population bursts (Methods, Burst detection; 04_bursting/main_4c,d,6a,b.py)
# ---------------------------------------------------------------------------------------------
BURST_BIN = 0.07      # s, Methods and code line 12
BURST_SIGMA = 0.04    # s, Methods and code line 15
BURST_PCT = 90        # percentile, Methods and code line 16


def smooth_counts(spike_times, total_dur, bin_size=BURST_BIN, sigma=BURST_SIGMA):
    from scipy.signal.windows import gaussian
    edges = np.arange(0.0, total_dur + bin_size, bin_size)
    c, _ = np.histogram(spike_times, bins=edges)
    # The code's kernel is gaussian(len(counts)) normalised to sum 1 (line 245); its weights beyond
    # 12 bins (sigma is 0.57 bins) are below 1e-90, so it is cut there, keeping its parity and
    # hence its half-bin offset when the length is even. This changes no value above 1e-80.
    M = len(c)
    full = gaussian(M, std=sigma / bin_size)
    full = full / full.sum()
    K = 12
    if M > 2 * K + 2:
        lo = (M - 1) // 2 - K if M % 2 else M // 2 - K
        hi = (M - 1) // 2 + K + 1 if M % 2 else M // 2 + K
        k = full[lo:hi]
    else:
        k = full
    return np.convolve(c, k, mode="same")


def burst_peaks(sm, threshold, rule="prominence", distance=2):
    """Peaks of the smoothed population count. rule 'prominence': prominence at or above the
    threshold (the code, lines 251-255, and the Results); rule 'height': local peaks whose smoothed
    value exceeds the threshold (Methods). distance in bins (2 bins = 140 ms, Methods and code)."""
    import scipy.signal as signal
    kw = {"distance": distance} if distance and distance > 1 else {}
    if rule == "prominence":
        pk, _ = signal.find_peaks(sm, prominence=threshold, **kw)
    else:
        pk, _ = signal.find_peaks(sm, height=np.nextafter(threshold, np.inf), **kw)
    return pk


def concat_trials(spike_lists, win):
    """Concatenate per-trial relative spike times (each in [0, win]) into one train."""
    parts = [np.asarray(s) + i * win for i, s in enumerate(spike_lists) if len(s)]
    return np.concatenate(parts) if parts else np.array([])


def spectral_types(features, random_state=42):
    """Spectral clustering on standardised firing rate, normalised mean ACG and tau_rise
    (07_spectral_clustering.py: StandardScaler, SpectralClustering(n_clusters=2,
    affinity='nearest_neighbors', random_state=42)). The cluster with the higher median firing
    rate is labelled IN (Results, Feature-based classification, paragraph 3)."""
    from sklearn.cluster import SpectralClustering
    from sklearn.preprocessing import StandardScaler
    X = StandardScaler().fit_transform(features[["firing_rate", "acg_norm", "tau_rise"]].values)
    lab = SpectralClustering(n_clusters=2, affinity="nearest_neighbors",
                             random_state=random_state).fit_predict(X)
    fr = features["firing_rate"].values
    in_label = 0 if np.median(fr[lab == 0]) > np.median(fr[lab == 1]) else 1
    return np.where(lab == in_label, "IN", "PY"), lab


def epoch_spikes(spikes, starts, ends, win):
    """Per-trial spike times relative to each start, within [start, end) and clipped to [0, win]
    (the code's parse_spike_entry keeps 0 <= t <= TRIAL_WIN)."""
    out = []
    for a, b in zip(starts, ends):
        i, j = np.searchsorted(spikes, [a, b])
        r = spikes[i:j] - a
        out.append(r[(r >= 0) & (r <= win)])
    return out


def group_bursts(neuron_trials, win, rng, rule="prominence", distance=2, thr_mode="real",
                 n_sur=100):
    """Population bursts of one group of one participant. neuron_trials: per neuron, the list of
    its per-trial relative spike times (same trials for all neurons). The group's spikes are pooled,
    trials concatenated with stride win, binned at 70 ms, smoothed (Gaussian, sigma 40 ms), and
    peaks found against the 90th percentile of the smoothed train. Surrogates: per neuron and trial a
    Poisson count with the trial's count as its mean, spike times uniform in the window (code lines
    272-306; Methods). thr_mode 'real' uses the real train's threshold for the surrogates (code),
    'own' each surrogate's own. Returns (real count, mean surrogate count, peak bins, n bins)."""
    n_tr = len(neuron_trials[0])
    pooled = np.concatenate([concat_trials(nt, win) for nt in neuron_trials]) if neuron_trials else np.array([])
    total = n_tr * win
    sm = smooth_counts(pooled, total)
    thr = np.percentile(sm, BURST_PCT)
    pk = burst_peaks(sm, thr, rule, distance)
    counts = np.array([[len(s) for s in nt] for nt in neuron_trials])  # neurons x trials
    sur = []
    offs = np.arange(n_tr) * win
    for _ in range(n_sur):
        n = rng.poisson(counts)
        tot = n.sum()
        if tot == 0:
            sur.append(0)
            continue
        tr_idx = np.repeat(np.tile(np.arange(n_tr), counts.shape[0]), n.ravel())
        st = rng.uniform(0, win, tot) + offs[tr_idx]
        s2 = smooth_counts(st, total)
        th = thr if thr_mode == "real" else np.percentile(s2, BURST_PCT)
        sur.append(len(burst_peaks(s2, th, rule, distance)))
    return len(pk), float(np.mean(sur)), pk, len(sm)


def burst_groups(NT, feats, concept, types, rule="code"):
    """Neuron groups per participant for the burst analyses. NT: neuron table; feats: ACG features
    (index aligned with NT); concept: boolean array; types: array of 'PY', 'IN' or None.
    rule 'methods': median split within participant of the well-fit neurons (R2 > 0.3) on
    normalised mean ACG and on tau_decay, the lower and upper halves (floor(n/2) each), participants
    with fewer than 5 neurons in a group left out (Methods, Burst detection); rule 'code': the 6
    lowest and 6 highest of participants with at least 10 well-fit neurons (main_4c,d,6a,b.py:52,
    95-120, 164-172). All cells: every neuron of participants with at least 10 neurons (code line
    183-185, 'All902'), or the well-fit neurons ('AllFit') with the same rule. Concept cells: at
    least 3 per participant (code) or 5 (Methods). PY and IN: at least 3 (Methods, Putative
    cell-type classification; code lines 178-181). Returns {group: {sub: [nid, ...]}}."""
    fit = feats["r2"].values > 0.3
    out = {g: {} for g in ["All902", "AllFit", "LowACG", "HighACG", "ShortDecay", "LongDecay",
                           "Concept", "PY", "IN"]}
    for sub, g in NT.groupby("sub"):
        nids = g.nid.values
        if len(nids) >= 10:
            out["All902"][sub] = list(nids)
        f = nids[fit[nids]]
        if len(f) >= 10:
            out["AllFit"][sub] = list(f)
        for feat, lo, hi in [("acg_norm", "LowACG", "HighACG"), ("tau_decay", "ShortDecay", "LongDecay")]:
            v = feats[feat].values[f]
            ok = np.isfinite(v)
            ff, v = f[ok], v[ok]
            order = np.lexsort((ff, v))  # stable, ties by neuron id as in the code
            if rule == "code":
                if len(ff) >= 10:
                    out[lo][sub] = list(ff[order[:6]])
                    out[hi][sub] = list(ff[order[-6:]])
            else:
                m = len(ff) // 2
                if m >= 5:
                    out[lo][sub] = list(ff[order[:m]])
                    out[hi][sub] = list(ff[order[-m:]])
        c = nids[concept[nids]]
        if len(c) >= (3 if rule == "code" else 5):
            out["Concept"][sub] = list(c)
        for ty in ["PY", "IN"]:
            t = nids[np.asarray(types, dtype=object)[nids] == ty]
            if len(t) >= 3:
                out[ty][sub] = list(t)
    return out


def epoch_burst_counts(neuron_trials_by_epoch, rule="prominence", distance=2, mreading="methods"):
    """Real burst counts of one group in encoding, M1 to M3 and probe (Methods, Burst detection,
    last paragraph; 04_bursting/main_4f-k,6c,d.py). neuron_trials_by_epoch: {'enc': [...],
    'maint': [...], 'probe': [...]}, each a per-neuron list of per-trial relative spike times;
    encoding and probe use 1 s windows, maintenance 3 s (the code's durations, lines 19-25).
    mreading 'methods': peaks of the maintenance train counted by their time within the trial,
    [0, 1), [1, 2) and [2, 3) s from maintenance onset; 'code': peaks assigned to thirds of the
    bins of the whole concatenated train (lines 216-219)."""
    out = {}
    for ep, win in [("enc", 1.0), ("probe", 1.0)]:
        nt = neuron_trials_by_epoch[ep]
        pooled = np.concatenate([concat_trials(x, win) for x in nt])
        sm = smooth_counts(pooled, len(nt[0]) * win)
        out[ep] = len(burst_peaks(sm, np.percentile(sm, BURST_PCT), rule, distance))
    nt = neuron_trials_by_epoch["maint"]
    win = 3.0
    pooled = np.concatenate([concat_trials(x, win) for x in nt])
    sm = smooth_counts(pooled, len(nt[0]) * win)
    pk = burst_peaks(sm, np.percentile(sm, BURST_PCT), rule, distance)
    if mreading == "methods":
        t_in = (pk * BURST_BIN) % win
        for i in range(3):
            out[f"M{i + 1}"] = int(np.sum((t_in >= i) & (t_in < i + 1)))
    else:
        thirds = np.array_split(np.arange(len(sm)), 3)
        for i, part in enumerate(thirds):
            out[f"M{i + 1}"] = int(np.sum(np.isin(pk, part)))
    return out


# ---------------------------------------------------------------------------------------------
# Decoding designs
# ---------------------------------------------------------------------------------------------

def window_starts(width, step, end):
    """The code's create_time_bins: np.arange(0, end - width + step, step)."""
    return np.arange(0, end - width + step, step)


def zcounts(spikes, onsets, starts, width, mu, sd):
    """Counts in [onset + s, onset + s + width) for each trial and window start, z-scored as in
    the code: (count - fixation mean rate) / fixation s.d. of rate, raw counts when s.d. is 0."""
    a = onsets[:, None] + starts[None, :]
    c = count_in(spikes, a.ravel(), (a + width).ravel()).reshape(a.shape).astype(float)
    return (c - mu) / sd if sd > 0 else c


def pseudo_rows(T, subs, load, reading, final=None):
    """Trial alignment of a pseudo-population. Returns ({sub: trial numbers}, labels).
    reading 'code': the rows of the code's identity-matched table (data/new_trial_final.xlsx,
    trial_id_final) at this load, in trial_id_final order, labels from subject 14 as in the code
    (main_2f,supp_1g.py:11; the label is the first image for load 1, the second for load 2, the
    third for load 3). reading 'rank': for each participant the first k trials of each image (the
    image at position = load) in trial order, aligned by image and rank, with k = 6 or the smallest
    count over participants and images if lower."""
    if reading == "code":
        f = final[final.num_images_presented == load].sort_values(["subject_id", "trial_id_final"])
        rows = {s: f[f.subject_id == s].sort_values("trial_id_final").trial_id.values for s in subs}
        lab = f[f.subject_id == 14].sort_values("trial_id_final")[f"stimulus_index_enc{load}"].values
        return rows, lab
    col = {1: "img1", 2: "img2", 3: "img3"}[load]
    k = 6
    for s in subs:
        t = T[s][T[s].load == load]
        k = min(k, t[col].value_counts().min())
    rows = {}
    for s in subs:
        t = T[s][T[s].load == load]
        rows[s] = np.concatenate([t[t[col] == im].trial.values[:k] for im in range(1, 6)])
    lab = np.repeat(np.arange(1, 6), k)
    return rows, lab


def psth_z(spikes, onsets, dur, mu, sd, bin_size=0.05, smooth=True):
    """Trial x bin firing rate in 50 ms bins from each onset, z-scored with the fixation mean and
    s.d. of rate, then smoothed across bins with a Gaussian of sigma one bin (Methods,
    Electrophysiology)."""
    from scipy.ndimage import gaussian_filter1d
    nb = int(round(dur / bin_size))
    st = np.arange(nb) * bin_size
    a = onsets[:, None] + st[None, :]
    c = count_in(spikes, a.ravel(), (a + bin_size).ravel()).reshape(a.shape) / bin_size
    z = (c - mu) / sd if sd > 0 else c - mu
    return gaussian_filter1d(z, 1, axis=1, mode="nearest") if smooth else z


def bh(p):
    from statsmodels.stats.multitest import multipletests
    p = np.asarray(p, float)
    return multipletests(p, method="fdr_bh")[1] if len(p) else p


def perm_null_loo(K, y, n_perm, seed):
    """LOOCV accuracies of the SVM with labels shuffled n_perm times (the code permutes the labels
    of all trials, then runs the same LOOCV; main_2f,supp_1g.py:77-83)."""
    rng = np.random.default_rng(seed)
    return np.array([loo_correct(K, rng.permutation(y)).mean() for _ in range(n_perm)])


def ct_perm_maps(X, y, seeds):
    """Cross-temporal accuracy maps with shuffled labels, one per seed."""
    return [loo_cross_temporal(X, np.random.default_rng(s).permutation(y)) for s in seeds]


def pmap(func, args_list, n_jobs=4):
    """Run func(*args) for each args in parallel processes (joblib)."""
    from joblib import Parallel, delayed
    return Parallel(n_jobs=n_jobs)(delayed(func)(*a) for a in args_list)


CODE_REPO = "https://raw.githubusercontent.com/dariakussovska/heterogeneitywm"
CODE_COMMIT = "5144fe80876d14e8aacb4044977c3474c454f14b"


def code_table(path):
    """A table shipped in the paper's code repository, read over HTTP at the pinned commit."""
    import io
    r = requests.get(f"{CODE_REPO}/{CODE_COMMIT}/{path}", timeout=120)
    r.raise_for_status()
    return pd.read_excel(io.BytesIO(r.content))


def stable_seed(*parts):
    """A seed from names and numbers that does not change between runs (Python's hash does)."""
    import zlib
    return zlib.crc32("|".join(map(str, parts)).encode())


def type_shuffle_null(py_trials, in_trials, win, rng, n_shuffle=100, rule="prominence", distance=2):
    """Null burst counts for the PY and IN groups of one participant from shuffling the cell-type
    labels among its PY and IN neurons, group sizes kept (a reading of the Results' 'label-shuffled
    null'). Returns (mean null count for the PY-sized group, for the IN-sized group)."""
    pool = list(py_trials) + list(in_trials)
    k = len(py_trials)
    n_tr = len(pool[0])
    outp, outi = [], []
    for _ in range(n_shuffle):
        perm = rng.permutation(len(pool))
        for sel, out in [(perm[:k], outp), (perm[k:], outi)]:
            pooled = np.concatenate([concat_trials(pool[j], win) for j in sel])
            sm = smooth_counts(pooled, n_tr * win)
            out.append(len(burst_peaks(sm, np.percentile(sm, BURST_PCT), rule, distance)))
    return float(np.mean(outp)), float(np.mean(outi))
