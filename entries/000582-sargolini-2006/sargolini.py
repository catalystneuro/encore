"""Data access and analysis helpers for dandiset 000582 (Sargolini et al. 2006).

`load_sessions` streams every file of the dandiset from the DANDI Archive and
returns positions and spike times as plain numpy arrays. `cell_measures` and
`pair_measures` compute, for every cell or pair of simultaneously recorded
cells, the measures the claims file asks for, under each reading it names.

Where each parameter comes from. "SOM" is the paper's Supporting Online
Material (Materials and Methods), as quoted in the claims file
(claims/000582/10.1126-science.1125572.yaml); O1 to O4 are the readings the
claims file lists for details the paper leaves open.

- Positions from the red LED, smoothed with a 15-point mean filter (SOM,
  Analysis of place fields). The files do not say which LED is red; LED1 is
  the only LED in the single-LED sessions, and the SOM says single-LED rats
  carried a red LED, so LED1 is taken as the red one.
- Rate maps: Gaussian kernel estimate with h = 3 cm, evaluated at the centre of
  each bin, positions more than 3 cm from the path unvisited (SOM). Bins of
  3 cm (reading O2a) or 1.5 cm (O2b).
- Autocorrelogram: Pearson correlation over lags, not estimated where fewer
  than 20 bins overlap (SOM).
- Gridness: peaks are contiguous pixels above r = 0.10 with an area of at
  least 100 pixels of 1.5 x 1.5 cm (225 cm2; 25 bins of 3 cm under O2a)
  (SOM). The circle around the outermost of the six peaks closest to the
  centre has a radius to that peak's centre plus its radius (O3a) or to its
  centre (O3b); the central peak is removed as its pixels (O3a) or as a disc
  of its radius around its centre (O3b) (claims file). Gridness =
  min(r60, r120) - max(r30, r90, r150) (SOM).
- A peak's centre is its pixel of highest correlation or the centroid of its
  pixels (`PEAK_CENTRES`), and its radius that of a disc of the same area or
  the largest distance from its centre to one of its pixels (`PEAK_RADII`):
  the readings the claims file names under O3. Both apply to the central peak
  as to the others. When the circle runs to the outer peak's centre and the
  central peak is removed as its pixels, no radius is used, so the radius
  readings give the same gridness and only one is kept (`GRID_READINGS`).
  Contiguity is 4-connected, the default of scipy.ndimage.label, a standard
  choice.
- Spacing: median distance from the centre to the (up to) six inner peaks;
  orientation: the smallest counterclockwise angle from the x axis to one of
  them (SOM), each with the peak centre of the reading (claims file, O3).
- Head direction from the two LEDs; tuning in 60 bins of 6 degrees,
  unsmoothed; peak rate is the highest bin (SOM). Watson's two-sample U2 of
  head direction at spikes against all tracked samples (SOM; claims file, O4),
  with the asymptotic p-value. Block correlation: Pearson correlation of the
  60-bin rates in odd against even minutes (SOM); a cell passes when r > 0 and
  the two-sided p is below the level (O4).
- Breadth of tuning: mean resultant length r of the 60-bin rate distribution
  (SOM). Both the angular deviation sqrt(2(1 - r)) and the circular standard
  deviation sqrt(-2 ln r) of Batschelet (1981), the SOM's reference S8, are
  returned, as the claims file does not say which "angular standard deviation"
  means (questions/000582.yaml).
- Speed in 1-s bins, unsmoothed (SOM); readings from the speed claim: path
  length or displacement over the bin, smoothed or raw positions.
- Trials (O1): the 20-minute files hold two 10-minute trials joined near 600 s
  (shown in the notebook); the split is placed at the jump in position within
  0.5 s of 600 s. "pooled" uses the whole file, "first" the first trial.
"""

from __future__ import annotations

import warnings
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from itertools import combinations

import numpy as np
from scipy import ndimage, signal, stats
from scipy.spatial import cKDTree

DANDISET = "000582"
VERSION = "0.251111.2151"

TRIAL_S = 600.0            # length of one trial, s (SOM: two 10-min trials)
MEAN_FILTER = 15           # position smoothing, samples (SOM)
KERNEL_H = 3.0             # Gaussian kernel of the rate map, cm (SOM)
UNVISITED_CM = 3.0         # bins farther than this from the path are unvisited (SOM)
MIN_OVERLAP = 20           # autocorrelogram bins needed at a lag (SOM)
PEAK_R = 0.10              # threshold for autocorrelogram peaks (SOM)
PEAK_AREA_CM2 = 100 * 1.5 * 1.5   # 100 pixels of 1.5 x 1.5 cm (SOM)
ANGLES = (30, 60, 90, 120, 150)   # rotations used by gridness (SOM)
HD_BINS = 60               # head-direction bins of 6 degrees (SOM)
SPEED_BIN_S = 1.0          # speed bins (SOM)
LOW_SPEED = 3.0            # cm/s, the paper's lowest velocity bin (main text)

