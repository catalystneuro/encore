**Verifier report, round 2: Li et al. 2016 (doi:10.1038/nature17643) on CRCNS alm-3**

The claims file has 29 claims, and the attempt record gives one outcome for each: 9 reproduced, 8 partially reproduced, 7 not reproduced and 5 blocked. Cell numbers below count from 0 in the re-executed notebook.

**1. Outcomes and assumptions**

I agree with 28 of the 29 outcomes. Most need no comment. These do:

- **fig6-modular-models-robust: I disagree.** The record says partially reproduced; it should be not reproduced. The criterion has no partial rule. It needs the integrator to recover in at least 90% of runs, and on lick-left trials it does not (cell 90: −7.2 against −14.4). For ed2e, ed7e and ed10e the record changed the outcome to not reproduced "as the criterion has no partial rule". The same rule applies here. If the cause is an incomplete matrix in the paper, that belongs in the methods_unavailable finding, which already asks about it. It does not make the outcome partial.
- **fig2-bilateral-recovery: I now agree with partially reproduced, with caveats.**
  - It rests on 6 of 64 readings, all with the 10 screening trials drawn in total (M4 reading b).
  - The criterion's partial rule does not quite fit. The rule is "a time outside tolerance". In those six readings both times are within tolerance, and what fails is the bilateral rate (1.114).
  - In the same six readings, ipsilateral selectivity 0.2 s before the cue is still 28% to 54% below control (cell 26). So it reaches 80% for a moment and then falls back.
- **ed6-bilateral-bias-inconsistent: agree, but it rests on reading (b).** The last sentence of the criterion still says "the side of the decision boundary" (reading a), which gives 0.62 and fails. Only reading (b) gives 0.88, with n = 8. The checker added reading (b) without updating that sentence. This is an inconsistency in the claims file, which I report here and do not correct.
- **models-monolithic-fail: agree.** This criterion also has no partial rule, so partially reproduced only makes sense here as "partly testable", since two of the five models were not simulated.
- **Fragile passes:** fig3-cd-roc (2 of 16 readings) and ed8 (3 of 32 readings).

Both outcomes marked `assumed: true` state their assumptions, and the assumptions are reasonable:

- **models-monolithic-fail.** The assumptions are a rank-one matrix 0.99uuᵀ, a ramp target, and RLS updates every 2 ms. One caution: the simple integrator's deviation of 0.212 against the 0.2 threshold depends on the rank-one choice, so this assumption decides a borderline result.
- **fig6-modular-models-robust.** The assumptions are noise variance per integration step and partners sharing the same preference. Choosing the per-step reading is justified: under the per-unit-time reading, even the unperturbed attractor ends on the wrong side 45% to 49% of the time. One small omission: running bilateral silencing to 4 s, not 2 s, is not listed as a deviation.

**2. Sentences the printed numbers do not support**

- **Cell 61 and the ed8 notes:** "three of the 24 readings match" / "3 of 24 readings match". Cell 60 prints 32 readings. The response to round 1 says the notes give the share, but the share they give is wrong.
- **ed8 notes:** "with window (a) the ipsilateral and bilateral values are 0.48 to 0.53". Cell 60 shows ipsilateral 0.490 to 0.544 and bilateral 0.473 to 0.526.
- **Cell 33:** "The neuron counts (180 …, 319 to 323 …, 56 in Experiment 3) are above the legend's … 52, 52, 102". 56 is below 102.
- **Cell 24 and the fig1g notes:** "every resample recovers" / "every resample recovering". In cell 23 the code-reading row has a censored mean of 424 ms against 420 ms for the early-delay condition, so a few resamples do not recover. "At least 99%" is what the numbers support.
- **Cell 82 and the fig5 notes:** "Across the 64 readings … bilateral in none". In seven readings of cell 44, `ms_12` has a value, so at least one resample recovered. The fraction is below 0.5%, not zero. The outcome does not change.
- **ed7e deviation:** "Three of the six Experiment 3 sessions, and one of them only in part, carry the paper's ROC". No output supports this. Cell 63 shows four sessions passing, each with trials in every group.
- **ed4 notes:** "The round-1 result … came from windows that overlapped photoinhibition". The window and the end point changed together, so the effect of the window alone was not isolated.
- **Cell 31 versus the ed2b deviation:** the cell says "Mouse lines from the code's comments". The record and cell 5 say the meta data files, and cell 5 is what the code uses.
- **README:** "It takes about seven minutes". No total run time is printed; cell 2 gives 141 s for loading only. Also, "their MD5 sums printed in the notebook" (and the cell 0 wording) refers to sums copied from checksums.md5. They are not computed from the bytes read, so they cannot show that a file changed.

Everything else in the Result conclusions, the Summary, the README table and the record's notes matches the printed outputs. The Summary's outcomes match the record.

The record states my round-1 reasons in my own words, accurately. For ed3 it takes the reason from section C of my report, because my table entry only cross-referenced it ("See item 4 below").

**3. Round-1 points**

Resolved:
- B1: a time now counts only if at least half the resamples recover, and the censored mean is shown.
- B2: the RMS windows now start after photoinhibition, and the end point is the last 400 ms of the delay.
- B3 and B4: every selection rule and every M4 reading is run, with neuron counts after each selection step.
- B5: the attractor runs to 4 s, and the matrix question is put to the authors.
- B6: modes from correct trials only are run.
- B7: the reading with more than 5 trials (12 sessions) is shown.
- B8: the variant without the four non-silenced sessions is shown, and the sessions are listed as a finding.
- B9: lick variants are run on the exp3 and exp2b sessions.
- B13 (ii) and (iii): now raised as questions and as a paper_inconsistency finding.
- Every "could not check" item in section C has been printed.

What remains that bears on a conclusion:
1. **fig6:** the outcome should be not reproduced, by the record's own rule for criteria without a partial rule.
2. **fig2:** partially reproduced rests on 6 of 64 readings, all M4 reading (b), with the ipsilateral deficit still 28% to 54% just before the cue. The criterion's partial rule does not cover a case where the rate fails and both times pass.
3. **ed6:** reproduced only under reading (b), which the claims file's own reproduction sentence does not name.
4. **ed8:** the reading count (24 against 32) and the window (a) range need correcting. A pass on 3 of 32 readings is fragile (B10).
5. **fig1g:** the neuron count (72 under the code's reading, 66 to 160 across readings, against 55) is still unexplained. It does not move the outcome from partially reproduced.
6. **ed2e (B13 i):** whether low-level inhibition means significance per neuron decides the outcome. It is now asked of a reader.
