"""Loading and measures for the optrode recordings of dandiset 000230.

Jacobsen, Nair, Obenhaus, Donato, Slettmoen, Moser & Moser (2022), Cell Reports Methods 2,
100221, doi:10.1016/j.crmeth.2022.100221.

Each NWB file holds one session of one mouse (58313 or 70375): an open field part (position and
head direction at 50 Hz, stored in cm and radians) followed by laser trials in a holding box (the
`PhotoStim` epochs, with the laser TTL as `task_events`, code 0 onset and code 1 offset), and the
spike times of a curated subset of units. Unit ids are tetrode * 1000 + cluster id (1089 is
tetrode 1, cluster 89), which is how the figures label cells (T1 C89). Files are streamed from the
archive at the pinned version; nothing is written to disk.

Where the parameters come from:

- Latency and fidelity follow the claims file's shared definitions, taken from the STAR Methods,
  "Analysis of electrophysiology data": the mean time from a pulse to the first spike within 10 ms,
  over pulses followed by a spike within 10 ms, and the percentage of pulses followed by one.
  `LATENCY_WINDOW_S` is that 10 ms. The pulse time is the TTL onset (reading a) or offset
  (reading b), as the claims file lists.
- The first TTL event of each laser epoch starts exactly at the epoch's start time and lasts 0.6
  to 1.9 s, where every other event lasts about 1.06 ms; its onset is not a pulse onset. Events
  longer than `MAX_PULSE_S` are left out (a check of the data, not a method of the paper).
- Open-field firing rate: spikes in the open field over its duration (claims file, opening
  comment). The open field is not an epoch in the files; it is taken as the span of the position
  series, 0 s to its last sample, an assumption (it is the open-field recording the files hold; the
  STAR Methods give its length only as "approximately 30 min"). `open_field(max_s=1800)` gives the
  other reading, the first 30 min, which the notebook runs for every session.
- Cell classification follows Rowland et al. (2018), eLife 7, e36664, which the STAR Methods
  cite for all analysis ("All data were analyzed with custom Python code ... as reported in
  Rowland et al. (2018)"). From its Materials and methods: the gridness score from expanding
  circular samples of the spatial autocorrelogram, central peak excluded, its radius the first
  local minimum of the radial profile or the first radius where correlation falls under 0.2,
  samples from 10 cm beyond that radius to 90 cm in steps of one bin of 2.5 cm, score the highest
  over samples of min(r60, r120) - max(r30, r90, r150); the mean vector length of the
  head-direction tuning map; a head-direction cell also needs a first-half to second-half tuning
  correlation above 0.6; the border score of Solstad et al. (2008), fields being neighbouring bins
  above 20% of the peak rate covering at least 200 cm2; a class is assigned when the score exceeds
  the 95th percentile of 200 shuffles of the spike train along the path, with wrap-around.
  Rowland et al. call the mean vector length the "head-direction score"; the paper's Figure S4 gives
  the two different values, so the notebook shows other readings of the tuning curve.
- Details Rowland et al. (2018) do not state in the text are taken from the analysis code it links,
  https://github.com/davidcrowland/archdata at commit 945226315bafe6ce68fcbd4c75a589fba0a8eca1
  (analysis_helpers/tracking.py, spatial_maps.py, and the parameter file
  analysis_helpers/parameters/params_ragnihiij): positions smoothed with a Gaussian of sigma 2
  samples, speed from the smoothed positions smoothed with sigma 1 sample, a speed cutoff of
  5 cm/s for rate maps, rate maps smoothed with a Gaussian of sigma 2 bins (spikes and time, zeros
  outside), head-direction tuning in 180 bins of 2 degrees, smoothed circularly with sigma 2 bins.
  The code's parameter file gives 2 cm bins; the text's 2.5 cm is used, the text coming first.
- The shuffle interval: the text says the spike train "was time-shifted along the animal's path by
  a random interval between ± 20 s, with the end of the session wrapped to the beginning"
  (Materials and methods, classification into functional classes); the archdata code has no spatial
  shuffle. Two readings are run:
  `literal`, uniform in [-20, 20] s, and `standard`, uniform in [20 s, duration - 20 s], the
  shuffle of the papers Rowland et al. cite for the scores (Langston et al. 2010; Solstad et al.
  2008). The notebook shows both; `standard` is adopted as an assumption, as a shift of under 20 s
  leaves the spike train close to the observed one.
- The border score takes the walls as the edges of the tracked extent and leaves unvisited bins out;
  a cell firing uniformly over the box scores above zero (about 0.5 on synthetic data), a baseline
  the shuffle thresholds take in.
- `MIN_OVERLAP_BINS` for the autocorrelogram (lags with fewer than 20 overlapping bins are left
  out) is a standard choice; it touches only the edges, beyond the 90 cm the gridness score uses.
"""

