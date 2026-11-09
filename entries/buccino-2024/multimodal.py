"""Loading and measures for dandiset 000294: simultaneous patch-clamp and HD-MEA recordings of two
cultured rat cortical neurons (Buccino et al. 2024, Neural Computation 36:1286,
doi:10.1162/neco_a_01672).

Each NWB file holds one neuron. Per run there is an HD-MEA `ElectricalSeries_run<k>` (uint16 counts,
678 or 675 channels, its own timestamps) and, per sweep, a `CurrentClampSeries`
`response_<protocol>_<run>_<sweep>` with its `CurrentClampStimulusSeries` `stimulus_...`, both
with timestamps on the same clock as the MEA series of the run. The files say volts and amperes;
the values are millivolts and picoamperes (checked in the notebook). Files are streamed from the
archive at the pinned version; nothing is written to disk.

Where the parameters come from:

- Spike detection on the patch voltage: eFEL `peak_time` with threshold -20 mV, as in
  `mea_patch.get_peak_times` of the paper's code (github.com/alejoe91/multimodalfitting at commit
  24e8e6168b2d5be45c551bcc08b62fde187d01c7), the "template method" of the claims file.
- Template (Methods 5.7.1, the claims file's "template method"): PosCheops left out; MEA band-pass
  300 to 6000 Hz, third-order Butterworth (Methods 5.7.1). The filter is applied forward and
  backward (`sosfiltfilt`), as the code's spikeinterface bandpass filter does by default; this is a
  standard choice. Waveforms cut 2 ms before and 5 ms after the peak; each centred on its
  negative peak on the largest channel, searched within +/- 2 ms of the patch peak
  (`process_mea_patch` default `center_ms=2`); the largest channel is the one with the largest
  absolute value of the uncentred median (`patch_triggered_average`); waveforms whose
  largest-channel amplitude (maximum absolute value, `clean_sta`) is more than 2 SD from the
  median are dropped; the template is the sample-wise median of the rest (Methods) and the mean
  (code, `clean_sta`) as a variant.
- Denoising: a channel is removed when its raw signal is constant in any of 10 one-second segments
  spread over the run, as `mea_patch.remove_blank_channels` does (n_segments=10,
  seconds_per_segments=1). Channels with a template peak-to-peak below 5 uV are also counted, as the
  code's feature notebooks threshold them (`thresh_uV = 5`).
- Stimulus segments: the stimulus is piecewise constant (ramps for PosCheops); a change of more
  than 3 pA between samples starts a new segment. The threshold is a standard choice that cannot
  change the result (the smallest step in the data is about 48 pA).
- Ramps: a PosCheops ramp is a run of samples more than 5 pA above the holding level (standard
  choice).

Threads: MEA reads are spread over processes, each with its own remote file.
"""

from __future__ import annotations

import re
from concurrent.futures import ProcessPoolExecutor

import h5py
import numpy as np
import remfile
from scipy.signal import butter, sosfiltfilt

DANDISET_ID = "000294"
DANDISET_VERSION = "0.260528.0854"

# The two neurons: NWB subject id, the paper's name, and the cell name of the paper's code.
CELLS = {"3148": "cell 1", "3436": "cell 2"}
CODE_NAMES = {"3148": "cell1_211006_3148", "3436": "cell1_211011_3436"}

EFEL_THRESHOLD = -20.0          # mV, mea_patch.get_peak_times
FREQ_MIN, FREQ_MAX, FILTER_ORDER = 300.0, 6000.0, 3   # Methods 5.7.1
MS_BEFORE, MS_AFTER = 2.0, 5.0  # cut-out, patch_triggered_average default
CENTER_MS = 2.0                 # process_mea_patch default
STD_THRESH = 2.0                # Methods 5.7.1, process_mea_patch
PTP_THRESHOLD_UV = 5.0          # feature notebooks, thresh_uV
BLANK_SEGMENTS, BLANK_SECONDS = 10, 1.0   # remove_blank_channels defaults
MARGIN_MS = 30.0                # filter margin around read blocks (standard choice)
MAX_BLOCK_CHUNKS = 3            # time chunks read at once (memory; standard choice)
STEP_JUMP_PA = 3.0
RAMP_THRESHOLD_PA = 5.0

# Pre-step timings of the paper's code (ecodes_cell_timings in the experimental feature notebooks).
CODE_TON_MS = {"idthres": 400, "firepattern": 500, "iv": 400, "idrest": 400, "apwaveform": 350,
               "hyperdepol": 400, "sahp": 400, "poscheops": 1000}

