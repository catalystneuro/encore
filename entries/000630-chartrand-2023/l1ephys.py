"""Loading and electrophysiology features for the human L1 patch-seq data of dandiset 000630.

Chartrand et al. (2023), Science 382, eadf0805, doi:10.1126/science.adf0805.

Each NWB file holds one cell, recorded with MIES at the Allen Institute: current clamp sweeps
(`CurrentClampSeries` in acquisition, `CurrentClampStimulusSeries` in stimulus/presentation),
named by their stimulus code (`stimulus_description`). The file names its cell in
`general/source_script_file_name` (for example H20.06.351.11.10.01.03) and its LIMS
`session_id`. Files are streamed from the archive at the pinned version into memory and read with
h5py; only the long square current clamp sweeps are kept, nothing is written to disk.

Where the parameters come from:

- Cell labels (t-type, homology subclass, layer, region, donor) come from the paper's code,
  github.com/AllenInstitute/patchseq_human_L1 at commit LABELS_COMMIT, file
  data/human_l1_dataset_2023_02_06.csv, with the strict L1 list human_l1_dataset_strict.csv
  and the homology table of patchseq_utils/l1_load.py (claims file, opening comment). The
  paper's own per-cell features, data/aibs_features_E.csv, are read as reading (b) of the
  claims file's open detail O1.
- Feature extraction follows the Methods ("Electrophysiology feature analysis"): spikes are
  detected with IPFX (dV/dt above 20 mV/ms, then refined); input resistance from all
  hyperpolarizing long squares between -10 and -90 pA (IPFX LongSquareAnalysis with
  subthresh_min_amp = -100, which keeps amplitudes above -100 pA); sag on the hyperpolarizing
  sweep whose response is closest to -100 mV (IPFX); rheobase and f-I slope; spike train
  features on the rheobase sweep and the sweep 40 pA above it (IPFX's "hero" sweep, 39 to
  61 pA above rheobase); single spike features of the first spike; the initial firing rate
  as the inverse of the first ISI; adaptation ratios between the first and third spike (and
  the first and third ISI) on the lowest amplitude long square with at least 4 spikes.
- The order of the adaptation ratio (third over first, or first over third) is not given by
  the Methods (claims file, O1). `ADAPT_RATIO_ORDER` is set to the order that agrees with the
  paper's per-cell table; the notebook shows the comparison for both orders.
- Sweep quality control follows the Methods' criteria as far as the files allow: the bias
  (leak) current within 0 +/- 100 pA, and the rms noise of the pre-stimulus baseline below
  0.2 mV over 1.5 ms and below 0.5 mV over 500 ms. The criterion "within 2 mV of target" needs
  the target potential, which the files do not state; it is not applied (a deviation).
- Which computed features enter reading (a) (`hybrid_table`) is chosen in the notebook: those
  within 1% of the paper's value for at least half of the cells. This is an assumption; the
  claims file's O1 does not say when a recomputed feature counts as computed.
- The code's filters (l1_load.py) set first_isi_inv_rheo and first_isi_inv_hero above 1000 Hz,
  and input_resistance above 1000 MOhm, to missing; `apply_code_filters` does the same.
"""

from __future__ import annotations

import io
import warnings
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import requests

DANDISET_ID = "000630"
DANDISET_VERSION = "0.230915.2257"
# The mouse comparison data (claims file: DANDI 000020 at the version the paper cites)
MOUSE_DANDISET_ID = "000020"
MOUSE_DANDISET_VERSION = "0.210913.1639"

LABELS_REPO = "https://raw.githubusercontent.com/AllenInstitute/patchseq_human_L1"
LABELS_COMMIT = "7777857c1b89b19735e45fd9c9bd7493cc1d805c"

SUBTHRESH_MIN_AMP = -100.0     # Methods: input resistance from -10 to -90 pA sweeps
MAX_LEAK_PA = 100.0            # Methods: leak 0 +/- 100 pA
MAX_RMS_SHORT_MV = 0.2         # Methods: rms noise over 1.5 ms
MAX_RMS_LONG_MV = 0.5          # Methods: rms noise over 500 ms
ADAPT_RATIO_ORDER = "third_over_first"   # set from the comparison with the paper's table

