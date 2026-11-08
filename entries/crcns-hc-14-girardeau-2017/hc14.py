"""Loading and measures for CRCNS hc-14 (Girardeau, Inema & Buzsaki 2017, Nature Neuroscience,
doi:10.1038/nn.4637).

The data set (doi:10.6080/K0MS3QXD) is not versioned. Its files are tar.gz archives in the public
S3 bucket crcnsarchive, under hc-14/live/. They are streamed: each archive is read once, in order,
through a gzip decompressor, and only the members needed are kept in memory. Nothing is written to
disk. (docs/archives.md describes opening zip files in place; these are tar.gz files, which have no
index, so they can only be read as a stream.)

What is read:

- AllRats-Variables.tar.gz: summary tables the authors deposited without documentation
  (AllRats-FinalType, AllRats-StatesFR, SpikeParameters, PoissonRippleMod, AllRats-EVcontribs,
  sessionindexing). Their columns are identified in the notebook's data check, against the raw
  files where that is possible.
- RatNN-Info.tar.gz: the structure lists per session and shank (Structures/*.mat for Rat09 and
  Rat10, Structures.txt for Rat11) and Structures.batch for Rat08 (BLA shanks only).
- RatNN-date_clu.tar.gz, per session: the sorted .clu/.res files (20 kHz sample indices), the
  position file .whl (39.0625 Hz, two LEDs, -1 when lost), and the events cat.evt (subsession
  boundaries), puf.evt (air puffs), lrw/rrw.evt (rewards) and rip.evt (ripples); event times are
  in ms. The RawKK folders, .fet and .klg files are skipped.

Where parameters come from:

- Clusters 0 and 1 are noise and multi-unit (claims file, units-recorded, after StatesFiringRates.m).
- 0.43 cm per pixel, the 20-cm danger zone, speed smoothed over 5 samples, laps as crossings of a
  150-cm segment with net displacement over 10 cm: claims file, opening comment ("Danger zone
  speed", "Reactivation strength"), from BehavioralMeasures.m and ClassifyLaps.m.
- 50-ms bins and Pearson correlations: claims file, opening comment ("Explained variance").
- EV and REV formula: claims file, opening comment.
- The air puff location and direction of each session are taken from the head position at the
  air puff times in the run (puf.evt and .whl). This is a standard choice: only six sessions carry
  an `airpuffloc` file, and where they do, it is compared in the notebook.
- The hand-scored sleep states are not in the data set. `substitute_nrem` stands in for NREM: periods
  of at least NREM_MIN_S (30 s) inside the pre-sleep and post-sleep subsessions in which the head speed,
  smoothed over NREM_SMOOTH_S (1 s), stays below NREM_SPEED (4 cm/s). This is an assumption of this
  attempt, not the paper's method (the paper scored states by hand from spectrograms and an
  accelerometer, Online Methods, Preprocessing). It cannot separate REM from NREM. The notebook checks
  it against the authors' NREM firing rates (StatesFR) and NREM pair correlations (EVcontribs).
- The speed computation (difference of the LED midpoint, centred, then a 5-sample moving mean)
  stands in for FMAToolbox LinearVelocity with smoothing 5, which the claims file names; it is a
  standard choice that the paper does not describe further.
"""

from __future__ import annotations

import io
import re
import tarfile
from concurrent.futures import ProcessPoolExecutor

import numpy as np
import requests
import scipy.io as sio
from isal import igzip

BASE = "https://crcnsarchive.s3-us-west-2.amazonaws.com/hc-14/live/"
DATASET = "crcns:hc-14"
DATASET_DOI = "10.6080/K0MS3QXD"
VERSION = "unversioned"   # CRCNS data sets are not versioned; MD5 sums pin the files read

SPIKE_FS = 20000.0
WHL_FS = 1250.0 / 32      # 39.0625 Hz, from the session .xml
CM_PER_PX = 0.43
BIN = 0.05                # s
DZ_CM = 20.0
LAP_SEGMENT_CM = 150.0
LAP_MIN_CM = 10.0
SPEED_SMOOTH = 5
NREM_SPEED = 4.0          # cm/s; substitute NREM (assumption, see substitute_nrem)
NREM_SMOOTH_S = 1.0       # s
NREM_MIN_S = 30.0         # s


