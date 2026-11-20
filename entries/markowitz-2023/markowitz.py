"""Loading and shared measures for Markowitz et al. (2023) on dandiset 000559.

Parameters and where they come from:
- dLight processing (Methods, Photometry pre-processing and Photometry active
  referencing, as the claims file's definitions give them): the files' dF/F of
  the 470 nm and 405 nm channels (taken as the Methods' dF/F0; the files call
  them SignalDfOverF and ReferenceDfOverF), the reference low-passed by a
  second-order Butterworth at 3 Hz, fitted to dLight by RANSAC with slope and
  bias, subtracted, and z-scored in a centred 20-s (600-sample) sliding window.
- Quality control (claims file, definitions): (a) the Methods' maximum
  percentage dF/F0 above 1.5 and dLight-to-reference correlation below 0.6;
  (b) the code's rule (signal.py, compute_photometry_quality_metrics; io/df.py,
  dlight_exclude as the claims file gives it): the 90th percentile of the
  exponentially smoothed dF/F (window 50, tau 10) in percent above 1.5, the
  correlation of the smoothed dLight and reference dF/F below 0.6, and no raw
  dF/F value above 1.0. The smoothing kernel is scipy's symmetric exponential
  window of 50 samples with tau 10, normalised to sum 1 (an assumption on how
  "window 50, tau 10" is implemented; the code is outside the claims file).
- Syllable-associated dLight (Methods, "Analysing the relationship between
  dLight and syllable statistics within an experiment across syllables"): the
  maximum z-scored dLight from syllable onset to 300 ms after, inclusive
  (10 samples at 30 Hz).
- Syllables: run-length instances of the per-frame labels; offline labels for
  photometry, online labels for the Opto-DA experiments (Methods, Offline
  variant, as the claims file reads it).
- Opto-DA session numbers (claims file, definitions; the files' TargetSessions
  table): -1 and 0 baseline, 1 and 2 stimulation, 3 and 4 post.
- The number of worker processes is a standard choice that does not change a
  result.
"""
import re
import numpy as np
import pandas as pd
import requests

DANDISET = "000559"
VERSION = "0.261113.1911"
API = "https://api.dandiarchive.org/api"
FS = 30.0


def list_assets():
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=1000"
    out = []
    while url:
        r = requests.get(url, timeout=60)
        r.raise_for_status()
        j = r.json()
        out += j["results"]
        url = j["next"]
    df = pd.DataFrame([dict(path=a["path"], asset_id=a["asset_id"], size=a["size"]) for a in out
                       if a["path"].endswith(".nwb")])
    df["subject"] = df.path.str.split("/").str[0].str.replace("sub-", "", regex=False)
    df["kind"] = df.path.str.extract(r"_ses-([a-z-]+?)-[0-9a-f]{8}-")[0]
    df.loc[df.path.str.contains("_ses-keypoint"), "kind"] = "keypoint"
    return df


def _open(asset_id):
    import h5py
    import remfile
    url = f"{API}/assets/{asset_id}/download/"
    for _ in range(5):
        try:
            loc = requests.get(url, allow_redirects=False, timeout=60).headers["Location"]
            return h5py.File(remfile.File(loc), "r")
        except Exception:
            import time
            time.sleep(5)
    raise RuntimeError(f"could not open asset {asset_id}")


def _s(x):
    return x.decode() if isinstance(x, bytes) else x


def _meta(f):
    d = dict(subject=_s(f["general/subject/subject_id"][()]),
             start=pd.Timestamp(_s(f["session_start_time"][()])),
             session_description=_s(f["session_description"][()]))
    m = re.search(r"Lab group code: ([^.]+)\.", _s(f["general/subject/description"][()]))
    d["group"] = m.group(1) if m else ""
    b = f["processing/behavior"]
    if "TargetSessions" in b:
        ts = b["TargetSessions"]
        for k in ts:
            if k != "id":
                d["ts_" + k] = [_s(x) for x in ts[k][()]]
    return d


