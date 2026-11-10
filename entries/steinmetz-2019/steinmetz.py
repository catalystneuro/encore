"""Loading and measures for Steinmetz et al. (2019), dandiset 000017.

Each parameter says where it comes from:
- "Methods" means the Methods of the paper (doi:10.1038/s41586-019-1787-x),
  section named; "claims" means claims/steinmetz-2019.yaml, definition named
  (T, N, M, R); "code" means github.com/nsteinme/steinmetz-et-al-2019 at commit
  9a0bea8, file named; "assumption" is a choice this attempt made, with the
  reason; "standard" is a choice that cannot change a result.

The files are streamed from the archive with remfile and h5py; nothing is
written to disk.
"""
import time

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient

DANDISET = "000017"
VERSION = "0.240329.1926"   # the only published version (notebook header)

BIN = 0.005                 # 5 ms bins (Methods, Data analysis; code kernelFitBasic.m)
STIM_WIN = (-0.3, 0.5)      # stimulus-aligned window kept (s); covers every window used
MOVE_WIN = (-0.3, 0.3)      # movement-aligned window kept (s)
# Definition T (claims; Methods, Training protocol).
GO_WIN = (0.125, 0.4)       # onset of a choice turn
NOMOVE_WIN = (-0.05, 0.4)   # no movement of any kind
MIN_TRIALS_TYPE = 12        # sessions need 12 Left, 12 Right and 12 NoGo trials
# Definition N (claims; Methods, Data analysis).
MIN_RATE = 0.1              # trial firing rate, stimulus onset to 0.4 s, Hz
MIN_PER_REGION = 13         # neurons of one region in one session
NONBRAIN = {"root", "void", "fiber tracts"}  # labels that are not brain regions (assumption:
# 'root' is the label for channels outside any annotated region)

