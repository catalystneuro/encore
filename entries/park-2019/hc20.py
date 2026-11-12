"""Loading and measures for CRCNS hc-20 (Park and Fenton 2018), used to test Park et al. (2019).

The data set is one zip, ``hc-20/live/data.zip``, read in place from the public CRCNS bucket
with fsspec and zipfile (docs/archives.md, CRCNS). It holds one TSD file per unit and trial
(folders SA1, RA_rm, RA_ar, SA2 under data/TSD), FileNameList.xlsx matching the files of a
unit across trials, and the tracker's .dat files (data/DAT).

TSD format (data descriptor, "Data format"): an ASCII header, then per 30 Hz tracker sample
x (1 byte), y (1 byte), direction (4 bytes, degrees), the number of spikes in the sample
(1 byte) and that many spike timestamps (4 bytes each, 100 us units). Untracked samples have
x = y = 0 and direction 2**32 - 1; samples with direction above 360 are dropped, as the
paper's code does (HD_Max_likelihood.py, "if d > 360: d = nan").

Where each parameter comes from is said where it is defined: the claim's criterion (which
cites the paper or its code), a passage of the paper (cited), an assumption (said so), or a
standard choice for a detail that cannot change a result (said so).
"""
from __future__ import annotations

import io
import re
import struct
import zipfile

import fsspec
import numpy as np
import pandas as pd
from scipy import stats

DATASET = "hc-20"
VERSION = "unversioned"  # CRCNS data sets are not versioned (docs/archives.md); data.zip MD5 below
DATA_MD5 = "b82c7b97b0ba3491f04ecc4dbcd48e83"  # checksums.md5 of the data set
URL = "https://crcnsarchive.s3-us-west-2.amazonaws.com/hc-20/live/data.zip"
TRIALS = ("S1", "RR", "RA", "S2")  # stable1, rotating room frame, rotating arena frame, stable2
FOLDER = {"S1": "SA1", "RR": "RA_rm", "RA": "RA_ar", "S2": "SA2"}
NBINS = 36  # 10 degree tuning curves (STAR Methods, Data Analysis)
PIX_PER_CM = 2.1333  # TrackerResolution_PixPerCM in every .dat header (checked in the notebook)


def open_zip():
    f = fsspec.open(URL, block_size=2**20).open()
    return zipfile.ZipFile(f)


def read_tsd(raw: bytes) -> dict:
    """Parse one TSD file into per-sample arrays and spikes (with the sample each falls in)."""
    nl = int(raw[: raw.index(b"\n")])
    pos = 0
    hdr = []
    for _ in range(nl):
        e = raw.index(b"\n", pos)
        hdr.append(raw[pos:e].decode())
        pos = e + 1
    rate = float(next(h for h in hdr if "SAMPLING_INTERVAL" in h).split()[-1])
    t0 = int(next(h for h in hdr if "FIRST_TIMESTAMP" in h).split()[-1])
    up = struct.unpack_from
    xs, ys, ds, st, si = [], [], [], [], []
    i, n_bytes = 0, len(raw)
    while pos + 7 <= n_bytes:
        x, y, d, n = up("=BBIB", raw, pos)
        pos += 7
        xs.append(x)
        ys.append(y)
        ds.append(d)
        if n:
            st.extend(up("=%dI" % n, raw, pos))
            si.extend([i] * n)
            pos += 4 * n
        i += 1
    d = np.array(ds, dtype=np.float64)
    d[d > 360] = np.nan
    d[d == 360] = 0.0
    return dict(rate=rate, t0=t0, x=np.array(xs, np.int16), y=np.array(ys, np.int16), d=d,
                spk_t=np.array(st, np.int64), spk_i=np.array(si, np.int64), trailing=n_bytes - pos)


def unit_key(fname: str) -> tuple[str, str]:
    """(session, tetrode-cluster) from a TSD file name, e.g. ('1022R029', 'P8C3')."""
    m = re.match(r"(\d{4})(SA1|SA2|TF|RA|CON)(R\d{3})-R?cl\d?\.(P\d+C\d+)", fname)
    return m.group(1) + m.group(3), m.group(4)


