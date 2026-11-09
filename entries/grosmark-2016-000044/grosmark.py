"""Loading and measures for dandiset 000044 (Grosmark & Buzsaki 2016, Science 351:1440).

The dandiset holds eight sessions from four rats. Each file covers PRE sleep in the home cage,
a MAZE epoch on a novel track, and POST sleep, with sorted units (`cell_type` excitatory or
inhibitory), LFP at 1250 Hz on 128 channels, sleep states and the position on the track.

Every file is streamed from the archive at a pinned version. `prepare_session` reduces a file
to what the analysis needs: spike times of every unit, the epochs, the sleep states, the
positions, one LFP channel's ripple envelope at the candidate events, and the outputs of the
data checks.

Where parameters come from. The paper's supplementary Materials and Methods could not be read
(see the notebook), so the parameters below are common choices in the hippocampal replay
literature unless marked otherwise:

- 20 ms decoding bins: the paper's main text (Results, paragraph 2).
- 100 ms bins for pairwise coactivation and windows of 20% of cells stepped by 1%: the legend
  of Figure 4.
- Speed threshold 5 cm/s, 2 cm position bins, 4 cm Gaussian smoothing, 1 Hz peak for a place
  cell, field threshold 20% of peak: common choices.
- Ripple band 150 to 250 Hz, envelope smoothed with an 8 ms Gaussian, threshold 3 SD over
  non-REM sleep; population bursts from all units in 1 ms bins, 10 ms Gaussian, peak z >= 3,
  bounded at z = 0, 50 to 500 ms: common choices.
- Burst ISI 6 ms: a common choice for CA1 pyramidal cells.
- 200 column-cycle shuffles for rZ (50 when templates are re-decoded for variants), 20
  circular shifts per cell and event for PCC, drawn afresh for every event: choices made here.
"""

from __future__ import annotations

import numpy as np
import h5py
import remfile
from scipy import signal
from scipy.ndimage import gaussian_filter1d

DANDISET = "000044"
VERSION = "0.261005.2101"
LFP_RATE = 1250.0

BIN_CM = 2.0            # position bin (cm)
SMOOTH_BINS = 2.0       # Gaussian SD of the rate map smoothing, in bins (4 cm)
RUN_SPEED = 5.0         # cm/s
PLACE_PEAK = 1.0        # Hz
DECODE_BIN = 0.02       # s, from the paper
MIN_ACTIVE = 5          # active template cells per event
N_SHUFFLE = 200         # column-cycle shuffles per event
N_PCC_SHIFT = 20        # circular shifts per cell and event for PCC
BURST_ISI = 0.006       # s


# ----------------------------------------------------------------------------- access

def asset_urls(version: str = VERSION) -> list[tuple[str, str]]:
    """(path, S3 URL) of every NWB file of the dandiset version, sorted by path."""
    from dandi.dandiapi import DandiAPIClient
    with DandiAPIClient() as client:
        ds = client.get_dandiset(DANDISET, version)
        assets = sorted(ds.get_assets(), key=lambda a: a.path)
        return [(a.path, a.get_content_url(follow_redirects=1, strip_query=True)) for a in assets]


def open_nwb(url: str) -> h5py.File:
    return h5py.File(remfile.File(url), "r")


def _text(values) -> list[str]:
    return [v.decode() if isinstance(v, bytes) else str(v) for v in values]


# ----------------------------------------------------------------------------- loading

def load_session(f: h5py.File) -> dict:
    """Everything but the LFP, from an open file."""
    s = {"session": f["general/session_id"][()].decode(),
         "subject": f["general/subject/subject_id"][()].decode()}
    ep = f["intervals/epochs"]
    s["epochs"] = {lab: (float(a), float(b)) for lab, a, b in
                   zip(_text(ep["label"][:]), ep["start_time"][:], ep["stop_time"][:])}
    st = f["processing/behavior/states"]
    s["states"] = {"label": np.array(_text(st["label"][:])),
                   "start": st["start_time"][:].astype(float),
                   "stop": st["stop_time"][:].astype(float)}
    u = f["units"]
    idx = u["spike_times_index"][:]
    times = u["spike_times"][:]
    s["spikes"] = np.split(times, idx[:-1])
    s["unit_id"] = u["id"][:]
    s["cell_type"] = np.array(_text(u["cell_type"][:]))
    s["location"] = np.array(_text(u["location"][:]))
    s["shank_id"] = u["shank_id"][:]
    beh = f["processing/behavior"]
    for name in beh:
        if name == "states":
            continue
        for sub in beh[name]:
            g = beh[name][sub]
            n = g["data"].shape[0]
            rate = float(g["starting_time"].attrs["rate"])
            t = float(g["starting_time"][()]) + np.arange(n) / rate
            key = "lin" if "Linearized" in name else "xy"
            s[key] = {"t": t, "data": g["data"][:], "rate": rate, "name": name,
                      "unit": g["data"].attrs["unit"]}
    s["track"] = s["lin"]["name"].replace("LinearizedPosition", "")
    lfp = f["processing/ecephys/LFP/LFP"]
    s["lfp_shape"] = lfp["data"].shape
    s["lfp_rate"] = float(lfp["starting_time"].attrs["rate"])
    s["lfp_conversion"] = float(lfp["data"].attrs["conversion"])
    s["bad_electrode"] = f["general/extracellular_ephys/electrodes/bad_electrode"][:]
    return s


