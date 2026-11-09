"""Loading and measures for dandiset 000552 (Huszar, Zhang, Blockus & Buzsaki 2022).

Huszar R, Zhang Y, Blockus H, Buzsaki G (2022). Preconfigured dynamics in the hippocampus are
guided by embryonic birthdate and rate of neurogenesis. Nature Neuroscience 25, 1201-1212.
doi:10.1038/s41593-022-01138-x.

The dandiset holds one `behavior+ecephys` NWB file per recording session (104 files, 17 mice) and
13 `raw_ecephys` files. A processed file holds sleep states, detected sharp-wave ripples
(SPW-Rs) and, in 65 of them, spike-sorted units with their spike times, the animal's position
(x, y and linearized, in cm) and the figure-eight maze trials. Units carry no cell type and no
light-responsiveness label. Files are streamed from the archive at the pinned version; nothing is
written to disk.

Each file is reduced as it loads: spike times are kept only inside the maze recordings (with a
margin for the time-shift check), plus per-unit counts by sleep state and a peri-ripple
histogram of the population.

Where the parameters come from:

- From the paper's Methods: spatial bins of 1 cm, only moments with speed above 1.5 cm/s,
  Gaussian smoothing of spike counts and occupancy with 9 cm full width at half maximum (FWHM),
  rate map = smoothed counts / smoothed occupancy, never-visited bins excluded; left and right
  trials mapped separately and concatenated; Pearson correlation of maps; spatial information in
  bits/s after Skaggs et al. (1993); SPW-R duration limits of 20 to 200 ms; 30 Hz tracking.
- From the paper's code (https://github.com/rhuszar/optotagCA1_final, commit
  51320d45c5ee41147048128df333f251379bf755), where the Methods are silent: the figure-eight
  trial spans 205 one-cm bins; its segments for Figure 5e are stem (bins 1-74), turn 1 (75-111),
  arm (112-185) and turn 2 (186-205) (`ratemap_remap.m`); the stem is excluded from ratemap
  correlations, keeping bins 75-205 on the familiar figure-eight and 51-164 on the novel T-maze
  (`get_corrBeh_famnov.m`); linear tracks keep all bins.
- Common choices made here, as the paper's are not available from the dandiset: speed is the
  absolute derivative of the linearized position smoothed with a Gaussian of 0.2 s s.d. (the
  paper uses a Kalman filter); putative pyramidal cells are units with a session mean firing rate
  of at most `PYR_MAX_RATE_HZ` (the paper classifies by waveform shape and autocorrelogram, which
  the dandiset does not hold); the "theta-related" firing rate is approximated by the firing rate
  while running at `RUN_SPEED_CM_S` or faster inside maze trials (the paper counts spikes in
  detected theta cycles of the LFP).
- Monosynaptic connections (used only to show what a test of Figure 7f would take): CCGs in
  0.8 ms bins, a baseline from a hollowed Gaussian of 15 ms s.d., alpha 0.001 Bonferroni-corrected,
  and a comparison of the peak with the anticausal bins, from the Methods (after English et al.
  2017); the hollow fraction of 0.6 and the three lag bins of 0.8 to 3.2 ms are common choices.
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy.ndimage import gaussian_filter1d

DANDISET_ID = "000552"
DANDISET_VERSION = "0.230630.2304"

BIN_CM = 1.0
MIN_SPEED_CM_S = 1.5            # Methods
SMOOTH_FWHM_CM = 9.0            # Methods (linear mazes)
SPEED_SMOOTH_S = 0.2            # common choice; the paper uses a Kalman filter
FIG8_BINS = 205                 # code: 205 one-cm bins per figure-eight trial (Methods: 205 cm)
FIG8_SEGMENTS = {"stem": (1, 74), "turn1": (75, 111), "arm": (112, 185), "turn2": (186, 205)}
FIG8_POST_STEM = (75, 205)      # code, 1-based inclusive
TMAZE_POST_STEM = (51, 164)     # code, novel T-maze
PYR_MAX_RATE_HZ = 5.0           # common choice; no cell type in the dandiset
RUN_SPEED_CM_S = 5.0            # common choice for the theta-rate proxy
CCG_BIN_S = 0.0008              # Methods: 0.8 ms bins
CCG_HALF_WINDOW_S = 0.1         # common choice (the code's CCG duration of 0.2 s)
CCG_BASELINE_SD_S = 0.015       # Methods: hollowed Gaussian of 15 ms s.d. (the reliability test)
CCG_HOLLOW = 0.6                # common choice (Stark & Abeles 2009)
MONO_BINS = 3                   # Methods: three bins; their lags (0.8 to 3.2 ms) a common choice
MONO_ALPHA = 0.001              # Methods
MONO_PEAK_MAX_LAG_BINS = 5      # variant: peak sought at lags up to 4.0 ms (not stated in the Methods)
SHIFT_MARGIN_S = 5.0            # spikes kept this far around the maze recordings
RIPPLE_PSTH_EDGES = np.arange(-0.5, 0.5001, 0.01)
RIPPLE_SHUFFLE_SEED = 0

_FWHM_TO_SD = 1.0 / (2.0 * np.sqrt(2.0 * np.log(2.0)))


def _dec(v):
    return v.decode() if isinstance(v, bytes) else v


def birthdate_of(subject_id: str) -> str:
    """Embryonic day of electroporation, from the subject id (e13 -> E13.5). The files hold it nowhere else."""
    return f"E{subject_id.split('_')[0][1:]}.5"


def list_assets() -> pd.DataFrame:
    """All files of the pinned version, with their kind and size."""
    ds = DandiAPIClient().get_dandiset(DANDISET_ID, DANDISET_VERSION)
    rows = []
    for a in ds.get_assets():
        rows.append({"path": a.path, "size": a.size, "size_gb": a.size / 1e9, "asset": a,
                     "kind": "raw" if "raw_ecephys" in a.path else "processed",
                     "subject": a.path.split("/")[0].replace("sub-", "")})
    return pd.DataFrame(rows).sort_values("path").reset_index(drop=True)


def open_asset(asset) -> h5py.File:
    url = asset.get_content_url(follow_redirects=1, strip_query=True)
    return h5py.File(remfile.File(url), "r")


def _intervals(group) -> tuple[np.ndarray, np.ndarray]:
    return group["start_time"][:], group["stop_time"][:]


def _in_intervals(t: np.ndarray, starts: np.ndarray, stops: np.ndarray) -> np.ndarray:
    """Boolean mask of sorted times t falling inside any [start, stop) interval."""
    mask = np.zeros(len(t), bool)
    for a, b in zip(starts, stops):
        i, j = np.searchsorted(t, [a, b])
        mask[i:j] = True
    return mask


def _segments(ts: np.ndarray, gap_s: float = 60.0) -> list[tuple[int, int]]:
    """Index ranges of the position series separated by gaps longer than gap_s (one per maze recording)."""
    cuts = np.where(np.diff(ts) > gap_s)[0] + 1
    bounds = np.r_[0, cuts, len(ts)]
    return [(int(bounds[i]), int(bounds[i + 1])) for i in range(len(bounds) - 1)]


def speed_from_linear(ts: np.ndarray, lin: np.ndarray, trial_id: np.ndarray) -> np.ndarray:
    """Speed (cm/s) from the linearized position, smoothed within each trial; NaN outside trials."""
    speed = np.full(len(ts), np.nan)
    for k in np.unique(trial_id[trial_id >= 0]):
        idx = np.where(trial_id == k)[0]
        if len(idx) < 5:
            continue
        dt = np.median(np.diff(ts[idx]))
        x = gaussian_filter1d(lin[idx], SPEED_SMOOTH_S / dt, mode="nearest")
        speed[idx] = np.abs(np.gradient(x, ts[idx]))
    return speed


def load_session(asset, with_units: bool = True) -> dict:
    """Read one processed file and reduce it to what the analyses use."""
    f = open_asset(asset)
    s = {"path": asset.path, "session_id": _dec(f["general/session_id"][()]),
         "subject": _dec(f["general/subject/subject_id"][()]), "sex": _dec(f["general/subject/sex"][()]),
         "age": _dec(f["general/subject/age"][()]), "start": _dec(f["session_start_time"][()])}
    s["birthdate"] = birthdate_of(s["subject"])
    # what the file holds, for the record of what is missing
    s["groups"] = {g: sorted(f[g].keys()) for g in ("acquisition", "stimulus/presentation", "analysis",
                                                     "intervals", "processing") if g in f}
    s["processing"] = {m: sorted(f["processing"][m].keys()) for m in f["processing"]}
    s["units_columns"] = sorted(f["units"].keys()) if "units" in f else []
    s["electrode_groups"] = sorted(k for k in f["general/extracellular_ephys"].keys() if k != "electrodes") \
        if "general/extracellular_ephys" in f else []
    if "processing/ecephys/LFP/ElectricalSeriesLFP" in f:
        e = f["processing/ecephys/LFP/ElectricalSeriesLFP"]
        s["lfp"] = {"shape": e["data"].shape, "rate": float(e["starting_time"].attrs["rate"]),
                    "conversion": float(e["data"].attrs["conversion"])}

    ss = f["processing/behavior/SleepStates"]
    st, sp = _intervals(ss)
    s["states"] = pd.DataFrame({"label": [_dec(x) for x in ss["label"][:]], "start": st, "stop": sp})

    rp = f["processing/ecephys/Ripples"]
    s["ripples"] = pd.DataFrame({"start": rp["start_time"][:], "stop": rp["stop_time"][:],
                                 "peak": rp["peaks"][:], "duration": rp["ripple_durations"][:]})
    s["end_s"] = float(max(sp.max(), s["ripples"]["stop"].max()))

    s["has_units"] = "units" in f
    s["has_position"] = "processing/behavior/LinearizedPosition" in f
    if s["has_position"]:
        t = f["intervals/trials"]
        trials = pd.DataFrame({k: [_dec(x) for x in t[k][:]] for k in t.keys() if k != "id"})
        trials["recordings"] = trials["recordings"].astype(int)
        s["trials"] = trials
        lp = f["processing/behavior/LinearizedPosition/LinearizedSpatialSeries"]
        ts, lin = lp["timestamps"][:], lp["data"][:]
        xy = f["processing/behavior/SubjectPosition/SpatialSeries/data"][:]
        s["pos_unit"] = lp["data"].attrs.get("unit")
        good = np.isfinite(trials.start_time.values) & np.isfinite(trials.stop_time.values)
        trial_id = np.full(len(ts), -1)
        for k in np.where(good)[0]:
            i, j = np.searchsorted(ts, [trials.start_time.iloc[k], trials.stop_time.iloc[k]])
            trial_id[i:j] = k
        s["pos"] = pd.DataFrame({"t": ts, "lin": lin, "x": xy[:, 0], "y": xy[:, 1], "trial": trial_id})
        s["pos"]["speed"] = speed_from_linear(ts, lin, trial_id)
        s["pos_segments"] = [(float(ts[a]), float(ts[b - 1])) for a, b in _segments(ts)]
        if "intervals/epochs" in f:
            s["epochs"] = pd.DataFrame({"start": f["intervals/epochs/start_time"][:],
                                        "stop": f["intervals/epochs/stop_time"][:]})

    if s["has_units"] and with_units:
        u = f["units"]
        idx = u["spike_times_index"][:]
        all_t = u["spike_times"][:]
        bounds = np.r_[0, idx]
        s["unit_names"] = [_dec(x) for x in u["unit_name"][:]]
        s["unit_groups"] = [_dec(x) for x in u["group_id"][:]]
        s["clu_ids"] = u["clu_id"][:]
        n = len(idx)
        s["n_spikes"] = np.diff(bounds)
        s["spikes_sorted"] = bool(all(np.all(np.diff(all_t[bounds[i]:bounds[i + 1]]) >= 0) for i in range(n)))
        s["first_spike"] = float(all_t.min()) if len(all_t) else np.nan
        s["last_spike"] = float(all_t.max()) if len(all_t) else np.nan
        # per-unit spike counts and durations by sleep state
        counts = {}
        for lab in s["states"].label.unique():
            sel = s["states"][s["states"].label == lab]
            counts[lab] = np.array([_in_intervals(all_t[bounds[i]:bounds[i + 1]], sel.start.values,
                                                  sel.stop.values).sum() for i in range(n)])
        s["state_counts"] = counts
        s["state_durations"] = s["states"].assign(d=lambda d: d.stop - d.start).groupby("label").d.sum().to_dict()
        # peri-ripple histogram of all spikes, and the same around random times in the same states
        pk = s["ripples"]["peak"].values
        pooled = np.sort(all_t)
        def psth(centres):
            h = np.zeros(len(RIPPLE_PSTH_EDGES) - 1)
            for c in centres:
                i, j = np.searchsorted(pooled, [c - 0.5, c + 0.5])
                h += np.histogram(pooled[i:j] - c, RIPPLE_PSTH_EDGES)[0]
            return h / len(centres) / np.diff(RIPPLE_PSTH_EDGES)
        rng = np.random.default_rng(RIPPLE_SHUFFLE_SEED)
        s["ripple_psth"] = psth(pk)
        s["ripple_psth_shuffled"] = psth(pk + rng.uniform(-60, 60, len(pk)))
        # spikes kept around the maze recordings only
        if s["has_position"]:
            keep = [(a - SHIFT_MARGIN_S, b + SHIFT_MARGIN_S) for a, b in s["pos_segments"]]
            ka, kb = np.array(keep).T
            s["maze_spikes"] = [all_t[bounds[i]:bounds[i + 1]][_in_intervals(all_t[bounds[i]:bounds[i + 1]], ka, kb)]
                                for i in range(n)]
        del all_t
    f.close()
    return s


def load_all(paths: list[str] | None = None, with_units: bool = True, workers: int = 6) -> list[dict]:
    """Load the processed files (all, or those listed), in path order."""
    assets = list_assets()
    assets = assets[assets.kind == "processed"]
    if paths is not None:
        assets = assets[assets.path.isin(paths)]
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(lambda a: load_session(a, with_units), assets.asset))


# --- maze recordings and rate maps ------------------------------------------------------------

def recordings(s: dict) -> list[dict]:
    """The maze recordings of a session: trials of one `recordings` value, with their position.

    The recording run first in the session is the familiar figure-eight (Methods). The length of a
    recording's track is taken from the largest linearized position inside its trials.
    """
    out = []
    tr = s["trials"]
    for r in sorted(tr.recordings.unique()):
        rows = tr[(tr.recordings == r) & tr.start_time.notna() & tr.stop_time.notna()]
        ids = rows.index.values
        pos = s["pos"][s["pos"].trial.isin(ids)]
        out.append({"recording": int(r), "trials": rows, "pos": pos,
                    "start": float(rows.start_time.min()), "stop": float(rows.stop_time.max()),
                    "track_max_cm": float(np.nanmax(pos.lin)) if len(pos) else np.nan})
    first = min(out, key=lambda d: d["start"])
    for d in out:
        d["familiar"] = d is first
        L = d["track_max_cm"]
        d["kind"] = ("figure-eight" if d["familiar"] else
                     "T-maze" if L > 150 else "linear track")
        d["n_bins"] = FIG8_BINS if d["familiar"] else int(np.ceil(L / BIN_CM))
    return out


def _smooth(v: np.ndarray, fwhm_bins: float) -> np.ndarray:
    return gaussian_filter1d(v.astype(float), fwhm_bins * _FWHM_TO_SD, mode="constant")


def rate_maps(spikes: list[np.ndarray], rec: dict, shift_s: float = 0.0,
              min_speed: float = MIN_SPEED_CM_S) -> dict:
    """Left and right rate maps (Hz) of every unit on one recording, per 1-cm bin.

    Occupancy and spike counts are taken at moments with speed above `min_speed`, inside trials;
    a spike is placed at the position sample nearest in time. Returns maps of shape
    (units, 2, bins), the occupancy (2, bins) in s, and a mask of visited bins.
    """
    pos = rec["pos"]
    n_bins = rec["n_bins"]
    edges = np.arange(n_bins + 1) * BIN_CM
    dt = np.median(np.diff(pos.t.values))
    arm = rec["trials"].visited_arm.reindex(pos.trial.values).values
    moving = (pos.speed.values > min_speed) & np.isfinite(pos.lin.values)
    occ = np.zeros((2, n_bins))
    counts = np.zeros((len(spikes), 2, n_bins))
    pos_t = pos.t.values
    pos_bin = np.clip(np.digitize(pos.lin.values, edges) - 1, 0, n_bins - 1)
    for side, name in enumerate(["left", "right"]):
        sel = moving & (arm == name)
        occ[side] = np.bincount(pos_bin[sel], minlength=n_bins)[:n_bins] * dt
        # trial intervals of this side, to keep spikes inside them
        rows = rec["trials"][rec["trials"].visited_arm == name]
        for u, t in enumerate(spikes):
            tt = t - shift_s
            inside = _in_intervals(tt, rows.start_time.values, rows.stop_time.values)
            tt = tt[inside]
            if not len(tt):
                continue
            k = np.clip(np.searchsorted(pos_t, tt), 1, len(pos_t) - 1)
            k -= (tt - pos_t[k - 1]) < (pos_t[k] - tt)
            ok = sel[k]
            counts[u, side] = np.bincount(pos_bin[k[ok]], minlength=n_bins)[:n_bins]
    fw = SMOOTH_FWHM_CM / BIN_CM
    occ_s = np.stack([_smooth(o, fw) for o in occ])
    visited = occ > 0
    with np.errstate(invalid="ignore", divide="ignore"):
        maps = np.stack([[_smooth(c, fw) for c in cu] for cu in counts]) / occ_s[None]
    maps[:, ~visited] = np.nan
    return {"maps": maps, "occupancy": occ, "visited": visited}


def correlation_bins(rec: dict) -> np.ndarray:
    """1-based bins used for ratemap correlations: post-stem on the figure-eight and T-maze, all on linear tracks."""
    if rec["kind"] == "figure-eight":
        a, b = FIG8_POST_STEM
    elif rec["kind"] == "T-maze":
        a, b = TMAZE_POST_STEM
    else:
        a, b = 1, rec["n_bins"]
    return np.arange(a, min(b, rec["n_bins"]) + 1)


def concatenated(maps: np.ndarray, bins_1based: np.ndarray) -> np.ndarray:
    """Left and right maps over the given bins, concatenated: (units, 2 * len(bins))."""
    i = bins_1based - 1
    return np.concatenate([maps[:, 0, i], maps[:, 1, i]], axis=1)


def pairwise_map_correlations(cat: np.ndarray) -> np.ndarray:
    """Pearson correlations of every unit pair over the bins visited in both trial types (upper triangle)."""
    ok = np.all(np.isfinite(cat), axis=0)
    x = cat[:, ok]
    with np.errstate(invalid="ignore", divide="ignore"):
        c = np.corrcoef(x)
    iu = np.triu_indices(len(cat), 1)
    return c[iu]


def skaggs_information(maps: np.ndarray, occ: np.ndarray) -> np.ndarray:
    """Spatial information in bits/s (Skaggs et al. 1993), over left and right maps together."""
    p = occ / occ.sum()
    out = np.full(len(maps), np.nan)
    for u, m in enumerate(maps):
        ok = np.isfinite(m) & (p > 0)
        lam = np.sum(p[ok] * m[ok])
        if lam <= 0:
            continue
        r = m[ok]
        with np.errstate(divide="ignore", invalid="ignore"):
            terms = np.where(r > 0, p[ok] * r * np.log2(r / lam), 0.0)
        out[u] = terms.sum()
    return out


def uniform_information(maps: np.ndarray) -> np.ndarray:
    """The paper code's variant: mean over bins of r log2(r / mean r), without occupancy weights (bits/s)."""
    out = np.full(len(maps), np.nan)
    for u, m in enumerate(maps):
        r = m[np.isfinite(m)]
        mu = r.mean() if len(r) else 0
        if mu <= 0:
            continue
        with np.errstate(divide="ignore", invalid="ignore"):
            out[u] = np.nanmean(np.where(r > 0, r * np.log2(r / mu), 0.0))
    return out


