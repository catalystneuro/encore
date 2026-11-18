"""Loading and measures for CRCNS aa-3 (Danish, Aronov & Fee 2017, PLoS ONE 12(6), e0169568).

The data set is two tar.gz archives in the public CRCNS bucket. They are streamed once each
(gzip cannot be read out of order) and reduced as they are read; nothing is written to disk.

Where each parameter comes from:

- MUA: the neural signal rectified and smoothed with a 2 ms (SD) Gaussian (paper, Methods,
  "Chronic neural recordings in Uva", and claims file header "Multiunit activity"). It is
  sampled at 1 kHz after smoothing, a standard choice that cannot change a result at the
  frequencies the claims use (below 60 Hz).
- Sound amplitude, reading (a): audio band-passed 1 to 4 kHz, squared, smoothed with a 2.5 ms
  (SD) Gaussian, 10 log10 (Methods, "Sound analysis"). Reading (c): audio rectified and smoothed
  with a 2 ms Gaussian (Methods, "Rhythmicity"). Reading (b), the first without the log, is
  computed from (a). The band-pass is a 4th-order Butterworth run forwards and backwards; the
  paper does not give the filter, a standard choice.
- Neural signal of the stimulation files: snippets around each stimulus artefact (samples at
  the converter's +-10 V rail) are kept at 40 kHz, from 5 ms before to 25 ms after.
- Bouts: syllables separated by gaps of at most 300 ms (Methods, "Sound analysis") or 350 ms
  (Methods, "Song rhythmicity"), as the claim says.
- Maturity index: Methods, "Maturity index" (claims file, fig2g-maturity-index-drop).
- Goodness of fit Gamma: Methods, "Sound analysis", paragraph 3, and the claims file's readings
  (fig2f-closer-to-exponential).
- Multitaper spectra: tapers [TW K] = [2 1] (claims file header "Spectra").
"""

import hashlib
import io
import re
import tarfile
import urllib.request

import numpy as np
import scipy.io as sio
from scipy import signal

BUCKET = "https://crcnsarchive.s3-us-west-2.amazonaws.com/aa-3/live/"
EPHYS_TAR = "Electrophysiology.tar.gz"
LESION_TAR = "Lesion_Experiments.tar.gz"
DOI = "10.6080/K0GQ6VP4"
DATASET = "aa-3"
VERSION = "unversioned"  # CRCNS data sets are not versioned; the archives' MD5 sums pin what was read
FS_OUT = 1000  # Hz, rate of the reduced traces


def iter_tar(name, select=None):
    """Yield (member name, bytes) for each file of a tar.gz in the bucket, streamed in order.

    `select(name)` decides which members are read; the others are skipped (still decompressed).
    """
    with urllib.request.urlopen(BUCKET + name, timeout=300) as raw:  # a stalled read raises, not hangs
        with tarfile.open(fileobj=raw, mode="r|gz") as t:
            for m in t:
                if not m.isfile():
                    continue
                if select is not None and not select(m.name):
                    continue
                yield m.name, t.extractfile(m).read()


