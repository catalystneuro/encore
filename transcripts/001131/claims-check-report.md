I checked the claims file for DANDI:001131 and I've marked it ready. It now has 36 claims, up from 34. Nothing is committed.

**Checker:** `claims/001131/10.1016-j.cell.2024.08.015.yaml: 36 claims, 36 quotes, 32 statistical values, 0 problems`

**Changes, by claim**
- **Header:** The file recorded p < 0.05 for most significant results. When a figure legend's star key starts at `**p≤0.01` (Figures 2, 4, 5, S3, S4, S6), every significant panel in that figure is at p ≤ 0.01. The header now says so, and p < 0.01 is recorded for those figures.
- **fig2g-bilateral-editing-reduces-aggression:** Statistics split in two. Figure 2G is a Mann-Whitney test at p < 0.01. S2B-C is a nested Mann-Whitney test at p < 0.05.
- **fig2-bilateral-editing-spares-sniff-and-mating:** The criterion now gives the scored windows from the Methods (15 min with males, 10 min with females) and the rule that mice with at most 1 bout are left out of the interval measures. It also says the percentage of mice mounting is a group proportion with no per-mouse test.
- **fig4ef-male-activity-slightly-lower**, the z-scored entry of **fig4ef-female-activity-unchanged**, and **fig4d-sex-decoding-intact:** p raised from 0.05 to 0.01 (star keys of Figures 4 and S4).
- **fig5ac-behavior-activity-male-lower:** Figure 5A and 5C set to p < 0.01. S5B is now a separate entry at p < 0.05.
- **fig5e-cp-tuning-shift:** The 28.8% and 41.1% values are assigned so that the fraction increases, as the text says. Elsewhere in that section the paper lists the experimental value first, which would give the opposite. That other reading is reported but does not decide.
- **fig6a-control-tau1-greater:** The Figure 6 legend names no test after Kruskal-Wallis. The criterion now has two readings: Kruskal-Wallis alone, or Dunn's comparison of dimension 1 with dimension 2. Dunn's is the follow-up test the paper uses with Kruskal-Wallis in the S1F and S7 legends.
- **figs7b-achw-female-slight:** The file named nested Mann-Whitney and Kolmogorov-Smirnov tests, but the S7 legend does not name them. The test is now recorded as not named. The Figure 7C tests are run for reporting only.
- **figs7cd-slice-rslds:** The paper's numbers disagree: 90 s over 15 s is 6-fold, not 8–9-fold. The ratio is reported and is no longer an expected value.
- **Added fig3d-cre-editing-spares-mounting** (Figure 3D, S3D) and **figs7l-blockers-slight-effect** (Figure S7L). Both are findings in the Results that had no claim. The S7L claim records no p-value, because the text does not call the effect significant.

**Still open (listed under `checks`)**
- The S7B, S4A and S6E star levels were read from the supplement images by the first reader. I could not open those images (pdftoppm, the PDF-to-image tool, is not installed), so they are unverified.
- **fig4c-pls-sex-separation:** The thresholds for "clear separation" are not from the paper: the sign of the mean PLS1 score, and a ROC area above 0.75 or below 0.25.
- **fig6g-flow-field-line-vs-point:** The flow-field shape is judged by the line attractor score in a majority of mice. The paper does not state this proxy, and the claim largely repeats fig6f.
- **rSLDS and decoder claims:** Several values fill details the paper leaves open, and the file names each as a reading. These are variance explained as the R² of the reconstruction, seeds 0 to 3, the forward-simulation horizon and folds, and the decoder's C values.

**Ready:** yes (`ready: true`). Every open detail is named as such, with the readings the paper allows.
