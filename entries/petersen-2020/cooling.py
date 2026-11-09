"""Loading and measures for dandiset 000059 (Petersen & Buzsaki 2020, Neuron 106:1-14).

The dandiset holds 50 behavioural sessions from five rats (MS10, MS12, MS13, MS21, MS22) running
a spatial alternation task on a figure-8 ("theta") maze while the medial septum (MS) was cooled.
Each session has two files: a processed file (trials with the cooling state and choice errors,
position, speed and MS temperature, and spike-sorted units in 24 sessions) and a raw file
(wide-band data at 20 kHz and LFP at 1250 Hz).

Every file is streamed from the archive at a pinned version. `load_session` reads a processed
file; `theta_for_session` streams one LFP channel over the behavioural period only; and
`waveforms` streams short windows of the wide-band data to measure spike waveforms.

Where parameters come from:

- Theta: LFP of the electrode flagged `theta_reference`, third-order Butterworth band-pass 4 to
  10 Hz applied forward and backward, Hilbert phase (the paper's Methods). The instantaneous
  frequency is one over the interval between successive upward zero crossings of the phase,
  values above 11 Hz removed, smoothed with a 7-point Gaussian (SD 1 point); theta power and
  peak frequency come from a 1 s Hamming-window spectrogram stepped by 0.1 s over 4 to 10 Hz
  (0.1 Hz steps), median filtered over 2 frequencies by 10 time steps and averaged over a 10 by
  10 box, as in the paper's code (calcInstantaneousTheta.m). The code reports the magnitude of
  the spectrogram, so power here is in the same units (uV per bin, not squared).
- Trial theta: the mean over position frames of the trial where the speed is above 30 cm/s
  (the paper's code, BatchProcessing.m).
- Error rates and the onset-aligned trial series (trial 65 is the first cooling trial, 200
  trial positions, errors smoothed with an 11-point Gaussian window of alpha 2.5, theta power
  minus each session's mean): the paper's code (BatchProcessing.m).
- Oscillation frequency of a unit: 1 ms spike raster convolved with an 80-point Gaussian
  window, autocorrelogram, frequency of the highest peak between 50 and 150 ms (the paper's
  Methods and calc_trial_averages.m).
- Place fields: 5 cm bins of the linearized maze (Methods: 3 to 5 cm), frames above 10 cm/s
  (the code's speed_th), rate maps smoothed with a Gaussian of SD 1 bin (a common choice).
  Fields follow the automatic criteria of the Methods for Figure 5: at least 4 contiguous bins
  above 10% of the peak rate, peak above 8 Hz and spatial coherence above 0.6.
- Cross-correlograms of place cell pairs: 1 ms bins smoothed with a 60-bin Gaussian window;
  phase cross-correlograms on the unwrapped theta phase in bins of 0.01 pi, smoothed with a
  60-bin Gaussian window (the Methods).
- Putative cell types: the files hold no cell types. Units are typed here by the
  trough-to-peak time of their mean waveform on the channel of largest amplitude, at the 0.425
  ms threshold CellExplorer uses for narrow interneurons, and by mean rate above 10 Hz for wide
  interneurons (a common choice; CellExplorer's own wide-interneuron rule needs a fit of the
  autocorrelogram that is not repeated here).
"""

from __future__ import annotations

import re
from functools import lru_cache

import h5py
import numpy as np
import pandas as pd
import remfile
from scipy import signal, stats
from scipy.ndimage import gaussian_filter1d, median_filter, uniform_filter

DANDISET_ID = "000059"
DANDISET_VERSION = "0.250624.0444"
LFP_RATE = 1250.0
RAW_RATE = 20000.0

THETA_BAND = (4.0, 10.0)
THETA_MAX_INSTANT = 11.0
TRIAL_THETA_SPEED = 30.0       # cm/s, BatchProcessing.m
MAP_SPEED = 10.0               # cm/s, generateFigures.m (behavior.speed_th)
BIN_CM = 5.0
FIELD_MIN_BINS = 4
FIELD_FRACTION = 0.1
FIELD_PEAK_HZ = 8.0
FIELD_COHERENCE = 0.6
NARROW_TTP_MS = 0.425
WIDE_INT_RATE = 10.0
ALIGN_ONSET = 65               # 1-based trial position of the first cooling trial
ALIGN_LENGTH = 200

# Sessions of the paper's behavioural analysis (BatchProcessing.m, ids 58 to 169), by name.
# Names are the dandiset's session ids with "Peter-" stripped and "-concat" dropped.
CODE_SESSIONS = {
    "MS10": ["170323-173246", "170321-164406", "170320-212321", "170317-153237", "170314-163038",
             "170319-180352", "170313-122631", "170311-180956"],
    "MS12": ["170713-093400", "170714-122034", "170715-111545", "170716-172307", "170717-111614",
             "170718-101720", "170719-095305", "170720-093528", "170723-141121", "170712-101120"],
    "MS13": ["171127-133330", "171128-113924", "171129-105507", "171130-121758", "171201-130527",
             "171206-132039", "171205-110831", "171204-102904"],
    "MS21": ["180621-141817", "180629-110332", "180627-143449", "180622-174411", "180623-170717",
             "180625-153927", "180628-155921", "180711-112927", "180712-103200", "180720-110037",
             "180724-144402", "180730-120605", "180806-111316", "180803-142301", "180802-120147"],
    "MS22": ["180621-131028", "180629-110319", "180628-120341", "180622-115734", "180623-170141",
             "180625-162932", "180626-110916", "180627-114856", "180711-112912", "180712-102504",
             "180720-110055", "180724-144421"],
}
# Sessions of Figure 5 in the paper's code (BatchProcessing.m, second part).
FIG5_SESSIONS = ["MS10-170317-153237", "MS10-170307-154746", "MS12-170714-122034",
                 "MS12-170715-111545", "MS12-170716-172307", "MS12-170717-111614",
                 "MS12-170719-095305", "MS13-171128-113924", "MS13-171129-105507",
                 "MS13-171130-121758", "MS21-180629-110332", "MS21-180627-143449",
                 "MS21-180625-153927", "MS21-180712-103200", "MS21-180628-155921",
                 "MS22-180628-120341", "MS22-180629-110319", "MS22-180711-112912"]
# Sessions the code's recording list marks as without a temperature channel (ch_temp = 0):
# all MS10 sessions and the two control sessions of 2018-07-19, which also have no cooling
# onsets (cooling_session = 0).
CODE_NO_TEMPERATURE = {"MS10"}
CODE_CONTROLS = {"MS21-180719-155941", "MS22-180719-122813"}


# ----------------------------------------------------------------------------- access

def session_key(path: str) -> str:
    """'sub-MS10/sub-MS10_ses-Peter-MS10-170307-154746-concat_desc-...' -> 'MS10-170307-154746'."""
    ses = re.search(r"_ses-Peter-(MS\d+-\d{6}-\d{6})", path).group(1)
    return ses


@lru_cache(maxsize=1)
def sessions() -> pd.DataFrame:
    """One row per session: subject, key, and the S3 URLs of its processed and raw files."""
    from dandi.dandiapi import DandiAPIClient
    rows = {}
    with DandiAPIClient() as client:
        ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        for a in ds.get_assets():
            key = session_key(a.path)
            row = rows.setdefault(key, {"key": key, "subject": key.split("-")[0]})
            kind = "processed" if "desc-processed" in a.path else "raw"
            row[kind + "_path"] = a.path
            row[kind + "_size_gb"] = a.size / 1e9
            row[kind + "_url"] = a.get_content_url(follow_redirects=1, strip_query=True)
    out = pd.DataFrame(sorted(rows.values(), key=lambda r: r["key"])).set_index("key")
    out["in_code_list"] = [k.split("-", 1)[1] in CODE_SESSIONS.get(k.split("-")[0], []) for k in out.index]
    out["in_fig5_list"] = [k in FIG5_SESSIONS for k in out.index]
    out["code_control"] = [k in CODE_CONTROLS for k in out.index]
    return out


