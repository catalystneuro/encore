"""Loading and per-session measures for the BraiDyn-BC lever-pull dataset, dandiset 001425.

Kondo, Sehara, Harukuni, Aoki et al. (2025), bioRxiv, doi:10.1101/2025.02.03.631599.

Every file is streamed from the archive at the pinned version (``DANDISET_VERSION``) with
``remfile`` and ``h5py``; nothing is written to disk. Each NWB file is one session: a task
session (``task``), a resting-state session (``resting-state``) or a sensory-mapping session
(``sensory-stim``). The functions below read only what the analysis needs and return small
per-session summaries, so the notebook can map them over sessions in parallel processes.

Where the parameters come from (claims file ``claims/001425/10.1101-2025.02.03.631599.yaml``,
"criterion"; the paper, Methods, cited by section; or a standard choice that cannot change a
result, said to be one):

- ``LEVER_THRESHOLD_MM = 1.0``: a pull is the lever held beyond 1 mm (Methods, Tone-triggered
  lever-pull task, paragraph 1; claim fig3c-response-rate-increase, reading (b)).
- ``CUE_WINDOW_S = 1.0``: a valid pull starts within 1 s of the tone onset (same passage; Figure
  3 legend).
- ``LIKELIHOOD_MIN = 0.2``: keypoints below this likelihood are dropped (Methods, Processing of
  high-speed videography, last paragraph; claim fig5f-lever-tip-correlation, reading (2)).
- ``PRE_S, POST_S = 1.0, 3.0``: traces around lever-pull onset run from -1 to 3 s (Figure 6c
  range; claims fig6b-*).
- ``BASE_MOVE = (-1.0, -0.5)``: the keypoint baseline window, and the 2 and 3 s.d. onset rules
  (``onset_time``), are the claims file's standard choices for fig6b-movement-order.
- ``SENSORY_WINDOW_S = 2.0``: the response is the trial average over 2 s from stimulus onset
  (Figure 4d legend); ``SENSORY_PRE_S = 2.0`` the pre-stimulus baseline of reading (2b) of
  fig4d-visual-map.
- ``N_BLUE_FRAMES = 8``: the raw blue fluorescence of a session (claim
  methods-no-signal-degradation, reading (a)) is the median over 8 evenly spaced frames of the
  ROI-mean intensity. The criterion asks for the median over all frames; reading every frame
  (54000 of 288 x 288 pixels, about 0.6 s each over the network) does not fit the time limit,
  so this is a subsample, recorded as a deviation.
- ``PUPIL_MAX_PX = 300``: pupil diameters that are not finite, not positive or wider than the
  300 x 300 pixel eye video are set missing before averaging (a standard cleaning step; the
  archive's diameters include values of 1e5 pixels and more, see the notebook).
- The lever-tip keypoint is ``rightbartip`` of the body camera, which the paper's linked code
  describes as "The tip of the lever" (and ``leftbartip`` as "The tip of the pawrest"):
  bdbc_nwb_explorer/data/body_video.csv in https://github.com/BraiDyn-BC/bdbc-nwb-explorer at
  commit 309c5fbdbc065cffdaf46e9160383545e5c8104f, the submodule commit the paper's
  bdbc-data-pipeline pins. The same file set gives the lever's unit as mm (data/daq.csv); the NWB
  files say "a.u.".
- ``CLOCK_SHIFTS_S``: the clock check of the notebook compares the response at the true event
  times with the response at the same times shifted by these offsets (a standard check, not
  from the paper).
"""

from __future__ import annotations

import hashlib
import json
import re
import urllib.error
import urllib.request
from concurrent.futures import ProcessPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile

DANDISET_ID = "001425"
DANDISET_VERSION = "0.250705.0947"
API = "https://api.dandiarchive.org/api"

FS = 30.0                 # effective imaging rate (Methods, Acquisition of wide-field image)
LEVER_THRESHOLD_MM = 1.0
CUE_WINDOW_S = 1.0
LIKELIHOOD_MIN = 0.2
PRE_S, POST_S = 1.0, 3.0
BASE_MOVE = (-1.0, -0.5)
SENSORY_WINDOW_S = 2.0
SENSORY_PRE_S = 2.0
N_BLUE_FRAMES = 8
CLOCK_SHIFTS_S = (-6.0, -3.0, 0.0, 3.0, 6.0)
PUPIL_MAX_PX = 300.0      # width of the eye video (its `dimensions`); see task_session

