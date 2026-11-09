I re-ran the claim for the one answered question. The entry now locks, passes its check and runs from a clean environment (`0 error(s)`, notebook pass in 2832 s), and the handover is built in `executed/001605-funamizu-2016/handover/`. Nothing is committed or pushed, and I did not verify my own work.

## Question: supp9-preserved-representation

**What I asked:** whether Supplementary Fig. 9b uses the signed difference in distance preference, not the absolute difference the claims file had.

**What the answer changed:** the reader amended the criterion. It now tests the signed difference (continuous minus intermittent), counts the area whose median is nearer zero as the one that preserved more, and requires both readings of where the before-reaching groups are split. The absolute difference is now a variant that is reported but not judged.

**Outcome: partially reproduced. Earlier: reproduced, resting on two assumptions** (the task-relevance baseline of zero, and equal-quarter groups). Under the amended criterion:

- **After-reaching neurons in intermittent 1:** PPC and PM differ in layers 2 and 3, with the PPC median nearer zero.
  - Layer 2: -2.10 against -5.04 cm, P = 0.0066.
  - Layer 3: -2.52 against -6.30 cm, P < 1e-5.
  - Layer 5 does not differ (P = 0.20).
- **Groups split at the zone borders:** none of the 9 significant comparisons has PM nearer zero, so the criterion is met.
- **Groups split into equal quarters:** 2 of the 10 significant comparisons have PM nearer zero, so the criterion fails. Both are layer 3 before-reaching groups far from the goal in intermittent 1:
  - 67 to 50.25 cm: PPC 2.52 cm, PM 0.00 cm, P = 0.013.
  - 50.25 to 33.5 cm: PPC -9.24 cm, PM -1.89 cm, P = 0.037.
- **Why partial:** the criterion needs both group readings, so it is not met, and this is the same under all four readings of the classification. The after-reaching part holds under every reading. In the groups nearest the goal, every significant comparison has PPC nearer zero.
- **Assumptions:** the outcome no longer rests on one. The criterion now covers both group readings, and the classification readings agree.
- **Absolute-difference variant (not judged):** PPC is smaller in all three layers. PM is significantly smaller in 0 of 30 comparisons with equal quarters and 1 of 30 with zone borders.

## Files changed

- **`entries/001605-funamizu-2016/reproduce_funamizu_2016.ipynb`:**
  - The supp9 section now runs the signed test with "nearer zero" decided per comparison, under both group readings and all four classification readings, with the absolute variant alongside.
  - It also prints the group sizes against Supplementary Fig. 9a, the range of the signed differences, and a per-mouse breakdown.
  - The conclusion and the summary table are updated.
- **`attempts/001605-funamizu-2016-01.yaml`:**
  - The supp9 outcome is now `partially_reproduced` without `assumed`. Its notes say what the answer changed, and the deviation for the group-border assumption is removed.
  - The finding addressed to the paper's authors now says that the two group readings disagree on supp9.

No other claim was affected by the answer.
