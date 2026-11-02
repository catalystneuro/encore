"""Head-fixed mouse eyepuff behaviour of dandiset 001347 (Kauvar, Richman, Liu et al. 2025).

Two kinds of file are read, streamed through dandi_io (nothing is written to disk):

- sub-mouse/sub-mouse_ses-<experiment id>_behavior.nwb: one TimeSeries acquisition/eye_closure
  at 200 Hz, trials of 81 s (16200 frames, 6 s before the first puff) concatenated, 20 or 40
  trials. The files carry no drug, dose, mouse, sex, day or pressure. Those labels come from the
  experiment lists of the paper's scripts mouse_eyepuff/scripts/fig1_*.py in the code record
  (Zenodo 10.5281/zenodo.14920570, kauvar-richman-liu-2025_zenodo.zip, md5
  bd1fb567121aaf0291337783df57bcfc, git commit b873ca5), read at run time by `code_lists`.
- sub-m<mouse>-<id>/..._ses-puff_behavior.nwb: Neuropixels-rig behaviour (DeepLabCut eye
  closure at 100 Hz, trial onsets `events-on`, `ket_trial`, stored trial ranges and windows).

The processing reimplements ketmouse/eye_trace_utils.py of the code record (not imported):

- `prox_norm`: each trial minus its mean over frames 0 to 399 (the first 2 s, 6 to 4 s before
  the first puff); eye_trace_utils.prox_norm, used with do_prox_norm=True by every fig1 script.
- `scale`: get_mean_traces then subtracts the mean of the first 400 frames of `baseline_trial`
  of the prox-normed data, which is zero, and scales by 1/(1 - that), which is one. The Methods
  ("Eyepuff assay (mouse)") instead scale by 1/(1 - baseline) with the raw pre-trial baseline
  averaged over the first two trials. `methods_scale` gives that factor; it changes absolute
  early and late values, never late/early.
- Windows: early 0.1 to 0.2 s, late 0.3 to 0.8 s after a puff (claims file M-EYE; fig1 scripts
  ref_w, aff_w); frame indices int(200 * (6 + t)) as in the scripts (`window`). Puff k (0 to 7)
  is at 3k s.
- Late/early per mouse: get_data_by_trial with mean_ref=True divides each trial's late value
  by the mean over trials of early, and plot_drug_comparison_bar_from_df averages over trials:
  mean(late) / mean(early) (`per_mouse`).
- Decay fit: fit_exponential_decay, a*exp(-b*x) + c with scipy.optimize.curve_fit (default
  initial values) on the trial-mean trace from 21.2 to 23.2 s (claims file, fig1no).
- Persistence: fig1_persistence.py (claims file, fig1m).
- Neuropixels-rig traces: make_puffseries_behavior_plot in analysis.py of Zenodo
  10.5281/zenodo.14876694 (md5 6cc7aa5059737c3bd753aad1f116019d): first puff 5 s after each
  `events-on`, puffs 3 s apart, 1 s before to 2 s after each puff (5 s more after the eighth),
  minus the mean of the 1 s before the first puff, trials 0 to 19 preinfusion and 22 to 31
  ketamine, each session's mean trace divided by its maximum (`npx_series`).
"""
from __future__ import annotations

import ast
import hashlib
import io
import zipfile
from concurrent.futures import ThreadPoolExecutor

import numpy as np
import requests

import dandi_io

CODE_URL = ("https://zenodo.org/api/records/14920570/files/"
            "kauvar-richman-liu-2025_zenodo.zip/content")
CODE_MD5 = "bd1fb567121aaf0291337783df57bcfc"
SCRIPTS = "kauvar-richman-liu-2025_zenodo/mouse_eyepuff/scripts/"

FPS = 200                 # file rate attribute; fig1 scripts fps = 200
FRAMES_PER_TRIAL = 16200  # eye_trace_utils.load_files_nwb
PRE_S = 6                 # seconds of each trial window before the first puff (t = arange/fps - 6)
BASE_FRAMES = 400         # prox_norm and baseline_frames in every fig1 script
EARLY = (0.1, 0.2)        # ref_w, claims file M-EYE
LATE = (0.3, 0.8)         # aff_w, claims file M-EYE
PUFF_TIMES = np.arange(0, 24, 3)   # eight puffs, 3 s apart (Methods)
# Trial selections (0-based), fig1_drugs.py which_pre / which_post (claims file M-EYE, Open I a)
PRE_CODE = np.arange(5, 20)
POST_CODE = np.arange(22, 37)
# Open I reading (b) as run here: every post trial from the third after the injection on
# (fig. S2B and S2C legends: 18 trials), with the 18 last preinfusion trials (3 to 20).
PRE_B = np.arange(2, 20)
POST_B = np.arange(22, 40)
# 20-trial sessions, fig1_psi.py and fig1_muscimol.py which_pre = which_post = arange(2, 17)
TRIALS_20 = np.arange(2, 17)


