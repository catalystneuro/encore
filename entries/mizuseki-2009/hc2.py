"""Loading and theta measures for CRCNS hc-2 (Mizuseki, Sirota, Pastalkova & Buzsaki 2009).

The data set hc-2 (doi:10.6080/K0Z60KZ9) holds 21 open-field sessions of three rats (ec13, ec14,
ec16) with a silicon probe in CA1. It is not versioned on CRCNS; the files read are pinned by the
MD5 sums of the data set's ``checksums.md5`` (``session_md5``).

Each session is one ``<session>.tar.gz`` in the public bucket ``crcnsarchive`` (all files but the
wideband ``.dat`` and the video). The tarball is streamed once over HTTP with ``fsspec`` and
``tarfile`` in stream mode, nothing written to disk, and reduced as it is read
(``load_session``): spike times and cluster ids of isolated units (cluster 2 and above, data
descriptor 2b), each unit's mean waveform from the ``.spk`` files, the head position from the
``.whl`` file, and one LFP channel (the CA1 pyramidal layer channel, below).

Where each parameter comes from:

- Theta band 5-11 Hz, maxima method for the phase (peak 0 and 360 degrees, trough 180), Hilbert
  and minima methods: Supplemental Experimental Procedures (SEP), paragraph "Theta periods were
  detected ...". The filter is not named (claims file, O3); a zero-phase 4th-order Butterworth
  band-pass is a standard choice.
- Theta epochs: SEP, ratio of 5-11 Hz power to the 1-4 and 12-14 Hz bands, with a manual
  adjustment that cannot be repeated, during walking/running. The paper uses EC3 LFP; hc-2 has
  no EC probe, so the CA1 pyramidal layer LFP is used (the paper's reference for rat i01, Figure
  S7 legend, and for Figure S10). The window (2 s, 1 s step), the ratio threshold
  (``THETA_RATIO``) and the running speed threshold (``SPEED_CM_S``) are not given in the paper:
  assumptions, varied in the notebook.
- CA1 pyramidal layer channel: the channel with the largest ripple-band (140-230 Hz, SEP ripple
  detection) power among sound channels, since ripples are largest in the pyramidal layer (a
  standard choice; the files do not say which channel is in the layer). See
  ``_pick_pyramidal_channel``.
- Ripples: SEP, CA1 pyramidal LFP in non-theta periods, 140-230 Hz, RMS in 17 ms windows,
  threshold 7 SD above the mean.
- Cell inclusion for circular statistics: at least 50 spikes and rate > 0.1 Hz in theta epochs,
  Rayleigh test p < 0.01 (SEP). Preferred phase = circular mean, modulation depth = mean
  resultant length.
- Instantaneous rate of a spike: the neuron's spikes in a 250 ms window centred on it,
  categories 1 to >= 10 (4 to >= 40 Hz; SEP and Figure 5 legend). Burst spikes: an ISI before or
  after < 6 ms; single spikes: both > 20 ms (SEP).
- Cell types: the paper separates hippocampal principal cells and interneurons "on the basis of
  their autocorrelograms, waveforms and mean firing rates (Skaggs et al., 1996; Csicsvari et al.,
  1999)" (SEP, Cell Type Classification) without thresholds. ``classify`` uses the
  trough-to-peak latency of the mean filtered waveform and the mean rate; its thresholds are an
  assumption (see its docstring).
"""
import re
import tarfile
import xml.etree.ElementTree as ET

import fsspec
import numpy as np
from scipy import signal

BUCKET = "https://crcnsarchive.s3-us-west-2.amazonaws.com/hc-2/"
DATASET = "crcns:hc-2/unversioned"
DOI = "10.6080/K0Z60KZ9"
FS = 20000.0  # wideband and spike time stamps, Hz (data descriptor 2a)
FS_LFP = 1250.0  # .eeg, Hz (data descriptor 1)
FS_WHL = 20000.0 / 512  # .whl, 39.06 Hz (data descriptor 4b)

