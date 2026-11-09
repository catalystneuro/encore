"""Loading and measures for the ex vivo patch-clamp data of dandiset 001195.

Lee, Matthews, Lemieux et al. (2025), eLife, doi:10.7554/eLife.105955, "Separable Dorsal Raphe
Dopamine Projections mediate the Facets of Loneliness-like state".

Each `*_icephys.nwb` file holds one cell: its region (`general/DandiIcephysMetadata`, field
`inferred_layer`), the subject's virus (`general/subject/description`, ChR2 or ChrimsonR) and its
sweeps under `acquisition`, each sweep a pair of series `...-ch-0` and `...-ch-1`. The protocol of
a sweep is named only in the series description ("Response to: episodic stimulation, 8*30Hz laser
pulses, 5ms width, every 30s, -30pA hold"). In current clamp ch-0 is the membrane potential and
ch-1 the injected current; ch-1 is labelled volts but its conversion (6.1e-13) and values (pA)
show it is current. The files hold no record of the light: the stimulus series are zeros. Files
are streamed from the archive at the pinned version; nothing is written to disk.

Where the parameters come from:

- Sampling at 10 kHz: the files (`rate`), as in the Methods ("digitized at 10 kHz").
- LIGHT_ONSET_S, the first light pulse 5.468 s into each 30 s light sweep: not in the files; it is
  read from the data, the onset of the average evoked response in the cells that respond, with
  the following pulses 33 ms apart (30 Hz). The notebook shows the check. An assumption.
- Baseline of 5 s before the light, the peak (EPSP) or trough (IPSP) of the average trace and the
  total voltage area 0-5.5 s after the first pulse: Methods, Ex vivo electrophysiology ("using
  the 5 s prior to stimulation as baseline", "Total voltage area was calculated from 0-5.5 s
  following the onset of the first light pulse"), as the claims' criteria give them.
- Detection of an EPSP or IPSP beyond K standard deviations of the 5 s baseline of the average
  trace, K = 2 or 3: the readings named in the criterion of fig6df-epsp-ipsp-at-rest.
- CONTROL_ONSET_S, a light-free window 12 s after the light (baseline 12.5-17.5 s, "response"
  17.5-23 s, before the test step some sweeps have at 24.5 s): the same detection run where no light
  is given, to measure how often it detects noise (a check, not a method of the paper).
- Sweeps at rest: current-clamp 30 s light sweeps with no holding current or a negative one
  (Methods: "In a minority of cells which showed spontaneous activity at the resting potential,
  negative current was injected to hold the cell at a subthreshold potential"), and, as that
  passage says the cells were subthreshold, only those with no action potential in the 5 s before
  the light (`subthreshold`). Firing sweeps:
  the same protocol with a positive holding current (Methods: "constant positive current was
  injected to elicit consistent spontaneous action potentials").
- IEI 5 s before and 5 s after the first pulse: Methods; 5.5 s before as a variant (Figure 6
  supplement 1G legend). Action potentials are upward crossings of 0 mV, a standard choice.
- Baseline features from the 1 s current steps (-120 to 260 pA in 20 pA): Methods. Sag, peak
  minus steady state in the -120 pA step; ramp ratio, mean Vm 900-1000 ms over mean Vm 100-200 ms
  at the largest subthreshold step; firing delay, step onset to first spike at rheobase; maximum
  instantaneous frequency, the highest 1/ISI of spike pairs in the first 100 ms of a depolarizing
  step. The injected current of each step is read from ch-1.
- Capacitance by the Q-method (Methods, ref. 138): the charge of the capacitive transient,
  integrated against the steady-state current, divided by the voltage step, here from the 5 mV
  square-pulse seal test (the only voltage-clamp test pulse in the files; the Methods describe a
  5 mV, 250 ms step). A substitution, stated in the notebook. With no correction for the series and
  membrane resistance, and the integration starting 10 samples before the edge, it reads low (42 pF
  for a 50 pF cell with 15 MOhm series and 300 MOhm membrane resistance, in the verifier's test); the
  bias is the same in every cell, so the clustering, which normalizes each feature, is little affected.
"""

