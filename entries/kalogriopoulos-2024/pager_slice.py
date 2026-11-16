"""Loading and per-sweep measures for the CA1 slice recordings of dandiset 001354.

Kalogriopoulos, Tei et al. (2024), Nature 637, 230-239, doi:10.1038/s41586-024-08282-3,
Fig. 4e-j and Extended Data Fig. 12a-h.

Each NWB file holds one cell: a run of 5-s current clamp sweeps at 20 kHz, each on two channels.
Channel 0 (`current_clamp-response-NN-ch-0`) is the membrane potential. Channel 1
(`current_clamp-response-NN-ch-1`) is stored as a CurrentClampSeries in volts, but its values
(about -1.5e-10 to 5e-10) are the injected current in amperes; it is read here as the current
monitor. The stored stimulus (`stimulus-NN-ch-0`) gives the ramp as a step to +500 pA, so the
current at each moment is read from channel 1. Files are streamed from the archive at the pinned
version; nothing is written to disk.

Where the parameters come from:

- Sweep layout, from the Methods (Neuronal electrophysiology assay in brain slices, Slice
  electrophysiology: "5 s sweeps ... a brief hyperpolarizing current step (-100 pA, 200 ms),
  followed shortly later (300 ms) by a linearly ramping current delivery (-150 to +500 pA,
  across 2 s)"), with the times read from the stored stimulus and channel 1: step 0.5 to 0.7 s,
  -150 pA from 1.0 s, ramp from 1.1 to 3.1 s.
- RMP: "the average value during the period (500 ms) in each sweep prior to any current
  injection" (Methods), so 0 to 0.5 s.
- Rin: steady-state voltage change to the -100 pA step divided by -100 pA (Methods; claim
  fig4i-rmp-hyperpolarization). The steady-state window is not given; the claim's criterion names
  the readings `RIN_WINDOWS`, the last 50 ms and the last 100 ms of the step.
- Action potentials, counted during the ramp (Methods: "All action potentials were counted during
  the ramping current delivery"), from 1.1 s to the end of the ramp as channel 1 delivers it. In
  ten cells the delivered ramp reaches +500 pA at 2.5 or 2.7 s, earlier than the 2 s of the
  Methods; the window follows the delivered ramp. Detection is not given; the criterion of
  fig4i-rmp-hyperpolarization names the readings A1, an upward crossing of 0 mV, and A2, dV/dt
  above 20 V/s.
- Rheobase: "the current being delivered when the first action potential of each sweep was
  evoked" (Methods), read from channel 1 at the time of detection, with the ramp formula and the
  stored stimulus value at that time kept as checks (criterion of fig4j-rheobase-increase).
- Exclusions (Methods): cells whose initial Rin exceeds 500 megaohms (the paper prints "mΩ"),
  initial meaning the first sweep (criterion of methods-slice-sample); sweeps with RMP above
  -50 mV or with no action potential.
"""

from __future__ import annotations

import hashlib
import re
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient

DANDISET_ID = "001354"
DANDISET_VERSION = "0.250312.0036"

RATE = 20000.0                     # Hz, as the files state; checked in the notebook
BASELINE = (0.0, 0.5)              # s, RMP window (Methods)
STEP = (0.5, 0.7)                  # s, -100 pA step (Methods, and the stored stimulus)
STEP_PA = -100.0
RIN_WINDOWS = {"last50": 0.050, "last100": 0.100}   # s before the end of the step (criterion)
RAMP = (1.1, 3.1)                  # s, nominal ramp from -150 to +500 pA (Methods; times from channel 1)
RAMP_PA = (-150.0, 500.0)
AP_RULES = ("A1", "A2")            # A1: upward crossing of 0 mV; A2: dV/dt above 20 V/s
DVDT_THRESHOLD = 20.0              # V/s, reading A2
RIN_MAX_MOHM = 500.0               # cell exclusion (Methods)
RMP_MAX_MV = -50.0                 # sweep exclusion (Methods)


def assets():
    """The dandiset's NWB assets at the pinned version, sorted by path."""
    client = DandiAPIClient()
    dandiset = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
    return sorted(dandiset.get_assets(), key=lambda a: a.path)


