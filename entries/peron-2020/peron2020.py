"""Loading and measures for Peron et al. (2020), Nature 579:256, on CRCNS ssc-11.

The data set holds one tar.gz per mouse (ssc-11/live/data/an<id>.tar.gz) in the public
bucket crcnsarchive. A gzip stream cannot be read at an offset, so each archive is read
once, front to back, as an HTTP stream (``ResumableStream``, which reopens at the byte
offset reached when a connection drops) through ``tarfile`` in stream mode; nothing is
written to disk. Each member is held in memory only while it is reduced:

- ``*/session_neuropilone_*_merged/an*_vol_NN_sess_struct.mat``: one subvolume over the
  pre-ablation or post-ablation period. Kept per neuron: ROI id, centre of mass, encoding
  scores and shuffle scores, event rate, trial-averaged dF/F on correct left and right
  trials; per session file: trial type counts, whisker angle, touch onsets and touch
  properties, and a touch-triggered population dF/F used to check the clocks.
- small ``.mat`` files (under 5 MB, such as the curation files) are kept whole.
- JRC ablation logs (``ablation_logs/<date>/ablation_log_*.mat``): the id of the targeted
  neuron (``la.ablatedId``), as ablation_figure_energy.m reads it.
- NYU per-attempt logs (``session_*_target_<id>_attempt_*.mat``): only their names.

Where each parameter comes from:

- Directory and curation file of each mouse and ablation (``ABLATIONS``): get_data_path.m
  of github.com/peronlab/ablation at commit 74b7321, the code the claims file cites.
- Feature names, pixel size (600/512 um), plane spacing (15 um) and subvolume spacing
  (45 um): get_ablation_data.m, pull_struct.
- Shuffle rule (99th percentile of the shuffle scores in event-rate deciles, per
  subvolume): claims file opening comment; Methods, Neuronal classification;
  get_rejects_based_on_shuffle.m. MATLAB's ``quantile`` is reproduced (method "hazen"
  in numpy, the piecewise-linear rule MATLAB documents).
- Proximity exclusion: claims file opening comment (Methods cylinder |dz| < 30 um, lateral
  < 10 um; the code's signed dz < 30 um as a variant).
- Touch bursts merged at a 50 ms interval: claims file, behaviour-unchanged (from
  ablation_figure_beh.m). The code calls a toolbox method (getBurstTimes) that is not in the
  repository; here a touch whose onset follows the previous touch's offset by less than 50 ms
  joins its burst. This is an assumption about that method, stated in the notebook.
"""
from __future__ import annotations

import io
import re
import tarfile
import time
from concurrent.futures import ProcessPoolExecutor

import h5py
import numpy as np
import pandas as pd
import requests
import scipy.io as sio

BASE = "https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-11/live/data/"
CHECKSUMS = "https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-11/live/checksums.md5"
FILELIST = "https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-11/live/filelist.txt"
DATASET = "ssc-11"
VERSION = "unversioned"  # CRCNS data sets are not versioned; the MD5 sums pin the files
DOI = "10.6080/K0Z31WWG"

PRE = "session_neuropilone_preablate_merged"
POST = "session_neuropilone_postablate_merged"


def _p(t):
    return f"session_neuropilone_postablate_{t}_merged"


# (mouse, ablation type) -> (pre directory, post directory, curation files); get_data_path.m
ABLATIONS = {
    ("274424", "touch"): (PRE, POST, ["2019_04_07_ablation/manualCurationData.mat"]),
    ("272761", "touch"): (PRE, POST, ["2019_03_24_ablation/manualCurationData.mat"]),
    ("274577", "touch"): (PRE, POST, ["2019_04_04_ablation/manualCurationData.mat"]),
    ("275798", "silent"): (PRE, _p("silent"), ["2019_05_07_ablation/manualCurationData.mat"]),
    ("275798", "whisking"): (_p("silent"), _p("whisking"), ["2019_05_17_ablation/manualCurationData.mat"]),
    ("275801", "silent"): (PRE, _p("silent"), ["2019_05_21_ablation/manualCurationData.mat"]),
    ("275801", "touch"): (_p("whisking"), _p("touch"), ["2019_05_31_ablation/manualCurationData.mat"]),
    ("276013", "silent"): (PRE, _p("silent"), ["2019_06_11_ablation_silent/manualCurationData.mat"]),
    ("276013", "whisking"): (_p("silent"), _p("whisking"), ["2019_06_17_ablation_whisking/manualCurationData.mat"]),
    ("278288", "whisking"): (PRE, POST, ["2019_07_08_ablation_whisking/manualCurationData.mat"]),
    ("278759", "whisking"): (PRE, POST, ["2019_07_17_whisking_ablation/manualCurationData.mat"]),
    ("250220", "touch"): (PRE, POST, ["an250220_all.mat"]),
    ("257218", "silent"): (PRE, POST, ["an257218_2014_09_01.mat"]),
    ("257220", "touch"): (PRE, POST, ["an257220_2014_09_17.mat"]),
    ("258836", "silent"): (PRE, _p("silent"), ["an258836_2014_10_11.mat"]),
    ("258836", "touch"): (_p("silent"), _p("touch"), ["an258836_2014_10_14.mat", "an258836_2014_10_16.mat"]),
    ("271211", "silent"): (PRE, _p("silent"), ["an271211_2014_11_12.mat"]),
    ("271211", "touch"): (_p("silent"), _p("touch"), ["an271211_2014_11_16.mat"]),
    ("278937", "silent"): (PRE, _p("silent"), ["an278937_2015_01_30.mat"]),
    ("278937", "whisking"): (_p("silent"), _p("whisking"), ["an278937_2015_02_04.mat"]),
    ("278939", "silent"): (PRE, _p("silent"), ["an278939_2015_01_30.mat"]),
    ("278939", "whisking"): (_p("silent"), _p("whisking"), ["an278939_2015_02_04.mat"]),
    ("281915", "whisking"): (PRE, _p("whisking"), ["an281915_2015_02_23.mat"]),
    ("281915", "touch"): (_p("whisking"), _p("touch"), ["an281915_2015_03_02.mat"]),
}

