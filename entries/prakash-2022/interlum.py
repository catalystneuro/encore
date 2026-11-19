"""Loading and measures for the in vivo Interluminescence data of dandiset 000935.

Prakash et al. (2022), Communications Biology 5, 33, doi:10.1038/s42003-021-02981-7.

Each NWB file holds one anaesthetised PV-Cre mouse: a 32-contact laminar recording
(`ElectricalSeries`, volts, float64, 10 kHz, stored contiguous and uncompressed), a 1 Hz
bioluminescence image series (`1pInternal`, absent for sub-interlum-6), and one interval in
`intervals/trials`, the start and stop of CTZ infusion. The group (Opsin (+) or Opsin (-)) is
the first word of the subject description. Files are streamed from the archive at the pinned
version by HTTP range requests on the datasets' byte offsets (the arrays are contiguous, so
each range is a block of time); nothing is written to disk.

Where the parameters come from. "Claims" means the opening comment of
claims/prakash-2022.yaml ("the in vivo pipeline") and its readings (o1) to (o7); "Methods"
means the paper's Methods, "Electrophysiology analysis", "Bioluminescence imaging analysis"
and "Statistical analysis".

- Errant contacts: RMS above Q3 + 3 IQR or below Q1 - 3 IQR of the 32 contacts (Methods).
  The RMS is taken over the whole recording; the paper does not say over which span (a
  standard choice; broken contacts stand out over any span). Quartiles by numpy's linear
  interpolation (standard choice; MATLAB's prctile is also computed and reported).
- Common average reference over the kept contacts (Methods).
- LFP: resampled from 10 kHz to 1 kHz with a polyphase anti-aliasing filter
  (`scipy.signal.resample_poly`, as MATLAB's `resample`; the paper says only "down sampled",
  a standard choice), 1 Hz high-pass, 3rd order Butterworth (Methods), zero-phase (claims, o7).
- Spectrogram: multitaper, time-bandwidth 3, 5 tapers, 10 s windows in 1 s steps, each
  zero-padded to 16384 samples (Methods, Chronux 2.11 `mtspecgramc`, whose tapers are DPSS
  scaled by sqrt(Fs), with no detrending); the window time is its centre, as in Chronux.
  P = 10 log10(A / B), B the mean power over the windows centred in the 180 s before onset
  (Methods). Gamma is the mean of P over the bins in 30 to 100 Hz (Methods) or 80 to 100 Hz
  (Fig. 7d legend).
- Gamma events: 30 to 100 Hz band-pass, 3rd order Butterworth, Hilbert amplitude envelope,
  threshold at the upper bound of the 99% jackknifed confidence interval of the baseline mean
  amplitude, runs above threshold of at least 100 ms counted over 1200 s (Methods). The
  jackknife (claims, o4): leave one sample out, which gives mean + t * SD / sqrt(n), or leave
  one 1 s block out. Rate 10 kHz or 1 kHz (claims, o4). A run is counted in the window if it
  starts in it (standard choice).
- MUA: 300 to 3000 Hz band-pass, 3rd order Butterworth, samples below -3 * median(|x|) /
  0.6745 (Methods; claims, o5, with the span of the median (a) the whole recording or (b) the
  baseline, and counting (a) every sample below threshold or (b) downward crossings), 1 s bins,
  percent change from the mean of the 180 baseline bins (claims, o5).
- Bioluminescence: 3 x 3 median filter per frame, mean over the whole frame (claims, o2b;
  the dandiset records no ROI, so o2a cannot be run), onset at the peak of the discrete
  derivative (Methods). Frames that are entirely zero (58 in sub-interlum-4) are treated as
  missing, so that the jump from a blank frame is not taken as the onset (a necessary choice
  the paper does not address). With MATLAB's `[~, i] = max(diff(b))` the onset is frame i, the last
  frame before the largest rise (standard choice, 1 s either way). As a sensitivity check
  (not a reading of the claims file), two other onsets per imaged mouse are run: the second
  largest rise where it lies within 60 s of the largest (a near tie), and the onset moved by
  the lag at which the whole-frame series best matches the paper's own series of the same
  group in Supplementary Data 7.
- 10 kHz band filters on streamed blocks use 2 s of overlap on each side, which removes edge
  transients of these filters (standard choice).
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache

import h5py
import numpy as np
import remfile
import requests
from dandi.dandiapi import DandiAPIClient
from scipy import fft as sfft
from scipy import ndimage, signal, stats
from scipy.signal.windows import dpss

DANDISET_ID = "000935"
DANDISET_VERSION = "0.240319.2026"

# Supplementary Data 1 to 7 of the article, served by the publisher under the article's DOI.
ARTICLE_DOI = "10.1038/s42003-021-02981-7"
_ESM = ("https://static-content.springer.com/esm/art%3A10.1038%2Fs42003-021-02981-7/"
        "MediaObjects/42003_2021_2981_MOESM{}_ESM.xlsx")
SUPPLEMENTARY_DATA = {k: _ESM.format(k + 3) for k in range(1, 8)}   # Supp. Data k is MOESM k+3

FS = 10_000.0             # file rate (ElectricalSeries starting_time rate)
FS_LFP = 1_000.0          # Methods
BASELINE_S = 180.0        # Methods
POST_S = 1200.0           # Methods, Results
RMS_IQR_K = 3.0           # Methods
GAMMA = (30.0, 100.0)     # Methods
GAMMA_FIG7D = (80.0, 100.0)  # Fig. 7d legend
MUA_BAND = (300.0, 3000.0)   # Methods
EVENT_MIN_S = 0.100       # Methods
EVENT_CI = 0.99           # Methods
MT_WIN_S, MT_STEP_S, MT_NW, MT_K, MT_NFFT = 10.0, 1.0, 3, 5, 16384   # Methods
F_MAX = 150.0             # frequencies kept from the spectrogram (plots and bands only)
BLOCK_S = 60.0            # streaming block
PAD_S = 2.0               # overlap for 10 kHz filters on blocks

_N_THREADS = 16
_PART = 8 * 2 ** 20


# ----------------------------------------------------------------------------- loading

@lru_cache(maxsize=1)
def asset_urls() -> dict[str, str]:
    """{path: streaming URL} of every NWB file at the pinned version."""
    with DandiAPIClient() as client:
        ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        return {a.path: a.get_content_url(follow_redirects=1, strip_query=True)
                for a in ds.get_assets() if a.path.endswith(".nwb")}


def _s(v) -> str:
    v = v[()] if hasattr(v, "shape") else v
    if isinstance(v, np.ndarray):
        v = v.ravel()[0]
    return v.decode() if isinstance(v, bytes) else str(v)


class Session:
    """One NWB file: metadata, and block reads of its contiguous arrays."""

    def __init__(self, path: str, url: str):
        self.path, self.url = path, url
        f = h5py.File(remfile.File(url), "r")
        self._f = f
        subj = f["general/subject"]
        self.subject = _s(subj["subject_id"])
        self.description = _s(subj["description"])
        self.group = "Opsin (+)" if self.description.replace(" ", "").startswith("Opsin(+)") \
            else "Opsin (-)"
        self.age = _s(subj["age"])
        self.sex = _s(subj["sex"])
        es = f["acquisition/ElectricalSeries"]
        self.ephys_description = _s(es.attrs["description"])
        self.fs = float(es["starting_time"].attrs["rate"])
        self.ephys_t0 = float(es["starting_time"][()])
        self.ephys_unit = _s(es["data"].attrs["unit"])
        self.ephys_conversion = float(es["data"].attrs["conversion"])
        d = es["data"]
        assert d.chunks is None and d.compression is None and d.dtype == np.float64
        self.n_samples, self.n_channels = d.shape
        self._ephys_off = d.id.get_offset()
        el = f["general/extracellular_ephys/electrodes"]
        self.position = el["Position"][:].reshape(-1, 3)
        self.labels = [_s(x) for x in el["label"][:]]
        self.infusion = (float(f["intervals/trials/start_time"][0]),
                         float(f["intervals/trials/stop_time"][0]))
        self.n_intervals = len(f["intervals/trials/start_time"])
        self.has_imaging = "1pInternal" in f["acquisition"]
        if self.has_imaging:
            im = f["acquisition/1pInternal"]
            di = im["data"]
            assert di.chunks is None and di.compression is None and di.dtype == np.uint16
            self.image_shape = di.shape
            self.image_rate = float(im["starting_time"].attrs["rate"])
            self.image_t0 = float(im["starting_time"][()])
            self._image_off = di.id.get_offset()

    def probe_metadata(self) -> dict:
        """What the file says about the probe: the electrode table's columns with their
        descriptions, and the descriptions of the electrode groups and devices."""
        f = self._f
        el = f["general/extracellular_ephys/electrodes"]
        cols = {_s(c): _s(el[_s(c)].attrs.get("description", "")) for c in el.attrs["colnames"]}
        ee = f["general/extracellular_ephys"]
        groups = {k: {a: _s(v) for a, v in ee[k].attrs.items() if a in ("description", "location")}
                  for k in ee if k != "electrodes"}
        devices = {k: _s(v.attrs.get("description", "")) for k, v in f["general/devices"].items()}
        return dict(table=_s(el.attrs["description"]), columns=cols, groups=groups, devices=devices)

    @property
    def duration(self) -> float:
        return self.n_samples / self.fs

    def _get(self, start: int, stop: int) -> bytes:
        """Bytes [start, stop) of the file, in parallel range requests."""
        cuts = list(range(start, stop, _PART)) + [stop]

        def one(i):
            for attempt in range(5):
                try:
                    r = requests.get(self.url, timeout=120,
                                     headers={"Range": f"bytes={cuts[i]}-{cuts[i + 1] - 1}"})
                    r.raise_for_status()
                    if len(r.content) == cuts[i + 1] - cuts[i]:
                        return r.content
                except requests.RequestException:
                    if attempt == 4:
                        raise
            raise IOError("short read")

        with ThreadPoolExecutor(_N_THREADS) as ex:
            return b"".join(ex.map(one, range(len(cuts) - 1)))

    def ephys(self, s0: int, s1: int) -> np.ndarray:
        """Samples [s0, s1) of all channels, volts, float64 (time x channel)."""
        s0, s1 = max(0, s0), min(self.n_samples, s1)
        row = 8 * self.n_channels
        b = self._get(self._ephys_off + s0 * row, self._ephys_off + s1 * row)
        return np.frombuffer(b, "<f8").reshape(s1 - s0, self.n_channels) * self.ephys_conversion

    def frames(self, t0: int, t1: int) -> np.ndarray:
        h, w = self.image_shape[1:]
        b = self._get(self._image_off + t0 * h * w * 2, self._image_off + t1 * h * w * 2)
        return np.frombuffer(b, "<u2").reshape(t1 - t0, h, w)


def sessions() -> list[Session]:
    return [Session(p, u) for p, u in sorted(asset_urls().items())]


def supplementary_sheet(k: int, sheet: str):
    """Rows of one sheet of Supplementary Data k, as a list of tuples (header row first)."""
    import io

    import openpyxl
    b = requests.get(SUPPLEMENTARY_DATA[k], timeout=120).content
    ws = openpyxl.load_workbook(io.BytesIO(b), read_only=True, data_only=True)[sheet]
    return [r for r in ws.iter_rows(values_only=True)]


def ladder_columns(k: int, sheet: str, header_row: int = 4) -> dict[str, np.ndarray]:
    """The columns of a ladder-plot sheet: {header: values, without empty cells}. A header that
    repeats an earlier one gets " #2" appended (Fig. 4e has two "Synaptic blockers (After)")."""
    rows = supplementary_sheet(k, sheet)
    head = rows[header_row]
    out = {}
    for j, h in enumerate(head):
        if h is None:
            continue
        v = [r[j] for r in rows[header_row + 1:] if j < len(r) and isinstance(r[j], (int, float))]
        name = str(h).strip()
        out[name + " #2" if name in out else name] = np.asarray(v, float)
    return out


# ----------------------------------------------------------------------------- bioluminescence

def bioluminescence(s: Session, block: int = 100) -> np.ndarray:
    """Whole-frame mean of each 3 x 3 median-filtered frame (claims, o2b), one value per frame.
    Frames that are entirely zero (dropped frames, sub-interlum-4) are returned as NaN."""
    n = s.image_shape[0]
    out = np.empty(n)

    def one(img):
        return np.nan if not img.any() else ndimage.median_filter(img, size=3).mean()

    with ThreadPoolExecutor(4) as ex:
        for t0 in range(0, n, block):
            out[t0:t0 + block] = list(ex.map(one, s.frames(t0, min(n, t0 + block))))
    return out


def onset_index(b: np.ndarray) -> int:
    """Frame of the onset: MATLAB's [~, i] = max(diff(b)) gives frame i (0-based: argmax).
    Differences next to a missing (NaN) frame are ignored."""
    return int(np.nanargmax(np.diff(b)))


# ----------------------------------------------------------------------------- ephys

def errant(rms: np.ndarray, method: str = "linear") -> np.ndarray:
    """Boolean mask of errant contacts by the Methods' IQR rule."""
    if method == "matlab":     # MATLAB prctile: midpoint rule, p = 100 (i - 0.5) / n
        x = np.sort(rms)
        n = len(x)
        pts = 100 * (np.arange(1, n + 1) - 0.5) / n
        q1, q3 = np.interp([25, 75], pts, x)
    else:
        q1, q3 = np.percentile(rms, [25, 75])
    iqr = q3 - q1
    return (rms > q3 + RMS_IQR_K * iqr) | (rms < q1 - RMS_IQR_K * iqr)


