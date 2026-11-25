"""Loading and Tree-Maze measures for Gonzalez & Giocomo (2024) on DANDI:000405.

The dandiset has no published version; the draft is read, and its modification
time is kept in DRAFT_MODIFIED so that a change can be detected.

Where the parameters come from:

- The claims file's opening comment and criteria, which cite the paper's code,
  https://github.com/alexgonzl/TMA at commit 6f935935d93a9a27f931f6e73c05d965dfbb862a
  (MIT licence). The maze geometry (TreeMazeZones), the trial windows, the
  blanking of samples, the balanced resampling, the remapping score and the
  segment rate comparison below are ports of that code
  (Analyses/tree_maze_functions.py), cited function by function.
- Details the claims file does not give, taken from the same code (author,
  step 1.6), cited where used: the session left out as invalid
  (experiment_info.py, SummaryInfo.invalid_sessions), the speed limits of the
  speed control (TrialAnalyses.__init__, sp_valid_limits 20 to 1000 mm/s), the
  reward blanking window (the event table's 'R_blank' events, 25 samples).
- Random draws use a generator seeded from the claim (docs/protocol.md), not
  the code's seed 0.
"""

from __future__ import annotations

import json
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
from scipy import stats
from shapely import contains_xy
from shapely.geometry import Polygon

DANDISET = "000405"
VERSION = "draft"  # no published version exists
DRAFT_MODIFIED = "2023-06-20T00:56:24.445627Z"
API = "https://api.dandiarchive.org/api"
TIME_STEP = 0.02  # s; firing_rates rate is 50 Hz
# experiment_info.py, SummaryInfo.invalid_sessions (the paper's code leaves these out)
INVALID_SESSIONS = ["Li_OF_080718", "Cl_T3g_121418_0"]
SUBJECTS = {"s0": "Li", "s1": "Ne", "s2": "Cl", "s3": "Al", "s4": "Ca"}
MIN_UNITS, MIN_TRIALS = 1, 50  # Results, paragraph 2 (claims file, fig1d-task-performance)


# ----------------------------------------------------------------------------- archive

def _get_json(url):
    for k in range(5):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                return json.load(r)
        except Exception:
            time.sleep(2 + 3 * k)
    raise RuntimeError(url)


def version_info():
    return _get_json(f"{API}/dandisets/{DANDISET}/versions/{VERSION}/info/")


def list_assets():
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=1000"
    out = []
    while url:
        d = _get_json(url)
        out += d["results"]
        url = d.get("next")
    df = pd.DataFrame(out)[["asset_id", "path", "size"]]
    return df.sort_values("path").reset_index(drop=True)


def open_asset(asset_id):
    url = f"{API}/assets/{asset_id}/download/"
    for k in range(5):
        try:
            return h5py.File(remfile.File(url), "r")
        except Exception:
            time.sleep(2 + 3 * k)
    raise RuntimeError(asset_id)


def _col(g, c):
    x = g[c][:]
    if x.dtype == object:
        x = np.array([v.decode() if isinstance(v, bytes) else v for v in x], dtype=object)
    return x


def _table(g):
    return pd.DataFrame({c: _col(g, c) for c in g.keys() if c != "id"})


def read_meta(asset_id):
    """Metadata, tables and array shapes of one file (no large arrays)."""
    f = open_asset(asset_id)
    A = f["acquisition"]
    r = dict(session=f["general/session_id"][()].decode(),
             task=f["session_description"][()].decode(),
             subject_id=f["general/subject/subject_id"][()].decode(),
             identifier=f["identifier"][()].decode(),
             start=f["session_start_time"][()].decode(),
             acquisition=sorted(A.keys()),
             fr_shape=A["firing_rates/data"].shape,
             fr_unit=A["firing_rates/data"].attrs["unit"],
             fr_rate=float(A["firing_rates/starting_time"].attrs["rate"]),
             td_shape=A["track_data/data"].shape,
             td_desc=A["track_data"].attrs["description"],
             td_unit=A["track_data/data"].attrs["unit"],
             td_rate=float(A["track_data/starting_time"].attrs["rate"]),
             units=_table(A["unit_table"]))
    if "trial_table" in A:
        r["trials"] = _table(A["trial_table"])
        r["events"] = _table(A["event_table"])
    f.close()
    return r


def read_all_meta(assets, n_jobs=16):
    with ThreadPoolExecutor(n_jobs) as ex:
        res = list(ex.map(read_meta, assets.asset_id))
    for r, p in zip(res, assets.path):
        r["path"] = p
    return res


def read_session(asset_id):
    """Firing rates [units x samples] and track data of one Tree-Maze file.

    The code writes track_data as get_track_data()[1:] with columns t, x, y, ha
    (experiment_info.py, session_to_nwb), so the file's first row is sample 1;
    a row of NaN is put back in front so that row k is sample k, as the trial
    table's sample indices expect."""
    f = open_asset(asset_id)
    A = f["acquisition"]
    fr = A["firing_rates/data"][:].T.astype(float)
    td = A["track_data/data"][:]
    f.close()
    td = np.vstack([np.full((1, td.shape[1]), np.nan), td])
    track = pd.DataFrame(td, columns=["t", "x", "y", "ha"])
    return fr, track


# ----------------------------------------------------------------------------- maze

