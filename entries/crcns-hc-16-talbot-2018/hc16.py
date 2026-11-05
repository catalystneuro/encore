"""Loading and measures for CRCNS hc-16 (Talbot et al. 2018, Neuron 97:684).

The data set is one zip, `hc-16/live/data.zip`, in the public CRCNS bucket. It is read in place
over range requests (fsspec and zipfile); nothing is written to disk. CRCNS data sets are not
versioned, so the files read are pinned by the MD5 sums of `hc-16/live/checksums.md5`, which
`check_md5_list` reads and the notebook prints.

Where each parameter comes from:

- Rate maps on 1.25 x 1.25 cm pixels, overall rate, coherence, information content, proportion of
  active pixels, place cell criteria (rate 0.1-2 AP/s, coherence z > 0.4, information > 0.4
  bits/spike): STAR Methods, "Characterization of Place Cells", as the claims file's opening
  comment gives them. Unsmoothed maps and pixels with any occupancy: the claims file's standard
  choice.
- Cell classes: STAR Methods, "Classification of Cell Types" (rate below or above 2 AP/s, bursts
  with peak ISI below 10 ms). The data hold no waveforms, so width is not used (the variant the
  claims file names for interneuron-proportion). The peak ISI is the mode of the ISI histogram in
  1 ms bins up to 500 ms: a standard choice, as the paper gives no binning.
- Cluster 0 of each tetrode is left out: it holds the unsorted spikes (rates near 40 AP/s), and the
  paper's code drops it (claims file, opening comment, SpikeField and
  CorrelateBPFSpikeTrainEpisodes).
- The spatial scale is not in the data set. It is taken from the extent of the tracked positions
  in the room frame and the enclosure sizes of the STAR Methods ("Constant Conditions Open-Field
  and Disk Rotation": large box 50 cm, disk-shaped arena 40 cm): an assumption, stated in the
  notebook.
- Passes and overdispersion z: STAR Methods, "Overdispersion" (5 s intervals, exp from the
  time-averaged rate map, pass when exp >= the cell's average rate, z = (obs - exp)/sqrt(exp)).
  Consecutive non-overlapping intervals from the session start: the claims file's reading.
- Kendall tau-b between spike counts: STAR Methods, "Functional Coupling of Cell Pairs", and the
  claims file (readings K1, every bin, and K2, the code's active-pixel gate on 32 x 32 maps).
- Ipos: STAR Methods, "Frame-Specific Spatial Firing Analysis", Equation 1, with 133 ms intervals,
  and the claims file (PositionalInfo code: 32 x 32 maps, pixels with fewer than 10 visits left
  out). An interval is four position samples at 30 Hz (133 ms); its location is that of its first
  sample, a standard choice.
"""

from __future__ import annotations

import re
import threading
from concurrent.futures import ThreadPoolExecutor

import fsspec
import numpy as np
import pandas as pd
import zipfile
from scipy import ndimage, stats

BUCKET = "https://crcnsarchive.s3-us-west-2.amazonaws.com/hc-16/live"
DATASET = "crcns:hc-16/unversioned"
DOI = "10.6080/K01V5C44"
DATA_ZIP = f"{BUCKET}/data.zip"
DATA_ZIP_MD5 = "45b534dd6dbeb94db539bc429223eecb"  # from checksums.md5, read and checked below

ENV_SIZE_CM = {"big_box": 50.0, "stationary_cylinder": 40.0, "rotating_cylinder": 40.0}
PIXEL_CM = 1.25
TIMESCALES = [0.025, 0.040, 0.125, 0.250, 1.0, 5.0]

NAME = re.compile(
    r"data/(?P<env>\w+)/(?P<geno>WT|KO)/(?P<mouse>M\d+)_(?P<date>\d+)_(?P<cond>\w+?)-(?P<cut>cl\w+)"
    r"-fix(?P<part>_\d+-\d+min)?\.(?P<unit>P\d+C\d+|0spks)(?P<frame>Rm|Ar)?(?P<times>\.times)?$")


