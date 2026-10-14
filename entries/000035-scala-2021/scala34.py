"""Data access and electrophysiological features for dandiset 000035 (Scala, Kobak et al. 2021).

Dandiset 000035 holds the paper's follow-up Patch-seq recordings at physiological temperature
(34 degrees C): one NWB file per neuron, each with a ladder of 600 ms current steps and, in
`general/DandiIcephysMetadata`, the neuron's transcriptomic type, layer and soma depth.

`load_cohort` streams every file from the DANDI Archive in parallel and reduces it, as it loads,
to one row per neuron: the metadata, checks of the stimulus and of the timing, and the 17
electrophysiological features the paper uses for its statistics.

Where parameters come from:

- Stimulus window 0.1 to 0.7 s, 25 kHz sampling: read from the files and checked in `load_cell`.
- Spike detection follows the Allen SDK code the paper adapted (berenslab/mini-atlas,
  code/ephys_features.py): 4-pole Bessel low-pass filter at 10 kHz before differentiation,
  upward crossing of dV/dt = 20 V/s, peak at least -30 mV and at least 2 mV above the crossing,
  threshold refined to 5% of the mean maximal upstroke slope. Those are the code's defaults.
- Feature definitions follow the paper's Methods ("Extraction of electrophysiological
  features"). Where the Methods leave a detail open the paper's code settles it, and the
  docstring of the function says so. Where they disagree (the maximum number of APs) the
  Methods are followed and the code's choice is returned as well.
- The fast trough used for the AHP is the minimum within 5 ms after the peak (Allen SDK
  convention; the paper's figure only shows it).
"""

from __future__ import annotations

import hashlib
import io
import warnings
from concurrent.futures import ProcessPoolExecutor

import numpy as np
import pandas as pd
from scipy import signal
from scipy.optimize import curve_fit

DANDISET = "000035"
VERSION = "0.211014.0808"

# The paper's code and published tables, at the commit read for this attempt.
MINI_ATLAS = "https://raw.githubusercontent.com/berenslab/mini-atlas/3bf98a524b8e48aa8647e1b9ae8f2351d9c712c9/data/"

FS_EXPECTED = 25000.0       # Hz, checked against every series
START, END = 0.1, 0.7       # s, the current step, checked against every stimulus series
DV_CUTOFF = 20.0            # V/s, spike detection (code default)
FILTER_KHZ = 10.0           # Bessel low-pass before differentiation (code default)
MIN_PEAK, MIN_HEIGHT = -30.0, 2.0   # mV (code defaults)
THRESH_FRAC = 0.05          # threshold at 5% of the mean upstroke slope (code default)
FAST_TROUGH = 0.005         # s after the peak, for the AHP
BEFORE, AFTER = 0.1, 0.2    # s around the step searched for spikes outside it (Methods)

# The 17 features the paper uses (Methods), named as in the paper's tables.
FEATURES = [
    "AP amplitude (mV)", "AP amplitude adaptation index", "AP coefficient of variation",
    "AP threshold (mV)", "AP width (ms)", "Afterhyperpolarization (mV)", "ISI adaptation index",
    "ISI coefficient of variation", "Input resistance (MOhm)", "Latency (ms)", "Max number of APs",
    "Membrane time constant (ms)", "Rebound (mV)", "Resting membrane potential (mV)",
    "Rheobase (pA)", "Sag ratio", "Upstroke-to-downstroke ratio",
]
LOG_FEATURES = ["AP coefficient of variation", "ISI coefficient of variation",
                "ISI adaptation index", "Latency (ms)"]


# --- labels -------------------------------------------------------------------

def family_of(ttype) -> str | None:
    """Transcriptomic family (subclass) from a t-type name, as the paper groups them.

    The files use the reference taxonomy's older names, in which ET types are called "L5 PT".
    """
    if not isinstance(ttype, str) or not ttype:
        return None
    for key, family in ((" IT", "IT"), (" PT", "ET"), (" ET", "ET"), (" NP", "NP"), (" CT", "CT")):
        if key in ttype:
            return family
    first = ttype.split()[0]
    return first if first in ("Sst", "Pvalb", "Vip", "Lamp5", "Sncg") else None


