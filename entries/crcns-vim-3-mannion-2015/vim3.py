"""Loading and measures for CRCNS vim-3 (Mannion 2015, PeerJ 3:e1038).

The data set is one gzipped tar file in the public CRCNS bucket. It cannot be
opened in place (a tar.gz has no index), so it is streamed once, member by
member, and each participant's files are handed over when the stream leaves
that participant's directory. Nothing is written to disk.

Where parameters come from:

- Task performance (`task_performance`) follows task.py of the paper's code
  (mannion-lab/ul_sens_fmri_analysis at 571e9312), as the claim
  figs2-task-no-condition-difference cites it: 0.1 s bins over the run length
  minus 32 s, targets and button presses after 32 s, the p1004 target rule for
  runs 1 to 5, a target assigned to the image event that starts 0 to 2 s after
  its bin, and correlations at lags of 0 to 19 bins. The window 0.4 to 0.9 s
  (bins 4 to 9) and the two-way repeated measures ANOVA are group.py tasks().
  Reading (a) is task.py as written, which compares event onsets with the bin
  time plus 32 s; reading (b) compares them with the bin time (criterion of
  the claim). Variant (c), an addition of this attempt shown for information,
  bins the whole of 32 to 332 s so that no presses pile into the last bin.
- Run order: the n-th NIfTI file of a participant, sorted by series number,
  is run n (the participant configs of the paper's code list the series in
  that order, for example p1003 series 3, 4, 6 to 13). The notebook checks it
  against the data.
- GLM (`design`, `fit_ols`): SPM canonical HRF convolved with a 1 s event
  (Methods, Analysis; AFNI SPMG1(1) in config.py), first 16 volumes of each
  run censored, polynomials up to the third degree per run (Methods,
  Analysis). Separate GLMs for upper and lower presentation (Methods,
  Analysis). The paper fits with AFNI 3dREMLfit (ARMA(1,1) noise); here
  ordinary least squares is used, which gives the same kind of beta estimate
  but different t values (a deviation, used only for the data checks and the
  volume variant). Standard choices that cannot change a conclusion here:
  the regressor is sampled at the middle of each 2 s volume (the slices are
  not shifted in time) and scaled to a peak of 1.
- Volume localiser (`volume_masks`): the threshold t > 2.58 is config.py
  loc_glm_thresh (the Methods' p < 0.01). The paper restricts the mask to
  V1, V2 and V3 on the cortical surface; those definitions are not in the
  data set, so here the mask is every voxel of the brain mask above
  threshold. This is a substitute, not the paper's region, and no outcome
  rests on it.
- Image patches and Gabor filters (`patch_crops` to `radial_bias_tests`)
  follow imstats.py get_fragments, _get_filter_bank, run_filter and
  test_radial_bias, as the claims no-radial-bias-in-patches and
  fig5bc-spatial-frequency cite them; the 353 pixel square is the Methods'
  (Image patch analysis) and the aperture position the experiment's
  config.py. The monitor's CIE coordinates are not public, so the DKL axes
  are formed under assumed calibrations (`CALIBRATIONS`, an assumption: two
  common LCD gamuts, to show how far the result depends on the choice). The
  OpenCV Gabor kernel and filter2D are written out in numpy and scipy, to
  avoid a dependency (same formula and border rule).
"""

import io
import re
import tarfile
import urllib.request
from collections import defaultdict

import nibabel as nib
import numpy as np
from scipy import stats

DATASET = "vim-3"
VERSION = "unversioned"  # CRCNS data sets are not versioned (docs/archives.md); the md5 pins the file
TAR_MD5 = "005760a76158d4f16f54b41ee24cd1f2"  # checksums.md5 of the data set
URL = "https://crcnsarchive.s3-us-west-2.amazonaws.com/vim-3/crcns_vim-3.tar.gz"

TR = 2.0
N_VOLS = 166
N_CENSOR = 16  # Methods, Analysis: "The first 16 volumes (32 s) of each run were censored"
RUN_LEN_S = 332.0  # Methods, Design
LOC_THRESH = 2.58  # config.py loc_glm_thresh