def check_md5_list():
    """The bucket's checksums.md5, as a dict of file name to MD5."""
    with fsspec.open(f"{BUCKET}/checksums.md5", "rt") as f:
        return {l.split()[1]: l.split()[0] for l in f if l.strip()}


def open_zip():
    return zipfile.ZipFile(fsspec.open(DATA_ZIP, block_size=2**22).open())


def list_members(z):
    """Every file of the zip with the parts of its name."""
    rows = []
    for info in z.infolist():
        m = NAME.match(info.filename)
        if m:
            rows.append(dict(m.groupdict(), name=info.filename, size=info.file_size))
    df = pd.DataFrame(rows)
    df["part"] = df["part"].fillna("full")
    df["frame"] = df["frame"].fillna("pos")
    df["times"] = df["times"].notna()
    df["genotype"] = df["geno"].map({"WT": "WT", "KO": "Fmr1-null"})
    return df


def parse_ts(b):
    """Decode a TS file (data descriptor, "Data format"): ASCII header, then per position sample
    x (1 byte), y (1 byte), n spikes (1 byte) and n spike times (4 bytes each, 100 us units)."""
    i = b.find(b"%%ENDHEADER")
    hdr = b[:i].decode("latin1")
    rate = float(re.search(r"SAMPLING_INTERVAL\(samps/sec\)\s+([\d.]+)", hdr).group(1))
    t0 = int(re.search(r"FIRST_TIMESTAMP\(100usUnits\)\s+(\d+)", hdr).group(1))
    body = b[b.find(b"\n", i) + 1:]
    starts, p, L = [], 0, len(body)
    while p + 3 <= L:
        starts.append(p)
        p += 3 + 4 * body[p + 2]
    st = np.array(starts)
    a = np.frombuffer(body, np.uint8)
    n = a[st + 2].astype(np.int64)
    if n.sum():
        k = np.arange(n.sum()) - np.repeat(np.cumsum(n) - n, n)
        s = np.repeat(st + 3, n) + 4 * k
        spk = (a[s].astype(np.int64) | a[s + 1].astype(np.int64) << 8
               | a[s + 2].astype(np.int64) << 16 | a[s + 3].astype(np.int64) << 24)
    else:
        spk = np.zeros(0, np.int64)
    return dict(rate=rate, t0=t0, x=a[st].copy(), y=a[st + 1].copy(), n=n, spk=spk, leftover=L - p)


def read_members(names, workers=8):
    """Parse TS files from the zip, several at a time, each thread with its own handle."""
    local = threading.local()

    def one(name):
        if not hasattr(local, "z"):
            local.z = open_zip()
        return name, parse_ts(local.z.read(name))

    with ThreadPoolExecutor(workers) as ex:
        return dict(ex.map(one, names))


