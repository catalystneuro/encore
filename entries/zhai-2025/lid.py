"""Loading and measures for dandiset 001538 (Zhai et al. 2025, Science Advances).

Zhai S, Cui Q, Wokosin D, Sun L, Tkatch T, Crittenden JR, Graybiel AM, Surmeier DJ (2025).
State-dependent modulation of spiny projection neurons controls levodopa-induced dyskinesia in a
mouse model of Parkinson's disease. Sci Adv 11:eadv8224. doi:10.1126/sciadv.adv8224.

The dandiset holds, among others, these kinds of NWB file, all streamed from the archive at the
pinned version (nothing is written to disk):

- patch-clamp files (`*_icephys+ophys.nwb`, `*_icephys.nwb`), one per mouse and day: somatic
  current steps (`CurrentClampSeries_CellN_Somatic`, 21 sweeps of 1 s from -120 to +300 pA) and,
  for most, the dendritic back-propagation assay (`CurrentClampSeries_CellN_Dendritic`, 4 s sweeps
  with three brief current injections) with two-photon line scans of Alexa 568 (red, channel 1) and
  Fluo-4 (green, channel 2) at proximal and distal dendritic sites;
- Sr2+-oEPSC files (`*_icephys+ogen.nwb`), one cell each, 10 voltage-clamp sweeps;
- GRAB-ACh3.0 imaging files (`*_ophys.nwb`), one slice region per mouse, with Prairie View region
  traces per trial and treatment, and ACh and TTX calibration trials;
- AIM score tables (`ses-pan++ON...` files without `_image`), one file per mouse and session.

Where the parameters come from:

- Somatic excitability follows the paper's script (Zenodo doi:10.5281/zenodo.14145776,
  "Input_output analysis--ver2024.11.ipynb"): action potentials are upward crossings of 0 mV over
  the whole sweep; the rheobase is the first current step with at least one action potential.
- The dendritic excitability index follows the Methods and the paper's script (Zenodo
  doi:10.5281/zenodo.14163502, "PVAnalysis-ver 2024.11.ipynb"): PMT background subtracted (the
  script's constants, 55 for the red and 161 for the green channel; the files carry no per-session
  background), a 6-sample running mean, the three trials of a site averaged, R0 and G0 the means
  from 0.5 to 0.95 s, and the area of (G - G0)/R0 from 0.95 to 1.5 s; the index is the distal area
  over the proximal area. The Methods keep only pairs "with similar baseline levels (G0/R0)" and
  give no threshold; `BASAL_RATIO_RANGE` is a choice made here. Splitting the three series that
  hold two sites under one name (see `dendritic_sites`) is a choice made here from the data.
- Sr2+-oEPSC events: the Methods detect events 40 to 400 ms after the light pulse at five standard
  deviations above the noise (TaroTools in Igor Pro, with visual verification, which cannot be
  repeated). `detect_events` is a common threshold detector written here: low-pass filter, noise
  as the robust standard deviation of the trace outside the detection window, and the local
  baseline just before each event.
- GRAB-ACh follows the Methods and the paper's script (Zenodo doi:10.5281/zenodo.14163731,
  "PVAnalysis-BOT for GRAB Ver 2024.11.ipynb"): PMT background subtracted (the script's 162, and a
  variant from the file's zero-laser reference images), the two repetitions averaged, F0 the mean of
  the 1 s before stimulation, the area of (F - F0)/(Fmax - Fmin) over the 2 s after it, Fmax and
  Fmin the means from 2 to 4 s of the ACh and TTX calibration trials.
"""

from __future__ import annotations

import hashlib
import io
import re
import urllib.request
import zipfile
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy.signal import butter, sosfiltfilt

DANDISET_ID = "001538"
DANDISET_VERSION = "0.260527.1302"

# The paper's per-cell and per-animal tables ("Zhai et al. 2025 Datasets", Zenodo record 17307059,
# doi:10.5281/zenodo.17307059, the version the paper's key resources table resolves to).
TIDY_URL = ("https://zenodo.org/api/records/17307059/files/"
            "Zhai%20et%20al.%202025%20Datasets.zip/content")