BODY_PARTS = ["rightbartip", "leftbartip", "rightpawcenter", "leftpawcenter"]
FACE_PARTS = ["nosetip", "lowerjaw"]


def _get_json(url):
    with urllib.request.urlopen(url, timeout=120) as r:
        return json.load(r)


def version_metadata(version=DANDISET_VERSION):
    return _get_json(f"{API}/dandisets/{DANDISET_ID}/versions/{version}/")


def list_assets(version=DANDISET_VERSION) -> pd.DataFrame:
    """All assets of the version, with the NWB file names parsed into subject, date, type, day."""
    rows, url = [], f"{API}/dandisets/{DANDISET_ID}/versions/{version}/assets/?page_size=1000"
    while url:
        page = _get_json(url)
        rows += page["results"]
        url = page["next"]
    df = pd.DataFrame([{"path": r["path"], "asset_id": r["asset_id"], "size": r["size"]} for r in rows])
    pat = re.compile(r"sub-(?P<subject>[^/]+)/sub-[^_]+_ses-(?P<date>\d{4}-\d\d-\d\d)-"
                     r"(?P<type>task|resting-state|sensory-stim)-day(?P<day>\d+)_(?P<suffix>[^/.]+)"
                     r"(?:/.*-(?P<camera>body|face|eye)-camera\.mp4|\.nwb)$")
    parsed = df["path"].str.extract(pat)
    df = pd.concat([df, parsed], axis=1)
    df["day"] = pd.to_numeric(df["day"])
    df["kind"] = np.where(df["path"].str.endswith(".nwb"), "nwb", "mp4")
    return df


def s3_url(asset_id: str) -> str:
    """The S3 address the archive redirects the asset's download to."""
    class _NoRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, *args, **kwargs):
            return None
    opener = urllib.request.build_opener(_NoRedirect)
    req = urllib.request.Request(f"{API}/assets/{asset_id}/download/", method="HEAD")
    try:
        with opener.open(req, timeout=120) as r:
            return r.url
    except urllib.error.HTTPError as e:
        if e.code in (301, 302, 303, 307, 308):
            return e.headers["Location"]
        raise


def open_nwb(asset_id: str) -> h5py.File:
    return h5py.File(remfile.File(s3_url(asset_id)), "r")


def pmap(fn, items, workers=8):
    """Map ``fn`` over ``items`` in worker processes (h5py serialises threads), keeping order."""
    with ProcessPoolExecutor(max_workers=workers) as ex:
        return list(ex.map(fn, items))


def _s(x):
    x = x[()]
    return x.decode() if isinstance(x, bytes) else x


def _rising(x, thr=0.5):
    b = np.asarray(x) > thr
    return np.flatnonzero(b[1:] & ~b[:-1]) + 1


# ---------------------------------------------------------------- every file: metadata and shapes

def session_meta(asset_id: str) -> dict:
    """Metadata, array shapes and a fingerprint of the first dF/F samples of one NWB file."""
    with open_nwb(asset_id) as f:
        out = {"asset_id": asset_id}
        for k in ["session_description", "session_start_time", "general/session_id", "general/notes"]:
            out[k.split("/")[-1]] = _s(f[k]) if k in f else None
        for k in ["age", "date_of_birth", "sex", "subject_id", "genotype", "strain", "species", "weight"]:
            out["subject_" + k] = _s(f["general/subject/" + k]) if "general/subject/" + k in f else None
        d = f["processing/ophys/DfOverF/dFF/data"]
        out["n_dff"], out["n_roi"] = d.shape
        head = d[:600, :]
        out["dff_hash"] = hashlib.md5(np.ascontiguousarray(head).tobytes()).hexdigest()
        ts = f["processing/ophys/DfOverF/dFF/timestamps"]
        out["dff_t0"], out["dff_t1"] = float(ts[0]), float(ts[-1])
        out["dff_dt"] = float((ts[-1] - ts[0]) / (len(ts) - 1))
        out["n_blue"] = f["acquisition/widefield_blue/data"].shape[0]
        out["n_uv"] = f["acquisition/widefield_UV/data"].shape[0]
        out["blue_lambda"] = float(f["general/optophysiology/ImagingPlane_blue/excitation_lambda"][()])
        out["uv_lambda"] = float(f["general/optophysiology/ImagingPlane_UV/excitation_lambda"][()])
        out["roi_names"] = "|".join(x.decode() for x in f["processing/ophys/ImageSegmentation/ROIs/roi_name"][:])
        out["has_body_kp"] = "processing/behavior/body_video_keypoints" in f
        g = "processing/downsampled/body_video_keypoints/rightbartip"
        out["ds_kp_len"] = f[g + "/data"].shape[0] if g in f else None
        out["ds_conf_len"] = f[g + "/confidence"].shape[0] if g in f else None
        out["has_face_kp"] = "processing/behavior/face_video_keypoints" in f
        out["has_pupil"] = "processing/behavior/pupil_tracking" in f
        out["n_trials"] = f["intervals/trials/id"].shape[0] if "intervals/trials" in f else 0
        out["trial_cols"] = "|".join(f["intervals/trials"].attrs.get("colnames", [])) if "intervals/trials" in f else ""
        out["acq"] = "|".join(sorted(f["acquisition"].keys()))
        out["analysis"] = "|".join(sorted(f["analysis"].keys())) if "analysis" in f else ""
        out["lever_unit"] = (f["acquisition/lever/data"].attrs.get("unit") if "acquisition/lever" in f else None)
    return out


