"""Loading and spectral measures for the Global/Local Oddball LFP of dandiset 000253.

Sennesh, Westerberg, Spencer-Smith & Bastos (2025), "Ubiquitous predictive processing in the
spectral domain of sensory cortex", bioRxiv doi:10.1101/2025.07.31.667946.

Each subject has one session file (`*_ogen.nwb`: stimulus tables, eye tracking, units) and one
file per probe (`*_probe-N_ecephys.nwb`: LFP at 1250 Hz, 2 channels per HDF5 chunk, gzip, with
the probe's own electrodes table and its area and layer labels). Files are streamed from the
archive at the pinned version; nothing is written to disk. The LFP is read chunk by chunk:
the chunk index is taken from the HDF5 B-tree through `remfile`, and the chunks are fetched with
parallel HTTP range requests and decompressed here.

Where the parameters come from (claims file, opening comment, S1 to S7, unless said otherwise):

- Conditions (claims file, "Conditions and contrasts"): lonaive is the first 50 "xxxy" of the main
  block (the code's lo_gloexp trial index below 50); lo_gloexp "xxxy" and go_gloexp "xxxx" in the
  main block; lo_rndctl "xxxy" in the random block; go_seqctl "xxxx" and igo_seqctl "yyyy" in the
  sequence control block. x is the orientation of the first three gratings of the sequence the
  mouse was habituated to, read here as the most common sequence of the main block. The blocks
  are told apart from the stimulus table (`init_grating_presentations`): the main block holds
  only "xxxy" and "xxxx", the random block every pattern, the sequence block only "xxxx" and
  "yyyy". The table has no condition labels; this reconstruction is checked against the trial
  counts of the paper (claim trial-counts).
- Epochs: 0.5 s before P4 onset to 0.5 s after P4 offset (S2; epoching notebook).
- Channels (S1): locations containing "VIS" on the area's probe, median filter over 3 adjacent
  channels, aligned across mice at the median L4 channel, cropped to the smallest extent above
  and below it, labels by majority vote, every fourth channel kept. The claims file does not say
  where the downsampling starts; it is taken from the code (`alignment`, `kept_rows`): channels
  ordered from the tip up, the topmost common row left out by the crop, every fourth row kept
  from the deepest. The notebook repeats the cluster tests with the start moved up by 1 and 3
  rows (`KEPT_SHIFTS`); in V1 the shift of 3 keeps the other L1 row and the shift of 1 none.
- Spectrogram (S2): Hann taper, 200 ms window (250 samples at 1250 Hz), FFT padded to the next
  power of two (256), power at the bins nearest 5, 10, ..., 150 Hz. The bins lie 4.88 Hz apart
  (`FOI_HZ`): the labels 5 to 100 Hz fall on 4.9 to 97.7 Hz, 105 to 150 Hz on 107.4 to
  151.4 Hz, and the 102.5 Hz bin is not used. The labels are kept, as the claims' ranges are
  written in them. Windows are centred every 10 ms from -10 ms to 510 ms after P4 onset. Centring each window on the nearest sample, as 10 ms is
  12.5 samples at 1250 Hz, is a standard choice that cannot change a result.
- Aperiodic removal (S3): FOOOF 1.1.0, the Methods' settings, fitted to the spectrogram averaged
  over trials and time per condition and channel; readings (a) 5 to 150 Hz, (b) 5 to 90 Hz.
- Condition panels (S6): the claims file's "dB spectrogram of S3 averaged over trials" is read
  as in the paper's code (epych cee2e6f, notebooks/passiveglo/oscillatory_eyeballs.ipynb, cell 12:
  `oscillatory()`, which divides each trial by the linear aperiodic fit, then `erp()`, the trial
  mean, then `decibels()`), that is dB of the trial-mean power over the aperiodic fit. The trial
  mean of per-trial dB values is shown as a second reading; for exponentially distributed power
  it lies about 2.5 dB lower.
- Cluster test (S4): F statistic of a one-way ANOVA of two groups, cluster-forming threshold the
  F quantile 0.99 with 1 and n1 + n2 - 1 degrees of freedom, clusters on the lattice of time,
  frequency and channel (faces adjacency, MNE's default lattice), cluster mass the sum of F,
  1000 permutations, cluster p < 0.01. `cluster_test` computes the same as
  mne.stats.spatio_temporal_cluster_test with these settings, using sums over the permuted
  group in place of a full ANOVA per permutation; the notebook checks it against MNE.
- Bands (S5): theta 2-10, alpha/beta 10-30, gamma 30-90 Hz, with the code's 30-50 Hz as a second
  gamma reading; band bins from the one nearest the lower edge up to, not including, the one
  nearest the upper edge.
- Trough-locked CSD (S7). The FIR band-pass (Syncopy firws in the code) is not specified; a
  windowed-sinc FIR (Hamming) of at most 249 taps applied forward and backward is an assumption
  forced by the 600 ms segments. The CSD is the standard second spatial difference,
  -(phi(z+h) - 2 phi(z) + phi(z-h)) / h^2 (Elephant StandardCSD with unit conductivity and its default Vaknin edge rows),
  computed here to avoid Elephant's dependencies. S7's first-sink rule ties when every layer
  group holds a displayed sink at the first lag; the notebook then uses, as an assumption, the
  sink onset of each group's mean CSD (the first lag at which it turns from source to sink),
  and prints the sign of each group's mean CSD at every lag.
- Per-mouse spectra (claim dd-gamma-peak-frequency-v1): Hann-tapered FFT of each trial's
  segment, zero-padded to 1250 samples, every second bin kept (a 2 Hz grid, the Methods' 2 Hz
  resolution).
"""

