"""Loading and measures for dandiset 001791 (Wong-Campos et al., dendritic voltage imaging in vivo).

Paper: Wong-Campos, Park, Davis, Qi, Fan, Marblestone, Grimm, Lavis, Cohen et al., "Voltage
dynamics of dendritic integration and back-propagation in vivo", bioRxiv preprint,
doi:10.1101/2023.05.25.542363 (version 1 is the text the claims were written from).

The dandiset holds the traces of the authors' analysis pipeline (PCA-extracted, per branch),
grouped by figure, some summary tables, and HiLo z-stacks. Every file is deposited twice, under a
figure name at the top level and under a `sub-*` folder, as byte-identical copies (same SHA-256).
`FILES` names the copy read here and `DUPLICATES` its twin. Files are streamed from the archive at
the pinned version with remfile and h5py and read with pynwb; nothing is written to disk.

Where the parameters come from:

- Sampling rate: 500 Hz for every trace file (the files' `rate` and descriptions), except
  recordings 14 and 15 of the Fig. 4e-h file, which are at 1,000 Hz (their `rate` and
  descriptions); the Methods give 500 or 1,000 Hz. The measures below take `fs` for those two.
- Spike detection: peaks of the high-pass filtered soma trace above K robust standard deviations
  (1.4826 times the median absolute deviation), with K = 5 and K = 4 as the two readings of the
  claims' criterion (fig1d-light-intensity-spike-rate); the paper gives no detection method. The
  high-pass filter (2nd-order Butterworth, 10 Hz, zero phase) and the minimum peak separation
  (2 frames, 4 ms) are standard choices that the paper does not fix; the separation is below the
  shortest doublet intervals the paper shows (18 +/- 7 ms).
- bAP amplitude: the peak of the dendritic trace within 0 to 5 ms (reading 2: 0 to 8 ms) after
  the somatic spike peak minus the mean of the 5 ms before the first spike of the event (the
  claims' criterion, fig4bc-doublet-first-fails). At 500 Hz, 0 to 5 ms is frames 0 to 2 after the
  spike frame and 0 to 8 ms frames 0 to 4; the 5 ms baseline is the 2 frames before.
- Peak timing below one frame: the sample of the maximum, or a parabola through the maximum and
  its two neighbours (the two readings of the criterion of fig2f-delay-range).
- Accelerating and decelerating trios at 75 ms: Fig. 4d legend.
- Distal dendrites have a conduction delay above 3 ms: Methods, "Analysis of bAP failures during
  optogenetic stimulation".
- Normalization of optogenetic bAP amplitudes by their mean 200 to 400 ms after stimulus onset:
  the same Methods section.
"""

import functools
import json
import urllib.request

import h5py
import numpy as np
import pynwb
import remfile
from scipy import signal

DANDISET_ID = "001791"
DANDISET_VERSION = "0.260424.0313"
FS = 500.0  # Hz, every trace file except recordings 14 and 15 of the Fig. 4e-h file (1,000 Hz)
API = "https://api.dandiarchive.org/api"

