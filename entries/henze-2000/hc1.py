"""Streaming loader and spike measures for CRCNS hc-1 (Henze et al. 2000, J Neurophysiol 84:390).

The data set holds one zip per intracellularly recorded cell under
https://crcnsarchive.s3-us-west-2.amazonaws.com/hc-1/live/Data/. Each zip holds one or more
binary .dat files (int16, samples interleaved by channel) with a Neuroscope .xml giving the
channel count and sampling rate. The zips are read in place over HTTP range requests with
fsspec and zipfile; nothing is written to disk.

Where each parameter comes from:

- Channel roles. The data descriptor says the last channel is "almost always" the injected
  current and the one before it the membrane potential, "but this varies", and to "look at the
  data and you will find the good channel containing intracellular spikes". The files show two
  formats: 12-bit values (0 to 4095, centre 2048; files named dNNNNNMM.dat) and signed 16-bit
  values (files named dNNNNN.00M.dat). The extracellular (EC) channels are taken from the
  folder READMEs where there are any (d5331, d5611, d6811, d7111: channels 2 to 5, one-based;
  d13521: 1 to 4) and extended to the folders of the same format and period; for the 16-bit
  files they are the first Neuroscope channel group (all channels except the last two). The
  intracellular (IC) channel is chosen from the data in each file (`pick_ic`): among the
  non-EC channels that are not clipped, the one with the most action-potential-like events of
  at least 10 mV. This is a choice made here from the descriptor's advice and is reported per
  file in the notebook.
- Scales. The xml gives a 20 V range and an amplification of 1000 for every channel; the
  descriptor says extracellular channels are "typically amplified 1000 times" and the
  intracellular "typically 50x". So IC is 20 V / 2^bits / 50 per step (0.0977 mV for 12-bit,
  0.0061 mV for 16-bit) and EC 20 V / 2^bits / 1000 (4.88 uV, 0.305 uV). The IC scale is
  checked in the notebook against the resting potentials of the spreadsheet IntraExtra.xls;
  the EC scale cannot be checked from the data.
- Action potential detection (Methods, "Detection of intracellular action potentials"): peaks
  of the first derivative of the membrane potential; the AP peak is where the derivative
  crosses back through zero. The derivative threshold is not given (claims file, O1); a
  standard choice is used: 10 V/s and 8 robust SD of the derivative, events 1 ms apart, and an
  AP rising at least 10 mV above the potential 1 ms before the derivative peak. Spikes within
  2 ms of an edge of an injected-current step are dropped (descriptor: "take care to not detect
  the capacitive pulse transients as spikes").
- Extracellular band (Results and Fig. 1C legend, 1 Hz to 3 kHz; claims file, O5): the files
  are wide band 1 Hz to 5 kHz (descriptor), so EC channels are low-pass filtered at 3 kHz with a
  zero-phase 4th-order Butterworth filter, a standard choice.
- Averaging (Methods: "The extracellular spikes were extracted based on the occurrence of the
  intracellular action potential"): windows from -4 to +8 ms around each AP peak sample are
  averaged. Spikes are grouped as all (O2 a), spontaneous (outside current steps, O2 b), and
  by order 1 to 5 within depolarizing steps (Fig. 4B).
- Averaged waveforms are put on a common 5 us grid by cubic interpolation (files are sampled at
  10 or 20 kHz), a standard choice for sub-sample timing that cannot change a mean by more than
  a fraction of a sample.
"""
import io
import json
import re
import zipfile

import fsspec
import numpy as np
import requests
from scipy import interpolate, signal

BUCKET = "https://crcnsarchive.s3-us-west-2.amazonaws.com"
ROOT = BUCKET + "/hc-1/live/"
WIN = (-4.0, 8.0)  # ms around the AP peak
GRID_DT = 0.005  # ms, common time grid of averaged waveforms
GRID = np.round(np.arange(WIN[0] + 0.5, WIN[1] - 0.5 + GRID_DT / 2, GRID_DT), 6)


