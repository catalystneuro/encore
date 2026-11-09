"""Loading and measures for the movie-watching EMU sessions of dandiset 000623.

Keles et al. (2024), Scientific Data 11, 214, doi:10.1038/s41597-024-03029-1.

Each NWB file holds one run ("session") of one participant: spike-sorted units with their quality
metrics, LFP from the microwires (LFP_micro) and the macro contacts (LFP_macro) at 1000 Hz, gaze
and pupil data, the frame times of the movie and a trials table (one encoding row for the movie,
then 40 recognition trials). Files are streamed from the archive at the pinned version; nothing
is written to disk.

Where the parameters come from. Unless stated otherwise each step follows the paper's code,
github.com/rutishauserlab/bmovie-release-NWB-BIDS at commit 8c35290 (the claims file cites it
for each criterion), and the file named in the comment:

- unit set U, firing rate and quality metrics: ephys_qc/gen_figure2ah_singleunitQC.py;
- AUC, confidence split and inclusion: ephys_qc/ephys_utills.py and gen_figure3_recogtask_roc.py;
- gaze binning, missing data and heatmaps: ephys_utills.py and gen_figure3_eyetracking.py;
- memory and event selectivity, bootstrap and permutation tests:
  singleneuron/examine_neurons_*.py, ieeg/examine_channels_*.py and vizutils_neuron.py;
- HFB power: ieeg/prep_filterLFP.py.

Two implementation choices are this entry's own and are stated as such:

- The permutation null (`perm_null_counts`) draws, in each shuffle, one set of bootstrap resamples
  per session and applies it to every cell of that session, where the code draws one per cell.
  Each cell's null decision has the code's distribution; only the bootstrap noise is shared
  between cells of a session within one shuffle. This makes 2,000 shuffles of 5,000 resamples
  affordable. The permutation of trials is drawn per cell, as in the code.
- The permutation test is unseeded in the code; it is seeded here (standard choice, open detail 8
  of the claims file).
"""

from __future__ import annotations

import io
import urllib.request

import h5py
import numpy as np
import pandas as pd
import pynwb
import remfile
from dandi.dandiapi import DandiAPIClient

DANDISET_ID = "000623"
DANDISET_VERSION = "0.240130.2108"   # the version the paper cites (reference 54)

CODE_COMMIT = "8c35290b74a9522bf27cbcae44dcb88ff2a1d58f"
SCENECUT_URL = ("https://raw.githubusercontent.com/rutishauserlab/bmovie-release-NWB-BIDS/"
                f"{CODE_COMMIT}/assets/annotations/scenecut_info.csv")

AREAS = ["amygdala", "hippocampus", "ACC", "preSMA", "vmPFC"]
CHANNEL_AREAS = {"AMY": "amygdala", "HIP": "hippocampus", "ACC": "ACC", "SMA": "preSMA",
                 "OFC": "vmPFC"}                       # prep_filterLFP.py keep_channel_areas
LFP_PAD_S = 10.0       # prep_filterLFP.py LFP_PAD_us: the LFP starts 10 s before the movie
EDGE_S = 10.0          # prep_filterLFP.py edge_offset
HFB_FREQS = np.arange(70.0, 171.0, 10.0)
MEMORY_WINDOW = (0.2, 1.7)   # s after trial start_time (examine_*_recognitiontask.py)
EVENT_WINDOW = (0.0, 1.0)    # s after cut onset (examine_*_scenecuts.py)
N_BOOT, N_BOOT_NULL, N_NULL = 10000, 5000, 2000
BOOT_SEED = 13               # examine_*: np.random.default_rng(13)


# ---------------------------------------------------------------- loading

def asset_urls():
    """Path and S3 URL of every NWB asset of the pinned version, sorted by path."""
    ds = DandiAPIClient().get_dandiset(DANDISET_ID, DANDISET_VERSION)
    out = []
    for a in ds.get_assets():
        if a.path.endswith(".nwb"):
            out.append((a.path, a.get_content_url(follow_redirects=1, strip_query=True), a.size))
    return sorted(out)


def open_nwb(url):
    f = h5py.File(remfile.File(url), "r")
    return f, pynwb.NWBHDF5IO(file=f, load_namespaces=True).read()


