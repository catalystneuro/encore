I took up all four answers. Two claims changed outcome, from blocked to reproduced: fig2a-temperature-resistance and fig2c-scv-lower-carrying-capacity. Every other affected claim kept its earlier outcome.

I re-ran the claims under the updated criteria and updated the notebook, the README and `attempts/dryad-tdz08kq5d-wang-2024-01.yaml`. Each affected claim's notes now say what the answer changed. `lock` left the lock file unchanged, `all` gave 0 errors and the notebook ran in 10 s, and `handover` wrote `executed/dryad-tdz08kq5d-wang-2024/handover/`. Nothing was verified by me, committed or pushed. The record's runner URL now points at this run (40511182873).

**Question 1: which OD600 time points enter the Figure 1B ANOVA.** The answer is days 2 to 12, which the three ANOVA claims now use. The other day sets (days 0 to 10, all seven days) are kept as variants that decide nothing. The area under the curve now has three readings named by day.

| Claim | Before | Now |
|---|---|---|
| fig1b-temperature-density | reproduced | reproduced (F = 73.989, p = 3e-10) |
| fig1b-phage-reduces-density | reproduced | reproduced (F = 48.800) |
| fig1b-phage-effect-diminishes | reproduced, decided on days 2 to 12; days 0 to 10 would have made it partially reproduced | reproduced (F(5, 180) = 3.870, p = 0.0024); days 0 to 10 no longer count |
| auc-phage-reduction-by-temperature | reproduced, measured 66.80 / 37.18 | reproduced, measured 64.55 / 33.73 |

For the area under the curve, the new readings give:
- (a) trapezoid over days 2 to 12: 64.55% at 25 °C and 33.73% at 35 °C. The record now gives these as the measured values, since (a) is the first reading listed.
- (b) trapezoid over days 0 to 12: 66.80% and 37.18%, the paper's numbers.
- (c) sum over days 2 to 12: 68.40% and 34.50%.

All six are within tolerance, the 25 °C reduction is the larger each time, and every p is below 0.004.

**Question 2: what the 0.24% is a share of.** The paper does not say, so the criterion now names both ways as readings: (a1) the mean of replicate frequencies and (a2) pooled counts. The rule is still that one matching reading is enough.

| Claim | Before | Now |
|---|---|---|
| fig1d-mucoid-lost-with-phage | reproduced, with a deviation | reproduced: (a1) gives 0.244% and matches, (a2) gives 0.561% and does not; the deviation is gone |

**Question 3: the unit of the Table S3a to S3c ANOVAs.** The unit is the mean of the clones of each colony type within each replicate population, 22 values. Each clone as the unit is now a variant. Sequential and type II sums of squares both remain readings.

| Claim | Before | Now |
|---|---|---|
| fig2a-phage-exposed-more-resistant | reproduced | reproduced (F = 280.75 and 30.50) |
| fig2a-temperature-resistance | blocked (methods_underspecified) | **reproduced**: p = 0.0226 and 0.0092, mean resistance higher at 35 °C (0.790 against 0.731). The p = 0.071 that blocked it came from the clone reading, now a variant. |
| fig2a-no-temperature-phage-interaction | reproduced | reproduced (p = 0.168 and 0.489) |
| fig2a-scv-more-resistant | reproduced | reproduced |
| fig2b-scv-higher-growth-rate | reproduced | reproduced: colony type p = 7e-5 and 4e-5; the interactions are not significant (p = 0.109; 0.967 and 0.559) |
| fig2c-scv-lower-carrying-capacity | blocked (methods_underspecified) | **reproduced**: colony type p < 1e-6; temperature × colony type p = 0.093 and 0.273, phage × colony type p = 0.109. The significant interactions that blocked it came from the clone variant. |

fig2a-mucoid-25p-replicate-resistant compares clones one by one, so this answer does not touch it; it stays reproduced.

**Question 4: whether the sequencing and RNA-seq claims are `data: dataset`.** Yes. The nine claims now count with the dataset, and their deviations no longer say the claims file marks them `elsewhere`. Each still says the pipeline from the raw reads was not re-run. No outcome changed:

| Claim | Outcome, before and now |
|---|---|
| sequencing-mutation-count | not reproduced |
| table1-phcs-in-scvs | reproduced |
| table1-pild-in-25p-mucoid | reproduced |
| table1-t2ss-in-35p-scv | blocked (metadata_insufficient) |
| rnaseq-differential-expression-count | reproduced |
| rnaseq-kegg-enrichment | blocked (methods_underspecified) |
| rnaseq-mutated-genes-expression | not reproduced |
| rnaseq-defense-systems | reproduced |
| rnaseq-virulence-genes-down | partially reproduced |