from __future__ import annotations

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy import ndimage
from scipy.signal import fftconvolve

DANDISET_ID = "000230"
DANDISET_VERSION = "0.220506.1516"

LATENCY_WINDOW_S = 0.010     # STAR Methods: first spike within 10 ms of the pulse
MAX_PULSE_S = 0.005          # data check: real pulses last about 1.06 ms
POS_RATE_HZ = 50.0           # STAR Methods: LED position data at 50 Hz; files agree
POS_SIGMA_SAMPLES = 2        # archdata tracking.py
SPEED_SIGMA_SAMPLES = 1      # archdata tracking.py
SPEED_CUTOFF_CM_S = 5.0      # archdata params_ragnihiij
BIN_CM = 2.5                 # Rowland et al. (2018), Methods, gridness score
RATE_SIGMA_BINS = 2          # archdata params_ragnihiij (sigma_rate, sigma_time)
HD_BINS = 180                # archdata spatial_maps.hd_tuning_curve
HD_SIGMA_BINS = 2            # archdata spatial_maps.hd_tuning_curve
HD_STABILITY_MIN = 0.6       # Rowland et al. (2018), Methods
GRID_STEP_BEYOND_PEAK_CM = 10.0
GRID_MAX_RADIUS_CM = 90.0
GRID_PEAK_THRESHOLD = 0.2
FIELD_FRACTION = 0.2         # Rowland et al. (2018), border score
FIELD_MIN_AREA_CM2 = 200.0
N_SHUFFLES = 200
SHUFFLE_PERCENTILE = 95
SHUFFLE_MIN_S = 20.0
MIN_OVERLAP_BINS = 20


def asset_urls() -> list[tuple[str, str]]:
    """(path, streaming URL) of every NWB file at the pinned version."""
    with DandiAPIClient() as client:
        dandiset = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        return sorted((a.path, a.get_content_url(follow_redirects=1, strip_query=True))
                      for a in dandiset.get_assets() if a.path.endswith(".nwb"))


def _text(value) -> str:
    value = value[()] if hasattr(value, "shape") else value
    return value.decode() if isinstance(value, bytes) else str(value)