from __future__ import annotations

import collections
import json
import time
import warnings
import zlib
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
import requests
from scipy import ndimage, signal, stats

DANDISET_ID = "000253"
DANDISET_VERSION = "0.240923.1441"
CITED_VERSION = "0.240503.0152"      # the version the paper cites (Data availability)
API = "https://api.dandiarchive.org/api"

FS = 1250.0                      # LFP sampling rate in the files (checked in the notebook)
PRE, POST = 0.5, 0.5             # epoch margins around P4 (s)
P4_DUR = 0.5                     # grating duration (s), checked against the table
AREAS = {"V1": "VISp", "LM": "VISl", "RL": "VISrl", "AL": "VISal", "PM": "VISpm", "AM": "VISam"}
CONDITIONS = ["lonaive", "lo_gloexp", "go_gloexp", "lo_rndctl", "go_seqctl", "igo_seqctl"]
CONTRASTS = {"DD": ("lo_rndctl", "lonaive"), "GO": ("go_gloexp", "go_seqctl"),
             "SSA": ("lo_gloexp", "igo_seqctl")}
BANDS = {"theta": (2, 10), "alphabeta": (10, 30), "gamma": (30, 90), "gamma_code": (30, 50)}

# Spectrogram grid (S2)
WIN = 250                        # 200 ms at 1250 Hz
NFFT = 256                       # next power of two
FOI = np.arange(5, 151, 5).astype(float)
TOI = np.round(np.arange(-0.010, 0.5101, 0.010), 3)


# ----------------------------------------------------------------------------- archive

def assets(version=DANDISET_VERSION):
    """Path -> asset record for a version (the pinned one by default)."""
    out, url = {}, f"{API}/dandisets/{DANDISET_ID}/versions/{version}/assets/?page_size=200"
    while url:
        r = requests.get(url, timeout=60).json()
        out.update({a["path"]: a for a in r["results"]})
        url = r["next"]
    return out


def s3_url(asset):
    return requests.head(f"{API}/assets/{asset['asset_id']}/download/", allow_redirects=True,
                         timeout=60).url


def sessions(asset_map=None, version=DANDISET_VERSION):
    """One row per subject: session file and probe files."""
    asset_map = asset_map or assets(version)
    rows = collections.defaultdict(dict)
    for p, a in asset_map.items():
        sub = p.split("/")[0]
        if p.endswith("_ogen.nwb"):
            rows[sub]["ogen"] = a
        elif "_probe-" in p:
            rows[sub][int(p.split("_probe-")[1].split("_")[0])] = a
    return dict(sorted(rows.items()))


def open_h5(asset):
    return h5py.File(remfile.File(s3_url(asset)), "r")


# ----------------------------------------------------------------------------- stimulus

def sequence_table(f):
    """One row per grating sequence of the session, from init_grating_presentations.

    Gratings at 45 degrees are 'a' and at 135 degrees 'b'; a row with no orientation (the
    blank between sequences) ends a sequence.
    """
    g = f["intervals/init_grating_presentations"]
    df = pd.DataFrame({c: g[c][:] for c in ["start_time", "stop_time", "orientation", "stimulus_block"]})
    rows, cur = [], []
    for r in df.itertuples():
        if np.isnan(r.orientation):
            if cur:
                rows.append(cur)
            cur = []
        else:
            cur.append(r)
    if cur:
        rows.append(cur)
    seqs = pd.DataFrame({
        "block": [int(s[0].stimulus_block) for s in rows],
        "pattern": ["".join("a" if x.orientation == 45 else "b" for x in s) for s in rows],
        "p4_on": [s[3].start_time if len(s) >= 4 else np.nan for s in rows],
        "p4_off": [s[3].stop_time if len(s) >= 4 else np.nan for s in rows],
        "p4_orientation": [s[3].orientation if len(s) >= 4 else np.nan for s in rows],
    })
    return seqs


