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
    names, their md5 sums and colour content (`colour`), and the md5 and size of the whole tar.gz as
    streamed (to compare with the data set's checksums.md5).
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

    with tarfile.open(fileobj=resp, mode="r|gz") as tf:
        for m in tf:
            if not m.isfile():
                continue
            parts = m.name.split("/")
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
    n_lags) correlations; info counts targets, assigned targets and presses.
    """
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
            ok = (time_diff > 0) & (time_diff < trial_len_s / 2.0)
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
    return perf, dict(info)


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