def layer_from_depth(depth, thickness):
    """Layer from normalized soma depth, with the Nissl boundaries in the paper's code."""
    x = np.asarray(depth, float) / np.asarray(thickness, float)
    out = np.full(x.shape, None, dtype=object)
    with np.errstate(invalid="ignore"):
        out[x < 0.07] = "1"
        out[(x > 0.07) & (x < 0.29)] = "2/3"
        out[(x > 0.29) & (x < 0.73)] = "5"
        out[x > 0.73] = "6"
    return out


# --- loading ------------------------------------------------------------------

def asset_urls(version: str = VERSION) -> list[tuple[str, str]]:
    from dandi.dandiapi import DandiAPIClient
    dandiset = DandiAPIClient().get_dandiset(DANDISET, version)
    return sorted((a.path, a.get_content_url(follow_redirects=1, strip_query=True))
                  for a in dandiset.get_assets())


def _text(x):
    return x.decode() if isinstance(x, bytes) else x


def read_sweeps(f):
    """All sweeps of one open file: (amplitude in pA, voltage in mV, stimulus or None) by amplitude.

    Sweeps are paired with their stimulus through the sweep table's sweep numbers. The 0 pA
    sweep is an IZeroClampSeries with no stimulus series.
    """
    table = f["general/intracellular_ephys/sweep_table"]
    by_sweep = {}
    for ref, number in zip(table["series"][:], table["sweep_number"][:]):
        obj = f[ref]
        kind = "stim" if obj.name.startswith("/stimulus") else "resp"
        by_sweep.setdefault(int(number), {})[kind] = obj
    sweeps = []
    for number, pair in sorted(by_sweep.items()):
        resp = pair["resp"]
        v = resp["data"][:] * resp["data"].attrs["conversion"]
        stim = pair.get("stim")
        i = None if stim is None else stim["data"][:] * stim["data"].attrs["conversion"]
        sweeps.append(dict(number=number, v=v, i=i,
                           rate=float(resp["starting_time"].attrs["rate"]),
                           starting_time=float(resp["starting_time"][()]),
                           v_unit=resp["data"].attrs["unit"],
                           i_unit=None if stim is None else stim["data"].attrs["unit"],
                           kind=_text(resp.attrs.get("neurodata_type"))))
    return sweeps


def load_cell(job):
    """Stream one file and reduce it to metadata, checks and features (one dict)."""
    import h5py
    import remfile
    path, url = job
    warnings.filterwarnings("ignore")
    with h5py.File(remfile.File(url), "r") as f:
        meta = {k: _text(v[()]) for k, v in f["general/DandiIcephysMetadata"].items()}
        meta = {k: (v.item() if hasattr(v, "item") else v) for k, v in meta.items()}
        subject = {k: _text(f["general/subject"][k][()]) for k in f["general/subject"]}
        description = _text(f["session_description"][()])
        sweeps = read_sweeps(f)
    row = {"path": path, **meta, **{f"subject_{k}": v for k, v in subject.items()},
           "session_description": description}

    # Stimulus: amplitude, onset and offset of each step, read from the stimulus series.
    amps, onsets, offsets = [], [], []
    for s in sweeps:
        if s["i"] is None:
            amps.append(0.0)
            continue
        on = np.flatnonzero(s["i"] != 0)
        amps.append(float(np.median(s["i"][on])) if on.size else 0.0)
        if on.size:
            onsets.append(on[0] / s["rate"])
            offsets.append((on[-1] + 1) / s["rate"])
    amps = np.array(amps)
    row.update(
        n_sweeps=len(sweeps), amplitudes=amps.tolist(),
        rates=sorted({s["rate"] for s in sweeps}),
        resp_samples=sorted({len(s["v"]) for s in sweeps}),
        stim_samples=sorted({len(s["i"]) for s in sweeps if s["i"] is not None}),
        starting_times_nan=all(np.isnan(s["starting_time"]) for s in sweeps),
        v_units=sorted({s["v_unit"] for s in sweeps}),
        i_units=sorted({s["i_unit"] for s in sweeps if s["i_unit"]}),
        zero_kinds=sorted({s["kind"] for s in sweeps if s["i"] is None}),
        step_onsets=(min(onsets), max(onsets)) if onsets else (np.nan, np.nan),
        step_offsets=(min(offsets), max(offsets)) if offsets else (np.nan, np.nan),
        v_min=float(min(s["v"].min() for s in sweeps)),
        v_max=float(max(s["v"].max() for s in sweeps)),
        hash_first=hashlib.md5(sweeps[0]["v"].tobytes()).hexdigest(),
        hash_all=hashlib.md5(b"".join(s["v"].tobytes() for s in sweeps)).hexdigest(),
    )
    rate = sweeps[0]["rate"]
    order = np.argsort(amps, kind="stable")
    V = [sweeps[k]["v"] for k in order]
    row.update(timing_checks(V, amps[order], rate))
    try:
        row.update(cell_features(V, amps[order], rate))
        row["feature_error"] = ""
    except Exception as e:      # recorded and counted in the notebook, never silently dropped
        row["feature_error"] = f"{type(e).__name__}: {e}"
    return row


