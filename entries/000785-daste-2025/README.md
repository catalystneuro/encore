# Daste, Pierré et al. (2025) from dandiset 000785

Tests the findings of [Daste, Pierré et al. (2025)](https://doi.org/10.64898/2025.12.12.694045), a
bioRxiv preprint, on [DANDI:000785](https://dandiarchive.org/dandiset/000785/0.260520.1603). The
dandiset holds two-photon imaging of anterior piriform cortex neurons projecting to the olfactory
bulb (OB-p) or the medial prefrontal cortex (mPFC-p): passive odor identity, concentration and 30 Hz
experiments, and a Go/NoGo task over four days with cells tracked across sessions.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

| Claims | Outcome |
|---|---|
| Neuron counts of the passive and 30 Hz experiments, tracked-neuron counts | Reproduced |
| Go/NoGo neuron counts per session | Partially reproduced |
| Labeling similar in OB-p and mPFC-p mice | Reproduced |
| Transformer and MLP classifiers (four claims) | Blocked: Tables 5, 6 and 8 missing from the text |
| Single-cell properties of Figure 2 (sparseness, mutual information, reliability) | Not reproduced (four claims); proportion responding reproduced |
| 30 Hz latencies and early peaks | Reproduced |
| Identity decoding (Figure 2H to 2K) | Three reproduced, one blocked (the two windows disagree) |
| Concentration tuning, decoding and sparseness (Figures 3, S5) | Two reproduced, one partially, one not |
| Behavior (learning, anticipatory licking) | Learning not reproduced, licking reproduced |
| Go/NoGo decoding (Figures 4D to 4J, S8) | Identity and any-p valence reproduced; three valence-timing claims not |
| Differences growing over learning (Discussion) | Reproduced, resting on an assumption |
| Tracked neurons (Figures 5, S10) | Three reproduced (one resting on an assumption), one partially, one blocked |

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/000785-daste-2025-01.yaml`](../../attempts/000785-daste-2025-01.yaml).

- `reproduce_daste_2025_passive.ipynb`: counts, the identity, concentration and 30 Hz experiments.
- `reproduce_daste_2025_gng.ipynb`: the Go/NoGo behavior, pseudo-population decoding and tracked
  neurons.
- `pcx.py`: streaming the files, the paper code's normalization, binarization, sparseness, mutual
  information, pseudo-populations and the decoders. Other notebooks on this dandiset can import it.