STEP_CURRENTS = [-120, -100, -80, -60, -40, -20] + list(range(20, 301, 20))
DEND_BG_RED, DEND_BG_GREEN = 55.0, 161.0     # the dendritic script's PMT backgrounds
DEND_SMOOTH = 6
DEND_BASE = (0.5, 0.95)                      # s, R0 and G0
DEND_AREA = (0.95, 1.5)                      # s, area of dG/R0
BASAL_RATIO_RANGE = (0.5, 2.0)               # choice made here: (G0/R0 distal)/(G0/R0 proximal)
SR_WINDOW = (0.040, 0.400)                   # s after the light pulse (Methods)
SR_THRESHOLD_SD = 5.0                        # Methods
SR_LOWPASS_HZ = 1000.0                       # choice made here
GRAB_BG = 162.0                              # the GRAB script's PMT background
GRAB_BASE_S, GRAB_AREA_S = 1.0, 2.0          # s before and after the stimulus
GRAB_CAL = (2.0, 4.0)                        # s, window of the calibration trials


def asset_urls() -> list[tuple[str, str]]:
    """(path, streaming URL) of every NWB file at the pinned version."""
    with DandiAPIClient() as client:
        dandiset = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        return sorted((a.path, a.get_content_url(follow_redirects=1, strip_query=True))
                      for a in dandiset.get_assets() if a.path.endswith(".nwb"))


def parse_session(path: str) -> dict:
    """The fields of a session name: cell type, state, drug, genotype and the rest."""
    ses = path.split("_ses-", 1)[1][:-4]
    head, _, kind = ses.rpartition("_") if ses.endswith(("_icephys", "_icephys+ophys", "_icephys+ogen",
                                                          "_ophys", "_image")) else (ses, "", "")
    parts = head.split("++")
    return {"cell_type": parts[0], "state": parts[1], "drug": parts[2], "genotype": parts[3],
            "date": parts[4], "kind": kind}


def _text(x) -> str:
    x = x[()] if hasattr(x, "shape") else x
    return x.decode() if isinstance(x, bytes) else str(x)


def _strings(ds) -> list[str]:
    return [v.decode() if isinstance(v, bytes) else str(v) for v in ds[:]]


def _spike_count(v: np.ndarray, threshold: float = 0.0) -> int:
    above = v > threshold
    return int(np.sum(above[1:] & ~above[:-1]) + int(above[0]))


def _smooth(x: np.ndarray, n: int) -> np.ndarray:
    """pandas rolling(n).mean(): NaN for the first n-1 samples."""
    out = np.full(len(x), np.nan)
    c = np.cumsum(np.insert(x.astype(float), 0, 0.0))
    out[n - 1:] = (c[n:] - c[:-n]) / n
    return out


# ---------------------------------------------------------------- patch-clamp files