BINS = {"3cm": 3.0, "1.5cm": 1.5}                 # O2
CIRCLES = ("enclose", "centre")                     # O3, circle radius
CENTRAL = ("blob", "disc")                          # O3, central peak removal
PEAK_CENTRES = ("max", "centroid")                  # O3, a peak's centre
PEAK_RADII = ("area", "farthest")                   # O3, a peak's radius
TRIALS = ("pooled", "first")                        # O1
GRID_KEYS = [f"{c}|{m}|{p}|{r}" for c in CIRCLES for m in CENTRAL for p in PEAK_CENTRES for r in PEAK_RADII
             if not (c == "centre" and m == "blob" and r == "farthest")]   # the radius is unused there
GRID_READINGS = [f"{b}|{k}" for b in BINS for k in GRID_KEYS]
SPEED_READINGS = [f"{s}|{p}" for s in ("path", "displacement") for p in ("smoothed", "raw")]


@dataclass
class Unit:
    name: str
    layer: str               # "II", "III", "V", "VI" or "" when not given
    depth_mm: float
    hemisphere: str
    spike_times: np.ndarray  # s

    @property
    def tetrode(self) -> str:
        return self.name.split("c")[0]


@dataclass
class Session:
    path: str
    subject: str
    session_id: str
    t: np.ndarray                  # position sample times, s
    red: np.ndarray                # LED1, cm, shape (n, 2), raw
    green: np.ndarray | None       # LED2, cm, or None
    units: list[Unit] = field(default_factory=list)
    description: str = ""

    @property
    def dt(self) -> float:
        return float(np.median(np.diff(self.t)))

    @property
    def duration(self) -> float:
        return float(self.t[-1] - self.t[0] + self.dt)

    @property
    def trials(self) -> list[tuple[float, float]]:
        """Start and end of each trial: two for the 20-minute files, split where the
        position jumps within 0.5 s of 600 s (shown in the notebook)."""
        end = self.t[-1] + self.dt
        if self.duration <= 1.5 * TRIAL_S:
            return [(self.t[0], end)]
        if not hasattr(self, "_split"):
            filled = np.column_stack([pd_ffill(self.red[:, i]) for i in range(2)])
            near = np.flatnonzero(np.abs(self.t[1:] - TRIAL_S) <= 0.5)
            steps = np.hypot(*(filled[near + 1] - filled[near]).T)
            self._split = float(self.t[near[np.nanargmax(steps)] + 1]) if np.isfinite(steps).any() else TRIAL_S
        return [(self.t[0], self._split), (self._split, end)]

    def window(self, reading: str) -> tuple[float, float]:
        """The time window of trial reading O1: the whole file or the first trial."""
        return (self.t[0], self.t[-1] + self.dt) if reading == "pooled" else self.trials[0]

    @property
    def xy(self) -> np.ndarray:
        """Red-LED positions smoothed with a 15-point mean filter, cm."""
        if not hasattr(self, "_xy"):
            self._xy = smooth_positions(self.red)
        return self._xy

    @property
    def head_direction(self) -> np.ndarray | None:
        """Head direction in radians from the two LEDs (raw positions), NaN where one is missing."""
        if self.green is None:
            return None
        d = self.green - self.red
        return np.arctan2(d[:, 1], d[:, 0])


def pd_ffill(x: np.ndarray) -> np.ndarray:
    """Carry the last valid value forward over missing samples."""
    idx = np.where(~np.isnan(x), np.arange(len(x)), 0)
    np.maximum.accumulate(idx, out=idx)
    return x[idx]


# --- loading ------------------------------------------------------------------

def _text(x) -> str:
    return x.decode() if isinstance(x, bytes) else str(x)


def _session_from_h5(path: str, f) -> Session:
    pos = f["processing/behavior/Position"]
    leds = {}
    for name in sorted(pos):
        data = pos[name]["data"]
        leds[name] = (data[:] * data.attrs["conversion"] * 100.0, pos[name]["timestamps"][:])
    red, t = leds["SpatialSeriesLED1"]
    green = leds["SpatialSeriesLED2"][0] if "SpatialSeriesLED2" in leds else None
    units_group = f["units"]
    index = units_group["spike_times_index"][:]
    spikes = np.split(units_group["spike_times"][:], index[:-1])
    units = [
        Unit(name=_text(n), layer=_text(h).replace("MEC L", "").strip(),
             depth_mm=float(d) * 1000, hemisphere=_text(s), spike_times=np.asarray(st, float))
        for n, h, d, s, st in zip(units_group["unit_name"][:], units_group["histology"][:],
                                  units_group["depth"][:], units_group["hemisphere"][:], spikes)
    ]
    return Session(path=path, subject=_text(f["general/subject/subject_id"][()]),
                   session_id=_text(f["general/session_id"][()]), t=t, red=red, green=green,
                   units=units, description=_text(f["session_description"][()]))


def asset_urls(version: str = VERSION) -> list[tuple[str, str]]:
    from dandi.dandiapi import DandiAPIClient

    with DandiAPIClient() as client:
        dandiset = client.get_dandiset(DANDISET, version)
        return sorted((a.path, a.get_content_url(follow_redirects=1, strip_query=True))
                      for a in dandiset.get_assets())


