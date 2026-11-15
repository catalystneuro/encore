"""Loading and measures for Gao et al. (2018), "A cortico-cerebellar loop for motor planning",
Nature 563, 113-116, doi:10.1038/s41586-018-0633-x, on its two datasets.

- DANDI:000007, version 0.220126.1903: 54 NWB files (13 mice) of ALM single units, a trial
  table and the photostimulation code of each trial. Streamed with remfile and h5py.
- CRCNS:alm-4 (doi:10.6080/K0NS0S26, unversioned): the same 54 sessions as MATLAB structures
  in two tar.gz archives (``datafiles.tar.gz``), with the GoodTrials flag, the trial type
  matrix, the laser power trace of every trial and the unit waveforms, plus the lab's analysis
  scripts (``analyses_scripts.zip``). The archives are gzip streams, which cannot be opened in
  place, so each is read once from start to end over HTTP and every member is reduced in
  memory as it passes; nothing is written to disk. One archive (7.4 GB) takes about 6 minutes.

Where the parameters come from (claims file ``claims/gao-2018.yaml``, shared methods B1 and
E1 to E6, cited there from the paper's Methods and legends):

- Trials. Neural analyses use trials with GoodTrials = 1, a photostimulation code that is not
  NaN, no early lick, and inside the unit's stable range (its first to last trial with a
  spike). The paper's Methods give none of these; they are taken from the analysis scripts
  deposited with CRCNS:alm-4 (``analysis_compile_all_ALM_data.m`` and the other compile
  scripts), which the paper's reporting summary announces ("Custom analysis scripts and data
  will be deposited on CRCNS.org").
- Epochs. Sample: pole in to pole out; delay: pole out to the go cue; response: go cue to
  1.3 s after it (scripts, ``Cue_Time + 1.3``; the claims file's reading (a) of E2). Rates are
  spike counts divided by the window length, as in the scripts.
- Units. Putative pyramidal neurons are those whose ``cellType`` is "pyramidal" (E1; the
  descriptor says this is the spike-width rule of the Methods).
- Selectivity test (E2): two-tailed t-test, "lick right" against "lick left" trials, p < 0.05,
  in any epoch.
- Population selectivity (E3): preferred trial type from 10 screening trials of each type
  (Methods, "10 trials for ALM"; the Fig. 2 script draws 10 of each type), spike counts from
  pole in to 1.3 s after the cue (scripts); PSTHs from the remaining trials, smoothed with a
  200 ms boxcar (``func_getPSTH.m``), here evaluated on a 10 ms grid (a standard choice for
  a detail that cannot change a result).
- Photostimulation effect (E4): t-test, control against photostimulation trials, both trial
  types pooled, p < 0.01. A neuron is tested when it has at least 8 control trials of each
  type and more than 3 photostimulation trials of each type (``analysis_compiled_all_ALM_
  DCNstim_FR.m``).
- Latency (E5): 10 ms bins in 1 ms steps, sign flipped for suppressed neurons, onset the first
  bin whose population change differs from 0 (two-tailed t-test, p < 0.01), 10,000 bootstrap
  resamples of neurons (Extended Data Fig. 9a legend).
- Behavior (B1): fraction correct excluding early-lick and no-lick trials; hierarchical
  bootstrap over mice, sessions and trials, 10,000 times (Methods, Behavioral data analysis).
  Trials resampled within a session are drawn as a binomial count of correct trials, which is
  the same distribution as resampling the trials with replacement.
"""

from __future__ import annotations

import io
import json
import tarfile
import time
from concurrent.futures import ThreadPoolExecutor

import fsspec
import h5py
import numpy as np
import pandas as pd
import remfile
import requests
import scipy.io as sio
from scipy import stats

DANDISET_ID = "000007"
DANDISET_VERSION = "0.220126.1903"
CRCNS_ID = "alm-4"
CRCNS_DOI = "10.6080/K0NS0S26"
CRCNS_BASE = "https://crcnsarchive.s3-us-west-2.amazonaws.com/alm-4/live/"
# MD5 sums from alm-4/live/checksums.md5, for the files read
CRCNS_FILES = {
    "photoactivation": ("ALM_recording_DCN_photoactivation/datafiles.tar.gz",
                        "12e9d7af630523ed2511826eeacf6b48"),
    "photoinhibition": ("ALM_recording_DCN_photoinhibition/datafiles.tar.gz",
                        "5123dc96df58457f853e2deb5ce479c7"),
}
CRCNS_SCRIPTS = {
    "photoactivation": ("ALM_recording_DCN_photoactivation/analyses_scripts.zip",
                        "601f4b52198614dbd4761a64d2658698"),
    "photoinhibition": ("ALM_recording_DCN_photoinhibition/analyses_scripts.zip",
                        "4639a8478bc307fb3a5a4b8f2a53fb58"),
}
CODES = {0: "control", 1: "fastigial sample", 2: "fastigial delay", 3: "dentate sample",
         4: "dentate delay", 5: "CN inhibition delay 0.5 s", 6: "CN inhibition delay 1.3 s"}