from __future__ import annotations

import hashlib
import re
from concurrent.futures import ThreadPoolExecutor
from itertools import combinations

import h5py
import numpy as np
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy import stats

DANDISET_ID = "001195"
DANDISET_VERSION = "0.250408.1733"

FS = 10_000.0                 # Hz, from the files
LIGHT_ONSET_S = 5.468         # first light pulse in a 30 s light sweep, read from the data (assumption)
BASELINE_S = 5.0              # Methods: 5 s prior to stimulation
WINDOW_S = 5.5                # Methods: total voltage area 0-5.5 s after the first pulse
IEI_S = 5.0                   # Methods: IEI 5 s before and 5 s after
IEI_BASELINE_VARIANT_S = 5.5  # Figure 6 supplement 1G legend
SPIKE_THRESHOLD_MV = 0.0      # standard choice
LIGHT_SWEEP_SAMPLES = 300_000
CONTROL_ONSET_S = LIGHT_ONSET_S + 12.0   # a light-free window: 5 s baseline and 5.5 s "response", 12-23 s
READ_SAMPLES = int(23.0 * FS)    # to 23 s: the analysis window and the light-free window, before the test step at 24.5 s

LIGHT_PROTOCOL = "Response to: episodic stimulation, 8*30Hz laser pulses, 5ms width, every 30s"
RED_PROTOCOL = "Response to: episodic stimulation, 8*30Hz 635nm laser pulses, 10mW, 5ms width, every 30s"
STEP_PROTOCOL = "Response to: episodic stimulation, 1s steps, 20pA increments, "
SEAL_PROTOCOL = "Response to: baseline, seal test"


def assets():
    """(path, url) of every NWB file of the pinned version."""
    client = DandiAPIClient()
    ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
    return [(a.path, a.get_content_url(follow_redirects=1, strip_query=True))
            for a in ds.get_assets() if a.path.endswith(".nwb")]


def sweep_kind(series_name: str, description: str, n: int) -> str | None:
    """The role of a sweep in the analysis, from its series type and its protocol description."""
    if description == SEAL_PROTOCOL:
        return "seal"
    if not series_name.startswith("current_clamp"):
        return None
    if description.startswith(STEP_PROTOCOL) and n == 50_000:
        # the Methods' -120 to 260 pA series, and in some cells a further series from 220 pA up
        return "steps"
    if n != LIGHT_SWEEP_SAMPLES:
        return None
    if description.startswith(RED_PROTOCOL):
        rest = description[len(RED_PROTOCOL):]
        if rest == "":
            return "red"
        if "cont blue" in rest:
            return "red_contblue"
        if "+0.3mW blue" in rest:
            return "blue03"
        if "+0.2mW blue" in rest:
            return "blue02"
        return None
    if not description.startswith(LIGHT_PROTOCOL):
        return None
    rest = description[len(LIGHT_PROTOCOL):].strip(" ,;")
    if rest in ("", "+step") or rest.startswith("@-"):
        # no holding current; "+step" is a test step at 24.5 s, after the analysis window;
        # "@-60mV" and "@-50mV" are held below threshold
        return "rest"
    m = re.match(r"^([+-]?\d+)\s*(?:-\s*-?\d+)?\s*p[aA](?: hold)?$", rest)
    if m:
        return "firing" if int(m.group(1)) > 0 else "rest"
    return None


def _read(series, n=None):
    data = series["data"]
    x = data[:n] if n else data[:]
    return x.astype(np.float64) * float(data.attrs["conversion"])