def load_sessions(version: str = VERSION, max_workers: int = 12) -> list[Session]:
    """Stream every file of the dandiset. Nothing is written to disk."""
    import h5py
    import remfile

    def load(asset):
        path, url = asset
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            with h5py.File(remfile.File(url), "r") as f:
                return _session_from_h5(path, f)

    with ThreadPoolExecutor(max_workers) as pool:
        return list(pool.map(load, asset_urls(version)))


# --- positions ----------------------------------------------------------------

def _fill(x: np.ndarray) -> np.ndarray:
    """Linearly interpolate over missing samples."""
    bad = np.isnan(x)
    if bad.any() and not bad.all():
        x = x.copy()
        x[bad] = np.interp(np.flatnonzero(bad), np.flatnonzero(~bad), x[~bad])
    return x


def smooth_positions(xy: np.ndarray, n: int = MEAN_FILTER) -> np.ndarray:
    """A centred n-point mean filter, after interpolating over missing samples."""
    return np.column_stack([ndimage.uniform_filter1d(_fill(xy[:, i]), n, mode="nearest")
                            for i in range(2)])


def sample_index(t: np.ndarray, times: np.ndarray) -> np.ndarray:
    """Index of the position sample nearest to each time."""
    idx = np.clip(np.searchsorted(t, times), 1, len(t) - 1)
    return np.where(times - t[idx - 1] < t[idx] - times, idx - 1, idx)


def in_window(times: np.ndarray, window: tuple[float, float]) -> np.ndarray:
    return times[(times >= window[0]) & (times < window[1])]


# --- rate maps and autocorrelograms -------------------------------------------

def map_edges(session: Session, bin_cm: float) -> tuple[np.ndarray, np.ndarray]:
    """Bin centres covering the tracked area of a file, the same for every map of the file."""
    lo = np.nanmin(session.xy, axis=0) - bin_cm
    hi = np.nanmax(session.xy, axis=0) + bin_cm
    return tuple(np.arange(lo[i], hi[i] + bin_cm / 2, bin_cm) for i in range(2))


def _kernel_weights(session: Session, bin_cm: float) -> tuple[np.ndarray, np.ndarray]:
    """Gaussian weight of every position sample at every bin centre, along x and along y,
    cached on the session."""
    cache = session.__dict__.setdefault("_weights", {})
    if bin_cm not in cache:
        cx, cy = map_edges(session, bin_cm)
        xy = session.xy.astype(np.float32)
        cache[bin_cm] = tuple(
            np.exp(-0.5 * ((xy[:, i, None] - c[None, :].astype(np.float32)) / KERNEL_H) ** 2)
            for i, c in enumerate((cx, cy)))
    return cache[bin_cm]


def rate_map(session: Session, sample_mask: np.ndarray, spike_times: np.ndarray,
             bin_cm: float) -> np.ndarray:
    """Kernel-smoothed rate map (Hz) at the bin centres, shape (nx, ny), NaN where unvisited.

    rate(x) = sum_i g((s_i - x)/h) / integral g((y(t) - x)/h) dt with a Gaussian g (SOM),
    computed exactly at each bin centre (the Gaussian is separable in x and y).
    """
    cx, cy = map_edges(session, bin_cm)
    wx, wy = _kernel_weights(session, bin_cm)
    idx = sample_index(session.t, spike_times)
    occupancy = (wx[sample_mask].T * session.dt) @ wy[sample_mask]
    counts = wx[idx].T @ wy[idx]
    with np.errstate(invalid="ignore", divide="ignore"):
        rate = (counts / occupancy).astype(float)
    xy = session.xy[sample_mask]
    gx, gy = np.meshgrid(cx, cy, indexing="ij")
    distance, _ = cKDTree(xy).query(np.column_stack([gx.ravel(), gy.ravel()]),
                                    distance_upper_bound=UNVISITED_CM + 1e-9)
    rate[(distance > UNVISITED_CM).reshape(rate.shape)] = np.nan
    return rate


def correlogram(a: np.ndarray, b: np.ndarray | None = None) -> np.ndarray:
    """Pearson correlation of map a with map b (a itself by default) at every lag.

    Shape (2 nx - 1, 2 ny - 1), lag 0 at the centre; NaN where fewer than 20 bins overlap.
    """
    b = a if b is None else b
    va, vb = ~np.isnan(a), ~np.isnan(b)
    x, y = np.where(va, a, 0.0), np.where(vb, b, 0.0)
    ma, mb = va.astype(float), vb.astype(float)

    def corr(p, q):
        return signal.correlate(p, q, mode="full", method="fft")

    n = np.round(corr(ma, mb))
    sx, sy = corr(x, mb), corr(ma, y)
    sxy = corr(x, y)
    sxx, syy = corr(x * x, mb), corr(ma, y * y)
    with np.errstate(invalid="ignore", divide="ignore"):
        r = (n * sxy - sx * sy) / (np.sqrt(n * sxx - sx ** 2) * np.sqrt(n * syy - sy ** 2))
    r[(n < MIN_OVERLAP) | ~np.isfinite(r)] = np.nan
    return r