# Extended Data Table 1 of the paper: region -> (recordings, mice, responsive, total neurons).
# Reference values the claims compare with (VISl and VISrl printed "VISI", "VISrI" in the text).
ED_TABLE1 = {
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
REGIONS42 = sorted(ED_TABLE1)
# Finer Allen CCF labels found in the files, mapped to the parent among the 42 regions
# (assumption: a unit labelled with a subdivision lies in the parent region; Allen CCF
# hierarchy). Labels not listed (TH, MB, CA, SSs, AUD, ...) stay outside the 42.
REGION_PARENT = {
    "SCig": "SCm", "SCiw": "SCm", "SCdg": "SCm", "SCdw": "SCm",
    "SCsg": "SCs", "SCop": "SCs", "SCzo": "SCs",
    "LSr": "LS", "LSc": "LS", "LSv": "LS",
    "ORBm": "ORB", "ORBl": "ORB", "ORBvl": "ORB",
    "TT": "OLF", "COA": "OLF", "PIR": "OLF", "DP": "OLF", "AON": "OLF", "NLOT": "OLF",
    "PAA": "OLF", "TR": "OLF", "MOB": "OLF", "AOB": "OLF",
}

# Supplementary Table 1: subject -> (sex, genotype).
SUPP_T1 = {
    "Cori": ("F", "tetO-G6s x CaMK-tTA"), "Forssmann": ("M", "C57BL/6J"),
    "Hench": ("M", "tetO-G6s x CaMK-tTA"), "Lederberg": ("F", "Vglut1-IRES2-Cre-D"),
    "Moniz": ("M", "RCL-GCaMP6f x VGlut-Cre"), "Muller": ("F", "RCL-GCaMP6f x VGlut-Cre"),
    "Radnitz": ("F", "Snap25-GCaMP6s"), "Richards": ("M", "C57BL/6J"),
    "Tatum": ("F", "Vglut1-IRES2-Cre-D"), "Theiler": ("F", "RCL-GCaMP6f x VGlut-Cre"),
}

# Supplementary Table 2: (subject, date, age in weeks, areas recorded).
SUPP_T2 = [
    ("Cori", "2016-12-14", 11, "ACA, CA3, DG, LS, MOs, SUB, VISp"),
    ("Cori", "2016-12-17", 12, "CA1, POST, VISl, VISpm"),
    ("Cori", "2016-12-18", 12, "CA1, DG, LP, MG, MRN, POST, VISam, VISp"),
    ("Radnitz", "2017-01-08", 20, "ACA, ILA, MOs, MRN, OLF, PL, RSP, SCm, SCs, VISp"),
    ("Radnitz", "2017-01-09", 20, "MOs, MRN, SCm, VISp"),
    ("Radnitz", "2017-01-10", 20, "ACA, ACB, CA1, DG, LD, LP, MOs, PL, PO, VISam"),
    ("Radnitz", "2017-01-11", 20, "APN, CA1, DG, LP, MRN, POL, RSP, SCm, SCs, VISpm"),
    ("Radnitz", "2017-01-12", 20, "CP, MOp, SSp"),
    ("Muller", "2017-01-07", 17, "ACA, ACB, MOs, MRN, OLF, PL, RSP, SCs, VISp"),
    ("Muller", "2017-01-08", 17, "CA1, DG, LP, MOs, PO, VISam"),
    ("Muller", "2017-01-09", 17, "CA1, MRN, RSP, SCm, SCs, VISpm, VISrl"),
    ("Moniz", "2017-05-15", 30, "APN, CA1, DG, LP, POL, SUB, VISam, VISpm"),
    ("Moniz", "2017-05-16", 30, "CA1, DG, LGd, LP, MG, SUB, VISa, VISp"),
    ("Moniz", "2017-05-18", 30, "LD, MOp, SSp"),
    ("Hench", "2017-06-15", 31, "CA1, CA3, DG, ILA, LD, LP, LS, MOs, OLF, PL, PO, SUB, VISa, VISp"),
    ("Hench", "2017-06-16", 32, "CA1, CA3, LD, LS, OLF, ORB, PL, VISam, VISl, VPL"),
    ("Hench", "2017-06-17", 32, "CA1, DG, GPe, MRN, POL, POST, SCm, SCs, VISl, VISp, VISrl"),
    ("Hench", "2017-06-18", 32, "CP, LS, MOp"),
    ("Theiler", "2017-10-11", 46, "ACA, CA1, DG, ILA, LP, MOs, PL, SUB, VISam, VISp"),
    ("Richards", "2017-10-29", 26, "ACA, CA1, DG, LP, LS, MD, MOs, PO, RSP, SUB, VISa, VPM"),
    ("Richards", "2017-10-30", 26, "CA3, MOs, OLF, ORB, POST, SCm, SNr"),
    ("Richards", "2017-10-31", 26, "MOs, MRN, OLF, ORB, PAG, RSP, SCm, SCs"),
    ("Richards", "2017-11-01", 26, "CA1, CA3, CP, LGd, SNr, VPM, ZI"),
    ("Richards", "2017-11-02", 26, "LP, OLF, PO, RT"),
    ("Forssmann", "2017-11-01", 26, "ACA, CA1, DG, LGd, LS, MOs, SUB, VISa, VISp, VPL"),
    ("Forssmann", "2017-11-02", 26, "ACA, CA1, DG, MOs, OLF, ORB, PL, SUB, VISa"),
    ("Forssmann", "2017-11-04", 27, "CA1, SSp"),
    ("Forssmann", "2017-11-05", 27, "CA3, CP, LD, OLF, SSp, VPL"),
    ("Lederberg", "2017-12-05", 15, "ACA, CA1, DG, LGd, MD, MOs, PL, SUB, VISam, VISp"),
    ("Lederberg", "2017-12-06", 15, "ACA, CA1, DG, LGd, MOs, MRN, PL, SCm, SCs, VISam, ZI"),
    ("Lederberg", "2017-12-07", 15, "CA1, MOs, MRN, ORB, PAG, RSP, SCm, SCs, VISp"),
    ("Lederberg", "2017-12-08", 15, "BLA, CA3, GPe, LGd, VPM, ZI"),
    ("Lederberg", "2017-12-09", 15, "CA3, LGd, SSp"),
    ("Lederberg", "2017-12-10", 15, "LD, RT, VPL, VPM"),
    ("Lederberg", "2017-12-11", 15, "ACB, CA3, CP, LGd, SNr, ZI"),
    ("Tatum", "2017-12-06", 15, "ACA, CA1, DG, LGd, LP, LS, MD, MOs, RSP, VISam"),
    ("Tatum", "2017-12-07", 15, "MOs, MRN, PL, SCm, SCs, VISam"),
    ("Tatum", "2017-12-08", 15, "MOs, ORB, PAG, RSP, SCm, SCs, VISam"),
    ("Tatum", "2017-12-09", 15, "BLA, CA3, GPe, LGd, SNr"),
]

# Region groups (claims, "Region groups", from code utils/brainRegionGroups.m and Methods).
VIS = ["VISp", "VISpm", "VISl", "VISrl", "VISa", "VISam"]
FRONTAL_JPECC = ["MOs", "MOp", "PL"]
MIDBRAIN_JPECC = ["MRN", "SCm", "SNr", "ZI"]
NEOCORTEX = ["ACA", "ILA", "MOp", "MOs", "ORB", "PL", "RSP", "SSp"] + VIS
VIS_THALAMUS = ["LGd", "LP", "LD"]
ED6B_MIDBRAIN = ["MRN", "SCm", "SCs", "APN", "PAG"]
ED6B_BASAL_GANGLIA = ["CP", "GPe", "SNr", "ACB", "LS"]
ED6B_HIPPOCAMPUS = ["POST", "SUB", "DG", "CA1", "CA3"]
VISUAL_PATHWAY = VIS + ["LGd", "LP", "LD", "SCs", "CP", "GPe", "SNr", "SCm", "MRN", "APN", "ZI"]


def asset_paths():
    """The NWB files of the pinned version, sorted by path."""
    ds = DandiAPIClient().get_dandiset(DANDISET, VERSION)
    return sorted((a.path, a.size) for a in ds.get_assets())


def open_nwb(path):
    """Stream one NWB file (h5py over remfile); nothing is written to disk."""
    ds = DandiAPIClient().get_dandiset(DANDISET, VERSION)
    url = ds.get_asset_by_path(path).get_content_url(follow_redirects=1, strip_query=True)
    return h5py.File(remfile.File(url), "r")


def _s(x):
    return x.decode() if isinstance(x, bytes) else str(x)


def file_metadata(f):
    """Subject, session and probe metadata, without reading any large array."""
    g = f["general"]
    E = g["extracellular_ephys/electrodes"]
    return dict(
        identifier=_s(f["identifier"][()]),
        subject=_s(g["subject/subject_id"][()]), sex=_s(g["subject/sex"][()]),
        genotype=_s(g["subject/genotype"][()]), age=_s(g["subject/age"][()]),
        start=_s(f["session_start_time"][()]),
        probes=len(np.unique(E["group_name"][:])), n_units=f["units/id"].shape[0],
        n_trials=f["intervals/trials/id"].shape[0],
        n_spikes=f["units/spike_times"].shape[0],
        wheel_samples=f["acquisition/wheel_position/data"].shape[0],
        wheel_rate_attr=float(f["acquisition/wheel_position/starting_time"].attrs["rate"]),
        wheel_conversion=float(f["acquisition/wheel_position/data"].attrs["conversion"]),
        lick_samples=f["acquisition/lickPiezo/data"].shape[0],
        lick_rate_attr=float(f["acquisition/lickPiezo/starting_time"].attrs["rate"]),
        me_samples=f["processing/behavior/BehavioralTimeSeries/face_motion_energy/data"].shape[0],
        me_rate_attr=float(f["processing/behavior/BehavioralTimeSeries/face_motion_energy/starting_time"].attrs["rate"]),
        moves_data=f["processing/behavior/BehavioralEpochs/wheel_moves/data"].shape[0],
        moves_timestamps=f["processing/behavior/BehavioralEpochs/wheel_moves/timestamps"].shape[0],
        last_spike=float(f["units/spike_times"][-1]),
    )


def counts_aligned(spike_times, spike_index, units, events, lo, hi, bin_size=BIN):
    """Spike counts per unit, event and bin: array (units, events, bins), uint8.

    Bins of `bin_size` from `lo` to `hi` around each event. Events that are NaN
    give zero counts.
    """
    nb = int(round((hi - lo) / bin_size))
    edges = events[:, None] + lo + bin_size * np.arange(nb + 1)[None, :]
    bad = ~np.isfinite(events)
    edges[bad] = 0.0
    out = np.zeros((len(units), len(events), nb), dtype=np.uint8)
    for k, u in enumerate(units):
        a = spike_index[u - 1] if u > 0 else 0
        b = spike_index[u]
        st = spike_times[a:b]
        c = np.diff(np.searchsorted(st, edges.ravel()).reshape(edges.shape), axis=1)
        c[bad] = 0
        out[k] = np.minimum(c, 255)
    return out


def classify_trials(tr, mv_on, mv_off, mv_type):
    """Definition T (claims; Methods, Training protocol).

    For each trial the first wheel movement whose interval overlaps the window
    -0.05 to 0.4 s from stimulus onset. Left or Right: that movement is a turn
    the dataset types as Left (1) or Right (2), i.e. of the amplitude that
    registers a choice (wheel_moves comments), with onset 0.125 to 0.4 s.
    NoGo: no movement overlaps -0.05 to 0.4 s. Otherwise excluded. Then
    disengaged trials (the dataset's `included` column, checked against the
    Methods rule in the notebook) are dropped.

    The code rule (code findMoveTimes.m, kernelFitBasic.m: first onset after
    stimulus minus 0.1 s and before feedback) is returned as a variant column.
    """
    stim = tr["stim"].to_numpy()
    fb = tr["fb_time"].to_numpy()
    n = len(stim)
    tchoice = np.array(["X"] * n, dtype=object)
    first_on = np.full(n, np.nan)
    first_type = np.full(n, -1)
    any_on = np.full(n, np.nan)       # first onset of any movement after stimulus onset
    code_choice = np.array(["X"] * n, dtype=object)
    for i in range(n):
        s = stim[i]
        ov = np.where((mv_off >= s + NOMOVE_WIN[0]) & (mv_on <= s + NOMOVE_WIN[1]))[0]
        if len(ov) == 0:
            tchoice[i] = "N"
        else:
            j = ov[0]
            first_on[i] = mv_on[j] - s
            first_type[i] = mv_type[j]
            if GO_WIN[0] <= mv_on[j] - s <= GO_WIN[1] and mv_type[j] in (1, 2):
                tchoice[i] = "L" if mv_type[j] == 1 else "R"
        k = np.searchsorted(mv_on, s)
        if k < len(mv_on):
            any_on[i] = mv_on[k] - s
        # code variant
        k = np.searchsorted(mv_on, s - 0.1, side="right")
        if k < len(mv_on) and mv_on[k] < fb[i]:
            ft = mv_on[k] - s
            if (ft < NOMOVE_WIN[0]) or (ft > NOMOVE_WIN[1]):
                code_choice[i] = "N"
            elif GO_WIN[0] < ft < GO_WIN[1] and mv_type[k] in (1, 2):
                code_choice[i] = "L" if mv_type[k] == 1 else "R"
    tr = tr.copy()
    tr["first_move"] = first_on
    tr["first_type"] = first_type
    tr["any_onset"] = any_on
    tr["t_raw"] = tchoice
    tr["t_choice"] = np.where(tr["included"].to_numpy(), tchoice, "X")
    tr["code_choice"] = np.where(tr["included"].to_numpy(), code_choice, "X")
    return tr


def disengaged_rule(tr):
    """Methods rule for disengaged trials: a Miss (stimulus present, NoGo response)
    preceded by two or more Misses, and the run of NoGo responses at the end."""
    resp = tr["choice"].to_numpy()
    stim_present = (tr["cl"].to_numpy() > 0) | (tr["cr"].to_numpy() > 0)
    miss = stim_present & (resp == 0)
    dis = np.zeros(len(resp), bool)
    for i in range(2, len(resp)):
        if miss[i] and miss[i - 1] and miss[i - 2]:
            dis[i] = True
    i = len(resp) - 1
    while i >= 0 and resp[i] == 0:
        dis[i] = True
        i -= 1
    return ~dis


class Session:
    """One session: trials, wheel movements, passive events and binned spikes."""

    def __init__(self, path, rng, bins=True):
        t0 = time.time()
        self.path = path
        f = open_nwb(path)
        self.meta = file_metadata(f)
        self.name = self.meta["identifier"]
        self.subject = self.meta["subject"]
        T = f["intervals/trials"]
        tr = pd.DataFrame(dict(
            start=T["start_time"][:], stim=T["visual_stimulus_time"][:],
            gocue=T["go_cue"][:], resp_time=T["response_time"][:],
            fb_time=T["feedback_time"][:], fb_type=T["feedback_type"][:],
            choice=T["response_choice"][:], cl=T["visual_stimulus_left_contrast"][:],
            cr=T["visual_stimulus_right_contrast"][:], included=T["included"][:].astype(bool),
            rep_num=T["rep_num"][:]))
        # Wheel. The 'rate' attribute holds the sampling interval (checked in the notebook).
        W = f["acquisition/wheel_position"]
        self.wheel = W["data"][:].astype(np.float32)          # encoder units
        self.wheel_mm = float(W["data"].attrs["conversion"])  # mm per unit
        self.wheel_t0 = float(W["starting_time"][()])
        self.wheel_dt = float(W["starting_time"].attrs["rate"])
        M = f["processing/behavior/BehavioralEpochs/wheel_moves"]
        ts = M["timestamps"][:]
        self.mv_on, self.mv_off = ts[0::2], ts[1::2]
        self.mv_type = M["data"][:]
        self.trials = classify_trials(tr, self.mv_on, self.mv_off, self.mv_type)
        self.trials["rule_included"] = disengaged_rule(self.trials)
        # Passive replay.
        P = f["stimulus/presentation"]
        self.passive_vis = pd.DataFrame(dict(
            t=P["passive_left_contrast/timestamps"][:], pl=P["passive_left_contrast/data"][:],
            pr=P["passive_right_contrast/data"][:],
            t_right=P["passive_right_contrast/timestamps"][:]))
        ev = [("visual", self.passive_vis["t"].to_numpy())]
        for k, nm in [("passive_beeps", "beep"), ("passive_click_times", "click"),
                      ("passive_white_noise", "noise")]:
            ev.append((nm, P[k + "/timestamps"][:]))
        self.passive_all = pd.DataFrame(
            [(nm, t) for nm, tt in ev for t in tt], columns=["kind", "t"]).sort_values("t")
        # Pupil and face motion energy.
        self.eye_t = f["processing/behavior/PupilTracking/eye_area/timestamps"][:]
        self.eye = f["processing/behavior/PupilTracking/eye_area/data"][:]
        ME = f["processing/behavior/BehavioralTimeSeries/face_motion_energy"]
        self.me = ME["data"][:]
        self.me_t0 = float(ME["starting_time"][()])
        self.me_dt = float(ME["starting_time"].attrs["rate"])
        # Units: region from the peak channel. peak_channel is 1-based (checked in the
        # notebook against cluster depths and site positions).
        U = f["units"]
        E = f["general/extracellular_ephys/electrodes"]
        loc = E["location"][:].astype(str)
        peak = U["peak_channel"][:, 0].astype(int) - 1
        y = E["site_position"][:, 1]
        dep = U["cluster_depths"][:, 0]
        for off in (0, 1):
            ii = np.clip(peak + off, 0, len(y) - 1)
            self.meta[f"depth_err_{off}"] = float(np.median(np.abs(y[ii] - dep)))
        self.units = pd.DataFrame(dict(
            phy=U["phy_annotations"][:], region=loc[peak],
            depth=U["cluster_depths"][:, 0],
            probe=E["group_name"][:].astype(str)[peak]))
        self.read_s = None
        if bins:
            st = U["spike_times"][:]
            si = U["spike_times_index"][:]
            amps = U["spike_amps"][:, 0]
            good = np.where(self.units["phy"].to_numpy() >= 2)[0]
            self.good = good
            self.units["n_spikes"] = np.diff(np.concatenate([[0], si]))
            self.units["amp"] = [np.mean(amps[(si[u - 1] if u else 0):si[u]]) if
                                 self.units["n_spikes"][u] else np.nan
                                 for u in range(len(si))]
            dur = st.max() - st.min() if len(st) else np.nan
            self.units["rate_all"] = self.units["n_spikes"] / dur
            del amps
            # Mean waveform amplitude (claims suppfig2 criterion, "the mean spike waveform
            # amplitude"): peak-to-trough of the unit's `waveform_mean` on the channel where it
            # is largest. The file gives no unit for either amplitude.
            wf = U["waveform_mean"]
            wamp = np.full(len(si), np.nan)
            for a in range(0, len(si), 200):
                w = wf[a:a + 200]
                wamp[a:a + 200] = (w.max(axis=1) - w.min(axis=1)).max(axis=1)
            self.units["wf_amp"] = wamp
            trs = self.trials
            self.stim_counts = counts_aligned(st, si, good, trs["stim"].to_numpy(), *STIM_WIN)
            # Movement time: Left/Right onset; for NoGo trials a time drawn at random from
            # the Left/Right trials' times (claims definition T; code findMoveTimes.m).
            go = trs["t_choice"].isin(["L", "R"]).to_numpy()
            mt = np.where(go, trs["first_move"].to_numpy(), np.nan)
            nogo = (trs["t_choice"] == "N").to_numpy()
            if go.sum():
                mt[nogo] = rng.choice(mt[go], nogo.sum())
            self.trials["move_time"] = mt
            self.move_counts = counts_aligned(st, si, good, trs["stim"].to_numpy() + mt, *MOVE_WIN)
            self.rew_counts = counts_aligned(st, si, good, trs["fb_time"].to_numpy(), 0.0, 0.15)
            self.pas_counts = counts_aligned(st, si, good, self.passive_all["t"].to_numpy(), *STIM_WIN)
            del st, si
        self.read_s = time.time() - t0
        f.close()

    # --- wheel ---------------------------------------------------------------
    def wheel_at(self, t):
        """Wheel position (encoder units) at times t, nearest sample."""
        t = np.asarray(t, float)
        i = np.round(np.nan_to_num((t - self.wheel_t0) / self.wheel_dt)).astype(int)
        out = self.wheel[np.clip(i, 0, len(self.wheel) - 1)].astype(float)
        out[~np.isfinite(t)] = np.nan
        return out

    def moving_in(self, t, lo, hi):
        """True where a detected movement overlaps [t+lo, t+hi] (onset or in progress)."""
        t = np.asarray(t)
        return np.array([np.any((self.mv_off >= x + lo) & (self.mv_on <= x + hi)) for x in t])

    def pupil_mean(self, t, lo, hi):
        """Mean pupil area in [t+lo, t+hi] for each t."""
        return np.array([np.nanmean(self.eye[(self.eye_t >= x + lo) & (self.eye_t < x + hi)])
                         if np.any((self.eye_t >= x + lo) & (self.eye_t < x + hi)) else np.nan
                         for x in t])

    def me_mean(self, t, lo, hi):
        tt = self.me_t0 + self.me_dt * np.arange(len(self.me))
        return np.array([np.nanmean(self.me[(tt >= x + lo) & (tt < x + hi)]) for x in t])


def window_rate(counts, win_lo, win_hi, lo):
    """Mean rate (Hz) per unit and event over bins in [win_lo, win_hi) of an array
    whose first bin starts at `lo`."""
    a = int(round((win_lo - lo) / BIN))
    b = int(round((win_hi - lo) / BIN))
    return counts[:, :, a:b].sum(axis=2) / ((b - a) * BIN)


def half_gauss_kernel(sd, bin_size=BIN):
    """Causal half-Gaussian smoothing kernel (Methods, Data analysis)."""
    x = np.arange(0, int(np.ceil(5 * sd / bin_size)) + 1) * bin_size
    k = np.exp(-x ** 2 / (2 * sd ** 2))
    return k / k.sum()


def causal_smooth(x, sd, axis=-1, bin_size=BIN):
    k = half_gauss_kernel(sd, bin_size)
    x = np.moveaxis(np.asarray(x, float), axis, -1)
    out = np.zeros_like(x)
    for j, w in enumerate(k):
        if j == 0:
            out += w * x
        else:
            out[..., j:] += w * x[..., :-j]
    return np.moveaxis(out, -1, axis)


def matched_contrast(groups, levels=(0.25, 0.5, 1.0), rng=None):
    """Definition M (claims; Methods, Training protocol): for each contrast level,
    draw from each group as many trials as the smallest group has.

    groups: list of (indices, contrasts) pairs. Returns list of index arrays.
    """
    out = [[] for _ in groups]
    for c in levels:
        sets = [idx[np.isclose(con, c)] for idx, con in groups]
        n = min(len(s) for s in sets)
        for k, s in enumerate(sets):
            if n:
                out[k].extend(rng.choice(s, n, replace=False))
    return [np.array(sorted(o), int) for o in out]


def combined_cp(rates, labels, conds, n_shuffle, rng):
    """Combined-conditions choice or detect probability (Methods, ccCP; code
    ccCP/choiceProbShuf.m) for every unit at once.

    rates: (trials, units); labels: bool (trials,), True for the first group;
    conds: condition code per trial. Only conditions with both labels
    contribute. Returns (cp, fraction of shuffles below cp) per unit; ties count
    one half (Mann-Whitney U through mid-ranks).
    """
    from scipy.stats import rankdata
    use = np.zeros(len(labels), bool)
    for c in np.unique(conds):
        m = conds == c
        if labels[m].any() and (~labels[m]).any():
            use |= m
    rates, labels, conds = rates[use], labels[use], conds[use]
    if len(labels) == 0:
        return None
    ranks = np.zeros_like(rates, dtype=float)
    denom = 0.0
    offset = 0.0
    groups = []
    for c in np.unique(conds):
        m = np.where(conds == c)[0]
        ranks[m] = rankdata(rates[m], axis=0)
        n1 = labels[m].sum()
        n0 = len(m) - n1
        denom += n1 * n0
        offset += n1 * (n1 + 1) / 2
        groups.append(m)
    cp = (labels.astype(float) @ ranks - offset) / denom
    perms = np.zeros((n_shuffle, len(labels)))
    for s in range(n_shuffle):
        lab = labels.copy()
        for m in groups:
            lab[m] = rng.permutation(lab[m])
        perms[s] = lab
    null = (perms @ ranks - offset) / denom
    frac_below = (null < cp[None, :]).mean(axis=0) + 0.5 * (null == cp[None, :]).mean(axis=0)
    return cp, frac_below, int(use.sum())


# ---------------------------------------------------------------------------
# Per-session measures. One pass over each file; the notebook aggregates them.
# ---------------------------------------------------------------------------
PRE_WINS = {"a": (-0.2, 0.0), "b": (-0.25, -0.05)}   # claims ed6b readings (a), (b)
VEL_OFFSETS = np.round(np.arange(-0.1, 0.1001, 0.01), 3)  # times around movement onset (s)


def six_tests(S, tr):
    """The six responsiveness tests (Methods, Data analysis; code kernelFitBasic.m).

    Rates are spike counts in the window divided by its length, on trials T.
    Returns p (units, 6), signed effect (units, 6), trial rate, baseline rate.
    Direction of effect as the code's effectSizes: positive minus negative paired
    differences (tests 1, 2, 3, 5); rank sum minus its null (tests 4, 6; for test 4
    positive means Right greater).
    """
    from scipy.stats import wilcoxon, mannwhitneyu, rankdata
    inc = np.where(tr["t_choice"].isin(["L", "R", "N"]).to_numpy())[0]
    go = np.where(tr["t_choice"].isin(["L", "R"]).to_numpy())[0]
    lft = tr["t_choice"].to_numpy() == "L"
    rgt = tr["t_choice"].to_numpy() == "R"
    rew = np.where(((tr["t_choice"] == "N") & (tr["cl"] == 0) & (tr["cr"] == 0)
                    & (tr["fb_type"] == 1) & (tr["choice"] == 0)).to_numpy())[0]
    C, Mv = S.stim_counts, S.move_counts
    lo, mlo = STIM_WIN[0], MOVE_WIN[0]
    trial = window_rate(C[:, inc], 0.0, 0.4, lo)
    bsl = window_rate(C[:, inc], -0.2, 0.0, lo)
    stim = window_rate(C[:, inc], 0.05, 0.15, lo)
    bsl_go = window_rate(C[:, go], -0.2, 0.0, lo)
    pre = window_rate(Mv[:, go], -0.1, 0.05, mlo)
    peri = window_rate(Mv[:, go], -0.05, 0.2, mlo)
    rewr = S.rew_counts[:, rew].sum(axis=2) / 0.15
    nu = C.shape[0]
    p = np.full((nu, 6), np.nan)
    e = np.full((nu, 6), np.nan)
    for q in range(nu):
        for k, (x, y) in {0: (trial[q], bsl[q]), 1: (stim[q], bsl[q]), 2: (pre[q], bsl_go[q]),
                          4: (peri[q], bsl_go[q])}.items():
            d = x - y
            if np.any(d != 0):
                p[q, k] = wilcoxon(d, zero_method="wilcox").pvalue
            e[q, k] = np.sum(d > 0) - np.sum(d < 0)
        a, b = pre[q][rgt[go]], pre[q][lft[go]]
        if len(a) and len(b):
            if np.ptp(np.concatenate([a, b])) > 0:
                p[q, 3] = mannwhitneyu(a, b, alternative="two-sided").pvalue
            r = rankdata(np.concatenate([a, b]))[:len(a)].sum()
            e[q, 3] = r - len(a) * (len(a) + len(b) + 1) / 2
        if len(rew):
            a, b = rewr[q], bsl[q]
            if np.ptp(np.concatenate([a, b])) > 0:
                p[q, 5] = mannwhitneyu(a, b, alternative="two-sided").pvalue
            r = rankdata(np.concatenate([a, b]))[:len(a)].sum()
            e[q, 5] = r - len(a) * (len(a) + len(b) + 1) / 2
    return p, e, trial.mean(axis=1), bsl.mean(axis=1)


def sliding_responsive(S, tr):
    """Display selection of Methods, Data analysis (claims fig2de reading a): ranksum
    p < 0.0001 in at least three consecutive 0.1 s windows stepped by 0.005 s,
    between task trials with stimuli and movements and those without both. The
    windows run from stimulus onset to 0.4 s (window starts 0 to 0.3 s; assumption,
    the analysis window of the paper)."""
    from scipy.stats import mannwhitneyu
    tc = tr["t_choice"].to_numpy()
    stim = ((tr["cl"] > 0) | (tr["cr"] > 0)).to_numpy()
    a = np.where(stim & np.isin(tc, ["L", "R"]))[0]
    b = np.where(~stim & (tc == "N"))[0]
    C = S.stim_counts
    nu = C.shape[0]
    if len(a) < 2 or len(b) < 2:
        return np.zeros(nu, bool)
    starts = np.arange(0.0, 0.3001, 0.005)
    sig = np.zeros((nu, len(starts)), bool)
    for j, s in enumerate(starts):
        ra = window_rate(C[:, a], s, s + 0.1, STIM_WIN[0])
        rb = window_rate(C[:, b], s, s + 0.1, STIM_WIN[0])
        pv = mannwhitneyu(ra, rb, axis=1, alternative="two-sided").pvalue
        sig[:, j] = np.nan_to_num(pv, nan=1.0) < 1e-4
    run = sig[:, 2:] & sig[:, 1:-1] & sig[:, :-2]
    return run.any(axis=1)


def norm_trace(S, idx, base):
    """Normalized rate of Methods, Data analysis: 5 ms bins, causal half-Gaussian
    0.02 s, trial mean, causal half-Gaussian 0.03 s, minus baseline, divided by
    baseline + 0.5 sp/s. `base` is each unit's baseline (-0.02 to 0 s, all task
    trials). Smoothing is linear, so it is applied to the trial mean."""
    if len(idx) == 0:
        return None
    m = S.stim_counts[:, idx].mean(axis=1) / BIN
    m = causal_smooth(causal_smooth(m, 0.02), 0.03)
    return ((m - base[:, None]) / (base[:, None] + 0.5)).astype(np.float32)


def zscores(counts, idx, lo):
    """Definition R (claims; Methods, Data analysis): mean rate 0 to 0.25 s over the
    trials against the trial baselines -0.1 to 0 s. Z1 uses the s.e. of the
    baseline mean, Z2 the s.d. of the trial baselines."""
    if len(idx) < 2:
        return None, None
    post = window_rate(counts[:, idx], 0.0, 0.25, lo).mean(axis=1)
    b = window_rate(counts[:, idx], -0.1, 0.0, lo)
    sd = b.std(axis=1, ddof=1)
    with np.errstate(divide="ignore", invalid="ignore"):
        z2 = (post - b.mean(axis=1)) / sd
        z1 = z2 * np.sqrt(len(idx))
    return z1, z2


# ---------------------------------------------------------------------------
# Kernel regression, full model (claims definition K; Methods, Kernel regression; code
# kernelFitBasic.m, regFullPipeline.m). Used for fig3c-variance-explained only.
# ---------------------------------------------------------------------------
K_VIS_LAGS = 90        # -0.05 to 0.4 s from stimulus onset in 5 ms bins (claims K)
K_MOVE_LAGS = 55       # -0.25 to 0.025 s from movement onset (claims K)
K_SMOOTH = 0.025       # causal half-Gaussian s.d. (claims K)
K_CONTRASTS = (0.25, 0.5, 1.0)


def kernel_inputs(S, tr):
    """Design and responses of the full kernel model for one session (claims K).

    Trials T. Samples from 0.05 s before stimulus onset to the earlier of 0.4 s after
    it and 0.025 s after movement onset (code). Predictors: six Vision kernels (left,
    right x low, medium, high contrast; 90 lags from -0.05 s), an Action kernel and a
    Choice kernel (+1 Left, -1 Right; code) at Left or Right movement onset (55 lags
    from -0.25 s). Responses: spike counts in 5 ms bins smoothed with a causal
    half-Gaussian of s.d. 25 ms, as rates, minus each unit's mean rate -0.2 to 0 s
    before stimulus onset over trials T (code). Returns the design as a sparse matrix
    (samples, 650), the responses (samples, units) as float32, the trial of each
    sample and the evaluation mask: samples from stimulus onset to the earlier of
    movement onset and 0.4 s (code)."""
    from scipy import sparse
    tc = tr["t_choice"].to_numpy()
    inc = np.where(np.isin(tc, ["L", "R", "N"]))[0]
    nb = S.stim_counts.shape[2]
    t_bins = STIM_WIN[0] + BIN * np.arange(nb)
    rate = causal_smooth(S.stim_counts[:, inc].astype(np.float32) / BIN, K_SMOOTH)
    base = rate[:, :, (t_bins >= -0.2) & (t_bins < 0)].mean(axis=(1, 2))
    rows, cols, vals, Ys, tid, ev = [], [], [], [], [], []
    n0 = 0
    nv = 6 * K_VIS_LAGS
    for j, i in enumerate(inc):
        mt = tr["first_move"].iloc[i] if tc[i] in ("L", "R") else np.nan
        t_end = min(0.4, mt + 0.025) if np.isfinite(mt) else 0.4
        samp = np.where((t_bins >= -0.05 - 1e-9) & (t_bins < t_end - 1e-9))[0]
        ts = t_bins[samp]
        lag_v = np.round((ts + 0.05) / BIN).astype(int)
        for side, c in [(0, tr["cl"].iloc[i]), (1, tr["cr"].iloc[i])]:
            if c > 0:
                k = side * 3 + K_CONTRASTS.index(min(K_CONTRASTS, key=lambda x: abs(x - c)))
                ok = (lag_v >= 0) & (lag_v < K_VIS_LAGS)
                rows.append(n0 + np.where(ok)[0]); cols.append(k * K_VIS_LAGS + lag_v[ok]); vals.append(np.ones(ok.sum()))
        if np.isfinite(mt):
            lag_m = np.round((ts - mt + 0.25) / BIN).astype(int)
            ok = (lag_m >= 0) & (lag_m < K_MOVE_LAGS)
            r_ = n0 + np.where(ok)[0]
            rows += [r_, r_]
            cols += [nv + lag_m[ok], nv + K_MOVE_LAGS + lag_m[ok]]
            vals += [np.ones(ok.sum()), np.full(ok.sum(), 1.0 if tc[i] == "L" else -1.0)]
        Ys.append(rate[:, j, samp].T - base[None, :])
        tid.append(np.full(len(samp), j))
        ev.append((ts >= -1e-9) & (ts < (min(mt, 0.4) if np.isfinite(mt) else 0.4) - 1e-9))
        n0 += len(samp)
    X = sparse.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))),
                          shape=(n0, nv + 2 * K_MOVE_LAGS), dtype=np.float32)
    return dict(X=X, Y=np.vstack(Ys).astype(np.float32), trial=np.concatenate(tid),
                eval=np.concatenate(ev))


