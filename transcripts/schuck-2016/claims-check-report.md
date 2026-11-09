The claims file is ready for an attempt. I changed only `claims/crcns-ofc-4/10.1016-j.neuron.2016.08.019.yaml` and did not commit.

**Checker result:** `29 claims, 29 quotes, 47 statistical values, 2 problems`. Both problems are the confidence-interval bounds of `fig4a-decoding-error-correlation` (-0.8432 and -0.0169). They are in the paper; the text shows them with a garbled minus sign ("[�0.8432, �0.0169]"), so the values are correct.

**Changes, by claim:**
- **behavior-error-rate:** The criterion counted time-outs as errors, which the paper does not say. Time-outs are 0.3% of trials, more than the 0.23 tolerance, so counting them or not is now an open reading with both versions.
- **supp-errors-stable-over-blocks:** Added the reason for judging this on the linear mixed model: the Methods name lmer, which fits linear models.
- **fig2b-hidden-components:** The paper's numbers disagree. A t26 above 3 gives a one-sided p below 0.003, not the reported 0.014 or 0.007. The bootstrap of Figure S2B is now a second reading.
- **fig2b-current-age-absent, fig2b-two-back-absent:** The paper does not name the test behind p > 0.72 and p > 0.66, so the statistics no longer call it a t-test. The criterion still judges on the t-test the Results imply, with the bootstrap shown as a variant.
- **figs2c-8way-decoding:** The current-category tolerance was 5.5; 10% of 55.5 is 5.55.
- **figs2a-permutation-control:**
  - The component tolerances (0.14 to 0.17 points) rested on a weak reason, so they are now the default 10% of the value.
  - The statement covers all four components, but the criterion only judged the 16-way result. It now judges all four.
- **synthetic-data-control:** For the participant peak locations, the Methods cite Figure S5, which is the Euclidean-distance figure. The claim had silently read Figure S3C instead. Both the conjunction peak and the 16-way searchlight peak are now named as readings. Restricting the simulation to the OFC mask is recorded as a deviation.
- **fig2d-enter-nonenter-decoding:** The criterion said the Figure 2 legend states one-sided tests, which it does not. The citation now points to the Results for Figure 2B and to the Figure S2 legend.
- **other-rois-incomplete:** The statement called the PPA/FFA relation "weaker", which the paper does not say, and it mixed two analyses. It now states the decoding-and-error-rate correlation and the similarity analysis separately, as the paper does.
- **fig4b-error-vs-matched:** Noted that the paper's t24 does not fit the 24 participants in the error analyses. Trial -1 is now reported against p = 0.07.
- **supp-motor-action-not-in-ofc:** The paper does not say which accuracy or which test gives the OFC result (p = .40). Two readings are named: 16-way accuracy against 6.25%, and the motor-response component against 50%.

**What remains open:**
- **fig3-searchlight-conjunction:** The main text puts the peak in the left medial orbital gyrus at x = 3, while Table S1 lists the right rectal gyrus. The data set cannot test this claim either way.
- **Nuisance regressors:** The paper's GLM used 26 cardiac regressors in SPM8. These cannot be rebuilt from the data set as its description gives it; this is already recorded as O5 in the header.
- **Coverage:** Decoding of the response mapping in visual cortex (Figure S3B) has no claim. I left it out because it is an exploratory supplementary result.

**Ready:** yes. The new `checks` entry is marked `ready: true`.
