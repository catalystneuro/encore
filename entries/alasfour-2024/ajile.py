"""Loading and measures for AJILE12 (DANDI:000055) as used by Alasfour and Gilja (2024).

Where each parameter comes from:

- ``VERSION``: the only published version of the dandiset (the paper cites none).
- ``PARTICIPANTS``: Table 1 of the paper (participants 1, 2, 4, 5, 8); the dandiset's
  ``sub-01`` and so on are AJILE12's participant numbers (Peterson et al., 2022).
- ``BANDS``: the claims file, M2 (Methods 2.1; beta is 8 to 32 Hz as printed).
- Butterworth order 4, zero phase: the claims file, O3, a standard choice. Zero-phase
  filtering (filtfilt) has the frequency response ``|H(f)|**2``; it is applied here in the
  frequency domain together with the Hilbert transform, which gives the same envelope as
  ``sosfiltfilt`` followed by ``scipy.signal.hilbert`` up to edge effects. 5 s of signal on
  each side of a block is filtered with it and then dropped (``PAD_S``), a standard choice.
- ``BIN_S``: 10-s bins, the claims file, M2.
- Artifact rule constants (``ART_SD``, ``ART_FRAC``, ``ART_DUR_S``): the claims file, M3 and
  O4 (Methods 2.1). The SD of a channel is the ``standard_deviation`` column of the day's
  electrodes table (reading O4 (ii)) or the pooled SD over the participant's days (O4 (i)).
- Labels: the epochs table's ``labels``; only blocks labelled with exactly one of ``Talk``,
  ``TV`` or ``Computer/phone`` are classes (an assumption: a block with two labels cannot be
  given to one class; the paper does not say).
- ROI projection matrices: Figshare item 10.6084/m9.figshare.12114408.v1 (Peterson et al.,
  2021a), as the claims file's header names it.
"""

import io
import struct
import threading
import time
import zlib
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
import requests
import scipy.fft as sfft
from requests.adapters import HTTPAdapter
from scipy import signal, stats

DANDISET = "000055"
VERSION = "0.220127.0436"
API = "https://api.dandiarchive.org/api"
PARTICIPANTS = ["01", "02", "04", "05", "08"]
FS = 500.0
BANDS = {
    "theta": (4.0, 8.0),
    "alpha": (8.0, 12.0),
    "beta": (8.0, 32.0),
    "low_gamma": (32.0, 55.0),
    "high_gamma": (70.0, 110.0),
}
BAND_NAMES = list(BANDS)
FILTER_ORDER = 4
PAD_S = 5.0
BIN_S = 10.0
ART_SD = 3.0
ART_FRAC = 0.10
ART_DUR_S = 2.0
CLASS_LABELS = {"Talk": "Talk", "TV": "TV", "Computer/phone": "Electronics"}

FIGSHARE_ARTICLE = 12114408
FIGSHARE_DOI = "10.6084/m9.figshare.12114408.v1"
ROIS = [
    "Precentral",
    "Frontal_Mid",
    "Postcentral",
    "Parietal_Inf",
    "SupraMarginal",
    "Temporal_Sup",
    "Temporal_Mid",
    "Temporal_Inf",
]
ROI_NAMES = {
    "Precentral": "precentral",
    "Frontal_Mid": "middle frontal",
    "Postcentral": "postcentral",
    "Parietal_Inf": "inferior parietal",
    "SupraMarginal": "supramarginal",
    "Temporal_Sup": "superior temporal",
    "Temporal_Mid": "middle temporal",
    "Temporal_Inf": "inferior temporal",
}

_session = requests.Session()
_session.mount("https://", HTTPAdapter(pool_maxsize=64, max_retries=3))


# ----------------------------------------------------------------------------- archive


