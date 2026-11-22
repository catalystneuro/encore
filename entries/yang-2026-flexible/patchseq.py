"""Loading and cell-level features for the Patch-seq recordings of DANDI:000020, as Yang (2026) uses them.

Where each parameter comes from:

- The dataset version, ``VERSION``, is the one the paper cites (README of the paper's code, "Data")
  and the only published version of the dandiset.
- Features are the cell-level features of the Allen Institute IPFX package (Methods,
  "Electrophysiological feature extraction"), computed per regime with IPFX's
  ``extract_cell_long_square_features``, ``extract_cell_short_square_features`` and
  ``extract_cell_ramp_features``, the parts of ``extract_data_set_features`` (claim
  table1-phenotype-spaces, reading 1a). ``extract_data_set_features`` itself also computes
  per-sweep features of every current-clamp sweep, which the paper does not use and which fail on
  sweeps without epochs; so only its per-regime parts are run (assumption, recorded).
- Empty epoch fields are dropped before IPFX builds a sweep, and only sweeps with both an
  ``experiment`` and a ``stim`` epoch are used: the code's ``repair_nwb_epochs`` and sweep filter
  (scripts/q1_split_half_long_square.py, commit 61a5a41), cited by the claims file.
- Flattening of the features into ``feat.<regime>.<key>`` columns follows the code's
  ``_pack_long_square_features``, ``pack_cell_record`` and ``flatten`` (same script), applied to all
  three regimes: the IPFX cell feature record plus each regime's nested feature dictionary, without
  the spike and sweep lists.
- ``extract_ok`` (Methods, "cells with extract_ok = 1") is not defined in the paper or the code,
  whose IPFX driver script is missing. Here it is 1 when the file could be opened as an IPFX data
  set and the three regime extractions ran, each regime being allowed to fail on its own (its
  features then missing), as IPFX's own cell state counts a cell failed only when every part
  failed. Assumption, recorded.
- The split-half extraction (claim split-half-reliability) is the code's ``extract_one_split``:
  at least four usable long squares, candidate splits in the code's order, at least two sweeps per
  half, the subthreshold minimum amplitude from the coarse long squares. Its random split uses the
  claim's seed (protocol), not the code's seed 0.
- The clock check takes, for each cell, the long square with the most negative amplitude, and
  the mean voltage, relative to a baseline 100 to 50 ms before stimulus onset, in the 10 ms just
  before the onset ("pre"), 15 to 25 ms after it ("post"), and in the last 100 ms of the stimulus
  ("dv"). The windows are a standard choice for a check, which cannot change a claim's result.
  For the check of recordings deposited twice, it also keeps the SHA-1 of that sweep's voltage
  trace and one SHA-1 over the voltage traces of all the cell's usable long squares.
"""

from __future__ import annotations

import hashlib
import io
import logging
import multiprocessing as mp
import os
import warnings
import zlib
from concurrent.futures import ProcessPoolExecutor, as_completed

# one linear-algebra thread per process: the extraction runs several processes at once (set before numpy loads)
for _var in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_var, "1")

import numpy as np  # noqa: E402
import requests  # noqa: E402

DANDISET = "000020"
VERSION = "0.210913.1639"
API = "https://api.dandiarchive.org/api"
PAPER_KEY = "yang-2026-flexible"

SKIP_FEATURE_KEYS = {"spikes", "sweeps", "spiking_sweeps", "subthreshold_sweeps",
                     "subthreshold_membrane_property_sweeps", "common_amp_sweeps"}
LONG_RECORD = {"vrest", "ri", "sag", "tau", "vm_for_sag", "f_i_curve_slope", "adaptation", "latency", "avg_isi"}
RECORD_SUFFIX = {"_long_square": "long_squares", "_ramp": "ramps", "_short_square": "short_squares"}
REGIMES = {"long_pulse": "long_squares", "ramp": "ramps", "brief_pulse": "short_squares"}
MIN_USABLE = 4
MIN_SWEEPS_PER_HALF = 2


