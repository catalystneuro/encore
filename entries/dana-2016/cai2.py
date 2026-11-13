"""Loading and measures for CRCNS data set cai-2 (Dana et al. 2016, eLife 5:e12727, Figure 4).

cai-2 holds simultaneous loose-seal cell-attached recordings and two-photon imaging of L2/3
neurons in mouse V1 expressing jRGECO1a (30 Hz frames) or jRCaMP1a (15 Hz frames). Each
recording is a MATLAB file inside one of two tar.gz archives in the public S3 bucket
crcnsarchive. The archives are streamed (decompressed as they are read, never written to disk)
and each recording is reduced, as it is read, to the soma and neuropil fluorescence, the frame
times and the detected spike times. The 10 kHz ephys traces are dropped after hashing them.

Where each parameter comes from:

- NEUROPIL_R = 0.7: Methods ("Simultaneous electrophysiology ...", paragraph 2, via the claims
  file's method summary) and the data set's description; also cont_ratio in the data set's script
  data_analysis_for_CRCNS_jRGECO1a.m.
- BIN_S (n-AP time bins): Methods, paragraph 3 ("jRGECO1a: 100 ms for 2APs and increasing by
  25 ms ... up to 250 ms for 8APs; jRCaMP1a: 150 ms for 2APs and increasing 50 ms ... up to
  350 ms for 6-8 APs") and the Figure 4d legend. For 1 AP the bin only bounds the next spike
  under reading (b); it is the 2 AP bin, as in the script (bin(1) = bin(2) = 100 ms).
- Isolation readings of the claim fig4d-event-counts: (a) more than 1 s before the first and
  after the last spike, (b) more than 1 s before the first spike only. The data set's script uses
  1 s before and 0.8 s after (interval_pre, interval_post), needs a spike on each side, and
  drops events after sample 3.15e6 (315 s); it is run as the reading "script".
- NOISE_S (noise bins, 4 s jRGECO1a and 5 s jRCaMP1a): Figure 4e legend. Readings of the claim:
  (i) consecutive non-overlapping bins in each spike-free stretch, (ii) the same in stretches
  shortened by 1 s at each end; "script" is find_no_event.m: one trace per gap between spikes
  longer than the bin, at its midpoint.
- F0 = mean of the 10 frames before the first spike: Methods, paragraph 2. "Before" is taken
  as frames whose time stamp precedes the spike (a standard choice; the script takes the frame
  nearest the spike as frame 0, which the "script" segment reading keeps).
- Projected segments (claim fig4e-jrgeco1a-1ap-detection): (a) frames from the first spike over
  the noise-bin length, (b) the same with the 10 baseline frames, (c) frames from the first
  spike over 1 s. Segment lengths use the nominal frame rates (30 and 15 Hz, Methods) so that
  every trace has the same number of frames; the recordings run at 29.6 to 30.0 and 14.9 to
  15.0 Hz. "script": the data set's script, 70 frames around the frame nearest the event,
  interpolated ten-fold, of which samples 1 to 300 (10 frames before to 20 frames after) are
  kept, F0 from the first 100 samples, and noise traces with any |dF/F0| >= 0.3 dropped.
- Templates (i) the mean of all event traces (Methods), (ii) leave-one-out (claim's reading).
- Detection rate: fraction of event projections above the 95th percentile of the noise
  projections (claim criterion; the script uses the 99th, shown as a variant).
- d-prime readings (claim fig4df): (i) (mean_s - mean_n) / sqrt((var_s + var_n) / 2), which is
  also the script's formula, (ii) (mean_s - mean_n) / sd_n.
- Kinetics (claim fig4g): 2 AP events with no spike in the 2 s before (Methods, paragraph 3);
  an exponential A exp(-(t - t_peak) / tau) fitted from the peak (claim's reading) to the first
  spike plus the 2 AP bin plus the post-event isolation (1 s, or 0.8 s for the script reading;
  1 s for reading (b)), so inside the spike-free interval (a standard choice, the paper gives
  no end); the 16 traces with the smallest RMS residual kept
  (claim's reading of "small fitting error"). Half decay (a) tau ln 2 or (b) peak to half peak
  on the trace; half rise from the first spike to half peak, by linear interpolation (claim).
"""
import hashlib
import io
import re
import tarfile

import fsspec
import numpy as np
import scipy.io as sio
from scipy.optimize import curve_fit

