"""Helpers for testing Kutschireiter, Basnak, Wilson & Drugowitsch (2023), "Bayesian inference in
ring attractor networks" (PNAS 120, e2210622120), with dandiset 000289.

The paper holds no recorded data. Its simulation claims are tested on the paper's own code and
processed outputs (Zenodo doi:10.5281/zenodo.7615975, BayesianRingAttractor v1.0, commit a9db6f9),
its connectome claim on the hemibrain connectome, and its one prediction about cue reliability on
the imaging data of dandiset 000289. Every source is read into memory; nothing is written to disk.

Where each parameter comes from:
- The claims file (claims/000289/10.1073-pnas.2210622120.yaml) gives every criterion: the
  information rates, the readings for unquantified words, the network parameters of the noise test,
  the decoder for bump amplitude.
- The paper's code fixes the rest: the objective() weighting (mean 0.5, SD 1 over log rate), the
  particle-filter reference, the Figure 2H simulation (run from the released notebook's own cells).
- Two patches are needed to run the released code, both named in the claims file's header:
  RNN_filter_Run gets a `z=None` argument (it uses z but has no such parameter), and the notebook
  Figure2h.ipynb calls vM_Projection_Run with `kappa_y=`, which the function names `kappa_v`.
- Standard choices that set only precision or speed are marked as such where they are made.
"""
import hashlib
import io
import json
import re
import tarfile
import types
import zipfile

import numpy as np
import requests
from scipy.stats import norm

# ---------------------------------------------------------------------------------------------
# Pinned sources
DANDISET = "000289"
VERSION = "0.240801.1040"  # the only published version (2024-08-01); see the notebook header
DANDI_API = "https://api.dandiarchive.org/api"

ZENODO_URL = ("https://zenodo.org/api/records/7615975/files/"
              "DrugowitschLab/BayesianRingAttractor-v1.0.zip/content")
ZENODO_MD5 = "c3f0574b98eef0c6c67d139f0d20a1ae"
CODE_ROOT = "DrugowitschLab-BayesianRingAttractor-a9db6f9/"

# Public export of the hemibrain v1.2 connectome (Scheffer et al. 2020), traced neurons and total
# synapse counts per pair. neuPrint, which serves v1.2.1, now needs a personal token for all data.
HEMIBRAIN_URL = "https://storage.googleapis.com/hemibrain/v1.2/exported-traced-adjacencies-v1.2.tar.gz"
HEMIBRAIN_MD5 = "ec1e076d15442f368fa5978b00f4a61c"

# Information rates of every scan (performance_scan_figure2i.py and the figure notebooks)
RATES = np.array([0.01, 0.03, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 2, 3, 4, 5, 6, 7, 8,
                  9, 10, 30, 100])
# kappa* grid of the fixed-certainty filter (Figure3b,c,e,d_FigureS3.ipynb)
KAPPA_FIXED = np.array([0.1, 0.3, 0.9, 1., 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2., 2.1, 2.2,
                        2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3., 4., 5., 6., 7., 8., 9., 10., 30., 100.])
# Figure 3D grid (same notebook)
KSTAR_3D = np.round(np.arange(1, 26) * 0.1, 1)
BETA_GRID = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 2, 4, 8])
# Figure 3F grid (Figure3f_FigureS4.ipynb)
KSTAR_3F = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6,
                     1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.2, 3.4,
                     3.6, 3.8, 4.0, 4.2, 4.4, 4.6, 4.8, 5.0])
SIGMAS_3F = np.array([0., 1., 2., 3., 4., 5., 6., 7., 8., 9., 10., 15, 20])
N_3F = 64
REF_PF_3F = 0.6912447327304075  # Figure3f_FigureS4.ipynb, "performance of particle filter as reference"
N_S2 = np.array([3, 4, 8, 16, 32, 64, 128])  # FigureS2.ipynb, N_array


def _get(url, md5):
    data = requests.get(url, timeout=600).content
    got = hashlib.md5(data).hexdigest()
    if got != md5:
        raise ValueError(f"{url}: md5 {got}, expected {md5}")
    return data


