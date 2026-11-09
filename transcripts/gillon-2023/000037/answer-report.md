I answered all three questions and marked each `answered: 2026-10-22`. The changes are only in `claims/000037/` and `questions/000037.yaml`, and nothing is committed. `tools/claims_check.py` reports 35 claims, 33 quotes and 0 problems. No statement or expected value changed.

1. **fig5-example-responses** (which Gabor panel the per-plane rule uses): The paper doesn't say. Its sentence cites Figure 5 as a whole, and the code picks the panel a and panel b ROIs separately. The criterion now lists three readings: (a) panel a, (b) panel b, (c) both. The outcome is the one all three give, otherwise `methods_underspecified`. From the numbers in the question, the readings disagree, so this claim (and fig5-consistent-vs-inconsistent) will probably end up `methods_underspecified`.

2. **fig7c-high-correlation-fraction**:
   - **Denominator:** It covers the two analysed mice, 413663 and 433414. The code's Fig. 7c source data list only those two, so 412933's sessions 4 to 6 are not included. Reading (a) wrongly said three mice; it now says two.
   - **Reading (c):** Every session must be within tolerance, not just one. The paper gives one value for L2/3 dendrites and names no session. The sessions are the three local sessions, each pooled over the two mice as Fig. 7c plots them. Per-mouse sessions are not a reading the paper allows.

   The code's own source data give 0.018% pooled, which is already outside the 0.005 to 0.015% tolerance.

3. **imaging-depths** (does a recorded 60 µm fail): No. The Methods give a range, "50–75 μm", so 60 µm passes. The criterion now reads 50 to 75 µm inclusive. The mismatch with Table 2 for mouse 433414 stays under table2-sessions.