def load_patch(path: str, url: str) -> dict:
    """One mouse-day: per cell, the somatic current steps (spike counts) and the dendritic sweeps.

    Sweeps are found through the file's RecordingsIndexTable, which gives per sweep the cell,
    compartment, commanded current and slices into the concatenated series.
    """
    out = {"path": path, **parse_session(path), "somatic": [], "dendritic": []}
    with h5py.File(remfile.File(url), "r") as f:
        out["subject_id"] = _text(f["general/subject/subject_id"])
        out["subject_genotype"] = _text(f["general/subject/genotype"]) if "genotype" in f["general/subject"] else ""
        out["subject_description"] = _text(f["general/subject/description"])
        out["session_description"] = _text(f["session_description"])
        t = f["processing/recordings_index/RecordingsIndexTable"]
        ir = f["general/intracellular_ephys/intracellular_recordings"]
        cell = t["cell_id"][:]
        comp = _strings(t["dendrite_type"])
        cond = _strings(t["condition_subfolder"])
        current = t["stimulus_current_pA"][:]
        resp = ir["responses/response"][:]
        stim = ir["stimuli/stimulus"][:]
        cache: dict[str, np.ndarray] = {}

        def series(ref):
            name = f[ref].name
            if name not in cache:
                cache[name] = f[ref]["data"][:]
            return cache[name], f[ref]["starting_time"].attrs["rate"]

        for c in sorted(set(cell)):
            for cd in sorted({cond[i] for i in range(len(cell)) if cell[i] == c and comp[i] == "Soma"}):
                rows = [i for i in range(len(cell)) if cell[i] == c and comp[i] == "Soma" and cond[i] == cd]
                counts, counts_last, vrest, duplicates, in_step, out_step, stim_err = {}, {}, [], 0, 0, 0, []
                digest = hashlib.md5()
                for i in rows:
                    data, rate = series(resp[i]["timeseries"])
                    v = data[resp[i]["idx_start"]:resp[i]["idx_start"] + resp[i]["count"]] * 1e3
                    amp = int(round(current[i]))
                    counts_last[amp] = _spike_count(v)
                    if amp in counts:          # a repeated step: keep the first (counts_last keeps the last)
                        duplicates += 1
                        continue
                    counts[amp] = _spike_count(v)
                    sd, srate = series(stim[i]["timeseries"])
                    sv = sd[stim[i]["idx_start"]:stim[i]["idx_start"] + stim[i]["count"]] * 1e12
                    stim_err.append(abs(np.median(sv[int(0.25 * srate):int(0.65 * srate)]) - current[i]))
                    digest.update(np.ascontiguousarray(v).tobytes())
                    vrest.append(np.median(v[: int(0.15 * rate)]))
                    above = v > 0
                    up = np.where(above[1:] & ~above[:-1])[0] / rate
                    in_step += int(np.sum((up >= 0.2) & (up < 0.7)))
                    out_step += int(np.sum((up < 0.2) | (up >= 0.7)))
                out["somatic"].append({"cell": int(c), "condition": cd, "counts": counts, "counts_last": counts_last,
                                       "n_sweeps": len(rows),
                                       "duplicates": duplicates, "vrest_mV": float(np.median(vrest)),
                                       "md5": digest.hexdigest(), "stim_error_pA": float(np.max(stim_err)),
                                       "spikes_in_step": in_step, "spikes_outside_step": out_step,
                                       "sweep_samples": int(resp[rows[0]]["count"]), "rate": float(rate)})
            drows = [i for i in range(len(cell)) if cell[i] == c and comp[i] != "Soma"]
            for i in drows:
                data, rate = series(resp[i]["timeseries"])
                v = data[resp[i]["idx_start"]:resp[i]["idx_start"] + resp[i]["count"]] * 1e3
                above = v > 0
                spikes = np.where(above[1:] & ~above[:-1])[0] / rate
                sd, _ = series(stim[i]["timeseries"])
                sv = sd[stim[i]["idx_start"]:stim[i]["idx_start"] + stim[i]["count"]]
                rec = {"cell": int(c), "compartment": comp[i], "condition": cond[i], "spike_times": spikes,
                       "stim_max_abs_A": float(np.max(np.abs(sv))) if len(sv) else np.nan,
                       "md5": hashlib.md5(np.ascontiguousarray(v).tobytes()).hexdigest()}
                for ch in ("1", "2"):
                    a, n, ref = t[f"roi_response_ch{ch}"][i]
                    d, r = series(ref)
                    rec[f"ch{ch}"] = d[a:a + n].astype(float).ravel()
                    rec[f"ch{ch}_rate"] = float(r)
                    rec[f"ch{ch}_series"] = f[ref].name.split("/")[-1]
                    la, ln, lref = t[f"line_scan_ch{ch}"][i]
                    rec[f"ls{ch}_ok"] = bool(la >= 0 and la + ln <= f[lref]["data"].shape[0])
                out["dendritic"].append(rec)
    return out


