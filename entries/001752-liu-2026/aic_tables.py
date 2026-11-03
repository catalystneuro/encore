"""Readers for the outside data of Liu et al. (2026), doi:10.1038/s41556-026-02009-4, that the claims file
places elsewhere (`data: elsewhere`): the per-cell tables of the paper's code, pinned at a commit, the
sodium-current dandiset DANDI:001750 and the Patch-seq electrophysiology dandiset DANDI:001746, each pinned
at its only published version. DANDI:001750 is streamed with remfile; each DANDI:001746 file is read into
memory in one request (never to disk), as reading its sweeps through remfile was about 100 times slower.

Where each parameter comes from is said at each function. Statistical helpers implement the tests the
paper's legends name (Kruskal-Wallis followed by Dunn's test with Bonferroni correction, Fig. 3e legend and
the code's PeakIdx_Fig5e.xlsx sheet "statistics"; two-way ANOVA, Fig. 4j text; two-tailed Wilcoxon
rank-sum, Fig. 4d legend; Welch's ANOVA and the Games-Howell test, Fig. 8 legend). The Patch-seq features
follow the Methods (Extraction of electrophysiological features): tau from an exponential fitted from the
stimulation onset to the bottom of the sag, averaged over the hyperpolarizing sweeps; the first AP of the
rheobase sweep, its threshold at the largest third derivative in the 20 ms before the peak, its amplitude
from threshold to peak and its half-width at half that amplitude. Finding an AP by a crossing of 0 mV and
dropping tau fits outside 0 to 600 ms (TAU_MAX_MS) are standard choices, not the paper's. The largest third
derivative is sought on the rising phase, from 20 ms before the peak to the largest first derivative: the
Methods' window, limited so that a noisy third derivative near the peak or on the falling phase cannot be
taken as the threshold (a standard guard; the first run searched the whole window, which put thresholds up
to +65 mV, and its values are kept as a variant).

The metabolomics table of MetaboLights MTBLS13927 is read from the study's first metadata revision
(METADATA_REVISIONS/MTBLS13927_01), a fixed copy. DANDI:001751 (multi-patch) is read for its metadata only.
"""
from __future__ import annotations

import io
import json
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from itertools import combinations

import h5py
import numpy as np
import pandas as pd
import remfile
from scipy import stats

CODE_COMMIT = "44cd8a6dfbb1f1ce363d73742e4f3652086b0f9d"
RAW = f"https://raw.githubusercontent.com/RFLiu2021/AIC_proj/{CODE_COMMIT}"

SODIUM_DANDISET = "001750"
SODIUM_VERSION = "0.260825.0222"
API = "https://api.dandiarchive.org/api"

# Cluster numbers of the excitatory scRNA-seq types, as the code groups them for Fig. 3f
# (morpho/Fig3f_plotCellTypesAIS_Cmp.m): VENs mapped to cluster 16 are the L5 ET group and those mapped to
# cluster 8 the L5/6 CT group.
CLUSTER_L5_ET = 16
CLUSTER_L56_CT = 8


def get(path: str) -> bytes:
    with urllib.request.urlopen(f"{RAW}/{path}", timeout=120) as r:
        return r.read()


def excel(path: str, sheet_name=0, header=None) -> pd.DataFrame:
    return pd.read_excel(io.BytesIO(get(path)), sheet_name=sheet_name, header=header)


def csv(path: str) -> pd.DataFrame:
    return pd.read_csv(io.BytesIO(get(path)))


def dunn_bonferroni(groups: dict[str, np.ndarray]) -> pd.DataFrame:
    """Dunn's test on the ranks of all values, with the tie correction, two-sided, Bonferroni-corrected
    over all pairs (Dunn 1964)."""
    names = list(groups)
    allv = np.concatenate([groups[n] for n in names])
    ranks = stats.rankdata(allv)
    n_total = len(allv)
    _, counts = np.unique(allv, return_counts=True)
    tie = np.sum(counts ** 3 - counts) / (12.0 * (n_total - 1))
    mean_rank, sizes, start = {}, {}, 0
    for n in names:
        k = len(groups[n])
        mean_rank[n], sizes[n] = ranks[start:start + k].mean(), k
        start += k
    rows, m = [], len(names) * (len(names) - 1) // 2
    for a, b in combinations(names, 2):
        se = np.sqrt((n_total * (n_total + 1) / 12.0 - tie) * (1 / sizes[a] + 1 / sizes[b]))
        z = (mean_rank[a] - mean_rank[b]) / se
        p = 2 * stats.norm.sf(abs(z))
        rows.append(dict(a=a, b=b, z=z, p=p, p_bonferroni=min(1.0, p * m)))
    return pd.DataFrame(rows)


