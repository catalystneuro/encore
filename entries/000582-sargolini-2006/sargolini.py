"""Data access and analysis helpers for dandiset 000582 (Sargolini et al. 2006).

`load_sessions` streams every session of the dandiset from the DANDI Archive
and returns positions and spike times as plain numpy arrays. The rest are the
standard measures for entorhinal spatial cells: firing-rate maps, spatial
autocorrelograms, grid scores, head-direction tuning and speed tuning.

The paper's full text was not available when this was written, so the
analysis parameters below are common choices from the grid-cell literature,
not values taken from the paper's methods.
"""

from __future__ import annotations

import warnings
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field

import numpy as np
from scipy import ndimage, signal

DANDISET = "000582"
VERSION = "0.251111.2151"

BIN = 0.05           # spatial bin, m
SMOOTH = 1.5         # Gaussian smoothing of rate maps, in bins
HD_BIN = 6           # head-direction bin, degrees
SPEED_EDGES = np.arange(0.0, 0.5001, 0.05)   # running-speed bins, m/s
MIN_SHIFT = 20.0     # smallest circular shift of the spike train in a shuffle, s


@dataclass
class Unit:
    name: str
    layer: str               # "II", "III", "V", "VI" or "" when not given
    spike_times: np.ndarray  # s


@dataclass
class Session:
    path: str
    subject: str
    t: np.ndarray                    # position sample times, s
    xy: np.ndarray                   # head position, m, shape (n, 2)
    head_direction: np.ndarray | None  # radians, or None with one tracking LED
    units: list[Unit] = field(default_factory=list)

    @property
    def dt(self) -> float:
        return float(np.median(np.diff(self.t)))

    @property
    def box(self) -> float:
        """Side of the square enclosure in m, from the range the rat covered.

        Positions are centred on zero. Every file's description says the
        enclosure was 1 x 1 m, but in 23 sessions the tracked positions span
        1.5 to 2.5 m, so the size is read from the data, rounded up to the next 0.5 m.
        """
        extent = 2 * np.nanpercentile(np.abs(self.xy), 99.9)
        return float(max(1.0, np.ceil(extent / 0.5 - 0.1) * 0.5))


# --- loading ------------------------------------------------------------------

def _session_from_nwb(path: str, nwb) -> Session:
    series = nwb.processing["behavior"]["Position"].spatial_series
    leds = [series[name] for name in sorted(series)]
    t = leds[0].timestamps[:]
    tracks = [led.data[:] * led.conversion for led in leds]
    if len(tracks) == 2:
        xy = np.nanmean(np.stack(tracks), axis=0)
        d = tracks[1] - tracks[0]
        head_direction = np.arctan2(d[:, 1], d[:, 0])
    else:
        xy, head_direction = tracks[0], None
    table = nwb.units.to_dataframe()
    units = [
        Unit(name=row.unit_name,
             layer=str(row.histology).replace("MEC L", "").strip(),
             spike_times=np.asarray(row.spike_times, dtype=float))
        for row in table.itertuples()
    ]
    return Session(path=path, subject=str(nwb.subject.subject_id), t=t, xy=xy,
                   head_direction=head_direction, units=units)


def load_sessions(version: str = VERSION, max_workers: int = 8) -> list[Session]:
    """Stream every session of the dandiset. Nothing is written to disk."""
    import h5py
    import remfile
    from dandi.dandiapi import DandiAPIClient
    from pynwb import NWBHDF5IO

    with DandiAPIClient() as client:
        dandiset = client.get_dandiset(DANDISET, version)
        assets = sorted(
            (a.path, a.get_content_url(follow_redirects=1, strip_query=True))
            for a in dandiset.get_assets()
        )

    def load(asset):
        path, url = asset
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            with NWBHDF5IO(file=h5py.File(remfile.File(url), "r"), mode="r",
                           load_namespaces=True) as io:
                return _session_from_nwb(path, io.read())

    with ThreadPoolExecutor(max_workers) as pool:
        return list(pool.map(load, assets))


# --- behavior -----------------------------------------------------------------

