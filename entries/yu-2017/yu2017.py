"""Loading and measures for CRCNS hc-13 (Yu et al. 2017, eLife 6:e27621).

The data set is one gzipped tar file, ``hc-13/live/data.tar.gz`` (8.7 GB), read
anonymously from the public S3 bucket ``crcnsarchive``. A gzip stream can only be
read from its start, so the whole archive is streamed once, in its own order, and
each animal is reduced as soon as its six files have arrived (``stream_dataset``).
Nothing is written to disk. The LFP files (MATLAB 7.3, HDF5) are read into one
preallocated buffer and opened in memory with h5py; one animal's LFP is held at a
time.

Where each parameter comes from:

- Movement is speed > 4 cm/s, immobility < 4 cm/s (Methods, Behavioral state
  definition). Speed is computed from the tracked position (the data set's
  ``rawpos``, one position per frame, zeros where untracked). How speed is
  computed is not given (claims file, O3): untracked frames are interpolated
  linearly and speed from frame differences is smoothed with a Gaussian of
  full width at half maximum 0.25 s, a standard choice; unsmoothed speed is kept
  as a variant.
- Reward wells (claims file, O1): the data set has no beam-break times, so
  reading (b) is used: the wells are located from the immobile positions of all
  of an animal's days (``find_wells``); each immobility period (a run of frames at
  speed < 4 cm/s) is assigned to the nearest well, and its start and end are the
  well entry and exit.
- CA1 pyramidal cells: spike width < 0.4 ms, mean rate < 10 Hz, > 200 spikes over
  the day's sessions (Methods, Cell selection). Spike width is the ``spikewidth``
  of cellinfo (ms); the mean rate is the day's spike count over the day's
  session time. IAPs: rate >= 3 Hz during immobility at one or more wells,
  spikes during SWRs excluded (Methods, Cell selection); readings O2 (a) SWR time
  kept in the denominator, (b) removed.
- SWR detection (Methods, SWR detection): CA1 tetrodes (tetinfo ``area`` CA1),
  days with >= 3 of them; 150 to 250 Hz band (a 4th-order Butterworth band-pass
  run forward and back, a standard choice: the paper names no filter); Hilbert
  envelope smoothed with a Gaussian sigma 4 ms; median over tetrodes; z-scored
  with the mean and SD over immobile samples of the day (O5); noise
  distribution from the histogram (0.05 z bins, standard choice) below the
  mode mirrored about it; threshold its 99.99th percentile; events above it
  for >= 20 ms, start and end where the envelope returns to the mean (z = 0);
  events at speed < 4 cm/s at their start kept. Readings O5 (a) envelope
  amplitude, (b) its square. A fixed threshold of 3 SD of the amplitude
  (``fixed3sd``), the standard method the Methods say they replaced, is kept as a
  sensitivity check only. The LFP is used as stored: the data set holds one
  channel per tetrode and does not say how it is referenced; the paper's Methods
  (Recording) say CA1 LFP was referenced to a corpus callosum tetrode, and no
  re-referencing is done.
- Spectral power per SWR (Methods, Spectrograms): multitaper (time-bandwidth 3,
  5 tapers, claims file), 100 ms windows (150 samples, padded to 256 as
  Chronux does by default), z-scored per frequency over the session; the window
  from SWR onset to onset + 100 ms; mean over CA1 tetrodes (claims file). The
  mean and SD per frequency are estimated from windows every 100 ms, not every
  10 ms (a reduction for speed that cannot change the result appreciably).
"""
import io
import tarfile

import h5py
import numpy as np
import scipy.io as sio
from scipy import signal
from scipy.ndimage import gaussian_filter1d

DATASET = "hc-13"
VERSION = "unversioned"  # CRCNS data sets are not versioned (docs/archives.md); checked by MD5
MD5 = "f45a799b63c543d82d61933c0c87efbb"  # data.tar.gz in hc-13/live/checksums.md5
URL = "https://crcnsarchive.s3-us-west-2.amazonaws.com/hc-13/live/data.tar.gz"
FILE_TYPES = ("eeg", "rawpos", "spikes", "cellinfo", "task", "tetinfo")
SPEED_THR = 4.0


