# Pasquereau & Turner (2013) from dandiset 001636

Tests the findings of [Pasquereau and Turner (2013)](https://doi.org/10.3389/fnsys.2013.00098) that
can be tested on [DANDI:001636](https://dandiarchive.org/dandiset/001636/0.261124.1906), which holds
single-unit recordings from primary motor cortex of monkeys V (Venus) and L (Leu) before and after
MPTP. Only the monkey V files mark the torque perturbations, so every claim is tested on monkey V.

| Claim | Outcome |
|---|---|
| Cells studied in monkey V, by state and projection type | Reproduced |
| Monkey L responses to wrist perturbations | Blocked: data missing |
| Baseline rate lower after MPTP for PTNs, not CSNs | Reproduced |
| PTNs fire faster than CSNs at rest | Reproduced |
| CSN antidromic latency longer after MPTP, PTN unchanged | Partially reproduced |
| False-positive rate of the response detection near 0.01 | Blocked: methods underspecified |
| 15 claims on the selected responses (prevalence, magnitude, latency, FWHM, directionality, correlations) | Blocked: methods underspecified |
| Torque-induced displacements slower and smaller after MPTP | Not reproduced |
| Latency of torque-induced displacements unchanged | Not reproduced |
| Long-latency (m2) EMG response larger after MPTP | Reproduced |
| EMG responses last longer after MPTP | Partially reproduced |
| Onset of EMG responses unchanged | Not reproduced |
| Short-latency (m1) EMG response weak | Partially reproduced |
| Trial-by-trial latency correlations | Blocked: methods underspecified |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The response detection the claims file specifies crosses its threshold in 23% of cell-directions
at a pseudo onset, about 20 times the paper's stated 1%, so the claims that rest on the selection
of responses are blocked; their results are shown in the notebook. The torque command's pulses are
about three times larger after MPTP than before, and the evoked displacements are faster and
larger after MPTP, the reverse of the paper's. The attempt record, with the reasons and the
differences from the paper's method, is
[`attempts/pasquereau-2013-03.yaml`](../../attempts/pasquereau-2013-03.yaml).

- `reproduce_pasquereau_2013.ipynb`: the analysis. It takes about seven minutes, most of it
  streaming the files.
- `pasq.py`: loading the files, spike density functions, response detection, kinematics and EMG
  measures, with where each parameter comes from. Other notebooks on this dandiset can import it.
