"""Loading and measures for Kim & Shin (2025), doi:10.1101/2025.06.30.662469.

Two datasets are streamed from the DANDI Archive at pinned versions; nothing is written to disk.

- Dandiset 000248 (Allen Institute OpenScope Illusion project), the dataset under test. Each
  session's `*_ogen.nwb` file holds the units table (spike times, Allen quality metrics, peak
  channel) and the `ICwcfg1_presentations` table. That table lists every 400 ms frame of the
  block, including the gray inter-trial frames, with the image code in `frame` (0 to 21) and no
  name for the codes.
- Dandiset 000021 (Allen Brain Observatory Visual Coding Neuropixels, Brain Observatory 1.1
  sessions), the paper's main dataset (claims `data: elsewhere`). Each session file holds the
  units table and `natural_scenes_presentations` (frame -1 is the gray image, 0 to 117 the
  scenes).

Where the parameters come from (the claims file is claims/kim-2025.yaml; "code" is
github.com/jhk4839/Neural_variability_robustness at commit ac3300b007c2348ccda73c0c87fb02f557791089):

- V1 units of the Illusion data: peak-channel location containing "VISp" and not "VISpm"
  (claims file, header O3 reading a, from fit_slope_openscope.ipynb cell 5). Reading b adds the
  Allen quality criteria of the Methods (isi_violations < 0.5, amplitude_cutoff < 0.1,
  presence_ratio > 0.9; Methods, "Main dataset and visual stimuli").
- Illusion spike counts: spikes in the 400 ms from stimulus onset (Methods, "Visualization of
  stimulus manifold geometry", paragraph 2). The trial slots of ICwcfg1 are recovered from the
  alternation of trials and gray inter-trial frames (see `illusion_trials`); a gray frame in a
  trial slot is a Blank trial. This is how the code's 12 stimuli with 400 repeats arise (its
  trialorder comes from a post-processed copy that is not public).
- Names of the image codes: the code's map, dict_trial_type in fit_slope_openscope.ipynb
  cell 5 (claims file header), `ILLUSION_NAMES`.
- Natural scenes counts: spikes in the 250 ms from onset; units in VISp passing the Allen
  quality criteria (Methods, "Main dataset and visual stimuli"). `abo_session` returns these
  units with their `quality` label; the notebooks keep only units labelled "good" (`restrict`),
  an assumption: AllenSDK, through which the paper read the data, serves only those by default
  (filter_by_validity, allensdk/brain_observatory/ecephys/probes.py lines 128 to 129 at commit
  a56bd8ea7613a812334602b64746cdd30c325a96), and the paper's unit counts match only with it.
- Natural movie sessions: excluded when a movie frame falls in an `invalid_times` interval
  tagged "stimulus", as AllenSDK's invalid presentations, which the paper's code skips
  (`movie_session`).
- Slope fit (M1), slope manipulation (M2), overlap (M3), geodesic distance (M5), orthogonal
  variance, effective dimensionality: as the claims file header and criteria give them, checked
  against box_and_overlap.py and compute_geo_ortho.py of the code.
- Isomap uses n_neighbors 5 (code). Isomap's eigen-solver is deterministic for the dense
  solver, which is set (`eigen_solver="dense"`), a standard choice that cannot change a result
  beyond numerical precision.
"""

from __future__ import annotations

import h5py
import networkx as nx
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy.sparse.csgraph import shortest_path
from scipy.spatial.distance import cdist
from sklearn.manifold import Isomap
from sklearn.neighbors import kneighbors_graph

DANDISET_ID = "000248"
DANDISET_VERSION = "0.240502.2344"
ABO_ID = "000021"
ABO_VERSION = "0.251116.2246"

# The paper code's order of the Illusion subjects; index 6 is its example session.
CODE_SUBJECTS = ["619296", "620333", "620334", "625545", "625554", "625555", "630506",
                 "631510", "631570", "633229", "637484"]
EXAMPLE_SUBJECT = "630506"

ILLUSION_NAMES = {0: "Blank", 1: "X", 2: "Tc1", 3: "Ic1", 4: "Lc1", 5: "Tc2", 6: "Lc2", 7: "Ic2",
                  8: "Ire1", 9: "Ire2", 10: "Tre1", 11: "Tre2", 12: "Xre1", 13: "Xre2",
                  14: "BR_in", 15: "BL_in", 16: "TL_in", 17: "TR_in", 18: "BR_out",
                  19: "BL_out", 20: "TL_out", 21: "TR_out"}
ILLUSION_WINDOW = 0.4
SCENES_WINDOW = 0.25
PRE_GRAY = 60  # gray frames before the first trial slot of ICwcfg1 (shown in the data check)
TARGET_SLOPES = np.round(np.linspace(0, 2, 21), 1)
QUALITY = dict(isi_violations=0.5, amplitude_cutoff=0.1, presence_ratio=0.9)

_client = None


def _dandiset(dandiset_id, version):
    global _client
    if _client is None:
        _client = DandiAPIClient()
    return _client.get_dandiset(dandiset_id, version)


def asset_paths(dandiset_id=DANDISET_ID, version=DANDISET_VERSION):
    return sorted(a.path for a in _dandiset(dandiset_id, version).get_assets())


def open_nwb(path, dandiset_id=DANDISET_ID, version=DANDISET_VERSION):
    asset = _dandiset(dandiset_id, version).get_asset_by_path(path)
    url = asset.get_content_url(follow_redirects=1, strip_query=True)
    return h5py.File(remfile.File(url), "r")