def _text(f, path):
    value = f[path][()]
    return value.decode() if isinstance(value, bytes) else value


def ramp_formula(t):
    """Current (pA) of the nominal ramp at time t (s) within a sweep."""
    return RAMP_PA[0] + (RAMP_PA[1] - RAMP_PA[0]) * (t - RAMP[0]) / (RAMP[1] - RAMP[0])


def first_ap(v_mv, rule):
    """Index (within the ramp) of the first action potential under a detection rule, or None."""
    if rule == "A1":
        idx = np.flatnonzero((v_mv[1:] >= 0.0) & (v_mv[:-1] < 0.0))
        return int(idx[0]) + 1 if idx.size else None
    dvdt = np.diff(v_mv) * RATE / 1000.0          # V/s
    idx = np.flatnonzero(dvdt > DVDT_THRESHOLD)
    return int(idx[0]) + 1 if idx.size else None


def count_aps(v_mv, rule):
    """Number of action potentials in the ramp under a rule (events separated by 2 ms)."""
    if rule == "A1":
        return int(np.sum((v_mv[1:] >= 0.0) & (v_mv[:-1] < 0.0)))
    dvdt = np.diff(v_mv) * RATE / 1000.0
    idx = np.flatnonzero(dvdt > DVDT_THRESHOLD)
    if idx.size == 0:
        return 0
    return int(1 + np.sum(np.diff(idx) > 0.002 * RATE))


def sweep_measures(v_mv, i_pa, stim_pa):
    """Measures of one sweep: RMP, Rin under each window, and per rule the first AP and rheobase."""
    s = lambda t: int(round(t * RATE))
    rmp = float(v_mv[s(BASELINE[0]):s(BASELINE[1])].mean())
    out = {"rmp_mv": rmp,
           "i_baseline_pa": float(i_pa[s(BASELINE[0]):s(BASELINE[1])].mean()),
           "i_step_pa": float(i_pa[s(STEP[0]) + 200:s(STEP[1]) - 200].mean()),
           "i_pre_ramp_pa": float(i_pa[s(RAMP[0] - 0.09):s(RAMP[0] - 0.01)].mean()),
           "i_gap_pa": float(i_pa[s(STEP[1] + 0.01):s(RAMP[0] - 0.11)].mean())}
    for name, width in RIN_WINDOWS.items():
        vss = float(v_mv[s(STEP[1] - width):s(STEP[1])].mean())
        out[f"rin_{name}_mohm"] = (vss - rmp) / STEP_PA * 1000.0   # mV / pA = GOhm; x1000 = MOhm
    # the delivered ramp, from channel 1: it starts at 1.1 s and ends where the current falls back
    # from its peak; its slope is a straight-line fit from 1.15 s to 50 ms before the end
    r0 = s(RAMP[0])
    late = i_pa[r0:s(RAMP[1] + 0.1)]
    r1 = r0 + int(np.argmax(late)) + 1
    tt = np.arange(r0 + s(0.05), r1 - s(0.05)) / RATE
    slope, intercept = np.polyfit(tt, i_pa[r0 + s(0.05):r1 - s(0.05)], 1)
    out["ramp_end_s"] = r1 / RATE
    out["ramp_peak_pa"] = float(late.max())
    out["ramp_slope_pa_s"] = float(slope)
    out["ramp_start_pa"] = float(intercept + slope * RAMP[0])
    out["stim_mid_ramp_pa"] = float(stim_pa[s(2.1)])
    vr = v_mv[r0:r1]
    for rule in AP_RULES:
        k = first_ap(vr, rule)
        out[f"n_ap_{rule}"] = count_aps(vr, rule)
        if k is None:
            out[f"t_ap_{rule}"] = np.nan
            out[f"rheo_{rule}_pa"] = np.nan
            out[f"rheo_formula_{rule}_pa"] = np.nan
            out[f"rheo_fit_{rule}_pa"] = np.nan
            out[f"rheo_stored_{rule}_pa"] = np.nan
        else:
            t = RAMP[0] + k / RATE
            out[f"t_ap_{rule}"] = t
            out[f"rheo_{rule}_pa"] = float(i_pa[r0 + k])
            out[f"rheo_formula_{rule}_pa"] = float(ramp_formula(t))
            out[f"rheo_fit_{rule}_pa"] = float(intercept + slope * t)
            out[f"rheo_stored_{rule}_pa"] = float(stim_pa[r0 + k])
        # peak voltage in the 3 ms after the first event, to tell an action potential from noise
        out[f"peak_{rule}_mv"] = np.nan if k is None else float(vr[k:k + s(0.003)].max())
    # timing check: the voltage drop at the step onset, and the current monitor's step onset
    out["dv_step_onset_mv"] = float(v_mv[s(STEP[0]) + 40:s(STEP[0]) + 100].mean()
                                    - v_mv[s(STEP[0]) - 60:s(STEP[0])].mean())
    out["dv_before_onset_mv"] = float(v_mv[s(STEP[0]) - 100:s(STEP[0]) - 40].mean()
                                      - v_mv[s(STEP[0]) - 160:s(STEP[0]) - 100].mean())
    di = np.diff(i_pa[s(STEP[0]) - 100:s(STEP[0]) + 100])
    out["i_step_onset_s"] = STEP[0] - 100 / RATE + (int(np.argmin(di)) + 1) / RATE
    return out