# ---------------------------------------------------------------- streaming

def stream_tar(path, want):
    """Yield (member name, bytes) for members of a .tar.gz on the bucket where want(name)."""
    with requests.get(BASE + path, stream=True, timeout=120) as r:
        r.raise_for_status()
        g = igzip.IGzipFile(fileobj=r.raw, mode="rb")
        with tarfile.open(fileobj=g, mode="r|") as tf:
            for m in tf:
                if m.isfile() and want(m.name):
                    yield m.name, tf.extractfile(m).read()


def md5sums():
    """The data set's checksums.md5, as {relative path: md5}."""
    txt = requests.get(BASE + "checksums.md5", timeout=60).text
    out = {}
    for line in txt.splitlines():
        parts = line.split()
        if len(parts) == 2:
            out[parts[1].lstrip("./")] = parts[0]
    return out


def file_list():
    """All keys and sizes under hc-14/ in the bucket."""
    keys, token = [], None
    while True:
        url = "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=hc-14/"
        if token:
            url += "&continuation-token=" + requests.utils.quote(token)
        t = requests.get(url, timeout=60).text
        keys += [(k, int(s)) for k, s in re.findall(r"<Key>(.*?)</Key>.*?<Size>(\d+)</Size>", t)]
        m = re.search(r"<NextContinuationToken>(.*?)</NextContinuationToken>", t)
        if not m:
            return keys
        token = m.group(1)


def _mat(data):
    return sio.loadmat(io.BytesIO(data), squeeze_me=True, struct_as_record=False)


# ---------------------------------------------------------------- summary tables

def load_summary():
    """The deposited summary tables and structure lists, as a dict."""
    out = {}
    for name, data in stream_tar("AllRats-Variables.tar.gz",
                                 lambda n: n.endswith(".mat") and "AllRippleCCGs" not in n):
        out[name.split("/")[-1][:-4]] = _mat(data)
    for name, data in stream_tar("Batch-Files.tar.gz", lambda n: n.endswith("Structures.batch")):
        out["Structures.batch"] = data.decode()
    for rat in (8, 9, 10, 11):
        for name, data in stream_tar(f"Rat{rat:02d}/Rat{rat:02d}-Info.tar.gz",
                                     lambda n: "/Structures" in n):
            key = f"Rat{rat:02d}/" + name.split("/")[-1]
            out[key] = _mat(data) if name.endswith(".mat") else data.decode()
    return out


def load_ripple_ccgs():
    """AllRats-AllRippleCCGs.mat: ripple-peak cross-correlograms and gains per cell, overall and for
    pre-NREM and post-NREM (undocumented; read in the notebook)."""
    for name, data in stream_tar("AllRats-Variables.tar.gz", lambda n: "AllRippleCCGs" in n):
        return _mat(data)


def structure_shanks(summary):
    """{(rat, session index, shank): label} from the deposited structure lists.

    Rat09 and Rat10: Structures/<label>.mat, rows (session index, shank). Rat11: Structures.txt,
    blocks headed by a label with rows (session index, shank). Rat08: only BLA shanks, from
    Batch-Files/Structures.batch (left shanks, right shanks per session, in session order).
    Hippocampal shanks are not in these lists (Rat10 has Hpc.mat); see hpc_shanks.
    """
    lab = {}
    for rat in (9, 10):
        for key, d in summary.items():
            if key.startswith(f"Rat{rat:02d}/") and key.endswith(".mat"):
                label = key.split("/")[-1][:-4]
                arr = np.atleast_2d(d[label])
                for s, sh in arr:
                    lab[(rat, int(s), int(sh))] = label
    txt = summary["Rat11/Structures.txt"]
    label = None
    for line in txt.splitlines():
        line = line.strip()
        if not line:
            continue
        if re.fullmatch(r"[A-Za-z][A-Za-z0-9]*", line):
            label = line
            continue
        m = re.fullmatch(r"(\d+)\s+(\d+)", line)
        if m and label and label != "Rat11-Structures":
            lab[(11, int(m.group(1)), int(m.group(2)))] = label
    sess = 0
    for line in summary["Structures.batch"].splitlines():
        m = re.match(r"\S*Rat08-\d+\s+\[([^\]]*)\]\s*\[([^\]]*)\]", line)
        if not m:
            continue
        sess += 1
        for grp in m.groups():
            for sh in _matlab_range(grp):
                lab[(8, sess, sh)] = "BLA"
    return lab


