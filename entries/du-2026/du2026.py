"""Loading and estimators for the attempt on Du, Lai, Hu & Ye (2026).

Paper: "A Context-Conditional Audit of Trial-Pairing-Dependent Neural Gain in
Motor-Cortex Decoding", bioRxiv doi:10.64898/2026.08.04.742876.
Datasets: DANDI:001201 (LINK) and DANDI:000129 (MC_RTT), streamed at the
versions the paper cites (Methods 4.2, Data availability).

Every estimator here is a port of the paper's own code, the release named in
its Code availability section: github.com/gwkuqgfkqe/neural-decoder-context-audit,
tag v1.0-jne-submission, commit b042fbe1cda2ca5a353751c693d7c95f45de0456
(BSD 3-Clause, copyright the paper's authors). The file and function each
port comes from is named in its docstring, so that a verifier can compare
them. Parameters come from the claims file's criteria (which cite the
Methods or that code), from the passage of the paper named where they are
set, or are marked as a standard choice that cannot change a result.
The ports read the NWB files by streaming them (remfile + h5py) and keep
the arithmetic of the original: the same Ridge pipelines, the same
scikit-learn splitters and the same random_state offsets.
"""

from __future__ import annotations

import json
import re
import urllib.request
from dataclasses import dataclass
from decimal import ROUND_HALF_UP, Decimal

import h5py
import numpy as np
import pandas as pd
import remfile
from sklearn.kernel_approximation import RBFSampler
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import StratifiedKFold, train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

API = "https://api.dandiarchive.org/api"
LINK_ID = "001201"
LINK_VERSION = "0.251023.2336"  # Methods 4.2 and Data availability
RTT_ID = "000129"
RTT_VERSION = "0.241017.1444"  # Methods 4.2 and Data availability
RTT_TRAIN_PATH = "sub-Indy/sub-Indy_desc-train_behavior+ecephys.nwb"

PAPER_CODE = "https://github.com/gwkuqgfkqe/neural-decoder-context-audit"
PAPER_COMMIT = "b042fbe1cda2ca5a353751c693d7c95f45de0456"

# Methods 4.5: penalty grid
ALPHA_GRID = (0.1, 1.0, 10.0, 100.0, 1000.0, 10000.0, 100000.0)
# run_primary_analyses.py SEEDS; Results 2.7 (three split seeds)
SPLIT_SEEDS = (20260726, 20260727, 20260728)
# Methods 4.6 and run_nonlinear_seed_sensitivity.py RFF_SEEDS
RFF_SEEDS = (20260802, 20260803, 20260804)
LADDER = ("phase_only", "condition_phase", "geometry_additive", "geometry_tensor", "causal_history")
LADDER_NAMES = {
    "phase_only": "phase only",
    "condition_phase": "direction by phase",
    "geometry_additive": "additive geometry",
    "geometry_tensor": "geometry by phase",
    "causal_history": "plus measured-output history",
    "geometry_quadratic": "quadratic geometry",
    "causal_history_quadratic": "quadratic plus history",
}


# --------------------------------------------------------------------------
# Archive access


def _get_json(url: str) -> dict:
    with urllib.request.urlopen(url, timeout=120) as response:
        return json.load(response)


def list_assets(dandiset: str, version: str) -> list[dict]:
    """Every asset of a published version, from the DANDI REST API."""
    url = f"{API}/dandisets/{dandiset}/versions/{version}/assets/?page_size=1000"
    out: list[dict] = []
    while url:
        page = _get_json(url)
        out.extend(page["results"])
        url = page["next"]
    return out


def asset_metadata(dandiset: str, version: str, asset_id: str) -> dict:
    return _get_json(f"{API}/dandisets/{dandiset}/versions/{version}/assets/{asset_id}/")


def s3_url(asset_id: str) -> str:
    """The asset's S3 address, from its contentUrl metadata."""
    urls = _get_json(f"{API}/assets/{asset_id}/")["contentUrl"]
    return next(u for u in urls if "s3" in u and "amazonaws.com" in u)


def open_h5(asset_id: str) -> h5py.File:
    """Stream one NWB file (no download to disk)."""
    return h5py.File(remfile.File(s3_url(asset_id)), "r")


# --------------------------------------------------------------------------
# LINK


def session_date(path: str) -> str:
    value = re.search(r"ses-(\d{8})", path).group(1)
    return f"{value[:4]}-{value[4:6]}-{value[6:]}"


def link_task_from_metadata(metadata: dict) -> str:
    """Target style from the asset metadata (build_link_confirmation_manifest.py, _task)."""
    for activity in metadata.get("wasGeneratedBy", []):
        match = re.search(r"target style\s+(CO|RD)", str(activity.get("description", "")))
        if match:
            return match.group(1)
    raise ValueError(f"No target style in metadata for {metadata.get('identifier')}")


def interior_ranks(n_items: int, n_select: int = 10) -> list[int]:
    """Half-up ranks nearest j/11 (build_link_confirmation_manifest.py, _interior_ranks; Methods 4.2)."""
    ranks = []
    for index in range(1, n_select + 1):
        raw = Decimal(index) * Decimal(n_items - 1) / Decimal(n_select + 1)
        ranks.append(int(raw.quantize(Decimal("1"), rounding=ROUND_HALF_UP)))
    return ranks


def _read_trials(h5: h5py.File) -> pd.DataFrame:
    group = h5["intervals/trials"]
    columns = {}
    for name in group:
        dataset = group[name]
        if not isinstance(dataset, h5py.Dataset) or name in {"id", "timeseries", "timeseries_index"}:
            continue
        values = dataset[:]
        if values.dtype.kind in "SO":
            values = np.array([v.decode() if isinstance(v, bytes) else str(v) for v in values])
        columns[name] = values
    frame = pd.DataFrame(columns)
    frame.index = group["id"][:]
    return frame


@dataclass
class LinkSession:
    asset_id: str
    path: str
    identifier: str
    date: str
    task: str
    timestamps: np.ndarray
    signals: dict
    position: np.ndarray
    velocity: np.ndarray
    trials: pd.DataFrame
    units: dict


def load_link_session(asset_id: str, path: str, signals=("SpikingBandPower", "ThresholdCrossings")) -> LinkSession:
    """Read the arrays link.py reads (load_link): the 20 ms SBP/TCR series in the
    NWB analysis module, index and MRS position and velocity, and the trials table."""
    with open_h5(asset_id) as h5:
        identifier = h5["identifier"][()]
        identifier = identifier.decode() if isinstance(identifier, bytes) else str(identifier)
        analysis = h5["analysis"]
        timestamps = analysis[signals[0]]["timestamps"][:].astype(float)
        data = {s: analysis[s]["data"][:].astype(np.float32) for s in signals}
        for s in signals:
            if not np.array_equal(analysis[s]["timestamps"][:].astype(float), timestamps):
                raise AssertionError(f"{s} timestamps differ from {signals[0]}")
        position = np.concatenate(
            [analysis["index_position"]["data"][:], analysis["mrs_position"]["data"][:]], axis=1
        ).astype(np.float32)
        velocity = np.concatenate(
            [analysis["index_velocity"]["data"][:], analysis["mrs_velocity"]["data"][:]], axis=1
        ).astype(np.float32)
        units = {}
        for name in ("SpikingBandPower", "ThresholdCrossings", "index_position", "index_velocity"):
            if name in analysis:
                units[name] = analysis[name]["data"].attrs.get("unit")
                if isinstance(units[name], bytes):
                    units[name] = units[name].decode()
        # position/velocity share the clock of the neural series
        for name in ("index_position", "index_velocity", "mrs_position", "mrs_velocity"):
            if not np.allclose(analysis[name]["timestamps"][:], timestamps):
                raise AssertionError(f"{name} timestamps differ from the neural series")
        trials = _read_trials(h5)
    date, task, _ = identifier.rsplit("_", 2)
    return LinkSession(asset_id, path, identifier, date, task, timestamps, data, position, velocity, trials, units)


