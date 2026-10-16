"""Loading and jPCA for the maze reaching data of dandiset 000070.

Churchland, Cunningham, Kaufman, Foster, Nuyujukian, Ryu & Shenoy (2012), Nature 487:51-56,
doi:10.1038/nature11129.

Each NWB file holds one session of one monkey (Jenkins or Nitschke): a trial table with event
times, maze condition and the lab's trial flags; hand, cursor and eye position at 1 kHz; and a
Units table of 192 units, one per electrode of the two 96-channel arrays (PMd and M1). Spikes
and positions were stored only inside trials. Files are streamed from the archive at the
pinned version; nothing is written to disk. Spike times and hand positions are read with
parallel HTTP range requests on the byte offsets of their storage (about 50 times faster than
through an HDF5 file object); `read_dataset` checks the result against h5py.

Where the parameters come from:

- Trial selection, from the paper's Methods: successful trials with a delay (go cue minus
  target onset) above 400 ms. The Methods also discard trials whose behaviour was not
  stereotyped; the trial table's `correct_reach` flag ("isConsistent" in the lab's files) is
  that selection, and `discard_trial` flags tracking problems. Condition 0 holds novel mazes
  (`novel_maze` = 1) and is not one of the 108 conditions.
- Firing rates are averaged per condition aligned on movement onset (`move_begins_time`) and
  smoothed with a Gaussian of 20 ms SD (the Methods give 20 or 24 ms "depending on the
  dataset" without saying which; 20 ms is used, 24 ms is a variant). The Methods' further
  "PC smoothing" is not applied; the supplement (Supplementary Fig. 10) says it has
  essentially no effect on the population analyses.
- jPCA follows the Methods, the Supplementary Derivation and the Python port of the lab's
  MATLAB code (github.com/bantin/jPCA at commit 3f8be9fa32a43a7b3090695c9e671f52f02878ac;
  the lab's own download page could not be fetched): soft normalisation by the firing-rate
  range plus 5 spikes/s (`SOFT_NORM`), subtraction of the cross-condition mean, PCA on the
  analysed times only, 6 PCs, 200 ms sampled every 10 ms (`ANALYSIS_TIMES`, -50 to +150 ms
  from movement onset, the window of the codepack's example; the Methods say only "starting
  just before the rapid change in neural activity that precedes movement onset"), the
  derivative as the difference of adjacent samples, and the skew-symmetric least-squares fit
  solved in closed form as in the Supplementary Derivation.
- The simulated 'velocity' and 'complex kinematic' populations follow the Methods where they
  are specific (factors, the complex model's sensitivities, gamma-interval spiking of order 2,
  one unit per recorded unit with matched mean rate and trial counts); the rest (lead of
  neural activity over kinematics, the time course of preparatory tuning, modulation depth of
  the velocity model) are choices made here and are named in `simulate_population`.
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
import requests
from dandi.dandiapi import DandiAPIClient
from scipy.ndimage import gaussian_filter1d

DANDISET_ID = "000070"
DANDISET_VERSION = "0.260528.0919"

# The paper's two array datasets, and the third session with 108 conditions (see the notebook).
SESSIONS = {
    "J-array": "sub-Jenkins/sub-Jenkins_ses-20090918_behavior+ecephys.nwb",
    "N-array": "sub-Nitschke/sub-Nitschke_ses-20100923_behavior+ecephys.nwb",
    "N-0910": "sub-Nitschke/sub-Nitschke_ses-20090910_behavior+ecephys.nwb",
}

MIN_DELAY_S = 0.4            # Methods: only trials with delays > 400 ms
SIGMA_MS = 20.0              # Methods: Gaussian of 20 or 24 ms
WINDOW_MS = (-800, 500)      # PSTH span around movement onset (1 ms bins)
ANALYSIS_TIMES = np.arange(-50, 151, 10)   # ms from movement onset, 200 ms every 10 ms
SOFT_NORM = 5.0              # spikes/s added to each unit's range (jPCA codepack)
N_PCS = 6                    # Methods: k = 6 for all main-text analyses
DT_S = 0.010                 # sampling interval of the analysed times


# ---------------------------------------------------------------- loading

def asset_urls() -> dict[str, str]:
    """Streaming URL of every NWB file at the pinned version, by path."""
    with DandiAPIClient() as client:
        dandiset = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        return {a.path: a.get_content_url(follow_redirects=1, strip_query=True)
                for a in dandiset.get_assets() if a.path.endswith(".nwb")}


def _get_range(url: str, start: int, stop: int) -> bytes:
    for attempt in range(5):
        try:
            r = requests.get(url, headers={"Range": f"bytes={start}-{stop - 1}"}, timeout=180)
            r.raise_for_status()
            if len(r.content) == stop - start:
                return r.content
        except requests.RequestException:
            if attempt == 4:
                raise
    raise RuntimeError(f"short read of bytes {start}-{stop} from {url}")


def read_dataset(url: str, dataset: h5py.Dataset, block: int = 8 * 2**20) -> np.ndarray:
    """The whole of a dataset, read by parallel byte ranges.

    Handles contiguous uncompressed datasets, and chunked ones whose only filter is gzip
    (the N-array file); adjacent chunks are fetched together in blocks.
    """
    dtype = dataset.dtype.newbyteorder("<")
    if dataset.chunks is None:
        if dataset.compression is not None:
            raise ValueError(f"{dataset.name}: unexpected layout")
        offset = dataset.id.get_offset()
        nbytes = dataset.size * dataset.dtype.itemsize
        starts = range(0, nbytes, block)
        with ThreadPoolExecutor(16) as pool:
            parts = list(pool.map(lambda s: _get_range(url, offset + s, offset + min(s + block, nbytes)), starts))
        out = np.frombuffer(b"".join(parts), dtype=dtype).reshape(dataset.shape)
    else:
        import zlib
        if set(dataset._filters) != {"gzip"} or len(dataset.chunks) > 2 or (
                len(dataset.chunks) == 2 and dataset.chunks[1] != dataset.shape[1]):
            raise ValueError(f"{dataset.name}: unexpected filters or chunk shape")
        info = [dataset.id.get_chunk_info(i) for i in range(dataset.id.get_num_chunks())]
        info.sort(key=lambda c: c.byte_offset)
        groups, cur = [], [info[0]]
        for c in info[1:]:
            if c.byte_offset == cur[-1].byte_offset + cur[-1].size and c.byte_offset + c.size - cur[0].byte_offset <= block:
                cur.append(c)
            else:
                groups.append(cur)
                cur = [c]
        groups.append(cur)
        out = np.empty(dataset.shape, dtype=dtype)
        rows = dataset.chunks[0]

        def fetch(group):
            raw = _get_range(url, group[0].byte_offset, group[-1].byte_offset + group[-1].size)
            for c in group:
                if c.filter_mask != 0:
                    raise ValueError("a chunk skipped its filter")
                piece = raw[c.byte_offset - group[0].byte_offset: c.byte_offset - group[0].byte_offset + c.size]
                arr = np.frombuffer(zlib.decompress(piece), dtype=dtype).reshape((rows,) + dataset.shape[1:])
                r0 = c.chunk_offset[0]
                n = min(rows, dataset.shape[0] - r0)
                out[r0:r0 + n] = arr[:n]

        with ThreadPoolExecutor(16) as pool:
            list(pool.map(fetch, groups))
    # the first and last values must match what h5py reads
    if not (np.array_equal(out[:5], dataset[:5]) and np.array_equal(out[-5:], dataset[-5:])):
        raise ValueError(f"byte-range read of {dataset.name} disagrees with h5py")
    return out


def _text(v):
    if isinstance(v, bytes):
        return v.decode()
    if isinstance(v, np.ndarray):
        return [_text(x) for x in v.tolist()]
    return v


def load_session(path: str, url: str | None = None, cursor: bool = False) -> dict:
    """Trials, spikes per unit, unit areas and hand position (and cursor, if asked) of one file."""
    url = url or asset_urls()[path]
    f = h5py.File(remfile.File(url), "r")
    tr = f["intervals/trials"]
    cols = {}
    for c in _text(tr.attrs["colnames"]):
        d = tr[c]
        if d.ndim == 1 and d.dtype.kind in "fiub" and c + "_index" not in tr:
            cols[c] = d[:]
    trials = pd.DataFrame(cols)
    trials["delay"] = trials.go_cue_time - trials.target_presentation_time
    hit = tr["hit_target_position"][:]
    trials["hit_x"], trials["hit_y"] = hit[:, 0], hit[:, 1]

    u = f["units"]
    index = u["spike_times_index"][:].astype(np.int64)
    spikes_flat = read_dataset(url, u["spike_times"])
    index_fixed, wraps = fix_first_index(spikes_flat, index)
    starts, stops = trials.start_time.values, trials.stop_time.values
    spikes = np.split(spikes_flat, index_fixed[:-1])
    spike_offsets = [assign_to_trials(x, starts, stops) for x in spikes]
    hand_t = read_dataset(url, f["processing/behavior/Position/Hand/timestamps"])
    hand_offsets = hand_blocks(hand_t, starts)
    electrodes = u["electrodes"][:]
    locations = np.array(_text(f["general/extracellular_ephys/electrodes/location"][:]))
    group_names = np.array(_text(f["general/extracellular_ephys/electrodes/group_name"][:]))
    obs_index = u["obs_intervals_index"][:]
    obs_first = u["obs_intervals"][: obs_index[0]]

    hand = f["processing/behavior/Position/Hand"]
    meta = {k: _text(f[k][()]) for k in ["session_start_time", "general/subject/subject_id",
                                         "general/subject/species", "session_description"]}
    meta.update(hand_unit=_text(hand["data"].attrs["unit"]),
                hand_conversion=float(hand["data"].attrs["conversion"]),
                units_description=_text(u.attrs.get("description")),
                units_colnames=_text(u.attrs["colnames"]),
                trials_colnames=_text(tr.attrs["colnames"]),
                electrode_locations=sorted(set(locations.tolist())),
                n_obs_intervals=np.diff(np.r_[0, obs_index]).tolist())
    return {
        "path": path, "url": url, "meta": meta, "trials": trials, "spikes": spikes,
        "spike_offsets": spike_offsets, "index_stored": index, "index_fixed": index_fixed,
        "index_wraps": wraps,
        "unit_area": np.where(np.char.find(locations[electrodes].astype(str), "M1") >= 0, "M1", "PMd"),
        "unit_group": group_names[electrodes],
        "obs_first": obs_first,
        "hand_t": hand_t, "hand_offsets": hand_offsets,
        "hand_xy": read_dataset(url, hand["data"]),
        "cursor_xy": read_dataset(url, f["processing/behavior/Position/Cursor/data"]) if cursor else None,
    }


def fix_first_index(flat: np.ndarray, index: np.ndarray) -> tuple[np.ndarray, int]:
    """Correct the first entry of spike_times_index when it wrapped at 2**16.

    In the files written by the first conversion the first entry is the true end of unit 0
    modulo 65536, so unit 0 is cut short and its remaining spikes open unit 1. The true end
    is the one candidate, index[0] + m * 65536 with m >= 0 and below index[1], where the
    stored times go backwards from the end of the session to its start (from the last
    trial's time to below the second trial's start). Returns the corrected index and m.
    """
    out = index.copy()
    cands = [index[0] + m * 65536 for m in range(0, (index[1] - index[0]) // 65536 + 1)]
    good = [c for c in cands if 0 < c < index[1] and flat[c - 1] > flat[c] and flat[c] < flat[c - 1] - 600]
    if index[0] < 65536 and good:
        if len(good) != 1:
            raise ValueError(f"ambiguous end of unit 0: {good}")
        out[0] = good[0]
    return out, int((out[0] - index[0]) // 65536)


def assign_to_trials(values: np.ndarray, starts: np.ndarray, stops: np.ndarray, eps: float = 1e-6) -> np.ndarray:
    """Offsets of each trial's block in a series stored trial by trial in table order.

    The conversion wrote each unit's spikes trial after trial, each inside its trial's
    interval. Where the file's clock resets (N-array), trials overlap in time and a spike
    cannot be placed by its time alone, but the storage order settles it: trial i's block
    is the run of values, from where trial i-1's ended, that lie inside trial i's interval.
    Raises if any value is left over.
    """
    off = np.zeros(len(starts) + 1, dtype=np.int64)
    p, n = 0, len(values)
    for i, (a, b) in enumerate(zip(starts, stops)):
        k = 512
        while True:
            w = values[p:p + k]
            inside = (w >= a - eps) & (w <= b + eps)
            if inside.all() and p + k < n:
                k *= 4
                continue
            p += len(w) if inside.all() else int(np.argmin(inside))
            break
        off[i + 1] = p
    if p != n:
        raise ValueError(f"{n - p} values not inside their trial")
    return off


def hand_blocks(t: np.ndarray, starts: np.ndarray) -> np.ndarray:
    """Offsets of each trial's block of 1 kHz position samples (one block per trial, in order)."""
    gaps = np.where(np.abs(np.diff(t) - 0.001) > 1e-6)[0] + 1
    off = np.r_[0, gaps, len(t)]
    if len(off) - 1 != len(starts) or not np.allclose(t[off[:-1]], starts):
        raise ValueError("position blocks do not match the trials")
    return off


