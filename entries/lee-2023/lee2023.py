"""Loading and measures for Lee, Dalley et al. (2023), Science 382, eadf6484, on dandiset 000636.

The dandiset holds one NWB file per neuron (Allen Institute MIES recordings, current clamp
at 50 kHz). Cell labels come from the paper's code repository, AllenInstitute/human_patchseq_gaba
at commit 5eb357a, matched by its `nwb_id` column, which equals the NWB session id.

Where parameters come from:
- Sweep inclusion: Methods, "Electrophysiology" (patch-clamp recording paragraph): "the bridge
  balance was <20 MΩ and <15% of the Rinput; (ii) bias (leak) current 0 ± 100 pA; and (iii) root
  mean square noise measurements in a short window (1.5 ms ...) and longer window (500 ms ...) were
  <0.07 and 0.5 mV". The noise windows are IPFX's own (qc_feature_extractor), which the paper
  uses ("Feature extraction was implemented using the IPFX python package").
- Features: Methods, "Electrophysiology feature analysis", computed with the IPFX package
  (version in the lock file) through its LongSquareAnalysis, ShortSquareAnalysis and
  RampAnalysis, with IPFX's defaults (sag at the sweep whose response is closest to -100 mV,
  hero sweep at rheobase + 39 to 61 pA, input resistance from sweeps between -100 and 0 pA).
  Column names follow the paper's table LeeDalley_ephys_fx.csv. Features that public IPFX does
  not compute are left out (Methods: "custom code used for chirps and some high-level features
  will be released in a future version of IPFX"); NOT_COMPUTED lists them.
- Adaptation ratios: Methods, "a ratio of the spike features between the first and third spike
  (on the lowest amplitude stimulus to elicit at least four spikes)". Read as third over first
  spike; for the ISI, the second ISI over the first (the ISIs that end at the third and the
  second spike). These are assumptions, checked against the paper's table in the link claim.
- adapt_mean/max, isi_cv_mean/max, isi_norm_sq_var_mean/max: mean and maximum over the
  spiking long square sweeps with at least four spikes, an assumption (the paper does not
  define them); isi_norm_sq_var is IPFX's norm_sq_diff of the ISIs, an assumption.
- Statistics helpers follow the claims file: Mann-Whitney (two-sided), Kruskal-Wallis with
  Dunn's post hoc, Benjamini-Hochberg FDR.
"""
import io
import json
import logging
import warnings
from concurrent.futures import ProcessPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
import requests

DANDISET = "000636"
VERSION = "0.241120.0510"
API = "https://api.dandiarchive.org/api"
CODE_REPO = "AllenInstitute/human_patchseq_gaba"
CODE_COMMIT = "5eb357a1cea246c7c847b5608a8fc7e87ea95b58"
# Mouse comparison data (claims fig6c, fig6e, figs8b, figs9; claims file header: "Mouse comparison
# data are the VISp Patch-seq GABAergic cells of Gouwens et al. 2020 (ref. 16)"). The recordings
# are dandiset 000020; the per-cell t-types are the Allen Institute's specimen table
# 20200711_patchseq_metadata_mouse.csv, read from a public copy pinned at a commit, as the Allen
# portal's own URL has no version. Its ephys_session_id is matched to the NWB session id.
MOUSE_DANDISET = "000020"
MOUSE_VERSION = "0.210913.1639"
MOUSE_LABELS = ("https://raw.githubusercontent.com/ewesteinde/patchseq_models/"
                "547d11ea2339d51402484a84538c32d64ff162e9/20200711_patchseq_metadata_mouse.csv")
MOUSE_LABELS_SHA256 = "2eb2a02ee1dd275b457055d6d4d57f2942d8c6d3cf329e820002010c7943c142"

# The 9 chirp columns of LeeDalley_ephys_fx.csv; the other 84 are the paper's 84 features
# (claims file, header, reading a).
CHIRP = ["peak_ratio_chirp", "peak_freq_chirp", "3db_freq_chirp", "peak_impedance_chirp",
         "low_freq_impedance_chirp", "sync_freq_chirp", "phase_peak_chirp", "phase_low_chirp",
         "total_inductive_phase_chirp"]
