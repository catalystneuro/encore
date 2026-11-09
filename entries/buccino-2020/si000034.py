"""Loading and checks for dandiset 000034, the recordings of Buccino et al. (2020), eLife 9:e61834,
"SpikeInterface, a unified framework for spike sorting", doi:10.7554/eLife.61834.

The dandiset holds six NWB files: a 15 min Neuropixels recording of mouse 412804 and two manual
curations of its Kilosort2 output (spike times only), a simulated (MEArec) Neuropixels recording
with its 250 ground-truth units, a rat cortex Neuropixels recording (dataset spe-c1) and a mouse
retina Biocam recording. Files are streamed from the archive at the pinned version with remfile
and h5py; nothing is written to disk.

Where the parameters come from:

- Spike times are turned into frames as spikeextractors 0.8.4 NwbSortingExtractor does
  (`round(t * fs)`, frames > 0), at the sampling rate of the recording the curations were made
  from (30 kHz); the curated files carry no rate of their own.
- The comparison of the two curations is spikecomparison 0.2.6 `compare_two_sorters` with its
  defaults (delta_time 0.4 ms, match_score 0.5, chance_score 0.1), as the claims file's opening
  comment and fig4a-curators-agree give it. spikeextractors 0.8.4 uses NumPy aliases removed in
  NumPy 2 (`np.float`, `np.int`, `np.Inf`, `np.product`, `np.in1d`); `legacy_numpy_aliases`
  restores them as the builtins and functions they stood for, which changes no computation.
- The band-pass filter (300 to 6000 Hz, third-order Butterworth, zero phase), the common median
  reference and the lag range of the clock check are standard choices for a data check; they
  decide no outcome.
"""

from __future__ import annotations

import shutil
import subprocess
import time

import h5py
import numpy as np
import remfile
import requests
from scipy.signal import butter, sosfiltfilt

DANDISET_ID = "000034"
DANDISET_VERSION = "0.211030.0713"
API = "https://api.dandiarchive.org/api"

CURATED_1 = "sub-mouse412804/sub-mouse412804_ses-20200824T155542.nwb"
CURATED_2 = "sub-mouse412804/sub-mouse412804_ses-20200824T155543.nwb"
MOUSE = "sub-mouse412804/sub-mouse412804_ecephys.nwb"
MEAREC = "sub-MEAREC-250neuron-Neuropixels/sub-MEAREC-250neuron-Neuropixels_ecephys.nwb"
RAT = "sub-c1/sub-c1_ecephys.nwb"
RETINA = "sub-P29-16-05-14-retina02-left/sub-P29-16-05-14-retina02-left_ecephys.nwb"
RECORDINGS = {"mouse412804": MOUSE, "MEArec": MEAREC, "rat c1": RAT, "retina": RETINA}

CURATION_FS = 30000.0      # the mouse recording's rate, used for the curated spike times
BAND = (300.0, 6000.0)     # standard choice, clock check only


def list_assets(version: str = DANDISET_VERSION) -> list[dict]:
    """Path, size and asset id of every asset of a version of the dandiset."""
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{version}/assets/?page_size=200"
    out = []
    while url:
        page = requests.get(url, timeout=60).json()
        out += [{"path": a["path"], "size": a["size"], "asset_id": a["asset_id"]} for a in page["results"]]
        url = page.get("next")
    return out


def version_info(version: str = DANDISET_VERSION) -> dict:
    return requests.get(f"{API}/dandisets/{DANDISET_ID}/versions/{version}/info/", timeout=60).json()


def open_nwb(path: str, version: str = DANDISET_VERSION) -> h5py.File:
    """Open an asset of the pinned version for streaming."""
    asset = next(a for a in list_assets(version) if a["path"] == path)
    s3 = requests.head(f"{API}/assets/{asset['asset_id']}/download/", allow_redirects=True, timeout=60).url
    return h5py.File(remfile.File(s3), "r")


def hdf5_tree(f: h5py.File, skip: str = "specifications") -> list[str]:
    """Every group and dataset of a file (shape and type of datasets), without the cached schema."""
    out = []

    def visit(name, obj):
        if name.startswith(skip):
            return
        out.append(f"{name} {obj.shape} {obj.dtype}" if isinstance(obj, h5py.Dataset) else f"{name}/")

    f.visititems(visit)
    return out


def bulk_read_rate(path: str, n_bytes: int, version: str = DANDISET_VERSION) -> dict:
    """Time one ranged GET of the first n_bytes of an asset, held in memory and discarded."""
    asset = next(a for a in list_assets(version) if a["path"] == path)
    s3 = requests.head(f"{API}/assets/{asset['asset_id']}/download/", allow_redirects=True, timeout=60).url
    got, t0 = 0, time.time()
    with requests.get(s3, headers={"Range": f"bytes=0-{n_bytes - 1}"}, stream=True, timeout=300) as r:
        r.raise_for_status()
        for block in r.iter_content(8 * 2**20):
            got += len(block)
    secs = time.time() - t0
    return {"bytes": got, "seconds": secs, "mb_per_s": got / 2**20 / secs, "file_bytes": asset["size"]}


def _text(x):
    return x.decode() if isinstance(x, bytes) else str(x)


