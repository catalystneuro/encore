"""Loading and per-sweep measures for CRCNS pvc-9 (Saez and Friedlander 2016, PLoS One 11(2):e0147642).

The data set (doi:10.6080/K00V89R6) is not versioned on CRCNS (docs/archives.md, "CRCNS"); it is read as
`crcns:pvc-9/unversioned` from the public S3 bucket, `pvc-9/live/data.tar.gz`, whose MD5 in the data set's
checksums.md5 is 217a64766d19e7ad87efa4e339b82295. The archive is a gzipped tar, which has no index, so it is
streamed once from start to end (about 1.1 GB compressed, 1.7 GB of members) and each ABF file is reduced to
per-sweep measures as it passes; nothing is written to disk. The three Excel files in the archive (ECS_IC.xls,
ECS_VC.xls, ECS_VCB.xls) are kept in memory: the data descriptor says they mark which recordings the paper
included (green) or excluded (red).

Where each parameter comes from:

- Pre-pairing epoch: the 120 sweeps before pairing (Methods, Plasticity induction, "After the pre-pairing epoch
  was complete (120 stimuli at 0.2 Hz)"; claims file, opening comment). Where a cell has more than 120
  baseline sweeps, the last 120 before the pairing file are used: an assumption (the epoch the Methods call
  complete when pairing starts); the first 120 are run as a variant.
- Post-pairing windows (P): (a) all sweeps after the first pairing, up to a second pairing if there is one;
  (b) the first 120 of them; (c) the last 120 (claims file, opening comment). Cells with two pairings use the
  first: the paper describes one pairing per cell (Methods, Plasticity induction).
- Peak measure (M): from the claims file's opening comment, the peak of the deflection in the response's
  sign (depolarizing in current clamp, inward in voltage clamp) from the end of the stimulus artifact to
  50 ms after the stimulus, less the mean of the 10 ms before it; a 30 ms window is a variant. The stimulus
  is found in each sweep as its largest step between 50 and 200 ms (the descriptor puts the pulse
  "typically around 100 ms into the recordings"). The end of the artifact is found per file, as the trough
  between artifact and response in the median aligned trace, 0.5 to 3 ms after the stimulus (a standard
  choice, as the claims file names no rule); fixed ends of 1 and 2 ms are variants.
- Per-cell t-test (T): (a) two-sample Student's t-test (equal variance) on sweep amplitudes, (b) the same on
  1-min bin means, 12 sweeps per bin at 0.2 Hz (claims file, opening comment; Figure 1B legend, 60 s bins).
- Classification: LTP when p < 0.05 and change > +15%, LTD when p < 0.05 and change < -15%, NC otherwise
  (Methods, Plasticity induction).
"""

from __future__ import annotations

import builtins
import hashlib
import io
import os
import re
import tarfile

import fsspec
import numpy as np
import pandas as pd
import pyabf
import pyabf.abf as _pyabf_abf
import xlrd
from scipy import stats

DATASET = "crcns:pvc-9/unversioned"
DATASET_DOI = "10.6080/K00V89R6"
BASE_URL = "https://crcnsarchive.s3-us-west-2.amazonaws.com/pvc-9/live/"
DATA_URL = BASE_URL + "data.tar.gz"
DATA_MD5 = "217a64766d19e7ad87efa4e339b82295"   # from pvc-9/live/checksums.md5

RATE = 20000              # Hz; checked against every file header in the notebook
N_PRE = 120               # Methods, Plasticity induction
N_POST_WINDOW = 120       # readings (P)(b) and (c): 10 min at 0.2 Hz
BIN_SWEEPS = 12           # reading (T)(b): 60 s bins at 0.2 Hz (Figure 1B legend)
BASELINE_MS = 10.0        # claims file, (M)
WINDOWS_MS = (50.0, 30.0)  # claims file, (M): 50 ms, with 30 ms as a variant
THRESHOLD = 0.15          # Methods, Plasticity induction
ALPHA = 0.05

GROUPS = {"IC": "ECS_IC.xls", "VC": "ECS_VC.xls", "VCB": "ECS_VCB.xls"}


# ----------------------------------------------------------------------------------------------- reading


