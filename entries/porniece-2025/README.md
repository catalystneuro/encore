# Porniece, Baker, Ausfahl, Zhang & Andermann (2025) from dandiset 001474

Tests the findings of [Porniece et al. (2025)](https://doi.org/10.1038/s41598-025-19800-2) on
[DANDI:001474](https://dandiarchive.org/dandiset/001474/0.251031.1725), which holds the fiber
photometry of PVH MC4R neurons, with licking, running and Ensure delivery, in head-fixed NCD and HFD
mice: cohort 1 (60-trial sessions, Fig. 1), cohort 2 (90-trial sessions, Fig. 2) and the diet-switch
recordings of the same mice (Fig. 3).

| Claim | Outcome |
|---|---|
| Fig. 1k, early and late responses per recording | Partially reproduced |
| Fig. 1k, LME: HFD early above NCD early, diet by phase interaction | Not reproduced |
| Fig. 1l, early and late responses per mouse | Partially reproduced |
| Supp. Fig. 1i, no HFD change with a 1-20 s window | Reproduced |
| Supp. Fig. 1h, HFD dF/F responses higher early and persisting | Reproduced |
| Fig. 1g, h, HFD mice consume less Ensure | Reproduced |
| Fig. 1c, HFD mice about 30% heavier | Partially reproduced |
| Supp. Fig. 1c, d, licking declines in both diets | Blocked: methods underspecified |
| Supp. Fig. 1e, HFD locomotion negligible and falling | Reproduced |
| Fig. 2b, meal size 70.1 against 52.9 trials | Reproduced |
| Fig. 2c, delta Z-score per recording | Reproduced (assumption) |
| Fig. 2d, delta Z-score per mouse | Reproduced |
| Fig. 2e, NCD lick more; onsets of decline at about 50 and 20 trials | Partially reproduced |
| Fig. 2f-j, initial lick rates by meal size | Reproduced |
| Fig. 2p, mid-meal lick rate correlates with meal size | Reproduced |
| Fig. 2g, h, l, m, higher HFD early responses at matched licking | Reproduced |
| Fig. 2q, HFD mid-meal response against meal size, r = -0.46 | Reproduced |
| Fig. 2r, HFD body weight against mid-meal response | Reproduced |
| Fig. 2s, HFD body weight against meal length | Reproduced |
| Supp. Fig. 2a, Ensure volume against triggered trials | Reproduced |
| Supp. Fig. 2h, delta Z-score against meal size | Not reproduced |
| Supp. Fig. 2f, g, locomotion lower in HFD, not related to meal size | Reproduced |
| Supp. Fig. 2j, weak correlation of variability with body weight | Reproduced |
| Supp. Fig. 2k, females larger early responses, more in HFD | Reproduced |
| Supp. Fig. 2l-p, fasting has no effect | Not reproduced |
| Supp. Fig. 2q, HFD mice need more training | Blocked: data missing |
| Fig. 3h, early responses after switching from HFD to NCD | Partially reproduced |
| Fig. 3i, early-late increase in NCD->NCD only | Reproduced |
| Fig. 3j, delta Z-score after the switch | Not reproduced |
| Fig. 3k, Ensure after the switch | Reproduced |
| Fig. 3, HFD->HFD never above 60 triggered trials | Not reproduced |
| Fig. 3c, licking recovers in HFD->NCD | Reproduced |
| Supp. Fig. 3c, NCD->HFD6w keep their response dynamics | Reproduced |
| Supp. Fig. 3j, body weight after the switch | Reproduced |
| Supp. Fig. 3m, mid-meal response against weight gain | Partially reproduced (assumption) |
| Supp. Fig. 3l, body weight does not predict meal length | Reproduced |
| Supp. Fig. 3q, HFD->NCD meal length against weight change | Partially reproduced (assumption) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper's Z-score could not be rebuilt exactly. The claims file's two readings of the Methods
are computed here from the deposited raw trace; the depositors' own Z-score is shown as a variant,
and under it the Fig. 1k mixed model reproduces. The dataset lacks one of the seven cohort-2 HFD
mice, holds four files twice, and in 32 files has a Z-score that does not match its own raw trace. In
those 32 files and the 26 without a Z-score, the trial starts in the raw trace are taken from the
other files. A check on the tone-evoked response supports them as a group; it cannot place 9 of
them, which show no tone response. Without these 58 recordings every outcome is the same except
Fig. 2c, which would be partially reproduced, so its outcome is marked as assumed.
The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/porniece-2025-01.yaml`](../../attempts/porniece-2025-01.yaml).

- `reproduce_porniece_2025.ipynb`: the analysis. It takes about two minutes, most of it reading the
  files.
- `pvh.py`: loading the files and the trial measures (windows, Z readings, early and late meal
  values). Other notebooks on this dandiset can import it.
