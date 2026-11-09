"""Loading and checks for the high-gamma ECoG of dandiset 001193.

Zhu, Xu, Lu, Hu et al. (2022), Nature Human Behaviour 6, 1104-1111, doi:10.1038/s41562-022-01334-6.

Each NWB file holds one experimental block of one participant: an ElectricalSeries `ECoG`
(samples by 256 electrodes, float32, stated in volts at a stated rate of 400 Hz) and an
electrode table with the columns location, group, group_name and filtering. Files are
streamed from the archive at the pinned version; nothing is written to disk. Each file is
reduced as it loads to the summaries the notebook prints, so that no file is held in memory
after it has been read.

Where the parameters come from:

- `MIN_LINGUISTIC_TRIALS_PER_BLOCK` and `MIN_TRIAL_S`, used to judge the stated sampling rate
  against the length of a block, are from the Methods ("The Chinese language and stimuli
  design", paragraphs 3 and 4): 32 sentences in each of CORR, SYN-P, SYN-C and SEM for every
  participant, "divided into four blocks", so at least 128 / 4 = 32 trials per block; each
  trial an 800 ms fixation, a 500 ms blank and at least six words at 500 ms each, so at least
  4.3 s before the question. The COM or NL trials and the response time only lengthen a
  block, so both numbers are lower bounds.
- `PAPER_HGA_HZ` = 100 Hz is the rate of the paper's HGA (Methods, "Frequency component
  extraction", paragraph 2: "the HGA was down-sampled to 100 Hz and z scored relative to the
  mean and standard deviation of the data within each experimental block").
- `WORD_SOA_S` = 0.5 s is the word onset asynchrony (400 ms word, 100 ms interval; same
  Methods paragraph). The spectral check at that period, and the flanking band used as its
  reference (`FLANK`), are standard choices for a check that decides no claim.
- `FINGERPRINT_SAMPLES` (the length of the differenced channel-mean trace, from the middle of
  each block, compared with every stretch of every other file to look for recordings deposited
  twice) is a standard choice that cannot change a result: an identical block gives a
  correlation of 1 at any length. The threshold of 3 z for the end of the start-of-block
  transient is a standard choice for a description that decides no claim.
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy.signal import correlate, welch

DANDISET_ID = "001193"
DANDISET_VERSION = "0.240921.1006"

PAPER_HGA_HZ = 100.0
MIN_LINGUISTIC_TRIALS_PER_BLOCK = 32
MIN_TRIAL_S = 0.8 + 0.5 + 6 * 0.5
WORD_SOA_S = 0.5
FLANK = (0.8, 1.25)            # flanking band, as a factor of the frequency tested
FINGERPRINT_SAMPLES = 4000


def _text(value):
    if isinstance(value, bytes):
        return value.decode()
    if isinstance(value, np.ndarray):
        return [_text(v) for v in value.tolist()]
    return value


def assets():
    """The dandiset's assets at the pinned version, sorted by path."""
    dandiset = DandiAPIClient().get_dandiset(DANDISET_ID, DANDISET_VERSION)
    return sorted(dandiset.get_assets(), key=lambda a: a.path)


def version_metadata(version: str = DANDISET_VERSION):
    """A version's metadata from the DANDI API, and its assets as {path: (blob, size)}."""
    dandiset = DandiAPIClient().get_dandiset(DANDISET_ID, version)
    files = {a.path: (a.get_raw_metadata().get("digest", {}).get("dandi:dandi-etag"), a.size)
             for a in dandiset.get_assets()}
    return dandiset.get_raw_metadata(), files


def published_versions():
    """Every version of the dandiset the API lists."""
    return [v.identifier for v in DandiAPIClient().get_dandiset(DANDISET_ID).get_versions()]


def _all_paths(f):
    names = []
    f.visit(lambda n: names.append(n) if not n.startswith("specifications") else None)
    return names


def _describe(f, top):
    """Every object under `top`, as "path (Group)" or "path (Dataset shape dtype)", with neurodata types."""
    out = []

    def visit(name, obj):
        kind = obj.attrs.get("neurodata_type")
        kind = f" [{_text(kind)}]" if kind is not None else ""
        if isinstance(obj, h5py.Dataset):
            out.append(f"{top}/{name} (Dataset {obj.shape} {obj.dtype}){kind}")
        else:
            out.append(f"{top}/{name} (Group){kind}")
    f[top].visititems(visit)
    return out


def _peak_excess(spectrum, freqs, target):
    """log10 power at `target` (cycles per sample) minus the median log10 power in the flanking band."""
    i = int(np.argmin(np.abs(freqs - target)))
    flank = ((freqs > target * FLANK[0]) & (freqs < target * 0.95)) | ((freqs > target * 1.05) & (freqs < target * FLANK[1]))
    return float(np.log10(spectrum[i]) - np.median(np.log10(spectrum[flank])))


