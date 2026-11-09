"""Loading and measures for CRCNS data set ofc-4 (Schuck, Cai, Wilson & Niv 2016, Neuron 91:1402).

The data set (doi:10.6080/K0FN14CH) is one zip, FHSS_OFC.zip, in the public S3 bucket
crcnsarchive under ofc-4/live/. It is opened in place over HTTP range requests with fsspec and
zipfile; members are read into memory and nothing is written to disk. It holds, for 24
participants (Subj-01 with four runs, the others five):

- FHSS_OFC_timeseries_designmatrix/Subj-xx/Subj-xx_run-r.mat: OFC_timecourse (TR x voxel), the
  realigned, slice-timing corrected time series inside the participant's OFC mask, in native
  space, with no voxel coordinates; design_matrix_task (TR x 17 or 18), the 16 state regressors
  plus 'first' and 'err' (no 'first' column in some runs); condition_label; nuisance_timecourse
  (TR x 10: four Legendre drift terms, the first a constant, and six motion parameters); TR.
- FHSS_OFC_event/Subj-xx/<condition>_RT_run<r>.1D and _dur_run<r>.1D: AFNI onset:duration
  lists per condition, duration the reaction time (RT files) or the stimulus duration (dur
  files). Times are in seconds, given to 0.1 s.

Condition labels are current then previous trial: 'HyFo' is a trial judging a young house after
a trial that judged an old face (data descriptor, "Data format"). The paper writes the same
state as (Fo)Hy.

Where the parameters come from (the claims file is claims/crcns-ofc-4/10.1016-j.neuron.2016.08.019.yaml):

- GLM: one regressor per state from the data set's design matrix, with 'first', 'err' and the
  ten nuisance time courses (the constant Legendre term is the run mean). The Methods, "fMRI Data
  Analysis", name 16 state regressors, motion and cardiac nuisance regressors and the run mean;
  the data set has no cardiac regressors, a deviation the claims file records (O5).
- Beta maps z-scored within run (Methods, "For classification analyses, we Z scored and
  spatially smoothed the resulting beta maps within each run"). The direction is open (claims
  file, O2): 'voxel' z-scores each voxel across the 16 maps of a run, 'map' each map across
  voxels. Spatial smoothing (O1) cannot be done: the files hold no voxel coordinates.
- Classifier: linear SVM, cost 1, LIBSVM (Methods), here scikit-learn's SVC, which wraps
  LIBSVM, with leave-one-run-out folds.
- Trial-wise test data: the run's time series z-scored per voxel over the run, the volume 2 TRs
  (4.8 s) after stimulus onset (Methods, "For the trial-wise decoding shown in Figure 4B"); the
  3 mm smoothing cannot be done (no coordinates). Which volume is meant is open (claims file):
  'after' takes the first volume starting at or after onset + 4.8 s, 'nearest' the nearest.
- Regressors built here (for the two-back state space): boxcars from onset for the reaction
  time, convolved with SPM's canonical HRF (Methods, "Trial events were modeled as boxcar
  functions whose length reflected the reaction time"; data descriptor, "Data processing"),
  sampled at TR with a shift of -0.6 s, the shift at which the rebuilt state columns best match
  the data set's own (a check in the notebook, not a method choice of the paper).
- Error trials: the 'err' events are blocks that start at the error trial and run over the
  repeated trials. The Methods ("Task") say errors on Internal and Enter trials led to "a
  repetition of the trial", and errors on Exit trials to a repetition of "the trial preceding the
  error"; the Figure 1B legend says the preceding trial was repeated for Internal and Exit trials.
  The Methods are followed; the data descriptor agrees with them. The error trial's previous components
  are the current components of the trial before the block; its current components are the
  previous components of the first labelled trial after the block when the block holds one
  error (the rule is in `error_trials`; its use is an assumption, stated in the notebook).
- Post-error trials in the GLM (claims file, O3). The data set's 'err' column follows a short
  event at each block onset, so the trials inside a block after the error trial are in no
  regressor. The two readings of O3 are rebuilt from the 'err' events: (a) the data set's 'err'
  column with a separate nuisance regressor for the rest of the block, a boxcar from onset +
  4.5 s (the mean trial duration, Methods, Task) to the end of the block; (b) one 'err' boxcar
  over the whole block, from onset to the end of the last stimulus (the dur file's duration).
"""

