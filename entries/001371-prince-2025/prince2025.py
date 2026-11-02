"""Loading and measures for dandiset 001371 (Prince et al. 2025, Nat. Commun. 16, 4822).

Every parameter says where it comes from:
- [claims Sn]: the shared method of the claims file `claims/001371/10.1038-s41467-025-60122-8.yaml`
  (opening comment, items S1 to S11), which cites the paper's Methods and its code
  (github.com/stephprince/update-project at d8557f031f45cb04532484a8a4f730af954a881d);
- [paper: passage]: a detail taken from the paper by the author (protocol, author step 1.6);
- [code: file]: the paper's linked code at that commit, where the claims file names it;
- [assumption]: a choice the paper leaves open, said why;
- [standard]: a standard choice for a detail that cannot change a result.

Data are streamed from the DANDI archive at a pinned version; nothing is written to disk.
"""
from __future__ import annotations

import concurrent.futures as cf
import itertools

import h5py
import numpy as np
import pandas as pd
import remfile
import requests

DANDISET = "001371"
VERSION = "0.260831.0201"
API = "https://api.dandiarchive.org/api"

# --- task constants -------------------------------------------------------------------------
# [claims S2; code general/virtual_track.py] track graph and edge spacing for linearization
NODES = [(0, 0), (0, 255), (-30, 285), (30, 285)]
EDGES = [(0, 1), (1, 2), (1, 3)]
EDGE_SPACING = 20
N_BINS = 50                       # [claims S2; paper Methods "n = 50 bins"]
POS_MIN = 5                       # [claims S2; code get_limits] lower limit of the feature bins
SPEED_THRESHOLD = 1000            # [claims S3; code speed_threshold] on |rot| + |trans| acquisition values
TEST_SIZE = 0.2                   # [claims S3; paper Methods 80/20]
SPLIT_SEED = 21                   # [claims S3; code train_test_split random_state=21]
BIN = 0.2                         # [claims S4; paper Methods 200 ms]
WINDOW = 2.5                      # [claims S5; code _align_by_times window 2.5]
UPDATE_LOC_DEFAULT = 145.125      # [claims S5; code general/trials.py]
RETRO_ZONE = (5, 50)              # [claims, sfig3c criterion; code prospective_reps]
MIN_UNITS = 20                    # [claims S1; paper Methods]
MIN_TRIALS = 50                   # [claims S1; paper Methods]
FINAL_MAZE = 4                    # [claims comment; NWB maze_id description 'ymaze_delay': 4]
TRIAL_TYPES = {1: "delay only", 2: "switch", 3: "stay"}   # [NWB update_type description; claims]


# --- archive --------------------------------------------------------------------------------
def list_assets() -> pd.DataFrame:
    """All NWB assets of the pinned version, with subject and session from the path."""
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=200"
    rows = []
    while url:
        r = requests.get(url, timeout=60).json()
        rows += r["results"]
        url = r.get("next")
    df = pd.DataFrame([dict(asset_id=a["asset_id"], path=a["path"], size_gb=a["size"] / 1e9) for a in rows])
    df["subject"] = df.path.str.extract(r"sub-([^/]+)/")[0]
    df["session"] = df.path.str.extract(r"_ses-([^_]+)_")[0]
    return df.sort_values(["subject", "session"]).reset_index(drop=True)


def open_asset(asset_id: str) -> h5py.File:
    """Open an asset by streaming its S3 object (no download)."""
    url = requests.get(f"{API}/assets/{asset_id}/download/", allow_redirects=False, timeout=60).headers["Location"]
    return h5py.File(remfile.File(url), "r")


# --- loading --------------------------------------------------------------------------------
def _str(a):
    return np.array([x.decode() if isinstance(x, bytes) else str(x) for x in a])


