# Namima, Kempkes, Zamarashkina, Owen & Pasupathy (2025) from dandiset 001357

Tests the findings of [Namima et al. (2025)](https://doi.org/10.1523/jneurosci.1893-23.2024) that can
be tested on [DANDI:001357](https://dandiarchive.org/dandiset/001357/0.261006.2007), which holds the
spike times of Neuropixels units in V4 of two monkeys during the shape test (74 sessions), the texture
test (51) and the position control (34).

| Claim | Outcome |
|---|---|
| Session and neuron counts | Reproduced |
| M2p6: a cluster of similarly tuned superficial neurons | Partially reproduced |
| M2p6: similarity of two example pairs | Partially reproduced |
| M2p6: contrast invariance in 19 of 24 neurons | Reproduced |
| M2p6 and M1p12: CSD sinks | Blocked: no LF signal in the dandiset |
| M1p12: no cluster, high invariance | Reproduced |
| M1p12: strong peak responses | Reproduced |
| 344 of 1,850 neurons with significant Isimilarity | Partially reproduced |
| Isimilarity and Ssimilarity correlated, r = -0.745 | Reproduced |
| Dark and bright Isimilarity consistent, r = 0.435 | Not reproduced |
| Median contrast invariance 0.64 | Reproduced |
| Clusters in 55 of 74 penetrations, 28 with five or more | Reproduced |
| About 20% significant when more than 30 neurons | Reproduced |
| Mean Isimilarity levels off with yield | Reproduced |
| Weak relation to recording density, r = 0.236 | Reproduced |
| Same-session pairs slightly more similar | Partially reproduced |
| Orientation x SF fits | Blocked: shape images not public |
| Coarse orientation preference along the probe | Not reproduced |
| APC peak clustering (two claims) | Blocked: shape descriptions not public |
| 18 gyral penetrations | Blocked: penetration coordinates not in the dandiset |
| Texture: 207 of 979 neurons clustered | Not reproduced |
| Texture: original and reversed Isimilarity consistent, r = 0.464 | Not reproduced |
| Texture: about 20% significant in large penetrations | Not reproduced |
| Isimilarity at the optimal position, r = 0.325 | Reproduced |
| Example penetrations at five positions | Not reproduced |
| Simulation of tuning progressions | Blocked: methods underspecified |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/001357-namima-2025-01.yaml`](../../attempts/001357-namima-2025-01.yaml).

- `reproduce_namima_2025.ipynb`: the analysis. It takes about eight minutes, half of it streaming the
  files.
- `v4clusters.py`: loading the files into spike counts per presentation, the noise-corrected
  correlation with its bootstrap, Isimilarity, and the per-session analyses. Other notebooks on this
  dandiset can import it.