# Of the 84, those public IPFX does not compute (custom code, Methods).
NOT_COMPUTED = ["width_suprathresh_ramp", "postap_slope_ramp", "width_suprathresh_short_square",
                "postap_slope_short_square", "sag_peak_t", "sag_area", "width_suprathresh_rheo",
                "postap_slope_rheo", "adp_v_last_rheo", "width_suprathresh_hero", "postap_slope_hero",
                "ahp_delay_ratio_hero", "sag_depol", "sag_peak_t_depol", "sag_area_depol",
                "ahp_delay_ratio_5spike", "trough_slowdeltav_rheo", "trough_slowdeltav_hero", "sag_tau"]

SPIKE_FEATURES = ["upstroke_downstroke_ratio", "threshold_v", "width", "upstroke", "downstroke"]


# --- archive -------------------------------------------------------------------------------

def assets(dandiset=DANDISET, version=VERSION):
    """All assets of a pinned version (default the human dandiset), with path, size, asset_id and
    the session id."""
    out, url = [], f"{API}/dandisets/{dandiset}/versions/{version}/assets/?page_size=1000"
    while url:
        r = requests.get(url, timeout=60)
        r.raise_for_status()
        d = r.json()
        out += d["results"]
        url = d["next"]
    df = pd.DataFrame(out)[["asset_id", "path", "size"]]
    df["subject"] = df.path.str.extract(r"sub-([^/_]+)")[0]
    df["session"] = df.path.str.extract(r"ses-([^_]+)_")[0]
    return df


def version_metadata():
    r = requests.get(f"{API}/dandisets/{DANDISET}/versions/{VERSION}/", timeout=60)
    r.raise_for_status()
    return r.json()


def s3_url(asset_id):
    r = requests.get(f"{API}/assets/{asset_id}/download/", allow_redirects=False, timeout=60)
    return r.headers["location"]


def code_table(name):
    """A table from the paper's code repository at the pinned commit (data/<name>)."""
    url = f"https://raw.githubusercontent.com/{CODE_REPO}/{CODE_COMMIT}/data/{name}"
    r = requests.get(url, timeout=120)
    r.raise_for_status()
    return pd.read_csv(io.StringIO(r.text))


def mouse_labels():
    """The mouse specimen table (t-type per cell), checked against its pinned sha256."""
    import hashlib
    r = requests.get(MOUSE_LABELS, timeout=120)
    r.raise_for_status()
    assert hashlib.sha256(r.content).hexdigest() == MOUSE_LABELS_SHA256, "mouse label table changed"
    m = pd.read_csv(io.BytesIO(r.content))
    m["ttype"] = m["T-type Label"].astype(str).str.strip()
    m["session"] = m.ephys_session_id.astype("Int64").astype(str)
    return m


def metadata_table():
    m = code_table("LeeDalley_manuscript_metadata_v2.csv")
    m.columns = [c.strip() for c in m.columns]
    m["nwb_session"] = m.nwb_id.map(lambda x: str(int(x)) if pd.notna(x) else None)
    return m


# --- reading a cell ------------------------------------------------------------------------

def _ontology():
    from ipfx.stimulus import StimulusOntology
    import ipfx.json_utilities as ju
    return StimulusOntology(ju.read(StimulusOntology.DEFAULT_STIMULUS_ONTOLOGY_FILE))


def stim_kind(code, ontology):
    """'long_square', 'short_square', 'ramp' or None, from IPFX's stimulus ontology."""
    code = code.rsplit("_DA_", 1)[0]
    try:
        flat = set(ontology.find_one(code, tag_type="code").tags(tag_type="name", flat=True))
    except (KeyError, ValueError):
        return None
    if "Long Square" in flat:
        return "long_square"
    if "Short Square" in flat:
        return "short_square"
    if "Ramp" in flat:
        return "ramp"
    return None


