"""Loading and measures for dandiset 001530 (Ghaderi, Crochet & Petersen 2026).

Paper: "Contextual gating of whisker-evoked responses by frontal cortex supports flexible
decision making", Nature Communications 17, 5982, doi:10.1038/s41467-026-73622-y.

The dandiset holds 35 Neuropixels sessions (`*-processed-behavior.nwb`: trials, units with
spike times and Allen CCF labels, DeepLabCut traces of whisker, jaw, tongue and snout, the
piezo lick trace), the same sessions again with raw voltage (`*-processed-behavior-raw.nwb`,
not read here) with their videos, and 91 optogenetic sessions (`*-opto-behavior.nwb`, trials
only). Files are streamed from the archive at the pinned version; nothing is written to disk.

Where the parameters come from. "Code" is the paper's code in its Zenodo record
doi:10.5281/zenodo.17973874 (the same files are on GitHub,
LSENS-BMI-EPFL/Ghaderi_et_al_NCOMMS_2026 at commit 20cf10c7b95069c12f762b7dd89817beedcc382f),
cited by file name as the claims file does.

- Time zero is the trial start (`start_time`, the auditory cue or its expected time); the
  whisker stimulus is at 1.0 s. Spike counts are binned from -1 to 2 s (code, psth_10ms.m and
  PSTH_Simple.m: histcounts with edges start_time + (-1:0.01:2)); bin i holds [-1 + i w,
  -1 + (i + 1) w). The code labels a bin by its right edge.
- Trial types 1 to 5 from the NWB `trial_type` (Go-tone Whisker, Go-tone No-Whisker, Nogo-tone
  Whisker, Nogo-tone No-Whisker, No-tone Whisker; code, trial_typeMaker.m). Hit is type 1 with
  a lick, correct rejections types 2 to 5 without; early-lick trials are excluded (Methods,
  Behavioral data analysis, "Only completed trials ... were included").
- Movement traces (code, psth_10ms.m and PSTHBehavior.m): whisker speed is the absolute
  frame-to-frame change of the C2 whisker angle; jaw movement the distance of the jaw tip from
  the mode of its x and y over the session; tongue movement the distance of the tongue tip from
  the jaw mode, values above 20 times the mean set to NaN. Each is averaged in 10 ms windows
  from the video frame nearest the trial start, at 200 frames/s (100 in PG019; code).
- Quiet trials (Methods, Quantification of orofacial movements, and code,
  nwb_findQuietTrial.m): for whisker speed and jaw movement, the mean over the bins of 0.8 to
  1.0 s at or below the median plus one MAD of the per-trial means over -1 to 0 s, over all
  trials of the session. The Methods say median absolute deviation (`MAD = "median"`, used for
  outcomes); MATLAB's mad() in the code defaults to the mean absolute deviation (`"mean"`,
  shown as a variant), as the claims file's header says.
- Areas (code, Neuronal_data_10ms.m with data_helpers/Area_list.mat): a unit belongs to an
  area when its probe's `location` is that area and its own `ccf_location` is one of the
  area's CCF labels. Area_list.mat is read from the Zenodo record (`area_list()`).
"""

from __future__ import annotations

import io
import json
import re
import struct
import urllib.request
import zipfile
from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache

import h5py
import numpy as np
import remfile

DANDISET_ID = "001530"
DANDISET_VERSION = "0.260605.0601"
API = "https://api.dandiarchive.org/api"
ZENODO_ZIP = ("https://zenodo.org/api/records/17973874/files/"
              "2026_Ghaderi_NCOMMS_Zenodo_data_code.zip/content")

AREAS = ["A1", "wS1", "wS2", "wM2", "ALM"]
OPTO_AREAS = ["A1", "wS1", "wS2", "wM2", "ALM", "fpS1"]
TRIAL_NAMES = {1: "Go-tone Whisker", 2: "Go-tone No-Whisker", 3: "Nogo-tone Whisker",
               4: "Nogo-tone No-Whisker", 5: "No-tone Whisker"}

