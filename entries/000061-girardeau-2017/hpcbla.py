"""Loading and measures for the hippocampus and amygdala recordings of dandiset 000061.

Girardeau, Inema & Buzsaki (2017), Nature Neuroscience, doi:10.1038/nn.4637.

Each NWB file is one day of one rat: sorted units with a brain-region label (and, in five Rat08
files, a `cell_type` column), sleep states (Awake, Non-REM, REM), an epochs table (pre-run,
pre-sleep, run, post-sleep, post-run), and annotation series for hippocampal ripples (`rip`:
start, peak and stop of each ripple), air puffs (`puf`) and rewards at the left and right ends
of the track (`lrw`, `rrw`). Some files also hold raw voltage, LFP and video, which are not read
here except for their shapes. Files are streamed from the archive at the pinned version; nothing
is written to disk.

Where the parameters come from. The claims file (claims/000061/10.1038-nn.4637.yaml) fixes the
methods from the paper's Online Methods, legends and code; its shared methods are M1 to M8 and
its open details O1 to O7, cited below.

- `EPOCH_TIME_SCALE`: the epochs table is stored in milliseconds although its column says
  seconds; the data check shows this (its last stop time is 1000 times the LFP duration).
- Region labels (M1): hippocampus `HPC_LABELS`, BLA `BLA_LABELS`, central nuclei `CEN_LABELS`,
  piriform cortex `PIR_LABELS` (case is ignored). `BLA_COMPLEX_LABELS` adds the labels the
  paper's Supplementary Fig. 3 names as other amygdala nuclei (BLV, LaDL, BMP), for a variant.
- `CELL_TYPES`: the dandiset's `cell_type` values "excitatory" and "inhibitory" are read as the
  paper's monosynaptically identified pyramidal cells and interneurons (O4 reading a); the data
  check gives the reasons this reading is consistent with the data.
- `BIN_S` (50 ms, M3, M4, M7), `MIN_CELLS` (6 in each structure, M4, M7), `MIN_REM_S` (180 s of
  REM in each sleep epoch, M4), `PERIOD_BINS` (24,000 bins of 20 min, reactivation-decay).
- `RIPPLE_GUARD_S` (100 ms either side of a ripple left out of the baseline, M6) and
  `RIPPLE_P` (0.0005 per tail, M6).
- `PERI_RIPPLE_S`, `PERI_BINS`, `PERI_SMOOTH_BINS`, `PEAK_WINDOW_S` (M7: 100 bins over -2 to
  +2 s, Gaussian smoothing of SD 2 bins, mean over bin centres strictly inside +-0.25 s).
- Bin times are bin centres (O3, a standard choice that cannot change an outcome at this
  resolution), and a 50 ms bin belongs to a set of intervals when its centre does (a standard
  choice). A ripple is in NREM when its peak is (M5; a standard choice for "inside").
- Laps (O1 reading c): the intervals between consecutive rewards at opposite ends of the track.
  A lap so includes the time spent on the starting platform after its reward, which the M8 laps
  (position inside a 150-cm window) leave out. `trim_laps` (variants only, decides no claim)
  keeps laps of at most 30 s or cuts each lap to its last 10 s; these values are the author's.
- M3 drops spikes after the end of the last run epoch. It is not applied: the last run epoch
  (post-run) follows post-sleep, and every analysis here reads only bins of the run and of the
  sleep epochs and z-scores within those bins, so the dropped spikes could not enter any of them.
- `MONO_*` (data check only, decides no claim): short-latency cross-correlogram test of whether
  a unit drives or inhibits another, used to check what the `cell_type` column marks. The
  windows are a standard choice for monosynaptic connections (1 to 4 ms after the reference
  spike against a 10 to 25 ms flank baseline); the p-value thresholds are shown at three values.
- Absence context (`signed_rank_power`, `min_detectable_shift`, `median_ci`): resampling of the
  session values, a standard choice; it gives power and bounds and decides no claim.
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy import stats
from scipy.ndimage import gaussian_filter1d

DANDISET_ID = "000061"
DANDISET_VERSION = "0.250624.0426"

EPOCH_TIME_SCALE = 1e-3
HPC_LABELS = {"hpc", "hip"}
BLA_LABELS = {"bla"}
BLA_COMPLEX_LABELS = {"bla", "blv", "bmp", "ladl"}
CEN_LABELS = {"cen"}
PIR_LABELS = {"pir"}
KEEP_LABELS = HPC_LABELS | BLA_COMPLEX_LABELS | CEN_LABELS
CELL_TYPES = {"excitatory": "pyramidal", "inhibitory": "interneuron"}

BIN_S = 0.05
MIN_CELLS = 6
MIN_REM_S = 180.0
PERIOD_BINS = 24000

RIPPLE_GUARD_S = 0.1
RIPPLE_P = 0.0005

PERI_RIPPLE_S = 2.0
PERI_BINS = 100
PERI_SMOOTH_BINS = 2
PEAK_WINDOW_S = 0.25

MONO_EDGES = np.array([-0.025, -0.01, -0.004, -0.001, 0.001, 0.004, 0.01, 0.025])
MONO_P = (1e-3, 1e-6, 1e-10)

MIXED_UNITS_NOTE = (
    "In some files the spike times of unit 1 fall back once, after 65536 times k spikes, and "
    "unit 0 stops part way through the session where unit 1 starts: the first part of unit 1 "
    "is the end of unit 0. Units 0 and 1 of those files are left out of the analyses.")


def asset_urls(version: str = DANDISET_VERSION) -> list[tuple[str, str]]:
    """(path, streaming URL) of every NWB file at a version."""
    with DandiAPIClient() as client:
        dandiset = client.get_dandiset(DANDISET_ID, version)
        return sorted((a.path, a.get_content_url(follow_redirects=1, strip_query=True))
                      for a in dandiset.get_assets() if a.path.endswith(".nwb"))


def _text(value) -> str:
    value = value[()]
    if isinstance(value, np.ndarray):
        value = value[0]
    return value.decode() if isinstance(value, bytes) else str(value)


def _strings(dataset) -> np.ndarray:
    return np.array([v.decode() if isinstance(v, bytes) else str(v) for v in dataset[()]])


def load_session(path: str, url: str) -> dict:
    """One file: metadata, tables and events, and the spike trains of the units analysed.

    Spike trains are kept for units labelled hippocampus, BLA (and the wider amygdala labels) or
    central nuclei; every unit keeps its label, type, spike count and first spike. Epoch times
    are converted to seconds with `EPOCH_TIME_SCALE`.
    """
    for attempt in range(3):
        try:
            f = h5py.File(remfile.File(url), "r")
            break
        except OSError:
            if attempt == 2:
                raise
    with f:
        s = {"path": path, "session": path.split("ses-")[1].split("_")[0],
             "rat": _text(f["general/subject/subject_id"]),
             "species": _text(f["general/subject/species"]),
             "age": _text(f["general/subject/age"]), "sex": _text(f["general/subject/sex"]),
             "session_start": _text(f["session_start_time"])}
        ep = f["intervals/epochs"]
        s["epoch_unit_stated"] = ep["start_time"].attrs.get("description")
        s["epochs_raw"] = list(zip(_strings(ep["tags"]), ep["start_time"][()], ep["stop_time"][()]))
        s["epochs"] = [(t, a * EPOCH_TIME_SCALE, b * EPOCH_TIME_SCALE) for t, a, b in s["epochs_raw"]]
        if "processing/behavior/states" in f:
            st = f["processing/behavior/states"]
            s["states"] = list(zip(_strings(st["label"]), st["start_time"][()].astype(float),
                                   st["stop_time"][()].astype(float)))
        else:
            s["states"] = None
        s["trials"] = None
        if "intervals/trials" in f:
            tr = f["intervals/trials"]
            s["trials"] = (tr["start_time"][()], tr["stop_time"][()], tr.attrs.get("description"))
        events = {}
        for name in (f["stimulus/presentation"] if "stimulus/presentation" in f else []):
            g = f[f"stimulus/presentation/{name}"]
            events[name] = (_strings(g["data"]), g["timestamps"][()], g.attrs.get("description"))
        s["events"] = events
        s["ripples"] = parse_ripples(*events["rip"][:2]) if "rip" in events else None
        lfp = "processing/ecephys/LFP/LFP"
        s["lfp"] = None
        if lfp in f:
            s["lfp"] = (f[f"{lfp}/data"].shape, float(f[f"{lfp}/starting_time"].attrs["rate"]),
                        f[f"{lfp}/data"].attrs.get("unit"))
        raw = "acquisition/ElectricalSeries/data"
        s["raw"] = (f[raw].shape, f[raw].chunks) if raw in f else None
        s["videos"] = {k: (f[f"acquisition/{k}/data"].shape[0], *f[f"acquisition/{k}/timestamps"][[0, -1]],
                           f[f"acquisition/{k}/timestamps"].attrs.get("unit"))
                       for k in f["acquisition"] if k.startswith("Video")}
        s["video_storage"] = {k: (f[f"acquisition/{k}/data"].shape, str(f[f"acquisition/{k}/data"].dtype),
                                  f[f"acquisition/{k}/data"].compression)
                              for k in f["acquisition"] if k.startswith("Video")}
        # The groups under acquisition, processing (two levels), stimulus and intervals, with
        # their NWB type, to show what each file holds beyond the paths read here (video series
        # are left out; the video check lists them).
        s["groups"] = []
        parents = [p for p in ("acquisition", "processing", "stimulus", "stimulus/presentation", "intervals") if p in f]
        parents += [f"processing/{m}" for m in (f["processing"] if "processing" in f else [])]
        for parent in parents:
            for k in f[parent]:
                if not k.startswith("Video") and f[parent].get(k, getclass=True) is h5py.Group:
                    kind = f[f"{parent}/{k}"].attrs.get("neurodata_type")
                    s["groups"].append((f"{parent}/{k}", kind.decode() if isinstance(kind, bytes) else kind))
        s["electrode_locations"] = sorted(set(_strings(f["general/extracellular_ephys/electrodes/location"])))
        s["units"] = None
        if "units" in f:
            u = f["units"]
            n = len(u["id"])
            loc = _strings(u["location"]) if "location" in u else np.array(["(none)"] * n)
            ctype = _strings(u["cell_type"]) if "cell_type" in u else np.array([""] * n)
            index = u["spike_times_index"][()]
            spikes = u["spike_times"][()]
            trains = np.split(spikes, index[:-1])
            unsorted = [i for i, t in enumerate(trains) if np.any(np.diff(t) < 0)]
            # A unit whose times fall back once holds the end of the unit before it (see
            # `MIXED_UNITS_NOTE`); both are left out of the analyses.
            mixed = sorted({j for i in unsorted for j in (i - 1, i) if j >= 0})
            s["units"] = {
                "columns": list(u.attrs["colnames"]),
                "cell_type_description": u["cell_type"].attrs.get("description") if "cell_type" in u else None,
                "label": loc, "region": np.char.lower(loc), "cell_type": ctype,
                "shank": u["shank_id"][()],
                "group": np.array([f[r].name.split("/")[-1] for r in u["electrode_group"][()]]),
                "n_spikes": np.diff(np.concatenate([[0], index])),
                "first_spike": np.array([t[0] if len(t) else np.nan for t in trains]),
                "unsorted": unsorted, "mixed": mixed,
                "unsorted_at": {i: np.flatnonzero(np.diff(trains[i]) < 0).tolist() for i in unsorted},
                "unit0_last": float(trains[0][-1]) if len(trains) and len(trains[0]) else np.nan,
                "unit1_first": float(trains[1][0]) if len(trains) > 1 and len(trains[1]) else np.nan,
                "trains": {i: t for i, t in enumerate(trains)
                           if loc[i].lower() in KEEP_LABELS and i not in mixed},
                "last_spike": float(spikes.max()) if len(spikes) else np.nan,
                "has_location_column": "location" in u,
            }
    return s


def asset_variables(version: str = DANDISET_VERSION) -> dict[str, list[str]]:
    """The variables the archive's asset metadata lists for each NWB file (variableMeasured)."""
    with DandiAPIClient() as client:
        dandiset = client.get_dandiset(DANDISET_ID, version)
        return {a.path: [v.get("value") for v in a.get_raw_metadata().get("variableMeasured", [])]
                for a in dandiset.get_assets() if a.path.endswith(".nwb")}