# get_anims.m
ANIMS = {
    "touch": ["250220", "257220", "258836", "271211", "281915", "274424", "272761", "274577", "275801"],
    "whisking": ["278937", "278939", "281915", "275798", "278288", "276013", "278759"],
    "silent": ["257218", "258836", "271211", "278937", "278939", "275801", "275798", "276013"],
}
MICE = sorted({a for v in ANIMS.values() for a in v})
NYU = {"276013", "275801", "275798", "274577", "274424", "272761", "278288", "278759"}

WHISK_FEAT = "eventBasedDff_k16t14_MeanWhiskerAmplitudeGLMScore"
TOUCH_FEAT = "eventBasedDff_k16t14_{}AbsMaxKappaZeroNotouchGLMScore"
PIX2UM = 600 / 512


# ----------------------------------------------------------------------------------------
# streaming and reduction
# ----------------------------------------------------------------------------------------
def checksums():
    txt = requests.get(CHECKSUMS, timeout=60).text
    return {l.split()[1]: l.split()[0] for l in txt.splitlines() if l.strip()}


def _feat(cf, key):
    keys = list(np.atleast_1d(cf.keys))
    if key not in keys:
        return None
    return np.asarray(cf.values[keys.index(key)], dtype=float)


def _triggered(trace, ca_t, onsets, lags):
    """Mean of ``trace`` at frame lags around each onset (ms), frames found on ca_t."""
    idx = np.searchsorted(ca_t, onsets)
    ok = (idx + lags.min() >= 0) & (idx + lags.max() < len(trace))
    idx = idx[ok]
    if len(idx) == 0:
        return np.full(len(lags), np.nan), 0
    return np.nanmean(trace[idx[:, None] + lags[None, :]], axis=0), len(idx)


