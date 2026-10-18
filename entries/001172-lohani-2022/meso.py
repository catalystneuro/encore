"""Loading and measures for dandiset 001172 (Lohani, Moberly et al. 2022, Nature Neuroscience).

The dandiset holds dual-colour mesoscopic imaging of ACh3.0 (blue excitation, green emission) and
jRCaMP1b (green excitation, red emission) with a 395 nm control channel, face video (FaceMap
output), pupil area, wheel speed and TTL pulses, from 4 mice (grabAM05 to grabAM08).

Everything is streamed from the archive. The blue and green ΔF/F movies (256 x 256 pixels, float64,
gzip, one chunk per 19 frames) are read chunk by chunk with parallel HTTP range requests and reduced
to parcel means as they arrive; no movie is held in memory.

Where parameters come from:
- Parcels: the Allen parcel masks `parcells_updated121519.mat`, the brain mask `brainMask.mat` and
  the anterior-posterior order of the Methods, from the paper's code (repository
  cardin-higley-lab/Lohani_Moberly_et_al_2022 at commit c337686). The dandiset's ΔF/F is in the
  same atlas space, rotated by 180 degrees (shown in the notebook). A parcel's trace is the mean
  ΔF/F of its pixels inside the brain mask; a parcel with fewer than 25% of its pixels inside the
  mask is left out, as `pixels2rois.m` does.
- Frame times: ΔF/F frame i is at blue LED pulse i + 499, because the code's detrending drops the
  first 500 frames (`smrxExtractionPreProcessing.m`); the notebook shows this from the data. Both
  colours are given the same times, as in the code. FaceMap and pupil frame i are at pupil camera
  pulse i, as in the code (`pupil_time = timing.pupilcamstart(1:length(face_Norm))`).
- Locomotion epochs: the change-point method of `wheel_changepoints.m` (2 s windows, moving SD
  threshold 0.005, epochs of half a window or less and epochs with mean speed at or below 0.02 m/s
  removed), run on the dandiset's WheelSpeed (m/s, 5 kHz).
- Face movement: FaceMap PC1 of the face, sign flipped when negatively skewed and normalised by
  the mean and SD of its lowest 10% (`AdjustFacePCNormalizeVideoVars.m`).
- Sustained states and face onsets: `getSustainedStates.m`, `extractFacePupilTStamps.m` and
  `changepoints.m`, with the parameters of `SustainedStatesCorrelation.m` and
  `faceStateTransition.m`.
- Correlations: `calcMaxCrossCorr.m` (MATLAB crosscorr within ±5 frames, the value of largest
  magnitude), Fisher z averaged over epochs, stratified permutation of epoch labels
  (`permuteEpochLabels.m`, `permutePval.m`) and Benjamini-Yekutieli FDR at q = 0.01.
- Regression: ridge regression with the penalty chosen per parcel by maximising the marginal
  likelihood (as ridgeMML.m, Musall et al. 2019), ten-fold cross-validation over contiguous
  blocks, R2 averaged over folds (Methods), predictors scaled with the training folds' statistics.
  The penalty grid (1e-3 to 1e6, 91 values) is a choice made here; ridgeMML optimises it. The
  code for this step is not in the repository, so the design (signed or absolute wheel speed, no
  lags) is a choice too; the notebook uses |WheelSpeed| (the stored series is signed; the paper's
  predictor is "locomotion speed") and shows the signed series as a variant.
"""

from __future__ import annotations

import io
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import remfile
import requests
import scipy.io as sio
from dandi.dandiapi import DandiAPIClient
from isal import isal_zlib
from threadpoolctl import threadpool_limits

DANDISET_ID = "001172"
DANDISET_VERSION = "0.260129.0829"
CODE_REPO = "cardin-higley-lab/Lohani_Moberly_et_al_2022"
CODE_COMMIT = "c337686fb3776112f1609ec1a19256d277c930fd"
CODE_RAW = f"https://raw.githubusercontent.com/{CODE_REPO}/{CODE_COMMIT}/"
PARCELS_FILE = "Figure3ExtractStatesCorrelation/Functions/parcells_updated121519.mat"
BRAINMASK_FILE = "PreProcessingCode/Functions/parcellation/AllenParcellationLan/allanParcellationTiffs/brainMask.mat"