OUTCOMES = ["HitR", "HitL", "ErrR", "ErrL", "NoLickR", "NoLickL"]
RESPONSE_S = 1.3


# ----------------------------------------------------------------------------- loading


def session_key(subject: str, date: str) -> str:
    """'ANM314746_20151020' style key from a DANDI subject id or a CRCNS file name."""
    s = subject.replace("sub-", "")
    if s.lower().startswith("anm00"):
        s = "ANM" + s[5:]
    return f"{s}_{date}"


def _dandi_one(asset):
    url = requests.head(f"https://api.dandiarchive.org/api/assets/{asset['asset_id']}/download/",
                        allow_redirects=True, timeout=60).url
    with h5py.File(remfile.File(url), "r") as f:
        tr = {k: f["intervals/trials/" + k][:] for k in
              ["start_time", "stop_time", "pole_in_time", "pole_out_time", "cue_time",
               "response", "lick_early", "photo_stim_id"]}
        u = f["units"]
        st, idx = u["spike_times"][:], u["spike_times_index"][:]
        og = {k: json.loads(f[f"general/optogenetics/{k}/location"][()] or "{}")
              for k in f["general/optogenetics"]}
        eg = {k: json.loads(f[f"general/extracellular_ephys/{k}"].attrs.get("location", "{}"))
              for k in f["general/extracellular_ephys"] if k != "electrodes"}
        out = dict(path=asset["path"], trials=pd.DataFrame({k: (v.astype(str) if v.dtype == object else v)
                                                             for k, v in tr.items()}),
                   spikes=np.split(st, idx[:-1]), cell_type=u["cell_type"][:].astype(str),
                   ogen=og, egroups=eg, genotype=f["general/subject/genotype"][()].decode(),
                   trial_columns={k: f["intervals/trials/" + k].attrs.get("description", "")
                                  for k in f["intervals/trials"]})
    sub = asset["path"].split("/")[0]
    out["key"] = session_key(sub, asset["path"].split("_ses-")[1][:8])
    return out


def load_dandi() -> dict:
    """Every NWB file of the pinned version, reduced to trials, spike times and metadata."""
    r = requests.get(f"https://api.dandiarchive.org/api/dandisets/{DANDISET_ID}/versions/"
                     f"{DANDISET_VERSION}/assets/?page_size=200", timeout=60).json()
    assets = [a for a in r["results"] if a["path"].endswith(".nwb")]
    with ThreadPoolExecutor(8) as ex:
        sessions = list(ex.map(_dandi_one, assets))
    return {s["key"]: s for s in sessions}


def _s2d(o):
    if isinstance(o, sio.matlab.mat_struct):
        return {k: _s2d(getattr(o, k)) for k in o._fieldnames}
    return o


def _laser_rows(ts):
    """Per trial: (first sample time, laser on, laser off, mean power while on, peak power),
    from the 'laser_power' channel of the Ephus time series."""
    ids = list(np.atleast_1d(ts.idStr))
    ip = ids.index("laser_power")
    tt, vm = ts.time, ts.valueMatrix
    if tt.ndim == 2:            # one row per trial, channels side by side
        n = tt.shape[1]
        trials = [(tt[i], vm[i, ip * n:(ip + 1) * n]) for i in range(tt.shape[0])]
        trial_ids = None
    else:                        # one long series with a trial number per sample
        tr = ts.trial
        seg = np.split(np.arange(len(tr)), np.flatnonzero(np.diff(tr)) + 1)
        trials = [(tt[g], vm[g, ip]) for g in seg]
        trial_ids = np.array([tr[g[0]] for g in seg])
    rows = []
    for t_, p in trials:
        p = np.nan_to_num(p)
        pk = p.max() if len(p) else 0.0
        on = np.flatnonzero(p > 0.05 * pk) if pk > 0.05 else []
        if len(on):
            rows.append((t_[0], t_[on[0]], t_[on[-1]], p[on[0]:on[-1] + 1].mean(), pk))
        else:
            rows.append((t_[0], np.nan, np.nan, 0.0, pk))
    return np.array(rows), trial_ids, tt.ndim