def list_data():
    """Keys and sizes of the data set's files from the bucket listing."""
    s = requests.get(BUCKET + "/?list-type=2&prefix=hc-1/", timeout=60).text
    keys = re.findall(r"<Key>(.*?)</Key>.*?<Size>(\d+)</Size>", s)
    return [(k, int(n)) for k, n in keys]


def read_small(path):
    return requests.get(ROOT + path, timeout=60).content


def read_spreadsheet():
    import pandas as pd

    return pd.read_excel(io.BytesIO(read_small("IntraExtra.xls")), sheet_name=0)


def open_zip(folder):
    f = fsspec.open(ROOT + "Data/" + folder + ".zip", block_size=2**22).open()
    return f, zipfile.ZipFile(f)


def _tag(t, tag):
    r = re.search("<%s>(.*?)</%s>" % (tag, tag), t)
    return r.group(1) if r else None


def folder_members(z):
    """The .dat members of a zip with their xml parameters (nChannels, samplingRate, groups)."""
    names = [i.filename for i in z.infolist()]
    out = []
    for n in names:
        if not n.endswith(".dat"):
            continue
        xml = n[:-4] + ".xml"
        info = {"member": n, "size": z.getinfo(n).file_size, "xml": xml in names}
        if xml in names:
            t = z.read(xml).decode("latin1")
            info["nc"] = int(_tag(t, "nChannels"))
            info["sr"] = float(_tag(t, "samplingRate"))
            groups = re.findall(r"<group>(.*?)</group>", t, re.S)
            info["groups"] = [[int(c) for c in re.findall(r">(\d+)</channel>", g)] for g in groups]
        else:
            # d15611 and d16811 have no xml; their size fits 14 channels at 20 kHz for 750 s,
            # as the other 16-bit silicon-probe files of that period.
            info.update(nc=14, sr=20000.0, groups=[list(range(12)), [12, 13]])
        readme = [m for m in names if m.endswith("README.txt")]
        info["readme"] = z.read(readme[0]).decode("latin1") if readme else None
        out.append(info)
    return out


def animal(folder):
    return int(folder[1:-2])


def electrode(folder, nc):
    """Electrode type from the channel count: 12 or 6 EC channels are the 2x6 silicon probe
    (spreadsheet "Electrode Type"), 4 or 8 a wire tetrode (one or two)."""
    a = animal(folder)
    return "silicon probe" if a >= 156 else "tetrode"


def ec_channels(folder, info, twelve):
    nc = info["nc"]
    if not twelve:
        return [c for c in range(nc - 2)]
    a = animal(folder)
    if nc == 16:
        return list(range(8))
    if a <= 72:  # READMEs of d5331, d5611, d6811, d7111: EC channels 2 3 4 5 (one-based)
        return [1, 2, 3, 4]
    return [0, 1, 2, 3]  # README of d13521: EC channels 1 2 3 4; d813101/2 group 0-3


def scales(twelve):
    """(IC mV per step, EC uV per step, centre)."""
    if twelve:
        return 20.0 / 4096 / 50 * 1000, 20.0 / 4096 / 1000 * 1e6, 2048.0
    return 20.0 / 65536 / 50 * 1000, 20.0 / 65536 / 1000 * 1e6, 0.0


def _events(y, sr, ic_scale):
    d = np.diff(y) * ic_scale * sr / 1000.0  # V/s
    mad = np.median(np.abs(d - np.median(d))) * 1.4826 + 1e-9
    thr = max(10.0, 8 * mad)
    pk, _ = signal.find_peaks(d, height=thr, distance=max(1, int(sr * 0.001)))
    return d, pk, thr


