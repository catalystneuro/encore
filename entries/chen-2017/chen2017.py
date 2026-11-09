"""Loading and selectivity measures for dandiset 000015 (Chen, Li, Daie & Svoboda 2017, Neuron).

The dandiset holds two-photon imaging of 105 image planes in left ALM and MM of six mice during the
object location task with a delay, one NWB file per plane, each deposited twice. Files are streamed
from the archive at a pinned version; nothing is written to disk.

Where each parameter comes from (the claims file is claims/000015/10.1016-j.neuron.2017.05.005.yaml;
its conventions T, M, A, D, B and O are in its opening comment):

- NEUROPIL_R = 0.7: F = F_roi - 0.7 F_neuropil (claims file header, from the STAR Methods).
- Trial start is the `sample` event (pole movement onset). The claims file places the go cue 4.2 s
  after trial start; in the data the go cue is 4.2 s after `sample` on every analysed trial, while
  the trial table's start_time is 0.623 s earlier (checked in the notebook).
- WINDOW = (-0.8, 9.2) s from trial start: 5 s before to 5 s after the go cue (convention T).
- BASELINE = (-0.5, 0) s: F0 is the mean F over the 0.5 s before trial start (convention T).
- Trial types CR, CL, ER, EL from instruction (right = posterior, left = anterior) and outcome (hit =
  correct, miss = error); early-lick trials and trials with no response are left out (convention T).
- Time bins: T1, the frames as acquired, taken on one grid at the majority frame rate (FRAME_HZ);
  each grid time takes the nearest frame, so planes at 14.2 Hz are sampled to the same times. T2,
  traces linearly interpolated to 66.7 ms bins. The common grid and the interpolation are standard
  choices for detail the claims file leaves open (it names T1 and T2 only).
- The test is a 3-way ANOVA, main effects only (convention M), with each factor's sum of squares
  adjusted for the other two (MATLAB anovan's default type 3, the same as type 2 for a model with
  main effects only); p < ALPHA = 0.01.
- Coefficients from trial-type means: alpha = (CR - CL + ER - EL)/2, beta = (CR - CL - ER + EL)/2,
  gamma = (CR + CL - ER - EL)/2 (convention M).
- Hierarchical bootstrap over animals, planes and cells with replacement (convention B); the number
  of resamples (1000) is the claims file's standard choice.
- Onset (convention O): the threshold is the baseline mean plus 6 SD of the baseline bins; baselines
  O1 (all bins before trial start in the window) and O2 (the 0.5 s before trial start); rules S1 (the
  first bin at or after trial start above the threshold) and S2 (the first bin from which the curve
  stays above it up to the go cue).
- dF/F is computed as the Methods' formula gives it, also where F0 <= 0 (convention T, reading V1);
  the notebook leaves out the ROIs concerned as the check V2.
- Tagged units of Li et al. (2015) in dandiset 000010 (claim ephys-pt-it-onset-not-detected): 400 ms
  windows in 100 ms steps, trials of the four types without photostimulation and without an early
  lick, time from the sample event (the criterion's readings 1 and 2). Matching trials to their
  sample event (0.5 to 0.7 s after start_time), counting a unit only in the trials within its
  observation intervals, and detecting the light from laser pulses or photostim events are readings
  of the data, shown in the notebook.
"""

from __future__ import annotations

import concurrent.futures as cf
import time

import h5py
import numpy as np
import remfile
import requests
from scipy import stats

DANDISET_ID = "000015"
DANDISET_VERSION = "0.220126.1914"
API = "https://api.dandiarchive.org/api"

NEUROPIL_R = 0.7
WINDOW = (-0.8, 9.2)
BASELINE = (-0.5, 0.0)
SAMPLE_END = 1.2
GO = 4.2
FRAME_HZ = 13.9529
T2_BIN = 0.0667
ALPHA = 0.01
TYPES = ("CR", "CL", "ER", "EL")
FACTORS = ("alpha", "beta", "gamma")   # object location, lick direction, outcome

# Trial-type codes on the three factors: posterior (CR, ER), lick right (CR, EL), correct (CR, CL).
DESIGN = {"CR": (1, 1, 1), "CL": (0, 0, 1), "ER": (1, 0, 0), "EL": (0, 1, 0)}


