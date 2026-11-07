"""Network models of Li, Daie, Svoboda & Druckmann (2016), Methods, "Modeling and simulation",
and Extended Data Fig. 1f-i. No recorded data are used.

Every network follows tau dr/dt = -r + W f(r) + I(t) + T + xi(t), simulated for 2 s by Euler
steps; photoinhibition holds the silenced neurons at zero for 0.2 s < t < 1.0 s (Methods).
Parameters are the Methods' unless said otherwise:

- Modular attractor (Fig. 6b): two modules of two neurons; self weight 0.5235, within-module
  -0.5235, each neuron coupled to its same-preference partner in the other module with 0.3;
  tau = 100 ms; f(x) = g(x) - g(0), g(x) = 1.4 / (1 + exp(-(x - 0.5) / 0.3)); transient input
  0.1 to the neurons preferring the trial type for 0.05 s < t < 0.1 s; tonic input 0.5; noise of
  variance 0.01. Whether the variance is per step or per unit time is not stated; both are run
  (`noise="step"`: xi drawn each step with variance 0.01; `noise="time"`: white noise of
  intensity 0.01 per second). That the partner is the same-preference neuron is an assumption
  (the Methods say "one partner").
- Modular integrator (Fig. 6c): the printed 8 x 8 matrix, linear synapses, rates kept
  non-negative, tau = 10 ms, input +-0.04 to the right and left preferring neurons of both
  modules for 0.1 s < t < 1.9 s (persistent input, Methods), tonic 40 to the four integrator
  neurons, no noise.
- Simple integrator (ED Fig. 1f): N = 100, tau = 100 ms, linear, connectivity with one non-zero
  eigenvalue 0.99; the matrix is taken as 0.99 u u^T with u a random unit vector (the Methods fix
  only the spectrum; three draws), input a persistent current along u with sign by trial type,
  output u^T r, 50 random neurons silenced.
- Monolithic attractor: one module of the modular attractor without inter-module connections
  (the claims file's reading; the paper gives no parameters for it); "half the neurons" is one
  of its two neurons, either one.
- Trained recurrent network (ED Fig. 1h): FORCE learning (Sussillo and Abbott 2009) with
  tau = 200 ms, tanh, N = 400, connection probability 0.1, weights with variance 1.5^2 / (p N),
  transient input for 0.05 s < t < 0.1 s with Gaussian weights of variance 1 and opposite signs
  for the two trial types, 30 training trials. Open details, standard choices: the target is a
  linear ramp of the output from 0 at 0.1 s to +-1 at 2 s, the output is fed back through random
  weights uniform in [-1, 1], the recursive least squares rule starts from P = I and updates
  every 2 ms, Euler step 1 ms. 200 random neurons silenced.

Integration step 1 ms (0.1 ms for the 10 ms integrator), a standard choice.
"""
import numpy as np

T_END = 2.0
SIL = (0.2, 1.0)


def _g(x):
    return 1.4 / (1 + np.exp(-(x - 0.5) / 0.3))


def attractor_f(x):
    return _g(x) - _g(0.0)


def attractor_weights(inter=0.3, self_w=0.5235):
    """Neurons [R1, L1, R2, L2]."""
    W = np.array([[self_w, -self_w, 0, 0], [-self_w, self_w, 0, 0], [0, 0, self_w, -self_w], [0, 0, -self_w, self_w]], float)
    W[0, 2] = W[2, 0] = inter
    W[1, 3] = W[3, 1] = inter
    return W


def run_attractor(trial, silence, rng, W=None, noise="step", dt=0.001, tau=0.1, var=0.01):
    """Simulate the attractor; trial +1 (right) or -1 (left); silence: indices held at zero."""
    W = attractor_weights() if W is None else W
    n = W.shape[0]
    pref = np.array([1, -1, 1, -1][:n])
    steps = int(round(T_END / dt))
    r = np.zeros(n)
    out = np.zeros((steps, n))
    for k in range(steps):
        t = k * dt
        I = 0.1 * (pref == trial) if 0.05 <= t < 0.1 else np.zeros(n)
        xi = rng.normal(0, np.sqrt(var), n)
        drive = -r + W @ attractor_f(r) + I + 0.5
        if noise == "step":
            r = r + dt / tau * (drive + xi)
        else:
            r = r + dt / tau * drive + np.sqrt(dt) / tau * xi
        if silence is not None and len(silence) and SIL[0] < t < SIL[1]:
            r[list(silence)] = 0.0
        out[k] = r
    return out