def _sweep_pattern(name):
    """A path with its sweep number replaced by NN, so that every sweep's series reads the same."""
    return re.sub(r"-\d+-ch-", "-NN-ch-", name)


def file_text(f):
    """Every text value in the file, and every path in it, with sweep numbers replaced by NN.

    Visits every group and dataset (the namespace specifications excepted): all attributes of every
    sweep's series, every string dataset of any length (the text columns of the icephys tables
    included), and /intervals, /analysis and /processing where they exist. Used to look for a
    record of the condition, the drug onset, the mEGFP intensity or the preincubation time.
    Returns (sorted "path: value" strings, sorted paths).
    """
    found, paths = set(), set()

    def visit(name, obj):
        if name.startswith("specifications"):
            return
        name = _sweep_pattern(name)
        paths.add(name)
        for k, v in obj.attrs.items():
            if k in ("namespace", "neurodata_type", "object_id"):
                continue
            if isinstance(v, (str, bytes)):
                vals = [v]
            elif isinstance(v, np.ndarray) and v.dtype.kind in "OSU":
                vals = list(v.ravel())
            else:
                continue
            found.update(f"{name}@{k}: {x.decode() if isinstance(x, bytes) else x}" for x in vals)
        if isinstance(obj, h5py.Dataset) and (obj.dtype.kind in "SU"
                                              or h5py.check_string_dtype(obj.dtype) is not None):
            found.update(f"{name}: {x.decode() if isinstance(x, bytes) else x}"
                         for x in np.atleast_1d(obj[()]))

    visit("", f)
    f.visititems(visit)
    return sorted(found), sorted(paths)


def interpolation_residual(raw, taps=8):
    """How well each half of a sweep's samples is predicted from the other half, in ADC counts.

    Odd samples are fitted by least squares on the `taps` even samples on each side, and even
    samples on the odd ones. Data upsampled from 10 kHz by any linear interpolator that keeps the
    original samples give one residual near the rounding error (about 0.3 counts); data sampled
    at 20 kHz with content above 5 kHz give two similar, larger residuals. A data check, not used
    in any measure.
    """
    x = raw.astype(float)
    out = []
    for phase in (1, 0):
        idx = np.arange(2 * taps + phase, len(x) - 2 * taps, 2)
        X = np.column_stack([x[idx + o] for o in range(-2 * taps + 1, 2 * taps, 2)] + [np.ones(len(idx))])
        beta = np.linalg.lstsq(X, x[idx], rcond=None)[0]
        out.append(float(np.std(x[idx] - X @ beta)))
    return out