# ---------------------------------------------------------------- code record
def fetch_code_zip() -> zipfile.ZipFile:
    """Fetch the code record from Zenodo into memory and check its md5."""
    r = requests.get(CODE_URL, timeout=120)
    r.raise_for_status()
    md5 = hashlib.md5(r.content).hexdigest()
    if md5 != CODE_MD5:
        raise ValueError(f"code zip md5 {md5} != {CODE_MD5}")
    return zipfile.ZipFile(io.BytesIO(r.content))


def literal_assignments(source: str) -> dict:
    """Every `name = <literal>` in a script (any depth), the last one winning."""
    out = {}
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, ast.Assign) and len(node.targets) == 1 \
                and isinstance(node.targets[0], ast.Name):
            try:
                out[node.targets[0].id] = ast.literal_eval(node.value)
            except ValueError:
                pass
    return out


def code_lists(zf: zipfile.ZipFile) -> dict:
    """Literal assignments (experiments, ntrials, SKIP_PUFFS, expids, ...) of each fig1 script."""
    names = ["fig1_drugs", "fig1_drugs_first_puff", "fig1_dose", "fig1_psi", "fig1_days",
             "fig1_sex", "fig1_muscimol", "fig1_persistence", "fig1_skippuff",
             "fig1_npx_behavior", "convert_npx_mouse_airpuff_to_nwb"]
    return {n: literal_assignments(zf.read(SCRIPTS + n + ".py").decode()) for n in names}


# ---------------------------------------------------------------- loading
def mouse_path(expid) -> str:
    return f"sub-mouse/sub-mouse_ses-{expid}_behavior.nwb"


def mouse_ids() -> list[int]:
    """Experiment ids of the sub-mouse files at the pinned version."""
    return sorted(int(p.split("ses-")[1].split("_")[0])
                  for p in dandi_io.list_assets() if p.startswith("sub-mouse/"))


def _load_one(expid):
    with dandi_io.open_h5(mouse_path(expid)) as f:
        ts = f["acquisition/eye_closure"]
        x = ts["data"][:]
        meta = {"rate": float(ts["starting_time"].attrs["rate"]),
                "unit": ts["data"].attrs["unit"],
                "identifier": f["identifier"][()].decode(),
                "subject_id": f["general/subject/subject_id"][()].decode(),
                "sex": f["general/subject/sex"][()].decode(),
                "age": f["general/subject/age"][()].decode(),
                "subject_description": f["general/subject/description"][()].decode(),
                "session_description": f["session_description"][()].decode()}
    return expid, x, meta


def load_all(ids, workers=8):
    """{expid: eye closure array}, {expid: metadata} for the given experiment ids."""
    with ThreadPoolExecutor(workers) as ex:
        res = list(ex.map(_load_one, ids))
    return {e: x for e, x, _ in res}, {e: m for e, _, m in res}


def trials(x, ntrials):
    """[ntrials, 16200] from the first ntrials trials (load_files_nwb truncates likewise)."""
    return x[:FRAMES_PER_TRIAL * ntrials].reshape(ntrials, FRAMES_PER_TRIAL)


def prox_norm(tr):
    return tr - tr[:, :BASE_FRAMES].mean(1, keepdims=True)


def methods_scale(tr_raw):
    """Methods reading: 1/(1 - baseline), baseline the raw first 2 s averaged over trials 1-2."""
    return 1.0 / (1.0 - tr_raw[:2, :BASE_FRAMES].mean())


def window(tpuff, w):
    """Frame slice of window w (s) after a puff at tpuff (s), as the fig1 scripts compute it."""
    a = (FPS * (PRE_S + np.array([tpuff + w[0], tpuff + w[1]]))).astype(int)
    return slice(a[0], a[1])


