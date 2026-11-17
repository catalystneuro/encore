**Verifier report, round 1: Elie & Theunissen 2019 on CRCNS aa-4**

The claims file has 26 claims. The notebook tests one, fig1-model-neurons, and blocks the other 25.

### A. Outcomes

| claim id | my outcome | reason |
|---|---|---|
| units-404 | blocked (methods_underspecified) | Cell 12: 1281 files are labelled single units, 1246 of them with I_AR ≥ 2.3. No file, the data description or the CRCNSCode folder lists the 914 or the 404 units. The criterion's reading (b), redoing the 2015 decoding, was not attempted, and the 914 count was not even approached (B1). |
| units-337 | blocked (methods_underspecified; too_large also applies) | Depends on units-404. Cell 15 estimates about 124 h on one core for the KDE rates alone. |
| s1-temporal-resolution | blocked (methods_underspecified) | Depends on units-404. The variant on 1246 units (cell 18: 65.8 ± 19.0% below 50 Hz, 1245 units losing more than 5%) decides nothing. The power part was not computed at all. |
| fig1-model-neurons | partially_reproduced | Cell 21, temporal neuron: mean \|KDE − model\| is 0.009 spikes/ms (< 0.02); bias-corrected peak instantaneous information is 0.519 bits (0.500 uncorrected; within 0.5 ± 0.05); cumulative information reaches 1.928 bits (≥ 1.8). The MATLAB tutorial's saved results agree (0.502; 1.894). The rate and onset neurons are not in the repository, so "each model neuron" holds for one of three. |
| fig2a-poisson-test | blocked (methods_underspecified) | Depends on units-404. No variant was run. |
| fig2cd-fano-factor | blocked (methods_underspecified) | Depends on units-404. The variant on 1246 units gives 1.027 (SEM 0.002), significantly different from 1; it decides nothing. |
| fig2b-noise-correlations | blocked (methods_underspecified) | Depends on units-404. The variant gives a noise-correlation median of 0.152, outside the ±0.05 band, and a stimulus-correlation median of 0.29 (over stimuli) or 0.24 (within stimulus); it decides nothing. |
| fig3-5-example-neurons | blocked (methods_underspecified) | The paper does not name the units. The S4 to S6 raster images are not in the materials, and the notebook shows no attempt to match them, which the criterion allows. |
| fig6a-onset-sustained-information, fig6c-new-information, fig6b-fixed-rate-fraction, fig7a-time-constants, fig7b-k300, k300-rate-regression, fig9a-mean-cii, fig9a-top-quartile, s7-invariant-information, fig9b-cii-tau-ratio, fig9c-cii-k300, cii-unimodal | blocked (methods_underspecified; too_large also applies) | Each depends on units-337, directly or through fig7a or fig9a-top-quartile, and units-337 is blocked. |
| table1-anatomy-counts, fig10-cii-distance, fig10-cii-area-anova, fig10-tau-k300-distance, fig10-no-anatomy-categorical | blocked (methods_underspecified) | All depend on units-337. The notebook's own reason ("no anatomical location in the data set") is not shown: the `extra_info` group was never opened (B3). |
| s2-spike-counts | blocked (methods_underspecified) | Depends on units-404. The variant on 1246 units gives max 9, 442 bins at 8, and a mean of 0.132; it decides nothing. |

No claim states a chance level for a selection, so there was no chance level to compare.

### B. Problems

1. **[does not affect a conclusion] Cell 13 says the `.f32` snippet files are undocumented. They are documented.** `CRCNSCode/h5_plot_one_spike.m`, inside the archive's `CRCNSCode.tar.gz`, reads them: 18 float32 samples per snippet, indexed by the `spike_ids` that `read_unit` already loads. That makes the 2015 SNR > 5 criterion, and so the 914 count, computable at least for the sites that have snippets. The notebook also never shows which sites have `.f32` files. The outcome stays blocked because the 404 still needs the 2015 decoding.