def trial_spikes(session: dict, unit: int, trial: int) -> np.ndarray:
    o = session["spike_offsets"][unit]
    return session["spikes"][unit][o[trial]:o[trial + 1]]


def select_trials(trials: pd.DataFrame, consistent: bool = True, min_delay: float = MIN_DELAY_S) -> pd.Series:
    """Boolean mask of the trials the Methods analyse."""
    ok = (trials.task_success == 1) & (trials.discard_trial == 0) & (trials.delay > min_delay)
    ok &= trials.maze_condition > 0
    if consistent and "correct_reach" in trials:
        ok &= trials.correct_reach == 1
    return ok & trials.move_begins_time.notna()


# ---------------------------------------------------------------- firing rates

def _trial_values(session: dict, unit: int, trial_idx: np.ndarray):
    st, off = session["spikes"][unit], session["spike_offsets"][unit]
    a, b = off[trial_idx], off[trial_idx + 1]
    row = np.repeat(np.arange(len(trial_idx)), b - a)
    vals = np.concatenate([st[x:y] for x, y in zip(a, b)]) if (b - a).sum() else np.zeros(0)
    return row, vals


def condition_counts(session: dict, trial_idx: np.ndarray, align: np.ndarray, conditions: np.ndarray,
                     window_ms=WINDOW_MS):
    """Spike counts in 1 ms bins around each alignment time, summed per condition.

    Returns the condition labels, the sums (conditions x bins x units) and the number of
    trials per condition. Each trial's spikes are taken from its own block
    (`assign_to_trials`), so trials that overlap on the file's clock do not take each
    other's spikes.
    """
    lo, hi = window_ms
    nb = hi - lo
    labels, cidx = np.unique(conditions, return_inverse=True)
    sums = np.zeros((len(labels), nb, len(session["spikes"])), dtype=np.float32)
    w0 = align + lo / 1000
    for k in range(len(session["spikes"])):
        row, vals = _trial_values(session, k, trial_idx)
        bins = np.floor((vals - w0[row]) * 1000).astype(int)
        keep = (bins >= 0) & (bins < nb)
        np.add.at(sums[:, :, k], (cidx[row[keep]], bins[keep]), 1)
    return labels, sums, np.bincount(cidx)


