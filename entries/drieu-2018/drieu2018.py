"""Loading and measures for Drieu, Todorova & Zugaro (2018) on CRCNS hc-18.

The data set is five tar.gz archives, one per rat, in the public S3 bucket
crcnsarchive (hc-18/live/data/). Each is streamed once: byte ranges are fetched
in parallel, decompressed with zlib and parsed as a tar stream in memory.
Nothing is written to disk. Each member is reduced as it arrives:

- .res.N / .clu.N: spike times (samples at the acquisition rate) and clusters;
  clusters 0 and 1 (artefacts and noise in the Klusters convention) dropped.
- .spk.N: only the first SPK_BYTES of each file (the first 96,000 to 190,000 spikes) of each group are kept, averaged over
  channels, to give each unit's mean waveform from its first 800 spikes
  (DiscriminateUnits.m in the data set's code.zip, nSpikesSample = 800).
- .fet.N: features, kept until the L-ratio of each cluster is computed
  (Methods, Data acquisition; ClusterIsolation.m).
- .lfp: only the first channel of each spike group is kept (int16, 1250 Hz).
- .pos, .cat.evt, .xml: kept whole.

Where a parameter comes from is said where it is defined: the claims file's
criterion (which cites the paper), the paper's code in code.zip (cited by file),
an assumption (said so), or a standard choice for a detail that cannot change a
result (said so).
"""
import io
import re
import time
import zlib
import zipfile
from concurrent.futures import ThreadPoolExecutor

import numpy as np
import requests
from scipy import signal, stats

DATASET = "crcns:hc-18/unversioned"   # CRCNS data sets are not versioned (docs/archives.md)
BUCKET = "https://crcnsarchive.s3-us-west-2.amazonaws.com/hc-18/live/"
RATS = ["Train-242-20140124", "Train-261-20140617", "Train-272-20141215",
        "Train-292-20150501", "Train-314-20160118"]
LFP_FS = 1250.0
POS_FS = 39.0625
CONDS = ["P1", "A", "P2"]          # Passive 1, Active, Passive 2
SLEEPS = ["SB", "S1", "SA", "S2"]  # baseline, after P1, after Active, after P2
SPK_BYTES = 80 * 2**20             # bytes of each .spk kept for mean waveforms (memory bound)


# ----------------------------------------------------------------------------
# Streaming
# ----------------------------------------------------------------------------
def _chunks(url, size, chunk=32 * 2**20, workers=6):
    s = requests.Session()

    def get(a):
        b = min(a + chunk, size) - 1
        for k in range(6):
            try:
                r = s.get(url, headers={"Range": f"bytes={a}-{b}"}, timeout=180)
                r.raise_for_status()
                if len(r.content) == b - a + 1:
                    return r.content
            except Exception:
                pass
            time.sleep(2 + 3 * k)
        raise RuntimeError(f"range fetch failed at {a}")

    offs = list(range(0, size, chunk))
    with ThreadPoolExecutor(workers) as ex:
        futs = {}
        nxt = 0
        for i in range(min(2 * workers, len(offs))):
            futs[i] = ex.submit(get, offs[i])
            nxt = i + 1
        for i in range(len(offs)):
            data = futs.pop(i).result()
            if nxt < len(offs):
                futs[nxt] = ex.submit(get, offs[nxt])
                nxt += 1
            yield data


def _decompressed(url):
    size = int(requests.head(url).headers["Content-Length"])
    d = zlib.decompressobj(16 + zlib.MAX_WBITS)
    for c in _chunks(url, size):
        while c:
            out = d.decompress(c, 64 * 2**20)
            if out:
                yield out
            c = d.unconsumed_tail


class _Buf:
    def __init__(self, gen):
        self.g, self.b = gen, bytearray()

    def read(self, n):
        while len(self.b) < n:
            try:
                self.b += next(self.g)
            except StopIteration:
                break
        out = bytes(self.b[:n])
        del self.b[:n]
        return out

    def blocks(self, n, blk=64 * 2**20):
        while n > 0:
            if not self.b:
                self.b += next(self.g)
            k = min(n, len(self.b), blk)
            out = bytes(self.b[:k])
            del self.b[:k]
            n -= k
            yield out


def tar_members(url):
    """Yield (name, size, blocks) for each regular member of a streamed tar.gz.
    blocks is a generator of byte blocks; it is drained if the caller skips it."""
    b = _Buf(_decompressed(url))
    longname = None
    while True:
        h = b.read(512)
        if len(h) < 512 or h == b"\0" * 512:
            return
        name = h[0:100].rstrip(b"\0").decode()
        size = int(h[124:136].rstrip(b"\0 ") or b"0", 8)
        typ = h[156:157]
        pre = h[345:500].rstrip(b"\0").decode()
        if pre:
            name = pre + "/" + name
        pad = (-size) % 512
        if typ == b"L":
            longname = b.read(size + pad)[:size].rstrip(b"\0").decode()
            continue
        if longname:
            name, longname = longname, None
        gen = b.blocks(size)
        yield name.split("/")[-1], size, gen
        for _ in gen:
            pass
        b.read(pad)


def read_code_zip():
    """The paper's MATLAB scripts, deposited with the data set (code.zip), read in memory."""
    r = requests.get(BUCKET + "code.zip", timeout=120)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    return {n.split("/")[-1]: z.read(n).decode("latin-1") for n in z.namelist() if n.endswith(".m")}


def checksums():
    txt = requests.get(BUCKET + "checksums.md5", timeout=60).text
    return {l.split()[1]: l.split()[0] for l in txt.strip().splitlines()}


# ----------------------------------------------------------------------------
# Parsing
# ----------------------------------------------------------------------------
def parse_xml(x):
    nch = int(re.search(r"<nChannels>(\d+)", x).group(1))
    fs = float(re.search(r"<samplingRate>([\d.]+)", x).group(1))
    sd = x.split("<spikeDetection>")[1].split("</spikeDetection>")[0]
    groups = []
    for g in sd.split("<group>")[1:]:
        chans = list(map(int, re.findall(r"<channel>(\d+)</channel>", g)))
        ns = int(re.search(r"<nSamples>(\d+)", g).group(1))
        groups.append(dict(channels=chans, nSamples=ns))
    vw = int(re.search(r"<width>(\d+)", x).group(1))
    return dict(nChannels=nch, fs=fs, groups=groups, video_width=vw)


def parse_evt(txt):
    """Events file: time in ms, 'beginning of X' / 'end of X'. Returns [(name, start_s, stop_s)]."""
    out, open_ = [], {}
    for line in txt.strip().splitlines():
        t, rest = line.split(None, 1)
        kind, name = rest.split(" of ", 1)
        if kind == "beginning":
            open_[name] = float(t) / 1000
        else:
            out.append((name, open_.pop(name), float(t) / 1000))
    return out


def consolidate(iv, eps=0.0):
    """Merge intervals that overlap or touch within eps (FMAToolbox ConsolidateIntervals)."""
    iv = sorted(map(list, iv))
    out = []
    for a, b in iv:
        if out and a <= out[-1][1] + eps:
            out[-1][1] = max(out[-1][1], b)
        else:
            out.append([a, b])
    return np.array(out)