def _str(values):
    return np.array([v.decode() if isinstance(v, bytes) else str(v) for v in values])


def units_table(f):
    """Units with their peak-channel location and the Allen quality metrics."""
    e = f["general/extracellular_ephys/electrodes"]
    loc = dict(zip(e["id"][:], _str(e["location"][:])))
    u = f["units"]
    df = pd.DataFrame({
        "id": u["id"][:],
        "location": [loc[p] for p in u["peak_channel_id"][:]],
        "quality": _str(u["quality"][:]),
        "isi_violations": u["isi_violations"][:],
        "amplitude_cutoff": u["amplitude_cutoff"][:],
        "presence_ratio": u["presence_ratio"][:],
        "firing_rate": u["firing_rate"][:],
    })
    df["passes_quality"] = ((df.isi_violations < QUALITY["isi_violations"])
                            & (df.amplitude_cutoff < QUALITY["amplitude_cutoff"])
                            & (df.presence_ratio > QUALITY["presence_ratio"]))
    return df


def is_v1(locations, exact=False):
    """VISp and not VISpm (code); with exact=True the location must be exactly 'VISp' (000021)."""
    locs = pd.Series(locations)
    if exact:
        return (locs == "VISp").to_numpy()
    return (locs.str.contains("VISp") & ~locs.str.contains("VISpm")).to_numpy()


def spike_counts(f, unit_rows, onsets, window):
    """Counts (trials x units) of spikes in [onset, onset + window) for the given unit rows."""
    idx = f["units/spike_times_index"][:]
    starts = np.r_[0, idx[:-1]]
    st = f["units/spike_times"]
    onsets = np.asarray(onsets)
    out = np.zeros((len(onsets), len(unit_rows)), dtype=np.float64)
    for j, r in enumerate(unit_rows):
        s = st[starts[r]:idx[r]]
        out[:, j] = np.searchsorted(s, onsets + window, "left") - np.searchsorted(s, onsets, "left")
    return out


def illusion_trials(f, block="ICwcfg1_presentations"):
    """Trial slots of an Illusion block: (onset times, image codes, report dict).

    Presentations last 400 ms with no gap. After PRE_GRAY leading gray frames, trials and gray
    inter-trial frames alternate, so the trial slots are every other presentation from there; a gray frame (code 0) in a trial slot is a Blank trial. The report
    says whether every non-gray frame falls in a trial slot and every slot is followed by a gray
    frame, which checks the reading.
    """
    g = f["intervals"][block]
    frame = g["frame"][:].astype(int)
    start = g["start_time"][:]
    first_image = int(np.argmax(frame != 0))
    last = int(len(frame) - 1 - np.argmax(frame[::-1] != 0))
    # The block opens with PRE_GRAY gray frames; when the first trial is a Blank trial the
    # leading gray run is longer by that trial and its inter-trial frame (two frames each).
    first = PRE_GRAY if first_image >= PRE_GRAY and (first_image - PRE_GRAY) % 2 == 0 else first_image
    slots = np.arange(first, last + 1, 2)
    off = np.setdiff1d(np.arange(first, last + 1), slots)
    report = {
        "presentations": len(frame),
        "leading_gray": first_image,
        "first_slot": first,
        "trailing_gray": len(frame) - 1 - last,
        "non_gray_outside_slots": int((frame[off] != 0).sum()),
        "slots": len(slots),
        "duration_range_s": (float(np.min(g["stop_time"][:] - start)),
                             float(np.max(g["stop_time"][:] - start))),
    }
    return start[slots], frame[slots], report


def illusion_session(path):
    """V1 spike counts (trials x units) and image codes for the 12 stimuli with 400 repeats.

    Returns X (all V1 units, reading a), labels, a per-unit mask of the Allen quality criteria
    (reading b is X[:, mask]), and a report of what was loaded.
    """
    f = open_nwb(path)
    units = units_table(f)
    rows = np.where(is_v1(units.location))[0]
    onsets, codes, report = illusion_trials(f)
    counts = spike_counts(f, rows, onsets, ILLUSION_WINDOW)
    vals, n = np.unique(codes, return_counts=True)
    use = np.isin(codes, vals[n == 400])
    order = np.argsort(codes[use], kind="stable")
    X = counts[use][order]
    labels = codes[use][order]
    mask = units.passes_quality.to_numpy()[rows]
    st = f["units/spike_times"]
    idx = f["units/spike_times_index"][:]
    first = st[int(np.r_[0, idx][rows[0]]):int(idx[rows[0]])] if len(rows) else np.array([])
    report.update(units_total=len(units), v1_units=len(rows), v1_quality=int(mask.sum()),
                  v1_good_label=int((units.quality.to_numpy()[rows] == "good").sum()),
                  v1_locations=dict(units.location.iloc[rows].value_counts()),
                  codes_with_400=[int(v) for v in vals[n == 400]],
                  counts_per_code=dict(zip(vals.tolist(), n.tolist())),
                  first_onset=float(onsets[0]), total_spikes=int(st.shape[0]),
                  first_unit_sorted=bool(np.all(np.diff(first) >= 0)),
                  isi_violations_range=(float(units.isi_violations.min()),
                                        float(units.isi_violations.max())))
    f.close()
    return X, labels, mask, report


