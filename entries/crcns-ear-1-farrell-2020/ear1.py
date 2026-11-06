"""Loading and measures for CRCNS data set ear-1 (doi:10.6080/K0571975), version `unversioned`.

The data set holds 89 guinea pig outer hair cells (OHCs) recorded by whole-cell voltage clamp, one
HDF5 file per cell, and the original MATLAB files they were translated from, all inside one zip,
`ear-1/live/data_and_scripts.zip`, in the public S3 bucket `crcnsarchive`. CRCNS data sets are not
versioned (docs/archives.md); the version is recorded as `unversioned` with the MD5 of the zip from
the data set's `checksums.md5`, which `zip_md5()` reads so that a later change is detectable.

The files are streamed: the zip is opened in place with fsspec and zipfile over range requests, and
each member is read into memory. Nothing is written to disk.

Sources of the parameters (docs/protocol.md, Author, step 1.6):

- Per-cell CL, QTm, V0.5 and alphaB are the values the data set stores ("transformed data set"
  group of each HDF5 file). The claims file's shared method says that where the data set stores
  corrected values they are used. The stored values for the example cell of Fig. S1 (original number
  99) are the legend's to the printed digits (checked in the notebook), so they are the values the
  paper used. They are computed at the lower frequency f1 (Methods, Whole-cell patch-clamp,
  paragraph 2, "we usually report the membrane capacitance calculated at the lower of the two
  frequencies"). Recomputed values from the traces are given as a check (`recompute_cell`).
- V0.5 corrected for the pipette drop is the second element of `V_0p5`; the first is uncorrected.
  The data set's own analysis script (Analysis/check_non_linear_electrical_properties.m) computes
  the correction as V0.5 x Rm/(Rm+Rs) with Rm and Rs averaged over the linear region at positive
  voltages, the second choice that Methods, paragraph 2 allows.
- alphaB is the stored `alpha_f1`, which that script computes as 4 x max d(q/QTm)/dV (Eq. 8d as
  rebuilt in the claims file); alpha(V0.5) = alphaB / 4.
- CNLW = 4.82 pF, the value the claims file's shared method uses (Results, Experimental magnitude,
  paragraph 1, "~4.82 pF"). The paper computes CLW with Eq. 8a and a per-cell stereocilia bundle
  capacitance (CSB) that the data set does not store, so CLW = CL - 4.82 pF is a stated assumption.
- T = 297.15 K (24 C, the stored temperature of every cell; claims file, opening comment).
- Basal and apical: the data set's own label `apical_basal_polarity` (basal for turns 1 and 2,
  apical for turns 3 and 4), which is reading (r-a) of the claims file. Reading (r-b) (turn 1 against
  turn 4) is `region_rb`.
- CLn, the linear capacitance at negative voltages, is not stored. Readings in `cln_readings`.
"""

from __future__ import annotations

import io
import re
import zipfile

import fsspec
import h5py
import numpy as np
import pandas as pd
import scipy.io as sio
from scipy import stats

DATASET = "ear-1"            # CRCNS data set
VERSION = "unversioned"      # CRCNS data sets are not versioned (docs/archives.md)
BASE = "https://crcnsarchive.s3-us-west-2.amazonaws.com/ear-1/live/"
ZIP_URL = BASE + "data_and_scripts.zip"

KB = 1.380649e-23            # J/K
E0 = 1.602176634e-19         # C
T = 297.15                   # K, 24 C (stored temperature; claims file opening comment)
KT = KB * T
CNLW = 4.82                  # pF, non-lateral-wall capacitance (claims file shared method; assumption)
SPECIFIC_C = 0.0095          # pF/um2 (Fig. 4c criterion; Results, Determine q, paragraph 1)

_A = ("assay/voltage clamp assay/whole-cell patch clamp voltage clamp assay/"
      "electrical admittance dual-sine stimulus/")
_IV = ("assay/voltage clamp assay/whole-cell patch clamp voltage clamp assay/"
       "membrane current (I) as a function of membrane potential (V) (I vs V plot)/")
_T = "transformed data set/transformed data sets for protocol electrical admittance dual-sine stimulus/"
_TIV = ("transformed data set/transformed data set for protocol membrane current (I) as a function "
        "of membrane potential (V) (I vs V plot)/")


def zip_md5() -> dict:
    """The data set's own checksums.md5, as {file: md5}."""
    with fsspec.open(BASE + "checksums.md5", "rt") as f:
        return {line.split()[1]: line.split()[0] for line in f if line.strip()}


