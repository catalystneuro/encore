"""The paper's code repository, pinned at a commit, and simulations of its released ground-truth
model (hay_ais) for the claims on data elsewhere (Buccino et al. 2024, Neural Computation).

The repository github.com/alejoe91/multimodalfitting at commit
24e8e6168b2d5be45c551bcc08b62fde187d01c7 is fetched as an archive into a temporary directory (code,
model files, morphologies, extracted feature files and the ground-truth template); its NEURON
mechanisms are compiled there with `nrnivmodl`.

The model is instantiated with the repository's own `create_ground_truth_model(model_name="hay_ais",
release=True)`, with BluePyOpt's NEURON simulator (`model_type="neuron"`) for the rheobase and the
fixed-step AIS check, and with BluePyOpt's LFPy simulator (`LFPyCellModel`, `LFPySimulator`, as the
paper's notebooks) for the code's own AIS cut-outs, the extracellular template and the evaluators.
The paper's notebooks use BluePyOpt 1.13.88; the locked environment has BluePyOpt 1.14.26, whose
`LFPySimulator` takes the electrode from the cell model in place of a constructor argument. The
intracellular dynamics are the same NEURON model under both simulators.

Where the parameters come from:

- Rheobase steps: 270 ms steps after a 250 ms delay (`compute_rheobase_for_model` defaults; Results
  3.2: "estimated using a 270 ms step"), from 0.15 nA by 0.005 nA (the ground-truth notebook
  1-generate-ecode-protocols-and-features-hay_ais.ipynb, `rheobase_compute_params["hay_ais"]`);
  a series from 0.10 nA is a variant, to see whether a lower step also fires.
- Spike counts: eFEL `Spikecount` at -20 mV (the code's eFEL threshold) for the rheobase steps,
  which have no spike outside the step; eFEL `peak_time` at -20 mV counted within a window
  elsewhere.
- IDrest 300%: the protocol of protocols_BPO_all.json (delay 250 ms, 1350 ms step of 0.45 nA, total
  1841.7 ms), as in 7-AIS-test.ipynb; recordings at the soma and at the middle (x = 0.5) and end
  (x = 1) of the AIS section (`utils.get_ais_extra_recordings`: ais_mid_v, ais_end_v); spike cut-outs
  3 ms before and 10 ms after each somatic peak, first and last spikes left out, averaged
  (`utils.get_peak_cutout`, 7-AIS-test.ipynb ms_before=3, ms_after=10). These cut-outs interpolate every trace on a 20 kHz grid
  (0.05 ms) and cut on that grid; `code_idrest300` and `code_cutouts` run them as 7-AIS-test.ipynb
  does (`define_protocols` with `protocols_with_lfp=["IDrest_300"]` and the AIS recordings).
  A fixed-step NEURON run (dt 0.005 ms, cvode off) times each spike directly, as a check of the
  ordering below the code's 0.05 ms grid (standard choice of step).
- AIS position for Figure 3A: read from the instantiated `LFPyCellModel` (`lfpy_cell` segment
  midpoints), the frame in which the template is simulated; LFPy's `Cell` puts the soma midpoint at
  the origin. The probe is the code's `define_electrode(probe_type="planar")` (20 by 4 at 50 um,
  z = 20 um), as in 1-generate-ecode-protocols-and-features-hay_ais.ipynb, and the template is
  recomputed with `utils.calculate_eap` and `get_extra_kwargs()` on IDrest 300%.
- Evaluators: the code's `create_evaluator` for each strategy (`protocols_with_lfp=["IDrest_300"]`
  for the extracellular ones, run_optimizations.py) and, for validation, `all_protocols=True`
  without IV, APWaveform and IDrest, with LFP on firepattern 120% (4-optimization-performance.ipynb).
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
    """Compile the model's mechanisms; returns the folder as a Path, the type the code's
    create_evaluator passes, since NEURON's load_mechanisms tells loaded folders apart by equality and
    a str and a Path of one folder would load the mechanisms twice."""
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
    sim = ephys.simulators.NrnSimulator(cvode_active=True, mechanisms_directory=folder)
    _state["cell"], _state["sim"] = cell, sim
    return cell, sim


def _soma_location():
    import bluepyopt.ephys as ephys
    return ephys.locations.NrnSeclistCompLocation(name="soma", seclist_name="somatic", sec_index=0, comp_x=0.5)


def fixed_step_simulator(dt: float):
    """A NEURON simulator with a fixed time step (cvode off)."""
    import bluepyopt.ephys as ephys
    ground_truth_cell()
    sim = ephys.simulators.NrnSimulator(dt=dt, cvode_active=False,
                                        mechanisms_directory=compile_mechanisms(MODEL))
    sim.neuron.h.dt = dt   # the NrnSimulator checks that h.dt is the step it was created with
    return sim


def run_step(amp_na: float, delay: float, duration: float, total: float, ais: bool = False, sim=None) -> dict:
    """Simulate a square current step at the soma; return {name: (time ms, voltage mV)}."""
    import bluepyopt.ephys as ephys
    cell, default_sim = ground_truth_cell()
    sim = default_sim if sim is None else sim
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


def per_spike_timing(resp: dict, names=("ais_end_v.v", "ais_mid_v.v", "soma.v"), before=3.0, after=1.0):
    """For each somatic spike but the first and last: the -20 mV crossing (linear between samples) and
    the peak time of each trace, in ms relative to the somatic peak. Returns an array
    (spikes, 2 * len(names)): crossings, then peaks."""
    t, v = resp["soma.v"]
    rows = []
    for p in peak_times(t, v)[1:-1]:
        cross, peak = [], []
        for name in names:
            tt, vv = resp[name]
            w = (tt > p - before) & (tt < p + after)
            tt, vv = tt[w], vv[w]
            k = int(np.where(vv >= SPIKE_THRESHOLD)[0][0])
            cross.append(tt[k - 1] + (SPIKE_THRESHOLD - vv[k - 1]) / (vv[k] - vv[k - 1]) * (tt[k] - tt[k - 1]) - p)
            peak.append(tt[np.argmax(vv)] - p)
        rows.append(cross + peak)
    return np.array(rows)


# --- LFPy simulator, as the paper's notebooks ---------------------------------------------------

def probe():
    """The code's planar probe (define_electrode(probe_type="planar")), as notebook 1 builds it."""
    mf = package()
    return mf.define_electrode(probe_type="planar")