def pick_ic(x, ec, twelve, sr):
    """IC channel: the non-EC, unclipped channel with a median below -30 mV (a
    membrane potential) and the most AP-like events (>= 10 mV)."""
    ic_scale = scales(twelve)[0]
    best, bestn, stats = None, 0, {}
    n1 = min(len(x), int(60 * sr))
    for c in range(x.shape[1]):
        if c in ec:
            continue
        y = x[:n1, c].astype(float)
        clip = np.mean((y <= 0) | (y >= 4095)) if twelve else np.mean(np.abs(y) >= 32767)
        if clip > 0.001:
            stats[c] = ("clipped", 0)
            continue
        d, pk, thr = _events(y, sr, ic_scale)
        w = int(sr * 0.0015)
        b = int(sr * 0.001)
        amp = np.array([y[p:p + w].max() - y[max(p - b, 0)] for p in pk]) * ic_scale
        n = int(np.sum(amp >= 10))
        vmed = float(np.median(y) - scales(twelve)[2]) * ic_scale
        stats[c] = (vmed, n)
        if vmed < -30 and n > bestn:
            best, bestn = c, n
    return best, stats


def current_channel(nc, ic, ec, twelve):
    """Injected current: the last channel for 16-bit files (descriptor); for 12-bit files the
    first channel after the IC channel that is not EC (channel 7 of the 8 where the IC is channel
    6, else channel 6), as the step traces show."""
    if not twelve:
        return nc - 1
    if nc == 16:
        return 9
    if ic == 6:
        return 7
    return 6


def step_mask(cur, sr):
    """Samples inside an injected-current step: deviation from the most common value (zero
    current) of more than 5 robust SD of the sample-to-sample noise and 4 steps, kept when the
    run lasts at least 5 ms. A standard choice; the descriptor gives no step timing."""
    c = cur.astype(float)
    vals, counts = np.unique(cur, return_counts=True)
    dev = c - float(vals[np.argmax(counts)])  # the most common value is taken as zero current
    dd = np.diff(c[: int(60 * sr)])
    noise = np.median(np.abs(dd - np.median(dd))) * 1.4826 / np.sqrt(2)
    on = np.abs(dev) > max(5 * noise, 4.0)
    if not on.any():
        return on, np.zeros(0, int), dev
    # keep runs of at least 5 ms
    edges = np.flatnonzero(np.diff(on.astype(np.int8)))
    starts = list(np.flatnonzero(np.diff(np.r_[0, on.astype(np.int8)]) == 1))
    ends = list(np.flatnonzero(np.diff(np.r_[on.astype(np.int8), 0]) == -1))
    keep = np.zeros_like(on)
    for s, e in zip(starts, ends):
        if e - s >= int(0.005 * sr):
            keep[s:e + 1] = True
    edges = np.flatnonzero(np.diff(keep.astype(np.int8))) + 1
    return keep, edges, dev


