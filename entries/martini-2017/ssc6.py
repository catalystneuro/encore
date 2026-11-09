"""Loading and measures for CRCNS ssc-6 (Martini, Molano-Mazon and Maravall 2017).

The data set is one gzipped tar file, ``ssc-6/live/data.tar.gz`` (8.06 GB), in
the public S3 bucket ``crcnsarchive``. It holds, for ten mice (``data/exp1`` to
``data/exp10``), the raw 2-photon movies of each field of view (``movies/gaborF_R.tif``,
833 frames of 128 x 512 pixels, uint8) and one stimulus file per movie
(``stim/expF_000R.mat``, 950000 x 3 at 10 kHz: time, piezo command, frame
pulses), and for mice 8 to 10 a histology figure (``histology/figure.pdf``).
A gzipped tar cannot be read at random, so :func:`stream` reads it once, as a
stream over HTTP, and reduces each field to ROI traces as it goes; no file is
written to disk and at most the four movies of one field are held in memory.

Where each parameter comes from:

- Registration (``register_movie``): rigid, each frame to the first frame of its
  movie (Methods, 2-Photon Image Analysis, "For each movie, rigid
  transformation was performed using the first frame as reference"). The
  shift is found by phase correlation at whole-pixel precision, on frames
  smoothed with a Gaussian of 1 pixel: a standard choice. The four movies of a
  field are then aligned to the first by their mean images, so that one ROI set
  serves all four (claims file, open detail 1, "one ROI set on the mean of all
  four registered movies").
- ROIs (``detect_rois``): cells are found on the mean image of all frames
  (Methods, "cells were visualized using the mean image of all frames and cell
  contours outlined automatically"). Caltracer's detector and the manual
  supervision cannot be repeated; this is an assumption: somata are blobs found
  by a Laplacian-of-Gaussian filter of scale ``SOMA_SIGMA_UM`` on the mean image
  normalised by its local mean and spread, segmented by a watershed and kept
  when their area is that of a soma (``MIN_AREA_UM2`` to ``MAX_AREA_UM2``,
  equivalent diameters 6 to 16 um, the size of layer 2/3 somata). The values
  were fixed before any tuning or correlation was computed.
- Background from unstained blood vessels (Methods, citing Greenberg et al.
  2008): the mean, in each frame, of the pixels darkest in the field's mean
  image (lowest ``VESSEL_PERCENTILE`` percent, outside ROIs and halos); a
  standard choice, the paper does not say how the vessel ROI was drawn.
- Halo (Methods, "A perisomatic halo was drawn automatically ... scaled
  (optimal factor = 0.7) and subtracted"): factor 0.7 from the Methods; the
  ring from ``HALO_INNER_PX`` to ``HALO_OUTER_PX`` pixels outside the ROI,
  excluding every ROI, is a standard choice (open detail 1).
- dF/F0 (``dff``): F0 the 8th percentile of corrected fluorescence in a
  symmetric 6 s window (Methods), per movie, 6 s being 53 frames at 114.3 ms.
- Response amplitude (``responses``): the mean dF/F0 of the first 5 frames after
  a stimulus minus the mean of the last 3 frames before (Methods). The first
  frame after is the first whose pulse is at or after the command onset (claims
  file, open detail 2).
- Frame times: the frame pulses of the stimulus file's third column; the k-th
  pulse (the first is at t = 0) is the k-th frame. The file covers 832 of the
  833 frames; the last frame is never within 5 frames of a stimulus.
"""

import io
import re
import tarfile
from collections import defaultdict

import numpy as np
import scipy.io
import scipy.ndimage as ndi
from scipy import stats

# CRCNS data sets are not versioned (docs/archives.md): ssc-6, version "unversioned",
# doi:10.6080/K02F7KCP; data.tar.gz MD5 eb7382e21fe469614d288923ae760f7a (checksums.md5).
URL = "https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-6/live/data.tar.gz"
PX_PER_UM = 1.48          # Methods and data description
FRAME_S = 0.1143          # data description, 114 ms; frame pulses give 114.3 ms
SOMA_SIGMA_UM = 3.5       # assumption, see module docstring
MIN_AREA_UM2 = 28.0       # 6 um equivalent diameter
MAX_AREA_UM2 = 200.0      # 16 um equivalent diameter
HALO_INNER_PX = 2
HALO_OUTER_PX = 8
VESSEL_PERCENTILE = 2.0
HALO_FACTOR = 0.7         # Methods
F0_WINDOW = 53            # 6 s at 8.75 Hz, Methods
F0_PERCENTILE = 8         # Methods
N_AFTER, N_BEFORE = 5, 3  # Methods
N_NEUROPIL = 10           # Results, paragraph 4