def sodium_assets() -> list[dict]:
    url = f"{API}/dandisets/{SODIUM_DANDISET}/versions/{SODIUM_VERSION}/assets/?page_size=200"
    with urllib.request.urlopen(url, timeout=120) as r:
        return json.loads(r.read())["results"]


def sodium_file(asset: dict) -> dict:
    """Stream one outside-out patch: every sweep's current (pA) and command (mV), with the rate."""
    url = f"{API}/assets/{asset['asset_id']}/download/"
    out = dict(file=asset["path"].split("/")[-1], sweeps={})
    with h5py.File(remfile.File(url), "r") as h:
        out["cell_id"] = h["general/intracellular_ephys/IntracellularElectrode/cell_id"][0].decode()
        out["subject"] = h["general/subject/subject_id"][()].decode()
        for name, ts in h["acquisition"].items():
            data = ts["data"]
            rate = float(ts["starting_time"].attrs["rate"])
            i = data[:] * float(data.attrs.get("conversion", 1.0)) * 1e12
            stim_name = name.replace("NaCurrentSeries", "NaCurrentStimulusSeries")
            v = None
            for key in h["stimulus/presentation"]:
                if key.endswith(name.split("NaCurrentSeries")[1]):
                    sd = h["stimulus/presentation"][key]["data"]
                    v = sd[:] * float(sd.attrs.get("conversion", 1.0)) * 1e3
            out["sweeps"][name] = dict(current_pA=i, command_mV=v, rate=rate,
                                       unit=data.attrs["unit"].decode() if isinstance(data.attrs["unit"], bytes)
                                       else data.attrs["unit"])
    return out


def sodium_all(asset_list: list[dict]) -> list[dict]:
    with ThreadPoolExecutor(12) as ex:
        return list(ex.map(sodium_file, asset_list))


def peak_inward(sweep: dict, baseline_ms: tuple[float, float], window_ms: tuple[float, float]) -> float:
    """Most negative current in the window, relative to the mean over the baseline window (pA).
    Windows are standard choices, said in the notebook."""
    i, r = sweep["current_pA"], sweep["rate"]
    b = i[int(baseline_ms[0] * r / 1000): int(baseline_ms[1] * r / 1000)].mean()
    w = i[int(window_ms[0] * r / 1000): int(window_ms[1] * r / 1000)]
    return float(w.min() - b)


def welch_anova(*groups: np.ndarray) -> tuple[float, float]:
    """Welch's one-way ANOVA (Welch 1951): F and p. The test the Fig. 8 legend names."""
    k = len(groups)
    n = np.array([len(g) for g in groups], float)
    m = np.array([np.mean(g) for g in groups])
    v = np.array([np.var(g, ddof=1) for g in groups])
    if np.any(v == 0):
        return np.nan, np.nan
    w = n / v
    mw = np.sum(w * m) / np.sum(w)
    a = np.sum(w * (m - mw) ** 2) / (k - 1)
    tmp = np.sum((1 - w / np.sum(w)) ** 2 / (n - 1))
    b = 1 + 2 * (k - 2) / (k ** 2 - 1) * tmp
    f = a / b
    df2 = (k ** 2 - 1) / (3 * tmp)
    return float(f), float(stats.f.sf(f, k - 1, df2))


def games_howell(a: np.ndarray, b: np.ndarray, k: int) -> float:
    """Games-Howell p-value for one pair among k groups (studentized range with Welch's degrees of
    freedom). The post hoc test the Fig. 8 legend names."""
    va, vb = np.var(a, ddof=1) / len(a), np.var(b, ddof=1) / len(b)
    if va + vb == 0:
        return np.nan
    q = abs(np.mean(a) - np.mean(b)) / np.sqrt((va + vb) / 2)
    df = (va + vb) ** 2 / (va ** 2 / (len(a) - 1) + vb ** 2 / (len(b) - 1))
    return float(stats.studentized_range.sf(q, k, df))


# --- Patch-seq electrophysiology, DANDI:001746 (fig2d-f-l23-it-tau-width) ---------------------------------
PATCHSEQ_DANDISET = "001746"
PATCHSEQ_VERSION = "0.260825.0222"

# Subclass groups of the code's Fig. 2d script (ephysio/Fig2D_ephyFeatCmp.m), by predicted cluster number;
# clusters 16 and 8 split by the expert cell type (VEN, or PC for L5 ET).
SUBCLASS_CLUSTERS = {"L2/3 IT HPCAL1": {1, 15, 5}, "IT RORB": {2, 0, 7, 13, 19}, "L5 IT FEZF2": {3, 6, 9, 11, 14, 18},
                     "L6 PC": {4, 12, 17}}


