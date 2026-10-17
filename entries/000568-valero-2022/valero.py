"""Loading and measures for dandiset 000568 (Valero, Zutshi, Yoon & Buzsaki 2022).

Valero M, Zutshi I, Yoon E, Buzsaki G (2022). Probing subthreshold dynamics of hippocampal
neurons by pulsed optogenetics. Science 375, 570-574. doi:10.1126/science.abm1891.

Each session is deposited twice: a full file with the wideband and LFP signals, and a
"no-raw-data" file with the same units, events and behaviour. Spikes, events and position are
read from the small files; the LFP, when needed, from the full file. Files are streamed from the
archive at the pinned version; nothing is written to disk.

Each file holds, per session: sorted units (spike times only, no cell type and no waveform),
epochs, ripple intervals, linearized position on a 110 cm linear track, the laps (`trials`), and
in two sessions only, the times of the light pulses of each uLED (`OptogeneticSeriesSite<n>`;
four samples per pulse, off-on-on-off).

Where the parameters come from. The paper's Materials and Methods are in its supplement, which
this attempt could not obtain; the main text and figure legends give only the pulse length
(20 ms) and the use of "random intervals (20 ms) between the light pulses" as control epochs.
The other choices are:

- Light response test (`responsive_sites`): the rule of getuLEDResponse.m in the first
  author's later lab code (HippoCookBook, github.com/valegarman/HippoCookBook at commit
  0cbded394fd87e2d8ca9807fde1da85e5937b29c), which the paper does not cite: the rate in the
  0 to 20 ms window after onset exceeds the 99.9th percentile of a normal fit to the rates at
  random times (bootstrap), the mean z-score of the 1 ms PSTH during the pulse, against the
  20 ms before it, exceeds 1.96, and a two-sample Kolmogorov-Smirnov test of the PSTH bins
  during against before gives p < 0.01. Sites with fewer than `MIN_PULSES` pulses in the
  window tested are not tested (the code's `minNumberOfPulses` is 2000). The number of
  bootstrap sets (`N_BOOT`) is reduced from the code's 500 for speed.
- Rate maps and place fields (`rate_map`, `find_fields`): the defaults of buzcode
  (github.com/buzsakilab/buzcode at commit e615663b2b100782d1f378580f6d7aaa35c12937),
  which the paper names for its scripts: 50 bins over the track, Gaussian smoothing of 2 bins
  (bz_firingMapAvg); a field is a run of bins at or above 0.2 of the peak, 5% to 60% of the
  track long, with a peak of at least 2 Hz (bz_findPlaceFields1D). Maps are made per running
  direction, from the laps only.
- Putative pyramidal cells (`PYR_MAX_RATE_HZ`): the files carry no cell type. A unit is taken
  as a putative pyramidal cell when its mean rate in the first (baseline) epoch is below this
  value, a common choice for CA1, not the paper's (which used waveform and ACG features).
- Control windows: the 20 ms before each pulse onset, kept only when no uLED is on during it.
- Theta phase (`theta_phase`): 6 to 10 Hz band, zero-phase Butterworth filter of order 3,
  Hilbert phase; phase 0 at the peak and +-pi at the trough of the filtered LFP. The channel is
  the one with the largest ripple-band power at the deposited ripple peaks (pyramidal layer).
  Common choices.
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy import signal, stats

DANDISET_ID = "000568"
DANDISET_VERSION = "0.230705.1633"

PULSE_WINDOW_S = 0.020      # paper: 20 ms pulses
CONTROL_WINDOW_S = 0.020    # paper: random 20 ms intervals between pulses
MIN_PULSES = 1000           # sites with fewer pulses are not tested (code: 2000 over a whole session)
N_BOOT = 100                # HippoCookBook getuLEDResponse.m uses 500
BOOT_PERCENTILE = 0.999     # getuLEDResponse.m bootsTrapCI [0.001 0.999]
Z_THRESHOLD = 1.96          # getuLEDResponse.m
KS_ALPHA = 0.01             # getuLEDResponse.m
PYR_MAX_RATE_HZ = 5.0       # putative pyramidal cells: baseline rate below this (common choice)
TRACK_CM = 110.0            # file description: PVC linear track, 110 cm long
N_BINS = 50                 # bz_firingMapAvg default
SMOOTH_BINS = 2.0           # bz_firingMapAvg default
FIELD_THRESHOLD = 0.2       # bz_findPlaceFields1D default
FIELD_MIN_SIZE = 0.05       # bz_findPlaceFields1D default, fraction of the track
FIELD_MAX_SIZE = 0.60       # bz_findPlaceFields1D default
FIELD_MIN_PEAK_HZ = 2.0     # bz_findPlaceFields1D default
GRID_S = 0.002              # time grid for occupancy, light and control masks
THETA_BAND = (6.0, 10.0)
RIPPLE_BAND = (130.0, 200.0)
LFP_RATE = 1250.0


# --- archive -------------------------------------------------------------------------------

def assets() -> list[dict]:
    """Path, size and streaming URL of every NWB file at the pinned version."""
    with DandiAPIClient() as client:
        dandiset = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        return sorted(({"path": a.path, "size": a.size,
                        "url": a.get_content_url(follow_redirects=1, strip_query=True)}
                       for a in dandiset.get_assets() if a.path.endswith(".nwb")),
                      key=lambda a: a["path"])


def session_key(path: str) -> str:
    """Subject and session name shared by the two files of a session."""
    name = path.split("/")[-1].split("_behavior")[0].replace("-no-raw-data", "")
    return name


def _open(url: str) -> h5py.File:
    return h5py.File(remfile.File(url), "r")


def _text(value) -> str:
    return value.decode() if isinstance(value, bytes) else str(value)


def file_fingerprint(asset: dict) -> dict:
    """What identifies the content of a file without reading its signals."""
    with _open(asset["url"]) as f:
        idx = f["units/spike_times_index"][:]
        st = f["units/spike_times"]
        n = st.shape[0]
        head = st[: min(n, 20000)]
        tail = st[max(0, n - 20000):]
        rip = f["processing/ecephys/RippleTimeIntervals/peak_time"][:] \
            if "processing/ecephys/RippleTimeIntervals" in f else np.array([])
        lin = "processing/behavior/LinearMazePositionTracking/SpatiaLSeriesLinearized/data"
        pos = f[lin][:] if lin in f else np.array([])
        raw = f["acquisition/ElectricalSeries"] if "ElectricalSeries" in f["acquisition"] else None
        lfp = f["processing/ecephys/LFP/ElectricalSeriesLFP"] if "processing/ecephys/LFP" in f else None
        epochs_stop = float(f["intervals/epochs/stop_time"][-1])
        return {
            "path": asset["path"], "session": session_key(asset["path"]),
            "session_id": _text(f["general/session_id"][()]),
            "pair_key": _text(f["general/session_id"][()]).replace("_no_raw_data", ""),
            "raw_s": raw["data"].shape[0] / float(raw["starting_time"].attrs["rate"])
            if raw is not None and "starting_time" in raw else (np.nan if raw is None else -1.0),
            "lfp_s": lfp["data"].shape[0] / float(lfp["starting_time"].attrs["rate"]) if lfp is not None else np.nan,
            "last_epoch_end_s": epochs_stop,
            "session_start_time": _text(f["session_start_time"][()]),
            "subject": _text(f["general/subject/subject_id"][()]),
            "n_units": int(len(idx)), "n_spikes": int(n),
            "spike_index_sum": int(idx.astype(np.int64).sum()),
            "spike_head_sum": float(np.sum(head)), "spike_tail_sum": float(np.sum(tail)),
            "n_ripples": int(len(rip)), "ripple_sum": float(np.sum(rip)),
            "n_position": int(len(pos)), "position_sum": float(np.nansum(pos)),
            "has_raw": "ElectricalSeries" in f["acquisition"],
            "has_lfp": "processing/ecephys/LFP" in f,
            "opto_sites": sorted(f["stimulus/presentation"].keys()) if "stimulus/presentation" in f else [],
        }


# --- one session ---------------------------------------------------------------------------

def _pulses(group) -> dict:
    """Onsets, offsets and stored value of each pulse of one uLED (off-on-on-off samples)."""
    v = group["data"][:]
    t = group["timestamps"][:]
    rising = np.flatnonzero((v[1:] > 0) & (v[:-1] == 0)) + 1
    falling = np.flatnonzero((v[1:] == 0) & (v[:-1] > 0)) + 1
    onsets = t[rising - 1]          # the off sample before the ramp: the start of the 1 ms rise
    offsets = t[falling]            # the off sample at the end of the ramp down
    return {"on": onsets, "off": offsets, "values": np.unique(v[v > 0]),
            "unit": _text(group["data"].attrs.get("unit", ""))}


def load_session(url: str, with_pulses: bool = True) -> dict:
    """Everything the analysis uses from one no-raw-data file, as numpy arrays."""
    with _open(url) as f:
        idx = f["units/spike_times_index"][:].astype(np.int64)
        st = f["units/spike_times"][:]
        starts = np.concatenate([[0], idx[:-1]])
        spikes = [st[a:b] for a, b in zip(starts, idx)]
        e = f["intervals/epochs"]
        cols = list(e.attrs["colnames"])
        epochs = [{"start": float(a), "stop": float(b),
                   **{c: _text(e[c][i]) for c in cols if c not in ("start_time", "stop_time")}}
                  for i, (a, b) in enumerate(zip(e["start_time"][:], e["stop_time"][:]))]
        s = {"subject": _text(f["general/subject/subject_id"][()]),
             "session_id": _text(f["general/session_id"][()]),
             "spikes": spikes, "unit_name": [_text(x) for x in f["units/unit_name"][:]],
             "epochs": epochs}
        if "processing/ecephys/RippleTimeIntervals" in f:
            r = f["processing/ecephys/RippleTimeIntervals"]
            s["ripples"] = np.column_stack([r["start_time"][:], r["stop_time"][:], r["peak_time"][:]])
        else:
            s["ripples"] = np.zeros((0, 3))
        lin = "processing/behavior/LinearMazePositionTracking/SpatiaLSeriesLinearized"
        if lin in f:
            s["pos_t"] = f[lin + "/timestamps"][:]
            s["pos_x"] = f[lin + "/data"][:]
            s["pos_attrs"] = {k: (v.item() if hasattr(v, "item") else _text(v))
                              for k, v in f[lin + "/data"].attrs.items() if k in ("unit", "conversion")}
        if "intervals/trials" in f:
            t = f["intervals/trials"]
            s["laps"] = np.column_stack([t["start_time"][:], t["stop_time"][:], t["visited_arm"][:]])
        else:
            s["laps"] = np.zeros((0, 3))
        s["pulses"] = {}
        if with_pulses and "stimulus/presentation" in f:
            for k in sorted(f["stimulus/presentation"].keys()):
                s["pulses"][k.replace("OptogeneticSeries", "")] = _pulses(f["stimulus/presentation"][k])
    return s


def load_sessions(urls: list[str], with_pulses: bool = True, workers: int = 8) -> list[dict]:
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(lambda u: load_session(u, with_pulses), urls))


def epoch_interval(s: dict, paradigm: str) -> list[tuple[float, float]]:
    return [(e["start"], e["stop"]) for e in s["epochs"] if e.get("behavioral_paradigm") == paradigm]


# --- intervals and counts ------------------------------------------------------------------

def count_in_windows(spk: np.ndarray, starts: np.ndarray, width: float) -> np.ndarray:
    """Number of spikes in [start, start + width) for each start."""
    return np.searchsorted(spk, starts + width) - np.searchsorted(spk, starts)


def in_intervals(t: np.ndarray, iv: np.ndarray) -> np.ndarray:
    """Whether each time falls inside any of the sorted, non-overlapping intervals (n x 2)."""
    if len(iv) == 0:
        return np.zeros(len(t), bool)
    i = np.searchsorted(iv[:, 0], t, side="right") - 1
    ok = i >= 0
    out = np.zeros(len(t), bool)
    out[ok] = t[ok] < iv[i[ok], 1]
    return out


def merge_intervals(iv: np.ndarray) -> np.ndarray:
    if len(iv) == 0:
        return iv.reshape(0, 2)
    iv = iv[np.argsort(iv[:, 0])]
    out = [list(iv[0])]
    for a, b in iv[1:]:
        if a <= out[-1][1]:
            out[-1][1] = max(out[-1][1], b)
        else:
            out.append([a, b])
    return np.array(out)


def all_light_intervals(s: dict) -> np.ndarray:
    """Merged on-intervals of every uLED."""
    iv = np.concatenate([np.column_stack([p["on"], p["off"]]) for p in s["pulses"].values()])
    return merge_intervals(iv)


def control_onsets(s: dict) -> np.ndarray:
    """Starts of the 20 ms windows before each pulse onset during which no uLED is on."""
    on = np.unique(np.concatenate([p["on"] for p in s["pulses"].values()]))
    light = all_light_intervals(s)
    starts = on - CONTROL_WINDOW_S
    # a window is free of light when no light interval overlaps [start, start + 20 ms)
    j = np.searchsorted(light[:, 0], starts + CONTROL_WINDOW_S, side="left") - 1
    ok = np.ones(len(starts), bool)
    has = j >= 0
    ok[has] = light[j[has], 1] <= starts[has]
    return starts[ok]


def restrict(t: np.ndarray, ivs) -> np.ndarray:
    keep = np.zeros(len(t), bool)
    for a, b in ivs:
        keep |= (t >= a) & (t < b)
    return t[keep]


# --- light responses -----------------------------------------------------------------------

def psth(spk: np.ndarray, onsets: np.ndarray, lo: float = -0.02, hi: float = 0.02,
         bin_s: float = 0.001) -> np.ndarray:
    """Rate (Hz) in 1 ms bins around the onsets."""
    edges = np.arange(lo, hi + bin_s / 2, bin_s)
    counts = np.zeros(len(edges) - 1)
    a = np.searchsorted(spk, onsets + lo)
    b = np.searchsorted(spk, onsets + hi)
    rel = np.concatenate([spk[i:j] - o for i, j, o in zip(a, b, onsets) if j > i]) if len(onsets) else []
    if len(rel):
        counts = np.histogram(rel, edges)[0].astype(float)
    return counts / max(len(onsets), 1) / bin_s


def response_test(spk: np.ndarray, onsets: np.ndarray, span: tuple[float, float],
                  rng: np.random.Generator) -> dict:
    """The three-way test of getuLEDResponse.m for one unit and one uLED."""
    n = len(onsets)
    rate_during = count_in_windows(spk, onsets, PULSE_WINDOW_S).sum() / (n * PULSE_WINDOW_S)
    boot = np.empty(N_BOOT)
    for k in range(N_BOOT):
        r = np.sort(rng.uniform(span[0], span[1] - PULSE_WINDOW_S, n))
        boot[k] = count_in_windows(spk, r, PULSE_WINDOW_S).sum() / (n * PULSE_WINDOW_S)
    ci_hi = stats.norm.ppf(BOOT_PERCENTILE, boot.mean(), boot.std(ddof=1) if boot.std() > 0 else 1e-12)
    h = psth(spk, onsets)
    before, during = h[:20], h[20:]
    sd = before.std(ddof=1)
    z = (during.mean() - before.mean()) / sd if sd > 0 else (np.inf if during.mean() > before.mean() else 0.0)
    ks_p = stats.ks_2samp(during, before).pvalue
    return {"rate_during": rate_during, "rate_before": before.mean(), "boot_hi": ci_hi,
            "z": z, "ks_p": ks_p,
            "responsive": bool(rate_during > ci_hi and z > Z_THRESHOLD and ks_p < KS_ALPHA)}


def responsive_sites(s: dict, window: tuple[float, float], rng: np.random.Generator) -> list[dict]:
    """Per unit and uLED, the light response test over the pulses inside `window`."""
    rows = []
    for site, p in s["pulses"].items():
        on = p["on"][(p["on"] >= window[0]) & (p["on"] < window[1])]
        for u, spk in enumerate(s["spikes"]):
            if len(on) < MIN_PULSES:
                rows.append({"unit": u, "site": site, "n_pulses": len(on), "tested": False})
                continue
            r = response_test(spk, on, window, rng)
            rows.append({"unit": u, "site": site, "n_pulses": len(on), "tested": True, **r})
    return rows


# --- position, maps and fields -------------------------------------------------------------

def lap_grid(s: dict, laps: np.ndarray) -> dict:
    """Time grid over the laps with position, direction and lap number at each step."""
    ts, dirs, lap_ids = [], [], []
    for i, (a, b, d) in enumerate(laps):
        t = np.arange(a, b, GRID_S)
        ts.append(t)
        dirs.append(np.full(len(t), int(d)))
        lap_ids.append(np.full(len(t), i))
    t = np.concatenate(ts)
    x = np.interp(t, s["pos_t"], s["pos_x"])
    return {"t": t, "x": x, "dir": np.concatenate(dirs), "lap": np.concatenate(lap_ids)}


def bin_index(x: np.ndarray) -> np.ndarray:
    return np.clip((x / TRACK_CM * N_BINS).astype(int), 0, N_BINS - 1)


def _smooth(v: np.ndarray) -> np.ndarray:
    k = np.arange(-int(4 * SMOOTH_BINS), int(4 * SMOOTH_BINS) + 1)
    w = np.exp(-0.5 * (k / SMOOTH_BINS) ** 2)
    w /= w.sum()
    return np.convolve(v, w, mode="same")


def rate_map(spk: np.ndarray, grid: dict, mask: np.ndarray) -> np.ndarray:
    """Smoothed rate map (Hz) per direction (2 x N_BINS), counting only grid steps where mask holds.

    Spikes are assigned to the grid step they fall in; occupancy is the masked time per bin.
    """
    g = grid["t"]
    i = np.searchsorted(g, spk, side="right") - 1
    ok = (i >= 0) & (i < len(g))
    i = i[ok]
    i = i[(spk[ok] - g[i]) < GRID_S]
    i = i[mask[i]]
    out = np.full((2, N_BINS), np.nan)
    b_all = bin_index(grid["x"])
    for d in (0, 1):
        sel = (grid["dir"] == d) & mask
        occ = np.bincount(b_all[sel], minlength=N_BINS) * GRID_S
        cnt = np.bincount(b_all[i][grid["dir"][i] == d], minlength=N_BINS).astype(float)
        if occ.sum() == 0:
            continue
        occ_s, cnt_s = _smooth(occ), _smooth(cnt)
        with np.errstate(invalid="ignore", divide="ignore"):
            m = np.where(occ_s > 0, cnt_s / occ_s, np.nan)
        m[occ == 0] = np.nan
        out[d] = m
    return out


def find_fields(m: np.ndarray) -> list[tuple[int, int, int]]:
    """Place fields of one direction's map, as (start bin, stop bin exclusive, peak bin).

    bz_findPlaceFields1D defaults: bins >= 0.2 x peak, 5% to 60% of the track, peak >= 2 Hz.
    Secondary fields need a peak of at least 0.6 of the map's maximum (minPeak2nd).
    """
    if np.all(np.isnan(m)):
        return []
    v = np.nan_to_num(m)
    top = v.max()
    if top < FIELD_MIN_PEAK_HZ:
        return []
    fields = []
    above = v >= FIELD_THRESHOLD * top
    i = 0
    while i < len(v):
        if above[i]:
            j = i
            while j < len(v) and above[j]:
                j += 1
            peak = i + int(np.argmax(v[i:j]))
            size = (j - i) / len(v)
            if FIELD_MIN_SIZE <= size <= FIELD_MAX_SIZE and v[peak] >= FIELD_MIN_PEAK_HZ:
                if v[peak] == top or v[peak] >= 0.6 * top:
                    fields.append((i, j, peak))
            i = j
        else:
            i += 1
    return fields


def spatial_info(m: np.ndarray, occ: np.ndarray) -> float:
    """Skaggs spatial information (bits/spike) of a map with its occupancy."""
    ok = ~np.isnan(m) & (occ > 0)
    p = occ[ok] / occ[ok].sum()
    r = m[ok]
    mean = np.sum(p * r)
    if mean <= 0:
        return np.nan
    with np.errstate(divide="ignore", invalid="ignore"):
        terms = np.where(r > 0, p * r / mean * np.log2(r / mean), 0.0)
    return float(np.sum(terms))


def map_corr(a: np.ndarray, b: np.ndarray) -> float:
    ok = ~np.isnan(a) & ~np.isnan(b)
    if ok.sum() < 5 or np.std(a[ok]) == 0 or np.std(b[ok]) == 0:
        return np.nan
    return float(stats.spearmanr(a[ok], b[ok]).statistic)


# --- LFP -----------------------------------------------------------------------------------

def read_lfp(url: str, t0: float, t1: float, channels=None) -> np.ndarray:
    """LFP samples (int16, time x channel) between t0 and t1 s from a full file."""
    with _open(url) as f:
        d = f["processing/ecephys/LFP/ElectricalSeriesLFP/data"]
        a, b = int(t0 * LFP_RATE), int(t1 * LFP_RATE)
        x = d[a:b, :]
    return x if channels is None else x[:, channels]


def ripple_channel(lfp: np.ndarray, t0: float, ripple_peaks: np.ndarray) -> int:
    """Channel with the largest ripple-band power in 50 ms around the deposited ripple peaks."""
    sos = signal.butter(3, RIPPLE_BAND, btype="band", fs=LFP_RATE, output="sos")
    y = signal.sosfiltfilt(sos, lfp.astype(float), axis=0)
    idx = ((ripple_peaks - t0) * LFP_RATE).astype(int)
    idx = idx[(idx > 40) & (idx < len(y) - 40)]
    win = np.concatenate([idx + k for k in range(-31, 32)])
    return int(np.argmax((y[win] ** 2).mean(axis=0)))


def theta_phase(x: np.ndarray) -> np.ndarray:
    sos = signal.butter(3, THETA_BAND, btype="band", fs=LFP_RATE, output="sos")
    y = signal.sosfiltfilt(sos, x.astype(float))
    return np.angle(signal.hilbert(y))
