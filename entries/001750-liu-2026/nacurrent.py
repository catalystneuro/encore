"""Loading and measures for dandiset 001750 (Liu et al. 2026, Nat Cell Biol), outside-out Na+ currents.

The dandiset holds one NWB file per outside-out patch (35 files, subject Mfa-221206, sessions
221206AS and 221206HS). Each file holds VoltageClampSeries named
NaCurrentSeries_Repetition_<r>_Sweep_<s> in acquisition and the matching
VoltageClampStimulusSeries in stimulus. Sweep s steps from -80 mV to -80 + 5 (s - 1) mV.

Where the parameters come from:
- Steps from -80 to 0 mV in 5 mV increments, 25 ms, leak subtracted online, 100 kHz (Methods,
  Electrophysiological recording, "families of Na+ currents in response to a series of depolarizing
  voltages ranging from -80 to 0 mV (25 ms) with 5-mV stepping ... leak subtracted online with
  PatchMaster ... 100-kHz sample frequency"). The sampling rate and step onset are read from each file.
- Measure: the largest peak inward current over the steps, absolute value in pA, after averaging the
  repeated sweeps of a step (claim fig4d-sodium-current-lower, criterion, which cites the paper's code
  ephysio/Fig4d_plotNaCurrent.m in github.com/RFLiu2021/AIC_proj at commit 44cd8a6).
- Readings named by the criterion: baseline (a1) as recorded or (a2) minus the mean of the first 100
  samples of a cut starting 2 ms before the step onset (the code's example traces); steps (b1) the 17
  sweeps from -80 to 0 mV or (b2) all sweeps; window (c1) 0 to 20 ms after onset or (c2) the whole
  25 ms step.
- `smooth` in max_inward (a moving average over n samples before the peak is taken) is not a
  reading of the paper: no filter is named in the Methods or the code. It is a variant, chosen after
  the readings were run, to see what measure the code table's values could come from; it decides
  nothing.
- `bessel_hz` in max_inward (a zero-phase 4-pole Bessel low-pass, scipy sosfiltfilt) is also not a
  reading of the paper, which names no filter. Bessel low-pass filters are what HEKA amplifiers
  apply (2.9 and 10 kHz are common settings); the cut-offs 2.9, 5 and 10 kHz were fixed before
  their results were seen, so unlike `smooth` they were not fitted to the code table. A standard
  choice for a variant that decides nothing.
- `win_ms` in max_inward overrides the reading's window with 0 to win_ms after onset. It is a
  non-deciding variant: a Na+ current peaks within a few ms of the step, so a short window keeps
  noise maxima late in the step out of the measure.
- Cell types are not in the files; they come from the paper's code table
  metadata_outSideOutSodiumCurrentRec.csv (CELL_TABLE_URL), matched by NWB file name.
"""
import io
import re

import hashlib

import h5py
import numpy as np
import pandas as pd
import remfile
import requests
from scipy import ndimage, signal

DANDISET = "001750"
VERSION = "0.260825.0222"
API = "https://api.dandiarchive.org/api"
CODE_COMMIT = "44cd8a6dfbb1f1ce363d73742e4f3652086b0f9d"
CELL_TABLE_URL = (
    "https://raw.githubusercontent.com/RFLiu2021/AIC_proj/" + CODE_COMMIT
    + "/ephysio/data_ephy/rawdata_ephysio/metadata_outSideOutSodiumCurrentRec.csv"
)

READINGS = [(a, b, c) for a in ("a1", "a2") for b in ("b1", "b2") for c in ("c1", "c2")]


def list_assets():
    """Assets of the pinned version: path, asset id and size."""
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=200"
    rows = []
    while url:
        r = requests.get(url, timeout=60).json()
        rows += [dict(path=a["path"], asset_id=a["asset_id"], size=a["size"]) for a in r["results"]]
        url = r["next"]
    df = pd.DataFrame(rows)
    df["file"] = df.path.str.split("/").str[-1]
    return df.sort_values("file").reset_index(drop=True)


def asset_metadata(asset_id):
    return requests.get(f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/{asset_id}/",
                        timeout=60).json()


def open_asset(asset_id):
    loc = requests.head(f"{API}/assets/{asset_id}/download/", allow_redirects=False,
                        timeout=60).headers["Location"]
    return h5py.File(remfile.File(loc), "r")


def cell_table():
    """The paper's code table of the 35 patches (subject, cell ID, NWB file, type, max current)."""
    return pd.read_csv(io.StringIO(requests.get(CELL_TABLE_URL, timeout=60).text))


