"""The CN recordings of Gao et al. (2018), streamed from Zenodo, for the claims the dandiset cannot test.

Dandiset 000007 holds only the ALM recordings. The paper's CN recordings (185 sessions, 18 mice,
by the record's description) are deposited as NWB files in one zip archive on Zenodo,
doi:10.5281/zenodo.6647629 (`datafiles_NWB.zip`, 11.9 GB). Zenodo answers HTTP range requests,
so each file is read from the archive's central directory, its compressed bytes are fetched in
32 MB ranges over parallel connections, inflated in memory, and opened with h5py from memory.
Nothing is written to disk. Zenodo allows 133 requests a minute; the large ranges keep the run
to a few hundred requests.

What is read from each file, and how, follows the paper's CN scripts (`analyses_scripts.zip` in
the MATLAB record doi:10.5281/zenodo.6653158, `analysis_compile_all_DCN_data.m` and
`analysis_compiled_all_DCN_ALMsilencing_selectivity.m`):

- trials: start time (session clock), pole in, pole out and cue times relative to the trial
  start, the outcome flags (HitR, HitL, ErrR, ErrL, NoLickR, NoLickL, LickEarly), `GoodTrials`
  and `PhotostimulationType` (0 control; 7, 8, 9, 10 left, right, bilateral ALM and bilateral M1
  photo-inhibition in the delay, by the column's description);
- units: spike times (session clock), and each unit's location from the `cellType` comment of
  its SpikeEventSeries (fastigial, interposed, dentate or outside the CN);
- the scripts' trial selection (correct or error by instructed type, no early lick, performing
  trials, the unit's stable trials) and epochs (sample, delay, response of 1.3 s after the cue).
"""

from __future__ import annotations

import io
import re
import struct
import threading
import time
import zipfile
import zlib
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import requests

ZENODO_RECORD = "6647629"
ZENODO_DOI = "10.5281/zenodo.6647629"
ZIP_URL = f"https://zenodo.org/api/records/{ZENODO_RECORD}/files/datafiles_NWB.zip/content"
CHUNK = 32 << 20
CONNECTIONS = 32
RESPONSE_S = 1.3
LOCATIONS = {"Fastigial unit": "FN", "Interposed unit": "IP", "Dentate unit": "DN", "Outside DCN unit": "outside"}

_local = threading.local()


def _session():
    if not hasattr(_local, "s"):
        _local.s = requests.Session()
    return _local.s


def get_range(a: int, b: int, attempts: int = 8, url: str = ZIP_URL) -> bytes:
    """Bytes a to b (inclusive) of the archive, waiting out the rate limit."""
    for k in range(attempts):
        try:
            r = _session().get(url, headers={"Range": f"bytes={a}-{b}"}, timeout=600)
            if r.status_code == 429:
                time.sleep(max(5.0, float(r.headers.get("Retry-After") or 30)))
                continue
            r.raise_for_status()
            if len(r.content) == b - a + 1:
                return r.content
        except requests.RequestException:
            pass
        time.sleep(2 * (k + 1))
    raise RuntimeError(f"could not fetch bytes {a}-{b} of {url}")


class _RangeFile(io.RawIOBase):
    def __init__(self, size, url):
        self.size, self.pos, self.url = size, 0, url

    def seekable(self):
        return True

    def readable(self):
        return True

    def seek(self, offset, whence=0):
        self.pos = offset if whence == 0 else (self.pos + offset if whence == 1 else self.size + offset)
        return self.pos

    def tell(self):
        return self.pos

    def readinto(self, b):
        if self.pos >= self.size:
            return 0
        end = min(self.pos + len(b), self.size) - 1
        d = get_range(self.pos, end, url=self.url)
        b[:len(d)] = d
        self.pos += len(d)
        return len(d)


def archive_entries(url: str = ZIP_URL, suffix: str = ".nwb") -> list[zipfile.ZipInfo]:
    """The files of a zip archive on Zenodo, read from its central directory with range requests."""
    size = int(requests.head(url, allow_redirects=True, timeout=60).headers["Content-Length"])
    z = zipfile.ZipFile(io.BufferedReader(_RangeFile(size, url), buffer_size=1 << 20))
    return [i for i in z.infolist() if i.filename.endswith(suffix)]


def read_entry(info: zipfile.ZipInfo, pool: ThreadPoolExecutor) -> bytes:
    head = get_range(info.header_offset, info.header_offset + 29)
    name_len, extra_len = struct.unpack("<HH", head[26:30])
    start = info.header_offset + 30 + name_len + extra_len
    parts = [pool.submit(get_range, a, min(a + CHUNK, start + info.compress_size) - 1)
             for a in range(start, start + info.compress_size, CHUNK)]
    inflate = zlib.decompressobj(-15)
    out = [inflate.decompress(p.result()) for p in parts]
    out.append(inflate.flush())
    data = b"".join(out)
    if len(data) != info.file_size or zlib.crc32(data) != info.CRC:
        raise RuntimeError(f"{info.filename} did not inflate to its stated size and checksum")
    return data