def open_h5(url: str) -> h5py.File:
    return h5py.File(remfile.File(url), "r")


def series_listing(f: h5py.File) -> list[tuple[str, str]]:
    """Every object of a file with an NWB type ending in 'Series' (or LFP), with its path."""
    out = []

    def visit(name, obj):
        nt = obj.attrs.get("neurodata_type")
        if nt is not None:
            nt = nt.decode() if isinstance(nt, bytes) else str(nt)
            if nt.endswith("Series") or nt == "LFP":
                out.append((name, nt))
    f.visititems(visit)
    return out


def _text(values) -> list[str]:
    return [v.decode() if isinstance(v, bytes) else str(v) for v in values]


def load_session(key: str) -> dict:
    """Read the processed file of one session into plain arrays.

    Units are kept only for phy quality 'good' and 'good2'; counts of every quality are kept.
    """
    url = sessions().loc[key, "processed_url"]
    f = open_h5(url)
    out = {"key": key, "subject": key.split("-")[0]}
    out["subject_meta"] = {k: f["general/subject"][k][()].decode() for k in f["general/subject"].keys()}
    out["session_id"] = f["general/session_id"][()].decode()
    out["series"] = series_listing(f)
    beh = f["processing/behavior"]
    out["t"] = beh["SubjectPosition/SpatialSeries/timestamps"][:]
    pos = beh["SubjectPosition/SpatialSeries/data"][:]
    out["pos_conversion"] = float(beh["SubjectPosition/SpatialSeries/data"].attrs["conversion"])
    out["x"], out["y"], out["z"] = pos[:, 0], pos[:, 1], pos[:, 2]
    out["speed"] = beh["SubjectSpeed/data"][:]
    out["speed_unit"] = beh["SubjectSpeed/data"].attrs["unit"]
    out["temp"] = beh["Temperature/data"][:]
    out["temp_t"] = beh["Temperature/timestamps"][:]
    out["same_clock"] = bool(np.array_equal(out["temp_t"], out["t"])
                             and np.array_equal(beh["SubjectSpeed/timestamps"][:], out["t"]))
    if "intervals/trials" in f:
        tr = f["intervals/trials"]
        df = pd.DataFrame({"start": tr["start_time"][:], "stop": tr["stop_time"][:],
                           "error": tr["error"][:].astype(bool),
                           "condition": _text(tr["condition"][:])})
        df["state"] = _text(tr["cooling state"][:]) if "cooling state" in tr else None
        out["trial_columns"] = [k for k in tr.keys() if not k.endswith("_index")]
    else:
        df = pd.DataFrame(columns=["start", "stop", "error", "condition", "state"])
        out["trial_columns"] = []
    out["trials"] = df
    el = f["general/extracellular_ephys/electrodes"]
    out["n_electrodes"] = len(el["id"])
    out["theta_channel"] = int(np.flatnonzero(el["theta_reference"][:])[0])
    out["electrode_group"] = _text(el["group_name"][:])
    out["unit_quality_counts"] = {}
    out["spikes"], out["unit_ids"] = [], []
    if "units" in f:
        u = f["units"]
        quality = _text(u["quality"][:])
        out["unit_quality_counts"] = pd.Series(quality).value_counts().to_dict()
        index = u["spike_times_index"][:]
        keep = [i for i, q in enumerate(quality) if q in ("good", "good2")]
        if keep:
            times = u["spike_times"]
            ids = u["id"][:]
            for i in keep:
                lo = index[i - 1] if i > 0 else 0
                out["spikes"].append(times[lo:index[i]])
                out["unit_ids"].append(int(ids[i]))
    f.close()
    return out


# ----------------------------------------------------------------------------- theta

def _gauss_kernel(n: int, sd: float) -> np.ndarray:
    x = np.arange(n) - (n - 1) / 2
    k = np.exp(-0.5 * (x / sd) ** 2)
    return k / k.sum()


def gausswin(n: int, alpha: float = 2.5) -> np.ndarray:
    """MATLAB's gausswin(n, alpha)."""
    x = np.arange(n) - (n - 1) / 2
    return np.exp(-0.5 * (alpha * x / ((n - 1) / 2)) ** 2)


def nanconv(x: np.ndarray, k: np.ndarray) -> np.ndarray:
    """Convolution that ignores NaNs and renormalises at edges; NaNs stay NaN."""
    x = np.asarray(x, float)
    ok = np.isfinite(x)
    num = np.convolve(np.where(ok, x, 0.0), k, mode="same")
    den = np.convolve(ok.astype(float), k, mode="same")
    with np.errstate(invalid="ignore", divide="ignore"):
        out = num / den
    out[~ok] = np.nan
    return out


def theta_from_lfp(lfp: np.ndarray, t0: float, rate: float = LFP_RATE) -> dict:
    """Theta phase, instantaneous frequency and spectrogram peak of one LFP trace starting at t0."""
    b, a = signal.butter(3, [THETA_BAND[0] / (rate / 2), THETA_BAND[1] / (rate / 2)], btype="band")
    filt = signal.filtfilt(b, a, lfp.astype(float))
    analytic = signal.hilbert(filt)
    phase = np.angle(analytic)
    up = np.flatnonzero(np.diff((phase > 0).astype(int)) == 1)
    freq = rate / np.diff(up)
    freq[freq > THETA_MAX_INSTANT] = np.nan
    freq = nanconv(freq, _gauss_kernel(7, 1.0))
    cycle_t = t0 + up[1:] / rate
    # spectrogram: 1 s Hamming window, 0.1 s step, magnitude at 4 to 10 Hz in 0.1 Hz steps
    win = int(rate)
    step = int(rate / 10)
    freqs = np.round(np.arange(4.0, 10.0001, 0.1), 1)
    n_frames = (len(filt) - win) // step + 1
    w = np.hamming(win)
    basis = np.exp(-2j * np.pi * np.outer(np.arange(win), freqs) / rate) * w[:, None]
    mags = np.empty((len(freqs), n_frames))
    for lo in range(0, n_frames, 4000):
        hi = min(n_frames, lo + 4000)
        frames = np.lib.stride_tricks.sliding_window_view(filt, win)[lo * step:(hi - 1) * step + 1:step]
        mags[:, lo:hi] = np.abs(frames @ basis).T
    mags = median_filter(mags, size=(2, 10), mode="constant")
    mags = uniform_filter(mags, size=10, mode="constant")
    spec_t = t0 + (np.arange(n_frames) * step + win / 2) / rate
    return {"phase": phase, "phase_unwrapped": np.unwrap(phase), "t0": t0, "rate": rate,
            "cycle_t": cycle_t, "inst_freq": freq, "spec_t": spec_t,
            "peak_freq": freqs[np.argmax(mags, axis=0)], "peak_power": mags.max(axis=0),
            "amplitude_uv": np.abs(analytic)}


