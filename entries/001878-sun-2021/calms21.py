"""Loading CalMS21 (Sun et al. 2021) from dandiset 001878 and from its CaltechDATA deposit.

Dandiset 001878 has no published version. The entry reads the draft and pins it by the blob id of
each asset it uses: if an asset changes, `asset_url` raises, so that a changed draft cannot pass
unnoticed. The draft's modification time when the entry was written is DRAFT_MODIFIED.

The dandiset holds one CalMS21 sequence, Task 1 test sequence mouse071, as an NWB file with MARS
pose (ndx-pose), the frame annotations as bouts (ndx-ethogram), two per-frame series the converter
derived from the pose, and the source video as an external mp4.

The paper's full dataset is on CaltechDATA (doi:10.22002/D1.1991, record s0vdx-0k302, version
1.0), as zip files of JSON. `caltech_sequences` streams one JSON member of a zip with HTTP range
requests and yields its sequences one at a time, without writing anything to disk.

Parameters and conventions:
- Keypoint order (nose, left ear, right ear, neck, left hip, right hip, tail base), mouse 0 the
  resident and mouse 1 the intruder, image size 1024 x 570, 30 Hz, and the Task 1 vocabulary
  {attack: 0, investigation: 1, mount: 2, other: 3}: the paper's Appendix C and D.
- Array layout of keypoints (frames, mouse, x/y, body part): the paper's Appendix C and the
  CaltechDATA readme.
- A frame's label from the bouts: the bout whose [start, stop) holds the frame's time, with times
  taken at frame index / 30. This is a choice made here; the NWB file does not say whether
  stop_time is inclusive.
"""

from __future__ import annotations

import datetime
import hashlib
import io
import json
import re
import struct
import time
import urllib.parse
import zipfile
import zlib

import h5py
import numpy as np
import pandas as pd
import remfile
import requests

DANDISET_ID = "001878"
DANDISET_VERSION = "draft"
DRAFT_MODIFIED = "2026-06-25T18:32:10.096594Z"
API = "https://api.dandiarchive.org/api"

CALMS21_NWB = "sub-mouse071-resident-intruder/sub-mouse071-resident-intruder_ses-mouse071-task1_image.nwb"
CALMS21_MP4 = ("sub-mouse071-resident-intruder/sub-mouse071-resident-intruder_ses-mouse071-task1_image/"
               "304bc772-9d15-41a5-80bd-bc57dcd5c9b9_external_file_0.mp4")
BLOBS = {  # blob id of each asset of the draft when the entry was written
    CALMS21_NWB: "e169899a-5a31-44d1-aa7a-93c33e5d3e73",
    CALMS21_MP4: "73781d39-da5a-41c9-9f25-9e009ca260d1",
}

PARTS = ["nose", "ear_left", "ear_right", "neck", "hip_left", "hip_right", "tail_base"]
MICE = ["resident", "intruder"]
RATE = 30.0
IMAGE_W, IMAGE_H = 1024, 570
TASK1_VOCAB = {"attack": 0, "investigation": 1, "mount": 2, "other": 3}

CALTECH_RECORD = "s0vdx-0k302"
CALTECH_DOI = "10.22002/D1.1991"


# --- dandiset -----------------------------------------------------------------