def stream_participants(url=URL, read_images=True):
    """Stream the tar.gz once and yield one dict per participant.

    Each dict has 'id', 'seq', 'task', 'lut' (dicts by run number 1 to 10),
    'series' (NIfTI series numbers, sorted), 'images' (list of int16 arrays
    in series order, or None), 'affine', 'scale', and 'md5' (per file). After
    the last participant a final dict with id 'stim' lists the stimulus PNG
    names, their md5 sums, colour content (`colour`) and bytes (`png`), the
    count of every member of the archive by kind and parent directory
    (`members`), the files outside the participant and stimulus directories
    (`other_files`), and the md5 and size of the whole tar.gz as streamed (to
    compare with the data set's checksums.md5).
    """
    import hashlib

    resp = _HashingReader(url)
    current = None
    stim = {"id": "stim", "names": [], "md5": {}}

    def new(pid):
        return {"id": pid, "seq": {}, "task": {}, "lut": {}, "nii": {},
                "md5": {}, "affine": None, "scale": None}

    def finish(p):
        series = sorted(p["nii"])
        p["series"] = series
        p["images"] = [p["nii"][s] for s in series] if read_images else None
        del p["nii"]
        return p

    members = defaultdict(int)
    with tarfile.open(fileobj=resp, mode="r|gz") as tf:
        for m in tf:
            parts = m.name.split("/")
            # every member, by kind and parent directory, so that nothing is skipped unseen
            members[("file" if m.isfile() else "directory" if m.isdir() else "other",
                     "/".join(parts[:-1]))] += 1
            if not m.isfile():
                continue
            if len(parts) == 4 and parts[1] == "data":
                pid = parts[2]
                if current is None or current["id"] != pid:
                    if current is not None:
                        yield finish(current)
                    current = new(pid)
                name = parts[3]
                is_nii = name.endswith(".nii")
                if is_nii and not read_images:
                    h = hashlib.md5()
                    f = tf.extractfile(m)
                    for chunk in iter(lambda: f.read(2**22), b""):
                        h.update(chunk)
                    current["md5"][name] = h.hexdigest()
                    current["nii"][int(re.search(r"SENSE_(\d+)_1", name).group(1))] = None
                    continue
                b = tf.extractfile(m).read()
                current["md5"][name] = hashlib.md5(b).hexdigest()
                if is_nii:
                    img = nib.Nifti1Image.from_bytes(b)
                    current["affine"] = img.affine
                    current["scale"] = (img.dataobj.slope, img.dataobj.inter)
                    data = np.asarray(img.dataobj.get_unscaled())
                    current["nii"][int(re.search(r"SENSE_(\d+)_1", name).group(1))] = data
                    del b, img
                else:
                    a = np.load(io.BytesIO(b), allow_pickle=False)
                    run = int(re.search(r"run_(\d+)_", name).group(1))
                    kind = ("lut" if name.endswith("task_lut.npy") else
                            "task" if name.endswith("task.npy") else "seq")
                    current[kind][run] = a
            elif len(parts) == 3 and parts[1] == "stim":
                b = tf.extractfile(m).read()
                stim["names"].append(parts[2])
                stim["md5"][parts[2]] = hashlib.md5(b).hexdigest()
                stim.setdefault("colour", {})[parts[2]] = _png_colour(b)
                stim.setdefault("png", {})[parts[2]] = b
            else:
                stim.setdefault("other_files", []).append((m.name, m.size))
    stim["members"] = dict(members)
    if current is not None:
        yield finish(current)
    while resp.read(2**22):
        pass
    stim["tar_md5"] = resp.md5.hexdigest()
    stim["tar_bytes"] = resp.n
    stim["reconnects"] = resp.reconnects
    yield stim