def list_assets():
    """Assets of the pinned version: DataFrame with path, asset_id, size, subject, session."""
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=200"
    rows = []
    while url:
        d = _session.get(url, timeout=60).json()
        rows += d["results"]
        url = d["next"]
    df = pd.DataFrame([dict(path=a["path"], asset_id=a["asset_id"], size=a["size"]) for a in rows])
    df["subject"] = df.path.str.extract(r"sub-(\d+)")[0]
    df["session"] = df.path.str.extract(r"ses-(\d+)")[0].astype(int)
    return df.sort_values(["subject", "session"]).reset_index(drop=True)


def s3_url(asset_id):
    r = _session.head(f"{API}/assets/{asset_id}/download/", allow_redirects=True, timeout=60)
    return r.url


def open_nwb(asset_id):
    """Open an asset by streaming (remfile and h5py). Returns (h5py.File, url)."""
    url = s3_url(asset_id)
    return h5py.File(remfile.File(url), "r"), url


def _get_range(url, off, n):
    for attempt in range(6):
        try:
            r = _session.get(url, headers={"Range": f"bytes={off}-{off + n - 1}"}, timeout=120)
            if r.status_code in (200, 206) and len(r.content) == n:
                return r.content
        except requests.RequestException:
            pass
        time.sleep(1 + 2 * attempt)
    raise IOError(f"range read failed at {off}")


class _LoggingFile(io.RawIOBase):
    """A file-like view of a URL that records the offsets h5py reads (to find the B-tree root)."""

    def __init__(self, url):
        self.url, self.pos, self.log = url, 0, []
        r = _session.get(url, headers={"Range": "bytes=0-0"}, timeout=60)
        self.size = int(r.headers["Content-Range"].split("/")[1])

    def seek(self, o, wh=0):
        self.pos = o if wh == 0 else (self.pos + o if wh == 1 else self.size + o)
        return self.pos

    def tell(self):
        return self.pos

    def readable(self):
        return True

    def seekable(self):
        return True

    def readinto(self, buf):
        n = min(len(buf), self.size - self.pos)
        if n <= 0:
            return 0
        b = _get_range(self.url, self.pos, n)
        self.log.append((self.pos, b[:4]))
        buf[:n] = b
        self.pos += n
        return n


def chunk_index(url, path="acquisition/ElectricalSeries/data", threads=48):
    """Byte offset and size of every chunk of a 2-D chunked dataset.

    h5py's own chunk queries walk the version-1 B-tree node by node over the network
    (about 200 s per file here); this reads the same B-tree level by level in parallel.
    Returns (shape, chunks, {chunk_offset_tuple: (byte_offset, nbytes)}).
    """
    lf = _LoggingFile(url)
    f = h5py.File(lf, "r")
    d = f[path]
    shape, chunks = d.shape, d.chunks
    plist = d.id.get_create_plist()
    filters = [plist.get_filter(i)[0] for i in range(plist.get_nfilters())]
    assert filters == [h5py.h5z.FILTER_DEFLATE], filters
    n0 = len(lf.log)
    probe = d.id.get_chunk_info_by_coord((0, 0))
    roots = [o for o, b in lf.log[n0:] if b == b"TREE"]
    if not roots:  # root already cached by h5py on open: take the first TREE read overall
        roots = [o for o, b in lf.log if b == b"TREE"]
    f.close()
    rank = len(shape)
    ks = 8 + 8 * (rank + 1)

    def node(addr):
        h = _get_range(url, addr, 24)
        assert h[:4] == b"TREE"
        lvl, used = h[5], struct.unpack("<H", h[6:8])[0]
        b = _get_range(url, addr + 24, used * (ks + 8) + ks)
        out = []
        for i in range(used):
            p = i * (ks + 8)
            sz, mask = struct.unpack("<II", b[p : p + 8])
            offs = struct.unpack("<%dQ" % (rank + 1), b[p + 8 : p + ks])[:rank]
            child = struct.unpack("<Q", b[p + ks : p + ks + 8])[0]
            out.append((lvl, sz, mask, offs, child))
        return out

    info, level = {}, [roots[0]]
    with ThreadPoolExecutor(threads) as ex:
        while level:
            nxt = []
            for ents in ex.map(node, level):
                for lvl, sz, mask, offs, child in ents:
                    if lvl == 0:
                        assert mask == 0
                        info[offs] = (child, sz)
                    else:
                        nxt.append(child)
            level = nxt
    assert info[(0, 0)] == (probe.byte_offset, probe.size)
    n_expected = int(np.ceil(shape[0] / chunks[0]) * np.ceil(shape[1] / chunks[1]))
    assert len(info) == n_expected, (len(info), n_expected)
    return shape, chunks, info


