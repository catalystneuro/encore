The claims file for DANDI:000637 is fit for an attempt (`ready: true`) after the corrections below. I left one problem open that the author must settle first: the paper puts its data in a different dandiset, DANDI:000946.

**Checker result:** `31 claims, 31 quotes, 84 statistical values, 0 problems`, before and after my edits.

**Changes, by claim**
- **Method S** (shared spiking method): the paper doesn't say whether the Wilcoxon test against baseline compares raw rates or normalized rates (where the baseline is 100% for every unit). Both are now named as readings.
- **Method D** (and Method T): the writer had decided on their own what to do with trials where a unit has no spike in the window. This is now open, with two readings: the trial gives no value, or it gives 0.
- **fig6c-pom-rsu-delayed**: the supporting sentence was cited to the Discussion, but it is in Results, tFUS parameters, paragraph 2. I also added that 30 and 300 Hz must not be significant, since the statement implies it and the other PRF claims require the same.
- **fig9a-s1-rsu-60dc** and **fig7d-pom-fsu-dc-3000**: the writer chose to Bonferroni-correct over 10 pairs, but the paper gives no count. Now open, with two readings: 10 pairs, or 15 including baseline.
- **fig10d-sttc-60dc** and **fig10ef-sttc-dc**: the writer chose median change, but the paper doesn't say whether it compares means or medians. The result must now hold under both.
- **fig5-sham-no-response** and **fig5-cg1-control-no-response**: these tested only for an increase. The paper says "no change" without naming a tail, and fig4-fsu-no-change already tests both, so both tails are now tested.

**Open**
- **Dataset mismatch:** the dataset description of 000637 lists S1 recordings only, with pulse durations of 100, 200 and 400 us. That may not match this paper's recordings. The author has to establish which conditions, if any, the dataset holds.
- **dSTTC formula:** the equation is missing from the text and there is no PDF. The form used is reconstructed from the STTC of Cutts and Eglen (2014).
- **Discussion finding with no claim:** the Discussion says 3000 Hz with 90% DC lowers local activity (Fig. 7). No claim covers it; fig7a only requires 90% not to be significant.
- **Grading rules:** the cut-offs for reproduced and partially reproduced (for example 10 of 12 counts in unit-counts) were set by the writer, not taken from the paper.

All other statements, quotes, statistics, expected values and tolerances matched the paper. The paper's main findings each have a claim, and no claim draws on another source. Nothing was committed or pushed.