class _MemFile(io.RawIOBase):
    """A seekable read-only file over a bytearray, so h5py can open it."""

    def __init__(self, buf):
        self.m = memoryview(buf)
        self.p = 0

    def readable(self):
        return True

    def seekable(self):
        return True

    def seek(self, o, w=0):
        self.p = o if w == 0 else (self.p + o if w == 1 else len(self.m) + o)
        return self.p

    def tell(self):
        return self.p

    def readinto(self, b):
        n = min(len(b), len(self.m) - self.p)
        b[:n] = self.m[self.p:self.p + n]
        self.p += n
        return n


def _plain(x):
    """Turn scipy mat_struct objects (left by simplify_cells inside some cells) into dicts, recursively."""
    if isinstance(x, sio.matlab.mat_struct):
        return {k: _plain(getattr(x, k)) for k in x._fieldnames}
    if isinstance(x, dict):
        return {k: _plain(v) for k, v in x.items()}
    if isinstance(x, np.ndarray) and x.dtype == object:
        out = np.empty(x.size, dtype=object)
        for i, v in enumerate(x.ravel()):
            out[i] = _plain(v)
        return out.reshape(x.shape)
    if isinstance(x, list):
        return [_plain(v) for v in x]
    return x


def _cells(x):
    """Iterate a MATLAB cell vector loaded by scipy (simplify_cells) as (1-based index, item)."""
    if isinstance(x, np.ndarray) and x.dtype == object:
        for i, v in enumerate(x.ravel()):
            if isinstance(v, np.ndarray) and v.size == 0:
                continue
            if isinstance(v, (list, tuple)) and len(v) == 0:
                continue
            yield i + 1, v
    elif isinstance(x, (list, tuple)):
        for i, v in enumerate(x):
            if isinstance(v, np.ndarray) and v.size == 0:
                continue
            if isinstance(v, (list, tuple)) and len(v) == 0:
                continue
            yield i + 1, v
    elif isinstance(x, dict):
        yield 1, x


class _Hashing:
    """A read-only stream wrapper that keeps the MD5 of the bytes read, to compare with checksums.md5."""

    def __init__(self, f):
        import hashlib
        self.f, self.md5, self.n = f, hashlib.md5(), 0

    def read(self, n=-1):
        b = self.f.read(n)
        self.md5.update(b)
        self.n += len(b)
        return b


def stream_dataset(process, animals=None, block_size=2 ** 24, log=print):
    """Stream the archive once and call ``process(animal, files)`` for each animal.

    ``files`` maps file type to the loaded MATLAB variable (scipy, simplified
    cells) and, for ``eeg``, to an open h5py File. Returns {animal: result}.
    ``animals`` restricts which animals are processed; the stream stops after
    the last one (S2 comes first in the archive, so it is the quick subset).
    """
    import fsspec
    raw = fsspec.open(URL, block_size=block_size).open()
    f = _Hashing(raw)
    tf = tarfile.open(fileobj=f, mode="r|gz")
    pending, out, members = {}, {}, []
    for m in tf:
        if not m.isfile():
            continue
        parts = m.name.split("/")
        animal, fname = parts[1], parts[2]
        kind = fname[len(animal):-4]
        members.append((m.name, m.size))
        if animals is not None and animal not in animals:
            if all(a in out for a in animals):
                break
            continue
        fo = tf.extractfile(m)
        if kind == "eeg":
            buf = bytearray(m.size)
            mv, p = memoryview(buf), 0
            while p < m.size:
                p += fo.readinto(mv[p:p + 2 ** 24])
            pending.setdefault(animal, {})["eeg"] = h5py.File(_MemFile(buf), "r")
        else:
            d = sio.loadmat(io.BytesIO(fo.read()), simplify_cells=True)
            pending.setdefault(animal, {})[kind] = _plain(d[kind])
        if len(pending[animal]) == len(FILE_TYPES):
            log(f"processing {animal}")
            out[animal] = process(animal, pending.pop(animal))
    if animals is None:
        while f.read(2 ** 24):
            pass
    return out, dict(members=members, md5=f.md5.hexdigest() if animals is None else None, bytes=f.n)


# ---------------------------------------------------------------- position


