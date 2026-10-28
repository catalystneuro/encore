"""Loading and measures for Gillon, Lecoq et al. (2023), Scientific Data 10, 287.

The target dataset is DANDI:000336 (the OpenScope "Dendritic Coupling" project), which names the paper
but does not hold its recordings. The paper's data are on DANDI:000037 (the OpenScope "Credit
Assignment" project), which the claims file names for every finding (`data: elsewhere`). This module
lists both and streams the basic files of 000037 (`_behavior+ophys.nwb`), reading only the arrays the
analysis needs with h5py.

Where each parameter comes from:

- Sessions analysed: sessions 1 to 3 that passed QC, 11 mice and 33 sessions (claims file, opening
  comment, from run_paper_figures.py and mouse_df.csv of the paper's code). Session numbers and QC
  come from mouse_df.csv of the paper's code at commit CODE_COMMIT, an input listed in the attempt;
  the files carry neither.
- SNR and signal: `calculate_snr` of the paper's code (github.com/colleenjg/util at commit
  2b05f954, util/math_util.py), as the claims file states: values at or below the median, mirrored
  about it, give the noise mean and SD; the threshold is the noise distribution's 95th percentile;
  signal is the mean of values above it; SNR is signal over noise SD.
- Correlations: Pearson correlations over all ROI pairs of the whole-session dF/F traces after a
  4-sample rolling mean (`rolling_mean`, scipy.ndimage.convolve with mode "mirror", as in the same
  file), ROIs with NaN or Inf values removed (claims file, fig7c-correlations-similar).
- Onsets and offsets: onsets are the ends of every grey-screen period but the last, offsets the
  starts of every grey-screen period but the first, 2 s before and 2 s after (claims file,
  fig9-onset-offset-transients). Event frames are the trial table's `start_frame_twop` (onset of a
  stimulus row) and `stop_frame_twop` of the stimulus row before a grey period, which is the
  frame mapping the table provides. 60 frames is 2 s at the 30 Hz of the Methods.
- Scaling: the paper's code scales ROI traces by default for the onset, offset and Fig. 5 analyses
  (paper_organization.py, get_specific_params scale=True), as (trace - median) / (95th - 5th
  percentile) (analysis/session.py, scale_facts with sc_type "stand_rob", extrem "perc"). The
  claims file uses unscaled dF/F; the scaled traces are shown as a variant.
- Fig. 5 windows: 0.9 s before to 0.6 s after D or U onset, and 2 s before to 2 s after
  inconsistent flow onset (claims file, from paper_organization.py). The ROI selection of reading
  (b) follows the Fig. 5 legends as the claims file gives them; the four-point moving average of
  single responses is the code's rolling_mean (win 4).
- Running: median filter of 5 frames, frames with a single-frame change of at least 50 cm/s
  dropped; pupil: frames with a single-frame change of at least 0.05 mm dropped (Methods, Running
  and pupil tracking).
"""

from __future__ import annotations

import io
import os

import h5py
import numpy as np
import pandas as pd
import remfile
import requests
import scipy.ndimage
import scipy.stats

API = "https://api.dandiarchive.org/api"
TARGET_DANDISET, TARGET_VERSION = "000336", "0.260325.1802"   # the target, the only published version
DANDISET, VERSION = "000037", "0.230426.0054"                 # the paper's data, the version the claims file names
CODE_COMMIT = "046e7fef5f452cdc0775fe54040b0f13aeae1e57"      # github.com/colleenjg/OpenScope_CA_Analysis
MOUSE_DF_URL = ("https://raw.githubusercontent.com/colleenjg/OpenScope_CA_Analysis/"
                f"{CODE_COMMIT}/mouse_df.csv")
FPS = 30            # imaging rate of the Methods; windows below are in frames at this rate
PRE = POST = 60     # 2 s before and after onsets and offsets (claims file, fig9)

TRIAL_COLUMNS = ["start_time", "stop_time", "stimulus_type", "stimulus_template_name", "unexpected",
                 "gabor_frame", "main_flow_direction", "square_proportion_flipped",
                 "start_frame_twop", "stop_frame_twop"]


