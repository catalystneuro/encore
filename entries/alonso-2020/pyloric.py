"""Loading, simulation and measures for the temperature-compensated pyloric networks of Dryad m31b1h7.

Alonso & Marder (2020), "Temperature compensation in a small rhythmic circuit", eLife 9:e55470,
doi:10.7554/eLife.55470. The dataset (doi:10.5061/dryad.m31b1h7, version id 94811, the only
published version) is one zip, alonso_marder_tempcomp_2019_root.zip, holding the authors' Java model,
their Python driver scripts, one initial-condition file (cis_network.txt) and one parameter file per
model (p-<NAME>.score.<score>.txt, 132 numbers each). Dryad needs a token to download, so the
workflow stages the file under /tmp/dryad/m31b1h7/94811/ before the run (docs/archives.md, "Dryad");
it is read there in place, into memory, and checked against the MD5 that Dryad's file list gives.

Where things come from:

- The model is a line-by-line port of the deposited Java classes
  PrinzNetworkWithTemperature_full_eu_slow_same_q10s_rk4.java (network, synapses, Q10 of the
  synapses), singleCompTemperature_slow_explicit.java (each cell) and Integrador.java (RK4), into
  numba. Parameter layout, per cell 37 numbers: 8 maximal conductances (Na, CaT, CaS, A, KCa, Kd, H,
  leak), EL, ENa, EK, EH, 23 Q10 values (indices 12 to 34), tau_Ca / 10 (index 35), injected
  current (36); then 7 synaptic conductances and 14 synaptic Q10 values, of which the Java uses
  0 (glutamatergic g), 1 (cholinergic g), 7 (glutamatergic tau) and 8 (cholinergic tau). As in the
  Java, the Q10 values of the PD (first) cell are used for all three cells. Choices kept from the
  Java: C = 10, area 0.628, caF 0.94, Ca0 0.05 uM, [Ca]out 3000 uM, synaptic bound 20 ms,
  Vth = -35 mV, Delta = 5 mV, Eglut = -70 mV, Echol = -80 mV, k = 1/40 and 1/100 per ms.
- dt = 0.05 ms and RK4 (Materials and methods, The model, last paragraph; the Java drivers' dt
  argument). Initial state cis_network.txt (V = -51 mV, gates 0, [Ca] = 5 uM, synapses 0), as the
  Methods say.
- Temperature ramps: the deposit holds no ramp code. The temperature changes linearly in time
  and the temperature factors are updated every 20 steps (1 ms), at the temperature of the middle
  of those 20 steps (an assumption; the Results give only the start, end and duration of a ramp;
  over 1 ms a 60 min ramp moves by less than 1e-5 degrees C).
- Spike times: the paper and the deposit give no spike detection rule. A spike is an upward
  crossing of SPIKE_THRESHOLD = -20 mV (an assumption, the standard choice for these models,
  whose slow waves stay below the -50 mV slow-wave threshold of the Methods). The main notebook
  repeats the runs at 10 and 25 C, the graded removals of fig10a-graded-removal and FGFKQS at 30 C
  with a 0 mV threshold, as a variant; the spikes of some cells peak below 0 mV, which that
  variant misses.
- Bursts and the classification scheme: Materials and methods, "Classification scheme": spiking
  when CV of ISI < 0.1 (tonic when the lag d between spike onset and the -50 mV slow-wave crossing
  is under 20 ms, else single-spike bursting); otherwise spikes grouped into bursts with a 200 ms
  gap; regular bursting when CV(dc) < 1, CV(fb) < 0.1 and mean(dc) > 0; irregular bursting when
  mean(dc) > 0 and CV(dc) > 1 or CV(fb) > 0.1; irregular spiking when mean(dc) = 0; quiescent when
  there is no more than 1 ISI. Duty cycle is burst duration over period (Results, Duty cycle and
  phase maintenance). The lag d is taken as the median over spikes of the time from the last
  upward crossing of -50 mV to the spike (an assumption: the Methods do not say how d is formed).
  The classes are computed over the analysed window only.
- Triphasic (Classification scheme): the three cells' burst frequencies within 5% and the cells
  firing in the right order. The order is read as LP bursts starting before PY bursts within the
  PD cycle: the median phase of LP onsets is below that of PY onsets, both in (0, 1) (an
  assumption; the paper does not say how order is tested). `triphasic(..., strict=True)` asks it
  of every cycle, a variant.
- Currents (for currentscapes): the deposit's getCurrents.py computes the eight intrinsic currents
  as g m^q h (V - E) times the area; the synaptic current into each cell is the sum of its
  synapses' currents (as integratePyloricSQ10s_currentscapes_RK4_mp.py adds them). Shares follow
  plotCurrentScape in plotPyloricTempUtils.py: positive currents (outward) over the sum of the
  positive ones, negative (inward) over the sum of the negative ones.
"""

from __future__ import annotations

import hashlib
import io
import re
import zipfile
from pathlib import Path

