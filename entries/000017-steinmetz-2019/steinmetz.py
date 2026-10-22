"""Loading and measures for dandiset 000017, Steinmetz, Zatka-Haas, Carandini & Harris (2019).

"Distributed coding of choice, action and engagement across the mouse brain", Nature 576,
266-273, doi:10.1038/s41586-019-1787-x. The claims tested are in
claims/000017/10.1038-s41586-019-1787-x.yaml; definitions T, N, K, M and R below are those of the
claims file's opening comment.

Each NWB file holds one session: a trials table, the detected wheel movements (onset, offset and
type, the output of findWheelMoves3), the wheel position, Kilosort/phy units with their spike
times, the brain location of every channel, the passive replay events, pupil area and face motion
energy. Files are streamed from the archive at the pinned version; nothing is written to disk.

What the files hold and how it is read here:

- A unit's channel is row `peak_channel - 1` of the electrodes table. The units table's
  `electrodes` column points to the first probe's rows for units on the second and third probes
  (shown in the notebook), so it is not used.
- The `rate` attribute of the regular time series (wheel position, lick piezo, face motion
  energy) holds the sampling interval in seconds, not a rate in Hz; it is read as an interval.
- `wheel_moves` keeps its onsets and offsets alternately in `timestamps` (twice as many as
  `data`, which holds the type: 0 flinch, 1 left turn, 2 right turn).
- `response_choice` is +1 for a Left choice, -1 for Right, 0 for NoGo. Wheel position increases
  for left turns. Recordings are in the left hemisphere, so right stimuli and Right choices are
  contralateral (claims file).

Where the parameters come from: windows, bins, thresholds and smoothing are from the claim's
criterion or the definitions of the claims file, which cite the paper's Methods and code
(github.com/nsteinme/steinmetz-et-al-2019 at commit 9a0bea8). Where a value is a standard
choice for a detail that cannot change a result, the docstring says so.
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
import requests

DANDISET_ID = "000017"
DANDISET_VERSION = "0.240329.1926"
API = "https://api.dandiarchive.org/api"

# Spike count tensors: 5 ms bins from -0.4 to 0.65 s around each event (a window covering every
# window the claims use, with room for the causal smoothing).
BIN = 0.005
T0, T1 = -0.4, 0.65
NBINS = int(round((T1 - T0) / BIN))
BIN_EDGES = T0 + BIN * np.arange(NBINS + 1)
BIN_CENTRES = BIN_EDGES[:-1] + BIN / 2

CONTRASTS = (0.0, 0.25, 0.5, 1.0)   # zero, low, medium, high

# The 42 regions of Extended Data Table 1, with its counts (recordings, mice, responsive neurons,
# neurons). VISl and VISrl are printed "VISI" and "VISrI" in the text.
ED_TABLE_1 = {
    "ACA": (11, 8, 395, 608), "ACB": (3, 3, 152, 255), "APN": (2, 2, 177, 235),
    "BLA": (2, 2, 107, 261), "CA1": (21, 10, 494, 1129), "CA3": (10, 6, 243, 438),
    "CP": (5, 5, 524, 914), "DG": (16, 10, 336, 711), "GPe": (3, 3, 146, 274),
    "ILA": (3, 3, 192, 338), "LD": (6, 5, 209, 308), "LGd": (10, 5, 397, 811),
    "LP": (11, 8, 393, 732), "LS": (7, 5, 508, 844), "MD": (3, 3, 244, 381),
    "MG": (2, 2, 180, 276), "MOp": (3, 3, 553, 682), "MOs": (19, 9, 993, 1534),
    "MRN": (11, 7, 722, 857), "OLF": (9, 5, 210, 684), "ORB": (6, 5, 281, 770),
    "PAG": (3, 3, 72, 130), "PL": (10, 7, 438, 728), "PO": (5, 4, 342, 620),
    "POL": (3, 3, 132, 190), "POST": (4, 3, 163, 272), "RSP": (9, 5, 308, 598),
    "RT": (2, 2, 111, 160), "SCm": (11, 6, 738, 997), "SCs": (10, 6, 192, 317),
    "SNr": (4, 3, 201, 274), "SSp": (5, 4, 296, 461), "SUB": (9, 7, 494, 669),
    "VISa": (5, 4, 207, 285), "VISam": (11, 8, 501, 805), "VISl": (3, 2, 248, 403),
    "VISp": (12, 8, 649, 923), "VISpm": (4, 4, 230, 516), "VISrl": (2, 2, 85, 236),
    "VPL": (4, 3, 202, 255), "VPM": (4, 2, 235, 357), "ZI": (4, 2, 167, 220),
}
REGIONS_42 = tuple(ED_TABLE_1)

# Region groups of the claims file (code utils/brainRegionGroups.m and the Methods).
VIS = ("VISp", "VISpm", "VISl", "VISrl", "VISa", "VISam")
FRONTAL_JPECC = ("MOs", "MOp", "PL")
MIDBRAIN_JPECC = ("MRN", "SCm", "SNr", "ZI")
STRIATUM = ("CP",)
NEOCORTEX = ("ACA", "ILA", "MOp", "MOs", "ORB", "PL", "RSP", "SSp") + VIS
VISUAL_THALAMUS = ("LGd", "LP", "LD")
THALAMUS = ("LP", "LD", "RT", "MD", "MG", "LGd", "VPM", "VPL", "PO", "POL")
FIRST_ORDER_THALAMUS = ("LGd", "VPL", "VPM", "MG")
GROUP_MIDBRAIN = ("MRN", "SCm", "SCs", "APN", "PAG")
GROUP_BASAL_GANGLIA = ("CP", "GPe", "SNr", "ACB", "LS")
GROUP_HIPPOCAMPUS = ("POST", "SUB", "DG", "CA1", "CA3")


# ---------------------------------------------------------------------------------------------
# Archive access

def list_assets() -> pd.DataFrame:
    """Path, asset id and size of every file of the pinned version."""
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/?page_size=200"
    rows = []
    while url:
        page = requests.get(url, timeout=60).json()
        rows += [(a["path"], a["asset_id"], a["size"]) for a in page["results"]]
        url = page.get("next")
    return pd.DataFrame(rows, columns=["path", "asset_id", "size"]).sort_values("path",
                                                                              ignore_index=True)


def version_metadata() -> dict:
    """The archive's metadata record of the pinned version."""
    return requests.get(f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/",
                        timeout=60).json()


def open_nwb(asset_id: str) -> h5py.File:
    """Open an asset for streaming (HTTP range requests through remfile)."""
    return h5py.File(remfile.File(f"{API}/assets/{asset_id}/download/"), "r")


def _s(x) -> str:
    return x.decode() if isinstance(x, bytes) else str(x)


# ---------------------------------------------------------------------------------------------
# One session, reduced as it loads

def _counts(st: np.ndarray, starts: np.ndarray, edges: np.ndarray) -> np.ndarray:
    """Spike counts of one unit in bins `starts[:, None] + edges` (st sorted)."""
    if len(starts) == 0:
        return np.zeros((0, len(edges) - 1), dtype=np.uint8)
    e = starts[:, None] + edges[None, :]
    c = np.searchsorted(st, e.ravel()).reshape(e.shape)
    return np.diff(c, axis=1).astype(np.uint8)