def lfpy_cell(electrode=None):
    """The released hay_ais model as an LFPyCellModel with the given probe, and an LFPy simulator."""
    import bluepyopt.ephys as ephys
    folder = compile_mechanisms(MODEL)
    mf = package()
    cell = mf.create_ground_truth_model(model_name=MODEL, release=True, electrode=electrode)
    sim = ephys.simulators.LFPySimulator(cvode_active=True, mechanisms_directory=folder)
    return cell, sim


def lfpy_segment_midpoints() -> dict:
    """Segment midpoints (x, y, z, um) of the instantiated LFPyCellModel, by section type
    ('soma', 'ais', ...), in the frame where LFPy simulates the extracellular signals."""
    cell, sim = lfpy_cell(probe())
    cell.instantiate(sim=sim)
    lc = cell.lfpy_cell
    names = [lc.get_idx_name(i)[1].split(".")[-1].split("[")[0] for i in range(lc.totnsegs)]
    mids = np.c_[lc.x.mean(axis=1), lc.y.mean(axis=1), lc.z.mean(axis=1)]
    out = {n: mids[[k for k, m in enumerate(names) if m == n]] for n in dict.fromkeys(names)}
    out["_somapos"] = np.asarray(lc.somapos, float)
    cell.destroy(sim=sim)
    return out


def code_idrest300(electrode=None, ais: bool = True):
    """IDrest 300% run as 7-AIS-test.ipynb runs it: the repository's protocols_BPO_all.json through
    define_protocols, LFP on IDrest_300 and the AIS recordings, on the LFPy cell model."""
    mf = package()
    electrode = probe() if electrode is None else electrode
    eff = fetch_repo() / "cell_models" / MODEL / "fitting" / "efeatures"
    extra = {"IDrest_300": mf.utils.get_ais_extra_recordings()} if ais else None
    prots = mf.define_protocols(MODEL, feature_file=eff / "features_BPO_all.json",
                                protocols_file=eff / "protocols_BPO_all.json", electrode=electrode,
                                protocols_with_lfp=["IDrest_300"], extra_recordings=extra)
    cell, sim = lfpy_cell(electrode)
    resp = prots["IDrest_300"].run(cell, {}, sim=sim, isolate=False)
    return resp, prots


def code_cutouts(resp):
    """The code's averaged cut-outs (utils.get_peak_cutout, 3 ms before and 10 ms after,
    7-AIS-test.ipynb): {name: (time ms from the cut-out start, voltage mV)} on its 20 kHz grid."""
    mf = package()
    cut = mf.utils.get_peak_cutout(resp, ms_before=CUT_BEFORE_MS, ms_after=CUT_AFTER_MS, average=True)
    return {k.split(".", 1)[1]: (np.asarray(r["time"]), np.asarray(r["voltage"]))
            for k, r in cut.items() if "voltage" in r}


def template(resp, prots):
    """The extracellular template of IDrest 300% by the code's calculate_eap and extra kwargs."""
    mf = package()
    return mf.utils.calculate_eap(resp, "IDrest_300", prots, **mf.utils.get_extra_kwargs())


def evaluator(strategy: str, validation: bool = False):
    """The code's create_evaluator for a strategy (run_optimizations.py), or the validation evaluator
    of 4-optimization-performance.ipynb."""
    mf = package()
    compile_mechanisms(MODEL)
    kw = mf.utils.get_extra_kwargs()
    if validation:
        return mf.create_evaluator(model_name=MODEL, strategy="all", protocols_with_lfp="firepattern_120",
                                   all_protocols=True, exclude_protocols=["IV", "APWaveform", "IDrest"], **kw)
    lfp = None if strategy == "soma" else ["IDrest_300"]
    return mf.create_evaluator(model_name=MODEL, strategy=strategy, protocols_with_lfp=lfp, **kw)


def release_params(param_names) -> dict:
    mf = package()
    cell = mf.create_ground_truth_model(model_name=MODEL, release=True)
    return {p.name: p.value for p in cell.params_by_names(param_names)}
