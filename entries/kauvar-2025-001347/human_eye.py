"""Human eye closure and CADSS for Kauvar, Richman, Liu et al. 2025 (DANDI:001347).

Loads the eyepuff behaviour of the non-iEEG cohort (sub-h*/..._ses-P50_behavior.nwb) and of the
iEEG cohort (sub-SD*/..._ses-puff_behavior.nwb), streamed through dandi_io, and computes the
early (reflexive) and late (affective) eye closure of the claims file's method H-EYE.

Where each parameter comes from
- Early window 0.1 to 0.2 s and late window 0.3 to 0.8 s after the puff: claims file, H-EYE
  (Fig. 1 legend, fig. S1B and S1C legends). The iEEG files also store them (ref_w, aff_w).
- Non-iEEG cohort: trials 3 to 40 (0-based 2 to 39), the late/early value of a participant is
  the mean over trials of late divided by the mean over trials of early: claims file, H-EYE and
  Open A reading (a), Open B reading (a). Reading (b) of Open A keeps trials 2 to 40; reading (b)
  of Open B takes the mean of per-trial ratios. In the P50 code the window masks are strict
  (tt > 0.3 and tt < 0.8; analyze_airpuff_p50.py), which is followed here.
- Which P50 series is saline: the files call the two series `pre_trials_data` and
  `post_trials_data` and do not say which visit is saline. The paper's code reads `pre` as
  saline and `post` as ketamine (analyze_airpuff_p50.py builds the `treatment` column so). This
  label comes from the code record (an outside input, with_labels; link claim
  p50-condition-labels-link).
- iEEG cohort: the per-trial late/early ratio and the trials listed in each file's
  `which_trials` (claims file, H-EYE; Table S3, fig. S8A). The session called `baseline` in the
  files of SD168, SD172, SD242 and SD245 is used as the preinfusion session, as the code does
  (airpuff_utils.load_airpuff_behavior renames baseline to preinfusion).
- iEEG traces: each trial window is 800 samples at 200 Hz with the puff at sample 400
  (by_trial_closure; the code asserts puff_ind == 400). Index windows are
  int(200 * (2 + w)) as in airpuff_utils.get_pt_eyeclosure.
- CADSS: the scores are not in the dataset. iEEG cohort, data/cadss_across_pts.csv of the code
  record; infusion is the maximum over the time points up to 50 min, postinfusion the 110 min
  point, and SD185's retrospective rating replaces its infusion rating (claims file, fig2d;
  code utils.load_full_cadss). Non-iEEG cohort, the constants of analyze_airpuff_p50.py (claims
  file, figs1d).
"""
import hashlib
import io
import zipfile

import numpy as np
import pandas as pd
import requests

import dandi_io

FPS = 200
EARLY_W = (0.1, 0.2)
LATE_W = (0.3, 0.8)
P50_SUBJECTS = ["h009", "h011", "h012", "h013"]
IEEG_SUBJECTS = ["SD163", "SD168", "SD170", "SD172", "SD178", "SD181", "SD184", "SD185",
                 "SD186", "SD207", "SD211", "SD215", "SD242", "SD245"]
INCLUDED = ["SD168", "SD172", "SD181", "SD185", "SD186", "SD211", "SD245"]
SESSIONS = ["preinfusion", "infusion", "postinfusion"]

CODE_URL = ("https://zenodo.org/api/records/14920570/files/"
            "kauvar-richman-liu-2025_zenodo.zip/content")
CODE_MD5 = "bd1fb567121aaf0291337783df57bcfc"
CODE_ROOT = "kauvar-richman-liu-2025_zenodo/"


def load_p50(subject):
    """Return (tt, pre, post) for a non-iEEG participant; pre and post are trials x samples."""
    h = dandi_io.open_h5(f"sub-{subject}/sub-{subject}_ses-P50_behavior.nwb")
    acq = h["acquisition"]
    tt = acq["time_reference/tt/data"][:]
    out = []
    for part in ["pre", "post"]:
        grp = acq[f"{part}_trials_data"]
        n = len(grp.keys())
        out.append(np.vstack([grp[f"{part}_trial_{i + 1}/data"][:] for i in range(n)]))
    return tt, out[0], out[1]


def p50_values(tt, trials, trial_idx, ratio="ratio_of_means"):
    """Early, late and late/early of one series of the non-iEEG cohort.

    ratio="ratio_of_means": mean late over trials / mean early over trials (code, mean_ref=True).
    ratio="mean_of_ratios": mean over trials of late / early of the same trial.
    """
    late_m = (tt > LATE_W[0]) & (tt < LATE_W[1])
    early_m = (tt > EARLY_W[0]) & (tt < EARLY_W[1])
    late = np.nanmean(trials[trial_idx][:, late_m], axis=1)
    early = np.nanmean(trials[trial_idx][:, early_m], axis=1)
    if ratio == "ratio_of_means":
        r = np.mean(late) / np.mean(early)
    else:
        r = np.mean(late / early)
    return np.mean(early), np.mean(late), r