def label_blocks(seqs):
    """Mark each sequence main, random or sequence control, and map a/b to x/y."""
    kinds = {}
    for b, d in seqs.groupby("block"):
        pats = set(d.pattern)
        if pats <= {"aaaa", "bbbb"} and len(pats) == 2:
            kinds[b] = "seqctl"
        elif len(pats) > 3:
            kinds[b] = "random"
        else:
            kinds[b] = "main"
    seqs = seqs.copy()
    seqs["kind"] = seqs.block.map(kinds)
    habit = seqs[seqs.kind == "main"].pattern.value_counts().index[0]
    x, y = habit[0], habit[3]
    seqs["xy"] = seqs.pattern.str.translate(str.maketrans({x: "x", y: "y"}))
    seqs.attrs["habituated"] = habit
    return seqs


def conditions(seqs):
    """Condition name -> rows of seqs (P4 trials), as the claims file defines them."""
    m, r, s = seqs.kind == "main", seqs.kind == "random", seqs.kind == "seqctl"
    lo = seqs[m & (seqs.xy == "xxxy")]
    return {
        "lonaive": lo.iloc[:50],
        "lo_gloexp": lo,
        "go_gloexp": seqs[m & (seqs.xy == "xxxx")],
        "lo_rndctl": seqs[r & (seqs.xy == "xxxy")],
        "go_seqctl": seqs[s & (seqs.xy == "xxxx")],
        "igo_seqctl": seqs[s & (seqs.xy == "yyyy")],
    }


# ----------------------------------------------------------------------------- electrodes

def probe_electrodes(f):
    """Electrodes of a probe file with the LFP column of each."""
    e = f["general/extracellular_ephys/electrodes"]
    el = pd.DataFrame({c: e[c][:] for c in ["id", "location", "probe_vertical_position",
                                             "probe_horizontal_position", "local_index"]})
    el["location"] = el.location.str.decode("utf8")
    key = [k for k in f["acquisition"] if k.endswith("_lfp_data")][0]
    cols = f[f"acquisition/{key}/electrodes"][:]
    lfp = el.iloc[cols].reset_index(drop=True)
    lfp["column"] = np.arange(len(lfp))
    return lfp, key


def area_of(location):
    for name, prefix in AREAS.items():
        if location.startswith(prefix) and location[len(prefix):][:1].isdigit():
            return name
    return None


def layer_of(location):
    """Layer group from a label such as 'VISp2/3' or 'VISp6a' (claims file, S1)."""
    tail = location.lstrip("VISplmrladm")
    if "2/3" in tail:
        return "L2/3"
    if tail.startswith("1"):
        return "L1"
    if tail.startswith("4"):
        return "L4"
    if tail.startswith("5") or tail.startswith("6"):
        return "L5/6"
    return None


def cortical_channels(lfp, area):
    """The area's visual-cortex channels, from the surface down (highest local index first)."""
    d = lfp[lfp.location.map(area_of) == area].sort_values("local_index", ascending=False)
    d = d.reset_index(drop=True)
    step = np.median(np.abs(np.diff(d.probe_vertical_position)))
    if step >= 40:
        # One channel every 40 um (one in four of the full probe): each stands for the four
        # full-resolution rows nearest it, so that rows align in depth with the other mice.
        d = d.loc[d.index.repeat(4)].reset_index(drop=True)
    return d


def kept_rows(n, shift=0):
    """S1 downsampling as the code does it (epych signal.py, downsample: channels.loc[0::4]) on a
    column ordered from the deepest row up: every fourth row from the deepest, here returned as
    top-down row numbers. shift moves the start up by that many rows (variants only)."""
    return np.arange(n - 1 - shift, -1, -4)[::-1]