def load_cell(path_url):
    """Everything the analysis needs from one cell, reduced as it loads."""
    path, url = path_url
    f = h5py.File(remfile.File(url), "r")
    md = f["general/DandiIcephysMetadata"]
    cell = {
        "path": path,
        "subject": f["general/subject/subject_id"][()].decode(),
        "virus": f["general/subject/description"][()].decode(),
        "region": md["inferred_layer"][()].decode(),
        "targeted": md["targeted_layer"][()].decode(),
        "cell_id": md["cell_id"][()].decode(),
        "sex": f["general/subject/sex"][()].decode(),
        "session_description": f["session_description"][()].decode(),
        "stimulus_types": [x.decode() for x in f["general/intracellular_ephys/sequential_recordings/stimulus_type"][:]],
        "electrode_descriptions": sorted({f[f"general/intracellular_ephys/{k}/description"][()].decode()
                                          for k in f["general/intracellular_ephys"] if k.startswith("electrode-")}),
        "sweeps": {},
        "hashes": [],
        "dropped": 0,
        "rates": set(),
        "descriptions": set(),
    }
    acq = f["acquisition"]
    for name in sorted(acq):
        if not name.endswith("ch-0") or "data" not in acq[name]:
            continue
        g = acq[name]
        desc = g.attrs.get("description", "")
        cell["descriptions"].add(desc)
        n = g["data"].shape[0]
        kind = sweep_kind(name, desc, n)
        if kind is None:
            if name.startswith("current_clamp") or name.startswith("voltage_clamp"):
                cell["dropped"] += 1
            continue
        cell["rates"].add(float(g["starting_time"].attrs["rate"]))
        g1 = acq[name.replace("ch-0", "ch-1")]
        if kind == "steps":
            v, i = _read(g) * 1e3, _read(g1) * 1e12          # mV, pA
            rec = {"v": v, "i": i}
        elif kind == "seal":
            i, v = _read(g) * 1e12, _read(g1) * 1e3          # pA, mV
            rec = {"v": v, "i": i}
        else:
            v = (_read(g, READ_SAMPLES) * 1e3).astype(np.float32)
            rec = {"v": v, "desc": desc, "hold_pA": float(np.median(_read(g1, 2000)) * 1e12)}
        cell["hashes"].append(hashlib.sha1(g["data"][:5000].tobytes()).hexdigest())
        cell["sweeps"].setdefault(kind, []).append(rec)
    f.close()
    return cell


def load_cells(path_urls, workers=12):
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(load_cell, path_urls))


# ---------------------------------------------------------------- evoked potentials

def light_window(v, onset=LIGHT_ONSET_S):
    """Baseline (5 s before) and response (0-5.5 s after) parts of a trace."""
    i0 = int(round(onset * FS))
    return v[i0 - int(BASELINE_S * FS):i0], v[i0:i0 + int(WINDOW_S * FS)]


def evoked(avg, k, onset=LIGHT_ONSET_S):
    """EPSP peak, IPSP trough (mV, from the baseline mean), area (mV s) and their detection at k SD."""
    base, resp = light_window(avg, onset)
    b, sd = base.mean(), base.std()
    peak = resp.max() - b
    trough = resp.min() - b
    return {
        "baseline_mV": b, "sd_mV": sd, "peak_mV": peak, "trough_mV": trough,
        "area_mVs": (resp - b).sum() / FS, "abs_area_mVs": np.abs(resp - b).sum() / FS,
        "epsp": peak > k * sd, "ipsp": trough < -k * sd,
    }


def response_class(e):
    if e["epsp"] and e["ipsp"]:
        return "mix"
    if e["epsp"]:
        return "excitation"
    if e["ipsp"]:
        return "inhibition"
    return "none"


def valid(sweeps):
    """The sweeps whose injected current (ch-1) is within +-10 nA. Outside it the recording failed: in the
    one cell that has such sweeps (P10) their membrane potential is flat at 0 mV."""
    return [s for s in sweeps if abs(s["hold_pA"]) < 1e4]


def subthreshold(sweeps, onset=LIGHT_ONSET_S):
    """The sweeps with no action potential in the 5 s before the light. Methods: at rest, cells "which
    showed spontaneous activity at the resting potential" were held "at a subthreshold potential"."""
    i0 = int(round(onset * FS))
    return [s for s in sweeps if len(spike_times(s["v"][i0 - int(BASELINE_S * FS):i0])) == 0]