def speed_from_rawpos(rp, fwhm_s=0.25):
    """Times, x, y (cm), smoothed speed and unsmoothed speed (cm/s) from one rawpos epoch."""
    d = np.asarray(rp["data"], float)
    cm = float(rp["cm_per_pixel"])
    t = d[:, 0]
    x, y = d[:, 1].copy(), d[:, 2].copy()
    ok = ~((x == 0) & (y == 0))
    x = np.interp(t, t[ok], x[ok]) * cm
    y = np.interp(t, t[ok], y[ok]) * cm
    dt = np.gradient(t)
    raw = np.hypot(np.gradient(x), np.gradient(y)) / dt
    fs = 1.0 / np.median(np.diff(t))
    sig = fwhm_s / 2.3548 * fs
    sp = gaussian_filter1d(raw, sig)
    return dict(t=t, x=x, y=y, speed=sp, speed_raw=raw, tracked=ok, cm_per_pixel=cm, fs=fs)


def runs(mask):
    """Start and end indices (end exclusive) of runs of True."""
    m = np.concatenate([[False], mask, [False]]).astype(int)
    d = np.diff(m)
    return np.flatnonzero(d == 1), np.flatnonzero(d == -1)


def find_wells(xs, ys, binsize=4.0):
    """The four wells: in each quadrant of the tracked area, the peak of the immobile occupancy.

    Positions are histogrammed in 4 cm bins and smoothed (Gaussian, sigma one bin);
    the quadrants are split at the midpoints of the x and y ranges. The wells are
    at the four corners of the maze (Methods, Behavior tasks; Figure 1, supplement
    1A) and the animal is immobile mostly at them (Methods, Behavioral state
    definition), so the occupancy peak in the outer part of each quadrant (beyond a
    quarter of the range from the centre, as some rats also rest at the centre) is
    taken as its well. A standard choice; returned in order around the maze.
    """
    from scipy.ndimage import gaussian_filter
    pts = np.column_stack([xs, ys])
    lo, hi = pts.min(0), pts.max(0)
    mid = (lo + hi) / 2
    xe = np.arange(lo[0], hi[0] + binsize, binsize)
    ye = np.arange(lo[1], hi[1] + binsize, binsize)
    h = gaussian_filter(np.histogram2d(pts[:, 0], pts[:, 1], [xe, ye])[0], 1.0)
    xc, yc = 0.5 * (xe[1:] + xe[:-1]), 0.5 * (ye[1:] + ye[:-1])
    X, Yg = np.meshgrid(xc, yc, indexing="ij")
    wells = []
    for sx, sy in ((-1, -1), (1, -1), (1, 1), (-1, 1)):
        q = ((X - mid[0]) * sx > 0.25 * (hi[0] - lo[0])) & ((Yg - mid[1]) * sy > 0.25 * (hi[1] - lo[1]))
        i = np.argmax(np.where(q, h, -1))
        wells.append((X.ravel()[i], Yg.ravel()[i]))
    wells = np.array(wells)
    lab = np.argmin(((pts[:, None, :] - wells[None]) ** 2).sum(-1), 1)
    return wells, lab


# ---------------------------------------------------------------- SWRs

def ripple_envelope(x, fs, band=(150, 250), sigma_s=0.004):
    b, a = signal.butter(4, [band[0] / (fs / 2), band[1] / (fs / 2)], btype="band")
    y = signal.filtfilt(b, a, x)
    env = np.abs(signal.hilbert(y))
    return gaussian_filter1d(env, sigma_s * fs)


def noise_threshold(z, binw=0.05, pct=99.99):
    """Mode of the histogram of z; mirror the part below the mode; its pct-th percentile."""
    lo, hi = np.percentile(z, [0.01, 99.9])
    edges = np.arange(lo, hi + binw, binw)
    h, e = np.histogram(z, edges)
    mode = 0.5 * (e[np.argmax(h)] + e[np.argmax(h) + 1])
    below = mode - z[z < mode]
    # mirrored distribution: |X - mode| has the distribution of `below`; its
    # pct-th percentile is mode + the (1 - 2 (1 - pct/100)) quantile of `below`
    q = 1 - 2 * (1 - pct / 100)
    return mode, mode + np.quantile(below, q)