def open_zip() -> zipfile.ZipFile:
    f = fsspec.open(ZIP_URL, block_size=2**20).open()
    return zipfile.ZipFile(f)


def _val(h, path):
    o = h[path][()]
    if isinstance(o, bytes):
        return o.decode()
    if isinstance(o, h5py.Empty):
        return np.nan
    return o


def load_cells(z: zipfile.ZipFile | None = None) -> tuple[pd.DataFrame, dict]:
    """Read every HDF5 file of the zip. Returns a table with one row per cell (scalars) and a dict
    of per-cell traces keyed by file number."""
    z = z or open_zip()
    names = sorted((n for n in z.namelist() if n.startswith("data_and_scripts/HDF5_data/")
                    and n.endswith(".h5")), key=lambda n: int(re.search(r"#(\d+)", n).group(1)))
    rows, traces = [], {}
    for name in names:
        num = int(re.search(r"#(\d+)", name).group(1))
        h = h5py.File(io.BytesIO(z.read(name)), "r")
        r = {
            "file": num,
            "orig": int(h.attrs["original cell number"][0]),
            "researcher": h.attrs["researcher"].decode(),
            "date": h.attrs["date of experiment"].decode(),
            "polarity": _val(h, "anatomical/position/apical_basal_polarity"),
            "turn": _val(h, "anatomical/subdivision of bony labyrinth/subdivision of cochlea/cochlear_turn"),
            "phenotype": _val(h, "organism/Cavia porcellus/mammalian_phenotype"),
            "sex": _val(h, "organism/Cavia porcellus/phenotypic_sex"),
            "maturity": _val(h, "organism/Cavia porcellus/maturity"),
            "xe991_uM": _val(h, _A + "chemical solution/extracellular solution/concentration/Xe991"),
            "cs_glutamate_mM": _val(h, _A + "chemical solution/solution in pipette/concentration/CsGlutamate"),
            "cscl_pipette_mM": _val(h, _A + "chemical solution/solution in pipette/concentration/CsCl"),
            "mgcl2_pipette_mM": _val(h, _A + "chemical solution/solution in pipette/concentration/MgCl2"),
            "temperature_C": _val(h, _A + "study design controlled variable/temperature"),
            "pressure_kPa": _val(h, _A + "study design controlled variable/pipette_pressure"),
            "t_after_death_min": _val(h, _A + "time_interval_from_death"),
            "f1_Hz": _val(h, _A + "intracellular electrophysiology stimulus/frequency")[0],
            "f2_Hz": _val(h, _A + "intracellular electrophysiology stimulus/frequency")[1],
            "diameter_um": _val(h, "cell/outer hair cell/morphology/measurement datum/cell_diameter"),
            "length_um": _val(h, "cell/outer hair cell/morphology/measurement datum/cochlear_outer_hair_cell_length"),
            "lw_length_um": _val(h, "cell/outer hair cell/morphology/measurement datum/"
                                    "cochlear_outer_hair_cell_lateral_wall_length"),
            "area_um2": _val(h, "cell/outer hair cell/morphology/predicted data item/cell_surface_area"),
        }
        lin, nl = _T + "linear (voltage-independent) data set/", _T + "non-linear (voltage-dependent) data set/"
        r["CL"], r["CL_sd"] = _val(h, lin + "LC_f1_mean")
        r["CL_f2"] = _val(h, lin + "LC_f2_mean")[0]
        r["Rm"] = _val(h, lin + "Rm_mean")[0]
        r["Rs"] = _val(h, lin + "Rs_mean")[0]
        r["VD"] = _val(h, lin + "voltage_drop_across_membrane")
        r["V05_raw"], r["V05"] = _val(h, nl + "V_0p5")
        r["QTm"] = _val(h, nl + "Qmax_f1")
        r["QTm_f2"] = _val(h, nl + "Qmax_f2")
        r["alphaB"] = _val(h, nl + "alpha_f1")
        r["alphaB_f2"] = _val(h, nl + "alpha_f2")
        r["NLC_peak"] = _val(h, nl + "NLC_f1_peak")
        rows.append(r)
        traces[num] = {
            "V": _val(h, _A + "intracellular electrophysiology stimulus/membrane_potential"),
            "t": _val(h, _A + "intracellular electrophysiology stimulus/time"),
            "C": _val(h, _A + "predicted data item/membrane_capacitance(Cmf1)"),
            "C2": _val(h, _A + "predicted data item/membrane_capacitance(Cmf2)"),
            "Rm": _val(h, _A + "predicted data item/membrane_resistance(Rm)"),
            "Rs": _val(h, _A + "predicted data item/series_resistance(Rs)"),
            "NLC": _val(h, nl + "NLC_f1"),
            "NLV": _val(h, nl + "membrane_potential"),
            "q": _val(h, nl + "q_f1"),
            "IV_V": _val(h, _IV + "intracellular electrophysiology stimulus/membrane_potential"),
            "IV_I": _val(h, _TIV + "I_mean"),
            "IV_steps": _val(h, _TIV + "membrane_potential"),
            "IV_R": _val(h, _TIV + "R_b"),
        }
    df = pd.DataFrame(rows).set_index("file")
    return derive(df), traces


