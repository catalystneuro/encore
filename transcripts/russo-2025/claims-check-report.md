The claims file is ready for an attempt. I made 16 corrections, all taken from the paper and its Source Data file, and recorded 5 open points. Only `claims/russo-2025.yaml` changed; nothing was committed or pushed.

**Checker result:** `claims/russo-2025.yaml: 39 claims, 39 quotes, 85 statistical values, 1 problems`. The one flag is `VALUE NOT FOUND fig4e-model-latencies 0.000111`. The Figure 4E legend prints "p = 1.11e-04", so the value is right and only the format differs. I left it.

**Main problem found:** the file said the Source Data gives per-subject values for the human claims. That is true only for the sheets for Figures 1A, 1B, S2G, S3A and S3B. Sheets S1A, S2A, S2C, S2D and S2E hold only box-plot summaries (minimum, quartiles, median, maximum). So several of the planned tests cannot be run.

**Changes, by claim**
- **Header:** now says which sheets have per-subject values and which have only summaries.
- **fig1a-tms-late-rest-active, fig1b-ieeg-late-rest-active:** the PLF part is now judged by comparing the rest and active medians, and the PLF test is recorded as not testable. In fig1b, the "four of five subjects" rule is now marked as this file's, not the paper's. The paper's means are over contacts, so the per-subject means (5.28 and 3.95) are not expected to match them.
- **figs2-tms-controls:** only the S2G signed-rank test (no difference between hand closing and opening) can be rerun. Passive movement and cycling are judged on medians. The absence of modulation for posterior TMS and median nerve stimulation is not testable.
- **figs2a-tms-early-component:** judged on medians only; the means, tests and correlation are not testable.
- **figs3b-ieeg-early-no-modulation:** a signed-rank test on 5 pairs can never reach p < 0.05 (its smallest possible p is 0.0625). The substitute test therefore cannot find an effect; the criterion now says so and asks for the per-subject differences.
- **fig1d-lfp-late-rest-larger:** notes that the Source Data sheets for Figures 1D and 1E have 12 pairs each, while the legends say n = 13.
- **figs4-intensity-dependence:** added three results from the Figure S4 legend that the criterion uses: LFP high and intermediate intensity, and CSD high, all p < 0.001.
- **speed-threshold-robust:** removed the minimum of 10 trials per state, which the paper does not set. A session now needs at least one trial in each state; the 10-trial cut is kept as a variant.
- **figs5-early-component-mouse:** the statement said the early CSD response is larger during running. The legend gives no direction, and the Source Data medians are higher at rest (1.8 against 1.5). The claim now requires only a difference and reports its direction.
- **figs7a-active-shorter-latency:** the criterion required a state-factor ANOVA result the paper never reports. That test is now reported but does not decide the claim. The statistics entry now says the legend's p < 0.001 refers to significance lines it doesn't name.
- **fig3a-thalamic-rate-higher-active:** the Source Data has 1439 rest and 952 active values, which cannot be paired; the file had described them as "over a thousand pairs". Added a per-trial reading that matches this.
- **fig3e (baseline, LF synchrony, HF frequency):** the Source Data values are per trial and match the paper exactly. Pooling the HF and LF baseline values gives 6.78 and 12.48 Hz, the paper's numbers. In the HF columns, the "ROV" and "Resp Freq" labels appear swapped: the "ROV" column holds the paper's HF frequency (309.65 ± 126.7). This is noted for the author.
- **figs8b-opto-cortical-inhibition-minimal:** added the test from the Figure S8B legend (Wilcoxon signed rank tests, all p < 0.001), which shows the small shifts are statistically significant. It is reported but does not decide the claim, which is about the size of the shift.

**Still open**
- **triphasic-pattern:** the paper doesn't say how the 127.8 ms silence was measured. Both readings are the file's own, and one uses a "baseline minus 2 SD" threshold that is not in the paper.
- **figs9-mos-rate-no-modulation:** the file uses only regular-spiking (RS) units, but the legend just says "MOs units".
- **fig2h-opto-gaba-suppresses-both:** the paper does not define the baseline the light window is compared against.
- **fig2b-thalamus-leads:** the paper doesn't say whether the post hoc test is pooled over state or run within each state.
- **No claim:** some minor supplementary results have none (Figures S1C, S2F, S3A, S9C and S9D, S10B). Every main finding has a claim, and all claims come from this paper.
