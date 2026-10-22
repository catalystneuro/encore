I wrote the claims file at `claims/001516/10.1016-j.bioelechem.2026.109283.yaml`. The quote checker reports 32 claims, 32 quotes, 9 statistical values and 0 problems. Nothing was committed.

**Text read:** the version of record, extracted from a PDF supplied by a person. It covers the main text, Methods, Results, Discussion and the legends of Figures 1 to 7. The paper has no supplement. It links no code ("Data will be made available on request"), and its analysis software (MetaMorph, an Excel macro, Grapher, Origin) is not published, so no code was read.

**What the dandiset holds:** its title and description point at the two-pulse recovery experiments of Fig. 7. The description differs from the paper in two ways, both named in the opening comment:
- It gives 20 sham and 40 pulse exposures per cell; the paper's Methods give 40 baseline and 60 pulse images.
- It says the interval between pulses varied; the paper reports only 5 µs.

The criteria test only 5-µs sets. If the data hold 20 and 40 images, they are averaged from the images present, and that is recorded as a deviation.

**How the file was built:** the same paper has checked claims for dandisets 001517 and 001518. I checked the 001517 claims against the paper, kept them, and made these changes:
- I added `fig7a-cosine-profiles`, the shape of the Fig. 7A test-pulse profiles.
- The `fig7b` criterion now says the top-panel data are the Fig. 4B cells, as the Results state. Single-pulse sets inside the recovery recordings count as a variant only.
- In `fig7ab`, two forms of the t-test (against a fixed 100%, or paired against the same cell) can each be read as the paper's test. A claimed absence now has to hold under both, or the claim is blocked as `methods_underspecified`.

**Counts:** 32 claims, all with quotes. 7 report statistics, 19 have expected values and all 32 have criteria. 9 claims need outside input: the charging time constant against cell radius, which the paper takes from its reference [20].

**Details the paper leaves open, and the readings named:**
- **Background subtraction for the laser images:** none, or a cell-free region as for the Ca²⁺ images.
- **How cell radius is measured:** perimeter divided by 2π, or the circle of equal area.
- **Start and end of a set:** the first and last image, or the first and last 10.
- **Paired or unpaired Student's t-test:** in Fig. 4, Fig. 5A and the equator claim.
- **Two-sided t-test in Fig. 7:** against a fixed 100% value, or paired against the same cell.
- **Normalization and pole in Fig. 7B:** per cell or of the means; each pole or their mean.
- **Cosine comparison in Fig. 7A:** against the profile's own fit, or the 150/150 benchmark.
- **The ~20% drop in Fig. 2D:** which pole, the reference set, and per set or pooled.
- **Which datapoints the Gd³⁺ comparison uses.**
- **Eq. 2 reduction:** relative to 1.5, or to the intact f.
- **Fig. 7C:** whether fully resealed points count among "most datapoints".
- **Correlation coefficient in Fig. 3:** Pearson r, or from the fit through the origin.
- **LOESS span in Fig. 3:** 0.3, 0.5, 0.75, or 50-mV bins.
- **Ca²⁺ windows:** peak or last 30 s for Fig. 6A; last frame, last 10 s or last 30 s for Fig. 6B.
- **"Strong" Ca²⁺ response:** 3 s.d. above baseline, 50%, or 100%.

**Missing from the paper:**
- The fit of time constant against radius (reference [20], not read).
- A definition of a "strong" Ca²⁺ response.
- Any test for "follows a cosine" or "nonlinear".
- The protocol of 20 and 40 images and the varied intervals that the dandiset describes.

The checked 001517 file also flags that Eq. 2 with the Methods' constants gives about 1.2% for a 10-fold rise in conductivity, against the paper's ~2%. That claim is kept as the paper states it.