def _png_colour(b):
    """Size of a stimulus screenshot and the largest difference between its R, G and B values."""
    import png
    w, h, rows, info = png.Reader(bytes=b).asRGB8()
    a = np.vstack([np.frombuffer(r, np.uint8) for r in rows]).reshape(h, w, 3).astype(np.int16)
    return {"width": w, "height": h, "max_rg": int(np.abs(a[..., 0] - a[..., 1]).max()),
            "max_rb": int(np.abs(a[..., 0] - a[..., 2]).max())}


class _HashingReader:
    """File-like reader of a URL that keeps an md5 and a byte count of what is read.

    The stream pauses while a participant is processed, and S3 may close an
    idle connection; on a connection error the reader reopens the URL with a
    Range request at the current offset (up to 20 times).
    """

    def __init__(self, url):
        import hashlib
        self.url = url
        self.md5 = hashlib.md5()
        self.n = 0
        self.reconnects = 0
        self.raw = urllib.request.urlopen(url, timeout=120)

    def read(self, size=-1):
        while True:
            try:
                b = self.raw.read(size)
                break
            except (ConnectionError, TimeoutError, OSError):
                self.reconnects += 1
                if self.reconnects > 20:
                    raise
                req = urllib.request.Request(self.url, headers={"Range": f"bytes={self.n}-"})
                self.raw = urllib.request.urlopen(req, timeout=120)
                assert self.raw.status == 206
        self.md5.update(b)
        self.n += len(b)
        return b


# ---------------------------------------------------------------- task (Fig. S2)

def task_performance(p, reading="a", n_runs=10, trial_len_s=4.0, n_lags=20, bin_res=0.1):
    """Performance on the central task per presentation, source and lag (task.py).

    Returns (perf, info): perf is (2 pres [upper, lower], 2 src [above, below],
    n_lags) correlations; info counts targets, assigned targets and presses,
    and 'by_condition' the assigned targets per presentation and source.

    Readings (a), (b) and (c) are described in the module docstring. Two more
    variants of this attempt, both on the timing of reading (b), change only
    the assignment window (task.py: an event starting strictly between 0 and
    2 s after the bin): (d) the same window with its start included
    (0 <= difference < 2 s), so that targets falling exactly on an event onset
    are kept; (e) the event in progress, starting up to 2 s before the target
    (-2 < difference <= 0 s).
    """
    lo, hi, lo_incl, hi_incl = 0.0, trial_len_s / 2.0, False, False
    if reading == "d":
        lo_incl = True
    elif reading == "e":
        lo, hi, hi_incl = -trial_len_s / 2.0, 0.0, True
    if reading == "c":
        edges = np.arange(32.0, RUN_LEN_S, bin_res)
        offset = 0.0
    else:
        edges = np.arange(0.0, RUN_LEN_S - 32.0, bin_res)
        offset = 32.0 if reading == "a" else 0.0
    n_bins = len(edges)
    responses = np.zeros((n_runs, n_bins))
    targets = np.zeros((n_runs, n_bins))
    tasks = np.zeros((n_runs, 2, 2, n_bins))
    info = defaultdict(int)
    for i_run in range(n_runs):
        for (_, t) in p["task"][i_run + 1]:
            if t <= 32.0:
                continue
            responses[i_run, np.where(t > edges)[0][-1]] = 1
            info["presses"] += 1
        lut = p["lut"][i_run + 1]
        for row in lut:
            if p["id"] == "p1004" and i_run < 5:
                # task.py: p1004 responded to white 9 and black 5 in runs 1 to 5
                is_target = (row[1] == 9 and row[2] == 1) or (row[1] == 5 and row[2] == -1)
            else:
                is_target = bool(row[3])
            if row[0] <= 32.0 or not is_target:
                continue
            targets[i_run, np.where(row[0] >= edges)[0][-1]] = 1
            info["targets"] += 1
        seq = p["seq"][i_run + 1]
        for i_bin in np.flatnonzero(targets[i_run]):
            time_diff = seq[..., 0] - (edges[i_bin] + offset)
            ok = (((time_diff >= lo) if lo_incl else (time_diff > lo))
                  & ((time_diff <= hi) if hi_incl else (time_diff < hi)))
            if ok.sum() == 0:
                info["unassigned"] += 1
                continue
            if ok.sum() > 1:
                info["ambiguous"] += 1
                continue
            vf, i_ev = np.where(ok)
            src = int(seq[vf[0], i_ev[0], 1]) - 1
            if src == -1:
                info["null_event"] += 1
                continue
            tasks[i_run, vf[0], src, i_bin] = 1
            info["assigned"] += 1
    perf = np.full((2, 2, n_lags), np.nan)
    for i_pres in range(2):
        for i_src in range(2):
            for lag in range(n_lags):
                perf[i_pres, i_src, lag] = np.corrcoef(
                    tasks[:, i_pres, i_src, :].ravel(),
                    np.roll(responses, -lag, axis=1).ravel())[0, 1]
    info = dict(info)
    info["by_condition"] = tasks.sum(axis=(0, 3)).astype(int)
    return perf, info