def peaks(corr: np.ndarray, bin_cm: float) -> dict:
    """Fields of a correlogram above r = 0.10 with at least 225 cm2 (SOM).

    Returns the central peak's mask, and for the central peak and every other
    peak, under each centre reading, its centre (in bins, relative to the
    correlogram's centre) and its radius under each radius reading.
    """
    centre = np.array([(s - 1) / 2 for s in corr.shape])
    filled = np.nan_to_num(corr, nan=-1.0)
    labels, n = ndimage.label(filled > PEAK_R)
    min_area = PEAK_AREA_CM2 / bin_cm ** 2
    index = np.arange(1, n + 1)
    areas = ndimage.sum(np.ones_like(corr), labels, index)
    locs = {"centroid": np.array(ndimage.center_of_mass(np.ones_like(corr), labels, index)).reshape(-1, 2),
            "max": np.array(ndimage.maximum_position(filled, labels, index), dtype=float).reshape(-1, 2)}
    objects = ndimage.find_objects(labels)

    def describe(k):
        sl = objects[k]
        ii, jj = np.nonzero(labels[sl] == k + 1)
        pixels = np.column_stack([ii + sl[0].start, jj + sl[1].start]).astype(float)
        return {p: (locs[p][k] - centre,
                    {"area": np.sqrt(areas[k] / np.pi), "farthest": np.hypot(*(pixels - locs[p][k]).T).max()})
                for p in PEAK_CENTRES}

    central_label = labels[tuple(centre.astype(int))]
    out = dict(central=labels == central_label if central_label else np.zeros(corr.shape, bool),
               central_peak=describe(central_label - 1) if central_label else None,
               loc={p: [] for p in PEAK_CENTRES},
               radius={(p, r): [] for p in PEAK_CENTRES for r in PEAK_RADII})
    for k in range(n):
        if k + 1 == central_label or areas[k] < min_area:
            continue
        for p, (loc, radii) in describe(k).items():
            out["loc"][p].append(loc)
            for r, v in radii.items():
                out["radius"][(p, r)].append(v)
    out["count"] = len(out["loc"]["max"])
    out["loc"] = {p: np.array(v).reshape(-1, 2) for p, v in out["loc"].items()}
    out["radius"] = {k: np.array(v) for k, v in out["radius"].items()}
    return out


def _rotations(corr: np.ndarray) -> dict:
    filled = np.nan_to_num(corr)
    valid = (~np.isnan(corr)).astype(float)
    return {a: (ndimage.rotate(filled, a, reshape=False, order=1),
                ndimage.rotate(valid, a, reshape=False, order=1) > 0.99) for a in ANGLES}


def _area(found: dict, corr: np.ndarray, circle: str, central: str, p: str, r: str) -> np.ndarray:
    """The pixels gridness is computed on under one O3 reading: inside the circle around the
    outermost of the six peaks closest to the centre, outside the central peak."""
    centre = np.array([(s - 1) / 2 for s in corr.shape])
    ii, jj = np.indices(corr.shape)
    d = np.hypot(*found["loc"][p].T)
    nearest = np.argsort(d)[:6]
    outer = nearest[np.argmax(d[nearest])]
    radius = d[outer] + (found["radius"][(p, r)][outer] if circle == "enclose" else 0.0)
    if central == "blob" or found["central_peak"] is None:
        removed = found["central"]
    else:
        loc, radii = found["central_peak"][p]
        removed = np.hypot(ii - centre[0] - loc[0], jj - centre[1] - loc[1]) <= radii[r]
    return (np.hypot(ii - centre[0], jj - centre[1]) <= radius) & ~removed & ~np.isnan(corr)


def grid_measures(corr: np.ndarray, bin_cm: float) -> dict:
    """Gridness under every O3 reading, with spacing and orientation.

    Keys are "circle|central|centre|radius" (GRID_KEYS) for gridness and
    "spacing|centre", "orientation|centre" (cm and degrees). NaN when no peak
    besides the central one is found.
    """
    found = peaks(corr, bin_cm)
    out = {}
    if found["count"] == 0:
        out.update({k: np.nan for k in GRID_KEYS})
        for p in PEAK_CENTRES:
            out[f"spacing|{p}"] = out[f"orientation|{p}"] = np.nan
        return out
    rotated = _rotations(corr)
    for p in PEAK_CENTRES:
        d = np.hypot(*found["loc"][p].T)
        nearest = np.argsort(d)[:6]
        angles = np.degrees(np.arctan2(found["loc"][p][nearest, 1], found["loc"][p][nearest, 0])) % 360
        out[f"spacing|{p}"] = float(np.median(d[nearest]) * bin_cm)
        out[f"orientation|{p}"] = float(angles.min())
    for key in GRID_KEYS:
        area = _area(found, corr, *key.split("|"))
        corrs = {}
        for a, (values, ok) in rotated.items():
            use = area & ok
            corrs[a] = np.corrcoef(corr[use], values[use])[0, 1] if use.sum() > 2 else np.nan
        out[key] = float(min(corrs[60], corrs[120]) - max(corrs[30], corrs[90], corrs[150]))
    return out


