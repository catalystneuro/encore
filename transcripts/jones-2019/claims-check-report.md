I found no misreading of the paper that changes a claim's meaning, so the file is ready for an attempt. I made 9 small corrections and left 5 points open.

**Checker result:** `claims/jones-2019.yaml: 65 claims, 65 quotes, 114 statistical values, 0 problems` (it was 110 values before I added four Figure S2 tests).

**What I checked.** I compared every claim with the text, legends, STAR Methods and Tables S1 to S4. I recomputed from the printed numbers:
- the three binomial p-values;
- the Holm-Sidak adjusted p for Figures 2, 3 and 4;
- each expected R against its printed F;
- the significant-comparison counts in Tables S2, S3 and S4.

These all agree with the claims, apart from the points below. Every main finding has a claim, and no claim comes from outside the paper.

**Changes, by claim:**
- **Header, method F:** the file gave no Holm-Sidak family for Figure 4. I added it: the 4 MWM learning metrics at 14-18 months and the 5 APA day 2 metrics. These reproduce every adjusted p printed in 4G, 4H, 4J, 4K and S4H.
- **cohort-swr-differences:** the existing readings don't fit the 25 degrees of freedom in t(25). I added a reading that does: the E4 mice with CA3 sites (13 + 14 mice).
- **figs2-nonspatial-no-difference:** the criterion counts 10 tests but only 6 were recorded. I added the missing four from the Figure S2 legend.
- **figs3-apa-day1-and-probe:** the directions for S3A to S3C are stated in the Results text, not only in the panels. The criterion now says so, and that only the S3D direction rests on the panel.
- **figs3fg-day2-predicts-later:** I made reading (b) precise. The 44 df match an ordinary two-way ANOVA of 13 mice over 4 days.
- **fig3c, fig4g:** each listed the unadjusted and adjusted results with nothing to tell them apart. I labelled them.
- **fig3g:** the day 3 and day 4 statistics are now written as F(1,7), as in Table S3.
- **rep-mwm-swr-overnight, rep-mwm-swr-slope-days-1-3:** the panel values 0.425 and 0.598 equal the R squared of the printed F. That supports the claims' choice to use the R implied by F.
- **figs4ab-aging-increase:** I noted that the apoE3 degrees of freedom are one lower than the legend's mouse counts give.

**Still open (recorded in `checks`):**
- I couldn't check the values the file says were "read from the panel", including the Spearman p of Figure 4C. No PDF renderer was available. Each R does agree with its printed F.
- I couldn't read the linked code repository, so the code-based method details are unchecked. The parts taken from the Methods match the paper.
- **nonspatial-not-correlated:** the paper doesn't say which spatial measures or which mice were used. The claim's choice (the four scores, E4 mice) is a reading.
- **Two numbers in the paper don't add up, and the claims already allow for both:**
  - **screen-88:** the printed p < 0.00032 doesn't follow from 9 of 88 significant, which gives about 0.032.
  - **fig2i:** the text's 77% doesn't fit F(1,11) = 27.3, which gives R squared 0.71.

**Ready:** yes. The last check is recorded with `ready: true`. Nothing was committed or pushed.
