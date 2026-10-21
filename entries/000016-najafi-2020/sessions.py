"""Per-session analyses of dandiset 000016, run in worker processes by the notebooks.

Each function takes (index, path, url) and returns small arrays, so that a notebook can stream
all 135 sessions in parallel without holding their traces. The measures are those of
najafi.py; the parameters each claim fixes are cited where they are set. Every analysis draws
from its own generator, seeded by (SEED, claim number, session index), so that results do not
depend on the order sessions are processed in.

Standard choices that the claims file does not fix and that cannot change an outcome:
- Sessions whose traces lack a bin a claim uses are left out of that claim, and counted.
- The 16 Hz trials are those whose stimulus rate is exactly 16 (149 trials in the dandiset).
"""

from __future__ import annotations

import numpy as np
import pandas as pd

import najafi as nj

CLAIM = {  # numbers that seed each claim's generator
    "roc": 1, "noise": 2, "dec_bin": 3, "mixed": 4, "pseudo": 5, "timecourse": 6, "angle": 7,
    "prev": 8, "stim": 9, "outcome": 10, "learn": 11, "learn_onset": 12, "learn_pseudo": 13,
    "equal": 14, "figs2": 15,
}


def rng_for(claim, idx):
    return np.random.default_rng([nj.SEED, CLAIM[claim], idx])


def _type_masks(types):
    return {"exc": types == "excitatory", "inh": types == "inhibitory", "unk": types == "unknown"}


def easy_performance(trials: pd.DataFrame) -> float:
    """Fraction correct on easy trials: the outermost of four equal bins of |rate - 16 Hz|
    on each side (claims file, fig8ab-learning-accuracy, from the code's thQStimStrength = 3).
    The bins span 0 to 11 Hz, the largest distance the 5 to 27 Hz range allows."""
    d = (trials.trial_pulse_rate - 16).abs()
    easy = trials.decided & (d >= 11 * 3 / 4)
    return float(trials.trial_response[easy].eq("correct").mean()) if easy.any() else np.nan


# --- notebook 1: single neurons, correlations ----------------------------------------------------