def _direction_octant(displacement: np.ndarray) -> int:
    """link.py _direction_octant."""
    angle = np.arctan2(displacement[1], displacement[0])
    return int(np.floor(((angle + np.pi) / (2.0 * np.pi)) * 8)) % 8


def phase_basis(n_time: int, n_harmonics: int = 4) -> np.ndarray:
    """1, sin(r pi tau), cos(r pi tau), r = 1..4 (Methods 4.4; link.py _phase_basis)."""
    phase = np.linspace(0.0, 1.0, n_time, endpoint=False)
    features = [np.ones_like(phase)]
    for harmonic in range(1, n_harmonics + 1):
        features.extend([np.sin(harmonic * np.pi * phase), np.cos(harmonic * np.pi * phase)])
    return np.stack(features, axis=-1)


@dataclass
class TrialDataset:
    neural: np.ndarray
    context: np.ndarray
    behavior: np.ndarray
    condition: np.ndarray
    train_indices: np.ndarray
    test_indices: np.ndarray
    source_rows: np.ndarray | None = None  # row of the NWB trials table, per usable trial


def build_link_dataset(
    session: LinkSession,
    *,
    signal: str = "SpikingBandPower",
    context_mode: str = "geometry_tensor",
    movement_window_ms: int = 500,
    neural_history_ms: int = 160,
    neural_lead_ms: int = 0,
    output_history_ms: int = 100,
    output_lead_ms: int = 0,
    sample_offset_ms: int | None = None,
    seed: int = 20260726,
    test_size: float = 0.30,
) -> TrialDataset:
    """Port of link.py load_link, from arrays already streamed.

    Defaults are those every LINK run script passes (run_link_context_ladder.py,
    run_primary_analyses.py, run_link_confirmation.py): SBP, 160 ms history
    ending at the behavior bin (lead 0), 100 ms position history (lead 0),
    25 bins of 20 ms (Methods 4.3), 70/30 split stratified by direction
    octant with random_state=seed (Methods 4.5).
    """
    bin_ms = 20
    n_time = movement_window_ms // bin_ms
    history_bins = neural_history_ms // bin_ms
    lead_bins = neural_lead_ms // bin_ms
    out_hist = output_history_ms // bin_ms
    out_lead = output_lead_ms // bin_ms
    warmup = max(history_bins + lead_bins, out_hist + out_lead)
    offset = warmup if sample_offset_ms is None else sample_offset_ms // bin_ms
    if offset < warmup:
        raise ValueError("sample offset must accommodate all history and lead bins")
    basis = phase_basis(n_time)
    timestamps = session.timestamps
    data = session.signals[signal]
    position = session.position
    velocity = session.velocity

    neural_trials, context_trials, behavior_trials, conditions, rows = [], [], [], [], []
    for row_index, row in enumerate(session.trials.itertuples()):
        start_index = int(np.argmin(np.abs(timestamps - float(row.start_time))))
        sample_start = start_index + offset
        samples = np.arange(sample_start, sample_start + n_time)
        stop_index = start_index + int(row.trial_count)
        if samples[-1] >= min(stop_index, len(timestamps)):
            continue
        neural_trial = np.stack(
            [data[b - lead_bins - history_bins : b - lead_bins].reshape(-1) for b in samples]
        )
        behavior_trial = velocity[samples]
        initial = position[start_index].astype(float)
        target = np.array([float(row.index_target_position), float(row.mrs_target_position)])
        displacement = target - initial
        condition = _direction_octant(displacement)
        one_hot = np.repeat(np.eye(8)[condition][None, :], n_time, axis=0)
        condition_phase = (one_hot[:, :, None] * basis[:, None, :]).reshape(n_time, -1)
        geometry = np.repeat(np.concatenate([target, initial, displacement])[None, :], n_time, axis=0)
        geometry_phase = (geometry[:, :, None] * basis[:, None, :]).reshape(n_time, -1)
        parts = [basis]
        if context_mode != "phase_only":
            parts.insert(0, condition_phase)
        if context_mode in {"geometry_additive", "geometry_tensor", "geometry_quadratic", "causal_history", "causal_history_quadratic"}:
            parts.append(geometry)
        if context_mode in {"geometry_tensor", "geometry_quadratic", "causal_history", "causal_history_quadratic"}:
            parts.append(geometry_phase)
        if context_mode in {"geometry_quadratic", "causal_history_quadratic"}:
            quadratic = np.stack(
                [geometry[:, a] * geometry[:, b] for a in range(6) for b in range(a, 6)], axis=-1
            )
            parts.extend([quadratic, (quadratic[:, :, None] * basis[:, None, :]).reshape(n_time, -1)])
        if context_mode in {"causal_history", "causal_history_quadratic"}:
            parts.append(
                np.stack([position[b - out_lead - out_hist : b - out_lead].reshape(-1) for b in samples])
            )
        neural_trials.append(neural_trial)
        context_trials.append(np.concatenate(parts, axis=-1))
        behavior_trials.append(behavior_trial)
        conditions.append(np.full(n_time, condition, dtype=int))
        rows.append(row_index)

    condition = np.stack(conditions)
    indices = np.arange(len(neural_trials))
    train, test = train_test_split(indices, test_size=test_size, random_state=seed, stratify=condition[:, 0])
    return TrialDataset(
        neural=np.stack(neural_trials),
        context=np.stack(context_trials).astype(float),
        behavior=np.stack(behavior_trials),
        condition=condition,
        train_indices=np.asarray(train, dtype=int),
        test_indices=np.asarray(test, dtype=int),
        source_rows=np.asarray(rows),
    )


# --------------------------------------------------------------------------
# MC_RTT


def _downsample_mean(data: np.ndarray, samples_per_bin: int) -> np.ndarray:
    usable = data.shape[0] - (data.shape[0] % samples_per_bin)
    return data[:usable].reshape(-1, samples_per_bin, data.shape[-1]).mean(axis=1)


def _rtt_octant(target_error: np.ndarray) -> int:
    mean_error = target_error.mean(axis=0)
    angle = np.arctan2(mean_error[1], mean_error[0])
    return int(np.floor(((angle + np.pi) / (2 * np.pi)) * 8)) % 8


@dataclass
class RttRaw:
    finger_vel: np.ndarray
    cursor_pos: np.ndarray
    target_pos: np.ndarray
    behavior_timestamps_head: np.ndarray
    behavior_rate: float | None
    spike_counts: np.ndarray
    n_units: int
    trials: pd.DataFrame
    n_bins: int
    descriptions: dict


def load_rtt_raw(asset_id: str, bin_ms: int = 20) -> RttRaw:
    """Arrays mc_rtt.py load_mc_rtt reads: finger_vel, cursor_pos, target_pos
    (1 kHz, averaged into 20 ms bins), spike times histogrammed on the same grid
    (Methods 4.3), and the trials table with its split column."""
    with open_h5(asset_id) as h5:
        behavior = h5["processing/behavior"]
        descriptions = {}

        def series(name):
            group = behavior[name]
            if "data" not in group:
                group = group[next(iter(group))]
            descriptions[name] = {
                "unit": group["data"].attrs.get("unit"),
                "conversion": group["data"].attrs.get("conversion"),
                "description": group.attrs.get("description"),
            }
            if "timestamps" in group:
                ts = group["timestamps"][:5]
                rate = None
            else:
                ts = np.array([group["starting_time"][()]])
                rate = group["starting_time"].attrs.get("rate")
            return group["data"][:].astype(float), ts, rate

        fv, ts_head, rate = series("finger_vel")
        cp, _, _ = series("cursor_pos")
        tp, _, _ = series("target_pos")
        finger_velocity = _downsample_mean(fv, bin_ms)
        cursor_position = _downsample_mean(cp, bin_ms)
        target_position = _downsample_mean(tp, bin_ms)
        n_bins = min(len(finger_velocity), len(cursor_position), len(target_position))
        edges = np.linspace(0.0, n_bins * bin_ms / 1000.0, n_bins + 1)
        index = h5["units/spike_times_index"][:]
        spike_times = h5["units/spike_times"][:]
        starts = np.concatenate([[0], index[:-1]])
        counts = np.stack(
            [np.histogram(spike_times[a:b], bins=edges)[0] for a, b in zip(starts, index)], axis=-1
        ).astype(np.float32)
        trials = _read_trials(h5)
    return RttRaw(finger_velocity, cursor_position, target_position, ts_head, rate, counts, counts.shape[1], trials, n_bins, descriptions)