def rm_anova_2x2(values):
    """Two-way repeated measures ANOVA on values of shape (n_subj, 2, 2).

    Returns {effect: (F, df1, df2, p)} for 'pres', 'src' and 'pres:src'. With
    two levels per factor each effect is a paired contrast, F = t**2.
    """
    v = np.asarray(values, float)
    n = v.shape[0]
    contrasts = {
        "pres": (v[:, 0, :].mean(1) - v[:, 1, :].mean(1)),
        "src": (v[:, :, 0].mean(1) - v[:, :, 1].mean(1)),
        "pres:src": (v[:, 0, 0] - v[:, 0, 1]) - (v[:, 1, 0] - v[:, 1, 1]),
    }
    out = {}
    for k, d in contrasts.items():
        t, p = stats.ttest_1samp(d, 0.0)
        out[k] = (float(t ** 2), 1, n - 1, float(p))
    return out


# ---------------------------------------------------------------- GLM

def spm_hrf(dt=0.1, length=32.0):
    """SPM canonical HRF (peak 6 s, undershoot 16 s, ratio 1/6) sampled at dt."""
    t = np.arange(0, length, dt)
    h = stats.gamma.pdf(t, 6) - stats.gamma.pdf(t, 16) / 6.0
    return h / h.sum()


def event_regressor(onsets, dur=1.0, dt=0.1):
    """Events of `dur` s convolved with the SPM HRF, sampled mid-volume, peak 1."""
    n_hi = int(round(N_VOLS * TR / dt))
    box = np.zeros(n_hi)
    for o in onsets:
        box[max(0, int(round(o / dt))):max(0, int(round((o + dur) / dt)))] = 1.0
    full = np.convolve(box, spm_hrf(dt))[:n_hi]
    idx = np.round((np.arange(N_VOLS) * TR + TR / 2) / dt).astype(int)
    reg = full[idx]
    # scale so that a single isolated event peaks at 1 (standard choice)
    single = np.convolve(np.ones(int(round(dur / dt))), spm_hrf(dt))
    return reg / single.max()


def poly_block(n_runs):
    """Legendre polynomials of degree 0 to 3 per run, censored volumes removed."""
    n_keep = N_VOLS - N_CENSOR
    x = np.linspace(-1, 1, n_keep)
    P = np.stack([np.polynomial.legendre.Legendre.basis(d)(x) for d in range(4)], 1)
    out = np.zeros((n_runs * n_keep, n_runs * 4))
    for r in range(n_runs):
        out[r * n_keep:(r + 1) * n_keep, r * 4:(r + 1) * 4] = P
    return out


