"""Loading and measures for EBRAINS dataset 10.25493/Q0FG-1X8 (v1).

Nagelhus, Andersson, Gonzalo Cogno, Moser & Moser (2023), "Object-centered population coding in
CA1 of the hippocampus", Neuron 111, 2091-2104, doi:10.1016/j.neuron.2023.04.008.

The dataset holds eight MATLAB files: four "single cell" files (CA1 and CA3 object sessions, CA1
and CA3 control sessions; each cell appears once) and four "population" files, one per rat, with
the No Object and Object trials of the sessions used for decoding. Each trial has tracking
(timestamps in s, x and y; the stored unit string, a MATLAB `string` object, reads "centimeters"),
the object position in object trials, and spike times per unit. The files are streamed from the
EBRAINS data proxy at the pinned version and read in memory; nothing is written to disk.

Where the parameters come from (claims file claims/ebrains-q0fg-1x8/10.1016-j.neuron.2023.04.008.yaml,
"opening comment", which cites the paper's Methods and code):

- Single-cell rate maps: 2.5 cm bins, Gaussian smoothing with SD 2 bins, epochs with speed above
  2.5 cm/s (Methods, Firing rate maps). Firing fields: contiguous bins above 3 x the median
  absolute deviation of all bins, at least 225 cm2, rate of at least 1 Hz (Methods).
- Every rate map (opening comment, "Smoothing and unvisited bins", from the Methods and
  calculateRateMap.m; called rm b there): the rate per bin (spikes over time), 0 in unvisited
  bins, then smoothed with the mirrored map padding the edges (smoothData.m); blanked maps have
  the unvisited bins set to NaN after smoothing. The time per position sample is the gap to the
  next sample, clipped at 0.1 s (maxGap); a spike is counted at the last position sample at or
  before it (histc).
- Template matching: 3 cm bins over 0 to 150 cm (50 x 50), smoothing 2 bins, unvisited bins not
  blanked; Gaussian templates at 9 offsets x 8 directions (0 offset once) and 8 widths, 500
  shuffled locations per width drawn uniformly in the arena and used in both trials; 99th
  percentile (Methods, Template matching; code rateMapData.m, shuffledTemplateMatchingScore.m).
- Decoders: 3 cm bins, smoothing 2 bins, each trial split at the midpoint of its position time
  span, 1 s testing bins from the start of the testing half, 5 equal-sample distance bins per
  trial and iteration with edges 0 and each group's largest distance, a prior restricted to the
  spatial bins strictly between the edges, ties left out (Methods; code distanceDecoder.m,
  equalDistanceEdges.m, calculateDecodingAccuracy.m).

Readings the claims file leaves open, run side by side (see the questions file
questions/ebrains-q0fg-1x8.yaml, and each claim's criterion):

- `speed`: for the decoders, "a" rate maps and occupancy from epochs above 2.5 cm/s, "b" no speed
  filter (claims file, distance decoder).
- `field`: "a" a field's peak is at least 1 Hz; "b" every bin of a field is at least 1 Hz.

Standard choices for details that cannot change a result (stated here once): speed from the
gradient of position over time; tracking samples without a position are dropped with their time,
and a spike whose position sample has none gets no position; the last sample of a trial stands for
the median sampling interval; the Gaussian kernel is truncated at 4 SD (smoothData.m's width is
not given); rates floored at 1e-10 Hz inside the Poisson log-likelihood (in place of log 0);
tracking resampled to 25 Hz for the behavioural decoders drops grid points more than 0.2 s from a
valid sample.
"""

from __future__ import annotations

import io
import json
import re

import fsspec
import numpy as np
import scipy.io as sio
from scipy import ndimage, sparse, stats
from scipy.special import gammaln, logsumexp, digamma, polygamma

KG_ID = "0162668e-bef0-4754-8562-40440db5bc0c"
DATASET_ID = "Q0FG-1X8"
DATASET_DOI = "10.25493/Q0FG-1X8"
DATASET_VERSION = "v1"
BASE = f"https://data-proxy.ebrains.eu/api/v1/public/datasets/{KG_ID}"
ARENA = 150.0
SPEED_MIN = 2.5          # cm/s, Methods, Firing rate maps
MAX_GAP = 0.1            # s, largest time per position sample (calculateRateMap.m, maxGap)
MAX_INTERP_GAP = 0.2     # s, standard choice (see docstring)
LUT_STEP = 0.01          # s, grid of the spike-to-sample lookup (speed only; the result is exact)
LAMBDA_FLOOR = 1e-10     # Hz, standard choice

SINGLE_FILES = {"CA1": "singlecellanalyses_CA1", "CA3": "singlecellanalyses_CA3",
                "CON_CA1": "singlecellanalyses_controls_CA1", "CON_CA3": "singlecellanalyses_controls_CA3"}
POP_FILES = ["populationanalyses_25987", "populationanalyses_26186",
             "populationanalyses_27012", "populationanalyses_27207"]


# ----------------------------------------------------------------------------------------------
# Reading the archive

def list_files() -> list[dict]:
    """The dataset's file list from the data proxy (name, bytes, md5 hash, last modified)."""
    with fsspec.open(f"{BASE}?limit=500", "rb") as f:
        return json.loads(f.read())["objects"]


def read_bytes(path: str) -> bytes:
    with fsspec.open(f"{BASE}/{path}", "rb", block_size=2 ** 24) as f:
        return f.read()


def _units_strings(mat: dict) -> list[str]:
    """Decode the MATLAB `string` objects (tracking_units) from the file's function workspace."""
    fw = mat.get("__function_workspace__")
    if fw is None:
        return []
    text = fw.tobytes().decode("utf-16-le", errors="ignore")
    return re.findall(r"[A-Za-z]{2,}", text)


def _L(x):
    return list(np.atleast_1d(x))


class Trial:
    """One trial: valid tracking samples and the spikes of every unit, reduced to what is used."""

    def __init__(self, name, t, x, y, obj, spikes):
        t = np.asarray(t, float)
        x = np.asarray(x, float)
        y = np.asarray(y, float)
        self.name = name
        self.n_samples_raw = len(t)
        ok = np.isfinite(x) & np.isfinite(y) & np.isfinite(t)
        self.n_nan = int((~ok).sum())
        # Time per position sample: the gap to the next sample, clipped at MAX_GAP (calculateRateMap.m,
        # maxGap), over all samples; samples without a position then drop out with their time.
        gap = np.diff(t)
        gap = np.append(gap, np.nanmedian(gap) if len(gap) else 0.0)
        gap = np.where(np.isfinite(gap), np.clip(gap, 0.0, MAX_GAP), 0.0)
        self.t, self.x, self.y, self.sdt = t[ok], x[ok], y[ok], gap[ok]
        self.t0, self.t1 = float(t[0]), float(t[-1])
        self.dt = float(np.median(np.diff(t)))
        # raw samples and the index of each among the valid ones (-1 without a position), for
        # assigning spikes to the last sample at or before them (histc in calculateRateMap.m)
        self._t_raw = np.where(np.isfinite(t), t, -np.inf)
        self._raw2valid = np.where(ok, np.cumsum(ok) - 1, -1)
        if len(self.t) > 2:
            vx = np.gradient(self.x, self.t)
            vy = np.gradient(self.y, self.t)
            self.speed = np.hypot(vx, vy)
        else:
            self.speed = np.zeros(len(self.t))
        self.obj = obj
        self.n_unsorted = 0
        self.spikes, self.spike_si = [], []
        for s in spikes:
            s = np.atleast_1d(np.asarray(s, float))
            if np.any(np.diff(s) < 0):
                self.n_unsorted += 1
                s = np.sort(s)
            self.spikes.append(s)
            self.spike_si.append(self._sample_index(s))

    def _sample_index(self, s):
        """Index of the valid tracking sample each spike is counted at: the last sample at or before
        the spike (histc), -1 when that sample has no position or the spike lies outside the
        tracking (before the first sample, or after the last)."""
        if len(self.t) == 0:
            return np.full(len(s), -1)
        tr = self._t_raw
        if getattr(self, "_lut", None) is None:
            # last sample at or before each point of a 10 ms grid, to start the search from
            start = tr[0]
            grid = start + LUT_STEP * np.arange(int(np.ceil((tr[-1] - start) / LUT_STEP)) + 2)
            self._lut = (start, (np.searchsorted(tr, grid, side="right") - 1).astype(np.int64))
        start, lut = self._lut
        c = np.clip(np.floor((s - start) / LUT_STEP).astype(np.int64), 0, len(lut) - 1)
        j = lut[c]
        while True:
            nxt = j + 1 < len(tr)
            nxt[nxt] = tr[j[nxt] + 1] <= s[nxt]
            if not nxt.any():
                break
            j = j + nxt
        out = np.where((s >= start) & (s <= tr[-1]), self._raw2valid[j], -1)
        return out

    @property
    def n_units(self):
        return len(self.spikes)

    @property
    def duration(self):
        return self.t1 - self.t0

    def subset(self, units):
        """A copy with only the given units."""
        new = object.__new__(Trial)
        new.__dict__.update(self.__dict__)
        new.spikes = [self.spikes[u] for u in units]
        new.spike_si = [self.spike_si[u] for u in units]
        return new

    def window(self, a, b):
        """A pseudo-trial holding the samples and spikes in [a, b)."""
        new = object.__new__(Trial)
        new.__dict__.update(self.__dict__)
        m = (self.t >= a) & (self.t < b)
        idx = np.flatnonzero(m)
        remap = np.full(len(self.t), -1)
        remap[idx] = np.arange(len(idx))
        new.t, new.x, new.y, new.speed = self.t[m], self.x[m], self.y[m], self.speed[m]
        new.sdt = self.sdt[m]
        mr = (self._t_raw >= a) & (self._t_raw < b)
        r2v = self._raw2valid[mr]
        new._t_raw = self._t_raw[mr]
        new._raw2valid = np.where(r2v >= 0, remap[np.maximum(r2v, 0)], -1)
        new._lut = None
        new.t0, new.t1 = float(a), float(b)
        new.spikes, new.spike_si = [], []
        for s, si in zip(self.spikes, self.spike_si):
            k = (s >= a) & (s < b)
            new.spikes.append(s[k])
            ss = si[k]
            new.spike_si.append(np.where(ss >= 0, remap[np.maximum(ss, 0)], -1))
        return new


