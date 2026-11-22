"""Loading and resonance measures for dandiset 000630 (Chartrand et al. 2023, human L1 Patch-seq),
and for two outside inputs read the same way: dandiset 000636 (Lee, Dalley et al. 2023, human
acute and slice-culture interneurons) and dandiset 000020 (Gouwens et al. 2020, mouse visual
cortex interneurons).

Used by the notebook that tests Shamugia et al. (2026), "Ion Channels and Morphology Drive
Widespread Resonance in Human Cortical Interneurons" (doi:10.21203/rs.3.rs-11136357/v1), on
this dandiset. Files are streamed from the DANDI archive with remfile and h5py; nothing is
written to disk. Only the sweeps the measures need are read: the chirp sweeps and the
hyperpolarizing long-square sweeps.

Where each parameter comes from:

- Chirp analysis (claims file, open detail O1). Impedance is |FFT(V) / FFT(I)| (Methods,
  "Patch-clamp ZD7288 experiments": "the ratio of the fast Fourier transform (FFT) of the
  voltage response (Vm) over the FFT of the injected current"), computed as IPFX v2.0.0
  `chirp.chirp_amp_phase` does (O1, reading a): the chirp sweeps of a cell are averaged (the
  Fig. 1a legend: "From an averaged CHIRP sweep"), average-downsampled to 2 kHz, and the FFT is
  taken over the chirp itself. The chirp window is read from the stimulus of each file (0.6 to
  20.6 s in the 2018 protocol, which is IPFX's default window, and 0.52 to 20.52 s in the 2017
  protocol). Reading (a) keeps 0.2 to 40 Hz (IPFX defaults), reading (b) 0.4 to 40 Hz (the
  stimulus band, Results, first section). The profile is LOWESS smoothed with frac 0.04, the
  value the Methods give for the model chirp ("CHIRP Experiments"), as O1 says. fres is the
  frequency of the smoothed maximum, Q = Zmax / Z0 with Z0 the smoothed impedance at the
  lowest frequency kept (Results: "the impedance at the lowest frequency (Z0)"), and f3dB the
  first frequency above the peak where the smoothed profile falls below Zmax / sqrt(2) (O1).
- A cell is resonant when fres > 1 Hz and Q > 1.05 (Quantification and Statistical Analysis).
- Sweep exclusions (standard choices, not from the paper; they remove recordings that cannot
  be measured). A sweep whose voltage holds exact zeros before the end of the stimulus
  window was stopped early and is dropped. A chirp sweep whose voltage rises above -20 mV
  inside the chirp fired an action potential and is dropped, as the chirp is meant to be
  subthreshold (Methods: "a subthreshold membrane voltage response of +/- 5 mV"). Only
  chirps of 20 s are used (Methods: "0.4 Hz to 40 Hz over 20 seconds"); the 2017 protocol
  also holds 10 s and 40 s chirps.
- Sag ratio (O2), the IPFX v2.0.0 `subthresh_features.sag` formula: (v_peak - v_steady) /
  (v_peak - v_baseline), with the peak averaged over 5 ms around the minimum and the baseline
  and steady state averaged over 30 ms before the step and before its end. Reading (a) takes
  the hyperpolarizing long square whose peak is closest to -100 mV (IPFX SAG_TARGET); reading
  (b) the -100 pA step, or the nearest step to it (when two steps are equally near, the mean
  of their sag ratios, a standard choice).
- Input resistance (O3). Reading (a) is IPFX v2.0.0 `subthresh_features.input_resistance`:
  the least-squares slope of the minimum voltage during the step against the step current
  over all hyperpolarizing long squares. Reading (b) is the steady-state deflection over the
  current for the step used in sag reading (b).
- Mixed models (O5). Reading (a) is a REML linear mixed model with a donor intercept and
  Satterthwaite degrees of freedom for each test (as SPSS MIXED and lmerTest compute them), in
  `lmm_satterthwaite`; reading (b) is statsmodels MixedLM with Wald z tests (in the notebook).
  The Satterthwaite F test of a term with several degrees of freedom follows lmerTest
  (Kuznetsova et al. 2017): the contrast is split into independent one-df contrasts by an
  eigendecomposition of its covariance, each gets its own df, and these are combined.
- Baseline membrane potential Vm (O4). Reading (a) is the mean voltage from 0.4 to 0.05 s
  before the chirp starts, averaged over the chirp sweeps used; reading (b) is the mean
  voltage over the 0.1 s before the step, averaged over the hyperpolarizing long squares
  (the baseline IPFX reports).
"""

import json
import urllib.request
from concurrent.futures import ProcessPoolExecutor

import h5py
import numpy as np
import remfile
from statsmodels.nonparametric.smoothers_lowess import lowess

DANDISET = "000630"
VERSION = "0.230915.2257"
API = "https://api.dandiarchive.org/api"

# Labels from the analysis repository of Chartrand et al. (2023), which the dandiset's
# description names. Pinned at a commit.
CHARTRAND_REPO = "https://raw.githubusercontent.com/AllenInstitute/patchseq_human_L1"
CHARTRAND_COMMIT = "7777857c1b89b19735e45fd9c9bd7493cc1d805c"
CHARTRAND_TABLE = "data/human_l1_dataset_2023_02_06.csv"

DOWN_RATE = 2000.0          # Hz, IPFX chirp_amp_phase default
LOWESS_FRAC = 0.04          # Methods, CHIRP Experiments (model chirp), O1
FREQ_RANGES = {"a": (0.2, 40.0), "b": (0.4, 40.0)}   # O1 readings
SPIKE_MV = -20.0            # standard choice, see docstring
SAG_TARGET_MV = -100.0      # IPFX SAG_TARGET, O2 reading a
SAG_STEP_PA = -100.0        # O2 reading b
PEAK_WIDTH = 0.005          # s, IPFX sag
BASELINE_INTERVAL = 0.03    # s, IPFX sag
LS_NAMES = ("SubThresh", "subthreshold", "C1LS")


# Outside inputs (protocol, Author, step 1.4): other dandisets of the paper's sources, pinned.
LEE_DANDISET, LEE_VERSION = "000636", "0.241120.0510"       # Lee, Dalley et al. 2023 (paper ref. 2)
MOUSE_DANDISET, MOUSE_VERSION = "000020", "0.210913.1639"   # Gouwens et al. 2020
# Per-cell labels of Lee, Dalley et al. (2023) from their analysis repository; nwb_id is the
# session id of the 000636 file.
LEE_TABLE = ("https://raw.githubusercontent.com/AllenInstitute/human_patchseq_gaba/"
             "5eb357a1cea246c7c847b5608a8fc7e87ea95b58/data/LeeDalley_manuscript_metadata_v2.csv")
# The Allen Institute's per-cell metadata of the mouse Patch-seq release of Gouwens et al.
# (2020), file 20200711_patchseq_metadata_mouse.csv, which maps cell specimen ids to the ephys
# session ids of the 000020 files and gives the T-type. The Allen portal does not give it at a
# fixed address; this is a copy in a public repository, pinned at a commit.
MOUSE_TABLE = ("https://raw.githubusercontent.com/keon-arbabi/patch-seq-microglia/"
               "bb5c0e206c6f01a0a5639fa3ef843641ecf4cb7e/data/patchseq/20200711_patchseq_metadata_mouse.csv")


def list_assets(dandiset=DANDISET, version=VERSION):
    """All assets of a pinned version: path, asset id and size."""
    url = f"{API}/dandisets/{dandiset}/versions/{version}/assets/?page_size=1000"
    out = []
    while url:
        with urllib.request.urlopen(url) as r:
            page = json.load(r)
        out += [dict(path=a["path"], asset_id=a["asset_id"], size=a["size"]) for a in page["results"]]
        url = page["next"]
    return out


