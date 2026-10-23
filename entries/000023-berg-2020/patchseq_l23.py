"""Loading and feature extraction for dandiset 000023 (human Patch-seq, Allen Institute, June 2020).

The dandiset holds one NWB file per neuron: whole-cell current clamp recorded with MIES, with the
Allen pipeline's spike times under processing/spikes. Each file is read whole into memory from the
archive's S3 store (no copy on disk) and passed to IPFX, which reads NWB files from a buffer.

Where the parameters come from:

- The 18 features and their names are those of the paper's code (data/ephys_feature_names.csv at
  AllenInstitute/patchseq_human_L23 commit 3daf9f0), as the claims file lists them. IPFX gives the
  underlying quantities; how each named feature is read from IPFX's output is in FEATURE_SOURCES.
  The code does not hold the step that made its table from IPFX, so this reading follows the names
  (`_hero` from the hero sweep, about 50 pA above rheobase; `_rheo` and `_long_square` from the first
  spike of the rheobase sweep; `_rel` relative to AP threshold; `adapt_mean` the mean adaptation
  over the spiking long squares, which matched the table where the hero sweep's adaptation did
  not), and the link claim checks it.
- Sweep QC is the Methods' (the claims file's link criterion asks for it): bridge balance below
  20 MOhm and below 15% of input resistance, bias current within +/-100 pA, and RMS noise below 0.07
  mV (short windows) and 0.5 mV (long window). IPFX 2.1.2's own sweep QC (qc_current_clamp_sweep)
  applies only the noise limits and a Vm-delta limit of its default criteria
  (ipfx/defaults/qc_criteria.json); the bias current and bridge balance limits are in that file but
  not applied to sweeps. So the Methods' two limits are added here (METHODS_SWEEP_QC) on IPFX's
  sweep table (leak_pa, the bias current, and bridge_balance_mohm), with the input resistance of
  IPFX's cell QC for the 15% limit; a sweep with no value is kept. The features under IPFX's sweep
  QC alone are kept too, as a variant (columns prefixed `ipfxqc_`). Cell QC is computed and
  reported but not used to drop cells: the claims file asks for sweep QC only.
- Long squares are analysed as IPFX's extract_cell_long_square_features does, except that a cell
  with no hero sweep keeps its other features (IPFX would drop the whole long-square set); this is
  how the code's table has cells with first_isi_hero_inv or avg_rate_hero missing and other features
  present.
- Non-positive input resistance, f-I slope and sag are set missing, as the code does
  (hivscc_data.load_data); the claims file's "common method" relies on it.
- The window for counting spikes outside the step in the clock check (1 s before the step) is a
  standard choice that cannot change a claim's outcome.
"""
from __future__ import annotations

import io
import json
import logging
import os
import time
import urllib.request
import warnings

import h5py
import numpy as np
import pandas as pd

DANDISET = "000023"
VERSION = "0.210914.1900"
API = "https://api.dandiarchive.org/api"
CODE_COMMIT = "3daf9f0803ea0c220a040ea523f23af5f93c56ac"
CODE_RAW = f"https://raw.githubusercontent.com/AllenInstitute/patchseq_human_L23/{CODE_COMMIT}/data/"

FEATURES = [
    "adapt_mean", "avg_rate_hero", "downstroke_long_square", "fast_trough_v_long_square_rel",
    "fi_fit_slope", "first_isi_hero_inv", "input_resistance", "latency_rheo",
    "peak_v_long_square_rel", "rheobase_i", "sag", "tau", "threshold_v_long_square",
    "trough_v_long_square_rel", "upstroke_downstroke_ratio_long_square", "upstroke_long_square",
    "v_baseline", "width_long_square",
]

FEATURE_SOURCES = {
    "adapt_mean": "spiking long squares: mean of adapt",
    "avg_rate_hero": "hero sweep: avg_rate",
    "downstroke_long_square": "rheobase sweep, first spike: downstroke",
    "fast_trough_v_long_square_rel": "rheobase sweep, first spike: fast_trough_v - threshold_v",
    "fi_fit_slope": "long squares: fi_fit_slope",
    "first_isi_hero_inv": "hero sweep: 1 / first_isi",
    "input_resistance": "long squares: input_resistance",
    "latency_rheo": "rheobase sweep: latency",
    "peak_v_long_square_rel": "rheobase sweep, first spike: peak_v - threshold_v",
    "rheobase_i": "long squares: rheobase_i",
    "sag": "long squares: sag",
    "tau": "long squares: tau",
    "threshold_v_long_square": "rheobase sweep, first spike: threshold_v",
    "trough_v_long_square_rel": "rheobase sweep, first spike: trough_v - threshold_v",
    "upstroke_downstroke_ratio_long_square": "rheobase sweep, first spike: upstroke_downstroke_ratio",
    "upstroke_long_square": "rheobase sweep, first spike: upstroke",
    "v_baseline": "long squares: v_baseline",
    "width_long_square": "rheobase sweep, first spike: width",
}