def epochs_from_events(ev, name, eps=0.0):
    """Travel and sleep intervals as GetEventsManip1.m (code.zip) builds them: the
    PassiveForward events consolidated, the first block Passive 1 and the second
    Passive 2; PseudoActiveForward consolidated as Active (for Train-292 the last
    PseudoActiveForward event is dropped, as the script does); Sleep events
    consolidated, in order baseline, after P1, after Active, after P2.
    eps: gap merged when consolidating; the script uses 0 (see the notebook)."""
    pf = [(a, b) for n, a, b in ev if n.endswith("-PassiveForward")]
    paf = [(a, b) for n, a, b in ev if n.endswith("-PseudoActiveForward")]
    if name == "Train-292-20150501":
        paf = paf[:-1]
    sl = [(a, b) for n, a, b in ev if re.search(r"-Sleep", n)]
    PF = consolidate(pf, eps)
    PAF = consolidate(paf, eps)
    SL = consolidate(sl, eps)
    return dict(PF_blocks=PF, PAF_blocks=PAF, SL_blocks=SL,
                travel={"P1": PF[0], "A": PAF[0], "P2": PF[1]},
                sleep=dict(zip(SLEEPS, SL[:4])))


def _ints(blob, dtype=np.int64):
    return np.array(blob.split(), dtype=dtype)


def lratio(fet, clu, c):
    """L-ratio of cluster c (Methods, Data acquisition; ClusterIsolation.m):
    sum over spikes outside c of 1 - chi2 CDF of their squared Mahalanobis distance
    to c, df = number of features, divided by the number of spikes on the group.
    Clusters with fewer spikes than features or more than half the group's spikes
    get NaN (ClusterIsolation.m skips them), so they are not well isolated."""
    inc = clu == c
    n_in, n = inc.sum(), len(clu)
    F = fet.shape[1]
    if n_in < F or n_in > n / 2:
        return np.nan
    X = fet[inc].astype(np.float64)
    mu = X.mean(0)
    cov = np.cov(X, rowvar=False)
    w, V = np.linalg.eigh(cov)
    keep = w > w.max() * 1e-10
    W = (V[:, keep] / np.sqrt(w[keep])).astype(np.float32)   # whitening (pseudo-inverse)
    out = fet[~inc]
    m = np.empty(len(out))
    mu32 = mu.astype(np.float32)
    for a in range(0, len(out), 500_000):
        z = (out[a:a + 500_000] - mu32) @ W
        m[a:a + 500_000] = np.einsum("ij,ij->i", z, z)
    return float(np.sum(stats.chi2.sf(m, F)) / n)


def waveform_metrics(w, fs):
    """Width and trough-to-second-peak of a mean waveform, after 10x
    interpolation, as DiscriminateUnits.m (code.zip). In seconds."""
    up = 10
    d = signal.resample_poly(w, up, 1)
    it = int(np.argmin(d))
    i2 = it + int(np.argmax(d[it:]))
    i1 = int(np.argmax(d[:it + 1]))
    return (i2 - i1) / (fs * up), (i2 - it) / (fs * up)


