"""Loading and measures for Schiavo et al. (2020) and dandiset 000249.

Schiavo, Valtcheva, Bair-Marshall, Song, Martin & Froemke (2020), Nature 587, 426-431,
doi:10.1038/s41586-020-2807-6. Text read: the NIH author manuscript, PMC7677212.

Two sources are read, both streamed into memory; nothing is written to disk.

- Dandiset 000249 at version `DANDISET_VERSION` (DANDI REST API, NWB files over HTTP range
  requests with remfile and h5py). Each NWB file holds one raw two-photon movie
  (`acquisition/TwoPhotonSeries`, 256 x 256 pixels, uint16), the subject id, a session
  description naming the stimulus set, and an experiment description naming the group. No ROIs,
  fluorescence traces, stimulus times or trial tables are stored.
- The figshare collection the dandiset's metadata links (doi:10.6084/m9.figshare.c.5043830.v6),
  for the claims the claims file marks `data: elsewhere`: in vivo whole-cell recordings
  (articles 12611657 v3 and 12613496 v2), slice recordings (12611522 v1), oxytocin slice
  recordings (12613811 v1) and operant touch times (13056584 v1). Each article is read at the
  version in `FIGSHARE`.

Where the parameters come from:

- In vivo PSC magnitude (Methods, "In vivo whole-cell recordings"): "Synaptic responses were
  calculated as the PSC area (pA*ms) divided by the duration of the analysis window (ms); the
  baseline window was 1 second, and prototypical and morphed calls were analyzed from the start
  of the call to 250 ms following call offset. Absolute magnitudes (pA) from the largest 5-10
  evoked trials were used for analysis. Evoked synaptic responses were calculated by subtracting
  the baseline response from the stimulus response." Hence `BASELINE_S`, `POST_OFFSET_S` and
  `TOP_N` (5 and 10, both run, as the claims file asks). The baseline is the 1 s before call
  onset (the claims file's reading of "the 1 s baseline").
- Call onset, offset and ISI of each sweep are measured from the recorded microphone channel
  (`MIC`); the files carry no stimulus labels. Syllables are segments of the rectified
  microphone signal, smoothed over `MIC_SMOOTH_S`, above `MIC_THRESHOLD` of the way from the
  median to the peak, with gaps under `MIC_MERGE_S` merged. These are standard choices for
  finding a clean playback in a microphone trace; they cannot change a result as long as each
  sweep's ISI falls clearly into one bin, which the notebook shows. The ISI is the median silent
  gap between syllables, assigned to the nearest of `ISI_BINS` (the ISIs of the Fig. 2h,i and
  Extended Data Fig. 6e legends, which the claims file adopts).
- Holding potentials, stimulus sets and notes come from the spreadsheets in the figshare
  articles. Notes "stop @sweep N", "drop @sweep N" keep sweeps before N, "from sweep N" keeps
  sweeps from N; a note "drop" or "block + stop" drops the file (an assumption: the
  spreadsheets do not define them; `apply_notes=False` runs every sweep as a variant). Where a
  note names a cell's "best call", only that call's set is used (Methods: "five prototypical
  calls were played ... to determine the best call for each cell ... Prototypes were then played
  in conjunction with a set of temporal morphs"); pooling all sets is a variant.
- Operant touch times (claims file, fig1i-operant-prototypes): the MATLAB task code
  (KAMB_OperantTask_*.m, figshare 13054076 v1) appends to the csv the time (s, `toc`) of every
  polling sample at which the sensor reads a touch. A press is a run of samples; the gap that ends
  a press is either twice the session's median inter-sample interval or 100 ms (the two readings
  the claims file names). Duration is last minus first sample of the run.
- Slice short-term depression (Methods, "In vitro whole-cell recordings"): "The peak amplitude of
  evoked EPSCs and IPSCs were measured and normalized to the event evoked by the first
  stimulation on each trial (Sn/S1)". Peak search window and baseline: `SLICE_PEAK_WIN_S` after
  each stimulus artefact and `SLICE_BASE_S` before it, standard choices stated here.
"""

from __future__ import annotations

import builtins
import io
import os
import re
import threading
from concurrent.futures import ThreadPoolExecutor