def _reduce_session(obj) -> dict:
    tp = obj.trialPropertiesHash
    props = dict(zip(tp.keyNames, tp.value))
    tts = list(obj.trialTypeStr)
    ttm = obj.trialTypeMat
    cue = np.asarray(props["CueTime"], float)
    trial_ids = np.asarray(obj.trialIds)
    n = len(trial_ids)
    outcome = np.full(n, "", object)
    for o in OUTCOMES:
        outcome[ttm[tts.index(o)] == 1] = o
    t = pd.DataFrame(dict(
        trial_id=trial_ids, start=np.asarray(obj.trialStartTimes, float),
        pole_in=np.asarray(props["PoleInTime"], float), pole_out=np.asarray(props["PoleOutTime"], float),
        cue=cue[:, 0] if cue.ndim == 2 else cue,
        cue_col2=cue[:, 1] if cue.ndim == 2 else np.nan,
        good=np.asarray(props["GoodTrials"]) == 1,
        ptype=np.asarray(props["PhotostimulationType"], float),
        outcome=outcome, lick_early=ttm[tts.index("LickEarly")] == 1,
        stim_flag=ttm[tts.index("StimTrials")] == 1))
    rows, lt_ids, form = _laser_rows(obj.timeSeriesArrayHash.value)
    lz = np.full((n, 5), np.nan)
    if lt_ids is None:
        lz[:len(rows)] = rows
    else:
        pos = np.searchsorted(trial_ids, lt_ids)
        ok = (pos < n) & (trial_ids[np.minimum(pos, n - 1)] == lt_ids)
        lz[pos[ok]] = rows[ok]
    for j, c in enumerate(["laser_t0", "laser_on", "laser_off", "laser_mean", "laser_peak"]):
        t[c] = lz[:, j]
    t["laser_on"] -= t.start
    t["laser_off"] -= t.start
    t["laser_t0"] -= t.start
    units = []
    for key, u in zip(np.atleast_1d(obj.eventSeriesHash.keyNames), np.atleast_1d(obj.eventSeriesHash.value)):
        ev = np.atleast_1d(np.asarray(u.eventTimes, float))
        etr = np.atleast_1d(np.asarray(u.eventTrials)).astype(int)
        ct = u.cellType if isinstance(u.cellType, str) else (
            "" if np.size(u.cellType) == 0 else str(np.atleast_1d(u.cellType)[0]))
        units.append(dict(key=str(key), t=ev, trial=etr, cell_type=ct,
                          waveform=np.atleast_2d(u.waveforms).mean(0), channel=float(np.median(u.channel))))
    return dict(trials=t, units=units, laser_form=int(form),
                trial_descr=[str(x) for x in np.atleast_1d(tp.descr).ravel()],
                ts_channels=[str(x) for x in np.atleast_1d(obj.timeSeriesArrayHash.value.idStr)])


def stream_crcns(which: str, verbose: bool = True) -> tuple[dict, dict]:
    """Read one CRCNS archive from start to end, reducing each member in memory."""
    path, _ = CRCNS_FILES[which]
    sessions, meta = {}, {}
    t0 = time.time()
    with fsspec.open(CRCNS_BASE + path, block_size=2 ** 24).open() as f:
        with tarfile.open(fileobj=f, mode="r|gz") as tf:
            for m in tf:
                if not m.isfile():
                    continue
                name = m.name.split("/")[-1][:-4]
                d = sio.loadmat(io.BytesIO(tf.extractfile(m).read()), squeeze_me=True,
                                struct_as_record=False)
                if name.startswith("meta_data_"):
                    meta[name[len("meta_data_"):]] = _s2d(d["meta_data"])
                elif name.startswith("data_structure_"):
                    sessions[name[len("data_structure_"):]] = _reduce_session(d["obj"])
                del d
    if verbose:
        print(f"{path}: {len(sessions)} sessions, {len(meta)} meta files, {time.time() - t0:.0f} s")
    return sessions, meta


def read_script_mat(which: str, name: str, variables: list[str]) -> dict:
    """Variables of one of the lab's compiled .mat files in the CRCNS zip (read into memory,
    not to disk). Used only to reconcile counts with the deposit, never for a result."""
    import zipfile
    path, _ = CRCNS_SCRIPTS[which]
    with fsspec.open(CRCNS_BASE + path, block_size=2 ** 22).open() as f:
        with zipfile.ZipFile(f) as z:
            raw = z.read(f"analyses_scripts/{name}")
    return sio.loadmat(io.BytesIO(raw), variable_names=variables, squeeze_me=True)


def read_script(which: str, name: str) -> str:
    """Text of one analysis script in the CRCNS zip, read in place."""
    import zipfile
    path, _ = CRCNS_SCRIPTS[which]
    with fsspec.open(CRCNS_BASE + path, block_size=2 ** 20).open() as f:
        with zipfile.ZipFile(f) as z:
            return z.read(f"analyses_scripts/{name}").decode("latin-1")


# ----------------------------------------------------------------------------- sessions