def illusion_psth(path, bins=np.arange(-0.2, 0.6001, 0.01)):
    """Population V1 rate (spikes/s per unit) around trial onsets, Blank and non-Blank trials,
    for the clock check."""
    f = open_nwb(path)
    units = units_table(f)
    rows = np.where(is_v1(units.location))[0]
    onsets, codes, _ = illusion_trials(f)
    idx = f["units/spike_times_index"][:]
    starts = np.r_[0, idx[:-1]]
    st = f["units/spike_times"]
    out = {}
    for name, sel in (("blank", codes == 0), ("image", codes != 0)):
        h = np.zeros(len(bins) - 1)
        edges = onsets[sel][:, None] + bins[None, :]
        for r in rows:
            s = st[starts[r]:idx[r]]
            h += np.diff(np.searchsorted(s, edges), axis=1).sum(0)
        out[name] = h / (sel.sum() * len(rows) * np.diff(bins))
    f.close()
    return bins, out


# ---------------------------------------------------------------- measures

def fit_slopes(X, labels):
    """M1: per stimulus, OLS of log10 variance (ddof 1) on log10 mean over neurons with mean > 0.

    Returns a DataFrame indexed by stimulus with slope, intercept and the number of neurons.
    """
    rows = []
    for c in np.unique(labels):
        Y = X[labels == c]
        m, v = Y.mean(0), Y.var(0, ddof=1)
        ok = (m > 0) & (v > 0)
        s, i = np.polyfit(np.log10(m[ok]), np.log10(v[ok]), 1)
        rows.append((c, s, i, int(ok.sum())))
    return pd.DataFrame(rows, columns=["stimulus", "slope", "intercept", "n"]).set_index("stimulus")


def manipulate(X, labels, target, fits=None):
    """M2: rescale each trial's residual so that the stimulus's log-mean vs log-variance slope
    becomes `target`, keeping the mean log variance over neurons (box_and_overlap.py)."""
    if fits is None:
        fits = fit_slopes(X, labels)
    out = np.zeros_like(X, dtype=np.float64)
    for c in np.unique(labels):
        sel = labels == c
        Y = X[sel]
        m, v = Y.mean(0), Y.var(0, ddof=1)
        ok = (m > 0) & (v > 0)
        s, i = fits.loc[c, "slope"], fits.loc[c, "intercept"]
        logm = np.log10(m[ok])
        new_logv = (np.log10(v[ok]) - i) / s * target + (s - target) * logm.mean() + i
        Z = np.repeat(m[None, :], Y.shape[0], 0)
        Z[:, ok] = m[ok] + (Y[:, ok] - m[ok]) / np.sqrt(v[ok]) * np.sqrt(10 ** new_logv)
        out[sel] = Z
    return out


def overlap_matrix(X, labels, variant="methods"):
    """M3: O[b, a] = fraction of a's trials whose nearest trial of b lies within the 5th
    percentile of b's within-manifold pairwise distances.

    variant "methods": the percentile over pairs of distinct trials, distances < threshold.
    variant "code": the percentile over the full self-distance matrix with its zero diagonal,
    distances <= threshold (box_and_overlap.py). The diagonal (self-overlap) is set to 1.
    """
    stims = np.unique(labels)
    groups = [X[labels == c] for c in stims]
    thr = np.zeros(len(stims))
    for k, G in enumerate(groups):
        D = cdist(G, G)
        if variant == "methods":
            thr[k] = np.percentile(D[np.triu_indices(len(G), 1)], 5)
        else:
            thr[k] = np.percentile(D, 5)
    O = np.ones((len(stims), len(stims)))
    for b, Gb in enumerate(groups):
        for a, Ga in enumerate(groups):
            if a == b:
                continue
            nn = cdist(Ga, Gb).min(1)
            O[b, a] = np.mean(nn < thr[b]) if variant == "methods" else np.mean(nn <= thr[b])
    return O, stims


def largest_scc(O, nodes=None):
    """Size of the largest strongly connected component; edge a -> b when O[b, a] > 0."""
    n = O.shape[0]
    nodes = range(n) if nodes is None else nodes
    g = nx.DiGraph()
    g.add_nodes_from(nodes)
    for b in nodes:
        for a in nodes:
            if a != b and O[b, a] > 0:
                g.add_edge(a, b)
    return max(len(c) for c in nx.strongly_connected_components(g))


def in_one_scc(O, nodes):
    """Whether the given nodes lie in one strongly connected component of the graph over all
    stimuli (edge a -> b when O[b, a] > 0), so that paths may pass through other stimuli."""
    g = nx.DiGraph()
    g.add_nodes_from(range(O.shape[0]))
    g.add_edges_from((a, b) for b in range(O.shape[0]) for a in range(O.shape[0]) if a != b and O[b, a] > 0)
    return any(set(nodes) <= c for c in nx.strongly_connected_components(g))


def mean_offdiag(O, nodes=None):
    nodes = list(range(O.shape[0])) if nodes is None else list(nodes)
    sub = O[np.ix_(nodes, nodes)]
    return float(sub[~np.eye(len(nodes), dtype=bool)].mean())


def effective_dimensionality(X, labels):
    """Participation ratio of the covariance eigenvalues over N, per stimulus (Methods)."""
    out = []
    for c in np.unique(labels):
        ev = np.clip(np.linalg.eigvalsh(np.cov(X[labels == c], rowvar=False)), 0, None)
        out.append(ev.sum() ** 2 / (ev ** 2).sum() / X.shape[1])
    return np.array(out)


