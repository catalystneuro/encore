"""Loading and measures for CRCNS pfc-7 (Hunt, Malalasekera et al. 2018, Nature Neuroscience).

Hunt, Malalasekera, de Berker, Miranda, Farmer, Behrens & Kennerley (2018), "Triple dissociation
of attention and decision computations across prefrontal cortex", doi:10.1038/s41593-018-0239-5.
The data set is CRCNS pfc-7 (crcns:pfc-7/unversioned; doi:10.6080/K0PZ5712); CRCNS data sets are
not versioned, so the files read are identified by the MD5 sums of its checksums.md5. It is read
anonymously from the public S3 bucket crcnsarchive, under pfc-7/live/. Each file is read into
memory and parsed there; nothing is written to disk.

What is read:

- behavioural_data/<Miles|Frank>_InfoGathering_All_Data.mat (MATLAB 7.3): per session, the
  completed option and attribute trials, with the cue values, the choice, the event codes and the
  joystick trace. `load_behaviour` reads one file at a time (about 1.1 and 1.7 GB in memory).
- neuronal_data/LTH_processed_data.zip: one MATLAB 5 file per unit (Unit0001 to Unit0724),
  the authors' preprocessed data (rasters at 1 ms locked to cues 1 to 3 and the response, the
  trial variables and the spike times per trial). `load_units` reduces each unit as it loads.
- other_data/all_units_info.mat: area, subject, session, channel and mean rate per unit.

Where the parameters come from. The paper's own MATLAB scripts are files of the data set
(scripts.zip); the Code Availability statement points to them. Where the claims file leaves a
detail open and those scripts settle it, the script is named next to the parameter.

- GLM (`glm_design`, `sliding_ols`): EVs 1 to 18 as InfoGathering_Neurons_Cue123_alltrials_
  attentional_value_final.m builds them, with its contrasts 19 to 35; no further constant (EVs 11
  and 12 sum to it); 200 ms windows stepped by 10 ms on rasters from -199 to 600 ms, giving 61
  bins centred from -100 to 500 ms (response-locked rasters run from -600 to 199 ms, so the
  response bins are centred from -500 to 100 ms); trials with fewer than 3 cues viewed dropped;
  odd and even trials numbered before that drop. Claims file, shared GLM method; Methods, GLM.
- CPD (`cpd`): (SSE without the regressor - SSE full) / SSE without it (cpd.m; Methods, RSA
  template-based regression).
- RSA (`rsa_inputs`, `rsa_matrix`, `rsa_design`): calculate_RSA_matrices.m and Fig4_RSA.m;
  conditions LP1-5, LM1-5, RP1-5, RM1-5 by cue 1's side, attribute and rank; mean spike count in
  100 < t < 500 ms; each unit z-scored over the 20 conditions; Pearson correlation between
  conditions. Sliding RSA uses a 200 ms boxcar at every 1 ms (conv2 'same').
- Unit exclusion: mean rate below 1 Hz (Methods, Neuronal Recordings), and unit 87, which every
  figure script of the paper drops as a "bad cell" (Fig4_RSA.m: `area([87 find(average_firing_
  rate<1)]) = nan`). Fig5 and Fig7 scripts also drop unit 653 ("contains nans in T-stats").
- Fig 6 rasters (`acc_long_rasters`): InfoGathering_Neurons_Ramp_to_choice.m; spike times
  from SpikeTable, cue 1 locked -500 to 3000 ms and response locked -3000 to 500 ms, z-scored by
  the unit's session mean and SD (`men`, `sdev`), 200 ms boxcar ('valid'), every 10 ms.
- Joystick movement time (`move_time`): InfoGathering_Behaviour.m, a 5-sample boxcar of the
  first joystick channel from fixation end to response, threshold 1 when the fixation-period
  mean is below 0.8 in absolute value, otherwise 2.9.
- Fig 6 random halves: the 100 halves the scripts drew and stored (`randproj_trials` of
  info_gathering_cue123_alltrials_attentional_final.mat, drawn per unit), read from the data set;
  a variant draws halves once per session, shared by the session's units.
- Cluster test of Figure 5g-j (`clusters`): 8-connected clusters, as MATLAB's bwconncomp and
  bwboundaries use by default (cross_corr_tstats.m, Fig5_OFCcrosscorrelation.m).
- Random seeds are standard choices that cannot change a result beyond permutation noise; each
  analysis passes its own generator.
"""

from __future__ import annotations

import io
import zipfile

import fsspec
import h5py
import numpy as np
import pandas as pd
import scipy.io as sio
from scipy import ndimage, stats