def average(sweeps):
    return np.mean([s["v"] for s in sweeps], axis=0, dtype=np.float64)


# ---------------------------------------------------------------- firing

def spike_times(v, threshold=SPIKE_THRESHOLD_MV):
    """Times (s) of upward crossings of the threshold."""
    up = np.flatnonzero((v[:-1] < threshold) & (v[1:] >= threshold)) + 1
    return up / FS


def iei_change(sweeps, before_s=IEI_S, after_s=IEI_S, onset=LIGHT_ONSET_S):
    """Mean IEI before and after the first pulse under readings (a) pooled and (b) mean of sweep means."""
    pooled_b, pooled_a, per_b, per_a = [], [], [], []
    for s in sweeps:
        t = spike_times(s["v"])
        tb = t[(t >= onset - before_s) & (t < onset)]
        ta = t[(t >= onset) & (t < onset + after_s)]
        ib, ia = np.diff(tb), np.diff(ta)
        pooled_b += list(ib)
        pooled_a += list(ia)
        if len(ib):
            per_b.append(ib.mean())
        if len(ia):
            per_a.append(ia.mean())
    out = {}
    out["a_before"] = np.mean(pooled_b) if pooled_b else np.nan
    out["a_after"] = np.mean(pooled_a) if pooled_a else np.nan
    out["b_before"] = np.mean(per_b) if per_b else np.nan
    out["b_after"] = np.mean(per_a) if per_a else np.nan
    out["n_spikes_before"] = len(pooled_b) + len(per_b)
    return out


def iei_label(before, after):
    if np.isnan(before) or np.isnan(after) or before == after:
        return None
    return "excitation" if after < before else "inhibition"


# ---------------------------------------------------------------- baseline properties

def step_epochs(i, min_step_pA=10.0):
    """Start and stop samples of the current step, from the injected current (ch-1)."""
    base = np.median(i[: int(0.05 * FS)])
    d = np.abs(np.convolve(i - base, np.ones(50) / 50, mode="same"))
    if d.max() < min_step_pA:
        return None
    on = np.flatnonzero(d > d.max() / 2)
    if len(on) < 0.5 * FS:
        return None
    return on[0], on[-1] + 1


def step_features(steps, sag_ss_ms=100):
    """Sag, ramp ratio (absolute Vm and deflections), firing delay and max instantaneous frequency."""
    rows = []
    for s in steps:
        ep = step_epochs(s["i"])
        if ep is None:
            # the 0 pA step has no current change; it is subthreshold and adds nothing the others lack
            continue
        a, b = ep
        cur = np.median(s["i"][a:b]) - np.median(s["i"][: int(0.05 * FS)])
        v = s["v"]
        t = spike_times(v[a:b])
        rows.append({"cur": cur, "a": a, "b": b, "v": v, "spikes": t,
                     "pre": v[max(0, a - int(0.1 * FS)):a].mean()})
    if not rows:
        return None
    rows.sort(key=lambda r: r["cur"])
    out = {"n_steps": len(rows), "min_pA": rows[0]["cur"], "max_pA": rows[-1]["cur"]}
    neg = [r for r in rows if abs(r["cur"] + 120) < 10]
    if neg:
        r = neg[0]
        seg = r["v"][r["a"]:r["b"]]
        n_ss = int(sag_ss_ms / 1000 * FS)
        out["sag_mV"] = seg[-n_ss:].mean() - seg.min()
    pos_sub = [r for r in rows if r["cur"] > 0 and len(r["spikes"]) == 0]
    if pos_sub:
        r = pos_sub[-1]
        seg = r["v"][r["a"]:r["b"]]
        late = seg[int(0.9 * FS):int(1.0 * FS)].mean()
        early = seg[int(0.1 * FS):int(0.2 * FS)].mean()
        out["ramp_ratio"] = late / early
        out["ramp_ratio_deflection"] = (late - r["pre"]) / (early - r["pre"]) if early != r["pre"] else np.nan
    supra = [r for r in rows if r["cur"] > 0 and len(r["spikes"])]
    if supra:
        out["firing_delay_ms"] = supra[0]["spikes"][0] * 1e3
        f = 0.0
        for r in supra:
            t = r["spikes"][r["spikes"] < 0.1]
            if len(t) > 1:
                f = max(f, (1.0 / np.diff(t)).max())
        out["max_freq_hz"] = f
    return out


