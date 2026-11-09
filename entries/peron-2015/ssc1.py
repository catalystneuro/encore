"""Loading and measures for CRCNS ssc-1 (Peron, Freeman, Iyer, Guo & Svoboda 2015).

The data set holds one MATLAB v5 structure ``s`` per session
(``<animal>_<date>/<animal>_<date>_session.mat``), described in the data set's
docs/crcns_ssc-1_data_description.pdf (version 0.8). Files are streamed from the
public S3 bucket ``crcnsarchive`` (docs/archives.md, "CRCNS"); nothing is
written to disk. Each file is read whole into memory (100 to 200 MB) and
reduced at once to the arrays the analysis uses.

Parameters and where they come from:

- Trial epochs. The pole-in-reach interval of each trial is the data set's
  ``poleInReach`` event series (start and end), and the reward cue its
  ``rewardCue`` series. The sample epoch is the pole-in-reach interval, as the
  paper defines it ("a 1 s sample epoch (pole in reach)", claims file opening
  comment; "remained in place for the 1 s sample epoch", Supplemental Experimental
  Procedures, Behavioral training; data description, "Imaging and behavior"). The
  Figure 1C legend gives the sample epoch as "1 to 2 s"; the data's pole-in-reach
  intervals (0.84 to 1.18 s in the median) are used as they are, so the difference
  does not enter any result.
- Whisking amplitude (claim results-whisking-amplitude). Reading (c) uses the
  Hilbert amplitude of whisking, as the Supplemental Experimental Procedures
  use for bout onset ("the amplitude of whisking, obtained using the Hilbert
  transform (as described previously; see (Huber et al., 2012))"). The band
  for the whisking signal is not given in the paper; 6 to 30 Hz, a
  second-order Butterworth band-pass applied forward and backward, is an
  assumption taken from the field's practice for mouse whisking (about 10 Hz
  whisking; the 6 to 30 Hz band is common in Svoboda-lab whisker analyses).
  The amplitude is half the peak-to-trough excursion, so a peak Hilbert
  amplitude of A corresponds to a full sweep of about 2A; both are printed.
- Gaps in the whisker angle (NaN, 0.003% of samples in the first file read)
  are filled by linear interpolation before filtering, a standard choice that
  cannot change a per-trial range.
"""

from __future__ import annotations

import io

import fsspec
import numpy as np
import scipy.io as sio
from scipy.ndimage import median_filter
from scipy.signal import butter, filtfilt, hilbert

DATASET = "ssc-1"
# CRCNS data sets are not versioned (docs/archives.md); the pinned version is "unversioned",
# and the MD5 sums below detect a later change.
VERSION = "unversioned"
BUCKET = "https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-1/"

# The five session files of the data set, as listed by the bucket and by its
# filelist.txt; the misspelt "sesssion" is the file's real name.
SESSIONS = {
    "an197522_2013_03_08": "an197522_2013_03_08/an197522_2013_03_08_session.mat",
    "an197522_2013_03_10": "an197522_2013_03_10/an197522_2013_03_10_session.mat",
    "an229717_2013_12_01": "an229717_2013_12_01/an229717_2013_12_01_sesssion.mat",
    "an229719_2013_12_02": "an229719_2013_12_02/an229719_2013_12_02_session.mat",
    "an229719_2013_12_05": "an229719_2013_12_05/an229719_2013_12_05_session.mat",
}

# MD5 sums from the data set's checksums.md5, for the files read.
MD5 = {
    "an197522_2013_03_08": "1d4bd20b7bd82a3bb41b0655d45998c0",
    "an197522_2013_03_10": "f0dfe39427828d0b1f77f0bed35412d6",
    "an229717_2013_12_01": "36048ccc26b241ef7c35734d35eae61a",
    "an229719_2013_12_02": "52091811e35b8fe11a6efac6d23f4ac7",
    "an229719_2013_12_05": "f9ceda31c2a7446541bb10b6f8a5d355",
}


