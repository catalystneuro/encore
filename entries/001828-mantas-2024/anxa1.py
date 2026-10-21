"""Loading and measures for dandiset 001828 (Mantas, Contestabile, Skara et al., bioRxiv 2024).

doi:10.1101/2024.12.22.629963. The dandiset holds the behaviour and fiber photometry of the paper:
open field sessions with DeepLabCut pose, kinematics and VAME motif labels (some with photometry),
optogenetically evoked dLight release, the water drop and forelimb reaching sessions with manually
annotated events (some with photometry), and arrow maze sessions with DeepLabCut pose. Files are
streamed from the archive at the pinned version with remfile and h5py; nothing is written to disk.

Kinds of file, as found in the data (the file names do not always say):

- open field (`load_oft`): every `*_behavior+image.nwb`. 84 of them are named `ses-tmaze-...`
  but their descriptions, contents and frame counts are those of open field sessions.
- evoked release (`load_opto`): the 20 `ses-oft-<date>.nwb` files without a suffix, with an
  `optogenetic_epochs` table.
- reaching and water drop (`load_reach`): `ses-reaching-test-...`.
- arrow maze (`load_maze`): `ses-tmaze-..._image.nwb`.

Groups, cohorts, days and test phases are stated only in the free text of `session_description`;
`parse_*` read them from it.

Where the parameters come from:

- Window edges, z-scoring readings, AUC windows, thresholds and tests are those of the claims file
  claims/001828/10.1101-2024.12.22.629963.yaml (which cites the paper); each function says which.
- Units are the files': `linear_velocity` is stored with conversion 0.01 to m/s, so the stored
  values are cm/s; `angular_velocity` is rad/s; pose is in pixels; reach distances are in cm.
- Standard choices that cannot change a result are named where they are made: the interpolation
  of photometry onto a regular grid around events, the 30 Hz frame grid of the open field.
"""

from __future__ import annotations

import json
import re
import urllib.request
from concurrent.futures import ProcessPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
from scipy import stats

DANDISET_ID = "001828"
DANDISET_VERSION = "0.261020.1002"
API = "https://api.dandiarchive.org/api"
FPS_OFT = 30.0          # open field and maze video, Methods and files
N_WORKERS = 16


# --- archive -------------------------------------------------------------------

def list_assets() -> pd.DataFrame:
    """Every asset of the pinned version: path, asset id, size in bytes."""
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/?page_size=1000"
    rows = []
    while url:
        page = json.load(urllib.request.urlopen(url))
        rows += [{"path": a["path"], "asset_id": a["asset_id"], "size": a["size"]} for a in page["results"]]
        url = page["next"]
    return pd.DataFrame(rows)


def version_metadata() -> dict:
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/"
    return json.load(urllib.request.urlopen(url))


def open_asset(asset_id: str) -> h5py.File:
    return h5py.File(remfile.File(f"{API}/assets/{asset_id}/download/"), "r")


def _s(x) -> str:
    return x.decode() if isinstance(x, bytes) else str(x)


def _subject(f) -> dict:
    g = f["general/subject"]
    return {"subject": _s(g["subject_id"][()]), "genotype": _s(g["genotype"][()]) if "genotype" in g else "",
            "sex": _s(g["sex"][()]), "start": _s(f["session_start_time"][()]),
            "session_id": _s(f["general/session_id"][()]) if "general/session_id" in f else "",
            "description": _s(f["session_description"][()]).replace("\n", " ")}


def _fp_meta(f) -> dict:
    loc = f.get("general/fiber_photometry/fiber_photometry_table/location")
    ind = f.get("general/fiber_photometry/fiber_photometry_indicators")
    return {"location": _s(loc[0]) if loc is not None else "", "indicator": ",".join(ind.keys()) if ind is not None else ""}


def load_many(fn, asset_ids, workers: int = N_WORKERS) -> list:
    """fn over many assets in parallel processes (h5py serialises threads, so threads do not help)."""
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(fn, asset_ids))


# --- open field ----------------------------------------------------------------

