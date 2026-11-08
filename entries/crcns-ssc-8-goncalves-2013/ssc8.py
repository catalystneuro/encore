"""Loading and measures for CRCNS data set ssc-8 (doi:10.6080/K0X63K3X).

Goncalves, Anstey, Golshani & Portera-Cailliau (2013), Nature Neuroscience 16:903-909,
doi:10.1038/nn.3415. Two-photon calcium imaging of L2/3 barrel cortex in unanesthetized WT and
Fmr1 -/- (KO) mice at P9-11, P14-16 and P30-40.

The data set (unversioned on CRCNS; files under ssc-8/live/ in the bucket crcnsarchive) holds
`firingrates_and_distances.mat`, with per mouse a frames x neurons matrix of estimated firing
rates and a neurons x neurons matrix of cell-to-cell distances in microns, and
`Ca2+_imaging_TIFFs.tar.gz`, the raw movies, one per mouse. Both are streamed from the bucket;
nothing is written to disk.

Where the parameters come from:

- `FRAME_HZ` = 3.9 Hz, the Methods ("an acquisition speed of 3.9 Hz") and the data descriptor.
  The movie folders are named "4Hz"; `FRAME_HZ_ALT` = 4.0 is shown as a variant where a rate in
  time units is computed.
- Correlation measures (claims file, shared method): `xcorr0`, the zero-lag normalised
  cross-correlation without mean subtraction (reading C-b, the claims file's main reading);
  `pearson`, the paper's own variant; `spearman`, reading C-a, a variant only. Trace reading T-a,
  the deposited estimated firing rates; T-b (low-pass filtered dF/F) cannot be run, as the data
  set holds no cell contours.
- Distance bins under 100, 100 to 200 and over 200 um (claims file, fig1d; Results, paragraph 1).
  A pair at exactly 100 or 200 um goes to the upper bin, a standard choice that cannot change a
  result at this precision.
- Per mouse, the mean over its pairs (claims file, shared method; the n in the paper are mice).
- The unequal-variance 2 x 3 fixed-effects ANOVA with Satterthwaite error degrees of freedom
  (Online Methods, Statistical Analyses) is fitted on the six cell means with each cell's
  variance of the mean (s^2/n); a contrast of k rows is tested with the Welch-James statistic
  (Johansen 1980), which for one row is the Welch t with Satterthwaite degrees of freedom. The
  claims file names weighted least squares with inverse-variance weights and Satterthwaite
  degrees of freedom as its standard choice; this is that model.
- Peaks of synchrony (Online Methods, "To calculate frequency..."): per frame the percent of
  cells active; 100 shuffles of each cell's trace keeping its mean; the 95th percentile of the
  100 shuffled peaks is the threshold; an event runs while the percent active is above it. The
  readings of "active" (R-a, rate above 0; R-b, at least one estimated spike in the frame, which
  is rate / FRAME_HZ >= 1 when the rates are in Hz, unit reading U-a, and rate >= 1 when they are
  per frame, U-b, here named "R-b/U-b") and of the shuffle (S-a, permutation of frames; S-b,
  circular shift) are the claims file's. The seed is a standard choice.
"""

from __future__ import annotations

import hashlib
import io
import struct
import tarfile

import fsspec
import numpy as np
import scipy.io
from scipy import stats

BUCKET = "https://crcnsarchive.s3-us-west-2.amazonaws.com"
DATASET_ID = "ssc-8"
DATASET_VERSION = "unversioned"   # CRCNS data sets are not versioned (docs/archives.md)
DATASET_DOI = "10.6080/K0X63K3X"
MAT_URL = f"{BUCKET}/ssc-8/live/firingrates_and_distances.mat"
TIFF_URL = f"{BUCKET}/ssc-8/live/Ca2%2B_imaging_TIFFs.tar.gz"
CHECKSUMS_URL = f"{BUCKET}/ssc-8/live/checksums.md5"

