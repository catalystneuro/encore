"""Loading and measures for dandiset 001619, Kaku, Liu et al. (2025), "A brainstem map of
orofacial rhythms", bioRxiv doi:10.1101/2025.01.27.635041.

Each NWB file holds one Neuropixels insertion (probe p1 or p2) of one session: the units with
their quality metrics and CCF positions (`units/histology`), the side and bottom DeepLabCut
tracking per trial (1471 frames at 3.4 ms), the 3D tracking, and the 25 kHz airflow per trial.
Trials are stored separately; every per-trial time starts at 0 at the trial start. The two
probes of a session carry the same behaviour (checked in the notebook), so behaviour is read
once per session. Files are streamed from the archive at the pinned version; nothing is written
to disk.

Spike times: `units/spike_times_index` holds the start offset of each unit, not its end, so the
standard NWB reading gives each unit the spikes of the unit before it. Spikes are read here by
the per-unit, per-trial spike counts of `units/unit and trial pairs`, which agree with the index
read as starts (checked in the notebook).

Where the parameters come from. "Code" is the paper's analysis code, process_mat.py and
generate_figures.py in https://github.com/NuoLiLabBCM/KakuEtAl2025 at commit fbc0abe, which
the claims file names and whose choices it adopts in its header.

- Unit filter: code get_good_units (amplitude > 150 uV, ISI violation < 10, rate > 0.2 Hz,
  presence ratio > 0.9, amplitude cutoff < 0.15); the Methods add drift metric < 0.5
  (claims file, variant V1).
- Trial filter: code get_good_trials.
- Tongue onsets and offsets, lick bouts, inspiration onsets: code get_movement_timing, ported
  line by line (tongue likelihood > 0.95 in both views; airflow z-scored, 3.4 ms moving
  average and down-sampling, 5th-order Butterworth 1-15 Hz, Hilbert phase + pi crossing pi,
  kept when the trace crosses -0.5 before the next onset). Times are on the code's timeline:
  the first 1471 frames (5.0014 s) of each trial placed end to end.
- Swallows: code detect_swallows and get_breathing, ported; swallow-aligned licks and breaths:
  code get_licks_around_event and get_breaths_around_event.
- Phase tuning: code get_unit_jaw_tuning and get_unit_breath_tuning (side-camera jaw_y,
  3-15 Hz; airflow down-sampled 100 times to 250 Hz, 1-10 Hz; filtfilt; Hilbert phase + pi;
  20 bins; spike counts divided by phase occupancy). The filter order is a reading (claims
  file V2: Methods "4-pole", read as order 4 (a) or order 2 (b); the code's order 5 as a
  variant).
- Tuning fit: the circular Gaussian of the Methods and code (vonMise_f), with the code's bounds
  (width 0 to pi/2, preferred phase 0 to 2 pi, amplitude and baseline >= 0). The code fits it
  with scipy curve_fit from two starting phases; here, so that 1000 resamples per unit can be
  fitted (claims file V3), the fit is a grid search over width and preferred phase with the
  amplitude and baseline solved in closed form at each grid point (`fit_tuning_grid`). This is
  a different optimiser for the same model; the notebook compares it with the code's
  curve_fit on a sample of units. MI = (r(phi) - r(phi - pi)) / r(phi) (Methods).
- Resampling (claims file V3): a resample of n spike phases drawn with replacement from a
  unit's spike phases, or from the session's phases, has a multinomial histogram with the
  observed bin probabilities; the resampled histograms are drawn that way, on the measured
  histogram's bins (the code's np.random.choice and np.histogram give the same distribution,
  with bin edges set by each sample's range, which differ by a small fraction of a bin).
- Peak differences of Figs 1g, 1i, 4e and 4f: code get_peak_diff_lick_behv,
  get_peak_diff_breath_behv, get_peak_diff_lick_unit, get_peak_diff_breath_unit, and the
  first-peak difference of generate_figures.plot_summary.
- Swallow modulation: code get_swallow_tuning (windows -0.3 to -0.1, -0.05 to 0.05 and 0.1 to
  0.3 s; 1000 bootstrap resamples; at least 20 swallows); generate_activity_maps.m (mean of
  the two MIs, max p <= 0.01, MI > 0.3). Swallow PSTH: code compute_psth (1 ms bins, 50 ms
  boxcar, -1 to 1 s).
"""

from __future__ import annotations

import hashlib
import re
from concurrent.futures import ProcessPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
from scipy import signal, stats

DANDISET_ID = "001619"
DANDISET_VERSION = "0.251027.1953"
API = "https://api.dandiarchive.org/api"
ONTOLOGY_URL = ("https://raw.githubusercontent.com/int-brain-lab/iblatlas/"
                "b88da5d8541d77285565fdb3f86f4f69c50b9e68/iblatlas/allen_structure_tree.csv")

FRAME_S = 0.0034           # code: bin_width
N_FRAMES = 1471            # code: traces_len
TRIAL_S = N_FRAMES * FRAME_S
BREATH_FS = 25000          # Methods; the timestamps step by 4e-5 s (checked in the notebook)
BREATH_DS = 100            # code get_unit_breath_tuning
N_BINS = 20                # code
FILTER_ORDERS = (4, 2, 5)  # claims file V2: (a) 4, (b) 2, code 5
MI_TUNED = 0.6             # Results and Methods
P_TUNED = 0.001

BEH = "processing/processing module/breathing_behavior/breathing"


# ----------------------------------------------------------------------------- archive

def list_assets():
    """Assets of the pinned version: path, asset id, size, subject, session, probe, url."""
    import json
    import urllib.request
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/?page_size=1000"
    rows = []
    while url:
        page = json.load(urllib.request.urlopen(url))
        rows += page["results"]
        url = page["next"]
    out = []
    for a in rows:
        m = re.match(r"(sub-[^/]+)/\1_ses-(.+)-(p\d)_behavior\+core\.nwb$", a["path"])
        out.append({"path": a["path"], "asset_id": a["asset_id"], "size": a["size"],
                    "subject": m.group(1)[4:], "session": m.group(2), "probe": m.group(3),
                    "url": f"{API}/assets/{a['asset_id']}/download/"})
    return pd.DataFrame(out).sort_values(["subject", "session", "probe"]).reset_index(drop=True)