def detect_events(z, fs, thr, min_s=0.020):
    """Events where z > thr for >= min_s; bounds extended to where z returns to 0. Merged when they overlap."""
    s, e = runs(z > thr)
    keep = (e - s) >= int(round(min_s * fs))
    s, e = s[keep], e[keep]
    below = np.flatnonzero(z <= 0)
    out = []
    for a, b in zip(s, e):
        i = np.searchsorted(below, a)
        st = below[i - 1] + 1 if i > 0 else 0
        j = np.searchsorted(below, b)
        en = below[j] if j < len(below) else len(z)
        if out and st <= out[-1][1]:
            out[-1][1] = max(out[-1][1], en)
            out[-1][2] = max(out[-1][2], z[a:b].max())
        else:
            out.append([st, en, z[a:b].max()])
    return np.array(out).reshape(-1, 3)


def dpss_power(x, fs, starts_idx, nwin=150, nfft=256, NW=3, K=5, stat_step=150):
    """Multitaper power for windows starting at the given sample indices, z-scored per frequency.

    Mean and SD per frequency from windows every ``stat_step`` samples over the epoch.
    Returns frequencies and the z-scored power of each requested window.
    """
    tapers = signal.windows.dpss(nwin, NW, K)
    freqs = np.fft.rfftfreq(nfft, 1 / fs)

    def power(idx):
        idx = idx[(idx >= 0) & (idx + nwin <= len(x))]
        seg = x[idx[:, None] + np.arange(nwin)[None, :]]
        seg = seg - seg.mean(1, keepdims=True)
        p = np.zeros((len(idx), len(freqs)))
        for tp in tapers:
            p += np.abs(np.fft.rfft(seg * tp, nfft)) ** 2
        return p / K, idx

    pstat, _ = power(np.arange(0, len(x) - nwin, stat_step))
    mu, sd = pstat.mean(0), pstat.std(0)
    starts_idx = np.asarray(starts_idx, int)
    valid = (starts_idx >= 0) & (starts_idx + nwin <= len(x))
    pz = np.full((len(starts_idx), len(freqs)), np.nan)
    if valid.any():
        p, _ = power(starts_idx[valid])
        pz[valid] = (p - mu) / sd
    return freqs, pz


# ---------------------------------------------------------------- per animal


def _eeg_tetrodes(h, day, ep):
    """{tetrode: (starttime, samprate, h5py dataset)} for one day and epoch of an hc-13 eeg file."""
    e = h["eeg"][()].ravel()
    if day > len(e):
        return {}
    d = h[e[day - 1]]
    if not isinstance(d, h5py.Dataset) or d.dtype != object:
        return {}
    eps = d[()].ravel()
    if ep > len(eps):
        return {}
    x = h[eps[ep - 1]]
    if not isinstance(x, h5py.Dataset) or x.dtype != object:
        return {}
    out = {}
    for ti, r in enumerate(x[()].ravel()):
        g = h[r]
        if isinstance(g, h5py.Group) and "data" in g:
            out[ti + 1] = (float(g["starttime"][()].ravel()[0]), float(g["samprate"][()].ravel()[0]), g["data"])
    return out