def alignment(channel_tables):
    """S1 as the paper's code does it (epych cee2e6f, statistics/alignment.py, ChannelAlignment).

    The code orders each probe's channels from the tip up (the LFP column order, local index
    ascending, checked in the notebook), takes as centre the L4 channel at round(median) of the
    L4 positions in that order (round half to even), and crops every mouse to
    range(centre - down, centre + up), down and up the smallest extents below and above the
    centre; the range leaves out the topmost common row. Labels by majority vote; every fourth
    row kept from the deepest (kept_rows).

    channel_tables: mouse -> cortical_channels table (top-down). Returns mouse -> (start, stop)
    rows of its table, the aligned labels (top-down), the kept rows and the raw labels.
    """
    l4 = {}
    for m, d in channel_tables.items():
        idx = np.flatnonzero(d.location.map(layer_of) == "L4")
        asc = np.sort(len(d) - 1 - idx)                     # positions counted from the tip
        l4[m] = len(d) - 1 - int(round(np.median(asc)))      # back to top-down
    above = min(l4[m] for m in channel_tables)
    below = min(len(d) - 1 - l4[m] for m, d in channel_tables.items())
    spans = {m: (l4[m] - above + 1, l4[m] + below + 1) for m in channel_tables}
    n = above + below
    raw = []
    for i in range(n):
        votes = collections.Counter(channel_tables[m].location.iloc[spans[m][0] + i]
                                    for m in channel_tables)
        raw.append(votes.most_common(1)[0][0])
    labels = [layer_of(x) for x in raw]
    return spans, labels, kept_rows(n), raw


# ----------------------------------------------------------------------------- LFP reading

def _chunk_index(args):
    url, key = args
    f = h5py.File(remfile.File(url), "r")
    ds = f[f"acquisition/{key}/data"]
    info = {}
    ds.id.chunk_iter(lambda c: info.__setitem__(c.chunk_offset, (c.byte_offset, c.size)))
    ts = f[f"acquisition/{key}/timestamps"]
    n = ds.shape[0]
    probe_t = [int(i) for i in np.linspace(0, n - 1, 12)]
    t_samples = np.array([ts[i] for i in probe_t])
    return {"index": info, "chunks": ds.chunks, "shape": ds.shape, "dtype": ds.dtype.str,
            "filters": (ds.compression, ds.shuffle), "conversion": float(ds.attrs["conversion"]),
            "t_index": probe_t, "t_samples": t_samples}


def chunk_indexes(jobs, workers=14):
    """Read the chunk index of several LFP datasets in parallel processes.

    jobs: list of (s3 url, acquisition key). Returns one dict per job.
    """
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(_chunk_index, jobs))


_session = None


def _get(url, off, size):
    global _session
    if _session is None:
        _session = requests.Session()
        _session.mount("https://", requests.adapters.HTTPAdapter(pool_maxsize=64))
    for attempt in range(5):
        try:
            r = _session.get(url, headers={"Range": f"bytes={off}-{off + size - 1}"}, timeout=60)
            if r.status_code in (200, 206) and len(r.content) == size:
                return r.content
        except requests.RequestException:
            pass
        time.sleep(1 + attempt)
    raise IOError(f"range read failed at {off}")


def read_columns(url, meta, col0, threads=48):
    """The full trace of the chunk column starting at col0 (2 channels), float32 volts."""
    T, C = meta["chunks"]
    n = meta["shape"][0]
    starts = list(range(0, n, T))
    out = np.empty((n, C), dtype=np.float32)

    def one(t0):
        off, size = meta["index"][(t0, col0)]
        raw = np.frombuffer(zlib.decompress(_get(url, off, size)), dtype=meta["dtype"])
        rows = min(T, n - t0)
        out[t0:t0 + rows] = raw.reshape(T, C)[:rows]

    with ThreadPoolExecutor(threads) as ex:
        list(ex.map(one, starts))
    return out * meta["conversion"]


def lfp_clock(meta):
    """Linear clock of the LFP: t0 and rate fitted to timestamps sampled across the file."""
    i, t = np.array(meta["t_index"]), meta["t_samples"]
    slope, t0 = np.polyfit(i, t, 1)
    resid = t - (t0 + slope * i)
    return t0, 1.0 / slope, np.abs(resid).max()


def epochs(trace, t0, fs, onsets, pre=PRE, post=P4_DUR + POST):
    """Cut (trials, samples) windows from a 1-D trace, from onset - pre to onset + post."""
    n = int(round((pre + post) * fs))
    first = np.round((np.asarray(onsets) - pre - t0) * fs).astype(int)
    idx = first[:, None] + np.arange(n)[None, :]
    return trace[idx]


def epoch_times(fs=FS, pre=PRE, post=P4_DUR + POST):
    n = int(round((pre + post) * fs))
    return np.arange(n) / fs - pre


# ----------------------------------------------------------------------------- spectra