def summarize(asset):
    """Read one file and reduce it to what the notebook checks."""
    url = asset.get_content_url(follow_redirects=1, strip_query=True)
    with h5py.File(remfile.File(url), "r") as f:
        series = f["acquisition/ECoG"]
        data = series["data"][:]
        electrodes = f["general/extracellular_ephys/electrodes"]
        groups = [p for p in _all_paths(f) if p.split("/")[0] in ("stimulus", "intervals", "analysis", "processing", "units")]
        out = {
            "path": asset.path,
            "asset_size": asset.size,
            "identifier": _text(f["identifier"][()]),
            "subject_id": _text(f["general/subject/subject_id"][()]),
            "sex": _text(f["general/subject/sex"][()]),
            "age": _text(f["general/subject/age"][()]),
            "subject_description": _text(f["general/subject/description"][()]),
            "species": _text(f["general/subject/species"][()]),
            "session_start": _text(f["session_start_time"][()]),
            "session_description": _text(f["session_description"][()]),
            "experiment_description": _text(f["general/experiment_description"][()]),
            "related_publications": _text(f["general/related_publications"][()]),
            "series_description": _text(series.attrs.get("description")),
            "unit": _text(series["data"].attrs.get("unit")),
            "conversion": float(series["data"].attrs.get("conversion")),
            "rate": float(series["starting_time"].attrs["rate"]),
            "starting_time": float(series["starting_time"][()]),
            "n_samples": data.shape[0],
            "n_channels": data.shape[1],
            "series_electrodes": series["electrodes"][:].tolist(),
            "electrode_columns": _text(electrodes.attrs["colnames"]),
            "locations": sorted(set(_text(electrodes["location"][:]))),
            "filtering": sorted(set(_text(electrodes["filtering"][:]))),
            "group_counts": {g: int(n) for g, n in zip(*np.unique(_text(electrodes["group_name"][:]), return_counts=True))},
            "group_descriptions": {g: _text(f[f"general/extracellular_ephys/{g}"].attrs["description"]) for g in ("Grid_1", "Grid_2")},
            "group_locations": {g: _text(f[f"general/extracellular_ephys/{g}"].attrs["location"]) for g in ("Grid_1", "Grid_2")},
            "other_objects": groups,
            "top_level": sorted(f.keys()),
            "acquisition_listing": _describe(f, "acquisition"),
            "general_listing": _describe(f, "general"),
            "data_storage": {"chunks": series["data"].chunks, "compression": series["data"].compression,
                             "dtype": str(series["data"].dtype)},
            "has_trials": "intervals/trials" in f,
        }
    out["n_nan"] = int(np.isnan(data).sum())
    mean, std = data.mean(0), data.std(0)
    out["channel_mean_absmax"] = float(np.abs(mean).max())
    out["channel_std_min"], out["channel_std_max"] = float(std.min()), float(std.max())
    out["min"], out["max"] = float(data.min()), float(data.max())
    out["p01"], out["p50"], out["p99"] = (float(v) for v in np.percentile(data, [1, 50, 99]))
    out["frac_above_10"] = float((data > 10).mean())
    out["first_sample_median"] = float(np.median(data[0]))
    # identical channels within the file
    hashes = [hash(data[:, c].tobytes()) for c in range(data.shape[1])]
    out["n_duplicate_channels"] = int(len(hashes) - len(set(hashes)))
    # spectral check at the word rate under the stated and the paper's rate
    freqs, spectrum = welch(data, fs=1.0, nperseg=4000, axis=0)
    spectrum = spectrum.mean(1)
    out["excess_word_rate_if_400"] = _peak_excess(spectrum, freqs, 1.0 / (WORD_SOA_S * 400.0))
    out["excess_word_rate_if_100"] = _peak_excess(spectrum, freqs, 1.0 / (WORD_SOA_S * PAPER_HGA_HZ))
    # the channel mean, differenced so that slow drifts and the transient at the start of a block
    # (shared by many files) do not make unrelated files look alike; the fingerprint is taken from
    # the middle of the block
    trace = np.diff(data.mean(1))
    middle = len(trace) // 2
    out["fingerprint"] = trace[middle:middle + FINGERPRINT_SAMPLES]
    out["trace"] = trace
    channel_median = np.median(data, axis=1)
    out["start_transient_samples"] = int(np.argmax(channel_median < 3.0)) if channel_median[0] >= 3.0 else 0
    return out


def load_all(workers: int = 8):
    """Summaries of every file, in path order."""
    with ThreadPoolExecutor(workers) as pool:
        return list(pool.map(summarize, assets()))


def best_match(fingerprint, trace):
    """Largest Pearson correlation of `fingerprint` with any equally long stretch of `trace`."""
    n = len(fingerprint)
    if len(trace) < n:
        return np.nan
    a = (fingerprint - fingerprint.mean()) / fingerprint.std()
    t = trace.astype(np.float64)
    dots = correlate(t, a, mode="valid", method="fft")
    c1 = np.concatenate([[0.0], np.cumsum(t)])
    c2 = np.concatenate([[0.0], np.cumsum(t * t)])
    s1, s2 = c1[n:] - c1[:-n], c2[n:] - c2[:-n]
    sd = np.sqrt(np.maximum(s2 / n - (s1 / n) ** 2, 1e-12))
    return float((dots / (n * sd)).max())