BASE = "https://crcnsarchive.s3-us-west-2.amazonaws.com/pfc-7/live/"
AREAS = {1: "ACC", 2: "DLPFC", 3: "OFC"}
BAD_UNITS = (87,)          # Fig4_RSA.m, Fig6, Fig8 scripts
NAN_TSTAT_UNITS = (653,)   # Fig5_OFCcrosscorrelation.m, Fig7_single_neurons_cue2and3.m
TIMEBINS = np.arange(-100, 501, 10)       # centres of the 61 GLM bins, cue locked
RESP_TIMEBINS = np.arange(-500, 101, 10)  # the same bins, response locked
CUE1_LONG = np.arange(-400, 2901, 10)     # Ramp_to_choice.m timebins_Cue1Long
RESP_LONG = np.arange(-2900, 401, 10)     # Ramp_to_choice.m timebins_ResponseLong


def read_bytes(path: str) -> bytes:
    with fsspec.open(BASE + path, block_size=2**24).open() as f:
        return f.read()


def script_lines(name: str, numbers) -> list[str]:
    """Lines `numbers` (1-based) of scripts/<name> in the data set's scripts.zip."""
    z = zipfile.ZipFile(io.BytesIO(read_bytes("scripts.zip")))
    text = z.read(f"scripts/{name}").decode("latin-1").splitlines()
    return [f"{name}:{i}: {text[i - 1].strip()}" for i in numbers]


def checksums() -> dict:
    """MD5 sums of the data set's files, from its checksums.md5."""
    out = {}
    for line in read_bytes("checksums.md5").decode().splitlines():
        if line.strip() and not line.startswith("#"):
            md5, name = line.split(None, 1)
            out[name.strip()] = md5
    return out


def listing() -> pd.DataFrame:
    import re
    import urllib.request
    url = "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=pfc-7/"
    txt = urllib.request.urlopen(url).read().decode()
    rows = re.findall(r"<Key>(.*?)</Key>.*?<Size>(\d+)</Size>", txt)
    return pd.DataFrame(rows, columns=["key", "size"]).astype({"size": int})


# --------------------------------------------------------------------------- units table

def units_info() -> pd.DataFrame:
    m = sio.loadmat(io.BytesIO(read_bytes("other_data/all_units_info.mat")), squeeze_me=True,
                    struct_as_record=False)
    rows = []
    for i, u in enumerate(m["all_units"], start=1):
        ui = u.UnitInfo
        rows.append(dict(unit=i, area=int(ui.area), area_name=str(ui.area_name),
                         subject=str(ui.subject).upper(), session=int(ui.session_number),
                         channel=int(ui.channel_number), info_rate=float(ui.average_firing_rate)))
    return pd.DataFrame(rows).set_index("unit")


# --------------------------------------------------------------------------- behaviour

def smooth_wa_boxcar(x: np.ndarray, window: int) -> np.ndarray:
    """smooth_wa.m with a boxcar kernel (window made even, ends padded with local means)."""
    if window % 2:
        window += 1
    half = window // 2
    n = len(x)
    padded = np.concatenate([np.full(half, x[:half].mean()), x,
                             np.full(half, x[n - half - 1:].mean())])
    out = np.convolve(padded, np.ones(window) / window)
    return out[window:n + window]


def move_time(joy: np.ndarray, fix_end: int, response: int) -> float:
    """Time of the first sizeable joystick movement, as InfoGathering_Behaviour.m computes it."""
    fix_joy = joy[fix_end - 101:fix_end].mean()
    jt = smooth_wa_boxcar(joy[fix_end - 1:response], 5)
    thr = 1.0 if abs(fix_joy) < 0.8 else 2.9
    idx = np.flatnonzero(np.abs(jt) > thr)
    return float(idx[0] + 1 + fix_end) if len(idx) else np.nan


def _rank(v):
    """calc_rank.m: 0.1/0.15 -> 1 ... 0.9/0.95 -> 5."""
    return int(np.floor(round(v, 2) * 5 + 1e-9)) + 1 if v > 0 else 0