def load(z=None) -> dict:
    """Read every unit's TSD files. Tracking is kept once per session and trial.

    Units are matched across trials by session and tetrode-cluster name. FileNameList.xlsx is
    read too and compared with this match (its stable2 column is misaligned in one session;
    see the notebook).
    """
    z = z or open_zip()
    names = [n for n in z.namelist() if n.startswith("data/TSD/") and not n.endswith("/")]
    flist = pd.read_excel(io.BytesIO(z.read("data/TSD/FileNameList.xlsx")), sheet_name=0, header=None)
    files = {tr: {} for tr in TRIALS}
    for n in names:
        folder, fname = n.split("/")[-2:]
        for tr, fo in FOLDER.items():
            if folder == fo:
                files[tr][unit_key(fname)] = n
    keys = sorted(files["S1"])
    trk, spk, tsd_meta = {}, {}, []
    for key in keys:
        sess, uid = key
        spk[key] = {}
        for tr in TRIALS:
            r = read_tsd(z.read(files[tr][key]))
            tsd_meta.append(dict(session=sess, unit=uid, trial=tr, rate=r["rate"], t0=r["t0"],
                                 n_samples=len(r["d"]), n_spikes=len(r["spk_t"]),
                                 trailing=r["trailing"],
                                 track_hash=hash(r["x"].tobytes() + r["y"].tobytes() + r["d"].tobytes())))
            if r["rate"] > 100:
                # one stable2 file states 2000 samples/s; its spike times span the trial at about
                # 30 Hz (see the notebook), so the rate of the other files is used
                r["rate"] = 30.022367
            this = dict(x=r["x"], y=r["y"], d=r["d"], rate=r["rate"], t0=r["t0"])
            if (sess, tr) not in trk:
                trk[(sess, tr)] = this
            elif not (np.array_equal(trk[(sess, tr)]["d"], r["d"], equal_nan=True)
                      and np.array_equal(trk[(sess, tr)]["x"], r["x"])):
                trk[(sess, tr, uid)] = this  # a unit whose file holds a different track
            spk[key][tr] = dict(i=r["spk_i"], t=(r["spk_t"] - r["t0"]) / 1e4)
    units = pd.DataFrame(keys, columns=["session", "unit"])
    units["rat"] = units.session.str[4:]
    units["file_S1"] = [files["S1"][k].split("/")[-1] for k in keys]
    units["file_S2"] = [files["S2"][k].split("/")[-1] for k in keys]
    return dict(units=units, trk=trk, spk=spk, meta=pd.DataFrame(tsd_meta), filelist=flist, z=z)


def track(D, key, tr):
    """The track a unit's spikes were stored with: the session's, or the unit's own when its file
    holds a different one."""
    sess, uid = key
    return D["trk"].get((sess, tr, uid), D["trk"][(sess, tr)])


def read_dat(raw: bytes):
    """A tracker .dat file: header lines and the sample table (columns from %Sample.0)."""
    txt = raw.decode("latin1")
    i = txt.index("%%END_HEADER")
    hdr = txt[:i]
    cols = re.search(r"%Sample\.0 \( (.*?) \)", hdr).group(1).split()
    tab = pd.read_csv(io.StringIO(txt[i:].split("\n", 1)[1]), sep=r"\s+", header=None, names=cols,
                      engine="c", na_values="*")
    return hdr, tab


def dat_value(hdr, name):
    m = re.search(r"%" + name + r"\.0 \( ([^)]*?) \)", hdr)
    return m.group(1).split() if m else None


def dat_session(fname):
    m = re.match(r"(\d{4})(?:TF|RA|SA1|SA2|CON)R?(\d{3})", fname)
    return m.group(1) + "R" + m.group(2)


# ---------------------------------------------------------------- tuning measures