def per_mouse(tr, tpuff, w_late=LATE, w_early=EARLY):
    """Per-mouse late, early and late/early (= mean late / mean early) over the given trials."""
    late = tr[:, window(tpuff, w_late)].mean(1)
    early = tr[:, window(tpuff, w_early)].mean(1)
    return {"late": late.mean(), "early": early.mean(),
            "ratio": np.mean(late / early.mean())}


def condition_values(data, ids, ntrials, sel_pre, sel_post, tpuff, scale="code",
                     w_early=EARLY):
    """Arrays over mice (list order) of pre and post late, early, ratio."""
    out = {f"{ph}_{m}": [] for ph in ("pre", "post") for m in ("late", "early", "ratio")}
    for e in ids:
        raw = trials(data[e], ntrials)
        tr = prox_norm(raw)
        if scale == "methods":
            tr = tr * methods_scale(raw)
        for ph, sel in (("pre", sel_pre), ("post", sel_post)):
            v = per_mouse(tr[sel], tpuff, w_early=w_early)
            for m in ("late", "early", "ratio"):
                out[f"{ph}_{m}"].append(v[m])
    return {k: np.array(v) for k, v in out.items()}


def mean_trace(data, e, ntrials, sel):
    """Trial-mean prox-normed trace of one session (get_mean_traces with agg_fn=np.mean)."""
    return prox_norm(trials(data[e], ntrials))[sel].mean(0)


def fit_decay(trace, t_start=21.2, t_end=23.2):
    """fit_exponential_decay: a*exp(-b*x)+c on [t_start, t_end); returns b (1/s) or nan."""
    from scipy.optimize import curve_fit
    t = np.arange(len(trace)) / FPS - PRE_S
    i0, i1 = np.searchsorted(t, t_start), np.searchsorted(t, t_end)
    try:
        popt, _ = curve_fit(lambda x, a, b, c: a * np.exp(-b * x) + c,
                            t[i0:i1] - t_start, trace[i0:i1], maxfev=10000)
        return popt[1]
    except RuntimeError:
        return np.nan


def survival_times(tr_raw, start_s, thresh=1.2, censor_s=50.0):
    """fig1_persistence.py: time from the start frame to the first frame not above
    thresh * (mean of the trial's first 5 s); trials never reopening censored at censor_s.
    start_s is seconds into the 81-s window (code: 6 + 24 + 0.3 = 30.3)."""
    i0 = int(FPS * start_s)
    base = tr_raw[:, :FPS * 5].mean(1, keepdims=True)
    closed = tr_raw > thresh * base
    first = closed[:, i0:].argmin(1).astype(float)
    never = closed[:, i0:].min(1) == 1
    first[never] = FPS * censor_s
    return first / FPS, (~never).astype(int)


# ---------------------------------------------------------------- Neuropixels rig
def npx_paths():
    return sorted(p for p in dandi_io.list_assets()
                  if p.startswith("sub-m") and not p.startswith("sub-mouse"))


def npx_load(path):
    """Every acquisition of a Neuropixels-rig behaviour file as arrays."""
    out = {}
    with dandi_io.open_h5(path) as f:
        for k, g in f["acquisition"].items():
            out[k] = g["data"][()]
        out["subject_id"] = f["general/subject/subject_id"][()].decode()
    return out


def npx_series(b, first_only=False, max_norm=True, pre=slice(0, 20), ket=slice(22, 32)):
    """make_puffseries_behavior_plot (analysis.py, Zenodo 14876694): per-trial series traces,
    baseline the mean of the 1 s before the first puff; returns (t, pre mean, ket mean, per-trial
    array). With max_norm each condition's mean trace is divided by its own maximum."""
    fps = int(b["fps"][0])
    on = b["events-on"] + 5 * fps
    ec = b["eyeclosure"]
    per_trial = []
    for o in on[:40]:
        segs = []
        for k in range(1 if first_only else 8):
            p = int(o + k * 3 * fps)
            extra = 5 * fps if (k == 7) else 0
            segs.append(ec[p - fps: p + 2 * fps + extra])
        per_trial.append(np.concatenate(segs) - np.nanmean(segs[0][:fps]))
    per_trial = np.stack(per_trial)
    m_pre = np.nanmean(per_trial[pre], 0)
    m_ket = np.nanmean(per_trial[ket], 0)
    if max_norm:
        m_pre, m_ket = m_pre / np.nanmax(m_pre), m_ket / np.nanmax(m_ket)
    t = np.arange(per_trial.shape[1]) / fps - 1   # time from the first puff for the first segment
    return t, m_pre, m_ket, per_trial