class Session:
    """One recording session in analysis form (from CRCNS:alm-4, checked against DANDI)."""

    def __init__(self, key, s, meta):
        self.key = key
        self.mouse, self.date = key.split("_")
        t = s["trials"].copy()
        assert np.all(np.diff(t.trial_id) == 1) and t.trial_id.iloc[0] == 1
        t["instructed"] = np.where(t.outcome.str.endswith("R"), "R",
                                   np.where(t.outcome.str.endswith("L"), "L", ""))
        t["correct"] = t.outcome.str.startswith("Hit")
        t["error"] = t.outcome.str.startswith("Err")
        t["nolick"] = t.outcome.str.startswith("NoLick")
        # licked direction: a hit licks the instructed side, an error the other one
        t["licked"] = np.where(t.correct, t.instructed,
                               np.where(t.error, np.where(t.instructed == "R", "L", "R"), ""))
        self.trials = t
        ps = meta["photostim"]["photostimLocation"]
        self.cn_side, self.cn = ps.split()[0], ps.split()[1]
        self.alm_ml = float(meta["extracellular"]["recordingCoordinates"][1])
        self.alm_side = "left" if self.alm_ml < 0 else "right"
        codes = set(t.ptype[t.good & t.ptype.notna()].astype(int))
        self.group = ("fastigial" if codes & {1, 2} else "dentate" if codes & {3, 4}
                      else "inhibition")
        self.units = []
        st = t.start.to_numpy()
        for u in s["units"]:
            ti = u["trial"] - 1
            ok = (ti >= 0) & (ti < len(t))
            ti, ts = ti[ok], u["t"][ok]
            self.units.append(dict(key=u["key"], cell_type=u["cell_type"], ti=ti, rel=ts - st[ti],
                                   first=ti.min() if len(ti) else 0, last=ti.max() if len(ti) else -1,
                                   n_spikes=len(ts), waveform=u["waveform"]))

    def pyramidal(self):
        return [u for u in self.units if u["cell_type"] == "pyramidal"]

    def base_mask(self):
        """Trials the scripts analyse: performing, a valid photostimulation code, no early lick."""
        t = self.trials
        return (t.good & t.ptype.notna() & ~t.lick_early).to_numpy()

    @staticmethod
    def stable(u, n):
        m = np.zeros(n, bool)
        m[u["first"]:u["last"] + 1] = True
        return m

    def counts(self, u, a, b):
        """Spike count of unit u per trial in (a, b), times relative to trial start
        (a and b are arrays over trials or scalars)."""
        n = len(self.trials)
        a = np.broadcast_to(np.asarray(a, float), (n,))
        b = np.broadcast_to(np.asarray(b, float), (n,))
        m = (u["rel"] > a[u["ti"]]) & (u["rel"] < b[u["ti"]])
        return np.bincount(u["ti"][m], minlength=n).astype(float)


def build_sessions(crcns: dict, meta: dict) -> list[Session]:
    return [Session(k, crcns[k], meta[k]) for k in sorted(crcns)]


# ----------------------------------------------------------------------------- behavior


def perf_table(sessions, codes, contra_from="paper"):
    """One row per session, photostimulation code and instructed type: correct and total
    trials (early-lick and no-lick trials excluded, Methods). 'side' is the instructed
    direction relative to the manipulated CN: contra or ipsi. contra_from='paper' takes the
    manipulated CN as contralateral to the recorded ALM (Methods; the photostimulation code
    descriptions); 'metadata' takes the CN side the files give."""
    rows = []
    for s in sessions:
        t = s.trials
        m = t.good & t.ptype.notna() & ~t.lick_early & ~t.nolick & (t.instructed != "")
        if contra_from == "paper":
            cn_side = "right" if s.alm_side == "left" else "left"
        else:
            cn_side = s.cn_side
        contra_dir = "L" if cn_side == "right" else "R"
        for c in codes:
            for d in ("L", "R"):
                mm = m & (t.ptype == c) & (t.instructed == d)
                rows.append(dict(mouse=s.mouse, session=s.key, group=s.group, code=c, instructed=d,
                                 side="contra" if d == contra_dir else "ipsi",
                                 n=int(mm.sum()), k=int((mm & t.correct).sum())))
    return pd.DataFrame(rows)


def early_lick_table(sessions, codes):
    """One row per session and photostimulation code: good trials with an instructed type (n)
    and those flagged LickEarly (k), the per-trial early-lick flag of the trial type matrix.
    With hier_boot this gives the early-lick rate and its bootstrap (B1 applied to early licks,
    the claims file's choice for fig1i and fig1l)."""
    rows = []
    for s in sessions:
        t = s.trials
        m = (t.good & t.ptype.notna() & (t.instructed != "")).to_numpy()
        for c in codes:
            mm = m & (t.ptype == c).to_numpy()
            rows.append(dict(mouse=s.mouse, session=s.key, code=c, side="all", n=int(mm.sum()),
                             k=int((mm & t.lick_early.to_numpy()).sum())))
    return pd.DataFrame(rows)