def read_cell(asset_id):
    """Stream one NWB file and return its file-level metadata and its long square, short square
    and ramp current-clamp sweeps, with the per-sweep bias current and bridge balance."""
    from ipfx.sweep import Sweep
    ont = _ontology()
    f = h5py.File(remfile.File(s3_url(asset_id)), "r")
    def txt(path):
        if path not in f:
            return None
        x = f[path][()]
        x = x.flat[0] if isinstance(x, np.ndarray) else x
        return x.decode() if isinstance(x, bytes) else str(x)
    meta = {k: txt(p) for k, p in [("session_id", "general/session_id"),
                                   ("subject_id", "general/subject/subject_id"),
                                   ("species", "general/subject/species"),
                                   ("genotype", "general/subject/genotype"),
                                   ("sex", "general/subject/sex"),
                                   ("institution", "general/institution"),
                                   ("session_start_time", "session_start_time")]}
    meta["general_fields"] = ",".join(sorted(f["general"].keys()))
    ie = f["general/intracellular_ephys"] if "general/intracellular_ephys" in f else {}
    meta["electrode_location"] = ";".join(txt(f"general/intracellular_ephys/{k}/location") or "none"
                                          for k in ie if isinstance(ie[k], h5py.Group))
    sweeps, stim_codes = [], []
    for name, d in f["acquisition"].items():
        if d.attrs["neurodata_type"] != "CurrentClampSeries":
            continue
        code = d.attrs.get("stimulus_description")
        code = code.flat[0] if isinstance(code, np.ndarray) else code
        code = code.decode() if isinstance(code, bytes) else str(code)
        stim_codes.append(code)
        kind = stim_kind(code, ont)
        if kind is None:
            continue
        sname = name.replace("_AD", "_DA")
        s = f["stimulus/presentation"][sname]
        rate = float(d["starting_time"].attrs["rate"])
        vconv = float(d["data"].attrs["conversion"]) * 1e3   # to mV
        iconv = float(s["data"].attrs["conversion"]) * 1e12  # to pA
        v = d["data"][:].astype(float) * vconv
        i = s["data"][:].astype(float) * iconv
        n = min(len(v), len(i))
        v, i = v[:n], i[:n]
        bias = float(d["bias_current"][0]) if "bias_current" in d else np.nan
        bridge = float(d["bridge_balance"][0]) if "bridge_balance" in d else np.nan
        t = np.arange(n) / rate
        sw = Sweep(t, v, i, "CurrentClamp", rate, sweep_number=int(d.attrs["sweep_number"]))
        sweeps.append(dict(kind=kind, code=code, sweep=sw, rate=rate, bias_pa=bias,
                           bridge_mohm=bridge, v_unit=d["data"].attrs.get("unit"),
                           i_unit=s["data"].attrs.get("unit")))
    f.close()
    meta["stim_codes"] = stim_codes
    return meta, sweeps


def sweep_qc(sw):
    """Noise and leak criteria of the Methods for one sweep, on IPFX's QC measures."""
    import ipfx.qc_feature_extractor as qcfe
    out = {"bias_pa": sw["bias_pa"], "bridge_mohm": sw["bridge_mohm"]}
    try:
        q = qcfe.current_clamp_sweep_qc_features(sw["sweep"], sw["kind"] == "ramp")
        out["pre_noise_rms_mv"] = q["pre_noise_rms_mv"]
        out["slow_noise_rms_mv"] = q["slow_noise_rms_mv"]
    except Exception:
        out["pre_noise_rms_mv"] = out["slow_noise_rms_mv"] = np.nan
    out["pass_noise"] = bool(out["pre_noise_rms_mv"] < 0.07 and out["slow_noise_rms_mv"] < 0.5)
    out["pass_leak"] = bool(abs(out["bias_pa"]) <= 100) if np.isfinite(out["bias_pa"]) else True
    out["pass_bridge20"] = bool(out["bridge_mohm"] < 20) if np.isfinite(out["bridge_mohm"]) else True
    return out