OFT_GROUPS = {   # (experiment, group in the description) -> the paper's name for the group
    ("oft_Tetx", "ctrl"): "Ctrl-Tdtomato", ("oft_Tetx", "Tetx"): "Anxa1-TeTx",
    ("oft_6OHDA", "asc_acid"): "Ctrl-Asc Acid", ("oft_6OHDA", "6OHDA"): "6OHDA-low",
    ("oft_mitopark_10-11weeks", "Ctrl 10-11 wks"): "Ctrl-early", ("oft_mitopark_10-11weeks", "KO 10-11 wks"): "MP-early",
    ("oft_mitopark_15-18weeks", "Ctrl 15-18 wks"): "Ctrl-middle", ("oft_mitopark_15-18weeks", "KO 15-18 wks"): "MP-middle",
    ("oft_fp", "anxa1-flp"): "Anxa1 GCaMP-dCP", ("oft_fp", "dat-cre"): "DAT GCaMP-dCP",
    ("oft_fp", "dLight_dStr"): "dLight-dCP", ("oft_fp", "dLight_vStr"): "dLight-cCP",
}
FIG5_GROUPS = ["Ctrl-Tdtomato", "Anxa1-TeTx", "Ctrl-Asc Acid", "6OHDA-low",
               "Ctrl-early", "MP-early", "Ctrl-middle", "MP-middle"]
FP_GROUPS = ["Anxa1 GCaMP-dCP", "DAT GCaMP-dCP", "dLight-dCP", "dLight-cCP"]
POSE6 = ["Snout", "Leftfrontpaw", "Rightfrontpaw", "Leftbackpaw", "Rightbackpaw", "Tailbase"]


def parse_oft(description: str) -> tuple[str, str]:
    m = re.match(r"From group '(.*?)' experiment '(.*?)'", description)
    return (m.group(2), m.group(1)) if m else ("", "")


def load_oft(asset_id: str) -> dict:
    """One open field file, reduced to kinematics, motif labels and (if present) photometry."""
    f = open_asset(asset_id)
    r = _subject(f)
    r["experiment"], r["group_raw"] = parse_oft(r["description"])
    r["group"] = OFT_GROUPS.get((r["experiment"], r["group_raw"]), "")
    k = "processing/behavior/Kinematics/"
    r["lin"] = f[k + "linear_velocity/data"][:]          # cm/s (conversion 0.01 to m/s)
    r["lin_unit"] = (_s(f[k + "linear_velocity/data"].attrs["unit"]), float(f[k + "linear_velocity/data"].attrs["conversion"]))
    r["ang"] = f[k + "angular_velocity/data"][:]         # rad/s
    r["acc"] = f[k + "linear_acceleration/data"][:]      # cm/s^2 (conversion 0.01 to m/s^2)
    r["dist"] = f[k + "distance_moved/data"][:]          # cm per frame
    r["kin_rate"] = float(f[k + "linear_velocity/starting_time"].attrs["rate"])
    r["kin_t0"] = float(f[k + "linear_velocity/starting_time"][()])
    r["motif"] = f["processing/behavior/VAME_42/MotifSeries/data"][:].astype(int)
    r["motif_t0"] = float(f["processing/behavior/VAME_42/MotifSeries/starting_time"][()])
    p = "processing/behavior/PoseEstimationDeepLabCut/PoseEstimationSeries"
    pose = np.stack([f[p + n + "/data"][:] for n in POSE6])          # (6, frames, 2), pixels
    r["n_pose"] = pose.shape[1]
    r["pose_step6"] = np.r_[np.nan, np.hypot(*np.diff(pose.mean(axis=0), axis=0).T)]   # px per frame
    r["pose_range"] = (float(np.nanmin(pose)), float(np.nanmax(pose)))
    r["fp"] = "processing/ophys/FiberPhotometrySeriesZScored" in f
    if r["fp"]:
        z = f["processing/ophys/FiberPhotometrySeriesZScored"]
        r["z"] = z["data"][:]
        r["z_t0"] = float(z["starting_time"][()])
        r["z_rate"] = float(z["starting_time"].attrs["rate"])
        d = f["processing/ophys/FiberPhotometrySeriesDfOverF"]
        r["dff"] = d["data"][:]
        r["dff_t"] = d["timestamps"][:]
        r.update(_fp_meta(f))
    return r


def z_on_frames(s: dict) -> tuple[np.ndarray, int]:
    """The 30 Hz z-scored photometry of an open field session and the behaviour frame of its first
    sample (the file's starting_time times 30, the frame grid of the kinematics)."""
    return s["z"], int(round(s["z_t0"] * s["kin_rate"]))


def frame_aligned(s: dict) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """z, speed and motif label on the frames both cover."""
    z, off = z_on_frames(s)
    n = min(len(z), len(s["lin"]) - off)
    return z[:n], s["lin"][off:off + n], s["motif"][off:off + n]


def motif_onsets(labels: np.ndarray) -> dict[int, np.ndarray]:
    """First frame of every run of a label (frame 0 left out, as it has no preceding frame)."""
    starts = np.flatnonzero(np.diff(labels) != 0) + 1
    out = {}
    for m in np.unique(labels):
        out[int(m)] = starts[labels[starts] == m]
    return out


# --- evoked release ------------------------------------------------------------