def list_bucket(prefix: str = "ssc-1/") -> list[tuple[str, int]]:
    """List every key under the prefix with its size in bytes."""
    import re
    import urllib.request

    keys, token = [], None
    while True:
        url = f"https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix={prefix}"
        if token:
            from urllib.parse import quote

            url += "&continuation-token=" + quote(token)
        text = urllib.request.urlopen(url).read().decode()
        keys += [(k, int(z)) for k, z in re.findall(r"<Key>(.*?)</Key>.*?<Size>(\d+)</Size>", text)]
        m = re.search(r"<NextContinuationToken>(.*?)</NextContinuationToken>", text)
        if not m:
            return keys
        token = m.group(1)


def _read_struct(name: str):
    url = BUCKET + SESSIONS[name]
    with fsspec.open(url, block_size=2**22) as f:
        raw = f.read()
    import hashlib

    md5 = hashlib.md5(raw).hexdigest()
    s = sio.loadmat(io.BytesIO(raw), squeeze_me=True, struct_as_record=False)["s"]
    return s, md5


def _list(x):
    """A MATLAB cell or scalar as a Python list."""
    if isinstance(x, np.ndarray) and x.dtype == object:
        return list(x.ravel())
    if isinstance(x, np.ndarray):
        return list(x.ravel()) if x.ndim else [x.item()]
    return [x]


def _events(s, key):
    """Event times (ms) and trial ids for one event series; type 2 has start/end pairs."""
    names = _list(s.eventSeriesArrayHash.keyNames)
    v = s.eventSeriesArrayHash.value[names.index(key)]
    return v