2. **[does not affect a conclusion] Cell 12 skips a check against the data description.** The description gives 1401 spike-sorted auditory units at I_AR ≥ 2.3. The notebook never counts the `_ss` files (any `sortType`) at that threshold, which would test whether its I_AR reading matches the authors'.

3. **[does not affect a conclusion] `read_unit` does not support the anatomy blocking reason.** It records only that `extra_info` exists (`has_extra_info`) and never reads its contents. "No anatomical location in the data set" is therefore unverified. The anatomy claims are blocked anyway through units-337.

4. **[does not affect a conclusion] `read_unit` contradicts the module docstring on stimulus selection.** The docstring says call stimuli come from "the unit's Call group", but the code takes stimuli of type call or song from every group, including Sel1–7, Mask1 and STRF1. This may explain why cell 4 finds 95.4 call stimuli per unit against the paper's 114, and 1874 unit-stimulus pairs with 12 trials against the description's maximum of 11. It affects only the non-deciding variants of cell 18.

5. **[does not affect a conclusion] `cum_info_mc` with `groups` is wrong when categories have unequal sizes.** It mixes a stimulus-weighted p(y) with category-weighted conditional entropies. I checked it against exact enumeration on a synthetic case (5 stimuli in groups {0,0,0,1,2}, 3 bins):

   | | bin 1 | bin 2 | bin 3 |
   |---|---|---|---|
   | exact | 0.101 | 0.424 | 0.686 |
   | `cum_info_mc` | −0.036 | 0.350 | 0.717 |

   It also disagrees with `inst_info` at bin 1. The stimulus version matches exact to about 0.001 bits. Category cumulative information is not used for any outcome here, but it would bias every category claim if those were run.

6. **[does not affect a conclusion] Cell 21 departs from Method I in three ways:**
   - It uses a fixed 200,000 samples instead of the code's adaptive chunks targeting 0.2 bits.
   - It uses jackknife SE instead of 20 bootstraps of the jackknife.
   - It never applies the 0.6-bit stopping rule.

   Its common-random-numbers assumption decides the curve: with independent draws the curve goes to 2.206 bits, above the 2-bit maximum, and ends at 0.803. The fig1 conclusion still stands because the MATLAB tutorial's saved results (peak 0.502, last 1.894) agree with the common-random-numbers run.

7. **[does not affect a conclusion] Cell 18: the coherence variant uses the stored `class_info` curve, which runs from 4 to 496 Hz.** That may not be the S1 Fig computation, so the 65.8% says nothing about the paper. The power part of s1 is not computed.

8. **[does not affect a conclusion] Cell 15: the cost argument is a valid second reason (too_large) for the 337-dependent claims, but the notebook does not name it as a blocking reason.**

I found no place where the claims file misreads the paper for the claims at issue.

### C. What I could not check, and the output that would have let me

- **Anatomy in the files:** a dump of the keys and attributes of one `extra_info` group, and of one `class_info` group beyond coherence.
- **Stimulus selection:** per-group counts of stimuli with type call or song (Call, Call1–3, Sel*, Mask1, STRF1), and whether the same `stim_md5` appears in more than one group for a unit.
- **The 914 route:** a count of `.f32` files per bird and site, and the SNR distribution for the units that have them.
- **The 1401 check:** the count of `_ss` files of any `sortType` with I_AR ≥ 2.3.
- **fig3-5:** a comparison against the S4 to S6 Fig images, or a statement that they were inspected and could not be matched.
- **fig1 under the paper's procedure:** the cumulative information with the code's adaptive sample size, its bootstrap error and the 0.6-bit stop. That would settle whether the 1.8-bit result depends on the common-random-numbers assumption.

The other 25 claims were not run by the notebook, so I could form no outcome on them beyond blocked. To check the archive I listed the S3 bucket and opened only the 389 KB `CRCNSCode.tar.gz`; no bird data was downloaded.