def _matlab_range(s):
    s = s.strip()
    if not s:
        return []
    out = []
    for part in s.replace(",", " ").split():
        if ":" in part:
            a, b = part.split(":")
            out += list(range(int(a), int(b) + 1))
        else:
            out.append(int(part))
    return out


def sessions(summary):
    """The 61 sessions of the paper, from sessionindexing.mat: (rat, index, folder name)."""
    si = summary["sessionindexing"]
    out = []
    for (rat, idx), path in zip(si["ratsessionindex"], si["xmlpath"]):
        out.append((int(rat), int(idx), path.rstrip("/").split("/")[-1]))
    return out


# ---------------------------------------------------------------- one session

def _parse_evt(txt):
    rows = []
    for line in txt.splitlines():
        parts = line.split(None, 1)
        if len(parts) == 2:
            rows.append((float(parts[0]) / 1000.0, parts[1].strip()))
    return rows


def subsessions(cat):
    """[(number, name, start, stop)] from the parsed cat.evt rows (times in s)."""
    starts, stops = {}, {}
    for t, label in cat:
        m = re.match(r"(beginning|end) of .*-(\d+)-(\w+)$", label)
        if m:
            key = (int(m.group(2)), m.group(3))
            (starts if m.group(1) == "beginning" else stops)[key] = t
    return [(k[0], k[1], starts[k], stops[k]) for k in sorted(starts) if k in stops]


def intervals(session, name):
    """All (start, stop) of the subsessions called `name` ("prerun", "run", "presleep", ...)."""
    return [(a, b) for _, n, a, b in session["subsessions"] if n == name]


def in_intervals(t, ivs):
    """Boolean mask of the times t that fall in any of the intervals [a, b)."""
    if not len(ivs):
        return np.zeros(len(t), bool)
    iv = np.array(sorted(ivs), float)
    i = np.searchsorted(iv[:, 0], t, side="right") - 1
    ok = i >= 0
    out = np.zeros(len(t), bool)
    out[ok] = t[ok] < np.maximum.accumulate(iv[:, 1])[i[ok]]
    return out


def substitute_nrem(whl, subs, speed=NREM_SPEED, smooth_s=NREM_SMOOTH_S, min_s=NREM_MIN_S):
    """Substitute NREM intervals {"pre": [(start, stop)], "post": [...]} in s (see the module docstring)."""
    pos = position_cm(whl)
    v = np.hypot(*np.gradient(pos, axis=0).T) * WHL_FS
    k = np.ones(int(round(smooth_s * WHL_FS)) | 1)
    k /= k.sum()
    good = ~np.isnan(v)
    cover = np.convolve(good.astype(float), k, mode="same")
    with np.errstate(invalid="ignore", divide="ignore"):
        vs = np.convolve(np.where(good, v, 0), k, mode="same") / cover
    still = (cover >= 0.5) & (vs < speed)
    edges = np.flatnonzero(np.diff(np.r_[0, still.astype(int), 0]))
    out = {"pre": [], "post": []}
    for a, b in zip(edges[::2], edges[1::2]):
        if b - a < min_s * WHL_FS:
            continue
        ta, tb = a / WHL_FS, b / WHL_FS
        for _, name, s0, s1 in subs:
            side = "pre" if name == "presleep" else "post" if name == "postsleep" else None
            lo, hi = max(ta, s0), min(tb, s1)
            if side and hi - lo >= min_s:
                out[side].append((lo, hi))
    for side in out:
        out[side].sort()
    return out