def subclass(cluster: int, cell_type: str) -> str | None:
    for name, ids in SUBCLASS_CLUSTERS.items():
        if cluster in ids:
            return name
    if cluster in (16, 8) and "ven" in str(cell_type).lower():
        return "VEN"
    if cluster == 16 and "pc" in str(cell_type).lower():
        return "L5 ET"
    return None


def patchseq_assets() -> list[dict]:
    out, url = [], f"{API}/dandisets/{PATCHSEQ_DANDISET}/versions/{PATCHSEQ_VERSION}/assets/?page_size=500"
    while url:
        with urllib.request.urlopen(url, timeout=120) as r:
            page = json.loads(r.read())
        out += page["results"]
        url = page.get("next")
    return out


TAU_MAX_MS = 600.0


def _tau_ms(v: np.ndarray, rate: float, on: int, off: int) -> float:
    """Membrane time constant from one hyperpolarizing sweep, as the Methods define it: f(t) = a exp(-t/tau) + C
    fitted from the stimulation onset to the bottom of the sag (the minimum during the step)."""
    from scipy.optimize import curve_fit
    seg = v[on:off]
    trough = int(np.argmin(seg))
    if trough < 10:
        return np.nan
    y = seg[: trough + 1]
    t = np.arange(len(y)) / rate * 1000.0
    try:
        p, _ = curve_fit(lambda t, a, tau, c: a * np.exp(-t / tau) + c, t, y,
                         p0=(y[0] - y[-1], max(t[-1] / 3, 1.0), y[-1]), maxfev=5000)
        # a fit outside 0 to TAU_MAX_MS is counted as failed (a standard guard, not the paper's)
        return float(p[1]) if 0 < p[1] <= TAU_MAX_MS else np.nan
    except Exception:
        return np.nan


def first_ap(v: np.ndarray, rate: float, on: int, off: int, rising_only: bool = True) -> dict | None:
    """The first AP during the step (an upward crossing of 0 mV, a standard choice), with the Methods'
    threshold (largest third derivative in the 20 ms before the peak), amplitude (peak minus threshold) and
    half-width (time between the rising and decaying crossings of half the amplitude). With rising_only, the
    third derivative is sought only up to the largest first derivative (see the module docstring)."""
    seg = v[on:off]
    up = np.flatnonzero((seg[:-1] < 0) & (seg[1:] >= 0))
    if len(up) == 0:
        return None
    i0 = on + up[0]
    pk = i0 + int(np.argmax(v[i0: i0 + int(0.002 * rate)]))
    w0 = max(on, pk - int(0.020 * rate))
    end = w0 + int(np.argmax(np.diff(v[w0: pk + 1]))) + 1 if rising_only and pk > w0 else pk
    d3 = np.diff(v[w0: end + 1], 3)
    if len(d3) == 0:
        return None
    thr_i = w0 + int(np.argmax(d3)) + 1
    thr, peak = v[thr_i], v[pk]
    half = thr + (peak - thr) / 2
    rise = np.flatnonzero(v[thr_i: pk + 1] >= half)
    fall = np.flatnonzero(v[pk: pk + int(0.010 * rate)] <= half)
    if len(rise) == 0 or len(fall) == 0:
        return None
    width = (pk + fall[0] - (thr_i + rise[0])) / rate * 1000.0
    return dict(threshold_mV=thr, amplitude_mV=peak - thr, half_width_ms=width)


