"""Loading and measures for the optical membrane potential recordings of Semenov, Kim,
Silkuniene and Pakhomov (2025), Cell Reports Physical Science 6, 102660, on dandiset 001271
(Figure S2, tetrodotoxin and vehicle controls). The same loading and measures serve dandisets
001030, 001032 to 001035 and 001272 of the paper, whose files have the same layout.

Each NWB file of the dandiset is one imaging session: an ImageSeries of 1,200 frames of 16 x 16
pixels at 3,086.4 frames/s, with the stimulus voltage and the solution given only in the free-text
session description. The files are streamed from the DANDI archive at the pinned version; nothing
is written to disk.

Where each parameter comes from:

- F, F0 and dF = 100 (F - F0) / F0, with F the mean emission over the soma per frame: Methods,
  "Recording of the optical APs and data analyses" (claims file header, F1). Traces are not
  filtered (F2).
- Stimulus onset at 50 ms and duration 250 ms: Methods ("The standard imaging protocol started 50
  ms before sine wave stimulation and continued for 250 ms during"), claims file F3. The notebook
  checks the onset and offset against the aliased stimulus in the images.
- Frames 0 and 1199 are left out: the first frame of every file is about three times brighter than
  the rest and the last about 5% brighter (camera read-out artefacts, shown in the notebook's data
  check). This is a choice of this attempt, recorded as a deviation; the paper says nothing of them.
- Soma ROI readings (claims file, O1): (a) the connected component nearest the image centre of an
  Otsu threshold of the mean pre-stimulus frame, (b) that mask eroded by 2 pixels. Otsu and 2
  pixels are the claims file's standard choices. The whole frame is computed as a variant only
  (a choice of this attempt, since the 16 x 16 crop is filled by the soma).
- F0 readings (O2): (a) all frames before the onset, (b) the last 20 ms before the onset.
- AP detection (O3): a local maximum of dF with width at half height between 2 and 20 ms and at
  least 5 ms from a larger maximum (claims file, standard choices). Height above (a) 5% dF, or (b)
  5 SD of dF before the onset. The width is measured at half the peak's prominence
  (scipy.signal.peak_widths, rel_height 0.5), a standard choice for "width at half height".
  After the solution change the 5-SD level is the median of the neuron's sessions before the
  change (claims file, O3).
- Sustained depolarization (O4): no AP in the last 100 ms of the stimulus and the mean dF over
  that window above (a) 5 SD of dF before the onset, (b) half the median AP height of the neuron
  before the change. The 100-ms window is the claims file's standard choice. After the change
  the 5-SD level of (a) is the neuron's level before the change, as O3 has it for APs (an
  extension of O3 to O4 made by this attempt, recorded as a deviation).
- The maximum firing rate is the inverse of the interval between the first two APs (Methods; F5).
- The solution change of a vehicle neuron, which the files do not mark, is placed at the last gap
  of more than 3 minutes between its sessions (an assumption of this attempt: the sessions are
  20 to 60 s apart in the Methods, and the TTX neurons' gaps before their first TTX session are
  3.6 to 10.0 minutes). For TTX neurons the change is the first session labelled with TTX.
"""

import hashlib
import json
import re
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor

from pathlib import Path

import h5py
import numpy as np
import pandas as pd
import remfile
import yaml
from scipy import ndimage, signal

DANDISET_ID = "001271"
DANDISET_VERSION = "0.250805.1352"
API = "https://api.dandiarchive.org/api"
# Other dandisets of the paper used by claims with data elsewhere, each at its pinned version.
OTHER_DANDISETS = {"001030": "0.240520.1924", "001032": "0.240527.1432", "001033": "0.240527.1432",
                   "001034": "0.240527.1431", "001035": "0.240527.1432", "001272": "0.250805.1358"}

ONSET_S = 0.050      # Methods, F3
STIM_S = 0.250       # Figure S2 legend, F3
N_FRAMES = 1200
LAST_WINDOW_S = 0.100  # O4, the last 100 ms of the stimulus
CHANGE_GAP_MIN = 3.0   # assumption, see the module docstring
CLAIMS_FILE = Path(__file__).resolve().parents[2] / "claims" / "001271" / "10.1016-j.xcrp.2025.102660.yaml"


