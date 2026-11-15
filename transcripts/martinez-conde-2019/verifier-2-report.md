**Verifier report, round 2: martinez-conde-2019-02**

**1. Outcomes**

The claims file has 19 claims and the attempt record has 19 outcomes. I agree with all 19.

- **No assumption needed:** neuron-counts (not reproduced), spikes-per-condition (blocked; `norm` is 0 in all 73 files read, cell 11), fig4a-above-baseline (reproduced), fig4b-pairwise-significance (reproduced), table1-p180 (partially reproduced), table1-s40 (reproduced), fig6-midpoint-representative (reproduced), fig7a-rms-contrast-fit (not reproduced), fig7c-fold-edge-significance (reproduced), fig7d-dog-similar and s3-latency-peak (blocked).
- **Assumed, stated and reasonable:**
  - s4-baseline-no-difference rests on the Methods' squares, which the criterion itself defines as the baseline. Both placements of the squares find a difference; `BaseActivity` does not (cell 34). Confidence stays low because `BaseActivity` may be the authors' own baseline.
  - fig4b-spike-rate-difference is partial under every baseline (cell 40), so its assumption does not decide the outcome.
  - fig5-average-maps and fig7d-nonlinear rest on the measures their criteria name.
  - table1-s52: the squares give 4 of 5, `BaseActivity` gives 2 of 5.
  - fig7c-fold-edge-equivalence follows the criterion's literal wording (0.037 from 0.90). The record says that the grid-step reading would pass and that "nearest" under reading (b) only picks the ends of the range.
- **Assumed, stated, but the alternative is as defensible:** table1-edge and table1-s90 (not reproduced). Squares inside the corners give at most 2 of 5 and 1 of 5. Squares centred on the corners give 3 of 5 for both, which is partial (cells 52, 58). The record argues that centred squares cross the ROI border. But they still lie entirely on 0% luminance (cell 25: max 0.0), and at most 19% of a square falls outside the ROI. The Methods say "at the corners of the … circumscribing square", which fits centred squares at least as well. The outcome is a toss-up between the two placements.
- **Assumed flags disagree with the Summary (cell 86).** table1-s52 is `assumed: true` in the record but carries no assumption in the Summary. table1-s40 carries "assumption: Corners baseline placement" in the Summary but is not `assumed` in the record. The Summary also lists the Corners placement as an assumption for s4, yet cell 35 says Square and Edge against Star alone is significant, so that placement does not decide s4.

**2. Text against outputs**

These statements are not supported by the printed numbers:

- **Cell 42:** "A lower baseline alone would therefore not bring all three to the paper's values at once" and "the gap is largest on the Edge, whose response is not baseline-related".
  - The record's fig4b notes say the same: "so no single lower baseline gives all three".
  - From cell 41, a mean baseline anywhere from 6.64 to 8.24 spikes/s puts all three midpoints within the paper's SEM:
    - Edge 27.50 − b must lie within 22.01 ± 3.41, so b is 2.08 to 8.90.
    - S90 16.99 − b must lie within 10.69 ± 1.94, so b is 4.36 to 8.24.
    - P180 12.66 − b must lie within 4.87 ± 1.15, so b is 6.64 to 8.94.
  - The squares give 8.78, only 0.54 above that range. The statements hold only for exact values.
  - The Edge difference is response minus baseline, like the other folds, so "not baseline-related" has no basis.
- **Cell 86:** "`smoothed_image_norm` is normalised by `BaseActivity` in three different ways or none". Cell 11 shows two relations (difference in 5 files, index in 12) and "other" in 21.
- **Record finding (metadata_insufficient):** "`BaseActivity` (… in 40 files …)". Cells 3 and 25 give 38 files (19 + 9 + 10). The same finding says `norm` is 0 "in every file that has it", but 74 files have it and only 73 were read (cells 3 and 11).
- **README:** "The baseline comparison and the Table 1 Edge and S90 outcomes depend on where the baseline squares are placed". The baseline comparison (s4) does not depend on placement: both placements find a difference (cell 34). It depends on squares against `BaseActivity`.
- **Cell 26:** "no placement of 16 x 16 DU squares tried while preparing reproduced `BaseActivity` (not run here)". There is no output for this. It is labelled as not run, so it is unverifiable but not misleading.

Every other number I checked in the "**Result:" cells (31 to 82), the record's notes and the remaining README rows matches the outputs.

The record's verification block states my round-1 reasons faithfully and in my own words, including the B-points I attached to each outcome.

**Claims file:** as in round 1, neither RMS-contrast reading in the claims file can produce the paper's 0.61 to 0.943. Reading (b) cannot exceed 0.5. The record says so and has put the question to a reader.

**3. Round-1 points**

- **Resolved:** B5 (grid-step variant, assumption flagged), B6 (`norm` is 0; `smoothed_image_norm` is neither an eye time nor a count), B7, B8 (refit run, cannot place the levels), B9 (concentric maps confirmed). B10 and B11 are stated, as before.
- **Resolved as far as the data allow:**
  - B1: the centred variant and a per-file baseline listing were added.
  - B2: the 12 registered Star maps do not differ from the 16 unregistered ones in gaze-frame peak (p = 0.49) or median (p = 0.75), with the caveat stated in cell 23.
  - B4: a physical-luminance variant was run; no black level gives the paper's curve; the question is with a reader.

What remains that bears on a conclusion:

1. **table1-edge and table1-s90** turn on inside versus centred squares. The reason given for "inside" is weak. These two outcomes should be read as "not reproduced or partially reproduced, depending on an unresolved placement".
2. **B3** was investigated, but cell 42 and the fig4b notes draw the wrong conclusion. A single mean baseline about 0.5 to 2 spikes/s lower, plus the three missing neurons, is consistent with all three Square and Edge midpoint gaps.
3. **The Corners baseline placement** is still the only one tried. It underlies every S40 value (fig4b, pairwise, table1-s40, fig7c, fig7d). The `BaseActivity` cross-check on 19 neurons gives the same outcomes, which limits the risk.
4. **s4** still rests on squares rather than `BaseActivity`. This is stated, but the conclusion carries low confidence.
5. **Wording fixes:** the assumed flags (table1-s52, table1-s40, s4) and the misstatements listed in section 2.
