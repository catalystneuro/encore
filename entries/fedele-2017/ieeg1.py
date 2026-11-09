"""Loading and measures for CRCNS ieeg-1 (Fedele et al. 2017, Sci Rep 7:13836).

The data set is twenty tar.gz files, one per patient, under
https://crcnsarchive.s3-us-west-2.amazonaws.com/ieeg-1/live/data/. Each holds one
MATLAB v5 file per 5-minute interval, ``pat_ii_night_jj_interval_kk.mat``, with a
struct ``data`` (fields in the data description: x, label, BipChOrder,
label_bipolar, R, FR, FRandR, fs, night, interval, Rec_timestamp, Lag_seconds).
A gzip stream cannot be read at an offset, so every file is streamed once from
start to end (``scan_patient``) and reduced, as it loads, to what the claims use:
the metadata, the event tables, the peak-to-peak amplitude of every ripple and
fast ripple, a check of the event timing against the signal, and a short
snippet of the bipolar signal around every FRandR event. Nothing is written to
disk.

Where each parameter comes from:

- Bipolar montage: ``x[BipChOrder[0]] - x[BipChOrder[1]]`` (1-based), as in the
  data set's own DB_HFO_create_bipolar.m (scripts.zip).
- Band-pass filters: the data set's FIR_2kHz.mat (scripts.zip; ``Rb``, ``FRb``,
  denominators 1), applied forward and backward as in its view_data.m
  (``filtfilt``). The paper, Methods "Prospective definition of HFOs": ripples
  80-240 Hz, FR 250-490 Hz, FIR equiripple. The forward-backward filter is
  computed as one convolution with ``conv(b, b[::-1])`` on the signal padded
  by odd reflection; it differs from Matlab's filtfilt only in the start-up
  transient at the ends of the 5-minute interval (standard choice, cannot
  change a result).
- Amplitude of an event: maximum minus minimum within [start, end] of the
  event (claim hfo-amplitudes, readings (a) filtered and (b) unfiltered).
- HFO rate: events per minute (Table S1, Fig. 3A of the paper; the detector
  code in detector.zip, Get_HFO_Analysis_Results_All_Channels.m, computes
  ``n / duration * 60``).
- HFO area: channels whose rate exceeds the 95th percentile of the patient's
  channel rates, percentile by Matlab prctile.m (Methods, "Definition of the
  HFO area by rate thresholding"); ``prctile_matlab`` below implements its
  default method.
- Normalised scalar product: cosine of the two rate vectors (claims file,
  opening comment); permutation null with 5000 permutations and the 97.5th
  percentile (Methods, "Test-retest reliability").
- FRandR snippets: 0.8 s of the unfiltered bipolar signal centred on the
  FRandR midpoint (standard choice: wide enough to hold the 0.6 s window of
  the Methods, "Spectral analysis", centred on either the FRandR or the FR
  midpoint).
"""
from __future__ import annotations

import hashlib
import io
import re
import tarfile
import urllib.request
import xml.etree.ElementTree as ET
import zipfile

import fsspec
import numpy as np
import scipy.io
from scipy.signal import oaconvolve

DATASET = "ieeg-1"          # CRCNS data set
VERSION = "unversioned"     # CRCNS data sets are not versioned (docs/archives.md)
BUCKET = "https://crcnsarchive.s3-us-west-2.amazonaws.com/ieeg-1/live/"
DATASET_DOI = "10.6080/K06Q1VD5"
FS = 2000
SNIP = 1600  # samples kept around each FRandR midpoint (0.8 s)
SUPPLEMENT_URL = ("https://static-content.springer.com/esm/art%3A10.1038%2Fs41598-017-13064-1/"
                  "MediaObjects/41598_2017_13064_MOESM1_ESM.pdf")
SUPPLEMENT_MD5 = "1a5b656563fa749a6d2d9c1a86268d8d"
PMC_XML_URL = "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5653833/fullTextXML"


# ---------------------------------------------------------------- archive files
def read_bytes(url):
    with fsspec.open(url).open() as f:
        return f.read()


def checksums():
    """The data set's checksums.md5, as {path: md5}."""
    txt = read_bytes(BUCKET + "checksums.md5").decode()
    return {p: m for m, p in (l.split() for l in txt.strip().splitlines())}


