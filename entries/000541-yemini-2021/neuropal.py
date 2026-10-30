"""Loading and measures for the whole-brain GCaMP6s recordings of dandiset 000541.

Yemini, Lin, Nejatbakhsh et al. (2021), NeuroPAL, Cell 184, 272-288, doi:10.1016/j.cell.2020.12.012.

Each NWB file holds one OH16230 head: a NeuroPAL identification volume, a single-channel GCaMP6s
movie at 4 Hz, the dNMF trace of every segmented neuron (`SignalRawFluordNMF`), the neuron names
(`NeuronIDs/labels`, one per trace, empty when unidentified), the neuron centres at the first
frame (`CalciumSeriesSegmentation/Seg_tpoint_0`, one voxel per neuron) and the three 10 s
stimuli (`intervals/chemical_stimuli`). Files are streamed from the archive at the pinned version;
nothing is written to disk.

Where the parameters come from:

- Trace processing, STAR Methods, "Brainwide imaging of neuronal activity traces": the first 1 s
  and the last frame of every recording are removed (`TRIM_START_S`); dF is the trace minus a
  fitted first-order exponential decay a*exp(b*t) ("we approximated the GCaMP6s bleach curve by
  fitting a 1st order exponential decay to each neuron"); F0 is the 5th percentile of the trace;
  neurons within 5 um of each other whose traces correlate at 0.95 or more are removed
  (`DUP_DIST_UM`, `DUP_CORR`); neurons with N <= 3 animals are not evaluated (`MIN_N`). Which
  member of a near-duplicate pair is removed is not stated. The main reading removes one member
  of each pair ("one", an assumption): of the four readings run, it comes closest to the
  per-class sample counts of the paper's Table S6 (shown in the notebook). Removing both
  members, none, or exactly the named traces that the paper's own deposit of these heads
  (Zenodo 3906530) lacks ("deposit") are variants. Distances use the calcium voxel coordinates scaled
  to micrometres with the NeuroPAL volume's spacing and the fitted ratio of the two volumes'
  coordinates (`calcium_to_neuropal_scale`), as the calcium volume's stated spacing does not fit
  its coordinates. The normalisation "when comparing neuronal activity across animals" is
  below.
- Normalisation before the response tests (`normalise`): the STAR Methods say "When comparing
  neuronal activity across animals, we used dNMF to normalize activity traces per neuron class"
  without saying how. The paper's Table S6 (per-class p values and 95% confidence intervals) is
  matched far better by tests on traces scaled one by one than on dF/F0 (shown in the notebook);
  the z-score of each trace is the main reading (an assumption), dF/F0 and min-max scaling are
  variants. A scale common to a class cannot change a paired t-test, so only a per-trace scale
  matters.
- Response tests, STAR Methods, "Analysis of brainwide imaging data": premotor interneurons (AVA,
  AVB, AVD, AVE, PVC) and ventral-cord motor neurons (AS, DA, DB, DD, VA, VB, VC, VD) are excluded
  (`EXCLUDED_CLASSES`, `MOTOR_PREFIXES`), and so are the two named cells that are not neurons
  (`NON_NEURONS`, absent from the paper's deposit); left and right neurons of a class are
  pooled; two-tailed paired t-test of the mean during the 10 s stimulus against the identical period immediately
  before (`PRE_S`); p values corrected with Storey (2002) q values, over the tests of all three
  stimuli together (Table S6 legend: "FDR was used to correct the p-values of all NaCl,
  2-butanone, and 2,3-pentanedione stimulus responses together"); significance at p or q <=
  0.05 (STAR Methods, "Statistical analysis").
- The Storey q values follow Storey (2002) with the bootstrap choice of lambda of Storey, Taylor
  and Siegmund (2004), lambda in 0.01 to 0.95 (`storey_q`). MATLAB's mafdr, the software the
  paper names ("All statistics and code were run in MATLAB"), uses this procedure by default.
  The bootstrap seed (0) is a standard choice, but it can move pi0, as the bootstrap picks one
  lambda from many: the notebook prints pi0 over ten seeds, checks the q values on the paper's
  own p values against its q values (Table S6), and adds Benjamini-Hochberg as a conservative
  check.
- AWC colors: the median of each NeuroPAL channel over a 5 x 5 pixel patch (1.3 um square) at
  the AWCL and AWCR centres of the NeuroPAL segmentation (`AWC_PATCH_PX`), a standard choice;
  the paper says srsx-3 colors AWC OFF in NeuroPAL (Results, Whole-Brain Activity Imaging).
- Class names: a name ending in L or R whose mirror name also occurs is a left/right member of
  the class without that letter (ASEL -> ASE); others are their own class (AVL, RIR, RMED).
  This matches the class list of the paper's Zenodo deposit.
"""

