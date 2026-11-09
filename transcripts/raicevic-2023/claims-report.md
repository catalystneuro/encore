I wrote the claims file `claims/000491/10.21203-rs.3.rs-2587250-v1.yaml`. The quote checker passes: 22 claims, 22 quotes, 4 statistical values, 0 problems. Nothing is committed.

**Text read.** I read the Research Square preprint, version 1, as served by PubMed Central (PMC9949243). It has the full Methods, Results, Discussion, figure legends and Tables 1 to 3. I did not read the version of record (Fluids and Barriers of the CNS, 2023). Additional Files 1 to 6 were not supplied:
- **Additional File 1** is the full description of the segmentation. The main Methods describe the approach, and the dandiset holds the final segmentations, so the claims start from those.
- **Additional Files 2 to 6** are figures. The per-location numbers the claims use are stated in the main text.

The paper links no code, so no repository was read and no detail is settled by code. The dandiset's description (14 datasets from 9 subjects, raw stacks plus final segmentations) maps its subjects to the paper's mice 1 to 9 and locations A to N. That mapping is in the opening comment.

**Claims.** All 22 are findings and all 22 have quotes; none is `inferred`.
- **Statistics:** 2 claims have them, both 95% confidence intervals: the slope of PVS area on vessel area (0.973 to 1.12), and the power-law exponent of resistance on area (−1.763 to −1.737). The paper reports no p-values.
- **Criteria:** all 22 have one, and 18 also have expected values.

**Details the paper leaves open, and the readings named.** The ones shared by many claims are written once, as steps P1 to P9 of a pipeline in the opening comment:
- **Isotropic voxel size:** 0.648 µm or 1 µm.
- **Centerline points removed by hand:** the longest skeleton path, or all skeleton points.
- **"Median PVS width" in the edge-exclusion rule:** the horizontal extent of the PVS segmentation, or the polynomial-fit width W.
- **Vessel area in the segmentation's area ratio:** the segmented vessel area, or the fitted circle's area.
- **Erosion of the convex hull in the circle fit:** 1, 3 or 5 pixels. The circle-fitting method is not named; I used a standard least-squares fit.
- **Range of the 20 bins for a distribution peak:** all values, or values after removing outliers. For resistance, also linear or logarithmic bins.
- **Ellipse-fit PVS region:** the ellipse minus its overlap with the circle, or ellipse area minus circle area.
- **Spline type** (cubic interpolating used as a standard choice), and **which pixels count as polynomial-fit edge points** (one reading given).
- **Slice orientation:** top toward the brain surface. This is my reading of the figures; the paper does not state it.
- **Per-claim details:**
  - Whether the area-on-area fit has an intercept.
  - Whether the power law is fit on log or linear scales.
  - What "within 30% / 37% of the peak" measures (three readings each).
  - What "much larger between segments" means (two readings).
  - The units of the offsets Ov and Oh (over R1, over R3, or µm).
  - Whether velocity means maximum or mean.
  - Which test showed no left/right width difference (three named tests).
  - Whether the heights pool both sides or average them.
  - What "very similar" means for the annulus and ellipse.
  - The representative cross section of Figure 7, which is not identified, so that claim is tested over all cross sections.
- **My own choice:** the tolerance on HC/R1, whose peak is near zero (0.1, the scale of the paper's 0.5 R1 statement). It is marked as a deviation.

**Problems in the paper itself.**
- **Table 2:** the 25th and 75th percentiles and IQRs of resistance are garbled in the text (the 75th percentile is printed below the median), and no PDF was supplied to check them. They are not used.
- **Table 3:** its dimensional values (R1 peak 64.9 µm) conflict with the 28 µm vessel radius peak given in the Results and Discussion. Only its ratios are used.
- **Width ratios:** one Results sentence says WS/R1 peaks at 1.85, but Table 3 gives that value for WL/R1. Table 3 is followed.
- **Spline resistance:** the text says the spline peak is 5 times the segmentation's, while Table 2 gives a ratio of 6.2. Both are named as readings.
- **Annulus formula (Equation 3):** garbled in the text. It is read from the cited Tithof et al. paper and the units.
- **Units:** the abstract gives resistance in Pa·s/m⁵, the tables in Pa·s/m⁴. The claims use m⁴.

**Missing data.** The segmentation-validation claim (at least 70% overlap with the 2D time-averaged images) needs the 2D images and their segmentations. The dataset description does not mention them, and the paper does not give the alignment method (it cites reference 31).