def design(seqs, field, by="all", shift_s=0.0):
    """Event regressors for one presentation field (0 upper, 1 lower).

    `seqs` is a list of run sequence arrays in run order. by='all' gives one
    regressor for every image event (the localiser); by='image' 60 (image by
    source, ordered by image id then above, below). Returns (X_events,
    labels); censored volumes are removed.
    """
    rows = []
    labels = None
    for seq in seqs:
        ev = seq[field]
        ev = ev[ev[:, 1] > 0]
        if by == "all":
            groups = {"image": ev[:, 0]}
        else:
            ids = sorted(set(ev[:, 2].astype(int)))
            groups = {(i, s): ev[(ev[:, 2] == i) & (ev[:, 1] == k), 0]
                      for i in ids for k, s in ((1, "above"), (2, "below"))}
        if labels is None:
            labels = list(groups)
        cols = [event_regressor(groups[g] + shift_s) for g in labels]
        rows.append(np.stack(cols, 1)[N_CENSOR:])
    return np.concatenate(rows, 0), labels


def fit_ols(X_ev, Y, n_runs):
    """OLS with per-run polynomials. Returns betas (events), t values, psc, residuals, dof.

    psc is 100 * beta / the temporal mean of the fitted polynomial part
    (Methods, Response amplitude: "division by the temporal average of the
    polynomial regressor timecourse").
    """
    P = poly_block(n_runs)
    X = np.concatenate([X_ev, P], 1)
    XtX_inv = np.linalg.pinv(X.T @ X)
    B = XtX_inv @ X.T @ Y
    resid = Y - X @ B
    dof = X.shape[0] - np.linalg.matrix_rank(X)
    s2 = (resid ** 2).sum(0) / dof
    k = X_ev.shape[1]
    se = np.sqrt(np.outer(np.diag(XtX_inv)[:k], s2))
    t = B[:k] / se
    baseline = (P @ B[k:]).mean(0)
    psc = 100.0 * B[:k] / baseline
    return B[:k], t, psc, resid, dof


def brain_mask(images, frac=0.2):
    """Voxels whose mean intensity exceeds `frac` of the 98th percentile (standard choice)."""
    m = np.mean([im.mean(-1) for im in images], 0)
    return m > frac * np.percentile(m, 98)


def masked_timeseries(images, mask):
    """Concatenate runs over uncensored volumes: array (n_runs * 150, n_voxels), float32."""
    return np.concatenate([im[mask][:, N_CENSOR:].T.astype(np.float32) for im in images], 0)


# ---------------------------------------------------------------- per participant

def motion_index(images, mask):
    """Displacement of the brain's intensity centre of mass, in mm.

    Returns per run the largest displacement of any volume from the first
    volume of run 1. A coarse index of head motion: the paper motion-corrected
    the data (Methods, Pre-processing); this attempt does not.
    """
    coords = np.argwhere(mask) * 2.0  # 2 mm voxels
    ref = None
    out = []
    for im in images:
        v = im[mask].astype(np.float64)  # (n_vox, n_vols)
        com = (coords.T @ v) / v.sum(0)  # (3, n_vols)
        if ref is None:
            ref = com[:, 0:1]
        out.append(float(np.sqrt(((com - ref) ** 2).sum(0)).max()))
    return np.array(out)