def grid(binning: str) -> np.ndarray:
    """Bin times from trial start (s) for binning T1 or T2."""
    step = 1.0 / FRAME_HZ if binning == "T1" else T2_BIN
    k0 = int(np.ceil(WINDOW[0] / step - 1e-9))
    k1 = int(np.floor(WINDOW[1] / step + 1e-9))
    return np.arange(k0, k1 + 1) * step


def list_assets(version: str = DANDISET_VERSION) -> list[dict]:
    """Every asset of the version, with its archive metadata (digest, size)."""
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{version}/assets/?page_size=1000&metadata=1"
    out = []
    while url:
        r = requests.get(url, timeout=120).json()
        out += r["results"]
        url = r.get("next")
    return sorted(out, key=lambda a: a["path"])


def _open(asset_id: str) -> h5py.File:
    for attempt in range(5):
        try:
            url = requests.head(f"{API}/assets/{asset_id}/download/", allow_redirects=True, timeout=120).url
            return h5py.File(remfile.File(url), "r")
        except Exception:
            if attempt == 4:
                raise
            time.sleep(5 * (attempt + 1))


def _text(values) -> np.ndarray:
    return np.array([v.decode() if isinstance(v, bytes) else str(v) for v in values])


def text_values(f: h5py.File) -> dict:
    """Every text value of a file outside the NWB specification: string datasets of at most 10
    values and string attributes, by path ('path@attribute' for attributes)."""
    out = {}

    def text(v):
        if isinstance(v, bytes):
            return v.decode(errors="replace")
        if isinstance(v, str):
            return v
        if isinstance(v, np.ndarray) and v.dtype.kind in "OSU" and v.size <= 10:
            return " | ".join(text(x) or "" for x in v.ravel())
        return None

    def visit(name, obj):
        if name.startswith("specifications"):
            return
        for k, v in obj.attrs.items():
            if k not in ("namespace", "neurodata_type", "object_id") and text(v) is not None:
                out[f"{name}@{k}"] = text(v)
        if isinstance(obj, h5py.Dataset) and obj.dtype.kind in "OSU" and obj.size <= 10:
            out[name] = text(obj[()]) if obj.shape == () else text(np.asarray(obj[()]))
    f.visititems(visit)
    return out


def compare_files(a: dict, b: dict) -> tuple[int, list[str]]:
    """Read every dataset of two files in full; return how many there are and which differ."""
    fa, fb = _open(a["asset_id"]), _open(b["asset_id"])
    names, differ = [], []
    fa.visititems(lambda n, o: names.append(n) if isinstance(o, h5py.Dataset) and not n.startswith("specifications") else None)
    for n in names:
        if n not in fb or not np.array_equal(np.asarray(fa[n][()]), np.asarray(fb[n][()])):
            differ.append(n)
    fa.close()
    fb.close()
    return len(names), differ


def read_header(asset: dict) -> dict:
    """The small parts of a file: metadata, every text value, trial table, events, ROI table, and the
    first and last 200 frames of the traces, used to tell copies of the same plane apart."""
    f = _open(asset["asset_id"])
    ip = f["general/optophysiology/ImagingPlane"]
    t = f["intervals/trials"]
    be = f["processing/behavior/BehavioralEvents"]
    ps = f["processing/ophys/ImageSegmentation/PlaneSegmentation"]
    rr = f["processing/ophys/Fluorescence/RoiResponseSeries"]
    npl = f["processing/ophys/Fluorescence/NeuropilResponseSeries"]
    h = {
        "path": asset["path"], "asset_id": asset["asset_id"], "size": asset["size"],
        "sha256": asset["metadata"]["digest"].get("dandi:sha2-256"),
        "identifier": f["identifier"][()].decode(),
        "subject": f["general/subject/subject_id"][()].decode(),
        "session": asset["path"].split("_ses-")[1].split("_")[0],
        "experiment_description": f["general/experiment_description"][()].decode(),
        "location": ip["location"][()].decode(),
        "rate": float(ip["imaging_rate"][()]),
        "rate_attr": float(rr["starting_time"].attrs["rate"]),
        "starting_time": float(rr["starting_time"][()]),
        "n_frames": rr["data"].shape[0], "n_rois": rr["data"].shape[1],
        "rois_unit": rr["data"].attrs.get("unit"),
        "trial_start": t["start_time"][()], "trial_stop": t["stop_time"][()],
        "instruction": _text(t["trial_instruction"][()]), "outcome": _text(t["outcome"][()]),
        "early_lick": t["early_lick"][()].astype(bool), "task": _text(t["task"][()]),
        "sample": be["sample/timestamps"][()], "delay": be["delay/timestamps"][()],
        "go": be["go/timestamps"][()],
        "cell_type": _text(ps["cell_type"][()]), "included": ps["included"][()].astype(bool),
        "roi_ids": ps["id"][()], "rr_rois": rr["rois"][()],
        "probe": np.concatenate([rr["data"][:200].ravel(), npl["data"][:200].ravel(),
                                 rr["data"][-200:].ravel(), npl["data"][-200:].ravel()]),
        "behavior_events": sorted(be.keys()),
        "texts": text_values(f),
    }
    h["area"] = "ALM" if h["experiment_description"].endswith("left_alm") else (
        "MM" if h["experiment_description"].endswith("left_vm1") else "?")
    f.close()
    return h