# ---------------------------------------------------------------- streaming

def open_stream(url=URL):
    import fsspec
    f = fsspec.open(url, block_size=2**24).open()
    return tarfile.open(fileobj=f, mode="r|gz")


def stream(url=URL, mice=None, max_fields=None, log=print):
    """Read the tar once and return a dict with, per field, the ROI traces and,
    per stimulus file, the frame and deflection times.

    ``mice`` limits the mice processed (others are skipped as they pass), and
    ``max_fields`` stops after that many fields (to develop on a subset).
    """
    out = {"members": [], "fields": {}, "stims": {}, "histology": {}, "readme": {}}
    pending = defaultdict(dict)   # (mouse, field) -> {rep: movie}
    tf = open_stream(url)
    n_done = 0

    def flush(key):
        nonlocal n_done
        movies = pending.pop(key)
        out["fields"][key] = process_field(movies)
        n_done += 1
        log(f"field {key}: {len(movies)} movies, {len(out['fields'][key]['rois'])} ROIs")

    for m in tf:
        out["members"].append((m.name, m.size))
        if not m.isfile():
            continue
        mm = re.match(r"data/exp(\d+)/movies/gabor(\d+)_(\d+)\.tif$", m.name)
        ms = re.match(r"data/exp(\d+)/stim/exp(\d+)_000(\d+)\.mat$", m.name)
        mh = re.match(r"data/exp(\d+)/histology/(.+\.pdf)$", m.name)
        mouse = int((mm or ms or mh).group(1)) if (mm or ms or mh) else None
        if mice is not None and mouse is not None and mouse not in mice:
            continue
        if mm:
            key = (mouse, int(mm.group(2)))
            for k in [k for k in pending if k != key]:
                flush(k)
            if max_fields is not None and n_done >= max_fields:
                break
            pending[key][int(mm.group(3))] = read_movie(tf.extractfile(m).read())
        else:
            for k in list(pending):
                flush(k)
            if max_fields is not None and n_done >= max_fields and not ms:
                break
            if ms:
                raw = scipy.io.loadmat(io.BytesIO(tf.extractfile(m).read()))
                out["stims"][(mouse, int(ms.group(2)), int(ms.group(3)))] = parse_stim(raw["datastim"])
            elif mh:
                out["histology"][mouse] = describe_pdf(tf.extractfile(m).read())
            elif m.name.endswith(".txt"):
                out["readme"][m.name] = tf.extractfile(m).read().decode("latin-1")
    for k in list(pending):
        flush(k)
    return out


def read_movie(buf):
    import tifffile
    with tifffile.TiffFile(io.BytesIO(buf)) as t:
        return t.asarray()


def describe_pdf(buf):
    """What a histology PDF holds: pages, images, text, and a small rendering."""
    import pymupdf
    d = pymupdf.open(stream=buf, filetype="pdf")
    pages = []
    for p in d:
        pix = p.get_pixmap(dpi=60)
        img = np.frombuffer(pix.samples, np.uint8).reshape(pix.height, pix.width, pix.n)
        pages.append({"size_pt": (p.rect.width, p.rect.height), "n_images": len(p.get_images()),
                      "text": p.get_text(), "render": img[..., :3].copy()})
    return {"n_pages": d.page_count, "creator": d.metadata.get("creator"), "pages": pages}


# ---------------------------------------------------------------- stimulus