from __future__ import annotations

import re
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import remfile
import requests
from scipy import optimize, stats

DANDISET_ID = "000541"
DANDISET_VERSION = "0.241009.1457"
API = "https://api.dandiarchive.org/api"

RATE_HZ = 4.0
TRIM_START_S = 1.0          # STAR Methods: first 1 s removed
PRE_S = 10.0                # identical period immediately before the 10 s stimulus
DUP_DIST_UM = 5.0
DUP_CORR = 0.95
MIN_N = 3                   # classes with N <= 3 animals are not evaluated
EXCLUDED_CLASSES = {"AVA", "AVB", "AVD", "AVE", "PVC"}
MOTOR_PREFIXES = ("AS", "DA", "DB", "DD", "VA", "VB", "VC", "VD")
NON_NEURONS = {"AMSO", "HMC"}  # amphid sheath glia and the head mesodermal cell, named in the files
AWC_PATCH_PX = 2            # 5 x 5 pixel patch of the NeuroPAL volume around each AWC centre
STIMULI = ("nacl", "butanone", "pentanedione")


def list_assets(version: str = DANDISET_VERSION) -> list[dict]:
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{version}/assets/?page_size=200"
    r = requests.get(url, timeout=60)
    r.raise_for_status()
    return sorted(r.json()["results"], key=lambda a: a["path"])


def _s(x):
    return x.decode() if isinstance(x, bytes) else x


def load_head(asset: dict) -> dict:
    """Stream one file and keep what the analysis uses."""
    url = f"{API}/assets/{asset['asset_id']}/download/"
    with h5py.File(remfile.File(url), "r") as f:
        ca = f["processing/CalciumActivity"]
        ser = ca["SignalRawFluordNMF/dNMFCalciumImResponseSeries"]
        raw = ser["data"][()]
        raw_other = ca["SignalRawFluor/SignalCalciumImResponseSeries/data"][()]
        st = f["intervals/chemical_stimuli"]
        seg = ca["CalciumSeriesSegmentation/Seg_tpoint_0"]
        vm = seg["voxel_mask"][()]
        vi = seg["voxel_mask_index"][()]
        gs = f["general/optophysiology/CalciumImVol/grid_spacing"][()]
        starts = np.r_[0, vi[:-1]]
        centre_px = np.array([[vm[s:e][c].astype(float).mean() for c in ("x", "y", "z")]
                              for s, e in zip(starts, vi)])
        npn = f["processing/NeuroPAL/NeuroPALSegmentation/NeuroPALNeurons"]
        idl = [_s(x) for x in npn["ID_labels"][()]]
        ii = npn["ID_labels_index"][()]
        np_labels = ["".join(idl[s:e]) for s, e in zip(np.r_[0, ii[:-1]], ii)]
        nvm = npn["voxel_mask"][()]
        np_px = np.c_[nvm["x"], nvm["y"], nvm["z"]].astype(float)
        np_gs = f["general/optophysiology/NeuroPALImVol/grid_spacing"][()]
        img = f["acquisition/NeuroPALImageRaw/data"]
        channels = [_s(x) for x in f["general/optophysiology/NeuroPALImVol/order_optical_channels/channels"][()]]
        awc_color = {}
        for n in ("AWCL", "AWCR"):
            if np_labels.count(n) == 1:
                x, y, z = np_px[np_labels.index(n)].astype(int)
                patch = img[max(x - AWC_PATCH_PX, 0):x + AWC_PATCH_PX + 1,
                            max(y - AWC_PATCH_PX, 0):y + AWC_PATCH_PX + 1, z, :].astype(float)
                awc_color[n] = dict(zip(channels, np.median(patch.reshape(-1, patch.shape[-1]), axis=0)))
        sub = f["general/subject"]
        rec = {
            "path": asset["path"],
            "identifier": _s(f["identifier"][()]),
            "session_description": _s(f["session_description"][()]),
            "strain": _s(sub["strain"][()]),
            "growth_stage": _s(sub["growth_stage"][()]),
            "labels": [_s(x) for x in ca["NeuronIDs/labels"][()]],
            "raw": raw,
            "raw_equals_other_series": bool(np.array_equal(raw, raw_other, equal_nan=True)),
            "rate": float(ser["starting_time"].attrs["rate"]),
            "t0": float(ser["starting_time"][()]),
            "unit": _s(ser["data"].attrs["unit"]),
            "n_movie_frames": int(f["acquisition/CalciumImageSeries/data"].shape[0]),
            "centre_px": centre_px,
            "grid_spacing_um": gs,
            "neuropal_labels": np_labels,
            "neuropal_px": np_px,
            "neuropal_grid_spacing_um": np_gs,
            "neuropal_shape": img.shape,
            "movie_shape": f["acquisition/CalciumImageSeries/data"].shape,
            "awc_color": awc_color,
            "subject_description": _s(sub["description"][()]),
            "stimuli": {_s(st["stimulus"][i]): (float(st["start_time"][i]), float(st["stop_time"][i]))
                        for i in range(len(st["id"]))},
            "stim_description": _s(st.attrs["description"]),
        }
    rec["xyz_scale"] = calcium_to_neuropal_scale(rec)
    # The calcium volume's own grid spacing equals the NeuroPAL volume's, but its x and y voxel
    # coordinates are half those of the same neurons in the NeuroPAL volume (the movie is 256 x 128
    # pixels against 512 x 256): the movie is binned, and its spacing is the NeuroPAL spacing times
    # the fitted scale, rounded (checked per file in the notebook).
    rec["centre_um"] = centre_px * np_gs * np.round(rec["xyz_scale"])
    return rec


