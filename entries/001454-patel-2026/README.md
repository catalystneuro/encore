# Patel, Kim et al. (2026) from dandiset 001454

Tests the findings of [Patel, Kim et al. (2026)](https://doi.org/10.1038/s41593-026-02413-x) that can be
tested on [DANDI:001454](https://dandiarchive.org/dandiset/001454/0.260911.2319), which holds the ex vivo
current clamp recordings of BLA neurons (Figure 2, Extended Data Figs. 2 and 3), calcium imaging of BLA and
mPFC neurons in the cued two-bottle choice (Figures 3, 5 and 6) and mPFC imaging in the resident-intruder
task. `ephys_patel_2026.ipynb` holds the patch-clamp claims, `imaging_patel_2026.ipynb` the imaging claims.

| Claims | Outcome |
|---|---|
| Isolation raises male BLA-mPFC excitability (Fig. 2c) | Not reproduced (no Sidak step with the 21 neurons of the 2022 cohort) |
| Group-housed females more excitable than males (Fig. 2e) | Reproduced |
| Isolation raises male input resistance (Supplementary Table 1) | Not reproduced (p = 0.052) |
| Nonspecific BLA: small isolation effect, no rank effect (Extended Data Fig. 2) | Reproduced (2 claims) |
| Male rank 1 less excitable than ranks 2 and 3 (Extended Data Fig. 3c) | Partially reproduced |
| No rank effect in females (Extended Data Fig. 3d) | Reproduced |
| Isolated females (Fig. 2d, three-way ANOVA, female Supplementary Table 1) | Blocked: 11 of 14 files hold only a flat secondary channel |
| BLA imaging: nonoverlapping ensembles, no correlation of nonspecific or water responses, bout duration | Reproduced (3 claims) |
| BLA imaging: cue response, clusters, BLA-mPFC response predicts bouts, no cue correlation | Not reproduced (4 claims) |
| Decoding of alcohol against water (Fig. 3h, Extended Data Fig. 6b) | Blocked: too few bouts per mouse (3 claims) |
| mPFC: isolation and stimulation effects on alcohol and sucrose responses (Figs. 5b, 5d, 6c to 6f, 6k, 6l,m, Extended Data Fig. 8n) | Not reproduced (8 claims) |
| mPFC: absence of water and isolation-sucrose effects (Figs. 5c, 6g to 6j, 6n, Extended Data Fig. 8o,p) | Reproduced (4 claims) |
| Home-cage drinking, ranks, blood alcohol, optogenetic behaviour, stability and resident-intruder imaging analyses | Blocked (28 data missing, 1 not runnable) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The imaging files hold every CNMF-E ROI, not the paper's curated neurons, and do not say which BLA cohort
is projection-specific (cohorts are assigned by their mouse counts). Three pairs of imaging files hold
identical traces, the cue schedule is the same in every session, and in many sessions the forced trial
types 1 and 2 are swapped against the licks. Cohort 9 traces are nonnegative and smooth between
transients, so the paper's z-score against a 3-s baseline is not defined on them; cohort 9 is left out of
the BLA z-scores, with the other readings shown. The attempt record, with the reasons and the differences from the paper's
method, is [`attempts/001454-patel-2026-01.yaml`](../../attempts/001454-patel-2026-01.yaml).