DROP_NONPOSITIVE = ["input_resistance", "fi_fit_slope", "sag"]

# The Methods' sweep QC limits that IPFX 2.1.2 does not apply to sweeps (see the docstring).
METHODS_SWEEP_QC = dict(bias_pa=100.0, bridge_mohm=20.0, bridge_frac_rin=0.15)

TYPE_ORDER = ["LTK", "GLP2R", "FREM3", "CARM1P1", "COL22A1"]


def _get_json(url):
    with urllib.request.urlopen(url) as r:
        return json.load(r)


def list_assets(version=VERSION):
    """All assets of the pinned version, with their S3 URL and the ids in their path."""
    url = f"{API}/dandisets/{DANDISET}/versions/{version}/assets/?page_size=1000"
    rows = []
    while url:
        page = _get_json(url)
        for a in page["results"]:
            b = a["blob"]
            sub, ses = a["path"].split("/")[1].replace("_icephys.nwb", "").split("_")
            rows.append(dict(path=a["path"], size=a["size"], subject_id=int(sub[4:]),
                             session_id=int(ses[4:]),
                             url=f"https://dandiarchive.s3.amazonaws.com/blobs/{b[:3]}/{b[3:6]}/{b}"))
        url = page["next"]
    return pd.DataFrame(rows)


def version_info(version=VERSION):
    return _get_json(f"{API}/dandisets/{DANDISET}/versions/{version}/")


def read_bytes(url, tries=4):
    """The whole file, in memory."""
    for k in range(tries):
        try:
            with urllib.request.urlopen(url, timeout=120) as r:
                return r.read()
        except Exception:
            if k == tries - 1:
                raise
            time.sleep(2 * (k + 1))


def code_table(name):
    """A table from the paper's code at the pinned commit."""
    return pd.read_csv(CODE_RAW + name.replace(" ", "%20"))


def _s(v):
    if isinstance(v, bytes):
        return v.decode()
    if isinstance(v, np.ndarray) and v.size == 1:
        return _s(v.reshape(-1)[0])
    return v


def file_metadata(raw):
    """Identifiers, units, rates and per-sweep amplifier settings of one file, from h5py."""
    f = h5py.File(io.BytesIO(raw), "r")
    out = dict(
        cell_name=_s(f["general/source_script"].attrs.get("file_name")),
        nwb_session_id=_s(f["general/session_id"][()]),
        nwb_subject_id=_s(f["general/subject/subject_id"][()]),
        age=_s(f["general/subject/age"][()]),
        sex=_s(f["general/subject/sex"][()]),
        species=_s(f["general/subject/species"][()]),
        session_start=_s(f["session_start_time"][()]),
    )
    sweeps = []
    for k, g in f["acquisition"].items():
        d = g["data"]
        sweeps.append(dict(
            series=k, kind=_s(g.attrs["neurodata_type"]), stim=_s(g.attrs.get("stimulus_description")),
            sweep_number=int(g.attrs["sweep_number"]), n=d.shape[0],
            rate=float(g["starting_time"].attrs["rate"]), unit=_s(d.attrs.get("unit")),
            conversion=float(d.attrs.get("conversion")),
            bridge_balance=float(g["bridge_balance"][0]) if "bridge_balance" in g else np.nan,
            bias_current=float(g["bias_current"][0]) if "bias_current" in g else np.nan,
        ))
    stored = {}
    if "processing/spikes" in f:
        for k, g in f["processing/spikes"].items():
            stored[int(k.split("_")[1])] = g["timestamps"][()]
    out["sweeps"] = sweeps
    out["stored_spikes"] = stored
    f.close()
    return out


