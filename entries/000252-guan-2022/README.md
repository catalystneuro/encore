# Guan et al. (preprint 2022) from dandiset 000252

Tests the findings of [Guan et al. (2022)](https://doi.org/10.1101/2022.12.07.22283227) that can be
tested on [DANDI:000252](https://dandiarchive.org/dandiset/000252/0.230408.2207). The dandiset holds
the ten-finger press task: 10 sessions of participant N (one PPC array) and 2 sessions of
participant J (a PPC and an MC array), with sorted units and trial times. The alternating-cues
task and the BMI sessions of Figures 4 to 6 are not in it.

| Claim | Outcome |
|---|---|
| Neurons per session and sessions in the ten-finger task | Reproduced (counts before the 0.5 Hz exclusion) |
| 1111 N-PPC neurons pooled | Reproduced |
| Most neurons discriminate the ten fingers (66%, 57%, 78%) | Not reproduced |
| Ten-finger decoding accuracy (70%, 66%, 75%) | Reproduced |
| Most errors are adjacent or matching fingers | Reproduced |
| Matching fingers of the two hands are closer than non-matching ones | Reproduced, resting on an assumption |
| N-PPC index finger distinct from middle and ring in both hands | Reproduced |
| Hand decoders generalize across finger types | Reproduced |
| Finger-type decoders generalize across hands (N-PPC, J-MC) | Reproduced |
| J-PPC finger-type generalization is low (36% against 65%) | Partially reproduced, resting on an assumption |
| J-PPC finger-type generalization lowest at matched population size | Reproduced |
| Alternating-cues task, Figures 4 and 5 (five claims) | Blocked: data missing |
| Online BMI, Figure 6 and Supplementary Figures 6 and 7 (three claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/000252-guan-2022-01.yaml`](../../attempts/000252-guan-2022-01.yaml).

- `reproduce_guan_2022.ipynb`: the analysis. It takes about fourteen minutes, most of it the
  permutation tests of the cross-condition generalization.
- `fingers.py`: streaming the files, firing rates in the paper's analysis windows, the 0.5 Hz
  exclusion, diagonal LDA, single-neuron ANOVA with FDR, cross-validated Mahalanobis distances
  (rsatoolbox) and cross-condition generalization. Other notebooks on this dandiset can import it.