class TreeMazeZones:
    """Port of tree_maze_functions.py, TreeMazeZones: the 15 zones, the linear
    segments cut into sub-segments 60 mm long, and the map of sub-segments to
    the big segments left, stem and right."""
    zones_coords = {'H': [(-250, -80), (-250, 80), (250, 80), (250, -80)],
                    'D': [(-80, 500), (-88, 450), (-150, 450), (-150, 600), (0, 700), (150, 600), (150, 450),
                          (88, 450), (80, 500)],
                    'a': [(150, 80), (-150, 80), (-80, 500), (80, 500)],
                    'b': [(150, 600), (0, 700), (220, 990), (329, 900)],
                    'e': [(0, 700), (-150, 600), (-329, 900), (-220, 990)],
                    'c': [(560, 800), (520, 1180), (450, 1180), (329, 900)],
                    'd': [(450, 1260), (50, 1190), (220, 990), (450, 1180)],
                    'f': [(-50, 1190), (-450, 1260), (-450, 1180), (-220, 990)],
                    'g': [(-520, 1180), (-560, 800), (-329, 900), (-450, 1180)],
                    'G1': [(520, 1180), (800, 1180.5), (800, 800), (560, 800)],
                    'G2': [(50, 1190), (50, 1450), (450, 1450), (450, 1260)],
                    'G3': [(-50, 1190), (-50, 1450), (-450, 1450), (-450, 1260)],
                    'G4': [(-520, 1180), (-800, 1180.5), (-800, 800), (-560, 800)],
                    'i1': [(220, 990), (450, 1180), (329, 900)],
                    'i2': [(-329, 900), (-450, 1180), (-220, 990)]}
    zone_names = ['H', 'a', 'D', 'b', 'i1', 'c', 'G1', 'd', 'G2', 'e', 'i2', 'f', 'G3', 'g', 'G4']
    linear_segs = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    wells = ['H', 'D', 'G1', 'G2', 'G3', 'G4']
    bigseg_names = ['left', 'stem', 'right']
    split_segs = {'right': ['b', 'c', 'd', 'i1', 'G1', 'G2'],
                  'left': ['e', 'f', 'g', 'i2', 'G3', 'G4'],
                  'stem': ['H', 'a', 'D']}
    ext_length, sub_seg_length, n_repeats, min_sub_seg_area = 200, 60, 10, 6000

    def __init__(self):
        self.zones_geom = {z: Polygon(self.zones_coords[z]) for z in self.zone_names}
        self.sub_segs = self._divide_segs()
        self.all_segs_names = []
        for zo in self.zone_names:
            if zo in self.linear_segs:
                self.all_segs_names += list(self.sub_segs[zo].keys())
            else:
                self.all_segs_names.append(zo)
        self.n_all_segs = len(self.all_segs_names)
        self.zone_index = {z: i for i, z in enumerate(self.all_segs_names)}
        self.subseg_parent = [z.split('_')[0] for z in self.all_segs_names]
        big = np.zeros((self.n_all_segs, 3), dtype=int)
        for i, p in enumerate(self.subseg_parent):
            for j, b in enumerate(self.bigseg_names):
                if p in self.split_segs[b]:
                    big[i, j] = 1
        self.subseg2bigseg = big
        self.valid_transition_mat = self._valid_transition_mat()

    # Lines2Polygons, as in the code
    @staticmethod
    def _line_angle(p0, p1):
        return np.arctan2(p1[1] - p0[1], p1[0] - p0[0])

    def _extend_line(self, line_points, buffer):
        idx = np.argsort(np.asarray(line_points)[:, 1])
        sp = line_points[idx]
        th = self._line_angle(sp[0], sp[1])
        wh = buffer * np.array((np.cos(th), np.sin(th)))
        out = np.array((sp[0] - wh, sp[1] + wh))
        return out if idx[0] == 0 else out[::-1]

    def _project_line(self, line_points, l):
        p0, p1 = line_points
        th = self._line_angle(p0, p1)
        th_d = np.rad2deg(th)
        pi2 = np.pi / 2
        if (th_d >= 0) & (th_d <= 180):
            wh = l * np.array((np.cos(pi2 - th), -np.sin(pi2 - th)))
        else:
            wh = l * np.array((np.cos(5 * pi2 - th), -np.sin(5 * pi2 - th)))
        return np.array((p0 + wh, p1 + wh))

    def _divide_segs(self):
        out = {}
        for seg in self.linear_segs:
            geom = self.zones_geom[seg]
            line = np.asarray(self.zones_coords[seg][:2], dtype=float)
            e_line = self._extend_line(line, self.ext_length)
            l_s = np.arange(-self.n_repeats * self.sub_seg_length, self.n_repeats * self.sub_seg_length + 1,
                            self.sub_seg_length)
            lines = [self._project_line(e_line, l) for l in l_s]
            polys = [Polygon([lines[i][0], lines[i][1], lines[i + 1][1], lines[i + 1][0]])
                     for i in range(len(lines) - 1)]
            subs, small, cnt = [], Polygon(), -1
            for p in polys:
                inter = geom.intersection(p)
                if inter.area >= self.min_sub_seg_area:
                    subs.append(inter)
                    cnt += 1
                    if small.area > 1:
                        subs[cnt] = subs[cnt].union(small)
                        small = Polygon()
                elif inter.area > 1:
                    if cnt > 0:
                        subs[cnt] = subs[cnt].union(inter)
                    else:
                        small = inter
            out[seg] = {f"{seg}_{i}": g for i, g in enumerate(subs)}
        return out

    def _valid_transition_mat(self):
        names = self.all_segs_names
        M = pd.DataFrame(np.eye(len(names), dtype=bool), index=names, columns=names)
        ss = {s: list(self.sub_segs[s].keys()) for s in self.linear_segs}
        for s in self.linear_segs:
            M.loc[ss[s], ss[s]] = True
        pairs = [('H', 'a'), ('a', 'D'), ('D', 'b'), ('b', 'i1'), ('i1', 'c'), ('c', 'G1'), ('i1', 'd'),
                 ('d', 'G2'), ('D', 'e'), ('e', 'i2'), ('i2', 'f'), ('f', 'G3'), ('i2', 'g'), ('g', 'G4'),
                 ('f', 'g'), ('c', 'd'), ('a', 'b'), ('a', 'e')]
        for a, b in pairs:
            M.loc[ss.get(a, a), ss.get(b, b)] = True
        v = M.values
        sym = np.triu(v) + np.triu(v, 1).T
        return sym.astype(bool)

    def pos_zones(self, x, y):
        """Sub-segment index of each sample, -1 where the sample is in no zone or
        not tracked (get_pos_zone_ts; the code assigns those samples to a zone
        but lists them as invalid, and TrialAnalyses blanks them)."""
        x = np.asarray(x, float)
        y = np.asarray(y, float)
        pz = np.full(len(x), -1, dtype=int)
        found = np.zeros(len(x), dtype=bool)
        ok = ~np.isnan(x) & ~np.isnan(y)
        for zo in self.zone_names:
            inz = ok & ~found & contains_xy(self.zones_geom[zo], x, y)
            if zo in self.linear_segs:
                sub_found = np.zeros(len(x), dtype=bool)
                for name, g in self.sub_segs[zo].items():
                    ins = inz & ~sub_found & contains_xy(g, x, y)
                    pz[ins] = self.zone_index[name]
                    sub_found |= ins
            else:
                pz[inz] = self.zone_index[zo]
            found |= inz
        return pz

    def valid_transitions(self, pz):
        """check_valid_pos_zones_transitions: False at a sample reached from the
        previous sample by a transition the maze does not allow."""
        v = np.ones(len(pz), dtype=bool)
        a, b = pz[:-1], pz[1:]
        both = (a >= 0) & (b >= 0)
        bad = np.zeros(len(a), dtype=bool)
        bad[both] = ~self.valid_transition_mat[a[both], b[both]]
        v[1:] = ~bad
        return v


