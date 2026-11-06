"""Loading and measures for CRCNS pag-2 (Moaddab, Wright & McDannald 2020, Sci Rep 10, 18035).

The data set (doi:10.6080/K0833Q7F) is one zip, pag-2/live/data.zip, in the public S3 bucket
crcnsarchive. It is streamed with fsspec and opened in place with zipfile; nothing is written to
disk. CRCNS data sets are not versioned: the MD5 of data.zip in the data set's checksums.md5 is
`DATA_ZIP_MD5`, and `check_md5` compares the ETag of the object read against it.

The zip holds one MATLAB file per unit (data/matFiles/<name>.mat: spike times `spike`, event
times `EVT01` to `EVT14`, mean waveform), the authors' cube of all units (data/cubeFile/cube.mat,
`vlPAGcube`) and the authors' script data/vlpagAnalysis.m. The event codes are not documented;
they are identified from the data and the cube's trial table (`tag`, cue type and onset per
trial) in the notebook's data check:
EVT09, EVT11 and EVT12 are the onsets of the three cues, EVT08 (= EVT01) shocks, EVT13 nose
pokes, EVT14 one marker 31.5 s before each cue onset, EVT02 not identified (not used). Which of
EVT09, EVT11 and EVT12 is danger, uncertainty or safety differs between behaviour programs
(epr38a, b, c: the counterbalanced auditory identities), so each cue code is assigned by its
shock contingency (shock 2 s after cue offset on all, some or none of its trials).

Where the parameters come from:

- Group of each rat (Control or EAA): only the authors' script data/vlpagAnalysis.m gives it
  (its "Select control units" and "Select EAA units" lists, lines 99 to 122). `CON_RATS`,
  `EAA_RATS` copy those lists. The data description and the files carry no group label.
- Trial types and windows: Methods, "Fear discrimination" (6 danger, 6 uncertainty shock, 10
  uncertainty no-shock, 10 safety; 10 s cues; shock 2 s after cue offset), "Identifying
  cue-responsive neurons" (10 s baseline; first 1 s, first 5 s, last 5 s cue epochs, from the
  Methods and the Results paragraph cited in the claims file), "Z score normalization" (250 ms
  bins, 20 s before cue onset to 20 s after offset, 200 bins; 2 s pre-cue baseline per trial type;
  Z score over all trial types of the neuron) and "Calculating suppression ratios" (20 s baseline,
  10 s cue, each trial its own baseline).
- Uncertainty shock and no-shock trials are pooled into one uncertainty type of 16 trials
  (Methods, "Population and single-unit firing analyses": "Uncertainty trial types were
  collapsed").
- Z scores use the sample SD (ddof = 1), as MATLAB's zscore and the cube's own z fields do
  (checked in the notebook); a standard choice that only rescales each neuron.
- The trial-wise normalized firing for the regressions has four readings (`trial_firing`): the
  three the claims file names (a, b, c) and the cube's own trial-wise z (d, the code's).
- Empty-poke trials (no pokes in baseline or cue, ratio 0/0): readings 'zero' and 'drop'
  (claims file, opening comment).
"""

from __future__ import annotations

import io
import zipfile

import fsspec
import numpy as np
import requests
import scipy.io as sio
from scipy import stats

DATASET = "crcns:pag-2/unversioned"
DOI = "10.6080/K0833Q7F"
BASE_URL = "https://crcnsarchive.s3-us-west-2.amazonaws.com/pag-2/live"
ZIP_URL = BASE_URL + "/data.zip"
DATA_ZIP_MD5 = "7d1686e3d4f6f36895c38f34eda632d4"   # checksums.md5 of the data set

# data/vlpagAnalysis.m, lines 99-103 (Control) and 117-122 (EAA). The lists name more rats than
# the data hold; the notebook prints which are present.
CON_RATS = ["mh%02d" % i for i in (9, 10, 11, 12, 13, 14, 21, 22, 23, 24, 25, 26, 27, 28)]
EAA_RATS = ["mh%02d" % i for i in (15, 16, 17, 18, 19, 20, 29, 30, 31, 32, 33, 34, 35, 36,
                                   37, 38, 39, 40)]