def _vec(t, name):
    x = t[name][:]
    if x.ndim == 2:          # CueTime is stored as two rows; the second has a value for every trial
        x = x[-1]
    return x


def parse_session(name: str, data: bytes) -> dict:
    f = h5py.File(io.BytesIO(data), "r")
    t = f["intervals/trials"]
    cols = ["HitR", "HitL", "ErrR", "ErrL", "NoLickR", "NoLickL", "LickEarly"]
    trials = pd.DataFrame({c: _vec(t, c) for c in cols})
    trials["start"] = t["start_time"][:]
    trials["pole_in"] = _vec(t, "PoleInTime")
    trials["pole_out"] = _vec(t, "PoleOutTime")
    trials["cue"] = _vec(t, "CueTime")
    trials["good"] = t["GoodTrials"][:] if "GoodTrials" in t else 1
    trials["stim"] = _vec(t, "PhotostimulationType") if "PhotostimulationType" in t else 0.0
    trials["trial_id"] = t["id"][:]
    trials["trial_type"] = np.select([(trials.HitR + trials.ErrR + trials.NoLickR) > 0,
                                      (trials.HitL + trials.ErrL + trials.NoLickL) > 0], ["R", "L"], None)
    trials["outcome"] = np.select([(trials.HitR + trials.HitL) > 0, (trials.ErrR + trials.ErrL) > 0], ["hit", "error"], "nolick")
    u = f["units"]
    st, idx = u["spike_times"][:], u["spike_times_index"][:].astype(int)
    ids = u["id"][:]
    loc = {}
    for k in f["analysis"]:
        a = f["analysis"][k]
        m = re.search(r"cellType:\s*(.+)", str(a.attrs.get("comments", "")))
        loc[int(a["control"][0])] = LOCATIONS.get(m.group(1).strip(), m.group(1).strip()) if m else None
    tr_of_spike = u["trials"][:]
    spikes, spike_trials = np.split(st, idx[:-1]), np.split(tr_of_spike, idx[:-1])
    order = [np.argsort(s, kind="stable") for s in spikes]
    mouse = re.search(r"/([A-Za-z]+\d+)_", name).group(1)
    f.close()
    return {"file": name.split("/")[-1], "mouse": mouse, "trials": trials,
            "spikes": [s[o] for s, o in zip(spikes, order)],
            "spike_trials": [s[o] for s, o in zip(spike_trials, order)],
            "location": [loc.get(int(i)) for i in ids], "unit_ids": ids.tolist(),
            "nbytes": len(data)}


def load_all(entries=None, files_in_parallel: int = 4) -> tuple[list[dict], dict]:
    """Every CN session of the archive, and timing of the fetch."""
    started = time.time()
    entries = entries if entries is not None else archive_entries()
    pool = ThreadPoolExecutor(CONNECTIONS)

    def one(info):
        return parse_session(info.filename, read_entry(info, pool))

    with ThreadPoolExecutor(files_in_parallel) as ex:
        out = list(ex.map(one, sorted(entries, key=lambda i: -i.compress_size)))
    pool.shutdown()
    timing = {"seconds": time.time() - started, "compressed_bytes": sum(i.compress_size for i in entries),
              "files": len(entries)}
    return sorted(out, key=lambda s: s["file"]), timing


# --- trial selection and measures, as in the paper's CN scripts ---------------------------------

def usable(s: dict) -> pd.Series:
    t = s["trials"]
    return (t.good == 1) & (t.LickEarly == 0) & t.pole_in.notna() & t.cue.notna()


def stable(s: dict, i: int) -> np.ndarray:
    """Trials from the first to the last trial in which unit i fired (the scripts' rule)."""
    tr = s["spike_trials"][i]
    ids = s["trials"].trial_id.values
    if len(tr) == 0:
        return np.zeros(len(ids), bool)
    return (ids >= np.nanmin(tr)) & (ids <= min(np.nanmax(tr), ids.max()))


def epoch_rates(s: dict, i: int) -> pd.DataFrame:
    """Spike rates in the sample, delay and response epochs of every trial."""
    t, sp = s["trials"], s["spikes"][i]
    bounds = {"sample": (t.pole_in, t.pole_out), "delay": (t.pole_out, t.cue), "response": (t.cue, t.cue + RESPONSE_S)}
    out = {}
    for k, (a, b) in bounds.items():
        a_abs, b_abs = (t.start + a).values, (t.start + b).values
        n = np.searchsorted(sp, b_abs) - np.searchsorted(sp, a_abs)
        out[k] = n / (b - a).values
    return pd.DataFrame(out, index=t.index)


def window_counts(s: dict, i: int, col: str, offsets, width: float) -> np.ndarray:
    """Counts in windows of `width` centred at `offsets` from trial event `col`, trials x windows."""
    t, sp = s["trials"], s["spikes"][i]
    t0 = (t.start + t[col]).values[:, None] + np.asarray(offsets)[None, :] - width / 2
    return (np.searchsorted(sp, t0 + width) - np.searchsorted(sp, t0)).astype(float)