# Session table of the data descriptor: session, rat, maze side (cm), reward.
SESSIONS = [
    ("ec013.527", "ec13", 180, "food"), ("ec013.528", "ec13", 180, "food"),
    ("ec013.529", "ec13", 180, "water"), ("ec013.713", "ec13", 180, "water"),
    ("ec013.714", "ec13", 180, "water"), ("ec013.754", "ec13", 180, "water"),
    ("ec013.755", "ec13", 180, "food"), ("ec013.756", "ec13", 180, "water"),
    ("ec013.757", "ec13", 180, "water"), ("ec013.808", "ec13", 180, "water"),
    ("ec013.844", "ec13", 180, "water"), ("ec014.277", "ec14", 180, "water"),
    ("ec014.333", "ec14", 180, "water"), ("ec014.793", "ec14", 120, "water"),
    ("ec014.800", "ec14", 120, "water"), ("ec015.041", "ec14", 120, "water"),
    ("ec015.047", "ec14", 120, "water"), ("ec016.397", "ec16", 180, "water"),
    ("ec016.430", "ec16", 180, "water"), ("ec016.448", "ec16", 180, "water"),
    ("ec016.582", "ec16", 180, "water"),
]
# Recording day of each session (data descriptor table); sessions of one day were clustered
# together and share cluster ids (data descriptor 2c).
DAY = {
    "ec013.527": "2006-02-02", "ec013.528": "2006-02-02", "ec013.529": "2006-02-02",
    "ec013.713": "2006-02-10", "ec013.714": "2006-02-10", "ec013.754": "2006-02-13",
    "ec013.755": "2006-02-13", "ec013.756": "2006-02-13", "ec013.757": "2006-02-13",
    "ec013.808": "2006-02-16", "ec013.844": "2006-02-18", "ec014.277": "2007-02-22",
    "ec014.333": "2007-02-25", "ec014.793": "2007-03-15", "ec014.800": "2007-03-15",
    "ec015.041": "2007-03-19", "ec015.047": "2007-03-19", "ec016.397": "2007-09-19",
    "ec016.430": "2007-09-21", "ec016.448": "2007-09-22", "ec016.582": "2007-10-01",
}

THETA_BAND = (5.0, 11.0)
THETA_RATIO = 2.0  # assumption: threshold on the theta ratio (varied in the notebook)
SPEED_CM_S = 3.0  # assumption: walking/running threshold (varied in the notebook)
RATE_BINS = np.arange(1, 11)  # spikes per 250 ms, 10 = ">= 10"


def checksums():
    """MD5 sums from the data set's checksums.md5, keyed by path below hc-2/."""
    with fsspec.open(BUCKET + "checksums.md5", "rt") as f:
        out = {}
        for line in f:
            parts = line.split()
            if len(parts) == 2:
                out[parts[1]] = parts[0]
    return out


def _ints(b):
    return np.array(b.split(), dtype=np.int64)


def _parse_xml(b):
    root = ET.fromstring(b)
    nch = int(root.find("acquisitionSystem/nChannels").text)
    groups = []
    for g in root.find("spikeDetection/channelGroups"):
        groups.append([int(c.text) for c in g.find("channels")])
    units = root.find("units")
    unit_meta = []
    if units is not None:
        for u in units:
            unit_meta.append({c.tag: (c.text or "") for c in u})
    return {"n_channels": nch, "spike_groups": groups, "units_xml": unit_meta,
            "lfp_rate": float(root.find("fieldPotentials/lfpSamplingRate").text),
            "rate": float(root.find("acquisitionSystem/samplingRate").text)}


def _waveform_means(fobj, size, labels, n_samples=32):
    """Mean waveform per cluster label (>= 2) from a .spk stream, read in chunks."""
    nspk = len(labels)
    nch = size // (2 * n_samples * nspk)
    assert nch * 2 * n_samples * nspk == size, "spk size does not match res/clu"
    good = np.unique(labels[labels >= 2])
    sums = np.zeros((len(good), n_samples, nch))
    counts = np.zeros(len(good))
    idx = np.full(labels.max() + 1, -1)
    idx[good] = np.arange(len(good))
    chunk = 50000
    start = 0
    while start < nspk:
        n = min(chunk, nspk - start)
        buf = fobj.read(n * n_samples * nch * 2)
        w = np.frombuffer(buf, dtype="<i2").reshape(n, n_samples, nch)
        lab = idx[labels[start:start + n]]
        keep = lab >= 0
        if keep.any():
            lab = lab[keep]
            order = np.argsort(lab, kind="stable")
            ws = w[keep][order].astype(np.float64)
            ls = lab[order]
            bounds = np.r_[0, np.flatnonzero(np.diff(ls)) + 1]
            sums[ls[bounds]] += np.add.reduceat(ws, bounds, axis=0)
            counts[ls[bounds]] += np.diff(np.r_[bounds, len(ls)])
        start += n
    means = sums / np.maximum(counts, 1)[:, None, None]
    return good, means