def load_behaviour(subject: str) -> pd.DataFrame:
    """One row per trial of behavioural_data/<Miles|Frank>_InfoGathering_All_Data.mat."""
    name = {"M": "Miles", "F": "Frank"}[subject]
    raw = read_bytes(f"behavioural_data/{name}_InfoGathering_All_Data.mat")
    h = h5py.File(io.BytesIO(raw), "r")
    z = h["zInfoGatheringInfo"]
    rows = []
    for s in range(z.shape[0]):
        g = h[z[s, 0]]
        cond = g["ConditionNumber"][()].ravel()
        terr = g["TrialError"][()].ravel()
        tnum = g["TrialNumber"][()].ravel()
        for i in range(len(cond)):
            u = h[h[g["Uservars"][i, 0]][0, 0]]
            codes = h[g["CodeNumbers"][i, 0]][()].ravel()
            times = h[g["CodeTimes"][i, 0]][()].ravel()
            joy = h[g["AnalogData"][i, 0]]["Joystick"][0, :]
            pay = u["PayoffTracker"][()].ravel()
            prob = u["ProbabilityTracker"][()].ravel()
            fix_end = int(times[codes == 12][0])
            resp = int(times[codes == 72][0])
            pos = codes[(codes > 90) & (codes < 95)].astype(int)
            pos_t = times[(codes > 90) & (codes < 95)]
            rows.append(dict(
                subject=subject, session=s + 1, trial=int(tnum[i]), condition=int(cond[i]),
                trial_error=int(terr[i]), LP=prob[0], RP=prob[1], LM=pay[0], RM=pay[1],
                chosen=int(u["ChosenTarget"][()].ravel()[0]), prob_top=int(u["ProbTop"][()].ravel()[0]),
                fix_end=fix_end, response=resp, cue1_on=float(pos_t[0]) if len(pos_t) else np.nan,
                positions=tuple(pos), pos_times=tuple(pos_t),
                move_time=move_time(joy, fix_end, resp)))
    h.close()
    del raw
    return add_behaviour_measures(pd.DataFrame(rows))


def add_behaviour_measures(b: pd.DataFrame) -> pd.DataFrame:
    """Per-trial measures of InfoGathering_Behaviour.m."""
    b = b.copy()
    b["left_choice"] = (b.chosen == 1).astype(int)
    b["LEV"] = b.LP * b.LM
    b["REV"] = b.RP * b.RM
    b["npv"] = b.positions.map(len)
    b["new_last_time"] = b.move_time - b.pos_times.map(lambda t: t[-1])
    # joystick moved before the last picture was fixated (num_pics_viewedprezero), or within
    # 250 ms of fixating it (num_pics_viewed250)
    b["npv_prezero"] = b.npv - ((b.new_last_time < 0) & (b.npv > 2))
    b["npv250"] = b.npv - ((b.new_last_time <= 250) & (b.npv > 2))
    # value at each position: 91 top left, 92 bottom left, 93 top right, 94 bottom right
    def vals(r):
        top_l, top_r = (r.LP, r.RP) if r.prob_top == 1 else (r.LM, r.RM)
        bot_l, bot_r = (r.LM, r.RM) if r.prob_top == 1 else (r.LP, r.RP)
        return {91: top_l, 92: bot_l, 93: top_r, 94: bot_r}
    seq_rank, seq_left, seq_isprob = [], [], []
    for r in b.itertuples():
        v = vals(r)
        seq_rank.append(tuple(_rank(v[p]) - 3 for p in r.positions))
        seq_left.append(tuple(p in (91, 92) for p in r.positions))
        seq_isprob.append(tuple(((p in (91, 93)) == (r.prob_top == 1)) for p in r.positions))
    b["seq_rank"] = seq_rank      # rank -2..2 of each viewed picture, in order
    b["seq_left"] = seq_left
    b["seq_isprob"] = seq_isprob
    return b


def seen_values(b: pd.DataFrame, npv_col: str, unseen=(0.5, 0.5), mag_shift=True):
    """Left/right probability and magnitude of the pictures seen within the first `npv_col`
    fixations; unseen ones take `unseen` (probability, magnitude). With mag_shift the magnitudes
    0.15..0.95 become 0.1..0.9, as InfoGathering_Behaviour.m does for accuracy_seen."""
    out = np.zeros((len(b), 4))  # LP, LM, RP, RM
    for k, r in enumerate(b.itertuples()):
        n = getattr(r, npv_col)
        lp, lm, rp, rm = unseen[0], unseen[1], unseen[0], unseen[1]
        for p in r.positions[:n]:
            isprob = (p in (91, 93)) == (r.prob_top == 1)
            left = p in (91, 92)
            if isprob and left:
                lp = r.LP
            elif isprob:
                rp = r.RP
            elif left:
                lm = r.LM - 0.05 if mag_shift else r.LM
            else:
                rm = r.RM - 0.05 if mag_shift else r.RM
        out[k] = lp, lm, rp, rm
    return out


# --------------------------------------------------------------------------- units

UNIT_VARS = ["Cue1_MatrixRaw", "Cue2_MatrixRaw", "Cue3_MatrixRaw", "Response_MatrixRaw",
             "reg_mat", "condition", "attendsac1", "Left_choice", "num_pics_viewed", "Lreg", "Rreg",
             "P_first", "First_pos", "Second_pos", "Left_prob", "Left_pay", "Right_prob",
             "Right_pay", "pictures_views", "Prob_top", "Cue1_ON", "Response_time", "SpikeTable",
             "men", "sdev", "sb", "snum", "chnum", "brain_region", "BhvInfo", "inf_trials",
             "nInfoGatheringTrials"]


