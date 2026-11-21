**Verifier report, round 2: fritsche-2022-01**

Cell indices refer to the re-executed notebook. The claims file has 31 claims and the attempt record has 31 outcomes: 26 reproduced, 3 partially reproduced, 2 not reproduced. Two outcomes are marked `assumed: true`: `fig3b-thalamus-short-term` and `decay-thalamus-single`.

## 1. Outcomes

I agree with all 31 stated outcomes. They match my round-1 outcomes claim by claim.

The two outcomes resting on an assumption:

- **fig3b-thalamus-short-term (reproduced, assumed).**
  - **What it assumes:** "significant adaptation" counts only ratios below 1. The assumption is stated in the deviations, which also say that a two-sided reading would make the outcome partial. That matches cell 66: under the across-blocks reading only the partial rule holds two-sided. The paper's wording ("exerted significant adaptation effect"; "adaptation … appeared to be limited") supports the assumption, so it is reasonable.
  - **How fragile it is:** the pass comes from 1 of 12 readings (pooled ratio, blanks held, pairs across blocks), and RL sits exactly at the threshold of 6 (cell 65).
  - **What is stated but not shown:** the second deviation says the outcome "rests on the `noise` unit filter". The variant with `noise` units kept (cell 17) was run only with pairs within blocks, so its effect on the passing reading is not shown.
- **decay-thalamus-single (reproduced, assumed).** The assumption, the `noise` filter, is stated and reasonable. Cell 17 shows the dependence: with `noise` units kept, the LGN tau is 0.000, outside [0.004, 0.63].

## 2. Sentences the printed numbers do not support

- **Cell 49, and the attempt record notes for fig3a-v1-long-term.** "Eight of 12 readings give 8" is wrong: cell 48 shows 7 readings give 8, four give 2 and one gives 5. The record's version, "Eight of 12 … the four … give 2, and one … 5", adds up to 13.
- **Cell 77, and the attempt record notes for decay-cortex-double-better.** "with every unit's values (p = 4.2e-06 to 0.0021)": cell 76 gives AL p_F_units = 4.5e-09, so the range is 4.5e-09 to 0.0021.
- **Summary (cell 120).** "it gives the paper's 1-back values to within 0.01": this holds for drifting gratings and for static cortex. It fails for static thalamus: LGN 0.957 against 0.93, and LP 0.900 against 0.85 (cell 93).
- **Summary.** "the two thalamic claims marked above rest on it, as does the direction rule of fig3b" garbles the dependence. fig3b rests on the direction rule and, as stated, on the filter. The direction rule does not rest on the filter.
- **Cell 116, and the attempt record notes for fig8 ("contains the ground truth in every run").** This is true for the six named runs. Over the 200-seed sweep, the 1-back CI contains the truth in 192 and 189 of 200 seeds (cell 115).

All other "**Result:**" sentences, the README (group counts add up to 31; outcomes as stated) and the other notes agree with the outputs.

The verifications block quotes my round-1 reasons faithfully. One of them was wrong in round 1. For units-responsive-count I said results are "unchanged without" the `noise` filter. Cell 17 now shows that the LGN results change: a significant 7-back appears and tau falls to 0.000. I withdraw that statement.

## 3. Round-1 points

**Resolved:**

- Problem 3: a session bootstrap was added (cell 87), and fig5 moved to not reproduced.
- Problem 5: drops per tertile and re-formed tertiles were added (cell 41).
- Problem 6: the `noise` filter is now an explicit assumption with its effect shown.
- Problem 7: an invalid-intervals variant was added (cell 67). It changes no conclusion except adding an LGN 7-back under the main fig3b reading.
- Problem 8: `_boot_task` now passes the sign (`adaptation.py:463`).
- Section C requests: the mice that fail reading (a), the fig3b two-sided table, the LGN 9-back values, and 200 fig8 seeds were all added.

**Remaining, and bearing on a conclusion:**

- **fig3b (problem 1).** The problem is disclosed, not removed. The pass depends on the one-sided reading, on 1 of 12 readings with RL at the threshold, and on the `noise` filter, which was not tested under the passing reading.
- **fig8 (problem 2).** "Not reproduced" still comes from the claims file asking every CI to contain 1. Cell 115 shows that noise alone breaks that at about the chance rate. Only 38% of seeds pass, against the 39.7% expected if exclusions were independent. This is now a question for a reader, which is the right route, but the outcome still reflects the claims file's misreading rather than the data.
- **fig7a / fig7b-static-areas (problem 4).** With the 1-to-20 family, the 18-to-22 test is partly met by construction. With 1 to 50, the largest significant n is 46 to 49. This is the claims file's reading, reported. It bears weakly on the conclusion.

## 4. Critical findings

No finding in the attempt record's `findings` is rated `critical`. Findings 1 to 4 and 6 are minor, finding 5 is none, and findings 7 to 9 have no severity.

I also see no reason to rate any finding critical. The checks for duplicate recordings, subjects and clocks pass (cells 8–9). The `noise` label (finding 1) is in the files and is easy to filter on, so minor is right.