def cell_capacitance_pf(seals):
    """Median over a cell's seal tests of the Q-method estimates. An estimate from fewer than 5 pulses,
    or of 0 pF or less, is a failed fit and is left out (a standard choice). NaN when all fail."""
    vals = [capacitance_pf(s) for s in seals]
    vals = [v for v, n in vals if n >= 5 and np.isfinite(v) and v > 0]
    return np.median(vals) if vals else np.nan


def capacitance_pf(seal):
    """Capacitance (pF) by the Q-method from the 5 mV square pulses of the seal test."""
    v, i = seal["v"], seal["i"]
    vs = np.convolve(v, np.ones(20) / 20, mode="same")
    hi, lo = np.percentile(vs, 90), np.percentile(vs, 10)
    mid = (hi + lo) / 2
    edges = np.flatnonzero(np.diff(np.sign(vs - mid)) != 0)
    caps = []
    for k, e in enumerate(edges[:-1]):
        nxt = edges[k + 1]
        if nxt - e < int(0.04 * FS) or e < 20:
            continue
        seg = i[e - 10:nxt - 10]
        n_ss = max(int(0.2 * (nxt - e)), 10)
        ss = seg[-n_ss:].mean()
        dv = vs[e + (nxt - e) // 2] - vs[max(e - (nxt - e) // 2, 0)]
        q = (seg - ss).sum() / FS          # pA s = pC
        if abs(dv) > 1:
            caps.append(q / dv * 1e3)       # pC/mV = nF -> pF
    return np.median(caps) if caps else np.nan, len(caps)


# ---------------------------------------------------------------- statistics (GraphPad Prism's tests)

def dunn(groups: dict):
    """Dunn's test after Kruskal-Wallis, with ties corrected; p multiplied by the number of
    comparisons, as Prism's Dunn's multiple comparisons test does."""
    names = list(groups)
    allv = np.concatenate([np.asarray(groups[k], float) for k in names])
    ranks = stats.rankdata(allv)
    n = len(allv)
    _, counts = np.unique(allv, return_counts=True)
    tie = (counts ** 3 - counts).sum() / (12 * (n - 1))
    mean_rank, start = {}, 0
    for k in names:
        m = len(groups[k])
        mean_rank[k] = ranks[start:start + m].mean()
        start += m
    pairs = list(combinations(names, 2))
    out = {}
    for a, b in pairs:
        se = np.sqrt((n * (n + 1) / 12 - tie) * (1 / len(groups[a]) + 1 / len(groups[b])))
        z = (mean_rank[a] - mean_rank[b]) / se
        out[(a, b)] = min(1.0, 2 * stats.norm.sf(abs(z)) * len(pairs))
    return out


def holm_sidak(groups: dict):
    """Holm-Sidak comparisons of all pairs after a one-way ANOVA, on the pooled residual variance."""
    names = list(groups)
    data = {k: np.asarray(groups[k], float) for k in names}
    n = sum(len(v) for v in data.values())
    dfw = n - len(names)
    mse = sum(((v - v.mean()) ** 2).sum() for v in data.values()) / dfw
    pairs = list(combinations(names, 2))
    raw = []
    for a, b in pairs:
        t = (data[a].mean() - data[b].mean()) / np.sqrt(mse * (1 / len(data[a]) + 1 / len(data[b])))
        raw.append(2 * stats.t.sf(abs(t), dfw))
    order = np.argsort(raw)
    adj, running = {}, 0.0
    for rank, idx in enumerate(order):
        p = 1 - (1 - raw[idx]) ** (len(pairs) - rank)
        running = max(running, p)
        adj[pairs[idx]] = min(1.0, running)
    return adj