def slide(raster: np.ndarray, window=200, step=10) -> np.ndarray:
    """sliding_regression_ols_perm.m smoothing: mean of `window` ms starting every `step` ms."""
    n = raster.shape[1]
    nb = n // step - (window // step - 1)
    c = np.concatenate([np.zeros((raster.shape[0], 1)), np.cumsum(raster, axis=1, dtype=float)], 1)
    starts = np.arange(nb) * step
    return (c[:, starts + window] - c[:, starts]) / window


def conv_same_200(x: np.ndarray) -> np.ndarray:
    """MATLAB conv2(1, ones(1,200)/200, x, 'same') along rows: output k sums inputs k-99 to k+100.
    For an even kernel MATLAB's 'same' keeps one sample later than numpy's 'same' (k-100 to k+99),
    so the two differ by one sample by design."""
    n = x.shape[1]
    c = np.concatenate([np.zeros((x.shape[0], 1)), np.cumsum(x, axis=1, dtype=float)], 1)
    k = np.arange(n)
    lo = np.clip(k - 99, 0, n)
    hi = np.clip(k + 101, 0, n)
    return (c[:, hi] - c[:, lo]) / 200


def _long_raster(spikes, events, pre, post, men, sdev):
    """neuron_matrix.m (1000 per spike), z-scored by men/sdev, 200 ms 'valid' boxcar, every
    10 ms (InfoGathering_Neurons_Ramp_to_choice.m)."""
    n = pre + post + 1
    out = np.zeros((len(events), n))
    for a, (st, ev) in enumerate(zip(spikes, events)):
        st = np.atleast_1d(st)
        t = st[(st >= ev - pre) & (st <= ev + post)]
        idx = (t - (ev - pre)).astype(int)
        out[a, idx] = 1000.0
    out = (out - men) / sdev
    c = np.concatenate([np.zeros((len(events), 1)), np.cumsum(out, axis=1)], 1)
    valid = (c[:, 200:] - c[:, :-200]) / 200
    return valid[:, ::10].astype(np.float32)


def rsa_inputs(lreg1, rreg1, p_first, raster, first_pos=None):
    """calculate_RSA_matrices.m: mean spike count 100 < t < 500 ms per condition (20), the
    1 ms smoothed condition means (20 x 800), and with `first_pos` the 40 conditions split by
    top/bottom (calculate_RSA_matrices_updown.m)."""
    pf = p_first.astype(bool)
    cond = np.full(len(lreg1), -1)
    L, R = lreg1 > 0, rreg1 > 0
    cond[L & pf] = lreg1[L & pf] - 1
    cond[L & ~pf] = lreg1[L & ~pf] - 1 + 5
    cond[R & pf] = rreg1[R & pf] - 1 + 10
    cond[R & ~pf] = rreg1[R & ~pf] - 1 + 15
    tb = np.arange(-199, 601)
    nsp = raster[:, (tb > 100) & (tb < 500)].sum(1)
    sm = conv_same_200(raster)
    m20 = np.zeros(20)
    s20 = np.zeros((20, raster.shape[1]), np.float32)
    for c in range(20):
        sel = cond == c
        if sel.any():
            m20[c] = nsp[sel].mean()
            s20[c] = sm[sel].mean(0)
        else:
            m20[c] = np.nan
    out = dict(m20=m20, s20=s20)
    if first_pos is not None:
        up = (first_pos % 2) == 1
        m40 = np.zeros(40)
        for c in range(20):
            for k, sel_up in enumerate((up, ~up)):
                sel = (cond == c) & sel_up
                m40[c + 20 * k] = nsp[sel].mean() if sel.any() else 0.0
        out["m40"] = m40
    return out