def get_json(url):
    r = requests.get(url)
    r.raise_for_status()
    return r.json()


def list_assets(dandiset=DANDISET, version=VERSION):
    """Every asset of a published version, as a DataFrame (path, size, asset_id)."""
    url = f"{API}/dandisets/{dandiset}/versions/{version}/assets/?page_size=1000"
    rows = []
    while url:
        page = get_json(url)
        rows += [{"path": a["path"], "size": a["size"], "asset_id": a["asset_id"]} for a in page["results"]]
        url = page["next"]
    return pd.DataFrame(rows)


def version_metadata(dandiset, version):
    return get_json(f"{API}/dandisets/{dandiset}/versions/{version}/")


def s3_url(asset_id):
    """The S3 address the archive's download link redirects to."""
    r = requests.head(f"{API}/assets/{asset_id}/download/", allow_redirects=False)
    r.raise_for_status()
    return r.headers["Location"]


def open_h5(asset_id):
    return h5py.File(remfile.File(s3_url(asset_id)), "r")


def read_mouse_df():
    """The session table of the paper's code (mouse_df.csv at CODE_COMMIT): session numbers and QC."""
    r = requests.get(MOUSE_DF_URL)
    r.raise_for_status()
    return pd.read_csv(io.StringIO(r.text))


def _str(x):
    return x.decode() if isinstance(x, bytes) else str(x)


def trials_table(f):
    """The trial (stimulus parameter) table, the columns the analysis uses."""
    g = f["intervals/trials"]
    out = {}
    for c in TRIAL_COLUMNS:
        v = g[c][:]
        out[c] = [_str(x) for x in v] if v.dtype.kind in "OS" else v
    return pd.DataFrame(out)


def session_metadata(f):
    """Subject, session, plane and stream summaries of one open file, without the ROI traces."""
    rrs = f["processing/ophys/DfOverF/RoiResponseSeries"]
    ts = rrs["timestamps"][:]
    plane = f["general/optophysiology"][list(f["general/optophysiology"].keys())[0]]
    ps = f["processing/ophys/ImageSegmentation/PlaneSegmentation"]
    # untracked sessions have no tracking_id column ("ROI tracking indices, for tracked sessions", Data Records)
    has_tracking = "tracking_id" in ps
    tracking = ps["tracking_id"][:] if has_tracking else np.full(ps["id"].shape[0], np.nan)
    run = f["processing/behavior/BehavioralTimeSeries/running_velocity"]
    pup = f["processing/behavior/PupilTracking/pupil_diameter"]
    run_t, pup_t = run["timestamps"][:], pup["timestamps"][:]
    subj = f["general/subject"]
    return {
        "subject_id": _str(subj["subject_id"][()]),
        "sex": _str(subj["sex"][()]),
        "genotype": _str(subj["genotype"][()]),
        "age": _str(subj["age"][()]),
        "session_id": _str(f["general/session_id"][()]),
        "session_start_time": _str(f["session_start_time"][()]),
        "location": _str(plane["location"][()]),
        "imaging_rate": float(plane["imaging_rate"][()]),
        "dff_shape": rrs["data"].shape,
        "dff_unit": rrs["data"].attrs.get("unit"),
        "n_rois": int(ps["id"].shape[0]),
        "n_tracked": int(np.sum(~np.isnan(tracking))), "has_tracking_column": has_tracking,
        "tracking_ids": tracking,
        "max_projection_shape": f["processing/ophys/PlaneImages/max_projection"].shape,
        "twop_timestamps": ts, "twop_first": float(ts[0]), "twop_last": float(ts[-1]), "twop_n": len(ts),
        "twop_median_dt": float(np.median(np.diff(ts))),
        "run_unit": _str(run["data"].attrs.get("unit")), "run_n": len(run_t),
        "run_first": float(run_t[0]), "run_last": float(run_t[-1]),
        "run_median_dt": float(np.median(np.diff(run_t))),
        "pupil_unit": _str(pup["data"].attrs.get("unit")), "pupil_n": len(pup_t),
        "pupil_first": float(pup_t[0]), "pupil_last": float(pup_t[-1]),
    }