def process_participant(p, shifts=tuple(range(-12, 14, 2))):
    """Reduce one participant to the small results the notebook uses.

    For each presentation field: the volume localiser mask over all runs
    (its location and the volume variant of the response amplitudes), and
    leave-one-run-out checks of the run order and the clock: the mask is made
    from the other nine runs, and the mean of the held-out run over that mask
    is fitted with each run's sequence (run order), with its own sequence
    shifted in time (clock), and with the other field's sequence (contrast).
    """
    images = p["images"]
    seqs = [p["seq"][r] for r in range(1, 11)]
    mask = brain_mask(images)
    out = {"id": p["id"], "n_brain_voxels": int(mask.sum()),
           "shape": images[0].shape, "dtype": str(images[0].dtype),
           "raw_range": (int(min(im.min() for im in images)),
                         int(max(im.max() for im in images)))}
    out["motion_mm"] = motion_index(images, mask)
    Y = masked_timeseries(images, mask)
    ijk = np.argwhere(mask)
    nk = N_VOLS - N_CENSOR
    out["fields"] = {}
    for field in (0, 1):
        res = {}
        X, _ = design(seqs, field)
        _, t, _, _, _ = fit_ols(X, Y, 10)
        sel = t[0] > LOC_THRESH
        res["n_mask"] = int(sel.sum())
        res["mask_j"] = ijk[sel, 1]  # axis 1 runs superior to inferior
        res["mask_k"] = ijk[sel, 2]  # axis 2 runs anterior to posterior
        order = np.zeros((10, 10))
        shift_t = np.zeros((10, len(shifts)))
        other_t = np.zeros(10)
        n_mask_cv = np.zeros(10, int)
        for i in range(10):
            keep = [k for k in range(10) if k != i]
            rows = np.concatenate([np.arange(k * nk, (k + 1) * nk) for k in keep])
            Xk, _ = design([seqs[k] for k in keep], field)
            _, tk, _, _, _ = fit_ols(Xk, Y[rows], 9)
            sel_i = tk[0] > LOC_THRESH
            n_mask_cv[i] = int(sel_i.sum())
            roi_i = Y[i * nk:(i + 1) * nk, sel_i].mean(1, keepdims=True)
            for j in range(10):
                Xj, _ = design([seqs[j]], field)
                order[i, j] = fit_ols(Xj, roi_i, 1)[1][0, 0]
            for s, sh in enumerate(shifts):
                Xs, _ = design([seqs[i]], field, shift_s=sh)
                shift_t[i, s] = fit_ols(Xs, roi_i, 1)[1][0, 0]
            Xo, _ = design([seqs[i]], 1 - field)
            other_t[i] = fit_ols(Xo, roi_i, 1)[1][0, 0]
        res.update(order_t=order, shift_t=shift_t, shifts=np.array(shifts),
                   other_field_t=other_t, n_mask_cv=n_mask_cv)
        # volume variant: ROI mean timecourse, 60 regressors (image by source)
        roi = Y[:, sel].mean(1, keepdims=True)
        Xi, labels = design(seqs, field, by="image")
        _, _, psc_i, resid, _ = fit_ols(Xi, roi, 10)
        res["labels"] = labels
        res["psc_image"] = psc_i[:, 0]
        res["resid_ms"] = float(np.mean((100.0 * resid[:, 0] / roi.mean()) ** 2))
        out["fields"][field] = res
    return out


# ---------------------------------------------------------------- image patches (radial bias)

# Patch geometry: the experiment's config.py (mannion-lab/ul_sens_fmri at
# 5e98dd81) gives 4.5 degree apertures centred at 5.37 degrees eccentricity on
# the diagonals; the Methods, Image patch analysis, give the 353 by 353 pixel
# square cut from the screenshot. imstats.py get_fragments takes the patches
# from the upper presentation screenshots ("pres_loc_a", here "pres_loc_u").
AP_ECC_DEG = 5.37
PATCH_PIX = 353
# Pixels per degree: psychopy deg2pix with the local "BOLDscreen" profile,
# which is not public. The claim fig5bc-spatial-frequency fixes about 78.7
# (1,920 pixels over the Methods' 24.4 degrees) and asks for 78.2 as the other value.
PIX_PER_DEG = 1920 / 24.4
SCREEN_ROWS, SCREEN_COLS = 1200, 1920

# Assumed monitor calibrations (an assumption of this attempt: the paper's
# measured CIE coordinates of the BOLDscreen primaries are not public). CIE
# 1931 xy of the red, green and blue primaries and their luminance at full
# output relative to the white, for two common LCD gamuts: sRGB (ITU-R BT.709
# primaries, D65 white) and Adobe RGB (1998), a wide-gamut LCD standard.
CALIBRATIONS = {
    "sRGB": {"xy": [(0.64, 0.33), (0.30, 0.60), (0.15, 0.06)], "Y": [0.2126, 0.7152, 0.0722]},
    "Adobe RGB": {"xy": [(0.64, 0.33), (0.21, 0.71), (0.15, 0.06)], "Y": [0.2974, 0.6273, 0.0753]},
}
# Smith and Pokorny cone fundamentals from (Judd-Vos) XYZ, as used by Brainard
# (1996), which the Methods cite for the DKL transform; L + M = Y.
XYZ_TO_LMS = np.array([[0.15514, 0.54312, -0.03286],
                       [-0.15514, 0.45684, 0.03286],
                       [0.0, 0.0, 0.00801]])