def load_session(url):
    """Everything but the LFP data of one file, as plain Python and numpy objects."""
    f, nwb = open_nwb(url)
    trials = nwb.trials.to_dataframe()
    units = nwb.units.to_dataframe()
    elec = nwb.electrodes.to_dataframe()
    beh = nwb.processing["behavior"]
    gaze = beh["EyeTracking"]["SpatialSeries"]
    mf = nwb.stimulus["movieframe_time"]
    lfp = {}
    for k in ["LFP_micro", "LFP_macro"]:
        try:
            es = nwb.processing["ecephys"][k]["ElectricalSeries"]
        except KeyError:
            continue
        lfp[k] = dict(shape=es.data.shape, rate=es.rate, starting_time=es.starting_time,
                      unit=es.unit, names=es.electrodes.to_dataframe()["origchannel_name"]
                      .to_numpy(str), locations=es.electrodes.to_dataframe()["location"]
                      .to_numpy(str))
    s = dict(
        identifier=nwb.identifier, session_id=nwb.session_id,
        subject=dict(subject_id=nwb.subject.subject_id, age=nwb.subject.age, sex=nwb.subject.sex,
                     description=nwb.subject.description),
        trials=trials,
        units=units.drop(columns=["waveform_mean_encoding", "waveform_mean_recognition",
                                  "electrodes"], errors="ignore"),
        units_columns=list(units.columns),
        electrodes=elec.drop(columns=["group"]),
        gaze=np.asarray(gaze.data[:]), gaze_rate=gaze.rate, gaze_start=gaze.starting_time,
        gaze_t=None if gaze.rate is not None else np.asarray(gaze.timestamps[:]),
        gaze_comments=gaze.comments, gaze_unit=gaze.unit,
        frame_data=np.asarray(mf.data[:]).astype(int), frame_times=np.asarray(mf.timestamps[:]),
        lfp=lfp, behavior_modules=sorted(beh.data_interfaces.keys()),
    )
    f.close()
    return s


def movie_window(s):
    enc = s["trials"][s["trials"].stim_phase == "encoding"].iloc[0]
    return float(enc.start_time), float(enc.stop_time)


def recog_trials(s):
    """Recognition rows: truth (old/new from the file name), response class and correctness."""
    r = s["trials"][s["trials"].stim_phase == "recognition"].copy()
    r["label"] = r.stimulus_file.str[:3]
    r["resp"] = np.where(r.actual_response <= 3, "new", "old")
    r["correct_code"] = r.label == r.resp
    return r


def area_of_location(loc):
    """examine_neurons_*: brain area is the location with 'Left ' or 'Right ' removed."""
    return loc.removeprefix("Left ").removeprefix("Right ")


def units_U(s):
    """Units with at least one spike in the movie window (set U), with their area and rate."""
    t0, t1 = movie_window(s)
    loc = s["electrodes"]["location"]
    rows = []
    for _, u in s["units"].iterrows():
        st = np.asarray(u.spike_times)
        n = int(np.sum((st >= t0) & (st <= t1)))
        rows.append(dict(unit_id_session=u.unit_id_session, electrode_id=int(u.electrode_id),
                         n_movie=n, rate=n / (t1 - t0), isibelow=u.isibelow, peakSNR=u.peakSNR,
                         meanSNR=u.meanSNR, isolationdist=u.isolationdist,
                         area=area_of_location(loc.iloc[int(u.electrode_id)]),
                         area_loc=area_of_location(loc.loc[int(u.electrode_id)])))
    df = pd.DataFrame(rows)
    df["in_U"] = df.n_movie > 0
    df["session"] = s["identifier"]
    return df


def window_counts(spike_times, onsets, window):
    """Spike counts in [onset + window[0], onset + window[1]] (inclusive, as win_spike_rate)."""
    st = np.sort(np.asarray(spike_times))
    lo = np.searchsorted(st, onsets + window[0], side="left")
    hi = np.searchsorted(st, onsets + window[1], side="right")
    return hi - lo