def patchseq_features(asset: dict) -> dict:
    """Stream one Patch-seq recording and return tau (mean over the hyperpolarizing sweeps), rheobase and the
    first AP's amplitude and half-width. Reads only the sweeps it needs: the stimulus at mid-step, every
    hyperpolarizing sweep, and depolarizing sweeps in order of current until the first AP."""
    url = f"{API}/assets/{asset['asset_id']}/download/"
    out = dict(file=asset["path"].split("/")[-1])
    # The file (about 44 MB) is read into memory in one request, never to disk: reading its sweeps one by one
    # through remfile was about 100 times slower here.
    with urllib.request.urlopen(url, timeout=600) as r:
        buf = io.BytesIO(r.read())
    with h5py.File(buf, "r") as h:
        acq, stim = h["acquisition"], h["stimulus/presentation"]
        names = sorted(acq.keys())
        snames = sorted(stim.keys())
        s0 = stim[snames[0]]["data"][:]
        nz = np.flatnonzero(s0 != 0)
        if len(nz) == 0:
            out["error"] = "first stimulus is all zeros"
            return out
        on, off = int(nz[0]), int(nz[-1]) + 1
        mid = (on + off) // 2
        amps = [float(stim[s]["data"][mid]) for s in snames]
        rate = float(acq[names[0]]["starting_time"].attrs["rate"])
        conv = float(acq[names[0]]["data"].attrs.get("conversion", 1.0))
        out.update(rate=rate, n_sweeps=len(names), step_ms=(off - on) / rate * 1000, min_pA=min(amps), max_pA=max(amps))
        taus = []
        for n, a in zip(names, amps):
            if a < 0:
                v = acq[n]["data"][:] * conv * 1000.0
                taus.append(_tau_ms(v, rate, on, off))
        out["tau_ms"] = float(np.nanmean(taus)) if np.isfinite(taus).any() else np.nan
        out["n_tau_sweeps"] = int(np.isfinite(taus).sum())
        out["n_tau_failed"] = int(len(taus) - np.isfinite(taus).sum())
        for n, a in sorted(((n, a) for n, a in zip(names, amps) if a > 0), key=lambda x: x[1]):
            v = acq[n]["data"][:] * conv * 1000.0
            ap = first_ap(v, rate, on, off)
            if ap is not None:
                out.update(rheobase_pA=a, **ap)
                ap0 = first_ap(v, rate, on, off, rising_only=False) or {}
                out.update({f"{k}_v0": x for k, x in ap0.items()})
                break
    return out


def patchseq_all(asset_list: list[dict], workers: int = 8) -> list[dict]:
    def safe(a):
        try:
            return patchseq_features(a)
        except Exception as e:  # recorded, so that failures are counted
            return dict(file=a["path"].split("/")[-1], error=repr(e)[:200])
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(safe, asset_list))


# --- Metabolomics, MetaboLights MTBLS13927 (fig8a-metabolite-gradient, fig8de-glycolytic-bias) ------------------
MTBLS = "MTBLS13927"
MTBLS_REVISION = "MTBLS13927_01"
MTBLS_MAF = (f"https://ftp.ebi.ac.uk/pub/databases/metabolights/studies/public/{MTBLS}/METADATA_REVISIONS/"
             f"{MTBLS_REVISION}/m_MTBLS13927_LC-MS_alternating_hilic_metabolite_profiling_v2_maf.tsv")


def metabolights_maf() -> pd.DataFrame:
    """The study's metabolite assignment file: one row per identified metabolite, one column per sample."""
    with urllib.request.urlopen(MTBLS_MAF, timeout=120) as r:
        return pd.read_csv(io.BytesIO(r.read()), sep="\t")


# --- Multi-patch recordings, DANDI:001751 (fig5-connectivity-total, fig5-connectivity-by-type) --------------------
MULTI_DANDISET = "001751"
MULTI_VERSION = "0.260825.0222"


def multi_assets() -> list[dict]:
    out, url = [], f"{API}/dandisets/{MULTI_DANDISET}/versions/{MULTI_VERSION}/assets/?page_size=400"
    while url:
        with urllib.request.urlopen(url, timeout=120) as r:
            page = json.loads(r.read())
        out += page["results"]
        url = page.get("next")
    return out


def multi_file_contents(asset: dict) -> dict:
    """Stream one multi-patch file and list what it holds apart from the traces: the groups other than
    acquisition and stimulus that have content, the entries of general/intracellular_ephys that are not
    electrodes (where icephys tables would be), and the fields of its first electrode. Reads names only, not
    the traces' attributes, so that it stays fast."""
    url = f"{API}/assets/{asset['asset_id']}/download/"
    out = dict(file=asset["path"].split("/")[-1])
    with h5py.File(remfile.File(url), "r") as h:
        out["n_series"] = len(h["acquisition"])
        out["nonempty_groups"] = sorted(g for g in ("analysis", "processing", "intervals", "scratch") if g in h and len(h[g]) > 0)
        e = h["general/intracellular_ephys"]
        names = list(e.keys())
        out["non_electrode_entries"] = sorted(k for k in names if not k.startswith("Elec_"))
        out["n_electrodes"] = sum(k.startswith("Elec_") for k in names)
        ex = {}
        el = [k for k in names if k.startswith("Elec_")]
        for f in (e[el[0]] if el else []):
            o = e[el[0]].get(f, getlink=False)
            if isinstance(o, h5py.Dataset):
                v = o[()]
                ex[f] = v.decode() if isinstance(v, bytes) else str(v)
        out["example_electrode"] = ex
        out["session_description"] = h["session_description"][()].decode()
    return out
