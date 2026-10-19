"""Loading and measures for dandiset 000005 (Yu, Gutnisky, Hires & Svoboda 2016).

Yu J, Gutnisky DA, Hires SA, Svoboda K (2016). Layer 4 fast-spiking interneurons filter
thalamocortical signals during active somatosensation. Nat Neurosci 19:1647-1657,
doi:10.1038/nn.4412.

The dandiset holds two kinds of file, one session each:

- `behavior+ecephys`: silicon probe recordings in VPM, a few sorted units per file (spike
  times at 1 ms resolution), with whisker angle, curvature, touch onsets and offsets and pole
  availability at 1 kHz for the principal whisker and its neighbours.
- `behavior+icephys(+ogen)`: one L4 neuron per file, recorded whole-cell or juxtacellularly,
  as a 10 kHz `CurrentClampSeries` (5.5 s per trial), with whisker angle and touches at 1 kHz
  (5 s per trial) and, in most files, one or two photostimulation series at 10 kHz.

Files are streamed from the archive at the pinned version; nothing is written to disk. Each
file is reduced on loading to spike times, the whisker variables of the principal whisker,
touch times and light epochs.

The paper's full text is not open access and no analysis code is linked by the paper or the
dandiset. Its supplementary figure legends and tables are public; they fix a few things (the
spike-phase fit and its r2 > 0.25 cut-off, the opsins, the cell counts per mouse line) but give no
windows or thresholds, so every parameter below is a common choice made here, not the paper's:

- Spikes. Whole-cell recordings (median Vm below -20 mV): peaks with a prominence of at least
  `WC_PROMINENCE_MV` and a maximum rate of rise of at least `WC_MIN_DVDT` in the 1 ms before
  the peak. Juxtacellular recordings: the trace high-passed at `JX_HIGHPASS_HZ`, its polarity
  taken from the larger tail, and peaks above `JX_THRESHOLD_SD` robust standard deviations.
  Detection is limited to the first `ANALYSIS_END_S` of each trial, the span of the whisker
  video and before the step in the trace near 5.1 s.
- Spike width: the full width at half maximum of the mean spike of the raw trace (polarity
  corrected, baseline from 1.5 to 0.5 ms before the peak), interpolated to 100 kHz.
- Whisking: the angle band-passed at `WHISK_BAND_HZ` and its Hilbert amplitude and phase.
  Whisking where the amplitude is at least `WHISK_AMP_DEG`, quiet where it is below
  `QUIET_AMP_DEG`. Samples within `TOUCH_GUARD_S` of any touch of any tracked whisker, or
  between a touch onset and its offset, are left out of the whisking and quiet measures.
- Touch response: spike rate in the `TOUCH_WIN_S` after each touch onset of the principal
  whisker minus that in the same span before it.
- Whisking modulation: the amplitude (Hz) of the first harmonic of spike rate against whisking
  phase during non-touch whisking, the rate in each phase bin being spikes over time spent there,
  minus the median of a null made by moving the spikes to other trials; modulated when the
  observed amplitude exceeds the null with p < `ALPHA_CELL` (see `phase_modulation`). The
  Rayleigh test of spike phases (`rayleigh_p`) and 2 x vector strength x rate
  (`whisk_mod_raw_vs_hz`) are kept as the first, uncorrected version: phase occupancy is not
  uniform, so the Rayleigh test finds modulation in spikes moved to the wrong trial. The r2 of a
  single sinusoid fitted to rate against phase (`whisk_r2`) is the paper's measure; the paper
  counts a cell as phase-modulated when r2 > 0.25 (Supp. Fig. 2e), which is shown as a variant.
- Touch-evoked membrane potential (whole-cell only, `vm_touch_response`): the trace 5 to 30 ms
  after each touch onset minus 10 to 0 ms before it, after a 3 ms running median.
"""

from __future__ import annotations

import hashlib
import threading
import multiprocessing
from concurrent.futures import ProcessPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
import requests
from dandi.dandiapi import DandiAPIClient
from scipy import signal, stats

DANDISET_ID = "000005"
DANDISET_VERSION = "0.220126.1853"

VM_HZ = 10_000             # most files; files from late August 2015 on are at 20 kHz
WHISK_HZ = 1_000
ANALYSIS_END_S = 5.0
WC_PROMINENCE_MV = 20.0
WC_MIN_DVDT = 10.0          # mV/ms
JX_HIGHPASS_HZ = 300.0
JX_THRESHOLD_SD = 6.0
REFRACTORY_S = 0.001
WHISK_BAND_HZ = (6.0, 30.0)
WHISK_AMP_DEG = 2.5
QUIET_AMP_DEG = 1.0
TOUCH_GUARD_S = 0.1
TOUCH_WIN_S = 0.025
LIGHT_PULSE_WIN_S = (0.0, 0.006)   # spikes counted after the onset of a 5 ms light pulse
TAG_MIN_PULSES = 10
TAG_MIN_DIFF = 0.2                  # evoked minus baseline spike probability
TAG_MAX_P = 0.001
EXC_MIN_FWHM_MS = 0.6               # whole-cell action potentials at least this wide
MIN_SPIKES = 20                     # spikes in the trials a measure uses
MIN_TOUCHES = 10
ALPHA_CELL = 0.01
PHASE_BINS = 12
MAX_TRIAL_SHIFTS = 99               # shifts of 1 to 99 trials, each at 4 offsets within the trial