# --- features ------------------------------------------------------------------------------

def _spike_row(spikes, idx=0):
    if spikes is None or len(spikes) <= idx:
        return None
    return spikes.iloc[idx]


def _shape(prefix, sp, out):
    """First-spike shape features of one sweep, named as in LeeDalley_ephys_fx.csv."""
    if sp is None:
        return
    for k in SPIKE_FEATURES:
        out[f"{k}_{prefix}"] = sp.get(k, np.nan)
    thr = sp.get("threshold_v", np.nan)
    out[f"peak_deltav_{prefix}"] = sp.get("peak_v", np.nan) - thr
    out[f"fast_trough_deltav_{prefix}"] = sp.get("fast_trough_v", np.nan) - thr
    if prefix != "short_square":
        out[f"trough_deltav_{prefix}"] = sp.get("trough_v", np.nan) - thr


def _train(prefix, sf, spikes, out):
    out[f"latency_{prefix}"] = sf.get("latency", np.nan)
    out[f"avg_rate_{prefix}"] = sf.get("avg_rate", np.nan)
    out[f"mean_isi_{prefix}"] = sf.get("mean_isi", np.nan)
    fi = sf.get("first_isi", np.nan)
    out[f"first_isi_inv_{prefix}"] = 1.0 / fi if fi and np.isfinite(fi) and fi > 0 else np.nan
    if prefix == "hero":
        out["adapt_hero"] = sf.get("adapt", np.nan)
        out["median_isi_hero"] = sf.get("median_isi", np.nan)
        out["isi_cv_hero"] = sf.get("isi_cv", np.nan)
        out["isi_norm_sq_var_hero"] = _norm_sq(spikes)
    if prefix == "rheo" and spikes is not None and len(spikes):
        out["fast_trough_v_last_rheo"] = spikes.iloc[-1].get("fast_trough_v", np.nan)


def _norm_sq(spikes):
    from ipfx.spike_train_features import norm_sq_diff
    if spikes is None or len(spikes) < 3:
        return np.nan
    isis = np.diff(spikes["peak_t"].values)
    return float(norm_sq_diff(isis))


def _nan_on_error(fn):
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except (ValueError, RuntimeError, TypeError, IndexError) as e:
            return np.nan
        except Exception as e:  # IPFX's FeatureError
            if type(e).__name__ == "FeatureError":
                return np.nan
            raise
    wrapper.patched = True
    return wrapper


def _patch_ipfx():
    """A failed tau fit on one sweep, or an f-I slope with one spiking sweep, makes IPFX drop
    every long square feature of the cell; here they give NaN for that feature only."""
    import ipfx.subthresh_features as subf
    import ipfx.spike_train_features as strf
    import ipfx.stimulus_protocol_analysis as spa
    if not getattr(subf.time_constant, "patched", False):
        subf.time_constant = _nan_on_error(subf.time_constant)
        strf.fit_fi_slope = _nan_on_error(strf.fit_fi_slope)
        spa.subf = subf
        spa.strf = strf


