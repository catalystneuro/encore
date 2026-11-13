"""Loading and measures for CRCNS hc-17 (van Dijk and Fenton 2018, Neuron 98, 832-845).

The data set is one zip, ``hc-17/live/data.zip``, read in place from the public S3 bucket
``crcnsarchive`` over range requests (docs/archives.md, CRCNS). Nothing is written to disk.

Files used (data descriptor, paper/hc-17.data-description.txt):

- ``data/TS/<session>..cl-fix.P<t>C<c>Rm`` and ``...Ar``: one file per unit and session, a
  13-line ASCII header and then, per position sample, x (1 byte), y (1 byte), the number of
  spikes n (1 byte) and n spike times (uint32, 100-us units). ``Rm`` is the room frame, ``Ar``
  the arena frame (place avoidance only). ``_4`` files are the same at 4x coarser time and 8x
  coarser space; ``.times`` the spike times as text. ``data/TS/EnvironmentalTask/`` holds the
  environment manipulation sessions (room frame only).
- ``data/*.xlsx``: the paper's lists of place cells and putative interneurons (date or mouse,
  tetrode P, cluster C).
- ``data/behavior/...dat``: Tracker files (30 Hz). The shock-on files hold the reinforced
  sector (centre angle, width, inner and outer radius in pixels) and the avoidance state.

Where each parameter comes from is said beside it: [claims Mx] is the method label of the
claims file (claims/dijk-2018.yaml), which cites the paper; [paper] a passage of the paper,
cited; [assumption] a choice the paper leaves open, with the reason; [standard] a choice
that cannot change a result.
"""
from __future__ import annotations

import functools
import io
import re
import zipfile

import fsspec
import numpy as np
import pandas as pd
from scipy import ndimage, stats

DATASET = "hc-17"  # CRCNS data set, doi:10.6080/K0Q23XDV
VERSION = "unversioned"  # CRCNS data sets are not versioned (docs/archives.md); see DATA_ZIP_MD5
URL = "https://crcnsarchive.s3-us-west-2.amazonaws.com/hc-17/live/data.zip"
DATA_ZIP_MD5 = "b577c885e9daf70a7a0af4ff67d11c51"  # from hc-17/live/checksums.md5

# Spatial grid. The paper analyses at "1.5 cm/pixel" (STAR Methods, Recording set up). The
# camera image is 256 x 256 tracker pixels; the data set's own rate maps (data/TIME, data/SPIKE)
# hold 1024 values and its "_4" files have SCALE 8, so the authors' grid is 32 x 32 bins of
# 8 tracker pixels. At the 6.4 pixels/cm of the Tracker headers that is 1.25 cm per bin.
# [assumption] we use the data set's 8-pixel grid, the closest to the paper's that the
# authors' own files show; see the notebook for the check.
BIN_PX = 8
NBIN = 256 // BIN_PX
PX_PER_CM = 6.4  # Tracker header, TrackerResolution_PixPerCM, place avoidance arena
ARENA_CENTER = (127.5, 127.5)  # Tracker header, ArenaCenterXY


@functools.lru_cache(maxsize=1)
def archive() -> zipfile.ZipFile:
    f = fsspec.open(URL, block_size=2**21).open()
    return zipfile.ZipFile(f)


@functools.lru_cache(maxsize=1)
def members() -> tuple:
    return tuple(i.filename for i in archive().infolist())


def read(name: str) -> bytes:
    return archive().read(name)