def enet_paths(G, c, lam, alpha, kmax, tol=1e-5, max_iter=500, kmin=1):
    """Elastic net (glmnet objective: 1/2 mean squared error + lam * (alpha |b|_1 +
    (1 - alpha) / 2 |b|^2), on standardized predictors) by coordinate descent on the Gram
    matrix, for the first k = 1..kmax predictors, for many responses at once.

    G: (p, p) Gram matrix of the standardized training predictors over n (so diag 1);
    c: (p, m) their products with the centred responses over n. Returns a list of
    coefficient arrays (k, m), one per k; each k starts from the solution for k - 1."""
    m = c.shape[1]
    out = []
    b = np.zeros((kmin - 1, m))
    l1, l2 = lam * alpha, lam * (1 - alpha)
    for k in range(kmin, kmax + 1):
        b = np.vstack([b, np.zeros((1, m))])
        Gk = G[:k, :k]
        for _ in range(max_iter):
            delta = 0.0
            for j in range(k):
                r = c[j] - Gk[j] @ b + Gk[j, j] * b[j]
                new = np.sign(r) * np.maximum(np.abs(r) - l1, 0) / (Gk[j, j] + l2)
                delta = max(delta, float(np.max(np.abs(new - b[j]))))
                b[j] = new
            if delta < tol:
                break
        out.append(b.copy())
    return out