def reduce_sess(raw: bytes, wtag=None):
    s = sio.loadmat(io.BytesIO(raw), squeeze_me=True, struct_as_record=False)["sess"]
    c = s.caTSA
    cf = c.cellFeatures
    if wtag is None:
        wtag = str(np.atleast_1d(s.whiskerTag)[0])
    tf = TOUCH_FEAT.format(wtag.lower())
    out = {"mouse": str(s.mouseId), "whisker": str(np.atleast_1d(s.whiskerTag)[0]), "wtag_used": wtag}
    keys = list(np.atleast_1d(cf.keys))
    out["feature_keys"] = keys
    per = {
        "t": _feat(cf, tf), "t_sh": _feat(cf, tf.replace("GLMScore", "GLMShuffleScore")),
        "w": _feat(cf, WHISK_FEAT), "w_sh": _feat(cf, WHISK_FEAT.replace("GLMScore", "GLMShuffleScore")),
        "er": _feat(cf, "eventRateHz"),
    }
    ids, xs, ys, fov, plane = [], [], [], [], []
    for v, ra in enumerate(np.atleast_1d(c.roiArray)):
        rois = np.atleast_1d(ra.rois)
        rid = np.atleast_1d(ra.roiIds)
        for r in rois:
            ind = np.atleast_1d(r.indices).astype(float)
            if len(ind):
                # get_ablation_data.m, pull_struct
                x_ = np.ceil(ind / 512)
                y_ = ind - np.floor(ind / 512) * 512
                xs.append(x_.mean() * PIX2UM)
                ys.append(y_.mean() * PIX2UM)
            else:
                xs.append(np.nan)
                ys.append(np.nan)
        ids.extend(rid.tolist())
        plane.extend([v] * len(rid))
    out["roi_ids"] = np.array(ids, dtype=np.int64)
    out["x"] = np.array(xs)
    out["y"] = np.array(ys)
    out["plane"] = np.array(plane)
    out["ca_ids"] = np.atleast_1d(c.ids).astype(np.int64)
    out["per"] = per
    hl, hr = _feat(cf, "dffBased_HitLTrialAvg"), _feat(cf, "dffBased_HitRTrialAvg")
    out["hitL"] = None if hl is None else hl.astype(np.float32)
    out["hitR"] = None if hr is None else hr.astype(np.float32)
    # behaviour
    tm = np.atleast_2d(s.trialTypeMat)
    out["trial_type_str"] = [str(x) for x in np.atleast_1d(s.trialTypeStr)]
    out["trial_type_counts"] = tm.sum(axis=1)
    out["n_trials"] = tm.shape[1]
    out["trial_ids"] = np.atleast_1d(s.trialIds)
    th = np.asarray(s.whiskerAngleTSA.valueMatrix, dtype=float)
    out["theta"] = (th if th.ndim == 1 else th[0]).astype(np.float32)
    out["wh_dt_ms"] = float(np.median(np.diff(np.atleast_1d(s.whiskerAngleTSA.time)[:1000])))
    esa = s.whiskerBarContactESA.esa
    e0 = np.atleast_1d(esa)[0]
    et = np.atleast_1d(e0.eventTimes).astype(float)
    etr = np.atleast_1d(e0.eventTrials)
    h = e0.eventPropertiesHash
    hk = list(np.atleast_1d(h.keys))
    hv = {k: np.atleast_1d(h.values[i]).astype(float) for i, k in enumerate(hk)}
    out["touch_on"], out["touch_off"], out["touch_trial"] = et[0::2], et[1::2], etr[0::2]
    out["theta_at_touch"] = hv.get("thetaAtTouchOnset", np.array([]))[0::2]
    out["kappa_at_touch"] = hv.get("kappaMaxAbsOverTouch", np.array([]))[0::2]
    # for the check of the [0::2] rule: property keys and lengths against the event edges
    out["touch_prop_lens"] = {k: len(v) for k, v in hv.items()}
    out["n_touch_edges"] = len(et)
    # clock check: population dF/F of this file's touch-scored cells around the first touch
    # of each trial, and around the same number of pseudo-onsets 2 s earlier
    dff = np.asarray(c.dffTimeSeriesArray.valueMatrix, dtype=np.float32)
    ca_t = np.atleast_1d(c.time).astype(float)
    out["ca_dt_ms"] = float(np.median(np.diff(ca_t)))
    out["n_frames"] = len(ca_t)
    t = per["t"]
    sel = np.where(t > 0.1)[0] if t is not None else np.array([], int)
    if len(sel) == 0 and t is not None:
        sel = np.argsort(-np.nan_to_num(t, nan=-9))[:5]
    pop = np.nanmean(dff[sel], axis=0) if len(sel) else np.nanmean(dff, axis=0)
    first = pd.Series(out["touch_on"]).groupby(out["touch_trial"]).min().values if len(et) else np.array([])
    lags = np.arange(-7, 15)
    out["trig_lags"] = lags
    out["trig_real"], out["trig_n"] = _triggered(pop, ca_t, first, lags)
    out["trig_shift"], _ = _triggered(pop, ca_t, first - 2000.0, lags)
    out["trial_start_range"] = (float(np.min(s.trialStartTimes)), float(np.max(s.trialStartTimes)))
    out["ca_t_range"] = (float(ca_t.min()), float(ca_t.max()))
    out["touch_t_range"] = (float(et.min()), float(et.max())) if len(et) else (np.nan, np.nan)
    del s, c, dff
    return out


def _h5str(d):
    return "".join(map(chr, np.asarray(d).ravel()))