def state_mask(t: np.ndarray, s: dict, label: str) -> np.ndarray:
    """True where t falls in an interval of the given sleep-state label."""
    st = s["states"]
    sel = st["label"] == label
    return in_intervals(t, st["start"][sel], st["stop"][sel])


def in_intervals(t, starts, stops) -> np.ndarray:
    order = np.argsort(starts)
    starts, stops = np.asarray(starts)[order], np.asarray(stops)[order]
    i = np.searchsorted(starts, t, side="right") - 1
    ok = i >= 0
    out = np.zeros(len(t), bool)
    out[ok] = t[ok] < stops[i[ok]]
    return out


# ----------------------------------------------------------------------------- LFP

def read_channel(url: str, ch: int, start: int = 0, stop: int | None = None) -> np.ndarray:
    with open_nwb(url) as f:
        d = f["processing/ecephys/LFP/LFP/data"]
        return d[start:stop, ch].astype(np.float32) * np.float32(d.attrs["conversion"] * 1e6)  # uV


def ripple_band(x: np.ndarray) -> np.ndarray:
    sos = signal.butter(3, [150, 250], btype="band", fs=LFP_RATE, output="sos")
    return signal.sosfiltfilt(sos, x).astype(np.float32)


def ripple_envelope(x: np.ndarray) -> np.ndarray:
    y = ripple_band(x)
    return np.sqrt(gaussian_filter1d(y * y, 0.008 * LFP_RATE)).astype(np.float32)


def choose_ripple_channel(url: str, s: dict) -> tuple[int, np.ndarray]:
    """The good channel with the most ripple-band power in one LFP chunk of POST non-REM.

    Returns the channel and the ripple-band power of every channel (NaN for bad ones)."""
    st = s["states"]
    post0 = s["epochs"]["POSTEpoch"][0]
    sel = (st["label"] == "Non-REM") & (st["start"] >= post0)
    i = np.argmax(np.where(sel, st["stop"] - st["start"], -1))
    with open_nwb(url) as f:
        d = f["processing/ecephys/LFP/LFP/data"]
        chunk = d.chunks[0]
        a = int(np.ceil(st["start"][i] * LFP_RATE / chunk)) * chunk
        b = min(a + chunk, int(st["stop"][i] * LFP_RATE))
        power = np.full(d.shape[1], np.nan)
        for ch in range(d.shape[1]):
            if s["bad_electrode"][ch]:
                continue
            x = d[a:b, ch].astype(np.float32) * np.float32(d.attrs["conversion"] * 1e6)
            power[ch] = float(np.mean(ripple_band(x) ** 2))
    return int(np.nanargmax(power)), power


def band_power(x: np.ndarray, lo: float, hi: float) -> float:
    f, p = signal.welch(x, fs=LFP_RATE, nperseg=2048)
    return float(p[(f >= lo) & (f < hi)].mean())


def theta_delta(x: np.ndarray, s: dict, shift: float = 0.0) -> dict:
    """Mean theta (6-10 Hz) over delta (1-4 Hz) power ratio in REM and non-REM intervals of at
    least 10 s, with the state labels shifted in time by `shift` seconds."""
    st = s["states"]
    out = {}
    for lab in ("REM", "Non-REM"):
        ratios = []
        for a, b in zip(st["start"][st["label"] == lab], st["stop"][st["label"] == lab]):
            a, b = a + shift, b + shift
            if b - a < 10 or a < 0 or b * LFP_RATE > len(x):
                continue
            seg = x[int(a * LFP_RATE):int(b * LFP_RATE)]
            ratios.append(band_power(seg, 6, 10) / band_power(seg, 1, 4))
        out[lab] = float(np.median(ratios)) if ratios else np.nan
    return out


# ----------------------------------------------------------------------------- behaviour

