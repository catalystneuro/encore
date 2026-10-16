"""Loading and measures for AJILE12, dandiset 000055, as used by Peterson, Singh et al. (2021).

Peterson SM, Singh SH, Wang NXR, Rao RPN, Brunton BW (2021). Behavioral and neural variability
of naturalistic arm movements. eNeuro 8(3), doi:10.1523/ENEURO.0007-21.2021.

Each NWB file holds one subject and one recording day: ECoG at 500 Hz (`ElectricalSeries`, data
times 1e-6 volts), pose of nine keypoints at 30 Hz (in pixels, though the files say meters),
coarse behavioural labels (`epochs`), and the wrist movement events with their features
(`intervals/reaches`). Files are streamed from the archive at the pinned version; nothing is
written to disk.

ECoG is stored in gzip chunks of 84375 samples x 1 channel. A window around an event costs one
chunk per channel, so `fetch_windows` reads, for each chunk it needs, only the compressed bytes
up to the end of the window (gzip streams decompress from the start), with HTTP range requests
in parallel threads.

Where the parameters come from:

- From the paper's Methods: LFB 8 to 32 Hz and HFB 76 to 100 Hz; power over the first 0.5 s after
  movement onset; baseline 1.5 to 1 s before onset; Morlet wavelets; the eight AAL regions;
  time of day in three 8 h bins from midnight; reach angle folded to -90 (down) to 90 (up).
- From the paper's code (github.com/BruntonUWBio/naturalistic_arm_movements_ecog, commit
  04c6faf2f219586fa834d10c614ef48a694cec55, `config.py`, `tfr_utils.py`, `regression_utils.py`,
  `Plot_banded_power_Fig5.ipynb`), where the Methods leave them open: frequencies 1 to 121 Hz in
  5 Hz steps with n_cycles = f / 4 (MNE `tfr_morlet`), power in dB, decimation by 50 (10 Hz time
  bins); baseline as the mean over its bins, subtracted per event, frequency and channel; band
  power as the median over the bins from 0 to 0.5 s and then over the band's frequencies; the
  projection of baseline-subtracted electrode power onto regions with the paper's projection
  matrices, with the weights of bad electrodes set to 0 and renormalised (bad electrodes are
  those of the subject's first file, as the code takes them); the folding of the reach angle
  (negate, then fold); NaN bimanual ratios set to 0.5; features in seconds, px and px/s.
- The projection matrices (electrode to AAL region weights) are the paper's, from Figshare,
  doi:10.6084/m9.figshare.12114408.v1; they are not in the dandiset.
- Common choices here: the window read around each event (-2 to 2 s; the wavelets are at most
  0.4 s long, as n_cycles = f / 4 gives a Gaussian of SD 1/(8 pi) s at every frequency).
"""

from __future__ import annotations

import io
import multiprocessing as mp
import struct
import zlib
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
import requests
from dandi.dandiapi import DandiAPIClient
from scipy.signal import fftconvolve

DANDISET_ID = "000055"
DANDISET_VERSION = "0.220127.0436"

FS = 500.0                 # ECoG sampling rate, Hz (stated in the files; checked in the notebook)
FS_VIDEO = 30.0            # pose rate, Hz
FREQS = np.arange(1, 124, 5).astype(float)   # code: config.constants_compute_tfr['freqs']
N_CYCLES = FREQS / 4.0                        # code: tfr_utils.compute_tfr
DECIM = 50                                     # code: config, 10 Hz time bins
TIMES = np.round(np.arange(-15, 16) / 10.0, 1)  # TFR bins kept, -1.5 to 1.5 s
BASELINE = (-1.5, -1.0)
T_AVE = (0.0, 0.5)
LFB = (8, 32)
HFB = (76, 100)
WINDOW = (-2.0, 2.0)       # seconds of ECoG read around each event

ROIS = ["Precentral_L", "Frontal_Mid_L", "Postcentral_L", "Parietal_Inf_L", "SupraMarginal_L",
        "Temporal_Sup_L", "Temporal_Mid_L", "Temporal_Inf_L"]