def reduce_sess_h5(raw: bytes, wtag=None):
    """As ``reduce_sess``, for MATLAB v7.3 (HDF5) files. HDF5 stores MATLAB arrays
    transposed, and cell arrays as references."""
    f = h5py.File(io.BytesIO(raw), "r")
    s = f["sess"]
    D = lambda r: f[r]  # noqa: E731
    c = s["caTSA"]
    whisker = _h5str(D(s["whiskerTag"][0, 0])[()]) if s["whiskerTag"].dtype == object else _h5str(s["whiskerTag"][()])
    if wtag is None:
        wtag = whisker
    tfeat = TOUCH_FEAT.format(wtag.lower())
    keys = [_h5str(D(k)[()]) for k in c["cellFeatures/keys"][:, 0]]

    def feat(key):
        if key not in keys:
            return None
        return np.asarray(D(c["cellFeatures/values"][keys.index(key), 0])[()], dtype=float).T

    def vec(key):
        v = feat(key)
        return None if v is None else v.ravel()

    out = {"mouse": _h5str(s["mouseId"][()]), "whisker": whisker, "wtag_used": wtag, "feature_keys": keys}
    per = {"t": vec(tfeat), "t_sh": vec(tfeat.replace("GLMScore", "GLMShuffleScore")),
           "w": vec(WHISK_FEAT), "w_sh": vec(WHISK_FEAT.replace("GLMScore", "GLMShuffleScore")),
           "er": vec("eventRateHz")}
    ids, xs, ys, plane = [], [], [], []
    for v, ref in enumerate(c["roiArray"][:, 0]):
        ra = D(ref)
        rid = np.asarray(ra["roiIds"][()]).ravel()
        for rr in ra["rois"][:, 0]:
            ind = np.asarray(D(rr)["indices"][()], dtype=float).ravel()
            if len(ind) and not (len(ind) == 2 and D(rr)["indices"].dtype == np.uint64):
                x_ = np.ceil(ind / 512)
                y_ = ind - np.floor(ind / 512) * 512
                xs.append(x_.mean() * PIX2UM)
                ys.append(y_.mean() * PIX2UM)
            else:
                xs.append(np.nan)
                ys.append(np.nan)
        ids.extend(rid.astype(np.int64).tolist())
        plane.extend([v] * len(rid))
    out["roi_ids"] = np.array(ids, dtype=np.int64)
    out["x"], out["y"], out["plane"] = np.array(xs), np.array(ys), np.array(plane)
    out["ca_ids"] = np.asarray(c["ids"][()]).ravel().astype(np.int64)
    out["per"] = per
    hl, hr = feat("dffBased_HitLTrialAvg"), feat("dffBased_HitRTrialAvg")
    out["hitL"] = None if hl is None else hl.astype(np.float32)
    out["hitR"] = None if hr is None else hr.astype(np.float32)
    tm = np.asarray(s["trialTypeMat"][()]).T
    out["trial_type_str"] = [_h5str(D(k)[()]) for k in s["trialTypeStr"][:, 0]]
    out["trial_type_counts"] = tm.sum(axis=1)
    out["n_trials"] = tm.shape[1]
    out["trial_ids"] = np.asarray(s["trialIds"][()]).ravel()
    out["theta"] = np.asarray(s["whiskerAngleTSA/valueMatrix"][()], dtype=np.float32)[:, 0]
    out["wh_dt_ms"] = float(np.median(np.diff(np.asarray(s["whiskerAngleTSA/time"][:1000]).ravel())))
    e0 = D(s["whiskerBarContactESA/esa"][0, 0])
    et = np.asarray(e0["eventTimes"][()], dtype=float).ravel()
    etr = np.asarray(e0["eventTrials"][()]).ravel()
    h = e0["eventPropertiesHash"]
    hk = [_h5str(D(k)[()]) for k in h["keys"][:, 0]]
    hv = {k: np.asarray(D(h["values"][i, 0])[()], dtype=float).ravel() for i, k in enumerate(hk)}
    out["touch_on"], out["touch_off"], out["touch_trial"] = et[0::2], et[1::2], etr[0::2]
    out["theta_at_touch"] = hv.get("thetaAtTouchOnset", np.array([]))[0::2]
    out["kappa_at_touch"] = hv.get("kappaMaxAbsOverTouch", np.array([]))[0::2]
    # for the check of the [0::2] rule: property keys and lengths against the event edges
    out["touch_prop_lens"] = {k: len(v) for k, v in hv.items()}
    out["n_touch_edges"] = len(et)
    ca_t = np.asarray(c["time"][()], dtype=float).ravel()
    out["ca_dt_ms"] = float(np.median(np.diff(ca_t)))
    out["n_frames"] = len(ca_t)
    t = per["t"]
    sel = np.where(t > 0.1)[0] if t is not None else np.array([], int)
    if len(sel) == 0 and t is not None:
        sel = np.sort(np.argsort(-np.nan_to_num(t, nan=-9))[:5])
    dset = c["dffTimeSeriesArray/valueMatrix"]  # frames x cells
    pop = np.nanmean(dset[:, sel], axis=1) if len(sel) else np.nanmean(dset[()], axis=1)
    first = pd.Series(out["touch_on"]).groupby(out["touch_trial"]).min().values if len(et) else np.array([])
    lags = np.arange(-7, 15)
    out["trig_lags"] = lags
    out["trig_real"], out["trig_n"] = _triggered(pop, ca_t, first, lags)
    out["trig_shift"], _ = _triggered(pop, ca_t, first - 2000.0, lags)
    out["trial_start_range"] = (float(np.min(s["trialStartTimes"][()])), float(np.max(s["trialStartTimes"][()])))
    out["ca_t_range"] = (float(ca_t.min()), float(ca_t.max()))
    out["touch_t_range"] = (float(et.min()), float(et.max())) if len(et) else (np.nan, np.nan)
    f.close()
    return out