def abf_from_bytes(buf: bytes, name: str = "mem.abf") -> pyabf.ABF:
    """Parse an ABF file held in memory. pyabf reads only from a path, so its file access is pointed at the
    bytes for the duration of the call."""
    fake = os.path.abspath("/__inmemory__/" + os.path.basename(name))
    real_exists, real_fromfile = os.path.exists, np.fromfile

    def fake_open(path, mode="r", *a, **k):
        if path == fake:
            return io.BytesIO(buf)
        return builtins.open(path, mode, *a, **k)

    def fake_fromfile(fb, dtype=float, count=-1, **k):
        if isinstance(fb, io.BytesIO):
            dt = np.dtype(dtype)
            return np.frombuffer(fb.read(-1 if count < 0 else count * dt.itemsize), dtype=dt)
        return real_fromfile(fb, dtype=dtype, count=count, **k)

    _pyabf_abf.open = fake_open
    os.path.exists = lambda p: True if p == fake else real_exists(p)
    np.fromfile = fake_fromfile
    try:
        return pyabf.ABF(fake, loadData=True, cacheStimulusFiles=False)
    finally:
        del _pyabf_abf.open
        os.path.exists = real_exists
        np.fromfile = real_fromfile


def stimulus_indices(Y: np.ndarray, rate: int) -> np.ndarray:
    """Sample of the stimulus pulse in each sweep: the largest step between 50 and 200 ms. The pulse is at
    107.9 ms in most sweeps but earlier (88 to 99 ms) in some sweeps of some files, so it is found per sweep."""
    lo, hi = int(0.05 * rate), int(0.2 * rate)
    return lo + np.argmax(np.abs(np.diff(Y[:, lo:hi + 1], axis=1)), axis=1)


def aligned(Y: np.ndarray, stims: np.ndarray, rate: int, before_ms: float, after_ms: float) -> np.ndarray:
    """Each sweep from before_ms before its stimulus to after_ms after it."""
    off = np.arange(-int(before_ms * rate / 1000), int(after_ms * rate / 1000) + 1)
    return Y[np.arange(len(Y))[:, None], stims[:, None] + off[None, :]]


def artifact_end(trace: np.ndarray, rate: int, sign: int, before_ms: float) -> int:
    """End of the stimulus artifact, in samples after the stimulus, from the median aligned trace of a file:
    the trough between the artifact and the response (the lowest point in the response's sign) between 0.5
    and 3 ms after the stimulus. A standard choice that implements the claims file's "end of the stimulus
    artifact" (M); fixed ends of 1 and 2 ms are run as variants."""
    z = int(before_ms * rate / 1000)
    a, b = z + int(0.5e-3 * rate) + 1, z + int(3e-3 * rate) + 1
    return a + int(np.argmin(sign * trace[a:b])) - z


def peak_amplitudes(A: np.ndarray, z: int, rate: int, sign: int, start: int, window_ms: float) -> tuple:
    """Peak of the response in its sign from `start` samples after the stimulus to window_ms after it, less
    the mean of the BASELINE_MS before the stimulus, on aligned sweeps A whose stimulus is at sample z.
    Returns amplitudes (positive for a response in the expected sign) and peak latencies in ms."""
    base = A[:, z - int(BASELINE_MS * rate / 1000):z].mean(axis=1)
    seg = sign * (A[:, z + start:z + int(window_ms * rate / 1000) + 1] - base[:, None])
    k = np.argmax(seg, axis=1)
    return seg[np.arange(len(seg)), k], (start + k) * 1000.0 / rate


def reduce_abf(a: pyabf.ABF) -> dict:
    """Per-sweep measures of channel 0 of one file, with its header, its median aligned trace near the
    stimulus, and an MD5 of each sweep's samples to find files deposited twice."""
    Y = np.array([_sweep(a, i) for i in range(a.sweepCount)], dtype=np.float64)
    rate = int(a.dataRate)
    units = a.adcUnits[0]
    head = dict(protocol=a.protocol, start=pd.Timestamp(a.abfDateTime), n_sweeps=a.sweepCount, rate=rate,
                sweep_s=Y.shape[-1] / rate if Y.ndim == 2 else 0.0, units=units, adc_units=list(a.adcUnits),
                n_channels=a.channelCount,
                interval_s=float(a.sweepTimesSec[1] - a.sweepTimesSec[0]) if a.sweepCount > 1 else np.nan)
    if Y.ndim != 2 or Y.shape[1] < int(0.3 * rate):
        return dict(head, sign=0, sweep_md5=[])
    sign = 1 if units == "mV" else -1
    stims = stimulus_indices(Y, rate)
    before, after = 70.0, 60.0
    A = aligned(Y, stims, rate, before, after)
    z = int(before * rate / 1000)
    med = np.median(A, axis=0)
    end = artifact_end(med, rate, sign, before)
    out = dict(head, sign=sign, stim_ms=stims * 1000.0 / rate, artifact_end_ms=end * 1000.0 / rate,
               base=A[:, z - int(BASELINE_MS * rate / 1000):z].mean(axis=1),
               sweep_md5=[hashlib.md5(y.astype(np.float32).tobytes()).hexdigest() for y in Y])
    for w in WINDOWS_MS:
        out[f"amp{int(w)}"], out[f"lat{int(w)}"] = peak_amplitudes(A, z, rate, sign, end, w)
    for fixed in (1, 2):
        out[f"amp50_end{fixed}ms"] = peak_amplitudes(A, z, rate, sign, int(fixed * rate / 1000), 50.0)[0]
    # the same measure on a stretch of equal length ending 5 ms before the stimulus: a reference for
    # whether the measured response is locked to the stimulus
    out["amp_prestim"] = peak_amplitudes(A, z - int(55e-3 * rate), rate, sign, end, 50.0)[0]
    out["median_trace"] = med[z - int(15e-3 * rate):].astype(np.float32)   # 15 ms before to 60 ms after
    return out