ROI_NAMES = {"Precentral_L": "precentral", "Frontal_Mid_L": "middle frontal",
             "Postcentral_L": "postcentral", "Parietal_Inf_L": "inferior parietal",
             "SupraMarginal_L": "supramarginal", "Temporal_Sup_L": "superior temporal",
             "Temporal_Mid_L": "middle temporal", "Temporal_Inf_L": "inferior temporal"}
FIGSHARE_ARTICLE = 12114408   # "ROI projection matrices and labels", version 1
FIGSHARE_DOI = "10.6084/m9.figshare.12114408.v1"

REACH_COLUMNS = ["start_time", "stop_time", "Reach_magnitude_px", "Reach_angle_degrees",
                 "Onset_speed_px_per_sec", "Speech_ratio", "Bimanual_ratio", "Bimanual_overlap",
                 "Bimanual_class"]
FEATURES = ["day", "time_of_day", "duration", "magnitude", "angle", "onset_speed", "speech_ratio",
            "bimanual_ratio", "bimanual_overlap", "bimanual_class"]


def asset_urls() -> list[tuple[str, str]]:
    """(path, streaming URL) of every NWB file at the pinned version."""
    with DandiAPIClient() as client:
        dandiset = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        return sorted((a.path, a.get_content_url(follow_redirects=1, strip_query=True))
                      for a in dandiset.get_assets() if a.path.endswith(".nwb"))


def dandiset_metadata() -> dict:
    with DandiAPIClient() as client:
        return client.get_dandiset(DANDISET_ID, DANDISET_VERSION).get_raw_metadata()


def _text(value) -> str:
    value = value[()] if hasattr(value, "shape") else value
    return value.decode() if isinstance(value, bytes) else str(value)


def _strings(values) -> list[str]:
    return [v.decode() if isinstance(v, bytes) else str(v) for v in values]


def load_session(path_url: tuple[str, str]) -> dict:
    """Everything but the ECoG and pose samples of one file."""
    path, url = path_url
    with h5py.File(remfile.File(url), "r") as f:
        ecog = f["acquisition/ElectricalSeries"]
        el = f["general/extracellular_ephys/electrodes"]
        electrodes = pd.DataFrame({k: el[k][:] for k in ["x", "y", "z", "imp", "good", "low_freq_R2",
                                                         "high_freq_R2", "standard_deviation",
                                                         "kurtosis", "median_deviation"]})
        electrodes["location"] = _strings(el["location"][:])
        electrodes["group_name"] = _strings(el["group_name"][:])
        groups = {g: _text(f["general/extracellular_ephys"][g].attrs["description"])
                  for g in f["general/extracellular_ephys"] if g != "electrodes"}
        r = f["intervals/reaches"]
        reaches = pd.DataFrame({k: r[k][:] for k in REACH_COLUMNS})
        ep = f["intervals/epochs"]
        epochs = pd.DataFrame({"start": ep["start_time"][:], "stop": ep["stop_time"][:],
                               "label": _strings(ep["labels"][:])})
        pose = f["processing/behavior/Position"]
        session = {
            "path": path, "url": url,
            "subject": _text(f["general/subject/subject_id"]),
            "species": _text(f["general/subject/species"]),
            "subject_fields": sorted(f["general/subject"].keys()),
            "day": int(_text(f["general/session_id"])),
            "session_start": _text(f["session_start_time"]),
            "ecog_shape": ecog["data"].shape,
            "ecog_chunks": ecog["data"].chunks,
            "ecog_rate": float(ecog["starting_time"].attrs["rate"]),
            "ecog_start": float(ecog["starting_time"][()]),
            "ecog_unit": _text(ecog["data"].attrs["unit"]),
            "ecog_conversion": float(ecog["data"].attrs["conversion"]),
            "ecog_electrodes": ecog["electrodes"][:],
            "acquisition": {k: _text(f["acquisition"][k].attrs.get("description", ""))
                            for k in f["acquisition"]},
            "pose_keys": sorted(pose.keys()),
            "pose_n": pose["R_Wrist/data"].shape[0],
            "pose_rate": float(pose["R_Wrist/starting_time"].attrs["rate"]),
            "pose_unit": _text(pose["R_Wrist/data"].attrs["unit"]),
            "pose_conversion": float(pose["R_Wrist/data"].attrs["conversion"]),
            "event_wrist": _text(f["processing/behavior/ReachEvents"].attrs["description"]),
            "event_times": f["processing/behavior/ReachEvents/timestamps"][:],
            "reach_descriptions": {k: _text(r[k].attrs.get("description", "")) for k in REACH_COLUMNS},
            "electrodes": electrodes, "groups": groups, "reaches": reaches, "epochs": epochs,
        }
    session["hemisphere"] = "R" if np.nanmean(electrodes.x) > 0 else "L"
    start = pd.Timestamp(session["session_start"]).tz_convert("UTC")
    # Seconds from the file's midnight (UTC) to session_start_time. The event, epoch and pose
    # times count from that midnight; the ECoG starts at session_start_time (starting_time 0).
    # The two agree in full-day files (offset 0); in three files that start later they do not,
    # and the notebook shows that subtracting the offset aligns the events with the ECoG.
    session["ecog_offset"] = (start - start.normalize()).total_seconds()
    return session


