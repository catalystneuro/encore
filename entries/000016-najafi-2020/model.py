"""The linearised rate model of Najafi et al. (2020), STAR Methods, "Modeling decision circuits".

Steady state of
    dv_E/dt = -v_E + W_EE v_E - W_EI v_I + h_s + xi_E
    dv_I/dt = -v_I + W_IE v_E - W_II v_I + xi_I,
so that v_E = J_E (h_s + xi_E - W~_EI xi_I) and v_I = J_I (xi_I + W~_IE (h_s + xi_E)), with
J_E = (I - W_EE + W~_EI W_IE)^-1, J_I = (I + W_II + W~_IE W_EI)^-1, W~_EI = W_EI (I + W_II)^-1 and
W~_IE = W_IE (I - W_EE)^-1. The optimal linear decoder of n neurons D_n has accuracy
Phi(sqrt(S/N) / 2), with S/N = s^T (D C D^T)^-1 s for the mean difference s and covariance C of
the n neurons (Methods; the claims file reads the garbled formula as Phi(sqrt(S/N)/2)).

Parameters (Methods, "Simulation details", as the claims file lists them): sigma 1.25, delta 0.75,
w_EE 0.25, w_II -2, w_IE(0) 0.87, w_EI(0) -0.87, c 0.1, N_E 4000, N_I 1000, n 50, h0 0.1, rho 0.75.
Connections W_ab,ij = w_ab / (c N) with probability c, N = N_E + N_I. The ratio on the x-axis of
Figure 5 is that of the mean E-to-I to the mean I-to-E strength, varied as W_IE -> g W_IE,
W_EI -> W_EI / g (product kept at the reference), so the ratio is g^2.

Two details of the Methods admit more than one reading, and each is run:
- sign: the printed inhibitory weights are negative while the equations already carry minus
  signs for inhibition; "signed" puts the printed values into the equations as written,
  "magnitude" their absolute values (inhibition inhibits);
- scale: the connection strength reads w_ab / (c N) in the extracted text ("cN"); the formula is
  garbled there and could be w_ab / sqrt(c N) ("sqrt_cN"), the usual scaling of sparse networks.
The range of the ratio is 0.1 to 10 on a log scale (claims file; 21 points, a standard choice).
"""

from __future__ import annotations

import numpy as np
from scipy import linalg
from scipy.stats import norm, rankdata

P = dict(sigma=1.25, delta=0.75, wEE=0.25, wII=-2.0, wIE=0.87, wEI=-0.87, c=0.1, NE=4000, NI=1000,
         n=50, h0=0.1, rho=0.75)
RATIOS = np.logspace(-1, 1, 21)


def _sparse(rng, rows, cols, w, c, N, scale="cN"):
    return (rng.random((rows, cols)) < c) * (w / ((c * N) if scale == "cN" else np.sqrt(c * N)))