def load_session(name: str) -> dict:
    """Load one session and reduce it to plain arrays.

    Returns a dict with:
      meta: metaDataHash as a dict; md5 of the file read.
      trials: dict of arrays per trial (id, start, type label, pole position,
        pole-in and pole-out time, first reward cue time), times in ms.
      whisker: dict with time (ms), trial, angle (deg), kappa (curvature
        change), and the whisker's name from idStrs.
      touches: protraction and retraction touch start/end times (ms) and trials.
      licks: left and right lick times (ms).
      subvolumes: list of dicts, one per dffTSA, with ids, plane of each id,
        time (ms), trial per frame, dff (float32, n x t), valid trials,
        ROI pixel centroids per id (row, col in the 512 x 512 master image).
    """
    s, md5 = _read_struct(name)
    out = {"name": name, "md5": md5}
    out["meta"] = dict(zip(_list(s.metaDataHash.keyNames), _list(s.metaDataHash.value)))
    out["time_units"] = dict(zip(_list(s.timeUnitIds), _list(s.timeUnitNames)))
    out["trial_time_unit"] = int(s.trialTimeUnit)

    ids = np.asarray(s.trialIds).astype(int)
    tmat = np.asarray(s.trialTypeMat)
    tstr = _list(s.trialTypeStr)
    label = np.array(["none"] * len(ids), dtype=object)
    n_labels = tmat[: len(tstr)].sum(0)
    for i, t in enumerate(tstr):
        label[tmat[i] == 1] = t
    props = dict(zip(_list(s.trialPropertiesHash.keyNames), _list(s.trialPropertiesHash.value)))

    pole = _events(s, "poleInReach")
    pt, ptr = np.asarray(pole.eventTimes, float), np.asarray(pole.eventTrials).astype(int)
    pole_in = {tr: t for t, tr in zip(pt[0::2], ptr[0::2])}
    pole_out = {tr: t for t, tr in zip(pt[1::2], ptr[1::2])}
    cue = _events(s, "rewardCue")
    ct, ctr = np.asarray(cue.eventTimes, float), np.asarray(cue.eventTrials).astype(int)
    # rewardCue is type 2 (start and end); the cue onset is the first start in the trial.
    cue_on = {}
    for t, tr in zip(ct[0::2], ctr[0::2]):
        cue_on.setdefault(tr, t)
    out["trials"] = {
        "id": ids,
        "start": np.asarray(s.trialStartTimes, float),
        "label": label,
        "n_labels": n_labels,
        "pole_position": np.asarray(props.get("StimulusPosition"), float),
        "pole_in": np.array([pole_in.get(i, np.nan) for i in ids]),
        "pole_out": np.array([pole_out.get(i, np.nan) for i in ids]),
        "cue": np.array([cue_on.get(i, np.nan) for i in ids]),
    }
    out["event_types"] = {"poleInReach": int(pole.type), "rewardCue": int(np.ravel(cue.type)[0])}

    keys = _list(s.timeSeriesArrayHash.keyNames)
    w = s.timeSeriesArrayHash.value[keys.index("whiskerVars")]
    wid = _list(w.idStrs)
    out["whisker"] = {
        "time": np.asarray(w.time, float),
        "trial": np.asarray(w.trial).astype(int),
        "angle": np.asarray(w.valueMatrix[0], float),
        "kappa": np.asarray(w.valueMatrix[1], float),
        "names": wid,
        "time_unit": int(w.timeUnit),
    }
    dh = _list(s.timeSeriesArrayHash.descrHash)
    out["valid_whisker_trials"] = np.asarray(dh[0].value).astype(int)

    tch = _events(s, "touches")
    out["touches"] = {}
    for nm, et, etr in zip(_list(tch.idStr), _list(tch.eventTimes), _list(tch.eventTrials)):
        et, etr = np.asarray(et, float), np.asarray(etr).astype(int)
        out["touches"][nm] = {"start": et[0::2], "end": et[1::2], "trial": etr[0::2]}
    out["licks"] = {
        "left": np.asarray(_events(s, "leftLicks").eventTimes, float),
        "right": np.asarray(_events(s, "rightLicks").eventTimes, float),
    }
    out["event_series"] = _list(s.eventSeriesArrayHash.keyNames)
    out["timeseries_keys"] = keys

    subs = []
    for k, key in enumerate(keys):
        if not key.startswith("dffTSA"):
            continue
        v = s.timeSeriesArrayHash.value[k]
        d = dh[k]
        roi_defs = _list(d.value[0])
        plane_of, centroid, npix = {}, {}, {}
        for p, rd in enumerate(roi_defs):
            for r in _list(rd.rois):
                idx = np.asarray(r.indicesWithinImage).astype(int).ravel() - 1  # MATLAB 1-based
                # MATLAB column-major linear index into a 512 x 512 image
                row, col = idx % 512, idx // 512
                plane_of[int(r.id)] = p
                centroid[int(r.id)] = (row.mean(), col.mean()) if idx.size else (np.nan, np.nan)
                npix[int(r.id)] = idx.size
        rid = np.asarray(v.ids).astype(int)
        subs.append({
            "key": key,
            "descr": _list(s.timeSeriesArrayHash.descr)[k],
            "ids": rid,
            "plane": np.array([plane_of.get(i, -1) for i in rid]),
            "n_planes": len(roi_defs),
            "centroid": np.array([centroid.get(i, (np.nan, np.nan)) for i in rid]),
            "npix": np.array([npix.get(i, 0) for i in rid]),
            "time": np.asarray(v.time, float),
            "trial": np.asarray(v.trial).astype(int),
            "dff": np.asarray(v.valueMatrix, np.float32),
            "valid_trials": np.asarray(d.value[1]).astype(int),
            "source_files": [str(x) for x in _list(v.imagingPlane[0].sourceFileList)][:3],
            "fields": list(v._fieldnames),
            "time_unit": int(v.timeUnit),
            "id_strs": [str(x) for x in _list(v.idStrs)],
            "id_strs_detailed": [str(x) for x in _list(v.idStrsDetailed)],
            "descr_keys": [str(x) for x in _list(d.keyNames)],
            "roi_array_fields": list(roi_defs[0]._fieldnames) if roi_defs else [],
            "roi_fields": list(_list(roi_defs[0].rois)[0]._fieldnames) if roi_defs else [],
            "plane_fields": list(_list(v.imagingPlane)[0]._fieldnames),
        })
    out["subvolumes"] = subs
    return out


ARTEFACT_LIMIT = 85.0   # degrees; |angle| above this is near the +/-90 degree limit of the tracker
SPIKE_DEV = 20.0        # degrees from the 5-sample running median; a one- or two-sample jump
EDGE_S = 0.2            # seconds left out at each end of a trial for the edge-trimmed Hilbert peak