def dandiset_metadata():
    import json
    import urllib.request
    return json.load(urllib.request.urlopen(f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/"))


def open_nwb(url):
    return h5py.File(remfile.File(url), "r")


def _str(v):
    if isinstance(v, bytes):
        return v.decode().strip()
    if isinstance(v, np.ndarray) and v.size == 1:
        return _str(v.reshape(-1)[0])
    return v


def ontology():
    """Allen CCF structure tree (iblatlas copy at a pinned commit): name -> acronym, path."""
    df = pd.read_csv(ONTOLOGY_URL)
    df = df[df.acronym != "void"]
    return df


def region_table(names, onto):
    """For each CCF region name in the files: acronym, and the major divisions (CB, P, MY, ...)
    it falls under, from the structure-id path."""
    def norm(n):  # the iblatlas copy drops the commas of the Allen names
        return " ".join(str(n).replace(",", " ").lower().split())

    by_name = {norm(n): r for n, r in zip(onto.name, onto.itertuples())}
    acr_by_id = dict(zip(onto.id, onto.acronym))
    rows = []
    for n in sorted(set(names)):
        r = by_name.get(norm(n))
        if r is None:
            rows.append({"name": n, "acronym": None, "ancestors": ()})
            continue
        ids = [int(i) for i in str(r.structure_id_path).strip("/").split("/") if i]
        rows.append({"name": n, "acronym": r.acronym, "ancestors": tuple(acr_by_id.get(i) for i in ids)})
    return pd.DataFrame(rows)


# ----------------------------------------------------------------------------- reading

def read_probe_meta(url):
    """Everything about one file except spikes, airflow and tracking arrays."""
    with open_nwb(url) as f:
        m = {k: f["analysis/unit_metrics"][k][:] for k in f["analysis/unit_metrics"] if k != "id"}
        units = pd.DataFrame(m)
        n = len(units)
        lengths = {"metrics": n, "units_id": len(f["units/id"]),
                   "histology": len(f["units/histology/unit_region"]),
                   "unit_info": len(f["units/unit_info/unit_id"]),
                   "pairs": f["units/unit and trial pairs"].shape[0],
                   "spike_index": len(f["units/spike_times_index"])}

        def put(col, v):
            v = np.asarray(v, dtype=object if isinstance(v[0], str) else None) if len(v) else np.array([])
            out = np.full(n, None if v.dtype == object else np.nan, dtype=v.dtype if v.dtype == object else float)
            k = min(n, len(v))
            out[:k] = v[:k]
            units[col] = out

        put("id", f["units/id"][:])
        put("metric_id", f["analysis/unit_metrics/id"][:])
        h = f["units/histology"]
        put("region", [_str(x) for x in h["unit_region"][:]])
        for k in ("ccf_x", "ccf_y", "ccf_z"):
            put(k, h[k][:])
        ui = f["units/unit_info"]
        for k in ui:
            if k != "id":
                v = ui[k][:]
                put("info_" + k, [_str(x) for x in v] if v.dtype == object else v)
        pairs = f["units/unit and trial pairs"][:]
        put("n_spikes", pairs.sum(1))
        si = f["units/spike_times_index"][:]
        n_st = f["units/spike_times"].shape[0]
        index_is_start = bool(si[0] == 0 and np.array_equal(np.diff(si), pairs.sum(1)[:-1])
                              and n_st - si[-1] == pairs[-1].sum())
        index_is_end = bool(np.array_equal(np.diff(np.r_[0, si]), pairs.sum(1)))
        pi_ = f["analysis/probe_insertion_info"]
        insertion = {k: _str(pi_[k][()]) for k in pi_ if k != "id"}
        trials = f["intervals/trials"]
        side_tr = f["processing/DLC_tracking/side-facing_camera/jaw"]["trial"]
        bot_tr = f["processing/DLC_tracking/bottom-facing_camera/jaw"]["trial"]
        meta = {
            "session_description": _str(f["session_description"][()]),
            "session_id": _str(f["general/session_id"][()]),
            "session_start_time": _str(f["session_start_time"][()]),
            "subject_id": _str(f["general/subject/subject_id"][()]),
            "sex": _str(f["general/subject/sex"][()]),
            "age": _str(f["general/subject/age"][()]),
            "genotype": _str(f["general/subject/genotype"][()]),
            "stimulus": _str(f["general/stimulus"][()]),
            "n_trials": len(trials["id"]),
            "trial_start_max": float(np.max(trials["start_time"][:])),
            "trial_duration_min": float(np.min(trials["trial_duration"][:])),
            "trial_duration_max": float(np.max(trials["trial_duration"][:])),
            "trial_columns": list(_str(c) for c in trials.attrs["colnames"]),
            "n_dlc_rows_side": len(side_tr), "n_dlc_rows_bottom": len(bot_tr),
            "n_3d_rows": f["processing/3D_tracking/tongue_bottom"].shape[0],
            "tracking_info": tuple(f["processing/3D_tracking/tracking_info"][0].tolist()),
            "n_breath": f[BEH + "/data"].shape[0],
            "breath_head_hash": hashlib.md5(f[BEH + "/data"][:200_000].tobytes()).hexdigest(),
            "jaw_head_hash": hashlib.md5(f["processing/DLC_tracking/side-facing_camera/jaw"][:20_000].tobytes()).hexdigest(),
            "breath_idx_sum": int(f[BEH + "/data_idx"][:].sum()),
            "acquisition": list(f["acquisition"].keys()),
            "stimulus_presentation": list(f["stimulus/presentation"].keys()),
            "index_is_start": index_is_start, "index_is_end": index_is_end,
            "n_units": len(units), **{"len_" + k: v for k, v in lengths.items()},
            **{"ins_" + k: v for k, v in insertion.items()},
        }
    return meta, units


def good_units(units, drift=False):
    """Code get_good_units; with drift=True also the Methods' drift metric < 0.5 (V1)."""
    ok = ((units.presence_ratio > 0.9) & (units.amplitude_cutoff < 0.15) & (units.avg_firing_rate > 0.2)
          & (units.isi_violation < 10) & (units.unit_amp > 150))
    if drift:
        ok &= units.drift_metric < 0.5
    return ok.to_numpy()


def _read_dlc(f, cam):
    g = f[f"processing/DLC_tracking/{cam}-facing_camera"]
    out = {}
    for part in ("jaw", "tongue"):
        d = g[part][:]
        out[part] = d
    return out


def _per_trial(rec, field, trials_present, trial):
    """Rows of a DLC record array for one trial as an (n_frames,) array."""
    return rec[field][rec["trial"] == trial]


def read_session(url, probe_urls):
    """Behaviour of a session (from one file) and the good units' spikes of each probe."""
    with open_nwb(url) as f:
        side = _read_dlc(f, "side")
        bottom = _read_dlc(f, "bottom")
        info = f["processing/3D_tracking/tracking_info"][0]
        video_fs = float(info[0])
        trial_len = float(info[2])
        t3 = f["processing/3D_tracking/tongue_bottom"][:]
        j3 = f["processing/3D_tracking/jaw_side"][:]
        idx = f[BEH + "/data_idx"][:]
        ds = f[BEH + "/data"]
        n = ds.shape[0]
        raw = np.empty(n)
        step = ds.chunks[0] * 64 if ds.chunks else 2_000_000
        for s in range(0, n, step):
            raw[s:s + step] = ds[s:s + step]
        ts0 = f[BEH + "/timestamps"][:3]
    starts = np.r_[0, np.cumsum(idx)[:-1]]
    breath_dt = float(ts0[1] - ts0[0])
    # code get_good_trials: trials tracked in both cameras, no negative jaw likelihood
    tr_side = np.unique(side["jaw"]["trial"])
    tr_bot = np.unique(bottom["jaw"]["trial"])
    trials = []
    for t in np.intersect1d(tr_side, tr_bot):
        if (side["jaw"]["likelihood"][side["jaw"]["trial"] == t] < 0).any():
            continue
        if (bottom["jaw"]["likelihood"][bottom["jaw"]["trial"] == t] < 0).any():
            continue
        trials.append(int(t))
    trials = np.array(trials)

    def frames(rec, field):
        out = np.full((len(trials), N_FRAMES), np.nan)
        tr = rec["trial"]
        for i, t in enumerate(trials):
            v = rec[field][tr == t]
            out[i, :min(len(v), N_FRAMES)] = v[:N_FRAMES]
        return out

    sess = {
        "video_fs": video_fs, "trial_len": trial_len, "breath_dt": breath_dt,
        "n_trials_total": len(idx), "trials": trials,
        "side_tongue_l": frames(side["tongue"], "likelihood"),
        "bottom_tongue_l": frames(bottom["tongue"], "likelihood"),
        "jaw_y": frames(side["jaw"], "y"),
        "trial_samples": idx,
    }
    # 3D tongue (bottom) and jaw (side) per good trial, for protrusion and lick angle
    t3d = np.full((len(trials), N_FRAMES, 3), np.nan)
    j3d = np.full((len(trials), N_FRAMES, 3), np.nan)
    for i, t in enumerate(trials):
        for rec, out in ((t3, t3d), (j3, j3d)):
            sel = rec["idx"] == t
            if sel.any():
                v = np.stack([rec["x"][sel], rec["y"][sel], rec["z"][sel]], 1)[:N_FRAMES]
                out[i, :len(v)] = v
    sess["tongue3d"] = t3d
    sess["jaw3d"] = j3d
    # airflow: the first 1471 frames' worth (ts < 5.0014 s) and the first 5 s, per good trial
    n_move = int(np.sum(np.arange(int(TRIAL_S / breath_dt) + 2) * breath_dt < TRIAL_S))
    n_tune = int(np.sum(np.arange(int(5 / breath_dt) + 2) * breath_dt < 5))
    move = np.empty((len(trials), n_move))
    tune = []
    for i, t in enumerate(trials):
        s = starts[t - 1]
        move[i] = raw[s:s + n_move]
        tune.append(raw[s:s + min(n_tune, idx[t - 1])][::BREATH_DS])
    del raw
    sess["breath_move"] = move
    sess["breath_tune"] = tune
    sess["n_move"] = n_move
    # spikes of the code's good units, per good trial, for each probe
    sess["probes"] = {}
    for probe, purl in probe_urls.items():
        with open_nwb(purl) as f:
            m = {k: f["analysis/unit_metrics"][k][:] for k in
                 ("presence_ratio", "amplitude_cutoff", "avg_firing_rate", "isi_violation", "unit_amp", "drift_metric")}
            units = pd.DataFrame(m)
            gu = np.where(good_units(units))[0]
            pairs = f["units/unit and trial pairs"][:]
            si = f["units/spike_times_index"][:].astype(np.int64)
            st = f["units/spike_times"][:]
        spikes = []
        for u in gu:
            counts = pairs[u]
            off = np.r_[0, np.cumsum(counts)].astype(np.int64) + si[u]
            spikes.append([np.sort(st[off[t - 1]:off[t]]) for t in trials])
        sess["probes"][probe] = {"good_idx": gu, "spikes": spikes}
    return sess


# ----------------------------------------------------------------------------- behaviour

def _ma_downsample(x, w):
    """np.convolve(x, ones(w)/w, 'same')[w::w], computed only at the kept samples."""
    c = np.r_[0.0, np.cumsum(x)]
    n = len(x)
    j = np.arange(w, n, w)
    lo = np.clip(j - (w - 1) // 2 - (1 if w % 2 == 0 else 0), 0, n)
    hi = np.clip(j + w // 2 + 1 - (1 if w % 2 == 0 else 0), 0, n)
    # numpy 'same' for odd w centres the kernel; for even w it is shifted by one
    return (c[hi] - c[lo]) / w


def movement_timing(sess):
    """Code get_movement_timing: tongue onsets and offsets, lick bouts and inspiration onsets
    on the concatenated timeline (s)."""
    bw = FRAME_S
    s_l = sess["side_tongue_l"]
    b_l = sess["bottom_tongue_l"]
    tl = ((s_l > 0.95) & (b_l > 0.95)).astype(float).reshape(-1)
    tl = tl[1:]  # code: moving average of width 1, then [window_size::window_size]
    # airflow
    br = sess["breath_move"].reshape(-1)
    br = (br - br.mean()) / br.std()
    w = int(round(bw / sess["breath_dt"]))
    gb = _ma_downsample(br, w)
    b, a = signal.butter(5, (1, 15), btype="band", fs=1 / bw)
    phase_b = np.angle(signal.hilbert(signal.filtfilt(b, a, gb))) + np.pi
    cond = (phase_b < np.pi) & (np.roll(phase_b, -1) >= np.pi)
    insp = np.argwhere(cond)[:, 0] * bw
    a_cond = (gb > -0.5) & (np.roll(gb, -1) <= -0.5)
    insp_amp = np.argwhere(a_cond)[:, 0] * bw
    keep = [insp[i] for i in range(len(insp) - 1)
            if np.any((insp_amp > insp[i]) & (insp_amp < insp[i + 1]))]
    insp = np.array(keep)
    # tongue
    on = np.argwhere((tl < 0.5) & (np.roll(tl, -1) >= 0.5))[:, 0] * bw
    off = np.argwhere((tl > 0.5) & (np.roll(tl, -1) <= 0.5))[:, 0] * bw
    ton_all = on.copy()
    ilf = 1 / np.diff(on)
    on = on[:-1]
    off = off[:-1]
    idx = np.argwhere((ilf > 3) & (ilf < 9))[:, 0]
    nxt = np.diff(idx)
    lick_idx = np.array([t for i, t in enumerate(idx[:-2]) if nxt[i] == 1], dtype=int)
    d = np.diff(lick_idx)
    b_on = np.argwhere(np.roll(d, 1) >= 2)[:, 0]
    b_off = np.argwhere(d >= 2)[:, 0]
    if len(b_on) == 0 or b_on[0] != 0:
        b_on = np.r_[0, b_on]
        b_off = np.r_[b_off, len(lick_idx) - 1]
    bout_on = on[lick_idx[b_on]]
    bout_off = on[np.minimum(lick_idx[b_off] + 2, len(on) - 1)]
    return {"tongue_onset": on, "tongue_offset": off, "tongue_onset_all": ton_all,
            "bout_on": bout_on, "bout_off": bout_off, "inspir_onset": insp,
            "breath_ds": gb, "phase_b": phase_b}


def get_breathing(sess):
    """Code get_breathing: negated z-scored 3.4 ms airflow, raw Hilbert amplitude and phase."""
    br = sess["breath_move"].reshape(-1)
    br = (br - br.mean()) / br.std()
    w = int(round(FRAME_S / sess["breath_dt"]))
    gb = _ma_downsample(br, w) * -1
    res = np.r_[gb, gb[-1]]
    h = signal.hilbert(res)
    n_tr = sess["breath_move"].shape[0]
    return res.reshape(n_tr, -1), np.angle(h).reshape(n_tr, -1)


def detect_swallows(sess, tongue_on):
    """Code detect_swallows: swallow onsets (frame index within trial) per trial."""
    fs = sess["video_fs"]
    tr_len = sess["trial_len"]
    breathing, phase = get_breathing(sess)
    out = []
    for i in range(breathing.shape[0]):
        breath = np.convolve(breathing[i], np.ones(5) / 5, mode="same")
        pk, _ = signal.find_peaks(breath, distance=10)
        ph = phase[i][pk]
        pk = pk[(ph > 1.2) & (ph < 1.7)]
        t0 = tr_len * i
        ton = tongue_on[(tongue_on >= t0) & (tongue_on <= t0 + tr_len)] - t0
        kept = []
        if ton.size:
            for p in pk / fs:
                bef = np.where((ton <= p) & (ton >= p - 1.5))[0]
                aft = np.where((ton >= p) & (ton <= p + 0.25))[0]
                if bef.size >= 5 and aft.size >= 1 and p - ton[bef[-1]] < 0.5:
                    ilf = 1 / np.diff(ton[bef])[-4:]
                    if ((ilf > 3.5) & (ilf < 13)).all():
                        kept.append(int(p * fs))
        kept = np.array(kept)
        vel = np.diff(breath)
        inb = (vel >= -0.07) & (vel <= 0.07)
        runs = []
        count, start = 0, None
        for j in range(len(vel)):
            if inb[j]:
                count += 1
                if start is None:
                    start = j
            else:
                if count >= 10:
                    runs.append((start, start + count, count / fs))
                count, start = 0, None
        if count >= 2:
            runs.append((start, start + count, count / fs))
        val = []
        for s, e, dur in runs:
            if dur < 0.05:
                continue
            s = s + 1
            if kept.size and np.any((kept >= s) & (kept <= e)):
                val.append(int(s))
        out.append(np.array(val, dtype=int))
    return out


def events_around_swallows(swallows, times, tr_len):
    """Code get_licks_around_event / get_breaths_around_event."""
    fs = 1000 / 3.4
    res = []
    for i, ev in enumerate(swallows):
        for el in ev:
            start = i * tr_len
            res.append(times[(times >= start) & (times <= start + tr_len)] - el / fs - start)
    return res


def swallow_intervals(aligned, max_ili, min_ili=1 / 15, num_before=4, num_after=2):
    """Code plot_licking_swallow_summary / plot_breath_swallow_summary, returning cycle 0, 1
    and -1 for every kept event, ordered by cycle 0 (longest first), and the latency of the
    first event after the swallow."""
    rows = []
    for k, lick in enumerate(aligned):
        lick = np.atleast_1d(lick)
        pre, post = lick[lick < 0], lick[lick >= 0]
        if post.size >= num_after and pre.size >= num_before:
            c0 = post[0] - pre[-1]
            if min_ili < c0 < max_ili:
                rows.append({"event": k, "c0": c0, "c1": post[1] - post[0], "cm1": pre[-1] - pre[-2],
                             "latency": post[0], "pre_last": pre[-1]})
    df = pd.DataFrame(rows)
    if len(df):
        df = df.iloc[np.argsort(df.c0.to_numpy(), kind="quicksort")[::-1]].reset_index(drop=True)
    return df


def peak_diff_lick_behv(mt, spikes=None, n_trial=None, unit=False):
    """Code get_peak_diff_lick_behv (unit=False) and the event selection of
    get_peak_diff_lick_unit. Returns the selection and the behavioural peaks."""
    insp, ton = mt["inspir_onset"], mt["tongue_onset"]
    on, off = mt["bout_on"], mt["bout_off"]
    insp_l = np.hstack([insp[(insp > on[i] + 0.2) & (insp < off[i] - 0.2)] for i in range(len(on))]) if len(on) else np.array([])
    max_ibi = np.max(np.diff(insp))
    rows = []
    for i in range(2, len(insp_l) - 2):
        lick = ton[(ton > insp_l[i - 2]) & (ton < insp_l[i + 2])]
        lick_in = lick[(lick > insp_l[i]) & (lick < insp_l[i + 1])]
        if lick_in.size:
            bef = lick[lick < insp_l[i]]
            if len(bef):
                rows.append((insp_l[i], lick - insp_l[i], lick_in[-1] - insp_l[i], bef[-1] - insp_l[i],
                             lick_in.size, insp_l[i + 1] - insp_l[i]))
    if not rows:
        return None
    t0 = np.array([r[0] for r in rows])
    licks = [r[1] for r in rows]
    lick2 = np.array([r[2] for r in rows])
    lbef = np.array([r[3] for r in rows])
    nl = np.array([r[4] for r in rows])
    ibi = np.array([r[5] for r in rows])
    k = ibi < max_ibi
    t0, licks, lick2, lbef, nl, ibi = t0[k], [l for l, kk in zip(licks, k) if kk], lick2[k], lbef[k], nl[k], ibi[k]
    rem1 = np.where((nl == 1) & (lbef > -0.05) & (lbef < 0))[0]
    rem2 = np.where((nl == 2) & (lick2 > ibi - 0.05) & (lick2 < ibi))[0]
    keep = np.setdiff1d(np.arange(len(ibi)), np.r_[rem1, rem2])
    t0, licks, lbef, nl, ibi, lick2 = t0[keep], [licks[i] for i in keep], lbef[keep], nl[keep], ibi[keep], lick2[keep]
    order = np.argsort(ibi)[::-1]
    t0, licks, lbef, nl, ibi, lick2 = t0[order], [licks[i] for i in order], lbef[order], nl[order], ibi[order], lick2[order]
    out = {"t0": t0, "licks": licks, "lick_bef": lbef, "n_licks": nl, "ibi": ibi, "max_ibi": max_ibi,
           "last_lick_to_next_insp": ibi - lick2}
    if not (nl == 2).any():
        return out
    d = np.median(ibi[nl == 2])
    i1 = np.where((ibi < d) & (nl == 2))[0]
    i2 = np.where((ibi > d) & (nl == 2))[0]
    out.update(i_fast=i1, i_slow=i2)
    bins = np.arange(-0.4, 1, 0.02)
    centres = bins[1:] - 0.01
    if len(i1) >= 40 and len(i2) >= 40:
        p1 = np.mean([np.histogram(licks[i], bins)[0] for i in i1], 0) / 0.02
        p2 = np.mean([np.histogram(licks[i], bins)[0] for i in i2], 0) / 0.02
        pk1 = _peaks(p1, centres, 5, 0.14, (0.12, 0.32))
        pk2 = _peaks(p2, centres, 5, 0.14, (0.16, 0.36))
        out.update(peaks_fast=pk1, peaks_slow=pk2,
                   diff=(pk2[0] - pk1[0]) if len(pk1) and len(pk2) else np.nan)
    else:
        out["diff"] = np.nan
    # unit version: 40 fastest and 40 slowest (code n_trial)
    out["unit_fast"] = i1[:40]
    out["unit_slow"] = i2[-40:]
    return out


def peak_diff_breath_behv(mt):
    """Code get_peak_diff_breath_behv (and the event selection of get_peak_diff_breath_unit)."""
    insp, ton = mt["inspir_onset"], mt["tongue_onset"]
    on, off = mt["bout_on"], mt["bout_off"]
    ton_l = np.hstack([ton[(ton > on[i] + 0.2) & (ton < off[i] - 0.2)] for i in range(len(on))]) if len(on) else np.array([])
    max_ili = np.max(np.diff(insp))
    rows = []
    for i in range(2, len(ton_l) - 2):
        br = insp[(insp > ton_l[i - 2]) & (insp < ton_l[i + 2])]
        bin_ = br[(br > ton_l[i]) & (br < ton_l[i + 1])]
        if bin_.size:
            rows.append((ton_l[i], br - ton_l[i], ton_l[i + 1] - ton_l[i]))
    if not rows:
        return None
    t0 = np.array([r[0] for r in rows])
    breaths = [r[1] for r in rows]
    ili = np.array([r[2] for r in rows])
    k = ili < max_ili
    t0, breaths, ili = t0[k], [b for b, kk in zip(breaths, k) if kk], ili[k]
    order = np.argsort(ili)[::-1]
    t0, breaths, ili = t0[order], [breaths[i] for i in order], ili[order]
    d = np.median(ili)
    i1 = np.where(ili < d)[0]
    i2 = np.where(ili > d)[0]
    out = {"t0": t0, "breaths": breaths, "ili": ili, "i_fast": i1, "i_slow": i2}
    bins = np.arange(-0.1, 0.6, 0.02)
    centres = bins[1:] - 0.01
    if len(i1) >= 100 and len(i2) >= 100:
        p1 = np.mean([np.histogram(breaths[i], bins)[0] for i in i1], 0) / 0.02
        p2 = np.mean([np.histogram(breaths[i], bins)[0] for i in i2], 0) / 0.02
        pk1 = _peaks(p1, centres, 7, 0.24, (0, 0.22))
        pk2 = _peaks(p2, centres, 7, 0.24, (0, 0.24))
        out.update(peaks_fast=pk1, peaks_slow=pk2,
                   diff=(pk2[0] - pk1[0]) if len(pk1) and len(pk2) else np.nan)
    else:
        out["diff"] = np.nan
    return out


def _peaks(psth, centres, min_height, dist_s, window):
    thr = max(np.mean(psth) + np.std(psth), min_height)
    pk = signal.find_peaks(psth, height=thr, distance=dist_s / 0.02)[0]
    t = centres[pk]
    return t[(t > window[0]) & (t < window[1])]


def unit_peak_diffs(train, t0, i_fast, i_slow, psth_s, psth_e, wins, dist_s, min_height=10):
    """Code get_peak_diff_*_unit for one unit: spike PSTHs (20 ms bins) around the events of
    the fast and slow groups, first peak above max(mean + SD, 10 spikes/s) in each window;
    slow minus fast (generate_figures.plot_summary)."""
    bins = np.arange(psth_s, psth_e, 0.02)
    centres = bins[1:] - 0.01
    pks = []
    for idx, win in zip((i_fast, i_slow), wins):
        edges = t0[idx][:, None] + bins[None, :]
        c = np.searchsorted(train, edges.ravel(), side="left").reshape(edges.shape)
        psth = np.diff(c, axis=1).mean(0) / 0.02
        pks.append(_peaks(psth, centres, min_height, dist_s, win))
    return (pks[1][0] - pks[0][0]) if len(pks[0]) and len(pks[1]) else np.nan


# ----------------------------------------------------------------------------- tuning

def phases(sess):
    """Jaw and breathing phase (+ pi) for each filter order: jaw (trials x 1471) and breathing
    (kept trials x 1250, with their indices)."""
    fs = sess["video_fs"]
    jaw = sess["jaw_y"]
    n_tr = jaw.shape[0]
    out = {"jaw": {}, "breath": {}}
    jy = jaw.reshape(-1)
    jy = np.where(np.isnan(jy), np.nanmean(jy), jy)
    for order in FILTER_ORDERS:
        b, a = signal.butter(order, (3, 15), btype="band", fs=fs)
        out["jaw"][order] = (np.angle(signal.hilbert(signal.filtfilt(b, a, jy))) + np.pi).reshape(n_tr, -1)
    n_tune = int(5 * BREATH_FS / BREATH_DS)
    keep = np.array([i for i, d in enumerate(sess["breath_tune"]) if len(d) == n_tune], dtype=int)
    bt = np.vstack([sess["breath_tune"][i] for i in keep]).reshape(-1) if len(keep) else np.array([])
    for order in FILTER_ORDERS:
        b, a = signal.butter(order, (1, 10), btype="band", fs=BREATH_FS / BREATH_DS)
        out["breath"][order] = (np.angle(signal.hilbert(signal.filtfilt(b, a, bt))) + np.pi).reshape(len(keep), -1)
    out["breath_trials"] = keep
    return out


def spike_phase_hist(spikes_by_trial, phase, fs, n_max, trial_sel=None):
    """Histogram (20 bins) of the phases at a unit's spikes, and the occupancy, as the code."""
    allp = []
    trials = range(len(spikes_by_trial)) if trial_sel is None else trial_sel
    for row, t in enumerate(trials):
        idx = (spikes_by_trial[t] * fs).astype(int)
        idx = idx[idx < n_max]
        allp.append(phase[row][idx])
    allp = np.hstack(allp) if allp else np.array([])
    return allp


def tuning_bins(phase_all, spike_phase):
    """Code: counts on np.histogram(spike phases, 20) and occupancy on np.histogram(session
    phases, 20); bin centres from the occupancy edges."""
    occ, edges = np.histogram(phase_all, bins=N_BINS)
    if len(spike_phase):
        cnt, _ = np.histogram(spike_phase, bins=N_BINS)
    else:
        cnt = np.zeros(N_BINS, int)
    centres = edges[:-1] + (edges[1] - edges[0]) / 2
    return cnt, occ, centres, edges


def _circ_dist(x, mu):
    d = np.mod(np.abs(x - mu), 2 * np.pi)
    return np.where(d > np.pi, 2 * np.pi - d, d)


_GRID_SD = np.geomspace(0.03, np.pi / 2, 24)
_GRID_MU = np.linspace(0, 2 * np.pi, 48, endpoint=False)


def _grid(centres):
    sd, mu = np.meshgrid(_GRID_SD, _GRID_MU, indexing="ij")
    sd, mu = sd.ravel(), mu.ravel()
    g = np.exp(-0.5 * (_circ_dist(centres[None, :], mu[:, None]) / sd[:, None]) ** 2)
    return sd, mu, g


def fit_tuning_grid(Y, centres, chunk=4000):
    """Least-squares fit of amp * exp(-0.5 (d(x, mu)/sd)^2) + base to each row of Y (rates per
    phase bin): grid over sd (24 steps, 0.03 to pi/2) and mu (7.5 degree steps), amp and base in closed form
    with the code's bounds. Returns MI and preferred phase per row."""
    sd, mu, g = _grid(centres)
    n = Y.shape[1]
    Sgg = (g * g).sum(1)
    Sg1 = g.sum(1)
    det = n * Sgg - Sg1 ** 2
    ered = np.exp(-0.5 * (np.pi / sd) ** 2)
    mi = np.empty(len(Y))
    pref = np.empty(len(Y))
    g = g.astype(np.float32)
    Sgg, Sg1, det = Sgg.astype(np.float32), Sg1.astype(np.float32), det.astype(np.float32)
    for s in range(0, len(Y), chunk):
        y = Y[s:s + chunk].astype(np.float32)
        yg = y @ g.T
        sy = y.sum(1)[:, None]
        yy = (y * y).sum(1)[:, None]
        amax = (y.max(1) + y.min(1))[:, None]
        bmax = y.max(1)[:, None]

        def sse_of(a, b):
            return yy - 2 * (a * yg + b * sy) + a * a * Sgg + 2 * a * b * Sg1 + b * b * n

        a0 = (n * yg - Sg1 * sy) / det
        b0 = (Sgg * sy - Sg1 * yg) / det
        cands = [(a0, b0)]
        a1 = np.clip(yg / Sgg, 0, amax)            # base at 0
        cands.append((a1, np.zeros_like(a1)))
        b2 = np.clip(sy / n, 0, bmax) + 0 * yg      # amp at 0
        cands.append((np.zeros_like(b2), b2))
        b3 = np.clip((sy - amax * Sg1) / n, 0, bmax)  # amp at its bound
        cands.append((amax + 0 * b3, b3))
        sse = np.full(yg.shape, np.inf)
        a = np.zeros(yg.shape)
        b = np.zeros(yg.shape)
        for ca, cb in cands:
            ok = (ca >= 0) & (ca <= amax) & (cb >= 0) & (cb <= bmax)
            e = np.where(ok, sse_of(ca, cb), np.inf)
            better = e < sse
            sse = np.where(better, e, sse)
            a = np.where(better, ca, a)
            b = np.where(better, cb, b)
        k = np.argmin(sse, 1)
        r = np.arange(len(y))
        ak, bk = a[r, k], b[r, k]
        rmax = ak + bk
        rmin = ak * ered[k] + bk
        with np.errstate(invalid="ignore", divide="ignore"):
            mi[s:s + chunk] = np.where(rmax > 0, (rmax - rmin) / rmax, np.nan)
        pref[s:s + chunk] = mu[k]
    return mi, pref


def code_phase_tuning(datax, datay):
    """The code's compute_phase_tuning (scipy curve_fit from two starts), for comparison."""
    from scipy import optimize

    def f(x, std, mean, amp, base):
        return amp * np.exp(-0.5 * (_circ_dist(x, np.full_like(x, mean)) / std) ** 2) + base

    mx, mn = np.amax(datay), np.amin(datay)
    mi_ = np.where(datay == mx)[0][0]
    best = None
    for p0m in (datax[mi_], 0):
        try:
            p, _ = optimize.curve_fit(f, datax, datay, p0=[1, p0m, mx - mn, mn],
                                      bounds=(0, [np.pi / 2, 2 * np.pi, mx + mn, mx]))
        except Exception:
            p = [1, datax[mi_], mx - mn, mn]
        res = datay - f(datax, *p)
        r2 = 1 - np.sum(res ** 2) / np.sum((datay - datay.mean()) ** 2)
        if best is None or r2 > best[0]:
            best = (r2, p)
    p = best[1]
    rmax = f(np.array([p[1]]), *p)[0]
    rmin = f(np.array([p[1] + np.pi]), *p)[0]
    return p[1], (rmax - rmin) / rmax


def resample_mis(cnt, occ, centres, fs, n_res, rng):
    """MIs of n_res resampled histograms: (a) spike phases resampled (multinomial on the unit's
    counts), (b) session phases resampled (multinomial on the occupancy)."""
    n = int(cnt.sum())
    p_sp = cnt / cnt.sum()
    p_ss = occ / occ.sum()
    boot = rng.multinomial(n, p_sp, size=n_res) / occ * fs
    null = rng.multinomial(n, p_ss, size=n_res) / occ * fs
    mi_b, _ = fit_tuning_grid(boot, centres)
    mi_n, _ = fit_tuning_grid(null, centres)
    return mi_b, mi_n


def unit_tuning(cnt, occ, cen, fs, rng, n_res=1000, n_code=100, sig_above=MI_TUNED):
    """Measured MI and preferred phase by the code's curve_fit and by the grid fit; for units
    whose measured (code) MI exceeds sig_above (only these can pass MI > 0.6), the significance readings of the
    claims file V3: (a) one-sided Mann-Whitney of 1000 resampled-spike MIs against 1000
    random-phase MIs; (b) the fraction of the 1000 random-phase MIs at least as large as the
    measured (grid) MI; code, (a) with the first 100 of each."""
    from scipy.stats import mannwhitneyu
    out = {"mi": np.nan, "pref": np.nan, "mi_grid": np.nan, "pref_grid": np.nan,
           "p_a": np.nan, "p_b": np.nan, "p_code": np.nan, "n_spk": int(cnt.sum()) if cnt is not None else 0}
    if cnt is None or cnt.sum() == 0 or (occ == 0).any():
        return out
    y = cnt / occ * fs
    pref, mi = code_phase_tuning(cen, y)
    mg, pg = fit_tuning_grid(y[None, :], cen)
    out.update(mi=float(mi), pref=float(pref), mi_grid=float(mg[0]), pref_grid=float(pg[0]))
    if mi > sig_above:
        mb, mn = resample_mis(cnt, occ, cen, fs, n_res, rng)
        out["p_a"] = float(mannwhitneyu(mb, mn, alternative="greater").pvalue)
        out["p_b"] = float(np.mean(mn >= mg[0]))
        out["p_code"] = float(mannwhitneyu(mb[:n_code], mn[:n_code], alternative="greater").pvalue)
        out["null_mi_median"] = float(np.median(mn))
    return out


# ----------------------------------------------------------------------------- swallow units

def swallow_unit_stats(spikes_by_trial, swallows, fs, rng, n_boot=1000):
    """Code get_swallow_aligned_spikes and get_swallow_tuning for one unit, with the peak of
    the code's PSTH (compute_psth) for Extended Data Fig 6e and reading V4 (b)."""
    rel = []
    for i, ev in enumerate(swallows):
        if len(ev) == 0:
            continue
        sp = (spikes_by_trial[i] * fs).astype(int)
        sp = sp[sp < N_FRAMES]
        for e in ev:
            rel.append((sp - e) / fs)
    out = {"n": len(rel)}
    if len(rel) < 20:
        return out
    r = np.array([[np.sum((t > -0.3) & (t < -0.1)) / 0.2, np.sum((t > -0.05) & (t < 0.05)) / 0.1,
                   np.sum((t > 0.1) & (t < 0.3)) / 0.2] for t in rel])
    idx = rng.integers(0, len(r), size=(n_boot, len(r)))
    rb = r[idx].mean(1)
    m = r.mean(0)
    p = []
    for j in (0, 2):
        dlt = m[1] - m[j]
        if dlt > 0:
            p.append(np.mean((rb[:, 1] - rb[:, j]) < 0))
        elif dlt < 0:
            p.append(np.mean((rb[:, 1] - rb[:, j]) > 0))
        else:
            p.append(1.0)
    mi1 = (m[1] - m[0]) / max(m[1], m[0], 1e-12)
    mi2 = (m[1] - m[2]) / max(m[1], m[2], 1e-12)
    # PSTH: 1 ms bins, 50 ms boxcar (code compute_psth), mean over events
    bins = np.arange(-1, 1 + 0.001, 0.001)
    h = np.zeros(len(bins) - 1)
    for t in rel:
        h += np.histogram(t, bins)[0]
    h = np.convolve(h / len(rel), np.ones(50) / 0.05, mode="same")
    c = bins[:-1]
    w = (c >= -0.15) & (c <= 0.15)
    peak_t = c[w][np.argmax(h[w])]
    w50 = (c >= -0.05) & (c <= 0.05)
    peak50 = h[w50].max()
    mi1b = (m[1] - m[0]) / max(peak50, 1e-12)
    mi2b = (m[1] - m[2]) / max(peak50, 1e-12)
    out.update(rates=m, p=p, mi=(mi1 + mi2) / 2, mi_b=(mi1b + mi2b) / 2, peak_t=peak_t)
    return out


# ----------------------------------------------------------------------------- per session

def process_session(args):
    """Everything the notebook needs from one session, reduced as it loads."""
    key, url, probe_urls, seed = args
    rng = np.random.default_rng(seed)
    sess = read_session(url, probe_urls)
    mt = movement_timing(sess)
    sw = detect_swallows(sess, mt["tongue_onset"])
    ph = phases(sess)
    fs = sess["video_fs"]
    out = {"key": key, "n_trials_total": sess["n_trials_total"], "n_good_trials": len(sess["trials"]),
           "video_fs": fs, "trial_len": sess["trial_len"], "breath_dt": sess["breath_dt"],
           "n_move": sess["n_move"], "n_breath_trials": len(ph["breath_trials"])}
    out["mt"] = {k: v for k, v in mt.items() if k not in ("breath_ds", "phase_b")}
    # expiration onsets (claims file ed1bc): phase + pi crossing 0 (raw phase wrapping)
    pb = mt["phase_b"]
    out["expir_onset"] = np.argwhere((pb > np.pi) & (np.roll(pb, -1) < np.pi - 1))[:, 0] * FRAME_S
    out["swallows"] = sw
    out["swallow_times"] = np.hstack([i * sess["trial_len"] + np.asarray(e) / fs for i, e in enumerate(sw)]) if sw else np.array([])
    pdl = peak_diff_lick_behv(mt)
    pdb = peak_diff_breath_behv(mt)
    out["pd_lick"] = None if pdl is None else {k: v for k, v in pdl.items() if k != "licks"}
    if pdl is not None:
        out["pd_lick"]["licks_fast"] = [pdl["licks"][i] for i in pdl.get("i_fast", [])]
        out["pd_lick"]["licks_slow"] = [pdl["licks"][i] for i in pdl.get("i_slow", [])]
    out["pd_breath"] = None if pdb is None else {k: v for k, v in pdb.items() if k != "breaths"}
    # protrusion phase per lick (ed8e): frame of the largest 3D tongue distance from its onset
    # position, between tongue onset and offset, jaw phase there
    prot = {o: [] for o in FILTER_ORDERS}
    t3 = sess["tongue3d"]
    s_l, b_l = sess["side_tongue_l"], sess["bottom_tongue_l"]
    vis = (s_l > 0.95) & (b_l > 0.95)
    lick_angles = []
    for i in range(vis.shape[0]):
        v = vis[i].astype(int)
        ons = np.where(np.diff(v) == 1)[0] + 1
        offs = np.where(np.diff(v) == -1)[0] + 1
        for o in ons:
            e = offs[offs > o]
            if not len(e):
                continue
            e = e[0]
            seg = t3[i, o:e]
            if np.isnan(seg).all() or len(seg) < 2:
                continue
            dist = np.linalg.norm(seg - seg[0], axis=1)
            fmax = o + int(np.nanargmax(dist))
            for order in FILTER_ORDERS:
                prot[order].append(ph["jaw"][order][i, fmax])
            jr = sess["jaw3d"][i, max(o - 10, 0):o]
            lick_angles.append((i, o * FRAME_S, *t3[i, fmax], *(np.nanmean(jr, 0) if len(jr) else [np.nan] * 3)))
    out["protrusion_phase"] = {o: np.array(v) for o, v in prot.items()}
    out["lick_tips"] = np.array(lick_angles)
    # units
    units = {}
    for probe, pr in sess["probes"].items():
        rows = []
        for ui, sp in zip(pr["good_idx"], pr["spikes"]):
            row = {"unit_index": int(ui), "rate_trials": sum(len(s) for s in sp) / (len(sp) * sess["trial_len"]) if len(sp) else np.nan}
            spf = [s[s < TRIAL_S] for s in sp]
            train = np.hstack([s + TRIAL_S * i for i, s in enumerate(spf)]) if spf else np.array([])
            row["rate_5s"] = len(train) / (len(spf) * TRIAL_S) if len(spf) else np.nan
            for order in FILTER_ORDERS:
                jp = spike_phase_hist(sp, ph["jaw"][order], fs, N_FRAMES - 1)
                cnt, occ, cen, _ = tuning_bins(ph["jaw"][order].reshape(-1), jp)
                row[f"jaw_cnt_{order}"], row[f"jaw_occ_{order}"], row[f"jaw_cen_{order}"] = cnt, occ, cen
                for k, v in unit_tuning(cnt, occ, cen, fs, rng).items():
                    row[f"jaw_{k}_{order}"] = v
                if len(ph["breath_trials"]):
                    bp = spike_phase_hist(sp, ph["breath"][order], BREATH_FS / BREATH_DS,
                                          int(5 * BREATH_FS / BREATH_DS), ph["breath_trials"])
                    cnt, occ, cen, _ = tuning_bins(ph["breath"][order].reshape(-1), bp)
                else:
                    cnt = occ = cen = None
                row[f"br_cnt_{order}"], row[f"br_occ_{order}"], row[f"br_cen_{order}"] = cnt, occ, cen
                for k, v in unit_tuning(cnt, occ, cen, BREATH_FS / BREATH_DS, rng).items():
                    row[f"br_{k}_{order}"] = v
            # clock check: tuning with each trial's spikes paired with the next trial's phases
            sp_shift = sp[1:] + sp[:1]
            jp = spike_phase_hist(sp_shift, ph["jaw"][4], fs, N_FRAMES - 1)
            cnt, occ, cen, _ = tuning_bins(ph["jaw"][4].reshape(-1), jp)
            row["jaw_mi_shift"] = fit_tuning_grid((cnt / occ * fs)[None, :], cen)[0][0] if cnt.sum() else np.nan
            if len(ph["breath_trials"]):
                bp = spike_phase_hist(sp_shift, ph["breath"][4], BREATH_FS / BREATH_DS,
                                      int(5 * BREATH_FS / BREATH_DS), ph["breath_trials"])
                cnt, occ, cen, _ = tuning_bins(ph["breath"][4].reshape(-1), bp)
                row["br_mi_shift"] = fit_tuning_grid((cnt / occ * 250.0)[None, :], cen)[0][0] if cnt.sum() else np.nan
            # spikes from -50 to 100 ms around each lick onset (Extended Data Fig 8g), per lick
            if len(lick_angles):
                ons = np.array([la[0] * TRIAL_S + la[1] for la in lick_angles])
                row["lick_counts"] = (np.searchsorted(train, ons + 0.1) - np.searchsorted(train, ons - 0.05)).astype(np.int16)
            # peak differences (Fig 4e-f)
            if pdl is not None and len(pdl.get("unit_fast", [])) >= 40 and len(pdl.get("unit_slow", [])) >= 40:
                row["pd_lick_unit"] = unit_peak_diffs(train, pdl["t0"], pdl["unit_fast"], pdl["unit_slow"],
                                                      -0.4, 1, ((0.1, 0.3), (0.16, 0.36)), 0.14)
            else:
                row["pd_lick_unit"] = np.nan
            if pdb is not None and len(pdb["i_fast"]) >= 100 and len(pdb["i_slow"]) >= 100:
                row["pd_breath_unit"] = unit_peak_diffs(train, pdb["t0"], pdb["i_fast"], pdb["i_slow"],
                                                        -0.1, 0.6, ((0, 0.24), (0.02, 0.26)), 0.24)
            else:
                row["pd_breath_unit"] = np.nan
            s = swallow_unit_stats(sp, sw, fs, rng)
            row["sw_n"] = s["n"]
            for k in ("mi", "mi_b", "peak_t"):
                row["sw_" + k] = s.get(k, np.nan)
            row["sw_p"] = max(s["p"]) if "p" in s else np.nan
            rows.append(row)
        units[probe] = rows
    out["units"] = units
    return out


def run_sessions(jobs, workers=4):
    """process_session over many sessions in worker processes; results in input order."""
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(process_session, jobs))


def _meta_job(url):
    return read_probe_meta(url)


def survey(assets, workers=8):
    """read_probe_meta over every file: a table of files and a table of all units."""
    with ProcessPoolExecutor(workers) as ex:
        res = list(ex.map(_meta_job, assets.url))
    files, units = [], []
    for (meta, u), row in zip(res, assets.itertuples()):
        files.append({"subject": row.subject, "session": row.session, "probe": row.probe, **meta})
        u = u.copy()
        u["subject"], u["session"], u["probe"] = row.subject, row.session, row.probe
        units.append(u)
    return pd.DataFrame(files), pd.concat(units, ignore_index=True)