GENOTYPES = ["WT", "KO"]
AGES = ["P9P11", "P14P16", "P30P40"]
AGE_LABEL = {"P9P11": "P9-11", "P14P16": "P14-16", "P30P40": "P30-40"}
GROUPS = [(g, a) for g in GENOTYPES for a in AGES]
# Folder names in the TIFF archive for each group.
TIFF_FOLDER = {("WT", "P9P11"): "WT_P9-P11_4Hz", ("WT", "P14P16"): "WT_P14-P16_4Hz",
               ("WT", "P30P40"): "WT_P30-P40_4Hz", ("KO", "P9P11"): "Fmr1_KO_P9-P11_4Hz",
               ("KO", "P14P16"): "Fmr1_KO_P14-P16_4Hz", ("KO", "P30P40"): "Fmr1_KO_P30-P40_4Hz"}

FRAME_HZ = 3.9
FRAME_HZ_ALT = 4.0
BINS = [(0.0, 100.0, "<100"), (100.0, 200.0, "100-200"), (200.0, np.inf, ">200")]
N_SHUFFLES = 100
SHUFFLE_PERCENTILE = 95


def checksums() -> dict[str, str]:
    """The data set's published MD5 sums, by file name."""
    with fsspec.open(CHECKSUMS_URL, "rt") as f:
        return {line.split()[1]: line.split()[0] for line in f if line.strip()}


def load_mat() -> tuple[dict, str]:
    """Return {(genotype, age): [{'rates': T x N, 'dist': N x N}, ...]} and the file's MD5.

    The 14.7 MB file is read into memory from the bucket."""
    with fsspec.open(MAT_URL, "rb") as f:
        raw = f.read()
    md5 = hashlib.md5(raw).hexdigest()
    m = scipy.io.loadmat(io.BytesIO(raw))
    data = {}
    for g, a in GROUPS:
        movies = m[f"{g}_{a}_movies"].ravel()
        dists = m[f"{g}_{a}_distances"].ravel()
        data[(g, a)] = [{"rates": np.asarray(r, float), "dist": np.asarray(d, float)}
                        for r, d in zip(movies, dists)]
    keys = sorted(k for k in m if not k.startswith("__"))
    return data, md5, keys


# ---------------------------------------------------------------- TIFF movies