import numpy as np
from numba import njit

DRYAD_ID = "m31b1h7"
DRYAD_VERSION = "94811"
DRYAD_DOI = "doi:10.5061/dryad.m31b1h7"
ZIP_NAME = "alonso_marder_tempcomp_2019_root.zip"
ZIP_MD5 = "37766522dabaaa620d4c44264e76e686"  # Dryad file list, https://datadryad.org/api/v2/versions/94811/files
STAGED = Path("/tmp") / "dryad" / DRYAD_ID / DRYAD_VERSION  # where the workflow stages the file
ROOT = "alonso_marder_tempcomp_2019_root/"

DT = 0.05                 # ms, Methods
SPIKE_THRESHOLD = -20.0   # mV, assumption (see module docstring)
SLOW_WAVE = -50.0         # mV, Methods
BURST_GAP = 0.2           # s, Methods, Classification scheme
CURRENTS = ["Na", "CaT", "CaS", "A", "KCa", "Kd", "H", "Leak"]
CELLS = ["PD", "LP", "PY"]


# --- loading ----------------------------------------------------------------------------------

def read_zip_bytes() -> bytes:
    return (STAGED / ZIP_NAME).read_bytes()


def digests(raw: bytes) -> dict:
    md5 = hashlib.md5(raw).hexdigest()
    if md5 != ZIP_MD5:
        raise ValueError(f"{ZIP_NAME}: MD5 {md5} differs from Dryad's file list ({ZIP_MD5})")
    return {"md5": md5, "sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw)}


def open_zip(raw: bytes) -> zipfile.ZipFile:
    return zipfile.ZipFile(io.BytesIO(raw))


def model_files(z: zipfile.ZipFile) -> dict:
    """Model name -> member name of its parameter file."""
    out = {}
    for n in z.namelist():
        m = re.match(re.escape(ROOT) + r"parameters_and_ci/p-([A-Z0-9]{6})\.score\.([0-9.]+)\.txt$", n)
        if m:
            out[m.group(1)] = n
    return dict(sorted(out.items()))


def read_vector(z: zipfile.ZipFile, member: str) -> np.ndarray:
    return np.array([float(s) for s in z.read(member).decode().split()])


def load_models(z: zipfile.ZipFile) -> dict:
    return {name: read_vector(z, member) for name, member in model_files(z).items()}


def load_ci(z: zipfile.ZipFile) -> np.ndarray:
    return read_vector(z, ROOT + "parameters_and_ci/cis_network.txt")


def score_of(member: str) -> float:
    return float(re.search(r"\.score\.([0-9.]+)\.txt$", member).group(1))


def conductances(p: np.ndarray) -> np.ndarray:
    """3 x 8 maximal conductances (PD, LP, PY; CURRENTS order)."""
    return np.array([p[37 * c:37 * c + 8] for c in range(3)])


def q10_conductances(p):
    return p[[12, 15, 18, 21, 24, 27, 30, 33]]


def q10_timescales(p):
    """Q10 values the Java uses for time scales: 11 gating variables and tau_Ca."""
    return p[[13, 14, 16, 17, 19, 20, 31, 28, 25, 22, 23, 34]]


def q10_synapses(p):
    return p[111 + 7 + np.array([0, 1, 7, 8])]


def scaled(p: np.ndarray, current: int, fraction: float) -> np.ndarray:
    """Copy of p with one intrinsic maximal conductance scaled in all three cells, as the deposit's
    integratePyloricSQ10s_remove_gA_onesteps_twotemps_RK4.py does."""
    q = p.copy()
    for c in range(3):
        q[37 * c + current] *= fraction
    return q


# --- the model (port of the deposited Java) ---------------------------------------------------

@njit(cache=True, error_model="numpy")
def _factors(p, T, f):
    x = (T - 10.0) / 10.0
    gi = (12, 15, 18, 21, 24, 27, 30, 33)
    for k in range(8):
        f[k] = p[gi[k]] ** x
    ti = (13, 14, 16, 17, 19, 20, 31, 28, 25, 22, 23, 34)
    for k in range(12):
        f[8 + k] = p[ti[k]] ** (-x)
    f[20] = p[118] ** x        # glutamatergic g
    f[21] = p[119] ** x        # cholinergic g
    f[22] = p[125] ** (-x)     # glutamatergic tau
    f[23] = p[126] ** (-x)     # cholinergic tau
    f[24] = T


@njit(cache=True, error_model="numpy")
def _boltz(V, A, B):
    return 1.0 / (1.0 + np.exp((V + A) / B))


@njit(cache=True, error_model="numpy")
def _taux(V, CT, DT_, AT, BT):
    return CT - DT_ / (1.0 + np.exp((V + AT) / BT))


@njit(cache=True, error_model="numpy")
def _spectau(V, CT, DT_, AT, BT, AT2, BT2):
    return CT + DT_ / (np.exp((V + AT) / BT) + np.exp((V + AT2) / BT2))


@njit(cache=True, error_model="numpy")
def _syn_ss(Vpre):
    return 1.0 / (1.0 + np.exp((-35.0 - Vpre) / 5.0))


@njit(cache=True, error_model="numpy")
def _cell_currents(y, o, p, po, f, out):
    """The eight intrinsic currents (nA, positive outward) of the cell with state offset o and
    parameter offset po."""
    V = y[o]
    T = f[24]
    caRev = ((8.314e3 * (273.15 + T)) / (2.0 * 96485.33)) * np.log(3000.0 / y[o + 12])
    A = 0.628
    out[0] = p[po + 0] * f[0] * y[o + 1] ** 3 * y[o + 2] * (V - p[po + 9]) * A
    out[1] = p[po + 1] * f[1] * y[o + 3] ** 3 * y[o + 4] * (V - caRev) * A
    out[2] = p[po + 2] * f[2] * y[o + 5] ** 3 * y[o + 6] * (V - caRev) * A
    out[3] = p[po + 3] * f[3] * y[o + 10] ** 3 * y[o + 11] * (V - p[po + 10]) * A
    out[4] = p[po + 4] * f[4] * y[o + 9] ** 4 * (V - p[po + 10]) * A
    out[5] = p[po + 5] * f[5] * y[o + 8] ** 4 * (V - p[po + 10]) * A
    out[6] = p[po + 6] * f[6] * y[o + 7] * (V - p[po + 11]) * A
    out[7] = p[po + 7] * f[7] * (V - p[po + 8]) * A


@njit(cache=True, error_model="numpy")
def _syn_currents(y, p, f, out):
    """Synaptic current into PD, LP and PY (nA, positive outward), as in the Java."""
    VAB, VLP, VPY = y[0], y[13], y[26]
    s = y[39:46]
    g = p[111:118]
    out[0] = f[20] * g[6] * s[6] * (VAB + 70.0)
    out[1] = (f[20] * g[2] * s[2] * (VLP + 70.0) + f[21] * g[3] * s[3] * (VLP + 80.0)
              + f[20] * g[5] * s[5] * (VLP + 70.0))
    out[2] = (f[20] * g[0] * s[0] * (VPY + 70.0) + f[21] * g[1] * s[1] * (VPY + 80.0)
              + f[20] * g[4] * s[4] * (VPY + 70.0))


@njit(cache=True, error_model="numpy")
def _rhs(y, p, f, dy, cur, syn):
    _syn_currents(y, p, f, syn)
    for c in range(3):
        o = 13 * c
        po = 37 * c
        V = y[o]
        _cell_currents(y, o, p, po, f, cur)
        iapp = -(p[po + 36] + syn[c])
        tot = 0.0
        for k in range(8):
            tot += cur[k]
        dy[o] = (-tot + iapp) / 10.0
        IntCa = y[o + 12]
        dy[o + 1] = (_boltz(V, 25.5, -5.29) - y[o + 1]) / (_taux(V, 1.32, 1.26, 120.0, -25.0) * f[8])
        dy[o + 2] = (_boltz(V, 48.9, 5.18) - y[o + 2]) / (
            _taux(V, 0.0, -0.67, 62.9, -10.0) * _taux(V, 1.50, -1.00, 34.9, 3.60) * f[9])
        dy[o + 3] = (_boltz(V, 27.1, -7.20) - y[o + 3]) / (_taux(V, 21.7, 21.3, 68.1, -20.5) * f[10])
        dy[o + 4] = (_boltz(V, 32.1, 5.50) - y[o + 4]) / (_taux(V, 105.0, 89.8, 55.0, -16.9) * f[11])
        dy[o + 5] = (_boltz(V, 33.0, -8.1) - y[o + 5]) / (_spectau(V, 1.40, 7.00, 27.0, 10.0, 70.0, -13.0) * f[12])
        dy[o + 6] = (_boltz(V, 60.0, 6.20) - y[o + 6]) / (_spectau(V, 60.0, 150.0, 55.0, 9.00, 65.0, -16.0) * f[13])
        dy[o + 7] = (_boltz(V, 70.0, 6.0) - y[o + 7]) / (_taux(V, 272.0, -1499.0, 42.2, -8.73) * f[14])
        dy[o + 8] = (_boltz(V, 12.3, -11.8) - y[o + 8]) / (_taux(V, 7.20, 6.40, 28.3, -19.2) * f[15])
        dy[o + 9] = ((IntCa / (IntCa + 3.0)) * _boltz(V, 28.3, -12.6) - y[o + 9]) / (
            _taux(V, 90.3, 75.1, 46.0, -22.7) * f[16])
        dy[o + 10] = (_boltz(V, 27.2, -8.70) - y[o + 10]) / (_taux(V, 11.6, 10.4, 32.9, -15.2) * f[17])
        dy[o + 11] = (_boltz(V, 56.9, 4.90) - y[o + 11]) / (_taux(V, 38.6, 29.2, 38.9, -26.5) * f[18])
        dy[o + 12] = (-0.94 * (cur[1] + cur[2]) - IntCa + 0.05) / (p[po + 35] * 10.0 * f[19])
    VAB, VLP, VPY = y[0], y[13], y[26]
    pre = (VAB, VAB, VAB, VAB, VLP, VPY, VLP)
    glut = (True, False, True, False, True, True, True)
    for k in range(7):
        ss = _syn_ss(pre[k])
        if glut[k]:
            tau = f[22] * (1.0 - ss) * 40.0
        else:
            tau = f[23] * (1.0 - ss) * 100.0
        dy[39 + k] = (ss - y[39 + k]) / (tau + 20.0)


@njit(cache=True, error_model="numpy")
def _run(y0, p, T0, T1, nsteps, dt, thr, rec_every, rec_start, full, hist_start, hist_lo, hist_bin, nbins):
    """RK4 from y0 for nsteps; temperature linear from T0 to T1 over the run. Returns the final
    state, upward crossings of thr per cell (time in ms, interpolated), upward and downward
    crossings of -50 mV, the recorded traces (V of each cell, or the full state when `full`, every
    rec_every steps from step rec_start) and voltage histograms from step hist_start."""
    n = y0.shape[0]
    y = y0.copy()
    k1 = np.empty(n); k2 = np.empty(n); k3 = np.empty(n); k4 = np.empty(n); tmp = np.empty(n)
    cur = np.empty(8); syn = np.empty(3)
    f = np.empty(25)
    maxev = int(nsteps * dt / 2.0) + 16           # at most one event per 2 ms
    spk = np.zeros((3, maxev)); nspk = np.zeros(3, np.int64)
    swu = np.zeros((3, maxev)); nswu = np.zeros(3, np.int64)
    swd = np.zeros((3, maxev)); nswd = np.zeros(3, np.int64)
    nrec = 0
    if rec_every > 0 and nsteps > rec_start:
        nrec = (nsteps - rec_start + rec_every - 1) // rec_every
    width = n if full else 3
    rec = np.zeros((nrec, width))
    hist = np.zeros((3, nbins))
    ri = 0
    ramp = T1 != T0
    _factors(p, T0, f)
    for i in range(nsteps):
        if ramp and i % 20 == 0:
            _factors(p, T0 + (T1 - T0) * (i + 10) / nsteps, f)
        if rec_every > 0 and i >= rec_start and (i - rec_start) % rec_every == 0:
            if full:
                for j in range(n):
                    rec[ri, j] = y[j]
            else:
                rec[ri, 0] = y[0]; rec[ri, 1] = y[13]; rec[ri, 2] = y[26]
            ri += 1
        if hist_start >= 0 and i >= hist_start:
            for c in range(3):
                b = int((y[13 * c] - hist_lo) / hist_bin)
                if 0 <= b < nbins:
                    hist[c, b] += 1
        _rhs(y, p, f, k1, cur, syn)
        for j in range(n):
            tmp[j] = y[j] + 0.5 * dt * k1[j]
        _rhs(tmp, p, f, k2, cur, syn)
        for j in range(n):
            tmp[j] = y[j] + 0.5 * dt * k2[j]
        _rhs(tmp, p, f, k3, cur, syn)
        for j in range(n):
            tmp[j] = y[j] + dt * k3[j]
        _rhs(tmp, p, f, k4, cur, syn)
        for c in range(3):
            v0 = y[13 * c]
            o = 13 * c
            v1 = y[o] + dt / 6.0 * (k1[o] + 2.0 * k2[o] + 2.0 * k3[o] + k4[o])
            t0 = i * dt
            if v0 < thr <= v1 and nspk[c] < maxev:
                spk[c, nspk[c]] = t0 + dt * (thr - v0) / (v1 - v0); nspk[c] += 1
            if v0 < -50.0 <= v1 and nswu[c] < maxev:
                swu[c, nswu[c]] = t0 + dt * (-50.0 - v0) / (v1 - v0); nswu[c] += 1
            if v0 >= -50.0 > v1 and nswd[c] < maxev:
                swd[c, nswd[c]] = t0 + dt * (-50.0 - v0) / (v1 - v0); nswd[c] += 1
        for j in range(n):
            y[j] = y[j] + dt / 6.0 * (k1[j] + 2.0 * k2[j] + 2.0 * k3[j] + k4[j])
    return y, spk, nspk, swu, nswu, swd, nswd, rec, hist


class Sim:
    """Result of one simulation. Times in seconds from the start of the run."""

    def __init__(self, out, dt, seconds, T0, T1, rec_every, rec_start, hist_lo, hist_bin):
        y, spk, nspk, swu, nswu, swd, nswd, rec, hist = out
        self.final = y
        self.finite = bool(np.isfinite(y).all())   # False when the integration diverged (NaN)
        self.spikes = [spk[c, :nspk[c]] / 1000.0 for c in range(3)]
        self.sw_up = [swu[c, :nswu[c]] / 1000.0 for c in range(3)]
        self.sw_down = [swd[c, :nswd[c]] / 1000.0 for c in range(3)]
        self.rec = rec
        self.rec_dt = dt * rec_every / 1000.0
        self.rec_t0 = rec_start * dt / 1000.0
        self.hist = hist
        self.hist_edges = hist_lo + hist_bin * np.arange(hist.shape[1] + 1)
        self.seconds, self.T0, self.T1 = seconds, T0, T1

    def temperature(self, t):
        return self.T0 + (self.T1 - self.T0) * np.asarray(t) / self.seconds

    def window(self, t0, t1):
        """Spike times of each cell within [t0, t1), shifted to start at 0."""
        return [s[(s >= t0) & (s < t1)] - t0 for s in self.spikes]


def simulate(p, temp, seconds, y0, temp_end=None, dt=DT, thr=SPIKE_THRESHOLD, rec_every=0,
             rec_from=0.0, full=False, hist_from=None, hist_lo=-100.0, hist_bin=0.1, nbins=1600):
    T1 = temp if temp_end is None else temp_end
    nsteps = int(round(seconds * 1000.0 / dt))
    rec_start = int(round(rec_from * 1000.0 / dt))
    hs = -1 if hist_from is None else int(round(hist_from * 1000.0 / dt))
    out = _run(np.asarray(y0, float), np.asarray(p, float), float(temp), float(T1), nsteps, dt, thr,
               rec_every, rec_start, full, hs, hist_lo, hist_bin, nbins)
    return Sim(out, dt, seconds, float(temp), float(T1), rec_every, rec_start, hist_lo, hist_bin)


def currents_from_states(states, p, temp):
    """Per cell: an array (9, n) of the 8 intrinsic currents and the synaptic current (nA,
    positive outward), from full states recorded at a fixed temperature."""
    f = np.empty(25)
    _factors(np.asarray(p, float), float(temp), f)
    return _currents_loop(states, np.asarray(p, float), f)


@njit(cache=True, error_model="numpy")
def _currents_loop(states, p, f):
    n = states.shape[0]
    out = np.zeros((3, 9, n))
    cur = np.empty(8); syn = np.empty(3)
    for i in range(n):
        y = states[i]
        _syn_currents(y, p, f, syn)
        for c in range(3):
            _cell_currents(y, 13 * c, p, 37 * c, f, cur)
            for k in range(8):
                out[c, k, i] = cur[k]
            out[c, 8, i] = syn[c]
    return out


def shares(curr):
    """Currentscape shares (plotCurrentScape): outward (positive) share of each current in the
    total outward current, inward (negative) share in the total inward current. curr is (k, n)."""
    pos = np.clip(curr, 0, None)
    neg = np.clip(-curr, 0, None)
    with np.errstate(invalid="ignore", divide="ignore"):
        out_sh = pos / pos.sum(axis=0)
        in_sh = neg / neg.sum(axis=0)
    return np.nan_to_num(out_sh), np.nan_to_num(in_sh)


# --- spikes, bursts and the classification scheme ---------------------------------------------

def bursts(spikes, gap=BURST_GAP):
    """Group spike times into bursts with a temporal threshold (Methods): returns (starts, ends,
    counts)."""
    s = np.asarray(spikes)
    if len(s) == 0:
        return np.array([]), np.array([]), np.array([], int)
    breaks = np.where(np.diff(s) > gap)[0]
    first = np.r_[0, breaks + 1]
    last = np.r_[breaks, len(s) - 1]
    return s[first], s[last], last - first + 1


def burst_stats(spikes, gap=BURST_GAP):
    """Per cycle: burst frequency (1 / time between successive burst starts), duty cycle (burst
    duration over period), as the Methods and the Results define them. The last burst is dropped
    (no period)."""
    st, en, cnt = bursts(spikes, gap)
    if len(st) < 2:
        return dict(starts=st, ends=en, counts=cnt, period=np.array([]), freq=np.array([]),
                    dc=np.array([]))
    period = np.diff(st)
    dur = (en - st)[:-1]
    return dict(starts=st, ends=en, counts=cnt, period=period, freq=1.0 / period, dc=dur / period)


def _cv(x):
    x = np.asarray(x, float)
    return np.std(x) / np.mean(x) if len(x) and np.mean(x) != 0 else np.inf


def classify_cell(spikes, sw_up):
    """Methods, Classification scheme. Returns one of: quiescent, tonic spiking, single-spike
    bursting, regular bursting, irregular bursting, irregular spiking, other."""
    s = np.asarray(spikes)
    if len(s) - 1 <= 1:
        return "quiescent"
    isi = np.diff(s)
    if _cv(isi) < 0.1:
        # lag d between spike onset and the last upward slow-wave crossing before it
        up = np.asarray(sw_up)
        if len(up) == 0:
            return "tonic spiking"   # V never crosses -50 mV upward in the window: no slow wave (assumption)
        idx = np.searchsorted(up, s) - 1
        lags = np.where(idx >= 0, s - up[np.clip(idx, 0, None)], np.inf)
        d = np.median(lags)
        return "tonic spiking" if d < 0.020 else "single-spike bursting"
    b = burst_stats(s)
    if len(b["dc"]) == 0:
        return "other"
    mdc = np.mean(b["dc"])
    if mdc > 0 and _cv(b["dc"]) < 1 and _cv(b["freq"]) < 0.1:
        return "regular bursting"
    if mdc > 0 and (_cv(b["dc"]) > 1 or _cv(b["freq"]) > 0.1):
        return "irregular bursting"
    if mdc == 0:
        return "irregular spiking"
    return "other"


def phases(spk3):
    """Burst onsets and offsets of LP and PY (and PD offset) in units of the PD period, from each
    PD burst start, per PD cycle; nan where a cell has no burst start in the cycle."""
    pd = burst_stats(spk3[0])
    out = {k: [] for k in ["PD off", "LP on", "LP off", "PY on", "PY off"]}
    bl = burst_stats(spk3[1]); bp = burst_stats(spk3[2])
    st = pd["starts"]
    for i in range(len(st) - 1):
        t0, T = st[i], st[i + 1] - st[i]
        out["PD off"].append((pd["ends"][i] - t0) / T)
        for name, b in (("LP", bl), ("PY", bp)):
            k = np.where((b["starts"] >= t0) & (b["starts"] < st[i + 1]))[0]
            if len(k):
                out[name + " on"].append((b["starts"][k[0]] - t0) / T)
                out[name + " off"].append((b["ends"][k[0]] - t0) / T)
            else:
                out[name + " on"].append(np.nan)
                out[name + " off"].append(np.nan)
    return {k: np.array(v) for k, v in out.items()}


def triphasic(spk3, strict=False):
    """Methods: triphasic when the three cells' burst frequencies agree within 5% and they fire in
    the right order (PD, LP, PY). Frequencies are each cell's mean burst frequency; agreement is
    (max - min) / max <= 0.05. Order (an assumption) as in the module docstring."""
    fr = []
    for s in spk3:
        b = burst_stats(s)
        if len(b["freq"]) < 2:
            return False
        fr.append(np.mean(b["freq"]))
    fr = np.array(fr)
    if (fr.max() - fr.min()) / fr.max() > 0.05:
        return False
    ph = phases(spk3)
    lp, py = ph["LP on"], ph["PY on"]
    if strict:
        return bool(np.all(np.isfinite(lp)) and np.all(np.isfinite(py)) and np.all(lp < py))
    if np.mean(np.isfinite(lp)) < 0.5 or np.mean(np.isfinite(py)) < 0.5:
        return False
    a, b = np.nanmedian(lp), np.nanmedian(py)
    return bool(0 < a < b < 1)


def classify(sim, t0, t1):
    """Cell classes of PD, LP, PY and the network class over [t0, t1) of a simulation. A run whose
    state became NaN (the RK4 diverged, as the deposited Java does too) is labelled
    "numerical failure"."""
    if not sim.finite:
        return ["numerical failure"] * 3 + ["not triphasic"]
    spk = sim.window(t0, t1)
    sw = [u[(u >= t0) & (u < t1)] - t0 for u in sim.sw_up]
    cls = [classify_cell(spk[c], sw[c]) for c in range(3)]
    net = "triphasic" if triphasic(spk) else "not triphasic"
    return cls + [net]


# --- parallel jobs (run in worker processes) ---------------------------------------------------

def pmap(fn, tasks, procs=4):
    """Map fn over tasks in `procs` processes (the runner has 4 CPUs)."""
    from multiprocessing import get_context
    with get_context("fork").Pool(procs) as pool:
        return pool.map(fn, tasks, chunksize=1)


def run_fixed(task):
    """task = (key, p, y0, temp, seconds, drop[, thr]). Simulates at a fixed temperature and returns,
    for the window after `drop` seconds, the spike times and upward slow-wave crossings of each cell
    (times from the window start), the four classes, and the final state. `thr` is the spike
    threshold (SPIKE_THRESHOLD when not given)."""
    key, p, y0, temp, seconds, drop = task[:6]
    thr = task[6] if len(task) > 6 else SPIKE_THRESHOLD
    s = simulate(p, temp, seconds, y0, thr=thr)
    return dict(key=key, temp=temp, spikes=s.window(drop, seconds),
                sw_up=[u[u >= drop] - drop for u in s.sw_up], classes=classify(s, drop, seconds),
                final=s.final, length=seconds - drop)


def run_states(task):
    """task = (key, p, y0, temp, seconds, record). Simulates and returns the full state at every
    step of the last `record` seconds, with the spike times in that window (times from its
    start)."""
    key, p, y0, temp, seconds, record = task
    s = simulate(p, temp, seconds, y0, rec_every=1, rec_from=seconds - record, full=True)
    return dict(key=key, temp=temp, states=s.rec, dt=s.rec_dt,
                spikes=s.window(seconds - record, seconds), classes=classify(s, seconds - record, seconds))


def run_ramp(task):
    """task = (key, p, y0, legs), legs a list of (T_start, T_end, seconds). Runs the legs one after
    the other from y0 and returns per leg the spike times (s from the leg start) and temperatures
    of the spikes."""
    key, p, y0, legs = task
    y = np.asarray(y0, float)
    out = []
    for T0, T1, sec in legs:
        s = simulate(p, T0, sec, y, temp_end=T1)
        out.append(dict(T0=T0, T1=T1, seconds=sec, spikes=s.spikes, sw_up=s.sw_up, finite=s.finite))
        y = s.final
    return dict(key=key, legs=out)


def slow_wave_bursts(V, spikes, dt, gap=BURST_GAP, level=SLOW_WAVE):
    """Bursts bounded by the slow wave: for each burst of `spikes` (s, grouped with the 200 ms
    threshold), the sample indices of the last upward crossing of `level` before its first spike and
    of the first downward crossing after its last spike, in the trace V sampled every dt s (the
    Methods' -50 mV slow-wave threshold, Classification scheme). Bursts whose crossings fall outside
    the trace are dropped."""
    up = np.where((V[:-1] < level) & (V[1:] >= level))[0] + 1
    down = np.where((V[:-1] >= level) & (V[1:] < level))[0] + 1
    out = []
    for s, e, k in zip(*bursts(spikes, gap)):
        i, j = int(s / dt), int(e / dt)
        u = up[up <= i]
        d = down[down > j]
        if len(u) and len(d):
            out.append((int(u[-1]), int(d[0]), int(k)))
    return out


def spike_region_start(hist, edges, frac, smooth=10, below=SPIKE_THRESHOLD):
    """fig2-lp-spike-amplitude-threshold, threshold reading (b): the voltage at which the
    distribution's spike region begins, read as the upper edge of the densely occupied part of the
    distribution: the highest voltage below `below` whose occupancy (smoothed over `smooth` bins of
    0.1 mV) is at least `frac` of the largest occupancy. Above it the cell passes only during spikes.
    The search stops at the spike detection level, which every spike crosses, so that the dwell
    near the spike peaks is not taken for the slow wave. An assumption: neither the paper nor the
    claims file says how the point is located; the notebook gives three values of `frac`."""
    h = np.convolve(hist, np.ones(smooth) / smooth, mode="same")
    centres = 0.5 * (edges[:-1] + edges[1:])
    k = np.where((h >= frac * h.max()) & (centres < below))[0]
    return float(centres[k[-1]]) if len(k) else np.nan


def peaks_after(V, idx, n):
    """Index of the maximum of V in the n samples after each index in idx."""
    return np.array([i + int(np.argmax(V[i:i + n])) for i in idx if i + n <= len(V)], int)


def dominant_summary(task):
    """currentscapes-dominant-currents, in a worker: simulate, compute shares and count, per cell,
    the spikes where Na holds the largest inward share in the 1 ms before the peak and Kd the
    largest outward share in the 1 ms after it, and the largest inward and outward currents over
    the 5% of time with the lowest voltage."""
    key, p, y0, temp, seconds, record = task
    r = run_states((key, p, y0, temp, seconds, record))
    st = r["states"]
    curr = currents_from_states(st, p, temp)
    n1 = int(round(0.001 / r["dt"]))
    res = []
    for c in range(3):
        V = st[:, 13 * c]
        out_sh, in_sh = shares(curr[c])
        cross = np.where((V[:-1] < SPIKE_THRESHOLD) & (V[1:] >= SPIKE_THRESHOLD))[0]
        pk = peaks_after(V, cross, int(round(0.003 / r["dt"])))
        pk = pk[(pk - n1 >= 0) & (pk + n1 < len(V))]
        na = kd = 0
        for i in pk:
            na += int(np.argmax(in_sh[:, i - n1:i].mean(axis=1)) == 0)
            kd += int(np.argmax(out_sh[:, i:i + n1].mean(axis=1)) == 5)
        low = V <= np.quantile(V, 0.05)
        top_in = int(np.argmax(in_sh[:, low].mean(axis=1)))
        top_out = int(np.argmax(out_sh[:, low].mean(axis=1)))
        both = np.maximum(in_sh[:, low].mean(axis=1), out_sh[:, low].mean(axis=1))
        res.append(dict(cell=CELLS[c], spikes=len(pk), na_first=na, kd_after=kd, low_in=top_in,
                        low_out=top_out, low_top2=sorted(np.argsort(both)[-2:].tolist())))
    return dict(key=key, temp=temp, cells=res, classes=r["classes"])


def end_shares(task):
    """fig5-a-to-kca-tradeoff, in a worker: mean outward shares in PD over the 20 ms after the
    last spike of each burst (from its threshold crossing)."""
    r = run_states(task)
    name, p = task[0], task[1]
    cur = currents_from_states(r["states"], p, r["temp"])[0]
    out_sh, _ = shares(cur)
    st, en, k = bursts(r["spikes"][0])
    n20 = int(round(0.020 / r["dt"]))
    w = [out_sh[:, int(e / r["dt"]):int(e / r["dt"]) + n20].mean(axis=1) for e in en
         if int(e / r["dt"]) + n20 <= out_sh.shape[1]]
    return name, r["temp"], np.mean(w, axis=0), len(w)


# --- ramps and voltage distributions -------------------------------------------------------------

def cycle_largest_isi(spikes, gap=BURST_GAP):
    """Per burst cycle (one burst start to the next): the burst start time and the largest ISI in
    the cycle, which is the interburst interval when the cell bursts."""
    s = np.asarray(spikes)
    st, en, cnt = bursts(s, gap)
    out_t, out_isi = [], []
    for a, b in zip(st[:-1], st[1:]):
        seg = s[(s >= a) & (s <= b)]
        if len(seg) >= 2:
            out_t.append(a)
            out_isi.append(np.max(np.diff(seg)))
    return np.array(out_t), np.array(out_isi)


def window_measures(spk3, t0, t1):
    """Per cell, over [t0, t1): mean duty cycle, mean burst frequency, median per-cycle largest ISI;
    and whether the network is triphasic in the window."""
    w = [s[(s >= t0) & (s < t1)] - t0 for s in spk3]
    out = []
    for s in w:
        b = burst_stats(s)
        t, isi = cycle_largest_isi(s)
        out.append((np.mean(b["dc"]) if len(b["dc"]) else np.nan,
                    np.mean(b["freq"]) if len(b["freq"]) else np.nan,
                    np.median(isi) if len(isi) else np.nan))
    return np.array(out), triphasic(w)


def spike_shapes(V, dt_ms, thr=SPIKE_THRESHOLD, dvdt=10.0):
    """fig2-lp-spike-amplitude-threshold readings (a). For each upward crossing of thr: the peak
    (largest V in the 3 ms after), the trough (lowest V between the previous peak, at most 30 ms
    back, and the crossing), and the threshold (V at the first sample after the trough where
    dV/dt exceeds dvdt mV/ms, a standard choice). Returns arrays of peak, trough, threshold."""
    cross = np.where((V[:-1] < thr) & (V[1:] >= thr))[0]
    n3, n30 = int(round(3 / dt_ms)), int(round(30 / dt_ms))
    d = np.diff(V) / dt_ms
    peaks, troughs, ths = [], [], []
    prev = -10 ** 9
    for i in cross:
        if i + n3 > len(V):
            break
        a = max(prev, i - n30, 0)
        if i - a < 2:
            prev = i + int(np.argmax(V[i:i + n3]))
            continue
        k = a + int(np.argmin(V[a:i + 1]))
        up = np.where(d[k:i + 1] > dvdt)[0]
        pk = i + int(np.argmax(V[i:i + n3]))
        peaks.append(V[pk]); troughs.append(V[k]); ths.append(V[k + up[0]] if len(up) else np.nan)
        prev = pk
    return np.array(peaks), np.array(troughs), np.array(ths)


def run_distribution(task):
    """task = (key, p, y0, temp, seconds, last, dt, every). Simulates `seconds` at dt from y0 and
    keeps V of each cell every `every` steps over the last `last` seconds (Methods, Membrane
    potential and current shares distributions: 30 s, dt = 0.001, the last 10 s, 5 x 10^5
    samples). Returns, per cell, the histogram (0.1 mV bins from -100 mV), mean V, the upper
    envelope (highest V), the lowest V and the spike shape summaries."""
    key, p, y0, temp, seconds, last, dt, every = task
    s = simulate(p, temp, seconds, y0, dt=dt, rec_every=every, rec_from=seconds - last)
    V3 = s.rec
    res = []
    edges = -100.0 + 0.1 * np.arange(1601)
    for c in range(3):
        V = V3[:, c]
        h, _ = np.histogram(V, edges)
        pk, tr, th = spike_shapes(V, dt * every)
        res.append(dict(cell=CELLS[c], n=len(V), mean=float(np.mean(V)), vmax=float(np.max(V)), vmin=float(np.min(V)),
                        hist=h, spikes=len(pk), peak=float(np.mean(pk)) if len(pk) else np.nan,
                        amp=float(np.mean(pk - tr)) if len(pk) else np.nan,
                        thr=float(np.nanmean(th)) if len(th) and np.isfinite(th).any() else np.nan))
    return dict(key=key, temp=temp, finite=s.finite, cells=res)