BUCKET = "https://crcnsarchive.s3-us-west-2.amazonaws.com/cai-2/live"
ARCHIVES = {"jRGECO1a": "data/jRGECO1a_data.tar.gz", "jRCaMP1a": "data/jRCAMP1a_data.tar.gz"}
NEUROPIL_R = 0.7
NOMINAL_FPS = {"jRGECO1a": 30.0, "jRCaMP1a": 15.0}
NOISE_S = {"jRGECO1a": 4.0, "jRCaMP1a": 5.0}
BIN_S = {
    "jRGECO1a": {1: 0.100, 2: 0.100, 3: 0.125, 4: 0.150, 5: 0.175, 6: 0.200, 7: 0.225, 8: 0.250},
    "jRCaMP1a": {1: 0.150, 2: 0.150, 3: 0.200, 4: 0.250, 5: 0.300, 6: 0.350, 7: 0.350, 8: 0.350},
}
ISOLATION = {"a": (1.0, 1.0), "b": (1.0, None), "script": (1.0, 0.8)}
SCRIPT_LAST_SAMPLE = 3.15e6  # script: ind_isolate(ind_isolate > 3.15e6) = []
FS_EPHYS = 10000.0


class _HashingReader(io.RawIOBase):
    """File wrapper that keeps an MD5 of every byte read, to check against checksums.md5."""

    def __init__(self, f):
        self.f = f
        self.md5 = hashlib.md5()
        self.nbytes = 0

    def readable(self):
        return True

    def readinto(self, b):
        data = self.f.read(len(b))
        n = len(data)
        b[:n] = data
        self.md5.update(data)
        self.nbytes += n
        return n

    def drain(self):
        while True:
            data = self.f.read(2**22)
            if not data:
                break
            self.md5.update(data)
            self.nbytes += len(data)


def published_md5():
    """The data set's checksums.md5, as a dict from path to sum."""
    with fsspec.open(f"{BUCKET}/checksums.md5", "rt") as f:
        return {p: s for s, p in (line.split() for line in f if line.strip())}


def parse_name(name):
    m = re.search(r"data_(\d{8})_cell(\d+)_(\d+)(?:_part(\d+))?\.mat$", name)
    date, cell, rec, part = m.groups()
    return dict(date=date, cell=f"{date}_cell{cell}", recording=int(rec), part=int(part) if part else None)


def _reduce(name, raw):
    d = sio.loadmat(io.BytesIO(raw), squeeze_me=True, struct_as_record=False)
    o = d["obj"]
    h = o.timeSeriesArrayHash
    v = h.value
    keys = [str(k) for k in h.keyNames]
    spikes = v[4].valueMatrix
    te = v[4].time
    idx = np.flatnonzero(spikes)
    rec = dict(
        file=name.split("/")[-1],
        indicator=str(o.indicator),
        keys=keys,
        descr=[str(x) for x in h.descr],
        time_units=[int(x.timeUnit) for x in v],
        trial_time_unit=int(o.trialTimeUnit),
        roi=np.asarray(v[0].valueMatrix, float),
        neuropil=np.asarray(v[1].valueMatrix, float),
        tf=np.asarray(v[0].time, float),
        tf_neuropil_same=bool(np.array_equal(v[0].time, v[1].time)),
        ephys_t0=float(te[0]),
        ephys_t1=float(te[-1]),
        ephys_n=int(len(te)),
        ephys_dt=(float(np.diff(te).min()), float(np.diff(te).max())),
        ephys_same_clock=bool(np.array_equal(v[2].time, te) and np.array_equal(v[3].time, te)),
        spike_values=sorted(np.unique(spikes).tolist()),
        spikes=te[idx].astype(float),
        spike_sample=idx + 1,  # 1-based sample index, as in the MATLAB script
        raw_ephys_range=(float(v[2].valueMatrix.min()), float(v[2].valueMatrix.max())),
        filt_ephys_range=(float(v[3].valueMatrix.min()), float(v[3].valueMatrix.max())),
        md5_roi=hashlib.md5(np.asarray(v[0].valueMatrix).tobytes()).hexdigest(),
        md5_raw_ephys=hashlib.md5(np.asarray(v[2].valueMatrix).tobytes()).hexdigest(),
        md5_member=hashlib.md5(raw).hexdigest(),
    )
    rec.update(parse_name(name))
    return rec


def stream_archive(indicator):
    """Read one archive as a stream and return (recordings, md5 of the archive, bytes, other members)."""
    url = f"{BUCKET}/{ARCHIVES[indicator]}"
    recs, others = [], []
    with fsspec.open(url, "rb", block_size=2**22) as f:
        hr = _HashingReader(f)
        buf = io.BufferedReader(hr, buffer_size=2**22)
        with tarfile.open(fileobj=buf, mode="r|gz") as tf:
            for m in tf:
                if not m.isfile():
                    continue
                if not m.name.endswith(".mat"):
                    others.append(m.name)
                    continue
                raw = tf.extractfile(m).read()
                recs.append(_reduce(m.name, raw))
                del raw
        buf.read()
        hr.drain()
    return recs, hr.md5.hexdigest(), hr.nbytes, others