def condition_rates(sums: np.ndarray, n_trials: np.ndarray, sigma_ms: float = SIGMA_MS) -> np.ndarray:
    """Trial-averaged, Gaussian-smoothed firing rates (spikes/s): conditions x bins x units."""
    rates = sums.astype(np.float64) / n_trials[:, None, None] * 1000.0
    if sigma_ms > 0:
        rates = gaussian_filter1d(rates, sigma_ms, axis=1, mode="nearest")
    return rates


def window_counts(session: dict, trial_idx: np.ndarray, t0: np.ndarray, t1: np.ndarray) -> np.ndarray:
    """Spike counts per trial and unit between times t0 and t1 of each trial."""
    out = np.zeros((len(trial_idx), len(session["spikes"])))
    for k in range(len(session["spikes"])):
        row, vals = _trial_values(session, k, trial_idx)
        keep = (vals >= t0[row]) & (vals < t1[row])
        out[:, k] = np.bincount(row[keep], minlength=len(trial_idx))
    return out


def sample_times(rates: np.ndarray, times_ms=ANALYSIS_TIMES, window_ms=WINDOW_MS) -> np.ndarray:
    return rates[:, np.asarray(times_ms) - window_ms[0], :]


# ---------------------------------------------------------------- jPCA

def skew_fit(X: np.ndarray, dX: np.ndarray) -> np.ndarray:
    """Least-squares skew-symmetric M with dX ~ X @ M (Supplementary Derivation, closed form)."""
    n = X.shape[1]
    iu = np.triu_indices(n, 1)
    # dX[:, j] = sum_i X[:, i] M[i, j]; M[i, j] = k for (i, j) in iu and -k for (j, i)
    design = np.zeros((X.shape[0] * n, len(iu[0])))
    for p, (i, j) in enumerate(zip(*iu)):
        col = np.zeros((X.shape[0], n))
        col[:, j] += X[:, i]
        col[:, i] -= X[:, j]
        design[:, p] = col.ravel(order="F")
    k = np.linalg.lstsq(design, dX.ravel(order="F"), rcond=None)[0]
    M = np.zeros((n, n))
    M[iu] = k
    return M - M.T