def read_png(b):
    """RGB screenshot as a uint8 array (rows, columns, 3)."""
    import png
    w, h, rows, info = png.Reader(bytes=b).asRGB8()
    return np.vstack([np.frombuffer(r, np.uint8) for r in rows]).reshape(h, w, 3)


def patch_crops(img, pix_per_deg=PIX_PER_DEG, size=PATCH_PIX, field="upper"):
    """The left and right patch squares of a screenshot.

    Same arithmetic as imstats.py get_fragments, which uses the upper
    presentation screenshots: the aperture centre is at (+-ecc / sqrt 2,
    +ecc / sqrt 2) degrees from the screen centre (-ecc / sqrt 2 vertically
    for field='lower', used only to check the screenshots), and the square
    starts at int(centre - size / 2). Returns float array (2 [left, right],
    size, size, 3) of pixel values / 255.
    """
    off = AP_ECC_DEG / np.sqrt(2.0) * pix_per_deg
    centre = np.array([SCREEN_ROWS, SCREEN_COLS]) / 2.0
    y = off if field == "upper" else -off
    out = []
    for x in (-off, +off):
        r0 = int(centre[0] - y - size / 2.0)
        c0 = int(centre[1] + x - size / 2.0)
        out.append(img[r0:r0 + size, c0:c0 + size, :].astype(float) / 255.0)
    return np.array(out)


def rgb_to_dkl_matrix(cal, background=(0.5, 0.5, 0.5)):
    """Matrix taking linear RGB (0 to 1, minus the background) to DKL axes.

    The Methods say the display was linearised, and imstats.py converts pixel
    value / 255 directly, so pixel values are taken as linear. RGB to XYZ from
    the primaries' xy and Y, XYZ to LMS (Smith and Pokorny), then the DKL axes
    about the background (Brainard 1996): luminance L + M; L - M at constant
    luminance, L - (L0 / M0) M; and S - (S0 / (L0 + M0)) (L + M). Each axis is
    scaled to unit length in cone-increment units here; the scale of an axis
    does not change a paired test within that axis.
    """
    cols = []
    for (x, y), Y in zip(cal["xy"], cal["Y"]):
        cols.append([x / y * Y, Y, (1 - x - y) / y * Y])
    rgb_to_xyz = np.array(cols).T
    rgb_to_lms = XYZ_TO_LMS @ rgb_to_xyz
    L0, M0, S0 = rgb_to_lms @ np.asarray(background)
    lms_to_dkl = np.array([[1.0, 1.0, 0.0],
                           [1.0, -L0 / M0, 0.0],
                           [-S0 / (L0 + M0), -S0 / (L0 + M0), 1.0]])
    lms_to_dkl /= np.linalg.norm(lms_to_dkl, axis=1, keepdims=True)
    return lms_to_dkl @ rgb_to_lms


def circle_mask(n, radius):
    """psychopy.filters.makeMask(n, 'circle', radius, range=[0, 1]): 1 inside radius (of the half width), else 0."""
    x = np.linspace(-1.0, 1.0, n)
    xx, yy = np.meshgrid(x, x)
    return (np.sqrt(xx ** 2 + yy ** 2) <= radius).astype(float)


def gabor_kernel(ksize, sigma, theta, lambd, gamma=1.0, psi=np.pi / 2):
    """cv2.getGaborKernel, written out in numpy (OpenCV 2/3 imgproc/gabor.cpp)."""
    half = ksize // 2
    c, s = np.cos(theta), np.sin(theta)
    sx, sy = sigma, sigma / gamma
    k = np.zeros((ksize, ksize))
    for y in range(-half, half + 1):
        for x in range(-half, half + 1):
            xr = x * c + y * s
            yr = -x * s + y * c
            k[half - y, half - x] = np.exp(-0.5 * (xr ** 2 / sx ** 2 + yr ** 2 / sy ** 2)) * np.cos(2 * np.pi / lambd * xr + psi)
    return k