def _str(x):
    v = x[()]
    if isinstance(v, bytes):
        return v.decode()
    if isinstance(v, np.ndarray):
        return [i.decode() if isinstance(i, bytes) else str(i) for i in v.ravel()]
    return v


def assets():
    """Path, download URL and size of every asset of the pinned version."""
    client = DandiAPIClient()
    ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
    out = []
    for a in ds.get_assets():
        out.append({"path": a.path, "size": a.size,
                    "url": a.get_content_url(follow_redirects=1, strip_query=True)})
    return sorted(out, key=lambda a: a["path"])


def versions_check():
    """The published versions of the dandiset, and whether the draft holds the same asset paths and
    sizes as the pinned version."""
    client = DandiAPIClient()
    published = [v.identifier for v in client.get_dandiset(DANDISET_ID).get_versions() if v.identifier != "draft"]
    pinned = {(a.path, a.size) for a in client.get_dandiset(DANDISET_ID, DANDISET_VERSION).get_assets()}
    draft = {(a.path, a.size) for a in client.get_dandiset(DANDISET_ID, "draft").get_assets()}
    return {"published": published, "pinned_assets": len(pinned), "draft_assets": len(draft),
            "draft_same_paths_and_sizes": pinned == draft}


_session = threading.local()


def _open(url):
    f = h5py.File(remfile.File(url), "r")
    f.url = url
    return f


def read(f, name):
    """Read a whole dataset. The datasets of this dandiset are contiguous and uncompressed, so
    their bytes are fetched with one HTTP range request, which is much faster than reading
    through h5py; other layouts are read through h5py."""
    d = f[name]
    off = d.id.get_offset()
    if off is None or d.chunks is not None or d.dtype.kind not in "biuf" or d.size == 0:
        return d[:]
    nbytes = d.size * d.dtype.itemsize
    if not hasattr(_session, "s"):
        _session.s = requests.Session()
    for attempt in range(4):
        try:
            r = _session.s.get(f.url, headers={"Range": f"bytes={off}-{off + nbytes - 1}"}, timeout=120)
            r.raise_for_status()
            if len(r.content) == nbytes:
                return np.frombuffer(r.content, dtype=d.dtype).reshape(d.shape)
        except requests.RequestException:
            if attempt == 3:
                raise
    raise IOError(f"incomplete read of {name}")


def _trials(f):
    t = f["intervals/trials"]
    df = pd.DataFrame({"start": t["start_time"][:], "stop": t["stop_time"][:]})
    for col in ["type", "response", "photo_stim_mode"]:
        df[col] = [v.decode() if isinstance(v, bytes) else str(v) for v in t[col][:]]
    for col in ["stim_present", "pole_in_time", "pole_out_time", "first_touch_time",
                "first_lick_time", "pole_position"]:
        df[col] = t[col][:]
    df["photo_stim_power"] = [float(v) if not isinstance(v, bytes) and v is not None else np.nan
                              for v in t["photo_stim_power"][:]]
    return df


def _whiskers(f):
    """Angle and touch series of every tracked whisker; the principal one is flagged."""
    out = {}
    for name in f["acquisition"]:
        g = f["acquisition"][name]
        if "whisker_angle" not in g:
            continue
        w = {"principal": name.lower().startswith("principal"),
             "name": name.split("_")[-1].upper(),
             "t": read(f, f"acquisition/{name}/whisker_angle/timestamps"),
             "angle": read(f, f"acquisition/{name}/whisker_angle/data").astype(float),
             "touch_on": np.flatnonzero(read(f, f"acquisition/{name}/touch_onset/data")),
             "touch_off": np.flatnonzero(read(f, f"acquisition/{name}/touch_offset/data"))}
        out[name] = w
    return out


def per_trial_index(t, trials):
    """Trial number of each timestamp (-1 when outside every trial)."""
    i = np.searchsorted(trials["start"].to_numpy(), t, side="right") - 1
    ok = (i >= 0) & (t < trials["stop"].to_numpy()[np.clip(i, 0, None)])
    return np.where(ok, i, -1)


def whisking_variables(angle, t, trials):
    """Band-passed amplitude and phase, computed trial by trial (trials are not contiguous)."""
    b, a = signal.butter(2, np.array(WHISK_BAND_HZ) / (WHISK_HZ / 2), btype="band")
    amp = np.full(angle.shape, np.nan)
    phase = np.full(angle.shape, np.nan)
    tri = per_trial_index(t, trials)
    for k in np.unique(tri[tri >= 0]):
        idx = np.flatnonzero(tri == k)
        x = angle[idx]
        good = np.isfinite(x)
        if good.sum() < 200:
            continue
        x = np.interp(np.arange(len(x)), np.flatnonzero(good), x[good])
        y = signal.filtfilt(b, a, x - x.mean())
        h = signal.hilbert(y)
        amp[idx] = np.abs(h)
        phase[idx] = np.angle(h)
        amp[idx[~good]] = np.nan
    return amp, phase, tri