_HANN = signal.windows.hann(WIN, sym=False)
_FREQS = np.fft.rfftfreq(NFFT, 1 / FS)
FOI_BINS = np.array([int(np.argmin(np.abs(_FREQS - f))) for f in FOI])
FOI_HZ = _FREQS[FOI_BINS]        # the FFT bins' own frequencies (4.88 Hz apart), printed in the notebook


def spectrogram(ep, fs=FS, batch=32):
    """S2. ep: (..., samples) epochs starting PRE s before P4 onset -> (..., time, freq) power.

    Computed over the leading axis in batches of trials, to bound memory; the result is the same.
    """
    centres = np.round((TOI + PRE) * fs).astype(int)
    idx = centres[:, None] + np.arange(WIN)[None, :] - WIN // 2
    out = np.empty(ep.shape[:-1] + (len(TOI), len(FOI)), dtype=np.float32)
    for i in range(0, max(len(ep), 1), batch):
        seg = ep[i:i + batch][..., idx] * _HANN
        spec = np.fft.rfft(seg, n=NFFT, axis=-1)[..., FOI_BINS]
        out[i:i + batch] = np.abs(spec) ** 2
    return out


def fooof_aperiodic(freqs, power, fit_range):
    """S3. Aperiodic fit (log10 power) at every frequency in freqs, FOOOF fixed mode."""
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        from fooof import FOOOF
        fm = FOOOF(peak_width_limits=(0.5, 12.0), max_n_peaks=np.inf, min_peak_height=0.0,
                   peak_threshold=2.0, aperiodic_mode="fixed", verbose=False)
        fm.fit(freqs, power, fit_range)
    off, exp = fm.aperiodic_params_
    return off - np.log10(freqs ** exp), (off, exp), fm


def band_bins(freqs, band):
    """S5: from the bin nearest the lower edge up to, not including, the one nearest the upper."""
    lo = int(np.argmin(np.abs(freqs - band[0])))
    hi = int(np.argmin(np.abs(freqs - band[1])))
    return np.arange(lo, hi)


def periodogram(ep, fs=FS):
    """Hann-tapered power spectrum on a 2 Hz grid (claim dd-gamma-peak-frequency-v1)."""
    n = ep.shape[-1]
    w = signal.windows.hann(n, sym=False)
    nfft = int(round(fs))  # 1 Hz bins; every second kept
    p = np.abs(np.fft.rfft((ep - ep.mean(-1, keepdims=True)) * w, n=nfft, axis=-1)) ** 2
    f = np.fft.rfftfreq(nfft, 1 / nfft)
    return f[::2], p[..., ::2]


# ----------------------------------------------------------------------------- statistics

def f_threshold(n1, n2, q=0.99):
    """S4: the F quantile with 1 and n1 + n2 - 1 degrees of freedom."""
    return stats.f.ppf(q, 1, n1 + n2 - 1)


def _f_from_sums(s1, n1, tot, totsq, n):
    m1 = s1 / n1
    m2 = (tot - s1) / (n - n1)
    m = tot / n
    ssb = n1 * (m1 - m) ** 2 + (n - n1) * (m2 - m) ** 2
    ssw = totsq - n * m ** 2 - ssb
    return ssb / np.maximum(ssw / (n - 2), 1e-30)


def cluster_test(a, b, rng, n_perm=1000, threshold=None, batch=50):
    """S4. a, b: (trials, time, freq, channel). Returns F, cluster labels, cluster p-values.

    Two-group F (one-way ANOVA), clusters of F above threshold on the faces lattice, cluster
    mass the sum of F, null distribution of the largest cluster mass over random relabellings
    of the pooled trials (the observed labelling counted in, as MNE does).
    """
    n1, n2 = len(a), len(b)
    n = n1 + n2
    shape = a.shape[1:]
    x = np.concatenate([a.reshape(n1, -1), b.reshape(n2, -1)]).astype(np.float32, copy=False)
    x -= x.mean(0, dtype=np.float64).astype(np.float32)   # centred, so that float32 sums lose little
    tot = x.sum(0, dtype=np.float64)
    totsq = np.zeros(x.shape[1])
    for i in range(0, n, 256):           # in blocks of trials, to bound memory
        totsq += (x[i:i + 256].astype(np.float64) ** 2).sum(0)
    threshold = f_threshold(n1, n2) if threshold is None else threshold
    f_obs = _f_from_sums(x[:n1].sum(0), n1, tot, totsq, n).reshape(shape)
    labels, k = ndimage.label(f_obs > threshold)
    mass = ndimage.sum(f_obs, labels, np.arange(1, k + 1)) if k else np.array([])
    null = np.empty(n_perm)
    null[0] = mass.max() if k else 0.0
    done = 1
    while done < n_perm:
        m = min(batch, n_perm - done)
        ind = np.zeros((m, n))
        for i in range(m):
            ind[i, rng.permutation(n)[:n1]] = 1.0
        sums = (ind.astype(np.float32) @ x).astype(np.float64)
        for i in range(m):
            fp = _f_from_sums(sums[i], n1, tot, totsq, n).reshape(shape)
            lp, kp = ndimage.label(fp > threshold)
            null[done + i] = ndimage.sum(fp, lp, np.arange(1, kp + 1)).max() if kp else 0.0
        done += m
    pvals = np.array([(null >= s).mean() for s in mass])
    return f_obs, labels, pvals