def _window_counts(st: np.ndarray, a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Spike counts of one unit in [a, b) for each pair (st sorted); NaN where a is NaN."""
    out = np.full(len(a), np.nan)
    ok = np.isfinite(a) & np.isfinite(b)
    out[ok] = np.searchsorted(st, b[ok]) - np.searchsorted(st, a[ok])
    return out


def _series_mean(t: np.ndarray, y: np.ndarray, a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Mean of a sampled series over [a, b) for each pair (t sorted); NaN when no sample."""
    i0 = np.searchsorted(t, a)
    i1 = np.searchsorted(t, b)
    cs = np.r_[0.0, np.cumsum(np.nan_to_num(y))]
    cn = np.r_[0.0, np.cumsum(np.isfinite(y))]
    n = cn[i1] - cn[i0]
    with np.errstate(invalid="ignore", divide="ignore"):
        return np.where(n > 0, (cs[i1] - cs[i0]) / n, np.nan)


def load_session(asset_id: str) -> dict:
    """Read one session and reduce it to what the claims use.

    Returns a dict with:
    - `session`, `subject`, `date`, `sex`, `genotype`, `age`, `n_probes`;
    - `trials`: the trials table, times in seconds (session clock), with `n` its row number;
    - `moves`: detected wheel movements (`onset`, `offset`, `type`) with `dpos`, the position
      change from onset to offset (encoder ticks, positive for left turns), and `vel`, the
      velocity pos(t) - pos(t - 10 ms) at t = onset + `VEL_OFFSETS` (ticks per 10 ms);
    - `units`: every unit (its `id` in the file, phy label, probe, region, depth, spike count,
      mean amplitude);
    - `good`: indices into `units` of the curated single units (phy label 2 or 3) kept below;
    - `C`: uint8 spike counts (good units x trials x `NBINS`), 5 ms bins aligned to stimulus
      onset; `Cp`: the same aligned to passive visual stimulus onsets;
    - `passive`: passive visual events (time, left and right contrast) and `passive_other`
      (beeps, valve clicks, noise bursts) with `Co`, pre-event counts of the good units in
      -0.25 to -0.05 s and -0.2 to 0 s (units x events x 2);
    - `rew`: counts of the good units 0 to 0.15 s after feedback (units x trials);
    - pupil area and face motion energy means in the pre-stimulus windows of each trial and
      passive event (`pupil`, `face`: columns w1 = -0.25 to -0.05 s, w2 = -0.2 to 0 s).
    """
    f = open_nwb(asset_id)
    out = {}
    sub = f["general/subject"]
    out["subject"] = _s(sub["subject_id"][()])
    out["sex"] = _s(sub["sex"][()])
    out["genotype"] = _s(sub["genotype"][()])
    out["age"] = _s(sub["age"][()])
    out["session"] = _s(f["identifier"][()])
    out["date"] = out["session"].split("_")[-1]

    tr = f["intervals/trials"]
    cols = ["start_time", "stop_time", "included", "go_cue", "visual_stimulus_time",
            "visual_stimulus_left_contrast", "visual_stimulus_right_contrast", "response_time",
            "response_choice", "feedback_time", "feedback_type", "rep_num"]
    trials = pd.DataFrame({c: tr[c][:] for c in cols}).rename(columns={
        "visual_stimulus_time": "stim", "visual_stimulus_left_contrast": "cL",
        "visual_stimulus_right_contrast": "cR", "response_choice": "choice",
        "feedback_time": "fb", "feedback_type": "fbtype", "response_time": "resp"})
    trials["n"] = np.arange(len(trials))
    out["trials"] = trials

    # wheel
    wp = f["acquisition/wheel_position"]
    w = wp["data"][:]
    w_t0 = float(wp["starting_time"][()])
    w_dt = float(wp["starting_time"].attrs["rate"])     # holds the interval (see docstring)
    out["wheel_dt"] = w_dt
    mv = f["processing/behavior/BehavioralEpochs/wheel_moves"]
    ts = mv["timestamps"][:]
    moves = pd.DataFrame({"onset": ts[0::2], "offset": ts[1::2], "type": mv["data"][:]})

    def pos(t):
        i = np.clip(np.round((np.asarray(t) - w_t0) / w_dt).astype(int), 0, len(w) - 1)
        return w[i]

    moves["dpos"] = pos(moves["offset"].values) - pos(moves["onset"].values)
    vel = np.stack([pos(moves["onset"].values + o) - pos(moves["onset"].values + o - 0.01)
                    for o in VEL_OFFSETS], axis=1)
    out["moves"] = moves
    out["move_vel"] = vel
    out["wheel_range"] = (w_t0, w_t0 + w_dt * (len(w) - 1))
    del w

    # passive events
    sp = f["stimulus/presentation"]
    passive = pd.DataFrame({"t": sp["passive_left_contrast/timestamps"][:],
                            "cL": sp["passive_left_contrast/data"][:],
                            "cR": sp["passive_right_contrast/data"][:]})
    out["passive_right_same_times"] = bool(np.array_equal(
        sp["passive_left_contrast/timestamps"][:], sp["passive_right_contrast/timestamps"][:]))
    other = []
    for k in ("passive_beeps", "passive_click_times", "passive_white_noise"):
        other.append(pd.DataFrame({"t": sp[k + "/timestamps"][:], "kind": k}))
    other = pd.concat(other, ignore_index=True).sort_values("t", ignore_index=True)
    out["passive"] = passive
    out["passive_other"] = other

    # pupil and face motion energy, pre-stimulus means
    eye = f["processing/behavior/PupilTracking/eye_area"]
    et, ea = eye["timestamps"][:], eye["data"][:]
    fm = f["processing/behavior/BehavioralTimeSeries/face_motion_energy"]
    fd = fm["data"][:]
    ft = float(fm["starting_time"][()]) + float(fm["starting_time"].attrs["rate"]) * np.arange(
        len(fd))

    def pre(t_ev):
        return np.stack([_series_mean(et, ea, t_ev - 0.25, t_ev - 0.05),
                         _series_mean(et, ea, t_ev - 0.2, t_ev),
                         _series_mean(ft, fd, t_ev - 0.25, t_ev - 0.05),
                         _series_mean(ft, fd, t_ev - 0.2, t_ev)], axis=1)

    pt = pre(trials["stim"].values)
    out["pupil"] = pt[:, :2]
    out["face"] = pt[:, 2:]
    pp = pre(passive["t"].values)
    out["pupil_passive"] = pp[:, :2]
    out["face_passive"] = pp[:, 2:]
    out["pupil_n"] = len(ea)
    out["pupil_nan_fraction"] = float(np.mean(~np.isfinite(ea)))

    # units
    u = f["units"]
    phy = u["phy_annotations"][:].ravel()
    pk = u["peak_channel"][:].ravel().astype(int)
    loc = f["general/extracellular_ephys/electrodes/location"][:].astype(str)
    gname = f["general/extracellular_ephys/electrodes/group_name"][:].astype(str)
    eg = u["electrode_group"][:]
    probe = np.array([f[r].name.split("/")[-1] for r in eg])
    first_el = u["electrodes"][:][np.r_[0, u["electrodes_index"][:-1]]]
    sti = u["spike_times_index"][:]
    starts = np.r_[0, sti[:-1]]
    st_all = u["spike_times"][:]
    amps = u["spike_amps"][:].ravel()
    wf = u["waveform_mean"]
    units = pd.DataFrame({
        "id": u["id"][:], "phy": phy, "probe": probe, "peak_channel": pk,
        "region": loc[pk - 1], "probe_of_peak": gname[pk - 1],
        "probe_of_electrodes": gname[first_el],
        "depth": u["cluster_depths"][:].ravel(),
        "n_spikes": sti - starts,
        "mean_amp": [amps[a:b].mean() if b > a else np.nan for a, b in zip(starts, sti)],
    })
    del amps
    # peak-to-trough amplitude of the mean waveform on its largest channel
    wfa = []
    for i0 in range(0, len(units), 200):
        x = wf[i0:i0 + 200]
        wfa.append((x.max(axis=1) - x.min(axis=1)).max(axis=1))
    units["wf_amp"] = np.concatenate(wfa)
    units["n_probes"] = len(set(gname))
    out["n_probes"] = len(set(gname))
    out["units"] = units
    good = np.flatnonzero(phy >= 2)
    out["good"] = good

    stim = trials["stim"].values
    fb = trials["fb"].values
    C = np.zeros((len(good), len(trials), NBINS), dtype=np.uint8)
    Cp = np.zeros((len(good), len(passive), NBINS), dtype=np.uint8)
    Co = np.zeros((len(good), len(other), 2))
    rew = np.zeros((len(good), len(trials)))
    oth = other["t"].values
    for j, i in enumerate(good):
        st = st_all[starts[i]:sti[i]]
        if np.any(np.diff(st) < 0):
            st = np.sort(st)
        C[j] = _counts(st, stim, BIN_EDGES)
        Cp[j] = _counts(st, passive["t"].values, BIN_EDGES)
        Co[j, :, 0] = _window_counts(st, oth - 0.25, oth - 0.05)
        Co[j, :, 1] = _window_counts(st, oth - 0.2, oth)
        rew[j] = _window_counts(st, fb, fb + 0.15)
    out["spikes_sorted"] = bool(all(np.all(np.diff(st_all[a:b]) >= 0)
                                    for a, b in zip(starts, sti)))
    del st_all
    out["C"], out["Cp"], out["Co"], out["rew"] = C, Cp, Co, rew
    f.close()
    return out


VEL_OFFSETS = np.round(np.arange(-0.1, 0.1001, 0.01), 3)


def load_all(asset_ids, workers: int = 6, progress=None) -> list[dict]:
    """Load sessions in parallel threads (each streams its own file)."""
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(load_session, asset_ids))