def calcium_to_neuropal_scale(rec: dict) -> np.ndarray:
    """Per axis, the slope of the NeuroPAL voxel coordinate on the calcium voxel coordinate of the same
    neuron (names found once in both segmentations)."""
    lab, nl = rec["labels"], rec["neuropal_labels"]
    common = [n for n in lab if n and lab.count(n) == 1 and nl.count(n) == 1]
    c = rec["centre_px"][[lab.index(n) for n in common]]
    p = rec["neuropal_px"][[nl.index(n) for n in common]]
    return np.array([np.polyfit(c[:, k], p[:, k], 1)[0] for k in range(3)])


def load_all(workers: int = 8) -> list[dict]:
    assets = list_assets()
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(load_head, assets))


# ---------------------------------------------------------------- names

def class_maps(all_names: set[str]) -> dict[str, str]:
    """Neuron name -> class name (left and right pooled)."""
    out = {}
    for n in all_names:
        if len(n) > 2 and n[-1] in "LR":
            mirror = n[:-1] + ("R" if n[-1] == "L" else "L")
            if mirror in all_names:
                out[n] = n[:-1]
                continue
        out[n] = n
    return out


def excluded_from_tests(cls: str) -> bool:
    if cls in EXCLUDED_CLASSES or cls in NON_NEURONS:
        return True
    return any(re.fullmatch(p + r"\d+", cls) for p in MOTOR_PREFIXES)


# ---------------------------------------------------------------- traces

def dff(raw: np.ndarray, rate: float = RATE_HZ) -> np.ndarray:
    """dF/F0 per column, STAR Methods. First 1 s set to NaN, last frame dropped."""
    x = raw[:-1].astype(float)
    n0 = int(round(TRIM_START_S * rate))
    t = np.arange(len(x)) / rate
    out = np.full_like(x, np.nan)
    for j in range(x.shape[1]):
        y = x[n0:, j]
        if not np.all(np.isfinite(y)):
            continue
        tt = t[n0:]
        try:
            (a, b), _ = optimize.curve_fit(lambda s, a, b: a * np.exp(b * s), tt, y,
                                           p0=(y[: int(5 * rate)].mean(), -1e-3), maxfev=20000)
            bleach = a * np.exp(b * tt)
        except RuntimeError:
            bleach = np.full_like(y, y.mean())
        out[n0:, j] = (y - bleach) / np.percentile(y, 5)
    return out