def _pool(workers: int) -> ProcessPoolExecutor:
    return ProcessPoolExecutor(workers, mp_context=mp.get_context("spawn"))


def load_all(workers: int = 12) -> list[dict]:
    """Every file's tables, ordered by subject and day."""
    with _pool(workers) as ex:
        sessions = list(ex.map(load_session, asset_urls()))
    return sorted(sessions, key=lambda s: (s["subject"], s["day"]))


def fold_angle(angle_deg):
    """The code's folding (regression_utils, feat_plot_utils): negate the image-coordinate angle so
    that up is positive, then fold 90 to 270 degrees onto 90 to -90."""
    a = -np.asarray(angle_deg, dtype=float)
    a = np.where(a <= 90, a, 180 - a)
    return np.where(a >= -90, a, -180 - a)


def reach_features(sessions: list[dict]) -> pd.DataFrame:
    """The paper's ten features for every event, with subject, day and event time.

    Time of day is the event time from the start of the file's day, in hours: the files start at
    local midnight as far as the sleep labels show, not at the 19:00 their session_start_time
    states (see the notebook's data check). Duration is stop_time - start_time. Bimanual overlap is kept as stored (seconds; see the
    notebook's data check)."""
    rows = []
    for s in sessions:
        r = s["reaches"]
        clock = (r.start_time / 3600) % 24
        rows.append(pd.DataFrame({
            "subject": s["subject"], "day": s["day"], "event": np.arange(len(r)),
            "t": r.start_time, "time_of_day": clock, "duration": r.stop_time - r.start_time,
            "magnitude": r.Reach_magnitude_px, "angle": fold_angle(r.Reach_angle_degrees),
            "angle_stored": r.Reach_angle_degrees, "onset_speed": r.Onset_speed_px_per_sec,
            "speech_ratio": r.Speech_ratio, "bimanual_ratio": r.Bimanual_ratio.fillna(0.5),
            "bimanual_ratio_nan": r.Bimanual_ratio.isna(),
            "bimanual_overlap": r.Bimanual_overlap, "bimanual_class": r.Bimanual_class}))
    return pd.concat(rows, ignore_index=True)


def wrist_windows(task: dict) -> np.ndarray:
    """x, y (pixels) of one keypoint from 1.5 s before to 4.5 s after each time in
    `task['times']` (seconds on the pose clock): events x frames x 2. Each window is read on its
    own, as the pose arrays hold a whole day."""
    n0, n1 = int(round(1.5 * FS_VIDEO)), int(round(4.5 * FS_VIDEO))
    with h5py.File(remfile.File(task["url"]), "r") as f:
        data = f[f"processing/behavior/Position/{task['keypoint']}/data"]
        out = np.full((len(task["times"]), n0 + n1 + 1, 2), np.nan)
        for k, t in enumerate(task["times"]):
            i = int(round(t * FS_VIDEO))
            if i - n0 >= 0 and i + n1 + 1 <= data.shape[0]:
                out[k] = data[i - n0:i + n1 + 1]
    return out