def read_dat(b):
    """Parse an AA_daq .dat file (formats -4 and -3), following daq_readDatafile.m of the data set.

    Returns (data, fs, native type). Values are in volts (native scale and offset applied).
    """
    h = np.frombuffer(b[: 8 * 64], "<f8")
    fmt = h[0]
    if fmt not in (-4, -3):
        raise ValueError(f"unknown format {fmt}")
    i = 13
    nch = int(h[i]); i += 1
    i += nch  # hardware channel numbers
    scale = h[i: i + 2 * nch: 2]; offset = h[i + 1: i + 2 * nch: 2]; i += 2 * nch
    typ = ""
    while h[i] != fmt:
        typ += chr(int(h[i])); i += 1
    i += 1
    start, stime = h[i], h[i + 1]; i += 2
    dt = {"double": "<f8", "int16": "<i2", "int32": "<i4"}[typ]
    bs = np.dtype(dt).itemsize
    p0 = i * 8
    if fmt == -3:
        endn, endt = np.frombuffer(b[-16:], "<f8")
    else:
        raw = np.frombuffer(b[p0: p0 + ((len(b) - p0) // bs) * bs], dt)
        cand = np.where(raw == -4)[0]
        k = next(k for k in cand[::-1] if k + 2 < len(raw) and raw[k + 1] == -4 and raw[k + 2] == -4)
        q = p0 + (k + 3) * bs
        endn, endt = np.frombuffer(b[q: q + 16], "<f8")
    n_room = (len(b) - p0 - 16) // (nch * bs)
    if np.isfinite(endn) and 0 < endn - start + 1 <= n_room + 1:
        n = int(endn - start + 1)
        fs = 1.0 / ((endt - stime) / (endn - start))
    else:
        # The closing sample number and time are not valid (seen in some Uva4 files): take every
        # sample before the last 16 bytes and mark the rate as unknown (NaN).
        n, fs = n_room, np.nan
    d = np.frombuffer(b[p0: p0 + n * nch * bs], dt).reshape(n, nch).astype(np.float64)
    d = d * scale + offset
    return (d[:, 0] if nch == 1 else d), fs, typ


def gauss_kernel(sd):
    """Normalized Gaussian kernel with SD `sd` samples, to +-4 SD."""
    h = int(np.ceil(4 * sd))
    k = np.exp(-0.5 * (np.arange(-h, h + 1) / sd) ** 2)
    return k / k.sum()


def gauss_smooth(x, sd):
    """Gaussian smoothing with SD `sd` samples (kernel to +-4 SD), by overlap-add convolution."""
    return signal.oaconvolve(x, gauss_kernel(sd), mode="same")


def gauss_smooth_circular(x, sd):
    """Gaussian smoothing as gauss_smooth, treating x as periodic (no edge effects)."""
    h = int(np.ceil(4 * sd))
    return gauss_smooth(np.r_[x[-h:], x, x[:h]], sd)[h: h + len(x)]


def _down(x, fs):
    """Sample a smoothed trace at FS_OUT by taking the nearest sample (no further filtering)."""
    n = int(len(x) * FS_OUT / fs)
    idx = np.minimum(np.round(np.arange(n) * fs / FS_OUT).astype(int), len(x) - 1)
    return x[idx].astype(np.float32)


def mua(x, fs):
    """Rectify and smooth with a 2 ms (SD) Gaussian (Methods); returned at 1 kHz."""
    return _down(gauss_smooth(np.abs(x - np.median(x)), 0.002 * fs), fs)


def amplitudes(x, fs):
    """Sound amplitude readings (a) dB (1-4 kHz, squared, 2.5 ms Gaussian) and (c) rectified, 2 ms."""
    x = x - np.mean(x)
    sos = signal.butter(4, [1000, 4000], btype="bandpass", fs=fs, output="sos")
    y = signal.sosfiltfilt(sos, x)
    p = gauss_smooth(y * y, 0.0025 * fs)
    db = 10 * np.log10(np.maximum(p, 1e-20))
    rect = gauss_smooth(np.abs(x), 0.002 * fs)
    return _down(db, fs), _down(rect, fs)


FEATURES = ["amplitude", "pitch_goodness", "wiener_entropy", "gravity_center", "am", "fm"]


def sap_features(x, fs, win=0.0093, fmin=860.0, fmax=8600.0, chunk=20000):
    """Six spectral song features at 1 kHz, after the definitions of Sound Analysis Pro
    (Tchernichovski et al. 2000), which the claims file adopts as an assumption
    (spectral-features-weak). Each 1 ms frame is a 9.3 ms window (SAP's default length) with a
    Hann taper (SAP uses two Slepian tapers; a standard choice), power between 860 Hz and 8.6 kHz
    (the band of the paper's Maturity index section; SAP's band is set by the user):
      amplitude: 10 log10 of the summed power;
      Wiener entropy: log of the ratio of the geometric to the arithmetic mean of the power;
      gravity center: the power-weighted mean frequency (Hz);
      pitch goodness: the largest cepstral peak at quefrencies of 0.5 to 2.5 ms (pitch 400 Hz to
        2 kHz);
      AM: the time derivative of log power summed over frequency (per ms);
      FM: arctan of the largest time derivative of log power over the largest frequency
        derivative, in degrees.
    The window is centred on each 1 ms sample. Returns {feature: float32 array}."""
    nwin = int(round(win * fs)); step = fs / FS_OUT
    n = int(len(x) * FS_OUT / fs)
    f = np.fft.rfftfreq(nwin, 1 / fs)
    band = (f >= fmin) & (f <= fmax)
    tap = np.hanning(nwin)
    xp = np.r_[np.zeros(nwin // 2), x - np.mean(x), np.zeros(nwin)]
    q = np.arange(nwin) / fs
    qband = (q >= 0.0005) & (q <= 0.0025)
    out = {k: np.empty(n, np.float32) for k in FEATURES}
    prev_last = None
    for a in range(0, n, chunk):
        idx = np.round(np.arange(a, min(n, a + chunk)) * step).astype(int)
        fr = xp[idx[:, None] + np.arange(nwin)[None, :]] * tap
        P = np.abs(np.fft.rfft(fr, axis=1)) ** 2 + 1e-20
        Pb = P[:, band]
        L = np.log(Pb)
        out["amplitude"][a:a + len(idx)] = 10 * np.log10(Pb.sum(1))
        out["wiener_entropy"][a:a + len(idx)] = L.mean(1) - np.log(Pb.mean(1))
        out["gravity_center"][a:a + len(idx)] = (Pb * f[band]).sum(1) / Pb.sum(1)
        cep = np.abs(np.fft.irfft(np.log(P), nwin, axis=1))
        out["pitch_goodness"][a:a + len(idx)] = cep[:, qband].max(1)
        Lp = np.vstack([L[:1] if prev_last is None else prev_last, L])
        dt = np.diff(Lp, axis=0)
        df = np.abs(np.diff(L, axis=1)).max(1)
        out["am"][a:a + len(idx)] = dt.sum(1)
        out["fm"][a:a + len(idx)] = np.degrees(np.arctan(np.abs(dt).max(1) / np.maximum(df, 1e-12)))
        prev_last = L[-1:]
    return out


def _dbase(b):
    d = sio.loadmat(io.BytesIO(b), squeeze_me=True, struct_as_record=False)["dbase"]
    files = []
    nf = len(d.SoundFiles)
    names = list(np.atleast_1d(d.Properties.Names[0])) if np.size(d.Properties.Names) else []
    for k in range(nf):
        st = np.asarray(d.SegmentTimes[k], dtype=float)
        st = st.reshape(-1, 2) if st.size else np.zeros((0, 2))
        sel = np.atleast_1d(np.asarray(d.SegmentIsSelected[k], dtype=float)).ravel()
        if sel.size != len(st):
            sel = np.zeros(len(st))
        tt = d.SegmentTitles[k]
        if len(st) == 1:
            tt = [tt]
        titles = [t if isinstance(t, str) else "" for t in (list(np.atleast_1d(tt)) if len(st) else [])]
        if len(titles) != len(st):
            titles = [""] * len(st)
        props = {}
        if names:
            v = np.atleast_1d(d.Properties.Values[k])
            props = {n: bool(int(x)) for n, x in zip(names, v)}
        files.append({
            "index": k + 1, "sound_file": d.SoundFiles[k].name, "time": float(np.atleast_1d(d.Times)[k]),
            "length": int(np.atleast_1d(d.FileLength)[k]), "seg": st, "selected": sel.astype(bool),
            "titles": titles, "props": props,
        })
    # Channels whose file lists are not empty (process_recording.m of the data set reads these as
    # the valid neural channels), with the name of each list's first file.
    chan_files = {k + 1: np.atleast_1d(c)[0].name
                  for k, c in enumerate(np.atleast_1d(getattr(d, "ChannelFiles", [])))
                  if np.size(c)}  # the lesion analysis files have no neural channels
    return {"fs": float(d.Fs), "files": files, "property_names": names, "channel_files": chan_files,
            "event_sources": [str(s) for s in np.atleast_1d(d.EventSources)] if np.size(d.EventSources) else [],
            "event_detectors": [str(s) for s in np.atleast_1d(getattr(d, "EventDetectors", []))]}


_DAT = re.compile(r"Electrophysiology/(Bird_[^/]+)/([^/]+)/(.+)_d(\d+)_(\d{8}T\d{6})chan(\d+)\.dat$")


def _stim_snippets(x, fs):
    """Snippets (-5 to +25 ms) of a neural channel around the onsets of saturating artefacts."""
    sat = np.abs(x) >= 9.9
    if sat.sum() == 0:
        return None
    idx = np.where(sat)[0]
    on = idx[np.r_[True, np.diff(idx) > int(0.2 * fs)]]
    pre, post = int(0.005 * fs), int(0.025 * fs)
    on = on[(on > pre) & (on + post < len(x))]
    if len(on) < 3:
        return None
    return np.stack([x[o - pre: o + post] for o in on]).astype(np.float32), on


def load_ephys():
    """Stream Electrophysiology.tar.gz once and reduce every recording.

    Returns a dict with:
      recs: {(bird, day, file number): {"mua": (3, n) float32 for the three neural channels in
             channel order, "chans": channel numbers, "amp_db", "amp_rect": (n,), "fs": raw rate,
             "n_raw": samples, "stim": {chan: (snippets, onsets)}}}
      dbase: {(bird, day): parsed analysis file}
      sheets: {file name: bytes of each spreadsheet}
      md5: {member name: md5 of its bytes}, nested_md5: same for the nested 2013-10-06.tar.gz
    """
    raw = {}
    out = {"recs": {}, "dbase": {}, "sheets": {}, "md5": {}, "nested_md5": {}, "sizes": {}}

    def finish(key):
        chans = raw.pop(key)
        neural = sorted(c for c in chans if c != min(chans))
        sound_ch = min(chans)
        x, fs = chans[sound_ch]
        db, rect = amplitudes(x, fs)
        m = np.stack([mua(chans[c][0], chans[c][1]) for c in neural])
        n = min(len(db), m.shape[1])
        stim = {}
        for c in neural:
            s = _stim_snippets(chans[c][0], chans[c][1])
            if s is not None:
                stim[c] = s
        feats = {k: v[:n] for k, v in sap_features(x, fs).items()}
        out["recs"][key] = {"mua": m[:, :n], "chans": neural, "amp_db": db[:n], "amp_rect": rect[:n],
                            "fs": fs, "n_raw": len(x), "stim": stim, "features": feats}

    for name, b in iter_tar(EPHYS_TAR):
        out["md5"][name] = hashlib.md5(b).hexdigest()
        out["sizes"][name] = len(b)
        if name.endswith(".xlsx"):
            out["sheets"][name.split("/")[-1]] = b
        elif name.endswith(".tar.gz"):
            with tarfile.open(fileobj=io.BytesIO(b), mode="r:gz") as t2:
                for m2 in t2:
                    if m2.isfile():
                        out["nested_md5"][m2.name] = hashlib.md5(t2.extractfile(m2).read()).hexdigest()
        elif name.endswith(".mat"):
            parts = name.split("/")
            out["dbase"][(parts[1], parts[2])] = _dbase(b)
        else:
            mm = _DAT.search(name)
            if not mm:
                continue
            key = (mm[1], mm[2], int(mm[4]))
            d, fs, _ = read_dat(b)
            if not np.isfinite(fs):
                out.setdefault("bad_tail", []).append(name)
                fs = 40000.0  # the rate of every other file and of the data description
            raw.setdefault(key, {})[int(mm[6])] = (d, fs)
            if len(raw[key]) == 4:
                finish(key)
    for key in list(raw):
        if len(raw[key]) >= 2:
            finish(key)
    return out


# ---------------------------------------------------------------- lesion data

def load_lesion_dbases():
    """First pass over Lesion_Experiments.tar.gz: the analysis files (segmentations) and file list."""
    out = {"dbase": {}, "syllgaps": {}, "wavs": {}, "md5": {}, "other": {}}
    for name, b in iter_tar(LESION_TAR, select=lambda n: n.endswith(".mat")):
        parts = name.split("/")
        key = (parts[1], parts[2].lower())
        out["md5"][name] = hashlib.md5(b).hexdigest()
        if parts[-1] == "analysis_bout.mat":
            out["dbase"][key] = _dbase(b)
        elif parts[-1] == "SyllGaps.mat":
            m = sio.loadmat(io.BytesIO(b), squeeze_me=True)
            out["syllgaps"][key] = {"durs": np.asarray(m["durs"], float), "gaps": np.asarray(m["gaps"], float)}
        else:
            # Vector clustering files (not described by the data descriptor); only their size and
            # checksum are kept, to find copies.
            out["other"][name] = {"bytes": len(b)}
    return out


def read_wav(b):
    from scipy.io import wavfile
    fs, x = wavfile.read(io.BytesIO(b))
    if x.ndim > 1:
        x = x[:, 0]
    return fs, x


def load_lesion_audio(keep):
    """Second pass: per wav file, amplitude traces at 1 kHz, and the raw audio of chosen spans.

    `keep`: {(bird, condition, wav name): [(start, stop) samples]} spans whose raw audio is returned.
    """
    out = {"amp": {}, "raw": {}, "fs": {}, "md5": {}}
    for name, b in iter_tar(LESION_TAR, select=lambda n: n.endswith(".wav")):
        parts = name.split("/")
        key = (parts[1], parts[2].lower(), parts[3])
        out["md5"][name] = hashlib.md5(b).hexdigest()
        fs, x = read_wav(b)
        out["fs"][key] = fs
        x = x.astype(np.float64)
        db, rect = amplitudes(x, fs)
        out["amp"][key] = (db, rect)
        for (a, z) in keep.get(key, []):
            out["raw"][(key, a, z)] = x[a:z].astype(np.float32)
    return out


def bouts_from_segments(seg, max_gap):
    """Group syllables (n x 2 array, same units as max_gap) into bouts by gaps <= max_gap.

    Returns a list of index arrays into seg (sorted by onset)."""
    if len(seg) == 0:
        return []
    order = np.argsort(seg[:, 0])
    s = seg[order]
    gaps = s[1:, 0] - s[:-1, 1]
    cuts = np.where(gaps > max_gap)[0] + 1
    return [order[g] for g in np.split(np.arange(len(s)), cuts)]


# ---------------------------------------------------------------- measures

def gamma_readings(durs):
    """Lilliefors statistic of an exponential fit by maximum likelihood (claims file readings).

    D is the Kolmogorov-Smirnov distance between the empirical CDF and the exponential CDF with
    the fitted mean. Reading (a): D * sqrt(n); reading (b): D / critical value at alpha 0.05,
    taking the large-sample Lilliefors critical value for the exponential, 1.06 / sqrt(n)
    (Lilliefors 1969, Table 1, n > 30).
    """
    x = np.sort(np.asarray(durs, float))
    n = len(x)
    cdf = 1 - np.exp(-x / x.mean())
    i = np.arange(1, n + 1)
    d = max(np.max(i / n - cdf), np.max(cdf - (i - 1) / n))
    return {"D": d, "n": n, "a": d * np.sqrt(n), "b": d / (1.06 / np.sqrt(n))}


def dpss_spectrum(x, fs, nw=2, k=1, nfft=None):
    """Multitaper power spectrum (Chronux-style, [TW K] = [2 1] by default)."""
    n = len(x)
    tap = signal.windows.dpss(n, nw, Kmax=k, return_ratios=False).reshape(k, n)
    nfft = nfft or max(2 ** int(np.ceil(np.log2(n))), n)
    X = np.fft.rfft(tap * x[None, :], nfft, axis=1)
    f = np.fft.rfftfreq(nfft, 1 / fs)
    return f, X


def spectrogram_mt(x, fs, win=0.010, step=0.001, nw=1.5, k=2, fmin=860, fmax=8600):
    """Multitaper spectrogram (Methods, Maturity index: 2 tapers, 10 ms window, 1 ms step,
    bandwidth parameter 1.5), power between 860 Hz and 8.6 kHz; returns (n slices, n freqs)."""
    nwin = int(round(win * fs)); nstep = int(round(step * fs))
    tap = signal.windows.dpss(nwin, nw, Kmax=k)
    nsl = 1 + (len(x) - nwin) // nstep
    if nsl < 1:
        return np.zeros((0, 0))
    idx = np.arange(nwin)[None, :] + nstep * np.arange(nsl)[:, None]
    seg = x[idx]
    seg = seg - seg.mean(1, keepdims=True)
    f = np.fft.rfftfreq(nwin, 1 / fs)
    band = (f >= fmin) & (f <= fmax)
    P = np.zeros((nsl, band.sum()))
    for t in tap:
        P += np.abs(np.fft.rfft(seg * t[None, :], axis=1)[:, band]) ** 2
    return P / k


def maturity_index(specs, min_overlap=10):
    """Mean over distinct bout pairs of the maximum of the lag correlation function.

    Each spectrogram slice is z-scored across frequency, so that the product of two slices,
    divided by the number of frequencies, is their Pearson correlation. The lag correlation
    function is the sum of the slice-by-slice correlation matrix along each diagonal, divided
    (reading a) by the length of the shorter bout, or (reading b) by the number of slice pairs on
    that diagonal (the overlap), keeping lags with at least `min_overlap` slices.
    Returns (MI reading a, MI reading b).
    """
    Z = []
    for s in specs:
        z = s - s.mean(1, keepdims=True)
        z = z / np.maximum(np.linalg.norm(z, axis=1, keepdims=True), 1e-12)
        Z.append(z)
    L = max(len(z) for z in Z)
    nfft = 2 ** int(np.ceil(np.log2(2 * L)))
    F = [np.fft.rfft(z, nfft, axis=0) for z in Z]
    va, vb = [], []
    for i in range(len(Z)):
        for j in range(i + 1, len(Z)):
            cc = np.fft.irfft((F[i] * np.conj(F[j])).sum(1), nfft)
            ni, nj = len(Z[i]), len(Z[j])
            # lags: index l >= 0 is z_i[t + l] . z_j[t]; negative lags wrap around
            lags = np.r_[np.arange(0, ni), np.arange(-(nj - 1), 0)]
            vals = np.r_[cc[:ni], cc[nfft - (nj - 1):]]
            ov = np.minimum(ni - np.maximum(lags, 0), nj + np.minimum(lags, 0))
            ov = np.minimum(ov, np.minimum(ni, nj))
            va.append(vals.max() / min(ni, nj))
            ok = ov >= min_overlap
            vb.append((vals[ok] / ov[ok]).max())
    return float(np.mean(va)), float(np.mean(vb))


# ---------------------------------------------------------------- song rhythm (Fig 2E)

NFFT_RHYTHM = 4096  # 1 kHz traces; 0.24 Hz grid, a standard choice


def bout_spectrum(trace):
    """Song rhythm spectrum of one bout (Methods, Song rhythmicity): mean-subtracted, detrended,
    one Slepian taper with time half-bandwidth 2, FFT, squared magnitude normalized by length."""
    # least-squares linear detrend, as signal.detrend, written out for speed (the nulls call it
    # millions of times)
    y = trace - trace.mean()
    t = np.arange(len(y)) - (len(y) - 1) / 2
    y = y - y.mean() - t * (t @ y) / (t @ t)
    tap = tapers(len(y)).ravel()
    X = np.fft.rfft(y * tap, NFFT_RHYTHM)
    return np.abs(X) ** 2 / len(y)


def synthetic_bout(n, syl_mean, gap_logmu, gap_logsd, lev_syl, lev_gap, rng):
    """A synthetic bout of n ms: syllables with exponential durations (mean syl_mean ms) and gaps
    with log-normal durations, at constant syllable and gap levels, smoothed with the 2.5 ms
    Gaussian of the amplitude (claims file, fig2e-rhythmicity-drop, null reading a)."""
    out = np.empty(n)
    t = 0
    on = True
    while t < n:
        d = rng.exponential(syl_mean) if on else rng.lognormal(gap_logmu, gap_logsd)
        d = max(int(round(d)), 1)
        out[t: t + d] = lev_syl if on else lev_gap
        t += d
        on = not on
    return np.convolve(out, gauss_kernel(2.5), mode="same")  # as gauss_smooth; direct, faster for short traces


# ---------------------------------------------------------------- electrophysiology tables

OUTSIDE_FLAGS = ("above Uva", "below Uva", "above", "?")  # file properties marking sites outside Uva


def sheet_table(sheets):
    """Recording notes and depths from the birds' spreadsheets, one row per (sheet, recording)."""
    import pandas as pd
    rows = []
    day_of_sheet = {("b871.xlsx", 0): "2013-09-08", ("b871.xlsx", 1): "2013-09-09",
                    ("Orange150.xlsx", 0): "2013-10-05", ("Orange150.xlsx", 1): "2013-10-06",
                    ("Uva4.xlsx", 0): "2007-07-25"}
    bird_of = {"b871.xlsx": "Bird_1-b871", "Orange150.xlsx": "Bird_2-Orange150", "Uva4.xlsx": "Bird_3-Uva4"}
    for name, b in sheets.items():
        x = pd.read_excel(io.BytesIO(b), sheet_name=None)
        for si, (tab, v) in enumerate(x.items()):
            for _, r in v.iterrows():
                if not np.isfinite(pd.to_numeric(r["Recording"], errors="coerce")):
                    continue
                depth = pd.to_numeric(r.get("Depth (estimated)"), errors="coerce")
                if not np.isfinite(depth):
                    depth = pd.to_numeric(r.get("Depth (actual)"), errors="coerce")
                note = " ".join(str(r[c]) for c in v.columns[4:] if str(r[c]) != "nan")
                rows.append({"bird": bird_of[name], "day": day_of_sheet[(name, si)], "tab": tab,
                             "file": int(r["Recording"]), "depth": depth, "note": note})
    return pd.DataFrame(rows)


def file_table(eph):
    """One row per recording: bird, day, file, number of segments, labels, flags and properties."""
    import pandas as pd
    rows = []
    for (bird, day), db in eph["dbase"].items():
        for f in db["files"]:
            key = (bird, day, f["index"])
            r = eph["recs"].get(key)
            titles = np.array(f["titles"], dtype=object)
            sel = f["selected"]
            rows.append({"bird": bird, "day": day, "file": f["index"], "loaded": r is not None,
                         "seconds": r["mua"].shape[1] / FS_OUT if r is not None else np.nan,
                         "n_seg": len(f["seg"]), "n_selected": int(sel.sum()),
                         "n_song_syl": int(np.sum(sel & ~np.isin(titles, ["i", "k", ""]))) if len(sel) else 0,
                         "n_intro": int(np.sum(sel & (titles == "i"))) if len(sel) else 0,
                         "n_call": int(np.sum(sel & (titles == "k"))) if len(sel) else 0,
                         "outside": any(f["props"].get(p, False) for p in OUTSIDE_FLAGS),
                         "props": ",".join(k for k, v in f["props"].items() if v),
                         "stim_artefacts": bool(r is not None and len(r["stim"]) > 0)})
    return pd.DataFrame(rows)


def events(eph, bird, fs_seg=None):
    """Vocal events of one bird, in ms on each file's 1 kHz trace.

    Returns a list of dicts per file with: key, on, off, title, selected (all segments), and the
    bouts (gap <= 300 ms, Methods, Sound analysis) over all segments."""
    out = []
    for (b, day), db in eph["dbase"].items():
        if b != bird:
            continue
        fs = db["fs"]
        for f in db["files"]:
            key = (b, day, f["index"])
            if key not in eph["recs"] or len(f["seg"]) == 0:
                continue
            seg = f["seg"] / fs * 1000.0
            order = np.argsort(seg[:, 0])
            seg = seg[order]
            titles = np.array(f["titles"], dtype=object)[order]
            sel = f["selected"][order]
            bouts = bouts_from_segments(seg, 300.0)
            out.append({"key": key, "on": seg[:, 0], "off": seg[:, 1], "title": titles, "sel": sel,
                        "bouts": [(seg[bb, 0].min(), seg[bb, 1].max(), np.sort(bb)) for bb in bouts],
                        "props": f["props"]})
    return out


def aligned(trace, times, pre, post):
    """Rows of trace around each time (ms), from -pre to +post ms; times too close to an edge are dropped."""
    t = np.round(np.asarray(times)).astype(int)
    ok = (t - pre >= 0) & (t + post < len(trace))
    idx = t[ok][:, None] + np.arange(-pre, post + 1)[None, :]
    return trace[idx], ok


def shuffle_band(pool, n_events, pre, post, n_shuffle, rng, q=(2.5, 97.5)):
    """Shuffled baseline (claims file header, reading a): averages of `n_events` windows at random
    times drawn from `pool` (list of (trace, allowed times array)), `n_shuffle` times.

    Returns the mean shuffled average (the average level), and the q-percentiles of the shuffles'
    minima and maxima over the window."""
    sizes = np.array([len(a) for _, a in pool], float)
    p = sizes / sizes.sum()
    mins, maxs, means = [], [], []
    for _ in range(n_shuffle):
        which = rng.choice(len(pool), n_events, p=p)
        acc = np.zeros(pre + post + 1)
        for w in np.unique(which):
            tr, allowed = pool[w]
            ts = rng.choice(allowed, np.sum(which == w))
            acc += aligned(tr, ts, pre, post)[0].sum(0)
        avg = acc / n_events
        means.append(avg.mean()); mins.append(avg.min()); maxs.append(avg.max())
    return float(np.mean(means)), np.percentile(mins, q[0]), np.percentile(maxs, q[1])


def crossing_before(avg, lags, ref, level, direction, search=(-100, 0)):
    """Extreme of avg in the search window (max for up, min for down), and the earliest time of the
    unbroken run beyond `level` that contains it. Returns (time of extreme, start of run or nan)."""
    w = (lags >= search[0]) & (lags <= search[1])
    seg = avg[w]; lw = lags[w]
    i = int(np.argmax(seg) if direction == "up" else np.argmin(seg))
    beyond = (avg > level) if direction == "up" else (avg < level)
    j = np.where(lags == lw[i])[0][0]
    if not beyond[j]:
        return float(lw[i]), np.nan
    while j > 0 and beyond[j - 1]:
        j -= 1
    return float(lw[i]), float(lags[j])


def warp(trace, src_points, dst_points):
    """Piecewise linear time warping (Methods, Time warping): the trace between successive source
    alignment points (ms) is resampled onto the template's intervals."""
    out = []
    for k in range(len(dst_points) - 1):
        a, b = src_points[k], src_points[k + 1]
        n = int(round(dst_points[k + 1] - dst_points[k]))
        t = np.linspace(a, b, n, endpoint=False)
        out.append(np.interp(t, np.arange(len(trace)), trace))
    return np.concatenate(out)


_TAPERS = {}


def tapers(n, nw=2, k=1):
    """Slepian tapers of length n (cached)."""
    if (n, nw, k) not in _TAPERS:
        _TAPERS[(n, nw, k)] = signal.windows.dpss(n, nw, Kmax=k).reshape(k, -1)
    return _TAPERS[(n, nw, k)]


def mt_fft(x, nfft, nw=2, k=1):
    """Tapered FFTs of the rows of x (Chronux-style, [TW K] = [2 1])."""
    x = np.atleast_2d(x)
    tap = tapers(x.shape[1], nw, k)
    xs = x - x.mean(1, keepdims=True)
    return np.fft.rfft(xs[:, None, :] * tap[None], nfft, axis=2)  # (rows, tapers, freqs)


def coherency(X, Y):
    """Trial-averaged coherency of tapered FFTs X, Y (rows, tapers, freqs), as Chronux coherencyc
    (S12 = mean of conj(J1) J2, so the phase is that of the second signal relative to the first)."""
    s12 = (np.conj(X) * Y).mean((0, 1))
    s1 = (np.abs(X) ** 2).mean((0, 1)); s2 = (np.abs(Y) ** 2).mean((0, 1))
    return s12 / np.sqrt(s1 * s2)


def shifted_ffts(segs, nfft, rng):
    """Tapered FFTs of segments each circularly shifted by a random amount (one taper), batched."""
    M = np.zeros((len(segs), nfft))
    for i, s in enumerate(segs):
        y = np.roll(s, rng.integers(len(s)))
        M[i, :len(s)] = (y - y.mean()) * tapers(len(s))[0]
    return np.fft.rfft(M, axis=1)[:, None, :]


def scrambled_ffts(segs, nfft, rng):
    """Tapered FFTs of segments whose samples are randomly permuted and smoothed again with the
    2 ms Gaussian (null of the long-syllable spectra, Methods, Rhythmicity paragraph 2).

    The permuted samples are smoothed circularly (padded with their own other end), so that the
    smoothing adds no dip at the window's edges; the real MUA was smoothed on the whole trace
    and has no such edges."""
    M = np.zeros((len(segs), nfft))
    for i, s in enumerate(segs):
        y = gauss_smooth_circular(rng.permutation(s), 2.0)
        M[i, :len(s)] = (y - y.mean()) * tapers(len(s))[0]
    return np.fft.rfft(M, axis=1)[:, None, :]