def load_patch(asset_id):
    """Read one file: currents (pA) as an array [repetition, sweep, sample], command (mV) of
    repetition 1, rate (Hz), and file-level metadata. Every series is read; the files are small."""
    f = open_asset(asset_id)
    acq, stim = f["acquisition"], f["stimulus/presentation"]
    keys = list(acq.keys())
    parsed = [tuple(int(x) for x in re.search(r"Repetition_(\d+)_Sweep_(\d+)", k).groups()) for k in keys]
    reps = sorted({r for r, _ in parsed})
    sweeps = sorted({s for _, s in parsed})
    n = acq[keys[0]]["data"].shape[0]
    cur = np.full((len(reps), len(sweeps), n), np.nan)
    info = []
    for k, (r, s) in zip(keys, parsed):
        d = acq[k]["data"]
        conv = d.attrs["conversion"]
        cur[reps.index(r), sweeps.index(s)] = d[:] * conv * 1e12
        st = acq[k]["starting_time"]
        info.append(dict(rep=r, sweep=s, unit=d.attrs["unit"], rate=float(st.attrs["rate"]),
                         n=d.shape[0], start=float(st[()]), gain=float(acq[k]["gain"][()]),
                         fields=",".join(sorted(acq[k].keys())),
                         stim_unit=stim[k.replace("NaCurrentSeries", "VoltageClampStimulusSeries")]["data"].attrs["unit"]))
    cmd = np.full((len(reps), len(sweeps), n), np.nan)
    for i, r in enumerate(reps):
        for j, s in enumerate(sweeps):
            sk = f"VoltageClampStimulusSeries_Repetition_{r}_Sweep_{s}"
            if sk in stim:
                cmd[i, j] = stim[sk]["data"][:] * 1e3
    meta = dict(cell_id=f["general/intracellular_ephys/IntracellularElectrode/cell_id"][0].decode(),
                session_id=f["general/session_id"][()].decode(),
                subject_id=f["general/subject/subject_id"][()].decode(),
                location=f["general/intracellular_ephys/IntracellularElectrode/location"][()].decode(),
                session_start=f["session_start_time"][0].decode() if f["session_start_time"].shape else f["session_start_time"][()].decode(),
                keys_general=",".join(sorted(f["general"].keys())))
    meta["text"] = file_text(f)
    f.close()
    digest = hashlib.sha1(np.ascontiguousarray(cur[0]).tobytes()).hexdigest()
    return dict(current=cur, command=cmd, sweeps=np.array(sweeps), reps=np.array(reps),
                info=pd.DataFrame(info), meta=meta, digest=digest)


def _txt(v):
    if isinstance(v, bytes):
        return v.decode()
    if isinstance(v, np.ndarray):
        return ";".join(_txt(x) for x in v.ravel())
    return str(v)


def file_text(f):
    """Every value and attribute of the file outside the data series and the format specification,
    as {path: text}, and the attributes of the series themselves (description, comments ...), each
    distinct value once, so that a search for capacitance or resistance covers the whole file."""
    out = {}

    def visit(name, obj):
        if name.startswith(("specifications", "acquisition/", "stimulus/")):
            return
        for k, v in obj.attrs.items():
            if k != "object_id":
                out[f"{name}@{k}"] = _txt(v)
        if isinstance(obj, h5py.Dataset):
            out[name] = _txt(obj[()])

    f.visititems(visit)
    for grp in ("acquisition", "stimulus/presentation"):
        for k in f[grp]:
            for sub in [f[grp][k]] + [f[grp][k][x] for x in f[grp][k]]:
                for a, v in sub.attrs.items():
                    if a not in ("object_id", "sweep_number"):
                        key = f"{grp}/<series>{sub.name[len(f[grp][k].name):]}@{a}"
                        out.setdefault(key, set()).add(_txt(v))
    return {k: (";".join(sorted(v)) if isinstance(v, set) else v) for k, v in out.items()}


def load_all(keep_reps=False):
    """Stream every file of the pinned version. Keeps the repetition-averaged currents (and, with
    keep_reps, every repetition), the command of repetition 1 and the metadata."""
    out = []
    for _, a in list_assets().iterrows():
        p = load_patch(a.asset_id)
        levels, onsets, offsets = step_levels(p["command"])
        p.update(file=a.file, path=a.path, asset_id=a.asset_id, size=a["size"], levels=levels,
                 onsets=onsets, offsets=offsets, mean=np.nanmean(p["current"], axis=0),
                 rate=float(p["info"].rate.iloc[0]), nrep=len(p["reps"]))
        stepped = onsets > 0
        p["onset"] = int(np.median(onsets[stepped]))
        p["step_ms"] = float(np.median(offsets[stepped] - onsets[stepped])) / p["rate"] * 1e3
        if not keep_reps:
            p["rep_sd"] = float(np.nanmean(np.nanstd(p["current"][:, :, :p["onset"] - 100], axis=2)))
            p["current"] = None
        out.append(p)
    return out


