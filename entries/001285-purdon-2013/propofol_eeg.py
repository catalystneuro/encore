"""Loading and data checks for dandiset 001285 (Purdon et al. 2013, propofol EEG).

The dandiset is streamed from the DANDI Archive at a pinned version; nothing is
written to disk. It holds one NWB file, one subject, with a single TimeSeries
of 64 EEG channels and no electrode table, behaviour, events or intervals, so
the helpers here only read the EEG and summarise it for the data check. No
claim of the paper is tested with them (see the notebook).

Parameters and where they come from:
- DANDISET, VERSION: the only published version (the paper cites none).
- BANDS: the Results' bands (Results, Dynamics of the EEG Spectrum, paragraph
  1: low frequency 0.1 to 1 Hz, alpha 8 to 12 Hz, beta 13 to 24 Hz, gamma 25 to
  40 Hz). Used here only to describe the recording, not to test a claim.
- WELCH_SECONDS (4 s segments) and BLOCK_SECONDS (60 s blocks): standard
  choices for a descriptive spectrum and time course; they decide no outcome.
- LINE_HZ = 60: the mains frequency where the paper's data were recorded
  (Massachusetts General Hospital, Materials and Methods); used to check the
  sampling rate, a standard check.
"""

from __future__ import annotations

import hashlib

import h5py
import numpy as np
import remfile
import requests
from scipy import signal

DANDISET = "001285"
VERSION = "0.250110.2125"
API = "https://api.dandiarchive.org/api"
SERIES = "acquisition/example_timeseries"

BANDS = {"low (0.1-1 Hz)": (0.1, 1.0), "alpha (8-12 Hz)": (8.0, 12.0),
         "beta (13-24 Hz)": (13.0, 24.0), "gamma (25-40 Hz)": (25.0, 40.0)}
WELCH_SECONDS = 4.0
BLOCK_SECONDS = 60.0
LINE_HZ = 60.0


def version_metadata() -> dict:
    """The pinned version's metadata from the DANDI API."""
    r = requests.get(f"{API}/dandisets/{DANDISET}/versions/{VERSION}/", timeout=60)
    r.raise_for_status()
    return r.json()


def list_versions() -> list[dict]:
    r = requests.get(f"{API}/dandisets/{DANDISET}/versions/", timeout=60)
    r.raise_for_status()
    return r.json()["results"]


def list_assets() -> list[dict]:
    r = requests.get(f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/", params={"page_size": 1000},
                     timeout=60)
    r.raise_for_status()
    return r.json()["results"]


def open_asset(asset_id: str) -> h5py.File:
    """Open an asset's NWB file by streaming it from S3."""
    r = requests.get(f"{API}/assets/{asset_id}/download/", allow_redirects=False, timeout=60)
    r.raise_for_status()
    return h5py.File(remfile.File(r.headers["Location"]), "r")


def describe_hdf5(f: h5py.File) -> list[str]:
    """Every group and dataset in the file, with shapes, types and attributes (the specifications left out)."""
    lines = []

    def visit(name, obj):
        if name.startswith("specifications"):
            return
        attrs = {k: (v.decode() if isinstance(v, bytes) else v) for k, v in obj.attrs.items()
                 if k not in ("object_id",)}
        if isinstance(obj, h5py.Dataset):
            value = ""
            if obj.size <= 4 and obj.dtype.kind in "OSU":
                value = " = " + repr(obj[()])
            lines.append(f"{name}  shape={obj.shape} dtype={obj.dtype}{value}  {attrs}")
        else:
            lines.append(f"{name}/  {attrs}")

    f.visititems(visit)
    return lines


def channel_summaries(data: h5py.Dataset) -> dict[str, np.ndarray]:
    """Per channel (rows of `data`): mean, SD, min, max, NaN count, the longest run of identical
    consecutive samples, a hash of the samples (for exact duplicates), and a decimated copy
    (every 25th sample after a 4 Hz anti-alias filter, i.e. 10 Hz) for correlations."""
    n = data.shape[0]
    out = {k: np.zeros(n) for k in ("mean", "sd", "min", "max", "nan", "longest_flat")}
    out["hash"] = np.empty(n, dtype=object)
    sos = signal.butter(4, 4.0, fs=250.0, output="sos")
    dec = []
    for i in range(n):
        x = data[i, :]
        out["mean"][i], out["sd"][i] = np.nanmean(x), np.nanstd(x)
        out["min"][i], out["max"][i] = np.nanmin(x), np.nanmax(x)
        out["nan"][i] = np.isnan(x).sum()
        same = np.diff(x) == 0
        if same.any():
            edges = np.flatnonzero(np.diff(np.r_[0, same.astype(np.int8), 0]))
            out["longest_flat"][i] = (edges[1::2] - edges[::2]).max() + 1
        else:
            out["longest_flat"][i] = 1
        out["hash"][i] = hashlib.sha1(x.tobytes()).hexdigest()
        dec.append(signal.sosfiltfilt(sos, x)[::25])
    out["decimated"] = np.array(dec)
    return out


def channel_spectra(data: h5py.Dataset, fs: float) -> tuple[np.ndarray, np.ndarray]:
    """Welch spectrum of each channel over the whole recording (WELCH_SECONDS segments)."""
    nper = int(WELCH_SECONDS * fs)
    psd = []
    for i in range(data.shape[0]):
        f, p = signal.welch(data[i, :], fs=fs, nperseg=nper)
        psd.append(p)
    return f, np.array(psd)


def block_band_power(data: h5py.Dataset, fs: float) -> tuple[np.ndarray, dict[str, np.ndarray]]:
    """Power in each band of BANDS per channel and BLOCK_SECONDS block (Welch within the block).
    Returns block start times (s) and, per band, an array channels x blocks."""
    nblock = int(BLOCK_SECONDS * fs)
    nper = int(WELCH_SECONDS * fs) * 5          # 20-s segments, so that 0.1 to 1 Hz has bins (0.05 Hz)
    n_blocks = data.shape[1] // nblock
    out = {b: np.zeros((data.shape[0], n_blocks)) for b in BANDS}
    for i in range(data.shape[0]):
        x = data[i, : n_blocks * nblock].reshape(n_blocks, nblock)
        f, p = signal.welch(x, fs=fs, nperseg=nper, axis=-1)
        for b, (lo, hi) in BANDS.items():
            sel = (f >= lo) & (f <= hi)
            out[b][i] = p[:, sel].mean(axis=1)
    return np.arange(n_blocks) * BLOCK_SECONDS, out