def isomap_embed(X, n_components=2):
    iso = Isomap(n_neighbors=5, n_components=n_components, eigen_solver="dense")
    return iso.fit_transform(X)


def centroid_geodesics(X, labels):
    """M5: geodesic distances among stimulus centroids, Isomap (n_neighbors 5) fitted on all
    trials with the centroids appended (compute_geo_ortho.py)."""
    stims = np.unique(labels)
    C = np.array([X[labels == c].mean(0) for c in stims])
    # Isomap's own geodesic step: a 5-nearest-neighbour distance graph and undirected shortest
    # paths (sklearn.manifold.Isomap.dist_matrix_), without its eigendecomposition.
    graph = kneighbors_graph(np.vstack([X, C]), n_neighbors=5, mode="distance")
    D = shortest_path(graph, directed=False, indices=np.arange(len(X), len(X) + len(C)))
    return D[:, len(X):], stims


def orthogonal_variance(X, labels, a, b):
    """Variance (ddof 1) over a's trials of the length of each trial's deviation from a's
    centroid projected on the line from a's centroid to b's, over a's summed per-neuron
    variance (Methods, "Orthogonal variance"; compute_geo_ortho.py)."""
    A = X[labels == a]
    ca, cb = A.mean(0), X[labels == b].mean(0)
    d = cb - ca
    proj = np.abs((A - ca) @ d) / np.linalg.norm(d)
    return proj.var(ddof=1) / A.var(0, ddof=1).sum()


# ---------------------------------------------------------------- Allen Visual Coding (000021)

ABO_AREAS = {"V1": "VISp", "LM": "VISl", "RL": "VISrl", "AL": "VISal", "PM": "VISpm", "AM": "VISam"}
SILENT_TRIAL_LIMIT = 0.10  # Methods: sessions with more than 10% of trials silent in all V1 units


def abo_session(path, areas=tuple(ABO_AREAS)):
    """Natural scenes spike counts (250 ms from onset) of the units of V1 and the five higher
    visual areas that pass the Allen quality criteria, trials sorted by stimulus (frame -1 is
    the gray image). Also the mean running speed (cm/s) of each trial over the same window."""
    f = open_nwb(path, ABO_ID, ABO_VERSION)
    units = units_table(f)
    area = np.full(len(units), "", dtype=object)
    for name in areas:
        area[(units.location == ABO_AREAS[name]).to_numpy()] = name
    rows = np.where((area != "") & units.passes_quality.to_numpy())[0]
    g = f["intervals/natural_scenes_presentations"]
    frame = g["frame"][:].astype(int)
    onsets = g["start_time"][:]
    order = np.lexsort((onsets, frame))
    counts = spike_counts(f, rows, onsets[order], SCENES_WINDOW)
    rs = f["processing/running/running_speed"]
    rt, rv = rs["timestamps"][:], rs["data"][:]
    a = np.searchsorted(rt, onsets[order])
    b = np.searchsorted(rt, onsets[order] + SCENES_WINDOW)
    csum = np.r_[0, np.cumsum(rv)]
    with np.errstate(invalid="ignore"):
        speed = (csum[b] - csum[a]) / (b - a)
    info = dict(path=path, units_total=len(units),
                eye_tracking=("EyeTracking" in f["acquisition"]) or any("eye" in k.lower() and "rig" not in k.lower()
                                                                     for k in f["processing"].keys()),
                area_units_all={k: int((units.location == v).sum()) for k, v in ABO_AREAS.items()},
                running_unit=rs["data"].attrs.get("unit"), trials=len(frame),
                isi_range=(float(units.isi_violations.min()), float(units.isi_violations.max())))
    f.close()
    return dict(X=counts, labels=frame[order], area=area[rows], speed=speed, info=info,
                good=(units.quality.to_numpy()[rows] == "good"))


def silent_fraction(X):
    return float(np.mean(X.sum(1) == 0))


def overlap_matrices_fast(X, labels):
    """Both readings of overlap_matrix (methods, code) from one squared-distance matrix, for
    equal numbers of trials per stimulus. Returns (O_methods, O_code, stims)."""
    stims, n = np.unique(labels, return_counts=True)
    if len(set(n)) > 1:
        return overlap_matrix(X, labels, "methods")[0], overlap_matrix(X, labels, "code")[0], stims
    S, R = len(stims), n[0]
    Xs = X[np.argsort(labels, kind="stable")].astype(np.float64)
    sq = (Xs ** 2).sum(1)
    D2 = sq[:, None] + sq[None, :] - 2 * Xs @ Xs.T
    np.maximum(D2, 0, out=D2)
    iu = np.triu_indices(R, 1)
    thr_m, thr_c = np.zeros(S), np.zeros(S)
    for k in range(S):
        block = D2[k * R:(k + 1) * R, k * R:(k + 1) * R].copy()
        np.fill_diagonal(block, 0)
        block = np.sqrt(block)
        thr_m[k] = np.percentile(block[iu], 5)
        thr_c[k] = np.percentile(block, 5)
    nn = np.sqrt(D2.reshape(S * R, S, R).min(2))     # trial of a x stimulus b
    O_m = (nn < thr_m[None, :]).reshape(S, R, S).mean(1).T
    O_c = (nn <= thr_c[None, :]).reshape(S, R, S).mean(1).T
    np.fill_diagonal(O_m, 1.0)
    np.fill_diagonal(O_c, 1.0)
    return O_m, O_c, stims