def full_model_ve(Z, Y, trial, ev, rng, lam=0.5, alpha=0.5, kmax=50, kfold=5):
    """Cross-validated variance explained of the full model (claims K): elastic net with
    alpha 0.5 and lambda 0.5 fixed (Methods; glmnet defaults, predictors standardized on
    the training trials), 5-fold cross-validation over trials, 1 to `kmax` reduced-rank
    components, VE over the evaluation samples of the test trials pooled over folds,
    the best k kept. Z: (samples, components) of one session; Y: (samples, units).
    Returns (best VE per unit, its k)."""
    kmax = min(kmax, Z.shape[1])
    ut = np.unique(trial)
    folds = np.array_split(rng.permutation(ut), kfold)
    sse = np.zeros((kmax, Y.shape[1]))
    for f in folds:
        te = np.isin(trial, f)
        trn = ~te
        mu, sd = Z[trn].mean(axis=0), Z[trn].std(axis=0)
        sd[sd == 0] = 1.0
        Zs = (Z[trn] - mu) / sd
        ym = Y[trn].mean(axis=0)
        n = trn.sum()
        G = Zs[:, :kmax].T @ Zs[:, :kmax] / n
        c = Zs[:, :kmax].T @ (Y[trn] - ym) / n
        B = enet_paths(G, c, lam, alpha, kmax)
        m = te & ev
        Zte = (Z[m, :kmax] - mu[:kmax]) / sd[:kmax]
        for k in range(kmax):
            pred = ym + Zte[:, :k + 1] @ B[k]
            sse[k] += ((Y[m] - pred) ** 2).sum(axis=0)
    ye = Y[ev]
    sst = ((ye - ye.mean(axis=0)) ** 2).sum(axis=0)
    with np.errstate(divide="ignore", invalid="ignore"):
        ve = 1 - sse / sst
    return ve.max(axis=0), ve.argmax(axis=0) + 1


