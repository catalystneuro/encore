"""Streaming access to CRCNS pvc-10 (Scholl et al. 2015, doi:10.6080/K0GT5K3V).

The data set is unversioned on CRCNS; the files read are those of its published
folder `pvc-10/live/`, at the MD5 sums its `checksums.md5` gives (printed by the
notebook). Files are read anonymously from the public S3 bucket `crcnsarchive`
over range requests (fsspec), never downloaded to disk.

What the published folder holds, per the data descriptor (docs/crcns_pvc-10_data_description.pdf):
- `data/mouse<m>/mouse<m>depth<d>green.mat` and `...red.mat`: MATLAB 7.3 (HDF5) cell arrays
  `green` / `red`, one 2-D frame per element;
- `data/mouse<m>/mouse<m>depth<d>stim.mat`: two columns, the frame at which each stimulus
  starts and its condition (1 blank, 2 to 9 binocular phases 0:45:315, 10 ipsilateral,
  11 contralateral);
- `data/mouse<m>/mouse<m>stats.mat`: per depth, the stimulus duration (s) and the x and y shift
  (um) of the plane;
- `script/cellmasks.mat`: 50 example cell masks for mouse5 depth 260 (descriptor, "How to get
  started"; "a mixture of responsive and nonresponsive cells"), with no cell type.

Parameters and where they come from:
- DARKNOISE = -160: the offset the data set's own examplecode.m subtracts from raw intensity
  ("based on our calibration experiments"); used only in the data check.
- F0_FRAMES = 10: frames before each stimulus onset used for Fo. The paper's Methods say only "the
  gray screen (Fo) immediately before the stimulus came on"; examplecode.m defines a
  pre-stimulus window `stim(i,1):(stim(i,1)+9)` of 10 frames. A standard choice for the data
  check, which decides no claim.
- RESP_WINDOW = 0.5 s centred on the average peak: Methods, Data Imaging Analysis ("mean change
  in fluorescence (DF/F) was calculated in a 0.5 s window, centered around the global average
  peak").
"""

from __future__ import annotations

import io
import re
import time
import urllib.parse
import urllib.request

import fsspec
import h5py
import numpy as np
import scipy.io as sio

BUCKET = "https://crcnsarchive.s3-us-west-2.amazonaws.com/"
DATASET = "pvc-10"
VERSION = "unversioned"  # CRCNS data sets are not versioned (docs/archives.md, CRCNS)
DOI = "10.6080/K0GT5K3V"
LIVE = f"{DATASET}/live/"

DARKNOISE = -160.0
F0_FRAMES = 10
RESP_WINDOW_S = 0.5

CONDITIONS = {1: "blank", **{k: f"binocular {45 * (k - 2)} deg" for k in range(2, 10)},
              10: "ipsilateral", 11: "contralateral"}


def list_bucket(prefix: str = f"{DATASET}/") -> list[tuple[str, int]]:
    """All (key, size) pairs under a prefix of the bucket, following continuation tokens."""
    out, token = [], None
    while True:
        url = f"{BUCKET}?list-type=2&prefix={prefix}"
        if token:
            url += "&continuation-token=" + urllib.parse.quote(token)
        xml = urllib.request.urlopen(url).read().decode()
        out += [(k, int(s)) for k, s in re.findall(r"<Key>(.*?)</Key>.*?<Size>(\d+)</Size>", xml, re.S)]
        m = re.search(r"<NextContinuationToken>(.*?)</NextContinuationToken>", xml)
        if not m:
            return out
        token = m.group(1)


def read_text(path: str) -> str:
    with fsspec.open(BUCKET + path, "rb").open() as f:
        return f.read().decode("utf-8", "replace")


def checksums() -> dict[str, str]:
    """MD5 sums published in live/checksums.md5, keyed by path relative to live/."""
    out = {}
    for line in read_text(LIVE + "checksums.md5").splitlines():
        parts = line.split()
        if len(parts) == 2:
            out[parts[1]] = parts[0]
    return out


def load_small_mat(path: str) -> dict:
    """A MATLAB 5 file read whole into memory (stim, stats and mask files are a few kB)."""
    with fsspec.open(BUCKET + path, "rb").open() as f:
        d = sio.loadmat(io.BytesIO(f.read()))
    return {k: v for k, v in d.items() if not k.startswith("__")}