def show_claim(claim_id=None):
    """Print a claim's statement and criterion from the claims file this entry tests, or with no
    id the header's fixed details and readings, so that each test can be read beside its criterion."""
    if not CLAIMS_FILE.is_file():
        print(f"claims file not found at {CLAIMS_FILE}")
        return
    text = CLAIMS_FILE.read_text()
    if claim_id is None:
        head = [l[2:] for l in text.splitlines() if l.startswith("#")]
        start = next(i for i, l in enumerate(head) if l.startswith("Method details fixed"))
        print(f"{CLAIMS_FILE.parent.name}/{CLAIMS_FILE.name}, header:")
        print("\n".join(head[start:]))
        return
    claim = {c["id"]: c for c in yaml.safe_load(text)["claims"]}[claim_id]
    print(f"{CLAIMS_FILE.parent.name}/{CLAIMS_FILE.name}, {claim_id}")
    for key in ("statement", "expected", "criterion", "where"):
        if key in claim:
            print(f"\n{key}: {claim[key]}")


def list_assets(dandiset=DANDISET_ID, version=DANDISET_VERSION):
    url = f"{API}/dandisets/{dandiset}/versions/{version}/assets/?page_size=1000"
    out = []
    while url:
        with urllib.request.urlopen(url) as r:
            page = json.load(r)
        out += page["results"]
        url = page.get("next")
    return out


def dandiset_metadata(dandiset=DANDISET_ID, version=DANDISET_VERSION):
    with urllib.request.urlopen(f"{API}/dandisets/{dandiset}/versions/{version}/") as r:
        return json.load(r)


def _open(asset_id):
    return h5py.File(remfile.File(f"{API}/assets/{asset_id}/download/"), "r")


def parse_series_description(desc):
    """Stimulus of a session of dandisets 001032 to 001035, from its free-text description:
    'sine' or 'spindle' (sine modulated at 20 Hz) or 'sham', carrier frequency (kHz) and the
    stated peak-to-peak voltage."""
    kind = "spindle" if "spindle" in desc else ("sham" if "sham" in desc else "sine")
    m = re.search(r"applied at ([\d.]+) ?(k?Hz) using ([\d.]+) ?V", desc)
    if not m:
        return dict(kind=kind, khz=0.0, volt=0.0, sham=True, solution="NaCl", vcm_per_volt_file=np.nan)
    hz = float(m.group(1)) * (1000 if m.group(2) == "kHz" else 1)
    vcm = re.search(r"1V translates into ([\d.]+) V/cm", desc)
    return dict(kind=kind, khz=hz / 1000, volt=float(m.group(3)), sham=kind == "sham",
                solution="NaCl" if "140 NaCl" in desc else "other",
                vcm_per_volt_file=float(vcm.group(1)) if vcm else np.nan)


def parse_description(desc):
    """Voltage (V), frequency and solution from the free-text session description."""
    m = re.search(r"with ([\d.]+) ?V amplitude", desc)
    sham = "sham" in desc
    volt = 0.0 if sham else float(m.group(1))
    if "presence of the sodium channel inhibitor" in desc:
        solution = "TTX"
    elif "without tetrodotoxin" in desc:
        solution = "no TTX"
    else:
        solution = "unknown"
    fm = re.search(r"at ([\d.]+) ?kHz", desc)
    vcm = re.search(r"1V translates to ([\d.]+) V/cm", desc)
    return dict(volt=volt, sham=sham, solution=solution,
                khz=float(fm.group(1)) if fm else 0.0,
                vcm_per_volt_file=float(vcm.group(1)) if vcm else np.nan)


def read_session(asset, retries=3, parser=None):
    """Stream one file; return its metadata and its frames (uint16, frames x 16 x 16)."""
    parser = parser or parse_description
    for k in range(retries):
        try:
            f = _open(asset["asset_id"])
            ts = f["acquisition/TimeLapseImaging"]
            data = ts["data"][:]
            def text(key):
                return f[key][()].decode() if key in f else None
            meta = dict(
                path=asset["path"],
                subject=text("general/subject/subject_id"),
                session_id=text("general/session_id"),
                start=pd.Timestamp(text("session_start_time")),
                description=text("session_description"),
                series_description=ts.attrs.get("description"),
                rate=float(ts["starting_time"].attrs["rate"]),
                starting_time=float(ts["starting_time"][()]),
                unit=ts["data"].attrs.get("unit"),
                age=text("general/subject/age"),
                species=text("general/subject/species"),
                shape=data.shape,
                sha1=hashlib.sha1(data.tobytes()).hexdigest(),
            )
            meta.update(parser(meta["description"]))
            return meta, data
        except Exception as e:  # network errors: retry
            err = e
            time.sleep(2 * (k + 1))
    raise err


