"""Loading and AP detection for the fast optical membrane potential imaging of dandisets 001030
and 001272.

Semenov, Kim, Silkuniene & Pakhomov (2025), doi:10.1016/j.xcrp.2025.102660.

Figure 3C (dandiset 001030): 2-s, 2-kHz unmodulated sine waves, ramped over the first 250 ms, in
the low-conductivity sodium gluconate solution. Each NWB file holds one session, a uint16 image
stack of 16 x 16 pixels at 3,134.8 frames/s. The session description gives the amplitude, and that
the stimulus "begins at 25 ms and lasts 2 s".

Figure S1 (dandiset 001272): 250-ms, 2-kHz sine waves with Di-8-ANEPPS instead of FluoVolt, 16 x 16
pixels at the rate the file gives. The descriptions give the amplitude but not the stimulus timing,
which is taken from the Methods ("The standard imaging protocol started 50 ms before sine wave
stimulation and continued for 250 ms during", `S1_STIM_START_S`, `S1_STIM_S`).

Files are streamed from the archive at the pinned versions; nothing is written to disk.

Where the parameters come from:

- F and dF. Methods, Recording of the optical APs: F is "the emission intensity over the entire
  cell soma", F0 "the mean value over a time interval preceding the electrical stimulation", and
  dF = 100% (F - F0) / F0. At 16 x 16 pixels the soma cannot be outlined, so F is the mean over the
  whole frame (a standard choice; the neuron was centred in the field of vision). The first frame
  of every file is several times brighter than the rest and the next ones recover from it over a
  few ms, so the first `DROP_FRAMES` frames (6.4 ms) are dropped (a standard choice).
- Bleaching. Methods: the long recordings of Figure 3C "were corrected for bleaching by
  subtracting a trace without APs". The only session without APs under both detection readings
  is used as that trace (chosen in the notebook from the data).
- AP detection. The claims file's readings (fig1-pure-sine-excites-all): (a) a peak above 5% dF,
  (b) a rise of at least 5% dF within 5 ms. Peaks are at least 5 ms apart, and for (a) stand at
  least `PROMINENCE` above their surroundings (standard choices; APs last about 10 ms, Methods).
"""

from __future__ import annotations

import json
import re
import urllib.request
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import remfile
from scipy.signal import find_peaks

DANDISET_ID = "001030"
DANDISET_VERSION = "0.240520.1924"
API = "https://api.dandiarchive.org/api"

FS = 3134.8               # frames/s, from the series rate and the session description
STIM_START_S = 0.025      # session description: "begins at 25 ms"
STIM_S = 2.0              # session description: "lasts 2 s"
RAMP_S = 0.25             # session description: ramped "during the initial 0.25 s"
AP_LEVEL = 5.0            # % dF, Methods (APs peaked at more than 5% dF)
RISE_WINDOW_S = 0.005     # claims file, reading (b)
MIN_SEPARATION_S = 0.005  # standard choice
PROMINENCE = 2.5          # % dF, standard choice for reading (a)
S1_DANDISET, S1_VERSION = "001272", "0.250805.1358"
S1_STIM_START_S = 0.05    # Methods, Recording of the optical APs
S1_STIM_S = 0.25
DROP_FRAMES = 20          # standard choice: the bright first frame and the recovery after it


def list_assets(dandiset=DANDISET_ID, version=DANDISET_VERSION):
    url = f"{API}/dandisets/{dandiset}/versions/{version}/assets/?page_size=1000"
    with urllib.request.urlopen(url) as r:
        results = json.load(r)["results"]
    return [{"path": a["path"], "url": f"{API}/assets/{a['asset_id']}/download/"} for a in results]


def read_session(asset):
    """Metadata and the whole-frame mean trace of one session."""
    with h5py.File(remfile.File(asset["url"]), "r") as h:
        s = h["acquisition/TimeLapseImaging"]
        desc = h["session_description"][()].decode()
        data = s["data"][:]
        out = {
            "path": asset["path"],
            "subject_id": h["general/subject/subject_id"][()].decode(),
            "species": h["general/subject/species"][()].decode(),
            "session_start": h["session_start_time"][()].decode(),
            "description": desc,
            "rate_hz": float(s["starting_time"].attrs["rate"]),
            "shape": tuple(data.shape),
        }
    amp = re.search(r"(?:under|with) ([\d.]+)V amplitude", desc)
    out["amplitude_v"] = float(amp.group(1)) if amp else np.nan
    out["cell"] = out["subject_id"].split("_")[0]
    out["frame_means"] = data.reshape(len(data), -1).mean(axis=1)
    return out


def read_all(assets):
    with ThreadPoolExecutor(16) as ex:
        return list(ex.map(read_session, assets))


def delta_f(frame_means, fs=FS, stim_start_s=STIM_START_S):
    """dF (%) per frame, F0 the mean before the stimulus; the first frames are dropped (NaN)."""
    f = frame_means.astype(float).copy()
    f[:DROP_FRAMES] = np.nan
    start = int(stim_start_s * fs)
    f0 = np.nanmean(f[DROP_FRAMES:start])
    return 100 * (f - f0) / f0


def detect(dF, reading, fs=FS, level=None):
    """Frames of the AP peaks under reading "a" or "b" (and "c", a peak above `level`, used for the
    5 SD reading of the Di-8-ANEPPS claim)."""
    x = np.where(np.isnan(dF), 0.0, dF)
    sep = int(round(MIN_SEPARATION_S * fs))
    if reading in ("a", "c"):
        height = AP_LEVEL if reading == "a" else level
        peaks, _ = find_peaks(x, height=height, distance=sep, prominence=PROMINENCE)
    else:
        w = int(round(RISE_WINDOW_S * fs))
        padded = np.concatenate([np.full(w, x[0]), x])
        rise = x - np.lib.stride_tricks.sliding_window_view(padded, w + 1).min(axis=1)
        peaks, _ = find_peaks(rise, height=AP_LEVEL, distance=sep)
    return peaks


def windows():
    """Frame ranges: the stimulus, after the 250-ms ramp, and its last 250 ms."""
    start = int(STIM_START_S * FS)
    end = int((STIM_START_S + STIM_S) * FS)
    return {"stimulus": (start, end), "after_ramp": (start + int(RAMP_S * FS), end),
            "last_250ms": (end - int(0.25 * FS), end)}