def r2(dX, pred) -> float:
    return 1.0 - np.sum((dX - pred) ** 2) / np.sum((dX - dX.mean(axis=0)) ** 2)


def jpca(rates: np.ndarray, times_ms=ANALYSIS_TIMES, window_ms=WINDOW_MS, n_pcs: int = N_PCS,
         soft_norm: float = SOFT_NORM, subtract_cc_mean: bool = True, n_planes: int = 1) -> dict:
    """jPCA of conditions x 1-ms bins x units firing rates.

    Returns the projections onto the jPC planes (conditions x times x 2 per plane), the
    variance captured by each plane and by the PCs as fractions of the total variance of the
    normalised data over the analysed times, the R2 of the skew-symmetric and unconstrained
    fits in the n_pcs-D space and in the first plane, and the plane's rotation frequency.
    """
    data = rates.astype(np.float64).copy()
    norm = np.ones(data.shape[2])
    if soft_norm is not None and soft_norm >= 0:
        norm = data.max(axis=(0, 1)) - data.min(axis=(0, 1)) + soft_norm
        data /= norm
    cc_mean = data.mean(axis=0, keepdims=True) if subtract_cc_mean else np.zeros((1,) + data.shape[1:])
    data -= cc_mean
    data = sample_times(data, times_ms, window_ms)                  # c x t x n
    c, t, n = data.shape
    flat = data.reshape(c * t, n)
    flat_mean = flat.mean(axis=0)
    flat = flat - flat_mean
    total_var = np.sum(flat ** 2)
    _, s, vt = np.linalg.svd(flat, full_matrices=False)
    pcs = vt[:n_pcs].T                                               # n x k
    pc_var = s[:n_pcs] ** 2 / total_var
    red = (flat @ pcs).reshape(c, t, n_pcs)
    X = red[:, :-1].reshape(-1, n_pcs)
    dX = np.diff(red, axis=1).reshape(-1, n_pcs)
    M_skew = skew_fit(X, dX)
    M_best = np.linalg.lstsq(X, dX, rcond=None)[0]
    evals, evecs = np.linalg.eig(M_skew)
    order = np.argsort(-np.abs(evals.imag), kind="stable")
    evals, evecs = evals[order], evecs[:, order]
    planes, plane_var, bases = [], [], []
    for p in range(n_planes):
        v1, v2 = evecs[:, 2 * p], evecs[:, 2 * p + 1]
        u1 = np.real(v1 + v2)
        u2 = np.real(1j * (v1 - v2))
        basis = np.column_stack([u1 / np.linalg.norm(u1), u2 / np.linalg.norm(u2)])
        proj = red @ basis                                            # c x t x 2
        # orient: net rotation counter-clockwise, preparatory spread along the first axis
        prep = proj[:, 0, :] - proj[:, 0, :].mean(axis=0)
        w, v = np.linalg.eigh(prep.T @ prep)
        rot = v[:, ::-1]
        if np.linalg.det(rot) < 0:
            rot[:, 1] *= -1
        basis = basis @ rot
        proj = red @ basis
        x, dx = proj[:, :-1].reshape(-1, 2), np.diff(proj, axis=1).reshape(-1, 2)
        if np.sum(x[:, 0] * dx[:, 1] - x[:, 1] * dx[:, 0]) < 0:
            basis[:, 1] *= -1
            proj = red @ basis
        planes.append(proj)
        bases.append(basis)
        plane_var.append(np.sum(proj.reshape(-1, 2) ** 2) / total_var)
    proj = planes[0]
    x, dx = proj[:, :-1].reshape(-1, 2), np.diff(proj, axis=1).reshape(-1, 2)
    m2_best = np.linalg.lstsq(x, dx, rcond=None)[0]
    m2_skew = skew_fit(x, dx)
    return {
        "planes": planes, "plane_var": np.array(plane_var), "pc_var": pc_var,
        "eigenvalues_rad_s": np.abs(evals.imag[::2]) / DT_S,
        "freq_hz": np.abs(evals.imag[0]) / DT_S / (2 * np.pi),
        "r2_skew": r2(dX, X @ M_skew), "r2_best": r2(dX, X @ M_best),
        "r2_skew_plane": r2(dx, x @ m2_skew), "r2_best_plane": r2(dx, x @ m2_best),
        "M_skew": M_skew, "pcs": pcs, "bases": bases,
        "transform": {"norm": norm, "cc_mean": cc_mean, "flat_mean": flat_mean, "times_ms": times_ms,
                      "window_ms": window_ms},
    }