def stream_lfp(key: str, channel: int, t0: float, t1: float) -> tuple[np.ndarray, float, dict]:
    """One LFP channel from t0 to t1 (s), in microvolts, with the time of its first sample.

    `channel` is a row of the electrodes table; the LFP column is the one whose entry in the
    LFP's `electrodes` region is that row. Also returns what the raw file holds: its series,
    and the row its own electrodes table flags as theta reference."""
    f = open_h5(sessions().loc[key, "raw_url"])
    region = f["processing/ecephys/LFP/LFP/electrodes"][:]
    cols = np.flatnonzero(region == channel)
    assert len(cols) == 1, (key, channel)
    info = {"lfp_column": int(cols[0]), "region_is_identity": bool(np.array_equal(region, np.arange(len(region)))),
            "raw_theta_rows": np.flatnonzero(f["general/extracellular_ephys/electrodes/theta_reference"][:]).tolist(),
            "raw_series": series_listing(f)}
    channel = int(cols[0])
    ds = f["processing/ecephys/LFP/LFP/data"]
    conv = float(ds.attrs["conversion"])
    start = float(f["processing/ecephys/LFP/LFP/starting_time"][()])
    rate = float(f["processing/ecephys/LFP/LFP/starting_time"].attrs["rate"])
    assert rate == LFP_RATE
    lo = max(0, int((t0 - start) * rate))
    hi = min(ds.shape[0], int((t1 - start) * rate))
    x = ds[lo:hi, channel].astype(float) * conv * 1e6
    f.close()
    return x, start + lo / rate, info


def theta_for_session(s: dict, pad: float = 10.0) -> dict:
    """Theta over the behavioural period (first trial start to last trial stop, with padding)."""
    tr = s["trials"]
    t0, t1 = float(tr.start.min()) - pad, float(tr.stop.max()) + pad
    lfp, start, info = stream_lfp(s["key"], s["theta_channel"], t0, t1)
    th = theta_from_lfp(lfp, start)
    th["lfp_rms_uv"] = float(np.std(lfp))
    th["raw_info"] = info
    return th


def phase_at(th: dict, times: np.ndarray, unwrapped: bool = False) -> np.ndarray:
    idx = np.round((times - th["t0"]) * th["rate"]).astype(int)
    ok = (idx >= 0) & (idx < len(th["phase"]))
    out = np.full(len(times), np.nan)
    src = th["phase_unwrapped"] if unwrapped else th["phase"]
    out[ok] = src[idx[ok]]
    return out


# ----------------------------------------------------------------------------- trials

STATE_CODE = {"Pre-Cooling": 1, "Cooling on": 2, "Post-Cooling": 3, "Cooling off": 4}


def trial_measures(s: dict, th: dict | None = None) -> pd.DataFrame:
    """Per trial: state, error, mean temperature and speed, and theta frequency and power."""
    tr = s["trials"].copy()
    t, speed, temp = s["t"], s["speed"], s["temp"]
    lo = np.searchsorted(t, tr.start.values)
    hi = np.searchsorted(t, tr.stop.values, side="right")
    tr["temperature"] = [np.nanmean(temp[a:b]) if b > a else np.nan for a, b in zip(lo, hi)]
    tr["speed"] = [np.nanmean(speed[a:b]) if b > a else np.nan for a, b in zip(lo, hi)]
    tr["speed_run"] = [np.nanmean(speed[a:b][speed[a:b] > MAP_SPEED]) if (speed[a:b] > MAP_SPEED).any() else np.nan
                       for a, b in zip(lo, hi)]
    if th is not None:
        f_frames = np.interp(t, th["cycle_t"], th["inst_freq"], left=np.nan, right=np.nan)
        p_frames = np.interp(t, th["spec_t"], th["peak_power"], left=np.nan, right=np.nan)
        for suffix, thr in (("", TRIAL_THETA_SPEED), ("_10", MAP_SPEED)):
            fr, pw = [], []
            for a, b in zip(lo, hi):
                sel = np.arange(a, b)[speed[a:b] > thr]
                fr.append(np.nanmean(f_frames[sel]) if len(sel) else np.nan)
                pw.append(np.nanmean(p_frames[sel]) if len(sel) else np.nan)
            tr["theta_freq" + suffix], tr["theta_power" + suffix] = fr, pw
    tr["code"] = tr.state.map(STATE_CODE)
    return tr


def error_rates(tr: pd.DataFrame, off_as: str | None = None) -> dict:
    """Percentage of error trials before, during and after cooling, from the state labels.

    off_as: None leaves 'Cooling off' trials out; 'post' or 'cooling' counts them there.
    """
    state = tr.state.replace({"Cooling off": {"post": "Post-Cooling", "cooling": "Cooling on"}.get(off_as, "Cooling off")})
    out = {}
    for name, label in [("pre", "Pre-Cooling"), ("cooling", "Cooling on"), ("post", "Post-Cooling")]:
        sel = state == label
        out[name] = 100.0 * tr.error[sel].mean() if sel.any() else np.nan
        out["n_" + name] = int(sel.sum())
    return out


def aligned_series(tr: pd.DataFrame, columns=("error", "temperature", "speed", "theta_freq", "theta_power")) -> dict:
    """The code's onset-aligned trial series (BatchProcessing.m): trial ALIGN_ONSET is the
    first cooling trial; the series stops at the last trial before a second cooling block
    (the first 'Cooling on' trial after the first block, whatever state precedes it); errors
    are smoothed with an 11-point Gaussian window."""
    code = tr.code.values
    first = int(np.flatnonzero(code == 2)[0])            # 0-based
    offset = ALIGN_ONSET - 1 - first
    ends = [i for i in range(first, len(code) - 1) if code[i] != 2 and code[i + 1] == 2]
    end = ends[0] + 1 if ends else len(code)             # number of trials kept (MATLAB 1:trial_end)
    out = {}
    for col in columns:
        row = np.full(ALIGN_LENGTH, np.nan)
        vals = tr[col].values[:end].astype(float)
        if col == "error":
            # the code marks errors with index < trial_end
            vals = vals.copy()
            vals[end - 1] = 0.0
        pos = np.arange(end) + offset
        ok = (pos >= 0) & (pos < ALIGN_LENGTH)
        row[pos[ok]] = vals[ok]
        out[col] = row
    out["n_kept"] = end
    out["error_smooth"] = nanconv(out["error"], gausswin(11) / gausswin(11).sum())
    if "theta_power" in out:
        out["theta_power"] = out["theta_power"] - np.nanmean(out["theta_power"])
    return out


def pearson(x, y) -> tuple[float, float, int]:
    x, y = np.asarray(x, float), np.asarray(y, float)
    ok = np.isfinite(x) & np.isfinite(y)
    if ok.sum() < 3:
        return np.nan, np.nan, int(ok.sum())
    r, p = stats.pearsonr(x[ok], y[ok])
    return float(r), float(p), int(ok.sum())


# ----------------------------------------------------------------------------- maze

def fit_circle(x: np.ndarray, y: np.ndarray) -> tuple[float, float, float]:
    """Least-squares circle through points: centre x, centre y, radius."""
    A = np.c_[2 * x, 2 * y, np.ones_like(x)]
    sol, *_ = np.linalg.lstsq(A, x ** 2 + y ** 2, rcond=None)
    cx, cy = sol[0], sol[1]
    return float(cx), float(cy), float(np.sqrt(sol[2] + cx ** 2 + cy ** 2))