def network(rng, kind="nonselective", reading="signed", scale="cN", p=P):
    """Connectivity, noise and input difference of one network at the reference ratio."""
    NE, NI, c = p["NE"], p["NI"], p["c"]
    N = NE + NI
    sgn = (lambda w: w) if reading == "signed" else abs
    wEE, wII, wIE, wEI = p["wEE"], sgn(p["wII"]), p["wIE"], sgn(p["wEI"])
    if kind == "signal":
        pe = np.r_[np.zeros(NE // 2, int), np.ones(NE - NE // 2, int)]
        pi = np.r_[np.zeros(NI // 2, int), np.ones(NI - NI // 2, int)]

        def block(rows, cols, w, prow, pcol):
            W = _sparse(rng, rows, cols, w, c, N, scale)
            return W * np.where(prow[:, None] == pcol[None, :], 1.0, p["rho"])
        W = dict(EE=block(NE, NE, wEE, pe, pe), II=block(NI, NI, wII, pi, pi),
                 IE=block(NI, NE, wIE, pi, pe), EI=block(NE, NI, wEI, pe, pi))
        dh = np.where(pe == 0, 2 * p["h0"], -2 * p["h0"])
    else:
        W = dict(EE=_sparse(rng, NE, NE, wEE, c, N, scale), II=_sparse(rng, NI, NI, wII, c, N, scale),
                 IE=_sparse(rng, NI, NE, wIE, c, N, scale), EI=_sparse(rng, NE, NI, wEI, c, N, scale))
        dh = 2 * p["h0"] * rng.choice([-1.0, 1.0], NE)
    lo, hi = p["sigma"] - p["delta"] / 2, p["sigma"] + p["delta"] / 2
    sEE = rng.uniform(lo, hi, NE)
    sII = rng.uniform(lo, hi, NI)
    return dict(W=W, dh=dh, sEE=sEE, sII=sII, kind=kind)


def _parts(net):
    """Quantities that do not depend on the ratio g."""
    W = net["W"]
    NE, NI = W["EE"].shape[0], W["II"].shape[0]
    IpII = np.eye(NI) + W["II"]
    tEI = linalg.solve(IpII.T, W["EI"].T).T                       # W_EI (I + W_II)^-1
    ImEE = np.eye(NE) - W["EE"]
    tIE = linalg.solve(ImEE.T, W["IE"].T).T                       # W_IE (I - W_EE)^-1
    JE = linalg.inv(np.eye(NE) - W["EE"] + tEI @ W["IE"])
    JI = linalg.inv(IpII + tIE @ W["EI"])
    return dict(JE=JE, JI=JI, tEI=tEI, tIE=tIE)


def snr_selective(net, g, base_parts=None):
    """Reweight E-to-I connections by (rank of the E neuron's single-neuron S/N / N_E)^4, rescaled
    to the same mean (Methods), at ratio g^2. The ranking uses the non-selective network at that
    ratio (input-averaged S/N; J_E does not depend on the ratio). Returns a new network."""
    pt = base_parts or _parts(net)
    JE, A = pt["JE"], pt["JE"] @ pt["tEI"]
    sig = (JE ** 2).sum(1)
    noise = (JE ** 2) @ net["sEE"] + (A ** 2) @ net["sII"] / g ** 2
    r = rankdata(sig / noise)                                     # ascending S/N
    W = {k: v.copy() for k, v in net["W"].items()}
    NE = W["EE"].shape[0]
    mean0 = W["IE"].mean()
    W["IE"] = W["IE"] * (r[None, :] / NE) ** 4
    W["IE"] *= mean0 / W["IE"].mean()
    return dict(W=W, dh=net["dh"], sEE=net["sEE"], sII=net["sII"], kind="snr")


def readout_stats(net, picks_E, picks_I, parts=None):
    """Per pick of n read-out neurons, the pieces of the signal and covariance at the reference
    ratio, from which any ratio follows: for E, C = A + B / g^2 and signal S; for I, C = A + g^2 B
    and signal g S (W~_EI scales as 1/g and W~_IE as g; J_E and J_I do not change)."""
    pt = parts or _parts(net)
    JE, JI = pt["JE"], pt["JI"]
    JEt, JIt = JE @ pt["tEI"], JI @ pt["tIE"]
    dh, sEE, sII = net["dh"], net["sEE"], net["sII"]
    out = {"E": [], "I": []}
    for d in picks_E:
        R = JE[d]
        Rn = JEt[d]
        out["E"].append(dict(A=(R * sEE) @ R.T, B=(Rn * sII) @ Rn.T, SS=R @ R.T, s=R @ dh))
    for d in picks_I:
        R = JI[d]
        S = JIt[d]
        out["I"].append(dict(A=(R * sII) @ R.T, B=(S * sEE) @ S.T, SS=S @ S.T, s=S @ dh))
    return out


def accuracy(stats, ratios, averaged=True, eps=0.0):
    """Mean decoding accuracy over picks for each ratio, for E and I read-outs.

    averaged: the input-averaged S/N of the Methods (non-selective and SNR-selective);
    otherwise the S/N for the network's own input difference. eps adds differential
    correlations eps * dh dh^T to Sigma_EE (Figure S8A legend)."""
    out = {}
    for pop in ("E", "I"):
        acc = np.zeros(len(ratios))
        for k, r in enumerate(ratios):
            g2 = r
            vals = []
            for st in stats[pop]:
                if pop == "E":
                    C, s, SS = st["A"] + st["B"] / g2, st["s"], st["SS"]
                else:
                    C, s, SS = st["A"] + g2 * st["B"], np.sqrt(g2) * st["s"], g2 * st["SS"]
                if eps:
                    C = C + eps * np.outer(s, s)
                if averaged and not eps:
                    snr = 4 * P["h0"] ** 2 * np.trace(linalg.solve(C, SS, assume_a="pos"))
                else:
                    snr = float(s @ linalg.solve(C, s, assume_a="pos"))
                vals.append(norm.cdf(np.sqrt(snr) / 2))
            acc[k] = np.mean(vals)
        out[pop] = acc
    return out
