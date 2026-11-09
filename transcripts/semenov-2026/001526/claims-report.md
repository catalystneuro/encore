I wrote the claims file, `claims/001526/10.1016-j.bioelechem.2026.109283.yaml`, and it passes the quote checker: 30 claims, 30 quotes, 9 statistical values, 0 problems. Nothing was committed.

**Text read:** the version of record (Bioelectrochemistry 171, 109283), as text extracted from a PDF a person supplied. It has the main text, full Methods, Results, Discussion and figure legends. The paper has no supplement and links no code, so there was no code to read. Its Data availability statement says "on request". I read no figures from the PDF, because the tool that renders PDF pages is not installed.

**Claims:**
- 30 claims, all with quotes and none `inferred`.
- 9 carry statistics: Fig 2C, Fig 2D, 5A anodic, 5A legend, 6B, 7B top and 7B bottom (two tests). One claim has two entries.
- 20 have expected values with tolerances. The tolerance is the paper's s.e. where it gives one, otherwise 10%.
- All 30 have criteria.
- They cover Fig 1 through Fig 7C and Gd3+, the Eq. 2 model, Ca2+ uptake with single pulses and trains, and the two-pulse recovery tests.
- The dataset's title points to the Fig 2 type experiments. Every claim still keeps the default data (`dataset`) unless it needs outside inputs.
- 7 claims are `with_inputs`. They need the fit of charging time constant against cell radius from Semenov et al. 2025, *Bioelechem.* 168:109143 (ref [20]), and this paper does not give that fit's coefficients.

**Details the paper leaves open, and the readings named:**
- **Applying to all claims:**
  - How the radius is measured: perimeter length over 2π, or the radius of a circle with the same area.
  - Whether background is subtracted from the dye images: none, or a cell-free region as is done for the calcium imaging.
  - How the perimeter trace and cell centre are drawn: by hand in the imaging software, not fixed.
- **Fig 2A, 2B (stability within and across sets):** the paper names no test. Readings are a linear-regression slope, or a paired t-test of the first half against the second half. For the within-set decline: the first 10 against the last 10 images, and which pole (cathodic, anodic, both).
- **Fig 2B bleaching:** an extrapolated drift of the baseline, or the first against the last 10 images.
- **Fig 2C:** what "beginning" and "end" of the set mean: one image, 10 images or 5 images.
- **Fig 2D:** which pole, and whether the 20% is the mean over sets or per set.
- **Fig 3:**
  - Which cells form the calibration: the Fig 4A/4B groups, or all cells.
  - Whether r is for the through-origin fit or a Pearson r.
  - The linearity test: one-sample t-tests per 50 mV bin, or a cubic term in the fit.
- **Fig 4C:** how far "near the equator" reaches: ±30° or ±45°.
- **Fig 5A:**
  - How the extreme value is taken: the most negative group mean, or a per-cell extreme.
  - "Nearly identical to theory": a one-sample t-test, or within 10%.
  - The legend's −700/1200 mV: which axis.
- **Fig 6A:** which test (one-sample, or against the 0 V/cm group) and which time point (the peak, or the end of recording).
- **Fig 6B:** the end of recording (last frame, or last 10 s).
- **Fig 7B:**
  - Normalization: per cell, or of the group mean.
  - The test pulse's "two-way t-test": one-sample against 100%, or two-sample against the 150/150 V/cm control.
  - Which pole.
- **Fig 7B naming:** the 560/760 V/cm in Fig 7 are read as the 570/780 V/cm sets of Fig 4B.

Where readings give different outcomes, the claim is blocked as `methods_underspecified`. Fig 4C and Fig 5A use the protocol's default 10% band as their measure, and I say so in those criteria.

**Missing from the paper:**
- The coefficients of the fit of charging time constant against radius. They are in ref [20], which is not under `paper/`.
- A definition of a "strong" Ca2+ response (Fig 6B). The 28% and 5.9% fractions are blocked unless the dataset or a reader's answer gives one.
- Eq. 2 comes out garbled in the extracted text. The Fig 5B criterion therefore shows its literal form and a form normalized so that an intact membrane gives f = 1.5.