def read_meta(asset_id):
    """Epochs, electrodes table and series attributes of one file (no signal data)."""
    f, url = open_nwb(asset_id)
    e = f["general/extracellular_ephys/electrodes"]
    el = pd.DataFrame(
        {
            k: (e[k][:].astype(str) if e[k].dtype.kind in "OS" else e[k][:])
            for k in e.keys()
            if k != "group"
        }
    )
    ep = f["intervals/epochs"]
    epochs = pd.DataFrame(
        dict(
            label=ep["labels"][:].astype(str),
            start=ep["start_time"][:],
            stop=ep["stop_time"][:],
        )
    )
    es = f["acquisition/ElectricalSeries"]
    meta = dict(
        session_start=f["session_start_time"][()].decode(),
        subject_id=f["general/subject/subject_id"][()].decode(),
        rate=float(es["starting_time"].attrs["rate"]),
        starting_time=float(es["starting_time"][()]),
        conversion=float(es["data"].attrs["conversion"]),
        unit=str(es["data"].attrs["unit"]),
        shape=es["data"].shape,
        chunks=es["data"].chunks,
        electrodes_index=es["electrodes"][:],
    )
    f.close()
    return meta, el, epochs, url


# ----------------------------------------------------------------------------- features


_resp_cache = {}


def _band_responses(nfft):
    """For each band, the rfft bins where the zero-phase response |H|^2 exceeds 1e-6."""
    if nfft in _resp_cache:
        return _resp_cache[nfft]
    freqs = np.fft.rfftfreq(nfft, 1 / FS)
    out = []
    for lo, hi in BANDS.values():
        sos = signal.butter(FILTER_ORDER, [lo, hi], btype="bandpass", fs=FS, output="sos")
        _, h = signal.sosfreqz(sos, worN=freqs, fs=FS)
        h2 = np.abs(h) ** 2
        k = np.where(h2 > 1e-6)[0]
        k0, k1 = k[0], k[-1] + 1
        m = sfft.next_fast_len(k1 - k0)
        w = h2[k0:k1] * 2.0  # analytic signal: positive frequencies doubled
        out.append((k0, k1, m, w))
    _resp_cache[nfft] = out
    return out


def band_envelopes(x):
    """Hilbert envelopes of each band of x (samples by channels), at reduced rate.

    Returns a list (one per band) of (times_in_samples, envelope array (m, channels)).
    The analytic signal of a band is band-limited, so its magnitude is computed from the
    band's own bins shifted to zero frequency, sampled at m points over the segment.
    """
    n = x.shape[0]
    X = sfft.rfft(x, axis=0, workers=4)
    out = []
    for k0, k1, m, w in _band_responses(n):
        Z = np.zeros((m, x.shape[1]), dtype=np.complex128)
        Z[: k1 - k0] = X[k0:k1] * w[:, None]
        z = sfft.ifft(Z, axis=0, workers=4)
        env = np.abs(z) * (m / n)  # ifft of length m divides by m; the analytic signal by n
        t = np.arange(m) * (n / m)
        out.append((t, env))
    return out


def envelope_check(x):
    """Envelope of one channel by sosfiltfilt and scipy.signal.hilbert, for comparison."""
    res = []
    for lo, hi in BANDS.values():
        sos = signal.butter(FILTER_ORDER, [lo, hi], btype="bandpass", fs=FS, output="sos")
        res.append(np.abs(signal.hilbert(signal.sosfiltfilt(sos, x))))
    return res


