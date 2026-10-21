"""Loading dandiset 000008 (Scala, Kobak et al. 2021) and extracting the paper's features.

The dandiset holds one NWB file per Patch-seq cell: the membrane voltage of each current step
(acquisition), the injected current (stimulus/presentation, absent for the 0 pA step), the
subject, and a `DandiIcephysMetadata` group with the cell's t-type (`RNA_type`), family
(`RNA_family`), layers, cortical thickness and read counts.

Choices made here, and where they come from:

- The version is pinned to 0.211014.0809, the latest published one (the paper cites none).
- Files are read over HTTPS into memory, whole, and opened with h5py; nothing is written to disk.
  Reading through `remfile` worked but took about 6 s per file, too slow for 1,328 files; the
  whole file is about 9 MB. This is a choice of transport, not of method.
- Features are extracted with the paper's own code, fetched from the mini-atlas repository at
  commit 3bf98a524b8e48aa8647e1b9ae8f2351d9c712c9 (claims, ed4-example-cell): the modules
  `ephys_extractor.py` and `ephys_features.py`, and the functions `extract_spike_features`
  (cell 16) and `get_cell_features` (cell 20) of `preprocess-ephys-files.ipynb`, executed as
  they are. Two names that newer numpy and scipy removed are restored as aliases with the
  same behaviour (`np.float` is `float`, `integrate.cumtrapz` is
  `scipy.integrate.cumulative_trapezoid`).
- The traces and currents are arranged as the code's `get_time_voltage_current_currindex0`
  does: voltage traces in sweep order, currents from the first stimulus value (sample 12000)
  upwards in 20 pA steps, the 0 pA trace at index 10. `read_cell` also returns each stimulus
  as recorded, so that this arrangement can be checked against the files.
- The rheobase uses scikit-learn's RANSACRegressor with no fixed seed in the paper's code; the
  global numpy seed is set to 0 before each cell (a standard choice for a random seed; it
  cannot change a feature beyond the RANSAC fit).
- The 17 features, the log transform, the ephys representation, the kNN classifier, the
  normalized variances and the Leiden entropies follow the claims file's criteria, which cite
  the Methods and the code (phenotype-tsne.ipynb); see each function.
"""

from __future__ import annotations

import io
import json
import time
import types
import warnings
from concurrent.futures import ProcessPoolExecutor

import numpy as np
import pandas as pd
import requests

DANDISET = "000008"
VERSION = "0.211014.0809"
API = "https://api.dandiarchive.org/api"
MINI_ATLAS = "https://raw.githubusercontent.com/berenslab/mini-atlas/3bf98a524b8e48aa8647e1b9ae8f2351d9c712c9"

# Feature names as the paper's code writes them (get_cell_features).
FEATURES_29 = ['Resting membrane potential (mV)', 'Input resistance (MOhm)', 'Membrane time constant (ms)',
               'AP threshold (mV)', 'AP amplitude (mV)', 'AP width (ms)',
               'Upstroke-to-downstroke ratio', 'Afterhyperpolarization (mV)', 'Afterdepolarization (mV)',
               'ISI adaptation index', 'Max number of APs', 'Rheobase (pA)', 'Sag ratio',
               'Latency (ms)', 'Latency @ +20pA current (ms)', 'Spike frequency adaptation',
               'ISI Fano factor', 'ISI coefficient of variation',
               'ISI average adaptation index', 'Rebound (mV)', 'Sag time (s)', 'Sag area (mV*s)',
               'AP amplitude adaptation index', 'AP amplitude average adaptation index',
               'AP Fano factor', 'AP coefficient of variation', 'Burstiness', 'Wildness', 'Rebound number of APs']
# The 12 features left out of all statistics (Methods; code phenotype-tsne.ipynb, features_exclude).
FEATURES_EXCLUDED = ['Afterdepolarization (mV)', 'AP Fano factor', 'ISI Fano factor',
                     'Latency @ +20pA current (ms)', 'Wildness', 'Spike frequency adaptation',
                     'Sag area (mV*s)', 'Sag time (s)', 'Burstiness',
                     'AP amplitude average adaptation index', 'ISI average adaptation index',
                     'Rebound number of APs']
