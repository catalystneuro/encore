"""Loading and measures for Huang et al. (2025) on DANDI:001349.

Paper: Huang, Hess, Bajpai, Li, Hobson, Xu, Barton & Lu (2025), "From initial formation to
developmental refinement: GABAergic inputs shape neuronal subnetworks in the primary
somatosensory cortex", iScience 28, 112104, doi:10.1016/j.isci.2025.112104.

Where each parameter comes from:

- The claims file (claims/huang-2025.yaml) fixes the measures and the readings O1 to O6 in its
  header; those are cited by their label.
- The paper's code is github.com/EdnaHuang/SubnetworkAssembley2024 at commit
  28e1b6d79c830b77831ceb97738ab423f9fc333f (REPO below). Its summary tables give the
  quiescent window of each dataset (O1 reading a): the dataset has no behavioural video, so
  reading b cannot be run.
- Events are the dataset's own `ca_events_chn0` series (non-zero frames), which the notebook
  shows to match the detection of Step2_Event_Detection_binaryRaster.mlx run on the dataset's
  `z_score_chn0`.
- The window is cut as in Step4 and Modol_script.m:
  frames floor(start/0.0656) to floor(end/0.0656) - 1, 1-based and inclusive.
- Shuffle thresholds whose distribution is known in closed form (the participation tests of
  Modol_script.m, which draw random frames or random cells without replacement) use the exact
  hypergeometric quantile in place of 5,000 random draws; this is a standard choice that
  only removes Monte Carlo noise.
- Random seeds are fixed (a standard choice); each dataset's generator is seeded from its
  asset path.
"""

import hashlib
import json
import os

import h5py
import numpy as np
import pandas as pd
import remfile
import requests
from scipy.signal import find_peaks
from scipy.stats import hypergeom

DANDISET_ID = "001349"
DANDISET_VERSION = "0.250604.1510"
API = "https://api.dandiarchive.org/api"
REPO = "EdnaHuang/SubnetworkAssembley2024"
REPO_COMMIT = "28e1b6d79c830b77831ceb97738ab423f9fc333f"
RAW = f"https://raw.githubusercontent.com/{REPO}/{REPO_COMMIT}/Statistical_Script_Data"
DEV_TABLE = f"{RAW}/Analysis_Develop_WT/data/Kmean_CovM_SummaryDevAll_CorrDistanceArea.xlsx"
DREADD_TABLE = f"{RAW}/Analysis_WT_Dlx_GsDREADD/data/Kmean_CovM_SummaryDlxGsDREADD_CorrDistanceArea.xlsx"
MI_DEV_TABLE = f"{RAW}/Analysis_Develop_WT/data/Kmean_CovM_MI_Corr.xlsx"
MI_DREADD_TABLE = f"{RAW}/Analysis_WT_Dlx_GsDREADD/data/Kmean_CovM_SummaryDlxGsDREADD_MICorr.xlsx"
HISTO_TABLE = f"{RAW}/Analysis_VGAT-Syt2/data/P15_VGAT_SYT2_20230318.xlsx"
FRAME_S = 0.0656  # Step4 and Modol_script.m, 65.6 ms per frame (Methods)
CNO_LABELS = {"CNOInjection: Neg; P15CNO: Neg": "none",
              "CNOInjection: +; P15CNO: Neg": "before",
              "CNOInjection: +; P15CNO: CNO": "after"}


# ---------------------------------------------------------------- archive

def list_assets():
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/?page_size=1000"
    out = []
    while url:
        page = requests.get(url, timeout=60).json()
        out += page["results"]
        url = page.get("next")
    return out


def s3_url(asset_id):
    return requests.head(f"{API}/assets/{asset_id}/download/", allow_redirects=True, timeout=60).url


def _scalar(f, key):
    try:
        v = f[key][()]
    except KeyError:
        return None
    return v.decode() if isinstance(v, bytes) else v


def read_metadata(asset):
    """Metadata and array shapes of one file, no data."""
    for attempt in range(4):
        try:
            with h5py.File(remfile.File(s3_url(asset["asset_id"])), "r") as f:
                fl = f["processing/ophys/Fluorescence"]
                ip = f["general/optophysiology/ImagingPlane_1_chn1"]
                loc = _scalar(ip, "location")
                parts = dict(p.split(": ") for p in loc.split(", "))
                return {
                    "path": asset["path"], "asset_id": asset["asset_id"], "size": asset["size"],
                    "subject": _scalar(f, "general/subject/subject_id"),
                    "sex": _scalar(f, "general/subject/sex"),
                    "age": _scalar(f, "general/subject/age"),
                    "date_of_birth": _scalar(f, "general/subject/date_of_birth"),
                    "line": json.loads(_scalar(f, "general/subject/description")).get("line"),
                    "session_start": _scalar(f, "session_start_time"),
                    "session_description": _scalar(f, "session_description"),
                    "hemisphere": parts.get("hemisphere"), "layer": int(parts["layer"]),
                    "location": int(parts["location_id"]),
                    "rate": float(fl["z_score_chn0/starting_time"].attrs["rate"]),
                    "imaging_rate": float(ip["imaging_rate"][()]),
                    "n_frames": fl["z_score_chn0/data"].shape[0],
                    "n_rois": fl["z_score_chn0/data"].shape[1],
                    "series": sorted(fl.keys()),
                }
        except Exception as e:  # network errors: retry
            err = e
    raise err