def seed_of(claim: str) -> int:
    """The claim's seed (protocol, author step 3)."""
    return zlib.crc32(f"{PAPER_KEY}/{claim}".encode())


def list_assets(version: str = VERSION) -> list[dict]:
    url = f"{API}/dandisets/{DANDISET}/versions/{version}/assets/?page_size=1000"
    out = []
    while url:
        r = requests.get(url, timeout=120)
        r.raise_for_status()
        js = r.json()
        out += js["results"]
        url = js["next"]
    return out


def _as_float(value):
    try:
        num = float(value)
    except (TypeError, ValueError):
        return None
    return None if num != num else num


def _flatten(prefix, obj, out):
    if obj is None:
        return
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in SKIP_FEATURE_KEYS:
                continue
            _flatten(f"{prefix}{k}.", v, out)
        return
    num = _as_float(obj)
    if num is not None:
        out[prefix.rstrip(".")] = num


def _pack_cell_record(cell_record, rec):
    for key, value in cell_record.items():
        num = _as_float(value)
        if num is None:
            continue
        proto, name = None, key
        for suffix, protocol in RECORD_SUFFIX.items():
            if key.endswith(suffix):
                proto, name = protocol, key[: -len(suffix)]
                break
        if proto is None:
            if key in LONG_RECORD:
                proto = "long_squares"
            else:
                continue
        rec[f"feat.{proto}.{name}"] = num


def pack(cell_features: dict) -> dict:
    """Flatten IPFX cell features as the paper's code does."""
    from ipfx.feature_record import build_cell_feature_record
    rec = {}
    full = {k: (cell_features.get(k) or {}) for k in ("long_squares", "ramps", "short_squares")}
    try:
        cell_record = build_cell_feature_record(full)
    except Exception:
        cell_record = {}
    if isinstance(cell_record, dict):
        _pack_cell_record(cell_record, rec)
    _flatten("feat.", {k: v for k, v in full.items() if v}, rec)
    return rec


def _repair_epochs():
    from ipfx.sweep import Sweep
    if getattr(Sweep.__init__, "_prg_epoch_repair", False):
        return
    original = Sweep.__init__

    def patched(self, t, v, i, clamp_mode, sampling_rate, sweep_number=None, epochs=None):
        if epochs:
            epochs = {k: val for k, val in epochs.items() if val is not None}
        original(self, t, v, i, clamp_mode, sampling_rate, sweep_number=sweep_number, epochs=epochs)

    patched._prg_epoch_repair = True
    Sweep.__init__ = patched