def step_levels(command):
    """Step level (mV) of each sweep, from the command of repetition 1, and the step onset and
    offset (samples), from the first and last change of the command."""
    c = command[0]
    levels, onsets, offsets = [], [], []
    for x in c:
        ch = np.flatnonzero(np.abs(np.diff(x)) > 0.01)
        if len(ch):
            onsets.append(ch[0] + 1)
            offsets.append(ch[-1] + 1)
            levels.append(float(np.median(x[ch[0] + 1:ch[-1] + 1])))
        else:
            onsets.append(-1)
            offsets.append(-1)
            levels.append(float(np.median(x)))
    return np.array(levels), np.array(onsets), np.array(offsets)


def lowpass(mean, rate, bessel_hz):
    """Zero-phase 4-pole Bessel low-pass of traces [sweep, sample] (non-deciding variant)."""
    sos = signal.bessel(4, bessel_hz, fs=rate, output="sos", norm="mag")
    return signal.sosfiltfilt(sos, mean, axis=1)


def max_inward(mean, levels, onset, rate, reading, smooth=1, bessel_hz=None, win_ms=None):
    """Largest peak inward current (absolute value, pA) under one reading (a, b, c), from the
    repetition-averaged traces [sweep, sample]. Returns the value, the step level (mV) and the
    latency (ms) where it is found. smooth > 1, bessel_hz and win_ms are the non-deciding
    variants (module docstring)."""
    a, b, c = reading
    if smooth > 1:
        mean = ndimage.uniform_filter1d(mean, smooth, axis=1)
    if bessel_hz:
        mean = lowpass(mean, rate, bessel_hz)
    pre = int(round(0.002 * rate))          # the cut starts 2 ms before onset (code's examples)
    win = int(round((0.020 if c == "c1" else 0.025) * rate))
    if win_ms:
        win = int(round(win_ms / 1e3 * rate))
    use = levels <= 0.5 if b == "b1" else np.ones(len(levels), bool)
    best, lev, lat = 0.0, np.nan, np.nan
    for j in np.flatnonzero(use):
        tr = mean[j]
        base = tr[onset - pre:onset - pre + 100].mean() if a == "a2" else 0.0
        seg = tr[onset:onset + win] - base
        k = int(np.argmin(seg))
        if -seg[k] > best:
            best, lev, lat = float(-seg[k]), float(levels[j]), k / rate * 1e3
    return best, lev, lat


def iv_curve(mean, levels, onset, rate, reading=("a2", "b1", "c1"), win_ms=None):
    """Peak inward current (pA, inward positive, 0 when the trace never goes below the baseline)
    and its latency (ms) at each step, under one reading's baseline and window, as a DataFrame
    indexed by step level (mV)."""
    rows = []
    for j in range(len(levels)):
        v, _, lat = max_inward(mean[j:j + 1], levels[j:j + 1], onset, rate,
                               (reading[0], "b2", reading[2]), win_ms=win_ms)
        rows.append(dict(level=float(levels[j]), peak=v, latency_ms=lat))
    return pd.DataFrame(rows).set_index("level")


def measure_all(patches, smooth=1, bessel_hz=None, win_ms=None):
    """Per patch, the maximal inward current under each reading (columns a1b1c1 ... a2b2c2), with the
    step level and latency of the maximum under the code's example reading a2 b1 c1."""
    rows = []
    for p in patches:
        r = dict(file=p["file"])
        for rd in READINGS:
            v, lev, lat = max_inward(p["mean"], p["levels"], p["onset"], p["rate"], rd, smooth,
                                     bessel_hz, win_ms)
            r["".join(rd)] = v
            if rd == ("a2", "b1", "c1"):
                r["level_mV"], r["latency_ms"] = lev, lat
        rows.append(r)
    return pd.DataFrame(rows)


def repo_file(path):
    """A file of the paper's code repository at the commit the claims file read, as bytes."""
    url = f"https://raw.githubusercontent.com/RFLiu2021/AIC_proj/{CODE_COMMIT}/{path}"
    r = requests.get(url, timeout=120)
    r.raise_for_status()
    return r.content