def otsu(x):
    """Otsu threshold of the values in x (256 bins)."""
    hist, edges = np.histogram(x.ravel(), bins=256)
    mids = (edges[:-1] + edges[1:]) / 2
    w0 = np.cumsum(hist)
    w1 = w0[-1] - w0
    m0 = np.cumsum(hist * mids)
    mu0 = m0 / np.maximum(w0, 1)
    mu1 = (m0[-1] - m0) / np.maximum(w1, 1)
    between = w0 * w1 * (mu0 - mu1) ** 2
    return mids[np.argmax(between)]


def soma_masks(mean_frame):
    """ROI readings of O1: 'otsu' (a), 'otsu_eroded' (b), and 'frame' (variant)."""
    fg = mean_frame > otsu(mean_frame)
    lab, n = ndimage.label(fg)
    cy, cx = (np.array(mean_frame.shape) - 1) / 2
    yy, xx = np.indices(mean_frame.shape)
    d = np.hypot(yy - cy, xx - cx)
    best = min(range(1, n + 1), key=lambda i: d[lab == i].min())
    a = lab == best
    b = ndimage.binary_erosion(a, iterations=2)
    return {"otsu": a, "otsu_eroded": b, "frame": np.ones_like(a)}


def frames(rate):
    onset = int(round(ONSET_S * rate))
    offset = int(round((ONSET_S + STIM_S) * rate))
    return onset, offset


def session_traces(meta, data):
    """Raw F traces (frames 1 to 1198) for each ROI reading, from the session's own frames."""
    onset, _ = frames(meta["rate"])
    d = data.astype(float)
    mean_pre = d[1:onset].mean(0)
    masks = soma_masks(mean_pre)
    out = {}
    for k, m in masks.items():
        tr = d[:, m].mean(1) if m.any() else np.full(len(d), np.nan)
        tr[0] = np.nan      # first-frame artefact
        tr[-1] = np.nan     # last-frame artefact
        out[k] = tr
    return out, {k: int(m.sum()) for k, m in masks.items()}, mean_pre


def dff(trace, rate, f0_reading):
    """dF in percent under F0 reading (a) 'all' frames before onset or (b) 'last20' ms."""
    onset, _ = frames(rate)
    if f0_reading == "all":
        lo = 1
    else:
        lo = onset - int(round(0.020 * rate))
    f0 = np.nanmean(trace[lo:onset])
    return 100 * (trace - f0) / f0, lo


def detect_aps(x, rate, height, t0, t1):
    """APs (O3) in dF trace x between frames t0 and t1 (exclusive), height level in % dF.

    Local maxima at least 5 ms from a larger maximum, with width at half prominence of 2 to
    20 ms. Returns a DataFrame with frame, peak dF, width (ms) and prominence."""
    y = np.nan_to_num(x, nan=np.nanmedian(x))
    dist = int(round(0.005 * rate))
    pk, props = signal.find_peaks(y, distance=dist, height=height)
    if len(pk) == 0:
        return pd.DataFrame(columns=["frame", "peak", "width_ms", "prominence"])
    w, wh, lips, rips = signal.peak_widths(y, pk, rel_height=0.5)
    width_ms = w / rate * 1000
    keep = (width_ms >= 2) & (width_ms <= 20) & (pk >= t0) & (pk < t1)
    prom = signal.peak_prominences(y, pk)[0]
    return pd.DataFrame(dict(frame=pk[keep], peak=y[pk[keep]], width_ms=width_ms[keep],
                             prominence=prom[keep]))


def duration_to_f0(x, rate, pk, max_back_ms=20, max_fwd_ms=30):
    """AP duration reading (b) of ap-amplitude-duration: from the last frame at or below F0
    (dF <= 0) before the peak to the first frame at or below F0 after it, so the
    afterhyperpolarization is left out. Searches 20 ms back and 30 ms forward (standard choices);
    NaN when dF does not reach F0 within them."""
    back = int(round(max_back_ms / 1000 * rate))
    fwd = int(round(max_fwd_ms / 1000 * rate))
    seg_b = x[max(pk - back, 0):pk + 1]
    seg_f = x[pk:pk + fwd + 1]
    ib = np.where(seg_b <= 0)[0]
    jf = np.where(seg_f <= 0)[0]
    if len(ib) == 0 or len(jf) == 0:
        return np.nan
    start = max(pk - back, 0) + ib[-1]
    end = pk + jf[0]
    return (end - start) / rate * 1000