def load_all(workers: int = 12, version: str = DANDISET_VERSION) -> list[dict]:
    """Every file of the dandiset, loaded in parallel."""
    urls = asset_urls(version)
    with ThreadPoolExecutor(workers) as pool:
        return list(pool.map(lambda pu: load_session(*pu), urls))


def parse_ripples(labels: np.ndarray, times: np.ndarray) -> dict:
    """The `rip` annotations as arrays of start, peak and stop, with the channel in each label.

    The labels come in triplets "Ripple start N", "Ripple peak N", "Ripple stop N"; `ordered`
    says whether every triplet is in that order with increasing times.
    """
    kind = np.array([lab.split()[1] for lab in labels])
    channel = np.array([lab.split()[2] if len(lab.split()) > 2 else "" for lab in labels])
    n = len(labels) // 3
    k = kind[:3 * n].reshape(n, 3)
    t = times[:3 * n].reshape(n, 3)
    ordered = bool(len(labels) % 3 == 0 and np.all(k == ["start", "peak", "stop"])
                   and np.all(np.diff(t, axis=1) >= 0))
    return {"start": t[:, 0], "peak": t[:, 1], "stop": t[:, 2], "ordered": ordered,
            "channels": sorted(set(channel))}


# --- intervals -------------------------------------------------------------------------------