def runs(labels):
    """Run-length instances of a per-frame label series: start index, label."""
    labels = np.asarray(labels)
    ch = np.flatnonzero(np.diff(labels.astype(int)) != 0) + 1
    starts = np.r_[0, ch]
    return starts, labels[starts]


def _nearest_index(t_src, t_dst):
    """Index into t_src of the last sample at or before each time of t_dst."""
    i = np.searchsorted(t_src, t_dst, side="right") - 1
    return np.clip(i, 0, len(t_src) - 1)


def rolling_z(x, win=600):
    s = pd.Series(x)
    m = s.rolling(win, center=True, min_periods=win // 2).mean()
    sd = s.rolling(win, center=True, min_periods=win // 2).std()
    return ((s - m) / sd).to_numpy()


def qc_code(sig, ref):
    """Quality-control metrics of reading (b) (module docstring)."""
    from scipy.signal.windows import exponential
    w = exponential(50, tau=10)
    w = w / w.sum()
    ok = np.isfinite(sig) & np.isfinite(ref)
    s_ = np.convolve(np.where(ok, sig, 0), w, mode="same")
    r_ = np.convolve(np.where(ok, ref, 0), w, mode="same")
    return dict(qcb_p90_pct=float(np.percentile(s_, 90) * 100), qcb_corr=float(np.corrcoef(s_, r_)[0, 1]),
                qcb_raw_max=float(np.nanmax(sig)))


def process_dlight(sig, ref, seed=0, return_rr=False, intercept=True):
    """Re-referenced, sliding-window z-scored dLight (module docstring). With `return_rr`, also
    the re-referenced trace before the sliding z-score. `intercept=False` fits the reference without
    a bias, as photometry/signal.py rereference does in the fig_s03 notebook (the claims file's variant)."""
    from scipy.signal import butter, filtfilt
    from sklearn.linear_model import RANSACRegressor, LinearRegression
    b, a = butter(2, 3.0 / (FS / 2), "low")
    ok = np.isfinite(sig) & np.isfinite(ref)
    sig = np.where(ok, sig, np.nanmedian(sig))
    ref = np.where(ok, ref, np.nanmedian(ref))
    ref_lp = filtfilt(b, a, ref)
    # RANSAC's random subsets are a standard choice that does not change the fit materially
    r = RANSACRegressor(LinearRegression(fit_intercept=intercept), random_state=seed).fit(ref_lp[:, None], sig)
    rr = sig - r.predict(ref_lp[:, None])
    if return_rr:
        return rolling_z(rr), float(np.corrcoef(sig, ref)[0, 1]), rr
    return rolling_z(rr), float(np.corrcoef(sig, ref)[0, 1])


def load_photometry(row):
    """One photometry session reduced to the 30 Hz dLight grid."""
    asset_id = row["asset_id"]
    with _open(asset_id) as f:
        d = _meta(f)
        d.update(path=row["path"], has_ophys="processing/ophys/SignalDfOverF" in f)
        b = f["processing/behavior"]
        if "BehavioralSyllableOffline" in b:
            st = b["BehavioralSyllableOffline/timestamps"][()]
            sl = b["BehavioralSyllableOffline/data"][()]
        else:
            st = sl = None
        if "BehavioralSyllableOnline" in b:
            ot = b["BehavioralSyllableOnline/timestamps"][()]
            ol = b["BehavioralSyllableOnline/data"][()]
        else:
            ot = ol = None
        g = "processing/behavior/moseq_extract_group/"
        et = f[g + "speed_2d/timestamps"][()]
        sp = f[g + "speed_2d/data"][()]
        av = f[g + "angular_velocity_2d/data"][()]
        pos = f[g + "position/position/data"][()]
        if d["has_ophys"]:
            t = f["processing/ophys/SignalDfOverF/timestamps"][()]
            sig = f["processing/ophys/SignalDfOverF/data"][()]
            ref = f["processing/ophys/ReferenceDfOverF/data"][()]
    d["syl_sorted"] = bool(st is None or np.all(np.diff(st) >= 0))
    if not d["has_ophys"]:
        # behaviour only: keep the offline syllable series on its own clock
        d["t"] = st.astype(np.float64) if st is not None else None
        d["syl"] = sl.astype(np.int16) if sl is not None else None
        return d
    z, corr, rr = process_dlight(sig, ref, return_rr=True)
    d.update(qc_code(sig, ref))
    # clock ranges of the photometry and syllable series, for the alignment check
    d["t_range"] = (float(t[0]), float(t[-1]))
    d["syl_range"] = (float(st.min()), float(st.max())) if st is not None else None
    d["ext_range"] = (float(et[0]), float(et[-1]))
    d["t"] = t
    d["z"] = z.astype(np.float32)
    d["rr"] = rr.astype(np.float32)
    d["dff"] = sig.astype(np.float32)
    d["qc_max_pct"] = float(np.nanmax(sig) * 100)
    d["qc_corr"] = corr
    d["fs_check"] = float(np.median(np.diff(t)))
    d["syl"] = sl[_nearest_index(st, t)].astype(np.int16) if st is not None else None
    d["syl_on"] = ol[_nearest_index(ot, t)].astype(np.int16) if ot is not None else None
    ie = _nearest_index(et, t)
    d["speed"] = (sp[ie] * FS).astype(np.float32)          # mm/frame -> mm/s
    d["angvel"] = (av[ie] * FS).astype(np.float32)         # rad/frame -> rad/s
    d["height"] = pos[ie, 2].astype(np.float32)
    d["xy"] = pos[ie, :2].astype(np.float32)
    return d


def load_opto(row):
    """One Opto-DA session reduced to online-label syllable instances."""
    with _open(row["asset_id"]) as f:
        d = _meta(f)
        d["path"] = row["path"]
        b = f["processing/behavior"]
        ot = b["BehavioralSyllableOnline/timestamps"][()]
        ol = b["BehavioralSyllableOnline/data"][()]
        if "BehavioralSyllableOffline" in b:
            ft = b["BehavioralSyllableOffline/timestamps"][()]
            fl = b["BehavioralSyllableOffline/data"][()]
            fs_, flab = runs(fl[np.argsort(ft, kind="stable")])
            fon = np.sort(ft)[fs_]
            d["off_inst"] = pd.DataFrame(dict(label=flab.astype(np.int16), dur=np.r_[np.diff(fon), np.nan].astype(np.float32)))
        g = "processing/behavior/moseq_extract_group/"
        has_ext = "moseq_extract_group" in b
        if has_ext:
            et = f[g + "speed_2d/timestamps"][()]
            sp = f[g + "speed_2d/data"][()]
            av = f[g + "angular_velocity_2d/data"][()]
            pos = f[g + "position/position/data"][()]
        if "TargetDetections" in b:
            td = b["TargetDetections"]
            d["det_time"] = td["time"][()]
            d["det_stim"] = td["stimulated"][()].astype(bool)
            d["det_target"] = td["target_syllable"][()]
        else:
            d["det_time"] = np.array([])
            d["det_stim"] = np.array([], bool)
            d["det_target"] = np.array([], int)
        if "stimulus/presentation/OptogeneticSeries" in f:
            od = f["stimulus/presentation/OptogeneticSeries/data"][()]
            otm = f["stimulus/presentation/OptogeneticSeries/timestamps"][()]
            # the series' description says onsets are 1, but the values are the power (0.01 W)
            d["stim_on"] = otm[od > 0]
        else:
            d["stim_on"] = np.array([])
    d["syl_sorted"] = bool(np.all(np.diff(ot) >= 0))
    o = np.argsort(ot, kind="stable")
    ot, ol = ot[o], ol[o]
    s, lab = runs(ol)
    on = ot[s]
    dur = np.r_[np.diff(on), np.nan]
    inst = pd.DataFrame(dict(onset=on, label=lab.astype(int), dur=dur))
    if has_ext:
        spd = sp * FS
        hv = np.r_[0, np.diff(pos[:, 2])] * FS
        acc = np.r_[0, np.diff(spd)] * FS
        avs = av * FS
        ie_on = _nearest_index(et, on)
        ie_off = np.r_[ie_on[1:], len(et)]
        cs = lambda x: np.r_[0, np.nancumsum(x)]
        n = np.maximum(ie_off - ie_on, 1)
        for name, x in [("vel", spd), ("angvel", avs), ("hvel", hv), ("acc", acc)]:
            c = cs(x)
            inst[name] = (c[np.maximum(ie_off, ie_on + 1)] - c[ie_on]) / n
        inst["x"] = pos[ie_on, 0]
        inst["y"] = pos[ie_on, 1]
    d["inst"] = inst
    d["t_first"] = float(ot[0])
    d["t_last"] = float(ot[-1])
    return d


def load_many(fn, rows, procs=16):
    from multiprocessing import get_context
    with get_context("fork").Pool(procs) as p:
        return p.map(fn, rows, chunksize=1)


# ---------------------------------------------------------------- measures

def instances(sess, use_online=False):
    """Syllable instances of a photometry session with their syllable-associated dLight."""
    lab = sess["syl_on"] if use_online else sess["syl"]
    s, l = runs(lab)
    z = sess["z"]
    n = len(z)
    # max over onset .. onset + 9 samples (0 to 0.3 s inclusive)
    idx = s[:, None] + np.arange(10)[None, :]
    idx = np.clip(idx, 0, n - 1)
    da = np.nanmax(z[idx], axis=1)
    on_next = np.r_[s[1:], n]
    cs = np.r_[0, np.nancumsum(sess["speed"])]
    vel = (cs[on_next] - cs[s]) / np.maximum(on_next - s, 1)
    ca = np.r_[0, np.nancumsum(sess["angvel"])]
    av = (ca[on_next] - ca[s]) / np.maximum(on_next - s, 1)
    cz = np.r_[0, np.nancumsum(z)]
    zmean = (cz[on_next] - cz[s]) / np.maximum(on_next - s, 1)
    return pd.DataFrame(dict(start=s, label=l.astype(int), da=da, dur=(on_next - s) / FS,
                             onset=sess["t"][s], vel=vel, angvel=av, zmean=zmean))


def holm(p):
    p = np.asarray(p, float)
    o = np.argsort(p)
    m = len(p)
    adj = np.empty(m)
    run = 0
    for k, i in enumerate(o):
        run = max(run, (m - k) * p[i])
        adj[i] = min(1, run)
    return adj


def dm_entropy(counts, prior):
    """Entropy (bits) of each row of a transition count matrix with a pseudo-count prior."""
    c = counts + prior
    p = c / c.sum(axis=1, keepdims=True)
    return -(p * np.log2(p)).sum(axis=1)


def cles(u, n1, n2):
    """Common-language effect size f of a Mann-Whitney U."""
    return u / (n1 * n2)


def load_keypoint(row):
    """A keypoint session: raw dLight and reference F, spine and forepaw keypoints (mm, 30 Hz).
    dF/F0 with F0 the 10th percentile in a centred 5-s window (Methods, Photometry pre-processing)."""
    with _open(row["asset_id"]) as f:
        d = dict(subject=_s(f["general/subject/subject_id"][()]), path=row["path"])
        sig = f["processing/ophys/SignalF/data"][()].astype(float)
        ref = f["processing/ophys/UVReferenceF/data"][()].astype(float)
        d["t"] = f["processing/ophys/SignalF/timestamps"][()]
        kp = "processing/behavior/keypoints/"
        d["rate"] = float(f[kp + "medial_spine/starting_time"].attrs["rate"])
        d["kp_start"] = float(f[kp + "medial_spine/starting_time"][()])
        for k in ["rostral_spine", "medial_spine", "caudal_spine", "left_forepaw", "right_forepaw"]:
            d[k] = f[kp + k + "/data"][()].astype(float)
    f0 = lambda x: pd.Series(x).rolling(150, center=True, min_periods=75).quantile(0.10).to_numpy()
    dff_s = (sig - f0(sig)) / f0(sig)
    dff_r = (ref - f0(ref)) / f0(ref)
    d["z"], d["refcorr"] = process_dlight(dff_s, dff_r)
    d["z_noint"], _ = process_dlight(dff_s, dff_r, intercept=False)
    return d