def bin_index(d_deg: np.ndarray, nbins: int = NBINS) -> np.ndarray:
    """Bin of each direction (nan stays -1); bins start at 0 degrees, as in the paper's code."""
    b = np.full(len(d_deg), -1, dtype=np.int64)
    ok = ~np.isnan(d_deg)
    b[ok] = np.floor(d_deg[ok] / (360 / nbins)).astype(np.int64) % nbins
    return b


def tuning(d_deg, spk_i, rate, nbins=NBINS, mask=None):
    """Rate per direction bin: spikes over time in the bin (STAR Methods, Data Analysis).

    Returns (rate curve, spike counts, occupancy in s). ``mask`` restricts the samples used
    (for halves of a trial).
    """
    b = bin_index(d_deg, nbins)
    if mask is not None:
        b = np.where(mask, b, -1)
    occ = np.bincount(b[b >= 0], minlength=nbins) / rate
    sb = b[spk_i]
    cnt = np.bincount(sb[sb >= 0], minlength=nbins).astype(float)
    with np.errstate(invalid="ignore", divide="ignore"):
        curve = np.where(occ > 0, cnt / occ, 0.0)
    return curve, cnt, occ


def centers(nbins=NBINS):
    return (np.arange(nbins) + 0.5) * 2 * np.pi / nbins


def resultant(curve, ang=None):
    """Rayleigh vector length and mean angle of a tuning curve (Quantifying Head-direction
    Signals, Directionality)."""
    ang = centers(len(curve)) if ang is None else ang
    s = np.sum(curve)
    if s <= 0:
        return np.nan, np.nan
    v = np.sum(curve * np.exp(1j * ang)) / s
    return np.abs(v), np.angle(v) % (2 * np.pi)


def pref_dir(curve):
    """Bin of maximum rate, in degrees (Quantifying Head-direction Signals, Preferred direction)."""
    return np.degrees(centers(len(curve))[int(np.argmax(curve))])


def circ_absdiff_deg(a, b):
    """Absolute circular difference in degrees, 0 to 180 (claim fig1d-preference-change)."""
    return np.abs((np.asarray(a) - np.asarray(b) + 180) % 360 - 180)


def kt_prob(v):
    """Krichevsky-Trofimov estimate: (n_i + 0.5) / (N + 0.5 jmax) (Directional Stability)."""
    v = np.asarray(v, float)
    return (v + 0.5) / (v.sum() + 0.5 * len(v))


def kld(a, b):
    """Resistor average of the two Kullback-Leibler divergences (Directional Stability).

    Natural log; the base scales every value equally and does not change a test (criterion).
    """
    p, q = kt_prob(a), kt_prob(b)
    d12 = np.sum(p * np.log(p / q))
    d21 = np.sum(q * np.log(q / p))
    return d12 * d21 / (d12 + d21) if d12 + d21 > 0 else 0.0


# ---------------------------------------------------------------- circular statistics

def rayleigh_p(r, n):
    """Rayleigh test p from resultant length r over n angles (Zar 1999, eq. 27.4)."""
    R = r * n
    return float(np.exp(np.sqrt(1 + 4 * n + 4 * (n**2 - R**2)) - (1 + 2 * n)))


def kuiper_two(a, b):
    """Two-sample Kuiper test on angles in radians; V = D+ + D- of the two empirical
    distribution functions, p from the asymptotic Kuiper distribution (Kuiper 1960; the
    paper cites it). Returns (V, scaled statistic, p)."""
    a = np.sort(np.mod(a, 2 * np.pi))
    b = np.sort(np.mod(b, 2 * np.pi))
    allv = np.concatenate([a, b])
    fa = np.searchsorted(a, allv, side="right") / len(a)
    fb = np.searchsorted(b, allv, side="right") / len(b)
    V = np.max(fa - fb) + np.max(fb - fa)
    ne = len(a) * len(b) / (len(a) + len(b))
    lam = (np.sqrt(ne) + 0.155 + 0.24 / np.sqrt(ne)) * V
    j = np.arange(1, 101)
    p = float(np.sum(2 * (4 * j**2 * lam**2 - 1) * np.exp(-2 * j**2 * lam**2)))
    return float(V), float(lam), float(min(max(p, 0.0), 1.0))