def _long_square_features(ds):
    """IPFX's extract_cell_long_square_features without its abort when there is no hero sweep."""
    import ipfx.data_set_features as dsft
    import ipfx.stim_features as stf
    import ipfx.stimulus_protocol_analysis as spa
    from ipfx.data_set_features import detection_parameters, extractors_for_sweeps
    from ipfx.stimulus import StimulusType

    nums = ds.get_sweep_numbers(ds.ontology.long_square_names, clamp_mode=ds.CURRENT_CLAMP)
    if len(nums) == 0:
        raise ValueError("no long square sweeps passed QC")
    clsq = ds.filtered_sweep_table(clamp_mode=ds.CURRENT_CLAMP, stimuli=ds.ontology.coarse_long_square_names)
    if len(clsq) > 0:
        sub_min, _ = dsft.select_subthreshold_min_amplitude(clsq["stimulus_amplitude"])
    else:
        sub_min = -100
    sweeps = ds.sweep_set(nums)
    sweeps.align_to_start_of_epoch("experiment")
    start, dur, _, _, _ = stf.get_stim_characteristics(sweeps.sweeps[0].i, sweeps.sweeps[0].t)
    spx, spfx = extractors_for_sweeps(sweeps, start=start, end=start + dur,
                                      **detection_parameters(StimulusType.LONG_SQUARE))
    an = spa.LongSquareAnalysis(spx, spfx, subthresh_min_amp=sub_min)
    feats = an.analyze(sweeps)
    return an.as_dict(feats, [dict(sweep_number=sn) for sn in nums]), start, dur


def named_features(ls):
    """The 18 features of the paper's code from IPFX's long-square output (FEATURE_SOURCES)."""
    out = {k: np.nan for k in FEATURES}

    def g(d, k):
        try:
            v = d[k]
            return np.nan if v is None else float(v)
        except (KeyError, TypeError):
            return np.nan

    for k in ["fi_fit_slope", "input_resistance", "rheobase_i", "sag", "tau", "v_baseline"]:
        out[k] = g(ls, k)
    spk = ls.get("spiking_sweeps")
    if spk is not None and len(spk) and "adapt" in pd.DataFrame(spk):
        out["adapt_mean"] = float(pd.to_numeric(pd.DataFrame(spk)["adapt"], errors="coerce").mean())
    hero = ls.get("hero_sweep")
    if hero is not None:
        out["avg_rate_hero"] = g(hero, "avg_rate")
        fi = g(hero, "first_isi")
        out["first_isi_hero_inv"] = 1.0 / fi if fi and np.isfinite(fi) else np.nan
    rheo = ls.get("rheobase_sweep")
    if rheo is not None:
        out["latency_rheo"] = g(rheo, "latency")
        spikes = rheo.get("spikes") or []
        if spikes:
            s0 = spikes[0]
            thr = g(s0, "threshold_v")
            out["threshold_v_long_square"] = thr
            out["peak_v_long_square_rel"] = g(s0, "peak_v") - thr
            out["fast_trough_v_long_square_rel"] = g(s0, "fast_trough_v") - thr
            out["trough_v_long_square_rel"] = g(s0, "trough_v") - thr
            out["upstroke_long_square"] = g(s0, "upstroke")
            out["downstroke_long_square"] = g(s0, "downstroke")
            out["upstroke_downstroke_ratio_long_square"] = g(s0, "upstroke_downstroke_ratio")
            out["width_long_square"] = g(s0, "width")
    for k in DROP_NONPOSITIVE:
        if not (out[k] > 0):
            out[k] = np.nan
    return out


def _clock_check(raw, ls_sweeps, step_start, step_dur, rheo_sweep):
    """Upward crossings of 0 mV in and out of the step, and stored against IPFX spike times.

    Counts spikes over the whole response of every QC-passed long square, inside the step and in the
    1 s before it, from the raw trace (not IPFX, which only looks inside the step).
    """
    f = h5py.File(io.BytesIO(raw), "r")
    inside = before = 0
    for k, g in f["acquisition"].items():
        if int(g.attrs["sweep_number"]) not in ls_sweeps:
            continue
        d = g["data"]
        v = d[()] * float(d.attrs["conversion"]) * 1e3
        rate = float(g["starting_time"].attrs["rate"])
        i = f["stimulus/presentation"][k.replace("AD", "DA")]["data"][()]
        # the step: the longest run of the most common non-zero value after the test pulse
        nz = np.flatnonzero(np.abs(i) > 0)
        if len(nz) == 0:
            continue
        t = np.arange(len(v)) / rate
        up = t[1:][(v[1:] > 0) & (v[:-1] <= 0)]
        on = nz[nz > int(0.1 * rate)]
        if len(on) == 0:
            continue
        s0, s1 = on[0] / rate, on[-1] / rate
        inside += int(np.sum((up >= s0) & (up <= s1 + 0.01)))
        before += int(np.sum((up >= s0 - 1.0) & (up < s0)))
    f.close()
    return inside, before