FEATURES_17 = [f for f in FEATURES_29 if f not in FEATURES_EXCLUDED]
# Log-transformed features (Methods; code phenotype-tsne.ipynb, features_log).
FEATURES_LOG = ['AP coefficient of variation', 'ISI coefficient of variation',
                'ISI adaptation index', 'Latency (ms)']
# The seven families of Fig. 3d and Fig. 5a, in the code's order.
FAMILIES_7 = ['Lamp5', 'Vip', 'Sst', 'Pvalb', 'IT', 'ET', 'CT']
INHIBITORY = ['Lamp5', 'Sncg', 'Vip', 'Sst', 'Pvalb']
EXCITATORY = ['IT', 'ET', 'NP', 'CT']
# Nissl layer boundaries of normalized depth (Fig. 1b legend).
LAYER_BOUNDS = (0.07, 0.29, 0.73)


# --------------------------------------------------------------------------------------------
# The archive
# --------------------------------------------------------------------------------------------

def _get(url, **kw):
    for attempt in range(6):
        try:
            r = requests.get(url, timeout=120, **kw)
            r.raise_for_status()
            return r
        except requests.RequestException:
            if attempt == 5:
                raise
            time.sleep(2 * (attempt + 1))


def version_metadata() -> dict:
    return _get(f"{API}/dandisets/{DANDISET}/versions/{VERSION}/").json()


def list_assets(version: str = VERSION) -> pd.DataFrame:
    """Every asset of the pinned version: path, asset id, size."""
    out, url = [], f"{API}/dandisets/{DANDISET}/versions/{version}/assets/?page_size=1000"
    while url:
        r = _get(url).json()
        out += r["results"]
        url = r["next"]
    return pd.DataFrame([{"path": a["path"], "asset_id": a["asset_id"], "size": a["size"]} for a in out])


def open_asset(asset_id: str):
    """The asset's NWB file, read over HTTPS into memory and opened with h5py."""
    import h5py
    b = _get(f"{API}/assets/{asset_id}/download/").content
    return h5py.File(io.BytesIO(b), "r")


def _dec(v):
    if isinstance(v, bytes):
        return v.decode()
    if isinstance(v, np.ndarray):
        return [_dec(x) for x in v.tolist()]
    if isinstance(v, np.generic):
        return v.item()
    return v


def read_cell(f) -> dict:
    """Metadata, voltage traces and stimuli of one file.

    Returns a dict with `meta` (every scalar of DandiIcephysMetadata and subject, and the session
    fields), `rate`, `voltage` (samples x sweeps, in sweep order, values as stored), `sweeps`
    (acquisition sweep numbers), and `stim`, one row per stimulus series: sweep, amplitude (the
    median of non-zero samples), onset and offset sample, length, and value at sample 12000.
    """
    meta = {}
    for grp in ["general/DandiIcephysMetadata", "general/subject"]:
        if grp in f:
            for k in f[grp]:
                meta[grp.split("/")[-1] + "." + k] = _dec(f[grp][k][()])
    meta["has_soma_depth_um"] = "general/DandiIcephysMetadata/soma_depth_um" in f
    for k in ["session_id", "experimenter", "institution", "lab", "experiment_description"]:
        if "general/" + k in f:
            meta[k] = _dec(f["general/" + k][()])
    for k in ["session_start_time", "session_description", "identifier"]:
        if k in f:
            meta[k] = _dec(f[k][()])
    acq = f["acquisition"]
    keys = sorted(acq.keys(), key=lambda k: int(acq[k].attrs["sweep_number"]))
    sweeps = [int(acq[k].attrs["sweep_number"]) for k in keys]
    lengths = {acq[k]["data"].shape[0] for k in keys}
    rates = {float(acq[k]["starting_time"].attrs["rate"]) for k in keys}
    starts = [float(acq[k]["starting_time"][()]) for k in keys]
    starts = {"nan": int(np.sum(np.isnan(starts))), "values": sorted({x for x in starts if not np.isnan(x)})}
    vunits = {_dec(acq[k]["data"].attrs["unit"]) for k in keys}
    conv = {float(acq[k]["data"].attrs["conversion"]) for k in keys}
    n = min(lengths)
    voltage = np.column_stack([acq[k]["data"][:n] for k in keys])
    st = f["stimulus/presentation"]
    rows = []
    for k in st.keys():
        d = st[k]["data"][:]
        nz = np.flatnonzero(np.abs(d) > 1e-9)
        rows.append({"sweep": int(st[k].attrs["sweep_number"]),
                     "amplitude": float(np.median(d[nz])) if len(nz) else 0.0,
                     "onset": int(nz[0]) if len(nz) else -1,
                     "offset": int(nz[-1]) + 1 if len(nz) else -1,
                     "length": len(d),
                     "at12000": float(d[12000]) if len(d) > 12000 else np.nan,
                     "levels": len(np.unique(d)),
                     "rate": float(st[k]["starting_time"].attrs["rate"]),
                     "unit": _dec(st[k]["data"].attrs["unit"])})
    stim = pd.DataFrame(rows).sort_values("sweep").reset_index(drop=True)
    return {"meta": meta, "rate": rates.pop() if len(rates) == 1 else sorted(rates),
            "lengths": sorted(lengths), "starting_times": starts,
            "voltage_units": sorted(vunits), "conversion": sorted(conv),
            "voltage": voltage, "sweeps": sweeps, "stim": stim}


