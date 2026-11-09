No outcome changed and none is proposed. The round-2 verifier agreed with all 35 outcomes, and the new checks it prompted give the same results. The entry passes `python tools/entry.py all` (0 errors, notebook runs in about 53 s). Nothing is committed.

**fig4dh-lateral-more-sensitive (still reproduced).** I added three checks after the main table:
- **Tuning selection.** The paper includes only significantly tuned neurons, which needs trial data the data set does not have. As a stand-in, I ran a one-way ANOVA from each mean curve, assuming spike-count variance equal to the mean and five repetitions per heading. That keeps 252 of 258 values, and the passing reading gives p = 1.2e-07. A stricter version (three repetitions, variance twice the mean) keeps 169 values and gives p = 9.6e-08.
- **Units counted twice.** A mixed model with one random intercept per unit gives p = 2.7e-07 in the passing reading, and no other reading passes.
- **Counting window.** With 0.5 s or 2 s windows the passing reading still gives p = 1.9e-07.

The other readings still do not reach p < 0.001 under either selection. The conclusion, notes and deviations now say:
- the outcome rests on one of the 8 readings;
- the preference by condition interaction is significant (p = 0.026);
- the tuning selection is not applied, and each unit enters twice.

I also corrected the claim that "a different window scales all thresholds alike"; one term of the threshold formula does not scale with the window. To support this, `stc1.neuron_threshold` gained a `window` argument, which defaults to 1 s, so earlier results are unchanged.

**Text corrected:**
- "Matches the paper to the third decimal" is gone from the Summary, the README and the finding. They now say the group means 0.0241 and 0.1190 lie within the SEMs of the paper's 0.023 and 0.116.
- The README now says 7 of the 17 tested outcomes rest on the pooled noise-correlation assumption and 4 on the tuning amplitude and baseline, instead of "most outcomes".

**Outputs added:**
- The data check now prints the file_ids ending in "s". The record said "ten file_ids"; it is ten pairs in six recordings, so the notes and the finding now say that.
- The data check also prints the 7 pairs whose recordings share a cell id with experiment 1 units.
- A new cell prints the notebook run time. The README now says about one minute, and `entry.yaml` lists 1 minute.

**Questions file:** I created `questions/crcns-stc-1.yaml` with two questions for a reader, without changing the claims:
- whether the fig4dh criterion should apply the Figure 4 legend's selection of significantly tuned neurons;
- whether fig8ab should compare raw choice probabilities or their distance from 0.5, as the Figure 8A legend describes.

**Record:** Round 2 is under `verifications`, with `agrees: true` for all 35 claims, the verifier's reasons and my responses.

**Not done:** The verifier's point that "reproduced under one reading" is a lenient rule when there are 8 or more readings is about how the claims file was designed, not a misreading of the paper. I recorded it in the fig8ab response and left the rule alone. The paper's exact tuning selection cannot be applied without trial responses, and whether the data set's 258 choice probabilities are among the paper's 311 cannot be checked from it.
