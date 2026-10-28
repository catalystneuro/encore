I agree with the one proposed change: figs2ijk-ppx-washout should go from partially reproduced to reproduced.

**Count.** The attempt record has one `proposed` block (line 296 of `001177-zhuang-2025-01.yaml`), so only figs2ijk-ppx-washout is under review.

| Claim id | Proposed outcome | Agree | My outcome if different | Reason |
|---|---|---|---|---|
| figs2ijk-ppx-washout | reproduced | Yes | — | See below. |

**Reason for figs2ijk-ppx-washout**

1. **The numbers come from the data.** Cell 32 prints the p-values from the fits made by `friedman_block`. The reading used is the four PPX sessions and every washout session, which is the criterion's "48 h after each PPX injection", with n = 30 and no failed fits. Cell 35 builds its tables from those same objects, and the values the proposal cites match its output:
   - A, baseline against PPX OFF: p = 1. The criterion needs p ≥ 0.05, so this part holds.
   - K, baseline against PPX OFF: p = 0.0278 (pooled error).
   - AUC, baseline against PPX OFF: p = 0.00717 (pooled error).

   `icd.rm_oneway` (icd.py:484–506) computes the pooled comparison in the standard way. The standard error is sqrt(2·MSE/n), the test has (k−1)(n−1) degrees of freedom, and the p-value is multiplied by 3 for Bonferroni. This is how Prism makes the comparisons when sphericity is assumed.

2. **Direction.** The criterion asks that K and AUC after washout sit on the same side of baseline as under PPX, and they do:
   - K: baseline 0.258, PPX 0.321, washout 0.419.
   - AUC: baseline 3.95, PPX 2.90, washout 3.38.

   One small gap: these are medians. The ANOVA compares means, and the means are not printed. Dunn's test on K is significant in the same direction (p = 0.020), so I see no sign that the direction reverses.

3. **The choice was not made to reach the result.** The paper does not say how its Bonferroni comparisons were made (criterion reading (b), Table 1). The pooled error is chosen because it fits the paper's own printed p-values better, not because it gives the outcome. Cell 35's second table shows this:
   - Pooled matches the paper's significance at 0.05 in all six comparisons; paired t tests match in five and miss K (paper 0.01, paired 0.063).
   - For AUC the paper gives p < 0.01. Pooled meets it (0.0072) and paired does not (0.039).
   - Paired is closer only for PPX ON against OFF AUC, where both are significant.

   The disclosure is complete:
   - The record keeps `assumed: true` and states the assumption.
   - Cell 36 and the notes say that reading (a), Friedman with Dunn's, misses AUC (p = 0.078).
   - They also say that the first-ON or first-OFF readings do not give both K and AUC (cell 35, first table).
   - The docstring contradiction I raised in round 2 is fixed (icd.py:485–489).

4. **The criterion is applied as written.** It lists readings (a) and (b) without requiring both. It sets p ≥ 0.05 for A, p < 0.05 for K and AUC, and the same direction as under PPX, and all three hold under reading (b) with the stated assumption. The PPX ON against OFF comparisons are reported but kept out of the outcome, as the criterion requires.

**Claims file.** I found no place in this claim where it misreads the paper.