def read_headers(assets: list[dict], workers: int = 24) -> list[dict]:
    with cf.ThreadPoolExecutor(workers) as ex:
        return list(ex.map(read_header, assets))


def content_key(h: dict) -> tuple:
    """What two copies of one plane share: subject, session, frame and ROI counts, the trial table, and
    the first and last 200 frames of both trace series."""
    return (h["subject"], h["session"], h["n_frames"], h["n_rois"], h["trial_start"].tobytes(),
            h["outcome"].tobytes(), h["probe"].tobytes())


def trial_types(h: dict) -> np.ndarray:
    """CR, CL, ER, EL per trial, or '' for trials outside the four types (early lick, no response)."""
    tt = np.full(len(h["outcome"]), "", dtype=object)
    ok = ~h["early_lick"]
    right, left = h["instruction"] == "right", h["instruction"] == "left"
    hit, miss = h["outcome"] == "hit", h["outcome"] == "miss"
    tt[ok & right & hit] = "CR"
    tt[ok & left & hit] = "CL"
    tt[ok & right & miss] = "ER"
    tt[ok & left & miss] = "EL"
    return tt


def read_traces(h: dict) -> np.ndarray:
    """Neuropil-corrected fluorescence F (frames x ROIs), float32."""
    f = _open(h["asset_id"])
    roi = f["processing/ophys/Fluorescence/RoiResponseSeries/data"][()]
    npl = f["processing/ophys/Fluorescence/NeuropilResponseSeries/data"][()]
    f.close()
    return (roi - NEUROPIL_R * npl).astype(np.float32)


def dff_trials(h: dict, F: np.ndarray, binning: str, start_event: str = "sample"):
    """dF/F per analysed trial on the bin grid: (trials, ROIs, bins), the trial types, the F0 values
    (trials, ROIs), and the number of analysed trials dropped because the window leaves the recording."""
    tt = trial_types(h)
    keep = np.flatnonzero(tt != "")
    starts = h[start_event][keep] if start_event != "start_time" else h["trial_start"][keep]
    rate, t0 = h["rate"], h["starting_time"]
    n = F.shape[0]
    g = grid(binning)
    first = np.floor((starts + WINDOW[0] - t0) * rate) - 1
    last = np.ceil((starts + WINDOW[1] - t0) * rate) + 1
    inside = (first >= 0) & (last < n)
    keep, starts = keep[inside], starts[inside]
    frame_t = t0 + np.arange(n) / rate
    out = np.empty((len(keep), F.shape[1], len(g)), dtype=np.float32)
    f0s = np.empty((len(keep), F.shape[1]), dtype=np.float32)
    for i, s in enumerate(starts):
        b0 = int(np.ceil((s + BASELINE[0] - t0) * rate - 1e-9))
        b1 = int(np.ceil((s + BASELINE[1] - t0) * rate - 1e-9))
        f0 = F[b0:b1].mean(0)
        if binning == "T1":
            idx = np.rint((s + g - t0) * rate).astype(int)
            tr = F[idx]
        else:
            lo = int(first[inside][i])
            hi = int(last[inside][i]) + 1
            seg_t = frame_t[lo:hi]
            seg = F[lo:hi]
            x = s + g
            j = np.clip(np.searchsorted(seg_t, x) - 1, 0, len(seg_t) - 2)
            w = ((x - seg_t[j]) / (seg_t[j + 1] - seg_t[j])).astype(np.float32)
            tr = seg[j] * (1 - w)[:, None] + seg[j + 1] * w[:, None]
        out[i] = ((tr - f0) / f0).T
        f0s[i] = f0
    return out, tt[keep], f0s, int((~inside).sum())