def _simplify(v):
    if isinstance(v, np.ndarray):
        return v
    if hasattr(v, "_fieldnames"):
        return {k: _simplify(getattr(v, k)) for k in v._fieldnames}
    return v


class ResumableStream(io.RawIOBase):
    """Sequential HTTP read of one object that reopens at the current byte offset (an HTTP
    Range request) when the connection drops, so a long gzip stream can be read through
    to the end. Nothing is written to disk."""

    def __init__(self, url, retries=20):
        self.url, self.pos, self.retries, self.reopens = url, 0, retries, 0
        self._open()

    def _open(self):
        hdr = {"Range": f"bytes={self.pos}-"} if self.pos else {}
        self.r = requests.get(self.url, headers=hdr, stream=True, timeout=(30, 120))
        self.r.raise_for_status()

    def readable(self):
        return True

    def readinto(self, b):
        for attempt in range(self.retries):
            try:
                data = self.r.raw.read(len(b))
                n = len(data)
                b[:n] = data
                self.pos += n
                return n
            except Exception:  # noqa: BLE001
                self.reopens += 1
                time.sleep(2 * (attempt + 1))
                try:
                    self.r.close()
                    self._open()
                except Exception:  # noqa: BLE001
                    pass
        raise IOError(f"could not resume {self.url} at byte {self.pos}")


def stream_mouse(anim: str, small_max=5_000_000):
    """Read one mouse's archive from front to back and reduce what the claims use."""
    t0 = time.time()
    url = BASE + f"an{anim}.tar.gz"
    res = {"anim": anim, "members": [], "sess": {}, "small": {}, "jrc_logs": {}, "nyu_attempts": [],
           "errors": []}
    wtags = {}
    raw_stream = ResumableStream(url)
    with io.BufferedReader(raw_stream, buffer_size=2**22) as f:
        tf = tarfile.open(fileobj=f, mode="r|gz")
        for m in tf:
            res["members"].append((m.name, m.size))
            if not m.isfile():
                continue
            rel = m.name.split("/", 1)[1]
            try:
                if rel.endswith("sess_struct.mat"):
                    d, fn = rel.rsplit("/", 1)
                    raw = tf.extractfile(m).read()
                    # pull_struct takes the whisker tag of the first file of the directory
                    if raw[:128].find(b"MATLAB 7.3") >= 0:
                        r = reduce_sess_h5(raw, wtags.get(d))
                        r["format"] = "v7.3"
                    else:
                        r = reduce_sess(raw, wtags.get(d))
                        r["format"] = "v5"
                    wtags.setdefault(d, r["whisker"])
                    del raw
                    res["sess"].setdefault(d, {})[fn] = r
                elif re.search(r"ablation_logs/.*/ablation_log_.*\.mat$", rel):
                    raw = tf.extractfile(m).read()
                    la = sio.loadmat(io.BytesIO(raw), squeeze_me=True, struct_as_record=False,
                                     variable_names=["la"])
                    del raw
                    aid = None
                    if "la" in la and hasattr(la["la"], "ablatedId"):
                        aid = int(np.atleast_1d(la["la"].ablatedId)[0])
                    res["jrc_logs"][rel] = aid
                elif "_attempt_" in rel:
                    res["nyu_attempts"].append(rel)
                elif rel.endswith(".mat") and m.size < small_max:
                    raw = tf.extractfile(m).read()
                    try:
                        d = sio.loadmat(io.BytesIO(raw), squeeze_me=True, struct_as_record=False)
                        res["small"][rel] = {k: _simplify(v) for k, v in d.items() if not k.startswith("__")}
                    except Exception as e:  # noqa: BLE001
                        res["errors"].append((rel, repr(e)))
            except Exception as e:  # noqa: BLE001
                res["errors"].append((rel, repr(e)))
    res["seconds"] = time.time() - t0
    res["bytes"] = raw_stream.pos
    res["reopens"] = raw_stream.reopens
    return res


def _safe_stream(anim):
    try:
        return stream_mouse(anim)
    except Exception as e:  # noqa: BLE001
        return {"anim": anim, "failed": repr(e), "sess": {}, "small": {}, "jrc_logs": {},
                "nyu_attempts": [], "members": [], "errors": [("stream", repr(e))]}


def load_all(mice=None, workers=5):
    """Stream every mouse, largest archives first, ``workers`` at a time."""
    mice = list(mice or MICE)
    txt = requests.get(FILELIST, timeout=60).text
    sizes = {m.group(1): int(m.group(2)) for m in re.finditer(r"an(\d+)\.tar\.gz\s+(\d+)", txt)}
    mice.sort(key=lambda a: -sizes.get(a, 0))
    with ProcessPoolExecutor(workers) as ex:
        out = dict(zip(mice, ex.map(_safe_stream, mice)))
    return out, sizes