def intervals_of(session: dict, label: str) -> np.ndarray:
    """(n, 2) state intervals with the given label, in seconds, sorted."""
    if session["states"] is None:
        return np.zeros((0, 2))
    return np.array(sorted((a, b) for lab, a, b in session["states"] if lab == label)).reshape(-1, 2)


def sleep_epochs(session: dict) -> tuple[np.ndarray, np.ndarray, tuple[float, float] | None]:
    """Pre-sleep intervals, post-sleep intervals and the (first) run epoch, in seconds (M2).

    Tags presleep and postsleep are used where present (a file may have two of either). Files
    that tag sleep only as "sleep" take the sleep epochs before and after the first run.
    """
    eps = session["epochs"]
    runs = [(a, b) for t, a, b in eps if t == "run"]
    run = runs[0] if runs else None
    pre = [(a, b) for t, a, b in eps if t == "presleep"]
    post = [(a, b) for t, a, b in eps if t == "postsleep"]
    if not pre and not post and run is not None:
        pre = [(a, b) for t, a, b in eps if t == "sleep" and b <= run[0]]
        post = [(a, b) for t, a, b in eps if t == "sleep" and a >= run[1]]
    return np.array(sorted(pre)).reshape(-1, 2), np.array(sorted(post)).reshape(-1, 2), run