class Session:
    """One recording: positions per frame, and spike counts per position sample per cluster."""

    def __init__(self, key, rows, parsed):
        self.env, self.genotype, self.mouse, self.date, self.cond, self.cut = key
        self.id = f"{self.mouse}_{self.date}_{self.cond}"
        first = parsed[rows.iloc[0]["name"]]
        self.rate = first["rate"]
        self.t0 = first["t0"]
        self.frames = {}
        self.counts = {}
        self.spikes = {}
        self.leftover = 0
        for _, r in rows.iterrows():
            d = parsed[r["name"]]
            self.leftover += d["leftover"]
            if r["unit"] == "0spks":
                continue
            fr = r["frame"]
            if fr not in self.frames:
                self.frames[fr] = (d["x"].astype(float), d["y"].astype(float))
            if fr == "Rm":
                self.counts[r["unit"]] = d["n"]
                self.spikes[r["unit"]] = d["spk"]
        self.nsamp = len(self.frames["Rm"][0])
        self.duration = self.nsamp / self.rate
        x, y = self.frames["Rm"]
        self.tracked = (x > 0) | (y > 0)
        lo = np.percentile(np.c_[x[self.tracked], y[self.tracked]], 0.1, axis=0)
        hi = np.percentile(np.c_[x[self.tracked], y[self.tracked]], 99.9, axis=0)
        self.extent_px = hi - lo
        self.px_per_cm = float(np.mean(self.extent_px) / ENV_SIZE_CM[self.env])
        self.sample_time = self._sample_time()
        self.cells = sorted((u for u in self.counts if not u.endswith("C0")),
                            key=lambda u: tuple(int(v) for v in re.findall(r"\d+", u)))

    def _sample_time(self):
        """Time (s, file clock) of each position sample. The stated sampling rate drifts against
        the spike clock and frames are dropped, so the nominal time t0 + k/rate can be seconds off
        the spikes filed under sample k. The offset of every spike (all clusters, cluster 0
        included) from its sample's nominal time is smoothed with a running median over 301
        samples (10 s) and added to the nominal time."""
        k = np.concatenate([np.repeat(np.arange(self.nsamp), n) for n in self.counts.values()])
        sp = np.concatenate([self.spikes[u] for u in self.counts]) / 1e4
        nominal = self.t0 / 1e4 + np.arange(self.nsamp) / self.rate
        off = sp - nominal[k]
        o = pd.Series(off).groupby(k).median().reindex(np.arange(self.nsamp))
        o = o.rolling(301, center=True, min_periods=1).median().interpolate(limit_direction="both")
        return nominal + o.to_numpy() - 0.5 / self.rate

    def __repr__(self):
        return f"Session({self.id}, {self.genotype}, {self.env}, {len(self.cells)} cells)"

    def tracked_in(self, frame):
        x, y = self.frames[frame]
        return (x > 0) | (y > 0)


def load_sessions(df):
    """Read every full-length session (not the 0-15 and 15-30 min copies) of the zip."""
    use = df[(df["part"] == "full") & ~df["times"] & df["frame"].isin(["Rm", "Ar", "pos"])]
    parsed = read_members(list(use["name"]))
    sessions = []
    for key, rows in use.groupby(["env", "genotype", "mouse", "date", "cond", "cut"]):
        sessions.append(Session(key, rows, parsed))
    order = {"big_box": 0, "stationary_cylinder": 1, "rotating_cylinder": 2}
    sessions.sort(key=lambda s: (s.genotype, s.mouse, s.date, s.cond, order[s.env]))
    return sessions


# ---------------------------------------------------------------- rate maps and single-cell measures

def pixel_index(s, frame="Rm", pixel_cm=PIXEL_CM):
    """Map pixel of each position sample (-1 when untracked), on a grid in cm from the room-frame
    extent. Returns (index, shape)."""
    x, y = s.frames[frame]
    ok = s.tracked_in(frame)
    size = pixel_cm * s.px_per_cm
    nb = int(np.ceil(256 / size))
    ix = np.clip((x / size).astype(int), 0, nb - 1)
    iy = np.clip((y / size).astype(int), 0, nb - 1)
    idx = np.where(ok, iy * nb + ix, -1)
    return idx, (nb, nb)


