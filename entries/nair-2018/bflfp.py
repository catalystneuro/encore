"""Loading and measures for CRCNS data set bf-1 (basal forebrain LFP in home cage and arena).

Nair, Klaassen, Arato, Vyssotski, Harvey & Rainer (2018), PNAS 115:1352-1357,
doi:10.1073/pnas.1712431115. Data set: Nair et al. (2018), CRCNS.org, doi:10.6080/K0MK6B2Q.

The data set is one archive, basal_forebrain_lfp.tar.gz, in the public bucket crcnsarchive under
bf-1/live/. CRCNS data sets are not versioned, so the version is recorded as "unversioned" and the
archive's MD5 sum from the data set's checksums.md5 is checked while it streams. The archive is a
gzipped tar (not a zip), so it is read as a stream with fsspec and tarfile; each .mat member is
loaded in memory with scipy.io.loadmat and nothing is written to disk.

Each member, Rat_X_Type_Y_Session_Z.mat, holds LFP_data (800 samples by segments), T_data (the time
of each sample, s) and mov_data (one movement-sensor value per segment). The data descriptor gives
400 Hz, 2-s segments, artifact segments removed.

Where the parameters come from:

- Sampling rate 400 Hz and 2-s segments: the data descriptor, checked against T_data in the notebook.
- Power spectrum of each epoch by FFT and gamma power as the mean of the spectrum from 30 to 80 Hz:
  SI Materials and Methods, "Preprocessing and Spectral Analysis" (the claims file's header).
  The FFT is a plain periodogram (no taper, no detrending, density scaling), a standard choice the
  claims file names; the scaling is a constant and cannot change a ratio or a paired test. Band
  edges are included (claims file header, a standard choice).
- Delta 1-5 Hz, theta 6-10 Hz, beta 12-30 Hz: SI, "Low-Frequency Power Modulations", paragraph 1.
- 10-s epochs as the variant epoch length, built from five consecutive 2-s segments: claims file
  header (the SI names 2- and 10-s epochs). Only runs of five segments contiguous in time are used.
- Artifact rule, reading (b): reject an epoch whose peak-to-peak amplitude exceeds the median plus
  1 SD over the file: SI Materials and Methods, "Preprocessing and Spectral Analysis".
- Excursions: boxcar of length 3 on the gamma time course, threshold at the intersection of the
  home-cage and arena gamma histograms, peaks from the unsmoothed data compared with the mean of the
  epochs 4 to 8 s before the peak: SI, "Analysis of Excursions" and the claim's criterion. The
  boxcar runs over the sequence of retained segments, as the paper's data also had artifact epochs
  removed (an assumption; the paper does not say how gaps were handled). Durations are the number
  of smoothed epochs above threshold times 2 s (the claims file: "its duration the time above
  threshold").
"""

from __future__ import annotations

import hashlib
import io
import re
import tarfile

import fsspec
import numpy as np
import pandas as pd
import scipy.io as sio
from scipy.signal import periodogram

DATASET_ID = "bf-1"
DATASET_VERSION = "unversioned"
DATASET_DOI = "10.6080/K0MK6B2Q"
BASE_URL = "https://crcnsarchive.s3-us-west-2.amazonaws.com/bf-1/live/"
ARCHIVE = "basal_forebrain_lfp.tar.gz"

FS = 400.0          # Hz, data descriptor
SEGMENT = 800       # samples per 2-s segment, data descriptor
BANDS = {"delta": (1.0, 5.0), "theta": (6.0, 10.0), "beta": (12.0, 30.0), "gamma": (30.0, 80.0)}
CONDITIONS = ("HCage", "Arena")


class _HashingReader(io.RawIOBase):
    """Pass-through reader that computes the MD5 of everything read."""

    def __init__(self, f):
        self.f, self.md5, self.n = f, hashlib.md5(), 0

    def readable(self):
        return True

    def readinto(self, b):
        data = self.f.read(len(b))
        self.md5.update(data)
        self.n += len(data)
        b[:len(data)] = data
        return len(data)


def checksums() -> dict:
    """The data set's checksums.md5, as {file: md5}."""
    with fsspec.open(BASE_URL + "checksums.md5", "rt") as f:
        return {line.split()[1]: line.split()[0] for line in f if line.strip()}