def load_session(folder, keep_units=None, epochs_keep=("prerun", "run", "postrun"), extra_shanks=(),
                 extra_epochs=()):
    """Stream one session's clu archive and reduce it.

    Returns a dict with: `subsessions` [(number, name, start, stop)] in s, from cat.evt; `puff` air puff times (s); `rewards`;
    `ripple_peaks` (s, empty if no rip.evt); `whl` (n, 4) LED positions in pixels at WHL_FS;
    `airpuffloc` text or None; `units` list of (shank, clu, n spikes over the session); `spikes`
    {(shank, clu): times in s} for every unit, restricted to the subsessions named in `epochs_keep` (all when None); for the units on the
    shanks in `extra_shanks`, the subsessions in `extra_epochs` and the substitute NREM intervals are kept too.
    `nrem` holds the substitute NREM intervals (substitute_nrem).
    """
    rat = folder[:5]
    path = f"{rat}/{folder}/{folder}_clu.tar.gz"
    files = {}

    def want(n):
        base = n.split("/")[-1]
        if "RawKK" in n or base.startswith(".") or n.count("/") > 2:
            return False
        return bool(re.search(r"\.(clu|res)\.\d+$", base)) or base.endswith(
            (".cat.evt", ".puf.evt", ".lrw.evt", ".rrw.evt", ".rip.evt")) or base == folder + ".whl" \
            or base == "airpuffloc"

    for name, data in stream_tar(path, want):
        files[name.split("/")[-1]] = data
    out = {"folder": folder}
    cat = _parse_evt(files[folder + ".cat.evt"].decode())
    out["subsessions"] = subsessions(cat)
    out["cat"] = cat
    out["puff"] = np.array([t for t, _ in _parse_evt(files.get(folder + ".puf.evt", b"").decode())])
    out["rewards"] = {side: np.array([t for t, _ in _parse_evt(files.get(f"{folder}.{side}.evt", b"").decode())])
                      for side in ("lrw", "rrw")}
    rip = _parse_evt(files.get(folder + ".rip.evt", b"").decode())
    out["ripple_peaks"] = np.array([t for t, lab in rip if "peak" in lab])
    whl = files[folder + ".whl"].decode().replace(",", " ")
    out["whl"] = np.loadtxt(io.StringIO(whl), ndmin=2).astype(np.float32)
    out["airpuffloc"] = files["airpuffloc"].decode() if "airpuffloc" in files else None
    keep = [(a, b) for _, name, a, b in out["subsessions"]
            if epochs_keep is None or name in epochs_keep]
    out["nrem"] = substitute_nrem(out["whl"], out["subsessions"])
    keep_x = keep + [(a, b) for _, name, a, b in out["subsessions"] if name in extra_epochs] \
        + out["nrem"]["pre"] + out["nrem"]["post"]
    extra_shanks = set(extra_shanks)
    units, spikes = [], {}
    shanks = sorted(int(k.split(".")[-1]) for k in files if re.search(r"\.clu\.\d+$", k))
    for sh in shanks:
        clu = np.loadtxt(io.BytesIO(files.pop(f"{folder}.clu.{sh}")), dtype=np.int32)
        res = np.loadtxt(io.BytesIO(files.pop(f"{folder}.res.{sh}")), dtype=np.int64)
        clu = clu[1:]
        t = res / SPIKE_FS
        sel = in_intervals(t, keep)
        sel_x = in_intervals(t, keep_x)
        for c in np.unique(clu):
            if c <= 1:
                continue
            m = clu == c
            units.append((sh, int(c), int(m.sum())))
            if sh in extra_shanks:
                spikes[(sh, int(c))] = t[m & sel_x]
            elif keep_units is None or (sh, int(c)) in keep_units:
                spikes[(sh, int(c))] = t[m & sel]
    out["units"] = units
    out["spikes"] = spikes
    return out


def load_sessions(folders, workers=3, extra_shanks=None, **kw):
    """load_session over several folders in parallel processes, in the order given.
    `extra_shanks` is {folder: set of shanks} for load_session's extra_shanks."""
    extra_shanks = extra_shanks or {}
    with ProcessPoolExecutor(workers) as ex:
        futs = [ex.submit(load_session, f, extra_shanks=extra_shanks.get(f, ()), **kw) for f in folders]
        return [f.result() for f in futs]


