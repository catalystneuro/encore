"""Loading and measures for Wang et al. (2025) on DANDI:000363 (Mesoscale Activity Map).

Streams NWB files from the archive; nothing is written to disk.

Where each parameter comes from:
- DANDI version 0.230822.0128: the version the paper cites (ref. 30's DANDI DOI
  10.48324/dandi.000363/0.230822.0128).
- Trial exclusions (photoinhibition, free water, early licks, no response): Methods,
  "Trial selection and cross-validation". Correct trials only, 20-fold stratified
  cross-validation for behavioural prediction: same passage.
- Delay epoch -1.2 to 0 s from the go cue: claims file opening comment (the code's epochs).
- Marker outliers by a five-sigma threshold on frame-to-frame velocity, imputed from nearby
  frames: Methods, "Neural recording and video" paragraph ("We identified outliers by a
  five-sigma threshold on velocity across frames and imputed outliers from nearby frames").
  Linear interpolation is the imputation used here, a standard choice (the Methods say other
  imputations did not change the results).
- Five-frame feature window t-6.8 to t+6.8 ms: claims file, fig6a-choice-from-video reading (a)
  (Methods, Prediction of neural activity); single frame is reading (b).
- L2 logistic regression with the penalty chosen by nested 5-fold cross-validation from
  C in 0.01, 0.1, 1, 10, 100: claims file, fig6a reading of the decoder and the grid of
  the paper's code (functions_for_r2.calculate_auc, cited in edfig10-subtraction-consistent).
- Decoding every 10th frame (34 ms) inside the epoch: a standard subsampling to keep the run
  short; the epoch AUC is a mean over time bins and cannot depend on it beyond noise.
- Calinski-Harabasz score with a null of 1,000 random reassignments of the mouse labels:
  Methods, "Calinski-Harabasz clustering score".
- Area grouping of CCF annotations (area2anno.json) from the authors' processed-data deposit,
  Zenodo doi:10.5281/zenodo.16740783, named in the claims file.
"""
import io
import json
import struct
import zipfile
import zlib

import h5py
import numpy as np
import remfile
import requests

DANDISET = "000363"
VERSION = "0.230822.0128"
API = "https://api.dandiarchive.org/api"
ZENODO_ZIP = ("https://zenodo.org/api/records/16740783/files/"
              "MapVideoAnalysisProcessedData.zip/content")
FRAME_DT = 0.0034          # frame step of the marker timestamps (s), checked in the notebook
DELAY = (-1.2, 0.0)        # delay epoch relative to the go cue (s)
CS = [0.01, 0.1, 1, 10, 100]


def list_assets(version=VERSION):
    url = f"{API}/dandisets/{DANDISET}/versions/{version}/assets/?page_size=1000"
    out = []
    while url:
        r = requests.get(url).json()
        out += r["results"]
        url = r.get("next")
    return sorted(out, key=lambda a: a["path"])


def open_asset(asset_id):
    url = f"{API}/assets/{asset_id}/download/"
    url = requests.head(url, allow_redirects=True).url
    return h5py.File(remfile.File(url), "r")


def _str(a):
    return np.array([x.decode() if isinstance(x, bytes) else str(x) for x in a])


def session_key(f):
    """Name used by the authors' files: <subject description>_<MMDDYY>."""
    desc = f["general/subject/description"][()].decode()
    st = f["session_start_time"][()].decode()  # 2019-02-08T13:36:00...
    return f"{desc}_{st[5:7]}{st[8:10]}{st[2:4]}"


def units_table(f):
    u = f["units"]
    eg = u["electrode_group"][:]
    groups = [f[r].name.split("/")[-1] for r in eg]
    gloc = {}
    for g in set(groups):
        loc = f[f"general/extracellular_ephys/{g}"].attrs.get("location", "")
        gloc[g] = loc
    return dict(
        anno=_str(u["anno_name"][:]),
        quality=_str(u["unit_quality"][:]),
        classification=_str(u["classification"][:]),
        rate=u["avg_firing_rate"][:],
        group=np.array(groups),
        group_location=np.array([gloc[g] for g in groups]),
    )