# --------------------------------------------------------------------------------------------
# The paper's feature extraction
# --------------------------------------------------------------------------------------------

_PAPER = None


def paper_code() -> types.SimpleNamespace:
    """The paper's extraction code, fetched at the pinned commit and executed unchanged."""
    global _PAPER
    if _PAPER is not None:
        return _PAPER
    import sys
    import scipy.integrate
    from sklearn import linear_model
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    if not hasattr(np, "float"):
        np.float = float  # alias removed in numpy 1.24; same behaviour
    mods = {}
    for name in ["ephys_features", "ephys_extractor"]:
        src = _get(f"{MINI_ATLAS}/code/{name}.py").text
        mod = types.ModuleType(name)
        mod.__file__ = f"{name}.py"
        sys.modules[name] = mod
        exec(compile(src, f"mini-atlas/code/{name}.py", "exec"), mod.__dict__)
        mods[name] = mod
    # The filter is designed anew for every trace with the same arguments; caching the design
    # gives identical coefficients and saves about a sixth of the run time.
    import functools
    import scipy.signal
    mods["ephys_features"].signal = types.SimpleNamespace(
        bessel=functools.lru_cache(maxsize=16)(scipy.signal.bessel), filtfilt=scipy.signal.filtfilt)
    nb = _get(f"{MINI_ATLAS}/code/preprocess-ephys-files.ipynb").json()
    integrate = types.SimpleNamespace(cumtrapz=scipy.integrate.cumulative_trapezoid)
    ns = {"np": np, "pd": pd, "plt": plt, "efex": mods["ephys_extractor"], "ft": mods["ephys_features"],
          "integrate": integrate, "ransac": linear_model.RANSACRegressor()}
    for cell in (16, 20):
        exec(compile("".join(nb["cells"][cell]["source"]), f"preprocess-ephys-files.ipynb[{cell}]", "exec"), ns)
    _PAPER = types.SimpleNamespace(efex=mods["ephys_extractor"], ft=mods["ephys_features"],
                                   extract_spike_features=ns["extract_spike_features"],
                                   get_cell_features=ns["get_cell_features"], plt=plt)
    return _PAPER


def arrange_as_code(cell: dict):
    """time, voltage, current, curr_index_0 as the code's get_time_voltage_current_currindex0."""
    st = cell["stim"]
    v = cell["voltage"]
    n = v.shape[1]
    time_ = np.arange(v.shape[0]) / cell["rate"]
    current_initial = st.loc[st["sweep"] == min(st["sweep"]), "at12000"].iloc[0]
    curr_index_0 = int(-current_initial / 20)
    current = np.linspace(current_initial, (n - 1) * 20 + current_initial, n)
    return time_, v, current, curr_index_0


def cell_features(cell: dict) -> dict:
    """The 29 features of one cell, from the paper's code (stimulus window 0.1 to 0.7 s, 10 kHz filter)."""
    pc = paper_code()
    time_, voltage, current, curr_index_0 = arrange_as_code(cell)
    np.random.seed(0)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        with np.errstate(all="ignore"):
            df, dfr = pc.extract_spike_features(time_, current, voltage)
            feats = pc.get_cell_features(df, dfr, time_, current, voltage, curr_index_0)
    pc.plt.close("all")
    return {k: float(np.asarray(feats[k].values[0]).squeeze()) for k in FEATURES_29}