def running_speed(session: Session, window_s: float = 0.5) -> np.ndarray:
    """Speed of the head in m/s at each position sample, from smoothed positions."""
    width = max(3, int(round(window_s / session.dt)) | 1)
    kernel = np.ones(width) / width
    xy = np.column_stack([
        np.convolve(_fill(session.xy[:, i]), kernel, mode="same") for i in range(2)
    ])
    return np.hypot(*np.gradient(xy, session.t, axis=0).T)


def _fill(x: np.ndarray) -> np.ndarray:
    """Linearly interpolate over missing samples."""
    bad = np.isnan(x)
    if bad.any() and not bad.all():
        x = x.copy()
        x[bad] = np.interp(np.flatnonzero(bad), np.flatnonzero(~bad), x[~bad])
    return x


def spike_samples(session: Session, spike_times: np.ndarray) -> np.ndarray:
    """Index of the position sample nearest to each spike within the session."""
    spikes = spike_times[(spike_times >= session.t[0]) & (spike_times <= session.t[-1])]
    idx = np.searchsorted(session.t, spikes)
    idx = np.clip(idx, 1, len(session.t) - 1)
    return np.where(spikes - session.t[idx - 1] < session.t[idx] - spikes, idx - 1, idx)


# --- position -----------------------------------------------------------------

def rate_map(session: Session, samples: np.ndarray) -> np.ndarray:
    """Smoothed firing rate (Hz) in each spatial bin; NaN where the rat never went."""
    half = session.box / 2
    edges = np.arange(-half, half + BIN / 2, BIN)
    ok = ~np.isnan(session.xy).any(axis=1)
    occupancy, _, _ = np.histogram2d(*session.xy[ok].T, bins=[edges, edges])
    spikes_xy = session.xy[samples]
    spikes_xy = spikes_xy[~np.isnan(spikes_xy).any(axis=1)]
    counts, _, _ = np.histogram2d(*spikes_xy.T, bins=[edges, edges])
    visited = occupancy > 0
    occupancy_s = ndimage.gaussian_filter(occupancy * session.dt, SMOOTH, mode="constant")
    counts_s = ndimage.gaussian_filter(counts, SMOOTH, mode="constant")
    with np.errstate(invalid="ignore", divide="ignore"):
        rate = counts_s / occupancy_s
    rate[~visited] = np.nan
    return rate


def autocorrelogram(rate: np.ndarray, min_overlap: int = 20) -> np.ndarray:
    """Pearson correlation of a rate map with itself at every spatial lag."""
    valid = ~np.isnan(rate)
    x = np.where(valid, rate, 0.0)
    m = valid.astype(float)

    def corr(a, b):
        return signal.correlate(a, b, mode="full", method="fft")

    n = np.round(corr(m, m))
    sx, sy = corr(x, m), corr(m, x)
    sxy = corr(x, x)
    sxx, syy = corr(x * x, m), corr(m, x * x)
    with np.errstate(invalid="ignore", divide="ignore"):
        num = n * sxy - sx * sy
        den = np.sqrt(n * sxx - sx ** 2) * np.sqrt(n * syy - sy ** 2)
        r = num / den
    r[(n < min_overlap) | ~np.isfinite(r)] = np.nan
    return r