def extract_cell(url, qc_criteria=None):
    """Metadata, sweep QC, the 18 features and the checks for one file. Never raises."""
    warnings.filterwarnings("ignore")
    logging.disable(logging.WARNING)
    import ipfx.json_utilities as ju
    import ipfx.sweep_props as sp
    from ipfx.bin.run_qc import run_qc
    from ipfx.dataset.create import create_ephys_data_set
    from ipfx.dataset.ephys_data_set import EphysDataSet
    from ipfx.qc_feature_extractor import cell_qc_features, sweep_qc_features
    from ipfx.stimulus import StimulusOntology

    out = dict(url=url, error=None)
    t0 = time.time()
    try:
        raw = read_bytes(url)
        out["bytes"] = len(raw)
        meta = file_metadata(raw)
        stored = meta.pop("stored_spikes")
        out.update(meta)
        if qc_criteria is None:
            import ipfx
            qc_criteria = ju.read(os.path.join(os.path.dirname(ipfx.__file__), "defaults", "qc_criteria.json"))
        # run_sweep_extraction's steps, on one reading of the file that is reused below
        ont = StimulusOntology(ju.read(StimulusOntology.DEFAULT_STIMULUS_ONTOLOGY_FILE))
        ds_all = create_ephys_data_set(nwb_file=io.BytesIO(raw), ontology=ont)
        cell_qc, _ = cell_qc_features(ds_all, {})
        se = dict(cell_features=cell_qc, sweep_features=sweep_qc_features(ds_all))
        sp.drop_tagged_sweeps(se["sweep_features"])
        sp.remove_sweep_feature("tags", se["sweep_features"])
        qc = run_qc(None, se["cell_features"], se["sweep_features"], qc_criteria)
        sp.assign_sweep_states(qc["sweep_states"], se["sweep_features"])
        out["cell_qc_failed"] = bool(qc["cell_state"]["failed_qc"])
        out["cell_qc_tags"] = "; ".join(qc["cell_state"].get("fail_tags", []))
        out["cell_qc_features"] = {k: (float(v) if isinstance(v, (int, float, np.floating)) and v is not None else v)
                                   for k, v in se["cell_features"].items()}
        # the Methods' bias current and bridge balance limits, which IPFX does not apply to sweeps
        rin = out["cell_qc_features"].get("input_resistance_mohm")
        rin = float(rin) if rin is not None and np.isfinite(rin) else np.nan
        lim = METHODS_SWEEP_QC
        for s in se["sweep_features"]:
            s["ipfx_passed"] = bool(s["passed"])
            extra = []
            bias, bb = s.get("leak_pa"), s.get("bridge_balance_mohm")
            if bias is not None and np.isfinite(bias) and abs(bias) > lim["bias_pa"]:
                extra.append("bias current")
            if bb is not None and np.isfinite(bb):
                if bb > lim["bridge_mohm"]:
                    extra.append("bridge balance")
                elif np.isfinite(rin) and bb > lim["bridge_frac_rin"] * rin:
                    extra.append("bridge balance over 15% of Rin")
            s["methods_fail"] = "; ".join(extra)
            s["passed"] = bool(s["passed"]) and not extra
        sw = pd.DataFrame(se["sweep_features"])
        ls_names = set(ont.long_square_names)
        is_ls = sw["stimulus_name"].isin(ls_names) if "stimulus_name" in sw else pd.Series(False, index=sw.index)
        out["n_iclamp_sweeps"] = int(len(sw))
        out["n_ls_sweeps"] = int(is_ls.sum())
        out["n_ls_passed"] = int((is_ls & sw["passed"].astype(bool)).sum()) if len(sw) else 0
        out["n_ls_passed_ipfx"] = int((is_ls & sw["ipfx_passed"].astype(bool)).sum()) if len(sw) else 0
        out["ls_amps"] = sorted(float(a) for a in sw.loc[is_ls, "stimulus_amplitude"].dropna()) if len(sw) else []
        out["ls_durations"] = sorted(set(round(float(a), 4) for a in sw.loc[is_ls, "stimulus_duration"].dropna())) if len(sw) else []
        # why long squares failed: IPFX's tags (by kind) and the Methods' added limits
        reasons = {}
        for st in qc["sweep_states"]:
            if int(st["sweep_number"]) in set(sw.loc[is_ls, "sweep_number"].astype(int)):
                for tag in st["reasons"]:
                    k = tag.split(":")[0].strip()
                    reasons[k] = reasons.get(k, 0) + 1
        for v in sw.loc[is_ls, "methods_fail"]:
            for k in filter(None, v.split("; ")):
                reasons["methods: " + k] = reasons.get("methods: " + k, 0) + 1
        out["ls_fail_reasons"] = reasons
        out["ls_bias_pa"] = [float(v) if v is not None else np.nan for v in sw.loc[is_ls, "leak_pa"]] if "leak_pa" in sw else []
        out["rin_cell_qc"] = rin
        variant = None
        if (sw["ipfx_passed"] != sw["passed"]).any():  # IPFX's sweep QC alone keeps other sweeps
            kept = [s for s in se["sweep_features"] if s["ipfx_passed"]]
            try:
                variant = named_features(_long_square_features(EphysDataSet(data=ds_all._data, sweep_info=kept))[0])
            except Exception as e:
                variant = {k: np.nan for k in FEATURES}
                out["ipfxqc_error"] = f"{type(e).__name__}: {e}"
        passed = [s for s in se["sweep_features"]]
        sp.drop_failed_sweeps(passed)
        ds = EphysDataSet(data=ds_all._data, sweep_info=passed)
        if variant is not None:
            out.update({"ipfxqc_" + k: v for k, v in variant.items()})
        ls, start, dur = _long_square_features(ds)
        out.update(named_features(ls))
        if variant is None:
            out.update({"ipfxqc_" + k: out[k] for k in FEATURES})
        out["has_hero"] = ls.get("hero_sweep") is not None
        spk = ls.get("spiking_sweeps")
        if spk is not None and len(spk):
            spk = pd.DataFrame(spk)
            out["spiking_sweeps"] = spk[[c for c in ["sweep_number", "stim_amp", "avg_rate", "adapt", "first_isi", "latency"]
                                         if c in spk]].to_dict("list")
        out["step_start"], out["step_dur"] = float(start), float(dur)
        rheo = ls.get("rheobase_sweep")
        rs = int(rheo["sweep_number"]) if rheo is not None else None
        out["rheo_sweep"] = rs
        # IPFX's rheobase spike times against the spike times stored in the file
        if rs is not None and rs in stored and rheo.get("spikes"):
            mine = np.array([s["threshold_t"] for s in rheo["spikes"]])
            st = np.asarray(stored[rs])
            out["stored_n"], out["ipfx_n"] = int(len(st)), int(len(mine))
            if len(st) and len(mine):
                out["stored_dt_ms"] = float(np.max([np.min(np.abs(st - m)) for m in mine]) * 1e3)
        ls_nums = set(int(s["sweep_number"]) for s in ls["sweeps"]) if "sweeps" in ls else set()
        out["spikes_in_step"], out["spikes_before_step"] = _clock_check(raw, ls_nums, start, dur, rs)
    except Exception as e:  # recorded and reported, never hidden
        out["error"] = f"{type(e).__name__}: {e}"
    out["seconds"] = time.time() - t0
    return out


