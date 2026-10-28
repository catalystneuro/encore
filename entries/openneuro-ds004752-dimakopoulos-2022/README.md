# Dimakopoulos, Mégevand, Stieglitz, Imbach & Sarnthein (2022) from OpenNeuro ds004752

Tests the findings of [Dimakopoulos et al. (2022)](https://doi.org/10.7554/elife.78677) on
[OpenNeuro ds004752](https://openneuro.org/datasets/ds004752/versions/1.0.1), snapshot 1.0.1, which
holds hippocampal depth recordings, ECoG in four participants, scalp EEG and LCMV virtual sensors
from 15 epilepsy patients performing a modified Sternberg task.

| Claim | Outcome |
|---|---|
| 15 participants, 71 sessions of 50 trials | Partially reproduced (68 sessions) |
| Accuracy 91%, falling with set size | Reproduced |
| Cowan's K of 6.1 | Reproduced |
| Response times and 53 ms per item | Reproduced |
| Participant 1, gamma over 100% at H3 and C2 in encoding | Partially reproduced |
| Participant 1, [11 14] Hz in maintenance at temporal and occipital contacts | Reproduced |
| Hippocampal beta over 100% in all four ECoG participants | Not reproduced |
| Participant 1, theta PLV 0.4 at C3 in maintenance | Not reproduced |
| Participant 1, GC reversal between hippocampus and C2 | Not reproduced (rests on an assumption) |
| Participant 1, spatial pattern of GC on the grid | Not reproduced |
| Participants 2 and 3, GC reversal | Not reproduced (rests on an assumption) |
| Participant 4, no GC on right parietal cortex | Not reproduced |
| Over 80% of significant EEG sources in the left hemisphere | Blocked: not runnable |
| Group GC reversal with the auditory source | Not reproduced |
| Temporal scalp electrodes, eliminated by a Laplacian | Reproduced (rests on an assumption) |
| Auditory cortex strongest among areas | Not reproduced |
| Reversal in all 15 participants, medians -0.049 and 0.034 | Not reproduced |
| Table 1 per-participant ΔGranger | Partially reproduced (rests on an assumption) |
| No reversal for lateral prefrontal cortex | Not reproduced (rests on an assumption) |
| No reversal on incorrect trials | Reproduced (rests on an assumption) |
| Reversal with 10% of correct trials | Reproduced (rests on an assumption) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The per-participant net flow reproduces the paper's sign pattern only when it is taken as the
minimum (encoding) or maximum (maintenance) over 4 to 8 Hz, as the paper's code does; the same
statistic gives the pattern for every area and for spectra with no direction, and the band mean
shows no effect. The per-frequency significance test flags a GC reversal in many trial pairings
with no trial-by-trial coupling (they keep the stimulus-locked responses; subtracting those does
not change this), so the ECoG reversals are judged with the cluster test. The scrambled-trial
cluster test that the figure legends name agrees on the reversals and finds GC in Participant 4. The derivative files
hold no beamformer filters, but each virtual sensor is an exact linear combination of the scalp
channels, so the filters were recovered and applied to the incorrect trials. The attempt record, with the reasons and the differences from the paper's
method, is [`attempts/openneuro-ds004752-dimakopoulos-2022-01.yaml`](../../attempts/openneuro-ds004752-dimakopoulos-2022-01.yaml).

- `reproduce_dimakopoulos_2022.ipynb`: the analysis. It takes about 26 minutes, most of it Granger
  causality permutations and about 2.5 GB of streaming.
- `wmflow.py`: streaming the snapshot's files (EDF by byte range, the derivative MAT files), the
  hippocampal readings, spectral Granger causality with Wilson factorisation, PSD and PLV, and the
  permutation tests. Other notebooks on this dataset can import it.