def load_cohort(version: str = VERSION, workers: int = 12) -> pd.DataFrame:
    """Stream all files in parallel; one row per neuron."""
    jobs = asset_urls(version)
    with ProcessPoolExecutor(workers) as ex:
        rows = list(ex.map(load_cell, jobs))
    df = pd.DataFrame(rows)
    df["family"] = df["RNA_type"].map(family_of)
    return df


def published_table(name: str, **kw) -> pd.DataFrame:
    """A table from the paper's repository at the pinned commit (outside input)."""
    import requests
    r = requests.get(MINI_ATLAS + name, timeout=120)
    r.raise_for_status()
    return pd.read_csv(io.StringIO(r.content.decode("utf-8")), **kw)


# --- timing -------------------------------------------------------------------

def timing_checks(V, amps, rate):
    """Does the voltage respond at the stimulus onset, in the direction of the current?

    For the most hyperpolarizing sweep and the first depolarizing sweep without spikes near the
    onset, the change of mean voltage from the 5 ms before to the 5 ms after the stimulus
    onset, and the same for a window 50 ms earlier (a null). Also the latency of the
    hyperpolarizing response: first sample after 0.09 s where the voltage is 1 mV below its
    mean over 0.05 to 0.1 s.
    """
    def step(v, t0):
        a, b = int(round((t0 - 0.005) * rate)), int(round(t0 * rate))
        c = int(round((t0 + 0.005) * rate))
        return float(v[b:c].mean() - v[a:b].mean())
    out = {}
    v = V[0]
    out["onset_step_hyper"] = step(v, START)
    out["onset_step_hyper_null"] = step(v, START - 0.05)
    base = v[int(0.05 * rate):int(START * rate)].mean()
    after = np.flatnonzero(v[int(0.09 * rate):] < base - 1.0)
    out["onset_latency_hyper_ms"] = (after[0] / rate + 0.09 - START) * 1000 if after.size else np.nan
    out["offset_step_hyper"] = step(v, END)
    pos = [k for k in range(len(amps)) if amps[k] > 0]
    out["amp_depol_check"] = float(amps[pos[0]]) if pos else np.nan
    out["onset_step_depol"] = step(V[pos[0]], START) if pos else np.nan
    out["onset_step_depol_null"] = step(V[pos[0]], START - 0.05) if pos else np.nan
    return out


# --- spikes -------------------------------------------------------------------

def dvdt(v, rate):
    """dV/dt in V/s after a 4-pole Bessel low-pass at FILTER_KHZ (as calculate_dvdt in the code)."""
    b, a = signal.bessel(4, FILTER_KHZ * 1e3 / (rate / 2), "low")
    return np.diff(signal.filtfilt(b, a, v)) * rate / 1000.0