def anova3(Y: np.ndarray, types: np.ndarray):
    """3-way ANOVA, main effects only, per column of Y (trials x M). Returns p (3, M) for object
    location, lick direction and outcome, and the coefficients (3, M) from trial-type means."""
    codes = np.array([DESIGN[t] for t in types], dtype=float)
    n = len(types)
    X = np.column_stack([np.ones(n), codes])
    Y = Y.astype(np.float64)
    yy = (Y ** 2).sum(0)

    def rss(Xm):
        q, _ = np.linalg.qr(Xm)
        proj = q.T @ Y
        return yy - (proj ** 2).sum(0)

    full = rss(X)
    dfe = n - X.shape[1]
    p = np.empty((3, Y.shape[1]))
    for k in range(3):
        red = rss(np.delete(X, k + 1, axis=1))
        with np.errstate(divide="ignore", invalid="ignore"):
            Fst = (red - full) / (full / dfe)
        p[k] = stats.f.sf(Fst, 1, dfe)
    p[~np.isfinite(p)] = 1.0
    means = {t: Y[types == t].mean(0) for t in TYPES}
    cr, cl, er, el = (means[t] for t in TYPES)
    coef = np.stack([(cr - cl + er - el) / 2, (cr - cl - er + el) / 2, (cr + cl - er - el) / 2])
    return p, coef


def process_plane(h: dict, binnings=("T1", "T2"), shuffle_seed: int | None = None,
                  start_events=("sample",)) -> dict:
    """Stream one plane and compute, per ROI and bin, the ANOVA p-values, the coefficients and the
    mean dF/F over analysed trials, for each binning; with shuffle_seed, also with the trial types
    permuted (a null for the clock check, T1 only)."""
    F = read_traces(h)
    out = {"n_frames": F.shape[0], "n_rois": F.shape[1]}
    for start_event in start_events:
        for b in binnings:
            if start_event != "sample" and b != "T1":
                continue
            D, types, f0, dropped = dff_trials(h, F, b, start_event)
            key = b if start_event == "sample" else f"{b}_{start_event}"
            counts = {t: int((types == t).sum()) for t in TYPES}
            res = {"counts": counts, "dropped_edge": dropped, "n_trials": len(types)}
            if min(counts.values()) >= 1 and len(types) > 4:
                nt, nr, nb = D.shape
                p, coef = anova3(D.reshape(nt, nr * nb), types)
                res["p"] = p.reshape(3, nr, nb).transpose(1, 2, 0).astype(np.float32)
                res["coef"] = coef.reshape(3, nr, nb).transpose(1, 2, 0).astype(np.float32)
                if shuffle_seed is not None and b == "T1" and start_event == "sample":
                    rng = np.random.default_rng(shuffle_seed)
                    ps, _ = anova3(D.reshape(nt, nr * nb), rng.permutation(types))
                    res["p_shuffled"] = ps.reshape(3, nr, nb).transpose(1, 2, 0).astype(np.float32)
            res["mean_dff"] = D.mean(0).astype(np.float32)
            if b == "T1" and start_event == "sample":
                res["f0_min"] = f0.min(0)
                res["f0_median"] = np.median(f0, 0)
                res["f0_nonpositive"] = (f0 <= 0).sum(0)
                res["dff_abs_max"] = np.abs(D).max(axis=(0, 2))
            out[key] = res
    return out


def process_planes(headers: list[dict], workers: int = 8, **kw) -> list[dict]:
    with cf.ThreadPoolExecutor(workers) as ex:
        return list(ex.map(lambda h: process_plane(h, **kw), headers))