# ----------------------------------------------------------------------------------------
# per-neuron table, as get_ablation_data.m
# ----------------------------------------------------------------------------------------
def matlab_quantile(x, q):
    x = np.asarray(x, float)
    x = x[~np.isnan(x)]
    if len(x) == 0:
        return np.full(np.shape(q), np.nan)
    return np.quantile(x, q, method="hazen")


def rejects_by_shuffle(score, sh, er, subi, thresh=0.99):
    """get_rejects_based_on_shuffle.m: indices in ``subi`` below the 99th percentile of the
    shuffle scores of their event-rate decile."""
    cut = matlab_quantile(er[subi], np.arange(0, 1.01, 0.1))
    cut[-1] += 1e-4
    bad = []
    for e in range(len(cut) - 1):
        b = subi[(er[subi] >= cut[e]) & (er[subi] < cut[e + 1])]
        if len(b) == 0:
            continue
        th = matlab_quantile(sh[b], thresh)
        bad.extend(b[score[b] < th].tolist())
    return np.array(bad, dtype=int)


def pull_dir(sess_dir: dict):
    """Concatenate the subvolume files of one directory, as pull_struct (files sorted by name)."""
    rows = []
    for f, fn in enumerate(sorted(sess_dir)):
        r = sess_dir[fn]
        n = len(r["ca_ids"])
        # roiArray ids and caTSA ids are in the same order in pull_struct; checked in the notebook
        z = f * 45 + r["plane"] * 15
        df = pd.DataFrame({
            "cell_id": r["roi_ids"], "subvol": f + 1, "x": r["x"], "y": r["y"], "z": z,
            "t": r["per"]["t"], "t_sh": r["per"]["t_sh"], "w": r["per"]["w"], "w_sh": r["per"]["w_sh"],
            "er": r["per"]["er"],
        })
        assert len(df) == n
        rows.append(df)
    return pd.concat(rows, ignore_index=True)


def trial_avgs(sess_dir: dict, ids):
    """Concatenated correct-left and correct-right trial-averaged dF/F (70 + 70 frames) and
    the code's version (right-trial average only), ordered as ``ids``."""
    cid, both, ronly = [], [], []
    for fn in sorted(sess_dir):
        r = sess_dir[fn]
        cid.append(r["ca_ids"])
        hl = r["hitL"] if r["hitL"] is not None else np.full((70, len(r["ca_ids"])), np.nan)
        hr = r["hitR"] if r["hitR"] is not None else np.full((70, len(r["ca_ids"])), np.nan)
        both.append(np.vstack([hl[:70], hr[:70]]))
        ronly.append(np.vstack([hr[:70], np.full_like(hr[:70], np.nan)]))
    cid = np.concatenate(cid)
    pos = pd.Series(np.arange(len(cid)), index=cid)
    idx = pos.loc[ids].values
    return np.hstack(both)[:, idx], np.hstack(ronly)[:, idx]


def ablated_ids(small: dict, files):
    """get_ablated_ids: successful targets of the curation file(s)."""
    out = []
    for fn in files:
        d = small[fn]
        if "ablationSuccessful" in d:
            out.extend(np.unique(np.atleast_1d(d["ablationTargetIds"])[np.atleast_1d(d["ablationSuccessful"]).astype(bool)]).tolist())
        elif "ablated_ids" in d:
            out.extend(np.unique(np.atleast_1d(d["ablated_ids"])).tolist())
    return np.array(out, dtype=np.int64)