def load_units(info: pd.DataFrame, areas=(1, 2, 3), long_areas=(1,)) -> dict:
    """Read the preprocessed units of `areas` and reduce each as it loads.

    Returns a dict unit -> dict with the trial variables, the GLM bins of each epoch
    (`X1`, `X2`, `X3`, `XR`: trials x 61, spikes per ms), RSA inputs, mean rates, and for units
    of `long_areas` the long rasters of Figure 6 (`L1`, `LR`).
    """
    raw = read_bytes("neuronal_data/LTH_processed_data.zip")
    z = zipfile.ZipFile(io.BytesIO(raw))
    out = {}
    for u in info.index[info.area.isin(areas)]:
        m = sio.loadmat(io.BytesIO(z.read(f"LTH_processed_data/Unit{u:04d}.mat")),
                        variable_names=UNIT_VARS, squeeze_me=True, struct_as_record=False)
        d = {}
        for k in ["reg_mat", "condition", "attendsac1", "Left_choice", "num_pics_viewed", "Lreg",
                  "Rreg", "P_first", "First_pos", "Second_pos", "Left_prob", "Left_pay",
                  "Right_prob", "Right_pay", "pictures_views", "Prob_top", "Cue1_ON",
                  "Response_time"]:
            d[k] = np.asarray(m[k], dtype=float)
        for k in ["men", "sdev", "snum", "chnum", "brain_region", "nInfoGatheringTrials"]:
            d[k] = float(m[k])
        d["sb_raw"] = str(m["sb"])
        d["sb"] = d["sb_raw"].upper()
        for k, src in [("X1", "Cue1_MatrixRaw"), ("X2", "Cue2_MatrixRaw"),
                       ("X3", "Cue3_MatrixRaw"), ("XR", "Response_MatrixRaw")]:
            d[k] = slide(np.asarray(m[src], dtype=np.float32)).astype(np.float32)
        r1 = np.asarray(m["Cue1_MatrixRaw"], dtype=np.float32)
        d["rsa"] = rsa_inputs(d["Lreg"][:, 0].astype(int), d["Rreg"][:, 0].astype(int),
                              d["P_first"], r1, d["First_pos"].astype(int))
        k3 = d["num_pics_viewed"] >= 3   # claims file O9 reading (b)
        d["rsa3"] = rsa_inputs(d["Lreg"][k3, 0].astype(int), d["Rreg"][k3, 0].astype(int),
                               d["P_first"][k3], r1[k3])
        bi = m["BhvInfo"]
        osc = np.asarray(bi.OverallSpikeCodes, dtype=float)
        # reading (a): whole session, spikes over the span of the session's spike train
        d["rate_session"] = 1000.0 * (len(osc) - 1) / max(osc.max(), 1.0)
        # reading (b): analysed trials, from trial start to response
        st = m["SpikeTable"]
        resp = d["Response_time"]
        nsp = sum(np.sum((np.atleast_1d(s) >= 0) & (np.atleast_1d(s) <= r)) for s, r in zip(st, resp))
        d["rate_trials"] = 1000.0 * nsp / resp.sum()
        te = np.asarray(bi.TrialError, dtype=float)
        cn = np.asarray(bi.ConditionNumber, dtype=float)
        d["n_info_trials_all"] = int(np.isin(cn, (3, 4)).sum())
        d["n_info_completed"] = int((np.isin(cn, (3, 4)) & np.isin(te, (0, 6))).sum())
        if int(d["brain_region"]) in long_areas:
            d["L1"] = _long_raster(st, d["Cue1_ON"], 500, 3000, d["men"], d["sdev"])
            d["LR"] = _long_raster(st, d["Response_time"], 3000, 500, d["men"], d["sdev"])
        out[u] = d
    del raw, z
    return out


# --------------------------------------------------------------------------- GLM

def glm_design(d: dict) -> np.ndarray:
    """EVs 1 to 18 (InfoGathering_Neurons_Cue123_alltrials_attentional_value_final.m)."""
    rm, cond, a1 = d["reg_mat"], d["condition"], d["attendsac1"]
    n = len(cond)
    X = np.zeros((n, 18))
    X[:, 0:4] = rm * (cond == 3)[:, None]
    X[:, 4:6] = rm[:, 0:2] * (cond == 4)[:, None]
    X[:, 6:8] = rm[:, 2:4] * (a1 == 1)[:, None]
    X[:, 8:10] = rm[:, 2:4] * (a1 == -1)[:, None]
    X[:, 10] = cond == 3
    X[:, 11] = cond == 4
    sg = np.sign
    X[:, 12] = sg(X[:, 0]) * X[:, 1]
    X[:, 13] = -sg(X[:, 4]) * X[:, 5]
    X[:, 14] = -sg(X[:, 0] + X[:, 1]) * X[:, 2]
    X[:, 15] = -sg(X[:, 4] - X[:, 5]) * X[:, 8] + sg(X[:, 4] - X[:, 5]) * X[:, 6]
    lc = np.where(d["Left_choice"] == 0, -1.0, d["Left_choice"])
    X[:, 16] = lc * (cond == 3)
    X[:, 17] = lc * (cond == 4)
    return X


def glm_contrasts() -> np.ndarray:
    """Contrasts 1 to 35 of the GLM script (rows; 0-based index = contrast number - 1), and
    four more for Figure 7 read as attribute trials at cue 3 (36 EV7 - EV5, 37 EV7 - EV6,
    38 EV9 - EV5, 39 EV9 - EV6)."""
    c = np.zeros((39, 18))
    c[:18] = np.eye(18)
    e = np.eye(18)
    c[18:20] = e[0:2] + e[4:6]
    c[20:22] = e[6:8] + e[8:10]
    c[22] = e[12] + e[13]
    c[23:25] = e[6:8] - e[8:10]
    c[25:27] = e[0:2] - e[4:6]
    c[27] = e[12] - e[13]
    c[28] = e[16] + e[17]
    c[29] = e[14] + e[15]
    c[30] = e[5] - e[4]
    c[31] = e[2] - e[0]
    c[32] = e[2] - e[1]
    c[33] = e[0] + e[1]
    c[34] = e[4] + e[5]
    c[35] = e[6] - e[4]
    c[36] = e[6] - e[5]
    c[37] = e[8] - e[4]
    c[38] = e[8] - e[5]
    return c