import io
import re
import zipfile
from functools import lru_cache

import fsspec
import numpy as np
import pandas as pd
import scipy.io as sio
from scipy.stats import gamma
from sklearn.svm import SVC

BASE = "https://crcnsarchive.s3-us-west-2.amazonaws.com/ofc-4/live"
ZIP_URL = f"{BASE}/FHSS_OFC.zip"
TR = 2.4
STATES = [c + a + pc + pa for c in "FH" for a in "oy" for pc in "FH" for pa in "oy"]
COMPONENTS = ["prev_cat", "prev_age", "cur_cat", "cur_age"]


@lru_cache(maxsize=1)
def open_zip():
    """The data set's zip, opened in place over HTTP range requests."""
    f = fsspec.open(ZIP_URL, block_size=2**20).open()
    return zipfile.ZipFile(f)


def members():
    return [i.filename for i in open_zip().infolist()]


def subjects():
    names = members()
    return sorted({int(m) for m in re.findall(r"timeseries_designmatrix/Subj-(\d+)/", "\n".join(names))})


def runs(subject):
    pat = re.compile(rf"Subj-{subject:02d}/Subj-{subject:02d}_run-(\d)\.mat$")
    return sorted(int(m.group(1)) for n in members() if (m := pat.search(n)))


def read_text(url):
    with fsspec.open(url, "rt") as f:
        return f.read()


def parse_state(label):
    """'HyFo' (current house young, previous face old) as a dict of the four components."""
    return {"cur_cat": label[0], "cur_age": label[1], "prev_cat": label[2], "prev_age": label[3]}


def trial_class(label):
    s = parse_state(label)
    if s["cur_cat"] != s["prev_cat"]:
        return "Enter"
    return "Internal" if s["cur_age"] == s["prev_age"] else "Exit"


def load_run(subject, run):
    """The .mat file of one run, with labels stripped."""
    path = f"FHSS_OFC/FHSS_OFC_timeseries_designmatrix/Subj-{subject:02d}/Subj-{subject:02d}_run-{run}.mat"
    m = sio.loadmat(io.BytesIO(open_zip().read(path)))
    return {
        "Y": m["OFC_timecourse"].astype(np.float64),
        "X": m["design_matrix_task"].astype(np.float64),
        "labels": [str(x).strip() for x in m["condition_label"]],
        "nuis": m["nuisance_timecourse"].astype(np.float64),
        "TR": float(m["TR"].ravel()[0]),
        "n_TR": int(m["n_TR"].ravel()[0]),
        "n_voxel": int(m["n_voxel"].ravel()[0]),
        "keys": sorted(k for k in m if not k.startswith("__")),
    }


def _events(subject, run, cond, kind):
    path = f"FHSS_OFC/FHSS_OFC_event/Subj-{subject:02d}/{cond}_{kind}_run{run}.1D"
    try:
        txt = open_zip().read(path).decode()
    except KeyError:
        return []
    out = []
    for tok in txt.split():
        if ":" in tok:
            o, d = tok.split(":")
            out.append((float(o), float(d)))
    return out


def events(subject, run):
    """All events of a run in time order: onset, condition, RT (RT file) and stimulus duration
    (dur file). AFNI's placeholder for an empty condition (negative onset) is dropped."""
    rows = []
    for c in STATES + ["first", "err"]:
        rt = _events(subject, run, c, "RT")
        du = _events(subject, run, c, "dur")
        for (o, r), (o2, d) in zip(rt, du):
            if o < 0:
                continue
            rows.append({"onset": o, "cond": c, "rt": r, "dur": d, "onset_dur": o2})
    df = pd.DataFrame(rows).sort_values("onset").reset_index(drop=True)
    df["subject"] = subject
    df["run"] = run
    return df