def process_file(z, info, folder):
    """Detect APs in one file and return per-spike features and window sums."""
    raw = z.read(info["member"])
    nc, sr = info["nc"], info["sr"]
    x = np.frombuffer(raw, np.int16)
    x = x[: len(x) // nc * nc].reshape(-1, nc)
    twelve = bool(x[: int(10 * sr)].min() >= 0 and x[: int(10 * sr)].max() <= 4095)
    ec = ec_channels(folder, info, twelve)
    ic, icstats = pick_ic(x, ec, twelve, sr)
    res = {"member": info["member"].split("/")[-1], "nc": nc, "sr": sr, "twelve": twelve,
           "ec": ec, "ic": ic, "icstats": icstats, "n_samples": len(x)}
    if ic is None:
        res["n_spikes"] = 0
        return res
    ics, ecs, centre = scales(twelve)
    v = (x[:, ic].astype(np.float64) - centre) * ics  # mV
    curc = current_channel(nc, ic, ec, twelve)
    res["cur"] = curc
    inside, edges, dev = step_mask(x[:, curc], sr)
    d, pk, thr = _events(x[:, ic].astype(float), sr, 1.0 if False else ics)
    res["deriv_threshold"] = thr
    b1 = int(round(sr * 0.001))
    w3 = int(round(sr * 0.003))
    peaks = []
    for p in pk:
        seg = d[p:p + w3]
        z0 = np.flatnonzero(seg <= 0)
        if len(z0) == 0:
            continue
        q = p + z0[0]
        if v[q] - v[max(p - b1, 0)] < 10:
            continue
        peaks.append(q)
    peaks = np.unique(np.array(peaks, int))
    if len(edges):
        dist = np.min(np.abs(peaks[:, None] - edges[None, :]), axis=1) if len(peaks) else np.zeros(0)
        peaks = peaks[dist > int(0.002 * sr)]
    i0 = int(round(WIN[0] * sr / 1000))
    i1 = int(round(WIN[1] * sr / 1000))
    peaks = peaks[(peaks + i0 >= 0) & (peaks + i1 < len(v))]
    res["n_spikes"] = len(peaks)
    res["vrest_median"] = float(np.median(v[~inside])) if (~inside).any() else float(np.median(v))
    res["duration_s"] = len(v) / sr
    res["frac_in_step"] = float(inside.mean())
    # depolarizing sign of current: the sign of dev during steps with higher mean Vm
    sign = 0
    if inside.any():
        pos = inside & (dev > 0)
        neg = inside & (dev < 0)
        mv = np.median(v[~inside])
        up = np.median(v[pos]) - mv if pos.sum() > sr * 0.01 else np.nan
        dn = np.median(v[neg]) - mv if neg.sum() > sr * 0.01 else np.nan
        if np.isfinite(up) and (not np.isfinite(dn) or up > dn):
            sign = 1
        elif np.isfinite(dn):
            sign = -1
    res["dep_sign"] = sign
    if len(peaks) == 0:
        return res
    # EC: zero-phase low-pass 3 kHz
    sos = signal.butter(4, 3000 / (sr / 2), "low", output="sos") if sr > 6000 else None
    idx = peaks[:, None] + np.arange(i0, i1 + 1)[None, :]
    icw = v[idx]  # spikes x samples, mV
    # control windows 25 ms after each AP peak (clock check: no spike expected there)
    shift = int(round(0.025 * sr))
    ok_shift = peaks + shift + i1 < len(v)
    idx_s = idx[ok_shift] + shift
    ecw = np.empty((len(peaks), len(ec), idx.shape[1]), np.float32)
    ecw_raw = np.empty_like(ecw)
    ecw_s = np.empty((len(idx_s), len(ec), idx.shape[1]), np.float32)
    for j, c in enumerate(ec):
        y = (x[:, c].astype(np.float32) - centre) * ecs
        ecw_raw[:, j, :] = y[idx]
        if sos is not None and sr > 6000:
            y = signal.sosfiltfilt(sos, y).astype(np.float32)
        ecw[:, j, :] = y[idx]
        ecw_s[:, j, :] = y[idx_s]
        del y
    # step membership and order of spikes within depolarizing steps
    dep = inside & ((dev > 0) if sign >= 0 else (dev < 0)) if sign != 0 else np.zeros_like(inside)
    in_step = inside[peaks]
    in_dep = dep[peaks]
    step_id = np.cumsum(np.r_[0, np.diff(dep.astype(np.int8)) == 1])[peaks]
    order = np.zeros(len(peaks), int)
    for sid in np.unique(step_id[in_dep]):
        m = np.flatnonzero(in_dep & (step_id == sid))
        order[m] = np.arange(1, len(m) + 1)
    isi_prev = np.r_[np.inf, np.diff(peaks) / sr * 1000]
    isi_next = np.r_[np.diff(peaks) / sr * 1000, np.inf]
    t = np.arange(i0, i1 + 1) / sr * 1000
    res["t"] = t
    res["spikes"] = {
        "time_s": peaks / sr, "in_step": in_step, "in_dep": in_dep, "order": order,
        "step_id": step_id, "isi_prev": isi_prev, "isi_next": isi_next,
    }
    res["spike_ic"] = per_spike_ic(t, icw, sr)
    res["spike_ec"] = per_spike_ec(t, ecw)
    groups = {"all": np.ones(len(peaks), bool), "spont": ~in_step}
    for k in range(1, 6):
        groups["ord%d" % k] = in_dep & (order == k)
    res["sums"] = {g: (int(m.sum()), icw[m].sum(0), ecw[m].sum(0).astype(np.float64)) for g, m in groups.items()}
    # unfiltered extracellular band as recorded (1 Hz to 5 kHz), for the Fig. 7 analysis
    res["sums"]["all_raw"] = (len(peaks), icw.sum(0), ecw_raw.sum(0).astype(np.float64))
    res["sums"]["shift"] = (int(ok_shift.sum()), icw[ok_shift].sum(0), ecw_s.sum(0).astype(np.float64))
    res["spike_ec_shift"] = per_spike_ec(t, ecw_s)
    # noise of the extracellular average: per-spike SD over the -4 to -2 ms baseline
    bl = (t >= -4) & (t <= -2)
    res["ec_base_sd"] = ecw[:, :, bl].std(axis=(0, 2)).astype(float)
    return res


def per_spike_ic(t, icw, sr):
    """Per-spike IC measures: peak (mV), pre-spike baseline (mean -3 to -1.5 ms), threshold
    (potential where dV/dt first exceeds 10 V/s before the peak), maximal rising and falling
    slopes (V/s)."""
    dv = np.diff(icw, axis=1) * sr / 1000.0
    pk = np.argmin(np.abs(t))
    peak = icw[:, pk]
    base = icw[:, (t >= -3) & (t <= -1.5)].mean(1)
    thr = np.full(len(icw), np.nan)
    for i in range(len(icw)):
        above = dv[i, :pk] > 10
        if above[-1] if len(above) else False:
            k = pk - 1
            while k > 0 and above[k - 1]:
                k -= 1
            thr[i] = icw[i, k]
    rise = dv[:, max(pk - int(sr * 0.0015), 0):pk].max(1)
    fall = dv[:, pk:pk + int(sr * 0.003)].min(1)
    return {"peak": peak, "base": base, "thr": thr, "rise": rise, "fall": fall}


def per_spike_ec(t, ecw):
    """Per-spike EC measures per channel: baseline (mean -3 to -1.5 ms), negative peak in -1 to
    +0.6 ms, positive peak in the 2.5 ms after it; amplitudes negative-to-positive (O7 a) and
    baseline-to-negative (O7 b)."""
    base = ecw[:, :, (t >= -3) & (t <= -1.5)].mean(2)
    w = (t >= -1.0) & (t <= 0.6)
    iw = np.flatnonzero(w)
    neg_i = iw[np.argmin(ecw[:, :, w], axis=2)]
    neg = np.take_along_axis(ecw, neg_i[:, :, None], 2)[:, :, 0]
    n = ecw.shape[2]
    dt = t[1] - t[0]
    span = int(round(2.5 / dt))
    pos = np.empty_like(neg)
    for j in range(ecw.shape[1]):
        for i in range(ecw.shape[0]):
            a = neg_i[i, j]
            pos[i, j] = ecw[i, j, a:min(a + span, n)].max()
    return {"base": base, "neg": neg, "pos": pos, "amp_np": pos - neg, "amp_neg": base - neg}


def summarize_cell(folder):
    """Stream every .dat file of a cell folder; return file results (without raw data)."""
    f, z = open_zip(folder)
    try:
        members = folder_members(z)
        files = []
        for info in members:
            r = process_file(z, info, folder)
            r["groups"] = info["groups"]
            r["readme"] = info["readme"]
            r["xml"] = info["xml"]
            files.append(r)
    finally:
        z.close()
        f.close()
    return {"folder": folder, "files": files}


def combine(files, group, use=None):
    """Average waveforms of a cell over its files for one spike group, on the common grid.
    Returns (n, ic[grid], ec[channels, grid]) or None. Files must share EC channel count."""
    n_tot, ic_acc, ec_acc = 0, 0.0, 0.0
    for r in files:
        if use is not None and r["member"] not in use:
            continue
        if "sums" not in r or r["sums"][group][0] == 0:
            continue
        n, ics, ecs = r["sums"][group]
        fi = interpolate.CubicSpline(r["t"], ics / n)(GRID)
        fe = interpolate.CubicSpline(r["t"], ecs / n, axis=1)(GRID)
        ic_acc = ic_acc + fi * n
        ec_acc = ec_acc + fe * n
        n_tot += n
    if n_tot == 0:
        return None
    return n_tot, ic_acc / n_tot, ec_acc / n_tot


# ---------- measures on averaged waveforms (time in ms on GRID, IC in mV, EC in uV) ----------

def ic_measures(v, t=GRID):
    """Intracellular landmarks of an averaged AP (claims file O4, O6).
    start_a: first point of the run before the peak where dV/dt > 10 V/s (O4 a);
    start_b: maximum of the second derivative in the 1.5 ms before the peak (O4 b);
    end_thr: return to the threshold potential (Vm at the start) after the peak (O4, Results);
    end_base: return to the mean Vm of the 2 ms before the start (O4, "return to baseline");
    amp_thr: peak minus threshold (O6 a); amp_base: peak minus that baseline (O6 b);
    ahp: minimum in the 5 ms after end_thr and its time; fahp: whether Vm falls below the
    threshold potential within 3 ms after end_thr (a fast AHP)."""
    dt = t[1] - t[0]
    dv = np.gradient(v, dt)  # mV/ms = V/s
    d2 = np.gradient(dv, dt)
    pk = int(np.argmax(np.where((t > -1) & (t < 1), v, -np.inf)))
    out = {"t_peak": t[pk], "peak": v[pk]}
    for key, si in (("a", None), ("b", None)):
        if key == "a":
            lo = np.searchsorted(t, t[pk] - 1.5)
            k = lo + int(np.argmax(dv[lo:pk])) if pk > lo else pk
            if dv[k] <= 10:
                si = None
            else:
                while k > 0 and dv[k - 1] > 10:
                    k -= 1
                si = k
        else:
            lo = np.searchsorted(t, t[pk] - 1.5)
            si = lo + int(np.argmax(d2[lo:pk])) if pk > lo else None
        if si is None:
            out.update({f"t_start_{key}": np.nan, f"thr_{key}": np.nan, f"t_end_thr_{key}": np.nan,
                        f"t_end_base_{key}": np.nan, f"base_{key}": np.nan,
                        f"amp_thr_{key}": np.nan, f"amp_base_{key}": np.nan})
            continue
        thr = v[si]
        bmask = (t >= t[si] - 2) & (t < t[si])
        base = v[bmask].mean()
        after = np.flatnonzero(v[pk:] <= thr)
        e1 = t[pk + after[0]] if len(after) else np.nan
        after2 = np.flatnonzero(v[pk:] <= base)
        e2 = t[pk + after2[0]] if len(after2) else np.nan
        out.update({f"t_start_{key}": t[si], f"thr_{key}": thr, f"t_end_thr_{key}": e1,
                    f"t_end_base_{key}": e2, f"base_{key}": base,
                    f"amp_thr_{key}": v[pk] - thr, f"amp_base_{key}": v[pk] - base})
    e = out["t_end_thr_a"]
    if np.isfinite(e):
        m = (t >= e) & (t <= e + 5)
        i = np.flatnonzero(m)[np.argmin(v[m])]
        out["t_ahp"], out["v_ahp"] = t[i], v[i]
        m3 = (t >= e) & (t <= e + 3)
        out["fahp"] = bool(v[m3].min() < out["thr_a"] - 0.5)
    else:
        out["t_ahp"], out["v_ahp"], out["fahp"] = np.nan, np.nan, False
    out["rise_max"] = dv[: pk + 1].max()
    out["fall_max"] = -dv[pk: pk + int(3 / dt)].min()
    return out


def ec_measures(e, noise_sd, t=GRID):
    """Extracellular landmarks of an averaged spike (claims file O4, O7).
    baseline: mean over -3 to -1.5 ms; negative peak: the most prominent trough in -1 to +0.6 ms;
    start_a: last point before the negative peak within 2 SD of the baseline noise (O4 a);
    start_b: most negative second derivative in the 1 ms before the negative peak (O4 b);
    end: maximum of the late positivity in the 2.5 ms after the negative peak;
    amp_np: negative to positive peak (O7 a); amp_neg: baseline to negative peak (O7 b)."""
    dt = t[1] - t[0]
    bm = (t >= -3) & (t <= -1.5)
    base = e[bm].mean()
    w = np.flatnonzero((t >= -1) & (t <= 0.6))
    pk, pr = signal.find_peaks(-e[w], prominence=0)
    # the most prominent trough in the window, so that a slow field trend reaching the window's
    # edge is not taken for the spike; the global minimum when there is no trough
    ni = w[pk[np.argmax(pr["prominences"])]] if len(pk) else w[np.argmin(e[w])]
    out = {"t_neg": t[ni], "neg": e[ni], "base": base, "amp_neg": base - e[ni]}
    lo = np.flatnonzero(np.abs(e[:ni] - base) <= 2 * noise_sd)
    out["t_start_a"] = t[lo[-1]] if len(lo) else np.nan
    d1 = np.gradient(e, dt)
    d2 = np.gradient(d1, dt)
    l2 = np.searchsorted(t, t[ni] - 1.0)
    out["t_start_b"] = t[l2 + int(np.argmin(d2[l2:ni]))] if ni > l2 else np.nan
    pw = np.arange(ni, min(ni + int(2.5 / dt), len(t)))
    pi = pw[np.argmax(e[pw])]
    out["t_pos"], out["pos"] = t[pi], e[pi]
    out["amp_np"] = e[pi] - e[ni]
    out["rise_slope"] = d1[ni:pi + 1].max() if pi > ni else np.nan  # positive-going phase
    out["fall_slope"] = -d1[max(ni - int(1 / dt), 0):ni + 1].min()
    out["d1"], out["d2"], out["ni"], out["pi"] = d1, d2, ni, pi
    return out


# ---------- whole data set ----------

def folders():
    """Cell folders (zip files under Data/), with their compressed sizes."""
    out = {}
    for k, n in list_data():
        if k.startswith("hc-1/live/Data/") and k.endswith(".zip"):
            out[k.split("/")[-1][:-4]] = n
    return out


def _summarize(folder):
    import os
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    return summarize_cell(folder)


def load_all(workers=3):
    """Stream and process every cell folder, `workers` folders at a time (each holds one file in
    memory at a time, up to 420 MB raw and about 1.6 GB while processing)."""
    from concurrent.futures import ProcessPoolExecutor

    sizes = folders()
    order = sorted(sizes, key=lambda f: -sizes[f])
    with ProcessPoolExecutor(workers) as ex:
        res = dict(zip(order, ex.map(_summarize, order)))
    return {f: res[f] for f in sorted(res)}


def align_trains(t1, t2, tol=0.001):
    """Fraction of the spikes of the shorter train that fall within `tol` s of a spike of the
    longer one, after the best constant offset (the mode of all pairwise differences, 1 ms bins)."""
    a, b = (t1, t2) if len(t1) >= len(t2) else (t2, t1)
    d = (b[None, :] - a[:, None]).ravel()
    h, e = np.histogram(d, bins=np.arange(d.min(), d.max() + 0.002, 0.001))
    off = e[np.argmax(h)] + 0.0005
    s = b - off
    k = np.clip(np.searchsorted(a, s), 1, len(a) - 1)
    dd = np.minimum(np.abs(a[k] - s), np.abs(a[k - 1] - s))
    return off, float(np.mean(dd < tol))


def cell_waves(files, group, drop=()):
    """Averaged waveforms of a cell for one spike group and the SD of the averaged EC noise
    (per-spike SD over -4 to -2 ms divided by the square root of the spike count)."""
    fs = [f for f in files if f["n_spikes"] > 0 and f["member"] not in drop]
    if not fs:
        return None
    ecn = max(len(f["ec"]) for f in fs)
    fs = [f for f in fs if len(f["ec"]) == ecn]
    c = combine(fs, group)
    if c is None:
        return None
    n, ic, ec = c
    var = sum(f["ec_base_sd"] ** 2 * f["sums"][group][0] for f in fs) / n
    return {"n": n, "ic": ic, "ec": ec, "noise": np.sqrt(var) / np.sqrt(n), "files": [f["member"] for f in fs]}