BIN = 0.25                     # s, Methods "Z score normalization"
PRE, POST = 20.0, 30.0         # s around cue onset: 20 s before onset to 20 s after offset
NBIN = int((PRE + POST) / BIN)  # 200
ONSET_BIN = int(PRE / BIN)     # bin 80 is the first 250 ms of the cue
CUE_S = 10.0
SHIFT_S = 10.0   # onsets moved 10 s earlier, before the cue, for the clock check (a standard
                 # choice: spikes are stored only from about 20 s before to 33 s after each onset)
TYPES = ("danger", "uncertainty", "safety")
PROB = {"danger": 1.0, "uncertainty": 0.375, "safety": 0.0}


def _bins(a, b):
    """Bin indices of the window [a, b) s from cue onset."""
    return slice(ONSET_BIN + int(round(a / BIN)), ONSET_BIN + int(round(b / BIN)))


WIN = {
    "base10": _bins(-10, 0), "base2": _bins(-2, 0), "first1": _bins(0, 1),
    "first5": _bins(0, 5), "last5": _bins(5, 10), "cue": _bins(0, 10),
    "anova": _bins(-2, 12),    # 56 bins, 2 s before onset to 2 s after offset
}


def check_md5():
    """ETag of data.zip (its MD5 for a single-part upload) and the checksums.md5 entry."""
    etag = requests.head(ZIP_URL, timeout=60).headers["ETag"].strip('"')
    listed = requests.get(BASE_URL + "/checksums.md5", timeout=60).text
    return etag, DATA_ZIP_MD5 in listed and etag == DATA_ZIP_MD5


def open_zip():
    return zipfile.ZipFile(fsspec.open(ZIP_URL, block_size=2 ** 20).open())


def _get(o, path):
    for p in path.split("."):
        if isinstance(o, np.ndarray) and o.dtype == object:
            o = o[0, 0]
        o = getattr(o, p)
    return o


def load_cube(zf):
    """The authors' cube, vlPAGcube, with unit names decoded (rows of the 22-character names)."""
    m = sio.loadmat(io.BytesIO(zf.read("data/cubeFile/cube.mat")), struct_as_record=False)
    c = m["vlPAGcube"][0, 0]
    nm = c.name
    names = ["".join(nm[0, j][i] for j in range(nm.shape[1])) for i in range(len(nm[0, 0]))]
    return c, names


def cube_field(c, path):
    return np.asarray(_get(c, path))


def group_of(rat):
    if rat in CON_RATS:
        return "Con"
    if rat in EAA_RATS:
        return "EAA"
    raise ValueError(rat)


