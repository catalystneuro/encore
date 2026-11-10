# Alasfour & Gilja (2024) from dandiset 000055 (AJILE12)

Tests the findings of [Alasfour and Gilja (2024)](https://doi.org/10.3389/fnhum.2024.1388267) on
[DANDI:000055](https://dandiarchive.org/dandiset/000055/0.220127.0436), which holds the ECoG, electrode
positions and annotated behaviour blocks of the paper's five participants (AJILE12 participants 01,
02, 04, 05 and 08). The electrode-to-ROI projection matrices come from
[Figshare](https://doi.org/10.6084/m9.figshare.12114408.v1).

| Claim | Outcome |
|---|---|
| The projection matrices belong to the dataset's electrodes (link) | Partially reproduced |
| Five of twelve participants have at least 1 h of each behaviour | Reproduced |
| Table 1: good electrodes and minutes per behaviour | Not reproduced |
| Figure 2: highest accuracy, significant bands per ROI (five claims) | Reproduced, resting on the readings |
| Two-way ANOVA: ROI and band effects, no interaction | Reproduced |
| Band and ROI averages | Reproduced, resting on the readings |
| Three-class decoding | Partially reproduced |
| Figure 4: every participant above chance | Reproduced, resting on the reading |
| Figure 4: missing ROIs; participant 2 highest | Partially reproduced |
| Figure 5: gamma higher, theta and alpha lower when talking; pre- and postcentral largest | Reproduced, resting on the readings |
| Figure 5: no gamma in parietal and superior temporal ROIs; middle temporal 4 of 5 bands | Partially reproduced |
| Inferior temporal high gamma decodes without a consistent mean difference | Reproduced |
| Every ROI but the inferior parietal has a consistent band | Reproduced, resting on the readings |
| Figure 6: 9 of 40 combinations share a sign | Reproduced, resting on the readings |
| Figure 6: the six named combinations | Partially reproduced |
| Figure 7: not additive; above group level | Reproduced (not additive resting on the reading) |
| Figure 7: participant 4 low gamma, above 70%, best bands; above 80% regularly | Partially reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper links no code, and many details are open (chance level, artifact rule, ROI assignment, ROI
feature, buffer). Every analysis runs under the grid of readings the claims file names; its criteria
accept a match under one reading, and many matches hold in a small share of them. The notebook gives,
for each claim, the result under the main reading and how many readings meet the criterion. The epochs
of two files are on a clock 8.5 h ahead of their ECoG; the offset is applied, and for sub-04 ses-3 the
alignment could not be confirmed. The attempt record is
[`attempts/alasfour-2024-01.yaml`](../../attempts/alasfour-2024-01.yaml).

- `reproduce_alasfour_2024.ipynb`: the analysis. It takes about 21 minutes, 16 of them streaming
  89 GB of the ECoG (only the labelled blocks and the good electrodes) in four processes.
- `ajile.py`: listing and streaming the files (with a parallel reader of the HDF5 chunk index),
  band envelopes in 10-s bins, the artifact rule, ROI assignment from the projection matrices, the
  cross-validated LDA and the finite chance level. Other notebooks on this dandiset can import it.