def trials_table(f):
    t = f["intervals/trials"]
    d = dict(
        start=t["start_time"][:], stop=t["stop_time"][:],
        outcome=_str(t["outcome"][:]), early=_str(t["early_lick"][:]),
        free_water=t["free_water"][:], auto_water=t["auto_water"][:],
        photostim=_str(t["photostim_onset"][:]),
        instruction=_str(t["trial_instruction"][:]),
    )
    go = f["acquisition/BehavioralEvents/go_start_times/timestamps"][:]
    nxt = np.r_[d["start"][1:], np.inf]
    gc = np.full(len(d["start"]), np.nan)
    for i, (a, b) in enumerate(zip(d["start"], nxt)):
        k = go[(go >= a) & (go < b)]
        if len(k):
            gc[i] = k[0]
    d["go"] = gc
    d["included"] = ((d["outcome"] != "ignore") & (d["early"] == "no early")
                     & (d["free_water"] == 0) & (d["auto_water"] == 0)
                     & (d["photostim"] == "N/A") & np.isfinite(gc))
    d["correct"] = d["included"] & (d["outcome"] == "hit")
    return d


def clean_marker(xy):
    """Five-sigma velocity outliers replaced by linear interpolation (Methods)."""
    xy = xy.astype(float).copy()
    v = np.r_[0.0, np.hypot(*np.diff(xy, axis=0).T)]
    bad = np.abs(v - v.mean()) > 5 * v.std()
    good = ~bad
    idx = np.arange(len(xy))
    for c in range(xy.shape[1]):
        xy[bad, c] = np.interp(idx[bad], idx[good], xy[good, c])
    return xy, int(bad.sum())


def load_marker(f, name, camera="Camera0"):
    g = f[f"acquisition/BehavioralTimeSeries/{camera}_side_{name}Tracking"]
    return g["data"][:, :2], g["timestamps"][:], g["data"][:, 2]


def marker_epoch(xy, ts, go, window=DELAY, stride=10, half=2):
    """Array (trials, bins, 2*(2*half+1)) of marker positions at frames t-half..t+half,
    for bins every `stride` frames from window[0] to window[1] relative to each go cue.
    Trials whose frames are not all present (gaps in the timestamps) are NaN."""
    nb = int(round((window[1] - window[0]) / FRAME_DT)) // stride
    offs = (np.arange(nb) * stride)[:, None] + np.arange(-half, half + 1)[None, :]
    out = np.full((len(go), nb, xy.shape[1] * (2 * half + 1)), np.nan)
    for i, g in enumerate(go):
        t0 = g + window[0]
        k = np.searchsorted(ts, t0)
        if k - half < 0 or k + offs.max() >= len(ts):
            continue
        idx = k + offs
        if abs(ts[k] - t0) > FRAME_DT or np.any(np.abs(np.diff(ts[idx.min():idx.max() + 1]) - FRAME_DT) > 1e-3):
            continue
        out[i] = xy[idx].reshape(nb, -1)
    return out


def decode_auc(X, y, seed, n_splits=20, cs=CS):
    """Per time bin: out-of-fold probabilities from L2 logistic regression with the penalty
    chosen by inner 5-fold cross-validation, 20-fold stratified outer split; one ROC AUC
    over all test predictions per bin. Returns the AUC per bin."""
    from sklearn.linear_model import LogisticRegressionCV
    from sklearn.metrics import roc_auc_score
    from sklearn.model_selection import StratifiedKFold
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler
    outer = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=seed)
    inner = StratifiedKFold(n_splits=5, shuffle=True, random_state=seed + 1)
    aucs = np.zeros(X.shape[1])
    for b in range(X.shape[1]):
        p = np.zeros(len(y))
        for tr, te in outer.split(X[:, b], y):
            m = make_pipeline(StandardScaler(), LogisticRegressionCV(
                Cs=cs, cv=inner, scoring="roc_auc", max_iter=1000))
            m.fit(X[tr, b], y[tr])
            p[te] = m.predict_proba(X[te, b])[:, 1]
        aucs[b] = roc_auc_score(y, p)
    return aucs


