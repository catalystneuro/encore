"""Loading and measures for Watson et al. (2016), "Network homeostasis and state dynamics of
neocortical sleep", on DANDI:000041 and CRCNS:fcx-1.

Where a parameter comes from is said beside it:
  [claim]    the claim's criterion in claims/watson-2016.yaml (which cites the paper);
  [paper]    a passage of the paper, cited (author, step 1.6);
  [assumed]  an assumption, with the reason;
  [standard] a standard choice for a detail that cannot change a result.

Both datasets are streamed: the NWB files of DANDI:000041 with remfile and h5py, the tar.gz files of
CRCNS:fcx-1 over HTTP range requests from the public bucket, decompressed as they arrive. Nothing is
written to disk.
"""
import io
import re
import tarfile
import threading
import time
from concurrent.futures import ThreadPoolExecutor

import numpy as np
import requests
import scipy.io as sio
from scipy import signal

DANDI_ID = "000041"
DANDI_VERSION = "0.261104.0300"
CRCNS_ID = "fcx-1"
CRCNS_VERSION = "unversioned"  # CRCNS data sets are not versioned (docs/archives.md); MD5 sums are printed
CRCNS_BASE = "https://crcnsarchive.s3-us-west-2.amazonaws.com/fcx-1/live/"
CRCNS_DOI = "10.6080/K02N506Q"
FS_LFP = 1250.0  # [paper] Supplemental Experimental Procedures, "resampled at 1250Hz"

# Band limits, Hz. [paper] Results and Fig. 1B legend (delta 0.5-4, sigma 9-25, gamma 40-100);
# Fig. 4 legend gives delta 1-4 (a variant, [claim] fig4i); theta ratio 5-10 / 2-16 Hz
# (Supplemental Experimental Procedures, Brain state scoring).
BANDS = {"delta": (0.5, 4.0), "delta14": (1.0, 4.0), "theta": (5.0, 10.0), "broad": (2.0, 16.0),
         "sigma": (9.0, 25.0), "gamma": (40.0, 100.0)}
# Long windows: 2 s Hann windows every 1 s. [standard] The paper's spectrogram is 10 s windows every
# 1 s (Brain state scoring); a 10 s window's band power is taken as the mean of the 2 s windows
# inside it (a Welch estimate), which keeps the 1 s step and gives 0.5 Hz resolution for delta.
LONG_WIN, LONG_HOP = 2500, 1250
# Short windows for within-UP-state power: 200 ms every 100 ms, sigma 10-25 Hz and gamma 40-100 Hz
# at 5 Hz resolution. [assumed] The paper does not give the UP-state spectrogram's window.
SHORT_WIN, SHORT_HOP = 250, 125
SHORT_BANDS = {"sigma": (10.0, 25.0), "gamma": (40.0, 100.0)}


# ----------------------------------------------------------------------------------------------
# Streaming readers
# ----------------------------------------------------------------------------------------------
class PrefetchReader(io.RawIOBase):
    """Sequential reader of a URL that fetches the next blocks in parallel range requests."""

    def __init__(self, url, block=16 * 2**20, nthreads=6):
        self.url, self.block = url, block
        self.size = int(requests.head(url, timeout=60).headers["Content-Length"])
        self.nb = (self.size + block - 1) // block
        self.ex = ThreadPoolExecutor(nthreads)
        self.nthreads = nthreads
        self.futs, self.next_block = {}, 0
        self.cur, self.curpos, self.pos = b"", 0, 0
        self._fill()

    def _get(self, i):
        s = i * self.block
        e = min(self.size, s + self.block) - 1
        for k in range(6):
            try:
                r = requests.get(self.url, headers={"Range": f"bytes={s}-{e}"}, timeout=120)
                if r.status_code in (200, 206) and len(r.content) == e - s + 1:
                    return r.content
            except requests.RequestException:
                pass
            time.sleep(2 + 3 * k)
        raise IOError(f"range request failed: {self.url} {s}-{e}")

    def _fill(self):
        while len(self.futs) < 2 * self.nthreads and self.next_block < self.nb:
            self.futs[self.next_block] = self.ex.submit(self._get, self.next_block)
            self.next_block += 1

    def readable(self):
        return True

    def readinto(self, b):
        if self.curpos >= len(self.cur):
            i = self.pos // self.block
            if i not in self.futs:
                return 0
            self.cur = self.futs.pop(i).result()
            self.curpos = 0
            self._fill()
        n = min(len(b), len(self.cur) - self.curpos)
        b[:n] = self.cur[self.curpos:self.curpos + n]
        self.curpos += n
        self.pos += n
        return n

    def close(self):
        for f in self.futs.values():
            f.cancel()
        self.ex.shutdown(wait=False, cancel_futures=True)
        super().close()


def _bandmask(freqs, lo, hi):
    return (freqs >= lo) & (freqs <= hi)


