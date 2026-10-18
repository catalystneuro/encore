# Mah, Schiereck, Bossio & Constantinople (2023) from dandiset 001169

Tests the findings of [Mah et al. (2023)](https://doi.org/10.1038/s41467-023-43250-x) on
[DANDI:001169](https://dandiarchive.org/dandiset/001169/0.260825.1909), which holds 23,034
behavioral sessions of 291 rats in a temporal wagering task with hidden reward blocks. The
paper has no neural data.

| Claim | Outcome |
|---|---|
| 291 rats, 184 male and 107 female; median 71 sessions and 33,493 trials | Reproduced |
| The dandiset holds the paper's processed data on Zenodo | Partially reproduced (9 sessions missing, 10 rats in another order) |
| Rats wait about 10% less for 20 uL in high than in low blocks | Reproduced |
| Rats initiate trials faster in high than in low blocks | Reproduced |
| Block effects on initiation times come mostly after unrewarded trials | Reproduced |
| No difference between males and females | Reproduced |
| Wait times converge in mixed blocks whatever the previous block | Reproduced |
| Initiation times in mixed blocks depend on the previous block | Reproduced (corrected criterion; see below) |
| Regression kernels: wait times on the current reward, initiation times on previous rewards | Reproduced |
| Time constants differ, and are not correlated | Reproduced |
| Fast and slow initiation-time rats differ in initiation but not wait time kernels | Reproduced |
| Previous offer: no effect on wait times (38 rats), an effect on initiation times (256 rats) | Reproduced |
| Graded effect of catch probability; cohort sizes | Reproduced |
| The inferential model fits wait times better than the retrospective model (BIC) | Reproduced |
| Wait times follow the model's mistaken inferences | Reproduced |
| Quality of inference separates wait time, not initiation time, dynamics | Reproduced (weakly) |
| A dynamic learning rate is needed for initiation time dynamics | Blocked: methods underspecified |
| Training: wait time ratio falls gradually, initiation ratio below 1 at once (Zenodo data) | Partially reproduced |
| Training: wait time coefficients grow, initiation coefficient stable (Zenodo data) | Reproduced |
| Training: overshoot grows (Zenodo data) | Not reproduced |
| Pre-initiation cue: initiation times follow the offer, the previous reward and the previous block | Reproduced, reproduced (fragile), reproduced (corrected criterion) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The criteria of the two claims on the dependence of initiation times on the previous block first
assumed that the dependence keeps its sign after the switch. The data show a strong dependence with
the sign reversed, which is the overshoot after high-to-mixed transitions that the paper describes.
After the first verification round the criteria were corrected to that sign, with the first versions
shown as variants. The overshoot over training (Figure 4d and 4e) was first blocked; it is now tested
on the Zenodo structs of all final-stage sessions, and it does not grow by this attempt's tests.
The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/001169-mah-2023-01.yaml`](../../attempts/001169-mah-2023-01.yaml).

- `reproduce_mah_2023.ipynb`: the analysis of the dandiset, and its comparison with the paper's
  structs on Zenodo. It takes about 15 minutes: 9 to read the files, 6 to fit the models.
- `reproduce_mah_2023_fig4.ipynb`: the training claims of Figure 4, including the overshoot, on the structs of all
  final-stage sessions that the paper deposited on Zenodo, which the dandiset does not hold.
  About 3 minutes.
- `wagering.py`: loading, the per-rat measures of the paper's code, the wait time models, and
  reading the Zenodo structs. Other notebooks on this dandiset can import it.