def load_filters():
    """Rb and FRb from the data set's scripts.zip/FIR_2kHz.mat (Ra = FRa = 1)."""
    with fsspec.open(BUCKET + "scripts.zip").open() as f:
        z = zipfile.ZipFile(f)
        m = scipy.io.loadmat(io.BytesIO(z.read("scripts/FIR_2kHz.mat")), squeeze_me=True,
                             struct_as_record=False)["filter"]
    assert np.all(np.atleast_1d(m.Ra) == 1) and np.all(np.atleast_1d(m.FRa) == 1)
    return {"R": np.asarray(m.Rb, float), "FR": np.asarray(m.FRb, float)}


def filtfilt_fir(x, b):
    """Zero-phase FIR filtering of the rows of x (see module docstring)."""
    h = np.convolve(b, b[::-1])
    pad = 3 * len(b)
    left = 2 * x[:, :1] - x[:, pad:0:-1]
    right = 2 * x[:, -1:] - x[:, -2:-pad - 2:-1]
    xp = np.concatenate([left, x, right], axis=1)
    y = oaconvolve(xp, h[None, :], mode="same", axes=1)
    return y[:, pad:-pad]


class _HashingReader(io.RawIOBase):
    """A file wrapper that computes the MD5 of what is read through it."""

    def __init__(self, f):
        self.f, self.md5, self.n = f, hashlib.md5(), 0

    def readable(self):
        return True

    def readinto(self, b):
        data = self.f.read(len(b))
        self.md5.update(data)
        self.n += len(data)
        b[:len(data)] = data
        return len(data)

    def drain(self):
        while self.read(1 << 22):
            pass


def _event_amplitudes(sig, filt, ev):
    """Peak-to-peak of filtered and raw bipolar signal inside each event."""
    out = np.full((len(ev), 2), np.nan)
    for i, (c, s, e) in enumerate(ev):
        if e < s:
            continue
        out[i, 0] = np.ptp(filt[c, s:e + 1])
        out[i, 1] = np.ptp(sig[c, s:e + 1])
    return out


def _timing_terms(filt, ev, shift):
    """Band power of the filtered signal inside each event, at the marked time
    and with the event shifted by ``shift`` samples (circularly)."""
    n = filt.shape[1]
    p0, p1 = np.empty(len(ev)), np.empty(len(ev))
    for i, (c, s, e) in enumerate(ev):
        idx = np.arange(s, e + 1)
        p0[i] = np.mean(filt[c, idx % n] ** 2)
        p1[i] = np.mean(filt[c, (idx + shift) % n] ** 2)
    return p0, p1