def behaviour(f):
    """Running velocity and pupil diameter, cleaned as in the Methods (Running and pupil tracking)."""
    run = f["processing/behavior/BehavioralTimeSeries/running_velocity/data"][:]
    run_f = scipy.ndimage.median_filter(run, size=5, mode="nearest")
    run_keep = np.ones(len(run_f), bool)
    run_keep[1:] = np.abs(np.diff(run_f)) < 50
    pup = f["processing/behavior/PupilTracking/pupil_diameter/data"][:]
    pup_keep = np.ones(len(pup), bool)
    pup_keep[1:] = ~(np.abs(np.diff(pup)) >= 0.05)
    return {"run_raw": run, "run": run_f[run_keep], "run_dropped": int((~run_keep).sum()),
            "pupil_raw": pup, "pupil": pup[pup_keep & np.isfinite(pup)],
            "pupil_dropped": int((~pup_keep).sum()), "pupil_nan": int(np.isnan(pup).sum())}


# --- ROI measures -------------------------------------------------------------------------------

def calculate_snr(trace):
    """SNR and signal of one trace, as calculate_snr of the paper's code (see module docstring)."""
    med = np.median(trace)
    low = trace[trace <= med]
    noise = np.concatenate([low, 2 * med - low])
    mu, sd = noise.mean(), noise.std()
    thr = scipy.stats.norm.ppf(0.95, mu, sd)
    signal = trace[trace > thr].mean()
    return signal / sd, signal


def rolling_mean(x, win=4):
    """Rolling mean along the last axis, as rolling_mean of the paper's code (convolve, mode mirror)."""
    return scipy.ndimage.convolve1d(x, np.repeat(1.0 / win, win), axis=-1, mode="mirror")


def robust_scale(dff):
    """The code's default ROI scaling: (trace - median) / (95th - 5th percentile), per ROI (rows)."""
    med = np.median(dff, axis=1, keepdims=True)
    p5, p95 = np.percentile(dff, [5, 95], axis=1, keepdims=True)
    return (dff - med) / (p95 - p5)


def stimulus_events(trials):
    """Onset frames (end of each grey period but the last) and offset frames (start of each grey
    period but the first), with the stimulus type on the stimulus side of each event."""
    trials = trials.reset_index(drop=True)
    grey = np.flatnonzero(trials.stimulus_type.values == "grayscreen")
    onsets, offsets = [], []
    for g in grey[:-1]:
        nxt = trials.iloc[g + 1]
        onsets.append((int(nxt.start_frame_twop), nxt.stimulus_type))
    for g in grey[1:]:
        prev = trials.iloc[g - 1]
        offsets.append((int(prev.stop_frame_twop), prev.stimulus_type))
    return onsets, offsets


def window_means(dff, frames, pre, post):
    """Per ROI, the mean over events of the mean dF/F over `post` frames after each event frame and
    over `pre` frames before it. dff is ROIs x frames."""
    after = np.stack([dff[:, fr:fr + post].mean(axis=1) for fr in frames], axis=1).mean(axis=1)
    before = np.stack([dff[:, fr - pre:fr].mean(axis=1) for fr in frames], axis=1).mean(axis=1)
    return after, before


def event_traces(dff, frames, pre, post):
    """ROIs x events x frames, from `pre` frames before to `post` frames after each event frame."""
    return np.stack([dff[:, fr - pre:fr + post] for fr in frames], axis=1)


def _median_pairwise_corr(resp):
    """Per ROI, the median correlation between its single responses (ROIs x events x frames),
    each smoothed with the code's 4-point rolling mean."""
    sm = rolling_mean(resp, 4)
    sm = sm - sm.mean(axis=2, keepdims=True)
    sm /= np.linalg.norm(sm, axis=2, keepdims=True)
    out = np.empty(sm.shape[0])
    iu = np.triu_indices(sm.shape[1], k=1)
    for i in range(sm.shape[0]):
        c = sm[i] @ sm[i].T
        out[i] = np.nanmedian(c[iu])
    return out