def touch_mask(n, whiskers, guard_samples):
    """True for samples during a touch, or within the guard of a touch onset or offset."""
    m = np.zeros(n, bool)
    for w in whiskers.values():
        on, off = w["touch_on"], w["touch_off"]
        for i in on:
            j = off[off >= i]
            end = j[0] if len(j) else i
            m[max(0, i - guard_samples): min(n, end + guard_samples + 1)] = True
        for j in off:
            m[max(0, j - guard_samples): min(n, j + guard_samples + 1)] = True
    return m


# --------------------------------------------------------------------------- spikes

def detect_spikes_whole_cell(v, fs=VM_HZ):
    """Indices of action potential peaks in a whole-cell trace (mV)."""
    dv = np.gradient(v) * fs / 1000.0          # mV/ms
    peaks, _ = signal.find_peaks(v, prominence=WC_PROMINENCE_MV, distance=int(REFRACTORY_S * fs))
    n1 = int(0.001 * fs)
    keep = [p for p in peaks if p >= n1 and dv[p - n1:p + 1].max() >= WC_MIN_DVDT]
    return np.array(keep, int)


def detect_spikes_juxta(v, fs=VM_HZ):
    """Indices of spikes in a juxtacellular trace, and the polarity used (+1 or -1)."""
    b, a = signal.butter(3, JX_HIGHPASS_HZ / (fs / 2), btype="high")
    hp = signal.filtfilt(b, a, v - np.median(v))
    hi, lo = np.percentile(hp, [99.99, 0.01])
    pol = 1 if abs(hi) >= abs(lo) else -1
    x = pol * hp
    sd = np.median(np.abs(x - np.median(x))) / 0.6745
    peaks, _ = signal.find_peaks(x, height=JX_THRESHOLD_SD * sd, distance=int(REFRACTORY_S * fs))
    return peaks, pol


def spike_fwhm_ms(wave, pre, fs=VM_HZ):
    """Full width at half maximum (ms) of a mean spike whose peak is at sample `pre`."""
    w = np.asarray(wave, float) - np.mean(wave[: max(pre - int(0.0005 * fs), 1)])
    up = 10
    fine = np.interp(np.arange((len(w) - 1) * up + 1) / up, np.arange(len(w)), w)
    ipk = pre * up
    half = fine[ipk] / 2
    if half <= 0:
        return np.nan
    left = ipk
    while left > 0 and fine[left] > half:
        left -= 1
    right = ipk
    while right < len(fine) - 1 and fine[right] > half:
        right += 1
    return (right - left) / up / fs * 1000.0


def peak_to_trough_ms(wave, pre, fs=VM_HZ):
    """Time (ms) from the peak of a mean spike to the lowest point in the 2 ms after it."""
    w = np.asarray(wave, float)
    seg = w[pre:pre + int(0.002 * fs) + 1]
    return float(np.argmin(seg) / fs * 1000.0)


# --------------------------------------------------------------------------- loaders

def _light_epochs(f, trials):
    """Per site, the light-on intervals (s) within each trial, from the photostimulation series."""
    out = {}
    pres = f["stimulus/presentation"]
    for name in pres:
        if not name.startswith("photostimulation"):
            continue
        d = read(f, f"stimulus/presentation/{name}/data")
        on = np.flatnonzero(d > 0)
        if len(on) == 0:
            out[name] = {"power_max": 0.0, "pulses": np.zeros((0, 2))}
            continue
        ts = read(f, f"stimulus/presentation/{name}/timestamps")
        brk = np.flatnonzero(np.diff(on) > 1)
        starts = np.r_[on[0], on[brk + 1]]
        stops = np.r_[on[brk], on[-1]]
        t0, t1 = ts[starts], ts[stops]
        out[name] = {"power_max": float(d[on].max()), "pulses": np.c_[t0, t1 + np.median(np.diff(ts[:1000]))]}
    return out


def _site_info(f):
    info = {}
    g = f.get("general/optogenetics")
    if g is None:
        return info
    for name in g:
        s = g[name]
        loc = _str(s["location"]) if "location" in s else ""
        region = loc.split(";")[0].replace("brain_region:", "").strip()
        info[name.replace("site_ ", "photostimulation_site_ ")] = {
            "region": region, "lambda_nm": float(s["excitation_lambda"][()])}
    return info