SERIES = re.compile(r"(response|stimulus)_(\w+?)_(run\d+)_(\d+)$")


# --- archive -----------------------------------------------------------------------------------

def asset_urls() -> dict:
    """Subject id -> S3 URL of its NWB file, at the pinned version."""
    from dandi.dandiapi import DandiAPIClient
    with DandiAPIClient() as client:
        ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        out = {}
        for asset in ds.get_assets():
            subject = asset.path.split("/")[0].replace("sub-", "")
            out[subject] = asset.get_content_url(follow_redirects=1, strip_query=True)
    return dict(sorted(out.items()))


def open_file(url: str) -> h5py.File:
    return h5py.File(remfile.File(url), "r")


def _s(x):
    return x.decode() if isinstance(x, bytes) else str(x)


def metadata(url: str) -> dict:
    """File-level metadata, the electrodes table, MEA series shapes and the icephys tables."""
    f = open_file(url)
    g = lambda p: _s(f[p][()]) if p in f else None
    out = {k: g(p) for k, p in {
        "identifier": "identifier", "session_description": "session_description",
        "session_start_time": "session_start_time", "subject_id": "general/subject/subject_id",
        "species": "general/subject/species", "subject_description": "general/subject/description",
        "institution": "general/institution", "lab": "general/lab"}.items()}
    subj = f["general/subject"]
    out["subject_fields"] = sorted(subj.keys())
    e = f["general/extracellular_ephys/electrodes"]
    out["electrodes"] = {c: e[c][:] for c in e.keys() if c not in ("group",)}
    out["electrodes"] = {c: (np.array([_s(v) for v in a]) if a.dtype.kind in "OS" else a)
                         for c, a in out["electrodes"].items()}
    mea = {}
    for name in f["acquisition"]:
        if name.startswith("ElectricalSeries"):
            s = f["acquisition"][name]
            ts = s["timestamps"]
            head = ts[:2001]
            mea[name] = dict(shape=s["data"].shape, chunks=s["data"].chunks, dtype=str(s["data"].dtype),
                             conversion=float(s["data"].attrs["conversion"]),
                             unit=_s(s["data"].attrs["unit"]), description=_s(s.attrs.get("description", "")),
                             n_electrodes=len(s["electrodes"]), t0=float(ts[0]), t1=float(ts[-1]),
                             rate=1.0 / float(np.median(np.diff(head))))
    out["mea"] = mea
    ie = f["general/intracellular_ephys"]
    ir = ie["intracellular_recordings"]
    out["ic_protocol_name"] = np.array([_s(v) for v in ir["protocol_name"][:]])
    out["ic_run"] = np.array([_s(v) for v in ir["run"][:]])
    sq = ie["sequential_recordings"]
    out["seq_index"] = sq["simultaneous_recordings_index"][:]
    out["seq_members"] = sq["simultaneous_recordings"][:]
    out["seq_type"] = np.array([_s(v) for v in sq["stimulus_type"][:]])
    out["n_repetitions"] = len(ie["repetitions"]["id"])
    a = f["acquisition"]
    first = sorted(n for n in a if n.startswith("response_"))[0]
    out["patch_attrs"] = {"data_unit": _s(a[first]["data"].attrs["unit"]),
                          "data_conversion": float(a[first]["data"].attrs["conversion"]),
                          "gain": float(a[first]["gain"][()])}
    st = f["stimulus/presentation"][first.replace("response", "stimulus")]
    out["stim_attrs"] = {"data_unit": _s(st["data"].attrs["unit"]),
                         "data_conversion": float(st["data"].attrs["conversion"])}
    out["confocal_shape"] = f["processing/imaging/confocal/Confocal max z projection"].shape
    return out


# --- patch data --------------------------------------------------------------------------------

def _read_run(args):
    url, run = args
    f = open_file(url)
    a, s = f["acquisition"], f["stimulus/presentation"]
    out = []
    for name in a:
        m = SERIES.match(name)
        if not m or m.group(1) != "response" or m.group(3) != run:
            continue
        r, st = a[name], s[name.replace("response", "stimulus", 1)]
        t = r["timestamps"][:]
        ti = st["timestamps"][:]
        out.append(dict(protocol=m.group(2), run=run, sweep=int(m.group(4)), v=r["data"][:],
                        t=t, i=st["data"][:], same_t=bool(np.array_equal(t, ti))))
    return sorted(out, key=lambda d: d["sweep"])


