I checked the claims file for DANDI:001950 (`claims/001950/10.1038-s41586-026-11026-0.yaml`) and it is ready for an attempt. I made 13 changes and three problems remain open. Nothing was committed.

**Checker result**, run against the preprint text: `39 claims, 38 quotes, 37 statistical values, 2 problems`. The two problems are p = 3.0e-4 for `fig5g-switch-dorsal` and `fig6a-outcome-space`. The paper prints these as "3.0 × 10 −4" (Figure 5g and 6a legends), so the values are right. I ran the checker on the preprint because the version-of-record text under `paper/` holds only the abstract and references. Against that text, nearly every quote fails. Every quote matches the preprint word for word.

**Changes, by claim**
- **Wrong paragraph in `source`:** in the section "Spatial variation of LC-NE activity", the paragraph number was one too low, now fixed:
  - `fig4c-choice-history` is paragraph 3.
  - `fig4g-go-cue-excitation` is paragraph 6.
  - `fig5a-engagement-reward-history`, `fig5b-baseline-predicts-ignore`, `fig5c-ignore-ventral` and `fig5d-ignore-on-anatomy-axes` are paragraph 7.
  - `fig5g-switch-dorsal` and `fig5h-switch-on-anatomy-axes` are paragraph 8.
  - `fig5k-cortical-input-switch` is paragraph 9.
  - `fig6i-axons-rpe` and `fig6j-cortical-input-more-positive` cited paragraph 4 of a section that has three; now paragraph 3.
- **`fig2c-primary-targets`:** the criterion used a spinal cord column that Figure 2c does not have, and it required negative correlations, which the paper never states. It now uses P and MY with correlations at or below zero, marked as a standard choice.
- **`fig2ef-dorsal-ventral-projections`:** the criterion now also covers the single-neuron reconstructions (Figure 2e), which the statement relies on. The comparison of medians is marked as a standard choice.
- **`iti-mean`:** the interval now runs from the end of the trial to the next cue onset. A full cue-to-cue interval cannot be as short as the reported 1.1 s minimum. Whether no-go cues count as cue onsets is named as open, with both readings.
- **`figs15f-tonic-modulation-vs-engagement`:** the statement claimed a direction for the second panel that the legend does not give. It is restated as the two correlations the legend reports.
- **`figs17i-baseline-axons-vs-spiking`:** the Methods describe a different sign test (a two-proportion z-test with a label permutation) from the legend's Fisher's exact test. It is added as a variant.
- **`fig6g-rpe-vs-no-reward-populations` and `fig6h-opposing-behavior`:** the quartile binning had no source. Quartiles are now cited to Figure 6d, and the binning of 6g and 6h is marked as not stated.
- **`figs16-pupil-spiking`:** added the Methods' autocorrelogram details: the 0.5 s sliding window, the excluded periods and the fitted curve.
- **Added `fig1-dense-axon-distribution`** (Figure 1c to 1e, data held elsewhere) **and `fig5e-switch-history`** (Figure 5e, testable on the dataset). Both are main-figure findings that had no claim.

**Still open**
- **`fig6j-cortical-input-more-positive`:** the paper does not say which t-statistic is "more positive". The criterion's use of the outcome t-statistic is one reading.
- **`figs18d-outcome-not-on-anatomy-axes`:** the legend does not say which two of the three axes its r values belong to. The criterion accepts either pair, which is lenient for a claim that there is no effect.
- **The paper's code:** I did not re-read it. The criteria's citations of `aind-beh-ephys-analysis` at commit 971c1ca are taken as written.

**Ready:** yes. The `checks` entry is appended with `ready: true`, one line per change and one per open problem.