# --------------------------------------------------------------------------- TS files
def parse_ts(b: bytes) -> dict:
    """Decode a TS file: header values, per-sample x, y and spike count, and spike times."""
    end = b.index(b"%%ENDHEADER") + len(b"%%ENDHEADER")
    while b[end:end + 1] in (b"\r", b"\n"):
        end += 1
    hdr = b[:end].decode("latin1")
    fs = float(re.search(r"SAMPLING_INTERVAL\(samps/sec\)\s+([\d.]+)", hdr).group(1))
    t0 = int(re.search(r"FIRST_TIMESTAMP\(100usUnits\)\s+(\d+)", hdr).group(1))
    scale = float(re.search(r"SCALE_X\(RatioTracktoMapPixels\)\s+([\d.]+)", hdr).group(1))
    a = np.frombuffer(b, dtype=np.uint8, offset=end)
    n = len(a)
    xs, ys, ns, pos = [], [], [], []
    i = 0
    # walk the records: 3 bytes, then 4 bytes per spike
    while i + 3 <= n:
        k = int(a[i + 2])
        xs.append(a[i]); ys.append(a[i + 1]); ns.append(k); pos.append(i + 3)
        i += 3 + 4 * k
    x = np.array(xs, dtype=np.int16); y = np.array(ys, dtype=np.int16)
    ns = np.array(ns, dtype=np.int32); pos = np.array(pos, dtype=np.int64)
    sidx = np.repeat(np.arange(len(ns)), ns)
    offs = np.repeat(pos, ns) + 4 * (np.arange(ns.sum()) - np.repeat(np.cumsum(ns) - ns, ns))
    raw = a[(offs[:, None] + np.arange(4)[None, :]).ravel()].reshape(-1, 4) if len(offs) else np.zeros((0, 4), np.uint8)
    times = raw.astype(np.uint32) @ np.array([1, 256, 65536, 16777216], dtype=np.uint32) if len(offs) else np.zeros(0, np.uint32)
    return dict(fs=fs, t0=t0, scale=scale, x=x, y=y, nspk=ns, spike_sample=sidx,
                spike_times=times.astype(np.int64), header=hdr)


def ts_index() -> pd.DataFrame:
    """One row per TS unit file in the room or arena frame (no _4, .times or 0spks)."""
    rows = []
    rx = re.compile(r"^data/TS/(EnvironmentalTask/)?([^./]+?)_?(?:spikes_)?cl-fix\.P(\d+)C(\d+)(Rm|Ar)$")
    for m in members():
        r = rx.match(m)
        if r:
            rows.append(dict(path=m, env=bool(r.group(1)), session=r.group(2), tetrode=int(r.group(3)),
                             cluster=int(r.group(4)), frame=r.group(5)))
    return pd.DataFrame(rows)


# --------------------------------------------------------------------------- class lists
def class_list(name: str) -> pd.DataFrame:
    """The paper's cell lists (data/<name>.xlsx), quotes stripped."""
    d = pd.read_excel(io.BytesIO(read(f"data/{name}.xlsx")), header=None)
    d = d.map(lambda v: str(v).strip().strip("'"))
    d.columns = ["day", "tetrode", "cluster"]
    d["tetrode"] = d.tetrode.str[1:].astype(int)
    d["cluster"] = d.cluster.str[1:].astype(int)
    return d


# --------------------------------------------------------------------------- sessions
AVOID_KIND = [("Hab", "pretraining"), ("Ini1", "training1"), ("Ini2", "training2"), ("Conf", "conflict")]


def avoidance_sessions(idx: pd.DataFrame) -> pd.DataFrame:
    s = idx[~idx.env][["session"]].drop_duplicates().copy()
    s["mouse"] = s.session.str.extract(r"(WT\d+)")[0]
    s["kind"] = None
    for key, kind in AVOID_KIND:
        s.loc[s.session.str.contains(key), "kind"] = kind
    s["part"] = s.session.str.extract(r"(?:Ini\d|Conf\d|Hab\d)_(\d)")[0]
    s["hab_n"] = s.session.str.extract(r"Hab(\d)")[0]
    return s.sort_values(["mouse", "session"]).reset_index(drop=True)