def near_duplicates(rec: dict, d: np.ndarray, mode: str = "both") -> set[int]:
    """Indices of named neurons within DUP_DIST_UM of another whose traces correlate >= DUP_CORR.

    mode "both" removes both members of each pair; "one" (the main reading) removes, pair by
    pair, the later neuron in the file's order unless one of the two is already removed.
    """
    idx = [i for i, n in enumerate(rec["labels"]) if n and np.all(np.isfinite(d[4:, i]))]
    xyz = rec["centre_um"][idx]
    c = np.corrcoef(d[4:, idx].T)
    dist = np.linalg.norm(xyz[:, None] - xyz[None], axis=-1)
    bad = set()
    for a in range(len(idx)):
        for b in range(a + 1, len(idx)):
            if dist[a, b] <= DUP_DIST_UM and c[a, b] >= DUP_CORR:
                if mode == "both":
                    bad.update((idx[a], idx[b]))
                elif idx[a] not in bad and idx[b] not in bad:
                    bad.add(idx[b])
    return bad


def prepare(recs: list[dict], dup_mode: str = "both", deposit=None, dffs: dict | None = None) -> dict:
    """dF/F0 traces by animal, with near-duplicate and empty traces removed (dup_mode "none" keeps
    them; "deposit" removes the named traces that the paper's deposit lacks, `deposit` being the
    set of (file, name) it holds). `dffs` gives dF/F0 per file identifier, computed once."""
    names = {n for r in recs for n in r["labels"] if n}
    cmap = class_maps(names)
    animals = []
    for r in recs:
        d = dffs[r["identifier"]] if dffs is not None else dff(r["raw"], r["rate"])
        if dup_mode == "none":
            dup = set()
        elif dup_mode == "deposit":
            dup = {i for i, n in enumerate(r["labels"]) if n and (r["identifier"], n) not in deposit}
        else:
            dup = near_duplicates(r, d, dup_mode)
        keep = {}
        dropped_nan = []
        for i, n in enumerate(r["labels"]):
            if not n or i in dup:
                continue
            if not np.all(np.isfinite(d[4:, i])):
                dropped_nan.append(n)
                continue
            keep[n] = d[:, i]
        animals.append({
            "id": r["identifier"], "traces": keep, "stimuli": r["stimuli"], "rate": r["rate"],
            "duplicates": sorted(r["labels"][i] for i in dup), "dropped_nan": dropped_nan,
            "unnamed": sum(1 for n in r["labels"] if not n),
        })
    return {"animals": animals, "class_of": cmap}


def window_means(trace: np.ndarray, start: float, stop: float, rate: float = RATE_HZ):
    """Mean during [start, stop) and during the identical period before it."""
    t = np.arange(len(trace)) / rate
    dur = stop - start
    during = trace[(t >= start) & (t < stop)].mean()
    before = trace[(t >= start - dur) & (t < start)].mean()
    return during, before


def normalise(trace: np.ndarray, how: str = "zscore") -> np.ndarray:
    """Per-trace scaling before the response tests: "zscore" (mean 0, SD 1), "minmax" (0 to 1), or
    "raw" (dF/F0 unchanged). Statistics over the frames after the first 1 s."""
    x = trace[int(round(TRIM_START_S * RATE_HZ)):]
    if how == "zscore":
        return (trace - x.mean()) / x.std()
    if how == "minmax":
        return (trace - x.min()) / (x.max() - x.min())
    return trace


def responses(data: dict, stimulus: str, norm: str = "zscore") -> list[dict]:
    """One row per animal and named neuron: means during and before the stimulus."""
    rows = []
    for a in data["animals"]:
        s0, s1 = a["stimuli"][stimulus]
        for n, tr in a["traces"].items():
            tr = normalise(tr, norm)
            dur, pre = window_means(tr, s0, s1, a["rate"])
            post, _ = window_means(tr, s1, s1 + (s1 - s0), a["rate"])
            post20, _ = window_means(tr, s1, s1 + 2 * (s1 - s0), a["rate"])
            rows.append({"animal": a["id"], "neuron": n, "cls": data["class_of"][n],
                         "stimulus": stimulus, "during": dur, "before": pre,
                         "post10": post, "post20": post20})
    return rows


def class_tests(rows: list[dict]) -> dict:
    """Two-tailed paired t-test per class (left and right pooled), STAR Methods."""
    by = {}
    for r in rows:
        by.setdefault(r["cls"], []).append(r)
    out = {}
    for c, rr in by.items():
        n_animals = len({r["animal"] for r in rr})
        if excluded_from_tests(c) or n_animals <= MIN_N:
            continue
        d = np.array([r["during"] for r in rr])
        b = np.array([r["before"] for r in rr])
        res = stats.ttest_rel(d, b)
        out[c] = {"n_traces": len(rr), "n_animals": n_animals, "mean_diff": float(np.mean(d - b)),
                  "t": float(res.statistic), "p": float(res.pvalue)}
    return out