def process_asset(row: dict) -> dict:
    """Read one asset and extract its features; errors are returned, not raised."""
    out = {"path": row["path"], "asset_id": row["asset_id"]}
    try:
        f = open_asset(row["asset_id"])
        cell = read_cell(f)
    except Exception as e:  # recorded and reported in the notebook
        out["read_error"] = repr(e)
        return out
    import hashlib
    v = cell["voltage"]
    # Mean voltage in 10 ms bins (0 to 0.9 s) of the sweeps with negative current, for the
    # timing check of the stimulus against the response.
    st = cell["stim"]
    neg = st.loc[st["amplitude"] < 0]
    sweep_col = {s: i for i, s in enumerate(cell["sweeps"])}
    nb = int(0.9 * cell["rate"] / 250) if not isinstance(cell["rate"], list) else 0
    binned = {int(s): v[:nb * 250, sweep_col[s]].reshape(nb, 250).mean(axis=1).tolist()
              for s in neg["sweep"] if s in sweep_col}
    out.update({"meta": cell["meta"], "rate": cell["rate"], "lengths": cell["lengths"],
                "starting_times": cell["starting_times"],
                "voltage_units": cell["voltage_units"], "conversion": cell["conversion"],
                "sweeps": cell["sweeps"], "stim": st.to_dict("list"),
                "vmin": float(np.nanmin(v)), "vmax": float(np.nanmax(v)),
                "v_baseline": float(np.median(v[:2000, :])),
                "hash_all": hashlib.md5(np.ascontiguousarray(v).tobytes()).hexdigest(),
                "hash_first": hashlib.md5(np.ascontiguousarray(v[:, 0]).tobytes()).hexdigest(),
                "binned": binned})
    try:
        out["features"] = cell_features(cell)
    except Exception as e:  # a cell the paper's code cannot process
        out["feature_error"] = repr(e)
    return out


def load_all(assets: pd.DataFrame, workers: int = 8):
    """Process every asset in parallel. Returns (meta, features, stim, binned, errors), keyed by path.

    `binned` holds, per path and negative-current sweep, the mean voltage in 10 ms bins.
    """
    rows = assets.to_dict("records")
    with ProcessPoolExecutor(workers) as ex:
        res = list(ex.map(process_asset, rows, chunksize=4))
    meta, feats, stim, errors, binned = [], [], [], [], {}
    for r in res:
        if "read_error" in r:
            errors.append({"path": r["path"], "stage": "read", "error": r["read_error"]})
            continue
        m = dict(r["meta"])
        m.update({"path": r["path"], "rate": r["rate"], "lengths": r["lengths"],
                  "starting_times": r["starting_times"], "voltage_units": r["voltage_units"],
                  "conversion": r["conversion"], "n_sweeps": len(r["sweeps"]),
                  "sweeps": r["sweeps"], "vmin": r["vmin"], "vmax": r["vmax"], "v_baseline": r["v_baseline"],
                  "hash_all": r["hash_all"], "hash_first": r["hash_first"]})
        meta.append(m)
        binned[r["path"]] = r["binned"]
        s = pd.DataFrame(r["stim"])
        s["path"] = r["path"]
        stim.append(s)
        if "features" in r:
            fr = dict(r["features"])
            fr["path"] = r["path"]
            feats.append(fr)
        else:
            errors.append({"path": r["path"], "stage": "features", "error": r["feature_error"]})
    meta = pd.DataFrame(meta)
    meta.columns = [c.replace("DandiIcephysMetadata.", "") for c in meta.columns]
    return (meta.set_index("path"), pd.DataFrame(feats).set_index("path"),
            pd.concat(stim, ignore_index=True), binned,
            pd.DataFrame(errors, columns=["path", "stage", "error"]))


# --------------------------------------------------------------------------------------------
# Labels and the cell table
# --------------------------------------------------------------------------------------------

def paper_name(name):
    """The paper's spelling of a dandiset label: the files call the ET subclass 'PT' (L5 PT_1
    for L5 ET_1), an older name. Labels that differ only in spelling are one label."""
    if not isinstance(name, str):
        return name
    return name.replace("L5 PT_", "L5 ET_") if name != "PT" else "ET"