def session_of(path):
    return path.split("_ses-")[1].split("_")[0]


def version_metadata(dandiset=DANDISET, version=VERSION):
    with urllib.request.urlopen(f"{API}/dandisets/{dandiset}/versions/{version}/") as r:
        return json.load(r)


def s3_url(asset_id):
    with urllib.request.urlopen(f"{API}/assets/{asset_id}/") as r:
        meta = json.load(r)
    return next(u for u in meta["contentUrl"] if "s3" in u)


def open_asset(asset_id):
    return h5py.File(remfile.File(s3_url(asset_id)), "r")


def _str(x):
    if isinstance(x, bytes):
        return x.decode()
    if isinstance(x, np.ndarray):
        return _str(x[()]) if x.shape == () else str(x)
    return str(x)


def _subject_and_sweeps(f):
    subj = {k: _str(f["general/subject"][k][()]) for k in f["general/subject"]}
    sweeps = [dict(name=k, stimulus=_str(f["acquisition"][k].attrs["stimulus_description"]))
              for k in f["acquisition"]]
    return subj, _str(f["general/session_id"][()]), sweeps


def process_file(asset, all_cells=False):
    """Open one file once: its subject, session id and sweep stimulus names, and, for a cell
    with chirp sweeps (or every cell, with all_cells), the reduced chirp and long-square data.
    A failed read is retried twice and then raised."""
    for attempt in range(3):
        try:
            with open_asset(asset["asset_id"]) as f:
                subj, session, sweeps = _subject_and_sweeps(f)
                cell = None
                if all_cells or any("CHIRP" in s["stimulus"] for s in sweeps):
                    cell = _load(f, sweeps)
            break
        except OSError:
            if attempt == 2:
                raise
    return dict(path=asset["path"], asset_id=asset["asset_id"], subject=subj, session_id=session,
                sweeps=sweeps, cell=cell)


def process_files(assets, workers=8, all_cells=False):
    """process_file over all assets in parallel processes. Streaming is I/O bound, but h5py
    holds a global lock, so threads would read one file at a time."""
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(process_file, assets, [all_cells] * len(assets), chunksize=1))


def _read(f, name):
    """Voltage (mV) and stimulus current (pA) of one sweep, and its sampling rate."""
    g = f["acquisition"][name]
    s = f["stimulus/presentation"][name.replace("_AD", "_DA")]
    v = g["data"][:].astype(float) * float(g["data"].attrs["conversion"]) * 1e3
    i = s["data"][:].astype(float) * float(s["data"].attrs["conversion"]) * 1e12
    return v, i, float(g["starting_time"].attrs["rate"])


def _segments(i, rate, thresh=0.5):
    on = np.abs(i) > thresh
    edges = np.flatnonzero(np.diff(on.astype(int))) + 1
    if on[0]:
        edges = np.r_[0, edges]
    if on[-1]:
        edges = np.r_[edges, len(i)]
    return [(a, b) for a, b in zip(edges[::2], edges[1::2])]


def _avg_down(x, width):
    n = len(x) // width
    return x[: n * width].reshape(n, width).mean(axis=1)


def _load(f, sweeps):
    """Read the chirp and hyperpolarizing long-square sweeps of one cell, reduced as loaded.

    Returns the downsampled chirp sweeps that pass the exclusions, and per long square the
    numbers the sag and input resistance need. Counts of dropped sweeps are kept.
    """
    chirp_names = [s["name"] for s in sweeps if "CHIRP" in s["stimulus"]]
    ls_names = [s["name"] for s in sweeps if any(t in s["stimulus"] for t in LS_NAMES)]
    out = dict(chirps=[], ls=[], drop=dict(chirp_truncated=0, chirp_spike=0, chirp_not20s=0,
                                           ls_truncated=0, chirp_lead_zero_only=0))
    for name in chirp_names:
        v, i, rate = _read(f, name)
        # the chirp runs from the first non-zero current after the test pulse (which ends
        # before 0.1 s) to the last non-zero sample
        nz = np.flatnonzero(np.abs(i) > 0.5)
        nz = nz[nz > int(0.2 * rate)]
        if not len(nz):
            continue
        a, b = int(nz[0]), int(nz[-1]) + 1
        dur = (b - a) / rate
        if abs(dur - 20.0) > 0.5:
            out["drop"]["chirp_not20s"] += 1
            continue
        if np.any(v[:b] == 0.0):
            out["drop"]["chirp_truncated"] += 1
            # zeros only before the chirp, with none inside it: counted, to show whether a
            # recording with a leading zero would be dropped wrongly
            if not np.any(v[a:b] == 0.0):
                out["drop"]["chirp_lead_zero_only"] += 1
            continue
        if v[a:b].max() > SPIKE_MV:
            out["drop"]["chirp_spike"] += 1
            continue
        width = int(round(rate / DOWN_RATE))
        pre = v[int(a - 0.4 * rate): int(a - 0.05 * rate)].mean()
        out["chirps"].append(dict(name=name, v=_avg_down(v[a:b], width), i=_avg_down(i[a:b], width),
                                  start=a / rate, end=b / rate, vm=pre,
                                  i_peak=float(np.abs(i[a:b]).max())))
    for name in ls_names:
        v, i, rate = _read(f, name)
        segs = [s for s in _segments(i, rate) if (s[1] - s[0]) / rate > 0.5]
        if not segs:
            continue
        a, b = segs[0]
        amp = float(np.median(i[a + 10: b - 10]))
        if amp >= 0:
            continue
        if np.any(v[: b + int(0.05 * rate)] == 0.0):
            out["drop"]["ls_truncated"] += 1
            continue
        seg = v[a:b]
        k = int(np.argmin(seg))
        hw = int(PEAK_WIDTH / 2 * rate)
        v_peak_avg = seg[max(k - hw, 0): k + hw + 1].mean()
        nb = int(BASELINE_INTERVAL * rate)
        out["ls"].append(dict(name=name, amp=amp, v_min=float(seg[k]), v_peak=float(v_peak_avg),
                              v_base=float(v[a - nb:a].mean()), v_steady=float(v[b - nb:b].mean()),
                              v_base100=float(v[a - int(0.1 * rate):a].mean())))
    return out


def impedance(chirps, reading="a", frac=LOWESS_FRAC):
    """Smoothed impedance profile of the averaged chirp sweeps (MOhm against Hz). `frac` other
    than LOWESS_FRAC is used only to show how the measures depend on the smoothing."""
    n = min(len(c["v"]) for c in chirps)    # sweeps can differ by a sample
    v = np.mean([c["v"][:n] for c in chirps], axis=0)
    i = np.mean([c["i"][:n] for c in chirps], axis=0)
    z = np.fft.rfft(v) / np.fft.rfft(i)
    freq = np.fft.rfftfreq(len(v), d=1.0 / DOWN_RATE)
    lo, hi = FREQ_RANGES[reading]
    keep = (freq >= lo) & (freq < hi)
    amp = np.abs(z[keep]) * 1e3        # mV / pA = GOhm, so x1000 for MOhm
    f = freq[keep]
    smooth = lowess(amp, f, frac=frac, return_sorted=False)
    return f, amp, smooth


def resonance(f, smooth):
    """fres, Q and f3dB from a smoothed profile (O1)."""
    k = int(np.argmax(smooth))
    zmax, z0 = smooth[k], smooth[0]
    below = np.flatnonzero(smooth[k:] < zmax / np.sqrt(2))
    f3db = float(f[k + below[0]]) if len(below) else np.nan
    return dict(fres=float(f[k]), Q=float(zmax / z0), f3db=f3db, zmax=float(zmax), z0=float(z0))


def is_resonant(fres, q, q_min=1.05):
    return (fres > 1.0) & (q > q_min)


