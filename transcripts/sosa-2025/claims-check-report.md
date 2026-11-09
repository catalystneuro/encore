**Checker result:** `50 claims, 48 quotes, 65 statistical values, 3 problems`. All three are p-values that are in the text but printed with a trailing zero: 4.40e-8 for m12 in Fig. 6e, 3.70e-6 for m4 in ED8k, and 8.0e-9 in ED3o. The YAML parses them as 4.4e-8, 3.7e-6 and 8e-9, so the checker doesn't match them. All quotes passed.

**Changes, by claim** (all in `claims/001361/10.1038-s41593-025-01985-4.yaml`):
- **Header:** the switch mice were given as "m2 to m19", but m2 is a fixed-condition mouse. I listed the 11 switch mice by name and added that m11 was imaged only from day 3.
- **fig6e-rr-prefer-reward:** the statement said the median index was positive in 9 of 11 mice. In fact it is positive in all 11 and significant in 9. Reworded.
- **ed8k-rr-prefer-reward-after-switch:** added the eleven per-mouse Wilcoxon tests from the legend.
- **ed6a-rr-near-reward-stable:** the rank-sum test and the 50 cm split were made up; the paper reports no test. I named the comparison as open, with two readings and a rule for when they disagree (`methods_underspecified`). I also added the legend's cell counts (2294 RR, 3408 TR) and "and become RR" to the statement.
- **ed6-across-day-drift:** added the two cell sets the cited panels hold as readings (j and l, or k and m). The comparison of medians is now marked as a reading, not the paper's test.
- **ed7-no-anatomical-bias:** the "fewer than half of the mice significant" rule was invented. It now uses the paper's counts (2 ML, 1 AP, 1 depth) plus their tolerance.
- **ed3fg-fields-remap-independently:** the criterion now counts significant correlations of either sign, not only positive ones, since the paper's tests are two-sided.
- **glm-well-fit-cells:** the FDE means (0.32 TR, 0.29 RR) could be over well-fit cells or all cells. Both readings now count equally, and the means are added to the statement.
- **fig4qr-tr-track-ends:** added "tended to" to the statement, as the paper words it.

**Still open:**
- **ed5-teleport-fractions:** the paper doesn't say whether the values pool mouse-day rows or average per mouse first. The legend's "n = 7 mice" leans towards per-mouse means.
- **fig1h-lick-ratio-improves** and **fig4no-licking-speed-increase:** the paper gives no test or window for "improved", "retained" or "anticipatory". The criteria rest on readings that are named as such.
- **Not covered:** Extended Data Figs. 3c, 3h-k, 4d,e and 5j,k have no claim. None is a main finding; the other main findings all have one.

**Ready:** yes. The `checks` entry records `ready: true`. Nothing is committed.