def env_condition(session: str) -> str:
    s = session.lower()
    if "rot" in s:
        return "rotated"
    if "circleintestbox" in s or "circleinbox" in s:
        return "standard"
    if "testbox" in s:
        return "removed"
    return "other"  # diffcircle, transferbin: not one of the paper's three versions


def env_sessions(idx: pd.DataFrame) -> pd.DataFrame:
    s = idx[idx.env][["session"]].drop_duplicates().copy()
    s["day"] = s.session.str.extract(r"^(\d+_WT\d+)")[0]
    s["condition"] = s.session.map(env_condition)
    s["rank"] = s.session.str.extract(r"box(\d*)_?$")[0].replace("", "0").fillna("0").astype(int)
    return s.sort_values(["day", "session"]).reset_index(drop=True)


# --------------------------------------------------------------------------- Tracker files
def read_dat(name: str) -> tuple[dict, pd.DataFrame]:
    b = read(name).decode("latin1")
    h, d = b.split("%%END_HEADER", 1)
    fmt = re.search(r"%Sample\.0 \( (.*?) \)", h).group(1).split()
    meta = {}
    for key in ["ReinforcedSector", "ElapsedPath_m", "TrackerResolution_PixPerCM", "ArenaDiameter_m",
                "Time", "Date", "ElapsedTime_ms", "Frame"]:
        m = re.search(r"%" + key + r"\.0 \( (.*?) \)", h)
        if m:
            meta[key] = m.group(1).strip()
    lines = d.strip().splitlines()[1:]
    rows = [l.split() for l in lines]
    rows = [r[:len(fmt)] for r in rows if len(r) >= len(fmt)]
    df = pd.DataFrame(rows, columns=fmt).replace("*", np.nan).apply(pd.to_numeric, errors="coerce")
    return meta, df


def sector_of(meta: dict):
    """(centre angle deg, width deg, inner r px, outer r px) of the reinforced sector."""
    if "ReinforcedSector" not in meta:
        return None
    v = [float(t) for t in meta["ReinforcedSector"].split()]
    return tuple(v[:4])


def polar(x, y, angle_sign=-1.0):
    """Angle (deg, 0-360) and radius of tracker coordinates around the arena centre.

    The sign convention (image y down) is checked against the Tracker's own sector flag in
    the notebook; ``angle_sign`` = -1 means angles grow counter-clockwise on screen.
    """
    dx = np.asarray(x, float) - ARENA_CENTER[0]
    dy = np.asarray(y, float) - ARENA_CENTER[1]
    ang = np.degrees(np.arctan2(angle_sign * dy, dx)) % 360
    return ang, np.hypot(dx, dy)


def in_sector(x, y, sector, angle_sign=-1.0):
    c, w, r0, r1 = sector
    ang, r = polar(x, y, angle_sign)
    d = (ang - c + 180) % 360 - 180
    return (np.abs(d) <= w / 2) & (r >= r0) & (r <= r1)


def sector_boundary(sector, angle_sign=-1.0, n=120):
    c, w, r0, r1 = sector
    pts = []
    for a in np.linspace(c - w / 2, c + w / 2, n):
        for r in (r0, r1):
            pts.append((a, r))
    for a in (c - w / 2, c + w / 2):
        for r in np.linspace(r0, r1, n):
            pts.append((a, r))
    pts = np.array(pts)
    th = np.radians(pts[:, 0])
    bx = ARENA_CENTER[0] + pts[:, 1] * np.cos(th)
    by = ARENA_CENTER[1] + angle_sign * pts[:, 1] * np.sin(th)
    return bx, by


def distance_to_sector(x, y, sector, angle_sign=-1.0):
    """Euclidean distance (tracker px) to the nearest edge of the sector; 0 inside it."""
    bx, by = sector_boundary(sector, angle_sign)
    x = np.asarray(x, float); y = np.asarray(y, float)
    out = np.empty(len(x))
    for i in range(0, len(x), 4000):
        dx = x[i:i + 4000, None] - bx[None, :]
        dy = y[i:i + 4000, None] - by[None, :]
        out[i:i + 4000] = np.sqrt((dx * dx + dy * dy).min(axis=1))
    out[in_sector(x, y, sector, angle_sign)] = 0.0
    return out