def long_square_features(sweeps):
    _patch_ipfx()
    import ipfx.data_set_features as dsf
    import ipfx.stim_features as stf
    import ipfx.stimulus_protocol_analysis as spa
    from ipfx.sweep import SweepSet
    from ipfx.stimulus import StimulusType
    ss = SweepSet([s["sweep"] for s in sweeps])
    ss.align_to_start_of_epoch("experiment")
    start, dur, _, _, _ = stf.get_stim_characteristics(ss.sweeps[0].i, ss.sweeps[0].t)
    spx, sptx = dsf.extractors_for_sweeps(ss, start=start, end=start + dur,
                                          **dsf.detection_parameters(StimulusType.LONG_SQUARE))
    an = spa.LongSquareAnalysis(spx, sptx, subthresh_min_amp=-100.0)
    feat = an.analyze(ss)
    out = {k: feat.get(k, np.nan) for k in ["v_baseline", "rheobase_i", "fi_fit_slope", "sag",
                                            "vm_for_sag", "input_resistance", "tau"]}
    spikes_set = feat["spikes_set"]
    sw_feat = an._sweep_features
    for prefix, key in [("rheo", "rheobase_sweep"), ("hero", "hero_sweep")]:
        row = feat.get(key)
        if row is None:
            continue
        idx = row.name
        spikes = spikes_set[idx]
        _shape(prefix, _spike_row(spikes), out)
        _train(prefix, row, spikes, out)
        out[f"{prefix}_amp"] = row.get("stim_amp", np.nan)
    # adaptation ratios, lowest amplitude sweep with at least four spikes
    amps = sw_feat["stim_amp"].values
    n_spk = np.array([len(s) for s in spikes_set])
    cand = np.where(n_spk >= 4)[0]
    if len(cand):
        j = cand[np.argmin(amps[cand])]
        sp = spikes_set[j]
        for k, col in [("width", "width_adapt_ratio"), ("upstroke", "upstroke_adapt_ratio"),
                       ("downstroke", "downstroke_adapt_ratio"), ("peak_v", "peak_v_adapt_ratio"),
                       ("threshold_v", "threshold_v_adapt_ratio"), ("fast_trough_v", "fast_trough_v_adapt_ratio")]:
            out[col] = sp[k].iloc[2] / sp[k].iloc[0]
        isis = np.diff(sp["peak_t"].values)
        out["isi_adapt_ratio"] = isis[1] / isis[0]
    # summaries over spiking sweeps with at least four spikes
    multi = [j for j in range(len(spikes_set)) if n_spk[j] >= 4]
    if multi:
        ad = [sw_feat["adapt"].iloc[j] for j in multi]
        cv = [sw_feat["isi_cv"].iloc[j] for j in multi]
        nsq = [_norm_sq(spikes_set[j]) for j in multi]
        out.update(adapt_mean=np.nanmean(ad), adapt_max=np.nanmax(ad), isi_cv_mean=np.nanmean(cv),
                   isi_cv_max=np.nanmax(cv), isi_norm_sq_var_mean=np.nanmean(nsq),
                   isi_norm_sq_var_max=np.nanmax(nsq))
    return out


def short_square_features(sweeps):
    import ipfx.data_set_features as dsf
    import ipfx.stim_features as stf
    import ipfx.stimulus_protocol_analysis as spa
    from ipfx.sweep import SweepSet
    from ipfx.stimulus import StimulusType
    ss = SweepSet([s["sweep"] for s in sweeps])
    ss.align_to_start_of_epoch("experiment")
    start, dur, _, _, _ = stf.get_stim_characteristics(ss.sweeps[0].i, ss.sweeps[0].t)
    spx, sptx = dsf.extractors_for_sweeps(ss, est_window=[start, start + 0.001],
                                          **dsf.detection_parameters(StimulusType.SHORT_SQUARE))
    an = spa.ShortSquareAnalysis(spx, sptx)
    feat = an.analyze(ss)
    out = {}
    cs = feat.get("common_amp_sweeps")
    if cs is None or len(cs) == 0:
        return out
    spikes = [feat["spikes_set"][j] for j in cs.index]
    first = pd.DataFrame([s.iloc[0] for s in spikes if len(s)])
    if len(first):
        _shape("short_square", first.mean(numeric_only=True), out)
    return out


def ramp_features(sweeps):
    import ipfx.data_set_features as dsf
    import ipfx.stim_features as stf
    import ipfx.stimulus_protocol_analysis as spa
    from ipfx.sweep import SweepSet
    from ipfx.stimulus import StimulusType
    ss = SweepSet([s["sweep"] for s in sweeps])
    ss.align_to_start_of_epoch("experiment")
    start, dur, _, _, _ = stf.get_stim_characteristics(ss.sweeps[0].i, ss.sweeps[0].t)
    spx, sptx = dsf.extractors_for_sweeps(ss, start=start,
                                          **dsf.detection_parameters(StimulusType.RAMP))
    an = spa.RampAnalysis(spx, sptx)
    feat = an.analyze(ss)
    out = {}
    spikes = [s for s in feat["spikes_set"] if len(s)]
    if spikes:
        first = pd.DataFrame([s.iloc[0] for s in spikes])
        m = first.mean(numeric_only=True)
        _shape("ramp", m, out)
        out["threshold_i_ramp"] = m.get("threshold_i", np.nan)
    return out