def rsm(X, labels, n_trials=None):
    """Mean over unordered pairs of trial indices (r1 < r2) of the cosine similarity between
    stimulus i's trial r1 and stimulus j's trial r2, ignoring zero vectors as the code's
    nanmean does (RSA_decoding.py). X rows sorted by stimulus; n_trials keeps the first n."""
    stims = np.unique(labels)
    R = min(np.sum(labels == s) for s in stims) if n_trials is None else n_trials
    T = np.stack([X[labels == s][:R] for s in stims])          # S x R x N
    norm = np.linalg.norm(T, axis=2, keepdims=True)
    valid = (norm[..., 0] > 0).astype(float)
    U = np.divide(T, norm, out=np.zeros_like(T), where=norm > 0)
    cumU = np.cumsum(U[:, ::-1], axis=1)[:, ::-1]               # sum over r2 >= r
    cumV = np.cumsum(valid[:, ::-1], axis=1)[:, ::-1]
    later_U = np.concatenate([cumU[:, 1:], np.zeros_like(cumU[:, :1])], axis=1)
    later_V = np.concatenate([cumV[:, 1:], np.zeros_like(cumV[:, :1])], axis=1)
    num = np.einsum("irn,jrn->ij", U, later_U)
    den = np.einsum("ir,jr->ij", valid, later_V)
    return num / den


def shuffle_within_stimulus(X, labels, rng):
    """Permute the trial order within each stimulus, separately for each neuron, which destroys
    pairwise noise correlations (Figure S4C; Discussion, paragraph 5, "shuffling the trial order
    for each neuron within each trial type")."""
    Y = X.copy()
    for s in np.unique(labels):
        idx = np.where(labels == s)[0]
        for j in range(X.shape[1]):
            Y[idx, j] = X[rng.permutation(idx), j]
    return Y


def restrict(s, mask):
    """A session of abo_session keeping only the units in mask (aligned with s["X"]'s columns)."""
    return dict(s, X=s["X"][:, mask], area=s["area"][mask], good=s["good"][mask])


def pc1_fraction(X, labels):
    """Fraction of variance on the first principal component of each stimulus manifold."""
    out = []
    for c in np.unique(labels):
        ev = np.clip(np.linalg.eigvalsh(np.cov(X[labels == c], rowvar=False)), 0, None)
        out.append(ev[-1] / ev.sum() if ev.sum() > 0 else np.nan)
    return np.array(out)


def occupied_voxels(Y, Xref):
    """Unit voxels (edge 1 spike) occupied by the points of Y inside the box of Xref
    (min - 1 to max + 1 per neuron), compute_percent_filled in box_and_overlap.py."""
    lo, hi = Xref.min(0) - 1, Xref.max(0) + 1
    inside = np.all((Y >= lo) & (Y <= hi), axis=1)
    P = Y[inside]
    if len(P) == 0:
        return 0
    return len(np.unique(np.floor(P - P.min(0)), axis=0))


def across_stimulus_slopes(X, labels):
    """Per neuron, OLS of log10 variance on log10 mean across stimuli with mean > 0
    (Methods, "Log-mean vs. log-variance relationship across stimuli")."""
    stims = np.unique(labels)
    M = np.array([X[labels == s].mean(0) for s in stims])
    V = np.array([X[labels == s].var(0, ddof=1) for s in stims])
    out = []
    for j in range(X.shape[1]):
        ok = (M[:, j] > 0) & (V[:, j] > 0)
        out.append(np.polyfit(np.log10(M[ok, j]), np.log10(V[ok, j]), 1)[0] if ok.sum() >= 2 else np.nan)
    return np.array(out)


def orthogonal_variances(X, labels):
    """orthogonal_variance for every ordered pair: V[a, b] (diagonal NaN)."""
    stims = np.unique(labels)
    C = np.array([X[labels == c].mean(0) for c in stims])
    V = np.full((len(stims), len(stims)), np.nan)
    for i, a in enumerate(stims):
        A = X[labels == a]
        d = C - C[i]
        nrm = np.linalg.norm(d, axis=1)
        nrm[i] = 1.0
        proj = np.abs((A - C[i]) @ d.T) / nrm
        v = proj.var(0, ddof=1) / A.var(0, ddof=1).sum()
        v[i] = np.nan
        V[i] = v
    return V


def pc1_vectors(X, labels):
    """First principal component of each stimulus manifold and of all other stimuli's trials."""
    stims = np.unique(labels)
    own, rest = [], []
    for c in stims:
        A, B = X[labels == c], X[labels != c]
        own.append(np.linalg.eigh(np.cov(A, rowvar=False))[1][:, -1])
        rest.append(np.linalg.eigh(np.cov(B, rowvar=False))[1][:, -1])
    return np.array(own), np.array(rest)


def _abs_cos(u, v):
    return np.abs(np.sum(u * v, 1)) / (np.linalg.norm(u, axis=1) * np.linalg.norm(v, axis=1))


def _offdiag(M):
    return M[~np.eye(M.shape[0], dtype=bool)]


