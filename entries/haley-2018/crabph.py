"""Loading and measures for OSF project r7aes, the raw recordings of Haley, Hampton & Marder (2018),
"Two central pattern generators from the crab, Cancer borealis, respond robustly and differentially
to extreme extracellular pH", eLife 7:e41877, doi:10.7554/elife.41877.

The project holds one folder per experiment, each with Axon .abf files (one per pH step) and, for the
STG and CG experiments, a README.txt naming each file's pH and each channel's nerve. Files are read
anonymously from OSF Storage at the version pinned in r7aes_files.py, streamed into memory with
fsspec and never written to disk. A file read whole has its SHA-256 checked against that table.

Where the parameters come from (claims/haley-2018.yaml names the methods [EXT], [STATE], [INTRA],
[RM] and [MIX] in its header; "paper" is paper/10.7554-elife.41877.txt; "code" is
github.com/jesshaley/haley_hampton_marder_2018 at commit 83f5904):

- Experiments and units: the 15 STG experiments, the 15 CG experiment and unit pairs and the 9 PTX
  experiments are the lists of pHCumulative.m and pHCumulativePTX.m (claims header). A CG unit
  "CGnL" is the Large Cell unit on the trunk channel the README names "CGn (trunk)".
- Conditions: the code's 13 columns (pHCumulative.m, `pH_vars`): recovery from acid, 5.5, 6.1,
  6.7, 7.2, control before acid, control before base, 8.3, 8.8, 9.3, 9.8, 10.4, recovery from base.
  The pH of a file is the README's; for the PTX folders, which have no README, it is assigned from
  the bath pH channel recorded in each file (assumption, as nothing else names it; see
  `assign_ptx_conditions`). Where a README lists several consecutive control files, the last
  one of at least 8 min stands for the condition (a standard choice; the code takes one file).
- [EXT] spikes: spikes are found by thresholding the extracellular trace (paper, Methods, "Data
  acquisition and analysis", paragraph 4). The paper set thresholds by hand in Spike2
  (spikenburst.s2s); here they are automatic, an assumption: the trace is high-passed at
  `HIGHPASS_HZ` (a standard choice for extracellular spikes), the polarity is that of the larger
  extreme, and the threshold of a file is the largest of `NOISE_K` times the robust noise (median
  absolute deviation / 0.6745), Otsu's split of the log heights of the events above `OTSU_MIN_K`
  noise SDs for the PD on the pdn (the unit against noise and pickup) or `LC_FRAC` times the
  `LC_PCTL` percentile of those heights for the LC on the CG trunk (the LC is the largest unit
  there, and the Small Cells outnumber it), and `FLOOR_FRAC` times the unit's median spike height in its first control file, so that smaller
  units are not counted when the unit falls silent.
- [EXT] bursts: Spike2 BurstMake with 0.3 s maximum interspike interval and at least 2 spikes per
  burst (spikenburst.s2s starting values, claims header [EXT]; `MAX_ISI_S`, `MIN_SPIKES`), which
  the authors adjusted per file; for the CG, 1.0 s and 1 spike (`BURST_RULES`, an assumption).
  Frequency 1 / (onset of the previous burst to this onset), duty cycle = (first to last spike) /
  that period, spikes per burst, as readSpikeOutput.m. Duty cycles above 0.4 and spike counts
  above 15 (STG) or 30 (CG) are discarded (extracellularAnalysis.m). Means in 10 s bins, 48 bins
  over the last 8 min of the file (paper, Methods paragraphs 2 and 4); an empty bin counts as 0
  (pHCumulative.m). The value of a preparation and condition is the mean of its 48 bins
  (pHCumulative.m csv export). Variant (code): 48 bins from the first burst of the file
  (`window="code"`; claims header [EXT]).
- [STATE] proxy: the manual state annotations are not in the dataset. `rhythmic_fraction` gives,
  per second of the last 8 min, whether the pacemaker unit (PD, or LC) is bursting rhythmically:
  the second lies between two burst onsets no more than `RHYTHM_GAP_FACTOR` times the unit's median
  period in its first control step apart (an assumption; see the notebook). Runs shorter than 10 s
  are merged into their surroundings, as the paper notes a transition only after 10 s in the new
  state (Methods paragraph 3).
- [INTRA]: last minute of each file (paper, Methods paragraph 5); slow wave = Vm minus its high-pass
  (2nd order Butterworth at 10 Hz, zero phase), slow-wave peaks and troughs with prominence 1 mV and
  minimum distance 1/maxBurstFreq, spikes as peaks of the high-passed trace with prominence of at
  least minSpikeHeight, amplitude = peak minus trough, troughs and peaks paired in order
  (analyzeWaveform.m). maxBurstFreq and minSpikeHeight take the code's starting values (2 Hz and 10
  mV for PD, 10 Hz and 3 mV for LP; intracellularAnalysis.m), which the authors adjusted by hand.
  Minimum membrane potential: Methods reading, the minimum of the unfiltered Vm between successive
  slow-wave peaks (per second when there are none); code reading, the slow-wave troughs, and in a
  bin with none, the mean of the per-second minima of the slow wave (pHCumulativePTX.m). PD burst
  frequency from trough-to-trough intervals (Methods; peak-to-peak in the code, a variant). LP
  firing rate = 1 / interspike interval. Six 10 s bins; empty bins of frequency or amplitude are 0.
- [RM] and [MIX]: `rm_anova` and `mixed_anova` fit the multivariate linear model of car::Anova
  (orthonormal within-subject contrasts) and give the univariate F (sphericity assumed, as
  statistics.R reads `univariate.tests`) and Pillai's trace for the multivariate reading.
"""

from __future__ import annotations

import hashlib
import json
import re
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor

import fsspec
import numpy as np
import pandas as pd
import pyabf
from scipy import signal, stats

import r7aes_files

OSF_NODE = "r7aes"
PUBLISHED_VERSION = r7aes_files.PUBLISHED_VERSION
FILES = r7aes_files.table()

STG_EXPERIMENTS = ["877_093", "877_101", "877_121", "877_127", "877_141", "887_005", "887_049",
                   "887_069", "887_097", "887_105", "887_137", "887_141", "887_145", "897_005",
                   "897_037"]
CG_UNITS = [("877_149", "CG1L"), ("877_149", "CG2L"), ("887_005", "CG2L"), ("887_011", "CG3L"),
            ("887_017", "CG3L"), ("887_061", "CG1L"), ("887_065", "CG2L"), ("887_073", "CG2L"),
            ("887_093", "CG2L"), ("887_127", "CG1L"), ("887_149", "CG1L"), ("887_149", "CG2L"),
            ("897_041", "CG1L"), ("897_041", "CG3L"), ("897_041", "CG7L")]