def _sweep(a: pyabf.ABF, i: int) -> np.ndarray:
    a.setSweep(i, channel=0)
    return a.sweepY.copy()


def stream_dataset(url: str = DATA_URL, keep=None) -> tuple[pd.DataFrame, dict]:
    """One pass over data.tar.gz. Returns a table of every ABF file (one row per file, with per-sweep arrays)
    and the bytes of the three Excel files. `keep(folder)` can limit the ABF files reduced (for a subset)."""
    rows, sheets, members = [], {}, []
    with fsspec.open(url, block_size=2**22) as f, tarfile.open(fileobj=f, mode="r|gz") as tf:
        for m in tf:
            members.append(dict(name=m.name, size=m.size, is_file=m.isfile()))
            if not m.isfile():
                continue
            parts = m.name.split("/")
            if m.name.endswith(".xls"):
                sheets[parts[-1]] = tf.extractfile(m).read()
                continue
            if len(parts) != 4 or not parts[3].lower().endswith(".abf"):
                continue
            if keep is not None and not keep(parts[2]):
                continue
            a = abf_from_bytes(tf.extractfile(m).read(), parts[3])
            row = dict(group_dir=parts[1], folder=parts[2], file=parts[3], size=m.size)
            row.update(reduce_abf(a))
            rows.append(row)
            del a
    files = pd.DataFrame(rows)
    return files, dict(sheets=sheets, members=pd.DataFrame(members))


# ------------------------------------------------------------------------------------------ spreadsheets


def _is_red(wb, sheet, r, c) -> bool:
    xf = wb.xf_list[sheet.cell_xf_index(r, c)]
    if not xf.background.fill_pattern:
        return False
    rgb = wb.colour_map.get(xf.background.pattern_colour_index)
    return rgb is not None and rgb[0] > 200 and rgb[1] < 50


def read_summary(xls: bytes, group: str) -> pd.DataFrame:
    """The Summary sheet: one row per recording with its name, whether its name is filled red (excluded, per
    the data descriptor), and the change it lists (fraction)."""
    wb = xlrd.open_workbook(file_contents=xls, formatting_info=True)
    s = wb.sheet_by_name("Summary")
    rows = []
    for r in range(s.nrows):
        name = s.cell_value(r, 1)
        if not (isinstance(name, str) and re.fullmatch(group + r"\d+", name)):
            continue
        v = s.cell_value(r, 2)
        rows.append(dict(cell=name, excluded=_is_red(wb, s, r, 1),
                         sheet_change=float(v) if isinstance(v, float) else np.nan,
                         note=" ".join(str(s.cell_value(r, c)) for c in range(3, min(s.ncols, 6))
                                       if isinstance(s.cell_value(r, c), str))))
    return pd.DataFrame(rows)


def _expand_files(value, prefix: str | None) -> list[str]:
    """File numbers as the IC sheets write them: 7301005.0, '7321004/005', a short 2.0 that continues the
    date prefix, or '07301003?'."""
    if value == "" or value is None:
        return []
    if isinstance(value, float):
        n = int(value)
        return [f"{n:08d}"] if n >= 1_000_000 else ([f"{prefix}{n:03d}"] if prefix else [])
    out = []
    first = None
    for part in str(value).replace("?", "").split("/"):
        part = part.strip()
        if not part.isdigit():
            continue
        if len(part) >= 7:
            first = f"{int(part):08d}"
            out.append(first)
        elif first or prefix:
            out.append((first[:5] if first else prefix) + f"{int(part):03d}")
    return out