# Groups by cell type and the file's condition_subfolder, with the paper's figure, sheet and group.
GROUPS = {
    ("dSPN", "LID off-state"): "dSPN off", ("dSPN", "LID on-state"): "dSPN on",
    ("dSPN", "LID on-state with SCH"): "dSPN on+SCH",
    ("iSPN", "LID off-state"): "iSPN off", ("iSPN", "LID on-state"): "iSPN on",
    ("iSPN", "LID on-state with sul (iSPN)"): "iSPN on+sul", ("iSPN", "LID on-state with sul"): "iSPN on+sul",
    ("iSPN", "control"): "Fig6 vehicle", ("iSPN", "M1R antagonist"): "Fig6 M1R antagonist",
    ("iSPN", "KO off-state"): "KO off", ("iSPN", "KO on-state"): "KO on",
    ("iSPN", "interleaved control"): "Fig9 control", ("iSPN", "M1R CRISPR"): "Fig9 M1R CRISPR",
}
TIDY_SOMATIC = {
    "dSPN off": ("Fig 1", "Fig 1E_dSPN somatic excitabilit", "LID off"),
    "dSPN on": ("Fig 1", "Fig 1E_dSPN somatic excitabilit", "LID on"),
    "dSPN on+SCH": ("Fig 1", "Fig 1E_dSPN somatic excitabilit", "LID on + SCH"),
    "iSPN off": ("Fig 3", "Fig 3C_iSPN somatic excitabilit", "LID off"),
    "iSPN on": ("Fig 3", "Fig 3C_iSPN somatic excitabilit", "LID on"),
    "iSPN on+sul": ("Fig 3", "Fig 3C_iSPN somatic excitabilit", "LID on + sul"),
    "Fig6 vehicle": ("Fig 6", "Fig 6C_M1R antagonist SE", "control"),
    "Fig6 M1R antagonist": ("Fig 6", "Fig 6C_M1R antagonist SE", "M1R antagonist"),
    "KO off": ("Fig 7", "Fig 7C_KO somatic excitability", "KO off"),
    "KO on": ("Fig 7", "Fig 7C_KO somatic excitability", "KO on"),
    "Fig9 control": ("Fig 9", "Fig 9D_M1R CRISPR SE", "control"),
    "Fig9 M1R CRISPR": ("Fig 9", "Fig 9D_M1R CRISPR SE", '"M1R"'),
}
TIDY_DENDRITIC = {
    "dSPN off": ("Fig 1", "Fig 1I_dSPN dendritic excitabil", "LID off"),
    "dSPN on": ("Fig 1", "Fig 1I_dSPN dendritic excitabil", "LID on"),
    "dSPN on+SCH": ("Fig 1", "Fig 1I_dSPN dendritic excitabil", "LID on + SCH"),
    "iSPN off": ("Fig 3", "Fig 3F_iSPN dendritic excitabil", "LID off"),
    "iSPN on": ("Fig 3", "Fig 3F_iSPN dendritic excitabil", "LID on"),
    "iSPN on+sul": ("Fig 3", "Fig 3F_iSPN dendritic excitabil", "LID on + sul"),
    "Fig6 vehicle": ("Fig 6", "Fig 6D_M1R antagonist DE", "control"),
    "Fig6 M1R antagonist": ("Fig 6", "Fig 6D_M1R antagonist DE", "M1R antagonist"),
    "KO off": ("Fig 7", "Fig 7F_KO dendritic excitabilit", "KO|LID off"),
    "KO on": ("Fig 7", "Fig 7F_KO dendritic excitabilit", "KO|LID on"),
}


def tidy_group(tidy: dict, spec: tuple) -> pd.DataFrame:
    """The rows of one group of a paper sheet; the last column is the value."""
    fig, sheet, group = spec
    x = tidy[fig][sheet].copy()
    x.columns = [str(c).strip() for c in x.columns]
    if "|" in group:
        gt, state = group.split("|")
        return x[(x["Genotype"].astype(str).str.strip() == gt) & (x["LID state"].astype(str).str.strip() == state)]
    col = [c for c in x.columns if c.lower() == "group"][0]
    return x[x[col].astype(str).str.strip() == group]


def load_subject(path: str, url: str) -> dict:
    with h5py.File(remfile.File(url), "r") as f:
        s = f["general/subject"]
        return {"path": path, **{k: _text(s[k]) for k in s if isinstance(s[k], h5py.Dataset)},
                "session_description": _text(f["session_description"])}


def rheobase(counts: dict[int, int]) -> float:
    """First positive step with at least one action potential (pA); NaN if none."""
    for i in sorted(k for k in counts if k > 0):
        if counts[i] >= 1:
            return float(i)
    return np.nan