def welch_perm_test(a, b, rng, n_perm=1000):
    """Welch t-test with a permutation p-value (scipy ttest_ind, equal_var False, permutations)."""
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        res = stats.ttest_ind(a, b, equal_var=False,
                              method=stats.PermutationMethod(n_resamples=n_perm, random_state=rng))
    return float(res.statistic), float(res.pvalue)


# ----------------------------------------------------------------------------- CSD

def bandpass(x, band, fs=FS, max_taps=249):
    """Zero-phase windowed-sinc FIR band-pass along the last axis (assumption, see docstring)."""
    taps = min(max_taps, int(3 * fs / band[0]) | 1)
    h = signal.firwin(taps, band, pass_zero=False, fs=fs)
    return signal.filtfilt(h, [1.0], x, axis=-1)


def trough_windows(phase, half):
    """S7: trial and sample of each trough (|phase| within 0.001 of pi) whose window fits."""
    tr, smp = np.nonzero(np.abs(np.abs(phase) - np.pi) <= 0.001)
    ok = (smp - half >= 0) & (smp + half < phase.shape[-1])
    return tr[ok], smp[ok]


def csd(phi, h):
    """Standard CSD, -(phi(z+h) - 2 phi(z) + phi(z-h)) / h^2, along axis -2 (channels).

    The edge rows are repeated once above and below (Vaknin electrodes, Elephant's default for
    StandardCSD), so that the CSD has one row per kept channel, the top (L1) row included.
    """
    p = np.concatenate([phi[..., :1, :], phi, phi[..., -1:, :]], axis=-2)
    return -(p[..., 2:, :] - 2 * p[..., 1:-1, :] + p[..., :-2, :]) / h ** 2


# ----------------------------------------------------------------------------- per-mouse pass

CSD_SEGMENT = (-0.05, 0.55)      # S7: 50 ms before P4 onset to 50 ms after offset
CSD_JOBS = {
    # claim: (condition, {reading: (band, phase layers)}); phase layers from the code (S7)
    "fig2g": ("lo_rndctl", "gamma"), "fig2h": ("lonaive", "alphabeta"), "fig2i": ("lo_rndctl", "theta"),
    "fig3g": ("go_gloexp", "gamma"), "fig3h": ("go_seqctl", "alphabeta"), "fig3i": ("go_gloexp", "theta"),
    "fig4g": ("lo_gloexp", "gamma"), "fig4h": ("igo_seqctl", "alphabeta"), "fig4i": ("lo_gloexp", "theta"),
}
CSD_BANDS = {"a": {"theta": (2, 10), "alphabeta": (10, 30), "gamma": (30, 90)},
             "b": {"theta": (4, 8), "alphabeta": (12, 24), "gamma": (30, 50)}}
PHASE_LAYERS = {"theta": None, "alphabeta": ["L5/6"], "gamma": ["L2/3", "L4"]}
SPECTRA_WINDOWS = {"a": (-0.05, 0.55), "b": (-0.02, 0.52)}   # claim dd-gamma-peak-frequency-v1


