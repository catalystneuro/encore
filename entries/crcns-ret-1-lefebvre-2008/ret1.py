"""Loading and measures for CRCNS data set ret-1 (doi:10.6080/K0RF5RZT).

Lefebvre, Zhang, Meister, Wang & Sanes (2008), Development 135:4141-4151,
doi:10.1242/dev.027912, Figure 9.

The data set is one zip file in the public S3 bucket `crcnsarchive`. It holds one MATLAB file per
retina (16), each with `datainfo` (date, genotype label in `animal`, number of cells), `spikes`
(cells by stimuli, spike times in s) and `stimulus` (one entry per recording: binary white noise
with its onset, frame length, number of frames, pixel size of 8.3 um and the size of its tiles),
and `ran1.bin`, the bits of the RAN1 generator with seed -10000 from which every stimulus is drawn
(the seed every recording states). The zip is opened in place over range requests and members are
read into memory; nothing is written to disk. CRCNS data sets are not versioned; `VERSION` is
"unversioned" and `ZIP_MD5` is the sum the data set's `checksums.md5` gives for the zip.

Where the parameters come from:

- Stimulus reconstruction follows the data set's own `Analysis_example.m`: frame k of a recording
  spans [onset + k frame, onset + (k+1) frame), Nframes - 1 frames are used, the first
  `m = (x/dx)(y/dy)` bits of `ran1.bin` are the tiles of frame 1, the next m those of frame 2, and
  so on, bit 1 is light (+1) and 0 dark (-1). Bits are read least significant first, as MATLAB's
  `fread(..., '*ubit1')` does; the notebook checks this against RAN1 itself.
- The spike-triggered average (Eqn 1 of the paper) subtracts each bar's time average and averages
  over all spikes of the cell. Its length in time, 0.5 s (30 frames), is the claim's standard
  choice (fig9d-rf-size-similar); the data set's example script uses the same window. Spikes in the
  first 29 frames, which lack a full stimulus history, are left out, as the example script does
  (a standard choice that cannot change a result).
- The separation h(x, t) = b(x) a(t) (Eqn 2) has the two readings of fig9d-rf-size-similar:
  "svd", the leading singular vectors, and "peak", h at the time and at the bar of its largest
  absolute value.
- Centre size is the full width at half maximum of |b(x)| around its peak, with linear
  interpolation between bars (fig9d-rf-size-similar; the interpolation is its standard choice).
- Time to peak is the time of the extremum of a(t) of largest absolute value (fig9e), at frame
  resolution or with parabolic interpolation. Lag j (stimulus j frames before the frame of the
  spike) is placed at (j + 0.5) frames, the convention of the example script; a constant offset
  that is the same for every cell and cannot change a comparison.
- The Linear-Nonlinear model (Eqn 3) and its fits follow fig9g-threshold-unaltered: generator
  y = stimulus filtered by h, scaled to unit variance; N(y) = B below theta and B + G y
  ("printed") or B + G (y - theta) ("continuous") above; least squares against the rate in bins of
  one frame ("frame") or against the mean rate in 20 bins of y of equal count ("binned"). Theta is
  searched on a grid of quantiles of y (a standard choice of resolution).
- The 95% bands of the cumulative histograms have the three readings of the claims file's header:
  "binomial" (pointwise, normal approximation), "dkw" (Dvoretzky-Kiefer-Wolfowitz) and
  "bootstrap" (pointwise percentile bootstrap over cells, 1000 resamples, a standard number).
"""

from __future__ import annotations

import io
import zipfile

import fsspec
import numpy as np
import scipy.io as sio

ARCHIVE = "crcns"
DATASET_ID = "ret-1"
DATASET_DOI = "10.6080/K0RF5RZT"
VERSION = "unversioned"
BASE_URL = "https://crcnsarchive.s3-us-west-2.amazonaws.com/ret-1/"
ZIP_NAME = "crcns_ret-1.zip"
ZIP_MD5 = "4b9390ddc51c72d6f66563cb02e48fe8"   # from the data set's checksums.md5
ZIP_SIZE = 71871914
PREFIX = "crcns_ret-1/"