def load_patch(urls: dict, runs: dict, workers: int = 9) -> dict:
    """Subject -> list of sweeps (protocol, run, sweep, v, t, i), every run read in its own process."""
    jobs = [(subj, run) for subj in urls for run in runs[subj]]
    with ProcessPoolExecutor(min(workers, len(jobs))) as ex:
        res = list(ex.map(_read_run, [(urls[s], r) for s, r in jobs]))
    out = {s: [] for s in urls}
    for (s, _), sweeps in zip(jobs, res):
        out[s].extend(sweeps)
    return out


def runs_in_file(url: str) -> list:
    f = open_file(url)
    return sorted({SERIES.match(n).group(3) for n in f["acquisition"] if SERIES.match(n)})


def peak_times(t_s: np.ndarray, v_mv: np.ndarray) -> np.ndarray:
    """Spike peak times (s) by eFEL peak_time at -20 mV over the whole sweep (mea_patch.get_peak_times)."""
    import efel
    efel.set_setting("Threshold", EFEL_THRESHOLD)
    tr = {"T": t_s * 1e3, "V": v_mv, "stim_start": [t_s[0] * 1e3], "stim_end": [t_s[-1] * 1e3]}
    import warnings
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        pk = efel.get_feature_values([tr], ["peak_time"])[0]["peak_time"]
    return np.array([]) if pk is None else np.asarray(pk) / 1e3


def segments(sweep: dict) -> list:
    """Piecewise-constant stimulus segments: (start ms from sweep start, duration ms, level pA above
    the holding level). The holding level is the median of the first 10 ms."""
    t, i = sweep["t"], sweep["i"]
    dt = float(np.median(np.diff(t)))
    hold = float(np.median(i[: max(10, int(0.01 / dt))]))
    d = i - hold
    jumps = np.where(np.abs(np.diff(d)) > STEP_JUMP_PA)[0]
    edges = np.r_[0, jumps + 1, len(d)]
    out = []
    for a, b in zip(edges[:-1], edges[1:]):
        dur = (t[b - 1] - t[a]) * 1e3 + dt * 1e3
        if dur > 1.0:
            out.append(((t[a] - t[0]) * 1e3, dur, float(np.median(d[a:b]))))
    return out


def holding_current(sweep: dict) -> float:
    t, i = sweep["t"], sweep["i"]
    dt = float(np.median(np.diff(t)))
    return float(np.median(i[: max(10, int(0.01 / dt))]))


def ramps(sweep: dict) -> list:
    """PosCheops ramps: (start ms, rise ms, fall ms, peak pA above holding)."""
    t, i = sweep["t"], sweep["i"]
    d = i - holding_current(sweep)
    above = d > RAMP_THRESHOLD_PA
    idx = np.where(np.diff(above.astype(int)) != 0)[0] + 1
    bounds = np.r_[0, idx, len(d)]
    out = []
    for a, b in zip(bounds[:-1], bounds[1:]):
        if above[a] and (t[b - 1] - t[a]) > 0.2:
            k = a + int(np.argmax(d[a:b]))
            # extend to where the ramp leaves the holding level, by linear extrapolation of each side
            out.append(((t[a] - t[0]) * 1e3, (t[k] - t[a]) * 1e3, (t[b - 1] - t[k]) * 1e3, float(d[k])))
    return out


def onset_ms(sweep: dict) -> float:
    """Time of the first stimulus change, from the sweep start (ms)."""
    segs = segments(sweep)
    if len(segs) > 1:
        return segs[1][0]
    r = ramps(sweep)
    return r[0][0] if r else np.nan


# --- MEA -----------------------------------------------------------------------------------------

def _blank_segment(args):
    url, series, start, n = args
    f = open_file(url)
    x = f["acquisition"][series]["data"][start:start + n, :]
    import hashlib
    return np.all(np.diff(x.astype(np.int32), axis=0) == 0, axis=0), hashlib.sha1(x.tobytes()).hexdigest()


def blank_channels(url: str, series: str, n_frames: int, fs: float = 20000.0, workers: int = 8):
    """Channels constant in any of 10 one-second segments (remove_blank_channels), and a checksum of
    each segment's raw data (to find recordings deposited twice)."""
    n = int(BLANK_SECONDS * fs)
    starts = np.linspace(0, n_frames - n - 1, BLANK_SEGMENTS).astype(int)
    with ProcessPoolExecutor(workers) as ex:
        res = list(ex.map(_blank_segment, [(url, series, int(s), n) for s in starts]))
    blank = np.any([r[0] for r in res], axis=0)
    return blank, [r[1] for r in res]