# ---------------------------------------------------------------------------------------------
# Trials: disengagement and definition T

def disengaged(trials: pd.DataFrame) -> np.ndarray:
    """Disengaged trials (claims file, definition T; Methods, Training protocol): a Miss (stimulus
    present, NoGo response) preceded by two or more Misses, and the run of NoGo responses that
    ends the session."""
    stim = (trials["cL"].values > 0) | (trials["cR"].values > 0)
    miss = stim & (trials["choice"].values == 0)
    out = np.zeros(len(trials), bool)
    out[2:] = miss[2:] & miss[1:-1] & miss[:-2]
    nogo = trials["choice"].values == 0
    k = len(trials)
    while k > 0 and nogo[k - 1]:
        k -= 1
    out[k:] = True
    return out


def classify_trials(trials: pd.DataFrame, moves: pd.DataFrame, rule: str = "methods",
                    engaged: np.ndarray | None = None, rng=None) -> pd.DataFrame:
    """Movement class of each trial (definition T).

    rule "methods": the moves overlapping -0.05 to 0.4 s from stimulus onset are found; with none
    the trial is NoGo ("N"); when the first of them has its onset 0.125 to 0.4 s after stimulus
    onset and is a left or right turn (type 1 or 2, a turn reaching 90 d.v.a.) the trial is Left
    ("L") or Right ("R"); otherwise it is dropped.
    rule "code": findMoveTimes.m and kernelFitBasic.m; the first move with onset after stimulus
    onset - 0.1 s and before feedback; L or R when it is a left or right turn with onset strictly
    between 0.125 and 0.4 s; N when such a move exists outside -0.05 to 0.4 s; a trial with no
    move before feedback is dropped.
    Adds `cls` (L, R, N or ''), `mt` (movement onset - stimulus onset, s; for N trials a time drawn
    from the L and R trials' times when `rng` is given, definition T), `keep` (cls set and
    engaged). `engaged` defaults to not disengaged().
    """
    on, off, typ = moves["onset"].values, moves["offset"].values, moves["type"].values
    stim, fb = trials["stim"].values, trials["fb"].values
    cls = np.array([""] * len(trials), dtype=object)
    mt = np.full(len(trials), np.nan)
    first_type = np.full(len(trials), -1)
    for i, s in enumerate(stim):
        if rule == "methods":
            k = np.flatnonzero((on < s + 0.4) & (off > s - 0.05))
            if len(k) == 0:
                cls[i] = "N"
                continue
            k = k[np.argmin(on[k])]
            t = on[k] - s
            first_type[i] = typ[k]
            if 0.125 <= t <= 0.4 and typ[k] in (1, 2):
                cls[i] = "L" if typ[k] == 1 else "R"
                mt[i] = t
        else:
            k = np.flatnonzero(on > s - 0.1)
            if len(k) == 0 or on[k[0]] >= fb[i]:
                continue
            k = k[0]
            t = on[k] - s
            first_type[i] = typ[k]
            if 0.125 < t < 0.4 and typ[k] in (1, 2):
                cls[i] = "L" if typ[k] == 1 else "R"
                mt[i] = t
            elif t < -0.05 or t > 0.4:
                cls[i] = "N"
    out = trials.copy()
    out["cls"] = cls
    out["first_type"] = first_type
    if engaged is None:
        engaged = ~disengaged(trials)
    out["engaged"] = engaged
    out["keep"] = (cls != "") & engaged
    if rng is not None:
        pool = mt[out["keep"].values & np.isin(cls, ["L", "R"])]
        nn = out["keep"].values & (cls == "N")
        mt[nn] = rng.choice(pool, nn.sum())
    out["mt"] = mt
    return out


def session_has_trials(tt: pd.DataFrame, minimum: int = 12) -> bool:
    """At least `minimum` kept trials of each of L, R and N (claims file, definition T)."""
    k = tt[tt["keep"]]
    return all((k["cls"] == c).sum() >= minimum for c in "LRN")


# ---------------------------------------------------------------------------------------------
# Spike count windows from the 5 ms count tensors

def bin_index(t: float) -> int:
    """Index of the bin edge at time t (s) relative to the event (5 ms grid)."""
    return int(round((t - T0) / BIN))


def window_rate(C: np.ndarray, a: float, b: float) -> np.ndarray:
    """Rate (sp/s) in [a, b) relative to the event: C is units x events x bins."""
    i, j = bin_index(a), bin_index(b)
    return C[..., i:j].sum(axis=-1) / (BIN * (j - i))


def shifted_window_rate(C: np.ndarray, shift: np.ndarray, a: float, b: float) -> np.ndarray:
    """Rate in [shift + a, shift + b) for each event, shift (s) per event rounded to the 5 ms
    grid (a standard choice: movement onsets are continuous, the counts are binned)."""
    out = np.full(C.shape[:2], np.nan)
    for e, sh in enumerate(shift):
        if not np.isfinite(sh):
            continue
        i, j = bin_index(sh + a), bin_index(sh + b)
        if i < 0 or j > C.shape[-1]:
            continue
        out[:, e] = C[:, e, i:j].sum(axis=-1) / (BIN * (j - i))
    return out