def single_neurons(args):
    idx, path, url = args
    s = nj.load_session(path, url, groups=("choice", "init", "stim", "reward", "go"), behaviour=True)
    tr, types = s["trials"], s["types"]
    tm = _type_masks(types)
    g = s["groups"]["choice"]
    x = g["x"]
    ok = nj.valid_trials(x) & tr.decided.values
    xb, i1, tb = nj.bin_traces(x, g["event"], g["period"])
    out = dict(idx=idx, path=path, mouse=s["mouse"], date=s["date"], description=s["description"],
               imaging_rate=s["imaging_rate"], period=g["period"], n_trials=len(tr),
               n_decided=int(tr.decided.sum()), n_correct=int(tr.trial_response.eq("correct").sum()),
               n_incorrect=int(tr.trial_response.eq("incorrect").sum()), n_choice_valid=int(ok.sum()),
               n_good=int((s["roi_status"] == "good").sum()), n_bad=int((s["roi_status"] == "bad").sum()),
               n_traced=len(types), traced_all_good=bool((s["roi_status_traced"] == "good").all()),
               n_exc=int(tm["exc"].sum()), n_inh=int(tm["inh"].sum()), n_unk=int(tm["unk"].sum()),
               bad_typed=int(((s["roi_status"] == "bad") & (s["roi_type_all"] != "unknown")).sum()),
               performance=easy_performance(tr), bin_times=tb, i1=i1,
               available=s["available"])
    import hashlib
    out["trial_hash"] = hashlib.md5(pd.util.hash_pandas_object(
        tr.drop(columns=["decided", "choice_high", "stim_high", "is16"]), index=False).values).hexdigest()
    out["start_time_range"] = (float(tr.start_time.min()), float(tr.start_time.max()))
    out["stop_time_range"] = (float(tr.stop_time.min()), float(tr.stop_time.max()))
    out["rate_range"] = (float(tr.trial_pulse_rate.min()), float(tr.trial_pulse_rate.max()))
    out["responses"] = tr.trial_response.value_counts().to_dict()
    out["frames"] = {k: (v["x"].shape[1], v["event"]) for k, v in s["groups"].items()}
    # clock checks against the trial table: a lick at the choice time in the choice-aligned lick
    # trace, and the wheel and lick sampling steps
    lt, lx = s["lick"]["t"], s["lick"]["x"]
    near0 = np.abs(lt) <= 0.0015
    out["lick_at_choice"] = float(np.nanmax(lx[near0][:, ok], 0).mean()) if ok.any() else np.nan
    out["lick_values"] = np.unique(lx[np.isfinite(lx)]).tolist()[:5]
    out["lick_step"] = float(np.median(np.diff(lt)))
    out["wheel_step"] = float(np.median(np.diff(s["wheel"]["t"])))
    out["wheel_range"] = (float(np.nanmin(s["wheel"]["x"])), float(np.nanmax(s["wheel"]["x"])))
    # value checks: inferred spiking, normalised to a maximum of 1 per neuron
    vals = x[np.isfinite(x).all(axis=(1, 2))]
    out["min_value"] = float(np.nanmin(vals)) if vals.size else np.nan
    out["max_value"] = float(np.nanmax(vals)) if vals.size else np.nan
    out["frac_near_zero"] = float(np.mean(np.abs(vals) < 1e-6)) if vals.size else np.nan
    per_neuron_max = np.nanmax(vals, axis=(0, 1)) if vals.size else np.array([])
    maxes = [per_neuron_max]
    for k in ("init", "stim", "reward", "go"):
        if k in s["groups"]:
            v = s["groups"][k]["x"]
            v = v[np.isfinite(v).all(axis=(1, 2))]
            if v.size:
                maxes.append(np.nanmax(v, axis=(0, 1)))
    out["neuron_max_any_alignment"] = np.nanmax(np.stack(maxes), 0)
    # behaviour (fig1b, trial counts)
    out["behaviour"] = tr[["trial_pulse_rate", "trial_type", "trial_response", "decided", "choice_high",
                           "is16"]].copy()
    # lick-free timing check on the trial table: event order within decided trials
    d = tr[tr.decided]
    out["event_order_ok"] = float(((d.init_tone < d.stim_onset) & (d.stim_onset < d.stim_offset)
                                   & (d.go_tone < d.first_commit)).mean())
    # fig1gi: activity per neuron in each bin, correct trials
    corr = ok & tr.trial_response.eq("correct").values
    act = np.nanmean(xb[corr], 0)                                     # (bins, neurons)
    out["act_bins"] = {k: act[:, m] for k, m in tm.items()}
    # ROC on correct trials without 16 Hz, per bin (fig2, figs3)
    roc_tr = corr & ~tr.is16.values
    y = tr.choice_high.values[roc_tr]
    out["n_roc_trials"] = (int((y == 1).sum()), int((y == 0).sum()))
    out["roc_ok"] = bool(min(out["n_roc_trials"]) >= nj.MIN_TRIALS)
    if out["roc_ok"]:
        rng = rng_for("roc", idx)
        R = nj.roc_selectivity(xb[roc_tr], y, rng)                     # arrays (bins, neurons)
        out["roc"] = {k: dict(auc=R["auc"][:, m], sel=R["sel"][:, m], sig=R["sig"][:, m],
                              sig_emp=R["sig_emp"][:, m], sel_shuffled=R["sel_shuffled"][:, m])
                      for k, m in tm.items()}
        # figs3d: neurons matched in median activity at bin -1 (max-bin rule)
        med = np.median(xb[roc_tr][:, i1], 0)
        me, mi = nj.max_bin_match(med[tm["exc"]], med[tm["inh"]])
        out["matched"] = dict(n_exc=int(me.sum()), n_inh=int(mi.sum()),
                              exc_sig=R["sig"][i1][tm["exc"]][me], inh_sig=R["sig"][i1][tm["inh"]][mi],
                              exc_sel=R["sel"][i1][tm["exc"]][me], inh_sel=R["sel"][i1][tm["inh"]][mi])
        # figs3c: wider window, readings (a) bins -2..+2 (194 ms before to 291 ms after) and (b) frames
        # from 200 ms before to 300 ms after the choice
        wa = x[roc_tr][:, g["event"] - 6:g["event"] + 9].mean(1)
        wb_, _ = nj.frame_window(x[roc_tr], g["event"], g["period"], -200, 300)
        win = {}
        for name, w in (("a", wa), ("b", wb_)):
            Rw = nj.roc_selectivity(w, y, rng_for("roc", 10000 + idx))
            win[name] = {k: dict(sig=Rw["sig"][m], sel=Rw["sel"][m]) for k, m in tm.items()}
        out["window"] = win
        # figs3e: AUC on error trials, same labels, bin -1
        err = ok & tr.trial_response.eq("incorrect").values & ~tr.is16.values
        ye = tr.choice_high.values[err]
        out["n_err"] = (int((ye == 1).sum()), int((ye == 0).sum()))
        if min(out["n_err"]) >= 1:
            ae = nj.auc(xb[err][:, i1], ye)
            ac = R["auc"][i1]
            out["auc_err"] = {k: ae[m] for k, m in tm.items()}
            out["auc_corr"] = {k: ac[m] for k, m in tm.items()}
    # noise correlations (fig6, figs10, fig8f): trials with a choice, bin -1, choice means subtracted
    yc = tr.choice_high.values[ok]
    Xn = xb[ok][:, i1]
    r_noise = nj.noise_corr(Xn, yc)
    out["corr"] = {"noise": _corr_summary(r_noise, tm)}
    # preference by the sign of AUC - 0.5 at bin -1, correct trials (significance not required)
    if out["roc_ok"]:
        pref = np.sign(R["auc"][i1] - 0.5)
        out["corr_pref"] = {"noise": _pref_summary(r_noise, tm, pref)}
    # spontaneous: 0-97 ms before the initiation tone, no subtraction
    if "init" in s["groups"]:
        gi = s["groups"]["init"]
        xi, j1, _ = nj.bin_traces(gi["x"], gi["event"], gi["period"])
        oki = ok & nj.valid_trials(gi["x"])
        r_sp = nj.noise_corr(xi[oki][:, j1], None)
        out["corr"]["spont"] = _corr_summary(r_sp, tm)
        if out["roc_ok"]:
            out["corr_pref"]["spont"] = _pref_summary(r_sp, tm, pref)
        out["n_spont_trials"] = int(oki.sum())
        # timing contrast: choice selectivity before the initiation tone, against the choice time
        if out["roc_ok"]:
            pre = oki & roc_tr
            yp = tr.choice_high.values[pre]
            if min((yp == 1).sum(), (yp == 0).sum()) >= nj.MIN_TRIALS:
                Rp = nj.roc_selectivity(xi[pre][:, j1], yp, rng_for("roc", 20000 + idx))
                out["sig_pre_init"] = float(Rp["sig"].mean())
    # matched activity (figs10de): max-bin rule on the median over trials with a choice, bin -1
    med = np.median(Xn, 0)
    me, mi = nj.max_bin_match(med[tm["exc"]], med[tm["inh"]])
    keep = np.zeros(len(types), bool)
    keep[np.where(tm["exc"])[0][me]] = True
    keep[np.where(tm["inh"])[0][mi]] = True
    tmk = {k: m[keep] for k, m in tm.items()}
    out["corr"]["matched_noise"] = _corr_summary(nj.noise_corr(Xn[:, keep], yc), tmk)
    if "init" in s["groups"]:
        out["corr"]["matched_spont"] = _corr_summary(nj.noise_corr(xi[oki][:, j1][:, keep], None), tmk)
    # figs2: fraction of neurons peaking in each 100 ms window of concatenated event-aligned averages
    out["figs2"] = _peak_windows(s, tr, tm)
    return out


