"""Loading and measures for the Neuropixels illusory contour sessions of dandiset 000248.

Shin, Ogando, Abdeladim, ... Lecoq & Adesnik (2025), Nature Neuroscience 28, 2319-2329,
doi:10.1038/s41593-025-02055-5.

Each session is one `*_ogen.nwb` file, which holds the units of all six probes (spike times,
waveform duration, peak channel), the electrode table with the CCF area label of each channel,
the stimulus tables of the four IC blocks, the receptive field block (RFCI) and the size block,
the spontaneous (gray screen) intervals and, in 10 sessions, the eye tracking fits. The
`*_probe-N_ecephys.nwb` files hold LFP and are not read. Files are streamed from the archive at
the pinned version; nothing is written to disk.

Where the parameters come from. "Criterion" means the claim's criterion in
claims/000248/10.1038-s41593-025-02055-5.yaml; "code" means the paper's analysis code,
github.com/hs13/IC_paper_code at commit 50e04eaf7c9192a067c129f3c1f174a27f10c406, which the
claims file cites.

- RS units: waveform_duration > 0.4 ms (Methods, "trough-to-peak width of >=0.4 ms"; code,
  analyzeICtxi_SVM_areas.m `neuRS = unit_wfdur>0.4`). No quality filter (criterion of
  results-npx-units-per-session); the `quality` column is kept so that a variant can drop the
  units labelled noise.
- Area: the location label of the unit's peak channel; V1 is a label starting with 'VISp' but
  not 'VISpm' (code). The layer is the rest of the label ('VISp2/3' is layer 2/3).
- IC trials: every second row of an IC block table from the first row with a non-zero `frame`,
  and the frame value indexes `IC_TRIAL_TYPES` (code, postprocessnwb_v240130.m, with its rule
  for a first or last trial that is blank).
- IC response: spikes in the 1-ms bins 1 to 400 after the bin of image onset, one count per bin
  as the code's boolean spike trains have, in spikes/s (code, postprocessnwb_v240130.m).
- RF trial: every fourth row of the RFCI table (one presentation of four directions), spikes in
  the 1-ms bins 1 to 1000 after onset (code). Position 0 is the center.
- Spontaneous rate: mean rate over the longest spontaneous interval (code).
- Kruskal-Wallis followed by Tukey-Kramer comparisons on mean ranks, as MATLAB's multcompare
  does after kruskalwallis (Methods; code analyzeStaticICtxi.m), and the AUROC of
  perfcurve.
- Eye: pupil position from `pupil_tracking`; the mode is the center of the most populated 3-pixel
  bin of a 2D histogram over the session; per trial, the largest distance from the mode in the
  frames from the first frame after onset to 0.4 s (IC) or 1 s (RF), at the 60 Hz the code
  assumes, and whether any of those frames is a likely blink (code, analyzeMouseEye.m).
"""

from __future__ import annotations

import re
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy import stats
from scipy.stats import studentized_range

DANDISET_ID = "000248"
DANDISET_VERSION = "0.240502.2344"

IC_BLOCKS = ["ICwcfg1", "ICwcfg0", "ICkcfg1", "ICkcfg0"]
# code, postprocessnwb_v240130.m: frame value k is trial type IC_TRIAL_TYPES[k]
IC_TRIAL_TYPES = np.r_[[0, 101, 105, 106], [107, 109, 110, 111], [506, 511], [1105, 1109], [1201, 1299],
                       np.arange(1301, 1309)]
BLANK, IC1, LC1, LC2, IC2 = 0, 106, 107, 110, 111
IRE1, IRE2, TRE1, TRE2, XRE1, XRE2 = 506, 511, 1105, 1109, 1201, 1299
SEG_IN = [1301, 1302, 1303, 1304]   # In BR, BL, TL, TR (ICwcfg1)
SEG_OUT = [1305, 1306, 1307, 1308]
AREAS = ["V1", "LM", "RL", "AL", "PM", "AM"]
AREA_PREFIX = {"V1": "VISp", "LM": "VISl", "RL": "VISrl", "AL": "VISal", "PM": "VISpm", "AM": "VISam"}
# Orientation of the illusory (and real) bar of image 1 and 2 in each white-circle block
# (Fig. 2c legend: IC1 135 and IC2 45 degrees; configuration 0 is rotated 315 degrees clockwise)
BAR_ORIENTATION = {("ICwcfg1", 1): 135, ("ICwcfg1", 2): 45, ("ICwcfg0", 1): 90, ("ICwcfg0", 2): 0}