def hier_boot(tab, stim_code, side=None, n_boot=10000, rng=None, ctrl_code=0):
    """Performance in control and stim trials and the one-tailed hierarchical bootstrap
    p-value of the change (Methods): resample mice, then sessions of each mouse, then trials
    of each session (as binomial counts), 10,000 times; p is the fraction of resamples whose
    change has the sign opposite to the observed change. Also returns p_drop, the fraction of
    resamples with no drop (change >= 0), which is the p of a test for a drop."""
    rng = rng or np.random.default_rng(0)
    t = tab if side is None else tab[tab.side == side]
    g = t.groupby(["mouse", "session", "code"])[["n", "k"]].sum().reset_index()
    ctrl = g[g.code == ctrl_code].set_index(["mouse", "session"])
    stim = g[g.code == stim_code].set_index(["mouse", "session"])
    idx = ctrl.index.intersection(stim.index)
    idx = [i for i in idx if stim.loc[i, "n"] > 0 and ctrl.loc[i, "n"] > 0]
    if not idx:
        return dict(ctrl=np.nan, stim=np.nan, change=np.nan, p=np.nan, p_drop=np.nan, n_mice=0, n_sessions=0)
    cn = np.array([ctrl.loc[i, "n"] for i in idx]); ck = np.array([ctrl.loc[i, "k"] for i in idx])
    sn = np.array([stim.loc[i, "n"] for i in idx]); sk = np.array([stim.loc[i, "k"] for i in idx])
    mice = np.array([i[0] for i in idx])
    obs_c, obs_s = ck.sum() / cn.sum(), sk.sum() / sn.sum()
    change = obs_s - obs_c
    umice = np.unique(mice)
    ses_of = [np.flatnonzero(mice == m) for m in umice]
    chg = np.empty(n_boot)
    for b in range(n_boot):
        pick_m = rng.integers(0, len(umice), len(umice))
        ses = np.concatenate([ses_of[m][rng.integers(0, len(ses_of[m]), len(ses_of[m]))] for m in pick_m])
        kc = rng.binomial(cn[ses], ck[ses] / cn[ses]).sum()
        ks = rng.binomial(sn[ses], sk[ses] / sn[ses]).sum()
        chg[b] = ks / sn[ses].sum() - kc / cn[ses].sum()
    p = np.mean(chg >= 0) if change < 0 else np.mean(chg <= 0)
    return dict(ctrl=obs_c, stim=obs_s, change=change, p=p, p_drop=np.mean(chg >= 0),
                n_ctrl=int(cn.sum()), n_stim=int(sn.sum()), n_mice=len(umice), n_sessions=len(idx))


def trial_level_tests(tab, stim_code, ctrl_code=0):
    """Trial-level checks of a performance change, beside the bootstrap of B1: a one-sided
    z-test of the pooled proportions (stim lower) and a two-sided Cochran-Mantel-Haenszel test
    stratified by session. They ignore the variation between mice and sessions, so they are
    less conservative than the hierarchical bootstrap; they are shown as a check, not used for
    an outcome."""
    from statsmodels.stats.contingency_tables import StratifiedTable
    from statsmodels.stats.proportion import proportions_ztest
    g = tab.groupby(["session", "code"])[["n", "k"]].sum().unstack("code")
    g = g[(g[("n", stim_code)] > 0) & (g[("n", ctrl_code)] > 0)]
    tables = [np.array([[r[("k", stim_code)], r[("n", stim_code)] - r[("k", stim_code)]],
                        [r[("k", ctrl_code)], r[("n", ctrl_code)] - r[("k", ctrl_code)]]]) for _, r in g.iterrows()]
    st = StratifiedTable(tables)
    z = proportions_ztest([g[("k", stim_code)].sum(), g[("k", ctrl_code)].sum()],
                          [g[("n", stim_code)].sum(), g[("n", ctrl_code)].sum()], alternative="smaller")
    return dict(z_p_one_sided=float(z[1]), cmh_odds_ratio=float(st.oddsratio_pooled),
                cmh_p_two_sided=float(st.test_null_odds().pvalue), sessions=len(tables))


# ----------------------------------------------------------------------------- neurons