def fig5_measures(dff, trials, snr, corrs=None):
    """Per ROI measures of the Fig. 5 criterion for one session (claims file, fig5-stimulus-responses).

    Gabor: mean dF/F over 0 to 0.6 s (18 frames) after D onsets against after U onsets. Flow, each
    direction: mean over 0 to 2 s after against 2 s before inconsistent flow onsets. Also the
    selection of reading (b): SNR above the session median and, for Gabor, the median pairwise
    correlation of single consistent sequence responses (-0.9 to 0.6 s), and the SD and skew of
    the mean response, each above the session's 75th percentile; for flow, the median pairwise
    correlation of single inconsistent flow responses (-2 to 2 s) and the mean response after
    minus before onset, each above the 75th percentile. The correlations do not change with
    scaling, so `corrs` from a first call can be passed to a second, on scaled traces."""
    corrs = {} if corrs is None else corrs
    t = trials.reset_index(drop=True)
    out = {}
    gab = t[t.stimulus_type == "gabors"]
    d_fr = gab.loc[gab.gabor_frame == "D", "start_frame_twop"].astype(int).values
    u_fr = gab.loc[gab.gabor_frame == "U", "start_frame_twop"].astype(int).values
    pre_g, post_g = 27, 18                        # 0.9 s and 0.6 s at 30 Hz
    d_resp = event_traces(dff, d_fr, pre_g, post_g)
    u_resp = event_traces(dff, u_fr, pre_g, post_g)
    d_mean = d_resp[:, :, pre_g:].mean(axis=(1, 2))
    u_mean = u_resp[:, :, pre_g:].mean(axis=(1, 2))
    mean_trace = d_resp.mean(axis=1)
    snr_ok = snr > np.median(snr)
    if "gabors" not in corrs:
        corrs["gabors"] = _median_pairwise_corr(d_resp)
    corr = corrs["gabors"]
    sd = mean_trace.std(axis=1)
    sk = scipy.stats.skew(mean_trace, axis=1)
    sel = snr_ok & (corr > np.percentile(corr, 75)) & (sd > np.percentile(sd, 75)) & (sk > np.percentile(sk, 75))
    out["gabors"] = {"consistent": d_mean, "inconsistent": u_mean, "selected": sel,
                     "n_consistent": len(d_fr), "n_inconsistent": len(u_fr)}
    vf = t[t.stimulus_type == "visflow"]
    for direction in sorted(vf.main_flow_direction.unique()):
        v = vf[vf.main_flow_direction == direction].reset_index(drop=True)
        unexp = v.unexpected.values == 1
        starts = np.flatnonzero(unexp & ~np.r_[False, unexp[:-1]])
        starts = starts[starts > 0]
        fr = v.loc[starts, "start_frame_twop"].astype(int).values
        resp = event_traces(dff, fr, PRE, POST)
        after = resp[:, :, PRE:].mean(axis=(1, 2))
        before = resp[:, :, :PRE].mean(axis=(1, 2))
        if direction not in corrs:
            corrs[direction] = _median_pairwise_corr(resp)
        corr = corrs[direction]
        diff = after - before
        sel = snr_ok & (corr > np.percentile(corr, 75)) & (diff > np.percentile(diff, 75))
        out[f"visflow {direction}"] = {"consistent": before, "inconsistent": after, "selected": sel,
                                       "n_inconsistent": len(fr)}
    return out, corrs


