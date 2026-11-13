# Temmar et al. (2025), LINK, from dandiset 001201

Tests the findings of [Temmar et al. (2025)](https://doi.org/10.52202/085713-4642) on
[DANDI:001201](https://dandiarchive.org/dandiset/001201/0.261026.1912), which holds 312 sessions of
spiking-band power (SBP), threshold crossings and the kinematics of two finger groups from Monkey N,
recorded on 303 days over 3.5 years.

| Notebook | Claims |
|---|---|
| `signals.ipynb` | dataset counts and contents, throughput, SBP decline, active channels, participation ratio, bank and activity slopes, population drift, trajectories, tuning (Figures 2, 3, S2, S4, S5) |
| `decoding.ipynb` | same-day and cross-day decoding with ridge regression and an LSTM, the shuffle baseline, irregular SBP shifts (Figure 4, Appendix C.1) |
| `multiday.ipynb` | multi-day training (Figure 5A) |
| `window.ipynb` | the LSTM part of the irregular SBP shifts claim, on 27 of the 45 sessions of July to November 2022 |

The LSTM is trained on 20 of the 312 sessions, on the 12 other sessions with the highest ridge
regression R2 (for the claim that it beats ridge regression on every day, and as variants of two
others), and on 24 more sessions of July to November 2022, and the multi-day comparison on 12 of 283 day-0 sessions, for time; the
continual fine-tuning of Figure 5B is too large to run here. The outcomes, the reasons and
the differences from the paper's method are in the attempt record,
[`attempts/temmar-2025-01.yaml`](../../attempts/temmar-2025-01.yaml).

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and
the differences from the paper's method.