def build_rtt_dataset(raw: RttRaw, *, bin_ms=20, neural_history_ms=100, neural_lead_ms=80,
                      output_history_ms=100, output_lead_ms=80, context_mode="causal_history") -> TrialDataset:
    """Port of mc_rtt.py load_mc_rtt. Defaults are run_primary_analyses.py _run_nlb:
    causal_history context, neural and output leads of 80 ms (Methods 4.3, 4.4);
    release split labels "train" and "val"."""
    history_bins = neural_history_ms // bin_ms
    lead_bins = neural_lead_ms // bin_ms
    out_hist = output_history_ms // bin_ms
    out_lead = output_lead_ms // bin_ms
    warmup = max(history_bins + lead_bins, out_hist + out_lead)
    neural_trials, context_trials, behavior_trials, conditions, labels, rows = [], [], [], [], [], []
    for row_index, row in enumerate(raw.trials.itertuples()):
        start_bin = int(round(float(row.start_time) * 1000.0 / bin_ms))
        stop_bin = int(round(float(row.stop_time) * 1000.0 / bin_ms))
        samples = np.arange(start_bin + warmup, stop_bin)
        if samples.size == 0 or samples[-1] >= raw.n_bins:
            continue
        neural_trial = np.stack([raw.spike_counts[b - lead_bins - history_bins : b - lead_bins].reshape(-1) for b in samples])
        target = raw.target_pos[samples]
        cursor = raw.cursor_pos[samples]
        error = target - cursor
        if context_mode == "target_only":
            context = target
        elif context_mode == "task_state":
            context = np.concatenate([target, cursor, error], axis=-1)
        else:
            history = np.stack([raw.cursor_pos[b - out_lead - out_hist : b - out_lead].reshape(-1) for b in samples])
            context = np.concatenate([target, history, target - history[:, -2:]], axis=-1)
        neural_trials.append(neural_trial)
        context_trials.append(context)
        behavior_trials.append(raw.finger_vel[samples])
        conditions.append(np.full(samples.size, _rtt_octant(error), dtype=int))
        labels.append(str(row.split))
        rows.append(row_index)
    labels = np.asarray(labels)
    return TrialDataset(
        neural=np.stack(neural_trials),
        context=np.stack(context_trials),
        behavior=np.stack(behavior_trials),
        condition=np.stack(conditions),
        train_indices=np.flatnonzero(labels == "train"),
        test_indices=np.flatnonzero(labels == "val"),
        source_rows=np.asarray(rows),
    )


# --------------------------------------------------------------------------
# MC_Maze (data elsewhere: DANDI:000139, the version the claims file names)

MAZE_ID = "000139"
MAZE_VERSION = "0.220113.0408"  # claims file, maze-gain "where"
MAZE_TRAIN_PATH = "sub-Jenkins/sub-Jenkins_ses-medium_desc-train_behavior+ecephys.nwb"


def _bin_timestamped_mean(data: np.ndarray, timestamps: np.ndarray, bin_edges: np.ndarray) -> np.ndarray:
    """mc_maze.py _bin_timestamped_mean: mean of the samples whose timestamps fall in each bin."""
    n_bins = len(bin_edges) - 1
    bin_index = np.searchsorted(bin_edges, timestamps, side="right") - 1
    valid = (bin_index >= 0) & (bin_index < n_bins)
    sums = np.zeros((n_bins, data.shape[-1]), dtype=float)
    counts = np.zeros(n_bins, dtype=int)
    np.add.at(sums, bin_index[valid], data[valid])
    np.add.at(counts, bin_index[valid], 1)
    output = np.full_like(sums, np.nan, dtype=float)
    populated = counts > 0
    output[populated] = sums[populated] / counts[populated, None]
    return output


@dataclass
class MazeRaw:
    hand_vel: np.ndarray
    cursor_pos: np.ndarray
    spike_counts: np.ndarray
    n_units: int
    heldout: np.ndarray
    trials: pd.DataFrame
    target_pos: list
    n_bins: int
    descriptions: dict


def load_maze_raw(asset_id: str, bin_ms: int = 20) -> MazeRaw:
    """Arrays mc_maze.py load_mc_maze reads: hand_vel and cursor_pos (stored
    values, as pynwb's data[:] returns them), averaged into 20 ms bins on a grid
    from 0 to the last trial stop_time, every unit's spike times histogrammed on
    the same grid, and the trials table with its ragged target_pos column."""
    with open_h5(asset_id) as h5:
        behavior = h5["processing/behavior"]
        descriptions = {name: {"unit": behavior[name]["data"].attrs.get("unit"),
                               "conversion": behavior[name]["data"].attrs.get("conversion"),
                               "description": behavior[name].attrs.get("description")}
                        for name in ("hand_vel", "cursor_pos")}
        group = h5["intervals/trials"]
        trials = pd.DataFrame({name: group[name][:] for name in
                               ("start_time", "stop_time", "move_onset_time", "trial_type", "trial_version",
                                "active_target", "split", "success", "maze_id")})
        trials["split"] = [v.decode() if isinstance(v, bytes) else str(v) for v in trials["split"]]
        target_index = group["target_pos_index"][:]
        target_data = group["target_pos"][:]
        target_pos = [target_data[a:b] for a, b in zip(np.concatenate([[0], target_index[:-1]]), target_index)]
        bin_seconds = bin_ms / 1000.0
        n_bins = int(np.ceil(float(trials.stop_time.max()) / bin_seconds))
        edges = np.arange(n_bins + 1, dtype=float) * bin_seconds
        hand_vel = _bin_timestamped_mean(behavior["hand_vel/data"][:], behavior["hand_vel/timestamps"][:], edges)
        cursor_pos = _bin_timestamped_mean(behavior["cursor_pos/data"][:], behavior["cursor_pos/timestamps"][:], edges)
        index = h5["units/spike_times_index"][:]
        spike_times = h5["units/spike_times"][:]
        starts = np.concatenate([[0], index[:-1]])
        counts = np.stack(
            [np.histogram(spike_times[a:b], bins=edges)[0] for a, b in zip(starts, index)], axis=-1
        ).astype(np.float32)
        heldout = h5["units/heldout"][:]
    return MazeRaw(hand_vel, cursor_pos, counts, counts.shape[1], heldout, trials, target_pos, n_bins, descriptions)