STA_FRAMES = 30          # 0.5 s window, fig9d-rf-size-similar (standard choice)
LN_BINS = 20             # fig9g-threshold-unaltered, reading (b)
THETA_GRID = 101         # quantiles of y searched for theta (standard choice of resolution)
BOOTSTRAP = 1000         # resamples for the bootstrap band (standard choice)


# --- loading -------------------------------------------------------------------

def open_zip() -> zipfile.ZipFile:
    """The data set's zip, opened in place over HTTP range requests."""
    f = fsspec.open(BASE_URL + ZIP_NAME, block_size=2**20).open()
    return zipfile.ZipFile(f)


def read_text(name: str) -> str:
    """A small text file at the top of the data set (checksums.md5, filelist.txt)."""
    with fsspec.open(BASE_URL + name, "rt") as f:
        return f.read()


def ran1_bits(z: zipfile.ZipFile, nbits: int) -> np.ndarray:
    """The first nbits of ran1.bin as booleans, least significant bit of each byte first."""
    nbytes = (nbits + 7) // 8
    with z.open(PREFIX + "ran1.bin") as f:
        raw = np.frombuffer(f.read(nbytes), dtype=np.uint8)
    return np.unpackbits(raw, bitorder="little")[:nbits].astype(bool)


def ran1(seed: int, n: int) -> np.ndarray:
    """n uniform numbers from RAN1 (Numerical Recipes 2nd ed.), as the data set's ran1.m."""
    IA, IM, IQ, IR, NTAB = 16807, 2147483647, 127773, 2836, 32
    NDIV = 1 + (IM - 1) // NTAB
    iv = [0] * NTAB
    s = -seed if seed < -1 else 1
    for j in range(NTAB + 8, 0, -1):
        k = s // IQ
        s = IA * (s - k * IQ) - IR * k
        if s < 0:
            s += IM
        if j <= NTAB:
            iv[j - 1] = s
    iy = iv[0]
    out = np.empty(n)
    for i in range(n):
        k = s // IQ
        s = IA * (s - k * IQ) - IR * k
        if s < 0:
            s += IM
        j = iy // NDIV
        iy = iv[j]
        iv[j] = s
        out[i] = min(iy / IM, 1.0 - 1.2e-7)
    return out


def _cellstr(x):
    return [np.atleast_1d(np.asarray(v, dtype=float)).ravel() for v in np.atleast_1d(x)]


def load_retinas(z: zipfile.ZipFile) -> list[dict]:
    """Every retina file: its info, its recordings and the spike times of each cell in each."""
    names = sorted(n for n in z.namelist() if n.startswith(PREFIX + "Data/") and n.endswith(".mat"))
    out = []
    for name in names:
        m = sio.loadmat(io.BytesIO(z.read(name)), squeeze_me=True, struct_as_record=False)
        di = m["datainfo"]
        stims = list(np.atleast_1d(m["stimulus"]))
        sp = m["spikes"]
        ncell = int(di.Ncell)
        sp = np.asarray(sp, dtype=object).reshape(ncell, len(stims)) if len(stims) > 1 or ncell > 1 else None
        if sp is None:
            sp = np.empty((1, 1), dtype=object)
            sp[0, 0] = m["spikes"]
        recs = []
        for i, s in enumerate(stims):
            p = s.param
            recs.append({
                "index": i, "type": str(s.type), "onset": float(s.onset), "frame": float(s.frame),
                "nframes": int(s.Nframes), "pixelsize": float(s.pixelsize),
                "x": int(p.x), "y": int(p.y), "dx": int(p.dx), "dy": int(p.dy), "seed": int(p.seed),
                "rec_no": int(np.atleast_1d(di.RecNo)[i]),
                "start": tuple(int(v) for v in np.atleast_2d(di.RecStartTime)[i]),
                "spikes": [np.atleast_1d(np.asarray(sp[c, i], dtype=float)).ravel() for c in range(ncell)],
            })
        out.append({
            "file": name.rsplit("/", 1)[-1], "retina": name.rsplit("/", 1)[-1][:-4],
            "date": str(di.date), "sample": int(di.SmplNo), "ncell": ncell, "animal": str(di.animal),
            "experimenter": str(di.experimenter), "description": str(di.description), "recordings": recs,
        })
    return out