def load_icephys(asset):
    """One L4 cell, reduced to what the analysis needs."""
    f = _open(asset["url"])
    trials = _trials(f)
    vd = f["acquisition/CurrentClampSeries/data"]
    conv = float(vd.attrs["conversion"])
    v = read(f, "acquisition/CurrentClampSeries/data").astype(float)   # stored values, mV
    vt = read(f, "acquisition/CurrentClampSeries/timestamps")
    whiskers = _whiskers(f)
    rec = {
        "path": asset["path"], "kind": "L4",
        "subject": _str(f["general/subject/subject_id"]),
        "genotype": _str(f["general/subject/genotype"]),
        "session_description": _str(f["session_description"]),
        "label_mode": "whole-cell" if "whole-cell, acute" in _str(f["session_description"]) else "juxtacellular",
        "vm_conversion": conv, "vm_unit": vd.attrs["unit"],
        "trials": trials, "sites": _site_info(f), "light": _light_epochs(f, trials),
        "n_vm": len(v), "vm_hash": hashlib.sha1(v.tobytes()).hexdigest()[:12],
        "vm_head": v[:100_000].astype(np.float32),
    }
    # timestamps: per-trial blocks at 10 kHz starting at the trial start
    tri = per_trial_index(vt, trials)
    rec["vm_outside_trials"] = int((tri < 0).sum())
    rel = vt - trials["start"].to_numpy()[np.clip(tri, 0, None)]
    k = np.r_[0, np.flatnonzero(np.diff(tri) != 0) + 1]
    rec["vm_block_first_rel"] = float(np.abs(rel[k]).max())
    dt = np.diff(vt)
    rec["vm_dt_within"] = float(np.median(dt))
    fs = float(round(1.0 / rec["vm_dt_within"]))
    rec["vm_hz"] = fs
    rec["vm_dt_irregular"] = int((np.abs(dt - 1 / fs) > 1e-6).sum() - (len(k) - 1))
    rec["vm_trial_s"] = float(np.median(np.bincount(tri[tri >= 0])) / fs)
    rec["vm_median"] = float(np.median(v))
    rec["vm_range"] = (float(np.percentile(v, 0.01)), float(np.percentile(v, 99.99)))
    mode = "whole-cell" if rec["vm_median"] < -20 else "juxtacellular"
    rec["mode"] = mode
    keep = (tri >= 0) & (rel < ANALYSIS_END_S)
    spikes, fwhm, waves, pols = [], [], [], []
    for kk in np.unique(tri[keep]):
        idx = np.flatnonzero((tri == kk) & keep)
        x = v[idx]
        if mode == "whole-cell":
            p = detect_spikes_whole_cell(x, fs)
            pol = 1
        else:
            p, pol = detect_spikes_juxta(x, fs)
        spikes.append(vt[idx[p]])
        pols.append((pol, len(p)))
        waves.append((x, p, pol))
    rec["spikes"] = np.concatenate(spikes) if spikes else np.zeros(0)
    pol_counts = {}
    for pol, n in pols:
        pol_counts[pol] = pol_counts.get(pol, 0) + n
    rec["polarity"] = max(pol_counts, key=pol_counts.get) if pol_counts else 1
    pre, post = int(0.0015 * fs), int(0.003 * fs)
    allw = []
    for x, p, pol in waves:
        if pol != rec["polarity"]:
            continue
        p = p[(p >= pre) & (p < len(x) - post)]
        allw += [pol * x[q - pre:q + post] for q in p]
    if len(allw) >= 5:
        rec["mean_wave"] = np.mean(allw, axis=0)
        rec["fwhm_ms"] = spike_fwhm_ms(rec["mean_wave"], pre, fs)
        rec["peak_trough_ms"] = peak_to_trough_ms(rec["mean_wave"], pre, fs)
    else:
        rec["fwhm_ms"], rec["peak_trough_ms"], rec["mean_wave"] = np.nan, np.nan, None
    rec["whiskers"] = {k_: _reduce_whisker(w, trials) for k_, w in whiskers.items()}
    rec["principal"] = next((k_ for k_, w in whiskers.items() if w["principal"]), None)
    if mode == "whole-cell" and rec["principal"] is not None:
        w = whiskers[rec["principal"]]
        lit = light_trials(rec)
        on_t = w["t"][w["touch_on"]]
        on_t = on_t[~lit[np.clip(per_trial_index(on_t, trials), 0, None)] & (per_trial_index(on_t, trials) >= 0)]
        rec.update(vm_touch_response(v, vt, tri, rel, fs, on_t))
    else:
        rec.update(vm_touch_n=0, vm_touch_mv=np.nan, vm_touch_p=np.nan)
    g = f["general"]
    rec["general_fields"] = sorted(g.keys())
    rec["subject_fields"] = sorted(g["subject"].keys())
    # every text value in the file's metadata: the root text fields and every string dataset or
    # attribute under general/ (experiment description, keywords, optogenetics sites and others)
    texts = [_str(f[k]) for k in ("session_description", "experiment_description") if k in f]

    def collect(name, obj):
        if isinstance(obj, h5py.Dataset) and obj.dtype.kind in "OSU":
            texts.append(_str(obj))
        texts.extend(str(a.decode() if isinstance(a, bytes) else a) for a in obj.attrs.values()
                     if isinstance(a, (str, bytes)))
    g.visititems(collect)
    rec["metadata_text"] = " ".join(" ".join(t) if isinstance(t, list) else str(t) for t in texts)
    rec["ic_location"] = next((_str(g["intracellular_ephys"][k]["location"]) for k in g["intracellular_ephys"]
                               if "location" in g["intracellular_ephys"][k]), "")
    return rec