def parse_stim(a):
    """Frame pulse times and deflections of one stimulus file.

    Deflections are runs of the command more than 0.01 V from its median (the
    resting level), joined across gaps under 0.2 s. A deflection is classed by
    shape: position (one positive lobe), velocity (positive then negative lobe
    of equal size) or acceleration (a negative lobe larger than the positive
    ones), as the filters of Figure 1B; its amplitude is its largest
    excursion in volts.
    """
    t, cmd, fr = a[:, 0], a[:, 1], a[:, 2]
    hi = fr > 1.5
    rises = np.flatnonzero(np.diff(hi.astype(np.int8)) == 1) + 1
    frames = t[rises]
    if hi[0]:
        frames = np.r_[t[0], frames]
    else:
        # the file started after the first frame's pulse: in these files the
        # deflections fall one frame earlier relative to the first pulse than
        # in files that start on a pulse, so one frame came before the file.
        frames = np.r_[frames[0] - np.median(np.diff(frames)), frames]
    missed_first = not hi[0]
    base = np.median(cmd)
    act = np.flatnonzero(np.abs(cmd - base) > 0.01)
    br = np.flatnonzero(np.diff(act) > 2000)
    starts = np.r_[act[0], act[br + 1]]
    ends = np.r_[act[br], act[-1]]
    shape, amp = [], []
    for s0, e0 in zip(starts, ends):
        seg = cmd[s0:e0 + 1] - base
        mx, mn = seg.max(), -seg.min()
        if mn < 0.1 * mx:
            shape.append("P"); amp.append(mx)
        elif mx < 0.6 * mn:
            shape.append("A"); amp.append(mn)
        else:
            shape.append("V"); amp.append(max(mx, mn))
    return {"frames": frames, "onsets": t[starts], "durations": (ends - starts) / 1e4,
            "shape": np.array(shape), "amp_v": np.array(amp), "baseline_v": base,
            "duration_s": t[-1] - t[0] + 1e-4, "n_samples": len(t),
            "missed_first_pulse": missed_first, "n_pulses": len(rises) + int(hi[0])}


def amplitude_levels(stim):
    """Amplitude level 1, 2 or 3 of each deflection within its shape, and the
    normalised amplitude (1, 3, 5 as the Figure 2B legend, from the volts
    divided by the smallest of that shape)."""
    lev = np.zeros(len(stim["shape"]), int)
    norm = np.zeros(len(stim["shape"]))
    for s in "PVA":
        i = stim["shape"] == s
        norm[i] = stim["amp_v"][i] / stim["amp_v"][i].min()
        lev[i] = np.argmin(np.abs(norm[i][:, None] - np.array([1, 3, 5])[None]), 1) + 1
    return lev, norm


# ---------------------------------------------------------------- images

def _shift_fft(ref_f, img, upto=20):
    """Whole-pixel shift that best aligns img to ref (phase correlation)."""
    f = np.fft.rfft2(img)
    r = ref_f * np.conj(f)
    r /= np.abs(r) + 1e-9
    c = np.fft.irfft2(r, s=img.shape)
    c = np.roll(c, (upto, upto), axis=(0, 1))[:2 * upto + 1, :2 * upto + 1]
    dy, dx = np.unravel_index(np.argmax(c), c.shape)
    return dy - upto, dx - upto


def _apply_shift(img, dy, dx):
    out = np.roll(img, (dy, dx), axis=(-2, -1))
    return out


def register_movie(mov, upto=20):
    """Rigid whole-pixel registration of every frame to the first frame."""
    sm = ndi.gaussian_filter(mov.astype(np.float32), (0, 1, 1))
    ref_f = np.fft.rfft2(sm[0] - sm[0].mean())
    shifts = np.array([_shift_fft(ref_f, fr - fr.mean(), upto) for fr in sm])
    reg = np.empty_like(mov)
    for k, (dy, dx) in enumerate(shifts):
        reg[k] = _apply_shift(mov[k], dy, dx)
    return reg, shifts


def detect_rois(mean_img):
    """Somatic ROIs on the mean image (assumption, module docstring)."""
    from skimage.feature import peak_local_max
    from skimage.segmentation import watershed
    img = mean_img.astype(float)
    sig = SOMA_SIGMA_UM * PX_PER_UM
    loc = ndi.gaussian_filter(img, 4 * sig)
    spread = np.sqrt(ndi.gaussian_filter((img - loc) ** 2, 4 * sig)) + 1e-6
    z = (img - loc) / spread
    log = -ndi.gaussian_laplace(z, sig) * sig ** 2
    peaks = peak_local_max(log, min_distance=int(sig), threshold_abs=0.5, exclude_border=4)
    markers = np.zeros(img.shape, int)
    for i, (y, x) in enumerate(peaks, 1):
        markers[y, x] = i
    mask = (ndi.gaussian_filter(z, 1) > 0.5) & (log > 0.2)
    lab = watershed(-log, markers, mask=mask)
    px_area = PX_PER_UM ** 2
    rois = []
    for i in range(1, len(peaks) + 1):
        m = lab == i
        a = m.sum() / px_area
        if MIN_AREA_UM2 <= a <= MAX_AREA_UM2:
            ys, xs = np.nonzero(m)
            rois.append({"pix": (ys, xs), "centroid_px": (ys.mean(), xs.mean()), "area_um2": a})
    return rois