def _read_chunk(chunk):
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(4) as ex:
        return list(ex.map(read_metadata, chunk))


def metadata_table(assets, workers=8):
    """read_metadata() over all assets, in processes (h5py holds the interpreter lock)."""
    from concurrent.futures import ProcessPoolExecutor
    import multiprocessing as mp
    chunks = [assets[i::workers * 4] for i in range(workers * 4)]
    with ProcessPoolExecutor(workers, mp_context=mp.get_context("spawn")) as ex:
        rows = [r for part in ex.map(_read_chunk, chunks) for r in part]
    d = pd.DataFrame(rows)
    d["age_days"] = d.age.str.extract(r"P(\d+)D", expand=False).astype(int)
    d["cno"] = d.session_description.map(CNO_LABELS)
    d["session"] = d.path.str.extract(r"ses-(\d+)_", expand=False).astype(int)
    return d


# ---------------------------------------------------------------- the paper's tables (O1 a)

def _norm_subject(s):
    s = s.replace("chrm3q", "Chrm3q")
    if s.startswith("C2-"):
        s = "C57-" + s
    return s.replace("_", "-")


def paper_tables():
    """Per-dataset rows of the repository's summary tables, with the dataset's naming of subjects."""
    dev = pd.read_excel(DEV_TABLE)
    dre = pd.read_excel(DREADD_TABLE)
    mi_dev = pd.read_excel(MI_DEV_TABLE)
    mi_dre = pd.read_excel(MI_DREADD_TABLE)
    # in the MI tables, the R_* columns hold MI of the event rasters and the ZF_* columns MI of the
    # Z-scored traces (their scale differs from the Pearson ZF_* columns of the other tables)
    for t, m in ((dev, mi_dev), (dre, mi_dre)):
        t["MI_events_allpair_mean"] = m["R_allpair_mean"].values
        t["MI_Z_allpair_mean"] = m["ZF_R_allpair_mean"].values
    assert (mi_dev["name"].values == dev["name"].values).all()
    assert (mi_dre["name"].values == dre["name"].values).all()
    for t in (dev, dre):
        t["subject"] = t.SubjectID.map(_norm_subject)
    dev["table"] = "developmental"
    dre["table"] = "dreadd"
    dre["cno"] = np.where(dre.P15CNO == "CNO", "after", "before")
    return dev, dre


def link(meta, table, kind):
    """Match table rows to files by subject, layer, location and ROI count, then by age.

    Returns the matched pairs and the unmatched rows on each side. The age is used to break ties
    and is reported, since one file's age field is wrong (P190D)."""
    if kind == "developmental":
        files = meta[meta.cno != "after"]
    else:
        files = meta[(meta.cno != "none") & (meta.age_days == 15)]
    t = table.rename(columns={"Layer": "layer", "Location": "location"}).copy()
    t["row"] = np.arange(len(t))
    keys = ["subject", "layer", "location"]
    if kind == "dreadd":
        keys.append("cno")
    m = t.merge(files, left_on=keys + ["total_cell_number"], right_on=keys + ["n_rois"],
                suffixes=("_paper", ""))
    m["age_match"] = m.Age == m.age_days
    # several candidates: keep the one whose age agrees
    m = m.sort_values("age_match", ascending=False).drop_duplicates("row")
    m = m.drop_duplicates("path")
    unmatched_rows = t[~t.row.isin(m.row)]
    unmatched_files = files[~files.path.isin(m.path)]
    return m.sort_values("row").reset_index(drop=True), unmatched_rows, unmatched_files


def window_frames(start_s, end_s):
    """0-based slice of the window, as MATLAB floor(start/0.0656):floor(end/0.0656) - 1."""
    a = int(np.floor(start_s / FRAME_S))
    b = int(np.floor(end_s / FRAME_S)) - 1
    return slice(a - 1, b)


# ---------------------------------------------------------------- loading