def rotation_curve(corr: np.ndarray, bin_cm: float, step: int = 6) -> tuple[np.ndarray, np.ndarray]:
    """Correlation of the autocorrelogram with itself rotated in 6-degree steps (for figures),
    within the area of the first O3 reading (GRID_KEYS[0])."""
    found = peaks(corr, bin_cm)
    angles = np.arange(0, 181, step)
    if found["count"] == 0:
        return angles, np.full(len(angles), np.nan)
    area = _area(found, corr, *GRID_KEYS[0].split("|"))
    values = []
    for a in angles:
        rot = ndimage.rotate(np.nan_to_num(corr), a, reshape=False, order=1)
        ok = ndimage.rotate((~np.isnan(corr)).astype(float), a, reshape=False, order=1) > 0.99
        use = area & ok
        values.append(np.corrcoef(corr[use], rot[use])[0, 1])
    return angles, np.array(values)


def map_correlation(a: np.ndarray, b: np.ndarray) -> tuple[float, float]:
    """Pearson correlation of two rate maps, bin by bin (SOM), and its p-value."""
    ok = ~np.isnan(a) & ~np.isnan(b)
    if ok.sum() < 3 or np.std(a[ok]) == 0 or np.std(b[ok]) == 0:
        return np.nan, np.nan
    r, p = stats.pearsonr(a[ok], b[ok])
    return float(r), float(p)


# --- head direction -----------------------------------------------------------

HD_EDGES = np.linspace(-np.pi, np.pi, HD_BINS + 1)
HD_CENTRES = (HD_EDGES[:-1] + HD_EDGES[1:]) / 2


def hd_tuning(hd_samples: np.ndarray, hd_spikes: np.ndarray, dt: float) -> np.ndarray:
    """Firing rate (Hz) in 60 bins of 6 degrees, unsmoothed (SOM); NaN where never sampled."""
    time = np.histogram(hd_samples[~np.isnan(hd_samples)], HD_EDGES)[0] * dt
    count = np.histogram(hd_spikes[~np.isnan(hd_spikes)], HD_EDGES)[0]
    with np.errstate(invalid="ignore", divide="ignore"):
        return np.where(time > 0, count / time, np.nan)


def watson_u2_two_sample(a: np.ndarray, b: np.ndarray) -> tuple[float, float]:
    """Watson's two-sample U2 for circular data (Zar, Biostatistical Analysis, 27.5),
    with the p-value of its asymptotic distribution."""
    a, b = np.sort(a % (2 * np.pi)), np.sort(b % (2 * np.pi))
    n1, n2 = len(a), len(b)
    if n1 < 2 or n2 < 2:
        return np.nan, np.nan
    pooled = np.concatenate([a, b])
    order = np.argsort(pooled, kind="mergesort")
    from_a = order < n1
    d = np.cumsum(from_a) / n1 - np.cumsum(~from_a) / n2
    n = n1 + n2
    u2 = n1 * n2 / n ** 2 * (np.sum(d ** 2) - np.sum(d) ** 2 / n)
    return float(u2), u2_pvalue(u2)


def u2_pvalue(u2: float) -> float:
    """Upper tail of the asymptotic distribution of Watson's U2."""
    k = np.arange(1, 101)
    return float(np.clip(2 * np.sum((-1.0) ** (k - 1) * np.exp(-2 * k ** 2 * np.pi ** 2 * u2)), 0, 1))


def watson_u2_uniformity(angles: np.ndarray) -> tuple[float, float]:
    """Watson's one-sample U2 test of uniformity, and its critical value at p = 0.05
    for n angles (Stephens' modification for small samples, as in Zar 27.3)."""
    n = len(angles)
    u = np.sort(angles % (2 * np.pi)) / (2 * np.pi)
    i = np.arange(1, n + 1)
    u2 = np.sum((u - (2 * i - 1) / (2 * n)) ** 2) - n * (u.mean() - 0.5) ** 2 + 1 / (12 * n)
    critical = (0.187 / (1 + 0.8 / n)) + 0.1 / n - 0.1 / n ** 2
    return float(u2), float(critical)


def mean_vector(rates: np.ndarray) -> tuple[float, float]:
    """Direction (radians) and length of the mean vector of a 60-bin rate distribution (SOM)."""
    ok = ~np.isnan(rates)
    total = rates[ok].sum()
    if total <= 0:
        return np.nan, np.nan
    v = np.sum(rates[ok] * np.exp(1j * HD_CENTRES[ok])) / total
    return float(np.angle(v)), float(np.abs(v))


def angular_deviations(r: float) -> tuple[float, float]:
    """Batschelet's angular deviation sqrt(2(1 - r)) and circular standard deviation
    sqrt(-2 ln r), in degrees."""
    return float(np.degrees(np.sqrt(2 * (1 - r)))), float(np.degrees(np.sqrt(-2 * np.log(r))))