TMZ = TreeMazeZones()


# ----------------------------------------------------------------------------- trials

def session_perf(trials):
    """BehaviorData.get_session_perf: fraction correct over trials with a
    correct flag (change-of-mind trials carry none), Switch trials from sw."""
    df = trials
    n_sw = df.sw.sum()
    return dict(n_trials=len(df), n_sw_trials=int(n_sw), pct_correct=df.correct.mean(),
                pct_sw_correct=(df.sw * df.correct).sum() / n_sw if n_sw else np.nan,
                pct_nsw_correct=df.correct[df.sw == 0].mean())


def speed(track):
    """spatial_functions.compute_velocity, in mm/s."""
    dx = np.append(0, np.diff(track.x.values))
    dy = np.append(0, np.diff(track.y.values))
    return np.sqrt(dx ** 2 + dy ** 2) / TIME_STEP


def event_vector(events, name, n):
    """BehaviorData._make_event_vector."""
    v = np.zeros(n, dtype=bool)
    for _, e in events[events.event == name].iterrows():
        v[int(e.t0):int(e.tE) + 1] = True
    return v


class Session:
    """The parts of tree_maze_functions.py, TrialAnalyses, that the claims use.

    Default trial parameters (experiment_info.py, _default_trial_analyses_params):
    trial end tE_2, samples outside the zones and invalid zone transitions
    blanked, no reward or speed blanking. Outbound runs are t0 to tE_2, inbound
    runs tE_2 to tR, both inclusive (get_trials_t0_tE)."""

    occ_bigseg = 5  # TrialAnalyses.occupation_thrs['bigseg']

    def __init__(self, fr, track, trials, events, reward_blank=False, speed_blank=False,
                 sp_valid_limits=(20, 1000)):
        self.n_units, self.n_samps = fr.shape
        self.trials = trials.reset_index(drop=True)
        self.n_trials = len(trials)
        pz = TMZ.pos_zones(track.x.values, track.y.values)
        blank = pz < 0
        valid_tr = TMZ.valid_transitions(pz)
        blank |= ~valid_tr
        if reward_blank:
            blank |= event_vector(events, 'R_blank', self.n_samps)
        if speed_blank:
            sp = speed(track)
            with np.errstate(invalid='ignore'):
                blank |= ~((sp >= sp_valid_limits[0]) & (sp <= sp_valid_limits[1]))
        pz = pz.copy()
        pz[blank] = -1
        self.pz = pz
        self.n_blank = int(blank.sum())
        fr = np.nan_to_num(fr)
        nz = TMZ.n_all_segs
        self.zone_rates, self.zone_counts = {}, {}
        for seg in ['out', 'in']:
            t0 = self.trials.t0.values if seg == 'out' else self.trials.tE_2.values
            tE = self.trials.tE_2.values if seg == 'out' else self.trials.tR.values
            R = np.full((self.n_trials, self.n_units, nz), np.nan)
            C = np.zeros((self.n_trials, nz))
            for i in range(self.n_trials):
                s = np.arange(int(t0[i]), int(tE[i]) + 1)
                s = s[s < self.n_samps]
                z = pz[s]
                k = z >= 0
                c = np.bincount(z[k], minlength=nz).astype(float)
                sums = np.zeros((self.n_units, nz))
                np.add.at(sums.T, z[k], fr[:, s[k]].T)
                with np.errstate(invalid='ignore', divide='ignore'):
                    r = sums / c
                r[:, c < 1] = np.nan
                R[i] = r
                C[i] = c
            self.zone_rates[seg] = R
            self.zone_counts[seg] = C
        self.cond = self._conditions()

    def _conditions(self):
        """generate_trial_condition_table."""
        t = self.trials
        n = self.n_trials
        even = np.ones(n, dtype=bool)
        even[::2] = False
        odd = np.ones(n, dtype=bool)
        odd[1::2] = False
        return pd.DataFrame(dict(CL=(t.cue == 'L').values, CR=(t.cue == 'R').values,
                                 Co=(t.correct == 1).values, Inco=(t.correct == 0).values,
                                 Even=even, Odd=odd, All=np.ones(n, dtype=bool)))

    def bigseg_rates(self, seg):
        """get_trial_segment_rates with segment_type 'bigseg': trial rate in
        left, stem and right, NaN where the trial has fewer than 5 samples in
        the segment. Returns [trials x units x 3]."""
        R = np.nan_to_num(self.zone_rates[seg])
        C = self.zone_counts[seg]
        sc = C @ TMZ.subseg2bigseg
        sums = np.einsum('tuz,tz,zb->tub', R, C, TMZ.subseg2bigseg)
        with np.errstate(invalid='ignore', divide='ignore'):
            out = sums / sc[:, None, :]
        out[np.broadcast_to((sc < self.occ_bigseg)[:, None, :], out.shape)] = np.nan
        return out

    def boot_trials(self, cond, sub_conds, n_boot, rng_seed):
        """get_trials_boot_cond_set: each sub-condition resampled with
        replacement to the mean of the smallest and largest sub-condition size.
        Returns [n_trials x n_boot], or None where a sub-condition is empty
        (the code fails on such a session and leaves it out)."""
        rng = np.random.RandomState(rng_seed)
        ct = self.cond[cond].values
        sets = [np.where(ct & self.cond[sc].values)[0] for sc in sub_conds]
        if min(len(s) for s in sets) == 0:
            return None
        n = int((min(len(s) for s in sets) + max(len(s) for s in sets)) / 2)
        out = np.zeros((n * len(sets), n_boot), dtype=int)
        for b in range(n_boot):
            out[:, b] = np.hstack([rng.choice(s, n, replace=True) for s in sets])
        return out


