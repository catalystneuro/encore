# Mayner, Marshall, Billeh et al. (2022) from dandiset 000036

Tests the findings of [Mayner et al. (2022)](https://doi.org/10.1523/eneuro.0280-21.2021) that
can be tested on [DANDI:000036](https://dandiarchive.org/dandiset/000036/0.230515.1917), which
holds the two-photon dF/F, running velocity and movie stimuli of the OpenScope differentiation
experiment: 57 sessions from 9 mice, of which the paper analysed 44.

| Claim | Outcome |
|---|---|
| The dandiset's sessions link to the paper's 44 (link claim) | Reproduced |
| 45 sessions in 9 mice, 15 per Cre line, 9 per area | Partially reproduced |
| 4018 cells (1683 L2/3, 1781 L4, 554 L5) | Reproduced |
| Unscrambled > scrambled ND specifically in L2/3 (Fig. 3A) | Reproduced |
| ... specifically in AL and AM (Fig. 3B) | Reproduced |
| Natural > artificial over all 12 stimuli (Ext. Fig. 3-1) | Reproduced |
| Specificity holds for nearly all ND parameters (Ext. Figs. 3-2 to 3-4) | Not reproduced |
| Per-session permutation tests (Table 1) | Reproduced |
| Effect size correlates with locomotion (Fig. 4) | Reproduced |
| Session effect sizes 0.57 to 1.25, pooled 0.34 (Discussion) | Partially reproduced |
| Multivariate ND specific to L2/3 and to AL and AM (Fig. 5) | Reproduced (2 claims) |
| Category and identity decoding high in most populations (Fig. 6, Ext. Fig. 6-1) | Reproduced (2 claims) |
| ND differs among natural clips; snake highest (Fig. 7) | Reproduced (2 claims) |
| ND correlates with stimulus differentiation, driven by noise (Fig. 8) | Reproduced (2 claims) |
| No relation to luminance, contrast or spectral energy (Ext. Fig. 8-1) | Blocked: methods underspecified |
| Effect size and pupil diameter (Fig. 4) | Blocked: methods underspecified |
| Claims on L0 events (Ext. Figs. 1-3, 3-8, 3-9, 5-1, mediation) | Blocked: not runnable |
| Arousal covariates and arousal mediation (Ext. Figs. 3-5 to 3-7, 7-1) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The dandiset does not say which of its sessions the paper used. They are found through the
paper's code output (`results/main.parquet` at commit 2d959bd), matched on mouse and start time;
the dF/F is the paper's, trial by trial. The not-reproduced claim fails under the claims file's
reading of "nearly all", which the paper's own outputs do not meet either. The attempt record,
with the reasons and the differences from the paper's method, is
[`attempts/000036-mayner-2022-01.yaml`](../../attempts/000036-mayner-2022-01.yaml).

- `reproduce_mayner_2022.ipynb`: the data check, the session link and most claims (about 12
  minutes).
- `multivariate_mayner_2022.ipynb`: the UMAP claims of Figure 5 (about 12 minutes).
- `arousal_mayner_2022.ipynb`: the running and pupil claims of Figure 4, with the paper's Zenodo
  deposit streamed in memory for the running artifact parameters, sync alignment and pupil area
  (about 20 minutes, most of it waiting for the deposit, which can only be read in order).
- `openscope_nd.py`: loading, the ND measure, decoding, the mixed models and post hoc tests, and
  the paper's artifact removal. Other notebooks on this dandiset can import it.
