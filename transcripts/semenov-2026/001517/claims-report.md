I wrote `claims/001517/10.1016-j.bioelechem.2026.109283.yaml`. The quote checker passes it: 31 claims, 31 quotes, 9 statistical values, 0 problems.

**Text read.** I read the version of record, extracted from a PDF a person supplied. It has the main text, Methods, Results, Discussion and the legends of Figures 1 to 7. The paper names no supplement and links no code: data are "available on request", and the analysis was done in MetaMorph, an Excel macro, Grapher and Origin. So there was no code to read. I didn't open the PDF.

**About the dataset.** Its archive title and description say it holds the Di-8-ANEPPS strobe-imaging experiments, most likely the stability tests of Fig. 2B to 2D and the Di-8-ANEPPS figures. The file still covers all the paper's main findings: FluoVolt, Gd3+, Ca2+ and the two-pulse recovery experiments.

**Relation to the 001518 file.** The same paper already has a checked claims file for dataset 001518. I read it, checked it against the paper, and reused its readings where the paper allows them. I made two changes:
- **Paired or unpaired test.** In two claims of absence, `fig4c-equator-follows-cosine` and `fig5a-gd-linear`, the 001518 file used a paired t-test that the paper never names. Here the paired and unpaired Student's t-test are both readings. If they give different outcomes, the claim is blocked as underspecified.
- **New claim, `fig2b-di8-bleaching`.** The roughly 5% bleaching shift at 43 V/cm in Fig. 2B now has its own claim.

**Counts.**
- 31 claims, all quoted, none inferred.
- 7 claims carry statistics, 9 entries in all.
- 19 claims have expected values. Tolerances use the paper's s.e. where it gives one, otherwise 10%.
- All 31 have a criterion.

**Details the paper leaves open, with the readings named:**
- **Background subtraction of the laser images:** none, or a cell-free region subtracted as for the Ca2+ images.
- **Cell radius:** perimeter divided by 2π, or the radius of the circle of equal area.
- **"Start" and "end" of a set:** the first and last image, or the first and last 10 images.
- **Which pole, and how the ~20% drop is pooled (Fig. 2D):** cathodic or anodic pole; each set alone or their mean; the reference is the first set or the mean of all earlier sets.
- **How the bleaching shift was measured:** last 10 pulse images against the first 10 pulse images, or against the first 10 baseline images.
- **Grapher's correlation coefficient for a fit through the origin:** Pearson r, or the square root of the uncentred R².
- **LOESS span (not given):** 0.3, 0.5 or 0.75, or 50-mV bins.
- **Student's t-test, paired or unpaired:** Fig. 4A, 4B, 4C and 5A.
- **Arc width for "near the equator":** ±15° or ±30°.
- **Which Gd3+ datapoints are compared:** three readings.
- **Fig. 5B reduction:** 1 − f/1.5, or relative to f at the intact conductivity.
- **"Strong" Ca2+ response:** 3 s.d. above baseline, ΔF above 50%, or above 100%.
- **Ca2+ windows:** for "by the end of recording", the last frame or the last 10 s or 30 s; for the single-pulse test, the peak frame or the last 30 s.
- **Fig. 7 normalization:** per cell or of the means; each pole or both poles together.
- **Fig. 7 test:** one-sample or paired.
- **Fig. 7C counting:** whether fully resealed points count toward "most datapoints".

Some criteria still have no rule from the paper and use thresholds of mine, named as readings: the conditions for Fig. 1 and for the Gd3+ "prevented decline", and 90% for "nearly all" cells.

**Missing from the paper that claims need:**
- **Calculated IMP (IMPC).** It needs the fit of time constant against cell radius from reference [20] (Semenov et al. 2025), which this paper doesn't give. The claims that use IMPC are marked as needing outside data.
- **A discrepancy for the attempt to report.** Eq. (2) with the Methods constants gives about 1.2 to 1.3% IMP reduction for a 10-fold conductivity rise, against the paper's ~2%. That figure comes from the 001518 file's check; I didn't recompute it.
- **No deposited data.** The paper deposited no data elsewhere.

Nothing was committed.