def detect_spikes(v, rate, t0, t1, d=None):
    """Spikes whose dV/dt crosses DV_CUTOFF between t0 and t1 (s). One dict per spike, indexes."""
    if d is None:
        d = dvdt(v, rate)
    i0, i1 = int(round(t0 * rate)), min(int(round(t1 * rate)), len(d))
    if i1 - i0 < 3:
        return []
    above = d[i0:i1] >= DV_CUTOFF
    cross = list(np.flatnonzero(~above[:-1] & above[1:]) + i0 + 1)
    if above[0]:
        cross.insert(0, i0)
    spikes = []
    for n, c in enumerate(cross):
        nxt = cross[n + 1] if n + 1 < len(cross) else i1
        peak = c + int(np.argmax(v[c:nxt + 1]))
        if v[peak] < MIN_PEAK or v[peak] - v[c] < MIN_HEIGHT or peak == c:
            continue
        up = c + int(np.argmax(d[c:peak]))
        spikes.append(dict(cross=c, peak=peak, up=up))
    if not spikes:
        return []
    target = THRESH_FRAC * np.mean([d[s["up"]] for s in spikes])
    prev = i0
    for s in spikes:
        back = np.flatnonzero(d[prev:s["up"] + 1][::-1] <= target)
        s["thr"] = s["up"] - back[0] if back.size else prev
        prev = s["peak"]
    for n, s in enumerate(spikes):
        end = spikes[n + 1]["thr"] if n + 1 < len(spikes) else i1
        end = max(end, s["peak"] + 1)
        s["trough"] = s["peak"] + int(np.argmin(v[s["peak"]:end]))
        fast_end = max(min(end, s["peak"] + int(FAST_TROUGH * rate)), s["peak"] + 1)
        s["fast_trough"] = s["peak"] + int(np.argmin(v[s["peak"]:fast_end]))
        s["height"] = v[s["peak"]] - v[s["thr"]]
        level = v[s["thr"]] + s["height"] / 2
        rise = np.flatnonzero(v[s["thr"]:s["peak"] + 1] <= level)
        fall = np.flatnonzero(v[s["peak"]:s["trough"] + 1] <= level)
        s["width"] = ((s["peak"] + fall[0]) - (s["thr"] + rise[-1])) / rate if rise.size and fall.size else np.nan
        down = d[s["peak"]:max(s["trough"], s["peak"] + 1)]
        s["udr"] = d[s["up"]] / abs(down.min()) if down.size and down.min() < 0 else np.nan
    return spikes


# --- features -----------------------------------------------------------------

def _exp(t, a, inv_tau, y0):
    return y0 + a * np.exp(-inv_tau * t)


def time_constant(v, rate, v_rest):
    """Membrane time constant (s) of a hyperpolarizing sweep.

    As the paper's code (estimate_time_constant): an exponential fitted from the point where the
    voltage has fallen 10% of the way to its minimum, to that minimum; the minimum is searched
    from the onset to 100 ms before the offset.
    """
    i0, i1 = int(START * rate), int((END - 0.1) * rate)
    k = i0 + int(np.argmin(v[i0:i1]))
    below = np.flatnonzero(v[i0:] <= v_rest + 0.1 * (v[k] - v_rest))
    if not below.size or i0 + below[0] >= k - 3:
        return np.nan
    j = i0 + below[0]
    t = np.arange(k - j) / rate
    try:
        popt, _ = curve_fit(_exp, t, v[j:k], p0=(v[j] - v[k], 50.0, v[k]), maxfev=5000)
    except RuntimeError:
        return np.nan
    return 1.0 / popt[1] if popt[1] > 0 else np.nan