def _pick_pyramidal_channel(eeg, groups, seconds=600):
    """CA1 pyramidal layer channel: the largest 140-230 Hz RMS among channels that look sound.

    Over the first ``seconds``: a channel is left out when its LFP (below 50 Hz) correlates with
    the median of its shank at r < 0.8, or when its ripple-band RMS is above 1.5 times the median
    over channels (a noisy site, which a bare maximum picks). Both checks are standard choices,
    made after a first pass picked a noisy channel in session ec016.582.
    """
    n = min(len(eeg), int(seconds * FS_LFP))
    sos = signal.butter(4, [140, 230], btype="band", fs=FS_LFP, output="sos")
    sos_lo = signal.butter(4, 50, btype="low", fs=FS_LFP, output="sos")
    diag = {}
    for g in groups:
        seg = eeg[:n, g].astype(np.float32)
        rms = np.sqrt((signal.sosfiltfilt(sos, seg, axis=0) ** 2).mean(axis=0))
        lo = signal.sosfiltfilt(sos_lo, seg, axis=0)
        med = np.median(lo, axis=1)
        for k, c in enumerate(g):
            r = np.corrcoef(lo[:, k], med)[0, 1] if len(g) > 2 else 1.0
            diag[c] = {"ripple_rms": float(rms[k]), "r_shank": float(r)}
    m = np.median([v["ripple_rms"] for v in diag.values()])
    ok = {c: v["ripple_rms"] for c, v in diag.items() if v["r_shank"] >= 0.8 and v["ripple_rms"] <= 1.5 * m}
    for c, v in diag.items():
        v["ok"] = c in ok
        v["rel_rms"] = v["ripple_rms"] / m
    return max(ok, key=ok.get), diag


def load_session(session):
    """Stream one session's tarball and reduce it. Returns a dict (see module docstring)."""
    url = f"{BUCKET}{session}/{session}.tar.gz"
    raw = fsspec.open(url, block_size=2**25, cache_type="readahead").open()
    tf = tarfile.open(fileobj=raw, mode="r|gz", bufsize=2**22)
    clu, res, wave, members = {}, {}, {}, {}
    eeg_bytes = whl = xml = None
    for m in tf:
        if not m.isfile():
            continue
        name = m.name.rsplit("/", 1)[-1]
        members[name] = m.size
        ext = name[len(session) + 1:]
        f = tf.extractfile(m)
        if re.fullmatch(r"clu\.\d+", ext):
            c = _ints(f.read())
            clu[int(ext[4:])] = c[1:]
        elif re.fullmatch(r"res\.\d+", ext):
            res[int(ext[4:])] = _ints(f.read())
        elif re.fullmatch(r"spk\.\d+", ext):
            sh = int(ext[4:])
            wave[sh] = _waveform_means(f, m.size, clu[sh])
        elif ext == "eeg":
            eeg_bytes = f.read()
        elif ext == "whl":
            whl = np.array(f.read().split(), dtype=float).reshape(-1, 4)
        elif ext == "xml":
            xml = _parse_xml(f.read())
    raw.close()
    nch = xml["n_channels"]
    eeg = np.frombuffer(eeg_bytes, dtype="<i2").reshape(-1, nch)
    del eeg_bytes
    ch, rms = _pick_pyramidal_channel(eeg, xml["spike_groups"])
    lfp = eeg[:, ch].astype(np.float32)
    eeg_samples = len(eeg)
    del eeg
    units = []
    for sh in sorted(res):
        t, c = res[sh], clu[sh]
        assert len(t) == len(c), f"{session} shank {sh}: res and clu lengths differ"
        good, means = wave.get(sh, (np.array([], int), None))
        for k, cl in enumerate(good):
            st = t[c == cl] / FS
            units.append({"session": session, "shank": sh, "cluster": int(cl),
                          "spikes": st, "waveform": means[k]})
    return {"session": session, "units": units, "lfp": lfp, "lfp_channel": ch,
            "channel_check": rms, "whl": whl, "xml": xml, "members": members,
            "eeg_samples": eeg_samples,
            "n_noise_spikes": int(sum(((clu[s] < 2).sum() for s in clu)))}