def phase_row(labels, band_name):
    """Middle aligned row of the layers the code takes the phase on (S7)."""
    layers = PHASE_LAYERS[band_name]
    rows = np.arange(len(labels)) if layers is None else \
        np.array([i for i, l in enumerate(labels) if l in layers])
    return int(rows[len(rows) // 2])


KEPT_SHIFTS = [1, 3]              # variants: the every-fourth start moved up by 1 or 3 rows (0 in the main analysis)


def _variant_specs(e, edges, names, fs):
    """Spectrograms of a variant channel set, stored compactly: per condition, float16 log10 power
    relative to a float32 reference (the log10 of the mean power per frequency and channel).
    The rounding (at most about 0.02 dB per trial and point) is a standard choice that cannot
    change a result."""
    out = {}
    for i, c in enumerate(names):
        x = e[edges[i]:edges[i + 1]]
        x = x - x.mean(-1, keepdims=True)
        p = np.log10(spectrogram(x, fs).transpose(0, 2, 3, 1))      # trials, time, freq, channel
        ref = p.mean((0, 1)).astype(np.float32)
        out[c] = ((p - ref).astype(np.float16), ref)
    return out


def variant_power(parts):
    """Rebuild float32 power from _variant_specs parts of several mice (concatenated over trials)."""
    return np.concatenate([10.0 ** (q.astype(np.float32) + ref) for q, ref in parts])


def mouse_pass(url, meta, chans, span, labels, kept, conds, threads=48):
    """Read one mouse's aligned channels and reduce them to what the claims use.

    Returns spectrograms of the kept channels per condition, per-channel mean spectra for the
    per-mouse analyses, ERP sums, the CSD trough sums, and the evoked check.
    """
    t0, fs, resid = lfp_clock(meta)
    rows = chans.iloc[span[0] - 1 if span[0] > 0 else 0: span[1] + 1]
    lo_pad = 1 if span[0] > 0 else 0
    cols = rows.column.to_numpy()
    allon = np.concatenate([c.p4_on.to_numpy() for c in conds.values()])
    sizes = [len(c) for c in conds.values()]
    n_s = int(round((PRE + P4_DUR + POST) * fs))
    ep = np.empty((len(cols), len(allon), n_s), dtype=np.float32)
    pairs = sorted(set((c // 2) * 2 for c in cols))
    started = time.time()
    for p in pairs:
        tr = read_columns(url, meta, p, threads=threads)
        for j in np.flatnonzero((cols // 2) * 2 == p):
            ep[j] = epochs(tr[:, cols[j] - p], t0, fs, allon)
        del tr
    read_s = time.time() - started
    n_al = span[1] - span[0]
    edges = np.cumsum([0] + sizes)
    names = list(conds)
    # Variant without the S1 median filter, on the kept rows (what light_pass reads in the areas
    # notebook), so that the effect of skipping the filter can be shown in V1.
    nofilt = np.ascontiguousarray(ep[lo_pad + np.asarray(kept)].transpose(1, 0, 2))
    out = {"read_s": read_s, "clock_resid": resid, "fs": fs, "t0": t0, "n_pairs": len(pairs),
           "variants": {}}
    out["variants"]["nofilt"] = _variant_specs(nofilt, edges, names, fs)
    del nofilt
    # S1: median over 3 adjacent channels (edges use the nearest channel), then crop.
    ep = ndimage.median_filter(ep, size=(3, 1, 1), mode="nearest")
    ep = ep[lo_pad:lo_pad + n_al]
    ep = np.ascontiguousarray(ep.transpose(1, 0, 2))      # trials, channels, samples
    out["spec"] = {}
    for i, c in enumerate(names):
        e = ep[edges[i]:edges[i + 1]][:, kept]
        e = e - e.mean(-1, keepdims=True)     # each trial de-meaned (Syncopy's default polyremoval=0)
        out["spec"][c] = spectrogram(e, fs).transpose(0, 2, 3, 1)   # trials, time, freq, channel
    # Variants of where the every-fourth downsampling starts (moved up from the deepest row).
    for k in KEPT_SHIFTS:
        out["variants"][f"shift{k}"] = _variant_specs(ep[:, kept_rows(n_al, k)], edges, names, fs)
    # per-mouse spectra, aligned channels, two windows
    tt = epoch_times(fs)
    out["psd"] = {}
    for r, (a, b) in SPECTRA_WINDOWS.items():
        sel = (tt >= a) & (tt < b)
        for i, c in enumerate(names):
            f, p = periodogram(ep[edges[i]:edges[i + 1]][:, :, sel], fs)
            out["psd"][(r, c)] = p.mean(0)          # channels, freq
    out["psd_freqs"] = f
    # evoked potentials (kept channels) for the clock check and CSD
    out["erp_sum"] = {c: ep[edges[i]:edges[i + 1]].sum(0) for i, c in enumerate(names)}
    out["n"] = dict(zip(names, sizes))
    # trough-locked sums (S7)
    seg = (tt >= CSD_SEGMENT[0]) & (tt < CSD_SEGMENT[1])
    out["csd"] = {}
    for claim, (c, band_name) in CSD_JOBS.items():
        i = names.index(c)
        x = ep[edges[i]:edges[i + 1]][:, :, seg]
        prow = phase_row(labels, band_name)
        for r, bands in CSD_BANDS.items():
            band = bands[band_name]
            half = int(round(0.75 * fs / np.mean(band)))
            ph = np.angle(signal.hilbert(bandpass(x[:, prow], band, fs), axis=-1))
            tr, smp = trough_windows(ph, half)
            L = 2 * half + 1
            xs = x[:, kept]
            S = np.zeros((x.shape[-1], len(kept), L), dtype=np.float32)
            N = np.zeros(x.shape[-1])
            Q = np.zeros((len(kept), L))
            for t_, s_ in zip(tr, smp):
                w = xs[t_, :, s_ - half:s_ + half + 1].astype(np.float64)
                S[s_] += w.astype(np.float32)
                N[s_] += 1
                Q += csd(w[None], 1.0)[0] ** 2
            out["csd"][(claim, r)] = (S, N, Q, half)
    return out


# ----------------------------------------------------------------------------- survey

def _session_meta(args):
    sub, ogen = args
    f = open_h5(ogen)
    seqs = label_blocks(sequence_table(f))
    subj = {k: f[f"general/subject/{k}"][()].decode() for k in ["age", "sex", "genotype", "subject_id"]}
    eye = None
    if "EyeTracking" in f["acquisition"]:
        g = f["acquisition/EyeTracking"]
        eye = {k: g[k] for k in g}
        eye = {"keys": sorted(eye), "t": g["pupil_tracking/timestamps"][:],
               "area": g["pupil_tracking/area"][:], "blink": g["likely_blink/data"][:]}
    return sub, seqs, subj, eye


def _probe_meta(args):
    sub, num, asset = args
    url = s3_url(asset)
    f = h5py.File(remfile.File(url), "r")
    lfp, key = probe_electrodes(f)
    areas = lfp.location.map(area_of).dropna().value_counts()
    ds = f[f"acquisition/{key}/data"]
    ts = f[f"acquisition/{key}/timestamps"]
    check = {"ts": (ts[0], ts[1], ts[-1]), "sample": ds[200000:200250, :8].astype(np.float64)}
    return sub, num, url, key, lfp, (areas.index[0] if len(areas) else None), ds.shape, ds.chunks, check


def survey(workers=16, version=DANDISET_VERSION):
    """Stimulus sequences of every session and the electrodes of every probe file."""
    sess = sessions(version=version)
    with ProcessPoolExecutor(workers) as ex:
        s = list(ex.map(_session_meta, [(k, v["ogen"]) for k, v in sess.items()]))
        p = list(ex.map(_probe_meta, [(k, n, v[n]) for k, v in sess.items() for n in range(6) if n in v]))
    return sess, {x[0]: x for x in s}, p


def light_pass(url, meta, chans, span, kept, conds, threads=64):
    """Read only the kept rows of an area (every fourth aligned channel; no median filter).

    Returns, per condition, the spectrograms of the kept rows (S2, trials de-meaned) and the
    trial-mean power spectra of each kept row for the two windows of the per-mouse analyses.
    Used for the areas other than V1, where reading every channel does not fit the time limit.
    """
    t0, fs, resid = lfp_clock(meta)
    rows = chans.iloc[span[0]:span[1]].iloc[kept]
    cols = rows.column.to_numpy()
    names = list(conds)
    allon = np.concatenate([conds[c].p4_on.to_numpy() for c in names])
    sizes = [len(conds[c]) for c in names]
    n_s = int(round((PRE + P4_DUR + POST) * fs))
    ep = np.empty((len(allon), len(cols), n_s), dtype=np.float32)
    started = time.time()
    for p in sorted(set((c // 2) * 2 for c in cols)):
        tr = read_columns(url, meta, p, threads=threads)
        for j in np.flatnonzero((cols // 2) * 2 == p):
            ep[:, j] = epochs(tr[:, cols[j] - p], t0, fs, allon)
        del tr
    out = {"read_s": time.time() - started, "clock_resid": resid, "n": dict(zip(names, sizes)), "spec": {}, "psd": {}}
    edges = np.cumsum([0] + sizes)
    tt = epoch_times(fs)
    for i, c in enumerate(names):
        e = ep[edges[i]:edges[i + 1]]
        out["spec"][c] = spectrogram(e - e.mean(-1, keepdims=True), fs).transpose(0, 2, 3, 1)
        for r, (a, b) in SPECTRA_WINDOWS.items():
            f, p = periodogram(e[:, :, (tt >= a) & (tt < b)], fs)
            out["psd"][(r, c)] = p.mean(0)
    out["psd_freqs"] = f
    return out