# ---------------------------------------------------------------- task sessions

def _trial_table(f, group="intervals/trials"):
    g = f[group]
    t = {c: g[c][:] for c in g.attrs["colnames"]}
    if "trial_outcome" in t:
        t["trial_outcome"] = np.array([x.decode() if isinstance(x, bytes) else x for x in t["trial_outcome"]])
    return pd.DataFrame(t)


def _segments(x, t, onsets, pre=PRE_S, post=POST_S, fs=FS):
    """Rows of ``x`` (time first) from ``pre`` s before to ``post`` s after each onset, 30 Hz."""
    n0, n1 = int(round(pre * fs)), int(round(post * fs))
    idx = np.searchsorted(t, onsets)
    keep = (idx - n0 >= 0) & (idx + n1 < len(t))
    idx = idx[keep]
    if len(idx) == 0:
        return np.full((0, n0 + n1) + x.shape[1:], np.nan), keep
    return np.stack([x[i - n0:i + n1] for i in idx]), keep


def _ds_keypoint(f, cam, part):
    """30 Hz keypoint (x, y) as the archive down-sampled it (likelihood < 0.2 already dropped)."""
    k = f"processing/downsampled/{cam}_video_keypoints/{part}/data"
    return f[k][:].astype(float) if k in f else None


def task_session(asset_id: str) -> dict:
    """Everything the task claims use from one task session, reduced as it loads."""
    out = {"asset_id": asset_id}
    with open_nwb(asset_id) as f:
        tr = _trial_table(f)
        out["trials"] = tr
        # --- raw 5 kHz channels: lever, tone, reward, state_lever
        lev = f["acquisition/lever/data"][:]
        lt = f["acquisition/lever/timestamps"][:]
        tone_on = lt[_rising(f["acquisition/tone/data"][:])]
        rew_on = lt[_rising(f["acquisition/reward/data"][:])]
        out["raw_tone_onsets"] = tone_on
        out["raw_reward_onsets"] = rew_on
        out["lever_range"] = (float(lev.min()), float(lev.max()))
        st = tr["start_time"].to_numpy()
        n = int(round(CUE_WINDOW_S * 5000))
        i0 = np.searchsorted(lt, st)
        above_any, cross_up, first_cross = [], [], []
        for i in i0:
            seg = lev[i:i + n]
            a = seg > LEVER_THRESHOLD_MM
            above_any.append(bool(a.any()))
            up = np.flatnonzero(a[1:] & ~a[:-1])
            cross_up.append(len(up) > 0)
            first_cross.append(lt[i + np.flatnonzero(a)[0]] if a.any() else np.nan)
        tr["lever_above_1mm_in_window"] = above_any
        tr["lever_cross_up_in_window"] = cross_up
        tr["lever_first_above_t"] = first_cross
        tr["lever_at_cue"] = lev[np.minimum(i0, len(lev) - 1)]
        # --- 30 Hz streams
        t30 = f["processing/ophys/DfOverF/dFF/timestamps"][:]
        out["t30_range"] = (float(t30[0]), float(t30[-1]))
        dff = f["processing/ophys/DfOverF/dFF/data"][:]
        out["dff_sd"] = np.nanstd(dff, axis=0)
        out["dff_mean"] = np.nanmean(dff, axis=0)
        lev30 = f["processing/downsampled/lever/data"][:]
        out["ds_reward_onsets"] = t30[_rising(f["processing/downsampled/reward/data"][:])]
        out["ds_tone_onsets"] = t30[_rising(f["processing/downsampled/tone/data"][:])]
        # --- raw blue fluorescence, subsampled frames, mean within each ROI mask
        masks = f["processing/ophys/ImageSegmentation/ROIs/image_mask"][:]
        nb = f["acquisition/widefield_blue/data"].shape[0]
        fr = np.linspace(0, nb - 1, N_BLUE_FRAMES + 2).astype(int)[1:-1]
        blue = np.stack([f["acquisition/widefield_blue/data"][i].astype(float) for i in fr])
        out["blue_roi"] = np.stack([[b[m].mean() for m in masks] for b in blue])  # frames x ROI
        out["blue_frames_idx"] = fr
        # --- keypoints and pupil
        has_body = "processing/behavior/body_video_keypoints" in f
        out["has_body_kp"] = has_body
        kp30 = {}
        if has_body:
            for p in BODY_PARTS:
                kp30["body_" + p] = _ds_keypoint(f, "body", p)
        if "processing/downsampled/face_video_keypoints" in f:
            for p in FACE_PARTS:
                kp30["face_" + p] = _ds_keypoint(f, "face", p)
        pk = "processing/downsampled/pupil_tracking/diameter/data"
        pupil = f[pk][:].astype(float) if pk in f else None
        if pupil is not None:
            # Some ellipse fits give diameters of 1e5 pixels or more, or infinite values; a pupil
            # cannot be wider than the 300-pixel eye video, so such values are set missing.
            bad = ~np.isfinite(pupil) | (pupil <= 0) | (pupil > PUPIL_MAX_PX)
            out["pupil_bad_frac"] = float(bad.mean())
            pupil[bad] = np.nan
        # --- lever-tip and forepaw correlation with the encoder lever (Figure 5e,f)
        if has_body:
            out["corr"] = _keypoint_lever_corr(f, tr, lev, lt, t30, lev30, kp30)
        # --- pull-aligned averages (Figure 6b)
        out["aligned"] = _aligned(tr, t30, dff, lev30, kp30, pupil, rew_on)
        out["clock"] = _clock_contrast(dff, t30, tr.loc[tr["trial_outcome"] == "success", "pull_onset"].dropna().to_numpy())
        out["kp_nan_frac"] = {k: float(np.isnan(v[:, 1]).mean()) for k, v in kp30.items() if v is not None}
    return out