# balanced pairs (TrialAnalyses.bal_cond_pairs, test_null_bal_cond_pairs)
BAL = {'CR_bo': ('CR', ['Co', 'Inco'], 'out'), 'CL_bo': ('CL', ['Co', 'Inco'], 'out'),
       'Even_bo': ('Even', ['CL', 'CR'], 'out'), 'Odd_bo': ('Odd', ['CL', 'CR'], 'out'),
       'Co_bi': ('Co', ['CL', 'CR'], 'in'), 'Inco_bi': ('Inco', ['CL', 'CR'], 'in'),
       'Even_bi': ('Even', ['CL', 'CR'], 'in'), 'Odd_bi': ('Odd', ['CL', 'CR'], 'in')}
TESTS = {'cue': (('CR_bo', 'CL_bo'), ('Even_bo', 'Odd_bo')),
         'rw': (('Co_bi', 'Inco_bi'), ('Even_bi', 'Odd_bi'))}
# Variant of the reward null that the Figure 4d paragraph describes ("an equal
# number of rewarded and unrewarded trials"): even and odd inbound trials, each
# balanced for correct and incorrect.
BAL_RW_NULL_CO = {'Even_bi': ('Even', ['Co', 'Inco'], 'in'), 'Odd_bi': ('Odd', ['Co', 'Inco'], 'in')}


# ----------------------------------------------------------------------------- correlations

def kendall_tau_b(X, Y):
    """Kendall tau-b of each row pair of X and Y [n x k], over the columns
    where both are finite (as pandas corrwith(method='kendall') does)."""
    X = np.asarray(X, float)
    Y = np.asarray(Y, float)
    ok = np.isfinite(X) & np.isfinite(Y)
    iu = np.triu_indices(X.shape[1], 1)
    out = np.full(X.shape[0], np.nan)
    for start in range(0, X.shape[0], 256):
        sl = slice(start, start + 256)
        x, y, m = X[sl], Y[sl], ok[sl]
        dx = np.sign(x[:, :, None] - x[:, None, :])[:, iu[0], iu[1]]
        dy = np.sign(y[:, :, None] - y[:, None, :])[:, iu[0], iu[1]]
        pm = (m[:, :, None] & m[:, None, :])[:, iu[0], iu[1]]
        dx = np.where(pm, dx, 0)
        dy = np.where(pm, dy, 0)
        s = (dx * dy).sum(1)
        n1 = (dx != 0).sum(1)
        n2 = (dy != 0).sum(1)
        with np.errstate(invalid='ignore', divide='ignore'):
            t = s / np.sqrt(n1.astype(float) * n2)
        npair = m.sum(1)
        t[npair < 2] = np.nan
        out[sl] = t
    return out


def pearson_rows(X, Y):
    X = np.asarray(X, float)
    Y = np.asarray(Y, float)
    ok = np.isfinite(X) & np.isfinite(Y)
    out = np.full(X.shape[0], np.nan)
    for i in range(X.shape[0]):
        x, y = X[i, ok[i]], Y[i, ok[i]]
        if len(x) > 2 and x.std() > 0 and y.std() > 0:
            out[i] = np.corrcoef(x, y)[0, 1]
    return out


def corr_to_z(r, method):
    with np.errstate(divide='ignore', invalid='ignore'):
        if method == 'kendall':
            r = np.sin(np.pi * r * 0.5)  # robust_stats.kendall2pearson
        z = np.arctanh(r)  # robust_stats.fisher_r2z
    z = np.where(np.isfinite(z), z, np.nan)
    return z


def compare_corrs(r1, r2, n1, n2, method):
    """robust_stats.compare_corrs; infinite values set to NaN as in
    all_zone_remapping_analyses."""
    with np.errstate(divide='ignore', invalid='ignore'):
        a = np.sin(np.pi * r1 * 0.5) if method == 'kendall' else r1
        b = np.sin(np.pi * r2 * 0.5) if method == 'kendall' else r2
        zd = (np.arctanh(a) - np.arctanh(b)) / np.sqrt(1 / (n1 - 3) + 1 / (n2 - 3))
    return np.where(np.isfinite(zd), zd, np.nan)