def planes() -> dict[int, list[int]]:
    """Depths with a green, red and stim file, per mouse, from the bucket listing of live/data."""
    keys = [k for k, _ in list_bucket(LIVE + "data/")]
    out: dict[int, set] = {}
    for k in keys:
        m = re.search(r"mouse(\d+)depth(\d+)(green|red|stim)\.mat$", k)
        if m:
            out.setdefault(int(m.group(1)), set()).add(int(m.group(2)))
    return {m: sorted(d) for m, d in sorted(out.items())}


def plane_path(mouse: int, depth: int, kind: str) -> str:
    return f"{LIVE}data/mouse{mouse}/mouse{mouse}depth{depth}{kind}.mat"


def stim_table(mouse: int, depth: int) -> np.ndarray:
    """(n, 2) int array: onset frame (1-based, MATLAB) and condition 1 to 11."""
    d = load_small_mat(plane_path(mouse, depth, "stim"))
    (v,) = d.values()
    return np.asarray(v, dtype=int)


def stats_table(mouse: int) -> np.ndarray:
    """(n, 4): depth (um), stimulus duration (s), x shift (um), y shift (um)."""
    d = load_small_mat(f"{LIVE}data/mouse{mouse}/mouse{mouse}stats.mat")
    (v,) = d.values()
    return np.asarray(v, dtype=float)


class Movie:
    """One channel of one plane, opened in place over HTTP range requests.

    MATLAB stores the cell array as a (n_frames, 1) array of object references, each frame
    a (455, 256) float64 dataset in HDF5 order, i.e. 256 rows by 455 columns in MATLAB.
    `frame(i)` returns it in MATLAB orientation (rows, columns) = (256, 455).
    """

    def __init__(self, mouse: int, depth: int, channel: str = "green"):
        self.path = plane_path(mouse, depth, channel)
        self._fh = fsspec.open(BUCKET + self.path, "rb", block_size=2**22,
                               cache_type="readahead").open()
        self._h5 = h5py.File(self._fh, "r")
        self._var = self._h5[channel]
        self.refs = self._var[:, 0]
        self.n_frames = len(self.refs)

    def frame_dataset(self, i: int):
        return self._h5[self.refs[i]]

    def frame(self, i: int) -> np.ndarray:
        return self._h5[self.refs[i]][:].T

    def close(self):
        self._h5.close()
        self._fh.close()


def mask_traces(movie: Movie, masks: np.ndarray, frames=None) -> tuple[np.ndarray, float]:
    """Mean intensity in each mask, per frame, minus DARKNOISE (as examplecode.m does).

    masks: (256, 455, n) in MATLAB orientation. Returns (n, n_frames) and the seconds taken.
    Holds one frame at a time in memory.
    """
    frames = range(movie.n_frames) if frames is None else frames
    m = masks.astype(bool)
    n = m.shape[2]
    flat = m.reshape(-1, n)
    counts = flat.sum(0)
    out = np.empty((n, len(frames)))
    t0 = time.time()
    for j, i in enumerate(frames):
        f = movie.frame(i).reshape(-1)
        out[:, j] = (f @ flat) / counts - DARKNOISE
    return out, time.time() - t0


def trial_dff(trace: np.ndarray, stim: np.ndarray, n_post: int, shift: int = 0) -> np.ndarray:
    """dF/F for each trial: (F - Fo) / Fo, Fo the mean of F0_FRAMES frames before onset.

    trace: (n_cells, n_frames); stim onsets are 1-based. `shift` moves every onset by that many
    frames (used for the clock check). Returns (n_cells, n_trials, n_post).
    """
    on = stim[:, 0] - 1 + shift
    out = np.full((trace.shape[0], len(on), n_post), np.nan)
    for k, o in enumerate(on):
        if o - F0_FRAMES < 0 or o + n_post > trace.shape[1]:
            continue
        f0 = trace[:, o - F0_FRAMES:o].mean(1, keepdims=True)
        out[:, k] = (trace[:, o:o + n_post] - f0) / f0
    return out