def lin_speed(s: dict) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Time, linearized position (cm) and signed velocity (cm/s), NaN off the track."""
    t, x = s["lin"]["t"], s["lin"]["data"][:, 0] * 100.0
    rate = s["lin"]["rate"]
    ok = np.isfinite(x)
    xi = np.interp(t, t[ok], x[ok])
    xs = gaussian_filter1d(xi, 0.25 * rate)
    v = np.gradient(xs) * rate
    v[~ok] = np.nan
    return t, np.where(ok, x, np.nan), v


def xy_speed(s: dict) -> tuple[np.ndarray, np.ndarray]:
    """Time and 2D head speed (cm/s, in the file's units times 100), NaN where untracked."""
    t, xy = s["xy"]["t"], s["xy"]["data"] * 100.0
    rate = s["xy"]["rate"]
    ok = np.all(np.isfinite(xy), axis=1)
    sm = np.column_stack([gaussian_filter1d(np.interp(t, t[ok], xy[ok, k]), 0.25 * rate)
                          for k in range(2)])
    sp = np.hypot(*np.gradient(sm, axis=0).T) * rate
    sp[~ok] = np.nan
    return t, sp


def track_length(s: dict) -> float:
    """Track length in cm from the name of the position series; the circular track is taken
    as the largest linearized position."""
    name = s["track"]
    if name.startswith("1.6m"):
        return 160.0
    if name.startswith("2m"):
        return 200.0
    return float(np.nanmax(s["lin"]["data"]) * 100.0)


def directions(s: dict) -> list[int]:
    """+1 and -1 on the linear tracks. On the circular track, where the animal ran one way, the
    direction it ran in most (the sign of the velocity in most running samples)."""
    if not s["track"].startswith("Circular"):
        return [1, -1]
    _, _, v = lin_speed(s)
    v = v[np.isfinite(v)]
    return [1] if np.sum(v > RUN_SPEED) >= np.sum(v < -RUN_SPEED) else [-1]


def run_samples(s: dict, direction: int) -> tuple[np.ndarray, np.ndarray]:
    """Times and positions (cm) of running samples in one direction."""
    t, x, v = lin_speed(s)
    m = np.isfinite(x) & np.isfinite(v) & (direction * v > RUN_SPEED)
    return t[m], x[m]


def rate_map(spk: np.ndarray, t_run: np.ndarray, x_run: np.ndarray, length: float,
             dt: float) -> tuple[np.ndarray, np.ndarray]:
    """Smoothed rate map (Hz) and smoothed occupancy (s) on 2 cm bins.

    Spikes are assigned the position of the nearest running sample within one sample."""
    nb = int(np.ceil(length / BIN_CM))
    edges = np.arange(nb + 1) * BIN_CM
    occ = np.histogram(x_run, edges)[0] * dt
    j = np.searchsorted(t_run, spk)
    j = np.clip(j, 1, len(t_run) - 1)
    near = np.where(np.abs(t_run[j - 1] - spk) < np.abs(t_run[j] - spk), j - 1, j)
    keep = np.abs(t_run[near] - spk) <= dt
    cnt = np.histogram(x_run[near[keep]], edges)[0].astype(float)
    occ_s = gaussian_filter1d(occ, SMOOTH_BINS)
    cnt_s = gaussian_filter1d(cnt, SMOOTH_BINS)
    with np.errstate(invalid="ignore", divide="ignore"):
        rm = np.where(occ_s > 0.05, cnt_s / occ_s, 0.0)
    return rm, occ


def spatial_info(rm: np.ndarray, occ: np.ndarray) -> float:
    """Skaggs information, bits per spike."""
    p = occ / occ.sum()
    lam = np.sum(p * rm)
    if lam <= 0:
        return np.nan
    r = rm / lam
    with np.errstate(divide="ignore", invalid="ignore"):
        terms = np.where(r > 0, p * r * np.log2(r), 0.0)
    return float(np.sum(terms))


def place_fields(rm: np.ndarray) -> list[np.ndarray]:
    """Contiguous runs of at least 3 bins at 1 Hz or more and 20% of the peak or more."""
    above = (rm >= PLACE_PEAK) & (rm >= 0.2 * rm.max())
    fields, i = [], 0
    while i < len(rm):
        if above[i]:
            j = i
            while j < len(rm) and above[j]:
                j += 1
            if j - i >= 3:
                fields.append(np.arange(i, j))
            i = j
        else:
            i += 1
    return fields


# ----------------------------------------------------------------------------- events

def runs_of(mask: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    d = np.diff(np.r_[0, mask.astype(np.int8), 0])
    return np.flatnonzero(d == 1), np.flatnonzero(d == -1)


def population_bursts(spikes: list[np.ndarray], t_end: float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Population bursts of all units: start, stop (s) and peak z of each, before the ripple
    and immobility conditions."""
    n = int(np.ceil(t_end / 0.001)) + 1
    cnt = np.bincount((np.concatenate(spikes) / 0.001).astype(np.int64), minlength=n)[:n]
    z = gaussian_filter1d(cnt.astype(np.float32), 10.0)
    z = (z - z.mean()) / z.std()
    a, b = runs_of(z > 0)
    peak = np.maximum.reduceat(z, a) if len(a) else np.array([])
    dur = (b - a) * 0.001
    keep = (peak >= 3) & (dur >= 0.05) & (dur <= 0.5)
    return a[keep] * 0.001, b[keep] * 0.001, peak[keep]


def segment_max(x: np.ndarray, starts: np.ndarray, stops: np.ndarray) -> np.ndarray:
    a = np.clip((starts * LFP_RATE).astype(np.int64), 0, len(x) - 1)
    b = np.clip((stops * LFP_RATE).astype(np.int64), a + 1, len(x))
    out = np.empty(len(a))
    for i, (p, q) in enumerate(zip(a, b)):
        out[i] = x[p:q].max()
    return out


def prepare_session(path: str, url: str) -> dict:
    """Load one file and reduce it: units, behaviour, the ripple channel, candidate events
    and the data checks that need the LFP."""
    with open_nwb(url) as f:
        s = load_session(f)
    s["path"] = path
    ch, power = choose_ripple_channel(url, s)
    s["ripple_channel"], s["ripple_power"] = ch, power
    x = read_channel(url, ch)
    s["lfp_seconds"] = len(x) / LFP_RATE
    env = ripple_envelope(x)
    nrem = state_mask(np.arange(len(env)) / LFP_RATE, s, "Non-REM")
    mu, sd = float(env[nrem].mean()), float(env[nrem].std())
    envz = (env - mu) / sd
    # state clock check: theta/delta in REM and non-REM, with true and shifted labels
    s["theta_delta"] = {sh: theta_delta(x, s, sh) for sh in (0.0, 600.0)}
    del x, env
    t_end = max(s["lfp_seconds"], max(sp.max() for sp in s["spikes"] if len(sp)))
    a, b, peak = population_bursts(s["spikes"], t_end)
    rip = segment_max(envz, a, b)
    # LFP and spike clock check: bursts in non-REM that hold a ripple, with the envelope true
    # and shifted by 0.5 s
    mid = (a + b) / 2
    in_nrem = state_mask(mid, s, "Non-REM")
    s["ripple_overlap"] = {sh: float(np.mean(segment_max(envz, a[in_nrem] + sh, b[in_nrem] + sh) >= 3))
                           for sh in (0.0, 0.5, 2.0)}
    del envz
    # immobility and epoch of each burst
    rem = state_mask(mid, s, "REM")
    ep = np.full(len(a), "", dtype=object)
    for lab in ("PREEpoch", "MazeEpoch", "POSTEpoch"):
        lo, hi = s["epochs"][lab]
        ep[(mid >= lo) & (mid < hi)] = lab.replace("Epoch", "").upper()
    tx, sp = xy_speed(s)
    sp_ev = np.interp(mid, tx, np.nan_to_num(sp, nan=np.inf), left=np.inf, right=np.inf)
    immobile = np.where(ep == "MAZE", sp_ev < RUN_SPEED, ~rem)
    s["bursts"] = {"start": a, "stop": b, "peak": peak, "ripple_z": rip, "epoch": ep,
                   "rem": rem, "immobile": immobile}
    keep = (rip >= 3) & immobile & (ep != "")
    s["events"] = {"start": a[keep], "stop": b[keep], "epoch": ep[keep].astype(str)}
    s["ripple_threshold_sd"] = (mu, sd)
    return s


# ----------------------------------------------------------------------------- templates

def build_templates(s: dict) -> dict:
    """Rate maps of every pyramidal cell in each direction, place cells and templates."""
    pyr = np.flatnonzero(s["cell_type"] == "excitatory")
    length = track_length(s)
    dt = 1.0 / s["lin"]["rate"]
    out = {"pyr": pyr, "length": length, "maps": {}, "occ": {}}
    for d in directions(s):
        t_run, x_run = run_samples(s, d)
        maps, occ = [], None
        for u in pyr:
            rm, occ = rate_map(s["spikes"][u], t_run, x_run, length, dt)
            maps.append(rm)
        out["maps"][d] = np.array(maps)
        out["occ"][d] = occ
        out[("run", d)] = (t_run, x_run)
    peaks = np.max([out["maps"][d].max(1) for d in out["maps"]], axis=0)
    out["peak"] = peaks
    return out


def template_cells(tpl: dict, threshold: float = PLACE_PEAK) -> dict:
    """Indices (into pyr) of the cells in each direction's template."""
    return {d: np.flatnonzero(tpl["maps"][d].max(1) >= threshold) for d in tpl["maps"]}


# ----------------------------------------------------------------------------- decoding

def event_counts(spikes: list[np.ndarray], start: float, stop: float) -> np.ndarray:
    """Spike counts (cells x 20 ms bins) of the given spike trains in one event."""
    nb = max(1, int(np.ceil((stop - start) / DECODE_BIN)))
    edges = start + np.arange(nb + 1) * DECODE_BIN
    return np.array([np.diff(np.searchsorted(sp, edges)) for sp in spikes])


def count_cache(s: dict, tpl: dict) -> list[np.ndarray]:
    """Counts (pyramidal cells x 20 ms bins) of every candidate event, computed once."""
    sp = [s["spikes"][u] for u in tpl["pyr"]]
    ev = s["events"]
    return [event_counts(sp, a, b) for a, b in zip(ev["start"], ev["stop"])]


def log_posterior(counts: np.ndarray, maps: np.ndarray) -> np.ndarray:
    """Log posterior (time x position) of a Poisson decoder with a flat prior."""
    f = maps + 1e-3
    return counts.T @ np.log(f) - DECODE_BIN * f.sum(0)[None, :]


def normalise(lp: np.ndarray) -> np.ndarray:
    lp = lp - lp.max(-1, keepdims=True)
    p = np.exp(lp)
    return p / p.sum(-1, keepdims=True)


def weighted_r(p: np.ndarray) -> np.ndarray:
    """Weighted correlation of position and time for posteriors (..., time, position)."""
    T, X = p.shape[-2:]
    t = np.arange(T, dtype=float)[:, None]
    x = np.arange(X, dtype=float)[None, :]
    w = p / p.sum((-2, -1), keepdims=True)
    mt = (w * t).sum((-2, -1))
    mx = (w * x).sum((-2, -1))
    ct = t - mt[..., None, None]
    cx = x - mx[..., None, None]
    cov = (w * ct * cx).sum((-2, -1))
    vt = (w * ct ** 2).sum((-2, -1))
    vx = (w * cx ** 2).sum((-2, -1))
    with np.errstate(invalid="ignore", divide="ignore"):
        return cov / np.sqrt(vt * vx)


def column_cycle_null(p: np.ndarray, rng: np.random.Generator, n: int = N_SHUFFLE) -> np.ndarray:
    """|r| of n column-cycle shuffles (each time bin's posterior rotated by a random amount)."""
    T, X = p.shape
    x = np.arange(X, dtype=float)
    # first and second moments of every rotation of every row
    rot = x[(np.arange(X)[None, :] + np.arange(X)[:, None]) % X]   # rot[k, i] = x[(i + k) % X]
    m1 = p @ rot.T                                                   # (T, X): sum_i p[t,i] x[(i+k)%X]
    m2 = p @ (rot ** 2).T
    k = rng.integers(0, X, size=(n, T))
    rows = np.arange(T)[None, :]
    a1, a2 = m1[rows, k], m2[rows, k]                                 # (n, T)
    t = np.arange(T, dtype=float)
    mt, mx = t.mean(), a1.mean(1)
    cov = (t[None, :] * a1).mean(1) - mt * mx
    vx = a2.mean(1) - mx ** 2
    vt = (t ** 2).mean() - mt ** 2
    with np.errstate(invalid="ignore", divide="ignore"):
        return np.abs(cov / np.sqrt(vt * vx))


def score_event(counts: np.ndarray, maps: np.ndarray, rng: np.random.Generator,
                n_shuffle: int = N_SHUFFLE) -> tuple[float, float, np.ndarray]:
    """(r, rZ, kept time bins) of one event: bins without spikes are left out."""
    keep = counts.sum(0) > 0
    if keep.sum() < 3:
        return np.nan, np.nan, keep
    p = normalise(log_posterior(counts[:, keep], maps))
    r = float(weighted_r(p))
    null = column_cycle_null(p, rng, n_shuffle)
    sd = null.std()
    return r, float((abs(r) - null.mean()) / sd) if sd > 0 else np.nan, keep


def decode_events(s: dict, tpl: dict, cache: list, cells: dict, rng: np.random.Generator,
                  epochs=("PRE", "MAZE", "POST"), maps: dict | None = None,
                  n_shuffle: int = N_SHUFFLE) -> dict:
    """Score every candidate event of the given epochs with each direction's template.

    `cells` gives the template cells per direction (indices into tpl['pyr']); `maps` replaces
    the rate maps (for shuffled templates). An event is scored with a template when at least
    MIN_ACTIVE of its cells fire; the event takes the template with the larger rZ."""
    maps = maps if maps is not None else tpl["maps"]
    ev = s["events"]
    sel = np.flatnonzero(np.isin(ev["epoch"], epochs))
    out = {"index": [], "epoch": [], "r": [], "rZ": [], "direction": [], "n_active": []}
    for i in sel:
        best = None
        for d, c in cells.items():
            if len(c) < MIN_ACTIVE:
                continue
            cnt = cache[i][c]
            n_active = int((cnt.sum(1) > 0).sum())
            if n_active < MIN_ACTIVE:
                continue
            r, rz, _ = score_event(cnt, maps[d][c], rng, n_shuffle)
            if np.isfinite(rz) and (best is None or rz > best[1]):
                best = (r, rz, d, n_active)
        if best is None:
            continue
        out["index"].append(i)
        out["epoch"].append(ev["epoch"][i])
        out["r"].append(best[0])
        out["rZ"].append(best[1])
        out["direction"].append(best[2])
        out["n_active"].append(best[3])
    return {k: np.array(v) for k, v in out.items()}


def _shifted_r(cnt: np.ndarray, f: np.ndarray, lp: np.ndarray, a: int, shifts: np.ndarray) -> np.ndarray:
    """|r| of an event with row a of the rate maps f circularly shifted by each of `shifts`."""
    X = f.shape[1]
    fs = f[a][(np.arange(X)[None, :] - shifts[:, None]) % X]           # np.roll by each shift
    delta = (cnt[a][None, :, None] * (np.log(fs)[:, None, :] - np.log(f[a])[None, None, :])
             - DECODE_BIN * (fs - f[a][None, :])[:, None, :])          # (K, T, X)
    return np.abs(weighted_r(normalise(lp[None] + delta)))


def _event_parts(cnt: np.ndarray, m: np.ndarray):
    keep = cnt.sum(0) > 0
    cnt = cnt[:, keep]
    f = m + 1e-3
    lp = cnt.T @ np.log(f) - DECODE_BIN * f.sum(0)[None, :]
    return cnt, f, lp


def cell_contributions(s: dict, tpl: dict, cache: list, cells: dict, decoded: dict,
                       rng: np.random.Generator, maps: dict | None = None,
                       mode: str = "template") -> list[tuple]:
    """Per event and active cell: (event index, epoch, cell index into pyr, |r|, |r| of each
    shift). The contribution is |r| minus the mean of the shifted |r|.

    Each cell's rate map is circularly shifted by N_PCC_SHIFT random amounts, drawn afresh for
    every event, and the event is decoded again with each.

    mode "template" (the criterion): |r| on the template the event was scored with (the one
    with the larger rZ on the linear tracks), active cells of that template.
    mode "best": |r| is the larger |r| over every template the event qualifies for, both with
    the original maps and with the cell's map shifted (in every template that holds the cell),
    so the choice of template is made the same way on both sides of the difference."""
    maps = maps if maps is not None else tpl["maps"]
    rows = []
    for i, ep, d0 in zip(decoded["index"], decoded["epoch"], decoded["direction"]):
        if ep not in ("PRE", "POST"):
            continue
        if mode == "template":
            use = [d0]
        else:
            use = [d for d, c in cells.items() if len(c) >= MIN_ACTIVE
                   and int((cache[i][c].sum(1) > 0).sum()) >= MIN_ACTIVE]
        parts = {d: _event_parts(cache[i][cells[d]], maps[d][cells[d]]) for d in use}
        base = {d: abs(float(weighted_r(normalise(parts[d][2])))) for d in use}
        r0 = max(base.values())
        active = sorted({int(cells[d][a]) for d in use for a in np.flatnonzero(parts[d][0].sum(1) > 0)})
        for u in active:
            sh = rng.integers(1, maps[use[0]].shape[1], size=N_PCC_SHIFT)
            best = np.full(N_PCC_SHIFT, -np.inf)
            for d in use:
                pos = np.flatnonzero(cells[d] == u)
                if len(pos):
                    cnt, f, lp = parts[d]
                    r = _shifted_r(cnt, f, lp, int(pos[0]), sh)
                else:
                    r = np.full(N_PCC_SHIFT, base[d])
                best = np.maximum(best, r)
            rows.append((i, ep, u, r0, best))
    return rows


def shifted_maps(tpl: dict, which: np.ndarray, rng: np.random.Generator) -> dict:
    """Copy of the rate maps with the cells `which` (indices into pyr) circularly shifted."""
    out = {}
    for d, m in tpl["maps"].items():
        m = m.copy()
        for j in which:
            m[j] = np.roll(m[j], rng.integers(1, m.shape[1]))
        out[d] = m
    return out


# ----------------------------------------------------------------------------- rates

def epoch_duration(s: dict, label: str) -> float:
    a, b = s["epochs"][label]
    return b - a


def count_in(sp: np.ndarray, starts: np.ndarray, stops: np.ndarray) -> int:
    i = np.searchsorted(sp, starts)
    j = np.searchsorted(sp, stops)
    return int((j - i).sum())


def burst_fraction(sp: np.ndarray) -> float:
    if len(sp) < 3:
        return np.nan
    isi = np.diff(sp)
    short = isi <= BURST_ISI
    inb = np.zeros(len(sp), bool)
    inb[:-1] |= short
    inb[1:] |= short
    return float(inb.mean())


def binned(spikes: list[np.ndarray], a: float, b: float, width: float = 0.1,
           mask_times: np.ndarray | None = None) -> np.ndarray:
    """Counts (cells x bins) of 100 ms bins between a and b; with mask_times, only the bins
    whose centres are True in it are kept."""
    edges = np.arange(a, b + width / 2, width)
    m = np.array([np.histogram(sp, edges)[0] for sp in spikes], dtype=float)
    if mask_times is not None:
        m = m[:, mask_times]
    return m


def corr_matrix(m: np.ndarray) -> np.ndarray:
    with np.errstate(invalid="ignore", divide="ignore"):
        c = np.corrcoef(m)
    return c


def partial_corr(x: np.ndarray, y: np.ndarray, z: np.ndarray) -> float:
    """Correlation of x and y controlling for z."""
    ok = np.isfinite(x) & np.isfinite(y) & np.isfinite(z)
    x, y, z = x[ok], y[ok], z[ok]
    if len(x) < 4:
        return np.nan
    rxy = np.corrcoef(x, y)[0, 1]
    rxz = np.corrcoef(x, z)[0, 1]
    ryz = np.corrcoef(y, z)[0, 1]
    return float((rxy - rxz * ryz) / np.sqrt((1 - rxz ** 2) * (1 - ryz ** 2)))


# ----------------------------------------------------------------------------- data checks

def position_error(s: dict, lags=(-30.0, -5.0, -1.0, 0.0, 1.0, 5.0, 30.0)) -> dict:
    """Median error (cm) of decoding position during running from pyramidal spikes, with rate
    maps from even minutes and 0.5 s windows of odd minutes, for spikes shifted by each lag."""
    t, x, v = lin_speed(s)
    m = np.isfinite(x) & (np.abs(np.nan_to_num(v)) > RUN_SPEED)
    t_run, x_run = t[m], x[m]
    dt = 1.0 / s["lin"]["rate"]
    length = track_length(s)
    even = (np.floor((t_run - t_run[0]) / 60) % 2) == 0
    pyr = np.flatnonzero(s["cell_type"] == "excitatory")
    out = {}
    for lag in lags:
        sp = [s["spikes"][u] + lag for u in pyr]
        maps = np.array([rate_map(q, t_run[even], x_run[even], length, dt)[0] for q in sp])
        # windows: consecutive odd-minute running samples grouped into 0.5 s
        to, xo = t_run[~even], x_run[~even]
        w = np.floor((to - to[0]) / 0.5).astype(int)
        uw, first = np.unique(w, return_index=True)
        errs = []
        for k, i0 in zip(uw, first):
            sel = w == k
            a, b = to[sel][0], to[sel][-1] + dt
            if b - a < 0.4:
                continue
            cnt = np.array([np.searchsorted(q, b) - np.searchsorted(q, a) for q in sp])
            if cnt.sum() == 0:
                continue
            f = maps + 1e-3
            lp = cnt @ np.log(f) - (b - a) * f.sum(0)
            errs.append(abs((np.argmax(lp) + 0.5) * BIN_CM - np.mean(xo[sel])))
        out[lag] = float(np.median(errs))
    return out


# ----------------------------------------------------------------------------- per-session passes

def first_pass(s: dict, seed_decode: int, seed_pcc: int, seed_null: int) -> dict:
    """Templates, the event score of every candidate event, the per-cell contributions, and the
    contributions under a fully shifted template (the PCC test's false-positive rate), each for
    the criterion's contribution (mode "template") and for the variant (mode "best")."""
    tpl = build_templates(s)
    cells = template_cells(tpl)
    cache = count_cache(s, tpl)
    dec = decode_events(s, tpl, cache, cells, np.random.default_rng(seed_decode))
    rows = cell_contributions(s, tpl, cache, cells, dec, np.random.default_rng(seed_pcc))
    rows_best = cell_contributions(s, tpl, cache, cells, dec, np.random.default_rng(seed_pcc + 1),
                                   mode="best")
    rng = np.random.default_rng(seed_null)
    null_maps = shifted_maps(tpl, np.arange(len(tpl["pyr"])), rng)
    dec_null = decode_events(s, tpl, cache, cells, rng, epochs=("PRE", "POST"), maps=null_maps,
                             n_shuffle=20)
    sub = {k: v[::4] for k, v in dec_null.items()}          # every fourth event is enough here
    rows_null = cell_contributions(s, tpl, cache, cells, sub, rng, maps=null_maps)
    rows_null_best = cell_contributions(s, tpl, cache, cells, sub, rng, maps=null_maps, mode="best")
    return {"tpl": tpl, "cells": cells, "decoded": dec, "contrib": rows, "contrib_null": rows_null,
            "contrib_best": rows_best, "contrib_null_best": rows_null_best}


def variant_pass(s: dict, tpl: dict, variants: dict, n_shuffle: int = 50) -> dict:
    """Decode PRE and POST events again for each variant.

    `variants` maps a name to (cells per direction, list of pyr indices to shift or None, seed)."""
    cache = count_cache(s, tpl)
    out = {}
    for name, (cells, shift, seed) in variants.items():
        rng = np.random.default_rng(seed)
        maps = shifted_maps(tpl, np.asarray(shift, int), rng) if shift is not None else None
        out[name] = decode_events(s, tpl, cache, cells, rng, epochs=("PRE", "POST"), maps=maps,
                                  n_shuffle=n_shuffle)
    return out


def cell_measures(s: dict, tpl: dict, place: np.ndarray) -> dict:
    """Per place cell (indices into pyr): rates, gains, bursting, spatial measures, and the
    100 ms coactivation matrices of PRE, POST, MAZE running and the whole session."""
    pyr = tpl["pyr"]
    sp = [s["spikes"][pyr[j]] for j in place]
    T = s["lfp_seconds"]
    pre, post = s["epochs"]["PREEpoch"], s["epochs"]["POSTEpoch"]
    st = s["states"]
    nrem = (st["label"] == "Non-REM")
    def nrem_in(ep):
        a = np.clip(st["start"][nrem], *ep)
        b = np.clip(st["stop"][nrem], *ep)
        return a, b
    na_pre, nb_pre = nrem_in(pre)
    na_post, nb_post = nrem_in(post)
    nrem_dur = (nb_pre - na_pre).sum() + (nb_post - na_post).sum()
    ev = s["events"]
    e_pre = ev["epoch"] == "PRE"
    e_post = ev["epoch"] == "POST"
    d_epre = (ev["stop"][e_pre] - ev["start"][e_pre]).sum()
    d_epost = (ev["stop"][e_post] - ev["start"][e_post]).sum()
    m = {k: [] for k in ("rate_session", "rate_sleep", "rate_prepost", "gain", "gain_pre",
                         "gain_post", "burst", "info", "n_fields", "peak_pos", "best_dir",
                         "infield_change")}
    for j, q in zip(place, sp):
        n_pre = count_in(q, np.array([pre[0]]), np.array([pre[1]]))
        n_post = count_in(q, np.array([post[0]]), np.array([post[1]]))
        r_pre, r_post = n_pre / (pre[1] - pre[0]), n_post / (post[1] - post[0])
        r_pp = (n_pre + n_post) / ((pre[1] - pre[0]) + (post[1] - post[0]))
        c_epre = count_in(q, ev["start"][e_pre], ev["stop"][e_pre])
        c_epost = count_in(q, ev["start"][e_post], ev["stop"][e_post])
        m["rate_session"].append(len(q) / T)
        m["rate_sleep"].append((count_in(q, na_pre, nb_pre) + count_in(q, na_post, nb_post)) / nrem_dur)
        m["rate_prepost"].append(r_pp)
        m["gain"].append(((c_epre + c_epost) / (d_epre + d_epost)) / r_pp if r_pp > 0 else np.nan)
        m["gain_pre"].append((c_epre / d_epre) / r_pre if r_pre > 0 else np.nan)
        m["gain_post"].append((c_epost / d_epost) / r_post if r_post > 0 else np.nan)
        m["burst"].append(burst_fraction(q))
        d = max(tpl["maps"], key=lambda dd: tpl["maps"][dd][j].max())
        rm, occ = tpl["maps"][d][j], tpl["occ"][d]
        m["best_dir"].append(d)
        m["info"].append(spatial_info(rm, occ))
        fields = place_fields(rm)
        m["n_fields"].append(len(fields))
        m["peak_pos"].append((np.argmax(rm) + 0.5) / len(rm))
        # in-field over out-of-field rate, first and last third of running in that direction
        t_run, x_run = tpl[("run", d)]
        if not fields:
            m["infield_change"].append(np.nan)
            continue
        fb = max(fields, key=lambda b: rm[b].sum())
        dt = 1.0 / s["lin"]["rate"]
        bins = np.minimum((x_run / BIN_CM).astype(int), len(rm) - 1)
        inf = np.isin(bins, fb)
        j_near = np.clip(np.searchsorted(t_run, q), 1, len(t_run) - 1)
        near = np.where(np.abs(t_run[j_near - 1] - q) < np.abs(t_run[j_near] - q), j_near - 1, j_near)
        near = near[np.abs(t_run[near] - q) <= dt]
        cnt = np.bincount(near, minlength=len(t_run))
        thirds = np.array_split(np.arange(len(t_run)), 3)
        lr = []
        for th in (thirds[0], thirds[-1]):
            i_in, i_out = th[inf[th]], th[~inf[th]]
            r_in = cnt[i_in].sum() / (len(i_in) * dt) if len(i_in) else np.nan
            r_out = cnt[i_out].sum() / (len(i_out) * dt) if len(i_out) else np.nan
            lr.append(np.log10((r_in + 0.01) / (r_out + 0.01)))
        m["infield_change"].append(lr[1] - lr[0])
    m = {k: np.array(v, float) for k, v in m.items()}
    # coactivation
    t, x, v = lin_speed(s)
    run_t = t[np.isfinite(x) & (np.abs(np.nan_to_num(v)) > RUN_SPEED)]
    maze = s["epochs"]["MazeEpoch"]
    edges = np.arange(maze[0], maze[1] + 0.05, 0.1)
    centres = edges[:-1] + 0.05
    near = np.clip(np.searchsorted(run_t, centres), 1, len(run_t) - 1)
    run_bins = np.minimum(np.abs(run_t[near] - centres), np.abs(run_t[near - 1] - centres)) < 0.05
    m["C_pre"] = corr_matrix(binned(sp, *pre))
    m["C_post"] = corr_matrix(binned(sp, *post))
    m["C_run"] = corr_matrix(binned(sp, maze[0], maze[1], mask_times=run_bins))
    m["C_session"] = corr_matrix(binned(sp, 0.0, T))
    return m