FS_IMAGING = 10.0       # Hz per colour (Methods)
FS_WHEEL = 5000.0       # Hz (Spike2)
DETREND_DROP = 499      # first ΔF/F frame is raw frame 499 (0-based); code drops filtLen/2 = 500 samples
N_WORKERS = 16

# Methods, Post-processing analysis: anterior to posterior order of the 23 parcels per hemisphere.
AP_ORDER = ["MOs", "MOp", "SSp-m", "SSp-ul", "SSp-n", "SSp-ll", "SSp-un", "SSp-tr", "SSp-bfd", "SSs",
            "PTLp", "VISam", "AUD", "RSPagl", "RSPd", "VISal", "VISpm", "TEa", "VISli", "VISl", "VISp",
            "VISpor", "VISpl"]
# Area groups of SustainedStatesCorrelation.m.
GROUPS = {"visual": ["VISp", "VISpm", "VISam", "VISl", "VISli", "VISpl", "VISpor", "VISal"],
          "retrosplenial": ["RSPagl", "RSPd"], "auditory": ["TEa", "AUD"], "parietal": ["PTLp"],
          "somatosensory": ["SSp-bfd", "SSs", "SSp-tr", "SSp-n", "SSp-un", "SSp-ul", "SSp-ll", "SSp-m"],
          "frontal-motor": ["MOp", "MOs"]}
LEFT_OUT = ["RSPv", "SC", "IC", "ACA", "PL"]   # Methods: masked for vasculature, or not cortex

# Sessions the code's state analyses use: spontaneous and air-puff sessions (not visual stimulus).
SESSIONS = {
    "grabAM05": ["11222019-spont", "11232019-airpuffs", "11262019-airpuffs"],
    "grabAM06": ["11222019-spont", "11242019-airpuffs"],
    "grabAM07": ["11232019-spont", "11242019-airpuffs"],
    "grabAM08": ["11232019-spont", "11242019-airpuffs"],
}
SESSION_WITHOUT_PUFFS = ("grabAM07", "11262019-airpuffs")   # air-puff session with no Airpuff table
VIS_SESSIONS = {"grabAM05": "11222019-vis-stim", "grabAM06": "11222019-vis-stim",
                "grabAM07": "11232019-vis-stim", "grabAM08": "11232019-vis-stim"}


def asset_path(mouse, session):
    return f"sub-{mouse}/sub-{mouse}_ses-{session}_behavior+image+ophys.nwb"


_URLS = {}


def asset_url(path):
    if path not in _URLS:
        with DandiAPIClient() as client:
            ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
            _URLS[path] = ds.get_asset_by_path(path).get_content_url(follow_redirects=1, strip_query=True)
    return _URLS[path]


def open_nwb(path):
    url = asset_url(path)
    return url, h5py.File(remfile.File(url), "r")


# --- streaming chunks ----------------------------------------------------------------------------

_session = requests.Session()
_session.mount("https://", requests.adapters.HTTPAdapter(pool_connections=N_WORKERS, pool_maxsize=N_WORKERS))


def _fetch(url, offset, size):
    for attempt in range(4):
        try:
            r = _session.get(url, headers={"Range": f"bytes={offset}-{offset + size - 1}"}, timeout=120)
            r.raise_for_status()
            if len(r.content) != size:
                raise IOError(f"short read {len(r.content)} of {size}")
            return r.content
        except (requests.RequestException, IOError):
            if attempt == 3:
                raise
    raise RuntimeError("unreachable")