def _corr_summary(r, tm):
    e, i = np.where(tm["exc"])[0], np.where(tm["inh"])[0]
    return dict(EE=nj.mean_partner_r(r, e, e), II=nj.mean_partner_r(r, i, i),
                EI_e=nj.mean_partner_r(r, e, i), EI_i=nj.mean_partner_r(r, i, e))


def _pref_summary(r, tm, pref):
    out = {}
    e, i = np.where(tm["exc"])[0], np.where(tm["inh"])[0]
    for name, rows, cols in (("EE", e, e), ("II", i, i), ("EI_e", e, i), ("EI_i", i, e)):
        same, opp = [], []
        for n in rows:
            c = cols[cols != n]
            s_ = c[pref[c] == pref[n]]
            o_ = c[pref[c] != pref[n]]
            same.append(np.nanmean(r[n, s_]) if len(s_) else np.nan)
            opp.append(np.nanmean(r[n, o_]) if len(o_) else np.nan)
        out[name] = (np.array(same), np.array(opp))
    return out


def _peak_windows(s, tr, tm):
    """Trial-averaged traces aligned to the start tone, stimulus, choice and reward, concatenated;
    each neuron's peak assigned to a 100 ms window of the concatenated time axis (Figure S2)."""
    keys = ("init", "stim", "choice", "reward")
    if not all(k in s["groups"] for k in keys):
        return None
    ok = tr.trial_response.eq("correct").values.copy()
    for k in keys:
        ok &= nj.valid_trials(s["groups"][k]["x"])
    if ok.sum() < 2:
        return None
    segs = {k: np.nanmean(s["groups"][k]["x"][ok], 0).astype(np.float32) for k in keys}
    return dict(segs=segs, events={k: s["groups"][k]["event"] for k in keys},
                period=s["groups"]["choice"]["period"], n_trials=int(ok.sum()),
                exc=tm["exc"], inh=tm["inh"])