INTEGRATOR_W = np.array([
    [0, -1, 0, 0, 0, 0, 0.5, 0],
    [-1, 0, 0, 0, 0, 0, -0.5, 0],
    [1, -1, 0, 0, 0, 0, 0, -6],
    [1, -1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0.5, 0, 0, -1, 0, 0],
    [0, 0, -0.5, 0, -1, 0, 0, 0],
    [0, 0, 0, -6, 1, -1, 0, 0],
    [0, 0, 0, 0, 1, -1, 0, 0],
], float)


def run_integrator(trial, silence, dt=0.0001, tau=0.01, amp=0.04, tonic=40.0):
    """The modular integrator (Methods matrix); returns rates every 1 ms."""
    W = INTEGRATOR_W
    steps = int(round(T_END / dt))
    every = int(round(0.001 / dt))
    r = np.zeros(8)
    r[[0, 1, 4, 5]] = tonic / 2
    out = []
    T = np.zeros(8)
    T[[0, 1, 4, 5]] = tonic
    for k in range(steps):
        t = k * dt
        I = np.zeros(8)
        if 0.1 <= t < 1.9:
            I[[0, 4]] = amp * trial
            I[[1, 5]] = -amp * trial
        r = r + dt / tau * (-r + W @ r + I + T)
        r = np.maximum(r, 0.0)
        if silence is not None and len(silence) and SIL[0] < t < SIL[1]:
            r[list(silence)] = 0.0
        if k % every == 0:
            out.append(r.copy())
    return np.array(out)


def run_simple_integrator(trial, silence, u, dt=0.001, tau=0.1, amp=1.0):
    """Rank-one linear integrator 0.99 u u^T with persistent input along u; returns u^T r."""
    W = 0.99 * np.outer(u, u)
    steps = int(round(T_END / dt))
    r = np.zeros(len(u))
    out = np.zeros(steps)
    for k in range(steps):
        t = k * dt
        I = amp * trial * u if 0.1 <= t < 1.9 else 0.0
        r = r + dt / tau * (-r + W @ r + I)
        if silence is not None and len(silence) and SIL[0] < t < SIL[1]:
            r[silence] = 0.0
        out[k] = u @ r
    return out


class Force:
    """A FORCE-trained rate network (Sussillo and Abbott 2009) producing a ramp."""

    def __init__(self, rng, N=400, p=0.1, g=1.5, tau=0.2, dt=0.001):
        self.N, self.tau, self.dt = N, tau, dt
        mask = rng.random((N, N)) < p
        self.J = np.where(mask, rng.normal(0, g / np.sqrt(p * N), (N, N)), 0.0)
        self.w_in = rng.normal(0, 1.0, N)
        self.w_fb = rng.uniform(-1, 1, N)
        self.w_out = np.zeros(N)
        self.P = np.eye(N)
        self.x0 = rng.normal(0, 0.5, N)

    def target(self, t, trial):
        return trial * np.clip((t - 0.1) / 1.9, 0, 1)

    def run(self, trial, silence=None, train=False, every=2):
        steps = int(round(T_END / self.dt))
        x = self.x0.copy()
        r = np.tanh(x)
        z = self.w_out @ r
        zs = np.zeros(steps)
        for k in range(steps):
            t = k * self.dt
            u = trial if 0.05 <= t < 0.1 else 0.0
            x = x + self.dt / self.tau * (-x + self.J @ r + self.w_fb * z + self.w_in * u)
            r = np.tanh(x)
            if silence is not None and len(silence) and SIL[0] < t < SIL[1]:
                r[silence] = 0.0
            z = self.w_out @ r
            if train and k % every == 0:
                Pr = self.P @ r
                c = 1.0 / (1.0 + r @ Pr)
                self.P -= c * np.outer(Pr, Pr)
                e = z - self.target(t, trial)
                self.w_out -= c * e * Pr
                z = self.w_out @ r
            zs[k] = z
        return zs

    def train(self, n_trials=30, rng=None):
        for i in range(n_trials):
            self.run(1 if i % 2 == 0 else -1, train=True)