SHORT_BLOCK = 12.0
MEAN_TRIAL = 4.5  # mean trial duration (Methods, Task), for reading (a) of O3


def error_trials(ev):
    """Reconstruct the error trial of each error block of one run.

    The error trial is the first trial of the block. Its previous components are the current
    components of the labelled trial before the block (P), and it is an Enter trial when P is an
    Exit trial (task rules, Methods, Task). Its current components are known when the block holds
    one designed trial, the error trial, with its repetitions: they are then the previous
    components of the labelled trial after the block (N). A run of the design has 96 trials after
    the first (Methods, Design: 32 + 32 + 16 + 16 per block), so every block of a run holds one
    designed trial when the run's labelled trials and its blocks add up to 96; the state is then
    taken, and kept only when it is legal (the category switches after an Exit trial and only
    then, and N follows it by the same rule). In other runs the current components are left
    unknown. `klass` is the error trial's class where it is known.

    A second reading (`state_span`) takes the state the same way for an Enter error (after an
    Exit trial) whose block is shorter than SHORT_BLOCK seconds from onset to the end of the last
    stimulus, the span of two trials (an error and its repetition: 4.5 s per trial on average and
    0.7 s of feedback, Methods, Task), in any run. The 12 s bound is read from the distribution of
    spans in the notebook, not from the paper.
    """
    cols = ["subject", "run", "onset", "span", "P", "N", "prev", "cur_cat", "klass", "state", "state_span",
            "one_per_block", "legal"]
    ev = ev.reset_index(drop=True)
    n_lab = int(ev["cond"].isin(STATES).sum())
    n_blk = int((ev["cond"] == "err").sum())
    one_per_block = n_lab + n_blk == 96
    rows = []
    for i, e in ev.iterrows():
        if e["cond"] != "err":
            continue
        P = ev.loc[i - 1, "cond"] if i > 0 else None
        N = ev.loc[i + 1, "cond"] if i + 1 < len(ev) else None
        rec = {"subject": e["subject"], "run": e["run"], "onset": e["onset"], "span": e["dur"],
               "P": P, "N": N, "klass": None, "state": None, "one_per_block": one_per_block, "legal": None}
        if P in STATES:
            p = parse_state(P)
            p_exit = trial_class(P) == "Exit"
            rec["cur_cat"] = ("H" if p["cur_cat"] == "F" else "F") if p_exit else p["cur_cat"]
            rec["prev"] = p["cur_cat"] + p["cur_age"]
            if p_exit:
                rec["klass"] = "Enter"
            if N in STATES:
                n = parse_state(N)
                cand = n["prev_cat"] + n["prev_age"] + p["cur_cat"] + p["cur_age"]
                legal_in = (cand[0] != p["cur_cat"]) if p_exit else (cand[0] == p["cur_cat"])
                legal_out = (N[0] != cand[0]) if trial_class(cand) == "Exit" else (N[0] == cand[0])
                legal = bool(legal_in and legal_out)
                if one_per_block:
                    rec["legal"] = legal
                    if legal:
                        rec["state"] = cand
                        rec["klass"] = trial_class(cand)
                if legal and p_exit and e["dur"] < SHORT_BLOCK:
                    rec["state_span"] = cand
        rows.append(rec)
    out = pd.DataFrame(rows, columns=cols)
    return out.astype({"subject": int, "run": int, "onset": float, "span": float})


def spm_hrf(dt):
    """SPM's canonical HRF (spm_hrf defaults: peak 6 s, undershoot 16 s, ratio 6, length 32 s)."""
    u = np.arange(0, int(32 / dt) + 1)
    h = gamma.pdf(u, 6, scale=1 / dt) - gamma.pdf(u, 16, scale=1 / dt) / 6
    return h / h.sum()


