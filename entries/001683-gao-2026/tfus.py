"""Loading and measures for dandiset 001683 (Gao, Frake, Durand and He 2026, IEEE TNSRE,
doi:10.1109/tnsre.2025.3644273): EEG and seizure labels of 16 rats with 4-AP seizures, and the
evoked-potential (LFP) and EEG recordings of the wild-type phase of 23 rats.

The files are streamed from the archive at the pinned version; nothing is written to disk. Every
ElectricalSeries in this dandiset is stored contiguous (not chunked) as float64, time by channel,
so reading any channel means reading whole rows. `read_rows` therefore fetches the byte range of
a block of rows with parallel HTTP range requests, which is several times faster than h5py over
remfile; `check_read` compares it with h5py on a slice.

Where the parameters come from:

- RATE, the sampling rate, is the files' own (3051.7578125 Hz; Methods C, "3051.8 Hz").
- Seizure labels are the files' `intervals` table, one row per seizure and hemisphere, tagged
  ipsilateral or contralateral (claims file, M1: the paper's labels are used when the dandiset
  holds them). Their times are in minutes, not the seconds NWB prescribes: the stops reach
  about 62.5 in blocks of 3752 s, and the notebook checks this against the EEG. `MINUTES` converts.
- Seizure metrics follow M2 of the claims file (Methods C): duration leaves out seizures that
  start at the first sample or end at the last; percent time is summed durations over the block
  length; the inter-seizure interval is the mean gap between neighbouring seizures. Whether a gap
  runs from one offset to the next onset or from onset to onset is not said ("time between
  neighboring seizures", Methods C); both are computed (`isi_gap`, `isi_onset`), and the gap
  reading is the one the words favour.
- Blocks are ordered by session start time within a rat: baseline, condition, post 1, post 2,
  post 3 (Methods D and Fig. 1E, ~62.5 min blocks).
- EEG channels: IPSI_CH (channel 8) and CONTRA_CH (channel 25), the electrodes encircled in the
  drawing of Fig. 1A, which is repeated in Fig. S1 with the channel numbers printed ("The EEG
  electrode encircled by the blue/orange ring represents the selected channel data used to label
  seizures"); Methods E uses the same "EEG electrode closest to the burr hole" for the PSD. The
  electrode table's coordinates put channels 8 and 25 at ML +/-2.8, AP -3 mm, next to the burr
  holes at ML +/-2.5, AP -2 mm (Methods A).
- S1 channels (Fig. 5A, which the text read does not list) are the ones the dandiset's own PLV
  files name in their notes: ipsilateral 7, 8, 10, 12 and contralateral 21, 23, 25, 26; the
  others of channels 1 to 16 (ipsilateral, right) and 17 to 32 (contralateral, left) are non-S1.
- Preprocessing (Methods C): 60 Hz notch, common average reference over the 32 EEG channels.
  ICA is not applied: which components the authors removed is not recorded (an assumption, as in
  M1 of the claims file). The 3 to 300 Hz bandpass is applied in the PLI path; for the band power
  the band limits are applied to the spectrum, with the total under the two M5 readings.
- PSD: Welch, 2 s Hann windows, half overlap (a standard choice, M5 of the claims file). Bands
  theta 5-8, alpha 8-12, beta 12-30, gamma 30-80 Hz (Methods E).
- PLI (Methods E, Eq. 2): zero-phase 4th order Butterworth band filter (a standard choice, M6),
  Hilbert phase, |mean sign(sin(dphi))|. For the seizure PLI the EEG is first decimated by 3 to
  1017 Hz with an anti-alias filter, a standard choice that keeps every band (top 80 Hz) and
  leaves the sign of the phase difference unchanged.
- Statistics (Methods F, M3 of the claims file): two-way ANOVA with Bonferroni post hoc tests;
  `twoway` runs the ordinary reading (OLS, post hoc t-tests on the pooled residual error, as
  Prism does) and the repeated-measures reading (a linear mixed model with a random intercept per
  rat, Prism's mixed-effects analysis, with Wald tests of contrasts).
"""

from __future__ import annotations

import json
import warnings
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
import requests
from scipy import signal

DANDISET_ID = "001683"
DANDISET_VERSION = "0.260109.2104"
API = "https://api.dandiarchive.org/api"

