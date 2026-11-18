**Verifier report, round 3: wang-2019-01 (doi:10.1113/jp278016, SPARC:212 v1)**

The attempt record has a `proposed` block on one outcome only: fig2a-rabbit-monotonic (record lines 94 to 102). No other claim has a proposed change, so this report covers that one claim.

| Claim | Proposed outcome | Agree? | My outcome if different | Reason |
|---|---|---|---|---|
| fig2a-rabbit-monotonic | not_reproduced (currently partially_reproduced) | Yes | | See below. |

**The numbers come from the data.** Cell 23 computes them from the per-heart Fig2 rabbit table (4 hearts, 10 time points) with `sns.monotonic` and `sns.against_time0`. I read `sns.monotonic` (sns.py:260), and it applies readings (a) and (b) as the claims file words them.
- **Heart rate:**
  - The mean peaks at 206.5 bpm at 20 s and falls at every later step, to 194.75 bpm at 60 s.
  - The 50 to 60 s fall is significant by paired t-test, p = 0.0469.
  - No heart rises at every step.
  - So heart rate fails monotonicity under both (a) and (b).
- **CaTD80:** monotonic under (b) but not (a). The mean is lowest at 25 s and rises after that.
- **APD80:**
  - It is monotonic under both readings.
  - At 60 s it is significant under (i), paired t-test p = 0.021, and under the pooled-error variant.
  - It is not significant under (ii), Holm-Sidak adjusted p = 0.1766.
- **All six combinations of readings fail** (cell 24: every (monotonic, significance) pair is False). The record's notes and cell 25 now match these printed values. The false sentence I flagged in round 2, that all three hold "under every significance reading", has been withdrawn and corrected.

**The choices were not made to reach the result.**
- **Time points:** the data's own time points are used, as the claims file directs.
- **Significance reading:** the outcome does not depend on it, because heart rate fails monotonicity before significance is considered. The record's deviation says this.
- **One sensitivity, from the claims file's wording, not from a choice made in this attempt:**
  - Under reading (b), heart rate fails only because of one unadjusted step test among 9 successive pairs, at p = 0.0469 (cell 23).
  - If that step were not significant, the combination (b, i) would hold for all three variables (cell 24: under (i) all three are significant at 60 s, CaTD80 and APD80 pass (b)).
  - The criterion specifies unadjusted paired t-tests at p < 0.05, so the analysis applies it as written.
  - Reading (a) fails for heart rate regardless: 5 of 9 steps go against, and the mean drops 11.75 bpm after 20 s.
  - The not_reproduced outcome is correct on the criterion's terms, but under reading (b) it hinges on a borderline test, and the notes should say so.

**The criterion is applied as written.** The criterion for fig2a says "Reproduced when, under some combination of readings, all three variables are monotonic ... and each differs from time 0 at p < 0.05 at 60 s." It has no partial clause, while fig2d, fig2cf and fig3abc have one (claims file lines 154 and 173 to 178). No combination meets the criterion, so not_reproduced follows. This is the outcome I gave in round 2.

**On the claims file:** it does not misread the paper here. The Fig. 2A legend and the Results (paper lines 61 and 121) state "monotonically" for rabbit HR, APD and CaTD, and the criterion follows that.

**Small remaining text points (no outcome effect):**
- The Summary in cell 52 says "HR and CaTD do not change monotonically". CaTD80 is monotonic under reading (b) (cell 23). The sentence should name heart rate under both readings and CaTD80 under reading (a) only.
- The README row says only "Partially reproduced; not reproduced is proposed…". It will need updating to not_reproduced once the change is accepted.