def masks_from_rois(rois, shape):
    lab = np.zeros(shape, int)
    for i, r in enumerate(rois, 1):
        lab[r["pix"]] = i
    return lab


def process_field(movies, seed=0):
    """Register the movies of one field, find ROIs on the mean image, and
    return the per-movie traces of the ROIs, halos, vessel background and ten
    neuropil ROIs (two placements)."""
    reps = sorted(movies)
    regs, shifts, means = {}, {}, {}
    for r in reps:
        regs[r], shifts[r] = register_movie(movies[r])
        means[r] = regs[r].mean(0)
    ref_f = np.fft.rfft2(ndi.gaussian_filter(means[reps[0]], 1) - means[reps[0]].mean())
    between = {}
    for r in reps:
        mi = ndi.gaussian_filter(means[r], 1)
        dy, dx = _shift_fft(ref_f, mi - mi.mean())
        between[r] = (dy, dx)
        regs[r] = _apply_shift(regs[r], dy, dx)
        means[r] = _apply_shift(means[r], dy, dx)
    mean_img = np.mean([means[r] for r in reps], 0)
    rois = detect_rois(mean_img)
    shape = mean_img.shape
    lab = masks_from_rois(rois, shape)
    allroi = lab > 0
    near = ndi.binary_dilation(allroi, iterations=HALO_INNER_PX)
    halos = []
    for r_ in rois:
        m = np.zeros(shape, bool); m[r_["pix"]] = True
        ring = ndi.binary_dilation(m, iterations=HALO_OUTER_PX) & ~near
        halos.append(np.nonzero(ring))
    excl = ndi.binary_dilation(allroi, iterations=HALO_OUTER_PX)
    vessel = (mean_img <= np.percentile(mean_img[~excl], VESSEL_PERCENTILE)) & ~excl
    # neuropil ROIs: disks of the median somatic area, centred in pixels away
    # from somata and halos and brighter than the darkest quarter (vessels).
    med_area_px = np.median([len(r_["pix"][0]) for r_ in rois]) if rois else 100
    rad = np.sqrt(med_area_px / np.pi)
    free = ~ndi.binary_dilation(allroi, iterations=HALO_OUTER_PX + int(rad))
    free &= mean_img > np.percentile(mean_img, 25)
    free[:int(rad) + 1] = free[-int(rad) - 1:] = False
    free[:, :int(rad) + 1] = free[:, -int(rad) - 1:] = False
    yy, xx = np.mgrid[:shape[0], :shape[1]]
    neuropil = []
    for placement in range(2):
        rng = np.random.default_rng([seed, placement])
        cand = np.flatnonzero(free.ravel())
        chosen = []
        for c in rng.permutation(cand):
            cy, cx = divmod(c, shape[1])
            if all((cy - a) ** 2 + (cx - b) ** 2 > (2 * rad) ** 2 for a, b in chosen):
                chosen.append((cy, cx))
            if len(chosen) == N_NEUROPIL:
                break
        neuropil.append([{"pix": np.nonzero((yy - a) ** 2 + (xx - b) ** 2 <= rad ** 2), "centroid_px": (a, b)}
                         for a, b in chosen])
    traces = {}
    for r in reps:
        mv = regs[r].reshape(regs[r].shape[0], -1).astype(np.float32)
        def tr(pix):
            idx = np.ravel_multi_index(pix, shape)
            return mv[:, idx].mean(1)
        bg = tr(np.nonzero(vessel))
        F = np.array([tr(r_["pix"]) for r_ in rois]).reshape(len(rois), -1)
        H = np.array([tr(h) for h in halos]).reshape(len(rois), -1)
        NP = [np.array([tr(n["pix"]) for n in pl]).reshape(len(pl), -1) for pl in neuropil]
        traces[r] = {"F": F, "halo": H, "bg": bg, "neuropil": NP,
                     "corrected": (F - bg) - HALO_FACTOR * (H - bg),
                     "neuropil_corrected": [n - bg for n in NP]}
    # a fingerprint of each movie, to find recordings deposited twice
    fp = {r: (float(movies[r][:50].mean()), float(movies[r].std()), int(movies[r][0].astype(np.int64).sum()))
          for r in reps}
    for r_ in rois:
        del r_["pix"]
    return {"reps": reps, "rois": rois, "traces": traces, "mean_img": mean_img.astype(np.float32),
            "shifts": shifts, "between": between, "fingerprint": fp,
            "n_vessel_px": int(vessel.sum()),
            "neuropil_centroids": [[n["centroid_px"] for n in pl] for pl in neuropil],
            "halo_npx": [len(h[0]) for h in halos]}