# The copy read, by its role, and the identical twin deposited under another path.
FILES = {
    "fig1": "Figure1_barrel500_2_20220711.nwb",
    "fig2_amplitude": "figure2f_bAP_propagation_amplitude.nwb",
    "fig2_delay": "figure2g_bAP_propagation_delay.nwb",
    "fig2_soma_dendrite_corr": "figure2h_soma_dendrite_correlation.nwb",
    "fig2_dendrite_dendrite_corr": "figure2j_dendrite_dendrite_correlation.nwb",
    "fig3_corr_vs_distance": "figure3d_voltage_correlation.nwb",
    "fig3_neuron_anesthetized": "barrel1_20220711_anesthetized_20220711_1p0iso.nwb",
    "fig3_neuron_awake": "barrel1_20220711_awake_20220711.nwb",
    "fig3_traces": "figure3i_zscore_traces.nwb",
    "fig3e": "figure3e_IUEMouse2_20220711.nwb",
    "fig4_spontaneous": "figure4ad_history_dependent_bAP.nwb",
    "fig4_optogenetic": "figure4eh_optogenetic_bAP.nwb",
    "fig4_sensory": "figure4il_sensory_evoked_bAP.nwb",
}
DUPLICATES = {
    "Figure1_barrel500_2_20220711.nwb": "sub-Barrel500-2/sub-barrel500-2_ses-20220711_ophys.nwb",
    "figure2f_bAP_propagation_amplitude.nwb":
        "sub-pooled-12neurons-12mice/sub-pooled-12neurons-12mice_ses-20220614_obj-bcvsl0.nwb",
    "figure2g_bAP_propagation_delay.nwb":
        "sub-pooled-12neurons-12mice/sub-pooled-12neurons-12mice_ses-20220614_obj-24h46s.nwb",
    "figure2h_soma_dendrite_correlation.nwb":
        "sub-pooled-12neurons-12mice/sub-pooled-12neurons-12mice_ses-20220614_obj-ejkwtm.nwb",
    "figure2j_dendrite_dendrite_correlation.nwb":
        "sub-pooled-9neurons-9mice/sub-pooled-9neurons-9mice_ses-20220614.nwb",
    "figure3d_voltage_correlation.nwb": "sub-pooled-7neurons-7mice/sub-pooled-7neurons-7mice_ses-20220504.nwb",
    "barrel1_20220711_anesthetized_20220711_1p0iso.nwb":
        "sub-barrel1-20220711-anesthetized/sub-barrel1-20220711-anesthetized_ses-20220711_ophys.nwb",
    "barrel1_20220711_awake_20220711.nwb":
        "sub-barrel1-20220711-awake/sub-barrel1-20220711-awake_ses-20220711_ophys.nwb",
    "figure3i_zscore_traces.nwb": "sub-pooled-multiple-mice/sub-pooled-multiple-mice_ses-20221014.nwb",
    "figure3e_IUEMouse2_20220711.nwb": "sub-IUEMouse2/sub-IUEMouse2_ses-20220711_ophys.nwb",
    "figure4ad_history_dependent_bAP.nwb": "sub-pooled-5neurons-5mice/sub-pooled-5neurons-5mice_ses-20221012.nwb",
    "figure4eh_optogenetic_bAP.nwb": "sub-pooled-neurons/sub-pooled-neurons_ses-20221012.nwb",
    "figure4il_sensory_evoked_bAP.nwb": "sub-Barrel500-1/sub-Barrel500-1_ses-20221107.nwb",
}


def _get_json(url):
    with urllib.request.urlopen(url) as r:
        return json.loads(r.read())


@functools.lru_cache(maxsize=None)
def assets():
    """Every asset of the pinned version: path -> dict(asset_id, size, sha256)."""
    out, url = {}, f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/?page_size=200"
    while url:
        page = _get_json(url)
        for a in page["results"]:
            out[a["path"]] = {"asset_id": a["asset_id"], "size": a["size"]}
        url = page.get("next")
    return out