def process_animal(animal, files):
    """Reduce one animal: positions, units, SWRs (both readings of O5) and per-SWR power."""
    res = dict(animal=animal, days={}, units=[], tet_area={}, eeg_info={})
    rawpos, spikes, cellinfo, tetinfo, task = (files[k] for k in ("rawpos", "spikes", "cellinfo", "tetinfo", "task"))
    h = files["eeg"]
    for day, eps in _cells(rawpos):
        dd = dict(epochs={}, swr={}, tasktype={})
        for ep, rp in _cells(eps):
            dd["epochs"][ep] = speed_from_rawpos(rp)
        try:
            for ep, tk in _cells(task[day - 1]):
                dd["tasktype"][ep] = tk.get("type") if isinstance(tk, dict) else None
        except Exception:
            pass
        res["days"][day] = dd
    # tetrode areas per day (first epoch that has them)
    for day, eps in _cells(tetinfo):
        areas = {}
        for ep, tets in _cells(eps):
            for ti, ttt in _cells(tets):
                if isinstance(ttt, dict) and "area" in ttt:
                    areas.setdefault(ti, str(ttt["area"]))
        res["tet_area"][day] = areas
    # units: spikes{day}{ep}{tet}{unit}; one unit per (day, tet, unit), times per epoch
    for day, eps in _cells(spikes):
        ud = {}
        for ep, tets in _cells(eps):
            for ti, us in _cells(tets):
                for ui, u in _cells(us):
                    if not isinstance(u, dict):
                        continue
                    dat = np.asarray(u.get("data", []), float)
                    times = dat[:, 0] if dat.ndim == 2 and dat.size else np.zeros(0)
                    rec = ud.setdefault((ti, ui), dict(animal=animal, day=day, tet=ti, unit=ui, spikes={},
                                                       spikewidth_pts=float(np.ravel(u.get("spikewidth", np.nan))[0]) if np.size(u.get("spikewidth", [])) else np.nan))
                    rec["spikes"][ep] = times
        for (ti, ui), rec in ud.items():
            ci = None
            try:
                ci = cellinfo[day - 1]
                for ep in sorted(rec["spikes"]):
                    c = ci[ep - 1][ti - 1][ui - 1]
                    if isinstance(c, dict) and "spikewidth" in c:
                        ci = c
                        break
                else:
                    ci = None
            except Exception:
                ci = None
            rec["area"] = str(ci["area"]) if ci is not None and "area" in ci else res["tet_area"].get(day, {}).get(ti, "")
            rec["spikewidth_ms"] = float(np.ravel(ci["spikewidth"])[0]) if ci is not None else rec["spikewidth_pts"] / 30
            res["units"].append(rec)
    # SWRs per day
    for day, dd in res["days"].items():
        ca1 = sorted(t for t, a in res["tet_area"].get(day, {}).items() if a == "CA1")
        res["eeg_info"][day] = dict(ca1_tetrodes=ca1)
        if len(ca1) < 3:
            continue
        envs = {}
        for ep, pos in dd["epochs"].items():
            tets = _eeg_tetrodes(h, day, ep)
            use = [t for t in ca1 if t in tets]
            if len(use) < 3:
                continue
            # Tetrodes of one epoch can start at different times (up to 45 ms apart in R1 and
            # N2): each is trimmed to the latest start, so the median is taken over aligned samples.
            fs = tets[use[0]][1]
            st = max(tets[t][0] for t in use)
            skip = {t: int(round((st - tets[t][0]) * fs)) for t in use}
            n = min(tets[t][2].shape[-1] - skip[t] for t in use)
            lfp = {}
            E = np.empty((len(use), n))
            for k, t in enumerate(use):
                x = np.asarray(tets[t][2][()], float).ravel()[skip[t]:skip[t] + n]
                lfp[t] = x.astype(np.float32)
                E[k] = ripple_envelope(x, fs)
            cons = np.median(E, 0)
            del E
            tt = st + np.arange(n) / fs
            sp = np.interp(tt, pos["t"], pos["speed"])
            envs[ep] = dict(t=tt, env=cons, speed=sp, fs=fs, lfp=lfp, starts={t: st for t in use})
            res["eeg_info"][day].setdefault("epochs", {})[ep] = dict(starttime=st, samprate=fs, n=n, tetrodes=use,
                                                                     starttimes=[tets[t][0] for t in use])
        if not envs:
            continue
        for reading, power in (("amplitude", 1), ("squared", 2), ("fixed3sd", 1)):
            vals = {ep: v["env"] ** power for ep, v in envs.items()}
            imm = np.concatenate([vals[ep][v["speed"] < SPEED_THR] for ep, v in envs.items()])
            mu, sd = imm.mean(), imm.std()
            zimm = (imm - mu) / sd
            mode, thr = noise_threshold(zimm)
            if reading == "fixed3sd":
                # Sensitivity check, not the paper's method: the fixed 3 SD threshold the Methods name as
                # the standard one they replaced (Methods, SWR detection, paragraph 2).
                thr = 3.0
            rows = []
            n_imm = n_imm_in = 0
            for ep, v in envs.items():
                z = (vals[ep] - mu) / sd
                ev = detect_events(z, v["fs"], thr)
                inside = np.zeros(len(z), bool)
                for a, b, pk in ev:
                    a, b = int(a), int(b)
                    inside[a:b] = True
                    rows.append((ep, v["t"][a], v["t"][min(b, len(z) - 1)], pk, v["speed"][a]))
                im = v["speed"] < SPEED_THR
                n_imm += im.sum()
                n_imm_in += (inside & im).sum()
            ev = np.array(rows).reshape(-1, 5)
            keep = ev[:, 4] < SPEED_THR
            dd["swr"][reading] = dict(epoch=ev[keep, 0].astype(int), start=ev[keep, 1], end=ev[keep, 2],
                                      peak=ev[keep, 3], n_all=len(ev), mode=mode, thr=thr, mu=mu, sd=sd,
                                      frac_imm_in_events=n_imm_in / max(n_imm, 1),
                                      frac_imm_above_thr=float((zimm > thr).mean()))
        # spectral power for the main reading's SWRs
        sw = dd["swr"]["amplitude"]
        p_rip = np.full(len(sw["start"]), np.nan)
        p_gam = np.full(len(sw["start"]), np.nan)
        for ep, v in envs.items():
            sel = np.flatnonzero(sw["epoch"] == ep)
            if not len(sel):
                continue
            acc_r, acc_g = [], []
            for t, x in v["lfp"].items():
                idx = np.round((sw["start"][sel] - v["starts"][t]) * v["fs"]).astype(int)
                fr, pz = dpss_power(x.astype(float), v["fs"], idx)
                acc_r.append(pz[:, (fr >= 150) & (fr <= 250)].mean(1))
                acc_g.append(pz[:, (fr >= 25) & (fr <= 35)].mean(1))
            p_rip[sel] = np.nanmean(acc_r, 0)
            p_gam[sel] = np.nanmean(acc_g, 0)
        sw["power_ripple"] = p_rip
        sw["power_gamma"] = p_gam
        dd["swr_env_stats"] = {ep: dict(n=len(v["env"])) for ep, v in envs.items()}
        del envs
    files["eeg"].close()
    return res