def intersect(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Intersection of two sets of (start, stop) intervals."""
    out = []
    for s1, e1 in a:
        for s2, e2 in b:
            s, e = max(s1, s2), min(e1, e2)
            if e > s:
                out.append((s, e))
    return np.array(sorted(out)).reshape(-1, 2)


def in_intervals(t: np.ndarray, iv: np.ndarray) -> np.ndarray:
    """Whether each time lies in one of the sorted, non-overlapping intervals."""
    if len(iv) == 0:
        return np.zeros(len(t), bool)
    i = np.searchsorted(iv[:, 0], t, side="right") - 1
    ok = i >= 0
    out = np.zeros(len(t), bool)
    out[ok] = t[ok] < iv[i[ok], 1]
    return out


def state_in(session: dict, label: str, epochs: np.ndarray) -> np.ndarray:
    """Intervals of a sleep state inside a set of epochs, e.g. pre-NREM (M2)."""
    return intersect(intervals_of(session, label), epochs)


# --- laps (O1 reading c) ----------------------------------------------------------------------

def laps(session: dict) -> list[tuple[float, float, str]]:
    """Laps from a reward at one end of the track to the next reward at the other end.

    Direction "LR" runs from the left reward to the right one. Consecutive rewards at the same
    end do not make a lap.
    """
    ev = sorted([(t, "L") for t in session["events"]["lrw"][1]] +
                [(t, "R") for t in session["events"]["rrw"][1]])
    return [(a, b, sa + sb) for (a, sa), (b, sb) in zip(ev[:-1], ev[1:]) if sa != sb]


def run_laps(session: dict) -> list[tuple[float, float, str]]:
    """Laps whose both rewards fall inside the run epoch."""
    _, _, run = sleep_epochs(session)
    if run is None:
        return []
    return [(a, b, d) for a, b, d in laps(session) if a >= run[0] and b <= run[1]]


def puff_direction(session: dict) -> tuple[str | None, dict]:
    """The lap direction in the run epoch that holds most air puffs, and the counts."""
    counts = {"LR": 0, "RL": 0, "none": 0}
    if "puf" not in session["events"] or sleep_epochs(session)[2] is None:
        return None, counts
    run_laps_ = run_laps(session)
    for t in session["events"]["puf"][1]:
        d = [lap[2] for lap in run_laps_ if lap[0] <= t < lap[1]]
        counts[d[0] if d else "none"] += 1
    if counts["LR"] == counts["RL"]:
        return None, counts
    return ("LR" if counts["LR"] > counts["RL"] else "RL"), counts


def lap_intervals(session: dict, kind: str) -> np.ndarray:
    """Run laps of the air puff direction ("puff") or of the other one ("safe")."""
    direction, _ = puff_direction(session)
    if direction is None:
        return np.zeros((0, 2))
    keep = [(a, b) for a, b, d in run_laps(session) if (d == direction) == (kind == "puff")]
    return np.array(keep).reshape(-1, 2)


def trim_laps(iv: np.ndarray, max_s: float | None = None, last_s: float | None = None) -> np.ndarray:
    """Laps of at most max_s, or each lap cut to its last last_s seconds (variants only).

    Both limit the time on the starting platform and the stops that a reading c lap holds; the
    values are the author's, for a robustness check that decides no claim.
    """
    d = iv[:, 1] - iv[:, 0]
    if max_s is not None:
        iv = iv[d <= max_s]
    if last_s is not None:
        iv = np.column_stack([np.maximum(iv[:, 0], iv[:, 1] - last_s), iv[:, 1]])
    return iv.reshape(-1, 2)


# --- units and binning -----------------------------------------------------------------------

def units_of(session: dict, labels: set, cell_type: str | None = None) -> list[int]:
    """Units with one of the region labels (and, if given, the dandiset's cell type)."""
    u = session["units"]
    if u is None:
        return []
    return [i for i in u["trains"] if u["region"][i] in labels
            and (cell_type is None or u["cell_type"][i] == cell_type)]


def grid_size(session: dict, bin_s: float = BIN_S) -> int:
    """Number of bins of width bin_s from 0 to the end of the last epoch or spike."""
    end = max(max(b for _, _, b in session["epochs"]), session["units"]["last_spike"])
    return int(np.ceil(end / bin_s)) + 1


def rows_in(session: dict, iv: np.ndarray, bin_s: float = BIN_S) -> np.ndarray:
    """Indices of the bins whose centre lies in the intervals."""
    centers = (np.arange(grid_size(session, bin_s)) + 0.5) * bin_s
    return np.flatnonzero(in_intervals(centers, iv))


def binned(session: dict, units: list[int], rows: np.ndarray, bin_s: float = BIN_S) -> np.ndarray:
    """(len(rows), n_units) spike counts in the bins `rows` of the grid of width bin_s."""
    n = grid_size(session, bin_s)
    out = np.zeros((len(rows), len(units)), np.float64)
    for j, i in enumerate(units):
        idx = (session["units"]["trains"][i] / bin_s).astype(np.int64)
        out[:, j] = np.bincount(idx[(idx >= 0) & (idx < n)], minlength=n)[rows]
    return out


def zscore(x: np.ndarray) -> np.ndarray:
    """Z-score each column; a column without variance becomes NaN."""
    sd = x.std(0)
    with np.errstate(invalid="ignore", divide="ignore"):
        return (x - x.mean(0)) / np.where(sd > 0, sd, np.nan)


# --- EV and REV (M4) ---------------------------------------------------------------------------

def pair_correlations(counts: np.ndarray, a: np.ndarray, b: np.ndarray | None = None) -> np.ndarray:
    """Pearson correlations of binned counts between columns a and b, as one vector of pairs.

    With b None, the distinct pairs within a (upper triangle). A silent column gives NaN.
    """
    z = zscore(counts)
    if b is None:
        c = z[:, a].T @ z[:, a] / len(z)
        return c[np.triu_indices(len(a), 1)]
    return (z[:, a].T @ z[:, b] / len(z)).ravel()


def ev_rev(pre: np.ndarray, run: np.ndarray, post: np.ndarray) -> tuple[float, float, int]:
    """EV and REV (percent) from three vectors of pair correlations, and the pairs used.

    Pairs with an undefined correlation in any epoch are left out (corrcoef 'rows','complete').
    """
    ok = np.isfinite(pre) & np.isfinite(run) & np.isfinite(post)
    if ok.sum() < 3:
        return np.nan, np.nan, int(ok.sum())
    r = np.corrcoef(np.vstack([pre[ok], run[ok], post[ok]]))
    r_pre_run, r_pre_post, r_run_post = r[0, 1], r[0, 2], r[1, 2]
    ev = ((r_run_post - r_pre_run * r_pre_post) / np.sqrt((1 - r_pre_run ** 2) * (1 - r_pre_post ** 2))) ** 2
    rev = ((r_pre_run - r_run_post * r_pre_post) / np.sqrt((1 - r_run_post ** 2) * (1 - r_pre_post ** 2))) ** 2
    return 100 * ev, 100 * rev, int(ok.sum())


def session_epoch_rows(session: dict, state: str = "Non-REM") -> dict:
    """Bins of the run epoch and of a state inside pre- and post-sleep, with their durations."""
    pre, post, run = sleep_epochs(session)
    pre_iv, post_iv = state_in(session, state, pre), state_in(session, state, post)
    return {"pre": rows_in(session, pre_iv), "post": rows_in(session, post_iv),
            "run": rows_in(session, np.array([run])),
            "pre_s": float(np.diff(pre_iv).sum()), "post_s": float(np.diff(post_iv).sum())}


def ev_session(session: dict, a_units: list[int], b_units: list[int] | None, rows: dict,
               post_periods: bool = False) -> dict:
    """EV and REV of one session between two sets of units (or within one set, b None).

    With `post_periods`, also for the successive `PERIOD_BINS` blocks of post-sleep bins (the
    first three, the third being what remains when shorter), each with the whole pre-sleep and run.
    """
    units = a_units + (b_units or [])
    a = np.arange(len(a_units))
    b = None if b_units is None else np.arange(len(a_units), len(units))
    corr = {k: pair_correlations(binned(session, units, rows[k]), a, b) for k in ("pre", "run", "post")}
    ev, rev, n_pairs = ev_rev(corr["pre"], corr["run"], corr["post"])
    out = {"ev": ev, "rev": rev, "pairs": n_pairs}
    if post_periods:
        post_rows = rows["post"]
        for k in range(3):
            block = post_rows[k * PERIOD_BINS:(k + 1) * PERIOD_BINS]
            if len(block) < 2:
                out[f"ev_{k}"], out[f"rev_{k}"] = np.nan, np.nan
                continue
            c = pair_correlations(binned(session, units, block), a, b)
            out[f"ev_{k}"], out[f"rev_{k}"], _ = ev_rev(corr["pre"], corr["run"], c)
            out[f"bins_{k}"] = len(block)
    return out


# --- ripple modulation (M6) ---------------------------------------------------------------------

def nrem_ripples(session: dict, nrem: np.ndarray | None = None) -> dict:
    """Ripples whose peak lies in NREM (all NREM of the session unless given)."""
    if nrem is None:
        nrem = intervals_of(session, "Non-REM")
    r = session["ripples"]
    keep = in_intervals(r["peak"], nrem)
    return {k: r[k][keep] for k in ("start", "peak", "stop")}


def merge(iv: np.ndarray) -> np.ndarray:
    """Union of possibly overlapping intervals, sorted."""
    if len(iv) == 0:
        return iv.reshape(0, 2)
    iv = iv[np.argsort(iv[:, 0])]
    out = [list(iv[0])]
    for a, b in iv[1:]:
        if a <= out[-1][1]:
            out[-1][1] = max(out[-1][1], b)
        else:
            out.append([a, b])
    return np.array(out)


def subtract(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Intervals a minus the (merged) intervals b."""
    b = merge(b)
    out = []
    for s, e in a:
        cur = s
        for bs, be in b[(b[:, 1] > s) & (b[:, 0] < e)]:
            if bs > cur:
                out.append((cur, bs))
            cur = max(cur, be)
        if cur < e:
            out.append((cur, e))
    return np.array(out).reshape(-1, 2)


def count_in(train: np.ndarray, iv: np.ndarray) -> int:
    """Spikes of a sorted train inside the intervals (intervals may overlap; each counts)."""
    return int((np.searchsorted(train, iv[:, 1]) - np.searchsorted(train, iv[:, 0])).sum())


def ripple_modulation(session: dict, units: list[int]) -> list[dict]:
    """Poisson test of each unit's spikes in NREM ripples against its NREM baseline (M6, O2).

    Baseline: all NREM of the session minus every ripple widened by `RIPPLE_GUARD_S` either
    side. Expected count: baseline rate times the total ripple time (start to stop). Reading a
    of O2 takes the tails P(X >= n) and P(X <= n), reading b P(X > n) and P(X < n). A unit with
    no spike in ripples or in the baseline is untested.
    """
    nrem = intervals_of(session, "Non-REM")
    rip = nrem_ripples(session, nrem)
    rip_iv = np.column_stack([rip["start"], rip["stop"]])
    base = subtract(nrem, rip_iv + np.array([-RIPPLE_GUARD_S, RIPPLE_GUARD_S]))
    base_s = float(np.diff(base).sum())
    rip_s = float(np.diff(rip_iv).sum())
    out = []
    for i in units:
        t = session["units"]["trains"][i]
        n_rip, n_base = count_in(t, rip_iv), count_in(t, base)
        mu = n_base / base_s * rip_s
        row = {"unit": i, "n_ripple": n_rip, "n_base": n_base, "expected": mu,
               "tested": n_rip > 0 and n_base > 0}
        row["p_up_a"] = stats.poisson.sf(n_rip - 1, mu)
        row["p_down_a"] = stats.poisson.cdf(n_rip, mu)
        row["p_up_b"] = stats.poisson.sf(n_rip, mu)
        row["p_down_b"] = stats.poisson.cdf(n_rip - 1, mu) if n_rip > 0 else 0.0
        for r in ("a", "b"):
            row[f"up_{r}"] = row["tested"] and row[f"p_up_{r}"] < RIPPLE_P
            row[f"down_{r}"] = row["tested"] and row[f"p_down_{r}"] < RIPPLE_P
        out.append(row)
    return out


# --- reactivation strength R (M7) ------------------------------------------------------------------

def peri_ripple_mean(times: np.ndarray, values: np.ndarray, peaks: np.ndarray) -> np.ndarray:
    """Mean of `values` (sampled at sorted `times`) in `PERI_BINS` bins over +-`PERI_RIPPLE_S`
    around each peak, all peaks pooled (FMAToolbox SyncHist, mode mean), smoothed with a
    Gaussian of SD `PERI_SMOOTH_BINS` bins."""
    width = 2 * PERI_RIPPLE_S / PERI_BINS
    total = np.zeros(PERI_BINS)
    count = np.zeros(PERI_BINS)
    lo = np.searchsorted(times, peaks - PERI_RIPPLE_S)
    hi = np.searchsorted(times, peaks + PERI_RIPPLE_S)
    for p, a, b in zip(peaks, lo, hi):
        k = np.floor((times[a:b] - p + PERI_RIPPLE_S) / width).astype(int)
        ok = (k >= 0) & (k < PERI_BINS)
        np.add.at(total, k[ok], values[a:b][ok])
        np.add.at(count, k[ok], 1)
    with np.errstate(invalid="ignore"):
        curve = total / count
    curve = np.where(np.isfinite(curve), curve, np.nanmean(curve))
    return gaussian_filter1d(curve, PERI_SMOOTH_BINS, mode="nearest")


def peri_centres() -> np.ndarray:
    width = 2 * PERI_RIPPLE_S / PERI_BINS
    return -PERI_RIPPLE_S + width * (np.arange(PERI_BINS) + 0.5)


def reactivation_strength(session: dict, hpc: list[int], bla: list[int], template_iv: np.ndarray) -> dict:
    """Peri-ripple reactivation strength in pre- and post-NREM for one template (M7).

    Counts are z-scored per cell within the template bins and within the NREM bins of each sleep
    epoch; a cell silent in either is left out (it has no z-score). C = Z_hpc' Z_bla / nBins;
    R(t) = z_hpc(t) C z_bla(t)'; R is z-scored over the NREM bins of each epoch.
    """
    rows = session_epoch_rows(session)
    template = rows_in(session, template_iv)
    units = hpc + bla
    nh = len(hpc)
    counts = {k: binned(session, units, r) for k, r in (("run", template), ("pre", rows["pre"]), ("post", rows["post"]))}
    z = {k: zscore(c) for k, c in counts.items()}
    ok = np.all([np.isfinite(v).all(0) for v in z.values()], axis=0)
    h, b = np.flatnonzero(ok[:nh]), nh + np.flatnonzero(ok[nh:])
    c = z["run"][:, h].T @ z["run"][:, b] / len(template)
    out = {"template_bins": len(template), "hpc_used": len(h), "bla_used": len(b)}
    pre_iv, post_iv, _ = sleep_epochs(session)
    for k, iv in (("pre", pre_iv), ("post", post_iv)):
        r = np.einsum("ti,ij,tj->t", z[k][:, h], c, z[k][:, b])
        r = (r - r.mean()) / r.std()
        times = (rows[k] + 0.5) * BIN_S
        peaks = nrem_ripples(session, state_in(session, "Non-REM", iv))["peak"]
        curve = peri_ripple_mean(times, r, peaks)
        centres = peri_centres()
        out[f"{k}_curve"] = curve
        out[f"{k}_peak"] = float(curve[np.abs(centres) < PEAK_WINDOW_S].mean())
        out[f"{k}_ripples"] = len(peaks)
    return out


# --- firing by state, and ripple rate ------------------------------------------------------------

def state_rates(session: dict, units: list[int]) -> list[dict]:
    """Firing rate of each unit over all REM, all NREM and all wake intervals of the session."""
    ivs = {k: intervals_of(session, lab) for k, lab in (("rem", "REM"), ("nrem", "Non-REM"), ("wake", "Awake"))}
    out = []
    for i in units:
        t = session["units"]["trains"][i]
        out.append({"unit": i, **{k: count_in(t, iv) / np.diff(iv).sum() for k, iv in ivs.items()}})
    return out


def ripple_rates(session: dict) -> dict:
    """Ripple peaks per second of pre-NREM and of post-NREM."""
    pre, post, _ = sleep_epochs(session)
    out = {}
    for k, iv in (("pre", pre), ("post", post)):
        nrem = state_in(session, "Non-REM", iv)
        out[f"{k}_nrem_s"] = float(np.diff(nrem).sum())
        out[f"{k}_ripples"] = int(in_intervals(session["ripples"]["peak"], nrem).sum())
        out[f"{k}_rate"] = out[f"{k}_ripples"] / out[f"{k}_nrem_s"] if out[f"{k}_nrem_s"] > 0 else np.nan
    return out


# --- data check: short-latency connections ----------------------------------------------------

def mono_counts(trains: dict, ref: int, targets: list[int]) -> np.ndarray:
    """(len(targets), 7) counts of target spikes at the lags of `MONO_EDGES` from each spike of ref."""
    ids = np.concatenate([np.full(len(trains[j]), k) for k, j in enumerate(targets)])
    t = np.concatenate([trains[j] for j in targets])
    order = np.argsort(t, kind="stable")
    t, ids = t[order], ids[order]
    r = trains[ref]
    lo = np.searchsorted(t, r + MONO_EDGES[0])
    n = np.searchsorted(t, r + MONO_EDGES[-1]) - lo
    idx = np.repeat(lo - np.cumsum(np.concatenate([[0], n[:-1]])), n) + np.arange(n.sum())
    b = np.searchsorted(MONO_EDGES, t[idx] - np.repeat(r, n), side="right") - 1
    ok = (b >= 0) & (b < len(MONO_EDGES) - 1)
    k = len(MONO_EDGES) - 1
    return np.bincount(ids[idx][ok] * k + b[ok], minlength=len(targets) * k).reshape(len(targets), k)


def mono_connections(session: dict, ref: int) -> dict:
    """Number of loaded units that ref excites or inhibits at short latency, at each `MONO_P`.

    Count of target spikes 1 to 4 ms after ref's spikes against a Poisson of mean the 10 to 25 ms
    flanks' count scaled to 3 ms; excitation needs the upper tail below the threshold and more
    spikes after than 1 to 4 ms before (to set aside common input), inhibition the lower tail and
    fewer after than before.
    """
    trains = session["units"]["trains"]
    c = mono_counts(trains, ref, [j for j in trains if j != ref])
    flank = (MONO_EDGES[1] - MONO_EDGES[0]) + (MONO_EDGES[-1] - MONO_EDGES[-2])
    mu = c[:, [0, 6]].sum(1) * (MONO_EDGES[5] - MONO_EDGES[4]) / flank
    after, before = c[:, 4], c[:, 2]
    out = {}
    for p in MONO_P:
        out[f"excites_{p:g}"] = int(((stats.poisson.sf(after - 1, mu) < p) & (after > before) & (mu > 0)).sum())
        out[f"inhibits_{p:g}"] = int(((stats.poisson.cdf(after, mu) < p) & (after < before) & (mu > 0)).sum())
    return out


# --- context for claims of absence -----------------------------------------------------------

def signed_rank_power(diffs: np.ndarray, n: int, shift: float, rng: np.random.Generator,
                      n_sim: int = 2000) -> float:
    """Share of samples of n values, drawn with replacement from `diffs` centred on a median of
    zero and moved by `shift`, in which the two-sided Wilcoxon signed rank test has p < 0.05."""
    centred = np.asarray(diffs) - np.median(diffs)
    x = rng.choice(centred, size=(n_sim, n), replace=True) + shift
    return float((stats.wilcoxon(x, axis=1).pvalue < 0.05).mean())


def min_detectable_shift(diffs: np.ndarray, n: int, rng: np.random.Generator, power: float = 0.8,
                         n_sim: int = 2000) -> float:
    """Smallest positive shift of the median that `signed_rank_power` detects with `power`
    (bisection to 2% of the spread of `diffs`)."""
    hi = 4 * (np.std(diffs) + 1e-12)
    lo = 0.0
    while hi - lo > 0.02 * np.std(diffs):
        mid = (lo + hi) / 2
        if signed_rank_power(diffs, n, mid, rng, n_sim) >= power:
            hi = mid
        else:
            lo = mid
    return hi


def median_ci(x: np.ndarray, rng: np.random.Generator, n_boot: int = 5000) -> tuple[float, float]:
    """Percentile bootstrap 95% interval of the median."""
    x = np.asarray(x)
    m = np.median(rng.choice(x, size=(n_boot, len(x)), replace=True), axis=1)
    return float(np.percentile(m, 2.5)), float(np.percentile(m, 97.5))


def effect_r(p: float, n: int, sign: float) -> float:
    """Effect size r = z / sqrt(n) of a two-sided test, z from its p-value and the sign given."""
    return float(np.sign(sign) * stats.norm.isf(p / 2) / np.sqrt(n))


def time_frame_reads(url: str, video: str, n_frames: int = 20) -> tuple[float, int]:
    """Seconds taken to stream `n_frames` frames spread over a video, and the bytes per frame."""
    import time
    f = h5py.File(remfile.File(url), "r")
    with f:
        data = f[f"acquisition/{video}/data"]
        frames = np.linspace(0, data.shape[0] - 1, n_frames).astype(int)
        started = time.time()
        for k in frames:
            data[k]
        return time.time() - started, int(np.prod(data.shape[1:]) * data.dtype.itemsize)
