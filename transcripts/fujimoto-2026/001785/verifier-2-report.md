**Verifier report, round 2: Fujimoto et al. 2026 on DANDI:001785 (0.260615.1835)**

The claims file has 35 claims and the attempt record has 35 outcomes: 24 reproduced, 1 partially reproduced, 2 not reproduced and 8 blocked. These match my round-1 outcomes claim for claim.

### 1. Outcomes

I agree with all 35 stated outcomes.

- **`assumed: true`.** No outcome in the record carries it any more. For ed6b the flag was removed because the 40-field design now gives the same outcome under all four readings (cell 97). That is right.
- **Basis of the IF outcomes.** fig3c, ed5, ed6a and ed6b all rest on the author's own counting pipeline. Their results hold under every reading, and the claims file sets no dependency on link-if-counts, so none of them turns on a single chosen value. The notes state the approximation.
- **fig6c.** Blocked as methods_underspecified is reasonable. The size filter is the author's parameter, but the paper gives none, and it reverses the outcome: p 0.31 at 10 pixels against 0.044 at 50 (cell 99).
- **fig5a-control-group-no-reduction.** Blocked is right, because reading (a) cannot be run. The record's argument that leaving out the cluster correction can only add clusters holds: the >20-voxel minimum is the paper's (Fig. 5a legend), and the correction is an extra requirement on top of it.
- **Weak support for ed6b.** It is a claim of absence, and it rests on counts that fail the link in that region under every reading (cell 82: UF-FM `holds` False ×4; CC1 r 0.69 at 10 pixels). The outcome follows the criterion, but its support is weak.

### 2. Sentences the printed numbers do not support

1. **Cell 35, and the record's notes for fig5c-network-decreases:** "With the Methods' LIM (no area 25) the LIM still falls (p printed as 0, below the floor)".
   - Cell 34 prints p = 0.0 for every network in that variant, together with scipy's `IntegrationWarning: The integral is probably divergent`.
   - p = 0.0 there is an integration failure, not evidence that p lies below the floor. "Below the floor" is unsupported; "not computable" is what the output shows. The outcome is unaffected, since this is a variant.
2. **Summary (cell 107):** "The counts match the paper's in three of four regions, under different size filters, and in none under one reading".
   - Read literally, "in none under one reading" is false. At 10 pixels the link holds in two regions (cell 82 rows 0, 2, 4 and 6).
   - Cell 82 supports "under no single reading in all four", which is the wording cell 84 uses.
3. **README:** "an automatic approximation of the paper's FIJI counts that matches them in three of the four regions".
   - This reads as one procedure. Cell 82 prints "readings under which it holds in every region: none". The three regions need different size filters: 10 pixels for N and T, 50 for D.
4. **Record notes for ed6a:** "they correlate with the paper's at r = 0.98 for each channel but run 8 to 14% higher".
   - This is true at 10 pixels only. At 50 pixels the counts run 9–21% lower (CC1 0.792, DAPI 0.907; cell 82). The sentence should name the reading.
5. **Record notes for link-fa-voxels, and the finding on repeated voxels:** "each repeat is the same value listed twice … no voxel is matched by two different values", with the example "904 values over 833 distinct voxels for the pre-DBS tracts of N".
   - Cell 9 checks only within a monkey × session × side × tract group, and finds 99 repeats in total over all four whole_NT sessions.
   - Counted per session, cell 8 implies 71 + 112 + 68 + 122 = 373 repeated voxels for whole_NT. So at least 274 voxels are shared between different tracts or sides within one session. These have not been examined: they may be overlapping tract masks or collisions among the 624 ambiguous nearest-value matches.
   - The example in the finding therefore mixes within-group repeats with cross-group sharing that was never checked. This does not bear on a conclusion, because the tests use values only.
6. **Cell 50:** "this fits a local increase at the implantation site". This is interpretation. The claims file says the local increase is to be reported, not judged, and the printed numbers (top-10 changes, mean change +0.0008) do not test it. It does not bear on a conclusion.

Every other "**Result:**" sentence I checked (cells 16, 20, 23, 26, 29, 32, 38, 41, 44, 47, 53, 56, 59, 63, 66, 69, 72, 75, 78, 84, 88, 91, 94, 97, 100, 103 and 106), the rest of the Summary, the README table (its claim counts add up to 35) and the record's other notes matches the printed outputs.

**My round-1 reasons in the record.** The `verifications` block states them faithfully and mostly in my words. Each reason carries its B number, and the request from section C (scatter plots, channel check) is included.

### 3. Round-1 points

**Resolved**
- **B1 (fig6c):** now blocked as methods_underspecified, and cell 100 states that the two readings disagree.
- **B2 (N122 RW6):** the main test uses 40 fields per hemisphere with df 76, and the sixth field is a variant.
- **B4:** "re-runs the paper's statistics on its own data" is now stated in cell 59, the Summary, the README and the record notes.
- **B5:** the match path for each value is printed (199 exact, 6133 nearest). 641 values are ambiguous, and their candidate values differ by at most 1.6e-6.
- **B6:** the floor of scipy's studentized range is stated. The new wording "below the floor" is wrong; see 2.1.
- **B7:** this is as far as the data allow. D has one map per session, so no thresholded map can be made, and the unthresholded change is reported instead.
- **B8, B10, B11, B12:** resolved. The two files in 001773 are named, the column headers are printed, the DAPI misprint is recorded as a finding, and fig3f now gives its reason category.
- **B9:** reading (b) is run without the cluster-level correction. It finds no negative cluster above 20 voxels (cell 55).
- **Section C:**
  - The scatter plots are in cell 83, and I viewed them.
  - The channel check is in cell 82: red counts follow the sheet's CC1 column and lie below blue.
  - The EM sheet has no axon positions (cell 12), so fig3f stays blocked.

**Remaining that bears on a conclusion**
- **B3, the counting pipeline.** It is now stated openly but is unchanged. It still bears on:
  - **ed6a (not reproduced).** The ratio is significant under every reading, while the paper's own counts give p = 0.090. The scatter plots show a level offset in this region, and the stimulated-side DAPI counts are higher by 9–13 cells per field. The not_reproduced outcome may come from the method rather than the tissue, as the record now says.
  - **ed6b (reproduced).** This claim of absence rests on counts that fail the link in the UF-FM overlap under every reading. The smallest p is 0.0685.

Nothing else bears on a conclusion. Items 2.1–2.6 are wording fixes.
