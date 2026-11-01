"""Loading and measures for the optical membrane potential recordings of Semenov et al. (2025).

Semenov, Kim, Silkuniene & Pakhomov (2025), "Excitation and polarization of isolated neurons by
high-frequency sine waves for temporal interference stimulation", Cell Rep. Phys. Sci. 6, 102660,
doi:10.1016/j.xcrp.2025.102660. The claims file is claims/001272/10.1016-j.xcrp.2025.102660.yaml;
its header items (F1 to F6, O1 to O6) are cited below by their labels.

Every file is one imaging session: an ImageSeries of 16 x 16 pixel frames of the soma at about
3,086 frames/s. The stimulus is described only in the file's session_description (frequency,
amplitude in volts, modulation, tetrodotoxin), which is parsed here.

Where each parameter comes from:

- DANDISETS: the published versions pinned. 001272 is the target; the others are the paper's
  other deposits (Data and code availability), used for the `with_inputs` and `elsewhere` claims.
- V_TO_V_PER_CM = 36: the files' own conversion ("1V translates to 36 V/cm at the location of
  neurons").
- ONSET_MS = 50, STIM_MS = 250: F3 of the claims file (Methods, "The standard imaging protocol
  started 50 ms before sine wave stimulation and continued for 250 ms during"); the 001032 to
  001035 files say the same ("Exposure was triggered 50 ms after the start of fluorescence
  time-lapse recording").
- Frame 0 and the last frame are left out of every trace. In nearly every file they are far
  brighter than the rest (a camera artefact, shown in the data check). Standard choice; leaving
  them in would only distort F0 and the last sample.
- roi_masks: reading O1 (a) the connected component nearest the image centre of an Otsu threshold
  of the mean pre-stimulus frame, (b) the same eroded by 2 pixels. Otsu and the 2 pixels are the
  claims file's standard choices. The whole 16 x 16 frame is offered as a variant only.
- dff: F1, dF = 100 (F - F0) / F0, F0 under O2 (a) all frames before the onset, (b) the last
  20 ms before it. No filtering or detrending (F2). `invert` gives -dF for Di-8-ANEPPS (F1).
- detect_aps: O3. A local maximum with width at half prominence of 1 to 20 ms, at least 5 ms from
  a larger maximum; height (the dF value at the peak, as the Methods' "APs peaked at a more than
  5% dF") above (a) 5% or (b) 5 SD of the trace before the onset. The claims file sets the 1-ms
  lower bound to exclude single-frame noise (about 3 frames at 3,086.4 or 3,130 frames/s), since the
  Methods' "lasted about 10 ms" is the whole AP duration and bounds the half-height width from above
  only; the 20-ms upper bound and the 5 ms are its standard choices. Its earlier 2-ms lower bound is
  run as a variant.
- sustained_firing, sustained_depolarization: O6 (standard choices of the claims file).
- first_two_rate: F5, inverse of the interval between the first two APs.
"""

from __future__ import annotations

import hashlib
import json
import re
import urllib.request
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import remfile
from scipy import ndimage, signal

DANDISETS = {
    "001272": "0.250805.1358",
    "001030": "0.240520.1924",
    "001032": "0.240527.1432",
    "001033": "0.240527.1432",
    "001034": "0.240527.1431",
    "001035": "0.240527.1432",
    "001271": "0.250805.1352",
}
API = "https://api.dandiarchive.org/api"
V_TO_V_PER_CM = 36.0
ONSET_MS = 50.0
STIM_MS = 250.0


def list_assets(dandiset: str) -> list[dict]:
    """Every asset of the pinned version: path, size and S3 address of its blob."""
    version = DANDISETS[dandiset]
    url = f"{API}/dandisets/{dandiset}/versions/{version}/assets/?page_size=200"
    out = []
    while url:
        page = json.load(urllib.request.urlopen(url))
        for a in page["results"]:
            b = a["blob"]
            out.append(dict(path=a["path"], size=a["size"], asset_id=a["asset_id"], blob=b,
                            url=f"https://dandiarchive.s3.amazonaws.com/blobs/{b[:3]}/{b[3:6]}/{b}"))
        url = page["next"]
    return sorted(out, key=lambda a: a["path"])