def sag_rin(ls):
    """Sag ratio and input resistance under readings (a) and (b) of O2 and O3."""
    if not ls:
        return dict(sag_a=np.nan, sag_b=np.nan, rin_a=np.nan, rin_b=np.nan, vm_b=np.nan,
                    n_ls=0, step_b=np.nan)
    sag = np.array([(s["v_peak"] - s["v_steady"]) / (s["v_peak"] - s["v_base"]) for s in ls])
    amps = np.array([s["amp"] for s in ls])
    vmin = np.array([s["v_min"] for s in ls])
    vpeak = np.array([s["v_peak"] for s in ls])
    sag_a = float(sag[np.argmin(np.abs(vpeak - SAG_TARGET_MV))])
    if len(np.unique(amps)) >= 2:
        m = np.linalg.lstsq(np.vstack([amps, np.ones_like(amps)]).T, vmin, rcond=None)[0][0]
    else:
        base = np.mean([s["v_base100"] for s in ls])
        m = np.linalg.lstsq(np.vstack([np.r_[amps, 0.0], np.ones(len(amps) + 1)]).T,
                            np.r_[vmin, base], rcond=None)[0][0]
    rin_a = float(m * 1e3)
    d = np.abs(amps - SAG_STEP_PA)
    near = np.isclose(d, d.min())
    sag_b = float(sag[near].mean())
    rin_b = float(np.mean([(s["v_steady"] - s["v_base"]) / s["amp"] for s, n in zip(ls, near) if n]) * 1e3)
    vm_b = float(np.mean([s["v_base100"] for s in ls]))
    return dict(sag_a=sag_a, sag_b=sag_b, rin_a=rin_a, rin_b=rin_b, vm_b=vm_b, n_ls=len(ls),
                step_b=float(np.mean(np.unique(amps[near]))))


def chartrand_table():
    """Per-cell labels of Chartrand et al. (2023), with the session (Ephys ROI result) id."""
    import pandas as pd
    t = pd.read_csv(f"{CHARTRAND_REPO}/{CHARTRAND_COMMIT}/{CHARTRAND_TABLE}", low_memory=False)
    t["session_id"] = t["nwb_path"].astype(str).str.extract(r"Ephys_Roi_Result_(\d+)")[0]
    return t