def artefact_masks(ang: np.ndarray) -> dict:
    """Samples of the whisker angle that look like tracking errors, two ways.

    ``limit``: |angle| > ARTEFACT_LIMIT (85 degrees). The angle is reported within +/-90 degrees,
    and isolated samples jump to the limits (for example 87.3, 37.8, -89.2, 41.7 degrees on
    successive 2 ms samples), which no whisker movement does. This mask also takes the tops of smooth
    excursions that reach 85 to 88 degrees, which may be real.
    ``spike``: samples more than SPIKE_DEV (20 degrees) from the median of the 5 samples around
    them, i.e. jumps that last one or two samples (4 ms) and return; this keeps smooth excursions.
    ``dev`` is that distance for every sample. ``ang`` must have no NaN (gaps filled first).
    Neither threshold comes from the paper, which says nothing on tracking errors; both are
    standard choices for removing tracker glitches, and the notebook shows other thresholds.
    """
    dev = np.abs(ang - median_filter(ang, size=5, mode="nearest"))
    return {"limit": np.abs(ang) > ARTEFACT_LIMIT, "spike": dev > SPIKE_DEV, "dev": dev}


def _fill(x: np.ndarray, drop: np.ndarray) -> np.ndarray:
    """x with the samples in ``drop`` replaced by linear interpolation from their neighbours."""
    x = x.copy()
    if drop.any() and (~drop).any():
        x[drop] = np.interp(np.flatnonzero(drop), np.flatnonzero(~drop), x[~drop])
    return x


def whisking_amplitudes(sess: dict, band=(6.0, 30.0), limits=(70.0, 80.0, 85.0, 88.0),
                        spike_devs=(10.0, 20.0, 40.0)) -> dict:
    """Per-trial whisker movement amplitude, three readings (claim results-whisking-amplitude).

    (a) range (max minus min) of the angle over the whole trial;
    (b) the same over the sample epoch (pole in reach);
    (c) the peak Hilbert amplitude of the band-passed angle over the trial
        (band: an assumption, see the module docstring).
    Only trials listed as valid whisker trials are used.

    Also returned, per trial, for the tracking errors the round-1 verifier found:
    (a) and (b) without the samples of each artefact mask (``artefact_masks``; ``_limit`` and
    ``_spike``), and (a) with other thresholds (``range_trial_limit<L>``, ``range_trial_spike<D>``);
    (a) after unwrapping the angle with a 180 degree period and removing spikes
    (``range_trial_unwrap_spike``), and the number of wraps (steps over 90 degrees) per trial;
    (c) leaving out EDGE_S (0.2 s) at each end of the trial, where filtfilt and the Hilbert
    transform inflate the amplitude (``hilbert_peak_trim``), and the same after the samples of
    either mask are replaced by interpolation (``hilbert_peak_trim_clean``); the number of samples
    of each mask in the trial.
    """
    w = sess["whisker"]
    t, tr, ang = w["time"], w["trial"], w["angle"].copy()
    bad = ~np.isfinite(ang)
    if bad.any():
        ang[bad] = np.interp(np.flatnonzero(bad), np.flatnonzero(~bad), ang[~bad])
    masks = artefact_masks(ang)
    dev = masks["dev"]
    fs = 1000.0 / np.median(np.diff(t))
    edge = int(round(EDGE_S * fs))
    b, a = butter(2, [band[0] / (fs / 2), band[1] / (fs / 2)], btype="band")
    valid = set(sess["valid_whisker_trials"].tolist())
    tri = sess["trials"]
    rows, extra = [], []

    def rng(v):
        return v.max() - v.min() if v.size > 10 else np.nan

    # Split the whisker samples by trial; samples of one trial are contiguous.
    bounds = np.flatnonzero(np.diff(tr)) + 1
    starts = np.r_[0, bounds]
    ends = np.r_[bounds, len(tr)]
    for s0, e0 in zip(starts, ends):
        trial = int(tr[s0])
        if trial not in valid or e0 - s0 < int(fs):
            continue
        x = ang[s0:e0]
        if bad[s0:e0].mean() > 0.5:
            continue
        amp = np.abs(hilbert(filtfilt(b, a, x)))
        k = np.flatnonzero(tri["id"] == trial)
        pin, pout = (tri["pole_in"][k[0]], tri["pole_out"][k[0]]) if k.size else (np.nan, np.nan)
        m = (t[s0:e0] >= pin) & (t[s0:e0] <= pout)
        rows.append((trial, x.max() - x.min(),
                     (x[m].max() - x[m].min()) if m.sum() > 10 else np.nan,
                     amp.max()))
        lim, spk = masks["limit"][s0:e0], masks["spike"][s0:e0]
        clean = _fill(x, lim | spk)
        amp_clean = np.abs(hilbert(filtfilt(b, a, clean)))
        # Angles past the +/-90 degree limit wrap to the other sign (88, 90, -90, -89, -88, 87: a
        # protraction past 90 degrees); unwrapping with a 180 degree period and then removing spikes
        # gives the range of the continuous angle.
        xu = np.unwrap(x, period=180.0)
        du = np.abs(xu - median_filter(xu, size=5, mode="nearest"))
        e = {"range_trial_limit": rng(x[~lim]), "range_trial_spike": rng(x[~spk]),
             "range_trial_unwrap_spike": rng(xu[du <= SPIKE_DEV]),
             "n_wrap": int((np.abs(np.diff(x)) > 90).sum()),
             "range_sample_limit": rng(x[m & ~lim]), "range_sample_spike": rng(x[m & ~spk]),
             "hilbert_peak_trim": amp[edge:-edge].max(),
             "hilbert_peak_trim_clean": amp_clean[edge:-edge].max(),
             "n_limit": int(lim.sum()), "n_spike": int(spk.sum())}
        for L in limits:
            e[f"range_trial_limit{L:g}"] = rng(x[np.abs(x) <= L])
        for D in spike_devs:
            e[f"range_trial_spike{D:g}"] = rng(x[dev[s0:e0] <= D])
        extra.append(e)
    arr = np.array(rows, float)
    out = {"trial": arr[:, 0].astype(int), "range_trial": arr[:, 1],
           "range_sample": arr[:, 2], "hilbert_peak": arr[:, 3], "fs": fs}
    for k in extra[0]:
        out[k] = np.array([e[k] for e in extra], float)
    return out