def extract_all(urls, processes=4):
    """extract_cell over many files, in parallel processes, one thread of linear algebra each."""
    import multiprocessing as mp
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
    os.environ.setdefault("MKL_NUM_THREADS", "1")
    ctx = mp.get_context("fork")
    with ctx.Pool(processes, maxtasksperchild=20) as pool:
        rows = pool.map(extract_cell, list(urls), chunksize=1)
    return pd.DataFrame(rows)


# --- statistics used by several claims (the claims file's "common method") --------------------------

def bh(p):
    """Benjamini-Hochberg adjusted p-values, missing values kept missing."""
    p = np.asarray(p, float)
    out = np.full_like(p, np.nan)
    ok = np.isfinite(p)
    if ok.sum():
        from statsmodels.stats.multitest import multipletests
        out[ok] = multipletests(p[ok], method="fdr_bh")[1]
    return out


def ols_hc3(df, feature, regressor, categorical=True):
    """R2 and the HC3 robust F-test p of an OLS fit of feature on regressor (statsmodels).

    As the code's hivscc_analysis.ols_model: missing values dropped per feature, a fit with
    cov_type HC3 and the type-2 ANOVA table of that fit.
    """
    import statsmodels.api as sm
    import statsmodels.formula.api as smf
    d = df[[feature, regressor]].dropna()
    if categorical:
        d = d.assign(**{regressor: d[regressor].astype(str)})
        if d[regressor].nunique() < 2:
            return dict(n=len(d), r2=np.nan, p=np.nan, slope=np.nan)
        formula = f"{feature} ~ C({regressor})"
    else:
        formula = f"{feature} ~ {regressor}"
    with warnings.catch_warnings():  # rank warnings of small resamples; the p-value is still returned
        warnings.simplefilter("ignore")
        fit = smf.ols(formula, data=d).fit(cov_type="HC3")
        tab = sm.stats.anova_lm(fit, typ=2)
    p = float(tab["PR(>F)"].iloc[0])
    slope = np.nan if categorical else float(fit.params[regressor])
    return dict(n=len(d), r2=float(fit.rsquared), p=p, slope=slope)


