# Lee et al. (2014) from CRCNS hc-10

Tests the findings of [Lee et al. (2014)](https://doi.org/10.1016/j.neuron.2014.03.034) that can be
tested on [CRCNS hc-10](https://doi.org/10.6080/K00P0WXQ), which holds the current-step sweeps of
8 superficial and 9 deep CA1 pyramidal cells (PCs) and 6 PV+ basket cells (PVBCs) of the paper,
with cells of other papers. These are the data of Figures S1E to S1H, S3F and Table S1.

| Claim | Outcome |
|---|---|
| sPCs and dPCs do not differ in firing against injected current (Figure S1E) | Reproduced |
| sPCs and dPCs do not differ in input resistance, 117 and 124 MOhm (Figure S1F) | Reproduced |
| sPCs rest more depolarized than dPCs (Figure S1G) | Blocked: data missing |
| sPCs have larger sag than dPCs, 8.7 and 5.6 mV (Figure S1H) | Reproduced |
| Both groups have a rheobase of +150 pA (Table S1) | Partially reproduced |
| A PVBC fires from +350 pA, at 2, 17, 36 and 52 Hz (Figure S3F) | Reproduced |
| Paired recordings, anatomy, imaging, optogenetics, retrograde labelling (26 claims) | Blocked: data missing |
| Network model simulations (2 claims) | Blocked: too large |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The files hold voltage only, with no injected or holding current; the step levels come from the
data set's description. The PC sweeps start at the -70 mV holding potential, so the resting
potential is not in them. The attempt record, with the reasons and the differences from the
paper's method, is [`attempts/crcns-hc-10-lee-2014-01.yaml`](../../attempts/crcns-hc-10-lee-2014-01.yaml).

- `reproduce_lee_2014.ipynb`: the analysis. It takes about 12 minutes, most of it a 20 ms run of the
  paper's network model, timed to estimate the cost of the two model claims.
- `hc10.py`: streaming and parsing the ATF files, the step window, and the measures of firing,
  input resistance and sag. Other notebooks on this data set can import it.