def somatic_table(days: list[dict]) -> pd.DataFrame:
    """One row per cell and condition: the spike count at each step from 20 to 300 pA (NaN where the
    step is missing), the rheobase, and the identifiers. `condition` is the file's
    condition_subfolder, which, unlike the session name, tells drug from baseline sweeps."""
    rows = []
    for d in days:
        for s in d["somatic"]:
            row = {"path": d["path"], "date": d["date"], "group": GROUPS.get((d["cell_type"], s["condition"]), "?"), "subject_id": d["subject_id"], "cell_type": d["cell_type"],
                   "session_state": d["state"], "session_drug": d["drug"], "genotype": d["genotype"],
                   "cell": s["cell"], "condition": s["condition"], "n_sweeps": s["n_sweeps"],
                   "duplicates": s["duplicates"], "vrest_mV": s["vrest_mV"], "rheobase": rheobase(s["counts"]),
                   "spikes_in_step": s["spikes_in_step"], "spikes_outside_step": s["spikes_outside_step"],
                   "md5": s["md5"], "stim_error_pA": s["stim_error_pA"],
                   "counts_last": [s["counts_last"].get(a, np.nan) for a in range(20, 301, 20)]}
            for amp in range(20, 301, 20):
                row[amp] = s["counts"].get(amp, np.nan)
            rows.append(row)
    return pd.DataFrame(rows)


def _site_measures(recs: list, bg_red: float, bg_green: float) -> dict:
    """R0, G0 and the area of dG/R0 of the trials of one site, averaged after background
    subtraction and smoothing, as in the paper's script."""
    n = min(min(len(r["ch1"]), len(r["ch2"])) for r in recs)
    red = np.nanmean([_smooth(r["ch1"][:n] - bg_red, DEND_SMOOTH) for r in recs], axis=0)
    green = np.nanmean([_smooth(r["ch2"][:n] - bg_green, DEND_SMOOTH) for r in recs], axis=0)
    rate = recs[0]["ch2_rate"]
    dt = 1.0 / rate
    a, b = int(DEND_BASE[0] / dt), int(DEND_BASE[1] / dt)
    c, d = b, int(DEND_AREA[1] / dt)
    r0, g0 = np.nanmean(red[a:b]), np.nanmean(green[a:b])
    # contrast for the clock check: the same window shifted 1.5 s later, after the transient
    late = np.nansum((green[c + int(1.5 / dt):d + int(1.5 / dt)] - g0) / r0) * dt
    return {"n_trials": len(recs), "R0": r0, "G0": g0, "area": np.nansum((green[c:d] - g0) / r0) * dt,
            "late_area": late, "rate": rate,
            "first_spike_s": float(np.median([r["spike_times"][0] if len(r["spike_times"]) else np.nan for r in recs])),
            "n_spikes": float(np.median([len(r["spike_times"]) for r in recs]))}


def dendritic_sites(day: dict, bg_red: float = DEND_BG_RED, bg_green: float = DEND_BG_GREEN,
                    split_merged: bool = True) -> pd.DataFrame:
    """Per dendritic site (cell, compartment, site series): R0, G0 and the area of dG/R0.

    Time is the sample index over the series' rate. A site is recorded in three trials. Three
    series hold six trials under one name while the cell has no series of the other compartment
    with that number; their first and last three trials differ in baseline and area, so each holds
    two sites. With `split_merged` such a series is split into its first and last three trials,
    and the half with the smaller area is taken as the distal site (bAP-evoked Ca2+ signals fall
    with distance; an assumption made here, flagged in the column `split`).
    """
    rows = []
    groups: dict[tuple, list] = {}
    for rec in day["dendritic"]:
        key = (rec["cell"], rec["compartment"], rec["ch2_series"], rec["condition"])
        groups.setdefault(key, []).append(rec)
    for (cell, comp, name, cond), recs in groups.items():
        m = re.search(r"(Proximal|Distal)(\d+)$", name)
        site = int(m.group(2)) if m else 0
        other = "Distal" if comp == "Proximal" else "Proximal"
        has_other = any(k[0] == cell and k[3] == cond and re.search(rf"{other}{site}$", k[2]) for k in groups)
        if split_merged and len(recs) == 6 and not has_other:
            halves = [_site_measures(recs[:3], bg_red, bg_green), _site_measures(recs[3:], bg_red, bg_green)]
            halves.sort(key=lambda h: h["area"])
            for comp_h, h in zip(("Distal", "Proximal"), halves):
                rows.append({"cell": cell, "compartment": comp_h, "site": site, "condition": cond,
                             "series": name, "split": True, **h})
        else:
            rows.append({"cell": cell, "compartment": comp, "site": site, "condition": cond,
                         "series": name, "split": False, **_site_measures(recs, bg_red, bg_green)})
    return pd.DataFrame(rows)