# ---------------------------------------------------------------- analysis tables


def day_tables(res, speed_key="speed"):
    """Per day: immobility periods with their well, the wells, and session durations.

    Immobility periods are runs of position frames with speed < 4 cm/s (O1 (b)).
    """
    out = {}
    # The maze and camera are fixed: wells are located once per animal from the immobile
    # positions of all its days (day-wise clusters drift onto rarely visited wells' paths).
    xs, ys = [], []
    for dd in res["days"].values():
        for ep, p in dd["epochs"].items():
            m = p[speed_key] < SPEED_THR
            xs.append(p["x"][m])
            ys.append(p["y"][m])
    wells, _ = find_wells(np.concatenate(xs), np.concatenate(ys))
    for day, dd in res["days"].items():
        per = []
        for ep, p in dd["epochs"].items():
            s, e = runs(p[speed_key] < SPEED_THR)
            for a, b in zip(s, e):
                cx, cy = p["x"][a:b].mean(), p["y"][a:b].mean()
                w = int(np.argmin(((wells - [cx, cy]) ** 2).sum(1)))
                t0 = p["t"][a]
                t1 = p["t"][b] if b < len(p["t"]) else p["t"][-1]
                per.append((ep, t0, t1, w, np.hypot(*(wells[w] - [cx, cy]))))
        per = np.array(per)
        dur = {ep: p["t"][-1] - p["t"][0] for ep, p in dd["epochs"].items()}
        out[day] = dict(wells=wells, periods=dict(epoch=per[:, 0].astype(int), start=per[:, 1], end=per[:, 2],
                                                  well=per[:, 3].astype(int), dist=per[:, 4]), session_s=dur)
    return out


def in_intervals(t, starts, ends):
    """Boolean: t inside any [start, end) (intervals sorted, non-overlapping)."""
    if len(starts) == 0:
        return np.zeros(len(t), bool)
    o = np.argsort(starts)
    s, e = np.asarray(starts)[o], np.asarray(ends)[o]
    i = np.searchsorted(s, t, side="right") - 1
    ok = i >= 0
    r = np.zeros(len(t), bool)
    r[ok] = t[ok] < e[i[ok]]
    return r