def load_opto(asset_id: str) -> dict:
    f = open_asset(asset_id)
    r = _subject(f)
    r.update(_fp_meta(f))
    d = f["processing/ophys/FiberPhotometrySeriesDfOverF"]
    r["dff"], r["t"] = d["data"][:], d["timestamps"][:]
    e = f["intervals/optogenetic_epochs"]
    r["on"], r["off"] = e["start_time"][:], e["stop_time"][:]
    r["power"] = e["power_in_mW"][:]
    r["pulses"] = e["number_pulses_per_pulse_train"][:]
    r["period_ms"] = e["period_in_ms"][:]
    return r


# --- reaching and water drop ---------------------------------------------------

def parse_reach(description: str) -> dict:
    d = description
    exp = re.search(r"Experiment: (\S+?)\.", d)
    phase = re.search(r"Test phase: (\S+)", d)
    out = {"experiment": exp.group(1) if exp else ("fp" if "fiber photometry" in d else ""),
           "phase": phase.group(1) if phase else ""}
    if "anxa1_tet" in out["experiment"]:
        out["group"] = "Ctrl" if "Littermate control" in d else "Anxa1-TeTx"
    elif "anxa1_arch" in out["experiment"]:
        out["group"] = "Ctrl" if "Littermate control" in d else "Anxa1-Arch"
    else:
        c = re.search(r"Cohort: (\S+?)\.", d)
        out["group"] = c.group(1) if c else ""
    light = re.search(r"(Optogenetic silencing laser[^.]*\.|Not applicable[^.]*\.)", d)
    out["light"] = light.group(1) if light else ""
    return out


def load_reach(asset_id: str) -> dict:
    f = open_asset(asset_id)
    r = _subject(f)
    r.update(parse_reach(r["description"]))
    ev = f.get("processing/behavior/reaching_events")
    rows = []
    if ev is not None:
        idx = ev["event_times_index"][:]
        labels = [_s(x) for x in ev["label"][:]]
        cols = {c: ev[c][:] for c in ["event_times", "frame", "paw", "distance_cm", "distance_px", "reference_px"]}
        lo = 0
        for lab, hi in zip(labels, idx):
            for j in range(lo, hi):
                rows.append({"label": lab, "time": cols["event_times"][j], "frame": cols["frame"][j],
                             "paw": _s(cols["paw"][j]), "distance_cm": cols["distance_cm"][j],
                             "distance_px": cols["distance_px"][j], "reference_px": cols["reference_px"][j]})
            lo = hi
    r["events"] = pd.DataFrame(rows, columns=["label", "time", "frame", "paw", "distance_cm", "distance_px", "reference_px"])
    vid = [k for k in f["acquisition"] if k.startswith("Video")]
    r["video_rate"] = float(f[f"acquisition/{vid[0]}/starting_time"].attrs["rate"]) if vid else np.nan
    r["fp"] = "processing/ophys/FiberPhotometrySeriesDfOverF" in f
    if r["fp"]:
        d = f["processing/ophys/FiberPhotometrySeriesDfOverF"]
        r["dff"], r["t"] = d["data"][:], d["timestamps"][:]
        r.update(_fp_meta(f))
        r["fp_group"] = fp_reach_group(r)
    return r


def fp_reach_group(r: dict) -> str:
    """The paper's group of a water drop photometry session, from indicator, line and fiber site."""
    if "GCaMP" in r["indicator"]:
        return ("Anxa1" if "anxa1" in r["genotype"].lower() else "DAT") + " GCaMP-dCP"
    if "dLight" in r["indicator"]:
        return "dLight-dCP" if r["location"].startswith("Dorsal") else "dLight-cCP"
    return ""


# --- arrow maze ----------------------------------------------------------------

MAZE_POINTS = ["Tailbase", "Snout", "Leftfrontpaw", "Rightfrontpaw", "Leftbackpaw", "Rightbackpaw"]


def parse_maze(description: str) -> dict:
    m = re.match(r"Day (\d+) from group '(.*?)' cohort '(.*?)'", description)
    return {"day": int(m.group(1)), "group_raw": m.group(2), "cohort": m.group(3)} if m else {}


def load_maze(asset_id: str) -> dict:
    """Arrow maze session: pose of six points (pixels) and their DeepLabCut confidence."""
    f = open_asset(asset_id)
    r = _subject(f)
    r.update(parse_maze(r["description"]))
    r["group"] = {"ctrl": "Ctrl-Tdtomato", "anxa1_tet": "Anxa1-TeTx"}.get(r.get("group_raw"), r.get("group_raw"))
    p = "processing/behavior/PoseEstimationDeepLabCut/PoseEstimationSeries"
    r["xy"] = np.stack([f[p + n + "/data"][:] for n in MAZE_POINTS])           # (6, frames, 2)
    r["conf"] = np.stack([f[p + n + "/confidence"][:] for n in MAZE_POINTS])   # (6, frames)
    r["rate"] = float(f[p + "Tailbase/starting_time"].attrs["rate"])
    return r