def ablation_table(mouse_data: dict, anim: str, abl: str, cyl="methods"):
    """Per-neuron table of one ablation, as get_ablation_data.m.

    ``cyl``: 'methods' excludes neurons within lateral 10 um and |dz| < 30 um of an ablated
    neuron (Methods, Multiphoton ablation); 'code' uses the signed dz < 30 um of the code.
    """
    pre_d, post_d, cur = ABLATIONS[(anim, abl)]
    pre = pull_dir(mouse_data["sess"][pre_d])
    post = pull_dir(mouse_data["sess"][post_d])
    info = {"n_pre_raw": len(pre), "n_post_raw": len(post)}
    pre = pre.sort_values("cell_id", kind="stable").reset_index(drop=True)
    post = post.set_index("cell_id")
    common = pre["cell_id"].isin(post.index)
    info["n_dropped_unmatched"] = int((~common).sum())
    pre = pre[common].reset_index(drop=True)
    post = post.loc[pre["cell_id"]].reset_index()
    d = pre.rename(columns={"t": "t_pre", "t_sh": "t_pre_sh", "w": "w_pre", "w_sh": "w_pre_sh", "er": "er_pre"})
    for k in ["t", "t_sh", "w", "w_sh", "er"]:
        d[k.replace("_sh", "") + ("_post_sh" if k.endswith("_sh") else "_post")] = post[k].values
    for col in ["t_pre", "t_post", "w_pre", "w_post"]:
        d[col + "_bad"] = 0
    for sv in d["subvol"].unique():
        subi = np.where(d["subvol"].values == sv)[0]
        for sc, er in [("t_pre", "er_pre"), ("t_post", "er_post"), ("w_pre", "er_pre"), ("w_post", "er_post")]:
            sh = sc.replace("_pre", "_pre_sh").replace("_post", "_post_sh")
            bad = rejects_by_shuffle(d[sc].values, d[sh].values, d[er].values, subi)
            d.loc[bad, sc + "_bad"] = 1
    abl_ids = ablated_ids(mouse_data["small"], cur)
    info["n_ablated_ids"] = len(abl_ids)
    d["is_ablated"] = d["cell_id"].isin(abl_ids).astype(int)
    info["n_ablated_found"] = int(d["is_ablated"].sum())
    x, y, z = d["x"].values, d["y"].values, d["z"].values
    dmin = np.full(len(d), np.inf)
    prox_m = np.zeros(len(d), bool)
    prox_c = np.zeros(len(d), bool)
    for a in np.where(d["is_ablated"].values == 1)[0]:
        dmin = np.minimum(dmin, np.sqrt((x - x[a]) ** 2 + (y - y[a]) ** 2 + (z - z[a]) ** 2))
        drad = np.sqrt((x - x[a]) ** 2 + (y - y[a]) ** 2)
        dz = z - z[a]
        prox_m |= (drad < 10) & (np.abs(dz) < 30)
        prox_c |= (drad < 10) & (dz < 30)
    d["d_ablated_um"] = dmin
    d["prox_methods"] = prox_m.astype(int)
    d["prox_code"] = prox_c.astype(int)
    d["proximity_exclude"] = d["prox_methods"] if cyl == "methods" else d["prox_code"]
    return d, info


def _valid_one(d, r, thresh):
    pre, post = d[f"{r}_pre"].values, d[f"{r}_post"].values
    v = ((pre > thresh) & (d[f"{r}_pre_bad"].values == 0)) | ((post > thresh) & (d[f"{r}_post_bad"].values == 0))
    v &= ~(np.isnan(pre) | np.isnan(post))
    v &= d["proximity_exclude"].values == 0
    v &= d["is_ablated"].values == 0
    return v


def members(d, r, thresh=0.1):
    """get_restricted_neurons.m: boolean mask of the neurons of representation ``r`` ('t' or
    'w'), neurons of both representations left out."""
    vt, vw = _valid_one(d, "t", thresh), _valid_one(d, "w", thresh)
    both = vt & vw
    return (vt & ~both) if r == "t" else (vw & ~both)


def class_counts(d, r, rule, thresh=0.1, keep_ablated=True):
    """Count of representation members in the pre and post periods separately.

    rule 'a': score above 0.1 alone (ablation_summ_stats.m); rule 'b': Methods membership
    (score above 0.1 and not rejected by the shuffle test, neurons in both representations,
    ablated and cylinder-excluded neurons left out) in each period.
    """
    out = []
    for per in ["pre", "post"]:
        s = d[f"{r}_{per}"].values
        if rule == "a":
            m = s > thresh
            if not keep_ablated:
                m &= d["is_ablated"].values == 0
        else:
            def one(rr):
                return (d[f"{rr}_{per}"].values > thresh) & (d[f"{rr}_{per}_bad"].values == 0)
            m = one(r) & ~(one("t") & one("w"))
            m &= (d["is_ablated"].values == 0) & (d["proximity_exclude"].values == 0)
        out.append(int(m.sum()))
    return out


def bursts(on, off, trial, gap_ms=50.0):
    """Number of touch bursts: a touch starting less than ``gap_ms`` after the previous touch
    of the same trial ended joins its burst (assumption about getBurstTimes)."""
    if len(on) == 0:
        return 0
    o = np.argsort(on, kind="stable")
    on, off, trial = on[o], off[o], trial[o]
    new = np.ones(len(on), bool)
    new[1:] = ~((trial[1:] == trial[:-1]) & (on[1:] - off[:-1] < gap_ms))
    return int(new.sum())


def adj_mad(x):
    x = np.asarray(x, float)
    x = x[~np.isnan(x)]
    return 1.4826 * np.median(np.abs(x - np.median(x)))


# ----------------------------------------------------------------------------------------
# measures used by several claims
# ----------------------------------------------------------------------------------------
def with_cyl(d, cyl):
    """Copy of an ablation table using the Methods ('methods') or the code's ('code') cylinder."""
    d = d.copy()
    d["proximity_exclude"] = d["prox_" + cyl]
    return d


def mouse_medians(d, r, thresh=0.1):
    """Median pre and post score of the members of representation ``r``, and their number
    (ablation_figure_score_change.m, single_type_basic)."""
    m = members(d, r, thresh)
    return float(np.nanmedian(d[f"{r}_pre"][m])), float(np.nanmedian(d[f"{r}_post"][m])), int(m.sum())