def ols(Y: np.ndarray, X: np.ndarray, C: np.ndarray):
    """ols.m: contrasts of parameter estimates, their variances and T-statistics.
    Y is trials x bins. Returns (cope, varcope, t), each contrasts x bins."""
    P = np.linalg.pinv(X)
    pe = P @ Y
    res = Y - X @ pe
    dof = X.shape[0] - np.linalg.matrix_rank(X)
    sig = (res * res).sum(0) / dof
    pre = np.einsum("ij,jk,ik->i", C, P @ P.T, C)
    cope = C @ pe
    var = pre[:, None] * sig[None, :]
    with np.errstate(divide="ignore", invalid="ignore"):
        t = cope / np.sqrt(var)
    return cope, var, t


def cpd(Y: np.ndarray, X: np.ndarray) -> np.ndarray:
    """cpd.m: coefficient of partial determination of each column of X (regressors x bins)."""
    def sse(A):
        return ((Y - A @ (np.linalg.pinv(A) @ Y)) ** 2).sum(0)
    full = sse(X)
    out = np.zeros((X.shape[1], Y.shape[1]))
    for i in range(X.shape[1]):
        red = sse(np.delete(X, i, axis=1))
        with np.errstate(divide="ignore", invalid="ignore"):
            out[i] = (red - full) / red
    return out


def fit_glm(d: dict, epochs=("X1", "X2", "X3", "XR"), with_cpd=False, halves=True) -> dict:
    """Sliding GLM of one unit on trials with 3 or more cues viewed."""
    X = glm_design(d)
    keep = d["num_pics_viewed"] >= 3
    n = len(keep)
    odd = np.zeros(n, bool)
    odd[0::2] = True
    C = glm_contrasts()
    out = {"keep": keep, "odd": odd}
    for ep in epochs:
        Y = d[ep].astype(float)[keep]
        Xk = X[keep]
        cope, _, t = ols(Y, Xk, C)
        out["t" + ep], out["b" + ep] = t, cope
        if halves:
            for name, sel in (("odd", odd[keep]), ("even", ~odd[keep])):
                cope, _, t = ols(Y[sel], Xk[sel], C)
                out[f"t{ep}_{name}"], out[f"b{ep}_{name}"] = t, cope
        if with_cpd:
            out["cpd" + ep] = cpd(Y, Xk)
    return out


# --------------------------------------------------------------------------- RSA

def rsa_matrix(M: np.ndarray) -> np.ndarray:
    """Fig4_RSA.m: corrcoef(normalise(unitmat(:,ok),1)') for a conditions x units matrix;
    units that never fire in the window are left out."""
    ok = ~np.all(M == 0, axis=0) & np.all(np.isfinite(M), axis=0)
    Z = M[:, ok]
    Z = (Z - Z.mean(0)) / Z.std(0, ddof=1)
    return np.corrcoef(Z)


def rsa_design(alternative=False) -> tuple[np.ndarray, list]:
    """The seven columns of Fig4_RSA.m: mean, diagonal, stimulus identity, attended value,
    accept/reject, spatial attention, left/right value; templates 3 to 7 divided by their
    maximum absolute value. With `alternative`, attended value is the Supplementary Note's
    -|rank(i) - rank(j)| (demeaned, as the commented line of Fig4_RSA.m), and left/right value
    follows it."""
    m1 = np.tile(np.arange(-2, 3), (5, 1))
    m2 = m1.T
    r1 = np.ones((20, 20))
    r2 = np.eye(20)
    r3 = np.block([[np.zeros((10, 10)), np.eye(10)], [np.eye(10), np.zeros((10, 10))]])
    if alternative:
        r4 = -np.tile(np.abs(m1 - m2), (4, 4)).astype(float)
        r4 = r4 - r4.mean()
    else:
        r4 = np.tile(m1 * m2, (4, 4)).astype(float)
    r5 = (np.tile(((m1 < 0) & (m2 < 0)) | ((m1 > 0) & (m2 > 0)), (4, 4)).astype(float)
          - np.tile(((m1 > 0) & (m2 < 0)) | ((m1 < 0) & (m2 > 0)), (4, 4)).astype(float))
    r6 = np.block([[np.ones((10, 10)), np.zeros((10, 10))], [np.zeros((10, 10)), np.ones((10, 10))]])
    r7 = (r6 > 0) * r4
    dm = np.column_stack([r.ravel(order="F") for r in (r1, r2, r3, r4, r5, r6, r7)])
    dm[:, 2:] = dm[:, 2:] / np.abs(dm[:, 2:]).max(0)
    names = ["mean", "diagonal", "stimulus identity", "attended value", "accept/reject",
             "spatial attention", "left/right value"]
    return dm, names