def _clock_contrast(x, t, onsets, shifts=CLOCK_SHIFTS_S, win=1.0):
    """Per ROI, mean of ``x`` over ``win`` s after each (shifted) onset minus ``win`` s before."""
    res = {}
    for s in shifts:
        seg, _ = _segments(x, t, onsets + s, pre=win, post=win)
        n = int(round(win * FS))
        res[s] = (np.nanmean(seg[:, n:], axis=(0, 1)) - np.nanmean(seg[:, :n], axis=(0, 1))
                  if seg.shape[0] else np.full(x.shape[1], np.nan))
    return res


def _successful_frames(tr, t, reading):
    """Boolean mask over times ``t`` inside the successful trials, under reading (a) or (b)."""
    s = tr[tr["trial_outcome"] == "success"]
    if reading == "a":       # trial interval of the trial table
        a, b = s["start_time"].to_numpy(), s["stop_time"].to_numpy()
    else:                    # tone onset to onset + 1 s + T_pull
        a = s["start_time"].to_numpy()
        b = a + CUE_WINDOW_S + s["pull_duration_for_success"].to_numpy()
    m = np.zeros(len(t), bool)
    for x, y in zip(a, b):
        m[np.searchsorted(t, x):np.searchsorted(t, y)] = True
    return m, len(s)


def _pearson(x, y):
    ok = np.isfinite(x) & np.isfinite(y)
    if ok.sum() < 3 or np.std(x[ok]) == 0 or np.std(y[ok]) == 0:
        return np.nan
    return float(np.corrcoef(x[ok], y[ok])[0, 1])