def maze_speed(r: dict, points: str, min_conf: float | None = None) -> np.ndarray:
    """Speed in pixels/s per frame: `points` 'tail' (tail base) or 'mean6' (mean of the six points),
    the readings of the claims file's header. With `min_conf`, positions below that DeepLabCut
    confidence are set missing and linearly interpolated (a variant; the claims file leaves
    smoothing open)."""
    xy = r["xy"].copy()
    if min_conf is not None:
        for i in range(xy.shape[0]):
            bad = r["conf"][i] < min_conf
            for c in range(2):
                v = xy[i, :, c]
                v[bad] = np.nan
                ok = np.isfinite(v)
                if ok.sum() > 2:
                    xy[i, :, c] = np.interp(np.arange(len(v)), np.flatnonzero(ok), v[ok])
    pos = xy[0] if points == "tail" else xy.mean(axis=0)
    return np.hypot(*np.diff(pos, axis=0).T) * r["rate"]


# --- signal measures -----------------------------------------------------------

def zscore(x: np.ndarray) -> np.ndarray:
    return (x - np.nanmean(x)) / np.nanstd(x)


def peri(t: np.ndarray, x: np.ndarray, events: np.ndarray, lo: float, hi: float, dt: float = 1 / 60):
    """Signal x(t) around each event, linearly interpolated onto a regular grid lo..hi (a standard
    choice; the photometry is sampled at 60 Hz). Events whose window leaves the recording are
    dropped; returns the grid, an (events, grid) array and the events kept."""
    grid = np.arange(lo, hi + dt / 2, dt)
    keep = [e for e in events if e + lo >= t[0] and e + hi <= t[-1]]
    if not keep:
        return grid, np.empty((0, len(grid))), np.array([])
    return grid, np.stack([np.interp(e + grid, t, x) for e in keep]), np.array(keep)


def auc(grid: np.ndarray, y: np.ndarray, a: float, b: float) -> np.ndarray:
    """Trapezoid area of y (last axis) over a <= grid <= b."""
    sel = (grid >= a - 1e-9) & (grid <= b + 1e-9)
    return np.trapezoid(y[..., sel], grid[sel], axis=-1)


def sidak(p, m: int):
    return 1 - (1 - np.asarray(p, float)) ** m


def rm_oneway(values: np.ndarray) -> dict:
    """RM one-way ANOVA over the columns of values (rows are recordings), with the
    Geisser-Greenhouse correction the claims file reads from the fractional degrees of freedom."""
    n, k = values.shape
    grand = values.mean()
    ss_cond = n * ((values.mean(axis=0) - grand) ** 2).sum()
    ss_subj = k * ((values.mean(axis=1) - grand) ** 2).sum()
    ss_err = ((values - grand) ** 2).sum() - ss_cond - ss_subj
    df1, df2 = k - 1, (k - 1) * (n - 1)
    F = (ss_cond / df1) / (ss_err / df2)
    S = np.cov(values, rowvar=False)
    C = np.eye(k) - 1 / k
    Sc = C @ S @ C
    eps = np.trace(Sc) ** 2 / ((k - 1) * np.sum(Sc * Sc))
    eps = min(1.0, eps)
    p = stats.f.sf(F, df1 * eps, df2 * eps)
    return {"F": F, "df1": df1 * eps, "df2": df2 * eps, "p": p, "eps": eps, "n": n}


def paired_sidak(values: np.ndarray, pairs: list[tuple[int, int]]) -> pd.DataFrame:
    """Paired t-tests between columns, Sidak-adjusted over the pairs (Prism's comparisons after an
    RM ANOVA with the Geisser-Greenhouse correction use each pair's own differences)."""
    rows = []
    for a, b in pairs:
        t, p = stats.ttest_rel(values[:, a], values[:, b])
        rows.append({"pair": f"{a + 1} vs {b + 1}", "mean diff": float(np.mean(values[:, b] - values[:, a])),
                     "t": t, "p": p})
    df = pd.DataFrame(rows)
    df["p Sidak"] = sidak(df.p, len(pairs))
    return df


def mixed_anova(df: pd.DataFrame, dv: str, within: str, between: str, subject: str) -> pd.DataFrame:
    """Two-way ANOVA with one repeated factor (Prism's RM two-way ANOVA), via pingouin."""
    import pingouin as pg
    return pg.mixed_anova(data=df, dv=dv, within=within, between=between, subject=subject)