def selectivity_tests(s: Session, u, trials="correct", response_s=RESPONSE_S, measure="rate"):
    """E2: p-values of the t-test 'lick right' against 'lick left' in the sample, delay and
    response epochs, control trials. trials='correct' (reading a; the Fig. 2 script) or
    'all' (reading b: correct and error trials grouped by instructed type). measure='rate'
    tests counts divided by each trial's epoch length, as the Fig. 2 script; 'count' tests
    spike counts, as E2 words it."""
    t = s.trials
    n = len(t)
    m = s.base_mask() & (t.ptype == 0).to_numpy() & s.stable(u, n)
    m &= t.correct.to_numpy() if trials == "correct" else (t.correct | t.error).to_numpy()
    R, L = m & (t.instructed == "R").to_numpy(), m & (t.instructed == "L").to_numpy()
    pi, po, cue = t.pole_in.to_numpy(), t.pole_out.to_numpy(), t.cue.to_numpy()
    out = {"nR": int(R.sum()), "nL": int(L.sum())}
    for ep, (a, b) in dict(sample=(pi, po), delay=(po, cue), response=(cue, cue + response_s)).items():
        r = s.counts(u, a, b) / ((b - a) if measure == "rate" else 1.0)
        if R.sum() >= 2 and L.sum() >= 2 and (np.var(r[R]) > 0 or np.var(r[L]) > 0):
            out[ep] = stats.ttest_ind(r[R], r[L]).pvalue
        else:
            out[ep] = np.nan
    return out


GRID = np.round(np.arange(-3.5, 2.0001, 0.01), 3)  # time relative to the go cue, s


def psth(s: Session, u, mask, half=0.1):
    """Mean rate (spikes/s) over the trials in mask, in a 200 ms boxcar centred on each point
    of GRID (relative to the go cue; func_getPSTH.m uses a 200 ms boxcar)."""
    idx = np.flatnonzero(mask)
    if len(idx) == 0:
        return np.full(len(GRID), np.nan)
    cue = s.trials.cue.to_numpy()
    sel = np.isin(u["ti"], idx)
    rel = u["rel"][sel] - cue[u["ti"][sel]]
    rel = np.sort(rel)
    hi = np.searchsorted(rel, GRID + half, side="left")
    lo = np.searchsorted(rel, GRID - half, side="right")
    return (hi - lo) / (2 * half) / len(idx)


def pref_selectivity(s: Session, u, ctrl_mask, stim_masks, n_screen, rng):
    """E3: preferred type from n_screen control trials of each type (counts from pole in to
    1.3 s after the cue), then preferred minus non-preferred PSTH on the remaining control
    trials and on each stimulation condition. Returns (control, {name: stim}) or None."""
    t = s.trials
    R = np.flatnonzero(ctrl_mask & (t.instructed == "R").to_numpy())
    L = np.flatnonzero(ctrl_mask & (t.instructed == "L").to_numpy())
    if len(R) <= n_screen or len(L) <= n_screen:
        return None
    R, L = rng.permutation(R), rng.permutation(L)
    c = s.counts(u, t.pole_in.to_numpy(), t.cue.to_numpy() + RESPONSE_S)
    pref_R = c[R[:n_screen]].mean() > c[L[:n_screen]].mean()
    n = len(t)
    mR = np.zeros(n, bool); mR[R[n_screen:]] = True
    mL = np.zeros(n, bool); mL[L[n_screen:]] = True
    sign = 1 if pref_R else -1
    ctrl = sign * (psth(s, u, mR) - psth(s, u, mL))
    out = {}
    for name, sm in stim_masks.items():
        out[name] = sign * (psth(s, u, sm & (t.instructed == "R").to_numpy())
                            - psth(s, u, sm & (t.instructed == "L").to_numpy()))
    return ctrl, out


def boot_mean_ci(x, rng, n_boot=10000, axis0=True):
    """Mean over rows and 95% bootstrap interval over rows (neurons or sessions)."""
    x = np.asarray(x, float)
    n = len(x)
    means = np.empty((n_boot,) + x.shape[1:])
    for b in range(n_boot):
        means[b] = np.nanmean(x[rng.integers(0, n, n)], axis=0)
    return np.nanmean(x, axis=0), np.percentile(means, 2.5, axis=0), np.percentile(means, 97.5, axis=0)


def stim_trials(s: Session, u, code, which="all"):
    """E4 trial sets: control and code trials, both types pooled, within the unit's stable
    range. which='all' (correct, error and no-lick, as the FR script) or 'correct'."""
    t = s.trials
    n = len(t)
    m = s.base_mask() & s.stable(u, n) & (t.instructed != "").to_numpy()
    if which == "correct":
        m &= t.correct.to_numpy()
    ctrl = m & (t.ptype == 0).to_numpy()
    stim = m & (t.ptype == code).to_numpy()
    R, L = (t.instructed == "R").to_numpy(), (t.instructed == "L").to_numpy()
    enough = (ctrl & R).sum() >= 8 and (ctrl & L).sum() >= 8 and (stim & R).sum() > 3 and (stim & L).sum() > 3
    return ctrl, stim, enough