# Human donors of Supplementary Table 1 of the paper (read from the preprint's supplement): donor
# name -> (Dataset, Area, Disease category, Lobe), with empty strings where the table is blank.
# Used to check which dandiset donors the paper lists, under which of its datasets, and for the
# region and disease labels of figs1-region-pathology.
TABLE_S1 = {
    "H16.03.001": ("Chartrand", "MTG", "Epilepsy", ""),
    "H16.03.006": ("Chartrand", "MTG", "Epilepsy", ""),
    "H16.03.008": ("Chartrand", "MTG", "Epilepsy", ""),
    "H16.03.012": ("Chartrand", "TemL", "Epilepsy", ""),
    "H16.06.010": ("Chartrand", "ITG", "Epilepsy", ""),
    "H16.06.011": ("Chartrand", "MTG", "Epilepsy", ""),
    "H16.06.012": ("Chartrand", "MFG", "Tumor", ""),
    "H17.03.002": ("AcuteLDPublished", "MTG", "epilepsy", "TemL"),
    "H17.03.005": ("Chartrand", "MTG", "Epilepsy", "TemL"),
    "H17.03.006": ("AcuteLDPublished", "STG", "epilepsy", "TemL"),
    "H17.03.007": ("Chartrand", "MTG", "Epilepsy", "TemL"),
    "H17.03.008": ("AcuteLDPublished", "STG", "epilepsy", "TemL"),
    "H17.03.009": ("Chartrand", "MTG", "Epilepsy", ""),
    "H17.03.010": ("AcuteLDPublished", "MTG", "epilepsy", "TemL"),
    "H17.03.013": ("AcuteLDPublished", "SFG", "epilepsy", "FroL"),
    "H17.03.014": ("AcuteLDPublished", "TemL", "epilepsy", "TemL"),
    "H17.03.015": ("AcuteLDPublished", "MTG", "tumor", "TemL"),
    "H17.03.016": ("AcuteLDPublished", "MTG", "epilepsy", "TemL"),
    "H17.06.003": ("AcuteLDPublished", "MTG", "epilepsy", "TemL"),
    "H17.06.006": ("AcuteLDPublished", "MTG", "epilepsy", "TemL"),
    "H17.06.007": ("Chartrand", "MFG", "Tumor", ""),
    "H17.06.012": ("AcuteLDPublished", "MTG", "epilepsy", "TemL"),
    "H17.06.013": ("AcuteLDPublished", "PLP", "epilepsy", "TemL"),
    "H17.06.015": ("AcuteLDPublished", "TemL", "epilepsy", "TemL"),
    "H17.26.002": ("AcuteLDPublished", "TemL", "tumor", "TemL"),
    "H17.26.003": ("AcuteLDPublished", "MTG", "tumor", "TemL"),
    "H17.26.005": ("AcuteLDPublished", "IFGtr", "tumor", "FroL"),
    "H18.03.002": ("AcuteLDPublished", "LOrG", "epilepsy", "FroL"),
    "H18.03.003": ("AcuteLDPublished", "", "tumor", ""),
    "H18.03.004": ("AcuteLDPublished", "ITG", "epilepsy", "TemL"),
    "H18.03.005": ("AcuteLDPublished", "STG", "epilepsy", "TemL"),
    "H18.03.006": ("AcuteLDPublished", "SPL", "epilepsy", "ParL"),
    "H18.03.008": ("AcuteLDPublished", "MTG", "epilepsy", "TemL"),
    "H18.03.009": ("AcuteLDPublished", "MTG", "epilepsy", ""),
    "H18.03.010": ("AcuteLDPublished", "MTG", "epilepsy", "TemL"),
    "H18.03.011": ("AcuteLDPublished", "PRG", "epilepsy", "TemL"),
    "H18.03.012": ("AcuteLDPublished", "PRG", "epilepsy", "TemL"),
    "H18.03.313": ("AcuteLDPublished", "STG", "epilepsy", "TemL"),
    "H18.03.314": ("AcuteLDPublished", "MTG", "epilepsy", "TemL"),
    "H18.03.315": ("AcuteLDPublished", "MTG", "epilepsy", "TemL"),
    "H18.03.316": ("AcuteLDPublished", "STG", "epilepsy", "TemL"),
    "H18.03.317": ("AcuteLDPublished", "TemL", "epilepsy", "TemL"),
    "H18.03.318": ("AcuteLDPublished", "MTG", "epilepsy", "TemL"),
    "H18.03.319": ("AcuteLDPublished", "MTG", "epilepsy", "TemL"),
    "H18.03.320": ("AcuteLDPublished", "MTG", "epilepsy", "TemL"),
    "H18.03.322": ("AcuteLDPublished", "MTG", "epilepsy", "TemL"),
    "H18.03.323": ("AcuteLDPublished", "SFG", "epilepsy", "FroL"),
    "H18.06.001": ("Chartrand", "SFG", "Tumor", ""),
    "H18.06.004": ("Chartrand", "MTG", "Tumor", ""),
    "H18.06.005": ("AcuteLDPublished", "MTG", "tumor", "TemL"),
    "H18.06.358": ("AcuteLDPublished", "MFG", "tumor", "FroL"),
    "H18.06.362": ("AcuteLDPublished", "SFG", "tumor", "FroL"),
    "H18.06.363": ("AcuteLDPublished", "MTG", "epilepsy", "TemL"),
    "H18.06.365": ("AcuteLDPublished", "MFG", "tumor", "FroL"),
    "H18.06.366": ("AcuteLDPublished", "MTG", "epilepsy", "TemL"),
    "H18.06.367": ("AcuteLDPublished", "MTG", "tumor", "TemL"),
    "H18.06.368": ("AcuteLDPublished", "MTG", "epilepsy", "TemL"),
    "H18.06.371": ("AcuteLDPublished", "MTG", "epilepsy", "TemL"),
    "H18.26.403": ("AcuteLDPublished", "MFG", "tumor", "FroL"),
    "H18.26.404": ("AcuteLDPublished", "MTG", "tumor", "TemL"),
    "H18.28.001": ("Chartrand", "", "", ""),
    "H18.28.021": ("Chartrand", "FroL", "hydrocephalus", "FroL"),
    "H18.28.022": ("Chartrand", "TemL", "tumor", "TemL"),
    "H18.28.025": ("Chartrand", "SOG", "Tumor", ""),
    "H18.29.124": ("Chartrand", "ITG", "epilepsy", "TemL"),
    "H18.29.125": ("Chartrand", "AnG", "epilepsy", "ParL"),
    "H18.29.135": ("Chartrand", "SFG", "tumor", ""),
    "H18.29.136": ("Chartrand", "SFG", "tumor", "FroL"),
    "H18.29.138": ("Chartrand", "MTG", "", ""),
    "H19.03.301": ("AcuteLDPublished", "MTG", "epilepsy", "TemL"),
    "H19.03.302": ("AcuteLDPublished", "MTG", "epilepsy", "TemL"),
    "H19.03.304": ("Chartrand", "TemL", "Epilepsy", ""),
    "H19.03.305": ("AcuteLDPublished", "MTG", "epilepsy", "TemL"),
    "H19.03.306": ("AcuteLDPublished", "ITG", "epilepsy", "TemL"),
    "H19.03.308": ("AcuteLDPublished", "ITG", "epilepsy", "TemL"),
    "H19.03.309": ("AcuteLDPublished", "SFG", "tumor", "FroL"),
    "H19.03.310": ("AcuteLDPublished", "SFG", "tumor", "FroL"),
    "H19.03.311": ("AcuteLDPublished", "TemL", "epilepsy", "TemL"),
    "H19.03.312": ("AcuteLDPublished", "MFG", "epilepsy", "FroL"),
    "H19.03.313": ("Chartrand", "TemL", "Epilepsy", ""),
    "H19.03.314": ("AcuteLDPublished", "MTG", "epilepsy", "TemL"),
    "H19.03.315": ("AcuteLDPublished", "TemL", "epilepsy", "TemL"),
    "H19.03.316": ("AcuteLDPublished", "PaCG", "epilepsy", "FroL"),
    "H19.03.317": ("AcuteLDPublished", "MTG", "epilepsy", "TemL"),
    "H19.03.319": ("AcuteLDPublished", "ITG", "epilepsy", "TemL"),
    "H19.03.320": ("AcuteLDPublished", "MTG", "epilepsy", "TemL"),
    "H19.03.321": ("Chartrand", "MTG", "epilepsy", "TemL"),
    "H19.03.323": ("AcuteLDPublished", "MTG", "epilepsy", "TemL"),
    "H19.06.351": ("AcuteLDPublished", "MTG", "tumor", "TemL"),
    "H19.06.353": ("AcuteLDPublished", "MFG", "Tumor status -", "FroL"),
    "H19.06.356": ("AcuteLDPublished", "TemL", "epilepsy", "TemL"),
    "H19.06.363": ("Chartrand", "OccL", "tumor", "OccL"),
    "H19.28.004": ("Chartrand", "MTG", "tumor", ""),
    "H19.28.005": ("Chartrand", "MTG", "tumor", "TemL"),
    "H19.28.007": ("Chartrand", "IOG", "", ""),
    "H19.28.009": ("Chartrand", "IOG", "hydrocephalus", "OccL"),
    "H19.28.014": ("Chartrand", "FroL", "tumor", ""),
    "H19.28.015": ("Chartrand", "TemL", "tumor", ""),
    "H19.28.018": ("Chartrand", "FroL", "tumor", ""),
    "H19.28.025": ("Chartrand", "FroL", "tumor", ""),
    "H19.29.142": ("Chartrand", "MFG", "tumor", ""),
    "H19.29.144": ("Chartrand", "MTG", "tumor", ""),
    "H19.29.146": ("Chartrand", "", "tumor", ""),
    "H19.29.147": ("Chartrand", "TemL", "tumor", ""),
    "H19.29.149": ("Chartrand", "MTG", "tumor", ""),
    "H19.29.160": ("Chartrand", "OccL", "tumor", ""),
    "H19.29.162": ("Chartrand", "SFG", "tumor", ""),
    "H20.03.301": ("Chartrand", "MTG", "epilepsy", "TemL"),
    "H20.03.302": ("AcuteLDPublished", "MTG", "epilepsy", "TemL"),
    "H20.03.303": ("AcuteLDPublished", "MTG", "epilepsy", "TemL"),
    "H20.06.351": ("AcuteLDPublished", "MTG", "epilepsy", "TemL"),
    "H20.28.001": ("Chartrand", "", "hydrocephalus", ""),
    "H20.28.002": ("Chartrand", "FroL", "tumor", "FroL"),
    "H20.28.006": ("Chartrand", "TemL", "tumor", "TemL"),
    "H20.28.008": ("Chartrand", "FroL", "tumor", "FroL"),
    "H20.28.009": ("Chartrand", "TemL", "tumor", "TemL"),
    "H20.28.012": ("Chartrand", "ParL", "tumor", "ParL"),
    "H20.28.019": ("Chartrand", "FroL", "tumor", "FroL"),
    "H20.28.022": ("Chartrand", "FroL", "tumor", "FroL"),
    "H20.28.023": ("Chartrand", "ParL", "hydrocephalus", "ParL"),
    "H20.28.027": ("Chartrand", "TemL", "tumor", "TemL"),
    "H20.28.028": ("Chartrand", "FroL", "tumor", "FroL"),
    "H20.28.031": ("Chartrand", "TemL", "tumor", "TemL"),
    "H20.28.039": ("Chartrand", "TemL", "tumor", "TemL"),
    "H20.29.174": ("Chartrand", "TemL", "epilepsy", "TemL"),
    "H20.29.177": ("Chartrand", "", "", ""),
    "H20.29.181": ("Chartrand", "FroL", "epilepsy", "FroL"),
    "H20.29.182": ("Chartrand", "SFG", "", ""),
    "H20.29.183": ("Chartrand", "", "", ""),
    "H20.29.186": ("Chartrand", "TemL", "", ""),
    "H21.03.305": ("AcuteLDPublished", "TemL", "epilepsy", "TemL"),
    "H21.03.306": ("Chartrand", "MTG", "Epilepsy", ""),
    "H21.03.309": ("Chartrand", "TemL", "Epilepsy", ""),
    "H21.03.310": ("Chartrand", "TemL", "Epilepsy", ""),
    "H21.03.315": ("Chartrand", "TemL", "Epilepsy", ""),
    "H21.03.316": ("Chartrand", "TemL", "", ""),
    "H21.06.353": ("Chartrand", "", "tumor", ""),
    "H21.28.006": ("Chartrand", "SFG", "tumor", ""),
    "H21.28.013": ("Chartrand", "TemL", "tumor", ""),
    "H21.28.019": ("Chartrand", "", "tumor", ""),
    "H21.28.022": ("Chartrand", "", "tumor", ""),
    "H21.28.034": ("Chartrand", "", "", ""),
    "H21.28.041": ("Chartrand", "", "", ""),
    "H21.29.190": ("Chartrand", "MTG", "tumor", ""),
    "H21.29.191": ("Chartrand", "SFG", "tumor", ""),
    "H21.29.194": ("Chartrand", "SPL", "", ""),
    "H21.29.197": ("Chartrand", "MFG", "", ""),
    "H21.29.199": ("Chartrand", "", "", ""),
    "H21.29.200": ("Chartrand", "", "", ""),
    "H21.29.201": ("Chartrand", "", "tumor", ""),
    "H21.29.203": ("Chartrand", "", "", ""),
    "H21.29.205": ("Chartrand", "", "", ""),
    "H21.29.206": ("Chartrand", "", "", ""),
    "H21.29.207": ("Chartrand", "LOrG", "", ""),
    "H22.03.305": ("NewLD", "TCx_L_L5", "", ""),
    "H22.26.404": ("Chartrand", "", "tumor", ""),
    "H22.29.210": ("Chartrand", "", "", ""),
    "H22.29.211": ("Chartrand", "", "", ""),
    "H23.03.302": ("NewLD", "TCx_L_L5", "", ""),
    "H23.03.307": ("NewLD", "TCx_L_L4", "", ""),
    "H23.03.308": ("NewLD", "TCx_L_L6", "", ""),
    "H23.03.309": ("NewLD", "TCx_L_L6", "", ""),
    "H23.26.405": ("NewLD", "TCx_L_L5", "", ""),
    "H24.03.001": ("NewLD", "TCx_L_L3", "", ""),
    "H24.06.352": ("NewLD", "TCx_L_L6", "", ""),
    "H24.06.353": ("NewLD", "TCx_L_L4", "", ""),
    "H24.26.402": ("NewLD", "FCx_L_L5", "", ""),
    "H24.26.408": ("NewLD", "FCx_L_L6", "", ""),
    "H25.03.302": ("NewLD", "TCx_L_L5", "", ""),
    "H25.03.303": ("NewLD", "TCx_L_L5", "", ""),
    "H18.06.364": ("PublishedLD_Cultured", "", "tumor", "TemL"),
    "H19.03.004": ("PublishedLD_Cultured", "", "epilepsy", "TemL"),
    "H19.03.006": ("PublishedLD_Cultured", "", "epilepsy", "TemL"),
    "H19.03.307": ("PublishedLD_Cultured", "", "tumor", "FroL"),
    "H19.03.318": ("PublishedLD_Cultured", "", "epilepsy", "TemL"),
    "H19.06.352": ("PublishedLD_Cultured", "", "cavernoma", "TemL"),
    "H19.06.355": ("PublishedLD_Cultured", "", "tumor", "TemL"),
    "H19.06.360": ("PublishedLD_Cultured", "", "tumor", "FroL"),
    "H19.06.361": ("PublishedLD_Cultured", "", "tumor", ""),
    "H19.06.362": ("PublishedLD_Cultured", "", "Epileptiform", "TemL"),
    "H19.06.364": ("PublishedLD_Cultured", "", "tumor", "FroL"),
    "H19.26.402": ("PublishedLD_Cultured", "", "tumor", "FroL"),
    "H19.26.405": ("PublishedLD_Cultured", "", "tumor", "FroL"),
    "H19.26.407": ("PublishedLD_Cultured", "", "tumor", "FroL"),
    "H20.03.304": ("PublishedLD_Cultured", "", "epilepsy", "TemL"),
    "H20.03.305": ("PublishedLD_Cultured", "", "epilepsy", "TemL"),
    "H20.03.307": ("PublishedLD_Cultured", "", "epilepsy", "TemL"),
    "H20.03.310": ("PublishedLD_Cultured", "", "epilepsy", ""),
    "H20.06.354": ("PublishedLD_Cultured", "", "tumor", "ParL"),
    "H20.06.355": ("PublishedLD_Cultured", "", "epilepsy", "TemL"),
    "H20.06.356": ("PublishedLD_Cultured", "", "tumor", "FroL"),
    "H20.26.401": ("PublishedLD_Cultured", "", "tumor", "TemL"),
    "H20.26.402": ("PublishedLD_Cultured", "", "tumor", "FroL"),
    "H20.26.406": ("PublishedLD_Cultured", "", "tumor", "TemL"),
    "H20.26.407": ("PublishedLD_Cultured", "", "tumor", "TemL"),
    "H20.26.408": ("PublishedLD_Cultured", "", "tumor", "TemL"),
    "H20.26.409": ("PublishedLD_Cultured", "", "tumor", "ParL"),
    "H20.26.411": ("PublishedLD_Cultured", "", "tumor", "FroL"),
    "H20.26.412": ("PublishedLD_Cultured", "", "tumor", "FroL"),
    "H21.03.302": ("PublishedLD_Cultured", "", "tumor", "TemL"),
    "H21.03.304": ("PublishedLD_Cultured", "", "epilepsy", "TemL"),
    "H21.26.401": ("PublishedLD_Cultured", "", "tumor", "TemL"),
    "H21.26.402": ("PublishedLD_Cultured", "", "tumor", "TemL"),
    "H21.26.403": ("PublishedLD_Cultured", "", "tumor", "TemL"),
    "H21.26.404": ("PublishedLD_Cultured", "", "tumor", ""),
}