def scenecuts():
    """The 93 annotated cuts and their type (rule S of the claims file)."""
    with urllib.request.urlopen(SCENECUT_URL) as r:
        cuts = pd.read_csv(io.BytesIO(r.read()))
    new_scenes = np.where(np.diff(cuts["scene_id"]))[0] + 1
    kind = np.array(["change" if i in new_scenes else "cont" for i in range(len(cuts))])
    kind[0] = "change"
    cuts["kind"] = kind
    return cuts


def cut_onsets(s, cuts):
    """examine_*_scenecuts.py: movieframe_time timestamp of frame shot_start_fr (1-based)."""
    return s["frame_times"][cuts["shot_start_fr"].to_numpy(int) - 1]


# ---------------------------------------------------------------- behaviour

def adjust_hf(H, F, n_new, n_old):
    if H == 1:
        H = 1 - 1 / (2 * n_old)
    if F == 1:
        F = 1 - 1 / (2 * n_new)
    if H == 0:
        H = 1 / (2 * n_old)
    if F == 0:
        F = 1 / (2 * n_new)
    return H, F


def session_auc(truth_old, response):
    """cal_auc on cumulative hit and false-alarm rates from confidence 6 down to 1."""
    truth_old = np.asarray(truth_old, bool)
    response = np.asarray(response)
    n_old, n_new = truth_old.sum(), (~truth_old).sum()
    TP = FP = 0
    Hs, Fs = [], []
    for i in range(6, 0, -1):
        sel = response == i
        TP += np.sum(truth_old[sel])
        FP += np.sum(~truth_old[sel])
        H, F = adjust_hf(TP / n_old, FP / n_new, n_new, n_old)
        Hs.append(H)
        Fs.append(F)
    TPr, FPr = np.array(Hs), np.array(Fs)
    if TPr[0] != 0 or FPr[0] != 0:
        TPr, FPr = np.insert(TPr, 0, 0), np.insert(FPr, 0, 0)
    if TPr[-1] != 1 or FPr[-1] != 1:
        TPr, FPr = np.append(TPr, 1), np.append(FPr, 1)
    auc = 0.0
    for i in range(1, len(TPr)):
        auc += (FPr[i] - FPr[i - 1]) * TPr[i - 1] + 0.5 * (TPr[i] - TPr[i - 1]) * (FPr[i] - FPr[i - 1])
    return auc


def check_inclusion(response, auc):
    counts = np.array([np.sum(response == i) for i in range(1, 7)])
    ok = auc >= 0.6
    if np.sum(counts[0:3] == 0) > 1 or np.sum(counts[3:6] == 0) > 1:
        ok = False
    return ok


def confidence_accuracy(truth_old, response):
    """dynamic_split and the accuracies of gen_figure3_recogtask_roc.py, in percent."""
    g = np.asarray(truth_old, int)
    r = np.asarray(response)
    rc = np.array([np.sum(r == i) for i in range(1, 7)])
    c1, c2, c3 = rc[0] + rc[5], rc[1] + rc[4], rc[2] + rc[3]
    split = [c1 - (c2 + c3), (c1 + c2) - c3]
    mode = int(np.where(np.abs(split) == np.min(np.abs(split)))[0][0]) + 1
    if rc[0] == 0 or rc[5] == 0:
        mode = 2
    if rc[1] == 0 or rc[4] == 0:
        mode = 1
    if mode == 1:
        hi_old, lo_old = r >= 6, r == 4
        hi_new, lo_new = r <= 1, (r == 3) | (r == 2)
    else:
        hi_old, lo_old = r >= 5, r == 4
        hi_new, lo_new = r <= 2, r == 3
    tp_h, tp_l = np.sum((g == 1) & hi_old), np.sum((g == 1) & lo_old)
    fp_h, fp_l = np.sum((g == 0) & hi_old), np.sum((g == 0) & lo_old)
    tn_h, tn_l = np.sum((g == 0) & hi_new), np.sum((g == 0) & lo_new)
    fn_h, fn_l = np.sum((g == 1) & hi_new), np.sum((g == 1) & lo_new)
    acc_h = (tn_h + tp_h) / (tn_h + tp_h + fn_h + fp_h) * 100
    acc_l = (tn_l + tp_l) / (tn_l + tp_l + fn_l + fp_l) * 100
    return mode, acc_h, acc_l


# ---------------------------------------------------------------- gaze

