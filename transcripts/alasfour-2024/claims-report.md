I wrote `claims/alasfour-2024.yaml`, and the quote checker passes it: 30 claims, 29 quotes, 10 statistical values, 0 problems. There are no em dashes, no "rather", and no plain scalar contains ": ". Nothing was committed.

**Text read.** The version of record from PubMed Central (PMC11169785): main text, Methods, Results, the legends of Figures 1 to 7, Table 1 and the Discussion. The paper has no supplement, and no PDF was supplied. The paper links no code and names no software, so no code was read.

**Claims.**
- **Quotes:** 30 claims, 29 with a quote. The Table 1 claim is marked `inferred` because its numbers appear only in the table.
- **Statistics:** 9 claims carry 10 entries. These are the t-tests against chance with Benjamini-Hochberg correction at p ≤ 0.01, the mean-difference t-tests against zero, and the ANOVA results (ROI and band p reported as 0, interaction p = 0.46).
- **Criteria and expected values:** all 30 claims have a criterion, and 10 have expected values.
- **Data:** 28 claims are `with_inputs`. They need the electrode-to-region projection matrices from Peterson et al. 2021a. The paper gives no location for these matrices; they are on that paper's Figshare deposit.

**Details the paper leaves open (O1 to O16 in the header).** Criteria refer to these by number.
- **O1, participant numbers:** Table 1 numbers the participants 1, 2, 4, 5 and 8, but the Results name a "Participant 3". Readings: (a) the figures number the five 1 to 5 in table order; (b) the figures use the table's numbers.
- **O2, inclusion:** at least 1 h of each behaviour, or at least 1 h of the two together.
- **O3, filters:** the Butterworth order and phase are not given. I used a standard choice (4th order, zero phase).
- **O4, artifact rule:** more than 2 s in total within the block, or more than 2 s in a row.
- **O5, assigning electrodes to regions:** an electrode goes to its largest-weight region or to the nearest region centroid. The density rule is fewer than 3 electrodes, or a summed weight below 3.
- **O6, features of a region:** each electrode is a feature, or one feature is the region's mean.
- **O7, cross-validation buffer:** the folds on both sides of the test fold are left out of training, or only one neighbouring fold is.
- **O8, balancing and LDA:** random downsampling and default LDA settings, a standard choice.
- **O9, finite chance level:** alpha is 0.05 or 0.01, and n is the test samples per fold or all test samples together.
- **O10, ANOVA:** the type of sums of squares is not given. I used type II, with types I and III as variants.
- **O11, averages:** pooled fold accuracies, or the mean of the per-feature means.
- **O12, post-hoc test on regions:** Tukey HSD, or pairwise t-tests with false-discovery-rate correction.
- **O13, per-participant significance (Figure 4):** a t-test over the 7 folds, or the mean above the chance threshold.
- **O14, regions missing for some participants (Figure 6):** count only the participants that have the region, or count only combinations present in all five.
- **O15, validation set (Figure 7):** a held-out training fold, or the ranking from single-region accuracies.
- **O16, three-class analysis:** read as the same scheme as the two-class one. Table 1 suggests participant 8 is the one left out.

**Missing from the paper that claims needed.**
- **Figures:** no figure could be read, so values shown only in Figures 2 to 7 are unknown. These include per-feature accuracies, confidence intervals and the chance level itself.
- **Missing thresholds:** the paper gives no test or threshold for "not additive" (Figure 7), "regularly exceeds 80%" or "usually exceeded". The criteria I wrote for these are readings, and their outcomes will rest on assumptions.
- **Conflicting statements:** the abstract and Results say "exceeded 70%", while the Discussion says "regularly exceeds 80%".