def remap_scores(ses, comp, seed, n_boot=100, method='kendall', bal=None, min_valid_trials=5):
    """Single-unit remapping score (all_zone_remapping_analyses, column
    '<test>-<null>-corr_zm'): per resample, the correlation over zones of the
    two mean zone rate maps of the test pair and of the null pair, compared by
    compare_corrs with n the number of zones, then averaged over resamples.
    Each balanced trial set is drawn from a generator started at `seed`, as the
    code reseeds for each set. Returns an array per unit (NaN where the session
    has too few trials)."""
    bal = {**BAL, **(bal or {})}
    test, null = TESTS[comp]
    nz = TMZ.n_all_segs
    corrs = []
    for pair in (test, null):
        maps = []
        for c in pair:
            cond, subs, seg = bal[c]
            tr = ses.boot_trials(cond, subs, n_boot, seed)
            if tr is None or tr.shape[0] < min_valid_trials:
                return np.full(ses.n_units, np.nan)
            R = ses.zone_rates[seg]
            with np.errstate(invalid='ignore'):
                import warnings
                with warnings.catch_warnings():
                    warnings.simplefilter('ignore')
                    m = np.stack([np.nanmean(R[tr[:, b]], axis=0) for b in range(n_boot)])  # boot x unit x zone
            maps.append(m)
        A = maps[0].reshape(-1, nz)
        B = maps[1].reshape(-1, nz)
        r = kendall_tau_b(A, B) if method == 'kendall' else pearson_rows(A, B)
        corrs.append(r.reshape(n_boot, ses.n_units))
    zd = compare_corrs(corrs[0], corrs[1], nz, nz, method)
    import warnings
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        return np.nanmean(zd, axis=0)


def pop_remap_score(ses, comp, seed, units=None, n_boot=100, method='kendall', min_valid_trials=5):
    """Population remapping score (pop_zone_remapping_analyses, with
    get_pop_zone_rates normalize=True, norm95=True): each unit's trial zone
    rates are clipped at their 95th percentile and divided by it, the units'
    zones are stacked into one map, and the maps are compared as for single
    units with n = n_units x n_zones."""
    test, null = TESTS[comp]
    if units is None:
        units = np.arange(ses.n_units)
    nz = TMZ.n_all_segs
    pop = {}
    for seg in ['out', 'in']:
        R = ses.zone_rates[seg][:, units, :].copy()
        for j in range(R.shape[1]):
            x = R[:, j, :]
            v = x[~np.isnan(x)]
            if len(v) == 0:
                continue
            mx = np.percentile(v, 95)
            x[x > mx] = mx
            R[:, j, :] = x / mx
        pop[seg] = R.reshape(R.shape[0], -1)
    corrs = []
    for pair in (test, null):
        sets = []
        for c in pair:
            cond, subs, seg = BAL[c]
            tr = ses.boot_trials(cond, subs, n_boot, seed)
            if tr is None or tr.shape[0] < min_valid_trials:
                return np.nan
            sets.append((tr, seg))
        r = np.zeros(n_boot)
        import warnings
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            for b in range(n_boot):
                m1 = np.nanmean(pop[sets[0][1]][sets[0][0][:, b]], axis=0)
                m2 = np.nanmean(pop[sets[1][1]][sets[1][0][:, b]], axis=0)
                ok = np.isfinite(m1) & np.isfinite(m2)
                if method == 'kendall':
                    r[b] = stats.kendalltau(m1[ok], m2[ok])[0]
                else:
                    r[b] = np.corrcoef(m1[ok], m2[ok])[0, 1]
        corrs.append(r)
    nf = ses.n_units * nz  # the code uses all of the session's units here
    zd = compare_corrs(corrs[0], corrs[1], nf, nf, method)
    return np.nanmean(zd)


def mannwhitney_z(x, y):
    """robust_stats.mannwhitney_z: z of the U statistic of x against y."""
    x = x[~np.isnan(x)]
    y = y[~np.isnan(y)]
    n1, n2 = len(x), len(y)
    if n1 == 0 or n2 == 0:
        return np.nan
    u = stats.mannwhitneyu(x, y).statistic
    return (u - n1 * n2 / 2) / np.sqrt(n1 * n2 * (n1 + n2 + 1) / 12)


def segment_uz(ses, comp):
    """rate_segment_comp_analysis: per unit and big segment, U_Z of the trial
    segment rates of CR against CL outbound trials ('cue') or of correct
    against incorrect inbound trials ('rw'). Returns [units x 3]
    (left, stem, right)."""
    c1, c2, seg = ('CR', 'CL', 'out') if comp == 'cue' else ('Co', 'Inco', 'in')
    S = ses.bigseg_rates(seg)
    t1 = ses.cond[c1].values
    t2 = ses.cond[c2].values
    out = np.full((ses.n_units, 3), np.nan)
    for u in range(ses.n_units):
        for j in range(3):
            out[u, j] = mannwhitney_z(S[t1, u, j], S[t2, u, j])
    return out


# ----------------------------------------------------------------------------- statistics

def logit(p):
    return np.log(p / (1 - p))


def lrt(full, null):
    """paper_stats.py, LRT: df is the difference in the number of parameters."""
    d = len(full.params) - len(null.params)
    v = 2 * (full.llf - null.llf)
    return v, d, stats.chi2.sf(v, d)


def mixed(formula, df, vc, groups='subject', reml=True):
    import warnings
    import statsmodels.formula.api as smf
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        return smf.mixedlm(formula, df, groups=groups, re_formula='1', vc_formula=vc).fit(reml=reml)


def clock_check(fr, ses, shifts=(0, 250, -250)):
    """Clock check (docs/protocol.md, author step 2): the Kendall correlation,
    per unit, between the mean outbound zone maps of even and of odd trials,
    with the rates shifted by each number of samples against the position
    (a circular shift). Rates and tracking on one clock give maps that agree
    better unshifted. Returns the median over units for each shift."""
    out = {}
    fr = np.nan_to_num(fr)
    tr = ses.trials
    nz = TMZ.n_all_segs
    even = np.arange(ses.n_trials) % 2 == 0
    for sh in shifts:
        f = np.roll(fr, sh, axis=1) if sh else fr
        maps = np.zeros((2, ses.n_units, nz))
        cnt = np.zeros((2, nz))
        for i in range(ses.n_trials):
            s = np.arange(int(tr.t0[i]), int(tr.tE_2[i]) + 1)
            s = s[s < ses.n_samps]
            z = ses.pz[s]
            k = z >= 0
            g = 0 if even[i] else 1
            np.add.at(maps[g].T, z[k], f[:, s[k]].T)
            cnt[g] += np.bincount(z[k], minlength=nz)
        with np.errstate(invalid='ignore', divide='ignore'):
            maps = maps / cnt[:, None, :]
        out[sh] = float(np.nanmedian(kendall_tau_b(maps[0], maps[1])))
    return out