TABLE_S1_DONORS = {}
for _d, _v in TABLE_S1.items():
    TABLE_S1_DONORS.setdefault(_v[0], []).append(_d)


def lee_table():
    """Per-cell labels of Lee, Dalley et al. (2023): subclass, condition (acute or culture),
    donor, layer, joined to the 000636 files by session id (nwb_id). One cell is listed twice
    with identical rows; duplicates are dropped."""
    import pandas as pd
    t = pd.read_csv(LEE_TABLE).drop_duplicates()
    t.columns = [c.strip() for c in t.columns]
    t = t[t["nwb_id"].notna()].copy()
    t["session_id"] = t["nwb_id"].astype("int64").astype(str)
    return t


def mouse_table():
    """Allen per-cell metadata of the mouse Patch-seq release (Gouwens et al. 2020)."""
    import pandas as pd
    t = pd.read_csv(MOUSE_TABLE)
    t["session_id"] = t["ephys_session_id"].astype("int64").astype(str)
    return t


def _reml_parts(theta, y, X, groups):
    """REML log-likelihood of a random-intercept model and the GLS estimate, for theta =
    (donor variance, residual variance)."""
    su, se = theta
    p = X.shape[1]
    XtVX = np.zeros((p, p))
    XtVy = np.zeros(p)
    logdet = 0.0
    for idx in groups:
        Xi, yi, n = X[idx], y[idx], len(idx)
        c = su / (se + n * su)
        sx, sy = Xi.sum(0), yi.sum()
        XtVX += (Xi.T @ Xi - c * np.outer(sx, sx)) / se
        XtVy += (Xi.T @ yi - c * sx * sy) / se
        logdet += (n - 1) * np.log(se) + np.log(se + n * su)
    C = np.linalg.inv(XtVX)
    beta = C @ XtVy
    quad = 0.0
    for idx in groups:
        r, n = y[idx] - X[idx] @ beta, len(idx)
        quad += (r @ r - su / (se + n * su) * r.sum() ** 2) / se
    sign, ld = np.linalg.slogdet(XtVX)
    return -0.5 * (logdet + ld + quad), beta, C