PRE, POST = -1.0, 2.0
W10 = 0.01
N10 = 300
# 5 ms bins around the whisker stimulus, 0.95 to 1.10 s (code, psth_5ms.m bins this range
# inside -1 to 2 s; only this part is kept, as the 5 ms analyses use no other times).
W5 = 0.005
T5_START, N5 = 0.95, 30


def _json(url):
    with urllib.request.urlopen(url, timeout=120) as r:
        return json.load(r)


@lru_cache(maxsize=None)
def assets():
    """Path, size and asset id of every asset of the pinned version."""
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/?page_size=1000"
    out = []
    while url:
        page = _json(url)
        out += [(a["path"], a["size"], a["asset_id"]) for a in page["results"]]
        url = page["next"]
    return out


def s3_url(asset_id):
    meta = _json(f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/{asset_id}/")
    return [u for u in meta["contentUrl"] if "s3" in u][0]


def open_nwb(asset_id):
    return h5py.File(remfile.File(s3_url(asset_id)), "r")


def ephys_assets():
    return sorted([a for a in assets() if a[0].endswith("-processed-behavior.nwb")])


def opto_assets():
    return sorted([a for a in assets() if a[0].endswith("-opto-behavior.nwb")])


def _str(a):
    return np.array([x.decode() if isinstance(x, bytes) else str(x) for x in a], dtype=object)


# ---------------------------------------------------------------- outside input: Area_list.mat

@lru_cache(maxsize=None)
def zenodo_member(name):
    """Bytes of one member of the paper's Zenodo zip, read by range requests."""
    import fsspec
    with fsspec.open(ZENODO_ZIP, block_size=2 ** 20).open() as f:
        with zipfile.ZipFile(f) as z:
            return z.read(name)


@lru_cache(maxsize=None)
def area_list():
    """The CCF labels of each area, from data_helpers/Area_list.mat (Zenodo).

    The file holds a struct of MATLAB string arrays. MATLAB stores them in an opaque
    subsystem; each array is written as [2, n, 1] (dimensions), n lengths, then the
    characters in UTF-16. The five arrays come in the struct's field order.
    """
    import scipy.io
    raw = zenodo_member("data_helpers/Area_list.mat")
    m = scipy.io.loadmat(io.BytesIO(raw))
    fields = list(m["area_list"].dtype.names)
    buf = m["__function_workspace__"].tobytes()
    out, pos = {}, 0
    pattern = re.compile(rb"\x02\x00\x00\x00\x00\x00\x00\x00(.)\x00\x00\x00\x00\x00\x00\x00"
                         rb"\x01\x00\x00\x00\x00\x00\x00\x00", re.S)
    for field in fields:
        mt = pattern.search(buf, pos)
        n = mt.group(1)[0]
        p = mt.end()
        lengths = struct.unpack(f"<{n}Q", buf[p:p + 8 * n])
        p += 8 * n
        labels = []
        for L in lengths:
            labels.append(buf[p:p + 2 * L].decode("utf-16le"))
            p += 2 * L
        out[field] = labels
        pos = p
    return out


# ---------------------------------------------------------------- behaviour

def _behavior_psth(signal, ts, starts, fs):
    """Mean of a video signal in 10 ms windows, as code PSTHBehavior.m: from the frame
    nearest the trial start, windows of 0.01*fs + 1 frames stepped by 0.01*fs frames."""
    step = int(round(W10 * fs))
    pre = int(round(PRE * fs))
    nwin = len(np.arange(PRE, POST - W10 + 1e-9, W10))  # 300 windows, as the code
    out = np.full((len(starts), nwin), np.nan)
    anchor = np.searchsorted(ts, starts)
    anchor = np.clip(anchor, 1, len(ts) - 1)
    anchor = np.where(np.abs(ts[anchor - 1] - starts) <= np.abs(ts[anchor] - starts), anchor - 1, anchor)
    # MATLAB indices are 1-based; startFrame = AnchorFrame + PreFrame keeps the same offset.
    for k, (a, s) in enumerate(zip(anchor, starts)):
        if s < ts[0] or s > ts[-1]:
            continue
        first = a + pre
        last = first + (nwin - 1) * step + step
        if first < 0 or last >= len(signal):
            continue
        idx = first + np.arange(nwin)[:, None] * step + np.arange(step + 1)[None, :]
        out[k] = signal[idx].mean(axis=1)
    return out


def _mode(x):
    v, c = np.unique(x[~np.isnan(x)], return_counts=True)
    return v[np.argmax(c)]


def _mad(x, kind):
    x = x[~np.isnan(x)]
    if kind == "median":
        return np.median(np.abs(x - np.median(x)))
    return np.mean(np.abs(x - np.mean(x)))


def bin_index(t1, t2):
    """Indices of the 10 ms bins whose right-edge labels are nearest t1 and t2, inclusive, as
    the code's min(abs(WindowCenters - t)) selection (labels -0.99 to 2.00)."""
    labels = PRE + W10 * np.arange(1, N10 + 1)
    return np.arange(np.argmin(np.abs(labels - t1)), np.argmin(np.abs(labels - t2)) + 1)


def quiet_flags(beh, kind):
    """Quiet by whisker speed and by jaw movement (see module docstring)."""
    base, pre = bin_index(-1.0, 0.0), bin_index(0.8, 1.0)
    out = {}
    for sig in ("whisker_speed", "jaw_movement"):
        x = beh[sig]
        with np.errstate(all="ignore"):
            b = np.nanmean(x[:, base], axis=1)
            p = np.nanmean(x[:, pre], axis=1)
        th = np.nanmedian(b) + _mad(b, kind)
        out[sig] = p <= th
    return out


def read_trials(f):
    T = f["intervals/trials"]
    tr = {k: T[k][:] for k in T.keys() if k not in ("id",) and not k.endswith("_index")}
    for k, v in tr.items():
        if v.dtype == object:
            tr[k] = _str(v)
    tr["trial_type"] = tr["trial_type"].astype(int)
    return tr


def read_behavior(f, subject, starts):
    g = f["processing/behavior/BehavioralTimeSeries"]
    ts = g["C2Whisker_Angle/timestamps"][:]
    wa = g["C2Whisker_Angle/data"][:].astype(float)
    jaw = g["Jaw_Coordinate/data"][:].astype(float)
    tongue = g["Tongue_Coordinate/data"][:].astype(float)
    fs = 100 if subject == "PG019" else 200
    ws = np.abs(np.diff(wa))
    ws = np.concatenate([[ws[0]], ws])
    jx, jy = _mode(jaw[:, 0]), _mode(jaw[:, 1])
    jm = np.hypot(jaw[:, 0] - jx, jaw[:, 1] - jy)
    tm = np.hypot(tongue[:, 0] - jx, tongue[:, 1] - jy)
    tm[tm > 20 * np.nanmean(tm)] = np.nan
    beh = {"whisker_speed": _behavior_psth(ws, ts, starts, fs),
           "jaw_movement": _behavior_psth(jm, ts, starts, fs),
           "tongue_movement": _behavior_psth(tm, ts, starts, fs)}
    dts = np.diff(ts)
    info = {"video_fs_nominal": fs, "video_dt_median_ms": 1000 * np.median(dts),
            "video_n_frames": len(ts), "video_t0": ts[0], "video_t1": ts[-1],
            "whisker_angle_range": (np.nanmin(wa), np.nanmax(wa)),
            "jaw_nan_frac": float(np.isnan(jaw).mean())}
    return beh, info


# ---------------------------------------------------------------- spikes

def _counts(spikes, starts, t0, width, nbins):
    edges = starts[:, None] + t0 + width * np.arange(nbins + 1)[None, :]
    c = np.searchsorted(spikes, edges.ravel(), side="left").reshape(edges.shape)
    return np.diff(c, axis=1)


def load_session(asset, with_spikes=True):
    """One ephys session: trials, movement traces, quiet flags, units and spike counts.

    Spike counts are kept for completed trials only and for units in the five areas that
    pass the CCF filter: `c10` (trials x 300 bins x units, 10 ms, -1 to 2 s) and `c5`
    (trials x 30 bins x units, 5 ms, 0.95 to 1.10 s), as uint8.
    """
    path, size, aid = asset
    f = open_nwb(aid)
    subject = f["general/subject/subject_id"][()].decode()
    tr = read_trials(f)
    starts = tr["start_time"]
    beh, binfo = read_behavior(f, subject, starts)
    U = f["units"]
    units = {k: _str(U[k][:]) for k in ("location", "ccf_location", "allenccf_area_layer", "probe_name")}
    for k in ("rsUnits", "fsUnits"):
        units[k] = U[k][:].astype(bool)
    units["spike_width"] = U["spike_width"][:]
    units["id"] = U["id"][:]
    alist = area_list()
    units["area"] = np.array([loc if (loc in alist and ccf in alist[loc]) else ""
                              for loc, ccf in zip(units["location"], units["ccf_location"])], dtype=object)
    s = {"path": path, "subject": subject, "session": path.split("/")[-1].split("-processed")[0],
         "trials": tr, "beh": beh, "beh_info": binfo, "units": units,
         "quiet_median": quiet_flags(beh, "median"), "quiet_mean": quiet_flags(beh, "mean")}
    s["completed"] = ~tr["early_lick"].astype(bool)
    if with_spikes:
        keep = np.flatnonzero(units["area"] != "")
        index = U["spike_times_index"][:]
        st = U["spike_times"]
        comp = starts[s["completed"]]
        c10 = np.zeros((len(comp), N10, len(keep)), np.uint8)
        c5 = np.zeros((len(comp), N5, len(keep)), np.uint8)
        allspk = st[:]
        unsorted = 0
        for j, u in enumerate(keep):
            a = 0 if u == 0 else int(index[u - 1])
            sp = allspk[a:int(index[u])]
            if np.any(np.diff(sp) < 0):
                unsorted += 1
                sp = np.sort(sp)
            c10[:, :, j] = np.minimum(_counts(sp, comp, PRE, W10, N10), 255)
            c5[:, :, j] = np.minimum(_counts(sp, comp, T5_START, W5, N5), 255)
        s["keep"] = keep
        s["c10"], s["c5"] = c10, c5
        s["unsorted_units"] = unsorted
        s["n_spikes"] = len(allspk)
    f.close()
    return s


def load_sessions(with_spikes=True, workers=4, subset=None):
    al = ephys_assets() if subset is None else [a for a in ephys_assets() if any(x in a[0] for x in subset)]
    area_list()
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(lambda a: load_session(a, with_spikes), al))