def linearize(s: dict) -> dict:
    """Linear position on the figure-8 maze for frames inside trials.

    The central arm (stem) runs from the bottom of the circle to its top; the left and right
    arms are the two halves of the circle. Linear position: stem 0 to L (cm, from the bottom),
    right arm L to L + pi R, left arm L + pi R to L + 2 pi R, each arm measured from the top.
    Frames outside trials get NaN. Which arm a frame is on is taken from its side of the
    stem; frames on the stem are those within 10 cm of the stem's line and above the circle's
    bottom rim (15 cm band).
    """
    x, y, t = s["x"], s["y"], s["t"]
    tr = s["trials"]
    in_trial = np.zeros(len(t), bool)
    lo = np.searchsorted(t, tr.start.values)
    hi = np.searchsorted(t, tr.stop.values, side="right")
    trial_id = np.full(len(t), -1)
    for i, (a, b) in enumerate(zip(lo, hi)):
        in_trial[a:b] = True
        trial_id[a:b] = i
    ok = in_trial & np.isfinite(x) & np.isfinite(y)
    stem_x = float(np.nanmedian(x[ok & (np.abs(y - np.nanmedian(y[ok])) < 20)]))
    arm = ok & (np.abs(x - stem_x) > 30)
    cx, cy, R = fit_circle(x[arm], y[arm])
    bottom, top = cy - R, cy + R
    L = top - bottom
    dist = np.hypot(x - cx, y - cy)
    on_stem = ok & (np.abs(x - stem_x) < 10) & (y > bottom + 15) & (y < top - 5)
    ang = np.arctan2(x - cx, y - cy)                     # 0 at the top, +pi/2 to the right
    lin = np.full(len(t), np.nan)
    lin[on_stem] = y[on_stem] - bottom
    on_arm = ok & ~on_stem & (np.abs(dist - R) < 20)
    right = on_arm & (ang >= 0)
    left = on_arm & (ang < 0)
    lin[right] = L + R * ang[right]
    lin[left] = L + np.pi * R + R * (-ang[left])
    segment = np.full(len(t), -1)
    segment[on_stem], segment[right], segment[left] = 0, 1, 2
    edges = np.arange(0, L + 2 * np.pi * R + BIN_CM, BIN_CM)
    return {"lin": lin, "segment": segment, "trial_id": trial_id, "L": L, "R": R,
            "centre": (cx, cy), "stem_x": stem_x, "edges": edges,
            "seg_bounds": [0.0, L, L + np.pi * R, L + 2 * np.pi * R],
            "frac_linearized": float(np.isfinite(lin[ok]).mean())}


# ----------------------------------------------------------------------------- rate maps

def occupancy_and_counts(t, lin, speed, frame_mask, spikes_list, edges):
    """Occupancy (s) per bin and spike counts per bin for frames in frame_mask above MAP_SPEED."""
    dt = np.median(np.diff(t))
    m = frame_mask & np.isfinite(lin) & (speed > MAP_SPEED)
    occ = np.histogram(lin[m], edges)[0] * dt
    counts = []
    for sp in spikes_list:
        idx = np.searchsorted(t, sp) - 1
        idx = idx[(idx >= 0) & (idx < len(t))]
        idx = idx[m[idx]]
        counts.append(np.histogram(lin[idx], edges)[0])
    return occ, np.array(counts)


def smooth_map(counts, occ, sd_bins: float = 1.0, seg_bins=None):
    """Rate map smoothed with a Gaussian, separately within each maze segment."""
    rate = np.full(counts.shape, np.nan)
    if seg_bins is None:
        seg_bins = [(0, counts.shape[-1])]
    for a, b in seg_bins:
        c = gaussian_filter1d(counts[..., a:b].astype(float), sd_bins, axis=-1, mode="nearest")
        o = gaussian_filter1d(occ[a:b].astype(float), sd_bins, mode="nearest")
        with np.errstate(invalid="ignore", divide="ignore"):
            r = c / o
        r[..., o < 0.05] = np.nan
        rate[..., a:b] = r
    return rate


def spatial_coherence(rate: np.ndarray) -> float:
    """Correlation of each bin's rate with the mean of its two neighbours (1-D coherence)."""
    r = np.asarray(rate, float)
    nb = np.full_like(r, np.nan)
    nb[1:-1] = 0.5 * (r[:-2] + r[2:])
    ok = np.isfinite(r) & np.isfinite(nb)
    if ok.sum() < 5 or np.nanstd(r[ok]) == 0:
        return np.nan
    return float(np.corrcoef(r[ok], nb[ok])[0, 1])


def find_fields(rate: np.ndarray, seg_bins) -> list[tuple[int, int, int]]:
    """Place fields: (first bin, last bin + 1, peak bin), within one segment each."""
    fields = []
    peak_all = np.nanmax(rate) if np.isfinite(rate).any() else 0
    if peak_all <= FIELD_PEAK_HZ:
        return fields
    coh = spatial_coherence(rate)
    if not np.isfinite(coh) or coh <= FIELD_COHERENCE:
        return fields
    above = np.nan_to_num(rate) > FIELD_FRACTION * peak_all
    for a, b in seg_bins:
        seg = above[a:b]
        i = 0
        while i < len(seg):
            if seg[i]:
                j = i
                while j < len(seg) and seg[j]:
                    j += 1
                if j - i >= FIELD_MIN_BINS:
                    pk = a + i + int(np.nanargmax(rate[a + i:a + j]))
                    if rate[pk] > FIELD_PEAK_HZ:
                        fields.append((a + i, a + j, pk))
                i = j
            else:
                i += 1
    return fields


def skaggs_information(rate: np.ndarray, occ: np.ndarray) -> float:
    """Bits per spike, as PlaceCellInfo.m (Information_1)."""
    ok = np.isfinite(rate) & (occ > 0)
    if not ok.any():
        return np.nan
    p = occ[ok] / occ[ok].sum()
    r = rate[ok]
    mean = (p * r).sum()
    if mean <= 0:
        return np.nan
    arg = r / mean
    arg[arg == 0] = 1
    return float((p * arg * np.log2(arg)).sum())


# ----------------------------------------------------------------------------- spike timing

def _gauss_acf_kernel(n: int = 80) -> np.ndarray:
    g = gausswin(n)
    return np.convolve(g, g[::-1])                      # length 2n - 1, centred


def oscillation_frequency(times: np.ndarray, min_spikes: int = 50) -> float:
    """1 / lag of the highest autocorrelogram peak between 50 and 150 ms (Methods).

    Same result as the code (1 ms raster convolved with an 80-point Gaussian window, then its
    autocorrelation), computed from the histogram of spike-time differences convolved with the
    autocorrelation of the window, which avoids building the raster.
    """
    t = np.round(np.sort(np.asarray(times)) * 1000).astype(np.int64)
    if len(t) < min_spikes:
        return np.nan
    k = _gauss_acf_kernel(80)
    half = len(k) // 2
    max_lag = 150 + half + 2
    lo = np.searchsorted(t, t - max_lag)
    hi = np.searchsorted(t, t + max_lag, side="right")
    diffs = np.concatenate([t[l:h] - x for x, l, h in zip(t, lo, hi)])
    hist = np.bincount(diffs + max_lag, minlength=2 * max_lag + 1).astype(float)
    ac = np.convolve(hist, k, mode="same")[max_lag:]   # lags 0 .. max_lag
    seg = ac[50:151]
    peaks, _ = signal.find_peaks(seg)
    if len(peaks) == 0:
        return np.nan
    best = peaks[np.argmax(seg[peaks])]
    return 1000.0 / (best + 50)


def ccg(a: np.ndarray, b: np.ndarray, max_lag: float, bin_size: float) -> np.ndarray:
    """Counts of b - a differences in bins of bin_size from -max_lag to max_lag."""
    edges = np.arange(-max_lag, max_lag + bin_size / 2, bin_size)
    out = np.zeros(len(edges) - 1)
    if len(a) == 0 or len(b) == 0:
        return out
    lo = np.searchsorted(b, a - max_lag)
    hi = np.searchsorted(b, a + max_lag)
    diffs = np.concatenate([b[l:h] - x for x, l, h in zip(a, lo, hi)]) if len(a) else np.array([])
    out += np.histogram(diffs, edges)[0]
    return out