def dendritic_index(sites: pd.DataFrame, basal_range=BASAL_RATIO_RANGE) -> pd.DataFrame:
    """Per cell (and condition): distal area over proximal area, by site pairs of the same number.

    Sites are paired by their number (Proximal1 with Distal1); a cell's index is the mean over
    its pairs whose basal ratio (G0/R0 distal over G0/R0 proximal) is inside `basal_range`
    (pass None to keep every pair). Unpaired sites are counted as dropped.
    """
    rows = []
    for (cell, cond), g in sites.groupby(["cell", "condition"]):
        prox = g[g.compartment == "Proximal"].set_index("site")
        dist = g[g.compartment == "Distal"].set_index("site")
        pairs = sorted(set(prox.index) & set(dist.index))
        ratios, basal, kept = [], [], 0
        for s in pairs:
            br = (dist.G0[s] / dist.R0[s]) / (prox.G0[s] / prox.R0[s])
            basal.append(br)
            if basal_range is None or basal_range[0] <= br <= basal_range[1]:
                ratios.append(dist.area[s] / prox.area[s])
                kept += 1
        rows.append({"cell": cell, "condition": cond, "pairs": len(pairs), "pairs_kept": kept,
                     "unpaired_sites": len(set(prox.index) ^ set(dist.index)),
                     "sites": " ".join(f"{c[0]}{s}" for c, s in sorted(zip(g.compartment, g.site), key=lambda x: (x[1], x[0]))),
                     "split": bool(g.split.any()),
                     "basal_ratios": np.round(basal, 2).tolist(),
                     "index": float(np.mean(ratios)) if ratios else np.nan})
    return pd.DataFrame(rows)


# ---------------------------------------------------------------- Sr2+-oEPSC files

def load_sr(path: str, url: str) -> dict:
    """One cell: its sweeps (pA), the light-pulse onset per sweep, and identifiers."""
    out = {"path": path, **parse_session(path), "sweeps": []}
    with h5py.File(remfile.File(url), "r") as f:
        ir = f["general/intracellular_ephys/intracellular_recordings"]
        out["cell_number"] = sorted(set(_strings(ir["cell_number"])))
        out["session_letter"] = sorted(set(_strings(ir["session_letter"])))
        out["led"] = sorted(set(_strings(ir["led_intensity"])))
        ep = f["intervals/optogenetic_epochs_table"]
        stages = _strings(ep["stage_name"])
        out["epoch_stim_s"] = float(ep["start_time"][stages.index("stimulation")])
        out["epoch_detect"] = (float(ep["start_time"][stages.index("detection")]),
                               float(ep["stop_time"][stages.index("detection")]))
        vc = sorted(k for k in f["acquisition"] if k.startswith("VoltageClampSeries"))
        og = sorted(k for k in f["stimulus/presentation"] if k.startswith("OptogeneticSeries"))
        for k, o in zip(vc, og):
            g = f["acquisition"][k]
            i = g["data"][:] * 1e12
            led = f["stimulus/presentation"][o]["data"][:]
            orate = f["stimulus/presentation"][o]["starting_time"].attrs["rate"]
            on = np.where(led > 0)[0]
            out["sweeps"].append({"name": k, "current": i, "md5": hashlib.md5(i.tobytes()).hexdigest(), "rate": float(g["starting_time"].attrs["rate"]),
                                  "led_onset_s": float(on[0] / orate) if len(on) else np.nan,
                                  "led_trace_nonzero": bool(len(on))})
        out["n_vc"], out["n_og"] = len(vc), len(og)
    return out