def nancorr(a, b):
    ok = ~(np.isnan(a) | np.isnan(b))
    if ok.sum() < 3:
        return np.nan
    return float(np.corrcoef(a[ok], b[ok])[0, 1])


def sign_test(x):
    """Two-sided sign test of values against 0 (MATLAB signtest drops zeros)."""
    from scipy import stats
    x = np.asarray(x, float)
    x = x[~np.isnan(x) & (x != 0)]
    return float(stats.binomtest(int((x > 0).sum()), len(x)).pvalue)


def similarity(mouse_data, d, anim, abl, trial_avg="both"):
    """Response similarity of each neuron of ``d`` to the mean pre-ablation trial-averaged
    dF/F of the ablated neurons (Methods, Response similarity). ``trial_avg`` 'both' is the
    correct-left and correct-right averages concatenated (Methods); 'right' is what the code
    ends up correlating (ablation_figure_correlation.m writes both averages into the same 70
    rows, so the right-trial average alone remains)."""
    pre_d = ABLATIONS[(anim, abl)][0]
    both, ronly = trial_avgs(mouse_data["sess"][pre_d], d["cell_id"].values)
    M = both if trial_avg == "both" else ronly
    ab = np.nanmean(M[:, d["is_ablated"].values == 1], axis=1)
    return np.array([nancorr(ab, M[:, i]) for i in range(M.shape[1])])


def similarity_slopes(x, y, bins=np.arange(-1, 1.0001, 0.1), min_n=3):
    """Slope of a line fitted to the neurons' points, the bin means (0.1-wide bins, bins with
    more than ``min_n`` neurons, as the code) and the slope fitted to those bin means."""
    ok = ~(np.isnan(x) | np.isnan(y))
    x, y = x[ok], y[ok]
    s_pts = float(np.polyfit(x, y, 1)[0]) if len(x) > 2 else np.nan
    bm = np.full(len(bins) - 1, np.nan)
    n_in = 0
    for b in range(len(bins) - 1):
        s = (x > bins[b]) & (x <= bins[b + 1])
        if s.sum() > min_n:
            bm[b] = y[s].mean()
            n_in += int(s.sum())
    xc = bins[:-1] + 0.05
    okb = ~np.isnan(bm)
    s_bin = float(np.polyfit(xc[okb], bm[okb], 1)[0]) if okb.sum() > 1 else np.nan
    return s_pts, s_bin, bm, len(x), n_in


def behaviour(mouse_data, anim, abl):
    """Per period: fraction correct (hits over hits and errors), touch bursts per trial,
    whisker angle samples, angle at touch onset and curvature change at touch, summed over
    the subvolume files of the period (ablation_figure_beh.m, pull_session_objects)."""
    pre_d, post_d, _ = ABLATIONS[(anim, abl)]
    out = {}
    for per, dd in [("pre", pre_d), ("post", post_d)]:
        S = mouse_data["sess"][dd]
        tc = np.zeros(4)
        nb = 0
        th, tat, kat = [], [], []
        for fn in sorted(S):
            r = S[fn]
            tc += np.asarray(r["trial_type_counts"][:4], float)
            nb += bursts(r["touch_on"], r["touch_off"], r["touch_trial"])
            th.append(r["theta"])
            tat.append(r["theta_at_touch"])
            kat.append(r["kappa_at_touch"])
        out[per] = {"frac_correct": tc[:2].sum() / tc.sum(), "touches_per_trial": nb / tc.sum(),
                    "n_trials": int(tc.sum()), "theta": np.concatenate(th),
                    "theta_at_touch": np.concatenate(tat), "kappa_at_touch": np.concatenate(kat)}
    return out


def targets_and_successes(mouse_data, anim, abl):
    """Targeted and successfully ablated neurons of one ablation. NYU curation files list
    each attempt (ablationTargetIds) and whether it succeeded; JRC curation files list
    attempted_ids and ablated_ids. The JRC logs' ablatedId (as ablation_figure_energy.m
    reads them) are returned too."""
    cur = ABLATIONS[(anim, abl)][2]
    tg, sc = set(), set()
    for c in cur:
        d = mouse_data["small"][c]
        if "ablationSuccessful" in d:
            ids = np.atleast_1d(d["ablationTargetIds"])
            ok = np.atleast_1d(d["ablationSuccessful"]).astype(bool)
            tg |= set(ids.tolist())
            sc |= set(ids[ok].tolist())
        else:
            tg |= set(np.atleast_1d(d.get("attempted_ids", [])).tolist())
            sc |= set(np.atleast_1d(d["ablated_ids"]).tolist())
    logs = set()
    for c in cur:
        m = re.match(r"an\d+_(.*)\.mat$", c)
        if m:
            for k, v in mouse_data["jrc_logs"].items():
                if k.startswith(f"ablation_logs/{m.group(1)}/") and v is not None:
                    logs.add(v)
    return tg, sc, logs