# Homology subclasses of the human L1 t-types (patchseq_utils/l1_load.py, `homology`).
HOMOLOGY = {
    "LAMP5 NMBR": "LAMP5", "LAMP5 DBP": "LAMP5", "LAMP5 LCP2": "LAMP5",
    "SST CHRNA4": "MC4R", "ADARB2 MC4R": "MC4R",
    "PAX6 CDH12": "PAX6", "PAX6 TNFAIP8L3": "PAX6",
    "VIP TSPAN12": "L1 VIP",
    "SST BAGE2": "other", "VIP PCDH20": "other",
}
SUBCLASSES = ["LAMP5", "MC4R", "PAX6", "L1 VIP"]
HOMOLOGY_MOUSE = {
    "Lamp5 Lsp1": "LAMP5", "Lamp5 Plch2 Dock5": "LAMP5", "Lamp5 Ntn1 Npy2r": "LAMP5",
    "Lamp5 Fam19a1 Tmem182": "MC4R", "Lamp5 Fam19a1 Pax6": "MC4R",
    "Lamp5 Krt73": "PAX6",
    "Sncg Vip Nptx2": "L1 VIP", "Vip Col15a1 Pde1a": "L1 VIP",
}


API = "https://api.dandiarchive.org/api"


def version_metadata(dandiset_id: str = DANDISET_ID, version: str = DANDISET_VERSION) -> dict:
    """The pinned version's metadata from the DANDI API."""
    r = requests.get(f"{API}/dandisets/{dandiset_id}/versions/{version}/", timeout=60)
    r.raise_for_status()
    return r.json()


def list_assets(dandiset_id: str = DANDISET_ID, version: str = DANDISET_VERSION) -> pd.DataFrame:
    """Path, size, asset id and S3 URL of every asset of a pinned version."""
    url = f"{API}/dandisets/{dandiset_id}/versions/{version}/assets/?page_size=200&metadata=1"
    rows = []
    while url:
        r = requests.get(url, timeout=60)
        r.raise_for_status()
        page = r.json()
        for a in page["results"]:
            s3 = [u for u in a["metadata"]["contentUrl"] if "s3.amazonaws.com" in u][0]
            rows.append({"path": a["path"], "size": a["size"], "asset_id": a["asset_id"], "url": s3})
        url = page["next"]
    return pd.DataFrame(rows).sort_values("path").reset_index(drop=True)


def read_table(name: str, **kwargs) -> pd.DataFrame:
    """A CSV file of the paper's code repository at the pinned commit, read into memory."""
    r = requests.get(f"{LABELS_REPO}/{LABELS_COMMIT}/data/{name}", timeout=120)
    r.raise_for_status()
    return pd.read_csv(io.BytesIO(r.content), **kwargs)


def load_labels() -> pd.DataFrame:
    """Per-cell labels of the paper's code (human_l1_dataset_2023_02_06.csv), with the code's
    homology subclass, the strict L1 flag (human_l1_dataset_strict.csv) and collaborator AIBS
    for cells with no collaborator (l1_load.py)."""
    h = read_table("human_l1_dataset_2023_02_06.csv", index_col=0,
                   dtype={"layer_lims": str, "target_layer": str})
    strict = read_table("human_l1_dataset_strict.csv", index_col=0)
    depth = read_table("human_layer_depths_2023_02_06.csv", index_col="specimen_id")
    h["homology_type"] = h["t-type"].map(HOMOLOGY)
    h["collaborator"] = h["collaborator"].fillna("AIBS")
    h["in_strict_set"] = h.index.isin(strict.index)
    # l1_load.py: the depth table's layer ("Layer1", "Layer2/3") without its "Layer" prefix
    h = h.join(depth["layer"].map(lambda x: x[5:] if isinstance(x, str) and x else None))
    h["ephys_roi_id"] = pd.to_numeric(h.nwb_path.str.extract(r"Ephys_Roi_Result_(\d+)")[0])
    return h


def load_mouse_labels() -> pd.DataFrame:
    """Per-cell labels of the paper's mouse cells (mouse_l1_dataset_2023_02_06.csv), with the
    code's homology subclass, the strict mouse L1 list, the depth table's layer, and the code's
    strict_l1 flag (layer_ccf or layer 1), as l1_load.py builds them."""
    m = read_table("mouse_l1_dataset_2023_02_06.csv", index_col=0)
    strict = read_table("mouse_l1_dataset_strict.csv", index_col=0)
    depth = read_table("mouse_layer_depths_2022_09_02.csv", index_col="specimen_id")
    m["homology_type"] = m["t-type"].map(HOMOLOGY_MOUSE)
    m["in_strict_set"] = m.index.isin(strict.index)
    m = m.join(depth["layer"].map(lambda x: x[5:] if isinstance(x, str) and x else None))
    m["layer_ccf"] = m["layer_ccf"].astype("string")
    m["ephys_roi_id"] = pd.to_numeric(m.nwb_path.str.extract(r"Ephys_Roi_Result_(\d+)")[0])
    return m


