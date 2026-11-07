"""Loading and measures for CRCNS fcx-1 (Watson et al. 2016, Neuron 90, 839-852).

The data set is 27 tar.gz files, one per session, in the public S3 bucket
crcnsarchive under fcx-1/live/data/. CRCNS data sets are not versioned
(docs/archives.md); the files read are pinned by the MD5 sums in the data set's
checksums.md5, which `checksums()` returns and the notebook prints.

A gzip stream cannot be read at random, and the order of the members differs
between tar files (the LFP .eeg file can come before the spike and state
files), so each session's tar is streamed once from start to end over
parallel range requests, decompressed in memory, and reduced as it is read:
the MATLAB files the analysis uses are kept in memory, and the LFP is reduced
to one channel, `goodeegchannel` of _BasicMetaData.mat, the "eeg channel
selected for default lfp analyses" (data description, section 1). When the
.eeg comes before _BasicMetaData.mat in the tar, the tar is streamed a second
time up to the end of the .eeg. Nothing is written to disk.

From that channel two reductions are kept (`lfp_reduce`):
- a spectrogram with 10 s windows every 1 s, the window and step of the
  paper's state scoring (Supplemental Experimental Procedures, Brain state
  scoring), reduced to mean power in the bands the paper names: delta 0.5-4 Hz
  (Results; Fig. 1B legend) and 1-4 Hz (Fig. 4 legend, a variant), sigma 9-25
  Hz, gamma 40-100 Hz (Results, Assessment of firing patterns), theta 5-10 Hz
  and the theta ratio 5-10 Hz over 2-16 Hz (Supplemental Experimental
  Procedures, Brain state scoring);
- band power in 8 ms bins for sigma and gamma (mean of the squared
  band-passed signal, 4th order Butterworth, zero phase), for analyses within
  UP states. The 8 ms bin and the filter are standard choices.
"""
from __future__ import annotations

import concurrent.futures as cf
import io
import re
import tarfile
import zlib

import numpy as np
import requests
import scipy.io as sio
from scipy import signal, stats

BUCKET = "https://crcnsarchive.s3-us-west-2.amazonaws.com"
DATASET = "fcx-1"
DOI = "10.6080/K02N506Q"
VERSION = "unversioned"   # CRCNS data sets are not versioned; pinned by checksums.md5
BASE = f"{BUCKET}/{DATASET}/live"

# Which MATLAB files are kept; the others (all units, burst-filtered trains,
# cluster quality, waveforms, synapses) are not used.
KEEP = ("_BasicMetaData.mat", "_WSRestrictedIntervals.mat", "_SStable.mat", "_CellIDs.mat",
        "_UPDOWNINtervals.mat", "_Spindles.mat", "_Motion.mat", "_EMGCorr.mat")

# Rat of each session prefix. The 2014052x sessions are rat JennBuzsaki22 in
# the data set's WatsonSleepHomestasis2016Table.xlsx.
def rat_of(session: str) -> str:
    if session.startswith("2014052"):
        return "JennBuzsaki22"
    return session.split("_")[0]


def checksums() -> dict:
    """MD5 sum of each file of the data set, from its checksums.md5."""
    text = requests.get(f"{BASE}/checksums.md5", timeout=60).text
    return {name: md5 for md5, name in re.findall(r"(\w{32})\s+(\S+)", text)}


def sessions() -> list:
    """The session names: one tar.gz per session under data/."""
    return sorted(re.findall(r"data/(\S+)\.tar\.gz", "\n".join(checksums())))


class _Prefetch(io.RawIOBase):
    """Sequential reader of a URL that fetches the next byte ranges in parallel."""

    def __init__(self, url, chunk=2**25, workers=6):
        self.url, self.chunk, self.workers = url, chunk, workers
        self.session = requests.Session()
        self.size = int(self.session.head(url, timeout=60).headers["Content-Length"])
        self.nchunks = (self.size + chunk - 1) // chunk
        self.pool = cf.ThreadPoolExecutor(workers)
        self.futures, self.next_request, self.current = {}, 0, 0
        self.buf, self.pos = b"", 0
        self._fill()

    def _get(self, i):
        a = i * self.chunk
        b = min(self.size, a + self.chunk) - 1
        err = None
        for _ in range(6):
            try:
                r = self.session.get(self.url, headers={"Range": f"bytes={a}-{b}"}, timeout=120)
                r.raise_for_status()
                if len(r.content) != b - a + 1:
                    raise IOError("short read")
                return r.content
            except Exception as e:  # retried, then raised
                err = e
        raise err

    def _fill(self):
        while self.next_request < self.nchunks and len(self.futures) < self.workers:
            self.futures[self.next_request] = self.pool.submit(self._get, self.next_request)
            self.next_request += 1

    def readable(self):
        return True

    def readinto(self, b):
        if self.pos >= len(self.buf):
            if self.current not in self.futures:
                return 0
            self.buf = self.futures.pop(self.current).result()
            self.pos = 0
            self.current += 1
            self._fill()
        n = min(len(b), len(self.buf) - self.pos)
        b[:n] = self.buf[self.pos:self.pos + n]
        self.pos += n
        return n

    def close(self):
        for f in self.futures.values():
            f.cancel()
        self.pool.shutdown(wait=False, cancel_futures=True)
        super().close()