def cell_features(asset_id):
    """Everything this entry measures on one NWB file: metadata, sweep counts and QC, features."""
    warnings.filterwarnings("ignore")
    logging.disable(logging.WARNING)
    rec = {"asset_id": asset_id}
    try:
        meta, sweeps = read_cell(asset_id)
    except Exception as e:  # unreadable file: reported, never filled in
        rec["error"] = f"read: {type(e).__name__}: {e}"
        return rec
    rec.update({k: v for k, v in meta.items() if k != "stim_codes"})
    rec["n_cc_sweeps"] = len(meta["stim_codes"])
    rec["rates"] = sorted({s["rate"] for s in sweeps})
    rec["units"] = sorted({f"{s['v_unit']}|{s['i_unit']}" for s in sweeps})
    qcs = [sweep_qc(s) for s in sweeps]
    keep = [s for s, q in zip(sweeps, qcs) if q["pass_noise"] and q["pass_leak"] and q["pass_bridge20"]]
    for kind in ["long_square", "short_square", "ramp"]:
        rec[f"n_{kind}"] = sum(s["kind"] == kind for s in sweeps)
        rec[f"n_{kind}_qc"] = sum(s["kind"] == kind for s in keep)
    rec["bridge_max"] = float(np.nanmax([s["bridge_mohm"] for s in keep])) if keep else np.nan
    for kind, fn in [("long_square", long_square_features), ("short_square", short_square_features),
                     ("ramp", ramp_features)]:
        sel = [s for s in keep if s["kind"] == kind]
        if not sel:
            continue
        try:
            rec.update(fn(sel))
        except Exception as e:
            rec[f"error_{kind}"] = f"{type(e).__name__}: {e}"
    # bridge balance < 15% of Rin (Methods): drop sweeps above and recompute long squares
    rin = rec.get("input_resistance", np.nan)
    if np.isfinite(rin):
        bad = [s for s in keep if np.isfinite(s["bridge_mohm"]) and s["bridge_mohm"] >= 0.15 * rin]
        rec["n_bridge15_dropped"] = len(bad)
        if bad:
            keep2 = [s for s in keep if s not in bad]
            for kind, fn in [("long_square", long_square_features), ("short_square", short_square_features),
                             ("ramp", ramp_features)]:
                sel = [s for s in keep2 if s["kind"] == kind]
                if sel:
                    try:
                        rec.update(fn(sel))
                    except Exception as e:
                        rec[f"error_{kind}"] = f"{type(e).__name__}: {e}"
    return rec


def all_cell_features(asset_ids, workers=4):
    """cell_features over many files, in parallel processes, one file per process at a time."""
    with ProcessPoolExecutor(workers) as ex:
        return pd.DataFrame(list(ex.map(cell_features, asset_ids, chunksize=1)))


# --- statistics ----------------------------------------------------------------------------

def bh(p):
    from statsmodels.stats.multitest import multipletests
    p = np.asarray(p, float)
    out = np.full_like(p, np.nan)
    ok = np.isfinite(p)
    if ok.any():
        out[ok] = multipletests(p[ok], method="fdr_bh")[1]
    return out


def mannwhitney_table(df, features, group_col, a, b):
    """Two-sided Mann-Whitney per feature, a against b, with BH FDR across features."""
    from scipy.stats import mannwhitneyu
    rows = []
    for f in features:
        x = df.loc[df[group_col] == a, f].dropna()
        y = df.loc[df[group_col] == b, f].dropna()
        if len(x) < 2 or len(y) < 2:
            rows.append(dict(feature=f, n_a=len(x), n_b=len(y), p=np.nan))
            continue
        u, p = mannwhitneyu(x, y, alternative="two-sided")
        rows.append(dict(feature=f, n_a=len(x), n_b=len(y), median_a=x.median(), median_b=y.median(),
                         U=u, p=p, rbc=1 - 2 * u / (len(x) * len(y))))
    t = pd.DataFrame(rows)
    t["p_fdr"] = bh(t.p)
    return t