import numpy as np
import pandas as pd
import requests
from scipy.ndimage import uniform_filter1d

DANDISET_ID = "000249"
DANDISET_VERSION = "0.230423.1416"
API = "https://api.dandiarchive.org/api"

# figshare articles and the versions read
FIGSHARE = {
    "invivo_ev": (12611657, 3),
    "invivo_nv": (12613496, 2),
    "slice": (12611522, 1),
    "oxytocin": (12613811, 1),
    "operant": (13056584, 1),
    "operant_code": (13054076, 1),
}
FIGSHARE_COLLECTION = (5043830, 6)

BASELINE_S = 1.0
POST_OFFSET_S = 0.25
TOP_N = (5, 10)
ISI_BINS = (125, 175, 275, 575)
MIC_SMOOTH_S = 0.002
MIC_THRESHOLD = 0.15
MIC_MERGE_S = 0.025

_session = requests.Session()


# ---------------------------------------------------------------- DANDI

def dandi_assets():
    """All assets of the pinned version: path, size, asset id."""
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/?page_size=1000"
    out = []
    while url:
        r = _session.get(url, timeout=60).json()
        out += r["results"]
        url = r["next"]
    return out


def dandi_version_metadata():
    return _session.get(f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/", timeout=60).json()


def _asset_meta(asset):
    m = _session.get(f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/"
                     f"{asset['asset_id']}/", timeout=60).json()
    gen = m["wasGeneratedBy"][0]
    return {"path": asset["path"], "asset_id": asset["asset_id"], "size": asset["size"],
            "sha256": m["digest"].get("dandi:sha2-256"), "session_description": gen.get("description"),
            "session_start": gen.get("startDate"), "subject": m["wasAttributedTo"][0]["identifier"],
            "s3": [u for u in m["contentUrl"] if "s3" in u][0]}


def asset_table(assets=None, threads=16):
    assets = assets if assets is not None else dandi_assets()
    with ThreadPoolExecutor(threads) as ex:
        return pd.DataFrame(list(ex.map(_asset_meta, assets)))


def _nwb_summary(row):
    import h5py
    import remfile
    with h5py.File(remfile.File(row["s3"]), "r") as f:
        ds = f["acquisition/TwoPhotonSeries/data"]
        out = {"path": row["path"],
               "groups": sorted(k for k in f.keys()),
               "acquisition": sorted(f["acquisition"].keys()),
               "processing": sorted(f["processing"].keys()) if "processing" in f else [],
               "stimulus": sorted(f["stimulus/presentation"].keys()) + sorted(f["stimulus/templates"].keys()),
               "intervals": sorted(f["intervals"].keys()) if "intervals" in f else [],
               "analysis": sorted(f["analysis"].keys()),
               "n_frames": ds.shape[0], "height": ds.shape[1], "width": ds.shape[2], "dtype": str(ds.dtype),
               "rate": float(f["acquisition/TwoPhotonSeries/starting_time"].attrs["rate"]),
               "imaging_rate": float(f["general/optophysiology/ImagingPlane/imaging_rate"][()]),
               "indicator": f["general/optophysiology/ImagingPlane/indicator"][()].decode(),
               "location": f["general/optophysiology/ImagingPlane/location"][()].decode(),
               "experiment_description": f["general/experiment_description"][()].decode(),
               "session_description_file": f["session_description"][()].decode(),
               "subject_id": f["general/subject/subject_id"][()].decode(),
               "genotype": f["general/subject/genotype"][()].decode(),
               "frame0_sum": int(ds[0].astype(np.int64).sum()),
               "frame_last_sum": int(ds[ds.shape[0] - 1].astype(np.int64).sum())}
    return out


def nwb_summaries(table, processes=32):
    """Structure, shapes and descriptive metadata of every NWB file (no movie data but two frames).
    h5py serializes calls within a process, so files are read in parallel processes."""
    from concurrent.futures import ProcessPoolExecutor
    rows = table.to_dict("records")
    with ProcessPoolExecutor(processes) as ex:
        return pd.DataFrame(list(ex.map(_nwb_summary, rows, chunksize=4)))


def movie_mean_trace(s3_url, crop=64):
    """Mean of the central crop x crop pixels of each frame of a movie."""
    import h5py
    import remfile
    with h5py.File(remfile.File(s3_url), "r") as f:
        ds = f["acquisition/TwoPhotonSeries/data"]
        h, w = ds.shape[1:]
        r0, c0 = (h - crop) // 2, (w - crop) // 2
        x = ds[:, r0:r0 + crop, c0:c0 + crop].astype(np.float64)
        rate = float(f["acquisition/TwoPhotonSeries/starting_time"].attrs["rate"])
    return x.mean(axis=(1, 2)), rate


def group_from_description(desc):
    """Experience group, indicator class and hemisphere from the NWB experiment description."""
    d = desc.lower()
    if "lactating" in d or "dam" in d.split("<")[0] and "virgin" not in d.split("<")[0]:
        group = "dam"
    elif "experienced" in d:
        group = "EV"
    elif "naive" in d or "naïve" in d:
        group = "NV"
    else:
        group = "unknown"
    if "halorhodopsin" in d or "synapsin" in d:
        cells = "pan-neuronal (opto-OT)"
    elif "inhibitory" in d or "interneuron" in d:
        cells = "inhibitory"
    elif "excitatory" in d:
        cells = "excitatory"
    else:
        cells = "unknown"
    hemi = "right" if "right" in d else ("left" if "left" in d else "not stated")
    cohoused = "cohoused" in d or "cohousing" in d
    return {"group": group, "cells": cells, "hemisphere": hemi, "cohoused": cohoused}


# ---------------------------------------------------------------- figshare

def figshare_article(article_id, version):
    return _session.get(f"https://api.figshare.com/v2/articles/{article_id}/versions/{version}",
                        timeout=60).json()


def figshare_files(key):
    aid, ver = FIGSHARE[key]
    art = figshare_article(aid, ver)
    return {f["name"]: f for f in art["files"]}, art


def fetch(url):
    """Bytes of a file, in memory."""
    r = _session.get(url, timeout=300)
    r.raise_for_status()
    return r.content


def read_sheet(key, name_contains=".xlsx"):
    files, _ = figshare_files(key)
    name = [n for n in files if name_contains in n and n.endswith(".xlsx")][0]
    return pd.read_excel(io.BytesIO(fetch(files[name]["download_url"])), sheet_name=0, header=None), name


def _fromfile(fb, dtype, count=-1):
    dt = np.dtype(dtype)
    return np.frombuffer(fb.read(count * dt.itemsize), dtype=dt).copy()


_ABF_LOCK = threading.Lock()


def abf_from_bytes(b, name):
    """Open an ABF file held in memory with pyabf, which otherwise reads only from a path."""
    with _ABF_LOCK:
        return _abf_from_bytes(b, name)


def _abf_from_bytes(b, name):
    import pyabf
    import pyabf.abf as _m
    real_exists, real_ff = os.path.exists, np.fromfile

    def fake_open(p, *a, **k):
        if str(p).endswith(name):
            return io.BytesIO(b)
        return builtins.open(p, *a, **k)
    _m.open = fake_open
    np.fromfile = _fromfile
    os.path.exists = lambda p: True if str(p).endswith(name) else real_exists(p)
    try:
        return pyabf.ABF(name, cacheStimulusFiles=False)
    finally:
        del _m.open
        os.path.exists = real_exists
        np.fromfile = real_ff


# ---------------------------------------------------------------- in vivo whole-cell

def syllables(mic, fs):
    """Onsets and offsets (s) of the syllables in a microphone sweep."""
    env = uniform_filter1d(np.abs(mic), max(1, int(MIC_SMOOTH_S * fs)))
    noise = np.median(env)
    on = env > noise + MIC_THRESHOLD * (env.max() - noise)
    d = np.diff(np.r_[0, on.astype(int), 0])
    s, e = np.flatnonzero(d == 1), np.flatnonzero(d == -1)
    S, E = [], []
    for a, b in zip(s, e):
        if S and a - E[-1] < MIC_MERGE_S * fs:
            E[-1] = b
        else:
            S.append(a)
            E.append(b)
    S, E = np.array(S, float), np.array(E, float)
    keep = (E - S) > 0.005 * fs
    return S[keep] / fs, E[keep] / fs


def assign_isi_by_duration(df):
    """ISI bin of each sweep of a morph-set file from the rank of its call duration.

    A set holds the prototype and morphs made by adding or removing the same time between
    syllables (Methods, "Stimulus library"), so call duration ranks the ISIs. When a file holds
    four distinct durations (gaps of more than 50 ms between them), the shortest is 125 ms, then
    175, 275 and 575 ms (`isi`); the ISI from the measured gap alone is kept as `isi_gap`."""
    df = df.copy()
    df["isi_gap"] = df.get("isi")
    if "onset" not in df or df.onset.isna().all():
        return df
    dur = (df.offset - df.onset).round(3)
    u = np.sort(dur.dropna().unique())
    if len(u) == 0:
        return df
    groups = np.split(u, np.flatnonzero(np.diff(u) > 0.05) + 1)
    if len(groups) == len(ISI_BINS):
        lookup = {d: ISI_BINS[i] for i, g in enumerate(groups) for d in g}
        df["isi"] = dur.map(lookup)
        df["duration_rank_used"] = True
    else:
        df["duration_rank_used"] = False
    df["duration"] = dur
    return df


def parse_invivo_sheet(df):
    """Rows of the in vivo recording list: cell, file, stimulus set, holding (mV), notes."""
    rows, cell = [], None
    for _, r in df.iloc[2:].iterrows():
        if pd.isna(r[1]):
            continue
        name = r[0]
        if isinstance(name, str) and re.match(r"^\d{6}_[eE]\d", name.strip()):
            cell = name.strip().lower()
            cell_note = ""
        elif isinstance(name, str):
            cell_note = name.strip()          # e.g. "j6a best call"
        rows.append({"cell": cell, "file": str(int(r[1])), "set": str(r[2]).strip(),
                     "holding": float(r[3]), "notes": "" if pd.isna(r[4]) else str(r[4]).strip(),
                     "cell_note": cell_note})
    out = pd.DataFrame(rows)
    # a cell note such as "j6a best call" applies to every later file of that cell
    best = {}
    for c, g in out.groupby("cell", sort=False):
        notes = [n for n in g.cell_note if "best call" in n.lower()]
        best[c] = notes[0].lower().replace("best call", "").strip() if notes else ""
    out["best_call"] = out.cell.map(best)
    return out.drop(columns="cell_note")


def sweep_range(notes, n_sweeps, apply_notes=True):
    """Sweeps kept under the spreadsheet notes (see module docstring)."""
    if not apply_notes:
        return list(range(n_sweeps)), "all"
    n = notes.lower()
    m = re.search(r"(stop|drop)\s*@\s*sweep\s*(\d+)", n)
    if m:
        return list(range(min(n_sweeps, int(m.group(2))))), f"before sweep {m.group(2)}"
    m = re.search(r"from sweep\s*(\d+)", n)
    if m:
        return list(range(int(m.group(1)), n_sweeps)), f"from sweep {m.group(1)}"
    if n.strip() == "drop" or "block + stop" in n:
        return [], "file dropped"
    return list(range(n_sweeps)), "all"


def invivo_file_sweeps(b, name):
    """Per sweep: call onset, offset, ISI, baseline and evoked current, from one ABF in memory."""
    abf = abf_from_bytes(b, name)
    fs = abf.dataRate
    rows = []
    for s in range(abf.sweepCount):
        abf.setSweep(s, channel=1)
        on, off = syllables(abf.sweepY, fs)
        abf.setSweep(s, channel=0)
        y = abf.sweepY
        row = {"file": name.replace(".abf", ""), "sweep": s, "n_syll": len(on),
               "holding_current": float(np.median(y))}
        if len(on) >= 2:
            gap = float(np.median(on[1:] - off[:-1]) * 1000)
            t0, t1 = on[0], off[-1] + POST_OFFSET_S
            i0, i1 = int(t0 * fs), int(min(t1, abf.sweepLengthSec) * fs)
            ib = max(0, int((t0 - BASELINE_S) * fs))
            base = float(y[ib:i0].mean())
            stim = float(y[i0:i1].mean())
            # a sham measure before the call, as a control for noise: the mean over the 0.75 s
            # before onset minus the mean over the 0.75 s before that
            i_s = max(0, int((t0 - 1.5) * fs))
            i_m = int((t0 - 0.75) * fs)
            sham = float(y[i_m:i0].mean() - y[i_s:i_m].mean())
            row.update({"onset": t0, "offset": off[-1], "gap_ms": gap,
                        "isi": min(ISI_BINS, key=lambda v: abs(v - gap)),
                        "baseline": base, "evoked": stim - base, "sham": sham,
                        "baseline_sd": float(y[ib:i0].std())})
        rows.append(row)
    df = assign_isi_by_duration(pd.DataFrame(rows))
    return df, {"rate": fs, "sweeps": abf.sweepCount, "sweep_s": abf.sweepLengthSec,
                                "adc": list(zip(abf.adcNames, abf.adcUnits)),
                                "protocol": abf.protocol, "date": str(abf.abfDateTime)}


def load_invivo(threads=8):
    """Every file of the two in vivo articles listed in their spreadsheets, measured per sweep."""
    sweeps, info, lists = [], [], []
    for key, group in (("invivo_ev", "experienced"), ("invivo_nv", "naive")):
        files, _ = figshare_files(key)
        sheet_name = [n for n in files if n.endswith(".xlsx")][0]
        lst = parse_invivo_sheet(pd.read_excel(io.BytesIO(fetch(files[sheet_name]["download_url"])),
                                               header=None))
        lst["group"] = group
        lst["on_figshare"] = lst.file.map(lambda f: f + ".abf" in files)
        lists.append(lst)

        def work(fname):
            sw, inf = invivo_file_sweeps(fetch(files[fname + ".abf"]["download_url"]), fname + ".abf")
            inf["file"] = fname
            return sw, inf
        todo = lst[lst.on_figshare].file.tolist()
        with ThreadPoolExecutor(threads) as ex:
            for sw, inf in ex.map(work, todo):
                sweeps.append(sw)
                info.append(inf)
    return pd.concat(lists, ignore_index=True), pd.concat(sweeps, ignore_index=True), pd.DataFrame(info)


def psc_table(lst, sweeps, top_n=5, apply_notes=True, best_call_only=True, check_holding=True,
              measure="evoked"):
    """Per cell, current (EPSC at -70 mV, IPSC at 0 mV or above) and ISI: mean absolute evoked
    current over the largest `top_n` trials, and the number of trials available. `measure` is
    "evoked" (the Methods' measure) or "sham" (the same taken before the call, a noise control)."""
    rows = []
    sw = sweeps.dropna(subset=["isi"])
    for _, f in lst[lst.on_figshare].iterrows():
        s = sw[sw.file == f.file]
        if not len(s):
            continue
        n_total = int(sweeps[sweeps.file == f.file].sweep.max()) + 1
        keep, _ = sweep_range(f.notes, n_total, apply_notes)
        s = s[s.sweep.isin(keep)]
        set_call = f.set.lower().replace(" set", "").strip()
        if best_call_only and f.best_call and "5xcalls" not in f.set and set_call != f.best_call:
            continue
        if "5xcalls" in f.set:
            continue
        kind = "EPSC" if f.holding < -30 else "IPSC"
        if check_holding:
            # a sweep whose holding current contradicts the listed holding potential (above
            # +100 pA in a -70 mV file, below -100 pA in a depolarized one) is dropped
            s = s[(s.holding_current <= 100) if kind == "EPSC" else (s.holding_current >= -100)]
        for _, r in s.iterrows():
            rows.append({"group": f.group, "cell": f.cell, "kind": kind, "file": f.file,
                         "isi": int(r.isi), "mag": abs(r[measure]), "evoked": r[measure]})
    t = pd.DataFrame(rows)
    out = (t.groupby(["group", "cell", "kind", "isi"])
             .agg(n_trials=("mag", "size"),
                  value=("mag", lambda v: np.sort(v.values)[::-1][:top_n].mean()),
                  signed=("evoked", "mean"))
             .reset_index())
    return out, t


# ---------------------------------------------------------------- operant

def operant_files():
    files, art = figshare_files("operant")
    rows = []
    for name, f in files.items():
        m = re.match(r"(?i)(nv\d+)_(proto|fast|slow)_v(\d+)(b?)\.csv", name)
        if m:
            rows.append({"name": name, "mouse": m.group(1).upper(), "group": m.group(2),
                         "session": int(m.group(3)), "part_b": m.group(4) == "b", "url": f["download_url"]})
    return pd.DataFrame(rows)


def read_touches(url):
    txt = fetch(url).decode()
    v = np.array([float(x) for x in txt.split() if x.strip()])
    return v


def resolution(t):
    """Step of the printed touch times: the csv holds 5 significant digits (MATLAB dlmwrite's
    default), so 0.001 s below 100 s, 0.01 s to 1000 s and 0.1 s above."""
    t = np.abs(np.asarray(t, float))
    return np.where(t < 100, 0.001, np.where(t < 1000, 0.01, 0.1))


def sampling_interval(t):
    """Median interval between touch samples, from the part of the session printed at 1 ms
    (below 100 s), over steps of at most 5 ms (within a press)."""
    t = np.sort(np.asarray(t, float))
    d = np.diff(t[t < 100])
    d = d[d <= 0.005]
    return float(np.mean(d)) if len(d) else np.nan


def presses(t, gap_rule, interval=np.nan):
    """Presses (start, end, duration in s) from touch-sample times. A gap ends a press when it
    exceeds the rule's threshold: 'median2', twice the median sampling interval (`interval`), or
    '100ms'. Because of the printed resolution a gap must also exceed the local step of the
    times (`resolution`) by half a step, otherwise one press held across a step would split."""
    t = np.sort(np.asarray(t, float))
    if len(t) == 0:
        return np.zeros((0, 3))
    d = np.diff(t)
    base = 2 * interval if gap_rule == "median2" else 0.1
    thr = np.maximum(base, 1.5 * resolution(t[1:]))
    brk = np.flatnonzero(d > thr + 1e-9)
    starts = np.r_[0, brk + 1]
    ends = np.r_[brk, len(t) - 1]
    return np.c_[t[starts], t[ends], t[ends] - t[starts]]


# ---------------------------------------------------------------- slices

SLICE_PEAK_WIN_S = (0.002, 0.030)   # after the stimulus artefact
SLICE_BASE_S = 0.005                # before it


def pulse_trains(abf):
    """Pulse trains of the sweep protocol: (first sample, period in samples, number of pulses,
    holding level in mV), from the ABF epoch table."""
    e = abf._epochPerDacSection
    p1s = abf.sweepEpochs.p1s
    trains = []
    for i, typ in enumerate(e.nEpochType):
        per = e.lEpochPulsePeriod[i]
        if typ == 3 and per > 0:
            start = p1s[i + 1]          # sweepEpochs carries a leading pre-holding segment
            m = re.search(r"Train(\d+)p", abf.protocol or "")
            n = int(m.group(1)) if m else int(np.ceil(e.lEpochInitDuration[i] / per))
            trains.append((start, per, n, float(e.fEpochInitLevel[i])))
    return trains


def _peak(y, tp, per, fs, kind):
    b0 = y[tp - int(SLICE_BASE_S * fs):tp].mean()
    w0 = tp + int(SLICE_PEAK_WIN_S[0] * fs)
    w1 = tp + int(min(SLICE_PEAK_WIN_S[1], per / fs - 0.002) * fs)
    seg = y[w0:w1]
    return b0 - seg.min() if kind == "EPSC" else seg.max() - b0


def slice_amplitudes(b, name):
    """Peak PSC of every pulse of every sweep of a slice recording: EPSCs in the train held at
    -70 mV (inward peak), IPSCs in the train held at a depolarized level (outward peak), each
    against the mean current in the `SLICE_BASE_S` before its pulse."""
    abf = abf_from_bytes(b, name)
    fs = abf.dataRate
    trains = pulse_trains(abf)
    sweeps = []
    for s in range(abf.sweepCount):
        abf.setSweep(s)
        sweeps.append(abf.sweepY.copy())
    rows = []
    # sweep -1 is the mean trace over the file's sweeps (a variant)
    for s, y in list(enumerate(sweeps)) + [(-1, np.mean(sweeps, axis=0))]:
        for start, per, n, level in trains:
            kind = "EPSC" if level <= -60 else "IPSC"
            for k in range(n):
                rows.append({"file": name.replace(".abf", ""), "sweep": s, "kind": kind, "level": level,
                             "pulse": k + 1, "period_ms": per / fs * 1000,
                             "amp": _peak(y, start + k * per, per, fs, kind)})
    return pd.DataFrame(rows)


def slice_list(df):
    """Cell, rate (ms) and file from the slice Recording List."""
    rows, cell = [], None
    rates = [int(str(c).split()[0]) for c in df.iloc[0, 1:]]
    for _, r in df.iloc[1:].iterrows():
        if isinstance(r[0], str) and r[0].startswith("Cell"):
            cell = r[0].strip()
        for j, rate in enumerate(rates, start=1):
            if not pd.isna(r[j]):
                rows.append({"cell": cell, "rate": rate, "file": str(r[j]).strip()})
    return pd.DataFrame(rows)


# ---------------------------------------------------------------- oxytocin slices

OXY_WINDOW_MIN = (15, 30)     # Methods: "15-30 minutes following wash onset"
SPIKE_MV = 0.0                # a spike is a crossing of 0 mV, a standard choice


def oxytocin_list(df):
    """Cell, group, file and label from the oxytocin spreadsheet (two side-by-side tables)."""
    rows = []
    for group, (c_cell, c_file, c_note) in (("oxytocin", (0, 2, 3)), ("control", (6, 8, 9))):
        cell = None
        for _, r in df.iloc[2:].iterrows():
            if pd.isna(r[c_file]):
                continue
            if isinstance(r[c_cell], str) and r[c_cell].strip():
                cell = r[c_cell].strip()
            rows.append({"group": group, "cell": cell, "file": str(r[c_file]).strip(),
                         "label": "" if pd.isna(r[c_note]) else str(r[c_note]).strip()})
    out = pd.DataFrame(rows)
    lab = out.label.str.lower()
    out["role"] = np.select(
        [lab.str.contains(r"\biv\b"), lab.str.contains("wash in"), lab.str.contains("wash out|post"),
         lab.str.contains("baseline|pre")],
        ["iv", "wash in", "wash out", "baseline"], default="other")
    return out


def spikes_per_pulse(b, name):
    """Per sweep: start time (s from the file's start) and, for each pulse of the stimulus train,
    whether Vm crossed `SPIKE_MV` before the next pulse."""
    abf = abf_from_bytes(b, name)
    fs = abf.dataRate
    trains = [t for t in pulse_trains(abf) if t[2] > 1]
    rows = []
    if not trains:
        return pd.DataFrame(rows), str(abf.abfDateTime)
    start, per, n, level = trains[0]
    for s in range(abf.sweepCount):
        abf.setSweep(s)
        y = abf.sweepY
        row = {"file": name.replace(".abf", ""), "sweep": s, "t": float(abf.sweepTimesSec[s]),
               "step_pA": level, "period_ms": per / fs * 1000}
        for k in range(n):
            tp = start + k * per
            row[f"stim{k + 1}"] = bool(y[tp + int(0.001 * fs):tp + per - int(0.001 * fs)].max() > SPIKE_MV)
        rows.append(row)
    return pd.DataFrame(rows), str(abf.abfDateTime)


def dunn_friedman(data, pairs):
    """Friedman test over the columns of `data` (subjects x conditions) and Dunn's comparisons of
    mean ranks for `pairs`, Bonferroni-corrected over the pairs (as in GraphPad Prism)."""
    from scipy import stats
    x = np.asarray(data, float)
    n, k = x.shape
    ranks = np.apply_along_axis(stats.rankdata, 1, x)
    R = ranks.mean(axis=0)
    chi = stats.friedmanchisquare(*x.T) if k >= 3 else None
    se = np.sqrt(k * (k + 1) / (6.0 * n))
    out = []
    for i, j in pairs:
        z = (R[j] - R[i]) / se
        p = 2 * stats.norm.sf(abs(z))
        out.append({"pair": (i, j), "mean_rank_diff": R[j] - R[i], "z": z, "p": p,
                    "p_bonf": min(1.0, p * len(pairs))})
    return chi, pd.DataFrame(out)