# ---------------------------------------------------------------- measures

def dff(corrected):
    """dF/F0 per movie; F0 the 8th percentile in a 6 s symmetric window."""
    f0 = ndi.percentile_filter(corrected, F0_PERCENTILE, size=(1, F0_WINDOW), mode="nearest")
    return (corrected - f0) / f0, f0


def first_frame_after(frames, onsets):
    return np.searchsorted(frames, onsets, side="left")


def responses(d, frames, onsets):
    """Response amplitude of every ROI (rows) to every deflection (columns)."""
    k = first_frame_after(frames, onsets)
    n = d.shape[1]
    ok = (k - N_BEFORE >= 0) & (k + N_AFTER <= n)
    out = np.full((d.shape[0], len(onsets)), np.nan)
    for j in np.flatnonzero(ok):
        out[:, j] = d[:, k[j]:k[j] + N_AFTER].mean(1) - d[:, k[j] - N_BEFORE:k[j]].mean(1)
    return out


def fdr(p, q=0.05, method="pdep"):
    """Benjamini-Hochberg ('pdep') or Benjamini-Yekutieli ('dep') step-up, as
    fdr_bh by D. Groppe, which the Methods name. Returns a boolean array."""
    p = np.asarray(p, float)
    shape = p.shape
    p = p.ravel()
    m = len(p)
    if m == 0:
        return np.zeros(shape, bool)
    order = np.argsort(p)
    ps = p[order]
    c = 1.0 if method == "pdep" else np.sum(1.0 / np.arange(1, m + 1))
    thr = np.arange(1, m + 1) * q / (m * c)
    below = np.flatnonzero(ps <= thr)
    h = np.zeros(m, bool)
    if len(below):
        h[order[:below[-1] + 1]] = True
    return h.reshape(shape)


def regress_separate(R, shape, norm):
    """Slope and two-sided p of the regression of responses on normalised
    amplitude, one regression per waveform type. R is ROIs x deflections."""
    n_roi = R.shape[0]
    slope = np.zeros((n_roi, 3)); p = np.ones((n_roi, 3)); se = np.zeros((n_roi, 3))
    for j, s in enumerate("PVA"):
        cols = (shape == s) & ~np.isnan(R[0])
        x = norm[cols]
        for i in range(n_roi):
            res = stats.linregress(x, R[i, cols])
            slope[i, j], p[i, j], se[i, j] = res.slope, res.pvalue, res.stderr
    return slope, p, se


def regress_joint(R, shape, norm):
    """One regression of all responses on the three amplitudes (zero for the
    other two types) with one intercept; slopes and two-sided t-test p."""
    cols = ~np.isnan(R[0])
    X = np.zeros((cols.sum(), 4)); X[:, 0] = 1
    for j, s in enumerate("PVA"):
        X[:, j + 1] = np.where(shape[cols] == s, norm[cols], 0)
    Y = R[:, cols].T
    beta, *_ = np.linalg.lstsq(X, Y, rcond=None)
    resid = Y - X @ beta
    dof = X.shape[0] - X.shape[1]
    s2 = (resid ** 2).sum(0) / dof
    cov = np.linalg.inv(X.T @ X)
    se = np.sqrt(np.outer(s2, np.diag(cov)[1:]))
    tval = beta[1:].T / se
    p = 2 * stats.t.sf(np.abs(tval), dof)
    return beta[1:].T, p, se


def tuning(slope, p, method="pdep", family="all", sign="both"):
    """Significant coefficients of one field after the false discovery rate
    procedure. family 'all' = all 3 x N p-values of the field, 'feature' = the
    N p-values of each feature. sign 'positive' keeps only positive
    significant slopes."""
    if family == "all":
        sig = fdr(p, method=method)
    else:
        sig = np.column_stack([fdr(p[:, j], method=method) for j in range(3)])
    if sign == "positive":
        sig &= slope > 0
    return sig


def pair_distances_mm(centroids_px):
    c = np.asarray(centroids_px, float) / PX_PER_UM / 1000.0
    d = np.sqrt(((c[:, None, :] - c[None, :, :]) ** 2).sum(-1))
    iu = np.triu_indices(len(c), 1)
    return d[iu], iu


def spearman_pairs(X):
    """Spearman correlation of every pair of rows of X (upper triangle)."""
    Rk = np.apply_along_axis(stats.rankdata, 1, X)
    c = np.corrcoef(Rk)
    return c[np.triu_indices(len(X), 1)]