# ---------------------------------------------------------------- optogenetics

def load_opto_session(asset):
    path, size, aid = asset
    f = open_nwb(aid)
    tr = read_trials(f)
    subject = f["general/subject/subject_id"][()].decode()
    geno = f["general/subject/genotype"][()].decode()
    f.close()
    areas = sorted(set(tr["opto_area"]) - {"nan"})
    return {"path": path, "subject": subject, "genotype": geno, "trials": tr,
            "area": areas[0] if len(areas) == 1 else ",".join(areas)}


def load_opto(workers=8):
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(load_opto_session, opto_assets()))


# ---------------------------------------------------------------- statistics

def bh_fdr(p):
    """Benjamini-Hochberg adjusted p-values (MATLAB mafdr(p, 'BHFDR', true))."""
    p = np.asarray(p, float)
    n = len(p)
    order = np.argsort(p)
    q = p[order] * n / np.arange(1, n + 1)
    q = np.minimum.accumulate(q[::-1])[::-1]
    out = np.empty(n)
    out[order] = np.minimum(q, 1)
    return out


def paired_bootstrap_p(a, b, n_draw, iterations, rng):
    """Code, Ghaderi2025_Figure2_d_Plick_Sessions.m: draw n_draw paired sessions with
    replacement, difference of means a - b; p = (draws on the wrong side of zero + 1) /
    iterations, two-tailed as 2 min(p, 1 - p)."""
    a, b = np.asarray(a, float), np.asarray(b, float)
    idx = rng.integers(0, len(a), size=(iterations, n_draw))
    d = a[idx].mean(axis=1) - b[idx].mean(axis=1)
    obs = a.mean() - b.mean()
    p = ((d <= 0).sum() + 1) / iterations if obs > 0 else ((d >= 0).sum() + 1) / iterations
    return 2 * min(p, 1 - p)