# ---------------------------------------------------------------- ANOVA

def rm_anova(Y):
    """One-way repeated-measures ANOVA on an (n subjects x k conditions) array, with Mauchly's
    test and the Greenhouse-Geisser correction applied when Mauchly's test has p < 0.05
    (STAR Methods, Statistics). Rows with a missing value are dropped."""
    Y = np.asarray(Y, float)
    Y = Y[~np.isnan(Y).any(axis=1)]
    n, k = Y.shape
    gm = Y.mean()
    ss_c = n * np.sum((Y.mean(0) - gm) ** 2)
    ss_s = k * np.sum((Y.mean(1) - gm) ** 2)
    ss_e = np.sum((Y - gm) ** 2) - ss_c - ss_s
    df1, df2 = k - 1, (n - 1) * (k - 1)
    F = (ss_c / df1) / (ss_e / df2)
    S = np.cov(Y, rowvar=False)
    # orthonormal contrasts (Helmert)
    C = np.zeros((k, k - 1))
    for j in range(1, k):
        C[:j, j - 1] = 1.0
        C[j, j - 1] = -j
        C[:, j - 1] /= np.linalg.norm(C[:, j - 1])
    St = C.T @ S @ C
    p_ = k - 1
    eps = np.trace(St) ** 2 / (p_ * np.sum(St**2))
    if k > 2:
        W = np.linalg.det(St) / (np.trace(St) / p_) ** p_
        chi = -(n - 1 - (2 * p_**2 + p_ + 2) / (6 * p_)) * np.log(W)
        dfm = p_ * (p_ + 1) / 2 - 1
        pm = float(stats.chi2.sf(chi, dfm))
    else:
        W, pm = 1.0, 1.0
    gg = pm < 0.05
    e = eps if gg else 1.0
    p = float(stats.f.sf(F, df1 * e, df2 * e))
    return dict(F=float(F), df1=df1 * e, df2=df2 * e, p=p, n=n, mauchly_p=pm, gg_eps=float(eps), gg_applied=gg,
                means=Y.mean(0))


def tukey(values: dict):
    """Tukey-Kramer HSD over groups (statsmodels), a standard implementation of the paper's
    post hoc test (STAR Methods, Statistics)."""
    from statsmodels.stats.multicomp import pairwise_tukeyhsd
    lab = np.concatenate([[k] * len(v) for k, v in values.items()])
    val = np.concatenate([np.asarray(v, float) for v in values.values()])
    ok = ~np.isnan(val)
    res = pairwise_tukeyhsd(val[ok], lab[ok])
    df = pd.DataFrame(res.summary().data[1:], columns=res.summary().data[0])
    return df


def fmt_anova(a):
    return (f"F({a['df1']:.2f}, {a['df2']:.2f}) = {a['F']:.2f}, p = {a['p']:.3g}, n = {a['n']}, "
            f"Mauchly p = {a['mauchly_p']:.3g}, GG applied = {a['gg_applied']} (eps {a['gg_eps']:.2f})")


# ---------------------------------------------------------------- decoding

def window_dirs(d_deg, nsamp):
    """Circular mean direction of each window of ``nsamp`` samples, nan when none is valid
    (HD_Max_likelihood.py; the paper's code bins such windows at 0 degrees, which is taken here
    as a defect and not copied)."""
    nw = len(d_deg) // nsamp
    dd = np.radians(d_deg[: nw * nsamp]).reshape(nw, nsamp)
    v = np.nansum(np.exp(1j * dd), axis=1)
    allnan = np.isnan(dd).all(axis=1)
    ang = np.degrees(np.angle(v)) % 360
    ang[allnan | (np.abs(v) == 0)] = np.nan
    return ang


def window_counts(spk_i, n_samples, nsamp):
    nw = n_samples // nsamp
    w = spk_i // nsamp
    return np.bincount(w[w < nw], minlength=nw)