def _auc(y, s):
    """ROC AUC by the Mann-Whitney rank formula (ties averaged)."""
    from scipy.stats import rankdata
    r = rankdata(s)
    n1 = y.sum()
    n0 = len(y) - n1
    return (r[y == 1].sum() - n1 * (n1 + 1) / 2) / (n1 * n0)


def _auc_rows(y, S):
    """ROC AUC of each row of S against labels y."""
    from scipy.stats import rankdata
    r = rankdata(S, axis=1)
    n1 = y.sum()
    n0 = len(y) - n1
    return (r[:, y == 1].sum(1) - n1 * (n1 + 1) / 2) / (n1 * n0)


def _fit_batch(X, y, W, C, iters=30):
    """L2 logistic regression fitted for many problems at once by Newton's method.
    X (n, p) shared design; W (B, n) 0/1 sample weights (the training set of each problem);
    C (B,) inverse penalties as in sklearn (loss = sum log-loss + ||w||^2 / (2C), intercept
    unpenalised). Each problem standardises X with its own training mean and s.d.
    Returns a function giving decision values for all n samples, shape (B, n)."""
    B, n = W.shape
    cnt = W.sum(1, keepdims=True)
    mu = (W @ X) / cnt
    sd = np.sqrt(np.maximum((W @ X ** 2) / cnt - mu ** 2, 1e-12))
    Z = (X[None] - mu[:, None]) / sd[:, None]
    Z = np.concatenate([np.ones((B, n, 1)), Z], axis=2)
    p = Z.shape[2]
    w = np.zeros((B, p))
    pen = np.ones(p)
    pen[0] = 0
    P = (1.0 / C)[:, None] * pen[None]
    Zt = Z.transpose(0, 2, 1)
    for _ in range(iters):
        eta = (Z @ w[..., None])[..., 0]
        m = 1 / (1 + np.exp(-eta))
        g = (Zt @ (W * (m - y[None]))[..., None])[..., 0] + P * w
        h = W * m * (1 - m)
        H = Zt @ (Z * h[..., None]) + P[:, :, None] * np.eye(p)[None]
        step = np.linalg.solve(H, g[..., None])[..., 0]
        w -= step
        if np.abs(step).max() < 1e-8:
            break
    return (Z @ w[..., None])[..., 0]


def decode_auc_fast(X, y, seed, n_splits=20, cs=CS, n_inner=5):
    """Same procedure as decode_auc (nested choice of C by mean inner-fold ROC AUC, refit
    on the outer training set, one AUC over the pooled out-of-fold predictions per bin),
    fitted in batches by _fit_batch. Returns the AUC per bin."""
    from sklearn.model_selection import StratifiedKFold
    n = len(y)
    outer = list(StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=seed).split(np.zeros(n), y))
    probs, Cs, groups = [], [], []
    for k, (tr, te) in enumerate(outer):
        inner = StratifiedKFold(n_splits=n_inner, shuffle=True, random_state=seed + 1)
        for itr, iva in inner.split(np.zeros(len(tr)), y[tr]):
            groups.append((k, tr[iva], list(range(len(probs), len(probs) + len(cs)))))
            for c in cs:
                wv = np.zeros(n)
                wv[tr[itr]] = 1
                probs.append(("in", k, tr[iva], wv))
                Cs.append(c)
        for c in cs:
            wv = np.zeros(n)
            wv[tr] = 1
            probs.append(("out", k, te, wv))
            Cs.append(c)
    W = np.array([p[3] for p in probs])
    Cs = np.array(Cs, float)
    aucs = np.zeros(X.shape[1])
    for b in range(X.shape[1]):
        D = _fit_batch(X[:, b], y.astype(float), W, Cs)
        score = {}
        for k, idx, rows in groups:
            a = _auc_rows(y[idx], D[np.ix_(rows, idx)])
            for r, v in zip(rows, a):
                score.setdefault((k, Cs[r]), []).append(v)
        pred = np.zeros(n)
        for i, (kind, k, idx, _) in enumerate(probs):
            if kind == "out":
                best = max(cs, key=lambda c: (np.mean(score[(k, c)]), -c))
                if Cs[i] == best:
                    pred[idx] = D[i, idx]
        aucs[b] = _auc(y, pred)
    return aucs