class Session:
    def __init__(self, file, index, rat, technique, trials):
        self.file, self.index, self.rat, self.technique, self.trials = file, index, rat, technique, trials

    @property
    def n_units(self):
        return self.trials[0].n_units

    def trial(self, name):
        for t in self.trials:
            if t.name == name:
                return t
        return None

    @property
    def key(self):
        return f"{self.file.replace('analyses', '')}#{self.index}"


TRIAL_CODES = {"no object": "NO", "object": "O", "object moved": "OM", "no object'": "NOp",
               "control 1": "CON1", "control 2": "CON2", "control 3": "CON3", "control 4": "CON4"}


def load(name: str) -> tuple[list[Session], dict]:
    """Read one file of the dataset into Sessions. Returns the sessions and file-level metadata."""
    raw = read_bytes(f"datasets/{name}.mat")
    mat = sio.loadmat(io.BytesIO(raw), squeeze_me=True, struct_as_record=False)
    d = mat["dataset"]
    out = []
    for i, s in enumerate(_L(d.sessions)):
        trials = []
        for tr in _L(s.trial):
            nm = getattr(tr, "trial_name", None) or getattr(tr, "name", None)
            op = getattr(tr, "object_position", None)
            obj = (float(op.x), float(op.y)) if hasattr(op, "x") else None
            trials.append(Trial(TRIAL_CODES.get(nm, nm), tr.tracking.timestamp, tr.tracking.x,
                                tr.tracking.y, obj, [u.spike_timestamps for u in _L(tr.units)]))
        rat = getattr(s, "rat_id", None) or getattr(d, "rat_id", "")
        tech = getattr(s, "recording_technique", None) or getattr(d, "recording_technique", "")
        out.append(Session(name, i, str(rat), str(tech), trials))
    meta = {"description": str(d.description), "bytes": len(raw), "units_strings": sorted(set(_units_strings(mat)))}
    return out, meta


def spike_hash(trial: Trial, u: int) -> bytes:
    return np.round(trial.spikes[u], 4).tobytes()


def link_population(pop: Session, single_sessions: list[Session]):
    """Match a population session to the single-cell session of the same recording, and its units
    to the single-cell units whose No Object spike train is identical. Returns (session, map)."""
    t0 = pop.trials[0].t0
    for s in single_sessions:
        if abs(s.trials[0].t0 - t0) < 1e-6 and len(s.trials[0].t) == len(pop.trials[0].t):
            h = {spike_hash(s.trials[0], u): u for u in range(s.n_units)}
            m = {u: h.get(spike_hash(pop.trials[0], u)) for u in range(pop.n_units)}
            return s, {k: v for k, v in m.items() if v is not None}
    return None, {}


# ----------------------------------------------------------------------------------------------
# Rate maps

def nbins(bin_cm):
    return int(round(ARENA / bin_cm))