def run_wrist(tasks: list[dict], workers: int = 12) -> list[np.ndarray]:
    with _pool(workers) as ex:
        return list(ex.map(wrist_windows, tasks))


# ---------------------------------------------------------------- projection weights (Figshare)

def projection_matrices() -> tuple[dict[str, pd.DataFrame], dict[str, pd.DataFrame]]:
    """The paper's electrode-to-AAL weights and region centroids per subject, read into memory
    from Figshare.

    In the weights, row 0 is the electrode density of each region and the other rows are the
    electrodes, each region's column normalised to sum to 1 (project_ecog_to_rois.m). The
    centroids are those of the left-hemisphere part of each region, in MNI coordinates."""
    meta = requests.get(f"https://api.figshare.com/v2/articles/{FIGSHARE_ARTICLE}/versions/1",
                        timeout=60)
    meta.raise_for_status()

    def get(item):
        r = requests.get(item["download_url"], timeout=120)
        r.raise_for_status()
        return item["name"], pd.read_csv(io.BytesIO(r.content))

    with ThreadPoolExecutor(8) as ex:
        tables = dict(ex.map(get, meta.json()["files"]))
    weights = {n.split("_")[1]: t for n, t in tables.items() if n.endswith("_elecs2ROI.csv")}
    centroids = {}
    for n, t in tables.items():
        if n.endswith("_ROIcentroids_Lside.csv"):
            s = n.split("_")[1]
            centroids[s] = t.set_axis(weights[s].columns, axis=0)
    return weights, centroids


def roi_weights(matrix: pd.DataFrame, n_electrodes: int, good: np.ndarray,
                rois: list[str] = ROIS) -> np.ndarray:
    """electrodes x regions weights, with bad electrodes set to 0 and each region renormalised
    (tfr_utils.load_project_spectral_power with rem_bad_chans=True)."""
    w = matrix.iloc[1:n_electrodes + 1][rois].to_numpy(float) * np.asarray(good, float)[:, None]
    return w / w.sum(axis=0, keepdims=True)


def covering(weights: np.ndarray, fraction: float) -> np.ndarray:
    """Indices of the fewest electrodes whose weights sum to `fraction` of each region's weight."""
    keep = set()
    for j in range(weights.shape[1]):
        order = np.argsort(-weights[:, j])
        n = int(np.searchsorted(np.cumsum(weights[order, j]), fraction) + 1)
        keep |= set(order[:n].tolist())
    return np.array(sorted(keep))


# ---------------------------------------------------------------- ECoG windows

def _morlet_bank():
    """MNE's morlet(): Gaussian of SD n_cycles / (2 pi f), cut at 5 SD, normalised."""
    bank = []
    for f, n in zip(FREQS, N_CYCLES):
        sigma = n / (2 * np.pi * f)
        t = np.arange(0, 5 * sigma, 1 / FS)
        t = np.r_[-t[::-1], t[1:]]
        w = np.exp(2j * np.pi * f * t) * np.exp(-t ** 2 / (2 * sigma ** 2))
        bank.append(w / (np.sqrt(0.5) * np.linalg.norm(w)))
    return bank


_BANK = _morlet_bank()


def log_power(x: np.ndarray) -> np.ndarray:
    """dB power of windows (..., samples) at FREQS and TIMES: (..., freqs, times)."""
    n0 = int(round(-WINDOW[0] * FS))
    idx = n0 + np.round(TIMES * FS).astype(int)
    out = np.empty(x.shape[:-1] + (len(FREQS), len(TIMES)))
    for k, w in enumerate(_BANK):
        c = fftconvolve(x, w.reshape((1,) * (x.ndim - 1) + (-1,)), mode="same", axes=-1)
        out[..., k, :] = np.abs(c[..., idx]) ** 2
    with np.errstate(divide="ignore"):
        out = 10 * np.log10(out)
    out[np.isinf(out)] = 0    # tfr_utils.compute_tfr sets infinite values to 0
    return out