class _Gunzip(io.RawIOBase):
    """Decompress a gzip stream in large chunks."""

    def __init__(self, raw, chunk=2**22):
        self.raw, self.chunk = raw, chunk
        self.d = zlib.decompressobj(16 + zlib.MAX_WBITS)
        self.buf, self.pos, self.eof = b"", 0, False

    def readable(self):
        return True

    def readinto(self, b):
        while self.pos >= len(self.buf):
            if self.eof:
                return 0
            c = self.raw.read(self.chunk)
            if not c:
                self.buf, self.pos, self.eof = self.d.flush(), 0, True
                continue
            self.buf, self.pos = self.d.decompress(c), 0
            if self.d.eof:
                self.eof = True
        n = min(len(b), len(self.buf) - self.pos)
        b[:n] = self.buf[self.pos:self.pos + n]
        self.pos += n
        return n


def _open_tar(session):
    raw = _Prefetch(f"{BASE}/data/{session}.tar.gz")
    stream = io.BufferedReader(_Gunzip(io.BufferedReader(raw, 2**22)), 2**22)
    return raw, tarfile.open(fileobj=stream, mode="r|")


def _read_channel(fobj, size, nch, ch):
    """One channel (0-based) of an interleaved int16 .eeg member, read in 1 min chunks."""
    step = nch * 2 * 1250 * 60
    out = []
    left = size
    rest = b""
    frame = nch * 2
    while left > 0:
        b = fobj.read(min(step, left))
        if not b:
            break
        left -= len(b)
        b = rest + b
        n = len(b) // frame * frame
        rest = b[n:]
        out.append(np.frombuffer(b[:n], dtype="<i2").reshape(-1, nch)[:, ch].copy())
    return np.concatenate(out)


def _meta(raw_bmd):
    b = sio.loadmat(io.BytesIO(raw_bmd), squeeze_me=True, struct_as_record=False)["bmd"]
    return dict(nChannels=int(b.Par.nChannels), lfp_fs=float(b.Par.lfpSampleRate),
                goodeegchannel=int(b.goodeegchannel), UPstatechannel=int(b.UPstatechannel),
                Thetachannel=int(b.Thetachannel), voltsperunit=float(b.voltsperunit),
                RecordingFileIntervals=np.atleast_2d(b.RecordingFileIntervals).astype(float))


def stream_session(session, lfp=True):
    """Stream one session's tar; return the kept files (bytes), the LFP channel and stream stats."""
    files, eeg, eeg_size = {}, None, None
    raw, tf = _open_tar(session)
    order = []
    for m in tf:
        key = m.name.split("/")[-1].replace(session, "", 1)
        order.append(key)
        if not m.isfile():
            continue
        if key in KEEP or key.endswith(".xml"):
            files[key] = tf.extractfile(m).read()
        elif key == ".eeg":
            eeg_size = m.size
            if lfp and "_BasicMetaData.mat" in files:
                md = _meta(files["_BasicMetaData.mat"])
                eeg = _read_channel(tf.extractfile(m), m.size, md["nChannels"], md["goodeegchannel"] - 1)
    raw.close()
    second_pass = False
    if lfp and eeg is None:
        second_pass = True
        md = _meta(files["_BasicMetaData.mat"])
        raw, tf = _open_tar(session)
        for m in tf:
            if m.name.endswith(".eeg"):
                eeg = _read_channel(tf.extractfile(m), m.size, md["nChannels"], md["goodeegchannel"] - 1)
                break
        raw.close()
    return dict(files=files, eeg=eeg, eeg_size=eeg_size, order=order, second_pass=second_pass)


# ---------------------------------------------------------------- parsing

def _pairs(x):
    a = np.asarray(x, dtype=float)
    if a.size == 0:
        return np.zeros((0, 2))
    return a.reshape(-1, 2) if a.ndim == 1 else a


