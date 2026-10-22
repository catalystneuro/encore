I wrote the claims file at `claims/001525/10.1016-j.bioelechem.2026.109283.yaml`. `tools/claims_check.py` passes with 0 problems: every quote matches word for word and all 9 p-values are found in the text. Nothing was committed.

**Text read.** I read the version of record (Bioelectrochemistry 171 (2026) 109283), from a PDF supplied by a person, as extracted text. That covers the main text, Methods, Results, Discussion and figure legends. The paper has no supplement and links no code ("Data will be made available on request"). I could not open any PDF page because no renderer is installed here. The extracted text garbles Eq. (2); I read it as the Kotnik thin-shell formula. That reading gives f = 1.5 for an intact membrane and the paper's 12% IMP drop for a 100-fold rise in conductivity, which confirms it.

**Dataset.** By its archive title and description, DANDI 001525 holds the membrane-recovery experiment after 1-µs electroporation. That is the two-pulse protocol of Section 3.7 and Fig. 7. Claims for the other figures are included because they are the paper's main findings.

**Counts.**
- 27 claims, all with quotes and all with criteria.
- 7 claims carry statistics, 9 entries in all.
- 20 claims have expected values with tolerances. Where the paper gives a s.e. I used it as the tolerance, otherwise 10%. One exception: the "~2%" figure gets half its last digit (0.5 point).
- 12 claims are `with_inputs`, because the calculated IMP needs the fit of time constant against cell radius from ref. [20] (Semenov et al. 2025, Bioelectrochemistry 168, 109143).
- Six claims cover Fig. 7: test pulse still cosine up to 1000 V/cm; conditioning pulse 1.5 and 2-fold below linear; test pulse unchanged up to 760 V/cm; test pulse at about 70% and 50% after 1200 and 1400 V/cm; conductivity dropping about 10-fold (range 7 to 20); full resealing after mild pulses.

**Details left open, with the readings named:**
- **Fig. 7B:**
  - Which pole the numbers refer to: cathodic, anodic, or the mean of both.
  - How the 150 V/cm normalization is applied: per cell with a one-sample t-test, or on group means with a two-sample test.
  - What the test compares for the absence claim. I set the tie-break to the per-cell reading.
- **Fig. 7C:** what "most datapoints" means. I read it as more than half of the pole and strength pairs with a finite fold change.
- **Fig. 2:** where a set "begins" and "ends" (first and last image, or first and last 10), and how within-set stability is measured (first 10 against last 10, or a regression slope).
- **Fig. 2D:** which pole the 20% drop refers to.
- **Fig. 3:**
  - The correlation coefficient for a fit through the origin: Pearson r, or the root of the uncentred R².
  - The LOESS span: 0.3 or 0.5.
- **Fig. 1 and 4C:** how far from the pole "closer to the equator" is: arcs at 30, 45 or 60 degrees from the pole (Fig. 1), or within 20 or 40 degrees of the equator (Fig. 4C).
- **Fig. 5A:** what the extreme IMP is: the per-cell extreme averaged over cells, or the extreme of the group mean.
- **Fig. 6A:** which time point is tested: the peak, or the end of the recording.
- **All figures:** how the cell radius is measured (perimeter over 2π, or equal-area radius), and whether background is subtracted from the dye images. I also named a 10% band, the protocol default, for "matched" and "nearly identical", since the paper gives none.

**Missing from the paper:**
- **Ref. [20]:** the coefficients of the time-constant fit, and the resampling macro, are only there. That paper is not under `paper/`.
- **"Strong" Ca²⁺ response (Fig. 6B):** never defined, so the 28% and 5.9% responder fractions can only be judged if the dataset marks responders. Otherwise they are blocked as `methods_underspecified`.
- **Field-strength labels:** the paper names the same strengths 570 and 780 V/cm in most sections but 560 and 760 V/cm in Section 3.7. The criteria take the dataset's nearest label.
- **Fig. 7B top panel:** the paper reuses the Fig. 4B data, which may not be in this dataset.
- **Pole-difference test (Fig. 7C):** the paper names no test for "no difference between the poles". I named a paired t-test as the Methods' Student's t-test applied to the two poles of the same cells; the second reader should look at that choice.