def hilbert_peak_synthetic(amplitude=20.0, freq=10.0, seconds=4.0, fs=500.0, band=(6.0, 30.0)):
    """Peak Hilbert amplitude of a pure sinusoid, over the whole trace and without EDGE_S at each end.

    A check of reading (c) on a known input: both should equal ``amplitude``.
    """
    t = np.arange(int(seconds * fs)) / fs
    x = amplitude * np.sin(2 * np.pi * freq * t)
    b, a = butter(2, [band[0] / (fs / 2), band[1] / (fs / 2)], btype="band")
    amp = np.abs(hilbert(filtfilt(b, a, x)))
    edge = int(round(EDGE_S * fs))
    return float(amp.max()), float(amp[edge:-edge].max())


def first_touch_times(sess: dict) -> dict:
    """First touch (protraction or retraction) per trial, in ms, from the touches event series."""
    first = {}
    for v in sess["touches"].values():
        for t, tr in zip(v["start"], v["trial"]):
            if tr not in first or t < first[tr]:
                first[int(tr)] = float(t)
    return first


def touch_response(sv: dict, first: dict, shift_ms: float = 0.0, win_ms: float = 1000.0):
    """Population dF/F after minus before the first touch of each imaged trial.

    The mean over ROIs of dF/F in the window after the (shifted) first touch
    minus that in the window before it, averaged over the subvolume's trials
    with a touch. Used only to check that the imaging and whisker clocks agree
    (protocol, author step 2); the 1 s window is a standard choice.
    Returns (mean difference, number of trials).
    """
    t = sv["time"]
    with np.errstate(all="ignore"):
        pop = np.nanmean(sv["dff"], 0)
    out = []
    for tr in np.unique(sv["trial"]):
        if int(tr) not in first:
            continue
        f = first[int(tr)] + shift_ms
        pre = pop[(t >= f - win_ms) & (t < f)]
        post = pop[(t >= f) & (t < f + win_ms)]
        if pre.size and post.size and np.isfinite(pre).any() and np.isfinite(post).any():
            out.append(np.nanmean(post) - np.nanmean(pre))
    return (float(np.mean(out)) if out else np.nan), len(out)