def session_measures(X, labels, seeds, areas=None, n_partitions=10, slopes=TARGET_SLOPES,
                     do_halves=True):
    """All per-session measures of the natural scenes claims, for the as-is data and each
    target slope. `seeds` maps a claim id to its seed (zlib.crc32 of "kim-2025/<claim id>");
    `areas` maps an area name to its own count matrix (higher visual areas, Figure S6).

    The nearest-neighbour manifold for local alignment is taken from the as-is geodesic
    distances, as local_global_alignment.py does (the per-slope neighbour is a variant).
    """
    from scipy.stats import spearmanr
    stims, n = np.unique(labels, return_counts=True)
    R = n.min()
    fits = fit_slopes(X, labels)
    conds = ["as-is"] + [float(s) for s in slopes]
    out = {k: {} for k in ("dim", "pc1", "O_m", "O_c", "vox", "geo_rho", "local", "local_slope_nn",
                           "global", "rsm", "rsm_half", "ov_half", "ov_half_off", "nc_maxdiff")}
    out["area_rsm"], out["area_rsm_half"] = {}, {}
    rng_trials = np.random.default_rng(seeds["fig4e-rsm-similarity-across-mice"])
    perm = {c: rng_trials.permutation(np.sum(labels == c))[:R] for c in stims}
    def take_rsm(Y, lab):
        Z = np.concatenate([Y[lab == c][perm[c]] for c in stims])
        return rsm(Z, np.repeat(stims, R))
    rng_part = np.random.default_rng(seeds["fig4c-rsm-similarity-within-mice"])
    parts = [rng_part.permutation(X.shape[1]) for _ in range(n_partitions)]
    rng_ov = np.random.default_rng(seeds["fig4a-overlap-consistency-within-mice"])
    parts_ov = [rng_ov.permutation(X.shape[1]) for _ in range(n_partitions)]
    h = X.shape[1] // 2
    D0, _ = centroid_geodesics(X, labels)
    nn_asis = np.array([np.argmin(np.where(np.eye(len(stims))[i] > 0, np.inf, D0[i])) for i in range(len(stims))])
    nc_asis = None
    area_fits = {a: fit_slopes(Xa, labels) for a, Xa in (areas or {}).items()}
    for c in conds:
        Y = X if c == "as-is" else manipulate(X, labels, c, fits)
        out["dim"][c] = effective_dimensionality(Y, labels)
        out["pc1"][c] = pc1_fraction(Y, labels)
        O_m, O_c, _ = overlap_matrices_fast(Y, labels)
        out["O_m"][c], out["O_c"][c] = O_m.astype(np.float32), O_c.astype(np.float32)
        out["vox"][c] = occupied_voxels(Y, X)
        D, _ = centroid_geodesics(Y, labels)
        V = orthogonal_variances(Y, labels)
        out["geo_rho"][c] = spearmanr(_offdiag(D), _offdiag(V)).statistic
        own, rest = pc1_vectors(Y, labels)
        nn_c = np.array([np.argmin(np.where(np.eye(len(stims))[i] > 0, np.inf, D[i])) for i in range(len(stims))])
        out["local"][c] = _abs_cos(own, own[nn_asis]).mean()
        out["local_slope_nn"][c] = _abs_cos(own, own[nn_c]).mean()
        out["global"][c] = _abs_cos(own, rest).mean()
        out["rsm"][c] = take_rsm(Y, labels).astype(np.float32)
        rh = []
        for pmt in parts:
            a, b = pmt[:h], pmt[h:2 * h]
            rh.append(spearmanr(take_rsm(Y[:, a], labels).ravel(), take_rsm(Y[:, b], labels).ravel(),
                                nan_policy="omit").statistic)
        out["rsm_half"][c] = float(np.mean(rh))
        if do_halves:
            oh, oh_off = [], []
            for pmt in parts_ov:
                a, b = pmt[:h], pmt[h:2 * h]
                Oa, Ob = overlap_matrices_fast(Y[:, a], labels)[0], overlap_matrices_fast(Y[:, b], labels)[0]
                oh.append(spearmanr(Oa.ravel(), Ob.ravel()).statistic)
                oh_off.append(spearmanr(_offdiag(Oa), _offdiag(Ob)).statistic)
            out["ov_half"][c], out["ov_half_off"][c] = float(np.mean(oh)), float(np.mean(oh_off))
        if c in ("as-is", 0.0, 1.0, 2.0):
            nc = []
            for s_ in stims:
                with np.errstate(invalid="ignore", divide="ignore"):
                    nc.append(np.corrcoef(Y[labels == s_], rowvar=False))
            nc = np.array(nc)
            if c == "as-is":
                nc_asis = nc
            else:
                out["nc_maxdiff"][c] = float(np.nanmax(np.abs(nc - nc_asis)))
        for a, Xa in (areas or {}).items():
            Ya = Xa if c == "as-is" else manipulate(Xa, labels, c, area_fits[a])
            out["area_rsm"].setdefault(a, {})[c] = take_rsm(Ya, labels).astype(np.float32)
            ha = Xa.shape[1] // 2
            rng_a = np.random.default_rng(seeds["figs6-higher-areas-consistency"])
            rh = []
            for _ in range(n_partitions):
                pmt = rng_a.permutation(Xa.shape[1])
                rh.append(spearmanr(take_rsm(Ya[:, pmt[:ha]], labels).ravel(),
                                    take_rsm(Ya[:, pmt[ha:2 * ha]], labels).ravel(), nan_policy="omit").statistic)
            out["area_rsm_half"].setdefault(a, {})[c] = float(np.mean(rh))
    out["asis_geo"], out["asis_ortho"] = D0, orthogonal_variances(X, labels)
    out["fits"] = fits
    return out