def vm_touch_response(v, vt, tri, rel, fs, touch_times):
    """Touch-evoked change of membrane potential in a whole-cell trace: for each touch onset, the
    mean of the trace 5 to 30 ms after it minus that 10 to 0 ms before it, after a 3 ms running
    median that removes spikes; a one-sided Wilcoxon signed-rank test over touches. Used only to
    tell cells (and mice) with a touch input from those without, as after ION transection."""
    from scipy.ndimage import median_filter
    pre, post = int(0.010 * fs), int(0.030 * fs)
    a0 = int(0.005 * fs)
    d = []
    for t in touch_times:
        i = int(np.searchsorted(vt, t))
        if i - pre < 0 or i + post >= len(v) or tri[i - pre] != tri[i] or tri[i + post] != tri[i] or rel[i + post] >= ANALYSIS_END_S:
            continue
        seg = median_filter(v[i - pre:i + post], size=int(0.003 * fs) | 1, mode="nearest")
        d.append(seg[pre + a0:].mean() - seg[:pre].mean())
    d = np.array(d)
    if len(d) < 5:
        return {"vm_touch_n": int(len(d)), "vm_touch_mv": np.nan, "vm_touch_p": np.nan}
    return {"vm_touch_n": int(len(d)), "vm_touch_mv": float(np.median(d)),
            "vm_touch_p": float(stats.wilcoxon(d, alternative="greater").pvalue)}


def _reduce_whisker(w, trials):
    """Whisking variables for the principal whisker; touches only for the others."""
    out = {"name": w["name"], "principal": w["principal"], "touch_on": w["touch_on"], "touch_off": w["touch_off"],
           "n": len(w["t"])}
    if w["principal"]:
        amp, phase, tri = whisking_variables(w["angle"], w["t"], trials)
        out.update(t=w["t"], amp=amp.astype(np.float32), phase=phase.astype(np.float32), trial=tri.astype(np.int32),
                   angle_range=(float(np.nanmin(w["angle"])), float(np.nanmax(w["angle"]))),
                   angle_nan=float(np.isnan(w["angle"]).mean()),
                   dt_median=float(np.median(np.diff(w["t"]))))
    return out


def load_vpm(asset):
    """One VPM session: every sorted unit, reduced to spike times."""
    f = _open(asset["url"])
    trials = _trials(f)
    u = f["units"]
    st = read(f, "units/spike_times")
    idx = u["spike_times_index"][:]
    starts = np.r_[0, idx[:-1]]
    units = []
    for i, (a, b) in enumerate(zip(starts, idx)):
        units.append({"unit": i, "desc": _str(u["cell_desc"])[i], "spikes": st[a:b],
                      "obs": u["obs_intervals"][:][i] if len(u["obs_intervals"].shape) == 2 else None})
    whiskers = _whiskers(f)
    rec = {"path": asset["path"], "kind": "VPM", "subject": _str(f["general/subject/subject_id"]),
           "genotype": _str(f["general/subject/genotype"]), "trials": trials, "units": units,
           "unit_sampling_rate": _str(u["sampling_rate"]),
           "location": [f["general/extracellular_ephys"][k].attrs.get("location", "")
                        for k in f["general/extracellular_ephys"] if k != "electrodes"],
           "whiskers": {k_: _reduce_whisker(w, trials) for k_, w in whiskers.items()},
           "principal": next((k_ for k_, w in whiskers.items() if w["principal"]), None)}
    return rec


def load_one(a):
    return load_vpm(a) if "ecephys" in a["path"] else load_icephys(a)


def load_all(kind=None, workers=12):
    """Load every file (or those of one kind: 'ecephys' or 'icephys') in parallel processes."""
    al = [a for a in assets() if kind is None or kind in a["path"]]
    with ProcessPoolExecutor(workers, mp_context=multiprocessing.get_context("fork")) as ex:
        return list(ex.map(load_one, al))


# --------------------------------------------------------------------------- measures

def spikes_to_samples(spikes, t):
    """Index of the whisker sample at or before each spike (whisker clock is 1 kHz)."""
    i = np.searchsorted(t, spikes, side="right") - 1
    ok = (i >= 0) & (np.abs(t[np.clip(i, 0, None)] - spikes) < 1.5 / WHISK_HZ)
    return i[ok]