def load_recordings() -> tuple[list[dict], dict]:
    """Stream the archive and return one dict per .mat member, and facts about the archive.

    Each recording: rat (int), condition ('HCage' or 'Arena', spelled as in the file names),
    session (int), name, lfp (800 x n segments), t (800 x n, s), mov (n), md5 of the member.
    """
    recordings = []
    with fsspec.open(BASE_URL + ARCHIVE, block_size=2**20) as f:
        reader = _HashingReader(f)
        with tarfile.open(fileobj=io.BufferedReader(reader, 2**20), mode="r|gz") as tf:
            for member in tf:
                if not (member.isfile() and member.name.endswith(".mat")):
                    continue
                raw = tf.extractfile(member).read()
                rat, cond, session = re.search(r"Rat_(\d+)_Type_(\w+)_Session_(\d+)\.mat$", member.name).groups()
                mat = sio.loadmat(io.BytesIO(raw))
                recordings.append({
                    "rat": int(rat), "condition": cond, "session": int(session), "name": member.name,
                    "variables": sorted(k for k in mat if not k.startswith("__")),
                    "lfp": mat["LFP_data"], "t": mat["T_data"], "mov": mat["mov_data"].ravel(),
                    "md5": hashlib.md5(raw).hexdigest()})
        # Read to the end of the stream so the MD5 covers the whole archive.
        while reader.read(2**20):
            pass
    recordings.sort(key=lambda r: (r["rat"], r["condition"], r["session"]))
    return recordings, {"md5": reader.md5.hexdigest(), "bytes": reader.n}


def key(r: dict) -> tuple:
    return (r["rat"], r["condition"], r["session"])


def shared_segments(recordings: list[dict]) -> pd.DataFrame:
    """Pairs of recordings that share identical LFP segments, with the count and time offset."""
    seen = {}
    for r in recordings:
        for j in range(r["lfp"].shape[1]):
            seen.setdefault(r["lfp"][:, j].tobytes(), []).append((key(r), r["t"][0, j]))
    rows = {}
    for hits in seen.values():
        for a in range(len(hits)):
            for b in range(a + 1, len(hits)):
                pair = (hits[a][0], hits[b][0])
                rows.setdefault(pair, []).append(hits[a][1] - hits[b][1])
    return pd.DataFrame([{"first": p[0], "second": p[1], "shared_segments": len(o),
                          "time_offsets_s": sorted(set(np.round(o, 3)))} for p, o in rows.items()])


def band_powers(lfp: np.ndarray) -> dict:
    """Mean periodogram power in each band, one value per column (epoch) of lfp."""
    f, p = periodogram(lfp, fs=FS, window="boxcar", detrend=False, scaling="density", axis=0)
    return {name: p[(f >= lo) & (f <= hi)].mean(axis=0) for name, (lo, hi) in BANDS.items()}