def load_dataset(path, asset_id, start_s, end_s, full_events=False):
    """Read the window of the events and Z-score series and the ROI centres of one file."""
    sl = window_frames(start_s, end_s)
    for attempt in range(4):
        try:
            with h5py.File(remfile.File(s3_url(asset_id)), "r") as f:
                fl = f["processing/ophys/Fluorescence"]
                ev_all = fl["ca_events_chn0/data"][:]
                z = fl["z_score_chn0/data"][sl, :].T.astype(float)
                ps = f["processing/ophys/ImageSegmentation/PlaneSegmentation_1"]
                pm = ps["pixel_mask"][:]
                idx = ps["pixel_mask_index"][:]
                zfull = fl["z_score_chn0/data"][:].T if full_events else None
            break
        except Exception as e:
            err = e
    else:
        raise err
    starts = np.r_[0, idx[:-1]].astype(int)
    # Calcuate_Subnetwork_Distances.m uses Suite2p's stat.med, the median pixel, rounded
    centres = np.array([[np.round(np.median(pm["x"][s:e])), np.round(np.median(pm["y"][s:e]))]
                        for s, e in zip(starts, idx.astype(int))])
    ev = ev_all.T
    out = {"events": ev[:, sl] != 0, "any_event_recording": (ev != 0).any(1), "z": z,
           "events_full_binary": ev != 0,
           "xy": centres, "n_frames_total": ev.shape[1], "seconds": end_s - start_s}
    if full_events:
        out["events_full"] = ev != 0
        out["z_full"] = zfull
    return out


# ---------------------------------------------------------------- Step2 event detection

def step2_events(Z, W=77, factor=4):
    """Step2_Event_Detection_binaryRaster.mlx on cells x frames Z-score traces (whole recording)."""
    from numpy.lib.stride_tricks import sliding_window_view
    out = np.zeros(Z.shape, bool)
    for i, z in enumerate(Z):
        tr = z + abs(z.min()) if z.min() < 0 else z
        rms = np.sqrt((sliding_window_view(tr, W) ** 2).mean(1))
        k = int(np.argmin(rms))
        wf = z[k:k + W]
        mu = wf.mean()
        p, _ = find_peaks(wf)
        v, _ = find_peaks(wf.max() - wf)
        mm = np.sort(np.r_[p, v])
        thr = np.mean(np.abs(np.diff(wf[mm]))) * factor
        ev = np.where(z <= mu, 0, z - mu if mu > 0 else z + abs(mu))
        pk, _ = find_peaks(ev)
        out[i, pk[ev[pk] >= thr]] = True
    return out


# ---------------------------------------------------------------- activity measures

def event_frequency(E, seconds):
    """Step4: events per second per neuron in the window. O6 a, cells with an event; b, all ROIs."""
    f = E.sum(1) / seconds
    return {"event_freq_active": float(f[f > 0].mean()) if (f > 0).any() else np.nan,
            "event_freq_all": float(f.mean())}


def _runs_above(x, th):
    above = x > th
    return int(np.sum(above[1:] & ~above[:-1]) + above[0])


def synchrony_methods(E, seconds, rng, n_shuffle=100, pct=95):
    """O2 main reading (Methods): each cell's events shuffled in time 100 times (rate kept); the
    threshold is the 95th percentile of the shuffles' peak percent of active cells; an event runs
    from an upward to a downward crossing."""
    n, T = E.shape
    frac = E.mean(0)
    peaks = np.empty(n_shuffle)
    counts = E.sum(1)
    for s in range(n_shuffle):
        sh = np.zeros_like(E)
        for i in range(n):
            if counts[i]:
                sh[i, rng.choice(T, counts[i], replace=False)] = True
        peaks[s] = sh.mean(0).max()
    th = np.percentile(peaks, pct)
    return _runs_above(frac, th) / seconds


def synchrony_step7(E, any_event, seconds, rng, n_shuffle=100, pct=95):
    """O2 variant (Step7_Synchrony_analysis.mlx): cells with no event in the recording dropped;
    circular shifts; threshold the 95th percentile of all shuffled frames; findpeaks above it."""
    E = E[any_event]
    n, T = E.shape
    frac = E.mean(0)
    shifted = np.zeros((n_shuffle, T))
    for s in range(n_shuffle):
        sh = rng.integers(1, T + 1, n)
        for i in range(n):
            shifted[s] += np.roll(E[i], sh[i])
    th = np.percentile(shifted.ravel() / n, pct)
    pk, _ = find_peaks(frac, height=th)
    # MATLAB MinPeakHeight keeps peaks >= th; scipy height is >= too
    return len(pk) / seconds


def pearson_mean(Z):
    """Mean over all pairs of the Pearson correlation of Z-scored traces (Step8)."""
    ok = Z.std(1) > 0
    C = np.corrcoef(Z[ok])
    iu = np.triu_indices(len(C), 1)
    return float(np.nanmean(C[iu]))