# ---------------------------------------------------------------------------------------------
# Neurons: the six responsiveness tests and definition N

def _signrank(x):
    from scipy.stats import wilcoxon
    x = x[np.isfinite(x)]
    x = x[x != 0]
    if len(x) == 0:
        return np.nan
    return wilcoxon(x, zero_method="wilcox", correction=True,
                    method="exact" if len(x) <= 15 else "approx").pvalue


def _ranksum(x, y):
    from scipy.stats import mannwhitneyu
    x, y = x[np.isfinite(x)], y[np.isfinite(y)]
    if len(x) == 0 or len(y) == 0:
        return np.nan, np.nan
    if np.all(np.r_[x, y] == np.r_[x, y][0]):
        return 1.0, 0.0
    r = mannwhitneyu(x, y, alternative="two-sided", method="auto")
    from scipy.stats import rankdata
    ranks = rankdata(np.r_[x, y])
    return r.pvalue, ranks[:len(x)].sum() - len(x) * (len(x) + len(y) + 1) / 2


def six_tests(C: np.ndarray, tt: pd.DataFrame, rew: np.ndarray):
    """p-values and signed effects of the six tests of the Methods (Data analysis), per unit.

    C: counts (units x trials x bins) aligned to stimulus onset; tt: classify_trials output
    (trials T are `keep`); rew: counts 0 to 0.15 s after feedback (units x trials). Rates are
    spike counts in the window divided by its length. Tests: 1 signrank, trial rate (0 to 0.4
    s) against baseline (-0.2 to 0 s); 2 signrank, 0.05 to 0.15 s against baseline; 3 signrank,
    -0.1 to 0.05 s from movement onset against baseline, L and R trials; 4 ranksum, that rate on
    R against L trials; 5 signrank, -0.05 to 0.2 s from movement onset against baseline; 6
    ranksum, 0 to 0.15 s after feedback on correct NoGo trials (no stimulus, NoGo response,
    reward) against the baselines of all trials T. Effects follow the code's effectSizes
    (kernelFitBasic.m): for signrank tests the count of positive minus negative differences, for
    ranksum tests the rank sum of the first group minus its null value (test 4: R greater is
    positive; test 6: post-reward greater is positive).
    """
    k = tt["keep"].values
    cls = tt["cls"].values[k]
    mv = np.isin(cls, ["L", "R"])
    mt = tt["mt"].values[k]
    Ck = C[:, k]
    trial = window_rate(Ck, 0.0, 0.4)
    bsl = window_rate(Ck, -0.2, 0.0)
    stim = window_rate(Ck, 0.05, 0.15)
    pre = shifted_window_rate(Ck[:, mv], mt[mv], -0.1, 0.05)
    post = shifted_window_rate(Ck[:, mv], mt[mv], -0.05, 0.2)
    cn = k & (tt["choice"].values == 0) & (tt["fbtype"].values == 1) & \
        (tt["cL"].values == 0) & (tt["cR"].values == 0)
    rr = rew[:, cn] / 0.15
    isR = cls[mv] == "R"
    n = C.shape[0]
    p = np.full((n, 6), np.nan)
    eff = np.full((n, 6), np.nan)
    for u in range(n):
        for j, x in ((0, trial[u] - bsl[u]), (1, stim[u] - bsl[u]), (2, pre[u] - bsl[u, mv]),
                     (4, post[u] - bsl[u, mv])):
            p[u, j] = _signrank(x)
            eff[u, j] = np.sum(x > 0) - np.sum(x < 0)
        p[u, 3], eff[u, 3] = _ranksum(pre[u, isR], pre[u, ~isR])
        p[u, 5], eff[u, 5] = _ranksum(rr[u], bsl[u])
    return p, eff


def neuron_table(sessions: list[dict], tts: list[pd.DataFrame]) -> pd.DataFrame:
    """One row per curated single unit (phy label 2 or 3) of every session.

    Columns: session index `s`, `session`, `subject`, `region`, unit index in the session's
    good units `j`, `rate` (mean over trials T of the spike count 0 to 0.4 s after stimulus
    onset / 0.4 s), `bsl` (mean rate -0.2 to 0 s over trials T), `mean_amp`, `wf_amp`.
    """
    rows = []
    for si, (s, tt) in enumerate(zip(sessions, tts)):
        k = tt["keep"].values
        u = s["units"].iloc[s["good"]]
        rows.append(pd.DataFrame({
            "s": si, "session": s["session"], "subject": s["subject"],
            "region": u["region"].values, "j": np.arange(len(u)),
            "rate": window_rate(s["C"][:, k], 0.0, 0.4).mean(axis=1),
            "bsl": window_rate(s["C"][:, k], -0.2, 0.0).mean(axis=1),
            "mean_amp": u["mean_amp"].values, "wf_amp": u["wf_amp"].values}))
    return pd.concat(rows, ignore_index=True)


def select_n(nt: pd.DataFrame, min_rate=0.1, min_per_region=13, min_subjects=2) -> np.ndarray:
    """Definition N without the responsiveness tests: rate at least 0.1 Hz, at least 13 such
    neurons of the region in the session, regions with such sessions in at least two subjects.
    Returns a boolean mask over `nt`."""
    ok = nt["rate"].values >= min_rate
    g = nt[ok].groupby(["s", "region"]).size()
    big = set(g[g >= min_per_region].index)
    ok2 = ok & np.array([(s, r) in big for s, r in zip(nt["s"], nt["region"])])
    subj = nt[ok2].groupby("region")["subject"].nunique()
    regs = set(subj[subj >= min_subjects].index)
    return ok2 & nt["region"].isin(regs).values


# ---------------------------------------------------------------------------------------------
# Region labels: the files label some channels with Allen subregions (SCig, SCsg, LSr ...). The
# Allen ontology of the paper's atlas tool maps each to its parent among the 42 regions.

ALLEN_TREE_URL = ("https://raw.githubusercontent.com/cortex-lab/allenCCF/"
                  "e5a57fe7e1c9fb333fec51c29a8471131c233a76/structure_tree_safe_2017.csv")


_TREE = {}


def allen_tree(url: str = ALLEN_TREE_URL) -> pd.DataFrame:
    """The Allen structure ontology (CCF 2017) of the paper's atlas tool, read once."""
    import io
    if url not in _TREE:
        _TREE[url] = pd.read_csv(io.StringIO(requests.get(url, timeout=60).text))
    return _TREE[url]


def allen_acronyms() -> set:
    return set(allen_tree()["acronym"])


def allen_parent_map(labels, url: str = ALLEN_TREE_URL) -> dict:
    """For each label, the region of the 42 that contains it in the Allen ontology (itself if it
    is one of the 42), or None. Labels missing from the ontology map to None."""
    tree = allen_tree(url)
    id2acr = dict(zip(tree["id"], tree["acronym"]))
    paths = dict(zip(tree["acronym"], tree["structure_id_path"]))
    out = {}
    for lab in labels:
        if lab not in paths:
            out[lab] = None
            continue
        anc = [id2acr[int(x)] for x in paths[lab].strip("/").split("/")]
        hit = [a for a in anc if a in REGIONS_42]
        out[lab] = hit[-1] if hit else None
    return out