def peak_window_fractions(f, before, after):
    """Concatenate each event's average over a common window (frames before and after each event),
    find each neuron's peak, and return the fraction of each type peaking in each 100 ms window."""
    segs = [f["segs"][k][f["events"][k] - before[k]:f["events"][k] + after[k]] for k in before]
    cat = np.concatenate(segs, 0)
    t = np.arange(cat.shape[0]) * f["period"] * 1000
    win = (t // 100).astype(int)
    n_win = win.max() + 1
    peak = cat.argmax(0)
    return {k: np.bincount(win[peak[f[k]]], minlength=n_win) / max(f[k].sum(), 1) for k in ("exc", "inh")}


def roc_repeats(args):
    """fig2a: the 50-shuffle ROC at 0-97 ms before the choice, repeated with 20 seeds."""
    idx, path, url, n_repeats = args
    s = nj.load_session(path, url, groups=("choice",))
    tr, types = s["trials"], s["types"]
    tm = _type_masks(types)
    g = s["groups"]["choice"]
    ok = nj.valid_trials(g["x"]) & tr.trial_response.eq("correct").values & ~tr.is16.values
    xb, i1, _ = nj.bin_traces(g["x"], g["event"], g["period"])
    y = tr.choice_high.values[ok]
    counts = []
    for k in range(n_repeats):
        R = nj.roc_selectivity(xb[ok][:, i1], y, rng_for("roc", 30000 + 100 * idx + k))
        counts.append((int(R["sig"][tm["exc"]].sum()), int(R["sig"][tm["inh"]].sum()),
                       int(R["sig_emp"][tm["exc"]].sum()), int(R["sig_emp"][tm["inh"]].sum())))
    return dict(n_exc=int(tm["exc"].sum()), n_inh=int(tm["inh"].sum()), counts=np.array(counts),
                n_trials=(int((y == 1).sum()), int((y == 0).sum())))


# --- notebook 2: choice decoders at 0-97 ms before the choice ----------------------------------

def _choice_data(s, trial_set="correct"):
    tr = s["trials"]
    g = s["groups"]["choice"]
    ok = nj.valid_trials(g["x"]) & tr.decided.values
    xb, i1, tb = nj.bin_traces(g["x"], g["event"], g["period"])
    if trial_set == "correct":
        sel = ok & tr.trial_response.eq("correct").values
    else:
        sel = ok
    return xb, i1, tb, sel, ok


def _zbins(x):
    z, _, _ = nj.zscore(x, 0)
    return z


def decode_bin(args):
    """fig3bc, fig3df (bin -1), figs6de and fig4bd."""
    idx, path, url = args
    s = nj.load_session(path, url, groups=("choice",))
    tr, types = s["trials"], s["types"]
    tm = _type_masks(types)
    xb, i1, tb, corr, ok = _choice_data(s, "correct")
    y = s["trials"].choice_high.values
    yc = y[corr].astype(int)
    out = dict(idx=idx, path=path, mouse=s["mouse"], date=s["date"], bin_times=tb, i1=i1,
               n_left=int((yc == 1).sum()), n_right=int((yc == 0).sum()),
               n_exc=int(tm["exc"].sum()), n_inh=int(tm["inh"].sum()), n_all=len(types))
    out["ok"] = min(out["n_left"], out["n_right"]) >= nj.MIN_TRIALS and out["n_inh"] >= 2
    if not out["ok"]:
        return out
    X = xb[corr]                                   # (trials, bins, neurons)
    Xz_bins = _zbins(X)                            # each bin z-scored over the correct trials
    inc = ok & tr.trial_response.eq("incorrect").values
    yi = y[inc].astype(int)
    out["n_incorrect"] = (int((yi == 1).sum()), int((yi == 0).sum()))
    Xi = xb[inc][:, i1]
    rng = rng_for("dec_bin", idx)

    def run(cols):
        Xp = X[:, i1][:, cols]
        mu = Xp.mean(0)
        sd = Xp.std(0) + nj.SD_PAD
        tests = {"stab": (Xz_bins[:, :, cols], "same_trials")}
        if len(yi) >= 2:
            tests["inc_train_norm"] = (((Xi[:, cols] - mu) / sd, yi), "other_trials")
            zi, _, _ = nj.zscore(Xi[:, cols])
            tests["inc_own_norm"] = ((zi, yi), "other_trials")
        r = nj.decode(Xp, yc, rng, test_sets=tests)
        return {k: v for k, v in r.items() if k not in ("w_reps", "mu", "sd")}

    all_cols = np.arange(len(types))
    out["all"] = run(all_cols)
    out["all"]["w_types"] = types.copy()
    out["inh"] = run(np.where(tm["inh"])[0])
    exc_idx = np.where(tm["exc"])[0]
    n = out["n_inh"]
    out["exc"] = [run(np.sort(rng.choice(exc_idx, n, replace=False))) for _ in range(nj.N_EXC_SAMPLES)]
    for d in out["exc"]:
        d.pop("w", None)
    return out


def decode_variants(args):
    """fig3hi (mixed against excitatory populations) and fig7 (real against pseudo populations),
    at 0-97 ms before the choice."""
    idx, path, url = args
    s = nj.load_session(path, url, groups=("choice",))
    types = s["types"]
    tm = _type_masks(types)
    xb, i1, tb, corr, ok = _choice_data(s, "correct")
    y = s["trials"].choice_high.values
    yc = y[corr].astype(int)
    exc_idx = np.where(tm["exc"])[0]
    n = int(tm["inh"].sum())
    out = dict(idx=idx, path=path, mouse=s["mouse"], date=s["date"], n_inh=n, n_exc=len(exc_idx),
               n_all=len(types), n_left=int((yc == 1).sum()), n_right=int((yc == 0).sum()))
    out["ok"] = min(out["n_left"], out["n_right"]) >= nj.MIN_TRIALS and n >= 2
    if not out["ok"]:
        return out
    X = xb[corr]
    # fig3hi: n inhibitory + n excitatory against 2n excitatory, 10 subsamples each
    rngm = rng_for("mixed", idx)
    mixed, exc2 = [], []
    if len(exc_idx) >= 2 * n:
        for _ in range(N_MIXED):
            e = rngm.choice(exc_idx, n, replace=False)
            mixed.append(nj.decode(X[:, i1][:, np.r_[np.where(tm["inh"])[0], e]], yc, rngm)["acc"])
            e2 = rngm.choice(exc_idx, 2 * n, replace=False)
            exc2.append(nj.decode(X[:, i1][:, e2], yc, rngm)["acc"])
    out["mixed"], out["exc2n"] = np.array(mixed), np.array(exc2)
    # fig7: real against pseudo population, all neurons, correct trials and all trials with a choice
    rngp = rng_for("pseudo", idx)
    out["pseudo"] = {}
    for trial_set, sel in (("correct", corr), ("all", ok)):
        yy = y[sel].astype(int)
        if min((yy == 1).sum(), (yy == 0).sum()) < nj.MIN_TRIALS:
            continue
        Xr = xb[sel][:, i1]
        real = nj.decode(Xr, yy, rngp)
        pseudo = nj.decode(nj.pseudo_population(Xr, yy, rngp), yy, rngp)
        out["pseudo"][trial_set] = dict(real=real["acc"], pseudo=pseudo["acc"],
                                        real_reps=real["acc_reps"], pseudo_reps=pseudo["acc_reps"])
    return out


N_MIXED = 10          # fig3hi subsamples (50 in the claims file; reduced for run time)
N_EXC_ANGLE = 1       # figs7c excitatory subsamples per bin (50 in the claims file; reduced)


# --- notebook 3: every bin of the choice-aligned traces ----------------------------------------

def decode_time_course(args):
    """fig3b (all neurons, every bin) and fig3df (mean |w| of each type, every bin)."""
    idx, path, url = args
    s = nj.load_session(path, url, groups=("choice",))
    types = s["types"]
    tm = _type_masks(types)
    xb, i1, tb, corr, ok = _choice_data(s, "correct")
    yc = s["trials"].choice_high.values[corr].astype(int)
    out = dict(idx=idx, path=path, mouse=s["mouse"], date=s["date"], bin_times=tb, i1=i1,
               n_inh=int(tm["inh"].sum()), n_exc=int(tm["exc"].sum()))
    out["ok"] = min((yc == 1).sum(), (yc == 0).sum()) >= nj.MIN_TRIALS and out["n_inh"] >= 2
    if not out["ok"]:
        return out
    X = xb[corr]
    nb = X.shape[1]
    rng = rng_for("timecourse", idx)
    acc, shfl, wabs_e, wabs_i = np.zeros(nb), np.zeros(nb), np.zeros(nb), np.zeros(nb)
    for b in range(nb):
        r = nj.decode(X[:, b], yc, rng)
        acc[b], shfl[b] = r["acc"], r["shfl"]
        w = r["w"] / np.linalg.norm(r["w"])
        wabs_e[b] = np.abs(w[tm["exc"]]).mean()
        wabs_i[b] = np.abs(w[tm["inh"]]).mean()
    out.update(acc_all=acc, shfl_all=shfl, wabs_exc=wabs_e, wabs_inh=wabs_i)
    return out


def decode_angles(args):
    """figs7c: angles between the weights of decoders trained at every pair of bins, for the
    inhibitory and a subsampled excitatory population of the same size."""
    idx, path, url = args
    s = nj.load_session(path, url, groups=("choice",))
    types = s["types"]
    tm = _type_masks(types)
    xb, i1, tb, corr, ok = _choice_data(s, "correct")
    yc = s["trials"].choice_high.values[corr].astype(int)
    out = dict(idx=idx, path=path, mouse=s["mouse"], date=s["date"], bin_times=tb, i1=i1,
               n_inh=int(tm["inh"].sum()))
    out["ok"] = min((yc == 1).sum(), (yc == 0).sum()) >= nj.MIN_TRIALS and out["n_inh"] >= 2
    if not out["ok"]:
        return out
    X = xb[corr]
    nb = X.shape[1]
    rnga = rng_for("angle", idx)
    inh = np.where(tm["inh"])[0]
    exc_sets = [np.sort(rnga.choice(np.where(tm["exc"])[0], len(inh), replace=False))
                for _ in range(N_EXC_ANGLE)]
    W_inh = np.stack([nj.decode(X[:, b][:, inh], yc, rnga)["w"] for b in range(nb)])
    W_exc = [np.stack([nj.decode(X[:, b][:, e], yc, rnga)["w"] for b in range(nb)]) for e in exc_sets]
    out["angles_inh"] = _angle_matrix(W_inh)
    out["angles_exc"] = np.mean([_angle_matrix(W) for W in W_exc], 0)
    return out


def _angle_matrix(W):
    nb = W.shape[0]
    A = np.full((nb, nb), np.nan)
    for a in range(nb):
        for b in range(nb):
            if a != b:
                A[a, b] = nj.angle(W[a], W[b])
    return A


# --- notebook 4: previous choice, stimulus category, outcome -----------------------------------

N_EXC_OTHER = 5       # excitatory subsamples for figs6ab and figs6c (50 in the claims file; reduced)


def _pop_decode(X, y, tm, rng, n_exc=N_EXC_OTHER, balance_groups=None):
    """All-neuron, inhibitory and subsampled excitatory decoders on one bin."""
    inh = np.where(tm["inh"])[0]
    exc = np.where(tm["exc"])[0]
    r_all = nj.decode(X, y, rng, balance_groups=balance_groups)
    r_inh = nj.decode(X[:, inh], y, rng, balance_groups=balance_groups)
    r_exc = [nj.decode(X[:, np.sort(rng.choice(exc, len(inh), replace=False))], y, rng,
                       balance_groups=balance_groups) for _ in range(n_exc)]
    return dict(all=r_all["acc"], all_shfl=r_all["shfl"], inh=r_inh["acc"], inh_shfl=r_inh["shfl"],
                exc=np.mean([r["acc"] for r in r_exc]), exc_shfl=np.mean([r["shfl"] for r in r_exc]),
                all_reps=r_all["acc_reps"], all_shfl_reps=r_all["shfl_reps"])


def decode_other(args):
    """figs6ab: previous choice and stimulus category."""
    idx, path, url = args
    s = nj.load_session(path, url, groups=("choice", "init", "stim"))
    tr, types = s["trials"], s["types"]
    tm = _type_masks(types)
    out = dict(idx=idx, path=path, mouse=s["mouse"], date=s["date"], n_inh=int(tm["inh"].sum()))
    if out["n_inh"] < 2:
        out["ok"] = False
        return out
    out["ok"] = True
    rng = rng_for("prev", idx)
    prev = np.r_[np.nan, tr.choice_high.values[:-1]]
    out["prev"] = {}
    for align in ("choice", "init"):
        g = s["groups"][align]
        xb, j1, _ = nj.bin_traces(g["x"], g["event"], g["period"])
        valid = nj.valid_trials(g["x"]) & np.isfinite(prev)
        for trial_set in ("correct", "all"):
            sel = valid & (tr.trial_response.eq("correct").values if trial_set == "correct"
                           else tr.decided.values)
            yy = prev[sel].astype(int)
            key = f"{align}_{trial_set}"
            if min((yy == 1).sum(), (yy == 0).sum()) < nj.MIN_TRIALS:
                continue
            out["prev"][key] = _pop_decode(xb[sel][:, j1], yy, tm, rng)
    # stimulus category: stimulus-aligned, equal left and right choices in each category, no 16 Hz
    rngs = rng_for("stim", idx)
    g = s["groups"]["stim"]
    xb, j1, tb = nj.bin_traces(g["x"], g["event"], g["period"])
    sel = nj.valid_trials(g["x"]) & tr.decided.values & ~tr.is16.values
    ys = tr.stim_high.values[sel].astype(int)
    ch = tr.choice_high.values[sel].astype(int)
    n_min = min(((ys == a) & (ch == b)).sum() for a in (0, 1) for b in (0, 1))
    out["stim_n_min_cell"] = int(n_min)
    out["stim"] = {}
    if n_min >= 3:
        # (a) the 3 frames before stimulus offset, located per trial from the trial table
        off = ((tr.stim_offset - tr.stim_onset).values[sel] / g["period"]).round().astype(int) + g["event"]
        xs = g["x"][sel]
        good = (off - 3 >= 0) & (off <= xs.shape[1])
        Xa = np.stack([xs[k, off[k] - 3:off[k]].mean(0) if good[k] else np.full(xs.shape[2], np.nan)
                       for k in range(len(off))])
        keep = good
        out["stim"]["offset"] = _pop_decode(Xa[keep], ys[keep], tm, rngs, balance_groups=ch[keep])
        out["stim_offset_dropped"] = int((~good).sum())
        # (b) the bin of peak all-neuron accuracy over the stimulus-aligned bins
        accs = np.array([nj.decode(xb[sel][:, b], ys, rngs, balance_groups=ch)["acc"]
                         for b in range(xb.shape[1])])
        bpk = int(np.argmax(accs))
        out["stim_all_by_bin"], out["stim_bin_times"], out["stim_peak_bin"] = accs, tb, bpk
        out["stim"]["peak"] = _pop_decode(xb[sel][:, bpk], ys, tm, rngs, balance_groups=ch)
    return out


def decode_outcome(args):
    """figs6c: outcome decoders aligned to the confirmation lick (reward for correct trials,
    the second commit of incorrect trials)."""
    idx, path, url = args
    s = nj.load_session(path, url, groups=("reward", "incorr"))
    tr, types = s["trials"], s["types"]
    tm = _type_masks(types)
    gr, gi = s["groups"]["reward"], s["groups"]["incorr"]
    before = min(gr["event"], gi["event"])
    after = min(gr["x"].shape[1] - gr["event"], gi["x"].shape[1] - gi["event"])
    xr = gr["x"][:, gr["event"] - before:gr["event"] + after]
    xi = gi["x"][:, gi["event"] - before:gi["event"] + after]
    cor = tr.trial_response.eq("correct").values & nj.valid_trials(xr)
    inc = tr.trial_response.eq("incorrect").values & nj.valid_trials(xi)
    x = np.where(cor[:, None, None], xr, xi)
    sel = cor | inc
    xb, i1, tb = nj.bin_traces(x[sel], before, gr["period"])
    yo = cor[sel].astype(int)
    ch = tr.choice_high.values[sel].astype(int)
    out = dict(idx=idx, path=path, mouse=s["mouse"], date=s["date"], bin_times=tb,
               n_correct=int(cor.sum()), n_incorrect=int(inc.sum()), n_inh=int(tm["inh"].sum()),
               rate_reward=gr["period"], rate_incorr=gi["period"])
    n_min = min(((yo == a) & (ch == b)).sum() for a in (0, 1) for b in (0, 1))
    out["n_min_cell"] = int(n_min)
    out["ok"] = n_min >= 3 and out["n_inh"] >= 2
    if not out["ok"]:
        return out
    rng = rng_for("outcome", idx)
    post = np.where(tb >= 0)[0]
    inh = np.where(tm["inh"])[0]
    exc = np.where(tm["exc"])[0]
    exc_sets = [np.sort(rng.choice(exc, len(inh), replace=False)) for _ in range(N_EXC_OTHER)]
    acc_all, acc_inh, acc_exc, sh_all = {}, {}, {}, {}
    k400 = np.where((tb <= 400) & (tb + 3 * gr["period"] * 1000 > 400))[0]
    for b in post:
        X = xb[:, b]
        if b in k400:
            r = nj.decode(X, yo, rng, balance_groups=ch)
            acc_all[int(b)], sh_all[int(b)] = r["acc"], r["shfl"]
        acc_inh[int(b)] = nj.decode(X[:, inh], yo, rng, balance_groups=ch)["acc"]
        acc_exc[int(b)] = np.mean([nj.decode(X[:, e], yo, rng, balance_groups=ch)["acc"] for e in exc_sets])
    out.update(acc_all=acc_all, shfl_all=sh_all, acc_inh=acc_inh, acc_exc=acc_exc,
               bin400=int(k400[0]) if len(k400) else None)
    return out


# --- notebooks 5: learning -------------------------------------------------------------------------

N_EXC_LEARN = 10      # fig8ab excitatory subsamples at 0-97 ms before choice (50 in the claims file)
N_EXC_ONSET = 1       # fig8ce excitatory subsamples at every bin (50 in the claims file)
N_EXC_PSEUDO = 5      # figs13ab excitatory subsamples


def _learning_trials(tr, ok, reading, rng):
    """Trials for the learning decoders: (a) all trials with a choice, (b) equal numbers of correct
    and incorrect trials within each choice (claims file, fig8ab-learning-accuracy)."""
    if reading == "a":
        return np.where(ok)[0]
    y = tr.choice_high.values
    c = tr.trial_response.eq("correct").values
    groups = [np.where(ok & (y == v) & (c == w))[0] for v in (0, 1) for w in (True, False)]
    k = min(len(g) for g in groups)
    return np.sort(np.concatenate([rng.choice(g, k, replace=False) for g in groups]))


def decode_learning(args):
    """fig8ab, fig8ce, figs13c, figs13ab, figs12 (running)."""
    idx, path, url = args
    s = nj.load_session(path, url, groups=("choice",), behaviour=True)
    tr, types = s["trials"], s["types"]
    tm = _type_masks(types)
    g = s["groups"]["choice"]
    ok = nj.valid_trials(g["x"]) & tr.decided.values
    xb, i1, tb = nj.bin_traces(g["x"], g["event"], g["period"])
    y = tr.choice_high.values
    out = dict(idx=idx, path=path, mouse=s["mouse"], date=s["date"], bin_times=tb, i1=i1,
               performance=easy_performance(tr), n_inh=int(tm["inh"].sum()),
               n_correct=int(tr.trial_response.eq("correct").sum()), readings={})
    inh = np.where(tm["inh"])[0]
    exc = np.where(tm["exc"])[0]
    rng = rng_for("learn", idx)
    rngo = rng_for("learn_onset", idx)
    rngp = rng_for("learn_pseudo", idx)
    for reading in ("a", "b"):
        sel = _learning_trials(tr, ok, reading, rng)
        yy = y[sel].astype(int)
        res = dict(n_trials=len(sel), n_left=int((yy == 1).sum()), n_right=int((yy == 0).sum()))
        res["ok"] = min(res["n_left"], res["n_right"]) >= nj.MIN_TRIALS and len(inh) >= 2
        if res["ok"]:
            X = xb[sel]
            # fig8ab: bin -1
            d = _pop_decode(X[:, i1], yy, tm, rng, n_exc=N_EXC_LEARN)
            res["bin1"] = {k: v for k, v in d.items() if not k.endswith("_reps")}
            # fig8ce: every bin; accuracy against the shuffle by a t-test across the repetitions
            e_sets = [np.sort(rngo.choice(exc, len(inh), replace=False)) for _ in range(N_EXC_ONSET)]
            p = {"all": [], "inh": [], "exc": []}
            acc = {"all": [], "inh": [], "exc": []}
            for b in range(X.shape[1]):
                for name, cols in (("all", np.arange(len(types))), ("inh", inh)):
                    r = nj.decode(X[:, b][:, cols], yy, rngo)
                    p[name].append(_ttest_p(r["acc_reps"], r["shfl_reps"]))
                    acc[name].append(r["acc"])
                re = [nj.decode(X[:, b][:, e], yy, rngo) for e in e_sets]
                p["exc"].append(_ttest_p(np.concatenate([r["acc_reps"] for r in re]),
                                            np.concatenate([r["shfl_reps"] for r in re])))
                acc["exc"].append(np.mean([r["acc"] for r in re]))
            res["p_bins"] = {k: np.array(v) for k, v in p.items()}
            res["acc_bins"] = {k: np.array(v) for k, v in acc.items()}
            # figs13ab: pseudo populations at bin -1
            Xp = nj.pseudo_population(X[:, i1], yy, rngp)
            d = _pop_decode(Xp, yy, tm, rngp, n_exc=N_EXC_PSEUDO)
            res["pseudo"] = {k: v for k, v in d.items() if not k.endswith("_reps")}
        out["readings"][reading] = res
    # figs13c: correct trials at 0-97 ms before the choice, kept for the equal-trials decoders
    corr = ok & tr.trial_response.eq("correct").values
    out["X1_correct"] = xb[corr][:, i1].astype(np.float32)
    out["y1_correct"] = y[corr].astype(int)
    # figs12: running in the bin 0-97 ms before the choice, two readings of "running distance"
    wt, wx = s["wheel"]["t"], s["wheel"]["x"]
    w0 = np.argmin(np.abs(wt - 0.0))
    wm = np.argmin(np.abs(wt + 0.097))
    disp = np.abs(wx[w0] - wx[wm])
    mean_ = np.nanmean(wx[(wt >= -0.097) & (wt < 0)], 0)
    out["wheel"] = dict(disp=disp, mean=mean_, choice=y, ok=ok, t_step=float(np.median(np.diff(wt))))
    # licks (all spouts; the file does not say which spout) in the 250 ms before the choice
    lt, lx = s["lick"]["t"], s["lick"]["x"]
    win = (lt >= -0.25) & (lt < 0)
    out["lick"] = dict(t=lt[win], x=lx[win], choice=y, ok=ok)
    return out


def decode_equal_trials(args):
    """figs13c: correct trials only, the same number of trials of each choice in every session of
    a mouse (the minimum over its sessions; code, same_HRLR_acrossDays)."""
    idx, X, y, n_per_choice = args
    rng = rng_for("equal", idx)
    sel = np.sort(np.r_[rng.choice(np.where(y == 1)[0], n_per_choice, replace=False),
                        rng.choice(np.where(y == 0)[0], n_per_choice, replace=False)])
    r = nj.decode(X[sel].astype(float), y[sel], rng)
    return dict(idx=idx, acc=r["acc"], shfl=r["shfl"], n=len(sel))


def _ttest_p(acc, shfl):
    """Two-tailed t-test of accuracy against the shuffle across repetitions; the p-value, signed
    negative when accuracy is below the shuffle."""
    from scipy import stats
    t, p = stats.ttest_ind(acc, shfl)
    return p if t >= 0 else -p