def roi_measures(f, trials, fig5=False):
    """Everything the analysis needs from one session's dF/F traces, computed as they load, so
    that the traces themselves are not kept. Returns per-ROI and per-pair summaries."""
    dff = f["processing/ophys/DfOverF/RoiResponseSeries/data"][:].T      # ROIs x frames
    bad = ~np.all(np.isfinite(dff), axis=1)
    out = {"n_rois": dff.shape[0], "n_bad": int(bad.sum()), "dff_min": float(np.nanmin(dff)),
           "dff_max": float(np.nanmax(dff)), "n_frames": dff.shape[1],
           "fingerprint": float(np.nansum(dff[:, :1000]))}
    dff = dff[~bad]
    snr_sig = np.array([calculate_snr(x) for x in dff])
    out["snr"], out["signal"] = snr_sig[:, 0], snr_sig[:, 1]
    sm = rolling_mean(dff, 4)
    c = np.corrcoef(sm)
    corr = c[np.triu_indices(len(c), k=1)]
    out["corr"] = corr.astype(np.float32)
    del sm, c
    onsets, offsets = stimulus_events(trials)
    # The same measure at onset frames shifted in time, for the clock check: population mean and SEM.
    out["onset_shift"] = {}
    for shift in (-600, -300, -150, 0, 150, 300, 600):
        after, before = window_means(dff, [fr + shift for fr, _ in onsets], PRE, POST)
        dlt = after - before
        out["onset_shift"][shift] = (dlt.mean(), dlt.std(ddof=1) / np.sqrt(len(dlt)))
    scaled = robust_scale(dff)
    for name, events in (("onset", onsets), ("offset", offsets)):
        frames = [fr for fr, _ in events]
        gab = [fr for fr, st in events if st == "gabors"]
        for label, x in (("", dff), ("_scaled", scaled)):
            after, before = window_means(x, frames, PRE, POST)
            out[f"{name}_diff{label}"] = after - before
            out[f"{name}_trace{label}"] = event_traces(x, frames, PRE, POST).mean(axis=1)
        after, before = window_means(dff, gab, PRE, POST)
        out[f"{name}_diff_gabor"] = after - before
        out[f"{name}_types"] = [st for _, st in events]
    if fig5:
        out["fig5"], corrs = fig5_measures(dff, trials, out["snr"])
        out["fig5_scaled"], _ = fig5_measures(scaled, trials, out["snr"], corrs)
    return out


# --- The paper's tables, as reference values -------------------------------------------------------
# Copied from the paper's text (Tables 1 and 2), which the claims judge the files against. They are
# the paper's reported values, not data: every measured value in the notebook comes from the files.
# Table 1: subject ID, sex, date of birth, imaged cell type, imaging plane ("distal apical dendrites"
# shortened to "dendrites"). Table 2: subject ID, session ID, imaging date, depth (um), # ROIs,
# # tracked ROIs, QC, stimulus seed.
PAPER_TABLE1 = """
408021 M 20180623 L2/3 somata
411400 F 20180711 L5 dendrites
411424 F 20180711 L2/3 somata
411771 M 20180713 L5 somata
412933 M 20180718 L2/3 dendrites
413663 M 20180721 L2/3 dendrites
418779 F 20180820 L5 somata
420011 F 20180826 L5 dendrites
433414 F 20181106 L2/3 dendrites
433448 M 20181106 L5 dendrites
433451 M 20181106 L5 dendrites
433458 M 20181106 L5 somata
440889 F 20181212 L2/3 somata
"""
PAPER_TABLE2 = """
408021 758519303 20180926 175 96 59 passed 30587
408021 759189643 20180927 175 74 59 passed 5730
408021 759660390 20181001 175 107 59 passed 36941
411400 759666166 20181001 20 942 0 failed 11883
411400 759872185 20181002 20 289 0 failed 8005
411400 760269100 20181003 20 524 0 failed 34380
411400 761730740 20181009 20 630 162 passed 44023
411400 762415169 20181011 20 637 162 passed 29259
411400 763646681 20181015 20 597 162 passed 1118
411424 761624763 20181009 175 87 55 passed 997
411424 761944562 20181010 175 90 55 passed 33856
411424 762250376 20181011 175 80 55 passed 23187
411771 760260459 20181003 375 90 47 passed 33767
411771 760659782 20181004 375 70 47 passed 32698
411771 761269197 20181008 375 79 47 passed 17904
412933 763949859 20181016 75 1041 0 failed 44721
412933 764897534 20181017 75 948 0 failed 32579
412933 765427689 20181018 75 836 0 failed 26850
412933 766755831 20181022 50 344 98 passed 39002
412933 767254594 20181023 50 168 98 passed 6698
412933 768807532 20181025 50 250 98 passed 8612
413663 764704289 20181017 50 628 136 passed 12470
413663 765193831 20181018 50 348 136 passed 7038
413663 766502238 20181022 50 512 136 passed 23433
418779 777496949 20181112 375 15 12 passed 32706
418779 778374308 20181113 375 26 12 passed 8114
418779 779152062 20181114 375 29 12 passed 11744
420011 777914830 20181113 20 205 51 passed 20846
420011 778864809 20181114 20 159 51 passed 35159
420011 779650018 20181115 20 182 51 passed 34931
433414 826187862 20190220 75 727 118 passed 303
433414 826773996 20190221 75 300 118 passed 13515
433414 827833392 20190222 75 333 118 passed 32899
433448 826338612 20190220 20 1636 112 passed 38171
433448 826819032 20190221 20 445 112 passed 38273
433448 828816509 20190225 20 496 112 passed 18246
433448 829283315 20190226 20 436 0 passed 17769
433451 823453391 20190215 20 966 353 passed 18665
433451 824434038 20190218 20 1029 353 passed 36
433451 825180479 20190219 20 986 353 passed 7754
433458 826659257 20190221 375 99 70 passed 35969
433458 827300090 20190222 375 87 70 passed 10378
433458 828475005 20190225 375 97 70 passed 10576
433458 829520904 20190227 375 88 0 passed 42270
440889 832883243 20190306 175 224 147 passed 27797
440889 833704570 20190307 175 224 147 passed 16745
440889 834403597 20190308 175 210 147 passed 10210
440889 836968429 20190314 175 205 0 passed 24253
440889 837360280 20190315 175 217 0 failed 19576
440889 838633305 20190318 175 227 0 failed 30582
"""