def project(rates: np.ndarray, res: dict, plane: int = 0) -> np.ndarray:
    """Projection of other conditions' rates onto a jPC plane fitted by `jpca` (c x t x 2).

    Uses the normalisation, cross-condition mean, PCs and plane of the fit, so that held-out
    conditions are placed as the fitted ones were.
    """
    tf = res["transform"]
    data = sample_times((rates / tf["norm"]) - tf["cc_mean"], tf["times_ms"], tf["window_ms"])
    return ((data - tf["flat_mean"]) @ res["pcs"]) @ res["bases"][plane]


def state_angles(proj: np.ndarray) -> np.ndarray:
    """Angle between the state x and its derivative in a jPC plane, every condition and time."""
    x, dx = proj[:, :-1], np.diff(proj, axis=1)
    return np.arctan2(x[..., 0] * dx[..., 1] - x[..., 1] * dx[..., 0],
                      x[..., 0] * dx[..., 0] + x[..., 1] * dx[..., 1]).ravel()


def net_rotation(proj: np.ndarray) -> np.ndarray:
    """Net change of each condition's polar angle in the plane over the analysed times (rad)."""
    ang = np.unwrap(np.arctan2(proj[..., 1], proj[..., 0]), axis=1)
    return ang[:, -1] - ang[:, 0]


def angle_peak(angles: np.ndarray, bins: int = 36) -> float:
    """Centre of the most populated of `bins` equal bins over (-pi, pi]."""
    h, edges = np.histogram(angles, bins=bins, range=(-np.pi, np.pi))
    return float((edges[:-1] + edges[1:])[np.argmax(h)] / 2)