def parse(session, raw):
    """Turn the kept files of a session into arrays."""
    f = raw["files"]
    md = _meta(f["_BasicMetaData.mat"])
    ws = sio.loadmat(io.BytesIO(f["_WSRestrictedIntervals.mat"]))
    states = {}
    for k in ("REM", "SWSEpisode", "SWSPacket", "MA", "WakeInterruption", "Wake", "Sleep", "REMEpisode"):
        states[k] = _pairs(ws[f"{k}TimePairFormat"])
    wsp = []
    for c in ws["WakeSleepTimePairFormat"].ravel():
        c = np.asarray(c, dtype=float)
        wsp.append(c)   # rows: [wake start, wake stop], [sleep start, sleep stop]
    states["WakeSleep"] = wsp
    st = sio.loadmat(io.BytesIO(f["_SStable.mat"]))
    spikes = [np.asarray(s, dtype=float).ravel() for s in st["S_CellFormat"].ravel()]
    ids = sio.loadmat(io.BytesIO(f["_CellIDs.mat"]), squeeze_me=True, struct_as_record=False)["CellIDs"]
    eall = np.atleast_1d(ids.EAll).astype(int) - 1
    iall = np.atleast_1d(ids.IAll).astype(int) - 1
    ud = sio.loadmat(io.BytesIO(f["_UPDOWNINtervals.mat"]))
    updown = {k: _pairs(ud[f"{k}IntsTimePairFormat"]) for k in ("UP", "DN", "ON", "OFF", "Gamma")}
    sp = sio.loadmat(io.BytesIO(f["_Spindles.mat"]), squeeze_me=True, struct_as_record=False)["SpindleData"]
    spindles = dict(times=np.atleast_2d(sp.normspindles).astype(float),
                    frequency=np.atleast_1d(sp.data.peakFrequency).astype(float),
                    amplitude=np.atleast_1d(sp.data.peakAmplitude).astype(float),
                    duration=np.atleast_1d(sp.data.duration).astype(float),
                    channel=int(sp.detectionchan))
    mo = sio.loadmat(io.BytesIO(f["_Motion.mat"]), squeeze_me=True, struct_as_record=False)["motiondata"]
    motion = dict(motion=np.atleast_1d(mo.motion).astype(float), filttype=str(mo.filttype))
    emg = sio.loadmat(io.BytesIO(f["_EMGCorr.mat"]))["EMGCorr"]
    out = dict(session=session, rat=rat_of(session), meta=md, states=states, spikes=spikes,
               E=eall, I=iall, updown=updown, spindles=spindles, motion=motion, emg=np.asarray(emg),
               order=raw["order"], second_pass=raw["second_pass"], eeg_size=raw["eeg_size"])
    if raw["eeg"] is not None:
        out["lfp"] = lfp_reduce(raw["eeg"].astype(np.float32) * md["voltsperunit"] * 1e6, md["lfp_fs"])
        out["lfp"]["n_samples"] = len(raw["eeg"])
    return out


# ---------------------------------------------------------------- LFP

BANDS = {"delta": (0.5, 4), "delta14": (1, 4), "sigma": (9, 25), "gamma": (40, 100),
         "theta": (5, 10), "theta_wide": (2, 16)}


def lfp_reduce(x, fs):
    """Band power per 1 s (10 s windows) and sigma/gamma power in 8 ms bins; x in uV."""
    # decimate 1250 -> 250 Hz for the spectrogram (gamma up to 100 Hz)
    q = int(round(fs / 250))
    y = signal.decimate(x, q, ftype="fir", zero_phase=True).astype(np.float32)
    f2 = fs / q
    nper = int(10 * f2)
    step = int(1 * f2)
    nwin = (len(y) - nper) // step + 1
    freqs = np.fft.rfftfreq(nper, 1 / f2)
    win = signal.windows.hann(nper).astype(np.float32)
    sel = {k: (freqs >= lo) & (freqs <= hi) for k, (lo, hi) in BANDS.items()}
    bp = {k: np.empty(nwin, np.float32) for k in BANDS}
    for s in range(0, nwin, 2000):
        e = min(nwin, s + 2000)
        idx = np.arange(s, e)[:, None] * step + np.arange(nper)[None, :]
        seg = y[idx]
        seg = seg - seg.mean(axis=1, keepdims=True)
        P = np.abs(np.fft.rfft(seg * win, axis=1)) ** 2
        for k in BANDS:
            bp[k][s:e] = P[:, sel[k]].mean(axis=1)
    # window k covers [k, k+10) s; its centre is k + 5 s
    t = np.arange(nwin) * 1.0 + 5.0
    fine = {}
    nb = int(round(fs * 0.008))   # 8 ms bins, 10 samples at 1250 Hz
    for k in ("sigma", "gamma"):
        sos = signal.butter(4, BANDS[k], btype="band", fs=fs, output="sos")
        z = signal.sosfiltfilt(sos, x).astype(np.float32) ** 2
        n = len(z) // nb
        fine[k] = z[:n * nb].reshape(n, nb).mean(axis=1)
    return dict(t=t, band=bp, fine=fine, fine_dt=nb / fs)


def load(session, lfp=True):
    return parse(session, stream_session(session, lfp=lfp))


# ---------------------------------------------------------------- intervals and per-second tables

def clip(iv, a, b):
    """Intervals of iv (n x 2) clipped to [a, b], empty ones dropped."""
    if len(iv) == 0:
        return np.zeros((0, 2))
    x = np.column_stack([np.maximum(iv[:, 0], a), np.minimum(iv[:, 1], b)])
    return x[x[:, 1] > x[:, 0]]


def within(iv, a, b):
    """Intervals of iv lying wholly inside [a, b]."""
    if len(iv) == 0:
        return np.zeros((0, 2))
    return iv[(iv[:, 0] >= a) & (iv[:, 1] <= b)]


def count_in(t, iv):
    """Number of sorted times t inside each interval of iv."""
    return np.searchsorted(t, iv[:, 1]) - np.searchsorted(t, iv[:, 0])