def parse_description(desc: str) -> dict:
    """Stimulus parameters from a session_description."""
    freq = re.search(r"(?:applied at|sine wave at) ([\d.]+) ?(k?Hz)", desc)
    amp = re.search(r"([\d.]+) ?V (?:\(peak-to-peak\) )?amplitude", desc) or \
        re.search(r"under ([\d.,]+)V amplitude", desc)
    hz = None
    if freq:
        hz = float(freq.group(1)) * (1000 if freq.group(2) == "kHz" else 1)
    volts = float(amp.group(1).replace(",", ".")) if amp else None
    return dict(
        freq_hz=hz,
        volts=volts,
        field=None if volts is None else volts * V_TO_V_PER_CM,
        modulated="spindle" in desc or "modulated at" in desc,
        sham="sham" in desc,
        ttx="presence of the sodium channel inhibitor" in desc,
        peak_to_peak="peak-to-peak) amplitude" in desc,
        nagluconate="NaGluconate" in desc,
    )


def read_session(asset: dict) -> dict:
    """Stream one file and return its frames and metadata."""
    with h5py.File(remfile.File(asset["url"]), "r") as f:
        ts = f["acquisition/TimeLapseImaging"]
        data = ts["data"][:]
        desc = f["session_description"][()].decode()
        rec = dict(
            path=asset["path"],
            subject=f["general/subject/subject_id"][()].decode(),
            start=f["session_start_time"][()].decode(),
            rate=float(ts["starting_time"].attrs["rate"]),
            description=desc,
            data=data,
        )
    rec.update(parse_description(desc))
    return rec


def read_sessions(assets: list[dict], workers: int = 8) -> list[dict]:
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(read_session, assets))


def frames(rec: dict) -> tuple[np.ndarray, np.ndarray]:
    """The frames used (frame 0 and the last frame left out) and their times in ms from the start."""
    d = rec["data"][1:-1].astype(float)
    t = np.arange(1, rec["data"].shape[0] - 1) / rec["rate"] * 1000.0
    return d, t


def onset_index(t: np.ndarray, onset_ms: float = ONSET_MS) -> int:
    """Index in `t` of the first frame at or after the stimulus onset (F3)."""
    return int(np.searchsorted(t, onset_ms))


def otsu_threshold(x: np.ndarray, bins: int = 256) -> float:
    hist, edges = np.histogram(x, bins=bins)
    mids = (edges[:-1] + edges[1:]) / 2
    w0 = np.cumsum(hist)
    w1 = w0[-1] - w0
    m0 = np.cumsum(hist * mids) / np.maximum(w0, 1)
    m1 = (np.sum(hist * mids) - np.cumsum(hist * mids)) / np.maximum(w1, 1)
    between = w0 * w1 * (m0 - m1) ** 2
    return float(mids[np.argmax(between[:-1])])


def roi_masks(mean_image: np.ndarray) -> dict[str, np.ndarray]:
    """O1 readings (a) Otsu component nearest the centre, (b) the same eroded by 2 pixels.

    When the erosion leaves nothing, (b) falls back to (a); `roi_report` says how often."""
    thr = otsu_threshold(mean_image)
    lab, n = ndimage.label(mean_image > thr)
    cy, cx = (np.array(mean_image.shape) - 1) / 2
    best, bestd = 0, np.inf
    for k in range(1, n + 1):
        yy, xx = np.nonzero(lab == k)
        dist = np.min(np.hypot(yy - cy, xx - cx))
        if dist < bestd:
            best, bestd = k, dist
    a = lab == best
    b = ndimage.binary_erosion(a, iterations=2)
    if b.sum() == 0:
        b = a.copy()
    return {"a": a, "b": b, "whole": np.ones_like(a, dtype=bool)}


def soma_trace(d: np.ndarray, mask: np.ndarray) -> np.ndarray:
    return d[:, mask].mean(axis=1)


def dff(trace: np.ndarray, t: np.ndarray, f0: str = "a", invert: bool = False,
        onset_ms: float = ONSET_MS) -> np.ndarray:
    """F1 with the O2 readings for F0: (a) all frames before the onset, (b) the last 20 ms."""
    i0 = onset_index(t, onset_ms)
    pre = trace[:i0] if f0 == "a" else trace[(t >= onset_ms - 20) & (t < onset_ms)]
    y = 100.0 * (trace - pre.mean()) / pre.mean()
    return -y if invert else y