def summary(res: dict) -> dict:
    ang = state_angles(res["planes"][0])
    rot = net_rotation(res["planes"][0])
    return {
        "plane_var": res["plane_var"][0], "pc1_var": res["pc_var"][0],
        "pc23_var": res["pc_var"][1:3].sum(), "pcs_var": res["pc_var"].sum(),
        "r2_ratio_6d": res["r2_skew"] / res["r2_best"],
        "r2_ratio_plane": res["r2_skew_plane"] / res["r2_best_plane"],
        "r2_skew": res["r2_skew"], "r2_best": res["r2_best"],
        "angle_peak": angle_peak(ang), "angle_median": float(np.median(ang)),
        "frac_ccw": float(np.mean(rot > 0)), "freq_hz": res["freq_hz"],
    }


# ---------------------------------------------------------------- shuffle controls

def shuffle_rates(rates: np.ndarray, t0_index: int, kind: int, rng: np.random.Generator) -> np.ndarray:
    """The three shuffle controls of Supplementary Fig. 2, on conditions x bins x units.

    Activity after the dividing bin t0 is: 1, inverted about its value at t0 for a random half
    of the conditions, separately for each unit; 2, inverted for all conditions; 3, taken from
    another condition (one permutation for all units) and shifted to continue from this
    condition's value at t0.
    """
    out = rates.copy()
    after = slice(t0_index + 1, None)
    at = rates[:, t0_index:t0_index + 1, :]
    if kind == 1:
        flip = rng.random((rates.shape[0], 1, rates.shape[2])) < 0.5
        out[:, after] = np.where(flip, 2 * at - rates[:, after], rates[:, after])
    elif kind == 2:
        out[:, after] = 2 * at - rates[:, after]
    elif kind == 3:
        perm = rng.permutation(rates.shape[0])
        out[:, after] = rates[perm][:, after] - rates[perm][:, t0_index:t0_index + 1] + at
    return out


# ---------------------------------------------------------------- simulated populations

def hand_kinematics(session: dict, trial_idx: np.ndarray, align: np.ndarray, window_ms=WINDOW_MS):
    """Hand position (m), velocity, acceleration and jerk around each alignment time.

    Samples come from each trial's own block; a window reaching outside the block raises.
    The file states metres; the values are in mm (see the notebook), so they are divided by
    1000. Positions are smoothed with a 10 ms SD Gaussian before differentiating.
    """
    t, xy, off = session["hand_t"], session["hand_xy"], session["hand_offsets"]
    lo, hi = window_ms
    rel = np.arange(lo, hi) / 1000.0
    first = off[trial_idx] + np.round((align - t[off[trial_idx]]) * 1000).astype(int) + lo
    if np.any(first < off[trial_idx]) or np.any(first + (hi - lo) > off[trial_idx + 1]):
        raise ValueError("window outside a trial's position samples")
    pos = np.stack([xy[i:i + (hi - lo)] for i in first]) / 1000.0     # trials x bins x 2 (m)
    pos = gaussian_filter1d(pos, 10, axis=1, mode="nearest")
    vel = np.gradient(pos, 1e-3, axis=1)
    acc = np.gradient(vel, 1e-3, axis=1)
    jerk = np.gradient(acc, 1e-3, axis=1)
    return rel, pos, vel, acc, jerk