# ---------------------------------------------------------------- behaviour

def position_cm(whl):
    """LED midpoint in cm (NaN where both LEDs are lost), from the (n, 4) .whl array."""
    xy = whl.astype(float).copy()
    xy[xy < 0] = np.nan
    a, b = xy[:, :2], xy[:, 2:]
    mid = np.where(np.isnan(a), b, np.where(np.isnan(b), a, (a + b) / 2))
    return mid * CM_PER_PX


def track_axis(pos):
    """Unit vector of the track's long axis (first principal axis of the run positions)."""
    p = pos[~np.isnan(pos).any(1)]
    p = p - p.mean(0)
    _, _, vt = np.linalg.svd(p, full_matrices=False)
    return vt[0]


def linear_speed(x, fs=WHL_FS, smooth=SPEED_SMOOTH):
    """Signed speed along the track (cm/s): centred difference, then a `smooth`-sample mean."""
    v = np.gradient(x) * fs
    k = np.ones(smooth) / smooth
    good = ~np.isnan(v)
    num = np.convolve(np.where(good, v, 0), k, mode="same")
    den = np.convolve(good.astype(float), k, mode="same")
    with np.errstate(invalid="ignore", divide="ignore"):
        return np.where(den > 0, num / den, np.nan)


def laps(x, fs=WHL_FS):
    """Track crossings: (start index, stop index, direction +1/-1) where the rat moves from one
    end zone to the other. End zones are the outer parts of the track beyond the 150-cm central
    segment; a crossing goes from leaving one end zone to entering the other (ClassifyLaps.m as
    the claims file describes it)."""
    good = ~np.isnan(x)
    lo, hi = np.nanpercentile(x, 1), np.nanpercentile(x, 99)
    mid = (lo + hi) / 2
    a, b = mid - LAP_SEGMENT_CM / 2, mid + LAP_SEGMENT_CM / 2
    zone = np.full(len(x), 0)
    zone[good & (x < a)] = -1
    zone[good & (x > b)] = 1
    out, last_zone, last_exit = [], 0, None
    for i in range(1, len(x)):
        if zone[i - 1] != 0 and zone[i] == 0:
            last_zone, last_exit = zone[i - 1], i
        if zone[i] != 0 and zone[i - 1] == 0 and last_exit is not None:
            if zone[i] == -last_zone and abs(x[i] - x[last_exit]) > LAP_MIN_CM:
                out.append((last_exit, i, int(zone[i])))
            last_exit = None
    return out


# ---------------------------------------------------------------- correlations and EV

def bin_counts(spikes, start, stop, bin=BIN):
    """(n units, n bins) spike counts in `bin`-s bins over [start, stop)."""
    edges = np.arange(start, stop + bin / 2, bin)
    return np.array([np.histogram(s, edges)[0] for s in spikes], dtype=float)


def cross_corr(a, b):
    """Pearson correlations between every row of a and every row of b (NaN where a row is flat)."""
    a = a - a.mean(1, keepdims=True)
    b = b - b.mean(1, keepdims=True)
    na, nb = np.sqrt((a * a).sum(1)), np.sqrt((b * b).sum(1))
    with np.errstate(invalid="ignore", divide="ignore"):
        return (a @ b.T) / np.outer(na, nb)


def corr_p(r, n):
    """Two-sided p-value of a Pearson r over n samples (t distribution), as Matlab corr gives."""
    from scipy.stats import t as tdist
    r = np.clip(r, -0.999999999, 0.999999999)
    tt = r * np.sqrt((n - 2) / (1 - r ** 2))
    return 2 * tdist.sf(np.abs(tt), n - 2)