def load_unit(zf, name):
    """One unit: spike counts per trial in 250 ms bins, trial types, shocks and nose pokes.

    Trials are ordered as the cube orders them (danger, uncertainty shock, uncertainty no-shock,
    safety; by onset time within each).
    """
    m = sio.loadmat(io.BytesIO(zf.read(f"data/matFiles/{name}.mat")))
    spk = np.sort(m["spike"].ravel())
    ev = {k: np.sort(m[k].ravel()) for k in m if k.startswith("EVT")}
    shocks = ev["EVT08"]
    rows = []
    for code in ("EVT09", "EVT11", "EVT12"):
        sh = [bool(np.any(np.abs(shocks - (t + CUE_S + 2.0)) < 0.05)) for t in ev[code]]
        frac = np.mean(sh)
        ty = "danger" if frac == 1 else "safety" if frac == 0 else "uncertainty"
        rows += [(t, ty, s) for t, s in zip(ev[code], sh)]
    order = {"danger": 0, "uncertainty": 1, "safety": 3}
    rows.sort(key=lambda r: (order[r[1]] + (0 if r[2] or r[1] != "uncertainty" else 1), r[0]))
    on = np.array([r[0] for r in rows])
    edges = on[:, None] + (-PRE + BIN * np.arange(NBIN + 1))[None, :]
    idx = np.searchsorted(spk, edges)
    counts = np.diff(idx, axis=1)
    sh_edges = edges - SHIFT_S
    counts_shift = np.diff(np.searchsorted(spk, sh_edges), axis=1)
    pokes = ev["EVT13"]
    pb = np.searchsorted(pokes, on) - np.searchsorted(pokes, on - 20.0)
    pc = np.searchsorted(pokes, on + CUE_S) - np.searchsorted(pokes, on)
    pbs = np.searchsorted(pokes, on - SHIFT_S) - np.searchsorted(pokes, on - SHIFT_S - 20.0)
    pcs = np.searchsorted(pokes, on - SHIFT_S + CUE_S) - np.searchsorted(pokes, on - SHIFT_S)
    return dict(name=name, rat=name[:4], session=name[:10], group=group_of(name[:4]),
                onset=on, type=np.array([r[1] for r in rows]), shock=np.array([r[2] for r in rows]),
                counts=counts, poke_base=pb, poke_cue=pc, n_spikes=len(spk),
                counts_shift=counts_shift, poke_base_shift=pbs, poke_cue_shift=pcs,
                n_events={k: len(v) for k, v in ev.items()}, events=ev)


def load_all(zf, names):
    return [load_unit(zf, n) for n in names]


# ---------- behaviour ----------

def suppression_ratio(u, empty="zero", shifted=False):
    """(baseline rate - cue rate) / (baseline + cue), 20 s baseline, 10 s cue, per trial.

    empty: what a trial with no pokes in either window (0/0) becomes: 'zero', 'drop' (NaN), the
    two readings of the claims file, or 'one', the value the authors' cube stores for such trials
    (cer.cue, checked in the notebook).
    """
    b = u["poke_base_shift" if shifted else "poke_base"] / 20.0
    c = u["poke_cue_shift" if shifted else "poke_cue"] / CUE_S
    with np.errstate(invalid="ignore", divide="ignore"):
        sr = (b - c) / (b + c)
    if empty in ("zero", "one"):
        sr = np.where(np.isnan(sr), 0.0 if empty == "zero" else 1.0, sr)
    return sr


# ---------- firing ----------

def rates(u, shifted=False):
    return u["counts_shift" if shifted else "counts"] / BIN    # Hz per 250 ms bin, trials x 200


def window_rate(u, win, shifted=False):
    return rates(u, shifted)[:, WIN[win]].mean(axis=1)


def select(u, epochs_exc, epochs_inh, alpha=0.05 / 6, r=None, shifted=False):
    """Cue-responsive selection (Methods, Identifying cue-responsive neurons).

    Per cue (danger, uncertainty pooled, safety) and epoch, a paired t test of the trial rates in
    the 10 s baseline against the epoch, two-sided, at p < alpha. Excited: a significant increase
    in an excitation epoch and no significant decrease in any excitation epoch; inhibited the
    reverse over the inhibition epochs. The epoch sets follow the readings of the claims file; the
    authors' script (vlpagAnalysis.m lines 136-147 and 225-236) tests increases over first 1 s and
    last 5 s and decreases over first 5 s and last 5 s, reading (b). `r` replaces the rates with
    other per-trial values (dict window -> array), used for the cube's stored rates.
    """
    def sig(win):
        out = []
        for ty in TYPES:
            m = u["type"] == ty
            base = (r["base10"] if r else window_rate(u, "base10", shifted))[m]
            ep = (r[win] if r else window_rate(u, win, shifted))[m]
            d = ep - base
            if np.all(d == 0):
                out.append(0)
                continue
            t, p = stats.ttest_rel(ep, base)
            out.append(int(np.sign(d.mean())) if p < alpha else 0)
        return out
    se = sum((sig(w) for w in epochs_exc), [])
    si = sum((sig(w) for w in epochs_inh), [])
    if 1 in se and -1 not in se:
        return "exc"
    if -1 in si and 1 not in si:
        return "inh"
    return "osc"