def pooled_basis(Xs, Ys, nkeep):
    """Reduced-rank basis over all sessions, as code reducedRankRegression/CanonCor2all.m
    (github.com/nsteinme/steinmetz-et-al-2019 at 9a0bea8): CXX the covariance of the designs
    of all sessions stacked, plus 1e-7 I; CYX each session's covariance of its responses
    with its design (each centred within session, divided by n_i - 1), sessions side by
    side; the SVD of CYX CXX^(-1/2) = d s c' gives the basis b = CXX^(-1/2) c, of which the
    first `nkeep` columns are returned. Xs: designs (sparse or dense), Ys: responses."""
    N = sum(X.shape[0] for X in Xs)
    p = Xs[0].shape[1]
    sx = sum(np.asarray(X.sum(axis=0)).ravel() for X in Xs)
    sxx = sum(np.asarray((X.T @ X).todense() if hasattr(X, "todense") else X.T @ X, float) for X in Xs)
    mu = sx / N
    CXX = (sxx - N * np.outer(mu, mu)) / (N - 1) + 1e-7 * np.eye(p)
    w, v = np.linalg.eigh(CXX)
    CXXMH = (v / np.sqrt(w)) @ v.T
    blocks = []
    for X, Y in zip(Xs, Ys):
        n = X.shape[0]
        Yc = np.asarray(Y, float) - np.asarray(Y, float).mean(axis=0)
        blocks.append(np.asarray(X.T @ Yc) / (n - 1))       # X' Yc = Xc' Yc since Yc has zero mean
    CXY = np.hstack(blocks)
    c = np.linalg.svd(CXXMH @ CXY, full_matrices=False)[0]   # = right singular vectors of CYX CXXMH
    return CXXMH @ c[:, :nkeep]