def rheobase(currents, counts, seed=0):
    """Rheobase (pA) as in the Methods and the paper's code.

    RANSAC regression of spike frequency on current over the five lowest non-negative currents
    with spikes; the crossing of zero, kept between the last current without spikes and the
    first with spikes, else the first current with spikes. Fewer than five such currents, or
    three or more of them with the same count, give the first current with spikes (code).
    """
    from sklearn.linear_model import RANSACRegressor
    currents, counts = np.asarray(currents, float), np.asarray(counts, float)
    keep = currents >= 0
    currents, counts = currents[keep], counts[keep]
    spiking = np.flatnonzero(counts > 0)
    if not spiking.size:
        return np.nan
    first = currents[spiking[0]]
    if spiking.size < 5:
        return first
    idx = spiking[:5]
    if max(list(counts[idx]).count(x) for x in counts[idx]) >= 3:
        return first
    model = RANSACRegressor(random_state=seed).fit(currents[idx, None], counts[idx] / (END - START))
    slope = model.estimator_.coef_[0]
    if slope <= 0:
        return first
    r = -model.predict(np.array([[0.0]]))[0] / slope
    below = currents[spiking[0] - 1] if spiking[0] > 0 else -np.inf
    return first if (r < below or r > first) else r


def cell_features(V, amps, rate):
    """The 17 features of one neuron, plus a few the notebook reports. V sorted by amplitude."""
    amps = np.asarray(amps, float)
    n = len(V)
    i_pre = slice(0, int(START * rate))
    i_ss = slice(int((END - 0.1) * rate), int(END * rate))
    D = [dvdt(v, rate) for v in V]
    spikes = [detect_spikes(V[k], rate, START, END, D[k]) for k in range(n)]
    counts = np.array([len(s) for s in spikes])
    outside = np.array([len(detect_spikes(V[k], rate, START - BEFORE, START, D[k]))
                        + len(detect_spikes(V[k], rate, END, END + AFTER, D[k])) for k in range(n)])
    out = {}

    # Passive properties: hyperpolarizing sweeps.
    hyper = [k for k in range(n) if amps[k] < 0]
    rest = np.array([V[k][i_pre].mean() for k in hyper])
    out["Resting membrane potential (mV)"] = float(np.median(rest)) if hyper else np.nan
    rin = [abs(V[k][i_ss].mean() - V[k][i_pre].mean()) * 1000 / abs(amps[k])
           for k in hyper if counts[k] == 0]
    out["Input resistance (MOhm)"] = float(np.median(rin)) if rin else np.nan
    taus = [time_constant(V[k], rate, V[k][i_pre].mean()) for k in hyper]
    taus = [t for t in taus if np.isfinite(t)]
    out["Membrane time constant (ms)"] = float(np.median(taus)) * 1000 if taus else np.nan
    out["n_tau_fits_failed"] = len(hyper) - len(taus)

    # Sag and rebound: the lowest sweep (Methods).
    v = V[0]
    v_rest, v_ss = v[i_pre].mean(), v[i_ss].mean()
    i0, i1 = int(START * rate), int((END - 0.1) * rate)
    k = i0 + int(np.argmin(v[i0:i1]))
    half = int(0.0025 * rate)
    trough = v[max(k - half, 0):k + half + 1].mean()
    out["Sag ratio"] = float((trough - v_rest) / (v_ss - v_rest)) if v_ss != v_rest else np.nan
    e = int(END * rate)
    back = np.flatnonzero(v[e:] > v_rest)
    if not back.size:
        rebound = 0.0
    else:
        j = e + back[0]
        rebound = float(v[j:j + int(0.15 * rate)].mean() - v_rest)
    out["Rebound (mV)"] = max(rebound, 0.0)        # the code sets negative values to zero
    out["lowest_amplitude"] = float(amps[0])

    # Spiking properties: depolarizing sweeps.
    depol = [k for k in range(n) if amps[k] > 0]
    spiking = [k for k in depol if counts[k] > 0]
    out["n_spiking_sweeps"] = len(spiking)
    if not spiking:
        for name in FEATURES:
            out.setdefault(name, np.nan)
        return out
    k1 = spiking[0]
    s = spikes[k1][0]
    v1 = V[k1]
    out["AP threshold (mV)"] = float(v1[s["thr"]])
    out["AP amplitude (mV)"] = float(s["height"])
    out["AP width (ms)"] = float(s["width"] * 1000)
    out["Upstroke-to-downstroke ratio"] = float(s["udr"])
    out["Afterhyperpolarization (mV)"] = float(v1[s["fast_trough"]] - v1[s["thr"]])
    out["Latency (ms)"] = float((s["thr"] / rate - START) * 1000)
    out["Rheobase (pA)"] = float(rheobase(amps, counts))

    # Highest firing trace: first sweep with the most spikes among sweeps without spikes in the
    # 100 ms before or the 200 ms after the step (Methods). The code takes the maximum count
    # before that exclusion; it is kept as a variant.
    clean = [k for k in depol if outside[k] == 0]
    out["Max number of APs (code)"] = int(counts.max())
    if clean and counts[clean].max() > 0:
        best = max(counts[clean])
        kmax = next(k for k in clean if counts[k] == best)
        out["Max number of APs"] = int(best)
        sp = spikes[kmax]
        t = np.array([x["thr"] for x in sp]) / rate
        isi = np.diff(t)
        out["ISI coefficient of variation"] = float(isi.std() / isi.mean()) if isi.size >= 2 else np.nan
        h = np.array([x["height"] for x in sp])
        out["AP coefficient of variation"] = float(h.std() / h.mean()) if h.size >= 2 else np.nan
    else:
        for name in ("Max number of APs", "ISI coefficient of variation", "AP coefficient of variation"):
            out[name] = np.nan
    out["n_sweeps_spikes_outside"] = int((outside[depol] > 0).sum())

    # Adaptation: median over the five lowest depolarizing sweeps with enough spikes (Methods).
    isi_ad = []
    for k in [k for k in depol if counts[k] >= 3][:5]:
        t = np.array([x["thr"] for x in spikes[k]]) / rate
        isi = np.diff(t)
        isi_ad.append(isi[1] / isi[0])
    out["ISI adaptation index"] = float(np.median(isi_ad)) if isi_ad else np.nan
    amp_ad = []
    for k in [k for k in depol if counts[k] >= 2][:5]:
        h = [x["height"] for x in spikes[k]]
        amp_ad.append(h[1] / h[0])
    out["AP amplitude adaptation index"] = float(np.median(amp_ad)) if amp_ad else np.nan
    return out