def simulate_population(kind: str, cond_kin: dict, recorded_rates: np.ndarray, trials_per_cond: np.ndarray,
                        rng: np.random.Generator, lead_ms: int = 100, prep_onset_ms: int = -400,
                        prep_decay_ms: float | None = 100.0) -> np.ndarray:
    """Spikes from a 'velocity' or 'complex' kinematic model, averaged as for the data.

    cond_kin holds condition-mean kinematics (conditions x bins x 2, from `hand_kinematics`)
    and per condition the endpoint (2) and peak speed. One simulated unit per recorded unit,
    with a uniformly random preferred direction for movement and for preparation.

    - velocity: rate = base + g * (velocity . PD) + s * speed during movement, the Methods'
      three movement factors; preparatory rate tuned to endpoint and peak speed.
    - complex: rate = base + 25 position + 10 velocity + 1 acceleration + 0.05 jerk, each
      along the PD (spikes/s per m, m/s, m/s2, m/s3; the Methods' constants); preparatory
      rate tuned to the endpoint.

    Choices made here, as the Methods do not give them: neural activity leads the kinematics
    by `lead_ms`; preparatory tuning is on from `prep_onset_ms` before movement onset and
    decays with a time constant of `prep_decay_ms` (100 ms) after it, or stays on to the end of
    the window if that is None (a step); a `prep_onset_ms` at or after the end of the window
    leaves no preparatory tuning; in the velocity model the movement
    modulation of each unit is scaled so that its range across conditions and times matches
    the recorded unit's, and preparatory modulation is half of it; the base rate is the
    recorded unit's mean rate; rates are rectified at zero. Spikes are drawn per trial from a
    gamma-interval process of order 2 and averaged and smoothed like the data.
    """
    pos, vel, acc, jerk = (cond_kin[k] for k in ("pos", "vel", "acc", "jerk"))
    c, nb, _ = vel.shape
    n_units = recorded_rates.shape[2]
    shift = lambda a: np.concatenate([a[:, lead_ms:], np.repeat(a[:, -1:], lead_ms, axis=1)], axis=1)
    pos, vel, acc, jerk = shift(pos), shift(vel), shift(acc), shift(jerk)
    speed = np.linalg.norm(vel, axis=2)
    t = np.arange(WINDOW_MS[0], WINDOW_MS[1])
    decay = np.ones(len(t)) if prep_decay_ms is None else np.exp(-np.clip(t, 0, None) / prep_decay_ms)
    prep_env = np.where(t < prep_onset_ms, 0.0, np.where(t < 0, 1.0, decay))
    end, peak = cond_kin["endpoint"], cond_kin["peak_speed"]
    end_n = (end - end.mean(0)) / end.std()
    peak_n = (peak - peak.mean()) / (peak.std() + 1e-12)
    base = recorded_rates.mean(axis=(0, 1))
    rec_range = recorded_rates.max(axis=(0, 1)) - recorded_rates.min(axis=(0, 1))
    rates = np.zeros((c, nb, n_units))
    for k in range(n_units):
        th = rng.uniform(0, 2 * np.pi)
        pd_ = np.array([np.cos(th), np.sin(th)])
        th_p = rng.uniform(0, 2 * np.pi)
        pdp = np.array([np.cos(th_p), np.sin(th_p)])
        prep_tuning = end_n @ pdp                                    # conditions
        if kind == "velocity":
            move = vel @ pd_ + rng.uniform(0, 1) * speed
            move = move / (np.ptp(move) + 1e-12) * rec_range[k]
            prep_tuning = prep_tuning + rng.normal() * peak_n
            prep = prep_tuning / (np.ptp(prep_tuning) + 1e-12) * 0.5 * rec_range[k]
        elif kind == "complex":
            move = 25 * (pos @ pd_) + 10 * (vel @ pd_) + 1 * (acc @ pd_) + 0.05 * (jerk @ pd_)
            prep = 25 * (end @ pdp)
        else:
            raise ValueError(kind)
        r = base[k] + move - move.mean() + prep[:, None] * prep_env[None, :]
        rates[:, :, k] = np.clip(r, 0, None)
    # gamma(2) spiking by time rescaling; all trials of a condition at once
    out = np.zeros_like(rates)
    for ci in range(c):
        n_tr = int(trials_per_cond[ci])
        cum = np.cumsum(rates[ci], axis=0) / 1000.0                  # bins x units, expected counts
        for k in range(n_units):
            total = cum[-1, k]
            if total <= 0:
                continue
            n_draw = int(total * 1.5 + 30)
            # unit-rate gamma(2) renewal process, started 5 units before the window
            ev = np.cumsum(rng.gamma(2.0, 0.5, (n_tr, n_draw)), axis=1) - 5.0
            ev = ev[(ev >= 0) & (ev < total)]
            bins = np.searchsorted(cum[:, k], ev).clip(0, nb - 1)
            out[ci, :, k] = np.bincount(bins, minlength=nb) / n_tr * 1000.0
    return gaussian_filter1d(out, SIGMA_MS, axis=1, mode="nearest")


def condition_kinematics(session: dict, trial_idx: np.ndarray, align: np.ndarray, conditions: np.ndarray) -> dict:
    """Condition-mean hand kinematics (m, s) and, per condition, target position and peak speed."""
    _, pos, vel, acc, jerk = hand_kinematics(session, trial_idx, align)
    labels = np.unique(conditions)
    mean = lambda a: np.stack([a[conditions == c].mean(axis=0) for c in labels])
    tr = session["trials"].iloc[trial_idx]
    out = {"labels": labels, "pos": mean(pos), "vel": mean(vel), "acc": mean(acc), "jerk": mean(jerk)}
    out["endpoint"] = np.stack([tr[conditions == c][["hit_x", "hit_y"]].mean().values for c in labels]) / 1000.0
    out["peak_speed"] = np.linalg.norm(out["vel"], axis=2).max(axis=1)
    return out


def heading_change(vel: np.ndarray, t0_ms: int = 0, t1_ms: int = WINDOW_MS[1], min_frac: float = 0.1,
                   contiguous: bool = False) -> np.ndarray:
    """Net change of heading (degrees) of each condition's mean hand path between t0 and t1.

    Only samples where speed exceeds `min_frac` of the condition's peak speed are used; with
    `contiguous`, only the unbroken run of such samples around the peak speed. Positive is
    counter-clockwise.
    """
    seg = vel[:, t0_ms - WINDOW_MS[0]: t1_ms - WINDOW_MS[0]]
    out = []
    for v in seg:
        sp = np.linalg.norm(v, axis=1)
        keep = sp > min_frac * sp.max()
        if contiguous:
            run = np.cumsum(~keep)
            keep &= run == run[np.argmax(sp)]
        h = np.unwrap(np.arctan2(v[keep, 1], v[keep, 0]))
        out.append(np.degrees(h[-1] - h[0]) if keep.sum() > 1 else 0.0)
    return np.array(out)