def detect_events(i: np.ndarray, rate: float, onset: float, window=SR_WINDOW,
                  threshold_sd: float = SR_THRESHOLD_SD, lowpass: float = SR_LOWPASS_HZ) -> pd.DataFrame:
    """Inward (negative) events between onset+window[0] and onset+window[1].

    The trace is low-pass filtered; the noise is the robust SD (1.4826 x median absolute
    deviation) of the filtered trace outside 0 to 450 ms after the pulse; an event starts where
    the trace falls below the local baseline (median of the 5 ms before) by threshold_sd x noise;
    its amplitude is the baseline minus the minimum within 10 ms; events closer than 5 ms to the
    previous one are merged.
    """
    sos = butter(4, lowpass, fs=rate, output="sos")
    x = sosfiltfilt(sos, i - np.median(i))
    t = np.arange(len(x)) / rate
    quiet = (t < onset) | (t > onset + 0.45)
    noise = 1.4826 * np.median(np.abs(x[quiet] - np.median(x[quiet])))
    nb, nw, gap = int(0.005 * rate), int(0.010 * rate), int(0.005 * rate)
    a, b = int((onset + window[0]) * rate), int((onset + window[1]) * rate)
    events, k = [], a
    while k < b:
        base = np.median(x[max(k - nb, 0):k])
        if base - x[k] > threshold_sd * noise:
            seg = x[k:k + nw]
            j = k + int(np.argmin(seg))
            events.append({"t": t[k] - onset, "amp": float(base - x[j])})
            k = j + gap
        else:
            k += 1
    df = pd.DataFrame(events, columns=["t", "amp"])
    df.attrs["noise"] = float(noise)
    return df


# ---------------------------------------------------------------- GRAB-ACh files

def load_grab(path: str, url: str) -> dict:
    """One mouse: the region trace of every trial, its treatment and stimulus time, and the PMT
    background of the zero-laser reference images (16-bit, channel 2)."""
    out = {"path": path, **parse_session(path), "trials": []}
    with h5py.File(remfile.File(url), "r") as f:
        tr = f["intervals/trials"]
        flu = f["processing/ophys/Fluorescence"]
        refs = f["acquisition/ImagesBackgroundReferences"]
        bgs = [float(np.mean(refs[k][:])) for k in refs if "Ch216Bit" in k]
        out["bg_reference"] = float(np.median(bgs)) if bgs else np.nan
        out["n_regions"] = int(f["processing/ophys/ImageSegmentation/PlaneSegmentationGRABCh/id"].shape[0])
        out["frame_rate_2p"] = sorted({round(float(f["acquisition"][k]["starting_time"].attrs["rate"]), 3)
                                       for k in f["acquisition"] if k.startswith("TwoPhotonSeriesGRABCh")})
        for j in range(tr["id"].shape[0]):
            name = _text(tr["roi_series_name"][j])
            s = flu[name]
            out["trials"].append({
                "treatment": _text(tr["treatment"][j]), "stimulation": _text(tr["stimulation"][j]),
                "repetition": int(tr["repetition_number"][j]), "start": float(tr["start_time"][j]),
                "stop": float(tr["stop_time"][j]), "stim": float(tr["stimulus_start_time"][j]),
                "series_start": float(s["starting_time"][()]), "rate": float(s["starting_time"].attrs["rate"]),
                "trace": s["data"][:].astype(float).ravel()})
    return out


