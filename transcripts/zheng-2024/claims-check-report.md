The checker's result line: `claims/zheng-2024.yaml: 32 claims, 32 quotes, 43 statistical values, 0 problems`. It printed the same before and after my edits.

**Changes, by claim:**
- **figs4g-population-vectors-gradual:** the expected value 0.65 ± 0.065 did not cover the stated widened range of 0.54 to 0.77. It is now 0.655 ± 0.115. The n values are now given in words with their unit.
- **fig3k-switch-abrupt:** the expected value is now 0.761 ± 0.086, so it matches the range of 0.675 to 0.847.
- **figs12-stability-after-switch-on:**
  - The statement said switch-ON fields have less location jitter against both windows. The novel middle window has p = 0.4, so the statement now names that exception.
  - I added the six location-SD medians from the legend to `expected`, and the criterion now judges location as well as CV.
  - The criterion said the choice of the five "middle" trials could not change the outcome. That is wrong, since novel CV has p = 0.019. Two readings are now named.
- **fig5c-switchiness-not-intrinsic:** matching fields across environments was listed as an equal reading. The legend and the Methods make the unit a neuron (n = 955), so the field-matched version is now a variant only.
- **figs13-btsp-signatures:** I added the Figure S13B within-position control that the Results cite. The rate normalisation in S13D is now named as open, with two readings.
- **figs14-preexisting-fields-ephys:** the selection quantity differs between the Results (average within-field peak rate) and the legend (mean rate). Both are now named as readings.
- **figs8-speed-no-trend:** the criterion now says whether a clear speed-switching correlation blocks reproduction. It also states that the |r| > 0.1 threshold is chosen here, not taken from the paper.
- **fig2d-switch-fractions:** the partial criterion said "four fractions" but counted six. It now names the four ON and OFF fractions.
- **fig3df-step-beats-polynomial-fields:** the expected quantity now says 0.96 is a lower bound, so its zero tolerance can't be read as "exactly 0.96".
- **fig1e-novel-drift-faster:** I added a sign convention for Cohen's d. **fig1e-later-lags-no-difference:** n is now given in words.

**Still open (recorded in `checks`):**
- Some thresholds are the writer's own choices, labelled as such, because the paper reports no test:
  - fig1h: the "twice as steep" factor.
  - fig6f: the 95th-percentile reading of "up to 5%".
  - fig3df-population, fig4-behavior and fig4no-head-scans: the rules and default tests.
- I could not verify the code details the file cites from the Zenodo repository, because the code is not under `paper/`.
- Figures S1A/B, S7 and S11 have no claim. They are minor control findings, not main ones.

All main findings have a claim, and every claim comes from this paper. The file is ready: `ready: true` is in the new checks entry. Nothing is committed.