def _runs(mask):
    """Total True count and longest True run, per column of a boolean array."""
    total = mask.sum(0)
    pad = np.zeros((1, mask.shape[1]), bool)
    m = np.vstack([pad, mask, pad]).astype(np.int8)
    d = np.diff(m, axis=0)
    longest = np.zeros(mask.shape[1], int)
    for c in np.where(total > 0)[0]:
        s = np.where(d[:, c] == 1)[0]
        e = np.where(d[:, c] == -1)[0]
        longest[c] = (e - s).max()
    return total, longest


def block_features(seg, i0, i1, sds):
    """Features and artifact statistics of one block.

    seg: samples by channels (microvolts), with padding; the block is seg[i0:i1].
    sds: list of per-channel SD arrays (one per artifact reading).
    Returns dict with feats (bins, channels, bands), exceed totals and longest runs.
    """
    seg = seg.astype(np.float64)
    seg = seg - np.median(seg, axis=0)
    envs = band_envelopes(seg)
    nb = int(np.floor((i1 - i0) / (BIN_S * FS)))
    feats = np.full((nb, seg.shape[1], len(BANDS)), np.nan, np.float32)
    for bi, (t, env) in enumerate(envs):
        rel = (t - i0) / (BIN_S * FS)
        idx = np.floor(rel).astype(int)
        for b in range(nb):
            sel = idx == b
            feats[b, :, bi] = env[sel].mean(0)
    blk = seg[i0:i1]
    blk_raw = blk + 0.0
    tot, lon = [], []
    for sd in sds:
        a, b = _runs(np.abs(blk_raw) > ART_SD * sd[None, :])
        tot.append(a)
        lon.append(b)
    return dict(
        feats=feats,
        exceed_total=np.array(tot),
        exceed_longest=np.array(lon),
        sumsq=(blk_raw.astype(np.float64) ** 2).sum(0),
        n=blk.shape[0],
    )