def build_maze_dataset(raw: MazeRaw, *, bin_ms=20, movement_window_ms=800, neural_history_ms=100,
                       neural_lead_ms=80, output_history_ms=100, output_lead_ms=None) -> TrialDataset:
    """Port of mc_maze.py load_mc_maze with context_mode "template", as
    run_primary_analyses.py _run_nlb calls it (neural_lead_ms=80): 40 bins from
    the bin nearest move_onset_time, five spike bins ending 80 ms before each
    behaviour bin, context = condition (trial_type, trial_version) one-hot by
    phase, phase basis, target, onset cursor position and their difference
    (Methods 4.3 and 4.4); release split labels "train" and "val"."""
    if output_lead_ms is None:
        output_lead_ms = neural_lead_ms
    n_time = movement_window_ms // bin_ms
    history_bins = neural_history_ms // bin_ms
    lead_bins = neural_lead_ms // bin_ms
    out_first = (output_lead_ms + output_history_ms) // bin_ms
    keys = sorted({(int(a), int(b)) for a, b in zip(raw.trials.trial_type, raw.trials.trial_version)})
    lookup = {k: i for i, k in enumerate(keys)}
    basis = phase_basis(n_time)
    neural_trials, context_trials, behavior_trials, conditions, labels, rows = [], [], [], [], [], []
    for row_index, row in enumerate(raw.trials.itertuples()):
        onset = int(round(float(row.move_onset_time) * 1000.0 / bin_ms))
        samples = np.arange(onset, onset + n_time)
        if (onset - lead_bins - history_bins < 0 or onset - out_first < 0 or samples[-1] >= raw.n_bins
                or float(row.stop_time) * 1000.0 < float(row.move_onset_time) * 1000.0 + movement_window_ms
                or not np.isfinite(raw.hand_vel[samples]).all() or not np.isfinite(raw.cursor_pos[onset]).all()):
            continue
        neural_trials.append(np.stack([raw.spike_counts[b - lead_bins - history_bins:b - lead_bins].reshape(-1)
                                       for b in samples]))
        c = lookup[(int(row.trial_type), int(row.trial_version))]
        one_hot = np.zeros(len(keys))
        one_hot[c] = 1.0
        condition_phase = (one_hot[None, :, None] * basis[:, None, :]).reshape(n_time, -1)
        targets = np.asarray(raw.target_pos[row_index]).reshape(-1, 2)
        if not 0 <= int(row.active_target) < len(targets):
            raise ValueError(f"active_target {row.active_target} for {len(targets)} targets")
        target = targets[int(row.active_target)].astype(float)
        cursor = raw.cursor_pos[onset].astype(float)
        geometry = np.repeat(np.concatenate([target, cursor, target - cursor])[None, :], n_time, axis=0)
        context_trials.append(np.concatenate([condition_phase, basis, geometry], axis=-1))
        behavior_trials.append(raw.hand_vel[samples])
        conditions.append(np.full(n_time, c, dtype=int))
        labels.append(str(row.split))
        rows.append(row_index)
    labels = np.asarray(labels)
    return TrialDataset(
        neural=np.stack(neural_trials),
        context=np.stack(context_trials),
        behavior=np.stack(behavior_trials),
        condition=np.stack(conditions),
        train_indices=np.flatnonzero(labels == "train"),
        test_indices=np.flatnonzero(labels == "val"),
        source_rows=np.asarray(rows),
    )


# --------------------------------------------------------------------------
# Synthetic generator (synthetic.py generate_synthetic_dataset; Methods 4.8)

SYNTHETIC_REGIMES = {
    "template_only": {"neural_innovation_strength": 0.0, "innovation_scale": 0.20},
    "weak": {"neural_innovation_strength": 0.8, "innovation_scale": 0.25},
    "strong": {"neural_innovation_strength": 1.8, "innovation_scale": 0.35},
}
SYNTHETIC_SEEDS = tuple(range(20260726, 20260736))