def count_entries(inside: np.ndarray, valid: np.ndarray) -> int:
    """Entrances into a zone: outside-to-inside transitions over tracked samples."""
    s = inside[valid].astype(int)
    return int(((s[1:] == 1) & (s[:-1] == 0)).sum())


# --------------------------------------------------------------------------- maps
def tracked(x, y):
    """Samples with a position; the tracker writes (0, 0) when it loses the animal."""
    return ~((x == 0) & (y == 0))


def occupancy(x, y, fs, valid=None):
    v = tracked(x, y) if valid is None else valid
    bx = np.clip(x[v] // BIN_PX, 0, NBIN - 1); by = np.clip(y[v] // BIN_PX, 0, NBIN - 1)
    occ = np.zeros((NBIN, NBIN)); np.add.at(occ, (by, bx), 1.0 / fs)
    return occ


def spike_map(x, y, spike_sample, valid=None):
    v = tracked(x, y) if valid is None else valid
    s = spike_sample[v[spike_sample]]
    bx = np.clip(x[s] // BIN_PX, 0, NBIN - 1); by = np.clip(y[s] // BIN_PX, 0, NBIN - 1)
    m = np.zeros((NBIN, NBIN)); np.add.at(m, (by, bx), 1.0)
    return m


def rate_map(spk, occ, min_occ=0.0):
    """Spikes per bin over time per bin [claims M2]; unvisited bins (or bins under ``min_occ``
    seconds, reading (b) of M2, 0.67 s) are NaN. No smoothing [claims M2, both readings]."""
    with np.errstate(invalid="ignore", divide="ignore"):
        r = spk / occ
    r[(occ <= 0) | (occ < min_occ)] = np.nan
    return r


def map_stability(a, b, max_shift=2):
    """Fisher z of the Pearson r between corresponding bins, the maximum over shifts of one map
    by up to 2 bins in x and y [claims M3; STAR Methods, Firing rate stability]. Bins visited in
    both maps enter [standard]."""
    best = -np.inf
    n = a.shape[0]
    for dy in range(-max_shift, max_shift + 1):
        for dx in range(-max_shift, max_shift + 1):
            sa = a[max(0, dy):n + min(0, dy), max(0, dx):n + min(0, dx)]
            sb = b[max(0, -dy):n + min(0, -dy), max(0, -dx):n + min(0, -dx)]
            ok = np.isfinite(sa) & np.isfinite(sb)
            if ok.sum() < 10 or np.std(sa[ok]) == 0 or np.std(sb[ok]) == 0:
                continue
            r = np.corrcoef(sa[ok], sb[ok])[0, 1]
            best = max(best, r)
    if not np.isfinite(best):
        return np.nan
    return float(np.arctanh(np.clip(best, -0.999999, 0.999999)))


def place_fields(rmap, reading="a", min_bins=9):
    """Fields under the claims file's readings of M5 [assumption, claims M5]: (a) at least 9
    edge-contiguous bins above 20% of the map's peak; (b) the same above 1 AP/s."""
    r = np.nan_to_num(rmap, nan=0.0)
    peak = np.nanmax(rmap) if np.isfinite(rmap).any() else 0
    thr = 0.2 * peak if reading == "a" else 1.0
    if peak <= 0 or peak <= thr and reading == "b":
        return []
    lab, n = ndimage.label(r > thr)  # 4-connectivity: edge-contiguous
    fields = []
    for k in range(1, n + 1):
        m = lab == k
        if m.sum() >= min_bins:
            fields.append(m)
    fields.sort(key=lambda m: -m.sum())
    return fields


def info_content(rmap, occ):
    """Skaggs information, bits/spike and bits/s, over visited bins [standard measure; Table S1
    names "info content (bits/s)"]."""
    ok = np.isfinite(rmap) & (occ > 0)
    p = occ[ok] / occ[ok].sum(); r = rmap[ok]
    mr = (p * r).sum()
    if mr <= 0:
        return np.nan, np.nan
    nz = r > 0
    bits_spk = (p[nz] * r[nz] / mr * np.log2(r[nz] / mr)).sum()
    return float(bits_spk), float(bits_spk * mr)


def coherence(rmap):
    """Muller and Kubie (1989) coherence: z of the correlation between each visited bin's rate
    and the mean of its visited neighbours [standard measure; Table S1 "map coherence (z)"]."""
    r = rmap
    ok = np.isfinite(r)
    rz = np.where(ok, r, 0.0); w = ok.astype(float)
    k = np.ones((3, 3)); k[1, 1] = 0
    s = ndimage.convolve(rz, k, mode="constant"); c = ndimage.convolve(w, k, mode="constant")
    use = ok & (c > 0)
    if use.sum() < 10:
        return np.nan
    nb = s[use] / c[use]
    rr = np.corrcoef(r[use], nb)[0, 1]
    return float(np.arctanh(np.clip(rr, -0.999999, 0.999999)))


def rate_change(a, b):
    """Delta(A,B)/max(A,B) [claims M4; STAR Methods, Firing rate stability], signed (B - A)."""
    m = max(a, b)
    return np.nan if m <= 0 else (b - a) / m


# --------------------------------------------------------------------------- binning
def bin_counts(spike_sample, n_samples, step):
    """Spike counts in bins of ``step`` position samples (4 samples = 133 ms at 30 Hz)."""
    nb = n_samples // step
    s = spike_sample[spike_sample < nb * step] // step
    return np.bincount(s, minlength=nb)


def bin_counts_time(spike_times, t_start, t_end, width):
    """Spike counts in bins of ``width`` (100-us units) from t_start to t_end."""
    edges = np.arange(t_start, t_end + 1, width)
    return np.histogram(spike_times, edges)[0]


def kendall(a, b):
    """Kendall's tau-b between two count series [claims M9, standard choice tau-b, all bins]."""
    if np.std(a) == 0 or np.std(b) == 0:
        return np.nan
    return float(stats.kendalltau(a, b).statistic)


def tau_sd_six(a, b):
    """SD of tau over the earlier session cut into six equal periods [claims M9; STAR Methods,
    Cell pair spike train discharge correlations]; sample SD (ddof 1) [standard]."""
    n = len(a) // 6
    v = [kendall(a[i * n:(i + 1) * n], b[i * n:(i + 1) * n]) for i in range(6)]
    v = np.array(v, float)
    return float(np.nanstd(v, ddof=1)) if np.isfinite(v).sum() >= 3 else np.nan


# --------------------------------------------------------------------------- positional information
def ipos_series(counts, loc, valid):
    """Momentary positional information per 133-ms step [claims M6; STAR Methods, Positional
    information]: |p(n|x) log2(p(n|x)/p(n))| with n the count in the step and x its location,
    probabilities over the session. Steps without a location are NaN."""
    out = np.full(len(counts), np.nan)
    c = counts[valid]; l = loc[valid]
    if len(c) == 0:
        return out
    cmax = int(c.max())
    pn = np.bincount(c, minlength=cmax + 1) / len(c)
    key = l.astype(np.int64) * (cmax + 1) + c
    joint = np.bincount(key, minlength=(l.max() + 1) * (cmax + 1)).astype(float)
    nx = np.bincount(l, minlength=l.max() + 1).astype(float)
    pnx = joint[key] / nx[l]
    out[valid] = np.abs(pnx * np.log2(pnx / pn[c]))
    return out


# --------------------------------------------------------------------------- overdispersion
def standardized_rates(spike_sample, x, y, fs, rmap_full, mean_rate, occ, starts, win,
                       min_occ=0.67):
    """z = (obs - exp)/sqrt(exp) for windows of ``win`` samples starting at ``starts``, with
    exp = sum over the window of rate x time [claims M10; STAR Methods, Overdispersion].
    A window enters when exp exceeds the cell's average rate times the window length (read as
    "exp was greater than the average firing of the cell") and all its bins were sampled more
    than 0.67 s."""
    v = tracked(x, y)
    bx = np.clip(x // BIN_PX, 0, NBIN - 1); by = np.clip(y // BIN_PX, 0, NBIN - 1)
    r = np.nan_to_num(rmap_full[by, bx], nan=0.0)
    okbin = occ[by, bx] > min_occ
    cnt = np.bincount(spike_sample, minlength=len(x))
    z = []; idx = []
    for s0 in starts:
        sl = slice(s0, s0 + win)
        vv = v[sl]
        if vv.sum() < 0.8 * win:
            continue
        if not okbin[sl][vv].all():
            continue
        exp = (r[sl][vv]).sum() / fs
        if exp <= mean_rate * (win / fs):
            continue
        obs = cnt[sl][vv].sum()
        z.append((obs - exp) / np.sqrt(exp)); idx.append(s0)
    return np.array(z), np.array(idx, dtype=int)


# --------------------------------------------------------------------------- loaders
def _unit_path(idx, session, tetrode, cluster, frame, env):
    r = idx[(idx.session == session) & (idx.tetrode == tetrode) & (idx.cluster == cluster)
            & (idx.frame == frame) & (idx.env == env)]
    return None if r.empty else r.path.iloc[0]


def load_avoidance(idx=None):
    """Positions in both frames for every place avoidance session, and the spike samples of the
    paper's 42 place cells and 21 putative interneurons in each session where a file exists."""
    idx = ts_index() if idx is None else idx
    ses = avoidance_sessions(idx)
    pcs = class_list("DGPlaceCellsPlaceAvoidanceTask"); pcs["cls"] = "pc"
    ins = class_list("DGPutativeInterneuronsPlaceAvoidanceTask"); ins["cls"] = "int"
    cells = pd.concat([pcs, ins], ignore_index=True).rename(columns={"day": "mouse"})
    out = {}
    for _, s in ses.iterrows():
        mine = cells[cells.mouse == s.mouse]
        units = {}
        pos = None
        for _, c in mine.iterrows():
            p = _unit_path(idx, s.session, c.tetrode, c.cluster, "Rm", False)
            if p is None:
                continue
            d = parse_ts(read(p))
            if pos is None:
                pos = dict(fs=d["fs"], t0=d["t0"], rx=d["x"], ry=d["y"])
                pa = _unit_path(idx, s.session, c.tetrode, c.cluster, "Ar", False)
                a = parse_ts(read(pa))
                pos["ax"], pos["ay"] = a["x"], a["y"]
                pos["n_ar_spikes_equal"] = bool(np.array_equal(a["spike_sample"], d["spike_sample"]))
            elif not np.array_equal(pos["rx"], d["x"]):
                pos.setdefault("mismatch", []).append(p)
            units[(c.mouse, c.tetrode, c.cluster)] = dict(cls=c.cls, spike_sample=d["spike_sample"],
                                                          spike_times=d["spike_times"])
        out[s.session] = dict(meta=s.to_dict(), pos=pos, units=units)
    return ses, cells, out


def load_environment(idx=None):
    """Positions and spike samples of the paper's 45 DG and 20 CA place cells in every
    environment session of their day."""
    idx = ts_index() if idx is None else idx
    ses = env_sessions(idx)
    dg = class_list("DGPlaceCellsEnvironmentalChangesTask"); dg["region"] = "DG"
    ca = class_list("CAPlaceCellsEnvironmentalChangesTask"); ca["region"] = "CA"
    cells = pd.concat([dg, ca], ignore_index=True)
    out = {}
    for _, s in ses[ses.day.isin(cells.day)].iterrows():
        mine = cells[cells.day == s.day]
        units = {}; pos = None
        for _, c in mine.iterrows():
            p = _unit_path(idx, s.session, c.tetrode, c.cluster, "Rm", True)
            if p is None:
                continue
            d = parse_ts(read(p))
            if pos is None:
                pos = dict(fs=d["fs"], t0=d["t0"], rx=d["x"], ry=d["y"])
            elif not np.array_equal(pos["rx"], d["x"]):
                pos.setdefault("mismatch", []).append(p)
            units[(c.day, c.tetrode, c.cluster)] = dict(region=c.region, spike_sample=d["spike_sample"],
                                                        spike_times=d["spike_times"])
        out[s.session] = dict(meta=s.to_dict(), pos=pos, units=units)
    return ses, cells, out


# --------------------------------------------------------------------------- statistics
# The paper's tests [claims M12; STAR Methods, Quantification and Statistical Analysis]: one-,
# two- and three-way ANOVAs, Kruskal-Wallis, Welch's ANOVA, Fisher's LSD post hoc, two-tailed,
# alpha 0.05. JMP's mixed models (fractional df) are approximated by statsmodels' MixedLM with
# Wald F tests on the fixed effects, with the residual df as denominator [assumption: JMP's
# Kenward-Roger df cannot be rebuilt here; the F values are comparable, the df are not].
def anova2(df, y, a, b):
    """Two-way ANOVA with sum-to-zero contrasts, type III sums of squares (JMP's default)."""
    import statsmodels.formula.api as smf
    from statsmodels.stats.anova import anova_lm
    d = df[[y, a, b]].dropna()
    m = smf.ols(f"{y} ~ C({a}, Sum) * C({b}, Sum)", data=d).fit()
    t = anova_lm(m, typ=3).drop(index="Intercept")
    t.index = [a, b, f"{a} x {b}", "Residual"]
    return t, m


def anova1(groups):
    """One-way ANOVA, Welch's ANOVA and Kruskal-Wallis on a list of arrays."""
    g = [np.asarray(v, float)[np.isfinite(v)] for v in groups]
    f = stats.f_oneway(*g)
    kw = stats.kruskal(*g)
    k = len(g); n = np.array([len(v) for v in g]); m = np.array([v.mean() for v in g])
    s2 = np.array([v.var(ddof=1) for v in g]); w = n / s2
    mw = (w * m).sum() / w.sum()
    a1 = (w * (m - mw) ** 2).sum() / (k - 1)
    lam = ((1 - w / w.sum()) ** 2 / (n - 1)).sum()
    fw = a1 / (1 + 2 * (k - 2) / (k * k - 1) * lam)
    df2 = (k * k - 1) / (3 * lam)
    pw = stats.f.sf(fw, k - 1, df2)
    lev = stats.levene(*g)
    return dict(F=f.statistic, p=f.pvalue, df=(k - 1, int(n.sum() - k)), welch_F=fw, welch_df2=df2,
                welch_p=pw, H=kw.statistic, kw_p=kw.pvalue, levene_p=lev.pvalue, n=n.tolist(),
                means=m.tolist())


def lsd(groups, names, mse=None, df=None):
    """Fisher's LSD: unadjusted pairwise t tests with the pooled error of the ANOVA."""
    g = [np.asarray(v, float)[np.isfinite(v)] for v in groups]
    if mse is None:
        g = [v for v in g]
        df = sum(len(v) for v in g if len(v)) - sum(1 for v in g if len(v))
        mse = sum(((v - v.mean()) ** 2).sum() for v in g if len(v)) / df
    rows = []
    for i in range(len(g)):
        for j in range(i + 1, len(g)):
            if len(g[i]) < 2 or len(g[j]) < 2:
                continue
            d = g[i].mean() - g[j].mean()
            se = np.sqrt(mse * (1 / len(g[i]) + 1 / len(g[j])))
            t = d / se
            rows.append(dict(a=names[i], b=names[j], diff=d, t=t, p=2 * stats.t.sf(abs(t), df)))
    return pd.DataFrame(rows)


def lsd_ranks(groups, names):
    """Fisher's LSD on ranks: the LSD of the pooled ranks [claims M12, two-way ANOVA on ranks
    and Kruskal-Wallis as the non-parametric forms]."""
    g = [np.asarray(v, float)[np.isfinite(v)] for v in groups]
    r = stats.rankdata(np.concatenate(g))
    cut = np.cumsum([0] + [len(v) for v in g])
    return lsd([r[cut[i]:cut[i + 1]] for i in range(len(g))], names)


def mixed_terms(df, formula, group, terms):
    """Wald F tests of fixed-effect terms in a linear mixed model (random intercept per
    ``group``). ``terms`` maps a label to the substring that names its parameters."""
    import statsmodels.formula.api as smf
    d = df.dropna()
    import warnings
    m, err = None, None
    for meth in ("lbfgs", "powell", "nm", "bfgs"):
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                m = smf.mixedlm(formula, d, groups=d[group]).fit(reml=True, method=meth)
            if np.all(np.isfinite(m.bse_fe)):
                break
        except Exception as e:  # singular fits: try the next optimiser
            err = e
    if m is None:
        raise err
    fe = m.fe_params.index.tolist()
    rows = []
    for lab, key in terms.items():
        idx = [i for i, n in enumerate(fe) if all(k in n for k in key.split("&")) and
               (":" in n) == ("&" in key)]
        L = np.zeros((len(idx), len(m.params)))
        for r, i in enumerate(idx):
            L[r, i] = 1
        w = m.wald_test(L, scalar=True, use_f=True)
        rows.append(dict(term=lab, F=float(np.squeeze(w.statistic)), df1=len(idx),
                         df2=float(np.squeeze(w.df_denom)), p=float(np.squeeze(w.pvalue))))
    return pd.DataFrame(rows), m


def prop_ztest(k1, n1, k2, n2):
    """Two-sample z test of proportions, pooled variance, two-sided."""
    p1, p2 = k1 / n1, k2 / n2
    p = (k1 + k2) / (n1 + n2)
    se = np.sqrt(p * (1 - p) * (1 / n1 + 1 / n2))
    z = (p1 - p2) / se if se > 0 else np.nan
    return float(z), float(2 * stats.norm.sf(abs(z)))


def rm_multivariate(Y):
    """Multivariate repeated-measures F test (Hotelling's T2 on successive differences) for an
    n x k array; df (k-1, n-k+1), JMP's default for a within-subject factor."""
    Y = np.asarray(Y, float)
    n, k = Y.shape
    D = Y[:, 1:] - Y[:, :1]
    mu = D.mean(0); S = np.cov(D, rowvar=False)
    t2 = n * mu @ np.linalg.solve(S, mu)
    F = (n - k + 1) / ((n - 1) * (k - 1)) * t2
    return float(F), (k - 1, n - k + 1), float(stats.f.sf(F, k - 1, n - k + 1))


def rm_univariate(Y):
    """Univariate one-way repeated-measures ANOVA on an n x k array."""
    Y = np.asarray(Y, float); n, k = Y.shape
    gm = Y.mean()
    ss_c = n * ((Y.mean(0) - gm) ** 2).sum()
    ss_s = k * ((Y.mean(1) - gm) ** 2).sum()
    ss_e = ((Y - gm) ** 2).sum() - ss_c - ss_s
    df1, df2 = k - 1, (k - 1) * (n - 1)
    F = (ss_c / df1) / (ss_e / df2)
    return float(F), (df1, df2), float(stats.f.sf(F, df1, df2))