# ---------------------------------------------------------------- FDR

def storey_pi0(p: np.ndarray, seed: int = 0, n_boot: int = 1000) -> float:
    """pi0 of Storey (2002), lambda chosen by bootstrap (Storey, Taylor & Siegmund 2004)."""
    p = np.asarray(p)
    m = len(p)
    lams = np.arange(0.01, 0.951, 0.01)
    lams = lams[[np.any(p > lam) for lam in lams]]   # a lambda above every p gives pi0 = 0
    pi0 = np.array([np.mean(p > lam) / (1 - lam) for lam in lams])
    rng = np.random.default_rng(seed)
    boot = np.empty((n_boot, len(lams)))
    for k in range(n_boot):
        pb = rng.choice(p, m, replace=True)
        boot[k] = [np.mean(pb > lam) / (1 - lam) for lam in lams]
    mse = np.mean((boot - pi0.min()) ** 2, axis=0)
    return float(min(1.0, pi0[np.argmin(mse)]))


def storey_q(p, seed: int = 0) -> np.ndarray:
    p = np.asarray(p, float)
    m = len(p)
    pi0 = storey_pi0(p, seed)
    order = np.argsort(p)
    q = np.empty(m)
    prev = 1.0
    for rank in range(m, 0, -1):
        i = order[rank - 1]
        prev = min(prev, pi0 * m * p[i] / rank)
        q[i] = prev
    return q


def bh_q(p) -> np.ndarray:
    p = np.asarray(p, float)
    m = len(p)
    order = np.argsort(p)
    q = np.empty(m)
    prev = 1.0
    for rank in range(m, 0, -1):
        i = order[rank - 1]
        prev = min(prev, m * p[i] / rank)
        q[i] = prev
    return q


# ---------------------------------------------------------------- AVF cycles

def medfilt_matlab(x: np.ndarray, n: int) -> np.ndarray:
    """MATLAB medfilt1(x, n): y(k) = median(x(k - floor(n/2) : k + ceil(n/2) - 1)), zero padded."""
    lo, hi = n // 2, n - n // 2 - 1
    xp = np.r_[np.zeros(lo), x, np.zeros(hi)]
    return np.array([np.median(xp[k:k + n]) for k in range(len(x))])


# ---------------------------------------------------------------- outside inputs

ZENODO_URL = "https://zenodo.org/api/records/3906530/files/NeuroPAL%20data.zip/content"
ZENODO_HEADS = "Whole-Brain Calcium Activity/Young Adults/Head_Activity_OH16230.mat"
# Cook et al. (2019), Nature 571, 63-71, doi:10.1038/s41586-019-1352-7, Supplementary Information.
# MOESM6 is "number of scored synapses between pairs of cells" (synapse counts, the measure the
# Results name); MOESM9 is SI 5, the connectome adjacency matrices weighted by synapse size.
COOK_SYNAPSE_COUNTS = ("https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-019-1352-7/"
                       "MediaObjects/41586_2019_1352_MOESM6_ESM.xlsx")
COOK_ADJACENCY = ("https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-019-1352-7/"
                  "MediaObjects/41586_2019_1352_MOESM9_ESM.xlsx")


def load_zenodo_heads() -> dict:
    """The paper's own deposit of the head traces (Zenodo 3906530), read from the zip in place."""
    import io
    import zipfile

    import fsspec
    import scipy.io as sio

    with fsspec.open(ZENODO_URL, block_size=2 ** 22).open() as fh:
        with zipfile.ZipFile(fh) as z:
            raw = z.read(ZENODO_HEADS)
    return sio.loadmat(io.BytesIO(raw), squeeze_me=True)


def zenodo_traces_by_file(m: dict) -> dict:
    """{class: (traces, is_L)} from the deposit's layout: per class, left traces then right
    traces, each in file order (README of the deposit), one slot per file, NaN where the file
    lacks the neuron."""
    out = {}
    for i, cls in enumerate(m["neurons"]):
        tr = list(m["traces"][i]) if np.ndim(m["traces"][i]) == 1 and len(m["traces"][i]) and \
            np.ndim(m["traces"][i][0]) == 1 else [m["traces"][i]]
        is_l = np.atleast_1d(np.asarray(m["is_L"][i], float))
        out[str(cls)] = (tr, is_l)
    return out