def modulation(s: Session, u, code, a_rel, b_rel, which="all", ref="pole_out"):
    """t-test of spike counts in (ref + a_rel, ref + b_rel), control against code trials.
    b_rel may be 'cue' for the end of the delay. Returns p, rate change, rates."""
    ctrl, stim, enough = stim_trials(s, u, code, which)
    if not enough:
        return None
    t = s.trials
    r0 = t[ref].to_numpy()
    a = r0 + a_rel
    b = t.cue.to_numpy() if isinstance(b_rel, str) else r0 + b_rel
    c = s.counts(u, a, b)
    dur = b - a
    rate = c / dur
    p = stats.ttest_ind(c[ctrl], c[stim]).pvalue if (np.var(c[ctrl]) + np.var(c[stim])) > 0 else 1.0
    return dict(p=p, rate_ctrl=rate[ctrl].mean(), rate_stim=rate[stim].mean(),
                change=rate[stim].mean() - rate[ctrl].mean(), n_ctrl=int(ctrl.sum()), n_stim=int(stim.sum()))


def fine_change(s: Session, u, code, which="all", t_from=-0.1, t_to=0.3, width=0.010, step=0.001):
    """Rate change (stim minus control, spikes/s) in `width` bins stepped by `step`, aligned to
    delay onset (the photostimulation onset of codes 2, 4, 5, 6). Bins are labelled by start."""
    ctrl, stim, enough = stim_trials(s, u, code, which)
    if not enough:
        return None
    t = s.trials
    po = t.pole_out.to_numpy()
    starts = np.round(np.arange(t_from, t_to + 1e-9, step), 4)
    sel = np.isin(u["ti"], np.flatnonzero(ctrl | stim))
    rel = u["rel"][sel] - po[u["ti"][sel]]
    ti = u["ti"][sel]
    out = []
    for m in (ctrl, stim):
        r = np.sort(rel[m[ti]])
        hi = np.searchsorted(r, starts + width, side="left")
        lo = np.searchsorted(r, starts, side="right")
        out.append((hi - lo) / width / m.sum())
    return starts, out[1] - out[0]


def latency(changes, signs, rng, n_boot=10000, alpha=0.01, starts=None, label_shift=0.0):
    """E5 onset: first bin (start >= 0) where the mean sign-flipped change differs from 0 by a
    two-tailed one-sample t-test at p < alpha; bootstrap over neurons. label_shift is added to
    the bin start to label a bin (0: start, 0.005: centre, 0.010: end). Returns onset on all
    neurons, bootstrap mean and s.d. of the onset (ms), and the fraction of resamples with no
    onset. A bin labelled by its start holds spikes up to 10 ms later, and starts are clipped at
    0, so the start label gives the earliest time an effect could begin (an effect that starts
    anywhere in the first 10 ms is labelled 0 ms); the centre and end labels are later by 5 and
    10 ms."""
    X = np.asarray(changes) * np.asarray(signs)[:, None]
    valid = starts >= 0

    def onset(Y):
        mu, sd = Y.mean(0), Y.std(0, ddof=1)
        tt = mu / (sd / np.sqrt(len(Y)))
        p = 2 * stats.t.sf(np.abs(tt), len(Y) - 1)
        hit = np.flatnonzero(valid & (p < alpha) & (mu > 0))
        return (starts[hit[0]] + label_shift) * 1000 if len(hit) else np.nan

    full = onset(X)
    n = len(X)
    ons = np.array([onset(X[rng.integers(0, n, n)]) for _ in range(n_boot)])
    return dict(onset_all=full, boot_mean=np.nanmean(ons), boot_sd=np.nanstd(ons), no_onset=np.mean(np.isnan(ons)), n=n)


# ----------------------------------------------------------------------------- coding direction

CD_STARTS = np.round(np.arange(-3.5, 1.0001, 0.01), 3)  # window starts rel. go cue; windows 400 ms
CD_WIN = 0.4


