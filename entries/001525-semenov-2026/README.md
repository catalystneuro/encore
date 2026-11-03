# Semenov et al. (2026) from dandiset 001525

Tests the findings of [Semenov et al. (2026)](https://doi.org/10.1016/j.bioelechem.2026.109283)
that can be tested on [DANDI:001525](https://dandiarchive.org/dandiset/001525/0.261006.1856),
which holds the two-pulse strobe imaging of ten Di-8-ANEPPS-loaded CHO cells (the experiment of
Fig. 7A and the bottom panel of Fig. 7B). The other experiments of the paper are not in it.

| Claim | Outcome |
|---|---|
| After conditioning up to 1000 V/cm the test-pulse profile still follows a cosine; 1200 and 1400 V/cm hinder pole charging | Reproduced, resting on assumptions |
| Test-pulse polarization does not differ from control up to 760 V/cm, about 80% after 1000 V/cm | Reproduced, resting on assumptions |
| 1200 and 1400 V/cm conditioning reduce the test response to about 70% and 50% | Partially reproduced, resting on assumptions (significant; values outside tolerance) |
| Full reseal after 570 and 760 V/cm, residual conductivity after stronger pulses, no pole difference at the test pulse | Partially reproduced, resting on assumptions (the during-pulse part is not testable) |
| Eq. (2): a 10-fold conductivity rise lowers IMP by about 2%, a 100-fold rise by 12% | Partially reproduced |
| Conditioning-pulse polarization below linear scaling, and the 10-fold conductivity drop of Fig. 7C (2 claims) | Blocked: data missing |
| Figures 1 to 6 (20 claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The files give pulses in generator volts; the conditioning strengths are mapped to the paper's
V/cm by rank, and the single 50 V pulse stands for the paper's 150/150 benchmark. The membrane trace is
found automatically; the outcomes of the first three claims depend on how (see the notebook). The record, with
the reasons and the differences from the paper's method, is
[`attempts/001525-semenov-2026-01.yaml`](../../attempts/001525-semenov-2026-01.yaml).
