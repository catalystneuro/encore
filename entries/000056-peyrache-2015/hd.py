"""Loading and measures for the head-direction recordings of dandiset 000056.

Peyrache, Lacroix, Petersen & Buzsaki (2015), Nature Neuroscience, doi:10.1038/nn.3968.

Each NWB file is one session of one mouse: spike times of sorted units (no electrode, shank,
region or waveform is stored for a unit), the processed position of a red and a blue LED on
the head (39.06 Hz, in cm; -1 where the LED was not detected), a table of sleep states
("Awake", "Non-REM", "REM"), LFP, and annotation series. Files are streamed from the archive
at the pinned version; nothing is written to disk.

Where the parameters come from:

- From the paper's Methods: head direction from the relative position of the two LEDs, with
  frames where either LED is missing left out; tuning curves in 1 degree bins, smoothed with a
  6 degree s.d. Gaussian; a von Mises fit and a Rayleigh test, and HD cells as concentration
  > 1, peak rate > 1 Hz and Rayleigh p < 0.001 (`KAPPA_MIN`, `PEAK_MIN_HZ`, `RAYLEIGH_P`);
  cells firing at 0.5 Hz or more for cross-correlations (`MIN_RATE_HZ`); binned spike-train
  correlations in 300 ms bins in waking and REM and 50 ms bins in SWS (Figure 3a); 10 ms bins
  for cross-correlograms, intensity functions and decoding, with decoding smoothed by a 300 ms
  s.d. Gaussian in waking; a chi-squared speed distribution with 3 degrees of freedom for the
  cross-correlogram estimate of angular velocity, fitted by a coarse search then a
  derivative-free search; at least 6 HD cells for Bayesian decoding.
- Chosen here, as the Methods do not fix them: the open-field epoch, which the files do not
  mark, found from position (`exploration_epoch`); the von Mises fit as the maximum
  likelihood fit to the tuning curve taken as a distribution of angles; the Rayleigh test on
  the tuning curve's resultant length with the number of waking spikes; the lag range of
  cross-correlograms (`CCG_MAX_LAG_S`); a free scale and offset between the expected and the
  observed cross-correlogram; the speed grid (`SPEED_GRID`); 6 degree angle bins for decoding.
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy import fft as sp_fft
from scipy.ndimage import gaussian_filter1d
from scipy.optimize import minimize

DANDISET_ID = "000056"
DANDISET_VERSION = "0.250624.0430"
EARLIER_VERSION = "0.210812.1518"

KAPPA_MIN, PEAK_MIN_HZ, RAYLEIGH_P = 1.0, 1.0, 0.001
MIN_RATE_HZ = 0.5
CANDIDATE_KAPPA = 0.5      # spike times are kept for units above this, for the clock check
TUNING_SMOOTH_DEG = 6.0
STATES = ("wake", "rem", "sws")
STATE_LABELS = {"sws": "Non-REM", "rem": "REM"}   # waking is the open-field epoch, found from position
PAIR_BIN_S = {"wake": 0.3, "rem": 0.3, "sws": 0.05}
CCG_BIN_S, CCG_MAX_LAG_S = 0.01, 4.0
SPEED_GRID = np.geomspace(2.0, 5000.0, 90)          # deg/s, coarse search of the mean angular speed
DECODE_BIN_S, DECODE_SMOOTH_S, DECODE_BIN_DEG = 0.01, 0.3, 6
MIN_HD_CELLS_DECODE = 6

# Exploration epoch (chosen here): 1 min windows, the 1st-99th percentile extent of the head
# position, the maximum over a rolling 5 min window, both axes above 30 cm; runs separated by
# 3 min or less merged; the first run of at least 15 min; 2 min trimmed from each end.
EXPL_SPAN_CM, EXPL_MIN_RUN_MIN, EXPL_MERGE_GAP_MIN, EXPL_TRIM_MIN = 30.0, 15, 3, 2


def asset_urls(version: str = DANDISET_VERSION) -> list[tuple[str, str]]:
    """(path, streaming URL) of every NWB file at a version."""
    with DandiAPIClient() as client:
        dandiset = client.get_dandiset(DANDISET_ID, version)
        return sorted((a.path, a.get_content_url(follow_redirects=1, strip_query=True))
                      for a in dandiset.get_assets() if a.path.endswith(".nwb"))


def asset_ids(version: str) -> dict[str, tuple[str, int]]:
    """Path -> (asset id, size) at a version, to compare versions."""
    with DandiAPIClient() as client:
        dandiset = client.get_dandiset(DANDISET_ID, version)
        return {a.path: (a.identifier, a.size) for a in dandiset.get_assets()}


def _text(value) -> str:
    if isinstance(value, bytes):
        return value.decode()
    if isinstance(value, np.ndarray):
        return "; ".join(_text(v) for v in value)
    return str(value)


def exploration_epoch(mid: np.ndarray, ok: np.ndarray, rate: float):
    """(start s, stop s, list of candidate runs in minutes) of the open-field epoch, or None."""
    w = int(round(60 * rate))
    nw = len(mid) // w
    span = np.zeros((nw, 2))
    for i in range(nw):
        o = ok[i * w:(i + 1) * w]
        if o.sum() > 0.3 * w:
            span[i] = np.ptp(np.percentile(mid[i * w:(i + 1) * w][o], [1, 99], axis=0), axis=0)
    rolling = np.array([span[max(0, i - 2):i + 3].max(0) for i in range(nw)])
    big = (rolling > EXPL_SPAN_CM).all(1)
    runs, i = [], 0
    while i < nw:
        if big[i]:
            j = i
            while j < nw and big[j]:
                j += 1
            if runs and i - runs[-1][1] <= EXPL_MERGE_GAP_MIN:
                runs[-1] = (runs[-1][0], j)
            else:
                runs.append((i, j))
            i = j
        else:
            i += 1
    long_runs = [r for r in runs if r[1] - r[0] >= EXPL_MIN_RUN_MIN]
    if not long_runs:
        return None, runs
    a, b = long_runs[0]
    return ((a + EXPL_TRIM_MIN) * 60.0, (b - EXPL_TRIM_MIN) * 60.0), runs


def circular_smooth(values: np.ndarray, sd_bins: float) -> np.ndarray:
    return gaussian_filter1d(values, sd_bins, mode="wrap")


def tuning_curve(spike_angles_deg: np.ndarray, occupancy_s: np.ndarray) -> np.ndarray:
    """Rate (Hz) in 1 degree bins: spike counts over time spent, smoothed (6 degree s.d.)."""
    counts = np.bincount(np.floor(spike_angles_deg).astype(int) % 360, minlength=360).astype(float)
    with np.errstate(invalid="ignore", divide="ignore"):
        rate = counts / occupancy_s
    if np.isnan(rate).any():   # unvisited bins: circular linear interpolation
        good = ~np.isnan(rate)
        x = np.arange(360)
        rate = np.interp(x, np.r_[x[good] - 360, x[good], x[good] + 360], np.tile(rate[good], 3))
    return circular_smooth(rate, TUNING_SMOOTH_DEG)


def a1inv(r: float) -> float:
    """Concentration of a von Mises distribution from its mean resultant length (Fisher 1993)."""
    if r < 0.53:
        return 2 * r + r ** 3 + 5 * r ** 5 / 6
    if r < 0.85:
        return -0.4 + 1.39 * r + 0.43 / (1 - r)
    return 1 / (r ** 3 - 4 * r ** 2 + 3 * r)


def von_mises_fit(curve: np.ndarray):
    """(preferred direction deg, concentration, mean resultant length) of a tuning curve."""
    phi = np.deg2rad(np.arange(360) + 0.5)
    w = np.clip(curve, 0, None)
    c, s = (w * np.cos(phi)).sum() / w.sum(), (w * np.sin(phi)).sum() / w.sum()
    r = float(np.hypot(c, s))
    return float(np.rad2deg(np.arctan2(s, c)) % 360), a1inv(r), r


def rayleigh_p(r: float, n: int) -> float:
    """Rayleigh test of uniformity for resultant length r over n angles (Zar's approximation)."""
    if n < 2:
        return 1.0
    rn = r * n
    p = np.exp(np.sqrt(1 + 4 * n + 4 * (n ** 2 - rn ** 2)) - (1 + 2 * n))
    return float(min(max(p, 0.0), 1.0))


def epochs_total(epochs) -> float:
    return float(sum(b - a for a, b in epochs))


def count_in_epochs(spikes: np.ndarray, epochs) -> int:
    return int(sum(np.searchsorted(spikes, b) - np.searchsorted(spikes, a) for a, b in epochs))


def load_session(path: str, url: str) -> dict:
    """Read one file and reduce it to what the analysis uses.

    All units get rates per state and a waking tuning curve; spike times are kept only for HD
    cells and other tuned units (concentration above `CANDIDATE_KAPPA`). Position is kept as head direction in the waking epoch and as 1 s head speed.
    """
    f = h5py.File(remfile.File(url), "r")
    s = {"path": path, "session": _text(f["general/session_id"][()]),
         "mouse": _text(f["general/subject/subject_id"][()])}
    s["species"] = _text(f["general/subject/species"][()])
    groups = [_text(g) for g in f["general/extracellular_ephys/electrodes/group_name"][()]]
    s["electrode_groups"] = {g: groups.count(g) for g in dict.fromkeys(groups)}
    s["locations"] = sorted(set(_text(x) for x in f["general/extracellular_ephys/electrodes/location"][()]))
    s["annotations"] = sorted(f["stimulus/presentation"].keys())
    s["has_raw"] = "ElectricalSeries" in f["acquisition"]
    lfp = f["processing/ecephys/LFP/LFP"]
    s["lfp_rate"] = float(lfp["starting_time"].attrs["rate"])
    s["duration_s"] = lfp["data"].shape[0] / s["lfp_rate"]

    # States
    behavior = f["processing"]["behavior"] if "behavior" in f["processing"] else {}
    s["states"] = {}
    if "states" in behavior:
        st = f["processing/behavior/states"]
        labels = np.array([_text(x) for x in st["label"][()]])
        t0, t1 = st["start_time"][()].astype(float), st["stop_time"][()].astype(float)
        s["state_table"] = (t0, t1, labels)
        for key, label in STATE_LABELS.items():
            m = labels == label
            s["states"][key] = list(zip(t0[m], t1[m]))
        s["states"]["awake_label"] = list(zip(t0[labels == "Awake"], t1[labels == "Awake"]))

    # Position: head direction and the open-field epoch
    s["has_position"] = "SubjectPosition" in behavior
    raw = f["acquisition/RedLED"]
    s["raw_led"] = {"unit": _text(raw["data"].attrs["unit"]), "conversion": float(raw["data"].attrs["conversion"]),
                    "max_first_10000": float(np.nanmax(raw["data"][:10000]))}
    if s["has_position"]:
        sp = f["processing/behavior/SubjectPosition"]
        red, blue = sp["RedLED"]["data"][:], sp["BlueLED"]["data"][:]
        rate = float(sp["RedLED"]["starting_time"].attrs["rate"])
        start = float(sp["RedLED"]["starting_time"][()])
        s["pos_unit"] = _text(sp["RedLED"]["data"].attrs["unit"])
        s["pos_conversion"] = float(sp["RedLED"]["data"].attrs["conversion"])
        s["pos_rate"], s["pos_start"], s["n_pos"] = rate, start, len(red)
        ok = (red[:, 0] >= 0) & (blue[:, 0] >= 0)
        s["led_missing"] = float(1 - ok.mean())
        mid = (red + blue) / 2
        sec = int(len(red) // rate)       # head speed (cm/s) in 1 s bins, for the clock check
        idx = (np.arange(len(red)) / rate).astype(int)
        step = np.r_[0, np.hypot(*np.diff(mid, axis=0).T)]
        step[~ok | ~np.r_[False, ok[:-1]]] = np.nan
        good = ~np.isnan(step) & (idx < sec)
        s["speed_1s"] = (np.bincount(idx[good], step[good], minlength=sec)[:sec]
                         / np.maximum(np.bincount(idx[good], minlength=sec)[:sec], 1) * rate)
        s["speed_1s"][np.bincount(idx[good], minlength=sec)[:sec] < rate / 2] = np.nan
        epoch, runs = exploration_epoch(mid, ok, rate)
        s["expl_runs_min"] = runs
        s["wake_epoch"] = epoch
        if epoch is not None:
            i0, i1 = int((epoch[0] - start) * rate), int((epoch[1] - start) * rate)
            seg_ok = ok[i0:i1]
            s["wake_extent_cm"] = np.ptp(np.percentile(mid[i0:i1][seg_ok], [1, 99], axis=0), axis=0)
            hd = np.rad2deg(np.arctan2(blue[i0:i1, 1] - red[i0:i1, 1], blue[i0:i1, 0] - red[i0:i1, 0])) % 360
            s["hd_t"] = start + (i0 + np.arange(i1 - i0)) / rate
            s["hd"] = np.where(seg_ok, hd, np.nan)
            s["states"]["wake"] = [epoch]

    # Units
    index = f["units/spike_times_index"][:]
    s["unit_ids"] = f["units/id"][:]
    s["n_spikes"] = np.diff(np.r_[0, index])
    all_spikes = f["units/spike_times"][:]
    s["spikes_sorted"] = True
    units = []
    for k in range(len(index)):
        sp_t = all_spikes[(index[k - 1] if k else 0):index[k]]
        if len(sp_t) > 1 and np.any(np.diff(sp_t) < 0):
            s["spikes_sorted"] = False
            sp_t = np.sort(sp_t)
        u = {"unit": int(s["unit_ids"][k]), "n": len(sp_t),
             "first": float(sp_t[0]) if len(sp_t) else np.nan, "last": float(sp_t[-1]) if len(sp_t) else np.nan}
        for key in STATES:
            if key in s["states"]:
                u[f"rate_{key}"] = count_in_epochs(sp_t, s["states"][key]) / epochs_total(s["states"][key])
        if "hd" in s:
            u.update(_hd_measures(sp_t, s))
            if u["kappa"] > CANDIDATE_KAPPA and u["peak"] > PEAK_MIN_HZ:
                u["spikes"] = sp_t
        units.append(u)
    s["units"] = units
    f.close()
    return s


def _occupancy(s) -> np.ndarray:
    valid = ~np.isnan(s["hd"])
    return np.bincount(np.floor(s["hd"][valid]).astype(int) % 360, minlength=360) / s["pos_rate"]


def spike_angles(spikes: np.ndarray, s: dict, shift_s: float = 0.0) -> np.ndarray:
    """Head direction (deg) at each spike in the waking epoch, from the nearest position frame."""
    t0, rate = s["hd_t"][0], s["pos_rate"]
    i = np.round((spikes + shift_s - t0) * rate).astype(int)
    i = i[(i >= 0) & (i < len(s["hd"]))]
    a = s["hd"][i]
    return a[~np.isnan(a)]


def _hd_measures(spikes: np.ndarray, s: dict) -> dict:
    w0, w1 = s["wake_epoch"]
    sp = spikes[(spikes >= w0) & (spikes < w1)]
    ang = spike_angles(sp, s)
    if "occupancy" not in s:
        s["occupancy"] = _occupancy(s)
    curve = tuning_curve(ang, s["occupancy"])
    pref, kappa, r = von_mises_fit(curve) if curve.sum() > 0 else (np.nan, 0.0, 0.0)
    p = rayleigh_p(r, len(ang))
    peak = float(curve.max())
    return {"n_wake": len(ang), "curve": curve, "pref": pref, "kappa": kappa, "r": r, "peak": peak,
            "rayleigh_p": p, "is_hd": bool(kappa > KAPPA_MIN and peak > PEAK_MIN_HZ and p < RAYLEIGH_P)}


def load_all(paths_urls=None, workers: int = 6) -> list[dict]:
    paths_urls = paths_urls or asset_urls()
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(lambda pu: load_session(*pu), paths_urls))


# --- binned activity ---------------------------------------------------------------------

def bin_mask(epochs, duration: float, binsize: float) -> np.ndarray:
    """Bins of `binsize` from time 0 that lie wholly inside the epochs."""
    n = int(np.ceil(duration / binsize))
    edges = np.arange(n + 1) * binsize
    m = np.zeros(n, bool)
    for a, b in epochs:
        i0, i1 = np.searchsorted(edges, a, "left"), np.searchsorted(edges, b, "right") - 1
        m[i0:i1] = True
    return m


def binned(spikes: np.ndarray, mask: np.ndarray, binsize: float) -> np.ndarray:
    """Spike counts in the bins of `mask`, concatenated."""
    i = (spikes / binsize).astype(int)
    i = i[i < len(mask)]
    return np.bincount(i, minlength=len(mask))[mask].astype(float)


def pearson_pairs(counts: np.ndarray, pairs) -> np.ndarray:
    z = counts - counts.mean(1, keepdims=True)
    sd = z.std(1)
    with np.errstate(invalid="ignore", divide="ignore"):
        return np.array([(z[i] * z[j]).mean() / (sd[i] * sd[j]) for i, j in pairs])


# --- cross-correlogram estimate of angular velocity --------------------------------------

def ccg_all(counts: np.ndarray, pairs, max_lag: int) -> np.ndarray:
    """Cross-correlograms of concatenated binned trains as a ratio to independent firing.

    Row k is the CCG of pair (i, j), with positive lags meaning j fires after i.
    """
    n = counts.shape[1]
    nfft = sp_fft.next_fast_len(n + max_lag, real=True)
    spec = sp_fft.rfft(counts, nfft, axis=1)
    means = counts.mean(1)
    out = np.empty((len(pairs), 2 * max_lag + 1))
    for k, (i, j) in enumerate(pairs):
        cc = sp_fft.irfft(np.conj(spec[i]) * spec[j], nfft)
        cc = np.r_[cc[-max_lag:], cc[:max_lag + 1]]
        out[k] = cc / (n * means[i] * means[j])
    return out


def angular_correlation(curve_i: np.ndarray, curve_j: np.ndarray) -> np.ndarray:
    """Correlation of curve_i with curve_j rotated by d degrees, d = 0..359."""
    zi = (curve_i - curve_i.mean()) / curve_i.std()
    zj = (curve_j - curve_j.mean()) / curve_j.std()
    return np.real(np.fft.ifft(np.conj(np.fft.fft(zi)) * np.fft.fft(zj))) / 360


_PROFILE_CACHE: dict = {}


def expected_profile(rho: np.ndarray, u_max: float, du: float = 1.0):
    """G(u) on a grid of u = mean speed x lag (deg): the expectation, over angular speeds
    distributed as chi-squared with 3 d.f. scaled to a mean of 1 (times the mean speed) and
    over both directions of turning, of the angular correlation `rho` at speed x lag.

    The expectation is exact: with rho written as a Fourier series, the symmetric part is
    sum_n a_n cos(n theta), and E[cos(n q u)] for q ~ Gamma(3/2, scale 2/3) is the real part of
    the characteristic function (1 - i (2/3) n u)^(-3/2), u in radians.
    """
    key = (u_max, du)
    if key not in _PROFILE_CACHE:
        u = np.arange(0, u_max + du, du)
        n = np.arange(181)
        _PROFILE_CACHE[key] = (u, np.real((1 - 1j * (2 / 3) * np.outer(np.deg2rad(u), n)) ** -1.5))
    u, m = _PROFILE_CACHE[key]
    c = np.fft.rfft(rho) / len(rho)
    a = 2 * np.real(c)
    a[0] = np.real(c[0])
    a[-1] = np.real(c[-1])        # the Nyquist term (n = 180) is not doubled
    return u, m @ a


def fit_speed(ccg: np.ndarray, lags_s: np.ndarray, u_grid: np.ndarray, g: np.ndarray):
    """Mean angular speed (deg/s) whose expected CCG, scaled and offset, best fits `ccg`.

    Returns (speed, at_edge, sse). The coarse grid gives the start of a Nelder-Mead search.
    """
    tau = np.abs(lags_s)

    def sse(log_v):
        e = np.interp(np.exp(log_v) * tau, u_grid, g)
        a_mat = np.c_[e, np.ones_like(e)]
        coef, *_ = np.linalg.lstsq(a_mat, ccg, rcond=None)
        if coef[0] <= 0:
            return np.inf
        return float(((a_mat @ coef - ccg) ** 2).sum())

    grid = np.array([sse(np.log(v)) for v in SPEED_GRID])
    k = int(np.argmin(grid))
    at_edge = k in (0, len(SPEED_GRID) - 1) or not np.isfinite(grid[k])
    res = minimize(lambda x: sse(x[0]), [np.log(SPEED_GRID[k])], method="Nelder-Mead",
                   options={"xatol": 1e-3, "fatol": 1e-12})
    v = float(np.exp(res.x[0]))
    at_edge = at_edge or not (SPEED_GRID[0] <= v <= SPEED_GRID[-1])
    return v, at_edge, float(res.fun)


# --- decoding ----------------------------------------------------------------------------

def decode(counts: np.ndarray, curves: np.ndarray, binsize: float) -> np.ndarray:
    """Poisson Bayesian decoder with a flat prior: angle bin of maximum posterior per time bin.

    counts: cells x time (smoothed counts per bin); curves: cells x angle bins (Hz).
    """
    f = np.clip(curves, 1e-3, None)
    loglik = counts.T @ np.log(f) - binsize * f.sum(0)[None, :]
    return np.argmax(loglik, axis=1)


def circ_diff(a, b):
    return (np.asarray(a) - np.asarray(b) + 180) % 360 - 180