# ----------------------------------------------------------------------------- zone encoders

def _zone_lag_features(z, max_lag):
    """ZoneEncoder._add_zone_lags with the inverse decay: one-hot zones of a
    trial's samples plus, for each lag 1 .. |max_lag| - 1 in the direction of
    max_lag, the zones that many samples ahead (max_lag > 0) or behind
    (max_lag < 0) weighted 1/|lag|; each row divided by its maximum (rows with
    no zone stay zero)."""
    nz = TMZ.n_all_segs
    X = np.zeros((len(z), nz))
    k = z >= 0
    X[np.where(k)[0], z[k]] = 1.0
    if max_lag == 0:
        return X
    X2 = X.copy()
    N = len(X)
    sgn = int(np.sign(max_lag))
    for lag in range(sgn, max_lag, sgn):
        b = 1 / abs(lag)
        if lag < 0:
            X2[abs(lag):] += b * X[:N + lag]
        else:
            X2[:N - lag] += b * X[lag:]
    mx = np.abs(X2).max(axis=1)
    with np.errstate(invalid='ignore', divide='ignore'):
        X2 = X2 / mx[:, None]
    return np.nan_to_num(X2)


def encoder_scores(fr, ses, seg, models, runs, min_dur=100, max_dur=2000):
    """Test-fold R2 of zone encoders (tree_maze_functions.py, ZoneEncoder and
    zone_encoding_analyses): least squares without intercept on zone features
    (look-ahead lags), trained on folds balanced for cue (get_cue_balanced_xval_table:
    left- and right-cue trials split into n_folds test sets, and an equal
    number of each drawn without replacement from the rest for training), with
    training samples weighted by the proportion of correct and incorrect trials
    (_get_fold_sample_weights, 'correct'). Trials of 2 to 40 s
    (min_trial_dur 100, max_trial_dur 2000 samples); trials without a correct
    flag are left out. Blanked samples are dropped. models: dict name ->
    (max_lag, cond_type) with cond_type None, 'fixed' (two condition inputs) or
    'inter' (zones split by condition); the condition is the cue for
    outbound and reward for inbound runs. runs: list of (n_folds, seed, label);
    the statistics of each trial are computed once. Returns a table
    unit x fold x model x run."""
    tr = ses.trials
    t0 = tr.t0.values if seg == 'out' else tr.tE_2.values
    tE = tr.tE_2.values if seg == 'out' else tr.tR.values
    dur = tE - t0
    valid = np.where((dur <= max_dur) & (dur >= min_dur) & tr.correct.notna().values)[0]
    cond = (tr.cue.values == 'L') if seg == 'out' else (tr.correct.values == 1)
    correct = tr.correct.values == 1
    fr = np.nan_to_num(fr)
    nz = TMZ.n_all_segs
    # per trial sufficient statistics of [X, 1] and the rates over unblanked samples,
    # so that each fold's weighted least squares and test R2 are exact sums over trials
    stats_ = {}
    for lag in sorted({m[0] for m in models.values()}):
        st = {}
        for i in valid:
            s_ = np.arange(int(t0[i]), int(tE[i]) + 1)
            s_ = s_[s_ < ses.n_samps]
            X = _zone_lag_features(ses.pz[s_], lag)
            keep = ses.pz[s_] >= 0
            X1 = np.hstack([X[keep], np.ones((keep.sum(), 1))])
            Y = fr[:, s_[keep]].T
            st[i] = (X1.T @ X1, X1.T @ Y, (Y ** 2).sum(0), Y.sum(0), keep.sum())
        stats_[lag] = st

    def M(ctype, c):
        """map from [X, 1] to the model's design"""
        if ctype is None:
            m = np.zeros((nz + 1, nz)); m[:nz] = np.eye(nz)
        elif ctype == 'fixed':
            m = np.zeros((nz + 1, nz + 2)); m[:nz, :nz] = np.eye(nz); m[nz, nz + (0 if c else 1)] = 1
        else:
            m = np.zeros((nz + 1, 2 * nz)); m[:nz, (0 if c else nz):(nz if c else 2 * nz)] = np.eye(nz)
        return m

    def make_folds(n_folds, seed):
        rng = np.random.RandomState(seed)
        L = np.intersect1d(valid, np.where(tr.cue.values == 'L')[0])
        Rr = np.intersect1d(valid, np.where(tr.cue.values == 'R')[0])
        n_train = min(len(L) * (n_folds - 1) // n_folds, len(Rr) * (n_folds - 1) // n_folds)
        n_train = 2 * (n_train // 2)
        L2 = L.copy(); rng.shuffle(L2); Lt = np.array_split(L2, n_folds)
        R2 = Rr.copy(); rng.shuffle(R2); Rt = np.array_split(R2, n_folds)
        folds = []
        for f in range(n_folds):
            Ltr = rng.choice(np.setdiff1d(L, Lt[f]), n_train, replace=False)
            Rtr = rng.choice(np.setdiff1d(Rr, Rt[f]), n_train, replace=False)
            folds.append((np.sort(np.concatenate([Ltr, Rtr])), np.sort(np.concatenate([Lt[f], Rt[f]]))))
        return folds

    rows = []
    for n_folds, seed, label in runs:
        folds = make_folds(n_folds, seed)
        for f, (trn, tst) in enumerate(folds):
            a = correct[trn]
            n = len(trn)
            w_trial = np.where(a, (~a).sum() / n, a.sum() / n)  # correct trials weight n_incorrect / n
            for name, (lag, ctype) in models.items():
                st = stats_[lag]
                G = 0
                H = 0
                for j, i in enumerate(trn):
                    m = M(ctype, cond[i])
                    G = G + w_trial[j] * m.T @ st[i][0] @ m
                    H = H + w_trial[j] * m.T @ st[i][1]
                beta = np.linalg.lstsq(G, H, rcond=None)[0]
                sse = 0
                yy = 0
                sy = 0
                nn = 0
                for i in tst:
                    m = M(ctype, cond[i])
                    Gi = m.T @ st[i][0] @ m
                    Hi = m.T @ st[i][1]
                    sse = sse + st[i][2] - 2 * (beta * Hi).sum(0) + ((Gi @ beta) * beta).sum(0)
                    yy = yy + st[i][2]
                    sy = sy + st[i][3]
                    nn += st[i][4]
                sst = yy - sy ** 2 / nn
                with np.errstate(invalid='ignore', divide='ignore'):
                    r2 = 1 - sse / sst  # robust_stats.get_r2
                for u in range(ses.n_units):
                    rows.append((u, f, name, label, r2[u]))
    return pd.DataFrame(rows, columns=['unit', 'fold', 'model', 'run', 'r2'])


def lrt_models(full_formula, null_formula, df, vc, groups='subject'):
    """LRT by ML as paper_stats.py does; when the default optimizer leaves the
    full model below the null (a negative statistic, which means a fit did
    not reach its maximum), both models are refitted with Powell's method
    and the higher likelihood of each is kept. Returns (statistic, df, p,
    refitted)."""
    import warnings
    import statsmodels.formula.api as smf
    full = mixed(full_formula, df, vc, groups, reml=False)
    null = mixed(null_formula, df, vc, groups, reml=False)
    refit = False
    if 2 * (full.llf - null.llf) < 0:
        refit = True
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            f2 = smf.mixedlm(full_formula, df, groups=groups, re_formula='1', vc_formula=vc).fit(reml=False, method='powell')
            n2 = smf.mixedlm(null_formula, df, groups=groups, re_formula='1', vc_formula=vc).fit(reml=False, method='powell')
        full = f2 if f2.llf > full.llf else full
        null = n2 if n2.llf > null.llf else null
    v, d, p = lrt(full, null)
    return v, d, p, refit


# ----------------------------------------------------------------------------- open field

def of_params():
    """experiment_info.py, get_task_params for 'OF' (subjects Li, Ne, Cl, Ca, Al): 3 cm bins over
    x -63 to 63 cm and y -6 to 135 cm, speed bins of 2 cm/s from 2 to 80 cm/s, angle bins of 10
    degrees, spatial smoothing window 3 bins with sigma 2."""
    p = dict(cm_bin=3, x_cm_lims=(-63, 63), y_cm_lims=(-6, 135), min_speed_thr=2, max_speed_thr=80,
             speed_bin=2, rad_bin=np.deg2rad(10), spatial_window_size=3, spatial_sigma=2)
    p['x_bin_edges'] = np.arange(p['x_cm_lims'][0], p['x_cm_lims'][1] + p['cm_bin'], p['cm_bin'])
    p['y_bin_edges'] = np.arange(p['y_cm_lims'][0], p['y_cm_lims'][1] + p['cm_bin'], p['cm_bin'])
    p['sp_bin_edges'] = np.arange(p['min_speed_thr'], p['max_speed_thr'] + p['speed_bin'], p['speed_bin'])
    p['ang_bin_edges'] = np.arange(0, 2 * np.pi + p['rad_bin'], p['rad_bin'])
    return p


def _position_pca(p):
    """spatial_functions.py, generate_position_design_matrix and _pca_position_features: for
    each spatial bin a Gaussian bump (window 3 bins, sigma 2, peak 1) over the arena, reduced
    by PCA to 95% of the variance."""
    from sklearn.decomposition import PCA
    nx, ny = len(p['x_bin_edges']) - 1, len(p['y_bin_edges']) - 1
    w, s = p['spatial_window_size'], p['spatial_sigma']
    g = np.arange(-w, w + 1)
    xx, yy = np.meshgrid(g, g)
    gv = np.exp(-(xx ** 2 + yy ** 2) / (2 * s * s))
    gv = (gv / gv.max()).flatten()
    F = np.zeros((nx * ny, nx * ny))
    for jj in range(ny):
        for ii in range(nx):
            lin = np.ravel_multi_index((jj, ii), (ny, nx))
            mj, mi = np.meshgrid(np.arange(jj - w, jj + w + 1), np.arange(ii - w, ii + w + 1))
            ok = ((mj >= 0) & (mj < ny) & (mi >= 0) & (mi < nx)).flatten()
            idx = np.ravel_multi_index((mj, mi), (ny, nx), mode='clip').flatten()
            F[lin, idx[ok]] = gv[ok]
    pca = PCA(n_components=0.95, svd_solver='full').fit(F)
    return F, pca


def _rate_map(fr, x, y, p):
    """spatial_functions.py, firing_rate_2_rate_map with occ_num_thr 1 (AllSpatialEncodingModels)
    and smooth_2d_map without the median filter: mean rate per bin, Gaussian smoothing."""
    from scipy import ndimage
    s, _, _ = np.histogram2d(y, x, bins=[p['y_bin_edges'], p['x_bin_edges']], weights=fr)
    c, _, _ = np.histogram2d(y, x, bins=[p['y_bin_edges'], p['x_bin_edges']])
    m = np.zeros_like(s)
    k = c >= 1
    m[k] = s[k] / c[k]
    n_bins, sigma = p['spatial_window_size'], p['spatial_sigma']
    trunc = (((n_bins - 1) / 2) - 0.5) / sigma
    return ndimage.gaussian_filter(m, sigma, mode='constant', truncate=trunc)


def of_models(fr, track, p, pos_pca, secs_per_split=30.0, n_xval=5, smooth_secs=0.5):
    """open_field_functions.py, AllSpatialEncodingModels with the settings of
    experiment_info.py, get_of_encoding_models_scores2 (models 'sdp', responses z-scored with each
    fold's training mean and SD, 30 s blocks): data smoothed with a 0.5 s Hann window (x, y, speed
    and rates, not angles); 5 folds of blocks cycling through the session (robust_stats.py,
    split_timeseries); speed model on one-hot speed bins and head-direction model on one-hot
    10-degree bins, both by least squares without intercept on samples with speed 2 to 80 cm/s;
    position model by elastic net (alpha 0.15, l1_ratio 0.15, intercept) on the PCA position
    features; aggregate model by least squares with intercept on the three models' fold
    predictions (zero where speed is outside the limits). Returns, per unit, fold and model, the
    test R2 (robust_stats.get_r2) and r_p, the Pearson correlation of the smoothed rate maps of the
    response and the prediction on the test samples. track columns: x, y, hd, sp, ha (cm, rad,
    cm/s)."""
    import warnings
    from scipy import signal
    from sklearn.linear_model import ElasticNet
    F, pca = pos_pca
    n = fr.shape[1]
    spb = int(secs_per_split / TIME_STEP)
    if n < n_xval * spb:
        return None
    win = signal.get_window('hann', int(np.round(smooth_secs / TIME_STEP)), fftbins=False)
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')  # scipy warns on the FIR coefficients, as in the code
        sos = signal.tf2sos(win / win.sum(), 1)
    x = signal.sosfiltfilt(sos, track[:, 0])
    y = signal.sosfiltfilt(sos, track[:, 1])
    sp = signal.sosfiltfilt(sos, track[:, 3])
    hd = track[:, 2]
    Y = signal.sosfiltfilt(sos, np.nan_to_num(fr), axis=1)
    edges = np.append(np.arange(0, n, spb), n)
    fold = np.zeros(n, dtype=int)
    for i in range(len(edges) - 1):
        fold[edges[i]:edges[i + 1]] = i % n_xval

    def onehot(v, e):
        b = np.digitize(v, e) - 1
        X = np.zeros((len(v), len(e) - 1))
        ok = (b >= 0) & (b < len(e) - 1)
        X[np.where(ok)[0], b[ok]] = 1
        return X

    valid = (sp >= p['sp_bin_edges'][0]) & (sp <= p['sp_bin_edges'][-1])
    Xs = onehot(sp[valid], p['sp_bin_edges'])
    Xd = onehot(hd[valid], p['ang_bin_edges'])
    nx, ny = len(p['x_bin_edges']) - 1, len(p['y_bin_edges']) - 1
    xb = np.clip(np.digitize(x, p['x_bin_edges']) - 1, 0, nx - 1)
    yb = np.clip(np.digitize(y, p['y_bin_edges']) - 1, 0, ny - 1)
    Xp = pca.transform(F[np.ravel_multi_index((yb, xb), (ny, nx))])
    rows = []
    for f in range(n_xval):
        tr, te = fold != f, fold == f
        mu = np.nanmean(Y[:, tr], axis=1)
        sd = np.nanstd(Y[:, tr], axis=1)
        Z = (Y - mu[:, None]) / sd[:, None]
        trv, tev = tr[valid], te[valid]
        # speed and head-direction models z-score their own (valid speed) responses
        # (SpatialEncodingModelCrossVal.get_response_fold)
        Yv = Y[:, valid]
        muv = np.nanmean(Yv[:, trv], axis=1)
        sdv = np.nanstd(Yv[:, trv], axis=1)
        Zv = (Yv - muv[:, None]) / sdv[:, None]
        Zs = Z.copy()
        Zs[:, valid] = Zv
        pred = {}
        for name, X in [('speed', Xs), ('hd', Xd)]:
            b = np.linalg.lstsq(X[trv], Zv[:, trv].T, rcond=None)[0]
            full = np.zeros((n, Y.shape[0]))
            full[valid] = X @ b
            pred[name] = full
        # one elastic net per unit, fitted together (a two-dimensional target is fitted unit by unit)
        m = ElasticNet(alpha=0.15, l1_ratio=0.15, fit_intercept=True, precompute=True).fit(Xp[tr], Z[:, tr].T)
        pred['pos'] = m.predict(Xp).reshape(n, -1)
        Pa = np.zeros((n, Y.shape[0]))
        for u in range(Y.shape[0]):
            A = np.column_stack([pred['speed'][:, u], pred['hd'][:, u], pred['pos'][:, u], np.ones(n)])
            b = np.linalg.lstsq(A[tr], Z[u, tr], rcond=None)[0]
            Pa[:, u] = A @ b
        pred['agg_sdp'] = Pa
        for name in ['speed', 'hd', 'pos', 'agg_sdp']:
            samp = te & valid if name in ('speed', 'hd') else te
            yt = (Zs if name in ('speed', 'hd') else Z)[:, samp]
            yh = pred[name][samp].T
            with np.errstate(invalid='ignore', divide='ignore'):
                r2 = 1 - ((yt - yh) ** 2).sum(1) / ((yt - yt.mean(1, keepdims=True)) ** 2).sum(1)
            for u in range(Y.shape[0]):
                m1 = _rate_map(yt[u], x[samp], y[samp], p).ravel()
                m2 = _rate_map(yh[u], x[samp], y[samp], p).ravel()
                r = np.corrcoef(m1, m2)[0, 1] if m1.std() > 0 and m2.std() > 0 else np.nan
                rows.append((u, f, name, r2[u], r))
    return pd.DataFrame(rows, columns=['unit', 'fold', 'model', 'r2', 'map_r'])
