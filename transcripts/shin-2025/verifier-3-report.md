**Verifier report, round 3: 000248-shin-2025-01**

The claims file has 40 claims, and the attempt record has 40 outcomes: 14 reproduced, 1 partially reproduced, 3 not reproduced and 22 blocked. Two outcomes carry a `proposed` change, and these are the only ones reviewed here.

| Claim | Recorded outcome | Proposed outcome | Agree? | My outcome if different | Reason |
|---|---|---|---|---|---|
| fig2d-npx-ccg-hva-input | reproduced (`assumed`) | blocked (methods_underspecified) | yes | | See the fig2d paragraph below. |
| fig3d-npx-areas-inference | partially_reproduced (`assumed`) | reproduced | yes, with a reservation | | See the fig3d paragraph below. |

**fig2d.** Reproduce cell 53 applies the criterion as written. A combination meets it when IC-encoders have a strictly higher median and the tie-corrected rank-sum p is below 0.05. Seven of the eight combinations meet it. The one that does not is boxcar smoothing with the raw flank, measured as number of connections, where the medians are 1 and 1 (p = 9.8e-05). The criterion sends readings that differ to blocked (methods_underspecified), so the proposal follows it.

The values in cell 53 come from the cell 51 table, which is computed from the data:
- The groups hold 79 IC-encoders and 526 segment responders, the paper's counts.
- P(IC-encoder > segment responder) is 0.62 to 0.64.
- Tie-corrected p runs from 1.0e-05 to 3.9e-04.

No choice was made to reach the result: the eight combinations and the strict median rule come from the claims file. This settles the round 1 and round 2 point. The substance still supports the paper's direction under every combination, and the record says so.

**fig3d, the checks.** The proposed numbers match the notebooks:
- Seed +100000 (seed1 cell 8): five areas are significant, V1, LM, RL, AL and PM. PM p = 0.0425 and AM p = 0.083. The three largest scores are LM, V1 and AL.
- Seed +200000 (seed2 cell 8): five areas are significant, V1, LM, RL, AL and AM. AM p = 0.0186 and PM p = 0.052. The three largest scores are LM, V1 and AL.
- First seed, reading (b) (decoding cell 14): four areas are significant. PM p = 0.077 and AM p = 0.083.
- Reading (a) (decoding cell 14, checks cell 8): five areas are significant with all three seeds, V1, LM, RL, AL and AM, and V1, LM and AL are the three largest.

So the criterion is met in 5 of 6 runs. The scores are derived correctly: the score is P(TRE→IC) − P(TRE→LC) (`illusion.py:583`), tested with a two-sided signed-rank test against 0. The session counts are 12, 8, 11, 10, 12 and 11, as in the paper. The seed runs use the same jobs and seeds offset by k·100000, and every fit converged.

**fig3d, why I agree.** The partition seed is random cross-validation noise, not a method choice, and the further seeds answer my round-2 point 2. Part of the result is stable across all six runs:
- V1, LM, RL and AL are significant every time.
- LM, V1 and AL are always the three largest.

Only the fifth area changes, and it sits near the threshold either way: PM p is 0.0425 to 0.092 and AM p is 0.0020 to 0.083.

**fig3d, the reservation.** Deciding by the majority of seeds is a rule added after the first-seed result, and it is not in the criterion. A rule requiring every seed under reading (b) would keep the claim partial. The rule should be recorded as an assumption in the fig3d deviations. Right now it appears only in the `proposed` reason and in decoding cell 15. Averaging per-session scores over seeds would be a more principled rule, but it was not computed.

The statement's specific pattern, PM significant and AM not, appears in only 1 of the 6 runs. Under reading (a), AM is significant and PM is not with every seed. The criterion counts significant areas and does not name them, so this does not decide the outcome, and the record states it. The claims file's fig3d criterion still does not say which decoder reading decides; I reported that in rounds 1 and 2.

**Stale statement found in passing.** Checks cell 16 still gives "4.4 ms per epoch … about 18 hours". The output of the cell before it, as quoted in my round-2 report, shows 3.60 ms and about 15 h. This is outside the two proposals and does not change any outcome.