def circular_correlation(a: np.ndarray, b: np.ndarray) -> tuple[float, float]:
    """Circular-circular correlation of Jammalamadaka and SenGupta (2001, eq. 8.2.2),
    with its large-sample test."""
    abar = stats.circmean(a)
    bbar = stats.circmean(b)
    sa, sb = np.sin(a - abar), np.sin(b - bbar)
    r = np.sum(sa * sb) / np.sqrt(np.sum(sa ** 2) * np.sum(sb ** 2))
    n = len(a)
    l20, l02 = np.mean(sa ** 2), np.mean(sb ** 2)
    l22 = np.mean(sa ** 2 * sb ** 2)
    z = np.sqrt(n * l20 * l02 / l22) * r
    return float(r), float(2 * stats.norm.sf(abs(z)))


# --- speed --------------------------------------------------------------------

def speed_bins(session: Session, window: tuple[float, float], how: str,
               positions: str) -> tuple[np.ndarray, np.ndarray]:
    """Running speed (cm/s) in each 1-s bin of the window, unsmoothed, and the bins' start times.

    how: "path" (path length over the bin) or "displacement" (distance between the
    first and last sample of the bin); positions: "smoothed" (15-point mean filter) or
    "raw" (bins with a missing sample are dropped). A bin runs from its first sample to
    the first sample of the next bin, and never spans two trials.
    """
    xy = session.xy if positions == "smoothed" else session.red
    speeds, starts = [], []
    for t0, t1 in session.trials:
        lo, hi = max(t0, window[0]), min(t1, window[1])
        last = np.searchsorted(session.t, hi) - 1          # last sample of the trial
        for start in np.arange(lo, hi - SPEED_BIN_S + 1e-9, SPEED_BIN_S):
            i0, i1 = np.searchsorted(session.t, [start, start + SPEED_BIN_S])
            seg = xy[i0:min(i1, last) + 1]
            if len(seg) < 2 or np.isnan(seg).any():
                continue
            elapsed = session.t[i0 + len(seg) - 1] - session.t[i0]
            if how == "path":
                dist = np.sum(np.hypot(*np.diff(seg, axis=0).T))
            else:
                dist = np.hypot(*(seg[-1] - seg[0]))
            speeds.append(dist / elapsed)
            starts.append(start)
    return np.array(speeds), np.array(starts)


def speed_regression(speed: np.ndarray, starts: np.ndarray, spike_times: np.ndarray) -> dict:
    """Linear regression of firing rate on speed over 1-s bins (SOM), with Pearson and
    Spearman p-values, and the mean rate in the bins from 0 to 3 cm/s."""
    spikes = np.sort(spike_times)
    counts = np.searchsorted(spikes, starts + SPEED_BIN_S) - np.searchsorted(spikes, starts)
    rate = counts / SPEED_BIN_S
    fit = stats.linregress(speed, rate)
    low = speed <= LOW_SPEED
    return dict(slope=fit.slope, intercept=fit.intercept, r=fit.rvalue, p_linear=fit.pvalue,
                p_spearman=stats.spearmanr(speed, rate).pvalue,
                low_rate=float(rate[low].mean()) if low.any() else np.nan,
                low_bins=int(low.sum()), low_spikes=int(counts[low].sum()))


# --- per cell -----------------------------------------------------------------

def _grid_set(session, mask, spikes, prefix: str, out: dict, keep_maps: dict | None = None):
    for bname, b in BINS.items():
        m = rate_map(session, mask, spikes, b)
        if keep_maps is not None:
            keep_maps[bname] = m
        g = grid_measures(correlogram(m), b)
        for k, v in g.items():
            out[f"{prefix}|{bname}|{k}"] = v
    return out


