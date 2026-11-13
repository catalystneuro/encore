The claims file is fit for an attempt (`ready: true`). Only `claims/danish-2017.yaml` changed, and nothing is committed or pushed.

**Checker:** `claims/danish-2017.yaml: 26 claims, 26 quotes, 10 statistical values, 0 problems` (the same before and after my edits).

**Changes, by claim**
- **lesion-directed-song-abolished:** The paper shows this only by video and gives no measure. I marked the criterion as open and labelled the spectral-correlation test as the reader's own reading.
- **lesion-undirected-rate-similar:** The paper doesn't say which days are compared, so I added two readings: first post-lesion day against last pre-lesion day, or all days against all days.
- **fig2g-maturity-index-drop:** The note on the Wilcoxon test was wrong. An exact two-sided test needs 7 birds to reach p < 0.025 (a one-sided test needs 6), not 6. I also named Aronov et al. 2008, which the Methods cite, as the source for open details.
- **fig2f-closer-to-exponential:** I named ref 41, which the Methods cite for this analysis, as the definition of the scale of Gamma where it gives one.
- **fig2e-rhythmicity-drop:** The spectrum was credited to Chronux. The Song rhythmicity section names the Matlab FFT function, with 1 taper and time half-bandwidth product 2, so I corrected that.
- **fig3-antidromic:** The statement said "thresholds". The paper says these intensities "could elicit" responses, so I reworded it. I also noted that the Methods give 50 to 200 uA against the Results' 70 to 300 uA, so the paper disagrees with itself.
- **single-unit-spontaneous-rates:** I restored the paper's hedge: units outside the core "appeared to exhibit" lower rates.
- **spectral-features-weak:** The paper doesn't define the six features; it only cites ref 49. The criterion now says so and marks the Sound Analysis Pro definitions as an assumption.
- **fig7d-10hz-coherence:** The 3 to 30 Hz search window isn't from the paper, so I labelled it a standard choice.
- **fig9-long-syllable-gamma:** "Coherent over most of 1 to 55 Hz" could not decide an outcome. I replaced it with an unbroken significant range from 1.1 to 49.5 Hz (each bound moved inward by 10%). I also noted that the criterion combines the Fig 9 legend's band with the null the Methods give for the neural spectrum.
- **no-motif-bout-signal:** The criterion called its t-test at p < 0.05 "the test level of Fig 6". Fig 6 actually reports a paired t-test result at p < 0.01, so I relabelled the test as a standard choice.
- **Header:** The paper gives no number of shuffles for the shuffled baseline, so I labelled the 1000 a standard choice.

**Open (recorded in the check entry)**
- **figs1-control-lesions-no-effect:** With 4 birds, an exact Wilcoxon test can never reach p < 0.05, so this claim of absence cannot fail under its criterion. The paper reports p > 0.50, and the protocol doesn't settle whether that bound should decide the outcome.
- **fig6-dip-before-offset:** The paper prints p < 0.01 only next to the onset increase. Recording it for the offset decrease is a reading of the sentence.
- **Lesion measures (M, Gamma, R):** The paper doesn't say which pre-lesion day it used.

Every main finding has a claim, and every claim comes from this paper.