def ch_null(X, labels, rng, n=1000):
    from sklearn.metrics import calinski_harabasz_score
    obs = calinski_harabasz_score(X, labels)
    null = np.array([calinski_harabasz_score(X, rng.permutation(labels)) for _ in range(n)])
    return obs, null, float(np.mean(null >= obs))


# Authors' processed-data deposit (Zenodo zip): read single members by HTTP range requests.
def zenodo_member(name):
    z = zipfile.ZipFile(remfile.File(ZENODO_ZIP))
    i = z.getinfo(name)
    h = requests.get(ZENODO_ZIP, headers={"Range": f"bytes={i.header_offset}-{i.header_offset + 29}"}).content
    n, m = struct.unpack("<HH", h[26:30])
    s = i.header_offset + 30 + n + m
    data = requests.get(ZENODO_ZIP, headers={"Range": f"bytes={s}-{s + i.compress_size - 1}"}).content
    return zlib.decompress(data, -15) if i.compress_type == 8 else data


def area_map():
    """Area name -> list of CCF annotation names (commas removed), area2anno.json."""
    return json.loads(zenodo_member("area2anno.json"))


SEED_OFFSETS = (0, 1000, 2000, 3000, 4000)
STRIDE = 20   # decode every 20th frame (68 ms) in the delay epoch: a standard subsampling


def bin_times(window=DELAY, stride=STRIDE):
    nb = int(round((window[1] - window[0]) / FRAME_DT)) // stride
    return window[0] + np.arange(nb) * stride * FRAME_DT


def _fingerprint(a):
    import hashlib
    return hashlib.md5(np.ascontiguousarray(a).tobytes()).hexdigest()[:12]


def session_summary(asset, seed):
    """Everything the notebook uses from one session, read in one pass.
    seed: the claim's seed for the choice decoders; the decoders are also run under
    seed + 1000 ... 4000 (reading (a) only) for the seed check."""
    import os
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    f = open_asset(asset["asset_id"])
    out = dict(path=asset["path"], key=session_key(f),
               subject=f["general/subject/subject_id"][()].decode())
    U = units_table(f)
    out["units"] = U
    st = f["units/spike_times"]
    out["fp_spikes"] = _fingerprint(st[:2000])
    T = trials_table(f)
    out["fp_trials"] = _fingerprint(T["start"])
    out["n_trials"] = len(T["start"])
    out["n_included"] = int(T["included"].sum())
    out["n_correct"] = int(T["correct"].sum())
    out["n_go_missing"] = int(np.isnan(T["go"]).sum())
    out["performance"] = float(T["correct"].sum() / max(T["included"].sum(), 1))
    out["excluded"] = {k: int(v.sum()) for k, v in dict(
        ignore=T["outcome"] == "ignore", early=T["early"] != "no early",
        free_water=T["free_water"] != 0, auto_water=T["auto_water"] != 0,
        photostim=T["photostim"] != "N/A").items()}
    out["cameras"] = sorted(f["acquisition/BehavioralTimeSeries"].keys())
    c = T["correct"]
    y = (T["instruction"][c] == "left").astype(int)
    out["n_left"], out["n_right"] = int(y.sum()), int((1 - y).sum())
    go = T["go"][c]
    # clock check: tongue and lick events against the go cue
    txy, tts, tlk = load_marker(f, "Tongue")
    d = np.diff(tts)
    out["frame_dt"] = dict(median=float(np.median(d)), within_1us=float(np.mean(np.abs(d - FRAME_DT) < 1e-6)),
                           n_gaps=int((d > 0.01).sum()), n_frames=len(tts), t0=float(tts[0]), t1=float(tts[-1]))
    out["fp_jaw"] = None
    vis = tlk > 0.9
    rel = np.arange(-1.0, 1.0, 0.1)
    ig = T["go"][T["included"]]
    prof = []
    for r in rel:
        k = np.searchsorted(tts, ig + r)
        k = np.clip(k, 0, len(tts) - 30)
        prof.append(float(np.mean([vis[j:j + 29].mean() for j in k])))
    out["tongue_vs_go"] = (rel.tolist(), prof)
    licks = np.concatenate([f[f"acquisition/BehavioralEvents/{s}_lick_times/timestamps"][:] for s in ("left", "right")])
    lk_out = {}
    for sh in (0.0, 0.05, 0.1, -0.05):
        k = np.clip(np.searchsorted(tts, licks + sh), 1, len(tts) - 2)
        ok = np.abs(tts[k] - (licks + sh)) < 2 * FRAME_DT
        lk_out[sh] = float(np.mean(vis[k[ok]] | vis[k[ok] - 1] | vis[k[ok] + 1])) if ok.any() else np.nan
    out["tongue_at_licks"] = lk_out
    out["n_licks"] = len(licks)
    # choice decoding from the jaw and the nose
    out["auc"] = {}
    out["outliers"] = {}
    enough = out["n_left"] >= 20 and out["n_right"] >= 20
    out["decoded"] = enough
    for name in ("Jaw", "Nose"):
        xy, ts, _ = load_marker(f, name)
        if name == "Jaw":
            out["fp_jaw"] = _fingerprint(xy[:5000])
        xy, nbad = clean_marker(xy)
        out["outliers"][name] = (nbad, len(xy))
        X = marker_epoch(xy, ts, go, stride=STRIDE)
        ok = ~np.isnan(X).any(axis=(1, 2))
        out.setdefault("n_missing_frames", {})[name] = int((~ok).sum())
        if not enough or (y[ok].sum() < 20 or (1 - y[ok]).sum() < 20):
            continue
        Xo, yo = X[ok], y[ok]
        for off in SEED_OFFSETS:
            out["auc"][(name, "a", off)] = decode_auc_fast(Xo, yo, seed + off)
        out["auc"][(name, "b", 0)] = decode_auc_fast(Xo[:, :, 4:6], yo, seed)
    f.close()
    return out