def rsa_ftest_parts(dm: np.ndarray):
    """Design for the between-region F-tests of Fig4_RSA.m (ols.m with Ftests): three regions
    stacked, one F per template comparing its three coefficients."""
    k = dm.shape[1]
    dmS = np.zeros((3 * 400, 3 * k))
    for r in range(3):
        dmS[400 * r:400 * (r + 1), k * r:k * (r + 1)] = dm
    cmatS = np.hstack([np.eye(2 * k), -np.vstack([np.eye(k), np.eye(k)])])
    full_R = np.eye(dmS.shape[0]) - dmS @ np.linalg.pinv(dmS)
    parts = []
    for i in range(k):
        tc = cmatS[[i, i + k]]
        corth = np.eye(dmS.shape[1]) - tc.T @ np.linalg.pinv(tc.T)
        desorth = dmS @ corth
        resO = np.eye(dmS.shape[0]) - desorth @ np.linalg.pinv(desorth)
        M = resO - full_R
        parts.append((M, np.linalg.matrix_rank(M @ dmS)))
    dof = dmS.shape[0] - np.linalg.matrix_rank(dmS)
    return dmS, full_R, parts, dof


def rsa_fstats(y: np.ndarray, ftp) -> np.ndarray:
    dmS, full_R, parts, dof = ftp
    pe = np.linalg.pinv(dmS) @ y
    fitted = dmS @ pe
    den = y @ full_R @ y
    return np.array([(fitted @ M @ fitted) / den * dof / r for M, r in parts])


def t75(vec: np.ndarray, times: np.ndarray) -> tuple[float, float, float]:
    """calculate_t75max.m: first time the curve exceeds 3/4 of its maximum."""
    i = int(np.argmax(vec))
    mx = vec[i]
    above = np.flatnonzero(vec > 0.75 * mx)
    return float(times[above[0]]), float(times[i]), float(mx)


# --------------------------------------------------------------------------- statistics

def fisher_z(r1, n1, r2, n2, two_sided=True):
    z = (np.arctanh(r1) - np.arctanh(r2)) / np.sqrt(1 / (n1 - 3) + 1 / (n2 - 3))
    p = 2 * stats.norm.sf(abs(z)) if two_sided else stats.norm.sf(z)
    return z, p


def chi2_yates(k1, n1, k2, n2):
    """chi2.m: 2 x 2 chi-square with Yates' correction."""
    obs = np.array([[k1, k2], [n1 - k1, n2 - k2]], float)
    if (obs == 0).any():
        return np.nan, np.nan
    exp = obs.sum(1, keepdims=True) * obs.sum(0, keepdims=True) / obs.sum()
    chi = (((np.abs(obs - exp) - 0.5) ** 2) / exp).sum()
    return chi, stats.chi2.sf(chi, 1)


def binom_p_code(k, n, p0=0.05):
    """Fig8_single_neuron_coding.m: (1 - binocdf(k, n, p0)) * 2."""
    return 2 * stats.binom.sf(k, n, p0)


def binom_p_exact(k, n, p0=0.05):
    """Exact one-sided binomial test, P(X >= k) at chance rate p0 (a check on binom_p_code, which
    leaves out P(X = k) and doubles the rest)."""
    return stats.binomtest(int(k), int(n), p0, alternative="greater").pvalue


def clusters(mask: np.ndarray):
    lab, n = ndimage.label(mask, structure=np.ones((3, 3), int))   # 8-connected, as bwconncomp
    return lab, n


# --------------------------------------------------------------------------- cue 1 regression

def cue1_script_design(d: dict) -> np.ndarray:
    """The 13 regressors of InfoGathering_Neurons_Cue1_regression.m: cue 1 value by attribute
    (magnitude, probability), side and row (raw values, minus 0.55 for magnitude and 0.5 for
    probability), four position constants, and the demeaned number of pictures viewed / 4."""
    fp = d["First_pos"].astype(int)
    lp, lm, rp, rm, pt = d["Left_prob"], d["Left_pay"], d["Right_prob"], d["Right_pay"], d["Prob_top"]
    n = len(fp)
    val = np.zeros(n)
    isprob = np.zeros(n, bool)
    for i in range(n):
        top = fp[i] in (1, 3)
        left = fp[i] in (1, 2)
        isprob[i] = top == (pt[i] == 1)
        val[i] = (lp[i] if left else rp[i]) if isprob[i] else (lm[i] if left else rm[i])
    cols = []
    for prob in (False, True):            # M1LT M1RT M1LB M1RB, then P1..
        for pos in (1, 3, 2, 4):          # LT, RT, LB, RB
            c = np.where((fp == pos) & (isprob == prob), val - (0.5 if prob else 0.55), 0.0)
            cols.append(c)
    for pos in (1, 2, 3, 4):
        cols.append((fp == pos).astype(float))
    pv = d["pictures_views"] / 4
    cols.append(pv - pv.mean())
    return np.column_stack(cols)