# ---------------------------------------------------------------- behaviour and theta epochs

def position_cm(whl, side_cm):
    """Head position in cm (mean of the two LEDs), NaN where tracking failed (-1).

    The .whl file is in video pixels; the scale is not stated in the data set. It is taken from
    the extent of the tracked positions (1st to 99th percentile of each axis), set to the
    platform's side from the session table (an assumption: the rat covers the platform).
    """
    import warnings
    w = whl.copy()
    w[w < 0] = np.nan
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", RuntimeWarning)
        x = np.nanmean(w[:, [0, 2]], axis=1)
        y = np.nanmean(w[:, [1, 3]], axis=1)
    ext = max(np.nanpercentile(x, 99) - np.nanpercentile(x, 1),
              np.nanpercentile(y, 99) - np.nanpercentile(y, 1))
    scale = side_cm / ext
    return x * scale, y * scale, scale


def speed_cm_s(x, y, smooth_s=0.25):
    """Speed from positions, Gaussian smoothed (SD ``smooth_s``, a standard choice)."""
    from scipy.ndimage import gaussian_filter1d
    good = np.isfinite(x) & np.isfinite(y)
    t = np.arange(len(x))
    xi = np.interp(t, t[good], x[good])
    yi = np.interp(t, t[good], y[good])
    sd = smooth_s * FS_WHL
    xs, ys = gaussian_filter1d(xi, sd), gaussian_filter1d(yi, sd)
    v = np.hypot(np.gradient(xs), np.gradient(ys)) * FS_WHL
    v[~good] = np.nan
    return v


def theta_ratio(lfp, win_s=2.0, step_s=1.0):
    """Ratio of mean 5-11 Hz power to mean power in 1-4 and 12-14 Hz, per window (SEP)."""
    f, t, p = signal.spectrogram(lfp, fs=FS_LFP, nperseg=int(win_s * FS_LFP),
                                 noverlap=int((win_s - step_s) * FS_LFP))
    th = p[(f >= 5) & (f <= 11)].mean(axis=0)
    nb = p[((f >= 1) & (f <= 4)) | ((f >= 12) & (f <= 14))].mean(axis=0)
    return t, th / nb


def theta_mask(lfp, speed, ratio_thr=THETA_RATIO, speed_thr=SPEED_CM_S):
    """Boolean mask at the LFP rate: theta ratio above threshold and speed above threshold.

    ``speed_thr=None`` drops the speed condition. Samples without tracking are excluded when the
    speed condition is used.
    """
    t, r = theta_ratio(lfp)
    n = len(lfp)
    tl = np.arange(n) / FS_LFP
    m = np.interp(tl, t, r) > ratio_thr
    if speed_thr is not None:
        tw = np.arange(len(speed)) / FS_WHL
        v = np.interp(tl, tw, np.nan_to_num(speed, nan=-1.0))
        m &= v > speed_thr
    return m


def mask_to_epochs(mask, fs=FS_LFP, min_s=1.0):
    """Runs of True as [start, end) in seconds, at least ``min_s`` long."""
    d = np.diff(np.r_[0, mask.astype(np.int8), 0])
    s, e = np.flatnonzero(d == 1), np.flatnonzero(d == -1)
    keep = (e - s) >= min_s * fs
    return np.c_[s[keep], e[keep]] / fs


def in_epochs(t, ep):
    if len(ep) == 0:
        return np.zeros(len(t), bool)
    i = np.searchsorted(ep[:, 0], t, side="right") - 1
    return (i >= 0) & (t < ep[np.maximum(i, 0), 1])


# ---------------------------------------------------------------- theta phase

def theta_filter(lfp, band=THETA_BAND):
    sos = signal.butter(4, band, btype="band", fs=FS_LFP, output="sos")
    return signal.sosfiltfilt(sos, lfp.astype(np.float64))