def grab_measures(m: dict, bg: float = GRAB_BG, fmin_rule: str = "ttx_or_quinpirole") -> pd.DataFrame:
    """Per treatment and stimulation: area of (F - F0)/(Fmax - Fmin) over 2 s after the stimulus,
    and the unnormalised area of dF/F0, from the mean of the repetitions."""
    cal = {}
    for kind in ("acetylcholine_calibration", "TTX_calibration"):
        trs = [t for t in m["trials"] if t["treatment"] == kind]
        if trs:
            vals = []
            for t in trs:
                tt = np.arange(len(t["trace"])) / t["rate"]
                vals.append(np.mean(t["trace"][(tt >= GRAB_CAL[0]) & (tt < GRAB_CAL[1])] - bg))
            cal[kind] = float(np.mean(vals))
    rows = []
    stims = {}
    for t in m["trials"]:
        if t["treatment"].endswith("calibration"):
            continue
        stims.setdefault((t["treatment"], t["stimulation"]), []).append(t)
    f0s = {}
    for (treat, stim), trs in stims.items():
        n = min(len(t["trace"]) for t in trs)
        rel = [t["stim"] - t["series_start"] for t in trs]
        rate = trs[0]["rate"]
        avg = np.mean([t["trace"][:n] - bg for t in trs], axis=0)
        k = int(round(np.mean(rel) * rate))
        f0 = avg[max(k - int(GRAB_BASE_S * rate), 0):k].mean()
        f0s[(treat, stim)] = f0
        rows.append({"treatment": treat, "stimulation": stim, "n_reps": len(trs), "stim_rel_s": float(np.mean(rel)),
                     "F0": f0, "avg": avg, "k": k, "rate": rate})
    fmax = cal.get("acetylcholine_calibration", np.nan)
    fmin_ttx = cal.get("TTX_calibration", np.nan)
    out = []
    for r in rows:
        quin = f0s.get(("quinpirole", r["stimulation"]), np.nan)
        fmin = np.nanmin([fmin_ttx, quin]) if fmin_rule == "ttx_or_quinpirole" else fmin_ttx
        k, rate, avg = r["k"], r["rate"], r["avg"]
        win = avg[k:k + int(GRAB_AREA_S * rate)]
        pre = avg[max(k - int(GRAB_AREA_S * rate), 0):k]
        dt = 1.0 / rate
        out.append({"treatment": r["treatment"], "stimulation": r["stimulation"], "n_reps": r["n_reps"],
                    "stim_rel_s": r["stim_rel_s"], "F0": r["F0"], "Fmax": fmax, "Fmin": fmin, "Fmin_ttx": fmin_ttx,
                    "auc_norm": float(np.sum(win - r["F0"]) * dt / (fmax - fmin)),
                    "auc_dff0": float(np.sum((win - r["F0"]) / r["F0"]) * dt),
                    "auc_norm_pre": float(np.sum(pre - r["F0"]) * dt / (fmax - fmin))})
    return pd.DataFrame(out)


# ---------------------------------------------------------------- AIM files

def load_aim(path: str, url: str) -> pd.DataFrame:
    with h5py.File(remfile.File(url), "r") as f:
        t = f["processing/behavior/DynamicTableAIMScore"]
        df = pd.DataFrame({k: (_strings(t[k]) if t[k].dtype.kind == "O" else t[k][:]) for k in t if k != "id"})
        df["subject_id"] = _text(f["general/subject/subject_id"])
        df["subject_genotype"] = _text(f["general/subject/genotype"])
        df["path"] = path
    return df


def file_contents(path: str, url: str) -> dict:
    """What a file holds outside its metadata: the acquisition objects with their types and
    number of members, and the names in processing and analysis."""
    with h5py.File(remfile.File(url), "r") as f:
        acq = {k: (_text(f["acquisition"][k].attrs.get("neurodata_type", "")), len(f["acquisition"][k]))
               for k in f.get("acquisition", {})}
        return {"path": path, "acquisition_types": sorted({t for t, _ in acq.values()}),
                "acquisition_objects": len(acq), "images": sum(n for _, n in acq.values()),
                "processing": sorted(f.get("processing", {})), "analysis": sorted(f.get("analysis", {}))}


def load_many(fn, items, workers: int = 8):
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(lambda pu: fn(*pu), items))


# ---------------------------------------------------------------- the paper's tables

def tidy_tables() -> dict[str, dict[str, pd.DataFrame]]:
    """Every sheet of the paper's per-cell tables, by workbook name ('Fig 1', ..., 'SupFigs')."""
    with urllib.request.urlopen(TIDY_URL) as r:
        z = zipfile.ZipFile(io.BytesIO(r.read()))
    out = {}
    for name in z.namelist():
        m = re.search(r"/(Fig \d+|SupFigs) datasets\.xlsx$", name)
        if m and "__MACOSX" not in name:
            out[m.group(1)] = pd.read_excel(io.BytesIO(z.read(name)), sheet_name=None)
    return out


def tidy_fi(sheet: pd.DataFrame) -> pd.DataFrame:
    """A somatic-excitability sheet as rows of spike counts by current (columns 0 to 300 pA)."""
    cols = {c: int(re.match(r"\s*(\d+)\s*pA", str(c)).group(1)) for c in sheet.columns if re.match(r"\s*\d+\s*pA", str(c))}
    out = sheet.rename(columns=cols)
    out.columns = [c if isinstance(c, int) else str(c).strip().lower() for c in out.columns]
    return out