def interval_overlap(starts, ends, xs, xe):
    """Total overlap of each [starts, ends) with the union of [xs, xe)."""
    out = np.zeros(len(starts))
    for k, (a, b) in enumerate(zip(starts, ends)):
        j0 = np.searchsorted(xe, a)
        j1 = np.searchsorted(xs, b)
        if j1 > j0:
            out[k] = np.clip(np.minimum(xe[j0:j1], b) - np.maximum(xs[j0:j1], a), 0, None).sum()
    return out


def classify_ca1(res, tables, swr_reading="amplitude", o2="a", rate_thr=3.0, width_max=0.4):
    """CA1 putative pyramidal cells of each day and their IAP/MAP label (Methods, Cell selection).

    Returns a list of dicts with day, tetrode, unit, spikes (concatenated over the
    day's sessions), the well rates and the label. ``o2``: 'a' keeps SWR time in
    the denominator, 'b' removes it.
    """
    cells = []
    for u in res["units"]:
        if u["area"] != "CA1":
            continue
        day = u["day"]
        if day not in tables:
            continue
        dd = res["days"][day]
        tb = tables[day]
        sp = np.sort(np.concatenate([u["spikes"].get(ep, np.zeros(0)) for ep in dd["epochs"]]))
        T = sum(tb["session_s"].values())
        n = len(sp)
        rate = n / T
        if not (u["spikewidth_ms"] < width_max and rate < 10 and n > 200):
            continue
        sw = dd["swr"].get(swr_reading)
        per = tb["periods"]
        if sw is not None and len(sw["start"]):
            o = np.argsort(sw["start"])
            ss, se = sw["start"][o], sw["end"][o]
        else:
            ss = se = np.zeros(0)
        nos = sp[~in_intervals(sp, ss, se)]
        rates = np.zeros(4)
        for w in range(4):
            m = per["well"] == w
            ps, pe = per["start"][m], per["end"][m]
            o = np.argsort(ps)
            ps, pe = ps[o], pe[o]
            cnt = in_intervals(nos, ps, pe).sum()
            dur = (pe - ps).sum()
            if o2 == "b":
                dur -= interval_overlap(ps, pe, ss, se).sum()
            rates[w] = cnt / dur if dur > 0 else 0.0
        cells.append(dict(animal=res["animal"], day=day, tet=u["tet"], unit=u["unit"], spikes=sp, n=n, rate=rate,
                          well_rates=rates, best_well=int(np.argmax(rates)),
                          label="IAP" if rates.max() >= rate_thr else "MAP"))
    return cells


# ---------------------------------------------------------------- correlograms and SWR content


def lags(a, b, maxlag):
    """All lags b - a within +-maxlag for sorted spike trains a and b."""
    if len(a) == 0 or len(b) == 0:
        return np.zeros(0)
    lo = np.searchsorted(b, a - maxlag, side="left")
    hi = np.searchsorted(b, a + maxlag, side="right")
    n = hi - lo
    if n.sum() == 0:
        return np.zeros(0)
    idx = np.repeat(np.arange(len(a)), n)
    off = np.arange(n.sum()) - np.repeat(np.cumsum(n) - n, n)
    return b[np.repeat(lo, n) + off] - a[idx]


def window_spikes(sp, centers, half):
    """Spikes within +-half of any centre, with the index of the window (spikes in two windows appear twice)."""
    lo = np.searchsorted(sp, centers - half)
    hi = np.searchsorted(sp, centers + half)
    n = hi - lo
    idx = np.repeat(np.arange(len(centers)), n)
    off = np.arange(n.sum()) - np.repeat(np.cumsum(n) - n, n)
    return sp[np.repeat(lo, n) + off], idx