def rate_in(t, iv):
    """Spike count over summed duration of the intervals (Hz); nan when the duration is 0."""
    d = np.sum(iv[:, 1] - iv[:, 0]) if len(iv) else 0.0
    return count_in(t, iv).sum() / d if d > 0 else np.nan


def cycles(s):
    """WAKE-SLEEP cycles of a session: list of dicts with wake and sleep [start, stop]."""
    out = []
    for k, c in enumerate(s["states"]["WakeSleep"]):
        out.append(dict(k=k, wake=c[0], sleep=c[1]))
    return out


def seconds_table(s):
    """Per-second tables of a session, the time base for binned measures.

    Second i covers [i, i+1). The state scoring is at 1 s resolution (data
    description, section 4), so every state interval is a whole number of
    seconds.
    """
    dur = s["eeg_size"] / 2 / s["meta"]["nChannels"] / s["meta"]["lfp_fs"]
    T = int(np.ceil(max(dur, max((x.max() for x in s["spikes"] if len(x)), default=0)))) + 1
    edges = np.arange(T + 1, dtype=float)
    ncell = len(s["spikes"])
    cnt = np.zeros((ncell, T), np.int32)
    burst = np.zeros((ncell, T), np.int32)    # ISIs <= 15 ms ending in the second
    isis = np.zeros((ncell, T), np.int32)     # ISIs ending in the second
    up = s["updown"]["UP"]
    dn = s["updown"]["DN"]
    upcnt = np.zeros((ncell, T), np.int32)    # spikes inside UP states
    for i, x in enumerate(s["spikes"]):
        cnt[i] = np.histogram(x, edges)[0]
        if len(x) > 1:
            isi = np.diff(x)
            isis[i] = np.histogram(x[1:], edges)[0]
            burst[i] = np.histogram(x[1:][isi <= 0.015], edges)[0]
        if len(up):
            j = np.searchsorted(up[:, 0], x, side="right") - 1
            inup = (j >= 0) & (x < up[np.maximum(j, 0), 1])
            upcnt[i] = np.histogram(x[inup], edges)[0]

    def time_in(iv):
        """Time (s) of each second covered by the intervals."""
        out = np.zeros(T)
        for a, b in iv:
            ia, ib = int(np.floor(a)), int(np.floor(b))
            if ia == ib:
                out[ia] += b - a
            else:
                out[ia] += ia + 1 - a
                out[ia + 1:ib] += 1
                if ib < T:
                    out[ib] += b - ib
        return out

    def starts(iv, w=None):
        st = np.histogram(iv[:, 0], edges)[0] if len(iv) else np.zeros(T)
        if w is None:
            return st
        return np.histogram(iv[:, 0], edges, weights=w)[0] if len(iv) else np.zeros(T)

    sp = s["spindles"]
    spt = sp["times"]
    tab = dict(T=T, cnt=cnt, burst=burst, isis=isis, upcnt=upcnt,
               uptime=time_in(up), dntime=time_in(dn),
               upn=starts(up), upd=starts(up, up[:, 1] - up[:, 0]) if len(up) else np.zeros(T),
               dnn=starts(dn), dnd=starts(dn, dn[:, 1] - dn[:, 0]) if len(dn) else np.zeros(T),
               spn=starts(spt[:, [0, 2]]),
               spdur=starts(spt[:, [0, 2]], sp["duration"]),
               spfreq=starts(spt[:, [0, 2]], sp["frequency"]),
               spamp=starts(spt[:, [0, 2]], sp["amplitude"] * 1e6))
    tab["label"], tab["sleep_id"] = state_labels(s, T)
    if "lfp" in s:
        lf = s["lfp"]
        # window k spans [k, k+10) s; second i takes the window centred on it, k = i - 5
        k = np.clip(np.arange(T) - 5, 0, len(lf["t"]) - 1)
        tab["band"] = {b: v[k].astype(float) for b, v in lf["band"].items()}
    return tab


def state_labels(s, T):
    """State of each second: 0 other, 1 WAKE (cycle), 2 packet, 3 MA, 4 REM, 5 wake interruption;
    and the cycle whose SLEEP holds the second (-1 outside SLEEP)."""
    lab = np.zeros(T, np.int8)
    sleep_id = -np.ones(T, np.int32)
    st = s["states"]
    for c in cycles(s):
        a, b = c["wake"]
        lab[int(a):int(b)] = 1
        a, b = c["sleep"]
        sleep_id[int(a):int(b)] = c["k"]
        for code, key in ((2, "SWSPacket"), (3, "MA"), (4, "REM"), (5, "WakeInterruption")):
            for x, y in within(st[key], a, b):
                lab[int(x):int(y)] = code
    return lab, sleep_id