def _keypoint_lever_corr(f, tr, lev, lt, t30, lev30, kp30):
    """Pearson R of keypoint y against the encoder lever, for each reading of the claim."""
    res = {}
    vt = f["processing/behavior/body_video_keypoints/rightbartip/timestamps"][:]
    # lever averaged over each video frame (frame onset to next frame onset), 100 Hz reading
    edges = np.searchsorted(lt, np.append(vt, vt[-1] + 0.01))
    cs = np.concatenate([[0.0], np.cumsum(lev)])
    cnt = np.diff(edges)
    lev100 = np.where(cnt > 0, (cs[edges[1:]] - cs[edges[:-1]]) / np.maximum(cnt, 1), np.nan)
    for reading in ["a", "b"]:
        m100, nsucc = _successful_frames(tr, vt, reading)
        m30, _ = _successful_frames(tr, t30, reading)
        res[("n_success",)] = nsucc
        for p in BODY_PARTS:
            g = f[f"processing/behavior/body_video_keypoints/{p}"]
            y = g["data"][:, 1].astype(float)
            c = g["confidence"][:]
            n = min(len(y), len(vt))
            y, c = y[:n], c[:n]
            res[(p, "100Hz", "kept", reading)] = _pearson(y[m100[:n]], lev100[:n][m100[:n]])
            yd = np.where(c >= LIKELIHOOD_MIN, y, np.nan)
            res[(p, "100Hz", "dropped", reading)] = _pearson(yd[m100[:n]], lev100[:n][m100[:n]])
            k = kp30.get("body_" + p)
            if k is not None:
                res[(p, "30Hz", "dropped", reading)] = _pearson(k[m30, 1], lev30[m30])
    return res


def onset_time(trace, t, base=BASE_MOVE, nsd=2.0):
    """First time after the baseline window that ``trace`` leaves its baseline mean +/- nsd s.d."""
    b = (t >= base[0]) & (t < base[1])
    mu, sd = np.nanmean(trace[b]), np.nanstd(trace[b])
    after = np.flatnonzero((t >= base[1]) & (np.abs(trace - mu) > nsd * sd))
    return float(t[after[0]]) if len(after) else np.nan


def _aligned(tr, t30, dff, lev30, kp30, pupil, rew_on):
    """Trial averages around lever-pull onset, for successful trials and for all valid pulls."""
    out = {}
    tt = (np.arange(-int(PRE_S * FS), int(POST_S * FS))) / FS
    out["t"] = tt
    base_move = (tt >= BASE_MOVE[0]) & (tt < BASE_MOVE[1])
    for sel in ["success", "valid"]:
        if sel == "success":
            rows = tr[(tr["trial_outcome"] == "success") & tr["pull_onset"].notna()]
        else:
            rows = tr[tr["trial_outcome"].isin(["success", "failure"]) & tr["pull_onset"].notna()]
        on = rows["pull_onset"].to_numpy()
        seg, keep = _segments(dff, t30, on)
        r = {"n": int(seg.shape[0])}
        if seg.shape[0] >= 2:
            r["dff_mean"] = np.nanmean(seg, axis=0)            # time x ROI
            r["dff_sd"] = np.nanstd(seg, axis=0)               # across-trial s.d., time x ROI
            r["dff_base"] = np.nanmean(seg[:, tt < 0, :], axis=1)   # trial x ROI, -1 to 0 s
            ls, _ = _segments(lev30, t30, on)
            r["lever_mean"] = np.nanmean(ls, axis=0)
            for k, v in kp30.items():
                if v is None:
                    continue
                s, _ = _segments(v, t30, on)                  # trial x time x 2
                b = np.nanmean(s[:, base_move, :], axis=1, keepdims=True)
                disp = np.sqrt(np.sum((s - b) ** 2, axis=2))   # displacement from baseline position
                r["kp_" + k] = np.nanmean(disp, axis=0)
                r["kpxy_" + k] = np.nanmean(s, axis=0)               # time x 2, trial-averaged position
            if pupil is not None:
                s, _ = _segments(pupil, t30, on)
                r["pupil_mean"] = np.nanmean(s, axis=0)
            if sel == "success" and len(rew_on):
                # reading (b) of fig6b-motor-somatosensory-after-reward: 0.5 to 2 s after reward
                on_k = on[keep]
                post, base = [], []
                for j, p in enumerate(on_k):
                    k = np.searchsorted(rew_on, p)
                    if k >= len(rew_on) or rew_on[k] - p > 2.0:
                        continue
                    a, b = np.searchsorted(t30, rew_on[k] + 0.5), np.searchsorted(t30, rew_on[k] + 2.0)
                    if b >= len(t30):
                        continue
                    post.append(np.nanmean(dff[a:b], axis=0))
                    base.append(r["dff_base"][j])
                if post:
                    r["post_reward_minus_base"] = np.nanmean(np.array(post) - np.array(base), axis=0)
                    r["n_reward_matched"] = len(post)
        out[sel] = r
    return out