def asset_metadata(path):
    a = assets()[path]
    return _get_json(f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/{a['asset_id']}/")


def version_metadata():
    return _get_json(f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/")


def s3_url(path):
    a = assets()[path]
    meta = asset_metadata(path)
    for u in meta.get("contentUrl", []):
        if "s3" in u and "amazonaws" in u:
            return u
    return f"{API}/assets/{a['asset_id']}/download/"


_OPEN = {}


def open_nwb(path):
    """Stream one NWB file and return the pynwb NWBFile (kept open for the session)."""
    if path not in _OPEN:
        h5 = h5py.File(remfile.File(s3_url(path)), "r")
        io = pynwb.NWBHDF5IO(file=h5, mode="r", load_namespaces=True)
        _OPEN[path] = (io, io.read(), h5)
    return _OPEN[path][1]


def open_h5(path):
    open_nwb(path)
    return _OPEN[path][2]


# ---------------------------------------------------------------- signal measures

def robust_sd(x):
    x = np.asarray(x, float)
    return 1.4826 * np.median(np.abs(x - np.median(x)))


def highpass(x, fc=10.0, fs=FS, order=2):
    """Zero-phase Butterworth high-pass (standard choice; the paper gives no filter)."""
    b, a = signal.butter(order, fc / (fs / 2), btype="high")
    return signal.filtfilt(b, a, np.asarray(x, float), axis=0)


def detect_spikes(trace, k, fc=10.0, min_sep_ms=4.0, fs=FS):
    """Frame indices of peaks of the high-pass filtered trace above k robust s.d."""
    hp = highpass(trace, fc, fs)
    thr = k * robust_sd(hp)
    idx, _ = signal.find_peaks(hp, height=thr, distance=max(1, frames(min_sep_ms, fs)))
    return idx


def peak_time(w, i, parabolic):
    """Time (frames) of the maximum of w at index i, optionally refined by a parabola."""
    if not parabolic or i <= 0 or i >= len(w) - 1:
        return float(i)
    y0, y1, y2 = w[i - 1], w[i], w[i + 1]
    den = y0 - 2 * y1 + y2
    if den == 0:
        return float(i)
    return i + 0.5 * (y0 - y2) / den


def sta(trace, idx, pre, post):
    """Average of trace[i-pre : i+post+1] over the indices that fit; returns (mean, n)."""
    trace = np.asarray(trace, float)
    keep = [i for i in idx if i - pre >= 0 and i + post < len(trace)]
    if not keep:
        return None, 0
    seg = np.stack([trace[i - pre:i + post + 1] for i in keep])
    return seg.mean(0), len(keep)


def sta_delay_ms(soma, dend, idx, parabolic, half_window_ms=10.0, fs=FS):
    """Peak delay of the dendritic STA after the somatic STA peak (ms), both triggered off idx.

    Peaks are searched within +/- half_window_ms (10 ms) of the trigger frame.
    """
    pre = post = frames(40, fs)
    half_window = frames(half_window_ms, fs)
    ws, n = sta(soma, idx, pre, post)
    wd, _ = sta(dend, idx, pre, post)
    if ws is None:
        return np.nan, 0
    lo, hi = pre - half_window, pre + half_window + 1
    i_s = lo + int(np.argmax(ws[lo:hi]))
    i_d = lo + int(np.argmax(wd[lo:hi]))
    return (peak_time(wd, i_d, parabolic) - peak_time(ws, i_s, parabolic)) * 1000.0 / fs, n


def frames(ms, fs=FS):
    return int(round(ms * fs / 1000.0))


def bap_amplitude(trace, spike, base_spike, win_ms, fs=FS):
    """Peak of trace within 0..win_ms after `spike` minus the mean of the 5 ms before `base_spike`.

    At 500 Hz, round(2.5) gives 2 frames for the 5 ms baseline (4 ms) and frames 0 to 2 for the
    0 to 5 ms window; at 1,000 Hz 5 frames and frames 0 to 5.
    """
    w = frames(win_ms, fs)
    b = frames(5, fs)
    if base_spike - b < 0 or spike + w >= len(trace):
        return np.nan
    return float(np.max(trace[spike:spike + w + 1]) - np.mean(trace[base_spike - b:base_spike]))


def wilcoxon(x, y=None):
    """Two-sided Wilcoxon signed-rank p-value (nan when there are fewer than 2 non-zero values)."""
    from scipy import stats
    x = np.asarray(x, float)
    d = x if y is None else x - np.asarray(y, float)
    d = d[np.isfinite(d)]
    if np.count_nonzero(d) < 2:
        return np.nan
    return float(stats.wilcoxon(d).pvalue)


# ---------------------------------------------------------------- loaders

def series(nwb_obj):
    """data, and timestamps when present, of a pynwb TimeSeries."""
    d = np.asarray(nwb_obj.data[:])
    t = None if nwb_obj.timestamps is None else np.asarray(nwb_obj.timestamps[:])
    return d, t


def load_fig1():
    nwb = open_nwb(FILES["fig1"])
    rrs = nwb.processing["ophys"]["Fluorescence"]["z_score_traces"]
    return {"data": np.asarray(rrs.data[:]), "rate": rrs.rate, "description": rrs.description,
            "unit": rrs.unit, "session": nwb.session_description, "subject": nwb.subject.subject_id}


def load_fig2():
    """bAP amplitude and delay against contour distance, as deposited."""
    out = {}
    for role in ("fig2_amplitude", "fig2_delay"):
        mod = open_nwb(FILES[role]).processing["figure2_bAP_propagation"]
        for name in mod.data_interfaces:
            ts = mod[name]
            d, t = series(ts)
            out[(role, name)] = {"data": d, "x": t, "unit": ts.unit, "description": ts.description}
    return out


def load_zscore_file(role):
    nwb = open_nwb(FILES[role])
    rrs = nwb.processing["ophys"]["Fluorescence"]["z_score_traces"]
    return {"data": np.asarray(rrs.data[:]), "description": rrs.description,
            "session": nwb.session_description, "subject": nwb.subject.subject_id}


def load_fig3_traces():
    nwb = open_nwb(FILES["fig3_traces"])
    out = []
    for name in sorted(nwb.acquisition):
        ts = nwb.acquisition[name]
        parts = name.split("_")
        out.append({"name": name, "state": parts[1], "mouse": parts[2],
                    "data": np.asarray(ts.data[:]), "description": ts.description, "rate": ts.rate})
    return out


def load_fig3_corr():
    mod = open_nwb(FILES["fig3_corr_vs_distance"]).processing["figure3d"]
    out = {}
    for name in mod.data_interfaces:
        d, t = series(mod[name])
        out[name] = {"corr": d, "distance": t, "description": mod[name].description}
    return out


def load_fig4_spontaneous():
    nwb = open_nwb(FILES["fig4_spontaneous"])
    mod = nwb.processing["figure4_analysis"]
    recs = []
    for i in range(1, 100):
        key = f"rec{i:02d}"
        if f"{key}_deltaF" not in nwb.acquisition:
            break
        ts = nwb.acquisition[f"{key}_deltaF"]
        st, _ = series(nwb.acquisition[f"{key}_spike_times"])
        amps, amp_t = series(mod[f"{key}_spike_amplitudes"])
        acc, _ = series(mod[f"{key}_accelerating"])
        dec, _ = series(mod[f"{key}_decelerating"])
        mouse = ts.description.split("(mouse ")[1].split(")")[0]
        recs.append({"rec": key, "mouse": mouse, "data": np.asarray(ts.data[:]), "rate": ts.rate,
                     "spike_times": st.astype(float), "spike_amplitudes": amps,
                     "accelerating": acc, "decelerating": dec, "description": ts.description})
    extra = {}
    for name in ("soma_dendrite_distances", "summary_accelerating", "summary_decelerating",
                 "STA_dendrites", "STA_soma"):
        extra[name] = {"data": np.asarray(mod[name].data[:]), "description": mod[name].description}
    return recs, extra


def load_fig4_optogenetic():
    nwb = open_nwb(FILES["fig4_optogenetic"])
    mod = nwb.processing["figure4eh_analysis"]
    recs = []
    for i in range(1, 100):
        key = f"rec{i:02d}"
        if f"{key}_deltaF" not in nwb.acquisition:
            break
        ts = nwb.acquisition[f"{key}_deltaF"]
        stim, _ = series(nwb.acquisition[f"{key}_stim_times"])
        desc = nwb.acquisition[f"{key}_stim_times"].description
        stim_len = int(desc.split("Stimulus length: ")[1].split(" frames")[0])
        recs.append({"rec": key, "data": np.asarray(ts.data[:]), "rate": ts.rate,
                     "stim_times": stim.astype(float), "stim_frames": stim_len,
                     "delay_deposited": np.asarray(mod[f"{key}_delay"].data[:]),
                     "allAmps": np.asarray(mod[f"{key}_allAmps"].data[:]),
                     "staCount": np.asarray(mod[f"{key}_staCount"].data[:]),
                     "description": ts.description})
    return recs


def load_fig4_sensory():
    nwb = open_nwb(FILES["fig4_sensory"])
    recs = []
    for i in range(1, 100):
        key = f"rec{i:02d}"
        if f"{key}_deltaF" not in nwb.acquisition:
            break
        ts = nwb.acquisition[f"{key}_deltaF"]
        st, _ = series(nwb.acquisition[f"{key}_spike_times"])
        on, _ = series(nwb.acquisition[f"{key}_stim_onsets"])
        aotf = np.asarray(nwb.stimulus[f"{key}_AOTF_stimulus"].data[:])
        recs.append({"rec": key, "data": np.asarray(ts.data[:]), "rate": ts.rate,
                     "spike_times": st.astype(float), "stim_onsets": on.astype(float), "aotf": aotf,
                     "description": ts.description})
    return recs


# ---------------------------------------------------------------- event selections

def isi_ms(spikes):
    return np.diff(np.asarray(spikes)) * 1000.0 / FS


def doublet_starts(spikes, reading, limit_ms=75.0):
    """Indices i of doublets (spikes i, i+1) under the two readings of fig4a-doublet-isi.

    (a) ISI below 75 ms (the triplet threshold of the Fig. 4d legend), preceded and followed by
    ISIs above 75 ms (the first and last spikes of a recording count as isolated on that side);
    (b) any consecutive pair with ISI below 75 ms.
    """
    isi = isi_ms(spikes)
    out = []
    for i in range(len(isi)):
        if isi[i] >= limit_ms:
            continue
        if reading == "b":
            out.append(i)
            continue
        pre = isi[i - 1] if i > 0 else np.inf
        post = isi[i + 1] if i + 1 < len(isi) else np.inf
        if pre > limit_ms and post > limit_ms:
            out.append(i)
    return out


def trios(spikes, limit_ms=75.0):
    """Reference (third) spike indices n of accelerating and decelerating trios (Fig. 4d legend).

    ISI_n-1 is the interval between spikes n-2 and n-1, ISI_n between n-1 and n.
    Accelerating: ISI_n-1 > 75 ms and ISI_n < 75 ms; decelerating: the reverse.
    """
    isi = isi_ms(spikes)
    acc = [n for n in range(2, len(spikes)) if isi[n - 2] > limit_ms and isi[n - 1] < limit_ms]
    dec = [n for n in range(2, len(spikes)) if isi[n - 2] < limit_ms and isi[n - 1] > limit_ms]
    return acc, dec


def infer_pulses(trace, on_ms=500, periods_ms=(1000,), smooth_ms=50):
    """Onsets (frames) of a train of light pulses inferred from the light-evoked depolarization.

    The Fig. 1 file has no stimulus record. The paper gives the pulse length (0.5 s); the phase
    (and the period, when more than one is given) is found here as the square wave (on for on_ms)
    whose on-minus-off contrast of the smoothed trace is largest. The default period of 1 s is
    read from the trace (its steps recur every 1.0 s; the notebook prints them). This is an
    assumption: the pulses are taken to be periodic.
    """
    from scipy import ndimage
    slow = ndimage.uniform_filter1d(np.asarray(trace, float), frames(smooth_ms))
    t = np.arange(len(slow)) * 1000.0 / FS
    best = None
    for per in periods_ms:
        for ph in np.arange(0, per, 2):
            on = ((t - ph) % per) < on_ms
            c = slow[on].mean() - slow[~on].mean()
            if best is None or c > best[0]:
                best = (c, per, ph)
    c, per, ph = best
    onsets = np.arange(ph, t[-1] + 1, per)
    return [frames(o) for o in onsets], {"contrast": c, "period_ms": per, "phase_ms": ph}


def pair_correlation(x, y, measure, max_lag_frames=5, exclude=None):
    """Correlation of two traces: 'zero' (Pearson at zero lag) or 'peak' (largest normalized
    cross-correlation within +/- max_lag_frames, 10 ms at 500 Hz). `exclude` is a boolean mask of
    frames left out (spike removal reading)."""
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    if exclude is not None:
        keep = ~exclude
        x, y = x[keep], y[keep]
    if measure == "zero":
        return float(np.corrcoef(x, y)[0, 1])
    a = (x - x.mean()) / x.std()
    b = (y - y.mean()) / y.std()
    n = len(a)
    vals = []
    for lag in range(-max_lag_frames, max_lag_frames + 1):
        if lag >= 0:
            vals.append(np.mean(a[:n - lag] * b[lag:]))
        else:
            vals.append(np.mean(a[-lag:] * b[:n + lag]))
    return float(max(vals))


def align_to_peak(trace, idx, half=2):
    """Move each frame index to the maximum of trace within +/- half frames (2 frames, 4 ms).

    Used for the deposited Fig. 4a-d spike times, which sit one frame after the soma's peak
    (the notebook shows it); the claims' bAP windows are measured from the somatic spike peak.
    """
    trace = np.asarray(trace, float)
    out = []
    for i in np.asarray(idx, int):
        lo, hi = max(0, i - half), min(len(trace), i + half + 1)
        out.append(lo + int(np.argmax(trace[lo:hi])))
    return np.unique(np.array(out, int))
