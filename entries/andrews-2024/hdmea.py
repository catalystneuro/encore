"""Streaming access to DANDI:001132 (Andrews, Geng, Voitiuk et al. 2024, HD-MEA recordings of human
hippocampal slices) and the reductions the notebook uses.

Every file of the dandiset holds one MaxWell recording as an NWB ElectricalSeries of raw voltage
(uint16 counts, 20 kHz, 745 to 1017 channels), stored in gzip chunks of 78125 samples by 64
channels. There are no sorted units, no light or stimulus events and no condition labels. The
helper reads the chunks of one 64-channel group by HTTP range requests and decompresses them
here, which is about ten times faster than reading through h5py over remfile; the first chunk is
checked against h5py's own read.

Parameters and where they come from:
- DANDISET and VERSION: the most recent published version (the paper cites none; the two
  published versions hold the same assets).
- BIN: 10 ms bins of the channel-mean voltage, used to find light steps. A standard choice for
  a resolution that cannot change a result (the steps are single-bin jumps of hundreds of counts).
- Light steps: the LED gives a step of the voltage on every channel at light onset and the
  opposite step at offset (seen in the data, notebook section "Light events"). A step is a
  change between consecutive 10 ms bins of more than STEP_MIN counts. STEP_MIN is a standard
  choice set far above the bin-to-bin noise (shown in the notebook).
- Multi-unit threshold crossings: band-pass 300 to 6000 Hz (the band the paper's spike sorting
  used; Methods, Spike Sorting), negative crossings of 5 times the median absolute deviation
  (/0.6745) of each channel in each chunk. The threshold is a standard choice; the crossings are
  not the paper's sorted units and only serve as a variant that decides no outcome.
- Saturation: the fraction of channels whose value is 0 or 1023 (the ends of the range the
  values span), per 100 ms bin. In slice 3C the light drives most channels to these values.
"""

from __future__ import annotations

import hashlib
import threading
import zlib
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import remfile
import requests
from scipy import signal

DANDISET = "001132"
VERSION = "0.241130.1903"
API = "https://api.dandiarchive.org/api"
FS = 20000.0
BIN = 200            # samples per 10 ms bin
STEP_MIN = 60.0      # counts; a light step between consecutive 10 ms bins
RAIL = 1023          # the top of the 10-bit range the values span (0 to 1023, seen in the data)
SERIES = "acquisition/ElectricalSeries"
_SOS = signal.butter(3, [300, 6000], btype="bandpass", fs=FS, output="sos")


def assets(version: str = VERSION) -> list[dict]:
    """Every asset of the pinned version, sorted by path."""
    out, url = [], f"{API}/dandisets/{DANDISET}/versions/{version}/assets/?page_size=200"
    while url:
        r = requests.get(url, timeout=60)
        r.raise_for_status()
        js = r.json()
        out += js["results"]
        url = js["next"]
    return sorted(out, key=lambda a: a["path"])


def s3_url(asset_id: str) -> str:
    """The asset's public S3 address, from its metadata."""
    r = requests.get(f"{API}/assets/{asset_id}/", timeout=60)
    r.raise_for_status()
    return next(u for u in r.json()["contentUrl"] if "s3.amazonaws.com" in u)


def recording_name(path: str) -> str:
    """'sub-3C-7/sub-3C-7_ses-..._ecephys.nwb' -> '3C-7'."""
    return path.split("/")[0][4:]


def metadata(url: str) -> dict:
    """What a file holds, without reading its voltage."""
    with h5py.File(remfile.File(url), "r") as f:
        es = f[SERIES]
        d = es["data"]
        el = f["general/extracellular_ephys/electrodes"]
        groups = []
        f.visit(lambda n: groups.append(n) if not n.startswith("specifications") else None)
        subj = {k: f["general/subject"][k][()].decode() for k in f["general/subject"]}
        plist = d.id.get_create_plist()
        return dict(
            subject_id=subj["subject_id"], age=subj["age"], sex=subj["sex"], species=subj["species"],
            session_start=f["session_start_time"][()].decode(),
            session_description=f["session_description"][()].decode(),
            n_samples=d.shape[0], n_channels=d.shape[1], dtype=str(d.dtype), chunks=d.chunks,
            filters=[plist.get_filter(k)[3].decode() for k in range(plist.get_nfilters())],
            rate=float(es["starting_time"].attrs["rate"]), conversion=float(d.attrs["conversion"]),
            offset=float(d.attrs["offset"]), unit=d.attrs["unit"],
            x=el["rel_x"][:], y=el["rel_y"][:], electrode=el["electrode"][:],
            location=sorted(set(v.decode() for v in el["location"][:])),
            device=f["general/devices/DeviceEcephys"].attrs["description"],
            has_units="units" in f, n_acquisition=len(f["acquisition"]),
            processing=list(f["processing"]), intervals="intervals" in f,
            stimulus=list(f["stimulus/presentation"]),
            paths=[n for n in groups if not n.startswith(("general", SERIES))],
        )