def reduce_many(jobs):
    """Apply a reducer to every chunk of one or more (frames, rows, cols) datasets.

    `jobs` is a list of (url, dataset, reducer, frames); `reducer(block, first_frame)` gets the
    decompressed frames of one chunk. Chunks are read in parallel by HTTP range requests and
    decompressed here (gzip only, as in these files). With `frames` (or None for all), only chunks
    holding one of those frame indices are read. Returns, per job, the reducer outputs in frame
    order.
    """
    items = []
    for j, (url, dset, reducer, frames) in enumerate(jobs):
        if dset.compression != "gzip" or dset.shuffle or dset.fletcher32:
            raise ValueError(f"unexpected filters on {dset.name}")
        cf = dset.chunks[0]
        n_chunks = -(-dset.shape[0] // cf)
        wanted = range(n_chunks) if frames is None else sorted({int(i) // cf for i in frames})
        for k in wanted:
            info = dset.id.get_chunk_info_by_coord((k * cf,) + (0,) * (dset.ndim - 1))
            items.append((j, k, cf, dset.shape, dset.dtype, url, info.byte_offset, info.size, reducer))

    def work(item):
        j, k, cf, shape, dtype, url, offset, size, reducer = item
        block = np.frombuffer(isal_zlib.decompress(_fetch(url, offset, size)), dtype=dtype)
        block = block.reshape((cf,) + tuple(shape[1:]))
        n = min(cf, shape[0] - k * cf)
        return reducer(block[:n], k * cf)

    with threadpool_limits(1), ThreadPoolExecutor(N_WORKERS) as ex:
        results = list(ex.map(work, items))
    out = [[] for _ in jobs]
    for item, r in zip(items, results):
        out[item[0]].append(r)
    return out


# --- parcels -------------------------------------------------------------------------------------

def _get_mat(path):
    r = requests.get(CODE_RAW + path, timeout=120)
    r.raise_for_status()
    return sio.loadmat(io.BytesIO(r.content), squeeze_me=True, struct_as_record=False)


def load_parcels():
    """The code's Allen parcels and brain mask, in the orientation of the dandiset's ΔF/F.

    Returns a dict with `mask` (256 x 256 bool, MATLAB orientation), `indicators` (56 parcels,
    MATLAB orientation), `names`, and the selection of 46 parcels used here (`sel`, with `area`,
    `hemi`, `ap_rank`).
    """
    pn = _get_mat(PARCELS_FILE)["parcells_new"]
    mask = _get_mat(BRAINMASK_FILE)["mask"].astype(bool)
    names = [str(n) for n in pn.names]
    canon = {a.lower(): a for a in AP_ORDER + LEFT_OUT}
    sel = []
    for i, n in enumerate(names):
        hemi, area = n.split("-", 1)
        area = canon[area.lower().replace("vls", "vis")]
        if area in LEFT_OUT:
            continue
        sel.append({"index": i, "name": n, "hemi": hemi, "area": area, "ap_rank": AP_ORDER.index(area) + 1})
    return {"mask": mask, "indicators": np.asarray(pn.indicators) > 0, "names": names, "sel": sel}


def orient(img):
    """MATLAB-orientation image to the orientation of the dandiset's ΔF/F (rotation by 180 degrees)."""
    return np.rot90(img, 2)


def parcel_weights(parcels):
    """Matrix (65536 x 47) giving the mean over each selected parcel's in-mask pixels, and the brain
    mean as the last column. Returns the matrix and the per-parcel fraction of pixels in the mask."""
    mask = orient(parcels["mask"]).ravel()
    cols, frac = [], []
    for p in parcels["sel"]:
        pix = orient(parcels["indicators"][:, :, p["index"]]).ravel()
        inside = pix & mask
        frac.append(inside.sum() / pix.sum())
        w = inside.astype(float)
        cols.append(w / w.sum() if inside.sum() / pix.sum() > 0.25 else np.full(w.shape, np.nan))
    cols.append(mask / mask.sum())
    return np.column_stack(cols), np.array(frac)


# --- one session ---------------------------------------------------------------------------------

def _ttl(f):
    names = [n.decode() if isinstance(n, bytes) else str(n) for n in f["acquisition/TTLTypesTable/event_name"][:]]
    ty = f["acquisition/TTLsTable/ttl_type"][:]
    ts = f["acquisition/TTLsTable/timestamp"][:]
    return {n: ts[ty == i] for i, n in enumerate(names)}


def _intervals(f, name):
    if name not in f["intervals"]:
        return None
    g = f["intervals/" + name]
    return np.column_stack([g["start_time"][:], g["stop_time"][:]])


def load_session(mouse, session, weights):
    """Parcel ΔF/F of both colours, behaviour and timing of one session, streamed."""
    path = asset_path(mouse, session)
    url, f = open_nwb(path)
    ttl = _ttl(f)
    out = {"mouse": mouse, "session": session, "ttl_counts": {k: len(v) for k, v in ttl.items()}}
    w = np.nan_to_num(weights)
    pix = np.flatnonzero(w.sum(1) > 0)
    w = w[pix]
    names = {"ach": "DFFOnePhotonSeriesBlue", "ca": "DFFOnePhotonSeriesGreen"}
    def reducer(b, k0):
        flat = b.reshape(b.shape[0], -1)
        return flat[:, pix] @ w, (flat != 0).any(0)
    jobs = [(url, f["processing/ophys/" + n + "/data"], reducer, None) for n in names.values()]
    for (colour, name), parts in zip(names.items(), reduce_many(jobs)):
        x = np.concatenate([p[0] for p in parts])
        x[:, np.isnan(weights).any(0)] = np.nan
        out[colour] = x
        out[colour + "_file_start"] = float(f["processing/ophys/" + name + "/starting_time"][()])
        out[colour + "_nonzero"] = np.any([p[1] for p in parts], axis=0).reshape(f["processing/ophys/" + name + "/data"].shape[1:])
    n = out["ach"].shape[0]
    out["t"] = ttl["TTLSignalBlueLED"][DETREND_DROP:DETREND_DROP + n]
    if len(out["t"]) != n:
        raise ValueError("fewer blue LED pulses than ΔF/F frames")
    out["n_raw"] = f["acquisition/OnePhotonSeriesBlueExcitationGreenChannel/data"].shape[0]
    out["blue_ttl"] = ttl["TTLSignalBlueLED"]
    out["green_ttl"] = ttl["TTLSignalGreenLED"]
    # behaviour
    speed = f["processing/behavior/WheelSpeed/data"][:]
    out["wheel_rate"] = float(f["processing/behavior/WheelSpeed/starting_time"].attrs["rate"])
    out["wheel_start"] = float(f["processing/behavior/WheelSpeed/starting_time"][()])
    out["wheel_unit"] = f["processing/behavior/WheelSpeed/data"].attrs["unit"]
    out["wheel_on_all"], out["wheel_off_all"] = wheel_changepoints(speed, out["wheel_rate"])
    tw = out["wheel_start"] + (np.arange(len(speed)) + 1) / out["wheel_rate"]
    out["speed_100hz_t"] = tw[::50]
    out["speed_100hz"] = speed.reshape(-1)[: len(speed) // 50 * 50].reshape(-1, 50).mean(1)
    out["speed_100hz_t"] = out["speed_100hz_t"][: len(out["speed_100hz"])]
    # quiescence check of the code: any sample above 0.03 m/s; keep the times of those samples
    fast = np.abs(speed) > 0.03
    out["fast_t"] = tw[fast]
    out["wheel_frame"] = np.interp(out["t"], out["speed_100hz_t"], out["speed_100hz"])
    del speed, fast, tw
    face = f["processing/behavior/MotionSVDSeriesFace/data"][:, :25].astype(float)
    out["face_pcs"] = face
    out["face_file_t"] = f["processing/behavior/MotionSVDSeriesFace/timestamps"][:]
    out["pupil"] = f["processing/behavior/PupilTracking/pupil_area/data"][:, 0].astype(float)
    out["pupil_unit"] = f["processing/behavior/PupilTracking/pupil_area/data"].attrs["unit"]
    out["face_t"] = ttl["TTLSignalPupilCamera"][: face.shape[0]]
    if len(out["face_t"]) != face.shape[0]:
        raise ValueError("fewer pupil camera pulses than FaceMap frames")
    out["wheel_activation"] = _intervals(f, "WheelActivation")
    out["airpuff"] = _intervals(f, "Airpuff")
    out["face_norm"] = normalise_face(face[:, 0])
    pr = f["processing/ophys/Fluorescence/RoiResponseSeriesParcellated/data"]
    out["parcellated_shape"] = pr.shape
    f.close()
    return out


def normalise_face(pc1):
    """AdjustFacePCNormalizeVideoVars.m: flip sign if negatively skewed, then (x - m) / s with m and
    s the mean and SD of the lowest 10% of values."""
    x = pc1 - pc1.mean()
    if np.mean(x ** 3) < 0:
        pc1 = -pc1
    low = np.sort(pc1)[: int(np.ceil(len(pc1) * 0.1))]
    return (pc1 - low.mean()) / low.std(ddof=1)


# --- locomotion change points (wheel_changepoints.m) ---------------------------------------------

def _same_sum(a, w):
    """MATLAB conv(a, ones(1, w), 'same') for even w: sum of a over [k - w/2 + 1, k + w/2]."""
    c = np.concatenate([[0.0], np.cumsum(a)])
    n = len(a)
    k = np.arange(n)
    lo = np.clip(k - w // 2 + 1, 0, n)
    hi = np.clip(k + w // 2 + 1, 0, n)
    return c[hi] - c[lo]


def wheel_changepoints(speed, fs):
    """Locomotion on and off times (s, Spike2 clock, sample k at k/fs with k from 1)."""
    speed = np.asarray(speed, float)
    n = len(speed)
    W = int(round(2.0 * fs))
    W += W % 2
    num = (~np.isnan(speed)).astype(float)
    s = np.nan_to_num(speed)
    mav = _same_sum(s, W)
    dof = _same_sum(num, W)
    msq = _same_sum(s ** 2, W)
    with np.errstate(invalid="ignore", divide="ignore"):
        sd = np.sqrt((msq - mav ** 2 / dof) / (dof - 1))
        mav = mav / dof
        h = W // 2
        zf = np.concatenate([np.full(W, np.nan), mav[3 * h: n - h] / sd[h - 1: n - 3 * h - 1], np.full(W, np.nan)])
        zb = np.concatenate([np.full(W, np.nan), mav[h - 1: n - 3 * h - 1] / sd[3 * h - 1: n - h - 1], np.full(W, np.nan)])
    sig = sd > 0.005
    sig[[0, -1]] = False
    d = np.diff(sig.astype(int))
    on = np.flatnonzero(d == 1) + 1           # 1-based index i where sig(i)=0, sig(i+1)=1
    off = np.flatnonzero(d == -1) + 2         # 1-based index of the first sample after the epoch
    for arr, z in ((on, zf), (off, zb)):
        for ii in range(len(arr)):
            i = arr[ii]
            if (z is zf and i == 1) or (z is zb and i == n):
                continue
            b, e = max(i - h, 1), min(i + h, n)
            seg = z[b - 1: e]
            m = 1 if np.all(np.isnan(seg)) else int(np.nanargmax(seg)) + 1
            arr[ii] = i - h + m - 1
    keep = (off - on) > h
    on, off = on[keep], off[keep]
    on[on < 1] = 1
    off[off < 1] = 1
    mean_speed = np.array([np.mean(np.abs(speed[a - 1: b])) for a, b in zip(on, off)])
    keep = mean_speed > 0.02
    return on[keep] / fs, off[keep] / fs


# --- face state change points (changepoints.m) ----------------------------------------------------

def matlab_smooth(x, span):
    """MATLAB smooth(x, span), moving average; an even span is reduced by one; the window shrinks at
    the ends."""
    span = span - 1 if span % 2 == 0 else span
    h = span // 2
    n = len(x)
    c = np.concatenate([[0.0], np.cumsum(x)])
    out = np.empty(n)
    for i in range(n):
        r = min(h, i, n - 1 - i)
        out[i] = (c[i + r + 1] - c[i - r]) / (2 * r + 1)
    return out


def changepoints(data, thr, times, fs, smooth_win=1):
    sm = matlab_smooth(np.asarray(data, float), int(smooth_win * fs))
    above = (sm > thr).astype(int)
    tmp = np.concatenate([[0], above])
    tmp[-1] = 0
    d = np.diff(tmp)
    on = np.flatnonzero(d == 1)      # 0-based data indices
    off = np.flatnonzero(d == -1)
    if len(on) == 0:
        return np.array([]), np.array([])
    gap = on[1:] - off[:-1]
    drop = np.flatnonzero(gap < 0.2 * fs) + 1
    on_int = np.delete(on, drop)
    off_int = np.zeros(len(on_int), int)
    for tt in range(len(on_int) - 1):
        idx = off[(off >= on_int[tt]) & (off < on_int[tt + 1])]
        off_int[tt] = idx[-1]
    off_int[-1] = off[-1]
    keep = (off_int - on_int) > round(0.5 * fs)
    return times[on_int[keep]], times[off_int[keep]]


# --- sustained states (getSustainedStates.m) and face onsets (extractFacePupilTStamps.m) ----------

def _clip(on, off, t0, t1):
    on, off = on.copy(), off.copy()
    for i in range(len(on)):
        if on[i] < t1 and off[i] > t1:
            off[i] = t1 - 1
        if on[i] < t0 and off[i] > t0:
            on[i] = t0 + 1
    return on, off


def _exclude_events(on, off, events, around):
    if events is None or len(events) == 0 or len(on) == 0:
        return np.asarray(on), np.asarray(off)
    ev = np.sort(events)
    pre, post = ev - around, ev + around
    new_on = np.sort(np.concatenate([on, pre, post]))
    new_off = np.sort(np.concatenate([off, pre, post]))
    keep = [not np.any((a >= pre) & (b <= post)) for a, b in zip(new_on, new_off)]
    return new_on[keep], new_off[keep]


def _split_fast(on, off, fast_t):
    tmp_on, tmp_off = list(on), list(off)
    for rr in range(len(on)):
        sel = fast_t[(fast_t > on[rr]) & (fast_t < off[rr])]
        if len(sel):
            tmp_off[rr] = sel[0] - 0.1
            tmp_off.append(off[rr])
            tmp_on.append(sel[-1] + 0.1)
    return np.sort(tmp_on), np.sort(tmp_off)


STATE_PARAMS = dict(since_loc_on=3, before_loc_off=3, since_sit_on=10, before_sit_off=10, since_event=10,
                    min_run=5, min_arousal=5, min_sit=5)


def sustained_states(s, p=STATE_PARAMS):
    """Sustained locomotion, high face and low face epochs of one session (lists of (on, off))."""
    t0, t1 = s["t"][0], s["t"][-1]
    puffs = None if s["airpuff"] is None else s["airpuff"][:, 0]
    won, woff = s["wheel_on_all"], s["wheel_off_all"]
    idx = (won < t1) & (woff > t0)
    on, off = _clip(won[idx], woff[idx], t0, t1)
    on, off = _exclude_events(on, off, puffs, p["since_event"])
    keep = (off - on) >= p["min_run"] + p["since_loc_on"] + p["before_loc_off"]
    loc = np.column_stack([on[keep] + p["since_loc_on"], off[keep] - p["before_loc_off"]])
    sit_on = np.concatenate([[0.0], woff])
    sit_off = np.concatenate([won, [t1]])
    idx = (sit_on < t1) & (sit_off > t0)
    son, soff = _clip(sit_on[idx], sit_off[idx], t0, t1)
    son, soff = _split_fast(son, soff, s["fast_t"])
    son_int, soff_int = _exclude_events(son, soff, puffs, p["since_event"])
    keep = (soff_int - son_int) >= p["min_sit"] + p["since_sit_on"] + p["before_sit_off"]
    sit_final = np.column_stack([son_int[keep] + p["since_sit_on"], soff_int[keep] - p["before_sit_off"]])
    ft, fn = s["face_t"], s["face_norm"]
    q = np.zeros(len(ft), bool)
    for a, b in zip(son_int, soff_int):
        q |= (ft > a) & (ft < b)
    hi_thr, lo_thr = np.quantile(fn[q], 0.6), np.quantile(fn[q], 0.4)
    hon, hoff = changepoints(fn, hi_thr, ft, FS_IMAGING)
    lon, loff = changepoints(-fn, -lo_thr, ft, FS_IMAGING)
    out = {"loc": loc, "sit": sit_final, "thresholds": (hi_thr, lo_thr)}
    for key, a, b in (("face_high", hon, hoff), ("face_low", lon, loff)):
        k = (b - a) >= p["min_arousal"]
        a, b = a[k], b[k]
        inside = [np.any((x >= sit_final[:, 0]) & (y <= sit_final[:, 1])) for x, y in zip(a, b)]
        out[key] = np.column_stack([a[inside], b[inside]]) if len(a) else np.zeros((0, 2))
    return out


def match_epochs(states):
    """Same number of epochs per state (the longest of each) and the same duration per rank, as in
    SustainedStatesCorrelation.m. Returns None when a state has no epoch."""
    keys = ("loc", "face_high", "face_low")
    if any(len(states[k]) == 0 for k in keys):
        return None
    n = min(len(states[k]) for k in keys)
    picked = {}
    for k in keys:
        e = states[k]
        order = np.argsort(-(e[:, 1] - e[:, 0]), kind="stable")[:n]
        picked[k] = e[order]
    dur = np.min([picked[k][:, 1] - picked[k][:, 0] for k in keys], axis=0)
    return {k: np.column_stack([picked[k][:, 0], picked[k][:, 0] + dur]) for k in keys}


def face_onsets(s, p=None, include_last=False):
    """Face movement onsets of faceStateTransition.m / extractFacePupilTStamps.m.

    The code's quiescent periods here are [0, wheelOff(1:end-1)] to wheelOn, so the period after
    the last locomotion epoch is left out (getSustainedStates.m keeps it). `include_last=True`
    keeps it, as a variant."""
    p = p or dict(since_sit_on=10, before_sit_off=10, since_event=10, min_sit=5, before_arousal_on=4)
    t0, t1 = s["t"][0], s["t"][-1]
    puffs = None if s["airpuff"] is None else s["airpuff"][:, 0]
    won, woff = s["wheel_on_all"], s["wheel_off_all"]
    if include_last:
        sit_on = np.concatenate([[0.0], woff])
        sit_off = np.concatenate([won, [t1]])
    else:
        sit_on = np.concatenate([[0.0], woff[:-1]])
        sit_off = won.copy()
    idx = (sit_on < t1) & (sit_off > t0)
    son, soff = _clip(sit_on[idx], sit_off[idx], t0, t1)
    son, soff = _split_fast(son, soff, s["fast_t"])
    son_int, soff_int = _exclude_events(son, soff, puffs, p["since_event"])
    keep = (soff_int - son_int) >= p["min_sit"] + p["since_sit_on"] + p["before_sit_off"]
    sit_final = np.column_stack([son_int[keep] + p["since_sit_on"], soff_int[keep] - p["before_sit_off"]])
    ft, fn = s["face_t"], s["face_norm"]
    q = np.zeros(len(ft), bool)
    for a, b in zip(son_int, soff_int):
        q |= (ft > a) & (ft < b)
    hon, hoff = changepoints(fn, np.quantile(fn[q], 0.6), ft, FS_IMAGING)
    lon, loff = changepoints(-fn, -np.quantile(fn[q], 0.4), ft, FS_IMAGING)

    def within(a, b):
        k = [np.any((x >= sit_final[:, 0]) & (y <= sit_final[:, 1])) for x, y in zip(a, b)]
        return a[k], b[k]
    hon, hoff = within(hon, hoff)
    lon, loff = within(lon, loff)
    keep = []
    for x in hon:
        d = x - loff
        j = np.flatnonzero((d >= 0) & (d <= 0.5))
        keep.append(len(j) == 1 and (loff[j[0]] - lon[j[0]]) >= p["before_arousal_on"])
    return hon[np.array(keep, bool)] if len(hon) else hon


def locomotion_onsets(s, min_sit=10, min_run=5):
    """The dandiset's WheelActivation onsets inside the imaging period, as combineData_spont uses."""
    wa = s["wheel_activation"]
    if wa is None:
        return np.array([])
    on = wa[:, 0]
    return on[(on > s["t"][0] + min_sit) & (on < s["t"][-1] - min_run)]


def event_traces(x, t, events, pre, post):
    """Trials (events x frames x parcels) of frames from `pre` s before to `post` s after each event."""
    n = int(round((pre + post) * FS_IMAGING))
    out = []
    for e in events:
        i0 = np.searchsorted(t, e - pre)
        if i0 + n <= len(t) and abs(t[i0] - (e - pre)) < 0.1:
            out.append(x[i0:i0 + n])
    return np.array(out)


# --- correlations ----------------------------------------------------------------------------------

def max_crosscorr(a, b, lags=5):
    """calcMaxCrossCorr.m: for rows of a (P x T) and b (Q x T), the MATLAB crosscorr value of largest
    magnitude within ±lags frames."""
    T = a.shape[1]
    a = a - a.mean(1, keepdims=True)
    b = b - b.mean(1, keepdims=True)
    a = a / np.sqrt((a ** 2).mean(1, keepdims=True))
    b = b / np.sqrt((b ** 2).mean(1, keepdims=True))
    cs = []
    for k in range(-lags, lags + 1):
        if k >= 0:
            cs.append(a[:, : T - k] @ b[:, k:].T / T)
        else:
            cs.append(a[:, -k:] @ b[:, : T + k].T / T)
    cs = np.stack(cs)
    idx = np.abs(cs).argmax(0)
    return np.take_along_axis(cs, idx[None], 0)[0]


def epoch_data(x, t, on, off):
    return x[(t > on) & (t < off)].T


def permutation_test(z1, z2, n_perm, rng):
    """Stratified permutation test (permuteEpochLabels.m, permutePval.m).

    z1, z2: per mouse, arrays (epochs x values) of Fisher z for the two states (equal numbers per
    mouse). Returns the observed mean difference over mice and two-sided p-values."""
    obs = np.mean([a.mean(0) - b.mean(0) for a, b in zip(z1, z2)], axis=0)
    perm = np.zeros((n_perm, len(obs)))
    for a, b in zip(z1, z2):
        comb = np.concatenate([a, b])
        m = len(a)
        w = np.zeros((n_perm, 2 * m))
        for i in range(n_perm):
            lab = rng.permutation(2 * m)
            w[i, lab[:m]] = 1.0 / m
            w[i, lab[m:]] = -1.0 / len(b)
        perm += w @ comb
    perm /= len(z1)
    p = (np.abs(perm) >= np.abs(obs)).mean(0)
    p[p == 0] = 1.0 / n_perm
    return obs, p


# --- regression (ridgeMML) -------------------------------------------------------------------------

LAMBDAS = np.logspace(-3, 6, 91)


def ridge_mml_fit(X, Y):
    """Ridge with the penalty per output chosen by maximising the marginal likelihood over a grid.
    X, Y centred. Returns weights (p x q)."""
    U, S, Vt = np.linalg.svd(X, full_matrices=False)
    d = S ** 2
    Z = U.T @ Y
    yy = (Y ** 2).sum(0)
    n = X.shape[0]
    best = None
    for lam in LAMBDAS:
        quad = yy - ((d / (d + lam))[:, None] * Z ** 2).sum(0)
        nll = n * np.log(quad) + np.log1p(d / lam).sum()
        best = (nll, np.full(Y.shape[1], lam)) if best is None else (
            np.minimum(best[0], nll), np.where(nll < best[0], lam, best[1]))
    lam = best[1]
    return Vt.T @ ((S[:, None] / (d[:, None] + lam[None])) * Z)


def cv_r2(X, Y, folds=10):
    """Ten-fold cross-validated R2 over contiguous blocks, averaged over folds (per output). The
    predictors are centred and scaled to unit SD, and the outputs centred, with the training folds'
    statistics only."""
    n = X.shape[0]
    edges = np.linspace(0, n, folds + 1).astype(int)
    r2 = []
    for k in range(folds):
        test = np.zeros(n, bool)
        test[edges[k]:edges[k + 1]] = True
        mx, my = X[~test].mean(0), Y[~test].mean(0)
        sx = X[~test].std(0)
        sx[sx == 0] = 1.0
        W = ridge_mml_fit((X[~test] - mx) / sx, Y[~test] - my)
        pred = ((X[test] - mx) / sx) @ W + my
        yt = Y[test]
        r2.append(1 - ((yt - pred) ** 2).sum(0) / ((yt - yt.mean(0)) ** 2).sum(0))
    return np.mean(r2, axis=0)