def regressor(onsets, durations, n_tr, tr=TR, shift=-0.6, micro=16):
    """Boxcar of the given durations from each onset, convolved with SPM's HRF, sampled at TR."""
    dt = tr / micro
    u = np.zeros(n_tr * micro + 400)
    for o, d in zip(onsets, durations):
        a = int(round((o + shift) / dt))
        b = int(round((o + shift + d) / dt))
        u[max(a, 0):max(b, a + 1)] = 1
    return np.convolve(u, spm_hrf(dt))[: n_tr * micro: micro]


def glm_betas(Y, X_interest, X_other):
    """OLS betas of the regressors of interest, with the other regressors in the model."""
    X = np.column_stack([X_interest, X_other])
    B, *_ = np.linalg.lstsq(X, Y, rcond=None)
    return B[: X_interest.shape[1]]


def zscore_maps(B, how):
    """z-score a run's beta maps (states x voxels): 'voxel' across states, 'map' across voxels."""
    ax = 0 if how == "voxel" else 1
    mu = B.mean(axis=ax, keepdims=True)
    sd = B.std(axis=ax, keepdims=True)
    sd[sd == 0] = 1
    return (B - mu) / sd


def svm():
    return SVC(kernel="linear", C=1.0)


def component_correct(pred, true):
    """Per test example, whether predicted and true state agree on each component."""
    out = {}
    for comp in COMPONENTS:
        idx = {"cur_cat": 0, "cur_age": 1, "prev_cat": 2, "prev_age": 3}[comp]
        out[comp] = np.array([p[idx] == t[idx] for p, t in zip(pred, true)])
    return out


def volume_index(onset, n_tr, how, lag=4.8, tr=TR):
    """Index of the volume 2 TRs after onset: 'after' the first volume starting at or after
    onset + 4.8 s, 'nearest' the nearest one. Volumes start at k * TR."""
    t = onset + lag
    k = int(np.ceil(t / tr - 1e-9)) if how == "after" else int(np.round(t / tr))
    return k if 0 <= k < n_tr else None


def eight_label(state):
    """The 8-state space without current age (Figure S2C legend): current category, previous
    category and previous age."""
    return state[0] + state[2:]


def subject_designs(subject):
    """Per run: the time series, the data set's 16 state columns, the other columns ('first',
    'err', nuisance), the events and reconstructed error trials, and the rebuilt regressors of
    the two-back state space under both readings of the claims file (a: trials whose two-back
    trial is unknown, after 'first' or an error block, go to one left-out regressor; b: after a
    block with one reconstructed error, which is an Enter error repeated as the same trial
    (Methods, Task), the trial two back as presented is the error trial, whose current components
    are those of its repetition, the trial before), and the nuisance sets of the two readings of
    O3."""
    out = {}
    for r in runs(subject):
        d = load_run(subject, r)
        ev = events(subject, r)
        err = error_trials(ev)
        lab = d["labels"]
        si = [lab.index(s) for s in STATES]
        oi = [i for i, l in enumerate(lab) if l not in STATES]
        Xs = d["X"][:, si]
        Xo = np.column_stack([d["X"][:, oi], d["nuis"]])
        n = d["n_TR"]
        single = set(err.loc[err["state"].notna(), "onset"])
        two = {"a": {}, "b": {}}
        for i, e in ev.iterrows():
            if e["cond"] not in STATES:
                continue
            prev = ev.loc[i - 1] if i > 0 else None
            for reading in ("a", "b"):
                if prev is not None and prev["cond"] in STATES:
                    lab2 = e["cond"][:2] + prev["cond"][2:]
                elif reading == "b" and prev is not None and prev["cond"] == "err" and prev["onset"] in single:
                    lab2 = e["cond"][:2] + e["cond"][2:]
                else:
                    lab2 = "leftout"
                two[reading].setdefault(lab2, []).append((e["onset"], e["rt"]))
        rebuilt = {}
        for reading in ("a", "b"):
            cols, missing = [], []
            for s in STATES:
                ons = two[reading].get(s, [])
                if not ons:
                    missing.append(s)
                cols.append(regressor([o for o, _ in ons], [t for _, t in ons], n))
            lo = two[reading].get("leftout", [])
            extra = [regressor([o for o, _ in lo], [t for _, t in lo], n)] if lo else []
            rebuilt[reading] = {"Xs": np.column_stack(cols), "Xo": np.column_stack(extra + [Xo]) if extra else Xo,
                                "missing": missing, "n_leftout": len(lo)}
        # the hypothesised space rebuilt the same way, to check the rebuilt regressors
        hyp = [regressor(ev.loc[ev.cond == s, "onset"], ev.loc[ev.cond == s, "rt"], n) for s in STATES]
        # the two readings of O3, in place of the data set's 'err' column where they differ from it
        blk = ev[ev.cond == "err"]
        o3 = {"a": Xo, "b": Xo}
        if len(blk):
            no_err = [i for i, l in enumerate(lab) if l not in STATES and l != "err"]
            rest = regressor(blk.onset + MEAN_TRIAL, blk.dur - MEAN_TRIAL, n)
            whole = regressor(blk.onset, blk.dur, n)
            o3 = {"a": np.column_stack([rest, Xo]),
                  "b": np.column_stack([d["X"][:, no_err], whole, d["nuis"]])}
        out[r] = {"Y": d["Y"], "Xs": Xs, "Xo": Xo, "ev": ev, "err": err, "n_TR": n,
                  "two": rebuilt, "Xs_rebuilt": np.column_stack(hyp), "o3": o3}
    return out