def windowed_lags(a, b, centers, half, maxlag):
    """Lags b - a between spikes of a and b falling in the same +-half window around each centre."""
    ta, ia = window_spikes(a, centers, half)
    tb, ib = window_spikes(b, centers, half)
    out = []
    # process windows; spikes sorted by window then time
    sa = np.searchsorted(ia, np.arange(len(centers) + 1))
    sb = np.searchsorted(ib, np.arange(len(centers) + 1))
    for w in np.flatnonzero((np.diff(sa) > 0) & (np.diff(sb) > 0)):
        x = ta[sa[w]:sa[w + 1]]
        y = tb[sb[w]:sb[w + 1]]
        d = (y[None, :] - x[:, None]).ravel()
        out.append(d[np.abs(d) <= maxlag])
    return np.concatenate(out) if out else np.zeros(0)


def swr_participation(cells, swr):
    """Spike counts of each cell in each SWR ([start, end]); cells x SWRs."""
    st, en = swr["start"], swr["end"]
    M = np.zeros((len(cells), len(st)), int)
    for i, c in enumerate(cells):
        sp = c["spikes"]
        M[i] = np.searchsorted(sp, en, side="right") - np.searchsorted(sp, st, side="left")
    return M


def coactivity_z(pa, pb):
    """Cheng and Frank (2008) coactivity z for two binary participation vectors.

    The paper permutes each cell's participation across SWRs 5000 times; the
    count of joint participations under that permutation is hypergeometric, so
    its exact mean and SD are used (the limit of the Monte Carlo estimate; a
    standard choice that cannot change a result beyond permutation noise).
    """
    N = len(pa)
    a, b = pa.sum(), pb.sum()
    obs = (pa & pb).sum()
    if N < 2 or a == 0 or b == 0 or a == N or b == N:
        return np.nan
    mu = a * b / N
    var = a * b * (N - a) * (N - b) / (N ** 2 * (N - 1))
    return (obs - mu) / np.sqrt(var) if var > 0 else np.nan


def ccg_peak(a, b, maxlag, binw=0.010, sigma_s=0.150):
    """Lag of the peak of the smoothed cross-correlogram (b relative to a)."""
    d = lags(a, b, maxlag)
    edges = np.arange(-maxlag, maxlag + binw / 2, binw)
    h, _ = np.histogram(d, edges)
    if h.sum() == 0:
        return np.nan, 0
    hs = gaussian_filter1d(h.astype(float), sigma_s / binw)
    cen = 0.5 * (edges[1:] + edges[:-1])
    return cen[np.argmax(hs)], h.sum()


def occupancy_map(pos_list, spikes, binsize=2.0, sigma=2.0, extent=(0, 320, 0, 260), min_occ=0.0):
    """Occupancy-normalized rate map, 2 cm bins, Gaussian sigma 2 cm (Methods, Occupancy normalized firing maps).

    The rate in visited bins is smoothed with normalized convolution, so unvisited
    bins do not pull the rate down (a standard choice). ``min_occ`` (s) leaves out
    bins visited for less than that; the paper sets no minimum, so 0 is the main
    choice and a minimum is a variant.
    """
    xe = np.arange(extent[0], extent[1] + binsize, binsize)
    ye = np.arange(extent[2], extent[3] + binsize, binsize)
    occ = np.zeros((len(xe) - 1, len(ye) - 1))
    cnt = np.zeros_like(occ)
    for p in pos_list:
        if len(p["t"]) < 2:
            continue
        dt = p["dt"] if "dt" in p else np.gradient(p["t"])
        o, _, _ = np.histogram2d(p["x"], p["y"], [xe, ye], weights=dt)
        occ += o
        s = spikes[(spikes >= p["t"][0]) & (spikes <= p["t"][-1])]
        if "dt" in p:  # positions already restricted (e.g. to movement): spikes are taken as given
            s = spikes[np.isin(spikes, s)]
        if len(s):
            sx = np.interp(s, p["t"], p["x"])
            sy = np.interp(s, p["t"], p["y"])
            c, _, _ = np.histogram2d(sx, sy, [xe, ye])
            cnt += c
    from scipy.ndimage import gaussian_filter
    vis = occ > min_occ
    rate = np.where(vis, cnt / np.where(vis, occ, 1), 0.0)
    num = gaussian_filter(rate, sigma / binsize, truncate=3.0)
    den = gaussian_filter(vis.astype(float), sigma / binsize, truncate=3.0)
    m = np.where(vis, num / np.maximum(den, 1e-12), np.nan)
    return m, xe, ye