def describe(f: h5py.File) -> dict:
    """Subject, session and the raw series of one file (no data read beyond metadata)."""
    out = {k: _text(f["general/subject"][k][()]) for k in f["general/subject"]}
    out["session_start_time"] = _text(f["session_start_time"][()])
    if "ElectricalSeries" in f.get("acquisition", {}):
        es = f["acquisition/ElectricalSeries"]
        d = es["data"]
        rate = float(es["starting_time"].attrs["rate"])
        out.update(frames=d.shape[0], channels=d.shape[1], dtype=str(d.dtype), chunks=d.chunks,
                   rate_hz=rate, duration_s=d.shape[0] / rate, starting_time=float(es["starting_time"][()]),
                   conversion=float(d.attrs["conversion"]), unit=_text(d.attrs["unit"]),
                   offset=float(d.attrs["offset"]) if "offset" in d.attrs else None)
    if "units" in f:
        out["units"] = int(f["units/id"].shape[0])
        out["unit_columns"] = [_text(c) for c in f["units"].attrs["colnames"]]
    return out


def load_units(f: h5py.File) -> dict[int, np.ndarray]:
    """Spike times (s) per unit id, from the Units table."""
    st = f["units/spike_times"][:]
    idx = f["units/spike_times_index"][:]
    ids = f["units/id"][:]
    return {int(u): t for u, t in zip(ids, np.split(st, idx[:-1]))}


def to_frames(times: np.ndarray, fs: float = CURATION_FS) -> np.ndarray:
    """As spikeextractors 0.8.4 NwbSortingExtractor.get_unit_spike_train: round, keep frames > 0."""
    frames = np.round(np.asarray(times) * fs).astype("int64")
    return frames[frames > 0]


def read_block(f: h5py.File, n_frames: int, channels: slice = slice(None)):
    """Read the first n_frames of the raw series; return the values and the seconds it took."""
    t0 = time.time()
    x = f["acquisition/ElectricalSeries/data"][0:n_frames, channels]
    return x, time.time() - t0


def bandpass_cmr(x: np.ndarray, fs: float) -> np.ndarray:
    """Band-pass and common median reference (standard choices, for the clock check)."""
    sos = butter(3, BAND, btype="band", fs=fs, output="sos")
    y = sosfiltfilt(sos, x.astype("float64"), axis=0)
    return y - np.median(y, axis=1, keepdims=True)


def lag_scan(y: np.ndarray, trains: dict[int, np.ndarray], lags: np.ndarray, min_spikes: int,
             rng: np.random.Generator, margin: int = 100) -> dict:
    """For each unit with enough spikes in the block, the mean trace at its spike frames shifted by
    each lag, and its largest negative deflection over channels. If the spike times share the
    recording's clock, the deflection peaks at lag 0. Random frames give the reference."""
    n = y.shape[0]
    best, amp0, amp_rand, units = [], [], [], []
    for u, fr in trains.items():
        fr = fr[(fr > margin) & (fr < n - margin)]
        if len(fr) < min_spikes:
            continue
        a = np.array([(-y[fr + L]).mean(0).max() for L in lags])
        rnd = np.sort(rng.integers(margin, n - margin, len(fr)))
        units.append(u)
        best.append(int(lags[a.argmax()]))
        amp0.append(float(a[lags == 0][0]))
        amp_rand.append(float((-y[rnd]).mean(0).max()))
    return {"unit": np.array(units), "best_lag": np.array(best), "amp_at_0": np.array(amp0),
            "amp_random": np.array(amp_rand)}


def legacy_numpy_aliases() -> list[str]:
    """Restore the NumPy names spikeextractors 0.8.4 and spikecomparison 0.2.6 use."""
    added = []
    for name, value in [("float", float), ("int", int), ("Inf", np.inf), ("product", np.prod),
                        ("in1d", np.isin)]:
        if name not in np.__dict__:
            setattr(np, name, value)
            added.append(name)
    return added


def numpy_sorting(trains: dict[int, np.ndarray], fs: float = CURATION_FS):
    """A spikeextractors 0.8.4 sorting from frames per unit."""
    import spikeextractors as se
    times = np.concatenate([trains[u] for u in trains])
    labels = np.concatenate([np.full(len(trains[u]), u) for u in trains])
    s = se.NumpySortingExtractor()
    s.set_times_labels(times, labels)
    s.set_sampling_frequency(fs)
    return s


def compare_two(trains1, trains2, name1="C1", name2="C2", **kwargs):
    """spikecomparison 0.2.6 compare_two_sorters, defaults unless given."""
    import spikecomparison as sc
    return sc.compare_two_sorters(numpy_sorting(trains1), numpy_sorting(trains2), name1, name2, **kwargs)


def environment() -> dict:
    """What the sorters the paper ran would need: MATLAB (Kilosort2, IronClust, HDSort), a CUDA
    GPU (Kilosort2), MPI (SpyKING Circus)."""
    gpu = None
    if shutil.which("nvidia-smi"):
        gpu = subprocess.run(["nvidia-smi", "-L"], capture_output=True, text=True).stdout.strip()
    return {"matlab": shutil.which("matlab"), "nvcc": shutil.which("nvcc"), "nvidia-smi": shutil.which("nvidia-smi"),
            "gpu": gpu, "mpiexec": shutil.which("mpiexec")}