def draft_info() -> dict:
    """The draft's metadata summary: modification time and asset count."""
    r = requests.get(f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/info/", timeout=60)
    r.raise_for_status()
    return r.json()


def list_assets() -> pd.DataFrame:
    r = requests.get(f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/",
                     params={"page_size": 200}, timeout=60)
    r.raise_for_status()
    return pd.DataFrame(r.json()["results"])[["path", "size", "blob", "asset_id", "modified"]]


def asset_url(path: str) -> str:
    """Download URL of an asset of the draft, after checking its blob is the one pinned here."""
    r = requests.get(f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/",
                     params={"path": path, "page_size": 10}, timeout=60)
    r.raise_for_status()
    hits = [a for a in r.json()["results"] if a["path"] == path]
    if len(hits) != 1:
        raise RuntimeError(f"asset {path} not found in dandiset {DANDISET_ID} {DANDISET_VERSION}")
    if path in BLOBS and hits[0]["blob"] != BLOBS[path]:
        raise RuntimeError(f"asset {path} has changed (blob {hits[0]['blob']}, pinned {BLOBS[path]})")
    return requests.head(f"{API}/assets/{hits[0]['asset_id']}/download/", allow_redirects=True,
                         timeout=60).url


def _text(x):
    return x.decode() if isinstance(x, bytes) else str(x)


def load_session(path: str = CALMS21_NWB) -> dict:
    """Everything the analysis uses from the CalMS21 NWB file, as arrays.

    keypoints: (frames, mouse, x/y, part), the CalMS21 layout; scores: (frames, mouse, part).
    """
    f = h5py.File(remfile.File(asset_url(path)), "r")
    beh = f["processing/behavior"]
    pe = beh["PoseEstimation"]
    series = {}
    for m in MICE:
        for p in PARTS:
            g = pe[f"{m}_{p}"]
            series[(m, p)] = {
                "data": g["data"][:], "confidence": g["confidence"][:],
                "rate": float(g["starting_time"].attrs["rate"]), "start": float(g["starting_time"][()]),
                "unit": g["data"].attrs["unit"], "reference_frame": _text(g["reference_frame"][()])}
    n = len(series[("resident", "nose")]["data"])
    kp = np.empty((n, 2, 2, 7))
    sc = np.empty((n, 2, 7))
    for i, m in enumerate(MICE):
        for j, p in enumerate(PARTS):
            kp[:, i, :, j] = series[(m, p)]["data"]
            sc[:, i, j] = series[(m, p)]["confidence"]
    b = beh["CalMS21"]
    bouts = pd.DataFrame({c: (b[c][:] if b[c].dtype.kind != "O" else [_text(v) for v in b[c][:]])
                          for c in b.attrs["colnames"]})
    eth = beh["CalMS21_ethogram"]
    ethogram = pd.DataFrame({c: (eth[c][:] if eth[c].dtype.kind != "O" else [_text(v) for v in eth[c][:]])
                             for c in eth.attrs["colnames"]})
    vid = f["acquisition/behavior_video"]
    out = {
        "keypoints": kp, "scores": sc, "n_frames": n, "series": series,
        "pose_dimensions": pe["dimensions"][:].tolist(), "pose_software": _text(pe["source_software"][()]),
        "skeleton_nodes": [_text(v) for v in beh["Skeletons/two_mice/nodes"][:]],
        "skeleton_edges": beh["Skeletons/two_mice/edges"][:].tolist(),
        "bouts": bouts, "ethogram": ethogram, "annotator": _text(b.attrs.get("annotator", "")),
        "bouts_description": _text(b.attrs.get("description", "")),
        "centroid_speed": beh["centroid_speed/data"][:],
        "centroid_speed_unit": beh["centroid_speed/data"].attrs["unit"],
        "centroid_speed_rate": float(beh["centroid_speed/starting_time"].attrs["rate"]),
        "interanimal_distance": beh["interanimal_distance/data"][:],
        "interanimal_distance_rate": float(beh["interanimal_distance/starting_time"].attrs["rate"]),
        "video_rate": float(vid["starting_time"].attrs["rate"]),
        "video_external_file": [_text(v) for v in vid["external_file"][:]],
        "session_id": _text(f["general/session_id"][()]),
        "identifier": _text(f["identifier"][()]),
        "session_start_time": _text(f["session_start_time"][()]),
        "related_publications": [_text(v) for v in f["general/related_publications"][:]],
        "subject": {k: _text(f[f"general/subject/{k}"][()]) for k in f["general/subject"].keys()},
    }
    f.close()
    return out


def pose_overview(path: str) -> dict:
    """Pose series names, their frame counts and the related publications of any NWB file of the draft."""
    f = h5py.File(remfile.File(asset_url(path)), "r")
    pe = f["processing/behavior/PoseEstimation"]
    series = {k: pe[k]["data"].shape[0] for k in pe.keys()
              if isinstance(pe[k], h5py.Group) and "reference_frame" in pe[k]}
    pubs = ([_text(v) for v in f["general/related_publications"][:]]
            if "related_publications" in f["general"] else [])
    f.close()
    return {"series": sorted(series), "frames": sorted(set(series.values())), "related_publications": pubs}


def frame_labels(bouts: pd.DataFrame, n_frames: int, rate: float = RATE) -> np.ndarray:
    """Label name of each frame from the bouts table; '' where no bout covers the frame.

    Raises if two bouts cover one frame.
    """
    t = np.arange(n_frames) / rate
    labels = np.full(n_frames, "", dtype=object)
    covered = np.zeros(n_frames, int)
    for start, stop, lab in zip(bouts.start_time, bouts.stop_time, bouts.label):
        sel = (t >= start - 1e-9) & (t < stop - 1e-9)
        labels[sel] = lab
        covered += sel
    if covered.max() > 1:
        raise ValueError("bouts overlap")
    return labels


def centroids(kp: np.ndarray) -> np.ndarray:
    """Centroid of each mouse, the mean of its seven keypoints: (frames, mouse, x/y)."""
    return kp.mean(axis=3)


def speed(xy: np.ndarray, rate: float = RATE) -> np.ndarray:
    """Speed (pixels/s) of a (frames, 2) trajectory; the first frame repeats the second."""
    v = np.hypot(*np.diff(xy, axis=0).T) * rate
    return np.concatenate([v[:1], v])


def nose_to_intruder(kp: np.ndarray) -> np.ndarray:
    """Distance (pixels) from the resident's nose to the nearest intruder keypoint, per frame."""
    nose = kp[:, 0, :, 0][:, :, None]
    return np.sqrt(((kp[:, 1] - nose) ** 2).sum(axis=1)).min(axis=1)


def block_bootstrap_diff(values: np.ndarray, group: np.ndarray, block: int, n_boot: int,
                         rng: np.random.Generator, stat=np.median,
                         include: np.ndarray | None = None) -> tuple[float, float, float]:
    """Difference stat(values[group]) - stat(values[~group]) with a 95% CI from a moving-block
    bootstrap over frames (contiguous blocks of `block` frames of the session, resampled with
    replacement). With `include`, only the frames where it is True enter either group; the blocks
    are still drawn from the whole session, so each block is a contiguous stretch of time."""
    n = len(values)
    inc = np.ones(n, bool) if include is None else include.astype(bool)
    obs = stat(values[inc & group]) - stat(values[inc & ~group])
    starts = np.arange(0, n - block + 1)
    k = int(np.ceil(n / block))
    diffs = []
    for _ in range(n_boot):
        s = rng.choice(starts, size=k, replace=True)
        idx = (s[:, None] + np.arange(block)[None, :]).ravel()[:n]
        idx = idx[inc[idx]]
        g, v = group[idx], values[idx]
        if g.all() or not g.any():
            continue
        diffs.append(stat(v[g]) - stat(v[~g]))
    lo, hi = np.percentile(diffs, [2.5, 97.5])
    return float(obs), float(lo), float(hi)


# --- video --------------------------------------------------------------------

def video_frames(every: int = 1, step: int = 4):
    """Stream the source video of mouse071 and yield (frame index, gray image downsampled by `step`)
    for every `every`-th frame. Every frame is decoded, so the indices are exact."""
    import av
    container = av.open(remfile.File(asset_url(CALMS21_MP4)))
    stream = container.streams.video[0]
    stream.thread_type = "AUTO"
    for i, frame in enumerate(container.decode(stream)):
        if i % every == 0:
            yield i, frame.to_ndarray(format="gray")[::step, ::step]
    container.close()


def video_frames_at(indices, step: int = 1) -> dict:
    """Decode the video up to the largest requested index and return {index: gray image
    downsampled by `step`} for the requested frames."""
    want = set(int(i) for i in indices)
    out = {}
    for i, img in video_frames(every=1, step=step):
        if i in want:
            out[i] = img
        if i >= max(want):
            break
    return out


def video_info() -> dict:
    import av
    container = av.open(remfile.File(asset_url(CALMS21_MP4)))
    s = container.streams.video[0]
    info = {"frames": s.frames, "rate": float(s.average_rate), "width": s.codec_context.width,
            "height": s.codec_context.height, "codec": s.codec_context.name,
            "duration_s": float(s.duration * s.time_base) if s.duration else None}
    container.close()
    return info


# --- CaltechDATA ----------------------------------------------------------------

def caltech_url(filename: str, min_left: float = 30.0) -> str:
    """Direct URL of a file of the CalMS21 record. It is presigned for 60 s, so a fresh one is
    taken for each read. The server reuses a signed URL for a while, so one with less than
    `min_left` seconds of validity left is not used: the function waits for it to expire and asks
    again."""
    for _ in range(3):
        with requests.get(f"https://data.caltech.edu/records/{CALTECH_RECORD}/files/{filename}?download=1",
                          allow_redirects=True, stream=True, timeout=60) as r:
            r.raise_for_status()
            url = r.url
        q = dict(urllib.parse.parse_qsl(urllib.parse.urlparse(url).query))
        signed = datetime.datetime.strptime(q["X-Amz-Date"], "%Y%m%dT%H%M%SZ").replace(tzinfo=datetime.timezone.utc)
        left = (signed - datetime.datetime.now(datetime.timezone.utc)).total_seconds() + int(q["X-Amz-Expires"])
        if left >= min_left:
            return url
        time.sleep(max(left, 0) + 1)
    raise RuntimeError(f"no signed URL for {filename} with {min_left} s of validity left")


def caltech_files() -> pd.DataFrame:
    r = requests.get(f"https://data.caltech.edu/api/records/{CALTECH_RECORD}/files", timeout=60)
    r.raise_for_status()
    return pd.DataFrame([{"file": e["key"], "size": e["size"], "checksum": e["checksum"]}
                         for e in r.json()["entries"]])


def caltech_record() -> dict:
    r = requests.get(f"https://data.caltech.edu/api/records/{CALTECH_RECORD}", timeout=60)
    r.raise_for_status()
    d = r.json()
    return {"doi": d["pids"]["doi"]["identifier"], "version": d["metadata"].get("version"),
            "publication_date": d["metadata"].get("publication_date"), "updated": d.get("updated"),
            "rights": [x.get("id") or x.get("title", {}).get("en") for x in d["metadata"].get("rights", [])]}


class _HTTPRange(io.RawIOBase):
    """A read-only seekable file over HTTP range requests, enough for zipfile's central directory."""

    def __init__(self, url):
        self.url, self.pos, self.size = url, 0, None

    def seekable(self):
        return True

    def readable(self):
        return True

    def tell(self):
        return self.pos

    def seek(self, offset, whence=0):
        if whence == 2 and self.size is None:
            r = requests.get(self.url, headers={"Range": "bytes=0-0"}, timeout=60)
            r.raise_for_status()
            self.size = int(r.headers["content-range"].split("/")[1])
        self.pos = {0: offset, 1: self.pos + offset, 2: (self.size or 0) + offset}[whence]
        return self.pos

    def read(self, n=-1):
        if n is None or n < 0:
            n = self.size - self.pos
        if n == 0:
            return b""
        r = requests.get(self.url, headers={"Range": f"bytes={self.pos}-{self.pos + n - 1}"}, timeout=120)
        r.raise_for_status()
        self.pos += len(r.content)
        return r.content


def zip_members(zip_name: str) -> pd.DataFrame:
    """The members of a zip of the CalMS21 record, read from its central directory."""
    url = caltech_url(zip_name)
    z = zipfile.ZipFile(_HTTPRange(url))
    return pd.DataFrame([{"member": i.filename, "size": i.file_size, "compressed": i.compress_size,
                          "crc32": i.CRC} for i in z.infolist()])


def _member_bytes(zip_name: str, member: str, chunk: int = 1 << 23):
    """Decompressed bytes of one deflated zip member, streamed in chunks."""
    url = caltech_url(zip_name)
    zi = zipfile.ZipFile(_HTTPRange(url)).getinfo(member)
    head = requests.get(url, headers={"Range": f"bytes={zi.header_offset}-{zi.header_offset + 29}"},
                        timeout=60).content
    name_len, extra_len = struct.unpack("<HH", head[26:30])
    start = zi.header_offset + 30 + name_len + extra_len
    d = zlib.decompressobj(-15)
    total, crc = 0, 0
    with requests.get(url, headers={"Range": f"bytes={start}-{start + zi.compress_size - 1}"},
                      stream=True, timeout=600) as r:
        r.raise_for_status()
        for b in r.iter_content(chunk):
            out = d.decompress(b)
            total += len(out)
            crc = zlib.crc32(out, crc)
            yield out
    out = d.flush()
    total += len(out)
    crc = zlib.crc32(out, crc)
    yield out
    if total != zi.file_size or crc != zi.CRC:
        raise RuntimeError(f"{member}: decompressed {total} bytes with CRC {crc:#x}, "
                           f"expected {zi.file_size} and {zi.CRC:#x}")


KEY = re.compile(rb'"((?:task[123]|unlabeled_videos)/[^"]+)"\s*:\s*\{')


def caltech_sequences(zip_name: str, member: str):
    """Yield (sequence key, raw JSON text of the sequence) for each sequence in a CalMS21 JSON member.

    A sequence's text runs from its opening brace to the next sequence key; parse it with
    `parse_sequence` (all fields) or `sequence_summary` (counts and annotations only, fast).
    """
    buf = b""
    current = None  # (key, offset of its opening brace in buf)
    for chunk in _member_bytes(zip_name, member):
        buf += chunk
        search_from = current[1] + 1 if current else 0
        while True:
            m = KEY.search(buf, search_from)
            if not m:
                break
            if current is not None:
                yield current[0], buf[current[1]:m.start()]
            current = (m.group(1).decode(), m.end() - 1)
            buf = buf[current[1]:]
            current = (current[0], 0)
            search_from = 1
        if current is None:
            buf = buf[-300:]
    if current is not None:
        yield current[0], buf[current[1]:]


CALMS21_FILES = {  # (zip, member) of the pose and annotation files of each set
    ("task1", "train"): ("task1_classic_classification.zip", "task1_classic_classification/calms21_task1_train.json"),
    ("task1", "test"): ("task1_classic_classification.zip", "task1_classic_classification/calms21_task1_test.json"),
    ("task2", "train"): ("task2_annotation_styles.zip", "task2_annotation_styles/calms21_task2_train.json"),
    ("task2", "test"): ("task2_annotation_styles.zip", "task2_annotation_styles/calms21_task2_test.json"),
    ("task3", "train"): ("task3_new_behaviors.zip", "task3_new_behaviors/calms21_task3_train.json"),
    ("task3", "test"): ("task3_new_behaviors.zip", "task3_new_behaviors/calms21_task3_test.json"),
    **{("unlabeled", f"part{i}"): ("unlabeled_videos.zip", f"unlabeled_videos/calms21_unlabeled_videos_part{i}.json")
       for i in range(1, 5)},
}


def run_lengths(mask: np.ndarray) -> np.ndarray:
    """Lengths (frames) of the runs of True in a boolean array."""
    m = np.concatenate([[False], mask.astype(bool), [False]])
    edges = np.flatnonzero(np.diff(m.astype(int)))
    return edges[1::2] - edges[0::2]


def set_summary(task: str, split: str) -> pd.DataFrame:
    """One row per sequence of a CalMS21 set: frames, frames per annotation code, the runs of each
    code, the vocabulary and annotator, and a hash of the keypoints (to find sequences deposited
    more than once)."""
    zip_name, member = CALMS21_FILES[(task, split)]
    rows = []
    for key, text in caltech_sequences(zip_name, member):
        s = sequence_summary(text)
        row = {"task": task, "split": split, "key": key, "n_frames": s["n_frames"],
               "n_frames_keypoints": s["n_frames_keypoints"], "kp_hash": s["keypoints_sha1"]}
        a = s["annotations"]
        if a is not None:
            row["n_annotations"] = len(a)
            codes, counts = np.unique(a, return_counts=True)
            row["counts"] = dict(zip(codes.tolist(), counts.tolist()))
            row["runs"] = {int(c): run_lengths(a == c).tolist() for c in codes}
        if s["metadata"] is not None:
            row["vocab"] = s["metadata"].get("vocab")
            row["annotator"] = s["metadata"].get("annotator-id", s["metadata"].get("annotator_id"))
        rows.append(row)
    return pd.DataFrame(rows)


def caltech_sequence(task: str, split: str, name: str) -> dict:
    """One sequence of a CalMS21 set, fully parsed, found by the end of its key."""
    zip_name, member = CALMS21_FILES[(task, split)]
    for key, text in caltech_sequences(zip_name, member):
        if key.endswith(name):
            obj = parse_sequence(text)
            obj["key"] = key
            return obj
    raise KeyError(name)


def parse_sequence(text: bytes) -> dict:
    obj, _ = json.JSONDecoder().raw_decode(text.decode())
    return obj


def sequence_summary(text: bytes) -> dict:
    """Frame count, annotations and metadata of a sequence, without parsing its keypoints.

    Frames are counted in the `scores` field, where each frame is [[7 scores], [7 scores]]: with
    whitespace removed, each frame ends with one "]]" (the last frame's "]]]" holds one
    non-overlapping "]]"). They are counted again in the `keypoints` field, where each frame is
    [[[7 x], [7 y]], [[7 x], [7 y]]] and ends with one "]]]" (the last frame's "]]]]" holds one). `keypoints_sha1` is a hash of the whole keypoints field without
    whitespace, used to find sequences deposited more than once; `keypoints_head` is its start.
    """
    dec = json.JSONDecoder()
    pos = {f: text.find(b'"%s"' % f.encode()) for f in ("keypoints", "scores", "annotations", "metadata")}
    if pos["scores"] < 0:
        raise ValueError("no scores field")

    def field(name):
        start = pos[name]
        later = [p for p in pos.values() if p > start]
        return text[start:min(later)] if later else text[start:]

    out = {"n_frames": field("scores").translate(None, b" \n\r\t").count(b"]]"),
           "n_frames_keypoints": None, "annotations": None, "metadata": None, "keypoints_head": None,
           "keypoints_sha1": None}
    if pos["annotations"] >= 0:
        a = field("annotations").translate(None, b" \n\r\t")
        out["annotations"] = np.array(dec.raw_decode(a[a.index(b"["):].decode())[0])
    if pos["metadata"] >= 0:
        m = field("metadata")
        out["metadata"] = dec.raw_decode(m[m.index(b"{"):].decode())[0]
    if pos["keypoints"] >= 0:
        k = field("keypoints").translate(None, b" \n\r\t")
        out["n_frames_keypoints"] = k.count(b"]]]")
        out["keypoints_head"] = k[:3000]
        out["keypoints_sha1"] = hashlib.sha1(k).hexdigest()
    return out