def load_session(path: str, url: str) -> dict:
    """Read one file: metadata, units, laser events, open-field tracking. Small arrays only."""
    with h5py.File(remfile.File(url), "r") as f:
        desc = _text(f["session_description"])
        first_line = desc.splitlines()[0]          # "Day 17 after rabies injection, session 1"
        day = int(first_line.split()[1])
        session_no = int(first_line.rsplit("session", 1)[1].strip())
        ids = f["units/id"][:]
        st_all = f["units/spike_times"][:]
        st_idx = f["units/spike_times_index"][:]
        starts = np.concatenate([[0], st_idx[:-1]])
        el_idx = f["units/electrodes_index"][:]
        el = f["units/electrodes"][:]
        el_starts = np.concatenate([[0], el_idx[:-1]])
        units = []
        for k, uid in enumerate(ids):
            units.append({
                "unit_id": int(uid), "tetrode": int(uid) // 1000, "cluster": int(uid) % 1000,
                "spikes": st_all[starts[k]:st_idx[k]],
                "electrodes": el[el_starts[k]:el_idx[k]].tolist(),
                "quality": _text(f["units/cluster_quality"][k]),
                "waveform": f["units/waveform_mean"][k],
            })
        ev_code = f["acquisition/task_events/data"][:]
        ev_t = f["acquisition/task_events/timestamps"][:]
        epochs = pd.DataFrame({
            "start": f["intervals/epochs/start_time"][:],
            "stop": f["intervals/epochs/stop_time"][:],
            "task": [_text(x) for x in f["intervals/epochs/task"][:]],
            "task_desc": [_text(x) for x in f["intervals/epochs/task_desc"][:]],
            "arena": [_text(x) for x in f["intervals/epochs/arena"][:]],
        })
        pos_ds = f["processing/behavior/position/animal_position/data"]
        pos = pos_ds[:] * pos_ds.attrs["conversion"] * 100.0          # cm
        pos_rate = float(f["processing/behavior/position/animal_position/starting_time"].attrs["rate"])
        pos_t0 = float(f["processing/behavior/position/animal_position/starting_time"][()])
        hd = f["processing/behavior/direction/head_direction/data"][:, 0]
        sp_ds = f["processing/behavior/speed/movement_speed/data"]
        stored_speed = sp_ds[:] * sp_ds.attrs["conversion"] * 100.0   # cm/s
        lfp_t = f["processing/ecephys/probe_0 - LFP/LFP/timestamps"]
        lfp_info = {"n": lfp_t.shape[0], "t_first": float(lfp_t[0]), "t_last": float(lfp_t[-1]),
                    "n_backward_steps": int((np.diff(lfp_t[:]) < 0).sum())}
        meta = {
            "subject": _text(f["general/subject/subject_id"]),
            "subject_description": _text(f["general/subject/description"]),
            "sex": _text(f["general/subject/sex"]),
            "session_start": _text(f["session_start_time"]),
            "description": desc,
            "electrode_location": _text(f["general/extracellular_ephys/electrodes/location"][0]),
        }
    on, off = ev_t[ev_code == 0], ev_t[ev_code == 1]
    t_pos = pos_t0 + np.arange(len(pos)) / pos_rate
    return {"path": path, "day": day, "session_no": session_no, "units": units,
            "ttl_on": on, "ttl_off": off, "epochs": epochs, "pos": pos, "hd": hd,
            "t_pos": t_pos, "pos_rate": pos_rate, "stored_speed": stored_speed,
            "lfp": lfp_info, **meta}


def load_all() -> list[dict]:
    return [load_session(p, u) for p, u in asset_urls()]


# ---------------------------------------------------------------- laser trials

def pulses(session: dict, reading: str = "onset", epoch: int | None = None) -> np.ndarray:
    """Pulse times: TTL onsets (reading a) or offsets (reading b), leaving out events longer than
    MAX_PULSE_S (the first event of each epoch, whose onset is the epoch start). `epoch` keeps the
    pulses of one PhotoStim epoch (0-based)."""
    on, off = session["ttl_on"], session["ttl_off"]
    keep = (off - on) < MAX_PULSE_S
    t = (on if reading == "onset" else off)[keep]
    if epoch is not None:
        ep = session["epochs"].iloc[epoch]
        t = t[(t >= ep.start) & (t <= ep.stop)]
    return t


def latency_fidelity(spikes: np.ndarray, pulse_t: np.ndarray, window: float = LATENCY_WINDOW_S) -> dict:
    """STAR Methods: latency is the mean time to the first spike within `window` over pulses that
    have one; fidelity the percentage of pulses that have one. Also the variant the claims file
    allows: the percentage of pulses preceded by a spike in the `window` before."""
    idx = np.searchsorted(spikes, pulse_t, side="right")
    nxt = np.where(idx < len(spikes), spikes[np.minimum(idx, len(spikes) - 1)], np.inf)
    lat = nxt - pulse_t
    hit = lat <= window
    idx_b = np.searchsorted(spikes, pulse_t, side="left") - 1
    prv = np.where(idx_b >= 0, spikes[np.maximum(idx_b, 0)], -np.inf)
    pre_hit = (pulse_t - prv) <= window
    return {"n_pulses": int(len(pulse_t)), "n_hit": int(hit.sum()),
            "latency_ms": float(lat[hit].mean() * 1000) if hit.any() else np.nan,
            "latency_median_ms": float(np.median(lat[hit]) * 1000) if hit.any() else np.nan,
            "fidelity_pct": 100.0 * hit.mean() if len(pulse_t) else np.nan,
            "pre_fidelity_pct": 100.0 * pre_hit.mean() if len(pulse_t) else np.nan}