def generate_synthetic(*, seed, n_trials=480, n_time=60, n_conditions=8, n_neurons=48, template_scale=1.0,
                       innovation_scale=0.20, neural_innovation_strength=0.0, neural_noise=0.20) -> TrialDataset:
    """Port of synthetic.py generate_synthetic_dataset. neural_noise=0.20 is what
    run_synthetic_calibration.py passes (Methods 4.8, neural noise SD 0.20). The
    outer split is the estimator's own 70/30 condition-stratified split with
    random_state=seed (nested_estimators.py _resolve_split)."""
    rng = np.random.default_rng(seed)
    condition_per_trial = np.tile(np.arange(n_conditions), n_trials // n_conditions)
    rng.shuffle(condition_per_trial)
    phase = np.linspace(0.0, 1.0, n_time, endpoint=False)
    angles = 2.0 * np.pi * condition_per_trial / n_conditions
    directions = np.stack([np.cos(angles), np.sin(angles)], axis=-1)
    speed = np.sin(np.pi * phase) ** 1.5
    template = template_scale * directions[:, None, :] * speed[None, :, None]
    innovations = rng.normal(size=(n_trials, n_time, 2))
    residual = np.zeros_like(innovations)
    residual[:, 0] = innovations[:, 0]
    rho = 0.85
    for t in range(1, n_time):
        residual[:, t] = rho * residual[:, t - 1] + np.sqrt(1 - rho**2) * innovations[:, t]
    residual = innovation_scale * residual
    behavior = template + residual
    one_hot = np.eye(n_conditions)[condition_per_trial]
    phase_features = np.stack(
        [np.sin(np.pi * phase), np.cos(np.pi * phase), np.sin(2 * np.pi * phase), np.cos(2 * np.pi * phase), speed], axis=-1
    )
    rep_one_hot = np.repeat(one_hot[:, None, :], n_time, axis=1)
    rep_phase = np.repeat(phase_features[None], n_trials, axis=0)
    condition_phase = (rep_one_hot[:, :, :, None] * rep_phase[:, :, None, :]).reshape(n_trials, n_time, -1)
    context = np.concatenate([rep_one_hot, rep_phase, condition_phase], axis=-1)
    context_weights = rng.normal(scale=1.0 / np.sqrt(context.shape[-1]), size=(context.shape[-1], n_neurons))
    innovation_weights = rng.normal(scale=1.0 / np.sqrt(2), size=(2, n_neurons))
    neural = (
        np.einsum("ntc,cp->ntp", context, context_weights)
        + neural_innovation_strength * np.einsum("ntd,dp->ntp", residual, innovation_weights)
        + rng.normal(scale=neural_noise, size=(n_trials, n_time, n_neurons))
    )
    condition = np.repeat(condition_per_trial[:, None], n_time, axis=1)
    train, test = train_test_split(np.arange(n_trials), test_size=0.30, random_state=seed, stratify=condition[:, 0])
    return TrialDataset(neural, context, behavior, condition, np.asarray(train), np.asarray(test))


# --------------------------------------------------------------------------
# Estimators (estimators.py, nested_estimators.py, robustness_estimators.py,
# specification_estimators.py)


def _ridge(alpha: float):
    """estimators.py _ridge: StandardScaler then Ridge (Methods 4.5)."""
    return make_pipeline(StandardScaler(), Ridge(alpha=alpha))


def _flat(array: np.ndarray, idx: np.ndarray) -> np.ndarray:
    selected = array[idx]
    return selected.reshape(-1, selected.shape[-1])


def _vw_r2(y, p) -> float:
    return float(r2_score(y, p, multioutput="variance_weighted"))


def _select_alpha(xtr, ytr, xva, yva, grid=ALPHA_GRID) -> float:
    """estimators.py _select_ridge_alpha (first best on ties)."""
    best, best_score = grid[0], -np.inf
    for a in grid:
        score = _vw_r2(yva, _ridge(a).fit(xtr, ytr).predict(xva))
        if score > best_score:
            best, best_score = a, score
    return float(best)


def normalized_gain(y, context_prediction, candidate_prediction) -> float:
    """(MSE_C - MSE_C+X) / Var(Y), Results 2.1 and Methods 4.9 (specification_estimators.py _normalized_gain)."""
    variance = float(np.mean((y - y.mean(axis=0)) ** 2))
    return float((mean_squared_error(y, context_prediction) - mean_squared_error(y, candidate_prediction)) / variance)


def _inner_split(ds: TrialDataset, idx: np.ndarray, seed: int, size: float = 0.20):
    """nested_estimators.py _stratified_inner_split."""
    cond = ds.condition[idx, 0]
    _, counts = np.unique(cond, return_counts=True)
    strat = cond if counts.min() >= 2 else None
    a, b = train_test_split(idx, test_size=size, random_state=seed, stratify=strat)
    return np.asarray(a, dtype=int), np.asarray(b, dtype=int)


def _nuisance_alphas(ds, idx, seed):
    """nested_estimators.py _select_nuisance_alphas: separate penalties for
    context->behavior and context->neural on an inner 80/20 split (Methods 4.5, step 3)."""
    tr, va = _inner_split(ds, idx, seed)
    ctr, cva = _flat(ds.context, tr), _flat(ds.context, va)
    ca = _select_alpha(ctr, _flat(ds.behavior, tr), cva, _flat(ds.behavior, va))
    ra = _select_alpha(ctr, _flat(ds.neural, tr), cva, _flat(ds.neural, va))
    return ca, ra


def _nested_oof(ds, idx, seed, folds=5):
    """nested_estimators.py _fully_nested_nuisance_predictions (Methods 4.5, steps 1-4)."""
    cond = ds.condition[idx, 0]
    _, counts = np.unique(cond, return_counts=True)
    k = min(folds, int(counts.min()))
    splitter = StratifiedKFold(n_splits=k, shuffle=True, random_state=seed)
    bp = np.empty(ds.behavior[idx].shape, dtype=float)
    npred = np.empty(ds.neural[idx].shape, dtype=float)
    for fold, (ltr, lva) in enumerate(splitter.split(idx, cond)):
        ftr, fva = idx[ltr], idx[lva]
        ca, ra = _nuisance_alphas(ds, ftr, seed + 100 + fold)
        ctr, cva = _flat(ds.context, ftr), _flat(ds.context, fva)
        bp[lva] = _ridge(ca).fit(ctr, _flat(ds.behavior, ftr)).predict(cva).reshape(bp[lva].shape)
        npred[lva] = _ridge(ra).fit(ctr, _flat(ds.neural, ftr)).predict(cva).reshape(npred[lva].shape)
    return bp, npred, k


def _innovation_alpha(rx, ry, cond, seed, grid=ALPHA_GRID):
    """nested_estimators.py _select_grouped_innovation_alpha: three-fold whole-trial
    validation on out-of-fold residuals (Methods 4.5)."""
    _, counts = np.unique(cond, return_counts=True)
    splitter = StratifiedKFold(n_splits=min(3, int(counts.min())), shuffle=True, random_state=seed)
    scores = {float(a): [] for a in grid}
    for tr, va in splitter.split(np.arange(len(cond)), cond):
        xtr, ytr = rx[tr].reshape(-1, rx.shape[-1]), ry[tr].reshape(-1, ry.shape[-1])
        xva, yva = rx[va].reshape(-1, rx.shape[-1]), ry[va].reshape(-1, ry.shape[-1])
        for a in grid:
            scores[float(a)].append(_vw_r2(yva, _ridge(a).fit(xtr, ytr).predict(xva)))
    return max(scores, key=lambda a: (np.mean(scores[a]), -a))


def ranked_sources(ds: TrialDataset, n_ranks: int = 1):
    """robustness_estimators.py _ranked_replacement_sources (Methods 4.7): other
    test trials of the same condition, flattened context trajectories standardized
    with outer-training centers and scales, mean squared distance, ties to the
    lower trial index."""
    tr, te = ds.train_indices, ds.test_indices
    flat = ds.context.reshape(ds.context.shape[0], -1).astype(float)
    center, scale = flat[tr].mean(axis=0), flat[tr].std(axis=0)
    informative = scale > 1e-8
    z = np.zeros_like(flat)
    z[:, informative] = (flat[:, informative] - center[informative]) / scale[informative]
    cond = ds.condition[:, 0]
    sources = np.empty((n_ranks, len(te)), dtype=int)
    distances = np.empty((n_ranks, len(te)))
    for j, t in enumerate(te):
        cand = te[cond[te] == cond[t]]
        cand = cand[cand != t]
        d = np.mean((z[cand] - z[t]) ** 2, axis=1)
        order = np.lexsort((cand, d))[:n_ranks]
        sources[:, j] = cand[order]
        distances[:, j] = d[order]
    return sources, distances


def permutation_sources(test_indices, conditions, rng):
    """nested_estimators.py _permutation_sources: random ordering then a random
    cyclic shift within condition, no fixed points (Methods 4.7)."""
    sources = np.empty_like(test_indices)
    tc = conditions[test_indices]
    for c in np.unique(tc):
        pos = np.flatnonzero(tc == c)
        shuffled = rng.permutation(pos)
        shift = int(rng.integers(1, len(pos)))
        sources[shuffled] = test_indices[np.roll(shuffled, shift)]
    assert not np.any(sources == test_indices)
    return sources


def _rankdata(values):
    order = np.argsort(values, kind="mergesort")
    ranks = np.empty(len(values))
    sv = values[order]
    start = 0
    while start < len(values):
        stop = start + 1
        while stop < len(values) and sv[stop] == sv[start]:
            stop += 1
        ranks[order[start:stop]] = 0.5 * (start + stop - 1)
        start = stop
    return ranks


def spearman(x, y) -> float:
    """nested_estimators.py _spearman."""
    if len(x) < 2 or np.std(x) == 0 or np.std(y) == 0:
        return float("nan")
    return float(np.corrcoef(_rankdata(x), _rankdata(y))[0, 1])


def fully_nested(ds: TrialDataset, *, seed: int = 20260726, n_permutations: int = 0, n_ranks: int = 1,
                 random_source_seeds: tuple = (), rff_seeds: tuple = (),
                 permutation_seed_offsets: tuple = (), n_bootstrap: int = 0) -> dict:
    """Port of nested_estimators.py evaluate_fully_nested_audit (Methods 4.5, 4.7, 4.9).

    Random-state offsets are the code's: nuisance folds seed+21 (fold
    selection seed+21+100+fold), residual-learner selection seed+301, final
    nuisance penalties seed+401, permutations seed+601 (Methods 4.7: "One
    hundred deterministic permutations"). The bootstrap interval of the code
    is not computed (no claim uses it).

    Extra outputs, using the same fitted models: replacement ranks 1..n_ranks
    (Methods 4.7 diagnostics), uniform random same-condition sources for each
    seed in random_source_seeds (the paper says only "a random same-condition
    source"; a uniform draw is a standard choice, claims file
    replacement-ranks-lower), and the nonlinear-neural RFF learner of
    evaluate_nonlinear_neural_audit for each map seed in rff_seeds (it shares
    the nuisances and differs only in the residual learner).
    """
    tr, te = ds.train_indices, ds.test_indices
    assert not np.intersect1d(tr, te).size
    bp, npred, k = _nested_oof(ds, tr, seed + 21)
    ry = ds.behavior[tr] - bp
    rx = ds.neural[tr] - npred
    cond_tr = ds.condition[tr, 0]
    ia = _innovation_alpha(rx, ry, cond_tr, seed + 301)
    innovation = _ridge(ia).fit(rx.reshape(-1, rx.shape[-1]), ry.reshape(-1, ry.shape[-1]))
    ca, ra = _nuisance_alphas(ds, tr, seed + 401)
    ctr, cte = _flat(ds.context, tr), _flat(ds.context, te)
    xte = _flat(ds.neural, te)
    yte = _flat(ds.behavior, te)
    context_model = _ridge(ca).fit(ctr, _flat(ds.behavior, tr))
    residualizer = _ridge(ra).fit(ctr, _flat(ds.neural, tr))
    cpred = context_model.predict(cte)
    resid_te = xte - residualizer.predict(cte)
    exact = cpred + innovation.predict(resid_te)

    def source_prediction(sources, learner=innovation):
        return cpred + learner.predict(_flat(ds.neural, sources) - residualizer.predict(_flat(ds.context, sources)))

    srcs, dists = ranked_sources(ds, n_ranks=max(1, n_ranks))
    replacement = source_prediction(srcs[0])
    self_prediction = source_prediction(te)
    shape = ds.behavior[te].shape
    y3 = yte.reshape(shape)
    trial_c = np.mean((y3 - cpred.reshape(shape)) ** 2, axis=(1, 2))
    trial_e = np.mean((y3 - exact.reshape(shape)) ** 2, axis=(1, 2))
    trial_r = np.mean((y3 - replacement.reshape(shape)) ** 2, axis=(1, 2))
    variance = float(np.mean((yte - yte.mean(axis=0)) ** 2))
    cmse, emse, rmse_ = (float(mean_squared_error(yte, p)) for p in (cpred, exact, replacement))
    comp_gain = []
    for c in range(yte.shape[1]):
        v = float(np.mean((yte[:, c] - yte[:, c].mean()) ** 2))
        comp_gain.append(float((mean_squared_error(yte[:, c], cpred[:, c]) - mean_squared_error(yte[:, c], exact[:, c])) / v))
    conditions = ds.condition[:, 0]
    eligible = np.array([np.sum(conditions[te] == conditions[t]) - 1 for t in te])
    reuse = np.bincount(srcs[0], minlength=ds.neural.shape[0])
    out = dict(
        context_r2=_vw_r2(yte, cpred),
        exact_r2=_vw_r2(yte, exact),
        gain=normalized_gain(yte, cpred, exact),
        replacement_gain=normalized_gain(yte, cpred, replacement),
        self_replacement_max_abs_error=float(np.max(np.abs(self_prediction - exact))),
        context_mse=cmse, exact_mse=emse, replacement_mse=rmse_,
        context_rmse=float(np.sqrt(cmse)), exact_rmse=float(np.sqrt(emse)),
        mse_reduction_percent=float(100 * (cmse - emse) / cmse),
        component_gain=tuple(comp_gain),
        variance=variance,
        n_train=len(tr), n_test=len(te), folds=k,
        context_alpha=ca, residualizer_alpha=ra, innovation_alpha=ia,
        eligible_sources_min=int(eligible.min()),
        source_reuse_max=int(reuse[reuse > 0].max()),
        replacement_penalty_distance_spearman=spearman(dists[0], trial_r - trial_e),
        per_trial_context_mse=trial_c, per_trial_exact_mse=trial_e,
        test_indices=te.copy(),
    )
    if n_bootstrap:
        rng = np.random.default_rng(seed + 501)
        c3 = cpred.reshape(shape)
        e3 = exact.reshape(shape)
        cte_cond = conditions[te]
        boots = np.empty(n_bootstrap)
        for b in range(n_bootstrap):
            sampled = np.concatenate([rng.choice(m, size=len(m), replace=True)
                                      for m in (np.flatnonzero(cte_cond == c) for c in np.unique(cte_cond))])
            yb = y3[sampled].reshape(-1, shape[-1])
            boots[b] = normalized_gain(yb, c3[sampled].reshape(-1, shape[-1]), e3[sampled].reshape(-1, shape[-1]))
        out["conditional_ci"] = tuple(float(q) for q in np.quantile(boots, [0.025, 0.975]))
    if n_ranks > 1:
        out["rank_gains"] = tuple(normalized_gain(yte, cpred, source_prediction(srcs[r])) for r in range(n_ranks))
    if random_source_seeds:
        gains = []
        for s in random_source_seeds:
            rng = np.random.default_rng(s)
            picks = np.empty_like(te)
            for j, t in enumerate(te):
                cand = te[conditions[te] == conditions[t]]
                cand = cand[cand != t]
                picks[j] = rng.choice(cand)
            gains.append(normalized_gain(yte, cpred, source_prediction(picks)))
        out["random_source_gains"] = tuple(gains)
    if n_permutations:
        # seed + 601 is the code's generator; extra offsets give the protocol's
        # seed-sensitivity runs (claim seed plus 1000, 2000, 3000, 4000)
        out["permutation_means"] = {}
        for offset in (0,) + tuple(permutation_seed_offsets):
            rng = np.random.default_rng(seed + 601 + offset)
            gains = [normalized_gain(yte, cpred, source_prediction(permutation_sources(te, conditions, rng)))
                     for _ in range(n_permutations)]
            out["permutation_means"][offset] = float(np.mean(gains))
        out["permutation_mean"] = out["permutation_means"][0]
    if rff_seeds:
        rff = {}
        for map_seed in rff_seeds:
            alpha = _rff_alpha(rx, ry, cond_tr, seed + 301, map_seed)
            learner = _rff_ridge(alpha, 512, 1.0 / rx.shape[-1], map_seed).fit(
                rx.reshape(-1, rx.shape[-1]), ry.reshape(-1, ry.shape[-1]))
            pred = cpred + learner.predict(resid_te)
            rff[map_seed] = dict(gain=normalized_gain(yte, cpred, pred), alpha=alpha,
                                 replacement_gain=normalized_gain(yte, cpred, source_prediction(srcs[0], learner)))
        out["rff"] = rff
    return out


def _rff_ridge(alpha, n_components, gamma, seed):
    """nested_estimators.py _rff_ridge: scaler, RBFSampler (W ~ N(0, 2 gamma),
    b ~ U(0, 2 pi)), scaler, Ridge lsqr (Methods 4.6)."""
    return make_pipeline(StandardScaler(), RBFSampler(gamma=gamma, n_components=n_components, random_state=seed),
                         StandardScaler(), Ridge(alpha=alpha, solver="lsqr", tol=1e-6))


def _rff_alpha(rx, ry, cond, seed, map_seed, n_components=512, g=1.0, grid=ALPHA_GRID):
    """nested_estimators.py _select_grouped_rff_alpha: gamma = g / (neural feature
    count), map seed + fold in the selection folds."""
    _, counts = np.unique(cond, return_counts=True)
    splitter = StratifiedKFold(n_splits=min(3, int(counts.min())), shuffle=True, random_state=seed)
    scores = {float(a): [] for a in grid}
    for fold, (tr, va) in enumerate(splitter.split(np.arange(len(cond)), cond)):
        xtr, ytr = rx[tr].reshape(-1, rx.shape[-1]), ry[tr].reshape(-1, ry.shape[-1])
        xva, yva = rx[va].reshape(-1, rx.shape[-1]), ry[va].reshape(-1, ry.shape[-1])
        for a in grid:
            model = _rff_ridge(a, n_components, g / max(1, xtr.shape[1]), map_seed + fold).fit(xtr, ytr)
            scores[float(a)].append(_vw_r2(yva, model.predict(xva)))
    return max(scores, key=lambda a: (np.mean(scores[a]), -a))


def _cross_fitted_fixed(ds, idx, ca, ra, seed, folds=5, transform=None):
    """estimators.py _cross_fitted_nuisance_predictions (fixed penalties)."""
    cond = ds.condition[idx, 0]
    _, counts = np.unique(cond, return_counts=True)
    k = min(folds, int(counts.min()))
    splitter = StratifiedKFold(n_splits=k, shuffle=True, random_state=seed)
    bp = np.empty(ds.behavior[idx].shape, dtype=float)
    npred = np.empty(ds.neural[idx].shape, dtype=float)
    for fold, (ltr, lva) in enumerate(splitter.split(idx, cond)):
        ftr, fva = idx[ltr], idx[lva]
        ctr, cva = _flat(ds.context, ftr), _flat(ds.context, fva)
        if transform is not None:
            fmap = transform(fold)
            ctr, cva = fmap.fit_transform(ctr), fmap.transform(cva)
        bp[lva] = _ridge(ca).fit(ctr, _flat(ds.behavior, ftr)).predict(cva).reshape(bp[lva].shape)
        npred[lva] = _ridge(ra).fit(ctr, _flat(ds.neural, ftr)).predict(cva).reshape(npred[lva].shape)
    return bp.reshape(-1, bp.shape[-1]), npred.reshape(-1, npred.shape[-1])


def decoders_nested(ds: TrialDataset, *, seed: int = 20260726, neural_only_only: bool = False) -> dict:
    """Port of estimators.py evaluate_decoders_nested, the release's neural-only
    Ridge and its residual-neural ("innovation") gain. Penalties from one inner
    80/20 direction-stratified split of the outer-training trials (random_state
    seed+11), nuisances cross-fitted with those fixed penalties (seed+21).
    The context-matched replacement and bootstrap of the original are not
    computed (no claim uses them)."""
    tr, te = ds.train_indices, ds.test_indices
    cond = ds.condition[:, 0]
    itr, iva = train_test_split(tr, test_size=0.20, random_state=seed + 11, stratify=cond[tr])
    xi, xv = _flat(ds.neural, itr), _flat(ds.neural, iva)
    yi, yv = _flat(ds.behavior, itr), _flat(ds.behavior, iva)
    xtr, xte = _flat(ds.neural, tr), _flat(ds.neural, te)
    ytr, yte = _flat(ds.behavior, tr), _flat(ds.behavior, te)
    na = _select_alpha(xi, yi, xv, yv)
    neural_r2 = _vw_r2(yte, _ridge(na).fit(xtr, ytr).predict(xte))
    if neural_only_only:
        return dict(neural_r2=neural_r2, neural_alpha=na)
    ci, cv = _flat(ds.context, itr), _flat(ds.context, iva)
    ca = _select_alpha(ci, yi, cv, yv)
    ra = _select_alpha(ci, xi, cv, xv)
    cm = _ridge(ca).fit(ci, yi)
    rm = _ridge(ra).fit(ci, xi)
    ia = _select_alpha(xi - rm.predict(ci), yi - cm.predict(ci), xv - rm.predict(cv), yv - cm.predict(cv))
    ctr, cte = _flat(ds.context, tr), _flat(ds.context, te)
    cpred = _ridge(ca).fit(ctr, ytr).predict(cte)
    residualizer = _ridge(ra).fit(ctr, xtr)
    bp, npred = _cross_fitted_fixed(ds, tr, ca, ra, seed + 21)
    innovation = _ridge(ia).fit(xtr - npred, ytr - bp)
    pred = cpred + innovation.predict(xte - residualizer.predict(cte))
    return dict(neural_r2=neural_r2, context_r2=_vw_r2(yte, cpred), innovation_gain=normalized_gain(yte, cpred, pred),
                neural_alpha=na, context_alpha=ca, residualizer_alpha=ra, innovation_alpha=ia)


class _BlockRidge:
    """specification_estimators.py _BlockRidge: blockwise standardization, each
    block divided by sqrt(its penalty), Ridge(alpha=1) (Methods 4.5 objective).

    The release solves this Ridge with solver="lsqr", tol=1e-6; here it is solved
    exactly (solver="cholesky"), which minimizes the same objective about seven
    times faster (a deviation recorded in the attempt). solver="lsqr" gives the
    release's solver; 03_link_estimators.ipynb compares the two on one session."""

    def __init__(self, cp, xp, solver="cholesky"):
        self.cp, self.xp = float(cp), float(xp)
        self.cs, self.xs = StandardScaler(), StandardScaler()
        self.model = Ridge(alpha=1.0, solver="cholesky") if solver == "cholesky" else Ridge(alpha=1.0, solver=solver, tol=1e-6)

    def _design(self, c, x, fit):
        if fit:
            c, x = self.cs.fit_transform(c), self.xs.fit_transform(x)
        else:
            c, x = self.cs.transform(c), self.xs.transform(x)
        return np.concatenate([c / np.sqrt(self.cp), x / np.sqrt(self.xp)], axis=1)

    def fit(self, c, x, y):
        self.model.fit(self._design(c, x, True), y)
        return self

    def predict(self, c, x):
        return self.model.predict(self._design(c, x, False))


def block_ridge(ds: TrialDataset, *, seed: int = 20260726, solver: str = "cholesky") -> dict:
    """Port of specification_estimators.py evaluate_block_ridge_audit: context-only
    penalty and the pair (lambda_C, lambda_X) over the grid squared on an inner
    80/20 split (random_state seed+11), refit on all outer-training trials."""
    tr, te = ds.train_indices, ds.test_indices
    itr, iva = train_test_split(tr, test_size=0.20, random_state=seed + 11, stratify=ds.condition[tr, 0])
    ci, cv = _flat(ds.context, itr), _flat(ds.context, iva)
    xi, xv = _flat(ds.neural, itr), _flat(ds.neural, iva)
    yi, yv = _flat(ds.behavior, itr), _flat(ds.behavior, iva)
    ca = _select_alpha(ci, yi, cv, yv)
    best, best_score = (ALPHA_GRID[0], ALPHA_GRID[0]), -np.inf
    for cp in ALPHA_GRID:
        for xp in ALPHA_GRID:
            score = _vw_r2(yv, _BlockRidge(cp, xp, solver).fit(ci, xi, yi).predict(cv, xv))
            if score > best_score:
                best, best_score = (cp, xp), score
    ctr, cte = _flat(ds.context, tr), _flat(ds.context, te)
    xtr, xte = _flat(ds.neural, tr), _flat(ds.neural, te)
    ytr, yte = _flat(ds.behavior, tr), _flat(ds.behavior, te)
    cpred = _ridge(ca).fit(ctr, ytr).predict(cte)
    joint = _BlockRidge(*best, solver).fit(ctr, xtr, ytr).predict(cte, xte)
    return dict(gain=normalized_gain(yte, cpred, joint), context_alpha=ca, penalties=best)


class _RFFContext:
    """specification_estimators.py _RFFContextFeatures: [c, sqrt(2/D) cos(W'c + b)]
    on standardized context, gamma = g / p (Methods 4.6)."""

    def __init__(self, g, n_components, seed):
        self.g, self.n, self.seed = g, n_components, seed
        self.scaler = StandardScaler()

    def fit_transform(self, c):
        z = self.scaler.fit_transform(c)
        self.sampler = RBFSampler(gamma=self.g / max(1, z.shape[1]), n_components=self.n, random_state=self.seed)
        return np.concatenate([z, self.sampler.fit_transform(z)], axis=1)

    def transform(self, c):
        z = self.scaler.transform(c)
        return np.concatenate([z, self.sampler.transform(z)], axis=1)


def rff_context(ds: TrialDataset, *, seed: int = 20260726, gammas=(0.25, 1.0, 4.0), n_components: int = 256,
                fixed_gamma: float | None = None, map_seed_offset: int = 0) -> dict:
    """Port of specification_estimators.py evaluate_rff_context_audit: g chosen
    from gammas together with the three penalties on an inner 80/20 split
    (random_state seed+11; map seed seed+101+gamma index), five cross-fitting
    folds (seed+21, map seed seed+21+1000+fold). With fixed_gamma, g is fixed
    (the reading that runs one setting of Methods 4.6); map_seed_offset shifts
    every map seed (the "three map seeds" of Methods 4.6)."""
    tr, te = ds.train_indices, ds.test_indices
    if fixed_gamma is not None:
        gammas = (fixed_gamma,)
    itr, iva = train_test_split(tr, test_size=0.20, random_state=seed + 11, stratify=ds.condition[tr, 0])
    ci, cv = _flat(ds.context, itr), _flat(ds.context, iva)
    xi, xv = _flat(ds.neural, itr), _flat(ds.neural, iva)
    yi, yv = _flat(ds.behavior, itr), _flat(ds.behavior, iva)
    best, best_score = None, -np.inf
    for gi, g in enumerate(gammas):
        fmap = _RFFContext(g, n_components, seed + 101 + gi + map_seed_offset)
        mi, mv = fmap.fit_transform(ci), fmap.transform(cv)
        ca = _select_alpha(mi, yi, mv, yv)
        ra = _select_alpha(mi, xi, mv, xv)
        cm, rm = _ridge(ca).fit(mi, yi), _ridge(ra).fit(mi, xi)
        rxi, rxv = xi - rm.predict(mi), xv - rm.predict(mv)
        ryi, ryv = yi - cm.predict(mi), yv - cm.predict(mv)
        ia = _select_alpha(rxi, ryi, rxv, ryv)
        pred = cm.predict(mv) + _ridge(ia).fit(rxi, ryi).predict(rxv)
        score = _vw_r2(yv, pred)
        if score > best_score:
            best, best_score = (gi, g, ca, ra, ia), score
    gi, g, ca, ra, ia = best
    ctr, cte = _flat(ds.context, tr), _flat(ds.context, te)
    xtr, xte = _flat(ds.neural, tr), _flat(ds.neural, te)
    ytr, yte = _flat(ds.behavior, tr), _flat(ds.behavior, te)
    bp, npred = _cross_fitted_fixed(
        ds, tr, ca, ra, seed + 21,
        transform=lambda fold: _RFFContext(g, n_components, seed + 21 + 1000 + fold + map_seed_offset))
    fmap = _RFFContext(g, n_components, seed + 101 + gi + map_seed_offset)
    mtr, mte = fmap.fit_transform(ctr), fmap.transform(cte)
    cpred = _ridge(ca).fit(mtr, ytr).predict(mte)
    residualizer = _ridge(ra).fit(mtr, xtr)
    innovation = _ridge(ia).fit(xtr - npred, ytr - bp)
    pred = cpred + innovation.predict(xte - residualizer.predict(mte))
    return dict(gain=normalized_gain(yte, cpred, pred), gamma=g, context_r2=_vw_r2(yte, cpred))


# --------------------------------------------------------------------------
# Summaries


def date_bootstrap(values_by_date: dict, rng: np.random.Generator, n: int = 10000) -> tuple[float, float]:
    """Resample dates with replacement, mean over the sessions of the sampled
    dates, 2.5 and 97.5 percentiles (Table 1 legend; build_submission_figures.py
    date_cluster_summary). values_by_date maps a date to its session values."""
    dates = sorted(values_by_date)
    boots = np.empty(n)
    for i in range(n):
        sampled = rng.choice(len(dates), size=len(dates), replace=True)
        boots[i] = np.mean(np.concatenate([np.atleast_1d(values_by_date[dates[j]]) for j in sampled]))
    return float(np.quantile(boots, 0.025)), float(np.quantile(boots, 0.975))


# --------------------------------------------------------------------------
# Running many fits: one process per session, one BLAS thread per process
# (protocol, "Keep it fast"). Number of workers is a standard choice that
# cannot change a result.

ESTIMATORS = {
    "nested": fully_nested,
    "decoders": decoders_nested,
    "block": block_ridge,
    "rff_context": rff_context,
}


def _drop_arrays(result: dict, keep_arrays: bool) -> dict:
    if keep_arrays:
        return result
    return {k: v for k, v in result.items() if not isinstance(v, np.ndarray)}


def link_session_jobs(asset_id: str, path: str, jobs: list, signals=("SpikingBandPower", "ThresholdCrossings")) -> dict:
    """Stream one LINK session once and run every job on it.

    Each job is (name, build_kwargs, estimator, estimator_kwargs, keep_arrays)."""
    from threadpoolctl import threadpool_limits

    with threadpool_limits(1):
        session = load_link_session(asset_id, path, signals=signals)
        out = {"date": session.date, "task": session.task, "identifier": session.identifier}
        for name, build_kwargs, estimator, estimator_kwargs, keep in jobs:
            ds = build_link_dataset(session, **build_kwargs)
            result = ESTIMATORS[estimator](ds, **estimator_kwargs)
            result["n_usable"] = len(ds.neural)
            result["n_context"] = ds.context.shape[-1]
            result["n_trials_table"] = len(session.trials)
            if keep:
                result["source_rows"] = ds.source_rows
            out[name] = _drop_arrays(result, keep)
    return out


def rtt_jobs(asset_id: str, jobs: list) -> dict:
    from threadpoolctl import threadpool_limits

    with threadpool_limits(1):
        raw = load_rtt_raw(asset_id)
        out = {}
        for name, build_kwargs, estimator, estimator_kwargs, keep in jobs:
            ds = build_rtt_dataset(raw, **build_kwargs)
            out[name] = _drop_arrays(ESTIMATORS[estimator](ds, **estimator_kwargs), keep)
    return out


RELEASE_MODULES = ("types", "estimators", "specification_estimators", "robustness_estimators", "nested_estimators")


def release_estimators():
    """The paper's own estimator modules, fetched from the release at PAPER_COMMIT
    into a temporary package (its __init__ is left empty: the real one imports
    the synthetic generator only), to run next to the ports here."""
    import importlib
    import sys
    import tempfile
    from pathlib import Path

    root = Path(tempfile.mkdtemp()) / "neural_evidence"
    root.mkdir()
    (root / "__init__.py").write_text("")
    raw = PAPER_CODE.replace("github.com", "raw.githubusercontent.com") + f"/{PAPER_COMMIT}/src/neural_evidence"
    for name in RELEASE_MODULES:
        with urllib.request.urlopen(f"{raw}/{name}.py", timeout=120) as response:
            (root / f"{name}.py").write_bytes(response.read())
    sys.path.insert(0, str(root.parent))
    return importlib.import_module("neural_evidence.nested_estimators"), importlib.import_module("neural_evidence.types")


def release_dataset(ds: TrialDataset, types_module):
    """A port TrialDataset as the release's TrialDataset (trial_id and phase are not read by the estimators)."""
    n, t = ds.neural.shape[:2]
    return types_module.TrialDataset(
        neural=ds.neural, context=ds.context, behavior=ds.behavior,
        trial_id=np.repeat(np.arange(n)[:, None], t, axis=1), condition=ds.condition,
        phase=np.repeat(np.linspace(0.0, 1.0, t, endpoint=False)[None, :], n, axis=0))


def maze_jobs(asset_id: str, jobs: list) -> dict:
    from threadpoolctl import threadpool_limits

    with threadpool_limits(1):
        raw = load_maze_raw(asset_id)
        out = {}
        for name, build_kwargs, estimator, estimator_kwargs, keep in jobs:
            ds = build_maze_dataset(raw, **build_kwargs)
            out[name] = _drop_arrays(ESTIMATORS[estimator](ds, **estimator_kwargs), keep)
    return out


def synthetic_job(seed: int, regime: str, n_permutations: int = 100) -> dict:
    from threadpoolctl import threadpool_limits

    with threadpool_limits(1):
        ds = generate_synthetic(seed=seed, **SYNTHETIC_REGIMES[regime])
        result = fully_nested(ds, seed=seed, n_permutations=n_permutations)
    return {"seed": seed, "regime": regime, **_drop_arrays(result, False)}


def run_parallel(function, argument_lists: list, workers: int = 4) -> list:
    """Run function(*args) for each args in a process pool; results in input order."""
    import multiprocessing as mp
    from concurrent.futures import ProcessPoolExecutor

    with ProcessPoolExecutor(max_workers=workers, mp_context=mp.get_context("spawn")) as pool:
        futures = [pool.submit(function, *args) for args in argument_lists]
        return [f.result() for f in futures]