def pixel_index_code(s, frame="Rm", nbins=32):
    """Pixel on the code's 32 x 32 map of the 256 x 256 tracker frame (8 tracker pixels each)."""
    x, y = s.frames[frame]
    ok = s.tracked_in(frame)
    w = 256 // nbins
    idx = np.where(ok, (y.astype(int) // w) * nbins + x.astype(int) // w, -1)
    return idx, (nbins, nbins)


def occupancy(s, idx, shape):
    occ = np.bincount(idx[idx >= 0], minlength=shape[0] * shape[1]) / s.rate
    return occ


def rate_map(s, cell, idx, shape, occ=None):
    """Spikes in each pixel over the time spent there (NaN where unvisited)."""
    if occ is None:
        occ = occupancy(s, idx, shape)
    n = s.counts[cell]
    sp = np.bincount(idx[idx >= 0], weights=n[idx >= 0], minlength=shape[0] * shape[1])
    with np.errstate(invalid="ignore", divide="ignore"):
        r = np.where(occ > 0, sp / occ, np.nan)
    return r.reshape(shape), occ.reshape(shape)


def coherence(rm):
    """Muller and Kubie (1989): Fisher z of the correlation between each visited pixel's rate and
    the mean rate of its visited neighbours (up to 8)."""
    v = ~np.isnan(rm)
    r0 = np.where(v, rm, 0.0)
    k = np.ones((3, 3)); k[1, 1] = 0
    s = ndimage.convolve(r0, k, mode="constant")
    c = ndimage.convolve(v.astype(float), k, mode="constant")
    ok = v & (c > 0)
    a, b = rm[ok], s[ok] / c[ok]
    if ok.sum() < 3 or a.std() == 0 or b.std() == 0:
        return np.nan
    r = np.corrcoef(a, b)[0, 1]
    return float(np.arctanh(min(r, 0.999999)))


def information(rm, occ):
    """Skaggs et al. (1993) information content in bits/spike."""
    v = ~np.isnan(rm)
    p = occ[v] / occ[v].sum()
    r = rm[v]
    mean = (p * r).sum()
    if mean <= 0:
        return np.nan
    nz = r > 0
    return float((p[nz] * r[nz] / mean * np.log2(r[nz] / mean)).sum())


def active_fraction(rm):
    v = ~np.isnan(rm)
    return float((rm[v] > 0).mean())


def fields(rm, occ, threshold, min_pixels=9):
    """Place fields as 4-connected visited pixels with rate above threshold, at least min_pixels.
    Returns the number of fields and the in-field rate (spikes over time in the fields)."""
    v = ~np.isnan(rm)
    above = v & (np.nan_to_num(rm) > threshold)
    lab, n = ndimage.label(above)
    keep = np.zeros_like(above)
    nf = 0
    for i in range(1, n + 1):
        m = lab == i
        if m.sum() >= min_pixels:
            keep |= m
            nf += 1
    if nf == 0:
        return 0, np.nan
    return nf, float((rm[keep] * occ[keep]).sum() / occ[keep].sum())


def isi_measures(spk):
    """Burst probability (fraction of ISIs below 10 ms), mean and median ISI (s), and the peak of
    the ISI histogram (1 ms bins to 500 ms, in ms)."""
    isi = np.diff(np.sort(spk)) / 1e4
    if len(isi) < 2:
        return np.nan, np.nan, np.nan, np.nan
    h, e = np.histogram(isi * 1e3, bins=np.arange(0, 501, 1))
    peak = e[np.argmax(h)] + 0.5 if h.sum() else np.nan
    return float((isi < 0.010).mean()), float(isi.mean()), float(np.median(isi)), float(peak)


def cell_table(sessions):
    """One row per cluster per session, with the single-cell measures on 1.25 cm room-frame maps."""
    rows = []
    for s in sessions:
        idx, shape = pixel_index(s, "Rm")
        occ = occupancy(s, idx, shape)
        for c in s.cells:
            rm, o = rate_map(s, c, idx, shape, occ)
            nsp = int(s.counts[c].sum())
            rate = nsp / s.duration
            burst, isi_mean, isi_med, peak = isi_measures(s.spikes[c])
            v = ~np.isnan(rm)
            mean_map = float(np.nansum(rm * o) / o[v].sum())
            peak_rate = float(np.nanmax(rm)) if v.any() else np.nan
            nf_a, inf_a = fields(rm, o, mean_map)
            nf_b, inf_b = fields(rm, o, 0.2 * peak_rate)
            rows.append(dict(
                session=s.id, env=s.env, genotype=s.genotype, mouse=s.mouse, date=s.date,
                cond=s.cond, cut=s.cut, cell=c, cell_key=f"{s.mouse}_{s.date}_{s.cut}_{c}",
                spikes=nsp, rate=rate, burst_prob=burst, isi_mean=isi_mean, isi_median=isi_med,
                isi_peak_ms=peak, coherence=coherence(rm), info=information(rm, o),
                active=active_fraction(rm), nfields_mean=nf_a, infield_mean=inf_a,
                nfields_20pk=nf_b, infield_20pk=inf_b))
    t = pd.DataFrame(rows)
    return t


def classify(t, use_burst=True):
    """Interneuron: rate above 2 AP/s. Pyramidal: rate below 2 AP/s and (when use_burst) ISI peak
    below 10 ms; other clusters are left unclassified. Place cell: pyramidal with rate 0.1-2 AP/s,
    coherence above 0.4 and information above 0.4 bits/spike; other pyramidal cells are
    non-spatial."""
    pyr = t["rate"] < 2
    if use_burst:
        pyr &= t["isi_peak_ms"] < 10
    cls = np.where(t["rate"] > 2, "interneuron", np.where(pyr, "pyramidal", "unclassified"))
    place = pyr & (t["rate"] >= 0.1) & (t["coherence"] > 0.4) & (t["info"] > 0.4)
    cls = np.where(place, "place", np.where(cls == "pyramidal", "nonspatial", cls))
    return pd.Series(cls, index=t.index)


# ---------------------------------------------------------------- overdispersion

def passes(s, cell, window_s=5.0, step_s=None, idx_shape=None):
    """5 s intervals: obs, exp and whether each is a pass (exp >= the cell's average rate).
    Intervals are consecutive from the session start, or start every step_s seconds."""
    idx, shape = idx_shape if idx_shape is not None else pixel_index(s, "Rm")
    rm, occ = rate_map(s, cell, idx, shape)
    r = np.nan_to_num(rm.ravel())
    dt = 1.0 / s.rate
    per_sample_exp = np.where(idx >= 0, r[np.clip(idx, 0, None)] * dt, 0.0)
    n = s.counts[cell].astype(float)
    w = int(round(window_s * s.rate))
    step = w if step_s is None else int(round(step_s * s.rate))
    starts = np.arange(0, s.nsamp - w + 1, step)
    ce = np.r_[0, np.cumsum(per_sample_exp)]
    co = np.r_[0, np.cumsum(n)]
    exp = ce[starts + w] - ce[starts]
    obs = co[starts + w] - co[starts]
    avg = n.sum() / s.duration
    ok = exp >= avg
    with np.errstate(invalid="ignore", divide="ignore"):
        z = np.where(exp > 0, (obs - exp) / np.sqrt(exp), np.nan)
    return dict(start=starts, obs=obs, exp=exp, z=z, is_pass=ok & (exp > 0))


# ---------------------------------------------------------------- Kendall correlation

def bin_counts(spk, t_start, t_stop, width):
    """Spike counts in bins of width seconds from t_start to t_stop (seconds from the file clock)."""
    edges = np.arange(t_start, t_stop + 1e-9, width)
    return np.histogram(spk / 1e4, bins=edges)[0], edges


def kendall_tau_b(a, b):
    """Kendall tau-b of two integer series, from their contingency table (exact, ties corrected)."""
    a = np.asarray(a); b = np.asarray(b)
    if len(a) < 3:
        return np.nan
    ka, kb = int(a.max()) + 1, int(b.max()) + 1
    tab = np.bincount(a * kb + b, minlength=ka * kb).reshape(ka, kb).astype(float)
    tab = tab[tab.sum(1) > 0][:, tab.sum(0) > 0]
    if tab.shape[0] < 2 or tab.shape[1] < 2:
        return np.nan
    # concordant: pairs with both larger; discordant: one larger, one smaller
    cum = tab[::-1, ::-1].cumsum(0).cumsum(1)[::-1, ::-1]  # sum of tab[k>=i, l>=j]
    below_right = np.zeros_like(tab)
    below_right[:-1, :-1] = cum[1:, 1:]
    conc = (tab * below_right).sum()
    cum2 = tab[::-1, :].cumsum(0)[::-1, :].cumsum(1)  # sum of tab[k>=i, l<=j]
    below_left = np.zeros_like(tab)
    below_left[:-1, 1:] = cum2[1:, :-1]
    disc = (tab * below_left).sum()
    n = len(a)
    n0 = n * (n - 1) / 2
    ra = tab.sum(1); rb = tab.sum(0)
    t1 = (ra * (ra - 1) / 2).sum(); t2 = (rb * (rb - 1) / 2).sum()
    den = np.sqrt((n0 - t1) * (n0 - t2))
    return float((conc - disc) / den) if den > 0 else np.nan


def session_bins(s, width, t_start=None, t_stop=None):
    """Bin edges in seconds of the file clock, from t_start to t_stop seconds after the first
    position sample, and the position sample at each bin centre (from Session.sample_time)."""
    t0 = s.sample_time[0]
    a = t0 if t_start is None else t0 + t_start
    b = s.sample_time[-1] + 1 / s.rate if t_stop is None else t0 + t_stop
    nb = int(np.floor((b - a) / width + 1e-9))
    edges = a + width * np.arange(nb + 1)
    centres = (edges[:-1] + edges[1:]) / 2
    sample = np.clip(np.searchsorted(s.sample_time, centres) - 1, 0, s.nsamp - 1)
    return edges, sample


def active_pixels(s, cell, idx32, shape32):
    """Pixels of the code's 32 x 32 map where the cell's rate is at least its mean rate."""
    rm, occ = rate_map(s, cell, idx32, shape32)
    mean = s.counts[cell].sum() / s.duration
    return np.nan_to_num(rm.ravel(), nan=-1) >= mean


def pair_taus(s, cells, widths=TIMESCALES, periods=None, gate=False, mask_fn=None):
    """Tau for every pair of cells, per timescale and period. periods: dict name -> (start, stop)
    in seconds from the session start. gate: K2, keep bins where the mouse is in an active pixel
    of both cells. mask_fn(s, sample) -> boolean array of bins to keep (e.g. low speed)."""
    if periods is None:
        periods = {"session": (None, None)}
    idx32, shape32 = pixel_index_code(s, "Rm")
    act = {c: active_pixels(s, c, idx32, shape32) for c in cells} if gate else None
    rows = []
    for pname, (a, b) in periods.items():
        for w in widths:
            edges, sample = session_bins(s, w, a, b)
            if len(edges) < 4:
                continue
            counts = {c: np.histogram(s.spikes[c] / 1e4, bins=edges)[0] for c in cells}
            keep_base = np.ones(len(sample), bool) if mask_fn is None else mask_fn(s, sample)
            pix = idx32[sample]
            for i in range(len(cells)):
                for j in range(i + 1, len(cells)):
                    keep = keep_base.copy()
                    if gate:
                        ok = pix >= 0
                        keep &= ok & act[cells[i]][np.clip(pix, 0, None)] & act[cells[j]][np.clip(pix, 0, None)]
                    tau = kendall_tau_b(counts[cells[i]][keep], counts[cells[j]][keep])
                    rows.append(dict(session=s.id, genotype=s.genotype, mouse=s.mouse,
                                     a=cells[i], b=cells[j], period=pname, width=w,
                                     nbins=int(keep.sum()), tau=tau))
    return pd.DataFrame(rows)


# ---------------------------------------------------------------- locomotion

def speed(s, window_s=1.0):
    """Speed in cm/s per position sample, from room-frame positions smoothed over window_s
    (a standard choice); NaN where untracked."""
    x, y = s.frames["Rm"]
    ok = s.tracked
    xs = pd.Series(np.where(ok, x, np.nan)).interpolate(limit_area="inside")
    ys = pd.Series(np.where(ok, y, np.nan)).interpolate(limit_area="inside")
    w = max(1, int(round(window_s * s.rate)))
    xs = xs.rolling(w, center=True, min_periods=1).mean().to_numpy()
    ys = ys.rolling(w, center=True, min_periods=1).mean().to_numpy()
    v = np.hypot(np.gradient(xs), np.gradient(ys)) * s.rate / s.px_per_cm
    v[~ok] = np.nan
    return v


# ---------------------------------------------------------------- positional information

def ipos_series(s, cell, frame, samples_per_bin=4, min_visits=10, signed=False, log=np.log2):
    """Ipos per 133 ms interval: |p(i|x) log2(p(i|x)/p(i))| for the count i observed at the
    interval's location x on the code's 32 x 32 map of the frame; NaN where x is untracked or
    visited in fewer than min_visits intervals."""
    idx32, shape32 = pixel_index_code(s, frame)
    nb = s.nsamp // samples_per_bin
    n = s.counts[cell][:nb * samples_per_bin].reshape(nb, samples_per_bin).sum(1)
    x = idx32[:nb * samples_per_bin:samples_per_bin]
    ok = x >= 0
    out = np.full(nb, np.nan)
    if ok.sum() == 0:
        return out
    ncount = int(n.max()) + 1
    joint = np.zeros((shape32[0] * shape32[1], ncount))
    np.add.at(joint, (x[ok], n[ok]), 1)
    visits = joint.sum(1)
    p_i = joint.sum(0) / joint.sum()
    with np.errstate(invalid="ignore", divide="ignore"):
        p_ix = joint / visits[:, None]
    xi = x[ok]; ni = n[ok]
    pix = p_ix[xi, ni]
    val = pix * log(pix / p_i[ni])
    val = np.where(visits[xi] >= min_visits, val, np.nan)
    out[ok] = val if signed else np.abs(val)
    return out


def fisher(r):
    return np.arctanh(np.clip(r, -0.999999, 0.999999))


# ---------------------------------------------------------------- statistics

def cohen_d(a, b):
    a = np.asarray(a, float); b = np.asarray(b, float)
    sp = np.sqrt(((len(a) - 1) * a.var(ddof=1) + (len(b) - 1) * b.var(ddof=1)) / (len(a) + len(b) - 2))
    return float((a.mean() - b.mean()) / sp) if sp > 0 else np.nan


def two_group(a, b, alternative="two-sided"):
    """Quantification section: t test, with Mann-Whitney U and Shapiro-Wilk normality reported."""
    a = np.asarray(a, float); a = a[~np.isnan(a)]
    b = np.asarray(b, float); b = b[~np.isnan(b)]
    t = stats.ttest_ind(a, b, alternative=alternative)
    u = stats.mannwhitneyu(a, b, alternative=alternative)
    sw_a = stats.shapiro(a).pvalue if len(a) >= 3 else np.nan
    sw_b = stats.shapiro(b).pvalue if len(b) >= 3 else np.nan
    normal = (sw_a >= 0.05) and (sw_b >= 0.05)
    return dict(n_a=len(a), n_b=len(b), mean_a=a.mean(), sem_a=stats.sem(a), mean_b=b.mean(),
                sem_b=stats.sem(b), t=t.statistic, df=len(a) + len(b) - 2, p_t=t.pvalue,
                U=u.statistic, p_U=u.pvalue, shapiro_a=sw_a, shapiro_b=sw_b,
                p_table=t.pvalue if normal else u.pvalue, test_table="t" if normal else "U",
                d=cohen_d(a, b))


def prop_test(k1, n1, k2, n2):
    """Pooled two-proportion z test; returns z and the two-sided p."""
    p = (k1 + k2) / (n1 + n2)
    se = np.sqrt(p * (1 - p) * (1 / n1 + 1 / n2))
    z = (k1 / n1 - k2 / n2) / se
    return float(z), float(2 * stats.norm.sf(abs(z)))


def anova2(df, y, a="genotype", b="cls"):
    """Two-way ANOVA (type II sums of squares) of y on a x b, with partial eta squared."""
    import statsmodels.formula.api as smf
    from statsmodels.stats.anova import anova_lm
    d = df[[y, a, b]].dropna()
    m = smf.ols(f"{y} ~ C({a}) * C({b})", data=d).fit()
    t = anova_lm(m, typ=2)
    t["eta_p2"] = t["sum_sq"] / (t["sum_sq"] + t.loc["Residual", "sum_sq"])
    return t