def auc_si(x, y):
    """Selectivity index 2(AUC - 0.5) of x (positive class) against y, ties counted half
    (MATLAB perfcurve's AUC)."""
    from scipy.stats import rankdata
    v = np.concatenate([x, y])
    r = rankdata(v)
    n1, n2 = len(x), len(y)
    auc = (r[:n1].sum() - n1 * (n1 + 1) / 2) / (n1 * n2)
    return 2 * (auc - 0.5)


def roc_test(x, y, permutations, rng):
    """SI and permutation p as code selectivity_index_calculation.m ('permut'): labels
    shuffled `permutations` times; p = fraction of shuffles with |SI| at least the observed."""
    from scipy.stats import rankdata
    v = np.concatenate([x, y]).astype(float)
    r = rankdata(v)
    n1, n2 = len(x), len(y)
    n = n1 + n2
    si = 2 * ((r[:n1].sum() - n1 * (n1 + 1) / 2) / (n1 * n2) - 0.5)
    perm = np.argsort(rng.random((permutations, n)), axis=1)[:, :n1]
    s = r[perm].sum(axis=1)
    si_rand = 2 * ((s - n1 * (n1 + 1) / 2) / (n1 * n2) - 0.5)
    return si, float(np.mean(np.abs(si) <= np.abs(si_rand)))