def filter_bank(pix_per_deg=PIX_PER_DEG, sfs=(1.0, 2.0, 4.0, 8.0, 16.0), oris_deg=(0, 45, 90, 135)):
    """imstats.py _get_filter_bank: odd-symmetric Gabors with a one octave bandwidth.

    Returns a list over spatial frequency of arrays (n_ori, k, k). The
    orientation convention is that of imstats.py (0 horizontal, angles
    counter-clockwise), passed to the kernel as mod(-ori - pi / 2, 2 pi).
    """
    bank = []
    for sf in sfs:
        wl = pix_per_deg / sf
        sigma = wl / np.pi * np.sqrt(np.log(2) / 2.0) * (2 ** 1 + 1) / (2 ** 1 - 1)
        k = int(sigma * 6)
        if k % 2 == 0:
            k += 1
        bank.append(np.array([gabor_kernel(k, sigma, np.mod(-np.radians(o) - np.pi / 2, 2 * np.pi), wl)
                              for o in oris_deg]))
    return bank


def filter_output(chan, bank):
    """imstats.py run_filter for one patch channel (already masked).

    cv2.filter2D (correlation, border reflected without repeating the edge
    pixel) by FFT; the output is the square root of the summed squared
    response. Returns (n_sf, n_ori).
    """
    from scipy.signal import fftconvolve
    out = np.zeros((len(bank), bank[0].shape[0]))
    for i_sf, b in enumerate(bank):
        h = b.shape[-1] // 2
        pad = np.pad(chan, h, mode="reflect")
        for i_o in range(b.shape[0]):
            r = fftconvolve(pad, b[i_o, ::-1, ::-1], mode="valid")
            out[i_sf, i_o] = np.sqrt((r ** 2).sum())
    return out


def patch_filter_outputs(screens, cal, pix_per_deg=PIX_PER_DEG, img_ids=None):
    """Filter outputs of every patch: array (n_img, 2 src [above, below], 2 side [left, right], 3 DKL, n_sf, n_ori).

    `screens` maps (img_id, src 'a' or 'b') to the upper presentation
    screenshot. The patch is converted to DKL about the background, multiplied
    by a circular mask of radius 0.9 (run_filter) and filtered.
    """
    M = rgb_to_dkl_matrix(cal)
    bank = filter_bank(pix_per_deg)
    mask = circle_mask(PATCH_PIX, 0.9)
    ids = sorted({k[0] for k in screens}) if img_ids is None else img_ids
    out = np.zeros((len(ids), 2, 2, 3, len(bank), bank[0].shape[0]))
    for i, img_id in enumerate(ids):
        for j, src in enumerate("ab"):
            crops = patch_crops(screens[(img_id, src)], pix_per_deg)
            for side in range(2):
                dkl = (crops[side] - 0.5) @ M.T
                for c in range(3):
                    out[i, j, side, c] = filter_output(dkl[..., c] * mask, bank)
    return out


def radial_bias_tests(filt):
    """imstats.py test_radial_bias: mean over spatial frequency, paired t-test over images of 45 against 135 degrees.

    `filt` as from patch_filter_outputs. Returns rows (channel, source, side,
    t, p, mean difference, median difference).
    """
    f = filt.mean(-2)
    rows = []
    for c in range(f.shape[3]):
        for j in range(2):
            for side in range(2):
                d = f[:, j, side, c, :]
                t, p = stats.ttest_rel(d[:, 1], d[:, 3])
                rows.append((c, j, side, float(t), float(p), float((d[:, 1] - d[:, 3]).mean()),
                             float(np.median(d[:, 1] - d[:, 3]))))
    return rows