def reduce_session(sess: dict, shifts=(0.0, -3000.0, 3000.0)) -> dict:
    """Keep what the notebook uses from a session and drop the dF/F matrices.

    Adds per subvolume: ROI ids, counts per plane, frame interval, trials,
    NaN fraction, a hash of the dF/F matrix (to find recordings deposited
    twice), dF/F range, and the first-touch population response at each shift.
    """
    import hashlib

    first = first_touch_times(sess)
    subs = []
    for sv in sess["subvolumes"]:
        d = sv["dff"]
        fin = d[np.isfinite(d)]
        subs.append({
            "key": sv["key"], "descr": sv["descr"], "ids": sv["ids"], "plane": sv["plane"],
            "fov": sv["source_files"][0].split("/")[1] if sv["source_files"] else "",
            "plane_counts": np.bincount(sv["plane"][sv["plane"] >= 0], minlength=sv["n_planes"]).tolist(),
            "n_planes": sv["n_planes"], "frame_ms": float(np.median(np.diff(sv["time"]))),
            "n_frames": len(sv["time"]), "trials": np.unique(sv["trial"]),
            "n_valid_trials": len(sv["valid_trials"]),
            "nan_fraction": float(np.isnan(d).mean()),
            "dff_range": (float(fin.min()), float(np.percentile(fin, 50)), float(fin.max())),
            "hash": hashlib.md5(np.ascontiguousarray(d).tobytes()).hexdigest(),
            "touch": {s: touch_response(sv, first, s) for s in shifts},
            "fields": sv["fields"], "time_unit": sv["time_unit"],
            "id_strs": sv["id_strs"], "id_strs_detailed": sv["id_strs_detailed"],
            "descr_keys": sv["descr_keys"], "roi_array_fields": sv["roi_array_fields"],
            "roi_fields": sv["roi_fields"], "plane_fields": sv["plane_fields"],
        })
    red = {k: v for k, v in sess.items() if k not in ("subvolumes", "whisker")}
    red["subvolumes"] = subs
    w = sess["whisker"]
    red["whisker_summary"] = {
        "names": w["names"], "n": len(w["time"]), "dt_ms": float(np.median(np.diff(w["time"]))),
        "angle_range": (float(np.nanmin(w["angle"])), float(np.nanmax(w["angle"]))),
        "angle_pct": np.nanpercentile(w["angle"], [1, 50, 99]).tolist(),
        "kappa_pct": np.nanpercentile(w["kappa"], [1, 50, 99]).tolist(),
        "angle_nan": float(np.isnan(w["angle"]).mean()),
        "angle_abs_over_85": float(np.mean(np.abs(w["angle"]) > 85)),
        # The first two steps of more than 90 degrees between samples, each with 6 samples on either
        # side, to show what the tracking errors and wraps look like.
        "jump_examples": [np.round(w["angle"][max(j - 6, 0):j + 8], 1).tolist()
                          for j in np.flatnonzero(np.abs(np.diff(w["angle"])) > 90)[:2]],
        "time_unit": w["time_unit"],
    }
    red["whisking"] = {band: whisking_amplitudes(sess, band) for band in [(6.0, 30.0), (4.0, 30.0), (8.0, 25.0)]}
    red["whisking_robust"] = robust_ranges(sess)
    return red


def robust_ranges(sess: dict, q=(1.0, 99.0)) -> np.ndarray:
    """Variant of reading (a): the 1st to 99th percentile range of the angle per valid trial.

    Not a reading the claim lists; shown because the angle holds rare values at
    +/-90 degrees that look like tracking errors (a standard choice of percentiles).
    """
    w = sess["whisker"]
    tr, ang = w["trial"], w["angle"]
    valid = set(sess["valid_whisker_trials"].tolist())
    bounds = np.flatnonzero(np.diff(tr)) + 1
    out = []
    for s0, e0 in zip(np.r_[0, bounds], np.r_[bounds, len(tr)]):
        x = ang[s0:e0]
        if int(tr[s0]) in valid and e0 - s0 >= 500 and np.isfinite(x).mean() > 0.5:
            lo, hi = np.nanpercentile(x, q)
            out.append(hi - lo)
    return np.array(out)


def load_all(names=None) -> list[dict]:
    """Load and reduce every session, one at a time to bound memory."""
    out = []
    for n in names or SESSIONS:
        out.append(reduce_session(load_session(n)))
    return out