RS_WIDTH_MS = 0.4
IC_WINDOW_MS = 400
RF_WINDOW_MS = 1000
EYE_HZ = 60.0
EYE_BIN_PX = 3.0


def area_of(label: str) -> str | None:
    """Area name of a CCF location label, or None outside the six visual areas."""
    m = re.match(r"VIS(pm|am|rl|al|p|l)(\d.*)?$", label)
    if not m:
        return None
    return {"p": "V1", "l": "LM", "rl": "RL", "al": "AL", "pm": "PM", "am": "AM"}[m.group(1)]


def layer_of(label: str) -> str:
    m = re.match(r"VIS(pm|am|rl|al|p|l)(.*)$", label)
    return m.group(2) if m and m.group(2) else "?"


def session_assets() -> list[dict]:
    """The session files (one `_ogen.nwb` per session) of the pinned version, with their URLs."""
    with DandiAPIClient() as client:
        ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        out = []
        for a in ds.get_assets():
            if a.path.endswith("_ogen.nwb"):
                out.append({"path": a.path, "asset_id": a.identifier, "size": a.size,
                            "url": a.get_content_url(follow_redirects=1, strip_query=True)})
    return sorted(out, key=lambda r: r["path"])


def all_assets() -> list[dict]:
    with DandiAPIClient() as client:
        ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        return [{"path": a.path, "size": a.size} for a in ds.get_assets()]


def _str(x):
    return x.decode() if isinstance(x, bytes) else str(x)


