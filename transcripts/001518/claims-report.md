I wrote `claims/001518/10.1016-j.bioelechem.2026.109283.yaml`. The quote checker passes it with 0 problems: 30 claims, 30 quotes, 9 statistical values. Nothing is committed.

**Text read:** the version of record (Bioelectrochemistry 171, 109283), from a PDF a person supplied: main text, Methods, Results, Discussion and the legends of Figures 1 to 7. The paper names no supplement and links no code. Its analysis used MetaMorph, an Excel macro, Grapher and Origin, none of them published, and "Data will be made available on request". So I read no code, and no method detail was settled by code. I did not open any figures.

**Claims:** 30, all with quotes and none `inferred`.
- **Statistics:** 7 claims carry 9 entries. They are paired and unpaired t-tests (2-tailed or single-tailed) and one-sample t-tests, all reported as bounds (p < 0.05, < 0.01, < 0.001, > 0.05).
- **`expected`:** 21 claims carry reported values. Where the paper gives a ± s.e., that is the tolerance; otherwise it is 10%, and ranges are widened by 10% of each bound.
- **Criteria:** all 30 claims have one. The four claims of absence (stability in Fig. 2A, 2C/D; the equator following the cosine in Fig. 4C; linearity with Gd3+ in Fig. 5A) are judged on the t-tests named in the Methods and legends.

**Details the paper leaves open, with the readings named:**
- **Pole position:** Fig. 4C puts the equator at −90°/270° but the Results say 0°/270°. The poles are taken from the field direction recorded with the data; if the data don't record it, this stays open.
- **Laser images:** no background subtraction is stated. Readings: none, or a cell-free region (as is done for the Ca2+ images).
- **Cell radius:** the method isn't given. Readings: perimeter/2π, or the radius of the circle of equal area.
- **Correlation coefficient of the fit through the origin (Fig. 3):** Pearson r, or √(uncentred R²).
- **FluoVolt non-linearity (Fig. 3):** the paper judges this by eye from a LOESS smooth with no span given. Readings: spans 0.3, 0.5 and 0.75, or 50-mV bins. A departure is the smooth falling more than 10% short of the line; that threshold is my own choice (the protocol's 10% default), not the paper's.
- **"Start" and "end" of a set (Fig. 2):** the first and last image, or the first and last 10 images.
- **Pole and pooling for the ~20% drop (Fig. 2D):** cathodic or anodic pole; each later set or their mean. The legend's "≤20%" wording is also accepted.
- **Which datapoints are compared for Gd3+ (Fig. 5A):** the group minima, the same field strength, or each cell's own minimum. The legend's "above 1200 mV" is read as IMPC on the x-axis.
- **Fig. 5B reduction relative to IMPC:** 1 − f/1.5, or relative to the intact f.
- **Normalization and pole in Fig. 7B:** per cell or of the means; each pole or both poles together. The Fig. 7 test is read as a one-sample t-test against 100% or a paired t-test.
- **Ca2+ data (Fig. 6):** "strong response" is undefined. Readings: 3 s.d. above baseline, dF > 50%, or dF > 100%. "End of recording" is the last frame, the last 10 s or the last 30 s. The test for the single-pulse data isn't named; the one-sample t-test the paper uses elsewhere is applied.
- **Smaller gaps:**
  - "Near the equator" in Fig. 4C has no angular range given; readings are ±15° and ±30°.
  - The 560/760 V/cm in the Fig. 7 Results are read as the same levels as 570/780 V/cm elsewhere.
  - Whether Figs. 2 and 4 used the same cells is not stated.

**Missing from the paper:** the fit of τ against cell radius, which Eq. 1 needs to calculate IMPC. It is only in reference [20] (Semenov et al., Bioelectrochemistry 168 (2025) 109143), which I did not read. The 9 claims that use IMPC are marked `data: with_inputs` for that reason. Most other methods are also deferred to [20]. No supplement or Methods section that the results rest on is missing.

When I worked Eq. 2 through as printed, a 10-fold conductivity rise gives about a 1.3% drop in IMP, against the paper's "~2%". That would fail the 10% tolerance in `fig5b-conductivity-calibration`, but I left the claim as the paper states it.

The dataset's title and description cover the FluoVolt and Di-8-ANEPPS experiments. It may not hold the Gd3+, Ca2+ (Fig. 6) or two-pulse (Fig. 7) data; checking that is the author's job.