class Group:
    """The chunks of one 64-channel group of a recording, read by byte range."""

    def __init__(self, url: str, group: int = 0):
        self.url = url
        with h5py.File(remfile.File(url), "r") as f:
            d = f[SERIES]["data"]
            self.n, self.n_channels = d.shape
            self.C, self.W = d.chunks
            plist = d.id.get_create_plist()
            assert [plist.get_filter(k)[3] for k in range(plist.get_nfilters())] == [b"deflate"]
            self.ch0 = group * self.W
            self.width = min(self.W, self.n_channels - self.ch0)
            self.info = [d.id.get_chunk_info_by_coord((i, self.ch0)) for i in range(0, self.n, self.C)]
            self.first = d[: self.C, self.ch0:self.ch0 + self.width]
        self._local = threading.local()

    def chunk(self, k: int) -> np.ndarray:
        """Chunk k as (samples, channels) uint16, trimmed to the recording's length and width."""
        if not hasattr(self._local, "s"):
            self._local.s = requests.Session()
        c = self.info[k]
        r = self._local.s.get(self.url, headers={"Range": f"bytes={c.byte_offset}-{c.byte_offset + c.size - 1}"},
                              timeout=120)
        r.raise_for_status()
        x = np.frombuffer(zlib.decompress(r.content), dtype="<u2").reshape(self.C, self.W)
        return x[: min(self.C, self.n - k * self.C), : self.width]

    def raw_digest(self, k: int) -> str:
        """SHA-1 of the compressed bytes of chunk k, to find recordings deposited twice."""
        c = self.info[k]
        r = requests.get(self.url, headers={"Range": f"bytes={c.byte_offset}-{c.byte_offset + c.size - 1}"},
                         timeout=120)
        r.raise_for_status()
        return hashlib.sha1(r.content).hexdigest()


def reduce_chunk(x: np.ndarray) -> tuple:
    """(channel-mean voltage per sample, sample index and channel of each threshold crossing,
    number of channels at the ADC rails per sample, smallest value, largest value)."""
    dc = x.astype(np.float32).mean(1)
    rail = ((x == 0) | (x >= RAIL)).sum(1).astype(np.int16)
    y = signal.sosfiltfilt(_SOS, x.astype(np.float32), axis=0)
    thr = -5 * np.median(np.abs(y), axis=0) / 0.6745
    t, ch = np.nonzero((y[1:] < thr) & (y[:-1] >= thr))
    return dc, (t + 1).astype(np.int64), ch.astype(np.int16), rail, int(x.min()), int(x.max())


def scan(url: str, group: int = 0, workers: int = 8) -> dict:
    """One pass over a channel group: the 10 ms channel-mean trace and 100 ms crossing counts per
    channel, both binned on the recording's own sample clock."""
    g = Group(url, group)
    first = g.chunk(0)
    assert np.array_equal(first, g.first), "range read differs from h5py"
    with ThreadPoolExecutor(workers) as ex:
        parts = list(ex.map(lambda k: reduce_chunk(g.chunk(k)), range(len(g.info))))
    dc = np.concatenate([p[0] for p in parts])
    nb = len(dc) // BIN
    t = np.concatenate([p[1] + k * g.C for k, p in enumerate(parts)])
    ch = np.concatenate([p[2] for p in parts])
    counts = np.zeros((int(np.ceil(g.n / (10 * BIN))), g.width), dtype=np.int32)
    np.add.at(counts, (t // (10 * BIN), ch), 1)
    rail = np.concatenate([p[3] for p in parts]).astype(np.float32)
    n100 = len(rail) // (10 * BIN)
    return dict(dc=dc[: nb * BIN].reshape(nb, BIN).mean(1), counts=counts,
                rail=rail[: n100 * 10 * BIN].reshape(n100, 10 * BIN).mean(1) / g.width,
                vmin=min(p[4] for p in parts), vmax=max(p[5] for p in parts),
                n=g.n, compressed=sum(c.size for c in g.info),
                digest_first=g.raw_digest(0), digest_last=g.raw_digest(len(g.info) - 1))


def light_steps(dc: np.ndarray, step_min: float = STEP_MIN) -> dict:
    """Light onsets (upward steps) and offsets (downward steps) in seconds, from the 10 ms trace.

    A step is a jump between consecutive bins larger than step_min; a run of bins over the
    threshold counts once, at its first bin. Onsets are paired with the next offset.
    """
    dd = np.diff(dc)
    up = np.nonzero((dd > step_min) & np.r_[True, dd[:-1] <= step_min])[0] + 1
    dn = np.nonzero((dd < -step_min) & np.r_[True, dd[:-1] >= -step_min])[0] + 1
    trials = []
    for u in up:
        later = dn[dn > u]
        if len(later) and (len(up[up > u]) == 0 or later[0] < up[up > u][0]):
            trials.append((u, later[0], dd[u - 1], dd[later[0] - 1]))
    on = np.array([t[0] for t in trials]) * BIN / FS
    off = np.array([t[1] for t in trials]) * BIN / FS
    return dict(on=on, off=off, up=np.array([t[2] for t in trials]), down=np.array([t[3] for t in trials]),
                n_up=len(up), n_down=len(dn), noise=float(np.median(np.abs(dd)) / 0.6745))


def window_rates(counts: np.ndarray, on: np.ndarray, dur: float = 10.0) -> dict:
    """Per channel, crossing rate (per s) in pre (10 s before onset), ON (10 s from onset) and OFF
    (onset + 10 to onset + 20 s), averaged over trials whose three windows lie in the recording
    (the windows of the claims file's opening comment)."""
    nb = int(round(dur * 10))
    pre, onr, offr = [], [], []
    for t in on:
        b = int(round(t * 10))
        if b - nb < 0 or b + 2 * nb > len(counts):
            continue
        pre.append(counts[b - nb:b].sum(0) / dur)
        onr.append(counts[b:b + nb].sum(0) / dur)
        offr.append(counts[b + nb:b + 2 * nb].sum(0) / dur)
    if not pre:
        return dict(n_trials=0)
    return dict(n_trials=len(pre), pre=np.mean(pre, 0), on=np.mean(onr, 0), off=np.mean(offr, 0))