def paper_meta_table() -> pd.DataFrame:
    """The paper's per-cell metadata table (mini-atlas data/m1_patchseq_meta_data.csv), indexed by cell."""
    t = pd.read_csv(io.StringIO(_get(f"{MINI_ATLAS}/data/m1_patchseq_meta_data.csv").text), sep="\t")
    return t.set_index("Cell")


def paper_feature_table() -> pd.DataFrame:
    """The paper's extracted features (mini-atlas data/m1_patchseq_ephys_features.csv), indexed by cell."""
    return pd.read_csv(io.StringIO(_get(f"{MINI_ATLAS}/data/m1_patchseq_ephys_features.csv").text)).set_index("cell id")


def layer_from_depth(nd, fallback):
    """Layer from normalized depth with the Nissl boundaries, else the fallback (the code's rule).

    The comparisons are those of the code (phenotype-tsne.ipynb cell 3, physiological-temperature.ipynb
    cell 2): strict on both sides, so a depth exactly at 0.07, 0.29 or 0.73 keeps the fallback, as
    it does in the code. The claims file's opening comment gives the targeted layer as the fallback."""
    out = np.array(fallback, dtype=object).copy()
    nd = np.asarray(nd, dtype=float)
    with np.errstate(invalid="ignore"):
        out[nd < 0.07] = "1"
        out[(nd > 0.07) & (nd < 0.29)] = "2/3"
        out[(nd > 0.29) & (nd < 0.73)] = "5"
        out[nd > 0.73] = "6"
    return out


def duplicate_recordings(meta: pd.DataFrame) -> pd.DataFrame:
    """Groups of files whose whole voltage matrix is identical: one row per file in such a group,
    with its cell id, mouse, t-type, and whether it is kept. Within a group the cell with the
    lowest sample number is kept; which cell the recording belongs to is not known, so this is a
    standard choice, made so that each recording is counted once."""
    m = meta.reset_index()
    d = m[m["hash_all"].duplicated(keep=False)].copy()
    d["sample"] = d["cell_id"].str.extract(r"sample_(\d+)")[0].astype(int)
    d = d.sort_values(["hash_all", "sample"])
    d["kept"] = ~d["hash_all"].duplicated(keep="first")
    return d[["cell_id", "subject.subject_id", "RNA_type", "slice_id", "hash_all", "kept"]].rename(
        columns={"subject.subject_id": "mouse", "RNA_type": "t-type"}).reset_index(drop=True)


def cell_table(meta: pd.DataFrame, feats: pd.DataFrame, excluded=None, drop=None) -> pd.DataFrame:
    """One row per cell (index: cell id) with labels from the files and the 29 features.

    `ttype` and `family` use the paper's spelling; cells without a t-type have family
    'low quality' as in the files. `depth_norm` is the files' `cortical_thickness_4x` (which
    holds the soma depth in 4x image units) over `cortical_thickness_um` (which holds the
    cortical thickness in the same units). `layer` is the layer of the claims file's opening
    comment: `depth_norm` cut at the Nissl boundaries, the targeted layer where there is no depth
    (`layer_from_depth`); `inferred_layer` is the files' own field. `excluded` is a set of cell ids to flag. The features
    of the cells in `drop` (duplicated recordings) are set to missing, so that analyses of the
    recordings count each recording once; their labels are kept.
    """
    m = meta.copy()
    t = pd.DataFrame(index=m["cell_id"].values)
    t["path"] = m.index.values
    t["mouse"] = m["subject.subject_id"].values
    t["ttype"] = [paper_name(x) if isinstance(x, str) else "" for x in m.get("RNA_type", pd.Series([np.nan] * len(m))).values]
    t["family"] = [paper_name(x) for x in m["RNA_family"].values]
    t["inferred_layer"] = m["inferred_layer"].astype(str).values
    t["targeted_layer"] = m["targeted_layer"].astype(str).values
    with np.errstate(invalid="ignore", divide="ignore"):
        t["depth_norm"] = (pd.to_numeric(m["cortical_thickness_4x"], errors="coerce")
                           / pd.to_numeric(m["cortical_thickness_um"], errors="coerce")).values
    t["layer"] = layer_from_depth(t["depth_norm"].values, t["targeted_layer"].values)
    t["excluded"] = t.index.isin(set(excluded or []))
    f = feats.reindex(m.index)
    for c in FEATURES_29:
        t[c] = f[c].values
    t["duplicate_dropped"] = t.index.isin(set(drop or []))
    t.loc[t["duplicate_dropped"], FEATURES_29] = np.nan
    return t