# ---------------------------------------------------------------- selections

def correct_mask(s, ttype):
    """Correct trials of a type among the completed trials: Hit for type 1, correct rejection
    (no lick) for types 2 to 5."""
    tr = s["trials"]
    c = s["completed"]
    lick = tr["lick_flag"].astype(bool)[c]
    tt = tr["trial_type"][c]
    return (tt == ttype) & (lick if ttype == 1 else ~lick)


def trial_mask(s, ttype, lick):
    """Completed trials of a type with (lick=True) or without (lick=False) a lick."""
    tr = s["trials"]
    c = s["completed"]
    L = tr["lick_flag"].astype(bool)[c]
    return (tr["trial_type"][c] == ttype) & (L if lick else ~L)


def quiet_mask(s, rule="median", signals=("whisker_speed", "jaw_movement")):
    """Quiet flags of the completed trials; rule 'median' (Methods) or 'mean' (code's mad),
    or 'none' for all trials."""
    n = int(s["completed"].sum())
    if rule == "none":
        return np.ones(n, bool)
    q = s[f"quiet_{rule}"]
    out = np.ones(n, bool)
    for sig in signals:
        out &= q[sig][s["completed"]]
    return out


def area_columns(s, area):
    """Columns of s['c10'] / s['c5'] that hold the units of an area (probe area and CCF label)."""
    return np.flatnonzero(s["units"]["area"][s["keep"]] == area)


def area_sessions(S, area, min_units=1):
    for s in S:
        cols = area_columns(s, area)
        if len(cols) >= min_units:
            yield s, cols


def temporal_correlation(X):
    """Trial-by-trial 300 x 300 Pearson correlation between the population vectors of the time
    bins (code, Temporal_corrrelation_10ms.m: corrcoef of the bins x neurons matrix), averaged
    over trials, NaN where a bin has no variance across neurons. X: trials x bins x neurons."""
    acc = np.zeros((X.shape[1], X.shape[1]))
    cnt = np.zeros_like(acc)
    for x in X.astype(float):
        z = x - x.mean(axis=1, keepdims=True)
        sd = np.sqrt((z ** 2).sum(axis=1))
        with np.errstate(all="ignore"):
            z = z / sd[:, None]
        r = z @ z.T
        ok = np.isfinite(r)
        acc[ok] += r[ok]
        cnt += ok
    with np.errstate(all="ignore"):
        return acc / cnt