def circ_lin_regression(x: np.ndarray, phase: np.ndarray, slopes=np.linspace(-2 * np.pi / 20, 2 * np.pi / 20, 801)):
    """Circular-linear regression (Kempter et al. 2012): the slope (rad per unit of x) that
    maximises the mean resultant length of phase - slope * x, over a grid of slopes."""
    x, phase = np.asarray(x, float), np.asarray(phase, float)
    ok = np.isfinite(x) & np.isfinite(phase)
    x, phase = x[ok], phase[ok]
    if len(x) < 10:
        return np.nan, np.nan
    R = np.abs(np.exp(1j * (phase[None, :] - slopes[:, None] * x[None, :])).mean(axis=1))
    k = int(np.argmax(R))
    return float(slopes[k]), float(R[k])


# ----------------------------------------------------------------------------- waveforms

def waveforms(key: str, spikes_list, windows, n_before: int = 20, n_after: int = 30, max_spikes: int = 300):
    """Mean wide-band waveform of each unit in each time window (list of (t0, t1) in s).

    Returns an array units x windows x samples x channels (uV), high-passed at 300 Hz, and the
    number of spikes averaged. Each window is streamed once.
    """
    f = open_h5(sessions().loc[key, "raw_url"])
    ds = f["acquisition/ElectricalSeries/data"]
    conv = float(ds.attrs["conversion"])
    start = float(f["acquisition/ElectricalSeries/starting_time"][()])
    b, a = signal.butter(3, 300 / (RAW_RATE / 2), btype="high")
    n_ch = ds.shape[1]
    out = np.full((len(spikes_list), len(windows), n_before + n_after, n_ch), np.nan)
    counts = np.zeros((len(spikes_list), len(windows)), int)
    for w, (t0, t1) in enumerate(windows):
        lo, hi = int((t0 - start) * RAW_RATE), int((t1 - start) * RAW_RATE)
        x = ds[lo:hi, :].astype(np.float32) * conv * 1e6
        x = signal.filtfilt(b, a, x, axis=0).astype(np.float32)
        for u, sp in enumerate(spikes_list):
            idx = np.round((sp[(sp > t0 + 0.01) & (sp < t1 - 0.01)] - start) * RAW_RATE).astype(int) - lo
            if len(idx) > max_spikes:
                idx = idx[np.linspace(0, len(idx) - 1, max_spikes).astype(int)]
            counts[u, w] = len(idx)
            if len(idx):
                snip = x[idx[:, None] + np.arange(-n_before, n_after)[None, :], :]
                out[u, w] = snip.mean(axis=0)
        del x
    f.close()
    return out, counts


def waveform_features(wf: np.ndarray) -> dict:
    """Trough-to-peak (ms) and peak-to-peak amplitude (uV) on the channel of largest amplitude."""
    if not np.isfinite(wf).any():
        return {"channel": -1, "ttp_ms": np.nan, "amplitude_uv": np.nan}
    amp = np.nanmax(wf, axis=0) - np.nanmin(wf, axis=0)
    ch = int(np.nanargmax(amp))
    w = wf[:, ch]
    trough = int(np.argmin(w))
    peak = trough + int(np.argmax(w[trough:]))
    return {"channel": ch, "ttp_ms": (peak - trough) / RAW_RATE * 1000, "amplitude_uv": float(amp[ch])}


# ----------------------------------------------------------------------------- per-session work

STATES = ["Pre-Cooling", "Cooling on", "Post-Cooling"]
SHORT = {"Pre-Cooling": "pre", "Cooling on": "cooling", "Post-Cooling": "post"}


def temperature_shape(s: dict) -> dict:
    """Summary of the temperature trace used to tell recorded from modelled traces."""
    t, T = s["temp_t"], s["temp"]
    ok = np.isfinite(T)
    grid = np.arange(t[ok][0], t[ok][-1], 1.0)
    T1 = np.interp(grid, t[ok], T[ok])
    return {"temp_min": float(np.nanmin(T)), "temp_max": float(np.nanmax(T)),
            "temp_n_unique": int(len(np.unique(T[ok]))),
            "temp_frac_at_max": float(np.mean(T[ok] == np.nanmax(T))),
            "temp_d2_sd": float(np.std(np.diff(T1, 2))),
            "temp_1hz_t": grid, "temp_1hz": T1}


def behaviour_session(key: str) -> dict:
    """Trial measures, theta summary and checks for one session (no units)."""
    s = load_session(key)
    out = {"key": key, "subject": s["subject"], "n_trials": len(s["trials"]),
           "trial_columns": s["trial_columns"], "has_state": s["trials"]["state"].notna().all() and len(s["trials"]) > 0,
           "theta_channel": s["theta_channel"], "n_electrodes": s["n_electrodes"],
           "unit_quality_counts": s["unit_quality_counts"], "n_good_units": len(s["spikes"]),
           "frame_dt": float(np.median(np.diff(s["t"]))), "same_clock": s["same_clock"],
           "speed_unit": s["speed_unit"], "pos_conversion": s["pos_conversion"],
           "x_range": (float(np.nanmin(s["x"])), float(np.nanmax(s["x"]))),
           "y_range": (float(np.nanmin(s["y"])), float(np.nanmax(s["y"]))),
           "speed_pct": np.nanpercentile(s["speed"], [1, 50, 99]).tolist(),
           "subject_meta": s["subject_meta"], "series": s["series"]}
    out.update(temperature_shape(s))
    if len(s["trials"]) == 0:
        f = open_h5(sessions().loc[key, "raw_url"])
        out["raw_info"] = {"raw_series": series_listing(f)}
        f.close()
        return out
    th = theta_for_session(s)
    tr = trial_measures(s, th)
    out["trials"] = tr
    out["raw_info"] = th["raw_info"]
    out["lfp_rms_uv"] = th["lfp_rms_uv"]
    out["theta_peak_freq_median"] = float(np.median(th["peak_freq"]))
    # clock check: cooling minus pre theta frequency with the theta series shifted in time
    if out["has_state"]:
        contrast = {}
        f_frames_t = s["t"]
        for shift in [-600, -300, -120, -60, -30, 0, 30, 60, 120, 300, 600]:
            th2 = dict(th, cycle_t=th["cycle_t"] + shift, spec_t=th["spec_t"] + shift)
            tr2 = trial_measures(s, th2)
            m = tr2.groupby("state").theta_freq.mean()
            contrast[shift] = float(m.get("Cooling on", np.nan) - m.get("Pre-Cooling", np.nan))
        out["shift_contrast"] = contrast
    return out


def _frame_state(s: dict) -> tuple[np.ndarray, np.ndarray]:
    t = s["t"]
    tr = s["trials"]
    state = np.full(len(t), "", dtype=object)
    trial = np.full(len(t), -1)
    lo = np.searchsorted(t, tr.start.values)
    hi = np.searchsorted(t, tr.stop.values, side="right")
    for i, (a, b, st) in enumerate(zip(lo, hi, tr.state.values)):
        state[a:b] = st
        trial[a:b] = i
    return state, trial


def _seg_bins(lin: dict) -> list[tuple[int, int]]:
    edges = lin["edges"]
    b = [int(np.searchsorted(edges, x, side="right") - 1) for x in lin["seg_bounds"]]
    b[-1] = len(edges) - 1
    return [(b[0], b[1]), (b[1], b[2]), (b[2], b[3])]