def random_measures(X, labels, seeds, areas=None, n_partitions=10, slopes=TARGET_SLOPES):
    """The RSM-based measures of session_measures alone (Figures 4C, 4E, S6), for the seed checks."""
    from scipy.stats import spearmanr
    stims, n = np.unique(labels, return_counts=True)
    R = n.min()
    fits = fit_slopes(X, labels)
    rng_trials = np.random.default_rng(seeds["fig4e-rsm-similarity-across-mice"])
    perm = {c: rng_trials.permutation(np.sum(labels == c))[:R] for c in stims}
    def take_rsm(Y, lab):
        Z = np.concatenate([Y[lab == c][perm[c]] for c in stims])
        return rsm(Z, np.repeat(stims, R))
    rng_part = np.random.default_rng(seeds["fig4c-rsm-similarity-within-mice"])
    parts = [rng_part.permutation(X.shape[1]) for _ in range(n_partitions)]
    h = X.shape[1] // 2
    area_fits = {a: fit_slopes(Xa, labels) for a, Xa in (areas or {}).items()}
    out = {"rsm": {}, "rsm_half": {}, "area_rsm": {}, "area_rsm_half": {}}
    for c in ["as-is"] + [float(s) for s in slopes]:
        Y = X if c == "as-is" else manipulate(X, labels, c, fits)
        out["rsm"][c] = take_rsm(Y, labels).astype(np.float32)
        out["rsm_half"][c] = float(np.mean([spearmanr(take_rsm(Y[:, p[:h]], labels).ravel(),
                                                      take_rsm(Y[:, p[h:2 * h]], labels).ravel(),
                                                      nan_policy="omit").statistic for p in parts]))
        for a, Xa in (areas or {}).items():
            Ya = Xa if c == "as-is" else manipulate(Xa, labels, c, area_fits[a])
            out["area_rsm"].setdefault(a, {})[c] = take_rsm(Ya, labels).astype(np.float32)
            ha = Xa.shape[1] // 2
            rng_a = np.random.default_rng(seeds["figs6-higher-areas-consistency"])
            rh = []
            for _ in range(n_partitions):
                pmt = rng_a.permutation(Xa.shape[1])
                rh.append(spearmanr(take_rsm(Ya[:, pmt[:ha]], labels).ravel(),
                                    take_rsm(Ya[:, pmt[ha:2 * ha]], labels).ravel(), nan_policy="omit").statistic)
            out["area_rsm_half"].setdefault(a, {})[c] = float(np.mean(rh))
    return out


def decode_session(X, labels, target, seed, n_splits=10, shuffle_neurons=False, shuffle_seed=None):
    """Linear SVC (sklearn SVC, kernel linear, default C) accuracy of stimulus identity, 10-fold
    StratifiedKFold without shuffling after a random reordering of trials within stimulus, counts
    centred by the training mean per fold (RSA_decoding.py, decode_ABO). Trials are cut to the
    smallest repeat count. With shuffle_neurons, each neuron's trials are permuted within
    stimulus before the slope change (Figure S4C), by a generator seeded with shuffle_seed, so
    that the trial order and folds, set by seed, are those of the unshuffled decoding. target
    None is the as-is data."""
    from sklearn.model_selection import StratifiedKFold
    from sklearn.svm import SVC
    rng = np.random.default_rng(seed)
    stims, n = np.unique(labels, return_counts=True)
    R = n.min()
    T = np.stack([X[labels == c][:R] for c in stims])           # S x R x N
    if shuffle_neurons:
        srng = np.random.default_rng(shuffle_seed)
        for j in range(T.shape[2]):            # one permutation per neuron, as the code
            T[:, :, j] = T[:, srng.permutation(R), j]
    Xc = T.reshape(-1, T.shape[2])
    lab = np.repeat(stims, R)
    if target is not None:
        Xc = manipulate(Xc, lab, target)
    T = Xc.reshape(len(stims), R, -1)
    for i in range(len(stims)):
        T[i] = T[i, rng.permutation(R)]
    Xc = T.reshape(-1, T.shape[2])
    acc = []
    for tr, te in StratifiedKFold(n_splits).split(Xc, lab):
        m = Xc[tr].mean(0)
        acc.append(SVC(kernel="linear").fit(Xc[tr] - m, lab[tr]).score(Xc[te] - m, lab[te]))
    return float(np.mean(acc))


FC_ID = "000022"
FC_VERSION = "0.251116.2247"
MOVIE_BIN_FRAMES = 12  # Methods: 12-frame (400 ms) bins of natural movie one, 75 bins