def lmm_satterthwaite(formula, data, group, tests):
    """REML linear mixed model with a random intercept for `group`, and Satterthwaite tests (O5
    reading a). `tests` maps a name to a list of design-matrix columns whose coefficients are
    tested jointly (one column: a t test; several: an F test). Returns the coefficients, and per
    test the estimate (one-df tests), F, numerator and denominator df and p, and whether the
    optimiser converged."""
    import patsy
    from scipy import optimize, stats
    y, X = patsy.dmatrices(formula, data, return_type="dataframe", NA_action="drop")
    g = data.loc[X.index, group].to_numpy()
    groups = [np.flatnonzero(g == k) for k in np.unique(g)]
    yv, Xv = y.to_numpy().ravel(), X.to_numpy()
    v0 = np.var(yv)
    nll = lambda lt: -_reml_parts(np.exp(lt), yv, Xv, groups)[0]
    best = None
    for start in (np.log([v0 / 2, v0 / 2]), np.log([v0 / 20, v0])):
        r = optimize.minimize(nll, start, method="Nelder-Mead",
                              options=dict(xatol=1e-8, fatol=1e-10, maxiter=4000))
        if best is None or r.fun < best.fun:
            best = r
    theta = np.exp(best.x)
    ll, beta, C = _reml_parts(theta, yv, Xv, groups)
    # Covariance of the variance estimates from the numerical Hessian of the REML log-likelihood
    # on the variance scale (as lmerTest). A donor variance at the boundary is held fixed, so
    # the residual variance alone carries the df.
    free = [0, 1] if theta[0] > 1e-6 * theta[1] else [1]
    h = 1e-4 * theta

    def ll_at(t):
        return _reml_parts(t, yv, Xv, groups)[0]

    H = np.zeros((2, 2))
    for i in free:
        for j in free:
            ei, ej = np.eye(2)[i] * h[i], np.eye(2)[j] * h[j]
            H[i, j] = (ll_at(theta + ei + ej) - ll_at(theta + ei - ej) - ll_at(theta - ei + ej)
                       + ll_at(theta - ei - ej)) / (4 * h[i] * h[j])
    A = np.zeros((2, 2))
    A[np.ix_(free, free)] = np.linalg.inv(-H[np.ix_(free, free)])
    dC = [(_reml_parts(theta + np.eye(2)[k] * h[k], yv, Xv, groups)[2]
           - _reml_parts(theta - np.eye(2)[k] * h[k], yv, Xv, groups)[2]) / (2 * h[k]) for k in range(2)]
    cols = list(X.columns)

    def df_one(l):
        var = l @ C @ l
        grad = np.array([l @ dC[k] @ l for k in range(2)])
        return 2 * var ** 2 / (grad @ A @ grad), var

    out = dict(coef=dict(zip(cols, beta)), converged=bool(best.success), n=len(yv), groups=len(groups),
               theta=theta, tests={})
    for name, keys in tests.items():
        L = np.zeros((len(keys), len(cols)))
        for i, k in enumerate(keys):
            L[i, cols.index(k)] = 1.0
        if len(keys) == 1:
            nu, var = df_one(L[0])
            est = float(L[0] @ beta)
            t = est / np.sqrt(var)
            out["tests"][name] = dict(est=est, se=float(np.sqrt(var)), F=t ** 2, df1=1, df2=float(nu),
                                      p=float(2 * stats.t.sf(abs(t), nu)))
        else:
            q = len(keys)
            M = L @ C @ L.T
            w, P = np.linalg.eigh(M)
            F = float((L @ beta) @ np.linalg.solve(M, L @ beta)) / q
            nus = np.array([df_one(l)[0] for l in P.T @ L])
            E = np.sum(nus[nus > 2] / (nus[nus > 2] - 2))
            nu = 2 * E / (E - q) if E > q else np.nan
            out["tests"][name] = dict(est=np.nan, se=np.nan, F=F, df1=q, df2=float(nu),
                                      p=float(stats.f.sf(F, q, nu)) if np.isfinite(nu) else np.nan)
    return out


def chi2_gof(k, n, p_ref):
    """Goodness-of-fit chi-square of k resonant of n cells against the reference proportion
    p_ref (O6 reading a): chi2 and p (1 df)."""
    from scipy import stats
    exp = np.array([n * p_ref, n * (1 - p_ref)])
    if np.any(exp == 0):
        return np.nan, np.nan
    r = stats.chisquare(np.array([k, n - k]), exp)
    return float(r.statistic), float(r.pvalue)


def chi2_2x2(k1, n1, k2, n2):
    """Pearson chi-square of a 2x2 table without continuity correction (O6 reading b)."""
    from scipy import stats
    r = stats.chi2_contingency(np.array([[k1, n1 - k1], [k2, n2 - k2]]), correction=False)
    return float(r[0]), float(r[1])