def paper_table1():
    rows = [r.split() for r in PAPER_TABLE1.strip().splitlines()]
    return pd.DataFrame(rows, columns=["subject_id", "sex", "dob", "line", "plane"])


def paper_table2():
    rows = [r.split() for r in PAPER_TABLE2.strip().splitlines()]
    df = pd.DataFrame(rows, columns=["subject_id", "session_id", "date", "depth", "n_rois", "n_tracked",
                                     "qc", "seed"])
    for c in ["depth", "n_rois", "n_tracked", "seed"]:
        df[c] = df[c].astype(int)
    return df


# --- ROI matching over session orderings (fig8-ordering-variation) ---------------------------------

def roi_masks(f):
    """Binary ROI masks (mask > 0) and the plane's max projection image of one open file."""
    m = f["processing/ophys/ImageSegmentation/PlaneSegmentation/image_mask"][:] > 0
    img = f["processing/ophys/PlaneImages/max_projection"][:]
    return m, img


def nway_input(sessions, workdir):
    """The input of the Allen Institute's n-way matching package (ophys_nway_matching) for sessions
    given in order, as (session id, masks, image). The image is the plane's max projection, written as
    a PNG in a temporary directory because the package reads images from paths."""
    from PIL import Image
    exps = []
    base = {sid: k + 1 for k, sid in enumerate(sorted(s[0] for s in sessions))}  # ROI ids must fit uint32
    for sid, masks, img in sessions:
        path = os.path.join(workdir, f"{sid}.png")
        Image.fromarray(img).save(path)
        rois = []
        for i, m in enumerate(masks):
            ys, xs = np.nonzero(m)
            y0, x0 = ys.min(), xs.min()
            rois.append({"id": base[sid] * 100000 + i, "x": int(x0), "y": int(y0), "z": 1,
                         "width": int(xs.max() - x0 + 1), "height": int(ys.max() - y0 + 1), "valid": True,
                         "mask_matrix": m[y0:ys.max() + 1, x0:xs.max() + 1].tolist()})
        exps.append({"id": int(sid), "ophys_average_intensity_projection_image": path, "cell_rois": rois})
    return exps


def _nway_args(experiments, workdir):
    return {"output_directory": workdir, "log_level": "ERROR", "parallel_workers": 1,
            "save_pairwise_results": True, "output_json": os.path.join(workdir, "out.json"),
            "experiment_containers": {"ophys_experiments": experiments}}


_JOBS = {}