def classify(p: np.ndarray) -> dict:
    """Per ROI and bin: significant factors (p < 0.01), trial-type selective (any), purely selective
    for one factor, and mixed (more than one) (convention M)."""
    sig = p < ALPHA
    n = sig.sum(-1)
    return {"sig": sig, "any": n >= 1, "mixed": n >= 2,
            "pure": sig & (n == 1)[..., None]}


def onset(curve: np.ndarray, times: np.ndarray, baseline: str = "O1", n_sd: float = 6.0,
          rule: str = "S1", go: float = GO, base: np.ndarray | None = None, search_end: float | None = None):
    """Onset of a curve by convention O: the threshold is the baseline mean plus n_sd baseline SDs.
    Baseline O1: all bins before trial start; O2: the 0.5 s before trial start; or a mask `base`
    given by the caller (the spike-count windows of the Li et al. units). Rule S1: the first bin at or
    after trial start above the threshold (up to search_end if given); S2: the first bin at or after
    trial start from which every bin before the go cue is above it. NaN when there is none."""
    if base is None:
        base = times < 0 if baseline == "O1" else (times >= BASELINE[0] - 1e-9) & (times < 0)
    mu, sd = curve[base].mean(), curve[base].std(ddof=1)
    above = curve > mu + n_sd * sd
    if rule == "S1":
        ok = (times >= 0) & above
        if search_end is not None:
            ok &= times < search_end
        idx = np.flatnonzero(ok)
        return times[idx[0]] if len(idx) else np.nan
    span = np.flatnonzero((times >= 0) & (times < go))
    stays = np.flip(np.cumprod(np.flip(above[span]))).astype(bool)
    return times[span[np.argmax(stays)]] if stays.any() else np.nan


def epochs(times: np.ndarray) -> dict:
    """Bin masks for the task epochs, from trial start: before the trial, sample (0 to 1.2 s), delay
    (1.2 to 4.2 s) and response (from the go cue at 4.2 s) (claims file header)."""
    return {"pre": times < 0, "sample": (times >= 0) & (times < SAMPLE_END),
            "delay": (times >= SAMPLE_END) & (times < GO), "response": times >= GO}


def assemble(headers: list[dict], results: list[dict], binning: str) -> dict:
    """Stack the per-plane results into arrays over all ROIs: p-values, coefficients (raw, and with
    non-significant factors set to 0), the selectivity classes, and the mean dF/F."""
    p = np.concatenate([r[binning]["p"] for r in results])
    coef = np.concatenate([r[binning]["coef"] for r in results])
    cl = classify(p)
    out = {"times": grid(binning), "p": p, "coef": coef, "coef_sig": np.where(cl["sig"], coef, 0),
           "mean_dff": np.concatenate([r[binning]["mean_dff"] for r in results]), **cl}
    if "p_shuffled" in results[0][binning]:
        out["shuffled"] = classify(np.concatenate([r[binning]["p_shuffled"] for r in results]))
    out["epochs"] = epochs(out["times"])
    return out


