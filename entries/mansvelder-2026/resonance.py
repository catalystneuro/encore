"""Loading and resonance measures for dandiset 000630 (Chartrand et al. 2023, human L1 Patch-seq).

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


def list_assets():
    """All assets of the pinned version: path, asset id and size."""
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=1000"
    out = []
    while url:
        with urllib.request.urlopen(url) as r:
            page = json.load(r)
        out += [dict(path=a["path"], asset_id=a["asset_id"], size=a["size"]) for a in page["results"]]
        url = page["next"]
    return out


def version_metadata():
    with urllib.request.urlopen(f"{API}/dandisets/{DANDISET}/versions/{VERSION}/") as r:
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


def process_file(asset):
    """Open one file once: its subject, session id and sweep stimulus names, and, for a cell
    with chirp sweeps, the reduced chirp and long-square data (load_cell)."""
    with open_asset(asset["asset_id"]) as f:
        subj, session, sweeps = _subject_and_sweeps(f)
        cell = None
        if any("CHIRP" in s["stimulus"] for s in sweeps):
            cell = _load(f, sweeps)
    return dict(path=asset["path"], asset_id=asset["asset_id"], subject=subj, session_id=session,
                sweeps=sweeps, cell=cell)


def process_files(assets, workers=8):
    """process_file over all assets in parallel processes. Streaming is I/O bound, but h5py
    holds a global lock, so threads would read one file at a time."""
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(process_file, assets, chunksize=1))


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
                                           ls_truncated=0))
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


def impedance(chirps, reading="a"):
    """Smoothed impedance profile of the averaged chirp sweeps (MOhm against Hz)."""
    n = min(len(c["v"]) for c in chirps)    # sweeps can differ by a sample
    v = np.mean([c["v"][:n] for c in chirps], axis=0)
    i = np.mean([c["i"][:n] for c in chirps], axis=0)
    z = np.fft.rfft(v) / np.fft.rfft(i)
    freq = np.fft.rfftfreq(len(v), d=1.0 / DOWN_RATE)
    lo, hi = FREQ_RANGES[reading]
    keep = (freq >= lo) & (freq < hi)
    amp = np.abs(z[keep]) * 1e3        # mV / pA = GOhm, so x1000 for MOhm
    f = freq[keep]
    smooth = lowess(amp, f, frac=LOWESS_FRAC, return_sorted=False)
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