PTX_EXPERIMENTS = ["903_046", "903_048", "903_050", "903_052", "903_054", "903_056", "903_058",
                   "903_060", "903_064"]
STG_EXAMPLE, CG_EXAMPLE = "897_037", ("877_149", "CG2L")

# The code's 13 columns (pHCumulative.m, pH_vars).
COLUMNS = ["rec_acid", "5.5", "6.1", "6.7", "7.2", "ctl_acid", "ctl_base", "8.3", "8.8", "9.3",
           "9.8", "10.4", "rec_base"]
ACID = ["5.5", "6.1", "6.7", "7.2", "ctl_acid"]
BASE = ["ctl_base", "8.3", "8.8", "9.3", "9.8", "10.4"]
ACID_STEPS, BASE_STEPS = ["7.2", "6.7", "6.1", "5.5"], ["8.3", "8.8", "9.3", "9.8", "10.4"]

WINDOW_S, BIN_S = 480, 10           # paper, Methods: last 8 min, 10 s bins
INTRA_S = 60                        # paper, Methods: last minute
CODE_WINDOW_S = 600                 # kept from the start of each file for the code's window variant
HIGHPASS_HZ = 100.0                 # standard choice for extracellular spikes
NOISE_K = 6.0                       # assumption: threshold at least 6 robust SDs of noise
OTSU_MIN_K = 4.0                    # events taken into the height split
FLOOR_FRAC = 0.4                    # assumption: floor at 40% of the unit's control spike height
LC_FRAC, LC_PCTL = 0.4, 99.5        # assumption: LC threshold at 40% of the largest events
MAX_ISI_S, MIN_SPIKES = 0.3, 2      # spikenburst.s2s starting values
# Burst rules per ganglion (maximum interspike interval in s, minimum spikes). STG: the
# spikenburst.s2s starting values. CG: an assumption, as the LC fires as few as one or two spikes,
# up to about 0.5 s apart, in each Small Cell burst, and the paper's CG state 1 counts one LC spike
# per SC burst (Results, cardiac rhythm, paragraph 3); the starting values are a variant.
BURST_RULES = {"STG": (MAX_ISI_S, MIN_SPIKES), "CG": (1.0, 1)}
MAX_SPIKES = {"STG": 15, "CG": 30}  # extracellularAnalysis.m
MAX_DUTY = 0.4                      # extracellularAnalysis.m
RHYTHM_GAP_FACTOR = 3.0             # assumption for the [STATE] proxy
MIN_STATE_S = 10                    # paper, Methods paragraph 3
INTRA_PARAMS = {"PD": (2.0, 10.0), "LP": (10.0, 3.0)}   # intracellularAnalysis.m starting values
WAVE_HP_HZ = 10.0                   # analyzeWaveform.m


# ----------------------------------------------------------------------------------------------
# Reading

def url(path):
    f = FILES[path]
    return f"https://osf.io/download/{f['key']}/?version={f['version']}"


def open_file(path):
    """An fsspec file of a pinned file, with its size from the target list (docs/archives.md)."""
    return fsspec.filesystem("http").open(url(path), block_size=2**20, size=FILES[path]["size"])


def read_text(path):
    data = open_file(path).read()
    assert hashlib.sha256(data).hexdigest() == FILES[path]["sha256"], path
    return data.decode()


def abf_header(fh, path):
    """pyabf's header readers applied to an open stream (pyabf.ABF itself wants a local path)."""
    a = pyabf.ABF.__new__(pyabf.ABF)
    a.abfFilePath, a.abfID, a.abfFolderPath = path, path, ""
    a._preLoadData, a._cacheStimulusFiles, a.stimulusFileFolder = False, False, None
    fh.seek(0)
    sig = fh.read(4)
    fh.seek(0)
    a.abfVersion = {"major": 2 if sig == b"ABF2" else 1}
    (a._readHeadersV2 if sig == b"ABF2" else a._readHeadersV1)(fh)
    return a


def header_info(path):
    with open_file(path) as fh:
        a = abf_header(fh, path)
    n = a.dataPointCount // a.channelCount
    return dict(path=path, rate=a.dataRate, nch=a.channelCount, channels=list(a.adcNames),
                units=list(a.adcUnits), seconds=n / a.dataRate, start=a.abfDateTime,
                dtype_bytes=a.dataPointByteSize)