def load_cell(asset):
    """Stream one file and return (cell metadata, per-sweep DataFrame)."""
    url = asset.get_content_url(follow_redirects=1, strip_query=True)
    with h5py.File(remfile.File(url), "r") as f:
        acq, stim = f["acquisition"], f["stimulus/presentation"]
        sweeps = sorted({k.split("-")[2] for k in acq}, key=int)
        meta = {
            "path": asset.path,
            "subject": _text(f, "general/subject/subject_id"),
            "sex": _text(f, "general/subject/sex"),
            "date_of_birth": _text(f, "general/subject/date_of_birth")[:10],
            "session_start": _text(f, "session_start_time")[:19],
            "cell_id": _text(f, "general/DandiIcephysMetadata/cell_id"),
            "slice_id": _text(f, "general/DandiIcephysMetadata/slice_id"),
            "targeted_layer": _text(f, "general/DandiIcephysMetadata/targeted_layer"),
            "n_sweeps": len(sweeps),
        }
        g0 = acq[f"current_clamp-response-{sweeps[0]}-ch-0"]
        g1 = acq[f"current_clamp-response-{sweeps[0]}-ch-1"]
        meta.update({
            "rate_hz": float(g0["starting_time"].attrs["rate"]),
            "n_samples": int(g0["data"].shape[0]),
            "ch0_unit": g0["data"].attrs["unit"], "ch1_unit": g1["data"].attrs["unit"],
            "ch0_conversion": float(g0["data"].attrs["conversion"]),
            "ch1_conversion": float(g1["data"].attrs["conversion"]),
            "stim_unit": stim[f"stimulus-{sweeps[0]}-ch-0"]["data"].attrs["unit"],
            "stim_description": g0.attrs["description"],
        })
        meta["text"], meta["paths"] = file_text(f)
        rows = []
        for n, sw in enumerate(sweeps):
            d0 = acq[f"current_clamp-response-{sw}-ch-0"]
            d1 = acq[f"current_clamp-response-{sw}-ch-1"]
            ds = stim[f"stimulus-{sw}-ch-0"]
            raw = d0["data"][:]
            v_mv = raw * float(d0["data"].attrs["conversion"]) * 1000.0
            i_pa = d1["data"][:] * float(d1["data"].attrs["conversion"]) * 1e12
            stim_pa = ds["data"][:] * float(ds["data"].attrs["conversion"]) * 1e12
            row = {"sweep": n, "t_start_s": float(d0["starting_time"][()])}
            row.update(sweep_measures(v_mv, i_pa, stim_pa))
            if n == 0:
                meta["hash_first_sweep"] = hashlib.sha1(raw.tobytes()).hexdigest()[:16]
                meta["stim_levels_pa"] = sorted(set(np.round(np.unique(stim_pa), 1)))
                meta["pairs_identical"] = float(np.mean(raw[0::2] == raw[1::2]))
                meta["pairs_identical_shift"] = float(np.mean(raw[1:-1:2] == raw[2::2]))
                meta["interp_resid_odd"], meta["interp_resid_even"] = interpolation_residual(raw)
            rows.append(row)
    df = pd.DataFrame(rows)
    df.insert(0, "cell_id", meta["cell_id"])
    df.insert(1, "subject", meta["subject"])
    return meta, df


def load_all(workers=4):
    """Load every cell; returns (cells DataFrame, sweeps DataFrame)."""
    with ThreadPoolExecutor(workers) as ex:
        results = list(ex.map(load_cell, assets()))
    cells = pd.DataFrame([m for m, _ in results])
    sweeps = pd.concat([d for _, d in results], ignore_index=True)
    return cells, sweeps


def apply_exclusions(cells, sweeps, rin_window, rule):
    """The paper's exclusions under one Rin window and one AP rule.

    Returns the cells table with `rin_first_mohm` and `cell_kept`, and the sweeps table with
    `sweep_kept` (cell kept, RMP at or below -50 mV, and an action potential in the ramp).
    """
    first = sweeps[sweeps.sweep == 0].set_index("cell_id")[f"rin_{rin_window}_mohm"]
    cells = cells.copy()
    cells["rin_first_mohm"] = cells.cell_id.map(first)
    cells["cell_kept"] = cells.rin_first_mohm <= RIN_MAX_MOHM
    kept_cells = set(cells.cell_id[cells.cell_kept])
    sweeps = sweeps.copy()
    sweeps["sweep_kept"] = (sweeps.cell_id.isin(kept_cells) & (sweeps.rmp_mv <= RMP_MAX_MV)
                            & sweeps[f"t_ap_{rule}"].notna())
    return cells, sweeps