# --------------------------------------------------------------------------------------------
# Measures (claims file; Methods; code phenotype-tsne.ipynb, families.ipynb)
# --------------------------------------------------------------------------------------------

def features17(t: pd.DataFrame, log=FEATURES_LOG) -> pd.DataFrame:
    """The 17 features with the log transform (four features in the Methods; `log` can be changed)."""
    X = t[FEATURES_17].astype(float).copy()
    with np.errstate(divide="ignore", invalid="ignore"):
        for c in log:
            X[c] = np.log(X[c])
    X[~np.isfinite(X)] = np.nan
    return X


def ephys_representation(X17: pd.DataFrame) -> pd.DataFrame:
    """Cells with all 17 features, standardized, all 17 PCs, scaled by the s.d. of PC1 (code)."""
    from sklearn.decomposition import PCA
    keep = X17.notna().all(axis=1)
    X = X17[keep].values
    X = (X - X.mean(axis=0)) / X.std(axis=0)
    Z = PCA().fit_transform(X)
    Z = Z / np.std(Z[:, 0])
    return pd.DataFrame(Z, index=X17.index[keep])


def standardized17(X17: pd.DataFrame) -> pd.DataFrame:
    """The 17 features standardized over the cells with all 17 (families.ipynb, ephysTransformed)."""
    keep = X17.notna().all(axis=1)
    mu, sd = X17[keep].mean(axis=0), X17[keep].std(axis=0, ddof=0)
    return ((X17 - mu) / sd)[keep]


def knn_predictions(Z: np.ndarray, labels: np.ndarray, k: int = 10) -> np.ndarray:
    """Majority label among the k nearest neighbours (Euclidean, the cell itself left out); ties go
    to the label first in numpy's sort order, as np.unique and argmax do in the code."""
    from sklearn.neighbors import NearestNeighbors
    _, ind = NearestNeighbors(n_neighbors=k).fit(Z).kneighbors()
    out = np.empty(len(Z), dtype=object)
    for i in range(len(Z)):
        u, c = np.unique(labels[ind[i]], return_counts=True)
        out[i] = u[np.argmax(c)]
    return out


def family_confusion(pred, labels, rows=FAMILIES_7) -> pd.DataFrame:
    """Rows: true family; columns: predicted family; cells predicted outside the seven not counted."""
    C = pd.DataFrame(0.0, index=rows, columns=rows)
    n = pd.Series(0, index=rows)
    for r in rows:
        sel = labels == r
        p = pred[sel]
        p = p[np.isin(p, rows)]
        n[r] = len(p)
        for c in rows:
            C.loc[r, c] = np.mean(p == c) if len(p) else np.nan
    C["n"] = n
    return C


def normalized_variance(Z: np.ndarray, members: np.ndarray) -> float:
    """Sum of per-dimension variances of the members over that of all cells (Methods)."""
    return float(np.sum(np.var(Z[members], axis=0)) / np.sum(np.var(Z, axis=0)))



# --------------------------------------------------------------------------------------------
# Outside inputs for the transcriptomic claims (claims file: with_inputs and elsewhere claims)
# --------------------------------------------------------------------------------------------

# The paper's preprocessed Allen Institute reference data (Zenodo record 5118962; the code's
# reduced-allen-data folder). Read member by member over HTTP range requests.
ZENODO_ZIP = "https://zenodo.org/api/records/5118962/files/reduced-allen-data.zip/content"
_MODULES = {}


def paper_module(name: str) -> types.ModuleType:
    """A module of the paper's code (mini-atlas/code/<name>.py at the pinned commit), executed unchanged."""
    import sys
    if name in _MODULES:
        return _MODULES[name]
    import matplotlib
    matplotlib.use("Agg")
    if name == "sparseRRR":
        _install_glmnet_substitute()
    src = _get(f"{MINI_ATLAS}/code/{name}.py").text
    mod = types.ModuleType(name)
    mod.__file__ = f"{name}.py"
    sys.modules[name] = mod
    exec(compile(src, f"mini-atlas/code/{name}.py", "exec"), mod.__dict__)
    _MODULES[name] = mod
    return mod