def load_ieeg_behavior(subject):
    """Return a dict with the iEEG participant's behaviour.

    Keys: which_trials, and per session (preinfusion, infusion, postinfusion): trials
    (n_trials x 800 eye closure), affective, reflexive, affective_normed (stored per-trial
    values), events_on (frame of each puff), eyeclosure (continuous trace), the file's session
    name.
    """
    h = dandi_io.open_h5(f"sub-{subject}/sub-{subject}_ses-puff_behavior.nwb")
    acq = h["acquisition"]
    names = sorted({k.split("-", 1)[1].replace("_puffeye", "") for k in acq
                    if k.startswith("by_trial_closure-")})
    out = {"which_trials": acq["which_trials/data"][:],
           "aff_w": acq["aff_w/data"][:], "ref_w": acq["ref_w/data"][:],
           "fps": float(acq["fps/data"][0])}
    for name in names:
        sess = name.replace("baseline", "preinfusion")
        out[sess] = {
            "file_session": name,
            "trials": acq[f"by_trial_closure-{name}_puffeye/data"][:].T,
            "affective": acq[f"affective-{name}_puffeye/data"][:],
            "reflexive": acq[f"reflexive-{name}_puffeye/data"][:],
            "affective_normed": acq[f"affective_normed-{name}_puffeye/data"][:],
            "events_on": acq[f"events-{name}_puffeye-on/data"][:],
            "events_off": acq[f"events-{name}_puffeye-off/data"][:],
            "eyeclosure": acq[f"eyeclosure-{name}_puffeye/data"][:],
        }
    return out


def window_mean(trials, w, shift_s=0.0):
    """Mean of each trial over window w (s after the puff at sample 400), as the code indexes.

    shift_s moves the window later, for the code's plotting origin shift (origin_shift_s).
    """
    a = int(FPS * (2 + w[0] + shift_s))
    b = int(FPS * (2 + w[1] + shift_s))
    return np.nanmean(trials[:, a:b], axis=1)


def per_trial(beh, sess, trial_idx=None):
    """Per-trial early, late and late/early of an iEEG session, recomputed from the traces."""
    if trial_idx is None:
        trial_idx = beh["which_trials"]
    tr = beh[sess]["trials"][trial_idx]
    early = window_mean(tr, EARLY_W)
    late = window_mean(tr, LATE_W)
    return pd.DataFrame({"trial": trial_idx, "early": early, "late": late,
                         "late_over_early": late / early})


@__import__("functools").lru_cache(maxsize=1)
def code_zip():
    """The paper's code record (Zenodo 14920570), fetched in memory, md5 checked."""
    r = requests.get(CODE_URL, timeout=300)
    r.raise_for_status()
    md5 = hashlib.md5(r.content).hexdigest()
    if md5 != CODE_MD5:
        raise ValueError(f"code record md5 {md5} differs from {CODE_MD5}")
    return zipfile.ZipFile(io.BytesIO(r.content))


def code_text(path):
    return code_zip().read(CODE_ROOT + path).decode()


def p50_code_labels():
    """The code's P50 subject list, (session name, treatment), and CADSS constants.

    Parsed from human_ieeg/scripts/analyze_airpuff_p50.py of the code record.
    """
    import ast
    src = code_text("human_ieeg/scripts/analyze_airpuff_p50.py")
    tree = ast.parse(src)
    found = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and \
                isinstance(node.targets[0], ast.Name) and node.targets[0].id in ("subjects", "cadss"):
            found[node.targets[0].id] = ast.literal_eval(node.value)
    return found["subjects"], found["cadss"]


def load_cadss():
    """Total CADSS per iEEG participant (pre, infusion, post, retro), from the code record's csv.

    Follows utils.load_full_cadss: infusion is the maximum over the columns 'N min' with
    N <= 50, post the 110 min column, retro any column containing 'retro'.
    """
    df = pd.read_csv(io.BytesIO(code_zip().read(CODE_ROOT + "data/cadss_across_pts.csv")),
                     header=[0, 1])
    qs = df.iloc[:, 0].astype(str).str.strip()
    total_row = np.where(qs == "TOTAL")[0]
    if len(total_row) != 1:
        raise ValueError("no single TOTAL row in the CADSS table")
    t = total_row[0]
    rows = []
    for pt in sorted({c[0] for c in df.columns[1:]}):
        sub = df[pt]
        cols = [str(c).strip() for c in sub.columns]
        vals = {c: pd.to_numeric(sub.iloc[t, i], errors="coerce") for i, c in enumerate(cols)}

        def minutes(c):
            p = c.split(" ")
            return int(p[0]) if p[0].isnumeric() and p[-1].startswith("min") else None
        inf_cols = [c for c in cols if minutes(c) is not None and minutes(c) <= 50]
        post_cols = [c for c in cols if minutes(c) == 110]
        retro_cols = [c for c in cols if "retro" in c]
        rows.append({
            "pt": pt,
            "pre": vals.get("Before Ket", np.nan),
            "infusion": np.nanmax([vals[c] for c in inf_cols]) if inf_cols else np.nan,
            "post": np.nanmax([vals[c] for c in post_cols]) if post_cols else np.nan,
            "retro": np.nanmax([vals[c] for c in retro_cols]) if retro_cols else np.nan,
            "columns": ", ".join(cols),
        })
    return pd.DataFrame(rows).set_index("pt")
