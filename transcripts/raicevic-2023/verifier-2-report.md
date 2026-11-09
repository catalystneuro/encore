**Round 2 verification: 000491-raicevic-2023-01**

The claims file has 22 claims and the attempt record has 22 outcomes:
- 7 reproduced
- 4 partially reproduced
- 8 not reproduced
- 3 blocked (segmentation-validation-overlap for missing data; fig5bc-area-intersegment-variation and left-right-no-difference because the methods are underspecified)

I found no place where the claims file misreads the paper.

## 1. Outcomes and assumptions

I agree with all 22 stated outcomes as the criteria decide them. Several need caveats:

- **ellipse-annulus-underestimate (reproduced):** this rests on one combination of 48 (P1 b, P4 a, erosion 1, P5 b, outliers out; cell 45). Across all 48, the ratio of the two peaks ranges from 0.038 to 2.259, so that one match is not robust. The record says this.
- **fig9a-heights-taper (reproduced):** this rests on 1 of 48 combinations (cell 69). The H1/R1 peak ranges from 0.343 to 1.445 across combinations, and by median H1 is about 2.3 times H3, not 4. The record says this.
- **fig5d-polynomial-closest-area-ratio (reproduced):** this rests on 4 of 96 combinations, all of which pair the segmented vessel area for the segmentation with the fitted circle for the fits. The ellipse share in them, 7.9 to 8.8%, sits at the edge of the tolerance band (7.2 to 8.8), while across all combinations it runs from 0.1 to 32.2%. The record states that the outcome rests on these four.
- **fig5b-polynomial-closest-resistance (partially reproduced):** this would become reproduced if logarithmic bins are allowed. Two combinations meet the full rule on log bins (cell 42). The question is with a reader.
- **Location E affects every pooled claim.** The cleaned E path follows a side branch of the vessel network, not the main artery (cell 9 projection). E's example cross section shows a tiny vessel with no PVS lobe, only the grey band (cell 9, second figure). E contributes 202 of the 6683 pooled cross sections (P1 a, P4 b). This is recorded only as a dataset finding, not as an assumption that the outcomes rest on.

Every outcome marked `assumed: true` states its assumptions:
- the path cleaning;
- taking the PVS as the two lobes beside the vessel;
- clearing planes the PVS mask fills;
- how the polynomial region is closed across the vessel.

All four are reasonable stand-ins for steps the paper leaves open, with two qualifications:
- The path cleaning leaves the path still longer than the vessel it follows (see 2d and section 3).
- The lobes deviation misquotes the Methods. It says the segmentation "kept 'all but the two largest regions in the PVS segmentation'". The paper says "removed all but the two largest regions", meaning it kept the two largest.

## 2. Statements the printed numbers do not support

- **a. Cell 37 and the fig6b-resistance-segmentation-peak notes:** "The peak is within tolerance in one combination, 1.68e15." Cell 36 shows three combinations within 1.557e15 to 1.903e15:
  - 1.86e15 (P1 a, P4 a, P7 a, log bins);
  - 1.68e15 (P1 a, P4 b, P7 b, linear bins);
  - 1.83e15 (P1 b, P4 b, P7 b, linear bins).

  The outcome does not change, because the median is outside tolerance everywhere.
- **b. A deviation repeated under fig5d, table2, fig5b, ellipse-annulus, fig7 and fig8:** "Table 2 reference polynomial peak 1.749 before, 1.752 now; median unchanged at 1.901". Cell 30's reference row gives a peak of 1.684 and a median of 1.710. The value 1.901 appears nowhere in the outputs; 1.752 appears only in the erosion-5 row.
- **c. Record finding on the depth step of L, M and N:** "median height over width 0.93 to 1.12". Cell 5 gives 0.91, 1.08 and 1.13.
- **d. Cell 10:** "most of the excess length that remains is the zigzag of a path of 26-connected voxels". From cell 9, kept points × mean step ÷ kept end-to-end distance is:
  - B 1.78, H 1.59, I 1.54;
  - F, N 1.42 and 1.41;
  - J, A, C 1.35 to 1.36;
  - all others 1.25 to 1.29, except G 1.13.

  Voxel zigzag adds at most about 8% on a straight line, so most of the excess is the path still meandering. The visibly jagged paths in the cell 9 projection agree.
- **e. Cell 10:** E's "cross sections show a thinner vessel than the paper's". Cell 54 gives E the largest median R1 of all 14 locations (40.9 µm), and the notebook prints no per-location values from the paper to compare with.
- **f. README:** "Every reading of the claims file's open method details is run, and the tables show each." P2 reading b (all skeleton points) is run for the counts only, as cell 0 says.
- **g. area-ratio-per-location notes:** "Before the revision … at most 11 locations met a reading". My round-1 report said at most 10. The verifications entry correctly says 10.

Everything else checks against the outputs:
- the other "**Result:**" conclusions;
- the Summary table, including "changed five outcomes" (fig5e, fig5bc, fig5d, fig6b, fig9a);
- the README table;
- the other record notes and measured values.

The attempt record states my round-1 reasons accurately and in my own terms. Problems 1, 2, 3, 5, 6, 8 and 9 are attached to the right claims, and problems 4, 7 and 10 are answered under cross-section-counts.

## 3. Round-1 points

**Resolved:**
- 4: the edge distance is now measured from the vessel centre in the slice.
- 5: the fits are solved at every erosion.
- 7: D's depth axis is kept. Its whole-plane intensity falls with depth in every channel and its PVS lies above the vessel, which is a sound argument.
- 8 and 9: both are stated in the conclusions.
- The truncated tables: compact tables have been added.
- 6, as far as the analysis can go: the rule is now stated, and the open question is with a reader.

**Partly resolved:**
- 1 (centerline): cleaning keeps 7534 of 9564 points. But the path remains 1.25 to 1.78 times its end-to-end distance in 12 of 14 segments (point 2d), and E follows a branch.
- 2 (PVS content): the lobes are now 91 to 99% of each slice's PVS except at E (29 to 52%) and at 1 µm voxels H (70%). F's lobes still join the band along the bottom of the slice.
- 3 (fragility): fig6a and spline-five-times now hold under P4 b, with all 14 segments. ellipse-annulus still rests on one P4 a combination, and fig9a and fig5d now rest on 1 and 4 combinations.
- 10 (overlap): quantified but not run. The overlap is above 5% of the PVS in 247 of 485 slices at J and 131 of 202 at E, which is not small at those two locations.

**Still bearing on a conclusion:**
- **Path meander (cross-section-counts):** with a path close to the vessel's real length, the largest count (604, now above the 496.1 limit) would fall to about 500 or below. The outcome could change.
- **Location E:** its cross sections are of a branch, with PVS that is mostly not lobes. This affects every pooled distribution and E's per-location values.
- **The bins question (fig5b):** the outcome turns on whether logarithmic bins are allowed.
- **Outcomes resting on one or a few combinations:** ellipse-annulus-underestimate, fig9a-heights-taper and fig5d-polynomial-closest-area-ratio.