def derive(df: pd.DataFrame) -> pd.DataFrame:
    """Per-cell quantities of the claims file's shared method."""
    df = df.copy()
    df["xe991"] = df["xe991_uM"].fillna(0) > 0
    # 140 mM CsCl + 2 x 2 mM MgCl2 = 144 mM chloride; 6 + 4 = 10 mM with CsGlutamate.
    df["chloride_mM"] = df["cscl_pipette_mM"] + 2 * df["mgcl2_pipette_mM"]
    df["pigmented"] = df["phenotype"].eq("normal")
    df["colony"] = np.where(df["pigmented"], "pigmented", "albino")
    df["adult"] = df["maturity"].eq("mature")
    df["region"] = df["polarity"].where(df["polarity"].isin(["basal", "apical"]))     # reading r-a
    df["region_rb"] = df["turn"].map({1: "basal", 4: "apical"})                         # reading r-b
    df["CLW"] = df["CL"] - CNLW
    df["dVmin"] = df["QTm"] / df["CLW"]                      # pC / pF = V (Eq. 2c)
    df["alpha"] = df["alphaB"] / 4                           # Eq. 8d as rebuilt
    df["z"] = df["alphaB"] * KT / E0                         # Eq. 5
    df["C_Leq_aF"] = df["z"] * E0 / df["dVmin"] * 1e18       # n e0 / dVmin with n = z (delta = 1)
    df["Vh"] = df["V05"] - df["dVmin"] / 2                    # Eq. 3b as rebuilt
    df["Vd"] = df["V05"] + df["dVmin"] / 2
    df["drop_pos"] = 1 - df["VD"]                            # Rs/(Rs+Rm) at positive voltages
    return df


# --- recomputation from the traces ---------------------------------------------------------------

def ramp_indices(V: np.ndarray) -> tuple[int, int]:
    """First and last index of the DC ramp (-0.18 to +0.18 V): the longest run of equal positive
    voltage steps. The analysis script of the data set looks for the holding level of -0.06 V, but
    one file holds at +0.06 V, so the run of steps is used; the transition points are left out."""
    dv = np.diff(V)
    step = np.median(dv[dv > 0])
    ok = np.isclose(dv, step, rtol=0.2)
    best, start = (0, 0), None
    for i, o in enumerate(np.r_[ok, False]):
        if o and start is None:
            start = i
        elif not o and start is not None:
            if i - start > best[1] - best[0]:
                best = (start, i)
            start = None
    return best[0], best[1]


def cln_readings(V: np.ndarray, C: np.ndarray, CL: float) -> dict:
    """Linear capacitance at negative voltages, CLn, which the data set does not store and the paper
    does not define beyond "the capacitance had not reached its plateau (hyperpolarized) value"
    (Results, Asymmetry, paragraph 1). Readings:

    - `first2`: mean C over the two most negative ramp points (gives the legend's 25.94 pF for the
      example cell of Fig. S1, so it is the reading the legend supports);
    - `below_m015`: mean C over the ramp points at or below -0.15 V.

    `plateau_slope` is the slope of C on V over the points at or below -0.15 V, in pF/V, and
    `rise_slope` the largest slope over 5-point windows on the hyperpolarized flank, so a plateau
    criterion can be stated as their ratio (a choice; shown with several thresholds in the notebook).
    """
    i0, i1 = ramp_indices(V)
    v, c = V[i0:i1 + 1], C[i0:i1 + 1]
    neg = v <= -0.15
    out = {"first2": float(np.mean(c[:2])), "below_m015": float(np.mean(c[neg]))}
    out["plateau_slope"] = float(np.polyfit(v[neg], c[neg], 1)[0]) if neg.sum() >= 3 else np.nan
    peak = int(np.argmax(np.where(v < 0.05, c, -np.inf)))
    slopes = [np.polyfit(v[j:j + 5], c[j:j + 5], 1)[0] for j in range(0, max(peak - 4, 1))]
    out["rise_slope"] = float(np.max(slopes)) if slopes else np.nan
    return out