def _tiff_frames(buf: bytes):
    """Walk the IFD chain of a classic TIFF; return (n_frames, height, width, bits, frame means).

    Each frame's mean pixel value is computed from its strips, assuming uncompressed data, which
    the Compression tag is checked for."""
    endian = "<" if buf[:2] == b"II" else ">"
    (magic,) = struct.unpack(endian + "H", buf[2:4])
    if magic != 42:
        raise ValueError("not a classic TIFF")
    (off,) = struct.unpack(endian + "I", buf[4:8])
    means, shape, bits = [], None, None
    tsize = {1: 1, 3: 2, 4: 4}
    while off:
        (n,) = struct.unpack(endian + "H", buf[off:off + 2])
        tags = {}
        for i in range(n):
            e = off + 2 + 12 * i
            tag, typ, cnt = struct.unpack(endian + "HHI", buf[e:e + 8])
            if typ not in tsize:
                continue
            size = tsize[typ] * cnt
            code = {1: "B", 3: "H", 4: "I"}[typ]
            if size <= 4:
                vals = struct.unpack(endian + code * cnt, buf[e + 8:e + 8 + size])
            else:
                (p,) = struct.unpack(endian + "I", buf[e + 8:e + 12])
                vals = struct.unpack(endian + code * cnt, buf[p:p + size])
            tags[tag] = vals
        w, h = tags[256][0], tags[257][0]
        bits = tags.get(258, (1,))[0]
        if tags.get(259, (1,))[0] != 1:
            raise ValueError("compressed TIFF")
        shape = (h, w)
        dt = np.dtype(endian + {8: "u1", 16: "u2"}[bits])
        tot, cnt_px = 0.0, 0
        for so, sb in zip(tags[273], tags[279]):
            px = np.frombuffer(buf, dtype=dt, count=sb // dt.itemsize, offset=so)
            tot += float(px.sum(dtype=np.float64))
            cnt_px += px.size
        means.append(tot / cnt_px)
        (off,) = struct.unpack(endian + "I", buf[off + 2 + 12 * n:off + 6 + 12 * n])
    return len(means), shape, bits, np.array(means)


def survey_movies() -> list[dict]:
    """Stream the TIFF archive once; per member, its folder, name, size, MD5, frame count, frame
    shape and per-frame mean intensity. One movie is held in memory at a time (up to 373 MB)."""
    out = []
    with fsspec.open(TIFF_URL, "rb", block_size=2**24) as f:
        with tarfile.open(fileobj=f, mode="r|gz") as tf:
            for mem in tf:
                if not mem.isfile():
                    continue
                buf = tf.extractfile(mem).read()
                parts = mem.name.split("/")
                rec = {"path": mem.name, "folder": parts[-2] if len(parts) > 2 else "",
                       "name": parts[-1], "bytes": mem.size,
                       "md5": hashlib.md5(buf).hexdigest()}
                try:
                    n, shape, bits, means = _tiff_frames(buf)
                    rec.update(tiff=True, frames=n, height=shape[0], width=shape[1], bits=bits,
                               frame_mean=means)
                except Exception as e:  # macOS resource forks and the like
                    rec.update(tiff=False, error=str(e)[:60])
                del buf
                out.append(rec)
    return out


# ---------------------------------------------------------------- correlation

def pair_corr(x: np.ndarray, measure: str) -> np.ndarray:
    """N x N matrix of zero-lag correlations between the columns of x (T x N)."""
    x = np.asarray(x, float)
    if measure == "spearman":
        x = np.apply_along_axis(stats.rankdata, 0, x)
        measure = "pearson"
    if measure == "pearson":
        x = x - x.mean(0)
    elif measure != "xcorr0":
        raise ValueError(measure)
    norm = np.sqrt((x * x).sum(0))
    with np.errstate(invalid="ignore", divide="ignore"):
        c = (x.T @ x) / np.outer(norm, norm)
    return c


def mouse_pair_means(rec: dict, measure: str) -> dict:
    """Per mouse, the mean correlation of its pairs in each distance bin and over all pairs;
    pairs with an undefined correlation (a silent cell) are left out and counted."""
    c = pair_corr(rec["rates"], measure)
    d = rec["dist"]
    iu = np.triu_indices_from(d, 1)
    cv, dv = c[iu], d[iu]
    ok = np.isfinite(cv)
    res = {"n_pairs": int(ok.sum()), "n_undefined": int((~ok).sum()), "all": float(cv[ok].mean())}
    for lo, hi, name in BINS:
        sel = ok & (dv >= lo) & (dv < hi)
        res[name] = float(cv[sel].mean()) if sel.any() else np.nan
        res["n_" + name] = int(sel.sum())
    return res


# ---------------------------------------------------------------- statistics

def welch_james(means, variances, ns, L) -> dict:
    """Welch-James test of L @ mu = 0 for independent groups with unequal variances.

    means, variances (sample variances) and ns are per group; L is k x G. Returns F, df1, df2, p.
    For k = 1 this is the Welch t-test squared with Satterthwaite degrees of freedom."""
    m = np.asarray(means, float)
    v = np.asarray(variances, float) / np.asarray(ns, float)
    n = np.asarray(ns, float)
    L = np.atleast_2d(np.asarray(L, float))
    k = L.shape[0]
    V = np.diag(v)
    LVL = L @ V @ L.T
    inv = np.linalg.inv(LVL)
    est = L @ m
    T = float(est @ inv @ est)
    P = V @ L.T @ inv @ L
    A = 0.0
    for j in range(len(m)):
        Q = np.zeros((len(m), len(m)))
        Q[j, j] = 1.0
        PQ = P @ Q
        A += (np.trace(PQ @ PQ) + np.trace(PQ) ** 2) / (2 * (n[j] - 1))
    c = k + 2 * A - 6 * A / (k + 2)
    df2 = k * (k + 2) / (3 * A)
    F = T / c
    return {"F": F, "df1": k, "df2": df2, "p": float(stats.f.sf(F, k, df2)), "estimate": est}


def welch_anova(groups) -> dict:
    """Welch's one-way ANOVA for unequal variances."""
    g = [np.asarray(x, float) for x in groups]
    n = np.array([len(x) for x in g], float)
    m = np.array([x.mean() for x in g])
    w = n / np.array([x.var(ddof=1) for x in g])
    mw = (w * m).sum() / w.sum()
    k = len(g)
    num = (w * (m - mw) ** 2).sum() / (k - 1)
    lam = 3 * (((1 - w / w.sum()) ** 2) / (n - 1)).sum() / (k ** 2 - 1)
    F = num / (1 + 2 * (k - 2) * lam / 3)
    df2 = 1 / lam
    return {"F": F, "df1": k - 1, "df2": df2, "p": float(stats.f.sf(F, k - 1, df2))}


def two_by_three(values: dict) -> dict:
    """The unequal-variance 2 x 3 model on per-mouse values {(genotype, age): array}.

    Returns the genotype main effect (KO minus WT, equal weight on the three ages), the age
    effect within each genotype (2 df) and the interaction."""
    order = GROUPS
    means = [np.mean(values[k]) for k in order]
    var = [np.var(values[k], ddof=1) for k in order]
    ns = [len(values[k]) for k in order]
    geno = np.array([[-1, -1, -1, 1, 1, 1]]) / 3.0
    age_wt = np.array([[1, -1, 0, 0, 0, 0], [0, 1, -1, 0, 0, 0]])
    age_ko = np.array([[0, 0, 0, 1, -1, 0], [0, 0, 0, 0, 1, -1]])
    inter = np.array([[1, -1, 0, -1, 1, 0], [0, 1, -1, 0, -1, 1]])
    age_main = np.array([[1, -1, 0, 1, -1, 0], [0, 1, -1, 0, 1, -1]]) / 2.0
    return {"genotype": welch_james(means, var, ns, geno),
            "age_main": welch_james(means, var, ns, age_main),
            "age_within_WT": welch_james(means, var, ns, age_wt),
            "age_within_KO": welch_james(means, var, ns, age_ko),
            "interaction": welch_james(means, var, ns, inter)}


def sem(x) -> float:
    x = np.asarray(x, float)
    return float(x.std(ddof=1) / np.sqrt(len(x)))


# ---------------------------------------------------------------- peaks of synchrony

def _active(rates: np.ndarray, rule: str) -> np.ndarray:
    if rule == "R-a":
        return rates > 0
    if rule == "R-b":
        return rates / FRAME_HZ >= 1.0
    if rule == "R-b/U-b":
        return rates >= 1.0
    raise ValueError(rule)


def _shuffle(rates: np.ndarray, how: str, rng: np.random.Generator) -> np.ndarray:
    T, N = rates.shape
    if how == "S-a":
        idx = np.argsort(rng.random((T, N)), axis=0)
        return np.take_along_axis(rates, idx, axis=0)
    if how == "S-b":
        shifts = rng.integers(0, T, N)
        rows = (np.arange(T)[:, None] - shifts[None, :]) % T
        return np.take_along_axis(rates, rows, axis=0)
    raise ValueError(how)


def synchrony_events(rates: np.ndarray, rule: str, how: str, rng: np.random.Generator) -> dict:
    """Peaks of synchrony of one recording (Online Methods), under an active rule and a shuffle.

    Both shuffles keep each cell's mean rate, as the Methods require. Returns the threshold
    (percent of cells), the events as (start, end) frame indices (end exclusive), and the
    participation measures Q-a (per event, fraction of cells active in any frame of the event,
    averaged over events) and Q-b (fraction of cells active in at least one event)."""
    T, N = rates.shape
    act = _active(rates, rule)
    pct = 100.0 * act.mean(1)
    peaks = np.empty(N_SHUFFLES)
    for s in range(N_SHUFFLES):
        peaks[s] = 100.0 * _active(_shuffle(rates, how, rng), rule).mean(1).max()
    thr = float(np.percentile(peaks, SHUFFLE_PERCENTILE))
    above = pct > thr
    edges = np.diff(np.concatenate([[0], above.astype(int), [0]]))
    starts, ends = np.flatnonzero(edges == 1), np.flatnonzero(edges == -1)
    in_any = np.zeros(N, bool)
    frac = []
    for a, b in zip(starts, ends):
        part = act[a:b].any(0)
        in_any |= part
        frac.append(part.mean())
    return {"threshold": thr, "n_events": len(starts), "frames": T,
            "rate_per_s": len(starts) / (T / FRAME_HZ),
            "rate_per_s_4hz": len(starts) / (T / FRAME_HZ_ALT),
            "Q-a": float(np.mean(frac)) if frac else np.nan,
            "Q-b": float(in_any.mean()),
            "mean_pct_active": float(pct.mean())}