def slope(x, y):
    if len(x) < 2 or np.ptp(x) == 0:
        return np.nan
    return np.polyfit(x, y, 1)[0]


def shuffle_segments(trace, bounds, rng):
    """Permute the order of the segments [bounds[i], bounds[i+1]) of a 1-D
    trace; frames before the first and after the last bound stay in place."""
    segs = [trace[bounds[i]:bounds[i + 1]] for i in range(len(bounds) - 1)]
    order = rng.permutation(len(segs))
    return np.concatenate([trace[:bounds[0]]] + [segs[o] for o in order] + [trace[bounds[-1]:]])


# ---------------------------------------------------------------- per field

def field_data(data, key, reps=None):
    """Responses and traces of one field over the recordings ``reps`` that
    have a stimulus file (all such recordings when None)."""
    f = data["fields"][key]
    use = [r for r in f["reps"] if (key[0], key[1], r) in data["stims"]]
    if reps is not None:
        use = [r for r in use if r in reps]
    Rs, shape, lev, norm, rec, bounds, corr, dffs = [], [], [], [], [], [], [], []
    offset = 0
    # ROIs whose F0 reaches zero or below in any recording (corrected
    # fluorescence at or under the halo's) have no defined dF/F0; dropped
    keep = np.ones(len(f["rois"]), bool)
    for r in f["reps"]:
        keep &= dff(f["traces"][r]["corrected"])[1].min(1) > 0
    for r in use:
        st = data["stims"][(key[0], key[1], r)]
        l, nm = amplitude_levels(st)
        c = f["traces"][r]["corrected"][keep]
        d, _ = dff(c)
        Rs.append(responses(d, st["frames"], st["onsets"]))
        shape.append(st["shape"]); lev.append(l); norm.append(np.array([1, 3, 5])[l - 1])
        rec.append(np.full(len(l), r))
        k = first_frame_after(st["frames"], st["onsets"])
        bounds.append(offset + k[k < c.shape[1]])
        corr.append(c); dffs.append(d)
        offset += c.shape[1]
    return {"reps": use, "R": np.concatenate(Rs, 1), "shape": np.concatenate(shape),
            "level": np.concatenate(lev), "norm": np.concatenate(norm), "rec": np.concatenate(rec),
            "bounds": bounds, "corrected": np.concatenate(corr, 1), "dff": np.concatenate(dffs, 1),
            "neuropil": [np.concatenate([f["traces"][r]["neuropil_corrected"][pl] for r in use], 1)
                         for pl in range(2)],
            "centroids": np.array([r_["centroid_px"] for r_ in f["rois"]]).reshape(-1, 2)[keep],
            "n_rois": len(f["rois"]), "n_dropped": int((~keep).sum()),
            "neuropil_centroids": f["neuropil_centroids"]}


def rank_rows(X):
    return stats.rankdata(X, axis=1)


def spearman_upper(X):
    c = np.corrcoef(rank_rows(X))
    return c[np.triu_indices(len(X), 1)]


def shuffled_series(X, bounds, rng, within=True):
    """Each row's responses to the stimulus presentations permuted in time:
    segments from one onset to the next, permuted within each recording
    (``within``) or over the whole concatenated series. Frames before the
    first onset and after the last of a recording stay in place."""
    out = X.copy()
    segs = []
    n_tot = X.shape[1]
    for b in bounds:
        segs.append([(b[i], b[i + 1]) for i in range(len(b) - 1)])
    for i in range(X.shape[0]):
        if within:
            for sg in segs:
                if not sg:
                    continue
                order = rng.permutation(len(sg))
                start = sg[0][0]
                pieces = [X[i, sg[o][0]:sg[o][1]] for o in order]
                cat = np.concatenate(pieces)
                out[i, start:start + len(cat)] = cat
        else:
            allseg = [s for sg in segs for s in sg]
            order = rng.permutation(len(allseg))
            pieces = [X[i, allseg[o][0]:allseg[o][1]] for o in order]
            # write the permuted segments back into the slots of the
            # segments, in order; segment lengths differ, so the slots are
            # filled consecutively across each recording's span
            cat = np.concatenate(pieces)
            pos = 0
            for sg in segs:
                if not sg:
                    continue
                L = sg[-1][1] - sg[0][0]
                out[i, sg[0][0]:sg[-1][1]] = cat[pos:pos + L]
                pos += L
    return out