def grid_score(acorr: np.ndarray) -> float:
    """Grid score of a spatial autocorrelogram.

    A ring around the centre, excluding the central peak, is correlated with
    itself rotated by 30 to 150 degrees. A hexagonal pattern correlates at 60
    and 120 degrees and not at 30, 90 and 150, so the score is
    min(60, 120) - max(30, 90, 150). The outer radius of the ring is varied
    and the highest score is returned.
    """
    size = acorr.shape[0]
    centre = (size - 1) / 2
    yy, xx = np.indices(acorr.shape)
    radius = np.hypot(yy - centre, xx - centre)

    # Radius of the central peak: where the radial profile first turns up
    # again or drops below zero.
    edges = np.arange(0, centre)
    profile = np.array([np.nanmean(acorr[(radius >= r) & (radius < r + 1)]) for r in edges])
    inner = None
    for i in range(1, len(profile) - 1):
        if np.isnan(profile[i]):
            break
        if profile[i] < 0 or profile[i + 1] > profile[i]:
            inner = i
            break
    if inner is None:
        return np.nan

    filled = np.where(np.isnan(acorr), 0.0, acorr)
    present = (~np.isnan(acorr)).astype(float)
    rotated = {
        angle: (ndimage.rotate(filled, angle, reshape=False, order=1),
                ndimage.rotate(present, angle, reshape=False, order=1) > 0.99)
        for angle in (30, 60, 90, 120, 150)
    }
    best = np.nan
    for outer in range(inner + 4, int(centre) + 1):
        ring = (radius >= inner) & (radius <= outer) & ~np.isnan(acorr)
        correlations = {}
        for angle, (values, valid) in rotated.items():
            use = ring & valid
            if use.sum() < 20:
                break
            correlations[angle] = np.corrcoef(acorr[use], values[use])[0, 1]
        else:
            score = (min(correlations[60], correlations[120])
                     - max(correlations[30], correlations[90], correlations[150]))
            if np.isnan(best) or score > best:
                best = score
    return best


# --- head direction -----------------------------------------------------------

def head_direction_tuning(session: Session, samples: np.ndarray) -> tuple[np.ndarray, float]:
    """Firing rate (Hz) by head direction, and the mean vector length of the tuning."""
    edges = np.deg2rad(np.arange(-180, 181, HD_BIN))
    hd = session.head_direction
    ok = ~np.isnan(hd)
    occupancy = np.histogram(hd[ok], bins=edges)[0] * session.dt
    spike_hd = hd[samples]
    counts = np.histogram(spike_hd[~np.isnan(spike_hd)], bins=edges)[0]
    with np.errstate(invalid="ignore", divide="ignore"):
        rate = counts / occupancy
    rate = np.where(occupancy > 0, rate, np.nan)
    kernel = np.ones(5) / 5      # circular boxcar over 30 degrees
    padded = np.concatenate([rate[-2:], rate, rate[:2]])
    good = ~np.isnan(padded)
    smooth = (np.convolve(np.where(good, padded, 0), kernel, mode="valid")
              / np.maximum(np.convolve(good.astype(float), kernel, mode="valid"), 1e-9))
    centres = (edges[:-1] + edges[1:]) / 2
    total = np.nansum(smooth)
    length = np.abs(np.nansum(smooth * np.exp(1j * centres))) / total if total > 0 else np.nan
    return smooth, float(length)


# --- speed --------------------------------------------------------------------

def speed_tuning(session: Session, samples: np.ndarray, speed: np.ndarray,
                 min_time_s: float = 5.0) -> tuple[np.ndarray, float]:
    """Firing rate (Hz) by running speed, and its correlation with speed.

    Speed bins the rat spent less than `min_time_s` in are left out. The
    correlation is between the bin centres and the rates, weighted equally.
    """
    time = np.histogram(speed, bins=SPEED_EDGES)[0] * session.dt
    counts = np.histogram(speed[samples], bins=SPEED_EDGES)[0]
    with np.errstate(invalid="ignore", divide="ignore"):
        rate = np.where(time >= min_time_s, counts / time, np.nan)
    centres = (SPEED_EDGES[:-1] + SPEED_EDGES[1:]) / 2
    ok = ~np.isnan(rate)
    if ok.sum() < 4 or np.nanstd(rate[ok]) == 0:
        return rate, np.nan
    return rate, float(np.corrcoef(centres[ok], rate[ok])[0, 1])


# --- shuffling ----------------------------------------------------------------

def shifted(session: Session, spike_times: np.ndarray, rng: np.random.Generator) -> np.ndarray:
    """The spike train circularly shifted in time by a random amount.

    This keeps the cell's firing statistics and the rat's path but breaks the
    relation between them, which gives the chance level for each measure.
    """
    start, stop = session.t[0], session.t[-1]
    duration = stop - start
    shift = rng.uniform(MIN_SHIFT, duration - MIN_SHIFT)
    return np.sort((spike_times - start + shift) % duration + start)