# The paper's mouse cells, Supplementary Table 2b: cell specimen id (spec_id) -> mouse (628 rows),
# read from the preprint's supplement (PDF text layer). Used only to select the mouse cells of
# 000020 that the paper analysed, through the Allen metadata (mouse_table), and to check the link.
TABLE_S2B = {
    637381329: 347157, 637824915: 349020, 637833144: 349020, 637846989: 349020, 637866154:
    349020, 638205354: 347159, 638212024: 347159, 638225388: 347159, 638246905: 349007,
    639018814: 347205, 639216521: 348997, 639689999: 350672, 639796648: 350674, 640106803:
    350675, 640311818: 351472, 640319052: 351472, 642110310: 351473, 642124659: 351473,
    642429586: 353735, 642442513: 353735, 642488015: 352686, 642496703: 352686, 642512300:
    352686, 642532676: 352686, 642767494: 354378, 642827810: 352688, 642833509: 353737,
    642842839: 353737, 642851911: 353737, 643190956: 353740, 643251590: 352690, 643269551:
    352690, 643501610: 355016, 644842725: 355222, 644848057: 355222, 644857312: 355222,
    644917900: 355223, 644919379: 355223, 644934835: 354958, 644935848: 355230, 644936843:
    354958, 644941196: 355230, 644946047: 355230, 644946408: 355230, 644957513: 355585,
    644976625: 355224, 644994103: 354959, 645000287: 354959, 645009607: 354959, 645016032:
    354959, 645016286: 354959, 645023727: 354959, 645075128: 355226, 645158069: 355591,
    645162257: 355228, 645169930: 355228, 648582997: 358898, 648585371: 358898, 648593656:
    358898, 648594299: 358898, 648605614: 358898, 648607165: 358898, 649008116: 358897,
    649012415: 358897, 649382312: 359342, 650132917: 361706, 650156059: 361705, 650161028:
    361705, 650172921: 361705, 650476171: 362153, 650484677: 362153, 651151937: 361703,
    651161691: 361703, 651167896: 361703, 652300499: 362149, 652303366: 362149, 652305423:
    362149, 652810157: 363968, 652811224: 363968, 652812484: 363968, 652938130: 361253,
    652953931: 363973, 652953971: 363973, 652959132: 363973, 652959904: 363973, 653024237:
    363949, 653024481: 363949, 653031614: 363967, 653031656: 363967, 653199987: 363969,
    653203017: 363969, 653677436: 363946, 654407470: 364559, 654689557: 364558, 656912028:
    367205, 657185314: 367172, 657194483: 367208, 657532988: 368853, 657585527: 368853,
    657945461: 368860, 658061248: 368761, 658068133: 368761, 658075752: 368761, 658089840:
    368761, 658103346: 368861, 658124114: 368861, 658411218: 368862, 658435131: 368863,
    658441785: 368863, 658477694: 368863, 658603411: 368864, 659147142: 368865, 659678793:
    372795, 660286172: 372798, 661401628: 374536, 661422469: 374536, 667300994: 377309,
    667306013: 377309, 667319630: 377309, 667320923: 377309, 667321194: 377309, 667478348:
    377310, 667478506: 377310, 667492234: 377313, 667492404: 377310, 667492978: 377313,
    667493822: 377313, 667585479: 377310, 668242473: 377316, 668292781: 377316, 668319974:
    377316, 668426472: 377316, 668489573: 378475, 669522853: 378110, 669523148: 378110,
    669567574: 378110, 670534322: 378108, 670556259: 378108, 670607755: 378108, 671876425:
    379873, 671927927: 379873, 671943738: 379873, 673047103: 379874, 673121351: 379874,
    673139917: 379874, 673724358: 379866, 674238265: 380156, 674240849: 380156, 674246494:
    380156, 674247723: 381042, 674471452: 380160, 674559170: 381045, 674582479: 381045,
    675025710: 381047, 675027801: 380161, 676757248: 380655, 677042379: 381810, 677042504:
    381810, 680904066: 381812, 680964142: 382695, 682158343: 384211, 682163968: 384211,
    682177103: 384211, 682320370: 384211, 682331689: 384211, 685382599: 384859, 686334539:
    384591, 686334676: 384591, 688133015: 385740, 688152462: 385740, 688175350: 385740,
    689256816: 385743, 689279957: 385743, 691665864: 386058, 691673416: 386058, 691685873:
    386058, 692296799: 387320, 692309268: 387320, 697764035: 389956, 697811579: 389956,
    697811820: 389956, 700161354: 391467, 700193566: 391467, 700278065: 391467, 701148434:
    390981, 701152294: 390981, 701155312: 390981, 701684250: 390983, 706531271: 392647,
    706531340: 392647, 706544221: 392647, 707660063: 393686, 707666779: 393686, 707678952:
    393686, 707681894: 393686, 708495657: 393687, 708513415: 393687, 708696754: 393922,
    708766941: 393922, 709417950: 393923, 709423277: 393692, 709447918: 393923, 709453221:
    393923, 709461711: 393923, 710346584: 393924, 711477649: 396817, 711483359: 396817,
    711508435: 396817, 711510463: 396817, 711572453: 396625, 711572656: 396817, 711577762:
    396625, 714701049: 397651, 714717722: 397651, 714722191: 397651, 716556217: 397654,
    716562206: 397654, 716832846: 397655, 716846357: 397655, 717637005: 399698, 717655913:
    399698, 717675736: 399698, 717770635: 399698, 718849411: 399825, 724191966: 403559,
    724744790: 403560, 724756081: 403560, 724770442: 403560, 724802323: 403560, 724812900:
    403560, 726156251: 404479, 726192665: 404479, 727146579: 402685, 730829986: 407127,
    730849363: 407127, 730859444: 407127, 730867067: 407127, 730878829: 407127, 731882356:
    406655, 731917470: 406655, 731974838: 407131, 731980846: 406655, 732708277: 406388,
    733537608: 406389, 734802524: 406386, 736485304: 407562, 736493069: 407562, 739594128:
    408755, 739710318: 408755, 740329222: 408759, 740377985: 408893, 741202597: 408761,
    741225385: 408761, 741894708: 408892, 741977538: 409200, 742016193: 409200, 742022294:
    409200, 742059312: 409200, 743013006: 408894, 743770160: 411627, 746086313: 411498,
    746102029: 411498, 746108633: 411498, 746172313: 411498, 750378755: 412517, 750421101:
    412517, 750421132: 412517, 750773551: 412518, 750780017: 412518, 750783623: 412518,
    750786577: 412518, 750795641: 412518, 752076719: 412526, 754271180: 412527, 761409397:
    417268, 764341238: 418814, 764365826: 418814, 764391439: 418814, 764464218: 418814,
    764479836: 418814, 764484965: 418814, 764500049: 419287, 764834652: 418815, 764870999:
    419797, 764896381: 419797, 764897253: 419797, 764898234: 419797, 764899841: 419797,
    764899933: 419291, 764901187: 419797, 764901694: 419291, 764902677: 419291, 764902707:
    419291, 764915850: 419291, 764916581: 419797, 764929763: 419797, 765143388: 419797,
    766049138: 418816, 766068893: 418816, 766204354: 422598, 766224440: 422598, 766774703:
    421030, 767257549: 421031, 788256204: 427597, 788349250: 427597, 788362658: 427597,
    788400935: 427597, 788418848: 427597, 797062169: 431562, 797113792: 431562, 797153425:
    431562, 799870027: 432548, 802366304: 432548, 812969884: 437762, 812989401: 437559,
    813000460: 437559, 821594273: 442794, 821652024: 442794, 823681740: 442769, 823719680:
    442796, 823745688: 442796, 823889517: 442797, 823907738: 442797, 823952975: 442797,
    823964038: 442797, 823968176: 442797, 824701767: 442606, 824792964: 442606, 824840538:
    442606, 825512557: 443337, 825522397: 443337, 825525063: 443337, 825525155: 443337,
    825534003: 443337, 825549510: 444161, 826700106: 443338, 826710259: 443338, 826712572:
    443338, 826719991: 443338, 826739825: 443338, 827347629: 445308, 827447865: 445308,
    827448258: 445308, 827503672: 445308, 827524052: 445308, 827573535: 445308, 827652298:
    445308, 828727693: 445711, 828778207: 445711, 828803869: 445711, 830445950: 445712,
    832005570: 445685, 833896435: 446681, 834073873: 446681, 834160937: 446681, 839819559:
    450876, 844226005: 452866, 844231938: 452866, 844232846: 452866, 844242654: 452866,
    844254029: 452866, 844269667: 452866, 844282161: 452866, 845586342: 453051, 845602469:
    453051, 845614297: 453051, 848635223: 455016, 851858759: 457299, 854425428: 456104,
    855275163: 456105, 866267921: 461574, 866337101: 461574, 866999931: 461933, 867015583:
    461933, 867017156: 461933, 867027741: 461933, 867038197: 461933, 867096689: 461933,
    867130068: 461933, 867176038: 461933, 886464017: 468435, 886482499: 468435, 887156236:
    468437, 888001481: 470194, 888080861: 470194, 888088377: 470194, 888108541: 470194,
    888115032: 470194, 888214374: 470194, 889183564: 470195, 889218836: 470195, 889235347:
    470195, 889266673: 470195, 889337361: 470195, 891449886: 470196, 891495976: 470196,
    891514933: 470196, 891534772: 470196, 891558548: 470196, 891652412: 470196, 891664096:
    470196, 894551006: 471157, 901179274: 473098, 916642385: 477850, 920529583: 479202,
    929360825: 482444, 934799128: 484066, 935084855: 484137, 935760710: 484067, 958922607:
    490004, 987138425: 498264, 993243528: 500414, 1003020818: 508158, 1055411789: 548440,
    1105606155: 578140, 1106021493: 579334, 1106038856: 579334, 1106041282: 579334, 1106981144:
    579337, 1109492535: 582439, 1131117370: 596326, 1131157058: 596326, 1131310191: 595001,
    1142136817: 603451, 1143440073: 604728, 1144619518: 604949, 1145326830: 605930, 1145916218:
    605932, 1145946269: 605932, 1146135408: 606634, 1146149834: 606634, 1146326038: 606664,
    1146361502: 606664, 1146396233: 606664, 1146400208: 606664, 1146884157: 606805, 1147429279:
    607073, 1147630597: 607074, 1282762138: 684404, 1418406796: 783430, 1418414756: 783430,
    1418607632: 783435, 1178522854: 627391, 1178551447: 627391, 1190369832: 634112, 1214926276:
    644263, 1214936607: 644263, 1214938127: 644263, 1217536313: 646936, 1252775877: 665565,
    1252789661: 665565, 1253050691: 665566, 1253063496: 665566, 1253070192: 665566, 1256866979:
    667036, 1256868137: 667036, 1256870657: 667036, 1256871845: 667036, 1256874400: 667036,
    1256879449: 667036, 1256896036: 667037, 1256908034: 667037, 1256914332: 667037, 1265665527:
    670841, 1268122683: 673117, 1268128472: 673117, 1291015598: 689739, 1291028780: 689739,
    1291043551: 689739, 1291073802: 689739, 1291108047: 689739, 1298277217: 695525, 1299766868:
    696407, 1407411121: 769450, 1415818471: 780154, 1415828560: 780154, 1415829314: 780154,
    1415833391: 780154, 1415841027: 780154, 1415851986: 780154, 1418593938: 783435, 1176788151:
    626576, 1204616174: 641058, 1204641135: 641058, 1204661949: 641058, 1204760052: 641059,
    1204793225: 641059, 1204830762: 641059, 1204844408: 641059, 1204857494: 641059, 1245848659:
    661648, 1258464606: 668016, 1258469914: 668016, 1258470053: 668016, 1258691177: 668017,
    1258691672: 668017, 1258706126: 668017, 1258767496: 668017, 1263849512: 670420, 1263859724:
    670420, 1263862985: 670420, 1264155288: 670421, 1264169513: 670421, 1264178937: 670421,
    1265465552: 670840, 1292226393: 691516, 1292228465: 691516, 1302032290: 697390, 1308442147:
    701492, 1316274680: 708512, 1316274718: 708512, 1316276295: 708512, 1336340778: 720303,
    1383393561: 750124, 1383398341: 750124, 1407403875: 769450, 1413456102: 776495, 1413461866:
    776495, 1413469715: 776495, 1413473290: 776495, 1416299136: 780726, 1417686911: 780814,
    1417689405: 780814, 1417704132: 780814, 1417708347: 780814, 1418604993: 783435, 637358051:
    348727, 643536919: 355016, 676768413: 381886, 682135792: 383086, 691433482: 386651,
    694212444: 387150, 709436266: 395303, 714462113: 398013, 714485370: 398013, 714755043:
    397651, 715140522: 398004, 723983069: 403931, 738783662: 409269, 739680146: 407235,
    739829029: 407479, 741255530: 409347, 741270123: 409347, 742954364: 409679, 742960975:
    409679, 743458081: 409684, 743458377: 409684, 744222514: 410166, 744405042: 410166,
    757205480: 415022, 757252810: 415022, 758058197: 415421, 760316107: 417327, 760949922:
    416938, 760965714: 417331, 760988294: 417331, 761820997: 417711, 761826348: 417711,
    764922700: 419291, 780471774: 425128, 799776604: 432548, 800276204: 433542, 802404053:
    433542, 803561499: 434336, 807349990: 435637, 809694067: 434588, 828707565: 445711,
    841185744: 451336, 850993746: 455018, 854359267: 456104, 854418891: 456104, 855221359:
    456105, 855255407: 456105, 855255710: 456105, 855357345: 456104, 855414991: 451115,
    855431538: 451115, 855489548: 451115, 855791035: 456107, 855798106: 456107, 855835289:
    456107, 855835410: 456107, 855962521: 451117, 857264868: 456109, 857326083: 456109,
    858029990: 451119, 858105502: 451119, 858252803: 453077, 858268431: 453077, 858312027:
    453077, 858937670: 460304, 858958151: 460304, 859050969: 456110, 859068129: 456110,
    859640396: 460308, 861740206: 460309, 861765347: 460309, 899739078: 472422, 913898432:
    477022, 913924619: 477022, 917536372: 479903, 921993647: 480220, 922832877: 480221,
    922877472: 480221, 925444752: 481162, 940018318: 485419, 940756541: 485420, 941829567:
    485421, 942744962: 485430, 942857102: 485430, 942932431: 485430, 945093559: 485432,
    945121810: 485432, 992000431: 499188, 992252579: 499189, 992253295: 499189, 992256615:
    499189, 992257502: 499189, 992260209: 499189, 992421687: 499190, 992825872: 499191,
    1176802876: 626576, 1211221283: 643483, 1211633264: 643484, 1211644229: 643484, 1211659267:
    643484, 1308434065: 701492, 1418395609: 783430
}