def _cut_block(args):
    """Read frames [f0, f1), filter, and cut wide windows around the given spike frames."""
    url, series, f0, f1, frames, conv_uv, fs, wide = args
    f = open_file(url)
    x = f["acquisition"][series]["data"][f0:f1, :]
    sos = butter(FILTER_ORDER, [FREQ_MIN, FREQ_MAX], btype="bandpass", fs=fs, output="sos")
    out = np.zeros((len(frames), wide[0] + wide[1], x.shape[1]), dtype=np.float32)
    step = 128
    for c in range(0, x.shape[1], step):
        y = sosfiltfilt(sos, x[:, c:c + step].astype(np.float64) * conv_uv, axis=0)
        for k, fr in enumerate(frames):
            a = fr - f0 - wide[0]
            out[k, :, c:c + step] = y[a:a + wide[0] + wide[1]]
    return out


def mea_waveforms(url: str, series: str, mea_t: np.ndarray, spike_times: np.ndarray, conv_uv: float,
                  chunk_frames: int, fs: float = 20000.0, workers: int = 8):
    """Filtered waveforms (n_spikes, samples, channels) in a wide window, CENTER_MS on each side added
    to the cut-out, around the frames of the spike times. Blocks of whole time chunks of the HDF5
    dataset are read, with a margin for the filter; spikes too close to the series' ends are skipped.
    Returns the waveforms and the frames used."""
    wide = (int((MS_BEFORE + 2 * CENTER_MS) * fs / 1000), int((MS_AFTER + 2 * CENTER_MS) * fs / 1000))
    margin = int(MARGIN_MS * fs / 1000)
    frames = np.searchsorted(mea_t, spike_times).astype(np.int64)
    n = len(mea_t)
    ok = (frames - wide[0] - margin >= 0) & (frames + wide[1] + margin < n)
    frames = np.sort(frames[ok])
    chunk_of = frames // chunk_frames
    blocks, cur = [], []
    for c in np.unique(chunk_of):
        if cur and (c != cur[-1] + 1 or len(cur) >= MAX_BLOCK_CHUNKS):
            blocks.append(cur)
            cur = []
        cur.append(int(c))
    if cur:
        blocks.append(cur)
    jobs = []
    for b in blocks:
        fr = frames[np.isin(chunk_of, b)]
        f0 = max(0, int(fr.min()) - wide[0] - margin)
        f1 = min(n, int(fr.max()) + wide[1] + margin)
        jobs.append((url, series, f0, f1, fr, conv_uv, fs, wide))
    with ProcessPoolExecutor(workers) as ex:
        parts = list(ex.map(_cut_block, jobs))
    used = np.concatenate([j[4] for j in jobs]) if jobs else np.array([], dtype=np.int64)
    return (np.concatenate(parts) if parts else np.zeros((0, sum(wide), 0), np.float32)), used, wide


def template_from_waveforms(wf: np.ndarray, wide: tuple, fs: float = 20000.0, keep=None):
    """The template method on wide waveforms: largest channel from the uncentred median, centring on
    the negative peak within +/- CENTER_MS, 2 SD amplitude cleaning, median (and mean) template.
    `keep` is a boolean mask of channels to use (denoising)."""
    if keep is None:
        keep = np.ones(wf.shape[2], bool)
    w = wf[:, :, keep]
    c = int(CENTER_MS * fs / 1000)
    before, after = int(MS_BEFORE * fs / 1000), int(MS_AFTER * fs / 1000)
    sta = np.median(w, axis=0)
    max_ch = int(np.unravel_index(np.argmax(np.abs(sta)), sta.shape)[1])
    centre = wide[0]
    centred = np.zeros((w.shape[0], before + after, w.shape[2]), np.float32)
    shifts = np.zeros(w.shape[0], int)
    for k in range(w.shape[0]):
        m = int(np.argmin(w[k, centre - c:centre + c, max_ch])) - c
        shifts[k] = m
        centred[k] = w[k, centre + m - before:centre + m + after]
    amp = np.max(np.abs(centred[:, :, max_ch]), axis=1)
    med, sd = np.median(amp), np.std(amp)
    kept = (amp > med - STD_THRESH * sd) & (amp < med + STD_THRESH * sd)
    return dict(median=np.median(centred[kept], axis=0), mean=np.mean(centred[kept], axis=0),
                max_channel=max_ch, n_waveforms=w.shape[0], n_kept=int(kept.sum()), shifts_ms=shifts / fs * 1e3,
                amplitudes=amp, channels=np.where(keep)[0])


def amplitudes(template: np.ndarray, max_channel: int) -> dict:
    """Absolute negative peak and peak-to-peak on a channel (uV)."""
    tr = template[:, max_channel]
    return {"neg_peak": float(-tr.min()), "ptp": float(np.ptp(tr))}