# ---------------------------------------------------------------------------------------------
# Kernel regression (definition K): reduced-rank regression and elastic net, as
# reducedRankRegression/ of the paper's code (regFullPipeline.m, kernelFitBasic.m,
# CanonCor2all.m, determineResidualsWithout.m, predictResidualsWith.m).

SMOOTH_SD = 0.025          # causal half-Gaussian, s (Methods; kernelFitBasic.m)
VIS_WIN = (-0.05, 0.4)     # Vision kernels, 90 lags
MOVE_WIN = (-0.25, 0.025)  # Action and Choice kernels, 55 lags
N_VIS = 90
N_MOVE = 55
# predictor column groups: 0-2 left (ipsilateral) low, medium, high; 3-5 right (contralateral);
# 6 Action; 7 Choice
KERNEL_COLS = {k: np.arange(k * N_VIS, (k + 1) * N_VIS) for k in range(6)}
KERNEL_COLS[6] = 6 * N_VIS + np.arange(N_MOVE)
KERNEL_COLS[7] = 6 * N_VIS + N_MOVE + np.arange(N_MOVE)
N_PRED = 6 * N_VIS + 2 * N_MOVE
KERNEL_SETS = {"vis_ipsi": [0, 1, 2], "vis_contra": [3, 4, 5], "action": [6], "choice": [7]}


def half_gaussian(sd: float = SMOOTH_SD, dt: float = BIN, n_sd: float = 5.0) -> np.ndarray:
    """Causal half-Gaussian filter weights (index 0 = current bin), normalised to sum 1. The
    truncation at 5 s.d. is a standard choice (the tail holds < 1e-5 of the weight)."""
    n = int(np.ceil(n_sd * sd / dt))
    w = np.exp(-0.5 * (np.arange(n + 1) * dt / sd) ** 2)
    return w / w.sum()


def causal_smooth(x: np.ndarray, w: np.ndarray) -> np.ndarray:
    """Filter along the last axis with causal weights w (no look-ahead)."""
    out = np.zeros(x.shape, dtype=np.float32)
    n = x.shape[-1]
    for k, wk in enumerate(w):
        if k == 0:
            out += wk * x
        else:
            out[..., k:] += wk * x[..., :n - k]
    return out


def kernel_design(tt: pd.DataFrame, choice_values: np.ndarray | None = None,
                  extended: bool = False):
    """Toeplitz design of one session for trials T (`keep`).

    Samples: for each kept trial, the 5 ms bins whose centres lie from 0.05 s before stimulus
    onset to the earlier of 0.4 s after it and 0.025 s after movement onset (kernelFitBasic.m);
    with `extended`, every bin of the count window (for residuals at any time).
    Returns (X, trial, rel_t, mt): X sparse CSR (samples x 650), the kept-trial number of each
    sample, its time from stimulus onset (bin centre) and the trial's movement time (NaN for
    NoGo). `choice_values` replaces the Choice event values (+1 Left, -1 Right) of the kept L/R
    trials, in their order (for the shuffle test).
    """
    from scipy import sparse
    k = np.flatnonzero(tt["keep"].values)
    cls = tt["cls"].values[k]
    mt = np.where(np.isin(cls, ["L", "R"]), tt["mt"].values[k], np.nan)
    cL, cR = tt["cL"].values[k], tt["cR"].values[k]
    cv = np.where(cls == "L", 1.0, np.where(cls == "R", -1.0, 0.0))
    if choice_values is not None:
        cv = cv.copy()
        cv[np.isin(cls, ["L", "R"])] = choice_values
    rows, cols, vals = [], [], []
    tr_of, t_of = [], []
    n = 0
    for i in range(len(k)):
        t = BIN_CENTRES
        if extended:
            sel = np.ones(len(t), bool)
        else:
            end = min(VIS_WIN[1], mt[i] + MOVE_WIN[1]) if np.isfinite(mt[i]) else VIS_WIN[1]
            sel = (t >= VIS_WIN[0]) & (t <= end)
        ts = t[sel]
        idx = n + np.arange(len(ts))
        lag = np.floor((ts - VIS_WIN[0]) / BIN + 1e-9).astype(int)
        okv = (lag >= 0) & (lag < N_VIS)
        for side, c in ((0, cL[i]), (3, cR[i])):
            if c > 0:
                col = (side + CONTRASTS.index(c) - 1) * N_VIS + lag[okv]
                rows.append(idx[okv]); cols.append(col); vals.append(np.ones(okv.sum()))
        if np.isfinite(mt[i]):
            lm = np.floor((ts - mt[i] - MOVE_WIN[0]) / BIN + 1e-9).astype(int)
            okm = (lm >= 0) & (lm < N_MOVE)
            rows.append(idx[okm]); cols.append(KERNEL_COLS[6][lm[okm]])
            vals.append(np.ones(okm.sum()))
            rows.append(idx[okm]); cols.append(KERNEL_COLS[7][lm[okm]])
            vals.append(np.full(okm.sum(), cv[i]))
        tr_of.append(np.full(len(ts), i)); t_of.append(ts)
        n += len(ts)
    r = np.concatenate(rows) if rows else np.zeros(0, int)
    X = sparse.csr_matrix((np.concatenate(vals), (r, np.concatenate(cols))), shape=(n, N_PRED))
    return X, np.concatenate(tr_of), np.concatenate(t_of), mt


def sample_rates(R: np.ndarray, trial: np.ndarray, rel_t: np.ndarray) -> np.ndarray:
    """Rates (units x kept trials x bins) at the design's samples -> samples x units."""
    b = np.round((rel_t - BIN_CENTRES[0]) / BIN).astype(int)
    return R[:, trial, b].T


def canoncor2all(Ys, Xs, eps: float = 1e-7):
    """CanonCor2all.m: reduced-rank regression basis over several instances (sessions) with the
    same predictors. Ys: list of (samples x units) arrays; Xs: list of sparse (samples x p)
    matrices. Returns b (p x p), columns ordered by the variance of Y they predict."""
    p = Xs[0].shape[1]
    n_all = sum(x.shape[0] for x in Xs)
    sx = sum(np.asarray(x.sum(axis=0)).ravel() for x in Xs)
    sxx = sum((x.T @ x).toarray() for x in Xs)
    mu = sx / n_all
    cxx = (sxx - n_all * np.outer(mu, mu)) / (n_all - 1) + eps * np.eye(p)
    ev, evec = np.linalg.eigh(cxx)
    cxxmh = (evec * ev ** -0.5) @ evec.T
    cyx = []
    for y, x in zip(Ys, Xs):
        n = x.shape[0]
        xm = np.asarray(x.mean(axis=0)).ravel()
        ym = y.mean(axis=0)
        cyx.append((np.asarray((x.T @ y)).T - n * np.outer(ym, xm)) / (n - 1))
    M = np.vstack(cyx) @ cxxmh
    _, _, vt = np.linalg.svd(M, full_matrices=False)
    return cxxmh @ vt.T