def short_wi_as_ma(s, tab):
    """MA reading (b): WakeInterruption intervals shorter than 40 s counted as MAs.

    Table S1 and the Results define an MA as an arousal under 40 s between nonREM
    packets, and the data description gives WakeInterruptions as 40 to 120 s, yet
    the files hold WakeInterruptions shorter than 40 s. Returns a shallow copy of
    the session and its per-second table with the states relabelled."""
    st = dict(s["states"])
    wi = st["WakeInterruption"]
    short = (wi[:, 1] - wi[:, 0]) < 40 if len(wi) else np.zeros(0, bool)
    ma = np.vstack([st["MA"], wi[short]])
    st["MA"] = ma[np.argsort(ma[:, 0])]
    st["WakeInterruption"] = wi[~short]
    s2 = dict(s, states=st)
    t2 = dict(tab)
    t2["label"], t2["sleep_id"] = state_labels(s2, tab["T"])
    return s2, t2


def overview_table():
    """The data set's WatsonSleepHomestasis2016Table.xlsx (docs/), as rows of the SleepOverview sheet."""
    import openpyxl
    r = requests.get(f"{BASE}/docs/WatsonSleepHomestasis2016Table.xlsx", timeout=60)
    r.raise_for_status()
    wb = openpyxl.load_workbook(io.BytesIO(r.content), read_only=True)
    return [list(row) for row in wb["SleepOverview"].iter_rows(values_only=True)]


# ---------------------------------------------------------------- per-cell rates

def state_intervals(s, key, cycle=None):
    """Intervals of a state inside the SLEEP of the cycles (or the given cycle)."""
    cs = cycles(s) if cycle is None else [cycle]
    if key == "WAKE":
        return np.array([c["wake"] for c in cs])
    out = [within(s["states"][key], *c["sleep"]) for c in cs]
    return np.vstack(out) if out else np.zeros((0, 2))


STATE_KEY = {"WAKE": "WAKE", "nonREM": "SWSPacket", "REM": "REM", "MA": "MA"}


def cell_rates(S, reading="b"):
    """Per-cell rates in WAKE, nonREM (packets), REM and MA within WAKE-SLEEP cycles.

    reading 'a': one row per cell and cycle; reading 'b': one row per cell, the
    mean of its per-cycle rates (claims file, M1)."""
    rows = []
    for s in S:
        for c in cycles(s):
            ivs = {st: state_intervals(s, k, c) for st, k in STATE_KEY.items()}
            for i, x in enumerate(s["spikes"]):
                r = dict(session=s["session"], rat=s["rat"], cell=i, cycle=c["k"],
                         type="E" if i in s["E"] else ("I" if i in s["I"] else "?"))
                for st, iv in ivs.items():
                    r[st] = rate_in(x, iv)
                rows.append(r)
    import pandas as pd
    df = pd.DataFrame(rows)
    if reading == "a":
        return df
    return df.groupby(["session", "rat", "cell", "type"], as_index=False)[list(STATE_KEY)].mean()


def session_wake_rates(S):
    """Each pE and pI cell's rate over all scored WAKE intervals of its session (M2, "general WAKE
    firing rate"; in these files the scored WAKE intervals are the WAKE of the cycles)."""
    import pandas as pd
    rows = [dict(session=s["session"], cell=i, type="E" if i in s["E"] else "I",
                 WAKE=rate_in(s["spikes"][i], s["states"]["Wake"]))
            for s in S for i in list(s["E"]) + list(s["I"])]
    return pd.DataFrame(rows)


def sextiles(df_b):
    """Sextile (1 lowest .. 6 highest WAKE rate) of each pE cell, over the whole data set (M2).

    df_b has one row per cell (session_wake_rates, M2 reading a)."""
    e = df_b[df_b.type == "E"].copy()
    ranks = e["WAKE"].rank(method="first")
    e["sextile"] = np.ceil(ranks / len(e) * 6).astype(int)
    return e.set_index(["session", "cell"])["sextile"]


# ---------------------------------------------------------------- statistics