def cd_session(s: Session, rng, stim_code=None, min_neurons=5, min_trials=5):
    """E6 for one session. Neurons: pyramidal units stable from the 50th trial to the 50th
    before the end (``analysis_compiled_all_ALM_DCNstim_CD.m``); trials inside every
    neuron's stable range. Rates in 400 ms windows in 10 ms steps (labelled by window centre).
    Control trials (correct and error) are split at random in halves; the cd is the mean
    over windows centred in the delay epoch of mean 'lick right' minus mean 'lick left'
    (correct trials of the first half), normalised to unit length. Returns None when the
    session has <= min_neurons neurons or <= min_trials trials in a condition."""
    t = s.trials
    n = len(t)
    neurons = [u for u in s.pyramidal() if u["first"] <= 49 and u["last"] >= n - 51]
    if len(neurons) <= min_neurons:
        return None
    stab = np.ones(n, bool)
    for u in neurons:
        stab &= s.stable(u, n)
    base = s.base_mask() & stab & (t.correct | t.error).to_numpy()
    R, L = (t.instructed == "R").to_numpy(), (t.instructed == "L").to_numpy()
    ctrl = base & (t.ptype == 0).to_numpy()
    cR, cL = rng.permutation(np.flatnonzero(ctrl & R)), rng.permutation(np.flatnonzero(ctrl & L))
    trR, teR = cR[: len(cR) // 2], cR[len(cR) // 2:]
    trL, teL = cL[: len(cL) // 2], cL[len(cL) // 2:]
    trRc = trR[t.correct.to_numpy()[trR]]
    trLc = trL[t.correct.to_numpy()[trL]]
    stim_codes = [stim_code] if stim_code is not None else []
    sets = {"train_R": trRc, "train_L": trLc, "test_R": teR, "test_L": teL,
            "train_all": np.concatenate([trR, trL])}
    for c in stim_codes:
        sets[f"stim_R"] = np.flatnonzero(base & (t.ptype == c).to_numpy() & R)
        sets[f"stim_L"] = np.flatnonzero(base & (t.ptype == c).to_numpy() & L)
    if min(len(v) for v in sets.values()) <= min_trials:
        return None
    used = np.unique(np.concatenate(list(sets.values())))
    cue = t.cue.to_numpy()
    X = np.zeros((len(neurons), n, len(CD_STARTS)))
    for j, u in enumerate(neurons):
        sel = np.isin(u["ti"], used)
        ti = u["ti"][sel]
        rel = u["rel"][sel] - cue[ti]
        for i in used:
            r = np.sort(rel[ti == i])
            X[j, i] = (np.searchsorted(r, CD_STARTS + CD_WIN) - np.searchsorted(r, CD_STARTS, side="right")) / CD_WIN
    centres = CD_STARTS + CD_WIN / 2
    po = np.median(t.pole_out.to_numpy()[used] - cue[used])
    pi = np.median(t.pole_in.to_numpy()[used] - cue[used])
    delay_w = (centres >= po) & (centres <= 0)   # windows centred in the delay epoch
    cd_t = X[:, sets["train_R"]].mean(1) - X[:, sets["train_L"]].mean(1)
    cd = cd_t[:, delay_w].mean(1)
    cd = cd / np.linalg.norm(cd)
    proj = np.einsum("j,jit->it", cd, X)          # trials x windows
    offset = proj[sets["train_all"]].mean()
    return dict(session=s.key, mouse=s.mouse, group=s.group, n_neurons=len(neurons), cd=cd, X=X,
                proj=proj - offset, sets=sets, centres=centres, pole_out=po, pole_in=pi,
                licked=t.licked.to_numpy(), cd_t=cd_t, stab=stab)


# ----------------------------------------------------------------------------- the two deposits


def compare_deposits(sessions: list[Session], dandi: dict, crcns: dict) -> pd.DataFrame:
    """Match each CRCNS session to its DANDI file (subject and date), its trials by start time
    (nearest, within 0.06 s, as DANDI rounds start times) and its units by order, and compare
    them. Adds the column `in_dandi` to each session's trial table."""
    rows = []
    for s in sessions:
        d = dandi[s.key]
        t = s.trials
        dt = d["trials"]
        dist = np.abs(t.start.to_numpy()[:, None] - dt.start_time.to_numpy()[None, :])
        j, dm = dist.argmin(0), dist.min(0)
        ok = dm < 0.06
        in_d = np.zeros(len(t), bool)
        in_d[j[ok]] = True
        t["in_dandi"] = in_d
        eligible = (t.good & t.ptype.notna()).to_numpy()
        jj = j[ok]
        ptype_same = np.all(dt.photo_stim_id.to_numpy()[ok].astype(float) == t.ptype.to_numpy()[jj])
        resp_same = np.all(dt.response.to_numpy()[ok] == t.outcome.to_numpy()[jj])
        cue_diff = np.nanmax(np.abs(dt.cue_time.to_numpy()[ok] - (t.start + t.cue).to_numpy()[jj]))
        cu = crcns[s.key]["units"]
        same = sum(len(a) == len(b["t"]) and np.allclose(a, b["t"]) for a, b in zip(d["spikes"], cu))
        ct_same = sum(a == (b["cell_type"] or "unknown") for a, b in zip(d["cell_type"], cu))
        rows.append(dict(session=s.key, group=s.group, crcns_trials=len(t), good_with_code=int(eligible.sum()),
                         dandi_trials=len(dt), matched=int(ok.sum()), max_start_diff_s=round(float(dm.max()), 3),
                         eligible_not_in_dandi=int((eligible & ~in_d).sum()), dandi_not_eligible=int((in_d & ~eligible).sum()),
                         codes_same=bool(ptype_same), outcomes_same=bool(resp_same), max_cue_diff_s=round(float(cue_diff), 4),
                         units_crcns=len(cu), units_dandi=len(d["spikes"]), units_same_spikes=same, cell_type_same=ct_same))
    return pd.DataFrame(rows)