def movie_session(path):
    """V1 (VISp, quality criteria) spike counts in each 12-frame bin of every repeat of natural
    movie one, Functional Connectivity session of dandiset 000022. Returns counts (repeats*bins x
    units), bin labels, the units' "good" label, and a report; a repeat is kept only when it holds
    all 900 frames in order.

    The report also gives, for the movie block, the longest repeat and the longest interval between
    consecutive frames within a repeat (a 30 s repeat at 30 Hz has 33 ms frames), and the number of
    movie frames inside an `invalid_times` interval tagged "stimulus". The paper's code skips the
    sessions whose AllenSDK stimulus table marks movie one presentations as invalid
    ("movie one presentation had trouble in some trials...stimtable.stimulus_name
    'invalid_presentation' (session 5, 14, 43)", extract_natural_movie_neuropixels.m lines 19 and
    101 at ac3300b); these are the intervals AllenSDK takes the invalid presentations from."""
    f = open_nwb(path, FC_ID, FC_VERSION)
    units = units_table(f)
    rows = np.where((units.location == "VISp").to_numpy() & units.passes_quality.to_numpy())[0]
    g = f["intervals/natural_movie_one_more_repeats_presentations"]  # 60 repeats, the "natural movie one" block of these sessions
    frame = g["frame"][:].astype(int)
    start, stop = g["start_time"][:], g["stop_time"][:]
    invalid = 0
    if "invalid_times" in f["intervals"]:
        iv = f["intervals/invalid_times"]
        tags, ti = _str(iv["tags"][:]), iv["tags_index"][:]
        t0 = np.r_[0, ti[:-1]]
        for s0, s1, i0, i1 in zip(iv["start_time"][:], iv["stop_time"][:], t0, ti):
            if "stimulus" in tags[i0:i1]:
                invalid += int(np.sum((start >= s0) & (start <= s1)))
    heads = np.where(frame == 0)[0]
    reps, bad = [], 0
    for h in heads:
        seg = frame[h:h + 900]
        if len(seg) == 900 and np.array_equal(seg, np.arange(900)):
            reps.append(h)
        else:
            bad += 1
    rep_dur = [stop[h + 899] - start[h] for h in reps]
    gap = [np.diff(start[h:h + 900]).max() for h in reps]
    nb = 900 // MOVIE_BIN_FRAMES
    on, off, lab = [], [], []
    for h in reps:
        for b in range(nb):
            on.append(start[h + b * MOVIE_BIN_FRAMES]); off.append(stop[h + (b + 1) * MOVIE_BIN_FRAMES - 1]); lab.append(b)
    on, off = np.array(on), np.array(off)
    idx = f["units/spike_times_index"][:]
    starts = np.r_[0, idx[:-1]]
    st = f["units/spike_times"]
    X = np.zeros((len(on), len(rows)))
    for j, r in enumerate(rows):
        s = st[starts[r]:idx[r]]
        X[:, j] = np.searchsorted(s, off, "left") - np.searchsorted(s, on, "left")
    good = units.quality.to_numpy()[rows] == "good"
    rep = dict(path=path, repeats_complete=len(reps), repeats_incomplete=bad, v1_units=len(rows),
               v1_good=int(good.sum()), invalid_stimulus_frames=invalid,
               longest_repeat_s=round(float(max(rep_dur)), 3) if reps else np.nan,
               longest_frame_gap_s=round(float(max(gap)), 3) if reps else np.nan,
               bin_s=(round(float(np.min(off - on)), 3) if len(on) else np.nan, round(float(np.max(off - on)), 3) if len(on) else np.nan))
    f.close()
    return X, np.array(lab), good, rep


def movie_invalid_frames(path, dandiset_id, version):
    """For each natural movie one table of a session file, the number of frames whose onset lies in
    an `invalid_times` interval tagged "stimulus" (the rule of movie_session), and the tags of all
    invalid_times intervals."""
    f = open_nwb(path, dandiset_id, version)
    out = dict(session=path.split("/")[0], intervals=[])
    iv = []
    if "invalid_times" in f["intervals"]:
        g = f["intervals/invalid_times"]
        tags, ti = _str(g["tags"][:]), g["tags_index"][:]
        t0 = np.r_[0, ti[:-1]]
        for s0, s1, i0, i1 in zip(g["start_time"][:], g["stop_time"][:], t0, ti):
            out["intervals"].append((round(float(s0), 1), round(float(s1), 1), ",".join(tags[i0:i1])))
            if "stimulus" in tags[i0:i1]:
                iv.append((s0, s1))
    for name in sorted(k for k in f["intervals"] if k.startswith("natural_movie_one")):
        start = f[f"intervals/{name}/start_time"][:]
        out[name] = int(sum(np.sum((start >= s0) & (start <= s1)) for s0, s1 in iv))
    f.close()
    return out


def abo_pupil(path, onsets, window=SCENES_WINDOW):
    """Mean pupil area (pixels^2, `processing/filtered_gaze_mapping/pupil_area`, the blink-filtered
    series AllenSDK serves as pupil area) over [onset, onset + window) of each trial; None when
    the session has no eye tracking."""
    f = open_nwb(path, ABO_ID, ABO_VERSION)
    if "filtered_gaze_mapping" not in f["processing"]:
        f.close()
        return None
    g = f["processing/filtered_gaze_mapping/pupil_area"]
    t, v = g["timestamps"][:], g["data"][:]
    f.close()
    a = np.searchsorted(t, onsets)
    b = np.searchsorted(t, onsets + window)
    ok = np.isfinite(v)
    cs = np.r_[0, np.cumsum(np.where(ok, v, 0))]
    cn = np.r_[0, np.cumsum(ok)]
    with np.errstate(invalid="ignore", divide="ignore"):
        return (cs[b] - cs[a]) / (cn[b] - cn[a])


def abo_onsets(path):
    """Natural scenes onsets in the order abo_session sorts its trials."""
    f = open_nwb(path, ABO_ID, ABO_VERSION)
    g = f["intervals/natural_scenes_presentations"]
    frame, onsets = g["frame"][:].astype(int), g["start_time"][:]
    f.close()
    return onsets[np.lexsort((onsets, frame))]
