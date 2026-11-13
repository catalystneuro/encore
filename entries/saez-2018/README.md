# Saez et al. (2018) from CRCNS ofc-3

Tests the findings of [Saez et al. (2018)](https://doi.org/10.1016/j.cub.2018.07.045) that can be
tested on [CRCNS ofc-3](https://doi.org/10.6080/K0VM49GF), which holds high-frequency activity (HFA)
epochs from 191 unique orbitofrontal electrodes in 10 epilepsy patients playing a gambling task, with
their behaviour and the authors' regressors. The broadband signal, the electrode locations and the
healthy participants' data are not in the data set.

| Claim | Outcome |
|---|---|
| Electrode, patient and timeout counts | Partially reproduced |
| Patients gamble on about 56% of trials | Reproduced |
| Gambling rises with win probability and with gamble expected value | Reproduced (2 claims) |
| Patients' choices like healthy participants' | Blocked: data missing |
| Longer reaction times in high-conflict trials | Not reproduced |
| Past and current regressors uncorrelated (mean R2 2.1%, max 3.7%) | Not reproduced |
| Regressors weakly correlated (mean R2 0.15) | Reproduced |
| HFA encodes choice and outcome regressors (counts of Table S2) | Not reproduced |
| Choice and outcome encoding delays and durations similar | Reproduced (assumption) |
| HFA encodes the previous trial | Partially reproduced (assumption) |
| Past signals more sustained | Partially reproduced (assumption) |
| Past trials do not affect choice | Not reproduced |
| Encoding limited to the previous trial | Reproduced |
| Sharp boundary between t-1 and t-2 | Reproduced (assumption) |
| All regressors significant in mixed-effects models | Reproduced (assumption) |
| Stepwise selection similar to the 5-window selection | Partially reproduced (assumption) |
| Risk over all trials explains more variance than over gamble trials | Not reproduced |
| No encoding of response direction | Reproduced |
| All signals in at least 6 patients (mean 7.41) | Not reproduced |
| Multiplexing and present-past overlap (Figures 7F, S7) | Not reproduced (2 claims) |
| Example risk and regret electrodes | Reproduced |
| Broadband comparisons (2 claims) and anatomy (3 claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The HFA is used as deposited, already baseline-corrected, as the authors' own correction; the claims
file's two baseline readings are run as well. They change the outcomes of four claims (past encoding,
past signals more sustained, sharp boundary, stepwise selection), which are marked as resting on that
assumption. The mixed-effects claim passes under reading (a), with one model per window, and rests
on that reading. The latency claim rests on a different assumption, the timing of the second epoch. The data set's "buttonpress" epoch behaves as locked to the outcome reveal, seven electrodes of s03
are deposited twice, and the HFA trials carry no round number (they are matched to rounds through the
authors' regressor file). The attempt record, with the reasons and the differences from the paper's
method, is [`attempts/saez-2018-01.yaml`](../../attempts/saez-2018-01.yaml).