def project(X, W):
    """Components of a design: (X - its mean over samples) @ W, for sparse or dense X."""
    mu = np.asarray(X.mean(axis=0)).ravel()
    return np.asarray(X @ W) - mu @ W


def enet_predict_all(Z, Y, k, lam=0.5, alpha=0.5):
    """Elastic net with the first k components fitted on all samples (no cross-validation);
    returns the predictions (claims K: "each neuron fit with 75 components on all its data")."""
    k = min(k, Z.shape[1])
    mu, sd = Z[:, :k].mean(axis=0), Z[:, :k].std(axis=0)
    sd[sd == 0] = 1.0
    Zs = (Z[:, :k] - mu) / sd
    ym = Y.mean(axis=0)
    n = len(Z)
    B = enet_paths(Zs.T @ Zs / n, Zs.T @ (Y - ym) / n, lam, alpha, k, kmin=k)[-1]
    return ym + Zs @ B


def nested_eval_mask(trial, tc, mt):
    """Evaluation samples of the nested tests (code evalWins): 0.05 to 0.4 s after stimulus
    onset, ending at movement onset, and -0.2 to 0 s from movement onset. `trial` indexes
    the trials T of the session; tc, mt their choice and movement time."""
    first = np.r_[0, np.where(np.diff(trial) != 0)[0] + 1]
    pos = np.arange(len(trial)) - np.repeat(first, np.diff(np.r_[first, len(trial)]))
    t = -0.05 + BIN * pos
    m = mt[trial]
    end = np.where(np.isfinite(m), np.minimum(m, 0.4), 0.4)
    stim_w = (t >= 0.05 - 1e-9) & (t < end - 1e-9)
    move_w = np.isfinite(m) & (t - m >= -0.2 - 1e-9) & (t - m <= 1e-9)
    return stim_w | move_w