def _pair_job(key):
    """One pairwise matching of the package (fixed session, moving session), default parameters."""
    import copy
    from nway.nway_matching import NwayMatching, pair_match_job
    mouse, i, j, workdir = key
    exps = _JOBS[mouse]
    workdir = os.path.join(workdir, f"{mouse}_{i}_{j}")   # the package writes mask files here; one per job
    os.makedirs(workdir)
    nm = NwayMatching(input_data=_nway_args([exps[i], exps[j]], workdir), args=[])
    nm.make_masks_from_dicts()
    pa = copy.deepcopy(nm.args)
    for k in ["substitute_max_for_avg", "pruning_method", "experiment_containers",
              "save_pairwise_results", "parallel_workers"]:
        pa.pop(k)
    fixed, moving = nm.experiments
    pa.update(fixed=fixed, moving=moving,
              output_json=os.path.join(workdir, f"{mouse}_{moving['id']}_to_{fixed['id']}.json"))
    pair_match_job(pa)
    return key, pa["output_json"]


class _Pair:
    def __init__(self, args):
        self.args = args


def ordering_counts(sessions_by_mouse, thresholds=(0.1, 0.2), workers=4):
    """Matched-ROI counts for every ordering of each mouse's sessions.

    The package (NwayMatching.run, without its summary plots) matches every pair of sessions with
    the earlier one in the given order as the fixed image (itertools.combinations), then builds
    the n-way table and prunes conflicts. An ordering therefore uses, for each pair of sessions,
    one of its two directed pairwise matchings; the six directed matchings of a mouse are computed
    once, in parallel processes, and each ordering combines the three it uses. A match across
    all sessions counts; with a threshold, only when every pairwise match in it has an
    intersection over union at least that large (the dendritic overlap constraint of the
    Methods, read as IoU: an assumption, the paper does not define its overlap measure)."""
    import itertools
    import multiprocessing
    import tempfile
    from nway.nway_matching import NwayMatching
    with tempfile.TemporaryDirectory() as workdir:
        _JOBS.clear()
        for m, sess in sessions_by_mouse.items():
            _JOBS[m] = nway_input(sess, workdir)
        size = {m: sum(len(s[1]) for s in v) for m, v in sessions_by_mouse.items()}
        keys = [(m, i, j, workdir) for m in sorted(size, key=size.get, reverse=True)
                for i, j in itertools.permutations(range(len(sessions_by_mouse[m])), 2)]
        with multiprocessing.get_context("fork").Pool(workers) as pool:
            done = dict(pool.map(_pair_job, keys, chunksize=1))
        rows = []
        for m, exps in _JOBS.items():
            for order in itertools.permutations(range(len(exps))):
                nm = NwayMatching(input_data=_nway_args([exps[k] for k in order], workdir), args=[])
                nm.make_masks_from_dicts()
                pairs = []
                for a, b in itertools.combinations(order, 2):
                    with open(done[(m, a, b, workdir)]) as fh:
                        pj = __import__("json").load(fh)
                    pairs.append(_Pair({"output_json": done[(m, a, b, workdir)], "fixed": {"id": pj["fixed_experiment"]},
                                        "moving": {"id": pj["moving_experiment"]}}))
                nm.pair_matches = pairs
                table = nm.remove_nway_table_redundancy(nm.gen_nway_table_with_redundancy())
                table = nm.prune_matching_graph(table)
                nm.matching_table_nway = nm.add_remaining_cells(table)
                out = nm.create_output_dict()
                full = [set(x) for x in out["nway_matches"] if len(x) == len(exps)]
                iou = {}
                for p in out["pairwise_results"]:
                    for x in p["matches"]:
                        iou[frozenset((x["fixed"], x["moving"]))] = x["iou"]
                row = {"mouse": m, "order": "-".join(str(k + 1) for k in order), "all": len(full)}
                for thr in thresholds:
                    row[f"iou>={thr:g}"] = sum(all(iou.get(frozenset((a, b)), 0) >= thr for a in x for b in x if a < b)
                                               for x in full)
                rows.append(row)
    return pd.DataFrame(rows)