def _install_glmnet_substitute():
    """sparseRRR.py calls glmnet_python, which has no distribution for Python 3.13. This puts in its
    place scikit-learn's ElasticNet and MultiTaskElasticNet, which minimize the same objective as
    glmnet's gaussian and mgaussian families with standardize=False and no intercept:
    1/(2n) ||Y - XB||^2 + lambda * (alpha * sum_j ||b_j||_2 + (1 - alpha)/2 ||B||^2).
    The tolerance (1e-7) and iteration limit (10,000) are standard choices for convergence."""
    import sys
    from sklearn.linear_model import ElasticNet, MultiTaskElasticNet

    def glmnet(x, y, alpha, lambdau, family="gaussian", standardize=False, intr=False, standardize_resp=False):
        lam = float(np.asarray(lambdau).ravel()[0])
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            if family == "mgaussian":
                m = MultiTaskElasticNet(alpha=lam, l1_ratio=alpha, fit_intercept=False, max_iter=10000, tol=1e-7).fit(x, y)
                return {"beta": [m.coef_[i][:, None] for i in range(y.shape[1])]}
            m = ElasticNet(alpha=lam, l1_ratio=alpha, fit_intercept=False, max_iter=10000, tol=1e-7).fit(x, np.ravel(y))
            return {"beta": m.coef_[:, None]}

    g = types.ModuleType("glmnet")
    g.glmnet = glmnet
    sys.modules["glmnet"] = g
    sys.modules["glmnet_python"] = types.ModuleType("glmnet_python")


def patchseq_counts():
    """The paper's exon and intron count tables (genes x cells) and gene lengths (mini-atlas data/)."""
    ex = pd.read_csv(io.BytesIO(_get(f"{MINI_ATLAS}/data/m1_patchseq_exon_counts.csv.gz").content),
                     compression="gzip", index_col=0, na_filter=False)
    it = pd.read_csv(io.BytesIO(_get(f"{MINI_ATLAS}/data/m1_patchseq_intron_counts.csv.gz").content),
                     compression="gzip", index_col=0, na_filter=False)
    gl = pd.read_csv(io.StringIO(_get(f"{MINI_ATLAS}/data/gene_lengths.txt").text))
    assert (ex.index == it.index).all() and (gl["GeneID"].values == ex.index.values).all()
    return ex, it, gl


_ZIP = None


def reference(member: str) -> dict:
    """One reference data set from the Zenodo archive, with the t-type names brought up to date as
    the code's allen-data-preprocess.ipynb (cell 14, 'Quickly update cluster annotations') does,
    from data/raw/allen/yao2020/cluster.annotation.csv; tasic2018 is returned as stored."""
    import pickle
    import zipfile
    import fsspec
    global _ZIP
    if _ZIP is None:
        _ZIP = zipfile.ZipFile(fsspec.open(ZENODO_ZIP, block_size=2 ** 22).open())
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        d = pickle.loads(_ZIP.read(member + ".pickle"))
    if member != "tasic2018":
        names, colors = reference_names()
        for subset in d:
            d[subset]["clusterNames"] = names
            d[subset]["clusterColors"] = colors
    return d


def reference_names():
    ann = pd.read_csv(io.StringIO(_get(f"{MINI_ATLAS}/data/raw/allen/yao2020/cluster.annotation.csv").text))
    ann = ann.sort_values("cluster_id")
    names = ann["cluster_label"].values
    neural = np.arange(np.where(names == "Meis2")[0][0])
    return names[neural], ann["cluster_color"].values[neural]


def family_of_type(names) -> np.ndarray:
    """The code's family of each t-type name (families.ipynb): the first word, or for excitatory
    names the first two letters of the second word; the last five (L6b) count as CT."""
    fams = np.array([c.split()[0] if c.split()[0][1] not in "2456" else c.split()[1][:2] for c in names], dtype=object)
    fams[-5:] = "CT"
    return fams


def tsne_atlas(subset: str) -> np.ndarray:
    """The reference t-SNE coordinates of the code (data/processed/rnaseq/10x-tsne-<subset>.pickle)."""
    import pickle
    return pickle.loads(_get(f"{MINI_ATLAS}/data/processed/rnaseq/10x-tsne-{subset}.pickle").content)