def subtract_baseline(p: np.ndarray) -> np.ndarray:
    base = (TIMES >= BASELINE[0]) & (TIMES <= BASELINE[1])
    return p - p[..., base].mean(axis=-1, keepdims=True)


def band_values(p: np.ndarray) -> np.ndarray:
    """(..., freqs, times) -> (..., 2): median over 0 to 0.5 s, then over LFB and HFB frequencies."""
    t = (TIMES >= T_AVE[0]) & (TIMES <= T_AVE[1])
    m = np.median(p[..., t], axis=-1)
    lo = (FREQS >= LFB[0]) & (FREQS <= LFB[1])
    hi = (FREQS >= HFB[0]) & (FREQS <= HFB[1])
    return np.stack([np.median(m[..., lo], axis=-1), np.median(m[..., hi], axis=-1)], axis=-1)


def _range(session, url: str, offset: int, n: int) -> bytes:
    r = session.get(url, headers={"Range": f"bytes={offset}-{offset + n - 1}"}, timeout=120)
    r.raise_for_status()
    return r.content


def chunk_index(url: str, session=None, threads: int = 24) -> dict:
    """Samples per chunk, and (chunk row, channel) -> (byte offset, stored size, filter mask) of
    every ECoG chunk.

    A filter mask of 1 means gzip was skipped for that chunk (HDF5 stores a chunk uncompressed
    when compression would not shrink it).

    h5py looks chunks up one at a time, and over the network each lookup of a B-tree node is a
    request (about 0.4 s per chunk row here). This reads the dataset's version 1 chunk B-tree
    directly, one level at a time with parallel requests: the object header gives the layout
    message (type 8, version 3, chunked) and the B-tree root; each node is "TREE", type, level,
    entries used, two sibling addresses, then keys (chunk size, filter mask, one 8-byte offset
    per dimension plus one) alternating with child addresses (HDF5 file format specification,
    sections III.A.1 and IV.A.2.i). The notebook checks it against h5py on sample chunks."""
    session = session or requests.Session()
    with h5py.File(remfile.File(url), "r") as f:
        # h5g.get_objinfo gives the object header address at once; h5o.get_info takes minutes
        header_address = h5py.h5g.get_objinfo(f["acquisition/ElectricalSeries"].id, b"data").objno[0]
    header = _range(session, url, header_address, 4096)
    if header[0] != 1:
        raise ValueError("expected a version 1 object header")
    size = struct.unpack_from("<I", header, 8)[0]
    blocks, layout = [(header, 16, 16 + size)], None
    while blocks:
        block, p, end = blocks.pop()
        while p + 8 <= end:
            kind, n = struct.unpack_from("<HH", block, p)
            body = block[p + 8:p + 8 + n]
            if kind == 0x10:                         # continuation
                offset, length = struct.unpack_from("<QQ", body)
                blocks.append((_range(session, url, offset, length), 0, length))
            elif kind == 0x08:
                layout = body
            p += 8 + n
    if layout is None or layout[0] != 3 or layout[1] != 2:
        raise ValueError("expected a version 3 chunked layout message")
    ndim = layout[2]
    root = struct.unpack_from("<Q", layout, 3)[0]
    chunk_rows = struct.unpack_from("<I", layout, 11)[0]
    key_size = 8 + 8 * ndim
    node_size = 24 + 129 * (key_size + 8)            # room for up to 128 entries

    def parse(address):
        node = _range(session, url, address, node_size)
        if node[:4] != b"TREE":
            raise ValueError(f"no B-tree node at {address}")
        level, used = struct.unpack_from("<BH", node, 5)
        p, entries = 24, []
        for _ in range(used):
            chunk_size, mask = struct.unpack_from("<II", node, p)
            offsets = struct.unpack_from("<" + "Q" * ndim, node, p + 8)
            child = struct.unpack_from("<Q", node, p + key_size)[0]
            entries.append((offsets, chunk_size, child, mask))
            p += key_size + 8
        return level, entries

    level, entries = parse(root)
    with ThreadPoolExecutor(threads) as ex:
        while level > 0:
            nodes = list(ex.map(parse, [e[2] for e in entries]))
            level = nodes[0][0]
            entries = [e for _, node in nodes for e in node]
    return chunk_rows, {(e[0][0] // chunk_rows, e[0][1]): (e[2], e[1], e[3]) for e in entries}


def fetch_windows(url: str, n_samples: int, times: np.ndarray, channels: np.ndarray,
                  threads: int = 24) -> np.ndarray:
    """ECoG in microvolts around each time: events x channels x samples (WINDOW, at FS).

    Windows that run past the recording are NaN."""
    n0, n1 = int(round(-WINDOW[0] * FS)), int(round(WINDOW[1] * FS))
    starts = np.round(np.asarray(times) * FS).astype(int) - n0
    length = n0 + n1
    session = requests.Session()
    session.mount("https://", requests.adapters.HTTPAdapter(pool_connections=threads,
                                                            pool_maxsize=threads))
    rows_per, index = chunk_index(url, session, threads)   # chunk length differs between files

    def rows(s):
        return range(s // rows_per, (s + length - 1) // rows_per + 1)

    inside = [(k, s) for k, s in enumerate(starts) if s >= 0 and s + length <= n_samples]
    need = {}                                  # chunk row -> samples needed from its start
    for _, s in inside:
        for row in rows(s):
            need[row] = max(need.get(row, 0), min(s + length, (row + 1) * rows_per) - row * rows_per)

    def get(key):
        row, ch = key
        offset, size, mask = index[key]
        want = need[row] * 4
        if mask & 1:                                 # stored without gzip
            return key, np.frombuffer(_range(session, url, offset, want), dtype="<f4")
        # gzip of these float32 samples barely compresses; ask for the bytes the samples need
        # plus a margin, and fetch the rest of the chunk if that was not enough.
        n_bytes, raw = min(size, int(want * 1.02) + 65536), b""
        for attempt in range(4):
            content = _range(session, url, offset, n_bytes)
            if len(content) != n_bytes:              # a short read; ask again
                continue
            raw = zlib.decompressobj().decompress(content)
            if len(raw) >= want:
                break
            n_bytes = size
        if len(raw) < want:
            raise OSError(f"{url}: chunk {key} gave {len(raw)} bytes, {want} needed")
        return key, np.frombuffer(raw[:want], dtype="<f4")

    with ThreadPoolExecutor(threads) as ex:
        chunks = dict(ex.map(get, [(row, int(ch)) for row in sorted(need) for ch in channels]))
    out = np.full((len(starts), len(channels), length), np.nan, dtype=np.float32)
    for k, s in inside:
        for j, ch in enumerate(channels):
            parts = []
            for row in rows(s):
                a = max(s, row * rows_per) - row * rows_per
                b = min(s + length, (row + 1) * rows_per) - row * rows_per
                parts.append(chunks[(row, int(ch))][a:b])
            out[k, j] = np.concatenate(parts)
    return out


def session_power(task: dict) -> dict:
    """For one file: fetch the windows of the requested events and channels and return

    - `bands`: events x channels x 2, baseline-subtracted LFB and HFB power (dB);
    - `bands_raw`: the same without baseline subtraction;
    - `roi_tfr`: events x regions x freqs x times, baseline-subtracted power projected with
      `task['weights']` (channels x regions, rows in the order of `task['channels']`);
    - `roi_tfr_raw`: the same, projected before baseline subtraction;
    - `hf_noise`: events, mean dB power at 116 and 121 Hz over channels and times;
    - `seg_power`: events, mean dB power over all frequencies, channels and times (microvolts^2);
    - `bad_window`: events, True where the window has NaN or is outside the recording, or where a
      channel is flat (all zeros; the preprocessing set artefacts to 0).
    """
    x = fetch_windows(task["url"], task["n_samples"], task["times"], task["channels"])
    bad = np.isnan(x).any(axis=(1, 2)) | (np.abs(x).max(axis=2) == 0).any(axis=1)
    x = np.nan_to_num(x).astype(float)
    p = log_power(x)                                    # events x channels x freqs x times
    pb = subtract_baseline(p)
    w = np.asarray(task["weights"])
    hf = (FREQS >= 115) & (FREQS <= 125)
    return {
        "bands": band_values(pb), "bands_raw": band_values(p),
        "roi_tfr": np.einsum("ecft,cr->erft", pb, w).astype(np.float32),
        "roi_tfr_raw": np.einsum("ecft,cr->erft", p, w).astype(np.float32),
        "hf_noise": p[:, :, hf, :].mean(axis=(1, 2, 3)),
        "seg_power": p.mean(axis=(1, 2, 3)),
        "bad_window": bad,
    }


def run_power(tasks: list[dict], workers: int = 12) -> list[dict]:
    with _pool(workers) as ex:
        return list(ex.map(session_power, tasks))


# ---------------------------------------------------------------- regression (Figure 6)

REG_FEATURES = ["duration", "magnitude", "angle", "onset_speed", "speech_ratio", "bimanual_ratio",
                "bimanual_overlap", "bimanual_class", "day", "time_of_day"]


def design(events: pd.DataFrame) -> tuple[np.ndarray, list[str], dict[str, list[int]]]:
    """The code's design matrix for one subject (regression_utils.single_subj_regression).

    Duration is log-transformed, magnitude and onset speed log(x + 1); the eight continuous
    features are standardised (mean 0, SD 1); day is one-hot by recording day and time of day
    one-hot in three 8 h bins (0 to 8, 8 to 16, 16 to 24, ends included as in the code); the
    one-hot columns are not standardised."""
    cont = pd.DataFrame({
        "duration": np.log(events.duration), "magnitude": np.log(events.magnitude + 1),
        "angle": events.angle, "onset_speed": np.log(events.onset_speed + 1),
        "speech_ratio": events.speech_ratio, "bimanual_ratio": events.bimanual_ratio,
        "bimanual_overlap": events.bimanual_overlap, "bimanual_class": events.bimanual_class})
    cont = (cont - cont.mean()) / cont.std()
    days = pd.get_dummies(events.day.to_numpy(), prefix="day").astype(float)
    tod = events.time_of_day.to_numpy()
    tods = pd.DataFrame({"tod_0_8": ((tod >= 0) & (tod <= 8)).astype(float),
                         "tod_8_16": ((tod >= 8) & (tod <= 16)).astype(float),
                         "tod_16_24": ((tod >= 16) & (tod <= 24)).astype(float)})
    x = pd.concat([cont.reset_index(drop=True), days.reset_index(drop=True), tods], axis=1)
    names = list(x.columns)
    groups = {f: [names.index(f)] for f in REG_FEATURES[:8]}
    groups["day"] = [i for i, n in enumerate(names) if n.startswith("day_")]
    groups["time_of_day"] = [i for i, n in enumerate(names) if n.startswith("tod_")]
    return x.to_numpy(float), names, groups


def _adj_r2(x: np.ndarray, y: np.ndarray) -> float:
    a = np.column_stack([np.ones(len(y)), x])
    beta = np.linalg.lstsq(a, y, rcond=None)[0]
    r2 = 1 - np.sum((y - a @ beta) ** 2) / np.sum((y - y.mean()) ** 2)
    n, p = len(y), x.shape[1]
    return 1 - (1 - r2) * (n - 1) / (n - p - 1)


def forward_select(x: np.ndarray, y: np.ndarray) -> list[int]:
    """Columns kept by forward selection on adjusted R2 of an OLS fit (the code's
    _forward_selected_new): add the best column while adjusted R2 rises above the current score,
    which starts at 0."""
    remaining, selected, current = list(range(x.shape[1])), [], 0.0
    while remaining:
        scores = [(_adj_r2(x[:, selected + [c]], y), c) for c in remaining]
        best, column = max(scores)
        if best <= current:
            break
        remaining.remove(column)
        selected.append(column)
        current = best
    return selected


def day_balanced_split(days: np.ndarray, per_train: float, rng: np.random.Generator):
    """The code's train_test_split_day_balance: the same number of test events from each day."""
    uniq = np.unique(days)
    n_test = int(((1 - per_train) * len(days)) // len(uniq))
    train, test = [], []
    for d in uniq:
        idx = np.flatnonzero(days == d)
        idx = idx[rng.permutation(len(idx))]
        train.extend(idx[:len(idx) - n_test])
        test.extend(idx[len(idx) - n_test:])
    return np.array(train), np.array(test)


def regression_model(task: dict) -> dict:
    """Huber regression of one electrode's band power on the features, over random day-balanced
    splits (`task`: x, y, groups, days, per_train, n_splits, seed).

    As in the code, forward selection runs once on all events and the columns it leaves out are
    set to 0. For each feature, Delta R2 is the full model's test R2 minus that of a model fit with
    the feature's columns shuffled across events; `delta_methods` scores the shuffled model on the
    unshuffled test events (the Methods), `delta_code` on the shuffled ones (the code). A feature
    with no column selected has Delta R2 0."""
    import warnings
    from sklearn.exceptions import ConvergenceWarning
    from sklearn.linear_model import HuberRegressor
    from sklearn.metrics import r2_score

    x, y, groups = task["x"], task["y"], task["groups"]
    rng = np.random.default_rng(task["seed"])
    selected = forward_select(x, y)
    xs = np.zeros_like(x)
    xs[:, selected] = x[:, selected]
    retained = {f: (len(set(c) & set(selected)) / len(c) if f in ("day", "time_of_day")
                    else float(c[0] in selected)) for f, c in groups.items()}
    r2_test, r2_train, coef_angle, unconverged = [], [], [], 0
    delta_methods = {f: [] for f in groups}
    delta_code = {f: [] for f in groups}
    for _ in range(task["n_splits"]):
        train, test = day_balanced_split(task["days"], task["per_train"], rng)
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always", ConvergenceWarning)
            model = HuberRegressor().fit(xs[train], y[train])
            full = r2_score(y[test], model.predict(xs[test]))
            r2_test.append(full)
            r2_train.append(r2_score(y[train], model.predict(xs[train])))
            coef_angle.append(model.coef_[groups["angle"][0]])
            for f, cols in groups.items():
                if not np.any(xs[:, cols]):
                    delta_methods[f].append(0.0)
                    delta_code[f].append(0.0)
                    continue
                shuffled = xs.copy()
                shuffled[:, cols] = xs[rng.permutation(len(y))][:, cols]
                m = HuberRegressor().fit(shuffled[train], y[train])
                delta_methods[f].append(full - r2_score(y[test], m.predict(xs[test])))
                delta_code[f].append(full - r2_score(y[test], m.predict(shuffled[test])))
        unconverged += sum(issubclass(w.category, ConvergenceWarning) for w in caught)
    return {"r2_test": float(np.mean(r2_test)), "r2_train": float(np.mean(r2_train)),
            "coef_angle": float(np.mean(coef_angle)), "retained": retained,
            "delta_methods": {f: float(np.mean(v)) for f, v in delta_methods.items()},
            "delta_code": {f: float(np.mean(v)) for f, v in delta_code.items()},
            "n_fits": task["n_splits"] * (1 + len(groups)), "unconverged": unconverged}


def run_regressions(tasks: list[dict], workers: int = 4) -> list[dict]:
    with _pool(workers) as ex:
        return list(ex.map(regression_model, tasks, chunksize=4))