def cell_measures(session: Session, unit: Unit, speed_cache: dict | None = None,
                  maps: dict | None = None) -> dict:
    """Every measure of one cell under every reading.

    Keys: "grid|T|bin|circle|central|centre|radius" (gridness), "spacing|T|bin|centre",
    "orientation|T|bin|centre"; head direction "u2|T", "u2_p|T", "block_r|T",
    "block_p|T", "peak_rate|T", "peak_dir|T", "mv_dir|T", "mv_r|T", "ang_dev|T",
    "circ_sd|T", "bg_min|T", "bg_far|T"; speed "slope|T|how|positions" and so on;
    stability "within|trial|split|bin|..." and "between|...". T is the O1 reading.
    """
    out = dict(subject=session.subject, path=session.path, session=session.session_id,
               unit=unit.name, tetrode=unit.tetrode, layer=unit.layer, depth_mm=unit.depth_mm,
               hemisphere=unit.hemisphere,
               two_leds=session.green is not None, trials=len(session.trials),
               spikes=len(unit.spike_times))
    hd = session.head_direction
    for T in TRIALS:
        window = session.window(T)
        mask = (session.t >= window[0]) & (session.t < window[1])
        spikes = in_window(unit.spike_times, window)
        out[f"rate|{T}"] = len(spikes) / (window[1] - window[0])
        cell_maps = {} if maps is not None else None
        g = _grid_set(session, mask, spikes, "g", {}, cell_maps)
        if maps is not None:
            maps[T] = cell_maps
        for k, v in g.items():
            _, bname, *rest = k.split("|")
            if rest[0] in ("spacing", "orientation"):
                out[f"{rest[0]}|{T}|{bname}|{rest[1]}"] = v
            else:
                out[f"grid|{T}|{bname}|{'|'.join(rest)}"] = v
        if hd is not None:
            hd_s = hd[mask]
            hd_k = hd[sample_index(session.t, spikes)]
            u2, p = watson_u2_two_sample(hd_k[~np.isnan(hd_k)], hd_s[~np.isnan(hd_s)])
            tuning = hd_tuning(hd_s, hd_k, session.dt)
            minute = np.floor((session.t[mask] - window[0]) / 60).astype(int)
            spike_minute = np.floor((spikes - window[0]) / 60).astype(int)
            odd = hd_tuning(hd_s[minute % 2 == 0], hd_k[spike_minute % 2 == 0], session.dt)
            even = hd_tuning(hd_s[minute % 2 == 1], hd_k[spike_minute % 2 == 1], session.dt)
            ok = ~np.isnan(odd) & ~np.isnan(even)
            if ok.sum() > 2 and np.std(odd[ok]) > 0 and np.std(even[ok]) > 0:
                br, bp = stats.pearsonr(odd[ok], even[ok])
            else:
                br, bp = np.nan, np.nan
            direction, length = mean_vector(tuning)
            peak = int(np.nanargmax(tuning)) if np.nanmax(tuning) > 0 else 0
            far = np.abs(np.angle(np.exp(1j * (HD_CENTRES - HD_CENTRES[peak])))) > np.pi / 2
            ad, csd = angular_deviations(length)
            out.update({f"u2|{T}": u2, f"u2_p|{T}": p, f"block_r|{T}": br, f"block_p|{T}": bp,
                        f"peak_rate|{T}": float(np.nanmax(tuning)), f"peak_dir|{T}": HD_CENTRES[peak],
                        f"mv_dir|{T}": direction, f"mv_r|{T}": length, f"ang_dev|{T}": ad,
                        f"circ_sd|{T}": csd, f"bg_min|{T}": float(np.nanmin(tuning)),
                        f"bg_far|{T}": float(np.nanmean(tuning[far]))})
        for sr in SPEED_READINGS:
            how, positions = sr.split("|")
            key = (session.path, T, sr)
            if speed_cache is not None and key in speed_cache:
                speed, starts = speed_cache[key]
            else:
                speed, starts = speed_bins(session, window, how, positions)
                if speed_cache is not None:
                    speed_cache[key] = (speed, starts)
            for k, v in speed_regression(speed, starts, spikes).items():
                out[f"{k}|{T}|{sr}"] = v
    # stability within each trial (halves, odd and even minutes) and between trials
    trial_maps = {}
    for k, (t0, t1) in enumerate(session.trials):
        spikes = in_window(unit.spike_times, (t0, t1))
        mid = (t0 + t1) / 2
        minute = np.floor((session.t - t0) / 60).astype(int)
        spike_minute = np.floor((spikes - t0) / 60).astype(int)
        inside = (session.t >= t0) & (session.t < t1)
        splits = {
            "halves": ((inside & (session.t < mid), spikes[spikes < mid]),
                       (inside & (session.t >= mid), spikes[spikes >= mid])),
            "minutes": ((inside & (minute % 2 == 0), spikes[spike_minute % 2 == 0]),
                        (inside & (minute % 2 == 1), spikes[spike_minute % 2 == 1])),
        }
        for split, parts in splits.items():
            for bname, b in BINS.items():
                pm = [rate_map(session, m, s, b) for m, s in parts]
                r, p = map_correlation(*pm)
                out[f"within|{k}|{split}|{bname}|r"] = r
                out[f"within|{k}|{split}|{bname}|p"] = p
                for half, m in enumerate(pm):
                    for gk, gv in grid_measures(correlogram(m), b).items():
                        if "|" in gk and not gk.startswith(("spacing", "orientation")):
                            out[f"within|{k}|{split}|{bname}|{half}|{gk}"] = gv
        if len(session.trials) == 2:
            trial_maps[k] = {bname: rate_map(session, inside, spikes, b) for bname, b in BINS.items()}
    if len(session.trials) == 2:
        for bname, b in BINS.items():
            r, p = map_correlation(trial_maps[0][bname], trial_maps[1][bname])
            out[f"between|{bname}|r"] = r
            out[f"between|{bname}|p"] = p
            for gk, gv in grid_measures(correlogram(trial_maps[1][bname]), b).items():
                if not gk.startswith(("spacing", "orientation")):
                    out[f"between|{bname}|trial2|{gk}"] = gv
        if hd is not None:
            for k, (t0, t1) in enumerate(session.trials):
                inside = (session.t >= t0) & (session.t < t1)
                spikes = in_window(unit.spike_times, (t0, t1))
                tuning = hd_tuning(hd[inside], hd[sample_index(session.t, spikes)], session.dt)
                out[f"trial_tuning|{k}"] = tuning
                out[f"trial_peak_dir|{k}"] = (HD_CENTRES[int(np.nanargmax(tuning))]
                                              if np.nanmax(tuning) > 0 else np.nan)
    return out