def responsive(lf: dict, lat_range=(2.0, 4.0), min_fidelity: float = 11.64) -> bool:
    """Reading R-a of the claims file: latency in `lat_range` ms and fidelity at least 11.64%."""
    return bool(lat_range[0] <= lf["latency_ms"] <= lat_range[1] and lf["fidelity_pct"] >= min_fidelity)


# ---------------------------------------------------------------- open field

def open_field(session: dict, max_s: float | None = None) -> dict:
    """Smoothed positions and speed as in the archdata code (tracking.py), on the open-field span.
    `max_s` keeps only the first `max_s` seconds of the position series (the reading of the open
    field as the Methods' "approximately 30 min"); None keeps the whole series (the assumption)."""
    xy, hd, t = session["pos"], session["hd"], session["t_pos"]
    if max_s is not None:
        n = int(round(max_s * session["pos_rate"]))
        xy, hd, t = xy[:n], hd[:n], t[:n]
    xs = ndimage.gaussian_filter1d(xy[:, 0], POS_SIGMA_SAMPLES, mode="nearest")
    ys = ndimage.gaussian_filter1d(xy[:, 1], POS_SIGMA_SAMPLES, mode="nearest")
    dt = 1.0 / session["pos_rate"]
    speed = np.hstack([0, np.hypot(np.diff(xs), np.diff(ys)) / dt])
    speed = ndimage.gaussian_filter1d(speed, SPEED_SIGMA_SAMPLES)
    return {"t": t, "x": xs, "y": ys, "hd": hd % (2 * np.pi), "speed": speed,
            "t_end": t[-1] + dt, "duration": len(t) * dt}


def open_field_rate(spikes: np.ndarray, of: dict) -> float:
    s = spikes[(spikes >= of["t"][0]) & (spikes < of["t_end"])]
    return len(s) / of["duration"]


def spike_samples(spikes: np.ndarray, of: dict) -> np.ndarray:
    """Index of the tracking sample of each open-field spike."""
    s = spikes[(spikes >= of["t"][0]) & (spikes < of["t_end"])]
    return np.clip(np.round((s - of["t"][0]) * POS_RATE_HZ).astype(int), 0, len(of["t"]) - 1)


def _edges(of: dict):
    nx = int(np.ceil((of["x"].max() - of["x"].min()) / BIN_CM))
    ny = int(np.ceil((of["y"].max() - of["y"].min()) / BIN_CM))
    ex = of["x"].min() + BIN_CM * np.arange(nx + 1)
    ey = of["y"].min() + BIN_CM * np.arange(ny + 1)
    ex[-1] = max(ex[-1], of["x"].max() + 1e-9)
    ey[-1] = max(ey[-1], of["y"].max() + 1e-9)
    return ex, ey


def occupancy(of: dict):
    """Speed-filtered occupancy (s), raw and smoothed, with the bin edges."""
    ex, ey = _edges(of)
    fast = of["speed"] > SPEED_CUTOFF_CM_S
    occ, _, _ = np.histogram2d(of["x"][fast], of["y"][fast], bins=[ex, ey])
    occ = occ / POS_RATE_HZ
    return occ, ndimage.gaussian_filter(occ, RATE_SIGMA_BINS, mode="constant"), ex, ey


def rate_map(samples: np.ndarray, of: dict, occ_cache=None) -> np.ndarray:
    """Speed-filtered, smoothed rate map (Hz), NaN where the animal never was (archdata ratemap)."""
    occ, occ_s, ex, ey = occ_cache if occ_cache is not None else occupancy(of)
    samples = samples[of["speed"][samples] > SPEED_CUTOFF_CM_S]
    h, _, _ = np.histogram2d(of["x"][samples], of["y"][samples], bins=[ex, ey])
    h = ndimage.gaussian_filter(h, RATE_SIGMA_BINS, mode="constant")
    with np.errstate(invalid="ignore", divide="ignore"):
        rm = h / occ_s
    rm[occ == 0] = np.nan
    return rm