# --- representation and classifier --------------------------------------------

def representation(table: pd.DataFrame, features=FEATURES) -> np.ndarray:
    """The paper's electrophysiological representation (phenotype-tsne.ipynb in its code).

    Four features log-transformed, all standardized, all principal components, scaled by the
    standard deviation of the first. Rows with any missing feature must be removed before.
    """
    X = table[features].to_numpy(float).copy()
    for j, name in enumerate(features):
        if name in LOG_FEATURES:
            X[:, j] = np.log(X[:, j])
    X = (X - X.mean(0)) / X.std(0)
    U, S, Vt = np.linalg.svd(X, full_matrices=False)
    pcs = X @ Vt.T
    return pcs / pcs[:, 0].std()


def knn_family_confusion(X, families, classes, k=10):
    """Leave-one-out kNN classification into families, as get_family_confusion in the code.

    Neighbours are drawn from all rows. A cell whose neighbours' majority family is not one of
    `classes` is not counted. Ties go to the alphabetically first family (np.unique, as in the
    code). Returns the row-normalized confusion matrix and the number of cells counted per row.
    """
    from sklearn.neighbors import NearestNeighbors
    families = np.asarray(families, dtype=object)
    labels = np.array([f if isinstance(f, str) else "" for f in families])
    idx = NearestNeighbors(n_neighbors=k).fit(X).kneighbors(return_distance=False)
    C = pd.DataFrame(0.0, index=classes, columns=classes)
    counted = pd.Series(0, index=classes)
    for cl in classes:
        for i in np.flatnonzero(labels == cl):
            u, c = np.unique(labels[idx[i]], return_counts=True)
            winner = u[np.argmax(c)]
            if winner in classes:
                C.loc[cl, winner] += 1
                counted[cl] += 1
    return C.div(counted.replace(0, np.nan), axis=0), counted