# ---------------------------------------------------------------- events


def fps(rec):
    return 1.0 / np.median(np.diff(rec["tf"]))


def nspike_events(rec, n, bin_s, reading, pre_override=None):
    """First-spike times of n-AP events under an isolation reading ('a', 'b' or 'script').

    An n-AP event: n consecutive spikes, last minus first below bin_s, isolated from earlier
    spikes by more than `pre` and (when post is set) from later ones by more than `post`.
    Readings 'a' and 'b' treat the start and end of the recording like a spike (an event needs
    the isolation interval inside the recording); 'b' requires the next spike outside the bin.
    'script' follows find_nspike_event.m: a spike is needed on each side, and events whose first
    spike is past sample 3.15e6 are dropped.
    """
    pre, post = ISOLATION[reading]
    if pre_override is not None:
        pre = pre_override
    s = rec["spikes"]
    t0, t1 = rec["ephys_t0"], rec["ephys_t1"]
    out = []
    for i in range(len(s) - n + 1):
        j = i + n - 1
        if not (s[j] - s[i] < bin_s):
            continue
        if reading == "script":
            if i == 0 or j + 1 >= len(s):
                continue
            if rec["spike_sample"][i] > SCRIPT_LAST_SAMPLE:
                continue
        prev = s[i - 1] if i > 0 else t0
        if not (s[i] - prev > pre):
            continue
        if post is not None:
            nxt = s[j + 1] if j + 1 < len(s) else t1
            if not (nxt - s[j] > post):
                continue
        elif j + 1 < len(s) and s[j + 1] - s[i] < bin_s:
            continue
        out.append(s[i])
    return np.array(out)


def noise_events(rec, length, reading):
    """Start times (or, for 'script', midpoints) of spike-free noise periods."""
    s = rec["spikes"]
    t0, t1 = rec["ephys_t0"], rec["ephys_t1"]
    if reading == "script":
        out = []
        for i in range(len(s) - 1):
            if s[i + 1] - s[i] > length:
                mid = 0.5 * (s[i] + s[i + 1])
                if (mid - t0) * FS_EPHYS + 1 <= SCRIPT_LAST_SAMPLE:
                    out.append(mid)
        return np.array(out)
    edges = np.concatenate([[t0], s, [t1]])
    pad = 0.0 if reading == "i" else 1.0
    out = []
    for a, b in zip(edges[:-1], edges[1:]):
        a2, b2 = a + pad, b - pad
        k = int(np.floor((b2 - a2) / length)) if b2 > a2 else 0
        out.extend(a2 + length * np.arange(k))
    return np.array(out)


# ---------------------------------------------------------------- traces


def corrected_f(rec):
    return rec["roi"] - NEUROPIL_R * rec["neuropil"]


def segment_traces(rec, times, segment, indicator, noise=False):
    """dF/F0 traces for events at `times`. Returns (traces, peak-window traces, n dropped).

    segment 'a', 'b', 'c' as in the module docstring; 'script' is the script's interpolated
    300-sample trace (for noise traces it also drops traces with |dF/F0| >= 0.3).
    """
    F = corrected_f(rec)
    tf = rec["tf"]
    nf = len(F)
    fr = NOMINAL_FPS[indicator]
    L = int(round(NOISE_S[indicator] * fr))
    one_s = int(round(fr))
    traces, dropped = [], 0
    for t in times:
        if segment == "script":
            idx = int(np.argmin(np.abs(tf - t)))
            if idx < 10 or idx + 60 > nf:
                dropped += 1
                continue
            sl = slice(idx - 10, idx + 60)
            tt_frames = tf[sl] - t
            tspace = np.mean(np.diff(tt_frames))
            tt = np.arange(-100, 591) * tspace / 10
            y = np.interp(tt, tt_frames, F[sl])
            y = y[:300]
            f0 = y[:100].mean()
            dff = (y - f0) / f0
            if noise and (dff.max() >= 0.3 or dff.min() <= -0.3):
                dropped += 1
                continue
            traces.append(dff)
            continue
        k0 = int(np.searchsorted(tf, t, side="right"))
        n_after = L if segment in ("a", "b") else one_s
        if k0 - 10 < 0 or k0 + n_after > nf:
            dropped += 1
            continue
        f0 = F[k0 - 10:k0].mean()
        start = k0 - 10 if segment == "b" else k0
        traces.append((F[start:k0 + n_after] - f0) / f0)
    return np.array(traces), dropped


