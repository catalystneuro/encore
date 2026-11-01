## Report: DANDI:000897, Neupane, Fiete & Jazayeri (2024)

All five author steps and the handover (step 6) are done. The entry is `entries/000897-neupane-2024/` and the record is `attempts/000897-neupane-2024-01.yaml`. It is pinned to version 0.240605.1710, the only published version; the paper links the dandiset without a version. `entry.py all` passed with 0 errors and the notebook ran in about 17 minutes. Nothing was committed.

**(1) Outcomes**

| Claim | Outcome |
|---|---|
| fig1bc-produced-matches-actual | reproduced |
| fig1e-immediate-generalization | blocked: data_missing |
| fig2-periodic-proportion | not_reproduced (assumed) |
| fig2d-periodicity-at-065 | partially_reproduced (assumed) |
| ed3-no-eye-hand-periodicity | reproduced (monkey A only) |
| ed2b-pi-navigation-above-iti | blocked: metadata_insufficient |
| ed2c-pi-error-below-correct | partially_reproduced (assumed) |
| fig2e-first-peak-near-065 | partially_reproduced |
| fig2f-earlier-peaks-multiples | partially_reproduced |
| ed4d-overshoot-longer-period | partially_reproduced |
| fig3b-onset-and-offset-coding | reproduced |
| fig3d-offset-coding-stronger | partially_reproduced |
| ed4e-rate-codes-distance-over-slope | not_reproduced |
| ed4fg-distance-over-landmark | partially_reproduced |
| fig3e, ed5, ed5efg | blocked: metadata_insufficient (ed5 and ed5efg depend on fig3e) |
| fig4h-periodic-fano-factor | partially_reproduced (assumed) |
| ed8-fano-periodic-without-rate-periodicity | reproduced |
| ed10-motor-preparation-signal | partially_reproduced |
| fig4g, fig4b, fig4d, ed6d | blocked: other (not attempted in the time; three are model simulations) |

**(2) The dataset, assumptions and questions**

What the dataset holds:
- **Only part of the data.** It has 15 of the paper's 32 sessions (monkey A 6, monkey M 9), with 1,093 units against the paper's 1,478. 103 monkey A units are labelled noise.
- **An undescribed sequence.** In monkey M, `seqq` 3 trials use vectors in 0.975 s steps, which the paper does not describe.
- **Eye and joystick clocks.** In 10 of the 15 sessions, the eye and joystick timestamps are on a different clock from the trials.
- **Three sessions with no evidence of a shared clock.** In A 09172019, M 04132021 and M 04142021, no unit's rate changes around joystick offset. In M 04132021 the spikes also stop halfway through the session.
- **No inter-trial interval.** It is not marked in the files: trial rows run back to back. So the ITI segments longer than 4 s that ed2b and fig3e use cannot be found.
- **Undocumented columns.** Unit labels differ between the monkeys, and several unit columns have no description.

Assumptions, each recorded as a deviation:
- **The null for the periodicity index.** The Methods do not say how the Gaussian-process null becomes a firing rate. I used rate = r·exp(g − ½), with r the median unit rate.
- **Which units count as periodic.** The classification rule is open, and I adopted the code's score compared with the same score on the surrogates. The readings disagree widely: the Methods' rule makes 58–81% of units periodic, against 8–24% for the adopted one.
- **Units for ed2c.** I took the code's selection (periodicity index at 650 ms above threshold).
- **Units of the 0.05 trial-rate threshold.** Read as spikes/s.
- **End of the Fano time course.** Taken as 500 ms before the shortest trial's offset.

Two `methods_unavailable` findings put these questions to the paper's authors. Because the dataset is a subset, counts are compared as proportions of the units it holds. I asked a reader nothing.

**(3) Where the protocol was unclear**
1. Expected counts cannot match when the dataset holds only part of the sessions, and the protocol does not say what to do. I compared proportions with the same 10% relative tolerance, recorded the raw counts as `measured`, and stated this as a deviation.
2. There is no blocked reason for "not attempted within the time limit". `too_large` covers only a computation that stopped, so I used `other` and said so in the notes.
3. For model-simulation claims that use no recorded data, the protocol gives no `data` category or blocked reason. I used `other`.
4. `measured` must be one number when several readings or groups each give one. I recorded the pooled median and said so in the notes.
5. The clock check suggests decoding, but a session where no unit responds at all cannot be told apart from a session whose clock is shifted. I recorded those three sessions as "not established".

**(4) Runtime and failures**

The run took from 17:13 to about 20:14 UTC. One `grep -o` on the single-line paper text hung for the full 60-minute timeout and cost an hour. During development the notebook had small bugs, all fixed; the final run executed cleanly, and its numbers match the conclusions.