def kruskal_dunn(df, feature, group_col, groups):
    """Kruskal-Wallis across groups and Dunn's post hoc with BH FDR over the pairs."""
    from scipy.stats import kruskal
    import scikit_posthocs as sp
    d = df[df[group_col].isin(groups)][[feature, group_col]].dropna()
    samples = [d.loc[d[group_col] == g, feature].values for g in groups]
    if min(len(s) for s in samples) < 1:
        return np.nan, None, d.groupby(group_col)[feature].median()
    h, p = kruskal(*samples)
    dunn = sp.posthoc_dunn(d, val_col=feature, group_col=group_col, p_adjust="fdr_bh")
    return p, dunn.loc[groups, groups], d.groupby(group_col)[feature].agg(["median", "count"])


def neighbour_fraction(X, labels, k, same=True, among=None, query=None):
    """For each query row, the fraction of its k nearest neighbours (Euclidean, among the rows
    flagged by `among`) whose label equals its own (same=True) or the given label."""
    from sklearn.neighbors import NearestNeighbors
    X = np.asarray(X)
    labels = np.asarray(labels)
    among = np.ones(len(X), bool) if among is None else np.asarray(among)
    query = np.ones(len(X), bool) if query is None else np.asarray(query)
    ref = np.where(among)[0]
    nn = NearestNeighbors(n_neighbors=k + 1).fit(X[ref])
    _, ind = nn.kneighbors(X[query])
    qidx = np.where(query)[0]
    out = []
    for qi, row in zip(qidx, ind):
        nb = [ref[j] for j in row if ref[j] != qi][:k]
        out.append(labels[nb])
    return qidx, out


def zscore_impute(F, ref=None):
    """Missing values set to the feature median and z-scored; with `ref` (a boolean mask of rows)
    the median, mean and sd are taken over those rows only and applied to all."""
    F = F.astype(float)
    R = F if ref is None else F[np.asarray(ref)]
    F = F.fillna(R.median())
    R = F if ref is None else F[np.asarray(ref)]
    sd = R.std(ddof=0).replace(0, np.nan)
    return ((F - R.mean()) / sd).fillna(0.0)


def umap_embed(Z, seed):
    import umap
    return umap.UMAP(random_state=seed).fit_transform(np.asarray(Z))


# --- transcriptomes (the paper's code repository) ----------------------------------------------

def transcriptomes():
    """The Patch-seq expression matrices of the code repository (log2(CPM + 1), genes x cells,
    columns named by tube id) and the per-cell table stored with them (metaPatch)."""
    import tempfile
    import rdata
    parts, meta = [], None
    for k in (1, 2):
        url = f"https://raw.githubusercontent.com/{CODE_REPO}/{CODE_COMMIT}/data/complete_patchseq_data_sets{k}.RData"
        r = requests.get(url, timeout=300)
        r.raise_for_status()
        with tempfile.NamedTemporaryFile(suffix=".RData") as tmp:  # rdata reads from a path; removed on close
            tmp.write(r.content)
            tmp.flush()
            conv = rdata.conversion.convert(rdata.parser.parse_file(tmp.name))
        d = conv[f"datPatch{k}"]
        parts.append(pd.DataFrame(np.asarray(d.values), index=[str(g) for g in d.coords["dim_0"].values],
                                  columns=[str(c) for c in d.coords["dim_1"].values]))
        if "metaPatch" in conv:
            meta = conv["metaPatch"]
    X = pd.concat(parts, axis=1)
    meta = meta.copy()
    meta.columns = [str(c) for c in meta.columns]
    return X, meta