def pairwise_mw(df, feature, group, groups):
    """Two-sided Mann-Whitney tests between pairs of groups, BH over the pairs of one feature."""
    from itertools import combinations
    from scipy.stats import mannwhitneyu
    rows = []
    for a, b in combinations(groups, 2):
        x = df.loc[df[group] == a, feature].dropna()
        y = df.loc[df[group] == b, feature].dropna()
        p = mannwhitneyu(x, y, alternative="two-sided").pvalue if len(x) and len(y) else np.nan
        rows.append(dict(feature=feature, a=a, b=b, n_a=len(x), n_b=len(y), median_a=x.median(),
                         median_b=y.median(), p=p))
    out = pd.DataFrame(rows)
    out["p_bh"] = bh(out["p"])
    return out


# --- NeuN sections of Figure 1a-c, from the code repository ------------------------------------------
#
# A port of Code6_cortical_depth_code_human.r and Code7_cortical_depth_code_mouse.r (same commit), which
# read ImageJ ROI sets with RImageJROI: one zip per section with the layer boundary lines, and one zip
# of soma outlines. Every constant below is the scripts' own: the pixel sizes (100 um = 95 pixels in
# human, 330 in mouse), the margin of 5% around the lines, the 20 bins of scaled depth, the 25 um
# section thickness implied by the factor 40 that turns cells per mm2 into thousands per mm3, and the
# use of only the first four lines in mouse.
#
# Two details of Code7 as committed do not give the values its comments print, and the port follows
# the printed values (the notebook shows both). (1) Code7 names the four mouse lines L2, L4, L5 and L6
# and takes L2/3 between the first two; its printed L2/3 thicknesses (281, 223 and 257 um) and L2
# fractions come from reading the lines as Code6 reads the human ones, L1 to L4 with L2/3 from the
# second to the fourth line. (2) Code7 sets 100 um = 330 pixels for all three mouse sections, but its
# printed values for case_set_1 need 100 um = 165 pixels, the scale its own comment gives ("100um ~
# 165 pixels"). With both, the port gives every value Code7 prints.
#
# Bins: as the scripts, the density uses R's hist (right-closed bins, the lowest included) and the
# mean and SD of soma area use left-closed bins ((rng >= lower) & (rng < upper)), so a soma clipped to
# scaled depth exactly 0 counts in the density and in no area bin.

HUMAN_CASES = ["case_072", "case_246", "case_316", "case_360", "case_732"]  # file names in the repository
MOUSE_CASES = ["case_set_1", "case_set_2", "case_set_3"]
HUMAN_UM_PER_PX = 100 / 95
MOUSE_UM_PER_PX = 100 / 330
# The scale Code7's printed values need (see above); MOUSE_UM_PER_PX is the one its code sets for all.
MOUSE_UM_PER_PX_PRINTED = {"case_set_1": 100 / 165, "case_set_2": 100 / 330, "case_set_3": 100 / 330}
DENSITY_BREAKS = -np.arange(20, -1, -1) / 20


def _roi_zip(data):
    import zipfile
    import roifile
    z = zipfile.ZipFile(io.BytesIO(data))
    return [roifile.ImagejRoi.frombytes(z.read(n)) for n in z.namelist() if n.endswith(".roi")]


def read_sections(species):
    """{case: (lines, soma outlines)} for one species, read in memory from the repository's zips."""
    import zipfile
    out = {}
    if species == "human":
        for case in HUMAN_CASES:
            z = zipfile.ZipFile(io.BytesIO(read_bytes(CODE_RAW + f"cell_sizes/human_cell_sizes/{case}.zip")))
            names = z.namelist()
            lines = _roi_zip(z.read(f"{case}/lines.zip"))
            somata = []
            for n in sorted(names):
                base = n.split("/")[-1]
                if base.startswith("L") and base.endswith(".zip") and base != "lines.zip":
                    somata += _roi_zip(z.read(n))
            out[case] = (lines, somata)
    else:
        z = zipfile.ZipFile(io.BytesIO(read_bytes(CODE_RAW + "cell_sizes/mouse_cell_sizes.zip")))
        for case in MOUSE_CASES:
            lines = _roi_zip(z.read(f"mouse_cell_sizes/{case}/lines.zip"))
            somata = []
            for n in sorted(z.namelist()):
                if n.startswith(f"mouse_cell_sizes/{case}/"):
                    base = n.split("/")[-1]
                    if base.startswith("L") and base.endswith(".zip") and base != "lines.zip":
                        somata += _roi_zip(z.read(n))
            out[case] = (lines, somata)
    return out