def kind(rec: dict) -> str:
    """'vbars' (vertical bars, full height), 'hbars' (horizontal bars, full width) or 'checker'."""
    if rec["dy"] == rec["y"] and rec["dx"] < rec["x"]:
        return "vbars"
    if rec["dx"] == rec["x"] and rec["dy"] < rec["y"]:
        return "hbars"
    return "checker"


def bar_width_um(rec: dict) -> float:
    return (rec["dx"] if kind(rec) == "vbars" else rec["dy"]) * rec["pixelsize"]


def group(animal: str) -> str:
    """'mutant' for the KO labels without Bax, 'control' for WT, 'bax' for the KO on Bax -/-."""
    if animal.startswith("KO") and "bax" in animal:
        return "bax"
    if animal.startswith("KO"):
        return "mutant"
    if animal.startswith("WT"):
        return "control"
    return "unknown"


# --- stimulus and spikes ---------------------------------------------------------

def stimulus(rec: dict, bits: np.ndarray) -> np.ndarray:
    """The tiles by frames matrix (+1 light, -1 dark), float32, for frames 0 .. Nframes-2."""
    m = (rec["x"] // rec["dx"]) * (rec["y"] // rec["dy"])
    n = rec["nframes"] - 1
    s = bits[: m * n].reshape(n, m).T
    return np.where(s, np.float32(1), np.float32(-1))


def frame_edges(rec: dict) -> np.ndarray:
    return rec["onset"] + np.arange(rec["nframes"]) * rec["frame"]


def counts(rec: dict) -> np.ndarray:
    """Spike counts per frame (frames by cells), frames 0 .. Nframes-2, as the example script."""
    edges = frame_edges(rec)
    return np.stack([np.histogram(t, edges)[0] for t in rec["spikes"]], axis=1).astype(np.float32)


def sta(S: np.ndarray, C: np.ndarray, nlag: int = STA_FRAMES) -> tuple[np.ndarray, np.ndarray]:
    """Spike-triggered averages, cells by tiles by lags, and the spikes used per cell.

    Lag j is the stimulus j frames before the frame of the spike. Spikes in the first nlag - 1
    frames are left out. Each tile's time average is subtracted from the stimulus.
    """
    S = S - S.mean(axis=1, keepdims=True)
    C = C.copy()
    C[: nlag - 1] = 0
    n = C.sum(axis=0)
    N = S.shape[1]
    h = np.empty((C.shape[1], S.shape[0], nlag), dtype=np.float64)
    for j in range(nlag):
        h[:, :, j] = (S[:, : N - j] @ C[j:]).T
    with np.errstate(invalid="ignore", divide="ignore"):
        h /= n[:, None, None]
    return h, n


def separate(h: np.ndarray, reading: str) -> tuple[np.ndarray, np.ndarray]:
    """b(x) and a(t) from h (tiles by lags), reading 'svd' or 'peak'."""
    if not np.all(np.isfinite(h)) or not np.any(h):
        return np.full(h.shape[0], np.nan), np.full(h.shape[1], np.nan)
    if reading == "svd":
        u, s, vt = np.linalg.svd(h, full_matrices=False)
        b, a = u[:, 0] * s[0], vt[0]
        # orient so that the extremum of a is positive; b then carries the sign of the centre
        if a[np.argmax(np.abs(a))] < 0:
            a, b = -a, -b
        return b, a
    if reading == "peak":
        x0, t0 = np.unravel_index(np.argmax(np.abs(h)), h.shape)
        return h[:, t0].copy(), h[x0, :].copy()
    raise ValueError(reading)


def fwhm(b: np.ndarray, width_um: float) -> float:
    """Full width at half maximum of |b| around its peak, in um, linear interpolation between bars."""
    if not np.all(np.isfinite(b)):
        return np.nan
    v = np.abs(b)
    i0 = int(np.argmax(v))
    half = v[i0] / 2
    left = i0
    while left > 0 and v[left - 1] >= half:
        left -= 1
    right = i0
    while right < len(v) - 1 and v[right + 1] >= half:
        right += 1
    # interpolate the crossings; at an edge of the stimulus the width stops there
    xl = left - (v[left] - half) / (v[left] - v[left - 1]) if left > 0 else float(left)
    xr = right + (v[right] - half) / (v[right] - v[right + 1]) if right < len(v) - 1 else float(right)
    return (xr - xl) * width_um


def time_to_peak(a: np.ndarray, frame: float, reading: str) -> float:
    """Time (s) of the extremum of a(t) of largest absolute value; 'frame' or 'parabolic'."""
    if not np.all(np.isfinite(a)):
        return np.nan
    j = int(np.argmax(np.abs(a)))
    off = 0.0
    if reading == "parabolic" and 0 < j < len(a) - 1:
        y0, y1, y2 = np.sign(a[j]) * a[j - 1 : j + 2]
        den = y0 - 2 * y1 + y2
        if den != 0:
            off = 0.5 * (y0 - y2) / den
    elif reading not in ("frame", "parabolic"):
        raise ValueError(reading)
    return (j + off + 0.5) * frame


def surround(b: np.ndarray, frac: float) -> bool:
    """A lobe of sign opposite to the centre peak on both flanks, deeper than frac of the peak."""
    if not np.all(np.isfinite(b)):
        return False
    i0 = int(np.argmax(np.abs(b)))
    c = np.sign(b[i0]) * b / np.abs(b[i0])
    if i0 == 0 or i0 == len(b) - 1:
        return False
    return bool(c[:i0].min() < -frac and c[i0 + 1 :].min() < -frac)


def generator(S: np.ndarray, h: np.ndarray) -> np.ndarray:
    """y(t) = sum over tiles and lags of h(x, j) s(x, t - j), cells by frames; NaN for t < nlag - 1."""
    S = S - S.mean(axis=1, keepdims=True)
    ncell, m, nlag = h.shape
    N = S.shape[1]
    y = np.zeros((ncell, N), dtype=np.float64)
    for j in range(nlag):
        y[:, j:] += h[:, :, j].astype(np.float32) @ S[:, : N - j]
    y[:, : nlag - 1] = np.nan
    return y


def fit_ln(y: np.ndarray, rate: np.ndarray, fit: str, form: str) -> dict:
    """Fit N(y) to the rate (Hz); y is scaled here to unit variance (Z of Eqn 3)."""
    ok = np.isfinite(y)
    y, r = y[ok], rate[ok]
    sd = y.std()
    if not np.isfinite(sd) or sd == 0:
        return {"B": np.nan, "G": np.nan, "theta": np.nan, "sse": np.nan}
    y = y / sd
    order = np.argsort(y, kind="stable")
    y, r = y[order], r[order].astype(float)
    if fit == "binned":
        chunks = np.array_split(np.arange(len(y)), LN_BINS)
        y = np.array([y[c].mean() for c in chunks])
        r = np.array([r[c].mean() for c in chunks])
        grid = (y[1:] + y[:-1]) / 2      # every split between the 20 bin centres
    elif fit == "frame":
        grid = np.quantile(y, np.linspace(0.0, 1.0, THETA_GRID)[1:-1])
    else:
        raise ValueError(fit)
    n = len(y)
    # sums over the points at or above each theta, from cumulative sums of the sorted values
    k0 = np.searchsorted(y, grid, side="left")
    def tail(v):
        c = np.concatenate([[0.0], np.cumsum(v[::-1])])[::-1]
        return c[k0]
    k = n - k0
    Sy, Syy, Sr_a, Syr = tail(y), tail(y * y), tail(r), tail(y * r)
    Sr, Srr = r.sum(), (r * r).sum()
    if form == "printed":
        Sg, Sgg, Sgr = Sy, Syy, Syr
    elif form == "continuous":
        Sg = Sy - grid * k
        Sgg = Syy - 2 * grid * Sy + grid ** 2 * k
        Sgr = Syr - grid * Sr_a
    else:
        raise ValueError(form)
    det = n * Sgg - Sg ** 2
    with np.errstate(invalid="ignore", divide="ignore"):
        B = (Sgg * Sr - Sg * Sgr) / det
        G = (n * Sgr - Sg * Sr) / det
    sse = Srr - B * Sr - G * Sgr
    sse = np.where(np.abs(det) > 1e-12 * max(1.0, n * n), sse, np.inf)
    i = int(np.argmin(sse))
    return {"B": float(B[i]), "G": float(G[i]), "theta": float(grid[i]), "sse": float(sse[i])}


# --- recordings and per-cell measures --------------------------------------------

READINGS = ("A", "B", "C")


def bar_recordings(retina: dict, reading: str) -> list[dict]:
    """The flickering-bar recordings of 8.3 or 16.6 um used for a retina under a reading.

    A: the first vertical-bar recording; B: all vertical-bar recordings, pooled; C: the
    horizontal-bar recording where there is one, otherwise as A. The readings are those of the
    criterion of fig9d-rf-size-similar, added after questions/crcns-ret-1.yaml was answered; under
    B the spikes and frames of the recordings are pooled.
    """
    ok = [r for r in retina["recordings"] if kind(r) != "checker" and round(bar_width_um(r), 1) in (8.3, 16.6)]
    vb = [r for r in ok if kind(r) == "vbars"]
    hb = [r for r in ok if kind(r) == "hbars"]
    if reading == "A":
        return vb[:1]
    if reading == "B":
        return vb
    if reading == "C":
        return hb[:1] if hb else vb[:1]
    raise ValueError(reading)


def split_trains(rec: dict) -> list[tuple[np.ndarray, np.ndarray]]:
    """Each train as (head, tail): the spikes up to the first decrease of time, and the rest."""
    out = []
    for t in rec["spikes"]:
        i = np.where(np.diff(t) < 0)[0]
        out.append((t[: i[0] + 1], t[i[0] + 1 :]) if len(i) else (t, t[:0]))
    return out


def with_tail_shift(rec: dict, offset: float) -> dict:
    """A copy of the recording whose trailing out-of-order segments are moved by offset seconds."""
    r = dict(rec)
    r["spikes"] = [np.concatenate([h, tl + offset]) for h, tl in split_trains(rec)]
    return r


def in_window(rec: dict, t: np.ndarray) -> int:
    return int(np.sum((t >= rec["onset"]) & (t < rec["onset"] + rec["nframes"] * rec["frame"])))


def measure_retina(retina: dict, recs: list[dict], bits: np.ndarray, ln: bool = True) -> list[dict]:
    """Every per-cell measure of the claims, from the recordings given (pooled when several).

    Returns one dict per cell: spikes used, firing rate, the ratio of the STA's peak to that of a
    null STA (spike counts circularly shifted by half the recording), FWHM, time to peak and
    surround under each separation, LN parameters under each fit and form, and b(x) and a(t) of
    the null STA's separation for reference.
    """
    if not recs:
        return []
    ncell = retina["ncell"]
    hs, ns, nulls, data = [], [], [], []
    spikes = np.zeros(ncell)
    duration = 0.0
    for rec in recs:
        S = stimulus(rec, bits)
        C = counts(rec)
        h, n = sta(S, C)
        hn, _ = sta(S, np.roll(C, C.shape[0] // 2, axis=0))
        hs.append(h * n[:, None, None])
        nulls.append(hn * n[:, None, None])
        ns.append(n)
        spikes += [in_window(rec, t) for t in rec["spikes"]]
        duration += rec["nframes"] * rec["frame"]
        data.append((S, C) if ln else None)
    n = np.sum(ns, axis=0)
    with np.errstate(invalid="ignore", divide="ignore"):
        h = np.sum(hs, axis=0) / n[:, None, None]
        hn = np.sum(nulls, axis=0) / n[:, None, None]
    width = bar_width_um(recs[0])
    frame = recs[0]["frame"]
    out = []
    ys = [generator(S, np.nan_to_num(h)) for S, _ in data] if ln else None
    for c in range(ncell):
        d = {"retina": retina["retina"], "animal": retina["animal"], "group": group(retina["animal"]),
             "cell": c, "recordings": "+".join(str(r["index"]) for r in recs), "kind": kind(recs[0]),
             "bar_um": round(width, 1), "spikes_sta": float(n[c]), "rate_hz": spikes[c] / duration}
        pk, pn = np.nanmax(np.abs(h[c])) if n[c] else np.nan, np.nanmax(np.abs(hn[c])) if n[c] else np.nan
        d["peak_ratio"] = pk / pn if n[c] else np.nan
        for sep in ("svd", "peak"):
            b, a = separate(h[c], sep)
            bn, _ = separate(hn[c], sep)
            d[f"fwhm_{sep}"] = fwhm(b, width)
            for pr in ("frame", "parabolic"):
                d[f"ttp_{sep}_{pr}"] = time_to_peak(a, frame, pr)
            for frac in (0.1, 0.2):
                d[f"surround_{sep}_{int(frac * 100)}"] = surround(b, frac)
                d[f"null_surround_{sep}_{int(frac * 100)}"] = surround(bn, frac)
        if ln:
            y = np.concatenate([yy[c] for yy in ys])
            r = np.concatenate([C[:, c] / rec["frame"] for (_, C), rec in zip(data, recs)])
            for fit in ("frame", "binned"):
                for form in ("printed", "continuous"):
                    p = fit_ln(y, r, fit, form) if n[c] else {"B": np.nan, "G": np.nan, "theta": np.nan}
                    d[f"theta_{fit}_{form}"] = p["theta"]
                    d[f"gain_{fit}_{form}"] = p["G"]
                    d[f"base_{fit}_{form}"] = p["B"]
        out.append(d)
    return out


def duplicate_pairs(rec: dict, tol: float = 0.0005, frac: float = 0.5) -> list[tuple[int, int, float]]:
    """Pairs of units in a recording where more than frac of the smaller train has a spike of the
    other within tol seconds (a standard check for one neuron sorted twice)."""
    sp = [np.sort(t) for t in rec["spikes"]]
    out = []
    for a in range(len(sp)):
        for b in range(a + 1, len(sp)):
            x, y = sp[a], sp[b]
            if len(x) == 0 or len(y) == 0:
                continue
            s, l = (x, y) if len(x) <= len(y) else (y, x)
            i = np.clip(np.searchsorted(l, s), 1, len(l) - 1)
            d = np.minimum(np.abs(l[i] - s), np.abs(l[i - 1] - s))
            f = float((d < tol).mean())
            if f > frac:
                out.append((a, b, f))
    return out


# --- cumulative histograms and their bands ---------------------------------------

def ecdf(values: np.ndarray, grid: np.ndarray) -> np.ndarray:
    v = np.sort(values)
    return np.searchsorted(v, grid, side="right") / len(v)


def band(values: np.ndarray, grid: np.ndarray, reading: str, rng=None) -> tuple[np.ndarray, np.ndarray]:
    """Lower and upper 95% band of the cumulative histogram of values, evaluated on grid."""
    v = np.asarray(values, dtype=float)
    v = v[np.isfinite(v)]
    n = len(v)
    F = ecdf(v, grid)
    if reading == "binomial":
        e = 1.96 * np.sqrt(F * (1 - F) / n)
        lo, hi = F - e, F + e
    elif reading == "dkw":
        e = np.sqrt(np.log(2 / 0.05) / (2 * n))
        lo, hi = F - e, F + e
    elif reading == "bootstrap":
        rng = rng if rng is not None else np.random.default_rng(0)
        boots = np.empty((BOOTSTRAP, len(grid)))
        for i in range(BOOTSTRAP):
            boots[i] = ecdf(rng.choice(v, n, replace=True), grid)
        lo, hi = np.percentile(boots, [2.5, 97.5], axis=0)
    else:
        raise ValueError(reading)
    return np.clip(lo, 0, 1), np.clip(hi, 0, 1)


def compare_bands(mutant: np.ndarray, control: np.ndarray, reading: str, rng=None) -> dict:
    """Whether the two 95% bands separate anywhere, where, and which curve lies to the right.

    The grid is every observed value of either group. 'mutant_right' counts grid points where the
    mutant band lies wholly below the control band (mutant values larger); 'mutant_left' the
    reverse.
    """
    mutant = np.asarray(mutant, float)
    control = np.asarray(control, float)
    mutant, control = mutant[np.isfinite(mutant)], control[np.isfinite(control)]
    grid = np.unique(np.concatenate([mutant, control]))
    lm, hm = band(mutant, grid, reading, rng)
    lc, hc = band(control, grid, reading, rng)
    right = hm < lc
    left = hc < lm
    sep = right | left
    return {
        "reading": reading, "n_mutant": len(mutant), "n_control": len(control),
        "separate": bool(sep.any()), "points_separate": int(sep.sum()), "points": len(grid),
        "mutant_right": int(right.sum()), "mutant_left": int(left.sum()),
        "range": (float(grid[sep].min()), float(grid[sep].max())) if sep.any() else None,
    }
