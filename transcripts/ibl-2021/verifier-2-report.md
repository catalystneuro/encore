**Verifier report, round 2: IBL behavioral data (doi:10.7554/elife.63711) on DANDI:000045 0.211209.1413**

The claims file holds 39 claims. The attempt record gives 39 outcomes: 20 reproduced (lab-link included), 13 partially reproduced, 5 not reproduced and 1 blocked (methods_underspecified).

**1. Outcomes**

I agree with all 39 stated outcomes. These are the ones that changed since round 1, or where I now take a different view:

- **fig2g-days-differ-across-labs: partially_reproduced.** Agree, as in round 1. Cell 18: p = 0.029. Lab 2 IQR is 7.75 (in tolerance), Lab 6 IQR is 5.75 (not).
- **fig3s2a-trial-duration: partially_reproduced.** Agree. Cell 52: median 420.45 ms, s.d. 219 ms, Kruskal-Wallis p = 0.061.
- **fig3s4-looser-criterion: partially_reproduced.** Agree. Cell 69: 91 mice; trials per minute has corrected p = 0.0022. Cell 99: the classifier is not above chance.
- **fig3s3-other-classifiers: reproduced.** Agree. In round 1 I gave partially_reproduced.
  - Logistic Regression ran the full 2000 subsamples: 2.5th percentile 0.000 against a shuffled mean of 0.070.
  - The Random Forest ran 50 of the 2000 (cell 101). Its 2.5th percentile is 0.035, and the bootstrap 95% interval tops out at 0.057, well under the shuffled mean of 0.100. More subsamples are very unlikely to change the result.
  - Running 50 instead of 2000 is recorded as a deviation.
- **fig5dg-history-weights-higher-full: reproduced.** I now agree; in round 1 I said partially_reproduced.
  - The criterion takes the weights from fig5cf. fig5cf's criterion names the code's sessions first and treats (b) as a reading of the Methods.
  - On the code's sessions both t-tests pass under every reading of P1 and both 50% readings (cell 115).
  - I accepted "a match under one reading" for fig5s2-glm-accuracy in round 1, so the same rule applies here.
  - The failure under (b) (p = 0.10 to 0.39) is disclosed.
- **fig5s2-glm-accuracy: reproduced.** Agree, as in round 1. Cell 118, code's sessions with 50% trials dropped: 81.9, 83.5, 2.38 and 3.14, all in tolerance.
- **The remaining 33 outcomes** match round 1. The re-executed outputs support them.

**2. Sentences the numbers do not support, or support only in part**

- **Cell 119 and the record's notes for fig5s2-glm-accuracy and fig5dg** say fig5cf-glm-weights is one "which match[es] under one reading". Under the main reading of P1b, fig5cf meets every part under no reading. Cell 112 shows it passes only under variants (rows 6, 7 and 9), which is why it is partially_reproduced. The sentence should say the criterion *allows* a match under one reading, not that fig5cf matched. Neither outcome depends on this wording.
- **Cell 34 and the record (fig2s2):** "The two means are within tolerance under most readings." Cell 33 shows both means within tolerance under every reading, all 20 rows. The sentence understates the result.
- **Cell 28 (fig2bc):** "the bias ranges are shifted to the left." The early range is shifted. The later range (−8.6 to 7.1 against −5.6 to 6.5) is wider, not just shifted: its upper bound is above the paper's.
- **Record, fig3s3:** "A run of 100 subsamples while preparing, not in the notebook, agreed." No printed output supports this.
- **Record finding (wheel):** "the timestamps are not monotonic." Cell 7 prints only the length mismatch, not monotonicity.
- **README and cells 0 and 2:** loading takes "about six minutes". Cell 3 prints "loaded in 3.4 min".
- **Record, session-end-criteria:** "Per training day, 5,683 of 6,435 met a criterion." Cell 130 labels this count "met (status or 90 min)", so the 90-minute rule is included. Also, the criterion defines the count per training day, but the notebook decides on the per-session count. The outcome is the same either way.

Everything else I checked against the printed outputs holds: every "**Result:**" cell, the Summary (cell 132), the README counts (19 + lab-link, 13, 5, 1; runtime 26.7 min) and the other per-claim notes.

**My round-1 reasons in the record.** The record states all 39 in my own words. Where it adds my B-points to a reason (B1, B2, B3, B4, B5, B6, B7, B8), it gives them faithfully. The cell numbers in those reasons refer to the round-1 notebook, not the current one. That is acceptable for a historical record, but it is not said anywhere.

**3. Round-1 points**

All are resolved:

- **B1 (missing stimOn and proficiency):** resolved. Cell 12 shows 0 windows that fail only on an undefined reaction time, under every reading and for P2. I checked `training_status` in the helper module: it keeps evaluating windows until it has both P1 and the first 1b session. `full_proficiency` evaluates every window up to each mouse's P2. So the count covers all windows that matter.
- **B2 (mice that began training before the dataset):** resolved. Cell 9: 5 whole-training mice start on 2019-06-11 and 6 in the first week. Cell 15: dropping the 2 of them that reach P1 leaves two of four values in tolerance. The five fastest mice start between August and November.
- **B3 (fig5cf monotonicity):** resolved. Cell 112, over the 7 mice that have every weight: 0.93, 1.55, 2.35, 8.05 and 3.25 for 6.25% to 100%. The 50% weight is above the 100% weight, so the failure to increase is real, not an effect of different denominators.
- **B4 (blocks that were not data limits):** resolved. The Random Forest ran on 50 subsamples, and the notebook's agree-or-block rule was removed.
- **B5 (mislabelled column):** resolved; it is now `p_kw_fdr` (cell 55).
- **B6 (Kaplan-Meier censoring):** resolved; censoring now uses the same day count as the events (cell 24).
- **B7 (status False):** resolved by a variant: 5,734 of 6,539 meet a criterion (cell 130).
- **B8 (days against sessions for P2):** resolved. At most 7 mice could change (cell 12), which cannot close the gap of 60 against 98.

**Still bearing on a conclusion:** nothing that would change an outcome.

- The fig3s3 Random Forest rests on 50 of the criterion's 2000 subsamples. It is disclosed, and the margin is wide.
- The wording points in section 2 should be corrected, especially "which match under one reading". I still find no place where the claims file misreads the paper; I re-checked the session-end counts and the condition numbers against the text.
