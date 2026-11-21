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
- Decoding every 20th frame (68 ms, STRIDE) inside the epoch: an assumption made to keep the
  run short (the paper decodes at each time bin); the epoch AUC is a mean over time bins, so
  subsampling the bins changes it by noise only.
- The session AUC of an epoch: the paper does not say how it is formed. Two readings are
  computed. (1) One ROC AUC per time bin over the pooled out-of-fold decision values of the 20
  outer folds, then the mean over bins. (2) The ROC AUC of each test fold, averaged over the
  folds, then over bins, as the Methods do for the other cross-validated measures ("Defining
  choice- and uninstructed movement-modulated neurons using video-based choice decoder": "The
  final AUC for each neuron is the average of the test AUC across all test-folds"; "Epoch-averaged
  explained variance": "After this, the folds were averaged"). Reading (2) is the main one.
- Response epoch 0 to 1.5 s from the go cue, second half 0.75 to 1.5 s: claims file opening
  comment and fig6-marker-vs-embedding-decoding readings (a) and (b).
- Tongue position set to its mean while the tongue is not visible (DeepLabCut likelihood of 0.9
  or less): Methods ("When the tongue was occluded ... we set the tongue position to its mean
  value"); the 0.9 likelihood cut is a standard choice, the one used for the clock check.
- Major divisions of the Allen CCF (Isocortex, olfactory areas, hippocampal formation, cortical
  subplate, striatum, pallidum, thalamus, hypothalamus, midbrain, pons, medulla, cerebellum), with
  isocortex split into ALM and other isocortex: the level of the areas the data-scale criterion
  names. The structure tree is the authors' (mousebrainontology_2.csv for ids and names,
  mousebrainontology_heirarchy_cortexMaskExclusions21_sc.xlsx for the paths), from the deposit.
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
RESPONSE = (0.0, 1.5)      # response epoch relative to the go cue (s)
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


def clean_marker(xy, ts=None):
    """Five-sigma velocity outliers replaced by linear interpolation (Methods). With the
    timestamps ts, no velocity is taken across the gap between two trial videos (> 10 ms).
    A frame is flagged when the velocity into it is an outlier, so a single bad frame also
    flags the frame after it, which is then interpolated too: a conservative choice that
    touches about one frame in 10,000."""
    xy = xy.astype(float).copy()
    v = np.r_[np.nan, np.hypot(*np.diff(xy, axis=0).T)]
    if ts is not None:
        v[1:][np.diff(ts) > 0.01] = np.nan
    with np.errstate(invalid="ignore"):
        bad = np.abs(v - np.nanmean(v)) > 5 * np.nanstd(v)
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
    pen[0] = 1e-8 * C.max()  # a negligible ridge on the intercept keeps H invertible under separation
    P = (1.0 / C)[:, None] * pen[None]
    Zt = Z.transpose(0, 2, 1)
    for _ in range(iters):
        eta = (Z @ w[..., None])[..., 0]
        m = 1 / (1 + np.exp(-np.clip(eta, -35, 35)))
        g = (Zt @ (W * (m - y[None]))[..., None])[..., 0] + P * w
        h = W * m * (1 - m)
        H = Zt @ (Z * h[..., None]) + P[:, :, None] * np.eye(p)[None] + 1e-10 * np.eye(p)[None]
        step = np.linalg.solve(H, g[..., None])[..., 0]
        w -= step
        if np.abs(step).max() < 1e-8:
            break
    return (Z @ w[..., None])[..., 0]


def decode_auc_fast(X, y, seed, n_splits=20, cs=CS, n_inner=5):
    """Same procedure as decode_auc (nested choice of C by mean inner-fold ROC AUC, refit
    on the outer training set), fitted in batches by _fit_batch. Returns two arrays of one
    AUC per bin: (pooled) one ROC AUC over the pooled out-of-fold decision values, and
    (fold mean) the ROC AUC of each outer test fold, averaged over the folds."""
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
    folds = np.zeros(X.shape[1])
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
        folds[b] = np.mean([_auc(y[te], pred[te]) for _, te in outer])
    return aucs, folds


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
STRIDE = 20   # decode every 20th frame (68 ms) in an epoch: an assumption (see the docstring)


def bin_times(window=DELAY, stride=STRIDE):
    nb = int(round((window[1] - window[0]) / FRAME_DT)) // stride
    return window[0] + np.arange(nb) * stride * FRAME_DT


def _fingerprint(a):
    import hashlib
    return hashlib.md5(np.ascontiguousarray(a).tobytes()).hexdigest()[:12]


def tongue_filled(f, ts_cut=0.9):
    """Tongue position, outliers cleaned among the visible frames, and set to its mean value
    while not visible (likelihood <= 0.9; Methods)."""
    xy, ts, lk = load_marker(f, "Tongue")
    xy = xy.astype(float)
    vis = lk > ts_cut
    out = np.empty_like(xy)
    if vis.sum() > 10:
        cv, _ = clean_marker(xy[vis], ts[vis])
        out[vis] = cv
        out[~vis] = cv.mean(0)
    else:
        out[:] = 0.0
    return out, ts


def session_summary(asset, seed, seed_resp=None):
    """Everything the notebook uses from one session, read in one pass.
    seed: the fig6e claim's seed for the delay-epoch choice decoders; they are also run under
    seed + 1000 ... 4000 (reading (a) only) for the seed check. seed_resp: the seed of
    fig6-marker-vs-embedding-decoding, for the response-epoch decoders (jaw, nose, all three
    markers; reading (a) only)."""
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
    out["auc"], out["auc_fold"] = {}, {}
    out["auc_resp"], out["auc_resp_fold"] = {}, {}
    out["outliers"] = {}
    out["n_resp_trials"] = {}
    enough = out["n_left"] >= 20 and out["n_right"] >= 20
    out["decoded"] = enough
    cleaned = {}
    for name in ("Jaw", "Nose"):
        xy, ts, _ = load_marker(f, name)
        if name == "Jaw":
            out["fp_jaw"] = _fingerprint(xy[:5000])
        xy, nbad = clean_marker(xy, ts)
        cleaned[name] = (xy, ts)
        out["outliers"][name] = (nbad, len(xy))
        X = marker_epoch(xy, ts, go, stride=STRIDE)
        ok = ~np.isnan(X).any(axis=(1, 2))
        out.setdefault("n_missing_frames", {})[name] = int((~ok).sum())
        if not enough or (y[ok].sum() < 20 or (1 - y[ok]).sum() < 20):
            continue
        Xo, yo = X[ok], y[ok]
        for off in SEED_OFFSETS:
            out["auc"][(name, "a", off)], out["auc_fold"][(name, "a", off)] = decode_auc_fast(Xo, yo, seed + off)
        out["auc"][(name, "b", 0)], out["auc_fold"][(name, "b", 0)] = decode_auc_fast(Xo[:, :, 4:6], yo, seed)
    if seed_resp is not None and enough:
        txy, tts2 = tongue_filled(f)
        feats = {}
        for name in ("Jaw", "Nose"):
            xy, ts = cleaned[name]
            feats[name] = marker_epoch(xy, ts, go, window=RESPONSE, stride=STRIDE)
        tX = marker_epoch(txy, tts2, go, window=RESPONSE, stride=STRIDE)
        feats["All"] = np.concatenate([feats["Jaw"], feats["Nose"], tX], axis=2)
        for name, X in feats.items():
            ok = ~np.isnan(X).any(axis=(1, 2))
            out["n_resp_trials"][name] = int(ok.sum())
            if y[ok].sum() < 20 or (1 - y[ok]).sum() < 20:
                continue
            out["auc_resp"][name], out["auc_resp_fold"][name] = decode_auc_fast(X[ok], y[ok], seed_resp)
    f.close()
    return out


def session_summary_retry(args, tries=3):
    """session_summary with retries on network errors (the archive is read over HTTP)."""
    import time
    asset, seed, seed_resp = args
    for i in range(tries):
        try:
            return session_summary(asset, seed, seed_resp)
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


def trial_video_timing(asset):
    """For one session: median frames per trial video, the median span of a trial video by its
    timestamps, the median trial duration (stop minus start) and the median time from the trial's
    start to its video's first frame. With the same trial durations, a video that holds half the
    frames over the same span of the trial was recorded at half the rate."""
    f = open_asset(asset["asset_id"])
    T = trials_table(f)
    _, ts, _ = load_marker(f, "Jaw")
    f.close()
    gaps = np.where(np.diff(ts) > 0.01)[0]
    st, en = np.r_[0, gaps + 1], np.r_[gaps, len(ts) - 1]
    k = np.clip(np.searchsorted(T["start"], ts[st], side="right") - 1, 0, len(T["start"]) - 1)
    return dict(path=asset["path"], trial_videos=len(st), frames_per_video=float(np.median(en - st + 1)),
                video_span_s=float(np.median(ts[en] - ts[st])),
                trial_duration_s=float(np.median((T["stop"] - T["start"])[k])),
                video_start_after_trial_start_s=float(np.median(ts[st] - T["start"][k])))


def later_video_series(path, version="0.231012.2129"):
    """The side-view ImageSeries of one file of the later version: how many, the frames of each
    (median), and the timing they carry (starting_time and its rate, timestamps if any)."""
    a = [x for x in list_assets(version) if x["path"].replace("+image", "") == path][0]
    r = requests.get(f"{API}/dandisets/{DANDISET}/versions/{version}/assets/{a['asset_id']}/").json()
    f = h5py.File(remfile.File([u for u in r["contentUrl"] if "s3" in u][0]), "r")
    side = [k for k in f["acquisition"] if "side_face" in k]
    g = f[f"acquisition/{side[0]}"]
    out = dict(path=a["path"], side_series=len(side),
               frames_per_series=float(np.median([f[f"acquisition/{k}/data"].shape[0] for k in side])),
               fields=sorted(g.keys()),
               rate=float(g["starting_time"].attrs["rate"]) if "starting_time" in g else None,
               has_timestamps="timestamps" in g)
    f.close()
    return out


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


def zenodo_listing():
    """Members of the authors' deposit zip, with their uncompressed sizes in bytes."""
    z = zipfile.ZipFile(remfile.File(ZENODO_ZIP))
    return [(i.filename, i.file_size) for i in z.infolist()]


DIVISIONS = {315: "Isocortex", 698: "Olfactory areas", 1089: "Hippocampal formation",
             703: "Cortical subplate", 477: "Striatum", 803: "Pallidum", 549: "Thalamus",
             1097: "Hypothalamus", 313: "Midbrain", 771: "Pons", 354: "Medulla", 512: "Cerebellum"}


def division_map():
    """CCF annotation name -> major division of the Allen CCF (DIVISIONS), or a label saying
    why it has none ('fiber tracts', 'ventricular systems', 'above division level', 'not in
    tree'). Ids and names from the deposit's mousebrainontology_2.csv, structure paths from its
    mousebrainontology_heirarchy_cortexMaskExclusions21_sc.xlsx (names there use '/' for ', ')."""
    import pandas as pd
    names = pd.read_csv(io.BytesIO(zenodo_member("mousebrainontology_2.csv")), header=None, names=["id", "name"])
    tree = pd.read_excel(io.BytesIO(zenodo_member("mousebrainontology_heirarchy_cortexMaskExclusions21_sc.xlsx")),
                         header=None, names=["id", "name", "path"])
    path_by_id = dict(zip(tree.id, tree.path))
    path_by_name = dict(zip(tree.name.str.replace("/", ", ", regex=False), tree.path))

    def division(path):
        ids = [int(x) for x in path.strip("/").split("/")]
        for i in ids:
            if i in DIVISIONS:
                return DIVISIONS[i]
        if 1009 in ids:
            return "fiber tracts"
        if 73 in ids:
            return "ventricular systems"
        return "above division level"

    def by_prefix(n):
        # a layer missing from the tree ("Frontal pole, layer 6a") takes the path of its area
        base = n.split(", layer")[0]
        hits = [q for k, q in path_by_name.items() if k == base or k.startswith(base + ", ")]
        return hits[0] if hits else None

    out = {}
    for i, n in zip(names.id, names.name):
        p = path_by_id.get(i, path_by_name.get(n)) or by_prefix(n)
        out[n] = division(p) if isinstance(p, str) else "not in tree"
    return out


def later_version_files(version="0.231012.2129"):
    """The later version's files: path, size, whether the path carries '+image' (the raw video),
    and the archive's variableMeasured for each."""
    rows = []
    for a in list_assets(version):
        r = requests.get(f"{API}/dandisets/{DANDISET}/versions/{version}/assets/{a['asset_id']}/").json()
        rows.append(dict(path=a["path"], size=a["size"], image="+image" in a["path"],
                         measured=sorted(v.get("value") for v in r.get("variableMeasured", []))))
    return rows


def acquisition_listing(path, version="0.231012.2129"):
    """Number of objects of each neurodata type in the acquisition group of one file."""
    a = [x for x in list_assets(version) if x["path"] == path][0]
    r = requests.get(f"{API}/dandisets/{DANDISET}/versions/{version}/assets/{a['asset_id']}/").json()
    f = h5py.File(remfile.File([u for u in r["contentUrl"] if "s3" in u][0]), "r")
    import collections
    types = []
    for k in f["acquisition"]:
        t = f[f"acquisition/{k}"].attrs.get("neurodata_type", "")
        types.append(t.decode() if isinstance(t, bytes) else str(t))
    f.close()
    return dict(collections.Counter(types))