RATE = 3051.7578125
N_EEG = 32
IPSI_CH, CONTRA_CH = 8, 25                 # 1-based channel numbers (Fig. S1 drawing)
S1_IPSI, S1_CONTRA = (7, 8, 10, 12), (21, 23, 25, 26)
NONS1_IPSI = tuple(c for c in range(1, 17) if c not in S1_IPSI)
NONS1_CONTRA = tuple(c for c in range(17, 33) if c not in S1_CONTRA)
BANDS = {"theta": (5.0, 8.0), "alpha": (8.0, 12.0), "beta": (12.0, 30.0), "gamma": (30.0, 80.0)}
BLOCKS = ["baseline", "condition", "post1", "post2", "post3"]
MINUTES = 60.0                             # the label table's unit, in seconds
WELCH_S = 2.0
DECIMATE = 3

_session = requests.Session()


# ---------------------------------------------------------------- archive

def list_assets() -> pd.DataFrame:
    """Every asset of the pinned version: path, asset id, size."""
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/?page_size=1000"
    rows = []
    while url:
        page = _session.get(url).json()
        rows += [{"path": a["path"], "asset_id": a["asset_id"], "size": a["size"]} for a in page["results"]]
        url = page.get("next")
    return pd.DataFrame(rows)


def version_info() -> dict:
    return _session.get(f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/info/").json()


def s3_url(asset_id: str) -> str:
    return _session.head(f"{API}/assets/{asset_id}/download/", allow_redirects=True).url


def _text(x):
    if isinstance(x, np.ndarray):
        x = x[0] if x.shape else x[()]
    return x.decode() if isinstance(x, bytes) else str(x)


def read_meta(asset_id: str) -> dict:
    """Metadata, labels and the data layout of one file (no signal is read)."""
    url = s3_url(asset_id)
    f = h5py.File(remfile.File(url), "r")
    es = f["acquisition/ElectricalSeries"]
    d = es["data"]
    iv = f["intervals/custom_intervals_table_name"]
    tags = [_text(t) for t in iv["tags"][:]]
    if "tags_index" in iv:
        idx = iv["tags_index"][:]
        tags = [",".join(tags[(idx[i - 1] if i else 0):idx[i]]) for i in range(len(idx))]
    e = f["general/extracellular_ephys/electrodes"]
    meta = {
        "asset_id": asset_id, "url": url,
        "subject": _text(f["general/subject/subject_id"][()]),
        "group": _text(f["identifier"][()]),
        "kind": _text(f["session_description"][()]),
        "label": _text(f["general/data_collection"][()]),
        "notes": _text(f["general/notes"][()]),
        "start": _text(f["session_start_time"][()]),
        "n_samples": d.shape[0], "n_channels": d.shape[1], "dtype": str(d.dtype),
        "chunks": d.chunks, "compression": d.compression, "offset": d.id.get_offset(),
        "rate": float(es["starting_time"].attrs["rate"]), "t0": float(es["starting_time"][()]),
        "unit": _text(d.attrs.get("unit")), "conversion": float(d.attrs.get("conversion", 1.0)),
        "filtering": _text(es.attrs.get("filtering", "")),
        "intervals": pd.DataFrame({"start": iv["start_time"][:], "stop": iv["stop_time"][:], "tag": tags}),
        "electrodes": pd.DataFrame({k: e[k][:] for k in ("x", "y", "z")} |
                                   {"location": [_text(v) for v in e["location"][:]]}),
    }
    f.close()
    return meta


def read_all_meta(asset_ids, threads: int = 16) -> list[dict]:
    with ThreadPoolExecutor(threads) as ex:
        return list(ex.map(read_meta, asset_ids))


def read_rows(meta: dict, start: int, stop: int, threads: int = 16, piece: int = 32 * 2**20) -> np.ndarray:
    """Rows start:stop of the ElectricalSeries (contiguous float64) by parallel range requests."""
    start, stop = max(0, start), min(meta["n_samples"], stop)
    row = meta["n_channels"] * 8
    a, b = meta["offset"] + start * row, meta["offset"] + stop * row
    edges = list(range(a, b, piece)) + [b]

    def get(i):
        for _ in range(5):
            r = _session.get(meta["url"], headers={"Range": f"bytes={edges[i]}-{edges[i + 1] - 1}"}, timeout=120)
            if r.status_code == 206 and len(r.content) == edges[i + 1] - edges[i]:
                return r.content
        raise OSError(f"range read failed for {meta['asset_id']}")

    with ThreadPoolExecutor(threads) as ex:
        buf = b"".join(ex.map(get, range(len(edges) - 1)))
    return np.frombuffer(buf, dtype="<f8").reshape(stop - start, meta["n_channels"])


def check_read(meta: dict, start: int = 100000, n: int = 3000) -> bool:
    """`read_rows` gives what h5py reads."""
    f = h5py.File(remfile.File(meta["url"]), "r")
    ref = f["acquisition/ElectricalSeries/data"][start:start + n]
    f.close()
    return bool(np.array_equal(ref, read_rows(meta, start, start + n)))


# ---------------------------------------------------------------- blocks and labels

def assign_blocks(labelled: list[dict]) -> pd.DataFrame:
    """One row per labelled block file, ordered by start time within each rat."""
    df = pd.DataFrame([{k: m[k] for k in ("asset_id", "subject", "group", "label", "start", "n_samples")}
                       for m in labelled])
    df["group"] = df.group.str.replace(" group", "", regex=False).replace({"tFUS": "tFUS", "sham": "sham"})
    df = df.sort_values(["subject", "start"]).reset_index(drop=True)
    df["order"] = df.groupby("subject").cumcount()
    df["block"] = df.order.map(dict(enumerate(BLOCKS)))
    df["minutes"] = df.n_samples / RATE / 60
    return df


def seizures(meta: dict, hemi: str) -> pd.DataFrame:
    """Seizures of one hemisphere, in seconds from the block start."""
    iv = meta["intervals"]
    s = iv[iv.tag == hemi][["start", "stop"]].sort_values("start") * MINUTES
    s["duration"] = s.stop - s.start
    T = meta["n_samples"] / RATE
    s["truncated"] = (s.start <= 1.5 / RATE) | (s.stop >= T - 1.5 / RATE)
    return s.reset_index(drop=True)


def merged_periods(meta: dict) -> np.ndarray:
    """Union of the ipsilateral and contralateral seizure periods (seconds), merged where they overlap."""
    iv = meta["intervals"]
    iv = iv[iv.tag.isin(["ipsilateral", "contralateral"])].sort_values("start")
    out = []
    for a, b in (iv[["start", "stop"]].to_numpy() * MINUTES):
        if out and a <= out[-1][1]:
            out[-1][1] = max(out[-1][1], b)
        else:
            out.append([a, b])
    return np.array(out).reshape(-1, 2)


def block_metrics(meta: dict, hemi: str) -> dict:
    """Seizure Count, Percent Time in Seizure, Seizure Duration and Inter-Seizure Interval (M2)."""
    s = seizures(meta, hemi)
    T = meta["n_samples"] / RATE
    full = s[~s.truncated]
    gaps = (s.start.to_numpy()[1:] - s.stop.to_numpy()[:-1]) if len(s) > 1 else np.array([])
    onsets = np.diff(s.start.to_numpy()) if len(s) > 1 else np.array([])
    return {"count": len(s), "percent_time": 100 * s.duration.sum() / T,
            "duration": full.duration.mean() if len(full) else np.nan,
            "isi_gap": gaps.mean() if len(gaps) else np.nan,
            "isi_onset": onsets.mean() if len(onsets) else np.nan,
            "n_truncated": int(s.truncated.sum())}


# ---------------------------------------------------------------- statistics

def _contrast_rows(di, cells: pd.DataFrame) -> np.ndarray:
    from patsy import build_design_matrices
    return np.asarray(build_design_matrices([di], cells)[0])


def twoway(df: pd.DataFrame, value: str, a: str, b: str, subject: str, comparisons: list, rm: bool = False,
           families: dict | None = None) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Two-way ANOVA of `value` on factors a and b, with Bonferroni post hoc comparisons.

    comparisons: list of (name, {a: x, b: y}, {a: x2, b: y2}, family). Within each family the p values
    are multiplied by the family's size (capped at 1). rm=False: ordinary ANOVA (OLS, type II), post hoc
    t on the pooled residual error and its df. rm=True: mixed model with a random intercept per subject;
    main effects and interaction by Wald tests, post hoc by Wald z of the contrast.
    """
    import statsmodels.formula.api as smf
    from scipy import stats
    from statsmodels.stats.anova import anova_lm
    d = df.dropna(subset=[value]).copy()
    rhs = f"C({a}, Sum) * C({b}, Sum)"
    formula = f"{value} ~ {rhs}"
    from patsy import dmatrix
    di = dmatrix(rhs, d).design_info
    if not rm:
        res = smf.ols(formula, d).fit()
        table = anova_lm(res, typ=2)[["F", "PR(>F)"]].dropna().rename(columns={"PR(>F)": "p"})
        V, beta, dof = res.cov_params().to_numpy(), res.params.to_numpy(), res.df_resid
    else:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")              # boundary fits (zero rat variance) are expected
            res = smf.mixedlm(formula, d, groups=d[subject]).fit(reml=True)
        names = list(res.fe_params.index)
        beta = res.fe_params.to_numpy()
        V = res.cov_params().loc[names, names].to_numpy()
        rows = []
        for term in (f"C({a}, Sum)", f"C({b}, Sum)", f"C({a}, Sum):C({b}, Sum)"):
            if ":" in term:
                idx = [i for i, n in enumerate(names) if ":" in n]
            else:
                idx = [i for i, n in enumerate(names) if n.startswith(term + "[") and ":" not in n]
            if not idx:
                continue
            bb, VV = beta[idx], V[np.ix_(idx, idx)]
            chi = float(bb @ np.linalg.pinv(VV) @ bb)
            rows.append({"term": term, "F": chi / len(idx), "p": stats.chi2.sf(chi, len(idx))})
        table = pd.DataFrame(rows).set_index("term")
        dof = None
    out = []
    for name, c1, c2, fam in comparisons:
        x1 = _contrast_rows(di, pd.DataFrame([c1]))[0][: len(beta)]
        x2 = _contrast_rows(di, pd.DataFrame([c2]))[0][: len(beta)]
        c = x1 - x2
        est, se = float(c @ beta), float(np.sqrt(c @ V @ c))
        stat = est / se if se > 0 else np.nan
        p = 2 * (stats.t.sf(abs(stat), dof) if dof is not None else stats.norm.sf(abs(stat)))
        n1 = int(((d[a] == c1[a]) & (d[b] == c1[b])).sum())
        n2 = int(((d[a] == c2[a]) & (d[b] == c2[b])).sum())
        out.append({"comparison": name, "family": fam, "diff": est, "stat": stat, "p_raw": p, "n1": n1, "n2": n2})
    post = pd.DataFrame(out)
    if len(post):
        size = post.groupby("family").comparison.transform("size")
        post["p_family"] = np.minimum(1.0, post.p_raw * size)
        post["p_all"] = np.minimum(1.0, post.p_raw * len(post))
    return table, post


# ---------------------------------------------------------------- spectra and PLI

def _notch(x: np.ndarray, fs: float) -> np.ndarray:
    b, a = signal.iirnotch(60.0, 30.0, fs)
    return signal.filtfilt(b, a, x, axis=0)


def band_powers(f: np.ndarray, p: np.ndarray) -> dict:
    """Band power (sum of PSD bins in the band), and the totals 3-300 Hz and 0-Nyquist."""
    df = f[1] - f[0]
    out = {band: p[(f >= lo) & (f < hi)].sum(axis=0) * df for band, (lo, hi) in BANDS.items()}
    out["total_3_300"] = p[(f >= 3) & (f <= 300)].sum(axis=0) * df
    out["total_all"] = p.sum(axis=0) * df
    return out


def welch_segments(x: np.ndarray, fs: float, periods: np.ndarray | None = None):
    """Welch PSD over the whole signal, or averaged over the given periods (seconds) weighted by
    the number of windows each holds; periods shorter than one window are skipped."""
    nper = int(round(WELCH_S * fs))
    if periods is None:
        return signal.welch(x, fs, window="hann", nperseg=nper, noverlap=nper // 2, axis=0)
    acc, w, f = 0.0, 0, None
    for a, b in periods:
        i, j = int(a * fs), int(b * fs)
        if j - i < nper:
            continue
        f, p = signal.welch(x[i:j], fs, window="hann", nperseg=nper, noverlap=nper // 2, axis=0)
        k = 1 + (j - i - nper) // (nper // 2)
        acc, w = acc + p * k, w + k
    if f is None:
        return None, None
    return f, acc / w


def pli(phase_a: np.ndarray, phase_b: np.ndarray) -> np.ndarray:
    """PLI between each column of a and each column of b over axis 0 (Eq. 2): shape (na, nb)."""
    sa, ca = np.sin(phase_a), np.cos(phase_a)
    sb, cb = np.sin(phase_b), np.cos(phase_b)
    # sin(a - b) = sin a cos b - cos a sin b
    out = np.empty((phase_a.shape[1], phase_b.shape[1]))
    for i in range(phase_a.shape[1]):
        out[i] = np.abs(np.sign(sa[:, [i]] * cb - ca[:, [i]] * sb).mean(axis=0))
    return out


def band_sos(band: str, fs: float):
    lo, hi = BANDS[band]
    return signal.butter(4, [lo, hi], btype="bandpass", fs=fs, output="sos")


def process_block(meta: dict, rows_per_read: int = 1_000_000) -> dict:
    """One labelled EEG block: PSD of channels 8 and 25 (whole block, seizure periods per hemisphere,
    merged seizure periods), 30-80 Hz power in 1 s bins (for the clock check of the labels), and the
    seizure PLI per band for S1 and non-S1 pairs.

    The 32 channels are read in pieces, re-referenced to their common average, and decimated by 3
    (polyphase FIR) for the PLI; each piece is read with a margin so that the decimation has no edges.
    The PLI band filters run on each seizure period with 2 s of signal on either side."""
    n = meta["n_samples"]
    pad = 3000
    car2 = np.empty((n, 2))
    dec = []
    for s in range(0, n, rows_per_read):
        a, b = max(0, s - pad), min(n, s + rows_per_read + pad)
        x = read_rows(meta, a, b)
        x = x - x.mean(axis=1, keepdims=True)                 # common average reference
        e = min(n, s + rows_per_read)
        car2[s:e] = x[s - a:e - a][:, [IPSI_CH - 1, CONTRA_CH - 1]]
        y = signal.resample_poly(x, 1, DECIMATE, axis=0)
        k0 = (s - a) // DECIMATE
        dec.append(y[k0:k0 + (e - s + DECIMATE - 1) // DECIMATE].astype(np.float32))
        del x, y
    xd = np.concatenate(dec)
    del dec
    car2 = _notch(car2, RATE)
    out = {"asset_id": meta["asset_id"], "n_samples": n}
    out["psd_block"] = welch_segments(car2, RATE)
    per = {h: seizures(meta, h)[["start", "stop"]].to_numpy() for h in ("ipsilateral", "contralateral")}
    merged = merged_periods(meta)
    out["psd_seiz_ipsi"] = welch_segments(car2[:, [0]], RATE, per["ipsilateral"])
    out["psd_seiz_contra"] = welch_segments(car2[:, [1]], RATE, per["contralateral"])
    out["psd_seiz_merged"] = welch_segments(car2, RATE, merged)
    out["periods_merged"] = merged
    sos = signal.butter(4, [30, 80], btype="bandpass", fs=RATE, output="sos")
    g = signal.sosfiltfilt(sos, car2, axis=0) ** 2
    nb = int(n // RATE)
    edges = (np.arange(nb + 1) * RATE).astype(int)
    out["gamma_1s"] = np.add.reduceat(g[: edges[-1]], edges[:-1], axis=0) / np.diff(edges)[:, None]
    del g, car2
    fs_d = RATE / DECIMATE
    bn, an = signal.iirnotch(60.0, 30.0, fs_d)
    sos_bp = signal.butter(4, [3, 300], btype="bandpass", fs=fs_d, output="sos")
    ii = [c - 1 for c in S1_IPSI + NONS1_IPSI]
    cc = [c - 1 for c in S1_CONTRA + NONS1_CONTRA]
    margin = int(2 * fs_d)
    segs = [(int(a0 * fs_d), int(b0 * fs_d)) for a0, b0 in merged if (b0 - a0) >= 1.0]
    acc = {band: ([], []) for band in BANDS}
    for i, j in segs:
        i0, j0 = max(0, i - margin), min(len(xd), j + margin)
        seg = signal.filtfilt(bn, an, xd[i0:j0].astype(np.float64), axis=0)
        seg = signal.sosfiltfilt(sos_bp, seg, axis=0)
        for band in BANDS:
            ph = np.angle(signal.hilbert(signal.sosfiltfilt(band_sos(band, fs_d), seg, axis=0), axis=0))
            ph = ph[i - i0: i - i0 + (min(j, len(xd)) - i)]
            acc[band][0].append(pli(ph[:, ii], ph[:, cc]))
            acc[band][1].append(ph[:, ii + cc].astype(np.float32))
    res = {}
    for band, (per_seiz, cat) in acc.items():
        if per_seiz:
            phc = np.concatenate(cat)
            res[band] = {"per_seizure": np.mean(per_seiz, axis=0),
                         "concat": pli(phc[:, : len(ii)], phc[:, len(ii):]), "n": len(per_seiz),
                         "seconds": len(phc) / fs_d}
        else:
            res[band] = None
    out["pli"] = res
    return out


def process_blocks(metas: list[dict], workers: int = 3) -> dict:
    """process_block over many files in parallel processes; returns {asset_id: result}."""
    from concurrent.futures import ProcessPoolExecutor
    import multiprocessing as mp
    with ProcessPoolExecutor(workers, mp_context=mp.get_context("spawn")) as ex:
        return {r["asset_id"]: r for r in ex.map(process_block, metas)}


def pair_means(m: np.ndarray) -> dict:
    """Mean PLI over S1 pairs (left S1 with right S1) and over non-S1 pairs, from a matrix whose rows
    are ipsilateral channels S1_IPSI + NONS1_IPSI and columns contralateral S1_CONTRA + NONS1_CONTRA."""
    k = len(S1_IPSI)
    return {"S1": float(m[:k, :k].mean()), "nonS1": float(m[k:, k:].mean())}


def group_block_tests(df: pd.DataFrame, value: str, blocks=BLOCKS[:4]) -> dict:
    """Group (sham, tFUS) by block two-way ANOVA (M3), both readings. Post hoc families: `within`, each
    block against baseline in each group; `between`, sham against tFUS at each block."""
    d = df[df.block.isin(blocks)]
    comps = [(f"{g} baseline-{b}", {"group": g, "block": "baseline"}, {"group": g, "block": b}, "within")
             for g in ("sham", "tFUS") for b in blocks[1:]]
    comps += [(f"sham-tFUS {b}", {"group": "sham", "block": b}, {"group": "tFUS", "block": b}, "between")
              for b in blocks]
    return {("repeated" if rm else "ordinary"): twoway(d, value, "group", "block", "subject", comps, rm=rm)
            for rm in (False, True)}


def hemi_block_tests(df: pd.DataFrame, value: str, blocks=BLOCKS) -> dict:
    """Hemisphere by block two-way ANOVA within one group (Figs. 2 and S4), both readings. Post hoc
    families: `blocks`, each pair of blocks within each hemisphere; `hemi`, the hemispheres at each block."""
    comps = []
    for h in ("ipsilateral", "contralateral"):
        for i, b1 in enumerate(blocks):
            for b2 in blocks[i + 1:]:
                comps.append((f"{h[:6]} {b1}-{b2}", {"hemi": h, "block": b1}, {"hemi": h, "block": b2}, "blocks"))
    for b in blocks:
        comps.append((f"ipsi-contra {b}", {"hemi": "ipsilateral", "block": b},
                      {"hemi": "contralateral", "block": b}, "hemi"))
    return {("repeated" if rm else "ordinary"): twoway(df, value, "hemi", "block", "subject", comps, rm=rm)
            for rm in (False, True)}


def significant(post: pd.DataFrame, family: bool = True) -> pd.DataFrame:
    """Post hoc rows significant at 0.05 under the family reading (i) or the all-in-one reading (ii)."""
    return post[post["p_family" if family else "p_all"] < 0.05]


# ---------------------------------------------------------------- wild-type phase (Fig. 5)

EP_PRE, EP_POST = 0.020, 0.200        # s, the windows of Fig. 5 (-20 to 0, 0 to 20, 20 to 200 ms)
N_TRIALS = 200                        # "extracting 200 EPs" (Methods E); 200 trials per position (supplement)


def read_epochs(meta: dict, onsets: np.ndarray, pre: float = EP_PRE, post: float = EP_POST,
                threads: int = 32) -> np.ndarray:
    """Epochs (trials, samples, channels) from onset - pre to onset + post, onsets in seconds; onsets
    whose window leaves the recording are dropped."""
    n0, n1 = int(round(pre * RATE)), int(round(post * RATE))
    idx = [int(round(t * RATE)) for t in onsets]
    idx = [i for i in idx if i - n0 >= 0 and i + n1 <= meta["n_samples"]]

    def one(i):
        return read_rows(meta, i - n0, i + n1, threads=1)

    with ThreadPoolExecutor(threads) as ex:
        return np.array(list(ex.map(one, idx)))


def evoked(epochs: np.ndarray, pre: float = EP_PRE) -> np.ndarray:
    """Mean over trials after subtracting each trial's mean of the pre-onset window (the Fig. 5B
    normalization, read as a baseline subtraction in the claims file)."""
    n0 = int(round(pre * RATE))
    return (epochs - epochs[:, :n0].mean(axis=1, keepdims=True)).mean(axis=0)


def timepoint_tests(a: np.ndarray, b: np.ndarray) -> pd.DataFrame:
    """tFUS against sham at each time point, a and b of shape (rats, time), the same rats in both.

    Ordinary reading: a two-way ANOVA group by time point; the post hoc t at each time point uses the
    pooled residual mean square of the full model and its df. Repeated reading: both groups come from
    the same rats, so each comparison is a paired t on that time point's differences (the per-comparison
    error a repeated-measures analysis uses without assuming sphericity). Bonferroni over the time points."""
    from scipy import stats
    n, T = a.shape
    resid = np.concatenate([a - a.mean(0), b - b.mean(0)])
    df_res = 2 * n * T - 2 * T
    mse = (resid ** 2).sum() / df_res
    diff = a.mean(0) - b.mean(0)
    t_ord = diff / np.sqrt(mse * 2 / n)
    p_ord = 2 * stats.t.sf(np.abs(t_ord), df_res)
    t_rm, p_rm = stats.ttest_rel(a, b, axis=0)
    return pd.DataFrame({"diff": diff, "p_ordinary": np.minimum(1, p_ord * T), "p_repeated": np.minimum(1, p_rm * T)})


def wild_pli(meta: dict, n_trials: int = N_TRIALS, onsets: np.ndarray | None = None) -> dict:
    """PLI of the three windows of Fig. 5 (pre -20-0 ms, tFUS 0-20 ms, post 20-200 ms) per band, for every
    pair of one ipsilateral and one contralateral EEG channel, from the first n_trials onsets of the file's
    interval table: per trial and averaged (reading a) and over the concatenated trial samples (reading b).
    The whole recording is re-referenced (CAR), notched at 60 Hz, band filtered and Hilbert transformed
    before the epochs are cut, so the short windows carry no filter edges."""
    x = read_rows(meta, 0, meta["n_samples"])
    x = x - x.mean(axis=1, keepdims=True)
    x = _notch(x, RATE)
    if onsets is None:
        onsets = np.sort(meta["intervals"].start.to_numpy())[:n_trials]
    ii = [c - 1 for c in S1_IPSI + NONS1_IPSI]
    cc = [c - 1 for c in S1_CONTRA + NONS1_CONTRA]
    n0, n1 = int(round(EP_PRE * RATE)), int(round(EP_POST * RATE))
    w20 = int(round(0.020 * RATE))
    idx = np.array([int(round(t * RATE)) for t in onsets])
    idx = idx[(idx - n0 >= 0) & (idx + n1 <= len(x))]
    windows = {"pre": (-n0, 0), "tfus": (0, w20), "post": (w20, n1)}
    out = {"n_trials": len(idx)}
    for band in BANDS:
        ph = np.angle(signal.hilbert(signal.sosfiltfilt(band_sos(band, RATE), x, axis=0), axis=0))
        res = {}
        for name, (a, b) in windows.items():
            seg = np.stack([ph[i + a:i + b] for i in idx])            # trials, samples, channels
            d = np.sin(seg[:, :, ii][:, :, :, None] - seg[:, :, cc][:, :, None, :])
            s = np.sign(d)
            res[name] = {"per_trial": np.abs(s.mean(axis=1)).mean(axis=0), "concat": np.abs(s.mean(axis=(0, 1)))}
        out[band] = res
    return out