def prep_prediction_r2(proj: np.ndarray) -> float:
    """Leave-one-condition-out R2 of the last state from the first by one complex gain."""
    z0 = proj[:, 0, 0] + 1j * proj[:, 0, 1]
    z1 = proj[:, -1, 0] + 1j * proj[:, -1, 1]
    pred = np.empty_like(z1)
    for i in range(len(z0)):
        m = np.arange(len(z0)) != i
        a = np.sum(np.conj(z0[m]) * z1[m]) / np.sum(np.abs(z0[m]) ** 2)
        pred[i] = a * z0[i]
    return float(1 - np.sum(np.abs(z1 - pred) ** 2) / np.sum(np.abs(z1 - z1.mean()) ** 2))


def prep_prediction_cv(rates: np.ndarray, **jpca_args) -> dict:
    """Prediction of the last state from the first, with jPCA refitted leaving each condition out.

    For each condition, jPCA (normalisation, cross-condition mean, PCs and plane) is fitted on
    the other conditions and the held-out condition is projected onto that plane. Two scores
    of the held-out conditions:

    - r2: R2 of the last state predicted from the first by one complex gain fitted on the
      other conditions (as `prep_prediction_r2`, without the plane seeing the held-out
      condition);
    - phase_score: mean cosine of the error of the last phase predicted as the first phase plus
      the other conditions' circular mean phase advance, with `static_phase_score` the same
      for a prediction of no advance, and `advance_deg` the mean advance itself. A rotation
      shared by all conditions gives a phase score near 1 and above the static one; states
      that do not rotate give a static score as high as the phase score.
    """
    times = np.asarray(jpca_args.pop("times_ms", ANALYSIS_TIMES))
    soft_norm = jpca_args.pop("soft_norm", SOFT_NORM)
    c = rates.shape[0]
    # the normalisation range of each fold is taken over the whole window of its own conditions;
    # the rest of jPCA needs only the analysed times, so the fits run on those bins alone
    cmax, cmin = rates.max(axis=1), rates.min(axis=1)                 # conditions x units
    lo = times[0] - WINDOW_MS[0]
    crop = rates[:, lo:times[-1] - WINDOW_MS[0] + 1].astype(np.float64)
    z0, z1, pred, adv = (np.empty(c, complex) for _ in range(4))
    for i in range(c):
        m = np.arange(c) != i
        norm = cmax[m].max(axis=0) - cmin[m].min(axis=0) + soft_norm
        r = jpca(crop[m] / norm, times_ms=times, window_ms=(times[0], times[-1] + 1), soft_norm=None, **jpca_args)
        tr = r["planes"][0]
        a0, a1 = tr[:, 0, 0] + 1j * tr[:, 0, 1], tr[:, -1, 0] + 1j * tr[:, -1, 1]
        held = project(crop[i:i + 1] / norm, r)[0]
        z0[i], z1[i] = held[0, 0] + 1j * held[0, 1], held[-1, 0] + 1j * held[-1, 1]
        pred[i] = np.sum(np.conj(a0) * a1) / np.sum(np.abs(a0) ** 2) * z0[i]
        adv[i] = np.mean(np.exp(1j * (np.angle(a1) - np.angle(a0))))
    err = np.angle(z1) - np.angle(z0) - np.angle(adv)
    return {"r2": float(1 - np.sum(np.abs(z1 - pred) ** 2) / np.sum(np.abs(z1 - z1.mean()) ** 2)),
            "phase_score": float(np.mean(np.cos(err))),
            "static_phase_score": float(np.mean(np.cos(np.angle(z1) - np.angle(z0)))),
            "advance_deg": float(np.degrees(np.angle(np.mean(adv))))}


def decode_accuracy(X: np.ndarray, y: np.ndarray, rng: np.random.Generator, folds: int = 5) -> float:
    """Cross-validated accuracy of a nearest-centroid classifier on z-scored sqrt counts."""
    X = np.sqrt(X.astype(float))
    order = rng.permutation(len(y))
    fold = np.empty(len(y), int)
    fold[order] = np.arange(len(y)) % folds
    correct = 0
    for k in range(folds):
        tr, te = fold != k, fold == k
        mu, sd = X[tr].mean(0), X[tr].std(0) + 1e-9
        Z, Zt = (X[tr] - mu) / sd, (X[te] - mu) / sd
        labels = np.unique(y[tr])
        cent = np.stack([Z[y[tr] == c].mean(0) for c in labels])
        d = ((Zt[:, None, :] - cent[None]) ** 2).sum(-1)
        correct += np.sum(labels[np.argmin(d, axis=1)] == y[te])
    return correct / len(y)