def fold_decode(train_X, train_y, test_X, rng=None, n_perm=0):
    """Fit the SVM on the training maps and predict the test examples; with n_perm, also fit
    n_perm classifiers on permuted training labels (test labels unchanged)."""
    clf = svm().fit(train_X, train_y)
    perms = []
    for _ in range(n_perm):
        pc = svm().fit(train_X, rng.permutation(train_y))
        perms.append(pc.predict(test_X))
    return clf, clf.predict(test_X), perms


# Volume readings for the trial-wise test data: the two readings of "2 TRs after stimulus onset"
# (claims file), and, for the timing check of the notebook only, the first volume at or after
# onset plus 0 to 5 TRs.
VOLUMES = {"after": ("after", 4.8), "nearest": ("nearest", 4.8),
           **{f"lag{k}": ("after", k * TR) for k in range(6)}}


SHIFTS = (-6, -4, -2, -1, 0, 1, 2, 4, 6)


def analyse_subject(subject, seed, zhow=("voxel", "map"), n_perm=10):
    """All decoding for one participant: per z-scoring reading, leave-one-run-out predictions of
    the 16-state, 8-state and two-back classifiers on the held-out run's beta maps, permutation
    predictions of the 16-state classifier, and trial-wise predictions of the 16-state
    classifier on single volumes of the held-out run. Also returns the raw beta maps."""
    rng = np.random.default_rng(seed)
    D = subject_designs(subject)
    rs = sorted(D)
    betas = {}
    for r in rs:
        d = D[r]
        betas[("16", r)] = glm_betas(d["Y"], d["Xs"], d["Xo"])
        betas[("16rebuilt", r)] = glm_betas(d["Y"], d["Xs_rebuilt"], d["Xo"])
        X8 = np.column_stack([d["Xs"][:, STATES.index(c + "y" + p)] + d["Xs"][:, STATES.index(c + "o" + p)]
                              for c in "FH" for p in ["Fo", "Fy", "Ho", "Hy"]])
        betas[("8", r)] = glm_betas(d["Y"], X8, d["Xo"])
        for reading in ("a", "b"):
            t = d["two"][reading]
            betas[("two" + reading, r)] = glm_betas(d["Y"], t["Xs"], t["Xo"])
            betas[("16o3" + reading, r)] = glm_betas(d["Y"], d["Xs"], d["o3"][reading])
    labels8 = [c + p for c in "FH" for p in ["Fo", "Fy", "Ho", "Hy"]]
    res = {"betas": {k: v for k, v in betas.items() if k[0] == "16"}, "pred": [], "perm": [], "trial": [],
           "missing_two": {r: {k: D[r]["two"][k]["missing"] for k in "ab"} for r in rs},
           "two_leftout": {r: {k: D[r]["two"][k]["n_leftout"] for k in "ab"} for r in rs},
           "events": pd.concat([D[r]["ev"] for r in rs]), "err": pd.concat([D[r]["err"] for r in rs]),
           "rebuilt_r": {r: [np.corrcoef(D[r]["Xs"][:, j], D[r]["Xs_rebuilt"][:, j])[0, 1] for j in range(16)] for r in rs}}
    for zh in zhow:
        for space, labs in (("16", STATES), ("16rebuilt", STATES), ("16o3a", STATES), ("16o3b", STATES), ("8", labels8),
                            ("twoa", STATES), ("twob", STATES)):
            Z = {r: zscore_maps(betas[(space, r)], zh) for r in rs}
            for test in rs:
                tr_r = [r for r in rs if r != test]
                Xtr = np.vstack([Z[r] for r in tr_r])
                ytr = np.array(labs * len(tr_r))
                if space.startswith("two"):
                    miss = {r: set(D[r]["two"][space[-1]]["missing"]) for r in rs}
                    keep = np.array([l not in miss[r] for r in tr_r for l in labs])
                    Xtr, ytr = Xtr[keep], ytr[keep]
                    tkeep = np.array([l not in miss[test] for l in labs])
                else:
                    tkeep = np.ones(len(labs), bool)
                Xte = Z[test][tkeep]
                yte = np.array(labs)[tkeep]
                nperm = n_perm if space == "16" else 0
                clf, pred, perms = fold_decode(Xtr, ytr, Xte, rng, nperm)
                for t, p in zip(yte, pred):
                    res["pred"].append({"z": zh, "space": space, "run": test, "true": t, "pred": p})
                for k, pp in enumerate(perms):
                    for t, p in zip(yte, pp):
                        res["perm"].append({"z": zh, "run": test, "perm": k, "true": t, "pred": p})
                if space == "16":
                    d = D[test]
                    Yz = (d["Y"] - d["Y"].mean(0)) / np.where(d["Y"].std(0) == 0, 1, d["Y"].std(0))
                    ev = d["ev"]
                    errstate = dict(zip(d["err"]["onset"], d["err"]["state"]))
                    errspan = dict(zip(d["err"]["onset"], d["err"]["state_span"]))
                    for i, e in ev.iterrows():
                        if e["cond"] == "first":
                            continue
                        true = e["cond"] if e["cond"] in STATES else errstate.get(e["onset"])
                        true_span = e["cond"] if e["cond"] in STATES else errspan.get(e["onset"])
                        for vh in VOLUMES:
                            k = volume_index(e["onset"], d["n_TR"], *VOLUMES[vh])
                            if k is None:
                                continue
                            p = clf.predict(Yz[k][None])[0]
                            res["trial"].append({"z": zh, "vol": vh, "run": test, "pos": i, "onset": e["onset"],
                                                 "cond": e["cond"], "true": true, "true_span": true_span, "pred": p})
    # Timing check (notebook, data check): the state regressors shifted by whole TRs against the
    # time series, 16-way leave-one-run-out accuracy with maps z-scored by voxel.
    shift_rows = []
    for k in SHIFTS:
        Z = {}
        for r in rs:
            d = D[r]
            Xs = np.roll(d["Xs"], k, axis=0)
            if k > 0:
                Xs[:k] = 0
            elif k < 0:
                Xs[k:] = 0
            Z[r] = zscore_maps(glm_betas(d["Y"], Xs, d["Xo"]), "voxel")
        for test in rs:
            tr_r = [r for r in rs if r != test]
            clf = svm().fit(np.vstack([Z[r] for r in tr_r]), np.array(STATES * len(tr_r)))
            shift_rows.append({"shift": k, "run": test, "acc": float(np.mean(clf.predict(Z[test]) == np.array(STATES)))})
    res["shift"] = shift_rows
    for key in ("pred", "perm", "trial", "shift"):
        res[key] = pd.DataFrame(res[key]).assign(subject=subject)
    return res