def load_all(assets, workers=16, parser=None):
    """Stream every file, reduce each to its ROI traces, and return a session table and traces."""
    def one(a):
        meta, data = read_session(a, parser=parser)
        tr, npx, mean_pre = session_traces(meta, data)
        meta["n_pixels"] = npx
        meta["frame_means"] = (float(data[0].mean()), float(data[1:-1].mean()),
                               float(data[-1].mean()), float(data[-2].mean()))
        meta["mean_pre"] = mean_pre
        meta["alias"] = alias_envelope(data, meta["rate"], meta["khz"] or 2.0)
        return meta, tr
    with ThreadPoolExecutor(workers) as ex:
        res = list(ex.map(one, assets))
    sessions = pd.DataFrame([m for m, _ in res])
    traces = [t for _, t in res]
    sessions["trace_index"] = range(len(sessions))
    return sessions, traces


def assign_change(sessions):
    """Order sessions per neuron and mark them before or after the solution change."""
    s = sessions.sort_values(["subject", "start"]).copy()
    s["order"] = s.groupby("subject").cumcount()
    s["gap_min"] = s.groupby("subject")["start"].diff().dt.total_seconds() / 60
    phase, group = [], {}
    for subj, g in s.groupby("subject", sort=False):
        if (g["solution"] == "TTX").any():
            group[subj] = "TTX"
            first = g.loc[g["solution"] == "TTX", "start"].min()
            phase += list(np.where(g["start"] >= first, "after", "before"))
        else:
            big = g.index[g["gap_min"] > CHANGE_GAP_MIN]
            if len(big):
                group[subj] = "vehicle"
                first = g.loc[big[-1], "start"]
                phase += list(np.where(g["start"] >= first, "after", "before"))
            else:
                group[subj] = "no change"
                phase += ["before"] * len(g)
    s["phase"] = phase
    s["group"] = s["subject"].map(group)
    return s


READINGS = dict(roi=("otsu", "otsu_eroded"), f0=("all", "last20"), ap=("5pct", "5sd"),
                sd=("5sd", "half_ap"))


def measure(sessions, traces, roi, f0r, apr, sdr, invert=False):
    """Per-session measures under one combination of the O1 to O4 readings.

    Returns one row per session: pre-onset SD of dF, the level used for APs, the APs during the
    stimulus (frames, peaks, widths), the mean dF over the last 100 ms of the stimulus, whether
    an AP falls in that window, the sustained depolarization flag and its level. With invert, dF
    is multiplied by -1 before anything is measured (Di-8-ANEPPS, whose emission falls with
    depolarization; Methods and the Figure S1 legend)."""
    rows = []
    for _, s in sessions.iterrows():
        rate = s["rate"]
        onset, offset = frames(rate)
        x, lo = dff(traces[s["trace_index"]][roi], rate, f0r)
        if invert:
            x = -x
        pre_sd = float(np.nanstd(x[lo:onset], ddof=1))
        rows.append(dict(path=s["path"], x=x, pre_sd=pre_sd, onset=onset, offset=offset))
    m = pd.DataFrame(rows).set_index("path")
    s = sessions.set_index("path").join(m)
    # levels from the neuron's sessions before the change (O3, extended to O4(a))
    before_sd = s[s["phase"] == "before"].groupby("subject")["pre_sd"].median()
    s["sd_level"] = np.where(s["phase"] == "before", s["pre_sd"], s["subject"].map(before_sd))
    s["ap_level"] = 5.0 if apr == "5pct" else 5 * s["sd_level"]
    aps = {}
    for p, r in s.iterrows():
        aps[p] = detect_aps(r["x"], r["rate"], r["ap_level"], r["onset"], r["offset"])
    s["n_ap"] = [len(aps[p]) for p in s.index]
    s["ap_frames"] = [aps[p]["frame"].to_numpy() for p in s.index]
    s["ap_peaks"] = [aps[p]["peak"].to_numpy() for p in s.index]
    s["ap_widths"] = [aps[p]["width_ms"].to_numpy() for p in s.index]
    s["max_rate_hz"] = [r["rate"] / np.diff(f[:2])[0] if len(f) >= 2 else np.nan
                        for f, (_, r) in zip(s["ap_frames"], s.iterrows())]
    s["first_ap_ms"] = [(f[0] - r["onset"]) / r["rate"] * 1000 if len(f) else np.nan
                        for f, (_, r) in zip(s["ap_frames"], s.iterrows())]
    win0 = (s["offset"] - (LAST_WINDOW_S * s["rate"]).round()).astype(int)
    s["last100_mean"] = [float(np.nanmean(r["x"][w0:r["offset"]])) for w0, (_, r) in zip(win0, s.iterrows())]
    s["ap_in_last100"] = [bool(((f >= w0) & (f < r["offset"])).any())
                          for f, w0, (_, r) in zip(s["ap_frames"], win0, s.iterrows())]
    before_heights = {}
    for subj, g in s[s["phase"] == "before"].groupby("subject"):
        h = np.concatenate(list(g["ap_peaks"])) if len(g) else np.array([])
        before_heights[subj] = float(np.median(h)) if len(h) else np.nan
    if sdr == "5sd":
        s["sd_dep_level"] = 5 * s["sd_level"]
    else:
        s["sd_dep_level"] = 0.5 * s["subject"].map(before_heights)
    s["sustained"] = (~s["ap_in_last100"]) & (s["last100_mean"] > s["sd_dep_level"])
    s["readings"] = f"{roi}/{f0r}/{apr}/{sdr}"
    return s.reset_index()