def ic_trials(frame: np.ndarray) -> np.ndarray:
    """Row indices of image presentations in an IC block (code, postprocessnwb_v240130.m)."""
    nz = np.flatnonzero(frame != 0)
    first, last = nz[0] + 1, nz[-1] + 1          # 1-based, as in the code
    if first % 10 != 1:
        first = 10 * (first // 10) + 1
    if last % 10 != 9:
        last = 10 * (last // 10) + 9
    return np.arange(first, last + 1, 2) - 1


def _window_counts(bins_list, onset_ms, lo, hi):
    """Spike counts per (trial, unit): 1-ms bins b with onset+lo <= b <= onset+hi."""
    out = np.zeros((len(onset_ms), len(bins_list)), dtype=np.float32)
    for j, b in enumerate(bins_list):
        out[:, j] = np.searchsorted(b, onset_ms + hi, side="right") - np.searchsorted(b, onset_ms + lo, side="left")
    return out


def load_session(asset: dict, ccg: bool = True) -> dict:
    """Read one session and reduce it to what the analyses use.

    Units of the six visual areas only. Returns per-trial responses (spikes/s) of every such unit
    in the four IC blocks and in the RF block, spontaneous rates, eye measures per trial, and, when
    `ccg`, the 1-ms spike bins of RS units during the ICwcfg1 block for the cross-correlograms.
    """
    f = h5py.File(remfile.File(asset["url"]), "r")
    s = {"path": asset["path"], "subject": _str(f["general/subject/subject_id"][()]),
         "session_id": _str(f["general/session_id"][()]),
         "genotype": _str(f["general/subject/genotype"][()]), "age": _str(f["general/subject/age"][()])}
    el = f["general/extracellular_ephys/electrodes"]
    loc_by_id = dict(zip(el["id"][:], (_str(x) for x in el["location"][:])))
    u = f["units"]
    peak = u["peak_channel_id"][:]
    labels = np.array([loc_by_id[p] for p in peak])
    s["n_units_file"] = len(peak)
    s["unit_labels_all"] = pd.Series(labels).value_counts()
    keep = np.flatnonzero([area_of(x) is not None for x in labels])
    units = pd.DataFrame({
        "unit_index": keep, "unit_id": u["id"][:][keep], "label": labels[keep],
        "area": [area_of(x) for x in labels[keep]], "layer": [layer_of(x) for x in labels[keep]],
        "waveform_duration": u["waveform_duration"][:][keep],
        "quality": [_str(x) for x in u["quality"][:][keep]],
        "firing_rate": u["firing_rate"][:][keep], "probe": peak[keep] // 1000})
    units["rs"] = units.waveform_duration > RS_WIDTH_MS
    s["waveform_duration_all"] = u["waveform_duration"][:]
    s["quality_all"] = np.array([_str(x) for x in u["quality"][:]])
    s["area_all"] = np.array([area_of(x) for x in labels], dtype=object)
    idx = u["spike_times_index"][:]
    starts = np.r_[0, idx[:-1]]
    st = u["spike_times"]
    # read contiguous runs of kept units at once
    bins = [None] * len(keep)
    run_start = 0
    while run_start < len(keep):
        run_end = run_start
        while run_end + 1 < len(keep) and keep[run_end + 1] == keep[run_end] + 1:
            run_end += 1
        a, b = starts[keep[run_start]], idx[keep[run_end]]
        chunk = st[a:b]
        for k in range(run_start, run_end + 1):
            t = chunk[starts[keep[k]] - a: idx[keep[k]] - a]
            bins[k] = np.unique(np.floor(t * 1000.0).astype(np.int64))
        run_start = run_end + 1
    s["sorted_ok"] = all(np.all(np.diff(st[starts[k]:idx[k]][:2000]) >= 0) for k in keep[:50])
    units["n_spikes_bins"] = [len(b) for b in bins]
    s["units"] = units

    iv = f["intervals"]
    s["blocks"] = {}
    for blk in IC_BLOCKS:
        g = iv[f"{blk}_presentations"]
        frame = g["frame"][:]
        rows = ic_trials(frame)
        start = g["start_time"][:]
        stop = g["stop_time"][:]
        other = np.setdiff1d(np.arange(rows[0], rows[-1] + 1), rows)
        onset_ms = np.floor(start[rows] * 1000.0).astype(np.int64)
        s["blocks"][blk] = {
            "codes": IC_TRIAL_TYPES[frame[rows].astype(int)], "start": start[rows], "stop": stop[rows],
            "n_rows": len(frame), "iti_rows_nonzero_frame": int(np.count_nonzero(frame[other])),
            "duration": stop[rows] - start[rows], "iti": start[rows][1:] - stop[rows][:-1],
            "R": _window_counts(bins, onset_ms, 1, IC_WINDOW_MS) * (1000.0 / IC_WINDOW_MS)}
        if blk == "ICwcfg1":   # the 400 ms before onset, for the check of the clock
            s["blocks"][blk]["R_pre"] = _window_counts(bins, onset_ms, 1 - IC_WINDOW_MS, 0) * (1000.0 / IC_WINDOW_MS)
    g = iv["RFCI_presentations"]
    start = g["start_time"][:]
    x, y = g["x_position"][:], g["y_position"][:]
    mask = np.array([_str(m) for m in g["Mask"][:]])
    rows = np.arange(0, len(start), 4)
    maskno = np.array([int(re.search(r"(\d+)\.tif", m).group(1)) for m in mask[rows]])
    # positions: 0 center, then code order (down, then counterclockwise), code RFcentersrel
    rel = np.array([[-1, 0], [-1 / np.sqrt(2), 1 / np.sqrt(2)], [0, 1], [1 / np.sqrt(2), 1 / np.sqrt(2)],
                    [1, 0], [1 / np.sqrt(2), -1 / np.sqrt(2)], [0, -1], [-1 / np.sqrt(2), -1 / np.sqrt(2)]])
    yx = np.c_[y[rows], x[rows]] / 203.3786
    pos = np.zeros(len(rows), dtype=int)
    for k, r in enumerate(rel):
        pos[np.all(np.abs(yx - r) < 1e-3, axis=1)] = k + 1
    s["rf"] = {"pos": pos, "inverse": maskno // 10000 == 1, "start": start[rows],
               "directions_per_trial": [tuple(g["orientation"][r:r + 4]) for r in rows[:3]],
               "row_dur": g["stop_time"][:] - start, "n_rows": len(start),
               "R": _window_counts(bins, np.floor(start[rows] * 1000).astype(np.int64), 1, RF_WINDOW_MS)
               * (1000.0 / RF_WINDOW_MS)}
    sp = iv["spontaneous_presentations"]
    s0, s1 = sp["start_time"][:], sp["stop_time"][:]
    k = int(np.argmax(s1 - s0))
    lo, hi = int(np.floor(s0[k] * 1000)) + 1, int(np.floor(s1[k] * 1000))
    s["spont_interval"] = (s0[k], s1[k])
    s["spont_all"] = np.c_[s0, s1]
    s["spont_rate"] = np.array([(np.searchsorted(b, hi, "right") - np.searchsorted(b, lo, "left"))
                                / ((hi - lo + 1) / 1000.0) for b in bins])
    nwin = int((s1[k] - s0[k]) // 1.0)
    w0 = np.floor(s0[k] * 1000).astype(np.int64) + 1000 * np.arange(nwin)
    s["spont_windows"] = _window_counts(bins, w0, 1, 1000)   # spikes/s in 1-s windows
    s["block_spans"] = {blk: (iv[f"{blk}_presentations"]["start_time"][0], iv[f"{blk}_presentations"]["stop_time"][-1])
                        for blk in IC_BLOCKS + ["RFCI", "sizeCI"]}

    if ccg:
        b0, b1 = s["block_spans"]["ICwcfg1"]
        lo, hi = int(np.floor(b0 * 1000)), int(np.floor(b1 * 1000))
        s["ccg_span_ms"] = (lo, hi)
        s["ccg_bins"] = {int(i): b[(b >= lo) & (b <= hi)].astype(np.int32)
                         for i, b, rs in zip(units.index, bins, units.rs) if rs}
    s["eye"] = _eye(f, s) if "acquisition/EyeTracking" in f else None
    return s


def _eye(f, s) -> dict:
    e = f["acquisition/EyeTracking"]
    ts = e["eye_tracking/timestamps"][:]
    n_nan_ts = int(np.isnan(ts).sum())
    ts = np.where(np.isnan(ts), np.inf, ts)       # a NaN timestamp is sorted last
    p = e["pupil_tracking/data"][:]
    area = e["pupil_tracking/area"][:]
    blink = e["likely_blink/data"][:].astype(bool)
    ok = np.isfinite(p).all(axis=1)
    xe = np.arange(np.nanmin(p[:, 0]), np.nanmax(p[:, 0]) + EYE_BIN_PX, EYE_BIN_PX)
    ye = np.arange(np.nanmin(p[:, 1]), np.nanmax(p[:, 1]) + EYE_BIN_PX, EYE_BIN_PX)
    H, _, _ = np.histogram2d(p[ok, 0], p[ok, 1], bins=[xe, ye])
    r, c = np.unravel_index(np.argmax(H), H.shape)
    mode = np.array([(xe[r] + xe[r + 1]) / 2, (ye[c] + ye[c + 1]) / 2])
    dist = np.sqrt(((p - mode) ** 2).sum(axis=1))
    za = (area - np.nanmean(area)) / np.nanstd(area)
    out = {"mode": mode, "hz": 1 / np.nanmedian(np.diff(ts[np.isfinite(ts)])), "n_frames": len(ts),
           "n_nan_timestamps": n_nan_ts, "nan_timestamp_last": bool(n_nan_ts == 0 or not np.isfinite(ts[-1])),
           "units": {k: _str(e[f"pupil_tracking/{k}"].attrs.get("unit", "")) for k in ["data", "area"]},
           "frac_nan": float(np.mean(~ok)), "frac_blink": float(blink.mean()),
           "x_range": np.nanpercentile(p[:, 0], [1, 99]), "y_range": np.nanpercentile(p[:, 1], [1, 99]),
           "width_median": float(np.nanmedian(e["pupil_tracking/width"][:])),
           "eye_width_median": float(np.nanmedian(e["eye_tracking/width"][:])),
           "density_xy": (p[ok][::10] - mode).astype(np.float32)}
    for name, starts, dur in [("ICwcfg1", s["blocks"]["ICwcfg1"]["start"], 0.4),
                              ("ICwcfg0", s["blocks"]["ICwcfg0"]["start"], 0.4), ("RF", s["rf"]["start"], 1.0)]:
        first = np.searchsorted(ts, starts, side="right")     # first frame after onset (code)
        n = int(round(dur * EYE_HZ))
        ind = np.clip(first[:, None] + np.arange(n)[None, :], 0, len(ts) - 1)
        d = dist[ind]
        out[name] = {"maxdist": np.nanmax(np.where(np.isnan(d), -np.inf, d), axis=1),
                     "blink": blink[ind].any(axis=1), "nan_frames": np.isnan(d).sum(axis=1),
                     "area_mean": np.nanmean(za[ind], axis=1), "area_end": za[ind[:, -1]],
                     "area_max": np.nanmax(np.where(np.isnan(za[ind]), -np.inf, za[ind]), axis=1),
                     "x_mean": np.nanmean(p[ind, 0], axis=1), "y_mean": np.nanmean(p[ind, 1], axis=1),
                     "lag_first_frame": ts[np.clip(first, 0, len(ts) - 1)] - starts}
    return out


def load_all(ccg: bool = True, workers: int = 4) -> list[dict]:
    assets = session_assets()
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(lambda a: load_session(a, ccg=ccg), assets))


# ---------------------------------------------------------------- statistics

_QCRIT = {}


def tukey_qcrit(k: int, alpha: float = 0.05) -> float:
    """Critical studentized range for k groups, infinite df (Tukey-Kramer after Kruskal-Wallis)."""
    if k not in _QCRIT:
        _QCRIT[k] = float(studentized_range.ppf(1 - alpha, k, 1e6))
    return _QCRIT[k]


def kw_tukey(R: np.ndarray, groups: np.ndarray, order: list):
    """Kruskal-Wallis per unit and Tukey-Kramer comparison of each group with the first.

    R is trials x units; groups the trial labels; order the groups compared, the first being the
    reference (blank). Returns (p_kw per unit, sig per unit x other group) where sig means the
    Tukey-Kramer comparison of mean ranks with the reference is significant at 0.05, as MATLAB's
    multcompare after kruskalwallis (mean ranks, variance N(N+1)/12 with the tie correction,
    infinite df).
    """
    sel = np.isin(groups, order)
    X = R[sel]
    g = groups[sel]
    N = X.shape[0]
    ranks = stats.rankdata(X, axis=0)
    k = len(order)
    n = np.array([np.sum(g == o) for o in order])
    meanr = np.stack([ranks[g == o].mean(axis=0) for o in order])         # k x units
    # Kruskal-Wallis H with tie correction
    H = 12.0 / (N * (N + 1)) * np.sum(n[:, None] * (meanr - (N + 1) / 2) ** 2, axis=0)
    ties = np.zeros(X.shape[1])
    for j in range(X.shape[1]):
        _, c = np.unique(X[:, j], return_counts=True)
        ties[j] = np.sum(c ** 3 - c)
    corr = 1 - ties / (N ** 3 - N)
    with np.errstate(invalid="ignore", divide="ignore"):
        Hc = np.where(corr > 0, H / corr, 0.0)
    p_kw = stats.chi2.sf(Hc, k - 1)
    p_kw[corr <= 0] = 1.0
    var = N * (N + 1) / 12.0 * corr                                             # per unit
    qc = tukey_qcrit(k)
    sig = np.zeros((X.shape[1], k - 1), dtype=bool)
    for i in range(1, k):
        se = np.sqrt(var * (1.0 / n[0] + 1.0 / n[i]) / 2.0)
        with np.errstate(invalid="ignore", divide="ignore"):
            q = np.abs(meanr[i] - meanr[0]) / se
        sig[:, i - 1] = np.nan_to_num(q) > qc
    return p_kw, sig


def auroc(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """AUROC of b against a (b positive) per unit; a, b are trials x units."""
    allx = np.vstack([a, b])
    r = stats.rankdata(allx, axis=0)
    rb = r[len(a):].sum(axis=0)
    nb, na = len(b), len(a)
    return (rb - nb * (nb + 1) / 2) / (na * nb)


def ranksum_p(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Two-sided Wilcoxon rank-sum p per unit (normal approximation with tie correction)."""
    return stats.mannwhitneyu(a, b, axis=0, alternative="two-sided", method="asymptotic").pvalue


def ic_groups(R: np.ndarray, codes: np.ndarray, seg_in=SEG_IN, seg_out=SEG_OUT) -> pd.DataFrame:
    """IC-encoders, LC-encoders and segment responders (code analyzeStaticICtxi.m; Methods).

    sigmcBK: +1/-1/0 per IC1, LC1, LC2, IC2 against blank: Tukey-Kramer significant, sign from
    the AUROC against blank. IC-encoder: Kruskal-Wallis p < 0.05, IC1 or IC2 +1, LC1 and LC2 0.
    Segment responder (indin): Kruskal-Wallis across blank and the 8 segment images p < 0.05,
    rank-sum In vs Out p < 0.05 with AUROC > 0.5, and not an IC- or LC-encoder.
    """
    order = [BLANK, IC1, LC1, LC2, IC2]
    pkw, sig = kw_tukey(R, codes, order)
    blank = R[codes == BLANK]
    au = np.stack([auroc(blank, R[codes == c]) for c in order[1:]], axis=1)
    smc = np.where(sig, np.sign(au - 0.5), 0).astype(int)
    smc[pkw >= 0.05] = 0
    kw = pkw < 0.05
    ic1 = kw & (smc[:, 0] == 1) & (smc[:, 1] == 0) & (smc[:, 2] == 0)
    ic2 = kw & (smc[:, 3] == 1) & (smc[:, 1] == 0) & (smc[:, 2] == 0)
    lc1 = kw & (smc[:, 1] == 1) & (smc[:, 0] == 0) & (smc[:, 3] == 0)
    lc2 = kw & (smc[:, 2] == 1) & (smc[:, 0] == 0) & (smc[:, 3] == 0)
    out = pd.DataFrame({"p_kw_BK": pkw, "ic1_enc": ic1, "ic2_enc": ic2, "ic_enc": ic1 | ic2,
                        "lc1_enc": lc1, "lc2_enc": lc2, "lc_enc": lc1 | lc2})
    pkw_bi, _ = kw_tukey(R, codes, [BLANK] + list(seg_in) + list(seg_out))
    seg_any = np.zeros(len(pkw), dtype=bool)
    for i, (ci, co) in enumerate(zip(seg_in, seg_out)):
        a, b = R[codes == co], R[codes == ci]
        sp = auroc(a, b)
        p = ranksum_p(a, b)
        sr = (sp > 0.5) & (pkw_bi < 0.05) & (p < 0.05) & ~out.ic_enc.values & ~out.lc_enc.values
        out[f"seg{i + 1}"] = sr
        seg_any |= sr
    out["seg_resp"] = seg_any
    return out


def ic_ire_responsive(R: np.ndarray, codes: np.ndarray, ic_code: int, ire_code: int, test: str):
    """Is a unit responsive to the IC image and to the IRE image (against blank)?

    test 'a': code's sigmcBICREl, Kruskal-Wallis across blank, IC and IRE p < 0.05 and
    Tukey-Kramer against blank significant with AUROC > 0.5. test 'b': rank-sum against blank
    p < 0.05 with AUROC > 0.5 (criterion of fig1f).
    """
    blank = R[codes == BLANK]
    res = []
    if test == "a":
        pkw, sig = kw_tukey(R, codes, [BLANK, ic_code, ire_code])
        for i, c in enumerate([ic_code, ire_code]):
            res.append((pkw < 0.05) & sig[:, i] & (auroc(blank, R[codes == c]) > 0.5))
    else:
        for c in [ic_code, ire_code]:
            x = R[codes == c]
            res.append((ranksum_p(blank, x) < 0.05) & (auroc(blank, x) > 0.5))
    return res[0], res[1]


def signrank_p(x: np.ndarray, y=None, alternative="two-sided") -> float:
    x = np.asarray(x, float) if y is None else np.asarray(x, float) - np.asarray(y, float)
    x = x[np.isfinite(x)]
    if np.all(x == 0) or len(x) == 0:
        return 1.0
    return float(stats.wilcoxon(x, alternative=alternative).pvalue)


def holm_exclusive(p: np.ndarray, best: np.ndarray, alpha: float = 0.05):
    """Code's RFsigexclclassic: the best position's p is the smallest, p*9 < alpha, and exactly
    one position passes the step-down Holm comparison sorted(p) * [9..1] < alpha."""
    m = p.shape[1]
    ps = np.sort(p, axis=1)
    pb = p[np.arange(len(p)), best]
    return (pb * m < alpha) & (pb == ps[:, 0]) & (np.sum(ps * np.arange(m, 0, -1) < alpha, axis=1) == 1)


def holm_reject(p: np.ndarray, alpha: float = 0.05) -> np.ndarray:
    """Bonferroni-Holm rejections per row of p."""
    m = p.shape[1]
    order = np.argsort(p, axis=1)
    ps = np.take_along_axis(p, order, axis=1)
    passed = ps * np.arange(m, 0, -1) < alpha
    passed = np.cumprod(passed, axis=1).astype(bool)
    rej = np.zeros_like(passed)
    np.put_along_axis(rej, order, passed, axis=1)
    return rej


def rf_positions(R: np.ndarray, pos: np.ndarray, inverse: np.ndarray, spont_rate: np.ndarray,
                 spont_windows: np.ndarray, trials=None):
    """Exclusive center responsiveness under the two readings of fig1e.

    R: RF trials x units (spikes/s); classic (not inverse) trials only are used. trials: optional
    boolean mask of RF trials to use (fixed-gaze). Returns a DataFrame with the best position,
    reading (a) (code: signed-rank of trial rates against the spontaneous rate, center best and
    the only position surviving the code's Holm step) and reading (b) (Methods: rank-sum against
    1-s windows of the longest spontaneous block, Holm over 9 positions, center the only
    significant position), and the Kruskal-Wallis p across positions.
    """
    use = ~inverse if trials is None else (~inverse & trials)
    Rc, pc = R[use], pos[use]
    means = np.stack([Rc[pc == k].mean(axis=0) if np.any(pc == k) else np.full(R.shape[1], np.nan)
                      for k in range(9)], axis=1)
    best = np.nanargmax(np.where(np.isnan(means), -np.inf, means), axis=1)
    pa = np.ones((R.shape[1], 9))
    pb = np.ones((R.shape[1], 9))
    for k in range(9):
        x = Rc[pc == k]
        if len(x) == 0:
            continue
        for j in range(R.shape[1]):
            d = x[:, j] - spont_rate[j]
            pa[j, k] = 1.0 if np.all(d == 0) else stats.wilcoxon(d).pvalue
        pb[:, k] = ranksum_p(spont_windows, x)
    excl_a = holm_exclusive(pa, best) & (best == 0)
    rej_b = holm_reject(pb)
    above = means > spont_windows.mean(axis=0)[:, None]
    excl_b = rej_b[:, 0] & (rej_b.sum(axis=1) == 1) & above[:, 0]
    pkw = np.ones(R.shape[1])
    for j in range(R.shape[1]):
        if np.ptp(Rc[:, j]) > 0:
            pkw[j] = stats.kruskal(*[Rc[pc == k, j] for k in range(9) if np.any(pc == k)]).pvalue
    return pd.DataFrame({"best": best, "excl_a": excl_a, "excl_b": excl_b, "p_kw_rf": pkw,
                         "p_center_a": pa[:, 0], "p_center_b": pb[:, 0]})


# ---------------------------------------------------------------- decoding

def decode(R: np.ndarray, codes: np.ndarray, train_types, probe_types, seed: int, reading: str = "a",
           kernel: str = "linear", n_splits: int = 10):
    """Linear SVM decoder of the Methods and the code (analyzeICtxi_SVM_areas.m).

    Trials of each training type are balanced to the smallest type by taking its first trials;
    stratified tenfold partition; each fold z-scores every unit by the training trials' mean and
    s.d. (NaN set to 0); one-vs-one SVM (libsvm, as MATLAB fitcecoc's default coding). reading
    'a': C = 1; reading 'b': C chosen by a threefold inner cross-validation on the training fold
    over 10^-3 to 1 (larger C did not finish in the time of this run; the Python counterpart of the code's OptimizeHyperparameters, criterion).
    Returns cross-validation accuracy (mean over classes of the fraction correct, mean over
    folds), the confusion matrix of test trials, and P(probe type -> train type) averaged over the
    ten fold models.
    """
    from sklearn.model_selection import GridSearchCV, StratifiedKFold
    from sklearn.svm import SVC

    train_types = list(train_types)
    n_min = min(np.sum(codes == t) for t in train_types)
    idx = np.concatenate([np.flatnonzero(codes == t)[:n_min] for t in train_types])
    y = codes[idx]
    probe = np.flatnonzero(np.isin(codes, probe_types))
    skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=seed)
    conf = np.zeros((len(train_types), len(train_types)))
    pconf = np.zeros((len(probe_types), len(train_types)))
    accs = []
    for tr, te in skf.split(idx, y):
        mu = R[idx[tr]].mean(axis=0)
        sd = R[idx[tr]].std(axis=0, ddof=1)
        with np.errstate(invalid="ignore", divide="ignore"):
            Z = (R - mu) / sd
        Z[~np.isfinite(Z)] = 0
        if kernel == "poly":
            base = SVC(kernel="poly", degree=2, C=1.0)
        else:
            base = SVC(kernel=kernel, C=1.0)
        if reading == "b":
            base.set_params(max_iter=200000)
            clf = GridSearchCV(base, {"C": 10.0 ** np.arange(-3, 1)},
                               cv=StratifiedKFold(3, shuffle=True, random_state=seed))
        else:
            clf = base
        clf.fit(Z[idx[tr]], y[tr])
        pred = clf.predict(Z[idx[te]])
        cm = np.array([[np.mean(pred[y[te] == a] == b) for b in train_types] for a in train_types])
        conf += cm / n_splits
        accs.append(np.mean(np.diag(cm)))
        pp = clf.predict(Z[probe])
        pconf += np.array([[np.mean(pp[codes[probe] == a] == b) for b in train_types] for a in probe_types]) / n_splits
    return {"acc": float(np.mean(accs)), "conf": conf, "probe": pconf, "n_per_class": int(n_min)}


def inference_score(probe: np.ndarray) -> tuple[float, float, float]:
    """TRE inference: rows TRE1, TRE2; columns IC1, LC1, LC2, IC2 (code line 171).
    Returns (score, IC value, LC value)."""
    ic = (probe[0, 0] + probe[1, 3]) / 2
    lc = (probe[0, 1] + probe[1, 2]) / 2
    return ic - lc, ic, lc


# ---------------------------------------------------------------- cross-correlograms

def ccg_counts(target_bins, source_bins, max_lag: int):
    """Raw cross-correlogram counts for every (target, source) pair.

    counts[i, j, max_lag + d] = number of spike pairs with t_target - t_source = d ms, for
    |d| <= max_lag, from 1-ms bin indices (one spike per bin). With d > 0 the source leads.
    """
    from numba import njit

    @njit(cache=False)
    def _run(tb, tptr, sb, slab, nsrc, L):
        out = np.zeros((len(tptr) - 1, nsrc, 2 * L + 1), dtype=np.int32)
        for i in range(len(tptr) - 1):
            lo = 0
            for k in range(tptr[i], tptr[i + 1]):
                t = tb[k]
                while lo < len(sb) and sb[lo] < t - L:
                    lo += 1
                m = lo
                while m < len(sb) and sb[m] <= t + L:
                    out[i, slab[m], L + t - sb[m]] += 1
                    m += 1
        return out

    tptr = np.r_[0, np.cumsum([len(b) for b in target_bins])].astype(np.int64)
    tb = np.concatenate(target_bins).astype(np.int64) if len(target_bins) else np.zeros(0, np.int64)
    sall = np.concatenate(source_bins).astype(np.int64)
    slab = np.concatenate([np.full(len(b), j, np.int64) for j, b in enumerate(source_bins)])
    o = np.argsort(sall, kind="stable")
    return _run(tb, tptr, sall[o], slab[o], len(source_bins), max_lag)


def connections(counts: np.ndarray, max_lag: int, smoothing: str, flank_from: str,
                win=(1, 10), flank=(50, 100), sd_factor=7.0) -> np.ndarray:
    """Putative excitatory connection from source to target (Methods, Cross-correlogram analysis).

    The CCG of trains smoothed with a 25-ms window equals the raw CCG convolved with the
    autocorrelation of the kernel, so the correction is computed from the raw counts.
    smoothing 'box': 25-bin boxcar; 'gauss': Gaussian 25 bins long with s.d. 5 ms (criterion).
    flank_from 'raw' or 'corrected': which CCG the flank s.d. is taken from (criterion readings
    i and ii). Normalisation by sqrt(n1 n2) is left out; it does not change the comparison of the
    peak with a multiple of the flank s.d. of the same pair.
    """
    if smoothing == "box":
        k = np.ones(25) / 25.0
    else:
        x = np.arange(25) - 12
        k = np.exp(-x ** 2 / (2 * 5.0 ** 2))
        k /= k.sum()
    ac = np.convolve(k, k[::-1])                       # 49 taps
    c = counts.astype(np.float32)
    from scipy.ndimage import convolve1d
    sm = convolve1d(c, ac.astype(np.float32), axis=-1, mode="constant")
    corr = c - sm
    lags = np.arange(-max_lag, max_lag + 1)
    w = (lags >= win[0]) & (lags <= win[1])
    fl = (np.abs(lags) >= flank[0]) & (np.abs(lags) <= flank[1])
    peak = corr[..., w].max(axis=-1)
    ref = c if flank_from == "raw" else corr
    sd = ref[..., fl].std(axis=-1, ddof=1)
    return (peak > sd_factor * sd) & (sd > 0)