def summarize(S, seed):
    """All per-session measures used by the notebook. `seed` gives one generator
    per use, so that random draws in one claim do not change another."""
    rng = {k: np.random.default_rng([seed, i]) for i, k in
           enumerate(["M", "Msingle", "cp", "dp_pre", "eng", "misc", "eq", "cp_lr"])}
    tr = S.trials.copy()
    tr["session"] = S.name
    tr["subject"] = S.subject
    tc = tr["t_choice"].to_numpy()
    out = {"meta": dict(S.meta, name=S.name, read_s=S.read_s)}
    # --- behaviour ---------------------------------------------------------
    stimt = tr["stim"].to_numpy()
    tr["disp_resp"] = S.wheel_at(tr["resp_time"]) - S.wheel_at(stimt)
    go = np.isin(tc, ["L", "R"])
    mabs = stimt + tr["first_move"].to_numpy()
    for o in VEL_OFFSETS:
        v = S.wheel_at(mabs + o) - S.wheel_at(mabs + o - 0.01)
        tr[f"vel_{o:+.2f}"] = np.where(go, v, np.nan)
    # First movement after stimulus onset of any kind, and first typed (choice) turn:
    # onset, type and direction (sign of the wheel displacement over the movement).
    k = np.searchsorted(S.mv_on, stimt)
    ok = k < len(S.mv_on)
    kk = np.minimum(k, len(S.mv_on) - 1)
    tr["any_type"] = np.where(ok, S.mv_type[kk], -1)
    tr["any_dir"] = np.where(ok, np.sign(S.wheel_at(S.mv_off[kk]) - S.wheel_at(S.mv_on[kk])), 0)
    typed = np.where(S.mv_type > 0)[0]
    j = np.searchsorted(S.mv_on[typed], stimt)
    okj = j < len(typed)
    jj = typed[np.minimum(j, len(typed) - 1)]
    tr["typed_onset"] = np.where(okj, S.mv_on[jj] - stimt, np.nan)
    tr["typed_type"] = np.where(okj, S.mv_type[jj], -1)
    tr["iti"] = np.concatenate([[np.nan], stimt[1:] - tr["fb_time"].to_numpy()[:-1]])
    tr["prev_reward"] = np.concatenate([[np.nan], (tr["fb_type"].to_numpy()[:-1] == 1).astype(float)])
    for w, (lo, hi) in PRE_WINS.items():
        tr[f"pupil_{w}"] = S.pupil_mean(stimt, lo, hi)
        tr[f"me_{w}"] = S.me_mean(stimt, lo, hi)
        tr[f"moving_{w}"] = S.moving_in(stimt, lo, hi)
    out["trials"] = tr
    pv = S.passive_vis.copy()
    pv["session"] = S.name
    pv["subject"] = S.subject
    pv["moving_a"] = S.moving_in(pv["t"].to_numpy(), -0.05, 0.4)
    pv["moving_b"] = S.moving_in(pv["t"].to_numpy(), 0.0, 0.4)
    out["passive"] = pv
    # --- units -------------------------------------------------------------
    U = S.units.iloc[S.good].copy()
    U["session"] = S.name
    U["subject"] = S.subject
    p, e, trate, brate = six_tests(S, tr)
    for k in range(6):
        U[f"p{k+1}"] = p[:, k]
        U[f"e{k+1}"] = e[:, k]
    U["trial_rate"] = trate
    U["baseline_rate"] = brate
    U["slide_resp"] = sliding_responsive(S, tr)
    U = U.reset_index().rename(columns={"index": "unit"})
    out["units"] = U
    # --- trial sets ----------------------------------------------------------
    cl, cr = tr["cl"].to_numpy(), tr["cr"].to_numpy()
    pas = S.passive_all.reset_index(drop=True)
    pvis_idx = np.where((pas["kind"] == "visual").to_numpy())[0]
    pl = np.full(len(pas), np.nan)
    pr = np.full(len(pas), np.nan)
    pl[pvis_idx] = S.passive_vis["pl"].to_numpy()
    pr[pvis_idx] = S.passive_vis["pr"].to_numpy()
    T_idx = np.where(np.isin(tc, ["L", "R", "N"]))[0]
    # Definition M as in the Methods: Go (Left or Right), NoGo and passive, contralateral
    # (right) contrast > 0.
    goM = np.where(go & (cr > 0))[0]
    ngM = np.where((tc == "N") & (cr > 0))[0]
    paM = pvis_idx[pr[pvis_idx] > 0]
    mGo, mNg, mPa = matched_contrast([(goM, cr[goM]), (ngM, cr[ngM]), (paM, pr[paM])], rng=rng["M"])
    # Same, for the single-stimulus trial types of Fig. 2d, f, h.
    gS = np.where((tc == "R") & (cr > 0) & (cl == 0))[0]
    nS = np.where((tc == "N") & (cr > 0) & (cl == 0))[0]
    pS = pvis_idx[(pr[pvis_idx] > 0) & (pl[pvis_idx] == 0)]
    sGo, sNg, sPa = matched_contrast([(gS, cr[gS]), (nS, cr[nS]), (pS, pr[pS])], rng=rng["Msingle"])
    ipsiGo = np.where((tc == "L") & (cl > 0) & (cr == 0))[0]
    ipsiMiss = np.where((tc == "N") & (cl > 0) & (cr == 0))[0]
    # Contralateral Miss trials of the matched set and ipsilateral Miss trials, matched to
    # each other in contrast and count (fig2fg condition iii on equal footing; verifier
    # round 1): at each level as many of each as the smaller has.
    eqC, eqI = matched_contrast([(sNg, cr[sNg]), (ipsiMiss, cl[ipsiMiss])], rng=rng["eq"])
    out["sets"] = dict(mGo=mGo, mNg=mNg, mPa=mPa, sGo=sGo, sNg=sNg, sPa=sPa,
                       ipsiGo=ipsiGo, ipsiMiss=ipsiMiss, n_goM=len(goM), n_ngM=len(ngM),
                       n_paM=len(paM), eqC=eqC, eqI=eqI)
    # --- Fig. 2 traces and z-scores ----------------------------------------
    base = window_rate(S.stim_counts[:, T_idx], -0.02, 0.0, STIM_WIN[0]).mean(axis=1)
    out["traces"] = {k: norm_trace(S, idx, base) for k, idx in
                     [("contraGo", sGo), ("ipsiGo", ipsiGo), ("contraMiss", sNg),
                      ("ipsiMiss", ipsiMiss), ("passive", None)] if k != "passive"}
    if len(sPa):
        m = S.pas_counts[:, sPa].mean(axis=1) / BIN
        m = causal_smooth(causal_smooth(m, 0.02), 0.03)
        out["traces"]["passive"] = ((m - base[:, None]) / (base[:, None] + 0.5)).astype(np.float32)
    z = {}
    for k, cnt, idx in [("sGo", S.stim_counts, sGo), ("sNg", S.stim_counts, sNg),
                        ("ipsiMiss", S.stim_counts, ipsiMiss), ("mNg", S.stim_counts, mNg),
                        ("mPa", S.pas_counts, mPa), ("sPa", S.pas_counts, sPa),
                        ("eqC", S.stim_counts, eqC), ("eqI", S.stim_counts, eqI)]:
        z[k] = zscores(cnt, idx, STIM_WIN[0])
    out["z"] = z
    # --- pre-stimulus rates per trial ----------------------------------------
    pre = {}
    for w, (lo, hi) in PRE_WINS.items():
        pre[f"task_{w}"] = window_rate(S.stim_counts, lo, hi, STIM_WIN[0]).astype(np.float32)
        pre[f"pas_{w}"] = window_rate(S.pas_counts, lo, hi, STIM_WIN[0]).astype(np.float32)
        pre[f"pas_moving_{w}"] = S.moving_in(pas["t"].to_numpy(), lo, hi)
    pre["pas_kind"] = pas["kind"].to_numpy()
    pre["pas_pr"] = pr
    out["pre"] = pre
    # --- detect probability (ccCP algorithm, Go against NoGo) ----------------
    cond = (np.round(cl * 100).astype(int) * 1000 + np.round(cr * 100).astype(int))
    dp = {}
    lab_go = go[T_idx]
    for w, (lo, hi) in {"a": (-0.1, 0.05), "b": (-0.05, 0.0)}.items():
        r = window_rate(S.move_counts[:, T_idx], lo, hi, MOVE_WIN[0]).T
        dp[w] = combined_cp(r, lab_go, cond[T_idx], 2000, rng["cp"])
    for w, (lo, hi) in PRE_WINS.items():
        r = window_rate(S.stim_counts[:, T_idx], lo, hi, STIM_WIN[0]).T
        dp["pre_" + w] = combined_cp(r, lab_go, cond[T_idx], 0, rng["dp_pre"])
    out["dp"] = dp
    # --- choice probability (ccCP, Left against Right; claims ed7c, the part that needs no
    # kernel model) --------------------------------------------------------------
    gi = np.where(go)[0]
    lab_l = tc[gi] == "L"
    cpl = {}
    for w, (lo, hi) in {"a": (-0.1, 0.05), "b": (-0.05, 0.0)}.items():
        r = window_rate(S.move_counts[:, gi], lo, hi, MOVE_WIN[0]).T
        cpl[w] = combined_cp(r, lab_l, cond[gi], 2000, rng["cp_lr"])
    out["cp_lr"] = cpl
    # --- kernel model inputs (fig3c): responses of units with a trial rate of at least
    # 0.1 Hz only, to keep memory down ---------------------------------------------
    ki = kernel_inputs(S, tr)
    keep_u = np.where(U["trial_rate"].to_numpy() >= MIN_RATE)[0]
    ki["Y"] = ki["Y"][:, keep_u]
    ki["unit_pos"] = keep_u
    out["kernel"] = ki
    # --- jPECC inputs: 10 ms counts of VIS, frontal and midbrain neurons ----------
    reg = U["region"].replace(REGION_PARENT).to_numpy()
    okr = (U["trial_rate"].to_numpy() >= MIN_RATE)
    jp = {}
    for gname, members in [("VIS", VIS), ("Frontal", FRONTAL_JPECC), ("Midbrain", MIDBRAIN_JPECC)]:
        sel = np.zeros(len(U), bool)
        for rg in members:
            m = okr & (reg == rg)
            if m.sum() >= MIN_PER_REGION:
                sel |= m
        if sel.sum() == 0:
            continue
        sc = S.stim_counts[sel][:, :, :].reshape(sel.sum(), S.stim_counts.shape[1], -1, 2).sum(axis=3)
        mc = S.move_counts[sel].reshape(sel.sum(), S.move_counts.shape[1], -1, 2).sum(axis=3)
        jp[gname] = dict(stim=sc.astype(np.uint8), move=mc.astype(np.uint8), unit=np.where(sel)[0])
    out["jpecc"] = jp
    # --- clock check: decode the contralateral stimulus from the population in a
    # window before and one after stimulus onset (protocol, author step 2) -------
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import cross_val_score, StratifiedKFold
    y = (cr[T_idx] > 0).astype(int)
    clk = {}
    for nm, (lo, hi) in {"pre": (-0.1, 0.0), "post": (0.05, 0.15)}.items():
        X = window_rate(S.stim_counts[:, T_idx], lo, hi, STIM_WIN[0]).T
        cv = StratifiedKFold(5, shuffle=True, random_state=0)
        clk[nm] = cross_val_score(LogisticRegression(C=0.1, max_iter=2000), X, y, cv=cv).mean()
    clk["chance"] = max(y.mean(), 1 - y.mean())
    out["clock"] = clk
    return out