def recompute_cell(tr: dict, CL: float) -> dict:
    """QTm and alphaB recomputed from the stored NLC and charge traces (Expressions..., paragraph 2:
    QTm is the sum of CNL dV; the script's alphaB is 4 max d(q/QTm)/dV)."""
    nlc, v = tr["NLC"], tr["NLV"]
    dv = np.median(np.diff(v))
    q = np.cumsum(nlc) * dv
    qtm = float(np.max(q))
    a = np.diff(tr["q"] / np.max(tr["q"])) / dv
    return {"QTm_re": qtm, "alphaB_re": float(4 * np.max(a))}


# --- statistics ------------------------------------------------------------------------------------

def ols(x, y, w=None, intercept=True):
    """Weighted least squares; returns slope, intercept, their standard errors, R2, adjusted R2 and
    the p-value of the slope. Adjusted R2 as in MATLAB's fit: 1 - (SSE/(n-m)) / (SST/(n-1))."""
    x, y = np.asarray(x, float), np.asarray(y, float)
    w = np.ones_like(x) if w is None else np.asarray(w, float)
    X = np.c_[x, np.ones_like(x)] if intercept else x[:, None]
    W = np.sqrt(w)
    beta, *_ = np.linalg.lstsq(X * W[:, None], y * W, rcond=None)
    res = y - X @ beta
    n, m = len(x), X.shape[1]
    sse = np.sum(w * res**2)
    ybar = np.sum(w * y) / np.sum(w) if intercept else 0.0
    sst = np.sum(w * (y - ybar) ** 2)
    r2 = 1 - sse / sst
    adj = 1 - (sse / (n - m)) / (sst / (n - 1))
    cov = sse / (n - m) * np.linalg.inv((X * W[:, None]).T @ (X * W[:, None]))
    se = np.sqrt(np.diag(cov))
    tval = beta[0] / se[0]
    p = 2 * stats.t.sf(abs(tval), n - m)
    return {"slope": beta[0], "intercept": beta[1] if intercept else 0.0, "se_slope": se[0],
            "se_intercept": se[1] if intercept else np.nan, "r2": r2, "adj_r2": adj, "p_slope": p,
            "n": n, "dfe": n - m}


def fit_eq3a(dvmin, v05, w=None, weighted_r2=True):
    """Fit V0.5 = Vd - dVmin/2 (Eq. 3a as rebuilt) with Vd the only free parameter, weighted by w
    (the number of cells per bin, Fig. 3a legend). R2 = 1 - SSE/SST, with one coefficient MATLAB's
    adjusted R2 equals R2. With weighted_r2 False the R2 is computed without the weights."""
    dvmin, v05 = np.asarray(dvmin, float), np.asarray(v05, float)
    w = np.ones_like(dvmin) if w is None else np.asarray(w, float)
    vd = np.sum(w * (v05 + dvmin / 2)) / np.sum(w)
    pred = vd - dvmin / 2
    ww = w if weighted_r2 else np.ones_like(w)
    ybar = np.sum(ww * v05) / np.sum(ww)
    r2 = 1 - np.sum(ww * (v05 - pred) ** 2) / np.sum(ww * (v05 - ybar) ** 2)
    return {"Vd": vd, "adj_r2": r2, "n": len(v05)}


def bin_cells(df: pd.DataFrame, col: str, width: float, start: float = 0.0) -> pd.DataFrame:
    """Group cells by `col` in bins of `width` with edges at start + k width; per bin the count and
    the means (and SEM) of dVmin, V0.5, CLW, z, alphaB."""
    k = np.floor((df[col] - start) / width).astype(int)
    g = df.assign(bin=k).groupby("bin")
    out = g.agg(n=("V05", "size"), dVmin=("dVmin", "mean"), V05=("V05", "mean"),
                V05_sem=("V05", "sem"), CLW=("CLW", "mean"), z=("z", "mean"),
                alphaB=("alphaB", "mean"), QTm=("QTm", "mean"))
    out["lo"] = start + out.index * width
    return out


def anova1(*groups):
    """One-way ANOVA (F, p)."""
    f, p = stats.f_oneway(*groups)
    return float(f), float(p)