def detect_aps(y: np.ndarray, t: np.ndarray, height: str = "a", stim_ms: float = STIM_MS,
               onset_ms: float = ONSET_MS, min_width_ms: float = 1.0, height_ref: str = "value") -> dict:
    """O3: APs as local maxima of the (inverted for Di-8-ANEPPS) dF trace.

    Returns peak times (ms from the onset), heights (dF at the peak), widths (ms) and the height
    threshold used, for peaks during the stimulus. `min_width_ms` is 1 ms (O3); 2 ms, the claims
    file's earlier bound, is run as a variant (FluoVolt APs are about 2 ms wide at half height).
    `height_ref` "value" compares the dF at the peak with the threshold (the Methods' "APs peaked at
    a more than 5% dF"); "prominence", a variant, compares the peak's prominence, which does not
    count a depolarized baseline towards the height."""
    dt = float(np.median(np.diff(t)))
    pre = y[t < onset_ms]
    thr = 5.0 if height == "a" else 5.0 * float(np.std(pre))
    hk = {"height": thr} if height_ref == "value" else {"prominence": thr}
    peaks, props = signal.find_peaks(y, distance=max(1, int(round(5.0 / dt))),
                                     width=(min_width_ms / dt, 20.0 / dt), rel_height=0.5, **hk)
    props["peak_heights"] = y[peaks]
    tp = t[peaks] - onset_ms
    keep = (tp >= 0) & (tp <= stim_ms)
    return dict(times=tp[keep], heights=props["peak_heights"][keep],
                widths=props["widths"][keep] * dt, threshold=thr, pre_sd=float(np.std(pre)))


def sustained_firing(aps: dict, stim_ms: float = STIM_MS) -> bool:
    """O6: at least three APs, one of them in the last 50 ms of the stimulus."""
    return len(aps["times"]) >= 3 and bool(np.any(aps["times"] >= stim_ms - 50))


def sustained_depolarization(y: np.ndarray, t: np.ndarray, aps: dict, level: float,
                             window_ms: float = 100.0, stim_ms: float = STIM_MS,
                             onset_ms: float = ONSET_MS) -> bool:
    """O6: no AP in the last `window_ms` of the stimulus while the mean dF there is above `level`."""
    w = (t >= onset_ms + stim_ms - window_ms) & (t < onset_ms + stim_ms)
    no_ap = not np.any(aps["times"] >= stim_ms - window_ms)
    return bool(no_ap and y[w].mean() > level)


def late_mean(y: np.ndarray, t: np.ndarray, window_ms: float = 100.0, stim_ms: float = STIM_MS,
              onset_ms: float = ONSET_MS) -> float:
    w = (t >= onset_ms + stim_ms - window_ms) & (t < onset_ms + stim_ms)
    return float(y[w].mean())


def first_two_rate(aps: dict) -> float:
    """F5: the inverse of the interval between the first two APs, in Hz (nan with fewer than two)."""
    if len(aps["times"]) < 2:
        return float("nan")
    return 1000.0 / float(aps["times"][1] - aps["times"][0])


READINGS = [(roi, f0, h) for roi in ("a", "b", "whole") for f0 in ("a", "b") for h in ("a", "b")]
"""Every combination of O1 (ROI a, b, and the whole deposited 16 x 16 frame), O2 (F0 a, b) and O3
(height a, b)."""


def prepare(rec: dict, onset_ms: float = ONSET_MS) -> dict:
    """Reduce a streamed session to its soma traces under each ROI reading; drops the frames."""
    d, t = frames(rec)
    i0 = onset_index(t, onset_ms)
    masks = roi_masks(d[:i0].mean(axis=0))
    out = {k: v for k, v in rec.items() if k != "data"}
    out["n_frames"] = rec["data"].shape[0]
    out["data_md5"] = hashlib.md5(rec["data"].tobytes()).hexdigest()
    out["frame0_ratio"] = float(rec["data"][0].mean() / np.median(d.mean(axis=(1, 2))))
    out["last_ratio"] = float(rec["data"][-1].mean() / np.median(d.mean(axis=(1, 2))))
    out["mean_intensity"] = float(d.mean())
    out["t"] = t
    out["traces"] = {k: soma_trace(d, m) for k, m in masks.items()}
    out["mask_px"] = {k: int(m.sum()) for k, m in masks.items()}
    out["eroded_empty"] = bool(ndimage.binary_erosion(masks["a"], iterations=2).sum() == 0)
    return out


