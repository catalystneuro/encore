The reader amended both claims, and both now come out reproduced. The other 38 outcomes are unchanged. The entry passed its checks (0 errors), the clean run passed in 383 s, and the handover is built in `executed/hunt-2018/handover/`. I did not verify my own work, and nothing is committed or pushed.

**Question 1, `figs1cd-fewer-cues-more-accurate`** (earlier outcome: not reproduced, now: reproduced)
- **What the answer changed:** the criterion now accepts two measures of accuracy and needs only one to hold:
  - (A) choosing the option with the higher true expected value;
  - (B) choosing the option with the higher expected value of the pictures observed, scored as in the claim `choice-accuracy-observed`.

  Trials stay pooled over sessions. The session mean that the paper's script uses is shown as a variant.
- **New analysis:** I added a notebook cell that computes (B), pooled, for 2, 3 and 4 pictures under each scoring rule of `choice-accuracy-observed`.
- **Results** (picture count from the paper's script):
  - Under (B), 2-picture trials are the most accurate in both monkeys under all four scoring rules. With the first rule: monkey F 90.24% against 82.67% and 79.81% on 3 and 4 pictures; monkey M 94.62% against 85.98% and 81.70%.
  - Under (A) they are not: F 74.96% against 76.10% and 79.62%; M 78.83% against 78.79% and 81.51%.
  - The mean value difference is largest on 2-picture trials in both monkeys under both definitions of value difference (F 0.266, 0.229, 0.219; M 0.271, 0.240, 0.228).
  - The session-mean variant gives the same order as (B).
  - Counting every fixated picture instead: (B) holds in both monkeys under three of the four scoring rules and in F only under the fourth. The value difference is then largest on 2-picture trials in F only.

**Question 2, `fig7a-ofc-value-difference-neurons`** (earlier outcome: partially reproduced, now: reproduced)
- **What the answer changed:** OFC no longer has to lead at both p < 0.05 and p < 0.01; one significance level is enough. The script's threshold, |T| > 1.64, was added as a third level. The proportions themselves are unchanged.
- **Results** (Figure 5 trial types), where OFC leads ACC and DLPFC at all three tests:
  - 250 ms, p < 0.05: OFC 6.0, 4.4, 6.6% against ACC 5.3, 3.2, 4.8% and DLPFC 1.5, 2.2, 2.2%.
  - 300 ms, p < 0.01: OFC 1.6, 1.6, 3.3%.
  - |T| > 1.64: both time bins.
- **Where it still fails:** 250 ms with p < 0.01, 300 ms with p < 0.05, and every combination using attribute trials for the cue 3 tests.
- **The effect is weak:**
  - None of the pairwise chi-square tests reaches 0.05 (smallest p = 0.084).
  - By monkey, OFC leads at all three tests in M but not in F. In F, ACC is higher at both cue 3 tests: 3.2% and 7.4% against OFC 3.0% and 5.0%.

  I added the per-monkey result to the notebook and the record, since the run printed it but no text reported it.

**`fig7b-ofc-value-difference-any`** (depends on fig7a; reproduced before and after)
- The outcome is unchanged. OFC has the largest fraction at every time bin and level with the Figure 5 trial types (for example 11.5% against 9.0% and 6.0% at 250 ms, p < 0.05). I added a note saying so.

**Files changed:**
- **Notebook:** the text for both claims, the new cell, and the summary table.
- **Attempt record `attempts/hunt-2018-01.yaml`:** the outcomes and notes, each note saying what the answer changed.
- **`README.md`:** the totals are now 37 reproduced and 3 partially reproduced. The run-time line now reads 6 to 14 minutes.

The finding that asks the authors to confirm the script's choices still applies, so I left it as it was.