def load_mouse_paper_features() -> pd.DataFrame:
    """The paper's per-cell features for the mouse cells (aibs_mouse_features_E.csv)."""
    return read_table("aibs_mouse_features_E.csv", index_col=0)


def load_paper_features() -> pd.DataFrame:
    """The paper's per-cell features for the Seattle cells (aibs_features_E.csv)."""
    return read_table("aibs_features_E.csv", index_col=0)


def apply_code_filters(df: pd.DataFrame) -> pd.DataFrame:
    """The code's filters on implausible values (l1_load.py)."""
    df = df.copy()
    for col, top in [("first_isi_inv_hero", 1000), ("first_isi_inv_rheo", 1000),
                     ("input_resistance_ss", 1000), ("input_resistance", 1000)]:
        if col in df:
            df.loc[df[col] > top, col] = np.nan
    return df


# --------------------------------------------------------------------------------------
# Reading sweeps

def _attr_str(x):
    return x.decode() if isinstance(x, bytes) else str(x)


_LS_CACHE = {}


def is_long_square(code: str) -> bool:
    """Whether IPFX's default stimulus ontology names a stimulus code a long square, as IPFX
    selects long square sweeps (`ontology.long_square_names`); search sweeps are left out."""
    from ipfx.stimulus import StimulusOntology
    import ipfx.json_utilities as ju
    if "ontology" not in _LS_CACHE:
        _LS_CACHE["ontology"] = StimulusOntology(ju.read(StimulusOntology.DEFAULT_STIMULUS_ONTOLOGY_FILE))
    key = code[:-5] if code.endswith("_DA_0") else code
    if key not in _LS_CACHE:
        onto = _LS_CACHE["ontology"]
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            try:
                names = {n for t in onto.find_one(key, tag_type="code").tags(tag_type="name") for n in t[1:]}
            except Exception:
                names = set()
        _LS_CACHE[key] = bool(names & set(onto.long_square_names))
    return _LS_CACHE[key]


def read_file(url: str) -> dict:
    """Metadata and long square sweeps of one file.

    Each sweep is returned as voltage (mV), current (pA), sampling rate (Hz), its stimulus
    code, its bias current (pA) and its sweep number."""
    # The file is streamed into memory in one request (no copy on disk), which is about thirty
    # times faster here than reading its many small sweeps through remfile.
    r = requests.get(url, timeout=300)
    r.raise_for_status()
    f = h5py.File(io.BytesIO(r.content), "r")
    out = {
        "cell_name": _attr_str(f["general/source_script"].attrs["file_name"]),
        "session_id": _attr_str(f["general/session_id"][()]),
        "subject_id": _attr_str(f["general/subject/subject_id"][()]),
        "sex": _attr_str(f["general/subject/sex"][()]),
        "age": _attr_str(f["general/subject/age"][()]),
        "species": _attr_str(f["general/subject/species"][()]),
        "institution": _attr_str(f["general/institution"][()]) if "institution" in f["general"] else None,
        "session_start": _attr_str(f["session_start_time"][()]),
    }
    acq, stim = f["acquisition"], f["stimulus/presentation"]
    codes, sweeps = {}, []
    for key in acq:
        g = acq[key]
        code = _attr_str(g.attrs.get("stimulus_description", ""))
        codes[code] = codes.get(code, 0) + 1
        if _attr_str(g.attrs.get("neurodata_type", "")) != "CurrentClampSeries":
            continue
        if not is_long_square(code):
            continue
        skey = key.replace("_AD", "_DA")
        if skey not in stim:
            continue
        rate = float(g["starting_time"].attrs["rate"])
        v = g["data"][()].astype(float) * float(g["data"].attrs["conversion"]) * 1e3
        i = stim[skey]["data"][()].astype(float) * float(stim[skey]["data"].attrs["conversion"]) * 1e12
        # bias_current is stored in pA although NWB states amperes (checked in the notebook)
        bias = float(np.ravel(g["bias_current"][()])[0]) if "bias_current" in g else np.nan
        sweeps.append({"key": key, "code": code, "rate": rate, "v": v, "i": i, "bias_pa": bias,
                       "sweep_number": int(g.attrs.get("sweep_number", -1))})
    out["codes"] = codes
    out["sweeps"] = sweeps
    f.close()
    return out


