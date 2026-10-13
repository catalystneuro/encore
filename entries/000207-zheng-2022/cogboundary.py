"""Data access and analysis helpers for dandiset 000207 (Zheng et al. 2022).

The dandiset holds one NWB file per patient: spike times of medial temporal
lobe neurons, and three trial tables (encoding, scene recognition, time
discrimination). `load_sessions` streams all files from the DANDI Archive and
returns one `Session` per file.

Where a parameter comes from:

- The 1 s windows before and after a boundary, the definitions of boundary
  cells and event cells, the label-shuffling chance level, the 200 ms sliding
  window for firing-rate traces, and the 10 ms bins, 200 ms Gaussian kernel,
  per-trial z-score and 99% variance criterion of the state-space analysis
  are from the paper's Methods.
- The paper says "permutation t-test" without saying how the permutation is
  done. Here a before/after comparison permutes the sign of each trial's
  difference, and a comparison between conditions permutes the condition
  labels. Both are choices.
- Which soft boundaries count as SB trials is taken from the authors'
  published plotting code (github.com/rutishauserlab/cogboundary-zheng):
  every soft boundary, in SB clips and in HB clips, 75 per session. The
  Methods do not say. That code holds no cell selection, statistics or
  chance level, so everything else here still rests on the Methods.
- The window in which a response peak is searched, the window the principal
  components are fitted on, and matching trials across patients by clip name
  are choices; the Methods do not state them. Each is a named parameter
  below.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
import pandas as pd
from scipy.ndimage import gaussian_filter1d

DANDISET = "000207"
VERSION = "0.220216.0323"          # the version the paper's Data Availability statement cites
LATEST_VERSION = "0.230530.1822"   # the most recent published version, used only for a comparison

KINDS = ("NB", "SB", "HB")          # no boundary, soft boundary, hard boundary
REGIONS = ("hippocampus", "amygdala", "parahippocampus")
WINDOW = 1.0                        # s before and after a boundary (Methods)
ALPHA = 0.05                        # (Methods)
PERMUTATIONS = 1000                 # per test (Methods: 1000 runs)
PSTH_WIDTH = 0.2                    # s, sliding window of firing-rate traces (Methods)
BIN = 0.01                          # s, state-space bins (Methods)
SMOOTH_SD = 0.2                     # s, Gaussian kernel of the state-space analysis (Methods)
VARIANCE = 0.99                     # fraction of variance kept in the state space (Methods)
STATE_BEFORE, STATE_AFTER = 1.0, 1.5    # s around the boundary kept for the state space (choice)
TRIAL_BEFORE, TRIAL_AFTER = 1.0, 8.0    # s around clip onset over which a trial is z-scored (choice)
MAX_FIRST_SPIKE = 1.0               # s; a session whose first spike is further than this from
                                    # time zero does not share the trial tables' clock


@dataclass
class Session:
    subject: str
    units: list            # one sorted array of spike times (s) per unit
    region: np.ndarray     # one of REGIONS per unit
    side: np.ndarray       # "left" or "right" per unit
    encoding: pd.DataFrame
    recognition: pd.DataFrame
    order: pd.DataFrame    # the time discrimination task
    sanity: dict = field(default_factory=dict)

    @property
    def aligned(self) -> bool:
        """Whether the spike times are on the clock of the trial tables."""
        return abs(self.sanity["first spike (s)"]) < MAX_FIRST_SPIKE


# --- loading ------------------------------------------------------------------

def asset_urls(version: str = VERSION) -> dict:
    """Subject id -> download URL of its file, for one version of the dandiset."""
    from dandi.dandiapi import DandiAPIClient

    urls = {}
    with DandiAPIClient() as client:
        for asset in client.get_dandiset(DANDISET, version).get_assets():
            if asset.path.endswith(".nwb"):
                subject = asset.path.split("/")[0].removeprefix("sub-")
                urls[subject] = asset.get_content_url(follow_redirects=1, strip_query=True)
    return dict(sorted(urls.items(), key=lambda item: int(item[0])))


def _open(url: str):
    import h5py
    import remfile

    return h5py.File(remfile.File(url), "r")


def _table(group) -> pd.DataFrame:
    columns = {}
    for name, dataset in group.items():
        if getattr(dataset, "ndim", 0) != 1:
            continue
        values = dataset[()]
        if values.dtype.kind == "O":
            values = [v.decode() if isinstance(v, bytes) else v for v in values]
        columns[name] = values
    return pd.DataFrame(columns)


def _kind_from_name(names: pd.Series) -> pd.Series:
    return names.str.slice(0, 2)


def read_session(subject: str, url: str) -> Session:
    """Read one file. Nothing is written to disk."""
    with _open(url) as f:
        spikes = f["units/spike_times"][()]
        index = f["units/spike_times_index"][()]
        unit_electrode = f["units/electrodes"][()]
        location = np.array([v.decode() for v in f["general/extracellular_ephys/electrodes/location"][()]])
        encoding = _table(f["intervals/encoding_table"])
        recognition = _table(f["intervals/recognition_table"])
        order = _table(f["intervals/timediscrimination_table"])
        event_codes = f["acquisition/events/data"][()]
        event_times = f["acquisition/events/timestamps"][()]
        descriptions = {
            "encoding stimCategory": f["intervals/encoding_table/stimCategory"].attrs["description"],
            "boundary2_time": f["intervals/encoding_table/boundary2_time"].attrs["description"],
            "accuracy": f["intervals/timediscrimination_table/accuracy"].attrs["description"],
            "resp_value": f["intervals/timediscrimination_table/resp_value"].attrs["description"],
            "RT": f["intervals/timediscrimination_table/RT"].attrs["description"],
        }
        spike_unit = f["units/spike_times"].attrs.get("unit", "not stated")
        subject_id = f["general/subject/subject_id"][()].decode()

    starts = np.r_[0, index[:-1]]
    units = [np.sort(spikes[a:b]) for a, b in zip(starts, index)]
    unsorted_units = sum(bool(np.any(np.diff(spikes[a:b]) < 0)) for a, b in zip(starts, index))
    where = location[unit_electrode]
    region = np.array([w.rsplit("_", 1)[0] for w in where])
    side = np.array([w.rsplit("_", 1)[1] for w in where])

    # Encoding: the condition is taken from the clip's name, and checked against stimCategory.
    encoding = encoding.rename(columns={"Clip_name": "clip"})
    encoding["clip"] = encoding["clip"].str.replace(".mp4", "", regex=False)
    encoding["kind"] = _kind_from_name(encoding["clip"])
    for n in (1, 2, 3):
        offset = encoding[f"boundary{n}_time"] - encoding.start_time
        # A boundary that does not exist is stored as NaN (later versions) or as the clip's
        # own start time (the pinned version).
        encoding[f"b{n}"] = offset.where(offset.abs() > 1e-6)
    recognition["kind"] = _kind_from_name(recognition.frameName)
    recognition["target"] = recognition.stimuli_type == 1
    recognition["correct"] = recognition.accuracy == 2
    recognition["responded"] = recognition.old_new != 0
    order["kind"] = _kind_from_name(order.frameName)
    order["correct"] = order.accuracy == 2
    order["responded"] = order.confidence != 0

    real_events = event_times[event_codes != 0]
    sanity = {
        "subject_id in file": subject_id,
        "units": len(units),
        "spikes": int(len(spikes)),
        "first spike (s)": float(spikes.min()),
        "last spike (s)": float(spikes.max()),
        "first event (s)": float(real_events.min()),
        "last event (s)": float(real_events.max()),
        "events with code 0": int((event_codes == 0).sum()),
        "earliest code-0 timestamp (s)": float(event_times[event_codes == 0].min())
        if (event_codes == 0).any() else np.nan,
        "units with unsorted spike times": int(unsorted_units),
        "spike time unit": spike_unit,
        "stimCategory values": sorted(int(v) for v in encoding.stimCategory.unique()),
        "descriptions": descriptions,
    }
    return Session(subject, units, region, side, encoding, recognition, order, sanity)


def file_tree(url: str) -> list:
    """Every group and dataset in one file, with the shape of each dataset."""
    lines = []
    with _open(url) as f:
        f.visititems(lambda name, obj: lines.append(
            f"{name} {obj.shape}" if hasattr(obj, "shape") else f"{name}/"))
    return lines


def load_sessions(version: str = VERSION, subjects=None) -> list:
    """Stream every file of the dandiset (or only `subjects`) at one version."""
    urls = asset_urls(version)
    return [read_session(s, u) for s, u in urls.items() if subjects is None or s in subjects]


# --- spike counts and permutation tests ---------------------------------------

def spike_counts(units: list, times: np.ndarray, start: float, stop: float) -> np.ndarray:
    """Spikes of each unit in [t + start, t + stop) for each t. Shape (units, times)."""
    times = np.asarray(times, dtype=float)
    return np.array([np.searchsorted(u, times + stop) - np.searchsorted(u, times + start)
                     for u in units], dtype=float).reshape(len(units), len(times))


def paired_permutation_p(pre: np.ndarray, post: np.ndarray, rng, n: int = PERMUTATIONS,
                         tail: str = "two-sided") -> np.ndarray:
    """Permutation test of post against pre, paired by trial, for each row.

    The sign of each trial's difference is permuted. With the sum of squares
    fixed, the paired t statistic is a monotonic function of the mean
    difference, so the mean difference is used as the statistic.
    `tail="greater"` tests post > pre.
    """
    d = post - pre
    signs = rng.choice([-1.0, 1.0], size=(n, d.shape[1]))
    observed = d.sum(axis=1, keepdims=True)
    permuted = d @ signs.T
    if tail == "greater":
        extreme = permuted >= observed - 1e-9
    else:
        extreme = np.abs(permuted) >= np.abs(observed) - 1e-9
    return (1 + extreme.sum(axis=1)) / (n + 1)


def two_sample_permutation_p(a: np.ndarray, b: np.ndarray, rng, n: int = PERMUTATIONS) -> np.ndarray:
    """One-sided permutation test that the mean of a exceeds the mean of b, for each row.

    Condition labels are permuted across the trials of both groups. With the
    pooled sum of squares fixed, the two-sample t statistic is a monotonic
    function of the difference of means, which is used as the statistic.
    """
    both = np.concatenate([a, b], axis=1)
    na, nb = a.shape[1], b.shape[1]
    in_a = np.zeros((n, na + nb))
    for row in in_a:
        row[rng.choice(na + nb, size=na, replace=False)] = 1.0
    total = both.sum(axis=1, keepdims=True)
    sum_a = both @ in_a.T
    permuted = sum_a / na - (total - sum_a) / nb
    observed = a.mean(axis=1, keepdims=True) - b.mean(axis=1, keepdims=True)
    return (1 + (permuted >= observed - 1e-9).sum(axis=1)) / (n + 1)


# --- boundary cells and event cells -------------------------------------------

def boundary_times(encoding: pd.DataFrame, soft: str = "authors") -> tuple:
    """Alignment times and their condition labels for one session.

    NB clips are aligned to their middle (4 s, stored as boundary1) and HB
    clips to the hard boundary. For soft boundaries:

    - `soft="authors"`: every soft boundary, in SB clips and in HB clips, 75
      per session. This is the set the authors' published plotting code builds
      (B01_raster_psth_encoding_BAligned_BSep_NWB.m, lines 29 to 37).
    - `soft="first"`: the first soft boundary of each SB clip, 30 per session.
    - `soft="all"`: every soft boundary of the SB clips, 50 per session.
    """
    times, kinds = [], []
    for row in encoding.itertuples():
        times.append(row.start_time + row.b1)
        kinds.append(row.kind)
        extra = []
        if (row.kind == "SB" and soft in ("all", "authors")) or (row.kind == "HB" and soft == "authors"):
            extra = [b for b in (row.b2, row.b3) if np.isfinite(b)]
        for b in extra:
            times.append(row.start_time + b)
            kinds.append("SB")
    return np.array(times), np.array(kinds)


def response_tests(pre: np.ndarray, post: np.ndarray, kinds: np.ndarray, rng,
                   n: int = PERMUTATIONS) -> dict:
    """The six p-values the cell definitions use, for each unit of one session."""
    p = {}
    for kind in KINDS:
        m = kinds == kind
        p[f"{kind} post vs pre"] = paired_permutation_p(pre[:, m], post[:, m], rng, n)
    for a, b in (("SB", "NB"), ("HB", "NB"), ("HB", "SB")):
        p[f"{a} > {b}"] = two_sample_permutation_p(post[:, kinds == a], post[:, kinds == b], rng, n)
    return p


def classify(p: dict, alpha: float = ALPHA) -> tuple:
    """Boundary cells and event cells from the p-values of `response_tests`.

    Boundary cell (Methods): the count after the boundary differs from the
    count before for SB and for HB but not for NB, and the count after the
    boundary is greater for SB than NB and for HB than NB.
    Event cell: it differs for HB but not for NB or SB, and the count after
    the boundary is greater for HB than NB and for HB than SB.
    """
    boundary = ((p["SB post vs pre"] < alpha) & (p["HB post vs pre"] < alpha)
                & (p["NB post vs pre"] >= alpha)
                & (p["SB > NB"] < alpha) & (p["HB > NB"] < alpha))
    event = ((p["HB post vs pre"] < alpha) & (p["NB post vs pre"] >= alpha)
             & (p["SB post vs pre"] >= alpha)
             & (p["HB > NB"] < alpha) & (p["HB > SB"] < alpha))
    return boundary, event


def find_cells(session: Session, rng, soft: str = "authors", alpha: float = ALPHA,
               n: int = PERMUTATIONS) -> pd.DataFrame:
    """One row per unit of a session: its region, the six p-values and the two labels."""
    times, kinds = boundary_times(session.encoding, soft)
    pre = spike_counts(session.units, times, -WINDOW, 0.0)
    post = spike_counts(session.units, times, 0.0, WINDOW)
    p = response_tests(pre, post, kinds, rng, n)
    boundary, event = classify(p, alpha)
    out = pd.DataFrame(p)
    out.insert(0, "subject", session.subject)
    out.insert(1, "unit", np.arange(len(session.units)))
    out.insert(2, "region", session.region)
    out["boundary"], out["event"] = boundary, event
    return out


def find_cells_pooled(session: Session, rng, soft: str = "authors", alpha: float = ALPHA,
                      n: int = PERMUTATIONS) -> pd.DataFrame:
    """A looser reading of the two definitions, for comparison only.

    Boundary cell: the count after the boundary differs from the count before
    over SB and HB trials taken together but not over NB trials, and the count
    after the boundary is greater over SB and HB trials together than over NB
    trials. Event cell: it differs over HB trials but not over NB and SB
    trials together, and is greater over HB trials than over NB and SB trials
    together. Three tests each, where `classify` uses five.
    """
    times, kinds = boundary_times(session.encoding, soft)
    pre = spike_counts(session.units, times, -WINDOW, 0.0)
    post = spike_counts(session.units, times, 0.0, WINDOW)
    boundary, event = classify_pooled(pre, post, kinds, rng, alpha, n)
    return pd.DataFrame({"subject": session.subject, "unit": np.arange(len(session.units)),
                         "region": session.region, "boundary": boundary, "event": event})


def classify_pooled(pre: np.ndarray, post: np.ndarray, kinds: np.ndarray, rng, alpha: float = ALPHA,
                    n: int = PERMUTATIONS) -> tuple:
    """The labels of `find_cells_pooled` from spike counts before and after each boundary."""
    nb, hb = kinds == "NB", kinds == "HB"
    cut, rest = ~nb, ~hb
    boundary = ((paired_permutation_p(pre[:, cut], post[:, cut], rng, n) < alpha)
                & (paired_permutation_p(pre[:, nb], post[:, nb], rng, n) >= alpha)
                & (two_sample_permutation_p(post[:, cut], post[:, nb], rng, n) < alpha))
    event = ((paired_permutation_p(pre[:, hb], post[:, hb], rng, n) < alpha)
             & (paired_permutation_p(pre[:, rest], post[:, rest], rng, n) >= alpha)
             & (two_sample_permutation_p(post[:, hb], post[:, rest], rng, n) < alpha))
    return boundary, event


def chance_counts(sessions: list, rng, shuffles: int, soft: str = "authors", n: int = PERMUTATIONS,
                  alpha: float = ALPHA, pooled: bool = False) -> pd.DataFrame:
    """Cells selected after shuffling the condition labels of each session's boundaries.

    One row per shuffle; columns are the number of boundary and event cells in
    each region and overall. This is the paper's chance-level procedure with
    `shuffles` repetitions (the paper used 1000). With `pooled`, the cells are
    selected by the looser reading of `find_cells_pooled`.
    """
    prepared = []
    for s in sessions:
        times, kinds = boundary_times(s.encoding, soft)
        prepared.append((s.region, kinds, spike_counts(s.units, times, -WINDOW, 0.0),
                         spike_counts(s.units, times, 0.0, WINDOW)))
    rows = []
    for _ in range(shuffles):
        row = {f"{label} {region}": 0 for label in ("boundary", "event") for region in REGIONS}
        for region, kinds, pre, post in prepared:
            shuffled = rng.permutation(kinds)
            if pooled:
                boundary, event = classify_pooled(pre, post, shuffled, rng, alpha, n)
            else:
                boundary, event = classify(response_tests(pre, post, shuffled, rng, n), alpha)
            for r in REGIONS:
                row[f"boundary {r}"] += int(boundary[region == r].sum())
                row[f"event {r}"] += int(event[region == r].sum())
        for label in ("boundary", "event"):
            row[f"{label} all"] = sum(row[f"{label} {r}"] for r in REGIONS)
        rows.append(row)
    return pd.DataFrame(rows)


# --- firing-rate traces -------------------------------------------------------

def rate_trace(spikes: np.ndarray, times: np.ndarray, centres: np.ndarray,
               width: float = PSTH_WIDTH) -> np.ndarray:
    """Trial-averaged firing rate (Hz) in a window of `width` centred on each of `centres`."""
    lo = np.searchsorted(spikes, times[:, None] + centres[None, :] - width / 2)
    hi = np.searchsorted(spikes, times[:, None] + centres[None, :] + width / 2)
    return (hi - lo).mean(axis=0) / width


def peak_time(spikes: np.ndarray, times: np.ndarray, search=(0.0, 1.0), step: float = 0.002) -> float:
    """Time after the events at which the trial-averaged rate trace is highest.

    NaN if the unit fires no spike in the search window. When several window
    positions share the maximum, the middle of the first run of them is used.
    """
    centres = np.arange(search[0], search[1] + step / 2, step)
    trace = rate_trace(spikes, times, centres)
    if trace.max() == 0:
        return np.nan
    at_max = np.flatnonzero(trace == trace.max())
    breaks = np.flatnonzero(np.diff(at_max) > 1)
    run = at_max[: breaks[0] + 1] if len(breaks) else at_max
    return float(centres[run].mean())


def onset_locking(session: Session, lags: np.ndarray, width: float = 0.5) -> np.ndarray:
    """How strongly spiking changes at clip onset if the spike clock were shifted by each lag.

    For each unit and lag, z = (after - before) / sqrt(after + before), where
    after and before are the spike counts, summed over clips, in `width`
    seconds after and before (clip onset + lag). Returns the mean |z| over
    units for each lag. A session whose spikes share the clock of the trial
    table has its peak a few hundred milliseconds after lag zero.
    """
    onsets = session.encoding.start_time.to_numpy()
    total = np.zeros(len(lags))
    used = 0
    for u in session.units:
        t = onsets[:, None] + lags[None, :]
        mid = np.searchsorted(u, t)
        after = (np.searchsorted(u, t + width) - mid).sum(axis=0)
        before = (mid - np.searchsorted(u, t - width)).sum(axis=0)
        n = after + before
        if n.max() == 0:
            continue
        total += np.abs(after - before) / np.sqrt(np.maximum(n, 1))
        used += 1
    return total / max(used, 1)


def clip_population_trace(sessions: list, edges: np.ndarray) -> pd.DataFrame:
    """How far the population's firing in each clip departs from the average clip, over clip time.

    For each unit, spikes are counted in the bins `edges` (s after clip onset)
    of every clip. The unit's mean count over the 90 clips is subtracted in
    each bin, and the result divided by the unit's standard deviation over
    clips (averaged over bins). These are summed over units and divided by
    the square root of the number of units, which gives roughly a z-score per
    clip and bin if units were independent. One row per clip, one column per
    bin centre.
    """
    clips = sorted(sessions[0].encoding["clip"])
    total = np.zeros((len(clips), len(edges) - 1))
    used = 0
    for s in sessions:
        onset = s.encoding.set_index("clip").start_time.loc[clips].to_numpy()
        for u in s.units:
            counts = np.array([np.histogram(u - t, bins=edges)[0] for t in onset], dtype=float)
            sd = counts.std(axis=0).mean()
            if sd == 0:
                continue
            total += (counts - counts.mean(axis=0)) / sd
            used += 1
    centres = np.round((edges[:-1] + edges[1:]) / 2, 3)
    return pd.DataFrame(total / np.sqrt(used), index=clips, columns=centres)


# --- state space --------------------------------------------------------------

def smoothed_trials(session: Session, units: np.ndarray | None = None) -> tuple:
    """Smoothed, z-scored activity of each unit around each clip's alignment time.

    For each clip, spikes are counted in 10 ms bins from 1 s before clip onset
    to 8 s after it, smoothed with a 200 ms Gaussian kernel and z-scored over
    that trial (a unit silent for the whole trial is set to zero). The part
    from STATE_BEFORE before to STATE_AFTER after the alignment time (the
    first boundary, or the middle of an NB clip) is returned.

    Returns (clip names, array of shape (units, clips, bins)).
    """
    enc = session.encoding
    edges = np.arange(-TRIAL_BEFORE, TRIAL_AFTER + BIN / 2, BIN)
    n_keep = int(round((STATE_BEFORE + STATE_AFTER) / BIN))
    chosen = range(len(session.units)) if units is None else units
    out = np.zeros((len(chosen), len(enc), n_keep), dtype=np.float32)
    first = np.round((TRIAL_BEFORE + enc.b1.to_numpy() - STATE_BEFORE) / BIN).astype(int)
    starts = enc.start_time.to_numpy()
    for i, u in enumerate(chosen):
        spikes = session.units[u]
        for j, t0 in enumerate(starts):
            a, b = np.searchsorted(spikes, [t0 + edges[0], t0 + edges[-1]])
            counts = np.histogram(spikes[a:b] - t0, bins=edges)[0].astype(float)
            rate = gaussian_filter1d(counts, SMOOTH_SD / BIN, mode="nearest")
            sd = rate.std()
            if sd > 0:
                z = (rate - rate.mean()) / sd
                out[i, j] = z[first[j]: first[j] + n_keep]
    return enc["clip"].to_numpy(), out


def state_times() -> np.ndarray:
    """Bin centres (s, relative to the alignment time) of the arrays of `smoothed_trials`."""
    n_keep = int(round((STATE_BEFORE + STATE_AFTER) / BIN))
    return -STATE_BEFORE + BIN * (np.arange(n_keep) + 0.5)


def pseudopopulation(per_session: list) -> tuple:
    """Stack sessions into pseudo-trials by clip name. Returns (clips, kinds, (clips, units, bins))."""
    clips = sorted(per_session[0][0])
    stacked = []
    for names, data in per_session:
        order = pd.Series(np.arange(len(names)), index=names).loc[clips].to_numpy()
        stacked.append(data[:, order])
    data = np.concatenate(stacked, axis=0).transpose(1, 0, 2)
    return np.array(clips), np.array([c[:2] for c in clips]), data


def distance_from_boundary(data: np.ndarray, kinds: np.ndarray, variance: float = VARIANCE) -> dict:
    """Multidimensional distance from the state at the alignment time.

    `data` has shape (trials, units, bins). Principal components are fitted on
    the three condition averages (bins of all three as samples, units as
    variables) and the first components that explain `variance` are kept.

    Returns the number of components, the distance over time of each
    condition's average trajectory ("average"), and of every single trial
    projected on the same components ("trials", shape (trials, bins)).
    """
    times = state_times()
    zero = int(np.argmin(np.abs(times)))        # the bin that starts at the alignment time
    means = np.stack([data[kinds == k].mean(axis=0) for k in KINDS])       # (3, units, bins)
    samples = means.transpose(0, 2, 1).reshape(-1, data.shape[1])           # (3 * bins, units)
    centre = samples.mean(axis=0)
    _, s, vt = np.linalg.svd(samples - centre, full_matrices=False)
    explained = np.cumsum(s ** 2) / np.sum(s ** 2)
    n = int(np.searchsorted(explained, variance) + 1)
    axes = vt[:n]                                                            # (n, units)

    def distance(trajectory):                    # (units, bins) -> (bins,)
        projected = axes @ (trajectory - centre[:, None])
        return np.linalg.norm(projected - projected[:, [zero]], axis=0)

    return {
        "components": n,
        "explained by first three": explained[2] if len(explained) > 2 else np.nan,
        "average": {k: distance(means[i]) for i, k in enumerate(KINDS)},
        "trials": np.array([distance(trial) for trial in data]),
    }