def phase_extrema(y, which="max"):
    """Phase in degrees at each LFP sample by the maxima (peak 0/360) or minima (trough 180) method.

    Peaks are positive-to-negative zero crossings of dy/dt, troughs negative-to-positive ones,
    phase linearly interpolated between successive extrema (SEP, following Siapas et al. 2005).
    Samples before the first or after the last extremum are NaN.
    """
    dy = np.diff(y)
    if which == "max":
        ext = np.flatnonzero((dy[:-1] > 0) & (dy[1:] <= 0)) + 1
        offset = 0.0
    else:
        ext = np.flatnonzero((dy[:-1] < 0) & (dy[1:] >= 0)) + 1
        offset = 180.0
    ph = np.full(len(y), np.nan)
    idx = np.arange(len(y))
    k = np.searchsorted(ext, idx, side="right") - 1
    ok = (k >= 0) & (k < len(ext) - 1)
    a, b = ext[k[ok]], ext[k[ok] + 1]
    ph[ok] = (offset + 360.0 * (idx[ok] - a) / (b - a)) % 360.0
    return ph, ext


def phase_hilbert(y):
    """Phase in degrees from the Hilbert transform; 0 at peaks, 180 at troughs."""
    from scipy.fft import next_fast_len
    n = len(y)
    h = signal.hilbert(y, N=next_fast_len(n))[:n]
    return np.degrees(np.angle(h)) % 360.0


def unwrap_phase(ph):
    """Unwrapped phase in degrees (NaN where ``ph`` is NaN), for interpolation at spike times."""
    good = np.isfinite(ph)
    un = np.full(len(ph), np.nan)
    un[good] = np.degrees(np.unwrap(np.radians(ph[good])))
    return un


def spike_phase(t, un):
    """Phase of each spike by linear interpolation of the unwrapped LFP phase ``un``."""
    i0 = np.clip(np.floor(t * FS_LFP).astype(int), 0, len(un) - 2)
    frac = t * FS_LFP - i0
    out = (un[i0] * (1 - frac) + un[i0 + 1] * frac) % 360.0
    return out


# ---------------------------------------------------------------- circular statistics

def circ_stats(deg):
    """Circular mean (degrees), mean resultant length R, Rayleigh p (Zar's approximation)."""
    deg = deg[np.isfinite(deg)]
    n = len(deg)
    if n == 0:
        return np.nan, np.nan, np.nan
    z = np.exp(1j * np.radians(deg)).mean()
    R = abs(z)
    mu = np.degrees(np.angle(z)) % 360.0
    p = np.exp(np.sqrt(1 + 4 * n + 4 * (n ** 2 - (n * R) ** 2)) - (1 + 2 * n))
    return mu, R, min(max(p, 0.0), 1.0)


def circ_diff(a, b):
    """a - b wrapped to (-180, 180]."""
    return (np.asarray(a) - np.asarray(b) + 180.0) % 360.0 - 180.0


def inst_rate_count(t, window=0.25):
    """Number of the neuron's spikes in a 250 ms window centred on each spike (itself included)."""
    lo = np.searchsorted(t, t - window / 2, side="left")
    hi = np.searchsorted(t, t + window / 2, side="right")
    return hi - lo


def isi_groups(t):
    """Burst spikes (an ISI before or after < 6 ms) and single spikes (both ISIs > 20 ms)."""
    isi = np.diff(t)
    before = np.r_[np.inf, isi]
    after = np.r_[isi, np.inf]
    burst = (before < 0.006) | (after < 0.006)
    single = (before > 0.020) & (after > 0.020)
    return burst, single


# ---------------------------------------------------------------- waveforms and cell types

def waveform_features(mean_wave):
    """Trough-to-peak latency (ms) and asymmetry index on the channel of largest trough.

    The spike files hold the 0.8-5 kHz filtered waveform (data descriptor), the waveform the
    paper uses for these features (SEP, Cell Type Classification). Asymmetry index is
    (b - a) / (b + a), a and b the baseline-to-peak amplitudes before and after the trough
    (Figure 2C; Sirota et al. 2008).
    """
    w = mean_wave - np.median(mean_wave[:4], axis=0)
    ch = int(np.argmin(w.min(axis=0)))
    x = w[:, ch]
    tr = int(np.argmin(x))
    a = x[:tr].max() if tr > 0 else 0.0
    post = x[tr:]
    pk = tr + int(np.argmax(post))
    b = post.max()
    t2p = (pk - tr) / FS * 1000.0
    asym = (b - a) / (b + a) if (b + a) > 0 else np.nan
    return t2p, asym, ch