def linearize(xy: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Linearized position and segment id with track-linearization, as the paper's code
    (get_linearized_position with its default projection, edge spacing 20) [claims S2].
    The Methods mention an HMM; the code's call uses the package default (no HMM), which is followed."""
    from track_linearization import make_track_graph, get_linearized_position
    g = make_track_graph(NODES, EDGES)
    out = get_linearized_position(position=xy, track_graph=g, edge_spacing=EDGE_SPACING)
    return out["linear_position"].to_numpy(), out["track_segment_id"].to_numpy()


def load_session(asset_id: str, lfp: bool = False) -> dict:
    """Read what the analyses use from one session: trials, units, behaviour and the locomotion
    flag; with lfp=True also the CA1 LFP of the ripple channel (theta claims)."""
    f = open_asset(asset_id)
    s = {}
    tr = f["intervals/trials"]
    s["trials"] = pd.DataFrame({k: tr[k][:] for k in tr.keys() if k not in ("id",)})
    u = f["units"]
    st, idx = u["spike_times"][:], u["spike_times_index"][:]
    s["spikes"] = np.split(st, idx[:-1])
    # five sessions hold units without region or cell type (phy columns only); their units are
    # labelled "unknown" and enter no decoding
    n_u = len(idx)
    s["region"] = _str(u["region"][:]) if "region" in u else np.full(n_u, "unknown")
    s["cell_type"] = _str(u["cell_type"][:]) if "cell_type" in u else np.full(n_u, "unknown")
    s["quality"] = _str(u["quality"][:])
    b = f["processing/behavior"]
    s["t"] = b["position/position/timestamps"][:]
    s["xy"] = b["position/position/data"][:]
    s["view_angle"] = b["view_angle/view_angle/data"][:]
    s["rot"] = b["rotational_velocity/data"][:]
    s["trans"] = b["translational_velocity/data"][:]
    # locomotion: |rot| + |trans| of the acquisition series (2 kHz) above 1000 [claims S3; code acquisition.get_velocity]
    a_rot = f["acquisition/rotational_velocity"]
    rate = float(a_rot["starting_time"].attrs["rate"])
    t0 = float(a_rot["starting_time"][()])
    comb = np.abs(a_rot["data"][:].astype(float)) + np.abs(f["acquisition/translational_velocity/data"][:].astype(float))
    i = np.clip(np.round((s["t"] - t0) * rate).astype(int), 0, len(comb) - 1)
    s["moving"] = comb[i] > SPEED_THRESHOLD
    s["acq_speed_hist"] = np.histogram(np.log10(comb + 1), bins=np.linspace(0, 5, 51))[0]
    s["lin"], s["seg"] = linearize(s["xy"])
    s["units_attrs"] = dict(pos_unit=b["position/position/data"].attrs.get("unit"),
                            va_unit=b["view_angle/view_angle/data"].attrs.get("unit"),
                            turn_type_desc=tr["turn_type"].attrs.get("description"),
                            update_type_desc=tr["update_type"].attrs.get("description"))
    if lfp:
        rc = f["general/extracellular_ephys/electrodes/ripple_channel"][:]
        loc = _str(f["general/extracellular_ephys/electrodes/location"][:])
        ch = np.where(rc == 1)[0]
        s["ripple_channel"] = int(ch[0]) if len(ch) else None
        s["ripple_channel_location"] = loc[ch[0]] if len(ch) else None
        if len(ch):
            L = f["processing/ecephys/LFP/LFP"]
            s["lfp_rate"] = float(L["starting_time"].attrs["rate"])
            s["lfp_t0"] = float(L["starting_time"][()])
            s["lfp"] = L["data"][:, int(ch[0])] * float(L["data"].attrs["conversion"])
            # the theta phase stored in the file, which the paper's code reads (general/lfp.py get_theta);
            # labelled degrees, but its values run from -pi to pi
            D = f["processing/ecephys/decomposition_phase"]
            bands = list(_str(D["bands/band_name"][:]))
            s["phase_stored"] = D["data"][:, int(ch[0]), bands.index("theta")]
            s["phase_stored_rate"] = float(D["starting_time"].attrs["rate"])
            s["phase_stored_t0"] = float(D["starting_time"][()])
            s["phase_stored_unit"] = D["data"].attrs.get("unit")
    f.close()
    return s


def load_many(asset_ids, workers=6, **kw):
    """Load several sessions in parallel threads (network bound)."""
    with cf.ThreadPoolExecutor(workers) as ex:
        return list(ex.map(lambda a: load_session(a, **kw), asset_ids))


# --- trials ---------------------------------------------------------------------------------
def final_trials(s: dict) -> pd.DataFrame:
    """Final-task trials (maze_id 4) with the pseudo update time on delay only trials
    [claims S5; code general/trials.py: the first time the animal reaches the larger of the
    session's lowest update-onset position on switch trials and 145.125]."""
    tr = s["trials"].copy()
    tr = tr[tr.maze_id == FINAL_MAZE].copy()
    t, y = s["t"], s["xy"][:, 1]
    sw = tr[tr.update_type == 2]
    locs = [y[min(np.searchsorted(t, tu), len(t) - 1)] for tu in sw.t_update]
    uloc = max(np.min(locs), UPDATE_LOC_DEFAULT) if len(locs) else UPDATE_LOC_DEFAULT
    pseudo = []
    for _, r in tr.iterrows():
        if r.update_type == 1:
            i0, i1 = np.searchsorted(t, [r.start_time, r.stop_time])
            k = np.where(y[i0:i1] >= uloc)[0]
            pseudo.append(t[i0 + k[0]] if len(k) else np.nan)
        else:
            pseudo.append(r.t_update)
    tr["t_align"] = pseudo
    tr["update_loc_used"] = uloc
    return tr


# --- track geometry -------------------------------------------------------------------------
def track_bins(s: dict):
    """Feature bins from 5 to the linearized track maximum [claims S2; code get_limits], and the
    arm boundaries [claims S6; code linearize_track_position]: left arm from its minimum - 5 to
    its maximum + 5, right arm from its minimum - 10 to its maximum (at least 380)."""
    lin, seg = s["lin"], s["seg"]
    lmin, lmax = np.round(np.nanmin(lin[seg == 1])), np.round(np.nanmax(lin[seg == 1]))
    rmin, rmax = np.round(np.nanmin(lin[seg == 2])), np.round(np.nanmax(lin[seg == 2]))
    rmax = max(rmax, 380)
    edges = np.linspace(POS_MIN, rmax, N_BINS + 1)
    centers = (edges[:-1] + edges[1:]) / 2
    left = (centers >= lmin - EDGE_SPACING / 4) & (centers <= lmax + EDGE_SPACING / 4)
    right = (centers >= rmin - EDGE_SPACING / 2) & (centers <= rmax)
    home_max = np.round(np.nanmax(lin[seg == 0]))
    central = centers <= home_max
    bound = (lmax + EDGE_SPACING / 4) - (lmin - EDGE_SPACING / 4)
    home_win = np.abs(centers - UPDATE_LOC_DEFAULT) <= bound / 2   # [code home_boundaries]
    retro = (centers >= RETRO_ZONE[0]) & (centers <= RETRO_ZONE[1])
    # bins lying wholly in the artificial gaps between track segments (paper Methods)
    gap = ((edges[:-1] >= home_max) & (edges[1:] <= lmin)) | ((edges[:-1] >= lmax) & (edges[1:] <= rmin))
    return dict(edges=edges, centers=centers, left=left, right=right, central=central,
                home_window=home_win, retro=retro, gap=gap)


# --- encoder / decoder ----------------------------------------------------------------------
def unit_mask(s, region):
    """All units of a region, all three cell types [claims S1; code units_types]."""
    return s["region"] == region


def trial_mask_times(t, trials):
    """Boolean over behaviour samples: inside any of the trials (start to stop)."""
    m = np.zeros(len(t), bool)
    for a, b in zip(trials.start_time, trials.stop_time):
        i0, i1 = np.searchsorted(t, [a, b])
        m[i0:i1] = True
    return m


def encode(s, units, trials, feature, edges, moving_only=True):
    """Occupancy-normalized tuning curves (Hz) from within-trial locomotion samples of the
    training trials [claims S3; paper Methods "only periods within a behavioral trial ... only
    locomotion periods"]. Returns (n_units, n_bins) and the occupancy (s)."""
    t = s["t"]
    m = trial_mask_times(t, trials)
    if moving_only:
        m &= s["moving"]
    dt = np.diff(t, append=t[-1])
    dt = np.clip(dt, 0, 0.1)        # [standard] gaps in the VR clock are not counted as occupancy
    fb = np.digitize(feature, edges) - 1
    ok = m & (fb >= 0) & (fb < len(edges) - 1) & np.isfinite(feature)
    occ = np.bincount(fb[ok], weights=dt[ok], minlength=len(edges) - 1)
    tc = np.zeros((len(units), len(edges) - 1))
    for j, sp in enumerate(units):
        k = np.searchsorted(t, sp) - 1
        k = k[(k >= 0)]
        k = k[ok[k]]
        tc[j] = np.bincount(fb[k], minlength=len(edges) - 1)
    with np.errstate(invalid="ignore", divide="ignore"):
        tc = np.where(occ > 0, tc / occ, 0.0)
    return tc, occ


def bin_counts(units, edges_t):
    """Spike counts of each unit in the given time bin edges (n_bins, n_units)."""
    return np.stack([np.histogram(sp, edges_t)[0] for sp in units], axis=1)


def decode(tc, counts, bin_size):
    """Memoryless Bayesian decoding with a uniform prior, as pynapple decode_1d [claims S4]:
    P(x|n) proportional to prod_i f_i(x)^n_i exp(-tau sum_i f_i(x)). Bins where no unit fires in
    the encoder (the gaps between track segments) are NaN [claims S4; code _decode]."""
    logf = np.log(np.maximum(tc, 1e-12))                     # (units, bins)
    ll = counts @ logf - bin_size * tc.sum(0)[None, :]
    ll -= ll.max(1, keepdims=True)
    p = np.exp(ll)
    p /= p.sum(1, keepdims=True)
    empty = tc.sum(0) == 0
    p[:, empty] = np.nan
    return p


def aligned_edges(t_align, window=WINDOW, bin_size=BIN, start=None):
    """Time bin edges around an event: -window to +window in bins of bin_size
    [claims S5: -2.5 to 2.5 s on a 0.2 s grid]; start=0 gives 0 to +window (trial start)."""
    lo = -window if start is None else start
    n = int(round((window - lo) / bin_size))
    return t_align + lo + bin_size * np.arange(n + 1)


def sample_at(t, x, times):
    """Value of a behaviour series at given times (last sample at or before)."""
    i = np.clip(np.searchsorted(t, times, side="right") - 1, 0, len(t) - 1)
    return x[i]


def bin_mean(t, x, edges_t):
    """Mean of a behaviour series in each time bin."""
    idx = np.digitize(t, edges_t) - 1
    sel = (idx >= 0) & (idx < len(edges_t) - 1)
    s_ = np.bincount(idx[sel], weights=x[sel], minlength=len(edges_t) - 1)
    n_ = np.bincount(idx[sel], minlength=len(edges_t) - 1)
    with np.errstate(invalid="ignore"):
        return s_ / n_


def split_trials(tr, encoder_types=(1,), seed=SPLIT_SEED):
    """Encoder (80%) and test trials [claims S3; code train_test_split(test_size=0.2,
    random_state=21)] of the given trial types. Returns (train, test) DataFrames."""
    from sklearn.model_selection import train_test_split
    enc = tr[tr.update_type.isin(encoder_types)]
    train, _ = train_test_split(enc, test_size=TEST_SIZE, random_state=seed)
    test = tr[~tr.index.isin(train.index)]
    return train, test


def session_decoding(s, region, tr, train, test, geo, units_idx=None, align_col="t_align",
                     window=WINDOW, bin_size=BIN, start=None):
    """Decode each test trial around its alignment time. Returns dict of arrays per trial:
    posterior (n_trials, n_time, n_bins), true linear position, velocities and view angle."""
    sel = np.where(unit_mask(s, region))[0] if units_idx is None else units_idx
    units = [s["spikes"][i] for i in sel]
    tc, occ = encode(s, units, train, s["lin"], geo["edges"])
    out = dict(trial=[], post=[], pos=[], rot=[], trans=[], va=[], tc=tc, occ=occ, n_units=len(units))
    for i, r in test.iterrows():
        ta = r[align_col]
        if not np.isfinite(ta):
            continue
        e = aligned_edges(ta, window, bin_size, start)
        c = bin_counts(units, e)
        out["trial"].append(i)
        out["post"].append(decode(tc, c, bin_size))
        out["pos"].append(bin_mean(s["t"], s["lin"], e))
        out["rot"].append(bin_mean(s["t"], s["rot"], e))
        out["trans"].append(bin_mean(s["t"], s["trans"], e))
        out["va"].append(sample_at(s["t"], s["view_angle"], ta - 1e-9))
    for k in ("post", "pos", "rot", "trans", "va"):
        out[k] = np.array(out[k])
    out["times"] = (aligned_edges(0.0, window, bin_size, start)[:-1] + bin_size / 2)
    return out


def arm_probs(post, geo, turn_type):
    """Integrated posterior over the initial and new goal arms per time bin [claims S6]. The
    initial arm is the side of the original cue: turn_type 1 the left arm (negative x), 2 the
    right [claims comment; code mappings turn_type 1 left; checked in the data]."""
    L = np.nansum(post[..., geo["left"]], -1)
    R = np.nansum(post[..., geo["right"]], -1)
    tt = np.asarray(turn_type)[:, None]
    init = np.where(tt == 1, L, R)
    new = np.where(tt == 1, R, L)
    return init, new


def window_mean(x, times, lo, hi):
    """Mean over the bins whose centres fall in [lo, hi) [claims S7]."""
    m = (times >= lo) & (times < hi)
    return np.nanmean(x[..., m], -1)


# --- statistics -----------------------------------------------------------------------------
def lme(df, value, predictor, animal="animal", session="session"):
    """Linear mixed model value ~ predictor + (1|animal) + (1|animal:session) [claims S9],
    fit by REML with statsmodels MixedLM. Returns the fit, the Wald F test of the predictor
    (Kenward-Roger degrees of freedom are not available in statsmodels; the test uses large-
    sample degrees of freedom), and all pairwise contrasts of the predictor's levels with
    Tukey-adjusted p values (studentized range with k levels), as emmeans pairs()."""
    import statsmodels.formula.api as smf
    from scipy import stats
    d = df[[value, predictor, animal, session]].dropna().copy()
    d["_pred"] = d[predictor].astype(str)
    levels = sorted(d["_pred"].unique())
    d["_pred"] = pd.Categorical(d["_pred"], categories=levels)
    d["_sess"] = d[animal].astype(str) + ":" + d[session].astype(str)
    md = smf.mixedlm(f"{value} ~ 0 + _pred", d, groups=d[animal], re_formula="1",
                     vc_formula={"sess": "0 + C(_sess)"})
    import warnings
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        fit = md.fit(reml=True, method=["lbfgs", "powell"])
    names = [f"_pred[{l}]" for l in levels]
    beta = fit.fe_params[names].to_numpy()
    cov = fit.cov_params().loc[names, names].to_numpy()
    k = len(levels)
    # Wald F for equality of all level means
    C = np.zeros((k - 1, k))
    for i in range(k - 1):
        C[i, 0], C[i, i + 1] = 1, -1
    cb = C @ beta
    W = float(cb @ np.linalg.solve(C @ cov @ C.T, cb))
    F = W / (k - 1)
    pF = float(stats.chi2.sf(W, k - 1))
    rows = []
    for a, b in itertools.combinations(range(k), 2):
        est = beta[a] - beta[b]
        se = np.sqrt(cov[a, a] + cov[b, b] - 2 * cov[a, b])
        z = est / se
        p_t = float(stats.studentized_range.sf(abs(z) * np.sqrt(2), k, 1e4)) if k > 2 else float(2 * stats.norm.sf(abs(z)))
        rows.append(dict(a=levels[a], b=levels[b], estimate=est, z=z, p_tukey=min(p_t, 1.0)))
    emm = pd.Series(beta, index=levels)
    n = d.groupby("_pred", observed=True).size()
    return dict(fit=fit, F=F, df1=k - 1, p_anova=pF, contrasts=pd.DataFrame(rows), emm=emm, n=n)


def contrast(res, a, b):
    """The contrast row a - b (sign flipped if stored as b - a)."""
    c = res["contrasts"]
    r = c[(c.a == a) & (c.b == b)]
    if len(r):
        return dict(r.iloc[0])
    r = dict(c[(c.a == b) & (c.b == a)].iloc[0])
    r.update(a=a, b=b, estimate=-r["estimate"], z=-r["z"])
    return r


# --- theta ----------------------------------------------------------------------------------
THETA_BAND = (4, 12)              # [claims fig3c criterion; paper Methods 4-12 Hz]
THETA_BIN = 0.025                 # [claims S4; paper Methods 25 ms for theta analyses]


def theta_phase(lfp, rate):
    """Theta phase from peaks and troughs of the 4-12 Hz band-passed LFP [paper Methods,
    "Theta cycles and phase": FIR equiripple filter, peaks and troughs define the phase]. The
    filter is a Parks-McClellan (equiripple) band-pass with 1 Hz transition bands [paper; the
    order is a standard choice], applied forward and backward. Phase is 0 at peaks and pi at
    troughs, linear in between, wrapped to (-pi, pi]."""
    from scipy import signal
    dec = 10                                      # [standard] 2 kHz to 200 Hz before filtering
    x = signal.decimate(lfp, dec, ftype="fir", zero_phase=True)
    fs = rate / dec
    b = signal.remez(301, [0, 3, 4, 12, 13, fs / 2], [0, 1, 0], fs=fs)
    y = signal.filtfilt(b, [1.0], x)
    pk = signal.argrelmax(y)[0]
    tr = signal.argrelmin(y)[0]
    ev = np.r_[pk, tr]
    ph = np.r_[np.zeros(len(pk)), np.full(len(tr), np.pi)]
    o = np.argsort(ev)
    ev, ph = ev[o], ph[o]
    ph_unw = np.r_[0, np.cumsum(np.full(len(ph) - 1, np.pi))] + ph[0]
    t = np.arange(len(y)) / fs
    return t, ev, ph_unw


def phase_at(times, t_th, ev, ph_unw, t0=0.0):
    tt = t_th[ev] + t0
    p = np.interp(times, tt, ph_unw)
    return np.angle(np.exp(1j * p))


# --- per-session processing -----------------------------------------------------------------
def view_angle_by_position(s, tr, n=50):
    """Mean view angle per y-position bin of each trial over the central arm, 50 bins
    [claims fig1d criterion; paper Methods, Behavioral analysis; code 50 bins]."""
    edges = np.linspace(POS_MIN, 255, n + 1)
    out = np.full((len(tr), n), np.nan)
    for j, (_, r) in enumerate(tr.iterrows()):
        i0, i1 = np.searchsorted(s["t"], [r.start_time, r.t_choice_made])
        y, va = s["xy"][i0:i1, 1], s["view_angle"][i0:i1]
        b = np.digitize(y, edges) - 1
        ok = (b >= 0) & (b < n)
        sm = np.bincount(b[ok], va[ok], n)
        c = np.bincount(b[ok], minlength=n)
        with np.errstate(invalid="ignore"):
            out[j] = sm / c
    return edges, out


def spread_bins(post):
    """Spread of each decoded posterior in feature bins, as the paper's code
    (plot_region_error_distribution): threshold = peak - std of the posterior; spread = the
    last bin at or after the peak minus the first bin at or before it that reach the threshold."""
    out = np.full(post.shape[:-1], np.nan)
    P = post.reshape(-1, post.shape[-1])
    o = out.reshape(-1)
    for i, p in enumerate(P):
        if np.all(np.isnan(p)):
            continue
        k = np.nanargmax(p)
        thr = p[k] - np.nanstd(p)
        ge = np.nan_to_num(p, nan=-1) >= thr
        before = np.where(ge[:k + 1])[0]
        after = np.where(ge[k:])[0]
        o[i] = (k + after[-1]) - before[0]
    return out


def zone_probs(post, geo, turn_type):
    """Integrated probability per zone and time bin: initial/new goal arms and their front
    (toward the choice point) and back halves, the retrospective zone, the whole central arm
    and the central window around the update cue."""
    init, new = arm_probs(post, geo, turn_type)
    out = dict(init=init, new=new)
    tt = np.asarray(turn_type)[:, None]
    for side in ("left", "right"):
        idx = np.where(geo[side])[0]
        h = len(idx) // 2
        geo[side + "_front"] = np.isin(np.arange(len(geo["centers"])), idx[:h])
        geo[side + "_back"] = np.isin(np.arange(len(geo["centers"])), idx[len(idx) - h:])
    for half in ("front", "back"):
        L = np.nansum(post[..., geo["left_" + half]], -1)
        R = np.nansum(post[..., geo["right_" + half]], -1)
        out["init_" + half] = np.where(tt == 1, L, R)
        out["new_" + half] = np.where(tt == 1, R, L)
    for z in ("retro", "central", "home_window"):
        out[z] = np.nansum(post[..., geo[z]], -1)
    return out


def stats_spearman(a, b):
    from scipy import stats
    return stats.spearmanr(a, b, nan_policy="omit")[0]


def _trialinfo(tr, idx):
    t = tr.loc[idx]
    return dict(trial=np.asarray(idx), update_type=t.update_type.to_numpy(), correct=t.correct.to_numpy(),
                turn_type=t.turn_type.to_numpy())


def process_session(asset_id, subject, session, theta=True, seed=0):
    """Everything the notebook needs from one session, reduced as it loads."""
    s = load_session(asset_id, lfp=theta)
    tr = final_trials(s)
    geo = track_bins(s)
    res = dict(subject=subject, session=session, asset_id=asset_id,
               n_units={r: int((s["region"] == r).sum()) for r in ("CA1", "PFC", "unknown")},
               cell_types=pd.crosstab(s["region"], s["cell_type"]),
               quality=pd.Series(s["quality"]).value_counts().to_dict(),
               trials_all=s["trials"], trials=tr, units_attrs=s["units_attrs"],
               acq_speed_hist=s["acq_speed_hist"], moving_frac=float(s["moving"].mean()),
               pos_range=(np.nanmin(s["xy"], 0), np.nanmax(s["xy"], 0)),
               va_range=(float(np.nanmin(s["view_angle"])), float(np.nanmax(s["view_angle"]))),
               lin_range=(float(np.nanmin(s["lin"])), float(np.nanmax(s["lin"]))),
               spike_range=(min(float(x.min()) for x in s["spikes"] if len(x)),
                            max(float(x.max()) for x in s["spikes"] if len(x))),
               t_range=(float(s["t"][0]), float(s["t"][-1])), geo=geo)
    # checks of the trial table against the behaviour: x at choice made, y at the update cue,
    # and how view angle relates to sideways movement
    tr["x_at_choice"] = sample_at(s["t"], s["xy"][:, 0], tr.t_choice_made.to_numpy())
    tr["y_at_update"] = sample_at(s["t"], s["xy"][:, 1], tr.t_update.to_numpy())
    tr["y_at_delay"] = sample_at(s["t"], s["xy"][:, 1], tr.t_delay.to_numpy())
    m = trial_mask_times(s["t"], tr) & (s["xy"][:, 1] < 250)
    dx = np.gradient(s["xy"][:, 0])
    res["va_dx_r"] = float(stats_spearman(s["view_angle"][m], dx[m]))
    res["trials"] = tr
    res["va_edges"], res["va_traj"] = view_angle_by_position(s, tr)
    res["va_traj_trials"] = tr.index.to_numpy()
    train, test = split_trials(tr)
    res["n_train"] = len(train)
    dec = {}
    for reg in ("CA1", "PFC"):
        if res["n_units"][reg] == 0:
            continue
        o = session_decoding(s, reg, tr, train, test, geo)
        z = zone_probs(o["post"], geo, tr.loc[o["trial"], "turn_type"].values)
        # validation over whole held-out delay only trials, from trial start, 200 ms bins
        v = session_decoding(s, reg, tr, train, test[test.update_type == 1], geo,
                             align_col="start_time", start=0, window=25)
        pk = np.nanargmax(np.nan_to_num(v["post"], nan=-1), -1)
        pb = np.digitize(v["pos"], geo["edges"]) - 1
        dur = (tr.loc[v["trial"], "stop_time"] - tr.loc[v["trial"], "start_time"]).to_numpy()
        inside = v["times"][None, :] + BIN / 2 <= dur[:, None]      # bins inside the trial only
        ok = (pb >= 0) & (pb < N_BINS) & np.isfinite(v["pos"]) & inside
        # clock contrast: the same posteriors against the position 2 s later or earlier
        e_sh = {}
        for sh in (-2.0, 2.0):
            ps = []
            for i in v["trial"]:
                e = aligned_edges(tr.loc[i, "start_time"], 25, BIN, 0) + sh
                ps.append(bin_mean(s["t"], s["lin"], e))
            ps = np.array(ps)
            okk = np.isfinite(ps) & np.isfinite(v["pos"]) & inside
            e_sh[sh] = float(np.median(np.abs(geo["centers"][pk[okk]] - ps[okk])))
        conf = np.zeros((N_BINS, N_BINS))
        np.add.at(conf, (pk[ok], pb[ok]), 1)
        # trial-start aligned (original cue), 0 to 2.5 s [claims sfig3ab; code start_time]
        st = session_decoding(s, reg, tr, train, test[test.update_type == 2], geo,
                              align_col="start_time", start=0)
        zs = zone_probs(st["post"], geo, tr.loc[st["trial"], "turn_type"].values)
        dec[reg] = dict(**_trialinfo(tr, o["trial"]), times=o["times"], zones=z, pos=o["pos"],
                        rot=o["rot"], trans=o["trans"], va=o["va"], peak=geo["centers"][
                            np.nanargmax(np.nan_to_num(o["post"], nan=-1), -1)],
                        tc_peak=o["tc"].argmax(1), tc_active=o["tc"].max(1) > 0, n_units=o["n_units"],
                        val_conf=conf, val_err_shift=e_sh, val_err=np.abs(geo["centers"][pk[ok]] - v["pos"][ok]),
                        val_err_bins=np.abs(pk[ok] - pb[ok]), val_occ_bins=pb[ok],
                        start=dict(**_trialinfo(tr, st["trial"]), times=st["times"], zones=zs))
    res["dec"] = dec
    # CA1 encoder from all trial types [claims sfig2f]: (a) all trials, decode all; (b) 80/20
    if res["n_units"]["CA1"]:
        alltr = tr[tr.update_type.isin([1, 2, 3])]
        oa = session_decoding(s, "CA1", tr, alltr, alltr, geo)
        trb, teb = split_trials(tr, encoder_types=(1, 2, 3))
        ob = session_decoding(s, "CA1", tr, trb, teb, geo)
        res["allenc"] = {}
        for k, o in (("a", oa), ("b", ob)):
            z = zone_probs(o["post"], geo, tr.loc[o["trial"], "turn_type"].values)
            res["allenc"][k] = dict(**_trialinfo(tr, o["trial"]), times=o["times"], init=z["init"], new=z["new"])
    # equal numbers of cells in both regions [claims sfig5f, sfig5g; paper Methods]
    nC, nP = res["n_units"]["CA1"], res["n_units"]["PFC"]
    if min(nC, nP) >= MIN_UNITS:
        rng = np.random.default_rng(seed)
        n = min(nC, nP)
        eq = {}
        for reg in ("CA1", "PFC"):
            idx = np.where(s["region"] == reg)[0]
            idx = np.sort(rng.choice(idx, n, replace=False))
            o = session_decoding(s, reg, tr, train, test, geo, units_idx=idx)
            z = zone_probs(o["post"], geo, tr.loc[o["trial"], "turn_type"].values)
            eq[reg] = dict(**_trialinfo(tr, o["trial"]), times=o["times"], init=z["init"], new=z["new"],
                           spread=spread_bins(o["post"]), pos=o["pos"], n_units=n)
        res["equal"] = eq
    # theta: CA1 decoding in 25 ms bins with the theta phase at each bin centre [claims fig3c]
    if theta and res["n_units"]["CA1"] and s.get("lfp") is not None:
        t_th, ev, ph = theta_phase(s["lfp"], s["lfp_rate"])
        t0 = s["lfp_t0"]
        pyr = np.where((s["region"] == "CA1") & (s["cell_type"] == "Pyramidal Cell"))[0]
        allsp = np.concatenate([s["spikes"][i] for i in pyr]) if len(pyr) else np.array([])
        allsp = allsp[(allsp > t_th[ev[0]] + t0) & (allsp < t_th[ev[-1]] + t0)]
        sp_ph = phase_at(allsp, t_th, ev, ph, t0)
        hist = np.histogram(sp_ph, bins=np.linspace(-np.pi, np.pi, 13))[0]
        ref = -np.pi + np.pi / 12 + np.argmax(hist) * np.pi / 6     # centre of the 30-degree bin of max firing
        sel = tr[tr.update_type.isin([1, 2, 3]) & tr.index.isin(test.index)]
        o = session_decoding(s, "CA1", tr, train, sel, geo, window=1.5, bin_size=THETA_BIN)
        z = zone_probs(o["post"], geo, tr.loc[o["trial"], "turn_type"].values)
        ta = tr.loc[o["trial"], "t_align"].to_numpy()[:, None] + o["times"][None, :]
        phs = np.angle(np.exp(1j * (phase_at(ta, t_th, ev, ph, t0) - ref)))
        # variant: the stored phase, referenced the same way
        def stored_at(x):
            k = np.clip(np.round((x - s["phase_stored_t0"]) * s["phase_stored_rate"]).astype(int), 0, len(s["phase_stored"]) - 1)
            return s["phase_stored"][k]
        sp2 = stored_at(allsp)
        hist2 = np.histogram(sp2, bins=np.linspace(-np.pi, np.pi, 13))[0]
        ref2 = -np.pi + np.pi / 12 + np.argmax(hist2) * np.pi / 6
        phs2 = np.angle(np.exp(1j * (stored_at(ta) - ref2)))
        res["theta"] = dict(**_trialinfo(tr, o["trial"]), times=o["times"], phase=phs, phase_stored=phs2,
                            spike_phase_hist_stored=hist2, stored_unit=s["phase_stored_unit"],
                            stored_range=(float(np.min(s["phase_stored"])), float(np.max(s["phase_stored"]))),
                            init=z["init"], new=z["new"], central=z["central"], home_window=z["home_window"],
                            spike_phase_hist=hist, ref=ref, channel=s["ripple_channel"],
                            channel_location=s["ripple_channel_location"])
    return res


# --- assembling results across sessions -----------------------------------------------------
def included(r, reg, rule="train"):
    """Session inclusion for decoding [claims S1]: at least 20 units in the region and at least
    50 trials; rule 'train' counts the encoder training trials (the code), rule 'final' the
    final-task trials (a reading of the Methods' "50 trials for the behavioral session")."""
    n_tr = r["n_train"] if rule == "train" else len(r["trials"])
    return r["n_units"].get(reg, 0) >= MIN_UNITS and n_tr >= MIN_TRIALS and reg in r.get("dec", {})


def trial_table(R, reg, windows, rule="train", source="dec"):
    """One row per decoded trial of included sessions, with the mean of each zone in each window
    (name -> (zone, lo, hi)), plus trial labels. source 'dec' (update aligned) or 'start'."""
    rows = []
    for r in R:
        if not included(r, reg, rule):
            continue
        d = r["dec"][reg] if source == "dec" else r["dec"][reg]["start"]
        z = d["zones"]
        df = pd.DataFrame(dict(animal=r["subject"], session=r["session"], trial=d["trial"],
                               update_type=d["update_type"], correct=d["correct"], turn_type=d["turn_type"]))
        for name, (zone, lo, hi) in windows.items():
            df[name] = window_mean(z[zone], d["times"], lo, hi)
        rows.append(df)
    out = pd.concat(rows, ignore_index=True)
    out["type"] = out.update_type.map(TRIAL_TYPES)
    return out


def long_format(df, cols, name="zone", value="value"):
    """Stack value columns into long format for the LME, with the column name as a factor."""
    keep = [c for c in df.columns if c not in cols]
    return df.melt(id_vars=keep, value_vars=cols, var_name=name, value_name=value)