# ---------------------------------------------------------------- resting-state, day 0 (Figure S2b)

def resting_signals(asset_id: str, rois=("MOs_l", "MOp_l", "SSp_bfd_l", "RSPd_l", "RSPagl_l", "VISp_r")):
    """Corrected dF/F and uncorrected dF_B/F_B of the named ROIs of a resting-state session."""
    with open_nwb(asset_id) as f:
        names = [x.decode() for x in f["processing/ophys/ImageSegmentation/ROIs/roi_name"][:]]
        idx = [names.index(r) for r in rois]
        dff = f["processing/ophys/DfOverF/dFF/data"][:][:, idx]
        dffb = f["processing/ophys/DfOverF/dFF_B/data"][:][:, idx]
    return {"asset_id": asset_id, "rois": list(rois), "dff": dff, "dff_b": dffb}


# ---------------------------------------------------------------- sensory mapping (Figure 4d)

SENSORY_TTL = ["stim_visual", "stim_whisker", "stim_auditory"]


def sensory_session(asset_id: str, gap_s=3.0) -> dict:
    """ROI responses averaged over stimuli, for each stimulus TTL channel and each trial code.

    The files give no meaning for the trial table's ``stim_modality`` codes, so responses are
    computed both for the onsets of each TTL channel, as the channels are named, and for the
    trial-table onsets of each code; the notebook shows how they relate. A visual stimulus is a
    1 s train of 10 Hz flashes (Methods, Sensory mapping), so TTL rising edges closer than
    ``gap_s`` to the previous one belong to the same stimulus; a standard choice that cannot
    change the onsets, as stimuli are 10 to 15 s apart. ``pulses`` counts the rising edges per
    stimulus, which tells the 10 Hz train apart.
    """
    with open_nwb(asset_id) as f:
        names = [x.decode() for x in f["processing/ophys/ImageSegmentation/ROIs/roi_name"][:]]
        t30 = f["processing/ophys/DfOverF/dFF/timestamps"][:]
        dff = f["processing/ophys/DfOverF/dFF/data"][:]
        tr = _trial_table(f)
        out = {"asset_id": asset_id, "names": names, "trials": tr, "resp": {}, "n": {}, "pulses": {},
               "n_frames": len(t30)}
        lt = f["acquisition/stim_auditory/timestamps"][:]
        onsets = {}
        for ch in SENSORY_TTL:
            if "acquisition/" + ch not in f:
                continue
            x = f["acquisition/" + ch + "/data"][:]
            on = lt[_rising(x, 0.5 * np.nanmax(x))]
            g = on[np.concatenate([[True], np.diff(on) > gap_s])] if len(on) else on
            out["pulses"][ch] = len(on) / max(len(g), 1)
            onsets["ch:" + ch] = g
        for c in sorted(tr["stim_modality"].unique()):
            onsets[f"code:{c}"] = tr.loc[tr["stim_modality"] == c, "start_time"].to_numpy()
        npre = int(SENSORY_PRE_S * FS)
        for key, on in onsets.items():
            seg, _ = _segments(dff, t30, on, pre=SENSORY_PRE_S, post=SENSORY_WINDOW_S)
            out["n"][key] = int(seg.shape[0])
            out[key + "_onsets"] = on
            if seg.shape[0] == 0:
                continue
            post = np.nanmean(seg[:, npre:, :], axis=(0, 1))
            pre = np.nanmean(seg[:, :npre, :], axis=(0, 1))
            out["resp"][key] = {"none": post, "baseline": post - pre}
            out.setdefault("clock", {})[key] = _clock_contrast(dff, t30, on)
    return out


def displacement_of_mean(xy, t, base=BASE_MOVE):
    """Distance of a trial-averaged (x, y) trajectory from its mean over the baseline window."""
    b = (t >= base[0]) & (t < base[1])
    return np.sqrt(np.nansum((xy - np.nanmean(xy[b], axis=0)) ** 2, axis=1))


def nan_pearson(x, y):
    return _pearson(np.asarray(x, float), np.asarray(y, float))