def measures(r):
    """One row per file: session, subject and the cell's measures under every reading (fres, Q,
    f3dB, Zmax and Z0 per chirp reading; sag, input resistance and Vm per reading), with the
    sweeps dropped and why."""
    d = dict(path=r["path"], subject=r["subject"].get("subject_id"), session_id=r["session_id"],
             nwb_age=r["subject"].get("age"), nwb_sex=r["subject"].get("sex"),
             nwb_species=r["subject"].get("species"), nwb_genotype=r["subject"].get("genotype"),
             has_chirp=any("CHIRP" in s["stimulus"] for s in r["sweeps"]))
    c = r["cell"]
    if c is None:
        return d
    d.update(c["drop"])
    d["n_chirp"] = len(c["chirps"])
    if c["chirps"]:
        for rd in FREQ_RANGES:
            f, amp, sm_ = impedance(c["chirps"], rd)
            d.update({f"{k}_{rd}": v for k, v in resonance(f, sm_).items()})
        d["vm_a"] = float(np.mean([x["vm"] for x in c["chirps"]]))
        d["chirp_start"] = c["chirps"][0]["start"]
        d["chirp_end"] = c["chirps"][0]["end"]
        d["chirp_i_peak"] = float(np.mean([x["i_peak"] for x in c["chirps"]]))
        d["chirp_v_pp"] = float(np.mean([np.ptp(x["v"]) for x in c["chirps"]]))
    d.update(sag_rin(c["ls"]))
    d["ls_amps"] = sorted({round(s["amp"]) for s in c["ls"]})
    d["ls_deflect_ok"] = int(sum(s["v_min"] < s["v_base"] for s in c["ls"]))
    d["ls_n"] = len(c["ls"])
    return d


# Patch-seq expression of the human cells, from the analysis repositories (outside inputs, pinned).
# The Chartrand et al. matrix (datPS) holds CPM; the Lee, Dalley et al. matrices (datPatch1 and
# datPatch2) hold log2(CPM + 1), as their column sums show (checked in the notebook). The .RData
# files are read into memory with the rdata package; nothing is written to disk.
CHARTRAND_EXPR = f"{CHARTRAND_REPO}/{CHARTRAND_COMMIT}/data/ps_human.RData"
LEE_EXPR = [("https://raw.githubusercontent.com/AllenInstitute/human_patchseq_gaba/"
             f"5eb357a1cea246c7c847b5608a8fc7e87ea95b58/data/complete_patchseq_data_sets{k}.RData") for k in (1, 2)]


def _read_rdata(url):
    import warnings
    import rdata
    with urllib.request.urlopen(url) as r:
        raw = r.read()
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        return rdata.conversion.convert(rdata.parser.parse_data(raw))


def expression(genes):
    """CPM of `genes` per cell, indexed by specimen id, for the Chartrand et al. and the Lee,
    Dalley et al. cells, with each matrix's column sums of CPM (all genes) as a check of scale."""
    import pandas as pd
    out, sums = [], {}
    c = _read_rdata(CHARTRAND_EXPR)
    d, a = c["datPS"], c["annoPS"]
    g = list(d.coords[d.dims[0]].values)
    spec = dict(zip(a["sample_id"].astype(str), a["spec_id_label"].astype(str)))
    cols = [spec.get(str(s)) for s in d.coords[d.dims[1]].values]
    v = d.values
    sums["chartrand"] = v.sum(axis=0)
    out.append(pd.DataFrame(v[[g.index(x) for x in genes]].T, index=cols, columns=genes).assign(expr_source="chartrand"))
    mats = [_read_rdata(u) for u in LEE_EXPR]
    anno = mats[1]["annoPatch"]
    spec = dict(zip(anno["sample_id"].astype(str), anno["spec_id_label"].astype(str)))
    for k, m in zip((1, 2), mats):
        d = m[f"datPatch{k}"]
        g = list(d.coords[d.dims[0]].values)
        cpm = 2.0 ** d.values - 1.0
        sums[f"lee{k}"] = cpm.sum(axis=0)
        cols = [spec.get(str(s)) for s in d.coords[d.dims[1]].values]
        out.append(pd.DataFrame(cpm[[g.index(x) for x in genes]].T, index=cols, columns=genes).assign(expr_source=f"lee{k}"))
    e = pd.concat(out)
    e.index.name = "spec_id"
    return e, sums