def read_cell_sheet(xls: bytes, cell: str) -> dict:
    """From a cell's sheet: the files the FILES block lists for each epoch (IC sheets only), the PRE and POST
    counts or ranges, and the mean pre and post amplitudes and change the sheet computes."""
    wb = xlrd.open_workbook(file_contents=xls)
    s = wb.sheet_by_name(cell)
    out = dict(files={}, pre_label=None, post_label=None, sheet_pre=np.nan, sheet_post=np.nan)
    labels = {}
    for r in range(min(s.nrows, 60)):
        for c in range(14, s.ncols):
            v = s.cell_value(r, c)
            if isinstance(v, str) and v.strip():
                labels.setdefault(v.strip(), (r, c))
    if "PRE" in labels:
        r, c = labels["PRE"]
        out["pre_label"] = s.cell_value(r, c + 1)
    if "POST" in labels:
        r, c = labels["POST"]
        out["post_label"] = s.cell_value(r, c + 1)
    amp_cols = [c for c in range(14, s.ncols) for r in range(min(s.nrows, 60))
                if s.cell_value(r, c) == "EPSC amplitude"]
    if amp_cols:
        r = next(r for r in range(min(s.nrows, 60)) if s.cell_value(r, amp_cols[0]) == "EPSC amplitude")
        vals = [s.cell_value(r + 1, c) for c in sorted(set(amp_cols))]
        if len(vals) == 2 and all(isinstance(v, float) for v in vals):
            out["sheet_pre"], out["sheet_post"] = vals
    prefix = None
    block = {}
    if "FILES" in labels:   # the epoch labels in the rows below "FILES", in its column
        r0, c0 = labels["FILES"]
        for r in range(r0 + 1, min(s.nrows, r0 + 12)):
            v = s.cell_value(r, c0)
            if isinstance(v, str) and v.strip():
                block.setdefault(v.strip(), s.cell_value(r, c0 + 2) if c0 + 2 < s.ncols else "")
    for lab in ("I/O", "Baseline", "Pairing 1", "Postpairing 1", "Pairing 2", "Postpairing 2"):
        if lab not in block:
            continue
        v = block[lab]
        f = _expand_files(v, prefix)
        if f and prefix is None:
            prefix = f[0][:5]
        out["files"][lab] = f
    return out


# ---------------------------------------------------------------------------------------------- cells


def cell_table(files: pd.DataFrame, sheets: dict) -> pd.DataFrame:
    """One row per recording listed in the three Summary sheets: group, inclusion, the files of each epoch,
    and where its data are. For IC cells the epochs come from the sheet's FILES block (the folders do not
    follow the sheets: folder IC7 holds the files the IC6 sheet lists). For VC and VCB cells, whose sheets
    list no files, the folder's own recordings are used, ordered by start time: the pairing file is the one
    with protocol "Extracellular pairing"; the derived files (Concatenate*, *_PRE, *_POST) are left out."""
    rows = []
    for group, fname in GROUPS.items():
        summ = read_summary(sheets[fname], group)
        for _, s in summ.iterrows():
            info = read_cell_sheet(sheets[fname], s.cell)
            row = dict(group=group, cell=s.cell, excluded=s.excluded, sheet_change=s.sheet_change,
                       note=s.note, pre_label=info["pre_label"], post_label=info["post_label"],
                       sheet_pre=info["sheet_pre"], sheet_post=info["sheet_post"])
            own = files[(files.folder == s.cell) & ~is_derived(files.file)].sort_values("start")
            if group == "IC":
                fl = info["files"]
                base = fl.get("Baseline", [])
                pair1 = fl.get("Pairing 1", [])
                post1 = fl.get("Postpairing 1", [])
                pair2 = fl.get("Pairing 2", [])
                stem = files.file.str.replace(".abf", "", regex=False)
                found = lambda names: list(files.index[stem.isin(names) & files.group_dir.eq("Data_ECS_IC")])
                # a listed file is used only if its header agrees with the epoch it is listed for
                is_test = lambda i: files.loc[i, "protocol"] == "Alternate stim Iclamp" and files.loc[i, "interval_s"] == 5.0
                is_pair = lambda i: files.loc[i, "protocol"] == "Extracellular pairing" and files.loc[i, "n_sweeps"] >= 30
                listed = dict(pre=found(base), pair=found(pair1), post=found(post1))
                row.update(pre_rows=[i for i in listed["pre"] if is_test(i)],
                           pair_rows=[i for i in listed["pair"] if is_pair(i)],
                           post_rows=[i for i in listed["post"] if is_test(i)],
                           pair2_rows=found(pair2), listed_files=base + pair1 + post1,
                           rejected_files=[files.loc[i, "file"] for k, f in (("pre", is_test), ("pair", is_pair),
                                                                              ("post", is_test))
                                           for i in listed[k] if not f(i)],
                           source="sheet FILES block")
            else:
                # a pairing file holds the 60 pairing trials; single-sweep files with the pairing protocol
                # (VCB6, VCB14) are not pairings. Test sweeps are pA files at 0.2 Hz.
                pair = own[(own.protocol == "Extracellular pairing") & (own.n_sweeps >= 30)]
                test = own[(own.protocol != "Extracellular pairing") & (own.units == "pA") & (own.interval_s == 5.0)]
                if len(pair):
                    t_pair = pair.start.iloc[0]
                    pre = test[test.start < t_pair]
                    post = test[test.start > t_pair]
                    nxt = pair.start.iloc[1] if len(pair) > 1 else None
                    if nxt is not None:
                        post = post[post.start < nxt]
                    row.update(pre_rows=list(pre.index), pair_rows=[pair.index[0]],
                               post_rows=list(post.index), pair2_rows=list(pair.index[1:]))
                else:
                    row.update(pre_rows=[], pair_rows=[], post_rows=[], pair2_rows=[])
                row.update(listed_files=[], rejected_files=[], source="folder")
            row["folder_exists"] = bool((files.folder == s.cell).any())
            row["has_data"] = bool(row["pre_rows"]) and bool(row["pair_rows"]) and bool(row["post_rows"])
            rows.append(row)
    return pd.DataFrame(rows)


