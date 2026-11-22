"""Reading the optogenetic data the paper deposited on figshare ("Data Mouse Opto", article
28440311 version 1, doi:10.6084/m9.figshare.28440311.v1, file 52456058, tmpOptoSharing.zip).

The zip (1.5 GB, about 100,000 members) is read in place over HTTP: its central directory with
`zipfile`, and each member with one range request. Nothing is written to disk.

Layout, as found in the zip: tmpOptoSharing/mouse<id>/<session>/<probe>/<state>/<protocol>/Units/,
with per protocol a SortedUnitsMetrics.csv (one row per unit: cluster_id, area, duration in ms and
the quality metrics) and per unit `Unit <cluster_id>_SpikeLatencies.npy` (spike times in s from
the trial's event) and `Unit <cluster_id>_Trial.npy` (the trial of each spike). Sessions named
optoTH or estim_optoTH have the light over the thalamus, optoCT over MOs (Methods). Protocols:
`estim_<uA>` electrical stimulation alone, `estim-opto_biphasic_<uA>_5_<ms>` with 5 mW of light
starting <ms> after the pulse, `opto_5` light alone. That `opto_5` latencies are timed from the
light onset is an assumption (the deposit has no description).
"""

from __future__ import annotations

import io
import struct
import time
import zlib
from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache

import numpy as np
import pandas as pd
import requests

FIGSHARE_FILE = "https://ndownloader.figshare.com/files/52456058"
FIGSHARE_DOI = "10.6084/m9.figshare.28440311.v1"
_url = [None]
_s = requests.Session()
_s.mount("https://", requests.adapters.HTTPAdapter(pool_connections=32, pool_maxsize=32))


class HttpFile(io.RawIOBase):
    """Seekable read-only file over HTTP range requests (for zipfile's central directory)."""

    def __init__(self, url):
        self.url, self.pos = url, 0
        r = _s.get(url, headers={"Range": "bytes=0-0"}, timeout=120)
        self.size = int(r.headers["Content-Range"].split("/")[-1])

    def seekable(self):
        return True

    def readable(self):
        return True

    def tell(self):
        return self.pos

    def seek(self, off, whence=0):
        self.pos = off if whence == 0 else (self.pos + off if whence == 1 else self.size + off)
        return self.pos

    def readinto(self, buf):
        n = min(len(buf), self.size - self.pos)
        if n <= 0:
            return 0
        b = _s.get(self.url, headers={"Range": f"bytes={self.pos}-{self.pos + n - 1}"}, timeout=120).content
        buf[:len(b)] = b
        self.pos += len(b)
        return len(b)


@lru_cache(maxsize=1)
def archive():
    import zipfile
    url = requests.head(FIGSHARE_FILE, allow_redirects=True, timeout=120).url
    z = zipfile.ZipFile(HttpFile(url))
    return url, {i.filename: i for i in z.infolist()}


def read_member(name: str) -> bytes:
    url, info = archive()
    i = info[name]
    start = i.header_offset
    end = start + 30 + len(i.filename.encode()) + 256 + i.compress_size
    for attempt in range(8):
        r = _s.get(_url[0] or url, headers={"Range": f"bytes={start}-{end}"}, timeout=120)
        b = r.content
        if r.status_code == 206 and b[:4] == b"PK\x03\x04":
            n, m = struct.unpack("<HH", b[26:30])
            data = b[30 + n + m:30 + n + m + i.compress_size]
            if len(data) == i.compress_size:
                break
        # the signed download address expires; resolve it again and wait a little
        _url[0] = requests.head(FIGSHARE_FILE, allow_redirects=True, timeout=120).url
        time.sleep(1 + attempt)
    else:
        raise IOError(f"could not read {name}: HTTP {r.status_code}")
    if i.compress_type == 0:
        return data
    return zlib.decompress(data, -15)


def sessions() -> pd.DataFrame:
    """One row per mouse, session, probe and protocol folder."""
    _, info = archive()
    rows = set()
    for name in info:
        p = name.split("/")
        if len(p) >= 8 and p[6] == "Units" and p[7] == "SortedUnitsMetrics.csv":
            rows.add((p[1], p[2], p[3], p[4], p[5]))
    df = pd.DataFrame(sorted(rows), columns=["mouse", "session", "probe", "state", "protocol"])
    df["light"] = np.where(df.session.str.contains("optoCT"), "MOs", "TH")
    df["kind"] = np.select([df.protocol.str.startswith("estim-opto"), df.protocol.str.startswith("estim"),
                            df.protocol.str.startswith("opto")], ["ES+opto", "ES", "opto"], "other")
    df["light_ms"] = df.protocol.str.extract(r"_(\d+)$")[0].where(df.kind == "ES+opto").astype(float)
    return df


def folder(row) -> str:
    return f"tmpOptoSharing/{row.mouse}/{row.session}/{row.probe}/{row.state}/{row.protocol}/Units/"


def load_units(rows: pd.DataFrame, keep) -> pd.DataFrame:
    """Metrics of the units whose area passes keep(area), and their spikes, for each protocol folder."""
    metas = []
    for _, r in rows.iterrows():
        m = pd.read_csv(io.BytesIO(read_member(folder(r) + "SortedUnitsMetrics.csv")))
        if "area" not in m:
            # One mouse's tables have no area column; Areas.pickle gives the area of each of the
            # probe's 384 channels, so the unit takes the area of its peak channel.
            ch = pd.read_pickle(io.BytesIO(read_member(f"tmpOptoSharing/{r.mouse}/{r.session}/{r.probe}/Areas.pickle")))
            m["area"] = ch.to_numpy()[m.peak_channel.to_numpy()]
            m["area_from"] = "peak channel"
        else:
            m["area_from"] = "table"
        m = m[m.area.astype(str).map(keep)].copy()
        for k in ["mouse", "session", "probe", "protocol", "kind", "light", "light_ms"]:
            m[k] = r[k]
        m["folder"] = folder(r)
        metas.append(m)
    meta = pd.concat(metas, ignore_index=True)
    _, info = archive()

    def one(k):
        r = meta.loc[k]
        base = f"{r.folder}Unit {int(r.cluster_id)}_"
        if base + "SpikeLatencies.npy" not in info:
            return k, None, None
        lat = np.load(io.BytesIO(read_member(base + "SpikeLatencies.npy")))
        tri = np.load(io.BytesIO(read_member(base + "Trial.npy")))
        return k, lat, tri

    with ThreadPoolExecutor(32) as ex:
        res = list(ex.map(one, meta.index))
    meta["lat"] = pd.Series({k: a for k, a, _ in res}, dtype=object)
    meta["trial"] = pd.Series({k: t for k, _, t in res}, dtype=object)
    return meta
