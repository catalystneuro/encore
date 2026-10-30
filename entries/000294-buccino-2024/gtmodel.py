"""The paper's code repository, pinned at a commit, and simulations of its released ground-truth
model (hay_ais) for the claims on data elsewhere (Buccino et al. 2024, Neural Computation).

The repository github.com/alejoe91/multimodalfitting at commit
24e8e6168b2d5be45c551bcc08b62fde187d01c7 is fetched as an archive into a temporary directory (code,
model files, morphologies, extracted feature files and the ground-truth template); its NEURON
mechanisms are compiled there with `nrnivmodl`.

The model is instantiated with the repository's own `create_ground_truth_model(model_name="hay_ais",
release=True)`, with BluePyOpt's NEURON simulator (`model_type="neuron"`). The paper's notebooks use
the LFPy-based simulator of BluePyOpt 1.13.88, whose interface the locked environment does not
provide (deviation); the intracellular dynamics are the same NEURON model.

Where the parameters come from:

- Rheobase steps: 270 ms steps after a 250 ms delay (`compute_rheobase_for_model` defaults; Results
  3.2: "estimated using a 270 ms step"), from 0.15 nA by 0.005 nA (the ground-truth notebook
  1-generate-ecode-protocols-and-features-hay_ais.ipynb, `rheobase_compute_params["hay_ais"]`);
  a series from 0.10 nA is a variant, to see whether a lower step also fires.
- Spike counts: eFEL `Spikecount` at -20 mV (the code's eFEL threshold).
- IDrest 300%: the protocol of protocols_BPO_all.json (delay 250 ms, 1350 ms step of 0.45 nA, total
  1841.7 ms), as in 7-AIS-test.ipynb; recordings at the soma and at the middle (x = 0.5) and end
  (x = 1) of the AIS section (`utils.get_ais_extra_recordings`: ais_mid_v, ais_end_v); spike cut-outs
  3 ms before and 10 ms after each somatic peak, first and last spikes left out, averaged
  (`utils.get_peak_cutout`, 7-AIS-test.ipynb ms_before=3, ms_after=10).
- AIS position for Figure 3A: LFPy places the cell with the midpoint of its soma at the origin
  (LFPy `Cell.set_pos`), so positions are taken relative to the mean of the soma's 3D points
  (an approximation of LFPy's soma midpoint, standard choice).
"""

from __future__ import annotations

import io
import json
import subprocess
import sys
import tarfile
import tempfile
import urllib.request
from pathlib import Path

import numpy as np

REPO = "alejoe91/multimodalfitting"
COMMIT = "24e8e6168b2d5be45c551bcc08b62fde187d01c7"
MODEL = "hay_ais"

RHEO_STEP_MIN, RHEO_STEP_INCREMENT, RHEO_STEP_MAX = 0.15, 0.005, 1.0   # nA, ground-truth notebook 1
RHEO_DELAY, RHEO_DURATION = 250.0, 270.0                               # ms
SPIKE_THRESHOLD = -20.0
CUT_BEFORE_MS, CUT_AFTER_MS = 3.0, 10.0                                # 7-AIS-test.ipynb

_state = {}


def fetch_repo() -> Path:
    """Download the repository at the pinned commit into a temporary directory (once)."""
    if "root" in _state:
        return _state["root"]
    url = f"https://github.com/{REPO}/archive/{COMMIT}.tar.gz"
    data = urllib.request.urlopen(url, timeout=120).read()
    tmp = Path(tempfile.mkdtemp(prefix="mmfit-"))
    with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as tar:
        tar.extractall(tmp, filter="data")
    root = next(tmp.iterdir())
    _state["root"] = root
    return root


def compile_mechanisms(model: str = MODEL) -> Path:
    root = fetch_repo()
    folder = root / "cell_models" / model
    nrnivmodl = Path(sys.executable).parent / "nrnivmodl"
    r = subprocess.run([str(nrnivmodl), "mechanisms"], cwd=folder, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(r.stdout[-2000:] + r.stderr[-2000:])
    return folder


def package():
    """Import the repository's package (multimodalfitting) from the fetched code."""
    root = fetch_repo()
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))
    import multimodalfitting as mf
    return mf


def ground_truth_cell():
    """The released hay_ais model as a BluePyOpt CellModel, and a NEURON simulator."""
    if "cell" in _state:
        return _state["cell"], _state["sim"]
    folder = compile_mechanisms(MODEL)
    mf = package()
    import bluepyopt.ephys as ephys
    cell = mf.create_ground_truth_model(model_name=MODEL, release=True, model_type="neuron")
    sim = ephys.simulators.NrnSimulator(cvode_active=True, mechanisms_directory=str(folder))
    _state["cell"], _state["sim"] = cell, sim
    return cell, sim