# ---------------------------------------------------------------------------------------------
# The paper's code and processed outputs
class Code:
    """The Zenodo deposit, held in memory."""

    def __init__(self):
        self.zip = zipfile.ZipFile(io.BytesIO(_get(ZENODO_URL, ZENODO_MD5)))
        self.names = [n[len(CODE_ROOT):] for n in self.zip.namelist() if n.startswith(CODE_ROOT)]
        self.patches = []
        self.flt = self._module()

    def read(self, name):
        return self.zip.read(CODE_ROOT + name)

    def npz(self, name):
        return np.load(io.BytesIO(self.read("data_processed/" + name)))

    def notebook_cells(self, name):
        nb = json.loads(self.read(name))
        return ["".join(c["source"]) for c in nb["cells"] if c["cell_type"] == "code"]

    def _module(self):
        src = self.read("circularFiltering.py").decode()
        old = "I_ext=0,stoch_corr=0,dy=None"
        assert src.count(old) == 1
        src = src.replace(old, "I_ext=0,stoch_corr=0,z=None,dy=None")
        self.patches.append("RNN_filter_Run: added z=None to the signature (it uses z and has no such "
                            "parameter; claims file header)")
        # numpy 2 moved numpy.core.numeric; isscalar is the same function at the top level
        src = src.replace("from numpy.core.numeric import isscalar", "from numpy import isscalar")
        self.patches.append("import of isscalar from numpy, not numpy.core.numeric (numpy 2)")
        mod = types.ModuleType("circularFiltering")
        exec(compile(src, "circularFiltering.py", "exec"), mod.__dict__)
        return mod


def objective(values, mu=0.5, sigma=1.0, rates=RATES):
    """Prior-weighted average over log rate, trapezoidal rule; objective() of the figure notebooks
    with mu_perf = 0.5 and sig_perf = 1 (Methods, Performance measures; claims file)."""
    x = np.log(rates)
    f = np.asarray(values) * norm.pdf(x, loc=mu, scale=sigma)
    return np.sum(0.5 * (f[1:] + f[:-1]) * np.diff(x))


# ---------------------------------------------------------------------------------------------
# Figure 2H: run the released notebook's own cells
def run_figure2h(code, rate=15):
    """Executes the simulation cells of Figure2h.ipynb (seed 42, T = 15, N = 80, cue off from 5 to
    10 s). `rate` replaces the notebook's information rate of 15 (the Methods say 10/s; claims
    file). The only other change is the keyword kappa_y -> kappa_v (claims file header)."""
    cells = code.notebook_cells("Figure2h.ipynb")
    sim = [c for c in cells if "np.random.seed(42)" in c][0]
    assert "kappa_z = 15 " in sim
    sim = sim.replace("kappa_z = 15 ", f"kappa_z = {rate} ")
    kf = [c for c in cells if "vM_Projection_Run" in c][0].replace("kappa_y=kappa_v", "kappa_v=kappa_v")
    net = [c for c in cells if "Single population network" in c][0]
    ns = {"np": np, "flt": code.flt}
    for c in (sim, kf, net):
        exec(c, ns)
    return ns


def circ_diff(a, b):
    return np.angle(np.exp(1j * (np.asarray(a) - np.asarray(b))))


# ---------------------------------------------------------------------------------------------
# Neural noise: a batched copy of RNN_filter_Run, checked against it in the notebook
def rnn_batch(rng, runs, T, N, sigma_N, w_even, w_quad, tau=1.0, kappa_0=1.0, phi_0=0.0, dt=0.01,
              noise=None):
    """RNN_filter_Run (circularFiltering.py) for `runs` independent runs at once, with no angular
    velocity input (w_odd = 0, dy = 0), no HD input (I_ext = 0) and stoch_corr = 0 (claims file).
    Same update, term by term: decay, even recurrence (2/N w_even cos), quadratic inhibition
    (pi/N sum of rectified rates), additive noise sigma_N sqrt(dt) N(0,1). `noise` may pass the
    standard normal draws (steps x runs x N) to reproduce a given run."""
    steps = int(T / dt)
    phi_r = np.linspace(-np.pi, np.pi - 2 * np.pi / N, N)
    W = 2 / N * w_even * np.cos(phi_r[:, None] - phi_r[None, :])
    A = np.array([np.cos(phi_r), np.sin(phi_r)])
    r = np.tile(kappa_0 * np.cos(phi_r - phi_0), (runs, 1))
    mu = np.zeros((steps, runs))
    kappa = np.zeros((steps, runs))

    def decode(r):
        th = 2 / N * r @ A.T
        return np.arctan2(th[:, 1], th[:, 0]), np.hypot(th[:, 0], th[:, 1])

    mu[0], kappa[0] = decode(r)
    for i in range(1, steps):
        inh = w_quad * (np.pi / N) * np.maximum(r, 0).sum(1, keepdims=True)
        dW = (noise[i] if noise is not None else rng.standard_normal((runs, N))) * np.sqrt(dt)
        r = r - r / tau * dt + (r @ W.T) * dt - inh * r * dt + sigma_N * dW
        mu[i], kappa[i] = decode(r)
    return mu, kappa