def _field_size(rate_state: np.ndarray, field, seg_bins) -> float:
    a, b, pk = field
    seg = next((lo, hi) for lo, hi in seg_bins if lo <= a < hi)
    lo, hi = max(seg[0], a - 4), min(seg[1], b + 4)
    r = np.nan_to_num(rate_state[lo:hi])
    if r.max() <= 0:
        return np.nan
    inside = r[(a - lo):(b - lo)]
    p = (a - lo) + int(np.argmax(inside))
    thr = FIELD_FRACTION * r.max()
    i = j = p
    while i - 1 >= 0 and r[i - 1] > thr:
        i -= 1
    while j + 1 < len(r) and r[j + 1] > thr:
        j += 1
    return (j - i + 1) * BIN_CM


def _smooth_ccg(c: np.ndarray, n: int = 60) -> np.ndarray:
    g = gausswin(n)
    return np.convolve(c, g / g.sum(), mode="same")


def ccg_period(c: np.ndarray, lags: np.ndarray, p0: float, bounds: tuple[float, float], span: float) -> float:
    """Period of the theta modulation of a summed cross-correlogram: least-squares fit, over
    |lag| <= span, of a quadratic baseline plus a Gaussian-windowed cosine (a 1-D form of the
    surface the paper fits in Figure 5C). Returns NaN when the fit fails."""
    from scipy.optimize import curve_fit
    sel = np.abs(lags) <= span
    x, y = lags[sel], c[sel] / np.mean(c[sel])

    def model(x, b0, b1, b2, a, s, x0, period):
        return b0 + b1 * x + b2 * x ** 2 + a * np.exp(-0.5 * (x / s) ** 2) * np.cos(2 * np.pi * (x - x0) / period)

    best = None
    for start in np.linspace(bounds[0], bounds[1], 7):
        try:
            p, _ = curve_fit(model, x, y, p0=[1, 0, 0, 0.05, span / 2, 0, start],
                             bounds=([-np.inf, -np.inf, -np.inf, 0, span / 10, -start / 2, bounds[0]],
                                     [np.inf, np.inf, np.inf, np.inf, 4 * span, start / 2, bounds[1]]),
                             maxfev=20000)
        except (RuntimeError, ValueError):
            continue
        sse = np.sum((model(x, *p) - y) ** 2)
        if best is None or sse < best[0]:
            best = (sse, p)
    return float(best[1][-1]) if best is not None else np.nan


def peak_lag(c: np.ndarray, lags: np.ndarray, half_width: float) -> float:
    """Lag of the largest local maximum of c within half_width of zero; NaN if none."""
    w = np.flatnonzero(np.abs(lags) <= half_width)
    seg = c[w]
    pk, _ = signal.find_peaks(seg)
    if len(pk) == 0:
        return np.nan
    return float(lags[w][pk[np.argmax(seg[pk])]])


def pair_period(c: np.ndarray, lags: np.ndarray, main: float, lo: float, hi: float, nearest: bool = False) -> float:
    """Mean spacing from the main peak (at lag `main`) to the largest local maxima between lo
    and hi away from it, on either side; NaN when neither side has one. With `nearest`, the
    nearest local maximum on each side is taken instead of the largest."""
    if not np.isfinite(main):
        return np.nan
    pk, _ = signal.find_peaks(c)
    out = []
    for sign in (-1, 1):
        d = sign * (lags[pk] - main)
        sel = (d >= lo) & (d <= hi)
        if sel.any():
            k = pk[sel][np.argmin(d[sel])] if nearest else pk[sel][np.argmax(c[pk[sel]])]
            out.append(abs(lags[k] - main))
    return float(np.mean(out)) if out else np.nan


TIME_LAGS = np.arange(-399.5, 400, 1.0)                     # ms, centres of 1 ms bins
PHASE_LAGS = (np.arange(-400, 400) + 0.5) * 0.01 * np.pi     # rad, centres of 0.01 pi bins


def pair_ccgs(ta, tb, pa, pb):
    """Smoothed time (1 ms bins, +-400 ms) and phase (0.01 pi bins, +-4 pi) cross-correlograms."""
    ct = _smooth_ccg(ccg(ta, tb, 0.5, 0.001))[100:900]
    cp = _smooth_ccg(ccg(pa, pb, 5 * np.pi, 0.01 * np.pi))[100:900]
    return ct, cp