def sweep_qc(sw: dict) -> dict:
    """The Methods' sweep QC criteria that the files allow (see the module docstring), measured
    with IPFX's sweep QC functions: rms noise over 1.5 ms at the start of the experiment epoch
    (pre_noise_rms_mv) and over 500 ms before the stimulus (slow_noise_rms_mv), the bias current,
    and IPFX's check that the recording did not stop before the end of the experiment epoch."""
    from ipfx.sweep import Sweep
    import ipfx.qc_feature_extractor as qcfe
    t = np.arange(len(sw["v"])) / sw["rate"]
    sweep = Sweep(t=t, v=sw["v"], i=sw["i"], sampling_rate=sw["rate"], clamp_mode="CurrentClamp")
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        try:
            q = qcfe.current_clamp_sweep_qc_features(sweep, is_ramp=False)
            integrity = qcfe.check_sweep_integrity(sweep, is_ramp=False)
        except Exception as e:
            return {"passed": False, "qc_error": f"{type(e).__name__}"}
    # In these files samples after the recording stopped are zeros, not NaN as IPFX expects, so
    # a run of at least 10 samples at exactly 0 mV before the end of the stimulus marks a sweep
    # that stopped early.
    try:
        import ipfx.stim_features as stf
        start, dur, _, _, _ = stf.get_stim_characteristics(sw["i"], t)
        end_idx = int(min(start + min(dur, 1.0) + 0.2, t[-1]) * sw["rate"])
    except Exception:
        end_idx = len(t)
    z = (sw["v"][:end_idx] == 0).astype(int)
    zero_run = int(np.max(np.convolve(z, np.ones(10, dtype=int), mode="valid"))) >= 10 if end_idx > 10 else False
    if zero_run:
        integrity = list(integrity) + ["zeros before the end of the stimulus"]
    leak = sw["bias_pa"]
    out = {"pre_noise_rms_mv": q["pre_noise_rms_mv"], "slow_noise_rms_mv": q["slow_noise_rms_mv"],
           "leak_pa": leak, "integrity": "; ".join(integrity), "zeros": zero_run}
    out["passed"] = bool(
        not integrity
        and (np.isnan(leak) or abs(leak) <= MAX_LEAK_PA)
        and q["pre_noise_rms_mv"] is not None and q["pre_noise_rms_mv"] < MAX_RMS_SHORT_MV
        and q["slow_noise_rms_mv"] is not None and q["slow_noise_rms_mv"] < MAX_RMS_LONG_MV)
    return out


# --------------------------------------------------------------------------------------
# Features

def _first_spike_features(spikes: pd.DataFrame, suffix: str) -> dict:
    out = {}
    if spikes is None or len(spikes) == 0:
        return out
    s = spikes.iloc[0]
    for name in ["threshold_v", "peak_v", "width", "upstroke", "downstroke",
                 "upstroke_downstroke_ratio", "trough_v", "fast_trough_v"]:
        out[f"{name}_{suffix}"] = s.get(name, np.nan)
    out[f"peak_deltav_{suffix}"] = s.get("peak_v", np.nan) - s.get("threshold_v", np.nan)
    out[f"fast_trough_deltav_{suffix}"] = s.get("fast_trough_v", np.nan) - s.get("threshold_v", np.nan)
    return out


def _isis(spikes: pd.DataFrame) -> np.ndarray:
    return np.diff(spikes["threshold_t"].values) if spikes is not None and len(spikes) > 1 else np.array([])