def enet(Z: np.ndarray, Y: np.ndarray, lam: float = 0.5, alpha: float = 0.5, tol: float = 1e-7,
         max_sweeps: int = 1000):
    """Elastic net for many responses at once, as glmnet's Gaussian fit with its default options
    (the paper's code calls glmnet with alpha 0.5 and takes lambda 0.5): predictors standardised
    (1/n s.d.), an unpenalised intercept, each response scaled by its 1/n s.d. ys and the penalty
    lam / ys applied on that scale; coefficients returned on the original scale. Coordinate
    descent on the Gram matrix to a tolerance tighter than glmnet's default (a standard choice).
    Z: samples x p; Y: samples x m. Returns (W p x m, intercept m)."""
    n, p = Z.shape
    zm = Z.mean(axis=0)
    zs = Z.std(axis=0)
    zs[zs == 0] = 1.0
    ym = Y.mean(axis=0)
    ys = Y.std(axis=0)
    good = ys > 0
    Zs = (Z - zm) / zs
    G = (Zs.T @ Zs) / n
    c = (Zs.T @ (Y[:, good] - ym[good])) / n / ys[good]
    lp = lam / ys[good]
    l1 = alpha * lp
    den = 1.0 + (1 - alpha) * lp
    B = np.zeros((p, good.sum()))
    r = c.copy()                       # c - G B
    gd = np.diag(G).copy()
    for _ in range(max_sweeps):
        dmax = 0.0
        for j in range(p):
            bj = B[j]
            zj = r[j] + gd[j] * bj
            new = np.sign(zj) * np.maximum(np.abs(zj) - l1, 0) / (gd[j] - 1 + den)
            d = new - bj
            if np.any(d):
                B[j] = new
                r -= np.outer(G[:, j], d)
                dmax = max(dmax, float(np.max(d * d)))
        if dmax < tol:
            break
    W = np.zeros((p, Y.shape[1]))
    W[:, good] = B * ys[good] / zs[:, None]
    b0 = ym - zm @ W
    return W, b0


def _fold_ids(n_trials: int, k: int, rng) -> np.ndarray:
    """Random partition of trials into k folds (cvpartition 'KFold'); the seed is a standard
    choice."""
    ids = np.arange(n_trials) % k
    rng.shuffle(ids)
    return ids


def _cv_ve(Z_parts, Y, folds_of_sample, eval_mask, n_comp, fit_cols=None, lam=0.5):
    """Cross-validated variance explained of predictions truncated to the first 1..n_comp
    columns (regFullPipeline.m / predictResidualsWith.m): for each fold, one elastic net on all
    columns of Z for the training samples; test predictions use the first nc columns and their
    coefficients, without intercept; VE = 1 - var(y - pred) / var(y) over the test samples in
    `eval_mask`, all folds together. Z_parts: samples x p array. Returns VE (n_comp x units)."""
    Z = Z_parts
    m = Y.shape[1]
    S1 = np.zeros((n_comp, m)); S2 = np.zeros((n_comp, m)); SYP = np.zeros((n_comp, m))
    n = 0; sy = np.zeros(m); syy = np.zeros(m)
    for f in np.unique(folds_of_sample):
        tr = folds_of_sample != f
        te = (folds_of_sample == f) & eval_mask
        if te.sum() == 0:
            continue
        W, _ = enet(Z[tr], Y[tr], lam=lam)
        Zt = Z[te][:, :n_comp]
        Wt = W[:n_comp]
        yt = Y[te]
        n += te.sum(); sy += yt.sum(0); syy += (yt ** 2).sum(0)
        S1 += np.cumsum(Zt.sum(0)[:, None] * Wt, axis=0)
        SYP += np.cumsum((Zt.T @ yt) * Wt, axis=0)
        Q = Zt.T @ Zt
        Mq = Wt[:, None, :] * Q[:, :, None] * Wt[None, :, :]
        cs = np.cumsum(np.cumsum(Mq, axis=0), axis=1)
        S2 += cs[np.arange(n_comp), np.arange(n_comp)]
    # residual e = y - p: sum e = sy - S1; sum e^2 = syy - 2 SYP + S2
    se = sy[None] - S1
    see = syy[None] - 2 * SYP + S2
    var_e = (see - se ** 2 / n) / (n - 1)
    var_y = (syy - sy ** 2 / n) / (n - 1)
    with np.errstate(invalid="ignore", divide="ignore"):
        return 1 - var_e / var_y[None]


def kernel_inputs(s: dict, tt: pd.DataFrame, units: np.ndarray, choice_values=None):
    """Design, sample rates and smoothed rates of one session for the kernel analysis.
    units: indices into the session's good units. Rates: 5 ms counts / 0.005 s, causal
    half-Gaussian s.d. 25 ms, minus each neuron's mean rate -0.2 to 0 s over trials T
    (kernelFitBasic.m)."""
    keep = tt["keep"].values
    R = causal_smooth(s["C"][units][:, keep].astype(np.float32) / BIN, half_gaussian())
    bm = (BIN_CENTRES >= -0.2) & (BIN_CENTRES <= 0)
    bsl = R[:, :, bm].mean(axis=(1, 2))
    R -= bsl[:, None, None]
    X, trial, rel_t, mt = kernel_design(tt, choice_values)
    Y = sample_rates(R, trial, rel_t)
    return dict(R=R, bsl=bsl, X=X, trial=trial, rel_t=rel_t, mt=mt, Y=Y)


def full_model(inputs: list[dict], seed: int = 0, n_basis: int = 200, n_comp: int = 50):
    """Reduced-rank basis over all sessions, then per neuron 5-fold cross-validated VE for 1 to
    50 components (best kept), evaluated from stimulus onset to the earlier of movement onset and
    0.4 s; a final fit on all samples gives the kernels. Returns dict with b, and per session
    VE (n_comp x units), best VE, best number of components and the final coefficients."""
    b = canoncor2all([d["Y"] for d in inputs], [d["X"] for d in inputs])[:, :n_basis]
    out = {"b": b, "ve": [], "best": [], "ndim": [], "W": []}
    for si, d in enumerate(inputs):
        rng = np.random.default_rng([seed, si])
        nt_ = len(d["mt"])
        fold = _fold_ids(nt_, 5, rng)[d["trial"]]
        end = np.where(np.isfinite(d["mt"]), np.minimum(d["mt"], VIS_WIN[1]), VIS_WIN[1])
        ev = (d["rel_t"] >= 0) & (d["rel_t"] <= end[d["trial"]])
        Z = np.asarray(d["X"] @ b)
        ve = _cv_ve(Z, d["Y"], fold, ev, n_comp)
        ve = np.nan_to_num(ve, nan=0.0)
        out["ve"].append(ve)
        out["best"].append(ve.max(axis=0))
        out["ndim"].append(ve.argmax(axis=0) + 1)
        W, _ = enet(Z, d["Y"])
        out["W"].append(W)
    return out