def pair_measures(session: Session, maps: dict) -> list[dict]:
    """For every pair of cells of a file: the displacement from the centre of the peak of
    their rate-map crosscorrelogram nearest the centre, in cm, per trial reading, bin size
    and peak centre. Peaks as for gridness (r > 0.10, 225 cm2), the central field included."""
    rows = []
    for (i, a), (j, b) in combinations(enumerate(session.units), 2):
        row = dict(path=session.path, subject=session.subject, unit_a=a.name, unit_b=b.name)
        for T in TRIALS:
            for bname, bin_cm in BINS.items():
                corr = correlogram(maps[i][T][bname], maps[j][T][bname])
                centre = np.array([(s - 1) / 2 for s in corr.shape])
                labels, n = ndimage.label(np.nan_to_num(corr, nan=-1.0) > PEAK_R)
                if n == 0:
                    for p in PEAK_CENTRES:
                        row[f"offset|{T}|{bname}|{p}"] = np.nan
                    continue
                index = np.arange(1, n + 1)
                areas = ndimage.sum(np.ones_like(corr), labels, index)
                big = index[areas >= PEAK_AREA_CM2 / bin_cm ** 2]
                locs = {
                    "max": np.array(ndimage.maximum_position(np.nan_to_num(corr, nan=-1.0), labels, big), float).reshape(-1, 2),
                    "centroid": np.array(ndimage.center_of_mass(np.ones_like(corr), labels, big)).reshape(-1, 2),
                }
                for p, loc in locs.items():
                    d = np.hypot(*(loc - centre).T) * bin_cm if len(loc) else np.array([np.nan])
                    row[f"offset|{T}|{bname}|{p}"] = float(np.nanmin(d)) if len(loc) else np.nan
        rows.append(row)
    return rows


def session_measures(session: Session) -> tuple[list[dict], list[dict]]:
    """cell_measures for every cell of a file, and pair_measures for its pairs."""
    speed_cache, cells, maps = {}, [], []
    for unit in session.units:
        m = {}
        cells.append(cell_measures(session, unit, speed_cache, m))
        maps.append(m)
    return cells, pair_measures(session, maps)


def lagged_u2(session: Session, unit: Unit, lags_s: np.ndarray) -> np.ndarray:
    """Watson U2 of head direction at spikes shifted by each lag, against all samples."""
    hd = session.head_direction
    ok = ~np.isnan(hd)
    out = []
    for lag in lags_s:
        spikes = unit.spike_times + lag
        spikes = spikes[(spikes >= session.t[0]) & (spikes <= session.t[-1])]
        k = hd[sample_index(session.t, spikes)]
        out.append(watson_u2_two_sample(k[~np.isnan(k)], hd[ok])[0])
    return np.array(out)


def lagged_map_info(session: Session, unit: Unit, lags_s: np.ndarray) -> np.ndarray:
    """Spatial information (bits/spike, SOM's formula) of the 3-cm rate map with spikes
    shifted by each lag."""
    mask = np.ones(len(session.t), bool)
    out = []
    for lag in lags_s:
        spikes = unit.spike_times + lag
        spikes = spikes[(spikes >= session.t[0]) & (spikes <= session.t[-1])]
        rate = rate_map(session, mask, spikes, BINS["3cm"])
        cx, cy = map_edges(session, BINS["3cm"])
        occ = np.histogram2d(*session.xy.T, bins=[np.append(cx - 1.5, cx[-1] + 1.5),
                                                  np.append(cy - 1.5, cy[-1] + 1.5)])[0]
        ok = ~np.isnan(rate) & (occ > 0)
        p = occ[ok] / occ[ok].sum()
        lam = rate[ok]
        mean = np.sum(p * lam)
        with np.errstate(divide="ignore", invalid="ignore"):
            info = np.nansum(p * lam / mean * np.log2(lam / mean))
        out.append(info)
    return np.array(out)


# --- cell classes ---------------------------------------------------------------

LEVELS = (0.05, 0.01)       # O4


def classify(cells, trial: str, grid_reading: str, level: float):
    """Cell classes of table S1 under one combination of readings (O1 to O4).

    grid: gridness above 0 (SOM). hd: two-LED cell with a significant Watson U2 and a
    positive, significant block correlation (SOM). conj: both. pure_hd: hd and not grid.
    grid_only: grid and not conjunctive, which includes the grid cells of single-LED rats
    (the speed claim's grid class).
    """
    import pandas as pd

    grid = cells[f"grid|{trial}|{grid_reading}"] > 0
    hd = (cells.two_leds & (cells[f"u2_p|{trial}"] < level) & (cells[f"block_r|{trial}"] > 0)
          & (cells[f"block_p|{trial}"] < level))
    return pd.DataFrame(dict(grid=grid, hd=hd, conj=grid & hd, pure_hd=hd & ~grid,
                             grid_only=grid & ~(grid & hd)), index=cells.index)


def readings(with_grid: bool = True, with_level: bool = True) -> list[tuple]:
    """Every combination of the trial (O1), gridness (O2, O3) and
    significance (O4) readings."""
    out = []
    for trial in TRIALS:
        for g in (GRID_READINGS if with_grid else [None]):
            for level in (LEVELS if with_level else [None]):
                out.append((trial, g, level))
    return out