def ev_rev(pre, run, post):
    """Explained and reversed explained variance from pair correlation vectors (claims file,
    opening comment). Pairs undefined in any epoch are dropped. Returns (EV, REV, n pairs)."""
    pre, run, post = map(np.asarray, (pre, run, post))
    ok = ~(np.isnan(pre) | np.isnan(run) | np.isnan(post))
    if ok.sum() < 3:
        return np.nan, np.nan, int(ok.sum())
    pre, run, post = pre[ok], run[ok], post[ok]
    r_rp = np.corrcoef(run, pre)[0, 1]
    r_ro = np.corrcoef(run, post)[0, 1]
    r_po = np.corrcoef(pre, post)[0, 1]
    ev = ((r_ro - r_rp * r_po) / np.sqrt((1 - r_rp ** 2) * (1 - r_po ** 2))) ** 2
    rev = ((r_rp - r_ro * r_po) / np.sqrt((1 - r_ro ** 2) * (1 - r_po ** 2))) ** 2
    return ev, rev, int(ok.sum())


def _zbins(spikes, ivs, bin=BIN):
    """Counts in `bin`-s bins over each interval, concatenated, z-scored per cell (0 where flat),
    with the start time of each bin. One histogram per cell over all intervals; the bins that span the
    gaps between intervals are dropped."""
    edges, keep = [], []
    for a, b in sorted(ivs):
        e = np.arange(a, b + bin / 2, bin)
        if len(e) < 2:
            continue
        if edges and e[0] <= edges[-1][-1]:
            e = e[e > edges[-1][-1]]
            if len(e) < 2:
                continue
        if edges:
            keep.append(np.r_[False, np.ones(len(e) - 1, bool)])     # gap bin, then the interval's bins
        else:
            keep.append(np.ones(len(e) - 1, bool))
        edges.append(e)
    E = np.concatenate(edges)
    K = np.concatenate(keep)
    X = np.array([np.histogram(s, E)[0][K] for s in spikes], dtype=float)
    mu, sd = X.mean(1, keepdims=True), X.std(1, keepdims=True)
    with np.errstate(invalid="ignore", divide="ignore"):
        Z = np.where(sd > 0, (X - mu) / sd, 0.0)
    return Z, E[:-1][K]


def sleep_bins(spk_h, spk_b, sleep_ivs, bin=BIN):
    """Z-scored 50-ms bins of both cell groups over the sleep intervals, for reactivation_strength."""
    Sh, t0 = _zbins(spk_h, sleep_ivs, bin)
    Sb, _ = _zbins(spk_b, sleep_ivs, bin)
    return Sh, Sb, t0


def reactivation_strength(spk_h, spk_b, template_ivs, sleep, ripple_peaks, half=2.0, bin=BIN):
    """Peri-ripple reactivation strength (claims file, opening comment, "Reactivation strength").

    Template C = Zh Zb' / n over the 50-ms bins of `template_ivs` (cells z-scored over those bins);
    R(t) = zh(t) C zb(t)' over the sleep bins (`sleep` from sleep_bins: cells z-scored over all of them),
    R z-scored over the same bins; returns (lags in s, mean R around the ripple peaks that fall in the
    sleep intervals, number of ripples). Bins of a window outside the sleep intervals are left out.
    """
    Zh, _ = _zbins(spk_h, template_ivs, bin)
    Zb, _ = _zbins(spk_b, template_ivs, bin)
    C = Zh @ Zb.T / Zh.shape[1]
    Sh, Sb, t0 = sleep
    R = ((C.T @ Sh) * Sb).sum(0)
    R = (R - R.mean()) / R.std()
    k = int(round(half / bin))
    lags = np.arange(-k, k + 1) * bin
    # bins of each sleep interval are contiguous in R; locate each ripple's bin
    seg_start = np.r_[0, np.flatnonzero(np.diff(t0) > bin * 1.5) + 1]
    seg_end = np.r_[seg_start[1:], len(t0)]
    prof, n = np.zeros(2 * k + 1), np.zeros(2 * k + 1)
    used = 0
    for p in ripple_peaks:
        j = np.searchsorted(t0, p, side="right") - 1
        if j < 0 or p >= t0[j] + bin:
            continue
        s = np.searchsorted(seg_start, j, side="right") - 1
        lo, hi = seg_start[s], seg_end[s]
        idx = j + np.arange(-k, k + 1)
        ok = (idx >= lo) & (idx < hi)
        prof[ok] += R[idx[ok]]
        n[ok] += 1
        used += 1
    with np.errstate(invalid="ignore", divide="ignore"):
        return lags, prof / n, used