class BandAccumulator:
    """Band powers of a multichannel int16 stream, in long (2 s / 1 s) and short (200 / 100 ms)
    windows, computed block by block so the signal is never held whole."""

    def __init__(self, nch):
        self.nch = nch
        self.carry = np.zeros((0, nch), np.float32)
        self.long = []
        self.short = []
        self.wl = signal.windows.hann(LONG_WIN, sym=False).astype(np.float32)
        self.ws = signal.windows.hann(SHORT_WIN, sym=False).astype(np.float32)
        fl = np.fft.rfftfreq(LONG_WIN, 1 / FS_LFP)
        fs = np.fft.rfftfreq(SHORT_WIN, 1 / FS_LFP)
        self.ml = {k: _bandmask(fl, *v) for k, v in BANDS.items()}
        self.ms = {k: _bandmask(fs, *v) for k, v in SHORT_BANDS.items()}
        self.n = 0

    def add(self, x):
        """x: (samples, nch) array. Keeps windows whose start is a multiple of the hop."""
        import scipy.fft as sfft
        x = np.concatenate([self.carry, x.astype(np.float32)])
        nlw = max(0, (len(x) - LONG_WIN) // LONG_HOP + 1)
        if nlw:
            v = np.lib.stride_tricks.sliding_window_view(x, LONG_WIN, axis=0)[::LONG_HOP][:nlw]
            P = np.abs(sfft.rfft(v * self.wl, axis=-1, workers=2)) ** 2
            self.long.append(np.stack([P[..., m].mean(-1) for m in self.ml.values()], -1))
            del P, v
        nsw = max(0, (len(x) - SHORT_WIN) // SHORT_HOP + 1)
        # keep both window grids aligned: consume only whole long hops
        consumed = nlw * LONG_HOP
        nsw = min(nsw, consumed // SHORT_HOP)
        if nsw:
            v = np.lib.stride_tricks.sliding_window_view(x, SHORT_WIN, axis=0)[::SHORT_HOP][:nsw]
            P = np.abs(sfft.rfft(v * self.ws, axis=-1, workers=2)) ** 2
            self.short.append(np.stack([P[..., m].mean(-1) for m in self.ms.values()], -1).astype(np.float32))
            del P, v
        self.carry = x[consumed:]
        self.n += consumed

    def result(self):
        L = np.concatenate(self.long) if self.long else np.zeros((0, self.nch, len(BANDS)))
        S = np.concatenate(self.short) if self.short else np.zeros((0, self.nch, len(SHORT_BANDS)))
        # window centres in s: long window k spans [k, k+2) s; short window j spans [0.1j, 0.1j+0.2)
        tl = np.arange(len(L)) * LONG_HOP / FS_LFP + LONG_WIN / FS_LFP / 2
        ts = np.arange(len(S)) * SHORT_HOP / FS_LFP + SHORT_WIN / FS_LFP / 2
        return tl, L, ts, S


def guess_nchannels(raw, candidates=range(16, 300)):
    """Channel count of an interleaved int16 recording, from the lag that maximizes the
    correlation of the sample stream with itself (the same channel one time step later).
    Used only when the session's .xml comes after its .eeg in the tar; checked against the
    .xml afterwards."""
    x = np.frombuffer(raw, np.int16).astype(np.float64)
    x = x - x.mean()
    best, bc = None, -2
    for n in candidates:
        c = np.corrcoef(x[:-n], x[n:])[0, 1]
        if c > bc:
            best, bc = n, c
    return best


def _tp(v):
    """TimePairFormat to an (n, 2) float array."""
    if isinstance(v, np.ndarray) and v.dtype == object:
        return [np.atleast_2d(np.asarray(e, float)) for e in v]
    a = np.asarray(v, float)
    if a.size == 0:
        return np.zeros((0, 2))
    return np.atleast_2d(a)


def _loadmat(b):
    return sio.loadmat(io.BytesIO(b), squeeze_me=True, struct_as_record=False)


CRCNS_SESSIONS = [
    "20140526_277um", "20140527_421um", "20140528_565um", "BWRat17_121712", "BWRat17_121912",
    "BWRat18_020513", "BWRat19_032413", "BWRat19_032513", "BWRat20_101013", "BWRat20_101513",
    "BWRat21_121113", "BWRat21_121613", "BWRat21_121813", "Bogey_012615", "Dino_061814_mPFC",
    "Dino_061914_ACC", "Dino_061914_mPFC", "Dino_062014_ACC", "Dino_062014_mPFC", "Dino_072114_mPFC",
    "Dino_072314_mPFC", "Dino_072414_mPFC", "Rizzo_022615", "Rizzo_022715", "Splinter_020515",
    "Splinter_020915", "Templeton_032415"]


def crcns_rat(name):
    """Rat of a CRCNS session folder; the 2014052x sessions are rat B22 (Table S1 lists B22 with 3
    OFC sessions; their .xml names the animal)."""
    if name.startswith("2014052"):
        return "B22"
    return name.split("_")[0]


def load_crcns(name, keep_all_channels=False):
    """Stream one CRCNS session tar and reduce it to a dict.

    Spikes are the stable units (_SStable, 'the units used in the publication', data descriptor),
    classified by _CellIDs EAll (pE) and IAll (pI). States are _WSRestrictedIntervals; UP and DOWN
    states _UPDOWNINtervals; spindles _Spindles; motion _Motion. Band powers are computed while the
    .eeg streams past, on every channel (the channel used, goodeegchannel, is in _BasicMetaData,
    which the tar may hold after the .eeg), and reduced to the good and theta channels after."""
    url = CRCNS_BASE + f"data/{name}.tar.gz"
    rdr = PrefetchReader(url)
    tf = tarfile.open(fileobj=io.BufferedReader(rdr, buffer_size=2**22), mode="r|gz")
    want = ("_BasicMetaData.mat", ".xml", "_CellIDs.mat", "_SStable.mat", "_WSRestrictedIntervals.mat",
            "_UPDOWNINtervals.mat", "_Spindles.mat", "_Motion.mat", "_ChannelAnatomy.csv", "_SAll.mat",
            "_EMGCorr.mat")
    files, order = {}, []
    nch_guess = None
    bands = None
    eeg_bytes = 0
    for m in tf:
        base = m.name.split("/")[-1]
        order.append(base)
        if not m.isfile():
            continue
        if base.endswith(".eeg"):
            fo = tf.extractfile(m)
            eeg_bytes = m.size
            nch = None
            if ".xml" in files:
                nch = int(re.search(rb"<nChannels>(\d+)</nChannels>", files[".xml"]).group(1))
            first = fo.read(2**22)
            if nch is None:
                nch = guess_nchannels(first[: 2 * 300 * 4000])
                nch_guess = nch
            acc = BandAccumulator(nch)
            blocksamp = int(FS_LFP * 300)  # 300 s blocks
            buf = first
            while True:
                need = blocksamp * nch * 2
                while len(buf) < need:
                    more = fo.read(need - len(buf))
                    if not more:
                        break
                    buf += more
                nwhole = (len(buf) // (2 * nch)) * 2 * nch
                if nwhole == 0:
                    break
                x = np.frombuffer(buf[:nwhole], np.int16).reshape(-1, nch)
                acc.add(x)
                buf = buf[nwhole:]
                if len(x) < blocksamp:
                    break
            bands = acc.result()
            continue
        for w in want:
            if base.endswith(w):
                files[w] = tf.extractfile(m).read()
    rdr.close()

    out = {"dataset": "crcns-fcx-1", "name": name, "rat": crcns_rat(name), "tar_order": order,
           "eeg_bytes": eeg_bytes}
    xml = files.get(".xml", b"")
    nch_xml = int(re.search(rb"<nChannels>(\d+)</nChannels>", xml).group(1))
    out["nch_xml"], out["nch_guess"] = nch_xml, nch_guess
    bmd = _loadmat(files["_BasicMetaData.mat"])["bmd"]
    out["goodeegchannel"] = int(bmd.goodeegchannel)  # 1-based
    out["thetachannel"] = int(bmd.Thetachannel)
    out["voltsperunit"] = float(bmd.voltsperunit)
    out["lfp_rate_xml"] = float(bmd.Par.lfpSampleRate)
    out["rec_intervals"] = np.atleast_2d(np.asarray(bmd.RecordingFileIntervals, float))
    st = _loadmat(files["_SStable.mat"])
    spk = [np.atleast_1d(np.asarray(s, float)) for s in st["S_CellFormat"]]
    ids = _loadmat(files["_CellIDs.mat"])["CellIDs"]
    ctype = np.array(["?"] * len(spk), dtype=object)
    for i in np.atleast_1d(ids.EAll):
        ctype[int(i) - 1] = "E"
    for i in np.atleast_1d(ids.IAll):
        ctype[int(i) - 1] = "I"
    out["spikes"], out["ctype"] = spk, ctype
    out["shank"] = np.atleast_1d(st["shank"])
    if "_SAll.mat" in files:
        out["n_all_units"] = len(np.atleast_1d(_loadmat(files["_SAll.mat"])["S_CellFormat"]))
    w = _loadmat(files["_WSRestrictedIntervals.mat"])
    ints = {}
    for k in ["REMEpisode", "REM", "SWSEpisode", "SWSPacket", "MA", "WakeInterruption", "Wake", "Sleep"]:
        ints[k] = _tp(w[k + "TimePairFormat"])
    ws = w["WakeSleepTimePairFormat"]
    if isinstance(ws, np.ndarray) and ws.dtype == object:
        cyc = [np.asarray(c, float) for c in ws]
    else:
        cyc = [np.asarray(ws, float)]
    ints["WakeSleep"] = [(c[0], c[1]) for c in cyc]  # list of (wake [s,e], sleep [s,e])
    out["ints"] = ints
    u = _loadmat(files["_UPDOWNINtervals.mat"])
    out["up"] = _tp(u["UPIntsTimePairFormat"])
    out["dn"] = _tp(u["DNIntsTimePairFormat"])
    out["upchannel"] = int(u["UPchannel"])
    sp = _loadmat(files["_Spindles.mat"])["SpindleData"]
    ns = np.atleast_2d(sp.normspindles)
    out["spindles"] = {"start": ns[:, 0], "peak": ns[:, 1], "stop": ns[:, 2],
                       "freq": np.atleast_1d(sp.data.peakFrequency).astype(float),
                       "amp_uV": np.atleast_1d(sp.data.peakAmplitude).astype(float) * 1e6,
                       "dur": np.atleast_1d(sp.data.duration).astype(float)}
    out["spindle_chan"] = int(sp.detectionchan)
    mo = _loadmat(files["_Motion.mat"])["motiondata"]
    out["motion"] = np.atleast_1d(np.asarray(mo.motion, float))
    out["motion_thr"] = np.atleast_1d(np.asarray(mo.thresholdedsecs, float))
    out["motion_type"] = str(mo.filttype)
    if "_EMGCorr.mat" in files:
        out["emg"] = np.asarray(_loadmat(files["_EMGCorr.mat"])["EMGCorr"], float)
    if bands is not None:
        tl, L, ts, S = bands
        g, th = out["goodeegchannel"] - 1, out["thetachannel"] - 1
        out["lfp_seconds"] = eeg_bytes / 2 / bands_nch(L) / FS_LFP if len(L) else 0
        out["bands_t"] = tl
        out["bands"] = {k: L[:, g, i] for i, k in enumerate(BANDS)}
        out["bands_theta_chan"] = {k: L[:, th, i] for i, k in enumerate(BANDS)} if th < L.shape[1] else None
        out["short_t"] = ts
        out["short"] = {k: S[:, g, i] for i, k in enumerate(SHORT_BANDS)}
        out["lfp_nch_used"] = L.shape[1]
        if keep_all_channels:
            out["bands_all"] = L
    return out


def bands_nch(L):
    return L.shape[1]


# ----------------------------------------------------------------------------------------------
# DANDI
# ----------------------------------------------------------------------------------------------
def dandi_assets():
    r = requests.get(f"https://api.dandiarchive.org/api/dandisets/{DANDI_ID}/versions/{DANDI_VERSION}/assets/",
                     params={"page_size": 200}, timeout=60).json()
    return sorted([(a["path"], a["asset_id"], a["size"]) for a in r["results"]])


def dandi_url(asset_id):
    r = requests.get(f"https://api.dandiarchive.org/api/assets/{asset_id}/download/", allow_redirects=False, timeout=60)
    return r.headers["Location"]


def _read_channel(url, path, ch, n, nthreads=8):
    import h5py
    import remfile
    loc = threading.local()

    def get(i):
        if not hasattr(loc, "d"):
            loc.d = h5py.File(remfile.File(url), "r")[path]
        return loc.d[i:min(n, i + 2**20), ch]

    with ThreadPoolExecutor(nthreads) as ex:
        out = list(ex.map(get, range(0, n, 2**20)))
    return np.concatenate(out)


def load_dandi(path, asset_id, lfp=True):
    """Stream one NWB file of DANDI:000041 and reduce it to a dict: units (spike times, cell type),
    the sleep_states table, and the LFP of the spindle-reference and theta-reference channels."""
    import h5py
    import remfile
    url = dandi_url(asset_id)
    f = h5py.File(remfile.File(url), "r")
    u = f["units"]
    st = u["spike_times"][:]
    idx = u["spike_times_index"][:]
    spikes = np.split(st, idx[:-1])
    ct = np.array([c.decode() if isinstance(c, bytes) else c for c in u["cell_type"][:]], dtype=object)
    ctype = np.array([{"excitatory": "E", "inhibitory": "I"}.get(c, "?") for c in ct], dtype=object)
    out = {"dataset": "000041", "name": path.split("ses-")[1].split("_ecephys")[0], "path": path,
           "rat": f["general/subject/subject_id"][()].decode(), "spikes": spikes, "ctype": ctype,
           "cell_type_raw": ct,
           "region": np.array([c.decode() for c in u["region"][:]], dtype=object),
           "shank": u["shank"][:], "global_id": u["global_id"][:]}
    s = f["processing/behavior/sleep_states"]
    lab = np.array([x.decode() for x in s["label"][:]])
    out["states_raw"] = (lab, s["start_time"][:], s["stop_time"][:])
    e = f["general/extracellular_ephys/electrodes"]
    out["electrode_location"] = np.array([x.decode() for x in e["location"][:]])
    have_lfp = "LFP" in f["processing/ecephys"]
    out["have_lfp"] = have_lfp
    if lfp and have_lfp:
        d = f["processing/ecephys/LFP/lfp/data"]
        n, nch = d.shape
        out["lfp_shape"] = d.shape
        out["lfp_rate"] = float(f["processing/ecephys/LFP/lfp/starting_time"].attrs["rate"])
        conv = float(d.attrs["conversion"])
        cols = {k: (np.where(e[k][:])[0] if k in e else []) for k in ["spindle_reference", "up_reference", "theta_reference"]}
        # electrodes of the LFP series, in row order of the electrodes table
        lfp_el = f["processing/ecephys/LFP/lfp/electrodes"][:]
        g = int(cols["spindle_reference"][0])
        gcol = int(np.where(lfp_el == g)[0][0])
        out["good_channel_id"] = int(e["channel_id"][g])
        x = _read_channel(url, "processing/ecephys/LFP/lfp/data", gcol, n).astype(np.float32) * conv * 1e6  # uV
        acc = BandAccumulator(1)
        for i in range(0, len(x), int(FS_LFP * 300)):
            acc.add(x[i:i + int(FS_LFP * 300)][:, None])
        tl, L, ts, S = acc.result()
        out["bands_t"], out["bands"] = tl, {k: L[:, 0, i] for i, k in enumerate(BANDS)}
        out["short_t"], out["short"] = ts, {k: S[:, 0, i] for i, k in enumerate(SHORT_BANDS)}
        th = descriptions_theta(f)
        out["bands_theta_chan"] = None
        if th is not None and th != g:
            tcol = int(np.where(lfp_el == th)[0][0])
            out["theta_channel_id"] = int(e["channel_id"][th])
            y = _read_channel(url, "processing/ecephys/LFP/lfp/data", tcol, n).astype(np.float32)
            acc = BandAccumulator(1)
            for i in range(0, len(y), int(FS_LFP * 300)):
                acc.add(y[i:i + int(FS_LFP * 300)][:, None])
            _, Lt, _, _ = acc.result()
            out["bands_theta_chan"] = {k: Lt[:, 0, i] for i, k in enumerate(BANDS)}
        out["lfp_good_uV"] = x
    f.close()
    return out


def descriptions_theta(f):
    """Theta-reference electrode row, from the theta_reference column or, when absent, from the
    ThetaDecompositionSeries description ('channel N' in the lab's numbering)."""
    e = f["general/extracellular_ephys/electrodes"]
    if "theta_reference" in e:
        w = np.where(e["theta_reference"][:])[0]
        return int(w[0]) if len(w) else None
    p = "processing/ecephys/ThetaDecompositionSeries"
    if p in f:
        m = re.search(r"channel (\d+)", f[p].attrs.get("description", ""))
        if m:
            w = np.where(e["channel_id"][:] == int(m.group(1)))[0]
            return int(w[0]) if len(w) else None
    return None


# ----------------------------------------------------------------------------------------------
# States from the DANDI sleep_states table (Awake, Non-REM, REM)
# ----------------------------------------------------------------------------------------------
# [paper] Table S1 and Supplemental Experimental Procedures, Brain state scoring: packets are 20+ s
# of uninterrupted nonREM; MAs are < 40 s arousals between nonREM packets; WAKE interruptions of
# SLEEP are 40-120 s; SLEEP is 20+ min of nonREM, REM and MA with no interruption > 2 min; WAKE is
# 7+ min of not-REM, not-nonREM with interruptions < 2 min; a WAKE-SLEEP cycle is a WAKE immediately
# followed by a SLEEP; a nonREM episode is a span of packets and MAs (interruptions < 40 s) between
# WAKE or REM; a REM episode begins and ends in REM with interruptions up to 40 s, not nonREM.
MA_MAX, WI_MAX, SLEEP_MIN, WAKE_MIN, PACKET_MIN = 40.0, 120.0, 1200.0, 420.0, 20.0
# [standard] The DANDI table leaves 1 s between consecutive epochs (scoring at 1 s resolution);
# epochs closer than ADJ are treated as adjacent.
ADJ = 2.0


def derive_states(lab, start, stop):
    """Build the paper's intervals from a sequence of scored epochs."""
    o = np.argsort(start)
    lab, start, stop = np.asarray(lab)[o], np.asarray(start, float)[o], np.asarray(stop, float)[o]
    n = len(lab)
    dur = stop - start
    is_s = lab != "Awake"
    # SLEEP: maximal runs of sleep epochs and Awake epochs <= 120 s, bounded by sleep epochs
    sleeps = []
    i = 0
    while i < n:
        if not is_s[i]:
            i += 1
            continue
        j = i
        k = i
        while k + 1 < n and (is_s[k + 1] or dur[k + 1] <= WI_MAX):
            k += 1
            if is_s[k]:
                j = k
        if stop[j] - start[i] >= SLEEP_MIN:
            sleeps.append((i, j))
        i = j + 1
    # WAKE: maximal runs of Awake epochs and sleep interruptions < 120 s, bounded by Awake epochs.
    # [assumed] SLEEP takes precedence: a WAKE ends where a SLEEP begins (else the first packets of
    # a SLEEP would be read as an interruption of the WAKE before it).
    insleep = np.zeros(n, bool)
    for a, b in sleeps:
        insleep[a:b + 1] = True
    wakes = []
    i = 0
    while i < n:
        if is_s[i] or insleep[i]:
            i += 1
            continue
        j = i
        k = i
        while k + 1 < n:
            # total sleep time of a contiguous interruption
            m = k + 1
            tot = 0.0
            while m < n and is_s[m]:
                tot += dur[m]
                m += 1
            if m < n and insleep[k + 1:m + 1].any():
                break
            if m == k + 1:  # next is awake
                k = m
                j = k
                continue
            if m < n and tot < WI_MAX and start[m] - stop[k] < WI_MAX + ADJ * (m - k):
                k = m
                j = k
                continue
            break
        if stop[j] - start[i] >= WAKE_MIN:
            wakes.append((i, j))
        i = j + 1
    W = np.array([[start[a], stop[b]] for a, b in wakes]).reshape(-1, 2)
    S = np.array([[start[a], stop[b]] for a, b in sleeps]).reshape(-1, 2)
    cycles = []
    for w in W:
        nxt = S[(S[:, 0] >= w[1] - ADJ) & (S[:, 0] <= w[1] + ADJ)]
        if len(nxt):
            cycles.append((w.copy(), nxt[0].copy()))
    packets = np.array([[start[i], stop[i]] for i in range(n) if lab[i] == "Non-REM" and dur[i] >= PACKET_MIN]).reshape(-1, 2)
    ma, wi = [], []
    for i in range(1, n - 1):
        if lab[i] == "Awake" and lab[i - 1] == "Non-REM" and lab[i + 1] == "Non-REM" and dur[i] < MA_MAX:
            ma.append([start[i], stop[i]])
    for i in range(n):
        if lab[i] == "Awake" and MA_MAX <= dur[i] <= WI_MAX and any((start[i] >= s0) & (stop[i] <= s1) for s0, s1 in S):
            wi.append([start[i], stop[i]])
    rem = np.array([[start[i], stop[i]] for i in range(n) if lab[i] == "REM"]).reshape(-1, 2)
    # REM episodes: REM epochs joined across non-nonREM interruptions up to 40 s
    remep = []
    for i in range(n):
        if lab[i] != "REM":
            continue
        if remep and remep[-1][2] is not None:
            last = remep[-1]
            between = [k for k in range(last[2] + 1, i)]
            if between and all(lab[k] == "Awake" for k in between) and start[i] - last[1] <= MA_MAX + ADJ:
                last[1] = stop[i]
                last[2] = i
                continue
        remep.append([start[i], stop[i], i])
    remep = np.array([[a, b] for a, b, _ in remep]).reshape(-1, 2)
    # nonREM episodes: runs of nonREM and MA epochs (Awake < 40 s between nonREM), starting and
    # ending with nonREM
    epis = []
    i = 0
    while i < n:
        if lab[i] != "Non-REM":
            i += 1
            continue
        j = i
        while j + 2 < n and lab[j + 1] == "Awake" and dur[j + 1] < MA_MAX and lab[j + 2] == "Non-REM":
            j += 2
        epis.append([start[i], stop[j]])
        i = j + 1
    return {"Wake": W, "Sleep": S, "WakeSleep": cycles, "SWSPacket": packets,
            "MA": np.array(ma).reshape(-1, 2), "WakeInterruption": np.array(wi).reshape(-1, 2),
            "REM": rem, "REMEpisode": remep, "SWSEpisode": np.array(epis).reshape(-1, 2)}


# ----------------------------------------------------------------------------------------------
# Event detection on the DANDI LFP and spikes (reading b of the claims)
# ----------------------------------------------------------------------------------------------
def _runs(mask):
    d = np.diff(np.r_[0, mask.astype(np.int8), 0])
    return np.c_[np.where(d == 1)[0], np.where(d == -1)[0]]


def _restrict_mask(n, fs, ints):
    m = np.zeros(n, bool)
    for a, b in ints:
        m[max(0, int(a * fs)):min(n, int(b * fs))] = True
    return m


def detect_spindles(x, packets, fs=FS_LFP):
    """[paper] Supplemental Experimental Procedures, Detection of sleep spindles: 10-20 Hz band,
    rectified, threshold 2 SD above the mean; parts more than 30 ms apart not joined; 200-3000 ms;
    events < 300 ms apart combined; high-voltage spindles (6-9 Hz, 7 SD) overlapping removed.
    [standard] 4th-order Butterworth, zero phase; the Hilbert envelope stands for the profile of
    rectified half-cycles; mean and SD over nonREM packets. Returns start, peak, stop, freq, amp."""
    m = _restrict_mask(len(x), fs, packets)
    b, a = signal.butter(4, [10 / (fs / 2), 20 / (fs / 2)], "band")
    y = signal.filtfilt(b, a, x)
    env = np.abs(signal.hilbert(y))
    mu, sd = env[m].mean(), env[m].std()
    above = (env > mu + 2 * sd) & m
    r = _runs(above)
    # join parts closer than 30 ms
    ev = []
    for s0, e0 in r:
        if ev and s0 - ev[-1][1] <= 0.03 * fs:
            ev[-1][1] = e0
        else:
            ev.append([s0, e0])
    # combine events < 300 ms apart
    ev2 = []
    for s0, e0 in ev:
        if ev2 and s0 - ev2[-1][1] < 0.3 * fs:
            ev2[-1][1] = e0
        else:
            ev2.append([s0, e0])
    ev2 = np.array(ev2).reshape(-1, 2)
    d = (ev2[:, 1] - ev2[:, 0]) / fs
    ev2 = ev2[(d >= 0.2) & (d <= 3.0)]
    b2, a2 = signal.butter(4, [6 / (fs / 2), 9 / (fs / 2)], "band")
    env2 = np.abs(signal.hilbert(signal.filtfilt(b2, a2, x)))
    hv = env2 > env2[m].mean() + 7 * env2[m].std()
    keep = np.array([not hv[s0:e0].any() for s0, e0 in ev2], bool)
    ev2 = ev2[keep] if len(ev2) else ev2
    out = {"start": [], "peak": [], "stop": [], "freq": [], "amp_uV": [], "dur": []}
    for s0, e0 in ev2:
        seg = y[s0:e0]
        pk = s0 + int(np.argmax(env[s0:e0]))
        zc = np.where(np.diff(np.signbit(seg)))[0]
        fr = (len(zc) - 1) / 2 / ((zc[-1] - zc[0]) / fs) if len(zc) > 2 else np.nan
        out["start"].append(s0 / fs)
        out["peak"].append(pk / fs)
        out["stop"].append(e0 / fs)
        out["freq"].append(fr)
        out["amp_uV"].append(env[pk])
        out["dur"].append((e0 - s0) / fs)
    return {k: np.array(v) for k, v in out.items()}


def detect_updown(spikes, x, packets, fs=FS_LFP):
    """[paper] Supplemental Experimental Procedures, Detection of UP and DOWN states: OFF periods
    of population-wide silence of 75-1250 ms; ON periods between OFFs with at least 10 spikes,
    200-4000 ms; LowGammaPower epochs with power in the 100 Hz+ range below 0.5 SD below the mean,
    75-1250 ms; DOWN = OFF coinciding with LowGammaPower; DOWNs separated by a single spike
    combined; UP = ON immediately following a DOWN, truncated by DOWN or OFF.
    [assumed] 100-400 Hz band (the LFP is sampled at 1250 Hz), Hilbert power smoothed over 25 ms,
    log-transformed and z-scored over nonREM packets; detection within nonREM packets; all units pooled."""
    mua = np.sort(np.concatenate(spikes))
    b, a = signal.butter(4, [100 / (fs / 2), 400 / (fs / 2)], "band")
    p = np.abs(signal.hilbert(signal.filtfilt(b, a, x))) ** 2
    k = int(0.025 * fs)
    p = np.convolve(p, np.ones(k) / k, "same")
    m = _restrict_mask(len(x), fs, packets)
    # [assumed] on log power: the linear power is so right-skewed that it never falls 0.5 SD below
    # its mean (5th percentile -0.40 SD in BWRat17-121912), so the rule can only be applied to the
    # log of the power.
    lp = np.log(p + 1e-12)
    z = (lp - lp[m].mean()) / lp[m].std()
    lg = _runs((z < -0.5) & m) / fs
    d = lg[:, 1] - lg[:, 0]
    lg = lg[(d >= 0.075) & (d <= 1.25)]
    ups, dns = [], []
    for a0, b0 in packets:
        t = mua[(mua >= a0) & (mua <= b0)]
        if len(t) < 20:
            continue
        isi = np.diff(t)
        off_i = np.where((isi >= 0.075) & (isi <= 1.25))[0]
        offs = np.c_[t[off_i], t[off_i + 1]]
        # DOWN: OFF overlapping a low-gamma epoch
        if len(lg):
            j = np.searchsorted(lg[:, 0], offs[:, 1])
            ov = np.zeros(len(offs), bool)
            for q in range(len(offs)):
                for jj in (j[q] - 1, j[q] - 2):
                    if 0 <= jj < len(lg) and lg[jj, 1] > offs[q, 0] and lg[jj, 0] < offs[q, 1]:
                        ov[q] = True
            isdn = ov
        else:
            isdn = np.zeros(len(offs), bool)
        # combine DOWNs separated by a single spike (consecutive OFF indices one ISI apart)
        dn = []
        for q in np.where(isdn)[0]:
            if dn and dn[-1][2] == off_i[q] - 1 and isdn[q - 1]:
                dn[-1][1] = offs[q, 1]
                dn[-1][2] = off_i[q]
            else:
                dn.append([offs[q, 0], offs[q, 1], off_i[q]])
        dn_end = {round(e, 6): True for _, e, _ in dn}
        # ON periods between consecutive OFFs
        for q in range(len(offs) - 1):
            s0, e0 = offs[q, 1], offs[q + 1, 0]
            nsp = off_i[q + 1] - off_i[q]
            if 0.2 <= e0 - s0 <= 4.0 and nsp >= 10 and round(s0, 6) in dn_end:
                ups.append([s0, e0])
        dns += [[s, e] for s, e, _ in dn]
    return np.array(ups).reshape(-1, 2), np.array(dns).reshape(-1, 2)


def reduce_dandi(d):
    """Derive states, detect events, and drop the raw LFP."""
    lab, s0, s1 = d["states_raw"]
    d["ints"] = derive_states(lab, s0, s1)
    if "lfp_good_uV" in d:
        x = d.pop("lfp_good_uV").astype(np.float64)
        pk = d["ints"]["SWSPacket"]
        d["spindles"] = detect_spindles(x, pk)
        d["up"], d["dn"] = detect_updown(d["spikes"], x, pk)
        d["lfp_seconds"] = len(x) / FS_LFP
    return d


# ----------------------------------------------------------------------------------------------
# Common per-session structure
# ----------------------------------------------------------------------------------------------
BURST_ISI = 0.015  # [paper] Results, burst index: ISIs below 15 ms; SEP: "less than or equal to 15ms"


def _clip(ints, a, b):
    ints = np.asarray(ints, float).reshape(-1, 2)
    if len(ints) == 0:
        return ints
    s = np.maximum(ints[:, 0], a)
    e = np.minimum(ints[:, 1], b)
    k = e > s
    return np.c_[s[k], e[k]]


def prepare(sess):
    """Per-cycle intervals of each state, and a per-second grid of counts used by every measure.

    Grid second k covers [k, k+1). States are scored at 1 s resolution ([paper] Table S1, "all
    analyses at 1 second resolution")."""
    I = sess["ints"]
    cyc = []
    for w, s in I["WakeSleep"]:
        w, s = np.asarray(w, float), np.asarray(s, float)
        c = {"wake": w, "sleep": s}
        for k, key in [("packets", "SWSPacket"), ("ma", "MA"), ("rem", "REM"), ("remep", "REMEpisode"),
                       ("episodes", "SWSEpisode"), ("wi", "WakeInterruption")]:
            v = np.asarray(I[key], float).reshape(-1, 2)
            inside = v[(v[:, 0] >= s[0] - 1) & (v[:, 1] <= s[1] + 1)] if len(v) else v
            c[k] = inside[np.argsort(inside[:, 0])] if len(inside) else inside
        cyc.append(c)
    sess["cycles"] = cyc
    spk = sess["spikes"]
    tmax = max([s.max() for s in spk if len(s)] + [max(np.max(np.asarray(v, float)) for v in [I["Wake"], I["Sleep"]] if np.size(v))])
    T = int(np.ceil(tmax)) + 2
    nc = len(spk)
    cnt = np.zeros((nc, T), np.int32)
    bshort = np.zeros((nc, T), np.int32)
    bisi = np.zeros((nc, T), np.int32)
    for i, s in enumerate(spk):
        s = np.sort(s)
        k = np.minimum(s.astype(int), T - 1)
        np.add.at(cnt[i], k, 1)
        if len(s) > 1:
            isi = np.diff(s)
            kk = k[1:]
            same = kk == k[:-1]  # ISIs within one second, so no ISI spans two state intervals
            np.add.at(bisi[i], kk[same], 1)
            np.add.at(bshort[i], kk[same & (isi <= BURST_ISI)], 1)
    G = {"T": T, "cnt": cnt, "bshort": bshort, "bisi": bisi}
    # band powers: long window k spans [k, k+2) s; assign to second k+1 (its centre)
    if "bands" in sess and sess.get("bands") is not None and len(sess.get("bands_t", [])):
        tl = sess["bands_t"]
        idx = np.minimum(np.round(tl - 0.5).astype(int), T - 1)
        for b, v in sess["bands"].items():
            a = np.full(T, np.nan)
            a[idx] = v
            G["bp_" + b] = a
        if sess.get("bands_theta_chan"):
            for b, v in sess["bands_theta_chan"].items():
                a = np.full(T, np.nan)
                a[idx] = v
                G["bt_" + b] = a
    # UP and DOWN states, by start second
    for nm in ["up", "dn"]:
        v = np.asarray(sess.get(nm, np.zeros((0, 2))), float).reshape(-1, 2)
        k = np.minimum(v[:, 0].astype(int), T - 1)
        n_ = np.zeros(T)
        np.add.at(n_, k, 1)
        d_ = np.zeros(T)
        np.add.at(d_, k, v[:, 1] - v[:, 0])
        G[nm + "_n"], G[nm + "_dur"] = n_, d_
        occ = np.zeros(T)  # seconds of the state within each grid second
        for a, b in v:
            ia, ib = int(a), int(b)
            if ia == ib:
                occ[min(ia, T - 1)] += b - a
            else:
                occ[min(ia, T - 1)] += ia + 1 - a
                occ[ia + 1:min(ib, T)] += 1
                if ib < T:
                    occ[ib] += b - ib
        G[nm + "_occ"] = occ
    sp = sess.get("spindles")
    if sp is not None and len(sp["start"]):
        k = np.minimum(np.asarray(sp["start"]).astype(int), T - 1)
        for nm, val in [("sp_n", np.ones(len(k))), ("sp_dur", sp["dur"]), ("sp_freq", sp["freq"]), ("sp_amp", sp["amp_uV"])]:
            a = np.zeros(T)
            ok = np.isfinite(val)
            np.add.at(a, k[ok], np.asarray(val)[ok])
            G[nm] = a
        a = np.zeros(T)
        np.add.at(a, k[np.isfinite(sp["freq"])], 1)
        G["sp_nf"] = a
    # spikes within UP states, per cell and second
    up = np.asarray(sess.get("up", np.zeros((0, 2))), float).reshape(-1, 2)
    if len(up):
        upc = np.zeros((nc, T), np.int32)
        st = up[:, 0]
        for i, s in enumerate(spk):
            j = np.searchsorted(st, s, "right") - 1
            ok = (j >= 0) & (s < up[np.maximum(j, 0), 1])
            k = np.minimum(s[ok].astype(int), T - 1)
            np.add.at(upc[i], k, 1)
        G["upcnt"] = upc
    # motion: per second ([data descriptor] _Motion.mat, one point per second)
    if "motion" in sess:
        a = np.full(T, np.nan)
        m = sess["motion"][:T]
        a[:len(m)] = m
        G["motion"] = a
    sess["G"] = G
    sess["E"] = np.where(sess["ctype"] == "E")[0]
    sess["I"] = np.where(sess["ctype"] == "I")[0]
    return sess


def secs(pieces):
    """Grid seconds covered by intervals at 1 s resolution: [ceil(a), floor(b))."""
    out = [np.arange(int(np.ceil(a)), int(np.floor(b))) for a, b in np.asarray(pieces).reshape(-1, 2)]
    return np.concatenate(out) if out else np.zeros(0, int)


def cell_rates(sess, pieces, cells=None):
    k = secs(pieces)
    k = k[k < sess["G"]["T"]]
    c = sess["G"]["cnt"] if cells is None else sess["G"]["cnt"][cells]
    if len(k) == 0:
        return np.full(c.shape[0], np.nan), 0
    return c[:, k].sum(1) / len(k), len(k)


def state_pieces(sess, state, cycles=None):
    """Intervals of a state within WAKE-SLEEP cycles: 'wake' (the cycle's WAKE), 'nrem' (packets),
    'rem', 'ma'."""
    cyc = sess["cycles"] if cycles is None else cycles
    key = {"wake": None, "nrem": "packets", "rem": "rem", "ma": "ma"}[state]
    out = []
    for c in cyc:
        out.append(c["wake"][None, :] if key is None else c[key])
    return np.concatenate(out) if out else np.zeros((0, 2))


def concat_time_bins(pieces, nbins=None, binlen=None):
    """Split the concatenated time of `pieces` into equal bins (nbins) or bins of binlen seconds
    within each piece. Returns a list of (subpieces, normalized mid-time)."""
    pieces = np.asarray(pieces, float).reshape(-1, 2)
    d = pieces[:, 1] - pieces[:, 0]
    tot = d.sum()
    cum = np.r_[0, np.cumsum(d)]
    out = []
    if tot <= 0:
        return out
    if nbins is not None:
        edges = np.linspace(0, tot, nbins + 1)
        for a, b in zip(edges[:-1], edges[1:]):
            sub = []
            for i, (s, e) in enumerate(pieces):
                lo, hi = max(a, cum[i]), min(b, cum[i + 1])
                if hi > lo:
                    sub.append([s + lo - cum[i], s + hi - cum[i]])
            out.append((np.array(sub), (a + b) / 2 / tot))
    else:
        for i, (s, e) in enumerate(pieces):
            nb = int((e - s) // binlen)
            for j in range(nb):
                a = s + j * binlen
                out.append((np.array([[a, a + binlen]]), (cum[i] + j * binlen + binlen / 2) / tot))
    return out


def gsum(sess, key, pieces):
    k = secs(pieces)
    k = k[k < sess["G"]["T"]]
    a = sess["G"][key]
    return (a[..., k].sum(-1) if a.ndim > 1 else np.nansum(a[k])), len(k)


def gmean(sess, key, pieces):
    k = secs(pieces)
    k = k[k < sess["G"]["T"]]
    a = sess["G"][key][k]
    a = a[np.isfinite(a)]
    return a.mean() if len(a) else np.nan


# ----------------------------------------------------------------------------------------------
# Time-normalized correlations (M3 of the claims file) and slopes (M5)
# ----------------------------------------------------------------------------------------------
def segments(sess, kind):
    """(segment pieces, [packet pieces inside]) for SLEEP (nonREM time only), nonREM episodes,
    packets, REM episodes and WAKE, all within WAKE-SLEEP cycles."""
    out = []
    for c in sess["cycles"]:
        if kind == "sleep":
            if len(c["packets"]):
                out.append(c["packets"])
        elif kind == "episode":
            for e in c["episodes"]:
                out.append(np.array([e]))
        elif kind == "packet":
            for p in c["packets"]:
                out.append(np.array([p]))
        elif kind == "rem":
            for e in c["remep"]:
                out.append(np.array([e]))
        elif kind == "wake":
            out.append(np.array([c["wake"]]))
        elif kind == "sleep_all":
            out.append(np.array([c["sleep"]]))
    return out


def norm_points(sessions, kind, fn, reading, normalize=True, nbins=50, binlen=10.0):
    """Points (normalized time, value, session index) for one reading:
    'a' one point per nonREM packet inside the segment (its value at its normalized mid-time);
    'b' one point per 10 s bin; 'c' nbins equal bins (averaged over segments later).
    Values are divided by the session's mean over its points ([claim] M3)."""
    T, V, S, SEG = [], [], [], []
    for si, s in enumerate(sessions):
        t_, v_, g_ = [], [], []
        for gi, seg in enumerate(segments(s, kind)):
            if reading == "a":
                if kind in ("packet", "rem", "wake"):
                    continue
                d = seg[:, 1] - seg[:, 0]
                tot = d.sum()
                cum = np.r_[0, np.cumsum(d)]
                if kind == "sleep":
                    bins = [(np.array([p]), (cum[i] + d[i] / 2) / tot) for i, p in enumerate(seg)]
                else:  # episode: packets inside it
                    pk = np.concatenate([c["packets"] for c in s["cycles"]]) if s["cycles"] else np.zeros((0, 2))
                    pk = pk[(pk[:, 0] >= seg[0, 0]) & (pk[:, 1] <= seg[0, 1])]
                    bins = [(np.array([p]), ((p[0] + p[1]) / 2 - seg[0, 0]) / tot) for p in pk]
            elif reading == "b":
                bins = concat_time_bins(seg, binlen=binlen)
            else:
                bins = concat_time_bins(seg, nbins=nbins)
            for sub, tn in bins:
                v = fn(s, sub)
                if v is not None and np.isfinite(v):
                    t_.append(tn)
                    v_.append(v)
                    g_.append(gi)
        v_ = np.array(v_, float)
        if normalize and len(v_) and np.nanmean(v_) != 0:
            v_ = v_ / np.nanmean(v_)
        T += t_
        V += list(v_)
        S += [si] * len(t_)
        SEG += g_
    return np.array(T), np.array(V), np.array(S), np.array(SEG)


def norm_corr(sessions, kind, fn, readings=("a", "b", "c"), normalize=True, nbins=50):
    """Pearson R, p and n of value against normalized time, for each reading. Reading c averages
    the per-segment values of each of the nbins bins over all segments (50 points)."""
    from scipy import stats
    res = {}
    for r in readings:
        if r == "a" and kind in ("packet", "rem", "wake"):
            continue
        t, v, s, g = norm_points(sessions, kind, fn, r, normalize, nbins)
        if r == "c":
            if len(t) == 0:
                continue
            b = np.minimum((t * nbins).astype(int), nbins - 1)
            vv = np.array([np.nanmean(v[b == i]) if (b == i).any() else np.nan for i in range(nbins)])
            tt = (np.arange(nbins) + 0.5) / nbins
            ok = np.isfinite(vv)
            t, v = tt[ok], vv[ok]
        if len(t) < 3:
            res[r] = (np.nan, np.nan, len(t))
            continue
        R, p = stats.pearsonr(t, v)
        res[r] = (R, p, len(t))
    return res


def ols_slope(x, y):
    """OLS slope of y on x with its 95% interval, and Pearson R and p ([claim] M5)."""
    from scipy import stats
    x, y = np.asarray(x, float), np.asarray(y, float)
    ok = np.isfinite(x) & np.isfinite(y)
    x, y = x[ok], y[ok]
    r = stats.linregress(x, y)
    tcrit = stats.t.ppf(0.975, len(x) - 2)
    return {"slope": r.slope, "lo": r.slope - tcrit * r.stderr, "hi": r.slope + tcrit * r.stderr,
            "R": r.rvalue, "p": r.pvalue, "n": len(x)}


def log_pairs(a, b):
    a, b = np.asarray(a, float), np.asarray(b, float)
    ok = (a > 0) & (b > 0) & np.isfinite(a) & np.isfinite(b)
    return np.log10(a[ok]), np.log10(b[ok]), int((~ok).sum())


def wake_rate(sess, cells):
    """[claim] M2 reading a: a cell's rate over all scored WAKE intervals of its session."""
    return cell_rates(sess, sess["ints"]["Wake"], cells)[0]


def sextiles(sessions, reading="a"):
    """Assign each pE cell of the whole dataset to a sextile of WAKE rate (0 lowest, 5 highest),
    [claim] M2; reading 'b' uses the WAKE of each cycle (mean over cycles)."""
    allr = []
    for si, s in enumerate(sessions):
        if reading == "a":
            r = wake_rate(s, s["E"])
        else:
            r = np.nanmean([cell_rates(s, [c["wake"]], s["E"])[0] for c in s["cycles"]], 0) if s["cycles"] else np.full(len(s["E"]), np.nan)
        allr.append(r)
    flat = np.concatenate(allr)
    ok = np.isfinite(flat)
    ranks = np.full(len(flat), -1)
    order = np.argsort(flat[ok], kind="stable")
    q = np.zeros(ok.sum(), int)
    q[order] = (np.arange(ok.sum()) * 6) // ok.sum()
    ranks[ok] = q
    out, i = [], 0
    for r in allr:
        out.append(ranks[i:i + len(r)])
        i += len(r)
    for s, sx, r in zip(sessions, out, allr):
        s["sextile"] = sx
        s["wake_rate_E"] = r
    return out


# ----------------------------------------------------------------------------------------------
# Loading whole datasets
# ----------------------------------------------------------------------------------------------
def _dandi_one(a):
    return prepare(reduce_dandi(load_dandi(a[0], a[1])))


def _crcns_one(name):
    return prepare(load_crcns(name))


def load_dataset(ds, workers):
    """All sessions of a dataset, reduced as they stream, `workers` files at a time. [standard]
    Workers are limited so the peak memory stays under about 10 GB (a DANDI file of 11 GB peaks
    near 5 GB while its LFP channel is filtered)."""
    from concurrent.futures import ProcessPoolExecutor
    import multiprocessing as mp
    ctx = mp.get_context("spawn")
    if ds == "000041":
        items, fn = dandi_assets(), _dandi_one
    else:
        items, fn = CRCNS_SESSIONS, _crcns_one
    with ProcessPoolExecutor(workers, mp_context=ctx) as ex:
        return list(ex.map(fn, items))


def crcns_checksums():
    t = requests.get(CRCNS_BASE + "checksums.md5", timeout=60).text
    return dict((l.split()[1], l.split()[0]) for l in t.strip().splitlines())