def pearson(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    ok = np.isfinite(x) & np.isfinite(y)
    if ok.sum() < 3:
        return np.nan, np.nan, int(ok.sum())
    r, p = stats.pearsonr(x[ok], y[ok])
    return float(r), float(p), int(ok.sum())


def ols_slope(x, y, level=0.95):
    """OLS slope of y on x with its confidence interval, and Pearson R (M5)."""
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    ok = np.isfinite(x) & np.isfinite(y)
    x, y = x[ok], y[ok]
    res = stats.linregress(x, y)
    tq = stats.t.ppf(0.5 + level / 2, len(x) - 2)
    return dict(slope=res.slope, lo=res.slope - tq * res.stderr, hi=res.slope + tq * res.stderr,
                r=res.rvalue, p=res.pvalue, n=len(x))


def log_slope(x, y):
    """M5: OLS of log10 y on log10 x, cells with a zero (or missing) rate in either left out."""
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    ok = (x > 0) & (y > 0) & np.isfinite(x) & np.isfinite(y)
    out = ols_slope(np.log10(x[ok]), np.log10(y[ok]))
    out["dropped"] = int((~ok).sum())
    return out


# ---------------------------------------------------------------- time-normalized trends (M3)

def units(s, scope):
    """The periods a trend is normalized over: SLEEP, nonREM episodes, packets, WAKE or REM
    episodes, each inside the session's WAKE-SLEEP cycles; list of (a, b, cycle)."""
    out = []
    for c in cycles(s):
        if scope == "sleep":
            out.append((c["sleep"][0], c["sleep"][1], c["k"]))
        elif scope == "wake":
            out.append((c["wake"][0], c["wake"][1], c["k"]))
        else:
            key = {"episode": "SWSEpisode", "packet": "SWSPacket", "rem": "REM", "ma": "MA"}[scope]
            out += [(a, b, c["k"]) for a, b in within(s["states"][key], *c["sleep"])]
    return out


def windows(s, tab, scope, reading, labels=(2,), nbins=50, clock="period"):
    """Sampling windows of a time-normalized trend (claims file, M3).

    Each window is (unit index, normalized time, array of seconds). Only seconds
    whose state is in `labels` are used (2 = nonREM packet), so for SLEEP only
    nonREM time is used (M3). Readings: 'a' one window per packet, at its
    normalized mid-time; 'b' 10 s bins of contiguous state time; 'c' `nbins`
    equal bins of normalized time.

    clock: how a period is normalized. 'period' (i): by its clock time, start 0
    and end 1; 'state' (ii): by the cumulative time of the used state only (for
    SLEEP, nonREM time concatenated). The paper says SLEEP is time-normalized and
    only nonREM time is used (Results; Fig. 3B legend) without saying which, so
    both are run where they differ.
    """
    lab = tab["label"]
    out = []
    for u, (a, b, k) in enumerate(units(s, scope)):
        a, b = int(a), int(b)
        secs = np.arange(a, b)
        ok = np.isin(lab[a:b], labels)
        L = b - a
        if clock == "period":
            pos = (np.arange(L) + 0.5) / L
        else:
            n_ok = max(ok.sum(), 1)
            pos = (np.cumsum(ok) - 0.5) / n_ok
        if reading == "a":
            for x, y in within(s["states"]["SWSPacket"], a, b):
                mid = min(int((x + y) / 2) - a, L - 1)
                out.append((u, float(pos[mid]), np.arange(int(x), int(y))))
        elif reading == "b":
            # contiguous runs of ok seconds, cut in 10 s pieces
            d = np.diff(np.concatenate([[0], ok.astype(int), [0]]))
            for r0, r1 in zip(np.where(d == 1)[0], np.where(d == -1)[0]):
                for j in range(r0, r1 - 9, 10):
                    out.append((u, float(pos[j:j + 10].mean()), secs[j:j + 10]))
        elif reading == "c":
            bi = np.minimum((pos * nbins).astype(int), nbins - 1)
            for j in range(nbins):
                m = (bi == j) & ok
                out.append((u, (j + 0.5) / nbins, secs[m]))
    return out


def trend(S, tabs, scope, measure, reading, labels=(2,), normalize=True, nbins=50, clock="period"):
    """Pearson R of a measure against normalized time (M3, M4).

    measure(s, tab, secs) gives the value of one window (nan when undefined).
    With normalize, values are divided by the session's mean value before
    pooling (M3, as the Supplemental Experimental Procedures do for CV and
    burst ratio). Reading 'c' averages the windows of each normalized bin over
    all periods, giving nbins points."""
    T, V = [], []
    for s, tab in zip(S, tabs):
        w = windows(s, tab, scope, reading, labels, nbins, clock)
        if not w:
            continue
        t = np.array([x[1] for x in w])
        v = np.array([measure(s, tab, x[2]) if len(x[2]) else np.nan for x in w], float)
        if normalize:
            m = np.nanmean(v) if np.any(np.isfinite(v)) else np.nan
            v = v / m if m and np.isfinite(m) else v * np.nan
        T.append(t)
        V.append(v)
    T, V = np.concatenate(T), np.concatenate(V)
    if reading == "c":
        bins = np.round(T * nbins - 0.5).astype(int)
        V = np.array([np.nanmean(V[bins == j]) if np.any(np.isfinite(V[bins == j])) else np.nan
                      for j in range(nbins)])
        T = (np.arange(nbins) + 0.5) / nbins
    r, p, n = pearson(T, V)
    return dict(r=r, p=p, n=n, t=T, v=V)


# measures of a window of seconds -------------------------------------------

def m_rate(cells):
    """Mean rate (Hz) of the given cells over the window."""
    def f(s, tab, secs):
        c = cells(s)
        if len(c) == 0:
            return np.nan
        return tab["cnt"][np.ix_(c, secs)].sum() / (len(c) * len(secs))
    return f


def m_uprate(cells):
    """Mean rate of the cells within UP states of the window (spikes in UP / UP time)."""
    def f(s, tab, secs):
        c = cells(s)
        ut = tab["uptime"][secs].sum()
        if len(c) == 0 or ut <= 0:
            return np.nan
        return tab["upcnt"][np.ix_(c, secs)].sum() / (len(c) * ut)
    return f


def m_cv(s, tab, secs):
    """CV across pE cells of their rates in the window."""
    r = tab["cnt"][np.ix_(s["E"], secs)].sum(axis=1) / len(secs)
    return r.std() / r.mean() if r.mean() > 0 else np.nan


def m_burst(s, tab, secs):
    """Mean over pE cells of the proportion of ISIs <= 15 ms in the window."""
    n = tab["isis"][np.ix_(s["E"], secs)].sum(axis=1)
    b = tab["burst"][np.ix_(s["E"], secs)].sum(axis=1)
    ok = n > 0
    return np.mean(b[ok] / n[ok]) if ok.any() else np.nan


def m_events(key):
    """Incidence (per s) of UP ('upn'), DOWN ('dnn') or spindle ('spn') starts."""
    return lambda s, tab, secs: tab[key][secs].sum() / len(secs)


def m_mean(keysum, keyn):
    """Mean property (duration etc.) of the events starting in the window."""
    def f(s, tab, secs):
        n = tab[keyn][secs].sum()
        return tab[keysum][secs].sum() / n if n > 0 else np.nan
    return f


def m_other(s, tab, secs):
    """Fraction of time in neither a detected UP nor DOWN state."""
    return 1 - (tab["uptime"][secs].sum() + tab["dntime"][secs].sum()) / len(secs)


def m_band(name):
    """Mean band power, z-scored per session over nonREM seconds of the cycles (see zband)."""
    return lambda s, tab, secs: np.mean(tab["zband"][name][secs])


def add_zband(tab):
    """Band power z-scored per session over the session's nonREM (packet) seconds; a standard choice."""
    nr = tab["label"] == 2
    tab["zband"] = {}
    for k, v in tab["band"].items():
        lv = np.log10(np.maximum(v, 1e-12))
        tab["zband"][k] = (lv - lv[nr].mean()) / lv[nr].std()
    tab["nrem_delta_mean"] = tab["band"]["delta"][nr].mean()


# ---------------------------------------------------------------- spike-train measures

def isi_counts(x, iv, thr=0.015):
    """ISIs <= thr and all ISIs whose two spikes lie in the same interval of iv.

    ISIs that span two intervals are dropped (claims file, burst-index-by-state,
    a standard choice)."""
    if len(iv) == 0 or len(x) < 2:
        return 0, 0
    j = np.searchsorted(iv[:, 0], x, side="right") - 1
    inside = (j >= 0) & (x < iv[np.maximum(j, 0), 1])
    xs, js = x[inside], j[inside]
    same = js[1:] == js[:-1]
    d = np.diff(xs)[same]
    return int((d <= thr).sum()), int(len(d))


def runs10(tab, label):
    """10 s bins of contiguous seconds with the given state label (and inside a cycle)."""
    ok = (tab["label"] == label)
    d = np.diff(np.concatenate([[0], ok.astype(int), [0]]))
    out = []
    for r0, r1 in zip(np.where(d == 1)[0], np.where(d == -1)[0]):
        for j in range(r0, r1 - 9, 10):
            out.append(np.arange(j, j + 10))
    return out


def acg(x, iv, maxlag=0.5, binw=0.001):
    """Autocorrelogram counts (1 ms bins, 0-500 ms) of spikes within the same interval of iv."""
    nb = int(round(maxlag / binw))
    h = np.zeros(nb)
    if len(iv) == 0 or len(x) < 2:
        return h
    j = np.searchsorted(iv[:, 0], x, side="right") - 1
    inside = (j >= 0) & (x < iv[np.maximum(j, 0), 1])
    xs, js = x[inside], j[inside]
    for k in range(1, 200):
        if k >= len(xs):
            break
        d = xs[k:] - xs[:-k]
        ok = (js[k:] == js[:-k]) & (d < maxlag)
        if not ok.any():
            break
        h += np.histogram(d[ok], bins=nb, range=(0, maxlag))[0]
    return h


def burst_spikes(x, iv, thr=0.015):
    """Spikes with an ISI <= thr before or after them (within the same interval), and all spikes
    in the intervals: the Results' "fraction of spikes with ISIs below 15 ms" read per spike."""
    if len(iv) == 0 or len(x) < 2:
        return 0, 0
    j = np.searchsorted(iv[:, 0], x, side="right") - 1
    inside = (j >= 0) & (x < iv[np.maximum(j, 0), 1])
    xs, js = x[inside], j[inside]
    if len(xs) < 2:
        return 0, int(len(xs))
    short = (np.diff(xs) <= thr) & (js[1:] == js[:-1])
    flag = np.zeros(len(xs), bool)
    flag[1:] |= short
    flag[:-1] |= short
    return int(flag.sum()), int(len(xs))


def fine_z(s, tab, band):
    """Fine band power (log10), z-scored over the session's nonREM-packet samples; and its bin (s)."""
    dt = s["lfp"]["fine_dt"]
    v = np.log10(np.maximum(s["lfp"]["fine"][band], 1e-12))
    sec = np.minimum((np.arange(len(v)) * dt).astype(int), tab["T"] - 1)
    nr = tab["label"][sec] == 2
    return (v - v[nr].mean()) / v[nr].std(), dt


def mean_in(z, dt, a, b):
    """Mean of a fine series over [a, b) for arrays of starts a and stops b (at least one sample)."""
    cs = np.concatenate([[0], np.cumsum(z)])
    lo = np.clip((a / dt).astype(int), 0, len(z) - 1)
    hi = np.clip(np.ceil(b / dt).astype(int), lo + 1, len(z))
    return (cs[hi] - cs[lo]) / (hi - lo)


# ---------------------------------------------------------------- triplets (claims file, M6)

def sleep_sequence(s, c):
    """Sub-state intervals of one SLEEP in time order: list of (kind, start, stop)."""
    seq = []
    for kind, key in (("P", "SWSPacket"), ("M", "MA"), ("R", "REM"), ("W", "WakeInterruption")):
        for a, b in within(s["states"][key], *c["sleep"]):
            seq.append((kind, a, b))
    return sorted(seq, key=lambda x: x[1])


def triplets(s, pattern, max_gap=2.0, wake_min=None):
    """Triplets A n, B, A n+1 of adjacent intervals (gaps <= max_gap s) inside each SLEEP.

    pattern is e.g. "MPM" (MA, packet, MA), "PRP" (packet, REM, packet). For "PWP",
    wake_min selects WakeInterruption intervals of at least that length (s), and the
    scored WAKE that follows a SLEEP is added as the middle state between the
    last packet of that SLEEP and the first packet of the next one when they are
    adjacent. For "PRP", the second packet is the next packet after the REM
    episode, with any MA or WakeInterruption between them: nonREM-REM-nonREM
    triplets are kept unless a WAKE of more than 120 s follows the REM before the
    second packet (Supplemental Experimental Procedures; claims file, M6), and
    inside a SLEEP no interruption exceeds 120 s. "RPR_after" applies that tolerance to
    REM, packet, REM triplets: any MA or WakeInterruption may come between REM n and the
    packet (an assumption, stated in the attempt record)."""
    out = []
    cs = cycles(s)
    for c in cs:
        seq = sleep_sequence(s, c)
        if pattern == "RPR_bridge":
            # variant: REM, packet, REM with any MA or WakeInterruption between them
            core = [x for x in seq if x[0] in "PR"]
            for x, y, z in zip(core, core[1:], core[2:]):
                if (x[0], y[0], z[0]) == ("R", "P", "R"):
                    out.append(dict(first=(x[1], x[2]), mid=(y[1], y[2]), second=(z[1], z[2]), kind="within"))
            continue
        if pattern == "RPR_after":
            # REM n, packet, REM n+1 with any MA or WakeInterruption between REM n and the
            # packet, the tolerance M6 gives for an arousal that follows REM; packet and
            # REM n+1 adjacent
            for j in range(len(seq)):
                if seq[j][0] != "R":
                    continue
                m = j + 1
                while m < len(seq) and seq[m][0] in "MW":
                    m += 1
                if m + 1 >= len(seq) or seq[m][0] != "P" or seq[m + 1][0] != "R":
                    continue
                if m == j + 1 and seq[m][1] - seq[j][2] > max_gap:
                    continue
                if seq[m + 1][1] - seq[m][2] > max_gap:
                    continue
                out.append(dict(first=(seq[j][1], seq[j][2]), mid=(seq[m][1], seq[m][2]),
                                second=(seq[m + 1][1], seq[m + 1][2]), kind="within"))
            continue
        if pattern == "PRP":
            for j in range(1, len(seq) - 1):
                x, y = seq[j - 1], seq[j]
                if x[0] != "P" or y[0] != "R" or y[1] - x[2] > max_gap:
                    continue
                k = j + 1
                while k < len(seq) and seq[k][0] in "MW":
                    k += 1
                if k < len(seq) and seq[k][0] == "P":
                    z = seq[k]
                    out.append(dict(first=(x[1], x[2]), mid=(y[1], y[2]), second=(z[1], z[2]), kind="within"))
            continue
        if pattern == "PWP" and wake_min is not None:
            seq = [x for x in seq if x[0] != "W" or x[2] - x[1] >= wake_min]
        for x, y, z in zip(seq, seq[1:], seq[2:]):
            if (x[0], y[0], z[0]) == tuple(pattern) and y[1] - x[2] <= max_gap and z[1] - y[2] <= max_gap:
                out.append(dict(first=(x[1], x[2]), mid=(y[1], y[2]), second=(z[1], z[2]), kind="within"))
    if pattern == "PWP":
        for c, d in zip(cs, cs[1:]):
            if d["wake"][0] - c["sleep"][1] <= max_gap:
                p1 = within(s["states"]["SWSPacket"], *c["sleep"])
                p2 = within(s["states"]["SWSPacket"], *d["sleep"])
                if len(p1) and len(p2):
                    out.append(dict(first=tuple(p1[-1]), mid=tuple(d["wake"]), second=tuple(p2[0]), kind="WAKE"))
    return out