def nested_test(inputs: list[dict], keep_units: list[np.ndarray], kernel: str, seed: int = 0,
                n_without: int = 75, n_comp: int = 18):
    """Nested test of one kernel set (determineResidualsWithout.m, predictResidualsWith.m):
    a basis without the kernel over the kept neurons of all sessions; each neuron fit with its
    first 75 columns on all samples and the prediction (without intercept) subtracted; a basis
    for the kernel alone on these residuals; 10-fold cross-validated VE for 1 to 18 components,
    over samples 0.05 to 0.4 s after stimulus onset (ending at movement onset) and -0.2 to 0 s
    from movement onset (not before stimulus onset). Returns per session the best VE of each
    kept neuron, and the residual model coefficients (for residuals at other times)."""
    cols = np.concatenate([KERNEL_COLS[k] for k in KERNEL_SETS[kernel]])
    other = np.setdiff1d(np.arange(N_PRED), cols)
    Ys = [d["Y"][:, k] for d, k in zip(inputs, keep_units)]
    Xo = [d["X"][:, other] for d in inputs]
    b_no = canoncor2all(Ys, Xo)[:, :n_without]
    resid, Wno = [], []
    for y, x in zip(Ys, Xo):
        Z = np.asarray(x @ b_no)
        W, _ = enet(Z, y)
        resid.append(y - Z @ W)
        Wno.append(b_no @ W)          # kernels without the tested set (len(other) x units)
    Xk = [d["X"][:, cols] for d in inputs]
    b_k = canoncor2all(resid, Xk)
    best = []
    for si, (d, r, x) in enumerate(zip(inputs, resid, Xk)):
        rng = np.random.default_rng([seed, si, 1])
        fold = _fold_ids(len(d["mt"]), 10, rng)[d["trial"]]
        mt = d["mt"][d["trial"]]
        t = d["rel_t"]
        stim_end = np.where(np.isfinite(mt), np.minimum(mt, 0.4), 0.4)
        ev = (t >= 0.05) & (t <= stim_end)
        ev |= np.isfinite(mt) & (t >= np.maximum(0, mt - 0.2)) & (t <= mt)
        Z = np.asarray(x @ b_k)
        if r.shape[1] == 0:
            best.append(np.zeros(0)); continue
        ve = np.nan_to_num(_cv_ve(Z, r, fold, ev, n_comp), nan=0.0)
        best.append(ve.max(axis=0))
    return {"best": best, "W_without": Wno, "other_cols": other, "b_k": b_k}


# ---------------------------------------------------------------------------------------------
# Matched contrast (definition M) and responsiveness in a condition (definition R)

def matched_contrast(tt: pd.DataFrame, passive: pd.DataFrame, go: np.ndarray, nogo: np.ndarray,
                     pas: np.ndarray, rng):
    """Definition M: at each contralateral (right) contrast above zero, the smallest of the counts
    of the go, nogo and passive sets is drawn at random from each (without replacement).
    go, nogo: boolean masks over trials (rows of tt); pas: over passive events.
    Returns (go_idx, nogo_idx, pas_idx, per-level counts)."""
    gi, ni, pi, per = [], [], [], {}
    for c in CONTRASTS[1:]:
        g = np.flatnonzero(go & (tt["cR"].values == c))
        n = np.flatnonzero(nogo & (tt["cR"].values == c))
        p = np.flatnonzero(pas & (passive["cR"].values == c))
        k = min(len(g), len(n), len(p))
        per[c] = k
        if k:
            gi.append(rng.choice(g, k, replace=False)); ni.append(rng.choice(n, k, replace=False))
            pi.append(rng.choice(p, k, replace=False))
    cat = lambda x: np.sort(np.concatenate(x)) if x else np.zeros(0, int)
    return cat(gi), cat(ni), cat(pi), per


def condition_z(C: np.ndarray, idx: np.ndarray, denominator: str = "se",
                zero_sd: str = "inf") -> np.ndarray:
    """Definition R: the mean rate 0 to 0.25 s after stimulus onset over the condition's trials,
    z-scored against the trial-by-trial baseline (-0.1 to 0 s). denominator "se" (reading Z1):
    s.d. of the baseline rates over trials / sqrt(number of trials); "sd" (reading Z2): their
    s.d. A neuron with no baseline variance (no spike in any baseline window) has a zero
    denominator, which the claims file does not settle: zero_sd "inf" (reading V1) gives +inf
    when its mean rate rises (as a division by zero in MATLAB), "zero" (reading V2) gives 0."""
    post = window_rate(C[:, idx], 0.0, 0.25)
    bsl = window_rate(C[:, idx], -0.1, 0.0)
    diff = post.mean(axis=1) - bsl.mean(axis=1)
    sd = bsl.std(axis=1, ddof=1)
    den = sd / np.sqrt(len(idx)) if denominator == "se" else sd
    with np.errstate(divide="ignore", invalid="ignore"):
        z = np.where(den > 0, diff / den, np.where((diff > 0) & (zero_sd == "inf"), np.inf, 0.0))
    return z


def normalized_trace(C: np.ndarray, idx: np.ndarray, all_idx: np.ndarray) -> np.ndarray:
    """Normalised firing rate (Methods, Data analysis): 5 ms bins, causal half-Gaussian s.d.
    0.02 s, mean over the condition's trials, causal half-Gaussian s.d. 0.03 s, minus the
    baseline (-0.02 to 0 s, the same trace over all task trials `all_idx`), divided by baseline
    + 0.5 sp/s. Returns units x bins."""
    w1, w2 = half_gaussian(0.02), half_gaussian(0.03)
    def trace(ix):
        r = causal_smooth(C[:, ix].astype(np.float32) / BIN, w1).mean(axis=1)
        return causal_smooth(r, w2)
    tr = trace(idx)
    allr = trace(all_idx)
    bm = (BIN_CENTRES >= -0.02) & (BIN_CENTRES <= 0)
    b = allr[:, bm].mean(axis=1)
    return (tr - b[:, None]) / (b[:, None] + 0.5)


def ranksum_windows(C: np.ndarray, a_idx: np.ndarray, b_idx: np.ndarray, starts: np.ndarray,
                    width: float = 0.1) -> np.ndarray:
    """Two-sided rank-sum p-values (normal approximation with tie correction) between the spike
    counts of two trial sets in sliding windows [t, t + width) relative to stimulus onset.
    Returns units x windows."""
    from scipy.stats import rankdata, norm
    out = np.ones((C.shape[0], len(starts)))
    n1, n2 = len(a_idx), len(b_idx)
    for w, t in enumerate(starts):
        i, j = bin_index(t), bin_index(t + width)
        x = np.concatenate([C[:, a_idx, i:j].sum(-1), C[:, b_idx, i:j].sum(-1)], axis=1).astype(float)
        r = rankdata(x, axis=1)
        R1 = r[:, :n1].sum(1)
        U = R1 - n1 * (n1 + 1) / 2
        tie = np.zeros(x.shape[0])
        for v in np.unique(x):
            t = (x == v).sum(axis=1).astype(float)
            tie += t ** 3 - t
        n = n1 + n2
        var = n1 * n2 / 12 * ((n + 1) - tie / (n * (n - 1)))
        with np.errstate(divide="ignore", invalid="ignore"):
            z = (U - n1 * n2 / 2) / np.sqrt(var)
        out[:, w] = np.where(var > 0, 2 * norm.sf(np.abs(z)), 1.0)
    return out


# ---------------------------------------------------------------------------------------------
# Combined-conditions choice probability (ccCP/choiceProbShuf.m, mannWhitneyUshuf.m)