def peak_dff(rec, times, indicator, window):
    """Peak dF/F0 after the first spike: window '1s' (1 s) or 'seg' (the noise-bin length)."""
    F = corrected_f(rec)
    tf = rec["tf"]
    fr = NOMINAL_FPS[indicator]
    n_after = int(round(fr)) if window == "1s" else int(round(NOISE_S[indicator] * fr))
    out = []
    for t in times:
        k0 = int(np.searchsorted(tf, t, side="right"))
        if k0 - 10 < 0 or k0 + n_after > len(F):
            continue
        f0 = F[k0 - 10:k0].mean()
        out.append(((F[k0:k0 + n_after] - f0) / f0).max())
    return np.array(out)


def unit(v):
    v = v - v.mean()
    return v / np.linalg.norm(v)


def projections(sig, noise, template="all"):
    """Projections of event and noise traces on the unit event template."""
    if template == "all":
        u = unit(sig.mean(0))
        return sig @ u, noise @ u
    # leave-one-out: each event scored on the template of the others; noise on the full template
    tot = sig.sum(0)
    ps = np.array([sig[i] @ unit((tot - sig[i]) / (len(sig) - 1)) for i in range(len(sig))])
    return ps, noise @ unit(sig.mean(0))


def detection_rate(ps, pn, pct=95.0):
    return float(np.mean(ps > np.percentile(pn, pct)))


def balanced_accuracy(ps, pn, pct=95.0):
    th = np.percentile(pn, pct)
    return float(0.5 * (np.mean(ps > th) + np.mean(pn <= th)))


def dprime(ps, pn, reading="i"):
    if reading == "i":
        return float((ps.mean() - pn.mean()) / np.sqrt(0.5 * (ps.var(ddof=1) + pn.var(ddof=1))))
    return float((ps.mean() - pn.mean()) / pn.std(ddof=1))


# ---------------------------------------------------------------- kinetics


def _expdecay(t, a, tau):
    return a * np.exp(-t / tau)


def kinetics(rec, times, indicator, post_s):
    """Per 2 AP event: half rise, fitted tau, trace half decay and RMS residual of the fit.

    The fit runs from the peak (maximum within 1 s of the first spike) to the first spike plus
    the bin plus post_s, a window inside the isolation interval for readings (a) and script.
    """
    F = corrected_f(rec)
    tf = rec["tf"]
    fr = NOMINAL_FPS[indicator]
    out = []
    for t in times:
        k0 = int(np.searchsorted(tf, t, side="right"))
        kend = int(np.searchsorted(tf, t + BIN_S[indicator][2] + post_s, side="right"))
        if k0 - 10 < 0 or kend > len(F):
            continue
        f0 = F[k0 - 10:k0].mean()
        y = (F[k0 - 1:kend] - f0) / f0  # frame before the spike, then frames after it
        tt = tf[k0 - 1:kend] - t
        win = int(round(fr)) + 1
        kp = int(np.argmax(y[1:win])) + 1
        peak = y[kp]
        if peak <= 0:
            continue
        # half rise: first crossing of peak/2 on the way up
        kr = next(k for k in range(1, kp + 1) if y[k] >= peak / 2)
        y0, y1, x0, x1 = y[kr - 1], y[kr], tt[kr - 1], tt[kr]
        x_half = x0 + (peak / 2 - y0) * (x1 - x0) / (y1 - y0) if y1 != y0 else x1
        rise = max(x_half, 0.0)
        # decay from the peak
        td, yd = tt[kp:] - tt[kp], y[kp:]
        if len(td) < 4:
            continue
        try:
            (a, tau), _ = curve_fit(_expdecay, td, yd, p0=(peak, 0.3), bounds=([0, 1e-3], [np.inf, 20]))
        except RuntimeError:
            continue
        rms = float(np.sqrt(np.mean((yd - _expdecay(td, a, tau)) ** 2)))
        below = np.flatnonzero(yd <= peak / 2)
        if len(below):
            kb = below[0]
            x0, x1, y0, y1 = td[kb - 1], td[kb], yd[kb - 1], yd[kb]
            decay_trace = x0 + (y0 - peak / 2) * (x1 - x0) / (y0 - y1)
        else:
            decay_trace = np.nan
        out.append(dict(rise=rise, tau=tau, decay_fit=tau * np.log(2), decay_trace=decay_trace, rms=rms, peak=peak))
    return out