def autocorrelogram(rm: np.ndarray) -> np.ndarray:
    """Pearson spatial autocorrelogram over bins visited at both lags (Sargolini et al. 2006)."""
    v = np.isfinite(rm).astype(float)
    r = np.where(v > 0, rm, 0.0)

    def corr(a, b):
        return fftconvolve(a, b[::-1, ::-1], mode="full")

    n = np.round(corr(v, v))
    sx, sy = corr(r, v), corr(v, r)
    sxx, syy = corr(r * r, v), corr(v, r * r)
    sxy = corr(r, r)
    with np.errstate(invalid="ignore", divide="ignore"):
        num = n * sxy - sx * sy
        den = np.sqrt(n * sxx - sx ** 2) * np.sqrt(n * syy - sy ** 2)
        ac = num / den
    ac[n < MIN_OVERLAP_BINS] = np.nan
    return ac


def gridness(rm: np.ndarray) -> float:
    """Gridness score as Rowland et al. (2018) describe it (expanding circular samples)."""
    ac = autocorrelogram(rm)
    cy, cx = (np.array(ac.shape) - 1) / 2.0
    yy, xx = np.indices(ac.shape)
    dist = np.hypot(yy - cy, xx - cx)                     # in bins
    max_r = int(np.floor(dist.max()))
    prof = np.array([np.nanmean(ac[(dist >= k) & (dist < k + 1)]) for k in range(max_r)])
    peak_r = None
    for k in range(1, len(prof) - 1):
        if prof[k] < GRID_PEAK_THRESHOLD or (prof[k] < prof[k - 1] and prof[k] <= prof[k + 1]):
            peak_r = k
            break
    if peak_r is None:
        return np.nan
    valid = np.isfinite(ac)
    acz = np.where(valid, ac, 0.0)
    rots = {}
    for ang in (30, 60, 90, 120, 150):
        rots[ang] = (ndimage.rotate(acz, ang, reshape=False, order=1, mode="constant", cval=0.0),
                     ndimage.rotate(valid.astype(float), ang, reshape=False, order=0, mode="constant") > 0.5)
    r_min = peak_r + int(round(GRID_STEP_BEYOND_PEAK_CM / BIN_CM))
    r_max = int(round(GRID_MAX_RADIUS_CM / BIN_CM))
    best = -np.inf
    for R in range(r_min, r_max + 1):
        ring = (dist > peak_r) & (dist <= R) & valid
        c = {}
        for ang, (rot, rvalid) in rots.items():
            m = ring & rvalid
            if m.sum() < 10:
                c[ang] = np.nan
                continue
            c[ang] = np.corrcoef(acz[m], rot[m])[0, 1]
        score = min(c[60], c[120]) - max(c[30], c[90], c[150])
        if np.isfinite(score):
            best = max(best, score)
    return best if np.isfinite(best) else np.nan


def hd_tuning(samples: np.ndarray, of: dict, sel: np.ndarray | None = None, smooth: bool = True,
              n_bins: int = HD_BINS, sigma: float = HD_SIGMA_BINS):
    """Head-direction tuning (Hz) in 180 bins, smoothed circularly with sigma 2 bins (archdata
    hd_tuning_curve; it applies no speed filter). `sel` restricts tracking samples (for halves).
    `n_bins` and `sigma` are changed only to show other readings of the tuning curve."""
    hd = of["hd"]
    if sel is None:
        sel = np.ones(len(hd), bool)
    edges = np.linspace(0, 2 * np.pi, n_bins + 1)
    occ, _ = np.histogram(hd[sel], bins=edges)
    s = samples[sel[samples]]
    cnt, _ = np.histogram(hd[s], bins=edges)
    with np.errstate(invalid="ignore", divide="ignore"):
        tc = cnt / (occ / POS_RATE_HZ)
    tc[occ == 0] = 0.0
    if smooth and sigma > 0:
        tc = ndimage.gaussian_filter1d(np.tile(tc, 3), sigma, mode="nearest")[n_bins:2 * n_bins]
    centers = edges[:-1] + np.pi / n_bins
    return centers, tc


def mean_vector_length(centers: np.ndarray, rates: np.ndarray) -> float:
    """|sum(rate * exp(i theta))| / sum(rate) (Rowland et al. 2018, Methods)."""
    return float(np.abs(np.sum(rates * np.exp(1j * centers))) / np.sum(rates))


def hd_stability(samples: np.ndarray, of: dict) -> float:
    half = len(of["t"]) // 2
    first = np.zeros(len(of["t"]), bool)
    first[:half] = True
    _, a = hd_tuning(samples, of, first)
    _, b = hd_tuning(samples, of, ~first)
    return float(np.corrcoef(a, b)[0, 1])