def is_derived(names: pd.Series) -> pd.Series:
    return names.str.contains(r"^Concatenate|_PRE|_POST", case=False, regex=True)


def epoch_amplitudes(files: pd.DataFrame, rows: list, window: int = 50) -> np.ndarray:
    if not rows:
        return np.array([])
    return np.concatenate([files.loc[i, f"amp{window}"] for i in sorted(rows, key=lambda i: files.loc[i, "start"])])


def cell_epochs(files: pd.DataFrame, cell: pd.Series, window: int = 50, pre_reading: str = "last") -> dict:
    """Pre and post sweep amplitudes of one cell. pre_reading 'last' (main) or 'first' 120 baseline sweeps."""
    pre_all = epoch_amplitudes(files, cell.pre_rows, window)
    post_all = epoch_amplitudes(files, cell.post_rows, window)
    pre = pre_all[-N_PRE:] if pre_reading == "last" else pre_all[:N_PRE]
    return dict(pre=pre, n_pre_available=len(pre_all), post={
        "a": post_all, "b": post_all[:N_POST_WINDOW], "c": post_all[-N_POST_WINDOW:]})


def bin_means(x: np.ndarray, k: int = BIN_SWEEPS) -> np.ndarray:
    """Means of consecutive bins of k sweeps; a last partial bin is kept if it holds at least half of k."""
    n = len(x) // k
    out = [x[i * k:(i + 1) * k].mean() for i in range(n)]
    if len(x) - n * k >= k / 2:
        out.append(x[n * k:].mean())
    return np.array(out)


def classify(pre: np.ndarray, post: np.ndarray, test: str = "a", alternative: str = "two-sided") -> dict:
    """Change (percent) and class of one cell. test 'a' on sweeps, 'b' on 1-min bin means."""
    change = 100.0 * (post.mean() / pre.mean() - 1.0)
    x, y = (pre, post) if test == "a" else (bin_means(pre), bin_means(post))
    if alternative == "two-sided":
        p = stats.ttest_ind(x, y, equal_var=True).pvalue
    else:  # one-sided in the direction of the change
        p = stats.ttest_ind(y, x, equal_var=True, alternative="greater" if change > 0 else "less").pvalue
    cls = "NC"
    if p < ALPHA and change > 100 * THRESHOLD:
        cls = "LTP"
    elif p < ALPHA and change < -100 * THRESHOLD:
        cls = "LTD"
    return dict(change=change, p=p, cls=cls, pre_mean=pre.mean(), post_mean=post.mean())


def classify_all(files: pd.DataFrame, cells: pd.DataFrame, window: int = 50, pre_reading: str = "last",
                 alternative: str = "two-sided") -> pd.DataFrame:
    """Every included cell with data, under every reading of (P) and (T)."""
    rows = []
    for _, c in cells[~cells.excluded & cells.has_data].iterrows():
        ep = cell_epochs(files, c, window, pre_reading)
        for P in "abc":
            for T in "ab":
                r = classify(ep["pre"], ep["post"][P], T, alternative)
                r.update(group=c.group, cell=c.cell, P=P, T=T, n_pre=len(ep["pre"]), n_post=len(ep["post"][P]),
                         n_pre_available=ep["n_pre_available"])
                rows.append(r)
    return pd.DataFrame(rows)
