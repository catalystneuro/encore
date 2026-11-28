**Verifier report, round 2: Alonso & Marder 2020 (doi:10.7554/elife.55470), Dryad m31b1h7 v94811**

The claims file has 23 claims and the attempt record gives 23 outcomes: 8 reproduced, 5 partially reproduced, 7 not reproduced and 3 blocked. Cell numbers below refer to `reproduce_alonso_2020.ipynb` unless a notebook is named. The cells have been renumbered since round 1, so deposit-models is now cell 14, not 12.

**1. Outcomes**

I agree with 21 outcomes and accept one more with a caveat. I now question fig6s1, which I accepted in round 1.

| Claim | Outcome | Agree? | Assumption stated and reasonable? |
|---|---|---|---|
| deposit-models | not_reproduced | Yes (cell 14: 3 of 38) | n/a |
| fig1c-frequency-q10-phase-constant | partial | Yes (cell 20) | n/a |
| fig1s1-three-models | not_reproduced | Yes (cell 23) | n/a |
| all-models-compensated | partial | Yes (cell 26: 36 of 38, 35 with the strict order test) | Yes. The order test is stated, and the variant also gives a partial outcome. |
| intermediate-temperature-failures | blocked (data_missing) | Yes (cell 32) | n/a |
| figs2-ramp-largest-isi | reproduced | Yes (ramps cell 5) | n/a |
| figs3-duty-cycle-variable-across-models | reproduced (variant reading) | Yes, on the variant the criterion names | n/a |
| fig2-lp-spike-amplitude-threshold | reproduced | Yes as the criterion is written (voltage cell 5) | Stated, but weakly supported; see below. |
| fig2s1-peak-voltage-diverse | reproduced | Yes (voltage cell 8) | n/a |
| fig3-current-amplitudes | partial | Yes (cell 35) | n/a |
| fig4-currentscapes-reorganize | not_reproduced | Yes (cell 38: no part holds under any of the 4 readings) | n/a |
| currentscapes-dominant-currents | reproduced | Yes (cell 41) | n/a |
| fig5-a-to-kca-tradeoff | reproduced | Yes (cell 44) | n/a |
| fig6-crash-different-mechanisms | not_reproduced | Yes (cell 50: FGFKQS PD fires 1005 spikes; still 336 at 0 mV, cell 71) | Yes |
| fig6s1-crash-mechanisms | not_reproduced | Questioned; see below | Yes |
| fig7-high-temperature-slow-timescales | blocked (data_missing) | Yes (cell 56) | n/a |
| fig8a-hysteresis-quiescence | reproduced | Yes (ramps cell 8: 1.94 °C) | n/a |
| fig8-up-down-ramps | blocked (too_large) | Accepted with a caveat; see below | n/a |
| fig8b-pathological-attractor | not_reproduced | Yes (ramps cell 15) | Yes |
| fig9a-remove-a-current | partial | Yes (cell 59) | Yes |
| fig9b-remove-kca-current | reproduced | Yes (cell 62) | Yes |
| fig10a-graded-removal | partial | Yes (cell 65: 4 of 5 with control first, 3 of 5 from t = 0) | Yes. Control first is the Results' Figure 9 protocol and the deposit's removal script. |
| fig10b-complete-removal-differs | not_reproduced | Yes (cell 68: H gives 30 or 31, against 33) | Yes |

- **fig2 threshold reading (b).** The criterion is met, but the rule the author chose for reading (b) is open to doubt:
  - The direct per-spike threshold (reading a) does not move: −27.8 to −27.5 mV, ρ = −0.197.
  - Reading (b) sits 8 to 10 mV below that threshold (−36.1 mV at 10 °C).
  - LP fires 114 spikes at 10 °C and 433 at 25 °C. More spikes put more occupancy just above the dense region, which would push this "edge" upward even if the threshold did not change. At 2% the rule reaches the −20 mV search limit at 24.4 and 25 °C.

  The outcome should be read as resting on this rule.
- **fig6s1.** Reproduced is ruled out, because B7SD0L, J9U8SQ and SJR46Y share a pattern (cell 53). Partial is not ruled out: it needs six distinct patterns among eight and every model crashing. The 7 models present give 5 patterns, so the missing Q8FBN1 could supply the sixth, and the notes themselves say "at most six could be". fig7 is in the same position (partial possible only through the missing models) and is marked blocked. For consistency fig6s1 should be blocked (data_missing), or both records should say that the outcome can be at best partial.
- **fig8-up-down-ramps.** On the printed estimate (102 min, ramps cell 12), the second reading exceeds the 60 min notebook limit. That meets the too_large definition the author quotes from the protocol, so I withdraw my provisional not_reproduced. The disagreement is recorded faithfully. The first reading gives 22 of 38 (ramps cell 11), so the claim cannot pass on that reading.