def ss_between(X: np.ndarray, labels: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Per bin, the sum of squares between the groups of `labels` (SSB) and the total sum of squares
    (SST) over cells, for X (cells x bins) (Methods, variance of neuronal selectivity)."""
    mu = X.mean(0)
    sst = ((X - mu) ** 2).sum(0)
    ssb = np.zeros(X.shape[1])
    for g in np.unique(labels):
        m = labels == g
        ssb += m.sum() * (X[m].mean(0) - mu) ** 2
    return ssb, sst


def joint_resample(animal: np.ndarray, plane: np.ndarray, groups: list[np.ndarray],
                   rng: np.random.Generator, hierarchical: bool = True) -> list[np.ndarray]:
    """One bootstrap resample of several groups of cells at once. Hierarchical (H1, convention B):
    animals, then planes within each animal, drawn once for all groups, then cells of each group
    within each plane. Over cells (H2): cells of each group drawn independently."""
    if not hierarchical:
        out = []
        for g in groups:
            c = np.flatnonzero(g)
            out.append(c[rng.integers(0, len(c), len(c))])
        return out
    anyg = np.any(groups, axis=0)
    animals = np.unique(animal[anyg])
    out = [[] for _ in groups]
    for a in rng.choice(animals, len(animals)):
        planes = np.unique(plane[anyg & (animal == a)])
        for pl in rng.choice(planes, len(planes)):
            for k, g in enumerate(groups):
                c = np.flatnonzero(g & (plane == pl))
                if len(c):
                    out[k].append(c[rng.integers(0, len(c), len(c))])
    return [np.concatenate(o) if o else np.array([], dtype=int) for o in out]


def li2015_tagged_units(version: str = "0.220126.1905", workers: int = 16) -> list[dict]:
    """Cell types of the units in dandiset 000010 (Li et al. 2015), the electrophysiology the paper
    compares with; only the units table's cell_type column is read."""
    url = f"{API}/dandisets/000010/versions/{version}/assets/?page_size=1000"
    assets = requests.get(url, timeout=120).json()["results"]

    def one(a):
        f = _open(a["asset_id"])
        row = {"path": a["path"], "asset_id": a["asset_id"], "genotype": f["general/subject/genotype"][()].decode()
               if "genotype" in f["general/subject"] else ""}
        row["cell_type"] = _text(f["units/cell_type"][()]) if "units" in f else np.array([])
        f.close()
        return row

    with cf.ThreadPoolExecutor(workers) as ex:
        return list(ex.map(one, sorted(assets, key=lambda a: a["path"])))


# Tagged units of Li et al. (2015), dandiset 000010 (claim ephys-pt-it-onset-not-detected). The
# criterion's readings: spike counts in 400 ms windows in 100 ms steps (EPH_WIN, EPH_STEP), each
# window placed at its centre; trials of the four types without photostimulation, early-lick trials
# excluded by the early_lick column; time from the sample event (pole movement onset).
EPH_WIN = 0.4
EPH_STEP = 0.1
# A trial is matched to the sample event that falls 0.5 to 0.7 s after its start_time; in these files
# it falls 0.57 s after it (a reading of the data, checked in the notebook).
LI_MATCH = (0.5, 0.7)


def _read_contiguous(url: str, ds, parts: int = 8) -> np.ndarray:
    """All values of an uncompressed, contiguous dataset, read with parallel HTTP range requests (a
    standard choice for speed that cannot change a result)."""
    off, n, dt = ds.id.get_offset(), ds.shape[0], ds.dtype
    if off is None or ds.compression or ds.chunks:
        return ds[()]
    edges = off + np.linspace(0, n, parts + 1).astype(int) * dt.itemsize

    def get(i):
        r = requests.get(url, headers={"Range": f"bytes={edges[i]}-{edges[i + 1] - 1}"}, timeout=300)
        r.raise_for_status()
        return r.content
    with cf.ThreadPoolExecutor(parts) as ex:
        buf = b"".join(ex.map(get, range(parts)))
    return np.frombuffer(buf, dt.newbyteorder("<") if dt.byteorder == "=" else dt)


def li2015_session(row: dict) -> dict:
    """One session of dandiset 000010 with tagged units: its trial table with the matched sample and
    go events, photostimulation per trial, and the spike times and observation intervals of the PT and
    IT units. A trial counts as photostimulated when a laser pulse (a rising edge above half the
    series maximum, in any laser_power series under stimulus/presentation) or a photostim_start_time
    event falls between its start and stop."""
    for attempt in range(5):
        try:
            url = requests.head(f"{API}/assets/{row['asset_id']}/download/", allow_redirects=True, timeout=120).url
            f = h5py.File(remfile.File(url), "r")
            break
        except Exception:
            if attempt == 4:
                raise
            time.sleep(5 * (attempt + 1))
    t = f["intervals/trials"]
    start, stop = t["start_time"][()], t["stop_time"][()]
    be = f["acquisition/BehavioralEvents"]
    ev = {k: np.sort(be[k]["timestamps"][()]) for k in be}
    s = ev["sample"]
    j = np.clip(np.searchsorted(s, start + LI_MATCH[0]), 0, len(s) - 1)
    matched = (s[j] >= start + LI_MATCH[0]) & (s[j] <= start + LI_MATCH[1])
    sample = np.where(matched, s[j], np.nan)
    nxt = np.append(s[1:], np.inf)[j]
    g = ev["go"]
    k = np.clip(np.searchsorted(g, np.nan_to_num(sample, nan=-1.0)), 0, len(g) - 1)
    go = np.where(matched & (g[k] >= sample) & (g[k] < nxt), g[k], np.nan)

    def in_trial(times):
        m = np.zeros(len(start), bool)
        i = np.searchsorted(start, times, side="right") - 1
        ok = (i >= 0) & (times <= stop[np.clip(i, 0, None)])
        m[i[ok]] = True
        return m, int((~ok).sum())

    pulses = []
    sp = f["stimulus/presentation"] if "stimulus/presentation" in f else {}
    for name in sp:
        if name.endswith("laser_power"):
            d = _read_contiguous(url, sp[name]["data"])
            ts = _read_contiguous(url, sp[name]["timestamps"])
            on = d > 0.5 * d.max()
            pulses.append(ts[np.flatnonzero(on[1:] & ~on[:-1]) + 1])
    laser, laser_out = in_trial(np.concatenate(pulses) if pulses else np.array([]))
    pst = ev.get("photostim_start_time", np.array([]))
    event, event_out = in_trial(pst)
    u = f["units"]
    ct = _text(u["cell_type"][()])
    si, oi_idx = u["spike_times_index"][()], u["obs_intervals_index"][()]
    oi = u["obs_intervals"][()]
    units = []
    for n in np.flatnonzero(np.isin(ct, ["PT", "IT"])):
        a, b = (si[n - 1] if n else 0), si[n]
        c, d = (oi_idx[n - 1] if n else 0), oi_idx[n]
        units.append({"label": ct[n], "index": int(n), "spikes": u["spike_times"][a:b], "obs": oi[c:d]})
    out = {"path": row["path"], "subject": f["general/subject/subject_id"][()].decode(), "genotype": row["genotype"],
           "start": start, "stop": stop, "sample": sample, "go": go,
           "instruction": _text(t["trial_instruction"][()]), "outcome": _text(t["outcome"][()]),
           "early": _text(t["early_lick"][()]), "light_laser": laser, "light_event": event,
           "laser_series": len(pulses), "pulses_outside": laser_out, "events_outside": event_out, "units": units}
    f.close()
    return out


def li2015_sessions(rows: list[dict], workers: int = 8) -> list[dict]:
    with cf.ThreadPoolExecutor(workers) as ex:
        return list(ex.map(li2015_session, rows))


def li2015_types(sess: dict) -> np.ndarray:
    """CR, CL, ER, EL per trial (right = posterior, lick right; hit = correct), or '' for trials
    outside the four types, with an early lick, with photostimulation, or with no matched sample event."""
    tt = np.full(len(sess["start"]), "", dtype=object)
    ok = (sess["early"] == "no early") & ~(sess["light_laser"] | sess["light_event"]) & np.isfinite(sess["sample"])
    right, left = sess["instruction"] == "right", sess["instruction"] == "left"
    hit, miss = sess["outcome"] == "hit", sess["outcome"] == "miss"
    tt[ok & right & hit] = "CR"
    tt[ok & left & hit] = "CL"
    tt[ok & right & miss] = "ER"
    tt[ok & left & miss] = "EL"
    return tt


def li2015_unit_counts(sess: dict, unit: dict, centres: np.ndarray):
    """Spike counts of one unit in 400 ms windows centred at `centres` (s from the sample event), for
    the trials of the four types (li2015_types) that lie within the unit's observation intervals.
    Returns counts (trials x windows) and the trial types."""
    tt = li2015_types(sess)
    obs = unit["obs"]
    inside = np.array([np.any((obs[:, 0] <= a + 1e-6) & (obs[:, 1] >= b - 1e-6)) for a, b in zip(sess["start"], sess["stop"])])
    keep = np.flatnonzero((tt != "") & inside)
    lo = sess["sample"][keep][:, None] + centres[None, :] - EPH_WIN / 2
    sp = unit["spikes"]
    counts = np.searchsorted(sp, lo + EPH_WIN) - np.searchsorted(sp, lo)
    return counts.astype(float), tt[keep], keep