FRAME_W, FRAME_H, FPS, NFRAMES = 640, 480, 25.0, 11971
NBINS = int(np.round(1000.0 / FPS * NFRAMES / 1000.0))   # 479 one-second bins


def pixel_per_dva(resolution_wh):
    """compute_pixelperDVA: 40 x 30 cm screen at 60 cm; mean over the two axes."""
    p = np.tan(np.deg2rad(1.0) / 2.0) * 2 * 60.0 * np.divide(resolution_wh, [40.0, 30.0])
    return p.mean()


def gaze_bins(s):
    """Gaze in the movie window mapped to the 640 x 480 frame, in 1-s bins (get_et_timebins).

    Returns a list of NBINS arrays of (x, y) samples (NaN where missing or off the frame; an
    empty bin is one NaN row), the missing fraction and pixels per degree."""
    t0, t1 = movie_window(s)
    xy = s["gaze"]
    if s["gaze_rate"] is None:
        t = s["gaze_t"]
    else:
        t = np.arange(len(xy)) / s["gaze_rate"] + s["gaze_start"]
    use = (t >= t0) & (t <= t1)
    t, xy = t[use], xy[use].astype(float).copy()
    scr, disp, area = s["gaze_comments"].split("::")
    sw, sh = map(float, scr.split("=")[1].split(","))
    dw, dh = map(float, disp.split("=")[1].split(","))
    da = list(map(float, area.split("=")[1].split(",")))
    x = (xy[:, 0] - da[0]) * FRAME_W / dw
    y = (xy[:, 1] - da[1]) * FRAME_H / dh
    bad = ~((x >= 0) & (x < FRAME_W)) | ~((y >= 0) & (y < FRAME_H))
    x[bad] = np.nan
    y[bad] = np.nan
    chunk = (t * 1000.0 // 1000.0 + 1).astype(int)
    bins = []
    for b in range(1, NBINS + 1):
        sel = chunk == b
        bins.append(np.c_[x[sel], y[sel]] if sel.any() else np.array([[np.nan, np.nan]]))
    allv = np.vstack(bins)
    missing = np.isnan(allv).any(axis=1).sum() / allv.shape[0]
    return bins, missing, pixel_per_dva([sw, sh])


def heatmap(xy, sigma, down=5.0, nan_ratio=1.0):
    """et_heatmap with get_down: 2-D histogram on the frame / down, Gaussian sigma / down."""
    from scipy.ndimage import gaussian_filter
    if xy is None or len(xy) == 0 or np.isnan(xy).any(axis=1).sum() >= nan_ratio * xy.shape[0]:
        return None
    fs = (np.array([FRAME_W, FRAME_H]) / down).astype(int)
    h, _, _ = np.histogram2d(xy[:, 0] / down, xy[:, 1] / down, bins=fs,
                             range=[[0, fs[0]], [0, fs[1]]])
    return gaussian_filter(h.T, sigma=sigma / down, mode="constant", cval=0.0)


# ---------------------------------------------------------------- selectivity tests

def boot_p_from_counts(n_le0, n_gt0, n_lt0, n_ge0, mean_sign, n):
    """get_bootstrappval (two-sided), vectorised over rows, from counts of resampled differences."""
    p_pos = 2 * np.minimum(n_le0 + 1.0, n_gt0 + 1.0) / (n + 1.0)
    p_neg = 2 * np.minimum(n_lt0 + 1.0, n_ge0 + 1.0) / (n + 1.0)
    p_zero = 2 * np.minimum(n_le0 + 1.0, n_ge0 + 1.0) / (n + 1.0)
    return np.where(mean_sign > 0, p_pos, np.where(mean_sign < 0, p_neg, p_zero))


def _counts_matrix(idx, m):
    """Bootstrap index array (k, n) into m items -> (n, m) matrix of counts per resample."""
    k, n = idx.shape
    flat = idx.T + (np.arange(n) * m)[:, None]
    return np.bincount(flat.ravel(), minlength=n * m).reshape(n, m).astype(float)


def _p_from_diffs(D):
    n = D.shape[1]
    n_gt, n_lt = (D > 0).sum(1), (D < 0).sum(1)
    return boot_p_from_counts(n - n_gt, n_gt, n_lt, n - n_lt, np.sign(D.mean(1)), n)


def observed_selection(values, mask_a, mask_b, balanced):
    """Bootstrap B with seed 13 for a block of cells sharing one trial design.

    values: (cells, trials) responses (spike counts or HFB means). mask_a, mask_b: group A
    (novel, or scene change) and group B (familiar, or continuity cut). Returns the observed
    difference of means A - B and the bootstrap p for each cell, as the code's ms_test and
    scenechange_test with run_permutation=False (the same seed, so the same resamples)."""
    A, B = values[:, mask_a], values[:, mask_b]
    na, nb = A.shape[1], B.shape[1]
    rng = np.random.default_rng(BOOT_SEED)
    if balanced:
        k = min(na, nb)
        ia, ib = rng.integers(na, size=(k, N_BOOT)), rng.integers(nb, size=(k, N_BOOT))
        ka, kb = k, k
    else:
        ia, ib = rng.integers(na, size=(na, N_BOOT)), rng.integers(nb, size=(nb, N_BOOT))
        ka, kb = na, nb
    Ca, Cb = _counts_matrix(ia, na), _counts_matrix(ib, nb)
    # kb * sum_a - ka * sum_b has the sign of the difference of resample means, and is exact
    # for integer data (spike counts), so that ties are ties as in the code
    D = kb * (A @ Ca.T) - ka * (B @ Cb.T)
    return A.mean(1) - B.mean(1), _p_from_diffs(D)


def perm_null_counts(blocks, balanced, positive_only, n_null=N_NULL, seed=0, alpha=0.05):
    """Permutation test P: for each cell and shuffle, whether the cell is selective in the null.

    blocks: list of (values (cells, trials), mask_a, mask_b), one per session. For each shuffle
    and cell, n_a + n_b responses are drawn without replacement from all of the cell's trials
    and split into pseudo-groups (B first, then A, as the code), and tested by bootstrap B with
    N_BOOT_NULL resamples; with `positive_only` a cell counts only when its pseudo-difference
    A - B is positive (examine_*_scenecuts.py). Sessions with the same design are pooled, and
    share the bootstrap resamples within a shuffle (see the module docstring). Returns a boolean
    array (cells in the order of `blocks`, n_null)."""
    rng = np.random.default_rng(seed)
    groups = {}
    for i, (values, mask_a, mask_b) in enumerate(blocks):
        key = (mask_a.tobytes(), mask_b.tobytes(), values.shape[1])
        groups.setdefault(key, []).append(i)
    res_by_block = [None] * len(blocks)
    for key, idx in groups.items():
        values = np.vstack([blocks[i][0] for i in idx]).astype(np.float32)
        mask_a, mask_b = blocks[idx[0]][1], blocks[idx[0]][2]
        ncell, ntr = values.shape
        na, nb = int(mask_a.sum()), int(mask_b.sum())
        res = np.zeros((ncell, n_null), bool)
        rows = np.arange(ncell)[:, None]
        for s in range(n_null):
            perm = rng.random((ncell, ntr)).argsort(1)[:, :na + nb]
            Bv = values[rows, perm[:, :nb]]
            Av = values[rows, perm[:, nb:]]
            if balanced:
                k = min(na, nb)
                ia = rng.integers(na, size=(k, N_BOOT_NULL))
                ib = rng.integers(nb, size=(k, N_BOOT_NULL))
                ka, kb = k, k
            else:
                ia = rng.integers(na, size=(na, N_BOOT_NULL))
                ib = rng.integers(nb, size=(nb, N_BOOT_NULL))
                ka, kb = na, nb
            Ca = _counts_matrix(ia, na).astype(np.float32)
            Cb = _counts_matrix(ib, nb).astype(np.float32)
            D = kb * (Av @ Ca.T) - ka * (Bv @ Cb.T)
            sig = _p_from_diffs(D) < alpha
            if positive_only:
                sig &= (Av.mean(1) - Bv.mean(1)) > 0
            res[:, s] = sig
        start = 0
        for i in idx:
            n = blocks[i][0].shape[0]
            res_by_block[i] = res[start:start + n]
            start += n
    return np.vstack(res_by_block)


def area_pvalues(null_sig, areas, observed_counts, area_list):
    """get_NulltestPvals_cols on the null counts per area."""
    areas = np.asarray(areas)
    null_counts = np.stack([null_sig[areas == a].sum(0) for a in area_list], 1)
    ps = []
    for j, a in enumerate(area_list):
        obs = observed_counts[a]
        if obs > 0:
            ps.append((np.sum(null_counts[:, j] >= obs) + 1.0) / (null_counts.shape[0] + 1.0))
        else:
            ps.append((np.sum(null_counts[:, j] <= obs) + 1.0) / (null_counts.shape[0] + 1.0))
    return np.array(ps), null_counts


# ---------------------------------------------------------------- HFB

def hfb_session(url, etype, onsets_by_task, n_chunk=8):
    """HFB pipeline H (prep_filterLFP.py) for one session and electrode type, reduced to means.

    onsets_by_task: {'enc': (t0, t1, {name: (onsets, window)}), 'recog': (...)}
    where t0, t1 bound the task block. Each block, padded by 10 s, is notch filtered at 60 Hz and
    harmonics, high-passed at 0.1 Hz, re-referenced to the common average of the kept channels,
    and transformed to Morlet power (5 cycles, 70 to 170 Hz in 10 Hz steps), z-scored over time
    per frequency, averaged over frequencies and resampled to 500 Hz. Returns the channel names
    and, for each onset set, the mean HFB in its window after each onset (session time). The LFP
    time is the file's sample time minus LFP_PAD_S, as the code."""
    import mne
    from scipy.stats import zscore
    mne.set_log_level("ERROR")
    f, nwb = open_nwb(url)
    try:
        es = nwb.processing["ecephys"][etype]["ElectricalSeries"]
    except KeyError:
        f.close()
        return None
    names_all = es.electrodes.to_dataframe()["origchannel_name"].to_numpy(str)
    use = np.array([n[1:4] in CHANNEL_AREAS for n in names_all])
    full = es.data[:]
    data = np.ascontiguousarray(full[:, use].T)
    del full
    rate, start = es.rate, es.starting_time
    f.close()
    names = names_all[use]
    lt = np.arange(data.shape[1]) / rate + start - LFP_PAD_S
    out = {"names": names}
    for task, (b0, b1, onset_sets) in onsets_by_task.items():
        sel = (lt >= b0 - EDGE_S) & (lt <= b1 + EDGE_S)
        seg_t0 = lt[sel][0]
        info = mne.create_info(list(names), sfreq=rate, ch_types="seeg")
        raw = mne.io.RawArray(data[:, sel], info)
        raw.notch_filter(np.arange(60, info["lowpass"] + 1, 60), phase="zero-double", n_jobs=1)
        raw.filter(0.1, None, n_jobs=1)
        raw, _ = mne.set_eeg_reference(raw, "average")
        x = raw.get_data()
        hfb = np.empty_like(x)
        for c0 in range(0, x.shape[0], n_chunk):
            p = mne.time_frequency.tfr_array_morlet(x[None, c0:c0 + n_chunk], sfreq=rate,
                                                    freqs=HFB_FREQS, n_cycles=5.0,
                                                    output="power", n_jobs=1)[0]
            hfb[c0:c0 + n_chunk] = zscore(p, axis=-1).mean(1)
        raw_h = mne.io.RawArray(hfb, info)
        raw_h.resample(500, npad="auto")
        h = raw_h.get_data()
        ht = raw_h.times + seg_t0
        for name, (onsets, w) in onset_sets.items():
            m = np.full((h.shape[0], len(onsets)), np.nan)
            for j, o in enumerate(onsets):
                tu = (ht >= o + w[0]) & (ht <= o + w[1])
                if tu.any():
                    m[:, j] = h[:, tu].mean(1)
            out[name] = m
        del raw, x, hfb, raw_h, h
    return out


# ---------------------------------------------------------------- cell-level designs

def rule_R(s):
    """examine_*_recognitiontask.py: a session is skipped with < 10 correct new or old trials."""
    r = recog_trials(s)
    n_old = int(((r.label == "old") & (r.resp == "old")).sum())
    n_new = int(((r.label == "new") & (r.resp == "new")).sum())
    return n_old >= 10 and n_new >= 10, n_new, n_old


def memory_design(s):
    """Masks of correct novel (A) and correct familiar (B) trials over all recognition trials."""
    r = recog_trials(s)
    a = ((r.label == "new") & (r.resp == "new")).to_numpy()
    b = ((r.label == "old") & (r.resp == "old")).to_numpy()
    return r.start_time.to_numpy(), a, b


def cell_blocks(S, task, cuts=None, sessions=None):
    """Per session, the spike counts of the units of U in the claim's window after each event.

    task 'memory': recognition trial onsets, 0.2 to 1.7 s (counts, proportional to the code's
    rates); task 'event': cut onsets, 0 to 1.0 s. Returns blocks for perm_null_counts and a
    table of the units (session, unit_id_session, area)."""
    blocks, rows = [], []
    for s in S:
        if sessions is not None and s["identifier"] not in sessions:
            continue
        U = units_U(s)
        keep = np.where(U.in_U.to_numpy())[0]
        if task == "memory":
            ons, a, b = memory_design(s)
            w = MEMORY_WINDOW
        else:
            ons = cut_onsets(s, cuts)
            a = (cuts.kind == "change").to_numpy()
            b = (cuts.kind == "cont").to_numpy()
            w = EVENT_WINDOW
        st = s["units"].spike_times.to_numpy()
        V = np.array([window_counts(np.asarray(st[k]), ons, w) for k in keep], float)
        if len(keep) == 0:
            continue
        blocks.append((V, a, b))
        rows.append(U.iloc[keep][["session", "unit_id_session", "area"]])
    return blocks, pd.concat(rows, ignore_index=True)


def selection_and_null(blocks, table, balanced, positive_only, seed, area_list=AREAS,
                       n_null=N_NULL):
    """Observed selection (bootstrap B, seed 13) and permutation p per area (test P)."""
    d, p = [], []
    for V, a, b in blocks:
        di, pi = observed_selection(V, a, b, balanced)
        d.append(di)
        p.append(pi)
    t = table.copy()
    t["diff"] = np.concatenate(d)
    t["p"] = np.concatenate(p)
    t["selective"] = (t.p < 0.05) & ((t["diff"] > 0) if positive_only else True)
    t["selective_any_direction"] = t.p < 0.05
    obs = {a: int(t.selective[t.area == a].sum()) for a in area_list}
    null = perm_null_counts(blocks, balanced, positive_only, n_null=n_null, seed=seed)
    pv, null_counts = area_pvalues(null, t.area.to_numpy(), obs, area_list)
    summary = pd.DataFrame({"area": area_list, "n": [int((t.area == a).sum()) for a in area_list],
                            "selective": [obs[a] for a in area_list], "p_perm": pv,
                            "null_mean": null_counts.mean(0),
                            "null_95th": np.percentile(null_counts, 95, axis=0)})
    summary["mc_se"] = np.sqrt(summary.p_perm * (1 - summary.p_perm) / n_null)
    return t, summary


def hfb_onsets(s, cuts):
    """The onset sets of one session for hfb_session: recognition trials (memory, 0.2 to 1.7 s,
    and a baseline 1 s before onset), scene cuts (events, 0 to 1 s), and the same read on the
    file's own LFP clock (onsets 10 s earlier on the code's clock), a check of the alignment."""
    t0, t1 = movie_window(s)
    r = recog_trials(s)
    ons = cut_onsets(s, cuts)
    return {"enc": (t0, t1, {"events": (ons, EVENT_WINDOW),
                             "events_fileclock": (ons - LFP_PAD_S, EVENT_WINDOW)}),
            "recog": (float(r.start_time.iloc[0]), float(r.stop_time.iloc[-1]),
                      {"memory": (r.start_time.to_numpy(), MEMORY_WINDOW),
                       "memory_pre": (r.start_time.to_numpy(), (-1.0, 0.0)),
                       "memory_fileclock": (r.start_time.to_numpy() - LFP_PAD_S, MEMORY_WINDOW),
                       "memory_pre_fileclock": (r.start_time.to_numpy() - LFP_PAD_S, (-1.0, 0.0))})}


def hfb_job(args):
    """One session, both electrode types (for a process pool)."""
    url, onsets = args
    return {et: hfb_session(url, et, onsets) for et in ["LFP_micro", "LFP_macro"]}