def deposit_slots(m: dict) -> dict:
    """{(file identifier, neuron name): deposit trace}, for every slot of the deposit that holds a
    trace. Files are named as in the dandiset (deposit 0924_01 is 20190924_01)."""
    files = ["2019" + str(f) for f in m["files"]]
    out = {}
    for cls, (trs, is_l) in zenodo_traces_by_file(m).items():
        if np.all(np.isnan(is_l)):
            groups = [(cls, list(range(len(trs))))]
        else:
            groups = [(cls + "L", [k for k in range(len(trs)) if is_l[k] == 1]),
                      (cls + "R", [k for k in range(len(trs)) if is_l[k] == 0])]
        for name, ks in groups:
            if len(ks) != len(files):
                continue
            for f, k in zip(files, ks):
                z = np.asarray(trs[k], float)
                if np.isfinite(z).any():
                    out[(f, name)] = z
    return out


# The paper's supplementary tables, from the publisher's server (doi:10.1016/j.cell.2020.12.012):
# Table S1 (reporters and their fluorophores) and Table S6 (per-class response statistics).
TABLE_S1 = "https://ars.els-cdn.com/content/image/1-s2.0-S0092867420316822-mmc3.xlsx"
TABLE_S6 = "https://ars.els-cdn.com/content/image/1-s2.0-S0092867420316822-mmc8.xlsx"


def _excel(url: str, sheet: str, header):
    import io

    import pandas as pd

    r = requests.get(url, timeout=120)
    r.raise_for_status()
    return pd.read_excel(io.BytesIO(r.content), sheet_name=sheet, header=header)


def load_table_s6():
    """Table S6, sheet "OH16230 Heads": one row per class with Samples, L/R Samples and, per
    stimulus, the 95% CI, p and q of the response."""
    import pandas as pd

    t = _excel(TABLE_S6, "OH16230 Heads", 0)
    t = t[pd.to_numeric(t["Samples"], errors="coerce").notna()]
    return t.set_index("Neuron")


def reporter_fluorophore(gene: str) -> str:
    """The NeuroPAL fluorophore of a reporter, from Table S1, sheet "NeuroPAL Reporters-Fluorophores"
    (row 2 names the fluorophore over a block of columns, row 3 the reporters)."""
    t = _excel(TABLE_S1, "NeuroPAL Reporters-Fluorophores", None)
    fluor = t.iloc[1].ffill()
    cols = [j for j, v in enumerate(t.iloc[2]) if str(v).strip() == gene]
    return "; ".join(str(fluor.iloc[j]) for j in cols)


def load_cook(url: str = COOK_SYNAPSE_COUNTS, chem_sheet: str = "herm chem synapse adjacency",
              gap_sheet: str = "herm gap jn synapse adjacency"):
    """Hermaphrodite chemical and gap-junction matrices as DataFrames indexed by cell name."""
    import io

    import pandas as pd

    r = requests.get(url, timeout=120)
    r.raise_for_status()
    out = []
    for sheet in (chem_sheet, gap_sheet):
        d = pd.read_excel(io.BytesIO(r.content), sheet_name=sheet, header=None)
        cols = d.iloc[2, 3:]
        rows = d.iloc[3:, 2]
        keep_c = cols.notna().values
        keep_r = rows.notna().values
        mat = d.iloc[3:, 3:].loc[keep_r, keep_c].apply(pd.to_numeric, errors="coerce").fillna(0)
        # Cook et al. pad motor neuron numbers (VA01); the dandiset does not (VA1).
        mat.index = [re.sub(r"^([A-Z]+)0(\d)$", r"\1\2", str(x).strip()) for x in rows[keep_r]]
        mat.columns = [re.sub(r"^([A-Z]+)0(\d)$", r"\1\2", str(x).strip()) for x in cols[keep_c]]
        mat = mat.groupby(level=0).sum().T.groupby(level=0).sum().T
        names = sorted(set(mat.index) | set(mat.columns))
        out.append(mat.reindex(index=names, columns=names, fill_value=0))
    return out[0], out[1]