def load_prepared(assets: list[dict], workers: int = 8, onset_ms: float = ONSET_MS) -> list[dict]:
    def one(a):
        return prepare(read_session(a), onset_ms)
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(one, assets))


def session_table(recs: list[dict], roi: str, f0: str, height: str, invert: bool,
                  onset_ms: float = ONSET_MS, stim_ms: float = STIM_MS, late_ms: float = 100.0,
                  baseline: dict | None = None, min_width_ms: float = 1.0, height_ref: str = "value"):
    """One row per session: AP count, first-AP latency, F5 rate, late mean dF and O6 measures.

    `late_ms` is the O6 window at the end of the stimulus. `baseline`, for the 2-s recordings of
    Figure 3C only, maps a session's path to a dF trace without APs that is subtracted from it
    (Methods, "corrected for bleaching by subtracting a trace without APs")."""
    import pandas as pd
    rows = []
    for r in recs:
        y = dff(r["traces"][roi], r["t"], f0, invert=invert, onset_ms=onset_ms)
        if baseline is not None and baseline.get(r["path"]) is not None:
            b = baseline[r["path"]]
            n = min(len(y), len(b))
            y = y[:n] - b[:n]
            tt = r["t"][:n]
        else:
            tt = r["t"]
        stim = min(stim_ms, float(tt[-1]) - onset_ms)
        ap = detect_aps(y, tt, height, stim_ms=stim, onset_ms=onset_ms, min_width_ms=min_width_ms,
                        height_ref=height_ref)
        rows.append(dict(
            subject=r["subject"], path=r["path"], start=r["start"], volts=r["volts"],
            field=r["field"], freq_hz=r["freq_hz"], modulated=r["modulated"], ttx=r["ttx"],
            sham=r["sham"], n_aps=len(ap["times"]),
            first_ms=float(ap["times"][0]) if len(ap["times"]) else np.nan,
            ap_times=ap["times"], ap_heights=ap["heights"],
            median_height=float(np.median(ap["heights"])) if len(ap["heights"]) else np.nan,
            pre_sd=ap["pre_sd"], threshold=ap["threshold"], stim_ms=stim,
            late_mean=late_mean(y, tt, window_ms=late_ms, stim_ms=stim, onset_ms=onset_ms),
            late_aps=int(np.sum(ap["times"] >= stim - late_ms)),
            sust_firing=sustained_firing(ap, stim_ms=stim),
            rate_hz=first_two_rate(ap),
        ))
    df = pd.DataFrame(rows)
    # O6 sustained depolarization, both levels: (a) 5 SD of the trace before the onset,
    # (b) half the neuron's median AP height (over all its APs).
    med = df.explode("ap_heights").groupby("subject")["ap_heights"].apply(
        lambda s: float(np.nanmedian(s.astype(float))) if s.notna().any() else np.nan)
    df["level_b"] = df["subject"].map(med) / 2
    df["sust_depol_a"] = (df["late_aps"] == 0) & (df["late_mean"] > 5 * df["pre_sd"])
    df["sust_depol_b"] = (df["late_aps"] == 0) & (df["late_mean"] > df["level_b"])
    return df


def thresholds(df, min_aps: int = 1, by=("subject",)):
    """F4: per neuron, the lowest field (and volts) of a session with at least `min_aps` APs."""
    import pandas as pd
    rows = []
    for key, g in df.groupby(list(by)):
        key = key if isinstance(key, tuple) else (key,)
        ex = g[g["n_aps"] >= min_aps]
        lower = g[g["field"] < ex["field"].min()]["field"] if len(ex) else g["field"]
        rows.append(dict(zip(by, key), threshold=ex["field"].min() if len(ex) else np.nan,
                         threshold_volts=ex["volts"].min() if len(ex) else np.nan,
                         next_lower=lower.max() if len(lower) else np.nan,
                         fields_tested=int(g["field"].nunique()), sessions=len(g)))
    return pd.DataFrame(rows)