SELECTION_READINGS = {
    "a": (("first1", "last5"), ("first1", "last5")),
    "b": (("first1", "last5"), ("first5", "last5")),
    "c": (("first1", "first5", "last5"), ("first1", "first5", "last5")),
}


def normalized_firing(u, types=TYPES):
    """Methods, Z score normalization: per type, trial-mean rate in 250 ms bins minus that type's
    mean 2 s pre-cue rate; Z score over all bins of all types of the neuron (ddof = 1).
    Returns (types x 200 array, mean, sd) where mean and sd are those of the normalization."""
    r = rates(u)
    diff = []
    for ty in types:
        m = u["type"] == ty if ty in TYPES else (u["type"] == "uncertainty") & (u["shock"] == (ty == "unc_shock"))
        mean = r[m].mean(axis=0)
        diff.append(mean - mean[WIN["base2"]].mean())
    diff = np.array(diff)
    mu, sd = diff.mean(), diff.std(ddof=1)
    return (diff - mu) / sd, mu, sd


def trial_firing(u, reading, cube_z=None):
    """Trial-wise normalized firing, trials x 200 (250 ms bins), for the regressions.

    a: each trial's rate minus the mean 2 s pre-cue rate of its trial type, Z scored with the
       mean and SD of the neuron's normalization (`normalized_firing`);
    b: the same with the trial's own 2 s pre-cue rate subtracted;
    c: each trial's rate Z scored over all trials and bins of the neuron;
    d: the cube's own trial-wise z (the trial's own 2 s baseline subtracted, Z scored over all
       trials and bins), in 1 s bins; `cube_z` is the cube's fire.z.s1 for the unit (32 x 50),
       returned expanded to 250 ms bins so that the same windows apply.
    """
    r = rates(u)
    if reading == "d":
        return np.repeat(cube_z, 4, axis=1)
    if reading == "c":
        return (r - r.mean()) / r.std(ddof=1)
    _, mu, sd = normalized_firing(u)
    own = r[:, WIN["base2"]].mean(axis=1)
    if reading == "a":
        base = np.array([own[u["type"] == t].mean() for t in u["type"]])
    else:
        base = own
    return (r - base[:, None] - mu) / sd


def regress_betas(y, sr, prob):
    """OLS with a constant (Matlab regress); y trials x k. Returns (fear output, threat) betas."""
    X = np.column_stack([np.ones_like(sr), sr, prob])
    ok = ~np.isnan(sr)
    b, *_ = np.linalg.lstsq(X[ok], y[ok], rcond=None)
    return b[1], b[2]


def interval_betas(u, reading, empty, unc_value=0.375, cube_z=None):
    """Fear output and threat probability betas for each 1 s interval of the cue (10 each).

    The response is the trial-wise normalized firing in each 1 s interval (Results, "Diminished
    threat probability signaling", paragraph 1: "normalized firing rate for each trial ... in 1 s
    bins over the 10 s cue"); regressors are the trial's suppression ratio for the 10 s cue and the
    cue's shock probability, with the uncertainty value `unc_value` (Methods, "Single-unit,
    linear regression" and "Threat probability tuning curve"). The beta of a window of several
    intervals is the mean of its interval betas; with the same trials and regressors this equals
    the beta of one regression on the window's mean firing (OLS is linear in the response), so the
    two window readings of the claims file coincide.
    """
    tf = trial_firing(u, reading, cube_z)
    y = tf[:, WIN["cue"]].reshape(len(tf), 10, 4).mean(axis=2)
    prob = np.array([unc_value if t == "uncertainty" else PROB[t] for t in u["type"]])
    return regress_betas(y, suppression_ratio(u, empty), prob)