def classify(t2p_ms, rate_hz, t2p_thr=0.4, rate_thr=10.0):
    """Putative interneuron when the trough-to-peak latency is short or the rate is high.

    Assumption: the paper gives no thresholds for hippocampal cells. Narrow spikes (trough to
    peak < 0.4 ms at 20 kHz) or a mean rate above 10 Hz mark interneurons, following the two
    criteria of the methods the paper cites (Csicsvari et al., 1999: waveform and rate). The
    notebook shows the distribution and the counts under other thresholds.
    """
    t2p_ms, rate_hz = np.asarray(t2p_ms), np.asarray(rate_hz)
    return np.where((t2p_ms < t2p_thr) | (rate_hz > rate_thr), "int", "pyr")


# ---------------------------------------------------------------- ripples

def detect_ripples(lfp, nontheta_mask, sd_thr=7.0):
    """Ripple power peaks: 140-230 Hz, RMS in 17 ms windows, 7 SD above the mean (SEP).

    Mean and SD of the RMS are taken over non-theta samples; events are runs above threshold
    within non-theta samples, at least 30 ms apart (a standard choice for merging). Returns
    peak times in seconds.
    """
    sos = signal.butter(4, [140, 230], btype="band", fs=FS_LFP, output="sos")
    y = signal.sosfiltfilt(sos, lfp.astype(np.float64))
    w = int(round(0.017 * FS_LFP))
    rms = np.sqrt(np.convolve(y ** 2, np.ones(w) / w, mode="same"))
    mu, sd = rms[nontheta_mask].mean(), rms[nontheta_mask].std()
    above = (rms > mu + sd_thr * sd) & nontheta_mask
    d = np.diff(np.r_[0, above.astype(np.int8), 0])
    s, e = np.flatnonzero(d == 1), np.flatnonzero(d == -1)
    peaks = np.array([a + int(np.argmax(rms[a:b])) for a, b in zip(s, e)], dtype=int)
    if len(peaks) > 1:
        keep = np.r_[True, np.diff(peaks) > 0.03 * FS_LFP]
        peaks = peaks[keep]
    return peaks / FS_LFP


# ---------------------------------------------------------------- per-session reduction to theta spikes

def theta_session(d, side_cm, ratio_thr=THETA_RATIO, speed_thr=SPEED_CM_S):
    """Theta epochs, theta phase and per-spike variables for one loaded session.

    Returns ``units`` (one dict per isolated unit with its waveform features, mean rate over the
    session, theta spike count and rate, and phases) and session-level values. Spikes are those
    in theta epochs; the instantaneous rate and ISI groups are computed on all the unit's spikes
    and then restricted to theta epochs.
    """
    x, y, scale = position_cm(d["whl"], side_cm)
    v = speed_cm_s(x, y)
    mask = theta_mask(d["lfp"], v, ratio_thr, speed_thr)
    ep = mask_to_epochs(mask)
    theta_s = float((ep[:, 1] - ep[:, 0]).sum()) if len(ep) else 0.0
    yth = theta_filter(d["lfp"])
    ph_max, peaks = phase_extrema(yth, "max")
    ph_max = unwrap_phase(ph_max)
    ph_min = unwrap_phase(phase_extrema(yth, "min")[0])
    ph_hil = unwrap_phase(phase_hilbert(yth))
    dur = len(d["lfp"]) / FS_LFP
    out = []
    for u in d["units"]:
        t = u["spikes"]
        t2p, asym, ch = waveform_features(u["waveform"])
        cnt = inst_rate_count(t)
        burst, single = isi_groups(t)
        it = in_epochs(t, ep)
        tt = t[it]
        out.append({
            "session": d["session"], "shank": u["shank"], "cluster": u["cluster"],
            "n_spikes": len(t), "rate": len(t) / dur, "t2p": t2p, "asym": asym,
            "burst_index": float((np.diff(t) < 0.006).mean()) if len(t) > 1 else np.nan,
            "n_theta": len(tt), "theta_rate": len(tt) / theta_s if theta_s > 0 else 0.0,
            "t": tt,
            "ph": spike_phase(tt, ph_max), "ph_min": spike_phase(tt, ph_min),
            "ph_hil": spike_phase(tt, ph_hil),
            "count": np.minimum(cnt[it], 10), "burst": burst[it], "single": single[it],
        })
    return {"units": out, "theta_s": theta_s, "duration_s": dur, "epochs": ep,
            "scale_cm_px": scale, "speed": v, "theta_mask": mask,
            "theta_freq": FS_LFP / np.median(np.diff(peaks)) if len(peaks) > 1 else np.nan}