def unit_session(key: str, waveform_seconds: float = 120.0, with_waveforms: bool = True) -> dict:
    """Everything the unit claims need from one session, reduced to tables."""
    s = load_session(key)
    th = theta_for_session(s)
    tr = trial_measures(s, th)
    lin = linearize(s)
    t, speed = s["t"], s["speed"]
    dt = float(np.median(np.diff(t)))
    fstate, ftrial = _frame_state(s)
    seg = lin["segment"]
    l = lin["lin"]
    dl = np.full(len(t), np.nan)
    dl[1:-1] = (l[2:] - l[:-2])
    same = np.r_[False, (seg[2:] == seg[:-2]) & (seg[1:-1] == seg[2:]), False]
    forward = same & (dl > 0)
    run = speed > MAP_SPEED
    temp = s["temp"]
    inst_f = np.interp(t, th["cycle_t"], th["inst_freq"], left=np.nan, right=np.nan)
    edges = lin["edges"]
    segb = _seg_bins(lin)
    out = {"key": key, "subject": s["subject"], "lin": {k: lin[k] for k in ("L", "R", "frac_linearized")}}

    spikes = s["spikes"]
    n_units = len(spikes)
    # frame index of every spike
    sp_idx = [np.clip(np.searchsorted(t, sp) - 1, 0, len(t) - 1) for sp in spikes]
    in_beh = [(sp >= t[0]) & (sp <= t[-1]) for sp in spikes]

    # rates by state, over trial frames above 10 cm/s
    rows = []
    for u in range(n_units):
        row = {"unit": s["unit_ids"][u]}
        idx = sp_idx[u][in_beh[u]]
        for st in STATES:
            m = (fstate == st) & run
            row["rate_" + SHORT[st]] = float(np.sum(m[idx]) / (m.sum() * dt)) if m.any() else np.nan
            sel = spikes[u][in_beh[u]][m[idx]]
            row["osc_" + SHORT[st]] = oscillation_frequency(sel)
        m = np.isin(fstate, STATES) & run
        row["rate_trials"] = float(np.sum(m[idx]) / (m.sum() * dt))
        ph = phase_at(th, spikes[u][in_beh[u]][m[idx]])
        row["theta_mrl"] = float(np.abs(np.mean(np.exp(1j * ph[np.isfinite(ph)])))) if np.isfinite(ph).sum() > 20 else np.nan
        ph2 = phase_at(th, spikes[u][in_beh[u]][m[idx]] + 0.5)
        row["theta_mrl_shift"] = float(np.abs(np.mean(np.exp(1j * ph2[np.isfinite(ph2)])))) if np.isfinite(ph2).sum() > 20 else np.nan
        rows.append(row)
    units = pd.DataFrame(rows)

    # waveforms in a pre window and around the coldest cooling trial
    pre_tr = tr[tr.state == "Pre-Cooling"]
    cool_tr = tr[tr.state == "Cooling on"]
    w_pre = (float(pre_tr.start.iloc[0]), float(pre_tr.start.iloc[0]) + waveform_seconds)
    coldest = cool_tr.iloc[int(np.nanargmin(cool_tr.temperature.values))]
    mid = 0.5 * (coldest.start + coldest.stop)
    w_cool = (float(mid - waveform_seconds / 2), float(mid + waveform_seconds / 2))
    out["waveform_windows"] = {"pre": w_pre, "cooling": w_cool,
                               "cooling_window_temp": float(coldest.temperature)}
    if with_waveforms and n_units:
        wf, counts = waveforms_chunked(key, spikes, [w_pre, w_cool])
        for w, name in enumerate(["pre", "cooling"]):
            feats = [waveform_features(wf[u, w]) for u in range(n_units)]
            units["ttp_" + name] = [f_["ttp_ms"] for f_ in feats]
            units["amp_" + name] = [f_["amplitude_uv"] for f_ in feats]
            units["chan_" + name] = [f_["channel"] for f_ in feats]
            units["nwf_" + name] = counts[:, w]
        for name, (a_, b_) in [("pre", w_pre), ("cooling", w_cool)]:
            units["nsp_" + name] = [int(np.sum((sp > a_) & (sp < b_))) for sp in spikes]
        units["ttp"] = np.where(units.nwf_pre >= 30, units.ttp_pre, np.where(units.nwf_cooling >= 30, units.ttp_cooling, np.nan))
        units["cell_type"] = np.where(units.ttp.isna(), "unclassified",
                                      np.where((units.ttp <= NARROW_TTP_MS) | (units.rate_trials > WIDE_INT_RATE),
                                               "interneuron", "pyramidal"))
    else:
        units["cell_type"] = "unclassified"

    # rate maps (forward runs above 10 cm/s)
    base = forward & run
    occ = {}
    counts = {}
    for st in STATES + ["all"]:
        fm = base & (np.isin(fstate, STATES) if st == "all" else (fstate == st))
        occ[st], counts[st] = occupancy_and_counts(t, l, speed, fm, spikes, edges)
    rate = {st: smooth_map(counts[st], occ[st], 1.0, segb) for st in occ}
    # spatial information check: true against spikes shifted by 60 s
    shifted = [np.sort(np.mod(sp - t[0] + 60.0, t[-1] - t[0]) + t[0]) for sp in spikes]
    _, c_shift = occupancy_and_counts(t, l, speed, base & np.isin(fstate, STATES), shifted, edges)
    r_shift = smooth_map(c_shift, occ["all"], 1.0, segb)
    units["info_all"] = [skaggs_information(rate["all"][u], occ["all"]) for u in range(n_units)]
    units["info_all_shift60"] = [skaggs_information(r_shift[u], occ["all"]) for u in range(n_units)]
    for st in STATES:
        units["info_" + SHORT[st]] = [skaggs_information(rate[st][u], occ[st]) for u in range(n_units)]
    units["coherence"] = [spatial_coherence(rate["all"][u]) for u in range(n_units)]
    # information with the same number of spikes in each state: each state's spikes are
    # subsampled to the smallest count of the three, 20 draws averaged (a variant for fig3f)
    rng = np.random.default_rng([31] + [int(x) for x in re.findall(r"\d+", key)])
    smask = {st: base & (fstate == st) & np.isfinite(l) & (speed > MAP_SPEED) for st in STATES}
    eq = {st: [] for st in STATES}
    n_eq = []
    for u in range(n_units):
        fr_idx = sp_idx[u][in_beh[u]]
        per = {st: fr_idx[smask[st][fr_idx]] for st in STATES}
        n_min = min(len(v) for v in per.values())
        n_eq.append(n_min)
        for st in STATES:
            if n_min < 20:
                eq[st].append(np.nan)
                continue
            vals = []
            for _ in range(20):
                pick = rng.choice(per[st], n_min, replace=False)
                c_ = np.histogram(l[pick], edges)[0][None, :]
                vals.append(skaggs_information(smooth_map(c_, occ[st], 1.0, segb)[0], occ[st]))
            eq[st].append(float(np.nanmean(vals)))
    for st in STATES:
        units["info_eq_" + SHORT[st]] = eq[st]
    units["n_eq"] = n_eq

    # place fields of putative pyramidal cells
    frows = []
    pyr = [u for u in range(n_units) if units.cell_type.iloc[u] == "pyramidal"]
    unit_fields = {}
    centres = 0.5 * (edges[:-1] + edges[1:])
    sp_lin = [l[i] for i in sp_idx]
    for u in pyr:
        fields = find_fields(rate["all"][u], segb)
        unit_fields[u] = fields
        for fi, fld in enumerate(fields):
            a, b, pk = fld
            row = {"unit": s["unit_ids"][u], "u": u, "field": fi, "segment": [k for k, (lo, hi) in enumerate(segb) if lo <= a < hi][0],
                   "start_cm": edges[a], "stop_cm": edges[b], "peak_cm": centres[pk], "peak_rate_all": float(rate["all"][u][pk])}
            in_field_frame = base & (l >= edges[a]) & (l < edges[b])
            sp_ok = in_beh[u] & in_field_frame[sp_idx[u]]
            for st in STATES:
                m = in_field_frame & (fstate == st)
                ss = sp_ok & (fstate[sp_idx[u]] == st)
                times = spikes[u][ss]
                key_ = SHORT[st]
                row["n_" + key_] = int(ss.sum())
                row["time_" + key_] = float(m.sum() * dt)
                row["infield_rate_" + key_] = float(ss.sum() / (m.sum() * dt)) if m.sum() else np.nan
                row["peak_rate_" + key_] = float(np.nanmax(rate[st][u][a:b])) if np.isfinite(rate[st][u][a:b]).any() else np.nan
                row["size_" + key_] = _field_size(rate[st][u], fld, segb)
                row["fp_" + key_] = oscillation_frequency(times)
                row["flfp_" + key_] = float(np.nanmean(inst_f[sp_idx[u][ss]])) if ss.any() else np.nan
                row["v_" + key_] = float(np.nanmean(speed[sp_idx[u][ss]])) if ss.any() else np.nan
                row["temp_" + key_] = float(np.nanmean(temp[sp_idx[u][ss]])) if ss.any() else np.nan
                if ss.sum() >= 30:
                    flen = edges[b] - edges[a]
                    grid = np.linspace(-2 * 2 * np.pi / flen, 2 * 2 * np.pi / flen, 801)
                    slope, rbar = circ_lin_regression(sp_lin[u][ss] - edges[a], phase_at(th, times), grid)
                else:
                    slope, rbar = np.nan, np.nan
                row["slope_" + key_], row["rbar_" + key_] = slope, rbar
                # speed bins
                for lo_v in range(20, 120, 20):
                    sel = ss & (speed[sp_idx[u]] >= lo_v) & (speed[sp_idx[u]] < lo_v + 20)
                    row[f"fp_{key_}_v{lo_v}"] = oscillation_frequency(spikes[u][sel])
                    row[f"flfp_{key_}_v{lo_v}"] = float(np.nanmean(inst_f[sp_idx[u][sel]])) if sel.sum() >= 50 else np.nan
            frows.append(row)
    fields = pd.DataFrame(frows)
    out["units"], out["fields"] = units, fields

    # 20-trial windows stepped by one trial (calc_trial_averages.m)

    wrows = []
    n_tr = len(tr)
    for _, fr in fields.iterrows():
        u = int(fr.u)
        in_field_frame = base & (l >= fr.start_cm) & (l < fr.stop_cm)
        ss = in_beh[u] & in_field_frame[sp_idx[u]]
        sp_trial = ftrial[sp_idx[u]]
        for k in range(0, n_tr - 19):
            sel = ss & (sp_trial >= k) & (sp_trial < k + 20)
            if sel.sum() <= 50:
                continue
            wrows.append({"unit": fr.unit, "field": fr.field, "k": k,
                          "fp": oscillation_frequency(spikes[u][sel]),
                          "flfp": float(np.nanmean(inst_f[sp_idx[u][sel]])),
                          "temp": float(np.nanmean(temp[sp_idx[u][sel]]))})
    out["windows"] = pd.DataFrame(wrows)

    # population vectors of pyramidal cells
    pv = {}
    for st in STATES:
        M = rate[st][pyr] if pyr else np.zeros((0, len(centres)))
        scale = np.nan
        if len(pyr) >= 5:
            curve = []
            for d in range(0, 21):
                cs = []
                for lo, hi in segb:
                    for i in range(lo, hi - d):
                        x1, x2 = M[:, i], M[:, i + d]
                        ok = np.isfinite(x1) & np.isfinite(x2)
                        if ok.sum() >= 5 and np.std(x1[ok]) > 0 and np.std(x2[ok]) > 0:
                            cs.append(np.corrcoef(x1[ok], x2[ok])[0, 1])
                curve.append(np.mean(cs) if cs else np.nan)
            curve = np.array(curve)
            below = np.flatnonzero(curve < 0.5)
            if len(below) and below[0] > 0:
                d1 = below[0]
                scale = BIN_CM * (d1 - 1 + (curve[d1 - 1] - 0.5) / (curve[d1 - 1] - curve[d1]))
            pv[SHORT[st] + "_curve"] = curve
        pv[SHORT[st]] = scale
    out["pv"] = pv

    # pairs of overlapping fields of different cells on the same segment
    prow = []
    ccg_sum = {c: {"time": np.zeros(800), "phase": np.zeros(800)} for c in ("pre", "cooling", "post")}
    sp_phase2 = [phase_at(th, sp, unwrapped=True) for sp in spikes]
    for i, fa in fields.iterrows():
        for j, fb in fields.iterrows():
            if j <= i or fa.u == fb.u or fa.segment != fb.segment:
                continue
            if fa.stop_cm <= fb.start_cm or fb.stop_cm <= fa.start_cm:
                continue
            lo_cm, hi_cm = min(fa.start_cm, fb.start_cm), max(fa.stop_cm, fb.stop_cm)
            region = base & (l >= lo_cm) & (l < hi_cm)
            row = {"unit_a": fa.unit, "unit_b": fb.unit, "ltr": float(fb.peak_cm - fa.peak_cm)}
            for st in STATES:
                c = SHORT[st]
                sa = in_beh[int(fa.u)] & region[sp_idx[int(fa.u)]] & (fstate[sp_idx[int(fa.u)]] == st)
                sb = in_beh[int(fb.u)] & region[sp_idx[int(fb.u)]] & (fstate[sp_idx[int(fb.u)]] == st)
                ta, tb = spikes[int(fa.u)][sa], spikes[int(fb.u)][sb]
                row["na_" + c], row["nb_" + c] = len(ta), len(tb)
                if len(ta) < 50 or len(tb) < 50:
                    row["tau_" + c] = row["tau_half_" + c] = row["phase_" + c] = row["phase_half_" + c] = np.nan
                    row["period_" + c] = row["phase_period_" + c] = row["period_near_" + c] = np.nan
                    row["phase_period_near_" + c] = np.nan
                    continue
                pa, pb = sp_phase2[int(fa.u)][sa], sp_phase2[int(fb.u)][sb]
                pa, pb = np.sort(pa[np.isfinite(pa)]), np.sort(pb[np.isfinite(pb)])
                cc, pc = pair_ccgs(ta, tb, pa, pb)
                row["tau_" + c] = peak_lag(cc, TIME_LAGS, 70.0)
                half = 500.0 / np.nanmean(inst_f[sp_idx[int(fa.u)][sa]])
                row["tau_half_" + c] = peak_lag(cc, TIME_LAGS, half)
                row["phase_" + c] = peak_lag(pc, PHASE_LAGS, np.pi)
                row["phase_half_" + c] = peak_lag(pc, PHASE_LAGS, np.pi / 2)
                row["period_" + c] = pair_period(cc, TIME_LAGS, row["tau_" + c], 60.0, 200.0)
                row["period_near_" + c] = pair_period(cc, TIME_LAGS, row["tau_" + c], 60.0, 200.0, nearest=True)
                row["phase_period_" + c] = pair_period(pc, PHASE_LAGS, row["phase_" + c], np.pi, 3 * np.pi)
                row["phase_period_near_" + c] = pair_period(pc, PHASE_LAGS, row["phase_" + c], np.pi, 3 * np.pi, nearest=True)
                if cc.sum() > 0:
                    ccg_sum[c]["time"] += cc / cc.sum()
                if pc.sum() > 0:
                    ccg_sum[c]["phase"] += pc / pc.sum()
            prow.append(row)
    out["pairs"] = pd.DataFrame(prow)
    out["ccg_sum"] = ccg_sum

    # theta cycles during runs in trials
    up_t = th["cycle_t"]
    starts, stops = up_t[:-1], up_t[1:]
    midf = np.clip(np.searchsorted(t, 0.5 * (starts + stops)) - 1, 0, len(t) - 1)
    keep = run[midf] & np.isin(fstate[midf], STATES) & ((stops - starts) < 0.25)
    starts, stops, cst = starts[keep], stops[keep], fstate[midf][keep]
    place_units = [u for u in pyr if unit_fields.get(u)]
    active = np.zeros(len(starts))
    total = np.zeros(len(starts))
    for u in range(n_units):
        sp = spikes[u]
        n_in = np.searchsorted(sp, stops) - np.searchsorted(sp, starts)
        total += n_in
        if u in place_units:
            active += n_in > 0
    out["cycles"] = pd.DataFrame({"state": [SHORT[x] for x in cst],
                                  "frac_active": active / len(place_units) if place_units else np.nan,
                                  "spikes": total, "duration_ms": 1000 * (stops - starts)})
    out["n_place_cells"] = len(place_units)
    out["trials"] = tr
    return out