def cccp(X: np.ndarray, label: np.ndarray, cond: np.ndarray, n_shuf: int = 0, rng=None):
    """ccCP of each unit: X units x trials (spike counts), label boolean (class A), cond the
    stimulus condition of each trial. Within each condition holding both classes, the
    Mann-Whitney numerator (ties counted half, through tied ranks) of A against B is summed
    over conditions and divided by the summed nA * nB. With n_shuf > 0, labels are permuted
    within each condition (the same permutations for every unit) and p is the tied rank of the
    true value among [true, shuffles] / (1 + n_shuf), as choiceProbShuf.m. Returns (cp, p,
    n_trials_used)."""
    from scipy.stats import rankdata
    num = np.zeros((X.shape[0], 1 + n_shuf))
    den = 0.0
    used = 0
    for c in np.unique(cond):
        m = cond == c
        a, b = label & m, ~label & m
        na, nb = a.sum(), b.sum()
        if na == 0 or nb == 0:
            continue
        idx = np.flatnonzero(m)
        r = rankdata(X[:, idx], axis=1)
        lab = label[idx]
        Sm = np.zeros((len(idx), 1 + n_shuf))
        Sm[:, 0] = lab
        if n_shuf:
            order = np.argsort(rng.random((len(idx), n_shuf)), axis=0)[:na]   # na trials drawn per shuffle
            Sm[order, np.arange(1, 1 + n_shuf)[None, :]] = 1.0
        num += r @ Sm - na * (na + 1) / 2
        den += na * nb
        used += len(idx)
    if den == 0:
        return np.full(X.shape[0], np.nan), np.full(X.shape[0], np.nan), 0
    cp = num / den
    if n_shuf:
        rk = rankdata(cp, axis=1)
        p = rk[:, 0] / (1 + n_shuf)
    else:
        p = np.full(X.shape[0], np.nan)
    return cp[:, 0], p, used


# ---------------------------------------------------------------------------------------------
# jPECC (jPECC/jPECC.m)

def binned_10ms(C: np.ndarray, starts: np.ndarray, n_bins: int, baseline: tuple, sd: float = 0.025,
                history: int = 15) -> np.ndarray:
    """Spike counts in 10 ms bins from `starts` (s from stimulus onset, per trial), smoothed with
    a causal half-Gaussian (s.d. 25 ms), in sp/s, divided by each neuron's baseline + 1 sp/s
    (mean rate in `baseline`, s from stimulus onset, over the trials given). C: units x trials
    x 5 ms bins. Returns trials x n_bins x units."""
    w = half_gaussian(sd, 0.01)
    bsl = window_rate(C, *baseline).mean(axis=1)
    out = np.zeros((C.shape[1], n_bins, C.shape[0]), dtype=np.float32)
    for i, st in enumerate(starts):
        i0 = bin_index(st) - 2 * history
        x = C[:, i, i0:i0 + 2 * (n_bins + history)].astype(np.float32)
        x = x.reshape(C.shape[0], -1, 2).sum(axis=2) / 0.01
        x = causal_smooth(x, w)[:, history:]
        out[i] = (x / (bsl[:, None] + 1.0)).T
    return out


def _pca_scores(X: np.ndarray, nd: int) -> np.ndarray:
    Xc = X - X.mean(axis=0)
    U, s, _ = np.linalg.svd(Xc, full_matrices=False)
    return (U * s)[:, :nd]


def jpecc(A: np.ndarray, B: np.ndarray, kfold: int = 10, lam: float = 0.5, max_pc: int = 10,
          rng=None) -> np.ndarray:
    """jPECC.m: for each pair of time bins, PCA of each population (trials x neurons) to nd =
    min(10, nA, nB) dimensions; k-fold over trials, CCA on the training PCs with ridge rows
    (lam * I appended, as jPECC.m), test PCs projected on the first canonical pair, Pearson r of
    the projections over all test trials. A: trials x T x nA; B: trials x T x nB. Returns
    r[t1, t2] (A at t1, B at t2)."""
    N, T = A.shape[0], A.shape[1]
    nd = min(max_pc, A.shape[2], B.shape[2])
    Xs = np.stack([_pca_scores(A[:, t], nd) for t in range(T)])          # T x N x nd
    Ys = np.stack([_pca_scores(B[:, t], nd) for t in range(T)])
    fold = np.arange(N) % kfold
    (rng or np.random.default_rng(0)).shuffle(fold)
    out = np.zeros((T, T))
    Iz = np.vstack([lam * np.eye(nd), np.zeros((nd, nd))])
    Zi = np.vstack([np.zeros((nd, nd)), lam * np.eye(nd)])
    for t1 in range(T):
        U = np.zeros((T, N)); V = np.zeros((T, N))
        for f in range(kfold):
            tr, te = fold != f, fold == f
            Xa = np.vstack([Xs[t1][tr], Iz]); Xa = Xa - Xa.mean(axis=0)
            Ya = np.concatenate([Ys[:, tr], np.broadcast_to(Zi, (T, 2 * nd, nd))], axis=1)
            Ya = Ya - Ya.mean(axis=1, keepdims=True)
            Q1, R1 = np.linalg.qr(Xa)
            Q2, R2 = np.linalg.qr(Ya)
            Lm, _, Mh = np.linalg.svd(np.einsum("ij,tik->tjk", Q1, Q2))
            a1 = np.linalg.solve(np.broadcast_to(R1, (T, nd, nd)), Lm[:, :, :1])[:, :, 0]   # T x nd
            b1 = np.linalg.solve(R2, np.swapaxes(Mh, 1, 2)[:, :, :1])[:, :, 0]
            U[:, te] = a1 @ Xs[t1][te].T
            V[:, te] = np.einsum("tnd,td->tn", Ys[:, te], b1)
        Uc = U - U.mean(axis=1, keepdims=True); Vc = V - V.mean(axis=1, keepdims=True)
        out[t1] = (Uc * Vc).sum(1) / np.sqrt((Uc ** 2).sum(1) * (Vc ** 2).sum(1))
    return out


def asymmetry(J: np.ndarray, k: int = 5) -> np.ndarray:
    """Mean r along the diagonal slice from (t, t) to k bins of lead of the first population,
    J[t - j, t + j], minus the mean along k bins of lead of the second, J[t + j, t - j],
    j = 0..k. NaN where the slice leaves the matrix."""
    T = J.shape[0]
    out = np.full(T, np.nan)
    for t in range(k, T - k):
        j = np.arange(k + 1)
        out[t] = J[t - j, t + j].mean() - J[t + j, t - j].mean()
    return out


# ---------------------------------------------------------------------------------------------
# The selections both notebooks share

def prepare(sessions: list[dict]) -> dict:
    """Trials T (Methods rule, disengagement rule as written, NoGo movement times drawn with the
    seed [1, session]), the table of curated units with regions mapped to the 42 regions through
    the Allen ontology, the six tests, and the neuron masks: `inN` (definition N), `active` (any
    test below 0.05/6), `resp4` (any of tests 1 to 4 below 0.05) and `inN35` (the Figs. 3 to 5
    set)."""
    tts = [classify_trials(s["trials"], s["moves"], "methods", rng=np.random.default_rng([1, si]))
           for si, s in enumerate(sessions)]
    nt = neuron_table(sessions, tts)
    parent = allen_parent_map(sorted(set(nt["region"])))
    nt["label"] = nt["region"]
    nt["region"] = nt["label"].map(parent).fillna("none")
    P, E = [], []
    for si, s in enumerate(sessions):
        p, e = six_tests(s["C"], tts[si], s["rew"])
        P.append(p); E.append(e)
    P, E = np.vstack(P), np.vstack(E)
    active = np.any(P < 0.05 / 6, axis=1)
    resp4 = np.any(P[:, :4] < 0.05, axis=1)
    inN = select_n(nt) & nt["region"].isin(REGIONS_42).values
    return dict(tts=tts, nt=nt, parent=parent, P=P, E=E, active=active, resp4=resp4, inN=inN,
                inN35=inN & resp4)