def scan_interval(d, filters):
    """Reduce one interval's struct to what the claims need."""
    x = np.asarray(d.x, dtype=np.float64)
    bco = np.atleast_2d(np.asarray(d.BipChOrder, int))
    labels_bip = [str(s) for s in np.atleast_1d(d.label_bipolar)]
    bip = x[bco[0] - 1] - x[bco[1] - 1]
    del x
    rec = {
        "patient": int(d.patient_number), "night": int(d.night), "interval": int(d.interval),
        "nch": int(d.nch), "n_rows_x": int(np.shape(d.x)[0]), "n_samples": int(np.shape(d.x)[1]),
        "fs": int(d.fs), "labels": [str(s) for s in np.atleast_1d(d.label)],
        "labels_bip": labels_bip, "bipchorder": bco,
        "rec_timestamp": str(d.Rec_timestamp), "lag_seconds": int(d.Lag_seconds),
        "x_range": (float(np.min(d.x)), float(np.max(d.x))),
        "x_fingerprint": hashlib.md5(np.asarray(d.x)[:, :20000].tobytes()).hexdigest(),
        "bip_median_abs": float(np.median(np.abs(bip[:, ::50]))),
    }
    d.x = None
    events = {}
    for k in ("R", "FR", "FRandR"):
        a = np.asarray(getattr(d, k), dtype=float).reshape(-1, 3)
        rec[k + "_nonint"] = int(np.sum(a != np.round(a)))
        ev = np.round(a).astype(int)
        ev[:, 0] -= 1                      # channel to 0-based
        ev[:, 1:] -= 1                     # samples to 0-based
        events[k] = ev
        rec[k] = ev
    n = bip.shape[1]
    for k in ("R", "FR", "FRandR"):
        ev = events[k]
        ok = (ev[:, 0] >= 0) & (ev[:, 0] < bip.shape[0]) & (ev[:, 1] >= 0) & (ev[:, 2] < n)
        rec[k + "_out_of_range"] = int(np.sum(~ok))
    # filtered signal, a few channels at a time to bound memory
    for b in ("R", "FR"):
        ev = events[b]
        amp = np.full((len(ev), 2), np.nan)
        p_true, p_shift = [], []
        for c0 in range(0, bip.shape[0], 8):
            chans = np.arange(c0, min(c0 + 8, bip.shape[0]))
            filt = filtfilt_fir(bip[chans], filters[b])
            sel = np.flatnonzero((ev[:, 0] >= c0) & (ev[:, 0] < c0 + 8))
            if len(sel):
                sub = ev[sel].copy()
                sub[:, 0] -= c0
                amp[sel] = _event_amplitudes(bip[chans], filt, sub)
                t = _timing_terms(filt, sub, FS)
                p_true.append(t[0])
                p_shift.append(t[1])
            del filt
        rec["amp_" + b] = amp
        # timing: band power inside the events, at the marked time and shifted by 1 s
        if p_true:
            p0, p1 = np.concatenate(p_true), np.concatenate(p_shift)
            rec["timing_" + b] = (float(np.median(p0)), float(np.median(p1)), float(np.mean(p0 > p1)))
        else:
            rec["timing_" + b] = (np.nan, np.nan, np.nan)
    # FRandR snippets of the unfiltered bipolar signal
    ev = events["FRandR"]
    snips = np.zeros((len(ev), SNIP), np.float32)
    for i, (c, s, e) in enumerate(ev):
        mid = (s + e) // 2
        lo = mid - SNIP // 2
        idx = np.clip(np.arange(lo, lo + SNIP), 0, n - 1)
        snips[i] = bip[c, idx]
    rec["frandr_snip_start"] = np.array([(s + e) // 2 - SNIP // 2 for _, s, e in ev], int)
    rec["frandr_snips"] = snips
    return rec


def scan_patient(pid, limit=None):
    """Stream pat_<pid>.tar.gz once; return the MD5 of the stream, the member
    names and one reduced record per interval (``scan_interval``)."""
    filters = load_filters()
    url = BUCKET + f"data/pat_{pid:02d}.tar.gz"
    names, recs = [], []
    with fsspec.open(url, block_size=2 ** 24).open() as f:
        h = _HashingReader(f)
        tf = tarfile.open(fileobj=io.BufferedReader(h, 1 << 22), mode="r|gz")
        for m in tf:
            names.append((m.name, m.size, m.isfile()))
            if not m.isfile():
                continue
            if not m.name.endswith(".mat"):
                continue
            b = tf.extractfile(m).read()
            d = scipy.io.loadmat(io.BytesIO(b), squeeze_me=True, struct_as_record=False)["data"]
            del b
            r = scan_interval(d, filters)
            r["member"] = m.name
            recs.append(r)
            del d
            if limit and len(recs) >= limit:
                return {"pid": pid, "md5": None, "bytes": h.n, "members": names, "intervals": recs}
        tf.close()
        h.drain()
    return {"pid": pid, "md5": h.md5.hexdigest(), "bytes": h.n, "members": names, "intervals": recs}


# ---------------------------------------------------------------- paper tables
def load_table_s1():
    """Parse Table 1S of the supplement (fetched from the publisher; MD5 checked).

    Returns {patient: {"ilae": int, "channels": [label], "excluded": set,
    "resected": set, "rates": {type: {label: rate}}, "area": {type: set}}}.
    Labels are spelt as ``label_key`` gives them (the table writes patient
    18's PML contacts both as PML and as PM). Colours are the PDF's vector fills: red (1, .78, .81) resected channel,
    green (.78, .94, .81) HFO-area cell, gray (.86, .86, .86) excluded channel.
    """
    import pymupdf
    pdf = urllib.request.urlopen(SUPPLEMENT_URL).read()
    assert hashlib.md5(pdf).hexdigest() == SUPPLEMENT_MD5, "supplement changed"
    page = pymupdf.open(stream=pdf, filetype="pdf")[2]
    fills = []
    for dr in page.get_drawings():
        if not dr.get("fill"):
            continue
        col = tuple(round(c, 2) for c in dr["fill"])
        name = {(1.0, 0.78, 0.81): "red", (0.78, 0.94, 0.81): "green",
                (0.86, 0.86, 0.86): "gray"}.get(col)
        if name:
            fills.append((name, dr["rect"]))

    def colour(x, y):
        for name, r in fills:
            if r.x0 <= x <= r.x1 and r.y0 <= y <= r.y1:
                return name
        return None

    words = page.get_text("words")
    lines = {}
    for w in words:
        lines.setdefault((w[5], w[6]), []).append(w)
    # group words into rows by their vertical position
    rows = {}
    for w in words:
        key = round((w[1] + w[3]) / 2, 0)
        rows.setdefault(key, []).append(w)
    ys = sorted(rows)
    out, pat, header = {}, None, None
    for y in ys:
        ws = sorted(rows[y], key=lambda w: w[0])
        first = ws[0][4]
        if first == "Patient":
            pat = int(ws[1][4])
            out[pat] = {"ilae": int(ws[3][4]), "channels": [], "excluded": set(),
                        "resected": set(), "rates": {"R": {}, "FR": {}, "FRandR": {}},
                        "area": {"R": set(), "FR": set(), "FRandR": set()}}
        elif first == "Channels":
            header = []
            for w in ws[1:]:
                lab = label_key(w[4].strip("'"))
                cx, cy = (w[0] + w[2]) / 2, (w[1] + w[3]) / 2
                c = colour(cx, cy)
                header.append((lab, cx))
                out[pat]["channels"].append(lab)
                if c == "gray":
                    out[pat]["excluded"].add(lab)
                elif c == "red":
                    out[pat]["resected"].add(lab)
        elif first in ("Ripples", "FR", "FRandR"):
            typ = {"Ripples": "R", "FR": "FR", "FRandR": "FRandR"}[first]
            for w in ws[1:]:
                cx, cy = (w[0] + w[2]) / 2, (w[1] + w[3]) / 2
                lab = min(header, key=lambda h: abs(h[1] - cx))[0]
                out[pat]["rates"][typ][lab] = float(w[4])
                if colour(cx, cy) == "green":
                    out[pat]["area"][typ].add(lab)
    return out


def load_table1():
    """Table 1 of the paper, from the Europe PMC full text (PMC5653833), as a
    list of dicts keyed by the table's column headings."""
    xml = urllib.request.urlopen(PMC_XML_URL).read()
    root = ET.fromstring(xml)
    tab = [t for t in root.iter("table-wrap") if t.get("id") == "Tab1"][0]

    def txt(e):
        return re.sub(r"\s+", " ", "".join(e.itertext())).strip()

    head = [txt(c) for c in tab.find(".//thead").iter() if c.tag in ("th", "td")]
    rows = []
    for tr in tab.find(".//tbody").iter("tr"):
        cells = [txt(c) for c in tr if c.tag in ("td", "th")]
        rows.append(dict(zip(head, cells)))
    return rows


# ---------------------------------------------------------------- measures
def prctile_matlab(v, p):
    """Matlab prctile.m default: sorted values at percentiles 100*(i-0.5)/n,
    linear interpolation between them, the extremes beyond the end points."""
    v = np.sort(np.asarray(v, float))
    n = len(v)
    q = 100 * (np.arange(1, n + 1) - 0.5) / n
    return float(np.interp(p, q, v))


def hfo_area(rates, strict=True):
    """Indices of channels whose rate exceeds the 95th percentile (Methods)."""
    r = np.asarray(rates, float)
    thr = prctile_matlab(r, 95)
    return np.flatnonzero(r > thr if strict else r >= thr), thr


def cosine(a, b):
    na, nb = np.linalg.norm(a), np.linalg.norm(b)
    if na == 0 or nb == 0:
        return np.nan
    return float(a @ b / (na * nb))


def cosine_null(a, b, nperm, rng):
    """Normalised scalar products with the channel order of both vectors
    permuted at random (Methods, Test-retest reliability)."""
    a, b = np.asarray(a, float), np.asarray(b, float)
    A = a[rng.random((nperm, len(a))).argsort(axis=1)]
    B = b[rng.random((nperm, len(b))).argsort(axis=1)]
    num = np.sum(A * B, axis=1)
    return num / (np.linalg.norm(a) * np.linalg.norm(b))


def scan_all(pids=range(1, 21), workers=4):
    """Scan every patient, the largest files first, ``workers`` at a time."""
    from multiprocessing import get_context
    order = sorted(pids, key=lambda p: -_size(p))
    with get_context("spawn").Pool(workers, maxtasksperchild=1) as pool:
        res = list(pool.imap_unordered(scan_patient, order))
    return {r["pid"]: r for r in sorted(res, key=lambda r: r["pid"])}


def _size(pid):
    fs = fsspec.filesystem("https")
    return fs.size(BUCKET + f"data/pat_{pid:02d}.tar.gz")


# ---------------------------------------------------------------- spectral analysis
def stockwell(x, fmin_idx, fmax_idx):
    """S-transform of a real vector for frequency indices fmin_idx..fmax_idx
    (in units of fs/len(x)), as st.m of the data set's detector.zip (no edge
    removal, no analytic signal, factor 1): row k is
    ifft(X[k:k+n] * gaussian window), the window summed over its two halves."""
    n = len(x)
    X = np.fft.fft(x)
    XX = np.concatenate([X, X])
    ks = np.arange(fmin_idx, fmax_idx + 1)
    m = np.arange(n)
    v = np.stack([m ** 2, (m - n) ** 2]).astype(float)
    g = np.exp(-2 * np.pi ** 2 * v[None, :, :] / ks[:, None, None] ** 2).sum(axis=1)
    rows = XX[ks[:, None] + m[None, :]] * g
    return np.fft.ifft(rows, axis=1)


def gauss4(f, p):
    p = p.reshape(4, 3)
    return np.sum(p[:, 0:1] * np.exp(-(f[None, :] - p[:, 1:2]) ** 2 / (2 * p[:, 2:3] ** 2)), axis=0)


def fit_gauss4(f, y, start):
    """Least-squares fit of four gaussians (amplitude >= 0, centre in the band,
    width 5 to 200 Hz) to a spectrum; ``start`` is "fixed" (centres 100, 200,
    300, 400 Hz, widths 50 Hz) or "maxima" (the four largest local maxima)."""
    from scipy.optimize import least_squares
    from scipy.signal import argrelmax
    scale = y.max() if y.max() > 0 else 1.0
    yy = y / scale
    if start == "fixed":
        mu = np.array([100.0, 200.0, 300.0, 400.0])
    else:
        im = argrelmax(yy)[0]
        im = im[np.argsort(yy[im])[::-1][:4]]
        mu = np.sort(np.concatenate([f[im], [100.0, 200.0, 300.0, 400.0]])[:4])
    amp = np.interp(mu, f, yy)
    p0 = np.column_stack([amp, mu, np.full(4, 50.0)]).ravel()
    lo = np.tile([0.0, f[0], 5.0], 4)
    hi = np.tile([np.inf, f[-1], 200.0], 4)
    p0 = np.clip(p0, lo + 1e-9, hi - 1e-9)
    r = least_squares(lambda p: gauss4(f, p) - yy, p0, bounds=(lo, hi), method="trf", max_nfev=400)
    return r.x, r.success


def classify(f, p, peaks_from="curve"):
    """Spectral class of one event from its fitted curve (Methods, Spectral
    analysis): bimodal, a trough between 150 and 250 Hz and at least one peak
    above 200 Hz; unimodal, a single peak above 100 Hz, in the ripple band
    (80-250 Hz); otherwise none. Peaks are the local maxima of the fitted curve
    ("curve") or the fitted centres whose amplitude is at least 10% of the
    curve's maximum ("centres"). Returns (class, peak frequencies, troughs)."""
    from scipy.signal import argrelmax, argrelmin
    yf = gauss4(f, p)
    tr = f[argrelmin(yf)[0]]
    if peaks_from == "curve":
        pk = f[argrelmax(yf)[0]]
        amps = yf[argrelmax(yf)[0]]
    else:
        q = p.reshape(4, 3)
        keep = q[:, 0] >= 0.1 * yf.max()
        pk, amps = q[keep, 1], q[keep, 0]
        o = np.argsort(pk)
        pk, amps = pk[o], amps[o]
    if np.any((tr > 150) & (tr < 250)) and np.any(pk > 200):
        return "bimodal", pk, amps
    above = pk[pk > 100]
    if len(above) == 1 and above[0] <= 250:
        return "unimodal", pk, amps
    return "none", pk, amps


# ---------------------------------------------------------------- rates and areas
TYPES = ("R", "FR", "FRandR")


def label_key(lab):
    """One spelling for patient 18's PML contacts, which Table 1S writes both
    as 'PML3-4' and as 'PM1-2' (same electrode; spelling only)."""
    return lab.replace("PML", "PM")


def count_matrix(scan, typ):
    """Events per interval (rows) and bipolar channel (columns), with the
    interval durations in minutes and the night of each interval."""
    ivs = scan["intervals"]
    nb = len(ivs[0]["labels_bip"])
    C = np.zeros((len(ivs), nb))
    for i, iv in enumerate(ivs):
        ch = iv[typ][:, 0]
        ch = ch[(ch >= 0) & (ch < nb)]
        C[i] = np.bincount(ch, minlength=nb)
    dur = np.array([iv["n_samples"] / iv["fs"] / 60 for iv in ivs])
    night = np.array([iv["night"] for iv in ivs])
    return C, dur, night


def pooled_rates(C, dur, night, reading="a"):
    """Rate per channel pooled over intervals (claims file, opening comment):
    (a) all events over the total recorded time; (b) the mean of per-interval
    rates; (c) the mean over nights of per-night mean rates."""
    if reading == "a":
        return C.sum(0) / dur.sum()
    R = C / dur[:, None]
    if reading == "b":
        return R.mean(0)
    return np.mean([R[night == u].mean(0) for u in np.unique(night)], axis=0)


def test_retest(R, nperm, rng, pooled_null=False):
    """Share of pairs of rate vectors (rows of R) whose normalised scalar
    product exceeds the 97.5th percentile of its permutation null (Methods,
    Test-retest reliability). Null per pair (reading a) or pooled over all
    pairs of the patient (reading b). Pairs with an all-zero vector have no
    scalar product and count as not significant; their number is returned."""
    n = len(R)
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    if not pairs:
        return np.nan, 0, 0
    true, nulls, undefined = [], [], 0
    for i, j in pairs:
        c = cosine(R[i], R[j])
        if np.isnan(c):
            undefined += 1
        true.append(c)
        nulls.append(cosine_null(R[i], R[j], nperm, rng) if not np.isnan(c) else None)
    if pooled_null:
        allnull = np.concatenate([x for x in nulls if x is not None]) if any(
            x is not None for x in nulls) else np.array([np.nan])
        thr = [np.percentile(allnull, 97.5)] * len(pairs)
    else:
        thr = [np.percentile(x, 97.5) if x is not None else np.nan for x in nulls]
    sig = [(not np.isnan(c)) and c > t for c, t in zip(true, thr)]
    return float(np.mean(sig)), len(pairs), undefined


def spectral_events(job):
    """Spectral classes of the FRandR events of one channel (Methods,
    Spectral analysis). ``job`` holds the events (start, end), snippet starts
    and snippets of one patient's channel. For each event, 0.6 s (1200
    samples) centred on the event's midpoint (in the deposit the FRandR event
    and its FR event share start and end, so readings (a) and (b) of the centre
    coincide), the Stockwell transform over 80-500 Hz, |S| averaged over the
    event's duration (main; power |S|^2 a variant), fitted by four gaussians.
    Signal: (a) unfiltered bipolar; (b) high-passed at 80 Hz (4th-order
    Butterworth, forward-backward, a standard choice). Starting values: fixed
    or the spectrum's local maxima."""
    from scipy.signal import butter, sosfiltfilt
    ev, starts, snips = job["events"], job["snip_start"], job["snips"]
    N = 1200
    k0, k1 = int(np.ceil(80 * N / FS)), int(500 * N / FS)
    f = np.arange(k0, k1 + 1) * FS / N
    sos = butter(4, 80, "highpass", fs=FS, output="sos")
    out = []
    for (s, e), st0, sn in zip(ev, starts, snips):
        mid = (s + e) // 2
        w0 = mid - N // 2 - st0
        sn = sn.astype(float)
        a, b = s - (mid - N // 2), e - (mid - N // 2)
        a, b = max(a, 0), min(b, N - 1)
        row = {}
        for sig in ("raw", "hp"):
            x = sn if sig == "raw" else sosfiltfilt(sos, sn)
            S = stockwell(x[w0:w0 + N], k0, k1)
            amp = np.abs(S[:, a:b + 1]).mean(axis=1)
            for start in ("fixed", "maxima"):
                p, ok = fit_gauss4(f, amp, start)
                row[(sig, "abs", start)] = (p, ok)
            if sig == "raw":
                pw = (np.abs(S[:, a:b + 1]) ** 2).mean(axis=1)
                row[("raw", "power", "fixed")] = fit_gauss4(f, pw, "fixed")
        out.append(row)
    return {"pid": job["pid"], "f": f, "fits": out}