def running_rate(spikes: list[np.ndarray], rec: dict, min_speed: float = RUN_SPEED_CM_S) -> np.ndarray:
    """Firing rate (Hz) of each unit while running at min_speed or faster inside the recording's trials.

    Consecutive running samples form a stretch, which ends where running stops, the trial changes or
    a sample is missing, so the time between trials is never counted. Each stretch spans half a
    sample interval beyond its first and last samples; the rate is the spike count inside the
    stretches over their summed length.
    """
    pos = rec["pos"]
    t = pos.t.values
    dt = np.median(np.diff(t))
    run = pos.speed.values >= min_speed
    cut = np.r_[True, (np.diff(pos.trial.values) != 0) | (np.diff(t) > 1.5 * dt)]
    first = run & (cut | ~np.r_[False, run[:-1]])
    last = run & (np.r_[cut[1:], True] | ~np.r_[run[1:], False])
    starts, stops = t[first] - dt / 2, t[last] + dt / 2
    total = float(np.sum(stops - starts))
    if total <= 0:
        return np.full(len(spikes), np.nan)
    return np.array([_in_intervals(x, starts, stops).sum() / total for x in spikes])


def spike_trains(asset) -> list[np.ndarray]:
    """All spike times of every unit of one processed file (s)."""
    f = open_asset(asset)
    idx = f["units/spike_times_index"][:]
    all_t = f["units/spike_times"][:]
    f.close()
    bounds = np.r_[0, idx]
    return [all_t[bounds[i]:bounds[i + 1]] for i in range(len(idx))]