def candidate_splits(sns, rng, amps=None):
    """The code's candidate splits, in its order (scripts/q1_split_half_long_square.py)."""
    sns = [int(s) for s in sns]
    out = []
    even = sorted(s for s in sns if s % 2 == 0)
    odd = sorted(s for s in sns if s % 2 == 1)
    out.append((even, odd, "odd_even_sweep_number"))
    sns_s = sorted(sns)
    out.append((sns_s[0::2], sns_s[1::2], "interleaved_index"))
    if amps:
        ordered = [s for s, _a, _n in sorted(((s, amps.get(s, 0.0), s) for s in sns), key=lambda t: (t[1], t[2]))]
        out.append((ordered[0::2], ordered[1::2], "amplitude_interleaved"))
    perm = rng.permutation(len(sns_s))
    mid = max(MIN_SWEEPS_PER_HALF, len(sns_s) // 2)
    if len(sns_s) - mid >= MIN_SWEEPS_PER_HALF:
        out.append((sorted(int(sns_s[i]) for i in perm[:mid]), sorted(int(sns_s[i]) for i in perm[mid:]), "random"))
    seen, uniq = set(), []
    for a, b, rule in out:
        if len(a) < MIN_SWEEPS_PER_HALF or len(b) < MIN_SWEEPS_PER_HALF:
            continue
        key = (tuple(a), tuple(b), rule)
        if key in seen:
            continue
        seen.add(key)
        uniq.append((a, b, rule))
    return uniq


def _fetch(asset_id: str, tries: int = 4) -> bytes:
    url = f"{API}/assets/{asset_id}/download/"
    for k in range(tries):
        try:
            r = requests.get(url, timeout=300)
            r.raise_for_status()
            return r.content
        except Exception:
            if k == tries - 1:
                raise
    raise RuntimeError("unreachable")


class _Series:
    """The fields of a pynwb PatchClampSeries that IPFX reads, taken from the HDF5 group directly."""

    def __init__(self, group, h5):
        ntype = group.attrs["neurodata_type"]
        ntype = ntype.decode() if isinstance(ntype, bytes) else str(ntype)
        self.is_stimulus = ntype.endswith("StimulusSeries")
        self.clamp_mode = "VoltageClamp" if ntype.startswith("VoltageClamp") else (
            "CurrentClamp" if ntype.startswith(("CurrentClamp", "IZero")) else ntype)
        self.data = group["data"]
        self.conversion = float(self.data.attrs.get("conversion", 1.0))
        unit = self.data.attrs.get("unit", "")
        self.unit = unit.decode() if isinstance(unit, bytes) else str(unit)
        self.rate = float(group["starting_time"].attrs["rate"])
        desc = group.attrs.get("stimulus_description", "")
        self.stimulus_description = desc.decode() if isinstance(desc, bytes) else str(desc)

        def scalar(key):
            if key not in group:
                return None
            val = group[key][()]
            return float(np.ravel(val)[0]) if np.size(val) else None
        self.gain = scalar("gain")
        self.bias_current = scalar("bias_current")
        self.bridge_balance = scalar("bridge_balance")


def _fast_reader(base):
    """A subclass of an IPFX NWB reader that builds its sweep table from HDF5 without pynwb.

    pynwb builds an object for every group in the file, about a third of the time IPFX spends on a
    cell; IPFX itself reads only the sweep table and, per sweep, the data, conversion, unit, rate,
    gain, stimulus description, bias current and bridge balance of its two series, which this
    reader takes from the same HDF5 fields pynwb reads them from. ``check_fast_reader`` in the
    notebook compares the features it gives with those of IPFX's own reader."""

    class Fast(base):
        def load_nwb(self, nwb_file, load_into_memory=True):
            import h5py
            self.nwb_file = nwb_file
            h5 = h5py.File(nwb_file, "r")
            st = h5["general/intracellular_ephys/sweep_table"]
            numbers = st["sweep_number"][:]
            refs = st["series"][:]
            index = st["series_index"][:]
            self._by_sweep = {}
            start = 0
            for row, stop in enumerate(index):
                for ref in refs[start:stop]:
                    self._by_sweep.setdefault(int(numbers[row]), []).append(_Series(h5[ref], h5))
                start = stop
            self._h5 = h5
            self.nwb = None

        def _get_series(self, sweep_number, series_class):
            want_stimulus = series_class == self.STIMULUS
            found = [s for s in self._by_sweep.get(int(sweep_number), []) if s.is_stimulus == want_stimulus]
            if len(found) != 1:
                raise ValueError(f"Found {len(found)} {'stimulus' if want_stimulus else 'response'} series "
                                 f"for sweep number {sweep_number}.")
            return found[0]

        def get_sweep_attrs(self, sweep_number):
            rs = self._get_series(sweep_number, self.RESPONSE)
            attrs = {"gain": rs.gain, "stimulus_description": rs.stimulus_description,
                     "sweep_number": sweep_number, "clamp_mode": rs.clamp_mode}
            if rs.clamp_mode == "CurrentClamp":
                attrs.update(bias_current=rs.bias_current, bridge_balance=rs.bridge_balance)
            elif rs.clamp_mode != "VoltageClamp":
                raise ValueError(f"Must be response series {self.RESPONSE} ")
            return attrs

        @property
        def sweep_numbers(self):
            return np.unique(np.array(sorted(self._by_sweep), dtype=int))

    Fast.__name__ = "Fast" + base.__name__
    return Fast


def open_data_set(data: bytes, fast: bool = True):
    """The IPFX data set of a file held in memory, built as ``ipfx.dataset.create.create_ephys_data_set``
    builds it; with ``fast``, its reader takes the sweeps from HDF5 directly (``_fast_reader``)."""
    from ipfx.dataset.create import create_ephys_data_set, get_nwb_version, is_file_mies
    if not fast:
        return create_ephys_data_set(nwb_file=io.BytesIO(data))
    import ipfx.json_utilities as ju
    from ipfx.dataset.ephys_data_set import EphysDataSet
    from ipfx.dataset.hbg_nwb_data import HBGNWBData
    from ipfx.dataset.labnotebook import LabNotebookReaderIgorNwb
    from ipfx.dataset.mies_nwb_data import MIESNWBData
    from ipfx.stimulus import StimulusOntology
    if get_nwb_version(io.BytesIO(data))["major"] != 2:
        raise ValueError("Unsupported NWB version")
    ontology = StimulusOntology(ju.read(StimulusOntology.DEFAULT_STIMULUS_ONTOLOGY_FILE))
    if is_file_mies(io.BytesIO(data)):
        nwb_data = _fast_reader(MIESNWBData)(io.BytesIO(data), LabNotebookReaderIgorNwb(io.BytesIO(data)), ontology)
    else:
        nwb_data = _fast_reader(HBGNWBData)(io.BytesIO(data), ontology)
    return EphysDataSet(sweep_info=None, data=nwb_data)


def extract_cell(asset: dict, split_seed: int | None = None, fast: bool = True) -> dict:
    """Stream one NWB file into memory (never to disk) and compute everything the notebook needs from it."""
    warnings.filterwarnings("ignore")
    logging.disable(logging.WARNING)
    stem = asset["path"].split("/")[-1].rsplit(".", 1)[0]
    rec = {"file_stem": stem, "path": asset["path"], "size": asset["size"], "extract_ok": 0, "error": "",
           "features": {}, "failed": {}, "split": None, "clock": None}
    try:
        _repair_epochs()
        import h5py
        import ipfx.data_set_features as dsf
        import ipfx.stim_features as stf
        data = _fetch(asset["asset_id"])
        with h5py.File(io.BytesIO(data), "r") as h5:
            g = h5["general"]
            for key, path in (("genotype", "subject/genotype"), ("session_id", "session_id"),
                              ("subject_id", "subject/subject_id"), ("sex", "subject/sex"), ("age", "subject/age")):
                val = g[path][()] if path in g else b""
                rec[key] = val.decode() if isinstance(val, bytes) else str(val)
        ds = open_data_set(data, fast)
        del data
        original_get = ds.get_sweep_numbers
        allowed = {"set": None}

        has_epochs = {}

        def filtered(*args, **kwargs):
            keep = []
            for sn in original_get(*args, **kwargs):
                if allowed["set"] is not None and int(sn) not in allowed["set"]:
                    continue
                if int(sn) not in has_epochs:
                    sw = ds.sweep(int(sn))
                    has_epochs[int(sn)] = bool(sw.epochs.get("experiment") and sw.epochs.get("stim"))
                if has_epochs[int(sn)]:
                    keep.append(sn)
            return keep

        ds.get_sweep_numbers = filtered
        cc = ds.CURRENT_CLAMP
        names = {"long_squares": ds.ontology.long_square_names, "short_squares": ds.ontology.short_square_names,
                 "ramps": ds.ontology.ramp_names}
        rec["n_sweeps"] = {}
        for k, v in names.items():
            try:
                rec["n_sweeps"][k] = len(ds.get_sweep_numbers(v, clamp_mode=cc))
            except IndexError:  # IPFX raises when a cell has no sweep of the kind
                rec["n_sweeps"][k] = 0
        cf = {}
        f1, s1 = dsf.extract_cell_long_square_features(ds)
        f2, s2 = dsf.extract_cell_short_square_features(ds)
        f3, s3 = dsf.extract_cell_ramp_features(ds)
        cf["long_squares"], cf["short_squares"], cf["ramps"] = f1, f2, f3
        rec["failed"] = {"long_squares": bool(s1.get("failed_fx")), "short_squares": bool(s2.get("failed_fx")),
                         "ramps": bool(s3.get("failed_fx"))}
        rec["features"] = pack({k: (v if not rec["failed"][k] else None) for k, v in cf.items()})
        rec["extract_ok"] = 1
        # clock check on the most hyperpolarizing long square
        usable = []
        try:
            usable = [int(s) for s in ds.get_sweep_numbers(names["long_squares"], clamp_mode=cc)]
            best = None
            for sn in usable:
                sw = ds.sweep(sn)
                start, dur, amp, _s, _e = stf.get_stim_characteristics(sw.i, sw.t)
                if amp is not None and amp < 0 and (best is None or amp < best[0]):
                    best = (amp, sw, start, dur)
            if best is not None:
                amp, sw, start, dur = best
                t, v = sw.t, sw.v

                def m(a, b):
                    sel = (t >= a) & (t < b)
                    return float(np.nanmean(v[sel])) if sel.any() else np.nan
                rec["clock"] = {"amp": float(amp), "start": float(start), "dur": float(dur),
                                "pre": m(start - 0.01, start) - m(start - 0.1, start - 0.05),
                                "post": m(start + 0.015, start + 0.025) - m(start - 0.1, start - 0.05),
                                "dv": m(start + dur - 0.1, start + dur) - m(start - 0.1, start),
                                "fingerprint": hashlib.sha1(np.ascontiguousarray(v).tobytes()).hexdigest()}
                # one hash over the voltage traces of every usable long square, in sweep order
                hs = hashlib.sha1()
                for sn in sorted(usable):
                    hs.update(np.ascontiguousarray(ds.sweep(sn).v).tobytes())
                rec["clock"]["long_square_hash"] = hs.hexdigest()
        except Exception as exc:
            rec["clock_error"] = f"{type(exc).__name__}: {exc}"[:200]
        # split halves of the long squares (claim split-half-reliability)
        if split_seed is not None:
            rec["split"] = _split_half(ds, dsf, names, cc, usable, allowed, split_seed)
    except Exception as exc:
        rec["error"] = f"{type(exc).__name__}: {exc}"[:300]
    finally:
        # IPFX caches series with an lru_cache on a method, which keeps every data set alive
        try:
            from ipfx.dataset.ephys_nwb_data import EphysNWBData
            EphysNWBData._get_series.cache_clear()
        except Exception:
            pass
        import gc
        gc.collect()
    return rec


def _split_half(ds, dsf, names, cc, usable, allowed, seed):
    out = {"n_usable": len(usable), "ok": 0, "rule": "", "reason": "", "a": {}, "b": {}}
    allowed["set"] = None
    if len(usable) < MIN_USABLE:
        out["reason"] = f"n_usable={len(usable)}<{MIN_USABLE}"
        return out
    amp_map = {}
    try:
        tab = ds.filtered_sweep_table(clamp_mode=cc, stimuli=names["long_squares"])
        amp_map = {int(a): float(b) for a, b in zip(tab["sweep_number"], tab["stimulus_amplitude"])}
    except Exception:
        amp_map = {}
    splits = candidate_splits(usable, np.random.default_rng(seed), amp_map or None)
    if not splits:
        out["reason"] = "could_not_split"
        return out
    clsq = ds.filtered_sweep_table(clamp_mode=cc, stimuli=ds.ontology.coarse_long_square_names)
    try:
        if clsq is not None and len(clsq) > 0 and "stimulus_amplitude" in clsq:
            smin = dsf.select_subthreshold_min_amplitude(clsq["stimulus_amplitude"])[0]
        else:
            smin = -100
    except Exception as exc:
        out["reason"] = f"{type(exc).__name__}: {exc}"
        return out

    def half(sweeps):
        allowed["set"] = set(sweeps)
        try:
            feats, state = dsf.extract_cell_long_square_features(ds, subthresh_min_amp=smin)
        except Exception as exc:
            return None, f"{type(exc).__name__}"
        finally:
            allowed["set"] = None
        if (state or {}).get("failed_fx") or not feats:
            return None, str((state or {}).get("fail_fx_message") or "failed_fx")[:120]
        return pack({"long_squares": feats}), ""

    last = ""
    for a, b, rule in splits:
        fa, ea = half(a)
        fb, eb = half(b)
        if fa is not None and fb is not None:
            out.update(ok=1, rule=rule, a=fa, b=fb, reason="")
            return out
        last = ea or eb
    out["reason"] = last or "half_failed"
    return out


def _init():
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
    warnings.filterwarnings("ignore")
    logging.disable(logging.WARNING)


def extract_all(assets: list[dict], split_seed: int | None, workers: int = 6, chunk: int = 300,
                progress: int = 500) -> list[dict]:
    """Run ``extract_cell`` over the assets in forked processes, a fresh pool for every ``chunk`` files.

    At most ``workers`` files are in flight at once. A process that dies (killed for memory, say)
    breaks the pool; the files then in flight are run again in a new pool, and a file in flight at
    two such breaks is recorded as failed ("worker died")."""
    from concurrent.futures import FIRST_COMPLETED, wait
    from concurrent.futures.process import BrokenProcessPool
    done: dict[str, dict] = {}
    breaks: dict[str, int] = {}
    queue = list(assets)
    n_breaks = 0
    while queue:
        batch, queue = queue[:chunk], queue[chunk:]
        todo = list(batch)
        retry = []
        with ProcessPoolExecutor(max_workers=workers, initializer=_init, mp_context=mp.get_context("fork")) as ex:
            inflight = {}
            broken = False
            while (todo or inflight) and not broken:
                while todo and len(inflight) < workers:
                    a = todo.pop(0)
                    inflight[ex.submit(extract_cell, a, split_seed)] = a
                finished, _ = wait(list(inflight), return_when=FIRST_COMPLETED)
                for fut in finished:
                    a = inflight.pop(fut)
                    try:
                        done[a["path"]] = fut.result()
                    except BrokenProcessPool:
                        broken = True
                        retry.append(a)
                        continue
                    except Exception as exc:
                        done[a["path"]] = {"file_stem": a["path"].split("/")[-1].rsplit(".", 1)[0], "path": a["path"],
                                           "extract_ok": 0, "error": f"worker: {exc}"[:300], "features": {}}
                    if progress and len(done) % progress == 0:
                        print(f"  {len(done)}/{len(assets)} files", flush=True)
            if broken:
                retry += list(inflight.values())
                n_breaks += 1
        for a in retry:
            breaks[a["path"]] = breaks.get(a["path"], 0) + 1
            if breaks[a["path"]] >= 2:
                done[a["path"]] = {"file_stem": a["path"].split("/")[-1].rsplit(".", 1)[0], "path": a["path"],
                                   "extract_ok": 0, "error": "worker died", "features": {}}
        queue = [a for a in retry if a["path"] not in done] + todo + queue
    if n_breaks:
        print(f"  the pool broke {n_breaks} times; files in flight were run again", flush=True)
    return [done[a["path"]] for a in assets]