# ---------------------------------------------------------------------------------------------
# Hemibrain connectome
def hemibrain():
    """Traced neurons (bodyId, type, instance) and total synapse counts per pair, hemibrain v1.2."""
    import pandas as pd
    tf = tarfile.open(fileobj=io.BytesIO(_get(HEMIBRAIN_URL, HEMIBRAIN_MD5)), mode="r:gz")
    base = "exported-traced-adjacencies-v1.2/"
    neurons = pd.read_csv(tf.extractfile(base + "traced-neurons.csv"))
    conns = pd.read_csv(tf.extractfile(base + "traced-total-connections.csv"))
    return neurons, conns


# Reading (a) of the sort: the PB glomerulus in the instance name, L9 to R9 (claims file)
PB_ORDER = [f"L{k}" for k in range(9, 0, -1)] + [f"R{k}" for k in range(1, 10)]


def pb_glomerulus(instance):
    m = re.search(r"_([LR][1-9])$", instance)
    return m.group(1) if m else None


# ---------------------------------------------------------------------------------------------
# Dandiset 000289
def assets():
    url = f"{DANDI_API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=1000"
    out = []
    while url:
        d = requests.get(url, timeout=120).json()
        out += d["results"]
        url = d.get("next")
    return out


def open_nwb(asset):
    """Streams one NWB file with remfile and h5py (no download)."""
    import h5py
    import remfile
    url = f"{DANDI_API}/assets/{asset['asset_id']}/download/"
    return h5py.File(remfile.File(url), "r")


def read_session(f):
    """dF/F per PB midline ROI, the cue position, the trials table, and metadata."""
    rrs = f["processing/ophys/Fluorescence/RoiResponseSeries"]
    pos = f["processing/behavior/Position/SpatialSeries"]
    out = {
        "description": f["session_description"][()].decode(),
        "subject": f["general/subject/subject_id"][()].decode(),
        "rate_meta": float(f["general/optophysiology/imaging_plane/imaging_rate"][()]),
        "dff": rrs["data"][:],
        "t": rrs["timestamps"][:],
        "cue": pos["data"][:],
        "t_cue": pos["timestamps"][:],
        "cue_unit": pos["data"].attrs.get("unit"),
        "tps_shape": f["acquisition/TwoPhotonSeries/data"].shape,
        "t_tps": f["acquisition/TwoPhotonSeries/timestamps"][:],
        "masks": f["processing/ophys/ImageSegmentation/PlaneSegmentation/image_mask"][:],
    }
    if "trials" in f["intervals"]:
        tr = f["intervals/trials"]
        out["trials"] = {k: tr[k][:] for k in tr.keys() if k != "id"}
        out["trial_desc"] = {k: tr[k].attrs.get("description") for k in tr.keys() if k != "id"}
    return out


def fourier(act, k=2):
    """Population vector of the activity at spatial frequency k across the ROIs, ordered along the
    PB midline (k = 2: the two copies of the bump across the bridge; the frequency is checked in the
    notebook as the peak of the spatial spectrum). Each ROI's preferred HD is 2 pi k j / n, the
    decoder A = (cos phi, sin phi) of the Methods, scaled by 2/n as in the paper's code (Figure2h:
    theta = 2/N A r). Returns (phase, amplitude) per frame."""
    n = act.shape[1]
    ph = 2 * np.pi * k * np.arange(n) / n
    z = 2 / n * act @ np.exp(-1j * ph)
    return np.angle(z), np.abs(z)


def spectrum(act):
    a = act - act.mean(1, keepdims=True)
    return np.abs(np.fft.rfft(a, axis=1)).mean(0)


def raw_roi_fluorescence(f, frames, masks, projection="mean", smooth=4.0):
    """Raw fluorescence per ROI from the TwoPhotonSeries for the given frame blocks: the volume is
    projected over planes (`projection`), smoothed in the plane with a Gaussian of SD `smooth`
    pixels, and averaged over each ROI's 2D mask (5 to 9 pixels on the PB midline). Neither the
    projection nor the extent of an ROI is stated in the files; the notebook picks them by agreement
    with the stored dF/F, and shows the alternatives."""
    from scipy.ndimage import gaussian_filter
    d = f["acquisition/TwoPhotonSeries/data"]
    m = masks.reshape(masks.shape[0], -1).astype(float)
    m /= m.sum(1, keepdims=True)
    out = []
    for a, b in frames:
        v = d[a:b].astype(np.float32)
        p = v.mean(1) if projection == "mean" else v.max(1)
        if smooth:
            p = gaussian_filter(p, (0, smooth, smooth))
        out.append(p.reshape(p.shape[0], -1) @ m.T)
    return np.concatenate(out)