# ----------------------------------------------------------------------------
# One rat
# ----------------------------------------------------------------------------
def load_rat(name, log=print):
    """Stream one rat's archive and return its reduced data (see module docstring)."""
    url = BUCKET + "data/" + name + ".tar.gz"
    t0 = time.time()
    meta = None
    res, clu, wav, fet, nspk_total = {}, {}, {}, {}, {}
    lfp = None
    lfp_pending = False
    small = {}
    spk_raw = {}
    sizes = {}

    def handle_lfp(blocks, size):
        nch = meta["nChannels"]
        chans = [g["channels"][0] for g in meta["groups"]]
        n = size // (2 * nch)
        out = np.empty((len(chans), n), dtype=np.int16)
        rem = b""
        pos = 0
        for blk in blocks:
            blk = rem + blk
            k = (len(blk) // (2 * nch)) * 2 * nch
            a = np.frombuffer(blk[:k], dtype=np.int16).reshape(-1, nch)
            out[:, pos:pos + len(a)] = a[:, chans].T
            pos += len(a)
            rem = blk[k:]
        return dict(channels=chans, data=out[:, :pos])

    for mname, size, blocks in tar_members(url):
        sizes[mname] = size
        ext = mname[len(name) + 1:]
        if ext == "xml":
            meta = parse_xml(b"".join(blocks).decode("latin-1"))
        elif ext in ("pos", "cat.evt"):
            small[ext] = b"".join(blocks)
        elif ext == "lfp":
            if meta is None:
                lfp_pending = True
            else:
                lfp = handle_lfp(blocks, size)
        elif ext.startswith("res.") or ext.startswith("clu."):
            kind, g = ext.split(".")
            arr = _ints(b"".join(blocks))
            (res if kind == "res" else clu)[int(g)] = arr if kind == "res" else arr[1:]
        elif ext.startswith("fet."):
            g = int(ext.split(".")[1])
            blob = b"".join(blocks)
            first, rest = blob.split(b"\n", 1)
            nf = int(first)
            a = np.fromstring(rest, dtype=np.int64, sep=" ").reshape(-1, nf)
            fet[g] = a[:, :-1].astype(np.float32)   # last column is the spike time
            del blob, rest, a
        elif ext.startswith("spk."):
            # the raw bytes of the first SPK_BYTES of each group are kept and reduced
            # once the xml (channels per group) has been read
            g = int(ext.split(".")[1])
            got = bytearray()
            for blk in blocks:
                if len(got) < SPK_BYTES:
                    got += blk[: SPK_BYTES - len(got)]
            spk_raw[g] = (bytes(got), size)
    for g, (raw, size) in spk_raw.items():
        gi = meta["groups"][g - 1]   # spike groups in file names are numbered from 1, xml order
        ns, nc = gi["nSamples"], len(gi["channels"])
        per = ns * nc * 2
        a = np.frombuffer(raw[: (len(raw) // per) * per], dtype=np.int16)
        wav[g] = a.reshape(-1, ns, nc).astype(np.float32).mean(2)
        nspk_total[g] = size // per
    del spk_raw
    if lfp_pending:
        for mname, size, blocks in tar_members(url):
            if mname.endswith(".lfp"):
                lfp = handle_lfp(blocks, size)
                break
    log(f"{name}: streamed in {time.time() - t0:.0f} s")
    fs = meta["fs"]

    # units
    units = []
    for g in sorted(clu):
        c, r = clu[g], res[g]
        assert len(c) == len(r), (g, len(c), len(r))
        nkeep = len(wav[g])
        for k in np.unique(c):
            if k <= 1:
                continue
            sel = c == k
            idx = np.flatnonzero(sel[:nkeep])[:800]
            w = wav[g][idx].mean(0) if len(idx) else np.full(wav[g].shape[1], np.nan)
            width, half = waveform_metrics(w, fs) if len(idx) else (np.nan, np.nan)
            units.append(dict(group=g, cluster=int(k), times=r[sel] / fs, n_wave=len(idx),
                              width=width, halfwidth=half, lratio=lratio(fet[g], c, k),
                              wave=w))
    del fet, wav

    ev = parse_evt(small["cat.evt"].decode())
    pos = np.loadtxt(io.BytesIO(small["pos"]))
    return dict(name=name, meta=meta, units=units, events=ev, pos=pos, lfp=lfp,
                sizes=sizes, nspk_spk=nspk_total, res_max_s=max(r.max() for r in res.values()) / fs)


# ----------------------------------------------------------------------------
# Positions, linearization, velocity
# ----------------------------------------------------------------------------
NBINS = 250          # 2.4 cm bins on the 6 m track (Methods, Firing fields; BatchPlaceFields.m nBins = 250)
MINV = 5.0           # cm/s (Methods, Firing fields)


def pixel_size(name):
    """cm per pixel: 250/640 for rats 292 and 314, 250/768 otherwise (every Batch*.m in code.zip)."""
    return 250 / 640 if name[6:9] in ("291", "292", "313", "314") else 250 / 768


def positions(r):
    """Head position in cm at 39.0625 Hz; samples at -1 (LED lost) are NaN."""
    p = r["pos"].astype(float)
    p[(p[:, 0] < 0) | (p[:, 1] < 0)] = np.nan
    t = np.arange(len(p)) / POS_FS
    return t, p * pixel_size(r["name"])


def in_intervals(t, iv):
    iv = np.atleast_2d(iv)
    m = np.zeros(len(t), bool)
    for a, b in iv:
        m |= (t >= a) & (t <= b)
    return m


def runs(mask):
    """Start and stop indices (stop exclusive) of the True runs of a boolean array."""
    d = np.diff(np.r_[0, mask.astype(np.int8), 0])
    return np.flatnonzero(d == 1), np.flatnonzero(d == -1)


def linearize(t, xy, travel_iv):
    """Linear position on the closed obround track, in [0, 1). The paper's
    LinearizeTrainTrack is not in code.zip; here (an assumption, a standard
    method for a closed track) the position is mapped to its angle around the
    track centre, and the angle to arc length along the median path of the
    travel samples in 360 angular bins. The direction is set so that the train,
    which always moved forward (Methods, Animal training), moves to increasing
    values. Returns lin, perimeter in cm, and whether the sign was flipped."""
    m = in_intervals(t, travel_iv) & np.isfinite(xy[:, 0])
    c = np.array([np.percentile(xy[m, 0], [1, 99]).mean(), np.percentile(xy[m, 1], [1, 99]).mean()])
    ang = np.arctan2(xy[:, 1] - c[1], xy[:, 0] - c[0])
    edges = np.linspace(-np.pi, np.pi, 361)
    b = np.clip(np.digitize(ang[m], edges) - 1, 0, 359)
    path = np.array([np.median(xy[m][b == k], 0) if np.any(b == k) else [np.nan, np.nan] for k in range(360)])
    ok = np.isfinite(path[:, 0])
    ctr = (edges[:-1] + edges[1:]) / 2
    for j in range(2):
        path[:, j] = np.interp(ctr, ctr[ok], path[ok, j], period=2 * np.pi)
    seg = np.linalg.norm(np.diff(np.vstack([path, path[:1]]), axis=0), axis=1)
    s = np.r_[0, np.cumsum(seg)]
    L = s[-1]
    knots = np.r_[ctr, ctr[0] + 2 * np.pi]
    lin = np.interp(np.mod(ang - ctr[0], 2 * np.pi) + ctr[0], knots, s) / L
    lin = np.mod(lin, 1)
    # direction: unwrapped displacement during travel must be positive
    d = np.diff(lin[m])
    d = (d + 0.5) % 1 - 0.5
    flipped = np.nansum(d) < 0
    if flipped:
        lin = np.mod(1 - lin, 1)
    return lin, L, flipped


def gsmooth(x, sd):
    """Gaussian smoothing with NaNs filled by linear interpolation first."""
    from scipy.ndimage import gaussian_filter1d
    x = np.asarray(x, float).copy()
    ok = np.isfinite(x)
    if not ok.all():
        x[~ok] = np.interp(np.flatnonzero(~ok), np.flatnonzero(ok), x[ok])
    return gaussian_filter1d(x, sd) if sd > 0 else x


def velocity(t, xy, sd=30):
    """Linear velocity, cm/s, from positions smoothed by a Gaussian of s.d. 30 samples
    (LinearVelocity(x,30) in the scripts of code.zip)."""
    x, y = gsmooth(xy[:, 0], sd), gsmooth(xy[:, 1], sd)
    v = np.hypot(np.gradient(x), np.gradient(y)) * POS_FS
    return v


def moving_periods(t, v, thr=MINV, min_dur=10.0, max_gap=1.0):
    """Intervals with v > 5 cm/s, gaps shorter than 1 s bridged, lasting at least
    10 s: Threshold(v,'>',minv,'min',10,'max',1) in the scripts of code.zip,
    with 'min' and 'max' read as seconds (assumption on FMAToolbox's units)."""
    a, b = runs(v > thr)
    iv = [[t[i], t[j - 1]] for i, j in zip(a, b)]
    iv = consolidate(iv, max_gap) if iv else np.zeros((0, 2))
    return np.array([x for x in iv if x[1] - x[0] >= min_dur]).reshape(-1, 2)


# ----------------------------------------------------------------------------
# Units
# ----------------------------------------------------------------------------
def classify_units(units, active_iv, seed=0, reading="methods"):
    """Putative pyramidal cells. 'methods': k-means (k = 2) on waveform width,
    trough-to-peak duration and firing rate (Methods, Data acquisition), the three
    features z-scored (a standard choice so that the rate in Hz does not outweigh
    durations in ms). 'code': k-means on width and trough-to-peak only, as
    DiscriminateUnits.m does (its rate exclusion never applies, see the notebook).
    The cluster with the wider waveforms is pyramidal (DiscriminateUnits.m).
    Rates over the Active travel (BatchDiscriminateUnits.m)."""
    from scipy.cluster.vq import kmeans2
    a, b = active_iv
    rate = np.array([np.sum((u["times"] >= a) & (u["times"] <= b)) / (b - a) for u in units])
    W = np.array([[u["width"], u["halfwidth"]] for u in units])
    X = np.c_[W, rate] if reading == "methods" else W
    ok = np.all(np.isfinite(X), 1)
    Z = (X[ok] - X[ok].mean(0)) / X[ok].std(0)
    best = None
    for k in range(20):   # several restarts; the best inertia is kept
        cen, lab = kmeans2(Z, 2, seed=seed + k, minit="++")
        inert = sum(((Z[lab == j] - cen[j]) ** 2).sum() for j in range(2))
        if best is None or inert < best[0]:
            best = (inert, lab)
    lab = best[1]
    wid = [np.mean(W[ok][lab == j]) for j in range(2)]
    pyr_lab = int(np.argmax(wid))
    pyr = np.zeros(len(units), bool)
    pyr[np.flatnonzero(ok)[lab == pyr_lab]] = True
    return pyr, rate


# ----------------------------------------------------------------------------
# Firing curves and fields
# ----------------------------------------------------------------------------
def circ_gauss_smooth(x, sd_bins):
    from scipy.ndimage import gaussian_filter1d
    return gaussian_filter1d(x, sd_bins, mode="wrap")


def firing_curve(spk_lin, occ_lin, sd_bins, nbins=NBINS):
    """Kernel firing curve on the circular linearized track (Methods, Firing fields):
    smoothed spike count over smoothed occupancy time."""
    occ = np.bincount(np.minimum((occ_lin * nbins).astype(int), nbins - 1), minlength=nbins) / POS_FS
    cnt = np.bincount(np.minimum((spk_lin * nbins).astype(int), nbins - 1), minlength=nbins).astype(float)
    so, sc = circ_gauss_smooth(occ, sd_bins), circ_gauss_smooth(cnt, sd_bins)
    with np.errstate(invalid="ignore", divide="ignore"):
        rate = np.where(so > 0, sc / so, 0.0)
    return rate, occ


def fields(rate, minpeak, thr=0.3, min_size=0, max_size=None):
    """Fields: contiguous (circular) runs of bins above 30% of the peak rate;
    the first holds the peak, which must reach minpeak (1 Hz Active, 0.7 Hz Passive);
    other runs count as fields when their own peak reaches minpeak (Methods, Firing
    fields). min_size and max_size in bins (readings; see the notebook).
    Returns a list of boolean masks, the peak field first."""
    n = len(rate)
    pk = int(np.argmax(rate))
    if rate[pk] < minpeak:
        return []
    above = rate > thr * rate[pk]
    if above.all():
        runs_ = [np.ones(n, bool)]
    else:
        sh = int(np.flatnonzero(~above)[0])
        ab = np.roll(above, -sh)
        a, b = runs(ab)
        runs_ = []
        for i, j in zip(a, b):
            m = np.zeros(n, bool)
            m[i:j] = True
            runs_.append(np.roll(m, sh))
    out = []
    for m in runs_:
        if rate[m].max() < minpeak:
            continue
        if m.sum() < min_size:
            continue
        if max_size is not None and m.sum() > max_size:
            continue
        out.append(m)
    out.sort(key=lambda m: -int(m[pk]))
    if not out or not out[0][pk]:
        return []          # the field holding the peak failed a size rule
    return out


FIELD_READINGS = {
    # name: (kernel s.d. in cm, min field size in bins, max size in bins, min spikes (Active, Passive))
    "a": (4.5, 0, None, (0, 0)),          # Methods only
    "b": (4.5, 10, None, (0, 0)),         # + FiringCurve's minSize 10 bins (claims file, reading b)
    "code": (12.0, 10, 187, (50, 30)),    # BatchPlaceFields.m: smooth 5 bins, minSize 10, maxSize 3/4, min spikes
}


def prepare(r, eps=0.0, class_reading="methods"):
    """Per-rat derived data: epochs, linear position and velocity, moving periods,
    unit classes, and per travel condition the firing curves and fields of every
    well-isolated pyramidal cell under each field reading."""
    name = r["name"]
    ep = epochs_from_events(r["events"], name, eps)
    t, xy = positions(r)
    trav = np.array([ep["travel"][c] for c in CONDS])
    lin, L, flipped = linearize(t, xy, trav)
    v = velocity(t, xy)
    mov = moving_periods(t, v)
    mv = in_intervals(t, mov) & np.isfinite(lin) & np.isfinite(xy[:, 0])
    units = r["units"]
    pyr, rate_active = classify_units(units, ep["travel"]["A"], reading=class_reading)
    iso = np.array([np.isfinite(u["lratio"]) and u["lratio"] < 0.05 for u in units])
    out = dict(name=name, ep=ep, t=t, xy=xy, lin=lin, L=L, flipped=flipped, v=v, mov=mov, mv=mv,
               pyr=pyr, iso=iso, rate_active=rate_active, cond={})
    # unwrapped linear position for spike interpolation
    lin_unw = np.copy(lin)
    ok = np.isfinite(lin_unw)
    lu = np.unwrap(lin_unw[ok] * 2 * np.pi) / (2 * np.pi)
    lin_unw[ok] = lu
    out["lin_unw"] = lin_unw
    for c in CONDS:
        a, b = ep["travel"][c]
        sel = mv & (t >= a) & (t <= b)
        occ_lin = lin[sel]
        cd = dict(interval=(a, b), occ_lin=occ_lin, n_occ=sel.sum(), cells={})
        minpeak = 1.0 if c == "A" else 0.7
        for i, u in enumerate(units):
            if not (pyr[i] and iso[i]):
                continue
            st = u["times"][(u["times"] >= a) & (u["times"] <= b)]
            k = np.clip(np.round(st * POS_FS).astype(int), 0, len(t) - 1)
            st = st[sel[k]]
            sl = np.mod(np.interp(st, t[ok], lu), 1)
            cell = dict(spk_t=st, spk_lin=sl, readings={})
            for rd, (sdcm, mins, maxs, minspk) in FIELD_READINGS.items():
                rate, _ = firing_curve(sl, occ_lin, sdcm / (L / NBINS))
                need = minspk[0] if c == "A" else minspk[1]
                f = fields(rate, minpeak, 0.3, mins, maxs) if len(st) >= need else []
                cell["readings"][rd] = dict(rate=rate, fields=f)
            cd["cells"][i] = cell
        out["cond"][c] = cd
    return out


def place_cells(P, c, rd="a"):
    return [i for i, cell in P["cond"][c]["cells"].items() if cell["readings"][rd]["fields"]]


# ----------------------------------------------------------------------------
# Remapping (Methods, Firing fields, paragraph 2; FMAToolbox TestRemapping, FieldShift)
# ----------------------------------------------------------------------------
def field_shift(c1, c2, size1, size2, circular=True):
    """Shift = lag of the peak of the cross-correlogram of two firing curves,
    divided by the mean field size (bins); circular or linear correlogram."""
    n = len(c1)
    a, b = c1 - c1.mean(), c2 - c2.mean()
    if circular:
        cc = np.real(np.fft.ifft(np.conj(np.fft.fft(a)) * np.fft.fft(b)))
        lags = np.r_[np.arange(0, n // 2 + 1), np.arange(-(n - n // 2 - 1), 0)]
    else:
        cc = np.correlate(b, a, mode="full")
        lags = np.arange(-(n - 1), n)
    lag = lags[int(np.argmax(cc))]
    return lag / ((size1 + size2) / 2)


def remapping_test(curves1, curves2, sizes1, sizes2, n_boot=2000, rng=None, circular=True):
    """Mean unsigned proportional shift against shuffled cell identities in the
    test condition; p = proportion of shuffled means at or below the observed one."""
    k = len(curves1)
    obs = np.mean([abs(field_shift(curves1[i], curves2[i], sizes1[i], sizes2[i], circular)) for i in range(k)])
    null = np.empty(n_boot)
    for j in range(n_boot):
        p = rng.permutation(k)
        null[j] = np.mean([abs(field_shift(curves1[i], curves2[p[i]], sizes1[i], sizes2[p[i]], circular)) for i in range(k)])
    return obs, null, (np.sum(null <= obs)) / n_boot


def rayleigh(theta):
    n = len(theta)
    R = np.abs(np.mean(np.exp(1j * theta)))
    Rn = n * R
    p = np.exp(np.sqrt(1 + 4 * n + 4 * (n ** 2 - Rn ** 2)) - (1 + 2 * n))
    return R, min(p, 1.0)


def vtest(theta, mu0=0.0):
    n = len(theta)
    V = np.sum(np.cos(theta - mu0))
    u = V * np.sqrt(2 / n)
    return u, stats.norm.sf(u)


# ----------------------------------------------------------------------------
# LFP: filters, spectra, theta cycles, phase
# ----------------------------------------------------------------------------
def bandpass(x, lo, hi, fs=LFP_FS, order=4):
    """Zero-phase band-pass; a Chebyshev type II filter as FMAToolbox FilterLFP
    (standard choice for a detail that cannot change a result)."""
    sos = signal.cheby2(order, 20, [lo, hi], btype="band", fs=fs, output="sos")
    return signal.sosfiltfilt(sos, x)


def mt_psd(segments, fs=LFP_FS, win=2.0, NW=3, K=5, fmax=30):
    """Multitaper spectrum (chronux default tapers [3 5], a standard choice) of
    detrended 2-s windows, averaged; returns f, mean spectrum, per-window spectra."""
    n = int(win * fs)
    tap = signal.windows.dpss(n, NW, K)
    f = np.fft.rfftfreq(n, 1 / fs)
    keep = f <= fmax
    S = []
    for x in segments:
        for a in range(0, len(x) - n + 1, n):
            w = signal.detrend(x[a:a + n].astype(float))
            S.append((np.abs(np.fft.rfft(tap * w, axis=1)) ** 2).mean(0)[keep])
    S = np.array(S)
    return f[keep], S.mean(0), S


def segments_of(lfp_row, iv, t0=0.0):
    out = []
    for a, b in np.atleast_2d(iv):
        i, j = int(round((a - t0) * LFP_FS)), int(round((b - t0) * LFP_FS))
        if j - i > LFP_FS:
            out.append(lfp_row[max(i, 0):j])
    return out


def theta_cycles(x, fs=LFP_FS):
    """Theta cycles (Methods, Theta power, frequency and cycles): from peak to peak
    of the 6-10 Hz filtered LFP; cycles shorter than 80 ms or longer than 200 ms
    dropped; only runs of at least three contiguous cycles kept. Returns cycle
    start and stop sample indices."""
    th = bandpass(x, 6, 10, fs)
    pk = signal.argrelmax(th)[0]
    pk = pk[th[pk] > 0]
    st, en = pk[:-1], pk[1:]
    d = (en - st) / fs
    good = (d > 0.08) & (d < 0.2)
    st, en = st[good], en[good]
    # runs of contiguous cycles
    cont = np.r_[False, st[1:] == en[:-1]]
    grp = np.cumsum(~cont)
    cnt = np.bincount(grp)
    keep = cnt[grp] >= 3
    return st[keep], en[keep], th


def extrema_1_40(x, fs=LFP_FS):
    """Peaks and troughs of the LFP filtered at 1-40 Hz (Methods, Theta asymmetry)."""
    y = bandpass(x, 1, 40, fs)
    return y, signal.argrelmax(y)[0], signal.argrelmin(y)[0]


def asymmetry(st, en, y, pk, tr):
    """log(dt2/dt1) per theta cycle: dt1 from cycle start to trough, dt2 from trough
    to cycle end, on the 1-40 Hz LFP (Methods). Cycle start and end are the 1-40 Hz
    peaks nearest the theta-band peaks; the trough is the 1-40 Hz minimum between."""
    out = np.full(len(st), np.nan)
    for k, (a, b) in enumerate(zip(st, en)):
        ia = pk[np.argmin(np.abs(pk - a))] if len(pk) else a
        ib = pk[np.argmin(np.abs(pk - b))] if len(pk) else b
        if ib - ia < 10:
            continue
        it = ia + int(np.argmin(y[ia:ib]))
        if it == ia or it == ib:
            continue
        out[k] = np.log((ib - it) / (it - ia))
    return out


def unwrapped_phase(x, reading, fs=LFP_FS):
    """Unwrapped theta phase (rad) per LFP sample. (a) linear interpolation between
    the 1-40 Hz peaks (0) and troughs (pi); (b) Hilbert phase of the 6-10 Hz signal,
    0 at peaks. Readings of the claims file (Common methods, Theta cycles)."""
    if reading == "b":
        th = bandpass(x, 6, 10, fs)
        return np.unwrap(np.angle(signal.hilbert(th)))
    y, pk, tr = extrema_1_40(x, fs)
    ev = np.r_[pk, tr]
    kind = np.r_[np.zeros(len(pk)), np.ones(len(tr))]
    o = np.argsort(ev)
    ev, kind = ev[o], kind[o]
    # keep alternating extrema (peak, trough, peak...): of repeated kinds, keep the extreme
    keep_ev, keep_k = [], []
    for e, k in zip(ev, kind):
        if keep_k and keep_k[-1] == k:
            if (k == 0 and y[e] > y[keep_ev[-1]]) or (k == 1 and y[e] < y[keep_ev[-1]]):
                keep_ev[-1] = e
            continue
        keep_ev.append(e)
        keep_k.append(k)
    keep_ev = np.array(keep_ev)
    ph = np.arange(len(keep_ev)) * np.pi + (np.pi if keep_k[0] == 1 else 0)
    return np.interp(np.arange(len(x)), keep_ev, ph)


def circ_lin_regression(x, phi, amin=-2 * np.pi, amax=2 * np.pi, n=2001):
    """Linear-circular regression (Kempter et al. 2012, ref. 43): slope a (rad per
    unit of x) maximizing the mean resultant length of phi - a x; the circular-linear
    correlation rho and its p-value (their eq. for large n)."""
    a_grid = np.linspace(amin, amax, n)
    R = np.abs(np.exp(1j * (phi[None, :] - a_grid[:, None] * x[None, :])).mean(1))
    a = a_grid[int(np.argmax(R))]
    phi0 = np.angle(np.mean(np.exp(1j * (phi - a * x))))
    theta = np.mod(np.abs(a) * x, 2 * np.pi)
    def cmean(z):
        return np.angle(np.mean(np.exp(1j * z)))
    pb, tb = cmean(phi), cmean(theta)
    num = np.sum(np.sin(phi - pb) * np.sin(theta - tb))
    den = np.sqrt(np.sum(np.sin(phi - pb) ** 2) * np.sum(np.sin(theta - tb) ** 2))
    rho = num / den if den > 0 else 0.0
    N = len(x)
    l20 = np.mean(np.sin(phi - pb) ** 2)
    l02 = np.mean(np.sin(theta - tb) ** 2)
    l22 = np.mean(np.sin(phi - pb) ** 2 * np.sin(theta - tb) ** 2)
    z = rho * np.sqrt(N * l20 * l02 / l22) if l22 > 0 else 0.0
    p = 2 * stats.norm.sf(abs(z))
    return a, phi0, rho, p


def spike_train_spectrum_peak(u, lo=0.75, hi=1.25, dt=1 / 50, NW=3, K=5):
    """Theta burst frequency (Methods, Theta burst frequency): spike times in
    units of theta cycles (unwrapped phase / 2 pi), binned at 1/50 cycle, and the
    multitaper spectrum (chronux default tapers, standard choice) of the
    mean-subtracted train; the mode within 0.75-1.25 cycle^-1 (fig. S4A legend)."""
    if len(u) < 20:
        return np.nan
    u = np.sort(u)
    nb = int(np.ceil((u[-1] - u[0]) / dt)) + 1
    if nb < 200:
        return np.nan
    x = np.bincount(((u - u[0]) / dt).astype(int), minlength=nb).astype(float)
    x -= x.mean()
    nfft = 1 << int(np.ceil(np.log2(nb)))
    tap = signal.windows.dpss(nb, NW, K)
    f = np.fft.rfftfreq(nfft, dt)
    S = (np.abs(np.fft.rfft(tap * x, n=nfft, axis=1)) ** 2).mean(0)
    m = (f >= lo) & (f <= hi)
    pk_i = np.flatnonzero(m)[np.argmax(S[m])]
    # a peak at the band edge is not a peak within the band
    if pk_i in (np.flatnonzero(m)[0], np.flatnonzero(m)[-1]):
        return np.nan
    return f[pk_i]


# ----------------------------------------------------------------------------
# Sleep: SWS, ripples, candidate events
# ----------------------------------------------------------------------------
def sws_periods(x, t0, fs=LFP_FS, win=5.0, k=5, seed=0):
    """SWS (Methods, Candidate replay events; SWSDetection.m in code.zip): k-means
    on the z-scored theta (6-10 Hz) / delta (1-4 Hz) power ratio of a spectrogram
    of the sleep session; the cluster with the lowest mean ratio is SWS; gaps
    < 1 s bridged ('brieflfp', 1); epochs > 120 s kept ('duration', 120). The
    number of clusters is SWSDetection.m's default, 5. Windows of 5 s: an
    assumption (FMAToolbox MTSpectrogram's default window as we read it).
    Returns intervals in seconds and the ratio per window."""
    from scipy.cluster.vq import kmeans2
    n = int(win * fs)
    m = len(x) // n
    seg = x[: m * n].reshape(m, n).astype(float)
    seg = seg - seg.mean(1, keepdims=True)
    f = np.fft.rfftfreq(n, 1 / fs)
    P = np.abs(np.fft.rfft(seg * np.hanning(n), axis=1)) ** 2
    th = P[:, (f >= 6) & (f <= 10)].sum(1)
    de = P[:, (f >= 1) & (f <= 4)].sum(1)
    # flat (zero) stretches and windows with saturated samples (|x| >= 32000, as
    # SWSDetection.m removes them) are left out
    sat = (np.abs(x[: m * n].reshape(m, n)) >= 32000).any(1)
    good = (th > 0) & (de > 0) & ~sat
    ratio = np.full(m, np.nan)
    ratio[good] = th[good] / de[good]
    z = (ratio[good] - ratio[good].mean()) / ratio[good].std()
    best = None
    for r in range(10):
        cen, lab = kmeans2(z[:, None], k, seed=seed + r, minit="++")
        inert = sum(((z[lab == j] - cen[j, 0]) ** 2).sum() for j in range(k))
        if best is None or inert < best[0]:
            best = (inert, cen, lab)
    _, cen, lab = best
    sws_lab = int(np.argmin(cen[:, 0]))
    # windows left out take the label of the preceding kept window, so that they
    # neither split nor extend an epoch (SWSDetection.m drops their samples and
    # joins the rest)
    gi = np.flatnonzero(good)
    fill = np.maximum.accumulate(np.where(good, np.arange(m), -1))
    lab_full = np.where(fill >= 0, np.r_[lab, 0][np.searchsorted(gi, np.maximum(fill, 0))], -1)
    mask = lab_full == sws_lab
    a, b = runs(mask)
    iv = [[t0 + i * win, t0 + j * win] for i, j in zip(a, b)]
    iv = consolidate(iv, 1.0) if iv else np.zeros((0, 2))
    return np.array([v for v in iv if v[1] - v[0] > 120]).reshape(-1, 2), ratio


def envelope(x, lo, hi, fs=LFP_FS):
    return np.abs(signal.hilbert(bandpass(x, lo, hi, fs))).astype(np.float32)


def detect_ripples(chans, t0, thr=1.0, peak_thr=3.0, min_d=0.02, max_d=0.11, fs=LFP_FS):
    """Ripples (Methods, Ripple detection; BatchFindRipples.m): 100-250 Hz envelopes
    of the pyramidal-layer channels averaged, minus the averaged 300-500 Hz
    envelope; negative values set to 0 and positive values z-scored; events above
    1 s.d. with a peak above 3 s.d.; events of 20 ms or less or 110 ms or more
    dropped. Returns [start, peak, stop] in s and the signal's peak values."""
    me = None
    no = None
    for x in chans:
        e = envelope(x, 100, 250, fs)
        q = envelope(x, 300, 500, fs)
        me = e if me is None else me + e
        no = q if no is None else no + q
    me /= len(chans)
    no /= len(chans)
    # saturated periods (any channel at |x| >= 32766, +/-50 ms) are excluded, as
    # BatchFindRipples.m does
    from scipy.ndimage import binary_dilation
    sat = np.zeros(len(me), bool)
    for x in chans:
        sat |= np.abs(x) >= 32766
    sat = binary_dilation(sat, iterations=int(0.05 * fs)) if sat.any() else sat
    s = me - no
    s[sat] = np.nan
    pos = s > 0
    z = np.zeros_like(s)
    z[pos] = (s[pos] - s[pos].mean()) / s[pos].std()
    a, b = runs(z > thr)
    out = []
    for i, j in zip(a, b):
        d = (j - i) / fs
        if d <= min_d or d >= max_d:
            continue
        k = i + int(np.argmax(z[i:j]))
        if z[k] > peak_thr:
            out.append([t0 + i / fs, t0 + k / fs, t0 + j / fs])
    return np.array(out).reshape(-1, 3)


def candidate_events(spike_times, sleep_iv, sws, norm="sws", sd_ms=10.0, max_dur=0.5):
    """Candidate events (Methods, Candidate replay events; BatchCandidateEvents.m):
    place-cell spike count in 1-ms bins, Gaussian s.d. 10 ms; within SWS, epochs
    above the mean that contain a peak above mean + 3 s.d.; events > 500 ms dropped.
    The mean and s.d. are over SWS bins (norm='sws', as the script does) or over
    the whole sleep session (norm='all')."""
    from scipy.ndimage import gaussian_filter1d
    a, b = sleep_iv
    nb = int(np.ceil((b - a) * 1000))
    st = spike_times[(spike_times >= a) & (spike_times < b)]
    h = np.bincount(((st - a) * 1000).astype(int), minlength=nb)[:nb].astype(np.float32)
    sh = gaussian_filter1d(h, sd_ms)
    tb = a + (np.arange(nb) + 0.5) / 1000
    insws = in_intervals(tb, sws) if len(sws) else np.zeros(nb, bool)
    ref = sh[insws] if norm == "sws" else sh
    if insws.sum() == 0:
        return np.zeros((0, 3))
    mu, sd = ref.mean(), ref.std()
    above = (sh > mu) & insws
    i0, i1 = runs(above)
    out = []
    for i, j in zip(i0, i1):
        if sh[i:j].max() > mu + 3 * sd:
            if (j - i) / 1000 <= max_dur:
                k = i + int(np.argmax(sh[i:j]))
                out.append([tb[i], tb[k], tb[j - 1]])
    return np.array(out).reshape(-1, 3)


# ----------------------------------------------------------------------------
# Bayesian decoding and trajectory scores
# ----------------------------------------------------------------------------
import numba

TRACK_M = 6.0                       # track length used for slopes (Methods: "the track length (6 m)")
D_CM = 45.0                         # d of the trajectory score (Methods, Assessing trajectories)


def train_decoder(P, c, cells, rd="a"):
    """Occupancy prior P(x) and firing curves lambda_i(x) (Hz) of the given
    place cells in travel condition c (Methods, Bayesian trajectory decoding)."""
    cd = P["cond"][c]
    occ = np.bincount(np.minimum((cd["occ_lin"] * NBINS).astype(int), NBINS - 1), minlength=NBINS).astype(float)
    px = circ_gauss_smooth(occ, FIELD_READINGS[rd][0] / (P["L"] / NBINS))
    px /= px.sum()
    lam = np.array([cd["cells"][i]["readings"][rd]["rate"] for i in cells])
    lam = np.maximum(lam, 1e-3)     # floor so that log(0) never occurs (standard choice)
    return px, lam


def decode(counts, tau, px, lam):
    """Posterior P(x|n) per window, Poisson likelihood; counts (cells x windows),
    tau (windows,) in s. Windows without spikes are NaN (the scripts set
    uniform windows to NaN). Returns (windows x bins)."""
    ll = counts.T @ np.log(lam) - tau[:, None] * lam.sum(0)[None, :] + np.log(px)[None, :]
    ll -= ll.max(1, keepdims=True)
    p = np.exp(ll)
    p /= p.sum(1, keepdims=True)
    p[counts.sum(0) == 0] = np.nan
    return p


@numba.njit(cache=True)
def _band_sums(Pm, d):
    m, N = Pm.shape
    B = np.zeros((m, N))
    for k in range(m):
        for c in range(N):
            s = 0.0
            for j in range(-d, d + 1):
                s += Pm[k, (c + j) % N]
            B[k, c] = s
    return B


@numba.njit(cache=True)
def _best_line(B, valid, shifts, Ds):
    """Max over lines (start b, total displacement D over the m windows) of the mean
    over valid windows of B[k, b + round(D k / (m-1))], wrapping around the track,
    for the unshuffled (row 0 of shifts, all zeros) and each shuffled event."""
    m, N = B.shape
    K = shifts.shape[0]
    best = np.full(K, -1.0)
    bestD = np.zeros(K, np.int64)
    nval = 0
    for k in range(m):
        if valid[k]:
            nval += 1
    acc = np.zeros(N)
    for s in range(K):
        for iD in range(len(Ds)):
            D = Ds[iD]
            for b in range(N):
                acc[b] = 0.0
            for k in range(m):
                if not valid[k]:
                    continue
                off = int(np.round(D * k / (m - 1))) - shifts[s, k]
                for b in range(N):
                    acc[b] += B[k, (b + off) % N]
            for b in range(N):
                v = acc[b] / nval
                if v > best[s]:
                    best[s] = v
                    bestD[s] = D
    return best, bestD


def trajectory_score(Pm, n_shuffles, rng, d_bins=None, D_step=1):
    """Trajectory score and slope (Methods, Assessing trajectories): the best line's
    mean probability within d = 45 cm, over all lines whose total distance is below
    the track length, wrapping around; and the same for shuffles circularly shifting
    each window by a random number of bins. Returns score, D (bins over the event),
    shuffled scores, shuffled D, Monte Carlo p (proportion of shuffled scores above
    the observed one)."""
    m, N = Pm.shape
    if d_bins is None:
        d_bins = int(round(D_CM / (TRACK_M * 100 / N)))
    valid = np.isfinite(Pm[:, 0])
    Pz = np.where(np.isfinite(Pm), Pm, 0.0)
    B = _band_sums(Pz, d_bins)
    Ds = np.arange(-(N - 1), N, D_step).astype(np.int64)
    shifts = np.zeros((n_shuffles + 1, m), np.int64)
    shifts[1:] = rng.integers(0, N, size=(n_shuffles, m))
    best, bestD = _best_line(B, valid, shifts, Ds)
    p = np.mean(best[1:] > best[0])
    return best[0], bestD[0], best[1:], bestD[1:], p


@numba.njit(parallel=True, cache=True)
def _best_line_many(Bs, valids, offsets, shifts_all, Ds, ms):
    """Batch version over events, events concatenated along the window axis.
    Bs is (windows x 2N): the band sums repeated twice, so that wrapping around the
    track needs no modulo in the inner loop."""
    nE = len(ms)
    K = shifts_all.shape[1]
    N = Bs.shape[1] // 2
    best = np.full((nE, K), -1.0)
    bestD = np.zeros((nE, K), np.int64)
    for e in numba.prange(nE):
        o = offsets[e]
        m = ms[e]
        nval = 0
        for k in range(m):
            if valids[o + k]:
                nval += 1
        acc = np.zeros(N)
        for s in range(K):
            for iD in range(len(Ds)):
                D = Ds[iD]
                acc[:] = 0.0
                for k in range(m):
                    if not valids[o + k]:
                        continue
                    off = (int(np.round(D * k / (m - 1))) - shifts_all[o + k, s]) % N
                    row = Bs[o + k, off:off + N]
                    for b in range(N):
                        acc[b] += row[b]
                mx = acc.max() / nval
                if mx > best[e, s]:
                    best[e, s] = mx
                    bestD[e, s] = D
    return best, bestD


def score_events(mats, n_shuffles, rng, D_step=1):
    """Trajectory scores of many events at once (see trajectory_score). mats: list
    of (windows x bins) posteriors. Returns dict of arrays."""
    if not mats:
        z = np.zeros(0)
        return dict(score=z, D=z, p=z, z=z, sh_score=np.zeros((0, n_shuffles)), sh_D=np.zeros((0, n_shuffles)))
    N = mats[0].shape[1]
    d_bins = int(round(D_CM / (TRACK_M * 100 / N)))
    ms = np.array([len(m) for m in mats], np.int64)
    offsets = np.r_[0, np.cumsum(ms)[:-1]].astype(np.int64)
    allP = np.vstack(mats)
    valids = np.isfinite(allP[:, 0])
    Bs = _band_sums(np.where(np.isfinite(allP), allP, 0.0), d_bins)
    Bs = np.ascontiguousarray(np.concatenate([Bs, Bs], 1))
    shifts_all = np.zeros((len(allP), n_shuffles + 1), np.int64)
    shifts_all[:, 1:] = rng.integers(0, N, size=(len(allP), n_shuffles))
    Ds = np.arange(-(N - 1), N, D_step).astype(np.int64)
    best, bestD = _best_line_many(Bs, valids, offsets, shifts_all, Ds, ms)
    sh = best[:, 1:]
    out = dict(score=best[:, 0], D=bestD[:, 0].astype(float), p=np.mean(sh > best[:, :1], 1),
               z=(best[:, 0] - sh.mean(1)) / sh.std(1), sh_score=sh.astype(np.float32),
               sh_D=bestD[:, 1:].astype(np.float32), m=ms)
    return out


# ----------------------------------------------------------------------------
# Per-rat LFP reduction
# ----------------------------------------------------------------------------
def reduce_lfp(r, P, ripple_peak_thr=3.0):
    """Choose the LFP channels and reduce the LFP to what the analyses need.
    The paper's channel lists (SessionsReactivations1-Channels.batch) are not in
    the data set. Pyramidal-layer channels: the first channel of each spike group
    with at least one well-isolated pyramidal cell. Theta channel, reading (a):
    the one of these with the largest 6-10 Hz power during moving travel; reading
    (b): their mean (claims file, Common methods, Theta cycles)."""
    lf = r["lfp"]
    data = lf["data"]
    groups_with_pyr = sorted({r["units"][i]["group"] for i in range(len(r["units"])) if P["pyr"][i] and P["iso"][i]})
    rows = [g - 1 for g in groups_with_pyr]
    trav_mov = []
    for c in CONDS:
        a, b = P["ep"]["travel"][c]
        for x0, x1 in P["mov"]:
            lo, hi = max(a, x0), min(b, x1)
            if hi - lo > 2:
                trav_mov.append((c, lo, hi))
    tpow = []
    for k in rows:
        segs = [data[k, int(lo * LFP_FS):int(hi * LFP_FS)] for _, lo, hi in trav_mov]
        f, S, _ = mt_psd(segs)
        tpow.append(S[(f >= 6) & (f <= 10)].max())
    best = rows[int(np.argmax(tpow))]
    out = dict(pyr_rows=rows, pyr_channels=[lf["channels"][k] for k in rows], theta_row=best,
               theta_channel=lf["channels"][best], theta_power_by_row=dict(zip(rows, tpow)), travel={})
    for c in CONDS:
        a, b = P["ep"]["travel"][c]
        i, j = int(a * LFP_FS), int(b * LFP_FS)
        out["travel"][c] = dict(t0=i / LFP_FS, a=data[best, i:j].astype(np.float32),
                                b=data[rows, i:j].astype(np.float32).mean(0))
    # sleep: SWS on the theta channel; ripples on the pyramidal-layer channels
    out["sleep"] = {}
    for s in SLEEPS:
        a, b = P["ep"]["sleep"][s]
        i, j = int(a * LFP_FS), int(b * LFP_FS)
        sws, ratio = sws_periods(data[best, i:j], i / LFP_FS)
        rip = detect_ripples([data[k, i:j] for k in rows], i / LFP_FS, peak_thr=ripple_peak_thr)
        out["sleep"][s] = dict(sws=sws, ratio=ratio, ripples=rip, interval=(a, b))
    return out


# ----------------------------------------------------------------------------
# Theta-cycle decoding
# ----------------------------------------------------------------------------
def theta_windows(P, LF, c, reading="b"):
    """Theta cycles of condition c during moving periods, each split in six phase
    windows of pi/3 by the unwrapped Hilbert phase of the 6-10 Hz LFP (FindSubcycles
    on the .tuw phase in BatchSequenceReconstructNewProto.m). Cycles from theta_cycles
    on the theta channel (reading a of the LFP channel). Returns window edges (s)
    as an array (cycles x 7)."""
    tr = LF["travel"][c]
    x = tr["a"]
    t0 = tr["t0"]
    st, en, th = theta_cycles(x)
    ph = np.maximum.accumulate(np.unwrap(np.angle(signal.hilbert(th))))
    tt = t0 + np.arange(len(x)) / LFP_FS
    mvm = in_intervals(tt, P["mov"])
    edges = []
    for a, b in zip(st, en):
        if not (mvm[a] and mvm[b - 1]):
            continue
        p0 = ph[a]
        targets = p0 + np.arange(7) * np.pi / 3
        idx = np.searchsorted(ph[a:b + 1], targets)
        if idx[-1] > b - a:
            idx[-1] = b - a
        if np.any(np.diff(idx) <= 0):
            continue
        edges.append(tt[a + idx])
    return np.array(edges).reshape(-1, 7)


def spike_matrix(spk_list, edges_flat):
    """Counts (cells x windows) of spikes in [edges[k], edges[k+1])."""
    out = np.zeros((len(spk_list), len(edges_flat) - 1))
    for i, st in enumerate(spk_list):
        out[i] = np.histogram(st, edges_flat)[0]
    return out


def decode_theta(P, LF, c, rd="a", cells=None, min_spikes=3, min_cells=3, min_win=3, spikes=None, train=None):
    """Decode every theta cycle of condition c with the decoder trained on c.
    Keeps cycles with >= 3 spikes and >= 3 cells (BatchSequenceReconstructNewProto.m:
    minSpikePerCycle, minUnitInEvent; Methods: at least three units) and >= 3
    windows with spikes (nMinWin). Returns posteriors (absolute), centred posteriors,
    current positions, cycle durations, edges."""
    if cells is None:
        cells = place_cells(P, c, rd)
    px, lam = train if train is not None else train_decoder(P, c, cells, rd)
    edges = theta_windows(P, LF, c)
    if spikes is None:
        spikes = [P["cond"][c]["cells"][i]["spk_t"] for i in cells]
    mats, cent, pos, dur, keep = [], [], [], [], []
    ok = np.isfinite(P["lin_unw"])
    tt, lu = P["t"][ok], P["lin_unw"][ok]
    for e in edges:
        cnt = spike_matrix(spikes, e)
        if cnt.sum() < min_spikes or (cnt.sum(1) > 0).sum() < min_cells or (cnt.sum(0) > 0).sum() < min_win:
            continue
        post = decode(cnt, np.diff(e), px, lam)
        mid = (e[:-1] + e[1:]) / 2
        cur = np.mod(np.interp(mid, tt, lu), 1)
        cb = np.floor(cur * NBINS).astype(int)
        cen = np.array([np.roll(post[k], NBINS // 2 - cb[k]) for k in range(6)])
        mats.append(post)
        cent.append(cen)
        pos.append(cb)
        dur.append(e[-1] - e[0])
        keep.append(e)
    return dict(mats=mats, cent=np.array(cent).reshape(-1, 6, NBINS), pos=np.array(pos).reshape(-1, 6),
                dur=np.array(dur), edges=np.array(keep).reshape(-1, 7), n_cells=len(cells), n_cycles_all=len(edges))


def quadrant_scores(cent):
    """Quadrant score (Methods, Assessing trajectories; BatchSequenceQuadrants.m):
    the centred posterior, +/-1.5 m around the current position (+/-62 bins of
    2.4 cm) and the four middle phase windows (+/-2/3 cycle around the trough),
    in four quadrants; (behind-early + ahead-late - ahead-early - behind-late) / sum."""
    h = NBINS // 2
    d = int(round(150 / (TRACK_M * 100 / NBINS)))
    z = np.nan_to_num(cent[:, 1:5, h - d:h + d])
    behind, ahead = z[:, :, :d], z[:, :, d:]
    early, late = slice(0, 2), slice(2, 4)
    be, ae = behind[:, early].sum((1, 2)), ahead[:, early].sum((1, 2))
    bl, al = behind[:, late].sum((1, 2)), ahead[:, late].sum((1, 2))
    tot = be + ae + bl + al
    with np.errstate(invalid="ignore"):
        return (be + al - ae - bl) / tot


# ----------------------------------------------------------------------------
# Replay decoding
# ----------------------------------------------------------------------------
def replay_matrices(events, spikes, px, lam, win=0.02, min_dur=0.06, min_cells=3, min_win=3):
    """Candidate events split in 20-ms windows and decoded (Methods, Bayesian
    trajectory decoding; BatchReplayReconstructNewProto.m: window 0.020, events
    shorter than 3 windows dropped, >= 3 units, >= 3 windows with spikes)."""
    mats, keep = [], []
    for k, (a, pk, b) in enumerate(events):
        if b - a < min_dur:
            continue
        nw = int(np.floor((b - a) / win))
        e = a + np.arange(nw + 1) * win
        cnt = spike_matrix(spikes, e)
        if (cnt.sum(1) > 0).sum() < min_cells or (cnt.sum(0) > 0).sum() < min_win:
            continue
        mats.append(decode(cnt, np.full(nw, win), px, lam))
        keep.append(k)
    return mats, np.array(keep, int)