def _blocks(s: Session, pad: int):
    """(a, b, lead, x) for consecutive blocks of BLOCK_S seconds with `pad` samples of overlap,
    the next block fetched while the current one is processed."""
    nb = int(BLOCK_S * s.fs)
    starts = list(range(0, s.n_samples, nb))
    with ThreadPoolExecutor(1) as ex:
        fut = ex.submit(s.ephys, -pad, min(s.n_samples, nb) + pad)
        for i, a in enumerate(starts):
            b = min(s.n_samples, a + nb)
            x = fut.result()
            if i + 1 < len(starts):
                a2 = starts[i + 1]
                fut = ex.submit(s.ephys, a2 - pad, min(s.n_samples, a2 + nb) + pad)
            yield a, b, a - max(0, a - pad), x


def stream_pass1(s: Session):
    """Whole recording: RMS of each contact and the 1 kHz resampled raw signal (float32)."""
    q = int(s.fs // FS_LFP)
    pad = int(1.0 * s.fs)
    sumsq = np.zeros(s.n_channels)
    lfp = []
    for a, b, lead, x in _blocks(s, pad):
        core = x[lead:lead + (b - a)]
        sumsq += (core ** 2).sum(0)
        y = signal.resample_poly(x, 1, q, axis=0)
        lfp.append(y[lead // q: lead // q + (b - a) // q].astype(np.float32))
    rms = np.sqrt(sumsq / s.n_samples)
    return rms, np.concatenate(lfp)


def car(x: np.ndarray, keep: np.ndarray) -> np.ndarray:
    """Common average reference over the kept contacts; returns the kept contacts only."""
    k = x[:, keep]
    return k - k.mean(1, keepdims=True)


def _sos(band, fs, kind="bandpass"):
    return signal.butter(3, band, btype=kind, fs=fs, output="sos")


# |x| histogram for the whole-recording MUA median: log-spaced bins from 1e-10 to 1e-2 (file
# units), 0.01% wide, so the median is exact to 0.01% (a standard choice that cannot change
# an outcome).
_HIST_PER_DECADE = 23_027
_HIST_EDGES = np.logspace(-10, -2, 8 * _HIST_PER_DECADE + 1)


def _hist_median(h: np.ndarray) -> float:
    c = np.cumsum(h)
    i = int(np.searchsorted(c, c[-1] / 2))
    return float(np.sqrt(_HIST_EDGES[i] * _HIST_EDGES[i + 1]))


def stream_pass2(s: Session, keep: np.ndarray, span: tuple[float, float]):
    """Whole recording at 10 kHz after CAR. Returns the MUA band signal and the gamma envelope
    over `span` (file seconds; float32, time x kept contact), the first sample of the span,
    and the median of |MUA band| over the whole recording per kept contact."""
    pad = int(PAD_S * s.fs)
    sos_mua = _sos(MUA_BAND, s.fs)
    sos_g = _sos(GAMMA, s.fs)
    e0, e1 = (max(0, int(span[0] * s.fs)), min(s.n_samples, int(span[1] * s.fs)))
    nk = int(keep.sum())
    mua = np.empty((e1 - e0, nk), np.float32)
    env = np.empty((e1 - e0, nk), np.float32)
    hist = np.zeros((nk, len(_HIST_EDGES) - 1), np.int64)
    for a, b, lead, x in _blocks(s, pad):
        x = car(x, keep)
        m = signal.sosfiltfilt(sos_mua, x, axis=0)[lead:lead + (b - a)]
        with np.errstate(divide="ignore"):
            idx = np.floor((np.log10(np.abs(m)) + 10) * _HIST_PER_DECADE)
        idx = np.clip(np.nan_to_num(idx, neginf=0), 0, hist.shape[1] - 1).astype(np.int64)
        for c in range(nk):
            hist[c] += np.bincount(idx[:, c], minlength=hist.shape[1])
        if b > e0 and a < e1:
            c0, c1 = max(a, e0), min(b, e1)
            mua[c0 - e0:c1 - e0] = m[c0 - a:c1 - a]
            g = np.abs(signal.hilbert(signal.sosfiltfilt(sos_g, x, axis=0), axis=0))
            env[c0 - e0:c1 - e0] = g[lead + c0 - a: lead + c1 - a]
    return mua, env, e0, np.array([_hist_median(h) for h in hist])


def lfp_car_hp(lfp_raw: np.ndarray, keep: np.ndarray) -> np.ndarray:
    """1 kHz LFP: CAR over the kept contacts, then 1 Hz high-pass (Methods)."""
    x = car(lfp_raw.astype(np.float64), keep)
    return signal.sosfiltfilt(_sos(1.0, FS_LFP, "highpass"), x, axis=0)


def gamma_envelope_1k(lfp: np.ndarray) -> np.ndarray:
    return np.abs(signal.hilbert(signal.sosfiltfilt(_sos(GAMMA, FS_LFP), lfp, axis=0), axis=0))


def mt_spectrogram(x: np.ndarray, t_start: float, t_stop: float, fs: float = FS_LFP):
    """Multitaper spectrogram (Chronux mtspecgramc settings of the Methods) of each column of x
    (time x channel, sampled from file time 0), for windows centred in [t_start, t_stop).
    Returns (centres in s, frequencies, power: window x frequency x channel)."""
    n = int(MT_WIN_S * fs)
    step = int(MT_STEP_S * fs)
    tapers = dpss(n, MT_NW, MT_K) * np.sqrt(fs)            # K x n
    freqs = np.fft.rfftfreq(MT_NFFT, 1 / fs)
    fk = freqs <= F_MAX
    starts = np.arange(0, x.shape[0] - n + 1, step)
    centres = (starts + n / 2) / fs
    sel = (centres >= t_start) & (centres < t_stop)
    starts, centres = starts[sel], centres[sel]
    out = np.empty((len(starts), int(fk.sum()), x.shape[1]), np.float32)
    for c in range(x.shape[1]):
        segs = np.lib.stride_tricks.sliding_window_view(x[:, c], n)[starts]   # W x n
        for i0 in range(0, len(starts), 200):
            seg = segs[i0:i0 + 200]
            J = sfft.rfft(seg[:, None, :] * tapers[None], n=MT_NFFT, axis=-1, workers=4)
            out[i0:i0 + 200, :, c] = (np.abs(J[..., fk]) ** 2).mean(1) / fs
    return centres, freqs[fk], out


def db_rel_baseline(S: np.ndarray, centres: np.ndarray, onset: float) -> np.ndarray:
    """P = 10 log10(A / B), B the mean power of windows centred in the 180 s before onset."""
    base = (centres >= onset - BASELINE_S) & (centres < onset)
    B = S[base].mean(0, keepdims=True)
    return (10 * np.log10(S / B)).astype(np.float32)


def band_mean(P: np.ndarray, freqs: np.ndarray, band) -> np.ndarray:
    k = (freqs >= band[0]) & (freqs <= band[1])
    return P[:, k].mean(1)


def event_threshold(env_base: np.ndarray, fs: float, jackknife: str) -> np.ndarray:
    """Upper bound of the 99% jackknifed CI of the baseline mean amplitude, per contact."""
    if jackknife == "sample":
        n = env_base.shape[0]
        m = env_base.mean(0)
        se = env_base.std(0, ddof=1) / np.sqrt(n)
    else:   # leave one 1 s block out
        k = int(fs)
        nb = env_base.shape[0] // k
        blocks = env_base[:nb * k].reshape(nb, k, -1).mean(1)
        n = nb
        m = blocks.mean(0)
        loo = (blocks.sum(0, keepdims=True) - blocks) / (n - 1)
        se = np.sqrt((n - 1) / n * ((loo - loo.mean(0)) ** 2).sum(0))
    t = stats.t.ppf(0.5 + EVENT_CI / 2, n - 1)
    return m + t * se


def event_starts(env: np.ndarray, thr: np.ndarray, fs: float) -> list[np.ndarray]:
    """Start samples of the runs above threshold lasting at least 100 ms, per contact."""
    minlen = int(round(EVENT_MIN_S * fs))
    out = []
    for c in range(env.shape[1]):
        above = env[:, c] > thr[c]
        d = np.diff(above.astype(np.int8), prepend=0, append=0)
        st, en = np.flatnonzero(d == 1), np.flatnonzero(d == -1)
        out.append(st[(en - st) >= minlen])
    return out


def count_events(starts: list[np.ndarray], fs: float, w0: int, nbins: int):
    """Events starting in [w0, w0 + nbins s): per-contact totals and counts per 1 s bin."""
    edges = w0 + np.arange(nbins + 1) * int(fs)
    bins = np.stack([np.histogram(st, edges)[0] for st in starts], 1)
    return bins.sum(0), bins


def mua_counts(mua: np.ndarray, fs: float, thr: np.ndarray, counting: str,
               b0: int, nbins: int) -> np.ndarray:
    """MUA counts per 1 s bin (bins x contacts) for bins starting at sample b0 of `mua`, with
    spikes below -thr (samples below, or downward crossings)."""
    k = int(fs)
    out = np.zeros((nbins, mua.shape[1]))
    for c in range(mua.shape[1]):
        seg = mua[b0:b0 + nbins * k, c]
        below = seg < -thr[c]
        if counting == "crossing":
            prev = np.concatenate([[mua[b0 - 1, c] < -thr[c] if b0 > 0 else False], below[:-1]])
            below = below & ~prev
        n = len(seg) // k
        out[:n, c] = below[:n * k].reshape(n, k).sum(1)
    return out


def bootstrap_upper(base: np.ndarray, rng: np.random.Generator, n_boot: int = 10_000,
                    q: float = 97.5) -> float:
    """Upper bound (percentile q) of the bootstrapped mean of base."""
    idx = rng.integers(0, len(base), size=(n_boot, len(base)))
    return float(np.percentile(base[idx].mean(1), q))


def block_bootstrap_means(base: np.ndarray, rng: np.random.Generator, block: int,
                          n_boot: int = 10_000) -> np.ndarray:
    """Moving-block bootstrap of the mean of base (time x contacts): each resample joins
    len(base) // block blocks of `block` consecutive values, drawn with replacement from all
    start positions. Returns resample means (n_boot x contacts). A variant to the claims file's
    bootstrap over single 1 s steps, as consecutive 10 s windows in 1 s steps overlap."""
    n = base.shape[0]
    nb = n // block
    starts = rng.integers(0, n - block + 1, size=(n_boot, nb))
    idx = (starts[:, :, None] + np.arange(block)).reshape(n_boot, nb * block)
    return base[idx].mean(1)


def prctile(x: np.ndarray, p: float, method: str) -> float:
    """Percentile by numpy's linear rule or MATLAB's prctile (midpoint) rule (claims, o6)."""
    if method == "matlab":
        xs = np.sort(np.asarray(x, float))
        n = len(xs)
        pts = 100 * (np.arange(1, n + 1) - 0.5) / n
        return float(np.interp(p, pts, xs))
    return float(np.percentile(x, p))


# ----------------------------------------------------------------------------- one session

def analyse_session(s: Session, lfp_raw: np.ndarray, keep: np.ndarray,
                    onsets: dict[str, float]) -> dict:
    """Every in vivo measure of one session, under every reading, for each onset given
    ({reading name: onset in file seconds}; for imaged mice the onset and the alternative
    onsets of the sensitivity check, for sub-interlum-6 the two readings of claims o1).
    Returns per onset:

    - `centres`, `gamma` (windows x contacts, P over 30-100 Hz), `gamma_hi` (80-100 Hz),
      `spec_mean` (windows x frequencies, P averaged over contacts) and `freqs`, for windows
      centred from 180 s before to 1200 s after onset;
    - `events[(rate, jackknife, window)]`: per-contact counts over 1200 s, and
      `event_bins[...]`: counts per 1 s bin of the post window (runs counted at their start);
    - `mua[(span, counting)]`: percent change per 1 s bin (1200 bins x contacts) and
      `mua_base[...]` the 180 baseline bins in percent change.
    """
    lfp = lfp_car_hp(lfp_raw, keep)
    env1k = gamma_envelope_1k(lfp)
    t_lo = min(min(onsets.values()), s.infusion[0]) - BASELINE_S - 1
    t_hi = max(max(onsets.values()), s.infusion[0]) + POST_S + 1
    mua, env10k, e0, med_whole = stream_pass2(s, keep, (t_lo, t_hi))
    out, done = {}, {}
    for name, on in onsets.items():
        if on in done:          # the same onset under another name: the same results
            out[name] = done[on]
            continue
        r = {}
        c, f, S = mt_spectrogram(lfp, on - BASELINE_S, on + POST_S)
        P = db_rel_baseline(S, c, on)
        r["centres"], r["freqs"] = c - on, f
        r["gamma"] = band_mean(P, f, GAMMA)
        r["gamma_hi"] = band_mean(P, f, GAMMA_FIG7D)
        r["spec_mean"] = P.mean(2)
        del S, P
        r["events"], r["event_bins"], r["thresholds"] = {}, {}, {}
        for rate, env, fs, off in (("10k", env10k, s.fs, e0), ("1k", env1k, FS_LFP, 0)):
            b0 = int(round((on - BASELINE_S) * fs)) - off
            b1 = int(round(on * fs)) - off
            base = env[b0:b1]
            for jk in ("sample", "block"):
                thr = event_threshold(base, fs, jk)
                r["thresholds"][(rate, jk)] = thr
                starts = event_starts(env, thr, fs)
                for win, w_on in (("onset", on), ("infusion", s.infusion[0])):
                    w0 = int(round(w_on * fs)) - off
                    tot, bins = count_events(starts, fs, w0, int(POST_S))
                    r["events"][(rate, jk, win)] = tot
                    r["event_bins"][(rate, jk, win)] = bins
        r["mua"], r["mua_base"], r["mua_rate"] = {}, {}, {}
        b0 = int(round((on - BASELINE_S) * s.fs)) - e0
        p0 = int(round(on * s.fs)) - e0
        med_base = np.median(np.abs(mua[b0:p0]), 0)
        for span, med in (("whole", med_whole), ("baseline", med_base)):
            thr = 3 * med / 0.6745
            for counting in ("samples", "crossing"):
                base = mua_counts(mua, s.fs, thr, counting, b0, int(BASELINE_S))
                post = mua_counts(mua, s.fs, thr, counting, p0, int(POST_S))
                m = base.mean(0, keepdims=True)
                with np.errstate(divide="ignore", invalid="ignore"):
                    r["mua"][(span, counting)] = 100 * (post - m) / m
                    r["mua_base"][(span, counting)] = 100 * (base - m) / m
                r["mua_rate"][(span, counting)] = m.ravel()
        out[name] = done[on] = r
    return out


def run_all(sess: list[Session], onsets: dict[str, dict[str, float]], log=print):
    """Pass 1 over every session (RMS and 1 kHz LFP), the errant contacts of each, then every
    measure of every session under both kept sets: the union over animals of the contacts
    flagged in each ("union"), and each animal's own flags ("own"); the claims file reads the
    excluded set as the union, and asks for both when the union is not 7 contacts.
    Returns (rms, flags by numpy's quartiles, flags by MATLAB's, union, results by kept set and
    subject)."""
    rms, lfp_raw = {}, {}
    for s in sess:
        rms[s.subject], lfp_raw[s.subject] = stream_pass1(s)
        log(f"pass 1 {s.subject}")
    flagged = {k: errant(v) for k, v in rms.items()}
    flagged_matlab = {k: errant(v, "matlab") for k, v in rms.items()}
    union = np.any(list(flagged.values()), axis=0)
    results = {"union": {}, "own": {}}
    for s in sess:
        lr = lfp_raw.pop(s.subject)
        for name, excl in (("union", union), ("own", flagged[s.subject])):
            results[name][s.subject] = analyse_session(s, lr, ~excl, onsets[s.subject])
            log(f"pass 2 {s.subject} {name}")
    return rms, flagged, flagged_matlab, union, results
