# Round 3 verifier report: 000686-pakhomov-2023-01

I counted from the attempt record: it has 20 outcomes, and one of them carries a `proposed` block. That claim is fig5c-normalized-contrast. The claims file has 20 claims. No other claim was reviewed.

| Claim | Proposed outcome | Agree? | My outcome if different | Reason |
|---|---|---|---|---|
| fig5c-normalized-contrast | not_reproduced, with `assumed: true` for ROIs one step wide (the record's current outcome is blocked, methods_underspecified) | Yes | — | See below. |

**Do the numbers come from the data?** Yes.
- Cell 21 prints every reading under all six ROI geometries.
- With ROIs one step wide, the test holds in 27 of 32 readings under both ROI ends. The 5 failures all use the centre ROI (O1 a):
  - measured-footprint end: p = 0.0529, 0.0543, 0.056, 0.0562, 0.0601;
  - needle end: p = 0.0512 to 0.0824.
- These match the proposal's reason and the summary in cell 24.
- Cell 24 prints the ROI spacing from Methods 2.4 (2 × 3.65 mm / 112 = 65.2 µm) against the step used in the images (65.4 to 68.4 µm).
- The test is the right one. `cancan.ttest` runs `stats.ttest_ind(..., equal_var=True)`, an unpaired Student's t-test, two-sided as Methods 2.4 says, and `test_5c` (cell 9) requires t > 0 and p < 0.05.
- `band_means` with `across=1` gives a square ROI, one step along the diagonal and one step across it.

**Was the width chosen to reach the result?** No.
- The 1-step square was the main geometry in round 1 (`MAIN = ("footprint", 1)`), before any of the width variants existed.
- In round 2 I called it the most direct reading of 224 ROIs that tile ±3.65 mm on two diagonals. The proposal quotes me correctly.
- The paper (Methods 2.4) gives the number of ROIs and the distance they cover, but no width. A square at that spacing is the plainest reading of the layout.
- The record still shows the 3- and 5-step variants: 32/32 and 31–32/32 readings hold. It also marks the outcome as resting on the width assumption. That is the right way to disclose it.

**Is the criterion applied as written?** Yes.
- The criterion for fig5c requires the test to hold "under all readings". Unlike fig5a-trains and fig5a-packet, it has no methods_underspecified clause.
- ROI width is not one of the claims file's readings (O1–O7), so the readings to count are O1 × O2 × O3 × O4 at the assumed width. Five of them fail, so the claim is not_reproduced.
- The other points the criterion asks to be reported are reported. The 1P × 40 normalized centre is above 100% in all 32 readings (128–267%), and 1T × 40 is at 43–64%.
- The record states that fig5c depends on fig5b-rotation-center-peak, which is not_reproduced. That is consistent with this outcome.
- The O3 (b) per-dish test is labelled as an assumption. One O3 (b) reading fails (roi/bg/e1+e2/b, p = 0.0543), but the outcome does not rest on it: the four O3 (a) centre-ROI failures are enough.

**Caveats, which do not change my agreement:**
- This is a near miss. Every failing p is between 0.051 and 0.083, and the direction holds in all readings.
- The centre-ROI value of 1P × 40 rests largely on one dish (dish2). Round 2 found that this dish's bright centre is consistent with labelled cells rather than saturation.
- One wording point in the claims file, reported but not corrected: O1 says "The paper gives no ROI size". The paper's ROI count and range do fix the ROI length along the diagonal (about 65 µm). Only the width is open. This does not change any outcome.