def spectrum(lfp: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Frequencies and the periodogram of every epoch (frequency x epoch)."""
    return periodogram(lfp, fs=FS, window="boxcar", detrend=False, scaling="density", axis=0)


def ptp_keep(lfp: np.ndarray) -> np.ndarray:
    """SI rule: keep epochs whose peak-to-peak amplitude is at most the median plus 1 SD."""
    ptp = np.ptp(lfp, axis=0)
    return ptp <= np.median(ptp) + np.std(ptp)


def ten_second_epochs(r: dict) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Non-overlapping 10-s epochs from runs of five 2-s segments contiguous in time.

    Returns the epoch LFP (4000 x m), the start time of each epoch and the mean movement value."""
    starts = r["t"][0]
    blocks, times, movs = [], [], []
    j = 0
    n = len(starts)
    while j + 5 <= n:
        if np.allclose(np.diff(starts[j:j + 5]), 2.0):
            blocks.append(r["lfp"][:, j:j + 5].T.ravel())
            times.append(starts[j])
            movs.append(r["mov"][j:j + 5].mean())
            j += 5
        else:
            j += 1
    if not blocks:
        return np.empty((5 * SEGMENT, 0)), np.empty(0), np.empty(0)
    return np.array(blocks).T, np.array(times), np.array(movs)


def epoch_table(recordings: list[dict], epoch_s: int = 2, artifact: str = "asis") -> pd.DataFrame:
    """One row per epoch: rat, condition, session, time (s from the file's start), movement and the
    band powers. epoch_s is 2 or 10; artifact is 'asis' (segments as delivered) or 'ptp' (the SI's
    peak-to-peak rule applied again, per file)."""
    frames = []
    for r in recordings:
        if epoch_s == 2:
            lfp, t, mov = r["lfp"], r["t"][0], r["mov"]
        else:
            lfp, t, mov = ten_second_epochs(r)
        keep = ptp_keep(lfp) if artifact == "ptp" else np.ones(lfp.shape[1], bool)
        powers = band_powers(lfp[:, keep])
        frames.append(pd.DataFrame({"rat": r["rat"], "condition": r["condition"], "session": r["session"],
                                    "index": np.flatnonzero(keep), "t": t[keep], "mov": mov[keep], **powers}))
    return pd.concat(frames, ignore_index=True)


def boxcar(x: np.ndarray, length: int = 3) -> np.ndarray:
    """Running mean of the given length, same size as x (SI, "Analysis of Excursions").

    At the ends the mean is over the values that exist (two of three), not padded with zeros."""
    kernel = np.ones(length)
    return np.convolve(x, kernel, mode="same") / np.convolve(np.ones(len(x)), kernel, mode="same")


def histogram_intersection(home: np.ndarray, arena: np.ndarray, bins: int = 20) -> float:
    """Threshold where the arena and home-cage histograms cross, on equal bins over the pooled range.

    The crossing searched is between the arena median and the home-cage median: the centre of the
    first bin, going up from the arena median, where the home-cage count reaches the arena count
    (bins: the claims file's standard choice of 20 equal bins). With few epochs a noisy bin can cross
    early, below the crossing of the underlying densities; kde_intersection is run alongside."""
    edges = np.linspace(min(home.min(), arena.min()), max(home.max(), arena.max()), bins + 1)
    h, _ = np.histogram(home, edges, density=True)
    a, _ = np.histogram(arena, edges, density=True)
    centres = (edges[:-1] + edges[1:]) / 2
    lo, hi = np.median(arena), np.median(home)
    for i in np.flatnonzero((centres >= lo) & (centres <= hi)):
        if h[i] >= a[i]:
            # interpolate between this bin and the one below it
            if i > 0 and (a[i - 1] - h[i - 1]) > 0:
                d0, d1 = a[i - 1] - h[i - 1], a[i] - h[i]
                return centres[i - 1] + (centres[i] - centres[i - 1]) * d0 / (d0 - d1)
            return centres[i]
    return (lo + hi) / 2


def kde_intersection(home: np.ndarray, arena: np.ndarray) -> float:
    """Variant threshold: where Gaussian kernel density estimates of the two cross, between the medians."""
    from scipy.stats import gaussian_kde
    grid = np.linspace(np.median(arena), np.median(home), 400)
    d = gaussian_kde(arena)(grid) - gaussian_kde(home)(grid)
    cross = np.flatnonzero(np.diff(np.sign(d)) != 0)
    return grid[cross[0]] if len(cross) else grid[len(grid) // 2]


def excursions(gamma: np.ndarray, theta: np.ndarray, t: np.ndarray, threshold: float) -> list[dict]:
    """Runs of the boxcar-smoothed gamma above threshold.

    For each run: duration (s, epochs above threshold x 2 s), the peak of the unsmoothed gamma within
    the run, and gamma and theta at the peak and as the mean of the epochs 4 to 8 s before it (by
    time, so removed segments are not counted). Runs without any epoch 4 to 8 s before are kept for
    the count and duration, with NaN for the before values."""
    smooth = boxcar(gamma)
    above = smooth > threshold
    out = []
    j, n = 0, len(above)
    while j < n:
        if not above[j]:
            j += 1
            continue
        k = j
        while k < n and above[k]:
            k += 1
        peak = j + int(np.argmax(gamma[j:k]))
        before = (t >= t[peak] - 8.0) & (t <= t[peak] - 4.0)
        out.append({"start_t": t[j], "duration_s": 2.0 * (k - j), "peak_t": t[peak],
                    "gamma_peak": gamma[peak], "theta_peak": theta[peak],
                    "gamma_before": gamma[before].mean() if before.any() else np.nan,
                    "theta_before": theta[before].mean() if before.any() else np.nan})
        j = k
    return out