def waveforms_chunked(key: str, spikes_list, windows, n_before: int = 20, n_after: int = 30, max_spikes: int = 300):
    """As `waveforms`, reading each window in pieces aligned to the file's 81920-sample chunks."""
    f = open_h5(sessions().loc[key, "raw_url"])
    ds = f["acquisition/ElectricalSeries/data"]
    conv = float(ds.attrs["conversion"])
    start = float(f["acquisition/ElectricalSeries/starting_time"][()])
    sos = signal.butter(3, 300 / (RAW_RATE / 2), btype="high", output="sos")
    n_ch = ds.shape[1]
    chunk = ds.chunks[0] if ds.chunks else 81920
    sums = np.zeros((len(spikes_list), len(windows), n_before + n_after, n_ch))
    counts = np.zeros((len(spikes_list), len(windows)), int)
    for w, (t0, t1) in enumerate(windows):
        lo, hi = int((t0 - start) * RAW_RATE), int((t1 - start) * RAW_RATE)
        sel_idx = []
        for sp in spikes_list:
            idx = np.round((sp[(sp > t0) & (sp < t1)] - start) * RAW_RATE).astype(np.int64)
            if len(idx) > max_spikes:
                idx = idx[np.linspace(0, len(idx) - 1, max_spikes).astype(int)]
            sel_idx.append(idx)
        for c0 in range((lo // chunk) * chunk, hi, chunk):
            c1 = min(c0 + chunk, ds.shape[0])
            x = ds[c0:c1, :].astype(np.float32) * np.float32(conv * 1e6)
            x = signal.sosfiltfilt(sos, x, axis=0).astype(np.float32)
            for u, idx in enumerate(sel_idx):
                ii = idx[(idx - n_before >= c0 + 200) & (idx + n_after < c1 - 200)] - c0
                if len(ii):
                    sums[u, w] += x[ii[:, None] + np.arange(-n_before, n_after)[None, :], :].sum(axis=0)
                    counts[u, w] += len(ii)
            del x
    f.close()
    with np.errstate(invalid="ignore"):
        means = sums / counts[:, :, None, None]
    return means, counts
