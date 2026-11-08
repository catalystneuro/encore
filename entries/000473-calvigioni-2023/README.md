# Calvigioni, Fuzik, Le Merre et al. (2023) from dandiset 000473

Tests the findings of [Calvigioni et al. (2023)](https://doi.org/10.1038/s41593-023-01367-8) that can be
tested on [DANDI:000473](https://dandiarchive.org/dandiset/000473/0.230417.1502), which holds Neuropixels
recordings in the mPFC of 25 head-fixed mice (Fig. 4 and Extended Data Figs. 7 to 9). The ex vivo, anatomy,
behavior and pupil data of the paper are not in it.

| Claim | Outcome |
|---|---|
| Sessions and units link to the paper's code outputs | Partially reproduced (assumption) |
| 4,152 units in ACAd, PL, ILA and ORBm | Reproduced |
| 1,945 units fitted with the GLM | Reproduced (assumption) |
| Light modulates mPFC units in Vglut2 and Esr1, not Npy mice; sound and air puff in all | Partially reproduced (assumption) |
| Mean opto tuning score above controls in Vglut2 and Esr1 | Not reproduced (assumption) |
| Counts of opto-tuned units per genotype | Partially reproduced (assumption) |
| Narrow- and wide-spiking classes, both opto-tuned | Reproduced |
| Units comodulated by light and air puff above chance | Reproduced |
| Similar response latency to tone and air puff | Reproduced (assumption) |
| Conditioned units in Vglut2 and Esr1 mice | Reproduced |
| Block-2 trajectories diverge in Vglut2 and Esr1 | Reproduced |
| Opto clusters from Vglut2 and Esr1 mice | Partially reproduced |
| State clusters | Reproduced |
| Activity modes | Reproduced |
| PL baseline decodes block 1 vs 2 better in Vglut2 and Esr1 | Reproduced |
| No genotype difference in decoding elsewhere | Not reproduced |
| Esr1 effects concentrated in PL, Vglut2 spread | Reproduced |
| Pupil, eye-closing and optotagging claims (4) | Blocked: data missing |
| Ex vivo, anatomy and behavior claims (11) | Blocked: data missing |
| Patch-seq markers (BioStudies) | Blocked: metadata insufficient |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Several outcomes rest on the period over which the GLM was fitted, which the paper does not state; the
paper's code outputs match a fit over blocks 1 to 4. Several counts of tuned units depend on the random
shifts of the GLM, so the notebook shows them over ten seeds. The attempt record, with the reasons, the
differences from the paper's method and the findings about the dataset, is
[`attempts/000473-calvigioni-2023-01.yaml`](../../attempts/000473-calvigioni-2023-01.yaml).

- `reproduce_calvigioni_2023.ipynb`: the analysis. It takes about 13 minutes, most of it the decoding and the GLM.
- `esr1npx.py`: streaming the files, the unit selection, the GLM tuning scores (closed-form Poisson fit with
  circular shifts) and trial-aligned rates. Other notebooks on this dandiset can import it.