def cue1_script_contrasts() -> np.ndarray:
    """Contrasts 26 (value), 41 (left minus right value), 51 (probability minus magnitude value)
    and 42 (top minus bottom value) of the script, over its 13 regressors."""
    e = np.eye(13)
    # columns: 0 M1LT, 1 M1RT, 2 M1LB, 3 M1RB, 4 P1LT, 5 P1RT, 6 P1LB, 7 P1RB
    value = e[0:8].sum(0)
    lr = e[[0, 2, 4, 6]].sum(0) - e[[1, 3, 5, 7]].sum(0)
    pm = e[4:8].sum(0) - e[0:4].sum(0)
    tb = e[[0, 1, 4, 5]].sum(0) - e[[2, 3, 6, 7]].sum(0)
    return np.vstack([value, lr, pm, tb])


def perm_significant(Y, X, C, rng, nperm=1000, first_bin=10, chunk=200):
    """sliding_regression_ols_perm.m: T-statistics of contrasts C over the bins of Y, against the
    2.5th and 97.5th percentiles of the minimum and maximum over bins of the T-statistics from
    `nperm` permutations of the trials; significant when any bin from `first_bin` on passes."""
    P = np.linalg.pinv(X)
    dof = X.shape[0] - np.linalg.matrix_rank(X)
    pre = np.einsum("ij,jk,ik->i", C, P @ P.T, C)
    XtX = X.T @ X
    yy = (Y ** 2).sum(0)

    def tstats(Ys):  # Ys: perms x trials x bins
        pe = np.einsum("kn,pnb->pkb", P, Ys, optimize=True)
        fit = np.einsum("pkb,kl,plb->pb", pe, XtX, pe, optimize=True)
        sig = (yy[None] - fit) / dof
        cope = np.einsum("ck,pkb->pcb", C, pe, optimize=True)
        return cope / np.sqrt(pre[None, :, None] * sig[:, None, :])

    t = tstats(Y[None])[0]
    mx, mn = [], []
    for s in range(0, nperm, chunk):
        idx = np.stack([rng.permutation(Y.shape[0]) for _ in range(min(chunk, nperm - s))])
        tp = tstats(Y[idx])
        mx.append(tp.max(2)); mn.append(tp.min(2))
    mx, mn = np.vstack(mx), np.vstack(mn)
    hi = np.percentile(mx, 97.5, axis=0)
    lo = np.percentile(mn, 2.5, axis=0)
    tt = t[:, first_bin:]
    return ((tt >= hi[:, None]) | (tt <= lo[:, None])).any(1), t


def mat_leading_values(path: str, name: str, count: int) -> tuple[tuple, np.ndarray]:
    """The first `count` values (column-major) of the double array `name`, a top-level variable of
    the MATLAB 5 file `path`, read by HTTP range requests: the variables are walked by their tags
    and only the start of the one wanted is fetched and decompressed. Used for the 5.3 GB
    info_gathering_ramp_to_choice.mat, whose arrays have the random half as their last axis."""
    import struct
    import zlib
    f = fsspec.open(BASE + path, block_size=2**20).open()
    pos, total = 128, f.size
    while pos < total:
        f.seek(pos)
        typ, nbytes = struct.unpack("<II", f.read(8))
        if typ != 15:
            raise ValueError(f"uncompressed element at byte {pos}")
        z = zlib.decompressobj()
        head = z.decompress(f.read(4096))
        off = 8 + 16
        _, dn = struct.unpack("<II", head[off:off + 8])
        dims = struct.unpack(f"<{dn // 4}i", head[off + 8:off + 8 + dn])
        off += 8 + dn + (-dn % 8)
        nt, nn = struct.unpack("<II", head[off:off + 8])
        if nt >> 16:   # small data element
            vname, off = head[off + 4:off + 4 + (nt >> 16)].decode(), off + 8
        else:
            vname, off = head[off + 8:off + 8 + nn].decode(), off + 8 + nn + (-nn % 8)
        if vname != name:
            pos += 8 + nbytes
            continue
        dtype = {9: "<f8", 7: "<f4", 2: "<u1", 1: "<i1", 4: "<u2", 3: "<i2", 6: "<u4", 5: "<i4"}
        rt = struct.unpack("<I", head[off:off + 4])[0] & 0xFFFF
        dt = np.dtype(dtype[rt])
        need = off + 8 + count * dt.itemsize
        buf = bytearray(head)
        while len(buf) < need:
            buf += z.decompress(f.read(2**22))
        return dims, np.frombuffer(bytes(buf[off + 8:need]), dt).astype(float)
    raise KeyError(name)