def _layer_matrix(lines, n_lines=None):
    """Boundary depth (pixels) at every x, as the scripts' layerMat (columns are lines 1 to 4)."""
    lines = lines[:n_lines] if n_lines else lines
    xv = np.array([[l.x1, l.x2] for l in lines], float)
    yv = np.array([[l.y1, l.y2] for l in lines], float)
    lo, hi = xv.min(), xv.max()
    lo, hi = np.round(lo - 0.05 * hi), np.round(hi + 0.05 * hi)
    x = np.arange(lo, hi + 1)
    m = (yv[:, 1] - yv[:, 0]) / (xv[:, 1] - xv[:, 0])
    b, y1 = xv[:, 0], yv[:, 0]
    cols = np.stack([np.round((x - b[j]) * m[j] + y1[j]) for j in range(4)], 1)
    if len(b) > 4:
        for k in range(2, int(np.round(len(b) / 4)) + 1):
            idx = np.arange(4) + 4 * (k - 1)
            keep = x > b[idx].mean()
            cols[keep] = np.stack([np.round((x[keep] - b[j]) * m[j] + y1[j]) for j in idx], 1)
    lay = pd.DataFrame(cols, columns=["l1", "l2", "l3", "l4"])
    lay.insert(0, "x", x)
    return lay


def section_tables(species, mouse_reading="printed"):
    """Per case: the L2/3 thickness (um), and a table of somata (x, depth, area in um2, scaled depth).

    For mouse, `mouse_reading` is "printed" (lines read L1 to L4 and case_set_1 at 165 pixels per
    100 um, which give Code7's printed values) or "as_committed" (lines read L2, L4, L5, L6 and 330
    pixels per 100 um for every section, as Code7's code reads)."""
    sections = read_sections(species)
    out = {}
    for case, (lines, somata) in sections.items():
        if species == "human":
            um, top, bottom = HUMAN_UM_PER_PX, "l2", "l4"
        elif mouse_reading == "printed":
            um, top, bottom = MOUSE_UM_PER_PX_PRINTED[case], "l2", "l4"
        else:
            um, top, bottom = MOUSE_UM_PER_PX, "l1", "l2"
        lay = _layer_matrix(lines, None if species == "human" else 4)
        lay["l23"] = lay[bottom] - lay[top]
        rows = []
        for r in somata:
            c = np.asarray(r.coordinates(), float)
            x = np.round(c[:, 0].mean())
            d = c[:, 1].mean()
            area = sum(np.ptp(c[c[:, 0] == xx, 1]) for xx in np.unique(c[:, 0])) * um * um
            row = lay.loc[lay.x == x]
            scaled = float((row[top].iloc[0] - d) / row.l23.iloc[0]) if len(row) else np.nan
            rows.append(dict(x=x, depth=d, area=area, scaled_depth=scaled))
        cells = pd.DataFrame(rows)
        cells["scaled_unclipped"] = cells.scaled_depth
        cells["scaled_depth"] = cells.scaled_depth.clip(-1, 0)
        l2_frac = float(-(lay.l3 - lay.l2).mean() / lay.l23.mean()) if top == "l2" else np.nan
        out[case] = dict(l23_um=float(lay.l23.mean() * um), cells=cells, lines=len(lines), um_per_px=um,
                         l2_fraction=l2_frac)
    return out


CODE_SCRIPTS = f"https://raw.githubusercontent.com/AllenInstitute/patchseq_human_L23/{CODE_COMMIT}/scripts/"