def fit_poisson_tuning(counts, wdir, nbins=36):
    """Mean spike count per window at each direction bin, fitted on the training trial
    (HD_Max_likelihood.py: spikes in windows at the bin over the number of such windows)."""
    b = bin_index(wdir, nbins)
    ok = b >= 0
    nwin = np.bincount(b[ok], minlength=nbins).astype(float)
    lam = np.zeros((counts.shape[0], nbins))
    for c in range(counts.shape[0]):
        s = np.bincount(b[ok], weights=counts[c, ok], minlength=nbins)
        lam[c] = np.where(nwin > 0, s / np.maximum(nwin, 1), 0.0)
    return lam


def decode(lam, counts, nbins=36):
    """Maximum likelihood direction per window from summed Poisson log likelihoods; windows in
    which no cell spiked are left undecoded (nan). A zero rate with a non-zero count is given
    log likelihood -10, as in HD_Max_likelihood.py."""
    from scipy.special import gammaln
    n = counts.T[:, :, None]  # windows x cells x 1
    L = lam[None, :, :]  # 1 x cells x bins
    with np.errstate(divide="ignore", invalid="ignore"):
        ll = n * np.log(L) - L - gammaln(n + 1)
    ll = np.where((L == 0) & (n > 0), -10.0, ll)
    ll = np.where((L == 0) & (n == 0), 0.0, ll)
    tot = ll.sum(axis=1)
    # bin start, as the code's angs 0..350; against window directions that fall anywhere in the
    # bin this biases the signed error by about -5 degrees (half a bin), kept to follow the code
    est = np.argmax(tot, axis=1) * (360 / nbins)
    est = est.astype(float)
    est[counts.sum(axis=0) == 0] = np.nan
    return est


def signed_err(est, true):
    """Decoded minus actual direction, wrapped to -180..180 degrees."""
    return (np.asarray(est) - np.asarray(true) + 180) % 360 - 180


# ---------------------------------------------------------------- momentary directional information

def idir_series(counts, dbin, ref_counts=None, ref_dbin=None, nbins=36, nmax=None):
    """Idir per interval: |p(n|d) log2(p(n|d)/p(n))| for the observed count n and direction
    bin d (STAR Methods, Estimating momentary directional information). The probabilities are
    estimated from (ref_counts, ref_dbin), the trial itself when they are not given. Intervals
    without a valid direction, or with a count or direction never seen in the reference, are nan.
    """
    if ref_counts is None:
        ref_counts, ref_dbin = counts, dbin
    nmax = int(max(counts.max(), ref_counts.max())) + 1 if nmax is None else nmax
    ok = ref_dbin >= 0
    joint = np.zeros((nbins, nmax))
    np.add.at(joint, (ref_dbin[ok], np.minimum(ref_counts[ok], nmax - 1)), 1)
    pd_ = joint.sum(1, keepdims=True)
    with np.errstate(invalid="ignore", divide="ignore"):
        pnd = joint / pd_
        pn = joint.sum(0) / joint.sum()
    out = np.full(len(counts), np.nan)
    v = dbin >= 0
    nn = np.minimum(counts[v], nmax - 1)
    a = pnd[dbin[v], nn]
    b = pn[nn]
    with np.errstate(invalid="ignore", divide="ignore"):
        val = np.abs(a * np.log2(a / b))
    val[(a == 0) | ~np.isfinite(val)] = np.nan
    out[v] = val
    return out


# ---------------------------------------------------------------- internally referenced tuning

def bin_cum(t, d):
    """Sorted times, and cumulative counts per 10 degree direction bin and of time, of a set of
    events (cell 2 spikes or tracker samples), for internal_tuning."""
    o = np.argsort(t)
    t, d = t[o], d[o]
    b = np.floor(d / 10).astype(int) % 36
    cum = np.zeros((len(t) + 1, 36))
    cum[1:] = np.cumsum(np.eye(36)[b], axis=0)
    ct = np.concatenate([[0.0], np.cumsum(t)])
    return t, cum, ct