def session_summary_retry(args, tries=3):
    """session_summary with retries on network errors (the archive is read over HTTP)."""
    import time
    asset, seed = args
    for i in range(tries):
        try:
            return session_summary(asset, seed)
        except Exception as e:  # noqa: BLE001
            err = repr(e)
            time.sleep(5 * (i + 1))
    return dict(path=asset["path"], error=err)


def authors_sessions():
    """Session names of the authors' Fig. 6 and 7 file (cal4cat-delay.pickle, Zenodo deposit)."""
    import pickle
    return sorted(str(k) for k in pickle.loads(zenodo_member("cal4cat-delay.pickle")).keys())


def video_read_estimate(n_frames=300):
    """Opens one file of the later version 0.231012.2129, which adds the raw video, and times
    reading n_frames side-view frames. Returns the per-session frame count and the rate."""
    import time
    V = "0.231012.2129"
    assets = list_assets(V)
    vid = [a for a in assets if "+image" in a["path"]]
    r = requests.get(f"{API}/dandisets/{DANDISET}/versions/{V}/assets/{vid[0]['asset_id']}/").json()
    s3 = [u for u in r["contentUrl"] if "s3" in u][0]
    f = h5py.File(remfile.File(s3), "r")
    side = [k for k in f["acquisition"] if "side_face" in k]
    frames = sum(f[f"acquisition/{k}/data"].shape[0] for k in side)
    d = f[f"acquisition/{side[0]}/data"]
    t = time.time()
    d[:n_frames]
    rate = n_frames / (time.time() - t)
    return dict(version=V, n_assets=len(assets), n_video_assets=len(vid),
                bytes_total=sum(a["size"] for a in assets),
                bytes_video_assets=sum(a["size"] for a in vid), example=vid[0]["path"],
                side_series=len(side), side_frames=frames, frame_shape=d.shape[1:],
                frames_per_s=rate)