# ---------- statistics ----------

def _helmert(k):
    """Orthonormal contrasts, k x (k-1)."""
    h = np.zeros((k, k - 1))
    for j in range(1, k):
        h[:j, j - 1] = 1.0
        h[j, j - 1] = -j
        h[:, j - 1] /= np.linalg.norm(h[:, j - 1])
    return h


def mixed_anova(Y, group):
    """Split-plot ANOVA, sphericity assumed, type III for one between factor.

    Y: subjects x within factor levels (one axis per within factor); group: label per subject.
    The paper names no software or correction; it reports partial eta squared and observed power,
    as SPSS does, so its type III sums of squares are used (a choice that changes only the within
    main effects, slightly, when groups differ in size; interactions and the group effect are
    the same under type I).
    Returns {effect: (F, df1, df2, p)} for every within effect, its interaction with group, and
    the group main effect. Within effects are tested on orthonormal contrasts, as SPSS's GLM
    repeated measures does: the effect from the intercept of the contrast scores over the
    unweighted group means, its interaction with group from a one-way ANOVA of the scores.
    """
    Y = np.asarray(Y, float)
    n = Y.shape[0]
    dims = Y.shape[1:]
    labels = np.unique(group)
    k = len(labels)
    gidx = [np.where(group == g)[0] for g in labels]
    out = {}
    # between
    m = Y.reshape(n, -1).mean(axis=1)
    gm = np.array([m[i].mean() for i in gidx])
    ssb = sum(len(i) * (gm[j] - m.mean()) ** 2 for j, i in enumerate(gidx))
    sse = sum(((m[i] - m[i].mean()) ** 2).sum() for i in gidx)
    w = np.prod(dims)
    df2 = n - k
    out["group"] = (ssb / (k - 1) / (sse / df2), k - 1, df2,
                    stats.f.sf(ssb / (k - 1) / (sse / df2), k - 1, df2))
    names = [chr(ord("A") + i) for i in range(len(dims))]
    from itertools import combinations
    for r in range(1, len(dims) + 1):
        for comb in combinations(range(len(dims)), r):
            mats = []
            for d in range(len(dims)):
                mats.append(_helmert(dims[d]) if d in comb else np.ones((dims[d], 1)) / np.sqrt(dims[d]))
            C = mats[0]
            for M in mats[1:]:
                C = np.kron(C, M)
            S = Y.reshape(n, -1) @ C            # n x df
            df1 = S.shape[1]
            err = sum(((S[i] - S[i].mean(axis=0)) ** 2).sum() for i in gidx)
            gmeans = np.array([S[i].mean(axis=0) for i in gidx])
            ss_int = sum(len(i) * ((gmeans[j] - S.mean(axis=0)) ** 2).sum() for j, i in enumerate(gidx))
            um = gmeans.mean(axis=0)
            ss_eff = (um ** 2).sum() / (np.sum([1.0 / len(i) for i in gidx]) / k ** 2)
            dfe = df1 * df2
            ms_e = err / dfe
            nm = "".join(names[c] for c in comb)
            F = ss_eff / df1 / ms_e
            out[nm] = (F, df1, dfe, stats.f.sf(F, df1, dfe))
            F = ss_int / ((k - 1) * df1) / ms_e
            out["group:" + nm] = (F, (k - 1) * df1, dfe, stats.f.sf(F, (k - 1) * df1, dfe))
    return out


def fisher_r_to_z(r1, n1, r2, n2):
    """Fisher r-to-z comparison of two independent correlations; (Z, one-tailed p, two-tailed p)."""
    z = (np.arctanh(r1) - np.arctanh(r2)) / np.sqrt(1.0 / (n1 - 3) + 1.0 / (n2 - 3))
    p1 = stats.norm.sf(abs(z))
    return z, p1, 2 * p1