def all_combinations(sessions, traces, invert=False):
    """measure() under every combination of the O1 to O4 readings, concatenated."""
    out = []
    for roi in READINGS["roi"]:
        for f0r in READINGS["f0"]:
            for apr in READINGS["ap"]:
                for sdr in READINGS["sd"]:
                    m = measure(sessions, traces, roi, f0r, apr, sdr, invert=invert)
                    m["roi"], m["f0"], m["ap"], m["sdr"] = roi, f0r, apr, sdr
                    out.append(m)
    return pd.concat(out, ignore_index=True)


def pairs(m, group, o5):
    """Session pairs at the same voltage before and after the change, per neuron of a group.

    O5 readings: 'every' voltage tested both before and after, or only the 'highest' such.
    Where a voltage was tested more than once in a phase, APs count when any session has them
    and sustained depolarization when any session shows it."""
    rows = []
    for subj, h in m[m["group"] == group].groupby("subject"):
        b, a = h[h["phase"] == "before"], h[h["phase"] == "after"]
        common = sorted(set(b["volt"]) & set(a["volt"]))
        if o5 == "highest" and common:
            common = [max(common)]
        for v in common:
            bb, aa = b[b["volt"] == v], a[a["volt"] == v]
            rows.append(dict(subject=subj, volt=v,
                             ap_before=int(bb["n_ap"].max()), ap_after=int(aa["n_ap"].max()),
                             sd_before=bool(bb["sustained"].any()), sd_after=bool(aa["sustained"].any()),
                             last100_before=float(bb["last100_mean"].mean()),
                             last100_after=float(aa["last100_mean"].mean()),
                             level_after=float(aa["sd_dep_level"].mean())))
    return pd.DataFrame(rows, columns=["subject", "volt", "ap_before", "ap_after", "sd_before",
                                       "sd_after", "last100_before", "last100_after", "level_after"])


def alias_envelope(data, rate, khz=2.0):
    """Amplitude of the aliased stimulus in the images, per frame (mean over pixels).

    A sine of frequency f sampled at the frame rate appears at |f - k rate|, k the nearest integer
    (1,086.4 Hz for 2 kHz at 3,086.4 frames/s). Each pixel
    is high-passed (minus a 5-frame running mean), demodulated at that frequency and smoothed over
    31 frames (10 ms). Used only to check the stimulus timing."""
    f = khz * 1000
    f_alias = abs(f - round(f / rate) * rate)
    d = data.astype(float).reshape(len(data), -1)
    d[0] = d[1]
    k5 = np.ones(5) / 5
    hp = d - ndimage.convolve1d(d, k5, axis=0, mode="nearest")
    z = hp * np.exp(-2j * np.pi * f_alias * np.arange(len(d)) / rate)[:, None]
    zr = ndimage.uniform_filter1d(z.real, 31, axis=0)
    zi = ndimage.uniform_filter1d(z.imag, 31, axis=0)
    return np.abs(zr + 1j * zi).mean(1)