def load_mat(z: zipfile.ZipFile | None = None) -> pd.DataFrame:
    """Scalars of the original MATLAB files (Original_Data/R1_*_mat2hdf5_out.mat), for a cross-check
    of the HDF5 translation: the `toxins` label, cell number, turn, CL and the ramp indices."""
    z = z or open_zip()
    rows = []
    for name in sorted(n for n in z.namelist() if n.startswith("data_and_scripts/Original_Data/")
                       and n.endswith(".mat")):
        m = sio.loadmat(io.BytesIO(z.read(name)), squeeze_me=True, struct_as_record=False)
        arr = np.atleast_1d(m["array_of_do_fits"])
        for s in arr:
            rows.append({"mat_file": name.rsplit("/", 1)[1], "cellnumber": int(s.cellnumber),
                         "toxins": s.toxins, "turn": int(s.turn), "CL": float(s.LC_low_mean[0]),
                         "Vmcorr": float(s.Vmcorr), "dT": float(s.dT),
                         "intracellularchloride": float(s.intracellularchloride),
                         "phenotype": s.phenotype, "sex": s.sex, "agetype": s.agetype,
                         "IV_I_mean": np.asarray(s.I_mean)})
    return pd.DataFrame(rows)


def with_cnlw(df: pd.DataFrame, cnlw: float) -> pd.DataFrame:
    """The per-cell quantities with another non-lateral-wall capacitance. The claims file uses
    4.82 pF; 5.89 pF is the value implied by the Fig. S1 legend (CL 24.45 pF, CLW 18.56 pF) and is
    shown as a variant (see the question for a reader in questions/crcns-ear-1.yaml)."""
    df = df.copy()
    df["CLW"] = df["CL"] - cnlw
    df["dVmin"] = df["QTm"] / df["CLW"]
    df["C_Leq_aF"] = df["z"] * E0 / df["dVmin"] * 1e18
    df["Vh"] = df["V05"] - df["dVmin"] / 2
    df["Vd"] = df["V05"] + df["dVmin"] / 2
    return df


def iv_table(tr: dict) -> pd.DataFrame | None:
    """Mean steady-state current at each voltage step. The HDF5 array `I_mean` has shape (N, 2) but
    holds its values in MATLAB's column order (first the N means, then the N SDs); read as given
    the mean and SD columns are interleaved (the original MATLAB files hold them as columns). It is
    reshaped here to (2, N)."""
    i = np.asarray(tr["IV_I"])
    if i.size == 0:
        return None
    n = len(tr["IV_steps"])
    flat = i.ravel()
    return pd.DataFrame({"V": tr["IV_steps"], "I_pA": flat[:n], "I_sd_pA": flat[n:2 * n]})


def dc_conductance_at(tr: dict, v: float) -> float:
    """DC chord conductance (nS) between the two voltage steps around v (Methods, Whole-cell
    patch-clamp, paragraph 2: "The DC conductance was measured between -0.1 and 0.1 V with a voltage
    step-function"). Steps are taken in ramp order, without the holding steps at the ends."""
    t = iv_table(tr)
    if t is None:
        return np.nan
    s = t.iloc[1:-1].sort_values("V")
    vv, ii = s["V"].to_numpy(), s["I_pA"].to_numpy()
    k = np.searchsorted(vv, v)
    k = min(max(k, 1), len(vv) - 1)
    return float((ii[k] - ii[k - 1]) / (vv[k] - vv[k - 1]) * 1e-3)   # pA/V = pS; to nS


def groups(df: pd.DataFrame, how: str) -> pd.DataFrame:
    """Groups of cells for Fig. 4d to f and Table 3 (fig4d-cleq-two-limits, readings j-a to j-c):
    `clw5` the 5 pF CLW bins of Fig. 3a, `dv001` the 0.01 V dVmin bins of Fig. S4, `cell` per cell.
    Bins are formed separately for the cells with and without XE991 (Fig. 3a and S4 plot the two
    sets apart) and then pooled. Per group the means of V0.5, z and dVmin, and C_Leq = z e0 / dVmin
    from the group means."""
    parts = []
    for xe, s in df.groupby("xe991"):
        if how == "cell":
            g = s[["V05", "z", "dVmin", "alphaB"]].assign(n=1)
        else:
            col, w = ("CLW", 5.0) if how == "clw5" else ("dVmin", 0.01)
            k = np.floor(s[col] / w).astype(int)
            g = s.assign(bin=k).groupby("bin").agg(V05=("V05", "mean"), z=("z", "mean"),
                                                   dVmin=("dVmin", "mean"), alphaB=("alphaB", "mean"),
                                                   n=("V05", "size"))
        parts.append(g.assign(xe991=xe).reset_index(drop=True))
    out = pd.concat(parts, ignore_index=True)
    out["C_Leq_aF"] = out["z"] * E0 / out["dVmin"] * 1e18
    out["A_nm2"] = out["C_Leq_aF"] / SPECIFIC_C          # aF / (pF/um2) = 1e-6 um2 = nm2
    return out