def _soma_location():
    import bluepyopt.ephys as ephys
    return ephys.locations.NrnSeclistCompLocation(name="soma", seclist_name="somatic", sec_index=0, comp_x=0.5)


def run_step(amp_na: float, delay: float, duration: float, total: float, ais: bool = False) -> dict:
    """Simulate a square current step at the soma; return {name: (time ms, voltage mV)}."""
    import bluepyopt.ephys as ephys
    cell, sim = ground_truth_cell()
    soma = _soma_location()
    recs = [ephys.recordings.CompRecording(name="soma.v", location=soma, variable="v")]
    if ais:
        for name, x in (("ais_mid_v", 0.5), ("ais_end_v", 1.0)):
            loc = ephys.locations.NrnSeclistCompLocation(name=name, seclist_name="axon_initial_segment",
                                                         sec_index=0, comp_x=x)
            recs.append(ephys.recordings.CompRecording(name=f"{name}.v", location=loc, variable="v"))
    stim = ephys.stimuli.NrnSquarePulse(step_amplitude=amp_na, step_delay=delay, step_duration=duration,
                                        location=soma, total_duration=total)
    protocol = ephys.protocols.SweepProtocol(f"step_{amp_na:.4f}", [stim], recs)
    resp = protocol.run(cell_model=cell, param_values={}, sim=sim, isolate=False)
    return {k: (np.asarray(v["time"]), np.asarray(v["voltage"])) for k, v in resp.items()}


def spike_count(t, v, start, end) -> int:
    import efel
    efel.set_setting("Threshold", SPIKE_THRESHOLD)
    tr = {"T": t, "V": v, "stim_start": [start], "stim_end": [end]}
    return int(efel.get_feature_values([tr], ["Spikecount"])[0]["Spikecount"][0])


def peak_times(t, v) -> np.ndarray:
    import efel
    efel.set_setting("Threshold", SPIKE_THRESHOLD)
    tr = {"T": t, "V": v, "stim_start": [t[0]], "stim_end": [t[-1]]}
    pk = efel.get_feature_values([tr], ["peak_time"])[0]["peak_time"]
    return np.array([]) if pk is None else np.asarray(pk)


def rheobase(step_min=RHEO_STEP_MIN, step_inc=RHEO_STEP_INCREMENT, step_max=RHEO_STEP_MAX):
    """Spike counts for each step of the series, stopping at the first that fires (as the code)."""
    rows = []
    for amp in np.arange(step_min, step_max + 1e-3, step_inc):
        r = run_step(float(amp), RHEO_DELAY, RHEO_DURATION, 2 * RHEO_DELAY + RHEO_DURATION)
        t, v = r["soma.v"]
        n = spike_count(t, v, RHEO_DELAY, RHEO_DELAY + RHEO_DURATION)
        rows.append((round(float(amp), 4), n))
        if n > 0:
            break
    return rows


def protocol_json(model: str = MODEL, strategy: str = "all") -> dict:
    root = fetch_repo()
    return json.loads((root / "cell_models" / model / "fitting" / "efeatures" /
                       f"protocols_BPO_{strategy}.json").read_text())


def features_json(model: str = MODEL, name: str = "features_BPO_all.json") -> dict:
    root = fetch_repo()
    return json.loads((root / "cell_models" / model / "fitting" / "efeatures" / name).read_text())


def averaged_cutouts(resp: dict, before=CUT_BEFORE_MS, after=CUT_AFTER_MS):
    """Average of the cut-outs around somatic peaks, first and last left out (utils.get_peak_cutout).
    Each trace is interpolated on a common 0.01 ms grid relative to the peak."""
    t, v = resp["soma.v"]
    pk = peak_times(t, v)[1:-1]
    grid = np.arange(-before, after, 0.01)
    out = {}
    for name, (tt, vv) in resp.items():
        out[name] = np.mean([np.interp(p + grid, tt, vv) for p in pk], axis=0)
    return grid, out, len(pk)


def section_points(cell_name_filter=None):
    """3D points of every section of the instantiated model: {section name: array (n, 3)}."""
    from neuron import h
    cell, sim = ground_truth_cell()
    cell.instantiate(sim=sim)
    pts = {}
    for sec in h.allsec():
        pts[sec.name()] = np.array([[sec.x3d(i), sec.y3d(i), sec.z3d(i)] for i in range(sec.n3d())])
    cell.destroy(sim=sim)
    return pts


def read_swc(path: Path) -> np.ndarray:
    return np.loadtxt(path)