def kruskal_lsd(groups):
    """Kruskal-Wallis over groups (NaN dropped), then Fisher LSD comparisons of mean ranks, as
    MATLAB multcompare(stats, 'CriticalValueType', 'lsd') after kruskalwallis: z = (Ri - Rj) /
    sqrt(s2 (1/ni + 1/nj)) with s2 = N (N + 1) / 12 (tie-corrected as MATLAB's variance of the
    ranks), two-sided normal p. Returns (H, p, {(i, j): (mean rank difference, p)})."""
    from scipy.stats import kruskal, norm, rankdata
    gs = [np.asarray(x, float)[np.isfinite(x)] for x in groups]
    H, p = kruskal(*gs)
    allv = np.concatenate(gs)
    r = rankdata(allv)
    N = len(allv)
    s2 = np.var(r, ddof=1)  # equals N(N+1)/12 without ties
    sizes = [len(x) for x in gs]
    bounds = np.cumsum([0] + sizes)
    mr = [r[bounds[i]:bounds[i + 1]].mean() for i in range(len(gs))]
    out = {}
    for i in range(len(gs)):
        for j in range(i + 1, len(gs)):
            z = (mr[i] - mr[j]) / np.sqrt(s2 * (1 / sizes[i] + 1 / sizes[j]))
            out[(i, j)] = (mr[i] - mr[j], 2 * norm.sf(abs(z)))
    return H, p, out


def split_train(idx, frac, rng):
    """A random fraction of trial indices for training and the rest held out."""
    idx = rng.permutation(idx)
    k = int(round(frac * len(idx)))
    return np.sort(idx[:k]), np.sort(idx[k:])


# ---------------------------------------------------------------- outside input: cluster labels

def cluster_labels():
    """The paper's cluster labels (processed_data/Data_Clustering.mat on Zenodo): per neuron
    the cluster number (Cluster_Counter_Ordered), the code's global unit index (Id_Ordered),
    and the area, CCF label and layer the code assigned."""
    import scipy.io
    m = scipy.io.loadmat(io.BytesIO(zenodo_member("processed_data/Data_Clustering.mat")),
                         variable_names=["Cluster_Counter_Ordered", "Id_Ordered", "Areas_Ordered",
                                         "CCF_location_Ordered", "Layer_Ordered"])
    sc = lambda a: str(a.ravel()[0]) if a.size else ""
    return {"cluster": m["Cluster_Counter_Ordered"].ravel().astype(int),
            "global_id": m["Id_Ordered"].ravel().astype(int),
            "area": np.array([sc(a) for a in m["Areas_Ordered"].ravel()], dtype=object),
            "ccf": np.array([sc(a) for a in m["CCF_location_Ordered"].ravel()], dtype=object),
            "layer": np.array([sc(a) for a in m["Layer_Ordered"].ravel()], dtype=object)}


def global_ids(S):
    """The code's global unit index (psth_10ms.m): files in name order, within a file one
    'probe' per distinct unit `location` in sorted order, units in file order, numbered from 1
    over all units of every location. Returns {global id: (session index, unit row)}."""
    out, n = {}, 0
    order = sorted(range(len(S)), key=lambda i: S[i]["path"].split("/")[-1])
    for i in order:
        loc = S[i]["units"]["location"]
        for L in sorted(set(loc)):
            for j, u in enumerate(np.flatnonzero(loc == L)):
                out[n + j + 1] = (i, int(u))
            n += int((loc == L).sum())
    return out


# ---------------------------------------------------------------- per-neuron PSTH measures

def neuron_window_means(S, area, masks, window, rule="median", signals=("whisker_speed", "jaw_movement"),
                        baseline=(-1.0, 0.0)):
    """Per neuron of an area, for each trial mask (a function of a session), the mean firing
    rate (Hz) over `window` minus the mean over `baseline` of the trial-averaged 10 ms PSTH
    (code, Neuronal_data_10ms.m). Sessions lacking trials for any mask are skipped.
    Returns a list of arrays (one per mask) and the session index of each neuron."""
    out, sess = [[] for _ in masks], []
    w, b = bin_index(*window), bin_index(*baseline)
    for k, s in enumerate(S):
        cols = area_columns(s, area)
        if len(cols) == 0:
            continue
        q = quiet_mask(s, rule, signals)
        ms = [m(s) & q for m in masks]
        if any(m.sum() == 0 for m in ms):
            continue
        for i, m in enumerate(ms):
            x = s["c10"][m][:, :, cols].mean(axis=0) / W10
            out[i].append(x[w].mean(axis=0) - x[b].mean(axis=0))
        sess.append(np.full(len(cols), k))
    return [np.concatenate(o) if o else np.array([]) for o in out], (np.concatenate(sess) if sess else np.array([]))