def bin_index(x, y, bin_cm):
    nb = nbins(bin_cm)
    ix = np.clip((x // bin_cm).astype(int), 0, nb - 1)
    iy = np.clip((y // bin_cm).astype(int), 0, nb - 1)
    return iy * nb + ix


def bin_centres(bin_cm):
    nb = nbins(bin_cm)
    c = (np.arange(nb) + 0.5) * bin_cm
    X, Y = np.meshgrid(c, c)        # [iy, ix]
    return X.ravel(), Y.ravel()


def sample_mask(trial: Trial, speed_filter: bool, a=None, b=None):
    m = np.ones(len(trial.t), bool)
    if speed_filter:
        m &= trial.speed > SPEED_MIN
    if a is not None:
        m &= trial.t >= a
    if b is not None:
        m &= trial.t < b
    return m


def raw_maps(trial: Trial, mask, bin_cm, units=None):
    """Time (s) and spike-count maps from the samples in `mask`. Returns occ (B,), spk (U, B)."""
    nb = nbins(bin_cm)
    B = nb * nb
    bidx = bin_index(trial.x, trial.y, bin_cm)
    occ = np.bincount(bidx[mask], weights=trial.sdt[mask], minlength=B)
    units = range(trial.n_units) if units is None else units
    rows, cols = [], []
    for k, u in enumerate(units):
        si = trial.spike_si[u]
        si = si[si >= 0]
        si = si[mask[si]]
        rows.append(np.full(len(si), k))
        cols.append(bidx[si])
    rows = np.concatenate(rows) if rows else np.zeros(0, int)
    cols = np.concatenate(cols) if cols else np.zeros(0, int)
    spk = np.bincount(rows * B + cols, minlength=len(units) * B).reshape(len(units), B).astype(float)
    return occ.astype(float), spk


def _gauss(a, sigma=2.0):
    """Gaussian smoothing over the last two axes (maps of shape (..., nb, nb)), edges padded with
    the mirrored map (smoothData.m), truncated at 4 SD."""
    sig = (0,) * (a.ndim - 2) + (sigma, sigma)
    return ndimage.gaussian_filter(a, sig, mode="reflect", truncate=4.0)


def _raw_rate(O, S):
    """Spikes over time per bin, 0 where the animal never was (countRaw ./ (timeRaw + eps))."""
    visited = O > 0
    with np.errstate(invalid="ignore", divide="ignore"):
        return np.where(visited, S / np.where(visited, O, 1.0), 0.0), visited


def rate_maps(occ, spk, rm="b", blank=True, sigma=2.0):
    """Smoothed rate maps (U, B) from time (B,) and spike (U, B) maps, by the claims file's method
    ("Smoothing and unvisited bins", rm b; calculateRateMap.m): the rate per bin, unvisited bins 0,
    smoothed; blanked maps have NaN where the animal never was."""
    if rm != "b":
        raise ValueError(f"rate-map reading {rm!r}: only b, the paper's method, is defined")
    B = occ.shape[-1]
    nb = int(round(np.sqrt(B)))
    raw, visited = _raw_rate(occ.reshape(nb, nb), spk.reshape(-1, nb, nb))
    r = _gauss(raw, sigma)
    if blank:
        r = np.where(visited[None], r, np.nan)
    return r.reshape(-1, B)


def mean_rate(trial: Trial, u: int, speed_filter: bool, mask=None):
    """Spikes over time: the speed-filtered epochs (reading a of rate overlap) or the whole trial."""
    m = sample_mask(trial, speed_filter) if mask is None else mask
    si = trial.spike_si[u]
    if speed_filter or mask is not None:
        n = np.sum(m[si[si >= 0]])
        T = trial.sdt[m].sum()
    else:
        n = len(trial.spikes[u])
        T = trial.duration
    return n / T if T > 0 else np.nan


def pearson_nan(a, b):
    """Pearson correlation over the bins with a value in both maps."""
    ok = np.isfinite(a) & np.isfinite(b)
    if ok.sum() < 3:
        return np.nan
    a, b = a[ok], b[ok]
    if a.std() == 0 or b.std() == 0:
        return np.nan
    return float(np.corrcoef(a, b)[0, 1])


def rate_overlap(r1, r2):
    lo, hi = min(r1, r2), max(r1, r2)
    return lo / hi if hi > 0 else np.nan


def spatial_information(rmap, occ, rate, duration=None):
    """Skaggs information in bits per spike (Methods, Spatial information content). Pi is the time
    in bin i over the summed time (duration None, lambda reading si-a) or over the trial's duration
    (si-b; then `rate` is ignored and lambda is sum Pi li, the claims file's fig7 criterion)."""
    ok = np.isfinite(rmap) & (occ > 0)
    P = occ[ok] / (occ[ok].sum() if duration is None else duration)
    l = rmap[ok]
    if duration is not None:
        rate = float(np.sum(P * l))
    if rate <= 0:
        return np.nan
    with np.errstate(divide="ignore", invalid="ignore"):
        terms = np.where(l > 0, P * l * np.log2(l / rate), 0.0)
    return float(terms.sum() / rate)


# ----------------------------------------------------------------------------------------------
# Firing fields

def fields(rmap, bin_cm=2.5, field="a"):
    """Firing fields of a blanked map: contiguous bins above 3 x MAD of all bins, at least 225 cm2,
    rate at least 1 Hz (reading a: the field's peak; b: every bin). Returns a list of bin-index arrays."""
    v = rmap[np.isfinite(rmap)]
    if v.size == 0:
        return []
    mad = np.median(np.abs(v - np.median(v)))
    thr = 3 * mad
    if field == "b":
        thr = max(thr, 1.0)
    nb = nbins(bin_cm)
    img = np.nan_to_num(rmap, nan=-np.inf).reshape(nb, nb)
    lab, n = ndimage.label(img > thr, structure=np.ones((3, 3)))
    out = []
    min_bins = 225.0 / bin_cm ** 2
    for k in range(1, n + 1):
        idx = np.flatnonzero(lab.ravel() == k)
        if len(idx) < min_bins - 1e-9:
            continue
        if field == "a" and np.nanmax(rmap[idx]) < 1.0:
            continue
        out.append(idx)
    return out


def field_geometry(idx, rmap, obj, bin_cm=2.5):
    """Centroid (mean of bin centres), peak bin centre, their distances from the object, and the
    angles of the field's bins seen from the object."""
    X, Y = bin_centres(bin_cm)
    cx, cy = X[idx].mean(), Y[idx].mean()
    p = idx[np.nanargmax(rmap[idx])]
    return {"cx": cx, "cy": cy, "d_centroid": float(np.hypot(cx - obj[0], cy - obj[1])),
            "px": X[p], "py": Y[p], "d_peak": float(np.hypot(X[p] - obj[0], Y[p] - obj[1])),
            "angle": float(np.degrees(np.arctan2(cy - obj[1], cx - obj[0])) % 360)}


def orientation_coverage(field_list, obj, bin_cm=2.5, res_deg=1.0):
    """Fraction of 0 to 360 degrees around the object covered by the angular spans of the field bins."""
    X, Y = bin_centres(bin_cm)
    grid = np.zeros(int(360 / res_deg), bool)
    for idx in field_list:
        dx, dy = X[idx] - obj[0], Y[idx] - obj[1]
        d = np.hypot(dx, dy)
        th = np.degrees(np.arctan2(dy, dx)) % 360
        half = np.degrees(np.arctan2(bin_cm / 2 * np.sqrt(2), np.maximum(d, 1e-9)))
        half = np.minimum(half, 180)
        for a, h in zip(th, half):
            lo, hi = a - h, a + h
            ks = np.arange(np.floor(lo / res_deg), np.ceil(hi / res_deg)).astype(int) % len(grid)
            grid[ks] = True
    return grid.mean()


# ----------------------------------------------------------------------------------------------
# Template matching (object-tuning score)

OFFSETS = [5, 10, 15, 20, 30, 40, 50, 60]
WIDTHS = {"a": [5, 10, 25, 50, 75, 100, 150, 200],                         # code: SDs in cm
          "b": list(np.sqrt([5, 10, 25, 50, 75, 100, 150, 200]))}          # Methods: variances


def template_offsets():
    offs = [(0.0, 0.0)]
    for r in OFFSETS:
        for k in range(8):
            offs.append((r * np.cos(k * np.pi / 4), r * np.sin(k * np.pi / 4)))
    return np.array(offs)


def _template_corr(M, cx, cy, sd, V=None, bin_cm=3.0):
    """Pearson correlation of map M (nb, nb; [iy, ix]) with isotropic Gaussian templates of SD `sd`
    centred at (cx, cy) (arrays), evaluated at bin centres; V an optional mask of bins to use."""
    nb = M.shape[0]
    c = (np.arange(nb) + 0.5) * bin_cm
    gx = np.exp(-(c[None, :] - cx[:, None]) ** 2 / (2 * sd ** 2))
    gy = np.exp(-(c[None, :] - cy[:, None]) ** 2 / (2 * sd ** 2))
    if V is None:
        V = np.ones_like(M)
    Mv = np.where(V > 0, M, 0.0)
    n = V.sum()
    sTM = ((gy @ Mv) * gx).sum(1)
    sT = ((gy @ V) * gx).sum(1)
    sT2 = ((gy ** 2 @ V) * gx ** 2).sum(1)
    sM, sM2 = Mv.sum(), (Mv ** 2).sum()
    num = sTM - sT * sM / n
    den = np.sqrt(np.maximum(sT2 - sT ** 2 / n, 0) * max(sM2 - sM ** 2 / n, 0))
    with np.errstate(invalid="ignore", divide="ignore"):
        return np.where(den > 0, num / den, np.nan)


def template_matching(MO, MOM, objO, objOM, widths, rng, n_shuffle=500, VO=None, VOM=None):
    """Object-tuning scores (widths x 65), per-width 99th percentile thresholds of 500 shuffled
    minimum scores, whether the cell is object-tuned, and its single score (largest margin)."""
    offs = template_offsets()
    nb = MO.shape[0]
    scores = np.zeros((len(widths), len(offs)))
    thr = np.zeros(len(widths))
    for w, sd in enumerate(widths):
        cO = _template_corr(MO, objO[0] + offs[:, 0], objO[1] + offs[:, 1], sd, VO)
        cOM = _template_corr(MOM, objOM[0] + offs[:, 0], objOM[1] + offs[:, 1], sd, VOM)
        scores[w] = np.minimum(cO, cOM)
        loc = rng.uniform(0, ARENA, size=(n_shuffle, 2))
        sO = _template_corr(MO, loc[:, 0], loc[:, 1], sd, VO)
        sOM = _template_corr(MOM, loc[:, 0], loc[:, 1], sd, VOM)
        thr[w] = np.nanpercentile(np.minimum(sO, sOM), 99)
    margin = scores - thr[:, None]
    tuned = bool(np.nanmax(margin) > 0) if np.isfinite(margin).any() else False
    k = np.nanargmax(margin) if np.isfinite(margin).any() else 0
    single = scores.ravel()[k]
    return {"scores": scores, "thr": thr, "tuned": tuned, "single": float(single),
            "n_sig": int(np.nansum(margin > 0))}


# ----------------------------------------------------------------------------------------------
# Distance decoder (Bayesian, Poisson)

class Part:
    """Training samples and testing windows of one trial in one iteration."""

    def __init__(self, trial, train_mask, starts, ends):
        self.trial, self.train_mask, self.starts, self.ends = trial, train_mask, starts, ends
        c = (starts + ends) / 2
        t = trial.t
        j = np.clip(np.searchsorted(t, c), 1, len(t) - 1)
        j = np.where(np.abs(c - t[j - 1]) <= np.abs(t[j] - c), j - 1, j)
        self.sample = j
        self.pos = np.c_[trial.x[j], trial.y[j]]

    def counts(self, units=None):
        units = range(self.trial.n_units) if units is None else units
        out = np.zeros((len(self.starts), len(units)), np.float32)
        for k, u in enumerate(units):
            s = self.trial.spikes[u]
            out[:, k] = np.searchsorted(s, self.ends) - np.searchsorted(s, self.starts)
        return out


def half_parts(trial, speed_filter, dt=1.0):
    """The two iterations of the main split: each trial split at the midpoint of its position time
    span; test on the first half and train on the second, then the reverse."""
    tm = (trial.t[0] + trial.t[-1]) / 2
    halves = [(trial.t[0], tm), (tm, trial.t[-1] + trial.dt)]
    out = []
    for test, train in ((0, 1), (1, 0)):
        a, b = halves[test]
        n = int(np.floor((b - a) / dt + 1e-9))
        starts = a + dt * np.arange(n)
        mask = sample_mask(trial, speed_filter, *halves[train])
        out.append(Part(trial, mask, starts, starts + dt))
    return out


def random_parts(trial, speed_filter, rng, dt=1.0):
    """Random partition (claims, figs5f reading a): the trial's 1 s bins permuted, the first half
    training and the rest testing, then the reverse."""
    a = trial.t[0]
    n = int(np.floor((trial.t[-1] + trial.dt - a) / dt + 1e-9))
    perm = rng.permutation(n)
    g = [np.sort(perm[: n // 2]), np.sort(perm[n // 2:])]
    sec = np.floor((trial.t - a) / dt).astype(int)
    out = []
    for test, train in ((0, 1), (1, 0)):
        starts = a + dt * g[test]
        mask = np.isin(sec, g[train])
        if speed_filter:
            mask &= trial.speed > SPEED_MIN
        out.append(Part(trial, mask, starts, starts + dt))
    return out


class Model:
    """Training rate maps and occupancy prior of one trial in one iteration."""

    def __init__(self, part: Part, units, rm, bin_cm=3.0, uniform=False):
        occ, spk = raw_maps(part.trial, part.train_mask, bin_cm, units)
        self.occ = occ
        self.lam = rate_maps(occ, spk, rm=rm, blank=False)            # (U, B), Hz
        self.prior = np.ones_like(occ) if uniform else occ.copy()
        self.bin_cm = bin_cm

    def loglik(self, counts, dt=1.0):
        """Poisson log-likelihood per sample and spatial bin, without the log n! term (S, B)."""
        lam = np.maximum(self.lam, LAMBDA_FLOOR) * dt
        return counts @ np.log(lam).astype(np.float32) - lam.sum(0).astype(np.float32)[None, :]


def equal_sample_edges(d, k=5):
    """Testing samples sorted by distance and split into k equal groups, the remainder to the
    last; edges are 0 and each group's largest distance (equalDistanceEdges.m)."""
    ds = np.sort(d)
    n = len(ds) // k
    edges = [0.0] + [ds[(i + 1) * n - 1] for i in range(k - 1)] + [ds[-1]]
    return np.array(edges)


def assign(values, edges):
    """Group index of each value (0..k-1), -1 when outside; a value on an inner edge goes below."""
    g = np.searchsorted(edges, values, side="left") - 1
    g = np.where(values == edges[0], 0, g)
    g[(values < edges[0]) | (values > edges[-1])] = -1
    return g


def masks_from_edges(dbins, edges):
    """Spatial bins whose centre lies strictly between each pair of edges."""
    return [(dbins > edges[i]) & (dbins < edges[i + 1]) for i in range(len(edges) - 1)]


def _logmarg(C, logl, lsum, prior):
    """log sum over spatial bins of Poisson likelihood x prior (normalised), for count rows C (S, U),
    log rates logl (U, b) and summed rates lsum (b,) of the bins kept, and their prior (b,)."""
    sel = prior > 0
    if not sel.any():
        return np.full(len(C), -np.inf)
    LL = C @ logl[:, sel] - lsum[sel][None, :]
    LL += np.log(prior[sel] / prior[sel].sum()).astype(np.float32)[None, :]
    m = LL.max(1, keepdims=True)
    return (np.log(np.exp(LL - m).sum(1)) + m[:, 0]).astype(float)


def decode_pair(partsA, partsB, mode="distance", obj=None, units=None, rm="b", dt=1.0,
                edges_fixed=None, uniform=False, bin_cm=3.0, angle_start=0.0, sample_filter=None,
                keep_bins=None, return_samples=False, cache=None, chunk=20000):
    """Run the two-trial decoder over both iterations. `partsA`/`partsB` are lists of Parts (one
    per iteration) for trial A (No Object, or the first of the pair) and B.

    mode: "arena" (whole arena, full prior), "distance" (5 equal-sample distance bins per trial and
    iteration), "fixed" (edges_fixed), "angle" (5 sectors of 72 degrees from angle_start).
    units: the units used (default all). keep_bins: optional boolean mask of spatial bins kept
    (sampling analysis). sample_filter: optional function(part, label, ring) -> bool mask of the
    testing samples kept. cache: a dict reused across calls on the same parts (models and counts
    of all units are computed once). Returns per-bin accuracy and counts and, optionally, the
    per-sample decisions."""
    X, Y = bin_centres(bin_cm)
    dbins = np.hypot(X - obj[0], Y - obj[1]) if obj is not None else None
    abins = (np.degrees(np.arctan2(Y - obj[1], X - obj[0])) - angle_start) % 360 if obj is not None else None
    k = {"arena": 1, "distance": 5, "fixed": 5, "angle": 5}[mode]
    correct, total, ties = np.zeros(k), np.zeros(k), np.zeros(k)
    samples = []
    cache = {} if cache is None else cache
    for it, (pA, pB) in enumerate(zip(partsA, partsB)):
        models = []
        for p in (pA, pB):
            key = ("model", id(p), rm, bin_cm, uniform)
            if key not in cache:
                m = Model(p, None, rm, bin_cm, uniform)
                lam = np.maximum(m.lam, LAMBDA_FLOOR)
                cache[key] = (m, np.log(lam).astype(np.float32), lam.astype(np.float32))
            models.append(cache[key])
        tests = [pA, pB]
        rings, masks = [], []
        for p in tests:
            if mode == "arena":
                rings.append(np.zeros(len(p.starts), int))
                masks.append([np.ones(len(X), bool)])
            elif mode in ("distance", "fixed"):
                d = np.hypot(p.pos[:, 0] - obj[0], p.pos[:, 1] - obj[1])
                e = equal_sample_edges(d) if mode == "distance" else np.asarray(edges_fixed, float)
                rings.append(assign(d, e))
                masks.append(masks_from_edges(dbins, e))
            else:
                a = (np.degrees(np.arctan2(p.pos[:, 1] - obj[1], p.pos[:, 0] - obj[0])) - angle_start) % 360
                e = np.arange(0, 361, 72.0)
                rings.append(np.clip(np.floor(a / 72).astype(int), 0, 4))
                masks.append([(abins >= e[i]) & (abins < e[i + 1]) for i in range(5)])
        for label, p in enumerate(tests):
            key = ("counts", id(p), dt)
            if key not in cache:
                cache[key] = p.counts()
            C = cache[key] if units is None else cache[key][:, units]
            keep = rings[label] >= 0
            if sample_filter is not None:
                keep &= sample_filter(p, label, rings[label])
            r_all = rings[label]
            marg = [np.full(len(p.starts), -np.inf), np.full(len(p.starts), -np.inf)]
            for b in range(k):
                rows = np.flatnonzero(keep & (r_all == b))
                if len(rows) == 0:
                    continue
                for mi, (m, logl, lam) in enumerate(models):
                    if units is not None:
                        logl_u, lam_u = logl[units], lam[units]
                    else:
                        logl_u, lam_u = logl, lam
                    cols = masks[mi][b]
                    prior = m.prior * cols
                    if keep_bins is not None:
                        prior = prior * (keep_bins[it] if isinstance(keep_bins, list) else keep_bins)
                    # Poisson mean rate x dt: log(rate dt) = log rate + log dt. Identical count
                    # vectors have identical likelihoods, so each distinct vector is computed once.
                    Cr = C[rows]
                    if dt < 0.5:
                        ci = np.ascontiguousarray(Cr.astype(np.int16))
                        _, first, inv = np.unique(ci.view(np.dtype((np.void, ci.dtype.itemsize * ci.shape[1]))).ravel(),
                                                  return_index=True, return_inverse=True)
                        uniq = Cr[first]
                    else:
                        uniq, inv = Cr, np.arange(len(rows))
                    vals = np.empty(len(uniq))
                    for c0 in range(0, len(uniq), chunk):
                        vals[c0:c0 + chunk] = _logmarg(uniq[c0:c0 + chunk], logl_u + np.float32(np.log(dt)),
                                                       (lam_u * dt).sum(0), prior)
                    marg[mi][rows] = vals[np.ravel(inv)]
            idx = np.flatnonzero(keep)
            lA, lB = marg[0][idx], marg[1][idx]
            r = r_all[idx]
            dec = np.where(lA > lB, 0, np.where(lB > lA, 1, -1))
            ok = dec >= 0
            np.add.at(total, r[ok], 1)
            np.add.at(correct, r[ok], (dec[ok] == label))
            np.add.at(ties, r[~ok], 1)
            if return_samples:
                samples.append({"iteration": it, "label": label, "ring": r, "decision": dec,
                                "lA": lA, "lB": lB, "pos": p.pos[idx], "index": idx})
    with np.errstate(invalid="ignore"):
        acc = correct / total
    res = {"acc": acc, "n": total, "ties": ties}
    if return_samples:
        res["samples"] = samples
    return res


def shuffled_accuracy(samples, rng, k=5, n_shuffle=50):
    """Accuracy with the trial labels of the testing samples shuffled within each iteration and
    distance bin (Methods, Shuffling trial labels); decisions are those of the trained decoder.
    Returns (n_shuffle, k) accuracies."""
    out = np.zeros((n_shuffle, k))
    by = {}
    for s in samples:
        for b in range(k):
            m = (s["ring"] == b) & (s["decision"] >= 0)
            by.setdefault((s["iteration"], b), []).append((np.full(m.sum(), s["label"]), s["decision"][m]))
    for i in range(n_shuffle):
        corr = np.zeros(k)
        tot = np.zeros(k)
        for (it, b), lst in by.items():
            lab = np.concatenate([l for l, _ in lst])
            dec = np.concatenate([d for _, d in lst])
            lab = lab[rng.permutation(len(lab))]
            corr[b] += np.sum(lab == dec)
            tot[b] += len(lab)
        out[i] = corr / tot
    return out


def slope(acc):
    """Least-squares slope of accuracy on distance-bin index 1..5 (Methods, Measuring strength)."""
    x = np.arange(1, len(acc) + 1)
    ok = np.isfinite(acc)
    if ok.sum() < 2:
        return np.nan
    return float(np.polyfit(x[ok], acc[ok], 1)[0])


# ----------------------------------------------------------------------------------------------
# Single-cell distance decoder, vectorised over circularly shifted spike trains

def shift_spikes(trial: Trial, u: int, shift: float):
    """Spike times of unit u circularly shifted within the trial's time span."""
    s = trial.spikes[u]
    lo = min(trial.t[0], s.min()) if len(s) else trial.t[0]
    T = max(trial.t[-1] + trial.dt, s.max() + 1e-6 if len(s) else 0) - lo
    return np.sort((s - lo + shift) % T + lo)


class PairContext:
    """What the single-cell distance decoder shares across the cells of a session: the parts of
    both trials, the distance bins of each part, the spatial-bin masks and the occupancy maps."""

    def __init__(self, trA, trB, speed_filter, bin_cm=3.0):
        self.trials = (trA, trB)
        obj = trB.obj
        X, Y = bin_centres(bin_cm)
        dbins = np.hypot(X - obj[0], Y - obj[1])
        self.B = nbins(bin_cm) ** 2
        self.bidx = [bin_index(t.x, t.y, bin_cm) for t in self.trials]
        self.parts = [half_parts(trA, speed_filter), half_parts(trB, speed_filter)]   # [trial][iteration]
        self.rings, self.masks, self.occ = {}, {}, {}
        for ti in range(2):
            for it in range(2):
                p = self.parts[ti][it]
                d = np.hypot(p.pos[:, 0] - obj[0], p.pos[:, 1] - obj[1])
                e = equal_sample_edges(d)
                self.rings[ti, it] = assign(d, e)
                self.masks[ti, it] = masks_from_edges(dbins, e)
                self.occ[ti, it] = np.bincount(self.bidx[ti][p.train_mask], weights=self.trials[ti].sdt[p.train_mask],
                                                minlength=self.B)


def single_cell_tuning(ctx: PairContext, u_pair, rm, shifts=((0.0, 0.0),)):
    """Distance-decoder accuracy per distance bin for one cell (unit u_pair[i] of trial i), for each
    pair of circular shifts of its spike trains (shifts (n, 2), in s). Returns (n, 5) accuracies."""
    shifts = np.atleast_2d(np.asarray(shifts, float))
    nS = len(shifts)
    B = ctx.B
    correct = np.zeros((nS, 5))
    total = np.zeros((nS, 5))
    # all shifted trains of each trial at once: spike times, variant index, nearest sample
    trains = []
    for ti, (tr, u) in enumerate(zip(ctx.trials, u_pair)):
        s = tr.spikes[u]
        lo = min(tr.t[0], s.min()) if len(s) else tr.t[0]
        T = max(tr.t[-1] + tr.dt, s.max() + 1e-6 if len(s) else 0) - lo
        allt = ((s[None, :] - lo + shifts[:, ti][:, None]) % T + lo).ravel()
        var = np.repeat(np.arange(nS), len(s))
        j = tr._sample_index(allt)
        trains.append((allt, var, j))
    for it in range(2):
        marg = []
        for mi in range(2):
            p = ctx.parts[mi][it]
            allt, var, j = trains[mi]
            ok = j >= 0
            ok[ok] = p.train_mask[j[ok]]
            spk = np.bincount(var[ok] * B + ctx.bidx[mi][j[ok]], minlength=nS * B).reshape(nS, B).astype(float)
            lam = np.maximum(rate_maps(ctx.occ[mi, it], spk, rm=rm, blank=False), LAMBDA_FLOOR)
            marg.append((lam, ctx.occ[mi, it], ctx.masks[mi, it]))
        cnts = []
        for ti in range(2):
            p = ctx.parts[ti][it]
            allt, var, _ = trains[ti]
            n = len(p.starts)
            k = np.floor((allt - p.starts[0]) / (p.ends[0] - p.starts[0])).astype(int)
            ok = (k >= 0) & (k < n)
            cnts.append(np.bincount(var[ok] * n + k[ok], minlength=nS * n).reshape(nS, n))
        nmax = max(int(c.max()) for c in cnts)
        nn = np.arange(nmax + 1, dtype=np.float32)
        tabs = []
        for lam, occ, masks in marg:
            out = np.full((nS, nmax + 1, 5), -np.inf, np.float32)
            loglam = np.log(lam).astype(np.float32)
            lam32 = lam.astype(np.float32)
            for b, m in enumerate(masks):
                pr = occ * m
                if pr.sum() <= 0:
                    continue
                sel = pr > 0
                lp = np.log(pr[sel] / pr.sum()).astype(np.float32)
                LL = nn[None, :, None] * loglam[:, None, sel] - lam32[:, None, sel] + lp
                mx = LL.max(2, keepdims=True)
                out[:, :, b] = np.log(np.exp(LL - mx).sum(2)) + mx[:, :, 0]
            tabs.append(out)
        for label in range(2):
            r = ctx.rings[label, it]
            ok = r >= 0
            c = cnts[label][:, ok]
            rr = r[ok]
            iS = np.arange(nS)[:, None]
            lA = tabs[0][iS, c, rr[None, :]]
            lB = tabs[1][iS, c, rr[None, :]]
            dec = np.where(lA > lB, 0, np.where(lB > lA, 1, -1))
            valid = dec >= 0
            for b in range(5):
                sel = (rr == b)[None, :] & valid
                total[:, b] += sel.sum(1)
                correct[:, b] += (sel & (dec == label)).sum(1)
    with np.errstate(invalid="ignore"):
        return correct / total


# ----------------------------------------------------------------------------------------------
# Population vector correlation

def pv_correlation(mA, mB):
    """Pearson correlation across cells at each spatial bin between two stacks of rate maps (U, B)."""
    a = mA - mA.mean(0)
    b = mB - mB.mean(0)
    num = (a * b).sum(0)
    den = np.sqrt((a ** 2).sum(0) * (b ** 2).sum(0))
    with np.errstate(invalid="ignore", divide="ignore"):
        return np.where(den > 0, num / den, np.nan)


# ----------------------------------------------------------------------------------------------
# Words and counts

def binned_counts(trial: Trial, units, dt=0.01):
    """Spike counts of the units in consecutive bins of dt over the trial's tracking span, the
    distance from a point of each bin (nearest tracking sample), returned as (T, U) and bin centres."""
    a, b = trial.t[0], trial.t[-1] + trial.dt
    n = int(np.floor((b - a) / dt))
    edges = a + dt * np.arange(n + 1)
    M = np.zeros((n, len(units)), np.int16)
    for k, u in enumerate(units):
        s = trial.spikes[u]
        M[:, k] = np.diff(np.searchsorted(s, edges))
    centres = (edges[:-1] + edges[1:]) / 2
    j = np.clip(np.searchsorted(trial.t, centres), 1, len(trial.t) - 1)
    j = np.where(np.abs(centres - trial.t[j - 1]) <= np.abs(trial.t[j] - centres), j - 1, j)
    pos = np.c_[trial.x[j], trial.y[j]]
    return M, pos


def word_ids(MA, MB):
    """Integer ids for the rows (words) of two count matrices, over both together; id of the all-zero word."""
    allm = np.vstack([MA, MB])
    u, inv = np.unique(allm, axis=0, return_inverse=True)
    inv = inv.ravel()
    zero = np.flatnonzero(~u.any(1))
    return inv[: len(MA)], inv[len(MA):], (int(zero[0]) if len(zero) else -1)


def mutual_information(sym, lab):
    """MI (bits) between symbols and a binary label, from frequency distributions."""
    if len(sym) == 0:
        return np.nan
    _, s = np.unique(sym, return_inverse=True)
    joint = np.zeros((s.max() + 1, 2))
    np.add.at(joint, (s, lab), 1)
    P = joint / joint.sum()
    ps = P.sum(1, keepdims=True)
    pl = P.sum(0, keepdims=True)
    with np.errstate(divide="ignore", invalid="ignore"):
        t = np.where(P > 0, P * np.log2(P / (ps * pl)), 0.0)
    return float(t.sum())


def mi_bias_corrected(sym, lab, rng, n_shuffle=50):
    mi = mutual_information(sym, lab)
    sh = [mutual_information(sym, lab[rng.permutation(len(lab))]) for _ in range(n_shuffle)]
    return mi - float(np.mean(sh)), mi


def entropy(sym):
    if len(sym) == 0:
        return np.nan
    _, c = np.unique(sym, return_counts=True)
    p = c / c.sum()
    return float(-(p * np.log2(p)).sum())


# ----------------------------------------------------------------------------------------------
# Behaviour

def lowess_smooth(y, span):
    """Local linear regression with tricube weights over `span` samples (as MATLAB smooth 'lowess',
    without robustness iterations)."""
    h = max(int(span) // 2, 1)
    k = np.arange(-h, h + 1)
    w = (1 - (np.abs(k) / (h + 1)) ** 3) ** 3
    valid = np.isfinite(y).astype(float)
    yv = np.nan_to_num(y)
    conv = lambda a, kern: np.convolve(a, kern[::-1], mode="same")
    S0 = conv(valid, w)
    S1 = conv(valid, w * k)
    S2 = conv(valid, w * k ** 2)
    T0 = conv(yv, w)
    T1 = conv(yv, w * k)
    den = S0 * S2 - S1 ** 2
    with np.errstate(invalid="ignore", divide="ignore"):
        out = np.where(np.abs(den) > 1e-12, (S2 * T0 - S1 * T1) / den, T0 / np.maximum(S0, 1e-12))
    return out


def resample_25hz(trial: Trial, hz=25.0):
    """Tracking on a 25 Hz grid (linear interpolation; grid points more than 0.2 s from a valid
    sample are dropped). Tetrode tracking is already at 25 Hz and is returned as it is."""
    if abs(trial.dt - 1 / hz) < 1e-3:
        return trial.t, trial.x, trial.y
    g = np.arange(trial.t[0], trial.t[-1], 1 / hz)
    j = np.clip(np.searchsorted(trial.t, g), 1, len(trial.t) - 1)
    near = np.minimum(np.abs(g - trial.t[j - 1]), np.abs(trial.t[j] - g))
    keep = near <= MAX_INTERP_GAP
    return g[keep], np.interp(g[keep], trial.t, trial.x), np.interp(g[keep], trial.t, trial.y)


def behaviour_speed(t, x, y, span_s=0.5, hz=25.0):
    """Speed (cm/s): position change over consecutive samples divided by the time step, each
    component Lowess-smoothed (span 0.5 s, the claims file's standard choice), then the norm."""
    vx = np.gradient(x, t)
    vy = np.gradient(y, t)
    span = int(round(span_s * hz))
    return np.hypot(lowess_smooth(vx, span), lowess_smooth(vy, span))


def gamma_fit(groups, s, minlength):
    """Maximum-likelihood gamma shape and scale per group (Minka's start and Newton steps).
    Groups with fewer than 2 samples or no spread get NaN."""
    n = np.bincount(groups, minlength=minlength).astype(float)
    S = np.bincount(groups, weights=s, minlength=minlength)
    L = np.bincount(groups, weights=np.log(s), minlength=minlength)
    with np.errstate(invalid="ignore", divide="ignore"):
        m = S / n
        q = np.log(m) - L / n
        a = (3 - q + np.sqrt((q - 3) ** 2 + 24 * q)) / (12 * q)
        for _ in range(5):
            a = a - (np.log(a) - digamma(a) - q) / (1 / a - polygamma(1, a))
        b = m / a
    bad = (n < 2) | ~np.isfinite(a) | (q <= 1e-12)
    a[bad] = np.nan
    b[bad] = np.nan
    return a, b


# ----------------------------------------------------------------------------------------------
# Statistics

def kruskal(groups):
    g = [np.asarray(x)[np.isfinite(x)] for x in groups]
    if any(len(x) == 0 for x in g):
        return np.nan, np.nan
    h, p = stats.kruskal(*g)
    return float(h), float(p)


def signrank(a, b):
    a, b = np.asarray(a, float), np.asarray(b, float)
    ok = np.isfinite(a) & np.isfinite(b)
    if ok.sum() < 2 or np.all(a[ok] == b[ok]):
        return np.nan, np.nan
    r = stats.wilcoxon(a[ok], b[ok])
    return float(r.statistic), float(r.pvalue)


def ranksum(a, b):
    a = np.asarray(a, float)
    b = np.asarray(b, float)
    a, b = a[np.isfinite(a)], b[np.isfinite(b)]
    r = stats.ranksums(a, b)
    return float(r.statistic), float(r.pvalue)


# ----------------------------------------------------------------------------------------------
# Within-trial and between-trial distributions in 1 s sections (Methods, Spatial correlation and
# rate overlap)

class SecMaps:
    """Time and spike maps per 1 s section of a trial, for building maps of random groups of
    sections. Speed-filtered maps (Methods); rates for rate overlap both speed-filtered (reading a)
    and over all of the sections (reading b)."""

    def __init__(self, trial: Trial, units, bin_cm=2.5):
        a = trial.t[0]
        self.n = n = int(np.floor(trial.t[-1] + trial.dt - a))
        B = nbins(bin_cm) ** 2
        self.B = B
        sec = np.floor(trial.t - a).astype(int)
        valid = sec < n
        fast = valid & (trial.speed > SPEED_MIN)
        bidx = bin_index(trial.x, trial.y, bin_cm)
        self.A = sparse.csr_matrix((trial.sdt[fast], (sec[fast], bidx[fast])), shape=(n, B))
        self.t_fast = np.bincount(sec[fast], weights=trial.sdt[fast], minlength=n)
        self.t_all = np.bincount(sec[valid], weights=trial.sdt[valid], minlength=n)
        self.units = list(units)
        C, self.s_fast, self.s_all = [], [], []
        for u in self.units:
            si = trial.spike_si[u]
            ok = si >= 0
            j = si[ok]
            keep = fast[j]
            C.append(sparse.csr_matrix((np.ones(keep.sum()), (sec[j[keep]], bidx[j[keep]])), shape=(n, B)))
            self.s_fast.append(np.bincount(sec[j[keep]], minlength=n))
            ss = np.floor(trial.spikes[u] - a).astype(int)
            ss = ss[(ss >= 0) & (ss < n)]
            self.s_all.append(np.bincount(ss, minlength=n))
        self.C = C
        self.s_fast = np.array(self.s_fast, float)
        self.s_all = np.array(self.s_all, float)

    def prepare(self, W, rm):
        """Cache what the groups in W (R, n) share across units: their time maps."""
        if rm != "b":
            raise ValueError(rm)
        occ = np.asarray((self.A.T @ W.T).T, np.float32)
        nb = int(round(np.sqrt(self.B)))
        O = occ.reshape(-1, nb, nb)
        return {"W": W, "O": O, "visited": O > 0, "K": _kernel(nb),
                "t_fast": W @ self.t_fast, "t_all": W @ self.t_all}

    def groups(self, prep, k):
        """Blanked rate maps (R, B) of unit k for the prepared groups, and the two mean rates (R,)."""
        W, O, visited, K = prep["W"], prep["O"], prep["visited"], prep["K"]
        spk = np.asarray((self.C[k].T @ W.T).T, np.float32).reshape(O.shape)
        with np.errstate(invalid="ignore", divide="ignore"):
            raw = np.where(visited, spk / np.where(visited, O, 1.0), 0.0).astype(np.float32)
        num = K @ raw @ K.T
        with np.errstate(invalid="ignore", divide="ignore"):
            r = np.where(visited, num, np.nan)
            r_fast = (W @ self.s_fast[k]) / prep["t_fast"]
            r_all = (W @ self.s_all[k]) / prep["t_all"]
        return r.reshape(len(W), -1), r_fast, r_all


_KERNELS = {}


def _kernel(nb, sigma=2.0, mode="reflect"):
    """Gaussian smoothing as a matrix (edges mirrored, truncated at 4 SD, as _gauss; or circular,
    mode "wrap"): K @ M @ K.T."""
    if (nb, sigma, mode) not in _KERNELS:
        _KERNELS[(nb, sigma, mode)] = ndimage.gaussian_filter1d(np.eye(nb), sigma, axis=0, mode=mode,
                                                               truncate=4.0).astype(np.float32)
    return _KERNELS[(nb, sigma, mode)]


def rate_maps_batch(occ, spk, rm, sigma=2.0):
    """Blanked rate maps for R pairs of time (R, B) and spike (R, B) maps (method of rate_maps)."""
    if rm != "b":
        raise ValueError(rm)
    R, B = occ.shape
    nb = int(round(np.sqrt(B)))
    raw, visited = _raw_rate(occ.reshape(R, nb, nb), spk.reshape(R, nb, nb))
    r = np.where(visited, _gauss(raw, sigma), np.nan)
    return r.reshape(R, B)


def pearson_rows(a, b):
    """Pearson correlation per row over the entries finite in both."""
    ok = np.isfinite(a) & np.isfinite(b)
    n = ok.sum(1).astype(np.float64)
    a0 = np.where(ok, a, 0).astype(np.float32)
    b0 = np.where(ok, b, 0).astype(np.float32)
    sa, sb = a0.sum(1, dtype=np.float64), b0.sum(1, dtype=np.float64)
    saa = np.einsum("ij,ij->i", a0, a0, dtype=np.float64)
    sbb = np.einsum("ij,ij->i", b0, b0, dtype=np.float64)
    sab = np.einsum("ij,ij->i", a0, b0, dtype=np.float64)
    with np.errstate(invalid="ignore", divide="ignore"):
        r = (n * sab - sa * sb) / np.sqrt((n * saa - sa ** 2) * (n * sbb - sb ** 2))
    r[n < 3] = np.nan
    return r


def random_halves(n, R, rng):
    """R random assignments of n sections to two groups of n/2 (two 0/1 matrices (R, n))."""
    W1 = np.zeros((R, n))
    W2 = np.zeros((R, n))
    for i in range(R):
        p = rng.permutation(n)
        W1[i, p[: n // 2]] = 1
        W2[i, p[n // 2: 2 * (n // 2)]] = 1
    return W1, W2


def change_test(within, between):
    """A cell changes on a measure when the mean of the between-trial values is below the 1st
    percentile of the within-trial values and a signed-rank test of the two (paired by repetition)
    gives p < 0.05."""
    w, b = np.asarray(within, float), np.asarray(between, float)
    ok = np.isfinite(w) & np.isfinite(b)
    if ok.sum() < 10:
        return False, np.nan
    _, p = signrank(w[ok], b[ok])
    return bool(np.mean(b[ok]) < np.percentile(w[ok], 1) and p < 0.05), p


# ----------------------------------------------------------------------------------------------
# Object traces (Methods, Region-of-interest analysis for object traces)

def roi_offsets(idx, reading, bin_cm=2.5):
    """A circular ROI for a field, as bin offsets from the bin holding the field's centroid.
    Reading a: a circle of the field's area centred on its centroid; b: the smallest circle
    centred on the centroid that holds every bin centre of the field."""
    nb = nbins(bin_cm)
    X, Y = bin_centres(bin_cm)
    cx, cy = X[idx].mean(), Y[idx].mean()
    if reading == "a":
        rad = np.sqrt(len(idx) * bin_cm ** 2 / np.pi)
    else:
        rad = np.hypot(X[idx] - cx, Y[idx] - cy).max()
    inside = np.hypot(X - cx, Y - cy) <= rad
    iy, ix = np.divmod(np.flatnonzero(inside), nb)
    return iy, ix


def roi_rate_overlap(mapA, mapB, iy, ix, nb, shift=(0, 0), wrap=True):
    """Rate overlap between the mean rate of ROI bins (iy, ix) in mapA and the same ROI shifted by
    `shift` bins in mapB (wrapped around the map)."""
    A = mapA.reshape(nb, nb)
    Bm = mapB.reshape(nb, nb)
    ra = np.nanmean(A[iy, ix])
    jy, jx = (iy + shift[0]) % nb, (ix + shift[1]) % nb
    rb = np.nanmean(Bm[jy, jx])
    return rate_overlap(ra, rb)


# ----------------------------------------------------------------------------------------------
# Per-cell tables used by several claims

def seed_for(*parts) -> int:
    """A fixed seed from a text key, so each claim's random draws do not depend on cell order
    elsewhere in a notebook."""
    import zlib
    return zlib.crc32("|".join(str(p) for p in parts).encode())


def template_maps(trial: Trial, rm, units=None):
    """Template-matching maps: 3 cm bins, speed-filtered, smoothed, not blanked; (U, 50, 50)."""
    occ, spk = raw_maps(trial, sample_mask(trial, True), 3.0, units)
    return rate_maps(occ, spk, rm=rm, blank=False).reshape(-1, 50, 50)


def single_maps(trial: Trial, rm, units=None, mask=None):
    """Single-cell rate maps: 2.5 cm bins, speed-filtered, smoothed, blanked; (U, 3600), and time."""
    m = sample_mask(trial, True) if mask is None else mask
    occ, spk = raw_maps(trial, m, 2.5, units)
    return rate_maps(occ, spk, rm=rm, blank=True), occ


def object_tuning(sessions, rm, widths, trials=("O", "OM"), objs=None, key="", masks_OM=None,
                  zero_OM=None, only=None):
    """Template matching for every cell of the sessions. objs: fixed object positions for the two
    trials (control sessions), else the trials' own. masks_OM / zero_OM: optional dict
    (session index, unit) -> boolean 50 x 50 array of OM bins left out of the correlations or set
    to zero (trace removal). only: optional set of (session index, unit) to run. Returns one dict
    per cell."""
    rng = np.random.default_rng(seed_for("object-tuning", key, rm, widths[0], *trials))
    out = []
    for si, s in enumerate(sessions):
        tO, tM = s.trial(trials[0]), s.trial(trials[1])
        if tO is None or tM is None:
            continue
        oO, oM = (objs if objs is not None else (tO.obj, tM.obj))
        MO, MM = template_maps(tO, rm), template_maps(tM, rm)
        for u in range(s.n_units):
            if only is not None and (si, u) not in only:
                continue
            mm, V = MM[u], None
            if zero_OM is not None and (si, u) in zero_OM:
                mm = np.where(zero_OM[si, u], 0.0, mm)
            if masks_OM is not None and (si, u) in masks_OM:
                V = (~masks_OM[si, u]).astype(float)
            r = template_matching(MO[u], mm, oO, oM, widths, rng, VOM=V)
            out.append({"session": si, "unit": u, "rat": s.rat, "technique": s.technique,
                        "tuned": r["tuned"], "single": r["single"], "n_sig": r["n_sig"],
                        "max_margin": float(np.nanmax(r["scores"] - r["thr"][:, None]))})
    return out


# ----------------------------------------------------------------------------------------------
# Object-vector score (claims file, ovs-method-extra-cells: Methods, Object-vector score, and the
# bins and smoothing of the paper's reference 12, Andersson et al. 2021)

OV_DIST_BIN = 2.0        # cm, reference 12
OV_ANGLE_BIN = 10.0      # degrees, reference 12, 0 = East
OV_SIGMA = 1.5           # bins, circular 2D Gaussian, reference 12


def shift_values(trial: Trial, n, rng):
    """Circular shifts (s) between 20 s and the trial's duration less 20 s (Methods, Shuffling of
    spike data)."""
    return rng.uniform(20.0, trial.duration - 20.0, n)


def shifted_samples(trial: Trial, u, shifts):
    """The sample index (as Trial._sample_index) of unit u's spikes, each spike train circularly
    shifted within the trial by each of `shifts`. Returns the shift number and sample index of the
    spikes that have a position."""
    s = trial.spikes[u]
    T = trial.t1 - trial.t0
    allt = ((s[None, :] - trial.t0 + np.asarray(shifts, float)[:, None]) % T + trial.t0).ravel()
    k = np.repeat(np.arange(len(shifts)), len(s))
    j = trial._sample_index(allt)
    ok = j >= 0
    return k[ok], j[ok]


def spatial_information_shuffled(trial: Trial, u, shifts):
    """Spatial information (bits per spike) of unit u in the 2.5 cm, speed-filtered, blanked map
    for each shift (a shift of 0 is the cell itself), under the lambda readings si-a and si-b of
    spatial_information. Returns two arrays (len(shifts),)."""
    m = sample_mask(trial, True)
    bidx = bin_index(trial.x, trial.y, 2.5)
    B = nbins(2.5) ** 2
    occ = np.bincount(bidx[m], weights=trial.sdt[m], minlength=B)
    k, j = shifted_samples(trial, u, shifts)
    keep = m[j]
    R = len(shifts)
    nb = nbins(2.5)
    spk = np.bincount(k[keep] * B + bidx[j[keep]], minlength=R * B).reshape(R, nb, nb).astype(np.float32)
    raw, visited = _raw_rate(occ.reshape(nb, nb), spk)
    K = _kernel(nb)
    l = np.where(visited.ravel()[None], (K @ raw.astype(np.float32) @ K.T).reshape(R, B), 0.0).astype(float)
    out = []
    for P, rate in ((occ / occ.sum(), spk.sum((1, 2)) / occ.sum()), (occ / trial.duration, None)):
        if rate is None:
            rate = (P[None] * l).sum(1)
        with np.errstate(divide="ignore", invalid="ignore"):
            terms = np.where(l > 0, P[None] * l * np.log2(l / rate[:, None]), 0.0)
            out.append(np.where(rate > 0, terms.sum(1) / rate, np.nan))
    return out


def max_object_distance(trial: Trial, obj):
    """Largest distance from the object sampled in the speed-filtered epochs."""
    m = sample_mask(trial, True)
    return float(np.hypot(trial.x[m] - obj[0], trial.y[m] - obj[1]).max())


def vector_maps(trial: Trial, u, shifts, obj, dmax):
    """Vector maps of unit u (rate as a function of distance and direction from the object) for
    each shift: speed-filtered samples up to dmax, distance bins of 2 cm from 0, direction bins of
    10 degrees from East, the rate per bin (unvisited bins 0) smoothed with a Gaussian of SD 1.5
    bins, circular in direction and with mirrored edges in distance (the rate-map method of the
    opening comment), unvisited bins blanked. Returns (len(shifts), nd * 36)."""
    m = sample_mask(trial, True)
    dx, dy = trial.x - obj[0], trial.y - obj[1]
    d = np.hypot(dx, dy)
    a = np.degrees(np.arctan2(dy, dx)) % 360
    nd = int(np.ceil(dmax / OV_DIST_BIN))
    na = int(round(360 / OV_ANGLE_BIN))
    m &= d <= dmax
    vb = np.minimum((d // OV_DIST_BIN).astype(int), nd - 1) * na + (a // OV_ANGLE_BIN).astype(int) % na
    B = nd * na
    occ = np.bincount(vb[m], weights=trial.sdt[m], minlength=B)
    k, j = shifted_samples(trial, u, shifts)
    keep = m[j]
    R = len(shifts)
    spk = np.bincount(k[keep] * B + vb[j[keep]], minlength=R * B).reshape(R, nd, na).astype(float)
    O = occ.reshape(nd, na)
    visited = O > 0
    with np.errstate(divide="ignore", invalid="ignore"):
        raw = np.where(visited[None], spk / np.where(visited, O, 1.0)[None], 0.0)
    sm = _kernel(nd, OV_SIGMA) @ raw.astype(np.float32) @ _kernel(na, OV_SIGMA, "wrap").T
    return np.where(visited[None], sm, np.nan).reshape(R, B)


def roi_rate_overlap_shuffled(mapA, mapB, iy, ix, nb, shifts):
    """roi_rate_overlap for many shifts (n, 2) at once."""
    A = mapA.reshape(nb, nb)
    Bm = mapB.reshape(nb, nb)
    ra = np.nanmean(A[iy, ix])
    jy = (iy[None, :] + shifts[:, :1]) % nb
    jx = (ix[None, :] + shifts[:, 1:]) % nb
    rb = np.nanmean(Bm[jy, jx], axis=1)
    lo, hi = np.minimum(ra, rb), np.maximum(ra, rb)
    with np.errstate(invalid="ignore", divide="ignore"):
        return np.where(hi > 0, lo / hi, np.nan)


# ----------------------------------------------------------------------------------------------
# Position decoding (Supplementary Figure 5J) and behaviour decoders (Behavioral analyses I)

def position_errors(parts, rm, bin_cm=3.0):
    """Decode position within one trial: train on one half, posterior over all spatial bins of the
    other half's 1 s samples (Poisson likelihood x occupancy prior). Returns the testing positions
    and the errors (cm) of the maximum-posterior bin and of the posterior mean."""
    X, Y = bin_centres(bin_cm)
    pos, e_map, e_mean = [], [], []
    for it in range(2):
        p = parts[it]          # tests on half `it`, trains on the other
        m = Model(p, None, rm, bin_cm)
        lam = np.maximum(m.lam, LAMBDA_FLOOR)
        C = p.counts()
        sel = m.prior > 0
        LL = C @ np.log(lam[:, sel]).astype(np.float32) - lam[:, sel].sum(0)[None, :]
        LL = LL + np.log(m.prior[sel] / m.prior[sel].sum())[None, :]
        LL -= LL.max(1, keepdims=True)
        P = np.exp(LL)
        P /= P.sum(1, keepdims=True)
        xs, ys = X[sel], Y[sel]
        k = P.argmax(1)
        mx, my = P @ xs, P @ ys
        pos.append(p.pos)
        e_map.append(np.hypot(xs[k] - p.pos[:, 0], ys[k] - p.pos[:, 1]))
        e_mean.append(np.hypot(mx - p.pos[:, 0], my - p.pos[:, 1]))
    return np.vstack(pos), np.concatenate(e_map), np.concatenate(e_mean)


class Behaviour:
    """25 Hz tracking of a trial with Lowess-smoothed speed, split at the same midpoint as the
    decoder's halves."""

    def __init__(self, trial: Trial):
        self.t, self.x, self.y = resample_25hz(trial)
        self.speed = behaviour_speed(self.t, self.x, self.y)
        tm = (trial.t[0] + trial.t[-1]) / 2
        self.half = (self.t >= tm).astype(int)          # 0 first half, 1 second half
        self.dt = 1 / 25.0


def behaviour_decoder(bA: Behaviour, bB: Behaviour, edges, obj, kind, bin_cm=3.0):
    """Speed or occupancy decoder (Methods, Behavioral analyses I). edges[(trial, iteration)]: the
    distance-bin edges of the neural decoder's testing samples. Iteration it tests on half it and
    trains on the other. Returns per-bin accuracy (5,)."""
    X, Y = bin_centres(bin_cm)
    dbins = np.hypot(X - obj[0], Y - obj[1])
    B = len(X)
    correct, total = np.zeros(5), np.zeros(5)
    beh = (bA, bB)
    for it in range(2):
        models = []
        for mi, b in enumerate(beh):
            tr = b.half != it
            bidx = bin_index(b.x[tr], b.y[tr], bin_cm)
            occ = np.bincount(bidx, minlength=B) * b.dt
            masks = masks_from_edges(dbins, edges[mi, it])
            if kind == "speed":
                s = np.maximum(b.speed[tr], 1e-6)
                a_, sc_ = gamma_fit(bidx, s, B)
                models.append((occ, masks, a_, sc_))
            else:
                models.append((occ, masks, None, None))
        for label, b in enumerate(beh):
            te = b.half == it
            d = np.hypot(b.x[te] - obj[0], b.y[te] - obj[1])
            ring = assign(d, edges[label, it])
            bidx = bin_index(b.x[te], b.y[te], bin_cm)
            s = np.maximum(b.speed[te], 1e-6)
            L = np.full((2, te.sum()), -np.inf)
            for mi, (occ, masks, a_, sc_) in enumerate(models):
                for r in range(5):
                    rows = np.flatnonzero(ring == r)
                    if len(rows) == 0:
                        continue
                    m = masks[r]
                    if kind == "speed":
                        m = m & np.isfinite(a_) & (occ > 0)
                    pr = occ * m
                    if pr.sum() <= 0:
                        continue
                    sel = pr > 0
                    lp = np.log(pr[sel] / pr.sum())
                    if kind == "speed":
                        aa, bb = a_[sel], sc_[sel]
                        ls = np.log(s[rows])
                        logpdf = (aa - 1)[None, :] * ls[:, None] - s[rows][:, None] / bb[None, :] \
                            - (aa * np.log(bb) + gammaln(aa))[None, :]
                        L[mi, rows] = logsumexp(logpdf + lp[None, :], axis=1)
                    else:
                        full = np.full(B, -np.inf)
                        full[sel] = lp
                        L[mi, rows] = full[bidx[rows]]
            ok = ring >= 0
            dec = np.where(L[0] > L[1], 0, np.where(L[1] > L[0], 1, -1))
            v = ok & (dec >= 0)
            np.add.at(total, ring[v], 1)
            np.add.at(correct, ring[v], dec[v] == label)
    with np.errstate(invalid="ignore"):
        return correct / total


def decoding_sessions(pop_sessions, ca1_sessions):
    """The 16 decoding sessions of the population files. In the two Neuropixels population files
    the tracking y equals x in every sample (checked in notebook 01); the same recordings in the
    CA1 single-cell file have the same timestamps, x and spike trains, and a y of their own. For
    those sessions the No Object and Object trials are taken from the CA1 file, with the units in
    the population file's order. Returns the sessions and the keys of the replaced ones."""
    out, replaced = [], []
    for p in pop_sessions:
        if not all(np.array_equal(t.x, t.y) for t in p.trials):
            out.append(p)
            continue
        s, m = link_population(p, ca1_sessions)
        if s is None or len(m) != p.n_units:
            raise ValueError(f"cannot replace the tracking of {p.key}")
        order = [m[u] for u in range(p.n_units)]
        out.append(Session(p.file, p.index, p.rat, p.technique,
                           [s.trial("NO").subset(order), s.trial("O").subset(order)]))
        replaced.append(p.key)
    return out, replaced