def border_score(rm: np.ndarray) -> float:
    """Solstad et al. (2008) as Rowland et al. (2018) describe it: (cM - dM) / (cM + dM), cM the
    largest fraction of one wall covered by one field, dM the rate-weighted mean distance of field
    bins to the nearest wall, divided by half the shorter side. Walls are the edges of the map."""
    peak = np.nanmax(rm)
    if not np.isfinite(peak) or peak <= 0:
        return np.nan
    above = np.nan_to_num(rm, nan=0.0) > FIELD_FRACTION * peak
    lab, n = ndimage.label(above)
    min_bins = FIELD_MIN_AREA_CM2 / BIN_CM ** 2
    fields = [k for k in range(1, n + 1) if (lab == k).sum() >= min_bins]
    if not fields:
        return np.nan
    nx, ny = rm.shape
    visited = np.isfinite(rm)
    walls = [(0, slice(None)), (nx - 1, slice(None)), (slice(None), 0), (slice(None), ny - 1)]
    cm = 0.0
    for k in fields:
        f = lab == k
        for w in walls:
            wv = visited[w]
            if wv.sum() == 0:
                continue
            cm = max(cm, (f[w] & wv).sum() / wv.sum())
    ii, jj = np.indices(rm.shape)
    d_wall = np.minimum.reduce([ii + 0.5, nx - ii - 0.5, jj + 0.5, ny - jj - 0.5])
    in_f = np.isin(lab, fields)
    w = np.nan_to_num(rm, nan=0.0)[in_f]
    dm = np.sum(d_wall[in_f] * w) / np.sum(w) / (min(nx, ny) / 2.0)
    return float((cm - dm) / (cm + dm))


def scores(samples: np.ndarray, of: dict, occ_cache=None) -> dict:
    rm = rate_map(samples, of, occ_cache)
    centers, tc = hd_tuning(samples, of)
    return {"gridness": gridness(rm), "mvl": mean_vector_length(centers, tc),
            "border": border_score(rm)}


def shuffled_scores(spikes: np.ndarray, of: dict, reading: str, rng: np.random.Generator,
                    n: int = N_SHUFFLES) -> pd.DataFrame:
    """Scores of `n` shuffles: the open-field spike train shifted along the path with wrap-around.
    reading `literal`: shift uniform in [-20, 20] s; `standard`: uniform in [20, T - 20] s."""
    t0, T = of["t"][0], of["duration"]
    s = spikes[(spikes >= t0) & (spikes < of["t_end"])] - t0
    occ_cache = occupancy(of)
    rows = []
    for _ in range(n):
        if reading == "literal":
            shift = rng.uniform(-SHUFFLE_MIN_S, SHUFFLE_MIN_S)
        else:
            shift = rng.uniform(SHUFFLE_MIN_S, T - SHUFFLE_MIN_S)
        sh = np.sort((s + shift) % T) + t0
        rows.append(scores(spike_samples(sh, of), of, occ_cache))
    return pd.DataFrame(rows)


def classify(spikes: np.ndarray, of: dict, rng_seed: int) -> dict:
    """Scores, shuffle thresholds under both readings, and the classes of Rowland et al. (2018)."""
    samples = spike_samples(spikes, of)
    obs = scores(samples, of)
    obs["hd_stability"] = hd_stability(samples, of)
    out = dict(obs)
    for k, reading in enumerate(("literal", "standard")):
        sh = shuffled_scores(spikes, of, reading, np.random.default_rng(rng_seed + k))
        thr = sh.quantile(SHUFFLE_PERCENTILE / 100.0)
        out[f"thr_grid_{reading}"] = thr["gridness"]
        out[f"thr_mvl_{reading}"] = thr["mvl"]
        out[f"thr_border_{reading}"] = thr["border"]
        out[f"grid_{reading}"] = bool(obs["gridness"] > thr["gridness"])
        out[f"hd_{reading}"] = bool(obs["mvl"] > thr["mvl"] and obs["hd_stability"] > HD_STABILITY_MIN)
        out[f"border_{reading}"] = bool(obs["border"] > thr["border"])
    return out