def stream_abf(path, keep, whole=True, chunk_mb=32):
    """Read an ABF file and keep windows of chosen channels.

    keep: {channel: [(t0, t1), ...]} with times in seconds, negative counting from the end.
    whole: read the whole file and check its SHA-256; otherwise read only the windows.
    Returns (dict channel -> list of float32 arrays, header info, sha256 ok or None).
    """
    with open_file(path) as fh:
        a = abf_header(fh, path)
        nch, rate = a.channelCount, a.dataRate
        assert a.dataPointByteSize == 2
        n = a.dataPointCount // nch
        idx = {c: a.adcNames.index(c) for c in keep}
        wins = {}
        for c, ws in keep.items():
            wins[c] = []
            for t0, t1 in ws:
                i0 = int(round((t0 if t0 >= 0 else n / rate + t0) * rate))
                i1 = int(round((t1 if t1 > 0 else n / rate + t1) * rate)) if t1 is not None else n
                wins[c].append((max(0, i0), min(n, i1)))
        out = {c: [np.empty(i1 - i0, np.float32) for i0, i1 in wins[c]] for c in keep}
        gain = {c: a._dataGain[idx[c]] for c in keep}
        offs = {c: a._dataOffset[idx[c]] for c in keep}

        def take(raw, f0):
            f1 = f0 + raw.shape[0]
            for c in keep:
                for k, (i0, i1) in enumerate(wins[c]):
                    lo, hi = max(i0, f0), min(i1, f1)
                    if lo < hi:
                        out[c][k][lo - i0:hi - i0] = raw[lo - f0:hi - f0, idx[c]] * gain[c] + offs[c]

        ok = None
        if whole:
            h = hashlib.sha256()
            fh.seek(0)
            head = fh.read(a.dataByteStart)
            h.update(head)
            frame = nch * 2
            step = max(1, (chunk_mb << 20) // frame) * frame
            f0, left = 0, n * frame
            while left > 0:
                buf = fh.read(min(step, left))
                if not buf:
                    break
                h.update(buf)
                usable = len(buf) - len(buf) % frame
                raw = np.frombuffer(buf[:usable], np.int16).reshape(-1, nch)
                take(raw, f0)
                f0 += raw.shape[0]
                left -= len(buf)
            h.update(fh.read())
            ok = h.hexdigest() == FILES[path]["sha256"]
        else:
            spans = sorted({w for c in wins for w in wins[c]})
            for i0, i1 in spans:
                fh.seek(a.dataByteStart + i0 * nch * 2)
                raw = np.frombuffer(fh.read((i1 - i0) * nch * 2), np.int16).reshape(-1, nch)
                take(raw, i0)
    info = dict(path=path, rate=rate, seconds=n / rate, channels=list(a.adcNames),
                units=list(a.adcUnits))
    return out, info, ok


# ----------------------------------------------------------------------------------------------
# Experiments, conditions and channels

def parse_readme(text):
    files = re.findall(r"(\S+\.abf):\s*pH\s*([\d.]+)", text)
    elec = re.findall(r"^(IN \d+|extra\d+|Vm[\w_]*|ME\d_Vx):\s*(.+?)\s*$", text, flags=re.M)
    notes = text.split("Notes:")[1].strip() if "Notes:" in text else ""
    return [(f, p) for f, p in files], [(k, v) for k, v in elec], notes


def experiment_files(exp):
    return sorted(p for p in FILES if p.startswith(exp + "/") and p.endswith(".abf"))


def protocol_columns(seq):
    """Map an ordered list of (file, pH label) to the code's 13 columns.

    Consecutive files at 7.8 form one control block; the block between the two step protocols is
    both the recovery from the first and the control before the second. A pH repeated within a
    protocol (887_061 steps back up through 6.1 to 7.2) keeps its first file. Returns
    ({column: file}, order "AB" or "BA").
    """
    blocks, cur = [], None
    for f, p in seq:
        kind = "ctl" if p == "7.8" else ("acid" if float(p) < 7.8 else "base")
        if cur is None or cur[0] != kind:
            cur = (kind, [])
            blocks.append(cur)
        cur[1].append((f, p))
    kinds = [k for k, _ in blocks]
    steps = [k for k in kinds if k != "ctl"]
    order = "AB" if steps and steps[0] == "acid" else "BA"
    cols = {}
    ctl_blocks = [b for k, b in blocks if k == "ctl"]
    for k, b in blocks:
        if k in ("acid", "base"):
            for f, p in b:
                cols.setdefault(p, f)
    first, middle, last = (ctl_blocks + [None, None, None])[:3]
    pick = lambda b: None if not b else b[-1][0]
    if order == "AB":
        cols["ctl_acid"], cols["rec_acid"], cols["ctl_base"], cols["rec_base"] = (
            pick(first), pick(middle), pick(middle), pick(last))
    else:
        cols["ctl_base"], cols["rec_base"], cols["ctl_acid"], cols["rec_acid"] = (
            pick(first), pick(middle), pick(middle), pick(last))
    return {c: cols.get(c) for c in COLUMNS}, order


def control_block_files(seq):
    return [f for f, p in seq if p == "7.8"]


def assign_ptx_conditions(ph_values):
    """pH labels for a PTX folder (no README) from the bath pH channel of each file.

    ph_values: list of (file, mean pH electrode signal in mV over the last minute). Files within
    `tol` mV of the first file are control (7.8); a run of files above (acid) or below (base) is
    a run of four acid or five base files takes the nominal steps in the order of its measured pH;
    a shorter run takes for each file the nominal step nearest its estimated pH, 7.8 minus the
    change from the preceding control over 0.82 x 56.4 mV per pH unit (the Nernst slope at 11 C,
    scaled to the electrode's response between 7.8 and the extreme solutions in complete runs). Returns list of (file, label, estimated pH).
    """
    ctl = ph_values[0][1]
    tol, slope = 10.0, 0.82 * 56.4
    est, last_ctl = [], ctl
    for f, v in ph_values:
        if abs(v - ctl) < tol:
            est.append((f, None, 7.8))
            last_ctl = v
        else:
            est.append((f, "run", 7.8 - (v - last_ctl) / slope))
    out, i = [], 0
    while i < len(est):
        if est[i][1] is None:
            out.append((est[i][0], "7.8", 7.8))
            i += 1
            continue
        j = i
        while j < len(est) and est[j][1] == "run":
            j += 1
        run = est[i:j]
        nominal = ACID_STEPS if run[0][2] < 7.8 else BASE_STEPS
        if len(run) == len(nominal):     # a complete run: steps by rank of the measured pH
            ranked = sorted(run, key=lambda r: -r[2] if nominal is ACID_STEPS else r[2])
            lab = {r[0]: s for r, s in zip(ranked, nominal)}
            out += [(f, lab[f], e) for f, _, e in run]
        else:                            # a step missing: nearest nominal step
            out += [(f, min(nominal, key=lambda s: abs(float(s) - e)), e) for f, _, e in run]
        i = j
    return out


# ----------------------------------------------------------------------------------------------
# Spikes, bursts and binned measures

def highpass(x, fs, hz=HIGHPASS_HZ):
    sos = signal.butter(2, hz, "highpass", fs=fs, output="sos")
    return signal.sosfiltfilt(sos, x.astype(np.float64)).astype(np.float32)


def events(x, fs, polarity=None, k=4.0):
    """Peaks of the high-passed trace above k robust SDs: times (s), heights, noise SD, polarity."""
    y = highpass(x, fs)
    sd = float(np.median(np.abs(y)) / 0.6745)
    if polarity is None:
        polarity = -1 if -np.percentile(y, 0.01) > np.percentile(y, 99.99) else 1
    pk, pr = signal.find_peaks(polarity * y, height=k * sd, distance=max(1, int(0.003 * fs)))
    return pk / fs, pr["peak_heights"].astype(np.float32), sd, polarity


def bursts_from_spikes(t, max_isi=MAX_ISI_S, min_spikes=MIN_SPIKES):
    """Group spikes with intervals up to max_isi; keep groups of at least min_spikes.
    Returns DataFrame: tstart, tend, spikes, duration, period, hz, duty (readSpikeOutput.m)."""
    if len(t) == 0:
        return pd.DataFrame(columns=["tstart", "tend", "spikes", "duration", "period", "hz", "duty"])
    brk = np.where(np.diff(t) > max_isi)[0]
    starts = np.r_[0, brk + 1]
    ends = np.r_[brk, len(t) - 1]
    n = ends - starts + 1
    keep = n >= min_spikes
    b = pd.DataFrame({"tstart": t[starts[keep]], "tend": t[ends[keep]], "spikes": n[keep]})
    b["duration"] = b.tend - b.tstart
    b["period"] = b.tstart.diff()
    b["hz"] = 1 / b.period
    b["duty"] = b.duration / b.period
    return b.reset_index(drop=True)


def burst_bins(b, t0, ganglion, nbins=WINDOW_S // BIN_S):
    """48 bin means of hz, spikes and duty from t0, with the code's discards; empty bins are 0."""
    b = b.copy()
    b.loc[b.duty > MAX_DUTY, "duty"] = np.nan
    b.loc[b.spikes > MAX_SPIKES[ganglion], "spikes"] = np.nan
    rel = b.tstart.to_numpy() - t0
    out = {}
    for m in ["hz", "spikes", "duty"]:
        v = b[m].to_numpy(dtype=float)
        vals = np.zeros(nbins)
        for i in range(nbins):
            sel = (rel >= BIN_S * i) & (rel < BIN_S * (i + 1))
            if sel.any() and np.isfinite(v[sel]).any():
                vals[i] = np.nanmean(v[sel])
        out[m] = vals
    return out


def rhythmic_seconds(onsets, t0, t1, max_gap):
    """Per second in [t0, t1): True when the second lies between two burst onsets at most max_gap
    apart (the window's edges count as onsets when the first or last onset is within max_gap of
    them); then runs shorter than MIN_STATE_S are merged into the state before them."""
    n = int(round(t1 - t0))
    r = np.zeros(n, bool)
    on = np.sort(np.asarray(onsets, float))
    if len(on):
        if on[0] - t0 <= max_gap:
            on = np.r_[t0, on]
        if t1 - on[-1] <= max_gap:
            on = np.r_[on, t1]
    for a, b in zip(on[:-1], on[1:]):
        if b - a <= max_gap:
            i0, i1 = int(np.floor(a - t0)), int(np.ceil(b - t0))
            r[max(0, i0):max(0, min(n, i1))] = True
    s = r.copy()
    i = 0
    while i < n:
        j = i
        while j < n and r[j] == r[i]:
            j += 1
        if j - i < MIN_STATE_S and i > 0:
            s[i:j] = s[i - 1]
        i = j
    return s


# ----------------------------------------------------------------------------------------------
# Intracellular

def waveform(vm, fs, unit):
    """[INTRA] measures of one minute of Vm (analyzeWaveform.m, with the Methods' minimum)."""
    max_burst_hz, min_spike = INTRA_PARAMS[unit]
    b, a = signal.butter(2, WAVE_HP_HZ, "highpass", fs=fs)
    vm = vm.astype(np.float64)
    spk = signal.filtfilt(b, a, vm)
    wave = vm - spk
    dist = max(1, int(fs / max_burst_hz))
    p1, _ = signal.find_peaks(wave, distance=dist, prominence=1)
    p2, _ = signal.find_peaks(-wave, distance=dist, prominence=1)
    p3, _ = signal.find_peaks(spk, prominence=min_spike)
    p4, _ = signal.find_peaks(-spk, prominence=min_spike)
    nw, ns = min(len(p1), len(p2)), min(len(p3), len(p4))
    secs = int(len(vm) // fs)
    per_sec_wave = np.array([wave[int(i * fs):int((i + 1) * fs)].min() for i in range(secs)])
    per_sec_raw = np.array([vm[int(i * fs):int((i + 1) * fs)].min() for i in range(secs)])
    # Methods: minimum of the unfiltered Vm between successive slow-wave peaks
    if len(p1) >= 2:
        between = [(p1[i] + np.argmin(vm[p1[i]:p1[i + 1]])) for i in range(len(p1) - 1)]
        raw_min_t = np.array(between) / fs
        raw_min_v = vm[np.array(between)]
    else:
        raw_min_t, raw_min_v = np.array([]), np.array([])
    return dict(
        wave_t=p1[:nw] / fs, wave_max=wave[p1[:nw]], wave_min=wave[p2[:nw]],
        wave_amp=wave[p1[:nw]] - wave[p2[:nw]],
        trough_t=p2 / fs, trough_v=wave[p2], peak_t=p1 / fs,
        spike_t=p3[:ns] / fs, spike_amp=spk[p3[:ns]] - spk[p4[:ns]],
        raw_min_t=raw_min_t, raw_min_v=raw_min_v,
        per_sec_wave=per_sec_wave, per_sec_raw=per_sec_raw, mean_vm=float(vm.mean()))


def _bin6(t, v, empty):
    out = np.zeros(INTRA_S // BIN_S)
    for i in range(len(out)):
        sel = (t >= BIN_S * i) & (t < BIN_S * (i + 1))
        out[i] = np.nanmean(v[sel]) if sel.any() else (empty(i) if callable(empty) else empty)
    return out


def intra_measures(w):
    """Per preparation values (means of six 10 s bins) of one unit's [INTRA] measures."""
    sec_mean = lambda arr: (lambda i: float(np.mean(arr[BIN_S * i:BIN_S * (i + 1)])))
    r = {}
    r["vmin_methods"] = _bin6(w["raw_min_t"], w["raw_min_v"], sec_mean(w["per_sec_raw"])).mean()
    r["vmin_code"] = _bin6(w["trough_t"], w["trough_v"], sec_mean(w["per_sec_wave"])).mean()
    r["spike_amp"] = _bin6(w["spike_t"], w["spike_amp"], 0.0).mean()
    tt = w["trough_t"]
    r["burst_hz_trough"] = _bin6(tt[1:], 1 / np.diff(tt), 0.0).mean() if len(tt) > 1 else 0.0
    pt = w["wave_t"]
    r["burst_hz_peak"] = _bin6(pt[:-1], 1 / np.diff(pt), 0.0).mean() if len(pt) > 1 else 0.0
    st = w["spike_t"]
    r["spike_hz"] = _bin6(st[:-1], 1 / np.diff(st), 0.0).mean() if len(st) > 1 else 0.0
    r["wave_amp"] = _bin6(w["wave_t"], w["wave_amp"], 0.0).mean()
    r["n_spikes"] = len(st)
    isi = np.diff(st)
    r["isi_cv"] = float(isi.std() / isi.mean()) if len(isi) > 2 else np.nan
    r["n_waves"] = len(pt)
    r["mean_vm"] = w["mean_vm"]
    return r


# ----------------------------------------------------------------------------------------------
# Statistics

def _orth_contrasts(k):
    c = np.zeros((k, k - 1))
    for j in range(1, k):
        c[:j, j - 1] = 1
        c[j, j - 1] = -j
    return c / np.linalg.norm(c, axis=0)


def _mlm_tests(Y, X, L):
    """Within-subject tests of a multivariate linear model Y ~ X for hypothesis L on B (rows of
    X's coefficients), with orthonormal contrasts over Y's columns. Returns univariate F, df1, df2,
    p (sphericity assumed) and Pillai's trace with its F approximation."""
    n, k = Y.shape
    C = _orth_contrasts(k)
    Z = Y @ C
    XtX_inv = np.linalg.pinv(X.T @ X)
    B = XtX_inv @ X.T @ Z
    R = Z - X @ B
    E = R.T @ R
    dfe = n - np.linalg.matrix_rank(X)
    LB = L @ B
    H = LB.T @ np.linalg.pinv(L @ XtX_inv @ L.T) @ LB
    q, p = L.shape[0], k - 1
    F = (np.trace(H) / (q * p)) / (np.trace(E) / (dfe * p))
    df1, df2 = q * p, dfe * p
    pu = stats.f.sf(F, df1, df2)
    ev = np.real(np.linalg.eigvals(H @ np.linalg.pinv(E)))
    V = float(np.sum(ev / (1 + ev)))
    s, m_, nn = min(p, q), (abs(p - q) - 1) / 2, (dfe - p - 1) / 2
    Fp = (2 * nn + s + 1) / (2 * m_ + s + 1) * V / (s - V) if s - V > 0 else np.inf
    d1, d2 = s * (2 * m_ + s + 1), s * (2 * nn + s + 1)
    return dict(F=F, df1=df1, df2=df2, p=pu, pillai=V, F_pillai=Fp, p_pillai=stats.f.sf(Fp, d1, d2) if d2 > 0 else np.nan)


def rm_anova(df, cols):
    """One-way repeated-measures ANOVA over the columns (rows with any NaN dropped)."""
    Y = df[cols].dropna().to_numpy(float)
    X = np.ones((len(Y), 1))
    r = _mlm_tests(Y, X, np.array([[1.0]]))
    r["n"] = len(Y)
    return r


def posthoc_paired(df, control, steps, factor):
    rows = []
    for s in steps:
        d = df[[control, s]].dropna()
        t, p = stats.ttest_rel(d[control], d[s])
        rows.append(dict(step=s, n=len(d), mean_control=d[control].mean(), mean_step=d[s].mean(),
                         diff=d[s].mean() - d[control].mean(), t=t, p=p, p_corr=min(1.0, p * factor)))
    return pd.DataFrame(rows)


def rm_family(df, label=""):
    """[RM]: acid and base ANOVAs and the corrected paired t-tests against each control."""
    a, b = rm_anova(df, ACID), rm_anova(df, BASE)
    ta = posthoc_paired(df, "ctl_acid", ACID_STEPS, 4)
    tb = posthoc_paired(df, "ctl_base", BASE_STEPS, 5)
    return a, b, pd.concat([ta, tb], ignore_index=True)


def mixed_anova(df_a, df_b, cols, coding="sum"):
    """[MIX]: ganglion (between, two groups) by pH (within). Returns a table of the univariate and
    multivariate tests of pH, ganglion and their interaction under the given contrast coding."""
    Ya, Yb = df_a[cols].dropna().to_numpy(float), df_b[cols].dropna().to_numpy(float)
    Y = np.vstack([Ya, Yb])
    g = np.r_[np.zeros(len(Ya)), np.ones(len(Yb))]
    if coding == "sum":
        X = np.c_[np.ones(len(Y)), np.where(g == 0, 1.0, -1.0)]
    else:   # R's treatment coding, first level (alphabetical: CG) as reference
        X = np.c_[np.ones(len(Y)), g]
    ph = _mlm_tests(Y, X, np.array([[1.0, 0.0]]))
    inter = _mlm_tests(Y, X, np.array([[0.0, 1.0]]))
    # between-subject effect of ganglion on the mean over conditions (independent of coding)
    m = Y.mean(axis=1)
    fg, pg = stats.f_oneway(m[g == 0], m[g == 1])
    return dict(pH=ph, interaction=inter, ganglion=dict(F=fg, df1=1, df2=len(Y) - 2, p=pg),
                n=(len(Ya), len(Yb)))


# ----------------------------------------------------------------------------------------------
# The OSF listing

def osf_listing():
    """Every file in the project's OSF Storage now, walked through the API (docs/archives.md)."""
    def get(u):
        for attempt in range(6):
            try:
                with urllib.request.urlopen(u, timeout=120) as r:
                    return json.load(r)
            except urllib.error.HTTPError as e:
                if e.code < 500 or attempt == 5:
                    raise
            except (TimeoutError, urllib.error.URLError):
                if attempt == 5:
                    raise
            time.sleep(5 * 2 ** attempt)
    rows, providers = [], {}
    prov = get(f"https://api.osf.io/v2/nodes/{OSF_NODE}/files/")
    for p in prov["data"]:
        name = p["attributes"]["provider"]
        todo = [p["relationships"]["files"]["links"]["related"]["href"]]
        try:
            while todo:
                u = todo.pop()
                while u:
                    page = get(u if "page" in u else u + ("&" if "?" in u else "?") + "page%5Bsize%5D=100")
                    for it in page["data"]:
                        at = it["attributes"]
                        if at["kind"] == "folder":
                            todo.append(it["relationships"]["files"]["links"]["related"]["href"])
                        else:
                            rows.append(dict(path=at["materialized_path"].lstrip("/"), provider=name,
                                             version=at.get("current_version"), size=at["size"],
                                             sha256=(at.get("extra") or {}).get("hashes", {}).get("sha256")))
                    u = page["links"].get("next")
            providers[name] = "listed"
        except urllib.error.HTTPError as e:
            providers[name] = f"HTTP {e.code} {e.reason}"
    return pd.DataFrame(rows), providers


# ----------------------------------------------------------------------------------------------
# The experiments as the READMEs and the recorded pH describe them

def abf_channel(readme_key, names):
    """The ABF channel a README electrode key names ("Vm1_1" is VM1 in files that have no VM1_1)."""
    k = readme_key.upper() if readme_key.lower().startswith("vm") else readme_key
    if k in names:
        return k
    if k.endswith("_1") and k[:-2] in names:
        return k[:-2]
    return None


def describe_experiment(exp):
    """README of an STG or CG experiment: ordered (file, pH) and electrodes."""
    text = read_text(f"{exp}/README.txt")
    files, elec, notes = parse_readme(text)
    return dict(exp=exp, files=files, electrodes=elec, notes=notes, text=text)


def pd_channel(desc, names_per_file):
    """The pdn channel (the PD unit, pHCumulative.m) that every file of the experiment holds."""
    for k, v in desc["electrodes"]:
        if v.strip().lower() == "pdn" and all(abf_channel(k, n) for n in names_per_file):
            return abf_channel(k, names_per_file[0])
    return None


def intra_channels(desc, names):
    out = {}
    for k, v in desc["electrodes"]:
        if v.strip() in ("PD", "LP") and abf_channel(k, names):
            out.setdefault(v.strip(), abf_channel(k, names))
    return out


def cg_channel(desc, unit, names_per_file):
    """The trunk channel of a CG unit: the first README electrode for "CGn (trunk)" that every file
    of the experiment holds."""
    want = unit[:-1]       # "CG2L" -> "CG2"
    for k, v in desc["electrodes"]:
        if v.split()[0] == want and all(abf_channel(k, n) for n in names_per_file):
            return abf_channel(k, names_per_file[0])
    return None


def ph_channel(names):
    return next(c for c in names if c.lower() == "ph") if any(c.lower() == "ph" for c in names) else None


def process_file(job):
    """Stream one file; return spike events of the extracellular channels in the analysis windows,
    the last minute of the intracellular channels reduced to [INTRA] measures, and the pH signal."""
    path, ext, intra, whole = job["path"], job["ext"], job["intra"], job["whole"]
    info = header_info(path)
    names = info["channels"]
    keep = {}
    for c in ext:
        keep[c] = [(0, min(CODE_WINDOW_S, info["seconds"])), (-WINDOW_S, None)]
    for unit, c in intra.items():
        keep.setdefault(c, [])
        keep[c] = keep[c] + [(-INTRA_S, None)]
    phc = ph_channel(names)
    if phc:
        keep.setdefault(phc, [])
        keep[phc] = keep[phc] + [(-INTRA_S, None)]
    data, info, ok = stream_abf(path, keep, whole=whole)
    fs = info["rate"]
    res = dict(path=path, seconds=info["seconds"], rate=fs, sha_ok=ok, ext={}, intra={}, ph=None)
    for c in ext:
        early, late = data[c][0], data[c][1]
        e0 = events(early, fs)
        e1 = events(late, fs, polarity=e0[3])
        res["ext"][c] = dict(early=(e0[0], e0[1]), late=(e1[0] + info["seconds"] - len(late) / fs, e1[1]),
                             sd_early=e0[2], sd_late=e1[2], polarity=e0[3], late_start=info["seconds"] - len(late) / fs)
    for unit, c in intra.items():
        vm = data[c][-1]
        res["intra"][unit] = intra_measures(waveform(vm, fs, unit))
        res["intra"][unit]["channel"] = c
    if phc:
        res["ph"] = float(np.mean(data[phc][-1]))
    return res


def run_jobs(jobs, workers=8):
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(process_file, jobs))


def otsu_log(heights, bins=100):
    """Otsu's two-class split of log10 event heights; returns the threshold height."""
    x = np.log10(heights)
    hist, edges = np.histogram(x, bins=bins)
    mids = (edges[:-1] + edges[1:]) / 2
    w = np.cumsum(hist)
    m = np.cumsum(hist * mids)
    tot, mt = w[-1], m[-1]
    w0, w1 = w[:-1], tot - w[:-1]
    with np.errstate(divide="ignore", invalid="ignore"):
        between = (mt * w0 / tot - m[:-1]) ** 2 / (w0 * w1 / tot)
    between = np.nan_to_num(between)
    return 10 ** edges[1:-1][np.argmax(between)]


def unit_threshold(sd, heights, floor, ganglion="STG"):
    """Spike threshold of one file (an assumption: the paper set thresholds by hand).

    STG (PD on the pdn, which carries only the PD axons): the larger of NOISE_K x noise, Otsu's
    split of the log event heights (PD against noise and pickup), and the floor.
    CG (LC on the trunk, the largest unit there): the larger of NOISE_K x noise, LC_FRAC x the
    LC_PCTL percentile of the event heights (the Small Cells far outnumber the LC spikes, so a
    split by counts finds the SC), and the floor.
    The floor is FLOOR_FRAC x the unit's median spike height in its first control file, so that
    smaller units are not counted when the unit falls silent."""
    big = heights[heights >= OTSU_MIN_K * sd]
    if ganglion == "CG":
        split = LC_FRAC * np.percentile(big, LC_PCTL) if len(big) >= 20 else 0.0
    else:
        split = otsu_log(big) if len(big) >= 20 else 0.0
    return max(NOISE_K * sd, split, floor)


def unit_measures(results_by_file, channel, columns, ganglion, ref_file, burst_rule=None):
    """Per condition column: bins of the Methods window and of the code window, rhythmic seconds,
    burst table, thresholds. results_by_file: {file path: process_file result}."""
    r0 = results_by_file[ref_file]["ext"][channel]
    h0 = r0["late"][1]
    thr0 = unit_threshold(r0["sd_late"], h0, 0.0, ganglion)
    ref = float(np.median(h0[h0 >= thr0])) if (h0 >= thr0).any() else 0.0
    floor = FLOOR_FRAC * ref
    max_isi, min_spikes = burst_rule or BURST_RULES[ganglion]
    out = {}
    ctl_period = None
    for col in COLUMNS:
        f = columns.get(col)
        if f is None or f not in results_by_file:
            out[col] = None
            continue
        r = results_by_file[f]["ext"][channel]
        sec = results_by_file[f]["seconds"]
        thr = unit_threshold(r["sd_late"], r["late"][1], floor, ganglion)
        t_late = r["late"][0][r["late"][1] >= thr]
        b_late = bursts_from_spikes(np.sort(t_late), max_isi, min_spikes)
        thr_e = unit_threshold(r["sd_early"], r["early"][1], floor, ganglion)
        t_early = r["early"][0][r["early"][1] >= thr_e]
        b_early = bursts_from_spikes(np.sort(t_early), max_isi, min_spikes)
        t0 = r["late_start"]
        bins = burst_bins(b_late, t0, ganglion)
        if len(b_early):
            code_bins = burst_bins(b_early, b_early.tstart.iloc[0], ganglion)
        else:
            code_bins = {m: np.zeros(WINDOW_S // BIN_S) for m in ["hz", "spikes", "duty"]}
        out[col] = dict(file=f, seconds=sec, thr=thr, sd=r["sd_late"], n_spikes=len(t_late),
                        bursts=b_late, bins=bins, code_bins=code_bins,
                        window_s=min(WINDOW_S, sec))
    first = columns.get("ctl_acid") if columns.get("ctl_acid") == ref_file else columns.get("ctl_base")
    ctl = out.get("ctl_acid") if out.get("ctl_acid") and out["ctl_acid"]["file"] == ref_file else out.get("ctl_base")
    ctl_period = float(np.nanmedian(ctl["bursts"]["period"])) if ctl and len(ctl["bursts"]) > 2 else np.nan
    for col, v in out.items():
        if v is None:
            continue
        gap = RHYTHM_GAP_FACTOR * ctl_period if np.isfinite(ctl_period) else 0
        sec = v["seconds"]
        v["rhythmic"] = rhythmic_seconds(v["bursts"]["tstart"].to_numpy(), sec - v["window_s"], sec, gap)
    return out, ref, ctl_period


def resolve_file(exp, name):
    """The folder's file for a README file name; a name the folder lacks is matched by its number
    (877_149's README lists 877_149_00010.abf, the folder holds 877_149_0010.abf), else None."""
    p = f"{exp}/{name}"
    if p in FILES:
        return p
    try:
        n = int(name.rsplit("_", 1)[1].split(".")[0])
    except (IndexError, ValueError):
        return None
    hits = [q for q in experiment_files(exp) if int(q.rsplit("_", 1)[1].split(".")[0]) == n]
    return hits[0] if len(hits) == 1 else None


def pick_controls(seq, seconds):
    """Within each block of consecutive 7.8 files keep the last one of at least 8 min (else the
    longest), so that the 8 min window lies in one file."""
    out, block = [], []
    def flush():
        if block:
            long = [f for f, _ in block if seconds.get(f, 0) >= WINDOW_S]
            keep = long[-1] if long else max(block, key=lambda x: seconds.get(x[0], 0))[0]
            out.append((keep, "7.8"))
    for f, p in seq:
        if p == "7.8":
            block.append((f, p))
        else:
            flush()
            block = []
            out.append((f, p))
    flush()
    return out


def plan_extracellular(stg=STG_EXPERIMENTS, cg=CG_UNITS):
    """Per experiment present in the project: README, file sequence, condition columns, channels.
    Returns (plans, missing experiments, file jobs)."""
    folders = {p.split("/")[0] for p in FILES}
    exps = sorted(set(stg) | {e for e, _ in cg})
    plans, missing = {}, [e for e in exps if e not in folders]
    exps = [e for e in exps if e in folders]
    with ThreadPoolExecutor(16) as ex:
        descs = dict(zip(exps, ex.map(describe_experiment, exps)))
        paths = sorted({resolve_file(e, f) for e in exps for f, _ in descs[e]["files"]} - {None})
        all_heads = dict(zip(paths, ex.map(header_info, paths)))
    for e in exps:
        d = descs[e]
        seq_raw = [(resolve_file(e, f), p) for f, p in d["files"]]
        heads = {f: all_heads[f] for f, _ in seq_raw if f}
        seconds = {f: h["seconds"] for f, h in heads.items()}
        seq = pick_controls([(f, p) for f, p in seq_raw if f], seconds)
        cols, order = protocol_columns(seq)
        names = [heads[f]["channels"] for f, _ in seq]
        units = {}
        if e in stg:
            units["PD"] = ("STG", pd_channel(d, names))
        for ee, u in cg:
            if ee == e:
                units[u] = ("CG", cg_channel(d, u, names))
        intra = {}
        if e in stg:
            for unit in ("PD", "LP"):
                chans = [intra_channels(d, n).get(unit) for n in names]
                if chans and all(chans) and len(set(chans)) == 1:
                    intra[unit] = chans[0]
        plans[e] = dict(desc=d, seq_raw=seq_raw, seq=seq, columns=cols, order=order, units=units,
                        intra=intra, heads=heads, unlisted=[f for f in experiment_files(e)
                                                            if f not in {x for x, _ in seq_raw}])
    jobs = []
    for e, pl in plans.items():
        ext = sorted({c for _, c in pl["units"].values() if c})
        for f, _ in pl["seq"]:
            jobs.append(dict(path=f, ext=ext, intra=pl["intra"], whole=True))
    return plans, missing, jobs


def ptx_jobs(exp):
    """The files of a PTX experiment, each with its PD and LP intracellular channels. The channels
    are chosen by input position, with the label most files of the experiment give that position
    (903_046_0002 names the two electrodes the other way round from the other ten files)."""
    paths = experiment_files(exp)
    names = [header_info(p)["channels"] for p in paths]
    width = min(len(n) for n in names)
    pos = {}
    for i in range(width):
        labels = [n[i] for n in names if i < len(n)]
        top = max(set(labels), key=labels.count)
        for u in ("PD", "LP"):
            if top.upper().startswith(u) and u not in pos:
                pos[u] = i
    jobs = []
    for p, n in zip(paths, names):
        jobs.append(dict(path=p, ext=[], intra={u: n[i] for u, i in pos.items()}, whole=False,
                         pdn="pdn" if "pdn" in n else None,
                         labels={u: n[i] for u, i in pos.items()}))
    return jobs


def process_ptx(job):
    """Last minute of a PTX file: [INTRA] measures of PD and LP, the pH signal, and the fraction of
    PD intracellular spikes that fall within 5 ms of a pdn spike (a check of the PD label)."""
    path, intra = job["path"], job["intra"]
    keep = {c: [(-INTRA_S, None)] for c in intra.values()}
    names = header_info(path)["channels"]
    phc = ph_channel(names)
    keep[phc] = [(-INTRA_S, None)]
    if job["pdn"]:
        keep["pdn"] = [(-INTRA_S, None)]
    data, info, _ = stream_abf(path, keep, whole=False)
    fs = info["rate"]
    res = dict(path=path, seconds=info["seconds"], channels=names, intra={}, ph=float(np.mean(data[phc][0])))
    ws = {}
    for unit, c in intra.items():
        w = waveform(data[c][0], fs, unit)
        ws[unit] = w
        res["intra"][unit] = intra_measures(w)
        res["intra"][unit]["channel"] = c
    if job["pdn"]:
        t, h, sd, pol = events(data["pdn"][0], fs, k=NOISE_K)
        for unit, w in ws.items():
            st = w["spike_t"]
            if len(st) and len(t):
                j = np.searchsorted(t, st)
                d = np.minimum(np.abs(t[np.clip(j, 0, len(t) - 1)] - st), np.abs(t[np.clip(j - 1, 0, len(t) - 1)] - st))
                res["intra"][unit]["pdn_match"] = float(np.mean(d < 0.005))
            else:
                res["intra"][unit]["pdn_match"] = np.nan
    return res


# ----------------------------------------------------------------------------------------------
# Tables per unit and condition

def ext_units(plans, results, cg_rule=None):
    """Every extracellular unit (STG PD per experiment, CG units) with its measures per condition.
    cg_rule: a (max ISI, min spikes) burst rule for the CG units in place of BURST_RULES["CG"]."""
    R = {r["path"]: r for r in results}
    units = []
    for e, pl in plans.items():
        for u, (g, ch) in pl["units"].items():
            row = dict(ganglion=g, exp=e, unit=u, channel=ch, order=pl["order"],
                       label=f"{e} {u}" if g == "CG" else e)
            if ch is None:
                row.update(out=None)
            else:
                out, ref, cp = unit_measures(R, ch, pl["columns"], g, pl["seq"][0][0],
                                             cg_rule if g == "CG" else None)
                row.update(out=out, ref=ref, ctl_period=cp)
            units.append(row)
    return units


def measure_frame(units, ganglion, measure, window="methods", missing="zero"):
    """Per unit and condition, the mean of the 48 bins. missing: "zero" (a step the experiment
    lacks counts as 0, as pHCumulative.m gives it) or "nan" (left out)."""
    rows = {}
    for u in units:
        if u["ganglion"] != ganglion or u["out"] is None:
            continue
        key = "bins" if window == "methods" else "code_bins"
        rows[u["label"]] = {c: (u["out"][c][key][measure].mean() if u["out"][c] is not None
                                else (0.0 if missing == "zero" else np.nan)) for c in COLUMNS}
    return pd.DataFrame(rows).T[COLUMNS]


def rhythmic_frame(units, ganglion, missing="zero"):
    rows = {}
    for u in units:
        if u["ganglion"] != ganglion or u["out"] is None:
            continue
        rows[u["label"]] = {c: (u["out"][c]["rhythmic"].mean() if u["out"][c] is not None
                                else (0.0 if missing == "zero" else np.nan)) for c in COLUMNS}
    return pd.DataFrame(rows).T[COLUMNS]


def bins_frame(units, ganglion, measure, column):
    """The 48 bin values of every unit at one condition (long form)."""
    rows = []
    for u in units:
        if u["ganglion"] != ganglion or u["out"] is None or u["out"][column] is None:
            continue
        for i, v in enumerate(u["out"][column]["bins"][measure]):
            rows.append(dict(unit=u["label"], bin=i, value=v))
    return pd.DataFrame(rows)


def ptx_tables(ptx_results):
    """PTX experiments: condition per file from the recorded pH, and per unit and measure a frame
    of preparations by condition (a step the experiment lacks is NaN)."""
    files, frames = [], {}
    for exp in PTX_EXPERIMENTS:
        rs = sorted([r for r in ptx_results if r["path"].startswith(exp + "/")], key=lambda r: r["path"])
        lab = assign_ptx_conditions([(r["path"], r["ph"]) for r in rs])
        seq = [(f, l) for f, l, _ in lab]
        cols, order = protocol_columns(pick_controls(seq, {r["path"]: 1e9 for r in rs}))
        byp = {r["path"]: r for r in rs}
        for (f, l, est), r in zip(lab, rs):
            files.append(dict(exp=exp, file=f, label=l, est_pH=est, ph_signal=r["ph"], minutes=r["seconds"] / 60,
                              order=order, used=f in cols.values(),
                              PD_channel=r["intra"].get("PD", {}).get("channel"),
                              LP_channel=r["intra"].get("LP", {}).get("channel"),
                              PD_pdn_match=r["intra"].get("PD", {}).get("pdn_match", np.nan),
                              LP_pdn_match=r["intra"].get("LP", {}).get("pdn_match", np.nan)))
        for unit in ("PD", "LP"):
            for c in COLUMNS:
                f = cols.get(c)
                m = byp[f]["intra"].get(unit) if f else None
                for k in ("vmin_methods", "vmin_code", "spike_amp", "burst_hz_trough", "burst_hz_peak",
                          "spike_hz", "wave_amp", "n_spikes", "n_waves", "mean_vm", "isi_cv"):
                    frames.setdefault((unit, k), {}).setdefault(exp, {})[c] = (m.get(k, np.nan) if m else np.nan)
    frames = {k: pd.DataFrame(v).T[COLUMNS] for k, v in frames.items()}
    return pd.DataFrame(files), frames


def intact_intra_frames(plans, results):
    """Intact STG preparations with intracellular PD or LP: [INTRA] measures per condition."""
    R = {r["path"]: r for r in results}
    frames = {}
    for e, pl in plans.items():
        for unit in pl["intra"]:
            for c in COLUMNS:
                f = pl["columns"].get(c)
                m = R[f]["intra"].get(unit) if f else None
                for k in ("vmin_methods", "vmin_code", "wave_amp", "n_spikes", "spike_amp", "mean_vm"):
                    frames.setdefault((unit, k), {}).setdefault(e, {})[c] = m[k] if m else np.nan
    return {k: pd.DataFrame(v).T[COLUMNS] for k, v in frames.items()}


# ----------------------------------------------------------------------------------------------
# Reporting

def rm_report(df, label, show=True):
    """[RM] on a frame of preparations by condition; prints the ANOVAs and the t-tests."""
    a, b, t = rm_family(df)
    if show:
        print(f"{label}: acid ANOVA F({a['df1']},{a['df2']}) = {a['F']:.2f}, p = {a['p']:.3g} (n = {a['n']}); "
              f"base ANOVA F({b['df1']},{b['df2']}) = {b['F']:.2f}, p = {b['p']:.3g} (n = {b['n']})")
        print(t.assign(mean_control=t.mean_control.round(3), mean_step=t.mean_step.round(3),
                       diff=t["diff"].round(3), t=t.t.round(2), p=t.p.map("{:.3g}".format),
                       p_corr=t.p_corr.map("{:.3g}".format)).to_string(index=False))
    return a, b, t.set_index("step")


def spearman_sign(row, cols, ph):
    r = stats.spearmanr([ph[c] for c in cols], [row[c] for c in cols])
    return r.statistic


PH_OF = {"ctl_acid": 7.8, "ctl_base": 7.8, "7.2": 7.2, "6.7": 6.7, "6.1": 6.1, "5.5": 5.5,
         "8.3": 8.3, "8.8": 8.8, "9.3": 9.3, "9.8": 9.8, "10.4": 10.4}