# ---------------------------------------------------------------- decoding

def _svm(method, C=1.0):
    """(b) the code's libsvm nu-SVC, '-s 1 -t 0' (linear kernel, default nu 0.5);
    (a) the Methods' grid search: a linear C-SVM whose C is chosen by nested 5-fold search over
    10^-3 to 10^3 in decades (the claims file's grid). Iterations are capped at 10^5 so that a
    large C on data that cannot be separated does not stall (a standard choice)."""
    from sklearn.svm import NuSVC, SVC
    if method == "code":
        return NuSVC(kernel="linear", nu=0.5)
    return SVC(kernel="linear", C=C, max_iter=100000)


C_GRID = 10.0 ** np.arange(-3, 4)


def _folds(y, k, rng):
    """Stratified k-fold assignment: each class shuffled and dealt round-robin to the folds."""
    f = np.empty(len(y), int)
    for c in np.unique(y):
        idx = rng.permutation(np.flatnonzero(y == c))
        f[idx] = np.arange(len(idx)) % k
    return f


def _fit_score(X, y, tr, te, method, C=1.0):
    import warnings
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")     # capped iterations warn; the cap is stated above
            clf = _svm(method, C).fit(X[tr], y[tr])
        return 100 * (clf.predict(X[te]) == y[te]).mean()
    except ValueError:      # nu infeasible for this training set: count as chance
        return 50.0


def decode_bin(X1, X2, rng, method="code"):
    """Accuracy (%) of one bin: the larger class randomly undersampled to the smaller, features
    z-scored over the balanced trials (constant features dropped), stratified 5-fold
    cross-validation, mean accuracy over folds (code, Decoding_NbNeurons5_50.m)."""
    n = min(len(X1), len(X2))
    if n < 5:
        return np.nan
    X1 = X1[rng.choice(len(X1), n, replace=False)] if len(X1) > n else X1
    X2 = X2[rng.choice(len(X2), n, replace=False)] if len(X2) > n else X2
    X = np.concatenate([X1, X2]).astype(float)
    y = np.r_[np.ones(n), -np.ones(n)]
    sd = X.std(axis=0, ddof=1)
    keep = sd > 0
    if not keep.any():
        return 50.0
    X = (X[:, keep] - X[:, keep].mean(axis=0)) / sd[keep]
    folds = _folds(y, 5, rng)
    acc = []
    for k in range(5):
        tr, te = np.flatnonzero(folds != k), np.flatnonzero(folds == k)
        if method == "code":
            acc.append(_fit_score(X, y, tr, te, "code"))
            continue
        inner = _folds(y[tr], 5, rng)
        scores = []
        for C in C_GRID:
            scores.append(np.mean([_fit_score(X[tr], y[tr], np.flatnonzero(inner != j), np.flatnonzero(inner == j), "methods", C)
                                   for j in range(5)]))
        acc.append(_fit_score(X, y, tr, te, "methods", C_GRID[int(np.argmax(scores))]))
    return float(np.mean(acc))


def decode_session(X1, X2, bins, n_neurons, repetitions, method, seed, drop=None):
    """Mean accuracy over `repetitions` random subsets of `n_neurons` neurons (None: all), for
    each bin in `bins`. X1, X2: trials x bins x neurons of the two classes. `drop`: boolean
    mask of neurons to leave out before decoding."""
    rng = np.random.default_rng(seed)
    if drop is not None:
        X1, X2 = X1[:, :, ~drop], X2[:, :, ~drop]
    out = np.full((repetitions, len(bins)), np.nan)
    for r in range(repetitions):
        cols = (np.arange(X1.shape[2]) if n_neurons is None else
                np.sort(rng.choice(X1.shape[2], n_neurons, replace=False)))
        for k, b in enumerate(bins):
            out[r, k] = decode_bin(X1[:, b][:, cols], X2[:, b][:, cols], rng, method)
    return out.mean(axis=0)