def code_printed_values():
    """The values Code6 and Code7 print, read from the output the scripts carry as comments.

    Keys: thickness_human, thickness_mouse (um per section), l2_fraction_human, l2_fraction_mouse,
    density_human, density_mouse (mean, SD), quantiles_human, quantiles_mouse (at QUANTILE_P),
    largest_human, largest_mouse (six largest areas), and the four ratios Code7 prints
    (area_l2, area_deep_l3, sd_l2, sd_deep_l3, to two significant figures)."""
    import re
    c6 = read_bytes(CODE_SCRIPTS + "Code6_cortical_depth_code_human.r").decode()
    c7 = read_bytes(CODE_SCRIPTS + "Code7_cortical_depth_code_mouse.r").decode()

    def nums(line):
        return [float(v) for v in re.findall(r"-?\d+\.?\d*", line.split("]", 1)[-1])]

    out = {"thickness_human": [float(v) for v in re.findall(r'#\[1\] "Average L23 depth for case_\d+ = (\d+)"', c6)],
           "thickness_mouse": [float(v) for v in re.findall(r'#\[1\] "Average L23 depth for case_set_\d = (\d+)"', c7)]}
    lines = c7.splitlines()
    for i, ln in enumerate(lines):
        if ln.startswith("print(l2)"):
            out["l2_fraction_mouse"] = nums(lines[i + 1])
        elif ln.startswith("print(l2H)"):
            out["l2_fraction_human"] = nums(lines[i + 1])
        elif ln.startswith("print(quantile(a,p))"):
            key = "quantiles_mouse" if "quantiles_mouse" not in out else "quantiles_human"
            out[key] = [float(v) for v in lines[i + 2].lstrip("#").split()]
        elif ln.startswith("head(-sort(-a))"):
            key = "largest_mouse" if "largest_mouse" not in out else "largest_human"
            out[key] = nums(lines[i + 1])
    for sp in ("Mouse", "Human"):
        m = re.search(rf'#\[1\] "{sp} density \(mm\^3\) = ([\d.]+) \+/- ([\d.]+)"', c7)
        out[f"density_{sp.lower()}"] = [float(m.group(1)), float(m.group(2))]
    for key, pat in [("area_l2", r"Average human / mouse cross-sectional area \(L2\): ([\d.]+)"),
                     ("area_deep_l3", r"Average human / mouse cross-sectional area \(deep L3\): ([\d.]+)"),
                     ("sd_l2", r"SD human / mouse cross-sectional area \(L2\): ([\d.]+)"),
                     ("sd_deep_l3", r"SD human / mouse cross-sectional area \(deep L3\): ([\d.]+)")]:
        out[key] = float(re.search(r'#\s*\[1\] "' + pat, c7).group(1))
    return out


QUANTILE_P = [0, 0.05, 0.25, 0.5, 0.75, 0.9, 0.99, 1]  # Code7's p


def code6_recycled(dens, cases, start=0):
    """The human bin table as Code6 builds it. Code6 never sets q9 to NULL (Code7 does, per section),
    so q9 grows across sections: with `start` sections' worth of values (20 each) already in q9 when
    Code6 runs, section k (in file order, from 1) has 20 (k + start) values of q9, and cbind recycles
    its 20 bins k + start times. Means over the table's rows then count section k k + start times.
    Code6 run alone stops at q9, so some q9 must be present; how much is not known. Shown as a variant,
    to explain Code7's printed ratios."""
    return pd.concat([dens[dens.case == c] for k, c in enumerate(cases) for _ in range(k + 1 + start)])


def density_profile(case_tables, area_bins="left"):
    """Per case and bin: density (R's hist density), mean and SD of soma area; and cells per mm3.

    `area_bins` "left" bins the areas as the scripts do (left-closed); "right" uses the density's
    right-closed bins, a variant."""
    br = DENSITY_BREAKS
    rows, per_mm3 = [], {}
    for case, t in case_tables.items():
        c = t["cells"]
        um = t["um_per_px"]
        s = c.scaled_depth.values
        # R's hist: right-closed bins, the lowest included
        idx = np.clip(np.searchsorted(br, s, side="left") - 1, 0, len(br) - 2)
        counts = np.bincount(idx, minlength=len(br) - 1)
        dens = counts / (len(s) * np.diff(br))
        for k in range(len(br) - 1):
            a = c.area[(s >= br[k]) & (s < br[k + 1])] if area_bins == "left" else c.area[idx == k]
            rows.append(dict(case=case, bin=k, centre=(br[k] + br[k + 1]) / 2, dens=dens[k],
                             area=a.mean(), het=a.std(ddof=1), n=len(a)))
        area_px = np.ptp(c.x) * np.ptp(c.depth[c.x <= 200])
        per_mm2 = 1e6 * len(c) / (area_px * um * um)
        per_mm3[case] = 40 * per_mm2 / 1000
    return pd.DataFrame(rows), pd.Series(per_mm3)