def _nan_on_error(fn):
    def wrapped(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except Exception:
            return np.nan
    return wrapped


_PATCHED = False


def _patch_ipfx():
    """IPFX fails a whole cell when the membrane time constant cannot be fitted on one sweep
    (an empty fit window) or when fewer than two sweeps spike (no f-I slope). Here such a
    sweep's tau, or the cell's f-I slope, is missing instead, and the other features are kept."""
    global _PATCHED
    if _PATCHED:
        return
    import ipfx.stimulus_protocol_analysis as spa
    spa.subf.time_constant = _nan_on_error(spa.subf.time_constant)
    spa.strf.fit_fi_slope = _nan_on_error(spa.strf.fit_fi_slope)
    _PATCHED = True


def extract_features(rec: dict) -> dict:
    """IPFX long square features of one cell, named as in the paper's table."""
    from ipfx.sweep import Sweep, SweepSet
    import ipfx.stim_features as stf
    import ipfx.data_set_features as dsf
    import ipfx.stimulus_protocol_analysis as spa
    from ipfx.stimulus import StimulusType

    _patch_ipfx()
    out = {"n_long_square": len(rec["sweeps"])}
    if not rec["sweeps"]:
        out["error"] = "no long square sweeps"
        return out
    built, qcs = [], []
    for sw in rec["sweeps"]:
        t = np.arange(len(sw["v"])) / sw["rate"]
        try:
            start, dur, amp, _, _ = stf.get_stim_characteristics(sw["i"], t)
        except Exception:
            continue
        if start is None or dur is None:
            continue
        if dur > 1.05:
            # In some files the stimulus waveform keeps an offset after the 1 s step, and IPFX
            # then reads the step as lasting to the end of the sweep; take its end at the first
            # jump back of at least half the step.
            i0 = int(round(start * sw["rate"]))
            pre = sw["i"][i0 - int(0.01 * sw["rate"])]
            step = sw["i"][i0 + 10] - pre
            after = np.abs(sw["i"][i0 + 10:] - pre) < 0.5 * abs(step)
            if abs(step) > 0 and after.any():
                dur = (np.argmax(after) + 10) / sw["rate"]
        q = sweep_qc(sw)
        qcs.append(q)
        if not q["passed"]:
            continue
        # keep the analysed part: up to the end of the recorded response
        built.append((Sweep(t=t, v=sw["v"], i=sw["i"], sampling_rate=sw["rate"],
                            sweep_number=sw["sweep_number"], clamp_mode="CurrentClamp"),
                      start, dur, sw))
    out["n_sweeps_qc_failed"] = sum(not q["passed"] for q in qcs)
    out["n_sweeps_zero_padded"] = sum(bool(q.get("zeros")) for q in qcs)
    out["n_sweeps_used"] = len(built)
    if not built:
        out["error"] = "no long square sweep passed QC"
        return out
    # one stimulus window for the set, as IPFX takes it from the first sweep
    starts = pd.Series([round(b[1], 3) for b in built]).mode()[0]
    durs = pd.Series([round(b[2], 3) for b in built]).mode()[0]
    built = [b for b in built if abs(b[1] - starts) < 0.002 and abs(b[2] - durs) < 0.002
             and b[0].t[-1] >= starts + durs]
    sweeps = SweepSet([b[0] for b in built])
    out["stim_start_s"], out["stim_dur_s"] = float(starts), float(durs)
    # Clock check: on hyperpolarizing sweeps, the voltage change from the 100 ms before the
    # stimulus onset to 100 to 200 ms after it, and the same with the onset taken 0.3 s early.
    true_d, shifted_d = [], []
    for sw, st, du, raw in built:
        amp = np.median(raw["i"][int((st + 0.1) * raw["rate"]):int((st + 0.2) * raw["rate"])]) - \
            np.median(raw["i"][int((st - 0.1) * raw["rate"]):int(st * raw["rate"])])
        if amp < -5:
            for onset, store in [(st, true_d), (st - 0.3, shifted_d)]:
                pre = sw.v[int((onset - 0.1) * sw.sampling_rate):int(onset * sw.sampling_rate)]
                post = sw.v[int((onset + 0.1) * sw.sampling_rate):int((onset + 0.2) * sw.sampling_rate)]
                store.append(np.mean(post) - np.mean(pre))
    out["clock_dv_true_mv"] = float(np.median(true_d)) if true_d else np.nan
    out["clock_dv_shifted_mv"] = float(np.median(shifted_d)) if shifted_d else np.nan
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        try:
            spx, sptx = dsf.extractors_for_sweeps(sweeps, start=starts, end=starts + durs,
                                                  **dsf.detection_parameters(StimulusType.LONG_SQUARE))
            an = spa.LongSquareAnalysis(spx, sptx, subthresh_min_amp=SUBTHRESH_MIN_AMP,
                                        require_subthreshold=False, require_suprathreshold=False)
            feat = an.analyze(sweeps)
        except Exception as e:  # recorded, the cell then has no IPFX features
            out["error"] = f"{type(e).__name__}: {e}"
            return out
    for k in ["sag", "vm_for_sag", "input_resistance", "tau", "v_baseline", "rheobase_i",
              "fi_fit_slope"]:
        val = feat.get(k, np.nan)
        out[k] = float(val) if val is not None and np.isscalar(val) else np.nan
    spikes = an._spikes_set
    sweep_feats = an.all_sweep_features()
    amps = sweep_feats["stim_amp"].values
    for label, key in [("rheo", "rheobase_sweep"), ("hero", "hero_sweep")]:
        row = feat.get(key)
        if row is None or (hasattr(row, "empty") and row.empty):
            continue
        idx = row.name
        sp = spikes[idx]
        out[f"stim_amp_{label}"] = float(amps[idx])
        out.update(_first_spike_features(sp, label))
        for name in ["latency", "avg_rate", "mean_isi", "median_isi", "isi_cv", "adapt"]:
            val = row.get(name, np.nan)
            out[f"{name}_{label}"] = float(val) if val is not None else np.nan
        isis = _isis(sp)
        out[f"first_isi_inv_{label}"] = 1.0 / isis[0] if len(isis) else np.nan
        out[f"n_spikes_{label}"] = len(sp)
    # every spiking sweep as amplitude:spike count:inverse first ISI, to find which sweep a
    # value of the paper's table comes from
    out["spiking_sweeps"] = ";".join(
        f"{amps[k]:.1f}:{len(spikes[k])}:{(1.0 / _isis(spikes[k])[0]) if len(spikes[k]) > 1 else np.nan:.4f}"
        for k in np.argsort(amps) if len(spikes[k]) > 0)
    # f-I slope over spiking sweeps up to rheobase + 80 pA (Methods); IPFX's own fit over
    # all spiking sweeps is kept as fi_fit_slope_all
    out["fi_fit_slope_all"] = out["fi_fit_slope"]
    rates = sweep_feats["avg_rate"].values
    if np.isfinite(out.get("rheobase_i", np.nan)):
        import ipfx.spike_train_features as strf
        keep = (rates > 0) & (amps <= out["rheobase_i"] + 80 + 1e-6)
        if keep.sum() >= 2:
            out["fi_fit_slope"] = float(strf.fit_fi_slope(amps[keep], rates[keep]))
    # adaptation ratios on the lowest amplitude sweep with at least 4 spikes
    n_sp = np.array([len(s) for s in spikes])
    cand = np.where(n_sp >= 4)[0]
    if len(cand):
        k = cand[np.argmin(amps[cand])]
        # variants: the same ratio averaged over every sweep with at least 4 spikes
        for name in ["upstroke", "isi"]:
            vals = []
            for kk in cand:
                v = spikes[kk][name].values if name != "isi" else _isis(spikes[kk])
                if len(v) >= 3:
                    vals.append(v[2] / v[0])
            out[f"{name}_adapt_ratio_3over1_meansweeps"] = float(np.mean(vals)) if vals else np.nan
        sp = spikes[k]
        isis = _isis(sp)
        pairs = {"upstroke": sp["upstroke"].values, "downstroke": sp["downstroke"].values,
                 "width": sp["width"].values, "threshold_v": sp["threshold_v"].values,
                 "peak_v": sp["peak_v"].values, "isi": isis}
        for name, vals in pairs.items():
            if len(vals) >= 3:
                out[f"{name}_adapt_ratio_3over1"] = vals[2] / vals[0]
                out[f"{name}_adapt_ratio_1over3"] = vals[0] / vals[2]
        out["adapt_sweep_amp"] = float(amps[k])
    return out


def cell_features(url: str) -> dict:
    """Metadata, stimulus code counts and features of one file."""
    rec = read_file(url)
    feats = extract_features(rec)
    meta = {k: rec[k] for k in ["cell_name", "session_id", "subject_id", "sex", "age", "species",
                                "institution", "session_start"]}
    meta["n_ccs_codes"] = len(rec["codes"])
    meta["codes"] = ";".join(f"{c}:{n}" for c, n in sorted(rec["codes"].items()))
    return {**meta, **feats}


def all_cell_features(assets: pd.DataFrame, workers: int = 8) -> pd.DataFrame:
    """`cell_features` for every asset, streamed in parallel threads."""
    def one(row):
        try:
            return {"path": row.path, **cell_features(row.url)}
        except Exception as e:  # a file that cannot be read is reported, not skipped silently
            return {"path": row.path, "error": f"read failed: {type(e).__name__}: {e}"}
    with ThreadPoolExecutor(workers) as ex:
        rows = list(ex.map(one, [r for r in assets.itertuples()]))
    return pd.DataFrame(rows)


def with_adapt_order(df: pd.DataFrame, order: str = ADAPT_RATIO_ORDER) -> pd.DataFrame:
    """Name the adaptation ratios as the paper's table does, in the chosen order."""
    df = df.copy()
    suffix = "3over1" if order == "third_over_first" else "1over3"
    for name in ["upstroke", "downstroke", "width", "threshold_v", "peak_v", "isi"]:
        col = f"{name}_adapt_ratio_{suffix}"
        if col in df:
            df[f"{name}_adapt_ratio"] = df[col]
    return df


# --------------------------------------------------------------------------------------
# Feature tables

def feature_columns(paper: pd.DataFrame) -> list:
    """The paper's electrophysiology features: every column of its table that is not a QC
    column (l1_load.py, `ephys_features`)."""
    return [c for c in paper.columns if "qc" not in c and "fail" not in c]


def hybrid_table(computed: pd.DataFrame, paper: pd.DataFrame, computed_cols: list) -> pd.DataFrame:
    """Reading (a) of O1: the features computed here from the NWB files where they could be
    computed (`computed_cols`), and the paper's per-cell values (reading (b)) for the others.
    Both tables are indexed by the paper's specimen id."""
    out = paper.copy()
    common = out.index.intersection(computed.index)
    for c in computed_cols:
        out[c] = np.nan
        out.loc[common, c] = computed.loc[common, c].astype(float)
    return out


# --------------------------------------------------------------------------------------
# Statistics, as the paper's code computes them (patchseq_utils/analysis.py at LABELS_COMMIT)

def run_kw_dunn(data, features, group_col, posthoc="dunn", cutoff=0.05):
    """Kruskal-Wallis per feature, epsilon2 = H/(n-1), Benjamini-Hochberg across features, and
    for each feature with FDR p < cutoff pairwise post hoc tests (Dunn's, or two-sided
    Mann-Whitney with posthoc='mw'), Benjamini-Hochberg across pairs (run_kw_dunn)."""
    from scipy.stats import kruskal, mannwhitneyu
    from statsmodels.stats.multitest import multipletests
    import scikit_posthocs as skp
    recs = []
    for f in features:
        df = data.dropna(subset=[f, group_col])
        groups = [g[f].values for _, g in df.groupby(group_col, observed=True)]
        if len(groups) < 2:
            continue
        h, p = kruskal(*groups)
        recs.append({"feature": f, "KW_H": h, "pval": p, "epsilon2": h / (len(df) - 1), "n": len(df)})
    res = pd.DataFrame(recs).set_index("feature")
    res["pval_fdr"] = multipletests(res["pval"], method="fdr_bh")[1]
    pairs_out = {}
    for f in res.index[res.pval_fdr < cutoff]:
        df = data.dropna(subset=[f, group_col])
        levels = [x for x in pd.Categorical(df[group_col]).categories if (df[group_col] == x).any()]
        pairs = [(a, b) for i, a in enumerate(levels) for b in levels[i + 1:]]
        if posthoc == "dunn":
            pm = skp.posthoc_dunn(df, val_col=f, group_col=group_col, p_adjust=None)
            pv = [pm.loc[a, b] for a, b in pairs]
        else:
            pv = [mannwhitneyu(df.loc[df[group_col] == a, f], df.loc[df[group_col] == b, f]).pvalue
                  for a, b in pairs]
        pv = multipletests(pv, method="fdr_bh")[1]
        pairs_out[f] = dict(zip([f"{a} - {b}" for a, b in pairs], pv))
    return res.sort_values("pval"), pairs_out


def dunn_pairs(data, feature, group_col, pairs):
    """Dunn's test p-values for the listed pairs, Benjamini-Hochberg across them."""
    import scikit_posthocs as skp
    from statsmodels.stats.multitest import multipletests
    df = data.dropna(subset=[feature, group_col])
    pm = skp.posthoc_dunn(df, val_col=feature, group_col=group_col, p_adjust=None)
    pv = multipletests([pm.loc[a, b] for a, b in pairs], method="fdr_bh")[1]
    return pd.Series(pv, index=[f"{a} - {b}" for a, b in pairs])


def run_twosamp(df, features, variable):
    """Two-sided exact Mann-Whitney per feature, r = 2 AUC - 1, Benjamini-Hochberg (run_twosamp)."""
    from scipy.stats import mannwhitneyu
    from statsmodels.stats.multitest import multipletests
    recs = []
    for f in features:
        d = df.dropna(subset=[variable, f])
        groups = [g[f].values for _, g in d.groupby(variable)]
        if len(groups) != 2 or min(len(g) for g in groups) == 0:
            continue
        u, p = mannwhitneyu(groups[0], groups[1], method="exact")
        auc = u / (len(groups[0]) * len(groups[1]))
        recs.append({"feature": f, "pval_mw": p, "auc_first_group": auc,
                     "mw_r": 2 * max(auc, 1 - auc) - 1, "nobs": len(d)})
    res = pd.DataFrame(recs).set_index("feature")
    res["pval_mw_fdr"] = multipletests(res["pval_mw"], method="fdr_bh")[1]
    return res.sort_values("pval_mw")


def run_correlations(data, features, xvar, filter_dropouts=True):
    """Spearman correlation of each feature with xvar, Benjamini-Hochberg; with filter_dropouts
    a feature with fewer than 5 values above 1 is left out first (run_correlations)."""
    from scipy.stats import spearmanr
    from statsmodels.stats.multitest import multipletests
    recs = []
    for f in features:
        if filter_dropouts and (data[f] > 1).sum() < 5:
            continue
        d = data.dropna(subset=[f, xvar])
        r, p = spearmanr(d[f], d[xvar])
        recs.append({"feature": f, "r": r, "pval": p, "n": len(d)})
    res = pd.DataFrame(recs).set_index("feature").dropna(subset=["pval"])
    res["pval_fdr"] = multipletests(res["pval"], method="fdr_bh")[1]
    return res.sort_values("pval")


# --------------------------------------------------------------------------------------
# Multivariate measures (patchseq_utils/cluster_pairs.py, pipelines.py, clustering.py)

def preproc_pipeline():
    """RobustScaler, KNN imputation, per-feature LocalOutlierFactor < -20 set missing, KNN
    imputation again (pipelines.py, preproc_pipeline; Methods, Discriminant analysis)."""
    from sklearn.base import BaseEstimator, TransformerMixin
    from sklearn.impute import KNNImputer
    from sklearn.neighbors import LocalOutlierFactor
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import RobustScaler

    class OutlierExtraction(BaseEstimator, TransformerMixin):
        def fit(self, X, y=None):
            return self

        def transform(self, X):
            X = np.array(X, dtype=float)
            lof = LocalOutlierFactor()
            for j in range(X.shape[1]):
                lof.fit_predict(X[:, [j]])
                X[lof.negative_outlier_factor_ < -20, j] = np.nan
            return X

    return Pipeline([("norm", RobustScaler()), ("impute1", KNNImputer()),
                     ("outliers", OutlierExtraction()), ("impute2", KNNImputer())])


def dprime_auc(y_true, y_score):
    """d' = sqrt(2) times the inverse normal of the ROC AUC; an AUC of 1 is replaced by (n-1)/n
    (cluster_pairs.py, dprime)."""
    from scipy.stats import norm
    from sklearn.metrics import roc_auc_score
    area = roc_auc_score(y_true, y_score)
    if np.isclose(area, 1):
        area = (len(y_true) - 1) / len(y_true)
    return np.sqrt(2) * norm.ppf(area)


def pairwise_dprime(data, features, cluster_col, seed):
    """Pairwise d' of the clusters from a random forest (class_weight balanced_subsample),
    scored by cross_val_predict probabilities with 5 stratified folds (scikit-learn's default,
    as cluster_pairs.py calls it with cv=None). The random seed is a standard choice; the
    code sets none."""
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import StratifiedKFold, cross_val_predict
    X = preproc_pipeline().fit_transform(data[features].values)
    types = data[cluster_col].astype("category").cat.remove_unused_categories()
    order = list(types.cat.categories)
    codes = types.cat.codes.values
    D = pd.DataFrame(np.nan, index=order, columns=order)
    for i in range(len(order)):
        for j in range(i):
            sub = np.isin(codes, [i, j])
            y = codes[sub] == i
            clf = RandomForestClassifier(class_weight="balanced_subsample", random_state=seed)
            cv = StratifiedKFold(5, shuffle=False)
            prob = cross_val_predict(clf, X[sub], y, cv=cv, method="predict_proba")[:, 1]
            D.iloc[i, j] = D.iloc[j, i] = dprime_auc(y, prob)
    return D