**2. Sentences the printed outputs do not support**

- Ramps cell 13 ("Result"): "timed on a subset at 40 simulated seconds per second, it would take 113 min, and this notebook had already run for 58 of its 60 min."
  - Ramps cell 12 prints 45 simulated seconds per second, an estimate of 102 min, and 52 min run so far.
  - The same stale figures appear in the attempt record's fig8-up-down-ramps notes and in its verification response.
- The 57 min estimate for the up legs is also not printed; ramps cell 12 prints 51 min.
  - It appears in ramps cell 17 (Summary): "113 and 57 min".
  - It appears in main cell 28: "57 min by the timing on a subset".
  - It appears in the figs3 deviation and response in the attempt record: "57 min … at 40 simulated seconds per second", "that notebook already takes 58 min".
  - The ramps notebook ran 51.7 min in total (ramps cell 18). A 51 min run would fit in a notebook of its own, so "does not fit" holds only for running it beside the existing ramps.
- deposit-models `measured` 0.192 and 0.239 ("means over models and cells"): neither value is printed. The cell 14 table averages to 0.193 for PD duty cycle and 0.234 for LP and PY. This does not change the outcome.
- Entry README:
  - "matches the Java to 3e-9 mV": that holds at 18 °C only. At 25 °C the difference is 0.056 mV (cell 5); the Summary states this correctly.
  - The run times do not match the printed ones. The README says about 15, 35 and 15 min; the printed times are 28.3 min (cell 73), 51.7 min (ramps cell 18) and 20.9 min (voltage cell 11).
  - "four are filed under other spellings": cell 7 shows one of the four (4X6W66) matched an unreadable character, not a different spelling.
  - The table gives fig2 as "Reproduced" without saying it rests on an assumed rule.
- Main cell 6 (markdown, not a conclusion): "The Methods name 25 models". Cell 7 prints 21.

I checked every other "**Result:**" sentence, the three Summaries and the remaining attempt-record notes against the outputs, and they agree. My round-1 reasons appear in the `verifications` entries in my own words, with points from section B merged into some of them. Their cell numbers are the round-1 indices.

**3. Round-1 points**

Resolved:
- Problem 1, removal protocol: both protocols are now run (cells 65 and 68).
- Problem 3, fig2 threshold reading (b): it is computed, with the caveat in section 1.
- Problem 4, fig4 slow-wave burst bounds: they are run and the outcome is unchanged (cell 38).
- Problem 5, Java against the port above 18 °C: compared at 25, 34 and 35 °C (cell 5). NaN appears at the same step in both.
- Problem 6, parameters outside the Methods' search space: shown in cell 12 and recorded as finding 7.
- Problem 7, 0 mV threshold: computed in cell 71.
- Problem 8, ramp update description: the helper and the ramps notebook now agree.
- Problem 10, fig6 and fig6s1 analysis windows: the dominant currents now come from the same 40 s runs.
- Problem 11, KNMLBC read as KMNLBC: kept as a stated assumption.
- Section C: fig7 reading (b) is computed, and the README lines and file-name scores are printed (cell 32).

Remaining, and bearing on a conclusion:
- fig8-up-down-ramps: the second reading has not been run, so the claim is undecided.
- figs3: the main ramp reading has not been run. A notebook of its own could run it (51 min printed).
- fig2: the outcome rests on the threshold-(b) rule.
- fig6s1: the outcome label, as set out in section 1.
- Which 36 of the 38 models the paper used still cannot be told from the files. This affects all-models-compensated and the counts in fig8 and fig10b.

**4. Critical findings**

No finding in the attempt record is rated `critical`. The ratings given match what the outputs show:
- Finding 1 (four named models absent) is rated major, shown in cells 7 and 8.
- Findings 2, 3, 4, 5 and 7 are rated minor, shown in cells 7, 10, 14 to 15, 5 and 47 to 48, and 12.
- Finding 6 (questions for the authors) carries no severity rating.

I found no misreading of the paper in the claims file.