def lick_alignment(asset, shifts=np.round(np.arange(-1.0, 1.0001, 0.01), 2)):
    """For one session: fraction of lick events with the tongue visible (likelihood > 0.9) within
    one frame, with the lick times shifted by each of `shifts` (s); and how many included trials
    have marker frames at their go cue."""
    f = open_asset(asset["asset_id"])
    T = trials_table(f)
    _, ts, lk = load_marker(f, "Tongue")
    vis = lk > 0.9
    licks = np.concatenate([f[f"acquisition/BehavioralEvents/{s}_lick_times/timestamps"][:] for s in ("left", "right")])
    frac = []
    for sh in shifts:
        k = np.clip(np.searchsorted(ts, licks + sh), 1, len(ts) - 2)
        ok = np.abs(ts[k] - (licks + sh)) < 2 * FRAME_DT
        frac.append(float(np.mean(vis[k[ok]] | vis[k[ok] - 1] | vis[k[ok] + 1])) if ok.any() else np.nan)
    go = T["go"][T["included"]]
    k = np.clip(np.searchsorted(ts, go), 0, len(ts) - 1)
    covered = int(np.sum(np.abs(ts[k] - go) < 2 * FRAME_DT))
    # The video is recorded per trial: each run of frames 3.4 ms apart is one trial's video.
    # Stretch each run from its first frame by a factor and test the licks again.
    gaps = np.where(np.diff(ts) > 0.01)[0]
    starts = np.r_[0, gaps + 1]
    ends = np.r_[gaps, len(ts) - 1]
    seg = np.zeros(len(ts), int)
    seg[starts[1:]] = 1
    seg = np.cumsum(seg)
    s0 = ts[starts][seg]
    stretch = {}
    for fac in (1.0, 1.5, 2.0, 2.5):
        t2 = s0 + (ts - s0) * fac
        kk = np.clip(np.searchsorted(t2, licks), 1, len(t2) - 2)
        ok = np.abs(t2[kk] - licks) < 2 * FRAME_DT * fac
        stretch[fac] = float(np.mean(vis[kk[ok]] | vis[kk[ok] - 1] | vis[kk[ok] + 1])) if ok.any() else np.nan
    per_seg = []
    for a, b in zip(starts, ends):
        L = licks[(licks >= ts[a]) & (licks <= ts[b])]
        if len(L):
            kk = np.clip(np.searchsorted(ts, L), a + 1, b - 1)
            per_seg.append(np.mean(vis[kk] | vis[kk - 1] | vis[kk + 1]))
    per_seg = np.array(per_seg)
    f.close()
    return dict(path=asset["path"], shifts=shifts, frac=np.array(frac), n_licks=len(licks),
                stretch=stretch, segments=len(starts), frames_per_segment=float(np.median(ends - starts + 1)),
                segments_with_licks=len(per_seg), segments_aligned=int(np.sum(per_seg > 0.8)),
                segments_misaligned=int(np.sum(per_seg < 0.3)),
                included=int(T["included"].sum()), included_with_frames=covered,
                video_span=(float(ts[0]), float(ts[-1])), trial_span=(float(T["start"][0]), float(T["stop"][-1])))


def version_fingerprints(asset, version=VERSION):
    """Counts and fingerprints of the units, trials and jaw marker of one file, for comparing
    the same session across versions."""
    if version == VERSION:
        f = open_asset(asset["asset_id"])
    else:
        r = requests.get(f"{API}/dandisets/{DANDISET}/versions/{version}/assets/{asset['asset_id']}/").json()
        f = h5py.File(remfile.File([u for u in r["contentUrl"] if "s3" in u][0]), "r")
    out = dict(units=len(f["units/id"]), spikes=int(f["units/spike_times"].shape[0]),
               fp_spikes=_fingerprint(f["units/spike_times"][:2000]),
               fp_anno=_fingerprint(_str(f["units/anno_name"][:]).astype("U")),
               trials=len(f["intervals/trials/id"]), fp_trials=_fingerprint(f["intervals/trials/start_time"][:]),
               jaw_frames=f["acquisition/BehavioralTimeSeries/Camera0_side_JawTracking/data"].shape[0],
               fp_jaw=_fingerprint(f["acquisition/BehavioralTimeSeries/Camera0_side_JawTracking/data"][:5000]))
    f.close()
    return out