def ccg_counts(pre: np.ndarray, post: np.ndarray, bin_s: float = CCG_BIN_S,
               half_window_s: float = CCG_HALF_WINDOW_S) -> np.ndarray:
    """Cross-correlogram: counts of post spikes at each lag from pre spikes, bins centred on 0."""
    n = int(round(half_window_s / bin_s))
    edges = (np.arange(-n, n + 2) - 0.5) * bin_s
    lo = np.searchsorted(post, pre + edges[0])
    hi = np.searchsorted(post, pre + edges[-1])
    k = hi - lo
    if k.sum() == 0:
        return np.zeros(2 * n + 1)
    rep = np.repeat(np.arange(len(pre)), k)
    j = np.arange(k.sum()) - np.repeat(np.cumsum(k) - k, k) + lo[rep]
    return np.histogram(post[j] - pre[rep], edges)[0].astype(float)


def hollowed_baseline(ccg: np.ndarray, bin_s: float = CCG_BIN_S, sd_s: float = CCG_BASELINE_SD_S,
                      hollow: float = CCG_HOLLOW) -> np.ndarray:
    """The CCG smoothed with a partially hollowed Gaussian (Stark & Abeles 2009), edges reflected."""
    sd = sd_s / bin_s
    x = np.arange(-int(4 * sd), int(4 * sd) + 1)
    w = np.exp(-x ** 2 / (2 * sd ** 2))
    w[len(x) // 2] *= 1 - hollow
    w /= w.sum()
    pad = len(x) // 2
    y = np.r_[ccg[pad:0:-1], ccg, ccg[-2:-pad - 2:-1]]
    return np.convolve(y, w, mode="valid")


def is_monosynaptic(ccg: np.ndarray, bin_s: float = CCG_BIN_S, alpha: float = MONO_ALPHA) -> bool:
    """Excitatory pre-to-post connection by the test of English et al. (2017), as the Methods describe.

    The bins at lags 0.8 to 3.2 ms (three bins of 0.8 ms) are tested against the hollowed-Gaussian
    baseline, and their peak against the largest of the bins at the same negative lags, each with a
    Poisson test at alpha Bonferroni-corrected over the three bins.
    """
    from scipy.stats import poisson
    c = len(ccg) // 2
    win = np.arange(c + 1, c + 1 + MONO_BINS)
    anti = np.arange(c - MONO_BINS, c)
    base = hollowed_baseline(ccg, bin_s)
    a = alpha / MONO_BINS
    p_base = poisson.sf(ccg[win] - 1, np.maximum(base[win], 1e-12))
    peak = ccg[win].max()
    p_anti = poisson.sf(peak - 1, max(ccg[anti].max(), 1e-12))
    return bool(np.any(p_base < a) and p_anti < a)


def is_monosynaptic_peak(ccg: np.ndarray, bin_s: float = CCG_BIN_S, alpha: float = MONO_ALPHA,
                         max_lag_bins: int = MONO_PEAK_MAX_LAG_BINS) -> bool:
    """The same test on the three bins centred on the CCG peak, as the Methods word it.

    The peak is the largest bin at lags 0.8 to 4.0 ms (bins 1 to 5); the bins either side of it are
    tested with it against the baseline, and the peak against the largest bin at the same negative
    lags.
    """
    from scipy.stats import poisson
    c = len(ccg) // 2
    pk = c + 1 + int(np.argmax(ccg[c + 1:c + 1 + max_lag_bins]))
    win = np.arange(pk - 1, pk + 2)
    anti = 2 * c - win
    base = hollowed_baseline(ccg, bin_s)
    a = alpha / len(win)
    p_base = poisson.sf(ccg[win] - 1, np.maximum(base[win], 1e-12))
    p_anti = poisson.sf(ccg[pk] - 1, max(ccg[anti].max(), 1e-12))
    return bool(np.any(p_base < a) and p_anti < a)


def raw_file_info(asset) -> dict:
    """Shapes and rates of the series in a raw_ecephys file, and its session start time."""
    f = open_asset(asset)
    out = {"path": asset.path, "start": _dec(f["session_start_time"][()])}
    for name, key in (("raw", "acquisition/ElectricalSeries"), ("lfp", "processing/ecephys/LFP/ElectricalSeriesLFP")):
        if key in f:
            out[name + "_shape"] = f[key]["data"].shape
            out[name + "_rate"] = float(f[key]["starting_time"].attrs["rate"])
    f.close()
    return out


def lfp_samples(asset, start: int, n: int, channel: int) -> np.ndarray:
    """A short stretch of one LFP channel (raw integer values)."""
    f = open_asset(asset)
    x = f["processing/ecephys/LFP/ElectricalSeriesLFP/data"][start:start + n, channel]
    f.close()
    return x


def mean_rates(s: dict) -> np.ndarray:
    """Session mean firing rate of each unit: spike count over the session length (Hz)."""
    return s["n_spikes"] / s["end_s"]