# ---------------------------------------------------------------------------
# jPECC (claims fig4d; Methods, jPECC analysis; code jPECC/jPECC.m)
# ---------------------------------------------------------------------------
JP_BIN = 0.01          # 10 ms bins (claims fig4d criterion)
JP_SMOOTH = 0.025      # causal half-Gaussian s.d. (claims)
JP_LAMBDA = 0.5        # ridge rows appended, as jPECC.m
JP_MAXPC = 10          # PCs kept, as jPECC.m
JP_FOLDS = 10


def _pcs(X, nd):
    Xc = X - X.mean(axis=0)
    u, s, vt = np.linalg.svd(Xc, full_matrices=False)
    return (u * s)[:, :nd]


def _canon_first(X, Y):
    """First canonical pair of MATLAB canoncorr (columns centred, QR, SVD)."""
    Xc = X - X.mean(axis=0)
    Yc = Y - Y.mean(axis=0)
    q1, r1 = np.linalg.qr(Xc)
    q2, r2 = np.linalg.qr(Yc)
    u, s, vt = np.linalg.svd(q1.T @ q2)
    a = np.linalg.solve(r1, u[:, 0])
    b = np.linalg.solve(r2, vt[0])
    return a, b


def _inv_sqrt(C):
    w, v = np.linalg.eigh(C)
    return (v / np.sqrt(np.maximum(w, 1e-12))[..., None, :]) @ np.swapaxes(v, -1, -2)


def jpecc(sp1, sp2, rng, kfold=JP_FOLDS, lam=JP_LAMBDA, maxpc=JP_MAXPC, pca="all"):
    """sp1, sp2: (trials, bins, neurons). Returns the cross-validated first canonical
    correlation for every pair of time bins (rows: sp1 time, columns: sp2 time).

    PCA (claims fig4d criterion as amended, questions/steinmetz-2019.yaml): pca="all" is
    one PCA per group across time points and trials ("For each region group, principal
    components analysis was performed across time points and trials to reduce population
    activity to 10 dimensions", Methods, jPECC analysis), fitted on the trials and bins
    passed in; pca="bin" is the variant of jPECC.m, one PCA per time bin over all trials.
    Then, as jPECC.m, per fold the first canonical
    pair of the training PCs with ridge rows appended (X: lambda*I then zeros; Y:
    zeros then lambda*I), test trials projected, and the projections of all folds
    correlated. The canonical pair is computed by whitening (Cxx^-1/2 Cxy Cyy^-1/2),
    which gives the same directions and unit training variance as canoncorr, batched
    over the second population's bins."""
    n, nb = sp1.shape[0], sp1.shape[1]
    nd = min(maxpc, sp1.shape[2], sp2.shape[2])
    folds = np.array_split(rng.permutation(n), kfold)
    if pca == "bin":     # one PCA per time bin (jPECC.m; a variant)
        X = np.stack([_pcs(sp1[:, t], nd) for t in range(nb)])   # (nb, n, nd)
        Y = np.stack([_pcs(sp2[:, t], nd) for t in range(nb)])
    else:                # one PCA across time points and trials (Methods, jPECC analysis; criterion)
        X, Y = [], []
        for sp, L in [(sp1, X), (sp2, Y)]:
            flat = sp.reshape(-1, sp.shape[2])
            mu = flat.mean(axis=0)
            _, _, vt = np.linalg.svd(flat - mu, full_matrices=False)
            L.extend([(sp[:, t] - mu) @ vt[:nd].T for t in range(nb)])
        X, Y = np.stack(X), np.stack(Y)
    I = lam * np.eye(nd)
    Zr = np.zeros((nd, nd))
    U = np.zeros((nb, nb, n))
    V = np.zeros((nb, nb, n))
    for f in folds:
        tr = np.setdiff1d(np.arange(n), f)
        Xa = np.concatenate([X[:, tr], np.broadcast_to(I, (nb, nd, nd)), np.broadcast_to(Zr, (nb, nd, nd))], axis=1)
        Ya = np.concatenate([Y[:, tr], np.broadcast_to(Zr, (nb, nd, nd)), np.broadcast_to(I, (nb, nd, nd))], axis=1)
        Xa = Xa - Xa.mean(axis=1, keepdims=True)
        Ya = Ya - Ya.mean(axis=1, keepdims=True)
        m = Xa.shape[1] - 1
        Cxx = np.swapaxes(Xa, 1, 2) @ Xa / m          # (nb, nd, nd)
        Cyy = np.swapaxes(Ya, 1, 2) @ Ya / m
        Wx, Wy = _inv_sqrt(Cxx), _inv_sqrt(Cyy)
        for t1 in range(nb):
            Cxy = (Xa[t1].T @ Ya) / m                  # (nb, nd, nd) over t2
            M = Wx[t1] @ Cxy @ Wy
            u, s_, vt = np.linalg.svd(M)
            a = Wx[t1] @ u[:, :, 0].T                  # (nd, nb)
            b = (Wy @ vt[:, 0, :, None])[:, :, 0]      # (nb, nd)
            U[t1, :, f] = X[t1, f] @ a
            V[t1, :, f] = (Y[:, f] @ b[:, :, None])[:, :, 0].T
    Uc = U - U.mean(axis=2, keepdims=True)
    Vc = V - V.mean(axis=2, keepdims=True)
    return (Uc * Vc).sum(axis=2) / np.sqrt((Uc ** 2).sum(axis=2) * (Vc ** 2).sum(axis=2))


def asymmetry(J, half=5):
    """Asymmetry index (Methods, jPECC analysis): the jPECC matrix is sliced diagonally
    from -50 to +50 ms around each time point t, i.e. the points (t-k, t+k), k = -5..5
    bins of 10 ms. The mean over the half where the first population is earlier
    (t-k, t+k), k = 0..5, minus the mean over the half where it is later (t+k, t-k).
    Positive means the first population leads. NaN where the slice leaves the window."""
    nb = J.shape[0]
    a = np.full(nb, np.nan)
    for t in range(half, nb - half):
        lead1 = np.mean([J[t - k, t + k] for k in range(half + 1)])
        lead2 = np.mean([J[t + k, t - k] for k in range(half + 1)])
        a[t] = lead1 - lead2
    return a