def _shift(C):
    """From C[b1, b2] (counts of cell 1 bin b1 against event bin b2) to the histogram of the
    displacement bin k = (b1 - b2 + 18) mod 36; bin k is (k - 18) * 10 degrees."""
    h = np.zeros(36)
    b1, b2 = np.meshgrid(np.arange(36), np.arange(36), indexing="ij")
    np.add.at(h, (b1 - b2 + 18) % 36, C)
    return h


def internal_tuning(t1, d1, ev2, evs, maxint, side="before", norm="sum_offsets"):
    """Internally referenced directional tuning of cell 2 on cell 1 (STAR Methods, Estimating
    internally referenced head direction; Spike_triggered_FR_curve.py).

    For each cell 1 spike (time t1, direction d1), the displacement d1 - d2 for each cell 2
    spike within ``maxint`` s, in 36 bins of 10 degrees between direction bins. ``ev2`` and
    ``evs`` are bin_cum of the cell 2 spikes and of the tracker samples. ``side``: 'before'
    takes cell 2 spikes in the window ending at the cell 1 spike (the code), 'after' the window
    starting at it (variant). ``norm``: 'sum_offsets' divides the histogram by the sum of the
    absolute time offsets (the Methods' "divided by the sum of the time offsets", one scale
    factor per curve, so the KLD, which is computed on the counts, the preferred bin and the
    Rayleigh length are those of the raw displacement histogram), 'occupancy' divides each bin by
    the count of the same displacement over all tracker samples of the windows (the code's
    rate_tunes), 'none' returns the histogram itself (used with tracker samples in place of cell 2
    spikes, to give the displacement histogram of head direction alone). Spikes and samples without a
    valid direction are dropped beforehand. Returns (curve, histogram of counts).
    """
    t2, cum2, ct2 = ev2

    def window(t):
        if side == "before":
            return np.searchsorted(t, t1 - maxint, "left"), np.searchsorted(t, t1, "left")
        return np.searchsorted(t, t1, "right"), np.searchsorted(t, t1 + maxint, "right")

    b1 = np.floor(d1 / 10).astype(int) % 36
    onehot = np.eye(36)[b1]
    lo, hi = window(t2)
    hist = _shift(onehot.T @ (cum2[hi] - cum2[lo]))
    if norm == "none":
        return hist, hist
    if norm == "sum_offsets":
        n = hi - lo
        s = np.sum(np.abs((ct2[hi] - ct2[lo]) - n * t1))
        return (hist / s if s > 0 else hist), hist
    ts, cums, _ = evs
    slo, shi = window(ts)
    occ = _shift(onehot.T @ (cums[shi] - cums[slo]))
    with np.errstate(invalid="ignore", divide="ignore"):
        curve = np.where(occ > 0, hist / occ, 0.0)
    return curve, hist


def disp_centers():
    """Centres of the displacement bins of internal_tuning, in radians."""
    return np.radians((np.arange(36) - 18) * 10 + 5)


def tukey_rm(Y, labels):
    """Tukey HSD with the error term of the repeated-measures ANOVA, (n x k) array: q = mean
    difference / sqrt(MS_error / n), df = (n - 1)(k - 1), p from the studentized range. This is
    the post hoc test that follows a repeated-measures ANOVA (STAR Methods, Statistics, "Post hoc
    Tukey-Kramer HSD tests"); the between-groups Tukey (tukey) is shown as a variant."""
    Y = np.asarray(Y, float)
    Y = Y[~np.isnan(Y).any(axis=1)]
    n, k = Y.shape
    gm = Y.mean()
    ss_e = (np.sum((Y - gm) ** 2) - n * np.sum((Y.mean(0) - gm) ** 2) - k * np.sum((Y.mean(1) - gm) ** 2))
    dfe = (n - 1) * (k - 1)
    se = np.sqrt(ss_e / dfe / n)
    rows = []
    m = Y.mean(0)
    for i in range(k):
        for j in range(i + 1, k):
            q = abs(m[j] - m[i]) / se
            rows.append(dict(group1=labels[i], group2=labels[j], meandiff=m[j] - m[i],
                             p=float(stats.studentized_range.sf(q, k, dfe))))
    return pd.DataFrame(rows)