def mi_mean(Z, L=256):
    """Mean over pairs of calculate_mi_matrix_trace.m: marginals from histcounts with L bins,
    joint histogram from values scaled and rounded to 0..L-1, MI in bits."""
    n, T = Z.shape
    mins, maxs = Z.min(1, keepdims=True), Z.max(1, keepdims=True)
    q = np.round((Z - mins) * (L - 1) / (maxs - mins + np.finfo(float).eps)).astype(np.int64)
    marg = np.zeros((n, L))
    for i in range(n):
        h, _ = np.histogram(Z[i], bins=L)
        marg[i] = h / T
    vals = []
    for i in range(n):
        codes = q[i][None, :] * L + q[i + 1:]
        for j_off, c in enumerate(codes):
            j = i + 1 + j_off
            u, cnt = np.unique(c, return_counts=True)
            pab = cnt / T
            pa = marg[i][u // L]
            pb = marg[j][u % L]
            papb = pa * pb
            ok = (papb > 1e-12) & (pab > 1e-12)
            vals.append(np.sum(pab[ok] * np.log2(pab[ok] / papb[ok])))
    return float(np.mean(vals)) if vals else np.nan


def tetrachoric(E):
    """tetrac.m on cells x frames binary rasters: cos(pi / (1 + sqrt(ad / bc))), 1 when bc = 0."""
    X = E.astype(float)
    d = X @ X.T
    s = X.sum(1)
    T = X.shape[1]
    b = s[None, :] - d   # col 0, row 1 (symmetric counts)
    c = s[:, None] - d
    a = T - d - b - c
    ad, bc = a * d, b * c
    with np.errstate(divide="ignore", invalid="ignore"):
        r = np.cos(np.pi / (1 + np.sqrt(ad / bc)))
    r[bc == 0] = 1.0
    np.fill_diagonal(r, 1.0)
    return r


# ---------------------------------------------------------------- k-means event clusters

def covariance_matrix(E):
    """CovarM.m: normalized covariance (lag 0, divided by N) between frames over cells; NaN to 0."""
    X = E.astype(float)
    Xc = X - X.mean(0, keepdims=True)
    sd = X.std(0, ddof=1)
    n = X.shape[0]
    with np.errstate(divide="ignore", invalid="ignore"):
        M = (Xc.T @ Xc) / np.outer(sd, sd) / n
    M[~np.isfinite(M)] = 0.0
    return M


def silhouette(M, idx, k):
    """silh.m with dissimilarity 1 - M."""
    n = len(idx)
    onehot = np.zeros((n, k))
    onehot[np.arange(n), idx] = 1
    sums = M @ onehot
    counts = onehot.sum(0)
    own = idx
    sums[np.arange(n), own] -= np.diag(M)
    cnt = np.broadcast_to(counts, (n, k)).copy()
    cnt[np.arange(n), own] -= 1
    with np.errstate(divide="ignore", invalid="ignore"):
        a = 1 - sums / cnt
    aa = a[np.arange(n), own]
    other = a.copy()
    other[np.arange(n), own] = np.inf
    b = other.min(1)
    s = (b - aa) / np.maximum(b, aa)
    return s


def kmeans_opt(M, n_runs, rng, kmin=2, kmax=19):
    """kmeansopt.m: k-means on the rows of M for 2 to 19 clusters, n_runs runs each (one k-means++
    start per run, as MATLAB's kmeans); keep the run with the best mean silhouette. Returns frame
    labels (clusters sorted by median silhouette, descending) and those medians."""
    from sklearn.cluster import KMeans
    # M is symmetric of low rank (at most the number of cells), so the Euclidean distances between
    # its rows equal those between the rows of Q * lambda from its eigendecomposition: k-means on
    # these coordinates is the same problem, solved in fewer dimensions.
    lam, Q = np.linalg.eigh(M)
    keep = np.abs(lam) > 1e-9 * np.abs(lam).max()
    Y = Q[:, keep] * lam[keep]
    best = (-np.inf, None, None)
    for k in range(kmin, kmax + 1):
        if k >= len(M):
            break
        for r in range(n_runs):
            km = KMeans(n_clusters=k, n_init=1, init="k-means++", max_iter=100,
                        random_state=int(rng.integers(2**31 - 1)), algorithm="lloyd").fit(Y)
            lab = km.labels_
            if len(np.unique(lab)) < k:
                continue
            s = silhouette(M, lab, k)
            ms = np.nanmean(s)
            if ms > best[0]:
                best = (ms, lab.copy(), k)
    _, lab, k = best
    s = silhouette(M, lab, k)
    med = np.array([np.median(s[lab == i]) for i in range(k)])
    order = np.argsort(-med, kind="stable")
    relabel = np.empty(k, int)
    relabel[order] = np.arange(k)
    return relabel[lab], med[order]


def assemblies(E, labels, participation):
    """Modol_script.m after the clustering. `participation` is "methods" (95th percentile of
    shuffled data, O4 main) or "code" (the 1 - 0.05/NCl quantile, O4 variant). Shuffles are
    replaced by the exact hypergeometric quantiles."""
    n, T = E.shape
    k = labels.max() + 1
    X = E.astype(int)
    onehot = np.zeros((T, k), int)
    onehot[np.arange(T), labels] = 1
    size = onehot.sum(0)
    CellP = X @ onehot
    CellR = CellP / size
    q_cell = 0.95 if participation == "methods" else 1 - 0.05 / k
    nrnd = X.sum(1)
    CellCl = np.zeros((k, n), bool)
    for j in range(n):
        if nrnd[j] == 0:
            continue
        th = hypergeom.ppf(q_cell, T, size, nrnd[j])
        CellCl[:, j] = CellP[j] > th
    nin = CellCl.sum(0)
    A0, A1, A2 = nin == 0, nin == 1, nin >= 2
    for j in np.where(A2)[0]:
        CellCl[:, j] = False
        CellCl[np.argmax(CellR[j]), j] = True
    C0 = [np.where(CellCl[i])[0] for i in range(k) if CellCl[i].sum() > 2]
    out = {"n_clusters_before": int(k), "n_subnetworks": len(C0), "C0": C0,
           "pct_non": 100 * A0.mean(), "pct_single": 100 * A1.mean(), "pct_multiple": 100 * A2.mean()}
    active = nrnd > 0
    na = active.sum()
    out.update({"pct_non_active": 100 * (A0 & active).sum() / na if na else np.nan,
                "pct_single_active": 100 * (A1 & active).sum() / na if na else np.nan,
                "pct_multiple_active": 100 * (A2 & active).sum() / na if na else np.nan})
    # frames recruiting assemblies (PCl)
    NCl = len(C0)
    if NCl:
        # the frame test is the code's under both readings: the Methods describe only the cell test
        q_frame = 1 - 0.05 / NCl
        nact = X.sum(0)
        recruited = np.zeros(T, int)
        for C in C0:
            RCl = X[C].sum(0)
            th = hypergeom.ppf(q_frame, n, len(C), nact)
            recruited += (RCl > th) & (nact > 0)
        out.update({"pct_frames_none": 100 * np.mean(recruited == 0),
                    "pct_frames_single": 100 * np.mean(recruited == 1),
                    "pct_frames_multiple": 100 * np.mean(recruited >= 2)})
    else:
        out.update({"pct_frames_none": 100.0, "pct_frames_single": 0.0, "pct_frames_multiple": 0.0})
    return out


def subnetwork_measures(E, xy, C0):
    """tCC within and between subnetworks (Calculate_Correlation_in_out_Cluster.mlx) and distances
    (Calcuate_Subnetwork_Distances.m), in pixels."""
    out = {}
    if len(C0) == 0:
        return {k: np.nan for k in ["tcc_in", "tcc_out", "tcc_all", "pw_neuron", "neuron_centroid",
                                    "centroid_centroid"]}
    r = tetrachoric(E)
    iu = np.triu_indices(len(r), 1)
    out["tcc_all"] = float(np.nanmean(r[iu]))
    ins, outs = [], []
    member = np.full(len(r), -1)
    for i, C in enumerate(C0):
        member[C] = i
    for i, C in enumerate(C0):
        sub = r[np.ix_(C, C)]
        ins.append(sub[np.triu_indices(len(C), 1)])
        others = np.where((member >= 0) & (member != i))[0]
        if len(others):
            outs.append(r[np.ix_(C, others)].ravel())
    out["tcc_in"] = float(np.nanmean(np.concatenate(ins)))
    out["tcc_out"] = float(np.nanmean(np.concatenate(outs))) if outs else np.nan
    pw, cd, cents = [], [], []
    for C in C0:
        p = xy[C]
        c = p.mean(0)
        cents.append(c)
        cd.append(np.sqrt(((p - c) ** 2).sum(1)))
        D = np.sqrt(((p[:, None] - p[None]) ** 2).sum(-1))
        pw.append(D[np.triu_indices(len(C), 1)])
    out["pw_neuron"] = float(np.mean(np.concatenate(pw)))
    out["neuron_centroid"] = float(np.mean(np.concatenate(cd)))
    cents = np.array(cents)
    if len(cents) >= 2:
        D = np.sqrt(((cents[:, None] - cents[None]) ** 2).sum(-1))
        out["centroid_centroid"] = float(D[np.triu_indices(len(cents), 1)].mean())
    else:
        out["centroid_centroid"] = np.nan
    return out


def seed_for(path):
    return int(hashlib.sha256(path.encode()).hexdigest()[:8], 16)


def analyse(job):
    """All measures of one dataset. `job` holds path, asset_id, start, end, n_runs (list)."""
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    d = load_dataset(job["path"], job["asset_id"], job["start"], job["end"])
    E, Z, sec = d["events"], d["z"], d["seconds"]
    rng = np.random.default_rng(seed_for(job["path"]))
    res = {"path": job["path"], "start": job["start"], "end": job["end"], "n_rois": E.shape[0], "n_window_frames": E.shape[1],
           "n_active": int(E.any(1).sum())}
    res.update(event_frequency(E, sec))
    # clock check: the same measure in windows shifted by 30 s
    full = d["events_full_binary"]
    sl = window_frames(job["start"], job["end"])
    for shift in (-30, 30):
        a, b = sl.start + int(round(shift / FRAME_S)), sl.stop + int(round(shift / FRAME_S))
        if a >= 0 and b <= full.shape[1]:
            res[f"event_freq_shift{shift:+d}"] = event_frequency(full[:, a:b], sec)["event_freq_active"]
        else:
            res[f"event_freq_shift{shift:+d}"] = np.nan
    res["sync_methods"] = synchrony_methods(E, sec, rng)
    res["sync_step7"] = synchrony_step7(E, d["any_event_recording"], sec, rng)
    res["pearson"] = pearson_mean(Z)
    res["mi"] = mi_mean(Z) if job.get("mi", True) else np.nan
    M = covariance_matrix(E)
    for runs in job["n_runs"]:
        labels, med = kmeans_opt(M, runs, rng)
        res[f"r{runs}_silhouette"] = float(np.mean(med))
        for part in ("methods", "code"):
            a = assemblies(E, labels, part)
            sm = subnetwork_measures(E, d["xy"], a.pop("C0"))
            for key, v in {**a, **sm}.items():
                res[f"r{runs}_{part}_{key}"] = v
    return res


# ---------------------------------------------------------------- the paper's tests T1 and T2

FACTORS_T1 = ("age", "sex", "layer")
FACTORS_T2 = ("cno", "sex", "layer")


def _formulas(f):
    """The eight nested models of Develop_Function_20230219.R (model_select), for factors
    (a, s, l) = (age or cno, sex, layer)."""
    a, s, l = f"C({f[0]})", f"C({f[1]})", f"C({f[2]})"
    main = f"{a} + {s} + {l}"
    return [main,
            f"{main} + {l}:{s}",
            f"{main} + {a}:{s}",
            f"{main} + {a}:{l}",
            f"{main} + {l}:{s} + {a}:{s}",
            f"{main} + {l}:{s} + {a}:{l}",
            f"{main} + {a}:{s} + {a}:{l}",
            f"{a} * {s} * {l}"]


def _fit_mixed(formula, df, structure, reml):
    import statsmodels.formula.api as smf
    import warnings
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        if structure == "subject+location":
            m = smf.mixedlm(formula, df, groups="subject", re_formula="1",
                            vc_formula={"loc": "0 + C(location)"})
        elif structure == "subject":
            m = smf.mixedlm(formula, df, groups="subject", re_formula="1")
        else:
            return smf.ols(formula, df).fit()
        return m.fit(reml=reml, method=["lbfgs", "powell"])


def _singular(fit, structure, tol=1e-4):
    if structure == "ols":
        return False
    var_subject = float(np.asarray(fit.cov_re)[0, 0])
    small = var_subject < tol * fit.scale
    if structure == "subject+location":
        small = small or float(fit.vcomp[0]) < tol * fit.scale
    return small


def select_model(df, y, factors):
    """Model selection of model_select(): random structure from the main-effects model (dropping
    subject:location, then subject, when singular), lowest AIC of the eight models (ML), then
    comparisons of the selected model with the simplest and the full model. The paper uses
    Kenward-Roger F tests (lmer) or F tests (lm); likelihood-ratio tests are used here for the
    mixed models (a stated deviation)."""
    from scipy.stats import chi2
    d = df.dropna(subset=[y]).copy()
    forms = [f"{y} ~ {r}" for r in _formulas(factors)]
    structure = "subject+location"
    def singular(structure):
        try:
            return _singular(_fit_mixed(forms[0], d, structure, True), structure)
        except np.linalg.LinAlgError:
            return True
    if singular(structure):
        structure = "subject"
        if singular(structure):
            structure = "ols"
    order = ["subject+location", "subject", "ols"]
    while True:
        try:
            fits = [_fit_mixed(f, d, structure, False) for f in forms]
            break
        except np.linalg.LinAlgError:
            # a model that cannot be fitted with this random structure: simplify it, as for a
            # singular fit
            structure = order[order.index(structure) + 1]
    aic = [f.aic if structure == "ols" else (-2 * f.llf + 2 * (len(f.fe_params) + len(f.cov_re) + len(np.atleast_1d(f.vcomp)) + 1)) for f in fits]
    sel = int(np.nanargmin(aic))

    def lr_p(big, small):
        if structure == "ols":
            from statsmodels.stats.anova import anova_lm
            return float(anova_lm(fits[small], fits[big])["Pr(>F)"].iloc[1])
        stat = 2 * (fits[big].llf - fits[small].llf)
        dfree = len(fits[big].fe_params) - len(fits[small].fe_params)
        return float(chi2.sf(stat, dfree)) if dfree > 0 else 1.0

    if sel == 0:
        chosen = 7 if lr_p(7, 0) < 0.05 else 0
    elif sel == 7:
        chosen = 7 if lr_p(7, 0) < 0.05 else 0
    else:
        p1, p2 = lr_p(7, sel), lr_p(sel, 0)
        if p1 > 0.05 and p2 < 0.05:
            chosen = sel
        elif p1 < 0.05 and p2 < 0.05:
            chosen = 7
        elif p1 > 0.05 and p2 > 0.05:
            chosen = 0
        else:
            chosen = 7 if lr_p(7, 0) < 0.05 else 0
    return {"data": d, "formula": forms[chosen], "structure": structure, "model": chosen,
            "aic_best": sel}


def _design(formula, d, grid):
    import patsy
    rhs = formula.split("~", 1)[1]
    X = patsy.dmatrix(rhs, d, return_type="dataframe")
    G = patsy.build_design_matrices([X.design_info], grid, return_type="dataframe")[0]
    return X.values, G.values


def case_bootstrap(sel, factors, levels, B=10000, seed=0):
    """Case bootstrap over subjects (lmeresampler resample = c(TRUE, FALSE, ...)), refitting the
    fixed effects of the selected model by generalized least squares with the variance components
    of the original fit held fixed (the paper refits lmer each time; a stated deviation). Returns
    cell predictions (grid rows) for the full data and for each replicate."""
    import itertools
    d = sel["data"]
    y = sel["formula"].split("~")[0].strip()
    grid = pd.DataFrame(list(itertools.product(*[levels[f] for f in factors])), columns=list(factors))
    X, G = _design(sel["formula"], d, grid)
    yv = d[y].values
    subj = d["subject"].values
    subjects = np.unique(subj)
    if sel["structure"] == "ols":
        var_e, var_s, var_l = 1.0, 0.0, 0.0
    else:
        try:
            fit = _fit_mixed(sel["formula"], d, sel["structure"], True)
        except np.linalg.LinAlgError:
            fit = _fit_mixed(sel["formula"], d, sel["structure"], False)
        var_e = fit.scale
        var_s = float(np.asarray(fit.cov_re)[0, 0])
        var_l = float(np.atleast_1d(fit.vcomp)[0]) if sel["structure"] == "subject+location" else 0.0
    p = X.shape[1]
    XtX = np.zeros((len(subjects), p, p))
    Xty = np.zeros((len(subjects), p))
    for i, s in enumerate(subjects):
        ix = subj == s
        loc = d["location"].values[ix]
        V = var_e * np.eye(ix.sum()) + var_s + var_l * (loc[:, None] == loc[None, :])
        Vi = np.linalg.inv(V)
        XtX[i] = X[ix].T @ Vi @ X[ix]
        Xty[i] = X[ix].T @ Vi @ yv[ix]
    beta = np.linalg.solve(XtX.sum(0), Xty.sum(0))
    rng = np.random.default_rng(seed)
    S = len(subjects)
    counts = np.stack([np.bincount(rng.integers(0, S, S), minlength=S) for _ in range(B)])
    A = np.einsum("bs,spq->bpq", counts, XtX)
    c = counts @ Xty
    ok = np.linalg.cond(A) < 1e10
    betas = np.full((B, p), np.nan)
    betas[ok] = np.linalg.solve(A[ok], c[ok][..., None])[..., 0]
    return grid, G @ beta, betas @ G.T, int((~ok).sum())


def contrast(grid, est, boot, a, b):
    """Estimate, 95% percentile interval and p = 2 (1 - pd) of cell a minus cell b (dicts of
    factor levels)."""
    def row(cond):
        m = np.ones(len(grid), bool)
        for k, v in cond.items():
            m &= grid[k].values == v
        assert m.sum() == 1
        return np.where(m)[0][0]
    i, j = row(a), row(b)
    e = est[i] - est[j]
    bt = boot[:, i] - boot[:, j]
    bt = bt[np.isfinite(bt)]
    pd_ = max(np.mean(bt > 0), np.mean(bt < 0))
    return {"estimate": float(e), "lo": float(np.percentile(bt, 2.5)), "hi": float(np.percentile(bt, 97.5)),
            "p": float(2 * (1 - pd_))}


def run_test(df, y, factors, levels, B=10000, seed=0):
    sel = select_model(df, y, factors)
    grid, est, boot, dropped = case_bootstrap(sel, factors, levels, B=B, seed=seed)
    return {"sel": sel, "grid": grid, "est": est, "boot": boot, "dropped": dropped, "n": len(sel["data"]),
            "n_subjects": sel["data"]["subject"].nunique()}


def run_all(jobs, workers=4):
    """analyse() over jobs in parallel processes, one linear-algebra thread each."""
    from concurrent.futures import ProcessPoolExecutor
    import multiprocessing as mp
    for k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
        os.environ[k] = "1"
    ctx = mp.get_context("spawn")
    with ProcessPoolExecutor(workers, mp_context=ctx) as ex:
        return list(ex.map(analyse, jobs, chunksize=1))


# ---------------------------------------------------------------- Figure S9 histology

def histology_tables():
    """The neuropil (Sorted-ForMultilevel) and perisomatic (Somatic_input_ForMultilevel) sheets of
    the repository's P15_VGAT_SYT2_20230318.xlsx, with short column names."""
    neu = pd.read_excel(HISTO_TABLE, sheet_name="Sorted-ForMultilevel")
    som = pd.read_excel(HISTO_TABLE, sheet_name="Somatic_input_ForMultilevel")
    def find(df, *words):
        cols = [c for c in df.columns if all(w in str(c) for w in words)]
        assert len(cols) == 1, (words, cols)
        return cols[0]
    n = pd.DataFrame({
        "subject": neu["Animal ID"], "sex": neu["Sex"], "layer": neu["Layer"].astype(str),
        "location": neu["Image_number"],
        "vgat": neu[find(neu, "Density (#/100 um^3) VGAT")],
        "syt2": neu[find(neu, "Density (#/100 um^3) Syt2")],
        "vgat_syt2": neu[find(neu, "colocalized signal", "VGA")]}).dropna(subset=["subject"])
    s = pd.DataFrame({
        "subject": som["Animal ID"], "sex": som["Sex"], "layer": som["Layer"].astype(str),
        "location": som["Image_number"], "soma_volume": som[find(som, "Soma_Volum")],
        "vgat_on_soma": som["VGAT+  punctate # on soma"],
        "vgat_syt2_on_soma_norm": som[find(som, "VGAT+ and Syt2+ punctate # on soma_normalized")]}).dropna(subset=["subject"])
    return n, s


def histology_test(df, y, B=10000, seed=0):
    """The Figure S9 model of VGAT_Syt2_Function_20230319.R (model_select): y ~ layer * sex with
    random intercepts for animal and animal by image, dropped when singular, then a case bootstrap
    over animals, as case_bootstrap above."""
    d = df.dropna(subset=[y]).copy()
    formula = f"{y} ~ C(layer) * C(sex)"
    structure = "subject+location"
    def singular(st):
        try:
            return _singular(_fit_mixed(formula, d, st, True), st)
        except np.linalg.LinAlgError:
            return True
    if singular(structure):
        structure = "subject"
        if singular(structure):
            structure = "ols"
    sel = {"data": d, "formula": formula, "structure": structure}
    levels = {"layer": sorted(d.layer.unique()), "sex": ["F", "M"]}
    grid, est, boot, dropped = case_bootstrap(sel, ("layer", "sex"), levels, B=B, seed=seed)
    return {"grid": grid, "est": est, "boot": boot, "dropped": dropped, "structure": structure,
            "n": len(d), "n_subjects": d.subject.nunique()}


def averaged_contrast(r, factor, a, b):
    """Contrast a minus b of one factor, averaged over the levels of the other (emmeans' default)."""
    g = r["grid"]
    other = [c for c in g.columns if c != factor][0]
    est, bt = 0.0, 0.0
    levels = sorted(g[other].unique())
    for lv in levels:
        i = np.where((g[factor] == a) & (g[other] == lv))[0][0]
        j = np.where((g[factor] == b) & (g[other] == lv))[0][0]
        est = est + (r["est"][i] - r["est"][j]) / len(levels)
        bt = bt + (r["boot"][:, i] - r["boot"][:, j]) / len(levels)
    bt = bt[np.isfinite(bt)]
    pd_ = max(np.mean(bt > 0), np.mean(bt < 0))
    return {"estimate": float(est), "lo": float(np.percentile(bt, 2.5)), "hi": float(np.percentile(bt, 97.5)),
            "p": float(2 * (1 - pd_))}