def extract_day(asset_id, channels, blocks, sds, threads=48, window=6, offset=0.0):
    """Stream the blocks of one file and compute their features.

    channels: electrode indices (columns of the ElectricalSeries) to read.
    blocks: DataFrame with start, stop (s) and label; one row per 2-min block.
    sds: list of per-channel SD arrays (microvolts, for ``channels``), one per artifact reading.
    Only the chunks covering the blocks (plus ``PAD_S``) and the requested channels are read.
    """
    url = s3_url(asset_id)
    shape, chunks, info = chunk_index(url)
    ch_len = chunks[0]
    assert chunks[1] == 1
    pad = int(PAD_S * FS)
    spans = []
    for b in blocks.itertuples():
        i0 = int(round((b.start - offset) * FS))
        i1 = int(round((b.stop - offset) * FS))
        a0, a1 = max(0, i0 - pad), min(shape[0], i1 + pad)
        spans.append((a0, a1, i0, i1))
    ok = [i0 >= 0 and i1 <= shape[0] and i1 > i0 for _, _, i0, i1 in spans]
    rows_needed = sorted(
        {r for (a0, a1, _, _), g in zip(spans, ok) if g for r in range(a0 // ch_len, (a1 - 1) // ch_len + 1)}
    )
    last_use = {}
    for k, ((a0, a1, _, _), g) in enumerate(zip(spans, ok)):
        if not g:
            continue
        for r in range(a0 // ch_len, (a1 - 1) // ch_len + 1):
            last_use[r] = k

    def fetch_chunk(key):
        off, sz = info[key]
        raw = zlib.decompress(_get_range(url, off, sz))
        a = np.frombuffer(raw, dtype="<f4")
        return a

    ex = ThreadPoolExecutor(threads)

    def fetch_row(r):
        futs = [ex.submit(fetch_chunk, (r * ch_len, c)) for c in channels]
        arr = np.stack([f.result() for f in futs], axis=1)
        n_valid = min(ch_len, shape[0] - r * ch_len)
        return arr[:n_valid]

    row_ex = ThreadPoolExecutor(window)
    pending = {}
    nxt = 0

    def ensure(upto):
        nonlocal nxt
        while nxt < len(rows_needed) and len(pending) < window + 2:
            r = rows_needed[nxt]
            pending[r] = row_ex.submit(fetch_row, r)
            nxt += 1

    have = {}
    out = []
    nbytes = 0
    for k, (a0, a1, i0, i1) in enumerate(spans):
        if i0 < 0 or i1 > shape[0] or i1 <= i0:
            out.append(None)  # block outside the recorded samples: counted as dropped
            continue
        r0, r1 = a0 // ch_len, (a1 - 1) // ch_len
        for r in range(r0, r1 + 1):
            if r not in have:
                ensure(r)
                while r not in pending:
                    ensure(r)
                have[r] = pending.pop(r).result()
                nbytes += sum(info[(r * ch_len, c)][1] for c in channels)
                ensure(r)
        seg = np.concatenate([have[r] for r in range(r0, r1 + 1)], axis=0)
        seg = seg[a0 - r0 * ch_len : a1 - r0 * ch_len]
        res = block_features(seg, i0 - a0, i1 - a0, sds)
        out.append(res)
        for r in list(have):
            if last_use[r] <= k:
                del have[r]
    row_ex.shutdown()
    ex.shutdown()
    return out, nbytes


# ----------------------------------------------------------------------------- ROIs


def figshare_files():
    d = _session.get(f"https://api.figshare.com/v2/articles/{FIGSHARE_ARTICLE}", timeout=60).json()
    return {f["name"]: f for f in d["files"]}, d


def load_projection(participant, files=None):
    """Projection matrix of one participant: (density per ROI, weights electrodes by ROI).

    Columns are AAL regions of both hemispheres; the first numerical row is the electrode
    density of each region (the Figshare item's description).
    """
    files = files or figshare_files()[0]
    f = files[f"aal_{participant}_elecs2ROI.csv"]
    r = _session.get(f["download_url"], timeout=120)
    import hashlib

    assert hashlib.md5(r.content).hexdigest() == f["computed_md5"]
    d = pd.read_csv(io.BytesIO(r.content))
    return d.iloc[0], d.iloc[1:].reset_index(drop=True)


def load_centroids(files=None):
    files = files or figshare_files()[0]
    f = files["aal_01_ROIcentroids_Lside.csv"]
    r = _session.get(f["download_url"], timeout=120)
    return pd.read_csv(io.BytesIO(r.content))


# ----------------------------------------------------------------------------- statistics


def bh_fdr(p, alpha):
    """Benjamini-Hochberg as written in Methods 2.2: reject all p <= P_k."""
    p = np.asarray(p, float)
    ok = np.isfinite(p)
    rej = np.zeros(p.shape, bool)
    ps = np.sort(p[ok])
    n = len(ps)
    below = np.where(ps <= (np.arange(1, n + 1) / n) * alpha)[0]
    if len(below):
        pk = ps[below.max()]
        rej[ok] = p[ok] <= pk
    return rej


def finite_chance(n, c, alpha):
    """Combrisson and Jerbi (2015): binomial inverse at 1 - alpha for n samples, c classes."""
    return stats.binom.ppf(1 - alpha, n, 1.0 / c) / n


# ----------------------------------------------------------------------------- whole dataset


def class_blocks(epochs):
    """Blocks labelled with exactly one class label (Talk, TV, Computer/phone)."""
    b = epochs[epochs.label.isin(list(CLASS_LABELS))].copy()
    b["cls"] = b.label.map(CLASS_LABELS)
    return b.reset_index(drop=True)


def survey(assets, procs=8):
    """Metadata of every file: (dict of (subject, session) -> (meta, electrodes, epochs))."""
    from multiprocessing import Pool

    with Pool(procs) as p:
        res = p.map(read_meta, list(assets.asset_id))
    return {
        (s, ses): (m, el, ep)
        for (s, ses), (m, el, ep, _) in zip(zip(assets.subject, assets.session), res)
    }


def epoch_offset(meta):
    """Seconds from the epochs' clock to the ElectricalSeries' clock.

    In most files both start at 19:00 and the offset is 0. In two files (sub-01 ses-7,
    sub-04 ses-3) the session, and the ECoG, start later in the night while the epochs
    still start at 19:00, with a data break up to the start of the ECoG; the offset is the
    session start minus 19:00. This is found from the data (see the notebook's data check).
    """
    t = pd.Timestamp(meta["session_start"])
    ref = t.normalize() + pd.Timedelta(hours=19)
    if ref > t:
        ref -= pd.Timedelta(days=1)
    return (t - ref).total_seconds()


def _extract_job(job):
    asset_id, channels, blocks, sds, offset = job
    t = time.time()
    out, nbytes = extract_day(asset_id, channels, blocks, sds, offset=offset)
    return out, nbytes, time.time() - t


def extract_participant_days(jobs, procs=3):
    """Run extract_day over (asset_id, channels, blocks, sds) jobs in parallel processes."""
    from multiprocessing import get_context

    with get_context("spawn").Pool(procs) as p:
        res = dict(p.imap_unordered(_extract_indexed, list(enumerate(jobs))))
    return [res[i] for i in range(len(jobs))]


def _extract_indexed(ij):
    i, job = ij
    return i, _extract_job(job)


# ----------------------------------------------------------------------------- samples


def artifact_drop(block, good, reading):
    """True when a block is dropped by the artifact rule (Methods 2.1; claims O4).

    reading: (rule, sd) with rule "a" (more than 2 s in total) or "b" (more than 2 s
    contiguous), sd 0 for the day's SD (O4 (ii)) and 1 for the participant's pooled SD (O4 (i)).
    good: boolean mask over the block's channels (the day's good electrodes).
    """
    rule, sd = reading
    stat = block["exceed_total"][sd] if rule == "a" else block["exceed_longest"][sd]
    bad = (stat > ART_DUR_S * FS) & good
    return bad.sum() >= ART_FRAC * good.sum()


def build_samples(days, artifact=("a", 0)):
    """10-s samples of one participant, in time order.

    days: list of (session, session_start_seconds, good_mask_over_channels, blocks_df, results).
    Returns dict: X (samples, channels, bands), cls, day, block id, time, and per-block table.
    """
    Xs, cls, day, blk, tt = [], [], [], [], []
    rows = []
    bid = 0
    for ses, t0, good, blocks, res in days:
        for b, r in zip(blocks.itertuples(), res):
            row = dict(session=ses, start=b.start, stop=b.stop, cls=b.cls, bid=bid)
            if r is None:
                row.update(status="outside recording")
            elif artifact is not None and artifact_drop(r, good, artifact):
                row.update(status="artifact", nbins=r["feats"].shape[0])
            else:
                nb = r["feats"].shape[0]
                row.update(status="kept", nbins=nb)
                Xs.append(r["feats"])
                cls += [b.cls] * nb
                day += [ses] * nb
                blk += [bid] * nb
                tt += list(t0 + b.start + BIN_S * np.arange(nb))
            rows.append(row)
            bid += 1
    X = np.concatenate(Xs, 0)
    order = np.argsort(np.array(tt), kind="stable")
    return dict(
        X=X[order],
        cls=np.array(cls)[order],
        day=np.array(day)[order],
        block=np.array(blk)[order],
        time=np.array(tt)[order],
        blocks=pd.DataFrame(rows),
    )


# ----------------------------------------------------------------------------- ROIs per reading


def roi_assignment(dens, W, xyz, centroids, reading):
    """ROI index (0 to 7, or -1 for none) of each electrode under a reading of O5.

    "a": largest stored projection weight among the eight ROIs (left-hemisphere columns).
    "b": nearest of the eight left-hemisphere ROI centroids, from the dataset's positions
         mirrored to the left hemisphere (x = -|x|).
    "c": the largest unnormalised weight (stored weight times the ROI's density, the
         Gaussian value of Methods 2.1) over all left AAL regions, kept only when that region
         is one of the eight: "thresholded only to include electrodes close to any of the
         eight defined ROIs, and the ROI label was assigned by choosing the ROI closest to
         each electrode" (Methods 2.1).
    """
    names = np.array(W.columns)
    eight = [r + "_L" for r in ROIS]
    n = len(xyz)
    if reading == "a":
        w = W[eight].values[:n]
        return w.argmax(1)
    if reading == "b":
        q = np.array(xyz, float).copy()
        q[:, 0] = -np.abs(q[:, 0])
        cl = np.array([np.where(names == e)[0][0] for e in eight])
        C = centroids.values[cl]
        d2 = ((q[:, None, :] - C[None]) ** 2).sum(-1)
        return d2.argmin(1)
    if reading == "c":
        L = np.array([c.endswith("_L") for c in names])
        g = W.values[:n][:, L] * dens.values[L].astype(float)[None, :]
        best = names[L][g.argmax(1)]
        return np.array([eight.index(b) if b in eight else -1 for b in best])
    raise ValueError(reading)


def roi_channels(assign, dens, channels, density_reading):
    """Channels (positions in ``channels``) of each ROI, dropping ROIs of density below 3.

    density_reading "i": fewer than 3 assigned electrodes; "ii": the matrix's density row
    below 3 (Methods 2.1, "electrode density of less than 3"; claims O5).
    """
    out = {}
    for k, r in enumerate(ROIS):
        idx = [j for j, c in enumerate(channels) if c < len(assign) and assign[c] == k]
        d = len(idx) if density_reading == "i" else float(dens[r + "_L"])
        if len(idx) == 0 or d < 3:
            continue
        out[r] = idx
    return out


# ----------------------------------------------------------------------------- classifier


def folds_and_buffers(n, buffer, k=7):
    """Contiguous folds of the time-ordered samples, with the training folds of each test fold.

    buffer "a": both neighbouring folds left out of training; "b": only the following one
    (the preceding one for the last fold) (claims O7).
    """
    edges = np.linspace(0, n, k + 1).round().astype(int)
    folds = [np.arange(edges[i], edges[i + 1]) for i in range(k)]
    out = []
    for i in range(k):
        if buffer == "a":
            excl = {i - 1, i, i + 1}
        else:
            excl = {i, i + 1} if i < k - 1 else {i, i - 1}
        train = [j for j in range(k) if j not in excl]
        out.append((train, i))
    return folds, out


def balance(idx, y, rng):
    """Random downsampling of every class to the smallest one (claims O8)."""
    classes = np.unique(y[idx])
    m = min((y[idx] == c).sum() for c in classes)
    keep = np.concatenate([rng.choice(idx[y[idx] == c], m, replace=False) for c in classes])
    return np.sort(keep)


def zscore(a):
    sd = a.std(0)
    sd[sd == 0] = 1
    return (a - a.mean(0)) / sd


def lda2(Xtr, ytr, Xte):
    """Two-class LDA with one covariance shared by the classes and equal priors.

    Returns predictions (bool, class 1) and the class means (mean0, mean1).
    Equivalent to scikit-learn's LinearDiscriminantAnalysis without shrinkage on balanced
    data (claims O8).
    """
    m0 = Xtr[~ytr].mean(0)
    m1 = Xtr[ytr].mean(0)
    R = np.concatenate([Xtr[~ytr] - m0, Xtr[ytr] - m1])
    S = R.T @ R / (len(Xtr) - 2)
    w = np.linalg.lstsq(S, m1 - m0, rcond=None)[0]
    b = -w @ (m0 + m1) / 2
    return Xte @ w + b > 0, m0, m1


def make_splits(y, classes, buffer, rng):
    """Indices of the balanced training and test sets of each of the 7 folds.

    The samples of the classes are pooled in time order (claims O7); y holds labels.
    """
    use = np.where(np.isin(y, classes))[0]
    folds, plan = folds_and_buffers(len(use), buffer)
    out = []
    for train, i in plan:
        tr = use[np.concatenate([folds[j] for j in train])]
        te = use[folds[i]]
        out.append((balance(tr, y, rng), balance(te, y, rng)))
    return out


def cv_two_class(F, y_is1, splits):
    """Fold accuracies and fitted mean differences (class 1 minus class 0, per feature)."""
    accs, diffs, ntest = [], [], []
    for tr, te in splits:
        Xtr, Xte = zscore(F[tr]), zscore(F[te])
        pred, m0, m1 = lda2(Xtr, y_is1[tr], Xte)
        accs.append((pred == y_is1[te]).mean())
        diffs.append(m1 - m0)
        ntest.append(len(te))
    return np.array(accs), diffs, np.array(ntest)


def run_two_class(S, rois, feature="a", buffer="a", seed=0, classes=("Talk", "TV")):
    """Talking against watching TV for every ROI and band of one participant.

    S: samples (build_samples) restricted to the analysed channels; rois: ROI -> positions.
    feature "a": the electrodes of an ROI are its features, and the mean difference of the ROI
    is the mean over its electrodes; "b": one feature, the mean envelope of the ROI's
    electrodes (claims O6). Returns one row per ROI, band and fold.
    """
    rng = np.random.default_rng(seed)
    y = S["cls"]
    splits = make_splits(y, list(classes), buffer, rng)
    is1 = y == classes[0]
    rows = []
    for roi, pos in rois.items():
        for bi, band in enumerate(BAND_NAMES):
            F = S["X"][:, pos, bi].astype(np.float64)
            if feature == "b":
                F = F.mean(1, keepdims=True)
            accs, diffs, ntest = cv_two_class(F, is1, splits)
            for k in range(len(accs)):
                rows.append(
                    dict(roi=roi, band=band, fold=k, acc=accs[k], meandiff=float(np.mean(diffs[k])), ntest=ntest[k])
                )
    return pd.DataFrame(rows)


def add_chance(df, c=2):
    """Finite chance level per fold for alpha 0.05 and 0.01 (claims O9 (i))."""
    for a in (0.05, 0.01):
        df[f"chance_fold_{a}"] = [finite_chance(int(n), c, a) for n in df.ntest]
    return df


def group_tests(df, alpha_chance=0.05, chance_n="fold", fdr=0.01):
    """Participant-wide accuracy and mean-difference tests per feature (claims M6, M8, O9).

    chance_n "fold": a chance level per fold and a t-test of accuracy minus chance; "total":
    one chance level per participant from all its test samples.
    """
    d = df.copy()
    if chance_n == "fold":
        d["chance"] = d[f"chance_fold_{alpha_chance}"]
    else:
        tot = d.groupby(["participant", "roi", "band"]).ntest.transform("sum")
        d["chance"] = [finite_chance(int(n), 2, alpha_chance) for n in tot]
    rows = []
    for (roi, band), g in d.groupby(["roi", "band"]):
        ex = g.acc - g.chance
        t, p = stats.ttest_1samp(ex, 0.0)
        t2, p2 = stats.ttest_1samp(g.meandiff, 0.0)
        ci = stats.t.interval(0.95, len(g) - 1, loc=g.meandiff.mean(), scale=stats.sem(g.meandiff))
        rows.append(
            dict(
                roi=roi, band=band, n=len(g), acc=g.acc.mean(), chance=g.chance.mean(), t_acc=t, p_acc=p,
                meandiff=g.meandiff.mean(), md_lo=ci[0], md_hi=ci[1], t_md=t2, p_md=p2,
            )
        )
    r = pd.DataFrame(rows)
    r["sig_acc"] = bh_fdr(r.p_acc, fdr) & (r.acc > r.chance)
    r["sig_md"] = bh_fdr(r.p_md, fdr)
    r["consistent"] = r.sig_acc & r.sig_md
    return r


def restrict(S, mask):
    """Keep the channels in mask and drop samples with a missing value in any of them."""
    X = S["X"][:, mask, :]
    ok = ~np.isnan(X).any(axis=(1, 2))
    out = {k: (v[ok] if isinstance(v, np.ndarray) and len(v) == len(ok) else v) for k, v in S.items()}
    out["X"] = X[ok]
    out["n_nan_dropped"] = int((~ok).sum())
    return out