def phase_modulation(spike_idx, phase, whisk, tri, rel_window_used=False):
    """Whisking modulation corrected for phase occupancy, with a trial-shift null.

    spike_idx: whisker-sample index of each spike in the used samples away from touch (the pool
    the null draws from; only those in whisking samples count); phase, whisk, tri: per
    sample phase, whisking mask (already restricted to the used samples) and trial number. The
    rate in each of PHASE_BINS phase bins is spikes over time spent in the bin; the amplitude (Hz)
    is that of the first harmonic of rate against phase. The null moves every spike to the trial
    1 to MAX_TRIAL_SHIFTS places later (wrapping over the used trials) and, unless a time window
    restricts the samples, also by a quarter, a half and three quarters of the trial; the p value
    is (1 + null amplitudes >= observed) / (1 + null count), and the corrected amplitude is the
    observed minus the median null, floored at 0.
    """
    used = np.unique(tri[whisk])
    if len(used) < 2 or len(spike_idx) == 0:
        return {"whisk_amp_raw_hz": np.nan, "whisk_null_median_hz": np.nan, "whisk_mod_hz": np.nan,
                "whisk_p": np.nan, "n_null": 0, "whisk_r2": np.nan}
    ks, first, cnt = np.unique(tri, return_index=True, return_counts=True)
    pos = np.searchsorted(ks, used)
    starts, lengths = first[pos], cnt[pos]
    L = int(lengths.min())
    edges = np.linspace(-np.pi, np.pi, PHASE_BINS + 1)
    b = np.clip(np.digitize(phase, edges) - 1, 0, PHASE_BINS - 1)
    M = np.full((len(used), L), -1, int)
    for r, (s0, n) in enumerate(zip(starts, lengths)):
        seg = slice(s0, s0 + L)
        M[r] = np.where(whisk[seg], b[seg], -1)
    occ = np.bincount(M[M >= 0], minlength=PHASE_BINS) / WHISK_HZ
    centers = (edges[:-1] + edges[1:]) / 2
    # spikes as (row, offset) within the used trials
    st = tri[spike_idx]
    keep = np.isin(st, used)
    rows = np.searchsorted(used, st[keep])
    offs = spike_idx[keep] - starts[rows]
    ok = offs < L
    rows, offs = rows[ok], offs[ok]

    def rate_of(r, o):
        bb = M[r, o]
        c = np.bincount(bb[bb >= 0], minlength=PHASE_BINS)
        return np.where(occ > 0, c / np.where(occ > 0, occ, 1), 0.0)

    def amp(r, o):
        return 2 * np.abs(np.mean(rate_of(r, o) * np.exp(1j * centers)))

    obs = amp(rows, offs)
    # Goodness of fit of a single sinusoid to rate against phase (the paper's measure, Supp.
    # Figs. 2e, 7g): with equally spaced bins the fitted sinusoid holds PHASE_BINS * A**2 / 2
    # of the sum of squares about the mean, A being the first-harmonic amplitude.
    rate = rate_of(rows, offs)
    ss = np.sum((rate - rate.mean()) ** 2)
    r2 = float(PHASE_BINS * obs ** 2 / 2 / ss) if ss > 0 else np.nan
    n = len(used)
    offsets = [0] if rel_window_used else [0, L // 4, L // 2, 3 * L // 4]
    null = []
    for d in offsets:
        for k in range(0, min(n - 1, MAX_TRIAL_SHIFTS) + 1):
            if k == 0 and d == 0:
                continue
            null.append(amp((rows + k) % n, (offs + d) % L))
    null = np.array(null)
    if len(null) == 0:
        return {"whisk_amp_raw_hz": obs, "whisk_null_median_hz": np.nan, "whisk_mod_hz": np.nan,
                "whisk_p": np.nan, "n_null": 0, "whisk_r2": r2}
    return {"whisk_amp_raw_hz": float(obs), "whisk_r2": r2, "whisk_null_median_hz": float(np.median(null)),
            "whisk_mod_hz": float(max(obs - np.median(null), 0.0)),
            "whisk_p": float((1 + np.sum(null >= obs)) / (1 + len(null))), "n_null": int(len(null))}


def response_measures(spikes, rec, trial_mask=None, time_window=None, isolated_touch_s=0.0):
    """Touch response, whisking modulation and rates for one cell.

    trial_mask: boolean per trial, the trials to use. time_window: per-trial (start, stop) in
    seconds after the trial start, the part of each trial to use (for light epochs).
    isolated_touch_s: when above 0, only touch onsets of the principal whisker with no other
    onset in the preceding span enter the touch response (a variant; the pre-touch window can
    otherwise hold the response to the previous touch of a bout). Touch windows that cross a
    trial boundary are left out.
    """
    w = rec["whiskers"][rec["principal"]]
    t, amp, phase, tri = w["t"], w["amp"], w["phase"], w["trial"]
    n = len(t)
    use = tri >= 0
    if trial_mask is not None:
        use &= np.asarray(trial_mask)[np.clip(tri, 0, None)] & (tri >= 0)
    if time_window is not None:
        rel = t - rec["trials"]["start"].to_numpy()[np.clip(tri, 0, None)]
        lo = np.asarray([tw[0] for tw in time_window])[np.clip(tri, 0, None)]
        hi = np.asarray([tw[1] for tw in time_window])[np.clip(tri, 0, None)]
        use &= (rel >= lo) & (rel < hi)
    guard = int(TOUCH_GUARD_S * WHISK_HZ)
    tmask = touch_mask(n, rec["whiskers"], guard)
    whisk = use & ~tmask & (amp >= WHISK_AMP_DEG)
    quiet = use & ~tmask & (amp < QUIET_AMP_DEG)
    si = spikes_to_samples(spikes, t)
    si = si[use[si]]
    count = np.bincount(si, minlength=n)
    out = {"n_spikes": int(len(si)), "rate": count[use].sum() / max(use.sum(), 1) * WHISK_HZ,
           "whisk_s": whisk.sum() / WHISK_HZ, "quiet_s": quiet.sum() / WHISK_HZ}
    out["rate_whisk"] = count[whisk].sum() / out["whisk_s"] if out["whisk_s"] > 0 else np.nan
    out["rate_quiet"] = count[quiet].sum() / out["quiet_s"] if out["quiet_s"] > 0 else np.nan
    ph = np.repeat(phase[whisk], count[whisk])
    out["n_whisk_spikes"] = len(ph)
    if len(ph) >= 1:
        z = np.mean(np.exp(1j * ph))
        out["vector_strength"] = float(np.abs(z))
        out["preferred_phase"] = float(np.angle(z))
        n_ph = len(ph)
        R = n_ph * np.abs(z)
        out["rayleigh_p"] = float(np.exp(np.sqrt(1 + 4 * n_ph + 4 * (n_ph ** 2 - R ** 2)) - (1 + 2 * n_ph)))
        out["whisk_mod_raw_vs_hz"] = 2 * out["vector_strength"] * out["rate_whisk"]
    else:
        out.update(vector_strength=np.nan, preferred_phase=np.nan, rayleigh_p=np.nan, whisk_mod_raw_vs_hz=np.nan)
    si_all = np.repeat(np.arange(n), count)
    pool = si_all[(use & ~tmask)[si_all]]          # spikes away from touch, moved by the null
    out.update(phase_modulation(pool, phase, whisk, tri, rel_window_used=time_window is not None))
    # touch response: principal whisker touch onsets inside the used samples
    on = w["touch_on"]
    on = on[use[on]]
    win = int(TOUCH_WIN_S * WHISK_HZ)
    if isolated_touch_s > 0:
        prev = np.r_[np.inf, np.diff(w["touch_on"])][np.searchsorted(w["touch_on"], on)]
        on = on[prev > isolated_touch_s * WHISK_HZ]
    on = on[(on >= win) & (on < n - win)]
    on = on[(tri[on - win] == tri[on]) & (tri[on + win - 1] == tri[on])]   # windows inside the trial
    cs = np.r_[0, np.cumsum(count)]
    post = cs[on + win] - cs[on]
    pre = cs[on] - cs[on - win]
    out["n_touches"] = int(len(on))
    out["touch_spikes_post"], out["touch_spikes_pre"] = int(post.sum()), int(pre.sum())
    out["touch_post_hz"] = post.mean() / TOUCH_WIN_S if len(on) else np.nan
    out["touch_pre_hz"] = pre.mean() / TOUCH_WIN_S if len(on) else np.nan
    out["touch_resp_hz"] = out["touch_post_hz"] - out["touch_pre_hz"] if len(on) else np.nan
    if len(on) >= 5 and np.any(post != pre):
        out["touch_p"] = float(stats.wilcoxon(post, pre, alternative="greater").pvalue)
    else:
        out["touch_p"] = np.nan
    tr = max(out["touch_resp_hz"], 0) if np.isfinite(out["touch_resp_hz"]) else np.nan
    wm = out["whisk_mod_hz"]
    out["touch_selectivity"] = tr / (tr + wm) if np.isfinite(tr) and np.isfinite(wm) and (tr + wm) > 0 else np.nan
    wr = out["whisk_mod_raw_vs_hz"]
    out["touch_selectivity_raw"] = tr / (tr + wr) if np.isfinite(tr) and np.isfinite(wr) and (tr + wr) > 0 else np.nan
    return out


def isolated_pulses(rec, site, max_dur=0.0075, gap=0.1):
    """Onsets of short light pulses at a site with no other pulse within `gap` seconds: the
    single 5 ms pulses, as opposed to the pulses of a train."""
    pulses = rec["light"].get(site, {}).get("pulses", np.zeros((0, 2)))
    if len(pulses) == 0:
        return np.zeros(0)
    on = pulses[:, 0]
    dur = pulses[:, 1] - pulses[:, 0]
    prev = np.r_[np.inf, np.diff(on)]
    nxt = np.r_[np.diff(on), np.inf]
    return on[(dur < max_dur) & (prev > gap) & (nxt > gap)]


def light_pulse_response(rec, site):
    """Spike probability in LIGHT_PULSE_WIN_S after each isolated light pulse at a site, the
    same 50 ms before it, a one-sided McNemar-type binomial test, and the median latency of
    the first spike within 20 ms."""
    on = isolated_pulses(rec, site)
    if len(on) == 0:
        return {"n_pulses": 0}
    sp = np.sort(rec["spikes"])
    a, b = LIGHT_PULSE_WIN_S

    def any_spike(t0, t1):
        return (np.searchsorted(sp, t1) - np.searchsorted(sp, t0)) > 0

    ev = np.array([any_spike(p + a, p + b) for p in on])
    base = np.array([any_spike(p - 0.05 + a, p - 0.05 + b) for p in on])
    n10, n01 = int((ev & ~base).sum()), int((~ev & base).sum())
    p = stats.binomtest(n10, n10 + n01, 0.5, alternative="greater").pvalue if n10 + n01 > 0 else 1.0
    lat = []
    for t in on:
        j = np.searchsorted(sp, t)
        if j < len(sp) and sp[j] - t < 0.02:
            lat.append(sp[j] - t)
    return {"n_pulses": int(len(on)), "p_evoked": float(ev.mean()), "p_base": float(base.mean()),
            "p_value": float(p), "median_latency_ms": float(np.median(lat) * 1000) if lat else np.nan}


def light_windows(rec, site, gap=0.1):
    """Per trial, the span (s after the trial start) from the first to the last light sample of
    a site, for trials with any light there; pulse trains count as one span."""
    pulses = rec["light"].get(site, {}).get("pulses", np.zeros((0, 2)))
    tr = rec["trials"]
    if len(pulses) == 0:
        return pd.DataFrame(columns=["trial", "rel_start", "rel_stop", "n_pulses"])
    k = per_trial_index(pulses[:, 0], tr)
    rows = []
    for t in np.unique(k[k >= 0]):
        p = pulses[k == t]
        s0 = tr["start"].iloc[t]
        rows.append({"trial": int(t), "rel_start": p[:, 0].min() - s0, "rel_stop": p[:, 1].max() - s0,
                     "n_pulses": len(p)})
    return pd.DataFrame(rows)


def window_rate(rec, trial_mask, rel_window):
    """Spike rate (Hz) inside the span `rel_window` (s after the trial start) of the trials in
    `trial_mask`, and the number of spikes counted."""
    sp = np.sort(rec["spikes"])
    lo, hi = rel_window
    starts = rec["trials"]["start"].to_numpy()[np.asarray(trial_mask)]
    n = sum(int(np.searchsorted(sp, s + hi) - np.searchsorted(sp, s + lo)) for s in starts)
    return (n / (len(starts) * (hi - lo)) if len(starts) else np.nan), n


def light_trials(rec):
    """Boolean per trial: any light at any site."""
    lit = np.zeros(len(rec["trials"]), bool)
    for site in rec["light"]:
        w = light_windows(rec, site)
        lit[w["trial"].to_numpy(int)] = True
    return lit


def shift_spikes(spikes, trials, by=1):
    """Each spike moved to the trial `by` places later, at the same time after the trial start
    (spikes in the last trials are dropped). Used as a null for the alignment of spikes to the
    behaviour."""
    starts = trials["start"].to_numpy()
    k = per_trial_index(spikes, trials)
    ok = (k >= 0) & (k + by < len(starts))
    return spikes[ok] - starts[k[ok]] + starts[k[ok] + by]


# --------------------------------------------------------------------------- the paper's supplement

SUPPLEMENT_URL = ("https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fnn.4412/"
                  "MediaObjects/41593_2016_BFnn4412_MOESM61_ESM.pdf")
# Mouse line IDs of Supplementary Table 2, named from the JAX stock numbers given there:
# 014548 VGAT-ChR2-EYFP, 017320 PV-IRES-Cre, 012569 Ai32, 012355 PV-ChR2, 013044 SOM-IRES-Cre.
LINES = {1: "VGAT-ChR2-EYFP", 2: "PV-IRES-Cre", 3: "PV-IRES-Cre x Ai32", 4: "C57BL/6", 5: "PV-ChR2",
         6: "SOM-IRES-Cre x Ai32"}


def supplement_mouse_lines():
    """The mouse line of each mouse, read from Supplementary Table 1 of the paper (the PDF
    supplement on the publisher's site, part of doi:10.1038/nn.4412)."""
    import io
    import re
    import pypdf
    r = requests.get(SUPPLEMENT_URL, timeout=120)
    r.raise_for_status()
    text = "\n".join(p.extract_text() or "" for p in pypdf.PdfReader(io.BytesIO(r.content)).pages)
    rows = re.findall(r"^(\d{6}) (\d) ", text, re.M)
    if len(rows) == 0:
        raise ValueError("Supplementary Table 1 not found in the supplement")
    return pd.DataFrame({"subject": ["anm" + a for a, _ in rows], "line": [LINES[int(b)] for _, b in rows]})
